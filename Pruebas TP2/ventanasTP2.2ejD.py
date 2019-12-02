#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:40:16 2019

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

f1 = fs/4
f2 = f1 + (10*fs/N)


#########################
###ventana rectangular###
#########################
plt.figure("Rectangular")
rectWindow = sig.boxcar(N)
a2dB = -250
a2 = 10**(a2dB/20)
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
x = x * rectWindow

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.plot(freq, modX)
plt.title("Rectangular", fontsize=20)
plt.xlim(0.2, 0.3)
plt.xlabel("Frecuencia normalizada", fontsize=20)
plt.ylabel("Amplitud en dB", fontsize=20)
plt.grid()


#########################
###ventana bartlett###
#########################
plt.figure("Bartlett")
rectWindow = sig.bartlett(N)
a2dB = -40
a2 = 10**(a2dB/20)
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
x = x * rectWindow

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.plot(freq, modX)
plt.title("Bartlett", fontsize=20)
plt.xlim(0.2, 0.3)
plt.xlabel("Frecuencia normalizada", fontsize=20)
plt.ylabel("Amplitud en dB", fontsize=20)
plt.grid()


#########################
###ventana hann###
#########################
plt.figure("Hann")
rectWindow = sig.hann(N)
a2dB = -105
a2 = 10**(a2dB/20)
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
x = x * rectWindow

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.plot(freq, modX)
plt.title("hann", fontsize=20)
plt.xlim(0.2, 0.3)
plt.xlabel("Frecuencia normalizada", fontsize=20)
plt.ylabel("Amplitud en dB", fontsize=20)
plt.grid()


#########################
###ventana blackman###
#########################
plt.figure("blackman")
rectWindow = sig.blackman(N)
a2dB = -100
a2 = 10**(a2dB/20)
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
x = x * rectWindow

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.plot(freq, modX)
plt.title("blackman", fontsize=20)
plt.xlim(0.2, 0.3)
plt.xlabel("Frecuencia normalizada", fontsize=20)
plt.ylabel("Amplitud en dB", fontsize=20)
plt.grid()


#########################
###ventana flattop###
#########################
plt.figure("flattop")
rectWindow = sig.flattop(N)
a2dB = -85
a2 = 10**(a2dB/20)
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
x = x * rectWindow

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.plot(freq, modX)
plt.title("flattop", fontsize=20)
plt.xlim(0.2, 0.3)
plt.xlabel("Frecuencia normalizada", fontsize=20)
plt.ylabel("Amplitud en dB", fontsize=20)
plt.grid()