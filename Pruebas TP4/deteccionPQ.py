#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 01:05:52 2020

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
QRS_det = mat_struct['qrs_detections']
QRS_det = QRS_det.flatten()
ecg_one_lead = ecg_one_lead.flatten()
clean_ecg = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

for i in range (0,len(QRS_det)-1):
       start = QRS_det[i] - 120
       stop = QRS_det[i] - 35
       next_s = QRS_det[i+1] - 120
       seg1 = np.mean(ecg_one_lead[start:stop])
       ecg_one_lead[start:next_s] = ecg_one_lead[start:next_s] - seg1

plt.vlines(QRS_det-35,-35000, 35000, colors='red', ls='dotted')
plt.vlines(QRS_det-120,-35000, 35000, colors='black', ls='dotted')

plt.plot(ecg_one_lead)
plt.plot(clean_ecg)