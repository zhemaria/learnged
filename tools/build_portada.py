"""LearnGED · Portada (index.html y es/index.html) con tres acordeones: Construya sus bases, Prepárese para el GED y Practique.
Cada acordeón agrupa las materias en filas con botones horizontales. Los enlaces a páginas que todavía no existen se muestran
como «Próximamente» con enlace al plan. El acordeón abierto se recuerda en el navegador; un enlace con #bases, #ged o #practica
(o #foundation, #ged, #practice) abre el acordeón correspondiente.
Uso: python3 tools/build_portada.py   (después de crear páginas nuevas, para que aparezcan sus botones)
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CIEN = [("The scientific method", "El método científico", "The scientific method and research design", "El método científico y el diseño de investigación"),
        ("Data and numbers", "Datos y números", "Quantitative reasoning in science", "Razonamiento cuantitativo en ciencias"),
        ("The cell and the body", "La célula y el cuerpo", "Life science I: the cell, energy, and the human body", "Ciencias de la vida I: célula, energía y cuerpo humano"),
        ("Heredity and evolution", "Herencia y evolución", "Life science II: heredity, evolution, and ecosystems", "Ciencias de la vida II: herencia, evolución y ecosistemas"),
        ("Matter and reactions", "Materia y reacciones", "Physical science I: matter, atoms, and chemical reactions", "Ciencias físicas I: materia, átomo y reacciones químicas"),
        ("Force and energy", "Fuerza y energía", "Physical science II: force, motion, energy, and waves", "Ciencias físicas II: fuerza, movimiento, energía y ondas"),
        ("Earth and space", "La Tierra y el espacio", "Earth and space science", "Ciencias de la Tierra y el espacio"),
        ("Test preparation", "Preparación del examen", "Putting it together: evaluating conclusions and GED preparation", "Integración, evaluación de conclusiones y preparación para el GED")]


def existe(ruta):
    ruta = ruta.split("?")[0].split("#")[0]
    p = os.path.join(ROOT, ruta)
    return os.path.exists(os.path.join(p, "index.html")) if ruta.endswith("/") else os.path.exists(p)


def pagina(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    pre = "" if en else "../"            # ruta de recursos compartidos desde es/
    raiz = "" if en else "es/"            # carpeta de las páginas en español, relativa a ROOT

    def boton(href, texto, aria=None, sec=False, rel_root=None):
        """href relativo a la página; rel_root: ruta desde ROOT para comprobar que existe."""
        if rel_root and not existe(rel_root):
            return ""
        a = f' aria-label="{html.escape(aria)}"' if aria else ""
        return f'<a class="btn{" btn-sec" if sec else ""}" href="{href}"{a}>{texto}</a>'

    def fila(titulo, botones, nota=None, pronto=None):
        bs = "".join(b for b in botones if b)
        cuerpo = f'<div class="niveles">{bs}</div>' if bs else ""
        if pronto:
            cuerpo += f'<a class="soon" href="{pronto}">{T("Coming soon · see the plan", "Próximamente · vea el plan")} <span aria-hidden="true">→</span></a>'
        n = f'<p class="fila-nota">{nota}</p>' if nota else ""
        return f'<div class="fila"><h3>{titulo}</h3>{n}{cuerpo}</div>'

    m = "math/" if en else "matematicas/"
    niv = (lambda k: f"level-{k}/") if en else (lambda k: f"nivel-{k}/")
    mr = lambda k: (f"math/level-{k}/" if en else f"es/matematicas/nivel-{k}/")
    sci = "science/" if en else "ciencias/"
    scir = "science/" if en else "es/ciencias/"

    # ---------- Construya sus bases
    bases = [
        fila(T("Math", "Matemáticas"), [boton(m + niv(k), T(f"Level {k}", f"Nivel {k}"), T(f"Math, level {k}", f"Matemáticas, nivel {k}"), rel_root=mr(k)) for k in (1, 2)],
             T("Whole numbers, fractions, decimals, and the first steps in algebra.", "Números enteros, fracciones, decimales y los primeros pasos del álgebra.")),
        fila(T("Reading and writing", "Lectura y escritura"), [], pronto=T("rla/#levels-1-2", "artes-del-lenguaje/#levels-1-2")),
    ]
    # ---------- Prepárese para el GED
    ciencias = [boton(sci, T("Course plan", "Plan del curso"), T("Science, plan of the course", "Ciencias, plan del curso"), sec=True, rel_root=scir)]
    for k, (cen, ces, len_, les) in enumerate(CIEN, 1):
        f = T(f"lesson-{k}-1.html", f"leccion-{k}-1.html")
        ciencias.append(boton(sci + f, f'<span class="tn">{k}</span> {T(cen, ces)}', T(f"Science, topic {k}: {len_}", f"Ciencias, tema {k}: {les}"), rel_root=scir + f))
    ciencias.append(boton(T("science/practice-test.html", "ciencias/simulacro.html"), T("Timed practice test", "Simulacro cronometrado"), T("Science, timed practice test of 40 questions", "Ciencias, simulacro cronometrado de 40 preguntas"), sec=True, rel_root=T("science/practice-test.html", "es/ciencias/simulacro.html")))
    ged = [
        fila(T("Math", "Matemáticas"), [boton(m + niv(k), T(f"Level {k}", f"Nivel {k}"), T(f"Math, level {k}", f"Matemáticas, nivel {k}"), rel_root=mr(k)) for k in (3, 4)],
             T("Algebra, geometry, functions, data, and probability, as on the GED Mathematical Reasoning test.", "Álgebra, geometría, funciones, datos y probabilidad, como en el examen de Razonamiento Matemático del GED.")),
        fila(T("Reasoning through language arts", "Razonamiento a través de las artes del lenguaje"), [], pronto=T("rla/#levels-3-4", "artes-del-lenguaje/#levels-3-4")),
        fila(T("Science", "Ciencias"), ciencias, T("Eight topics, from the scientific method to test preparation. Each button opens the first lesson of the topic.", "Ocho temas, del método científico a la preparación del examen. Cada botón abre la primera lección del tema.")),
        fila(T("Social studies", "Estudios sociales"), [], pronto=T("social-studies/", "estudios-sociales/")),
    ]
    # ---------- Practique
    pruebas = [boton(T("science/practice-test.html", "ciencias/simulacro.html"), T("Science · timed practice test", "Ciencias · simulacro cronometrado"), rel_root=T("science/practice-test.html", "es/ciencias/simulacro.html")),
               boton(m + niv(3) + T("final-check-level-3.html", "evaluacion-final-nivel-3.html"), T("Math · Level 3 final check", "Matemáticas · evaluación final del Nivel 3"), rel_root=mr(3) + T("final-check-level-3.html", "evaluacion-final-nivel-3.html")),
               boton(m + niv(4) + T("final-check-level-4.html", "evaluacion-final-nivel-4.html"), T("Math · Level 4 final check", "Matemáticas · evaluación final del Nivel 4"), rel_root=mr(4) + T("final-check-level-4.html", "evaluacion-final-nivel-4.html"))]
    juegos = [boton(f"{pre}math/level-2/fracciomania.html?lang={lang}", T("Fracciomanía · fractions", "Fracciomanía · fracciones"), rel_root="math/level-2/fracciomania.html"),
              boton(f"{pre}math/level-2/tengo-debo.html?lang={lang}", T("What I have and what I owe · integers", "Tengo y debo · números enteros"), rel_root="math/level-2/tengo-debo.html"),
              boton(m + niv(3) + T("speed-irrationals.html", "rapidez-irracionales.html"), T("Speed practice · irrational numbers", "Rapidez · números irracionales"), rel_root=mr(3) + T("speed-irrationals.html", "rapidez-irracionales.html"))]
    explora = [boton(m + niv(3) + T(a, b), T(c, d), rel_root=mr(3) + T(a, b)) for a, b, c, d in [
        ("explore-angles.html", "explorar-angulos.html", "Angles and parallel lines", "Ángulos y rectas paralelas"),
        ("explore-pythagoras.html", "explorar-pitagoras.html", "The Pythagorean theorem", "El teorema de Pitágoras"),
        ("explore-similar.html", "explorar-semejanza.html", "Similar figures", "Figuras semejantes"),
        ("explore-chance.html", "explorar-azar.html", "Dice, cards, and a spinner", "Dados, cartas y ruleta"),
        ("explore-tree.html", "explorar-arbol.html", "Tree diagrams", "Diagramas de árbol")]]
    practica = [
        fila(T("Practice tests and final checks", "Simulacros y evaluaciones finales"), pruebas, T("Timed or full-length tests with a report that tells you what to review.", "Pruebas completas o cronometradas, con un informe que indica qué repasar.")),
        fila(T("Games and speed practice", "Juegos y ejercicios de rapidez"), juegos),
        fila(T("Explore with interactive models", "Explore con modelos interactivos"), explora, T("Math models from Level 3: move the pieces and watch what changes.", "Modelos de matemáticas del Nivel 3: mueva las piezas y observe qué cambia.")),
    ]

    def acordeon(aid, alias, titulo, desc, filas, color):
        return (f'<details class="acordeon ac-{color[2:]}" id="{aid}" data-alias="{alias}">'
                f'<summary><span class="ac-tit">{titulo}</span><span class="ac-desc">{desc}</span></summary>'
                f'<div class="ac-cuerpo">{"".join(filas)}</div></details>')

    acs = "\n".join([
        acordeon(T("foundation", "bases"), T("bases", "foundation"), T("Build your foundation", "Construya sus bases"), T("Reading, writing, and math, step by step, starting from what you already know.", "Lectura, escritura y matemáticas, paso a paso, a partir de lo que ya sabe."), bases, "--teal"),
        acordeon("ged", "ged", T("Prepare for the GED", "Prepárese para el GED"), T("The four subjects of the test: math, reasoning through language arts, science, and social studies.", "Las cuatro materias del examen: matemáticas, razonamiento a través de las artes del lenguaje, ciencias y estudios sociales."), ged, "--rust"),
        acordeon(T("practice", "practica"), T("practica", "practice"), T("Practice", "Practique"), T("Practice tests, games, and interactive models, with explanations for every answer.", "Simulacros, juegos y modelos interactivos, con explicaciones de cada respuesta."), practica, "--mustard"),
    ])

    redirige = """<script>
(function(){
  var saved=null; try{saved=localStorage.getItem('learnged-lang');}catch(e){}
  if(!saved){var l=(navigator.languages&&navigator.languages[0])||navigator.language||'';
    if(/^es\\b/i.test(l)){location.replace('es/'+location.hash);}}
})();
</script>
""" if en else ""
    return f'''<!DOCTYPE html>
<!-- LearnGED · {T("Home page", "Portada")} — {T("built by", "construida con")} tools/build_portada.py -->
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T("LearnGED · Free GED prep in English and Spanish", "LearnGED · Preparación gratuita para el GED en español e inglés")}</title>
<meta name="description" content="{T("Free GED preparation in English and Spanish, at your own pace.", "Preparación gratuita para el GED en español e inglés, a su propio ritmo.")}">
{redirige}<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#1E3A5F">
<link rel="alternate" hreflang="en" href="https://www.learnged.com/">
<link rel="alternate" hreflang="es" href="https://www.learnged.com/es/">
<link href="/fonts/fonts.css" rel="stylesheet">
<link rel="stylesheet" href="{pre}learnged.css?v=2">
</head>
<body>
<a class="skip" href="#main">{T("Skip to content", "Saltar al contenido")}</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="./"><img src="{pre}img/learnged-logo-horizontal.svg" alt="{T("LearnGED home", "Inicio de LearnGED")}"></a>
    <div class="tools">
      <button type="button" id="b-big" data-off="{T("A+ Larger text", "A+ Texto más grande")}" data-on="{T("A− Smaller text", "A− Texto más pequeño")}">{T("A+ Larger text", "A+ Texto más grande")}</button>
      <button type="button" id="b-hc" data-off="{T("High contrast", "Alto contraste")}" data-on="{T("Less contrast", "Menor contraste")}">{T("High contrast", "Alto contraste")}</button>
      <nav class="lang" aria-label="Language / Idioma">
        <a href="{T("./", "../")}" lang="en" data-lang="en"{' aria-current="true"' if en else ""}>EN</a>
        <a href="{T("es/", "./")}" lang="es" data-lang="es"{"" if en else ' aria-current="true"'}>ES</a>
      </nav>
    </div>
  </div>
</header>

<main id="main">
  <section class="hero">
    <div class="wrap">
      <div>
        <span class="badge">{T("New: the complete Science course", "Nuevo: el curso completo de Ciencias")}</span>
        <h1>{T("Free GED<sup>®</sup> prep, in English and Spanish, at your own pace.", "Preparación gratuita para el GED<sup>®</sup>, en español e inglés, a su propio ritmo.")}</h1>
        <p class="lead">{T("Build your foundation, study the four GED subjects, and practice with explanations that help you move forward.", "Fortalezca sus bases, estudie las cuatro materias del examen y practique con explicaciones que le ayuden a avanzar.")}</p>
        <p><a class="btn" href="#{T("start", "comenzar")}">{T("Get started", "Comenzar")} <span aria-hidden="true">↓</span></a></p>
        <p>{T("LearnGED offers free study materials. We do not give the official GED test or award the GED credential, and the official test has a fee.", "LearnGED ofrece materiales de estudio gratuitos. No administramos el examen oficial ni expedimos la credencial GED, y el examen oficial tiene un costo.")}</p>
      </div>
      <img src="{pre}img/leo-animado.svg" alt="{T("Leo, the LearnGED owl, wearing glasses and a graduation cap and holding a digital pen", "Leo, el búho de LearnGED, con lentes, birrete y un lápiz digital")}">
    </div>
  </section>
  <div class="wrap">
    <h2 class="ac-intro" id="{T("start", "comenzar")}">{T("Where do you want to start?", "¿Por dónde quiere empezar?")}</h2>
    <p class="ac-ayuda">{T("Open a section to see its subjects. You can open more than one.", "Abra una sección para ver sus materias. Puede abrir más de una.")}</p>
    <div class="acordeones">
{acs}
    </div>
    <aside class="note">
      <h2>{T("While we build LearnGED", "Mientras construimos LearnGED")}</h2>
      <p>{T("All our materials in Spanish are available right now, free, at GEDparaHispanos.", "Todos nuestros materiales en español ya están disponibles, gratis, en GEDparaHispanos.")}</p>
      <a class="btn" href="https://www.gedparahispanos.com/">{T("Go to GEDparaHispanos", "Ir a GEDparaHispanos")}</a>
    </aside>
  </div>
</main>

<footer>
  <div class="wrap">
    <p><img src="{pre}img/learnged-logo-invertido.svg" alt="LearnGED" style="height:48px;width:auto"></p>
    <p>{T("Free · No account needed · We do not collect personal data.", "Gratis · Sin cuentas · No recogemos datos personales.")}</p>
    <p class="tm">{T("GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.", "GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.")}</p>
  </div>
</footer>

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
  /* Acordeones: recordar cuáles están abiertos y abrir el que nombra el enlace (#ged, #practica…) */
  var acs=[].slice.call(document.querySelectorAll('details.acordeon'));
  var abiertos=(get('learnged-portada')||'').split(',');
  acs.forEach(function(d){{
    if(abiertos.indexOf(d.id)>=0) d.open=true;
    d.addEventListener('toggle',function(){{ set('learnged-portada',acs.filter(function(x){{return x.open;}}).map(function(x){{return x.id;}}).join(',')); }});
  }});
  function porHash(){{
    var h=decodeURIComponent(location.hash.slice(1)); if(!h) return;
    acs.forEach(function(d){{ if(d.id===h||d.getAttribute('data-alias')===h){{ d.open=true; d.scrollIntoView(); d.querySelector('summary').focus(); }} }});
  }}
  porHash(); window.addEventListener('hashchange',porHash);
}})();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    for lang, ruta in (("en", "index.html"), ("es", "es/index.html")):
        open(os.path.join(ROOT, ruta), "w", encoding="utf-8").write(pagina(lang))
        print("ok", ruta)
