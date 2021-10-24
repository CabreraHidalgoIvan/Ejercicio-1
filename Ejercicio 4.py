"""Programa: Ejercicio 4
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Dados dos números, se calculará la suma, resta, multiplicación y división de ellos"""

"""Se piden los dos números"""
print("Escribe un número")
n1 = float(input())
print("Escribe otro número")
n2 = float(input())

"""Se efectúan las 4 operaciones"""
suma = n1 + n2
resta = n1 - n2
division = n1/n2
multiplicacion = n1*n2

"""Se imprimen todas las respuestas"""
print(f"La suma es = {suma}")
print(f"La resta es = {resta}")
print(f"La division es = {division}")
print(f"La multiplicacion es = {multiplicacion}")