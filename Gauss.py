# 2036497 Franklin Ajuluchukwu
# 2036138 Segun Badmus
# Gaussian blur (also known as Gaussian smoothing) is the result of blurring an image by a Gaussian function

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read-in picture 
img = cv2.imread('balloon.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# Gauss filtering 
result = cv2.GaussianBlur(source, (37,37), 1.9)
#Graphical representation
titles = [' original image ', ' Gauss filtering ']
images = [source, result]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
