import pytest
from src.models.concretos.sillon import Sillon


@pytest.fixture
def sillon_basico():
    return Sillon("Sillón Relax", "Tela", "Gris", 350.0, es_reclinable=True)


def test_instanciacion_sillon(sillon_basico):
    assert sillon_basico.nombre == "Sillón Relax"


def test_precio_sillon(sillon_basico):
    precio = sillon_basico.calcular_precio()
    assert isinstance(precio, (int, float))
