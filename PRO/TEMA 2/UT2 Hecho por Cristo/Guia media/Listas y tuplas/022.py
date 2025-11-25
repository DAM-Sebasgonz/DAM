'''Escribir un programa en Python que indique si dos fichas de dominó cuyos 
valores  se  leen  por  el  teclado  encajan o  no.  Las  fichas  se  almacenan  
en  tuplas,  por  ejemplo: (3,4) y (5,4). 
 
Ejecuciones del programa pueden ser la siguientes: 
 
Indique la primera ficha: 3,5 
Indique la segunda ficha: 4,6 
 
Las fichas no encajan 
 
Indique la primera ficha: 2,3 
Indique la segunda ficha: 0,3 
 
Las fichas si encajan 
 
Debe  comprobarse  que  se  leen  fichas  correctas  de  dominó  y  no  se  permite  seguir  la 
ejecución del programa hasta que se introduzca datos correctos. 
'''
unir=False
while True:
    try:
        valor_ficha_1_a=int(input("Escribe un valor numérico entre 0-6 inclusive para la ficha 1 /1º cara: "))
        valor_ficha_1_b=int(input("Escribe un valor numérico entre 0-6 inclusive para la ficha 1 /2º cara: "))
        valor_ficha_2_a=int(input("Escribe un valor numérico entre 0-6 inclusive para la ficha 2 /1º cara: "))
        valor_ficha_2_b=int(input("Escribe un valor numérico entre 0-6 inclusive para la ficha 2 /2º cara: "))
    except:
        print("Error. Por favor, introduce valores numéricos.")
    else:
        if valor_ficha_1_a>=0 and valor_ficha_1_a<=6 and valor_ficha_1_b>=0 and valor_ficha_1_b<=6 and valor_ficha_2_a>=0 and valor_ficha_2_a<=6 and valor_ficha_2_b>=0 and valor_ficha_2_b<=6:
            tupla_ficha_1=(valor_ficha_1_a, valor_ficha_1_b)
            tupla_ficha_2=(valor_ficha_2_a, valor_ficha_2_b)
            break
        else:
            print("Error. Introduce los datos nuevamente. (Rango 0-6)")
print(tupla_ficha_1)
print(tupla_ficha_2)
for i in tupla_ficha_1: #en la iteración 1 y 2 
    if i in tupla_ficha_2:
        unir=True

if unir:
    print("La ficha se puede unir.")
else:
    print("No se puede unir.")
