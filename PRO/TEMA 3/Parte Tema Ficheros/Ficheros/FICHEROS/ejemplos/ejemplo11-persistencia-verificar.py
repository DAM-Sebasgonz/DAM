import pickle
import os.path

try:
     if os.path.exists("ejemplos/contactos.pckl"):
          with open ("ejemplos/contactos.pckl", "rb") as pcklfile:
               lista = pickle.load(pcklfile)
               if lista != []:
                    for fila in lista:
                         print(fila)
               else:
                    print('Advertencia... El fichero está vacío')

     else:
          print("Error...el fichero no existe")
except:
     print("Error...En la apertura del fichero")

     
     



               
# except:
#     print('Error en la apertura del fichero')

