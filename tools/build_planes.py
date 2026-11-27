# -*- coding: utf-8 -*-
"""Plan pages for the subjects that are still coming (EN/ES), and the reviewers' page
review/whats-next.html.

  science/index.html          es/ciencias/index.html
  social-studies/index.html   es/estudios-sociales/index.html
  rla/index.html              es/artes-del-lenguaje/index.html

Each page tells the student (and the reviewing teachers) what the course will cover and
how it is organized, while its lessons are being written.
Run:  python3 tools/build_planes.py
"""
import os, html

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape

TXT = {
    "en": dict(skip="Skip to content", home="Home", logo_alt="LearnGED home", big="A+ Larger text", big_on="A− Smaller text",
               hc="High contrast", hc_on="Less contrast", migas="Breadcrumb", raiz="/",
               tm='© 2026. <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">CC BY-NC-SA 4.0</a>. GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.',
               estado="Coming soon", lecciones="lessons", tema="Topic", contenido="On this page", arriba="↑ Back to top"),
    "es": dict(skip="Saltar al contenido", home="Inicio", logo_alt="Inicio de LearnGED", big="A+ Texto más grande", big_on="A− Texto más pequeño",
               hc="Alto contraste", hc_on="Menor contraste", migas="Ruta de navegación", raiz="/es/",
               tm='© 2026. <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">CC BY-NC-SA 4.0</a>. GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.',
               estado="Próximamente", lecciones="lecciones", tema="Tema", contenido="En esta página", arriba="↑ Volver arriba"),
}

CSS = """<style>
  main.plan{max-width:1180px}
  .plan h1{color:var(--navy);margin:16px 0 4px;font-size:1.75em}
  .plan .intro{margin:0 0 10px;max-width:60em}
  .estado{display:flex;gap:14px;align-items:center;background:#fff8e1;border:1px solid #f0d58a;border-radius:12px;padding:10px 16px;margin:10px 0 16px;max-width:60em}
  .estado img{width:62px;height:auto;flex:none}
  .estado p{margin:0}
  .indice{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 18px;padding:0;list-style:none}
  .indice a{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:4px 12px;background:#fff;color:var(--navy);text-decoration:none;font-size:.9em;font-weight:700}
  .indice a:hover{border-color:var(--teal);background:#f1faf9}
  .bloque{background:#fff;border:1px solid var(--line);border-left:6px solid var(--teal);border-radius:12px;padding:16px 22px;margin:0 0 18px;scroll-margin-top:12px}
  .bloque h2{margin:0 0 6px;color:var(--navy);font-size:1.3em}
  .bloque h3{margin:14px 0 4px;color:var(--teal-d);font-size:1.05em}
  .bloque .sub{margin:0 0 10px;color:var(--muted)}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;align-items:start}
  .tema{border:1px solid var(--line);border-top:5px solid var(--c,var(--teal));border-radius:10px;padding:10px 14px;background:#fff}
  .tema h4{margin:0 0 6px;font-size:1.02em;color:var(--navy);line-height:1.3}
  .tema .tn{display:inline-block;background:var(--c,var(--teal));color:#fff;border-radius:999px;padding:0 9px;font-size:.82em;margin-right:4px}
  .tema ol{margin:0;padding-left:0;list-style:none}
  .tema li{padding:5px 0;border-top:1px solid #eef0f2;font-size:.96em;line-height:1.35;color:var(--ink)}
  .tema li:first-child{border-top:0}
  .tema li b{color:var(--muted);margin-right:4px}
  .tema .nota{font-size:.85em;color:var(--muted);margin:6px 0 0}
  .area{margin:18px 0 6px;font-size:1.12em;color:var(--navy);display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
  .area .peso{font-size:.8em;font-weight:700;color:var(--muted)}
  .ruta{display:inline-block;font-size:.78em;font-weight:700;border-radius:999px;padding:1px 10px;margin-left:6px;vertical-align:middle;background:#e7f3f4;color:var(--teal-d)}
  .ruta.prep{background:#e8edf6;color:var(--navy)}
  .dos{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .dos .tema ol{counter-reset:t}
  .borrador{display:inline-block;font-size:.78em;font-weight:700;border-radius:999px;padding:0 8px;background:#fff1e6;color:#9a4a1c;margin-left:4px}
  .plan ul.lista li{margin:4px 0}
  .plan .up{display:inline-block;margin-top:8px;font-size:.85rem;color:var(--muted)}
  body.hc .tema,body.hc .bloque{border-color:#000}
  @media (max-width:760px){ .dos{grid-template-columns:1fr} .plan h1{font-size:1.4em} }
  @media print{ .top .tools,.indice,.plan .up{display:none} .bloque{break-inside:avoid} }
</style>"""

SCRIPT = """<script>
(function(){
  function get(k){try{return localStorage.getItem(k);}catch(e){return null;}}
  function set(k,v){try{localStorage.setItem(k,v);}catch(e){}}
  var b=document.body;
  [['b-big','big'],['b-hc','hc']].forEach(function(x){
    var btn=document.getElementById(x[0]);
    function pon(on){btn.textContent=on?btn.getAttribute('data-on'):btn.getAttribute('data-off');}
    if(get('learnged-'+x[1])==='1'){b.classList.add(x[1]);pon(true);}
    btn.addEventListener('click',function(){
      var on=b.classList.toggle(x[1]); pon(on); set('learnged-'+x[1],on?'1':'0');
    });
  });
  document.querySelectorAll('.lang a').forEach(function(a){
    a.addEventListener('click',function(){set('learnged-lang',a.getAttribute('data-lang'));});
  });
})();
</script>"""


def pagina(lang, titulo, en, es, cuerpo, nombre_migas):
    T = TXT[lang]
    otro = "es" if lang == "en" else "en"
    return """<!DOCTYPE html>
<!-- LearnGED · {titulo} — built by tools/build_planes.py; do not edit by hand -->
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · LearnGED</title>
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{otro}" href="{otra_url}">
<link href="/fonts/fonts.css" rel="stylesheet">
<link rel="stylesheet" href="/learnged.css">
{css}
</head>
<body>
<a class="skip" href="#main">{skip}</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{raiz}"><img src="/img/learnged-logo-horizontal.svg" alt="{logo_alt}"></a>
    <div class="tools">
      <a class="inicio" href="{raiz}"><span aria-hidden="true">🏠 </span>{home}</a>
      <button type="button" id="b-big" data-off="{big}" data-on="{big_on}">{big}</button>
      <button type="button" id="b-hc" data-off="{hc}" data-on="{hc_on}">{hc}</button>
      <nav class="lang" aria-label="Language / Idioma">
        <a href="{en}" lang="en" hreflang="en" data-lang="en"{cur_en}>EN</a>
        <a href="{es}" lang="es" hreflang="es" data-lang="es"{cur_es}>ES</a>
      </nav>
    </div>
  </div>
</header>
<main id="main" class="wrap plan">
<nav class="migas" aria-label="{migas}"><a href="{raiz}">{home}</a> <span aria-hidden="true">›</span> <span aria-current="page">{nm}</span></nav>
{cuerpo}
</main>
<footer><div class="wrap">
<p class="tm">{tm}</p>
</div></footer>
{script}
</body>
</html>
""".format(titulo=e(titulo), lang=lang, otro=otro, otra_url=es if lang == "en" else en, css=CSS, en=en, es=es,
           cur_en=' aria-current="true"' if lang == "en" else "", cur_es=' aria-current="true"' if lang == "es" else "",
           nm=e(nombre_migas), cuerpo=cuerpo, script=SCRIPT, **T)


def estado(lang, texto):
    alt = "" if lang == "en" else ""
    return '<div class="estado" role="note"><img src="/img/leo-piensa.svg" alt="%s"><p>%s</p></div>' % (alt, texto)


def indice(lang, items):
    T = TXT[lang]
    return '<nav aria-label="%s"><ul class="indice">%s</ul></nav>' % (
        T["contenido"], "".join('<li><a href="#%s">%s</a></li>' % (a, e(t)) for a, t in items))


def tarjeta(lang, num, nombre, lecciones, color=None, nota=None, sin_num=False, enlaces=None):
    T = TXT[lang]
    st = ' style="--c:%s"' % color if color else ""
    s = ['<div class="tema"%s>' % st]
    if num is None:
        s.append('<h4>%s</h4>' % nombre)
    else:
        s.append('<h4><span class="tn">%s %s</span> %s</h4>' % (T["tema"], num, e(nombre)))
    if lecciones:
        s.append('<ol>')
        for i, l in enumerate(lecciones, 1):
            pref = "" if sin_num else "<b>%s.%d</b>" % (num, i)
            href = (enlaces or {}).get(i)
            s.append('<li>%s%s</li>' % (pref, '<a href="%s">%s</a>' % (href, e(l)) if href else e(l)))
        s.append('</ol>')
    if nota:
        s.append('<p class="nota">%s</p>' % nota)
    s.append('</div>')
    return "".join(s)


def bloque(id_, titulo, cuerpo, lang, sub=None):
    T = TXT[lang]
    return '<section class="bloque" id="%s"><h2>%s</h2>%s%s<a class="up" href="#main">%s</a></section>' % (
        id_, titulo, '<p class="sub">%s</p>' % sub if sub else "", cuerpo, T["arriba"])


def lista(items):
    return '<ul class="lista">%s</ul>' % "".join("<li>%s</li>" % x for x in items)


# ---------------------------------------------------------------- common: how every course is made
COMO = {
    "en": [
        "<strong>Lesson and practice page.</strong> Each lesson has its own practice page with activities that make new exercises every time, linked by section.",
        "<strong>Two tries.</strong> First wrong answer: a hint. Second: the solution, explained. Two-choice questions explain right away.",
        "<strong>English and Spanish.</strong> Both versions are built from the same source, so they teach exactly the same thing.",
        "<strong>GED and CCR standards</strong> at the end of each lesson, taken from the official GED Assessment Guide.",
        "<strong>Accessible.</strong> Keyboard navigation, text descriptions for every figure, larger text and high contrast, and nothing to install.",
        "<strong>Everything on LearnGED.</strong> No accounts, no outside sites: the readings, the tools, and the practice live here.",
    ],
    "es": [
        "<strong>Lección y página de práctica.</strong> Cada lección tiene su propia página de práctica, con actividades que generan ejercicios nuevos cada vez y enlaces a cada sección.",
        "<strong>Dos intentos.</strong> Al primer error, una pista; al segundo, la solución explicada. En las preguntas de dos opciones, la explicación va de inmediato.",
        "<strong>En español y en inglés.</strong> Las dos versiones salen de la misma fuente, así que enseñan exactamente lo mismo.",
        "<strong>Estándares del GED y CCR</strong> al final de cada lección, tomados de la guía oficial de evaluación del GED.",
        "<strong>Accesible.</strong> Navegación con teclado, descripción de cada figura, texto más grande y alto contraste, y nada que instalar.",
        "<strong>Todo dentro de LearnGED.</strong> Sin cuentas ni sitios externos: las lecturas, las herramientas y la práctica están aquí.",
    ],
}

# ---------------------------------------------------------------- SCIENCE
CIEN_TEMAS = {
    "en": [
        ("The scientific method and research design", ["From a phenomenon to a hypothesis: the anatomy of an investigation", "Variables, control groups, and sources of error", "Reading science: technical vocabulary and multistep procedures"]),
        ("Quantitative reasoning in science", ["Scientific notation, units, and the TI-30XS calculator", "From the table to the graph, and from the graph to the text", "Statistics and probability with experimental data"]),
        ("Life science I: the cell, energy, and the human body", ["Cell theory, organelles, and the cell membrane", "Photosynthesis and cellular respiration: how energy flows", "Human body systems, homeostasis, and health"]),
        ("Life science II: heredity, evolution, and ecosystems", ["DNA, RNA, and gene expression", "Meiosis, Punnett squares, and genetic probability", "Natural selection, evidence for evolution, and ecosystems"]),
        ("Physical science I: matter, atoms, and chemical reactions", ["The atom, the periodic table, and chemical bonds", "States of matter, density, and solutions", "Chemical equations, conservation of matter, and thermochemistry"]),
        ("Physical science II: force, motion, energy, and waves", ["Newton's laws, force, and friction", "Work, energy, and conservation", "Heat, heat transfer, and waves"]),
        ("Earth and space science", ["The dynamic Earth: plate tectonics, rocks, and geologic time", "The atmosphere, the water cycle, weather, and climate", "The solar system, the universe, and energy resources"]),
        ("Putting it together: evaluating conclusions and GED preparation", ["Multiple findings and evaluating conclusions with evidence", "Final project: my own investigation", "Timed practice test and item types"]),
    ],
    "es": [
        ("El método científico y el diseño de investigación", ["Del fenómeno a la hipótesis: la anatomía de una investigación", "Variables, grupos de control y fuentes de error", "Leer ciencia: vocabulario técnico y procedimientos de pasos múltiples"]),
        ("Razonamiento cuantitativo en ciencias", ["Notación científica, unidades y la calculadora TI-30XS", "De la tabla a la gráfica y de la gráfica al texto", "Estadística y probabilidad de datos experimentales"]),
        ("Ciencias de la vida I: célula, energía y cuerpo humano", ["Teoría celular, organelos y membrana plasmática", "Fotosíntesis y respiración celular: el flujo de la energía", "Sistemas del cuerpo humano, homeostasis y salud"]),
        ("Ciencias de la vida II: herencia, evolución y ecosistemas", ["ADN, ARN y expresión genética", "Meiosis, cuadros de Punnett y probabilidad genética", "Selección natural, evidencia evolutiva y ecosistemas"]),
        ("Ciencias físicas I: materia, átomo y reacciones químicas", ["El átomo, la tabla periódica y los enlaces químicos", "Estados de la materia, densidad y disoluciones", "Ecuaciones químicas, conservación de la materia y termoquímica"]),
        ("Ciencias físicas II: fuerza, movimiento, energía y ondas", ["Las leyes de Newton, fuerza y fricción", "Trabajo, energía y conservación", "Calor, transferencia térmica y ondas"]),
        ("Ciencias de la Tierra y el espacio", ["La Tierra dinámica: tectónica, rocas y tiempo geológico", "Atmósfera, ciclo del agua, tiempo y clima", "El sistema solar, el universo y los recursos energéticos"]),
        ("Integración, evaluación de conclusiones y preparación para el GED", ["Hallazgos múltiples y evaluación de conclusiones con evidencia", "Proyecto final integrador: mi propia investigación", "Simulacro cronometrado y tipos de pregunta"]),
    ],
}
# (anchor, EN name, ES name, weight EN, weight ES, topics, color)
CIEN_AREAS = [
    ("skills", "Science skills", "Destrezas científicas", "on every question of the test", "en todas las preguntas del examen", [1, 2], "#2a7f86"),
    ("life", "Life science", "Ciencias de la vida", "about 40% of the test", "cerca del 40% del examen", [3, 4], "#2e7d32"),
    ("physical", "Physical science (chemistry and physics)", "Ciencias físicas (química y física)", "about 40% of the test", "cerca del 40% del examen", [5, 6], "#1e3a8a"),
    ("earth", "Earth and space science", "Ciencias de la Tierra y el espacio", "about 20% of the test", "cerca del 20% del examen", [7], "#7c3aed"),
    ("ged", "Putting it together", "Integración y preparación para el GED", "the skills and the content, together", "las destrezas y el contenido, juntos", [8], "#c0582f"),
]


def lecciones_hechas(lang, tema, carpetas=("science", "es/ciencias")):
    """Lecciones ya publicadas en el tema: {número de lección: enlace}."""
    out = {}
    for i in (1, 2, 3):
        f = ("lesson-%d-%d.html" if lang == "en" else "leccion-%d-%d.html") % (tema, i)
        if os.path.exists(os.path.join(RAIZ, carpetas[0] if lang == "en" else carpetas[1], f)):
            out[i] = f
    return out


def ciencias(lang):
    en = lang == "en"
    T = CIEN_TEMAS[lang]
    c = []
    c.append('<h1>%s</h1>' % ("Science" if en else "Ciencias"))
    c.append('<p class="intro">%s</p>' % (
        "The GED Science test gives you a text, a table, a graph, or an experiment, and asks what you can conclude from it. This course teaches the science you need and, above all, how to read and reason with scientific information."
        if en else
        "El examen de Ciencias del GED le presenta un texto, una tabla, una gráfica o un experimento, y le pregunta qué se puede concluir. Este curso le enseña la ciencia que necesita y, sobre todo, a leer y razonar con información científica."))
    c.append(estado(lang,
        "<strong>The whole course is ready.</strong> Its twenty-four lessons are linked below, each with a practice page, plus the final project (Lesson 8.2) and a timed 40-question practice test (Lesson 8.3)."
        if en else
        "<strong>El curso completo ya está listo.</strong> Sus veinticuatro lecciones están enlazadas abajo, cada una con su página de práctica, además del proyecto final (Lección 8.2) y un simulacro cronometrado de 40 preguntas (Lección 8.3)."))
    c.append(indice(lang, [("organization", "How it is organized" if en else "Cómo se organiza")] +
                    [(a[0], a[1] if en else a[2]) for a in CIEN_AREAS] +
                    [("extras", "Labs and simulations" if en else "Laboratorios y simulaciones"), ("how", "How each lesson works" if en else "Cómo es cada lección")]))
    # organization
    org = lista([
        "<strong>24 lessons in 8 topics</strong>, about 4 hours of study each, from the method of science to a timed practice test." if en else
        "<strong>24 lecciones en 8 temas</strong>, de unas 4 horas de estudio cada una, desde el método científico hasta un simulacro cronometrado.",
        "<strong>Not by levels, but by area.</strong> Science is organized by the three content areas of the GED test: life science, physical science, and Earth and space science. The skills topics (1, 2, and 8) come before and after them." if en else
        "<strong>No va por niveles, sino por áreas.</strong> Ciencias se organiza según las tres áreas de contenido del examen del GED: ciencias de la vida, ciencias físicas y ciencias de la Tierra y el espacio. Los temas de destrezas (1, 2 y 8) van antes y después.",
        "<strong>The eight science practices of the GED</strong> (SP.1 to SP.8: reading science, designing investigations, reasoning from data, evaluating conclusions, and more) run through the whole course. Each lesson says which ones it works on." if en else
        "<strong>Las ocho prácticas científicas del GED</strong> (de SP.1 a SP.8: leer ciencia, diseñar investigaciones, razonar con datos, evaluar conclusiones y otras) recorren todo el curso. Cada lección indica cuáles trabaja.",
        "<strong>Three reporting categories.</strong> The test reports your score in three parts: analyzing arguments, evidence, and texts (30%); applying scientific processes (40%); and reasoning with numbers and data (30%). Each lesson shows the category, the depth of knowledge (DOK), and the standards aligned with each practice, and ends with GED-style questions." if en else
        "<strong>Tres categorías de informe.</strong> El examen informa la puntuación en tres partes: analizar argumentos, evidencia y textos (30 %); aplicar procesos científicos (40 %); y razonar con números y datos (30 %). Cada lección indica la categoría, la profundidad de conocimiento (DOK) y los estándares alineados con cada práctica, y termina con preguntas tipo GED.",
        "<strong>Where to start:</strong> Topics 1 and 2 first, because they teach the skills the other topics use. After that, the areas can be studied in any order. Math Level 2 (graphs, percents, mean and median) is a good base." if en else
        "<strong>Por dónde empezar:</strong> primero los Temas 1 y 2, porque enseñan las destrezas que usan los demás. Después, las áreas se pueden estudiar en cualquier orden. El Nivel 2 de Matemáticas (gráficas, porcentajes, media y mediana) es una buena base.",
    ])
    c.append(bloque("organization", "How it is organized" if en else "Cómo se organiza", org, lang))
    for a in CIEN_AREAS:
        tarjetas = "".join(tarjeta(lang, t, T[t - 1][0], T[t - 1][1], color=a[6], enlaces=lecciones_hechas(lang, t)) for t in a[5])
        c.append(bloque(a[0], a[1] if en else a[2], '<div class="grid">%s</div>' % tarjetas, lang,
                        sub=(a[3] if en else a[4]).capitalize()))
    extras = lista([
        "Interactive pages already used in the Spanish course will come into LearnGED, in both languages: building and reading graphs, a virtual lab to design experiments, statistics with experimental data, and arguments with evidence." if en else
        "Las páginas interactivas que ya usa el curso en español pasarán a LearnGED, en los dos idiomas: hacer y leer gráficas, un laboratorio virtual para diseñar experimentos, estadística con datos experimentales y argumentos con evidencia.",
        "Simulations for physics and Earth science, such as a roller coaster (energy), a pendulum, plate tectonics and earthquakes, the solar system, and the water and carbon cycles." if en else
        "Simulaciones de física y de ciencias de la Tierra, como la montaña rusa (energía), el péndulo, la tectónica de placas y los sismos, el sistema solar y los ciclos del agua y del carbono.",
        "The TI-30XS calculator and the formula sheet, as in Math, wherever a lesson uses numbers." if en else
        "La calculadora TI-30XS y la hoja de fórmulas, como en Matemáticas, en las lecciones que usan números.",
    ])
    c.append(bloque("extras", "Labs and simulations" if en else "Laboratorios y simulaciones", extras, lang))
    c.append(bloque("how", "How each lesson works" if en else "Cómo es cada lección", lista(COMO[lang]), lang))
    return "".join(c)


# ---------------------------------------------------------------- SOCIAL STUDIES
SOC_TEMAS = {
    "en": [
        ("Inquiry, sources, and analytical literacy", "SSP.1 · SSP.2 · SSP.5 · SSP.7 · SSP.8", ["Compelling and supporting questions: the inquiry arc", "Primary and secondary sources: origin, purpose, and context", "Bias, point of view, and persuasive language"]),
        ("Quantitative reasoning in social studies", "SSP.6 · SSP.10 · SSP.11", ["Graphs, tables, and the TI-30XS calculator", "Measures of center in population and economic data", "Percents, rates, map scales, and population density"]),
        ("Civics I: founding documents and constitutional principles", "SSP.1 · SSP.4 · SSP.5", ["From the social contract to the Declaration of Independence", "The Constitution: structure and principles", "Federalism in practice"]),
        ("Civics II: the three branches and policymaking", "SSP.2 · SSP.3 · SSP.4", ["The legislative branch: how a bill becomes a law", "The executive branch: the presidency, the cabinet, and the bureaucracy", "The judicial branch: judicial review and precedent"]),
        ("Citizenship in action: rights, elections, and public finance", "SSP.3 · SSP.6 · SSP.10", ["The Bill of Rights and the expansion of citizenship", "The election process: parties, campaigns, and the Electoral College", "Taxes, the budget, and fiscal policy"]),
        ("U.S. history: cause and change", "SSP.3 · SSP.5 · SSP.8", ["Colonies, the Revolution, and building a nation", "Expansion, slavery, the Civil War, and Reconstruction", "From the 20th century to today: industrialization, wars, and civil rights"]),
        ("Economics and geography of a connected world", "SSP.3 · SSP.6 · SSP.10", ["Supply, demand, markets, and the consumer", "Population, migration, and human geography", "Resources, the environment, and sustainability"]),
        ("Putting it together: multiple-source scenarios and GED preparation", "SSP.6 · SSP.7 · SSP.8", ["Multiple-source scenarios: text, graph, and map", "Final project: civic inquiry and informed action", "Timed practice test, item types, and the Illinois Constitution"]),
    ],
    "es": [
        ("Indagación, fuentes y alfabetización analítica", "SSP.1 · SSP.2 · SSP.5 · SSP.7 · SSP.8", ["Preguntas convincentes y de apoyo: el arco de indagación", "Fuentes primarias y secundarias: origen, propósito y contexto", "Sesgo, punto de vista y lenguaje persuasivo"]),
        ("Razonamiento cuantitativo en estudios sociales", "SSP.6 · SSP.10 · SSP.11", ["Gráficas, tablas y la calculadora TI-30XS", "Medidas de tendencia central en datos demográficos y económicos", "Porcentajes, tasas, escalas de mapas y densidad de población"]),
        ("Cívica I: documentos fundacionales y principios constitucionales", "SSP.1 · SSP.4 · SSP.5", ["Del contrato social a la Declaración de Independencia", "La Constitución: estructura y principios", "El federalismo en la práctica"]),
        ("Cívica II: las tres ramas y la formación de políticas", "SSP.2 · SSP.3 · SSP.4", ["El poder legislativo: del proyecto a la ley", "El poder ejecutivo: presidencia, gabinete y burocracia", "El poder judicial: revisión judicial y precedente"]),
        ("Ciudadanía en acción: derechos, elecciones y finanzas públicas", "SSP.3 · SSP.6 · SSP.10", ["La Carta de Derechos y la expansión de la ciudadanía", "El proceso electoral: partidos, campañas y colegio electoral", "Impuestos, presupuesto y política fiscal"]),
        ("Historia de los Estados Unidos: causalidad y cambio", "SSP.3 · SSP.5 · SSP.8", ["Colonia, Revolución y la construcción de la nación", "Expansión, esclavitud, Guerra Civil y Reconstrucción", "Del siglo XX a hoy: industrialización, guerras y derechos civiles"]),
        ("Economía y geografía del mundo conectado", "SSP.3 · SSP.6 · SSP.10", ["Oferta, demanda, mercados y el consumidor", "Población, migración y geografía humana", "Recursos, medio ambiente y sostenibilidad"]),
        ("Integración, escenarios de varias fuentes y preparación para el GED", "SSP.6 · SSP.7 · SSP.8", ["Escenarios de varias fuentes: texto, gráfica y mapa", "Proyecto final: indagación cívica y acción informada", "Simulacro cronometrado, tipos de pregunta y Constitución de Illinois"]),
    ],
}
SOC_COLORES = ["#8d5a3b", "#2a7f86", "#1e3a5f", "#3949ab", "#00838f", "#b0532c", "#2e7d32", "#6a3fa0"]
SOC_GRUPOS = [
    ("tools", "The tools: sources and data", "Las herramientas: fuentes y datos", [1, 2]),
    ("civics", "Civics and government", "Educación cívica y gobierno", [3, 4, 5]),
    ("history", "U.S. history", "Historia de los Estados Unidos", [6]),
    ("economics", "Economics and geography", "Economía y geografía", [7]),
    ("ged", "Putting it together", "Integración y preparación para el GED", [8]),
]


def sociales(lang):
    en = lang == "en"
    T = SOC_TEMAS[lang]
    c = []
    c.append('<h1>%s</h1>' % ("Social studies" if en else "Estudios sociales"))
    c.append('<p class="intro">%s</p>' % (
        "The GED Social Studies test almost never asks for a date. It shows a document (a piece of the Constitution, a map, a graph, a speech, a political cartoon) and asks what it supports and what it does not. This course teaches exactly that, with real documents."
        if en else
        "El examen de Estudios Sociales del GED casi nunca pregunta una fecha. Presenta un documento (un fragmento de la Constitución, un mapa, una gráfica, un discurso, una caricatura política) y pregunta qué se puede sostener con él y qué no. Este curso enseña exactamente eso, con documentos reales."))
    c.append(estado(lang,
        "<strong>Topics 1 to 7 are ready:</strong> their twenty-one lessons are linked below, each with a practice page. The other topics are being written now, in English and in Spanish; this page shows the whole plan."
        if en else
        "<strong>Los Temas 1 a 7 ya están listos:</strong> sus veintiuna lecciones están enlazadas abajo, cada una con su página de práctica. Los demás temas se están escribiendo ahora, en español y en inglés; esta página muestra el plan completo."))
    c.append(indice(lang, [("organization", "How it is organized" if en else "Cómo se organiza")] +
                    [(g[0], g[1] if en else g[2]) for g in SOC_GRUPOS] +
                    [("sources", "Source archive and extras" if en else "Archivo de fuentes y complementos"), ("how", "How each lesson works" if en else "Cómo es cada lección")]))
    org = lista([
        "<strong>One course, 24 lessons in 8 topics</strong>, about 4 hours of study each (about 96 hours in all). It is not split into levels." if en else
        "<strong>Un solo curso de 24 lecciones en 8 temas</strong>, de unas 4 horas de estudio cada una (unas 96 horas en total). No se divide en niveles.",
        "<strong>Topics 1 and 2 build the tools</strong> (questioning sources and reading data); <strong>Topics 3 to 7</strong> cover civics, history, economics, and geography in about the same proportion as the test, where civics and government weigh the most; <strong>Topic 8</strong> puts everything together and prepares for test day." if en else
        "<strong>Los Temas 1 y 2 construyen las herramientas</strong> (interrogar fuentes y leer datos); <strong>los Temas 3 a 7</strong> recorren cívica, historia, economía y geografía en una proporción parecida a la del examen, donde la cívica y el gobierno pesan más; <strong>el Tema 8</strong> lo integra todo y prepara el día de la prueba.",
        "<strong>The social studies practices of the GED</strong> (SSP.1 to SSP.11: drawing conclusions, central ideas, cause and effect, words in context, point of view, maps and graphs, fact and opinion, comparing sources, and data) appear in every topic. Each lesson shows the ones it works on, with their depth of knowledge (DOK) and the aligned CCR standards, and ends with GED-style questions." if en else
        "<strong>Las prácticas de estudios sociales del GED</strong> (de SSP.1 a SSP.11: sacar conclusiones, ideas centrales, causa y efecto, palabras en contexto, punto de vista, mapas y gráficas, hecho y opinión, comparar fuentes y datos) aparecen en todos los temas. Cada lección indica las que trabaja, con su profundidad de conocimiento (DOK) y los estándares CCR alineados, y termina con preguntas tipo GED.",
        "<strong>Every question on the test joins one practice with one content topic:</strong> civics and government (about 50% of the test), U.S. history (20%), economics (15%), and geography and the world (15%)." if en else
        "<strong>Cada pregunta del examen une una práctica con un tema de contenido:</strong> educación cívica y gobierno (cerca del 50 % del examen), historia de los Estados Unidos (20 %), economía (15 %) y geografía y el mundo (15 %).",
        "<strong>When to take it:</strong> it leans on reading and argument more than on math. It works best after Reasoning through language arts Level 3 and Math Level 3, and it can go along with Language arts Level 4. Always start with Lesson 1.1." if en else
        "<strong>Cuándo tomarlo:</strong> se apoya más en la lectura y la argumentación que en las matemáticas. Funciona mejor después del Nivel 3 de Artes del Lenguaje y del Nivel 3 de Matemáticas, y puede cursarse junto con el Nivel 4 de Artes del Lenguaje. Siempre conviene empezar por la Lección 1.1.",
    ])
    c.append(bloque("organization", "How it is organized" if en else "Cómo se organiza", org, lang))
    for g in SOC_GRUPOS:
        tarj = "".join(tarjeta(lang, t, T[t - 1][0], T[t - 1][2], color=SOC_COLORES[t - 1],
                               nota=("Practices: " if en else "Prácticas: ") + T[t - 1][1],
                               enlaces=lecciones_hechas(lang, t, ("social-studies", "es/estudios-sociales"))) for t in g[3])
        c.append(bloque(g[0], g[1] if en else g[2], '<div class="grid">%s</div>' % tarj, lang))
    extras = lista([
        "<strong>Source archive.</strong> The real public-domain documents the lessons use (the Declaration of Independence, the Constitution, speeches, court decisions, and more). The English version links to each original as its official repository keeps it; the Spanish version adds a translation." if en else
        "<strong>Archivo de fuentes.</strong> Los documentos reales de dominio público que usan las lecciones (la Declaración de Independencia, la Constitución, discursos, sentencias y otros). La versión en español trae su traducción; la versión en inglés enlaza cada original tal como lo guarda su repositorio oficial.",
        "<strong>World history.</strong> An interactive timeline from prehistory to the 20th century, for reference." if en else
        "<strong>Historia mundial.</strong> Una línea del tiempo interactiva, de la prehistoria al siglo XX, para consulta.",
        "<strong>Economics and geography.</strong> Interactive pages on supply and demand, the business cycle, the stock market, and the balance of payments, plus map work." if en else
        "<strong>Economía y geografía.</strong> Páginas interactivas de oferta y demanda, el ciclo económico, el mercado de valores y la balanza de pagos, además de trabajo con mapas.",
    ])
    c.append(bloque("sources", "Source archive and extras" if en else "Archivo de fuentes y complementos", extras, lang))
    c.append(bloque("how", "How each lesson works" if en else "Cómo es cada lección", lista(COMO[lang]), lang))
    return "".join(c)


# ---------------------------------------------------------------- RLA
# Spanish path (from GEDparaHispanos): level names and topics, in both languages.
RLA_NIVELES = [
    dict(n=1, ruta="build", en="Getting started with reading and writing", es="Iniciación a la lectura y la escritura", lec=42,
         sp_en=["The alphabet and the direction of reading", "Phonological awareness and fluency", "The sentence: noun, adjective, verb, and punctuation", "Comprehension strategies and vocabulary", "Narrative text and how ideas connect", "Visual information: images, maps, tables, and graphs", "The paragraph and kinds of text", "Communication, technology, and final project"],
         sp_es=["El alfabeto y la dirección de la lectura", "Conciencia fonológica y fluidez", "La oración: sustantivo, adjetivo, verbo y puntuación", "Estrategias de comprensión y vocabulario", "El texto narrativo y las relaciones entre ideas", "Información visual: imágenes, mapas, tablas y gráficas", "El párrafo y los tipos de texto", "Comunicación, tecnología y proyecto final"],
         en_en=["Letters and sounds: consonants, short vowels, and signs", "Long vowels, silent e, and the most common words", "Sound teams (sh, ch, th, wh) and endings -s, -ed, -ing", "The sentence: capital letters, end marks, subject and verb", "Everyday reading: labels, schedules, notices, and forms", "Short stories: who, what, where, and in what order", "Writing sentences and filling out forms", "Reading fluency and final project"],
         en_es=["Letras y sonidos: consonantes, vocales cortas y letreros", "Vocales largas, la e muda y las palabras más frecuentes", "Grupos de letras (sh, ch, th, wh) y terminaciones -s, -ed, -ing", "La oración: mayúscula, punto final, sujeto y verbo", "Lectura cotidiana: etiquetas, horarios, avisos y formularios", "Cuentos breves: quién, qué, dónde y en qué orden", "Escribir oraciones y llenar formularios", "Fluidez lectora y proyecto final"]),
    dict(n=2, ruta="build", en="Connecting ideas and texts", es="Conectando ideas y textos", lec=24,
         sp_en=["Advanced phonics and reading fluency", "Sentence grammar", "Punctuation, spelling, and register", "Main idea and text structure", "Comparing texts, vocabulary, and figurative language", "Reading with images and in the content areas", "Writing with structure", "Speaking, listening, and final project"],
         sp_es=["Fonética avanzada y fluidez lectora", "Gramática de la oración", "Puntuación, ortografía y registro", "Idea principal y estructura del texto", "Comparar textos, vocabulario y lenguaje figurado", "Leer con imágenes y en las materias", "Escribir con estructura", "Hablar, escuchar y proyecto final"],
         en_en=["Longer words: syllables, prefixes, and suffixes", "Word meaning: context clues, cognates, and false friends", "Verbs: subject–verb agreement and verb tenses", "Pronouns and confusing words (their, there, they're)", "Main idea and details in informational texts", "Stories: character, setting, problem, and theme", "The paragraph: topic sentence, details, and transitions", "Reading at work (graphs, emails, memos) and final project"],
         en_es=["Palabras largas: sílabas, prefijos y sufijos", "El significado: pistas del contexto, cognados y falsos amigos", "Los verbos: concordancia sujeto–verbo y tiempos verbales", "Pronombres y palabras que se confunden (their, there, they're)", "Idea principal y detalles en textos informativos", "Cuentos: personaje, ambiente, problema y tema", "El párrafo: oración temática, detalles y transiciones", "Leer en el trabajo (gráficas, correos, memorandos) y proyecto final"]),
    dict(n=3, ruta="prep", en="Exploring analysis and argument", es="Exploración del análisis y la argumentación", lec=24,
         sp_en=["Advanced sentence grammar", "Advanced punctuation and academic vocabulary", "Inference and textual evidence", "Text structure and literary language", "Evaluating arguments and integrating sources", "Reading in the content areas: data, procedures, and multimedia", "Argumentative and informative writing with analysis", "Research, speaking, and final project"],
         sp_es=["Gramática avanzada de la oración", "Puntuación avanzada y vocabulario académico", "Comprensión inferencial y evidencia textual", "Estructura del texto y lenguaje literario", "Evaluar argumentos e integrar fuentes", "Leer en las materias: datos, procedimientos y multimedia", "Escritura argumentada e informativa con análisis", "Investigación, oralidad y proyecto final"],
         en_en=["Complete sentences: fragments, run-ons, and comma splices", "Punctuation: commas, apostrophes, and capital letters", "Academic words: Latin and Greek roots, word choice, and tone", "Inference and evidence", "Text structure and the author's purpose", "Literature: theme, point of view, and figurative language", "Arguments: claims, reasons, and evidence", "Writing to explain and argue; final project"],
         en_es=["Oraciones completas: fragmentos y oraciones fusionadas", "Puntuación: comas, apóstrofos y mayúsculas", "Palabras académicas: raíces latinas y griegas, elección de palabras y tono", "Inferencia y evidencia", "Estructura del texto y propósito del autor", "Literatura: tema, punto de vista y lenguaje figurado", "Argumentos: afirmación, razones y evidencia", "Escribir para explicar y argumentar; proyecto final"]),
    dict(n=4, ruta="prep", en="Mastering the GED and argumentative writing", es="Dominio del GED y escritura argumentativa", lec=24,
         sp_en=["Complex syntax and expert control of conventions", "Advanced vocabulary and figurative language", "Critical reading: interacting themes and complex inference", "Structure, rhetoric, and style", "Evaluating arguments and synthesizing sources", "Quantitative and scientific analysis in the content areas", "Argumentative and discipline-specific writing", "Extended research, speaking, and GED preparation"],
         sp_es=["Sintaxis compleja y control experto de convenciones", "Vocabulario avanzado y lenguaje figurado", "Comprensión crítica: temas en interacción e inferencia compleja", "Estructura, retórica y estilo", "Evaluar argumentos y sintetizar fuentes", "Análisis cuantitativo y científico en las materias", "Escritura argumentativa y disciplinar", "Investigación extensa, oralidad y preparación GED"],
         en_en=["Editing like the GED: modifiers, parallel structure, and subordination", "Clear, formal writing: wordiness, informal usage, and transitions", "Complex nonfiction: science, social studies, and the workplace", "America's founding documents and the conversation that followed", "Literature: stories, novels, and drama; complex inference", "Two texts, two views: paired passages", "The extended response: analyzing two arguments", "Test day: item types, timing, and a full practice test"],
         en_es=["Corregir como en el GED: modificadores, paralelismo y subordinación", "Escritura clara y formal: palabras de más, registro informal y transiciones", "Textos informativos complejos: ciencia, estudios sociales y trabajo", "Los documentos fundacionales de EE. UU. y la conversación que les siguió", "Literatura: cuentos, novela y teatro; inferencia compleja", "Dos textos, dos puntos de vista: textos en pareja", "La respuesta extendida: analizar dos argumentos", "El día del examen: tipos de pregunta, tiempo y simulacro completo"]),
]


def rla(lang):
    en = lang == "en"
    c = []
    c.append('<h1>%s</h1>' % ("Reasoning through language arts" if en else "Razonamiento a través de las artes del lenguaje"))
    c.append('<p class="intro">%s</p>' % (
        "Reading, grammar, and writing: the GED test that asks you to understand texts, edit sentences, and write a short essay that analyzes two arguments. LearnGED will have <strong>two paths</strong>: reading and writing <strong>in English</strong>, and reading and writing <strong>in Spanish</strong>."
        if en else
        "Lectura, gramática y escritura: el examen del GED que le pide comprender textos, corregir oraciones y escribir un ensayo breve que analice dos argumentos. LearnGED tendrá <strong>dos caminos</strong>: lectura y escritura <strong>en español</strong>, y lectura y escritura <strong>en inglés</strong>."))
    c.append(estado(lang,
        "<strong>Coming soon.</strong> This page shows the plan for both paths, so you (and the teachers who review LearnGED) can see what is coming."
        if en else
        "<strong>Próximamente.</strong> Esta página muestra el plan de los dos caminos, para que usted (y los profesores que revisan LearnGED) pueda ver lo que viene."))
    c.append(indice(lang, [("organization", "How it is organized" if en else "Cómo se organiza"),
                           ("levels-1-2", "Levels 1 and 2" if en else "Niveles 1 y 2"),
                           ("levels-3-4", "Levels 3 and 4" if en else "Niveles 3 y 4"),
                           ("how", "How each lesson works" if en else "Cómo es cada lección")]))
    org = lista([
        "<strong>Four levels, like Math.</strong> Levels 1 and 2 are part of <em>Build your foundation</em>; Levels 3 and 4 are part of <em>Prepare for the GED</em>. Each level has 8 topics." if en else
        "<strong>Cuatro niveles, como Matemáticas.</strong> Los Niveles 1 y 2 forman parte de <em>Construya sus bases</em>; los Niveles 3 y 4, de <em>Prepárese para el GED</em>. Cada nivel tiene 8 temas.",
        "<strong>Two languages, two courses.</strong> Unlike Math, the two paths are not translations of each other: English and Spanish have different sounds, spelling, grammar, and punctuation, so each path has its own lessons, texts, and exercises." if en else
        "<strong>Dos idiomas, dos cursos.</strong> A diferencia de Matemáticas, los dos caminos no son traducciones el uno del otro: el inglés y el español tienen sonidos, ortografía, gramática y puntuación distintos, así que cada camino tiene sus propias lecciones, textos y ejercicios.",
        "<strong>Reading and writing in Spanish</strong> comes from the complete course of GEDparaHispanos (four levels, already finished), adapted to LearnGED." if en else
        "<strong>Lectura y escritura en español</strong> viene del curso completo de GEDparaHispanos (cuatro niveles ya terminados), adaptado a LearnGED.",
        "<strong>Reading and writing in English</strong> is a new course, written from the start for English, with public-domain texts. Its four levels follow the College and Career Readiness Standards for adults (A–B, C, D, and E) and combine phonics, reading, grammar for editing, and writing. GED teachers who teach in English will review it before the lessons are written. It is for adults who already understand spoken English; if you are still learning English, you can take the GED in Spanish with the Spanish path." if en else
        "<strong>Lectura y escritura en inglés</strong> es un curso nuevo, escrito desde el principio para el inglés, con textos de dominio público. Sus cuatro niveles siguen los estándares CCR para adultos (A–B, C, D y E) y combinan fonética, lectura, gramática para corregir textos y escritura. Los profesores de GED que enseñan en inglés lo revisarán antes de escribir las lecciones. Es para adultos que ya entienden el inglés hablado; si usted todavía está aprendiendo inglés, puede presentar el GED en español con el camino en español.",
        "<strong>Practice for the extended response</strong> will be connected to an essay checker in each language." if en else
        "<strong>La práctica de la respuesta extendida</strong> estará conectada con un evaluador de ensayos en cada idioma.",
    ])
    c.append(bloque("organization", "How it is organized" if en else "Cómo se organiza", org, lang))
    for id_, niveles, tit in (("levels-1-2", RLA_NIVELES[:2], ("Levels 1 and 2 · Build your foundation", "Niveles 1 y 2 · Construya sus bases")),
                              ("levels-3-4", RLA_NIVELES[2:], ("Levels 3 and 4 · Prepare for the GED", "Niveles 3 y 4 · Prepárese para el GED"))):
        cuerpo = []
        for nv in niveles:
            nombre = nv["en"] if en else nv["es"]
            cuerpo.append('<h3 id="level-%d">%s %d · %s</h3>' % (nv["n"], "Level" if en else "Nivel", nv["n"], e(nombre)))
            sp = nv["sp_en"] if en else nv["sp_es"]
            ing = nv["en_en"] if en else nv["en_es"]
            t_ing = ("Reading and writing in English" if en else "Lectura y escritura en inglés") + ' <span class="borrador">%s</span>' % ("in preparation" if en else "en preparación")
            t_esp = ("Reading and writing in Spanish" if en else "Lectura y escritura en español") + ' <span class="ruta">%d %s</span>' % (nv["lec"], TXT[lang]["lecciones"])
            col_ing = tarjeta(lang, None, t_ing, ["%d · %s" % (i, x) for i, x in enumerate(ing, 1)], color="#1e3a5f", sin_num=True)
            col_esp = tarjeta(lang, None, t_esp, ["%d · %s" % (i, x) for i, x in enumerate(sp, 1)], color="#2a7f86", sin_num=True)
            cuerpo.append('<div class="dos">%s</div>' % ((col_ing + col_esp) if en else (col_esp + col_ing)))
        c.append(bloque(id_, tit[0] if en else tit[1], "".join(cuerpo), lang))
    c.append(bloque("how", "How each lesson works" if en else "Cómo es cada lección", lista(COMO[lang][:2] + COMO[lang][3:]), lang))
    return "".join(c)


# ---------------------------------------------------------------- reviewers' page
def whats_next():
    import build_review as R
    s = [R.HEAD.format(n=0).replace("Reviewer guide · Math Level 0", "Reviewer guide · What comes next"), R.barra("whats-next.html")]
    s.append('<h1 id="top">What comes next: science, social studies, and language arts</h1>')
    s.append('<p>The four Math levels are done. This page tells you how the other three GED subjects will be organized, so you can comment before the lessons are written. Each subject already has a public page with its full plan (in English and in Spanish); the buttons below open them.</p>')
    s.append('<p class="links"><a class="btn" href="/science/" target="_blank" rel="noopener">Science · plan</a> '
             '<a class="btn" href="/social-studies/" target="_blank" rel="noopener">Social studies · plan</a> '
             '<a class="btn" href="/rla/" target="_blank" rel="noopener">Language arts · plan</a></p>')
    s.append("""<section id="home"><h2>1. Where each subject goes on the home page</h2>
<div class="scroll"><table>
<tr><th scope="col">Route</th><th scope="col">Subject</th><th scope="col">Organized by</th></tr>
<tr><td>Build your foundation</td><td>Math Levels 1–2 (done) · Reading and writing Levels 1–2</td><td>Levels</td></tr>
<tr><td>Prepare for the GED</td><td>Math Levels 3–4 (done) · Reasoning through language arts Levels 3–4</td><td>Levels</td></tr>
<tr><td>Prepare for the GED</td><td>Science</td><td>The three content areas of the test (life, physical, Earth and space), plus skills topics</td></tr>
<tr><td>Prepare for the GED</td><td>Social studies</td><td>One course of 8 topics (24 lessons)</td></tr>
</table></div>
<a class="up" href="#top">↑ Back to top</a></section>""")
    s.append("""<section id="same"><h2>2. What stays the same as in Math</h2>
<ul>%s</ul>
<a class="up" href="#top">↑ Back to top</a></section>""" % "".join("<li>%s</li>" % x for x in COMO["en"]))
    s.append("""<section id="order"><h2>3. Order of work</h2>
<ol>
<li><strong>Science</strong> first: it already exists in Spanish (24 lessons), so it follows the same path as Math, lesson by lesson, in both languages at once.</li>
<li><strong>Social studies</strong> next: it also exists in Spanish (24 lessons and a source archive of real documents).</li>
<li><strong>Reasoning through language arts</strong> last: the Spanish path comes from GEDparaHispanos, but the English path is a new course and needs your help the most.</li>
</ol>
<a class="up" href="#top">↑ Back to top</a></section>""")
    s.append("""<section id="questions"><h2>4. Questions for you</h2>
<ol>
<li><strong>Units in science.</strong> Math uses US customary units only. Science, like the GED Science test, uses metric units (grams, meters, liters, °C). We plan to use metric units in science and give the US equivalent the first time each unit appears. Does that match what your students need?</li>
<li><strong>Science by area, not by level.</strong> Is it useful for your students to choose an area (life, physical, Earth and space) after the two skills topics, or would you rather have a single fixed order?</li>
<li><strong>Social studies documents.</strong> The English version will link each primary source to the official transcript (National Archives, Library of Congress, and others). Are there documents you always use that we should add?</li>
<li><strong>State constitution.</strong> Lesson 8.3 of Social studies includes the Illinois Constitution, which some Illinois programs require. Should it stay, or become an optional page?</li>
<li><strong>Reading and writing in English.</strong> Please look at the outline of the four levels on the <a href="/rla/" target="_blank" rel="noopener">language arts plan</a>. What is missing for your students? What would you move to another level?</li>
<li><strong>Texts.</strong> Which public-domain authors or kinds of texts (workplace documents, news, letters, speeches) work best with your students?</li>
<li><strong>Would you like to help write or review</strong> one of these subjects? Tell us which one.</li>
</ol>
<a class="up" href="#top">↑ Back to top</a></section>""")
    s.append("""<section id="send"><h2>5. How to send comments</h2>
<p>Any format is fine: an email or a list. Please say <strong>which subject</strong> and, if you can, <strong>which topic or lesson</strong>. Send your comments to José M. Fernández (Zhema).</p>
<a class="up" href="#top">↑ Back to top</a></section>""")
    s.append(R.FOOT)
    return "\n".join(s)


PAGINAS = [
    ("science/index.html", "es/ciencias/index.html", "/science/", "/es/ciencias/", ("Science", "Ciencias"), ciencias),
    ("social-studies/index.html", "es/estudios-sociales/index.html", "/social-studies/", "/es/estudios-sociales/", ("Social studies", "Estudios sociales"), sociales),
    ("rla/index.html", "es/artes-del-lenguaje/index.html", "/rla/", "/es/artes-del-lenguaje/", ("Reasoning through language arts", "Artes del lenguaje"), rla),
]


def main():
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for f_en, f_es, u_en, u_es, nombres, fn in PAGINAS:
        for lang, f, nm in (("en", f_en, nombres[0]), ("es", f_es, nombres[1])):
            p = os.path.join(RAIZ, f)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            tit = nm + (" · plan" if lang == "en" else " · plan del curso")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(pagina(lang, tit, u_en, u_es, fn(lang), nm))
            print("ok", f)
    p = os.path.join(RAIZ, "review", "whats-next.html")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(whats_next())
    print("ok review/whats-next.html")


if __name__ == "__main__":
    main()
