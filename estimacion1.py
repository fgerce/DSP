#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:37:06 2019

@author: fede
"""
from Modulos import instrumentos as ins

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


N  = 1000 # muestras
fs = 1000 # Hz

a0 = 1 # Volts
p0 = 0 # radianes

f0 = fs/4

Nexp = 600 #Repeticiones de montecarlo

df = np.random.uniform(-10,10, Nexp)
fn = f0 + df

#graficar histograma de las variaciones en frecuencia
plt.figure(1)
plt.title("Histograma delta f")
plt.hist(fn,15)

Ts = 1/fs
tt = np.linspace(0, (N-1)*Ts, N)

sig = np.transpose(np.vstack([a0*np.sin(2*np.pi*j*tt+p0) for j in fn]))

lim = int(np.floor(N/2))
ww = np.linspace(0,(N-1)*fs/N, N)
complexMat = np.transpose(np.vstack([np.fft.fft(sig[:,i]) for i in range(0,Nexp)]))
moduloMat = np.abs(complexMat)/lim
faseMat = np.angle(complexMat, True)
ww = ww[0:lim]
moduloMat = moduloMat[0:lim]
faseMat = faseMat[0:lim]
#Graficar las fft
#plt.figure(2)
#plt.plot(ww[0:lim], moduloMat[0:lim])

o=[]    
#Estimador de frecuencia
for i in range(0,Nexp):
       o += [np.argmax(moduloMat[:,i])]
       
plt.figure(2)
plt.title("Distribucion error")
plt.hist(fn-o,15)


       

       