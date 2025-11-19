letras = "TRWAGMYFPDXBNJZSQVHLCKE"
nif = input("introduzca el nif a validar:" ).upper()
if len(nif) == 9 and nif[:8].isdigit() and nif[8].isalpha():
    if letras [int(nif[:8]) % 23] == nif[8]:
        print("El NIF introducido es correcto")
    else:
        print("El NIF introducido no es correcto")
else:
    print("Error... El NIF introducido no tiene el formato correcto")