# Escribir un programa en Python que permita encontrar la/las claves con el valor máximo.
# El resultado se debe mostrar como una tupla (clave, valor).

# REVISION DE INTEGRIDAD DE DATOS Y DE VALIDACIÓN DE ENTRADAS

todos_str = True
todos_int = True
diccionario = {}

# Entrada de cantidad de registros
try:
    registros = int(input("Escribe una cantidad de registros para el diccionario > (nº enteros mayores que 0): "))
except:
    print("Error. Escribe una cantidad válida.")
else:
    if registros > 0:
        for i in range(registros):
            clave = input("Ingresa una clave: ")
            valor = input("Ingresa un valor: ")
            
            # Determinar si el valor es un número entero
            if valor.isdigit() or valor[0] == '-':  # Si es un número, lo guardamos como int
                valor = int(valor)
                diccionario[clave] = valor
            else:  # Si no es un número, lo guardamos como string
                diccionario[clave] = valor
    else:
        print("Error. La cantidad de registros debe ser mayor que 0.")

# Revisar el tipo de los valores en el diccionario
for valor in diccionario.values():
    if type(valor) != str:  # Si hay algún valor que no es un str, entonces no todos son str
        todos_str = False
        break

if todos_str:
    # Si todos los valores son str
    primer_valor = list(diccionario.values())[0]
    valor_maximo = primer_valor
    for valor in diccionario.values():
        if valor > valor_maximo:
            valor_maximo = valor
    claves = []
    for clave, valor in diccionario.items():
        if valor == valor_maximo:
            claves.append(clave)
    solucion = (claves, valor_maximo)
    print(solucion)

elif not todos_str:
    # Revisamos si todos los valores son int
    for valor in diccionario.values():
        if type(valor) != int:  # Si hay algún valor que no es un int, no son todos int
            todos_int = False
            break
    
    if todos_int:
        # Si todos los valores son int
        primer_valor = list(diccionario.values())[0]
        valor_maximo = primer_valor
        for valor in diccionario.values():
            if valor > valor_maximo:
                valor_maximo = valor
        claves = []
        for clave, valor in diccionario.items():
            if valor == valor_maximo:
                claves.append(clave)
        solucion = (claves, valor_maximo)
        print(solucion)
#Quitar la solución donde los valores se pueden mezclar, no tiene sentido. Poner la condición de que si hay datos mezclados aparezcan el error de que no se puede hacer.