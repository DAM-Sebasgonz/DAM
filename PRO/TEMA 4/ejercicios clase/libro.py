# libros queremos saber

# ISBN : str
# titulo: str
# nro_pag: entero
# autor: str
# prestado : booleano

# métodos

# verEstadoLibro() es indicar si está prestado o no
# prestarLibro()
# devolverLibro()
# listarLibros() lista los libros según opciones
# mostrarInformacionLibro()

# dos libros son iguales si sus ISBN son iguales

# Se quiere guardar los libros según su autor

# funciones del programa

# insertarLibro()
# eliminarLibro() sólo si no está prestado

class Libro:
    def __init__(self, isbn:str, titulo:str, nro_paginas:int, autor:str):
        self.ISBN = isbn
        self.autor = autor
        self.titulo = titulo
        self.nro_paginas = nro_paginas
        self.prestado = False

    def verEstadoLibro(self):
        return self.prestado
    
    def cambiarEstado(self):
        self.prestado = not self.prestado

    def verISBN(self):
        return self.ISBN

    def prestarLibro(self) -> bool:
        prestado = False
        if not self.verEstadoLibro():
            self.cambiarEstado()
            prestado = True
        return prestado

    def devolverLibro(self):
       self.cambiarEstado()

def insertarLibro(diccionario, objeto):
    diccionario.setdefault(objeto.autor, []) 
    diccionario[objeto.autor].append(objeto)

def buscarLibro(diccionario, isbn) -> bool:
    for libro in diccionario:
        if libro.verISBN() == isbn:
            return True
            break
    else:
        return False
    
if __name__ == '__main__':
    dicc_libros = {} # clave = autor, valor = lista objetos
    
    while True:
        print('''\n1. Agregar Libro\n2. EliminarLibro\n3. Realizar préstamo\n4. Realizar devolución\n5. Listar libros\n9. Salir''')
        opc = int(input('\nIndique opción: '))
        match opc:
            case 1:
                isbn = input('Indique ISBN -> ')

                if not buscarLibro(dicc_libros, isbn):
                    autor = input('Indique autor -> ')
                    titulo = input('Indique titulo -> ')
                    nro_pag = int(input('Indique el número de páginas -> '))
                    objeto = Libro(isbn, titulo, nro_pag,autor)
                    insertarLibro(dicc_libros, objeto)
                else:
                    print('Error...el libro ya está registrado')
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 9:
                print('\nFin de ejecución ...')
                break
            case _:
                print('Error...Opción inválida')
