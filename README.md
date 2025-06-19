# Real-Time Keystroke Logger

A simple Python script to log keystrokes in real-time, designed for educational purposes and personal monitoring.

# ⚠️ Disclaimer: Ethical Use Required ⚠️
This script is provided for educational purposes only, to demonstrate how a basic keylogger works. *It is crucial to understand and adhere to all applicable laws and ethical guidelines regarding privacy and surveillance.* Unauthorized use of this software to monitor others without their explicit consent is illegal and unethical.

Always ensure you have proper authorization before deploying or using this script on any system.

# Features
* Real-time Logging: Captures keystrokes as they are typed.
* Alphanumeric and Special Keys: Logs both regular characters and special keys (e.g., `Space`, `Enter`, `Shift`, `Ctrl`, `Alt`, `Tab`, `Esc`). Special keys are wrapped in brackets for clarity (e.g., `[Key.space]`).
* Log File: All captured keystrokes are saved to a text file named `real_time_keystrokes.txt`.
* Simple Termination: The keylogger can be gracefully stopped by pressing the `Esc` (Escape) key.

# Prerequisites
Before running this script, you need to have Python installed on your system.
This script uses the `pynput` library.

# Installation
1. Clone the repository (or download the script):

`git clone https://github.com/Ubuntu-Dekiru/PRODIGY_CS_04.git
cd PRODIGY_CS_O4`

2. Install the pynput library:

`pip install pynput`

# Usage
1. Save the script: Save the provided Python code as `keylogger.py` (or any other `.py` extension).

2. Run the script from your terminal:

`python keylogger.py`

3. Start Logging: The script will print a message indicating it has started:

`[*] Starting real-time keylogger. All keystrokes will be saved to 'real_time_keystrokes.txt'.
Press 'Esc' to stop the keylogger.`

From this point, any keystrokes you type will be logged.

4. Stop the Keylogger: To stop the keylogger, simply press the `Esc` key on your keyboard. The script will then terminate.

Output
All logged keystrokes will be appended to a file named `real_time_keystrokes.txt` in the same directory where the script is executed.
Example `real_time_keystrokes.txt` content:

`Hello[Key.space]World![Key.enter]This[Key.space]is[Key.space]a[Key.space]test.[Key.enter]`


# License
This project is licensed under the MIT License - see the LICENSE file for details.
