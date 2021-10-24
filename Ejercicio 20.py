""" Programa: Ejercicio 16
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Averiguar cuantos Euros y centimos tienes en total"""

"""Se preguntan por la cantidad de monedas que se tienen"""
Deu = int(input("¿Cuántas monedas de 2€ tienes?"))
Ueu = int(input("Cuántas monedas de 1€ tienes?"))
Fcent = int(input("Cuántas monedas de 50 cent tienes?"))
Vcent = int(input("Cuántas monedas de 20 cent tienes? "))
Tcent = int(input("Cuántas monedas de 10 cent tienes?"))

"""Se realiza el cálculo para averiguar cuántos euros tienes"""
Eur = 2*Deu + 1*Ueu + int((0.5*Fcent + 0.2*Vcent + 0.1*Tcent))

"""Se realiza el cambio de centimos a euros para poder sumarlo a lo euros totales"""
Cent = int(((0.5*Fcent + 0.2*Vcent + 0.1*Tcent) - int((0.5*Fcent + 0.2*Vcent + 0.1*Tcent)))*100)

"""Se muestra el resultado de euros y céntimos finales"""
print(f"Tienes {Eur} Euros y {Cent} centimos en total")