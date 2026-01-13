f = open("files/temps.dat", "r")
# f = open("files/temps_mal.dat", "r")
# lee el fichero completo
# print(f.read())

# lee el fichero completo y
# lo almacena en una variable

# fichero = f.read()

# lee una línea del fichero
# tener en cuenta que la línea termina con \n
# print(f.readline())

# lee todo el fichero 
# y lo almacena en una lista donde
# cada elemento es una línea del fichero

# print(f.readlines())

# bucle para recorrer todo el fichero
# y mostrarlo por pantalla
# recordar que line termina \n 
# aunque en algunos casos no 
# depende del ficehro de datos original

# for line in f:              # quito el \n
#     print(line.replace("\n", ""))

# guardamos las temperaturas en una lista de tuplas
# método 1 usando directamente el flujo de datos f

# temp = []
# for line in f:              # evitar
#     if line[-1] == "\n":
#         linea_trabajo = tuple(line[:-1].split())
#         temp.append(linea_trabajo)
#     else:
#         linea_trabajo = tuple(line.split())
#         temp.append(linea_trabajo)
# f.close()
# print(temp)

# gurdamos las temperaturas en una lista de tuplas
# método 2 usando readlines()

# temp = []
# for line in f.readlines():              # evitar
#     if line[-1] == "\n":
#         linea_trabajo = tuple(line[:-1].split())
#         temp.append(linea_trabajo)
#     else:
#         linea_trabajo = tuple(line.split())
#         temp.append(linea_trabajo)
# print(temp)

# gurdamos las temperaturas en una lista de tuplas
# método 3 usando bucle con readline()

# temp = []
# line = f.readline()
# while line != "":   # cuando NO haya más líneas que leer devuelve ""
#     if line[-1] == "\n":
#         linea_trabajo = tuple(line[:-1].split())
#         temp.append(linea_trabajo)
#     else:
#         linea_trabajo = tuple(line.split())
#         temp.append(linea_trabajo)
#     line = f.readline()
# print(temp)


# # otra forma de quitar los \n al final de la línea

# for _ in range(3):
#     print(f.readline().strip())

# # leer caracter a caracter
f = open("files/texto.txt", "r")

# caracter = f.read(1)
# while caracter != "":   # cuando se acaba fichero devuelve ""
#     print(caracter)
#     caracter = f.read(1)

caracter = f.read(2)
while caracter != "":   # cuando se acaba fichero devuelve ""
    print(caracter)
    caracter = f.read(2)
print()