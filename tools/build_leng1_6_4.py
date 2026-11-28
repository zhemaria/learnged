# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.4 · Organización de datos en tablas.
Fuente: clases_leng1/clase_6-4.html (GEDparaHispanos) y gramatica/n1-l6-4.html, adaptadas al marco de LearnGED.
Temperaturas de enero: normales climáticas 1991–2020 de la NOAA, redondeadas (Chicago 25.2 °F en O'Hare; Miami unos 69 °F).
Las preguntas de la práctica se generan a partir de tablas de datos de ejemplo.
Uso: python3 tools/build_leng1_6_4.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-4"
# (título, encabezado de filas, encabezado de datos, unidad, filas, palabra para «más» y «menos»)
TABLAS = [("Minutos que caminó Rosa cada día", "Día", "Minutos", " min", [("Lunes", 20), ("Martes", 35), ("Miércoles", 15), ("Jueves", 40), ("Viernes", 25)], ("caminó más", "caminó menos")),
          ("Lluvia caída en cada mes (datos de ejemplo)", "Mes", "Pulgadas de lluvia", " pulg.", [("Marzo", 2.5), ("Abril", 3.6), ("Mayo", 4.1), ("Junio", 3.4), ("Julio", 1.9)], ("tuvo más lluvia", "tuvo menos lluvia")),
          ("Estudiantes inscritos en cada clase", "Clase", "Estudiantes", "", [("Inglés", 28), ("Ciudadanía", 15), ("Computación", 22), ("GED", 31), ("Costura", 12)], ("tiene más estudiantes", "tiene menos estudiantes")),
          ("Precio de la libra de frutas en el mercado", "Fruta", "Precio por libra", "", [("Plátano", "$0.69"), ("Manzana", "$1.49"), ("Uvas", "$2.99"), ("Mango", "$1.25"), ("Fresas", "$3.49")], ("es la más cara", "es la más barata")),
          ("Horas que abre cada biblioteca el sábado", "Biblioteca", "Horas abierta", " h", [("Las Flores", 6), ("Del Parque", 4), ("Central", 9), ("Del Lago", 5)], ("abre más horas", "abre menos horas"))]
BUS = ("Horario del autobús 12 (datos de ejemplo)", ["Parada", "Primer autobús", "Último autobús"],
       [["Calle Roble", "5:30 a. m.", "11:10 p. m."], ["Biblioteca", "5:38 a. m.", "11:18 p. m."], ["Hospital", "5:45 a. m.", "11:25 p. m."], ["Centro", "6:00 a. m.", "11:40 p. m."]])
CIUDADES = [("Chicago", 25), ("Nueva York", 34), ("Los Ángeles", 58), ("Miami", 69)]


def tabla_html(titulo, enc, filas):
    cab = "".join(f'<th scope="col">{e}</th>' for e in enc)
    cuerpo = "".join("<tr>" + f'<th scope="row">{f[0]}</th>' + "".join(f"<td>{x}</td>" for x in f[1:]) + "</tr>" for f in filas)
    return f'<table class="tabla-ej"><caption>{titulo}</caption><thead><tr>{cab}</tr></thead><tbody>{cuerpo}</tbody></table>'


def valor(v):
    return float(str(v).replace("$", "")) if not isinstance(v, (int, float)) else v


MAPA_US = """<figure class="figura"><svg viewBox="0 0 520 300" role="img" aria-labelledby="us-t us-d" style="width:100%;max-width:520px">
<title id="us-t">Mapa de Estados Unidos (simplificado)</title><desc id="us-d">Mapa simplificado con el norte arriba. Chicago y Nueva York están arriba, en el norte; Chicago en el centro y Nueva York a la derecha, en el este. Los Ángeles está a la izquierda, en el oeste, un poco más abajo. Miami está abajo a la derecha, en el extremo sur.</desc>
<path d="M40 70 L470 50 L480 120 L440 170 L420 200 L440 270 L415 275 L380 215 L300 225 L250 250 L200 235 L120 230 L60 190 L35 130 Z" fill="#e0f2fe" stroke="#0b679c" stroke-width="3"/>
<circle cx="300" cy="105" r="7" fill="#b42318"/><text x="300" y="92" text-anchor="middle" font-size="16" font-weight="700">Chicago</text>
<circle cx="440" cy="95" r="7" fill="#b42318"/><text x="430" y="82" text-anchor="middle" font-size="16" font-weight="700">Nueva York</text>
<circle cx="70" cy="180" r="7" fill="#b42318"/><text x="82" y="205" text-anchor="start" font-size="16" font-weight="700">Los Ángeles</text>
<circle cx="425" cy="258" r="7" fill="#b42318"/><text x="410" y="262" text-anchor="end" font-size="16" font-weight="700">Miami</text>
<g transform="translate(490 30)"><polygon points="0,-18 6,4 0,0 -6,4" fill="#b42318"/><text x="0" y="22" text-anchor="middle" font-size="15" font-weight="800">N</text></g></svg>
<figcaption>Figura 1: Ubicación de cuatro ciudades.</figcaption></figure>"""


def leccion():
    P = C.Practicas()
    bib = tabla_html("Hora de apertura de cuatro bibliotecas (datos de ejemplo)", ["Biblioteca", "Hora de apertura"],
                     [["Las Flores", "9:00 a. m."], ["Del Parque", "10:00 a. m."], ["Central", "8:00 a. m."], ["Del Lago", "11:00 a. m."]])
    s1 = f"""<p>Una <strong>tabla</strong> organiza los datos en <strong>filas</strong> (horizontales) y <strong>columnas</strong> (verticales) para encontrar información exacta en segundos. Aparece mucho en el GED.</p>
<ul><li><strong>Filas:</strong> cada una tiene los datos de un mismo elemento (una biblioteca, un día, una ciudad).</li><li><strong>Columnas:</strong> cada una tiene el mismo tipo de dato para todos (todas las horas, todos los precios).</li></ul>
{C.caja("tip", "Idea central", "<p>Cada dato está en el <strong>cruce</strong> de una fila con una columna. Para encontrarlo, busque la fila correcta y la columna correcta, y mire dónde se encuentran. A eso se le llama <strong>cruzar la información</strong>.</p>")}"""

    s2 = f"""{bib}
{C.tabla("Las cuatro partes de una tabla", ["Parte", "Qué es"],
         [["1 · Título", "Arriba. Dice el tema de la tabla."], ["2 · Encabezados", "Arriba de cada columna. Dicen qué tipo de dato hay en ella: «Biblioteca», «Hora de apertura»."],
          ["3 · Columnas", "De arriba abajo. Cada una guarda el mismo tipo de dato."], ["4 · Filas", "De izquierda a derecha. Cada una es un elemento con toda su información."]])}
<h3>Cruzar la información, paso a paso</h3>
<p><strong>Pregunta:</strong> ¿A qué hora abre la biblioteca Del Parque?</p>
<ol><li><strong>La fila:</strong> busque «Del Parque» en la primera columna.</li><li><strong>La columna:</strong> la pregunta es de la hora, así que mire «Hora de apertura».</li>
<li><strong>El cruce:</strong> donde se encuentran está la respuesta: <strong>10:00 a. m.</strong></li></ol>
{C.caja("tip", "Regla práctica", "<p>Antes de buscar, pregúntese: <strong>¿qué fila necesito?</strong> y <strong>¿qué columna necesito?</strong> El cruce de las dos es la respuesta.</p>")}
{P("Compruebe", "¿Qué biblioteca abre más temprano?", ["Central", "Del Lago", "Las Flores"], 0, {1: "Del Lago abre a las 11:00, la más tarde.", 2: "Las Flores abre a las 9:00; hay una que abre antes."}, "<strong>Central</strong>, a las 8:00 a. m.")}"""

    temp = tabla_html("Temperatura promedio en enero", ["Ciudad", "Temperatura"], [[c, f"{t} °F"] for c, t in CIUDADES])
    s3 = f"""<p>En Ciencias y en Estudios Sociales, a veces hay que juntar la información de una tabla con la de un mapa.</p>
{MAPA_US}
{temp}
<p class="nota-fina">Tabla 1: Promedio de enero. Fuente: NOAA, normales climáticas 1991–2020 (valores redondeados).</p>
{P("Pregunta 1", "¿Cuál es la temperatura promedio de Chicago en enero?", ["25 °F", "58 °F", "69 °F"], 0, {1: "Esa es la de Los Ángeles.", 2: "Esa es la de Miami."}, "Fila «Chicago», columna «Temperatura»: <strong>25 °F</strong>.")}
{P("Pregunta 2", "¿Hacia dónde queda Miami con respecto a Chicago?", ["al sur", "al norte", "al oeste"], 0, {1: "Miami está abajo en el mapa.", 2: "Miami está abajo y un poco a la derecha."}, "<strong>Al sur</strong> (y un poco al este).")}
{P("Pregunta 3", "Juntando el mapa y la tabla, ¿qué se observa?", ["En estos datos, las ciudades más al sur son más cálidas", "En estos datos, las ciudades más al norte son más cálidas", "No hay ninguna relación"], 0,
   {1: "Chicago y Nueva York, al norte, son las más frías.", 2: "Sí se ve una tendencia."}, "Las ciudades más al sur tienen temperaturas más altas. Con solo cuatro ciudades es una <strong>tendencia</strong>, no una regla.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Conteste las tres preguntas con el horario. En cada una, anote qué fila y qué columna usó.</p>
{tabla_html(*BUS)}
<ol><li>¿A qué hora pasa el primer autobús por el hospital?</li><li>¿A qué hora pasa el último autobús por el centro?</li><li>¿Cuántos minutos tarda el primer autobús en ir de la Calle Roble al centro?</li></ol></div>
<details class="caja caja-tip"><summary><strong>Ya contesté: ver las respuestas</strong></summary>
<ol><li><strong>5:45 a. m.</strong> Fila «Hospital», columna «Primer autobús».</li><li><strong>11:40 p. m.</strong> Fila «Centro», columna «Último autobús».</li>
<li><strong>30 minutos.</strong> En la columna «Primer autobús», sale de la Calle Roble a las 5:30 y llega al centro a las 6:00.</li></ol></details>"""

    secciones = [("s1", "¿Qué es una tabla?", s1), ("s2", "Las partes de una tabla", s2), ("s3", "Práctica: tabla y mapa juntos", s3)]
    tarea = [("Una tabla de mi vida.", "Haga en su cuaderno una tabla con título, encabezados y al menos cuatro filas: sus gastos de la semana, el horario de su familia o los precios de cinco cosas que compra."),
             ("Cruzar.", "Escriba tres preguntas que se respondan cruzando una fila y una columna de su tabla, y respóndalas."),
             ("Comparar.", "Escriba cuál es el dato más alto y cuál el más bajo de una columna.")]
    quiz = [
        ("¿Cómo van las filas?", ["De izquierda a derecha", "De arriba abajo"], 0, {}, "<strong>De izquierda a derecha</strong> (horizontales)."),
        ("¿Cómo van las columnas?", ["De arriba abajo", "De izquierda a derecha"], 0, {}, "<strong>De arriba abajo</strong> (verticales)."),
        ("¿Qué dicen los encabezados?", ["Qué tipo de dato hay en cada columna", "El tema de la tabla", "El dato más alto"], 0, {1: "Eso es el título.", 2: "No."}, "Qué <strong>tipo de dato</strong> hay en cada columna."),
        ("¿Dónde está un dato en la tabla?", ["En el cruce de una fila y una columna", "Siempre en la primera fila", "En el título"], 0, {1: "No.", 2: "No."}, "En el <strong>cruce</strong>."),
        ("En la tabla del autobús, ¿a qué hora pasa el último autobús por la biblioteca?", ["11:18 p. m.", "5:38 a. m.", "11:10 p. m."], 0, {1: "Esa es la columna del primer autobús.", 2: "Esa es la fila de la Calle Roble."}, "<strong>11:18 p. m.</strong>"),
        ("¿Qué ciudad tiene la temperatura más baja en enero?", ["Chicago", "Nueva York", "Miami"], 0, {1: "Nueva York tiene 34 °F; hay una más baja.", 2: "Miami es la más cálida."}, "<strong>Chicago</strong>, con 25 °F."),
        ("¿Qué pregunta conviene hacerse antes de buscar un dato?", ["¿Qué fila y qué columna necesito?", "¿Cuántas filas hay?"], 0, {}, "<strong>¿Qué fila y qué columna necesito?</strong>"),
        ("¿Cuántas filas de datos tiene la tabla de temperaturas (sin el encabezado)?", ["Cuatro", "Tres", "Cinco"], 0, {1: "Cuente las ciudades.", 2: "Cuente las ciudades."}, "<strong>Cuatro</strong>."),
        ("¿Para qué sirve el título de una tabla?", ["Dice el tema", "Da el dato más alto"], 0, {}, "Dice el <strong>tema</strong>."),
        ("Con solo cuatro ciudades, «las del sur son más cálidas» es…", ["una tendencia de estos datos", "una regla para todas las ciudades"], 0, {}, "Una <strong>tendencia</strong>: con más datos podría haber excepciones."),
    ]
    filas = [
        ("Partes de la tabla", "Reconozco el título, los encabezados, las filas y las columnas.", "Confundo filas y columnas.", "No las distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Cruzar", "Encuentro cualquier dato en el cruce de fila y columna.", "A veces miro la columna equivocada.", "No sé dónde buscar (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Comparar y combinar", "Comparo datos y los junto con un mapa.", "Comparo, pero me cuesta juntar con el mapa.", "No lo intento (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe leer tablas y cruzar sus datos. En la próxima lección va a leer <strong>gráficas de barras y circulares</strong>.</p>"
    glosario = [("Tabla", "Datos organizados en filas y columnas."), ("Fila", "Línea horizontal de una tabla."), ("Columna", "Línea vertical de una tabla."),
                ("Encabezado", "Texto arriba de cada columna que dice qué dato hay en ella."), ("Cruzar la información", "Buscar el dato donde se encuentran una fila y una columna.")]
    conexion = ("<p>En la Lección 6.3 leyó mapas. Ahora va a estudiar otra herramienta que aparece muchísimo en el GED: la tabla. Parece simple, pero tiene una lógica muy útil.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.7.4", "R.9.1/R.7.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Una fila, una columna y, en el cruce, la respuesta.", ["R.7 · Información visual", "Tablas"],
                            ["<strong>Reconocer</strong> las partes de una tabla.", "<strong>Cruzar</strong> una fila y una columna para encontrar un dato.",
                             "<strong>Comparar</strong> los datos de una columna.", "<strong>Combinar</strong> una tabla con un mapa."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-5", LE.titulo("6-5")), glosario, P)


def practica():
    r = random.Random(64)
    cru, comp = [], []
    for tit, ef, ed, u, filas, (mas, menos) in TABLAS:
        t = tabla_html(tit, [ef, ed], [[f, (str(v) + u) if not isinstance(v, str) else v] for f, v in filas])
        txt = lambda v: (str(v) + u) if not isinstance(v, str) else v
        for f, v in r.sample(filas, 3):
            otras = [txt(x) for g, x in filas if g != f]
            cru.append({"enun": f"{t}¿Qué dato está en el cruce de la fila <strong>{f}</strong> con la columna <strong>{ed}</strong>?", "ops": [txt(v)] + r.sample(otras, 2), "ok": 0,
                        "pista": f"Ponga el dedo en la fila «{f}» y muévalo hasta la columna «{ed}».", "exp": f"Fila «{f}», columna «{ed}»: <strong>{txt(v)}</strong>."})
        orden = sorted(filas, key=lambda x: valor(x[1]))
        alto, bajo = orden[-1][0], orden[0][0]
        medio = [g for g, _ in filas if g not in (alto, bajo)]
        comp.append({"enun": f"{t}Según la tabla, ¿qué {ef.lower()} {mas}?", "ops": [alto, bajo] + r.sample(medio, 1), "ok": 0, "pista": f"Compare todos los números de la columna «{ed}» y busque el más alto.",
                     "exp": f"<strong>{alto}</strong>: tiene el valor más alto de la columna."})
        comp.append({"enun": f"{t}Según la tabla, ¿qué {ef.lower()} {menos}?", "ops": [bajo, alto] + r.sample(medio, 1), "ok": 0, "pista": f"Compare todos los números de la columna «{ed}» y busque el más bajo.",
                     "exp": f"<strong>{bajo}</strong>: tiene el valor más bajo de la columna."})
    mods = [("cruzar", "Cruce la fila y la columna", C.om("m1", "Busque el dato en el cruce.")),
            ("comparar", "Compare los datos", C.om("m2", "Busque el valor más alto o el más bajo de la columna."))]
    js = C.js_datos("CRU", cru) + C.js_datos("COMP", comp) + 'creaBanco("m1", CRU);\ncreaBanco("m2", COMP);\n'
    return C.pagina_practica(N, LE.titulo(N), "Dos actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
