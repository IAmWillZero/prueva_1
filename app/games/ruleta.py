"""Lógica de la ruleta europea (números del 0 al 36)."""

import random

# Distribución de colores de la ruleta europea.
ROJOS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
NEGROS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

NUMERO_MAXIMO = 36


def color_de(numero: int) -> str:
    """Devuelve el color que corresponde a un número de la ruleta."""
    if numero == 0:
        return "verde"
    return "rojo" if numero in ROJOS else "negro"


def girar() -> dict:
    """Gira la ruleta y devuelve el número obtenido junto a su color."""
    numero = random.randint(0, NUMERO_MAXIMO)
    return {"numero": numero, "color": color_de(numero)}
