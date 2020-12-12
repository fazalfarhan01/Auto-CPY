.\env\Scripts\python.exe -m eel .\main.py .\web --onefile --icon=.\web\images\favicon.ico -n Auto-CPY.exe
move /Y .\dist\Auto-CPY.exe .
del Auto-CPY.exe.spec /f /q
"C:\Program Files (x86)\NSIS\makensis.exe" .\Auto-CPY.nsi