'''
The sys library has tools to work with the interpreter.
The os library has tools to work with the operating system.
The PyQt6 library has tools to work with the Qt UI framework.
The TextureConverter class has custom functions to work with image files.
'''
import sys
import os
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox # pylint: disable=no-name-in-module
from assets.tools.texture_converter import TextureConverter

class MainWindow(QMainWindow):
    '''
    The MainWindow class which inherits the QMainWindow class from PyQt6
    displays the main window and adds the needed functionality
    to the elements in the UI.
    '''
    def __init__(self):
        super().__init__()

        uic.loadUi('assets/pyqt/MainUI.ui', self)
        self.setWindowIcon(QtGui.QIcon('assets/pyqt/Icon.ico')) # pylint: disable=c-extension-no-member
        self.setFixedSize(self.size().width(), self.size().height())

        self.texture_converter = TextureConverter()
        self.convert_file_paths = ([], '')
        self.separate_file_paths = ([], '')
        self.invert_file_paths = ([], '')

        # Select files
        self.pushButton.clicked.connect(self.open_files_convert)
        self.pushButton_3.clicked.connect(self.open_files_separate)
        self.pushButton_5.clicked.connect(self.open_files_invert)

        # Convert selected files
        self.pushButton_2.clicked.connect(self.convert_files)
        self.pushButton_4.clicked.connect(self.separate_files)
        self.pushButton_6.clicked.connect(self.invert_files)

    def open_files_convert(self):
        '''
        The open_files_convert() function opens a file browser dialog
        to open files for the File Format Conversion tab.
        '''
        self.convert_file_paths = QFileDialog.getOpenFileNames(
            self,
            'Select image(s)',
            '',
            'Image files (*.png *.jpeg *.jpg *.tga *.dds)'
        )

        if len(self.convert_file_paths[0]) != 0:
            paths_length = len(self.convert_file_paths[0])

            self.label.setText(f'{paths_length} {"Files" if paths_length > 1 else "File"} Selected')
            self.textBrowser.clear()

            for path in self.convert_file_paths[0]:
                self.textBrowser.append(os.path.basename(path))

    def open_files_separate(self):
        '''
        The open_files_separate() function opens a file browser dialog
        to open files for the Mask Texture Separation tab.
        '''
        self.separate_file_paths = QFileDialog.getOpenFileNames(
            self,
            'Select image(s)',
            '',
            'Image files (*.png *.jpeg *.jpg *.tga *.dds)'
        )

        if len(self.separate_file_paths[0]) != 0:
            paths_length = len(self.separate_file_paths[0])

            self.label_4.setText(
                f'{paths_length} {"Files" if paths_length > 1 else "File"} Selected'
            )
            self.textBrowser_2.clear()

            for path in self.separate_file_paths[0]:
                self.textBrowser_2.append(os.path.basename(path))

    def open_files_invert(self):
        '''
        The open_files_invert() function opens a file browser dialog
        to open files for the Normal Map Conversion tab.
        '''
        self.invert_file_paths = QFileDialog.getOpenFileNames(
            self,
            'Select image(s)',
            '',
            'Image files (*.png *.jpeg *.jpg *.tga *.dds)'
        )

        if len(self.invert_file_paths[0]) != 0:
            paths_length = len(self.invert_file_paths[0])

            self.label_6.setText(
                f'{paths_length} {"Files" if paths_length > 1 else "File"} Selected'
            )
            self.textBrowser_3.clear()

            for path in self.invert_file_paths[0]:
                self.textBrowser_3.append(os.path.basename(path))

    def convert_files(self):
        '''
        The convert_files() function converts the selected files from the
        File Format Conversion tab to the specified file format.
        '''
        if len(self.convert_file_paths[0]) != 0:
            selected_format = self.comboBox.currentText()
            self.texture_converter.convert(self.convert_file_paths[0], selected_format)

            paths_length = len(self.convert_file_paths[0])

            self.show_message_box('success', paths_length)
        else:
            self.show_message_box('no_files')

    def separate_files(self):
        '''
        The separate_files() function separates the RGB channels of the selected files from the
        Mask Texture Separation tab to the specified file format.
        '''
        if len(self.separate_file_paths[0]) != 0:
            selected_format = self.comboBox_2.currentText()
            invert_roughness = self.checkBox.isChecked()
            self.texture_converter.separate(
                self.separate_file_paths[0],
                selected_format,
                invert_roughness
            )

            paths_length = len(self.separate_file_paths[0])

            self.show_message_box('success', paths_length)
        else:
            self.show_message_box('no_files')

    def invert_files(self):
        '''
        The invert_files() function inverts the green channel of the selected files from the
        Normal Map Conversion tab to the specified file format.
        '''
        if len(self.invert_file_paths[0]) != 0:
            selected_format = self.comboBox_3.currentText()
            self.texture_converter.invert(self.invert_file_paths[0], selected_format)

            paths_length = len(self.invert_file_paths[0])

            self.show_message_box('success', paths_length)
        else:
            self.show_message_box('no_files')

    def show_message_box(self, message_type, paths_length = 0):
        '''
        The show_message_box() functions shows a customizable message box
        based on the given message type.
        '''
        message = QMessageBox()
        message.setWindowIcon(QtGui.QIcon('assets/pyqt/Icon.ico')) # pylint: disable=c-extension-no-member

        if message_type == 'success':
            message.setWindowTitle('Success!')
            message.setIcon(QMessageBox.Icon.Information)
            message.setText(
                f'Successfully converted {paths_length} {"files" if paths_length > 1 else "file"}!'
            )
        elif message_type == 'no_files':
            message.setWindowTitle('No Files Selected!')
            message.setIcon(QMessageBox.Icon.Critical)
            message.setText('Please select files before trying to convert!')

        message.exec()

def main():
    '''
    The main() function is the entry point to the application which
    starts a window and shows the user interface.
    '''
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == '__main__':
    main()
