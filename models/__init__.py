import os

# Este paquete es un shim para permitir importaciones como `from models.x import Y`
# apuntando al contenido real en `src/models`.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_MODELS = os.path.join(ROOT, "src", "models")

if os.path.isdir(SRC_MODELS):
    # Reemplazar el search path del paquete para que Python busque los módulos en src/models
    __path__ = [SRC_MODELS]
else:
    # Fallback: mantener el path por defecto
    __path__ = [os.path.dirname(__file__)]
