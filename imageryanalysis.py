#GreenTapir, date edited: 10/12/18, challenge 3. most of this code came from the slides. numpy standard deviation came from
#https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.std.html

from __future__ import division
from PIL import Image
import glob
import matplotlib
import numpy as np
matplotlib.use('TkAgg') #makes matplotlib work
import matplotlib.pyplot as plt

imgs = []

imagenames = sorted(glob.glob("unionconstruction_*.jpg")) #reading image names into string to be opened.
imagenames = imagenames[0:199]

for i in imagenames: #opens images, converts to float, appends to list of images matrices
    img = Image.open(i)
    img = np.float32(img)
    imgs.append(img)

avg_img = imgs[0]

for j in range(1, len(imgs)):
    avg_img+=imgs[j]

result5 = 0

avg_img/=len(imgs)

for h in imgs:
    result5 += (h - avg_img)**2

result2 = result5/len(imgs)
result3 = np.sqrt(result2)

changeThreshold = input("Enter change threshold: ")

if changeThreshold >= 0 and changeThreshold <= 255:
    for row in range(0, len(avg_img)):
        for col in range(0, len(avg_img[row])):
            if (result3[row][col] > [changeThreshold, changeThreshold, changeThreshold]).any():
                avg_img[row][col] = [255, 0, 0] #highlights pixels as red


    avg_img = np.clip(avg_img, 0, 255)

    avg_img = np.uint8(avg_img) #converts from float to int to show image

    plt.imshow(avg_img)
    plt.show()
else:
    print "\nThis is not a valid threshold!"


