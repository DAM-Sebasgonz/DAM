print("||Sistema de Cifrado Cesar||")
print("Que desea hacer?")
print("S - Para salir del programa ")       #Pedimos al usuario que introduzca una de la opciones
print("D - Descrifrar el mensaje")
print("C - Cifrar el mensaje")

letras_min = "abcdefghijklmnopqrstuvwxyz"
letras_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"       
desplazamiento = 0

resultado = ""
i = 0                    

while True:
    opcion = input("==> ").upper().strip() #le pedimos al usuario que eliga las opciones y que estas no diferencien entre minusculas y mayusculas
    
    if opcion == "S":
        print("...saliendo del programa")
        break
    elif opcion == "C":
        texto = input("Introduzca el texto a cifrar ==> ")
        desplazamiento = int(input("Introduzca el desplazamiento ==> "))
        resultado = ""
        i = 0
    
    while i < len[texto]:
        c = texto[i]
        encontrado = False
        j = 0
        
        # Buscar en minúsculas
        while j < len(letras_min):
            if c == letras_min[j]:
                nuevo = (j + desplazamiento) % len(letras_min)
                resultado += letras_min[nuevo]  # ← Corchetes, no paréntesis
                encontrado = True
                break
            j += 1
        
        # Buscar en mayúsculas
        k = 0
        while not encontrado and k < len(letras_may):
            if c == letras_may[k]:
                nuevo = (k + desplazamiento) % len(letras_may)
                resultado += letras_may[nuevo]  # ← Corchetes
                encontrado = True
                break
            k += 1
        
        # Si no es letra, mantener el carácter
        if not encontrado:
            resultado += c
        
        i += 1
    
    print(f"Ha pasado '{texto}' a '{resultado}'")

    






