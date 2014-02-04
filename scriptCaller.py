#!/usr/bin/python

import subprocess
import time
import os

# Set path variables
current_user = os.getlogin()
script_path = "/Users/" + current_user + "/restartMac.py"

# Wait 
time.sleep(6)

if os.path.isfile(script_path):
	temp_userfile = open('/tmp/domainuser', 'r')
	newuser = temp_userfile.read()
	temp_userfile.close()
	f = open('/var/log/newuser.log', 'w')
	f.write(str(newuser))
	f.close()

# Call user's restart script
subprocess.call(['python', script_path])



