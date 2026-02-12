# generación de código

from random import randint, choice

# codigo = srt_dep '-' str_empleado + str_nif_nie

# lectura de los datos
nombre_completo = input('Introduzca su nombre completo -> ')
nif_nie = input('Introduzca su nif/nie -> ').upper()
departamento = input('Introduzca el departamento -> ')
# generar str_dpto
str_depto = ""
lista_aux = departamento.split()
for palabra in lista_aux:
    if len(palabra) >= 3:
        str_depto += palabra[0].upper()

str_depto = str_depto + 'X'*(3-len(str_depto))
print(str_depto)

# generar str_empleado
ALFABETO = 'abcdefghijklmnñopqrstuvwxyz'
nombre_completo = nombre_completo.replace('á', 'a')
nombre_completo = nombre_completo.replace('é', 'e')
nombre_completo = nombre_completo.replace('í', 'i')
nombre_completo = nombre_completo.replace('ó', 'o')
nombre_completo = nombre_completo.replace('ú', 'u')
nombre_completo = nombre_completo.replace('Á', 'A')
nombre_completo = nombre_completo.replace('É', 'E')
nombre_completo = nombre_completo.replace('Í', 'I')
nombre_completo = nombre_completo = nombre_completo.replace('Ó', 'O')
nombre_completo = nombre_completo.replace('Ú', 'U')
lista_aux = nombre_completo.split()
long_str_empleado = 4 * len(lista_aux)
str_empleado = ''
alfabeto_empleado = ''
for palabra in lista_aux:
    for letra in palabra:
        if letra not in alfabeto_empleado:
            alfabeto_empleado += letra
while len(alfabeto_empleado) > 0 and len(str_empleado) < long_str_empleado:
    caracter = choice(alfabeto_empleado)
    str_empleado += caracter
    pos = alfabeto_empleado.find(caracter)
    alfabeto_empleado = alfabeto_empleado[:pos] + alfabeto_empleado[pos+1:]
while len(str_empleado) < long_str_empleado:
    if (letra := choice(ALFABETO)) not in str_empleado:
        str_empleado += letra
print(str_empleado)

# generar str_nif_nie
str_nif_nie = ''
com_busqueda = 1 if nif_nie[0] in "XYZ" else 0
while len(str_nif_nie) != 2:
    digito = nif_nie[randint(com_busqueda, 7)]
    if digito not in str_nif_nie:
        str_nif_nie += digito
if com_busqueda:
    str_nif_nie = nif_nie[0] + str_nif_nie
print(str_nif_nie)

# imprimir el código
codigo = str_depto + '-' + str_empleado + str_nif_nie
print(f'El código del empleado es -> {codigo}\n')