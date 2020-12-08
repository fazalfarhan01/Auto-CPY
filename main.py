import os
import subprocess, sys, shlex
import re
import threading

import eel


adb = r"./scrcpy/adb.exe"
scrcpy = r"./scrcpy/scrcpy.exe"

Devices = []
Connect_To = ""

@eel.expose
def start_scrcpy(device_to_connect_to):
    command_string = "{} -s {}".format(scrcpy ,device_to_connect_to)
    command = shlex.split(command_string)
    stream = subprocess.Popen(command, stdout=sys.stdout)
    thread = threading.Thread(name= "scrcpy", target= stream.communicate)
    thread.start()
    print("Completed")

@eel.expose
def get_device_to_connect_to(devices):
    for device_number in range(len(devices)):
        print("{}. {}".format(device_number + 1, devices[device_number]))
    print("\n")
    connect_to = input("Enter the device number to connect to: ".upper())
    if connect_to.isnumeric() and int(connect_to) in range(len(devices)+ 1) :
        device_to_connect_to =  devices[int(connect_to) - 1]
    else:
        print("Enter a valid Device Number".upper())
        get_device_to_connect_to(devices)
    return device_to_connect_to

@eel.expose
def get_connected_devices():
    command_string = "{} devices".format(adb)
    command = shlex.split(command_string)
    stream = subprocess.Popen(command, stdout=subprocess.PIPE)
    command_output = stream.communicate()
    output = (command_output[0].decode("utf-8") if (command_output[0] is not None) else None).split()
    error = command_output[1].decode("utf-8") if (command_output[1] is not None) else None
    if error != None:
        print("Error Occured".upper())
    devices = []
    for element in output[4::2]:
        devices.append(element)
    return devices

@eel.expose
def begin():
    global Devices, Connect_To
    Devices = get_connected_devices()
    Connect_To = get_device_to_connect_to(Devices)
    start_scrcpy(Connect_To)




if __name__ == "__main__":
    # CHECK IF RUNNING ON WINDOWS
    # if sys.platform == "win32":
        # begin()
        # eel.start("index.html")
    eel.init("web")
    eel.start("index.html")
    # IF NOT ON WINDOWS
    # else:
    #     print("Un-supported Platform...!\nCurrently works only on Windows.")