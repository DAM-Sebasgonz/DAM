import random

# Diccionario de usuarios: clave = usrname, valor = [password, nombre, apellido1, apellido2]
usuarios = {}

# Una única lista con todos los caracteres posibles:
# posiciones  0-25  → minúsculas
# posiciones 26-51  → mayúsculas
# posiciones 52-61  → dígitos
# posiciones 62-71  → signos
ALFABETO = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '0','1','2','3','4','5','6','7','8','9',
            '[',']','{','}','&','%','$','@','*','+']

opcion = ""

while opcion != "S":
    print("\n========== GESTIÓN DE USUARIOS ==========")
    print("N - Nuevo usuario")
    print("U - Usuarios validados")
    print("S - Salir")
    opcion = input("Selecciona una opción: ").strip().upper()

    # ─────────────────────────────────────────────
    # OPCIÓN N: NUEVO USUARIO
    # ─────────────────────────────────────────────
    if opcion == "N":
        print("\n--- NUEVO USUARIO ---")

        nombre = input("Nombre: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre: ").strip()

        apellido1 = input("Primer apellido: ").strip()
        while apellido1 == "":
            print("El primer apellido no puede estar vacío.")
            apellido1 = input("Primer apellido: ").strip()

        apellido2 = input("Segundo apellido: ").strip()
        while apellido2 == "":
            print("El segundo apellido no puede estar vacío.")
            apellido2 = input("Segundo apellido: ").strip()

        # ── Pasar a minúsculas con replace() por cada par mayúscula→minúscula ──
        nombre_min = nombre
        ap1_min    = apellido1
        ap2_min    = apellido2

        pos_may = 26
        while pos_may <= 51:
            mayus = ALFABETO[pos_may]
            minus = ALFABETO[pos_may - 26]
            nombre_min = nombre_min.replace(mayus, minus)
            ap1_min    = ap1_min.replace(mayus, minus)
            ap2_min    = ap2_min.replace(mayus, minus)
            pos_may += 1

        # ── Generar usrname base ──
        base_nombre = nombre_min[:2]
        base_ap1    = ap1_min[:3]
        base_ap2    = ap2_min[:3]

        usrname = base_nombre + base_ap1 + base_ap2
        usrname_encontrado = False

        if usrname not in usuarios:
            usrname_encontrado = True
        else:
            # Paso 1: añadir siguiente letra del nombre
            idx_nombre = 2
            while idx_nombre < len(nombre_min) and not usrname_encontrado:
                usrname = nombre_min[:idx_nombre + 1] + base_ap1 + base_ap2
                idx_nombre += 1
                if usrname not in usuarios:
                    usrname_encontrado = True

            if not usrname_encontrado:
                nombre_usado = nombre_min[:idx_nombre]

                # Paso 2: añadir siguiente letra del apellido1
                idx_ap1 = 3
                while idx_ap1 < len(ap1_min) and not usrname_encontrado:
                    usrname = nombre_usado + ap1_min[:idx_ap1 + 1] + base_ap2
                    idx_ap1 += 1
                    if usrname not in usuarios:
                        usrname_encontrado = True

                if not usrname_encontrado:
                    ap1_usado = ap1_min[:idx_ap1]

                    # Paso 3: añadir siguiente letra del apellido2
                    idx_ap2 = 3
                    while idx_ap2 < len(ap2_min) and not usrname_encontrado:
                        usrname = nombre_usado + ap1_usado + ap2_min[:idx_ap2 + 1]
                        idx_ap2 += 1
                        if usrname not in usuarios:
                            usrname_encontrado = True

        if not usrname_encontrado:
            print("ERROR: El usuario ya existe en el sistema. No se puede añadir.")
        else:
            # ── Generar contraseña desde ALFABETO ──
            # minúsculas: pos  0-25 | mayúsculas: pos 26-51 | dígitos: pos 52-61 | signos: pos 62-71
            password_valida = False
            password = []

            while not password_valida:
                password = []
                for i in range(8):
                    password.append(random.choice(ALFABETO))

                tiene_min   = False
                tiene_may   = False
                tiene_dig   = False
                tiene_signo = False

                for c in password:
                    pos = ALFABETO.index(c)
                    if pos <= 25:
                        tiene_min = True
                    elif pos <= 51:
                        tiene_may = True
                    elif pos <= 61:
                        tiene_dig = True
                    else:
                        tiene_signo = True

                # No puede comenzar por dígito (pos 52-61) ni signo (pos 62-71)
                pos_primero = ALFABETO.index(password[0])
                if pos_primero >= 52:
                    continue

                if tiene_min and tiene_may and tiene_dig and tiene_signo:
                    password_valida = True

            password_str = ""
            for c in password:
                password_str += c

            # ── Insertar en el diccionario ──
            usuarios[usrname] = [password_str, nombre, apellido1, apellido2]

            print("\nUsuario creado exitosamente.")
            print("  Username : " + usrname)
            print("  Password : " + password_str)

    # ─────────────────────────────────────────────
    # OPCIÓN U: USUARIOS VALIDADOS
    # ─────────────────────────────────────────────
    elif opcion == "U":
        print("\n--- VALIDACIÓN DE USUARIO ---")

        usrname_input  = input("Introduce tu username: ").strip()
        password_input = input("Introduce tu contraseña: ").strip()

        if usrname_input in usuarios and usuarios[usrname_input][0] == password_input:
            print("Bienvenido al sistema, " + usuarios[usrname_input][1] + "!")
        else:
            print("ERROR: Username o contraseña incorrectos.")

    # ─────────────────────────────────────────────
    # OPCIÓN S: SALIR
    # ─────────────────────────────────────────────
    elif opcion == "S":
        print("\nCerrando la aplicación. ¡Hasta pronto!")

    else:
        print("Opción no válida. Por favor elige N, U o S.")
