pais = {}
ciudades = {}

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
                        for nombre_pais, lista_ciudades in pais.items():
                            print(f"{nombre_pais}")
                            if not lista_ciudades:
                                print("(Sin ciudades registradas)")
                            else:
                                for ciudad in lista_ciudades:
                                    poblacion = ciudades.get(ciudad, 0)
                                    print(f"{ciudad} : {poblacion:} habitantes")
                    case "4.2":
                        lista_ciudades = list(ciudades.items())
                        for i in range(len(lista_ciudades)):
                            for j in range(len(lista_ciudades) - 1 - i):
                                if lista_ciudades[j][1] < lista_ciudades[j + 1][1]:
                                    lista_ciudades[j], lista_ciudades[j + 1] = lista_ciudades[j + 1], lista_ciudades[j] #bubble sort 
                        print("\nCiudades ordenadas por población:")
                        for ciudad, poblacion in lista_ciudades:
                            nombre_pais = ""
                        for pais_nombre, lista_ciudad_pais in pais.items():
                            if ciudad in lista_ciudad_pais:
                                nombre_pais = pais_nombre
                            break
                        print(f"{ciudad}: {poblacion:} habitantes - País: {nombre_pais}")
                    case "4.3":
                        if not ciudades:
                            print("\nNo hay ciudades registradas en el sistema")
                        else:
                            poblacion_total = sum(ciudades.values())
                            if poblacion_total == 0:
                                print("\nNo hay habitantes registrados")
                            else:
                                poblacion_por_pais = {}
                                for nombre_pais, ciudades_pais in pais.items():
                                    for pais, poblacion in sorted(poblacion_por_pais.items()):
                                        porcentaje = (poblacion / poblacion_total * 100)
                                        print(f"{pais:<30} {poblacion:>15,} {porcentaje:>14.2f}%")
                                        
                    case "4.4":
                        print("Volviendo al menú principal...")
                        break
                    case _:
                        print("Elija una opcion correcta")