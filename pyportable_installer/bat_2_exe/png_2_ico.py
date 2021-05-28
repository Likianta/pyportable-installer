"""
Convert jpg, png, etc. to ico.

Requirements:
    pillow
    
BTW: You can find a convertion tool online, for example this site:
    https://www.easyicon.net/covert/
"""
from PIL import Image


def dialog():
    file_i = input('image: ')
    file_o = file_i.removesuffix('.png') + '.ico'
    main(file_i, file_o)


def main(file_i, file_o):
    img = Image.open(file_i)
    img.save(file_o)
    img.close()
    
    
if __name__ == '__main__':
    dialog()
