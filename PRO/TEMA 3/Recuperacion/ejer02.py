def clasficacionVocales(frase):
    mapeo_vocales = {
        "a":0, "A":0, "á":0, "Á":0,
        "e":1, "E":1, "é":1, "É":1,
        "i":2, "I":2, "í":2, "Í":2,
        "o":3, "O":3, "ó":3, "Ó":3,
        "u":4, "U":4, "ú":4, "Ú":4, "ü":4, "Ü":4
    }
    #A esta variable he añadido todo el tipo de variables que puede ser vocales
    if frase == "":
        return [0, 0, 0, 0, 0, 0] #condicion de parada. 
    
    caracter = frase[0]
    restante = clasficacionVocales(frase[1:])

    if caracter in mapeo_vocales:
        indice = mapeo_vocales[caracter]
        restante[indice] += 1
        restante[5] += 1 
    return restante

if __name__ == "__main__":
    frase_usuario = "El melocotón está maduro y listo para comer."
    frase_vacia = ""
    resultado = clasficacionVocales(frase_usuario) # compruebo con una frase con vocales
    print(resultado)
    resultado2 = clasficacionVocales(frase_vacia) # compruebo con un frase vacia a ver si la condicion de parada funciona. 
    print(resultado2)