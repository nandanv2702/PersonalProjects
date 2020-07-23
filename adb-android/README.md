# Python ADB

## adb-main.py

This was the main script used to install and uninstall apps. This was run only after running app-list.py. 

## app-list.py

This script was created to get the list of packages on the phone directly out of the box, then get the list of packages after manually uninstalling some apps. This script outputs two '.txt' files which are used in the next module.

## app-diff.py

This script determine the difference between the two lists, i.e., the apps that I uninstalled. I created this since I didn't know the names of the packages in order to uninstall them using the script. This module was then used in the main file 'adb-main.py' to do everything together, i.e., uninstall and install the required apps on a new phone

### Note: Developer Options must be enabeld on the phone in order for this to run, and in some cases, 'Verify apps over USB' needs to be turned off (only safe APKs were downloaded)
