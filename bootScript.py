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

# Get the owner of the file the new user created on firstboot.
def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

new_user = find_owner('/Users/Shared/newuser.txt')
new_uid = pwd.getpwnam(new_user).pw_uid
new_gid = grp.getgrnam("wheel").gr_gid

# Open boxen default.json file and change user
# Change owner of /opt/boxen folder
for root, dirs, files in os.walk('/opt/boxen'):
	for momo in dirs:
		os.chown(os.path.join(root, momo), new_uid, new_gid)
	for momo in files:
		os.chown(os.path.join(root, momo), new_uid, new_gid)

# os.chown('/opt/boxen', new_uid, new_gid)

# check for software updates
subprocess.call(['softwareupdate', '-ia'])

now = time.strftime("%c")



f = open('/var/log/bootupdate.log', 'a')
f.write("Softwareupdate -ia command ran %s" % now)
f.close()

f = open('/var/log/bootupdate.log', 'a')


# f.write(str(current_user))
f.write(new_user)

