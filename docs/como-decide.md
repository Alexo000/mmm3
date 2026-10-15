# Cómo decide la máquina

Todo sale de `run(picks, spin)` en `source/template.html`. Es determinista: las mismas tres piezas y la misma vuelta dan siempre el mismo ídolo, en cualquier navegador. La semilla sale de los `id` de las piezas ordenados y del número de vuelta.

## Los cuatro discos

| Disco | Papel en el ídolo | Piezas hoy |
|---|---|---|
| I Cuerpos | la figura | 14 |
| II Partes | el milagrito prendido (y lo que pides) | 14 |
| III Materia | la peana, o un resplandor detrás | 9 |
| IV Signos | la inscripción | 14 |

## Una vuelta

1. **Tu perfil.** Se suman los atributos de tus tres piezas. Los atributos vienen del vocabulario que la SFDIS recogió para MMM #2 (2018): orgánico, táctil, secreto, efigioso…
2. **La regla rota.** De los discos que nadie llamó se escoge uno. En ese disco sale la pieza que *menos* se parece a tu perfil. Pascal Boyer: lo que viola un poco el sentido común es lo que se recuerda.
3. **Los demás discos.** En cada uno sale la pieza que más atributos comparte con tu perfil, con algo de azar. Los hilos de la máquina muestran qué atributo la jaló.
4. **Sin repetir.** En la vuelta II y III no salen piezas ni tareas que ya salieron en las vueltas anteriores de la misma tirada.
5. **El ensamble.** Una de 14 operaciones de Actionary decide cómo se unen las piezas (injertar, contener, reflejar, partir a la mitad, ocultar…). Gana la que más afinidad tiene con los atributos de todo el ídolo, con algo de azar.
6. **La mutación.** A veces el ídolo trae algo de más: un gemelo chico, su signo regado como enjambre o una corona de tres milagritos.
7. **El nombre.** Siete formas: "Xólotl del cerebro", "San Mr. Ketchup de la bendición", "Huevo de Cada Hombre" (la parte se vuelve dueña del cuerpo), "Nuestra…", "Divino…", con materia o con signo.
8. **La tarea.** Sale de las unidades rituales de Wallace (*Religion: An Anthropological View*, 1966). Cada disco trae ciertas tareas (`U` en `data.json`) y las piezas que llamaste pesan más. La tarea se llena con lo que pide el milagrito (`{pide}`), la figura (`{cuerpo}`), la materia y el signo.
9. **El poema.** Cada tarea tiene un poema concreto en `POEMS` (dentro de la plantilla): un acomodo de palabras en una página de 400 × 300. El ídolo lo dice palabra por palabra.

## Las tres vueltas

| Vuelta | Para quién | Música |
|---|---|---|
| I | para ti | en re |
| II | para alguien que tienes cerca | una cuarta arriba |
| III | para alguien que ya no está | una cuarta abajo y más lenta |

## La concha y las efigies

- Cada ídolo que te llevas se pega en una espiral (la *Xenophora* pega a su concha lo que encuentra). Pendiente se ve en gris; hecha, en negro; transformada, volteada.
- Al terminar cada tirada sale la **efigie de la tirada**: sus ídolos apilados, los milagritos como brazos, los signos tallados en la peana. Se guarda en la concha.
- Con **siete tareas hechas** la concha se cierra: sale la efigie grande de siete ídolos y siete tarjetas de 10 × 15 cm con el ídolo, su nombre y su poema.
