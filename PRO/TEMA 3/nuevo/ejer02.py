def clasificaVocales(frase):
    mapeo = {
        'a': 0, 'A': 0, 'á': 0, 'Á': 0,
        'e': 1, 'E': 1, 'é': 1, 'É': 1,
        'i': 2, 'I': 2, 'í': 2, 'Í': 2,
        'o': 3, 'O': 3, 'ó': 3, 'Ó': 3,
        'u': 4, 'U': 4, 'ú': 5, 'Ú': 4, 'ü': 4, 'Ü': 4
    }

    if not frase:
        return [0, 0, 0, 0, 0, 0]

    caracter = frase[0]
    restante = clasificaVocales(frase[1:])
    
    if caracter in mapeo:
        indice = mapeo[caracter]
        restante[indice] += 1
        restante[5] += 1 # Incrementa el total (sexto elemento)
        
    return restante

# Ejemplo de uso
frase_usuario = "El melocotón está maduro y listo para comer."
resultado = clasificaVocales(frase_usuario)
print(f"Lista de vocales: {resultado}")