<div align="center">
  <img src="https://github.com/lorenzopaoria/Smoking-detection-and-distance-analysis/blob/7166f993e1fcce8dee768ad3523857a733f61be1/Logo/logo.jpg"/>
</div>

# Smoking detection and distance analysis

## Overview
This project implements a smoking detection system using object detection techniques with YOLOv11 to identify cigarettes, smokers, and non-smokers in images.

## Dataset
**Source**: [Smoking Detection Dataset on Roboflow](https://universe.roboflow.com/alt-f4-dom2z/smoking_detection_v3_noisefree)

### Dataset Characteristics
- **Total Images**: Approximately 700 images
- **Annotation Type**: YOLO format
- **Classes**:
  - Cigarette
  - Smoker
  - Non-smoker
- **Image Qualities**: High-resolution, noise-free images
- **Environments**: Various settings (indoor, outdoor, different lighting conditions)

### Dataset Preprocessing
- Noise reduction
- Consistent annotation format
- Balanced class distribution

## Technical Details
- **Model**: YOLOv11
- **Framework**: PyTorch
- **Development Environment**: Google Colab

## Key Features
- Multi-class object detection (cigarettes, smokers, non-smokers)
- Distance calculation between detected entities ##TODO

## Requirements
- PyTorch
- torchvision
- YOLOv11
- Google Colab (recommended)

## Installation
1. Clone the repository
2. Open the notebook in Google Colab
3. Mount your Google Drive

## Usage
- Train the model on your annotated dataset
- Evaluate model performance
- Generate detections and calculate distances

## Performance Metrics
- Average Precision (AP)
- Average Recall (AR)
- Mean Average Precision (mAP)
