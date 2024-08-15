# Basic Hand Detection Script

This Python script uses OpenCV and the `cvzone` library to detect hands in real-time through a webcam feed. The script initializes the webcam, detects hands in the video stream, and displays the live feed with hand detection overlaid.

## Features

- **Real-time Hand Detection**: Detects up to two hands simultaneously using the `cvzone.HandTrackingModule`.
- **Customizable Webcam Feed**: Configurable webcam resolution for better control over the output display.
- **Easy Exit**: The application can be closed by pressing the 'q' key.

## Prerequisites

To run this script, you need to have the following libraries installed:

- **OpenCV**: For capturing video from the webcam and processing images.
- **cvzone**: A library that simplifies the usage of OpenCV and MediaPipe for various computer vision tasks.

You can install these libraries using pip:

```bash
pip install opencv-python-headless
pip install cvzone
```

## How to Run

### Clone the Repository:

```bash
git clone https://github.com/Isa-khan/Basic-Hand-Detection-Script.git
cd Basic-Hand-Detection-Script
```
### Then just run the script

## License
This project is open source and available under the MIT License.
