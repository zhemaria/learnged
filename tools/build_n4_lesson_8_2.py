"""Level 4 · Lesson 8.2 · Exponential functions, growth and decay, and a first look at logarithms — builds the lesson and its practice page
in English and in Spanish. Sources (GEDparaHispanos): clase_mate4/leccion_8-2.html and algebra/n4-l8-2.html (the base and the starting
value, six situations of growth and decay period by period, the compound interest calculator, and the logarithm as a question).
They are rebuilt here, inside LearnGED, with math/func4.js; all units are U.S. customary.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n4

B.NIVEL = 4
N = "8-2"
TEMA = ("Modeling with functions and a practice GED test", "Modelado de funciones y simulacro GED")
TIT = ("Exponential functions, growth and decay, and a first look at logarithms", "Funciones exponenciales, crecimiento/decaimiento e introducción a logaritmos")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js", "/math/func4.js")
ESTILO = n4.ESTILO + """
  .tabla-lados.centro td,.tabla-lados.centro th{text-align:center;}
  .tabla-lados td.sel{background:#e8f5e9;font-weight:700;}
"""

def fig_exp():
    p = n4.Plano(-3, 3, -1, 8, 34, paso=1)
    up = [(x / 20, 2 ** (x / 20)) for x in range(-60, 61)]
    dn = [(x / 20, 0.5 ** (x / 20)) for x in range(-60, 61)]
    for l, col in ((up, "#1565c0"), (dn, "#c62828")):
        for a, b in zip(l, l[1:]):
            p.seg(a, b, col, 3.5)
    p.punto((0, 1), "#2e7d32").seg((0.08, 1.15), (0.25, 2.25), "#2e7d32", 1.5).texto((0.12, 2.6), "(0, 1)", "#2e7d32", 13, "start")
    p.texto((2.95, 2.0), "y = 2ˣ", "#1565c0", 15, "end").texto((-2.95, 2.0), "y = (1/2)ˣ", "#c62828", 15, "start")
    p.texto((2.9, 1.0), t("growth", "crecimiento"), "#1565c0", 13, "end").texto((-2.9, 1.0), t("decay", "decaimiento"), "#c62828", 13, "start")
    return p.svg(t("The graphs of y = 2 to the x, which grows faster and faster to the right, and y = one half to the x, which decays toward zero to the right without touching it. Both cross at 0, 1.",
                   "Las gráficas de y = 2 a la x, que crece cada vez más rápido hacia la derecha, e y = un medio a la x, que decae hacia cero por la derecha sin tocarlo. Las dos se cruzan en 0, 1."), 330)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 8.1.</strong> Quadratic functions go up and then down (or down and then up), making a parabola. Exponential functions are different: they grow (or decay) faster and faster, because they <strong>multiply by a fixed base</strong>. They model money that earns interest, a population that doubles, or a substance that breaks down.", "<strong>Conexión con la lección anterior.</strong> Las cuadráticas (8.1) crecen y luego decrecen (o al revés) formando una parábola. Las funciones exponenciales son distintas: crecen (o decaen) cada vez más rápido al <strong>multiplicarse por una base fija</strong>. Modelan el dinero que gana interés, una población que se duplica o una sustancia que se desintegra.")}</p>
<p>{t("In f(x) = a · bˣ, the number a is the <strong>starting value</strong> (when x = 0), and the base b decides the behavior:", "En f(x) = a · bˣ, el número a es el <strong>valor inicial</strong> (cuando x = 0) y la base b decide el comportamiento:")}</p>
{tabla(t("Growth or decay", "Crecimiento o decaimiento"), t("The behavior of an exponential function by its base b", "Comportamiento de la función exponencial según la base b"), [t("If the base b…", "Si la base b…"), t("The function…", "La función…"), t("Example", "Ejemplo")],
  [[t("is greater than 1 (b &gt; 1)", "es mayor que 1 (b &gt; 1)"), t("grows (growth)", "crece (crecimiento)"), "y = 2ˣ"], [t("is between 0 and 1 (0 &lt; b &lt; 1)", "está entre 0 y 1 (0 &lt; b &lt; 1)"), t("decays (decay)", "decae (decaimiento)"), "y = (1/2)ˣ"]])}
{fig_exp()}
<p>{t("The two curves cross at (0, 1) because any base to the power 0 is 1. To the right, the growth curve goes up faster and faster; the decay curve gets closer and closer to zero without touching it.", "Las dos curvas se cruzan en (0, 1) porque cualquier base elevada a 0 da 1. A la derecha, la de crecimiento sube cada vez más rápido; la de decaimiento se acerca a cero sin tocarlo.")}</p>
{practica("p1", t("Practice 1 — Base 3", "Práctica 1 — Base 3"), t("f(x) = 3ˣ:", "f(x) = 3ˣ:"), [("a", t("decays", "decae")), ("b", t("grows", "crece"))])}
{practica("p2", t("Practice 2 — Base 0.5", "Práctica 2 — Base 0.5"), t("f(x) = (0.5)ˣ:", "f(x) = (0.5)ˣ:"), [("a", t("decays", "decae")), ("b", t("grows", "crece"))])}
{practica("p3", t("Practice 3 — When does it decay?", "Práctica 3 — ¿Cuándo decae?"), t("In f(x) = a · bˣ, the function decays when:", "En f(x) = a · bˣ, la función decae cuando:"), [("a", "b &gt; 1"), ("b", "0 &lt; b &lt; 1")])}
{enlace(n, t("exponential", "exponencial"), t("the exponential function", "la función exponencial"), t("Sliders for the starting value a and the base b of f(x) = a · bˣ, with the point (0, a) and the curve that grows or decays.", "Deslizadores del valor inicial a y de la base b de f(x) = a · bˣ, con el punto (0, a) y la curva que crece o decae."))}'''

    s2 = f'''<p>{t("Exponential <strong>growth</strong> appears when something is multiplied by a fixed factor every period: a population that doubles, an account that earns interest. Exponential <strong>decay</strong> appears when something is reduced by a fixed factor: the half-life of a radioactive substance, a car that loses value.", "El <strong>crecimiento</strong> exponencial aparece cuando algo se multiplica por un factor fijo en cada período: una población que se duplica, una cuenta que gana interés. El <strong>decaimiento</strong> aparece cuando algo se reduce por un factor fijo: la vida media de una sustancia radiactiva, un auto que pierde valor.")}</p>
{caja("tip", t("Half-life", "Vida media"), t("<p>The half-life is the time it takes for an amount to be cut in half. If there are 80 ounces and the half-life is 1 hour, after 1 hour there are 40 ounces, after 2 hours 20 ounces, and so on.</p>", "<p>La vida media es el tiempo en que una cantidad se reduce a la mitad. Si hay 80 onzas y la vida media es 1 hora, tras 1 hora quedan 40 onzas, tras 2 horas 20 onzas, y así.</p>"))}
{caja("ojo", t("From a percent to the base", "Del porcentaje a la base"), t("<p>Grows 8% each year: it keeps all of it plus 8%, so the base is 1 + 0.08 = 1.08. Loses 15% each year: it keeps 85%, so the base is 1 − 0.15 = 0.85.</p>", "<p>Crece un 8 % cada año: conserva todo más el 8 %, así que la base es 1 + 0.08 = 1.08. Pierde un 15 % cada año: conserva el 85 %, así que la base es 1 − 0.15 = 0.85.</p>"))}
{practica("p4", t("Practice 4 — Doubling", "Práctica 4 — Se duplica"), t("A population that doubles every year is an example of:", "Una población que se duplica cada año es un ejemplo de:"), [("a", t("exponential growth", "crecimiento exponencial")), ("b", t("exponential decay", "decaimiento exponencial"))])}
{practica("p5", t("Practice 5 — Half-life", "Práctica 5 — Vida media"), t("A radioactive substance with a half-life is an example of:", "Una sustancia radiactiva con vida media es un ejemplo de:"), [("a", t("exponential growth", "crecimiento exponencial")), ("b", t("exponential decay", "decaimiento exponencial"))])}
{practica("p6", t("Practice 6 — What is half-life?", "Práctica 6 — ¿Qué es la vida media?"), t("“Half-life” is the time in which the amount:", "«Vida media» es el tiempo en que la cantidad:"), [("a", t("is cut in half", "se reduce a la mitad")), ("b", t("doubles", "se duplica"))])}
{enlace(n, t("context", "contexto"), t("growth and decay", "el crecimiento y el decaimiento"), t("Population, bacteria, half-life, a car that loses value, a medicine that leaves the body, and savings, with the table that shows where each number comes from.", "Población, bacterias, vida media, depreciación de un auto, eliminación de un medicamento y ahorro, con la tabla que muestra de dónde sale cada número."))}'''

    s3 = f'''<p>{t("Compound interest is exponential growth applied to money. It is on the <strong>GED formula sheet</strong>:", "El interés compuesto es crecimiento exponencial aplicado al dinero. Está en la <strong>hoja de fórmulas del GED</strong>:")}</p>
{n4.formula("A = P(1 + r/n)<sup>nt</sup>")}
<p>{t("P is the starting amount (the principal), r the rate (as a decimal), n the number of times it is compounded each year, t the number of years, and A the final amount.", "P es el capital inicial, r la tasa (en decimal), n las veces que se capitaliza por año, t el número de años y A el monto final.")}</p>
{ejemplo(t("Example 1: $1,000 at 5% a year, compounded once a year (n = 1), for 10 years.", "Ejemplo 1 · $1,000 al 5 % anual, capitalizado una vez al año (n = 1), durante 10 años."),
  [("1", t("Substitute:", "Se sustituye:"), "A = 1000(1 + 0.05/1)<sup>1·10</sup> = 1000(1.05)<sup>10</sup>."), ("2", t("With the calculator:", "Con la calculadora:"), "(1.05)<sup>10</sup> ≈ 1.6289."),
   ("✓", t("Answer.", "Respuesta."), "<strong>A ≈ $1,628.89.</strong>")])}
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. For powers such as (1.05)¹⁰, use the power key (^). Write the rate as a decimal (5% = 0.05). The calculator on this page does the same operations, although some keys have other names or are in other places.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. Para potencias como (1.05)¹⁰ use la tecla de la potencia (^). Escriba la tasa en decimal (5 % = 0.05). La calculadora de esta página hace las mismas operaciones, aunque algunas teclas tienen otro nombre o están en otro lugar.</p>"))}
{practica("p7", t("Practice 7 — P", "Práctica 7 — P"), t("In A = P(1 + r/n)<sup>nt</sup>, what is P?", "En A = P(1 + r/n)<sup>nt</sup>, ¿qué representa P?"), [("a", t("the starting amount (principal)", "la cantidad inicial (capital)")), ("b", t("the interest rate", "la tasa de interés")), ("c", t("the time", "el tiempo"))])}
{practica("p8", t("Practice 8 — Ten years", "Práctica 8 — Diez años"), t("$1,000 at 5% a year (n = 1) for 10 years gives about:", "$1,000 al 5 % anual (n = 1) en 10 años da aproximadamente:"), [("a", "$1,500.00"), ("b", "$5,000.00"), ("c", "$1,628.89")])}
{practica("p9", t("Practice 9 — r", "Práctica 9 — r"), t("In the formula, r is:", "En la fórmula, r representa:"), [("a", t("the number of years", "el número de años")), ("b", t("the interest rate", "la tasa de interés")), ("c", t("the principal", "el capital"))])}
{enlace(n, t("interest", "interes"), t("compound interest", "el interés compuesto"), t("A step-by-step calculator with the formula from the GED sheet and a table that compares compounding yearly, twice a year, quarterly, monthly, and daily.", "Calculadora paso a paso con la fórmula de la hoja del GED y una tabla que compara la capitalización anual, semestral, trimestral, mensual y diaria."))}'''

    s4 = f'''<p>{t("The <strong>logarithm</strong> is the inverse of the exponential. It answers the question: “to what exponent must I raise the base to get this number?”", "El <strong>logaritmo</strong> es la operación inversa de la exponencial. Responde la pregunta: «¿a qué exponente hay que elevar la base para obtener este número?»")}</p>
{n4.formula(t("if b<sup>y</sup> = x, then log<sub>b</sub>(x) = y", "si b<sup>y</sup> = x, entonces log<sub>b</sub>(x) = y"))}
{ejemplo(t("Example 2: log₁₀(1000).", "Ejemplo 2 · log₁₀(1000)."), [("1", t("The question:", "La pregunta:"), t("to what power do I raise 10 to get 1000?", "¿a qué potencia elevo 10 para obtener 1000?")), ("✓", t("Since 10³ = 1000,", "Como 10³ = 1000,"), "<strong>log₁₀(1000) = 3.</strong>")])}
{caja("tip", t("The log key", "La tecla log"), t("<p>On the TI-30XS, the log key finds log₁₀ directly. For example, log(100) gives 2, because 10² = 100.</p>", "<p>En la TI-30XS, la tecla log calcula log₁₀ directamente. Por ejemplo, log(100) da 2, porque 10² = 100.</p>"))}
{practica("p10", t("Practice 10 — The inverse", "Práctica 10 — La inversa"), t("The logarithm is the inverse of:", "El logaritmo es la operación inversa de:"), [("a", t("the exponential", "la exponencial")), ("b", t("addition", "la suma")), ("c", t("the square root", "la raíz cuadrada"))])}
{practica("p11", t("Practice 11 — log 1000", "Práctica 11 — log 1000"), t("log₁₀(1000) = ? (10 to what power gives 1000?)", "log₁₀(1000) = ? (¿10 a qué potencia da 1000?)"), [("a", "2"), ("b", "1000"), ("c", "3")])}
{practica("p12", t("Practice 12 — log 100", "Práctica 12 — log 100"), "log₁₀(100) = ?", [("a", "100"), ("b", "2"), ("c", "1")])}
{enlace(n, t("logarithm", "logaritmo"), t("logarithms", "los logaritmos"), t("The logarithm asked as a question, “to what exponent?”, with the table of powers of the base and the switch between exponential and logarithmic form.", "El logaritmo planteado como pregunta, «¿a qué exponente?», con la tabla de potencias de la base y el cambio entre forma exponencial y logarítmica."))}'''

    secciones = [("s-" + t("exponential", "exponencial"), t("The exponential function f(x) = a · bˣ", "La función exponencial f(x) = a · bˣ"), s1),
                 ("s-" + t("context", "contexto"), t("Growth and decay in context", "Crecimiento y decaimiento en contexto"), s2),
                 ("s-" + t("interest", "interes"), t("Compound interest", "El interés compuesto"), s3),
                 ("s-" + t("logarithm", "logaritmo"), t("A first look at the logarithm", "Introducción al logaritmo"), s4)]

    dos = lambda ok, mal, right, sol: {"ok": ok, "hints": mal, "right": right, "solution": sol}
    lesson = {"next": t("Lesson 8.3", "Lección 8.3"), "review": t("sections 1 and 3", "las secciones 1 y 3"),
     "practice": {
      "p1": dos("b", {"a": t("3 is greater than 1.", "3 es mayor que 1.")}, t("b &gt; 1: it grows.", "b &gt; 1: crece."), t("It grows.", "Crece.")),
      "p2": dos("a", {"b": t("0.5 is between 0 and 1.", "0.5 está entre 0 y 1.")}, t("0 &lt; b &lt; 1: it decays.", "0 &lt; b &lt; 1: decae."), t("It decays.", "Decae.")),
      "p3": dos("b", {"a": t("b &gt; 1 is growth.", "b &gt; 1 es crecimiento.")}, t("A base between 0 and 1 makes it smaller each time.", "Una base entre 0 y 1 la achica cada vez."), "0 &lt; b &lt; 1."),
      "p4": dos("a", {"b": t("Doubling makes it bigger.", "Duplicar la hace más grande.")}, t("Multiply by 2 each year: growth.", "Se multiplica por 2 cada año: crecimiento."), t("Exponential growth.", "Crecimiento exponencial.")),
      "p5": dos("b", {"a": t("It gets smaller over time.", "Se hace más pequeña con el tiempo.")}, t("Multiply by 1/2 each half-life: decay.", "Se multiplica por 1/2 en cada vida media: decaimiento."), t("Exponential decay.", "Decaimiento exponencial.")),
      "p6": dos("a", {"b": t("Half-life: half is left.", "Vida media: queda la mitad.")}, t("Half of it is left.", "Queda la mitad."), t("It is cut in half.", "Se reduce a la mitad.")),
      "p7": dos("a", {"b": t("The rate is r.", "La tasa es r."), "c": t("The time is t.", "El tiempo es t.")}, t("P is the principal.", "P es el capital."), t("The starting amount.", "La cantidad inicial.")),
      "p8": dos("c", {"a": t("That is simple interest: 50 × 10. Compound interest earns interest on interest.", "Eso es interés simple: 50 × 10. El compuesto gana interés sobre el interés."), "b": t("That would be multiplying by 5.", "Eso sería multiplicar por 5.")}, "1000(1.05)¹⁰ ≈ 1,628.89.", "$1,628.89."),
      "p9": dos("b", {"a": t("The years are t.", "Los años son t."), "c": t("The principal is P.", "El capital es P.")}, t("r is the rate, as a decimal.", "r es la tasa, en decimal."), t("The interest rate.", "La tasa de interés.")),
      "p10": dos("a", {"b": t("The inverse of addition is subtraction.", "La inversa de la suma es la resta."), "c": t("The inverse of the square root is squaring.", "La inversa de la raíz es elevar al cuadrado.")}, t("It undoes the exponential.", "Deshace la exponencial."), t("The exponential.", "La exponencial.")),
      "p11": dos("c", {"a": t("10² = 100, not 1000.", "10² = 100, no 1000."), "b": t("The answer is an exponent.", "La respuesta es un exponente.")}, "10³ = 1000.", "3."),
      "p12": dos("b", {"a": t("The answer is an exponent.", "La respuesta es un exponente."), "c": t("10¹ = 10, not 100.", "10¹ = 10, no 100.")}, "10² = 100.", "2."),
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("4 is greater than 1.", "4 es mayor que 1."), "b": t("It changes: it multiplies by 4.", "Cambia: se multiplica por 4."), "d": t("x is in the exponent.", "La x está en el exponente.")}, "solution": t("It grows.", "Crece.")},
      "B": {"ok": "b", "hints": {"a": t("1/3 is less than 1.", "1/3 es menor que 1."), "c": t("x is in the exponent.", "La x está en el exponente."), "d": t("It is a function.", "Es una función.")}, "solution": t("It decays.", "Decae.")},
      "C": {"ok": "d", "hints": {"a": t("The base is b.", "La base es b."), "b": t("The exponent is x.", "El exponente es x."), "c": t("Exponentials do not have a slope like lines.", "Las exponenciales no tienen pendiente como las rectas.")}, "solution": t("The starting value.", "El valor inicial.")},
      "D": {"ok": "a", "hints": {"b": t("Any base to the 0 is 1: y = 1 when x = 0.", "Toda base a la 0 da 1: y = 1 cuando x = 0."), "c": t("They never touch 0.", "Nunca tocan el 0."), "d": t("At x = 1 they are 2 and 1/2.", "En x = 1 valen 2 y 1/2.")}, "solution": "(0, 1)."},
      "E": {"ok": "c", "hints": {"a": t("10% of 2,000 is 200, not 100.", "El 10 % de 2,000 es 200, no 100."), "b": t("10% of 2,000 is 200.", "El 10 % de 2,000 es 200."), "d": t("That would double it.", "Eso lo duplicaría.")}, "solution": "2000(1.10) = $2,200."},
      "F": {"ok": "a", "hints": {"b": t("Double three times: 100 → 200 → 400 → 800.", "Duplique tres veces: 100 → 200 → 400 → 800."), "c": t("That multiplies by 3; it doubles each year.", "Eso multiplica por 3; se duplica cada año."), "d": t("100 · 2³ = 800.", "100 · 2³ = 800.")}, "solution": "100 · 2³ = 800."},
      "G": {"ok": "b", "hints": {"a": t("That is after 1 hour.", "Eso es tras 1 hora."), "c": t("Halve, do not subtract 20.", "Se reduce a la mitad, no se resta 20."), "d": t("It never reaches 0.", "Nunca llega a 0.")}, "solution": t("80 → 40 → 20 ounces.", "80 → 40 → 20 onzas.")},
      "H": {"ok": "c", "hints": {"a": t("10² = 100.", "10² = 100."), "b": t("The answer is an exponent.", "La respuesta es un exponente."), "d": t("The answer is an exponent.", "La respuesta es un exponente.")}, "solution": "10³ = 1000, log₁₀(1000) = 3."},
     }}

    quiz = [
     ("A", t("f(x) = 4ˣ. Does it grow or decay?", "f(x) = 4ˣ. ¿Crece o decae?"), [("a", t("it decays", "decae")), ("b", t("it is constant", "es constante")), ("c", t("it grows", "crece")), ("d", t("it is linear", "es lineal"))]),
     ("B", t("f(x) = (1/3)ˣ. Does it grow or decay?", "f(x) = (1/3)ˣ. ¿Crece o decae?"), [("a", t("it grows", "crece")), ("b", t("it decays", "decae")), ("c", t("it is linear", "es lineal")), ("d", t("it is not a function", "no es función"))]),
     ("C", t("In f(x) = a · bˣ, what is a?", "En f(x) = a · bˣ, ¿qué representa a?"), [("a", t("the base", "la base")), ("b", t("the exponent", "el exponente")), ("c", t("the slope", "la pendiente")), ("d", t("the starting value", "el valor inicial"))]),
     ("D", t("The graphs of y = 2ˣ and y = (1/2)ˣ cross at the point:", "Las gráficas de y = 2ˣ e y = (1/2)ˣ se cruzan en el punto:"), [("a", "(0, 1)"), ("b", "(1, 0)"), ("c", "(0, 0)"), ("d", "(1, 1)")]),
     ("E", t("$2,000 at 10% a year (n = 1) for 1 year gives:", "$2,000 al 10 % anual (n = 1) en 1 año dan:"), [("a", "$2,100"), ("b", "$2,010"), ("c", "$2,200"), ("d", "$4,000")]),
     ("F", t("A population doubles every year and starts at 100. How many are there after 3 years?", "Una población se duplica cada año y empieza en 100. ¿Cuántos hay a los 3 años?"), [("a", "800"), ("b", "600"), ("c", "300"), ("d", "2,300")]),
     ("G", t("A substance weighs 80 ounces and its half-life is 1 hour. How much is left after 2 hours?", "Una sustancia de 80 onzas tiene una vida media de 1 hora. ¿Cuánto queda tras 2 horas?"), [("a", t("40 oz", "40 oz")), ("b", t("20 oz", "20 oz")), ("c", t("60 oz", "60 oz")), ("d", t("0 oz", "0 oz"))]),
     ("H", "log₁₀(1000) = ?", [("a", "2"), ("b", "100"), ("c", "3"), ("d", "1000")])]

    tarea = (t("For your own work, with your notebook, the calculator, and the GED formula sheet: (1) The bank and time: find how much $1,000 is worth at 5% interest compounded yearly after 1, 5, 10, and 20 years. Graph the points and describe the shape of the curve: why does the growth speed up? (2) When does it double? With the table above, estimate between which two years the money reaches $2,000, and narrow it down by trying the years in between. Then find log₁₀(1000), log₁₀(100), and log₂(8), and check each result by writing it as a power. (3) Growth or decay? Classify each model and justify it with the base (greater or less than 1): a population P = 2000(1.03)ᵗ; a medicine in the blood M = 500(0.5)ᵗ; savings A = 800(1.04)ᵗ; the temperature difference of a cooling cup of coffee D = 60(0.9)ᵗ; the value of a car V = 25000(0.85)ᵗ. Then do several exercises of each activity on the practice page. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, la calculadora y la hoja de fórmulas del GED: (1) El banco y el tiempo: calcule cuánto valen $1,000 al 5 % de interés compuesto anual después de 1, 5, 10 y 20 años. Grafique los puntos y describa la forma de la curva: ¿por qué el crecimiento se acelera? (2) ¿En cuántos años se duplica? Con la tabla anterior, estime entre qué dos años el dinero llega a $2,000 y afine la estimación probando años intermedios. Después calcule log₁₀(1000), log₁₀(100) y log₂(8), y compruebe cada resultado escribiéndolo como potencia. (3) ¿Crece o decae? Clasifique cada modelo y justifique con la base (mayor o menor que 1): una población P = 2000(1.03)ᵗ; un medicamento en la sangre M = 500(0.5)ᵗ; un ahorro A = 800(1.04)ᵗ; la diferencia de temperatura de un café que se enfría D = 60(0.9)ᵗ; el valor de un auto V = 25000(0.85)ᵗ. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Look at a savings account, a loan, or a credit card statement. Find its yearly rate and how often it compounds, and use the formula to see how much it grows (or how much you owe) in 5 years.",
               "Mire un estado de cuenta de ahorro, de un préstamo o de una tarjeta de crédito. Busque su tasa anual y cada cuánto se capitaliza, y use la fórmula para ver cuánto crece (o cuánto se debe) en 5 años."))

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Tell growth from decay by the base, model real situations, use the compound interest formula, and read a logarithm as “to what exponent?”.", "Distinga el crecimiento del decaimiento por la base, modele situaciones reales, use la fórmula del interés compuesto y lea un logaritmo como «¿a qué exponente?»."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Tell</strong> exponential growth from decay by the base b.", "<strong>Distinguir</strong> el crecimiento del decaimiento exponencial según la base b."),
         t("<strong>Model</strong> growth and decay situations (population, half-life, value).", "<strong>Modelar</strong> situaciones de crecimiento y decaimiento (población, vida media, valor)."),
         t("<strong>Use</strong> the compound interest formula A = P(1 + r/n)<sup>nt</sup>.", "<strong>Aplicar</strong> la fórmula del interés compuesto A = P(1 + r/n)<sup>nt</sup>."),
         t("<strong>Understand</strong> the logarithm as the inverse of the exponential.", "<strong>Entender</strong> el logaritmo como la operación inversa de la exponencial.")],
        secciones, tarea, quiz,
        t("Self-check checklist for exponential functions", "Lista de autoevaluación de las funciones exponenciales"),
        t("Self-check checklist: skills for exponential functions, compound interest, and logarithms", "Lista de autoevaluación: destrezas de funciones exponenciales, interés compuesto y logaritmos"),
        [(t("Growth or decay", "Crecimiento o decaimiento"), t("I tell them apart by the base and connect it with the graph.", "Los distingo por la base y lo conecto con la gráfica."), t("I sometimes mix up growth and decay.", "A veces confundo crecimiento con decaimiento."), t("I do not connect the base with the behavior.", "No relaciono la base con el comportamiento.")),
         (t("Compound interest", "Interés compuesto"), t("I use A = P(1 + r/n)^(nt) with the rate as a decimal and the calculator.", "Aplico A = P(1 + r/n)^(nt) con la tasa en decimal y la calculadora."), t("I substitute, but with mistakes in the variables.", "Sustituyo, pero con errores en las variables."), t("I do not use the formula.", "No uso la fórmula.")),
         (t("Logarithm and exponential", "Logaritmo y exponencial"), t("I find logarithms base 10 and check them as powers.", "Calculo logaritmos base 10 y los compruebo como potencias."), t("I know the idea, but I make mistakes.", "Reconozco la idea, pero cometo errores."), t("I do not see the logarithm as the inverse.", "No reconozco el logaritmo como inversa."))],
        t("<p>In this lesson you studied exponential functions (growth and decay), compound interest, and a first look at the logarithm as the inverse of the exponential.</p>\n<p><strong>Lesson 8.3 · Final project and practice GED math test</strong> closes Level 4: you will present your project “My mathematical model” and take the Level 4 final check. It is the last step before the GED Mathematical Reasoning test.</p>",
          "<p>En esta lección se estudiaron las funciones exponenciales (crecimiento y decaimiento), el interés compuesto y una primera mirada al logaritmo como inversa de la exponencial.</p>\n<p>La <strong>Lección 8.3 · Proyecto final integrador y simulacro GED</strong> cierra el Nivel 4: presentará su proyecto «Mi modelo matemático» y hará la evaluación final del nivel. Es el último paso antes del GED Mathematical Reasoning.</p>"),
        ("8-3", ("", t("Lesson 8.3 · Final project and practice GED math test", "Lección 8.3 · Proyecto final integrador y simulacro GED"))),
        [(t("starting value", "valor inicial"), t("The a in f(x) = a · bˣ: the value when x = 0.", "La a de f(x) = a · bˣ: el valor cuando x = 0.")),
         (t("half-life", "vida media"), t("The time it takes for an amount to be cut in half.", "El tiempo en que una cantidad se reduce a la mitad.")),
         (t("compound interest", "interés compuesto"), t("Interest earned on the interest too: A = P(1 + r/n)^(nt).", "Interés que también se gana sobre el interés: A = P(1 + r/n)^(nt).")),
         (t("logarithm", "logaritmo"), t("The exponent: log_b(x) = y means bʸ = x.", "El exponente: log_b(x) = y significa bʸ = x."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function uniq(l){ return l.filter(function(o, i){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }); }
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function dn(v, d){ var r = Math.round(v * Math.pow(10, d === undefined ? 2 : d)) / Math.pow(10, d === undefined ? 2 : d); return (r < 0 ? "−" : "") + Math.abs(r).toLocaleString("en-US", {maximumFractionDigits: d === undefined ? 2 : d}); }
function din(v){ return "$" + (Math.round(v * 100) / 100).toLocaleString("en-US", {minimumFractionDigits: 2, maximumFractionDigits: 2}); }
function bTxt(b){ return b === Math.round(b) ? String(b) : "(" + String(b) + ")"; }
function eTxt(a, b, v){ return (a === 1 ? "" : dn(a) + " · ") + bTxt(b) + "<sup>" + (v || "x") + "</sup>"; }

/* ===== MODULE 1 · The exponential function ===== */
function exDibuja(){ var a = +$("e-a").value, b = +$("e-b").value; $("e-av").textContent = a; $("e-bv").textContent = b;
  var top = Math.max(a * Math.pow(b, 4), a * Math.pow(b, -3), a) , R = {x0: -3, x1: 5, y0: -1, y1: Math.min(Math.ceil(top * 1.1), 200)};
  $("e-graf").innerHTML = grafFun({rango: R, curvas: [{f: function(x){ return a * Math.pow(b, x); }}], puntos: [[0, a, "#2e7d32", par(0, a), 7, true, true], [1, a * b, "#6a1b9a", par(1, Math.round(a * b * 100) / 100), 6, b < 1, true]],
    voz: T("Graph of f(x) = ", "Gráfica de f(x) = ") + a + " · " + b + T(" to the x.", " a la x.")});
  var k = b > 1 ? T("b = " + b + " &gt; 1: the function <strong>grows</strong>, faster and faster.", "b = " + b + " &gt; 1: la función <strong>crece</strong>, cada vez más rápido.") : b < 1 ? T("0 &lt; b = " + b + " &lt; 1: the function <strong>decays</strong> toward 0 without touching it.", "0 &lt; b = " + b + " &lt; 1: la función <strong>decae</strong> hacia 0 sin tocarlo.") : T("b = 1: 1 to any power is 1, so the function is <strong>constant</strong> (not exponential).", "b = 1: 1 a cualquier potencia es 1, así que la función es <strong>constante</strong> (no es exponencial).");
  $("e-txt").innerHTML = '<div class="linea"><strong>f(x) = ' + eTxt(a, b) + "</strong></div>" + '<div class="linea">' + k + "</div>" +
    '<div class="linea">' + T("Starting value: f(0) = " + a + " · " + b + "⁰ = " + a + ". Each step to the right multiplies by " + b + ": f(1) = " + dn(a * b) + ", f(2) = " + dn(a * b * b) + ".", "Valor inicial: f(0) = " + a + " · " + b + "⁰ = " + a + ". Cada paso a la derecha multiplica por " + b + ": f(1) = " + dn(a * b) + ", f(2) = " + dn(a * b * b) + ".") + "</div>"; }
["e-a", "e-b"].forEach(function(id){ $(id).addEventListener("input", exDibuja); }); exDibuja();
OMR("eq", function(){ var opc = [[2, "2"], [3, "3"], [4, "4"], [1.05, "1.05"], [1.5, "1.5"], [.5, "0.5"], [.8, "0.8"], [.25, "0.25"], [1 / 3, "1/3"], [2 / 3, "2/3"], [1, "1"]], c = elige(opc), a = elige([1, 1, 2, 3, 5, 100]);
  var txt = "f(x) = " + (a === 1 ? "" : a + " · ") + (c[1].length > 1 ? "(" + c[1] + ")" : c[1]) + "<sup>x</sup>", k = c[0] > 1 ? "c" : c[0] < 1 ? "d" : "k";
  return {enun: T("Does ", "¿") + "<strong>" + txt + "</strong>" + T(" grow or decay?", " crece o decae?"), correcta: k, enOrden: true,
    opciones: [{clave: "c", html: T("it grows", "crece")}, {clave: "d", html: T("it decays", "decae")}, {clave: "k", html: T("it stays the same", "se mantiene igual")}],
    pista: T("Look only at the base, the number with the exponent x: more than 1, between 0 and 1, or exactly 1?", "Fíjese solo en la base, el número que lleva el exponente x: ¿mayor que 1, entre 0 y 1, o exactamente 1?"),
    bien: T("The base is " + c[1] + ": ", "La base es " + c[1] + ": ") + (k === "c" ? T("greater than 1, so it grows.", "mayor que 1, así que crece.") : k === "d" ? T("between 0 and 1, so it decays.", "entre 0 y 1, así que decae.") : T("1, so it never changes.", "1, así que nunca cambia.")) + (a !== 1 ? T(" The " + a + " in front is only the starting value.", " El " + a + " de adelante es solo el valor inicial.") : "")};
});

/* ===== MODULE 2 · Growth and decay in context ===== */
var CASOS = [
 {a: 100, b: 2, u: T("people", "habitantes"), p: T("years", "años"), m: "P(t) = 100 · 2<sup>t</sup>", ex: T("A town has 100 people, and its population doubles every year.", "Un pueblo tiene 100 habitantes y su población se duplica cada año.")},
 {a: 50, b: 3, u: T("bacteria", "bacterias"), p: T("hours", "horas"), m: "B(t) = 50 · 3<sup>t</sup>", ex: T("A culture starts with 50 bacteria and triples every hour.", "Un cultivo empieza con 50 bacterias y se triplica cada hora.")},
 {a: 80, b: .5, u: T("ounces", "onzas"), p: T("hours", "horas"), m: "M(t) = 80 · (0.5)<sup>t</sup>", ex: T("There are 80 ounces of a substance with a half-life of one hour: every hour, half is left.", "Hay 80 onzas de una sustancia cuya vida media es de una hora: cada hora queda la mitad.")},
 {a: 20000, b: .85, u: T("dollars", "dólares"), p: T("years", "años"), m: "V(t) = 20,000 · (0.85)<sup>t</sup>", ex: T("A car costs $20,000 and loses 15% of its value every year, so it keeps 85%.", "Un auto cuesta $20,000 y pierde el 15 % de su valor cada año, así que conserva el 85 %.")},
 {a: 200, b: .75, u: "mg", p: T("hours", "horas"), m: "D(t) = 200 · (0.75)<sup>t</sup>", ex: T("A 200 mg dose of a medicine leaves the body at 25% each hour: 75% of what was there is left.", "Una dosis de 200 mg de un medicamento se elimina a razón del 25 % cada hora: queda el 75 % de lo que había.")},
 {a: 500, b: 1.08, u: T("dollars", "dólares"), p: T("years", "años"), m: "A(t) = 500 · (1.08)<sup>t</sup>", ex: T("An account starts with $500 and grows 8% every year, so it is multiplied by 1.08.", "Una cuenta empieza con $500 y crece un 8 % cada año, es decir, se multiplica por 1.08.")}];
function caDibuja(){ var C = CASOS[+$("c-caso").value], tt = +$("c-t").value, din2 = C.u === T("dollars", "dólares"), f = function(v){ return din2 ? din(v) : dn(v) + " " + C.u; };
  $("c-tv").textContent = tt; $("c-enun").innerHTML = C.ex + " " + T("Model: ", "Modelo: ") + "<strong>" + C.m + "</strong>.";
  var filas = "", pts = [];
  for (var k = 0; k <= 8; k++){ var v = C.a * Math.pow(C.b, k); pts.push([k, v]); filas += "<tr><td" + (k === tt ? ' class="sel"' : "") + ">" + k + "</td><td" + (k === tt ? ' class="sel"' : "") + ">" + (k ? f(C.a * Math.pow(C.b, k - 1)) + " × " + C.b + " = " : "") + f(v) + "</td></tr>"; }
  $("c-tabla").innerHTML = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Period by period", "Período a período") + '</caption><thead><tr><th scope="col">t (' + C.p + ')</th><th scope="col">' + T("Amount", "Cantidad") + "</th></tr></thead><tbody>" + filas + "</tbody></table></div>";
  var top = Math.max.apply(null, pts.map(function(q){ return q[1]; }));
  $("c-graf").innerHTML = grafFun({rango: {x0: 0, x1: 8, y0: 0, y1: Math.ceil(top * 1.08)}, curvas: [{f: function(x){ return x >= 0 ? C.a * Math.pow(C.b, x) : NaN; }, color: "#90caf9"}], puntos: pts.map(function(q){ return [q[0], q[1], q[0] === tt ? "#c62828" : "#1565c0", q[0] === tt ? f(q[1]) : null, q[0] === tt ? 7 : 4.5, true, q[0] < 5]; }),
    voz: C.m.replace(/<\/?sup>/g, "") + ". " + T("After ", "Después de ") + tt + " " + C.p + ": " + f(C.a * Math.pow(C.b, tt)) + "."});
  $("c-txt").innerHTML = '<div class="linea">' + C.m.split(" = ")[0] + " → " + C.m.split(" = ")[1].replace("<sup>t</sup>", "<sup>" + tt + "</sup>") + " = <strong>" + f(C.a * Math.pow(C.b, tt)) + "</strong> " + T("after ", "después de ") + tt + " " + C.p + ". " + (C.b > 1 ? T("Growth: base greater than 1.", "Crecimiento: base mayor que 1.") : T("Decay: base between 0 and 1.", "Decaimiento: base entre 0 y 1.")) + "</div>"; }
$("c-caso").addEventListener("change", caDibuja); $("c-t").addEventListener("input", caDibuja); caDibuja();
OMR("cq", function(){ var t = aleatorio(0, 2);
  if (t === 0){ var b = elige([2, 3]), a = elige([10, 20, 50, 100, 250]), n = aleatorio(2, 5), r = a * Math.pow(b, n), nom = b === 2 ? T("doubles", "se duplica") : T("triples", "se triplica");
    return {enun: T("A colony of " + a + " bacteria " + nom + " every hour. How many are there after " + n + " hours?", "Una colonia de " + a + " bacterias " + nom + " cada hora. ¿Cuántas hay a las " + n + " horas?"), correcta: "ok",
      opciones: uniq([{clave: "ok", html: r.toLocaleString("en-US")}, {clave: "l", html: (a + a * b * n - a).toLocaleString("en-US")}, {clave: "m", html: (a * b * n).toLocaleString("en-US")}, {clave: "u", html: (a * Math.pow(b, n - 1)).toLocaleString("en-US")}]),
      pista: T("Multiply by " + b + " once for each hour: " + a + " · " + b + "<sup>" + n + "</sup>.", "Multiplique por " + b + " una vez por cada hora: " + a + " · " + b + "<sup>" + n + "</sup>."),
      bien: a + " · " + b + "<sup>" + n + "</sup> = " + a + " · " + Math.pow(b, n) + " = " + r.toLocaleString("en-US") + "."}; }
  if (t === 1){ var a1 = elige([64, 80, 96, 160, 200, 320]), n1 = aleatorio(1, 4), r1 = a1 / Math.pow(2, n1), h = elige([1, 2, 3, 5]);
    return {enun: T("A substance weighs " + a1 + " ounces, and its half-life is " + h + (h === 1 ? " hour" : " hours") + ". How much is left after " + n1 * h + " hours?", "Una sustancia pesa " + a1 + " onzas y su vida media es de " + h + (h === 1 ? " hora" : " horas") + ". ¿Cuánto queda tras " + n1 * h + " horas?"), correcta: "ok",
      opciones: uniq([{clave: "ok", html: dn(r1) + " oz"}, {clave: "s", html: dn(Math.max(a1 - a1 / 2 * n1 * h, 0)) + " oz"}, {clave: "u", html: dn(a1 / Math.pow(2, n1 * h)) + " oz"}, {clave: "m", html: dn(a1 / 2) + " oz"}]),
      pista: T(n1 * h + " hours are " + n1 + " half-lives: halve the amount " + n1 + (n1 === 1 ? " time." : " times."), n1 * h + " horas son " + n1 + (n1 === 1 ? " vida media" : " vidas medias") + ": reduzca la cantidad a la mitad " + n1 + (n1 === 1 ? " vez." : " veces.")),
      bien: n1 + T(" half-lives: ", " vidas medias: ") + a1 + " · (1/2)<sup>" + n1 + "</sup> = " + dn(r1) + T(" ounces.", " onzas.")}; }
  var p = elige([3, 4, 5, 6, 8, 10, 12, 15, 20, 25]), crece = Math.random() < .5, base = crece ? 1 + p / 100 : 1 - p / 100;
  return {enun: crece ? T("A quantity grows " + p + "% every year. What is the base of its model a · bᵗ?", "Una cantidad crece un " + p + " % cada año. ¿Cuál es la base de su modelo a · bᵗ?") : T("A quantity loses " + p + "% every year. What is the base of its model a · bᵗ?", "Una cantidad pierde un " + p + " % cada año. ¿Cuál es la base de su modelo a · bᵗ?"), correcta: "ok",
    opciones: uniq([{clave: "ok", html: dn(base)}, {clave: "o", html: dn(crece ? 1 - p / 100 : 1 + p / 100)}, {clave: "p", html: dn(p / 100)}, {clave: "e", html: String(p)}]),
    pista: crece ? T("It keeps 100% and adds " + p + "%: 1 + 0." + (p < 10 ? "0" : "") + p + ".", "Conserva el 100 % y suma el " + p + " %: 1 + 0." + (p < 10 ? "0" : "") + p + ".") : T("It keeps 100% − " + p + "% = " + (100 - p) + "%.", "Conserva el 100 % − " + p + " % = " + (100 - p) + " %."),
    bien: (crece ? "1 + " + dn(p / 100) : "1 − " + dn(p / 100)) + " = " + dn(base) + ". " + (crece ? T("A base greater than 1: growth.", "Base mayor que 1: crecimiento.") : T("A base between 0 and 1: decay.", "Base entre 0 y 1: decaimiento."))};
});

/* ===== MODULE 3 · Compound interest ===== */
var NOMN = {1: T("yearly", "anual"), 2: T("twice a year", "semestral"), 4: T("quarterly", "trimestral"), 12: T("monthly", "mensual"), 365: T("daily", "diaria")};
function inDibuja(){ var P = +$("i-p").value, r = +$("i-r").value, t = +$("i-t").value, n = +$("i-n").value;
  $("i-pv").textContent = "$" + P.toLocaleString("en-US"); $("i-rv").textContent = r + " %"; $("i-tv").textContent = t;
  var rd = r / 100, A = P * Math.pow(1 + rd / n, n * t), base = 1 + rd / n;
  $("i-txt").innerHTML = '<div class="linea">P = ' + P.toLocaleString("en-US") + ", r = " + r + " % = " + dn(rd, 4) + ", n = " + n + " (" + NOMN[n] + "), t = " + t + ".</div>" +
    '<div class="linea">A = ' + P.toLocaleString("en-US") + "(1 + " + dn(rd, 4) + "/" + n + ")<sup>" + n + "·" + t + "</sup> = " + P.toLocaleString("en-US") + "(" + dn(base, 6) + ")<sup>" + n * t + "</sup></div>" +
    '<div class="linea">(' + dn(base, 6) + ")<sup>" + n * t + "</sup> ≈ " + dn(Math.pow(base, n * t), 4) + " → <strong>A ≈ " + din(A) + "</strong>. " + T("Interest earned: ", "Interés ganado: ") + din(A - P) + ".</div>";
  $("i-tabla").innerHTML = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("The same money with different compounding", "El mismo dinero con distinta capitalización") + '</caption><thead><tr><th scope="col">' + T("Compounding", "Capitalización") + '</th><th scope="col">n</th><th scope="col">A</th></tr></thead><tbody>' +
    [1, 2, 4, 12, 365].map(function(k){ var v = P * Math.pow(1 + rd / k, k * t); return "<tr><td" + (k === n ? ' class="sel"' : "") + ">" + NOMN[k] + "</td><td" + (k === n ? ' class="sel"' : "") + ">" + k + "</td><td" + (k === n ? ' class="sel"' : "") + ">" + din(v) + "</td></tr>"; }).join("") +
    '<tr><td>' + T("simple interest (to compare)", "interés simple (para comparar)") + "</td><td>—</td><td>" + din(P * (1 + rd * t)) + "</td></tr></tbody></table></div>"; }
["i-p", "i-r", "i-t"].forEach(function(id){ $(id).addEventListener("input", inDibuja); }); $("i-n").addEventListener("change", inDibuja); inDibuja();
creaPracticaLibre("kq", function(){ var P = elige([500, 800, 1000, 1500, 2000, 2500, 5000]), r = elige([2, 3, 4, 5, 6, 8]), n = elige([1, 1, 2, 4, 12]), t = aleatorio(2, 10), rd = r / 100;
  var A = Math.round(P * Math.pow(1 + rd / n, n * t) * 100) / 100, simple = P * (1 + rd * t), interes = A - P;
  return {enun: T("$" + P.toLocaleString("en-US") + " is deposited at " + r + "% a year, compounded " + NOMN[n] + " (n = " + n + "), for " + t + " years. Use A = P(1 + r/n)<sup>nt</sup>. What is A, to the nearest cent?", "Se depositan $" + P.toLocaleString("en-US") + " al " + r + " % anual, con capitalización " + NOMN[n] + " (n = " + n + "), durante " + t + " años. Use A = P(1 + r/n)<sup>nt</sup>. ¿Cuánto es A, redondeado al centavo?"),
    evalua: function(txt){ var v = leeDecimal(String(txt).replace(/[$,\s]/g, "")); if (v === null) return {estado: "invalido", msg: T("Type an amount, such as 1628.89.", "Escriba una cantidad, como 1628.89.")};
      if (Math.abs(v - A) <= .011) return {estado: "bien"};
      if (Math.abs(v - simple) < .02) return {estado: "mal", msg: T("That is simple interest. Compound interest uses the power: (1 + r/n)<sup>nt</sup>.", "Eso es interés simple. El compuesto usa la potencia: (1 + r/n)<sup>nt</sup>.")};
      if (Math.abs(v - interes) <= .011) return {estado: "mal", msg: T("That is only the interest. A is the whole amount: add the $" + P.toLocaleString("en-US") + ".", "Eso es solo el interés. A es el monto total: sume los $" + P.toLocaleString("en-US") + ".")};
      if (v > A * 3) return {estado: "mal", msg: T("Write the rate as a decimal: " + r + "% = " + dn(rd, 2) + ".", "Escriba la tasa en decimal: " + r + " % = " + dn(rd, 2) + ".")};
      return {estado: "mal", msg: T("Check the exponent: n · t = " + n + " · " + t + " = " + n * t + ", and the base: 1 + " + dn(rd, 2) + "/" + n + ".", "Revise el exponente: n · t = " + n + " · " + t + " = " + n * t + ", y la base: 1 + " + dn(rd, 2) + "/" + n + ".")}; },
    solucion: "A = " + P.toLocaleString("en-US") + "(1 + " + dn(rd, 2) + "/" + n + ")<sup>" + n * t + "</sup> = " + P.toLocaleString("en-US") + "(" + dn(1 + rd / n, 6) + ")<sup>" + n * t + "</sup> ≈ <strong>" + din(A) + "</strong>."};
});

/* ===== MODULE 4 · The logarithm ===== */
function loDibuja(){ var b = +$("l-base").value, x = leeDecimal($("l-x").value), out = $("l-txt");
  var pot = ""; for (var k = 0; k <= 6; k++) pot += "<tr><td>" + b + "<sup>" + k + "</sup></td><td>" + Math.pow(b, k).toLocaleString("en-US") + "</td></tr>";
  $("l-tabla").innerHTML = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Powers of the base", "Potencias de la base") + '</caption><thead><tr><th scope="col">' + T("Power", "Potencia") + '</th><th scope="col">' + T("Value", "Valor") + "</th></tr></thead><tbody>" + pot + "</tbody></table></div>";
  if (x === null || x <= 0){ out.innerHTML = '<div class="linea">' + T("Type a positive number. (There is no logarithm of 0 or of a negative number: no power of a positive base gives them.)", "Escriba un número positivo. (No hay logaritmo de 0 ni de un número negativo: ninguna potencia de una base positiva los da.)") + "</div>"; return; }
  var y = Math.log(x) / Math.log(b), ent = Math.abs(y - Math.round(y)) < 1e-9;
  out.innerHTML = '<div class="linea">log<sub>' + b + "</sub>(" + dn(x, 4) + ") " + T("asks: to what exponent must I raise ", "pregunta: ¿a qué exponente hay que elevar ") + b + T(" to get ", " para obtener ") + dn(x, 4) + "?</div>" +
    '<div class="linea">' + (ent ? T("Since ", "Como ") + b + "<sup>" + Math.round(y) + "</sup> = " + dn(x, 4) + ", <strong>log<sub>" + b + "</sub>(" + dn(x, 4) + ") = " + Math.round(y) + "</strong>." :
      T(dn(x, 4) + " is not a whole power of " + b + ": the answer is between " + Math.floor(y) + " and " + Math.ceil(y) + ". With the calculator, log", dn(x, 4) + " no es una potencia entera de " + b + ": la respuesta está entre " + Math.floor(y) + " y " + Math.ceil(y) + ". Con la calculadora, log") + "<sub>" + b + "</sub>(" + dn(x, 4) + ") ≈ <strong>" + dn(y, 3) + "</strong>.") + "</div>"; }
$("l-base").addEventListener("change", loDibuja); $("l-x").addEventListener("input", loDibuja); loDibuja();
var PARES = [[2, 3], [3, 2], [10, 2], [5, 3], [10, 4], [2, 5]];
function paDibuja(){ var q = PARES[+$("l-par").value], v = Math.pow(q[0], q[1]);
  $("l-par-txt").innerHTML = '<div class="linea">' + T("Exponential form: ", "Forma exponencial: ") + "<strong>" + q[0] + "<sup>" + q[1] + "</sup> = " + v.toLocaleString("en-US") + "</strong></div>" + '<div class="linea">' + T("Logarithmic form: ", "Forma logarítmica: ") + "<strong>log<sub>" + q[0] + "</sub>(" + v.toLocaleString("en-US") + ") = " + q[1] + "</strong></div>" +
    '<div class="linea">' + T("The base stays the base; the exponent becomes the answer of the logarithm.", "La base sigue siendo la base; el exponente pasa a ser la respuesta del logaritmo.") + "</div>"; }
$("l-par").addEventListener("change", paDibuja); paDibuja();
OMR("lq", function(){ var t = aleatorio(0, 2), b = elige([2, 3, 5, 10]), k = aleatorio(b === 10 ? 1 : 2, b === 2 ? 6 : b === 10 ? 5 : 4), v = Math.pow(b, k);
  if (t === 0) return {enun: "log<sub>" + b + "</sub>(" + v.toLocaleString("en-US") + ") = ?", correcta: "ok", opciones: uniq([{clave: "ok", html: String(k)}, {clave: "v", html: (v / b).toLocaleString("en-US")}, {clave: "m", html: String(k + 1)}, {clave: "d", html: (v / 10 === Math.round(v / 10) && b !== 10 ? v / 10 : k * b).toLocaleString("en-US")}]),
    pista: T("Ask: " + b + " to what power gives " + v.toLocaleString("en-US") + "? Count how many times you multiply by " + b + ".", "Pregunte: ¿" + b + " a qué potencia da " + v.toLocaleString("en-US") + "? Cuente cuántas veces se multiplica por " + b + "."),
    bien: b + "<sup>" + k + "</sup> = " + v.toLocaleString("en-US") + ", log<sub>" + b + "</sub>(" + v.toLocaleString("en-US") + ") = " + k + "."};
  if (t === 1){ do { k = aleatorio(2, b === 10 ? 4 : 5); } while (k === b); v = Math.pow(b, k); }
  if (t === 1) return {enun: T("Write ", "Escriba ") + "<strong>" + b + "<sup>" + k + "</sup> = " + v.toLocaleString("en-US") + "</strong>" + T(" in logarithmic form.", " en forma logarítmica."), correcta: "ok",
    opciones: uniq([{clave: "ok", html: "log<sub>" + b + "</sub>(" + v.toLocaleString("en-US") + ") = " + k}, {clave: "a", html: "log<sub>" + k + "</sub>(" + v.toLocaleString("en-US") + ") = " + b}, {clave: "b", html: "log<sub>" + b + "</sub>(" + k + ") = " + v.toLocaleString("en-US")}, {clave: "c", html: "log<sub>" + v.toLocaleString("en-US") + "</sub>(" + b + ") = " + k}]),
    pista: T("The base stays the base, and the exponent is the answer of the logarithm.", "La base sigue siendo la base, y el exponente es la respuesta del logaritmo."), bien: T("Base " + b + ", answer (exponent) " + k + ".", "Base " + b + ", respuesta (exponente) " + k + ".")};
  var x = elige([10, 100, 1000, 10000, 100000, 1000000]), e = Math.round(Math.log10(x));
  return {enun: T("On the calculator you type log(" + x.toLocaleString("en-US") + "). What does it show?", "En la calculadora se escribe log(" + x.toLocaleString("en-US") + "). ¿Qué muestra?"), correcta: "ok",
    opciones: uniq([{clave: "ok", html: String(e)}, {clave: "z", html: String(x.toString().length)}, {clave: "d", html: (x / 10).toLocaleString("en-US")}, {clave: "m", html: String(e + 2)}]),
    pista: T("The log key is log base 10: count the zeros of " + x.toLocaleString("en-US") + ".", "La tecla log es el logaritmo base 10: cuente los ceros de " + x.toLocaleString("en-US") + "."), bien: "10<sup>" + e + "</sup> = " + x.toLocaleString("en-US") + "."};
});
'''

def practica_pagina():
    n = N
    rango = lambda i, et, mn, mx, st, v: f'<div class="campo"><label for="{i}">{et} <output id="{i}v"></output></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    casos = [("0", t("A population that doubles every year", "Población que se duplica cada año")), ("1", t("Bacteria that triple every hour", "Bacterias que se triplican cada hora")), ("2", t("A radioactive substance (half-life 1 hour)", "Sustancia radiactiva (vida media 1 hora)")),
             ("3", t("A car that loses 15% of its value a year", "Auto que pierde 15 % de valor al año")), ("4", t("A medicine that leaves the body at 25% an hour", "Medicamento que se elimina 25 % por hora")), ("5", t("Savings that grow 8% a year", "Ahorro que crece 8 % al año"))]
    ns = [("1", t("yearly (n = 1)", "anual (n = 1)")), ("2", t("twice a year (n = 2)", "semestral (n = 2)")), ("4", t("quarterly (n = 4)", "trimestral (n = 4)")), ("12", t("monthly (n = 12)", "mensual (n = 12)")), ("365", t("daily (n = 365)", "diaria (n = 365)"))]
    pares = [(str(i), f"{b}<sup>{k}</sup> = {b ** k:,}") for i, (b, k) in enumerate([(2, 3), (3, 2), (10, 2), (5, 3), (10, 4), (2, 5)])]
    pares = [(v, txt.replace("<sup>", "^").replace("</sup>", "")) for v, txt in pares]
    mods = [
     (t("exponential", "exponencial"), t("The exponential function f(x) = a · bˣ", "La función exponencial f(x) = a · bˣ"),
      f'''      <p>{t("Move the starting value a and the base b. The curve always passes through (0, a); each step to the right multiplies by b.", "Mueva el valor inicial a y la base b. La curva pasa siempre por (0, a); cada paso a la derecha multiplica por b.")}</p>
      <div class="panel"><div class="campos">{rango("e-a", "a =", 1, 8, 1, 2)}{rango("e-b", "b =", 0.25, 3, 0.25, 2)}</div></div>
{n4.salida("e-txt")}
      <div id="e-graf"></div>
{B.om("eq", t("Practice: does it grow or decay?", "Practique: ¿crece o decae?"))}'''),
     (t("context", "contexto"), t("Growth and decay in context", "Crecimiento y decaimiento en contexto"),
      f'''      <p>{t("Choose a situation and move the time. The table shows where each number comes from: the amount before, times the base.", "Elija una situación y mueva el tiempo. La tabla muestra de dónde sale cada número: la cantidad anterior por la base.")}</p>
      <div class="panel"><div class="campos">{n4.lista("c-caso", t("Situation", "Situación"), casos)}{rango("c-t", t("Periods t:", "Períodos t:"), 0, 8, 1, 3)}</div><p class="enun" id="c-enun"></p></div>
{n4.salida("c-txt")}
      <div id="c-graf"></div>
      <div id="c-tabla"></div>
{B.om("cq", t("Practice: the model", "Practique: el modelo"))}'''),
     (t("interest", "interes"), t("Compound interest", "El interés compuesto"),
      f'''{n4.formula("A = P(1 + r/n)<sup>nt</sup>")}
      <div class="panel"><div class="campos">{rango("i-p", "P =", 100, 10000, 100, 1000)}{rango("i-r", "r =", 1, 12, 0.5, 5)}{rango("i-t", t("t (years) =", "t (años) ="), 1, 30, 1, 10)}{n4.lista("i-n", t("Compounding", "Capitalización"), ns, "1")}</div></div>
{n4.salida("i-txt")}
      <div id="i-tabla"></div>
{B.libre("kq", t("Practice: compound interest", "Practique: interés compuesto"), t("A (in dollars)", "A (en dólares)"), nota=False)}
      <p class="nota">{t("Use the calculator. Type the amount with or without the $ sign, rounded to the cent.", "Use la calculadora. Escriba la cantidad con o sin el signo $, redondeada al centavo.")}</p>'''),
     (t("logarithm", "logaritmo"), t("A first look at the logarithm", "Introducción al logaritmo"),
      f'''      <p>{t("log<sub>b</sub>(x) asks: “to what exponent must I raise b to get x?” Choose a base and a number.", "log<sub>b</sub>(x) pregunta: «¿a qué exponente hay que elevar b para obtener x?» Elija una base y un número.")}</p>
      <div class="panel"><div class="campos">{n4.lista("l-base", t("Base b", "Base b"), [("2", "2"), ("3", "3"), ("5", "5"), ("10", "10")], "10")}<div class="campo"><label for="l-x">x =</label><input type="text" inputmode="decimal" autocomplete="off" id="l-x" value="1000" style="width:7em"></div></div></div>
{n4.salida("l-txt")}
      <div id="l-tabla"></div>
      <h3>{t("Two ways to write the same thing", "Las dos formas de escribir lo mismo")}</h3>
      <div class="panel"><div class="campos">{n4.lista("l-par", t("Power", "Potencia"), pares)}</div></div>
{n4.salida("l-par-txt")}
{B.om("lq", t("Practice: logarithms", "Practique: logaritmos"))}''')]
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Funciones exponenciales, crecimiento/decaimiento e introducción a logaritmos")
