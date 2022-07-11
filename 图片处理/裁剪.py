import cv2

# 读取图片
img = '5.bmp'
img = cv2.imread(img)
cv2.imshow('original', img)

# 选择ROI
roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
print(roi)

# 显示ROI并保存图片
if roi != (0, 0, 0, 0):
    crop = img[y:y+h, x:x+w]
    cv2.imshow('crop', crop)
    cv2.imwrite('5.bmp', crop)
    print('Saved!')

# 退出
cv2.waitKey(0)
cv2.destroyAllWindows()