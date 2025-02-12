from pynput import keyboard

def on_press(key):
    print(f"Key pressed: {key}")

listener = keyboard.Listener(on_press=on_press)
listener.start()  # Starts the listener

print("Keylogger started...")
# Program exits immediately because there's no `join()`
# Main thread doesn't wait for the listener to stop, it ends listener
# using listener.join() blocks the main thread until manually stopped.