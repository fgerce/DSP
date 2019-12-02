#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:49:22 2019

@author: fede
"""

# Simular para los siguientes tamaños de señal
N = 1000
slp = 50 # por ciento de ventanas adyacentes
K = np.array([2, 5, 10, 20, 50], dtype=np.float)

##########################################
# Acá podés generar los gráficos pedidos #
##########################################
u = 0
sigma_2 = 2
s = np.random.normal(u, np.sqrt(sigma_2), N)
sesgos = np.zeros(len(K))
varianzas = np.zeros(len(K))
index = 0

for k in K:
       L = int(N/k)
       f, S = sig.welch(s, nperseg=L) #hanning windowed, overlap default = 50%
       esperanza = np.mean(S)
       sesgos[index] = esperanza
       varianzas[index] = np.var(S)
       index+=1