#!/usr/bin/python

import subprocess
import os

# 
current_user = str(os.getlogin())
home_path = "/Users/" + current_user + "/"
file_name = "restartMac.py"
newfilename = "restartMac.py.done"

# rename this file to stop it running again
os.rename(home_path + file_name, home_path + newfilename)

temp_userfile = open('/tmp/domainuser', 'w')
temp_userfile.write(current_user)
temp_userfile.close()

# Restart the mac to start encryption process
subprocess.call(['osascript', '-e',
'tell app "System Events" to restart'])

