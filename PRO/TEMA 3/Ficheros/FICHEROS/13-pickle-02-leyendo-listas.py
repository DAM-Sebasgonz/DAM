# leyendo fichero formato pickle y transformado en lista
import pickle

# Lectura en modo binario
fichero = open ('files/lista.pckl', 'rb')

# Cargamos los datos del fichero

lista1, lista2, variable = pickle.load(fichero)
print(lista1)
print(lista2)
print(variable)

# cerramos el fichero
fichero. close()
