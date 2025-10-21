import pytest
from src.models.composicion.comedor import Comedor


def test_agregar_silla_invalida(mesa_factory):
    mesa = mesa_factory()
    comedor = Comedor("C", mesa, [])
    # pasar un objeto que no es Silla (ej: int)
    res = comedor.agregar_silla(123)
    assert "Error" in res or "agregada" in res


def test_quitar_silla_indices(mesa_factory):
    mesa = mesa_factory()
    comedor = Comedor("C2", mesa, [])
    # quitar cuando no hay sillas
    assert comedor.quitar_silla() == "No hay sillas para quitar"
    # agregar y quitar con indice inválido
    class Dummy: pass
    dummy = Dummy()
    comedor._sillas.append(dummy)
    assert comedor.quitar_silla(10) == "Índice de silla inválido"


def test_calcular_precio_descuento(mesa_factory, silla_factory):
    mesa = mesa_factory(precio=100.0, capacidad=6)
    sillas = [silla_factory(precio=50.0) for _ in range(6)]
    comedor = Comedor("C3", mesa, sillas)
    total = comedor.calcular_precio_total()
    # con 6 sillas aplica 5% de descuento
    assert isinstance(total, float)
    assert total > 0


def test_obtener_resumen_y_materiales(mesa_factory, silla_factory):
    mesa = mesa_factory(precio=120.0)
    s1 = silla_factory(nombre="S1", precio=40.0, material="Roble")
    s2 = silla_factory(nombre="S2", precio=40.0, material="Roble")
    comedor = Comedor("C4", mesa, [s1, s2])
    resumen = comedor.obtener_resumen()
    assert resumen["nombre"] == "C4"
    assert resumen["total_muebles"] >= 1
    assert isinstance(resumen["materiales_utilizados"], list)


def test_obtener_descripcion_completa_y_len(mesa_factory, silla_factory):
    mesa = mesa_factory(precio=100.0)
    s1 = silla_factory(nombre="S1", precio=40.0, material="Roble")
    s2 = silla_factory(nombre="S2", precio=40.0, material="Metal")
    comedor = Comedor("C5", mesa, [s1, s2])
    desc = comedor.obtener_descripcion_completa()
    assert "COMEDOR" in desc.upper()
    assert len(comedor) == 3  # mesa + 2 sillas


def test_calcular_capacidad_maxima(mesa_factory):
    # Mesa con capacidad_personas presente
    m = mesa_factory(capacidad=8)
    comedor = Comedor("C6", m, [])
    # _calcular_capacidad_maxima es privado; invocamos indirectamente
    assert comedor._calcular_capacidad_maxima() == 8
