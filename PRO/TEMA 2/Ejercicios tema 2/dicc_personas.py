personas = {}
trabajadores = {}

menu = """1. Insertar personas\n2. Insertar trabajadores\n3. Nombre de los trabajadores desempleados\n4. Nº de personas que trabajan en una provincia\n8. Mostrar personas\n9. Salir"""

while True:
    print(menu)
    opc_menu = input("opción --> ")
    match opc_menu:
        case "1":
            nif_entrada = input("Introduce un NIF (ej: 0000000A)")
            if nif_entrada not in personas:
                nombre = input("Introduce la edad   -->").lower()
                edad = int(input("nombre -->"))
                municipio = input("nombre -->").title()
                provincia = input("nombre -->").title()

                if input(f"Seguro que desea crear el usuario con NIF:{nif_entrada} (S/N) -->").upper() == "S":
                    personas[nif_entrada] = [nombre, edad, municipio, provincia] 
            else:
                print("El usuario ya se encuentra en el sistema ")
        case "2":
            nif_entrada = input("nif --> ").upper
            if nif_entrada not in trabajadores:
                if nif_entrada not in personas:
                    nss = input("Ingrese El numero de la seguridad social (NUSS) -->").upper()
                    situacion = input("Está Desempleado o Trabajando -- (D/T)").upper()
                    salario = float(input("Salario -->"))
                    if input("Seguro que sea añadir este trabajardor (S/N) -->").upper():
                        trabajadores[nif_entrada] = [nss, situacion, salario]
                else:
                    print("Error.. para añadir trabajador debe primero añadir persona")
            else: 
                print("Warning... el trabajador ya esta registrado")
        case "3":
            for nif_trabajador in trabajadores:
                if trabajadores[nif_trabajador][1] == "D":
                    print(personas[nif_trabajador][0])
        case "4":
            municipio = input("Introduzca el municipio a buscar").title()
            con_trab = 0
            for nif_trabajador in trabajadores:
                if trabajadores[nif_trabajador][1] == "T":
                    if personas[nif_trabajador][2] == municipio:
                        con_trab += 1
            print(con_trab)
        case "8":
            print(personas)
        case "9":
            break
        case _:
            print("Elija una opcion correcta")
