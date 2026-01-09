# Ejercicio 1 (Python) - Seguimiento de variables
# Objetivo: depurar paso a paso y observar la evolución de a, b y c.

def main() -> None:
    a = b = c = 0

    a = 5

    a += 2
    b = a

    b = 3

    c = a
    a += 1

    b += 1
    c = b

    b -= 3

    c = -3
    c *= 2
    c += 1

    a *= b
    a *= b * c

    c -= 1
    a += c

    a -= 5
    c = a

    temp = c
    c += 1
    b = b // temp   # división entera

    a = a // 5

    print("FIN")
    input("Pulsa ENTER para terminar...")

if __name__ == "__main__":
    main()
