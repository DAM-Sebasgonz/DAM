def esNumeroPerfecto(numero:int) -> bool:

    def calculaDivisoresPropios ():
        lista = []
        for divisor in range(1, numero // 2 + 1):
            if numero % divisor == 0:
                lista.append(numero)
        return lista
    
    if numero == sum(calculaDivisoresPropios(numero)):
        return True
    return False

if __name__ == "__main__":
    numero =  8128
    print(f"{numero} Es numero perfecto")