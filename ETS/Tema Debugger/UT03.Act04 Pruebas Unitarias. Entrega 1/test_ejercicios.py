from ejercicios import num_menor_media, esta_ordenada

def test_num_menor_media_ejemplo_basico():
    assert num_menor_media([10, 20, 30, 40, 50]) == 2 #ejemplo enunciado

def test_num_menor_media_todos_iguales():
    assert num_menor_media([5, 5, 5, 5]) == 0 #Ejemplo en el que todos son iguales

def test_num_menor_media_un_elemento():
    assert num_menor_media([42]) == 0 #Ejemplo con un solo elemento, la media es el mismo número y no hay números menores

def test_num_menor_media_lista_vacia():
    assert num_menor_media([]) == 0 #Ejemplo con lista vacía, la media no está definida pero se asume que no hay números menores

def test_num_menor_media_numeros_negativos():
    assert num_menor_media([-10, -5, -3, 0, 5]) == 2 #Ejemplo con números negativos, la media es -2.6 y los números menores son -10 y -5, Tiene que dar error porque la media realmente ees -2,6

def test_num_menor_media_dos_elementos():
    assert num_menor_media([1, 9]) == 1 #Ejemplo con dos elementos, la media es 5 y el número menor es 1

def test_num_menor_media_todos_menores_excepto_uno():
    assert num_menor_media([1, 1, 1, 7]) == 3 #Ejemplo en el que todos los números son menores que la media excepto uno, la media es 2.5 y los números menores son 1, 1 y 1


def test_esta_ordenada_descendente_estricto():
    assert esta_ordenada([50, 40, 30, 20, 10]) == True #Ejemplo en el que la lista está ordenada de forma estrictamente descendente, cada elemento es menor que el anterior

def test_esta_ordenada_ascendente():
    assert esta_ordenada([10, 20, 30]) == False #Ejemplo en el que la lista está ordenada de forma ascendente, cada numero es mayor que el anterior, no cumple con la condición de estar ordenada de forma descendente

def test_esta_ordenada_elementos_iguales_consecutivos():
    assert esta_ordenada([50, 50, 30, 10]) == True #Ejemplo en el que la lista tiene elementos iguales consecutivos, la función debería considerar que sigue estando ordenada de forma descendente, ya que no hay ningún numero que sea mayor que el anterior

def test_esta_ordenada_un_elemento():
    assert esta_ordenada([7]) == True #Ejemplo con un solo elemento, la función debería considerar que una lista con un solo elemento está ordenada de forma descendente, ya que no hay ningún numero que sea mayor que el anterior

def test_esta_ordenada_lista_vacia():
    assert esta_ordenada([]) == True #Ejemplo con lista vacía, la función debería considerar que una lista vacía está ordenada de forma descendente, ya que no hay ningún numero que sea mayor que el anterior

def test_esta_ordenada_dos_elementos_descendente():
    assert esta_ordenada([10, 5]) == True #Ejemplo con dos elementos ordenados de forma descendente, la función debería considerar que la lista está ordenada de forma descendente, ya que el segundo numero es menor que el primero

def test_esta_ordenada_dos_elementos_ascendente():
    assert esta_ordenada([5, 10]) == False #Ejemplo con dos elementos ordenados de forma ascendente, la función debería considerar que la lista no está ordenada de forma descendente, ya que el segundo numero es mayor que el primero

def test_esta_ordenada_desordenado_en_medio():
    assert esta_ordenada([50, 40, 25, 30, 10]) == False #Ejemplo en el que la lista tiene un elemento desordenado en medio, la función debería considerar que la lista no está ordenada de forma descendente, ya que el numero 25 es mayor que el numero 30

def test_esta_ordenada_todos_iguales():
    assert esta_ordenada([3, 3, 3]) == True #Ejemplo en el que todos los elementos son iguales, la función debería considerar que la lista está ordenada de forma descendente, ya que no hay ningún numero que sea mayor que el anterior


