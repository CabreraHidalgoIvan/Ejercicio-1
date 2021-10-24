""" Programa: Ejercicio 18
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Mostrar las iniciales del nombre y apellidos después de preguntar su nombre completo"""

"""Se pregunta el nombre completp"""
Name = input("Introduce tu nombre ")
Apellido1 = input("Introduce tu primer apellido ")
Apellido2 = input("Introduce tu segundo apellido ")

"""Resultado del nombre completo"""
Full_name = Name + Apellido1 + Apellido2

"""Se muestran las iniciales del nombre y apellidos"""
print(f"Hola {Full_name}, sus iniciales son {Name[0]} {Apellido1[0]} {Apellido2[0]}")