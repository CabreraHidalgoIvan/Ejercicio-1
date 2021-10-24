"""Programa: Ejercicio 7
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Programa: Se realiza un cambio de minutos a horas"""

"""Se piden los minutos"""
print("Realizaremos una conversion de minutos a horas")
print("Escribe cuántos minutos desea convertir")
min = (input())

"""Se realiza el cálculo"""
horas = int(min//60)
minutos = min % 60

"""Se muestra el resultado"""
print(f"el resultado es: {horas} horas y {minutos}")