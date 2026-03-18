def suma_lista_anidada(lista):
    total = 0
    for elemento in lista:
        try:
            total += suma_lista_anidada(elemento)  
        except TypeError:
            total += elemento                    
    return total


# Ejemplos del ej
print(suma_lista_anidada([1, 2, [3, 4], 5]))         
print(suma_lista_anidada([[1, 2], [3, [4, 5]], 6]))   
print(suma_lista_anidada([[[[[10]]]]]))               
print(suma_lista_anidada([]))                        
