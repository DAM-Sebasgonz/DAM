# ejercicio supermercado

productos = {}       # {"lacteos": {"leche": [10, 1.20]}, ...}
tickets = {}

tipos_productos = ["lacteos", "panaderia", "carniceria", "fruta", "verduras",
                   "menaje", "limpieza", "licores"]

menu = """1. Insertar producto
2. Actualizar inventario
3. Realizar venta 
4. Estadisticas
5. Salir"""

sub_menu = """
A. Productos mas vendidos
B. Regresar al menu anterior"""

while True:
    print("="*40)
    print(menu)
    print("="*40)
    opcion_menu = input("Opcion --> ")
    match opcion_menu:
        case "1":
            print("="*40)
            producto_entrada = input("Introduzca un producto --> ").strip().title()
            tipos_productosent = input("Introduca el tipo de producto --> ").strip().title()
            if tipos_productosent not in tipos_productos:
                print("El tipo de producto no se encuentra en el catálogo")
            else:
                try:
                    cantidad = int(input("Introduzca cantidad del producto --> "))
                    precio = float(input("Precio de venta del producto --> "))
                    # Crear el tipo si no existe aún
                    if tipos_productosent not in productos:
                        productos[tipos_productosent] = {}
                    productos[tipos_productosent][producto_entrada] = [cantidad, precio]
                    print(f"{producto_entrada} se ha añadido correctamente al inventario")
                except ValueError:
                    print("Error valor incorrecto")
        case "2":
            producto_entrada = input("Introduzca el producto a modificar --> ").strip().title()
            tipos_productosent = input("Introduzca el tipo del artículo --> ").strip().title()

            if tipos_productosent not in productos:
                print(f"Error: {tipos_productosent} no existe en el inventario")
                continue

            if producto_entrada not in productos[tipos_productosent]:
                print(f"Error: {producto_entrada} no existe")
                continue

            try:
                cantidad = int(input("Cantidad que desea cambiar --> "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa")
                else:
                    productos[tipos_productosent][producto_entrada][0] += cantidad
                    print("Cantidad del producto modificada correctamente")
            except ValueError:
                print("Cantidad invalida")
        case "3":
            productos_vendidos = []

            producto_entrada = input("Que producto desea llevar --> ").strip().title()
            tipos_productosent = input("Que tipo de producto es --> ").strip().title()

            if tipos_productosent not in productos or producto_entrada not in productos[tipos_productosent]:
                print("El producto no existe en el inventario")
                continue

            try:
                cantidad_deseada = int(input("Que cantidad desea llevar --> "))
                if cantidad_deseada <= 0:
                    print("La cantidad debe ser mayor que cero")
                    continue

                existencia = productos[tipos_productosent][producto_entrada][0]
                precio = productos[tipos_productosent][producto_entrada][1]

                if cantidad_deseada > existencia:
                    print(f"Solo hay {existencia} unidades")
                    cantidad_vendida = existencia
                else:
                    cantidad_vendida = cantidad_deseada

                if cantidad_vendida > 0:
                    productos_vendidos.append((producto_entrada, cantidad_vendida, precio))
                    productos[tipos_productosent][producto_entrada][0] -= cantidad_vendida
                    print(f"Se ha añadido a su cesta {producto_entrada} x {cantidad_vendida}")
            except ValueError:
                print("Cantidad invalida")

            print("="*40)
            continuar = input("Desea seguir comprando? (s/n): ").strip().lower()
            if continuar != "s":
                break
        case "4":
            while True:
                print("="*40)
                print(sub_menu)
                print("="*40)
                opc_submenu = input("Opción --> ").strip().upper()
                match opc_submenu:
                    case "A":
                        print("Función aún no implementada.")
                    case "B":
                        break
                    case _:
                        print("Opción inválida")
        case "5":
            print("Hasta luego...")
            break
        case _:
            print("Opción inválida")
