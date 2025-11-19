# Escribir un programa en Python que pide al usuario un texto, una vez leído
# muestra un menú con las operaciones a realizar con él.
# Menú
# 1. Contar vocales
# 2. Contar la frecuencia de una palabra
# 3. Reemplazar todas las ocurrencias de una palabra
# 4. Reemplazar una ocurrencia determinada
# 5. Salir
# Cada opción del menú realiza lo siguiente:
# 1. Contar vocales
# Esta opción cuenta las vocales que hay en el texto. Se debe considerar las
# vocales acentuadas, las que estén en mayúsculas y las que puedan tener diéresis.
# La salida deberá ser la siguiente:
# Total de vocales: xx
# Nro de a’es: xx
# Nro de e’es: xx
# Nro de i’es: xx
# Nro de o’es: xx
# Nro de u’es: xx
# 2. Contar la frecuencia de una palabra
# Cuenta las veces que aparece una palabra en el texto. Tener en cuenta que se
# busca las palabras completas no se deben contar las que formen parte de otra
# más grande.
# La salida deberá ser:
# La palabra xxxxxxx está xx en el texto.
# 3. Reemplazar todas las ocurrencias de una palabra/letra
# Esta opción pide al usuario dos cosas:
# • La palabra/letra a reemplazar
# • La palabra/letra con la que se remplaza
# La salida debe ser la siguiente:
# Se han realizado xx reemplazos
# Se muestra el texto original con el contenido cambiado.
# 4. Reemplazar una ocurrencia determinada
# Esta opción pide al usuario la palabra a reemplazar.
# Luego muestra la posición de todas las ocurrencias de la palabra en el texto.
# Le pide al usuario cual es la posición de la palabra que quiere cambiar
# Le pide al usuario la palabra con la que se quiere reemplazar.
# La salida debe ser mostrar el texto original con el cambio realizado.

while True:
    menu = "1. Contar vocales \n2. Contar frecuencia \n3. Reemplazar ocurrencias \n4. Reemplazar ocurrencia determinada"
    print(menu)

    opc = input("opcion? --> ")
    match opc:
        case "1":
            vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
            con_vol = input("Ingrese una palabra que desee contar vocales: ").upper()
            for letra in vocales:
                contador = con_vol.count(letra)
                print(f"Numeros de {letra}: {contador}")
        case "2":
            frase = input("Ingrese una frase: ").upper()
            palabra = input("Ingrese la palabra que desea buscar:").upper()
            contador = frase.count(palabra)
            print(f"La palabra {palabra} aparece {contador} veces")
        case "3":
            frase = input("Ingrese una frase: ").upper()
            palabra1 = input("Ingrese la palabra que desea reemplazar:").upper()
            palabra2 = input("Ingrese la palabra por la que desea reemplazarla:").upper()
            contador = frase.count(palabra1)
            nueva_frase = frase.replace(palabra1, palabra2)
            print(f"Se han realizado {contador} reemplazos")
            print(nueva_frase)
        case "_":
            print("No funciona ese coso")
    break