#!/usr/bin/python

import subprocess
import time
import os

# Set path variables
current_user = os.getlogin()
script_path = "/Users/" + current_user + "/restartMac.py"
first_restart = script_path + ".done"

# Wait 
time.sleep(6)

# if os.path.isfile(first_restart):
# 	temp_userfile = open('/tmp/domainuser', 'r')
# 	newuser = temp_userfile.read()
# 	temp_userfile.close()
	f = open('/var/log/newuser.log', 'w')
	f.write(str(current_user))
	f.close()



# Call user's restart script
subprocess.call(['python', script_path])



