"""Lógica del juego de dados."""

import random

CARAS_POR_DEFECTO = 6
CANTIDAD_MAXIMA = 10
CARAS_MAXIMAS = 100


def tirar(cantidad: int = 1, caras: int = CARAS_POR_DEFECTO) -> dict:
    """Tira ``cantidad`` dados de ``caras`` caras cada uno.

    Los valores se limitan a rangos razonables para evitar abusos en la API.
    """
    cantidad = max(1, min(int(cantidad), CANTIDAD_MAXIMA))
    caras = max(2, min(int(caras), CARAS_MAXIMAS))

    valores = [random.randint(1, caras) for _ in range(cantidad)]
    return {
        "dados": valores,
        "total": sum(valores),
        "caras": caras,
    }
