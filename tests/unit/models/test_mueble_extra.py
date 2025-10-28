import pytest
from src.models.mueble import Mueble


class _Stub(Mueble):
    def calcular_precio(self):
        return 1.0
    def obtener_descripcion(self):
        return "stub"


def test_setters_and_str_repr():
    s = _Stub("N", "Madera", "Rojo", 10.0)
    assert str(s).startswith("N de Madera")
    assert "Mueble(" in repr(s)
    # name validation
    with pytest.raises(ValueError):
        s.nombre = ""
    with pytest.raises(ValueError):
        s.material = "   "
    with pytest.raises(ValueError):
        s.color = ""
    with pytest.raises(ValueError):
        s.precio_base = -5
