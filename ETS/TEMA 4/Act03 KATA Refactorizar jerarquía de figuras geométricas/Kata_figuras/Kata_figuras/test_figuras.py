# test_figuras.py
import math

import pytest

from figuras import (
    Punto,
    Rectangulo,
    Cuadrado,
    Triangulo,
)


def test_punto_str():
    p = Punto(1.5, -2.0)
    assert str(p) == "(1.5, -2.0)"


def test_rectangulo_area_y_perimetro():
    centro = Punto(0, 0)
    rect = Rectangulo(centro, "rojo", base=4, altura=3)
    assert rect.area() == 12
    assert rect.perimetro() == 14
    assert "Rectángulo" in str(rect)
    assert "centro=(0, 0)" in str(rect)


def test_cuadrado_es_rectangulo():
    centro = Punto(1, 1)
    cuad = Cuadrado(centro, "azul", lado=5)

    # Hereda de Rectangulo, así que base y altura son 5
    assert isinstance(cuad, Rectangulo)
    assert cuad.base == 5
    assert cuad.altura == 5

    # Área y perímetro del cuadrado
    assert cuad.area() == 25
    assert cuad.perimetro() == 20
    assert "Cuadrado" in str(cuad)


@pytest.mark.parametrize(
    "base,altura,lado2,lado3,area_esperada,perimetro_esperado",
    [
        (6, 4, 5, 5, 12, 16),   # base=6, altura=4
        (10, 2, 3, 4, 10, 17),  # base=10, altura=2
    ],
)
def test_triangulo_area_y_perimetro(
    base, altura, lado2, lado3, area_esperada, perimetro_esperado
):
    centro = Punto(-1, 0)
    tri = Triangulo(centro, "verde", base, altura, lado2, lado3)

    assert tri.area() == area_esperada
    assert tri.perimetro() == perimetro_esperado
    assert "Triángulo" in str(tri)


def test_polimorfismo_lista_figuras():
    centro = Punto(0, 0)
    figuras = [
        Rectangulo(centro, "rojo", 2, 3),
        Cuadrado(centro, "azul", 4),
        Triangulo(centro, "verde", 6, 2, 3, 4),
    ]

    areas = [f.area() for f in figuras]
    perimetros = [f.perimetro() for f in figuras]

    # Comprobamos que todas tienen métodos area y perimetro coherentes
    assert areas == [6, 16, 6]
    assert perimetros == [10, 16, 13]

    # Además, que el __str__ de cada una contiene su nombre
    textos = [str(f) for f in figuras]
    assert any("Rectángulo" in t for t in textos)
    assert any("Cuadrado" in t for t in textos)
    assert any("Triángulo" in t for t in textos)