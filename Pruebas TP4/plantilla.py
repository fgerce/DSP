#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:10:06 2020

@author: fede
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.fftpack import fft, fftshift
from spectrum import CORRELOGRAMPSD
from spectrum.tools import cshift
import scipy.io as sio

fs = 1000
mat_struct = sio.loadmat('ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten(1)
#ecg_one_lead = ecg_one_lead[15000:20000]
cant_muestras = len(ecg_one_lead)

freqX, Xw = sig.welch(ecg_one_lead, fs, axis=0)

X = fft(ecg_one_lead)
modX = np.abs(fftshift(X))*2/cant_muestras
center = int(np.floor(cant_muestras/2))
modX = modX[center:cant_muestras]
modX = 20*np.log10(modX)
freq = np.linspace(0, fs/2, len(modX))

plt.plot(freq, modX)
#plt.figure(1)
#plt.plot(ecg_one_lead)
#plt.figure(2)
#plt.plot(freqX, Xw)