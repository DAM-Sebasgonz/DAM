# Leemos del fichero list.bin creando una nueva lista y mostramos por pantalla

fichero = open("files/lista.bin", "rb")

# interpretado como no binario
nueva_lista = []
numero = list(fichero.read(1))

while numero:
    nueva_lista += numero
    numero = list(fichero.read(1))
    
    # # usando append()
    # nueva_lista.append(numero)
    # numero = list(fichero.read(1))

print(nueva_lista)