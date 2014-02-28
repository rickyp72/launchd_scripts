#!/usr/bin/python

import subprocess
import time
import os
from os import stat
from pwd import getpwuid
import pwd
import grp
import shutil

#TODO: logic to check if file exists already.

f = open('/var/log/bootupdate.log', 'w')
f.write('scripts called\n')
f.close()

# Get the owner of the file the new user created on firstboot, and apply it to boxen
def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

new_user = find_owner('/Users/Shared/newuser.txt')


# change default user in boxen default.json file

oldstr = 'localadmin'
newstr =  str(new_user)

with open("/opt/boxen/config/boxen/defaults.json") as f:
    file_lines = f.readlines()
    new_file = [line.replace(oldstr,newstr) for line in file_lines]

open("/Users/Shared/defaults.json","w").write(''.join(new_file))

# swap original boxen file for new one
defaults_path = "/opt/boxen/config/boxen/"
shared_path = "/Users/Shared/"
filename = "defaults.json"
newfilename = "defaults.json.original"

os.rename(defaults_path + filename, defaults_path + newfilename)
shutil.move(shared_path + filename, defaults_path + filename)

# change owner of files
subprocess.call(['chown', '-R', new_user, '/opt/boxen'])

# swap original sudoers file for new one
############################################
defaults_path = "/etc/"
shared_path = "/Users/Shared/"
filename = "sudoers"
newfilename = "sudoers.original"
oldstr = 'localadmin'
newstr =  str(new_user)

with open(defaults_path + filename) as f:
    file_lines = f.readlines()
    new_file = [line.replace(oldstr,newstr) for line in file_lines]

open(shared_path + filename, "w").write(''.join(new_file))


os.rename(defaults_path + filename, defaults_path + newfilename)
shutil.move(shared_path + filename, defaults_path + filename)
################################################
# Update apple software
subprocess.call(['softwareupdate', '-ia'])
now = time.strftime("%c")

# ## setup puppet THERE IS A NETWORK CONNECTION!!! MIGHT JUST HAVE CALL 'PUPPET AGENT??
subprocess.call(['puppet', 'agent', '-t'])
# file_name = "install_puppet.py"
# newfilename = "install_puppet.py.done"
# subprocess.call(['python', file_name])
# # rename this file to stop it running again
# os.rename(file_name, newfilename)

# Log some stuff
f = open('/var/log/bootupdate.log', 'a')
f.write("Softwareupdate -ia command ran %s" % now)
f.close()

f = open('/var/log/bootupdate.log', 'a')
f.write(new_user)
f.close()

