valor = input("Escriba un numero > 0 --> ")
if valor.isdigit():
    numero = int(valor)
    len_campo = len(str(20 * numero)) + 2
    for aux in range(1,21):
        print(f'{aux * numero:{len_campo}}', end=" ")
        if aux % 5 == 0:
            print()
elif valor [0] == "-" and valor [1:].isdigit():
    print("Error ... El numero debe ser mayor que 0")
else:
    print("Error... debe introducir un numero")