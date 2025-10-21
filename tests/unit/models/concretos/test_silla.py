import pytest
from src.models.concretos.silla import Silla


@pytest.fixture
def silla_basica():
    return Silla("Silla Básica", "Madera", "Marrón", 50.0, tiene_respaldo=True, material_tapizado=None)


def test_instanciacion_y_atributos(silla_basica):
    assert silla_basica.nombre == "Silla Básica"
    assert silla_basica.material == "Madera"
    assert silla_basica.precio_base == 50.0


def test_calcular_precio_y_metodos(silla_basica):
    precio = silla_basica.calcular_precio()
    assert isinstance(precio, float)
    desc = silla_basica.obtener_descripcion()
    assert "Silla" in desc
    assert "Precio final" in desc


def test_regular_altura_y_ruedas():
    s = Silla("Oficina", "Metal", "Negro", 120.0, altura_regulable=False, tiene_ruedas=False)
    assert s.regular_altura(50) == "Esta silla no tiene altura regulable"
    s.altura_regulable = True
    assert s.regular_altura(30) == "La altura debe estar entre 40 y 100 cm"
    assert s.regular_altura(60) == "Altura ajustada a 60 cm"
