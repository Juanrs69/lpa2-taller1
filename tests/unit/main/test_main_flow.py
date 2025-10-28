import sys
import os

# Asegurar que el paquete 'ui' y 'services' importen desde el directorio src
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
SRC_PATH = os.path.join(ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from src import main as main_module
from src.services.tienda import TiendaMuebles


def test_crear_catalogo_y_comedores(capsys):
    tienda = TiendaMuebles("Prueba")
    # Llamar funciones que crean catálogos y comedores
    main_module.crear_catalogo_inicial(tienda)
    main_module.crear_comedores_ejemplo(tienda)
    out = capsys.readouterr().out
    # Verificar que se imprimieron mensajes de creación
    assert "Creando catálogo" in out or "Catálogo inicial" in out
    assert len(tienda._inventario) > 0
    assert len(tienda._comedores) > 0


def test_aplicar_descuentos_ejemplo(capsys):
    tienda = TiendaMuebles("Prueba")
    main_module.aplicar_descuentos_ejemplo(tienda)
    out = capsys.readouterr().out
    assert "Descuentos" in out or "aplicado" in out


def test_mostrar_estadisticas_iniciales(capsys):
    tienda = TiendaMuebles("Prueba")
    main_module.mostrar_estadisticas_iniciales(tienda)
    out = capsys.readouterr().out
    assert "Estadísticas" in out or "Total de muebles" in out
