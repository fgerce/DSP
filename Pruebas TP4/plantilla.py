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
ecg_one_lead = ecg_one_lead.flatten()
ecg_one_lead = ecg_one_lead[1000:60000]
cant_muestras = len(ecg_one_lead)

K = 10 #Bloques de welch
L = cant_muestras/K
freqS, welchS = sig.welch(ecg_one_lead, fs,nperseg=L,window='bartlett')
welchS = 20*np.log10(welchS)

plt.figure(1)
plt.plot(ecg_one_lead)
plt.xlabel('# muestra')
plt.ylabel('Amplitud')
plt.grid()

plt.figure(2)
plt.plot(freqS, welchS)
plt.xlabel('Frecuencia  [Hz]')
plt.ylabel('Amplitud [dB]')
plt.xlim(30, 120)
plt.grid()