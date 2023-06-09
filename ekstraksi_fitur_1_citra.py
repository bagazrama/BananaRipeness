""" 
Ekstraksi Fitur Warna
by Rivansyah Suhendra
@ 2023
Program Studi Teknologi Informasi
"""

import cv2
import numpy as np
from scipy.stats import skew, kurtosis

# inisialisasi array fitur
fitur = []

img = cv2.imread('cr7.jpg')

# pemisahan nilai masing-masing channel
R = (img[:, :, 2])
G = (img[:, :, 1])
B = (img[:, :, 0])

meanR = np.mean(R)
meanG = np.mean(G)
meanB = np.mean(B)

stdR = np.std(R)
stdG = np.std(G)
stdB = np.std(B)

# konversi matrix to array
Rflat = R.flatten()
Gflat = G.flatten()
Bflat = B.flatten()

skewR = skew(Rflat)
skewG = skew(Gflat)
skewB = skew(Bflat)

kurtR = kurtosis(Rflat)
kurtG = kurtosis(Gflat)
kurtB = kurtosis(Bflat)

fitur.append([meanR, meanG, meanB, stdR, stdG, stdB,
              skewR, skewG, skewB, kurtR, kurtG, kurtB])


print(fitur)
