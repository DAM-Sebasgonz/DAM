def es_primo(numero):
    if numero <= 1:
        return False
    divisor = 2
    while divisor <= numero // 2:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

