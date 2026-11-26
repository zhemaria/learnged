"""Builds the two Level 1 indexes with the same compact layout:
   math/level-1/index.html (English) and es/matematicas/nivel-1/index.html (Spanish).
Only lessons that exist are linked; the others show as "coming soon" / «próximamente».
Usage: python3 tools/build_indices.py   (run it each time you add a lesson)"""
import os
import re
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
        "4-1": ("complement", "lesson-4-1-gcf-lcm.html", "practice-4-1-gcf-lcm.html", "Complement: GCF and LCM")},
 "es": {"3-1": ("explore", "decimales-infinitos.html", None, "Explorar: los decimales no se acaban"),
        "4-1": ("complement", "leccion-4-1-mcd-mcm.html", "practica-4-1-mcd-mcm.html", "Complemento: MCD y MCM")}}

TX = {
 "en": {"dir": "math/level-1", "lec": "lesson-{}.html", "prac": "practice-{}.html", "lang": "en", "title": "Math · Level 1 · LearnGED",
        "h1": "Math · Level 1 · Build your foundation", "home": "/", "inicio": "Home", "migas": "Breadcrumb", "logoalt": "LearnGED home", "skip": "Skip to content",
        "intro": "Eight topics, from whole numbers to tables and graphs. Each lesson has a practice page that makes new exercises every time.",
        "otro": '<span lang="es">Versión en español: <a href="/es/matematicas/nivel-1/" hreflang="es">Matemáticas · Nivel 1</a></span>',
        "maestros": 'For teachers: <a href="../ged-standards.html">standards map</a>',
        "navlabel": "Topics", "big": "A+ Larger text", "small": "A− Smaller text", "hc": "High contrast", "lc": "Less contrast", "tema": "Topic", "leccion": "Lesson", "practica": "practice", "ariaPrac": "Practice for lesson {}", "pronto": "coming soon",
        "alt": '<link rel="alternate" hreflang="es" href="/es/matematicas/nivel-1/">',
        "pie": '<p class="tm">© 2026. <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">CC BY-NC-SA 4.0</a>. GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>'},
 "es": {"dir": "es/matematicas/nivel-1", "lec": "leccion-{}.html", "prac": "practica-{}.html", "lang": "es", "title": "Matemáticas · Nivel 1 · LearnGED",
        "h1": "Matemáticas · Nivel 1 · Iniciación y dominio numérico", "home": "/es/", "inicio": "Inicio", "migas": "Ruta de navegación", "logoalt": "Inicio de LearnGED", "skip": "Saltar al contenido",
        "intro": "Ocho temas, de los números enteros a las tablas y gráficas. Cada lección tiene una página de práctica que genera ejercicios nuevos cada vez.",
        "otro": '<span lang="en">English version: <a href="/math/level-1/" hreflang="en">Math · Level 1</a></span>',
        "maestros": 'Para maestros: <a href="/math/ged-standards.html" hreflang="en">mapa de estándares (en inglés)</a>',
        "navlabel": "Temas", "big": "A+ Texto más grande", "small": "A− Texto más pequeño", "hc": "Alto contraste", "lc": "Menor contraste", "tema": "Tema", "leccion": "Lección", "practica": "práctica", "ariaPrac": "Práctica de la lección {}", "pronto": "próximamente",
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
  .tema li.extra{font-size:.9em;border-top:0;padding-top:0}
  .tema li.extra .num{min-width:2.34em}
  .tema li.soon{color:var(--muted)}
  body.hc .tema{border-color:#000}
  .sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  @media (min-width:1100px){ .temas-nav{display:none} }
  @media (max-width:1099px){ .grid-temas{grid-template-columns:repeat(2,1fr)} }
  @media (max-width:700px){ .nivel h1{font-size:1.4em} .grid-temas{grid-template-columns:1fr} }"""

def construye(L, temas=None, extras=None, tx=None):
    temas = temas or TEMAS; extras = extras or EXTRAS; tx = tx or TX
    X = tx[L]; d = os.path.join(ROOT, X["dir"])
    existe = lambda f: os.path.exists(os.path.join(ROOT, f.split("?")[0].lstrip("/")) if f.startswith("/") else os.path.join(d, f.split("?")[0]))
    nav, tarjetas = [], []
    for n, nombre, lecs in temas[L]:
        ancla = ("topic-" if L == "en" else "tema-") + n
        nav.append(f'<li><a href="#{ancla}">{n} · {nombre}</a></li>')
        items = []
        for k, titulo in lecs:
            num = k.replace("-", ".")
            if existe(X["lec"].format(k)):
                p = f' <a class="prac" href="{X["prac"].format(k)}" aria-label="{X["ariaPrac"].format(num)}">{X["practica"]}</a>' if existe(X["prac"].format(k)) else ""
                items.append(f'<li><span class="num" aria-hidden="true">{num}</span><a class="lec" href="{X["lec"].format(k)}"><span class="sr">{X["leccion"]} {num}: </span>{titulo}</a>{p}</li>')
                xs = extras[L].get(k)
                for x in (xs if isinstance(xs, list) else [xs] if xs else []):  # one extra, or a list of them
                    if not existe(x[1]): continue
                    pe = f' <a class="prac" href="{x[2]}" aria-label="{X["practica"]}: {x[3]}">{X["practica"]}</a>' if x[2] and existe(x[2]) else ""
                    items.append(f'<li class="extra"><span class="num" aria-hidden="true"></span><a class="lec" href="{x[1]}">{x[3]}</a>{pe}</li>')
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
      <a class="inicio" href="{X["home"]}"><span aria-hidden="true">🏠 </span>{X["inicio"]}</a>
      <button type="button" id="b-big" data-off="{X["big"]}" data-on="{X["small"]}">{X["big"]}</button>
      <button type="button" id="b-hc" data-off="{X["hc"]}" data-on="{X["lc"]}">{X["hc"]}</button>
      <nav class="lang" aria-label="Language / Idioma">
        <a href="/{tx["en"]["dir"]}/" lang="en" hreflang="en" data-lang="en"{' aria-current="true"' if L == "en" else ""}>EN</a>
        <a href="/{tx["es"]["dir"]}/" lang="es" hreflang="es" data-lang="es"{' aria-current="true"' if L == "es" else ""}>ES</a>
      </nav>
    </div>
  </div>
</header>
<main id="main" class="wrap nivel">
<nav class="migas" aria-label="{X["migas"]}"><a href="{X["home"]}">{X["inicio"]}</a> <span aria-hidden="true">›</span> <span aria-current="page">{" · ".join(X["h1"].split(" · ")[:2])}</span></nav>
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
    function pon(on){{btn.textContent=on?btn.getAttribute('data-on'):btn.getAttribute('data-off');}}
    if(get('learnged-'+x[1])==='1'){{b.classList.add(x[1]);pon(true);}}
    btn.addEventListener('click',function(){{
      var on=b.classList.toggle(x[1]); pon(on); set('learnged-'+x[1],on?'1':'0');
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

# ---------------- Level 2 · Connecting with algebra ----------------
TEMAS2 = {
 "en": [
  ("1", "Integers", [("1-1", "The number line, absolute value, and opposites"), ("1-2", "Adding and subtracting integers"), ("1-3", "Multiplying and dividing integers; applications")]),
  ("2", "Fractions, exponents, and roots", [("2-1", "Fractions with negative signs"), ("2-2", "Positive integer exponents and powers of 10"), ("2-3", "Square roots of perfect squares")]),
  ("3", "The full order of operations (PEMDAS)", [("3-1", "Order of operations: review and nested parentheses"), ("3-2", "PEMDAS with powers, roots, fractions, and signs"), ("3-3", "PEMDAS with fractions and in algebra")]),
  ("4", "Ratios, rates, and proportions", [("4-1", "Ratios and unit rates"), ("4-2", "Direct proportions: the rule of three"), ("4-3", "Inverse proportions and mixed applications")]),
  ("5", "Percents", [("5-1", "Percent: conversions and the three basic cases"), ("5-2", "Percent change: increase and decrease"), ("5-3", "Discount, tax, tip, and mixed applications")]),
  ("6", "Money math and unit conversions", [("6-1", "Simple interest: I = P × r × t"), ("6-2", "Depreciation and other money applications"), ("6-3", "Converting between U.S. customary and metric units")]),
  ("7", "Geometry: circles and composite figures", [("7-1", "Area of composite figures"), ("7-2", "Circumference of a circle"), ("7-3", "Area of a circle and figures with semicircles")]),
  ("8", "Statistics and probability", [("8-1", "Mean, median, mode, range, and weighted mean"), ("8-2", "Circle graphs: read, interpret, and make"), ("8-3", "Simple probability")])],
 "es": [
  ("1", "Enteros con signo", [("1-1", "La recta numérica, el valor absoluto y los opuestos"), ("1-2", "Suma y resta de enteros con signo"), ("1-3", "Multiplicación y división de enteros; aplicaciones")]),
  ("2", "Fracciones, exponentes y raíces", [("2-1", "Fracciones complejas con coeficientes negativos"), ("2-2", "Exponentes enteros positivos y potencias de base 10"), ("2-3", "Raíces cuadradas de cuadrados perfectos")]),
  ("3", "PEMDAS completo", [("3-1", "Orden de operaciones: repaso y paréntesis anidados"), ("3-2", "PEMDAS con potencias, raíces, fracciones y signos"), ("3-3", "PEMDAS en expresiones con fracciones y contexto algebraico")]),
  ("4", "Razones, proporciones y porcentajes", [("4-1", "Razones y tasas unitarias"), ("4-2", "Proporciones directas: regla de tres y resolver proporciones"), ("4-3", "Proporciones inversas y aplicaciones mixtas")]),
  ("5", "Porcentajes", [("5-1", "El porcentaje: conversiones y los tres casos fundamentales"), ("5-2", "Cambio porcentual: aumento y disminución"), ("5-3", "Descuento, impuesto, propina y aplicaciones mixtas")]),
  ("6", "Matemáticas financieras y conversiones de medidas", [("6-1", "Interés simple: la fórmula I = P × r × t"), ("6-2", "Depreciación y otras aplicaciones financieras"), ("6-3", "Conversiones entre el sistema inglés y el métrico")]),
  ("7", "Geometría transicional", [("7-1", "Área de figuras compuestas"), ("7-2", "Circunferencia del círculo"), ("7-3", "Área del círculo y figuras compuestas con semicírculos")]),
  ("8", "Estadística y probabilidad", [("8-1", "Media, mediana, moda, rango y media ponderada"), ("8-2", "Gráficos circulares: leer, interpretar y construir"), ("8-3", "Probabilidad simple")])]}

EXTRAS2 = {
 "en": {"1-2": ("complement", "tengo-debo.html?lang=en", None, "Complement: What I have and what I owe"),
        "2-1": ("game", "fracciomania.html?lang=en", None, "Game: Fracciomanía")},
 "es": {"1-2": ("complement", "/math/level-2/tengo-debo.html?lang=es", None, "Complemento: Tengo y debo"),
        "2-1": ("game", "/math/level-2/fracciomania.html?lang=es", None, "Juego: Fracciomanía")}}

def _tx2():
    import copy
    X = copy.deepcopy(TX)
    for L in X:
        for k, v in X[L].items():
            X[L][k] = v.replace("level-1", "level-2").replace("nivel-1", "nivel-2").replace("Level 1", "Level 2").replace("Nivel 1", "Nivel 2")
    X["en"]["h1"] = "Math · Level 2 · Connecting with algebra"
    X["es"]["h1"] = "Matemáticas · Nivel 2 · Conectando con el álgebra"
    X["en"]["intro"] = "Eight topics, from integers to probability: the bridge from arithmetic to algebra. Each lesson has a practice page that makes new exercises every time."
    X["es"]["intro"] = "Ocho temas, de los enteros con signo a la probabilidad: el puente entre la aritmética y el álgebra. Cada lección tiene una página de práctica que genera ejercicios nuevos cada vez."
    return X
TX2 = _tx2()

# ---------------- Level 3 · Exploring geometry and statistics ----------------
TEMAS3 = {
 "en": [
  ("1", "Rules of exponents", [("1-1", "The product rule, power of a power, and power of a product"), ("1-2", "The quotient rule, zero exponents, and negative exponents"), ("1-3", "Simplifying with several rules")]),
  ("2", "Scientific notation", [("2-1", "Scientific notation and orders of magnitude"), ("2-2", "Multiplying and dividing in scientific notation"), ("2-3", "Adding, subtracting, and using scientific notation")]),
  ("3", "Radicals and the real numbers", [("3-1", "Simplifying radicals with perfect-square factors"), ("3-2", "Adding, subtracting, and multiplying radicals"), ("3-3", "The real number system: rational and irrational numbers")]),
  ("4", "Linear algebra", [("4-1", "Variables, algebraic expressions, and translating words"), ("4-2", "Solving linear equations with variables on both sides"), ("4-3", "Equations with fractions, decimals, and special cases")]),
  ("5", "Inequalities and formulas", [("5-1", "Solving and graphing linear inequalities"), ("5-2", "Inequalities that need simplifying, and word problems"), ("5-3", "Solving formulas for a variable, and a general strategy")]),
  ("6", "Advanced geometry", [("6-1", "Angles and parallel lines cut by a transversal"), ("6-2", "The Pythagorean theorem: proof, uses, and converse"), ("6-3", "Similar figures and scale drawings")]),
  ("7", "Volume and data analysis", [("7-1", "Volume of prisms and cylinders"), ("7-2", "Box plots"), ("7-3", "Histograms: make, read, and compare")]),
  ("8", "Counting and probability", [("8-1", "The counting principle, permutations, and combinations"), ("8-2", "Compound probability: with and without replacement"), ("8-3", "Final project and strategies for the GED math test")])],
 "es": [
  ("1", "Reglas de los exponentes", [("1-1", "Regla del producto, potencia de potencia y potencia de un producto"), ("1-2", "Regla del cociente, exponente cero y exponentes negativos"), ("1-3", "Simplificar expresiones exponenciales con múltiples reglas")]),
  ("2", "Notación científica", [("2-1", "Conversión decimal ↔ científica y órdenes de magnitud"), ("2-2", "Multiplicación y división en notación científica"), ("2-3", "Suma, resta y aplicaciones en ciencia y tecnología")]),
  ("3", "Radicales y números reales", [("3-1", "Simplificar radicales: factorización en cuadrados perfectos"), ("3-2", "Operaciones con radicales: suma, resta y multiplicación"), ("3-3", "El sistema de números reales: racionales, irracionales y la recta numérica completa")]),
  ("4", "Álgebra lineal", [("4-1", "Variables, expresiones algebraicas y traducción"), ("4-2", "Resolver ecuaciones lineales: propiedades de igualdad y variables en ambos lados"), ("4-3", "Ecuaciones con coeficientes fraccionarios, decimales y casos especiales")]),
  ("5", "Inecuaciones y fórmulas", [("5-1", "Resolver inecuaciones lineales y graficar en la recta numérica"), ("5-2", "Inecuaciones que requieren simplificación y problemas verbales"), ("5-3", "Despeje de fórmulas literales y estrategia general de resolución")]),
  ("6", "Geometría avanzada", [("6-1", "Ángulos: relaciones y líneas paralelas cortadas por una transversal"), ("6-2", "Teorema de Pitágoras: demostración, aplicaciones y converso"), ("6-3", "Semejanza de figuras y dibujos a escala (teorema de Tales)")]),
  ("7", "Volumen y análisis de datos", [("7-1", "Volumen de prismas y cilindros"), ("7-2", "Diagramas de caja y bigotes"), ("7-3", "Histogramas: construir, interpretar y comparar distribuciones")]),
  ("8", "Combinatoria y probabilidad", [("8-1", "Principio fundamental del conteo, permutaciones y combinaciones"), ("8-2", "Probabilidad compuesta: con y sin reemplazo"), ("8-3", "Proyecto final integrador y estrategias para el GED Mathematical Reasoning")])]}

EXTRAS3 = {
 "en": {"1-3": ("check", "topic-1-check.html", None, "Topic 1 check: the five rules of exponents"),
        "3-3": ("speed", "speed-irrationals.html", None, "Speed practice: irrational numbers against the clock"),
        "6-1": ("explore", "explore-angles.html", None, "Explore: angles, parallel lines, and a transversal"),
        "6-2": ("explore", "explore-pythagoras.html", None, "Explore: the Pythagorean theorem in real life"),
        "6-3": ("explore", "explore-similar.html", None, "Explore: congruent and similar triangles"),
        "8-2": [("explore", "explore-chance.html", None, "Explore: dice, cards, and spinners (simulations)"),
                ("explore", "explore-tree.html", None, "Explore: tree diagrams and two-way tables")],
        "8-3": [("project", "project-level-3.html", None, "Final project: My data analysis (template)"),
                ("check", "final-check-level-3.html", None, "Level 3 final check: 25 questions")]},
 "es": {"1-3": ("check", "comprobacion-tema-1.html", None, "Comprobación del Tema 1: las cinco reglas de los exponentes"),
        "3-3": ("speed", "rapidez-irracionales.html", None, "Ejercicios de rapidez: números irracionales contra reloj"),
        "6-1": ("explore", "explorar-angulos.html", None, "Explorar: ángulos, paralelas y una transversal"),
        "6-2": ("explore", "explorar-pitagoras.html", None, "Explorar: el teorema de Pitágoras en la vida real"),
        "6-3": ("explore", "explorar-semejanza.html", None, "Explorar: triángulos congruentes y semejantes"),
        "8-2": [("explore", "explorar-azar.html", None, "Explorar: dados, cartas y ruletas (simulaciones)"),
                ("explore", "explorar-arbol.html", None, "Explorar: diagramas de árbol y tablas de doble entrada")],
        "8-3": [("project", "proyecto-nivel-3.html", None, "Proyecto final: Mi análisis de datos (plantilla)"),
                ("check", "evaluacion-final-nivel-3.html", None, "Evaluación final del Nivel 3: 25 preguntas")]}}

def _tx3():
    import copy
    X = copy.deepcopy(TX)
    for L in X:
        for k, v in X[L].items():
            X[L][k] = v.replace("level-1", "level-3").replace("nivel-1", "nivel-3").replace("Level 1", "Level 3").replace("Nivel 1", "Nivel 3")
    X["en"]["h1"] = "Math · Level 3 · Exploring geometry and statistics"
    X["es"]["h1"] = "Matemáticas · Nivel 3 · Exploración geométrica y estadística"
    X["en"]["intro"] = "Eight topics, from the rules of exponents to probability: the algebra, geometry, and data of the GED test. Each lesson has a practice page that makes new exercises every time."
    X["es"]["intro"] = "Ocho temas, de las reglas de los exponentes a la probabilidad: el álgebra, la geometría y los datos del examen GED. Cada lección tiene una página de práctica que genera ejercicios nuevos cada vez."
    return X
TX3 = _tx3()

# ---------------- Level 4 · Mastering the GED and problem solving ----------------
TEMAS4 = {
 "en": [
  ("1", "Analytic geometry", [("1-1", "The coordinate plane: ordered pairs, distance, and midpoint"), ("1-2", "Slope: idea, formula, and meaning"), ("1-3", "Equations of a line: slope-intercept, point-slope, and standard form")]),
  ("2", "3D volume and polynomials", [("2-1", "Volume of spheres, cones, and pyramids"), ("2-2", "Composite 3D figures and surface area"), ("2-3", "Polynomials: types, adding, subtracting, and multiplying")]),
  ("3", "Multiplying and factoring", [("3-1", "Multiplying binomials: FOIL and special products"), ("3-2", "Factoring: common factor and difference of squares"), ("3-3", "Factoring trinomials (a = 1 and a ≠ 1)")]),
  ("4", "Quadratic equations", [("4-1", "Solving quadratic equations by factoring"), ("4-2", "Completing the square"), ("4-3", "The quadratic formula, the discriminant, and applications")]),
  ("5", "Rational expressions", [("5-1", "Simplifying rational expressions: factor and cancel"), ("5-2", "Adding, subtracting, multiplying, and dividing rational expressions"), ("5-3", "Solving rational equations and modeling")]),
  ("6", "Systems of linear equations", [("6-1", "Solving systems by substitution"), ("6-2", "Solving systems by elimination, and types of systems"), ("6-3", "The graphing method, applications, and modeling with systems")]),
  ("7", "Systems of inequalities and functions", [("7-1", "Systems of linear inequalities: graphing the solution region"), ("7-2", "Relations and functions, f(x) notation, domain and range"), ("7-3", "Average rate of change and types of functions")]),
  ("8", "Modeling with functions and a practice GED test", [("8-1", "Quadratic functions: the parabola, the vertex, and the intercepts"), ("8-2", "Exponential functions, growth and decay, and a first look at logarithms"), ("8-3", "Final project and practice GED math test")])],
 "es": [
  ("1", "Geometría analítica", [("1-1", "El plano cartesiano: pares ordenados, distancia y punto medio"), ("1-2", "La pendiente: concepto, fórmula e interpretación"), ("1-3", "Ecuaciones de la recta: pendiente-intercepto, punto-pendiente y forma estándar")]),
  ("2", "Volumen 3D y polinomios", [("2-1", "Volumen de esferas, conos y pirámides"), ("2-2", "Figuras 3D compuestas y área de superficie"), ("2-3", "Polinomios: clasificación, suma, resta y multiplicación básica")]),
  ("3", "Multiplicación y factorización", [("3-1", "Multiplicación de binomios: FOIL e identidades notables"), ("3-2", "Factorización: factor común y diferencia de cuadrados"), ("3-3", "Factorización de trinomios (a = 1 y a ≠ 1)")]),
  ("4", "Ecuaciones cuadráticas", [("4-1", "Resolver ecuaciones cuadráticas por factorización"), ("4-2", "Completar el cuadrado"), ("4-3", "La fórmula cuadrática, el discriminante y aplicaciones")]),
  ("5", "Expresiones racionales complejas", [("5-1", "Simplificar expresiones racionales: factorizar y cancelar"), ("5-2", "Sumar, restar, multiplicar y dividir expresiones racionales"), ("5-3", "Resolver ecuaciones con expresiones racionales y modelado")]),
  ("6", "Sistemas de ecuaciones lineales", [("6-1", "Resolver sistemas de ecuaciones por sustitución"), ("6-2", "Resolver sistemas por eliminación y clasificar sistemas"), ("6-3", "Método gráfico, aplicaciones y modelado con sistemas")]),
  ("7", "Sistemas de desigualdades y funciones", [("7-1", "Sistemas de desigualdades lineales: graficar la región solución"), ("7-2", "Relaciones vs. funciones, notación f(x) y dominio/rango"), ("7-3", "Tasa de cambio promedio e identificar tipos de funciones")]),
  ("8", "Modelado de funciones y simulacro GED", [("8-1", "Funciones cuadráticas: la parábola, el vértice y los interceptos"), ("8-2", "Funciones exponenciales, crecimiento/decaimiento e introducción a logaritmos"), ("8-3", "Proyecto final integrador y simulacro GED Mathematical Reasoning")])]}

def _tx4():
    import copy
    X = copy.deepcopy(TX)
    for L in X:
        for k, v in X[L].items():
            X[L][k] = v.replace("level-1", "level-4").replace("nivel-1", "nivel-4").replace("Level 1", "Level 4").replace("Nivel 1", "Nivel 4")
    X["en"]["h1"] = "Math · Level 4 · Mastering the GED and problem solving"
    X["es"]["h1"] = "Matemáticas · Nivel 4 · Dominio del GED y resolución de problemas"
    X["en"]["intro"] = "Eight topics, from the coordinate plane to functions and a practice GED test. Each lesson will have a practice page that makes new exercises every time."
    X["es"]["intro"] = "Ocho temas, del plano cartesiano a las funciones y un simulacro del GED. Cada lección tendrá una página de práctica que genera ejercicios nuevos cada vez."
    return X
TX4 = _tx4()

RE_BARRA = re.compile(r'(<a class="lg-logo" href="(/|/es/)"><img [^>]*></a>)(?!<a class="lg-link lg-inicio")')
RE_VIEJO = re.compile(r'<a class="lg-link lg-inicio" [^>]*><span aria-hidden="true">🏠 </span>(?:Home|Inicio)</a>')
def pon_inicio():
    """Adds a visible Home / Inicio link next to the logo in the top bar of every lesson, practice, and explore page.
    The logo already goes home, but students may not know that. Safe to run again: pages that have the link are left alone."""
    n = 0
    for base, _, archivos in os.walk(ROOT):
        if "/.git" in base or "/tools" in base:
            continue
        for a in archivos:
            if not a.endswith(".html"):
                continue
            ruta = os.path.join(base, a)
            s = open(ruta, encoding="utf-8").read()
            if 'class="lg-bar"' not in s:
                continue
            def enlace(m):
                es = m.group(2) == "/es/"
                return (m.group(1) + '<a class="lg-link lg-inicio" href="' + m.group(2) + '" style="margin-left:auto;border:1.5px solid #1E3A5F;border-radius:999px;padding:3px 12px">'
                        + '<span aria-hidden="true">🏠 </span>' + ("Inicio" if es else "Home") + "</a>")
            t = RE_BARRA.sub(enlace, RE_VIEJO.sub("", s), count=1)
            if t != s:
                open(ruta, "w", encoding="utf-8").write(t); n += 1
    return n

if __name__ == "__main__":
    print("Level 1 ok:", construye("en"), "English lessons ·", construye("es"), "lecciones en español")
    print("Level 2 ok:", construye("en", TEMAS2, EXTRAS2, TX2), "English lessons ·", construye("es", TEMAS2, EXTRAS2, TX2), "lecciones en español")
    print("Level 3 ok:", construye("en", TEMAS3, EXTRAS3, TX3), "English lessons ·", construye("es", TEMAS3, EXTRAS3, TX3), "lecciones en español")
    print("Home link added to", pon_inicio(), "pages")
    print("Level 4 ok:", construye("en", TEMAS4, {"en": {}, "es": {}}, TX4), "English lessons ·", construye("es", TEMAS4, {"en": {}, "es": {}}, TX4), "lecciones en español")
