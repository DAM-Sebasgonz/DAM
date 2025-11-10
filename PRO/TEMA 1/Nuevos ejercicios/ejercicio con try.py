try:
    numero = int(input("numero -->"))
except ValueError:
    print("debe introducir un numero")
else:
    if numero >= 1:
        if numero % 2 == 0:
            potencia_dos = 2
            while potencia_dos <= numero:
                if potencia_dos == numero:
                    print(f"el numero {numero} es potencia de dos")
                    break
                potencia_dos *= 2
            else:
                print(f"el numero {numero} no es potencia de 2")
    else:
        print("El numero no es potencia de dos")