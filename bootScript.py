#!/usr/bin/python

import subprocess
import time
import os
from os import stat
from pwd import getpwuid
import pwd
import grp

#TODO: logic to check if file exists already.

f = open('/var/log/bootupdate.log', 'w')
f.write('scripts called\n')
f.close()

# Get the owner of the file the new user created on firstboot, and apply it to boxen
def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

new_user = find_owner('/Users/Shared/newuser.txt')
subprocess.call(['chown', '-R', new_user, '/opt/boxen'])


# Update apple software
subprocess.call(['softwareupdate', '-ia'])
now = time.strftime("%c")


# Log some stuff
f = open('/var/log/bootupdate.log', 'a')
f.write("Softwareupdate -ia command ran %s" % now)
f.close()

f = open('/var/log/bootupdate.log', 'a')
f.write(new_user)
f.close()

