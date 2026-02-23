# operaciones.py

def suma(a: int, b: int) -> int:
    """Devuelve la suma de a y b."""
    return a + b


def resta(a: int, b: int) -> int:
    """Devuelve la resta de a y b (a - b)."""
    return a - b


def es_par(n: int) -> bool:
    """Devuelve True si n es par, False en caso contrario."""
    return n % 2 == 0


def es_mayor_de_edad(edad: int) -> bool:
    """
    Devuelve True si la edad corresponde a una persona mayor de edad.
    Supongamos que a partir de 18 años (incluido) es mayor de edad.
    """
    return edad >= 18
