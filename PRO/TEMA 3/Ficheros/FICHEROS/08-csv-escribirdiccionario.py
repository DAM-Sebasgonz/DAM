import csv

contactos = [
        ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
        ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
        ("Javier", "Analista de datos", "javier@ejemplo.com"),
        ("Marta", "Experta en Python", "marta@ejemplo.com") ]

campos = ["nombre", "empleo", "email"] 
with open("files/contactosdict.csv", "w", newline ="\n") as csvfile:

    # se necesita esta lista para pasarla como parámetro en fieldnames
    writer = csv.DictWriter(csvfile, fieldnames = campos)                          

    # escribe un encabezado con los elementos de la lista campos
    writer.writeheader()

    for nombre, empleo, email in contactos:
        # en cada iteración se genera un diccionario que se escribe en el fichero
        writer.writerow({ "nombre":nombre, "empleo":empleo, "email":email })