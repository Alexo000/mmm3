# Notas para trabajar en MMM #3

- Lee `README.md` y `docs/` antes de cambiar algo.
- La página es un solo archivo: `source/template.html`. Los datos están en `source/data.json`. Después de cualquier cambio: `python3 build.py`. No edites `site/` a mano.
- Escribe en español de México, en lenguaje sencillo. Sin guiones largos.
- Todo es blanco y negro y grises. El naranja #FF5E39 se usa solo para lo que escogiste, la regla rota, una palabra de cada poema, la sombra de los botones principales y los números de las tareas.
- La letra de píxel es VT323; el texto corrido, Inter; los datos, IBM Plex Mono.
- La máquina tiene que ser determinista: mismas piezas y misma vuelta dan el mismo ídolo. Si cambias `run()`, cambian los ídolos ya guardados en las conchas de la gente.
- Cada tarea necesita su poema en `POEMS` y en `POEMS_EN`, y su hoja en `TF` y `TF_EN`; `build.py` lo revisa.
- Hay versión en inglés (inglés británico): cada pieza, fondo, operación y tarea necesita su ficha en `source/en.json`. Los textos de la plantilla van con `L('español','English')` o con `data-en` en el marcado.
- Anota cada ronda de cambios en `docs/rondas.md`.
