# ejercicio supermercado

productos ={}

tickets = {}

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
            tipos_productos = ["lacteos", "panaderia", "carniceria", "fruta","verduras", "menaje", "limpieza", "licores"]
            print("="*40)
            producto_entrada = input("Introduzca un producto --> ").strip()
            tipos_productosent = input("Introduca el tipo de producto --> ").strip()
            if tipos_productosent not in tipos_productos:
                print(f"El Tipo de producto no se encuentra en el catalogo")
            else:
                try:
                    cantidad = int(input("Introduzca cantidad del producto --> "))
                    precio = float("Precio de venta del producto --> ")
                    productos[tipos_productosent][producto_entrada] = [cantidad, precio]
                    print(f"{producto_entrada} se ha añadido correctamente al inventario")
                except ValueError:
                    print("Error valor incorrecto")
        case "2":
            producto_entrada = input("Introduzca el producto a modificar --> ").strip()
            tipos_productosent = input("Introduzca el tipo del articulo --> ").strip()
            if tipos_productosent not in tipos_productos:
                print(f"Error {tipos_productosent} no existe")
                continue
            if producto_entrada not in productos[tipos_productos]:
                print(f"Error {producto_entrada} no existe")
                continue
            try:
                cantidad = int(input("Cantidad que desea cambiar --> "))
                if cantidad < 0:
                    print("La cantidad del producto no puede ser menor a 0")
                    continue
                productos[tipos_productosent][productos][0] += cantidad
                print("Cantidad del producto modificada correctamente")
            except ValueError:
                print("Cantidad invalida")  
        case "3":
            productos_vendidos = []
            producto_entrada = input("Que producto desea llevar --> ").strip()
            tipos_productosent = input("Que tipo de producto es --> ").strip()
            if producto_entrada not in productos:
                print(f"El producto {producto_entrada} no esta en el inventario")
                continue
            if tipos_productosent not in tipos_productos:
                print(f"El producto {tipos_productosent} no existe")
                continue
            try:
                cantidad_deseada = int(input("que cantidad de producto desea llevar --> "))
                if cantidad <= 0:
                    print("La cantida de producto no puede ser negativa o igual a cero")
                    continue
                existencia_producto = productos[tipos_productosent][producto_entrada][0]
                precio = productos[tipos_productosent][1]             
                if cantidad_deseada > existencia_producto:
                    print(f"Solo hay {existencia_producto} unidades del producto")
                    cantidad_vendida = existencia_producto
                else:
                    cantidad_vendida = cantidad_deseada
                if cantidad_vendida > 0:
                    productos_vendidos.append((producto_entrada, cantidad_vendida, precio))
                    productos[tipos_productosent][producto_entrada][0] -= cantidad_vendida
                    print(f"Se ha añadido a su cesta el producto {producto_entrada} y se ha llevado {cantidad_deseada}")
            except ValueError:
                        print("Cantidad invalida")
                        print("="*40)
                        continuar =  input("Desea seguir comprando? (s/n): ").strip().lower()
                        if continuar != "s":
                            break
        case "4":
            while True:
                print("="*40)
                print(sub_menu)
                print("="*40)
                opc_submenu = input("Opción --> ").upper
                match opc_submenu:
                    case "a":
                        pass
                    case "b":
                        pass
        case "5":
            print("Hasta luego...") 
        case _:
            print("opcion invalida")

                       
