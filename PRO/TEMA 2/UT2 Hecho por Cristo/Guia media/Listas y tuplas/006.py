'''Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. 
Copia  los  elementos  de  la  lista  en  otra  lista,  pero  en  orden  inverso,  y  muestra  sus 
elementos por la pantalla.'''
lista = []
lista_auxiliar=[]
while True:
    elemento=input("Introduce un elemento para la lista o escribe @ para finalizar: ")
    if elemento=='@':
        break
    try:
        lista.append(elemento)
        print(f"Elemento añadido: {elemento}")
    except:
        print("Error. Introduce un elemento válido.")

for elto in range(len(lista)-1,-1,-1):
    lista_auxiliar.append(lista[elto])
print(lista)
print(lista_auxiliar)