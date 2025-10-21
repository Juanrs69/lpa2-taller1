import pytest
from src.models.concretos.mesa import Mesa


def test_mesa_instanciacion_y_validacion():
    m = Mesa("Mesa", "Roble", "Natural", 200.0, forma="rectangular", capacidad_personas=4)
    assert m.capacidad_personas == 4
    with pytest.raises(ValueError):
        m.forma = "triangular"
    with pytest.raises(ValueError):
        m.capacidad_personas = 0


def test_mesa_calcular_precio():
    m = Mesa("Comedor", "Roble", "Natural", 200.0, forma="redonda", capacidad_personas=8)
    precio = m.calcular_precio()
    assert precio > 200.0
