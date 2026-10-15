# Escaneos: cómo entran dibujos nuevos

Los recortes de hoy salen de escaneos viejos y miden en promedio 413 px en su lado largo (el más grande, 900 px). En pantalla se ven bien chicos, pero se ven suaves en el ídolo grande, en la efigie y en las tarjetas impresas. Con escaneos nuevos se pueden rehacer las piezas actuales y sumar otras.

## Specs

- **600 dpi**, escala de grises de 8 bits.
- **TIFF o PNG.** Sin JPG.
- Sin "auto mejora", sin enfoque automático y sin quitar polvo. La misma configuración toda la sesión.
- Escáner de cama, tapa cerrada, papel plano.
- Cada dibujo debe quedar de **al menos 1500 px** en su lado largo. A 600 dpi eso es un dibujo de 6.5 cm o más. Si el dibujo es más chico, escanea a 1200 dpi.
- Tinta negra sobre papel blanco. El lápiz y las aguadas sirven si quieres esa textura, pero se limpian peor.
- Varios dibujos por hoja está bien si dejas **1 cm de blanco** entre ellos. El script los separa.

## Qué dibujos le sirven a la máquina

| Carpeta | Qué va | Cómo conviene dibujarlo |
|---|---|---|
| `escaneos/cuerpos/` | figuras | de frente, completas, de pie o sentadas |
| `escaneos/partes/` | milagritos: partes del cuerpo, órganos, objetos de promesa | sueltos, que se lean solos |
| `escaneos/materia/` | peanas, bases, nubes, piedras, resplandores | con la parte de arriba plana para que algo se pare encima |
| `escaneos/signos/` | signos, glifos, marcas | que quepan en un cuadrado |
| `escaneos/sin-clasificar/` | lo que no sepas dónde va | |

Hoy el disco más corto es materia (9 piezas). La meta es unas 20 por disco.

## Nombres

Con el nombre de lo que es, si lo sabes: `xolotl.tif`, `pie-del-camino.tif`. Si es una hoja con varios: `hoja-01.tif`. Si es un dibujo que ya está en la máquina (para rehacerlo con más calidad), pon su `id` en el nombre: `059_033-xolotl.tif`.

## Qué pasa después

1. Se cortan los dibujos de cada hoja, se les quita el fondo y se normaliza el grosor de línea (ver `scripts/historico/segment_hi.py` y `lineweight.py`).
2. Cada pieza nueva recibe su `id`, su disco, tres atributos, su nombre, su epíteto, su lectura y su fuente cultural en `source/data.json`.
3. Se exporta a `source/pieces/<id>.webp` y se corre `python3 build.py`.

Los pasos 1 y 2 los hace Claude con tus escaneos; tú revisas los nombres, las lecturas y las fuentes.
