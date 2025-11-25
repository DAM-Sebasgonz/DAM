'''Escriba un programa en Python que dada una lista, genere otra lista eliminando los elementos
que ocupan posiciones pares.
Ejemplo: [1, 2, 3, 4, 5, 6] se debe generar la lista [1, 3, 5] '''
lista=[]
lista_auxiliar=[]
while True:
    numero=input("Escriba un nº entero: ")
    if numero=='@':
        break
    try:
        numero=int(numero)
        lista.append(numero)
    except:
        print("Error.")
print(lista)

for i in range(len(lista)):
    if i%2==0:
        lista_auxiliar.append(lista[i])
print(lista_auxiliar)