#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 01:19:14 2019

@author: fede
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift

N  = 1000 # muestras
fs = 1000 # Hz

k = 200 #Repeticiones de montecarlo

f0 = fs/4
p0 = 0     # radianes
a0 = 2      # Volts

df = np.random.uniform(-2,2, k)
fn = f0 + df*fs/N

Ts = 1/fs
tt = np.linspace(0, (N-1)*Ts, N)

x = np.transpose(np.vstack([a0*np.sin(2*np.pi*ff*tt) for ff in fn]))

ventana = [sig.boxcar(N), sig.bartlett(N), sig.hann(N), sig.blackman(N), sig.flattop(N)]

V = len(ventana)
sesgo = np.zeros(V)
var = np.zeros(V)
prom = np.zeros(V)

dist = np.zeros((k,V))

for (vv, this_win) in zip(range(V), ventana):
       X = np.transpose(np.vstack([x[:,kk]*this_win for kk in range(0,k)]))
       X = fft(X, axis=0)
       modX = np.abs(fftshift(X))*2/N
       center = int(np.floor(N/2))
       modX = modX[center:N]
       freq = np.linspace(0, 0.5, len(modX))
       mod_slice = modX[248:253, :]**2
       mod_slice = np.mean(mod_slice, axis=0)
       dist[:,vv] = mod_slice
       prom[vv] = np.mean(mod_slice)
       sesgo[vv] = prom[vv] - a0
       var[vv] = np.mean((mod_slice-prom[vv])**2)
       
s1, edge1 = np.histogram(dist[:,0], 20)
s2, edge2 = np.histogram(dist[:,1], 20)
s3, edge3 = np.histogram(dist[:,2], 20)
s4, edge4 = np.histogram(dist[:,3], 20)
s5, edge5 = np.histogram(dist[:,4], 20)


plt.figure("Histograma normalizado del estimador")
plt.title("Histograma normalizado del estimador")
plt.plot(edge1[0:20], s1, label="rectangular")  
plt.plot(edge2[0:20], s2, label="barlett")  
plt.plot(edge3[0:20], s3, label="hanning")  
plt.plot(edge4[0:20], s4, label="blackman")  
plt.plot(edge5[0:20], s5, label="flattop")  
plt.xlabel("Amplitud estimada")
plt.ylabel("Cantidad de repeticiones (k=200)")

plt.legend()