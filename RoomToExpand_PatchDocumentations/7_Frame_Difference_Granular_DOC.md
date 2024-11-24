
# Project Name: Frame Difference Granular

## Document Details
- **Version:** 1.0
- **Author:** [Your Name Here]
- **Date:** November 24, 2024

## Project Overview
### Purpose
This TouchDesigner project processes Kinect Azure input to calculate frame differences for granular video analysis. It highlights changes in motion and generates output suitable for visual feedback and control.

### Key Features
- Real-time frame difference calculation.
- Integration with Kinect Azure for depth and motion data.
- Granular video output for interactive or analytical purposes.

### Hardware Requirements
- Kinect Azure for motion tracking and input.
- A GPU capable of real-time processing for video outputs.

## Node Graph Overview
### Diagram
![Complete Node Network](frame_difference.png)

### General Flow Description
The project captures video input via Kinect Azure and calculates frame differences using a caching mechanism. The differences are processed to highlight motion and output to OSC for integration with other applications or visual systems.

## Detailed Node Descriptions
### Nodes Listing
#### `kinectazure1`
- **Type:** Kinect Azure TOP
- **Description:** Captures video input from Kinect Azure.
- **Parameters:** 
  - Sensor: Kinect Azure
  - Image Mode: IR
- **Inputs/Outputs:** Outputs to `level2`.

#### `level2`
- **Type:** Level TOP
- **Description:** Adjusts brightness, contrast, and gamma of the Kinect Azure input.
- **Parameters:** 
  - Brightness: `1.91`
  - Gamma: `2.01`
  - Contrast: `1.14`
- **Inputs/Outputs:** Inputs from `kinectazure1`; outputs to `level3`.

#### `cache1`
- **Type:** Cache TOP
- **Description:** Stores frames for calculating differences.
- **Parameters:** 
  - Cache Size: `50`
  - Step: `3`
- **Inputs/Outputs:** Inputs from `level1`; outputs to `diff1`.

#### `diff1`
- **Type:** Difference TOP
- **Description:** Calculates frame differences to highlight motion.
- **Inputs/Outputs:** Inputs from `cache1` and `level1`; outputs to `blur1`.

#### `blur1` and `blur2`
- **Type:** Blur TOP
- **Description:** Smoothens the frame difference for better visualization.
- **Parameters:**
  - Blur1 Size: `31`
  - Blur2 Size: `6`
  - Pre-shrink: `5`
- **Inputs/Outputs:** Blur1 inputs from `diff1`, Blur2 inputs from `thresh1`.

#### `thresh1`
- **Type:** Threshold TOP
- **Description:** Applies a threshold to the blurred frame difference to highlight significant changes.
- **Parameters:**
  - Threshold: `0.104`
  - Soften: `0.005`
- **Inputs/Outputs:** Inputs from `blur1`; outputs to `blur2` and `comp1`.

#### `oscout1` and `oscout2`
- **Type:** OSC Out CHOP
- **Description:** Sends processed motion data via OSC for integration.
- **Parameters:** 
  - Address: `127.0.0.1`
- **Inputs/Outputs:** Inputs from `lag1` and `rename1`.

## Dependencies and External Files
### List of External Files
- None required for this patch.

### Dependencies
- Requires Kinect Azure SDK for motion tracking.
- OSC-compatible application for receiving output.

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** Realtime
- **Viewers:** Disabled for performance optimization.

### Environment Settings
- Environment variable `TOUCHDESIGNER_ENV` set to `development`.

## Performance Considerations
### Optimization
- Non-essential viewers are disabled to save GPU resources.
- Efficient caching reduces computational load.

### Performance Metrics
- Maintains 60 FPS on hardware with recommended specifications.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-24 | Initial release.             |

## Appendices
### A. Code Snippets
```python
# Example code for customizing OSC output parameters
op('oscout1').par.netaddress = '192.168.1.100'
```
