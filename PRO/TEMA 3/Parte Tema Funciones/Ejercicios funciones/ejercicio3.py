def encuentraNroSeries(lista: list) -> int:

    nro_serie = 0
    variable = 0

    for valor in lista:
        if valor != variable:
            variable = valor
            nro_serie += 1
    return nro_serie

def posicionSerieMasLarga(lista:int) -> int:
    variable = None
    long_max_actual = 0
    lista_pos = []

    for indice , valor in enumerate(lista):
        if valor != variable:
            long_serie_actual = 1
            pos_serie_actual = indice
            variable = valor

        else:




if __name__ == "__main__":
    print(encuentraNroSeries[1,1,8,8,8,8,0,0,0,2,10,10])