import datetime

"""
Programa diseñado para la administración de catálogos de películas.
Version 1.0.
"""

class RecursoCinematografico:
    """
    Clase base para representar un recurso cinematográficod de manera general.

    :param identificador: Código único del recurso.
    :type identificador: str
    :param fecha_registro: Fecha en la que se dio de alta el recurso.
    :type fecha_registro: datetime.date
    """
    def __init__(self, identificador, fecha_registro):
        self.identificador = identificador
        self.fecha_registro = fecha_registro

class Pelicula(RecursoCinematografico):
    """
    Clase que representa una película, heredando de RecursoCinematografico.

    Atributos heredados:
        identificador (str): ID del recurso.
        fecha_registro (datetime.date): Fecha de registro automática.

    :param identificador: Código único de la película.
    :type identificador: str
    :param titulo: Nombre de la obra.
    :type titulo: str
    :param duracion: Tiempo de duración en minutos.
    :type duracion: int
    :param genero: Categoría cinematográfica.
    :type genero: str
    :param presupuesto: Valor monetario asignado a la producción.
    :type presupuesto: float
    """

    def __init__(self, identificador, titulo, duracion, genero, presupuesto):
        super().__init__(identificador, datetime.date.today())
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.presupuesto = presupuesto

    def calcular_impuestos(self, tasa=0.21):
        """Calcula los impuestos basados en el presupuesto de la película.

        Args:
            tasa (float): Porcentaje de impuesto a aplicar (por defecto 0.21).

        Returns:
            float: El monto total de impuestos calculado.

        Raises:
            ValueError: Si el presupuesto de la película es un valor negativo.
        """
        if self.presupuesto < 0:
            raise ValueError("El presupuesto no puede ser negativo")
        return self.presupuesto * tasa

    def es_apta_para_maraton(self):
        """Determina si la película es breve para un maratón."""
        return self.duracion < 90

class GestorBiblioteca:
    """
    Administrador del catálogo de películas.

    :ivar catalogo: Lista que contiene los objetos de tipo Pelicula.
    :vartype catalogo: list[Pelicula]
    """
    def __init__(self):
        self.catalogo = []

    def agregar_pelicula(self, pelicula):
        """Añade una nueva película al catálogo."""
        if isinstance(pelicula, Pelicula):
            self.catalogo.append(pelicula)
            return True
        return False

    def obtener_estatisticas(self):
        """Calcula métricas financieras del catálogo completo.

        Returns:
            tuple: Un conjunto de valores financieros:
            total_presupuesto (float): Suma de todos los presupuestos.
            promedio (float): Media de presupuesto por película.
        """
        if not self.catalogo:
            return 0, 0
        total_presupuesto = sum(p.presupuesto for p in self.catalogo)
        promedio = total_presupuesto / len(self.catalogo)
        return total_presupuesto, promedio

def buscar_por_genero(gestor, genero):
    """Filtra los títulos de las películas según su género.

    Args:
        gestor (GestorBiblioteca): Instancia del gestor que contiene el catálogo.
        genero (str): Nombre del género a filtrar.

    Returns:
        list[str]: Lista con los títulos de las películas encontradas.
    """
    return [p.titulo for p in gestor.catalogo if p.genero.lower() == genero.lower()]