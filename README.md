launchd_scripts
===============

These files need to copied to there respective folder before the image is created.

Run the script:

sudo python manageLaunchd.py

This will put everything in its respective place, set the permissions and load the launchctl plists

Files to check before creating image are:

'/Library/Scripts/scriptCaller.py', 0755
'/System/Library/User Template/English.lproj/restartMac.py', 0755
'/Library/LaunchAgents/com.rnbrestart.plist', 0644
'/Library/Scripts/bootScript.py', 0755
'/Library/LaunchDaemons/com.rnbbootrun.plist', 0644
