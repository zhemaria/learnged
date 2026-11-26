"""Level 4 · Lesson 3.1 · Multiplying binomials: FOIL and special products — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_3-1.html and algebra/interactivo_3-1_multiplicacion_binomios (area model, FOIL,
the square of a binomial, sum times difference). They are rebuilt here, inside LearnGED, with typed answers read by math/poly4.js.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "3-1"
TEMA = ("Multiplying and factoring", "Multiplicación y factorización")
TIT = ("Multiplying binomials: FOIL and special products", "Multiplicación de binomios: FOIL e identidades notables")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def fig_area():
    s = ('<rect x="80" y="40" width="200" height="200" fill="#e3f2fd" stroke="#37474f" stroke-width="2.5"/>'
         '<rect x="280" y="40" width="100" height="200" fill="#fff8e1" stroke="#37474f" stroke-width="2.5"/>'
         '<rect x="80" y="240" width="200" height="60" fill="#e8f5e9" stroke="#37474f" stroke-width="2.5"/>'
         '<rect x="280" y="240" width="100" height="60" fill="#f3e5f5" stroke="#37474f" stroke-width="2.5"/>'
         '<text x="180" y="30" font-size="18" font-weight="700" text-anchor="middle" fill="#0d47a1">x</text><text x="330" y="30" font-size="18" font-weight="700" text-anchor="middle" fill="#0d47a1">5</text>'
         '<text x="68" y="145" font-size="18" font-weight="700" text-anchor="end" fill="#b71c1c">x</text><text x="68" y="276" font-size="18" font-weight="700" text-anchor="end" fill="#b71c1c">3</text>'
         '<text x="180" y="146" font-size="22" font-weight="700" text-anchor="middle">x²</text><text x="330" y="146" font-size="22" font-weight="700" text-anchor="middle">5x</text>'
         '<text x="180" y="277" font-size="22" font-weight="700" text-anchor="middle">3x</text><text x="330" y="277" font-size="22" font-weight="700" text-anchor="middle">15</text>'
         '<text x="230" y="335" font-size="18" font-weight="700" text-anchor="middle" fill="#10174f">x² + 5x + 3x + 15 = x² + 8x + 15</text>')
    return B.svg("0 0 460 350", t("A rectangle with sides (x + 5) across and (x + 3) down, split into four parts: x², 5x, 3x, and 15. The total area is x² + 8x + 15.",
                                  "Un rectángulo de lados (x + 5) a lo ancho y (x + 3) a lo alto, dividido en cuatro partes: x², 5x, 3x y 15. El área total es x² + 8x + 15."), s, 420)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 2.3.</strong> In Lesson 2.3 you multiplied a monomial by a polynomial with the distributive property. Now each factor has two terms: you multiply a <strong>binomial by a binomial</strong>. The idea is the same (each term of one factor multiplies each term of the other), organized with a method called FOIL.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 2.3 se multiplicó un monomio por un polinomio con la propiedad distributiva. Ahora cada factor tiene dos términos: se multiplica un <strong>binomio por un binomio</strong>. La idea sigue siendo la misma (cada término de un factor multiplica a cada término del otro), organizada con un método llamado FOIL.")}</p>
<p>{t("Multiplying (x + 3)(x + 5) is like finding the area of a rectangle with sides (x + 3) and (x + 5). Split the rectangle into four parts: the total area is the sum of the four areas.", "Multiplicar (x + 3)(x + 5) es como hallar el área de un rectángulo de lados (x + 3) y (x + 5). Si se divide ese rectángulo en cuatro partes, el área total es la suma de las cuatro áreas.")}</p>
{fig_area()}
<p>{t("The <strong>FOIL</strong> method puts those four multiplications in order. The letters tell you which pairs to multiply:", "El método <strong>FOIL</strong> ordena esas cuatro multiplicaciones. Sus siglas en inglés indican qué pares se multiplican:")}</p>
{tabla(t("What the letters FOIL mean", "Significado de las siglas FOIL"), t("What each letter of FOIL means when you multiply two binomials", "Qué significa cada letra de FOIL al multiplicar dos binomios"),
  [t("Letter", "Letra"), t("Stands for", "Significa"), t("Multiply", "Multiplica")],
  [["F", "First", t("the first terms of each binomial", "los primeros términos de cada binomio")], ["O", "Outer", t("the two terms on the outside", "los términos de los extremos")],
   ["I", "Inner", t("the two terms in the middle", "los términos del centro")], ["L", "Last", t("the last terms of each binomial", "los últimos términos de cada binomio")]])}
{enlace(n, t("area", "area"), t("the area model", "el modelo del área"), t("Fill in the four parts of the rectangle and add them.", "Complete las cuatro partes del rectángulo y súmelas."))}'''

    s2 = f'''{ejemplo(t("Example 1: multiply (x + 3)(x + 5).", "Ejemplo 1 · Multiplicar (x + 3)(x + 5)."),
  [("F", t("First:", "Primeros:"), "x · x = x²."), ("O", t("Outer:", "Externos:"), "x · 5 = 5x."), ("I", t("Inner:", "Internos:"), "3 · x = 3x."), ("L", t("Last:", "Últimos:"), "3 · 5 = 15."),
   ("✓", t("Combine the like terms (5x + 3x = 8x).", "Se combinan los términos semejantes (5x + 3x = 8x)."), "<strong>x² + 8x + 15</strong>.")])}
{ejemplo(t("Example 2: with numbers and signs. Multiply (2x − 1)(x + 4).", "Ejemplo 2 · Con coeficientes y signos. Multiplicar (2x − 1)(x + 4)."),
  [("F", "", "2x · x = 2x²."), ("O", "", "2x · 4 = 8x."), ("I", "", "−1 · x = −x."), ("L", "", "−1 · 4 = −4."),
   ("✓", t("Combine: 8x − x = 7x.", "Se combinan: 8x − x = 7x."), "<strong>2x² + 7x − 4</strong>.")])}
{caja("ojo", t("Watch the signs", "Cuide los signos"), t("<p>Each term carries its sign when you multiply. A negative times a positive is negative, and a negative times a negative is positive. The last step is always to combine the two middle terms (Outer + Inner).</p>", "<p>Cada término lleva su signo al multiplicar. Un negativo por un positivo da negativo, y un negativo por un negativo da positivo. El paso final siempre es combinar los dos términos del centro (Outer + Inner).</p>"))}
{practica("p1", t("Practice 1 — FOIL", "Práctica 1 — FOIL"), "(x + 1)(x + 4) = …", [("a", "x² + 4x + 4"), ("b", "x² + 5x + 5"), ("c", "x² + 5x + 4")])}
{practica("p2", t("Practice 2 — With a minus sign", "Práctica 2 — Con un signo menos"), "(x + 2)(x − 3) = …", [("a", "x² + x − 6"), ("b", "x² − x − 6"), ("c", "x² − x + 6")])}
{practica("p3", t("Practice 3 — With a coefficient", "Práctica 3 — Con un coeficiente"), "(2x + 1)(x + 2) = …", [("a", "2x² + 5x + 2"), ("b", "2x² + 3x + 2"), ("c", "2x² + 2x + 2")])}
{enlace(n, "foil", t("FOIL", "FOIL"), t("The four products step by step, then typed practice that names the mistake.", "Los cuatro productos paso a paso y después práctica escrita que nombra el error."))}'''

    s3 = f'''<p>{t("When a binomial is squared, FOIL always gives the same pattern. The shortcut is worth knowing by heart:", "Cuando un binomio se eleva al cuadrado, FOIL siempre produce el mismo patrón. Vale la pena saberse el atajo:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">(a + b)² = a² + 2ab + b² &nbsp;·&nbsp; (a − b)² = a² − 2ab + b²</p>
<p>{t("In words: the square of the first, plus (or minus) twice the product, plus the square of the second.", "En palabras: el cuadrado del primero, más (o menos) el doble del producto, más el cuadrado del segundo.")}</p>
{ejemplo(t("Example 3: expand (x + 5)².", "Ejemplo 3 · Desarrollar (x + 5)²."),
  [("1", t("Square of the first.", "Cuadrado del primero."), "x²."), ("2", t("Twice the product.", "Doble del producto."), "2 · x · 5 = 10x."), ("3", t("Square of the second.", "Cuadrado del segundo."), "5² = 25."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x² + 10x + 25</strong>.")])}
{ejemplo(t("Example 4: with a minus sign. Expand (x − 3)².", "Ejemplo 4 · Con resta. Desarrollar (x − 3)²."),
  [("1", t("Square of the first.", "Cuadrado del primero."), "x²."), ("2", t("Twice the product, with a minus sign.", "Doble del producto, con signo menos."), "−2 · x · 3 = −6x."), ("3", t("Square of the second.", "Cuadrado del segundo."), "3² = 9."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x² − 6x + 9</strong>.")])}
{caja("ojo", t("(x + 5)² is not x² + 25", "(x + 5)² no es x² + 25"), t("<p>Squaring a binomial is not squaring each term separately: the middle term, 2ab, is missing. Forgetting it is the most common mistake. And the last term is always positive: (−3)² = 9.</p>", "<p>Elevar un binomio al cuadrado no es elevar cada término por separado: falta el término del medio, 2ab. Olvidarlo es el error más frecuente. Y el último término siempre es positivo: (−3)² = 9.</p>"))}
{enlace(n, t("square", "cuadrado"), t("the square of a binomial", "el cuadrado de un binomio"), t("Build the three pieces: the square of the first, twice the product, and the square of the second.", "Construya las tres piezas: el cuadrado del primero, el doble del producto y el cuadrado del segundo."))}'''

    s4 = f'''<p>{t("When you multiply a sum and a difference of the same two terms, the middle terms cancel and a difference of squares is left:", "Cuando se multiplican una suma y una diferencia de los mismos términos, los términos del centro se cancelan y queda una diferencia de cuadrados:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">(a + b)(a − b) = a² − b²</p>
{ejemplo(t("Example 5: multiply (x + 7)(x − 7).", "Ejemplo 5 · Multiplicar (x + 7)(x − 7)."),
  [("1", t("Square of the first.", "Cuadrado del primero."), "x²."), ("2", t("The middle terms cancel.", "Los términos del centro se cancelan."), "+7x − 7x = 0."), ("3", t("Square of the second, with a minus sign.", "Cuadrado del segundo, con signo menos."), "−49."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x² − 49</strong>.")])}
{caja("tip", t("The shortcut saves time", "El atajo ahorra tiempo"), t("<p>When you recognize (a + b)(a − b), you can write a² − b² right away, without the four products of FOIL. This identity will be the key to factoring in the next lesson.</p>", "<p>Reconocer (a + b)(a − b) permite escribir el resultado directamente como a² − b², sin hacer los cuatro productos de FOIL. Esta identidad será clave para factorizar en la próxima lección.</p>"))}
{practica("p4", t("Practice 4 — A square", "Práctica 4 — Un cuadrado"), "(x + 3)² = …", [("a", "x² + 9"), ("b", "x² + 6x + 9"), ("c", "x² + 3x + 9")])}
{practica("p5", t("Practice 5 — Sum times difference", "Práctica 5 — Suma por diferencia"), "(x − 5)(x + 5) = …", [("a", "x² − 25"), ("b", "x² + 25"), ("c", "x² − 10x − 25")])}
{practica("p6", t("Practice 6 — A square with a coefficient", "Práctica 6 — Un cuadrado con coeficiente"), "(2x + 1)² = …", [("a", "2x² + 4x + 1"), ("b", "4x² + 1"), ("c", "4x² + 4x + 1")])}
{enlace(n, t("sum-difference", "suma-diferencia"), t("sum times difference", "la suma por diferencia"), t("Decide whether the shortcut applies, then write a² − b².", "Decida si se puede usar el atajo y después escriba a² − b²."))}'''

    secciones = [("s-" + t("area", "area"), t("The area model and FOIL", "El modelo del área y FOIL"), s1),
                 ("s-foil", t("FOIL step by step", "FOIL paso a paso"), s2),
                 ("s-" + t("square", "cuadrado"), t("Special product: the square of a binomial", "Identidad: el cuadrado de un binomio"), s3),
                 ("s-" + t("sum-difference", "suma-diferencia"), t("Special product: sum times difference", "Identidad: suma por diferencia"), s4)]

    lesson = {"next": t("Lesson 3.2", "Lección 3.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("O + I: 4x + x = 5x.", "O + I: 4x + x = 5x."), "b": t("L: 1 · 4 = 4, not 5.", "L: 1 · 4 = 4, no 5.")}, "right": "x² + 4x + x + 4 = x² + 5x + 4.", "solution": "x² + 5x + 4."},
      "p2": {"ok": "b", "hints": {"a": t("O + I: −3x + 2x = −x.", "O + I: −3x + 2x = −x."), "c": t("L: 2 · (−3) = −6.", "L: 2 · (−3) = −6.")}, "right": "x² − 3x + 2x − 6 = x² − x − 6.", "solution": "x² − x − 6."},
      "p3": {"ok": "a", "hints": {"b": t("O + I: 2x · 2 = 4x and 1 · x = x, so 5x.", "O + I: 2x · 2 = 4x y 1 · x = x, así que 5x."), "c": t("O + I: 4x + x = 5x.", "O + I: 4x + x = 5x.")}, "right": "2x² + 4x + x + 2 = 2x² + 5x + 2.", "solution": "2x² + 5x + 2."},
      "p4": {"ok": "b", "hints": {"a": t("The middle term 2ab is missing.", "Falta el término del medio, 2ab."), "c": t("Twice the product: 2 · x · 3 = 6x.", "El doble del producto: 2 · x · 3 = 6x.")}, "right": "x² + 2 · 3x + 9 = x² + 6x + 9.", "solution": "x² + 6x + 9."},
      "p5": {"ok": "a", "hints": {"b": t("The last term is −5 · 5 = −25.", "El último término es −5 · 5 = −25."), "c": t("The middle terms cancel: −5x + 5x = 0.", "Los términos del centro se cancelan: −5x + 5x = 0.")}, "right": "x² − 25.", "solution": "x² − 25."},
      "p6": {"ok": "c", "hints": {"a": t("The first term squared: (2x)² = 4x².", "El primer término al cuadrado: (2x)² = 4x²."), "b": t("The middle term 2 · 2x · 1 = 4x is missing.", "Falta el término del medio: 2 · 2x · 1 = 4x.")}, "right": "(2x)² + 2 · 2x · 1 + 1 = 4x² + 4x + 1.", "solution": "4x² + 4x + 1."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("O + I: 3x + 2x = 5x; L: 2 · 3 = 6.", "O + I: 3x + 2x = 5x; L: 2 · 3 = 6."), "c": t("The middle terms are missing.", "Faltan los términos del centro."), "d": t("L: 2 · 3 = 6.", "L: 2 · 3 = 6.")}, "solution": "x² + 5x + 6."},
      "B": {"ok": "d", "hints": {"a": t("O + I: −x + 4x = +3x.", "O + I: −x + 4x = +3x."), "b": t("L: 4 · (−1) = −4.", "L: 4 · (−1) = −4."), "c": t("O + I: −x + 4x = 3x, not −4x.", "O + I: −x + 4x = 3x, no −4x.")}, "solution": "x² + 3x − 4."},
      "C": {"ok": "c", "hints": {"a": t("O: 2x · 5 = 10x; I: 1 · x = x.", "O: 2x · 5 = 10x; I: 1 · x = x."), "b": t("Add the inner product too: 10x + x = 11x.", "Sume también el producto interno: 10x + x = 11x."), "d": t("F: 2x · x = 2x².", "F: 2x · x = 2x².")}, "solution": "2x² + 11x + 5."},
      "D": {"ok": "a", "hints": {"b": t("O + I: 12x − 2x = +10x.", "O + I: 12x − 2x = +10x."), "c": t("O: 3x · 4 = 12x; I: −2 · x = −2x.", "O: 3x · 4 = 12x; I: −2 · x = −2x."), "d": t("L: −2 · 4 = −8.", "L: −2 · 4 = −8.")}, "solution": "3x² + 10x − 8."},
      "E": {"ok": "d", "hints": {"a": t("O + I: −2x − 5x = −7x.", "O + I: −2x − 5x = −7x."), "b": t("L: (−5)(−2) = +10.", "L: (−5)(−2) = +10."), "c": t("O + I: −2x − 5x = −7x.", "O + I: −2x − 5x = −7x.")}, "solution": "x² − 7x + 10."},
      "F": {"ok": "c", "hints": {"a": t("The middle term 2ab is missing.", "Falta el término del medio, 2ab."), "b": t("Twice the product: 2 · 6x = 12x.", "El doble del producto: 2 · 6x = 12x."), "d": t("The square of the second: 6² = 36.", "El cuadrado del segundo: 6² = 36.")}, "solution": "x² + 12x + 36."},
      "G": {"ok": "c", "hints": {"a": t("(2x)² = 4x², not 2x².", "(2x)² = 4x², no 2x²."), "b": t("The middle term 2 · 2x · 3 = 12x is missing.", "Falta el término del medio: 2 · 2x · 3 = 12x."), "d": t("Twice the product: 2 · 2x · 3 = 12x.", "El doble del producto: 2 · 2x · 3 = 12x.")}, "solution": "4x² + 12x + 9."},
      "H": {"ok": "b", "hints": {"a": t("The last term is negative: 5 · (−5).", "El último término es negativo: 5 · (−5)."), "c": t("(3x)² = 9x².", "(3x)² = 9x²."), "d": t("The middle terms cancel; the last is −25.", "Los del centro se cancelan; el último es −25.")}, "solution": "9x² − 25."},
     }}

    quiz = [
     ("A", "(x + 2)(x + 3) = …", [("a", "x² + 6x + 5"), ("b", "x² + 5x + 6"), ("c", "x² + 6"), ("d", "x² + 5x + 5")]),
     ("B", "(x + 4)(x − 1) = …", [("a", "x² − 3x − 4"), ("b", "x² + 3x + 4"), ("c", "x² − 4x − 4"), ("d", "x² + 3x − 4")]),
     ("C", "(2x + 1)(x + 5) = …", [("a", "2x² + 6x + 5"), ("b", "2x² + 10x + 5"), ("c", "2x² + 11x + 5"), ("d", "3x² + 11x + 5")]),
     ("D", "(3x − 2)(x + 4) = …", [("a", "3x² + 10x − 8"), ("b", "3x² − 10x − 8"), ("c", "3x² + 14x − 8"), ("d", "3x² + 10x + 8")]),
     ("E", "(x − 5)(x − 2) = …", [("a", "x² + 7x + 10"), ("b", "x² − 7x − 10"), ("c", "x² − 3x + 10"), ("d", "x² − 7x + 10")]),
     ("F", "(x + 6)² = …", [("a", "x² + 36"), ("b", "x² + 6x + 36"), ("c", "x² + 12x + 36"), ("d", "x² + 12x + 6")]),
     ("G", "(2x + 3)² = …", [("a", "2x² + 12x + 9"), ("b", "4x² + 9"), ("c", "4x² + 12x + 9"), ("d", "4x² + 6x + 9")]),
     ("H", "(3x + 5)(3x − 5) = …", [("a", "9x² + 25"), ("b", "9x² − 25"), ("c", "3x² − 25"), ("d", "9x² − 10")])]

    tarea = (t("For your own work, with your notebook open and no calculator: (1) Twelve products. Before you solve, sort each one as general FOIL, the square of a binomial, or sum times difference, then use the fastest method: (x + 3)(x + 5), (x − 4)(x + 2), (2x + 1)(x − 3), (x + 6)², (x − 7)², (3x + 2)², (x + 9)(x − 9), (2x − 5)(2x + 5), (x − 1)(x − 8), (4x + 3)(4x − 3), (x + 2y)², and (5x − 1)(x + 4). (2) Expand (x + 5)² two ways, with the whole FOIL and with the identity. Check that they match and point out where the 2ab term appears in FOIL. (3) Find the mistake: fix these three expansions and describe each mistake in one sentence: (x + 4)² = x² + 16; (x − 3)² = x² − 6x − 9; (x + 6)(x − 6) = x² − 12x − 36. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto y sin calculadora: (1) Doce productos. Antes de resolver, clasifique cada uno como FOIL general, cuadrado de un binomio o suma por diferencia, y después use el método más rápido: (x + 3)(x + 5), (x − 4)(x + 2), (2x + 1)(x − 3), (x + 6)², (x − 7)², (3x + 2)², (x + 9)(x − 9), (2x − 5)(2x + 5), (x − 1)(x − 8), (4x + 3)(4x − 3), (x + 2y)² y (5x − 1)(x + 4). (2) Desarrolle (x + 5)² de dos maneras, con FOIL completo y con la identidad. Compruebe que coinciden y señale dónde aparece el término 2ab en el desarrollo con FOIL. (3) Caza del error: corrija estos tres desarrollos y describa cada error en una frase: (x + 4)² = x² + 16; (x − 3)² = x² − 6x − 9; (x + 6)(x − 6) = x² − 12x − 36. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("A square room measures x feet on each side. You add a strip 3 feet wide along two sides, so the new room is (x + 3) by (x + 3). Draw it as an area model and find the new area: where are the 2ab pieces? Measure a real room and check your formula.",
               "Una habitación cuadrada mide x pies de lado. Se le añade una franja de 3 pies a lo largo de dos lados, así que la nueva habitación mide (x + 3) por (x + 3). Dibújela como un modelo de área y halle el área nueva: ¿dónde están las piezas 2ab? Mida una habitación real y compruebe su fórmula."))

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Multiply two binomials with the area model and FOIL, and use the shortcuts for the square of a binomial and for sum times difference.", "Multiplique dos binomios con el modelo del área y FOIL, y use los atajos del cuadrado de un binomio y de la suma por diferencia."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Multiply</strong> two binomials with the area model and with FOIL.", "<strong>Multiplicar</strong> dos binomios con el modelo del área y con FOIL."),
         t("<strong>Combine</strong> the middle terms and give the result in standard form.", "<strong>Combinar</strong> los términos del centro y dar el resultado ordenado."),
         t("<strong>Use</strong> the identity (a ± b)² = a² ± 2ab + b².", "<strong>Usar</strong> la identidad (a ± b)² = a² ± 2ab + b²."),
         t("<strong>Use</strong> the identity (a + b)(a − b) = a² − b².", "<strong>Usar</strong> la identidad (a + b)(a − b) = a² − b².")],
        secciones, tarea, quiz,
        t("Self-check checklist for multiplying binomials", "Lista de autoevaluación de la multiplicación de binomios"),
        t("Self-check checklist: skills for FOIL and special products", "Lista de autoevaluación: destrezas de FOIL y las identidades notables"),
        [(t("Using FOIL", "Aplicar FOIL"), t("I do the four products and combine the like terms with no mistakes.", "Hago los cuatro productos y combino los semejantes sin errores."), t("I do the four products but make sign mistakes.", "Hago los cuatro productos, pero con errores de signo."), t("I leave out one or more of the four products.", "Omito uno o más de los cuatro productos.")),
         (t("Using the special products", "Usar las identidades notables"), t("I recognize the identity, use the shortcut surely, and can say why it works.", "Reconozco la identidad, uso el atajo con seguridad y sé explicar por qué funciona."), t("I recognize it but forget the middle term or a sign.", "La reconozco, pero olvido el término del medio o un signo."), t("I do not recognize the identities.", "No reconozco las identidades.")),
         (t("Simplifying the result", "Simplificar el resultado"), t("I give the result in standard form and check it.", "Entrego el resultado ordenado y lo compruebo."), t("I combine some terms but make mistakes.", "Combino algunos términos, pero con errores."), t("I leave like terms without combining.", "Dejo términos semejantes sin combinar."))],
        t("<p>In this lesson you multiplied binomials with <strong>FOIL</strong> and used the <strong>special products</strong>: the square of a binomial, (a ± b)² = a² ± 2ab + b², and sum times difference, (a + b)(a − b) = a² − b².</p>\n<p>In <strong>Lesson 3.2 · Factoring: common factor and difference of squares</strong> you will go the other way: instead of multiplying to get a polynomial, you will <strong>break</strong> a polynomial into its factors. The identity a² − b² = (a + b)(a − b) will be the key to recognizing and factoring a difference of squares.</p>",
          "<p>En esta lección se multiplicaron binomios con <strong>FOIL</strong> y se usaron las <strong>identidades notables</strong>: el cuadrado de un binomio, (a ± b)² = a² ± 2ab + b², y la suma por diferencia, (a + b)(a − b) = a² − b².</p>\n<p>En la <strong>Lección 3.2 · Factorización: factor común y diferencia de cuadrados</strong> se recorrerá el camino inverso: en lugar de multiplicar para obtener un polinomio, se <strong>descompondrá</strong> un polinomio en sus factores. La identidad a² − b² = (a + b)(a − b) será la clave para reconocer y factorizar las diferencias de cuadrados.</p>"),
        ("3-2", ("", t("Lesson 3.2 · Factoring: common factor and difference of squares", "Lección 3.2 · Factorización: factor común y diferencia de cuadrados"))),
        [(t("binomial", "binomio"), t("A polynomial with two terms, like x + 3.", "Un polinomio de dos términos, como x + 3.")),
         ("FOIL", t("First, Outer, Inner, Last: the four products of two binomials.", "First, Outer, Inner, Last (primeros, externos, internos, últimos): los cuatro productos de dos binomios.")),
         (t("special product", "identidad notable"), t("A product with a pattern you can write right away.", "Un producto con un patrón que se puede escribir directamente.")),
         (t("perfect square trinomial", "trinomio cuadrado perfecto"), t("The result of squaring a binomial: a² ± 2ab + b².", "El resultado de elevar un binomio al cuadrado: a² ± 2ab + b².")),
         (t("difference of squares", "diferencia de cuadrados"), t("a² − b², the result of (a + b)(a − b).", "a² − b², el resultado de (a + b)(a − b)."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function bin(a, b){ return [b, a]; }                       /* ax + b */
function binVis(q){ return "(" + pVis(q) + ")"; }
function prodHTML(p1, p2, cuadrado){ return envuelve(cuadrado ? binVis(p1) + "<sup>2</sup>" : binVis(p1) + binVis(p2), cuadrado ? T("the quantity ", "la cantidad ") + pVoz(p1) + T(", squared", ", al cuadrado") : T("the quantity ", "la cantidad ") + pVoz(p1) + T(", times the quantity ", ", por la cantidad ") + pVoz(p2)); }
function tmv(c, g){ return tVis(c, g, true); }
function azarBin(conA){ var a = conA ? elige([1, 1, 2, 3]) : 1, b; do { b = aleatorio(-9, 9); } while (!b); return bin(a, b); }
function trampasProd(p1, p2){
  var a = p1[1], b = p1[0], c = p2[1], d = p2[0], ok = pMul(p1, p2), l = [];
  l.push({p: pDe({2: a * c, 0: b * d}), msg: T("The middle terms are missing: add the Outer and Inner products.", "Faltan los términos del centro: sume los productos externos (O) e internos (I).")});
  l.push({p: pDe({2: a * c, 1: a * d - b * c, 0: b * d}), msg: T("Check the sign of the Inner product (I): each term keeps its sign.", "Revise el signo del producto interno (I): cada término lleva su signo.")});
  l.push({p: pDe({2: a * c, 1: b * c - a * d, 0: b * d}), msg: T("Check the sign of the Outer product (O): each term keeps its sign.", "Revise el signo del producto externo (O): cada término lleva su signo.")});
  l.push({p: pDe({2: a * c, 1: a * d + b * c, 0: -b * d}), msg: T("Check the Last product (L): " + pn(b) + " · " + pn(d) + " = " + sg(b * d) + ".", "Revise el producto de los últimos (L): " + pn(b) + " · " + pn(d) + " = " + sg(b * d) + ".")});
  l.push({p: pDe({2: a + c, 1: a * d + b * c, 0: b * d}), msg: T("First (F): multiply the x terms, " + a + "x · " + c + "x = " + a * c + "x².", "Primeros (F): se multiplican los términos con x, " + a + "x · " + c + "x = " + a * c + "x².")});
  return l.filter(function(x){ return !pIgual(x.p, ok); });
}
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }

/* ===== MODULE 1 · The area model ===== */
var AR = {p1: null, p2: null, ver: false};
function areaSVG(p1, p2, ver){
  var a = p1[1], b = p1[0], c = p2[1], d = p2[0], W = 460, H = 340, x0 = 90, y0 = 50, wx = 190, wb = 90, hx = 170, hb = 70, s = "";
  var celdas = [[x0, y0, wx, hx, tmv(a * c, 2), "#e3f2fd"], [x0 + wx, y0, wb, hx, tmv(a * d, 1), "#fff8e1"], [x0, y0 + hx, wx, hb, tmv(b * c, 1), "#e8f5e9"], [x0 + wx, y0 + hx, wb, hb, sg(b * d), "#f3e5f5"]];
  celdas.forEach(function(q){ s += '<rect x="' + q[0] + '" y="' + q[1] + '" width="' + q[2] + '" height="' + q[3] + '" fill="' + q[5] + '" stroke="#37474f" stroke-width="2.5"/><text x="' + (q[0] + q[2] / 2) + '" y="' + (q[1] + q[3] / 2 + 8) + '" font-size="22" font-weight="700" text-anchor="middle">' + (ver ? q[4] : "?") + "</text>"; });
  s += '<text x="' + (x0 + wx / 2) + '" y="' + (y0 - 14) + '" font-size="19" font-weight="700" text-anchor="middle" fill="#0d47a1">' + tmv(c, 1) + '</text><text x="' + (x0 + wx + wb / 2) + '" y="' + (y0 - 14) + '" font-size="19" font-weight="700" text-anchor="middle" fill="#0d47a1">' + sg(d) + "</text>";
  s += '<text x="' + (x0 - 12) + '" y="' + (y0 + hx / 2 + 6) + '" font-size="19" font-weight="700" text-anchor="end" fill="#b71c1c">' + tmv(a, 1) + '</text><text x="' + (x0 - 12) + '" y="' + (y0 + hx + hb / 2 + 6) + '" font-size="19" font-weight="700" text-anchor="end" fill="#b71c1c">' + sg(b) + "</text>";
  return '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("Area model: a rectangle with sides ", "Modelo del área: un rectángulo de lados ") + pVoz(p2) + T(" across and ", " a lo ancho y ") + pVoz(p1) + T(" down, split into four parts", " a lo alto, dividido en cuatro partes") + (ver ? ": " + [tmv(a * c, 2), tmv(a * d, 1), tmv(b * c, 1), sg(b * d)].join(", ").replace(/<[^>]+>/g, "") : "") + '." style="max-width:440px">' + s.replace(/<sup>/g, '<tspan baseline-shift="super" font-size="14">').replace(/<\/sup>/g, "</tspan>") + "</svg>";
}
function arPinta(){ $("ar-svg").innerHTML = areaSVG(AR.p1, AR.p2, AR.ver); }
creaPracticaLibre("ar", function(){
  AR.p1 = azarBin(Math.random() < .4); AR.p2 = azarBin(false); AR.ver = false; arPinta();
  var ok = pMul(AR.p1, AR.p2), a = AR.p1[1], b = AR.p1[0], c = AR.p2[1], d = AR.p2[0];
  return {enun: T("Find the area of the rectangle: ", "Halle el área del rectángulo: ") + prodHTML(AR.p1, AR.p2) + T(". Find the four parts, add them, and combine the like terms. Use ^ for exponents: x^2.", ". Calcule las cuatro partes, súmelas y combine los términos semejantes. Use ^ para los exponentes: x^2."),
    evalua: function(txt){ var r = evaluaP(txt, ok, trampasProd(AR.p1, AR.p2)); if (r.estado !== "invalido"){ AR.ver = r.estado === "bien"; arPinta(); } return r; },
    solucion: T("The four parts: ", "Las cuatro partes: ") + [tmv(a * c, 2), tmv(a * d, 1), tmv(b * c, 1), sg(b * d)].join(", ") + T(". The two middle ones are like terms: ", ". Las dos del centro son semejantes: ") + tmv(a * d, 1) + " + " + pn(b * c) + "x = " + tmv(a * d + b * c, 1) + ". " + T("Total: ", "Total: ") + pVis(ok) + "."};
});
$("ar-ver").addEventListener("click", function(){ AR.ver = true; arPinta(); });

/* ===== MODULE 2 · FOIL ===== */
function casoFOIL(){ var p1 = azarBin(true), p2 = azarBin(Math.random() < .3), a = p1[1], b = p1[0], c = p2[1], d = p2[0], ok = pMul(p1, p2);
  var C = function(l, col){ return '<strong style="color:' + col + '">' + l + "</strong> "; };
  return {p1: p1, p2: p2, ok: ok, pasos: [C("F", "#0d47a1") + T("First: ", "Primeros: ") + tmv(a, 1) + " · " + tmv(c, 1) + " = " + tmv(a * c, 2) + ".", C("O", "#e65100") + T("Outer: ", "Externos: ") + tmv(a, 1) + " · " + pn(d) + " = " + tmv(a * d, 1) + ".", C("I", "#2e7d32") + T("Inner: ", "Internos: ") + pn(b) + " · " + tmv(c, 1) + " = " + tmv(b * c, 1) + ".", C("L", "#6a1b9a") + T("Last: ", "Últimos: ") + pn(b) + " · " + pn(d) + " = " + sg(b * d) + ".", T("Combine O + I: ", "Se combinan O + I: ") + tmv(a * d, 1) + (b * c < 0 ? " − " + tmv(-b * c, 1) : " + " + tmv(b * c, 1)) + " = " + (a * d + b * c ? tmv(a * d + b * c, 1) : "0") + ". " + T("Result: ", "Resultado: ") + "<strong>" + pVis(ok) + "</strong>."]};
}
pasoAPaso4("fo", function(){ var c = casoFOIL(); return {enun: T("Multiply ", "Multiplique ") + prodHTML(c.p1, c.p2) + T(" with FOIL.", " con FOIL."), pasos: c.pasos}; });
creaPracticaLibre("fq", function(){ var c = casoFOIL();
  return {enun: T("Multiply ", "Multiplique ") + prodHTML(c.p1, c.p2) + T(". Use ^ for exponents: x^2.", ". Use ^ para los exponentes: x^2."), evalua: function(txt){ return evaluaP(txt, c.ok, trampasProd(c.p1, c.p2)); }, solucion: c.pasos.join(" ").replace(/<\/?strong[^>]*>/g, "")}; });

/* ===== MODULE 3 · The square of a binomial ===== */
function casoCuad(){ var a = elige([1, 1, 1, 2, 3]), b; do { b = aleatorio(-9, 9); } while (!b); var p1 = bin(a, b), ok = pMul(p1, p1);
  return {p1: p1, ok: ok, a: a, b: b, pasos: [T("Square of the first: ", "Cuadrado del primero: ") + (a === 1 ? "x²" : "(" + tmv(a, 1) + ")² = " + tmv(a * a, 2)) + ".", T("Twice the product, with its sign: ", "Doble del producto, con su signo: ") + "2 · " + tmv(a, 1) + " · " + pn(b) + " = " + tmv(2 * a * b, 1) + ".", T("Square of the second (always positive): ", "Cuadrado del segundo (siempre positivo): ") + pn(b) + "² = " + b * b + ".", T("Result: ", "Resultado: ") + "<strong>" + pVis(ok) + "</strong>."]};
}
pasoAPaso4("cu", function(){ var c = casoCuad(); return {enun: T("Expand ", "Desarrolle ") + prodHTML(c.p1, null, true) + ".", pasos: c.pasos}; });
creaPracticaLibre("cq", function(){ var c = casoCuad(), a = c.a, b = c.b;
  var tr = [{p: pDe({2: a * a, 0: b * b}), msg: T("The middle term 2ab is missing: squaring a binomial is not squaring each term.", "Falta el término del medio, 2ab: elevar un binomio al cuadrado no es elevar cada término.")},
    {p: pDe({2: a * a, 1: a * b, 0: b * b}), msg: T("The middle term is twice the product: 2ab.", "El término del medio es el doble del producto: 2ab.")},
    {p: pDe({2: a * a, 1: 2 * a * b, 0: -b * b}), msg: T("The square of the second is always positive.", "El cuadrado del segundo siempre es positivo.")},
    {p: pDe({2: a, 1: 2 * a * b, 0: b * b}), msg: T("Square the whole first term: (" + a + "x)² = " + a * a + "x².", "Eleve al cuadrado todo el primer término: (" + a + "x)² = " + a * a + "x².")}];
  return {enun: T("Expand ", "Desarrolle ") + prodHTML(c.p1, null, true) + T(". Use ^ for exponents: x^2.", ". Use ^ para los exponentes: x^2."), evalua: function(txt){ return evaluaP(txt, c.ok, tr.filter(function(x){ return !pIgual(x.p, c.ok); })); }, solucion: c.pasos.join(" ").replace(/<\/?strong>/g, "")}; });

/* ===== MODULE 4 · Sum times difference ===== */
var SD = {};
function sdNuevo(){
  var a = elige([1, 1, 2, 3, 4]), b = aleatorio(1, 9), es = Math.random() < .65, p1 = bin(a, b), p2 = es ? bin(a, -b) : (Math.random() < .5 ? bin(a, -b + elige([-1, 1, 2])) : bin(a + 1, -b));
  if (!es && p2[0] === 0) p2 = bin(a, -b - 1);
  if (Math.random() < .5){ var t1 = p1; p1 = p2; p2 = t1; }
  SD = {p1: p1, p2: p2, es: es && true, ok: pMul(p1, p2), paso: 1};
  $("sd-enun").innerHTML = T("The product is ", "El producto es ") + prodHTML(p1, p2) + ".";
  $("sd-fb").className = "fb"; $("sd-fb").innerHTML = ""; $("sd-paso2").hidden = true; $("sd-r").value = ""; $("sd-si").disabled = $("sd-no").disabled = false;
}
function sdDecide(si){
  var fb = $("sd-fb");
  if (si === SD.es){ fb.className = "fb bien"; fb.innerHTML = TX.bien + (SD.es ? T("Same terms, opposite signs: the shortcut works.", "Mismos términos y signos opuestos: el atajo funciona.") : T("The terms are not the same, so use FOIL.", "Los términos no son los mismos, así que hay que usar FOIL.")); $("sd-paso2").hidden = false; $("sd-paso2t").innerHTML = SD.es ? T("Step 2. Write the result with the identity: the square of the first minus the square of the second.", "Paso 2. Escriba el resultado con la identidad: el cuadrado del primero menos el cuadrado del segundo.") : T("Step 2. Multiply with FOIL and write the result.", "Paso 2. Multiplique con FOIL y escriba el resultado."); $("sd-si").disabled = $("sd-no").disabled = true; $("sd-r").focus(); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + T("Look again: for a sum times a difference, the two binomials have exactly the same terms and differ only in the sign in the middle.", "Mire otra vez: en una suma por diferencia, los dos binomios tienen exactamente los mismos términos y solo cambia el signo del medio."); }
}
$("sd-si").addEventListener("click", function(){ sdDecide(true); }); $("sd-no").addEventListener("click", function(){ sdDecide(false); });
$("sd-comprobar").addEventListener("click", function(){
  var a = SD.p1[1], b = SD.p1[0], r = evaluaP($("sd-r").value, SD.ok, SD.es ? [{p: pDe({2: a * a, 0: b * b}), msg: T("The second square is subtracted: a² − b².", "El segundo cuadrado se resta: a² − b².")}, {p: pDe({2: a * a, 1: -2 * Math.abs(a * b), 0: -b * b}), msg: T("The middle terms cancel: there is no x term.", "Los términos del centro se cancelan: no queda término con x.")}] : trampasProd(SD.p1, SD.p2)), fb = $("sd-fb");
  if (r.estado === "bien"){ fb.className = "fb bien"; fb.innerHTML = TX.bien + pVis(SD.ok) + "."; SD.bien = (SD.bien || 0) + 1; }
  else { fb.className = "fb pista"; fb.innerHTML = (r.estado === "invalido" ? "" : TX.todavia) + r.msg + (r.estado === "mal" ? " " + T("Answer: ", "Respuesta: ") + pVis(SD.ok) + "." : ""); }
});
$("sd-otro").addEventListener("click", sdNuevo); sdNuevo();
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    mods = [
     (t("area", "area"), t("Multiplying binomials: the area model", "Producto de binomios: modelo del área"),
      f'''      <p>{t("The product of two binomials is the area of a rectangle. Find the area of each of the four parts, add them, and combine the like terms. The two middle parts always hold like terms (both have x), so the total has only three terms.", "El producto de dos binomios es el área de un rectángulo. Calcule el área de cada una de las cuatro partes, súmelas y combine los términos semejantes. Las dos partes del centro siempre llevan términos semejantes (las dos tienen x), por eso el área total tiene solo tres términos.")}</p>
      <div id="ar-svg"></div>
      <div class="fila-btn"><button type="button" class="btn-sec" id="ar-ver">{t("Show the four parts", "Mostrar las cuatro partes")}</button></div>
{libre("ar", t("Practice: the total area", "Practique: el área total"), t("Area", "Área"))}'''),
     ("foil", t("Multiplying binomials with FOIL", "Producto de binomios usando FOIL"),
      f'''      <p>{t("F, O, I, L: First, Outer, Inner, Last. Each term carries its sign: if the binomial is (x − 4), the last term is −4, not 4, and that sign travels with the number in the O, I, and L products.", "F, O, I, L: primeros, externos, internos y últimos. Cada término lleva su signo: si el binomio es (x − 4), el último término es −4, no 4, y ese signo viaja con el número en los productos O, I y L.")}</p>
{n4.pasos("fo", t("Another product", "Otro producto"))}
{libre("fq", t("Practice: multiply with FOIL", "Practique: multiplique con FOIL"), t("Product", "Producto"))}'''),
     (t("square", "cuadrado"), t("Special product: the square of a binomial", "Identidad: el cuadrado de un binomio"),
      f'''{n4.formula("(a + b)² = a² + 2ab + b² · (a − b)² = a² − 2ab + b²")}
      <p>{t("Build the three pieces: the square of the first, twice the product (with its sign), and the square of the second.", "Construya las tres piezas: el cuadrado del primero, el doble del producto (con su signo) y el cuadrado del segundo.")}</p>
{n4.pasos("cu", t("Another square", "Otro cuadrado"))}
      <div class="caja-atencion"><strong>{t("The most common mistake:", "El error más frecuente:")}</strong> {t("writing (x + 5)² as x² + 25. The middle term, 2ab, is missing. Squaring a binomial is never squaring each term separately.", "escribir (x + 5)² como x² + 25. Falta el término del medio, 2ab. Elevar al cuadrado un binomio nunca es elevar al cuadrado cada término por separado.")}</div>
{libre("cq", t("Practice: expand the square", "Practique: desarrolle el cuadrado"), t("Result", "Resultado"))}'''),
     (t("sum-difference", "suma-diferencia"), t("Special product: sum times difference", "Identidad: suma por diferencia"),
      f'''{n4.formula("(a + b)(a − b) = a² − b²")}
      <p>{t("First decide whether the product is a sum times a difference. It is only when the two binomials have the same terms and differ only in the sign in the middle. If not, use FOIL.", "Primero decida si el producto es una suma por diferencia. Solo lo es cuando los dos binomios tienen los mismos términos y difieren únicamente en el signo del medio. Si no, hay que usar FOIL.")}</p>
      <div class="practica"><p class="enun" id="sd-enun"></p>
        <p><strong>{t("Step 1. Can you use the shortcut (a + b)(a − b) = a² − b²?", "Paso 1. ¿Se puede aplicar el atajo (a + b)(a − b) = a² − b²?")}</strong></p>
        <div class="fila-btn"><button type="button" class="btn-sec" id="sd-si">{t("Yes, it is a sum times a difference", "Sí, es suma por diferencia")}</button><button type="button" class="btn-sec" id="sd-no">{t("No, use FOIL", "No, hay que usar FOIL")}</button></div>
        <div id="sd-paso2" hidden><p><strong id="sd-paso2t"></strong></p>
          <div class="campos"><div class="campo"><label for="sd-r">{t("Result", "Resultado")}</label><input type="text" autocomplete="off" class="ancho" id="sd-r"></div></div>
          <div class="fila-btn"><button type="button" class="btn" id="sd-comprobar">{t("Check the result", "Comprobar el resultado")}</button></div></div>
        <div class="fb" id="sd-fb" role="status"></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="sd-otro">{t("New exercise", "Otro ejercicio")}</button></div></div>
      <div class="caja-tip">{t("Why it works: in FOIL, the Outer and Inner products are opposites and cancel. Only the square of the first minus the square of the second is left.", "Por qué funciona: con FOIL, los productos externo e interno son opuestos y se cancelan. Queda solo el cuadrado del primero menos el cuadrado del segundo.")}</div>''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Multiplicación de binomios: FOIL e identidades notables")
