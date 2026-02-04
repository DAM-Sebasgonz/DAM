import os

def inicializar_inventario():
    """
    Retorna un diccionario con el inventario inicial de la tienda
    organizado por categorías
    """
    inventario = {
        "Electrónica": [
            {"nombre": "Laptop HP 15", "precio": 599.99, "stock": 5},
            {"nombre": "Mouse Logitech", "precio": 25.50, "stock": 15},
            {"nombre": "Teclado Mecánico", "precio": 89.99, "stock": 8},
            {"nombre": "Monitor Samsung 24", "precio": 179.99, "stock": 6},
            {"nombre": "Webcam HD", "precio": 45.00, "stock": 12},
            {"nombre": "Auriculares Bluetooth", "precio": 65.00, "stock": 10}
        ],
        "Hogar": [
            {"nombre": "Cafetera Express", "precio": 45.00, "stock": 3},
            {"nombre": "Licuadora 600W", "precio": 55.99, "stock": 7},
            {"nombre": "Plancha de Vapor", "precio": 35.50, "stock": 9},
            {"nombre": "Aspiradora Robot", "precio": 199.99, "stock": 4},
            {"nombre": "Microondas 20L", "precio": 89.00, "stock": 5},
            {"nombre": "Batidora de Mano", "precio": 28.50, "stock": 11}
        ],
        "Electricidad": [
            {"nombre": "Cable THHN 12 AWG (metro)", "precio": 1.25, "stock": 500},
            {"nombre": "Interruptor Simple", "precio": 3.50, "stock": 45},
            {"nombre": "Tomacorriente Doble", "precio": 4.25, "stock": 38},
            {"nombre": "Bombilla LED 9W", "precio": 2.99, "stock": 120},
            {"nombre": "Cinta Aislante", "precio": 1.50, "stock": 60},
            {"nombre": "Tablero Eléctrico 12 Polos", "precio": 45.00, "stock": 8},
            {"nombre": "Breaker 20A", "precio": 12.50, "stock": 25}
        ],
        "Jardín": [
            {"nombre": "Cortadora de Césped", "precio": 225.00, "stock": 3},
            {"nombre": "Manguera 25m", "precio": 18.99, "stock": 12},
            {"nombre": "Tijeras de Podar", "precio": 15.50, "stock": 18},
            {"nombre": "Rastrillo Metálico", "precio": 9.99, "stock": 14},
            {"nombre": "Regadera 10L", "precio": 12.00, "stock": 8},
            {"nombre": "Fertilizante 5kg", "precio": 22.50, "stock": 20},
            {"nombre": "Pala de Jardín", "precio": 14.75, "stock": 10}
        ],
        "Pinturas": [
            {"nombre": "Pintura Látex Blanco 4L", "precio": 28.99, "stock": 25},
            {"nombre": "Pintura Esmalte Negro 1L", "precio": 15.50, "stock": 18},
            {"nombre": "Brocha 3 pulgadas", "precio": 5.25, "stock": 30},
            {"nombre": "Rodillo con Extensión", "precio": 12.00, "stock": 15},
            {"nombre": "Thinner 1L", "precio": 6.50, "stock": 22},
            {"nombre": "Cinta de Enmascarar", "precio": 3.75, "stock": 35},
            {"nombre": "Pintura Anticorrosiva 1L", "precio": 18.00, "stock": 12}
        ],
        "Madera": [
            {"nombre": "Tabla de Pino 2x4x8", "precio": 8.50, "stock": 40},
            {"nombre": "MDF 18mm (plancha)", "precio": 32.00, "stock": 15},
            {"nombre": "Triplay 15mm (plancha)", "precio": 28.50, "stock": 20},
            {"nombre": "Listón de Eucalipto 2x2", "precio": 4.25, "stock": 50},
            {"nombre": "Pegamento para Madera 250ml", "precio": 7.50, "stock": 25},
            {"nombre": "Lija Grano 80 (pliego)", "precio": 1.25, "stock": 60},
            {"nombre": "Tornillos Madera 2\" (caja 100)", "precio": 5.99, "stock": 30}
        ]
    }
    
    return inventario

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")

def mostrar_menu():
    """
    Muestra el menú principal del sistema
    """
    print("\n" + "="*60)
    print("SISTEMA DE INVENTARIO DE TIENDA".center(60))
    print("="*60)
    print("\n MENÚ PRINCIPAL:")
    print("-" * 60)
    print("1. Agregar producto")
    print("2. Actualizar stock de producto")
    print("3. Consultar productos por categoría")
    print("4. Ver valor total del inventario")
    print("5. Ver productos con bajo stock")
    print("0. Salir")
    print("-" * 60)

if __name__ == "__main__":
    inventario = inicializar_inventario()
    
    print("\n¡Bienvenido al Sistema de Inventario de Tienda!")
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            limpiar_pantalla()
            ...
            pausar()
            
            
        elif opcion == "2":
            limpiar_pantalla()
            ...
            pausar()
            
        elif opcion == "3":
            limpiar_pantalla()
            ...
            pausar()
            
        elif opcion == "4":
            limpiar_pantalla()
            ...
            pausar()
            
        elif opcion == "5":
            limpiar_pantalla()
            ...
            pausar()
                        
        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Inventario!")
            print("Saliendo del programa...")
            break
            
        else:
            print("\nOpción inválida. Por favor, seleccione una opción del menú.")
            pausar()