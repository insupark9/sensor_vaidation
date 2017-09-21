import numpy as np 
import matplotlib.pyplot as plt
import calculate_statics as cs 
import read_raw_data as rd 


filename = './frame.bin'
width  = 1280
height = 1088

img = rd.read_raw_data(filename, height, width)
mean_gr, mean_gb, mean_r, mean_b = cs.calculate_statics(img)

print('mean_r  = ', mean_r)
print('mean_gr = ', mean_gr)
print('mean_gb = ', mean_gb)
print('mean_b  = ', mean_b)

mean = [mean_gr, mean_gb, mean_r, mean_b]

plt.plot(mean)
plt.show()