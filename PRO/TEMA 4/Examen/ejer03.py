class Cancion:
    """Clase general """

    def __init__(self, titulo: str, artista: str, duracion: int, genero: str):
        """Inicializa una cancion con todos sus atributos."""
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.genero = genero

    def __str__(self) -> str:
        """Devuelve una representacion amigable de la cancion en formato 'Titulo - Artista (MM:SS)'."""
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{self.titulo} - {self.artista} ({minutos:}:{segundos:})"

    def __eq__(self, otra) -> bool:
        """Comprueba si dos canciones son iguales por titulo y artista."""
        if not isinstance(otra, Cancion):
            return False
        return self.titulo == otra.titulo and self.artista == otra.artista

    def __lt__(self, otra) -> bool:
        """Comprueba si la cancion es menor que otra en base a su duracion."""
        return self.duracion < otra.duracion

    def __len__(self) -> int:
        """Devuelve la duracion de la cancion en segundos."""
        return self.duracion

    def __add__(self, otro) -> int:
        """Suma la duracion de esta cancion con otra cancion o con un entero. """
        if isinstance(otro, Cancion):
            return self.duracion + otro.duracion
        elif isinstance(otro, int):
            return self.duracion + otro
        raise TypeError(f"No se puede sumar Cancion con {type(otro)}")

    def __radd__(self, otro) -> int:
        """Permite sumar un entero con una cancion (orden invertido)."""
        if isinstance(otro, int):
            return self.duracion + otro
        raise TypeError(f"No se puede sumar {type(otro)} con Cancion")


class Playlist:
    """Representa una lista de reproduccion de canciones. Implementa metodos magicos para acceso, modificacion y operaciones entre playlists."""

    def __init__(self, nombre: str, canciones: list = None):
        """Inicializa la playlist con un nombre y una lista opcional de canciones."""
        self.nombre = nombre
        self.canciones = canciones if canciones is not None else []

    def __str__(self) -> str:
        """Devuelve una representacion legible de la playlist con nombre y numero de canciones.
        """
        return f"Playlist: {self.nombre} ({len(self.canciones)} canciones)"

    def __len__(self) -> int:
        """Devuelve el numero de canciones en la playlist."""
        return len(self.canciones)

    def __getitem__(self, indice):
        """Permite acceder a canciones por indice. """
        return self.canciones[indice]

    def __setitem__(self, indice: int, cancion):
        """Permite modificar una cancion en una posicion especifica. """
        self.canciones[indice] = cancion

    def __delitem__(self, indice: int):
        """Permite eliminar una cancion por su indice."""
        del self.canciones[indice]

    def __contains__(self, cancion) -> bool:
        """Comprobar si una cancion esta en la playlist. """
        return cancion in self.canciones

    def __add__(self, otra) -> "Playlist":
        """Concatena dos playlists y devuelve una nueva playlist con las canciones de ambas."""
        nombre_nuevo = f"{self.nombre} + {otra.nombre}"
        canciones_nuevas = self.canciones + otra.canciones
        return Playlist(nombre_nuevo, canciones_nuevas)

    def __iadd__(self, otro) -> "Playlist":
        """Permite usar += para añadir canciones a la playlist. Puede recibir una Playlist o una Cancion suelta"""
        if isinstance(otro, Playlist):
            self.canciones += otro.canciones
        elif isinstance(otro, Cancion):
            self.canciones.append(otro)
        else:
            raise TypeError(f"No se puede aniadir {type(otro)} a la playlist")
        return self


def ordenar_canciones(canciones: list) -> list:
    """Ordenamos una lista de canciones por duracion de menor a mayor usando bubble sort"""
    lista = canciones[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == "__main__":

    cancion1 = Cancion("Bohemian Rhapsody", "Queen", 354, "Rock")
    cancion2 = Cancion("Imagine", "John Lennon", 183, "Pop")
    cancion3 = Cancion("Thriller", "Michael Jackson", 357, "Pop")
    cancion4 = Cancion("Stairway to Heaven", "Led Zeppelin", 482, "Rock")
    cancion5 = Cancion("Bohemian Rhapsody", "Queen", 600, "Remix")
    cancion6 = Cancion("Billie Jean", "Michael Jackson", 294, "Pop")

    playlist1 = Playlist("Rock Clasico", [cancion1, cancion4])
    playlist2 = Playlist("Pop Hits", [cancion2, cancion3, cancion6])

    print("--- __str__ de canciones ---")
    print(cancion1)
    print(cancion2)
    print(cancion4)

    print("\nComparacion de canciones ---")
    print(f"cancion1 == cancion5 (mismo titulo/artista, distinta duracion): {cancion1 == cancion5}")
    print(f"cancion1 == cancion2: {cancion1 == cancion2}")

    print("\nOrdenacion por duracion (bubble sort) ---")
    todas = [cancion1, cancion2, cancion3, cancion4, cancion5, cancion6]
    ordenadas = ordenar_canciones(todas)
    for c in ordenadas:
        print(f"  {c} ({len(c)} segundos)")

    print("\nDuracion de canciones y numero de canciones en playlists ---")
    print(f"Duracion de cancion1: {len(cancion1)} segundos")
    print(f"Canciones en playlist1: {len(playlist1)}")
    print(f"Canciones en playlist2: {len(playlist2)}")

    print("\nSuma de duraciones ---")
    total = cancion1 + cancion2
    print(f"Duracion de cancion1 + cancion2: {total} segundos")
    total_con_int = cancion1 + 60
    print(f"Duracion de cancion1 + 60 segundos: {total_con_int} segundos")

    print("\nConcatenar dos playlists ---")
    playlist3 = playlist1 + playlist2
    print(playlist3)
    for c in playlist3:
        print(f"  {c}")

    print("\nAcceso por indice y slice ---")
    print(f"Primera cancion de playlist1: {playlist1[0]}")
    print(f"Slice playlist2[1:]: {[str(c) for c in playlist2[1:]]}")

    print("\nModificar cancion en posicion ---")
    print(f"Antes: {playlist1[1]}")
    playlist1[1] = cancion3
    print(f"Despues de playlist1[1] = cancion3: {playlist1[1]}")

    print("\nEliminar cancion ---")
    print(f"Antes de eliminar: {playlist1}")
    del playlist1[0]
    print(f"Despues de del playlist1[0]: {playlist1}")
    for c in playlist1:
        print(f"  {c}")

    print("\nComprobar pertenencia con 'in' ---")
    print(f"cancion2 en playlist2: {cancion2 in playlist2}")
    print(f"cancion4 en playlist2: {cancion4 in playlist2}")

    print("\nUsar += para aniadir contenido ---")
    playlist1 += cancion4
    print(f"Despues de playlist1 += cancion4: {playlist1}")
    playlist1 += playlist2
    print(f"Despues de playlist1 += playlist2: {playlist1}")
    for c in playlist1:
        print(f"  {c}")
