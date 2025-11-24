# Escriba un programa en Python que dada una lista de valores numéricos enteros obtenga su
# máximo valor. En este ejercicio no se puede usar los métodos max() y sorted().
# Ejemplos:
# La salida debe mostrarse como se muestra a continuación.
# [ 3, 7, 100, 2, -20] -> 100
# [200, -100, 4, 8, 200] -> 200
# [-7, -10, -6, -3] -> -3 

lista = [1,2,3,4,5,6,7,8,9,10,1645,123,345,52345,23542345,23452354,]

maximo = lista[0]

for elemento in lista:
    if elemento > maximo:
        maximo = elemento

print("El valor máximo es:", maximo)



