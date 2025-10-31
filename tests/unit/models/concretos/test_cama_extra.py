from src.models.concretos.cama import Cama


def test_cama_tamanos_y_extras():
    c1 = Cama(
        "C1",
        "Madera",
        "Natural",
        300.0,
        tamaño="individual",
        incluye_colchon=False,
        tiene_cabecera=False,
    )
    c2 = Cama(
        "C2",
        "Madera",
        "Natural",
        300.0,
        tamaño="queen",
        incluye_colchon=True,
        tiene_cabecera=True,
    )
    # comprobar que ambos calculan precio y que la queen+colchon es más caro
    p1 = c1.calcular_precio()
    p2 = c2.calcular_precio()
    assert isinstance(p1, float) and isinstance(p2, float)
    assert p2 >= p1
    # cambiar tamaño en c1 y comprobar que precio cambia
    c1.tamaño = "matrimonial"
    assert c1.tamaño == "matrimonial"
    assert c1.calcular_precio() != p1
