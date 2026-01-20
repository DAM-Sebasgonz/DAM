import json
try:
     with open ("ejemplos/contactos.json", "r", newline="\n") as jsonfile:
          # creamos un objeto de la clase
          datos = json.load(jsonfile)
          for fila in datos:
               print(fila) 
except:
    print('Error en la apertura del fichero')

