""" Programa: Ejercicio 16
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Averiguar el tiempo que tarda un coche en alcanzar al otro"""

"""Se piden las velocidades de ambos coches"""
v1 = float(input("introduce la velocidad 1en km/h: "))
v2 = float(input("Introduce la segunda velocidad en km/h: "))
assert(v2>v1)

"""Se pide la distancia que separa a los coches"""
d = float(input("introduce la distancia entre los dos coches en km "))

"""Se realizan las operaciones"""
minutos = 60*d/(v2 - v1)

"""Se muestra el resultado"""
print(f"El coche 2 alcanzará al coche 1 en {minutos} min")
