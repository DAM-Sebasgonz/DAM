n = int(input("Ingrese el valor de n: "))

while n < 3 or n % 2 == 0:
    print("Error: n debe ser impar y mayor o igual a 3.")
    n = int(input("Ingrese el valor de n: "))

mitad = n // 2

i = 0
while i < n:

    diferencia = mitad - i
    if diferencia < 0:
        diferencia = -diferencia

    espacios = diferencia

    distancia = mitad - diferencia

    linea = ""

    j = 0
    while j < espacios:
        linea = linea + " "
        j = j + 1

    if distancia == 0:
        linea = linea + "*"
    else:
        linea = linea + "*"
        internos = 2 * distancia - 1
        k = 0
        while k < internos:
            linea = linea + " "
            k = k + 1
        linea = linea + "*"

    print(linea)
    i = i + 1