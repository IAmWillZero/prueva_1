"""Lógica del juego cara o cruz."""

import random

RESULTADOS = ("cara", "cruz")


def lanzar() -> dict:
    """Lanza una moneda y devuelve ``cara`` o ``cruz``."""
    return {"resultado": random.choice(RESULTADOS)}
