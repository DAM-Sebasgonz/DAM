import csv
import json

if __name__ == '__main__':

    trab_tfe = []
    trab_gc = []

    with open ("ejemplos/tenerife.csv", "r", newline="\n") as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")

        for nombre, nif, municipio in reader: 
            trab_tfe.append((nombre, nif, municipio))
    
    with open ("ejemplos/grancanaria.csv", "r", newline="\n") as csvfile:
        reader = csv.DictReader(csvfile)

        for fila in reader: 
            trab_gc.append((fila['nombre'], fila['nif'], fila['municipio']))
    
    trab_comunes = []
    for trab_01 in trab_tfe:
        for trab_02 in trab_gc:
            if trab_01[1] == trab_02[1]:
                trab_comunes.append({'nombre':trab_01[0], 'nif':trab_01[1]})

    with open ("ejemplos/trabajan-en-ambas.json", "w") as jsonfile:
        json.dump(trab_comunes, jsonfile, indent = 3)



 
