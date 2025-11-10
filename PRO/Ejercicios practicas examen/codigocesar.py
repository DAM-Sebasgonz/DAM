texto = input("Introduce el texto a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

abc_min = "abcdefghijklmnopqrstuvwxyz"
abc_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

resultado = ""
i = 0

while i < len(texto):
    c = texto[i]
    j = 0
    encontrado = False

    while j < len(abc_min):
        if c == abc_min[j]:
            nuevo = j + desplazamiento

            while nuevo >= len(abc_min):
                nuevo -= len(abc_min)
            while nuevo < 0:
                nuevo += len(abc_min)

            resultado += abc_min[nuevo]
            encontrado = True
            break
        j += 1

    k = 0
    while not encontrado and k < len(abc_may):
        if c == abc_may[k]:
            nuevo = k + desplazamiento

            while nuevo >= len(abc_may):
                nuevo -= len(abc_may)
            while nuevo < 0:
                nuevo += len(abc_may)

            resultado += abc_may[nuevo]
            encontrado = True
            break
        k += 1

    if not encontrado:
        resultado += c

    i += 1

print("Texto cifrado:", resultado)