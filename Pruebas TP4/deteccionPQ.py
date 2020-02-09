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
from scipy.interpolate import CubicSpline

mat_struct = sio.loadmat('ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead']
QRS_det = mat_struct['qrs_detections']
QRS_det = QRS_det.flatten()
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)
QRS_means = np.zeros(len(QRS_det))

for i in range (0,len(QRS_det)-1):
       start = QRS_det[i] - 120
       stop = QRS_det[i] - 35
       next_s = QRS_det[i+1] - 120
       QRS_means[i] = np.mean(ecg_one_lead[start:next_s])
       
QRS_x = QRS_det - 77 #Media aritmetica entre 120 y 35

cs = CubicSpline(QRS_x, QRS_means)
plt.figure(1)
plt.plot(np.arange(0,len(ecg_one_lead),1), cs(np.arange(0,len(ecg_one_lead),1)), label="Movimiento de línea de base interpolado")
plt.legend()
plt.xlabel("# Muestra")
plt.ylabel("Ruido medio en segmento PQ")
plt.show()

plt.figure(2)
ECG_filtered = ecg_one_lead - cs(np.arange(0,len(ecg_one_lead),1))
plt.plot(ECG_filtered, label="ECG Filtrado con detección de segmento PQ")
plt.plot(ecg_one_lead, label="ECG Original")
plt.legend()
plt.xlabel("# Muestra")
plt.ylabel("Amplitud")
plt.show()

plt.figure(3)
ECG_filtered = ecg_one_lead - cs(np.arange(0,len(ecg_one_lead),1))
plt.plot(ECG_filtered[10000:20000], label="ECG Filtrado con detección de segmento PQ")
plt.plot(ecg_one_lead[10000:20000], label="ECG Original")
plt.legend()
plt.title("Zoom en muestras 10000:20000")
plt.xlabel("# Muestra")
plt.ylabel("Amplitud")
plt.show()

plt.figure(4)
ECG_filtered = ecg_one_lead - cs(np.arange(0,len(ecg_one_lead),1))
plt.plot(ECG_filtered[650000:660000], label="ECG Filtrado con detección de segmento PQ")
plt.plot(ecg_one_lead[650000:660000], label="ECG Original")
plt.legend()
plt.title("Zoom en muestras 650000:660000")
plt.xlabel("# Muestra")
plt.ylabel("Amplitud")
plt.show()