# Notas para trabajar en MMM #3

- Lee `README.md` y `docs/` antes de cambiar algo.
- La página es un solo archivo: `source/template.html`. Los datos están en `source/data.json`. Después de cualquier cambio: `python3 build.py`. No edites `site/` a mano.
- Escribe en español de México, en lenguaje sencillo. Sin guiones largos.
- Todo es blanco y negro y grises. El naranja #FF5E39 se usa solo para lo que escogiste, la regla rota y una palabra de cada poema.
- La letra de píxel es VT323; el texto corrido, Inter; los datos, IBM Plex Mono.
- La máquina tiene que ser determinista: mismas piezas y misma vuelta dan el mismo ídolo. Si cambias `run()`, cambian los ídolos ya guardados en las conchas de la gente.
- Cada tarea necesita su poema en `POEMS`; `build.py` lo revisa.
- Anota cada ronda de cambios en `docs/rondas.md`.
