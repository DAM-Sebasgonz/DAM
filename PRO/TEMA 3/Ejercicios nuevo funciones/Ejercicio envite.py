import random

# Primero definimos las variables necesarias con los valores de la baraja española

palos = ("oros", "copas", "espadas", "bastos")
valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'sota', 'caballo', 'rey')


def generarMazo(palos, valores):
    """
    Genera y baraja un mazo completo
    """
    
    mazo = []
    
    for baraj in palos:
        for carta in valores:
            mazo.append((carta, baraj))
            
    random.shuffle(mazo)
    return mazo  

def generarManoJugador(mazo):
    
    """
    Extrar tres cartas del mazo para formar la mano del jugador
    """
    
    mano = []
    
    for i in range (3):
        if mazo:
            carta = mazo.pop()
            mano.append(carta)
    
    return mano

def imprimirManoJugador(mano, numero_jugador):
    """
    Muestra las cartas de un jugador
    """
    print(f"Mano del jugador {numero_jugador + 1}:")
    for carta in mano:
        print(f"{carta[0]} de {carta[1]}")
    print()
    
def main():
    """
        Funcion principal del programa
    """
while True:
    try:
        num_jugadores = int(input("Ingrese el numero de jugadores (3-10): "))
        
        if 3 <= num_jugadores <= 10:
            break
        else:
            print("Numero inválido. Intente de nuevo")
    
    except ValueError:
        print("Por favor ingrese un numero valido.")
        
mazo = generarMazo(palos, valores)

cartas_necesarias = num_jugadores * 3

if cartas_necesarias > len(mazo):
    print("No hay suficientes cartas en el mazo para todos los jugadores.")

print(f"Repartiendo cartas para {num_jugadores} jugadores...\n")
for i in range(num_jugadores):
    mano = generarManoJugador(mazo)
    imprimirManoJugador(mano, i)
    
print(f"Cartas restantes en el mazo: {len(mazo)}")

if __name__ == "__main__":
    main()
        