def digitoNoSeEncuentra(numero:int, digito:int) -> bool:
    if numero == 0:
        return True #parada

    ultimo_digito = numero % 10

    if ultimo_digito == digito:
        return False

    return digitoNoSeEncuentra(numero // 10, digito)    

if __name__ == "__main__":
    print(digitoNoSeEncuentra(1323, 3))