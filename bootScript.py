#!/usr/bin/python

import subprocess
import time
import os


#TODO: logic to check if file exists already.

f = open('/var/log/bootupdate.log', 'w')
f.write('scripts called\n')
f.close()
# Set path variables


# Call user's restart script
subprocess.call(['softwareupdate', '-ia'])

now = time.strftime("%c")


f = open('/var/log/bootupdate.log', 'a')
f.write("Softwareupdate -ia command ran %s" % now)
f.close()

