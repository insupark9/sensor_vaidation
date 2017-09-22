import numpy as np 
import matplotlib.pyplot as plt
import calculate_statics as cs 
import read_raw_data as rd 

DEBUG = 0

width  = 1280
height = 1088
dg_value = [256, 512, 1024, 2048, 4096]

mean_gr = [] 
mean_gb = [] 
mean_r = [] 
mean_b = [] 

for value in dg_value:
    filename = './Images/frame-000097_long_' + str(value) + '.bin'

    img = rd.read_raw_data(filename, height, width)
    m_gr, m_gb, m_r, m_b = cs.calculate_mean(img)
    mean_gr.append(m_gr)
    mean_gb.append(m_gb)
    mean_r.append(m_r)
    mean_b.append(m_b)

if DEBUG:
    print('mean_r  = ', mean_r)
    print('mean_gr = ', mean_gr)
    print('mean_gb = ', mean_gb)
    print('mean_b  = ', mean_b)

#mean = [mean_gr, mean_gb, mean_r, mean_b]

dg_value = np.array(dg_value) / 256

plt.subplot(2, 2, 3)
plt.plot(dg_value, mean_b, '--bo' )
plt.title('Component B')
plt.ylabel('Mean pixel value')
plt.xlabel('Digital gain [X]')

plt.subplot(2, 2, 2)
plt.plot(dg_value, mean_r, '--ro' )
plt.title('Component R')
plt.ylabel('Mean pixel value')
plt.xlabel('Digital gain [X]')

plt.subplot(2, 2, 1)
plt.plot(dg_value, mean_gr, '--gs' )
plt.title('Component GR')
plt.ylabel('Mean pixel value')
plt.xlabel('Digital gain [X]')

plt.subplot(2, 2, 4)
plt.plot(dg_value, mean_gb, '--go' )
plt.title('Component GB')
plt.ylabel('Mean pixel value')
plt.xlabel('Digital gain [X]')

plt.show()