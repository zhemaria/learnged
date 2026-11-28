# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.2 · Las características del texto informativo visual.
Fuente: clases_leng1/clase_6-2.html (GEDparaHispanos) y gramatica/n1-l6-2.html, adaptadas al marco de LearnGED.
Dato de la llave que gotea: EPA WaterSense (una gota por segundo puede desperdiciar más de 3,000 galones al año).
Uso: python3 tools/build_leng1_6_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-2"
PISTAS = ["El título", "Un subtítulo", "Un rótulo", "El pie de foto"]
CUAL = [("Está arriba de todo, en letra grande, y anuncia el tema del artículo.", 0), ("«Los volcanes de Centroamérica», en letra grande al comienzo de la página.", 0),
        ("«La salud de sus dientes», arriba del artículo, en letras grandes y de color.", 0), ("Divide el artículo en partes y dice de qué trata cada una.", 1),
        ("«1. Cómo se forman los volcanes», en negrita, en medio del artículo.", 1), ("«Qué comer para cuidar los dientes», en negrita antes de un párrafo.", 1),
        ("Son palabras cortas dentro de la imagen, con una flecha que señala una parte.", 2), ("Dentro del dibujo de un diente, la palabra «esmalte» con una línea que señala la capa de afuera.", 2),
        ("En el dibujo de un volcán, la palabra «cráter» escrita en la punta.", 2), ("En un diagrama del corazón, las palabras «aurícula» y «ventrículo» junto a cada parte.", 2),
        ("Está debajo de la foto y explica qué se ve, dónde y cuándo.", 3), ("«Figura 2: El volcán de Fuego, en Guatemala, durante la erupción de 2018.» Debajo de una foto.", 3),
        ("«Una dentista revisa a un niño en la clínica del barrio.» En letra pequeña debajo de la imagen.", 3), ("«Voluntarios plantan árboles en el parque el 22 de abril.» En cursiva, debajo de la foto.", 3)]
# Artículos de práctica: (título, subtítulo, secciones, emojis, descripción, rótulos, pie)
ARTS = [("Los árboles de la ciudad", "Por qué refrescan las calles en verano", ["La sombra", "El agua de las hojas"], "🌳 🏘️ 🌳", "Una calle con árboles.", ["sombra", "hojas", "raíces"],
         "Figura 1: Una calle con árboles puede estar varios grados más fresca que una calle sin ellos."),
        ("El huerto de la escuela", "Cómo los niños aprenden a sembrar", ["Preparar la tierra", "Regar y cuidar"], "🍅 🥬 🚿", "Un huerto con tomates, lechugas y una manguera.", ["tomates", "lechugas", "manguera"],
         "Figura 1: Niños de tercer grado siembran tomates en el huerto, en abril."),
        ("La vacuna contra la gripe", "Quién debe ponérsela y cuándo", ["Por qué cambia cada año", "Dónde conseguirla"], "💪 🩹", "Un brazo con una curita.", ["hombro"],
         "Figura 1: Una enfermera aplica la vacuna en la clínica comunitaria."),
        ("La biblioteca del barrio", "Mucho más que libros", ["Computadoras gratis", "Clases para adultos", "La hora del cuento"], "📚 💻 🧑‍🏫", "Libros, una computadora y un maestro.", ["libros", "computadoras"],
         "Figura 1: Vecinos usan las computadoras de la biblioteca un sábado por la mañana.")]


def articulo(tit, sub, secs, emo, desc, rot, pie, num=False, cuerpo=""):
    n = (lambda k: f'<span class="art-num" aria-hidden="true">{k}</span>') if num else (lambda k: "")
    secs_html = "".join(f"<h5>{i + 1}. {s}</h5>" for i, s in enumerate(secs)) if isinstance(secs, list) else secs
    rots = "".join(f'<span class="art-rot">{r}</span>' for r in rot)
    return (f'<article class="articulo"><p class="art-tit">{tit}{n(1)}</p><p class="art-sub">{sub}{n(2)}</p>{cuerpo}'
            f'<figure><div class="art-fig"><span class="escena" role="img" aria-label="{desc}">{emo}</span><div class="art-rots">{rots}{n(3)}</div></div>'
            f'<figcaption>{pie}{n(4)}</figcaption></figure>{secs_html}</article>')


AGUA = ('<article class="articulo"><p class="art-tit">El agua potable en nuestra ciudad</p><p class="art-sub">De dónde viene y cómo llega a su llave</p>'
        '<h5>1. El recorrido del agua</h5><p>El agua que sale de su llave hace un viaje largo antes de llegar a su casa. Pasa por varias etapas en las que se limpia y se prueba para asegurar que sea segura para beber.</p>'
        '<figure><div class="art-fig"><span class="escena" role="img" aria-label="El lago, una planta de tratamiento, una tubería y una casa, unidos por flechas.">🌊 ➡️ 🏭 ➡️ 🚰 ➡️ 🏠</span>'
        '<div class="art-rots"><span class="art-rot">Lago Michigan</span><span class="art-rot">planta de tratamiento</span><span class="art-rot">tubería</span><span class="art-rot">su casa</span></div></div>'
        '<figcaption>Figura 1: El agua viaja del lago Michigan a la planta de tratamiento, y de ahí por tuberías hasta cada hogar de Chicago.</figcaption></figure>'
        '<h5>2. Cuidar el agua en casa</h5><p>Una llave que gotea parece un problema pequeño, pero gota a gota se pierde mucha agua. Revisar y reparar las fugas ayuda a cuidar este recurso y a pagar menos en la factura.</p>'
        '<figure><div class="art-fig"><span class="escena" role="img" aria-label="Una llave que gotea.">🚰 💧 💧 💧</span><div class="art-rots"><span class="art-rot">una gota por segundo</span></div></div>'
        '<figcaption>Figura 2: Una llave que gotea una vez por segundo puede desperdiciar más de 3,000 galones de agua en un año.</figcaption></figure></article>')


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Quien escribe un artículo informativo no quiere que usted se pierda. Por eso pone <strong>señales visuales</strong>, como los letreros de una carretera: dicen dónde está, qué viene y qué es importante. Las cuatro principales son:</p>
{C.tabla("Las cuatro pistas visuales", ["Pista", "Dónde está", "Para qué sirve"],
         [["1 · Título", "Arriba, en letra grande.", "Anuncia el tema general."], ["2 · Subtítulo", "Debajo del título o al empezar cada sección.", "Dice el enfoque o de qué trata cada parte."],
          ["3 · Rótulo", "Dentro de la imagen.", "Nombra lo que se ve, a veces con una flecha."], ["4 · Pie de foto", "Debajo de la imagen, en letra pequeña.", "Explica qué se ve, dónde y cuándo. También se llama leyenda."]])}
{C.caja("tip", "Idea central", "<p>Estas pistas se leen <strong>antes</strong> que el texto. Son un mapa que dice dónde encontrar cada cosa. Si las salta, pierde la guía.</p>")}
{C.caja("ojo", "Ojo con «leyenda»", "<p>En un artículo, <em>leyenda</em> puede ser el pie de foto. En un mapa, la leyenda es otra cosa: el cuadro que explica los símbolos. Lo verá en la Lección 6.3.</p>")}"""

    s2 = f"""
{articulo("Las abejas y nuestra comida", "Por qué su desaparición es un problema para todos", "<p>Las abejas son insectos pequeños que cumplen una función enorme. Cuando vuelan de flor en flor para alimentarse, llevan polen de una a otra sin darse cuenta…</p>",
          "🐝 🌸", "Una abeja sobre una flor.", ["abeja", "flor", "polen"], "Las abejas llevan polen de una flor a otra. Sin ellas, muchas frutas y verduras no existirían.", num=True)}
<p>1 es el <strong>título</strong>; 2, el <strong>subtítulo</strong>; 3, los <strong>rótulos</strong>; 4, el <strong>pie de foto</strong>.</p>
{C.tabla("El título y el pie de foto no son lo mismo", ["", "Título", "Pie de foto"],
         [["Dónde", "Arriba, en letra grande.", "Justo debajo de la imagen, en letra pequeña."], ["Qué hace", "Anuncia el tema de todo el artículo.", "Explica una imagen."],
          ["Tamaño", "De 3 a 10 palabras.", "De 1 a 3 oraciones."]])}
{C.caja("tip", "Pista de examen", "<p>Cuando una pregunta dice «según la imagen…» o «según la figura…», lea el <strong>pie de foto</strong> y los <strong>rótulos</strong>: muchas veces ahí está el dato.</p>")}
{P("Compruebe", "«Por qué su desaparición es un problema para todos» es…", PISTAS, 1, {0: "El título es «Las abejas y nuestra comida».", 2: "No está dentro de la imagen.", 3: "No está debajo de la imagen."}, "El <strong>subtítulo</strong>: dice el enfoque.")}"""

    s3 = f"""<h3>Búsqueda del tesoro</h3>
<p>Responda las preguntas leyendo <strong>solo</strong> el título, el subtítulo, los subtítulos de sección, los rótulos y los pies de foto.</p>
{AGUA}
{P("Pregunta 1", "¿Cuál es el tema general del artículo?", ["El agua potable de la ciudad", "Las tuberías rotas", "El lago Michigan"], 0, {1: "Solo es una parte.", 2: "Es de donde viene el agua, no el tema."}, "Lo dice el <strong>título</strong>.")}
{P("Pregunta 2", "¿De dónde viene el agua de Chicago?", ["Del lago Michigan", "De un río", "De la lluvia"], 0, {1: "Mire los rótulos de la Figura 1.", 2: "Mire los rótulos de la Figura 1."}, "Del <strong>lago Michigan</strong>: lo dicen el rótulo y el pie de la Figura 1.")}
{P("Pregunta 3", "¿Cuánta agua puede desperdiciar en un año una llave que gotea una vez por segundo?", ["Más de 3,000 galones", "Una gota", "Más de 300 galones"], 0, {1: "Eso es por segundo.", 2: "Lea el número del pie de la Figura 2 con cuidado."}, "<strong>Más de 3,000 galones</strong>: lo dice el pie de la Figura 2.")}
{P("Pregunta 4", "¿En qué sección se habla de las fugas?", ["2. Cuidar el agua en casa", "1. El recorrido del agua"], 0, {}, "En la sección <strong>2</strong>: su subtítulo lo anuncia.")}"""

    secciones = [("s1", "Las pistas visuales del texto", s1), ("s2", "Un artículo por dentro", s2), ("s3", "Práctica: búsqueda del tesoro", s3)]
    tarea = [("Un artículo de verdad.", "Busque un artículo con imágenes en una revista, un folleto o una página de internet."),
             ("Las cuatro pistas.", "Copie en su cuaderno el título, un subtítulo, un rótulo (si lo hay) y un pie de foto, y escriba al lado qué pista es cada uno."),
             ("Sin leer todo.", "Escriba dos preguntas que se puedan responder solo con esas pistas, y respóndalas.")]
    quiz = [
        ("¿Para qué sirven las pistas visuales de un artículo?", ["Para encontrar la información más rápido", "Para adornar la página", "Para alargar el texto"], 0, {1: "No son adorno.", 2: "No."}, "Para <strong>encontrar la información</strong>."),
        ("¿Dónde está el título?", ["Arriba, en letra grande", "Debajo de la foto", "Dentro de la imagen"], 0, {1: "Ese es el pie de foto.", 2: "Ese es el rótulo."}, "<strong>Arriba, en letra grande.</strong>"),
        ("¿Qué hace un subtítulo de sección?", ["Dice de qué trata esa parte", "Explica la foto", "Nombra una parte del dibujo"], 0, {1: "Eso hace el pie de foto.", 2: "Eso hace el rótulo."}, "Dice de qué trata <strong>esa parte</strong>."),
        ("La palabra «cráter» en la punta del dibujo de un volcán es…", PISTAS, 2, {0: "No anuncia el tema.", 1: "No divide el artículo.", 3: "No está debajo de la imagen."}, "Un <strong>rótulo</strong>."),
        ("«Figura 1: Vecinos limpian el parque el sábado.» Debajo de una foto. Es…", PISTAS, 3, {0: "No está arriba.", 1: "No divide el artículo.", 2: "No está dentro de la imagen."}, "El <strong>pie de foto</strong>."),
        ("Si una pregunta dice «según la figura», ¿qué conviene leer?", ["El pie de foto y los rótulos", "Solo el título"], 0, {}, "El <strong>pie de foto y los rótulos</strong>."),
        ("En un mapa, ¿qué es la leyenda?", ["El cuadro que explica los símbolos", "El título del mapa"], 0, {}, "El cuadro que <strong>explica los símbolos</strong>."),
        ("¿Qué se lee primero en un artículo informativo?", ["Las pistas visuales", "El último párrafo"], 0, {}, "Las <strong>pistas visuales</strong>: son el mapa del artículo."),
        ("¿Cuántas palabras suele tener un título?", ["De 3 a 10", "Más de 50", "Una sola letra"], 0, {1: "Eso sería un párrafo.", 2: "No."}, "<strong>De 3 a 10.</strong>"),
        ("En el artículo del agua, ¿cuántas secciones hay?", ["Dos", "Una", "Cuatro"], 0, {1: "Cuente los subtítulos numerados.", 2: "Cuente los subtítulos numerados."}, "<strong>Dos</strong>."),
    ]
    filas = [
        ("Reconocer las pistas", "Distingo título, subtítulo, rótulo y pie de foto.", "Confundo el pie de foto con el rótulo.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Usar las pistas", "Encuentro datos sin leer todo el artículo.", "Encuentro algunos, pero leo de más.", "Leo todo línea por línea (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe usar las señales de un artículo para encontrar la información. En la próxima lección va a leer <strong>mapas</strong>: título, leyenda, rosa de los vientos y escala.</p>"
    glosario = [("Título", "Texto grande arriba que anuncia el tema."), ("Subtítulo", "Texto que dice el enfoque o de qué trata cada sección."),
                ("Rótulo", "Palabra corta dentro de una imagen que nombra una parte."), ("Pie de foto", "Texto debajo de una imagen que explica lo que se ve. También se llama leyenda.")]
    conexion = ("<p>En la Lección 6.1 vio que las imágenes ayudan a comprender. Ahora va a estudiar las demás señales que el autor pone en un artículo para guiar al lector. Quien las reconoce encuentra la información rápido; quien no, pierde tiempo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una revista, un folleto o una página de internet con imágenes.</p>")
    estd = LE.estandares(["R.5.4", "R.7.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Título, subtítulos, rótulos y pies de foto: el mapa del artículo.", ["R.5.4 · Estructura", "R.7 · Información visual"],
                            ["<strong>Reconocer</strong> el título, los subtítulos, los rótulos y el pie de foto.", "<strong>Explicar</strong> para qué sirve cada uno.",
                             "<strong>Encontrar</strong> datos leyendo solo las pistas visuales."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-3", LE.titulo("6-3")), glosario, P)


def practica():
    cual = [{"enun": f"<strong>{d}</strong><br>¿Qué pista visual es?", "ops": PISTAS, "ok": k, "enOrden": True, "pista": "Título: arriba, el tema. Subtítulo: divide en partes. Rótulo: dentro de la imagen. Pie: debajo de la imagen.",
             "exp": f"Es <strong>{PISTAS[k].lower()}</strong>."} for d, k in CUAL]
    bus = []
    for tit, sub, secs, emo, desc, rot, pie in ARTS:
        art = articulo(tit, sub, secs, emo, desc, rot, pie)
        n = ["Una", "Dos", "Tres", "Cuatro"]
        bus += [{"enun": f"{art}¿Cuál es el tema general del artículo?", "ops": [tit, sub, secs[0]], "ok": 0, "enOrden": False, "pista": "El tema general lo anuncia la pista de arriba, en letra grande.", "exp": f"Lo dice el <strong>título</strong>: {tit}."},
                {"enun": f"{art}¿En qué se enfoca el artículo?", "ops": [sub, tit, secs[-1]], "ok": 0, "pista": "El enfoque lo dice el texto que va justo debajo del título.", "exp": f"Lo dice el <strong>subtítulo</strong>: {sub}."},
                {"enun": f"{art}¿Cuántas secciones tiene el artículo?", "ops": [n[len(secs) - 1]] + [x for x in n if x != n[len(secs) - 1]][:2], "ok": 0, "pista": "Cuente los subtítulos numerados.", "exp": f"<strong>{n[len(secs) - 1]}</strong>: hay {len(secs)} subtítulos numerados."},
                {"enun": f"{art}Según el pie de la Figura 1, ¿qué se ve en la imagen?", "ops": [pie.split(": ", 1)[1].rstrip("."), sub, tit], "ok": 0, "pista": "Lea el texto que está justo debajo de la imagen.", "exp": "Lo dice el <strong>pie de foto</strong>."}]
    mods = [("pistas", "¿Qué pista visual es?", C.om("m1", "Lea la descripción y decida qué pista visual es.")),
            ("buscar", "Encuentre el dato sin leer todo", C.om("m2", "Use solo las pistas visuales del artículo."))]
    js = C.js_datos("CUAL", cual) + C.js_datos("BUS", bus) + 'creaBanco("m1", CUAL);\ncreaBanco("m2", BUS);\n'
    return C.pagina_practica(N, LE.titulo(N), "Dos actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
