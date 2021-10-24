""" Programa: Ejercicio 12
# Autor: Iván Cabrera
# Fecha: 12/10/2021"""

"""Problema: Calcular la distancia entre dos coordenadas"""
"""Se importa el módulo de math para poder hacer la raíz cuadrada"""
import math

"""Se piden las dos coordenadas (x,y)"""
print("Para averiguar la distancia entre dos coordenadas, sigue los siguientes pasos:")
x1, y1 = float(input("Introduce dos variables de x1:" )) , float(input("Introduce dos variables de y1:" ))
x2, y2 = float(input("Introduce dos variables de x2:" )) , float(input("Introduce dos variables de y2:" ))

"""Se muestrab las coordenadas dadas"""
print(f"({x1}, {y1}) y ({x2}, {y2})")

"""Se calcula la distancia entre ambas coordenadas"""
print("ahora calcularemos la distancia entre dichas coordenadas")
dist = abs(int(math.sqrt((x2-x1)**2 + (y2-y1)**2)))

"""Se muestra la distancia resultante"""
print(f"La distancia entre las coordenadas dadas es de: {dist}")
