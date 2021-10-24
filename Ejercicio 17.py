""" Programa: Ejercicio 17
 Autor: Iván Cabrera
 Fecha: 12/10/2021"""

"""Problema: Averiguar a que hora llega el ciclista a la segunda ciudad"""

"""Se piden las horas minutos y segundos por separado a los que sale el ciclista"""
horas = int(input("introduce la horas a la que sale el ciclista: "))
minutos = int(input("Añade los minutos correspondientes: "))
seg = int(input("Por último añade los segundos: "))

"""Preguntamos cuántos segundos tarda"""
Ttotal = float(input("Añade en segundos el tiempo total que ha tardado: "))

"""Se averigua el tiempo total en segundos"""
sectotal = horas*3600 + minutos*60 + seg + Ttotal

"""Se hacen las operaciones para averiguar la hora de llegada"""
HoraLlegada = int(sectotal/3600)
Minllegada = int(((sectotal/3600)/60)*100)

"""Se muestra la hora final a la que llega el ciclista a la segunda ciudad"""
print(f"ha llegado a las {HoraLlegada} horas y {Minllegada} minutos")