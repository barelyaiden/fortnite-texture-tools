# Fortnite Texture Tools
## A set of tools to work with Fortnite texture files.

A small Python GUI application for converting file formats, separating mask textures and switching normal map files between DirectX and OpenGL normals.

All publicly available builds are uploaded to the [Releases](https://github.com/barelyaiden/fortnite-texture-tools/releases) page of the repository.

![fttScreenshot](https://user-images.githubusercontent.com/99072163/181904393-b2683a92-adae-4937-a785-cce3a44146f7.png)

## How To Compile From Source

1. Fork the repository.
2. Start a terminal in the root directory of the project and create a Python virtual environment using:
    - ```python -m venv venv```
3. Activate the virtual environment using:
    - ```venv\Scripts\activate.bat```
4. After activating the virtual environment in your terminal, install the required pip packages using:
    - ```pip install -r requirements.txt```
5. To run the program in a development environment for testing, run the `main.py` script using:
    - ```main.py```
    
    Make sure you are in your virtual environment before running the command.
6. To compile, run the `build.bat` batch file located in the root directory of the project, it will output an .exe file in the \dist directory.

## Copyright Notice

This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Epic Games Inc., or any of its subsidiaries or its affiliates. The name Fortnite as well as related names, marks, emblems and images are registered trademarks of their respective owners.

## License

This project is licensed under the [MIT license](LICENSE).
