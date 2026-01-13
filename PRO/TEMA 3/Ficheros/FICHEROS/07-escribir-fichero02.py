# copiar un fichero en otro caracter a caracter

try:
    fichero_lectura = open('dir_trab/fichero01.txt', 'r')
except:
    print("Ha ocurrido un error con el fichero de lectura\n")
else:
    try:
        fichero_escritura = open('dir_trab/fichero01.bckp', 'w')
    except:
        print("Ha ocurrido un error con el fichero de escritura\n")
    else:
        # aquí se pueden realizar las operaciones con el fichero
        
        car_leido = fichero_lectura.read(1)
        while car_leido != "":
            fichero_escritura.write(car_leido)
            car_leido = fichero_lectura.read(1)

        fichero_escritura.close()
        fichero_lectura.close()

        