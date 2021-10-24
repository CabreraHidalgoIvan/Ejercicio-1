""" Programa: Ejercicio 16
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Averiguar la nota final del alumno contando respuestas correctas, incorrectas y nulas"""

"""Se piden los resultados de las preguntas realizadas"""
Correct = int(input("introduce las respuestas correctas "))
Incorrect = int(input("introduce las respuestas incorrectas"))
NoAnsw = int(input("Introduce cuantas respuestas están sin responder"))

"""Se realiza el cálculo de putos correspondiente"""
Nota_correct = Correct*5
Nota_incorrect = Incorrect*(-1)
Nota_Null = NoAnsw*0

"""Se averiguan los puntos totales"""
Nota_final = (Nota_correct + Nota_incorrect + Nota_Null)

"""Se muestra el resultado obtenido"""
print(f"La nota final del alumno es de {Nota_final} puntos")