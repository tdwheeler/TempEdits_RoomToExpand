
# Project Name: Audio Filter Example

## Document Details
- **Version:** 1.0
- **Author:** [Your Name Here]
- **Date:** November 24, 2024

## Project Overview
### Purpose
This TouchDesigner project processes audio input data to apply real-time filtering and visualize changes. The pipeline demonstrates how to integrate audio processing with Kinect Azure for interactive projects.

### Key Features
- Integration with Kinect Azure for motion data.
- Real-time audio filtering and visualization.
- Configurable parameters for data scaling and lag.

### Hardware Requirements
- Kinect Azure for motion tracking.
- Audio interface for high-quality audio input and output.

## Node Graph Overview
### Diagram
![Complete Node Network](5_audio%20filter%20example.toe.png)

### General Flow Description
The project captures audio input and applies filters, with visualizations controlled by Kinect Azure motion data. The pipeline ensures real-time processing for interactive audio-visual installations or performances.

## Detailed Node Descriptions
### Nodes Listing
#### `kinectazure1`
- **Type:** Kinect Azure
- **Description:** Captures motion data for controlling parameters.
- **Parameters:** 
  - Sensor: `000233924512`
  - Depth Mode: Wide Binned
  - Data Output: Position and Depth
- **Inputs/Outputs:** Outputs to `null1`
- **Custom Parameters:** None

#### `audiofilein1`
- **Type:** Audio File In
- **Description:** Streams audio data for filtering and visualization.
- **Parameters:** 
  - File: `audio/sample_input.wav`
  - Play Mode: Locked to Timeline
- **Inputs/Outputs:** Outputs to `audiofilter1`
- **Custom Parameters:** None

#### `audiofilter1`
- **Type:** Audio Filter
- **Description:** Applies filtering to the audio data.
- **Parameters:** 
  - Frequency Cutoff: 200 Hz
  - Filter Type: Low-pass
- **Inputs/Outputs:** Inputs from `audiofilein1`; outputs to `audiodevout1`

#### `audiodevout1`
- **Type:** Audio Device Out
- **Description:** Sends processed audio to the output device.
- **Parameters:** 
  - Driver: ASIO
  - Device: Focusrite USB
- **Inputs/Outputs:** Inputs from `audiofilter1`

#### `lag1`
- **Type:** Lag
- **Description:** Smoothens motion data for controlling parameters.
- **Parameters:** 
  - Lag Time: 0.5 seconds
- **Inputs/Outputs:** Inputs from `math1`; outputs to `math2`

#### `math1`
- **Type:** Math
- **Description:** Normalizes Kinect Azure data.
- **Parameters:** 
  - Scale: `-1.0 to 1.0`
- **Inputs/Outputs:** Inputs from `select1`; outputs to `lag1`

#### `null1`
- **Type:** Null
- **Description:** Passes Kinect Azure data for further processing.
- **Inputs/Outputs:** Inputs from `kinectazure1`; outputs to `out1`

#### `out1`
- **Type:** Output
- **Description:** Final output for processed data.
- **Inputs/Outputs:** Inputs from `null1`

## Dependencies and External Files
### List of External Files
- **Audio Files:** Stored in `/project/audio/` for testing.

### Dependencies
- Requires Kinect Azure SDK for motion data processing.
- Professional audio interface supported by ASIO drivers.

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** Realtime

### Environment Settings
- Set environment variable `TOUCHDESIGNER_ENV` to `development`.

## Performance Considerations
### Optimization
- Viewers disabled to optimize resource use.
- Audio processing nodes configured for low latency.

### Performance Metrics
- Stable 60 FPS with hardware meeting requirements.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-24 | Initial release.             |

## Appendices
### A. Code Snippets
```python
# Example Python code for parameter updates
op('audiofilter1').par.freq = op('lag1').par.value0
```
