import pytest
from src.models.concretos.sofacama import SofaCama


def test_sofacama_mecanismos_y_capacidades():
    sc1 = SofaCama("SC1", "Tela", "Beige", 400, capacidad_personas=3, tamaño_cama="matrimonial", incluye_colchon=True, mecanismo_conversion="hidraulico")
    assert sc1.mecanismo_conversion == "hidraulico"
    assert sc1.calcular_precio() > 0
    # convertir modos
    assert sc1.modo_actual == "sofa"
    msg = sc1.convertir_a_cama()
    assert "convertido" in msg.lower()
    msg2 = sc1.convertir_a_sofa()
    assert "convertida" in msg2.lower() or "convertido" in msg2.lower()


def test_sofacama_mecanismo_electrico():
    sc2 = SofaCama("SC2", "Cuero", "Negro", 600, capacidad_personas=2, tamaño_cama="queen", incluye_colchon=False, mecanismo_conversion="electrico")
    precio = sc2.calcular_precio()
    assert precio >= 0
    caps = sc2.obtener_capacidad_total()
    assert "como_sofa" in caps and "como_cama" in caps
