class Casa:

    lista_tipos = ['casa', 'adosado', 'piso', 'terreno']

    def __init__(self, valor_direccion : str, valor_superficie:float, valor_tipo:str, valor_m2:float):
        self.direccion = valor_direccion
        self._tipo = valor_tipo
        self._superficie = valor_superficie
        self._precio_m2 = valor_m2
    
    # validar _tipo

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, nuevo_tipo):
        if nuevo_tipo in Casa.lista_tipos:
            self.__tipo = nuevo_tipo
        else:
            raise ValueError('\nError... el tipo no está permitido')

    # validar _superficie

    @property
    def _superficie(self):
        return self.__superficie
    
    @_superficie.setter
    def _superficie(self, nueva_superficie):
        if nueva_superficie > 0.0:
            self.__superficie = nueva_superficie
        else:
            raise ValueError('\nError... el valor de la superficie debe ser > 0.0')

    # validar _precio_m2

    @property
    def _precio_m2(self):
        return self.__precio_m2

    @_precio_m2.setter
    def _precio_m2(self, nuevo_precio):
        if nuevo_precio > 0.0:
            self.__precio_m2 = nuevo_precio
        else:
            raise ValueError('\nError... el valor de la superficie debe ser > 0.0')

    # atributo de solo lectura

    @property
    def valor(self):
        return self._superficie * self._precio_m2

    # no se define el setter

    def __str__(self) -> str:
        return f'''\nDireccion = {self.direccion}\n\
Tipo = {self._tipo}\n\
Superficie = {self._superficie}\n\
Precio del m2 = {self._precio_m2}\n\
Valor = {self.valor}\n'''

if __name__ == '__main__':

    casa01 = Casa('Los Realejos', 90.00, 'casa', 4500.00)
    print(casa01)

    # intentamos modificar el atributo valor
    # casa01.valor = 500000.00   # property of object has no setter

    try:
        casa01.valor = 500000.00
    except AttributeError:
        print('Error... el atributo valor es de solo lectura')


 # ejemplo de atributo sólo lectura

# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
#
#  # no se define el setter