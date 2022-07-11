# 导入库
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import cv2
import paddlehub as hub
import time
from PIL import Image

matplotlib.use('TkAgg')  # 不写这个plt没用

start = time.time()
# 待检测图像
image_path_list = ["1.jpg", "2.jpg"]  # 这里传入一个列表，这里我就处理一张图片
img = [cv2.imread(image_path) for image_path in image_path_list]

module = hub.Module(name="deeplabv3p_xception65_humanseg")
input_dict = {"image": image_path_list}
# execute predict and print the result
results = module.segmentation(data=input_dict)

for i in range(1):  # 处理一张图所以range(1)
    prediction = results[i]["data"]
    newimg = np.zeros(img[i].shape)
    newimg[:, :, 0] = img[i][:, :, 0] * (prediction > 0)
    newimg[:, :, 1] = img[i][:, :, 1] * (prediction > 0)
    newimg[:, :, 2] = img[i][:, :, 2] * (prediction > 0)
    cv2.imwrite('test.jpg', newimg)
    newimg = newimg.astype(np.uint8)

    end = time.time()
    print('time cost:', (end - start), 's')
    # 预测结果展示
    plt.figure(figsize=(10, 10))
    plt.imshow(newimg)
    plt.axis('off')
    plt.show()


def replace_color(img, src_clr, dst_clr):
    '''
    通过矩阵操作颜色替换程序
    :param img: 图像矩阵
    :param src_clr: 需要替换的颜色(r,g,b)
    :param dst_clr: 目标颜色(r,g,b)
    :return: 替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)
    # 分离通道
    r_img = img_arr[:, :, 0].copy()
    g_img = img_arr[:, :, 1].copy()
    b_img = img_arr[:, :, 2].copy()

    # 编码
    img = r_img * 256 * 256 + g_img * 256 + b_img
    src_color = src_clr[0] * 256 * 256 + src_clr[1] * 256 + src_clr[2]

    # 索引并替换颜色
    r_img[img == src_color] = dst_clr[0]
    g_img[img == src_color] = dst_clr[1]
    b_img[img == src_color] = dst_clr[2]

    # 合并通道
    dst_img = np.array([r_img, g_img, b_img], dtype=np.uint8)
    # 将数据转换为图像数据(h,w,c)
    dst_img = dst_img.transpose(1, 2, 0)

    return dst_img


def replace_color_tran(img, src_clr, dst_clr):
    '''
    通过遍历颜色替换程序
    :param img: 图像矩阵
    :param src_clr: 需要替换的颜色(r,g,b)
    :param dst_clr: 目标颜色(r,g,b)
    :return: 替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)

    dst_arr = img_arr.copy()
    for i in range(img_arr.shape[1]):
        for j in range(img_arr.shape[0]):
            if (img_arr[j][i] == src_clr)[0] == True:
                dst_arr[j][i] = dst_clr

    return np.asarray(dst_arr, dtype=np.uint8)


# 需要修改的文件
img = 'test.jpg'
img = Image.open(img).convert('RGB')
res_img = img.copy()
count = 20

for i in range(count):
    # 需要替换的颜色、替换成的颜色
    dst_img = replace_color(img, (0, 0, 0), (255, 255, 255))
    res_img = dst_img

res_img = Image.fromarray(res_img)
# 更改后保存的文件
res_img.save('result.jpg')
