#  Ejercicio 001:
# Escriba un programa en Python que:
# • Pida al usuario un número de días, horas, minutos y segundos.
# • Calcule el número total de segundos del tiempo introducido por el usuario.
# • Muestre por pantalla el número total de segundos calculado, según el siguiente formato:
# El número total de segundos es: xxxxxxx

dias = int(input("Introduzca la cantidad de dias:"))
horas = int(input("Introduzca la cantidad de horas:"))
minutos = int(input("Introduzca la cantidad de minutos:"))
segundos = int(input("Introduzca la cantidad de segundos:"))

cantidad_total = (dias*86400) + (horas*8600) + (minutos*60) + segundos

print(f"La cantidad total de segundos es {cantidad_total}")
