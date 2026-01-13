# Ejercicio 2 (Python) - Tabla de multiplicar del 6
# Objetivo:
#  1) Corregir errores de sintaxis y lógica.
#  2) Sustituir el uso de ++ (que NO existe en Python) por incrementos equivalentes.
#  3) Refactorizar usando un bucle.

# numero = 6
# paso = 1

# print("Esta es la tabla del 6")
# print("----------------------")

# print(paso, "x", numero, "=", (paso * numero))

# print(paso, "x", numero, "=", (paso+= * numero))
# print(paso, "x", numero, "=", (paso+= * numero))
# print(paso, "x", numero, "=", (paso+= * numero))
# print(paso, "x", numero, "=", (paso+= * numero))

# print(" 6 x", numero, "=", (paso++ * numero))
# print(paso, "x", numero, "=", (paso++ * numero))
# print(paso, "x", numero, "=", (paso++ * numero)
# print(paso, "x", numero, "=", (paso++ * numero)
# print(paso, "x", numero, "=", 10 * numero)

# print("----------------------")
# input("Pulsa ENTER para terminar...")


# numero = 6

# print("Esta es la tabla del 6")
# print("----------------------")

# for paso in range(1, 11):
#     print(paso, "x", numero, "=", (paso * numero))

# print("----------------------")
# input("Pulsa ENTER para terminar...")


numero = 6
paso = 1

print("Esta es la tabla del 6")
print("----------------------")

print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

paso += 1
print(paso, "x", numero, "=", (paso * numero))

print("----------------------")
input("Pulsa ENTER para terminar...")
