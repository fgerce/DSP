#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:40:34 2019

@author: fede
"""
import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import DataFrame
from IPython.display import HTML
import scipy.signal as sig
from scipy.fftpack import fft, fftshift

# Simular para los siguientes tamaños de señal
N = 1000
K = np.array([2, 5, 10, 20, 50], dtype=np.float)

u = 0
sigma_2 = 2
s = np.random.normal(u, np.sqrt(sigma_2), N)
sesgos = np.zeros(len(K))
varianzas = np.zeros(len(K))
index = 0

for k in K:
       L = int(N/k)
       S = np.transpose(np.vstack([fft(s[i*L:((i+1)*L)]) for i in range (0,int(k))]))
       modS = (np.abs(S)**2)/N
       periodgram = np.mean(modS, axis=1)
       esperanza = np.mean(periodgram)
       sesgos[index] = esperanza
       varianzas[index] = np.var(periodgram)
       index+=1