f = open('2.bmp', 'rb')  # 只读，二进制打开，

'1、文件头:一共14字节'
bfType = f.read(2)  # 文件类型
bfSize1 = f.read(4)  # 该bmp文件总大小
f.seek(f.tell() + 4)  # 跳过保留字
bfOffBits1 = f.read(4)  # 从文件开始到数据开始的偏移量，    偏移1078 加上256*256正好是文件的大小（单位：B）

# struct.unpack('i',*) 也可以
bfSize = int.from_bytes(bfSize1, byteorder='little', signed=True)
bfOffBits = int.from_bytes(bfOffBits1, byteorder='little', signed=True)

'2、信息头：40B'
biSize = f.read(4)  # 这部分长度为40字节
biWidth1 = f.read(4)
biHeight1 = f.read(4)
biPlanes = f.read(2)  # 1,位图的位面数
biBitCount1 = f.read(4)

# struct.unpack('i',*) 也可以
biWidth = int.from_bytes(biWidth1, byteorder='little', signed=True)
biHeight = int.from_bytes(biHeight1, byteorder='little', signed=True)
biBitCount = int.from_bytes(biBitCount1, byteorder='little', signed=True)

print('文件类型{0}，大小{1}，偏移量{2}，位图宽度（列）{3}，高度（行）{4}，每个像素所占位数{5}'.format(bfType, bfSize, bfOffBits, biWidth, biHeight,
                                                                    biBitCount))