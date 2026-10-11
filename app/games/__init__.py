"""Paquete con la lógica de cada juego de sorteo.

Cada módulo expone una función pura y sin estado que devuelve un
diccionario listo para serializar a JSON.
"""

from . import dados, moneda, ruleta

__all__ = ["dados", "moneda", "ruleta"]
