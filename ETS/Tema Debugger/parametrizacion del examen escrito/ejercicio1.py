
def Perfecto(num):

    divisor = 1
    suma_divisores = 0
    while divisor <= num // 2:
        if num % divisor == 0:
            suma_divisores = suma_divisores + divisor
        divisor += 1

    if num == suma_divisores:   
        retur
    else:
        print(f"El numero {num}")