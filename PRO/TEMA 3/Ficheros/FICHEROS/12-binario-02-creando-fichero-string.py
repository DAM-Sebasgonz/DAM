# Creamos un fichero binario con contenido de caracteres

fichero = open("files/string.bin", "wb")

# Escribir dos líneas de texto en modo binario
fichero.write(b"Welcome to LinuxHint.\nLearn Python Programming.")
fichero.close()