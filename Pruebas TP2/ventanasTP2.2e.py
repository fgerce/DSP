#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:24:33 2019

@author: fede
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift

N = 1000
fs = 1000
Ts = 1/fs

tt = np.linspace(0, (N-1)*Ts, N)

ventana = sig.flattop(N)

daux = np.asarray([1, 1, 1])
d = np.asarray([0.8, 0.9, 1])
f1 = fs/4 + daux*0.5*fs/N
f2 = f1 + d*(fs/N)

a2 = 1

x1 = np.transpose(np.vstack([np.sin(2*np.pi*fi*tt) for fi in f1]))
x2 = np.transpose(np.vstack([a2*np.sin(2*np.pi*fi*tt) for fi in f2]))

x = x1 + x2
for aux in range(len(d)):
       x[:,aux] = x[:,aux] * ventana

X = fft(x, axis=0)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Modulo bitonal", figsize=(10,10))
plt.plot(freq, modX)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")