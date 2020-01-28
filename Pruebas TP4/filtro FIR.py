#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:43:33 2019

@author: fede
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift
import scipy.io as sio
from time import time

mat_struct = sio.loadmat('ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten(1)
cant_muestras = len(ecg_one_lead)

clean_ecg = ecg_one_lead[0:95000]

N = 95000
X = fft(clean_ecg, axis=0)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
freq = freq * 1000
plt.plot(freq, modX)

#freqX, Xw = sig.welch(clean_ecg,fs=1000, nperseg=10000)
#freqX2, Xw2 = sig.welch(ecg_one_lead,fs=1000, nperseg=10000)
#
#Xw = 20*np.log10(Xw)
#Xw2 = 20*np.log10(Xw2)
#plt.plot(freqX, Xw)
#plt.plot(freqX2, Xw2)

#plt.plot(clean_ecg)
#med = np.mean(clean_ecg)
#med = 20*np.log10(med)