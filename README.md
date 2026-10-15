# Meaning Making Machine #3

Una máquina para pedir algo que hacer. Llamas a tres piezas dibujadas, la máquina da tres vueltas y en cada vuelta arma un ídolo con cuatro discos de dibujos. Cada ídolo te dice una tarea en clave, como un poema concreto. Si te lo llevas, se pega a tu concha. Al final de la tirada sale una efigie con sus ídolos fundidos, y la lectura te dice cada tarea en claro y por qué te tocó. Con siete tareas hechas, la concha se cierra y te da una efigie grande con siete tarjetas.

Es la tercera versión de la Meaning Making Machine (MMM #2: Imperial College London / Royal College of Art, 2018). Está hecha con dibujos propios de Alejandro Ramos Saavedra (inventario de originales 2020–2023), las operaciones de [Actionary](https://operations.ramos-saavedra.com) y las unidades rituales de Anthony F. C. Wallace.

## El recorrido

1. **Llamado.** Escoges tres piezas de la mesa. El disco que nadie llamó es de donde vendrá lo extraño.
2. **Máquina.** Cuatro discos giran. Los hilos muestran qué atributo de tus piezas jaló a cada pieza nueva.
3. **Ídolos.** Uno por vuelta: para ti, para alguien que tienes cerca, para alguien que ya no está. El ídolo dice su tarea como poema. "Descifrar" la muestra en claro, en pasos. "Pegarlo en la concha" se lo lleva.
4. **La tirada está completa.** Los ídolos juntos en un altar y la efigie de la tirada.
5. **Lectura.** Cada mensaje, su tarea en pasos y por qué te tocó.
6. **Concha.** Los ídolos pegados, en gris mientras su tarea está pendiente. Marcas "La hice" o "La transformé". Siete hechas cierran la concha.

Hay dos modos: **Explicado** y **Místico** (negro, con menos explicación). Hay música y sonidos, hechos por el navegador, con botones para apagarlos.

## Archivos

- `source/template.html` es la página entera: estilos, marcado y código. Lleva el marcador `__DATA__` donde entra `data.json`.
- `source/data.json` tiene las piezas, las operaciones, las tareas y qué tareas trae cada disco. Ver `docs/datos.md`.
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

La versión publicada vive como artifact privado en Claude. El código vive en github.com/Alexo000/mmm3.

## Qué se guarda

La concha, las tiradas y los modos se guardan solo en el navegador de quien la usa (`localStorage`, claves `mmm3-concha-v2`, `mmm3-mode`, `mmm3-music`, `mmm3-sounds`). No se manda nada a ningún lado.
