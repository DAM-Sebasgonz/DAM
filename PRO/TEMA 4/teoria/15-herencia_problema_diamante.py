# ejemplo del diamante sin el uso del super()

class Base:
    def saludar(self) -> str:
        return "Hola desde Base"

class Izquierda(Base):
    def saludar(self) -> str:
        return "Hola desde Izquierda"

class Derecha(Base):
    def saludar(self) -> str:
        return "Hola desde Derecha"

class Final(Izquierda, Derecha):
    pass

print(Final.__mro__)
print()
print(Final().saludar())  