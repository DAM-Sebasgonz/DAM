#RECURSIVIDAD

# def suma_n(n):
#     if n == 1:
#         return 1
#     return n + suma_n(n - 1)

# def suma_lista(lista) -> int:
#     if lista == []:
#         return 0
#     return lista[0] + suma_lista(lista[1:])

# def lista_invertida(lista) -> list:
#     if lista == []:
#         return []
#     return 

# if __name__ == "main":
#     lista = [1, 3, 5, 7, 9]
#     print(f'La suma de los primeros numeros es {suma_lista(lista)}')

# FACTORIAL CON RECURSIVIDAD:

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
if __name__ == "__main__":
    print(factorial_recursivo(5))