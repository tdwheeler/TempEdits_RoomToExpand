
# Project Name: Airdrum Interactive Patch

## Document Details
- **Version:** 1.0
- **Author:** [Your Name Here]
- **Date:** November 24, 2024

## Project Overview
### Purpose
This TouchDesigner project allows users to interact with an air drum system using Kinect Azure. It tracks hand and pelvis movements to trigger audio samples, simulating a drum-playing experience.

### Key Features
- Real-time motion tracking via Kinect Azure.
- Dynamic triggering of audio samples based on hand and pelvis positions.
- Configurable motion ranges for precise interaction.

### Hardware Requirements
- Kinect Azure for motion tracking.
- An audio output device for playing drum samples.

## Node Graph Overview
### Diagram
![Complete Node Network](airdrum.png)

### General Flow Description
The project captures motion data for two players using Kinect Azure. Each player's hand and pelvis positions are tracked and mapped to corresponding drum sounds. Motion data is filtered, processed, and used to trigger audio samples in real-time.

## Detailed Node Descriptions
### Nodes Listing
#### `kinectazure1`
- **Type:** Kinect Azure
- **Description:** Captures depth and motion data from Kinect Azure.
- **Parameters:** 
  - Sensor: Kinect Azure
  - Depth Mode: Wide Binned
  - Players: 2
- **Inputs/Outputs:** Outputs to `select1`, `select2`, `select3`, `select4`, and `select5`.

#### `select1` - `select5`
- **Type:** Select CHOP
- **Description:** Extracts specific body parts' motion data.
- **Parameters:**
  - Select1: Tracks `p1hand_r:depthv`.
  - Select2: Tracks `p1hand_l:depthv`.
  - Select3: Tracks `p1pelvis:depthv`.
  - Select4: Tracks `p2hand_r:depthv`.
  - Select5: Tracks `p2hand_l:depthv`.
- **Inputs/Outputs:** Inputs from `kinectazure1`; outputs to corresponding `math` nodes.

#### `math1` - `math5`
- **Type:** Math CHOP
- **Description:** Normalizes and scales motion data to fit interaction ranges.
- **Parameters:** 
  - Custom ranges for each body part to map motion accurately.
- **Inputs/Outputs:** Inputs from `select` nodes; outputs to corresponding `limit` nodes.

#### `limit1` - `limit5`
- **Type:** Limit CHOP
- **Description:** Clamps or loops normalized data to stay within usable ranges.
- **Inputs/Outputs:** Inputs from `math` nodes; outputs to `trigger` nodes.

#### `trigger1` - `trigger5`
- **Type:** Trigger CHOP
- **Description:** Converts clamped motion data into triggers for audio playback.
- **Inputs/Outputs:** Inputs from `limit` nodes; outputs to `audioplay` nodes.

#### `audioplay1` - `audioplay5`
- **Type:** Audio Play CHOP
- **Description:** Plays corresponding audio samples for drum sounds.
- **Parameters:**
  - Audioplay1: Snare
  - Audioplay2: Hi-hat
  - Audioplay3: Bass
  - Audioplay4: Tom
  - Audioplay5: Crash
- **Inputs/Outputs:** Inputs from `trigger` nodes.

## Dependencies and External Files
### List of External Files
- **Audio Files:** Drum sound samples stored in the project folder.

### Dependencies
- Requires Kinect Azure SDK for motion tracking.
- An audio output device (e.g., Focusrite USB).

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** Realtime
- **Viewers:** Disabled for performance optimization.

### Environment Settings
- Ensure the environment variable `TOUCHDESIGNER_ENV` is set to `development`.

## Performance Considerations
### Optimization
- Only active nodes are cooked to save computational resources.
- Viewer nodes are disabled to maximize real-time performance.

### Performance Metrics
- Consistent 60 FPS on hardware meeting the specified requirements.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-24 | Initial release.             |

## Appendices
### A. Code Snippets
```python
# Example Python for audio trigger customization
op('audioplay1').par.file = 'audio/snare.wav'
```
