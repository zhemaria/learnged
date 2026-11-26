"""Level 4 · Lesson 7.2 · Relations and functions, f(x) notation, and domain and range — builds the lesson and its practice page in
English and in Spanish. Sources (GEDparaHispanos): clase_mate4/leccion_7-2.html, its complement leccion_7-2-composicion.html, and
algebra/n4-l7-2.html (the function machine, the vertical line test, evaluating f(x), domain and range, and composition: machines in a
chain, why the order matters, tables, context, and the expression of f(g(x))). They are rebuilt here, inside LearnGED, with
math/func4.js and math/poly4.js. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "7-2"
TEMA = ("Systems of inequalities and functions", "Sistemas de desigualdades y funciones")
TIT = ("Relations and functions, f(x) notation, and domain and range", "Relaciones y funciones, notación f(x), dominio y rango")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js", "/math/func4.js")
ESTILO = n4.ESTILO + """
  .maq{display:block;width:100%;max-width:560px;height:auto;margin:10px auto;}
  .tabla-lados td.nueva{background:#e8f5e9;font-weight:700;}
  .tabla-lados.centro td,.tabla-lados.centro th{text-align:center;}
"""

def maquina(x, regla, y, voz, ancho=520):
    return B.svg("0 0 520 150", voz, f'''<rect x="0" y="0" width="520" height="150" fill="#fff"/>
<text x="40" y="82" font-size="30" font-weight="700" fill="#1565c0" text-anchor="middle">{x}</text>
<line x1="68" y1="72" x2="148" y2="72" stroke="#1565c0" stroke-width="4"/><polygon points="160,72 146,64 146,80" fill="#1565c0"/>
<text x="108" y="58" font-size="13" fill="#455a64" text-anchor="middle">{t("input x", "entrada x")}</text>
<rect x="164" y="26" width="192" height="92" rx="16" fill="#ede7f6" stroke="#6a1b9a" stroke-width="3"/>
<text x="260" y="66" font-size="15" fill="#6a1b9a" text-anchor="middle">{t("rule", "regla")}</text>
<text x="260" y="92" font-size="19" font-weight="700" fill="#4a148c" text-anchor="middle">{regla}</text>
<line x1="356" y1="72" x2="436" y2="72" stroke="#2e7d32" stroke-width="4"/><polygon points="448,72 434,64 434,80" fill="#2e7d32"/>
<text x="396" y="58" font-size="13" fill="#455a64" text-anchor="middle">{t("output f(x)", "salida f(x)")}</text>
<text x="480" y="82" font-size="30" font-weight="700" fill="#2e7d32" text-anchor="middle">{y}</text>''', ancho)

def fig_parabola():
    p = n4.Plano(-4, 4, -3, 6, 32, paso=1)
    pts = [(x / 10, (x / 10) ** 2 - 2) for x in range(-28, 29)]
    for a, b in zip(pts, pts[1:]):
        p.seg(a, b, "#1565c0", 3.5)
    p.seg((1.5, -3), (1.5, 6), "#ef6c00", 3, "8 6").punto((1.5, 0.25), "#2e7d32", "(1.5, 0.25)", "ne")
    p.texto((-3.85, -2.3), "y = x² − 2", "#1565c0", 14, "start")
    return p.svg(t("The parabola y = x squared minus 2 with a dashed vertical line at x = 1.5. The line cuts the parabola at only one point, so the parabola is a function.",
                   "La parábola y = x al cuadrado menos 2 con una línea vertical punteada en x = 1.5. La línea corta la parábola en un solo punto, así que la parábola es una función."), 320)

def fig_cadena():
    cuerpo = f'''<rect x="0" y="0" width="560" height="130" fill="#fff"/>
<text x="26" y="72" font-size="26" font-weight="700" fill="#1565c0" text-anchor="middle">4</text>
<line x1="46" y1="64" x2="88" y2="64" stroke="#1565c0" stroke-width="4"/><polygon points="100,64 86,56 86,72" fill="#1565c0"/>
<rect x="102" y="22" width="132" height="84" rx="14" fill="#e3f2fd" stroke="#1565c0" stroke-width="3"/>
<text x="168" y="56" font-size="16" font-weight="700" fill="#0d47a1" text-anchor="middle">g</text><text x="168" y="84" font-size="17" fill="#0d47a1" text-anchor="middle">{t("add 3", "suma 3")}</text>
<line x1="234" y1="64" x2="266" y2="64" stroke="#455a64" stroke-width="4"/><polygon points="278,64 264,56 264,72" fill="#455a64"/>
<text x="256" y="44" font-size="22" font-weight="700" fill="#263238" text-anchor="middle">7</text>
<rect x="280" y="22" width="132" height="84" rx="14" fill="#ede7f6" stroke="#6a1b9a" stroke-width="3"/>
<text x="346" y="56" font-size="16" font-weight="700" fill="#4a148c" text-anchor="middle">f</text><text x="346" y="84" font-size="17" fill="#4a148c" text-anchor="middle">{t("times 2", "por 2")}</text>
<line x1="412" y1="64" x2="470" y2="64" stroke="#2e7d32" stroke-width="4"/><polygon points="482,64 468,56 468,72" fill="#2e7d32"/>
<text x="522" y="73" font-size="26" font-weight="700" fill="#2e7d32" text-anchor="middle">14</text>
<text x="168" y="124" font-size="14" fill="#455a64" text-anchor="middle">g(4) = 7</text><text x="346" y="124" font-size="14" fill="#455a64" text-anchor="middle">f(7) = 14</text>'''
    return B.svg("0 0 560 130", t("Two machines in a chain: 4 goes into g, which adds 3 and gives 7; 7 goes into f, which multiplies by 2 and gives 14. So f of g of 4 is 14.",
                                  "Dos máquinas en cadena: el 4 entra en g, que suma 3 y da 7; el 7 entra en f, que multiplica por 2 y da 14. Por lo tanto, f de g de 4 es 14."), cuerpo, 540)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 7.1.</strong> In Lesson 7.1 you worked with regions of the plane. Now comes one of the central ideas of the GED test: the <strong>function</strong>. A function is a rule that takes an input and gives back exactly one output. It is the base of all of Topic 8.", "<strong>Conexión con la lección anterior.</strong> En la Lección 7.1 se trabajó con regiones del plano. Ahora se introduce uno de los conceptos centrales del GED: la <strong>función</strong>. Una función es una regla que toma una entrada y devuelve exactamente una salida. Es la base de todo el Tema 8.")}</p>
<p>{t("Think of a function as a <strong>machine</strong>: a number goes in (the input x), the machine applies a rule, and a result comes out (the output f(x)). The key condition: <strong>each input gives only one output</strong>.", "Conviene imaginar una función como una <strong>máquina</strong>: entra un número (la entrada x), la máquina aplica una regla y sale un resultado (la salida f(x)). La condición clave: <strong>cada entrada produce una sola salida</strong>.")}</p>
{maquina("4", "f(x) = 2x − 3", "5", t("A function machine: the input 4 goes into the rule f of x = 2x minus 3, and the output 5 comes out.", "Una máquina de funciones: la entrada 4 entra en la regla f de x = 2x − 3 y sale la salida 5."))}
{caja("tip", t("The input test", "La prueba de la entrada"), t("<p>If the same input (the same value of x) had two different outputs, the relation would not be a function. A machine that gave two different results for the same number would be broken.</p>", "<p>Si una misma entrada (un mismo valor de x) tuviera dos salidas distintas, la relación no sería función. Una máquina que diera dos resultados distintos para el mismo número estaría descompuesta.</p>"))}
{enlace(n, t("machine", "maquina"), t("the function machine", "la máquina de funciones"), t("Inputs and outputs of a function, with the table of pairs filling in, and a broken machine that gives two outputs.", "Entradas y salidas de una función, con la tabla de pares que se va completando, y una máquina descompuesta que da dos salidas."))}'''

    s2 = f'''<p>{t("On a graph, a relation is a function if <strong>no vertical line</strong> cuts it at more than one point. If some vertical line touches the graph two or more times, that input would have several outputs, and the relation would not be a function.", "En una gráfica, una relación es función si <strong>ninguna línea vertical</strong> la corta en más de un punto. Si alguna vertical toca la gráfica dos o más veces, esa entrada tendría varias salidas y no sería función.")}</p>
{fig_parabola()}
<p>{t("The parabola is a function: any vertical line cuts it only once. A circle or a parabola “lying on its side” would fail the test.", "La parábola es una función: cualquier línea vertical la corta una sola vez. En cambio, una circunferencia o una parábola «acostada» fallarían la prueba.")}</p>
{practica("p1", t("Practice 1 — A set of pairs", "Práctica 1 — Un conjunto de pares"), t("Is {(1, 2), (2, 3), (3, 4)} a function?", "¿Es función {(1, 2), (2, 3), (3, 4)}?"), [("a", t("Yes, it is a function", "Sí, es función")), ("b", t("No", "No")), ("c", t("You cannot tell", "No se puede saber"))])}
{practica("p2", t("Practice 2 — A repeated input", "Práctica 2 — Una entrada repetida"), t("Is {(1, 2), (1, 5), (2, 3)} a function?", "¿Es función {(1, 2), (1, 5), (2, 3)}?"), [("a", t("No: the input 1 has two outputs", "No, la entrada 1 tiene dos salidas")), ("b", t("Yes, it is a function", "Sí, es función")), ("c", t("Yes, always", "Sí, siempre"))])}
{practica("p3", t("Practice 3 — A vertical line", "Práctica 3 — Una recta vertical"), t("Is a vertical line (x = 3) a function?", "Una recta vertical (x = 3), ¿es función?"), [("a", t("Yes", "Sí")), ("b", t("No: it fails the vertical line test", "No, falla la prueba de la línea vertical")), ("c", t("Sometimes", "A veces"))])}
{enlace(n, t("vertical-line", "linea-vertical"), t("the vertical line test", "la prueba de la línea vertical"), t("Move a vertical line across six relations and count how many points it cuts, including the circle and the parabola on its side.", "Mueva la línea vertical sobre seis relaciones y cuente en cuántos puntos corta, incluidas la circunferencia y la parábola acostada."))}'''

    s3 = f'''<p>{t("The notation f(x) is read “f of x” and means the output of the function for the input x. To <strong>evaluate</strong>, substitute the value of x and simplify following the order of operations (PEMDAS).", "La notación f(x) se lee «f de x» e indica la salida de la función para una entrada x. Para <strong>evaluar</strong> se sustituye el valor de x y se simplifica respetando el orden de operaciones (PEMDAS).")}</p>
{ejemplo(t("Example 1: if f(x) = 2x − 3, find f(4).", "Ejemplo 1 · Si f(x) = 2x − 3, calcular f(4)."),
  [("1", t("Substitute x = 4:", "Se sustituye x = 4:"), "f(4) = 2(4) − 3."), ("2", t("Simplify:", "Se simplifica:"), "8 − 3 = 5."),
   ("✓", t("Answer.", "Respuesta."), "<strong>f(4) = 5.</strong>")])}
{ejemplo(t("Example 2 (quadratic): if f(x) = x² + 1, find f(−2).", "Ejemplo 2 · Cuadrática. Si f(x) = x² + 1, calcular f(−2)."),
  [("1", t("Substitute:", "Se sustituye:"), "f(−2) = (−2)² + 1."), ("2", t("Simplify:", "Se simplifica:"), "4 + 1 = 5."),
   ("✓", t("Answer.", "Respuesta."), "<strong>f(−2) = 5.</strong>")])}
{caja("ojo", t("Careful with the signs", "Cuidado con los signos"), t("<p>When you evaluate at a negative number, use parentheses: (−2)² = 4, not −4. The parentheses prevent the most common sign mistake.</p>", "<p>Al evaluar en un número negativo, conviene usar paréntesis: (−2)² = 4, no −4. El paréntesis evita el error de signo más común.</p>"))}
{practica("p4", t("Practice 4 — f(3)", "Práctica 4 — f(3)"), t("f(x) = 4x. What is f(3)?", "f(x) = 4x ; ¿cuánto es f(3)?"), [("a", "12"), ("b", "7"), ("c", "43")])}
{practica("p5", t("Practice 5 — f(−2)", "Práctica 5 — f(−2)"), t("f(x) = x + 5. What is f(−2)?", "f(x) = x + 5 ; ¿cuánto es f(−2)?"), [("a", "7"), ("b", "3"), ("c", "−3")])}
{practica("p6", t("Practice 6 — f(4)", "Práctica 6 — f(4)"), t("f(x) = x². What is f(4)?", "f(x) = x² ; ¿cuánto es f(4)?"), [("a", "8"), ("b", "4"), ("c", "16")])}
{enlace(n, t("notation", "notacion"), t("evaluating f(x)", "la evaluación de f(x)"), t("Choose a function and a value of x and see the substitution step by step, with the point marked on the graph.", "Elija una función y un valor de x y vea la sustitución paso a paso, con el punto marcado en la gráfica."))}'''

    s4 = f'''<p>{t("The <strong>domain</strong> is all the input values (x). The <strong>range</strong> is all the output values (y). For a set of points, just list the first coordinates (domain) and the second coordinates (range).", "El <strong>dominio</strong> son todos los valores de entrada (x). El <strong>rango</strong> son todos los valores de salida (y). En un conjunto de puntos, basta listar las primeras coordenadas (dominio) y las segundas (rango).")}</p>
{ejemplo(t("Example 3: for the points {(1, 2), (3, 4), (5, 6)}:", "Ejemplo 3 · Para los puntos {(1, 2), (3, 4), (5, 6)}:"),
  [("1", t("Domain (inputs):", "Dominio (entradas):"), "{1, 3, 5}."), ("2", t("Range (outputs):", "Rango (salidas):"), "{2, 4, 6}.")])}
{tabla(t("Kinds of functions by their form", "Clasificar funciones por su forma"), t("Kinds of functions by their algebraic form", "Tipos de función según su forma algebraica"), [t("Kind", "Tipo"), t("Form", "Forma")],
  [[t("Linear", "Lineal"), "f(x) = mx + b"], [t("Quadratic", "Cuadrática"), "f(x) = ax² + bx + c"], [t("Exponential", "Exponencial"), "f(x) = a · bˣ"], [t("Rational", "Racional"), t("f(x) = a fraction with the variable in the denominator", "f(x) = fracción con variable en el denominador")]])}
{practica("p7", t("Practice 7 — The domain", "Práctica 7 — El dominio"), t("For the points {(0, 1), (2, 3), (4, 5)}, what is the domain?", "Para los puntos {(0, 1), (2, 3), (4, 5)}, ¿cuál es el dominio?"), [("a", "{0, 2, 4}"), ("b", "{1, 3, 5}"), ("c", "{0, 1}")])}
{practica("p8", t("Practice 8 — The range", "Práctica 8 — El rango"), t("For the same points, what is the range?", "Para los mismos puntos, ¿cuál es el rango?"), [("a", "{0, 2, 4}"), ("b", "{1, 5}"), ("c", "{1, 3, 5}")])}
{practica("p9", t("Practice 9 — Outputs", "Práctica 9 — Salidas"), t("The range is made of the values of:", "El rango está formado por los valores de:"), [("a", t("the input (x)", "entrada (x)")), ("b", t("the output (y)", "salida (y)")), ("c", t("the slope", "la pendiente"))])}
{enlace(n, t("domain-range", "dominio-rango"), t("domain and range", "el dominio y el rango"), t("Seven relations, from sets of points to rational functions, with the domain read across and the range read up and down.", "Siete relaciones, de conjuntos de puntos a funciones racionales, con el dominio leído a lo ancho y el rango a lo alto."))}'''

    s5 = f'''<p>{t("What if the output of one function goes into another? That is the <strong>composition of functions</strong>. The GED test asks it as “if f(x) = … and g(x) = …, what is f(g(3))?”, and you solve it with what you already know: evaluate functions, twice, in the right order.", "¿Qué pasa si la salida de una función entra en otra? Eso es la <strong>composición de funciones</strong>. El examen GED la pregunta en la forma «si f(x) = … y g(x) = …, ¿cuál es el valor de f(g(3))?», y se resuelve con lo que ya sabe: evaluar funciones, dos veces y en el orden correcto.")}</p>
<p>{t("In f(g(x)), read “f of g of x,” there are two machines in a chain. First x goes into machine <strong>g</strong>. What comes out, g(x), then goes into machine <strong>f</strong>. Some books write (f ∘ g)(x): it means the same thing.", "En f(g(x)), que se lee «f de g de x», hay dos máquinas en cadena. Primero el valor x entra en la máquina <strong>g</strong>. Lo que sale, g(x), entra después en la máquina <strong>f</strong>. Algunos libros escriben (f ∘ g)(x): significa lo mismo.")}</p>
{fig_cadena()}
{ejemplo(t("Example 4: if f(x) = 3x − 2 and g(x) = x + 4, find f(g(2)).", "Ejemplo 4 · Si f(x) = 3x − 2 y g(x) = x + 4, hallar f(g(2))."),
  [("1", t("Inside first:", "Primero adentro:"), "g(2) = 2 + 4 = 6."), ("2", t("Then outside:", "Después afuera:"), "f(6) = 3(6) − 2 = 18 − 2 = 16."),
   ("✓", t("Answer.", "Respuesta."), "<strong>f(g(2)) = 16.</strong>")])}
{caja("ojo", t("The order matters", "El orden importa"), t("<p>The function closest to the x acts first: in f(g(x)), g goes first. With f(x) = 2x and g(x) = x + 5, f(g(3)) = f(8) = 16, but g(f(3)) = g(6) = 11. And a composition is not a product: f(g(2)) is not f(2) · g(2).</p>", "<p>Actúa primero la función que está más cerca de la x: en f(g(x)), va primero la g. Con f(x) = 2x y g(x) = x + 5, f(g(3)) = f(8) = 16, pero g(f(3)) = g(6) = 11. Y la composición no es una multiplicación: f(g(2)) no es f(2) · g(2).</p>"))}
{ejemplo(t("Example 5: if f(x) = 3x + 1 and g(x) = x − 2, write the expression of f(g(x)).", "Ejemplo 5 · Si f(x) = 3x + 1 y g(x) = x − 2, hallar la expresión de f(g(x))."),
  [("1", t("Put g(x) inside f, with parentheses:", "Se escribe g(x) dentro de f, con paréntesis:"), "f(g(x)) = 3(x − 2) + 1."), ("2", t("Distribute and combine:", "Se distribuye y se combinan los términos:"), "3x − 6 + 1 = 3x − 5."),
   ("3", t("Check with x = 4:", "Se comprueba con x = 4:"), t("g(4) = 2 and f(2) = 7; with the formula, 3(4) − 5 = 7.", "g(4) = 2 y f(2) = 7; con la fórmula, 3(4) − 5 = 7.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>f(g(x)) = 3x − 5.</strong>")])}
{practica("p10", t("Practice 10 — Inside out", "Práctica 10 — De adentro hacia afuera"), t("f(x) = 2x + 1 and g(x) = x − 3. What is f(g(5))?", "f(x) = 2x + 1 y g(x) = x − 3. ¿Cuánto vale f(g(5))?"), [("a", "5"), ("b", "8"), ("c", "11")])}
{practica("p11", t("Practice 11 — With a square", "Práctica 11 — Con un cuadrado"), t("f(x) = x² and g(x) = x + 2. What is f(g(3))?", "f(x) = x² y g(x) = x + 2. ¿Cuánto vale f(g(3))?"), [("a", "11"), ("b", "25"), ("c", "15")])}
{practica("p12", t("Practice 12 — Which goes first?", "Práctica 12 — ¿Cuál va primero?"), t("In f(g(4)), which function is applied first?", "En la expresión f(g(4)), ¿qué función se aplica primero?"), [("a", "g"), ("b", "f"), ("c", t("both at once", "las dos a la vez"))])}
{enlace(n, t("composition", "composicion"), t("machines in a chain", "las máquinas en cadena"), t("The output of g goes into f: follow the chain step by step and compare f(g(x)) with g(f(x)) for the same x.", "La salida de g entra en f: recorra la cadena paso a paso y compare f(g(x)) con g(f(x)) para el mismo x."))}
{enlace(n, t("composition-tables", "composicion-tablas"), t("composition with tables, context, and expressions", "la composición con tablas, contexto y expresiones"), t("Read f(g(a)) in tables, in coupon and tax problems, and write the expression of f(g(x)).", "Lea f(g(a)) en tablas, en problemas de cupones e impuestos, y escriba la expresión de f(g(x))."))}'''

    secciones = [("s-" + t("function", "funcion"), t("What is a function? The function machine", "¿Qué es una función? La máquina de funciones"), s1),
                 ("s-" + t("vertical-line", "linea-vertical"), t("The vertical line test", "La prueba de la línea vertical"), s2),
                 ("s-" + t("notation", "notacion"), t("f(x) notation: evaluating functions", "La notación f(x): evaluar funciones"), s3),
                 ("s-" + t("domain-range", "dominio-rango"), t("Domain and range", "Dominio y rango"), s4),
                 ("s-" + t("composition", "composicion"), t("Composition of functions", "Composición de funciones"), s5)]

    lesson = {"next": t("Lesson 7.3", "Lección 7.3"), "review": t("sections 3 and 5", "las secciones 3 y 5"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Look at the inputs 1, 2, 3: none repeats.", "Mire las entradas 1, 2, 3: ninguna se repite."), "c": t("Yes, you can tell: check whether an input repeats.", "Sí se puede saber: revise si se repite una entrada.")}, "right": t("Each input has one output.", "Cada entrada tiene una sola salida."), "solution": t("Yes.", "Sí.")},
      "p2": {"ok": "a", "hints": {"b": t("The input 1 appears twice, with 2 and with 5.", "La entrada 1 aparece dos veces, con 2 y con 5."), "c": t("A repeated input with two outputs breaks the rule.", "Una entrada repetida con dos salidas rompe la regla.")}, "right": t("1 → 2 and 1 → 5: two outputs.", "1 → 2 y 1 → 5: dos salidas."), "solution": t("No.", "No.")},
      "p3": {"ok": "b", "hints": {"a": t("The input 3 has infinitely many outputs.", "La entrada 3 tiene infinitas salidas."), "c": t("It always fails: the vertical line at x = 3 touches it everywhere.", "Falla siempre: la vertical en x = 3 la toca en todos sus puntos.")}, "right": t("x = 3 gives every y.", "x = 3 da todas las y."), "solution": t("No.", "No.")},
      "p4": {"ok": "a", "hints": {"b": t("4x means 4 times x, not 4 + x.", "4x es 4 por x, no 4 + x."), "c": t("4x is not the digits 4 and 3 side by side.", "4x no es poner el 4 y el 3 juntos.")}, "right": "4(3) = 12.", "solution": "12."},
      "p5": {"ok": "b", "hints": {"a": t("That is 2 + 5; the input is −2.", "Eso es 2 + 5; la entrada es −2."), "c": t("−2 + 5 is positive.", "−2 + 5 es positivo.")}, "right": "−2 + 5 = 3.", "solution": "3."},
      "p6": {"ok": "c", "hints": {"a": t("x² is x times x, not 2 times x.", "x² es x por x, no 2 por x."), "b": t("Square the 4: 4 · 4.", "Eleve el 4 al cuadrado: 4 · 4.")}, "right": "4² = 16.", "solution": "16."},
      "p7": {"ok": "a", "hints": {"b": t("Those are the outputs (the range).", "Esas son las salidas (el rango)."), "c": t("Take every first coordinate.", "Tome todas las primeras coordenadas.")}, "right": t("The first coordinates.", "Las primeras coordenadas."), "solution": "{0, 2, 4}."},
      "p8": {"ok": "c", "hints": {"a": t("Those are the inputs (the domain).", "Esas son las entradas (el dominio)."), "b": t("Take every second coordinate: 1, 3, and 5.", "Tome todas las segundas coordenadas: 1, 3 y 5.")}, "right": t("The second coordinates.", "Las segundas coordenadas."), "solution": "{1, 3, 5}."},
      "p9": {"ok": "b", "hints": {"a": t("The inputs form the domain.", "Las entradas forman el dominio."), "c": t("The slope is not a set of values.", "La pendiente no es un conjunto de valores.")}, "right": t("Range = outputs.", "Rango = salidas."), "solution": t("The output (y).", "La salida (y).")},
      "p10": {"ok": "c", "hints": {"a": t("That is f(2) − … : first compute g(5) = 2.", "Primero calcule g(5) = 2."), "b": t("g(5) = 2, then f(2) = 2(2) + 1.", "g(5) = 2, luego f(2) = 2(2) + 1.")}, "right": "g(5) = 2; f(2) = 5.", "solution": "5."},
      "p11": {"ok": "b", "hints": {"a": t("That is g(f(3)) = 9 + 2. Inside first: g(3) = 5.", "Eso es g(f(3)) = 9 + 2. Primero adentro: g(3) = 5."), "c": t("That is f(3) · … : it is not a product. g(3) = 5, then 5².", "No es un producto. g(3) = 5, luego 5².")}, "right": "g(3) = 5; f(5) = 25.", "solution": "25."},
      "p12": {"ok": "a", "hints": {"b": t("f is outside: it acts last.", "La f está afuera: actúa al final."), "c": t("One after the other, never at once.", "Una después de la otra, nunca a la vez.")}, "right": t("g touches the 4: it goes first.", "La g toca el 4: va primero."), "solution": "g."},
     }}
    lesson["practice"]["p10"]["ok"] = "a"
    lesson["practice"]["p10"]["hints"] = {"b": t("Inside first: g(5) = 2, then f(2) = 2(2) + 1.", "Primero adentro: g(5) = 2, luego f(2) = 2(2) + 1."), "c": t("That is f(5) = 11; but you need f of g(5).", "Eso es f(5) = 11; pero se pide f de g(5).")}

    lesson["quiz"] = {
      "A": {"ok": "b", "hints": {"a": t("Several outputs would break the machine.", "Varias salidas descompondrían la máquina."), "c": t("Every input has an output.", "Toda entrada tiene salida."), "d": t("It assigns outputs, not inputs.", "Asigna salidas, no entradas.")}, "solution": t("Exactly one output.", "Exactamente una salida.")},
      "B": {"ok": "c", "hints": {"a": t("The input 2 has two outputs.", "La entrada 2 tiene dos salidas."), "b": t("A repeated input with two outputs is not allowed.", "Una entrada repetida con dos salidas no se permite."), "d": t("You can tell from the table.", "Se puede saber con la tabla.")}, "solution": t("No: the input 2 has two outputs.", "No: la entrada 2 tiene dos salidas.")},
      "C": {"ok": "b", "hints": {"a": t("3 · 4 = 12, then add 2.", "3 · 4 = 12, y luego se suma 2."), "c": t("3x is 3 times x.", "3x es 3 por x."), "d": t("Substitute: 3(4) + 2.", "Sustituya: 3(4) + 2.")}, "solution": "f(4) = 14."},
      "D": {"ok": "d", "hints": {"a": t("(−2)² = 4, and 2(−2) = −4.", "(−2)² = 4, y 2(−2) = −4."), "b": t("(−2)² is positive.", "(−2)² es positivo."), "c": t("Add both terms: 4 + (−4).", "Sume los dos términos: 4 + (−4).")}, "solution": "f(−2) = 4 − 4 = 0."},
      "E": {"ok": "b", "hints": {"a": t("Those are the outputs (range).", "Esas son las salidas (rango)."), "c": t("Take the first coordinates: 1, 3, 5.", "Tome las primeras coordenadas: 1, 3, 5."), "d": t("It is a finite set of points.", "Es un conjunto finito de puntos.")}, "solution": "{1, 3, 5}."},
      "F": {"ok": "a", "hints": {"b": t("Those are the inputs (domain).", "Esas son las entradas (dominio)."), "c": t("The range has three outputs: 2, 4, 6.", "El rango tiene tres salidas: 2, 4, 6."), "d": t("It is a finite set of points.", "Es un conjunto finito de puntos.")}, "solution": "{2, 4, 6}."},
      "G": {"ok": "c", "hints": {"a": t("That is 3(2) − 1 = 5: g(2) = 4 comes first.", "Eso es 3(2) − 1 = 5: primero va g(2) = 4."), "b": t("That is g(f(2)) = 5² = 25 … check the order: inside first, g(2) = 4.", "Revise el orden: primero adentro, g(2) = 4."), "d": t("g(2) = 4, then f(4) = 3(4) − 1.", "g(2) = 4, luego f(4) = 3(4) − 1.")}, "solution": "g(2) = 4; f(4) = 11."},
      "H": {"ok": "d", "hints": {"a": t("Square the whole f(x) = x + 3, with parentheses.", "Se eleva al cuadrado todo f(x) = x + 3, con paréntesis."), "b": t("(x + 3)² is not x² + 9: the middle term is missing.", "(x + 3)² no es x² + 9: falta el término del medio."), "c": t("g squares; it does not multiply by 3.", "g eleva al cuadrado; no multiplica por 3.")}, "solution": "g(f(x)) = (x + 3)²."},
    }
    quiz = [
     ("A", t("A function assigns to each input:", "Una función asigna a cada entrada:"), [("a", t("several outputs", "varias salidas")), ("b", t("exactly one output", "exactamente una salida")), ("c", t("no output", "ninguna salida")), ("d", t("two inputs", "dos entradas"))]),
     ("B", t("In the table x: 1, 2, 2 with y: 3, 4, 5 (the input 2 gives two outputs), is it a function?", "En la tabla x: 1, 2, 2 con y: 3, 4, 5 (la entrada 2 da dos salidas), ¿es función?"), [("a", t("Yes", "Sí")), ("b", t("Yes, always", "Sí, siempre")), ("c", t("No: the input 2 has two outputs", "No, la entrada 2 tiene dos salidas")), ("d", t("You cannot tell", "No se puede saber"))]),
     ("C", t("If f(x) = 3x + 2, what is f(4)?", "Si f(x) = 3x + 2, ¿cuánto es f(4)?"), [("a", "12"), ("b", "14"), ("c", "9"), ("d", "20")]),
     ("D", t("If f(x) = x² + 2x, what is f(−2)?", "Si f(x) = x² + 2x, ¿cuánto es f(−2)?"), [("a", "8"), ("b", "−8"), ("c", "4"), ("d", "0")]),
     ("E", t("For the points {(1, 2), (3, 4), (5, 6)}, the domain is:", "Para los puntos {(1, 2), (3, 4), (5, 6)}, el dominio es:"), [("a", "{2, 4, 6}"), ("b", "{1, 3, 5}"), ("c", "{1, 2, 3}"), ("d", t("all real numbers", "todos los reales"))]),
     ("F", t("For the same points, the range is:", "Para los mismos puntos, el rango es:"), [("a", "{2, 4, 6}"), ("b", "{1, 3, 5}"), ("c", "{2, 4}"), ("d", t("all real numbers", "todos los reales"))]),
     ("G", t("f(x) = 3x − 1 and g(x) = x². What is f(g(2))?", "f(x) = 3x − 1 y g(x) = x². ¿Cuánto vale f(g(2))?"), [("a", "5"), ("b", "25"), ("c", "11"), ("d", "12")]),
     ("H", t("f(x) = x + 3 and g(x) = x². What is the expression of g(f(x))?", "f(x) = x + 3 y g(x) = x². ¿Cuál es la expresión de g(f(x))?"), [("a", "x² + 3"), ("b", "x² + 9"), ("c", "3x²"), ("d", "(x + 3)²")])]
    lesson["quiz"]["G"]["hints"]["b"] = t("25 would be (3 · 2 − 1)². Inside first: g(2) = 4.", "25 sería (3 · 2 − 1)². Primero adentro: g(2) = 4.")

    tarea = (t("For your own work, with your notebook and graph paper: (1) Function or not? Classify these ten relations and justify each decision with the input test or the vertical line test (draw the graphs): {(1, 2), (2, 4), (3, 6)}; {(1, 2), (1, 5), (3, 4)}; {(−2, 4), (2, 4), (0, 0)}; {(3, 1), (3, 2), (3, 3)}; y = 3x − 2; x = y²; y = x²; x² + y² = 9; x = 4; y = 4. (2) Evaluate the machine: with f(x) = 2x² − 3x + 1, find f(0), f(1), f(−2), and f(1/2). Write each substitution in parentheses and explain what would happen with f(−2) without them. (3) Domain and range: write the domain and range of y = 2x + 1, y = x², y = 2ˣ, and y = 1/x, and classify each as linear, quadratic, exponential, or rational. (4) Composition: with f(x) = 2x − 1 and g(x) = x² + 3, find f(g(0)), f(g(2)), g(f(0)), and g(f(2)), always writing the inside result first. Then write the expressions of f(g(x)) and g(f(x)) for f(x) = 5x and g(x) = x − 3, and check them with x = 2. Then do several exercises of each activity on the practice page. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y papel cuadriculado: (1) ¿Función o no? Clasifique estas diez relaciones y justifique cada decisión con la prueba de la entrada o con la de la línea vertical (dibuje las gráficas): {(1, 2), (2, 4), (3, 6)}; {(1, 2), (1, 5), (3, 4)}; {(−2, 4), (2, 4), (0, 0)}; {(3, 1), (3, 2), (3, 3)}; y = 3x − 2; x = y²; y = x²; x² + y² = 9; x = 4; y = 4. (2) Evaluar la máquina: con f(x) = 2x² − 3x + 1, calcule f(0), f(1), f(−2) y f(1/2). Escriba cada sustitución entre paréntesis y explique qué pasaría con f(−2) si no los usara. (3) Dominio y rango: escriba el dominio y el rango de y = 2x + 1, y = x², y = 2ˣ e y = 1/x, y clasifique cada una como lineal, cuadrática, exponencial o racional. (4) Composición: con f(x) = 2x − 1 y g(x) = x² + 3, calcule f(g(0)), f(g(2)), g(f(0)) y g(f(2)), escribiendo siempre primero el resultado de adentro. Después escriba las expresiones de f(g(x)) y g(f(x)) para f(x) = 5x y g(x) = x − 3, y compruébelas con x = 2. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Think of two steps in your daily life where the result of one goes into the other, such as a discount and then the sales tax. Write each step as a function and compose them.",
               "Piense en dos pasos de su vida diaria en los que el resultado de uno entra en el otro, como un descuento y después el impuesto. Escriba cada paso como una función y compóngalas."))

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Recognize a function, use the vertical line test, evaluate f(x), find the domain and the range, and compose two functions.", "Reconozca una función, aplique la prueba de la línea vertical, evalúe f(x), halle el dominio y el rango, y componga dos funciones."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Decide</strong> whether a relation is a function (one output for each input).", "<strong>Decidir</strong> si una relación es función (una salida por cada entrada)."),
         t("<strong>Apply</strong> the vertical line test to a graph.", "<strong>Aplicar</strong> la prueba de la línea vertical a una gráfica."),
         t("<strong>Evaluate</strong> f(x) with parentheses and the order of operations.", "<strong>Evaluar</strong> f(x) con paréntesis y el orden de operaciones."),
         t("<strong>Find</strong> the domain and the range, and <strong>compose</strong> two functions.", "<strong>Identificar</strong> el dominio y el rango, y <strong>componer</strong> dos funciones.")],
        secciones, tarea, quiz,
        t("Self-check checklist for functions", "Lista de autoevaluación de las funciones"),
        t("Self-check checklist: skills for functions, f(x), domain and range, and composition", "Lista de autoevaluación: destrezas de funciones, f(x), dominio y rango, y composición"),
        [(t("Applying the definition of function", "Aplicar la definición de función"), t("I use the vertical line test and the input test correctly and explain why.", "Aplico la prueba de la línea vertical y la de la entrada correctamente y explico por qué."), t("I sometimes tell them apart, with the tests used partly.", "Distingo a veces, con las pruebas aplicadas de forma parcial."), t("I do not tell a function from a non-function.", "No distingo función de no función.")),
         (t("Evaluating f(x) and f(g(x))", "Evaluar f(x) y f(g(x))"), t("I substitute with parentheses, follow PEMDAS, and compose inside out.", "Sustituyo con paréntesis, respeto PEMDAS y compongo de adentro hacia afuera."), t("I substitute, but I make sign or order mistakes.", "Sustituyo, pero cometo errores de signo o de orden."), t("I do not substitute correctly.", "No sustituyo correctamente.")),
         (t("Finding the domain and range", "Identificar dominio y rango"), t("I find both from a table, a graph, or an equation, and I classify the function by its form.", "Identifico ambos desde tabla, gráfica o ecuación y clasifico la función por su forma."), t("I find one of the two, or I mix them up.", "Identifico uno de los dos o los confundo."), t("I do not find the domain or the range.", "No identifico dominio ni rango."))],
        t("<p>In this lesson you defined a function (one output for each input), applied the vertical line test, evaluated f(x), found the domain and the range, and composed two functions.</p>\n<p>In <strong>Lesson 7.3 · Average rate of change and kinds of functions</strong> you will measure how much a function changes over an interval with the formula (f(b) − f(a)) / (b − a), and tell linear, quadratic, and exponential functions apart by their pattern of change.</p>",
          "<p>En esta lección se definió una función (una salida por cada entrada), se aplicó la prueba de la línea vertical, se evaluó f(x), se identificaron el dominio y el rango y se compusieron dos funciones.</p>\n<p>En la <strong>Lección 7.3 · Tasa de cambio promedio e identificar tipos de funciones</strong> se medirá cuánto cambia una función en un intervalo con la fórmula (f(b) − f(a)) / (b − a), y se distinguirán las funciones lineales, cuadráticas y exponenciales por su patrón de cambio.</p>"),
        ("7-3", ("", t("Lesson 7.3 · Average rate of change and kinds of functions", "Lección 7.3 · Tasa de cambio promedio e identificar tipos de funciones"))),
        [(t("function", "función"), t("A rule that gives exactly one output for each input.", "Una regla que da exactamente una salida para cada entrada.")),
         (t("domain", "dominio"), t("All the input values (x) of a relation.", "Todos los valores de entrada (x) de una relación.")),
         (t("range", "rango"), t("All the output values (y) of a relation.", "Todos los valores de salida (y) de una relación.")),
         (t("composition", "composición"), t("f(g(x)): the output of g goes into f.", "f(g(x)): la salida de g entra en f."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function conj(l){ var u = []; l.forEach(function(v){ if (u.indexOf(v) < 0) u.push(v); }); u.sort(function(a, b){ return a - b; }); return "{" + u.map(sg).join(", ") + "}"; }
function paresTxt(l){ return "{" + l.map(function(p){ return par(p[0], p[1]); }).join(", ") + "}"; }
function maqSVG(x, regla, y, color){ color = color || "#6a1b9a";
  return '<svg class="maq" viewBox="0 0 520 150" role="img" aria-label="' + T("Function machine: input ", "Máquina de funciones: entrada ") + x + T(", rule ", ", regla ") + regla + T(", output ", ", salida ") + y + '">' +
  '<text x="40" y="82" font-size="28" font-weight="700" fill="#1565c0" text-anchor="middle">' + x + '</text><line x1="72" y1="72" x2="148" y2="72" stroke="#1565c0" stroke-width="4"/><polygon points="160,72 146,64 146,80" fill="#1565c0"/>' +
  '<rect x="164" y="26" width="192" height="92" rx="16" fill="#ede7f6" stroke="' + color + '" stroke-width="3"/><text x="260" y="62" font-size="14" fill="' + color + '" text-anchor="middle">' + T("rule", "regla") + '</text><text x="260" y="92" font-size="18" font-weight="700" fill="#4a148c" text-anchor="middle">' + regla + "</text>" +
  '<line x1="356" y1="72" x2="432" y2="72" stroke="#2e7d32" stroke-width="4"/><polygon points="444,72 430,64 430,80" fill="#2e7d32"/><text x="482" y="82" font-size="' + (String(y).length > 5 ? 17 : 26) + '" font-weight="700" fill="#2e7d32" text-anchor="middle">' + y + "</text></svg>"; }

/* ===== MODULE 1 · The function machine ===== */
var REGLAS = [[1, 2], [0, 0, 1], [-4, 3], [0, -2, 1], [10, -1]], mPares = [];
function mRegla(){ return REGLAS[+$("m-regla").value]; }
function mTabla(nueva){ $("m-tabla").innerHTML = mPares.length ? '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Pairs (input, output) of the machine", "Pares (entrada, salida) de la máquina") + '</caption><thead><tr><th scope="col">' + T("Input x", "Entrada x") + '</th><th scope="col">' + T("Output f(x)", "Salida f(x)") + "</th></tr></thead><tbody>" +
  mPares.map(function(p, i){ return "<tr><td" + (i === nueva ? ' class="nueva"' : "") + ">" + sg(p[0]) + "</td><td" + (i === nueva ? ' class="nueva"' : "") + ">" + nf(p[1]) + "</td></tr>"; }).join("") + "</tbody></table></div>" : ""; }
function mMeter(){ var p = mRegla(), x = leeDecimal($("m-x").value);
  if (x === null){ $("m-txt").innerHTML = '<div class="linea">' + T("Type a number for the input.", "Escriba un número como entrada.") + "</div>"; return; }
  var y = pEval(p, x); $("m-svg").innerHTML = maqSVG(sg(x), fDef(p), nf(y));
  $("m-txt").innerHTML = pasosEval(p, x).map(function(s){ return '<div class="linea">' + s + "</div>"; }).join("");
  var i = -1; mPares.forEach(function(q, k){ if (q[0] === x) i = k; }); if (i < 0){ mPares.push([x, y]); mPares.sort(function(a, b){ return a[0] - b[0]; }); mPares.forEach(function(q, k){ if (q[0] === x) i = k; }); }
  mTabla(i); }
$("m-meter").addEventListener("click", mMeter); $("m-x").addEventListener("keydown", function(e){ if (e.key === "Enter") mMeter(); });
$("m-regla").addEventListener("change", function(){ mPares = []; mTabla(); $("m-svg").innerHTML = maqSVG("x", fDef(mRegla()), "f(x)"); $("m-txt").innerHTML = ""; });
$("m-svg").innerHTML = maqSVG("x", fDef(mRegla()), "f(x)");
function mRota(){ var x = leeDecimal($("m-rota-x").value), out = $("m-rota-txt");
  if (x === null){ out.innerHTML = '<div class="linea">' + T("Type a number.", "Escriba un número.") + "</div>"; return; }
  var s; if (x < 0){ s = T("No number squared gives " + sg(x) + ": no output at all.", "Ningún número al cuadrado da " + sg(x) + ": no hay ninguna salida."); $("m-rota-svg").innerHTML = maqSVG(sg(x), "y² = x", "—", "#b71c1c"); }
  else if (x === 0){ s = T("Only 0² = 0: one output, y = 0.", "Solo 0² = 0: una salida, y = 0."); $("m-rota-svg").innerHTML = maqSVG("0", "y² = x", "0", "#b71c1c"); }
  else { var r = Math.sqrt(x); s = T("Both " + nf(r) + " and −" + nf(r) + " squared give " + nf(x) + ": <strong>two outputs for one input</strong>. This machine is broken: y² = x is not a function.", "Tanto " + nf(r) + " como −" + nf(r) + " al cuadrado dan " + nf(x) + ": <strong>dos salidas para una sola entrada</strong>. Esta máquina está descompuesta: y² = x no es función."); $("m-rota-svg").innerHTML = maqSVG(sg(x), "y² = x", nf(r) + T(" and ", " y ") + "−" + nf(r), "#b71c1c"); }
  out.innerHTML = '<div class="linea">' + s + "</div>"; }
$("m-rota").addEventListener("click", mRota); $("m-rota-x").addEventListener("keydown", function(e){ if (e.key === "Enter") mRota(); });
OMR("fq", function(){ var n = aleatorio(4, 5), xs = [], ys = [], k, es = Math.random() < .5, caso;
  while (xs.length < n){ k = aleatorio(-5, 6); if (xs.indexOf(k) < 0) xs.push(k); }
  var pares = xs.map(function(x){ return [x, aleatorio(-4, 8)]; });
  if (es){ caso = aleatorio(0, 2); if (caso === 1){ pares[1][1] = pares[0][1]; } if (caso === 2){ pares.push([pares[0][0], pares[0][1]]); } }
  else { var j = aleatorio(0, n - 1), y2; do { y2 = aleatorio(-4, 8); } while (y2 === pares[j][1]); pares.push([pares[j][0], y2]); }
  pares = baraja(pares);
  var rep = null; if (!es) pares.forEach(function(p){ pares.forEach(function(q){ if (p[0] === q[0] && p[1] !== q[1]) rep = p[0]; }); });
  var tabla = Math.random() < .4;
  var mostrar = tabla ? '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Table of the relation", "Tabla de la relación") + '</caption><tbody><tr><th scope="row">x</th>' + pares.map(function(p){ return "<td>" + sg(p[0]) + "</td>"; }).join("") + '</tr><tr><th scope="row">y</th>' + pares.map(function(p){ return "<td>" + sg(p[1]) + "</td>"; }).join("") + "</tr></tbody></table></div>" : "<strong>" + paresTxt(pares) + "</strong>";
  var dupY = !tabla && es && caso === 1, dupP = es && caso === 2;
  return {enun: T("Is this relation a function? ", "¿Es función esta relación? ") + mostrar, correcta: es ? "si" : "no", enOrden: true,
    opciones: [{clave: "si", html: T("Yes, it is a function", "Sí, es función")}, {clave: "no", html: T("No, it is not a function", "No, no es función")}],
    bien: es ? (dupP ? T("The pair " + par(pares.filter(function(p){ return pares.filter(function(q){ return q[0] === p[0]; }).length > 1; })[0][0], pares.filter(function(p){ return pares.filter(function(q){ return q[0] === p[0]; }).length > 1; })[0][1]) + " is written twice, but it is the same input with the same output: still one output. It is a function.", "El par " + par(pares.filter(function(p){ return pares.filter(function(q){ return q[0] === p[0]; }).length > 1; })[0][0], pares.filter(function(p){ return pares.filter(function(q){ return q[0] === p[0]; }).length > 1; })[0][1]) + " aparece dos veces, pero es la misma entrada con la misma salida: sigue siendo una sola salida. Es función.") :
      T("No input repeats with a different output" + (caso === 1 ? " (a repeated output is allowed)" : "") + ": it is a function.", "Ninguna entrada se repite con otra salida" + (caso === 1 ? " (repetir una salida está permitido)" : "") + ": es función.")) :
      T("The input " + sg(rep) + " has two different outputs: it is not a function.", "La entrada " + sg(rep) + " tiene dos salidas distintas: no es función.")};
});

/* ===== MODULE 2 · The vertical line test ===== */
var RELS = [
 {ramas: [function(x){ return x + 1; }], fun: true, com: T("Each value of x gives only one height: the vertical line always cuts at one point.", "Cada valor de x da una sola altura: la línea vertical corta siempre en un punto.")},
 {ramas: [function(x){ return x * x - 2; }], fun: true, com: T("The parabola opens up with two branches, but for each x there is only one point.", "Aunque la parábola tenga dos ramas hacia arriba, para cada x hay un solo punto.")},
 {ramas: [function(x){ return Math.abs(x); }], fun: true, com: T("The V also passes the test: one point for each value of x.", "La V también pasa la prueba: un solo punto por cada valor de x.")},
 {ramas: [function(x){ return Math.abs(x) <= 5 ? Math.sqrt(25 - x * x) : NaN; }, function(x){ return Math.abs(x) <= 5 ? -Math.sqrt(25 - x * x) : NaN; }], fun: false, circ: 5, com: T("Between x = −5 and x = 5 the vertical line cuts at two points, above and below. It is not a function.", "Entre x = −5 y x = 5 la línea vertical corta en dos puntos: arriba y abajo. No es función.")},
 {ramas: [function(x){ return x >= -3 ? Math.sqrt(x + 3) : NaN; }, function(x){ return x >= -3 ? -Math.sqrt(x + 3) : NaN; }], fun: false, com: T("To the right of x = −3 every vertical line cuts the parabola on its side twice. It is not a function.", "A la derecha de x = −3, cada vertical corta dos veces la parábola acostada. No es función.")},
 {vert: 2, ramas: [], fun: false, com: T("The vertical line x = 2 is its own vertical line: at x = 2 it touches every point. It is not a function.", "La recta x = 2 es ella misma una vertical: en x = 2 la toca en todos sus puntos. No es función.")}];
function cortes(Rl, k){ if (Rl.vert !== undefined) return Math.abs(k - Rl.vert) < 1e-9 ? Infinity : [];
  var ys = []; Rl.ramas.forEach(function(r){ var y = r(k); if (isFinite(y) && Math.abs(y) <= 7 && !ys.some(function(v){ return Math.abs(v - y) < 1e-9; })) ys.push(y); }); return ys; }
function curvasRel(Rl){ if (Rl.vert !== undefined) return {curvas: [], segmentos: [[[Rl.vert, -7], [Rl.vert, 7], "#1565c0", null, 3.5]]};
  var cs = Rl.ramas.map(function(r){ return {f: r, color: "#1565c0"}; });
  if (Rl.circ){ var pz = []; for (var i = 0; i <= 120; i++){ var a = i / 120 * 2 * Math.PI; pz.push([Rl.circ * Math.cos(a), Rl.circ * Math.sin(a)]); } cs = [{piezas: [pz], color: "#1565c0"}]; }
  if (Rl.acostada !== undefined || Rl === RELS[4]){ var pz2 = []; for (var y = -3.2; y <= 3.2; y += .05) pz2.push([y * y - 3, y]); cs = [{piezas: [pz2], color: "#1565c0"}]; }
  return {curvas: cs, segmentos: []}; }
function lvDibuja(){ var Rl = RELS[+$("lv-rel").value], k = +$("lv-x").value, c = cortes(Rl, k), cr = curvasRel(Rl);
  $("lv-xv").textContent = sg(k);
  var pts = c === Infinity || c === 0 ? [] : c.map(function(y){ return [k, y, c.length > 1 ? "#b71c1c" : "#2e7d32"]; });
  $("lv-graf").innerHTML = grafFun({curvas: cr.curvas, segmentos: cr.segmentos, vertical: k, puntos: pts, voz: T("The relation with a vertical line at x = ", "La relación con una línea vertical en x = ") + sg(k) + "."});
  var n = c === Infinity ? Infinity : c.length;
  $("lv-txt").innerHTML = '<div class="linea">' + T("The vertical line x = " + sg(k) + " cuts the graph at ", "La vertical x = " + sg(k) + " corta la gráfica en ") + "<strong>" + (n === Infinity ? T("infinitely many points", "infinitos puntos") : n + (n === 1 ? T(" point", " punto") : T(" points", " puntos"))) + "</strong>." + (n > 1 ? T(" This input has several outputs.", " Esta entrada tiene varias salidas.") : "") + "</div>" +
    '<div class="linea"><strong>' + (Rl.fun ? T("It is a function.", "Es función.") : T("It is not a function.", "No es función.")) + "</strong> " + Rl.com + "</div>"; }
$("lv-rel").addEventListener("change", lvDibuja); $("lv-x").addEventListener("input", lvDibuja); lvDibuja();
OMR("lq", function(){ var tipo = aleatorio(0, 6), Rl, a, b, h, k, r, voz;
  if (tipo === 0){ a = elige([-2, -1, -.5, .5, 1, 2, 3]); b = aleatorio(-3, 3); Rl = {ramas: [function(x){ return a * x + b; }], fun: true, por: T("a slanted line: one point for each x", "una recta inclinada: un punto por cada x")}; }
  else if (tipo === 1){ a = elige([-1, -.5, .5, 1]); h = aleatorio(-2, 2); k = aleatorio(-3, 3); Rl = {ramas: [function(x){ return a * (x - h) * (x - h) + k; }], fun: true, por: T("a parabola that opens up or down: one point for each x", "una parábola que abre hacia arriba o hacia abajo: un punto por cada x")}; }
  else if (tipo === 2){ h = aleatorio(-2, 2); k = aleatorio(-3, 2); Rl = {ramas: [function(x){ return Math.abs(x - h) + k; }], fun: true, por: T("a V shape: one point for each x", "una V: un punto por cada x")}; }
  else if (tipo === 3){ r = aleatorio(2, 5); h = aleatorio(-1, 1); k = aleatorio(-1, 1); var pz = []; for (var i = 0; i <= 120; i++){ var an = i / 120 * 2 * Math.PI; pz.push([h + r * Math.cos(an), k + r * Math.sin(an)]); } Rl = {piezas: [pz], fun: false, por: T("a circle: a vertical line through it cuts it twice", "una circunferencia: una vertical que la atraviesa la corta dos veces")}; }
  else if (tipo === 4){ h = aleatorio(-4, 0); var s = elige([1, -1]), pz2 = []; for (var y = -3.5; y <= 3.5; y += .05) pz2.push([h + s * y * y, y]); Rl = {piezas: [pz2], fun: false, por: T("a parabola on its side: vertical lines cut it twice", "una parábola acostada: las verticales la cortan dos veces")}; }
  else if (tipo === 5){ h = nz(-5, 5); Rl = {segs: [[[h, -7], [h, 7], "#1565c0", null, 3.5]], fun: false, por: T("a vertical line: the input " + h + " has infinitely many outputs", "una recta vertical: la entrada " + h + " tiene infinitas salidas")}; }
  else { k = aleatorio(-5, 5); Rl = {ramas: [function(){ return k; }], fun: true, por: T("a horizontal line: every x has the same single output", "una recta horizontal: cada x tiene una sola salida, la misma")}; }
  var g = grafFun({curvas: Rl.piezas ? [{piezas: Rl.piezas, color: "#1565c0"}] : (Rl.ramas || []).map(function(f){ return {f: f, color: "#1565c0"}; }), segmentos: Rl.segs || [], voz: T("A relation drawn on the coordinate plane: ", "Una relación dibujada en el plano: ") + Rl.por + "."});
  return {enun: T("Is this graph a function? Use the vertical line test.", "¿Esta gráfica es una función? Use la prueba de la línea vertical.") + g, correcta: Rl.fun ? "si" : "no", enOrden: true,
    opciones: [{clave: "si", html: T("Yes, it is a function", "Sí, es función")}, {clave: "no", html: T("No, it is not a function", "No, no es función")}],
    bien: T("It is ", "Es ") + Rl.por + ". " + (Rl.fun ? T("It passes the test: it is a function.", "Pasa la prueba: es función.") : T("It fails the test: it is not a function.", "Falla la prueba: no es función."))};
});

/* ===== MODULE 3 · f(x) notation ===== */
var EVAL = [[-3, 2], [1, 0, 1], [4, 0, -1], [5, 3], [0, -2, 1], [1, -3, 2]];
function nDibuja(){ var p = EVAL[+$("n-fun").value], x = leeDecimal($("n-x").value), out = $("n-txt");
  if (x === null){ out.innerHTML = '<div class="linea">' + T("Type a number for x.", "Escriba un número en x.") + "</div>"; return; }
  var y = pEval(p, x); out.innerHTML = pasosEval(p, x).map(function(s){ return '<div class="linea">' + s + "</div>"; }).join("");
  var R = {x0: -6, x1: 6, y0: -8, y1: 12}, dentro = Math.abs(x) <= 6 && y >= -8 && y <= 12;
  $("n-graf").innerHTML = grafFun({rango: R, paso: 2, curvas: [{f: function(t){ return pEval(p, t); }}], puntos: dentro ? [[x, y, "#2e7d32", par(x, Math.round(y * 100) / 100), 6.5, (x < 2.4) === (pEval(p, x + .3) < pEval(p, x - .3))]] : [], segmentos: dentro ? [[[x, 0], [x, y], "#2e7d32", "5 5", 2], [[0, y], [x, y], "#2e7d32", "5 5", 2]] : [],
    voz: T("Graph of ", "Gráfica de ") + fDef(p) + (dentro ? T(" with the point ", " con el punto ") + par(x, Math.round(y * 100) / 100) : "") + "."});
  if (!dentro) out.innerHTML += '<div class="linea">' + T("The point " + par(x, Math.round(y * 100) / 100) + " is outside this graph window.", "El punto " + par(x, Math.round(y * 100) / 100) + " queda fuera de esta ventana de la gráfica.") + "</div>"; }
$("n-fun").addEventListener("change", nDibuja); $("n-x").addEventListener("input", nDibuja); nDibuja();
creaPracticaLibre("nq", function(){ var t = aleatorio(0, 4), p, a = nz(-4, 5);
  if (t === 0) p = [aleatorio(-9, 9), nz(-5, 6)];
  else if (t === 1) p = [nz(-6, 6), 0, 1];
  else if (t === 2) p = [nz(-2, 9), 0, -1];
  else if (t === 3) p = [0, nz(-4, 4), 1];
  else p = [aleatorio(-3, 3), nz(-4, 4), elige([2, 3, -2])];
  if (t > 0 && Math.random() < .6) a = -aleatorio(1, 4);
  var res = pEval(p, a), error = p.reduce(function(s, c, g){ return s + (g >= 2 ? -c * Math.pow(Math.abs(a), g) : c * Math.pow(a, g)); }, 0);
  return {enun: T("If ", "Si ") + fDef(p) + T(", what is ", ", ¿cuánto es ") + "f(" + sg(a) + ")?",
    evalua: function(txt){ var v = leeDecimal(txt); if (v === null) return {estado: "invalido", msg: T("Type a number, such as 7 or −12.", "Escriba un número, como 7 o −12.")};
      if (Math.abs(v - res) < 1e-9) return {estado: "bien"};
      if (a < 0 && p.length > 2 && Math.abs(v - error) < 1e-9) return {estado: "mal", msg: T("Careful with the sign: (" + sg(a) + ")² = " + a * a + ", positive. Use parentheses.", "Cuidado con el signo: (" + sg(a) + ")² = " + a * a + ", positivo. Use paréntesis.")};
      return {estado: "mal", msg: T("Write " + sustP(p, a) + " and simplify: powers first, then products, then sums.", "Escriba " + sustP(p, a) + " y simplifique: primero las potencias, luego los productos y al final las sumas.")}; },
    solucion: pasosEval(p, a).join(" ")};
});

/* ===== MODULE 4 · Domain and range ===== */
var DR = [
 {pts: [[1, 2], [3, 4], [5, 6]], dom: "{1, 3, 5}", ran: "{2, 4, 6}", com: T("With a set of points, list the first coordinates (domain) and the second coordinates (range).", "Con un conjunto de puntos basta con listar las primeras coordenadas (dominio) y las segundas (rango).")},
 {pts: [[-2, 4], [-1, 1], [0, 0], [1, 1], [2, 4]], dom: "{−2, −1, 0, 1, 2}", ran: "{0, 1, 4}", com: T("1 and 4 appear twice as outputs, but in the range you write them once. Repeating outputs is allowed; repeating inputs with different outputs is not.", "El 1 y el 4 aparecen dos veces como salida, pero en el rango se escriben una sola vez. Repetir salidas está permitido; repetir entradas con salidas distintas, no.")},
 {f: function(x){ return 2 * x - 3; }, d: [-7, 7], r: [-7, 7], dom: T("all real numbers", "todos los números reales"), ran: T("all real numbers", "todos los números reales"), com: T("The line goes on forever across and up and down: no input is forbidden and every output is reached.", "La recta se extiende sin límite a lo ancho y a lo alto: no hay entradas prohibidas ni salidas inalcanzables.")},
 {f: function(x){ return x * x; }, d: [-7, 7], r: [0, 7], dom: T("all real numbers", "todos los números reales"), ran: "y ≥ 0", com: T("Across there is no limit, but the parabola never goes below the x-axis: no output is negative.", "A lo ancho no hay límite, pero la parábola nunca baja del eje x: ninguna salida es negativa.")},
 {f: function(x){ return x * x + 1; }, d: [-7, 7], r: [1, 7], dom: T("all real numbers", "todos los números reales"), ran: "y ≥ 1", com: T("The lowest point (the vertex) is (0, 1): the outputs start at 1.", "El punto más bajo (el vértice) es (0, 1): las salidas empiezan en 1.")},
 {f: function(x){ return x >= 0 ? Math.sqrt(x) : NaN; }, d: [0, 7], r: [0, 7], dom: "x ≥ 0", ran: "y ≥ 0", com: T("You cannot take the square root of a negative number: the graph starts at x = 0 and its outputs are never negative.", "No se puede sacar la raíz cuadrada de un número negativo: la gráfica empieza en x = 0 y sus salidas nunca son negativas.")},
 {f: function(x){ return Math.abs(x) < 1e-9 ? NaN : 1 / x; }, d: [[-7, -.15], [.15, 7]], r: [[-7, -.15], [.15, 7]], dom: "x ≠ 0", ran: "y ≠ 0", com: T("You cannot divide by zero: x = 0 is excluded. And 1/x is never 0, so y = 0 is excluded too.", "No se puede dividir entre cero: x = 0 queda excluido. Y 1/x nunca vale 0, así que y = 0 también queda excluido.")}];
function drDibuja(){ var D = DR[+$("d-rel").value], o = {voz: T("Domain: ", "Dominio: ") + D.dom + T(". Range: ", ". Rango: ") + D.ran + "."};
  if (D.pts){ o.rango = {x0: -3, x1: 7, y0: -2, y1: 7}; o.puntos = D.pts.map(function(p){ return [p[0], p[1], "#1565c0", par(p[0], p[1])]; }); }
  else { o.curvas = [{f: D.f}]; o.dominio = D.d; o.rangoY = D.r; }
  var g = grafFun(o);
  if (D.pts){ /* marks on the axes for a set of points */ var marcas = "", P = Plano({xmin: -3, xmax: 7, ymin: -2, ymax: 7, u: 44, paso: 1});
    D.pts.forEach(function(p){ marcas += '<circle cx="' + P.X(p[0]) + '" cy="' + P.Y(0) + '" r="6" fill="#ef6c00"/><circle cx="' + P.X(0) + '" cy="' + P.Y(p[1]) + '" r="6" fill="#6a1b9a"/>' + P.seg([p[0], p[1]], [p[0], 0], "#ef6c00", 1.5, "4 4") + P.seg([p[0], p[1]], [0, p[1]], "#6a1b9a", 1.5, "4 4"); });
    g = g.replace("</svg>", marcas + "</svg>"); }
  $("d-graf").innerHTML = g;
  $("d-txt").innerHTML = '<div class="linea"><strong style="color:#e65100">' + T("Domain (inputs, read across):", "Dominio (entradas, a lo ancho):") + "</strong> " + D.dom + '</div><div class="linea"><strong style="color:#6a1b9a">' + T("Range (outputs, read up and down):", "Rango (salidas, a lo alto):") + "</strong> " + D.ran + '</div><div class="linea">' + D.com + "</div>"; }
$("d-rel").addEventListener("change", drDibuja); drDibuja();
OMR("dq", function(){ var t = aleatorio(0, 2);
  if (t < 2){ var n = aleatorio(3, 4), xs = []; while (xs.length < n){ var k = aleatorio(-3, 7); if (xs.indexOf(k) < 0) xs.push(k); }
    var pts = xs.map(function(x){ return [x, aleatorio(-2, 9)]; }); if (Math.random() < .5) pts[2][1] = pts[0][1];
    var dom = conj(pts.map(function(p){ return p[0]; })), ran = conj(pts.map(function(p){ return p[1]; })), pide = t === 0 ? "d" : "r";
    var mezcla = conj([pts[0][0], pts[1][1], pts[2][0]]), todos = conj(pts.map(function(p){ return p[0]; }).concat(pts.map(function(p){ return p[1]; })));
    return {enun: T("For the points ", "Para los puntos ") + paresTxt(pts) + T(", what is the ", ", ¿cuál es el ") + (pide === "d" ? T("domain", "dominio") : T("range", "rango")) + "?", correcta: pide === "d" ? dom : ran,
      opciones: [{clave: dom, html: dom}, {clave: ran, html: ran}, {clave: mezcla, html: mezcla}, {clave: todos, html: todos}],
      pista: pide === "d" ? T("The domain is the set of inputs: the first coordinates.", "El dominio es el conjunto de entradas: las primeras coordenadas.") : T("The range is the set of outputs: the second coordinates, each written once.", "El rango es el conjunto de salidas: las segundas coordenadas, cada una una sola vez."),
      bien: T("Domain ", "Dominio ") + dom + T("; range ", "; rango ") + ran + "."}; }
  var tipos = [["lin", fDef([nz(-5, 5), nz(-4, 4)])], ["cuad", fDef([aleatorio(-5, 5), aleatorio(-3, 3), nz(-3, 3)])], ["exp", "f(x) = " + elige([2, 3, 5]) + " · " + elige([2, 3, 4]) + "ˣ"], ["rac", "f(x) = " + nz(1, 6) + " / (x " + elige(["+ 1", "− 2", "+ 3"]) + ")"]], c = elige(tipos);
  return {enun: T("What kind of function is ", "¿Qué tipo de función es ") + "<strong>" + c[1] + "</strong>?", correcta: c[0], enOrden: true,
    opciones: ["lin", "cuad", "exp", "rac"].map(function(k){ return {clave: k, html: nomTipo(k)}; }),
    pista: T("Look at where x is: alone (linear), squared (quadratic), in the exponent (exponential), or in a denominator (rational).", "Fíjese dónde está la x: sola (lineal), al cuadrado (cuadrática), en el exponente (exponencial) o en un denominador (racional)."),
    bien: {lin: T("x appears alone, to the first power: linear.", "La x aparece sola, a la primera potencia: lineal."), cuad: T("The highest power of x is 2: quadratic.", "La mayor potencia de x es 2: cuadrática."), exp: T("x is in the exponent: exponential.", "La x está en el exponente: exponencial."), rac: T("x is in the denominator: rational.", "La x está en el denominador: racional.")}[c[0]]};
});

/* ===== MODULE 5 · Composition: machines in a chain ===== */
var CF = [[3, 1], [0, 2], [0, 0, 1], [-4, 1], [-1, 3], [0, -1]];
function cDibuja(){ var g = CF[+$("c-g").value], f = CF[+$("c-f").value], x = leeDecimal($("c-x").value), out = $("c-txt");
  if (x === null){ out.innerHTML = '<div class="linea">' + T("Type a number for x.", "Escriba un número en x.") + "</div>"; return; }
  var gx = pEval(g, x), fgx = pEval(f, gx), fx = pEval(f, x), gfx = pEval(g, fx);
  $("c-svg").innerHTML = maqSVG(sg(x), fDef(g, "g"), nf(gx), "#1565c0") + maqSVG(nf(gx), fDef(f), nf(fgx));
  out.innerHTML = '<div class="linea"><strong>f(g(' + sg(x) + "))</strong>: " + T("inside, ", "adentro, ") + "g(" + sg(x) + ") = " + sustP(g, x) + " = " + nf(gx) + "; " + T("outside, ", "afuera, ") + "f(" + nf(gx) + ") = " + sustP(f, gx) + " = <strong>" + nf(fgx) + "</strong>.</div>" +
    '<div class="linea"><strong>g(f(' + sg(x) + "))</strong>: " + T("inside, ", "adentro, ") + "f(" + sg(x) + ") = " + sustP(f, x) + " = " + nf(fx) + "; " + T("outside, ", "afuera, ") + "g(" + nf(fx) + ") = " + sustP(g, fx) + " = <strong>" + nf(gfx) + "</strong>.</div>" +
    '<div class="linea">' + (Math.abs(fgx - gfx) < 1e-9 ? T("This time both orders give the same result, but that is a coincidence: in general the order matters.", "Esta vez los dos órdenes dan lo mismo, pero es casualidad: en general el orden importa.") : T("The two orders give different results: <strong>the order matters</strong>. The function closest to the x acts first.", "Los dos órdenes dan resultados distintos: <strong>el orden importa</strong>. Actúa primero la función más cercana a la x.")) + "</div>"; }
["c-g", "c-f"].forEach(function(id){ $(id).addEventListener("change", cDibuja); }); $("c-x").addEventListener("input", cDibuja); cDibuja();
function fAzar(){ var t = aleatorio(0, 3); if (t === 0) return [nz(-5, 5), 1]; if (t === 1) return [0, elige([2, 3, 4, -2])]; if (t === 2) return [nz(-4, 4), elige([2, 3])]; return [nz(-3, 3), 0, 1]; }
creaPracticaLibre("cq", function(){ var f, g; do { f = fAzar(); g = fAzar(); } while (pIgual(f, g) || (f.length > 2 && g.length > 2));
  var a = aleatorio(-3, 4), orden = Math.random() < .5, ext = orden ? f : g, int = orden ? g : f, ni = orden ? "g" : "f", ne = orden ? "f" : "g";
  var ia = pEval(int, a), res = pEval(ext, ia), otro = pEval(int, pEval(ext, a)), prod = pEval(f, a) * pEval(g, a);
  return {enun: T("If ", "Si ") + fDef(f) + T(" and ", " y ") + fDef(g, "g") + T(", what is ", ", ¿cuánto vale ") + ne + "(" + ni + "(" + sg(a) + "))?",
    evalua: function(txt){ var v = leeDecimal(txt); if (v === null) return {estado: "invalido", msg: T("Type a number.", "Escriba un número.")};
      if (Math.abs(v - res) < 1e-9) return {estado: "bien"};
      if (Math.abs(v - otro) < 1e-9) return {estado: "mal", msg: T("You worked in the opposite order. The function closest to the number goes first: " + ni + "(" + sg(a) + ").", "Trabajó en el orden contrario. Va primero la función más cercana al número: " + ni + "(" + sg(a) + ").")};
      if (Math.abs(v - prod) < 1e-9) return {estado: "mal", msg: T("A composition is not a product. Find " + ni + "(" + sg(a) + ") and put that result into " + ne + ".", "La composición no es una multiplicación. Calcule " + ni + "(" + sg(a) + ") y meta ese resultado en " + ne + ".")};
      return {estado: "mal", msg: T("Inside first: " + ni + "(" + sg(a) + "). Then put that result into " + ne + ".", "Primero adentro: " + ni + "(" + sg(a) + "). Después meta ese resultado en " + ne + ".")}; },
    solucion: T("Inside: ", "Adentro: ") + ni + "(" + sg(a) + ") = " + sustP(int, a) + " = " + nf(ia) + ". " + T("Outside: ", "Afuera: ") + ne + "(" + nf(ia) + ") = " + sustP(ext, ia) + " = <strong>" + nf(res) + "</strong>."};
});

/* ===== MODULE 6 · Tables, context, and the expression ===== */
var TB = null;
function tbNueva(){ var v = [1, 2, 3, 4]; TB = {g: baraja(v.slice()), f: baraja(v.slice()).map(function(x){ return x + elige([0, 0, 4]); })};
  /* f must accept the values of g (1–4), and g must accept the values of f when they are in 1–4 */
  $("t-tabla").innerHTML = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Values of f and g for x = 1, 2, 3, and 4", "Valores de f y g para x = 1, 2, 3 y 4") + '</caption><thead><tr><th scope="col">x</th><th scope="col">1</th><th scope="col">2</th><th scope="col">3</th><th scope="col">4</th></tr></thead><tbody><tr><th scope="row">g(x)</th>' + TB.g.map(function(y){ return "<td>" + y + "</td>"; }).join("") + '</tr><tr><th scope="row">f(x)</th>' + TB.f.map(function(y){ return "<td>" + y + "</td>"; }).join("") + "</tr></tbody></table></div>"; tbCalc(); }
function tbCalc(){ var a = +$("t-a").value, fg = $("t-comp").value === "fg", out = $("t-txt");
  var ext = fg ? TB.f : TB.g, int = fg ? TB.g : TB.f, ni = fg ? "g" : "f", ne = fg ? "f" : "g", v = int[a - 1];
  if (v < 1 || v > 4){ out.innerHTML = '<div class="linea">' + ni + "(" + a + ") = " + v + T(", but the table has no column for x = " + v + ": " + ne + "(" + v + ") cannot be read here.", ", pero la tabla no tiene columna para x = " + v + ": " + ne + "(" + v + ") no se puede leer aquí.") + "</div>"; return; }
  out.innerHTML = '<div class="linea">1. ' + T("In the row of " + ni + ", under x = " + a + ": ", "En la fila de " + ni + ", bajo x = " + a + ": ") + ni + "(" + a + ") = " + v + '.</div><div class="linea">2. ' + T("In the row of " + ne + ", under x = " + v + ": ", "En la fila de " + ne + ", bajo x = " + v + ": ") + ne + "(" + v + ") = " + ext[v - 1] + '.</div><div class="linea"><strong>' + ne + "(" + ni + "(" + a + ")) = " + ext[v - 1] + "</strong></div>"; }
$("t-nueva").addEventListener("click", tbNueva); ["t-comp", "t-a"].forEach(function(id){ $(id).addEventListener("change", tbCalc); }); tbNueva();
function dinero(n){ return "$" + (Math.round(n * 100) / 100).toFixed(2); }
function ctDibuja(){ var x = +$("t-precio").value, d = x - 10, td = 1.08 * d, tx = 1.08 * x, dt = tx - 10; $("t-preciov").textContent = "$" + x;
  $("t-ctx").innerHTML = '<div class="linea">' + T("Coupon first, then tax: ", "Primero el cupón y luego el impuesto: ") + "t(d(" + x + ")) = t(" + d + ") = 1.08 · " + d + " = <strong>" + dinero(td) + "</strong></div>" +
    '<div class="linea">' + T("Tax first, then coupon: ", "Primero el impuesto y luego el cupón: ") + "d(t(" + x + ")) = d(" + dinero(tx) + ") = " + dinero(tx) + " − 10 = <strong>" + dinero(dt) + "</strong></div>" +
    '<div class="linea">' + T("The order of the steps changes the price by ", "El orden de los pasos cambia el precio en ") + dinero(dt - td) + T(": with the coupon first, you pay less.", ": con el cupón primero se paga menos.") + "</div>"; }
$("t-precio").addEventListener("input", ctDibuja); ctDibuja();
var EP = [[[1, 3], [-2, 1]], [[0, 0, 1], [1, 1]], [[-3, 2], [4, 1]], [[0, 4], [2, 1]], [[3, 1], [0, 0, 1]], [[0, 5], [-3, 1]]];
function pComp(ext, int){ var r = [0], pot = [1]; ext.forEach(function(c){ r = pSuma(r, pEsc(pot, c)); pot = pMul(pot, int); }); return r; }
function dentroTxt(ext, intTxt){ var l = []; for (var g = ext.length - 1; g >= 0; g--) if (ext[g]) l.push([ext[g], g]);
  return l.map(function(t, i){ var c = t[0], g = t[1], ab = Math.abs(c), cuerpo = g === 0 ? String(ab) : (ab === 1 ? "" : ab) + "(" + intTxt + ")" + (g > 1 ? SUPF[g] : ""); return (i === 0 ? (c < 0 ? "−" : "") : (c < 0 ? " − " : " + ")) + cuerpo; }).join(""); }
function exprPasos(f, g, fg){ var ext = fg ? f : g, int = fg ? g : f, ne = fg ? "f" : "g", ni = fg ? "g" : "f", r = pComp(ext, int), x = 2;
  return {r: r, pasos: [T("Write ", "Se escribe ") + ni + "(x) = " + pVis(int) + T(" inside ", " dentro de ") + ne + T(", in parentheses: ", ", entre paréntesis: ") + ne + "(" + ni + "(x)) = " + dentroTxt(ext, pVis(int)) + ".",
    T("Expand and combine like terms: ", "Se desarrolla y se combinan los términos semejantes: ") + "<strong>" + ne + "(" + ni + "(x)) = " + pVis(r) + "</strong>.",
    T("Check with x = 2: ", "Se comprueba con x = 2: ") + ni + "(2) = " + nf(pEval(int, 2)) + ", " + ne + "(" + nf(pEval(int, 2)) + ") = " + nf(pEval(ext, pEval(int, 2))) + T("; with the formula, ", "; con la fórmula, ") + nf(pEval(r, 2)) + ". ✓"]}; }
function exDibuja(){ var par0 = EP[+$("e-par").value], fg = $("e-orden").value === "fg", E = exprPasos(par0[0], par0[1], fg);
  $("e-fun").innerHTML = fDef(par0[0]) + " ; " + fDef(par0[1], "g");
  $("e-txt").innerHTML = E.pasos.map(function(s, i){ return '<div class="linea">' + (i + 1) + ". " + s + "</div>"; }).join("") +
    (par0[0].length > 2 || par0[1].length > 2 ? '<div class="linea">' + T("Careful: (x + 1)² is not x² + 1. Squaring a binomial gives a middle term.", "Cuidado: (x + 1)² no es x² + 1. Al elevar un binomio al cuadrado aparece el término del medio.") + "</div>" : ""); }
["e-par", "e-orden"].forEach(function(id){ $(id).addEventListener("change", exDibuja); }); exDibuja();
OMR("eq", function(){ var t = aleatorio(0, 2);
  if (t === 0){ var g = baraja([1, 2, 3, 4]), f = baraja([1, 2, 3, 4]).map(function(x){ return x + elige([0, 3, 5]); }), a = aleatorio(1, 4), v = g[a - 1], res = f[v - 1];
    var tb = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Values of f and g", "Valores de f y g") + '</caption><thead><tr><th scope="col">x</th><th scope="col">1</th><th scope="col">2</th><th scope="col">3</th><th scope="col">4</th></tr></thead><tbody><tr><th scope="row">g(x)</th>' + g.map(function(y){ return "<td>" + y + "</td>"; }).join("") + '</tr><tr><th scope="row">f(x)</th>' + f.map(function(y){ return "<td>" + y + "</td>"; }).join("") + "</tr></tbody></table></div>";
    return {enun: T("Use the table. What is f(g(" + a + "))?", "Use la tabla. ¿Cuánto vale f(g(" + a + "))?") + tb, correcta: "ok",
      opciones: [{clave: "ok", html: String(res)}, {clave: "fa", html: String(f[a - 1])}, {clave: "gv", html: String(v)}, {clave: "gf", html: String(f[a - 1] >= 1 && f[a - 1] <= 4 ? g[f[a - 1] - 1] : f[a - 1] + 1)}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }),
      pista: T("First read g(" + a + ") in the row of g. Then look for that number in the x row, and read f below it.", "Primero lea g(" + a + ") en la fila de g. Después busque ese número en la fila de x y lea f debajo."),
      bien: "g(" + a + ") = " + v + "; f(" + v + ") = " + res + "."}; }
  if (t === 1){ var w = elige([12, 15, 18, 20]), h = elige([10, 20, 25, 30, 40]), q = elige([.8, .75, .9]), bruto = w * h, neto = Math.round(q * bruto * 100) / 100;
    return {enun: T("A person earns p(h) = " + w + "h dollars for h hours of work, and after taxes keeps n(p) = " + q + "p. How much does the person keep for " + h + " hours, n(p(" + h + "))?", "Una persona gana p(h) = " + w + "h dólares por h horas de trabajo, y después de impuestos le queda n(p) = " + q + "p. ¿Cuánto le queda por " + h + " horas, n(p(" + h + "))?"), correcta: "ok",
      opciones: [{clave: "ok", html: dinero(neto)}, {clave: "b", html: dinero(bruto)}, {clave: "c", html: dinero(Math.round((1 - q) * bruto * 100) / 100)}, {clave: "d", html: dinero(q * w)}],
      pista: T("Inside first: p(" + h + ") is the pay before taxes. Then take " + q + " of it.", "Primero adentro: p(" + h + ") es el pago antes de impuestos. Después se toma " + q + " de eso."),
      bien: "p(" + h + ") = " + w + " · " + h + " = " + dinero(bruto) + "; n(" + bruto + ") = " + q + " · " + bruto + " = " + dinero(neto) + "."}; }
  var pr = elige(EP), fg = Math.random() < .5, E = exprPasos(pr[0], pr[1], fg), ext = fg ? pr[0] : pr[1], int = fg ? pr[1] : pr[0];
  var mal2 = pComp(int, ext), mal3 = pMul(ext, int), mal1;
  if (ext.length > 2) mal1 = [int[0] * int[0] + ext[0], 0, int[1] * int[1]];            /* squared each term */
  else if (int.length > 2) mal1 = [int[0] + ext[0], 0, ext[1]];                       /* did not multiply the constant */
  else mal1 = [int[0] + ext[0], ext[1] * int[1]];                                      /* did not distribute */
  var ops = [{clave: "ok", html: pVis(E.r)}, {clave: "o", html: pVis(mal2)}, {clave: "p", html: pVis(mal3)}, {clave: "s", html: pVis(mal1)}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; });
  return {enun: T("If ", "Si ") + fDef(pr[0]) + T(" and ", " y ") + fDef(pr[1], "g") + T(", what is the expression of ", ", ¿cuál es la expresión de ") + (fg ? "f(g(x))" : "g(f(x))") + "?", correcta: "ok", opciones: ops,
    pista: T("Write the inside function, with parentheses, in place of the x of the outside function. Then simplify.", "Escriba la función de adentro, con paréntesis, en lugar de la x de la función de afuera. Después simplifique."),
    bien: E.pasos.slice(0, 2).join(" ")};
});
'''

def practica_pagina():
    n = N
    campo = lambda i, et, v, w="5em": f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{i}" value="{v}" style="width:{w}"></div>'
    reglas = [("0", "f(x) = 2x + 1"), ("1", "f(x) = x²"), ("2", "f(x) = 3x − 4"), ("3", "f(x) = x² − 2x"), ("4", "f(x) = 10 − x")]
    rels = [("0", t("y = x + 1 (line)", "y = x + 1 (recta)")), ("1", t("y = x² − 2 (parabola)", "y = x² − 2 (parábola)")), ("2", t("y = |x| (absolute value)", "y = |x| (valor absoluto)")), ("3", t("x² + y² = 25 (circle)", "x² + y² = 25 (circunferencia)")), ("4", t("x = y² − 3 (parabola on its side)", "x = y² − 3 (parábola acostada)")), ("5", t("x = 2 (vertical line)", "x = 2 (recta vertical)"))]
    evals = [("0", "f(x) = 2x − 3"), ("1", "f(x) = x² + 1"), ("2", "f(x) = −x² + 4"), ("3", "f(x) = 3x + 5"), ("4", "f(x) = x² − 2x"), ("5", "f(x) = 2x² − 3x + 1")]
    drs = [("0", t("Points {(1, 2), (3, 4), (5, 6)}", "Puntos {(1, 2), (3, 4), (5, 6)}")), ("1", t("Points {(−2, 4), (−1, 1), (0, 0), (1, 1), (2, 4)}", "Puntos {(−2, 4), (−1, 1), (0, 0), (1, 1), (2, 4)}")), ("2", t("f(x) = 2x − 3 (linear)", "f(x) = 2x − 3 (lineal)")), ("3", t("f(x) = x² (quadratic)", "f(x) = x² (cuadrática)")), ("4", t("f(x) = x² + 1 (quadratic, shifted)", "f(x) = x² + 1 (cuadrática desplazada)")), ("5", t("f(x) = √x (square root)", "f(x) = √x (raíz cuadrada)")), ("6", t("f(x) = 1/x (rational)", "f(x) = 1/x (racional)"))]
    cf = ["x + 3", "2x", "x²", "x − 4", "3x − 1", "−x"]
    eps = [("0", "f(x) = 3x + 1 ; g(x) = x − 2"), ("1", "f(x) = x² ; g(x) = x + 1"), ("2", "f(x) = 2x − 3 ; g(x) = x + 4"), ("3", "f(x) = 4x ; g(x) = x + 2"), ("4", "f(x) = x + 3 ; g(x) = x²"), ("5", "f(x) = 5x ; g(x) = x − 3")]
    tipos = tabla_html = f'''<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Kinds of functions by their algebraic form", "Tipos de función según su forma algebraica")}</caption><thead><tr><th scope="col">{t("Kind", "Tipo")}</th><th scope="col">{t("Form", "Forma")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead><tbody>
<tr><td>{t("Linear", "Lineal")}</td><td>f(x) = mx + b</td><td>f(x) = 2x − 3</td></tr><tr><td>{t("Quadratic", "Cuadrática")}</td><td>f(x) = ax² + bx + c</td><td>f(x) = x² + 1</td></tr>
<tr><td>{t("Exponential", "Exponencial")}</td><td>f(x) = a · bˣ</td><td>f(x) = 3 · 2ˣ</td></tr><tr><td>{t("Rational", "Racional")}</td><td>{t("a fraction with x in the denominator", "fracción con x en el denominador")}</td><td>f(x) = 1/x</td></tr></tbody></table></div>'''
    mods = [
     (t("machine", "maquina"), t("The function machine", "La máquina de funciones"),
      f'''      <p>{t("A number goes in, the rule works on it, and one result comes out. Put several inputs in and watch the table of pairs fill in.", "Entra un número, la regla lo transforma y sale un resultado. Meta varias entradas y observe cómo se llena la tabla de pares.")}</p>
      <div class="panel"><div class="campos">{n4.lista("m-regla", t("Rule", "Regla"), reglas)}{campo("m-x", t("Input x", "Entrada x"), 3)}</div>
        <div class="fila-btn"><button type="button" class="btn" id="m-meter">{t("Put it in the machine", "Meter en la máquina")}</button></div></div>
      <div id="m-svg"></div>
{n4.salida("m-txt")}
      <div id="m-tabla"></div>
      <h3>{t("The broken machine", "La máquina descompuesta")}</h3>
      <p>{t("This machine follows the rule y² = x: it looks for the numbers whose square is the input. Try 9, 0, and −4.", "Esta máquina sigue la regla y² = x: busca los números cuyo cuadrado es la entrada. Pruebe con 9, 0 y −4.")}</p>
      <div class="panel"><div class="campos">{campo("m-rota-x", t("Input x", "Entrada x"), 9)}</div><div class="fila-btn"><button type="button" class="btn-sec" id="m-rota">{t("Try it", "Probar")}</button></div></div>
      <div id="m-rota-svg"></div>
{n4.salida("m-rota-txt")}
{B.om("fq", t("Practice: function or not?", "Practique: ¿función o no?"))}'''),
     (t("vertical-line", "linea-vertical"), t("The vertical line test", "La prueba de la línea vertical"),
      f'''      <p>{t("Choose a relation and slide the vertical line across it. If some vertical line cuts the graph at more than one point, the relation is not a function.", "Elija una relación y deslice la línea vertical sobre ella. Si alguna vertical corta la gráfica en más de un punto, la relación no es función.")}</p>
      <div class="panel"><div class="campos">{n4.lista("lv-rel", t("Relation", "Relación"), rels)}<div class="campo"><label for="lv-x">{t("Vertical line: x =", "Línea vertical: x =")} <output id="lv-xv"></output></label><input type="range" id="lv-x" min="-6" max="6" step="0.5" value="1"></div></div></div>
      <div id="lv-graf"></div>
{n4.salida("lv-txt")}
{B.om("lq", t("Practice: is the graph a function?", "Practique: ¿la gráfica es una función?"))}'''),
     (t("notation", "notacion"), t("f(x) notation: evaluating functions", "La notación f(x): evaluar funciones"),
      f'''      <p>{t("To evaluate, put the input in parentheses in place of x and simplify with the order of operations. The point (x, f(x)) appears on the graph.", "Para evaluar, se sustituye la entrada entre paréntesis en lugar de x y se simplifica con el orden de operaciones. El punto (x, f(x)) aparece en la gráfica.")}</p>
      <div class="panel"><div class="campos">{n4.lista("n-fun", t("Function", "Función"), evals)}{campo("n-x", "x =", -2)}</div></div>
{n4.salida("n-txt")}
      <div id="n-graf"></div>
{B.libre("nq", t("Practice: evaluate f(x)", "Practique: evalúe f(x)"), t("Answer", "Respuesta"), nota=False)}'''),
     (t("domain-range", "dominio-rango"), t("Domain and range", "Dominio y rango"),
      f'''      <p>{t("The <strong>domain</strong> is read across, on the x-axis (orange); the <strong>range</strong> is read up and down, on the y-axis (purple).", "El <strong>dominio</strong> se lee a lo ancho, en el eje x (naranja); el <strong>rango</strong> se lee a lo alto, en el eje y (morado).")}</p>
      <div class="panel"><div class="campos">{n4.lista("d-rel", t("Relation", "Relación"), drs)}</div></div>
      <div id="d-graf"></div>
{n4.salida("d-txt")}
      <h3>{t("Kinds of functions by their form", "Clasificar funciones por su forma")}</h3>
{tipos}
{B.om("dq", t("Practice: domain, range, and kind", "Practique: dominio, rango y tipo"))}'''),
     (t("composition", "composicion"), t("Composition: two machines in a chain", "Composición: dos máquinas en cadena"),
      f'''      <p>{t("In f(g(x)), x goes into g first, and the output of g goes into f. Choose g, f, and x, and compare the result with g(f(x)).", "En f(g(x)), la x entra primero en g, y la salida de g entra en f. Elija g, f y x, y compare el resultado con g(f(x)).")}</p>
      <div class="panel"><div class="campos">{n4.lista("c-g", t("Inside: g(x) =", "Adentro: g(x) ="), [(str(i), v) for i, v in enumerate(cf)], "0")}{n4.lista("c-f", t("Outside: f(x) =", "Afuera: f(x) ="), [(str(i), v) for i, v in enumerate(cf)], "1")}{campo("c-x", "x =", 4)}</div></div>
      <div id="c-svg"></div>
{n4.salida("c-txt")}
{B.libre("cq", t("Practice: follow the chain", "Practique: siga la cadena"), t("Answer", "Respuesta"), nota=False)}'''),
     (t("composition-tables", "composicion-tablas"), t("Composition with tables, in context, and as an expression", "Composición con tablas, en contexto y como expresión"),
      f'''      <p>{t("When the functions come in a table, look up each value in its row, inside out.", "Cuando las funciones vienen en una tabla, se busca cada valor en su fila, de adentro hacia afuera.")}</p>
      <div id="t-tabla"></div>
      <div class="panel"><div class="campos">{n4.lista("t-comp", t("Composition", "Composición"), [("fg", "f(g(a))"), ("gf", "g(f(a))")])}{n4.lista("t-a", "a =", [(str(i), str(i)) for i in range(1, 5)])}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="t-nueva">{t("Another table", "Otra tabla")}</button></div></div>
{n4.salida("t-txt")}
      <h3>{t("In context: a coupon and the sales tax", "En contexto: un cupón y el impuesto")}</h3>
      <p>{t("A store takes off a $10 coupon, d(x) = x − 10, and charges an 8% sales tax, t(x) = 1.08x. Does the order matter?", "Una tienda descuenta un cupón de $10, d(x) = x − 10, y cobra un impuesto del 8 %, t(x) = 1.08x. ¿Importa el orden?")}</p>
      <div class="panel"><div class="campos"><div class="campo"><label for="t-precio">{t("Price of the item:", "Precio del artículo:")} <output id="t-preciov"></output></label><input type="range" id="t-precio" min="20" max="200" step="5" value="50"></div></div></div>
      <div class="salida" aria-live="polite" id="t-ctx"></div>
      <h3>{t("The expression of f(g(x))", "La expresión de f(g(x))")}</h3>
      <div class="panel"><div class="campos">{n4.lista("e-par", t("Functions", "Funciones"), eps)}{n4.lista("e-orden", t("Find", "Hallar"), [("fg", "f(g(x))"), ("gf", "g(f(x))")])}</div><p class="enun" id="e-fun"></p></div>
{n4.salida("e-txt")}
{B.om("eq", t("Practice: tables, context, and expressions", "Practique: tablas, contexto y expresiones"))}''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Six practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Seis actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Relaciones y funciones, notación f(x), dominio y rango")
