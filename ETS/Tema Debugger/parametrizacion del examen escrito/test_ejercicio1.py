import pytest
from ejercicio1 import Perfecto

@pytest.mark.parametrize("num, esperado",[
    (6,True)
    (1, False),
    (3, False),
    (8, False),
], ids = [""]