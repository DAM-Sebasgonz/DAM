'''Dados dos diccionarios de entrada, escriba un programa en Python que mezcle ambos diccionarios en uno único de salida 
sin usar métodos de mezcla como update.'''
diccionario1={}
diccionario2={}
diccionario3={}
while True:
    clave1=input("Dime una clave para diccionario 1: ")
    valor1=input("Dime un valor para la clave del diccionario 1: ")
    salir=input("Escribe @para salir: ")
    if salir=='@':
        break
    else:
        diccionario1[clave1]=valor1
    clave2=input("Dime una clave para diccionario 2: ")
    valor2=input("Dime un valor para la clave del diccionario 2: ")
    salir=input("Escribe @ para salir: ")
    if salir=='@':
        break
    else:
        diccionario2[clave2]=valor2
print(diccionario1, diccionario2)
diccionario3=diccionario1
for clave in diccionario2:
    diccionario3[clave]=diccionario2[clave]
print(diccionario3)

#c=a.copy()
# for clave in b:
#     c[clave] = b[clave]