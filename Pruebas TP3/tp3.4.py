#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:49:55 2019

@author: fede
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.fftpack import fft, fftshift
from spectrum import CORRELOGRAMPSD
from spectrum.tools import cshift

N  = 1000 # muestras
fs = 1000 # Hz

k = 200 #realizaciones

fr = np.random.uniform(-0.5, 0.5, k)

f0 = fs/4 + fr*2*np.pi
p0 = 0     # radianes
a0db = 10
a0 = 10**(a0db/20)     # Volts

Ts = 1/fs
tt = np.linspace(0, (N-1)*Ts, N)

s = np.transpose(np.vstack([a0*np.sin(2*np.pi*ff*tt + p0) for ff in f0])) 

u = 0
sigma_2 = 2
dbDiff = 3 # Ruido 3dB por debajo del pico de la señal
dbSignal = 20*np.log10(a0)
an = 10**((dbSignal-dbDiff)/20)
n = an*np.transpose(np.vstack([np.random.normal(u, np.sqrt(sigma_2), N) for ff in f0]))

x = s + n

freqX, Xw = sig.welch(x, axis=0)

estimador = np.zeros(Xw.shape[0])
for r in range(0,Xw.shape[0]):
       estimador[r] = freqX[np.argmax(Xw[:,r])]
       
varWelch10 = np.var(estimador)
meanWelch10 = np.mean(estimador)
meanWelch10 = meanWelch10 * fs


estimadorCorr = np.zeros(k)
for r in range(0,k):
       correlogram = CORRELOGRAMPSD(x[:,r], x[:,r], lag=100)
       correlogram = cshift(correlogram, len(correlogram)/2)
       correlogram = correlogram[int(correlogram.size/2): int(correlogram.size)]
       f = np.linspace(0, 0.5, int(len(correlogram)))
       estimadorCorr[r] = f[np.argmax(correlogram)]

varCorr10 = np.var(estimadorCorr)
meanCorr10 = np.mean(estimadorCorr)
meanCorr10 = meanCorr10 * fs       

