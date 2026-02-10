n = int(input("Introduce cuántos números primos quieres mostrar: "))

while n <= 0:
    print("El número debe ser positivo")
    print(n)

contador = 0
numero = 2

while contador < n:
    es_primo = True
    
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        print(numero)
        contador += 1
    
    numero += 1