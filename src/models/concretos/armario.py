"""
Clase concreta Armario.
Representa un armario genérico.
"""

from ..categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
    """
    Clase concreta que representa un armario.
    Hereda de Almacenamiento.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        num_puertas: int = 2,
        num_cajones: int = 0,
        tiene_espejos: bool = False,
        num_compartimentos: int = 1,
        capacidad_litros: float = 200.0,
    ):
        # Calcular compartimentos y capacidad basados en puertas y cajones
        total_compartimentos = (
            num_puertas + num_cajones if num_compartimentos == 1 else num_compartimentos
        )
        capacidad_total = capacidad_litros + (num_puertas * 50) + (num_cajones * 20)

        super().__init__(
            nombre,
            material,
            color,
            precio_base,
            num_compartimentos=total_compartimentos,
            capacidad_litros=capacidad_total,
        )
        self.num_puertas = num_puertas
        self.num_cajones = num_cajones
        self.tiene_espejos = tiene_espejos

    def calcular_precio(self) -> float:
        """Calcula el precio final del armario."""
        precio = self.precio_base
        precio += self.num_puertas * 50
        precio += self.num_cajones * 30
        if self.tiene_espejos:
            precio += 100
        # Aplicar factor de almacenamiento
        precio *= self.calcular_factor_almacenamiento()
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del armario.
        """
        desc = (
            f"Armario '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Puertas={self.num_puertas}, Cajones={self.num_cajones}, Espejos={'Sí' if self.tiene_espejos else 'No'}, "
            f"Precio base=${self.precio_base:.2f}, "
        )
        desc += self.obtener_info_almacenamiento()
        return desc
