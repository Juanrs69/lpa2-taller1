from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    def test_herencia_multiple(self):
        sofa_cama = SofaCama(
            "Sofá Cama Moderno",
            "Tela",
            "Gris",
            500.0,
            capacidad_personas=3,
            tamaño_cama="queen",
        )

        # Verificar atributos de Sofa
        assert hasattr(sofa_cama, "capacidad_personas")
        assert sofa_cama.capacidad_personas == 3

        # Verificar atributos de Cama
        assert hasattr(sofa_cama, "tamaño_cama") or hasattr(sofa_cama, "tamaño")
        assert sofa_cama.tamaño_cama == "queen"

        # Verificar métodos de conversión
        assert hasattr(sofa_cama, "convertir_a_cama")

    def test_resolucion_metodos(self):
        sofa_cama = SofaCama(
            "Sofá Cama",
            "Cuero",
            "Marrón",
            600.0,
            capacidad_personas=2,
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="electrico",
        )

        # Verificar que usa el método correcto (MRO)
        precio = sofa_cama.calcular_precio()
        assert precio > 600.0  # Debe incluir recargos de ambas clases
