'''Ejercicio 007:
Escriba un programa en Python que pida al usuario un número entero no negativo y obtenga una
lista con todas las potencias de 2 con el exponente variando desde 0 hasta dicho valor (inclusive).
Si n = 8
La lista de potencias es: [1, 2, 4, 16, 32, 64, 128, 256] 
'''

while True:
    n = int(input("Introduzca un número entero no negativo: "))
    if n<0:
        print("Debe introducir un número entero no negativo.")
    else:
        break
lista=[]*n

for i in range(n+1):
    lista.append(2**i)
print(lista)