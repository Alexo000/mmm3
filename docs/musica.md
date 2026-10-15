# Música y sonidos

Todo lo hace el navegador con Web Audio. No hay archivos de sonido. El código está en `source/template.html`, en la sección que empieza con "sound: a ritual music box".

Se aprendió de la música del Shubyrinth (`_GAME/game/prototypes/labyrinth/js/music.js`): cada nota se golpea y se apaga, todo pasa por un filtro suave y un eco lento, el tempo es lento, baja cuando hay algo que leer, calla cuando la página está oculta y empieza con el primer clic.

## La partitura

- 32 compases a 44 negras por minuto, partes A A′ B A′, unos tres minutos, en loop.
- Re menor con mi bemol (segundo grado bemol) para lo extraño.
- **Voz principal:** campana tipo kalimba o cajita de música: una onda senoidal con dos armónicos inarmónicos que mueren rápido (`vBell`).
- **Bajo:** onda triangular larga, raíz y quinta (`vBass`).
- **Tic:** un pulso de 8 bits muy bajito en cada corchea, como reloj (`vTick`).
- **Sonaja:** ruido filtrado en la parte B (`vShk`).
- La melodía está escrita por compás en `MU_A`, `MU_A2` y `MU_B` (nota, octava y duración en corcheas: `D5:3`), y los acordes en `CH_A` y `CH_B`. Se puede reescribir a mano.

## Cambios según dónde estás

- **Vueltas:** I en re; II una cuarta arriba; III una cuarta abajo y al 82 % de velocidad (`VUELTA_KEY`). Fuera de la máquina y del ídolo vuelve a re.
- **Volumen por etapa:** mesa 100 %, máquina 55 %, ídolo 70 %, altar 80 %, lectura 30 %, concha 85 % (`STAGE_LEVEL`). Baja más mientras el ídolo habla y mientras gira la máquina.
- **Modo místico:** sin tic y sin sonaja, la campana una octava abajo y más eco.

## Efectos

`pick` (cada disco tiene su nota), `unpick`, `spin` (trinquete que frena y una campana grave), `voice` (el ídolo habla en campanitas), `paste` (pegar en la concha), `altar` (una campana por ídolo), `pop` (cada ídolo que cae en la concha), `reveal` y `close` (la concha se cierra).

## Escucharla fuera de la página

`musicPreview(vuelta, sampleRate, compases)` la renderiza sin tiempo real. `scripts/historico/render_music.py` la guarda como WAV para cada vuelta (necesita la página servida en localhost:8768).
