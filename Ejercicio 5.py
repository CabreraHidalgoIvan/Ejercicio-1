"""Programa: Ejercicio 5
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Cambia la temperatura dada en Fahrenheit a grados Celsius"""

"""Se pide la temperatura en Fahrenheit"""
print("Introduzca la temperatura en grados Fahrenheit")
f = float(input())

"""Se calcula el cambio de grados Fahrenheit a grados Celsius"""
Celsius = (f-32)*(5/9)

print("Ahora se mostrará la temperatura en grados Celsius")

print(f"Los grados en Celsius sería {Celsius}")