"""Programa: Ejercicio 2
 Autor: Iván Cabrera
 Fecha: 12/10/2021

Problema: Dados 2 valores a elegir, calcula el perímetro y el área de un rectángulo"""

"""Pregunta y respuesta de las medidas en metros: """

print("Medida de la base en metros")
b = float(input())
print("Medidas de la altura en metros")
h = float(input())

"""Cálculo del perímetro y respuesta"""
print("Calcularemos el perímetro del rectángulo")
perimetro = (2*b) + (2*h)
print(f"El perímetro es {perimetro} m")

"""Cálculo del área y respuesta"""
print("Calcularemos el área del rectángulo")
area = (b*h)
print(f"El área es {area} m")