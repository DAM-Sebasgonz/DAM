# Escriba un programa en Python que dada una lista de números enteros, obtenga otra lista donde
# se eliminen los duplicados. Mantenga el orden de los números en la nueva lista generada.
# Ejemplos de como debe ser la salida del programa debe ser como la que se muestra a
# continuación: 

lista =[12,10,15,25,1,3,1,3,2,2,2]

lista_ord = []

for numero in lista:
    existe = False

    for elemento in lista_ord:
        if elemento == numero: 
            existe = True
            break

    if not existe:
        lista_ord.append(numero)

print("Lista original:", lista)
print("Lista sin duplicados:", lista_ord)