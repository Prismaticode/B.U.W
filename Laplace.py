# 2036497 Franklin Ajuluchukwu
# 2036138 Segun Badmus
#Laplacian filter is an edge detector used to compute the second derivatives of an image, 
# measuring the rate at which the first derivatives change. 
# This determines if a change in adjacent pixel values is from an edge or continuous progression.

from matplotlib import pyplot as plt
import cv2
image2=cv2.imread('wallimg.jpg')
new_image = cv2.Laplacian(image2,cv2.CV_64F,ksize=7)
plt.figure(figsize=(11,6))
plt.subplot(131), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(new_image, cmap='gray'),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(image2 + new_image, cmap='gray'),plt.title('Resulting image')
plt.xticks([]), plt.yticks([])
plt.show()