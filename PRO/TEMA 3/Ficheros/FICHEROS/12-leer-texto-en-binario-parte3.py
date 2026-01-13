# Mostramos el contenido del fichero string.bin por pantalla

# fichero = open("files/string.bin", "rb")

# interpretado como binario y leyendo el fichero entero

with open('files/string.bin', 'rb') as fichero:
    content = fichero.read()

# # interpretado salida como binario
# print("Imprimimos el contenido del fichero leído\n")
# print(content)

# interpretado salida como texto --> decodificar
print("Imprimimos el contenido del fichero leído\n")
print(content.decode())
