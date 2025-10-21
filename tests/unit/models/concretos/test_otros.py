import pytest
from src.models.concretos.sofa import Sofa
from src.models.concretos.sofacama import SofaCama
from src.models.concretos.cama import Cama
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera


def test_sofa_y_atributos():
    s = Sofa("Sofa1", "Tela", "Gris", 500.0, capacidad_personas=3, incluye_cojines=True)
    assert s.capacidad_personas == 3
    assert s.incluye_cojines is True
    assert s.calcular_precio() > 500.0


def test_sofacama_conversion_y_precio():
    sc = SofaCama("SC", "Tela", "Beige", 400, capacidad_personas=3, tamaño_cama="matrimonial", incluye_colchon=True)
    assert sc.modo_actual == "sofa"
    msg = sc.convertir_a_cama()
    assert "convertido" in msg.lower()
    assert sc.calcular_precio() > 0


def test_cama_tamanos_y_extras():
    c = Cama("C1", "Madera", "Blanco", 300.0, tamaño="queen", incluye_colchon=True, tiene_cabecera=True)
    assert c.tamaño == "queen"
    assert c.calcular_precio() > 300


def test_armario_cajonera_precio_y_descripcion():
    a = Armario("A1", "Madera", "Natural", 250, num_puertas=3, num_cajones=2, tiene_espejos=True)
    assert a.calcular_precio() > 250
    assert "Armario" in a.obtener_descripcion()
    caj = Cajonera("CJ", "Metal", "Blanco", 120, num_cajones=4, tiene_ruedas=True)
    assert caj.calcular_precio() > 120
    assert "Cajonera" in caj.obtener_descripcion()
