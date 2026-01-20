import json
try:
     lista = []
     with open ("ejemplos/contactos.json", "w", newline="\n") as jsonfile:
          while True:
               campo01 = input('campo01:-> ')
               if campo01 == '@':
                    break
               campo02 = input('campo02:-> ')
               campo03 = input('campo03:-> ')
               lista.append({'campo01':campo01,'campo02':campo02,'campo03':campo03})
          json.dump(lista, jsonfile, sort_keys = True, indent = 3)
except:
     pass
#      


               
# except:
#     print('Error en la apertura del fichero')

