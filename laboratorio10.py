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


a=1
while a<0 or a>0:
    a = int(input('Ingrese base:  '))
    b = abs(int(input('Ingrese exponente:  ')))
    a_power_b(a,b)