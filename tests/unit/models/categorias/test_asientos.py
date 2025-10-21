import pytest
from src.models.categorias.asientos import Asiento


class ConcreteAsiento(Asiento):
    def calcular_precio(self) -> float:
        return round(self.precio_base * self.calcular_factor_comodidad(), 2)

    def obtener_descripcion(self) -> str:
        return "desc"


def test_factor_comodidad_respaldo_y_tapizado():
    a = ConcreteAsiento("A", "Madera", "Rojo", 100.0, 1, True, "cuero")
    factor = a.calcular_factor_comodidad()
    # tiene respaldo (+0.1) y cuero (+0.2)
    assert factor > 1.0
    assert round(a.calcular_precio(), 2) == round(100.0 * factor, 2)


def test_capacidad_personas_setter_validation():
    a = ConcreteAsiento("A2", "Madera", "Negro", 50.0, 1, False)
    with pytest.raises(ValueError):
        a.capacidad_personas = 0
