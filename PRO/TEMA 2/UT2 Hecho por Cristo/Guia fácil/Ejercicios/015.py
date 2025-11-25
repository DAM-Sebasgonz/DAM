'''Dado  un  número  entero  no  negativo,  genere  una  lista  con  los  dígitos  de  dicho  número  en  orden 
inverso. Debe trabajar el valor como número y no pasarlo a string. '''
lista=[]
lista_aux=[]
while True:
    numero=input("Introduce un nº entero o @ para salir: ")
    if numero=='@':
        break
    try:
        numero=int(numero)
        lista.append(numero)
    except:
        print("Error. Introduce un nº válido entero.")
for i in range(len(lista)-1,-1,-1):
    lista_aux.append(lista[i])
print(lista_aux)