"""Rutas web que sirven la interfaz del juego."""

from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Devuelve la página principal con los tres juegos de sorteo."""
    return render_template("index.html")


@main_bp.route("/health")
def health():
    """Endpoint sencillo para comprobar que el servidor está vivo."""
    return {"status": "ok"}
