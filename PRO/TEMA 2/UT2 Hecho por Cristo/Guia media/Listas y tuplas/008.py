'''Programa que cree una lista y la llene de números leídos por pantalla hasta 
que introduzcamos un número negativo. Entonces se debe imprimir la lista (como lista) 
(sólo los elementos introducidos).'''
lista=[]
while True:
    try:
        numero=int(input("Escribe un nº o un nº entero negativo para parar: "))
    except:
        print("Escribe un nº. ")
    else:
        if numero<0:
            break
        else:
            lista.append(numero)
for elto in lista:
    print(f"{elto}", end=' ')