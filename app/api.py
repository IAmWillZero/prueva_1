"""Endpoints JSON que resuelven los sorteos."""

from flask import Blueprint, jsonify, request

from .games import dados, moneda, ruleta

api_bp = Blueprint("api", __name__)


@api_bp.post("/ruleta")
def api_ruleta():
    """Gira la ruleta y devuelve el número y su color."""
    return jsonify(ruleta.girar())


@api_bp.post("/dados")
def api_dados():
    """Tira los dados indicados por ``cantidad`` y ``caras``."""
    cantidad = request.args.get("cantidad", default=2, type=int)
    caras = request.args.get("caras", default=6, type=int)
    return jsonify(dados.tirar(cantidad=cantidad, caras=caras))


@api_bp.post("/moneda")
def api_moneda():
    """Lanza la moneda y devuelve ``cara`` o ``cruz``."""
    return jsonify(moneda.lanzar())
