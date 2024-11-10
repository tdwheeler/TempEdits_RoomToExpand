# Patch Name: [output file name here]
- **Date:** [output today's date in MM/DD/YYYY format]

## General Overview
### Summary
[output your assessment of the general purpose and functionality of the TouchDesigner patch in 1-3 sentences here. For example: This TouchDesigner project integrates live audio inputs with visual effects to create dynamic visualizations during live performances.]

### Key Features
[output a list of key features]

### Hardware Requirements
[output hardware requirements if neccessary]

## Node Graph Overview
### General Flow Description
[output your assessment of how the patch functions and which essential groups of nodes function together. This should be 1-3 sentences. For example: 
The project captures live audio and motion data, processes the information, and outputs synchronized audio-visual content. Audio data is filtered, analyzed, and then used to modulate various visual parameters.]

## Detailed Node Descriptions
### Nodes Listing
[output a list of all essential nodes here. The 'Description' parameter is the most important. Do not stretch your faculties of induction if you aren't so sure. For example:
  #### `kinectazure1`
  - **Type:** Kinect Azure
  - **Description:** Captures motion data for audience interaction.
  - **Parameters:** 
    - Depth Mode: High
    - Camera Index: 0
  - **Inputs/Outputs:** Outputs to `select1`
  - **Custom Parameters:** None]

## Dependencies and External Files
[For example:
  ### List of External Files
  - **Audio Files:** Stored in `/project/audio/` used for testing.
  ### Dependencies
  - Requires an external audio interface supported by ASIO drivers.]

## Misc
[Any additional special info about the patch can go here. For example:
### A. Code Snippets
  ```python
  # Example of a custom parameter expression
  op('audiofilein1').par.rate = op('kinectazure1').par.framerate
  ```
]
