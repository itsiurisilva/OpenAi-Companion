import os
import threading
from pynput import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image

# Global state for toggle
is_active = False

# Paths to your custom icons
on_icon_path = r"C:\Users\YOUR_USER\Icon\chatgpt-on.png"
off_icon_path = r"C:\Users\YOUR_USER\Icon\chatgpt.png"

# Load custom icons
on_icon = Image.open(on_icon_path)
off_icon = Image.open(off_icon_path)

# Function to activate ChatGPT
def activate_chatgpt(icon):
    global is_active
    if not is_active:
        os.system("adb shell am start -n com.openai.chatgpt/com.openai.voice.assistant.AssistantActivity")
        icon.icon = on_icon  # Update to custom "on" icon
        icon.title = "ChatGPT Active"
        is_active = True

# Function to deactivate ChatGPT
def deactivate_chatgpt(icon):
    global is_active
    if is_active:
        os.system("adb shell am force-stop com.openai.chatgpt")
        icon.icon = off_icon  # Update to custom "off" icon
        icon.title = "ChatGPT Inactive"
        is_active = False

# Function to toggle ChatGPT
def toggle_chatgpt(icon):
    if is_active:
        deactivate_chatgpt(icon)
    else:
        activate_chatgpt(icon)

# Function to listen for Play/Pause Media key
def listen_for_key(icon):
    def on_press(key):
        try:
            if key.name == "media_play_pause":  # Check for Play/Pause Media key
                toggle_chatgpt(icon)  # Pass the icon for updates
        except AttributeError:
            pass

    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Tray menu
menu = Menu(
    MenuItem("Activate ChatGPT", lambda: activate_chatgpt(icon)),
    MenuItem("Deactivate ChatGPT", lambda: deactivate_chatgpt(icon)),
    MenuItem("Exit", lambda: icon.stop())
)

# Initialize the tray icon
icon = Icon("ChatGPT", off_icon, "ChatGPT Inactive", menu)

# Run the tray icon and key listener in parallel
threading.Thread(target=listen_for_key, args=(icon,), daemon=True).start()
icon.run()
