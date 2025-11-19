
# opción 1

offset = 5
valor_imprimir = -4
for inicial in range(1,6):
    valor_imprimir += offset
    print(f'\n{valor_imprimir:3}', end=' ')
    factor = 1 if inicial % 2 else -1
    for _ in range(1,5):
        valor_imprimir += factor
        print(f'{valor_imprimir:3}', end=' ')
print('\n')

# opción 2

offset = 1
for inicial in range(1,6):
    valor_imprimir = inicial
    print(f'\n{valor_imprimir:3}', end=' ')
    for valor in range(1,5):
        valor_imprimir += (10-offset) if valor % 2 else offset
        print(f'{valor_imprimir:3}', end=' ')
    offset += 2
print('\n')