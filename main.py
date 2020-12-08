import os
import subprocess, sys, shlex
import re
import threading

import eel


# adb = os.path.join(os.getcwd(), os.path.normpath("scrcpy/adb.exe"))
# scrcpy = os.path.join(os.getcwd(), os.path.normpath("scrcpy/scrcpy.exe"))

adb = "scrcpy/adb.exe"
scrcpy = "scrcpy/scrcpy.exe"

# print("Scrcpy Path: {}".format(scrcpy))
# print("ADB Path: {}".format(adb))

Devices = []
Connect_To = ""

@eel.expose
def start_scrcpy(parameters):
    command_string = "{} -s {} --window-title 'Auto CPY'".format(scrcpy ,parameters["-s"])
    if parameters["-b"] != "0":
        command_string += " -b " + parameters["-b"]
    if parameters["-m"] != "0":
        command_string += " -m " + parameters["-m"]
    if not parameters["--no-control"]:
        command_string += " --no-control"
    if parameters["--turn-screen-off"]:
        command_string += " --turn-screen-off"
    if parameters["--fullscreen"]:
        command_string += " --fullscreen"
    if parameters["--always-on-top"]:
        command_string += " --always-on-top"
    command = shlex.split(command_string)
    stream = subprocess.Popen(command, stdout=sys.stdout)
    thread = threading.Thread(name= "scrcpy", target= stream.communicate)
    thread.start()
    print("Starting Scrcpy")

    ## DEBUG
    # print(parameters)
    # print(command_string)

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


def begin():
    global Devices, Connect_To
    Devices = get_connected_devices()
    Connect_To = get_device_to_connect_to(Devices)
    parameters = {
        "-s":Connect_To,
    }
    start_scrcpy(parameters)




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