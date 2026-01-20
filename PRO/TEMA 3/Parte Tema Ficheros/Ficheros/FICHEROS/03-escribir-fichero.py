# f = open("files/temps.dat", "r")
# f2 = open("files/tempcopia.dat", "w")

# copiar un fichero en otro

# esta forma de escritura NO es correcta

# for line in f:              
#     f2.write(line)
# f.close()
# f2.close()

# esta forma de escritura no es correcta

# for line in f:    # recuerden que line termina con \n      
#     f2.write(line)
# f.close()
# f2.close()

# nombre_fichero = input("Nombre Fichero: ")
# f = open(nombre_fichero, "w")

# while True:
#     datos = input("Datos: ")
#     if datos == "":
#         break
#     f.write(datos+"\n")
# f.close()

f = open("files/prueba.txt", "w")
listadatos = []
while True:
    datos = input("Datos: ")
    if datos == "":
        break
    listadatos.append(datos+"\n")
f.writelines(listadatos)   
f.close() 

f = open("files/prueba.txt", "r")
for line in f:              # quito el \n
    print(line.replace("\n", ""))