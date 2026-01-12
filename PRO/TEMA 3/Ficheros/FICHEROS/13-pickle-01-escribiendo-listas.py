# escribiendo fichero binario ocn pickle
import pickle

# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
variable = 0
lista1 = [1,2,3,4,5]
lista2 = ['a','b']
lista = [lista1, lista2, variable]

# Escritura en modo binario, vacía el fichero si existe
fichero = open ('files/lista.pckl', 'wb')

# Escribe la lista en el fichero
pickle.dump (lista, fichero)

# cerramos el fichero
fichero.close()