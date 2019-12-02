#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:14:26 2019

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

a2 = 10**(-15/20)

x1 = np.sin(2*np.pi*f1*tt)
x2 = a2*np.sin(2*np.pi*f2*tt)

x = x1 + x2 
original = x
b=16
const = (2**(b-1))
x = x*const
x = x + np.random.uniform(-5,5, N)
x = np.round(x)

X = fft(x)
modX = np.abs(fftshift(X))*2/N
center = int(np.floor(N/2))
modX = modX[center:N]
modX = 20*np.log10(modX + np.finfo(float).eps)
freq = np.linspace(0, 0.5, len(modX))

plt.figure("Modulo bitonal", figsize=(10,10))
plt.title("Límite de detección del segundo tono con ruido blanco")
plt.plot(freq, modX)
plt.grid()
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Amplitud en dB")

error = original - x/const
plt.figure("error")
plt.hist(error)