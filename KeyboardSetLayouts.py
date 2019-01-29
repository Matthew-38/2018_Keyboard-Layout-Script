#!/usr/bin/python3

"""This script depends on Python 3 or higher, and needs the libraries subprocess, os and sys. It only works in Linux
Usage: called simply from the command line: python3 KeyboardSetLayouts.py [reset]
you can use the 'reset' flag in the above command to set all the defined keyboards to the layout DefaultLayout
You, as the end user, may need to modify any of the following 3 things, depending on your situation:
1. Keybaords - use the xinput command in your terminal to help find the names or id numbers of your keyboards. Repeating with different ones plugged and unplugged can help to find which is which.
2. DefaultLayout - I have it set to Uk International with Dead Keys. You can change it to suit your situation. It is only used when the "reset" flag is used in the terminal. To get the names of layouts and variants, use ls and cat in the following directory of your system: /usr/share/X11/xkb/symbols
3. The if correct: clause below. This allows to select a specific device when there are several listed with identical names. When there aren't, it selects the only one. See comment.

This script is without licence. Use it as you want"""
import subprocess, os, sys
Keyboards=({"name":"LITEON", "id":False, "layout":"ru"},{"name":"HID", "id":False, "layout":"fr latin9"})  # Must have one of ID or Name
DefaultLayout= "gb intl"  # Used when resetting
if sys.version_info[0] < 3:  # REQUIRE VERSION 3.0 or higher of Python
    raise Exception("Python 3 or a more recent version is required.")
    quit(1)

for keyboard in Keyboards:
    layout = keyboard["layout"] if not "reset" in sys.argv else DefaultLayout
    device_id=keyboard["id"]
    if not device_id: #Prioritise a supplied ID number, otherwise look for it given the name. 
        result=subprocess.run(["xinput"], stdout=subprocess.PIPE) 
        deviceList=result.stdout.decode('utf-8').split('\n')
        correct=False
        for device in deviceList: 
            if keyboard["name"] in device:
                if correct:  # means it was already set once
                    correct=device
                    break  # For my second device, there are 3 devices with identical name. I used this setup to select the second. TODO: make a more stable solution to this. Or use the device id number 13.
                correct=device
        if not correct: continue  # In case the keyboard is not currently connected, for example. Still check for other keyboards in the list.
        device_id=correct.split("\t")[1][3:]
    #Compile command
    cmd="setxkbmap"
    argz="-device "+str(device_id)+" -layout "+layout
    fullcmd=cmd+" "+argz
    #Display and execute
    print(fullcmd)
    print(["Success!", "Failure!"][bool(os.system(fullcmd))])
