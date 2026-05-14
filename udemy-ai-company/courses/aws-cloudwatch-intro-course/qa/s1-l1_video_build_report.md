# S1-L1 Video Build Report

## Target

- Course: `aws-cloudwatch-intro-course`
- Lecture: `s1-l1`
- Output: `courses/aws-cloudwatch-intro-course/video/s1-l1/s1-l1.mp4`

## Ownership

- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## Result

- Status: PASS
- Slide count: 10
- Audio count: 10
- Duration seconds: 174.878254
- Size bytes: 5386270
- Resolution: 1920 x 1080
- Video codec: H.264
- Audio codec: AAC
- Faststart: true
- Frame check: `video/s1-l1/frame_check_87s.png`

## Build Command

```bash
python3 udemy-ai-company/tools/build_slide_audio_video.py \
  --course-root udemy-ai-company/courses/aws-cloudwatch-intro-course \
  --lecture s1-l1 \
  --fps 1
```

## Verification

- `ffmpeg` decode validation: PASS
- `ffprobe` duration and stream check: PASS
- `build_report.json`: recorded
- Midpoint frame extracted and visually checked

## Approval

Status: Ready for content QA and Drive upload

Approved By: AI-QA-01

