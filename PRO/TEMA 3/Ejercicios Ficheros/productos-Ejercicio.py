import csv
import json

def leerCSV_1():

    lista = []

    with open ("C:/DAM/PRO/TEMA 3/Ejercicios Ficheros/productos.csv", "r", newline="\n") as csv1file:
        lec = csv.reader(csv1file, delimiter=";")

        for tupla in lec:
            lista.append(tupla)

    return lista


def leerCSVsinEncabezado():

    lista_datos = []
    
    with open ("C:/DAM/PRO/TEMA 3/Ejercicios Ficheros/productos2.csv", "r", newline="\n") as csv2file:
        reader = csv.DictReader(csv2file, delimiter=",")

        for fila in reader:
            lista_datos.append(fila)
    return lista_datos

def generar_inventario(datosA, datosB):

    datos_json = []

    for lista in datosA:

        dicc_json = {"codigo":lista[0], "producto":lista[1], "precio": lista[2], "cantidad": lista[3]}
        producto = lista[1]
        for diccionario in datosB:
            if producto == diccionario["productos"]:
                dicc_json["cantidad"] += diccionario["cantidad"]
                dicc_json["precio"] = max(dicc_json["precio"], diccionario["precio"])
                break
            datos_json.append(dicc_json)



if __name__ == "__main__":
    datos_A = leerCSV_1()
    datos_B = leerCSVsinEncabezado()
    



# campos = ["cod","producto","precio","cantidad"]
