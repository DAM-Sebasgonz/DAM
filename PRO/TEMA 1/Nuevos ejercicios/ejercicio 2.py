contrasenya =input("introduzca contraseña -->")

valida = True

if len(contrasenya) < 8:
    print("La contraseña no tiene la longitud adecuada: ")
    valida = False
if contrasenya.upper() == contrasenya:
    print("La contraseña no tiene caracteres en minusculas")
    valida = False
