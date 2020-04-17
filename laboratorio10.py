# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:25:01 2020

@author: ARMANDO
"""


def a_power_b(a, b):
    potencia = 1
    while (b>0):
        potencia = potencia*a
        b = b - 1
    return potencia

a=1
c1=0
c2=0
c3=0
while a!=0:
    a = int(input('Ingrese base: '))
    b = abs(int(input('Ingrese exponente: ')))
    c3 = c3 + 1
    if a_power_b(a, b)%2 != 0:
       c1 += 1
    elif a_power_b(a, b)%2 == 0:
        c2 += 1
    print("El resultado es: "+str(a_power_b(a, b)))
print("El número de impares es: "+str(c1))
print("El número de pares es: "+str(c2))
print("El número de potencias es: "+str(c3 - 1))

import numpy as np
np.array 