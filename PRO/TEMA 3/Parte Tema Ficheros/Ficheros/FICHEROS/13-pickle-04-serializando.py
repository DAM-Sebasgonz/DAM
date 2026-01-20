# ejemplo de serialización de una lista

import pickle
# Creamos una clase de prueba

class Persona:
    def __init__(self, nombre):
        self. nombre = nombre

    def __str__(self):
        return self.nombre

# Creamos la lista con los nombres
nombres = ["Héctor", "Mario", "Marta" ]
personas = [] 
                                                                                                                                                                  
for n in nombres:
    p = Persona(n)
    personas.append(p)

# Escribimos la lista en el fichero con pickle
f = open ('ficheros/personas.pckl', 'wb')
pickle.dump (personas, f)
f.close()

# Leemos la lista del fichero con pickle

f = open ('ficheros/personas.pckl', 'rb') 
personas = pickle.load(f)
f.close()

for p in personas:
    print (p)