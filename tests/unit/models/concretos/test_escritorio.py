import pytest
from src.models.concretos.escritorio import Escritorio


@pytest.fixture
def escritorio_basico():
    return Escritorio("Escritorio Home", "Madera", "Nogal", 200.0, tiene_cajones=True)


def test_instaciacion_escritorio(escritorio_basico):
    assert escritorio_basico.nombre == "Escritorio Home"


def test_precio_escritorio(escritorio_basico):
    precio = escritorio_basico.calcular_precio()
    assert isinstance(precio, (int, float))
