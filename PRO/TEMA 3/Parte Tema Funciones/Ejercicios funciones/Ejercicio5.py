def calculaNumeroVocales( texto ) -> int:
    if texto == "":
        return 0
    
    miletra = texto[0]
    numero_recibido = calculaNumeroVocales(texto[1:])

    if miletra in "aeiouáéíóú":
        return numero_recibido + 1
    else:
        return numero_recibido

if __name__ == "__main__":
    print(calculaNumeroVocales("aeiou"))