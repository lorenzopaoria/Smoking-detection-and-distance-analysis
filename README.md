<div align="center">
  <img src="https://github.com/lorenzopaoria/Smoking-detection-and-distance-analysis/tree/048445ce72d1d1b292e1e2e7d6edac3a2aab296c/Logo"/>
</div>

# Smoking detection and distance analysis

## Overview
This project implements a smoking detection system using object detection techniques with Faster R-CNN to identify cigarettes, smokers, and non-smokers in images.

## Dataset
**Source**: [Smoking Detection Dataset on Roboflow](https://universe.roboflow.com/alt-f4-dom2z/smoking_detection_v3_noisefree)

### Dataset Characteristics
- **Total Images**: Approximately 500-1000 images
- **Annotation Type**: COCO format
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
- **Model**: Faster R-CNN with ResNet50 FPN backbone
- **Framework**: PyTorch
- **Development Environment**: Google Colab

## Key Features
- Multi-class object detection (cigarettes, smokers, non-smokers)
- Performance evaluation using COCO metrics
- Distance calculation between detected entities

## Requirements
- PyTorch
- torchvision
- pycocotools
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
