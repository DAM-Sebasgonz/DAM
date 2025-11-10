# i = 4
# print("hola")
# valor = input ("intrduzca un numero: ") # con la almohadilla se puede poner un comentario en cualquier linea del codigo
# i = i + int(valor)
# print(0)
# a = "b"
# # literales
# # 0 , "a",

# a = 3
# b = 3
# print(id(a))
# print(id(b))

# encadenamiento de asignaciones

# a = b = 3, 5 #a cada numero se le asignara una variable
# print(a)
# print(b)

# asignacion de variable en una sola linea
# hay varias maneras
# PRIMER CASO
# a = 3 b = 5
# print(a)
# print(b)
# SEGUNDO CASO
# a, b = 3, 5
# a, b = b, a
# print(a, b)
# a, b = "3" , "5"
# a, b b , a
# print(a, b)
# print(type(a), type(b))

# b = 10
# a = b + 3 * 2
# print (a)

# operador walrus :=

# entrada = input("introduzca dos valores enteros por un blanco: ")
# valor1, valor2= entrada.split() #separa las cadenas
# valor1 = int(valor1)
# valor2 = int(valor2)
# print(entrada)

# a = int(input("numero 1: "))
# b = int(input("numero 2: "))

# print("el valor mayor:", max(a,b))
# print("el valor menor:", min(a,b))

# a = int(input("numero 1: "))
# b = int(input("numero 2: "))
# print("los numero ordenados son:", min(a,b), max(a,b))

# leo 3 imprimir de forma decreciente
# leo 3 numero (a, b, c)

# a = int(input("numero 1: "))
# b = int(input("numero 2: "))
# c = int(input("numero 3: "))
# print(
#     "los numeros ordenados son:", min(a, b, c), max(a, b, c)
# )  # preguntar maestro porque esto no funciona

# lista = [1,"2", True,]# las listas pueden contener varios valores un entero, un string y un booleano (estos solo pueden ser true or false)

# conjunto = {1,2,1}
# print(conjunto)

# numerador = 10
# denominador = 3
# print(numerador // denominador)  # este da el cociente de la divison
# print(numerador % denominador)  # este da el resto de la division
# print(numerador / denominador)  # este da el resultador de la division
# a = 1
# b = 2
# print(a**b)
# print(pow(a, b)) # Ambas maneras son potencias
# c = 2 * (3 + 4 * 2)
# print(c)

# a = int(input("dd ->:"))
# print(a)

# print(round(123.656))  # REDONDEO o truncamiento en funcion de lo que diga el parametro

# palabra = "hola"

# print(len(palabra))  # len te permite saber la longitud de un string
# print(palabra[-4])

# operaciones con string

# nueva = "hola" + " " + "adios"  #suma
# print(nueva)

# patron = "+*12"
# print(1 * patron) #repeticion

# a = "0123456789"
# print("#" + a[2:1] + "#")  # slice permite cortar un string

# a = "0123456789"
# print(a[-7:-5:-2])

# a = "0123456789"
# print(a[::-1]) invierte

# a = "aaaBBB"

# print(a.upper())
# print(a.lower())

# se quiere crear un  programa en python que permita cambiar la temperatura entre grados centigrados y grados farenheit.
# el programa lee una temperatura y la escala en la que se encuentra
# muestra el resultado en la otra escala

# temp_or = float(input('Introduzca la temperatura: '))
# escala = input('Introduzca la escala C / F: ')
# if escala == 'C' :
#     temp_dest = (temp_or * 9 // 5) + 32
#     print(temp_or, 'ºC --> ', temp_dest, 'ºF')
# else:
#     if escala == 'F':
#         temp_dest = (temp_or - 32) * 5 / 9
#         print(temp_or, 'ºF --> ', temp_dest, 'ºC')
#     else:
#         print('Error...escala incorrecta')

# se quiere leer un numero y sumar todos sus digitos

# see lee una palabra si es palindrome

# palabra = input("introduzca una palabra")

# if palabra == palabra[::-1]:
#     print("la palabra es palindrome")
# else:
#     print("la palabra no es palindrome")

# se quiere calcular la media de tres numeros enteros
# que se llen por teclado

# num1 = int(input("introduzca el primer numero: "))
# num2 = int(input("introduzca el segundo numero: "))
# num3 = int(input("introduzca el tercer numero"))

# media = (num1 + num2 + num3) / 3
# print("la media es = ", media)

# # un = asigna, dos == preguntan


# # # # # BUCLES FOR 

# # for con range k

# iterador

# for i in range(10): 
#     print(i)

# palabra = "Hola"

# for letra in palabra:
#     print(letra) # descompone la palabra "hola" en cada uno de sus letras

# print(range(10))

# palabra = "Hola"
# for letra in palabra:
#     print(letra)

# for num in range(4):
#     print(num)
#     num += 100
#     print(num)

# for letra in "murcielago":
#     if letra not in "murcielago":
#         break
#     print(letra)

# for num in range(10):
#     if num % 2:
#         continue
#     print(num)

# palabra = input("Introduzca una palabra -->")
# for letra in palabra:
#     if letra == "z":
#         print("La palabra contiene z")
#         break
# else:
#     print("La palabra no contiene z")

# for i in range(1,6):
#     j = 5-i
#     print(" " *i + "*" * j , end="")
#     print("*"* j + "" * i)

# for i in range(1,6):
#     j = 5-i
#     print("*" *j + " " * i, end="")
#     print(" " *i + "*" * j)

