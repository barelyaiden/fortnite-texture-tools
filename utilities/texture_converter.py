'''The PIL library has tools to manipulate images with code.'''
from PIL import Image, ImageChops

class TextureConverter:
    '''
    The TextureConverter class has multiple functions for converting texture file formats,
    separating RGB channels, etc.
    '''
    def __init__(self, image, file_format):
        self.image = image
        self.file_format = file_format

    def convert(self):
        '''The convert() function converts a texture from one file format to another.'''
        Image.open(self.image).save(f'{self.image}.{self.file_format}')

    def separate(self, invert_roughness = False):
        '''
        The separate() function separates the RGB channels of a texture,
        most commonly used for _M and _S textures as each RGB channel
        contains a different mask texture.
        '''
        mask_texture = Image.open(self.image)
        r_specular, g_metallic, b_roughness = mask_texture.split()

        r_specular.save(f'{self.image[:len(self.image) - 6]}_S.{self.file_format}')
        g_metallic.save(f'{self.image[:len(self.image) - 6]}_M.{self.file_format}')

        if invert_roughness is True:
            ImageChops.invert(b_roughness).save(
                f'{self.image[:len(self.image) - 6]}_R.{self.file_format}'
            )
        else:
            b_roughness.save(f'{self.image[:len(self.image) - 6]}_R.{self.file_format}')

    def invert_green(self):
        '''
        The invert_green() function inverts the green channel of the image,
        most commonly used for _N textures to change between
        DirectX and OpenGL normals.
        '''
        normal_texture = Image.open(self.image)
        red, green, blue = normal_texture.split()
        Image.merge('RGB', (red, ImageChops.invert(green), blue)).save(
            f'{self.image}.{self.file_format}'
        )
