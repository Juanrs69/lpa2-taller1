import pytest
from src.models.concretos.armario import Armario


@pytest.fixture
def armario():
    return Armario("Ropero", "Madera", "Natural", 250, num_puertas=3, num_cajones=1)


def test_atributos_armario(armario):
    assert armario.nombre == "Ropero"
    assert armario.num_puertas == 3


def test_calcular_precio_armario(armario):
    p = armario.calcular_precio()
    assert isinstance(p, int)
    assert p >= armario.precio_base
