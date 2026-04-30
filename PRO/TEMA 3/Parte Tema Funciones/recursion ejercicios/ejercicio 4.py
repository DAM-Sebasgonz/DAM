def digitoNoSeEncuentra(numero: int, digito: int) -> bool:
    # Caso base: si el número es 0, el dígito no se encontró
    if numero == 0:
        return True
    
    # Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # Si el último dígito coincide con el dígito buscado, retornar False
    if ultimo_digito == digito:
        return False
    
    # Caso recursivo: continuar buscando en el resto del número
    return digitoNoSeEncuentra(numero // 10, digito)


# Ejemplos de uso
print(digitoNoSeEncuentra(1323, 5))  # True (el 5 NO está en 1323)
print(digitoNoSeEncuentra(1323, 1))  # False (el 1 SÍ está en 1323)
print(digitoNoSeEncuentra(1323, 3))  # False (el 3 SÍ está en 1323)
print(digitoNoSeEncuentra(1323, 2))  # False (el 2 SÍ está en 1323)
print(digitoNoSeEncuentra(456, 7))   # True (el 7 NO está en 456)
print(digitoNoSeEncuentra(456, 5))   # False (el 5 SÍ está en 456)

