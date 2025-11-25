'''Crea  una  lista  de  números  de  un  tamaño  pasado  por  teclado,  la  lista 
contendrá números aleatorios entre 1 y 300 y mostrar aquellos números que acaben en un 
dígito  que  nosotros  le  indiquemos  por  teclado  (debes  controlar  que  se  introduce  un 
numero correcto), estos números deben guardarse en una nueva lista '''
import random
#Creamos la lista de numeros aleatorios: pedimos el tamaño de la lista.
lista=[]
lista_solucion=[]
while True:
    try:
        tamaño=int(input("Introduce un tamaño de la lista entero > 0: "))
    except:
        print("Error. Introduce un número válido entero.")
    else:
        if tamaño>0:
            break
        else:
            print("Error. Introduce un número válido entero mayor que 0.")
#Creamos la lista rellenandola con nº aleatorios dado el tamaño de la lista previamente solicitado. 
for i in range(tamaño):
    lista.append(random.randint(1, 300))
#Pedimos el nº para buscar donde acaban los nº. 
while True:
    try:
        n=int(input("Introduce un nº entre el 0-9: "))
    except:
        print("Error. Introduce un número válido entero. ")
    else:
        if n>=0 and n<=9:
            break
        else:
            print("Error. Introduce un número entre el 0-9.")
#Creamos una nueva lista con los nº que acaban en el dígito introducido por el usuario.
lista_formateada=map(str, lista)
lista_formateada=list(lista_formateada)
#Buscamos los nº que acaban en el dígito introducido.
for i in range(0,len(lista_formateada)-1):
    if lista_formateada[i][-1]==str(n):
        lista_solucion.append(int(lista_formateada[i]))
print(lista_solucion)

#formateamos la lista para pasar los nº a string y poder operar con las posiciones. 
