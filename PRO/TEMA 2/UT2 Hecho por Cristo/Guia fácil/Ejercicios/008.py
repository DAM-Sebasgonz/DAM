'''Escriba un programa en Python que dada una lista de enteros y de string que representan
números enteros, calcule la suma de todos los valores de la lista como si todos sus elementos
fueran números.

Ejemplo:'''
lista=[]
while True:
  num_string=input("Introduce los nº string que quieras - @ para parar: ")
  if num_string.isdigit():
    lista.append(num_string)
  elif num_string=='@':
    break
while True:
  num_string=input("Introduce nº enteros - @ para parar: ")
  if num_string.isdigit():
    lista.append(int(num_string))
  elif num_string=='@':
    break
  elif num_string[0]=='-':
    lista.append(int(num_string))
  else:
    print("Introduce un número entero.")
suma=0
for elto in lista:
  if type(elto)==str:
    elto=int(elto)
    suma+=elto
  else:
    suma+=elto
print(lista)
print("La suma es:",suma)

  
                       