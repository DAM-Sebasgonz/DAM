# programa que lea el fichero de datos
# muestra por pantalla todos los números que hay en fichero
# escribe el total de números hallados.

# version leyendo con readline

if __name__ == '__main__':
    try:
        fichero = open('ejemplos/datos_ejemplo01.txt', 'r')
    except:
        print("Ha ocurrido un error con el fichero\n")
    else:
        lista_numeros = []
        numero = ""
        while True:
            linea_leida = fichero.readline()


            if linea_leida != "":
                print(linea_leida[:-1])
            else:
                break
        print()
        fichero.close()
    #print(lista_numeros)
    #print(f'En el fichero se han encontrado {len(lista_numeros)} numeros')