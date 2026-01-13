import pickle

class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print ('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f"{self.titulo} {str(self.lanzamiento)}"

class Catalogo:
    peliculas = []

    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print ("El catálogo está vacío")
        else:
            for p in self.peliculas:
                print (p)

    def cargar(self):
        fichero = open('ficheros/catalogo.pckl', 'rb')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print(f"Se han cargado {str(len(self.peliculas))} películas")

    def guardar(self):
        fichero = open('ficheros/catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
    
def main():
    # Creamos un catálogo
    c = Catalogo()

    # Mostramos el contenido
    c.mostrar()

    # Agregamos unas películas
    c.agregar(Pelicula("El Padrino", 175, 1972))
    c.agregar(Pelicula("El Padrino: Parte 2" , 202, 1974))

    # Mostramos el catálogo de nuevo
    c. mostrar()

    # Borramos el catálogo de la memoria ram (persistir                                                                                                                                           el fichero)                                                                       
    del(c)

    # Creamos un catálogo
    c = Catalogo()

    # Mostramos el contenido
    c. mostrar()

    # Agregamos una película
    c.agregar(Pelicula ("Prueba", 100, 2005))

    # Mostramos el catálogo de nuevo
    c. mostrar()

if __name__ == "__main__":
    main()
    