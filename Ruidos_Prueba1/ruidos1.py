#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:44:42 2019

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

M = 1000 #Repeticiones de montecarlo

u = 0
sigma = 2

s = np.transpose(np.vstack([np.random.normal(u,np.sqrt(sigma),N) for jj in range (0,M)]))

lim = int(np.floor(N/2))
ww = np.linspace(0,(N-1)*fs/N, N)
complexMat = np.transpose(np.vstack([np.fft.fft(s[:,ii]) for ii in range(0,M)]))
moduloMat = np.abs(complexMat)*np.sqrt(2)/N
faseMat = np.angle(complexMat, True)
ww = ww[0:lim]
moduloMat = moduloMat[0:lim]
faseMat = faseMat[0:lim]

periodgram = np.zeros(lim)

#Periodogram = np.mean(moduloMat axis=0)
for ii in range (0,lim):
       periodgram[ii] = np.mean(moduloMat[ii, :]**2)

psum = np.sum(periodgram)

pvar = np.var(periodgram)

#suma = np.zeros(M)
#for ii in range (0,M):
#       suma[ii] = np.sum(moduloMat[:,ii]**2)
#
#promvar = np.mean(suma)
#
#var = np.zeros(M)
#for ii in range (0,M):
#       var[ii] = np.var(s[:,ii])
#



