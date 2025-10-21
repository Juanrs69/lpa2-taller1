import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


@pytest.fixture
def comedor_basico():
    mesa = Mesa("Mesa", "Roble", "Natural", 200.0, capacidad_personas=6)
    sillas = [Silla(f"Silla{i}", "Madera", "Marrón", 50.0) for i in range(6)]
    return Comedor("Comedor1", mesa, sillas)


def test_calcular_precio_total(comedor_basico):
    precio_total = comedor_basico.calcular_precio_total()
    assert precio_total > 0


def test_agregar_quitar_silla():
    mesa = Mesa("Mesa2", "Roble", "Natural", 150.0)
    c = Comedor("C2", mesa, [])
    s = Silla("Extra", "Madera", "Negro", 45.0)
    msg = c.agregar_silla(s)
    assert "agregada" in msg.lower()
    assert len(c.sillas) == 1
    msg2 = c.quitar_silla()  # quita la última por defecto
    assert "removida" in msg2.lower()
    assert len(c.sillas) == 0
