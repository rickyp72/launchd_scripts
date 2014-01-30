#!/usr/bin/env python

import subprocess
import os
import sys
import shutil

# copy files in relevant locations
shutil.copyfile('com.rnbrestart.plist', '/Library/LaunchAgents/com.rnbrestart.plist')
shutil.copyfile('scriptCaller.py', '/Library/Scripts/scriptCaller.py')
shutil.copyfile('restartMac.py', '/System/Library/User Template/English.lproj/restartMac.py')
# script to run as root to run software updates
shutil.copyfile('com.rnbbootrun.plist', '/Library/LaunchDaemons/com.rnbbootrun.plist')
shutil.copyfile('bootScript.py', '/Library/Scripts/bootScript.py')


# Set permissions on files
os.chmod('/Library/Scripts/scriptCaller.py', 0755)
os.chmod('/System/Library/User Template/English.lproj/restartMac.py', 0755)
os.chmod('/Library/LaunchAgents/com.rnbrestart.plist', 0644)

os.chmod('/Library/Scripts/bootScript.py', 0755)
os.chmod('/Library/LaunchDaemons/com.rnbbootrun.plist', 0644)

# Initialise launchd
print "Setting launchd process for rnbrestart"
subprocess.call(['launchctl', 'load', '/Library/LaunchAgents/com.rnbrestart.plist'])
print "Setting launchd process for rnbbootrundom"
subprocess.call(['launchctl', 'load', '/Library/LaunchDaemons/com.rnbbootrun.plist'])

# sign scripts
#subprocess.call(['codesign', "-s - --resource-rules='/Users/user/Desktop/launchd_files/ResourceRules-ignoring-Scripts.plist' '/Library/Scripts/devloginhook.sh'"])

# print "Copy and run the below command in the terminal: "
# print 'sudo codesign -s - --resource-rules=/Users/user/Desktop/launchd_files/ResourceRules-ignoring-Scripts.plist /Library/Scripts/devloginhook.sh'
print "sudo shutdown -r now"


