# Auto-CPY

[![Total Downloads](https://img.shields.io/github/downloads/fazalfarhan01/Auto-CPY/total?color=0f0&label=Total%20Downloads&style=plastic)](https://github.com/fazalfarhan01/Auto-CPY/releases/download/Beta-2.0/Auto-CPY.Installer.exe)
[![Release Version](https://img.shields.io/github/v/release/fazalfarhan01/Auto-CPY?label=Release&style=plastic)](https://github.com/fazalfarhan01/Auto-CPY/releases/)
[![License](https://img.shields.io/github/license/fazalfarhan01/Auto-CPY?style=plastic)]()

---
GUI Client for [Scrcpy](https://github.com/Genymobile/scrcpy) and [Gnirehtet](https://github.com/Genymobile/gnirehtet) (Yet to be added) with auto-launch on device connect.

## Note:
1. Make sure you have your device's [__USB Debugging__](https://developer.android.com/studio/debug/dev-options) mode turned __ON__ (WiFi Support to be added soon.)
2. Connect your device to one of the USB ports on computer. 
3. Launch the Application.
#### If Auto launch on device connect is turned on, you will have to add an ___exclusion___ in windows defender.
Windows Defender detects it as a trojan (False Positive) and removes the executable because it has the auto launch on connect feature.
The application ___shortcut___ get placed in the startup applications folder `C:\Users\$USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` to make the application run in background.

Adding a folder exclusion in Windows Defender will work.

__Windows Defender__ >> __Virus and threat protection__ >> __Manage settings__ >> __Add or remove exclusions__ >> __Add an exclusion__ >> __Select the program install directory__. (Default `C:\Program Files\Auto-CPY\`)

![Windows Defender Exclusion](https://user-images.githubusercontent.com/45929854/101587925-3b5e0200-3a0b-11eb-922a-7c69ee0da6fa.png)

Check [__Releases__](https://github.com/fazalfarhan01/Auto-CPY/releases/) for more information

## Screenshots
![App Interface Home](./web/images/AppInterface1.png)
![App Interface Scrcpy](./web/images/AppInterface2.png)
