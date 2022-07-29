# Fortnite Texture Tools
## A set of tools to work with Fortnite texture files.

A small Python GUI application for converting file formats, separating mask textures and switching normal map files between DirectX and OpenGL normals.
All publicly available builds are uploaded to the `Releases` page of the repository.

![fttScreenshot](https://user-images.githubusercontent.com/99072163/181739003-7f59db07-c331-4fd2-b676-2fc46e26fe4a.png)

## How To Compile From Source

1. Fork the repository.
2. Start a terminal in the root directory of the project and create a Python virtual environment using:
    - ```python -m venv venv```
3. Activate the virtual environment using:
    - ```venv\Scripts\activate.bat```
4. After activating the virtual environment in your terminal, install the required pip packages using:
    - ```python -m pip install PyQt6```
    - ```python -m pip install pyinstaller```
    - ```python -m pip install Pillow```
5. To compile, run the `build.bat` batch file located in the root directory of the project, it will output an .exe file in the \dist directory.
6. Copy the \assets\pyqt folders to the \dist directory. Your \dist directory should look like this after finishing:

    ![exampleOfFinishedDistDirectory](https://user-images.githubusercontent.com/99072163/181738932-ff82237e-6b7f-4557-b2d4-978df67c075c.png)
- **This step is required as the program requires the MainUI.ui and Icon.ico files to be present in the correct directories next to the executable file for PyQt to load the UI.**

## Copyright Notice

This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Epic Games Inc., or any of its subsidiaries or its affiliates. The name Fortnite as well as related names, marks, emblems and images are registered trademarks of their respective owners.

## License

This project is licensed under the [MIT license](LICENSE).
