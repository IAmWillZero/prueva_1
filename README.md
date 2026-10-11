# prueva_1 🎲

Aplicación web de **sorteos** hecha con **Python + Flask**. Incluye tres juegos
de azar con un frontend ligero en HTML, CSS y JavaScript:

- **Ruleta** europea (números del 0 al 36 con su color).
- **Dados** configurables (cantidad y número de caras).
- **Cara o Cruz**.

## Arquitectura

```
prueva_1/
├── app/
│   ├── __init__.py          # Fábrica de la app Flask (create_app)
│   ├── routes.py            # Rutas web (páginas HTML)
│   ├── api.py               # Endpoints JSON que resuelven los sorteos
│   ├── games/               # Lógica pura de cada juego
│   │   ├── ruleta.py
│   │   ├── dados.py
│   │   └── moneda.py
│   ├── templates/           # Plantillas Jinja2
│   │   ├── base.html
│   │   └── index.html
│   └── static/              # Recursos del cliente
│       ├── css/style.css
│       └── js/app.js
├── tests/
│   └── test_games.py        # Pruebas de la lógica (unittest)
├── run.py                   # Punto de entrada del servidor
├── requirements.txt
└── README.md
```

La idea central es separar **lógica de negocio** (`app/games/`) del **transporte
HTTP** (`app/api.py` y `app/routes.py`). Los módulos de `games` son funciones
puras sin estado, lo que los hace fáciles de probar y reutilizar.

## Requisitos

- Python 3.10 o superior.
- Las dependencias de `requirements.txt` (Flask).

## Puesta en marcha

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
# venv\Scripts\activate.bat       # Windows (CMD)
# source venv/bin/activate        # Linux / macOS

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Arrancar el servidor
python run.py
```

Después abre <http://127.0.0.1:5000> en el navegador.

## API

| Método | Ruta            | Descripción                                  |
| ------ | --------------- | -------------------------------------------- |
| POST   | `/api/ruleta`   | Gira la ruleta.                              |
| POST   | `/api/dados`    | Tira dados (`?cantidad=&caras=`).            |
| POST   | `/api/moneda`   | Lanza la moneda.                             |
| GET    | `/health`       | Comprueba que el servidor responde.          |

Ejemplos de respuesta:

```json
// POST /api/ruleta
{ "numero": 17, "color": "negro" }

// POST /api/dados?cantidad=3&caras=6
{ "dados": [4, 1, 6], "total": 11, "caras": 6 }

// POST /api/moneda
{ "resultado": "cara" }
```

## Pruebas

```bash
python -m unittest discover -s tests
```

## Licencia

MIT.
