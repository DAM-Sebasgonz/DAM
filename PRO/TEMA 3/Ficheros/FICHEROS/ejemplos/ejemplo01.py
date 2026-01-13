# programa que lea el fichero de datos
# muestra por pantalla todos los números que hay en fichero
# escribe el total de números hallados.

# versión leyendo caracter a caracter

if __name__ == '__main__':
    try:
        fichero = open('ejemplos/datos_ejemplo01.txt', 'r')
    except:
        print("Ha ocurrido un error con el fichero\n")
    else:
        lista_numeros = []
        numero = ""
        while True:
            caracter = fichero.read(1)
            if caracter != "":
                if caracter.isdigit():  # es dígito
                    numero += caracter
                else: # no es dígito
                    if numero:
                        lista_numeros.append(numero)
                        numero = ""
            else:
                break
        print()
        fichero.close()
    print(lista_numeros)
    print(f'En el fichero se han encontrado {len(lista_numeros)} numeros')