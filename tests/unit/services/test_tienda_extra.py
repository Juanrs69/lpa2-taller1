import pytest
from src.services.tienda import TiendaMuebles


class DummyBad:
    def calcular_precio(self):
        raise RuntimeError("precio fallo")


def test_agregar_mueble_none():
    t = TiendaMuebles()
    assert t.agregar_mueble(None).startswith("Error")


def test_agregar_mueble_precio_error():
    t = TiendaMuebles()
    bad = DummyBad()
    res = t.agregar_mueble(bad)
    assert res.startswith("Error")


def test_buscar_y_filtrar():
    t = TiendaMuebles()
    class Item:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self._precio = precio
        def calcular_precio(self):
            return self._precio
    a = Item("Silla Roja", 50)
    b = Item("Mesa Azul", 200)
    t.agregar_mueble(a)
    t.agregar_mueble(b)
    assert t.buscar_muebles_por_nombre("") == []
    res = t.buscar_muebles_por_nombre("silla")
    assert a in res
    # filtrar por precio con min negativo
    res2 = t.filtrar_por_precio(-10, 100)
    assert a in res2 and b not in res2
    # filtrar por material (items have no material -> should skip)
    assert t.filtrar_por_material("") == []


def test_aplicar_descuento_y_realizar_venta():
    t = TiendaMuebles()
    class Item:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self._precio = precio
        def calcular_precio(self):
            return self._precio
    it = Item("SillaDesc", 100)
    t.agregar_mueble(it)
    # aplicar descuento inválido
    assert t.aplicar_descuento("sillas", 0) .startswith("Error")
    # aplicar descuento válido
    assert "aplicado" in t.aplicar_descuento("sillas", 10)
    # realizar venta por nombre
    assert t.vender_producto("SillaDesc") is True
    # vender inexistente
    assert t.vender_producto("NoExiste") is False


def test_generar_reporte_inventario_vacio():
    t = TiendaMuebles("MiTienda")
    rep = t.generar_reporte_inventario()
    assert "REPORTE" in rep or "Total de muebles" in rep
