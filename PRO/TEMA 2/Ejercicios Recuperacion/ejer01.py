ventas = [
    ("47898511E", 5, 12780.78),
    ("Y9413423C", 7, 699.0),
    ("47898511E", 7, 532.90),
    ("42993341Q", 12, 5715.99),
    ("Y9413423C", 15, 958.05)
]

clientes = [
    ("Nuria Costa", "47898511E", "Calle Las Flores 355"),
    ("Jorge Russo", "Y9413423C", "Mirasol 218"),
    ("Julián Rodriguez", "42993341Q", "La Mancha 761"),
    ("María Fernández", "X0915730P", "Calle La Centinela 23")
]

while True:

    print("""\n--- MENÚ DE GESTIÓN DE CLIENTES Y VENTAS ---"""
          """\n1. Añadir cliente"""
          """\n2. Eliminar cliente"""
          """\n3. Añadir venta"""
          """\n4. Facturación del mes"""
          """\n5. Listado de clientes"""
          """\n9. Salir""")

    opc = input("Seleccione una opción: ").strip()

    match opc:

        case "1":
            print("\n--- Añadir cliente ---")
            nombre = input("Nombre del cliente: ").strip()
            nif = input("NIF/NIE del cliente: ").strip().upper()
            direccion = input("Dirección del cliente: ").strip()

            indice = -1
            i = 0
            while i < len(clientes):
                if clientes[i][1] == nif:
                    indice = i
                    break
                i += 1

            if indice != -1:
                print("Ya existe un cliente con ese NIF/NIE.")
            else:
                clientes.append((nombre, nif, direccion))
                print(f"Cliente '{nombre}' añadido correctamente.")

        case "2":
            print("\n--- Eliminar cliente ---")
            nif = input("Introduce el NIF/NIE del cliente a eliminar: ").strip().upper()

            indice_cliente = -1
            i = 0
            while i < len(clientes):
                if clientes[i][1] == nif:
                    indice_cliente = i
                    break
                i += 1

            if indice_cliente == -1:
                print("No existe ningún cliente con ese NIF/NIE.")
            else:
                indice_venta = -1
                i = 0
                while i < len(ventas):
                    if ventas[i][0] == nif:
                        indice_venta = i
                        break
                    i += 1

                if indice_venta != -1:
                    print("No se puede eliminar el cliente porque tiene ventas registradas en el mes.")
                else:
                    cliente = clientes[indice_cliente]
                    print(f"\nDatos del cliente:")
                    print(f"Nombre: {cliente[0]}")
                    print(f"NIF/NIE: {cliente[1]}")
                    print(f"Dirección: {cliente[2]}")
                    confirmacion = input("Desea eliminar este cliente? (S/N): ").strip().upper()
                    if confirmacion == "S":
                        clientes.pop(indice_cliente)
                        print("Cliente eliminado correctamente.")
                    else:
                        print("Eliminación cancelada.")

        case "3":
            print("\n--- Añadir venta ---")
            nif = input("NIF/NIE del cliente: ").strip().upper()

            indice_cliente = -1
            i = 0
            while i < len(clientes):
                if clientes[i][1] == nif:
                    indice_cliente = i
                    break
                i += 1

            if indice_cliente == -1:
                print("ERROR: El cliente no existe en la lista de clientes.")
            else:
                dia = 0
                dia_ok = False
                while not dia_ok:
                    try:
                        dia = int(input("Día del mes (1-31): "))
                        if 1 <= dia <= 31:
                            dia_ok = True
                        else:
                            print("ERROR: El día debe estar entre 1 y 31.")
                    except ValueError:
                        print("ERROR: Introduce un número entero válido.")

                importe = 0.0
                importe_ok = False
                while not importe_ok:
                    try:
                        importe = float(input("Importe de la venta (€): "))
                        if importe > 0:
                            importe_ok = True
                        else:
                            print("ERROR: El importe debe ser mayor que 0.")
                    except ValueError:
                        print("ERROR: Introduce un número válido.")

                indice_venta = -1
                i = 0
                while i < len(ventas):
                    if ventas[i][0] == nif and ventas[i][1] == dia:
                        indice_venta = i
                        break
                    i += 1

                if indice_venta != -1:
                    print("Ya existe una venta para este cliente en ese día.")
                else:
                    ventas.append((nif, dia, importe))
                    print("Venta registrada correctamente.")

        case "4":
            print("\n--- Facturación del mes ---")

            if len(clientes) == 0:
                print("No hay clientes registrados.")
            else:
                i = 0
                while i < len(clientes):
                    cliente = clientes[i]
                    nombre_cliente = cliente[0]
                    nif_cliente = cliente[1]
                    direccion_cliente = cliente[2]

                    ventas_cliente = []
                    j = 0
                    while j < len(ventas):
                        if ventas[j][0] == nif_cliente:
                            ventas_cliente.append(ventas[j])
                        j += 1

                    n = len(ventas_cliente)
                    k = 0
                    while k < n - 1:
                        l = 0
                        while l < n - k - 1:
                            if ventas_cliente[l][1] > ventas_cliente[l + 1][1]:
                                temp = ventas_cliente[l]
                                ventas_cliente[l] = ventas_cliente[l + 1]
                                ventas_cliente[l + 1] = temp
                            l += 1
                        k += 1

                    print("\n" + "=" * 50)
                    print(f"FACTURA - {nombre_cliente}")
                    print(f"NIF/NIE: {nif_cliente}")
                    print(f"Dirección: {direccion_cliente}")
                    print("-" * 50)

                    if len(ventas_cliente) == 0:
                        print("Este cliente no tiene ventas en el mes.")
                    else:
                        total = 0.0
                        j = 0
                        while j < len(ventas_cliente):
                            venta = ventas_cliente[j]
                            print(f"Día {venta[1]}: {venta[2]:.2f} €")
                            total += venta[2]
                            j += 1
                        print("-" * 50)
                        print(f"Número de ventas: {len(ventas_cliente)}")
                        print(f"TOTAL MES: {total:.2f} €")

                    print("=" * 50)
                    i += 1

        case "5":
            print("\n--- Listado de clientes ---")

            if len(clientes) == 0:
                print("No hay clientes registrados.")
            else:
                lista_ordenada = []
                i = 0
                while i < len(clientes):
                    lista_ordenada.append(clientes[i])
                    i += 1

                n = len(lista_ordenada)
                i = 0
                while i < n - 1:
                    j = 0
                    while j < n - i - 1:
                        if lista_ordenada[j][0] > lista_ordenada[j + 1][0]:
                            temp = lista_ordenada[j]
                            lista_ordenada[j] = lista_ordenada[j + 1]
                            lista_ordenada[j + 1] = temp
                        j += 1
                    i += 1

                print("\nNombre - NIF/NIE - Dirección")
                print("-" * 60)
                i = 0
                while i < len(lista_ordenada):
                    c = lista_ordenada[i]
                    print(f"{c[0]} - {c[1]} - {c[2]}")
                    i += 1
                print(f"\nTotal de clientes: {len(clientes)}")

        case "9":
            print("\nSaliendo del programa. ¡Hasta pronto!")
            break

        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")