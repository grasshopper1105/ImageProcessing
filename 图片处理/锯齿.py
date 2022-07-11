import cv2 as cv
import numpy as np

def cornerHarri(imgae):
    gray = cv.cvtColor(imgae, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 1, 0.06)
    dst = cv.dilate(dst, None)
    print(dst.shape)
    imgae[dst>0.01*dst.max()]=[255,0,0]
    cv.imshow("corn",imgae)


src = cv.imread("55.bmp")
cornerHarri(src)
#cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imwrite('555.bmp',src)
cv.waitKey(0)

cv.destroyAllWindows()