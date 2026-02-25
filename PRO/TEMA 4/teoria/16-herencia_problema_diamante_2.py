# ejemplo del diamante con el uso del super()

class Base:
    def __init__(self):
        print("Inicializando Base")

class Izquierda(Base):
    def __init__(self):
        print("Inicializando Izquierda")
        super().__init__()

class Derecha(Base):
    def __init__(self):
        print("Inicializando Derecha")
        super().__init__()

class Final(Izquierda, Derecha):
    def __init__(self):
        print("Inicializando Final")
        super().__init__()

# Creamos una instancia
f = Final()
print()
print(Final.__mro__)