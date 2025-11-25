# Crear una lista vacía para almacenar los números
lista = []

# Recibir números del usuario hasta que se ingrese '@'
while True:
    numero = input("Escriba un nº entero o @ para salir: ")
    if numero == '@':
        break
    try:
        lista.append(int(numero))  # Añadir el número a la lista
    except ValueError:
        print("Error. Solo números enteros.")

# Verificar si hay algún número no consecutivo
iguales = True  # Suponemos que todos son consecutivos

for i in range(len(lista) - 1):
    if abs(lista[i + 1] - lista[i]) > 1:  # Si la diferencia entre dos números consecutivos es mayor que 1
        print(lista[i + 1])  # Imprimir el primer número no consecutivo
        iguales = False  
        break

if iguales:
    print("None")
