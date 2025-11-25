'''Escriba un programa en Python que genere una lista con los n primeros múltiplos de x, donde n y
x son parámetros de entrada pedidos al usuario y que deben ser valores enteros mayores que 0
(se debe verificar).
Ejemplo:
Si x = 3 y n = 8 la lista debe ser: [0, 3, 6, 9, 12, 15, 18, 21]'''
listado=[]
x=int(input("Dime un valor para 'x': "))
n=int(input("Dime otro valor para 'n': "))
if x>0 and n>0:
    for i in range(0, n+1):
        multiplo=i*x
        listado+=[multiplo]
print(listado)
