def calcular_mcd(a,b):
    """Calculamos el maximo comun divisor de dos numeros """
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_fraccion(n,d):
    """Simplificamos la fraccion utilizando el maximo comun divisor """
    mcd = calcular_mcd(n,d)
    return n // mcd ,d // mcd

def leer_fraccion():
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    return simplificar_fraccion(numerador, denominador)

def escribir_fraccion(n,d):
    """Escribimos la fraccion"""
    if d == 1:
        print(f"Resultado: {n}")
    else:
        print(f"Resultado: {n}/{d}")

def sumar_fracciones (n1,d1,n2,d2):
    """Sumamos dos fracciones y simplificamos el resultado"""
    res_n = n1 * d2 + d1 * n2
    res_d = d1 * d2 
    return simplificar_fraccion(res_n, res_d)

def restar_fracciones(n1,d1,n2,d2):
    """Restamos dos fracciones y simplificamos el resultado"""
    res_n = n1*d2-d1*n2
    res_d = d1*d2
    return simplificar_fraccion(res_n, res_d)

def multiplicar_fracciones(n1,d1,n2,d2):
    """Multiplicamos dos fracciones y simplificamos el resultado"""
    return simplificar_fraccion(n1*n2, d1*d2)

def menu():
    while True:
        print("""1 - Sumar fracciones
2 - Restar fracciones
3 - Multiplicar fracciones
4 - Salir""")
        opcion = input("Selecciona una opcion: ")

        match opcion:
            case "1":
                print("Fraccion 1:")
                n1, d1 = leer_fraccion()
                print("Fraccion 2:")
                n2, d2 = leer_fraccion()
                rn, rd = sumar_fracciones(n1, d1, n2, d2)
                escribir_fraccion(rn, rd)
            case "2":
                print("Fraccion 1:")
                n1, d1 = leer_fraccion()
                print("Fraccion 2:")
                n2, d2 = leer_fraccion()
                rn, rd = restar_fracciones(n1, d1, n2, d2)
                escribir_fraccion(rn, rd)
            case "3":
                print("Fraccion 1:")
                n1, d1 = leer_fraccion()
                print("Fraccion 2:")
                n2, d2 = leer_fraccion()
                rn, rd = multiplicar_fracciones(n1, d1, n2, d2)
                escribir_fraccion(rn, rd)
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, por favor selecciona una opcion del 1 al 4.")

if __name__ == "__main__":
    menu()


