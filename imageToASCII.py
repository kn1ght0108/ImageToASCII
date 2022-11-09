import sys
import math
from PIL import Image, ImageStat

def imgToASCII(image, resolution):
    width, height = image.size
    rows = math.floor(height/resolution)
    cols = math.floor(width/resolution)
    ascii_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1}{[]?-_+~<>i!lI;:,\"^`'. "
    ascii_txt = ""
    for row in range(rows):
        y_upper = row * resolution
        y_lower = y_upper + resolution
        for col in range(cols):
            x_upper = col * resolution
            x_lower = x_upper + resolution
            tile = image.crop((x_upper,y_upper,x_lower,y_lower))
            avg_lum = ImageStat.Stat(tile)._getmean()
            asciival = ascii_scale[math.ceil(((avg_lum[0]*69)/255))]
            ascii_txt += 2*asciival
        ascii_txt += "\n"
    return ascii_txt

image_path = sys.argv[1]
resolution = int(sys.argv[2])
image = Image.open(image_path).convert("L")
print(imgToASCII(image, resolution))

