import os
import numpy as np

from PIL import Image

img_dir = '/alldata'
number_of_picture = len(os.listdir(img_dir))  # 850 pictures

R = 0
G = 0
B = 0

for name in os.listdir(img_dir):
    I = Image.open(os.path.join('/alldata', name))

    a = np.array(I).size
    pixel_number_of_a_channel = a / 3

    one_image_pi_value = np.array(I) / 255

    R_channel = np.sum(one_image_pi_value[:, :, 0]) / pixel_number_of_a_channel
    G_channel = np.sum(one_image_pi_value[:, :, 1]) / pixel_number_of_a_channel
    B_channel = np.sum(one_image_pi_value[:, :, 2]) / pixel_number_of_a_channel

    R = R + R_channel
    G = G + G_channel
    B = B + B_channel

print(R / 8000)
print(G / 8000)
print(B / 8000)
