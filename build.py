#!/usr/bin/env python3
"""Arma site/ a partir de source/.

  python3 build.py

- Junta source/template.html con source/data.json y escribe site/index.html.
- Copia las piezas de source/pieces/ a site/p/.
- Se detiene y dice qué falta si una pieza de data.json no tiene imagen, o si una
  tarea o un poema no coinciden.
"""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC, SITE = ROOT / 'source', ROOT / 'site'


def fail(msg):
    print('ERROR:', msg)
    sys.exit(1)


def main():
    tpl = (SRC / 'template.html').read_text(encoding='utf-8')
    data_txt = (SRC / 'data.json').read_text(encoding='utf-8')
    data = json.loads(data_txt)
    if '__DATA__' not in tpl:
        fail('source/template.html no tiene el marcador __DATA__')

    discs = {'cuerpos', 'partes', 'materia', 'signos'}
    ids = set()
    for p in data['P']:
        if p['d'] not in discs:
            fail(f"la pieza {p['id']} tiene un disco desconocido: {p['d']}")
        if not (SRC / 'pieces' / f"{p['id']}.webp").exists():
            fail(f"falta la imagen source/pieces/{p['id']}.webp")
        if p['id'] in ids:
            fail(f"pieza repetida: {p['id']}")
        ids.add(p['id'])

    tasks = set(data['T'])
    for d, units in data['U'].items():
        for u in units:
            if u not in tasks:
                fail(f'el disco {d} nombra una tarea que no existe: {u}')
    poems = set(re.findall(r"^\s{2}(\w+):\{txt:", tpl, re.M))
    missing = tasks - poems
    if missing:
        fail('estas tareas no tienen poema en la plantilla (POEMS): ' + ', '.join(sorted(missing)))

    (SITE / 'p').mkdir(parents=True, exist_ok=True)
    (SITE / 'CNAME').write_text('mmm.ramos-saavedra.com\n', encoding='utf-8')
    (SITE / 'index.html').write_text(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':'))), encoding='utf-8')
    n = 0
    for f in sorted((SRC / 'pieces').glob('*.webp')):
        shutil.copy2(f, SITE / 'p' / f.name)
        n += 1
    count = {d: sum(1 for p in data['P'] if p['d'] == d) for d in sorted(discs)}
    print(f'site/index.html listo · {len(data["P"])} piezas ({count}) · {len(tasks)} tareas · {n} imágenes copiadas')


if __name__ == '__main__':
    main()
