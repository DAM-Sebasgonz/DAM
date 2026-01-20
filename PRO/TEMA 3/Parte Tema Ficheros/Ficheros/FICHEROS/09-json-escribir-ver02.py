import json

contactos = [
        ("Manuel", "Desarrollador Web", "manuel@ejemplo.com") ,
        ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
        ("Javier", "Analista de datos", "javier@ejemplo.com"),
        ("Marta", "'Experta en Python", "marta@ejemplo.com") ]

datos = []                    

# creamos un diccionario con los datos de la lista

for nombre, empleo, email in contactos:
        datos.append({"nombre":nombre, "empleo":empleo, "email":email})

with open ("files/contactos.json", "w") as jsonfile:
        json.dump(datos, jsonfile, sort_keys = True, indent = 3)
