import random

# Definición de las constantes
PALOS = ('oros', 'copas', 'bastos', 'espadas')
VALORES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'sota', 'caballo', 'rey')

def generarMazo(palos, valores):
    """
    Genera y baraja un mazo completo de baraja española.
    
    Parámetros:
        palos: tupla con los palos de la baraja
        valores: tupla con los valores de las cartas
    
    Retorna:
        Lista de tuplas (valor, palo) representando las cartas barajadas
    """
    mazo = []
    
    # Generar todas las combinaciones de cartas
    for palo in palos:
        for valor in valores:
            mazo.append((valor, palo))
    
    # Barajar el mazo
    random.shuffle(mazo)
    
    return mazo

def generarManoJugador(mazo):
    """
    Extrae 3 cartas del mazo para un jugador.
    
    Parámetros:
        mazo: lista de cartas disponibles
    
    Retorna:
        Lista con 3 tuplas representando las cartas del jugador
    """
    mano = []
    
    # Extraer 3 cartas del mazo
    for i in range(3):
        if mazo:  # Verificar que haya cartas disponibles
            carta = mazo.pop()  # Extraer la última carta del mazo
            mano.append(carta)
    
    return mano

def imprimirManoJugador(mano, numero_jugador):
    """
    Imprime las cartas de un jugador de forma legible.
    
    Parámetros:
        mano: lista con las cartas del jugador
        numero_jugador: número del jugador para identificarlo
    """
    print(f"\nJugador {numero_jugador}:")
    print("-" * 30)
    
    for i, carta in enumerate(mano, 1):
        valor, palo = carta
        print(f"  Carta {i}: {valor} de {palo}")
    
    print("-" * 30)

# Programa principal
def main():
    print("=" * 50)
    print("SIMULADOR DE REPARTO DE CARTAS - JUEGO DEL ENVITE")
    print("=" * 50)
    
    # Solicitar número de jugadores
    while True:
        try:
            num_jugadores = int(input("\n¿Cuántos jugadores participarán? (3-10): "))
            
            if 3 <= num_jugadores <= 10:
                break
            else:
                print("Error: El número de jugadores debe estar entre 3 y 10.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
    
    # Generar el mazo barajado
    mazo = generarMazo(PALOS, VALORES)
    print(f"\nMazo generado con {len(mazo)} cartas.")
    
    # Verificar que hay suficientes cartas
    cartas_necesarias = num_jugadores * 3
    if cartas_necesarias > len(mazo):
        print(f"Error: No hay suficientes cartas para {num_jugadores} jugadores.")
        return
    
    print(f"Repartiendo {cartas_necesarias} cartas para {num_jugadores} jugadores...\n")
    
    # Repartir cartas a cada jugador
    for i in range(1, num_jugadores + 1):
        mano = generarManoJugador(mazo)
        imprimirManoJugador(mano, i)
    
    print(f"\nCartas restantes en el mazo: {len(mazo)}")
    print("\n" + "=" * 50)
    print("REPARTO COMPLETADO")
    print("=" * 50)

# Ejecutar el programa
if __name__ == "__main__":
    main()