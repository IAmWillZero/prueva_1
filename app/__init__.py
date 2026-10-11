"""Fábrica de la aplicación Flask para el proyecto de sorteos."""

from flask import Flask

from .api import api_bp
from .routes import main_bp


def create_app() -> Flask:
    """Crea y configura una instancia de la aplicación Flask."""
    app = Flask(__name__)

    # Página principal (interfaz web).
    app.register_blueprint(main_bp)

    # Endpoints JSON que resuelven los sorteos.
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
