"""Level 4 · Lesson 8.1 · Quadratic functions: the parabola, the vertex, and the intercepts — builds the lesson and its practice page in
English and in Spanish. Sources (GEDparaHispanos): clase_mate4/leccion_8-1.html and algebra/n4-l8-1.html (the coefficients a, b, and c,
the vertex and the axis of symmetry step by step, the intercepts with the discriminant, and four maximum and minimum problems).
They are rebuilt here, inside LearnGED, with math/func4.js and math/poly4.js; all units are U.S. customary.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n4

B.NIVEL = 4
N = "8-1"
TEMA = ("Modeling with functions and a practice GED test", "Modelado de funciones y simulacro GED")
TIT = ("Quadratic functions: the parabola, the vertex, and the intercepts", "Funciones cuadráticas: la parábola, el vértice y los interceptos")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js", "/math/func4.js")
ESTILO = n4.ESTILO + """
  .tabla-lados.centro td,.tabla-lados.centro th{text-align:center;}
"""

def parabola(p, f, x0, x1, color="#1565c0"):
    pts = [(x0 + (x1 - x0) * i / 80, f(x0 + (x1 - x0) * i / 80)) for i in range(81)]
    for a, b in zip(pts, pts[1:]):
        p.seg(a, b, color, 3.5)

def fig_vertice():
    p = n4.Plano(-2, 6, -2, 6, 32, paso=1)
    f = lambda x: x * x - 4 * x + 3
    p.seg((2, -2), (2, 6), "#6a1b9a", 2.5, "8 6")
    parabola(p, f, -0.6, 4.6)
    p.punto((2, -1), "#c62828", t("vertex (2, −1)", "vértice (2, −1)"), "se").punto((1, 0), "#2e7d32").punto((3, 0), "#2e7d32").punto((0, 3), "#ef6c00", "(0, 3)", "ne")
    p.texto((1, 0), "(1, 0)", "#2e7d32", 13, "end", -8, -12).texto((3, 0), "(3, 0)", "#2e7d32", 13, "start", 8, -12)
    p.texto((2, 5.4), t("axis x = 2", "eje x = 2"), "#6a1b9a", 14, "start", 8, 0)
    return p.svg(t("The parabola f of x = x squared minus 4x plus 3. It opens up. Its vertex, the lowest point, is 2, negative 1, and the dashed axis of symmetry is the vertical line x = 2. It crosses the x-axis at 1, 0 and 3, 0, and the y-axis at 0, 3.",
                   "La parábola f de x = x al cuadrado menos 4x más 3. Abre hacia arriba. Su vértice, el punto más bajo, es 2, −1, y el eje de simetría punteado es la recta vertical x = 2. Cruza el eje x en 1, 0 y 3, 0, y el eje y en 0, 3."), 330)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Topic 7.</strong> In Topic 7 you classified quadratic functions by their pattern. Now you study them in depth: their graph (the <strong>parabola</strong>), their most important point (the <strong>vertex</strong>), and how they model maximum and minimum situations, such as the height of a ball or the profit of a business.", "<strong>Conexión con el tema anterior.</strong> En el Tema 7 se clasificaron las funciones cuadráticas por su patrón. Ahora se estudian a fondo: su gráfica (la <strong>parábola</strong>), su punto más importante (el <strong>vértice</strong>) y cómo modelan situaciones de máximo o mínimo, como la altura de un proyectil o el beneficio de un negocio.")}</p>
<p>{t("The graph of a quadratic function f(x) = ax² + bx + c is a parabola. The sign of a decides which way it opens:", "La gráfica de una función cuadrática f(x) = ax² + bx + c es una parábola. El signo de a decide hacia dónde abre:")}</p>
{tabla(t("Which way the parabola opens", "Hacia dónde abre la parábola"), t("How the sign of a decides the way the parabola opens", "Dirección de apertura de la parábola según el signo de a"), [t("If…", "Si…"), t("The parabola…", "La parábola…"), t("The vertex is…", "El vértice es…")],
  [["a &gt; 0", t("opens up", "abre hacia arriba"), t("a minimum", "un mínimo")], ["a &lt; 0", t("opens down", "abre hacia abajo"), t("a maximum", "un máximo")]])}
{caja("tip", t("Wide or narrow", "Ancha o estrecha"), t("<p>The larger |a| is, the narrower the parabola. The number c is where it crosses the y-axis, and b moves the vertex to the side.</p>", "<p>Cuanto mayor es |a|, más cerrada es la parábola. El número c es donde cruza el eje y, y b desplaza el vértice hacia un lado.</p>"))}
{practica("p1", t("Practice 1 — Which way?", "Práctica 1 — ¿Hacia dónde?"), t("f(x) = 2x² − 5x + 1 opens:", "f(x) = 2x² − 5x + 1 abre hacia:"), [("a", t("up", "arriba")), ("b", t("down", "abajo"))])}
{practica("p2", t("Practice 2 — A negative a", "Práctica 2 — Una a negativa"), t("f(x) = −x² + 3x opens:", "f(x) = −x² + 3x abre hacia:"), [("a", t("up", "arriba")), ("b", t("down", "abajo"))])}
{practica("p3", t("Practice 3 — The vertex", "Práctica 3 — El vértice"), t("A parabola that opens up has:", "Una parábola que abre hacia arriba tiene:"), [("a", t("a minimum", "un mínimo")), ("b", t("a maximum", "un máximo"))])}
{enlace(n, t("parabola", "parabola"), t("the shape of the parabola", "la forma de la parábola"), t("Sliders for a, b, and c that open, close, and move the parabola, with its vertex and its y-intercept.", "Deslizadores de a, b y c que abren, cierran y desplazan la parábola, con su vértice y su intercepto con el eje y."))}'''

    s2 = f'''<p>{t("The <strong>vertex</strong> is the highest or lowest point of the parabola. You find its x-coordinate with the formula, and its y-coordinate by evaluating the function. The <strong>axis of symmetry</strong> is the vertical line through the vertex.", "El <strong>vértice</strong> es el punto más alto o más bajo de la parábola. Su coordenada x se halla con la fórmula, y la y se obtiene evaluando la función. El <strong>eje de simetría</strong> es la recta vertical que pasa por el vértice.")}</p>
{n4.formula(t("x of the vertex = −b / (2a) · axis of symmetry: x = −b / (2a)", "x del vértice = −b / (2a) · eje de simetría: x = −b / (2a)"))}
{fig_vertice()}
{ejemplo(t("Example 1: find the vertex and the axis of f(x) = x² − 4x + 3.", "Ejemplo 1 · Hallar el vértice y el eje de f(x) = x² − 4x + 3."),
  [("1", t("Here a = 1 and b = −4.", "Aquí a = 1 y b = −4."), t("x of the vertex: −(−4) / (2 · 1) = 4/2 = 2.", "x del vértice: −(−4) / (2 · 1) = 4/2 = 2.")), ("2", t("The y of the vertex:", "La y del vértice:"), "f(2) = (2)² − 4(2) + 3 = 4 − 8 + 3 = −1."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Vertex (2, −1); axis of symmetry x = 2; since a &gt; 0, it is a minimum.</strong>", "<strong>Vértice (2, −1); eje de simetría x = 2; como a &gt; 0, es un mínimo.</strong>"))])}
{practica("p4", t("Practice 4 — The x of the vertex", "Práctica 4 — La x del vértice"), t("f(x) = x² − 6x + 5. What is the x of the vertex?", "f(x) = x² − 6x + 5. ¿x del vértice?"), [("a", "3"), ("b", "−3"), ("c", "6")])}
{practica("p5", t("Practice 5 — The whole vertex", "Práctica 5 — El vértice completo"), t("f(x) = x² − 4x + 3. The whole vertex is:", "f(x) = x² − 4x + 3. El vértice completo es:"), [("a", "(−2, −1)"), ("b", "(2, 1)"), ("c", "(2, −1)")])}
{practica("p6", t("Practice 6 — The axis", "Práctica 6 — El eje"), t("The axis of symmetry of f(x) = x² − 6x + 5 is:", "El eje de simetría de f(x) = x² − 6x + 5 es:"), [("a", "y = 3"), ("b", "x = 3"), ("c", "x = −3")])}
{enlace(n, t("vertex", "vertice"), t("the vertex and the axis of symmetry", "el vértice y el eje de simetría"), t("Functions solved step by step with −b/(2a), the axis drawn, and two symmetric points that show why it is called the axis of symmetry.", "Funciones resueltas paso a paso con −b/(2a), el eje dibujado y dos puntos simétricos que muestran por qué se llama eje de simetría."))}'''

    s3 = f'''<p>{t("The intercepts are where the parabola crosses the axes:", "Los interceptos son donde la parábola cruza los ejes:")}</p>
{tabla(t("The intercepts", "Los interceptos"), t("How to find the intercepts of a parabola", "Cómo encontrar los interceptos de una parábola"), [t("Intercept", "Intercepto"), t("How to find it", "Cómo se halla")],
  [[t("With the y-axis", "Con el eje y"), t("Evaluate f(0) = c. It gives the point (0, c).", "Evaluar f(0) = c. Da el punto (0, c).")], [t("With the x-axis", "Con el eje x"), t("Solve ax² + bx + c = 0 (by factoring or with the quadratic formula of Topic 4).", "Resolver ax² + bx + c = 0 (factorizando o con la fórmula cuadrática del Tema 4).")]])}
{ejemplo(t("Example 2: the intercepts of f(x) = x² − 4x + 3.", "Ejemplo 2 · Interceptos de f(x) = x² − 4x + 3."),
  [("1", t("With y:", "Con y:"), t("f(0) = 3, so (0, 3).", "f(0) = 3, así que (0, 3).")), ("2", t("With x:", "Con x:"), t("x² − 4x + 3 = 0 → (x − 1)(x − 3) = 0 → x = 1 and x = 3, so (1, 0) and (3, 0).", "x² − 4x + 3 = 0 → (x − 1)(x − 3) = 0 → x = 1 y x = 3, así que (1, 0) y (3, 0)."))])}
{caja("tip", t("A link with Topic 4", "Conexión con el Tema 4"), t("<p>Finding the x-intercepts of a parabola is exactly solving a quadratic equation. The discriminant b² − 4ac tells you how many there are: positive, two; zero, one (the vertex touches the axis); negative, none.</p>", "<p>Hallar los interceptos con el eje x de una parábola es exactamente resolver una ecuación cuadrática. El discriminante b² − 4ac dice cuántos hay: positivo, dos; cero, uno (el vértice toca el eje); negativo, ninguno.</p>"))}
{practica("p7", t("Practice 7 — The y-intercept", "Práctica 7 — El intercepto con y"), t("The y-intercept of f(x) = x² − 4x + 3 is:", "El intercepto con el eje y de f(x) = x² − 4x + 3 es:"), [("a", "(3, 0)"), ("b", "(0, −3)"), ("c", "(0, 3)")])}
{practica("p8", t("Practice 8 — The x-intercepts", "Práctica 8 — Los interceptos con x"), t("The x-intercepts of f(x) = (x − 1)(x − 3) are:", "Los interceptos con el eje x de f(x) = (x − 1)(x − 3) son:"), [("a", t("x = −1 and x = −3", "x = −1 y x = −3")), ("b", t("x = 1 and x = 3", "x = 1 y x = 3")), ("c", t("x = 0 and x = 3", "x = 0 y x = 3"))])}
{practica("p9", t("Practice 9 — How to find it", "Práctica 9 — Cómo se halla"), t("You find the y-intercept by evaluating:", "El intercepto con el eje y se halla evaluando:"), [("a", "f(0)"), ("b", "f(1)"), ("c", "x = y")])}
{enlace(n, t("intercepts", "interceptos"), t("the intercepts", "los interceptos"), t("The intercepts found step by step, with the discriminant deciding whether there are two, one, or no x-intercepts.", "Los interceptos hallados paso a paso, con el discriminante decidiendo si hay dos, uno o ninguno con el eje x."))}'''

    s4 = f'''<p>{t("The vertex solves real problems: the greatest height of a ball, the greatest profit of a business, the greatest area of a yard. If the parabola opens down, the vertex is the maximum; if it opens up, it is the minimum.", "El vértice resuelve problemas reales: la altura máxima de un proyectil, el beneficio máximo de un negocio, el área máxima de un terreno. Si la parábola abre hacia abajo, el vértice es el máximo; si abre hacia arriba, es el mínimo.")}</p>
{ejemplo(t("Example 3 (a ball): its height is h(t) = −16t² + 64t + 5 feet (t in seconds). When does it reach its greatest height, and what is it?", "Ejemplo 3 · El proyectil. La altura es h(t) = −16t² + 64t + 5 pies (t en segundos). ¿Cuándo alcanza la altura máxima y cuál es?"),
  [("1", t("Since a = −16 &lt; 0,", "Como a = −16 &lt; 0,"), t("it opens down: the vertex is a maximum.", "abre hacia abajo: el vértice es un máximo.")), ("2", t("t of the vertex:", "t del vértice:"), t("−64 / (2 · −16) = −64 / −32 = 2 seconds.", "−64 / (2 · −16) = −64 / −32 = 2 segundos.")),
   ("✓", t("Greatest height:", "Altura máxima:"), t("<strong>h(2) = −16(4) + 64(2) + 5 = −64 + 128 + 5 = 69 feet.</strong>", "<strong>h(2) = −16(4) + 64(2) + 5 = −64 + 128 + 5 = 69 pies.</strong>"))])}
{ejemplo(t("Example 4 (profit): the profit is P(x) = −2x² + 120x − 800 dollars. How many units give the greatest profit?", "Ejemplo 4 · El beneficio. El beneficio es B(x) = −2x² + 120x − 800 dólares. ¿Cuántas unidades lo maximizan?"),
  [("1", t("x of the vertex:", "x del vértice:"), t("−120 / (2 · −2) = −120 / −4 = 30 units.", "−120 / (2 · −2) = −120 / −4 = 30 unidades.")), ("✓", t("Greatest profit:", "Beneficio máximo:"), t("<strong>P(30) = −2(900) + 120(30) − 800 = −1,800 + 3,600 − 800 = $1,000.</strong>", "<strong>B(30) = −2(900) + 120(30) − 800 = −1,800 + 3,600 − 800 = $1,000.</strong>"))])}
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. The calculator on this page does the same operations, although some keys have other names or are in other places. Use it to evaluate the function at the vertex, with parentheses around negative numbers.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. La calculadora de esta página hace las mismas operaciones, aunque algunas teclas tienen otro nombre o están en otro lugar. Úsela para evaluar la función en el vértice, con paréntesis alrededor de los números negativos.</p>"))}
{practica("p10", t("Practice 10 — Maximum or minimum", "Práctica 10 — Máximo o mínimo"), t("In h(t) = −16t² + 64t + 5, the vertex is a:", "En h(t) = −16t² + 64t + 5, el vértice es un:"), [("a", t("maximum", "máximo")), ("b", t("minimum", "mínimo"))])}
{practica("p11", t("Practice 11 — When?", "Práctica 11 — ¿Cuándo?"), t("The greatest height of h(t) = −16t² + 64t + 5 happens at t =", "La altura máxima de h(t) = −16t² + 64t + 5 ocurre en t ="), [("a", "4 s"), ("b", "2 s"), ("c", "64 s")])}
{practica("p12", t("Practice 12 — The profit", "Práctica 12 — El beneficio"), t("P(x) = −2x² + 120x − 800 is greatest at x =", "B(x) = −2x² + 120x − 800 se maximiza en x ="), [("a", "60"), ("b", "120"), ("c", "30")])}
{enlace(n, t("maximum", "maximo"), t("maximum and minimum", "el máximo y el mínimo"), t("Four situations (a ball, a fenced yard, income, and cost) with the vertex marked and a slider to check that no other value beats it.", "Cuatro situaciones (proyectil, jardín cercado, ingreso y costo) con el vértice marcado y un deslizador para comprobar que ningún otro valor lo supera."))}'''

    secciones = [("s-" + t("parabola", "parabola"), t("The parabola and its shape", "La parábola y su forma"), s1),
                 ("s-" + t("vertex", "vertice"), t("The vertex and the axis of symmetry", "El vértice y el eje de simetría"), s2),
                 ("s-" + t("intercepts", "interceptos"), t("The intercepts with the axes", "Los interceptos con los ejes"), s3),
                 ("s-" + t("maximum", "maximo"), t("Maximum and minimum in context", "Máximo y mínimo en contexto"), s4)]

    dos = lambda ok, mal, right, sol: {"ok": ok, "hints": {k: v for k, v in mal.items()}, "right": right, "solution": sol}
    lesson = {"next": t("Lesson 8.2", "Lección 8.2"), "review": t("sections 2 and 4", "las secciones 2 y 4"),
     "practice": {
      "p1": dos("a", {"b": t("a = 2 is positive.", "a = 2 es positivo.")}, t("a &gt; 0: it opens up.", "a &gt; 0: abre hacia arriba."), t("Up.", "Arriba.")),
      "p2": dos("b", {"a": t("a = −1 is negative.", "a = −1 es negativo.")}, t("a &lt; 0: it opens down.", "a &lt; 0: abre hacia abajo."), t("Down.", "Abajo.")),
      "p3": dos("a", {"b": t("Opening up, the vertex is the lowest point.", "Si abre hacia arriba, el vértice es el punto más bajo.")}, t("The vertex is the lowest point.", "El vértice es el punto más bajo."), t("A minimum.", "Un mínimo.")),
      "p4": dos("a", {"b": t("−b = −(−6) = 6, positive.", "−b = −(−6) = 6, positivo."), "c": t("Divide by 2a = 2.", "Divida entre 2a = 2.")}, "6 / 2 = 3.", "3."),
      "p5": dos("c", {"a": t("x = −(−4)/2 = 2, positive.", "x = −(−4)/2 = 2, positivo."), "b": t("f(2) = 4 − 8 + 3 = −1.", "f(2) = 4 − 8 + 3 = −1.")}, "x = 2; f(2) = −1.", "(2, −1)."),
      "p6": dos("b", {"a": t("The axis is vertical: x = …", "El eje es vertical: x = …"), "c": t("x = −(−6)/2 = 3.", "x = −(−6)/2 = 3.")}, t("A vertical line through the vertex.", "Una recta vertical por el vértice."), "x = 3."),
      "p7": dos("c", {"a": t("On the y-axis, x = 0: (0, …).", "En el eje y, x = 0: (0, …)."), "b": t("f(0) = c = 3, positive.", "f(0) = c = 3, positivo.")}, "f(0) = 3.", "(0, 3)."),
      "p8": dos("b", {"a": t("x − 1 = 0 gives x = 1, not −1.", "x − 1 = 0 da x = 1, no −1."), "c": t("Set each factor equal to 0.", "Iguale cada factor a 0.")}, t("Each factor equal to zero.", "Cada factor igual a cero."), t("x = 1 and x = 3.", "x = 1 y x = 3.")),
      "p9": dos("a", {"b": t("On the y-axis, x is 0.", "En el eje y, x vale 0."), "c": t("Substitute x = 0.", "Sustituya x = 0.")}, t("On the y-axis, x = 0.", "En el eje y, x = 0."), "f(0)."),
      "p10": dos("a", {"b": t("a = −16 is negative: it opens down.", "a = −16 es negativo: abre hacia abajo.")}, t("It opens down: maximum.", "Abre hacia abajo: máximo."), t("A maximum.", "Un máximo.")),
      "p11": dos("b", {"a": t("At 4 s the ball is back near where it started. Use t = −b/(2a).", "A los 4 s la pelota vuelve cerca de donde salió. Use t = −b/(2a)."), "c": t("64 is b; divide −b by 2a.", "64 es b; divida −b entre 2a.")}, "−64 / (−32) = 2.", "2 s."),
      "p12": dos("c", {"a": t("Divide −120 by 2a = −4.", "Divida −120 entre 2a = −4."), "b": t("120 is b; divide −b by 2a.", "120 es b; divida −b entre 2a.")}, "−120 / (−4) = 30.", "30."),
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("−b/(2a) = 6/2.", "−b/(2a) = 6/2."), "b": t("−(−6) is positive.", "−(−6) es positivo."), "d": t("5 is c.", "5 es c.")}, "solution": "x = 3."},
      "B": {"ok": "d", "hints": {"a": t("x = 3, positive.", "x = 3, positivo."), "b": t("f(3) = 9 − 18 + 5 = −4.", "f(3) = 9 − 18 + 5 = −4."), "c": t("Use x = −b/(2a), not b and c.", "Use x = −b/(2a), no b y c.")}, "solution": "(3, −4)."},
      "C": {"ok": "a", "hints": {"b": t("The axis is a vertical line: x = …", "El eje es una recta vertical: x = …"), "c": t("−(−8) = 8, positive.", "−(−8) = 8, positivo."), "d": t("Divide 8 by 2a = 4.", "Divida 8 entre 2a = 4.")}, "solution": "x = 2."},
      "D": {"ok": "b", "hints": {"a": t("a = −3 is negative.", "a = −3 es negativo."), "c": t("A function's parabola opens up or down.", "La parábola de una función abre hacia arriba o hacia abajo."), "d": t("A function's parabola opens up or down.", "La parábola de una función abre hacia arriba o hacia abajo.")}, "solution": t("Down.", "Abajo.")},
      "E": {"ok": "d", "hints": {"a": t("a &gt; 0 opens up.", "a &gt; 0 abre hacia arriba."), "b": t("The vertex is always a maximum or a minimum.", "El vértice siempre es máximo o mínimo."), "c": t("A parabola has one vertex.", "Una parábola tiene un solo vértice.")}, "solution": t("A minimum.", "Un mínimo.")},
      "F": {"ok": "a", "hints": {"b": t("On the y-axis, x = 0: (0, …).", "En el eje y, x = 0: (0, …)."), "c": t("f(0) = −6, negative.", "f(0) = −6, negativo."), "d": t("x must be 0.", "x debe ser 0.")}, "solution": "(0, −6)."},
      "G": {"ok": "b", "hints": {"a": t("At 6 s the ball is back on the ground.", "A los 6 s el objeto vuelve al suelo."), "c": t("96 is b.", "96 es b."), "d": t("16 is |a|.", "16 es |a|.")}, "solution": "−96 / (−32) = 3 s."},
      "H": {"ok": "c", "hints": {"a": t("Evaluate h(3) = −16(9) + 96(3).", "Evalúe h(3) = −16(9) + 96(3)."), "b": t("96 is b, not the height.", "96 es b, no la altura."), "d": t("h(3) = −144 + 288.", "h(3) = −144 + 288.")}, "solution": t("h(3) = 144 feet.", "h(3) = 144 pies.")},
     }}

    quiz = [
     ("A", t("f(x) = x² − 6x + 5. What is the x of the vertex?", "f(x) = x² − 6x + 5. ¿Cuál es la x del vértice?"), [("a", "6"), ("b", "−3"), ("c", "3"), ("d", "5")]),
     ("B", t("f(x) = x² − 6x + 5. What is the whole vertex?", "f(x) = x² − 6x + 5. ¿Cuál es el vértice completo?"), [("a", "(−3, −4)"), ("b", "(3, 4)"), ("c", "(6, 5)"), ("d", "(3, −4)")]),
     ("C", t("The axis of symmetry of f(x) = 2x² − 8x + 1 is:", "El eje de simetría de f(x) = 2x² − 8x + 1 es:"), [("a", "x = 2"), ("b", "y = 2"), ("c", "x = −2"), ("d", "x = 4")]),
     ("D", t("f(x) = −3x² + x − 2 opens:", "f(x) = −3x² + x − 2 abre hacia:"), [("a", t("up", "arriba")), ("b", t("down", "abajo")), ("c", t("to the right", "la derecha")), ("d", t("to the left", "la izquierda"))]),
     ("E", t("A parabola with a &gt; 0 has a:", "Una parábola con a &gt; 0 tiene un:"), [("a", t("maximum", "máximo")), ("b", t("neither a maximum nor a minimum", "ni máximo ni mínimo")), ("c", t("two vertices", "dos vértices")), ("d", t("minimum", "mínimo"))]),
     ("F", t("The y-intercept of f(x) = x² + 2x − 6 is:", "El intercepto con el eje y de f(x) = x² + 2x − 6 es:"), [("a", "(0, −6)"), ("b", "(−6, 0)"), ("c", "(0, 6)"), ("d", "(2, −6)")]),
     ("G", t("A ball: h(t) = −16t² + 96t. At what time does it reach its greatest height?", "Proyectil h(t) = −16t² + 96t. ¿En qué tiempo alcanza la altura máxima?"), [("a", "6 s"), ("b", "3 s"), ("c", "96 s"), ("d", "16 s")]),
     ("H", t("With h(t) = −16t² + 96t, the greatest height is:", "Con h(t) = −16t² + 96t, la altura máxima es:"), [("a", t("288 ft", "288 pies")), ("b", t("96 ft", "96 pies")), ("c", t("144 ft", "144 pies")), ("d", t("48 ft", "48 pies"))])]

    tarea = (t("For your own work, with your notebook, graph paper, the calculator, and the GED formula sheet: (1) The ball and the profit: the height of a ball is h(t) = −16t² + 64t + 5 (in feet, with t in seconds). Graph it, find the greatest height with the vertex, and find when it hits the ground. Then find how many units x give the greatest profit P(x) = −2x² + 120x − 800 and what that profit is. (2) The four features: make a table with the direction of opening, the vertex, the axis of symmetry, and the intercepts of y = x² − 4x + 3, y = −x² + 6x − 5, y = 2x² + 8x, and y = x² + 2x + 5. One of them has no x-intercepts; explain how you know. (3) From the vertex to the answer: you have 40 feet of fence for a rectangular garden. Write the area as a function of the width, find the vertex, and say which measurements give the greatest area. Do it again if one side of the garden is against a wall and needs no fence. Then do several exercises of each activity on the practice page. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, papel cuadriculado, la calculadora y la hoja de fórmulas del GED: (1) El proyectil y el beneficio: la altura de una pelota es h(t) = −16t² + 64t + 5 (en pies, con t en segundos). Grafíquela, halle la altura máxima con el vértice y calcule cuándo toca el suelo. Después, halle cuántas unidades x maximizan el beneficio B(x) = −2x² + 120x − 800 y cuál es ese beneficio máximo. (2) Las cuatro características: haga una tabla con la dirección de apertura, el vértice, el eje de simetría y los interceptos de y = x² − 4x + 3, y = −x² + 6x − 5, y = 2x² + 8x e y = x² + 2x + 5. En una de ellas no hay interceptos con el eje x; explique cómo lo sabe. (3) Del vértice a la respuesta: con 40 pies de cerca se quiere cercar un jardín rectangular. Plantee el área como función del ancho, halle el vértice y diga qué medidas dan el área máxima. Repita el problema si un lado del jardín queda contra una pared y no necesita cerca. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Throw a ball straight up and count the seconds until it comes back down. Use h(t) = −16t² + vt with that time to estimate how fast you threw it and how high it went.",
               "Lance una pelota hacia arriba y cuente los segundos hasta que vuelve a caer. Use h(t) = −16t² + vt con ese tiempo para estimar con qué rapidez la lanzó y qué altura alcanzó."))

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Read the shape of a parabola, find its vertex, its axis, and its intercepts, and use the vertex to solve maximum and minimum problems.", "Lea la forma de una parábola, halle su vértice, su eje y sus interceptos, y use el vértice para resolver problemas de máximo y mínimo."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Tell</strong> which way a parabola opens from the sign of a.", "<strong>Identificar</strong> hacia dónde abre una parábola según el signo de a."),
         t("<strong>Find</strong> the vertex with x = −b/(2a) and the axis of symmetry.", "<strong>Calcular</strong> el vértice con x = −b/(2a) y el eje de simetría."),
         t("<strong>Find</strong> the intercepts with the x-axis and the y-axis.", "<strong>Encontrar</strong> los interceptos con el eje x y con el eje y."),
         t("<strong>Use</strong> the vertex to solve maximum and minimum problems in context.", "<strong>Usar</strong> el vértice para resolver problemas de máximo y mínimo en contexto.")],
        secciones, tarea, quiz,
        t("Self-check checklist for quadratic functions", "Lista de autoevaluación de las funciones cuadráticas"),
        t("Self-check checklist: skills for the parabola, the vertex, and the intercepts", "Lista de autoevaluación: destrezas de la parábola, el vértice y los interceptos"),
        [(t("Finding the vertex", "Calcular el vértice"), t("I find the whole vertex (x and y) and check it with symmetry.", "Calculo el vértice completo (x e y) y lo verifico con la simetría."), t("I find the x of the vertex, but not the y.", "Hallo la x del vértice, pero no la y."), t("I do not use x = −b/(2a).", "No aplico x = −b/(2a).")),
         (t("Opening and intercepts", "Apertura e interceptos"), t("I tell the opening from a and find all the intercepts.", "Identifico la apertura por el signo de a y hallo todos los interceptos."), t("I find only one kind of intercept.", "Hallo solo un tipo de intercepto."), t("I do not connect a with the opening.", "No relaciono a con la apertura.")),
         (t("Maximum and minimum in context", "Máximo y mínimo en contexto"), t("I explain the vertex as the maximum or the minimum, with its units.", "Interpreto el vértice como máximo o mínimo, con sus unidades."), t("I find the vertex but do not explain it.", "Hallo el vértice, pero no lo interpreto."), t("I do not use the vertex in context.", "No uso el vértice en contexto."))],
        t("<p>In this lesson you studied quadratic functions: the parabola, the way it opens, the vertex and the axis of symmetry, the intercepts, and the vertex as a maximum or a minimum in context.</p>\n<p>In <strong>Lesson 8.2 · Exponential functions, growth and decay, and a first look at logarithms</strong> you study the other great model of the GED test: exponential functions, with compound interest and half-life, and a first look at the logarithm.</p>",
          "<p>En esta lección se estudiaron las funciones cuadráticas: la parábola, su dirección de apertura, el vértice y el eje de simetría, los interceptos y el uso del vértice para hallar máximos y mínimos en contexto.</p>\n<p>En la <strong>Lección 8.2 · Funciones exponenciales, crecimiento/decaimiento e introducción a logaritmos</strong> se estudia el otro gran modelo del GED: las funciones exponenciales, con aplicaciones como el interés compuesto y la vida media, y una primera mirada al logaritmo.</p>"),
        ("8-2", ("", t("Lesson 8.2 · Exponential functions, growth and decay, and a first look at logarithms", "Lección 8.2 · Funciones exponenciales, crecimiento/decaimiento e introducción a logaritmos"))),
        [(t("parabola", "parábola"), t("The U-shaped graph of a quadratic function.", "La gráfica en forma de U de una función cuadrática.")),
         (t("vertex", "vértice"), t("The highest or lowest point of a parabola; its x is −b/(2a).", "El punto más alto o más bajo de una parábola; su x es −b/(2a).")),
         (t("axis of symmetry", "eje de simetría"), t("The vertical line through the vertex: x = −b/(2a).", "La recta vertical que pasa por el vértice: x = −b/(2a).")),
         (t("intercept", "intercepto"), t("A point where the graph crosses an axis.", "Un punto donde la gráfica cruza un eje."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function uniq(l){ return l.filter(function(o, i){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }); }
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function qTxt(a, b, c, n){ return (n || "f") + "(x) = " + pVis([c, b, a]); }
function vert(a, b, c){ var x = -b / (2 * a); return [x, a * x * x + b * x + c]; }
function rr(v){ return Math.round(v * 100) / 100; }
function rangoPara(a, b, c){ var v = vert(a, b, c), x0 = Math.floor(v[0] - 5), x1 = Math.ceil(v[0] + 5), ys = [v[1], a * x0 * x0 + b * x0 + c, a * x1 * x1 + b * x1 + c, c];
  var y0 = Math.floor(Math.min(0, Math.min.apply(null, ys))) - 1, y1 = Math.ceil(Math.max(0, Math.max.apply(null, ys))) + 1; if (y1 - y0 > 40){ if (a > 0) y1 = Math.ceil(Math.max(v[1] + 30, c + 2, 2)); else y0 = Math.floor(Math.min(v[1] - 30, c - 2, -2)); }
  return {x0: Math.min(x0, -1), x1: Math.max(x1, 1), y0: y0, y1: y1}; }

/* ===== MODULE 1 · The shape of the parabola ===== */
function paDibuja(){ var a = +$("f-a").value, b = +$("f-b").value, c = +$("f-c").value;
  if (!a){ a = .5; $("f-a").value = .5; }
  $("f-av").textContent = sg(a); $("f-bv").textContent = sg(b); $("f-cv").textContent = sg(c);
  var v = vert(a, b, c), R = {x0: -8, x1: 8, y0: -10, y1: 10};
  $("f-graf").innerHTML = grafFun({rango: R, paso: 2, curvas: [{f: function(x){ return a * x * x + b * x + c; }}], puntos: [[v[0], v[1], "#c62828", T("vertex ", "vértice ") + par(rr(v[0]), rr(v[1])), 6.5, a < 0], [0, c, "#ef6c00", par(0, c), 6, a < 0, v[0] < 0]],
    voz: T("Graph of ", "Gráfica de ") + qTxt(a, b, c) + T(". Vertex ", ". Vértice ") + par(rr(v[0]), rr(v[1])) + "."});
  $("f-txt").innerHTML = '<div class="linea"><strong>' + qTxt(a, b, c) + "</strong></div>" +
    '<div class="linea">' + (a > 0 ? T("a = " + sg(a) + " is positive: the parabola opens <strong>up</strong> and the vertex is a <strong>minimum</strong>.", "a = " + sg(a) + " es positivo: la parábola abre <strong>hacia arriba</strong> y el vértice es un <strong>mínimo</strong>.") : T("a = " + sg(a) + " is negative: the parabola opens <strong>down</strong> and the vertex is a <strong>maximum</strong>.", "a = " + sg(a) + " es negativo: la parábola abre <strong>hacia abajo</strong> y el vértice es un <strong>máximo</strong>.")) +
    " " + (Math.abs(a) > 1 ? T("|a| &gt; 1: narrower than y = x².", "|a| &gt; 1: más cerrada que y = x².") : Math.abs(a) < 1 ? T("|a| &lt; 1: wider than y = x².", "|a| &lt; 1: más abierta que y = x².") : T("|a| = 1: as wide as y = x².", "|a| = 1: igual de abierta que y = x².")) + "</div>" +
    '<div class="linea">' + T("Vertex: x = −b/(2a) = ", "Vértice: x = −b/(2a) = ") + sg(rr(v[0])) + ", y = " + sg(rr(v[1])) + T(". The y-intercept is c: ", ". El intercepto con el eje y es c: ") + par(0, c) + ".</div>"; }
["f-a", "f-b", "f-c"].forEach(function(id){ $(id).addEventListener("input", paDibuja); }); paDibuja();
OMR("aq", function(){ var a = nz(-4, 4), b = aleatorio(-6, 6), c = aleatorio(-9, 9), arriba = a > 0;
  return {enun: T("Which way does ", "¿Hacia dónde abre ") + "<strong>" + qTxt(a, b, c) + "</strong>" + T(" open, and what is its vertex?", " y qué es su vértice?"), correcta: arriba ? "am" : "bM", enOrden: true,
    opciones: [{clave: "am", html: T("up · the vertex is a minimum", "hacia arriba · el vértice es un mínimo")}, {clave: "aM", html: T("up · the vertex is a maximum", "hacia arriba · el vértice es un máximo")}, {clave: "bM", html: T("down · the vertex is a maximum", "hacia abajo · el vértice es un máximo")}, {clave: "bm", html: T("down · the vertex is a minimum", "hacia abajo · el vértice es un mínimo")}],
    pista: T("Look only at a, the number in front of x². Then think: opening up, is the vertex the top or the bottom?", "Fíjese solo en a, el número delante de x². Después piense: si abre hacia arriba, ¿el vértice es lo más alto o lo más bajo?"),
    bien: "a = " + sg(a) + (arriba ? T(" &gt; 0: it opens up, and the vertex is the lowest point (a minimum).", " &gt; 0: abre hacia arriba y el vértice es el punto más bajo (un mínimo).") : T(" &lt; 0: it opens down, and the vertex is the highest point (a maximum).", " &lt; 0: abre hacia abajo y el vértice es el punto más alto (un máximo)."))};
});

/* ===== MODULE 2 · The vertex and the axis of symmetry ===== */
var QV = [[1, -4, 3], [1, -6, 5], [-1, 4, 1], [1, 2, -3], [2, -8, 5], [1, 0, 4], [-2, -4, 6], [-1, 6, -5]];
function pasosVert(a, b, c){ var v = vert(a, b, c), d = 2, p = [c, b, a];
  return [T("The coefficients: a = " + sg(a) + ", b = " + sg(b) + ", c = " + sg(c) + ".", "Los coeficientes: a = " + sg(a) + ", b = " + sg(b) + " y c = " + sg(c) + "."),
    T("The x of the vertex: ", "La x del vértice: ") + "x = −b / (2a) = −(" + sg(b) + ") / (2 · " + (a < 0 ? "(" + sg(a) + ")" : a) + ") = " + sg(-b) + " / " + sg(2 * a) + " = <strong>" + sg(rr(v[0])) + "</strong>.",
    T("The y of the vertex: ", "La y del vértice: ") + "f(" + sg(rr(v[0])) + ") = " + sustP(p, rr(v[0])) + " = <strong>" + sg(rr(v[1])) + "</strong>.",
    T("Vertex ", "Vértice ") + "<strong>" + par(rr(v[0]), rr(v[1])) + "</strong>; " + T("axis of symmetry ", "eje de simetría ") + "<strong>x = " + sg(rr(v[0])) + "</strong>" + T(" (an equation in x: a vertical line).", " (una ecuación en x: una recta vertical)."),
    T("Symmetry check: f(" + sg(rr(v[0] - d)) + ") = " + sg(rr(pEval(p, v[0] - d))) + " and f(" + sg(rr(v[0] + d)) + ") = " + sg(rr(pEval(p, v[0] + d))) + ": the same height on both sides of the axis.", "Comprobación con la simetría: f(" + sg(rr(v[0] - d)) + ") = " + sg(rr(pEval(p, v[0] - d))) + " y f(" + sg(rr(v[0] + d)) + ") = " + sg(rr(pEval(p, v[0] + d))) + ": la misma altura a los dos lados del eje."),
    "<strong>" + (a > 0 ? T("a &gt; 0: the vertex is a minimum.", "a &gt; 0: el vértice es un mínimo.") : T("a &lt; 0: the vertex is a maximum.", "a &lt; 0: el vértice es un máximo.")) + "</strong>"]; }
function grafVert(a, b, c, sim){ var v = vert(a, b, c), p = [c, b, a], R = rangoPara(a, b, c), d = 2, pts = [[v[0], v[1], "#c62828", T("vertex ", "vértice ") + par(rr(v[0]), rr(v[1])), 7, a < 0, true]];
  if (sim) pts.push([v[0] - d, pEval(p, v[0] - d), "#2e7d32", null, 6], [v[0] + d, pEval(p, v[0] + d), "#2e7d32", null, 6]);
  return grafFun({rango: R, curvas: [{f: function(x){ return pEval(p, x); }}], segmentos: [[[v[0], R.y0], [v[0], R.y1], "#6a1b9a", "8 6", 2.5]].concat(sim ? [[[v[0] - d, pEval(p, v[0] - d)], [v[0] + d, pEval(p, v[0] + d)], "#2e7d32", "4 4", 2]] : []), puntos: pts,
    voz: T("Graph of ", "Gráfica de ") + qTxt(a, b, c) + T(" with its vertex ", " con su vértice ") + par(rr(v[0]), rr(v[1])) + T(" and its axis x = ", " y su eje x = ") + sg(rr(v[0])) + "."}); }
var VA = null;
pasoAPaso4("v", function(){ var q = QV[+$("v-fun").value]; VA = q; return {enun: T("Find the vertex and the axis of ", "Halle el vértice y el eje de ") + "<strong>" + qTxt(q[0], q[1], q[2]) + "</strong>.", pasos: pasosVert(q[0], q[1], q[2]), inicio: function(){ $("v-graf").innerHTML = ""; }, fin: function(){ $("v-graf").innerHTML = grafVert(VA[0], VA[1], VA[2], true); }}; });
$("v-fun").addEventListener("change", function(){ $("v-nuevo").click(); });
creaPracticaPar("vq", function(){ var a = elige([1, 1, -1, 2, -2, 3]), h = aleatorio(-4, 4), k = aleatorio(-8, 8), b = -2 * a * h, c = a * h * h + k;
  return {enun: T("Find the vertex of ", "Halle el vértice de ") + "<strong>" + qTxt(a, b, c) + "</strong>.", x: h, y: k,
    diag: function(x, y){ if (x === -h && h) return T("Check the sign of the x: x = −b/(2a) = −(" + sg(b) + ") / " + sg(2 * a) + ".", "Revise el signo de la x: x = −b/(2a) = −(" + sg(b) + ") / " + sg(2 * a) + "."); if (x === h) return T("The x is right. Now evaluate f(" + sg(h) + ") to find the y.", "La x está bien. Ahora evalúe f(" + sg(h) + ") para hallar la y."); return T("Use x = −b/(2a), then evaluate the function at that x.", "Use x = −b/(2a) y después evalúe la función en esa x."); },
    solucion: "x = −(" + sg(b) + ") / (2 · " + (a < 0 ? "(" + sg(a) + ")" : a) + ") = " + sg(h) + "; f(" + sg(h) + ") = " + sustP([c, b, a], h) + " = " + sg(k) + T(". Vertex ", ". Vértice ") + par(h, k) + "."};
});

/* ===== MODULE 3 · The intercepts ===== */
var QI = [[1, -4, 3], [1, -2, -8], [1, -6, 9], [1, 2, 5], [2, -3, -2], [1, -2, -1]];
function pasosInter(a, b, c){ var p = [c, b, a], D = b * b - 4 * a * c, st = [];
  st.push(T("With the y-axis: f(0) = c = " + sg(c) + ", so the point is ", "Con el eje y: f(0) = c = " + sg(c) + ", así que el punto es ") + "<strong>" + par(0, c) + "</strong>.");
  st.push(T("With the x-axis, solve ", "Con el eje x se resuelve ") + pVis(p) + " = 0. " + T("Discriminant: ", "Discriminante: ") + "b² − 4ac = " + (b < 0 ? "(" + sg(b) + ")" : b) + "² − 4(" + sg(a) + ")(" + sg(c) + ") = " + sg(D) + ".");
  if (D < 0){ st.push(T("The discriminant is negative: the equation has no real solutions.", "El discriminante es negativo: la ecuación no tiene soluciones reales.")); st.push("<strong>" + T("No x-intercepts: the parabola does not touch the x-axis.", "Ningún intercepto con el eje x: la parábola no toca el eje x.") + "</strong>"); return st; }
  var r = Math.sqrt(D), x1 = (-b - r) / (2 * a), x2 = (-b + r) / (2 * a);
  if (D === 0){ st.push(T("The discriminant is 0: one double root, x = −b/(2a) = " + sg(rr(x1)) + ".", "El discriminante es 0: una raíz doble, x = −b/(2a) = " + sg(rr(x1)) + ".")); st.push("<strong>" + T("One x-intercept, ", "Un intercepto con el eje x, ") + par(rr(x1), 0) + T(": the vertex touches the axis.", ": el vértice toca el eje.") + "</strong>"); return st; }
  st.push(T("Positive discriminant: two solutions. ", "Discriminante positivo: dos soluciones. ") + "x = (" + sg(-b) + " ± √" + D + ") / " + sg(2 * a) + (r === Math.round(r) ? " = (" + sg(-b) + " ± " + r + ") / " + sg(2 * a) : " ≈ (" + sg(-b) + " ± " + rr(r) + ") / " + sg(2 * a)) + ".");
  var lo = Math.min(x1, x2), hi = Math.max(x1, x2);
  st.push("<strong>" + T("Two x-intercepts: ", "Dos interceptos con el eje x: ") + par(rr(lo), 0) + T(" and ", " y ") + par(rr(hi), 0) + (r === Math.round(r) ? "" : T(" (rounded)", " (redondeados)")) + ".</strong>"); return st; }
var IA = null;
pasoAPaso4("i", function(){ var q = QI[+$("i-fun").value]; IA = q; return {enun: T("Find the intercepts of ", "Halle los interceptos de ") + "<strong>" + qTxt(q[0], q[1], q[2]) + "</strong>.", pasos: pasosInter(q[0], q[1], q[2]), inicio: function(){ $("i-graf").innerHTML = ""; },
  fin: function(){ var a = IA[0], b = IA[1], c = IA[2], p = [c, b, a], D = b * b - 4 * a * c, pts = [[0, c, "#ef6c00", par(0, c), 6.5, a < 0, vert(a, b, c)[0] < 0]];
    if (D >= 0){ var r = Math.sqrt(D); [(-b - r) / (2 * a), (-b + r) / (2 * a)].forEach(function(x, i){ if (i && D === 0) return; pts.push([x, 0, "#2e7d32", par(rr(x), 0), 6.5, a < 0, x > vert(a, b, c)[0]]); }); }
    $("i-graf").innerHTML = grafFun({rango: rangoPara(a, b, c), curvas: [{f: function(x){ return pEval(p, x); }}], puntos: pts, voz: T("Graph of ", "Gráfica de ") + qTxt(a, b, c) + T(" with its intercepts.", " con sus interceptos.")}); }}; });
$("i-fun").addEventListener("change", function(){ $("i-nuevo").click(); });
OMR("iq", function(){ var t = aleatorio(0, 2);
  if (t === 0){ var a = nz(-3, 3), b = aleatorio(-6, 6), c = nz(-9, 9);
    return {enun: T("What is the y-intercept of ", "¿Cuál es el intercepto con el eje y de ") + "<strong>" + qTxt(a, b, c) + "</strong>?", correcta: "ok",
      opciones: uniq([{clave: "ok", html: par(0, c)}, {clave: "x", html: par(c, 0)}, {clave: "s", html: par(0, -c)}, {clave: "a", html: par(0, a)}]),
      pista: T("On the y-axis, x = 0: evaluate f(0).", "En el eje y, x = 0: evalúe f(0)."), bien: "f(0) = " + sg(c) + "."}; }
  if (t === 1){ var r1 = aleatorio(-6, 6), r2; do { r2 = aleatorio(-6, 6); } while (r2 === r1); var k = elige([1, 1, 2]), p = pMul([-r1 * k, k], [-r2, 1]), fact = Math.random() < .5;
    var txt = fact ? "f(x) = " + (k === 1 ? "" : k) + "(x " + (r1 < 0 ? "+ " + -r1 : "− " + r1) + ")(x " + (r2 < 0 ? "+ " + -r2 : "− " + r2) + ")" : "f(x) = " + pVis(p);
    var lo = Math.min(r1, r2), hi = Math.max(r1, r2), op = function(u, v){ return T("x = " + sg(u) + " and x = " + sg(v), "x = " + sg(u) + " y x = " + sg(v)); };
    return {enun: T("What are the x-intercepts of ", "¿Cuáles son los interceptos con el eje x de ") + "<strong>" + txt.replace(/\(x − 0\)/g, "x").replace(/\(x \+ 0\)/g, "x") + "</strong>?", correcta: "ok",
      opciones: uniq([{clave: "ok", html: op(lo, hi)}, {clave: "s", html: op(-hi, -lo)}, {clave: "y", html: op(0, p[0])}, {clave: "m", html: op(lo, -hi)}]),
      pista: fact ? T("Set each factor equal to 0. Careful with the signs: x − 3 = 0 gives x = 3.", "Iguale cada factor a 0. Cuidado con los signos: x − 3 = 0 da x = 3.") : T("Factor the trinomial (or use the quadratic formula) and set each factor equal to 0.", "Factorice el trinomio (o use la fórmula cuadrática) e iguale cada factor a 0."),
      bien: T("The factors give ", "Los factores dan ") + op(lo, hi) + "."}; }
  var a2 = nz(-2, 3), b2 = aleatorio(-6, 6), c2 = aleatorio(-6, 6), D = b2 * b2 - 4 * a2 * c2, n = D > 0 ? "2" : D === 0 ? "1" : "0";
  if (Math.random() < .35){ var h = aleatorio(-3, 3); a2 = 1; b2 = -2 * h; c2 = h * h; D = 0; n = "1"; }
  return {enun: T("How many x-intercepts does ", "¿Cuántos interceptos con el eje x tiene ") + "<strong>" + qTxt(a2, b2, c2) + "</strong>" + T(" have?", "?"), correcta: n, enOrden: true,
    opciones: [{clave: "2", html: T("two", "dos")}, {clave: "1", html: T("one", "uno")}, {clave: "0", html: T("none", "ninguno")}],
    pista: T("Find the discriminant b² − 4ac: positive, two; zero, one; negative, none.", "Calcule el discriminante b² − 4ac: positivo, dos; cero, uno; negativo, ninguno."),
    bien: "b² − 4ac = " + (b2 < 0 ? "(" + sg(b2) + ")" : b2) + "² − 4(" + sg(a2) + ")(" + sg(c2) + ") = " + sg(D) + "."};
});

/* ===== MODULE 4 · Maximum and minimum in context ===== */
var CTX = [
 {a: -16, b: 64, c: 80, x0: 0, x1: 5, p: .5, n: "h(t)", vx: "t", ux: T("seconds", "segundos"), uy: T("feet", "pies"), ex: T("A ball is thrown from a roof, and its height in feet after t seconds is h(t) = −16t² + 64t + 80.", "Una pelota se lanza desde una azotea y su altura en pies a los t segundos es h(t) = −16t² + 64t + 80."), qx: T("After how many seconds is it highest?", "¿A los cuántos segundos alcanza la altura máxima?"), qy: T("What is that greatest height?", "¿Cuál es esa altura máxima?")},
 {a: -2, b: 40, c: 0, x0: 0, x1: 20, p: .5, n: "A(x)", vx: "x", ux: T("feet", "pies"), uy: T("square feet", "pies cuadrados"), ex: T("A rectangular garden against a wall is fenced on three sides with 40 feet of fence. If each side perpendicular to the wall is x, the area is A(x) = x(40 − 2x) = −2x² + 40x.", "Un jardín rectangular contra una pared se cerca por tres lados con 40 pies de cerca. Si cada lado perpendicular a la pared mide x, el área es A(x) = x(40 − 2x) = −2x² + 40x."), qx: T("How long should x be for the greatest area?", "¿Cuánto debe medir x para que el área sea máxima?"), qy: T("What is the greatest area?", "¿Cuál es el área máxima?")},
 {a: -2, b: 100, c: 0, x0: 0, x1: 50, p: 1, n: "I(x)", vx: "x", ux: T("dollars", "dólares"), uy: T("dollars", "dólares"), ex: T("A store sells (100 − 2x) T-shirts when the price is x dollars. The income is I(x) = x(100 − 2x) = −2x² + 100x.", "Una tienda vende (100 − 2x) camisetas cuando el precio es x dólares. El ingreso es I(x) = x(100 − 2x) = −2x² + 100x."), qx: T("Which price gives the greatest income?", "¿Qué precio deja el ingreso máximo?"), qy: T("What is that greatest income?", "¿Cuál es ese ingreso máximo?")},
 {a: 1, b: -20, c: 150, x0: 0, x1: 20, p: 1, n: "C(x)", vx: "x", ux: T("pieces", "piezas"), uy: T("dollars", "dólares"), ex: T("A shop's daily cost, in dollars, is C(x) = x² − 20x + 150, where x is the number of pieces made.", "El costo diario de un taller, en dólares, es C(x) = x² − 20x + 150, donde x es la cantidad de piezas producidas."), qx: T("How many pieces give the least cost?", "¿Con cuántas piezas el costo es mínimo?"), qy: T("What is that least cost?", "¿Cuál es ese costo mínimo?")}];
function cuDibuja(){ var C = CTX[+$("x-caso").value], s = $("x-val"); s.min = C.x0; s.max = C.x1; s.step = C.p; if (+s.value > C.x1 || +s.value < C.x0) s.value = C.x0 + (C.x1 - C.x0) / 4;
  var x = +s.value, p = [C.c, C.b, C.a], v = vert(C.a, C.b, C.c), fx = pEval(p, x), ys = [pEval(p, C.x0), pEval(p, C.x1), v[1]], y0 = Math.min(0, Math.min.apply(null, ys)), y1 = Math.max.apply(null, ys);
  $("x-valv").textContent = sg(x); $("x-enun").innerHTML = C.ex;
  var dol = C.uy === T("dollars", "dólares"), f = function(y){ return dol ? "$" + rr(y).toLocaleString("en-US") : rr(y).toLocaleString("en-US") + " " + C.uy; };
  var R = {x0: C.x0, x1: C.x1, y0: Math.floor(y0 - (y1 - y0) * .05), y1: Math.ceil(y1 + (y1 - y0) * .12)};
  $("x-graf").innerHTML = grafFun({rango: R, curvas: [{f: function(t){ return t >= C.x0 && t <= C.x1 ? pEval(p, t) : NaN; }}], segmentos: [[[x, R.y0], [x, fx], "#00695c", "5 5", 2]],
    puntos: [[v[0], v[1], "#c62828", (C.a < 0 ? T("maximum ", "máximo ") : T("minimum ", "mínimo ")) + f(v[1]), 7, C.a < 0, v[0] < (C.x0 + C.x1) / 2], [x, fx, "#00695c", C.vx + " = " + sg(x), 6, C.a > 0, x < v[0]]],
    voz: C.n + ": " + (C.a < 0 ? T("greatest value ", "valor máximo ") : T("least value ", "valor mínimo ")) + f(v[1]) + T(" at ", " en ") + C.vx + " = " + sg(v[0]) + "."});
  var dif = Math.abs(fx - v[1]) < 1e-9;
  $("x-txt").innerHTML = '<div class="linea">' + C.qx + " " + C.vx + " = −b / (2a) = −(" + sg(C.b) + ") / (2 · " + (C.a < 0 ? "(" + sg(C.a) + ")" : C.a) + ") = <strong>" + sg(v[0]) + " " + C.ux + "</strong>.</div>" +
    '<div class="linea">' + C.qy + " " + C.n.replace(/\(.\)/, "(" + sg(v[0]) + ")") + " = <strong>" + f(v[1]) + "</strong>.</div>" +
    '<div class="linea">' + T("With the slider: ", "Con el deslizador: ") + C.n.replace(/\(.\)/, "(" + sg(x) + ")") + " = " + f(fx) + ". " + (dif ? T("That is the vertex: no other value does better.", "Ese es el vértice: ningún otro valor lo mejora.") : (C.a < 0 ? T("Less than the maximum, ", "Menos que el máximo, ") : T("More than the minimum, ", "Más que el mínimo, ")) + f(v[1]) + ".") + "</div>"; }
$("x-caso").addEventListener("change", cuDibuja); $("x-val").addEventListener("input", cuDibuja); cuDibuja();
OMR("mq", function(){ var t = aleatorio(0, 2);
  if (t === 0){ var tv = aleatorio(1, 4), v0 = 32 * tv, h0 = elige([0, 0, 5, 10, 20, 48]), hm = -16 * tv * tv + v0 * tv + h0, pide = Math.random() < .5;
    var en = T("A ball's height in feet after t seconds is h(t) = " + pVis([h0, v0, -16]).replace(/x/g, "t") + ". ", "La altura en pies de una pelota a los t segundos es h(t) = " + pVis([h0, v0, -16]).replace(/x/g, "t") + ". ");
    if (pide) return {enun: en + T("When is it highest?", "¿Cuándo alcanza la altura máxima?"), correcta: "ok", opciones: uniq([{clave: "ok", html: tv + " s"}, {clave: "d", html: 2 * tv + " s"}, {clave: "b", html: v0 + " s"}, {clave: "m", html: tv + 1 + " s"}]),
      pista: "t = −b / (2a).", bien: "t = −" + v0 + " / (2 · (−16)) = " + tv + " s."};
    return {enun: en + T("What is its greatest height?", "¿Cuál es su altura máxima?"), correcta: "ok", opciones: uniq([{clave: "ok", html: hm + T(" ft", " pies")}, {clave: "b", html: v0 + T(" ft", " pies")}, {clave: "d", html: 2 * hm + T(" ft", " pies")}, {clave: "s", html: (16 * tv * tv + v0 * tv + h0) + T(" ft", " pies")}]),
      pista: T("First the time of the vertex, t = −b/(2a); then evaluate h at that time.", "Primero el tiempo del vértice, t = −b/(2a); después evalúe h en ese tiempo."), porClave: {s: T("Careful: −16t² is negative.", "Cuidado: −16t² es negativo.")},
      bien: "t = " + tv + "; h(" + tv + ") = −16(" + tv * tv + ") + " + v0 + "(" + tv + ")" + (h0 ? " + " + h0 : "") + " = " + hm + T(" ft.", " pies.")}; }
  if (t === 1){ var a = elige([-1, -2, -3, -5]), xv = elige([10, 15, 20, 25, 30, 40]), b = -2 * a * xv, c = aleatorio(1, 9) * 100, pm = a * xv * xv + b * xv - c;
    return {enun: T("The profit of a business is P(x) = " + pVis([-c, b, a]) + " dollars. How many units give the greatest profit?", "El beneficio de un negocio es B(x) = " + pVis([-c, b, a]) + " dólares. ¿Cuántas unidades lo maximizan?"), correcta: "ok",
      opciones: uniq([{clave: "ok", html: String(xv)}, {clave: "b", html: String(b)}, {clave: "d", html: String(2 * xv)}, {clave: "p", html: "$" + pm.toLocaleString("en-US")}]),
      pista: "x = −b / (2a).", porClave: {p: T("That is the greatest profit, not the number of units.", "Ese es el beneficio máximo, no el número de unidades.")},
      bien: "x = −" + b + " / (2 · (" + a + ")) = " + xv + T(" units; the profit is then $", " unidades; el beneficio es entonces $") + pm.toLocaleString("en-US") + "."}; }
  var P = elige([24, 32, 40, 48, 60, 80]), lado = P / 4;
  return {enun: T("A rectangular pen will use " + P + " feet of fence. Its area is A(x) = x(" + P / 2 + " − x). What is the greatest area?", "Un corral rectangular usará " + P + " pies de cerca. Su área es A(x) = x(" + P / 2 + " − x). ¿Cuál es el área máxima?"), correcta: "ok",
    opciones: uniq([{clave: "ok", html: lado * lado + T(" square feet", " pies cuadrados")}, {clave: "l", html: lado + T(" square feet", " pies cuadrados")}, {clave: "p", html: P * P / 4 + T(" square feet", " pies cuadrados")}, {clave: "m", html: (lado - 1) * (lado + 1) + T(" square feet", " pies cuadrados")}]),
    pista: T("A(x) = −x² + " + P / 2 + "x. The vertex is at x = −b/(2a).", "A(x) = −x² + " + P / 2 + "x. El vértice está en x = −b/(2a)."),
    bien: "x = " + P / 2 + " / 2 = " + lado + "; A(" + lado + ") = " + lado + " · " + lado + " = " + lado * lado + T(" square feet: the best rectangle is a square.", " pies cuadrados: el mejor rectángulo es un cuadrado.")};
});
'''

def practica_pagina():
    n = N
    rango = lambda i, et, mn, mx, st, v: f'<div class="campo"><label for="{i}">{et} <output id="{i}v"></output></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    fq = lambda l: [(str(i), "f(x) = " + v) for i, v in enumerate(l)]
    qv = fq(["x² − 4x + 3", "x² − 6x + 5", "−x² + 4x + 1", "x² + 2x − 3", "2x² − 8x + 5", "x² + 4", "−2x² − 4x + 6", "−x² + 6x − 5"])
    qi = fq(["x² − 4x + 3", "x² − 2x − 8", "x² − 6x + 9", "x² + 2x + 5", "2x² − 3x − 2", "x² − 2x − 1"])
    ctx = [("0", t("The ball", "El proyectil")), ("1", t("The fenced garden", "El jardín cercado")), ("2", t("The store's income", "El ingreso de la tienda")), ("3", t("The cost of production", "El costo de producción"))]
    mods = [
     (t("parabola", "parabola"), t("The parabola and its shape", "La parábola y su forma"),
      f'''      <p>{t("Move a, b, and c in f(x) = ax² + bx + c. The sign of a opens the parabola up or down, |a| makes it narrower or wider, b moves the vertex to the side, and c is the y-intercept.", "Mueva a, b y c en f(x) = ax² + bx + c. El signo de a abre la parábola hacia arriba o hacia abajo, |a| la cierra o la abre, b desplaza el vértice hacia un lado y c es el intercepto con el eje y.")}</p>
      <div class="panel"><div class="campos">{rango("f-a", "a =", -3, 3, 0.5, 1)}{rango("f-b", "b =", -6, 6, 1, -2)}{rango("f-c", "c =", -6, 6, 1, -3)}</div></div>
{n4.salida("f-txt")}
      <div id="f-graf"></div>
{B.om("aq", t("Practice: which way does it open?", "Practique: ¿hacia dónde abre?"))}'''),
     (t("vertex", "vertice"), t("The vertex and the axis of symmetry", "El vértice y el eje de simetría"),
      f'''{n4.formula(t("x of the vertex = −b / (2a) · axis: x = −b / (2a)", "x del vértice = −b / (2a) · eje: x = −b / (2a)"))}
      <div class="panel"><div class="campos">{n4.lista("v-fun", t("Function", "Función"), qv)}</div></div>
{n4.pasos("v", t("Start again", "Empezar de nuevo"))}
      <div id="v-graf"></div>
{n4.par_libre("vq", t("Practice: find the vertex", "Practique: halle el vértice"))}'''),
     (t("intercepts", "interceptos"), t("The intercepts with the axes", "Los interceptos con los ejes"),
      f'''      <p>{t("The y-intercept is f(0) = c. The x-intercepts are the solutions of ax² + bx + c = 0; the discriminant b² − 4ac tells you how many there are.", "El intercepto con el eje y es f(0) = c. Los interceptos con el eje x son las soluciones de ax² + bx + c = 0; el discriminante b² − 4ac dice cuántos hay.")}</p>
      <div class="panel"><div class="campos">{n4.lista("i-fun", t("Function", "Función"), qi)}</div></div>
{n4.pasos("i", t("Start again", "Empezar de nuevo"))}
      <div id="i-graf"></div>
{B.om("iq", t("Practice: the intercepts", "Practique: los interceptos"))}'''),
     (t("maximum", "maximo"), t("Maximum and minimum in context", "Máximo y mínimo en contexto"),
      f'''      <p>{t("Choose a situation. The vertex gives the answer; move the slider to check that no other value does better.", "Elija una situación. El vértice da la respuesta; mueva el deslizador para comprobar que ningún otro valor lo mejora.")}</p>
      <div class="panel"><div class="campos">{n4.lista("x-caso", t("Situation", "Situación"), ctx)}{rango("x-val", t("Try a value:", "Pruebe un valor:"), 0, 6, 0.5, 1)}</div><p class="enun" id="x-enun"></p></div>
      <div id="x-graf"></div>
{n4.salida("x-txt")}
{B.om("mq", t("Practice: maximum and minimum", "Practique: máximo y mínimo"))}''')]
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Funciones cuadráticas: la parábola, el vértice y los interceptos")
