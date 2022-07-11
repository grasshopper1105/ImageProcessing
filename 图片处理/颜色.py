import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_red(img):
    redImg = img[:, :, 2]
    return redImg


def get_green(img):
    greenImg = img[:, :, 1]
    return greenImg


def get_blue(img):
    blueImg = img[:, :, 0]
    return blueImg


if __name__ == '__main__':
    img = cv2.imread("3600.jpg")
    b, g, r = cv2.split(img)
    # open_cv2.imshow("Blue 1", b)
    # open_cv2.imshow("Green 1", g)
    # open_cv2.imshow("Red 1", r)
    # b = get_blue(img)
    # g = get_green(img)
    # r = get_red(img)
    # open_cv2.imshow("Blue 2", b)
    # open_cv2.imshow("Green 2", g)
    # open_cv2.imshow("Red 2", r)
    # open_cv2.waitKey(0)
    # open_cv2.destroyAllWindows()
    # np.savetxt('b.txt',b)
    # np.savetxt('g.txt',g)
    # np.savetxt('r.txt',r)

    # [215, 213, 219]
    i = 69
    print('b', np.average(b[i, :]))
    print('g', np.average(g[i, :]))
    print('r', np.average(r[i, :]))
    plt.imshow(img)
    plt.show()
    # print('g',g)
    # print('r',r)
