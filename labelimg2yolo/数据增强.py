import os
import albumentations as A
import cv2 as cv

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
trans = A.Compose(
    [
        A.HorizontalFlip(p=0.5),
        # A.Transpose(),
        A.OneOf([
            A.ISONoise(),
            A.GaussNoise(),
        ], p=0.3),
        A.OneOf([
            A.MotionBlur(p=0.2),
            A.MedianBlur(blur_limit=3, p=0.1),
            A.Blur(blur_limit=3, p=0.1),
        ], p=0.5),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        A.OneOf([
            A.OpticalDistortion(p=0.3),
            A.GridDistortion(p=0.1),
            A.PiecewiseAffine(p=0.3),
        ], p=0.5),
        A.OneOf([
            A.CLAHE(clip_limit=2),
            A.Sharpen(),
            A.Emboss(),
            A.RandomBrightnessContrast(),
        ], p=0.5),
        A.HueSaturationValue(p=0.3),
    ])


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
    return L


files = file_name('F:\\Python\\pycharm-community-2019.3.1\\AI\\insects\\la')
for i in range(len(files)):
    files_pth = str(files[i].split('.')[0]) + '.' + str(files[i].split('.')[1]) + '.' + str(files[i].split('.')[2])
    image = cv.imread(files[i])
    img = trans(image=image)['image']
    files_name = str(files_pth) + 'new3.jpg'
    print(files_name)
    cv.imwrite(files_name, img)
