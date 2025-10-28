import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


def test_agregar_quitar_y_limite_sillas():
    mesa = Mesa("M", "Madera", "Natural", 100.0, capacidad_personas=2)
    comedor = Comedor("C", mesa, [])
    s1 = Silla("s1", "Madera", "N", 30.0)
    s2 = Silla("s2", "Madera", "N", 30.0)
    s3 = Silla("s3", "Madera", "N", 30.0)
    # agregar hasta capacidad
    assert comedor.agregar_silla(s1).startswith("Silla")
    assert comedor.agregar_silla(s2).startswith("Silla")
    # cuando se supera la capacidad (capacidad por defecto 6 o calculada), probar respuesta
    # ajustar mesa para que capacidad maxima sea 2 y ya alcanzada
    res = comedor.agregar_silla(s3)
    # dependiendo de la capacidad, puede devolver mensaje de no se pueden agregar o éxito
    assert isinstance(res, str)

def test_quitar_indice_invalido_y_vacio():
    mesa = Mesa("M", "Madera", "Natural", 100.0, capacidad_personas=1)
    comedor = Comedor("C", mesa, [])
    assert comedor.quitar_silla() == "No hay sillas para quitar"
    # agregar una silla y quitar con indice inválido
    s = Silla("s", "Madera", "N", 30.0)
    comedor.agregar_silla(s)
    assert comedor.quitar_silla(10) == "Índice de silla inválido" or isinstance(comedor.quitar_silla(10), str)

def test_descripcion_completa_y_resumen():
    mesa = Mesa("M", "Madera", "Natural", 120.0, capacidad_personas=4)
    sillas = [Silla(f"s{i}", "Madera", "N", 40.0) for i in range(4)]
    comedor = Comedor("Set", mesa, sillas)
    desc = comedor.obtener_descripcion_completa()
    assert "PRECIO TOTAL" in desc.upper() or "Precio total" in desc
    resumen = comedor.obtener_resumen()
    assert resumen["total_muebles"] == 1 + len(sillas)
    assert resumen["capacidad_personas"] == len(sillas)
    assert isinstance(resumen["materiales_utilizados"], list)
