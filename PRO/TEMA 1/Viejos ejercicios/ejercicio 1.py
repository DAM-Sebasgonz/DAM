# Ejercicio 001:
# Escriba un programa en Python que:
# • Pida al usuario un número de días, horas, minutos y segundos.
# • Calcule el número total de segundos del tiempo introducido por el usuario.
# • Muestre por pantalla el número total de segundos calculado, según el siguiente formato:
# El número total de segundos es: xxxxxxx

dias = int(input("introduzca el numero de dias:"))
horas = int(input("introduzca el numero de horas:"))
minutos = int(input("introduzca el numero de minutos:"))
segundos = int(input("introduzca el numero de segundos:"))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print("el numero total de segundos es:", total_segundos)