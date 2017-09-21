import numpy as np 
import cv2
import matplotlib.pyplot as plt

def calculate_statics(img):
    img_bayer = np.array(img)
    Gr = img_bayer[::2, ::2]
    R  = img_bayer[::2, 1::2]
    B  = img_bayer[1::2, ::2]
    Gb = img_bayer[1::2, 1::2]

    print R.shape
    mean_r  = np.mean(R)
    mean_gr = np.mean(Gr)
    mean_gb = np.mean(Gb)
    mean_b  = np.mean(B)
    
    if 0:
        print('mean_r  = ', mean_r)
        print('mean_gr = ', mean_gr)
        print('mean_gb = ', mean_gb)
        print('mean_b  = ', mean_b)

#    hist = cv2.calcHist([img_bayer], [0], None, [256], [0, 256])
    #img_1d = img_bayer[0,:]
    #print('img_1d', img_1d)
    #hist, bin_edges = np.histogram(img_1d, range=(img_1d.min(), img_1d.max()))
    #plt.hist(hist)
    #plt.show()
  #  plt.hist(img_1d, bins='auto')
  #  plt.show()
    return mean_gr, mean_gb, mean_r, mean_b

def calculate_mean():
    b = [[1, 2], [3, 4]]
    a = np.array([[1, 2], [3, 5]])
    m = np.mean(b)
    m_1 = np.mean(a, axis=0)
    m_2 = np.mean(a, axis=1)
    print('mean_m, mean m_1 and m_2 are:', m, m_1, m_2)