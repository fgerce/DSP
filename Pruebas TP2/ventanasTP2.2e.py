#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:24:33 2019

@author: fede
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift

N = 1000
fs = 1000
Ts = 1/fs

tt = np.linspace(0, (N-1)*Ts, N)

ventanas = [1, sig.boxcar(N), sig.bartlett(N), sig.hann(N), sig.blackman(N), sig.flattop(N)]

##Rect
d = 2.8
f1 = fs/4 + 0.5*fs/N
f2 = f1 + d*(fs/N)
a2 = 1
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
xw = x * sig.boxcar(N)
X = fft(xw)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Rectangular")
plt.title("Rectangular")
plt.plot(freq, modX, label=d)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.legend()

##Rect
d = 2.3
f1 = fs/4 + 0.5*fs/N
f2 = f1 + d*(fs/N)
a2 = 1
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
xw = x * sig.bartlett(N)
X = fft(xw)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Bartlett")
plt.title("Bartlett")
plt.plot(freq, modX, label=d)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.legend()


##Hann
d = 2.5
f1 = fs/4 + 0.5*fs/N
f2 = f1 + d*(fs/N)
a2 = 1
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
xw = x * sig.hann(N)
X = fft(xw)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Hann")
plt.title("Hann")
plt.plot(freq, modX, label=d)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.legend()

##Blackman
d = 2.5
f1 = fs/4 + 0.5*fs/N
f2 = f1 + d*(fs/N)
a2 = 1
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
xw = x * sig.blackman(N)
X = fft(xw)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Blackman")
plt.title("Blackman")
plt.plot(freq, modX, label=d)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.legend()

##Flattop
d = 2.8
f1 = fs/4 + 0.5*fs/N
f2 = f1 + d*(fs/N)
a2 = 1
x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)
x = x1 + x2
xw = x * sig.flattop(N)
X = fft(xw)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX)
freq = np.linspace(0, 0.5, len(modX))
plt.figure("Flat Top")
plt.title("Flat Top")
plt.plot(freq, modX, label=d)
plt.grid()
plt.xlim(0.248,0.28)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")
plt.legend()
