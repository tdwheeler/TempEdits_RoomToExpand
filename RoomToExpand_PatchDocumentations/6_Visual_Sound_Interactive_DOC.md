
# Project Name: Visual Sound Interactive

## Document Details
- **Version:** 1.0
- **Author:** [Your Name Here]
- **Date:** November 24, 2024

## Project Overview
### Purpose
This TouchDesigner project combines visual and audio elements to create an interactive experience. The project utilizes Kinect Azure for motion tracking, processes audio inputs, and generates dynamic visualizations synchronized with sound and motion.

### Key Features
- Motion capture integration using Kinect Azure.
- Real-time audio analysis and visual modulation.
- Interactive controls for audio-visual effects.

### Hardware Requirements
- Kinect Azure for motion tracking.
- Professional audio interface for capturing high-quality audio inputs.
- A capable GPU for real-time rendering.

## Node Graph Overview
### Diagram
![Complete Node Network](visual_sound_interactive.png)

### General Flow Description
The project captures motion and audio inputs, processes the data, and outputs synchronized audio-visual effects. The node graph is organized to handle motion data via Kinect Azure and audio data through audio file inputs, which are then filtered, analyzed, and used to drive visual outputs.

## Detailed Node Descriptions
### Nodes Listing
#### `kinectazure1`
- **Type:** Kinect Azure
- **Description:** Captures motion data for visual modulation.
- **Parameters:** 
  - Sensor: Kinect Azure
  - Image Mode: Depth + Color
- **Inputs/Outputs:** Outputs to multiple processing nodes.

#### `audioplay1`
- **Type:** Audio Play CHOP
- **Description:** Streams audio for synchronization with visual effects.
- **Parameters:** 
  - File: `audio-samplesKick909.wav`
  - Timeslice: On
- **Inputs/Outputs:** Outputs to visual modulation nodes.

#### `math1`
- **Type:** Math CHOP
- **Description:** Processes and normalizes Kinect motion data.
- **Parameters:**
  - From Range: `0 - 1`
  - To Range: `-1 - 1`
- **Inputs/Outputs:** Processes data from `kinectazure1`; outputs normalized data.

#### `blur1`
- **Type:** Blur TOP
- **Description:** Applies a blur effect to visual outputs for smooth transitions.
- **Parameters:**
  - Blur Size: `5`
- **Inputs/Outputs:** Inputs from visual processing nodes; outputs to composite.

#### `comp1`
- **Type:** Composite TOP
- **Description:** Combines visual layers into a single output.
- **Parameters:** 
  - Composite Method: Add
- **Inputs/Outputs:** Combines multiple visual layers; outputs final visuals.

## Dependencies and External Files
### List of External Files
- **Audio Samples:** Located in `/audio_samples/` directory.

### Dependencies
- Kinect Azure SDK for motion tracking.
- Audio files for testing and live inputs.

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** Realtime
- **Viewers:** Disabled for performance optimization.

### Environment Settings
- Environment variable `TOUCHDESIGNER_ENV` set to `interactive`.

## Performance Considerations
### Optimization
- Heavy nodes, such as Kinect Azure processing, are carefully managed to avoid frame drops.
- Visual viewers are disabled unless needed during debugging.

### Performance Metrics
- Maintains a steady 60 FPS on a system with the recommended hardware.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-24 | Initial release.             |

## Appendices
### A. Code Snippets
```python
# Example of linking audio modulation to a visual parameter
op('comp1').par.opacity = op('audioplay1').par.volume
```
