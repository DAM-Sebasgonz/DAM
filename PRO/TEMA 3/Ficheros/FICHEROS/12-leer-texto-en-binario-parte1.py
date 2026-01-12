# Mostramos el contenido del fichero string.bin por pantalla

fichero = open("files/string.bin", "rb")

# interpretado como binario

# data_byte = fichero.read(7)
# while data_byte:
#     print(data_byte)
#     data_byte = fichero.read(7)

# interpretado como no binario

data_byte = fichero.read(3)
while data_byte:
    print(data_byte.decode())
    data_byte = fichero.read(3)
