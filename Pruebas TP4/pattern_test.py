#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:29:14 2020

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

ecg_pattern = mat_struct['qrs_pattern1']
ecg_pattern = ecg_pattern.flatten()
cant_muestras = len(ecg_pattern)

freqS, welchS = sig.welch(ecg_pattern, fs,window='bartlett')
welchS = 20*np.log10(welchS)

plt.figure(1)
plt.plot(ecg_pattern)
plt.xlabel('# muestra')
plt.ylabel('Amplitud')
plt.grid()

plt.figure(2)
plt.plot(freqS, welchS)
plt.xlabel('Frecuencia  [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid()

plt.figure(3)
plt.plot(freqS, welchS)
plt.xlabel('Frecuencia  [Hz]')
plt.ylabel('Amplitud [dB]')
plt.xlim(0,50)
plt.ylim(60,125)
plt.grid()