import pytest
from unittest.mock import Mock
from src.services.tienda import TiendaMuebles


def test_agregar_mueble_valido(silla_factory, tienda_factory):
    tienda = tienda_factory()
    silla = silla_factory()
    res = tienda.agregar_mueble(silla)
    assert "agregado" in res


def test_agregar_mueble_invalidos(tienda_factory):
    tienda = tienda_factory()
    assert "Error" in tienda.agregar_mueble(None)
    # objeto con calcular_precio que lanza
    class Bad:
        def calcular_precio(self):
            raise RuntimeError("boom")
    assert "Error" in tienda.agregar_mueble(Bad())


def test_buscar_y_filtrar(silla_factory, tienda_factory):
    tienda = tienda_factory()
    s1 = silla_factory(nombre="Silla A")
    s2 = silla_factory(nombre="Silla B")
    tienda.agregar_mueble(s1)
    tienda.agregar_mueble(s2)
    res = tienda.buscar_muebles_por_nombre("silla")
    assert len(res) == 2
    filt = tienda.filtrar_por_precio(0, 60)
    assert len(filt) >= 2


def test_aplicar_descuento_y_venta(silla_factory, tienda_factory):
    tienda = tienda_factory()
    s = silla_factory(precio=100.0)
    tienda.agregar_mueble(s)
    tienda.aplicar_descuento('sillas', 10)
    venta = tienda.realizar_venta(s, cliente="Juan")
    assert 'precio_final' in venta
    assert venta['cliente'] == 'Juan'


def test_generar_reporte_y_estadisticas(tienda_factory, silla_factory):
    tienda = tienda_factory()
    s = silla_factory(precio=80.0)
    tienda.agregar_mueble(s)
    reporte = tienda.generar_reporte_inventario()
    assert "REPORTE" in reporte.upper()
    stats = tienda.obtener_estadisticas()
    assert isinstance(stats, dict)


def test_realizar_venta_error_no_disponible(tienda_factory, silla_factory):
    tienda = tienda_factory()
    s = silla_factory(precio=80.0)
    # no agregado al inventario
    res = tienda.realizar_venta(s)
    assert 'error' in res
