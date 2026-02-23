# class Circulo:
#     def __init__(self, valor_radio):
#         self._radio = valor_radio       # se define el atributo con 1 guión

#     @property  # getter
#     def _radio(self):                   # se define la propiedad con 1 guión
#         print("pasando por el getter")
#         return self.__radio             # el return con 2 guiones para proteger
    
#     @_radio.setter # setter             # se define setter con 1 guión
#     def _radio(self, nuevo_valor):
#         print("Paso por el setter")
#         if nuevo_valor > 0:
#             self.__radio = nuevo_valor  # se asigna al atributo con 2 guiones
#         else:
#             print('El radio debe tener un valor > 0')

#     @_radio.deleter
#     def _radio(self):                   # se define el deleter con 1 guión
#         print("pasando por el deleter")
#         del self.__radio                # se borra el atriburo con 2 guiones

#     def obtenerRadio(self):
#         return self._radio
    
#     def actualizarRadio(self, nuevo_radio):
#         self._radio = nuevo_radio
    
#     def __str__(self) -> str:
#         return str(self._radio)

# if __name__ == '__main__':

# # funcionamiento sin errores

#     # al crear objeto se pasa por setter
#     circulo01 = Circulo(5)      
#     print('---')
    
#     # al leer su valor se pasa por el getter
#     print(circulo01)

#     # al modificar su valor por un valor correcto
#     circulo01.actualizarRadio(8)
#     print('---')
#     print(circulo01)

#     # al modificar su valor por un valor incorrecto (no cambia su valor)
#     circulo01.actualizarRadio(-7)
#     print('---')
#     print(circulo01)

# # funcionamiento con errores

#     # se pide crear un objeto con un valor no valido
#     circulo02 = Circulo(0)
#     # verificamos que el objeto se crea
#     print(id(circulo02))
#     # escribimos el contenido del objeto
#     print(circulo02)
#     # nos damos cuenta que el objeto se ha creado
#     # pero no se ha definido su atributo
#     # por eso el error de ejecución

# # Primera forma de resolver este problema

# # 1. asignar un valor por defecto al atributo
    
#     # el código completo queda como sigue

# class Circulo:
#     def __init__(self, valor_radio):
#         self._radio = valor_radio       # se define el atributo con 1 guión

#     @property  # getter
#     def _radio(self):                   # se define la propiedad con 1 guión
#         print("pasando por el getter")
#         return self.__radio             # el return con 2 guiones para proteger
    
#     @_radio.setter # setter             # se define setter con 1 guión
#     def _radio(self, nuevo_valor):
#         print("Paso por el setter")
#         if nuevo_valor > 0:
#             self.__radio = nuevo_valor  # se asigna al atributo con 2 guiones
#         else:
#             print('El radio debe tener un valor > 0')
#             self.__radio = None # o algún valor fuera del dominio

#     @_radio.deleter
#     def _radio(self):                   # se define el deleter con 1 guión
#         print("pasando por el deleter")
#         del self.__radio                # se borra el atriburo con 2 guiones

#     def obtenerRadio(self):
#         return self._radio
    
#     def actualizarRadio(self, nuevo_radio):
#         self._radio = nuevo_radio
    
#     def __str__(self) -> str:
#         return str(self._radio)

# if __name__ == '__main__':

    # # se pide crear un objeto con un valor no valido
    # circulo03 = Circulo(0)
    # # verificamos que el objeto se crea
    # print(id(circulo03))
    # # escribimos el contenido del objeto
    # print(circulo03)
    # # ahora no se produce el error
    # # pero ¿que sentido tiene tener un objeto sin unvalor válido?

    # # la mejora en este caso pasa por borrar el objeto creado
    # del circulo03
    # # ahora al intentar imprimir no se encuentra el objeto
    # # print(id(circulo03)) 

    # # entonces la forma correcta de crear un objeto sería

    # circulo04 = Circulo(9)
    # if circulo04.obtenerRadio() == None:
    #     # borramos el objeto
    #     del circulo04
    #     ...
    # else:
    #     print(circulo04)
    #     ...

    # # que con un valor incorrecto del radio

    # circulo05 = Circulo(-9)
    # if circulo05.obtenerRadio() == None:
    #     # borramos el objeto
    #     del circulo05
    #     print('se ha borrado el objeto')
    #     ...
    # else:
    #     print(circulo05)

# # Segunda forma de resolver este problema

# # 2. usar try-except
    
#     # el código completo queda como sigue

class Circulo:
    def __init__(self, valor_radio):
        self._radio = valor_radio       # se define el atributo con 1 guión

    @property  # getter
    def _radio(self):                   # se define la propiedad con 1 guión
        print("pasando por el getter")
        return self.__radio             # el return con 2 guiones para proteger
    
    @_radio.setter # setter             # se define setter con 1 guión
    def _radio(self, nuevo_valor):
        print("Paso por el setter")

        if nuevo_valor > 0:
        # if isinstance(nuevo_valor,int) and nuevo_valor > 0:
            self.__radio = nuevo_valor      # se asigna al atributo con 2 guiones
        else:
            # se genera una señal
            raise ValueError('El radio debe ser un valor > 0')
            # raise NameError('El radio debe ser un valor > 0')

    @_radio.deleter
    def _radio(self):                   # se define el deleter con 1 guión
        print("pasando por el deleter")
        del self.__radio                # se borra el atriburo con 2 guiones

    def obtenerRadio(self):
        return self._radio
    
    def actualizarRadio(self, nuevo_radio):
        self._radio = nuevo_radio
    
    def __str__(self) -> str:
        return str(self._radio)

if __name__ == '__main__':

# # la creación del objeto se pone dentro del try

# # con un valor correcto del radio
   
    # try:
    #     circulo01 = Circulo(3)
    #     print(circulo01)
    # except ValueError as msg_error:
    #     print(msg_error)
    #     ...
    #     print(id(circulo01))
    #     print(circulo01)

# # con un valor no correcto del radio

    # try:
    #     circulo01 = Circulo(-2)
    #     print(circulo01)
    # except ValueError as msg_error:
    #     print(msg_error)
    #     # se muestra error porque el objeto no se crea
    #     # print(id(circulo01))
    #     # print(circulo01)