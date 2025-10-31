import pytest
from src.models.concretos.comedor import Comedor as ComedorConcreto
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


@pytest.fixture
def mesa():
    return Mesa("Mesa Redonda", "Madera", "Natural", 180.0, capacidad_personas=4)


@pytest.fixture
def sillas():
    return [Silla(f"Silla {i}", "Madera", "Natural", 45.0) for i in range(4)]


def test_comedor_concreto(mesa, sillas):
    comedor = ComedorConcreto(mesa, sillas)
    # comprobaciones básicas de composición
    assert hasattr(comedor, "mesa")
    assert isinstance(comedor.mesa, Mesa)
    assert comedor.cantidad_sillas() == len(sillas)
    assert comedor.calcular_precio_total() >= mesa.calcular_precio()
