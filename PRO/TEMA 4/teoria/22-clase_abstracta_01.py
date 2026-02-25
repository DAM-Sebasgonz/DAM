# Las clases abstractas en Python se definen usando el módulo abc (Abstract Base Class).
# Sirven como plantillas para obligar a las subclases a implementar ciertos métodos, 
# asegurando que todas sigan una estructura común.

from abc import ABC, abstractmethod

# # Definimos una clase abstracta
class Animal(ABC):
    
    @abstractmethod
    def hacer_sonido(self):
        """Método abstracto que obliga a las subclases a implementarlo"""
        pass

# # Subclase concreta: Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"

# # Subclase concreta: Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau Miau"

# # Crear instancias
perro = Perro()
gato = Gato()

# # Usar los métodos implementados
print(perro.hacer_sonido())  # Salida: Guau Guau
print(gato.hacer_sonido())   # Salida: Miau Miau
