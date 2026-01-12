import csv

# creamos un fichero csv sin encabezado

try:
    with open ("ejemplos/contactos-libreria.csv", "w", newline="\n") as csvfile:
            
# recuerden que si la apertura se hace en modo "a" el fichero si existe no se borran los datos

            # creamos un objeto de escritura de la clase
            writer = csv.writer(csvfile, delimiter = ";")
            while True:
                 campo01 = input('campo01:-> ')
                 if campo01 == '@':
                      break
                 campo02 = input('campo02:-> ')
                 campo03 = input('campo03:-> ')
                 writer.writerow((campo01,campo02,campo03))
except:
    print('Error en la apertura del fichero')
