"""Construye es/matematicas/nivel-1/index.html (índice de las lecciones del Nivel 1 en español).
Enlaza solo las lecciones que ya existen; las demás aparecen como «próximamente».
Uso: python3 tools/build_indice_es.py   (vuelva a ejecutarlo cada vez que añada una lección)"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "es", "matematicas", "nivel-1")

TEMAS = [
 ("1", "Números enteros", [("1-1", "Valor posicional y números enteros"), ("1-2", "Suma y resta de números enteros"), ("1-3", "Suma y resta en problemas verbales")]),
 ("2", "Multiplicación y división", [("2-1", "Multiplicación de números enteros"), ("2-2", "División de números enteros"), ("2-3", "Multiplicación y división en problemas verbales")]),
 ("3", "Decimales", [("3-1", "Decimales: leer, escribir, comparar y redondear"), ("3-2", "Operaciones con decimales"), ("3-3", "Decimales en contexto y formas equivalentes")]),
 ("4", "Fracciones", [("4-1", "Fracciones equivalentes, simplificar y comparar"), ("4-2", "Suma y resta de fracciones"), ("4-3", "Multiplicación y división de fracciones"), ("4-4", "Operaciones con números mixtos")]),
 ("5", "Patrones y pensamiento algebraico", [("5-1", "Patrones numéricos y de figuras"), ("5-2", "Lenguaje algebraico e incógnitas simples"), ("5-3", "Problemas verbales de un paso con las cuatro operaciones")]),
 ("6", "Sistemas de medidas y el tiempo", [("6-1", "Sistema inglés: longitud, peso y capacidad"), ("6-2", "Sistema métrico, tiempo y temperatura"), ("6-3", "Problemas aplicados de medición en contexto real")]),
 ("7", "Geometría", [("7-1", "Clasificación de figuras 2D: atributos y vocabulario"), ("7-2", "Perímetro de polígonos"), ("7-3", "Área de rectángulos y triángulos")]),
 ("8", "Tablas, gráficas y proyecto final", [("8-1", "Leer e interpretar tablas de datos"), ("8-2", "Gráficas de barras y de líneas"), ("8-3", "Proyecto final")]),
]
# Complementos de algunas lecciones: (lección, archivo de la lección, archivo de práctica o None, texto)
EXTRAS = {
 "3-1": ("explorar", "decimales-infinitos.html", None, "explorar: los decimales no se acaban"),
 "4-1": ("complemento", "leccion-4-1-mcd-mcm.html", "practica-4-1-mcd-mcm.html", "Factores, múltiplos, MCD y MCM"),
}

def existe(f): return os.path.exists(os.path.join(DIR, f))

secciones = []
for n, nombre, lecs in TEMAS:
    items = []
    for k, t in lecs:
        num = k.replace("-", ".")
        if existe(f"leccion-{k}.html"):
            li = f'<li><a href="leccion-{k}.html">Lección {num} · {t}</a>' + (f' · <a href="practica-{k}.html">práctica</a>' if existe(f"practica-{k}.html") else "")
            x = EXTRAS.get(k)
            if x and existe(x[1]):
                if x[0] == "explorar":
                    li += f' · <a href="{x[1]}">{x[3]}</a>'
                else:
                    li += f'<br><span style="font-size:.95em">Complemento: <a href="{x[1]}">{x[3]}</a>' + (f' · <a href="{x[2]}">práctica</a>' if x[2] and existe(x[2]) else "") + '</span>'
            items.append(li + "</li>")
        else:
            items.append(f'<li class="soon">Lección {num} · {t} — próximamente</li>')
    secciones.append(f'<section class="tema" id="tema-{n}"><h2>Tema {n} · {nombre}</h2>\n<ol>\n' + "\n".join(items) + '\n</ol></section>')

html = f'''<!DOCTYPE html>
<!-- LearnGED · Matemáticas · Nivel 1 (español) — construido por tools/build_indice_es.py -->
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Matemáticas · Nivel 1 · LearnGED</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="en" href="/math/level-1/">
<link href="/fonts/fonts.css" rel="stylesheet">
<link rel="stylesheet" href="/learnged.css">
<style>
  .nivel h1{{color:var(--navy);margin:28px 0 6px}}
  .tema{{background:#fff;border:1px solid var(--line);border-left:6px solid var(--teal);border-radius:12px;padding:16px 22px;margin:0 0 16px}}
  .tema h2{{margin:0 0 8px;font-size:1.2rem;color:var(--navy)}}
  .tema ol{{margin:0;padding-left:1.3rem}}
  .tema li{{margin:6px 0}}
  .soon{{color:var(--muted);font-size:.9rem}}
</style>
</head>
<body>
<a class="skip" href="#main">Saltar al contenido</a>
<header class="top"><div class="wrap">
  <a class="logo" href="/es/"><img src="/img/learnged-logo-horizontal.svg" alt="Inicio de LearnGED"></a>
</div></header>
<main id="main" class="wrap nivel">
<h1>Matemáticas · Nivel 1 · Iniciación y dominio numérico</h1>
<p>Números enteros, operaciones, decimales, fracciones y los primeros pasos en el álgebra, la medición y los datos. Cada lección tiene una página de práctica que genera ejercicios nuevos cada vez.</p>
<p lang="en">English version: <a href="/math/level-1/" hreflang="en">Math · Level 1</a></p>
{chr(10).join(secciones)}
</main>
<footer><div class="wrap">
<p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p>
<p class="tm">© 2026. Licencia <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license">CC BY-NC-SA 4.0</a>. GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.</p>
</div></footer>
</body>
</html>
'''
os.makedirs(DIR, exist_ok=True)
open(os.path.join(DIR, "index.html"), "w", encoding="utf-8").write(html)
print("ok")
