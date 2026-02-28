# Version pytest: test_operaciones_pytest.py
# test_operaciones_pytest.py
# Para ejecutar: pytest

from operaciones import suma, resta, es_par, es_mayor_de_edad


def test_suma_positivos():
    assert suma(2, 3) == 5


def test_resta_positivos():
    assert resta(5, 2) == 3


def test_es_par_para_numero_par():
    assert es_par(4) is True


def test_es_par_para_numero_impar():
    assert es_par(5) is False


def test_es_mayor_de_edad_para_20():
    assert es_mayor_de_edad(20) is True


def test_es_mayor_de_edad_para_15():
    assert es_mayor_de_edad(15) is False

# <- Añadir tu test de valores límite de 18 años

