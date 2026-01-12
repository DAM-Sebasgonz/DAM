import csv

with open("files/contactosdict.csv", "r", newline ="\n") as csvfile:

    reader = csv.DictReader(csvfile, delimiter=",")                          
    for fila in reader:
        # en cada iteración se escribe un diccionario que se muestra por pantalla
        # el objeto reader creado sólo se puede recorrer una vez
        print(fila)
        print(f'\tnombre: {fila["nombre"]}\n\templeo: {fila["email"]} \n\tcorreo:{fila["email"]}')