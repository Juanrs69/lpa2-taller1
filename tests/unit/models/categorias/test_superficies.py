import pytest
from src.models.categorias.superficies import Superficie


class ConcreteSuperficie(Superficie):
    def calcular_precio(self) -> float:
        return round(self.precio_base * self.calcular_factor_tamaño(), 2)

    def obtener_descripcion(self) -> str:
        return "desc"


def test_calcular_area_y_factor():
    s = ConcreteSuperficie("S", "Madera", "Blanco", 100.0, 100.0, 50.0, 75.0)
    area = s.calcular_area()
    assert area == 5000.0
    factor = s.calcular_factor_tamaño()
    assert factor > 0


def test_largo_ancho_altura_validacion():
    s = ConcreteSuperficie("S2", "Madera", "Blanco", 80.0, 10.0, 10.0, 10.0)
    with pytest.raises(ValueError):
        s.largo = 0
    with pytest.raises(ValueError):
        s.ancho = -1
    with pytest.raises(ValueError):
        s.altura = 0
