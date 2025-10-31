"""
Clase concreta Cajonera.
Representa una cajonera genérica.
"""

from ..categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
    """
    Clase concreta que representa una cajonera.
    Hereda de Almacenamiento.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        num_cajones: int = 3,
        tiene_ruedas: bool = False,
        capacidad_litros: float = 150.0,
    ):
        # Los compartimentos son los cajones
        super().__init__(
            nombre,
            material,
            color,
            precio_base,
            num_compartimentos=num_cajones,
            capacidad_litros=capacidad_litros,
        )
        self.num_cajones = num_cajones
        self.tiene_ruedas = tiene_ruedas

    def calcular_precio(self) -> float:
        """Calcula el precio final de la cajonera."""
        precio = self.precio_base
        precio += self.num_cajones * 20
        if self.tiene_ruedas:
            precio += 30
        # Aplicar factor de almacenamiento
        precio *= self.calcular_factor_almacenamiento()
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada de la cajonera.
        """
        desc = (
            f"Cajonera '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Cajones={self.num_cajones}, Ruedas={'Sí' if self.tiene_ruedas else 'No'}, "
            f"Precio base=${self.precio_base:.2f}, "
        )
        desc += self.obtener_info_almacenamiento()
        return desc
