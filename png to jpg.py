#importing required packages and library
import cv2

# Loading .png image
png_img = cv2.imread('img.png')

# converting to jpg file
#saving the jpg file
cv2.imwrite('modified_img.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
