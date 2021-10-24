""" Programa: Ejercicio 14
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Devolver el número invertido"""

"""Se piden los dos números por separado por si intentamos hacer trampa"""
num = int(input("Introduce el primer dígito", []) + input("Introduce el segundo dígito", []))
print(f"Su número es: {num})

"""Se realiza el cálculo del número invertido"""
invertido = int(str(num)[::-1])

"""Se muestra el resultado"""

print(f"su número invertido es {invertido}")
