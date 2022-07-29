call %cd%\venv\Scripts\activate.bat
pyinstaller main.py --clean --onefile --name "Fortnite Texture Tools" --windowed --icon=assets/pyqt/Icon.ico --version-file=file_version_info.txt
