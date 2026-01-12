# Creamos un fichero binario a partir de una lista

fichero = open("files/lista.bin", "wb")
lista=[10,30,45,60,70,85,99]

# Convertimos la lista en un array binario
barray=bytearray(lista)

# escribinos el array binario en el fichero
fichero.write(barray)
fichero.close()
