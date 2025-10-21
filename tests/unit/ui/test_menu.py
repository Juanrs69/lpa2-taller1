import pytest
from src.ui.menu import MenuTienda
from src.services.tienda import TiendaMuebles
from src.models.concretos.silla import Silla


@pytest.fixture
def menu(tienda_factory, capsys):
    tienda = tienda_factory()
    m = MenuTienda(tienda)
    return m


def test_mostrar_banner(menu, capsys):
    menu.mostrar_banner()
    # solo comprobamos que no lanza y produce salida
    captured = capsys.readouterr()
    assert captured.out


def test_mostrar_catalogo_vacio(menu, capsys):
    menu.mostrar_catalogo_completo()
    out = capsys.readouterr().out
    assert "No hay muebles" in out


def test_mostrar_lista_muebles(menu, silla_factory, capsys):
    s = silla_factory()
    menu.tienda._inventario.append(s)
    menu._mostrar_lista_muebles(menu.tienda._inventario)
    out = capsys.readouterr().out
    assert "Silla" in out or "$" in out


def test_mostrar_comprobante(menu, capsys):
    venta = {
        'cliente': 'Ana',
        'mueble': 'Silla X',
        'precio_original': 100.0,
        'descuento': 10.0,
        'precio_final': 90.0
    }
    menu._mostrar_comprobante_venta(venta)
    out = capsys.readouterr().out
    assert "COMPROBANTE" in out.upper() or "PRECIO FINAL" in out.upper()
