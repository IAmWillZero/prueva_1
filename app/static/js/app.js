// Interfaz del cliente: llama a la API y pinta los resultados de cada sorteo.

const ENDPOINTS = {
    ruleta: '/api/ruleta',
    dados: '/api/dados',
    moneda: '/api/moneda',
};

/** Realiza una petición POST y devuelve el JSON resultante. */
async function pedir(url) {
    const respuesta = await fetch(url, { method: 'POST' });
    if (!respuesta.ok) {
        throw new Error(`El servidor respondió ${respuesta.status}`);
    }
    return respuesta.json();
}

/** Sustituye el contenido de la caja de resultado de un juego. */
function pintar(juego, html) {
    document.querySelector(`[data-resultado="${juego}"]`).innerHTML = html;
}

function pintarRuleta(datos) {
    pintar(
        'ruleta',
        `<div>
            <div class="destaque">${datos.numero}</div>
            <div class="detalle">
                <span class="badge ${datos.color}">${datos.color}</span>
            </div>
        </div>`,
    );
}

function pintarDados(datos) {
    const fichas = datos.dados.map((valor) => `<span class="dado">${valor}</span>`).join('');
    pintar(
        'dados',
        `<div>
            <div class="dados-pista">${fichas}</div>
            <div class="detalle">Total: <strong>${datos.total}</strong> (d${datos.caras})</div>
        </div>`,
    );
}

function pintarMoneda(datos) {
    const icono = datos.resultado === 'cara' ? '🪙' : '🌚';
    pintar(
        'moneda',
        `<div>
            <div class="destaque">${icono} ${datos.resultado}</div>
        </div>`,
    );
}

const PINTORES = {
    ruleta: pintarRuleta,
    dados: pintarDados,
    moneda: pintarMoneda,
};

/** Gestiona el clic de un botón de sorteo. */
async function lanzarSorteo(juego, boton) {
    boton.disabled = true;
    try {
        let url = ENDPOINTS[juego];
        if (juego === 'dados') {
            const cantidad = document.querySelector('[data-campo="cantidad"]').value;
            const caras = document.querySelector('[data-campo="caras"]').value;
            url += `?cantidad=${encodeURIComponent(cantidad)}&caras=${encodeURIComponent(caras)}`;
        }
        const datos = await pedir(url);
        PINTORES[juego](datos);
    } catch (error) {
        pintar(juego, `<span class="error">Error: ${error.message}</span>`);
    } finally {
        boton.disabled = false;
    }
}

document.querySelectorAll('[data-accion]').forEach((boton) => {
    boton.addEventListener('click', () => lanzarSorteo(boton.dataset.accion, boton));
});
