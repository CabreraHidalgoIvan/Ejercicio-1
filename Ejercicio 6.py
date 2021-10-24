"""Programa: Ejercicio 6
# Autor: Iván Cabrera
# Fecha: 12/10/2021"""

"""Problema: Te hace la media de 3 números dados"""

"""Se pregunta por los 3 números que necesitamos"""
print("Realizaremos la media de 3 números")
print("Escribe un número")
n1 = float(input())
print("Escribe un segundo número")
n2 = float(input())
print("Escribe un tercer número")
n3 = float(input())

"""Se calcula la media"""
media = (n1 + n2 + n3)/3

"""Se muestra el resultado"""
print(f"La media de los 3 números es: {media}")