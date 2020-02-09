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
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

start_time = time()
diff = sig.medfilt(ecg_one_lead, 201)
diff = sig.medfilt(diff, 601)
end_time = time()

sustr = ecg_one_lead - diff
total_time = end_time - start_time

plt.plot(ecg_one_lead, label="Original")
plt.plot(sustr, label="Filtrada con medianas")
plt.title("Comparativa señal original y con filtro de mediana")
plt.legend()

freqX, Xw = sig.welch(diff,fs=1000)
acum = np.cumsum(Xw)

aux = (acum < 0.99*acum[-1])
Xw = 20*np.log10(Xw)
plt.plot(freqX, Xw)

