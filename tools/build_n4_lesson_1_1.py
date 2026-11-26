"""Level 4 · Lesson 1.1 · The coordinate plane: ordered pairs, distance, and midpoint — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_1-1.html; the interactives interactivos/plano_cartesiano, interactivos/distancia
(with its Illinois map), interactivos/punto_medio, and algebra/n4-l1-1.html (perimeter). All of them are rebuilt here, inside LearnGED.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n4
from n4 import Plano, AZUL, ROJO, VERDE, CATETO, MORADO

B.NIVEL = 4
N = "1-1"
TEMA = ("Analytic geometry", "Geometría analítica")
TIT = ("The coordinate plane: ordered pairs, distance, and midpoint", "El plano cartesiano: pares ordenados, distancia y punto medio")
SCRIPTS = n4.SCRIPTS

def fig_cuadrantes():
    p = Plano(-6, 6, -6, 6, 30, cuadrantes=True, paso=2)
    for (x, y), nom, c, lado in (((3, 2), "A(3, 2)", AZUL, "ne"), ((-4, 3), "B(−4, 3)", ROJO, "nw"), ((-2, -3), "C(−2, −3)", VERDE, "sw"), ((4, -2), "D(4, −2)", MORADO, "se")):
        p.punto((x, y), c, nom, lado)
    return p.svg(t("Coordinate plane with the four quadrants numbered I to IV, counterclockwise from the upper right. A(3, 2) is in Quadrant I, B(−4, 3) in Quadrant II, C(−2, −3) in Quadrant III, and D(4, −2) in Quadrant IV.",
                   "Plano cartesiano con los cuatro cuadrantes numerados del I al IV, en sentido contrario a las manecillas del reloj desde la parte superior derecha. A(3, 2) está en el cuadrante I, B(−4, 3) en el II, C(−2, −3) en el III y D(4, −2) en el IV."), 420)

def fig_distancia():
    p = Plano(-2, 6, -1, 7, 36)
    p.poli([(1, 2), (4, 2), (4, 6)], "rgba(26,35,126,.07)", "none", 0).seg((1, 2), (4, 2), CATETO, 2.5, "7 5").seg((4, 2), (4, 6), CATETO, 2.5, "7 5").seg((1, 2), (4, 6), AZUL, 3.5)
    p.texto((2.5, 2), "Δx = 3", CATETO, 14, dy=16).texto((4, 4), "Δy = 4", CATETO, 14, "start", dx=10).texto((2.1, 4.6), "d = 5", AZUL, 15, "end")
    p.punto((1, 2), AZUL, "P(1, 2)", "nw").punto((4, 6), AZUL, "Q(4, 6)", "ne")
    return p.svg(t("P(1, 2) and Q(4, 6) joined by a segment. A horizontal leg of 3 and a vertical leg of 4 form a right triangle; the segment PQ, the hypotenuse, measures 5.",
                   "P(1, 2) y Q(4, 6) unidos por un segmento. Un cateto horizontal de 3 y uno vertical de 4 forman un triángulo rectángulo; el segmento PQ, la hipotenusa, mide 5."), 360)

def fig_medio():
    p = Plano(-1, 8, -1, 6, 36)
    p.seg((1, 1), (7, 5), AZUL, 3.5).punto((1, 1), AZUL, "A(1, 1)", "nw").punto((7, 5), AZUL, "B(7, 5)", "nw").punto((4, 3), ROJO, "M(4, 3)", "se")
    return p.svg(t("Segment from A(1, 1) to B(7, 5). Its midpoint M(4, 3) is exactly halfway between them.",
                   "Segmento de A(1, 1) a B(7, 5). Su punto medio M(4, 3) está exactamente a mitad de camino."), 380)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Level 3.</strong> In Level 3 you used the Pythagorean theorem (a² + b² = c²) to find a missing side of a right triangle. Level 4 opens by taking that same theorem to a new place: the coordinate plane. The distance formula is not a new formula to memorize; it is the Pythagorean theorem written with coordinates. On this base you will build, in the next lessons, everything about lines and functions.",
 "<strong>Conexión con el nivel anterior.</strong> En el Nivel 3 se usó el teorema de Pitágoras (a² + b² = c²) para hallar el lado que falta de un triángulo rectángulo. El Nivel 4 empieza llevando ese mismo teorema a un lugar nuevo: el plano cartesiano. La fórmula de la distancia no es una fórmula nueva que memorizar: es el teorema de Pitágoras escrito con coordenadas. Sobre esta base se construirá, en las próximas lecciones, todo el estudio de la recta y de las funciones.")}</p>
<p>{t("The <strong>coordinate plane</strong> is made of two perpendicular number lines: the <strong>x-axis</strong> (horizontal) and the <strong>y-axis</strong> (vertical). They cross at the <strong>origin</strong>, (0, 0). Each point is located with an <strong>ordered pair</strong> (x, y): first count across (x), then up or down (y).",
 "El <strong>plano cartesiano</strong> está formado por dos rectas numéricas perpendiculares: el <strong>eje x</strong> (horizontal) y el <strong>eje y</strong> (vertical). Se cruzan en el <strong>origen</strong>, (0, 0). Cada punto se localiza con un <strong>par ordenado</strong> (x, y): primero se cuenta horizontalmente (x) y después hacia arriba o hacia abajo (y).")}</p>
<p>{t("The axes split the plane into four <strong>quadrants</strong>, numbered with Roman numerals counterclockwise, starting at the upper right.", "Los ejes dividen el plano en cuatro <strong>cuadrantes</strong>, numerados con números romanos en sentido contrario a las manecillas del reloj, a partir de la esquina superior derecha.")}</p>
{fig_cuadrantes()}
{tabla(t("Sign of the coordinates in each quadrant", "Signo de las coordenadas en cada cuadrante"), t("Sign of x and of y in each quadrant, with an example", "Signo de x y de y en cada cuadrante, con un ejemplo"),
  [t("Quadrant", "Cuadrante"), t("Sign of x", "Signo de x"), t("Sign of y", "Signo de y"), t("Example", "Ejemplo")],
  [["I", t("positive (+)", "positivo (+)"), t("positive (+)", "positivo (+)"), "(3, 2)"], ["II", t("negative (−)", "negativo (−)"), t("positive (+)", "positivo (+)"), "(−4, 3)"],
   ["III", t("negative (−)", "negativo (−)"), t("negative (−)", "negativo (−)"), "(−2, −3)"], ["IV", t("positive (+)", "positivo (+)"), t("negative (−)", "negativo (−)"), "(4, −2)"]])}
{caja("ojo", t("The order matters", "El orden importa"), t("<p>The pair (3, 2) is not the same point as (2, 3). In (x, y), the first coordinate always tells the move across and the second, the move up or down. A point on the x-axis has the form (x, 0); a point on the y-axis has the form (0, y).</p>", "<p>El par (3, 2) no es el mismo punto que (2, 3). En (x, y), la primera coordenada siempre indica el desplazamiento horizontal y la segunda, el vertical. Un punto sobre el eje x tiene la forma (x, 0); uno sobre el eje y, la forma (0, y).</p>"))}
{practica("p1", t("Practice 1 — Where is the point?", "Práctica 1 — ¿Dónde está el punto?"), t("Where is the point (−5, −1)?", "¿Dónde está el punto (−5, −1)?"), [("a", t("Quadrant II", "Cuadrante II")), ("b", t("Quadrant III", "Cuadrante III")), ("c", t("Quadrant IV", "Cuadrante IV"))])}
{enlace(n, t("plane", "plano"), t("ordered pairs and quadrants", "los pares ordenados y los cuadrantes"), t("Place points in the four quadrants and read their coordinates until you can do it without stopping to think.", "Ubique puntos en los cuatro cuadrantes y lea sus coordenadas hasta hacerlo sin dudar."))}'''

    s2 = f'''<p>{t("To find the distance between two points, a right triangle appears naturally: the horizontal difference of the coordinates (Δx, “delta x”) is one leg, the vertical difference (Δy) is the other, and the distance you want is the hypotenuse. By the Pythagorean theorem:",
 "Para hallar la distancia entre dos puntos se forma, de manera natural, un triángulo rectángulo: la diferencia horizontal de las coordenadas (Δx, «delta x») es un cateto, la diferencia vertical (Δy) es el otro, y la distancia buscada es la hipotenusa. Por el teorema de Pitágoras:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">d = √[(x₂ − x₁)² + (y₂ − y₁)²]</p>
{fig_distancia()}
{ejemplo(t("Example 1: legs 3 and 4. Find the distance between P(1, 2) and Q(4, 6).", "Ejemplo 1 · Catetos 3 y 4. Hallar la distancia entre P(1, 2) y Q(4, 6)."),
  [("1", t("Find the differences.", "Se calculan las diferencias."), "x₂ − x₁ = 4 − 1 = 3 " + t("and", "y") + " y₂ − y₁ = 6 − 2 = 4."),
   ("2", t("Substitute.", "Se sustituye."), "d = √(3² + 4²) = √(9 + 16)."),
   ("3", t("Add and take the square root.", "Se suma y se saca la raíz."), "d = √25 = 5."),
   ("✓", t("Answer.", "Respuesta."), t("The distance is <strong>5 units</strong>.", "La distancia es de <strong>5 unidades</strong>."))])}
{ejemplo(t("Example 2: with negative coordinates. Find the distance between A(−2, 1) and B(3, 13).", "Ejemplo 2 · Con coordenadas negativas. Hallar la distancia entre A(−2, 1) y B(3, 13)."),
  [("1", t("Differences.", "Diferencias."), "3 − (−2) = 5 " + t("and", "y") + " 13 − 1 = 12."),
   ("2", t("Substitute.", "Sustitución."), "d = √(5² + 12²) = √(25 + 144) = √169."),
   ("3", t("Square root.", "Raíz."), "d = 13."),
   ("✓", t("Answer.", "Respuesta."), t("The distance is <strong>13 units</strong>.", "La distancia es de <strong>13 unidades</strong>."))])}
{caja("tip", t("The order of the subtraction does not matter", "El orden de la resta no importa"), t("<p>Because the differences are squared, it makes no difference whether you subtract (x₂ − x₁) or (x₁ − x₂): squaring turns any result positive. Be careful with negative coordinates, though: from −2 to 3 is 3 − (−2) = 5, not 3 − 2.</p>", "<p>Como las diferencias se elevan al cuadrado, da igual restar (x₂ − x₁) o (x₁ − x₂): el cuadrado convierte cualquier resultado en positivo. Eso sí, cuidado con las coordenadas negativas: de −2 a 3 hay 3 − (−2) = 5, no 3 − 2.</p>"))}
{calc(t("With the calculator", "Con la calculadora"), t("<p>When the sum of the squares is not a perfect square, use the calculator. Between (1, 1) and (4, 3): √(3² + 2²) = √13 ≈ 3.6. Round to the tenth unless the problem says otherwise.</p>", "<p>Cuando la suma de los cuadrados no es un cuadrado perfecto, use la calculadora. Entre (1, 1) y (4, 3): √(3² + 2²) = √13 ≈ 3.6. Redondee a la décima, salvo que el problema diga otra cosa.</p>"))}
{practica("p2", t("Practice 2 — From the origin", "Práctica 2 — Desde el origen"), t("What is the distance between (0, 0) and (3, 4)?", "¿Cuál es la distancia entre (0, 0) y (3, 4)?"), [("a", "7"), ("b", "5"), ("c", "25")])}
{practica("p3", t("Practice 3 — A vertical segment", "Práctica 3 — Un segmento vertical"), t("What is the distance between (1, 1) and (1, 6)?", "¿Cuál es la distancia entre (1, 1) y (1, 6)?"), [("a", "5"), ("b", "6"), ("c", "7")])}
{practica("p4", t("Practice 4 — With a negative coordinate", "Práctica 4 — Con una coordenada negativa"), t("What is the distance between (−1, 2) and (2, 6)?", "¿Cuál es la distancia entre (−1, 2) y (2, 6)?"), [("a", "4"), ("b", "25"), ("c", "5")])}
{enlace(n, t("distance", "distancia"), t("the distance between two points", "la distancia entre dos puntos"), t("See the right triangle form between the two points, find the hypotenuse step by step, and measure real distances on a map of Illinois.", "Vea cómo se forma el triángulo rectángulo entre los dos puntos, calcule la hipotenusa paso a paso y mida distancias reales en un mapa de Illinois."))}'''

    s3 = f'''<p>{t("The <strong>midpoint</strong> is the point exactly halfway along the segment that joins two points. Its x-coordinate is the average of the two x-coordinates, and its y-coordinate is the average of the two y-coordinates:",
 "El <strong>punto medio</strong> es el punto que está exactamente a la mitad del segmento que une dos puntos. Su coordenada x es el promedio de las dos coordenadas x, y su coordenada y es el promedio de las dos coordenadas y:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">M = ( (x₁ + x₂) ÷ 2 , (y₁ + y₂) ÷ 2 )</p>
{fig_medio()}
{ejemplo(t("Example 3: a midpoint. Find the midpoint of the segment from A(2, 4) to B(8, 10).", "Ejemplo 3 · Punto medio. Hallar el punto medio del segmento que une A(2, 4) y B(8, 10)."),
  [("1", t("Average of the x's.", "Promedio de las x."), "(2 + 8) ÷ 2 = 10 ÷ 2 = 5."),
   ("2", t("Average of the y's.", "Promedio de las y."), "(4 + 10) ÷ 2 = 14 ÷ 2 = 7."),
   ("✓", t("Answer.", "Respuesta."), t("The midpoint is <strong>M(5, 7)</strong>.", "El punto medio es <strong>M(5, 7)</strong>."))])}
{ejemplo(t("Example 4: finding an endpoint from the midpoint. The midpoint of a segment is M(4, 3) and one endpoint is A(2, 1). What is the other endpoint B(x, y)?", "Ejemplo 4 · Hallar un extremo a partir del punto medio. El punto medio de un segmento es M(4, 3) y uno de sus extremos es A(2, 1). ¿Cuál es el otro extremo B(x, y)?"),
  [("1", t("For x.", "Para la x."), t("(2 + x) ÷ 2 = 4, so 2 + x = 8, and x = 6.", "(2 + x) ÷ 2 = 4, entonces 2 + x = 8, de donde x = 6.")),
   ("2", t("For y.", "Para la y."), t("(1 + y) ÷ 2 = 3, so 1 + y = 6, and y = 5.", "(1 + y) ÷ 2 = 3, entonces 1 + y = 6, de donde y = 5.")),
   ("✓", t("Answer.", "Respuesta."), t("The other endpoint is <strong>B(6, 5)</strong>. Check: the midpoint of (2, 1) and (6, 5) is (4, 3).", "El otro extremo es <strong>B(6, 5)</strong>. Comprobación: el punto medio de (2, 1) y (6, 5) es (4, 3)."))])}
{caja("ojo", t("Two common slips", "Dos descuidos frecuentes"), t("<p>The first is adding and forgetting to divide by 2: the point lands twice as far away. The second is subtracting instead of adding: the difference is used for the distance, not for the midpoint. If a sum is odd, the coordinate ends in .5, and that is fine.</p>", "<p>El primero es sumar y olvidar dividir entre 2: el punto queda al doble de distancia. El segundo es restar en lugar de sumar: la diferencia sirve para la distancia, no para el punto medio. Si una suma es impar, la coordenada termina en .5, y está bien.</p>"))}
{practica("p5", t("Practice 5 — A midpoint", "Práctica 5 — Un punto medio"), t("What is the midpoint of the segment from (2, 2) to (6, 8)?", "¿Cuál es el punto medio del segmento de (2, 2) a (6, 8)?"), [("a", "(8, 10)"), ("b", "(4, 5)"), ("c", "(4, 4)")])}
{practica("p6", t("Practice 6 — From the origin", "Práctica 6 — Desde el origen"), t("What is the midpoint of the segment from (0, 0) to (10, 4)?", "¿Cuál es el punto medio del segmento de (0, 0) a (10, 4)?"), [("a", "(5, 2)"), ("b", "(10, 4)"), ("c", "(5, 4)")])}
{practica("p7", t("Practice 7 — With negative coordinates", "Práctica 7 — Con coordenadas negativas"), t("What is the midpoint of the segment from (−4, 2) to (2, −6)?", "¿Cuál es el punto medio del segmento de (−4, 2) a (2, −6)?"), [("a", "(−2, −4)"), ("b", "(3, 4)"), ("c", "(−1, −2)")])}
{enlace(n, t("midpoint", "punto-medio"), t("the midpoint of a segment", "el punto medio de un segmento"), t("Average the coordinates and check on the graph that the point lands right in the middle; then find a missing endpoint.", "Promedie las coordenadas y compruebe en la gráfica que el punto queda justo en el centro; después halle un extremo que falta."))}'''

    s4 = f'''<p>{t("When the vertices of a figure are given as points on the plane, the distance formula lets you measure each side and add them to get the <strong>perimeter</strong>.", "Cuando los vértices de una figura se dan como puntos del plano, la fórmula de la distancia permite medir cada lado y sumarlos para obtener el <strong>perímetro</strong>.")}</p>
{ejemplo(t("Example 5: the perimeter of a triangle. A triangle has vertices A(0, 0), B(3, 0), and C(0, 4). Find its perimeter.", "Ejemplo 5 · Perímetro de un triángulo. Un triángulo tiene vértices en A(0, 0), B(3, 0) y C(0, 4). Calcular su perímetro."),
  [("1", t("Side AB (horizontal).", "Lado AB (horizontal)."), t("Same y, so subtract the x's: 3 − 0 = 3.", "Misma y, así que se restan las x: 3 − 0 = 3.")),
   ("2", t("Side AC (vertical).", "Lado AC (vertical)."), t("Same x, so subtract the y's: 4 − 0 = 4.", "Misma x, así que se restan las y: 4 − 0 = 4.")),
   ("3", t("Side BC (slanted).", "Lado BC (inclinado)."), "d = √[(0 − 3)² + (4 − 0)²] = √(9 + 16) = √25 = 5."),
   ("4", t("Perimeter.", "Perímetro."), "3 + 4 + 5 = 12."),
   ("✓", t("Answer.", "Respuesta."), t("The perimeter is <strong>12 units</strong>.", "El perímetro es de <strong>12 unidades</strong>."))])}
{caja("tip", t("A useful shortcut", "Atajo útil"), t("<p>When two points have the same x-coordinate, the segment is vertical and its length is the difference of the y's. When they have the same y, it is horizontal and its length is the difference of the x's. Only slanted sides need the whole formula.</p>", "<p>Cuando dos puntos comparten la misma coordenada x, el segmento es vertical y su longitud es la diferencia de las y. Si comparten la misma y, es horizontal y su longitud es la diferencia de las x. Solo los lados inclinados requieren la fórmula completa.</p>"))}
{enlace(n, t("perimeter", "perimetro"), t("the perimeter on the plane", "el perímetro en el plano"), t("Measure each side by subtracting or with the distance formula, and add.", "Mida cada lado restando o con la fórmula de la distancia, y sume."))}'''

    secciones = [("s-" + t("plane", "plano"), t("The coordinate plane and ordered pairs", "El plano cartesiano y los pares ordenados"), s1),
                 ("s-" + t("distance", "distancia"), t("The distance between two points", "La distancia entre dos puntos"), s2),
                 ("s-" + t("midpoint", "punto-medio"), t("The midpoint of a segment", "El punto medio de un segmento"), s3),
                 ("s-" + t("perimeter", "perimetro"), t("Figures on the plane: the perimeter", "Figuras en el plano: el perímetro"), s4)]

    lesson = {"next": t("Lesson 1.2", "Lección 1.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("In Quadrant II, y is positive. Here y = −1.", "En el cuadrante II la y es positiva. Aquí y = −1."), "c": t("In Quadrant IV, x is positive. Here x = −5.", "En el cuadrante IV la x es positiva. Aquí x = −5.")}, "right": t("Both coordinates are negative: Quadrant III.", "Las dos coordenadas son negativas: cuadrante III."), "solution": t("x < 0 and y < 0: Quadrant III.", "x < 0 y y < 0: cuadrante III.")},
      "p2": {"ok": "b", "hints": {"a": t("You added the legs (3 + 4). Add their squares and take the square root.", "Sumó los catetos (3 + 4). Hay que sumar sus cuadrados y sacar la raíz."), "c": t("25 is d². You still need the square root.", "25 es d². Falta sacar la raíz.")}, "right": "√(3² + 4²) = √25 = 5.", "solution": "d = √(9 + 16) = √25 = 5."},
      "p3": {"ok": "a", "hints": {"b": t("Same x, so the segment is vertical: subtract the y's, 6 − 1.", "Misma x: el segmento es vertical. Se restan las y: 6 − 1."), "c": t("You added the y's. Subtract them: 6 − 1.", "Sumó las y. Hay que restarlas: 6 − 1.")}, "right": t("A vertical segment: 6 − 1 = 5.", "Segmento vertical: 6 − 1 = 5."), "solution": "6 − 1 = 5."},
      "p4": {"ok": "c", "hints": {"a": t("That is only Δy. Use both differences: Δx = 2 − (−1) = 3 and Δy = 4.", "Ese es solo Δy. Use las dos diferencias: Δx = 2 − (−1) = 3 y Δy = 4."), "b": t("25 is d². Take the square root.", "25 es d². Saque la raíz.")}, "right": "Δx = 2 − (−1) = 3, Δy = 4, d = √25 = 5.", "solution": "√(3² + 4²) = √25 = 5."},
      "p5": {"ok": "b", "hints": {"a": t("You added but did not divide by 2.", "Sumó pero no dividió entre 2."), "c": t("The x is right. For y: (2 + 8) ÷ 2.", "La x está bien. Para la y: (2 + 8) ÷ 2.")}, "right": "((2 + 6) ÷ 2, (2 + 8) ÷ 2) = (4, 5).", "solution": "M = (8 ÷ 2, 10 ÷ 2) = (4, 5)."},
      "p6": {"ok": "a", "hints": {"b": t("That is the other endpoint. Divide each coordinate by 2.", "Ese es el otro extremo. Divida cada coordenada entre 2."), "c": t("The x is right. For y: (0 + 4) ÷ 2.", "La x está bien. Para la y: (0 + 4) ÷ 2.")}, "right": "(10 ÷ 2, 4 ÷ 2) = (5, 2).", "solution": "M = (5, 2)."},
      "p7": {"ok": "c", "hints": {"a": t("You added but did not divide by 2.", "Sumó pero no dividió entre 2."), "b": t("You subtracted. For the midpoint, add and divide by 2: (−4 + 2) ÷ 2.", "Restó. Para el punto medio se suma y se divide entre 2: (−4 + 2) ÷ 2.")}, "right": "((−4 + 2) ÷ 2, (2 + (−6)) ÷ 2) = (−1, −2).", "solution": "M = (−2 ÷ 2, −4 ÷ 2) = (−1, −2)."},
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("In Quadrant I both coordinates are positive. Here x = −3.", "En el cuadrante I las dos coordenadas son positivas. Aquí x = −3."), "c": t("In Quadrant III both are negative. Here y = 5.", "En el cuadrante III las dos son negativas. Aquí y = 5."), "d": t("In Quadrant IV, x is positive and y negative. It is the other way around here.", "En el cuadrante IV la x es positiva y la y negativa. Aquí es al revés.")}, "solution": t("x < 0 and y > 0: Quadrant II.", "x < 0 y y > 0: cuadrante II.")},
      "B": {"ok": "b", "hints": {"a": t("On the x-axis, y = 0. Here x = 0.", "Sobre el eje x, y = 0. Aquí es x = 0."), "c": t("A point with a 0 coordinate is on an axis, not in a quadrant.", "Un punto con una coordenada 0 está sobre un eje, no en un cuadrante."), "d": t("The origin is (0, 0). Here y = −4.", "El origen es (0, 0). Aquí y = −4.")}, "solution": t("x = 0: the point is on the y-axis.", "x = 0: el punto está sobre el eje y.")},
      "C": {"ok": "c", "hints": {"a": t("Left means x is negative; down means y is negative.", "A la izquierda, la x es negativa; abajo, la y es negativa."), "b": t("Down means y is negative.", "Abajo, la y es negativa."), "d": t("Left means x is negative.", "A la izquierda, la x es negativa.")}, "solution": "(−2, −3)."},
      "D": {"ok": "d", "hints": {"a": t("You added the legs. Add their squares and take the square root.", "Sumó los catetos. Hay que sumar sus cuadrados y sacar la raíz."), "b": t("You multiplied the legs. Add their squares.", "Multiplicó los catetos. Hay que sumar sus cuadrados."), "c": t("25 is d². Take the square root.", "25 es d². Saque la raíz.")}, "solution": "Δx = 3, Δy = 4, d = √25 = 5."},
      "E": {"ok": "a", "hints": {"b": t("You subtracted the y's. Add them and divide by 2.", "Restó las y. Hay que sumarlas y dividir entre 2."), "c": t("You did not divide by 2.", "No dividió entre 2."), "d": t("Check the signs: (−3 + 7) ÷ 2 = 2.", "Revise los signos: (−3 + 7) ÷ 2 = 2.")}, "solution": "((−3 + 7) ÷ 2, (5 + (−1)) ÷ 2) = (2, 2)."},
      "F": {"ok": "c", "hints": {"a": t("That is only AB + AC. The slanted side BC is missing.", "Eso es solo AB + AC. Falta el lado inclinado BC."), "b": t("Measure BC with the formula: √(9 + 16) = 5.", "Mida BC con la fórmula: √(9 + 16) = 5."), "d": t("Check the slanted side: BC = 5, not 8.", "Revise el lado inclinado: BC = 5, no 8.")}, "solution": "3 + 4 + 5 = 12."},
      "G": {"ok": "d", "hints": {"a": t("That is the midpoint of A and M, not the other endpoint.", "Ese es el punto medio entre A y M, no el otro extremo."), "b": t("Solve (2 + x) ÷ 2 = 4 for x.", "Despeje x en (2 + x) ÷ 2 = 4."), "c": t("You doubled M. Then subtract A: 8 − 2 and 6 − 1.", "Duplicó M. Ahora reste A: 8 − 2 y 6 − 1.")}, "solution": "x = 2 · 4 − 2 = 6, y = 2 · 3 − 1 = 5."},
      "H": {"ok": "b", "hints": {"a": t("You subtracted 5 − 2 instead of 5 − (−2).", "Restó 5 − 2 en lugar de 5 − (−2)."), "c": t("49 is d². Take the square root.", "49 es d². Saque la raíz."), "d": t("Same y, so the segment is horizontal: subtract the x's.", "Misma y: el segmento es horizontal. Se restan las x.")}, "solution": "5 − (−2) = 7."},
     }}

    quiz = [
     ("A", t("Which quadrant is the point (−3, 5) in?", "¿En qué cuadrante está el punto (−3, 5)?"), [("a", t("Quadrant II", "Cuadrante II")), ("b", t("Quadrant I", "Cuadrante I")), ("c", t("Quadrant III", "Cuadrante III")), ("d", t("Quadrant IV", "Cuadrante IV"))]),
     ("B", t("Where is the point (0, −4)?", "¿Dónde se localiza el punto (0, −4)?"), [("a", t("On the x-axis", "Sobre el eje x")), ("b", t("On the y-axis", "Sobre el eje y")), ("c", t("In Quadrant III", "En el cuadrante III")), ("d", t("At the origin", "En el origen"))]),
     ("C", t("A point is 2 units to the left of the origin and 3 units down. What are its coordinates?", "Un punto está 2 unidades a la izquierda y 3 hacia abajo del origen. ¿Cuáles son sus coordenadas?"), [("a", "(2, 3)"), ("b", "(−2, 3)"), ("c", "(−2, −3)"), ("d", "(2, −3)")]),
     ("D", t("What is the distance between (1, 2) and (4, 6)?", "¿Cuál es la distancia entre (1, 2) y (4, 6)?"), [("a", "7"), ("b", "12"), ("c", "25"), ("d", "5")]),
     ("E", t("What is the midpoint of the segment from (−3, 5) to (7, −1)?", "¿Cuál es el punto medio del segmento de (−3, 5) a (7, −1)?"), [("a", "(2, 2)"), ("b", "(2, 3)"), ("c", "(4, 4)"), ("d", "(−5, 3)")]),
     ("F", t("A triangle has vertices A(0, 0), B(3, 0), and C(0, 4). What is its perimeter?", "Un triángulo tiene vértices A(0, 0), B(3, 0) y C(0, 4). ¿Cuál es su perímetro?"), [("a", "7"), ("b", "10"), ("c", "12"), ("d", "15")]),
     ("G", t("The midpoint of a segment is (4, 3) and one endpoint is (2, 1). What is the other endpoint?", "El punto medio de un segmento es (4, 3) y un extremo es (2, 1). ¿Cuál es el otro extremo?"), [("a", "(3, 2)"), ("b", "(2, 2)"), ("c", "(8, 6)"), ("d", "(6, 5)")]),
     ("H", t("On a map grid, the library is at (−2, 4) and the clinic at (5, 4). Each unit is 1 block. How many blocks apart are they in a straight line?", "En la cuadrícula de un mapa, la biblioteca está en (−2, 4) y la clínica en (5, 4). Cada unidad es 1 cuadra. ¿A cuántas cuadras están en línea recta?"), [("a", "3"), ("b", "7"), ("c", "49"), ("d", "8")])]

    tarea = (t("For your own work, with a notebook and graph paper: (1) Eight points on the plane: two in each quadrant, one on the x-axis, and one on the y-axis. Graph them, write their coordinates, and note the quadrant or the axis of each one. (2) Six distances between two points: two horizontal or vertical segments, two with negative coordinates, and two whose square root is not exact (round to the tenth with the calculator). Write Δx and Δy before you substitute. (3) Four midpoints and two missing-endpoint problems; check each endpoint by finding the midpoint again with both endpoints. (4) A rectangle with vertices (−3, −1), (5, −1), (5, 4), and (−3, 4), and a triangle with vertices (0, 0), (6, 0), and (0, 8): graph them and find the perimeter of each. Say which sides you could measure without the whole formula. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y papel cuadriculado: (1) Ocho puntos en el plano: dos en cada cuadrante, uno sobre el eje x y otro sobre el eje y. Grafíquelos, escriba sus coordenadas y anote el cuadrante o el eje de cada uno. (2) Seis distancias entre dos puntos: dos de segmentos horizontales o verticales, dos con coordenadas negativas y dos cuya raíz no sea exacta (redondee a la décima con la calculadora). Escriba Δx y Δy antes de sustituir. (3) Cuatro puntos medios y dos problemas de extremo desconocido; compruebe cada extremo calculando de nuevo el punto medio con los dos extremos. (4) Un rectángulo con vértices en (−3, −1), (5, −1), (5, 4) y (−3, 4) y un triángulo con vértices en (0, 0), (6, 0) y (0, 8): grafíquelos y calcule el perímetro de cada uno. Indique qué lados pudo medir sin la fórmula completa. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Take a map of your neighborhood (a printed one or on your phone) and draw a grid on it, with your home at the origin (0, 0) and 1 unit = 1 block. Write the coordinates of three places you go often (the store, the school, the bus stop). Find the straight-line distance from home to each one, and the midpoint between two of them: is there anything there?",
               "Tome un mapa de su vecindario (impreso o en el teléfono) y trácele una cuadrícula, con su casa en el origen (0, 0) y 1 unidad = 1 cuadra. Escriba las coordenadas de tres lugares a los que va a menudo (la tienda, la escuela, la parada del autobús). Calcule la distancia en línea recta de su casa a cada uno y el punto medio entre dos de ellos: ¿qué hay en ese lugar?"))

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("Graph ordered pairs in the four quadrants, find the distance between two points with the Pythagorean theorem, and find the midpoint of a segment.", "Grafique pares ordenados en los cuatro cuadrantes, halle la distancia entre dos puntos con el teorema de Pitágoras y calcule el punto medio de un segmento."),
        ("📐", t("Graph paper and a calculator", "Papel cuadriculado y calculadora")),
        [t("<strong>Graph</strong> ordered pairs in the four quadrants of the coordinate plane.", "<strong>Graficar</strong> pares ordenados en los cuatro cuadrantes del plano cartesiano."),
         t("<strong>Find</strong> the distance between two points with the formula that comes from the Pythagorean theorem.", "<strong>Calcular</strong> la distancia entre dos puntos con la fórmula que se deriva del teorema de Pitágoras."),
         t("<strong>Find</strong> the midpoint of a segment, and a missing endpoint from the midpoint.", "<strong>Calcular</strong> el punto medio de un segmento y un extremo que falta a partir del punto medio."),
         t("<strong>Identify</strong> figures on the coordinate plane and find their perimeter.", "<strong>Identificar</strong> figuras en el plano de coordenadas y calcular su perímetro.")],
        secciones, tarea, quiz,
        t("Self-check checklist for the coordinate plane", "Lista de autoevaluación del plano cartesiano"),
        t("Self-check checklist: skills for ordered pairs, distance, and midpoint", "Lista de autoevaluación: destrezas de pares ordenados, distancia y punto medio"),
        [(t("Graphing ordered pairs", "Graficar pares ordenados"), t("I graph points in the four quadrants and name the quadrant from the signs without hesitating.", "Grafico puntos en los cuatro cuadrantes y nombro el cuadrante por los signos sin vacilar."), t("I graph with occasional sign or quadrant mistakes.", "Grafico con errores ocasionales de signo o de cuadrante."), t("I swap the coordinates or mix up the quadrants.", "Invierto las coordenadas o confundo los cuadrantes.")),
         (t("Using the distance formula", "Aplicar la fórmula de la distancia"), t("I use the formula with no substitution mistakes and notice when a segment is horizontal or vertical.", "Aplico la fórmula sin errores de sustitución y reconozco cuándo el segmento es horizontal o vertical."), t("I use the formula with substitution or sign mistakes.", "Aplico la fórmula con errores de sustitución o de signo."), t("I add the coordinates without squaring them.", "Sumo las coordenadas sin elevarlas al cuadrado.")),
         (t("Finding the midpoint", "Calcular el punto medio"), t("I find the midpoint, and a missing endpoint from the midpoint.", "Calculo el punto medio y hallo un extremo desconocido a partir del punto medio."), t("I find the midpoint with occasional mistakes.", "Calculo el punto medio con errores ocasionales."), t("I add the coordinates without dividing by 2.", "Sumo las coordenadas sin dividir entre 2.")),
         (t("Perimeter on the plane", "Perímetro en el plano"), t("I measure each side (subtracting or with the formula) and add them.", "Mido cada lado (restando o con la fórmula) y los sumo."), t("I forget a side or measure a slanted side by adding Δx and Δy.", "Olvido un lado o mido un lado inclinado sumando Δx y Δy."), t("I do not know how to measure the sides from the coordinates.", "No sé medir los lados a partir de las coordenadas."))],
        t("<p>In this lesson you set up the language of the coordinate plane: ordered pairs and the four quadrants, the distance formula (which is just the Pythagorean theorem with coordinates), and the midpoint formula (the average of the coordinates). With them you measured the sides and the perimeter of figures on the plane.</p>\n<p>In <strong>Lesson 1.2 · Slope: idea, formula, and meaning</strong> you will measure how steep a line is. The slope is the vertical change divided by the horizontal change (the same Δy and Δx of this lesson), and you will read it as a rate of change: dollars per hour, miles per hour, or cost per item.</p>",
          "<p>En esta lección se estableció el lenguaje del plano cartesiano: los pares ordenados y los cuatro cuadrantes, la fórmula de la distancia (que no es más que el teorema de Pitágoras con coordenadas) y la fórmula del punto medio (el promedio de las coordenadas). Con ellas se midieron los lados y el perímetro de figuras en el plano.</p>\n<p>En la <strong>Lección 1.2 · La pendiente: concepto, fórmula e interpretación</strong> se medirá la inclinación de una recta. La pendiente es el cambio vertical dividido entre el cambio horizontal (los mismos Δy y Δx de esta lección) y se interpretará como una tasa de cambio: dólares por hora, millas por hora o costo por unidad.</p>"),
        ("1-2", ("", t("Lesson 1.2 · Slope: idea, formula, and meaning", "Lección 1.2 · La pendiente: concepto, fórmula e interpretación"))),
        [(t("coordinate plane", "plano cartesiano"), t("Two perpendicular number lines, the x-axis and the y-axis, that cross at the origin.", "Dos rectas numéricas perpendiculares, el eje x y el eje y, que se cruzan en el origen.")),
         (t("ordered pair", "par ordenado"), t("(x, y): the move across first, then the move up or down.", "(x, y): primero el desplazamiento horizontal y después el vertical.")),
         (t("quadrant", "cuadrante"), t("Each of the four regions the axes make, numbered I to IV counterclockwise.", "Cada una de las cuatro regiones que forman los ejes, numeradas del I al IV en sentido contrario a las manecillas del reloj.")),
         (t("distance formula", "fórmula de la distancia"), "d = √[(x₂ − x₁)² + (y₂ − y₁)²]"),
         (t("midpoint", "punto medio"), t("The point halfway along a segment: the average of the x's and of the y's.", "El punto a mitad de un segmento: el promedio de las x y el de las y."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ===== MODULE 1 · The plane: explore, place, read ===== */
var PL = {modo: 1, obj: null, intentos: 0, bien: 0, total: 0, racha: 0, hecho: false}, plano;
function plInfo(x, y){
  if (x === null){ $("pl-info").innerHTML = ""; return; }
  $("pl-info").innerHTML = '<div class="linea">' + T("Across (x): ", "Movimiento horizontal (x): ") + (x === 0 ? T("none", "ninguno") : Math.abs(x) + (x > 0 ? T(" to the right", " a la derecha") : T(" to the left", " a la izquierda"))) +
    " · " + T("Up or down (y): ", "Movimiento vertical (y): ") + (y === 0 ? T("none", "ninguno") : Math.abs(y) + (y > 0 ? T(" up", " hacia arriba") : T(" down", " hacia abajo"))) + "</div>" +
    '<div class="linea">' + parHTML(x, y) + " → " + cuadrante(x, y) + "</div>";
}
function plMarcador(){ $("pl-marcador").textContent = PL.total ? T("Right: ", "Aciertos: ") + PL.bien + T(" of ", " de ") + PL.total + " · " + T("streak: ", "racha: ") + PL.racha : ""; }
function plFin(ok){
  PL.hecho = true; PL.total++; if (ok){ PL.bien++; PL.racha++; } else PL.racha = 0; plMarcador();
}
function plNuevo(){
  var x = azarNZ(-7, 7), y = azarNZ(-7, 7);
  if (Math.random() < 0.15){ if (Math.random() < 0.5) x = 0; else y = 0; }
  PL.obj = [x, y]; PL.intentos = 0; PL.hecho = false;
  $("pl-fb").className = "fb"; $("pl-fb").innerHTML = ""; plInfo(null);
  ["pl-x", "pl-y"].forEach(function(i){ $(i).value = ""; $(i).disabled = false; });
  if (PL.modo === 2){ plano.limpia(); $("pl-enun").innerHTML = T("Mark the point ", "Marque el punto ") + "<strong>" + parHTML(x, y) + "</strong>" + T(" on the plane (click it, or use the arrow keys and Enter).", " en el plano (haga clic, o use las flechas y Enter)."); }
  if (PL.modo === 3){ plano.limpia(); plano.pinta(plano.P.punto(PL.obj, C4.azul, "P", null, 7)); $("pl-enun").innerHTML = T("Write the coordinates of point P.", "Escriba las coordenadas del punto P."); }
}
function plModo(m){
  PL.modo = m;
  [1, 2, 3].forEach(function(k){ $("pl-m" + k).setAttribute("aria-pressed", k === m ? "true" : "false"); });
  $("pl-leer").hidden = m !== 3; $("pl-otro").hidden = m === 1;
  plano.limpia(); $("pl-fb").className = "fb"; $("pl-fb").innerHTML = ""; plInfo(null);
  if (m === 1) $("pl-enun").innerHTML = T("Mark any point and look at its coordinates. Then try the other two modes.", "Marque cualquier punto y observe sus coordenadas. Después pruebe los otros dos modos.");
  else plNuevo();
}
function plRevisa(x, y){
  if (PL.hecho) return;
  var o = PL.obj, fb = $("pl-fb");
  if (x === o[0] && y === o[1]){
    fb.className = "fb bien"; fb.innerHTML = TX.bien + parHTML(o[0], o[1]) + " → " + cuadrante(o[0], o[1]) + ". <em>" + elige(PL.intentos ? ELOGIO2 : ELOGIO) + "</em>";
    plInfo(o[0], o[1]); plFin(true); $("pl-x").disabled = $("pl-y").disabled = true; return;
  }
  PL.intentos++;
  if (PL.intentos >= 2){
    fb.className = "fb mal"; fb.innerHTML = TX.asi + T("The point is ", "El punto es ") + parHTML(o[0], o[1]) + ": " + T("from the origin, ", "desde el origen, ") +
      (o[0] === 0 ? T("do not move across", "no se mueve horizontalmente") : Math.abs(o[0]) + (o[0] > 0 ? T(" to the right", " a la derecha") : T(" to the left", " a la izquierda"))) + T(", then ", " y después ") +
      (o[1] === 0 ? T("do not move up or down", "no se mueve verticalmente") : Math.abs(o[1]) + (o[1] > 0 ? T(" up", " hacia arriba") : T(" down", " hacia abajo"))) + "." + TX.nuevo;
    if (PL.modo === 2) plano.pinta(plano.P.punto(o, C4.verde, T("here", "aquí"), null, 7));
    plFin(false); $("pl-x").disabled = $("pl-y").disabled = true;
  } else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + diagPar(x, y, o[0], o[1]) + TX.unoMas; }
}
plano = PlanoActivo($("pl-plano"), {xmin: -8, xmax: 8, ymin: -8, ymax: 8, u: 30, cuadrantes: true, paso: 2},
  function(x, y){ if (PL.modo === 1) plInfo(x, y); else if (PL.modo === 2) plRevisa(x, y); },
  T("Coordinate plane from −8 to 8 on each axis.", "Plano cartesiano de −8 a 8 en cada eje."));
[1, 2, 3].forEach(function(k){ $("pl-m" + k).addEventListener("click", function(){ plModo(k); }); });
$("pl-otro").addEventListener("click", plNuevo);
$("pl-comprobar").addEventListener("click", function(){ var v = [leeDecimal($("pl-x").value), leeDecimal($("pl-y").value)]; if (v[0] === null || v[1] === null){ $("pl-fb").className = "fb pista"; $("pl-fb").innerHTML = T("Type a number in each box.", "Escriba un número en cada casilla."); return; } plRevisa(v[0], v[1]); });
["pl-x", "pl-y"].forEach(function(i){ $(i).addEventListener("keydown", function(ev){ if (ev.key === "Enter") $("pl-comprobar").click(); }); });
plModo(1);

/* Quadrant or axis */
OMR("cu", function(){
  var x = azarNZ(-9, 9), y = azarNZ(-9, 9), r = Math.random();
  if (r < 0.12) x = 0; else if (r < 0.24) y = 0;
  var ops = [["I", T("Quadrant I", "Cuadrante I")], ["II", T("Quadrant II", "Cuadrante II")], ["III", T("Quadrant III", "Cuadrante III")], ["IV", T("Quadrant IV", "Cuadrante IV")], ["ex", T("On the x-axis", "Sobre el eje x")], ["ey", T("On the y-axis", "Sobre el eje y")]];
  var ok = x === 0 ? "ey" : (y === 0 ? "ex" : (x > 0 ? (y > 0 ? "I" : "IV") : (y > 0 ? "II" : "III")));
  return {enun: T("Where is the point ", "¿Dónde está el punto ") + "<strong>" + parHTML(x, y) + "</strong>?", correcta: ok, enOrden: true,
    opciones: ops.map(function(o){ return {clave: o[0], html: o[1]}; }),
    porClave: {ex: T("On the x-axis the y-coordinate is 0.", "Sobre el eje x la coordenada y vale 0."), ey: T("On the y-axis the x-coordinate is 0.", "Sobre el eje y la coordenada x vale 0.")},
    pista: T("Look at the signs: x tells left (−) or right (+); y tells down (−) or up (+). A 0 puts the point on an axis.", "Fíjese en los signos: la x dice izquierda (−) o derecha (+); la y, abajo (−) o arriba (+). Un 0 pone el punto sobre un eje."),
    bien: parHTML(x, y) + " → " + cuadrante(x, y) + "."};
});

/* ===== MODULE 2 · Distance ===== */
var DI = {modo: "plano", a: null, b: null, ver: true};
var CIUDADES = [{n: "Chicago", x: 430, y: 80}, {n: "Rockford", x: 370, y: 35}, {n: "Freeport", x: 330, y: 25}, {n: "Elgin", x: 425, y: 65}, {n: "Naperville", x: 415, y: 100}, {n: "Aurora", x: 405, y: 120},
  {n: "Joliet", x: 425, y: 140}, {n: "Kankakee", x: 430, y: 210}, {n: "Pontiac", x: 395, y: 255}, {n: "Bloomington", x: 355, y: 330}, {n: "Peoria", x: 285, y: 285}, {n: "Galesburg", x: 245, y: 235},
  {n: "Rock Island", x: 185, y: 160}, {n: "Kewanee", x: 235, y: 195}, {n: "Macomb", x: 205, y: 315}, {n: "Quincy", x: 130, y: 380}, {n: "Springfield", x: 310, y: 360, capital: true},
  {n: "Decatur", x: 360, y: 370}, {n: "Champaign", x: 410, y: 385}, {n: "Charleston", x: 425, y: 400}, {n: "Vandalia", x: 390, y: 430}, {n: "Alton", x: 150, y: 415}];
var MILLAS = 0.982;
function diDibuja(){
  var a = DI.a, b = DI.b, s;
  if (DI.modo === "plano"){
    var P = Plano({xmin: -9, xmax: 9, ymin: -9, ymax: 9, u: 28, paso: 3});
    s = (DI.ver ? catetos(P, a, b) : "") + P.seg(a, b, C4.tinta, 3.5) + P.punto(a, C4.azul, "A" + par(a[0], a[1])) + P.punto(b, C4.azul, "B" + par(b[0], b[1]));
    $("di-svg").innerHTML = P.svg(s, T("Points A", "Puntos A") + par(a[0], a[1]) + T(" and B", " y B") + par(b[0], b[1]) + T(" joined by a segment", " unidos por un segmento") + (DI.ver ? T(", with the horizontal and vertical legs drawn.", ", con los catetos horizontal y vertical dibujados.") : "."));
  } else {
    var W = 580, H = 520, ox = 40, oy = 10;
    s = '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("Map of most of Illinois with a coordinate grid. ", "Mapa de la mayor parte de Illinois con una cuadrícula de coordenadas. ") + a.n + T(" is at ", " está en ") + par(a.x, a.y) + T(" and ", " y ") + b.n + T(" at ", " en ") + par(b.x, b.y) + '." style="max-width:580px">';
    s += '<image href="/img/illinois-mapa.jpg" x="' + ox + '" y="' + oy + '" width="520" height="470" opacity="0.45" preserveAspectRatio="none"/>';
    for (var v = 0; v <= 450; v += 50) s += '<line x1="' + ox + '" y1="' + (oy + v) + '" x2="' + (ox + 520) + '" y2="' + (oy + v) + '" stroke="#b0bec5" stroke-width="1"/><text x="' + (ox - 6) + '" y="' + (oy + v + 4) + '" font-size="12" fill="#455a64" text-anchor="end">' + v + "</text>";
    for (v = 0; v <= 500; v += 50) s += '<line x1="' + (ox + v) + '" y1="' + oy + '" x2="' + (ox + v) + '" y2="' + (oy + 470) + '" stroke="#b0bec5" stroke-width="1"/><text x="' + (ox + v) + '" y="' + (oy + 488) + '" font-size="12" fill="#455a64" text-anchor="middle">' + v + "</text>";
    if (DI.ver){
      s += '<line x1="' + (ox + a.x) + '" y1="' + (oy + a.y) + '" x2="' + (ox + b.x) + '" y2="' + (oy + a.y) + '" stroke="' + C4.cateto + '" stroke-width="2.5" stroke-dasharray="7 5"/>';
      s += '<line x1="' + (ox + b.x) + '" y1="' + (oy + a.y) + '" x2="' + (ox + b.x) + '" y2="' + (oy + b.y) + '" stroke="' + C4.cateto + '" stroke-width="2.5" stroke-dasharray="7 5"/>';
    }
    s += '<line x1="' + (ox + a.x) + '" y1="' + (oy + a.y) + '" x2="' + (ox + b.x) + '" y2="' + (oy + b.y) + '" stroke="' + C4.tinta + '" stroke-width="3.5"/>';
    CIUDADES.forEach(function(c){
      var sel = c === a || c === b;
      s += '<circle cx="' + (ox + c.x) + '" cy="' + (oy + c.y) + '" r="' + (sel ? 7 : 4) + '" fill="' + (sel ? C4.tinta : C4.rojo) + '" stroke="#fff" stroke-width="2"/>';
      var cerca = !sel && [a, b].some(function(z){ return Math.abs(z.x - c.x) < 90 && Math.abs(z.y - c.y) < 22; });
      if (!sel && !cerca) s += '<text x="' + (ox + c.x - 7) + '" y="' + (oy + c.y + 4) + '" font-size="11" font-weight="700" fill="' + C4.rojo + '" text-anchor="end" paint-order="stroke" stroke="#fff" stroke-width="3">' + c.n + "</text>";
      if (sel) s += '<text x="' + (ox + c.x + (c.x > 300 ? -10 : 10)) + '" y="' + (oy + c.y - 10) + '" font-size="14" font-weight="700" fill="' + C4.tinta + '" text-anchor="' + (c.x > 300 ? "end" : "start") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + c.n + " " + par(c.x, c.y) + "</text>";
    });
    $("di-svg").innerHTML = s + "</svg>";
  }
}
function diPasos(dx, dy, d2, unidad){
  return "<ol><li>" + T("Differences: ", "Diferencias: ") + "Δx = " + dx + ", Δy = " + dy + ".</li><li>" + T("Squares: ", "Cuadrados: ") + dx + "² + " + dy + "² = " + (dx * dx) + " + " + (dy * dy) + " = " + d2 + ".</li><li>" + T("Square root: ", "Raíz: ") + "d = " + raizTexto(d2) + (unidad || "") + ".</li></ol>";
}
function genDistancia(){
  var a, b, dx, dy, d2, unidad = "", enun;
  if (DI.modo === "plano"){
    do {
      a = [aleatorio(-8, 8), aleatorio(-8, 8)];
      if (Math.random() < 0.5){ var tr = elige([[3, 4], [4, 3], [6, 8], [8, 6], [5, 12], [12, 5], [0, 5], [7, 0]]); b = [a[0] + (Math.random() < .5 ? -1 : 1) * tr[0], a[1] + (Math.random() < .5 ? -1 : 1) * tr[1]]; }
      else b = [aleatorio(-8, 8), aleatorio(-8, 8)];
    } while (b[0] < -8 || b[0] > 8 || b[1] < -8 || b[1] > 8 || (a[0] === b[0] && a[1] === b[1]));
    DI.a = a; DI.b = b; dx = b[0] - a[0]; dy = b[1] - a[1];
    enun = T("Find the distance between ", "Calcule la distancia entre ") + parHTML(a[0], a[1], "A") + T(" and ", " y ") + parHTML(b[0], b[1], "B") + T(". If it is not exact, round to the tenth.", ". Si no es exacta, redondee a la décima.");
  } else {
    var c1, c2; do { c1 = elige(CIUDADES); c2 = elige(CIUDADES); } while (c1 === c2 || Math.hypot(c1.x - c2.x, c1.y - c2.y) < 60);
    DI.a = c1; DI.b = c2; dx = c2.x - c1.x; dy = c2.y - c1.y; unidad = T(" grid units", " unidades de la cuadrícula");
    enun = T("How far apart, in a straight line, are ", "¿A qué distancia en línea recta están ") + c1.n + " " + par(c1.x, c1.y) + T(" and ", " y ") + c2.n + " " + par(c2.x, c2.y) + T("? Answer in grid units, rounded to the whole number.", "? Responda en unidades de la cuadrícula, redondeando al entero.");
  }
  diDibuja();
  var adx = Math.abs(dx), ady = Math.abs(dy); d2 = dx * dx + dy * dy;
  var d = Math.sqrt(d2), tol = DI.modo === "plano" ? 0.051 : 1.01;
  $("di-pasos").innerHTML = diPasos(adx, ady, d2, unidad);
  $("di-ver-pasos").open = false;
  var extra = DI.modo === "mapa" ? " " + T("At about 0.982 miles per unit, that is about ", "A unas 0.982 millas por unidad, son unas ") + Math.round(d * MILLAS) + T(" miles in a straight line (by road it is longer).", " millas en línea recta (por carretera es más).") : "";
  return {enun: enun,
    evalua: function(txt){
      var v = leeDecimal(String(txt).replace(/,/g, ES ? "." : ""));
      if (v === null) return {estado: "invalido", msg: T("Type a number, like 5 or 7.2.", "Escriba un número, como 5 o 7.2.")};
      if (Math.abs(v - d) <= tol) return {estado: "bien"};
      if (Math.abs(v - (adx + ady)) < 0.01) return {estado: "mal", msg: T("You added Δx and Δy. The distance is the hypotenuse: square them, add, and take the square root.", "Sumó Δx y Δy. La distancia es la hipotenusa: se elevan al cuadrado, se suman y se saca la raíz.")};
      if (Math.abs(v - d2) < 0.01) return {estado: "mal", msg: T("That is d² (" + d2 + "). You still need the square root.", "Ese es d² (" + d2 + "). Falta sacar la raíz.")};
      return {estado: "mal", msg: T("Find Δx and Δy first (watch the negative signs), then use d = √(Δx² + Δy²).", "Calcule primero Δx y Δy (cuidado con los signos negativos) y luego use d = √(Δx² + Δy²).")};
    },
    solucion: "d = √(" + adx + "² + " + ady + "²) = " + (DI.modo === "plano" ? raizTexto(d2, 1) : "√" + d2 + " ≈ " + Math.round(d)) + (unidad || "") + "." + extra};
}
function diModo(m){ DI.modo = m; $("di-m1").setAttribute("aria-pressed", m === "plano" ? "true" : "false"); $("di-m2").setAttribute("aria-pressed", m === "mapa" ? "true" : "false"); $("di-nota-mapa").hidden = m !== "mapa"; $("di-nuevo").click(); }
creaPracticaLibre("di", genDistancia);
$("di-m1").addEventListener("click", function(){ diModo("plano"); });
$("di-m2").addEventListener("click", function(){ diModo("mapa"); });
$("di-catetos").addEventListener("click", function(){ DI.ver = !DI.ver; $("di-catetos").textContent = DI.ver ? T("Hide the legs", "Ocultar los catetos") : T("Show the legs", "Mostrar los catetos"); diDibuja(); });

/* ===== MODULE 3 · Midpoint ===== */
var PM = {a: null, b: null};
function pmDibuja(m){
  var P = Plano({xmin: -9, xmax: 9, ymin: -9, ymax: 9, u: 28, paso: 3}), a = PM.a, b = PM.b, ver = $("pm-ver").checked;
  var s = P.seg(a, b, C4.azul, 3.5) + P.punto(a, C4.azul, "A" + (ver ? par(a[0], a[1]) : "")) + P.punto(b, C4.azul, "B" + (ver ? par(b[0], b[1]) : ""));
  if (m) s += P.punto(m, C4.rojo, "M" + par(m[0], m[1]), null, 7);
  $("pm-svg").innerHTML = P.svg(s, T("Segment from A to B on the coordinate plane", "Segmento de A a B en el plano cartesiano") + (ver ? ": A" + par(a[0], a[1]) + ", B" + par(b[0], b[1]) : T(". Read the coordinates of A and B on the grid.", ". Lea las coordenadas de A y de B en la cuadrícula.")) + (m ? T(". Midpoint M", ". Punto medio M") + par(m[0], m[1]) : "") + ".");
}
creaPracticaPar("pm", function(){
  var a, b; do { a = [aleatorio(-8, 8), aleatorio(-8, 8)]; b = [aleatorio(-8, 8), aleatorio(-8, 8)]; } while (Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]) < 4);
  if (Math.random() < 0.6){ if ((a[0] + b[0]) % 2) b[0] += b[0] < 8 ? 1 : -1; if ((a[1] + b[1]) % 2) b[1] += b[1] < 8 ? 1 : -1; }
  PM.a = a; PM.b = b; var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
  return {enun: T("Read the endpoints A and B on the graph and find the midpoint M of the segment AB.", "Lea en la gráfica los extremos A y B y calcule el punto medio M del segmento AB."), x: mx, y: my,
    despues: function(){ pmDibuja(null); },
    alFinal: function(){ pmDibuja([mx, my]); $("pm-ver").checked = true; pmDibuja([mx, my]); },
    diag: function(xu, yu){
      if (Math.abs(xu - 2 * mx) < 1e-9 && Math.abs(yu - 2 * my) < 1e-9) return T("You added the coordinates but did not divide by 2.", "Sumó las coordenadas pero no dividió entre 2.");
      if ((Math.abs(xu - Math.abs(a[0] - b[0]) / 2) < 1e-9 || Math.abs(xu - (b[0] - a[0]) / 2) < 1e-9) && Math.abs(xu - mx) > 1e-9) return T("It looks like you subtracted. For the midpoint, add the two x's and divide by 2.", "Parece que restó. Para el punto medio se suman las dos x y se divide entre 2.");
      return diagPar(xu, yu, mx, my) + " " + T("Read A and B again (you can check “Show the coordinates”), then average: (x₁ + x₂) ÷ 2 and (y₁ + y₂) ÷ 2.", "Lea otra vez A y B (puede marcar «Mostrar las coordenadas») y promedie: (x₁ + x₂) ÷ 2 y (y₁ + y₂) ÷ 2.");
    },
    solucion: "A" + par(a[0], a[1]) + ", B" + par(b[0], b[1]) + ". M = ((" + sg(a[0]) + " + " + sg(b[0]) + ") ÷ 2, (" + sg(a[1]) + " + " + sg(b[1]) + ") ÷ 2) = " + par(mx, my) + "."};
}, null);
$("pm-ver").addEventListener("change", function(){ pmDibuja(null); });

creaPracticaPar("ex", function(){
  var a = [aleatorio(-6, 6), aleatorio(-6, 6)], b; do { b = [aleatorio(-8, 8), aleatorio(-8, 8)]; } while ((a[0] + b[0]) % 2 || (a[1] + b[1]) % 2 || (a[0] === b[0] && a[1] === b[1]));
  var m = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
  return {enun: T("The midpoint of a segment is ", "El punto medio de un segmento es ") + parHTML(m[0], m[1], "M") + T(" and one endpoint is ", " y un extremo es ") + parHTML(a[0], a[1], "A") + T(". What is the other endpoint B?", ". ¿Cuál es el otro extremo B?"), x: b[0], y: b[1],
    diag: function(xu, yu){
      if (Math.abs(xu - (a[0] + m[0]) / 2) < 1e-9 && Math.abs(yu - (a[1] + m[1]) / 2) < 1e-9) return T("That is the midpoint of A and M. B is on the other side of M: B = 2·M − A.", "Ese es el punto medio entre A y M. B está del otro lado de M: B = 2·M − A.");
      if (Math.abs(xu - 2 * m[0]) < 1e-9 && Math.abs(yu - 2 * m[1]) < 1e-9) return T("You doubled M. Now subtract A from it.", "Duplicó M. Ahora réstele A.");
      return diagPar(xu, yu, b[0], b[1]) + " " + T("Solve (x₁ + x) ÷ 2 = M for x, and the same for y.", "Despeje x en (x₁ + x) ÷ 2 = M, y lo mismo para la y.");
    },
    solucion: "x = 2 · " + pn(m[0]) + " − " + (a[0] < 0 ? "(" + sg(a[0]) + ")" : a[0]) + " = " + sg(b[0]) + ", y = 2 · " + pn(m[1]) + " − " + (a[1] < 0 ? "(" + sg(a[1]) + ")" : a[1]) + " = " + sg(b[1]) + T(". Check: the midpoint of A and B is M.", ". Comprobación: el punto medio de A y B es M.")};
});

function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
/* ===== MODULE 4 · Perimeter ===== */
function figura(tipo){
  var x0 = aleatorio(-7, -1), y0 = aleatorio(-6, -1), tr, w, h, v;
  if (tipo === "rect"){ w = aleatorio(3, 9); h = aleatorio(2, 7); v = [[x0, y0], [x0 + w, y0], [x0 + w, y0 + h], [x0, y0 + h]]; }
  else if (tipo === "tri"){ tr = elige([[3, 4], [6, 8], [5, 12], [4, 3], [8, 6], [3, 5], [4, 6], [2, 7]]); v = [[x0, y0], [x0 + tr[0], y0], [x0, y0 + tr[1]]]; if (y0 + tr[1] > 8) return figura(tipo); }
  else if (tipo === "iso"){ w = 2 * aleatorio(2, 4); h = elige([3, 4, 5, 6, 8]); v = [[x0, y0], [x0 + w, y0], [x0 + w / 2, y0 + h]]; }
  else { w = aleatorio(6, 10); var s = aleatorio(1, 3), r = aleatorio(1, 3); h = elige([3, 4, 5, 6]); if (w - s - r < 2) return figura(tipo); v = [[x0, y0], [x0 + w, y0], [x0 + w - r, y0 + h], [x0 + s, y0 + h]]; }
  if (v.some(function(p){ return p[0] > 8 || p[1] > 8; })) return figura(tipo);
  return v;
}
function lados(v){
  return v.map(function(p, i){
    var q = v[(i + 1) % v.length], dx = Math.abs(q[0] - p[0]), dy = Math.abs(q[1] - p[1]), d2 = dx * dx + dy * dy;
    return {p: p, q: q, dx: dx, dy: dy, d2: d2, d: Math.sqrt(d2), recto: dx === 0 || dy === 0};
  });
}
var LETRAS = ["A", "B", "C", "D"];
function dibujaFigura(v, ls, conLong, cont){
  var P = Plano({xmin: -8, xmax: 8, ymin: -7, ymax: 8, u: 28, paso: 2}), s = P.poli(v, "rgba(13,71,161,.06)", "none", 0);
  ls.forEach(function(l, i){
    s += P.seg(l.p, l.q, l.recto ? C4.verde : "#e65100", 3.5, l.recto ? null : "");
    if (conLong){ var m = [(l.p[0] + l.q[0]) / 2, (l.p[1] + l.q[1]) / 2], cx = v.reduce(function(a, p){ return a + p[0]; }, 0) / v.length, cy = v.reduce(function(a, p){ return a + p[1]; }, 0) / v.length;
      var nx = m[0] - cx, ny = m[1] - cy, nn = Math.hypot(nx, ny) || 1; s += P.texto([m[0] + nx / nn * .7, m[1] + ny / nn * .7], l.recto ? String(l.d) : (esCuadrado(l.d2) ? String(l.d) : "√" + l.d2), l.recto ? C4.verde : "#e65100", 14); }
  });
  v.forEach(function(p, i){ s += P.punto(p, C4.tinta, LETRAS[i] + par(p[0], p[1]), (p[1] >= v.reduce(function(a, q){ return a + q[1]; }, 0) / v.length ? "n" : "s") + (p[0] >= v.reduce(function(a, q){ return a + q[0]; }, 0) / v.length ? "e" : "w")); });
  cont.innerHTML = P.svg(s, T("A figure with vertices ", "Una figura con vértices ") + v.map(function(p, i){ return LETRAS[i] + par(p[0], p[1]); }).join(", ") + ".");
}
var PR = {v: null};
function prExplora(){
  var v = figura($("pr-tipo").value), ls = lados(v), tot = ls.reduce(function(a, l){ return a + l.d; }, 0);
  dibujaFigura(v, ls, true, $("pr-svg"));
  $("pr-tabla").innerHTML = "<caption class=\"sr-only\">" + T("Each side, how it is measured, and its length", "Cada lado, cómo se mide y su longitud") + "</caption><thead><tr><th scope=\"col\">" + T("Side", "Lado") + "</th><th scope=\"col\">" + T("How", "Cómo") + "</th><th scope=\"col\">" + T("Length", "Longitud") + "</th></tr></thead><tbody>" +
    ls.map(function(l, i){ var nom = LETRAS[i] + LETRAS[(i + 1) % ls.length];
      return '<tr class="' + (l.recto ? "" : "incl") + '"><th scope="row">' + nom + "</th><td>" + (l.recto ? (l.dx === 0 ? T("vertical: subtract the y's", "vertical: se restan las y") : T("horizontal: subtract the x's", "horizontal: se restan las x")) : T("slanted: distance formula", "inclinado: fórmula de la distancia") + ", √(" + l.dx + "² + " + l.dy + "²)") + "</td><td>" + (l.recto ? l.d : raizTexto(l.d2)) + "</td></tr>"; }).join("") + "</tbody>";
  $("pr-total").innerHTML = '<div class="linea veredicto">' + T("Perimeter = ", "Perímetro = ") + ls.map(function(l){ return l.recto || esCuadrado(l.d2) ? String(l.d) : aprox(l.d, 1); }).join(" + ") + (ls.every(function(l){ return esCuadrado(l.d2); }) ? " = " + tot : " ≈ " + aprox(tot, 1)) + T(" units", " unidades") + "</div>";
}
$("pr-tipo").addEventListener("change", prExplora); $("pr-otro").addEventListener("click", prExplora); prExplora();
creaPracticaLibre("pp", function(){
  var v = figura(elige(["rect", "tri", "tri", "iso", "trap"])), ls = lados(v), tot = ls.reduce(function(a, l){ return a + l.d; }, 0), exacto = ls.every(function(l){ return esCuadrado(l.d2); });
  dibujaFigura(v, ls, false, $("pp-svg"));
  var malSuma = ls.reduce(function(a, l){ return a + l.dx + l.dy; }, 0);
  return {enun: T("Find the perimeter of the figure with vertices ", "Calcule el perímetro de la figura de vértices ") + v.map(function(p, i){ return LETRAS[i] + par(p[0], p[1]); }).join(", ") + "." + (exacto ? "" : T(" Round to the tenth.", " Redondee a la décima.")),
    evalua: function(txt){
      var x = leeDecimal(txt); if (x === null) return {estado: "invalido", msg: T("Type a number, like 24 or 18.6.", "Escriba un número, como 24 o 18.6.")};
      if (Math.abs(x - tot) <= 0.151) return {estado: "bien"};
      if (Math.abs(x - malSuma) < 0.01 && !ls.every(function(l){ return l.recto; })) return {estado: "mal", msg: T("A slanted side is not Δx + Δy: square, add, and take the square root.", "Un lado inclinado no mide Δx + Δy: se eleva al cuadrado, se suma y se saca la raíz.")};
      for (var i = 0; i < ls.length; i++) if (Math.abs(x - (tot - ls[i].d)) <= 0.151) return {estado: "mal", msg: T("It looks like a side is missing. The figure has " + ls.length + " sides.", "Parece que falta un lado. La figura tiene " + ls.length + " lados.")};
      return {estado: "mal", msg: T("Measure each side: horizontal and vertical sides by subtracting, slanted sides with the distance formula. Then add them all.", "Mida cada lado: los horizontales y verticales restando; los inclinados, con la fórmula de la distancia. Después súmelos todos.")};
    },
    solucion: ls.map(function(l, i){ return LETRAS[i] + LETRAS[(i + 1) % ls.length] + " = " + (l.recto ? l.d : raizTexto(l.d2)); }).join("; ") + ". " + T("Perimeter ", "Perímetro ") + (exacto ? "= " + tot : "≈ " + aprox(tot, 1)) + "."};
});
'''

def practica_pagina():
    n = N
    mods = [
     (t("plane", "plano"), t("The coordinate plane: ordered pairs and quadrants", "El plano cartesiano: pares ordenados y cuadrantes"),
      f'''      <p>{t("Three ways to practice. <strong>Explore</strong>: mark points freely and see their coordinates. <strong>Place the point</strong>: you get the ordered pair and mark it on the plane. <strong>Read the coordinates</strong>: you get the point and write its ordered pair. When an answer is not right, the page tells you what went wrong: the coordinates swapped, a sign, or just one of the two.",
        "Tres maneras de practicar. <strong>Explorar</strong>: marque puntos libremente y vea sus coordenadas. <strong>Ubicar el punto</strong>: se da el par ordenado y hay que marcarlo en el plano. <strong>Leer las coordenadas</strong>: se da el punto y hay que escribir su par ordenado. Si la respuesta no es correcta, la página indica en qué consistió el error: las coordenadas invertidas, un signo o solo una de las dos.")}</p>
      <div class="modos" role="group" aria-label="{t("Mode", "Modo")}"><button type="button" class="btn-sec" id="pl-m1" aria-pressed="true">1 · {t("Explore", "Explorar")}</button><button type="button" class="btn-sec" id="pl-m2" aria-pressed="false">2 · {t("Place the point", "Ubicar el punto")}</button><button type="button" class="btn-sec" id="pl-m3" aria-pressed="false">3 · {t("Read the coordinates", "Leer las coordenadas")}</button></div>
      <p class="enun" id="pl-enun"></p>
      <div id="pl-plano"></div>
      <div id="pl-leer" hidden><div class="par-campos" role="group" aria-label="{t("Coordinates of P", "Coordenadas de P")}"><span class="pa" aria-hidden="true">P(</span><div class="campo"><label for="pl-x">x</label><input type="text" inputmode="decimal" autocomplete="off" id="pl-x"></div><span class="pa" aria-hidden="true">,</span><div class="campo"><label for="pl-y">y</label><input type="text" inputmode="decimal" autocomplete="off" id="pl-y"></div><span class="pa" aria-hidden="true">)</span></div>
        <div class="fila-btn"><button type="button" class="btn" id="pl-comprobar">{t("Check", "Comprobar")}</button></div></div>
{n4.salida("pl-info")}
      <div class="fb" id="pl-fb" role="status"></div>
      <div class="fila-btn"><button type="button" class="btn-sec" id="pl-otro" hidden>{t("New exercise", "Otro ejercicio")}</button></div>
      <p class="marcador" id="pl-marcador"></p>
      <p class="nota">{t("With the keyboard: Tab takes you to the plane; the arrows move the cursor one unit (with Shift, five units); Enter or the space bar marks the point; Home takes the cursor back to the origin.", "Con el teclado: la tecla Tab lleva al plano; las flechas mueven el cursor una unidad (con Mayús, cinco); Enter o la barra espaciadora marcan el punto; la tecla Inicio (Home) devuelve el cursor al origen.")}</p>
      <div class="caja-tip">{t("The order matters: (3, 2) is not the same point as (2, 3). The first coordinate is always the move across from the origin, and the second, the move up or down. A common mistake is to count up first.", "El orden importa: (3, 2) no es el mismo punto que (2, 3). La primera coordenada siempre indica cuánto se avanza horizontalmente desde el origen, y la segunda, cuánto se sube o se baja. Un error frecuente es contar primero hacia arriba.")}</div>
{B.om("cu", t("Practice: quadrant or axis?", "Practique: ¿cuadrante o eje?"))}'''),
     (t("distance", "distancia"), t("The distance between two points", "La distancia entre dos puntos"),
      f'''{n4.formula("d = √[(x₂ − x₁)² + (y₂ − y₁)²]")}
      <p>{t("The segment that joins the two points is always the hypotenuse of a right triangle whose legs are the horizontal difference (Δx) and the vertical difference (Δy). That is why there is no new formula to memorize: it is the same Pythagorean theorem. Practice on the plane, then measure real distances between cities in Illinois.", "El segmento que une los dos puntos es siempre la hipotenusa de un triángulo rectángulo cuyos catetos son la diferencia horizontal (Δx) y la vertical (Δy). Por eso no hay una fórmula nueva que memorizar: es el teorema de Pitágoras de siempre. Practique en el plano y después mida distancias reales entre ciudades de Illinois.")}</p>
      <div class="modos" role="group" aria-label="{t("Where to practice", "Dónde practicar")}"><button type="button" class="btn-sec" id="di-m1" aria-pressed="true">1 · {t("On the coordinate plane", "En el plano cartesiano")}</button><button type="button" class="btn-sec" id="di-m2" aria-pressed="false">2 · {t("On the map of Illinois", "En el mapa de Illinois")}</button><button type="button" class="btn-sec" id="di-catetos">{t("Hide the legs", "Ocultar los catetos")}</button></div>
      <div id="di-svg"></div>
      <p class="nota" id="di-nota-mapa" hidden>{t("On this map grid, y is measured from the top edge down, the opposite of the coordinate plane. That does not change the calculation: the differences are squared, so the sign disappears. The scale is about 0.982 miles per unit, and the result is the straight-line distance, not the distance by road.", "En esta cuadrícula la coordenada y se mide desde el borde superior hacia abajo, al revés que en el plano cartesiano. Esto no cambia el cálculo: como las diferencias se elevan al cuadrado, el signo desaparece. La escala es de unas 0.982 millas por unidad, y el resultado es la distancia en línea recta, no por carretera.")}</p>
{B.libre("di", t("Practice: find the distance", "Practique: calcule la distancia"), t("Distance", "Distancia"), nota=False)}
      <details class="pasos-det" id="di-ver-pasos"><summary>{t("See the procedure step by step", "Ver el procedimiento paso a paso")}</summary><div id="di-pasos"></div></details>'''),
     (t("midpoint", "punto-medio"), t("The midpoint of a segment", "El punto medio de un segmento"),
      f'''{n4.formula("M = ( (x₁ + x₂) ÷ 2 , (y₁ + y₂) ÷ 2 )")}
      <p>{t("The midpoint is not a formula to memorize: it is the average of the two endpoints. Add the two x's and divide by 2; do the same with the two y's. That is why the result always lands halfway. Read the endpoints on the graph (or check the box to see them), and find M. When you finish, M appears on the segment.", "El punto medio no es una fórmula que memorizar: es el promedio de los dos extremos. Se suman las dos x y se divide entre 2; lo mismo con las dos y. Por eso el resultado siempre queda a mitad de camino. Lea los extremos en la gráfica (o marque la casilla para verlos) y calcule M. Al terminar, M aparece sobre el segmento.")}</p>
      <div class="campo"><label><input type="checkbox" id="pm-ver"> {t("Show the coordinates of A and B", "Mostrar las coordenadas de A y de B")}</label></div>
      <div id="pm-svg"></div>
{n4.par_libre("pm", t("Practice: find the midpoint", "Practique: calcule el punto medio"), "M", t("You can use a decimal point: if a sum is odd, the result ends in .5.", "Puede usar el punto decimal: si una suma es impar, el resultado termina en .5."))}
      <div class="caja-tip">{t("Two common slips: adding and forgetting to divide by 2 (the point lands twice as far), and subtracting instead of adding (the difference is for the distance, not for the midpoint).", "Dos descuidos frecuentes: sumar y olvidar la división entre 2 (el punto sale al doble de distancia) y restar en lugar de sumar (la diferencia sirve para la distancia, no para el punto medio).")}</div>
{n4.par_libre("ex", t("Practice: find the missing endpoint", "Practique: halle el extremo que falta"), "B")}'''),
     (t("perimeter", "perimetro"), t("Figures on the plane: the perimeter", "Figuras en el plano: el perímetro"),
      f'''      <p>{t("When the vertices of a figure are points on the plane, measure each side and add them. Choose a figure, ask for new coordinates, and see how each side is measured.", "Cuando los vértices de una figura son puntos del plano, se mide cada lado y se suman. Elija una figura, pida nuevas coordenadas y observe cómo se mide cada lado.")}</p>
      <div class="panel"><div class="campos">{n4.lista("pr-tipo", t("Figure", "Figura"), [("tri", t("Right triangle", "Triángulo rectángulo")), ("rect", t("Rectangle", "Rectángulo")), ("iso", t("Isosceles triangle", "Triángulo isósceles")), ("trap", t("Trapezoid", "Trapecio"))])}
        <div class="fila-btn" style="align-self:flex-end;"><button type="button" class="btn-sec" id="pr-otro">{t("New coordinates", "Nuevas coordenadas")}</button></div></div></div>
      <div class="leyenda-geo" aria-hidden="true"><span><svg width="26" height="10"><line x1="1" y1="5" x2="25" y2="5" stroke="#1b5e20" stroke-width="3.5"/></svg>{t("Horizontal or vertical side (subtract)", "Lado horizontal o vertical (se resta)")}</span><span><svg width="26" height="10"><line x1="1" y1="5" x2="25" y2="5" stroke="#e65100" stroke-width="3.5"/></svg>{t("Slanted side (distance formula)", "Lado inclinado (fórmula de la distancia)")}</span></div>
      <div id="pr-svg"></div>
      <div class="tabla-scroll"><table class="tabla-lados" id="pr-tabla"></table></div>
{n4.salida("pr-total")}
      <div class="caja-atencion"><strong>{t("Watch the signs.", "Cuidado con los signos.")}</strong> {t("From x = −3 to x = 5 there are 5 − (−3) = 8 units, not 5 − 3 = 2. And a slanted side is not Δx + Δy: square, add, and take the square root.", "De x = −3 a x = 5 hay 5 − (−3) = 8 unidades, no 5 − 3 = 2. Y un lado inclinado no mide Δx + Δy: hay que elevar al cuadrado, sumar y sacar la raíz.")}</div>
{B.libre("pp", t("Practice: find the perimeter", "Practique: calcule el perímetro"), t("Perimeter", "Perímetro"), nota=False).replace('<div class="enun" id="pp-enun"></div>', '<div class="enun" id="pp-enun"></div><div id="pp-svg"></div>')}''')]
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "El plano cartesiano: pares ordenados, distancia y punto medio")
