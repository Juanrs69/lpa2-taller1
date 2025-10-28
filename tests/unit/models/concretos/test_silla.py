import pytest
from src.models.concretos.silla import Silla

class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        # firma actual: Silla(nombre, material, color, precio_base, tiene_respaldo=True, material_tapizado=None, ...)
        return Silla("Silla Básica", "Madera", "Marrón", 50.0)
    
    def test_instanciacion_correcta(self, silla_basica):
        # Verificar herencia de atributos
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.precio_base == 50.0
        # Verificar atributos específicos (firma actual)
        assert hasattr(silla_basica, 'altura_regulable')
        assert hasattr(silla_basica, 'tiene_ruedas')
    
    def test_calcular_precio(self, silla_basica):
        # Probar polimorfismo
        precio = silla_basica.calcular_precio()
        assert isinstance(precio, float)
        assert precio >= 50.0
    
    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion