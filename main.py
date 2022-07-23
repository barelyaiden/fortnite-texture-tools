'''The TextureConverter class provides the main source of the program's logic.'''
from utilities.texture_converter import TextureConverter

texture_converter = TextureConverter('image.tga', 'png')

texture_converter.convert()
# The boolean parameter will dictate whether or not to invert the Roughness map on the _S texture.
texture_converter.separate(True)
texture_converter.invert_green()
