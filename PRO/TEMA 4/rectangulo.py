class Rectangulo:
    def __init__(self,x,y,lado_a,lado_b):
        self._x = x
        self._y = y
        self._a = lado_a
        self._b = lado_b


    @property
    def _y(self):
        return self._y
    
    @_x.setter
    def _x(self, nuevo_valor):
        if nuevo_valor > 0:
            self._x = nuevo_valor
        else:
            raise ValueError("La coordenada x debe ser un valor mayor a 0")
        
     def _y(self):
        return self._y
        
    def __str__(self):
        resultado = f"x = {self._x}"
        return resultado

    def modificarCoordenada(self, nuevo_X, nuevo_y):
        self._x = nuevo_X
        self._x = nuevo_y


    def calcularPerimetro(self) -> int:
        return 2 * self._a + 2 * self._b
    
    def calcularArea(self) -> int:
        return self._a * self._b
    
    def rotIzquierda(self):
        



if __name__ == "__main__":
    valor_x  = int(input("Introduzca valor coordenada X"))
    valor_y  = int(input("Introduzca valor coordenada Y"))
    lado_a  = int(input("Introduzca valor de la base"))
    lado_b = int(input("Introduzca valor de la altura"))

    try:
        rect01 = Rectangulo(valor_x, valor_y, lado_a, lado_b)
        print(rect01)
    except ValueError as mensaje:
        print(mensaje)
    else:
        rect01.modificarCoordenada(37,-1)


    