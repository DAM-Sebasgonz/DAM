entradas = {
    "Platea": {
    "asientos_totales": 100,
    "asientos_disponibles": 100,
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
                zona_disponible()
            case "2":
                hacer_reserva()
            case "3": 
                cancelar_reserva()
            case "4":
                mostrar_reservas()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
                              
def zona_disponible():
    """
    Muestra la cantidad de asientos disponibles en una zona específica.
    solicitamos al usuario que ingrese la zona y mostramos la disponibilidad de los asientos en esa zona.
    """
    zona_dispo = input("Ingrese la zona para ver disponibilidad (Platea, Palco, Proscenio) --> ").upper().capitalize() 
    if zona_dispo not in entradas:
        print("Zona no valida. Solo se puede elegir entre Platea, Palco o Proscenio.") #Si la zona no es valida mostramos un mensaje de error
    else:
        dispo_asientos = entradas[zona_dispo]["asientos_disponibles"]
        print(f"En la zona {zona_dispo} hay {dispo_asientos} asientos disponibles")
                    
def verificar_NIF_NIE( valor:str ) -> bool:
    '''Verifica que valor sea un NIF o NIE correcto.
       valor es el nif o nie a validar.
       Retorna True si es correcto, False en caso contrario.''' #Esto se ha sacado de un ejemplo que haz colgado en el aula virtual

    alfabeto_nif = 'TRWAGMYFPDXBNJZSQVHLCKE'

    if len(valor) != 9:
        print('1')
        return False
    if valor[0].isdigit(): # NIF
        if not valor[:8].isdigit():
            return False
    elif not (valor[0] in 'XYZ' and valor[1:8].isdigit()): # NIE
        return False 

    numero = valor[:8].replace('X','0').replace('Y','1').replace('Z','2')
    if alfabeto_nif[int(numero)%23] != valor[-1]:
        return False
    return True

def hacer_reserva ():
    """
    Permite al usuario reservar entradas en una zona específica.
    Solicita al usuario la zona, la cantidad de asientos a reservar, el DNI y el nombre del comprador. 
    """
    zona_reser = input("Ingrese la zona para reservar (Platea, Palco, Proscenio) --> ").upper().capitalize() 
    if zona_reser not in entradas:
        print("Zona no valida. Solo se puede elegir entre Platea, Palco o Proscenio.") 
    else:
        numero_asientos_pedir = int(input("Ingrese la ccantidad de asientos a reservar --> "))
        if numero_asientos_pedir > entradas[zona_reser]["asientos_disponibles"]:
            print(f"No hay suficientes asientos disponibles en la zona {zona_reser}.)") #Si no hay suficientes asientos mostramos un mensaje de error
        else:
            dni_comprador = input ("Ingrese el DNi del comprador -->")
            if not verificar_NIF_NIE(dni_comprador):
                print("DNI no válido.") # Si el DNI no es valido mostramos un mensaje de error
                return
            nombre_comprador = input("Ingrese el nombre del comprador --> ")
            entradas [zona_reser]["asientos_disponibles"] -= numero_asientos_pedir # Restamos los asientos reservados a la disponibilidad de la zona
            entradas [zona_reser]["reservas"].append({ #
                "dni": dni_comprador, 
                "nombre": nombre_comprador, # Agregamos la reserva a la lista de reservas de la zona correspondiente
                "asientos_reservados": numero_asientos_pedir
            })
            print(f"Reserva realizada con exito para {numero_asientos_pedir} asientos en la zona {zona_reser}.")

def cancelar_reserva():
    dni_cancelar = input("Ingrese el DNI del comprador para cancelar la reserva --> ")
    if not verificar_NIF_NIE(dni_cancelar): 
        print("DNI no válido.")
        return
    for zona, datos in entradas.items():
        for reserva in datos["reservas"]:
            if reserva["dni"] == dni_cancelar:
                datos["asientos_disponibles"] += reserva["asientos_reservados"]
                datos["reservas"].remove(reserva) # Eliminamos la reserva de la lista de reservas de la zona correspondiente
                print(f"Reserva cancelada para el DNI {dni_cancelar} en la zona {zona}.")
                return
   
def mostrar_reservas():
    for zona, datos in entradas.items(): #usamos items para obtener tanto la zona como los datos asociados a esa zona
        print(f"Zona: {zona}")
        if not datos["reservas"]:
            print("No hay reservas en esta zona.")
        else:
            for reserva in datos["reservas"]:
                print(f"  DNI: {reserva['dni']}, Nombre: {reserva['nombre']}, Asientos reservados: {reserva['asientos_reservados']}") # Mostramos todas las reservas de la zona correspondiente 

if __name__ == "__main__": 
    funcion_menu() 
    
    
# Cada vez que se quiere acceder al diccionario mediante el [reserva] se entra y se pregunta directamente por el dato del diccionario.