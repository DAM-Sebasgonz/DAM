import json

with open ("C:/DAM/PRO/TEMA 3/Ficheros/FICHEROS/files/contactos.json", "r") as jsonfile:
    datos = json.load(jsonfile)

    # datos es una lista donde cada elemento es un diccionario

    for fila in datos:
        print(fila) # en orden inverso
        # print(f'\tnombre: {fila["nombre"]}\n\templeo: {fila["empleo"]} \n\tcorreo:{fila["email"]}')