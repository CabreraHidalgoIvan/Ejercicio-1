 """Programa: Ejercicio 8
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Se calcula el sueldo base más las pagas extras por ventas"""

"""Se pide el sueldo base y las ventas realizadas"""
print("Clacularemos el sueldo total recibido, para ello introduzca su sueldo base")
sueldo = float(input())
print("ahora introduzca cuantas ventas ha realizado")
ventas = int(input())

"""Se calcúla el sueldo total"""
sueldototal = ((ventas*0.1)*sueldo) + sueldo

"""Se muestra el resultado"""
print(f"El total de su sueldo es:{sueldototal} €")