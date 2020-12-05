import os
import subprocess, sys, shlex
import re
import threading

class AutoCPY(object):
    def __init__(self):
        self.adb = r"./scrcpy/adb.exe"
        self.scrcpy = r"./scrcpy/scrcpy.exe"

    def start_scrcpy(self):
        command_string = "{} -s {}".format(self.scrcpy ,self.device_to_connect_to)
        command = shlex.split(command_string)
        stream = subprocess.Popen(command, stdout=sys.stdout)
        thread = threading.Thread(name= "scrcpy", target= stream.communicate)
        thread.start()
        print("Completed")

    def get_device_to_connect_to(self):
        for device_number in range(len(self.devices)):
            print("{}. {}".format(device_number + 1, self.devices[device_number]))
        print("\n")

        connect_to = input("Enter the device number to connect to: ".upper())
        if connect_to.isnumeric() and int(connect_to) in range(len(self.devices)+ 1) :
            self.device_to_connect_to =  self.devices[int(connect_to) - 1]
        else:
            print("Enter a valid Device Number".upper())
            self.get_device_to_connect_to()

    def get_connected_devices(self):

        command_string = "{} devices".format(self.adb)
        command = shlex.split(command_string)
        stream = subprocess.Popen(command, stdout=subprocess.PIPE)
        command_output = stream.communicate()
        output = (command_output[0].decode("utf-8") if (command_output[0] is not None) else None).split()
        error = command_output[1].decode("utf-8") if (command_output[1] is not None) else None

        if error != None:
            print("Error Occured".upper())


        self.devices = []
        for element in output[4::2]:
            # RE Approach isn't efficient in this case
            # print (element)
            # device = re.findall(r"[0-9]+.[0-9]", element)
            # if len(device) != 0:
            self.devices.append(element)
    
    def begin(self):
        self.get_connected_devices()
        self.get_device_to_connect_to()
        self.start_scrcpy()




if __name__ == "__main__":
    # CHECK IF RUNNING ON WINDOWS
    if sys.platform == "win32":
        autocpy = AutoCPY()
        autocpy.begin()
        
        
    # IF NOT ON WINDOWS
    else:
        print("Un-supported Platform...!\nCurrently works only on Windows.")