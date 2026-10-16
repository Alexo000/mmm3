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

- Catálogo aparte (página de Claude, privada) con las 72 piezas de la máquina y 526 recortes de 31 hojas, para escoger qué entra, a qué disco, qué sale y cómo se gira. Lo que se marca queda en la base de datos del catálogo y Claude lo lee para la siguiente versión. Las hojas de contacto salen de `scripts/escaneos/` (en la Mac quedan en `escaneos/_contacto/catalogo/`).

## V6.1 · a partir de la revisión de ChatGPT

- **Tu llamado es tuyo.** La mesa empieza vacía, con tres lugares arriba. Una cuarta pieza ya no desplaza a la primera: la máquina avisa y cada lugar tiene ✕. "Ver un ejemplo" llena las tres del ejemplo. Entrada nueva: "Elige tres piezas que te llamen" y una frase; lo demás va en "Cómo funciona", plegado.
- **La tirada queda congelada.** Máquina, ídolos y lectura muestran arriba "Tirada de A · B · C". Si cambias las piezas en la mesa, se avisa que la tirada anterior sigue guardada.
- **Responder al oráculo.** La lectura tiene tres capas: 1) cómo juntó la máquina las piezas (regla comprobable), 2) qué propone el ídolo, 3) para ti, esto es: "Me resuena", "Lo leo de otra manera" (con nota opcional) o "Lo dejo pasar". También en la tarea a pantalla completa. Se guarda por ídolo (`store.resp`).
- "Lo que pides" pasa a "La máquina propone que pidas…". El botón dice "Descifrar: ¿qué me propone?".
- **La transformé** pide, sin obligar, "¿Qué hiciste a tu manera?". La nota y la respuesta salen en la xenófora y en la tarjeta ("Yo encontré", "A mi manera"); una tarea transformada lleva una costura en la tarjeta.
- **Xenófora:** si hay una tarea pendiente, la acción principal es hacerla; "Hacer otra tirada" pasa a segundo plano. El menú separa ídolos y gestos (`3 · 1/7`). Botones para descargar la efigie, imprimir las tarjetas (A4 horizontal, dos por hoja) y guardar o recuperar la xenófora en un archivo.
- **Acceso:** las piezas de la rueda se enfocan con teclado y dicen su dicho; cada pantalla pone el foco en su título; la tarea devuelve el foco al cerrarse; botones de 44 px en pantallas táctiles; "Leer como texto" para el poema; la ayuda se ve también en Místico.
- **Textos:** el menú ya no usa números romanos (quedan solo para los discos). La ayuda nombra los discos con su papel, explica que el fondo se escoge aparte, presenta a Boyer y a Wallace como marcos de la obra, y separa la lectura del autor de la referencia cultural. La pieza "Concha" ahora se llama "Xenófora".
- **Bienvenida:** dice qué añade el sonido y que sin sonido el recorrido es el mismo; un toque, espacio o flecha avanza a la siguiente frase.

- Recortes rehechos (`scripts/escaneos/seg2.py`): primero grupos finos de tinta; los pedacitos chicos (ojos, migajas, una mano suelta de menos de 1 cm) se unen al cuerpo más cercano; un cuerpo que cae casi todo dentro de otro se une a él; dos cuerpos grandes no se juntan; se guarda cada trazo que cae al menos 70 % dentro de la figura; se descartan marcos de página, grupos enormes y trazos de lápiz muy tenues. Quedaron 474 recortes; los 18 que ya están en la máquina no se repiten. Las hojas muy apretadas (6, 26, 27, 30) todavía dan grupos.

## V6.2 · rastros (decisión 1c)

- Al marcar "La hice" o "La transformé" se abre "Deja un rastro", opcional: escribir, dibujar con el dedo o el ratón, o subir una foto (se pasa a grises y se reduce a 1100 px). "Marcar sin rastro" marca sin nada. En una tarea hecha, "Tu rastro" deja verlo o cambiarlo.
- El texto queda en la entrada (`nota`); el dibujo y la foto quedan en IndexedDB (`mmm3` → `rastros`, llave = la del ídolo). Nada sale del navegador.
- El rastro sale en la xenófora (miniaturas), en la tarjeta (prendido como foto de exvoto, y el texto como "Lo que pasó" o "A mi manera") y en la efigie de siete: cada rastro prendido junto a su ídolo, alternando lados.
- "Guardar mi xenófora" ahora incluye los rastros (archivo versión 2); "Recuperar" los vuelve a poner.

## V6.3 · compartir (decisión 1a)

- Botón "Compartir" en cada tarea hecha (manda su tarjeta), en la efigie de la tirada, en la efigie de siete y en el visor grande. En el teléfono abre el menú de compartir del sistema (WhatsApp, correo, Instagram…) con la imagen y el enlace a mmm.ramos-saavedra.com. Donde el navegador no comparte imágenes (casi todas las computadoras), la descarga y avisa.
- Nada va a un servidor: el testimonio llega por donde la persona decida. Si en la temporada de prueba la gente comparte, el siguiente paso sería un archivo propio con aprobación (opción c).

## V7 · la xenófora al centro

Problema: competían coleccionar ídolos y hacer sus propuestas; la máquina se llevaba el espectáculo y las tareas se sentían como una condición añadida. Principio: mantener el misterio del significado y hacer comprensible cómo participar. Prueba: a los treinta segundos, ¿la persona entiende qué le puede pasar a su xenófora y cómo hacerla cambiar?

- La bienvenida ya no es el cielo: cuenta la xenófora en seis frases mientras se dibuja (espiral, un ídolo que llega en espera, un gesto que lo integra y la hace crecer, siete gestos y la metamorfosis). Termina en "Ver mi xenófora". Solo sale la primera vez.
- La xenófora es la casa: la página abre ahí y todo regresa ahí. El menú tiene dos lugares: "Tu xenófora" y "La máquina".
- La espiral es lo primero que ves, con la frase de qué sigue y las acciones al lado. Cada gesto entinta un séptimo de la espiral (desde el centro, con un nudo) y se anima al volver.
- Tres estados visibles: **descubierto** (en la máquina, "todavía no es tuyo"), **en espera** (fantasma con borde punteado) e **integrado** (sólido, doble borde, con su rastro prendido). Más la **metamorfosis** a los siete.
- Primera visita de una sola vuelta: "Llevármelo a mi xenófora" termina la visita y te devuelve a la xenófora, donde el ídolo llega. Las tres vueltas aparecen como opción en la mesa después del primer gesto.
- La lectura dejó de ser un paso: cada ídolo abre "Ver su propuesta" (poema, tarea en claro, "la máquina propone…", tu respuesta y, plegado, cómo lo juntó la máquina), con "La hice" y "La transformé" ahí mismo.
- Al volver con un gesto en espera: "Hay un gesto esperando. ¿Quieres hacerlo, cambiarlo a tu manera o dejarlo ir?". "Despegar" ahora se llama "Dejarlo ir".

## V7.1 · bienvenida: del cielo al mar

- Vuelve el cielo con las constelaciones: los dibujos aparecen como estrellas, se unen de tres en tres y la máquina los jala a sus cuatro anillos. Luego la cámara baja: el horizonte, el mar, burbujas, y siete dibujos caen hasta el fondo. Ahí vive la xenófora; uno de esos dibujos llega en espera, un gesto lo integra y la hace crecer, siete gestos la transforman. Ocho frases; un toque avanza.

## V8 · datos versión 3: tus elecciones del catálogo y el disco de devotos

- Entran 114 piezas (ids `rHHH_NN`, segunda tanda de recortes) y salen 27 (`"out": 3`). Las fichas las escribieron cuatro ayudantes con la misma guía y las revisé; la referencia cultural solo va donde hay una clara.
- Disco nuevo, **devotos**: caras y cabezas que se hincan a los pies del ídolo. Cada uno trae `cree` (lo que cree). Sale con su propio azar y solo en ídolos de la versión 3, así los de antes no cambian. En la rueda comparte el anillo de afuera con los fondos, entrelazados, y cae en una marca abajo, "a los pies". Su creencia aparece en la propuesta y en las notas de la máquina.
- Se quedó fuera un recorte (hoja 7, número 2) porque recuerda demasiado a un personaje conocido.
- El ejemplo de la mesa cambia el Cempasúchil (sale) por el Ojo de Dios.
- Las versiones 1 y 2 dan los mismos ídolos que antes (revisado con 1,182 tiradas).

## V8.1 · bienvenida sin promesa, versión en inglés y borrar sesión

- La bienvenida ya no promete significado ni describe la máquina anterior. Ahora empieza: "Desde 2018 hago máquinas. Esta junta dibujos de tres en tres. Y los pone a girar. Lo que suelta cae al mar."
- Versión en inglés (británico). Botón EN / ES en la barra y "English / Español" en la bienvenida; `?lang=en` en la dirección. Las fichas están en `source/en.json`; los poemas en `POEMS_EN` y las hojas de tarea en `TF_EN`. Los ídolos son los mismos en los dos idiomas (revisado con 1,182 tiradas); solo cambian las palabras. El nombre del ídolo en inglés usa el mismo azar: "Moustached devil of the wish ribbon and the woven grid".
- "Borrar y empezar de cero", abajo en la xenófora, con confirmación: borra la xenófora, los rastros, las respuestas y los ajustes de este navegador (menos el idioma) y vuelve a la bienvenida. Para cuando otra persona usa el mismo teléfono o computadora.
- "Cómo decide la máquina" ahora cuenta cinco discos y el devoto.
- La pantalla vieja de "La lectura" ya no se usa; quedó en español.

## V8.2 · líneas más finas en las piezas nuevas y otra salida a la xenófora

- Las 114 piezas de la versión 3 salieron con la línea demasiado gruesa: se engordaban hasta 8 px y se tapaban ojos y detalles, sobre todo en los devotos. Se rehicieron desde los recortes originales con `scripts/escaneos/grosor.py`: engorda la línea a lo más 3 px y solo mientras el dibujo conserva sus huecos (ojos, espacios entre líneas). 48 quedaron como estaban dibujadas, las demás con 1 a 3 px más. Mismo tamaño, así que los datos no cambian.
- En la tira de arriba de la visita hay "← Mi xenófora", además del botón de la barra.

## Pendiente

- Cabezas de las hojas con fondo negro (39, 40, 120, 121): ya tienen disco (devotos); falta recortarlas.
- Variantes de tareas por duración, cuerpo y destinatario (revisión P2).
- Ronda con 6 a 8 personas (ver la revisión).
- Recortes de textura como piezas sueltas (peanas, piedras, nubes).
- ¿Cruzar las tareas con las de Shubidubi? Opción con más peso: casi todas propias y, de vez en cuando, una hoja de Shubidubi.
- Versión física algún día: impresa, por correo o en un cuarto.
