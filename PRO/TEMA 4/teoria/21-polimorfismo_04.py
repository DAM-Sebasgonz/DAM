class Animal():
    def hacer_sonido(self) -> str:
        return 'nothing'

class Perro(Animal):
    def hacer_sonido(self) -> str:
        return "Guau 🐶"

class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "Miau 🐱"

class Vaca():
    def hacer_sonido(self) -> str:
        return "Muuu 🐮"

# Función que demuestra polimorfismo
def escuchar_animal(animal:Animal):
    print(animal.hacer_sonido())

# Programa principal
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    escuchar_animal(animal)