# installation of pillow library
# change the image extenssion 
# resize image files
# resize multiple images using for Loop
# sharpness
# brightness
# Color
# contrast
# image blur, gaussianblur

from  PIL import Image,ImageEnhance,ImageFilter
import os

# img1 = Image.open('download.jpg')
# img1.save('download.png')
# img1.save('download.pdf')
# img1.show()
# 250
# MAX_SIZE =(250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('downloadsmall.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'(filename).png')

#   -----------sharpness--------------
# img1 = Image.open('dog2.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(2).save('dog1edited.jpg')
# 0 : blurry
# 1 : original image
# 2 :image with increased sharpness

#  ---------------color------------------
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save('dog1coloredit.jpg')

#   ----------brigthness--------------
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(3).save('dog1editedbright.jpg')


# ----------------contrast----------------
img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.5).save('dog2editcontrast.jpg')

# image blur

img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog2bluredited.jpg')