# 2036497 Franklin Ajuluchukwu
# 2036138 Segun Badmus
# Box Filter: is similar to the averaging blur operation, it applies a bilateral image
# to a filter. Choice can be made on whether the box should be normalized or not.
import cv2
import matplotlib.pyplot as plt
# Read the picture 
img = cv2.imread('chess.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# Box filtering 
result = cv2.boxFilter(source, -1, (3,3), normalize=5)
# The graphics 
titles = ['Original image ', ' Box filtered image ']
images = [source, result]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
