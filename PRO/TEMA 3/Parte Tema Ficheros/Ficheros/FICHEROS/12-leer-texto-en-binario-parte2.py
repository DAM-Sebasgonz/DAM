# Mostramos el contenido del fichero string.bin por pantalla

fichero = open("files/string.bin", "rb")

# interpretado como no binario

data_byte = fichero.read(1)

while data_byte:
    print(data_byte.decode(), end = "")
    data_byte = fichero.read(1)
