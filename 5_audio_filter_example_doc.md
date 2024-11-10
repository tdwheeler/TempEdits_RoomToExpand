
# TouchDesigner Patch Documentation: 5_audio_filter_example.toe

## Overview
This documentation details the TouchDesigner patch named **5_audio_filter_example.toe**. The patch is designed for processing audio input and filtering, utilizing components such as audio file input, filtering methods, and output mechanisms.

---

## Patch Information
- **Version**: 099
- **Build**: 2023.11880
- **Operating System**: Windows 10
- **Created On**: Mon Oct 7 16:26:16 2024

---

## Components and Descriptions

### 1. KinectAzure1
- **Type**: TOP
- **Function**: Captures depth and other sensor data from a Kinect Azure device.
- **Location**: Top-left of the patch.

### 2. Null1
- **Type**: TOP
- **Function**: Acts as a pass-through for the data from KinectAzure1, simplifying connections to other components.
- **Location**: Middle-top of the patch.
- **Connections**: Receives data from KinectAzure1 and forwards it to Out1.

### 3. Out1
- **Type**: TOP
- **Function**: Outputs the final visual processed data.
- **Location**: Top-right of the patch.
- **Connections**: Receives data from Null1.

### 4. KinectAzure2
- **Type**: TOP (Error flagged)
- **Function**: Intended to be a secondary Kinect Azure device input, currently showing an error (possibly due to unavailability or incorrect configuration).
- **Location**: Bottom-left of the patch.

### 5. Select1
- **Type**: CHOP
- **Function**: Selects specific channels from the Kinect data for further processing.
- **Location**: Middle-left of the patch.
- **Connections**: Receives data from KinectAzure2 and sends it to Math1.

### 6. Math1
- **Type**: CHOP
- **Function**: Applies mathematical operations to the data received from Select1.
- **Location**: Center of the patch.
- **Connections**: Outputs processed data to Lag1.

### 7. Lag1
- **Type**: CHOP
- **Function**: Adds a lag effect to smooth transitions in the data.
- **Location**: Center-right of the patch.
- **Connections**: Receives data from Math1 and sends it to Math2.

### 8. Math2
- **Type**: CHOP
- **Function**: Further processes the lagged data with additional mathematical operations.
- **Location**: Right-center of the patch.
- **Connections**: Outputs processed data to AudioDevOut1.

### 9. AudioFileIn1
- **Type**: CHOP
- **Function**: Inputs an audio file for analysis and filtering.
- **Location**: Bottom-left of the patch.

### 10. AudioFilter1
- **Type**: CHOP
- **Function**: Applies filtering to the audio data received from AudioFileIn1.
- **Location**: Bottom-center of the patch.
- **Connections**: Processes data from AudioFileIn1 and outputs to AudioDevOut1.

### 11. AudioDevOut1
- **Type**: CHOP
- **Function**: Sends processed audio data to the system's audio output.
- **Location**: Bottom-right of the patch.
- **Connections**: Receives filtered audio data from AudioFilter1.

---

## Patch Settings and Configuration
### Window and Display Settings
- **Perform Mode**: Press F1 to enter, ESC to exit.
- **Window Placement**: Top mode with auto configuration, position x=0, y=0, size x=1024, y=768.

### Audio Settings
- **Driver**: ASIO
- **Device**: Focusrite_USB_ASIO2
- **Sample Rate**: 44100 Hz
- **Tracks**: 2 (Channel 1 and Channel 2)

### Cook Settings
- **Cook Rate**: 60 FPS
- **Real-Time Mode**: On
- **Audio Reset on Device Change**: Off

---

## Error Handling
- **KinectAzure2**: Currently flagged with an error. Ensure the device is properly connected and configured.

---

## Additional Notes
- The patch leverages depth data from Kinect Azure and processes audio input, applying custom filters and outputting the processed data.
- Ensure that all external devices (Kinect, audio interfaces) are correctly connected and configured to avoid errors.

---

**End of Documentation**
