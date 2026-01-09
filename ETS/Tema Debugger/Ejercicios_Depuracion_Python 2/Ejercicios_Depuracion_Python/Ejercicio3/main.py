# Ejercicio 3 (Python) - Breakpoint condicional por umbral

def main() -> None:
    valor = 0
    for contador in range(100_000):
        # Coloca un breakpoint CONDICIONAL en la siguiente línea:
        # condición sugerida: valor > 10_000_000
        valor = valor + contador * 23 // 11

    print(valor)
    print("Terminé.")
    input("Pulsa ENTER para terminar...")

if __name__ == "__main__":
    main()
