# source/data.json

## `P`: piezas

| Campo | Qué es | Ejemplo |
|---|---|---|
| `id` | hoja y número del recorte; también el nombre de la imagen | `059_033` |
| `d` | disco: `cuerpos`, `partes`, `materia`, `signos` | `cuerpos` |
| `a` | tres atributos del vocabulario SFDIS | `["intrigante","ingenioso","organico"]` |
| `n` | nombre corto | `Xólotl` |
| `art` | con artículo, para frases | `el xólotl` |
| `de` | con "de", para nombres de ídolos | `del xólotl` |
| `ep` | epíteto: la identidad de la pieza | `Xólotl, el que cruza el río` |
| `lec` | lectura simbólica, una frase | `El perro que acompaña a los muertos a cruzar el río.` |
| `src` | práctica real de donde viene | `Xólotl y el xoloitzcuintle en el camino al Mictlán, tradición mexica.` |
| `x` | en partes: lo que pides (infinitivo); en materia: `base` o `halo` | `ver claro lo que piensas` |
| `w`, `h` | tamaño en px de la imagen | |
| `dicho` | lo que dice en la máquina: tipo (`a` acertijo, `c` conjuro, `o` opinión) y texto | `["a", "Tengo cuatro patas…"]` |

## `O`: operaciones de ensamble (14, de Actionary)

`slug`, `es`, `en`, `rule` (la regla corta), `aff` (atributos afines), `como` (cómo se armó, con huecos `{cuerpo}`…), `svg` (su símbolo).

## `T`: tareas (14, unidades rituales de Wallace)

`u` (unidad), `t` (la tarea en claro, con huecos `{pide}`, `{parte}`, `{cuerpo}`, `{materia}`, `{signo}`), `f` (de dónde viene). Cómo se ve cada tarea en pantalla (pasos, receta, siete días…) está en `TF` dentro de la plantilla. El campo `o` es la frase de oráculo de la versión 4; ya no se usa porque ahora el ídolo habla con los poemas de `POEMS` en la plantilla.

## `U`: qué tareas trae cada disco

Una lista por disco. Una tarea puede repetirse para pesar más.

## `F`: fondos (texturas)

`id` (hoja y número de la textura; también el nombre de `source/fondos/<id>.webp` y de la muestra `source/fondos/s/<id>.webp`), `n` (nombre con artículo: "la Malla"), `ep` (de qué está hecho el nicho), `a` (tres atributos), `lec` (lectura), `dicho` (lo que dice en la rueda).

## Versiones: `V`, `v` y `out`

Un ídolo guardado en la concha se vuelve a calcular cada vez que se ve. Si cambian las piezas, cambiaría. Para que no pase:

- `V` (arriba en `data.json`, 1 si falta) es la versión actual de los datos.
- Cada pieza, operación, fondo o tarea nueva lleva `"v"` con la versión en la que entra. Sin `v` cuenta como 1.
- Para quitar algo (una pieza tosca que se reemplaza) no se borra: se le pone `"out"` con la versión en la que sale. Sigue existiendo para los ídolos viejos.
- En `U`, una tarea que se suma a un disco en una versión nueva se escribe `"nombre@2"`.
- Cada tirada y cada ídolo guardado recuerdan su versión. Los de antes de esto cuentan como 1.
- `build.py` guarda en `source/versiones.json` todo lo que decide los ídolos de cada versión (ids, atributos, orden). Si algo de una versión vieja cambia, el build falla y explica qué hacer. No edites ese archivo a mano.
- La rueda tiene un número fijo de lugares por anillo (`CAP` en la plantilla). Con más piezas que lugares muestra una mezcla, y la pieza que sale toma un lugar antes de girar.

## Para sumar una pieza

1. Pon la imagen en `source/pieces/<id>.webp` (fondo transparente, tinta negra).
2. Agrega su entrada en `P` con todos los campos y `"v"`: la versión nueva (sube `V` si es la primera cosa nueva de esta ronda).
3. `python3 build.py`.
