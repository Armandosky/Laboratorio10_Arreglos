# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:25:01 2020

@author: ARMANDO
"""


def a_power_b(a,b):
    potencia = 1
    while (b>0):
        potencia = potencia*a
        b = b - 1
    print("el resultado es: "+str(potencia))
    return potencia
