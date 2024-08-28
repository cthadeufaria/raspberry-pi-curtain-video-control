# Automatic Curtain Controller

## Overview

The **Automatic Curtain Controller** is a Python-based project that controls a video simulating the opening and closing of curtains, much like an automatic door. The system uses an HC-SR501 PIR sensor to detect motion and triggers the curtain video accordingly. This project demonstrates the integration of hardware sensors with video control through software.

## Features

- **Motion Detection**: Uses the HC-SR501 PIR sensor to detect movement.
- **Video Playback**: Controls video playback in both forward and reverse directions to simulate curtain movement.
- **State Machine**: Implements a state machine to manage different states of the curtain (e.g., opening, closing, opened, closed).
- **Smooth Playback**: Optimized video playback for a seamless user experience.
- **Asynchronous Execution**: Uses Python's `asyncio` to handle sensor input and video playback concurrently.

## Installation

### Prerequisites

- Python 3.7+
- OpenCV
- gpiozero
- asyncio
- HC-SR501 PIR sensor connected to your device

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/cthadeufaria/raspberry-pi-curtain-video-control.git
    cd raspberry-pi-curtain-video-control
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Connect the HC-SR501 PIR sensor** to the appropriate GPIO pins on your device (e.g., Raspberry Pi).

4. **Place your video file** in the `videos/` directory, and update the video file name in the `config.py` file.

## Usage

Run the main script to start the curtain controller:

```bash
python3 main.py
```

## Contribution

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.