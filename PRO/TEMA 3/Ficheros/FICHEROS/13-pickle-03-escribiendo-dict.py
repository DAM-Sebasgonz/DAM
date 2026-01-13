# escribir y leer diccionario en fichero binario
import pickle
students = {
  'Student 1': {
        'Name': "Alice", 'Age' :10, 'Grade':4,
    },
    'Student 2': {
        'Name':'Bob', 'Age':11, 'Grade':5
    },
    'Student 3': {
        'Name':'Elena', 'Age':14, 'Grade':8
    }
}

# serializa el diccionario

with open("files/dict.pkl", "wb") as f:
    pickle.dump(students, f)
   
# deserializa el diccionario y muestra por pantalla

with open("files/dict.pkl", "rb") as f:
    dict_deserializado = pickle.load(f)
    print(dict_deserializado)