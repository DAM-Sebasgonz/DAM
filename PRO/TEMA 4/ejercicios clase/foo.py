class Foo():
    _atributo_clase_privado = 0
    __atributo_clase_protegido = 0

    def __init__(self, x : int):
        self.x  = x
        self._x = 2 * x
        self.__x = 3 * x
    
    def obtener_x(self):
        return self._x

    def obtener__atributo_clase(self):
        return Foo.__atributo_clase_protegido
    
    def obtener__x(self):
        return self.__x

if __name__ == '__main__':
    objeto = Foo(2)

    print(objeto.x)
    print(objeto.obtener_x()) # print(objeto._x)
    print(objeto.obtener__x()) # print(objeto.__x)

    print(objeto.obtener__atributo_clase())