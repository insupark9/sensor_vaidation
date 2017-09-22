import numpy as np 
import cv2
import matplotlib.pyplot as plt

def calculate_mean(img_bayer):
#    img_bayer = np.array(img)

    Gr = img_bayer[::2, ::2]
    R  = img_bayer[::2, 1::2]
    B  = img_bayer[1::2, ::2]
    Gb = img_bayer[1::2, 1::2]

    mean_r  = np.mean(R)
    mean_gr = np.mean(Gr)
    mean_gb = np.mean(Gb)
    mean_b  = np.mean(B)
    return mean_gr, mean_gb, mean_r, mean_b