#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:15:33 2019

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
d = np.array([0.01, 0.25, 0.5])

f1 = fs/4 + (d*fs/N)
f2 = [fs/4 + (10*fs/N), fs/4 + (10*fs/N), fs/4 + (10*fs/N)]

a2dB = -30
a2 = 10**(a2dB/20)

x1 = np.transpose(np.vstack([np.sin(2*np.pi*fi*tt) for fi in f1]))
x2 = np.transpose(np.vstack([a2*np.sin(2*np.pi*fi*tt) for fi in f2]))

x = x1 + x2

X = fft(x, axis=0)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Modulo bitonal", figsize=(10,10))
plt.plot(freq, modX)
plt.grid()
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.title("Desintonias en bitonal")
plt.xlim(0.22,0.28)
plt.legend(d, title="Desintonías")