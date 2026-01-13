def sinDuplicados(lista):
    if lista == []:  # caso base
        return []
    
    primero = lista[0]
    resto = sinDuplicados(lista[1:])  # llamo a la función con el resto de la lista
    
    if primero in resto:  # si ya está en la lista del resto
        return resto      # lo salto
    else:
        return [primero] + resto  # si no, lo pongo al principio
    
print(sinDuplicados([1, 3, 5, 2, 1, 4, 7, 7, 3]))



