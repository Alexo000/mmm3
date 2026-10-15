# Scripts para los escaneos nuevos

Se corren en la Mac (necesitan `numpy`, `opencv-python` y `Pillow`). Leen de `escaneos/sin-clasificar` y los números de hoja son la posición del archivo en orden alfabético, empezando en 0.

- `seg2.py 7,9,18`: el corte bueno, que no parte figuras (ver `docs/rondas.md`, V6.1). Para signos chicos: `seg2.py 8 0.010 0.004 0.0004`.
- `catalog2.py`: arma las hojas del catálogo con los recortes de `seg2.py` y las cabezas.
- `seg.py 7,9,18`: el corte de la primera vuelta; corta cada hoja de dibujos sobre blanco en recortes sueltos con fondo transparente (`~/seg/c/nHHH_NN.png`).
- `heads.py 39,40,120,121`: lo mismo para hojas de cabezas blancas sobre fondo negro.
- `sheet.py a 7,9`: hoja de contacto chica de los recortes, en `escaneos/_contacto/cand_a.jpg`.
- `big.py nombre 007_14,018_05`: hoja de contacto grande de recortes escogidos.
- `tiles.py 44,47`: saca cuadros de textura de las hojas de patrones (de ahí salieron los fondos).

Después de escoger: girar si hace falta, igualar el grosor de línea al de las piezas que ya están (ver `scripts/historico/lineweight.py`) y guardar en `source/pieces/<id>.webp`. Las piezas nuevas llevan id `nHHH_NN` (hoja y recorte) para no chocar con las de `Originales`.
