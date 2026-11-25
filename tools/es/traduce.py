"""Ayuda para crear una página en español a partir de la versión en inglés (mismo código, textos traducidos).
Uso desde otro script:  from traduce import Traductor
  t = Traductor("math/level-1/practice-2-1.html"); t.r("English text", "Texto en español"); ... ; t.guarda("es/.../practica-2-1.html")
Cada reemplazo debe aparecer en la página (una vez, o las veces indicadas) para que nada se escape sin traducir."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COMUNES = [
 ('<html lang="en">', '<html lang="es">'),
 ('<a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="./">Math · Level 1 lessons</a>',
  '<a class="lg-logo" href="/es/"><img src="/img/learnged-logo-horizontal.svg" alt="Inicio de LearnGED" height="34"></a><a class="lg-link" href="./">Matemáticas · Lecciones del Nivel 1</a>'),
 ('<a class="saltar" href="#titulo-indice">Skip to contents</a>', '<a class="saltar" href="#titulo-indice">Saltar al contenido</a>'),
 ('<h2 id="titulo-indice">On this page</h2>', '<h2 id="titulo-indice">En esta página</h2>'),
 ('id="abrir-todo">Open all</button>', 'id="abrir-todo">Abrir todo</button>'),
 ('id="cerrar-todo">Close all</button>', 'id="cerrar-todo">Cerrar todo</button>'),
 ('<link rel="stylesheet" href="../practice.css">', '<link rel="stylesheet" href="/math/practice.css">'),
 ('<script src="../practice.js"></script>', '<script src="/math/practice.js"></script>'),
 ('<script src="/js/calculator.js"', '<script src="/js/calculadora.js"'),
 ('<p>This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p>',
  '<p>Esta obra está licenciada bajo <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" target="_blank" rel="noopener noreferrer">Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)</a>.</p>'),
 ('GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.',
  'GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.'),
 (' TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.',
  ' TI-30XS MultiView es una marca de Texas Instruments; la calculadora de esta página es un simulador independiente para aprender.'),
]
TODAS = [
 ('>New exercise</button>', '>Otro ejercicio</button>'),
 ('>Check</button>', '>Comprobar</button>'),
 ('<a class="volver" href="#titulo-indice">↑ Back to contents</a>', '<a class="volver" href="#titulo-indice">↑ Volver al contenido</a>'),
 ('Type digits only. You can use commas to separate the groups.', 'Escriba solo cifras. Puede separar los grupos con una coma.'),
 ('>Type only the number.</p>', '>Escriba solo el número.</p>'),
 ('>Next step</button>', '>Paso siguiente</button>'),
 ('>Show all</button>', '>Mostrar todo</button>'),
 ('>Start over</button>', '>Empezar de nuevo</button>'),
]
LECCION = [
 ('<link rel="stylesheet" href="../lesson.css">', '<link rel="stylesheet" href="/math/lesson.css">'),
 ('<script src="../lesson.js"></script>', '<script src="/math/lesson.js"></script>'),
 ('<a class="saltar" href="#indice">Skip to the lesson contents</a>', '<a class="saltar" href="#indice">Saltar al contenido de la lección</a>'),
 ('<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>', '<h2><span aria-hidden="true" class="num-seccion">🎯</span>Lo que va a aprender</h2>'),
 ('<p>When you finish this lesson, you will be able to:</p>', '<p>Al terminar esta lección, usted podrá:</p>'),
 ('<h2 id="indice-titulo">Lesson contents</h2>', '<h2 id="indice-titulo">Contenido de la lección</h2>'),
 ('About 4 hours with practice and homework · take breaks', 'Unas 4 horas con la práctica y la tarea · tome descansos'),
 ('<span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span>', '<span class="ei-cta">Abrir la actividad <span aria-hidden="true">›</span></span>'),
 ('(opens in a new tab)', '(se abre en una pestaña nueva)'),
 ('aria-label="Open the practice activity: ', 'aria-label="Abrir la actividad de práctica: '),
 ('<span class="ei-titulo">Practice more: ', '<span class="ei-titulo">Practique más: '),
 ('<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>', '<p class="aviso-desliza"><span aria-hidden="true">↔</span> Deslice la tabla horizontalmente para ver todas las columnas.</p>'),
 ('(table you can scroll sideways)', '(tabla desplazable horizontalmente)'),
 ('<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">', '<h2 id="s-tarea"><span aria-hidden="true" class="num-seccion">'),
 ('</span>Homework</h2>', '</span>Tarea</h2>'),
 ('<p>This is independent practice. Plan for about one hour, with your notebook open. Use the examples and the self-check checklist to review your work and decide what to practice next.</p>',
  '<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto. Use los ejemplos y la lista de autoevaluación para revisar su trabajo y decidir qué le conviene practicar después.</p>'),
 ('<p>This is independent practice. Plan for about one hour, with your notebook open.</p>', '<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto.</p>'),
 ('and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>',
  'y haga cada actividad. Los ejercicios cambian cada vez. Haga por lo menos 10 en cada actividad y siga hasta acertar 8 de 10 al primer intento. El marcador de cada actividad lleva la cuenta por usted.</li>'),
 ('<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">', '<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">'),
 ('</span>Practice quiz</h2>', '</span>Quiz de práctica</h2>'),
 ('If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution.', 'Si una respuesta no es correcta, recibirá una pista y un segundo intento. Después del segundo intento, verá la solución.'),
 ('Questions with only two choices show the explanation right away.', 'Las preguntas que tienen solo dos opciones muestran la explicación enseguida.'),
 ('You can take the quiz as many times as you want.</p>', 'Puede hacer el quiz las veces que quiera.</p>'),
 ('<p class="qnum">Question ', '<p class="qnum">Pregunta '),
 ('id="btn-calificar" type="button">Check my answers</button>', 'id="btn-calificar" type="button">Revisar mis respuestas</button>'),
 ('style="display:none;" type="button">Start the quiz again</button>', 'style="display:none;" type="button">Empezar el quiz de nuevo</button>'),
 ('<h2 id="s-checklist"><span aria-hidden="true" class="num-seccion">', '<h2 id="s-autoevaluacion"><span aria-hidden="true" class="num-seccion">'),
 ('</span>Self-check checklist</h2>', '</span>Lista de autoevaluación</h2>'),
 ('<p>Use this checklist to see how you are doing. For each skill, choose <strong>Got it</strong>, <strong>Getting there</strong>, or <strong>Needs more practice</strong>. Read it <strong>before</strong> you start the homework. Use it <strong>after</strong> to check your own work honestly.</p>',
  '<p>Use esta lista para ver cómo va. En cada destreza, elija <strong>Lo domino</strong>, <strong>Voy avanzando</strong> o <strong>Necesito más práctica</strong>. Léala <strong>antes</strong> de empezar la tarea. Úsela <strong>después</strong> para revisar su propio trabajo con honestidad.</p>'),
 ('<th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th>',
  '<th scope="col">Destreza</th><th class="nivel-cab" scope="col">Lo domino</th><th class="nivel-cab" scope="col">Voy avanzando</th><th class="nivel-cab" scope="col">Necesito más práctica</th>'),
 ('and what Got it, Getting there, and Needs more practice look like</caption>', 'y cómo se ve cada nivel: Lo domino, Voy avanzando y Necesito más práctica</caption>'),
 ('<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>', '<h2 id="s-siguiente"><span aria-hidden="true" class="num-seccion">➡️</span>Lo que viene</h2>'),
 ('<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>', '<h2 id="s-terminos"><span aria-hidden="true" class="num-seccion">📘</span>Términos clave</h2>'),
 ('<li><a href="#s-homework">Homework</a></li>', '<li><a href="#s-tarea">Tarea</a></li>'),
 ('<li><a href="#s-quiz">Practice quiz</a></li>', '<li><a href="#s-quiz">Quiz de práctica</a></li>'),
 ('<li><a href="#s-checklist">Self-check checklist</a></li>', '<li><a href="#s-autoevaluacion">Lista de autoevaluación</a></li>'),
 ('<li><a href="#s-next">Coming next</a></li>', '<li><a href="#s-siguiente">Lo que viene</a></li>'),
 ('<li><a href="#s-words">Key words</a></li>', '<li><a href="#s-terminos">Términos clave</a></li>'),
 ('<p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p>',
  '<p class="licencia">© 2026. Esta obra está licenciada bajo <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license" target="_blank">Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)</a>.</p>'),
 ('<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>', '<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license"/>'),
 ('<a aria-label="Back to the lesson contents" class="volver-indice" href="#indice"><span aria-hidden="true">↑</span> Contents</a>', '<a aria-label="Volver al contenido de la lección" class="volver-indice" href="#indice"><span aria-hidden="true">↑</span> Índice</a>'),
 ('<span class="etiqueta et-ambar">Watch out!</span>', '<span class="etiqueta et-ambar">¡Ojo!</span>'),
 ('<span class="etiqueta et-verde">Key idea</span>', '<span class="etiqueta et-verde">Idea clave</span>'),
 ('<span class="etiqueta et-verde">Tip</span>', '<span class="etiqueta et-verde">Consejo</span>'),
 ('<span class="etiqueta et-verde">Words to know</span>', '<span class="etiqueta et-verde">Palabras que debe conocer</span>'),
 ('<span class="etiqueta et-ambar">The most common mistake</span>', '<span class="etiqueta et-ambar">El error más común</span>'),
]
def F(a, b):
    """Fracción apilada como la escriben los constructores en inglés."""
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{a}</span><span class="fb2">{b}</span></span><span class="cap-oculto">{a}/{b}</span>'
# Textos frecuentes que pueden aparecer o no en una página: se cambian todos los que haya.
FRECUENTES = [
 ('<span aria-hidden="true">🧮</span> Open the calculator</button>', '<span aria-hidden="true">🧮</span> Abrir la calculadora</button>'),
 ('<span aria-hidden="true">🧮</span> Check it on the calculator</span>', '<span aria-hidden="true">🧮</span> Compruébelo en la calculadora</span>'),
 ('<strong>Step 1.</strong>', '<strong>Paso 1.</strong>'), ('<strong>Step 2.</strong>', '<strong>Paso 2.</strong>'),
 ('<strong>Step 3.</strong>', '<strong>Paso 3.</strong>'), ('<strong>Step 4.</strong>', '<strong>Paso 4.</strong>'),
 ('<strong>Result.</strong>', '<strong>Resultado.</strong>'),
 ('<span class="etiqueta et-verde">Tip</span>', '<span class="etiqueta et-verde">Consejo</span>'),
 ('<h3>Step by step</h3>', '<h3>Paso a paso</h3>'),
]
class Traductor:
    def __init__(self, en, alterna=None):
        self.en = en
        self.s = open(os.path.join(ROOT, en), encoding="utf-8").read()
        for a, b in COMUNES:
            if a in self.s: self.s = self.s.replace(a, b)
        for a, b in TODAS: self.s = self.s.replace(a, b)
        i = self.s.index("</title>")
        self.s = self.s[:i] + self.s[i:].replace('<link rel="icon"', '<link rel="alternate" hreflang="en" href="/' + en + '">\n<link rel="icon"', 1)
    def leccion(self, titulo_es):
        """Lección: quita el cuadro de estándares (lo pone ged_standards_es.py) y aplica los textos comunes."""
        import re
        self.s = re.sub(r"<!-- GED-STANDARDS -->.*?<!-- /GED-STANDARDS -->\n?", "", self.s, flags=re.S)
        for a, b in LECCION: self.s = self.s.replace(a, b)
        self.s = self.s.replace('<link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>\n<link rel="alternate"', '<link href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license"/>\n<link rel="alternate"')
    def js(self, texto):
        """Sustituye el objeto window.LESSON completo."""
        i = self.s.index("window.LESSON = "); j = self.s.index("</script>", i)
        self.s = self.s[:i] + "window.LESSON = " + texto.strip() + "\n" + self.s[j:]
    def cabecera(self, comentario):
        i = self.s.index("<!--"); j = self.s.index("-->", i) + 3
        self.s = self.s[:i] + comentario + self.s[j:]
    def frecuentes(self):
        for a, b in FRECUENTES: self.s = self.s.replace(a, b)
    def r(self, a, b, n=1):
        c = self.s.count(a)
        if c != n: sys.exit(f"[{self.en}] se esperaba {n}, hay {c}: {a[:90]!r}")
        self.s = self.s.replace(a, b)
    def todas(self, a, b):
        if a not in self.s: sys.exit(f"[{self.en}] no está: {a[:90]!r}")
        self.s = self.s.replace(a, b)
    def guarda(self, es):
        open(os.path.join(ROOT, es), "w", encoding="utf-8").write(self.s)
        print("ok", es)
