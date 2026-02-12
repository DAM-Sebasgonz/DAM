cadena = input("Ingrese texto: ")

contador = 0
bien = True
i = 0

while i < len(cadena):
    caracter = cadena[i]

    if caracter == "(":
        contador = contador + 1
    elif caracter == ")":
        contador = contador - 1

    if contador < 0:
        bien = False

    i = i + 1

if contador != 0:
    bien = False

if bien == True:
    print("La cadena esta BIEN encerrada entre parentesis.")
else:
    print("La cadena esta MAL encerrada entre parentesis.")