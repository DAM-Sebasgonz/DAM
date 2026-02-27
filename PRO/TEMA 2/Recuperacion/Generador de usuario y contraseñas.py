import random

usuarios = {}

# Creamos una sola lista con todos las letras tanto en minuscula, como en mayusucula del alfabeto, ademas de los numeros y los caracteres especiales.

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '0','1','2','3','4','5','6','7','8','9',
            '[',']','{','}','&','%','$','@','*','+']

menu = """
N. Nuevo usuario\n
U. Usuarios validos\n
S. Salir
    """

while True:
    print(menu)
    opc_menu = input("opción --> ").strip().upper()
    match opc_menu:
        case "N":
            print("\nNuevo Usuario")

            nombre_entrada = input("Nombre: ").strip()

            while nombre_entrada == "":
                print("El nombre no puede estar vacio")
                nombre_entrada = input("Nombre: ").strip()
            apellido1_entrada = input ("Primer Apellido: ").strip()

            while apellido1_entrada == "":
                print("El Primer Apellido no puede estar vacio")
                apellido1_entrada = input("Apellido: ").strip()
            apellido2_entrada = input("Segundo Apellido: ")

            while apellido2_entrada == "":
                print("El Segundo apellido no puede estar vacio")
                apellido2_entrada = input("Segundo Apellido: ")
            
            nombre_minusculas = nombre_entrada
            apellido1_minusculas = apellido1_entrada
            apellido2_minusculas = apellido2_entrada

            posicion_mayusculas = 26

            while posicion_mayusculas <= 51:
                mayusculas = alfabeto[posicion_mayusculas]
                minusculas = alfabeto[posicion_mayusculas- 26]
                nombre_minusculas = nombre_minusculas.replace(mayusculas, minusculas)
                apellido1_minusculas = apellido1_minusculas.replace(mayusculas, minusculas)
                apellido2_minusculas = apellido2_minusculas.replace(mayusculas, minusculas)
                posicion_mayusculas += 1
            
            parte_nombre = nombre_minusculas[:2]
            parte_apellido1 = apellido1_minusculas[:3]
            parte_apellido2 = apellido2_minusculas[:3]

            combinacion_usuario = parte_nombre + parte_apellido1 + parte_apellido2
            combinacion_usuario_encontrada = False

            if combinacion_usuario not in usuarios:
                combinacion_usuario_encontrada =  True
            else:
                letras_pilladas_nombre = 2
                while letras_pilladas_nombre < len(nombre_minusculas) and not combinacion_usuario_encontrada:
                    combinacion_usuario = nombre_minusculas[:letras_pilladas_nombre + 1] + parte_apellido1 + parte_apellido2
                    letras_pilladas_nombre += 1
                    if combinacion_usuario not in usuarios:
                        combinacion_usuario_encontrada = True
                
                if not combinacion_usuario_encontrada:
                    nombre_usado = nombre_minusculas[:letras_pilladas_nombre]

                    letras_pilladas_apellido1 = 3
                    while letras_pilladas_nombre < len(apellido1_minusculas) and not combinacion_usuario_encontrada:
                        combinacion_usuario = nombre_usado + apellido1_minusculas[:letras_pilladas_apellido1 + 1]
                        letras_pilladas_apellido1 += 1
                        if combinacion_usuario not in usuarios:
                            combinacion_usuario_encontrada = True
                    
                    if not combinacion_usuario_encontrada:
                        apellido1_usado = apellido1_minusculas[:letras_pilladas_apellido1 + 1]

                        letras_pilladas_apellido2 = 3
                        while letras_pilladas_apellido2 < len(apellido2_minusculas) and not combinacion_usuario_encontrada:
                            combinacion_usuario = nombre_usado + apellido1_usado + apellido2_minusculas[:letras_pilladas_apellido2 + 1]
                            letras_pilladas_apellido2 += 1
                            if combinacion_usuario not in usuarios:
                                combinacion_usuario_encontrada = True
                    
            if not combinacion_usuario_encontrada:
                print("Ya existe el usuario en el sistema.")

            else:
                contraseña_valida = False
                contraseña = []
            
            while not contraseña_valida:
                contraseña = []
                for i in range(8):
                    contraseña.append(random.choice(alfabeto))

                tiene_min = False
                tiene_may = False
                tiene_dig = False
                tiene_signo = False

                for con in contraseña:
                    pos = alfabeto.index(con)
                    if pos <= 25:
                        tiene_min = True
                    elif pos <= 51:
                        tiene_may = True
                    elif pos <= 61:
                        tiene_dig = True
                    else:
                        tiene_signo = True

                pos_primero = alfabeto.index(contraseña[0])
                if pos_primero >= 52:
                    continue

                if tiene_min and tiene_may and tiene_dig and tiene_signo:
                    contraseña_valida = True

            contraseña_vacia = ""
            for c in contraseña:
                contraseña_vacia += c
            usuarios[combinacion_usuario] = [contraseña_vacia, nombre_entrada, apellido1_entrada, apellido2_entrada]
            print("Usuario creado.")
            print(f"Usuario: {combinacion_usuario}")
            print(f"Contraseña: {contraseña_vacia}")

        case "U":
            print("\n--- VALIDACIÓN DE USUARIO ---")

            usrname_input  = input("Introduce tu username: ").strip()
            password_input = input("Introduce tu contraseña: ").strip()

            if usrname_input in usuarios and usuarios[usrname_input][0] == password_input:
                print("Bienvenido al sistema, " + usuarios[usrname_input][1] )
            else:
                print("Usuario o contraseña incorrectos.")
        case "S":
            print("Hasta luego...")
            break
        case "_":
            print("Opcion no valida. Por favor elige N, U o S")