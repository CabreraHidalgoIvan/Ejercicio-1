""" Programa: Ejercicio 10
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Calcular la nota final de la asignatura"""

"""Se piden las notas de los parciales"""
print("La nota final de algoritmos se compondrá de los resultados de:")
print("Notas de los parciales, el exámen y el trabajo final, introduce los siguientes datos: ")
    parcial1 = float(input("introduce la nota del 1 parcial = "))
    parcial2 = float(input("introduce la nota del 2 parcial = "))
    parcial3 = float(input("introduce la nota del 3 parcial = "))

"""Se hace la media de los parciales"""
media = (parcial1 + parcial2 + parcial3)/3
print(f"La media de los 3 parciales es: {media}")

"""Se piden las notas del examen final y del trabajo"""
Exfinal = float(input("Introduce la nota del examen final = "))
Trfinal = float(input("Introduce la nota del trabajo = "))

"""Se calcula la nota final"""
Algoritmos = (media*0.55) + (Exfinal*0.3) + (Trfinal*0.15)

"""Se muestra cual es el nota final"""
print(f"El resultado de la nota final de Algoritmos es: {Algoritmos}")