import pytest
from src.models.concretos.cama import Cama


@pytest.fixture
def cama_basica():
    return Cama("Cama 1", "Madera", "Roble", 300.0, incluye_colchon=False)


def test_instanciacion_cama(cama_basica):
    assert cama_basica.nombre == "Cama 1"


def test_precio_cama(cama_basica):
    precio = cama_basica.calcular_precio()
    assert isinstance(precio, (int, float))
