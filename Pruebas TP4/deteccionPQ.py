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
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

plt.vlines(QRS_det[0:6]-35,-15000, 15000, colors='red', ls='dotted')

plt.vlines(QRS_det[0:6]-120,-15000, 15000, colors='black', ls='dotted')
plt.plot(ecg_one_lead[0:5000])