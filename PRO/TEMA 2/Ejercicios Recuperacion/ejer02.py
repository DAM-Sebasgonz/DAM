viajeros = {
    "12345678A": ["Ana García", ["Madrid", "París", "Roma"]],
    "87654321B": ["Luis Pérez", ["París", "Londres"]],
    "11223344C": ["Carmen López", ["Tokio", "Madrid"]]
}

paises = {
    "España":      ["Madrid", "Barcelona", "Sevilla"],
    "Francia":     ["París", "Lyon", "Marsella"],
    "Italia":      ["Roma", "Milán", "Venecia"],
    "Reino Unido": ["Londres", "Manchester"],
    "Japón":       ["Tokio", "Kioto", "Osaka"]
}

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar viajero/a")
    print("2. Agregar país")
    print("3. Países visitados por un viajero/a")
    print("4. Número de viajeros que han visitado una ciudad")
    print("5. Dado un país, cuántos viajeros lo han visitado")
    print("9. Salir del programa")
    print("=====================================")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:

        case "1":
            print("\n--- Agregar viajero/a ---")

            nif = input("NIF del viajero/a: ").strip().upper()

            while nif != "":

                if nif in viajeros:
                    print(f"Ya existe un viajero con el NIF '{nif}'.")
                else:
                    nombre = input("Nombre completo: ").strip()
                    if nombre == "":
                        print("El nombre no puede estar vacío.")
                    else:
                        destinos = []
                        ciudad = input("Ciudad: ").strip()

                        while ciudad != "":
                            ciudad_exacta = ""
                            for pais in paises:
                                i = 0
                                while i < len(paises[pais]):
                                    if paises[pais][i].lower() == ciudad.lower():
                                        ciudad_exacta = paises[pais][i]
                                        break
                                    i += 1
                                if ciudad_exacta != "":
                                    break

                            if ciudad_exacta == "":
                                print(f"'{ciudad}' no pertenece a ningún país registrado en el sistema.")
                            else:
                                indice_destino = -1
                                i = 0
                                while i < len(destinos):
                                    if destinos[i].lower() == ciudad_exacta.lower():
                                        indice_destino = i
                                        break
                                    i += 1

                                if indice_destino != -1:
                                    print(f"'{ciudad_exacta}' ya está en la lista de destinos de este viajero.")
                                else:
                                    destinos.append(ciudad_exacta)
                                    print(f"Ciudad '{ciudad_exacta}' añadida.")

                            ciudad = input("Ciudad: ").strip()

                        viajeros[nif] = [nombre, destinos]
                        print(f"Viajero/a '{nombre}' ({nif}) registrado/a correctamente.")

                nif = input("\nNIF del siguiente viajero/a : ").strip().upper()

        case "2":
            print("\n--- Agregar país ---")
            nombre_pais = input("Nombre del país: ").strip()

            if nombre_pais == "":
                print("El nombre del país no puede estar vacío.")
            elif nombre_pais in paises:
                print(f"El país '{nombre_pais}' ya está registrado.")
            else:
                ciudades = []
                print("Introduce las ciudades del país :")
                ciudad = input("Ciudad: ").strip()

                while ciudad != "":
                    indice = -1
                    i = 0
                    while i < len(ciudades):
                        if ciudades[i].lower() == ciudad.lower():
                            indice = i
                            break
                        i += 1

                    if indice != -1:
                        print(f"{ciudad}' ya está en la lista de ciudades de este país.")
                    else:
                        ciudades.append(ciudad)
                        print(f"Ciudad '{ciudad}' añadida.")

                    ciudad = input("Ciudad: ").strip()

                if len(ciudades) == 0:
                    print("No se añadió ninguna ciudad. El país no fue registrado.")
                else:
                    paises[nombre_pais] = ciudades
                    print(f"País '{nombre_pais}' registrado con {len(ciudades)} ciudad(es).")

        case "3":
            print("\n--- Países visitados por un viajero/a ---")
            nif = input("Introduce el NIF del viajero/a: ").strip().upper()

            if nif not in viajeros:
                print(f" No existe ningún viajero/a con el NIF '{nif}'.")
            else:
                datos = viajeros[nif]
                nombre = datos[0]
                destinos = datos[1]

                print(f"\nViajero/a: {nombre} ({nif})")

                if len(destinos) == 0:
                    print("Este viajero/a no tiene destinos registrados.")
                else:
                    paises_visitados = []

                    i = 0
                    while i < len(destinos):
                        ciudad = destinos[i]

                        for pais in paises:
                            j = 0
                            while j < len(paises[pais]):
                                if paises[pais][j].lower() == ciudad.lower():
                                    indice_pais = -1
                                    k = 0
                                    while k < len(paises_visitados):
                                        if paises_visitados[k] == pais:
                                            indice_pais = k
                                            break
                                        k += 1
                                    if indice_pais == -1:
                                        paises_visitados.append(pais)
                                    break
                                j += 1

                        i += 1

                    n = len(paises_visitados)
                    i = 0
                    while i < n - 1:
                        j = 0
                        while j < n - i - 1:
                            if paises_visitados[j] > paises_visitados[j + 1]:
                                temp = paises_visitados[j]
                                paises_visitados[j] = paises_visitados[j + 1]
                                paises_visitados[j + 1] = temp
                            j += 1
                        i += 1

                    print(f"Países visitados ({len(paises_visitados)}):")
                    i = 0
                    while i < len(paises_visitados):
                        print(f"  - {paises_visitados[i]}")
                        i += 1

        case "4":
            print("\n--- Número de viajeros que han visitado una ciudad ---")
            ciudad_buscada = input("Nombre de la ciudad: ").strip()

            ciudad_exacta = ""
            for pais in paises:
                i = 0
                while i < len(paises[pais]):
                    if paises[pais][i].lower() == ciudad_buscada.lower():
                        ciudad_exacta = paises[pais][i]
                        break
                    i += 1
                if ciudad_exacta != "":
                    break

            if ciudad_exacta == "":
                print(f"La ciudad '{ciudad_buscada}' no está registrada en el sistema.")
            else:
                contador = 0
                nombres_viajeros = []

                for nif in viajeros:
                    destinos = viajeros[nif][1]
                    i = 0
                    while i < len(destinos):
                        if destinos[i].lower() == ciudad_exacta.lower():
                            contador += 1
                            nombres_viajeros.append(viajeros[nif][0])
                            break
                        i += 1

                print(f"\nCiudad: {ciudad_exacta}")
                print(f"Número de viajeros/as que la han visitado: {contador}")
                if contador > 0:
                    print("Viajeros/as:")
                    i = 0
                    while i < len(nombres_viajeros):
                        print(f"  - {nombres_viajeros[i]}")
                        i += 1

        case "5":
            print("\n--- Viajeros que han visitado un país ---")
            pais_buscado = input("Nombre del país: ").strip()

            if pais_buscado not in paises:
                print(f"El país '{pais_buscado}' no está registrado en el sistema.")
            else:
                ciudades_del_pais = paises[pais_buscado]
                viajeros_del_pais = []

                for nif in viajeros:
                    datos = viajeros[nif]
                    nombre = datos[0]
                    destinos = datos[1]

                    indice_ciudad = -1
                    i = 0
                    while i < len(destinos) and indice_ciudad == -1:
                        j = 0
                        while j < len(ciudades_del_pais):
                            if destinos[i].lower() == ciudades_del_pais[j].lower():
                                indice_ciudad = i
                                break
                            j += 1
                        i += 1

                    if indice_ciudad != -1:
                        indice_viajero = -1
                        k = 0
                        while k < len(viajeros_del_pais):
                            if viajeros_del_pais[k] == nombre:
                                indice_viajero = k
                                break
                            k += 1
                        if indice_viajero == -1:
                            viajeros_del_pais.append(nombre)

                n = len(viajeros_del_pais)
                i = 0
                while i < n - 1:
                    j = 0
                    while j < n - i - 1:
                        if viajeros_del_pais[j] > viajeros_del_pais[j + 1]:
                            temp = viajeros_del_pais[j]
                            viajeros_del_pais[j] = viajeros_del_pais[j + 1]
                            viajeros_del_pais[j + 1] = temp
                        j += 1
                    i += 1

                print(f"\nPaís: {pais_buscado}")
                print(f"Número de viajeros/as distintos que lo han visitado: {len(viajeros_del_pais)}")
                if len(viajeros_del_pais) > 0:
                    print("Nombres:")
                    i = 0
                    while i < len(viajeros_del_pais):
                        print(f"  - {viajeros_del_pais[i]}")
                        i += 1

        case "9":
            print("\nSaliendo del programa. ¡Hasta pronto!")
            break

        case _:
            print("Opción no válida. Seleccione un número del menú.")