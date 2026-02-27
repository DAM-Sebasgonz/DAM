import pytest
from ejercicios import num_menor_media, esta_ordenada

def test_num_menor_media_ejemplo():
    assert num_menor_media([10, 20, 30, 40, 50]) == 2

def test_num_menor_media_iguales():
    assert num_menor_media([10, 10, 10]) == 0

def test_num_menor_media_vacia():
    assert num_menor_media([]) == 0


def test_esta_ordenada_descendente():
    assert esta_ordenada([50, 40, 30, 20, 10]) == True

def test_esta_ordenada_ascendente():
    assert esta_ordenada([10, 20, 30]) == False

def test_esta_ordenada_duplicados():
    assert esta_ordenada([30, 20, 20, 10]) == True

def test_esta_ordenada_un_elemento():
    assert esta_ordenada([100]) == True