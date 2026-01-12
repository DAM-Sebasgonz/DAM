import csv

# creamos un fichero csv con encabezado
try:
    with open ("ejemplos/contactos-libreria-encabezado.csv", "w", newline="\n") as csvfile:
            # creamos un objeto de la clase
            lista = ['campo01', 'campo02', 'campo03']
            writer = csv.DictWriter(csvfile, fieldnames = lista)
            writer.writeheader()
            while True:
                 campo01 = input('campo01:-> ')
                 if campo01 == '@':
                      break
                 campo02 = input('campo02:-> ')
                 campo03 = input('campo03:-> ')
                 writer.writerow({'campo01':campo01,'campo02':campo02,'campo03':campo03})
except:
    print('Error en la apertura del fichero')