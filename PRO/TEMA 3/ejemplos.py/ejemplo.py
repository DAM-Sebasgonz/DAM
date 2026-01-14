#1º CSV
#2º CSV CON ENCABEZADO
#3º JSON

# diferentes ficheros

import csv

alumno = ["Nombre", "nif" , "CIAL" , "Tipo_Estudio"]





with open ("alumnos01.csv", "w" ) as csvfile:
    writer = csv.writer (csvfile, delimiter= ";")

    




