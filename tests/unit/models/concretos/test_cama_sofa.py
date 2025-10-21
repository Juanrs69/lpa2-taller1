import pytest
from src.models.concretos.cama import Cama
from src.models.concretos.sofa import Sofa


def test_cama_tamanos_invalidos():
    c = Cama("C", "Madera", "Blanco", 300.0)
    with pytest.raises(ValueError):
        c.tamaño = "gigante"


def test_sofa_caracteristicas():
    s = Sofa("S", "Tela", "Azul", 400.0, tiene_brazos=False, es_modular=True, incluye_cojines=True)
    precio = s.calcular_precio()
    assert precio > 0
    desc = s.obtener_descripcion()
    assert "Sofá" in desc
