import pytest
from src.models.categorias.almacenamiento import Almacenamiento
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera


@pytest.fixture
def armario_basico():
    return Armario(
        "Armario Básico", "Madera", "Blanco", 200, num_puertas=2, num_cajones=0
    )


@pytest.fixture
def cajonera_basica():
    return Cajonera("Cajonera 3 cajones", "MDF", "Gris", 120, num_cajones=3)


def test_almacenamiento_es_abstracta():
    """Verifica que Almacenamiento es una clase abstracta."""
    with pytest.raises(TypeError):
        Almacenamiento(
            "Test",
            "Madera",
            "Blanco",
            100.0,
            num_compartimentos=3,
            capacidad_litros=50.0,
        )


def test_instanciacion_armario(armario_basico):
    assert armario_basico.nombre == "Armario Básico"
    assert armario_basico.num_puertas == 2
    # Verificar que es instancia de Almacenamiento
    assert isinstance(armario_basico, Almacenamiento)


def test_calcular_precio_armario(armario_basico):
    precio = armario_basico.calcular_precio()
    assert isinstance(precio, (int, float))
    assert precio > 0


def test_instanciacion_cajonera(cajonera_basica):
    assert cajonera_basica.num_cajones == 3
    # Verificar que es instancia de Almacenamiento
    assert isinstance(cajonera_basica, Almacenamiento)


def test_calcular_precio_cajonera(cajonera_basica):
    precio = cajonera_basica.calcular_precio()
    assert isinstance(precio, (int, float))
    assert precio > 0


def test_propiedades_almacenamiento(armario_basico):
    """Prueba las propiedades de almacenamiento."""
    assert armario_basico.num_compartimentos > 0
    assert armario_basico.capacidad_litros > 0


def test_calcular_factor_almacenamiento(cajonera_basica):
    """Prueba el cálculo del factor de almacenamiento."""
    factor = cajonera_basica.calcular_factor_almacenamiento()
    assert isinstance(factor, float)
    assert factor >= 1.0


def test_obtener_info_almacenamiento(armario_basico):
    """Prueba que se obtiene información del almacenamiento."""
    info = armario_basico.obtener_info_almacenamiento()
    assert isinstance(info, str)
    assert "Compartimentos" in info
    assert "Capacidad" in info


def test_setter_num_compartimentos_valido(armario_basico):
    """Prueba que se puede cambiar el número de compartimentos."""
    armario_basico.num_compartimentos = 5
    assert armario_basico.num_compartimentos == 5


def test_setter_num_compartimentos_invalido(armario_basico):
    """Prueba que no se puede poner 0 o negativo en compartimentos."""
    with pytest.raises(ValueError):
        armario_basico.num_compartimentos = 0
    with pytest.raises(ValueError):
        armario_basico.num_compartimentos = -1


def test_setter_capacidad_litros_valido(cajonera_basica):
    """Prueba que se puede cambiar la capacidad."""
    cajonera_basica.capacidad_litros = 100.0
    assert cajonera_basica.capacidad_litros == 100.0


def test_setter_capacidad_litros_invalido(cajonera_basica):
    """Prueba que no se puede poner 0 o negativo en capacidad."""
    with pytest.raises(ValueError):
        cajonera_basica.capacidad_litros = 0
    with pytest.raises(ValueError):
        cajonera_basica.capacidad_litros = -10.0
