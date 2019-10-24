#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:35:03 2019

@author: fede
"""

import sys

sys.path.append('/home/fede/PDS/DSP-Entregas/Modulos')

import instrumentos as ins

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

N  = 1000 # muestras
fs = 1000 # Hz

k = 200 #Repeticiones de montecarlo

f0 = fs/4
p0 = 0     # radianes
a0 = 2      # Volts

df = np.random.uniform(-2,2, k)
fn = f0 + df

Ts = 1/fs
tt = np.linspace(0, (N-1)*Ts, N)

ventana = [sig.boxcar(N), sig.bartlett(N), sig.hann(N), sig.blackman(N), sig.flattop(N)]
V = len(ventana)
sesgo = np.zeros(V)
var = sesgo
prom = sesgo

dist = np.zeros((k,V))

for (vv, this_win) in zip(range(V), ventana):
       sig = np.transpose(np.vstack([a0*np.sin(2*np.pi*jj*tt+p0)*this_win for jj in fn]))
       
       lim = int(np.floor(N/2))
       ww = np.linspace(0,(N-1)*fs/N, N)
       complexMat = np.transpose(np.vstack([np.fft.fft(sig[:,ii]) for ii in range(0,k)]))
       moduloMat = np.abs(complexMat)/lim
       faseMat = np.angle(complexMat, True)
       ww = ww[0:lim]
       moduloMat = moduloMat[0:lim]
       faseMat = faseMat[0:lim]
       
       moduloMat = moduloMat[int(fs/4), :]
       dist[:,vv] = moduloMat
       prom[vv] = np.mean(moduloMat)
       sesgo[vv] = prom[vv] - a0
       var[vv] = np.mean(np.exp2(moduloMat - prom[vv]))


s1, edge1 = np.histogram(dist[:,0], 20)
s2, edge2 = np.histogram(dist[:,1], 20)
s3, edge3 = np.histogram(dist[:,2], 20)
s4, edge4 = np.histogram(dist[:,3], 20)
s5, edge5 = np.histogram(dist[:,4], 20)


plt.figure("Distribucion lineal")
plt.plot(edge1[0:20], s1, label="rectangular")  
plt.plot(edge2[0:20], s2, label="barlett")  
plt.plot(edge3[0:20], s3, label="hanning")  
plt.plot(edge4[0:20], s4, label="blackman")  
plt.plot(edge5[0:20], s5, label="flattop")  

plt.legend()

plt.figure("Distribucion total")
plt.hist(dist[:,0], label="rectangular")
plt.hist(dist[:,1], label="barlett")
plt.hist(dist[:,2], label="hanning")
plt.hist(dist[:,3], label="blackman")
plt.hist(dist[:,4], label="flattop")

#Implementar Seaborn!
