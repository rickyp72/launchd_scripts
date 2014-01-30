#!/usr/bin/python

import subprocess
import time
import os

# Set path variables
current_user = os.getlogin()
script_path = "/Users/" + current_user + "/restartMac.py"

# Wait 
time.sleep(6)

# Call user's restart script
subprocess.call(['python', script_path])



