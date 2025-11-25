'''Realizar un programa en Python para llevar la gestión de los precios de los 
artículos de una tienda, así como la cantidad vendida en total de cada artículo para lo cual, 
habrá que tener 3 vectores. 
 
1. Nombres: guardará los nombres de los artículos 
2. Precios: guardará los precios de los artículos 
3. Cantidades vendidas: guardará la cantidad vendida en total de cada artículo 
 
Además, este programa debe implementar las siguientes opciones que van a mostrarse en 
un menú: 
 
1. Introducir un artículo nuevo – Registrar un nuevo artículo con nombre y precio 
2. Hacer una venta – Solicitar nombre de producto y cantidad a vender 
3. Mostrar información – Mostrar nombre, precio, cantidad vendida e importe de los 
artículos, además del total 
4. Borrar un artículo 
5. Borrar todos los artículos 
6. Salir 
 '''
articulos=[]
while True:
    print("Bienvenido al menu principal. Elige entre las siguientes opciones:\n1. Introducir un nuevo artículo.\n2. Hacer una venta.\n3. Mostrar información.\n4. Borrar un artículo.\n5. Borrar todos los artículos.\n6. Salir")
    eleccion=input("Escoja entre las opciones > ")
    match eleccion:
        case '1':  # Introducir un nuevo artículo
            producto = []
            nombre = input("Introduzca el nombre del producto: ")
            while True:
                try:
                    precio = float(input("Introduzca el precio del producto: "))
                    if precio < 0:
                        print("Error. El precio no puede ser menor que 0.")
                    else:
                        unidades = 0  # Unidades vendidas inicializadas a 0
                        producto.append(nombre)
                        producto.append(precio)
                        producto.append(unidades)
                        break
                except:
                    print("Error. El precio debe ser un número válido.")
            articulos.append(producto)
            print(f"Producto '{nombre}' añadido con éxito.")

        case '2':  # Hacer una venta
            print(f"Listado de productos")
            for i in range(len(articulos)):
                print(f"{articulos[i][0]} | ", end=" ")

            solicitar = input("Solicita el nombre del producto: ")
            encontrado = False
            for i, producto in enumerate(articulos):
                if producto[0] == solicitar:  # Comparar nombres de productos
                    encontrado = True
                    while True:
                        try:
                            venta = int(input("Introduzca la cantidad a vender: "))
                            if venta < 0:
                                print("Error. La cantidad no puede ser negativa.")
                            else:
                                articulos[i][2] += venta  # Actualizar cantidad vendida
                                print(f"Se han vendido {venta} unidades de '{solicitar}'.")
                                break
                        except:
                            print("Error. La cantidad debe ser un número entero.")
                    break
            if not encontrado:
                print(f"Error. El producto '{solicitar}' no se encuentra registrado.")
        case '3':
            for i in range(len(articulos)):
                cantidad_vendida=articulos[i][1]*articulos[i][2]
                articulos[i].append(cantidad_vendida)
            for i in range(len(articulos)):
                print(f"Nombre: {articulos[i][0]} | Precio: {articulos[i][1]} | Unidades: {articulos[i][2]} | Importe total venta: {articulos[i][3]}")
            total=0
            for i in range(len(articulos)):
                total+=articulos[i][3]
            print(f"Total de venta de productos: {total}")
        case '4':
            encontrado=False
            print(f"Listado de productos")
            for i in range(len(articulos)):
                print(f"{articulos[i][0]} | ", end=" ")
            borrado=input("Introduce un producto para borrar sus registros: ")
            for i in range(len(articulos)):
                if articulos[i][0]==borrado:
                    localizador=i
                    encontrado=True
            if encontrado:
                articulos.pop(localizador)
                print("Artículo eliminado con éxito.")
            elif not encontrado:
                print("Artículo no disponible / mal especificado.")
        case '5':
            print("Borrando la lista...")
            articulos.clear()
            print("Lista borrada con éxito.")
        case '6':
            break
print("Gracias por utilizar el sistema gestor.")
exit()            