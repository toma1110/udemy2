# S1-L3 動画生成レポート

## Ticket

- Task ID: TASK-0020
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- 実施日: 2026-05-10

## Inputs

- Script: `udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md`
- Slides: `udemy-ai-company/courses/aws-slo-adoption-course/slides/s1-l3/slide_001.png` ... `slide_009.png`
- Audio: `udemy-ai-company/courses/aws-slo-adoption-course/audio/s1-l3/slide_001.wav` ... `slide_009.wav`
- Audio QA: `udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_audio_review_report.md`

## Output

- Final video: `udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l3/s1-l3.mp4`
- Segments: `udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l3/segments/segment_001.mp4` ... `segment_009.mp4`
- Representative frame: `udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l3/frame_check_90s.png`

## Build Settings

- Video codec: H.264 / libx264
- Video size: 1920x1080
- Frame rate: 30 fps
- Slide scaling: fit within 1920x1080 and pad to 16:9
- Audio codec: AAC
- Audio sample rate: 44100 Hz
- Audio channels: mono
- `-nostdin`: enabled
- `-movflags +faststart`: enabled

## Validation

| Check | Result | Notes |
| --- | --- | --- |
| Slide count | Pass | 9 PNG files |
| Audio count | Pass | 9 WAV files |
| Segment count | Pass | 9 MP4 files |
| Segment audio spec | Pass | all AAC mono 44100 Hz |
| Final video stream | Pass | H.264 1920x1080, 30 fps time base |
| Final audio stream | Pass | AAC mono 44100 Hz |
| Duration | Pass | 189.982 sec |
| File size | Pass | 8,044,300 bytes |
| Decode | Pass | `ffmpeg -v error -i s1-l3.mp4 -f null -` |
| Faststart | Pass | `moov` at byte 36, before `mdat` at byte 207639 |
| Representative frame | Pass | 90秒地点はSlide 5のCloudFormation説明で、台本内容と一致 |
| Git tracking | Pass | MP4、segments、frame_checkは`.gitignore`対象 |

## ffprobe Summary

```json
{
  "video": {
    "codec_name": "h264",
    "width": 1920,
    "height": 1080,
    "r_frame_rate": "30/1"
  },
  "audio": {
    "codec_name": "aac",
    "sample_rate": "44100",
    "channels": 1
  },
  "format": {
    "duration": "189.982268",
    "size": "8044300",
    "bit_rate": "338738"
  }
}
```

## Notes

- Slide 2のみ元PNGが1671x941だが、動画生成時に1920x1080へスケール・パディングしている。
- 音声の最終自然さ確認は、`s1-l3_audio_review_report.md` に記載したCEOスポット聴取ポイントを使う。
