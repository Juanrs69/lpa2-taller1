import pytest
from src.models.concretos.cajonera import Cajonera


@pytest.fixture
def cajonera():
    return Cajonera("Cajonera Simple", "MDF", "Blanco", 110, num_cajones=3)


def test_instanciacion_cajonera(cajonera):
    assert cajonera.num_cajones == 3


def test_precio_cajonera(cajonera):
    precio = cajonera.calcular_precio()
    assert isinstance(precio, (int, float))
    assert precio > 0
