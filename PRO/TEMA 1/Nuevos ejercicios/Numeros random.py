
from random import randint

valor_adivinar = randint(1,10)
print(valor_adivinar)
nro_total_intentos = 5
intentos = 1

while intentos <= nro_total_intentos:
    try:
        nro_usuario = int(input(f"Estas en el intento {intentos}-{nro_total_intentos}.Introduzca un numero del 1-10 -->"))
        if 0 < nro_usuario <= 10:
            if valor_adivinar == nro_usuario:
                print(f"Enhorabuena has acertado en {intentos} intentos ")
                break
            elif nro_total_intentos < 0 or nro_usuario < 10:
                intentos += 1
    except:
        print("debe introducir un numero") 
else:
    print(f"Po po po...no has acertado. El numero era el {valor_adivinar}")
print("\nFin de ejecucion ")