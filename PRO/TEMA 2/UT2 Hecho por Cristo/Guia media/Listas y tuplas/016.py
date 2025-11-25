'''Hacer  un  programa  que  inicialice  una  lista  de  números  con  valores 
aleatorios (10 valores), y posterior ordene los elementos de menor a mayor y los muestre 
por pantalla.'''
import random
lista=[]
for i in range(10):
    lista.append(random.randint(1,10))
print(f"La lista es: {lista}")
print(f"La longitud de la lista: {len(lista)}")

lista.sort()
print(f"La lista es: {lista}")
