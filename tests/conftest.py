import pytest
from src.models.concretos.silla import Silla
from src.models.concretos.mesa import Mesa
from src.services.tienda import TiendaMuebles


@pytest.fixture
def silla_factory():
    def _silla(nombre="Silla", precio=50.0, material="Madera"):
        return Silla(nombre, material, "Natural", precio)
    return _silla


@pytest.fixture
def mesa_factory():
    def _mesa(nombre="Mesa", precio=200.0, capacidad=4):
        return Mesa(nombre, "Roble", "Natural", precio, capacidad_personas=capacidad)
    return _mesa


@pytest.fixture
def tienda_factory():
    def _tienda():
        return TiendaMuebles("Tienda Test")
    return _tienda
