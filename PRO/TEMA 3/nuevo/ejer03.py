def calcular_mcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_fraccion(n, d):
    mcd = calcular_mcd(n, d)
    return n // mcd, d // mcd

def leer_fraccion():
    n = int(input("Introduce numerador: "))
    d = int(input("Introduce denominador: "))
    return simplificar_fraccion(n, d)

def escribir_fraccion(n, d):
    if d == 1:
        print(f"Resultado: {n}")
    else:
        print(f"Resultado: {n}/{d}")

def sumar_fracciones(n1, d1, n2, d2):
    res_n = n1 * d2 + d1 * n2
    res_d = d1 * d2
    return simplificar_fraccion(res_n, res_d)

def restar_fracciones(n1, d1, n2, d2):
    res_n = n1 * d2 - d1 * n2
    res_d = d1 * d2
    return simplificar_fraccion(res_n, res_d)

def multiplicar_fracciones(n1, d1, n2, d2):
    return simplificar_fraccion(n1 * n2, d1 * d2)

def dividir_fracciones(n1, d1, n2, d2):
    return simplificar_fraccion(n1 * d2, d1 * n2)

def menu():
    while True:
        print("\n--- MENÚ FRACCIONES ---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        opc = input("Selecciona una opción: ")
        
        if opc == '5':
            break
        
        print("Fracción 1:")
        n1, d1 = leer_fraccion()
        print("Fracción 2:")
        n2, d2 = leer_fraccion()
        
        if opc == '1': 
            rn, rd = sumar_fracciones(n1, d1, n2, d2)
        elif opc == '2': 
            rn, rd = restar_fracciones(n1, d1, n2, d2)
        elif opc == '3': 
            rn, rd = multiplicar_fracciones(n1, d1, n2, d2)  
        elif opc == '4': 
            rn, rd = dividir_fracciones(n1, d1, n2, d2)
        
        escribir_fraccion(rn, rd)

if __name__ == "__main__":
    menu()