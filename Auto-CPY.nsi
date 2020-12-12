############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System                
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006               
############################################################################################
Unicode True

!define APP_NAME "Auto-CPY"
!define COMP_NAME "DeepFocus"
!define VERSION "0.0.0.01"
!define COPYRIGHT "Mohamed Farhan Fazal"
!define DESCRIPTION "GUI Scrcpy & Gnirhetet"
; !define INSTALLER_NAME "C:\Users\fazal\Desktop\Compiled\Auto-CPY Installer.exe"
!define MAIN_APP_EXE "Auto-CPY.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
!define MUI_ICON ".\favicon.ico"


######################################################################

VIProductVersion "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
; OutFile "${INSTALLER_NAME}"
OutFile "Auto-CPY Installer.exe"
BrandingText "${APP_NAME}"
XPStyle on
; InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES64\Auto-CPY\"

######################################################################

!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!insertmacro MUI_PAGE_DIRECTORY

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "Auto-CPY"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

; !define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_APP_EXE}"
!define MUI_FINISHPAGE_RUN "$INSTDIR\run.vbs"
; !insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File "Auto-CPY.exe"
File "autoadb.exe"
File "start.bat"
File "start.vbs"
File "run.bat"
File "run.vbs"
File "favicon.ico"
SetOutPath "$INSTDIR\scrcpy"
File /nonfatal /a /r "scrcpy\"
SectionEnd

######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
; CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\run.vbs"
; CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\run.vbs"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"
CreateShortCut "$INSTDIR\${APP_NAME}.lnk" "$INSTDIR\start.vbs" "" "$INSTDIR\favicon.ico" "" "" "" "Launch Auto-CPY in background on boot"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\Auto-CPY"
CreateShortCut "$SMPROGRAMS\Auto-CPY\${APP_NAME}.lnk" "$INSTDIR\run.vbs" "" "$INSTDIR\favicon.ico" "" "" "" "Launch Auto-CPY"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\run.vbs" "" "$INSTDIR\favicon.ico" "" "" "" "Launch Auto-CPY"
CreateShortCut "$SMPROGRAMS\Auto-CPY\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"
CreateShortCut "$INSTDIR\${APP_NAME}.lnk" "$INSTDIR\start.vbs" "" "$INSTDIR\favicon.ico" "" "" "" "Launch Auto-CPY in background on boot"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\Auto-CPY\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}
Delete "$INSTDIR\${MAIN_APP_EXE}"
Delete "$INSTDIR\autoadb.exe"
Delete "$INSTDIR\start.bat"
Delete "$INSTDIR\run.bat"
Delete "$INSTDIR\start.vbs"
Delete "$INSTDIR\run.vbs"
Delete "$INSTDIR\favicon.ico"
Delete "$INSTDIR\scrcpy\adb.exe"
Delete "$INSTDIR\scrcpy\AdbWinApi.dll"
Delete "$INSTDIR\scrcpy\AdbWinUsbApi.dll"
Delete "$INSTDIR\scrcpy\avcodec-58.dll"
Delete "$INSTDIR\scrcpy\avformat-58.dll"
Delete "$INSTDIR\scrcpy\avutil-56.dll"
Delete "$INSTDIR\scrcpy\scrcpy-noconsole.exe"
Delete "$INSTDIR\scrcpy\scrcpy-server"
Delete "$INSTDIR\scrcpy\scrcpy.exe"
Delete "$INSTDIR\scrcpy\SDL2.dll"
Delete "$INSTDIR\scrcpy\swresample-3.dll"
Delete "$INSTDIR\scrcpy\swscale-5.dll"
Delete "$INSTDIR\${APP_NAME}.lnk"
 
RmDir "$INSTDIR\scrcpy"
 
Delete "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"
Delete "$INSTDIR\${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\Auto-CPY\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\Auto-CPY\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\Auto-CPY\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\Auto-CPY"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd

######################################################################

