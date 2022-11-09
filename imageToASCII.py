import sys
import math
from PIL import Image, ImageStat

def imgToASCII(image, num_pixels):
    width, height = image.size
    rows = math.floor(height/num_pixels)
    cols = math.floor(width/num_pixels)
    ascii_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1}{[]?-_+~<>i!lI;:,\"^`'. "
    ascii_txt = ""
    for row in range(rows):
        y_upper = row * num_pixels
        y_lower = y_upper + num_pixels
        for col in range(cols):
            x_upper = col * num_pixels
            x_lower = x_upper + num_pixels
            tile = image.crop((x_upper,y_upper,x_lower,y_lower))
            avg_lum = ImageStat.Stat(tile)._getmean()
            asciival = ascii_scale[math.ceil(((avg_lum[0]*69)/255))]
            ascii_txt += 2*asciival
        ascii_txt += "\n"
    return ascii_txt

image_path = sys.argv[1]
num_pixels = int(sys.argv[2])
image = Image.open(image_path).convert("L")
print(imgToASCII(image, num_pixels))

