import numpy as np #memanggil library numpy
import cv2 #memanggil library opencv
import matplotlib.pyplot as plt #memanggil library matplotlib
from scipy import ndimage #memangil library ndimage dari scipy


im = cv2.imread('D:\KULIAH\SMT 6\PCD\DIP\logo.png')#membaca file gambar
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
data = np.array(gray, dtype=float)

kernel = np.array([[-1, -1, -1, -1, -1],
                   [-1,  1,  2,  1, -1],
                   [-1,  2,  4,  2, -1],
                   [-1,  1,  2,  1, -1],
                   [-1, -1, -1, -1, -1]])#matrik untuk operasi hpf
highpass_5x5 = ndimage.convolve(data, kernel)#operasi hpf

hist1,bins1 = np.histogram(highpass_5x5.flatten(),256,[0,256]) #
cdf1 = hist1.cumsum() #                                     membuat histogram gambar dari hasil highpassfilter pass filter pada highpass_5x5
norm1 = cdf1 * hist1.max()/ cdf1.max()

cv2.imshow('Grayscale',gray)
cv2.imshow('Highpass_5x5',highpass_5x5)
plt.plot(norm1, color = 'b')
plt.hist(highpass_5x5.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

