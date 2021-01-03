import os
import subprocess
import sys
import shlex
import re
import threading
from shutil import copyfile
from datetime import datetime

import eel

# Set to false on production
DEBUG_MODE = False

Devices = []
Connect_To = ""


def run_command(command_string):
    command = shlex.split(command_string)
    stream = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=STD_ERR, stdin=STD_IN)
    command_output = stream.communicate()
    output = (command_output[0].decode(
        "utf-8") if (command_output[0] is not None) else None).split()
    error = command_output[1].decode(
        "utf-8") if (command_output[1] is not None) else None
    if error != None:
        print("Error Occured".upper())
    print(" ".join(output))
    eel.printOnWiFiConnect(" ".join(output))


@eel.expose
def connect_on_WiFi(ipAddress):
    command = adb + " connect " + ipAddress
    threading.Thread(name="Wifi", target=run_command, args=(command,)).start()


@eel.expose
def adb_disconnect():
    command = adb + " disconnect"
    threading.Thread(name="Wifi", target=run_command, args=(command,)).start()


@eel.expose
def open_explorer():
    command_string = explorer + " \"C:\\Users\\" + os.getlogin() + "\\Videos\""
    command = shlex.split(command_string)
    stream = subprocess.Popen(command, stdout=STD_OUT,
                              stderr=STD_ERR, stdin=STD_IN)
    thread = threading.Thread(name="explorer", target=stream.communicate)
    thread.start()


@eel.expose
def start_scrcpy(parameters):
    command_string = "{} -s {} --window-title 'Auto CPY {}'".format(
        scrcpy, parameters["-s"], parameters["-s"])
    fileSaveOption = "C:\\Users\\" + os.getlogin() + "\\Videos\\" + \
        datetime.now().strftime("%Y%m%d%H%M%S")

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
    if parameters["--stay-awake"]:
        command_string += " --stay-awake"
    if parameters["--record"]:
        command_string += " --record \"{}.{}\"".format(
            fileSaveOption, parameters["extension"])

    command = shlex.split(command_string)
    stream = subprocess.Popen(command, stdout=STD_OUT,
                              stderr=STD_ERR, stdin=STD_IN)
    thread = threading.Thread(name="scrcpy", target=stream.communicate)
    thread.start()
    print("Starting Scrcpy")

    # DEBUG
    # print(parameters)
    # print(command_string)


@eel.expose
def get_device_to_connect_to(devices):
    for device_number in range(len(devices)):
        print("{}. {}".format(device_number + 1, devices[device_number]))
    print("\n")
    connect_to = input("Enter the device number to connect to: ".upper())
    if connect_to.isnumeric() and int(connect_to) in range(len(devices) + 1):
        device_to_connect_to = devices[int(connect_to) - 1]
    else:
        print("Enter a valid Device Number".upper())
        get_device_to_connect_to(devices)
    return device_to_connect_to


@eel.expose
def get_connected_devices():
    command_string = "{} devices".format(adb)
    command = shlex.split(command_string)
    stream = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=STD_ERR, stdin=STD_IN)
    command_output = stream.communicate()
    output = (command_output[0].decode(
        "utf-8") if (command_output[0] is not None) else None).split()
    error = command_output[1].decode(
        "utf-8") if (command_output[1] is not None) else None
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
        "-s": Connect_To,
        "-b": "0",
        "-m": "0",
        "--no-control": True,
        "--turn-screen-off": False,
        "--fullscreen": False,
        "--always-on-top": False,
        "--stay-awake": False,
        "--record": False,
    }

    start_scrcpy(parameters)


@eel.expose
def checkStartOnConnect():
    enabled = os.path.exists("C:\\Users\\" + os.getlogin() +
                             "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Auto-CPY.lnk")
    return enabled


@eel.expose
def changeStartOnConnectStatus(status):
    # If Have to install and not already installed
    if status and not checkStartOnConnect():
        copyfile(os.path.join(os.getcwd(), "Auto-CPY.lnk"), "C:\\Users\\" + os.getlogin() +
                 "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Auto-CPY.lnk")
    # if have to remove and file exists
    elif (not status) and checkStartOnConnect():
        os.remove("C:\\Users\\" + os.getlogin() +
                  "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Auto-CPY.lnk")


def setupModes():
    global STD_OUT, STD_ERR, STD_IN
    if DEBUG_MODE:
        print("Debug Mode")
        STD_OUT = sys.stdout
        STD_ERR = sys.stderr
        STD_IN = sys.stdin
    else:
        STD_OUT = subprocess.PIPE
        STD_ERR = subprocess.STDOUT
        STD_IN = subprocess.PIPE


if __name__ == "__main__":
    if sys.platform == "win32":
        adb = "scrcpy/adb.exe"
        scrcpy = "scrcpy/scrcpy.exe"
        explorer = "C:\\\\Windows\\\\explorer.exe"
    else:
        print("Not on windows")
        quit()
    setupModes()
    eel.init("web")
    eel.start("index.html")
