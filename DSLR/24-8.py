import os
import cv2
import numpy as np
from PIL import Image

# 24位转8位灰度
image1 = Image.open('C:/Users/cui/Desktop/code/DSLR-release-861429482faf50ee3d6570948af8c48df1fc7f43/data/training_dataset/data directory/1.bmp')
image2 = Image.fromarray(np.uint8(image1))
print(image2.mode)
t = image2.convert("L")
print(t.mode)
image3 = Image.fromarray(np.uint8(t) * 255)
print(image3.mode)
image3.save('C:/Users/cui/Desktop/code/DSLR-release-861429482faf50ee3d6570948af8c48df1fc7f43/data/training_dataset/data directory/1.jpg')



