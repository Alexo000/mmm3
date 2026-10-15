# Scripts históricos

Así se hizo el primer juego de piezas, el 15 de octubre de 2026. Están tal como se usaron, con rutas de aquella sesión (`/home/claude/mmm`, `/mnt/user-data/uploads/Originales`). Antes de volver a usarlos hay que cambiar las rutas para que lean de `escaneos/` y escriban en `source/pieces/`.

- `segment.py`, `segment_hi.py`: cortan cada hoja escaneada en dibujos sueltos (umbral, componentes conectados, margen) y les quitan el fondo.
- `export_full.py`, `export_mono.py`: recortan a resolución completa y pasan a tinta negra pura.
- `lineweight.py`: empareja el grosor de línea según el tamaño al que se ve cada pieza en el ídolo.
- `cropsheet.py`: hojas de contacto para revisar.
- `curate.py`: la primera selección por disco.
- `attrs.py`: atributos SFDIS por pieza.
- `pieces2.py`, `tasks2.py`, `ops_es.py`: los textos de piezas, tareas y operaciones antes de pasar a `data.json`. Hoy `source/data.json` es la fuente; edita ahí.
- `render_music.py`: renderiza la música de cada vuelta a WAV.
