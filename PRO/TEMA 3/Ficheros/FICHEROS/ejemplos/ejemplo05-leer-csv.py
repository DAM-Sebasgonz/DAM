import csv

try:
    with open ("ejemplos/contactos-libreria.csv", "r", newline="\n") as csvfile:
        # creamos un objeto con el método reader() para la lectura de los datos
        # los datos se almacenan en el objeto reader 
        reader = csv.reader(csvfile, delimiter = ";")
        for campo01, campo02, campo03 in reader:
            print(f'campo01-> {campo01}\ncampo02-> {campo02}\ncampo03-> {campo03}\n')
except:
    print('Error en la apertura del fichero')
