'''
The os library has tools to work with the operating system.
The PIL library has tools to manipulate images with code.
'''
import os
from PIL import Image, ImageChops

class TextureConverter:
    '''
    The TextureConverter class has multiple functions for converting image file formats,
    separating RGB channels, etc.
    '''
    def convert(self, files, file_format):
        '''The convert() function converts an image from one file format to another.'''
        for file in files:
            file_path = f'{os.path.dirname(file)}/Converted'
            file_name = os.path.basename(file)

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            Image.open(file).save(
                f'{file_path}/{file_name[:len(file_name) - 4]}.{file_format.lower()}'
            )

    def separate(self, files, file_format, invert_roughness = False):
        '''
        The separate() function separates the RGB channels of an image,
        most commonly used for _M and _S textures as each RGB channel
        contains a different mask texture.
        '''
        for file in files:
            file_path = f'{os.path.dirname(file)}/Converted'
            file_name = os.path.basename(file)

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            mask_texture = Image.open(file)
            mask_channels = mask_texture.split()

            mask_channels[0].save(
                f'{file_path}/{file_name[:len(file_name) - 4]}_R.{file_format.lower()}'
            )
            mask_channels[1].save(
                f'{file_path}/{file_name[:len(file_name) - 4]}_G.{file_format.lower()}'
            )

            if invert_roughness is True:
                ImageChops.invert(mask_channels[2]).save(
                    f'{file_path}/{file_name[:len(file_name) - 4]}_B.{file_format.lower()}'
                )
            else:
                mask_channels[2].save(
                    f'{file_path}/{file_name[:len(file_name) - 4]}_B.{file_format.lower()}'
                )

    def invert(self, files, file_format):
        '''
        The invert() function inverts the green channel of an image,
        most commonly used for _N textures to switch between
        DirectX and OpenGL normals.
        '''
        for file in files:
            file_path = f'{os.path.dirname(file)}/Converted'
            file_name = os.path.basename(file)

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            normal_texture = Image.open(file)
            normal_channels = normal_texture.split()
            Image.merge(
                'RGB',
                (normal_channels[0], ImageChops.invert(normal_channels[1]), normal_channels[2])
            ).save(f'{file_path}/{file_name[:len(file_name) - 4]}.{file_format.lower()}')
