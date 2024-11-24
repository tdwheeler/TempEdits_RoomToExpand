
# Project Name: Smoke & Fire Simulation

## Document Details
- **Version:** 1.0
- **Author:** [Your Name Here]
- **Date:** November 24, 2024

## Project Overview
### Purpose
This TouchDesigner project demonstrates a real-time smoke and fire simulation using Kinect Azure for motion tracking and NVFlow for smoke simulation.

### Key Features
- Integration of Kinect Azure for capturing motion data.
- Realistic smoke and fire rendering using NVFlow.
- Customizable emitter parameters for dynamic control.

### Hardware Requirements
- Kinect Azure for motion tracking.
- A GPU with NVFlow support for real-time smoke rendering.

## Node Graph Overview
### Diagram
![Complete Node Network](1_smoke_fire_body_toe.png)

### General Flow Description
The project captures motion data from Kinect Azure and uses it to drive NVFlow emitters. The emitters generate dynamic smoke and fire effects rendered in real time, with outputs configured for multi-display setups.

## Detailed Node Descriptions
### Nodes Listing
#### `project1kinectazure1`
- **Type:** Kinect Azure
- **Description:** Captures motion data to drive smoke dynamics.
- **Parameters:** 
  - Sensor: `000233924512`
  - Depth Mode: Wide Binned
  - Model Path: `Models/dnn_model_2_0_op11.onnx`
- **Inputs/Outputs:** Outputs to `null1`
- **Custom Parameters:** None

#### `project1nvflow1`
- **Type:** NVFlow
- **Description:** Handles smoke and fire rendering.
- **Parameters:** 
  - Camera: `cam2`
  - Emitters: `flowemitter1`
  - Output Resolution: 1280x720
- **Inputs/Outputs:** Outputs to `lookup2`
- **Custom Parameters:** None

#### `project1nvflowemitter1`
- **Type:** NVFlow Emitter
- **Description:** Emitter for NVFlow smoke simulation.
- **Parameters:** 
  - Type: `TOP`
  - Size: `2x2x0.5`
  - Shape Operator: `null1`
- **Inputs/Outputs:** Connected to `null1`
- **Custom Parameters:** None

#### `project1out1`
- **Type:** Out
- **Description:** Final output node for the smoke and fire simulation.
- **Parameters:** None
- **Inputs/Outputs:** Connected to `lookup2`
- **Custom Parameters:** None

## Dependencies and External Files
### List of External Files
- **Model Files:** DNN model file located in the project config folder.
- **Geometry:** Default `cam.geo` file for camera setup.

### Dependencies
- Requires NVFlow-supported GPU for rendering.
- Kinect Azure SDK for motion tracking.

## Configuration Settings
### Project Settings
- **Frame Rate:** 60 FPS
- **Cook Mode:** Realtime
- **Viewers:** Disabled for performance optimization.

### Environment Settings
- Environment variable `TOUCHDESIGNER_ENV` should be set to `production`.

## Performance Considerations
### Optimization
- Viewer nodes are disabled to save GPU resources.
- Resolution set to balance visual quality and real-time performance.

### Performance Metrics
- Consistent 60 FPS observed on recommended hardware.

## Version History
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| 1.0     | 2024-11-24 | Initial release.             |

## Appendices
### A. Code Snippets
```python
# Example custom Python for replicator callbacks
def replicate(comp, allOps, newOps, template, master):
    for c in newOps:
        c.display = True
        c.render = True
```
