cont = 0
for num1 in range(100,999):
    for num2 in range(100,999):
        numero = num1 * num2
        numero_str = str(numero)
        if numero_str == numero_str[::-1]:
            print(f'{numero_str:8}', end='    ')
            cont += 1
            if cont == 6:
                cont = 0
                print()