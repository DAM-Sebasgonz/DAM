class Person:
    
    # constructor
    def __init__(self, name):  
        self._name = name         # atributos protegidos con _ (1 guión)

    # getter
    @property
    def _name(self): # name = property(name)    # se define la propiedad con __ (2 guiones)
        print('fetch...')
        return self.__name

    # setter
    @_name.setter
    def _name(self, value): # name = name.setter(name)
        print('change...')
        self.__name = value
    
    # deleter
    @_name.deleter
    def _name(self): # name = name.deleter(name)
        print('remove...')
        del self.__name

    # métodos 
    def __str__(self) -> str:       # en todos los métodos se debe usar la propiedad
        return self.__name

    def cambiarNombre(self, nombre):
        print("Entra en cambiar nombre")
        self.__name = nombre
        print("Sale de cambiar nombre")
    
    def duplicaNombre(self):
        return self.__name * 2
        
#-----

if __name__ == '__main__':
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob)
    print('-'*20)
    bob.cambiarNombre('Reinaldo') # Runs name setter (name 2)
    print(bob)
    del bob._name # Runs name deleter (name 3)
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.duplicaNombre())
    sue.cambiarNombre('Alberto')
    print(sue)