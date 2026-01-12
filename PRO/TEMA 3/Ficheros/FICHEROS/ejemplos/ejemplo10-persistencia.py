import pickle
import os.path

try:
     if os.path.exists("ejemplos/contactos.pckl"):
          with open ("ejemplos/contactos.pckl", "rb") as pcklfile:
               lista = pickle.load(pcklfile)
     else:
          lista = []
     while True:
          campo01 = input('campo01:-> ')
          if campo01 == '@':
               break
          campo02 = input('campo02:-> ')
          campo03 = input('campo03:-> ')
          lista.append({'campo01':campo01,'campo02':campo02,'campo03':campo03})
     with open ("ejemplos/contactos.pckl", "wb") as pcklfile:
          pickle.dump(lista, pcklfile)
except:
     print("Error...El fichero no se encuentra en el directorio")
