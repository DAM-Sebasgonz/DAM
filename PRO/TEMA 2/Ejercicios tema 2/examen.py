import random

# =============================================================================
# EJERCICIO 001 - GESTIÓN DE TIENDA (6.0 puntos)
# =============================================================================

# Estructuras de datos iniciales
articulos = {}

# Variable de control para el menú principal
salir = False

while not salir:
    # Mostrar menú principal
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE TIENDA")
    print("="*50)
    print("1. Insertar producto")
    print("2. Actualizar compra")
    print("3. Realizar venta")
    print("4. Estadísticas")
    print("5. Salir")
    print("="*50)
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    # OPCIÓN 1: INSERTAR PRODUCTO
    if opcion == '1':
        print("\n--- INSERTAR PRODUCTO ---")
        
        tipos_validos = ["Lácteos", "Panadería", "Carnicería", "Fruta", 
                         "Verduras", "Menaje", "Limpieza", "Licores"]
        
        producto = input("Nombre del producto: ").strip()
        if not producto:
            print("Error: El nombre del producto no puede estar vacío")
        else:
            print("\nTipos disponibles:", ", ".join(tipos_validos))
            tipo = input("Tipo de producto: ").strip()
            
            if tipo not in tipos_validos:
                print(f"Error: El tipo '{tipo}' no es válido")
            elif tipo in articulos and producto in articulos[tipo]:
                print(f"Error: El producto '{producto}' ya existe en '{tipo}'")
            else:
                try:
                    cantidad = int(input("Cantidad en existencia: "))
                    precio = float(input("Precio de venta: "))
                    
                    if cantidad < 0 or precio < 0:
                        print("Error: La cantidad y el precio deben ser positivos")
                    else:
                        # Crear el tipo si no existe
                        if tipo not in articulos:
                            articulos[tipo] = {}
                        
                        # Añadir el producto
                        articulos[tipo][producto] = [cantidad, precio]
                        print(f"\n✓ Producto '{producto}' añadido correctamente en '{tipo}'")
                        
                except ValueError:
                    print("Error: Valores numéricos inválidos")
    
    # OPCIÓN 2: ACTUALIZAR COMPRA
    elif opcion == '2':
        print("\n--- ACTUALIZAR COMPRA ---")
        print("(Presione INTRO en producto para terminar)")
        
        while True:
            producto = input("\nProducto: ").strip()
            if not producto:
                break
            
            tipo = input("Tipo: ").strip()
            
            if tipo not in articulos:
                print(f"Error: El tipo '{tipo}' no existe")
                continue
            
            if producto not in articulos[tipo]:
                print(f"Error: El producto '{producto}' no existe en '{tipo}'")
                continue
            
            try:
                cantidad = int(input("Cantidad comprada: "))
                if cantidad < 0:
                    print("Error: La cantidad debe ser positiva")
                    continue
                
                articulos[tipo][producto][0] += cantidad
                print(f"✓ Stock actualizado. Nueva existencia: {articulos[tipo][producto][0]}")
                
            except ValueError:
                print("Error: Cantidad inválida")
    
    # OPCIÓN 3: REALIZAR VENTA
    elif opcion == '3':
        print("\n--- REALIZAR VENTA ---")
        
        productos_vendidos = []
        
        while True:
            producto = input("\nProducto: ").strip()
            if not producto:
                break
            
            tipo = input("Tipo: ").strip()
            
            # Verificar que existe el tipo y el producto
            if tipo not in articulos:
                print(f"Error: El tipo '{tipo}' no existe")
                continue
            
            if producto not in articulos[tipo]:
                print(f"Error: El producto '{producto}' no existe en '{tipo}'")
                continue
            
            try:
                cantidad_deseada = int(input("Cantidad a comprar: "))
                if cantidad_deseada <= 0:
                    print("Error: La cantidad debe ser mayor que 0")
                    continue
                
                existencia_actual = articulos[tipo][producto][0]
                precio = articulos[tipo][producto][1]
                
                # Verificar existencias
                if cantidad_deseada > existencia_actual:
                    print(f"⚠ Advertencia: Solo hay {existencia_actual} unidades disponibles")
                    cantidad_vendida = existencia_actual
                else:
                    cantidad_vendida = cantidad_deseada
                
                if cantidad_vendida > 0:
                    productos_vendidos.append((producto, cantidad_vendida, precio))
                    # Actualizar existencias
                    articulos[tipo][producto][0] -= cantidad_vendida
                    print(f"✓ Añadido: {cantidad_vendida} x {producto} - ${precio * cantidad_vendida:.2f}")
                
            except ValueError:
                print("Error: Cantidad inválida")
            
            continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()
            if continuar != 's':
                break
        
        # Generar ticket si hay productos
        if productos_vendidos:
            cod_ticket = input("\nNúmero de ticket: ").strip()
            ticket = {cod_ticket: productos_vendidos}
            tickets.append(ticket)
            
            print(f"\n{'='*50}")
            print(f"TICKET: {cod_ticket}")
            print(f"{'='*50}")
            total = 0
            for prod, cant, precio in productos_vendidos:
                subtotal = cant * precio
                total += subtotal
                print(f"{prod:20} {cant:3} x ${precio:6.2f} = ${subtotal:8.2f}")
            print(f"{'='*50}")
            print(f"{'TOTAL:':30} ${total:8.2f}")
            print(f"{'='*50}")
        else:
            print("\nNo se realizó ninguna venta")
    
    # OPCIÓN 4: ESTADÍSTICAS
    elif opcion == '4':
        salir_estadisticas = False
        
        while not salir_estadisticas:
            print("\n" + "="*50)
            print("ESTADÍSTICAS")
            print("="*50)
            print("A. Productos más vendidos")
            print("B. Salir")
            print("="*50)
            
            opcion_est = input("Seleccione una opción: ").strip().upper()
            
            # OPCIÓN A: PRODUCTOS MÁS VENDIDOS
            if opcion_est == 'A':
                print("\n--- PRODUCTOS MÁS VENDIDOS ---")
                
                if not tickets:
                    print("No hay ventas registradas")
                else:
                    # Diccionario para acumular ventas por producto
                    ventas_por_producto = {}
                    
                    # Recorrer todos los tickets
                    for ticket in tickets:
                        for cod_ticket, productos in ticket.items():
                            for producto, cantidad, precio in productos:
                                if producto not in ventas_por_producto:
                                    ventas_por_producto[producto] = 0
                                ventas_por_producto[producto] += cantidad
                    
                    # Ordenar por cantidad vendida (descendente)
                    productos_ordenados = sorted(ventas_por_producto.items(), 
                                                 key=lambda x: x[1], reverse=True)
                    
                    # Mostrar los 3 primeros
                    print(f"\n{'PRODUCTO':<25} {'TIPO':<15} {'CANTIDAD VENDIDA'}")
                    print("-" * 60)
                    
                    for i, (producto, cantidad) in enumerate(productos_ordenados[:3], 1):
                        # Buscar el tipo del producto
                        tipo_encontrado = "N/A"
                        for tipo, prods in articulos.items():
                            if producto in prods:
                                tipo_encontrado = tipo
                                break
                        
                        print(f"{i}. {producto:<22} {tipo_encontrado:<15} {cantidad}")
            
            elif opcion_est == 'B':
                salir_estadisticas = True
            else:
                print("Opción inválida")
    
    # OPCIÓN 5: SALIR
    elif opcion == '5':
        print("\n¡Hasta luego!")
        salir = True
    
    else:
        print("Opción inválida. Intente de nuevo.")


# =============================================================================
# EJERCICIO 002 - ENCRIPTACIÓN/DESENCRIPTACIÓN (4.0 puntos)
# =============================================================================

print("\n\n" + "="*60)
print("EJERCICIO 002 - SISTEMA DE ENCRIPTACIÓN/DESENCRIPTACIÓN")
print("="*60)

# Solicitar texto al usuario
print("\nIngrese el texto a encriptar (puede ser multilínea):")
print("Escriba 'FIN' en una línea separada para terminar")

lineas_texto = []
while True:
    linea = input()
    if linea == 'FIN':
        break
    lineas_texto.append(linea)

texto_original = '\n'.join(lineas_texto)

if texto_original:
    print("\nTexto original:")
    print("-" * 50)
    print(texto_original)
    print("-" * 50)
    
    # PARTE 01: ENCRIPTACIÓN
    print("\n--- ENCRIPTACIÓN ---")
    
    # Dividir el texto en líneas
    lineas = texto_original.split('\n')
    nro_lineas = len(lineas)
    
    # Diccionario para guardar posiciones de cada letra
    pos_letras = {}
    
    # Recorrer cada línea y posición
    for num_linea, linea in enumerate(lineas):
        for posicion, letra in enumerate(linea):
            if letra not in pos_letras:
                pos_letras[letra] = []
            pos_letras[letra].append((num_linea, posicion))
        
        # Añadir el salto de línea si no es la última línea
        if num_linea < nro_lineas - 1:
            if '\n' not in pos_letras:
                pos_letras['\n'] = []
            pos_letras['\n'].append((num_linea, len(linea)))
    
    # Crear lista alfabeto con letras únicas
    alfabeto = list(pos_letras.keys())
    
    # Realizar shuffle (aleatorizar)
    random.shuffle(alfabeto)
    
    # Crear lista encriptada
    encriptada = []
    for letra in alfabeto:
        encriptada.append(pos_letras[letra])
    
    print(f"Texto encriptado exitosamente")
    print(f"Número de líneas: {nro_lineas}")
    print(f"Letras únicas: {len(alfabeto)}")
    
    # PARTE 02: DESENCRIPTACIÓN
    print("\n--- DESENCRIPTACIÓN ---")
    
    # Crear diccionario desencriptar
    desencriptar = {i: [] for i in range(nro_lineas)}
    
    # Recorrer la lista encriptada por posiciones
    for i in range(len(encriptada)):
        letra = alfabeto[i]
        lista_posiciones = encriptada[i]
        
        # Para cada tupla (fila, pos) en la lista de posiciones
        for fila, pos in lista_posiciones:
            # Añadir tupla (pos, letra) al diccionario en la clave fila
            desencriptar[fila].append((pos, letra))
    
    # Reconstruir el mensaje
    mensaje_original = []
    for linea in range(nro_lineas):
        # Ordenar las tuplas por posición
        tuplas_ordenadas = sorted(desencriptar[linea], key=lambda x: x[0])
        
        # Construir la línea
        linea_texto = ''.join([letra for pos, letra in tuplas_ordenadas])
        mensaje_original.append(linea_texto)
    
    # Unir todas las líneas
    texto_recuperado = '\n'.join(mensaje_original)
    
    print("Texto desencriptado exitosamente:")
    print("-" * 50)
    print(texto_recuperado)
    print("-" * 50)
    
    # Verificar
    if texto_original == texto_recuperado:
        print("\n✓ Verificación exitosa: El texto recuperado es idéntico al original")
    else:
        print("\n✗ Error: El texto recuperado no coincide con el original")
else:
    print("No se ingresó ningún texto")