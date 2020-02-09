#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:21:49 2020

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
ECG_medfilt = np.load("ECG_medfilt.npy")
pattern = mat_struct['heartbeat_pattern1']
pattern = pattern.flatten()
QRS_det = mat_struct['qrs_detections']
QRS_det = QRS_det.flatten()

res = np.correlate(ECG_medfilt, pattern)
res = (res/np.max(res))*np.max(ECG_medfilt)
# plt.plot(res, label="Correlacion")
plt.figure(1)
plt.plot(ECG_medfilt, label="Señal filtrada")
plt.legend()

peaks = sig.find_peaks(ECG_medfilt, distance=len(pattern), prominence=0.6)
peaks = peaks[0]
peaks = peaks

peaksY = np.zeros(len(peaks))
for ii in range(0,len(peaks)):
       peaksY[ii] = ECG_medfilt[peaks[ii]]
       
plt.plot(peaks, peaksY, 'rx', label="Detección de latidos")
plt.legend()

plt.figure(2)
plt.plot(peaks, 'go', label="Serie de detección de picos")
plt.plot(QRS_det, 'bo', label ="Ubicación real de picos")
plt.xlabel("Posición en el vector")
plt.ylabel("Ubicación del latido en el ECG")
plt.legend()

tick = np.zeros(101)
for ii in range(-50, 50):
       tick[ii+50] = len(set(QRS_det).intersection(peaks-ii))