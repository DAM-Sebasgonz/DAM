'''Escriba un programa en Python que dada una lista de números enteros positivos y un número no
negativo N, calcule el valor del elemento en la posición N elevado a N.
Ejemplo: [10, 20, 30, 40, 50] y N = 4 el resultado es 6250000 '''
# Solicitamos al usuario una lista de números enteros positivos
lista = []
while True:
    numero = input("Escriba un número entero positivo (o '@' para finalizar): ")
    if numero == '@':
        break
    try:
        numero = int(numero)
        if numero >= 0:
            lista.append(numero)
        else:
            print("Por favor, ingrese solo números enteros positivos.")
    except:
        print("Error: Por favor, ingrese un número entero positivo.")

# Pedimos el valor de N
while True:
    try:
        N = int(input("Escriba el valor de N (posición no negativa): "))
        if N >= 0:
            break
        else:
            print("N debe ser un número entero no negativo.")
    except:
        print("Error: Por favor, ingrese un número entero no negativo.")

if N < len(lista):
    resultado = lista[N] ** N
    print(f"El resultado de elevar el elemento en la posición {N} a la potencia {N} es: {resultado}")
else:
    print("Error: La posición N está fuera del rango de la lista.")