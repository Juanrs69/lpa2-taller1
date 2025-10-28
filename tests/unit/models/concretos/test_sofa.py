import pytest
from src.models.concretos.sofa import Sofa


@pytest.fixture
def sofa_basico():
    return Sofa("Sofá 3 puestos", "Tela", "Azul", 500.0, es_modular=False)


def test_instanciacion_sofa(sofa_basico):
    assert sofa_basico.nombre == "Sofá 3 puestos"


def test_precio_sofa(sofa_basico):
    precio = sofa_basico.calcular_precio()
    assert isinstance(precio, (int, float))
