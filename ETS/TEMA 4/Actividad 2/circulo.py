import math

class Circulo:
    """Clase que representa un circulo en el plano cartesiano."""
    def __init__(self, cx: float, cy: float, r: float) -> None:
        """Inicializa un nuevo circulo con centro en cordenadas (cx, cy) y radio r."""
        self._centro_x = cx
        self._centro_y = cy
        self._radio = r

    def get_centro_x(self) -> float:
        """Devuelve la coordenada x del centro del circulo."""
        return self._centro_x

    def get_centro_y(self) -> float:
        """Devuelve la coordenada y del centro del circulo."""
        return self._centro_y

    def get_radio(self) -> float:
        """Devuelve el radio del circulo."""
        return self._radio

    def get_circunferencia(self) -> float:
        """Devuelve la circunferencia del circulo."""
        return 2 * math.pi * self._radio

    def mueve(self, delta_x: float, delta_y: float) -> None:
        """Mueve el circulo sumando delta_x a la coordenada x del centro y delta_y a la coordenada y del centro."""
        self._centro_x += delta_x
        self._centro_y += delta_y

    def escala(self, s: float) -> None:
        """Escala el circulo multiplicando el radio por s."""
        self._radio *= s