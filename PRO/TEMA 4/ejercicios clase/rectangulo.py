class Rectangulo:
    def __init__(self,puntox,puntoy,lado_a,lado_b):
        self._x = puntox
        self._y = puntoy
        self._a = lado_a
        self._b = lado_b

    # getter de x
    @property
    def _x(self):
        return self.__x
    
    @_x.setter # setter             # se define setter con 1 guión
    def _x(self, nuevo_valor):
        if nuevo_valor >= 0:
            self.__x = nuevo_valor
        else:
            raise ValueError('La coordenada x debe ser un valor >= 0')

    # getter de y
    @property
    def _y(self):
        return self.__y
    
    @_y.setter # setter             # se define setter con 1 guión
    def _y(self, nuevo_valor):
        if nuevo_valor >= 0:
            self.__y = nuevo_valor
        else:
            raise ValueError('La coordenada y debe ser un valor >= 0')

# getter de a
    @property
    def _a(self):
        return self.__a
    
    @_a.setter # setter             # se define setter con 1 guión
    def _a(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__a = nuevo_valor
        else:
            raise ValueError('La base debe ser un valor > 0')

# getter de b
    @property
    def _b(self):
        return self.__b
    
    @_b.setter # setter             # se define setter con 1 guión
    def _b(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__b = nuevo_valor
        else:
            raise ValueError('La altura debe ser un valor > 0')

    def __str__(self) -> str:
        resultado = f'x = {self.__x}\ny = {self.__y}\nbase = {self.__a}\naltura = {self.__b}'
        return resultado

    def modificarCoordenadas(self, nuevo_x, nuevo_y):
        self._x = nuevo_x
        self._y = nuevo_y
    
    def calcularPerimetro(self) -> int:
        return 2 * self._a + 2 * self._b
    
    def calcularArea(self) -> int:
        return self._a * self._b

    def rotIzquierda(self):
        self._x = self._x - self._b
        self._a, self._b = self._b, self._a

    def rotDerecha(self):
        self._x = self._x + self._a
        self._a, self._b = self._b, self._a
    
    def rotSimetrica_X(self):
        self._y = self._y - self._b
    
    def rotSimetrica_Y(self):
        self._x = self._x + self._a

if __name__ == '__main__':
    valor_x = int(input('Introduzca valor coordenada x '))
    valor_y = int(input('Introduzca valor coordenada y '))
    lado_a = int(input('Introduzca valor de la base '))
    lado_b = int(input('Introduzca valor de la altura '))
    try:
        rect01 = Rectangulo(valor_x, valor_y, lado_a, lado_b)
        print(rect01)
        # rect01.modificarCoordenadas(7,-1)
        rect01.rotIzquierda()
        print(rect01)
    except ValueError as mensaje:
        print(mensaje)

        
