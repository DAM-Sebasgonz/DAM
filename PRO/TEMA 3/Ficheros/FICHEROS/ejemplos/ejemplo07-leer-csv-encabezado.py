import csv

try:
    with open ("ejemplos/contactos-libreria-encabezado.csv", "r", newline="\n") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for fila in reader:
            print(f'campo01 -> {fila['campo01']}\ncampo02 -> {fila['campo02']}\ncampo03 -> {fila['campo03']}\n')
except:
    print('Error en la apertura del fichero')