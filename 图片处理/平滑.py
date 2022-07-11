import cv2
import numpy as np

INPUT = cv2.imread('brain-out.bmp',0)
# MASK = np.array(INPUT/255.0, dtype='float32')
#
# MASK = open_cv2.GaussianBlur(MASK, (5,5), 11)
# BG = np.ones([INPUT.shape[0], INPUT.shape[1], 1], dtype='uint8')*255
#
# OUT_F = np.ones([INPUT.shape[0], INPUT.shape[1], 1],dtype='uint8')
#
# for r in range(INPUT.shape[0]):
#     for c in range(INPUT.shape[1]):
#         OUT_F[r][c]  = int(BG[r][c]*(MASK[r][c]) + INPUT[r][c]*(1-MASK[r][c]))

cv2.imwrite('brain-out.bmp', INPUT)