import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = '111.bmp'
img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)  # red=76
img = np.array(img)
m,n = img.shape
print(m,n)
x = []
y = []
for rows in range(m-4,200,-3):
    y.append(rows)
    mids = []
    mids2 = []
    for cols in range(0,n-4):
        if img[rows,cols] == 76 and img[rows+2,cols] != 29 and img[rows-2,cols] != 29 and img[rows,cols-2] != 29 and img[rows,cols+2] != 29:
            mids.append(cols)
            # if len(mids) > 2:
            #     if len(mids) % 2 == 0:
            #         mids2 = mids[int((len(mids)/2)):int((len(mids)/2+1))]
            #     else:
            #         a = int((len(mids)-1)/2)
            #         mids2 = mids[a-1:a+1]
            # x.append(mid)
    x.append(np.mean(mids))

img2 = cv2.imread(image_path,cv2.IMREAD_ANYCOLOR)
img2 = img2[:,:,[2,1,0]]
x = np.array(x)

fig, ax = plt.subplots()
ax.imshow(img2)
ax.plot(x, y)
plt.show()