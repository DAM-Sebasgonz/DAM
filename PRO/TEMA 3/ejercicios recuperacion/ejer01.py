import pickle
import os

nombreArchivo = "usuarios.pckl"
usuarios = {}

def cargarUsuarios():
    if os.path.exists(nombreArchivo):
        with open(nombreArchivo, "rb") as f:
            return pickle.load(f)
    return {} 


def guardarUsuarios():
    with open(nombreArchivo, "wb") as f:
        pickle.dump(usuarios, f)


def validarEdad(edad):
    if 18 <= edad < 70:
        return True
    return False

def validarEstadoCivil(estado):
    estadosValidos = {"casado", "casada", "divorciado", "divorciada", "viudo", "viuda", "soltero", "soltera"}
    return estado.lower() in estadosValidos


def validarContrasena(contrasenia):
    if not (6 <= len(contrasenia) <= 10):
        return False
    if contrasenia[0].isdigit():
        return False

    tieneDigito = False
    tieneMayuscula = False
    tieneMinuscula = False
    tieneLetra = False

    for con in contrasenia:
        if con.isdigit():
            tieneDigito = True
        if con.isupper():
            tieneMayuscula = True
        if con.islower():
            tieneMinuscula = True
        if con.isalpha():
            tieneLetra = True

    return tieneDigito and tieneMayuscula and tieneMinuscula and tieneLetra

def buscarNIF(nif):
    return nif in usuarios


def buscarNombreUsuario(nombreUsuario):
    for datos in usuarios.values():
        if datos[0] == nombreUsuario:
            return True
    return False


def generarContrasena(nif):
    return nif[::-1]


def obtenerNIFPorNombreUsuario(nombreUsuario):
    for nif, datos in usuarios.items():
        if datos[0] == nombreUsuario:
            return nif
    return None


def anadirUsuario(datos):
    nif, nombreUsuario, nombreCompleto, edad, sexo, estadoCivil, contrasena = datos
    usuarios[nif] = [nombreUsuario, nombreCompleto, edad, sexo, estadoCivil, contrasena]
    guardarUsuarios()


def pedirDatosNuevoUsuario(nif):
    print("\n-- Crear nueva cuenta --")

    nombreUsuario = input("Nombre de usuario (8 caracteres): ").strip()
    if len(nombreUsuario) != 8:
        print("El nombre de usuario debe tener exactamente 8 caracteres.")
        return
    if buscarNombreUsuario(nombreUsuario):
        print("El nombre de usuario ya existe.")
        return

    nombreCompleto = input("Nombre completo: ").strip()
    if not nombreCompleto:
        print("El nombre completo no puede estar vacio.")
        return

    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("La edad debe ser un numero entero.")
        return
    if not validarEdad(edad):
        print("Edad invalida. Debe ser >= 18 y < 70.")
        return

    sexo = input("Sexo (Hombre / Mujer / Otro): ").strip().capitalize()
    if sexo not in ("Hombre", "Mujer", "Otro"):
        print("Sexo invalido.")
        return

    estadoCivil = input("Estado civil (casado/a, divorciado/a, viudo/a, soltero/a): ").strip().lower()
    if not validarEstadoCivil(estadoCivil):
        print("Estado civil invalido.")
        return

    contrasenia = generarContrasena(nif)
    print(f"Contraseña de primer uso generada: {contrasenia}")

    anadirUsuario([nif, nombreUsuario, nombreCompleto, edad, sexo, estadoCivil, contrasenia])
    print("Cuenta creada correctamente.")


def esPrimerUso(nif):
    contraseniaActual = usuarios[nif][5]
    return contraseniaActual == generarContrasena(nif)


def pedirNuevaContrasenia(nif):
    while True:
        nueva = input("Nueva contraseña: ").strip()
        if not validarContrasena(nueva):
            print("Contraseña invalida. Debe tener entre 6 y 10 caracteres, letras y numeros,")
            print("no puede empezar por numero, y debe tener mayusculas y minusculas.")
            continue
        confirmacion = input("Confirme la nueva contraseña: ").strip()
        if nueva != confirmacion:
            print("Las contraseñas no coinciden.")
            continue
        usuarios[nif][5] = nueva
        guardarUsuarios()
        print("Contraseña cambiada correctamente.")
        break


def flujoAutenticacion():
    print("\n1. Identificarse por NIF")
    print("2. Identificarse por nombre de usuario")
    opcionId = input("Opcion: ").strip()

    match opcionId:
        case "1":
            identificador = input("Introduce tu NIF: ").strip()
            nif = identificador if buscarNIF(identificador) else None
        case "2":
            identificador = input("Introduce tu nombre de usuario: ").strip()
            nif = obtenerNIFPorNombreUsuario(identificador)
        case _:
            print("Opcion invalida.")
            return

    if nif is None:
        print("Usuario no encontrado.")
        respuesta = input("Deseas crear una cuenta? (s/n): ").strip().lower()
        if respuesta == "s":
            if opcionId == "1":
                pedirDatosNuevoUsuario(identificador)
            else:
                nifNuevo = input("Introduce tu NIF para crear la cuenta: ").strip()
                if buscarNIF(nifNuevo):
                    print("Ese NIF ya esta registrado.")
                else:
                    pedirDatosNuevoUsuario(nifNuevo)
        return

    contrasena = input("Contraseña: ").strip()
    contrasenaGuardada = usuarios[nif][5]

    if contrasena != contrasenaGuardada:
        print("Contraseña incorrecta.")
        return

    nombreCompleto = usuarios[nif][1]  

    if esPrimerUso(nif):
        print("Contraseña de primer uso detectada. Debes establecer una nueva contraseña.")
        pedirNuevaContrasenia(nif)
        print(f"Bienvenido/a, {nombreCompleto}.")
    else:
        print(f"Bienvenido/a, {nombreCompleto}.")


def menuPrincipal():
    menu = """1. Entrar\n2. Salir"""

    while True:
        print(menu)
        opcion = input("Opcion: ").strip()

        match opcion:
            case "1":
                flujoAutenticacion()
            case "2":
                guardarUsuarios()
                print("Hasta luego.")
                break
            case _:
                print("Opcion invalida.")

usuarios = cargarUsuarios()
menuPrincipal()