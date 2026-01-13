import json

fichero = open("ejercicio/libreria.json", "rb")

libreria = json.load(fichero)
# for tipo, detalle in libreria.items():
#     print(tipo)
#     for elto in detalle:
#         print(elto)

print(libreria)