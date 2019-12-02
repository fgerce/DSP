#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:24:39 2019

@author: fede
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift

N = np.array([10, 50, 100, 250, 500, 1000, 5000, 20000], dtype=np.float)

u = 0
sigma_2 = 2

sesgos = np.zeros(len(N))
varianzas = np.zeros(len(N))
index = 0

for M in N:
       s = np.random.normal(u, np.sqrt(sigma_2), int(M))
       S = fft(s)
       modS = np.abs(S)
       periodgram = (modS**2)/M
       esperanza = np.mean(periodgram)
       sesgos[index] = esperanza
       varianzas[index] = np.var(periodgram)
       index+=1  