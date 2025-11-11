tupla = (2,3,4,5,2,3,2,4,5,-7,2)

num_tupla = []

try:
    valor = int(input("valor ? --> "))
except ValueError:
    print("Error... se debe introducir un numero")
else:
    pos = 0
    cnt_veces = tupla.count(valor)
    nro_veces = 0
    if cnt_veces > 0:
        while nro_veces < cnt_veces:
            pos_encontrada = tupla.index(valor, pos)
            print(f"posicion = {pos_encontrada}")
            pos = pos_encontrada + 1
            nro_veces +=1
    else:
        print("Error... el numero no se encuentra en la tupla")



