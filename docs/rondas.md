# Rondas

Lo que se pidió en cada ronda y qué se hizo. Todo el 15 de octubre de 2026, con Claude.

## Punto de partida

Una versión hecha con ChatGPT (`Documents/Codex/2026-10-14/c`) que se sentía superficial y muy literal. Se revisó junto con el reporte de MMM #2 (2018) y la tesis *Designable Religion*. Se tomó la ruta de las operaciones de diseño, con un toque de colección que crece (la concha). Material: los dibujos de `__INVENTORY/Scans/Originales` y `Catálogo`.

## V1

Cuatro discos de dibujos, tres piezas, un ídolo, una concha que acumula. Decisiones: la concha se cierra con 7 tareas en una efigie con tarjetas (algún día, una versión física); Claude escoge las imágenes primero.

## V2

- Todo monocromo; imágenes curadas.
- Lecturas simbólicas y culturales reales (la flor del inframundo, la calavera memento mori).
- Tareas nuevas con más fondo, a partir de las unidades rituales de Wallace.
- Ensamble modular, con el *monomito* de Dr. Lakra (kurimanzutto, 2015) como referencia.

## V3

- Etapas separadas: mesa, máquina, ídolo, lectura, concha.
- Modo místico paralelo.
- Grosor de línea parejo.
- Relación visible entre lo que escoges y los discos (hilos).
- La concha crece.
- La efigie más exótica y menos diagrama.

## V4

- Sin rosa; el naranja del Supermenú (#FF5E39) y líneas más delgadas.
- Estética del Shubyrinth: letra de píxel, sombras duras, diálogos de borde doble.
- Las piezas con identidad: epítetos ("la Oreja que oye de lado").
- La mesa explica para qué sirve escoger tres.
- El ídolo dice un mensaje y la lectura lo interpreta.
- Tres vueltas con sentido: para ti, para alguien cerca, para alguien que ya no está.
- La concha explicada.

## V5

- Música propia y sonidos, aprendidos del Shubyrinth.
- El recorrido: en cada vuelta pegas o no; al final, altar, lectura de toda la tirada y la concha como cierre, con los ídolos cayendo en la espiral.
- Más rareza: nombres nuevos (San…, Nuestro…, la parte dueña del cuerpo), mutaciones (gemelo, enjambre, corona).
- Los mensajes como poesía concreta.

## V5.1

- De lo raro a la tarea: el botón "Descifrar" en cada ídolo y, en la lectura, "en claro ↓" con la tarea en pasos numerados.
- Lo demás plegado.

## V5.2

- La efigie de cada tirada (decisión 1b). Las efigies de la tirada se guardan en la concha. La grande sigue saliendo con 7 tareas hechas.
- La música vuelve a re fuera de las vueltas.
- Carpeta local en `_GAME/mmm3` (decisión 2b).
- Repositorio en GitHub (decisión 3b).
- Specs de escaneo.

## V5.3

- "Descifrar" ya no tapa el mensaje del ídolo: va debajo, como botón.
- La tarea ocupa toda la pantalla al descifrarla, con el mensaje en clave arriba y "Volver al ídolo" o "Pegarlo en la concha".
- En la lectura, la tarea es una franja negra de lado a lado, con letra grande.

## V5.4

- Pantalla de bienvenida, a partir del video *Cosmorama* (2018) como referencia: cielo estrellado, los dibujos como constelaciones que se llaman de tres en tres y luego la máquina los jala a sus cuatro anillos. Debajo, la historia en cinco frases y "Encender la máquina" (que también enciende la música). Se puede saltar; el logo MMM#3 la vuelve a abrir.

## V5.5

- En la máquina, cada pieza dice algo al pasar el cursor o al tocarla: un acertijo, un conjuro o una opinión (`dicho` en `data.json`).
- "Otra vuelta" es el doble de grande. Los botones principales llevan sombra naranja; así "Ver el ídolo" ya no se ve desalineado.
- "Cerrar la tirada" cambió a "Ver mis ídolos juntos" (después de la tercera vuelta) y "Ya no quiero más vueltas" (antes).
- Las tareas ya no son todas pasos: cada una tiene su forma (`TF` en la plantilla): pasos, un minuto, siete días, receta, hoja de exvoto, horario de un día, tres noches, regla, contador de 108, guion de pregunta, mañana con líneas en blanco.
- La concha explica su ciclo en tres pasos, tiene "Hacer otra tirada" y, en cada ídolo, "Ver la tarea", "La hice" y "La transformé". Al marcar una tarea sale un aviso con cuántas faltan. Los ídolos pendientes se ven más; los nuevos caen en la vuelta de afuera de la espiral.

## V5.6

- La rueda de la máquina ahora gira por script (el atributo `transform` del SVG) en vez de una transición de CSS, que en algunos navegadores no se animaba.

## V5.7

- Los escaneos de texturas (carpeta `sin-clasificar`) entran como un quinto elemento: el **fondo**. Son 29 texturas en `source/fondos/` (tinta negra con transparencia, 900 px, más una muestra chica de 160 px en `fondos/s/`).
- Cada vuelta escoge un fondo por atributos (como las piezas, con su propio azar) y una forma de nicho: arco, aureola, mandorla, piso o retablo. La textura rellena el nicho y deja un margen blanco alrededor del ídolo, así nunca tapa el dibujo.
- La rueda tiene un anillo de afuera con las muestras de fondo. También hablan al pasar el cursor.
- La efigie de la tirada y la grande llevan su textura en una mandorla. Las tarjetas tienen reverso con la textura.
- Las piezas no cambiaron, así que los ídolos guardados siguen siendo los mismos; solo ganan su fondo.

## V5.8

- Versiones de datos (`V`, `v`, `out`): sumar o retirar piezas ya no cambia los ídolos guardados. Cada tirada e ídolo guardan su versión. `build.py` cuida que nada de una versión vieja cambie (`source/versiones.json`).
- La rueda tiene lugares fijos por anillo, listos para cuando haya más piezas.

## V5.9 · datos versión 2

- 21 piezas nuevas de los escaneos (decisión 2a), todas con `"v": 2`:
  - Cuerpos: Oso, Calaca dentona, Cochinito, Gato de cuatro manos, Cíclope, Hombre caracol, Panzón de ojos, Luna, Sombra doble, Gólem, Pulpo.
  - Partes: Mano y Pie (más finos; reemplazan a los de plumón, que quedan con `"out": 2`), Boca, Brazo, Cuerno.
  - Materia: Cristal, Tocón, Copal (halo), Piedra cosida.
  - Signos: Eclipse.
- Los ídolos guardados antes siguen igual: se calculan con la versión 1.
- Scripts de recorte en `scripts/escaneos/`.

## V6.0

- La concha ahora se llama **xenófora** en todo el texto (la palabra concha tiene otro sentido en varios países). Las llaves internas (`mmm3-concha-v2`, `data-step="concha"`) no cambian, así nadie pierde lo guardado.
- Bienvenida: primero una pantalla negra con "Entrar" (o "Entrar sin sonido"), porque el navegador solo deja sonar algo después de un toque. Luego suena su propia pieza (`MU_IN`: la primera frase de la melodía A, a la mitad de velocidad, con bajo sostenido y campanas lentas). Las frases salen al centro, palabra por palabra con una campana cada una, y se deshacen antes de la siguiente. Al final los dibujos caen a la rueda y aparece MMM#3 con "Encender la máquina", que cambia a la música de siempre.
- La xenófora muestra **siete lugares**: cada tarea hecha llena uno con su ídolo; el octavo es la efigie. Debajo, una frase dice cuántas faltan y cuántos ídolos esperan. El ciclo explica que cada tirada da hasta tres ídolos y que lo que cuenta son las tareas.
- El menú muestra `V Xenófora 2/7` (tareas hechas) en lugar del número de ídolos. El aviso al pegar dice que la tarea cuenta cuando la hagas.
- Visor grande para la efigie, las tarjetas y las efigies de tirada: con anterior, siguiente y "Guardar imagen".
- El anillo de fondos muestra 12 muestras redondas y tenues; solo la que sale se ve completa.

## Pendiente

- Cabezas de las hojas con fondo negro (39, 40, 120, 121): ¿disco nuevo?
- Más recortes: signos de la hoja 8, manos de la 28, caras de la 37.
- Recortes de textura como piezas sueltas (peanas, piedras, nubes).
- ¿Cruzar las tareas con las de Shubidubi? Opción con más peso: casi todas propias y, de vez en cuando, una hoja de Shubidubi.
- Versión física algún día: impresa, por correo o en un cuarto.
