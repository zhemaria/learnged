"""Herramientas para construir una lección y su práctica en inglés y en español a la vez.

Cada constructor (tools/build_lesson_X_Y.py) escribe los textos una sola vez, lado a lado,
con t("inglés", "español"). El marco común (barra, índice, tarea, quiz, lista, pie) se escribe
en inglés en los dos borradores: para el español lo traduce tools/es/traduce.py, igual que en
las lecciones anteriores, así que las páginas en español quedan idénticas en su estructura.

Después de construir, ejecute tools/ged_standards.py, tools/ged_standards_es.py,
tools/build_indice_es.py y tools/indice_en.py.
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "es"))
from traduce import Traductor

L = "en"
NIVEL = 1   # el constructor de cada lección del Nivel 2 pone B.NIVEL = 2
def t(en, es):
    """El texto en el idioma que se está construyendo."""
    return en if L == "en" else es

def constructor(n):
    """Nombre del script que construye la lección n."""
    return f"build_{'' if NIVEL == 1 else f'n{NIVEL}_'}lesson_{n.replace('-', '_')}.py"

def existe(ruta):
    return os.path.exists(os.path.join(ROOT, ruta))

def lec(n):   return f"lesson-{n}.html" if L == "en" else f"leccion-{n}.html"
def prac(n):  return f"practice-{n}.html" if L == "en" else f"practica-{n}.html"
def ruta_lec(n, lang=None):
    lang = lang or L
    return f"math/level-{NIVEL}/lesson-{n}.html" if lang == "en" else f"es/matematicas/nivel-{NIVEL}/leccion-{n}.html"

# ---------- piezas de la lección ----------
def T(*keys):
    return " ".join(f'<span class="{"tecla num" if k.isdigit() or k == "." else ("tecla dos" if k == "2nd" else "tecla")}">{k}</span>' for k in keys)

def E(x):
    return f'<span class="ec">{x}</span>'

def opciones(pid, items):
    btn = "\n".join(f'<button class="opcion" data-k="{k}" type="button">{x}</button>' for k, x in items)
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n{opciones(pid, items)}\n</div>'

def enlace(n, ancla, titulo, sub):
    """Enlace a la práctica. El marco va en inglés: traduce.py lo pasa al español."""
    return f'''<a class="enlace-interactivo" href="{prac(n)}#{ancla}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def calc(titulo, cuerpo):
    return f'<div class="caja-calc">\n<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>\n{cuerpo}\n<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> {t("Open the calculator", "Abrir la calculadora")}</button>\n</div>'

def caja(tipo, etiqueta, cuerpo):
    """tipo: 'tip' (verde) u 'ojo' (ámbar)."""
    cls, et = ("caja-tip", "et-verde") if tipo == "tip" else ("caja-ojo", "et-ambar")
    return f'<div class="caja {cls}">\n<span class="etiqueta {et}">{etiqueta}</span>\n{cuerpo}\n</div>'

def ejemplo(titulo, pasos):
    """pasos: lista de (marca, negrita, resto). marca '✓' para el último."""
    p = "\n".join(f'<p class="paso"><span aria-hidden="true" class="n">{m}</span><strong>{b}</strong> {r}</p>' for m, b, r in pasos)
    return f'<div class="ejemplo">\n<p class="titulo-ej">{titulo}</p>\n{p}\n</div>'

def tabla(aria, caption, cabeza, filas, expr_cols=()):
    """Tabla desplazable. aria y caption en el idioma; el sufijo del aria va en inglés (lo traduce traduce.py)."""
    th = "".join(f'<th scope="col">{c}</th>' for c in cabeza)
    tr = "\n".join("<tr>" + "".join(f'<td class="expr">{c}</td>' if i in expr_cols else f"<td>{c}</td>" for i, c in enumerate(f)) + "</tr>" for f in filas)
    return (f'<div aria-label="{aria} {t("(table you can scroll sideways)", "(tabla desplazable horizontalmente)")}" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">{caption}</caption>\n'
            f'<thead><tr>{th}</tr></thead>\n<tbody>\n{tr}\n</tbody>\n</table></div>\n'
            '<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>')

def svg(vb, label, cuerpo, ancho=560):
    return f'<svg viewBox="{vb}" role="img" aria-label="{label}" style="width:100%;max-width:{ancho}px;height:auto;display:block;margin:12px auto;">{cuerpo}</svg>'

def quiz(q, pregunta, items):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{x}</button>' for k, x in items)
    return f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>\n<p class="pregunta" id="t-q{q}">{pregunta}</p>\n<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'

def seccion(sid, num, titulo, cuerpo):
    return f'<section>\n<h2 id="{sid}"><span aria-hidden="true" class="num-seccion">{num}</span>{titulo}</h2>\n{cuerpo}\n</section>'

# ---------- la página de la lección ----------
def pagina_leccion(n, tema_num, tema, titulo, lema, chip, objetivos, secciones, tarea, quiz_items, lista_aria, lista_cap, lista_filas,
                   cierre, siguiente, glosario, lesson):
    """secciones: lista de (id, título, html). tarea: (papel, vida). siguiente: (n_siguiente, texto) o (None, texto)."""
    num = n.replace("-", ".")
    idx = "\n".join(f'<li><a href="#{sid}">{tt}</a></li>' for sid, tt, _ in secciones)
    cuerpo = "\n\n".join(seccion(sid, i + 1, tt, h) for i, (sid, tt, h) in enumerate(secciones))
    k = len(secciones)
    ns, ntxt = siguiente
    if ns and existe(ruta_lec(ns)):
        sig = f'{t("Next", "Siguiente")}: {ntxt[0]}<a href="{lec(ns)}">{ntxt[1]}</a>'
    else:
        sig = f'{t("Next", "Siguiente")}: {ntxt[0]}{ntxt[1]}'
    objs = "\n".join(f"<li>{o}</li>" for o in objetivos)
    filas = "\n".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in lista_filas)
    glos = "\n".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in glosario)
    practica_li = (f'<li><strong>The practice page.</strong> Open the <a href="{prac(n)}">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>'
                   if L == "en" else
                   f'<li><strong>La página de práctica.</strong> Abra la <a href="{prac(n)}">página de práctica de esta lección</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>')
    return f'''<!DOCTYPE html>
<!-- LearnGED · Lesson {num} · Math Level {NIVEL} (English) — built by tools/{constructor(n)}
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{t("Lesson", "Lección")} {num} · {titulo} · LearnGED</title>
<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="../lesson.css">
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="./">Math · Level {NIVEL} lessons</a></nav>
<a class="saltar" href="#indice">Skip to the lesson contents</a>
<header class="principal">
<div class="envoltura-header">
<p class="ruta">{t(f"Math · Level {NIVEL} · Topic", f"Matemáticas · Nivel {NIVEL} · Tema")} {tema_num} — {tema}</p>
<h1>{t("Lesson", "Lección")} {num} · {titulo}</h1>
<p class="lema">{lema}</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">{chip[0]}</span> {chip[1]}</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
{objs}
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
{idx}
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

{cuerpo}

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">{k + 1}</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
{practica_li}
<li><strong>{t("Paper and pencil.", "Papel y lápiz.")}</strong> {tarea[0]}</li>
<li><strong>{t("In your daily life.", "En su vida diaria.")}</strong> {tarea[1]}</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">{k + 2}</span>Practice quiz</h2>
<p>{t("Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")} If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{chr(10).join(quiz(q, p, it) for q, p, it in quiz_items)}
</div>
<p style="text-align:center;margin-top:18px;">
<button class="btn" id="btn-calificar" type="button">Check my answers</button>
<button class="btn btn-sec" id="btn-reintentar" style="display:none;" type="button">Start the quiz again</button>
</p>
<div aria-live="polite" class="marcador" id="marcador" role="status">
<div aria-hidden="true" class="barra-prog"><span id="barra"></span></div>
<p class="puntaje" id="puntaje"></p>
<p class="mensaje" id="mensaje"></p>
</div>
</section>

<section>
<h2 id="s-checklist"><span aria-hidden="true" class="num-seccion">{k + 3}</span>Self-check checklist</h2>
<p>Use this checklist to see how you are doing. For each skill, choose <strong>Got it</strong>, <strong>Getting there</strong>, or <strong>Needs more practice</strong>. Read it <strong>before</strong> you start the homework. Use it <strong>after</strong> to check your own work honestly.</p>
<div aria-label="{lista_aria} (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">{lista_cap} and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
{filas}
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
{cierre}
<p class="flecha-sig"><span aria-hidden="true">➡️</span> {sig}</p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
{glos}
</dl>
</section>
</div>
<footer><p>LearnGED · {t(f"Math · Level {NIVEL} · Topic", f"Matemáticas · Nivel {NIVEL} · Tema")} {tema_num} · {t("Lesson", "Lección")} {num}</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(lesson, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''

# ---------- la página de práctica ----------
PIE_PRACTICA = '''  <footer class="pie">
    <p><strong>{tema} · LearnGED</strong><br>
    José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago.</p>
    <p>This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p>
    <p class="tm">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p>
  </footer>'''

def modulo(mid, num, titulo, cuerpo, abierto=False):
    return f'''  <details class="modulo" id="{mid}"{" open" if abierto else ""}>
    <summary><span class="num" aria-hidden="true">{num}</span><h2>{titulo}</h2><span class="chev" aria-hidden="true">›</span></summary>
    <div class="cuerpo">
{cuerpo}
      <a class="volver" href="#titulo-indice">↑ Back to contents</a>
    </div>
  </details>'''

def om(pid, titulo):
    """Práctica de opción múltiple (creaPracticaOM)."""
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="opciones" id="{pid}-opciones"></div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def libre(pid, titulo, etiqueta, nota=True):
    """Práctica con respuesta escrita (creaPracticaLibre)."""
    nt = '\n        <p class="nota">Type only the number.</p>' if nota else ""
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos"><div class="campo"><label for="{pid}-r">{etiqueta}</label><input type="text" inputmode="decimal" autocomplete="off" class="ancho" id="{pid}-r"></div></div>{nt}
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def libre_e(pid, titulo, etiqueta=None):
    """Práctica con respuesta escrita de un entero con signo (creaPracticaLibre + numE de integers.js)."""
    et = etiqueta or t("Answer", "Respuesta")
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos"><div class="campo"><label for="{pid}-r">{et}</label><input type="text" autocomplete="off" class="ancho" id="{pid}-r"></div></div>
        <p class="nota">{t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def signo_valor(pid, titulo):
    """Práctica en dos pasos: el signo y el valor (creaSignoValor de integers.js)."""
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <p><strong>{t("Step 1.", "Paso 1.")}</strong> {t("What is the sign of the answer?", "¿Qué signo tiene el resultado?")}</p>
        <div class="signos" role="group" aria-label="{t("Sign of the answer", "Signo del resultado")}"><button type="button" id="{pid}-mas" aria-pressed="false" aria-label="{t("Positive", "Positivo")}">+</button><button type="button" id="{pid}-menos" aria-pressed="false" aria-label="{t("Negative", "Negativo")}">−</button></div>
        <div class="campos"><div class="campo"><label for="{pid}-v"><strong>{t("Step 2.", "Paso 2.")}</strong> {t("The value of the answer, without the sign", "El valor del resultado, sin signo")}</label><input type="text" inputmode="numeric" autocomplete="off" class="corto" id="{pid}-v"></div></div>
        <p class="nota">{t("If the answer is 0, you do not need to choose a sign.", "Si el resultado es 0, no hace falta elegir signo.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def pagina_practica(n, tema_num, tema, titulo, meta, modulos, js, estilo="", scripts=()):
    """modulos: lista de (id, título, html). js: el código de la página (después de practice.js)."""
    num = n.replace("-", ".")
    idx = "\n".join(f'      <li><a href="#{mid}">{tt}</a></li>' for mid, tt, _ in modulos)
    mods = "\n\n".join(modulo(mid, i + 1, tt, h, i == 0) for i, (mid, tt, h) in enumerate(modulos))
    ruta = f'{t(f"Level {NIVEL} · Topic", f"Nivel {NIVEL} · Tema")} {tema_num} · {tema}'
    est = f"\n<style>\n{estilo}\n</style>" if estilo else ""
    return f'''<!DOCTYPE html>
<!-- LearnGED · Level {NIVEL} · Lesson {num} · practice (English) — built by tools/{constructor(n)}
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Practice · Lesson", "Práctica · Lección")} {num} · {titulo} · LearnGED</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../practice.css">{est}
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="./">Math · Level {NIVEL} lessons</a></nav>
<a class="saltar" href="#titulo-indice">Skip to contents</a>
<div class="contenedor">
  <header class="principal">
    <div class="ruta">{ruta}</div>
    <h1>{t("Lesson", "Lección")} {num} · {titulo}</h1>
    <div class="meta">{meta}</div>
  </header>
  <nav class="indice" aria-labelledby="titulo-indice">
    <h2 id="titulo-indice">On this page</h2>
    <ol>
{idx}
    </ol>
    <div class="controles-todo">
      <button type="button" class="btn-sec" id="abrir-todo">Open all</button>
      <button type="button" class="btn-sec" id="cerrar-todo">Close all</button>
    </div>
  </nav>

{mods}

{PIE_PRACTICA.format(tema=ruta)}
</div>
<script src="../practice.js"></script>{"".join(chr(10) + '<script src="' + x + '"></script>' for x in scripts)}
<script>
{js.strip()}
iniciaNavegacion();
</script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''

# ---------- escribir los cuatro archivos ----------
def construye(n, hacer_leccion, hacer_practica, cabecera_es):
    """hacer_leccion() y hacer_practica() devuelven el HTML en el idioma L actual."""
    global L
    salida = {}
    for lang in ("en", "es"):
        L = lang
        salida[lang] = (hacer_leccion(), hacer_practica())
    L = "en"
    en_l = f"math/level-{NIVEL}/lesson-{n}.html"; en_p = f"math/level-{NIVEL}/practice-{n}.html"
    for ruta, html in ((en_l, salida["en"][0]), (en_p, salida["en"][1])):
        open(os.path.join(ROOT, ruta), "w", encoding="utf-8").write(html); print("ok", ruta)
    # español: el marco en inglés lo traduce traduce.py
    tl = Traductor(en_l, texto=salida["es"][0], nivel=NIVEL); tl.leccion(""); tl.frecuentes()
    tl.cabecera(f"<!-- LearnGED · Lección {n.replace('-', '.')} · Matemáticas Nivel {NIVEL} (español) — construida con tools/{constructor(n)}\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
    tl.guarda(f"es/matematicas/nivel-{NIVEL}/leccion-{n}.html")
    tp = Traductor(en_p, texto=salida["es"][1], nivel=NIVEL); tp.frecuentes()
    tp.cabecera(f"<!-- LearnGED · Nivel {NIVEL} · Lección {n.replace('-', '.')} · {cabecera_es} — práctica (español) — construida con tools/{constructor(n)}\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
    tp.guarda(f"es/matematicas/nivel-{NIVEL}/practica-{n}.html")
    # comprobación: no debe quedar marco en inglés en las páginas en español
    for ruta in (f"es/matematicas/nivel-{NIVEL}/leccion-{n}.html", f"es/matematicas/nivel-{NIVEL}/practica-{n}.html"):
        s = open(os.path.join(ROOT, ruta), encoding="utf-8").read()
        for frase in ["Open the activity", "Practice more", "Homework", "Self-check", "Coming next", "Key words", "New exercise", "Back to contents", "On this page", "(opens in a new tab)", "table you can scroll", "Question A", "and do each activity"]:
            if frase in s: print("  ¡OJO! queda en inglés en", ruta, ":", frase)
