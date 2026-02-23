# PI = 3.1416

# class Circulo:
#     def __init__(self, valor_radio):
#         self._radio = valor_radio
    
#     @property
#     def _radio(self):
#         return self.__radio
    
#     @_radio.setter
#     def _radio(self, nuevo_valor):
#         if nuevo_valor > 0:
#             self.__radio = nuevo_valor
#         else:
#             print("El radio debe tener un valor > 0")
    
#     @_radio.deleter
#     def _radio (self):
#         print("Entrando en el deleter")
#         del self.__radio
    
#     def obtenerRadio(self):
#         return self.__radio
 
#     def actualizarRadio(self, nuevo_radio):
#         self.__radio = nuevo_radio
    
#     def __str__(self) -> str:
#         return f'El radio del círculo es: {self.__radio}'
    
#     # # manera 1 de definir el diámetro 

#     # # DEFINIR UN MÉTODO

#     def obtenerDiametro(self) -> float:
#         return 2.0 * self.__radio
    
#     def obtenerPerimetro(self) -> float:
#         return PI * self.obtenerDiametro()

# if __name__ == '__main__':
#     circulo01 = Circulo(3)      
#     print(circulo01)
#     print(f'El diámetro del círculo es {circulo01.obtenerDiametro()}')
#     print(f'El perímetro del círculo es {circulo01.obtenerPerimetro()}')


# Otra forma de definir el diámetro

PI = 3.1416

class Circulo:
    def __init__(self, valor_radio):
        self._radio = valor_radio
    
    @property
    def _radio(self):
        return self.__radio
    
    @_radio.setter
    def _radio(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__radio = nuevo_valor
        else:
            print("El radio debe tener un valor > 0")
    
    @_radio.deleter
    def _radio (self):
        print("Entrando en el deleter")
        del self.__radio
    
    def obtenerRadio(self):
        return self.__radio
 
    def actualizarRadio(self, nuevo_radio):
        self.__radio = nuevo_radio
    
#     # # manera 2 de definir el diámetro 

#     # # DEFINIR UNA PROPIEDAD (@property)

    @property                       # de esta forma se puede definir un atributo
    def diametro(self):             # que se puede invocar desde el principal
        return self.__radio * 2.0
    
    def obtenerDiametro(self):      #  para evitarlo se crea un método como antes
        return self.diametro      
                                  
    def obtenerPerimetro(self) -> float:
        return self.obtenerDiametro() * PI

if __name__ == '__main__':
    circulo01 = Circulo(3)      
    
    print(circulo01)
    print(f'El diámetro del círculo es {circulo01.diametro}')    # se puede usar desde aquí
    print(circulo01.obtenerDiametro())                     # mediante el método se oculta la propiedad
    print(f'El diámetro del círculo es {circulo01.obtenerDiametro()}')
    print(f'El perímetro del círculo es {circulo01.obtenerPerimetro()}')

