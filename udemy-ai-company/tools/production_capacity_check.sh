#!/usr/bin/env bash
set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CPU_COUNT="$(nproc 2>/dev/null || echo 1)"
LOAD_AVG="$(cut -d' ' -f1-3 /proc/loadavg 2>/dev/null || echo 'unknown unknown unknown')"
LOAD_1="$(cut -d' ' -f1 /proc/loadavg 2>/dev/null || echo 0)"
MEM_AVAILABLE_MB="$(free -m 2>/dev/null | awk '/^Mem:/ {print $7}')"
MEM_TOTAL_MB="$(free -m 2>/dev/null | awk '/^Mem:/ {print $2}')"
SWAP_USED_MB="$(free -m 2>/dev/null | awk '/^Swap:/ {print $3}')"
DISK_USED_PCT="$(df -P "$ROOT_DIR" 2>/dev/null | awk 'NR==2 {gsub("%", "", $5); print $5}')"
FFMPEG_COUNT="$(pgrep -fc 'ffmpeg' 2>/dev/null || true)"
VOICEVOX_COUNT="$(pgrep -fc 'voicevox|VOICEVOX|/opt/voicevox_engine' 2>/dev/null || true)"

MEM_AVAILABLE_MB="${MEM_AVAILABLE_MB:-0}"
MEM_TOTAL_MB="${MEM_TOTAL_MB:-0}"
SWAP_USED_MB="${SWAP_USED_MB:-0}"
DISK_USED_PCT="${DISK_USED_PCT:-0}"
FFMPEG_COUNT="${FFMPEG_COUNT:-0}"
VOICEVOX_COUNT="${VOICEVOX_COUNT:-0}"

LOAD_OVER_CPU="$(awk -v loadv="$LOAD_1" -v cpu="$CPU_COUNT" 'BEGIN { print (loadv >= cpu) ? 1 : 0 }')"

CPU_JOB_RECOMMENDATION="1"
REASON="CPU job slot is available."

if [ "$DISK_USED_PCT" -ge 85 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="Disk usage is at or above 85 percent."
elif [ "$MEM_AVAILABLE_MB" -lt 700 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="Available memory is below 700 MiB."
elif [ "$SWAP_USED_MB" -gt 1200 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="Swap usage is above 1200 MiB."
elif [ "$FFMPEG_COUNT" -gt 0 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="ffmpeg is already running."
elif [ "$VOICEVOX_COUNT" -gt 0 ] && [ "$CPU_COUNT" -le 2 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="VOICEVOX is running on a 2 vCPU host."
elif [ "$LOAD_OVER_CPU" -eq 1 ]; then
  CPU_JOB_RECOMMENDATION="0"
  REASON="Load average is at or above CPU count."
fi

cat <<REPORT
# Production Capacity Check

- Timestamp: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
- Root: $ROOT_DIR
- CPU count: $CPU_COUNT
- Load average: $LOAD_AVG
- Memory total: ${MEM_TOTAL_MB} MiB
- Memory available: ${MEM_AVAILABLE_MB} MiB
- Swap used: ${SWAP_USED_MB} MiB
- Disk used: ${DISK_USED_PCT} percent
- ffmpeg process count: $FFMPEG_COUNT
- VOICEVOX process count: $VOICEVOX_COUNT

## Recommendation

- Start new CPU-heavy production job: $CPU_JOB_RECOMMENDATION
- Reason: $REASON

## Running Production Processes

REPORT

pgrep -af 'ffmpeg|voicevox|VOICEVOX|/opt/voicevox_engine' 2>/dev/null || true

cat <<'REPORT'

## Top CPU Processes

REPORT

ps -eo pid,ppid,stat,pcpu,pmem,etime,comm,args --sort=-pcpu 2>/dev/null | head -n 12
