"""Level 4 · Lesson 1.2 · Slope: idea, formula, and meaning — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_1-2.html, algebra/n4-l1-2.html (two points, the four types, rate of change)
and interactivos/pendiente-dos-puntos (the slope in motion, with its challenge). All of them are rebuilt here, inside LearnGED.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4
from n4 import Plano, AZUL, ROJO

B.NIVEL = 4
N = "1-2"
TEMA = ("Analytic geometry", "Geometría analítica")
TIT = ("Slope: idea, formula, and meaning", "La pendiente: concepto, fórmula e interpretación")
SCRIPTS = n4.SCRIPTS
AVANCE, ELEVA = "#1565c0", "#c62828"

def fig_pendiente():
    p = Plano(-1, 6, -1, 6, 40)
    p.seg((-1 / 3, -1), (13 / 3, 6), "#90a4ae", 2.5)
    p.seg((1, 1), (3, 1), AVANCE, 3, "7 5").seg((3, 1), (3, 4), ELEVA, 3, "7 5")
    p.texto((2, 1), t("run = 2", "avance = 2"), AVANCE, 14, dy=16).texto((3, 2.5), t("rise = 3", "elevación = 3"), ELEVA, 14, "start", dx=10)
    p.punto((1, 1), AZUL, "(1, 1)", "nw").punto((3, 4), AZUL, "(3, 4)", "nw").texto((4.3, 4.2), "m = 3/2", "#10174f", 16)
    return p.svg(t("A line through (1, 1) and (3, 4). From the first point to the second the line moves 2 to the right (the run) and 3 up (the rise), so its slope is 3/2.",
                   "Una recta que pasa por (1, 1) y (3, 4). Del primer punto al segundo la recta avanza 2 hacia la derecha (el avance) y sube 3 (la elevación), así que su pendiente es 3/2."), 380)

def fig_tipos():
    piezas = []
    for i, (nom, a, b) in enumerate(((t("Positive", "Positiva"), (-2, -2), (2, 2)), (t("Negative", "Negativa"), (-2, 2), (2, -2)), (t("Zero", "Cero"), (-2.5, 1), (2.5, 1)), (t("Undefined", "Indefinida"), (1, -2.5), (1, 2.5)))):
        ox = 10 + i * 135
        s = f'<rect x="{ox}" y="10" width="125" height="125" rx="10" fill="#fff" stroke="#cfd8dc"/>'
        s += f'<line x1="{ox + 10}" y1="72.5" x2="{ox + 115}" y2="72.5" stroke="#b0bec5" stroke-width="1.5"/><line x1="{ox + 62.5}" y1="20" x2="{ox + 62.5}" y2="125" stroke="#b0bec5" stroke-width="1.5"/>'
        X = lambda x: ox + 62.5 + x * 18; Y = lambda y: 72.5 - y * 18
        s += f'<line x1="{X(a[0])}" y1="{Y(a[1])}" x2="{X(b[0])}" y2="{Y(b[1])}" stroke="{AZUL}" stroke-width="4" stroke-linecap="round"/>'
        s += f'<text x="{ox + 62.5}" y="158" font-size="15" font-weight="700" fill="#10174f" text-anchor="middle">{nom}</text>'
        piezas.append(s)
    return B.svg("0 0 560 170", t("Four small graphs: a line that rises from left to right (positive slope), one that falls (negative slope), a horizontal line (zero slope), and a vertical line (undefined slope).",
                                  "Cuatro gráficas pequeñas: una recta que sube de izquierda a derecha (pendiente positiva), una que baja (pendiente negativa), una horizontal (pendiente cero) y una vertical (pendiente indefinida)."), "".join(piezas), 560)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 1.1.</strong> In Lesson 1.1 you found the horizontal change (Δx) and the vertical change (Δy) between two points to get the distance. This lesson uses exactly those two changes, but now as a <strong>quotient</strong>: the slope measures how much a line goes up or down (Δy) for each unit it moves to the right (Δx). It is the idea that connects the geometry of the plane with the algebra of the line in Lesson 1.3.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 1.1 se calcularon el cambio horizontal (Δx) y el cambio vertical (Δy) entre dos puntos para hallar la distancia. Esta lección usa exactamente esos dos cambios, pero ahora en forma de <strong>cociente</strong>: la pendiente mide cuánto sube o baja una recta (Δy) por cada unidad que avanza hacia la derecha (Δx). Es el concepto que une la geometría del plano con el álgebra de la recta de la Lección 1.3.")}</p>
<p>{t("The <strong>slope</strong> of a line, written with the letter <strong>m</strong>, measures how steep it is. It is the <strong>rise</strong> (how much it goes up or down, the vertical change) divided by the <strong>run</strong> (how far it moves to the right, the horizontal change):",
 "La <strong>pendiente</strong> de una recta, que se representa con la letra <strong>m</strong>, mide su inclinación. Es el cociente entre la <strong>elevación</strong> (cuánto sube o baja, el cambio vertical) y el <strong>avance</strong> (cuánto se desplaza a la derecha, el cambio horizontal):")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">{t("m = rise ÷ run = Δy ÷ Δx", "m = elevación ÷ avance = Δy ÷ Δx")}</p>
{fig_pendiente()}
{caja("tip", t("A key idea", "Una idea clave"), t("<p>The slope is the same all along a line. Whatever two points of the same line you choose, rise ÷ run always gives the same number.</p>", "<p>La pendiente es constante a lo largo de toda la recta. No importa qué par de puntos se elija sobre la misma recta: elevación entre avance siempre da el mismo número.</p>"))}
{enlace(n, t("slope", "pendiente"), t("the slope in motion", "la pendiente en movimiento"), t("Move two points on a line and watch how the rise, the run, and the slope change.", "Mueva dos puntos sobre una recta y observe cómo cambian la elevación, el avance y la pendiente."))}'''

    s2 = f'''<p>{t("When you know two points (x₁, y₁) and (x₂, y₂), find the slope with the formula:", "Cuando se conocen dos puntos (x₁, y₁) y (x₂, y₂), la pendiente se calcula con la fórmula:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">m = (y₂ − y₁) ÷ (x₂ − x₁)</p>
{ejemplo(t("Example 1: a positive slope. Find the slope of the line through (1, 2) and (4, 11).", "Ejemplo 1 · Pendiente positiva. Hallar la pendiente de la recta que pasa por (1, 2) y (4, 11)."),
  [("1", t("Rise (top).", "Elevación (numerador)."), "y₂ − y₁ = 11 − 2 = 9."),
   ("2", t("Run (bottom).", "Avance (denominador)."), "x₂ − x₁ = 4 − 1 = 3."),
   ("3", t("Divide.", "Cociente."), "m = 9 ÷ 3 = 3."),
   ("✓", t("Answer.", "Respuesta."), t("The slope is <strong>3</strong> (positive: the line goes up).", "La pendiente es <strong>3</strong> (positiva: la recta sube)."))])}
{ejemplo(t("Example 2: a negative slope. Find the slope of the line through (0, 0) and (5, −10).", "Ejemplo 2 · Pendiente negativa. Hallar la pendiente de la recta que pasa por (0, 0) y (5, −10)."),
  [("1", t("Rise.", "Elevación."), "−10 − 0 = −10."),
   ("2", t("Run.", "Avance."), "5 − 0 = 5."),
   ("3", t("Divide.", "Cociente."), "m = −10 ÷ 5 = −2."),
   ("✓", t("Answer.", "Respuesta."), t("The slope is <strong>−2</strong> (negative: the line goes down).", "La pendiente es <strong>−2</strong> (negativa: la recta baja)."))])}
{caja("ojo", t("Keep the same order", "Mantenga el mismo orden"), t("<p>The point you subtract first on top must be the point you subtract first on the bottom. If you switch only one of the two, the sign of the slope comes out wrong. Rise goes on top: Δx ÷ Δy is the most common mistake.</p>", "<p>El punto que se resta primero en el numerador debe ser el mismo que se resta primero en el denominador. Si se invierte solo uno de los dos, el signo de la pendiente sale mal. La elevación va arriba: Δx ÷ Δy es el error más común.</p>"))}
{practica("p1", t("Practice 1 — Through (1, 1) and (3, 7)", "Práctica 1 — Por (1, 1) y (3, 7)"), t("What is the slope of the line through (1, 1) and (3, 7)?", "¿Cuál es la pendiente de la recta que pasa por (1, 1) y (3, 7)?"), [("a", "1/3"), ("b", "2"), ("c", "3")])}
{practica("p2", t("Practice 2 — Through (0, 4) and (2, 0)", "Práctica 2 — Por (0, 4) y (2, 0)"), t("What is the slope of the line through (0, 4) and (2, 0)?", "¿Cuál es la pendiente de la recta que pasa por (0, 4) y (2, 0)?"), [("a", "2"), ("b", "−2"), ("c", "−1/2")])}
{practica("p3", t("Practice 3 — Through (2, 3) and (6, 3)", "Práctica 3 — Por (2, 3) y (6, 3)"), t("What is the slope of the line through (2, 3) and (6, 3)?", "¿Cuál es la pendiente de la recta que pasa por (2, 3) y (6, 3)?"), [("a", "0"), ("b", t("undefined", "indefinida")), ("c", "4")])}
{enlace(n, t("two-points", "dos-puntos"), t("the slope from two points", "la pendiente con dos puntos"), t("Find the rise, the run, and the quotient step by step, with new points every time.", "Calcule la elevación, el avance y el cociente paso a paso, con puntos nuevos cada vez."))}'''

    s3 = f'''<p>{t("The sign and the value of the slope describe the direction of the line. Always read lines from left to right.", "El signo y el valor de la pendiente describen la dirección de la recta. Las rectas se leen siempre de izquierda a derecha.")}</p>
{fig_tipos()}
{tabla(t("The four types of slope", "Los cuatro tipos de pendiente"), t("Types of slope: what the line looks like and the sign or value of m", "Tipos de pendiente: cómo se ve la recta y el signo o valor de m"),
  [t("Type", "Tipo"), t("What does the line look like?", "¿Cómo se ve la recta?"), t("Value of m", "Valor de m")],
  [[t("Positive", "Positiva"), t("It goes up from left to right.", "Sube de izquierda a derecha."), "m > 0"], [t("Negative", "Negativa"), t("It goes down from left to right.", "Baja de izquierda a derecha."), "m < 0"],
   [t("Zero", "Cero"), t("Horizontal (flat).", "Horizontal (plana)."), "m = 0"], [t("Undefined", "Indefinida"), t("Vertical.", "Vertical."), t("m does not exist (run = 0)", "m no existe (avance = 0)")]])}
{caja("ojo", t("Why is a vertical line undefined?", "¿Por qué la vertical es indefinida?"), t("<p>On a vertical line every point has the same x, so the run (x₂ − x₁) is 0. You cannot divide by 0, so the slope does not exist. On a horizontal line, the rise is 0, so m = 0 ÷ run = 0.</p>", "<p>En una recta vertical todos los puntos tienen la misma x, así que el avance (x₂ − x₁) es 0. Como no se puede dividir entre 0, la pendiente no existe. En cambio, en la horizontal la elevación es 0, así que m = 0 ÷ avance = 0.</p>"))}
<p>{t("To compare two lines, the <strong>steeper</strong> one has the larger <strong>absolute value</strong> of the slope. For example, a line with m = −5 is steeper than one with m = 3, even though one goes down and the other goes up.", "Para comparar dos rectas, la <strong>más empinada</strong> es la que tiene el mayor <strong>valor absoluto</strong> de la pendiente. Por ejemplo, una recta con m = −5 es más empinada que una con m = 3, aunque una baje y la otra suba.")}</p>
{practica("p4", t("Practice 4 — A line that goes up", "Práctica 4 — Una recta que sube"), t("A line that goes up from left to right has a slope that is…", "Una recta que sube de izquierda a derecha tiene pendiente…"), [("a", t("negative", "negativa")), ("b", t("zero", "cero")), ("c", t("positive", "positiva"))])}
{practica("p5", t("Practice 5 — A vertical line", "Práctica 5 — Una recta vertical"), t("A vertical line has a slope that is…", "Una recta vertical tiene pendiente…"), [("a", t("undefined", "indefinida")), ("b", t("zero", "cero")), ("c", t("positive", "positiva"))])}
{practica("p6", t("Practice 6 — The steepest line", "Práctica 6 — La más empinada"), t("Which slope belongs to the steepest line?", "¿Qué pendiente corresponde a la recta más empinada?"), [("a", "m = 2/3"), ("b", "m = 4"), ("c", "m = 1")])}
{enlace(n, t("types", "tipos"), t("the four types of slope", "los cuatro tipos de pendiente"), t("Positive, negative, zero, or undefined: recognize it on the graph and from the points.", "Positiva, negativa, cero o indefinida: reconózcala en la gráfica y en los puntos."))}'''

    s4 = f'''<p>{t("Outside the plane, the slope takes on a very useful meaning: it is a <strong>rate of change</strong>, that is, how much one quantity changes for each unit of the other. The units of a slope are always “units of y per unit of x.”", "Fuera del plano, la pendiente cobra un significado muy útil: es una <strong>tasa de cambio</strong>, es decir, cuánto cambia una cantidad por cada unidad de la otra. Las unidades de la pendiente son siempre «unidades de y por cada unidad de x».")}</p>
{tabla(t("The slope as a rate of change", "La pendiente como tasa de cambio"), t("Examples of the slope read as a rate of change in different situations", "Ejemplos de la pendiente interpretada como tasa de cambio en distintas situaciones"),
  [t("Situation", "Situación"), t("The slope is…", "La pendiente representa…")],
  [[t("Distance traveled vs. time", "Distancia recorrida vs. tiempo"), t("the speed (miles per hour).", "la velocidad (millas por hora).")], [t("Pay vs. hours worked", "Salario vs. horas trabajadas"), t("the pay per hour (dollars per hour).", "la paga por hora (dólares por hora).")],
   [t("Total cost vs. items bought", "Costo total vs. unidades compradas"), t("the price per item (dollars per item).", "el precio por unidad (dólares por unidad).")], [t("Water in a tank vs. time", "Agua en un tanque vs. tiempo"), t("how fast it fills or empties (gallons per minute).", "qué tan rápido se llena o se vacía (galones por minuto).")]])}
{ejemplo(t("Example 3: reading the slope. The graph of the distance a car travels (in miles) against time (in hours) is a line with slope 60. What does that slope mean?", "Ejemplo 3 · Interpretar la pendiente. La gráfica de la distancia que recorre un auto (en millas) en función del tiempo (en horas) es una recta de pendiente 60. ¿Qué significa esa pendiente?"),
  [("1", t("The units.", "Las unidades."), t("Miles per hour.", "Millas por hora.")),
   ("2", t("The meaning.", "El significado."), t("A slope of 60 means that for every hour that goes by, the distance grows by 60 miles.", "Una pendiente de 60 indica que, por cada hora que pasa, la distancia aumenta 60 millas.")),
   ("✓", t("Answer.", "Respuesta."), t("The car travels at a steady speed of <strong>60 miles per hour</strong>.", "El auto viaja a una velocidad constante de <strong>60 millas por hora</strong>."))])}
{caja("tip", t("The sign also has a meaning", "El signo también se interpreta"), t("<p>A positive rate means the quantity grows; a negative one, that it shrinks. A tank that empties at −10 gallons per minute loses 10 gallons every minute: say it in words, not only with the sign.</p>", "<p>Una tasa positiva indica que la cantidad aumenta; una negativa, que disminuye. Un tanque que se vacía a −10 galones por minuto pierde 10 galones cada minuto: conviene decirlo con palabras, no solo con el signo.</p>"))}
{practica("p7", t("Practice 7 — The electric bill", "Práctica 7 — La factura de la luz"), t("The graph of the total cost of electricity against the kilowatt-hours used is a line with slope 0.15 (dollars per kWh). What does the slope mean?", "La gráfica del costo total de la electricidad en función de los kilovatios-hora consumidos es una recta de pendiente 0.15 (dólares por kWh). ¿Qué representa la pendiente?"), [("a", t("Each extra kWh costs $0.15", "Cada kWh adicional cuesta $0.15")), ("b", t("The fixed charge for the service", "El cargo fijo del servicio")), ("c", t("The whole bill is $0.15", "El total de la factura es $0.15"))])}
{enlace(n, t("rate", "tasa"), t("the slope as a rate of change", "la pendiente como tasa de cambio"), t("Find the rate, with its units, from tables and graphs, and say what it means.", "Calcule la tasa con sus unidades a partir de tablas y gráficas, y diga qué significa."))}'''

    secciones = [("s-" + t("slope", "pendiente"), t("What is slope?", "¿Qué es la pendiente?"), s1),
                 ("s-" + t("two-points", "dos-puntos"), t("The slope from two points", "La pendiente a partir de dos puntos"), s2),
                 ("s-" + t("types", "tipos"), t("The four types of slope", "Los cuatro tipos de pendiente"), s3),
                 ("s-" + t("rate", "tasa"), t("The slope as a rate of change", "La pendiente como tasa de cambio"), s4)]

    U = t("undefined", "indefinida")
    lesson = {"next": t("Lesson 1.3", "Lección 1.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("You divided the run by the rise. The rise goes on top: 6 ÷ 2.", "Dividió el avance entre la elevación. La elevación va arriba: 6 ÷ 2."), "b": t("Check the rise: 7 − 1 = 6, and the run: 3 − 1 = 2.", "Revise la elevación: 7 − 1 = 6, y el avance: 3 − 1 = 2.")}, "right": "(7 − 1) ÷ (3 − 1) = 6 ÷ 2 = 3.", "solution": "m = 6 ÷ 2 = 3."},
      "p2": {"ok": "b", "hints": {"a": t("The line goes down (y goes from 4 to 0), so the slope is negative.", "La recta baja (la y pasa de 4 a 0), así que la pendiente es negativa."), "c": t("You divided the run by the rise. The rise goes on top: −4 ÷ 2.", "Dividió el avance entre la elevación. La elevación va arriba: −4 ÷ 2.")}, "right": "(0 − 4) ÷ (2 − 0) = −4 ÷ 2 = −2.", "solution": "m = −4 ÷ 2 = −2."},
      "p3": {"ok": "a", "hints": {"b": t("Undefined is for a vertical line (run = 0). Here the rise is 0.", "Indefinida es para una recta vertical (avance = 0). Aquí la elevación es 0."), "c": t("4 is the run. The rise is 3 − 3 = 0.", "4 es el avance. La elevación es 3 − 3 = 0.")}, "right": t("The rise is 0, so m = 0 ÷ 4 = 0: a horizontal line.", "La elevación es 0, así que m = 0 ÷ 4 = 0: una recta horizontal."), "solution": "m = 0 ÷ 4 = 0."},
      "p4": {"ok": "c", "hints": {"a": t("A negative slope goes down from left to right.", "Una pendiente negativa baja de izquierda a derecha."), "b": t("A zero slope is a flat, horizontal line.", "Una pendiente cero es una recta plana, horizontal.")}, "right": t("It goes up: m > 0.", "Sube: m > 0."), "solution": t("Positive.", "Positiva.")},
      "p5": {"ok": "a", "hints": {"b": t("Zero is for a horizontal line. On a vertical line the run is 0.", "Cero es para una horizontal. En una vertical el avance es 0."), "c": t("A vertical line neither rises nor falls from left to right: the run is 0.", "Una vertical no sube ni baja de izquierda a derecha: el avance es 0.")}, "right": t("The run is 0, and you cannot divide by 0.", "El avance es 0 y no se puede dividir entre 0."), "solution": U + "."},
      "p6": {"ok": "b", "hints": {"a": t("2/3 is less than 1: a gentle line.", "2/3 es menor que 1: una recta suave."), "c": t("Compare the absolute values: 4 is bigger than 1.", "Compare los valores absolutos: 4 es mayor que 1.")}, "right": t("4 has the largest absolute value.", "4 tiene el mayor valor absoluto."), "solution": "m = 4."},
      "p7": {"ok": "a", "hints": {"b": t("The fixed charge is where the line starts (when the kWh are 0), not the slope.", "El cargo fijo es donde empieza la recta (con 0 kWh), no la pendiente."), "c": t("The slope is a rate: dollars per kWh, not a total.", "La pendiente es una tasa: dólares por kWh, no un total.")}, "right": t("Dollars per kWh: each extra kWh adds $0.15.", "Dólares por kWh: cada kWh más suma $0.15."), "solution": t("$0.15 per kWh.", "$0.15 por kWh.")},
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("You divided the run by the rise.", "Dividió el avance entre la elevación."), "b": t("You added them. Divide the rise by the run.", "Los sumó. Divida la elevación entre el avance."), "c": t("Divide: 3 ÷ 2.", "Divida: 3 ÷ 2.")}, "solution": "m = 3 ÷ 2 = 3/2."},
      "B": {"ok": "c", "hints": {"a": t("It goes down, so the slope is negative.", "Baja, así que la pendiente es negativa."), "b": t("You divided the run by the rise.", "Dividió el avance entre la elevación."), "d": t("It goes down, and the rise goes on top: −4 ÷ 1.", "Baja, y la elevación va arriba: −4 ÷ 1.")}, "solution": "m = −4 ÷ 1 = −4."},
      "C": {"ok": "a", "hints": {"b": t("A slope of 1 rises one unit per unit of run.", "Una pendiente de 1 sube una unidad por cada unidad de avance."), "c": t("Undefined is for a vertical line.", "Indefinida es para una vertical."), "d": t("A horizontal line neither goes up nor down.", "Una horizontal no sube ni baja.")}, "solution": t("The rise is 0, so m = 0.", "La elevación es 0, así que m = 0.")},
      "D": {"ok": "b", "hints": {"a": t("9 is the rise. Divide it by the run, 3.", "9 es la elevación. Divídala entre el avance, 3."), "c": t("You divided the run by the rise.", "Dividió el avance entre la elevación."), "d": t("You added. Divide the rise by the run.", "Sumó. Divida la elevación entre el avance.")}, "solution": "(11 − 2) ÷ (4 − 1) = 9 ÷ 3 = 3."},
      "E": {"ok": "c", "hints": {"a": t("The line goes down (y goes from 0 to −10), so the slope is negative.", "La recta baja (la y pasa de 0 a −10), así que la pendiente es negativa."), "b": t("You divided the run by the rise.", "Dividió el avance entre la elevación."), "d": t("−10 is the rise. Divide it by the run, 5.", "−10 es la elevación. Divídala entre el avance, 5.")}, "solution": "−10 ÷ 5 = −2."},
      "F": {"ok": "a", "hints": {"b": t("Zero is for a horizontal line. Here x stays at 4: the run is 0.", "Cero es para una horizontal. Aquí la x se queda en 4: el avance es 0."), "c": t("6 is the rise. The run is 4 − 4 = 0.", "6 es la elevación. El avance es 4 − 4 = 0."), "d": t("Find the run: 4 − 4 = 0.", "Calcule el avance: 4 − 4 = 0.")}, "solution": t("The run is 0: a vertical line, undefined slope.", "El avance es 0: recta vertical, pendiente indefinida.")},
      "G": {"ok": "d", "hints": {"a": t("|1/2| is small: a gentle line.", "|1/2| es pequeño: una recta suave."), "b": t("Compare absolute values: |−5| = 5 is more than 3.", "Compare valores absolutos: |−5| = 5 es más que 3."), "c": t("A zero slope is flat.", "Una pendiente cero es plana.")}, "solution": t("|−5| = 5 is the largest absolute value.", "|−5| = 5 es el mayor valor absoluto.")},
      "H": {"ok": "c", "hints": {"a": t("The slope is a rate (per hour), not the total distance.", "La pendiente es una tasa (por hora), no la distancia total."), "b": t("The units are miles per hour, not hours.", "Las unidades son millas por hora, no horas."), "d": t("The units are miles and hours.", "Las unidades son millas y horas.")}, "solution": t("60 miles for each hour.", "60 millas por cada hora.")},
     }}

    quiz = [
     ("A", t("On a graph, a line goes up 3 units for every 2 units it moves to the right. What is its slope?", "En una gráfica, una recta sube 3 unidades por cada 2 que avanza a la derecha. ¿Cuál es su pendiente?"), [("a", "2/3"), ("b", "5"), ("c", "1"), ("d", "3/2")]),
     ("B", t("On a graph, a line goes down 4 units for every 1 unit it moves to the right. What is its slope?", "En una gráfica, una recta baja 4 unidades por cada 1 que avanza. ¿Cuál es su pendiente?"), [("a", "4"), ("b", "−1/4"), ("c", "−4"), ("d", "1/4")]),
     ("C", t("What is the slope of a horizontal line?", "¿Cuál es la pendiente de una recta horizontal?"), [("a", "0"), ("b", "1"), ("c", U), ("d", t("negative", "negativa"))]),
     ("D", t("What is the slope of the line through (1, 2) and (4, 11)?", "¿Cuál es la pendiente de la recta que pasa por (1, 2) y (4, 11)?"), [("a", "9"), ("b", "3"), ("c", "1/3"), ("d", "13")]),
     ("E", t("What is the slope of the line through (0, 0) and (5, −10)?", "¿Cuál es la pendiente de la recta que pasa por (0, 0) y (5, −10)?"), [("a", "2"), ("b", "−1/2"), ("c", "−2"), ("d", "−10")]),
     ("F", t("What is the slope of the line through (4, 1) and (4, 7)?", "¿Cuál es la pendiente de la recta que pasa por (4, 1) y (4, 7)?"), [("a", U), ("b", "0"), ("c", "6"), ("d", "3/2")]),
     ("G", t("Which of these slopes belongs to the steepest line?", "¿Cuál de estas pendientes corresponde a la recta más empinada?"), [("a", "m = 1/2"), ("b", "m = 3"), ("c", "m = 0"), ("d", "m = −5")]),
     ("H", t("The graph of distance (miles) against time (hours) is a line with slope 60. What does that mean?", "La gráfica de distancia (millas) en función del tiempo (horas) es una recta de pendiente 60. ¿Qué significa?"), [("a", t("It travels 60 miles in all", "Recorre 60 millas en total")), ("b", t("It takes 60 hours", "Tarda 60 horas")), ("c", t("It travels 60 miles each hour", "Recorre 60 millas por cada hora")), ("d", t("It goes 60 feet per second", "Va a 60 pies por segundo"))])]

    tarea = (t("For your own work, with a notebook and graph paper: (1) Six slopes from two points, two of them with negative coordinates. Write the rise and the run before you divide, and simplify the fraction. (2) Four lines drawn, one of each type (positive, negative, zero, and undefined). Explain in one sentence why each one has that slope. (3) Three different lines with slope 3/5 that go through different points. Write what they have in common and why. (4) Three situations from your daily life (a fee, a speed, a savings plan) written as a rate of change with units, and one sentence that explains each one. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y papel cuadriculado: (1) Seis pendientes a partir de dos puntos, dos de ellas con coordenadas negativas. Escriba la elevación y el avance antes de dividir, y simplifique la fracción. (2) Cuatro rectas dibujadas, una de cada tipo (positiva, negativa, cero e indefinida). Explique en una oración por qué cada una tiene esa pendiente. (3) Tres rectas distintas con pendiente 3/5 que pasen por puntos diferentes. Escriba qué tienen en común y por qué. (4) Tres situaciones de su vida diaria (una tarifa, una velocidad, un ahorro) expresadas como tasa de cambio con sus unidades, y una oración que interprete cada una. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Look at an electric, gas, or phone bill. Find the price per unit (per kWh, per therm, per GB) and write it as a slope: “dollars per ___.” If you used 100 more units, how much more would you pay? Then look for a road sign that warns about a steep grade (for example, “7% grade”): that percent is a slope too, 7 feet of rise for every 100 feet of run.",
               "Mire una factura de la luz, del gas o del teléfono. Busque el precio por unidad (por kWh, por therm, por GB) y escríbalo como una pendiente: «dólares por ___». Si consumiera 100 unidades más, ¿cuánto más pagaría? Después busque una señal de carretera que avise de una pendiente pronunciada (por ejemplo, «7% grade»): ese porcentaje también es una pendiente, 7 pies de elevación por cada 100 pies de avance."))

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("Find the slope of a line from its graph and from two points, tell the four types apart, and read the slope as a rate of change.", "Calcule la pendiente de una recta desde su gráfica y desde dos puntos, distinga los cuatro tipos y lea la pendiente como una tasa de cambio."),
        ("📐", t("Graph paper", "Papel cuadriculado")),
        [t("<strong>Find</strong> the slope of a line from its graph (rise ÷ run).", "<strong>Calcular</strong> la pendiente de una recta desde su gráfica (elevación entre avance)."),
         t("<strong>Find</strong> the slope from two points with the formula m = (y₂ − y₁) ÷ (x₂ − x₁).", "<strong>Calcular</strong> la pendiente a partir de dos puntos con la fórmula m = (y₂ − y₁) ÷ (x₂ − x₁)."),
         t("<strong>Identify</strong> positive, negative, zero, and undefined slopes.", "<strong>Identificar</strong> pendientes positivas, negativas, cero e indefinidas."),
         t("<strong>Read</strong> the slope as a rate of change and compare two lines by how steep they are.", "<strong>Interpretar</strong> la pendiente como una tasa de cambio y comparar dos rectas por su inclinación.")],
        secciones, tarea, quiz,
        t("Self-check checklist for slope", "Lista de autoevaluación de la pendiente"),
        t("Self-check checklist: skills for finding, classifying, and reading slope", "Lista de autoevaluación: destrezas para calcular, clasificar e interpretar la pendiente"),
        [(t("Finding the slope", "Calcular la pendiente"), t("I find the slope from a graph or from two points with no mistakes (rise over run).", "Calculo la pendiente desde la gráfica o desde dos puntos sin errores (elevación entre avance)."), t("I make occasional sign mistakes.", "Cometo errores ocasionales de signo."), t("I mix up the rise and the run, or flip the quotient.", "Confundo la elevación con el avance o invierto el cociente.")),
         (t("Identifying the type of slope", "Identificar el tipo de pendiente"), t("I tell the four types apart and compare steepness by the absolute value.", "Distingo los cuatro tipos y comparo inclinaciones por el valor absoluto."), t("I recognize some types but mix up zero and undefined.", "Reconozco algunos tipos, pero confundo cero con indefinida."), t("I cannot tell the four types apart.", "No distingo los cuatro tipos.")),
         (t("Reading it as a rate of change", "Interpretar como tasa de cambio"), t("I read the slope as a rate with the right units and explain what its sign means.", "Interpreto la pendiente como tasa con las unidades correctas y explico qué significa su signo."), t("I read the slope but leave out or confuse the units.", "Interpreto la pendiente, pero omito o confundo las unidades."), t("I do not connect the slope with a real meaning.", "No relaciono la pendiente con un significado real."))],
        t("<p>In this lesson you defined the <strong>slope</strong> as rise over run (Δy ÷ Δx), found it from a graph and from two points, sorted the four types (positive, negative, zero, and undefined), and read it as a <strong>rate of change</strong> with units.</p>\n<p>In <strong>Lesson 1.3 · Equations of a line</strong> you will put the slope and the intercept together to <strong>write the equation</strong> of a line. You will use the form y = mx + b, change between the three forms of the equation, and recognize <strong>parallel</strong> lines (the same slope) and <strong>perpendicular</strong> lines (negative reciprocal slopes).</p>",
          "<p>En esta lección se definió la <strong>pendiente</strong> como elevación entre avance (Δy ÷ Δx), se calculó desde una gráfica y desde dos puntos, se clasificaron los cuatro tipos (positiva, negativa, cero e indefinida) y se interpretó como una <strong>tasa de cambio</strong> con unidades.</p>\n<p>En la <strong>Lección 1.3 · Ecuaciones de la recta</strong> se unirán la pendiente y el intercepto para <strong>escribir la ecuación</strong> de una recta. Se usará la forma y = mx + b, se convertirá entre las tres formas de la ecuación y se reconocerán las rectas <strong>paralelas</strong> (misma pendiente) y <strong>perpendiculares</strong> (pendientes recíprocas negativas).</p>"),
        ("1-3", ("", t("Lesson 1.3 · Equations of a line: slope-intercept, point-slope, and standard form", "Lección 1.3 · Ecuaciones de la recta: pendiente-intercepto, punto-pendiente y forma estándar"))),
        [(t("slope (m)", "pendiente (m)"), t("How steep a line is: rise ÷ run, Δy ÷ Δx.", "La inclinación de una recta: elevación ÷ avance, Δy ÷ Δx.")),
         (t("rise", "elevación"), t("The vertical change between two points, y₂ − y₁.", "El cambio vertical entre dos puntos, y₂ − y₁.")),
         (t("run", "avance"), t("The horizontal change between two points, x₂ − x₁.", "El cambio horizontal entre dos puntos, x₂ − x₁.")),
         (t("undefined slope", "pendiente indefinida"), t("The slope of a vertical line: the run is 0.", "La pendiente de una recta vertical: el avance es 0.")),
         (t("rate of change", "tasa de cambio"), t("How much one quantity changes for each unit of another, like miles per hour.", "Cuánto cambia una cantidad por cada unidad de otra, como millas por hora."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function frase(dy, dx){
  if (dx === 0 && dy === 0) return T("The two points are the same point: move one of them.", "Los dos puntos coinciden: mueva uno de ellos.");
  if (dx === 0) return T("The run is 0: the line is vertical and the slope is undefined (you cannot divide by 0).", "El avance es 0: la recta es vertical y la pendiente es indefinida (no se puede dividir entre 0).");
  if (dy === 0) return T("The rise is 0: the line is horizontal and the slope is 0.", "La elevación es 0: la recta es horizontal y la pendiente es 0.");
  var m = fr(dy, dx), up = fval(m) > 0, sube = Math.abs(m.n), av = m.d;
  return (up ? T("The line goes up ", "La recta sube ") : T("The line goes down ", "La recta baja ")) + sube + (sube === 1 ? T(" unit", " unidad") : T(" units", " unidades")) + T(" for every ", " por cada ") + av + (av === 1 ? T(" unit", " unidad") : T(" units", " unidades")) + T(" it moves to the right.", " que avanza hacia la derecha.");
}
/* ===== MODULE 1 · The slope in motion ===== */
var MV = PlanoArrastre($("mv-plano"), {xmin: -8, xmax: 8, ymin: -8, ymax: 8, u: 30, paso: 2}, [{x: 1, y: 1, nombre: "A", color: C4.azul}, {x: 3, y: 4, nombre: "B", color: C4.morado}],
  function(pts, P){
    var a = [pts[0].x, pts[0].y], b = [pts[1].x, pts[1].y], dx = b[0] - a[0], dy = b[1] - a[1];
    if (typeof mvLee === "function") mvLee(a, b);
    return rectaPor(P, a, b, "#90a4ae", 3) + trianguloPendiente(P, a, b);
  }, T("Coordinate plane with two points, A and B, that you can move. The line through them and the run-and-rise triangle are drawn.", "Plano cartesiano con dos puntos, A y B, que se pueden mover. Se dibujan la recta que los une y el triángulo de avance y elevación."));
function mvLee(a, b){
  var dx = b[0] - a[0], dy = b[1] - a[1], m = dx ? fr(dy, dx) : null;
  $("mv-lect").innerHTML = '<div class="linea">A ' + parHTML(a[0], a[1]) + " · B " + parHTML(b[0], b[1]) + "</div>" +
    '<div class="linea">' + T("Rise", "Elevación") + " · Δy = y₂ − y₁ = " + sg(b[1]) + " − " + (a[1] < 0 ? "(" + sg(a[1]) + ")" : a[1]) + " = <strong>" + sg(dy) + "</strong> · " +
    T("Run", "Avance") + " · Δx = x₂ − x₁ = " + sg(b[0]) + " − " + (a[0] < 0 ? "(" + sg(a[0]) + ")" : a[0]) + " = <strong>" + sg(dx) + "</strong></div>" +
    '<div class="linea veredicto">m = ' + (dx === 0 ? (dy === 0 ? "—" : T("undefined", "indefinida")) : (m.d === 1 ? sg(dy) + " ÷ " + (dx < 0 ? "(" + sg(dx) + ")" : sg(dx)) + " = " : (Math.abs(dy) !== Math.abs(m.n) || dx < 0 ? sg(dy) + "/" + (dx < 0 ? "(" + sg(dx) + ")" : sg(dx)) + " = " : "")) + (m.d === 1 ? sg(m.n) : fracHTML(m.n, m.d) + T(", which is ", ", equivale a ") + aprox(fval(m), 2).replace(/\.?0+$/, ""))) +
    (dx || dy ? " · " + T("slope ", "pendiente ") + (dx === 0 ? T("undefined", "indefinida") : tipoM(m)) : "") + "</div>" +
    '<div class="linea">' + frase(dy, dx) + "</div>";
}
MV.pinta();
$("mv-cambia").addEventListener("click", function(){ var p = MV.pts, x = p[0].x, y = p[0].y; p[0].x = p[1].x; p[0].y = p[1].y; p[1].x = x; p[1].y = y; MV.pinta();
  $("mv-nota").textContent = T("Both differences changed sign at the same time, so the slope did not change.", "Las dos diferencias cambiaron de signo a la vez, así que la pendiente no cambió."); });
$("mv-tramo").addEventListener("click", function(){
  var p = MV.pts, dx = p[1].x - p[0].x, dy = p[1].y - p[0].y; if (!dx && !dy) return;
  var g = mcd(Math.abs(dx), Math.abs(dy)) || 1, sx = dx / g, sy = dy / g, opciones = [];
  for (var k1 = -8; k1 <= 8; k1++) for (var k2 = -8; k2 <= 8; k2++){
    if (k1 === k2) continue;
    var a = [p[0].x + k1 * sx, p[0].y + k1 * sy], b = [p[0].x + k2 * sx, p[0].y + k2 * sy];
    if ([a[0], a[1], b[0], b[1]].every(function(v){ return v >= -8 && v <= 8; }) && !(k1 === 0 && k2 === g)) opciones.push([a, b]);
  }
  if (!opciones.length) return;
  var o = elige(opciones); p[0].x = o[0][0]; p[0].y = o[0][1]; p[1].x = o[1][0]; p[1].y = o[1][1]; MV.pinta();
  $("mv-nota").textContent = T("Another two points of the same line: the rise and the run changed, but the slope did not.", "Otros dos puntos de la misma recta: cambiaron la elevación y el avance, pero no la pendiente.");
});
var RETO = {m: null, bien: 0, total: 0};
function retoNuevo(){
  var l = [[3, 4], [1, 2], [2, 3], [-1, 2], [-3, 2], [2, 1], [-2, 1], [0, 1], [3, 1], [-1, 3], [4, 3], [-4, 5], [1, 1], [-1, 1], [5, 2]], q = elige(l);
  RETO.m = q[1] === 0 ? null : fr(q[0], q[1]); RETO.cero = q[0] === 0;
  $("rt-meta").innerHTML = "m = " + (RETO.cero ? "0" : fracHTML(RETO.m.n, RETO.m.d)); $("rt-fb").className = "fb"; $("rt-fb").innerHTML = "";
}
$("rt-comprobar").addEventListener("click", function(){
  var p = MV.pts, dx = p[1].x - p[0].x, dy = p[1].y - p[0].y, fb = $("rt-fb"); RETO.total++;
  if (!dx && !dy){ fb.className = "fb pista"; fb.innerHTML = T("A and B are the same point. Separate them.", "A y B son el mismo punto. Sepárelos."); return; }
  var ok = dx !== 0 && figual(fr(dy, dx), RETO.cero ? fr(0, 1) : RETO.m);
  if (ok){ RETO.bien++; fb.className = "fb bien"; fb.innerHTML = TX.bien + T("Rise ", "Elevación ") + sg(dy) + T(", run ", ", avance ") + sg(dx) + ": m = " + (RETO.cero ? "0" : fracHTML(RETO.m.n, RETO.m.d)) + "."; }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + T("Now the rise is ", "Ahora la elevación es ") + sg(dy) + T(" and the run is ", " y el avance es ") + sg(dx) + ". " +
    (RETO.cero ? T("For m = 0 the rise must be 0: put A and B at the same height.", "Para m = 0 la elevación debe ser 0: ponga A y B a la misma altura.") :
     T("Start at A, move " + RETO.m.d + " to the right, then " + Math.abs(RETO.m.n) + (RETO.m.n > 0 ? " up" : " down") + ", and put B there.", "Desde A, avance " + RETO.m.d + " a la derecha, después " + (RETO.m.n > 0 ? "suba " : "baje ") + Math.abs(RETO.m.n) + " y ponga B ahí.")); }
  $("rt-marcador").textContent = T("Challenges solved: ", "Retos resueltos: ") + RETO.bien + T(" in ", " en ") + RETO.total + T(" tries", " intentos");
});
$("rt-otro").addEventListener("click", retoNuevo); retoNuevo();

/* ===== MODULE 2 · From two points ===== */
function evaluaM(txt, m, a, b){
  var s = String(txt).trim().toLowerCase();
  var ind = /^(u|undef|undefined|indef|indefinida|no existe|none|n\/a)\.?$/.test(s);
  if (m === null){ if (ind) return {estado: "bien"}; if (leeFraccion(s) || leeDecimal(s) !== null) return {estado: "mal", msg: T("Look at the run: x₂ − x₁ = 0. You cannot divide by 0.", "Fíjese en el avance: x₂ − x₁ = 0. No se puede dividir entre 0.")}; return {estado: "invalido", msg: T("Type a number, a fraction like −3/4, or the word “undefined.”", "Escriba un número, una fracción como −3/4 o la palabra «indefinida».")}; }
  if (ind) return {estado: "mal", msg: T("The run is not 0 here, so the slope exists. Undefined is only for vertical lines.", "Aquí el avance no es 0, así que la pendiente existe. Indefinida es solo para rectas verticales.")};
  var mm = s.replace(/\s+/g, "").replace(/[−–]/g, "-").match(/^(-?\d+)\/(-?\d+)$/), f = mm && +mm[2] !== 0 ? {p: +mm[1], q: +mm[2]} : leeFraccion(s), d = leeDecimal(s), v = f ? fr(f.p, f.q) : null;
  if (!f && d === null) return {estado: "invalido", msg: T("Type a whole number, a fraction like −3/4, or a decimal.", "Escriba un número entero, una fracción como −3/4 o un decimal.")};
  var ok = v ? figual(v, m) : Math.abs(d - fval(m)) < 0.005;
  if (ok) return {estado: "bien"};
  var dy = b[1] - a[1], dx = b[0] - a[0];
  var val = v ? fval(v) : d;
  if (dy !== 0 && Math.abs(val - dx / dy) < 0.005) return {estado: "mal", msg: T("You divided the run by the rise. The rise (Δy) goes on top.", "Dividió el avance entre la elevación. La elevación (Δy) va arriba.")};
  if (Math.abs(val + fval(m)) < 0.005) return {estado: "mal", msg: T("The size is right, but the sign is not. Subtract in the same order on top and on the bottom.", "El valor está bien, pero el signo no. Reste en el mismo orden arriba y abajo.")};
  return {estado: "mal", msg: T("Find the rise y₂ − y₁ and the run x₂ − x₁ first (watch the negative signs), then divide.", "Calcule primero la elevación y₂ − y₁ y el avance x₂ − x₁ (cuidado con los signos negativos) y después divida.")};
}
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
creaPracticaLibre("dp", function(){
  var a, b, r = Math.random();
  do { a = [aleatorio(-8, 8), aleatorio(-8, 8)]; b = [aleatorio(-8, 8), aleatorio(-8, 8)]; if (r < 0.1) b[0] = a[0]; else if (r < 0.2) b[1] = a[1]; } while ((a[0] === b[0] && a[1] === b[1]) || (r >= 0.2 && (a[0] === b[0] || a[1] === b[1])));
  var dy = b[1] - a[1], dx = b[0] - a[0], m = dx ? fr(dy, dx) : null;
  var P = Plano({xmin: -9, xmax: 9, ymin: -9, ymax: 9, u: 22, paso: 3});
  $("dp-svg").innerHTML = P.svg(rectaPor(P, a, b, "#90a4ae", 2.5) + P.punto(a, C4.azul, "A") + P.punto(b, C4.morado, "B"), T("The line through A", "La recta que pasa por A") + par(a[0], a[1]) + T(" and B", " y B") + par(b[0], b[1]) + ".", 380);
  return {enun: T("Find the slope of the line through ", "Calcule la pendiente de la recta que pasa por ") + parHTML(a[0], a[1], "A") + T(" and ", " y ") + parHTML(b[0], b[1], "B") + ".",
    evalua: function(txt){ return evaluaM(txt, m, a, b); },
    solucion: "m = (" + sg(b[1]) + " − " + pn(a[1]) + ") ÷ (" + sg(b[0]) + " − " + pn(a[0]) + ") = " + sg(dy) + " ÷ " + (dx < 0 ? "(" + sg(dx) + ")" : sg(dx)) + " = " + (m === null ? T("undefined (the run is 0)", "indefinida (el avance es 0)") : fracHTML(m.n, m.d)) + "."};
});

/* ===== MODULE 3 · The four types ===== */
function tpPinta(){
  var dy = +$("tp-dy").value, dx = +$("tp-dx").value, a = [-3, 0], b = [-3 + dx, dy], tipo = dx === 0 ? (dy === 0 ? "" : "ind") : (dy === 0 ? "cero" : (dy * dx > 0 ? "pos" : "neg"));
  $("tp-dyv").textContent = sg(dy); $("tp-dxv").textContent = dx;
  var P = Plano({xmin: -8, xmax: 8, ymin: -7, ymax: 7, u: 26, paso: 2});
  $("tp-svg").innerHTML = P.svg((dx || dy ? rectaPor(P, a, b, C4.azul, 3) + trianguloPendiente(P, a, b) : "") + P.punto(a, C4.tinta, "(−3, 0)", "nw"), T("A line that starts at (−3, 0) with a rise of ", "Una recta que parte de (−3, 0) con elevación ") + dy + T(" and a run of ", " y avance ") + dx + ".", 460);
  ["pos", "neg", "cero", "ind"].forEach(function(k){ var f = $("tp-f-" + k); if (f) f.className = k === tipo ? "fila-activa" : ""; $("tp-b-" + k).setAttribute("aria-pressed", k === tipo ? "true" : "false"); });
  $("tp-lect").innerHTML = '<div class="linea veredicto">' + (dx === 0 ? (dy === 0 ? T("Rise and run are both 0: there is no line.", "La elevación y el avance son 0: no hay recta.") : "m = " + dy + " ÷ 0 → " + T("undefined", "indefinida")) :
    "m = " + sg(dy) + " ÷ " + dx + " = " + mHTML(fr(dy, dx)) + " · |m| = " + aprox(Math.abs(dy / dx), 2).replace(/\.?0+$/, "")) + "</div>";
}
["tp-dy", "tp-dx"].forEach(function(i){ $(i).addEventListener("input", tpPinta); });
[["pos", 3, 2], ["neg", -3, 2], ["cero", 0, 3], ["ind", 4, 0]].forEach(function(q){ $("tp-b-" + q[0]).addEventListener("click", function(){ $("tp-dy").value = q[1]; $("tp-dx").value = q[2]; tpPinta(); }); });
tpPinta();
OMR("tc", function(){
  var r = Math.random(), U = T("Undefined", "Indefinida");
  if (r < 0.3){
    var dx = elige([0, 1, 2, 3, 4]), dy = elige([-4, -3, -2, -1, 0, 1, 2, 3, 4]); if (!dx && !dy) dy = 3;
    var a = [aleatorio(-5, 0), aleatorio(-3, 3)], b = [a[0] + dx, a[1] + dy], m = dx ? fr(dy, dx) : null, P = Plano({xmin: -7, xmax: 7, ymin: -7, ymax: 7, u: 18, paso: 7, sinNumeros: true});
    var k = m === null ? "ind" : (m.n === 0 ? "cero" : (m.n > 0 ? "pos" : "neg"));
    return {enun: T("What type of slope does this line have?", "¿Qué tipo de pendiente tiene esta recta?") + P.svg(rectaPor(P, a, b, C4.azul, 3.5), T("A line on the plane.", "Una recta en el plano.") + " " + (k === "ind" ? T("It is vertical.", "Es vertical.") : k === "cero" ? T("It is horizontal.", "Es horizontal.") : k === "pos" ? T("It goes up from left to right.", "Sube de izquierda a derecha.") : T("It goes down from left to right.", "Baja de izquierda a derecha.")), 260),
      correcta: k, enOrden: true, opciones: [{clave: "pos", html: T("Positive", "Positiva")}, {clave: "neg", html: T("Negative", "Negativa")}, {clave: "cero", html: T("Zero", "Cero")}, {clave: "ind", html: U}],
      porClave: {cero: T("Zero is a flat, horizontal line.", "Cero es una recta plana, horizontal."), ind: T("Undefined is a vertical line.", "Indefinida es una recta vertical.")},
      pista: T("Read the line from left to right: does it go up, go down, stay flat, or stand straight up?", "Lea la recta de izquierda a derecha: ¿sube, baja, se queda plana o está de pie?"), bien: T("It is ", "Es ") + (k === "ind" ? U.toLowerCase() : tipoM(m)) + "."};
  }
  if (r < 0.6){
    var x1 = aleatorio(-6, 6), y1 = aleatorio(-6, 6), s = elige(["pos", "neg", "cero", "ind"]), x2 = s === "ind" ? x1 : x1 + aleatorio(1, 5), y2 = s === "cero" ? y1 : (s === "pos" ? y1 + aleatorio(1, 6) : (s === "neg" ? y1 - aleatorio(1, 6) : y1 + aleatorio(1, 6)));
    return {enun: T("What type of slope does the line through ", "¿Qué tipo de pendiente tiene la recta que pasa por ") + parHTML(x1, y1) + T(" and ", " y ") + parHTML(x2, y2) + T(" have?", "?"), correcta: s, enOrden: true,
      opciones: [{clave: "pos", html: T("Positive", "Positiva")}, {clave: "neg", html: T("Negative", "Negativa")}, {clave: "cero", html: T("Zero", "Cero")}, {clave: "ind", html: U}],
      porClave: {cero: T("Zero needs the same y in both points.", "Cero pide la misma y en los dos puntos."), ind: T("Undefined needs the same x in both points.", "Indefinida pide la misma x en los dos puntos.")},
      pista: T("Find the rise (y₂ − y₁) and the run (x₂ − x₁) and look at their signs.", "Calcule la elevación (y₂ − y₁) y el avance (x₂ − x₁) y fíjese en sus signos."),
      bien: T("Rise ", "Elevación ") + sg(y2 - y1) + T(", run ", ", avance ") + sg(x2 - x1) + "."};
  }
  var l = baraja([fr(1, 2), fr(2, 3), fr(3, 1), fr(-5, 1), fr(-1, 4), fr(4, 1), fr(-3, 2), fr(5, 2), fr(-6, 1), fr(1, 1)]).slice(0, 4), max = l.reduce(function(a, b){ return Math.abs(fval(b)) > Math.abs(fval(a)) ? b : a; });
  return {enun: T("Which slope belongs to the steepest line?", "¿Qué pendiente corresponde a la recta más empinada?"), correcta: fTxt(max),
    opciones: l.map(function(m){ return {clave: fTxt(m), html: "m = " + fracHTML(m.n, m.d)}; }),
    pista: T("Compare the absolute values (ignore the sign): the biggest one is the steepest.", "Compare los valores absolutos (sin el signo): el mayor es el más empinado."), bien: "|" + fTxt(max) + "| " + T("is the largest absolute value.", "es el mayor valor absoluto.")};
});

/* ===== MODULE 4 · Rate of change ===== */
var SIT = [
  {id: "auto", x: T("Time (hours)", "Tiempo (horas)"), y: T("Distance (miles)", "Distancia (millas)"), ux: T("hour", "hora"), uy: T("miles", "millas"), filas: [[0, 0], [1, 55], [2, 110], [3, 165], [4, 220], [5, 275]], que: T("the speed of the car", "la velocidad del auto")},
  {id: "paga", x: T("Hours worked", "Horas trabajadas"), y: T("Pay (dollars)", "Salario (dólares)"), ux: T("hour", "hora"), uy: T("dollars", "dólares"), filas: [[0, 0], [4, 66], [8, 132], [12, 198], [16, 264], [20, 330]], que: T("the pay per hour", "la paga por hora")},
  {id: "gas", x: T("Gas (gallons)", "Gasolina (galones)"), y: T("Cost (dollars)", "Costo (dólares)"), ux: T("gallon", "galón"), uy: T("dollars", "dólares"), filas: [[0, 0], [2, 7], [4, 14], [6, 21], [8, 28], [10, 35]], que: T("the price per gallon", "el precio por galón")},
  {id: "tanque", x: T("Time (minutes)", "Tiempo (minutos)"), y: T("Water in the tank (gallons)", "Agua en el tanque (galones)"), ux: T("minute", "minuto"), uy: T("gallons", "galones"), filas: [[0, 120], [2, 96], [4, 72], [6, 48], [8, 24], [10, 0]], que: T("how fast the tank empties", "qué tan rápido se vacía el tanque")}];
function tsLlena(){
  var s = SIT[$("ts-sit").selectedIndex];
  ["ts-f1", "ts-f2"].forEach(function(id, k){ var sel = $(id), v = sel.selectedIndex; sel.innerHTML = s.filas.map(function(f, i){ return '<option value="' + i + '">' + f[0] + " → " + f[1] + "</option>"; }).join(""); sel.selectedIndex = v >= 0 && v < s.filas.length ? v : (k ? 3 : 1); });
  tsPinta();
}
function tsPinta(){
  var s = SIT[$("ts-sit").selectedIndex], i = +$("ts-f1").value, j = +$("ts-f2").value, a = s.filas[i], b = s.filas[j];
  $("ts-tabla").innerHTML = '<caption class="sr-only">' + s.y + T(" for each value of ", " para cada valor de ") + s.x + "</caption><thead><tr><th scope=\"col\">" + s.x + "</th><th scope=\"col\">" + s.y + "</th></tr></thead><tbody>" +
    s.filas.map(function(f, k){ return '<tr class="' + (k === i || k === j ? "fila-activa" : "") + '"><td>' + f[0] + "</td><td>" + f[1] + "</td></tr>"; }).join("") + "</tbody>";
  var xs = s.filas.map(function(f){ return f[0]; }), ys = s.filas.map(function(f){ return f[1]; }), xM = Math.max.apply(null, xs), yM = Math.max.apply(null, ys);
  var W = 520, H = 300, x0 = 60, y0 = 250, X = function(v){ return x0 + v / xM * 420; }, Y = function(v){ return y0 - v / yM * 210; }, g = "";
  for (var k = 0; k <= 5; k++){ var yv = yM * k / 5, xv = xM * k / 5; g += '<line x1="' + x0 + '" y1="' + f1(Y(yv)) + '" x2="' + (x0 + 420) + '" y2="' + f1(Y(yv)) + '" stroke="#eceff1"/><text x="' + (x0 - 6) + '" y="' + f1(Y(yv) + 4) + '" font-size="12" text-anchor="end" fill="#455a64">' + Math.round(yv) + '</text><text x="' + f1(X(xv)) + '" y="' + (y0 + 18) + '" font-size="12" text-anchor="middle" fill="#455a64">' + Math.round(xv * 10) / 10 + "</text>"; }
  g += '<line x1="' + x0 + '" y1="' + y0 + '" x2="' + (x0 + 430) + '" y2="' + y0 + '" stroke="#10174f" stroke-width="2"/><line x1="' + x0 + '" y1="' + y0 + '" x2="' + x0 + '" y2="30" stroke="#10174f" stroke-width="2"/>';
  g += '<text x="' + (x0 + 210) + '" y="' + (y0 + 40) + '" font-size="13" font-weight="700" text-anchor="middle" fill="#10174f">' + s.x + '</text><text x="16" y="' + (y0 - 105) + '" font-size="13" font-weight="700" text-anchor="middle" fill="#10174f" transform="rotate(-90 16 ' + (y0 - 105) + ')">' + s.y + "</text>";
  g += '<polyline points="' + s.filas.map(function(f){ return f1(X(f[0])) + "," + f1(Y(f[1])); }).join(" ") + '" fill="none" stroke="' + C4.azul + '" stroke-width="3"/>';
  if (i !== j){ var p = [X(a[0]), Y(a[1])], q = [X(b[0]), Y(b[1])]; g += '<line x1="' + f1(p[0]) + '" y1="' + f1(p[1]) + '" x2="' + f1(q[0]) + '" y2="' + f1(p[1]) + '" stroke="#1565c0" stroke-width="2.5" stroke-dasharray="6 4"/><line x1="' + f1(q[0]) + '" y1="' + f1(p[1]) + '" x2="' + f1(q[0]) + '" y2="' + f1(q[1]) + '" stroke="#c62828" stroke-width="2.5" stroke-dasharray="6 4"/>'; }
  [a, b].forEach(function(f){ g += '<circle cx="' + f1(X(f[0])) + '" cy="' + f1(Y(f[1])) + '" r="7" fill="' + C4.morado + '" stroke="#fff" stroke-width="2"/>'; });
  $("ts-svg").innerHTML = '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("Graph of ", "Gráfica de ") + s.y + T(" against ", " en función de ") + s.x + T(": a straight line. The two chosen rows are marked.", ": una recta. Las dos filas elegidas están marcadas.") + '" style="max-width:520px">' + g + "</svg>";
  if (i === j){ $("ts-res").innerHTML = '<div class="linea">' + T("Choose two different rows.", "Elija dos filas distintas.") + "</div>"; return; }
  var dy = b[1] - a[1], dx = b[0] - a[0], m = fr(dy, dx), v = fval(m);
  $("ts-res").innerHTML = '<div class="linea">' + T("Rate = ", "Tasa = ") + "(" + b[1] + " − " + a[1] + ") ÷ (" + b[0] + " − " + a[0] + ") = " + sg(dy) + " ÷ " + sg(dx) + " = <strong>" + sg(Math.round(v * 100) / 100) + " " + s.uy + T(" per ", " por ") + s.ux + "</strong></div>" +
    '<div class="linea">' + T("That is ", "Es ") + s.que + (v < 0 ? T(": it goes down ", ": baja ") + Math.abs(Math.round(v * 100) / 100) + " " + s.uy + T(" every ", " cada ") + s.ux + "." : ".") + "</div>";
}
$("ts-sit").addEventListener("change", tsLlena); $("ts-f1").addEventListener("change", tsPinta); $("ts-f2").addEventListener("change", tsPinta); tsLlena();
OMR("tr", function(){
  var c = elige([
    function(){ var r = elige([45, 50, 55, 60, 65]), h = aleatorio(2, 5); return {en: T("A car's distance against time is a straight line. After 1 hour it has gone " + r + " miles; after " + (h + 1) + " hours, " + r * (h + 1) + " miles. What is the rate of change?", "La distancia de un auto en función del tiempo es una recta. A la hora ha recorrido " + r + " millas; a las " + (h + 1) + " horas, " + r * (h + 1) + " millas. ¿Cuál es la tasa de cambio?"),
      ok: r + T(" miles per hour", " millas por hora"), mal: [r * (h + 1) + T(" miles per hour", " millas por hora"), T("1/" + r + " hour per mile", "1/" + r + " hora por milla"), r * h + T(" miles", " millas")]}; },
    function(){ var p = elige([14, 15, 16, 17, 18]), h = elige([20, 30, 40]); return {en: T("Pay against hours worked is a straight line: 0 hours pays $0 and " + h + " hours pay $" + p * h + ". What does the slope mean?", "El salario en función de las horas trabajadas es una recta: 0 horas pagan $0 y " + h + " horas pagan $" + p * h + ". ¿Qué significa la pendiente?"),
      ok: T("$" + p + " for each hour worked", "$" + p + " por cada hora trabajada"), mal: [T("$" + p * h + " for each hour worked", "$" + p * h + " por cada hora trabajada"), T(h + " hours per dollar", h + " horas por dólar"), T("The pay for the whole week", "El salario de toda la semana")]}; },
    function(){ var g = elige([8, 10, 12, 15]), t0 = elige([120, 150, 180]); return {en: T("A tank has " + t0 + " gallons and drains at a steady rate. After 4 minutes it has " + (t0 - 4 * g) + " gallons. What is the rate of change?", "Un tanque tiene " + t0 + " galones y se vacía a ritmo constante. A los 4 minutos tiene " + (t0 - 4 * g) + " galones. ¿Cuál es la tasa de cambio?"),
      ok: T("−" + g + " gallons per minute (it loses " + g + " each minute)", "−" + g + " galones por minuto (pierde " + g + " cada minuto)"), mal: [T(g + " gallons per minute (it gains " + g + " each minute)", g + " galones por minuto (gana " + g + " cada minuto)"), T("−" + 4 * g + " gallons per minute", "−" + 4 * g + " galones por minuto"), T("−1/" + g + " minute per gallon", "−1/" + g + " minuto por galón")]}; },
    function(){ var k = elige([0.12, 0.14, 0.15, 0.18]); return {en: T("The graph of an electric bill against kilowatt-hours used is a line with slope " + k + ". What does the slope mean?", "La gráfica de la factura de la luz en función de los kilovatios-hora consumidos es una recta de pendiente " + k + ". ¿Qué significa la pendiente?"),
      ok: T("Each extra kWh costs $" + k.toFixed(2), "Cada kWh adicional cuesta $" + k.toFixed(2)), mal: [T("The fixed monthly charge", "El cargo fijo del mes"), T("The whole bill is $" + k.toFixed(2), "El total de la factura es $" + k.toFixed(2)), T("Each extra dollar buys " + k + " kWh", "Cada dólar adicional compra " + k + " kWh")]}; }])();
  var ops = [{clave: "ok", html: c.ok}].concat(c.mal.map(function(m, i){ return {clave: "m" + i, html: m}; }));
  return {enun: c.en, correcta: "ok", opciones: ops, pista: T("The slope is a rate: (change in y) ÷ (change in x), with units “y per x.” Check the sign too.", "La pendiente es una tasa: (cambio en y) ÷ (cambio en x), con unidades «y por x». Revise también el signo."), bien: c.ok + "."};
});
'''

def practica_pagina():
    n = N
    mods = [
     (t("slope", "pendiente"), t("The slope in motion", "La pendiente en movimiento"),
      f'''      <p>{t("Drag point A or point B with the mouse or your finger, or tap any grid crossing to move the last point you used. With the keyboard, press Tab to reach a point and move it with the arrows. The triangle shows the run (Δx, across) and the rise (Δy, up or down) between the two points.", "Arrastre el punto A o el punto B con el ratón o con el dedo, o toque cualquier cruce de la cuadrícula para llevar allí el último punto que movió. Con el teclado, pulse Tab hasta llegar a un punto y muévalo con las flechas. El triángulo muestra el avance (Δx, en horizontal) y la elevación (Δy, en vertical) entre los dos puntos.")}</p>
      <div id="mv-plano"></div>
      <div class="salida" id="mv-lect" aria-live="polite"></div>
      <div class="fila-btn"><button type="button" class="btn-sec" id="mv-cambia">{t("Swap the two points", "Intercambiar los dos puntos")}</button><button type="button" class="btn-sec" id="mv-tramo">{t("Another stretch of the same line", "Ver otro tramo de la misma recta")}</button></div>
      <p class="nota" id="mv-nota" aria-live="polite"></p>
      <h3>{t("Challenge: build the line", "Reto: construya la recta")}</h3>
      <div class="practica"><p class="enun">{t("Place A and B so that the line has this slope:", "Coloque A y B de modo que la recta tenga esta pendiente:")} <strong id="rt-meta" style="font-size:20px"></strong></p>
        <div class="fila-btn"><button type="button" class="btn" id="rt-comprobar">{t("Check", "Comprobar")}</button><button type="button" class="btn-sec" id="rt-otro">{t("Another challenge", "Otro reto")}</button></div>
        <div class="fb" id="rt-fb" role="status"></div><p class="marcador" id="rt-marcador"></p></div>
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("How the position of the points changes the slope", "Relación entre la posición de los puntos y la pendiente")}</caption>
        <thead><tr><th scope="col">{t("If you move the points like this…", "Si mueve los puntos así…")}</th><th scope="col">{t("…the slope does this", "…la pendiente hace esto")}</th></tr></thead><tbody>
        <tr><td>{t("B higher than A, to the right", "B más arriba que A, a la derecha")}</td><td>{t("m is positive: the line goes up.", "m es positiva: la recta sube.")}</td></tr>
        <tr><td>{t("B lower than A, to the right", "B más abajo que A, a la derecha")}</td><td>{t("m is negative: the line goes down.", "m es negativa: la recta baja.")}</td></tr>
        <tr><td>{t("A and B at the same height", "A y B a la misma altura")}</td><td>{t("Δy = 0, so m = 0: the line is horizontal.", "Δy = 0, así que m = 0: la recta es horizontal.")}</td></tr>
        <tr><td>{t("A and B in the same column", "A y B en la misma columna")}</td><td>{t("Δx = 0, and you cannot divide by 0: the slope is undefined.", "Δx = 0 y no se puede dividir entre 0: la pendiente es indefinida.")}</td></tr>
        <tr><td>{t("The points move apart without changing the tilt", "Los puntos se separan sin cambiar la inclinación")}</td><td>{t("The slope does not change: it is the same all along the line.", "La pendiente no cambia: es constante en toda la recta.")}</td></tr></tbody></table></div>'''),
     (t("two-points", "dos-puntos"), t("The slope from two points", "La pendiente a partir de dos puntos"),
      f'''{n4.formula("m = (y₂ − y₁) ÷ (x₂ − x₁)")}
      <p>{t("The top is the rise (Δy); the bottom is the run (Δx). Subtract in the same order on top and on the bottom: the point you subtract first in one place is the point you subtract first in the other.", "El numerador es la elevación (Δy) y el denominador, el avance (Δx). Reste en el mismo orden arriba y abajo: el punto que se resta primero en un lugar es el que se resta primero en el otro.")}</p>
{B.libre("dp", t("Practice: find the slope", "Practique: calcule la pendiente"), t("Slope m", "Pendiente m"), nota=False).replace('<div class="enun" id="dp-enun"></div>', '<div class="enun" id="dp-enun"></div><div id="dp-svg"></div>').replace('<div class="fila-btn">', '<p class="nota">' + t("Type a whole number or a fraction like −3/4. If the run is 0, type “undefined.”", "Escriba un número entero o una fracción como −3/4. Si el avance es 0, escriba «indefinida».") + '</p>\n        <div class="fila-btn">', 1)}'''),
     (t("types", "tipos"), t("The four types of slope", "Los cuatro tipos de pendiente"),
      f'''      <p>{t("The line starts at (−3, 0). Change the rise and the run, or choose a type directly. Read lines from left to right.", "La recta parte del punto (−3, 0). Cambie la elevación y el avance, o elija directamente un tipo. Las rectas se leen de izquierda a derecha.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo" style="flex:1;min-width:200px;"><label for="tp-dy">{t("Rise", "Elevación")} Δy = <span id="tp-dyv"></span></label><input type="range" id="tp-dy" min="-6" max="6" step="1" value="3"></div>
        <div class="campo" style="flex:1;min-width:200px;"><label for="tp-dx">{t("Run", "Avance")} Δx = <span id="tp-dxv"></span></label><input type="range" id="tp-dx" min="0" max="6" step="1" value="2"></div></div>
        <div class="modos" role="group" aria-label="{t("Choose a type", "Elegir un tipo")}"><button type="button" class="btn-sec" id="tp-b-pos">{t("Positive", "Positiva")}</button><button type="button" class="btn-sec" id="tp-b-neg">{t("Negative", "Negativa")}</button><button type="button" class="btn-sec" id="tp-b-cero">{t("Zero", "Cero")}</button><button type="button" class="btn-sec" id="tp-b-ind">{t("Undefined", "Indefinida")}</button></div></div>
      <div id="tp-svg"></div>
{n4.salida("tp-lect")}
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("The four types of slope; the row of the current type is highlighted", "Los cuatro tipos de pendiente; la fila del tipo actual aparece resaltada")}</caption>
        <thead><tr><th scope="col">{t("Type", "Tipo")}</th><th scope="col">{t("What does the line look like?", "¿Cómo se ve la recta?")}</th><th scope="col">{t("Value of m", "Valor de m")}</th></tr></thead><tbody>
        <tr id="tp-f-pos"><td>{t("Positive", "Positiva")}</td><td>{t("It goes up from left to right.", "Sube de izquierda a derecha.")}</td><td>m &gt; 0</td></tr>
        <tr id="tp-f-neg"><td>{t("Negative", "Negativa")}</td><td>{t("It goes down from left to right.", "Baja de izquierda a derecha.")}</td><td>m &lt; 0</td></tr>
        <tr id="tp-f-cero"><td>{t("Zero", "Cero")}</td><td>{t("Horizontal (flat).", "Horizontal (plana).")}</td><td>m = 0</td></tr>
        <tr id="tp-f-ind"><td>{t("Undefined", "Indefinida")}</td><td>{t("Vertical.", "Vertical.")}</td><td>{t("m does not exist (run = 0)", "m no existe (avance = 0)")}</td></tr></tbody></table></div>
      <div class="caja-tip">{t("Which is steeper? The one with the larger absolute value of the slope, |m|. A line with m = −5 is steeper than one with m = 3, even though one goes down and the other goes up.", "¿Cuál es más empinada? La que tiene el mayor valor absoluto de la pendiente, |m|. Una recta con m = −5 es más empinada que una con m = 3, aunque una baje y la otra suba.")}</div>
{B.om("tc", t("Practice: classify the slope", "Practique: clasifique la pendiente"))}'''),
     (t("rate", "tasa"), t("The slope as a rate of change", "La pendiente como tasa de cambio"),
      f'''      <p>{t("Outside the plane, the slope is a rate of change: how much one quantity changes for each unit of the other, in “units of y per unit of x.” Choose a situation and any two rows of the table: because the graph is a straight line, the rate always comes out the same.", "Fuera del plano, la pendiente es una tasa de cambio: cuánto cambia una cantidad por cada unidad de la otra, en «unidades de y por cada unidad de x». Elija una situación y dos filas cualesquiera de la tabla: como la gráfica es una recta, la tasa sale siempre igual.")}</p>
      <div class="panel"><div class="campos">{n4.lista("ts-sit", t("Situation", "Situación"), [("auto", t("A car on the highway", "Un auto en la carretera")), ("paga", t("Pay for hours worked", "El salario por horas")), ("gas", t("Filling up with gas", "Cargar gasolina")), ("tanque", t("A tank that drains", "Un tanque que se vacía"))])}
        <div class="campo"><label for="ts-f1">{t("First row", "Primera fila")}</label><select id="ts-f1"></select></div><div class="campo"><label for="ts-f2">{t("Second row", "Segunda fila")}</label><select id="ts-f2"></select></div></div></div>
      <div class="tabla-scroll"><table class="tabla-lados" id="ts-tabla"></table></div>
      <div id="ts-svg"></div>
{n4.salida("ts-res")}
      <div class="caja-tip">{t("The sign has a meaning too. A positive rate means the quantity grows; a negative one, that it shrinks. A tank that drains at −12 gallons per minute loses 12 gallons every minute: say it in words, not only with the sign.", "El signo también se interpreta. Una tasa positiva indica que la cantidad aumenta; una negativa, que disminuye. Un tanque que se vacía a −12 galones por minuto pierde 12 galones cada minuto: conviene decirlo con palabras, no solo con el signo.")}</div>
{B.om("tr", t("Practice: find and read the rate", "Practique: calcule e interprete la tasa"))}''')]
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO + "\n  tr.fila-activa td{background:#fff8e1;font-weight:700;}", scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "La pendiente: concepto, fórmula e interpretación")
