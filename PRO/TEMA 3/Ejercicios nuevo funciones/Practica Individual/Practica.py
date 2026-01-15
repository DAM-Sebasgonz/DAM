entradas = {
    "Platea": {
    "asientos_totales": 100,
    "asientos_disponibles": 80,
    "reservas": []
 },
    "Palco": {
    "asientos_totales": 50,
    "asientos_disponibles": 50,
    "reservas": []
 },
    "Proscenio": {
    "asientos_totales": 30,
    "asientos_disponibles": 30,
    "reservas": []
 }
} 

menu = """
1. Mostrar disponibilidad por zona
2. Reservar entradas
3. Cancelar una reserva
4. Mostrar todas las reservas
5. Salir del programa
"""

def funcion_menu():
    while True:
        print("="*40)
        print(menu)
        print("="*40)
        opcion = input("Seleccione una opción --> ")
        match opcion:
            case "1":
                zona_dispo = input("Ingrese la zona para ver disponibilidad (Platea, Palco, Proscenio) --> ").upper().capitalize()
                if zona_dispo not in entradas:
                    print("Zona no valida. Solo se puede elegir entre Platea, Palco o Proscenio.")
                else:
                    dispo_asientos = entradas[zona_dispo]["asientos_disponibles"]
                    print(f"En la zona {zona_dispo} hay {dispo_asientos} asientos disponibles")                           
            case "2":
                zona_reser = input("Ingrese la zona para reservar (Platea, Palco, Proscenio) --> ").upper().capitalize()
                if zona_reser not in entradas:
                    print("Zona no valida. Solo se puede elegir entre Platea, Palco o Proscenio.") 
                else:
                    numero_asientos = int(input("Ingrese la ccantidad de asientos a reservar --> "))
                    if numero_asientos > entradas[zona_reser]["asientos_disponibles"]:
                        print(f"No hay suficientes asientos sdisbponibles enn la zona {zona_reser}.)")
                    
            case "3": # Segun el DNi del comprador
                
                print("Cancelando una reserva...")
                
            case "4":
                print("Mostrando todas las reservas:")
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
                
funcion_menu()
        