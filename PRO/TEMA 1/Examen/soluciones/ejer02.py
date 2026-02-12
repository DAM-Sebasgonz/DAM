# generación del patrón
patron = '+-'
fila = int(input('Introduzca el número de filas -> '))
print()
for i in range(fila):
    c = 1
    pos_patron = i % 2
    print(c, end = ' ')
    for j in range(fila - i - 1, 0, -1):
        print(patron[pos_patron], end = ' ')
        c = c + 1
        pos_patron = (pos_patron + 1) % 2
        print(c, end = ' ')
    print('\n')
