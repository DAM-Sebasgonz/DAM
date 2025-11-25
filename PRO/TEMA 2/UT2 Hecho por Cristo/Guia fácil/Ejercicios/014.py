'''Dada una lista de valores numéricos enteros, obtenga el resultado de multiplicar todos los valores 
en orden.'''
lista=[]
while True:
    numero=input("Introduce un nº entero o @ para salir: ")
    if numero=='@':
        break
    try:
        numero=int(numero)
        lista.append(numero)
    except:
        print("Error. Introduce un nº válido entero.")
resultado=1
for digito in lista:
    resultado*=digito
print(resultado)