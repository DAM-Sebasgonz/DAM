'''Dado un diccionario escribir un programa que compruebe si todos sus valores son iguales o no.'''

diccionario={'a': 1, 'b': 1, 'c': 1, 'd': 1}
iguales=True
valor=diccionario['a']
for clave in diccionario.values():
    if clave!=valor:
        print(f'Los valores no son iguales.')
        iguales=False
        break
if iguales:
    print('Todos los valores son iguales')
