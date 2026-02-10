# libros queremos saber

# isbn: str
# titul:  str
# nro_pag: entero
# autor: str
# prestado: bool True False

# metodos
# insertarLibro()
# eliminarLibro() solo si no esta prestado
# verEstadoLibro() es indicar si esta prestado o no
# PrestarLibro()
# devolverLibro()
# listaLibros() lista los libro segun las opciones
# mostarInformacionLibro()

# dos libros son iguales si sus isbn son iguales


class Libro:
    def __init__(self, isbn:str, titulo:str, nro_paginas:int, autor:str) :
        self.ISBN = isbn
        self.autor = autor
        self.titulo = titulo
        self.nro_paginas = nro_paginas
        self.prestado = False

    def verEstadoLibro(self):
       

def insertarLibro(diccionario, objeto):
 ...






if __name__ ==  "__main__":
    dicc_libros =  {} #clave = lautor
