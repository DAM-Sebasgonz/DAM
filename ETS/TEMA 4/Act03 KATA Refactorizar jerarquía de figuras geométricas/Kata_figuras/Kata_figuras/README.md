### KATA: Refactorizar jerarquía de figuras geométricas

## Enunciado:
- Queremos modelar figuras: Rectángulo, Cuadrado y Triángulo.
- Todas las figuras tienen:
    - Un centro (Punto con coordenadas x, y)
    - Un color
- No tiene sentido crear una Figura genérica sin saber de qué tipo es,
  así que la clase Figura debe ser abstracta.
- Cada figura debe poder calcular su área y su perímetro.
- El programa principal mostrará un menú:
    1. Rectángulo
    2. Cuadrado
    3. Triángulo
    0. Salir

  Tras elegir una figura:
    - Se piden por teclado sus datos (centro, color, lados, etc.)
    - Se muestran por pantalla su perímetro y su área.

## Objetivo de la KATA:
1. Empezar con una solución *pobre*, sin clase abstracta y con bastante duplicación.
2. Ir aplicando refactorizaciones poco a poco:
    - Extraer atributos y comportamiento común a la superclase Figura.
    - Convertir Figura en clase abstracta usando abc.ABC.
    - Hacer que Cuadrado herede de Rectángulo.
    - Limpiar el código del menú para usar polimorfismo.
