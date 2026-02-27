def num_menor_media(lista):
    if not lista:
        return 0
    
    media = sum(lista) / len(lista)
    contador = len([x for x in lista if x < media])
    return contador

def esta_ordenada(lista):

    if not lista or len(lista) == 1:
        return True
    
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            return False
    return True