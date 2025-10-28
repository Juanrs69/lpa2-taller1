import pytest
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera


@pytest.fixture
def armario_basico():
    return Armario("Armario Básico", "Madera", "Blanco", 200, num_puertas=2, num_cajones=0)


@pytest.fixture
def cajonera_basica():
    return Cajonera("Cajonera 3 cajones", "MDF", "Gris", 120, num_cajones=3)


def test_instanciacion_armario(armario_basico):
    assert armario_basico.nombre == "Armario Básico"
    assert armario_basico.num_puertas == 2


def test_calcular_precio_armario(armario_basico):
    precio = armario_basico.calcular_precio()
    assert isinstance(precio, (int, float))


def test_instanciacion_cajonera(cajonera_basica):
    assert cajonera_basica.num_cajones == 3


def test_calcular_precio_cajonera(cajonera_basica):
    precio = cajonera_basica.calcular_precio()
    assert isinstance(precio, (int, float))
