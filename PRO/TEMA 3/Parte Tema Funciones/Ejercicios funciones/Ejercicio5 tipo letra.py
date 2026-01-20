#ahora que queremos que diga cuantas vocales hay de cada tipo

def calculaNumeroVocalesPorTipo( texto ) -> int:
    if texto == "":
        return [0,0,0,0,0]
    
    miletra = texto[0]
    lista_recibida = calculaNumeroVocalesPorTipo(texto[1:])

    match miletra:
        case "a"| "á":
            lista_recibida[0] + 1
        case "e"| "é":
            lista_recibida[1] + 1
        case "i"| "í":
            lista_recibida[2] + 1
        case "o"| "ó":
            lista_recibida[3] + 1
        case "u"| "ú":
            lista_recibida[4] + 1
    return lista_recibida

if __name__ == "__main__":
    print(calculaNumeroVocalesPorTipo)


