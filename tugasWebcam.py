import numpy as np
import cv2

capture = cv2.VideoCapture(0) #inisialisasi webcam. angka "0" berarti webcam internal
alpha = 1.5 #mengubah nilai brightness
beta = 25
while (1): #looping imshow, jadi seolah olah camera menangkap objek secara video realtime
	
	val, frame = capture.read()#menangkap gambar dengan format berwarna /BGR
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#mengkonversi dari berwarna ke grayscale
	negative = (255 - gray)#perintah membuat citra negative effect dari grayscale
	#changebright = (1 + gray)
	ColorBright = cv2.addWeighted(frame,alpha, np.zeros(frame.shape, frame.dtype), 0, beta)#mengubah brightness citra berwarna / BGR
	GrayBright = cv2.addWeighted(gray,alpha, np.zeros(gray.shape, gray.dtype), 0, beta)#mengubah brightness citra grayscale
	cv2.imshow('ColorBright',ColorBright) #menampilkan citra berwarna dengan brightness yang telah diubah
	cv2.imshow('Original',frame)#menampilkan citra berwarna yang asli
	cv2.imshow('Gray',gray)#menampilkan citra grayscale
	cv2.imshow('Negative Effect',negative)#menampilkan citra negative effect grayscale
	cv2.imshow('GrayBright',GrayBright)#menampilkan citra grayscale dengan brightness yang telah diubah
	#cv2.imshow('Change Bright',changebright)
	if cv2.waitKey(1) & 0xFF == ord('k'):#perintah untuk menghentikan program dengan menekan tombol k pada keyboard
		break
		


cv2.destroyAllWindows()
capture.release()
