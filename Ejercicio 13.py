""" Programa: Ejercicio 13
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Calcular la raíz cuadrada y cúbica de un número"""

"""Se pide el número"""
num = int(input("Escriba un número: "))

"""Se realizan las dos operaciones"""
raizcuadrada = num**(1/2)
raizcubica = num**(1/3)

"""Se muestran las dos raíces"""
print(f"La raiz cuadrada es: {raizcuadrada} y la raiz cubica es: {raizcubica}")