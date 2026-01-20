import json

contactos = [
        ("Manuel", "Desarrollador Web", "manuel@ejemplo.com") ,
        ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
        ("Javier", "Analista de datos", "javier@ejemplo.com"),
        ("Marta", "'Experta en Python", "marta@ejemplo.com") ]

datos = []                    

# creamos una lista donde cada elemento
# es un diccionario con los datos a escribir en el fichero

for nombre, empleo, email in contactos:
        datos.append({"nombre":nombre, "empleo":empleo, "email":email})

with open ("files/contactos.json", "w") as jsonfile:
        json.dump(datos, jsonfile)
