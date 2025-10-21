import pytest
from src.models.mueble import Mueble


def test_mueble_abstract_methods_present():
    assert hasattr(Mueble, 'calcular_precio')
    assert hasattr(Mueble, 'obtener_descripcion')


def test_setters_validations():
    class Impl(Mueble):
        def calcular_precio(self):
            return self.precio_base

        def obtener_descripcion(self):
            return ""

    m = Impl("X", "Madera", "Rojo", 10.0)
    with pytest.raises(ValueError):
        m.nombre = ""
    with pytest.raises(ValueError):
        m.material = ""
    with pytest.raises(ValueError):
        m.color = ""
    with pytest.raises(ValueError):
        m.precio_base = -1
