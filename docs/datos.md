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

## Para sumar una pieza

1. Pon la imagen en `source/pieces/<id>.webp` (fondo transparente, tinta negra).
2. Agrega su entrada en `P` con todos los campos.
3. `python3 build.py`.
