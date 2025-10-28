import pytest
from src.models.concretos.sofacama import SofaCama
from src.models.concretos.sofa import Sofa
from src.models.concretos.cama import Cama


def test_sofacama_herencia_y_str():
    s = SofaCama("SofaCama X", "Tela", "Gris", 400, capacidad_personas=3, material_tapizado="tela", tamaño_cama="matrimonial", incluye_colchon=True, mecanismo_conversion="hidraulico")
    # herencia: debería comportarse como Sofa y Cama
    assert isinstance(s, Sofa)
    assert isinstance(s, Cama)
    assert "SofaCama X" in str(s)
    assert "modo" in str(s)


def test_convertir_modos_y_capacidades():
    s = SofaCama("SC", "Tela", "Beige", 350, capacidad_personas=2, tamaño_cama="queen", incluye_colchon=False, mecanismo_conversion="electrico")
    # modo inicial sofa
    assert s.modo_actual == "sofa"
    # convertir a cama
    res = s.convertir_a_cama()
    assert "convertido" in res.lower()
    assert s.modo_actual == "cama"
    # convertir de nuevo a sofa
    res2 = s.convertir_a_sofa()
    assert "convertida" in res2.lower() or "convertido" in res2.lower()
    assert s.modo_actual == "sofa"
    # capacidades
    caps = s.obtener_capacidad_total()
    assert caps["como_sofa"] == s.capacidad_personas
    assert caps["como_cama"] == 2


def test_calcular_precio_variantes():
    base = 300
    s1 = SofaCama("A", "Tela", "N", base, capacidad_personas=3, tamaño_cama="matrimonial", incluye_colchon=True, mecanismo_conversion="hidraulico")
    s2 = SofaCama("B", "Tela", "N", base, capacidad_personas=3, tamaño_cama="queen", incluye_colchon=False, mecanismo_conversion="electrico")
    # s1 debe incluir recargos por matrimonial + colchon + hidraulico
    p1 = s1.calcular_precio()
    p2 = s2.calcular_precio()
    assert isinstance(p1, float)
    assert isinstance(p2, float)
    assert p1 != p2


def test_obtener_descripcion_contiene_campos():
    s = SofaCama("Desc", "Tela", "Azul", 250, mecanismo_conversion="hidraulico")
    desc = s.obtener_descripcion()
    assert "Mecanismo" in desc or "Mecanismo:" in desc or "mecanismo" in desc.lower()
    assert "Precio final" in desc or "Precio final" in desc
