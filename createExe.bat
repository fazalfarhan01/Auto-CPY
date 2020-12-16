.\env\Scripts\python.exe -m eel .\main.py .\web --onefile --icon=.\web\images\favicon.ico -n Auto-CPY.exe
move /Y .\dist\Auto-CPY.exe .
@REM del Auto-CPY.exe.spec /f /q
move /Y Auto-CPY.exe.spec .\dist\.
"C:\Program Files (x86)\NSIS\makensis.exe" .\Auto-CPY.nsi