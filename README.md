# BoxInspect

BoxInspect is an AI-powered visual quality inspection system for detecting packaging defects in box products.

The system analyzes images of packaged boxes and detects defects such as:

- crushed_box
- torn_box
- seal_issue
- label_issue

The goal is to automate industrial packaging inspection and return a PASS / FAIL decision for each inspected box.

---

## Features

- Image upload for inspection
- Automated defect detection using computer vision
- PASS / FAIL decision logic
- Visual overlay of detected defects
- Batch inspection support

---

## Architecture

Frontend → FastAPI Backend → Inference Engine → Storage → Results

---

## Project Structure
boxinspect/
backend/ → API server
frontend/ → web interface
ml/ → training pipeline
storage/ → uploaded images

## Status
In development