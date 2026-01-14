# copiar un fichero en otro en modo binario

try:
    fichero_lectura = open('C:/DAM/PRO/TEMA 3/Ficheros/FICHEROS/files/jack_russell.png', 'rb')
except:
    print("Ha ocurrido un error con el fichero de lectura\n")
else:
    try:
        fichero_escritura = open('C:/DAM/PRO/TEMA 3/Ficheros/FICHEROS/files/Perro.png', 'wb')
    except:
        print("Ha ocurrido un error con el fichero de escritura\n")
    else:
        byte_leido = fichero_lectura.read(1)
        while byte_leido != b"":
            fichero_escritura.write(byte_leido)
            byte_leido = fichero_lectura.read(1)

        fichero_escritura.close()
        fichero_lectura.close()
