# Project Name: Audio-Visual Mixer

## Document Details
- **Version:** 1.0
- **Author:** John Doe
- **Date:** November 10, 2024

## Project Overview
### Purpose
This TouchDesigner project integrates live audio inputs with visual effects to create dynamic visualizations during live performances.

### Key Features
- Real-time audio analysis.
- Dynamic visual generation based on audio input.
- Output to multi-display setup.

### Hardware Requirements
- Kinect Azure for motion capture.
- Professional audio interface for high-quality audio input.

## Node Graph Overview
### Diagram
![Complete Node Network](path/to/diagram.png)
### General Flow Description
The project captures live audio and motion data, processes the information, and outputs synchronized audio-visual content. Audio data is filtered, analyzed, and then used to modulate various visual parameters.

## Detailed Node Descriptions
### Nodes Listing
#### `kinectazure1`
- **Type:** Kinect Azure
- **Description:** Captures motion data for audience interaction.
- **Parameters:** 
  - Depth Mode: High
  - Camera Index: 0
- **Inputs/Outputs:** Outputs to `select1`
- **Custom Parameters:** None

#### `audiofilein1`
- **Type:** Audio File In
- **Description:** Streams audio data from the connected interface.
- **Parameters:** 
  - File: `live_input`
  - Play Mode: Locked to Timeline
- **Inputs/Outputs:** Outputs to `audiofilter1`
- **Custom Parameters:** None

## Dependencies and External Files
### List of External Files
- **Audio Files:** Stored in `/project/audio/` used for testing.
### Dependencies
- Requires an external audio interface supported by ASIO drivers.

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** On Demand

### Environment Settings
- Set environment variable `TOUCHDESIGNER_ENV` to `production` for live shows.

## Performance Considerations
### Optimization
- Nodes not in use are bypassed to save resources.
### Performance Metrics
- Typically runs at 60 FPS on hardware specified in requirements.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-10 | Initial release.             |
| 1.1     | 2024-12-01 | Improved audio processing.   |

## Appendices
### A. Code Snippets
```python
# Example of a custom parameter expression
op('audiofilein1').par.rate = op('kinectazure1').par.framerate
