call %cd%\venv\Scripts\activate.bat
pyinstaller main.py --clean --onefile --name "Fortnite Texture Tools" --windowed --icon=assets/pyqt/Icon.ico --version-file=file_version_info.txt
echo:
echo Copying required asset files to the build directory . . .
if not exist %cd%\dist\assets\pyqt mkdir %cd%\dist\assets\pyqt
xcopy %cd%\assets\pyqt\*.* %cd%\dist\assets\pyqt\. /Y
echo:
echo Build successful!
pause
