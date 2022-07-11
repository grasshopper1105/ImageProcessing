import cv2
import numpy as np

image_path = '5.png'
img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
img = np.array(img)
m,n = img.shape
for i in range(m):
    for j in range(n):
        if img[i][j] > 200:
            img[i][j] = 255
        else:
            img[i][j] = 0

cv2.imwrite('5.bmp',img)