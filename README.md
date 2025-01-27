# OpenAi Companion - V1
This Python application allows you to toggle the ChatGPT voice assistant using a system tray icon or a Play/Pause media hotkey. 

## Key Features
- Activate or deactivate ChatGPT directly from the system tray.
- Hotkey support using the **Play/Pause media key**.
- Custom icons to indicate the assistant's state (active/inactive).

## Requirements
### Software Requirements:
- Python 3.8+
- Modules: `pynput`, `pystray`, `Pillow`
- ADB (Android Debug Bridge): [Download ADB here.](https://developer.android.com/studio/releases/platform-tools)
### Device Requirements:
- An Android phone with the ChatGPT app installed.
- USB Debugging enabled on the phone.

## How to Setup
  ### 1. Enable USB Debugging on Your Android Device
   1. Open **Settings** on your Android phone.
   2. Navigate to **About Phone** and tap on **Build Number** seven times to enable **Developer Options**.
   3. Go back to **Settings → System → Developer Options**.
   4. Enable **USB Debugging**.

  ### 2. Install ADB on Your Computer
   1. Download the ADB platform tools (ABOVE)
   2. Extract the tools and add the **directory** to your system's **PATH** for global access.

  ### 3. Connect your Android Device via USB
   1. Run `adb device` (To make sure is Detected)

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/OpenAi-Companion.git
2. Install the required Python modules:
   ```bash
   pip install pynput pystray Pillow
3. Edit the script Path:
   ```bash
   Edit OpenAi_Companion.py at:
    on_icon_path = r"C:\Users\YOUR_USER\Icon\chatgpt-on.png"
    off_icon_path = r"C:\Users\YOUR_USER\Icon\chatgpt.png"
4. Run the script:
   ```bash
    python OpenAi_Companion.py

## How it Works
- System Tray: `Right-click the tray icon to activate or deactivate ChatGPT.`
- Hotkey: `Press the Play/Pause media key to toggle ChatGPT.`

## Contributing
`Feel free to submit issues or pull requests to improve this project.`

## Upcoming Features (V2)
The next version (V2) will include the following improvements and new features:
- Custom Hotkeys: Assign your own hotkey instead of the default Play/Pause media key.
- Auto-Deactivation Timer: Automatically turn off ChatGPT after a specified period.
- Notifications: Show system notifications when ChatGPT is activated or deactivated.
- Improved User Interface: Add more options and enhancements to the system tray menu.
- Cross-Platform Support: Test and refine compatibility for macOS and Linux systems.

