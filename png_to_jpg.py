#importing the required package
from PIL import Image

#open image in png format
img_png = Image.open('C:\gfg\img.png')

#The image object is used to save the image in jpg format
img_png.save('C:\gfg\modified_img.jpg')
