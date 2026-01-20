def cuentaParImpar(numero):
    if numero == 0:
        return (1, 0)
    
    if numero < 10:
        if numero % 2 == 0:
            return (1, 0)
        else:
            return (0, 1)
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    pares_resto, impares_resto = cuentaParImpar(resto_numero)
    
    if ultimo_digito % 2 == 0:
        return (pares_resto + 1, impares_resto)
    else:
        return (pares_resto, impares_resto + 1) #quice hacerlo como lo explicaste en clases para el dia del examen verlo mas claro por si cae ejercicio de recursividad
    
print(cuentaParImpar(345))