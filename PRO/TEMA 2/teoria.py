# lista1 = list()

# lista2 = []

# print(lista1,lista2)

# if lista1:
#     print('a ver si escribe') #No escribe, ya que lista vacia se considera falso

# lista3 = [3]

# if lista3: #La lista vacia no se considera true
#     print('a ver si escribe')




# lista3 = [1,2,3]
# print(len(lista3)) #Indica el numero de elementos
# print(lista3[0]) #Primera posicion es 0
# print(lista3[1])
# print(lista3[2]) #ultima len(lista) - 1



# lista3 = ['a','b','r']
# print(lista3)


# lista3 = ['a',1,'b','r',1.2]
# print(lista3)


# lista3 = ['a',1,'b','r',1.2, [92,12]]
# print(lista3)





# lista3 = list('12345')
# print(lista3)

# lista3 = list([2,3,4,5])
# print(lista3)



# lista1 = [1,2]
# lista2 = [1,2]

# if lista1 == lista2:
#     print('Las listas son iguales')
# else:
#     print('Las listas no son iguales')





# lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista[5])
# print(lista[len(lista) -1])


# lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista[-1])
# print(lista[-len(lista)])





# lista = [0,1,2,3,4,5,6,7,8,9]
# print(len[20])





# lista = [0,1,2,3,4,5,6,7,8,9]
# try:
#     print(lista[-1])
# except TypeError:
#     print('Errorrr...esa posicion no existe') #Con esto hace que no se roma el programa




# lista = [[0,1],[2,3],[4,5],[6,7],[8,9]]
# print(lista[2])
# print(lista[2][1])



# lista = [[0,1],[2,3],[4,5],[6,7],[8,9],['a','b']]
# print(lista[2])
# print(lista[2][1])
# print(lista [4][2][0]



# lista = [[0,1],[2,3],[4,5],[6,7],[8,9],['a','b']]
# lista[0] = 1
# print(lista)
# lista[1] = [4,5,6]
# print(lista)
# lista[4][2][1] = 'z'
# print(lista)





# a = [1,2] # Zona de memoria distinta
# b = [1,2]
# print(a,b)
# print(id(a))
# print(id(b))
# a[0] = 'a'
# b[1] = 'b'
# print(a,b)




# a = [1,2]
# b = a
# print(a,b)
# print(id(a))
# print(id(b))
# a[0] = 'a'
# b[1] = 'b'
# print(a,b)





# a = [1,2]
# b = a
# print(a,b)
# print(id(a))
# print(id(b))
# a[0] = 'a'
# b = ['c','d']
# print(a,b)







# lista = [0,1,2,3,4,5,6,7,8,9]
# for elto in lista: # La variable toma el valor del elemento
#     print(elto)


# lista = [0,1,'z',2,3,4,5,6,7,8,9]
# for pos in range(len(lista)): # La variable toma el valor del elemento
#     print(len[pos])


# lista = [0,1,'z',2,3,4,5,6,7,8,9]
# pos = 0
# while pos < len(lista):
#     print(f'lista[{pos}] = {lista[pos]}')





# lista = [0,1,2,3,4,5,6,7,8,9]
# for valor in enumerate(lista):
#     print(valor)


# lista = [0,1,2,3,4,5,6,7,8,9]
# for pos,valor in enumerate(lista):
#     print(f'lista[{pos}] = {valor}')

# una lista anidada es simplemente una lista que contiene otras listas como elementos.
# lista_anidada = [[0,1],[2,3],[4,5],[6,7],[8,9]]

# for fila in lista_anidada: # Fila es una de la sublista
#     for col in fila: # col son los elementos de la sublista
#         print(col, end='')



# lista_anidada = [[0,1],[2,3],[4,5],[6,7],[8,9]]

# for fila in range(len(lista_anidada)): # Fila es una de la sublista
#     for col in range(len(lista_anidada[fila])): # col son los elementos de la sublista
#         print(lista_anidada[fila][col], end='')
#     print()






# lista_anidada = [[0,1],[2,3],[4,5],[6,7],[8,9]]
# fila = 0
# while fila < len(lista_anidada):
#     col = 0
#     while col < len(lista_anidada[fila]):
#         print(lista_anidada[fila][col], end='')
#         col += 1
#     fila +=1
#     print()




# lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista[2:4])
# print(lista[:7])
# print(lista[6:])

# print(lista[1::2]) # Numeros impares en posicion par
# print(lista[::2]) # Numero pares en posicion impar
# print(lista[1::6]) # imprime el 1/7 avanzando de 6 en 6
# print(lista[1::15]) # Solo imprime el uno pq no hay mas numero si sumamos 15
# print(lista[8:6]) # no imprime nada 
# print(lista[-7:-5]) # Imprime el 3/4
# print(lista[-7:-5:-1])

# lista = [1,2,3]
# print(lista)
# lista.append([4,5])
# print(lista)
# lista.append([6,7])
# print(lista)

# # # Insert

# lista = [1,3]
# # lista.insert(1,2) # posicion, valor
# # print(lista)
# lista.insert(-1,4) # posicion, valor
# print(lista)


# lista = [1,2,3]
# lista.extend("abc") #debe usar iterador
# print(lista)

# # # remove

# lista = [1,2,3]
# lista.remove(2)
# print(lista)

# lista = [1,2,3,2]
# try:
#     valor = int(input("Inserte un numero"))
#     lista.remove(valor)
# except ValueError:
#     print(f"Error... El numero {valor} no esta en la lista")
# else:
#     print(f"El numero {valor} se ha borrado de la lista")
# finally:
#     print(lista)

# # # BORRAR TODAS LAS OCURRENCIAS

# nro_borrados = 0
# lista = [1,2,3,2]
# while True:
#     if lista.count(17):
#         lista.remove(17)
#         nro_borrados += 1
#     else:
#         print(f"Error...el numero se ha borrado {nro_borrados} veces")
#         break
# print(lista)


# nro_borrados = 0
# lista = [1,2,3,2]
# while lista.count(17):
#     lista.remove(17)
#     nro_borrados += 1
# print(f"Error...el numero se ha borrado {nro_borrados} veces")

# print(lista)

# lista=[1,2,3,2,7,8,2,2,3]
# pos_borrar = int(input("pos = "))
# if pos_borrar < len(lista):
#     elto_borrado = lista.pop(pos_borrar)
#     print(elto_borrado)
# else:
#     print(f"Error... La posicion {pos_borrar} NO EXISTE")


# lista=[1,2,3,2,7,8,2,2,3]
# try:
#     valor = int(input("inserte un numero ->"))
#     pos = lista.index(valor, 3)
# except ValueError:
#     print(f"Error... El numero {valor} no esta en la lista")
# except NameError:
#     print("Debe introducir un numero")
# except:
#     print(f"\nError...desconocido")
# else:
#     print(f"El numero {valor} se encuentra en la posicion {pos}")


# lista=[1,2,3,2,7,8,2,2,3]
# print(lista)
# lista.sort()
# print(lista)
# lista.sort(reverse = False)
# # print(lista)

# lista=[1,2,3,2,7,8,2,2,3]
# lista.reverse()
# print(lista)

# lista=[1,2,3,2,7,8,2,2,3]
# lista.clear()
# print(lista)
# del lista
# print(lista)

# a = [[1],2]
# b = a.copy() 
# print("--",a)
# print("--", b)
# a[0][0] = "a"
# b[1] = "x"
# print("**",a)
# print("**",b)

# import copy

# a = [[1],2]
# b = copy.deepcopy(a) 
# print("--",a)
# print("--", b)
# a[0] = "a"
# b[1] = "x"
# print("**",a)
# print("**",b)


# lista=[1,2,3,2,7,8,2,2,3]
# print(min(lista))
# print(max(lista))
# print(sum(lista))

# lista1 = [1,2,3]
# lista2 = ["a", "b", "c"]
# lista3 = ["*", "@", "#"]

# iterador = zip(lista1, lista2, lista3)
# print(list(iterador))



# lista1 = []
# lista2 = ["a", "b", "c"]
# lista3 = ["*", "@", ]

# iterador = zip(lista1, lista2, lista3)
# print(list(iterador))

# lista = ["a", "b", "c"]

# iterador_mayusculas = map(print, lista)

# for _ in iterador_mayusculas:
#     pass

# lista = [1,2,3,4]

# def potencia_2(numero : int):
#     return pow(numero, 2)

# iterador_cuadrados = map (potencia_2, lista)
# lista_potencia_2 = list(iterador_cuadrados)
# print(lista_potencia_2)

# lista = [1,2,3,4,5,6,7,8,9,10]

# def es_par(numero : int):
#     return not numero % 2

# iterador_pares = filter(es_par, lista)
# lista_pares = list(iterador_pares)
# print(lista_pares)

# lista = [3,1,2,7,[8,3],4]
# elto_int = 

# lista_aplanada = []
# for elto in lista:
#     if type(elto) != list:
#         lista_aplanada.append(elto_int)
# print(lista_aplanada)

# Recorrer una lista mediante compresion

# lista = [1,2,3,4]

# lista_cuadrados = [pow(elto,2) for elto in lista]
# print(lista)
# print(lista_cuadrados)

# lista = [1,2,3,4]
# lista_cuadrados = []

# for elto in lista:
#     lista_cuadrados.append(pow(elto,2))
# print(lista)
# print(lista_cuadrados)
 
# TUPLAS

# maneras de crear una tupla vacia

# tupla01 = tuple() 
# # o
# tupla02 = ()

# import random
# lista = []
# alfabeto = "abcdefghijklmnñopqrstuvwxyz"
# cont = 1
# while cont <= 10:
#     tupla = (random.choice(alfabeto), random.randint(1,100))
#     if tupla not in lista:
#         lista.append(tupla)

# print(lista)
# print ("--")
# print(lista.sort())











