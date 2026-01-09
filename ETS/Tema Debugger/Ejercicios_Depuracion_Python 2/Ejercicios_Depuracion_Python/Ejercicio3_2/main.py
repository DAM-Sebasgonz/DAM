# Ejercicio 3_2 (Python) - Bucle infinito y estado de variables

def main() -> None:
    veces = 4

    # BUG 1: el while nunca termina (bucle infinito)
    while veces > 0:
        print("Hola! me quedan", veces, "instantes de vida")
        # Falta actualizar 'veces'

    print("Adios :(")

    # BUG 2: incluso si corriges el while decrementando 'veces',
    # el segundo bucle podría no ejecutarse si 'veces' termina valiendo 0.
    for vueltas in range(veces):
        print("Esta es mi vuelta número", vueltas)

    print("Hasta luego :)")
    input("Pulsa ENTER para terminar...")

if __name__ == "__main__":
    main()
