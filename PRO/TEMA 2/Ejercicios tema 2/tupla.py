tupla = (2,3,4,5,2,3,2,4,5,-7,2)

num_tupla = []

try:
    valor = int(input("valor ? --> "))
except ValueError:
    print("Error... se debe introducir un numero")
else:
    if (cnt_veces := tupla.count(valor)):
        print(f"El numero se encuentra {tupla.index(valor)}")
    else:
        print("Error... el numero no se encuentra en la tupla")



