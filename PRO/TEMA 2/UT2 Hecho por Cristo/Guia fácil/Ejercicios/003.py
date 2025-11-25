'''Escriba un programa en Python que dada una lista que puede tener como elementos números 
enteros y otras listas con números enteros (sólo 1 nivel de anidamiento), se pide que se genere 
una lista aplanada a partir de la original. 
Una lista es aplanada cuando le quitamos el anidamiento de listas que puedan tener. Es decir, se 
quitan los elementos de tipo lista, colocando los elementos que contiene en la lista original en la 
misma posición. 
Un ejemplo es el que se muestra 
[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100,110, 120]] al aplanarla debe quedar así 
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120] '''
lista_original = eval(input("Introduce una lista que puede contener números y listas anidadas (un nivel): "))

# Inicializar una lista vacía para almacenar el resultado aplanado
lista_aplanada = []

# Recorrer cada elemento en la lista original
for elemento in lista_original:
    # Verificar si el elemento es una lista revisando si es de tipo 'int'
    if type(elemento) == int:  
        lista_aplanada.append(elemento)  # Agregar el número directamente
    else:
        # Si no es un número entero, asumimos que es una lista y extendemos sus elementos
        lista_aplanada.extend(elemento)

# Imprimir la lista aplanada
print("Lista aplanada:", lista_aplanada)