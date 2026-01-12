import csv

# datos en una lista para generar fichero .csv

contactos = [
        ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
        ("Lorena" , "Gestora de proyectos", "lorena@ejemplo.com"),
        ("Javier", "Analista de datos", "javier@ejemplo.com"),
        ("Marta", "Experta en Python", "marta@ejemplo.com") ]

with open ("files/contactos.csv", "w", newline="\n") as csvfile:
        # creamos un objeto de la clase
        writer = csv.writer(csvfile, delimiter = ";")
        for contacto in contactos:
                writer.writerow(contacto)