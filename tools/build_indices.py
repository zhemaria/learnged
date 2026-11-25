"""Builds the two Level 1 indexes with the same compact layout:
   math/level-1/index.html (English) and es/matematicas/nivel-1/index.html (Spanish).
Only lessons that exist are linked; the others show as "coming soon" / «próximamente».
Usage: python3 tools/build_indices.py   (run it each time you add a lesson)"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMAS = {
 "en": [
  ("1", "Whole numbers", [("1-1", "Place value and whole numbers"), ("1-2", "Adding and subtracting whole numbers"), ("1-3", "Adding and subtracting in word problems")]),
  ("2", "Multiplication and division", [("2-1", "Multiplying whole numbers"), ("2-2", "Dividing whole numbers"), ("2-3", "Multiplication and division in word problems")]),
  ("3", "Decimals", [("3-1", "Decimals: read, write, compare, and round"), ("3-2", "Operations with decimals"), ("3-3", "Decimals in context and equivalent forms")]),
  ("4", "Fractions", [("4-1", "Equivalent fractions: simplify and compare"), ("4-2", "Adding and subtracting fractions"), ("4-3", "Multiplying and dividing fractions"), ("4-4", "Operations with mixed numbers")]),
  ("5", "Patterns and algebraic thinking", [("5-1", "Number and shape patterns"), ("5-2", "Algebraic language and simple unknowns"), ("5-3", "One-step word problems with the four operations")]),
  ("6", "Measurement and time", [("6-1", "U.S. customary units: length, weight, and capacity"), ("6-2", "Metric system, time, and temperature"), ("6-3", "Applied measurement problems")]),
  ("7", "Geometry", [("7-1", "Classifying 2D shapes: attributes and vocabulary"), ("7-2", "Perimeter of polygons"), ("7-3", "Area of rectangles and triangles")]),
  ("8", "Tables, graphs, and final project", [("8-1", "Reading and understanding data tables"), ("8-2", "Bar graphs and line graphs"), ("8-3", "Final project")])],
 "es": [
  ("1", "Números enteros", [("1-1", "Valor posicional y números enteros"), ("1-2", "Suma y resta de números enteros"), ("1-3", "Suma y resta en problemas verbales")]),
  ("2", "Multiplicación y división", [("2-1", "Multiplicación de números enteros"), ("2-2", "División de números enteros"), ("2-3", "Multiplicación y división en problemas verbales")]),
  ("3", "Decimales", [("3-1", "Decimales: leer, escribir, comparar y redondear"), ("3-2", "Operaciones con decimales"), ("3-3", "Decimales en contexto y formas equivalentes")]),
  ("4", "Fracciones", [("4-1", "Fracciones equivalentes: simplificar y comparar"), ("4-2", "Suma y resta de fracciones"), ("4-3", "Multiplicación y división de fracciones"), ("4-4", "Operaciones con números mixtos")]),
  ("5", "Patrones y pensamiento algebraico", [("5-1", "Patrones numéricos y de figuras"), ("5-2", "Lenguaje algebraico e incógnitas simples"), ("5-3", "Problemas verbales de un paso con las cuatro operaciones")]),
  ("6", "Sistemas de medidas y el tiempo", [("6-1", "Sistema inglés: longitud, peso y capacidad"), ("6-2", "Sistema métrico, tiempo y temperatura"), ("6-3", "Problemas aplicados de medición en contexto real")]),
  ("7", "Geometría", [("7-1", "Clasificación de figuras 2D: atributos y vocabulario"), ("7-2", "Perímetro de polígonos"), ("7-3", "Área de rectángulos y triángulos")]),
  ("8", "Tablas, gráficas y proyecto final", [("8-1", "Leer e interpretar tablas de datos"), ("8-2", "Gráficas de barras y de líneas"), ("8-3", "Proyecto final")])]}

# Extras: (kind, lesson file, practice file or None, text)
EXTRAS = {
 "en": {"3-1": ("explore", "infinite-decimals.html", None, "Explore: decimals never end"),
        "4-1": ("complement", "lesson-4-1-gcf-lcm.html", "practice-4-1-gcf-lcm.html", "Complement: factors, multiples, GCF, and LCM")},
 "es": {"3-1": ("explore", "decimales-infinitos.html", None, "Explorar: los decimales no se acaban"),
        "4-1": ("complement", "leccion-4-1-mcd-mcm.html", "practica-4-1-mcd-mcm.html", "Complemento: factores, múltiplos, MCD y MCM")}}

TX = {
 "en": {"dir": "math/level-1", "lec": "lesson-{}.html", "prac": "practice-{}.html", "lang": "en", "title": "Math · Level 1 · LearnGED",
        "h1": "Math · Level 1 · Build your foundation", "home": "/", "logoalt": "LearnGED home", "skip": "Skip to content",
        "intro": "Eight topics, from whole numbers to tables and graphs. Each lesson has a practice page that makes new exercises every time.",
        "otro": '<span lang="es">Versión en español: <a href="/es/matematicas/nivel-1/" hreflang="es">Matemáticas · Nivel 1</a></span>',
        "maestros": 'For teachers: <a href="../ged-standards.html">standards map</a>',
        "navlabel": "Topics", "big": "A+ Larger text", "hc": "High contrast", "tema": "Topic", "leccion": "Lesson", "practica": "practice", "ariaPrac": "Practice for lesson {}", "pronto": "coming soon",
        "alt": '<link rel="alternate" hreflang="es" href="/es/matematicas/nivel-1/">',
        "pie": '<p class="tm">© 2026. <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">CC BY-NC-SA 4.0</a>. GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>'},
 "es": {"dir": "es/matematicas/nivel-1", "lec": "leccion-{}.html", "prac": "practica-{}.html", "lang": "es", "title": "Matemáticas · Nivel 1 · LearnGED",
        "h1": "Matemáticas · Nivel 1 · Iniciación y dominio numérico", "home": "/es/", "logoalt": "Inicio de LearnGED", "skip": "Saltar al contenido",
        "intro": "Ocho temas, de los números enteros a las tablas y gráficas. Cada lección tiene una página de práctica que genera ejercicios nuevos cada vez.",
        "otro": '<span lang="en">English version: <a href="/math/level-1/" hreflang="en">Math · Level 1</a></span>',
        "maestros": 'Para maestros: <a href="/math/ged-standards.html" hreflang="en">mapa de estándares (en inglés)</a>',
        "navlabel": "Temas", "big": "A+ Texto más grande", "hc": "Alto contraste", "tema": "Tema", "leccion": "Lección", "practica": "práctica", "ariaPrac": "Práctica de la lección {}", "pronto": "próximamente",
        "alt": '<link rel="alternate" hreflang="en" href="/math/level-1/">',
        "pie": '<p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p>\n<p class="tm">© 2026. Licencia <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license">CC BY-NC-SA 4.0</a>. GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.</p>'}}

CSS = """  main.nivel{max-width:1320px}
  .top .wrap,footer .wrap{max-width:1320px}
  .nivel h1{color:var(--navy);margin:16px 0 4px;font-size:1.75em}
  .nivel .intro{margin:0 0 4px}
  .nivel .meta{margin:0 0 12px;font-size:.92em;color:var(--muted)}
  .temas-nav{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 14px;padding:0;list-style:none}
  .temas-nav a{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:4px 12px;background:#fff;color:var(--navy);text-decoration:none;font-size:.88em;font-weight:700}
  .temas-nav a:hover{border-color:var(--teal);background:#f1faf9}
  .grid-temas{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start;margin-bottom:28px}
  .tema{background:#fff;border:1px solid var(--line);border-top:5px solid var(--teal);border-radius:12px;padding:12px 16px 10px;scroll-margin-top:12px}
  .tema h2{margin:0 0 6px;font-size:1.18em;color:var(--navy);display:flex;gap:9px;align-items:center;line-height:1.25}
  .tn{flex:none;background:var(--teal);color:#fff;border-radius:50%;width:30px;height:30px;display:inline-grid;place-items:center;font-size:.85em}
  .tema ul{list-style:none;margin:0;padding:0}
  .tema li{display:flex;gap:9px;align-items:baseline;padding:6px 0;border-top:1px solid #eef0f2;font-size:1.02em;line-height:1.35}
  .tema li:first-child{border-top:0}
  .tema .num{flex:none;min-width:2.1em;font-weight:700;color:var(--muted);font-size:.9em}
  .tema .lec{flex:1}
  .tema .prac{flex:none;font-size:.82em;font-weight:700;border:1px solid var(--teal);border-radius:999px;padding:2px 10px;text-decoration:none;white-space:nowrap}
  .tema .prac:hover{background:#f1faf9}
  .tema li.extra{display:block;font-size:.88em;padding-left:2.9em;border-top:0;padding-top:0}
  .tema li.soon{color:var(--muted)}
  body.hc .tema{border-color:#000}
  .sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  @media (min-width:1100px){ .temas-nav{display:none} }
  @media (max-width:1099px){ .grid-temas{grid-template-columns:repeat(2,1fr)} }
  @media (max-width:700px){ .nivel h1{font-size:1.4em} .grid-temas{grid-template-columns:1fr} }"""

def construye(L):
    X = TX[L]; d = os.path.join(ROOT, X["dir"])
    existe = lambda f: os.path.exists(os.path.join(d, f))
    nav, tarjetas = [], []
    for n, nombre, lecs in TEMAS[L]:
        ancla = ("topic-" if L == "en" else "tema-") + n
        nav.append(f'<li><a href="#{ancla}">{n} · {nombre}</a></li>')
        items = []
        for k, titulo in lecs:
            num = k.replace("-", ".")
            if existe(X["lec"].format(k)):
                p = f' <a class="prac" href="{X["prac"].format(k)}" aria-label="{X["ariaPrac"].format(num)}">{X["practica"]}</a>' if existe(X["prac"].format(k)) else ""
                items.append(f'<li><span class="num" aria-hidden="true">{num}</span><a class="lec" href="{X["lec"].format(k)}"><span class="sr">{X["leccion"]} {num}: </span>{titulo}</a>{p}</li>')
                x = EXTRAS[L].get(k)
                if x and existe(x[1]):
                    pe = f' · <a href="{x[2]}">{X["practica"]}</a>' if x[2] and existe(x[2]) else ""
                    items.append(f'<li class="extra"><a href="{x[1]}">{x[3]}</a>{pe}</li>')
            else:
                items.append(f'<li class="soon"><span class="num" aria-hidden="true">{num}</span><span class="lec"><span class="sr">{X["leccion"]} {num}: </span>{titulo} — {X["pronto"]}</span></li>')
        tarjetas.append(f'<section class="tema" id="{ancla}" aria-labelledby="h-{ancla}"><h2 id="h-{ancla}"><span class="tn" aria-hidden="true">{n}</span><span><span class="sr">{X["tema"]} {n}: </span>{nombre}</span></h2>\n<ul>\n' + "\n".join(items) + '\n</ul></section>')
    html = f'''<!DOCTYPE html>
<!-- LearnGED · {X["title"]} — built by tools/build_indices.py; do not edit by hand -->
<html lang="{X["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{X["title"]}</title>
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{X["alt"]}
<link href="/fonts/fonts.css" rel="stylesheet">
<link rel="stylesheet" href="/learnged.css">
<style>
{CSS}
</style>
</head>
<body>
<a class="skip" href="#main">{X["skip"]}</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{X["home"]}"><img src="/img/learnged-logo-horizontal.svg" alt="{X["logoalt"]}"></a>
    <div class="tools">
      <button type="button" id="b-big" aria-pressed="false">{X["big"]}</button>
      <button type="button" id="b-hc" aria-pressed="false">{X["hc"]}</button>
      <nav class="lang" aria-label="Language / Idioma">
        <a href="/math/level-1/" lang="en" hreflang="en" data-lang="en"{' aria-current="true"' if L == "en" else ""}>EN</a>
        <a href="/es/matematicas/nivel-1/" lang="es" hreflang="es" data-lang="es"{' aria-current="true"' if L == "es" else ""}>ES</a>
      </nav>
    </div>
  </div>
</header>
<main id="main" class="wrap nivel">
<h1>{X["h1"]}</h1>
<p class="intro">{X["intro"]}</p>
<p class="meta">{X["otro"]} · {X["maestros"]}</p>
<nav aria-label="{X["navlabel"]}"><ul class="temas-nav">
{chr(10).join(nav)}
</ul></nav>
<div class="grid-temas">
{chr(10).join(tarjetas)}
</div>
</main>
<footer><div class="wrap">
{X["pie"]}
</div></footer>
<script>
(function(){{
  function get(k){{try{{return localStorage.getItem(k);}}catch(e){{return null;}}}}
  function set(k,v){{try{{localStorage.setItem(k,v);}}catch(e){{}}}}
  var b=document.body;
  [['b-big','big'],['b-hc','hc']].forEach(function(x){{
    var btn=document.getElementById(x[0]);
    if(get('learnged-'+x[1])==='1'){{b.classList.add(x[1]);btn.setAttribute('aria-pressed','true');}}
    btn.addEventListener('click',function(){{
      var on=b.classList.toggle(x[1]); btn.setAttribute('aria-pressed',on?'true':'false'); set('learnged-'+x[1],on?'1':'0');
    }});
  }});
  document.querySelectorAll('.lang a').forEach(function(a){{
    a.addEventListener('click',function(){{set('learnged-lang',a.getAttribute('data-lang'));}});
  }});
}})();
</script>
</body>
</html>
'''
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    return html.count(f'class="lec" href=')

if __name__ == "__main__":
    print("ok:", construye("en"), "English lessons ·", construye("es"), "lecciones en español")
