"""Programa: Ejercico 15
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Intercambiar el valor de dos variables a y b"""

"""Se piden los valores de las variables"""
print("Ingresa el valor de a y b y el programa te devolverá los valores invertidos")

"""Se realiza el algoritmo"""
a, b = input("ingresa el valor de a= "), input("ingresa el valor de b= ")

x = a
a = b
b = x

"""Se muestra el resultado"""
print(f"el valor de a= {a} y el valor de b={b}")