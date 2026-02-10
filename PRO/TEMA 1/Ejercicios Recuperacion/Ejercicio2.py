from random import randint

monedasp = int(input("Introduce el número de monedas: "))
monedas = monedasp

while monedasp > 0:
    
    monedasp = monedasp - 1
    
    n1 = randint(1, 9)
    n2 = randint(1, 9)
    n3 = randint(1, 9)
    
    print(f"Los números son: {n1}, {n2} y {n3}")
    
    if n1 == n2 == n3:
        print("Has ganado 5 monedas")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Has ganado 2 monedas")
    else:
        print("No has ganado nada")
        
    if monedas <= 0:
        print("No te quedan monedas, el juego ha terminado.")
    
    seguir = input("¿Quieres seguir jugando? (s/n): ").lower()
    if seguir != 's':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    
ganancias = monedas - monedasp
print("\nPartida Terminada")
print(f"Monedas finales: {monedas}")
print(f"Ganancia/Perdida : {ganancias}")
