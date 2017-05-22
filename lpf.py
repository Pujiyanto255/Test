import numpy as np #memanggil library numpy
import cv2 #memanggil library opencv
from matplotlib import pyplot as plt #memanggil library pyplot

img = cv2.imread('D:\KULIAH\SMT 6\PCD\DIP\logo.png') #mengambil file gambar
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #mengkonversi gambar berwarna mengjadi grayscale

kernel = np.ones((5,5),np.float32)/25 #matrix 5x5 yang berisikan angka 1, lalu dibagi 25 untuk low pass filter
#kernel2 = np.ones((3,3),np.float32)/9 

lpf = cv2.filter2D(gray,-1,kernel) #low pass filter gambar dengan matrix pada variable kernel
#lpf2 = cv2.filter2D(gray,-1,kernel2)
hist1,bins1 = np.histogram(lpf.flatten(),256,[0,256]) #
cdf1 = hist1.cumsum() #                                     membuat histogram gambar dari hasil low pass filter pada lpf
norm1 = cdf1 * hist1.max()/ cdf1.max() #
equ = cv2.equalizeHist(lpf) #mengolah gambar dengan histogram equalization
res = np.hstack((lpf,equ))
cv2.imwrite('res.png',res) #menyimpan gambar histogram equalization satu folder dengan lokasi program
cv2.imshow('Org',img) #menampilkan gambar asli
cv2.imshow('Gray',gray) #menampilkan gambar grayscale
cv2.imshow('LPF 5x5',lpf) #menampilkan gambar hasil low pass filter
plt.plot(norm1, color = 'b')
plt.hist(lpf.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show() #menampilkan histogram gambar hasil low pass filter
# cv2.imshow('Org',img)
# cv2.imshow('LPF 3x3',lpf2)
# cv2.imshow('LPF 5x5',lpf)

cv2.waitKey(0)
cv2.destroyAllWindows()

