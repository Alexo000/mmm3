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


LOCK = SRC / 'versiones.json'


def live(x, v):
    return x.get('v', 1) <= v and not (x.get('out') and v >= x['out'])


def snapshot(data, v):
    """Todo lo que decide un ídolo en la versión v, en orden. Si esto cambia, cambian los ídolos guardados."""
    T = data['T']
    def unit_ok(u):
        m = re.search(r'@(\d+)$', u)
        name = re.sub(r'@\d+$', '', u)
        t = T[name] if isinstance(T, dict) else {}
        return (int(m.group(1)) if m else 1) <= v and live(t, v)
    return {
        'P': [[p['id'], p['d'], p['a'], p.get('x', '')] for p in data['P'] if live(p, v)],
        'O': [[o['slug'], o['aff']] for o in data['O'] if live(o, v)],
        'F': [[f['id'], f['a']] for f in data.get('F', []) if live(f, v)],
        'U': {d: [re.sub(r'@\d+$', '', u) for u in us if unit_ok(u)] for d, us in data['U'].items()},
    }


def check_versions(data):
    V = data.get('V', 1)
    lock = json.loads(LOCK.read_text(encoding='utf-8')) if LOCK.exists() else {}
    for v in range(1, V + 1):
        snap = json.loads(json.dumps(snapshot(data, v)))
        if str(v) not in lock:
            lock[str(v)] = snap
            print(f'versión {v} de los datos guardada en source/versiones.json')
        elif lock[str(v)] != snap:
            fail(f'cambió algo que decide los ídolos de la versión {v} (piezas, atributos, operaciones, fondos o tareas por disco). '
                 f'Eso cambiaría ídolos ya guardados. Para sumar cosas, sube "V" en data.json y ponles "v": {V + 1}; '
                 f'para quitar una, ponle "out": {V + 1}. Ver docs/datos.md.')
    LOCK.write_text(json.dumps(lock, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def main():
    tpl = (SRC / 'template.html').read_text(encoding='utf-8')
    data_txt = (SRC / 'data.json').read_text(encoding='utf-8')
    data = json.loads(data_txt)
    if '__DATA__' not in tpl:
        fail('source/template.html no tiene el marcador __DATA__')

    discs = {'cuerpos', 'partes', 'materia', 'signos', 'devotos'}
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
            if re.sub(r'@\d+$', '', u) not in tasks:
                fail(f'el disco {d} nombra una tarea que no existe: {u}')
    poems = set(re.findall(r"^\s{2}(\w+):\{txt:", tpl.split('const POEMS_EN')[0], re.M))
    poems_en = set(re.findall(r"^\s{2}(\w+):\{txt:", tpl.split('const POEMS_EN')[1].split('function poem(')[0], re.M)) if 'const POEMS_EN' in tpl else set()
    if tasks - poems_en:
        fail('estas tareas no tienen poema en inglés (POEMS_EN): ' + ', '.join(sorted(tasks - poems_en)))
    forms_en = set(re.findall(r"^\s{2}(\w+):\{k:'", tpl.split('const TF_EN')[1].split('};')[0], re.M)) if 'const TF_EN' in tpl else set()
    if tasks - forms_en:
        fail('estas tareas no tienen forma en inglés (TF_EN): ' + ', '.join(sorted(tasks - forms_en)))
    missing = tasks - poems
    if missing:
        fail('estas tareas no tienen poema en la plantilla (POEMS): ' + ', '.join(sorted(missing)))
    forms = set(re.findall(r"^\s{2}(\w+):\{k:'", tpl, re.M))
    if tasks - forms:
        fail('estas tareas no tienen forma en la plantilla (TF): ' + ', '.join(sorted(tasks - forms)))
    for p in data['P']:
        if not p.get('dicho'):
            fail(f"la pieza {p['id']} no tiene dicho")
        if p['d'] == 'devotos' and not p.get('cree'):
            fail(f"el devoto {p['id']} no tiene creencia (cree)")
    for u_list in data['U'].values():
        for u in u_list:
            if re.sub(r'@\d+$', '', u) not in tasks:
                fail(f'tarea desconocida en U: {u}')
    check_versions(data)
    en = json.loads((SRC / 'en.json').read_text(encoding='utf-8'))
    for p in data['P']:
        t = en['P'].get(p['id'])
        need = ['n', 'art', 'de', 'ep', 'lec', 'dicho'] + (['cree'] if p['d'] == 'devotos' else []) + (['x'] if p['d'] == 'partes' else [])
        if not t or any(not t.get(k) for k in need):
            fail(f"falta la ficha en inglés de {p['id']} en source/en.json ({', '.join(need)})")
    for f in data.get('F', []):
        if f['id'] not in en['F']:
            fail(f"falta en inglés el fondo {f['id']} en source/en.json")
    for o in data['O']:
        if o['slug'] not in en['O']:
            fail(f"falta en inglés la operación {o['slug']} en source/en.json")
    for k in data['T']:
        if k not in en['T']:
            fail(f"falta en inglés la tarea {k} en source/en.json")

    (SITE / 'p').mkdir(parents=True, exist_ok=True)
    (SITE / 'CNAME').write_text('mmm.ramos-saavedra.com\n', encoding='utf-8')
    (SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://mmm.ramos-saavedra.com/sitemap.xml\n', encoding='utf-8')
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://mmm.ramos-saavedra.com/</loc></url>\n</urlset>\n', encoding='utf-8')
    html = tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    html = html.replace('__EN__', json.dumps(en, ensure_ascii=False, separators=(',', ':')))
    (SITE / 'index.html').write_text(html, encoding='utf-8')
    n = 0
    for f in sorted((SRC / 'pieces').glob('*.webp')):
        shutil.copy2(f, SITE / 'p' / f.name)
        n += 1
    (SITE / 'img').mkdir(parents=True, exist_ok=True)
    for f in sorted((SRC / 'img').glob('*')):
        shutil.copy2(f, SITE / 'img' / f.name)
    nf = 0
    if data.get('F'):
        (SITE / 'fondos' / 's').mkdir(parents=True, exist_ok=True)
        for f in data['F']:
            for sub in ('', 's/'):
                srcf = SRC / 'fondos' / f"{sub}{f['id']}.webp"
                if not srcf.exists():
                    fail(f"falta la textura source/fondos/{sub}{f['id']}.webp")
                shutil.copy2(srcf, SITE / 'fondos' / f"{sub}{f['id']}.webp")
            nf += 1
    count = {d: sum(1 for p in data['P'] if p['d'] == d) for d in sorted(discs)}
    print(f'site/index.html listo · {len(data["P"])} piezas ({count}) · {len(tasks)} tareas · {n} imágenes copiadas · {nf} fondos')


if __name__ == '__main__':
    main()
