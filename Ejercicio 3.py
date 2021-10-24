""" Programa: Ejercicio 3
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Calcula la hipotenusa de un triángulo dados los dos catetos"""

"""Se importa el módulo math para poder hacer la raíz cuadrada"""
import math

"""Se piden los valores de ambos catetos"""
print("Intruduzca el valor del cateto1")
c1 = float(input())
print("Introduzca el valor del cateto2")
c2 = float(input())

"""Se calcula la hipotenusa y se imprime la respuesta"""
hipotenusa = math.sqrt(c1**2 + c2**2)
print(f"La hipotenusa del triángulo será de {hipotenusa}")