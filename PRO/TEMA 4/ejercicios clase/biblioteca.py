# biblioteca de libros y revistas

class Recurso:
    def __init__(self, titulo_nombre, editorial, identificador, fecha_publicacion):
        self.id = identificador
        self.titulo = titulo_nombre      # nombre revista
        self.editorial = editorial
        self.fecha_publicacion  = fecha_publicacion

    def prestarRecurso(self):
        print('Prestando un libro')

class Revista(Recurso):
    ...

class Libro(Recurso):
    ...

if __name__ == '__main__':
    revista01 = Revista('Hola', 'Editorial Omega','125','01/02/2026')

    revista01.prestarRecurso()