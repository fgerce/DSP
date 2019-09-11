# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:30:10 2019

@author: IVAN.GERCENSZTEIN
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def analizador_espectro(signal, fs):
    N = signal.shape[0]
    lim = int(np.floor(N/2))
    complexArray = np.fft.fft(signal)
    modulo = 20*np.log10(np.abs(complexArray)/lim)
    fase = np.angle(complexArray, True)
    ww = np.linspace(0,(N-1)*fs/N, N)
    return modulo[0:lim], fase[0:lim], ww[0:lim]


def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """ 
    
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    
    """    
    # comienzo de la función
    Ts = 1/fs
    tt = np.linspace(0, (N-1)*Ts, N)
    signal = a0*np.sin(2*np.pi*f0*tt+p0)
    
    # fin de la función
    
    return tt, signal

