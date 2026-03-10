import pytest
from primos import es_primo

@pytest.mark.parametrize("numero, valor" , [
    # (2,3,5,7,11,13) #casos retorna True
    # (4,6,8,9,10) # casos retorna False
    # (0,1,-5) #casos especiales

#------------------------------- Casos PRIMOS retorna True
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
#------------------------------ Casos NO PRIMOS retorna False 
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
#------------------------------- Casos especiales deben retornar False
    (0, False),
    (1, False),
    (-5, False),

], ids= ["primo","primo","primo","primo","primo","primo","no_primo","no_primo","no_primo","no_primo","no_primo","cero", "uno", "negativo"])



def test_es_primos(numero, valor):
    assert es_primo(numero) == valor