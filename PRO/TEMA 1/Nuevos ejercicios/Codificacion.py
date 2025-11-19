
# Desarrolla un programa que reciba un string de exactamente 4 caracteres (código) y lo decodifique según reglas
# específicas: si el primer carácter es vocal, el mensaje es "urgente"; si el segundo es número par, agregar
# "confidencial"; si el tercero es consonante, agregar "dirección norte"; si el cuarto es símbolo especial, agregar
# "nivel alto". Debe construir el mensaje final concatenando las partes. 


vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnñpqrstuvwyz"
especiales = "@#$%&*+{}[]-()"

codigo = input("introduzca el codigo -->") .lower()
if len(codigo) == 4:
    if codigo [0] in vocales:
        mensaje = "El mensajes es urgente"
    else:
        mensaje = "El mensaje no es un urgente"
    
    if codigo[1].isdigit() and int(codigo[1]) % 2 == 0:
        mensaje == "confidencial"
    else:
        mensaje += "normal"
    
    if codigo[2] in consonantes:
        mensaje += "Va en direccion norte"
    
    if codigo[3] in especiales:
        mensaje += "con nivel alto"
    else:
        mensaje += "con nivel bajo"
else:
    print("mensaje no valido")
    