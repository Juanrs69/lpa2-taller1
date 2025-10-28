import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla

class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        # Construir con firmas actuales: Mesa(nombre, material, color, precio_base, forma, capacidad_personas)
        mesa = Mesa("Mesa Comedor", "Roble", "Natural", 200.0, forma="rectangular", capacidad_personas=6)
        sillas = [Silla("Silla Comedor", "Roble", "Natural", 50.0) for _ in range(6)]
        return Comedor("Comedor Familiar", mesa, sillas)
    
    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)
    
    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        precio_esperado = comedor_basico.mesa.calcular_precio() + sum(s.calcular_precio() for s in comedor_basico.sillas)
        # si aplica descuento por set completo
        if len(comedor_basico.sillas) >= 4:
            precio_esperado = round(precio_esperado * 0.95, 2)
        assert precio_total == precio_esperado