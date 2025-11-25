pais = {"pollalandia":["pollita"]}
ciudades = {"pollita": [2]}

menu = """Seleccione una opción:
1. Insertar pais
2. Insertar ciudad
3. Modificar población de una ciudad
4. Estadisticas
5. Salir"""

sub_menu= """4.1 Listado de paises y ciudades registradas
4.2 Listado de ciudades por numero de habitantes
4.3 Indicar porcentaje respecto al total de habitantes
4.4 Volver al menú principal"""
while True:
    print("="*40)
    print(menu)
    print("="*40)
    opc = input("Opción --> ")
    match opc:
        case "1":
            pais_entrada = input("Introduzca el pais --> ").title()
            if pais_entrada not in pais:
                if input (f"¿Seguro que desea crear {pais_entrada}? (S/N) --> ").upper() == "S":
                    pais[pais_entrada] = []
                    print("="*40)
                    print(f"{pais_entrada} añadido correctamente")
            else:
                print(f"{pais_entrada} ya se encuentra en el sistema")
        case "2":
            ciudad_entrada = input("Introduzca la ciudad --> ").title()
            if ciudad_entrada not in ciudades:
                poblacion_entrada = int(input("Introduzca la poblacion de la ciudad --> "))
                pais_entrada = input("Introduzca el país al que pertenece --> ").title() 
        
                pais.setdefault(pais_entrada, []).append(ciudad_entrada)
                ciudades[ciudad_entrada] = poblacion_entrada
        
                print(f"Ciudad {ciudad_entrada} añadida correctamente al país {pais_entrada}")
            else:
                print(f"{ciudad_entrada} ya se encuentra en el sistema")
        case "3":
            ciudad_entrada = input("Introduzca la ciudad a modificar la poblacion --> ").title()
            if ciudad_entrada in ciudades:
                nueva_poblacion = int(input("Introduzca la nueva poblacion -->  "))
                ciudades[ciudad_entrada] = nueva_poblacion
                print(f"Poblacion de {ciudad_entrada} actualizada correctamente")
            else:
                print(f"{ciudad_entrada} no se encuentra en el sistema")
        case "4":
            while True:
                print("="*40)
                print(sub_menu)
                print("="*40)
                opc_submenu = input("Opción --> ")
                match opc_submenu:
                    case "4.1":
                        for llave in pais.keys( ):
                            print(llave)
                    case "4.2":
                        pass
                    case "4.3":
                        pass
                    case "4.4":
                        break
                    case _:
                        print("Elija una opcion correcta")