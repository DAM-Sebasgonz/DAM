def suma_lista_anidada(lista):
    total = 0
    for elemento in lista:
        try:
            total += suma_lista_anidada(elemento)  
        except TypeError:
            total += elemento                    
    return total

if __name__ == "__main__":
    
    suma_lista_anidada([1, 2, [3, 4], 5])      
    suma_lista_anidada([[1, 2], [3, [4, 5]], 6]) 
    suma_lista_anidada([[[[[10]]]]])               
    suma_lista_anidada([])                     #Pruebas del PDF 
