"""Programa: Ejercicio 9
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Total a pagar con el descuento incluido"""

"""Se pide el costo total de la compra"""
print("Introduzca el importe original de la compra")
compra = float(input())

"""Se realiza el descuento"""
total = compra*(0.85)

"""Se muestra el valor final de la compra"""
print(f"El importe a pagar con el descuento aplicado es: {total} €")