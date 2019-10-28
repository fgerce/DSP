#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:47:24 2019

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

ventanas = [1, sig.boxcar(N), sig.bartlett(N), sig.hann(N), sig.blackman(N), sig.flattop(N)]
ventanas_names = ["No window", "Rectangular", "Bartlett", "Hanning", "Blackman", "Flattop"]
V = len(ventanas_names)

f1 = fs/4
f2 = f1 + (10*fs/N)

a2dB = -250
a2 = 10**(a2dB/20)

x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)

x = x1 + x2

xw = np.transpose(np.vstack([x * this_win for this_win in ventanas]))

X = fft(xw, axis=0)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Modulo bitonal", figsize=(10,10))
plt.suptitle('Mediciones para ejercicio 2b (a2=-250dB y f2 = f1 + (10*fs/N))', fontsize=20)
for ii in range (V):
       plt.subplot(3,2,ii+1)
       plt.tight_layout(pad=2, w_pad=0.5, h_pad=5)
       plt.plot(freq, modX[:, ii], label=ventanas_names[ii])
       plt.title(ventanas_names[ii], fontsize=20)
       plt.xlim(0.2, 0.3)
       plt.xlabel("Frecuencia normalizada", fontsize=20)
       plt.ylabel("Amplitud en dB", fontsize=20)
       plt.legend()
       plt.grid()
plt.subplots_adjust(top=0.88)