import math


class Circulo:
    """
    Representa un círculo en el plano cartesiano.

    Permite crear un círculo definido por su centro y radio.

    :param cx: Coordenada X.
    :type cx: float
    :param cy: Coordenada Y.
    :type cy: float
    :param r: Radio del círculo.
    :type r: float
    """

    def __init__(self, cx: float, cy: float, r: float) -> None:
        """
        Inicializa un círculo con centro (cx, cy) y radio r.

        :param cx: Coordenada X del centro.
        :type cx: float
        :param cy: Coordenada Y del centro.
        :type cy: float
        :param r: Radio del círculo.
        :type r: float
        """
        self._centro_x = cx
        self._centro_y = cy
        self._radio = r

    def get_centro_x(self) -> float:
        """
        Devuelve la coordenada X del centro del círculo.

        :return: Coordenada X del centro.
        :rtype: float
        """
        return self._centro_x

    def get_centro_y(self) -> float:
        """
        Devuelve la coordenada Y del centro del círculo.

        :return: Coordenada Y del centro.
        :rtype: float
        """
        return self._centro_y

    def get_radio(self) -> float:
        """
        Devuelve el radio del círculo.

        :return: Radio del círculo.
        :rtype: float
        """
        return self._radio

    def get_circunferencia(self) -> float:
        """
        Calcula y devuelve la longitud de la circunferencia del círculo.
        
        la formula para calcular la circunferencia es: C = 2 * π * r

        :return: Longitud de la circunferencia.
        :rtype: float
        """
        return 2 * math.pi * self._radio

    def mueve(self, delta_x: float, delta_y: float) -> None:
        """
        Desplaza el centro del círculo sumando los deltas indicados.

        El radio no se ve afectado por esta operación.

        :param delta_x: Desplazamiento en el eje X. 
        :type delta_x: float
        :param delta_y: Desplazamiento en el eje Y.
        :type delta_y: float

        """
        self._centro_x += delta_x
        self._centro_y += delta_y

    def escala(self, s: float) -> None:
        """
        Escala el radio del círculo multiplicándolo por la s.

        :param s: Factor de escala. Un valor mayor que 1 agranda el círculo;
        entre 0 y 1 lo reduce. No puede ser negativo.
        :type s: float


        """
        self._radio *= s
        
        
class Rectangulo:
    """
    Representa un rectángulo plano.
    
    Clase añadida como parte de la documentación.
    """
    def __init__(self, base: float, altura: float) -> None:
        """
        Constructor del rectángulo.
        
        :param base: Longitud de la base.
        :type base: float
        :param altura: Longitud de la altura.
        :type altura: float
        """
        self._base = base
        self._altura = altura

    def get_area(self) -> float:
        """
        Calcula el área del rectángulo.
        
        :returns: Área calculada multiplicando la base por la altura.
        :rtype: float
        """
        return self._base * self._altura