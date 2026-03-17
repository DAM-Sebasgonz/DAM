def num_menor_media(lista):
    if not lista:
        return 0
    media = sum(lista) / len(lista)
    return sum(1 for x in lista if x < media)


def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            return False
    return True