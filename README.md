# Meaning Making Machine #3

Una xenófora que cambia con lo que haces. La xenófora es tu casa: ahí esperan los ídolos que te llevas. Para conseguir uno visitas la máquina: escoges tres piezas dibujadas, cuatro discos giran y sale un ídolo que te propone un gesto en clave, como un poema concreto. Si te lo llevas, espera en tu xenófora. Cuando haces su gesto (o lo cambias a tu manera) dejas una huella y la xenófora crece. Con siete gestos se transforma en una efigie con siete tarjetas.

Es la tercera versión de la Meaning Making Machine (MMM #2: Imperial College London / Royal College of Art, 2018). Está hecha con dibujos propios de Alejandro Ramos Saavedra (inventario de originales 2020–2023), las operaciones de [Actionary](https://operations.ramos-saavedra.com) y las unidades rituales de Anthony F. C. Wallace.

## El recorrido

La xenófora es el lugar de regreso; la máquina es un lugar que visitas.

0. **Bienvenida** (solo la primera vez; el logo la vuelve a abrir). Con o sin sonido. Del cielo al mar en ocho frases: las constelaciones de dibujos, la máquina, el mar y la xenófora. Se ve qué le pasa a una xenófora: llega un ídolo en espera, un gesto lo integra y la hace crecer, siete gestos la transforman. Termina en "Ver mi xenófora".
1. **Tu xenófora.** La espiral con tus ídolos, siete lugares y una frase que dice qué sigue. Si hay un ídolo en espera, la acción principal es hacer su gesto. Al volver otro día, la página abre aquí.
2. **Visitar la máquina.** Escoges tres piezas, los discos giran y sale un ídolo **descubierto**. "Llevármelo a mi xenófora" o "Dejarlo aquí". La primera visita es de una vuelta; después de tu primer gesto puedes pedir tres (para ti, para alguien cerca, para alguien que ya no está), que terminan en un altar con la efigie de la visita.
3. **En espera.** De vuelta en la xenófora, el ídolo llega como fantasma, con borde punteado. "Ver su propuesta" muestra el poema, la tarea en claro y, plegado, cómo lo juntó la máquina.
4. **Integrado.** "La hice" o "La transformé" abren "Deja un rastro" (escribir, dibujar o foto, opcional). La espiral se entinta un séptimo más, el ídolo se vuelve sólido y su rastro queda prendido junto a él.
5. **Metamorfosis.** Con siete gestos, la xenófora se transforma en la efigie grande, con siete tarjetas para compartir, descargar o imprimir.

Hay dos modos: **Místico** (negro, con menos explicación; es el que sale al principio) y **Explicado**. Hay música y sonidos, hechos por el navegador, con botones para apagarlos.

Hay dos idiomas: español e inglés. El botón **EN / ES** de la barra (y "English / Español" en la bienvenida) cambia de idioma; también `?lang=en` o `?lang=es` en la dirección. Si nadie escogió, sale el idioma del navegador. El idioma no cambia los ídolos: la máquina decide con ids y atributos.

## Archivos

- `source/template.html` es la página entera: estilos, marcado y código. Lleva el marcador `__DATA__` donde entra `data.json`.
- `source/en.json` tiene las fichas en inglés: piezas, fondos, operaciones y tareas, por id. Los poemas y las hojas de tarea en inglés están en la plantilla (`POEMS_EN`, `TF_EN`). `build.py` se detiene si falta algo en inglés.
- `source/data.json` tiene las piezas, las operaciones, las tareas y qué tareas trae cada disco. Ver `docs/datos.md`.
- `source/img/` tiene las dos vistas de la xenófora real (escaneo 3D del Smithsonian, dominio público).
- `source/fondos/` tiene las texturas de los nichos (900 px) y en `fondos/s/` sus muestras para la rueda.
- `source/pieces/` tiene un recorte `.webp` por pieza, con fondo transparente, nombrado con su `id`.
- `build.py` arma `site/` (la página con los datos adentro y las imágenes). Revisa que cada pieza tenga imagen y que cada tarea tenga poema.
- `site/` es lo que se publica: `site/index.html` y `site/p/`.
- `escaneos/` es donde entran los dibujos nuevos. Ver `docs/escaneos.md`.
- `scripts/historico/` tiene los scripts que se usaron para cortar y limpiar el primer juego de piezas. Están como se usaron, con rutas de esa sesión. Sirven de referencia y hay que adaptarlos antes de volver a usarlos.
- `docs/` tiene cómo decide la máquina, la música, los datos, los escaneos y las rondas de cambios.

## Cómo trabajar

```
python3 build.py
```

Después de cualquier cambio en `source/`. Para verla, abre `site/index.html` con un servidor local (las imágenes no cargan desde `file://` en todos los navegadores):

```
cd site && python3 -m http.server 8000
```

y abre http://localhost:8000.

La página pública vive en https://mmm.ramos-saavedra.com: GitHub Pages publica la carpeta `site` cada vez que cambia y se sube a GitHub (`.github/workflows/pages.yml`). El dominio apunta a GitHub desde la configuración de DNS en Squarespace (registro CNAME `mmm` → `alexo000.github.io`). El código vive en github.com/Alexo000/mmm3 (público). También hay una copia privada como artifact en Claude.

## Qué se guarda

La xenófora, las tiradas y los modos se guardan solo en el navegador de quien la usa (`localStorage`, claves `mmm3-concha-v2`, `mmm3-mode`, `mmm3-music`, `mmm3-sounds`, `mmm3-welcome`, `mmm3-lang`). No se manda nada a ningún lado.

Si otra persona va a usar el mismo navegador, abajo en la xenófora está "Borrar y empezar de cero" (pide confirmar). Borra todo lo de MMM #3 en ese navegador, menos el idioma, y vuelve a la bienvenida.
