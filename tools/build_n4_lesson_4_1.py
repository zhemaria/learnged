"""Level 4 · Lesson 4.1 · Solving quadratic equations by factoring — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_4-1.html, algebra/4-1_resolver_por_factorizacion (zero product property, the five steps,
word problems) and algebra/n4-l4-1.html (standard form first). They are rebuilt here, inside LearnGED, with typed solutions read by
math/poly4.js (leeSol, evaluaSol). US units only. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "4-1"
TEMA = ("Quadratic equations", "Ecuaciones cuadráticas")
TIT = ("Solving quadratic equations by factoring", "Resolver ecuaciones cuadráticas por factorización")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Topic 3.</strong> In Topic 3 you learned to <strong>factor</strong> polynomials. Now that skill gets a powerful purpose: <strong>solving equations</strong>. A quadratic equation is an equation with an x² term; solving it means finding the values of x that make it true. Factoring, together with a very simple property of the number zero, opens the door to those solutions.",
 "<strong>Conexión con el tema anterior.</strong> En el Tema 3 se aprendió a <strong>factorizar</strong> polinomios. Esa destreza ahora cobra un propósito poderoso: <strong>resolver ecuaciones</strong>. Una ecuación cuadrática es una igualdad con un término x²; resolverla significa hallar los valores de x que la hacen cierta. La factorización, junto con una propiedad muy sencilla del número cero, abre la puerta a esas soluciones.")}</p>
<p>{t("Zero has a property in multiplication that no other number has:", "El número cero tiene una propiedad única en la multiplicación:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">{t("If A · B = 0, then A = 0 or B = 0.", "Si A · B = 0, entonces A = 0 o B = 0.")}</p>
<p>{t("In words: if the product of two quantities is zero, at least one of them <strong>has to</strong> be zero. There is no other way for a product to be zero.", "En palabras: si el producto de dos cantidades es cero, al menos una de ellas <strong>tiene</strong> que ser cero. No hay otra manera de que un producto dé cero.")}</p>
{caja("tip", t("The idea with numbers", "Idea con números"), t("<p>If 7 · B = 0, what is B? It has to be 0, because 7 is not zero. The same happens with factors that contain x: if (x − 2)(x + 5) = 0, then x − 2 = 0 or x + 5 = 0, so x = 2 or x = −5.</p>", "<p>Si 7 · B = 0, ¿cuánto vale B? Necesariamente B = 0, porque 7 no es cero. Lo mismo ocurre con factores que contienen x: si (x − 2)(x + 5) = 0, entonces x − 2 = 0 o x + 5 = 0, es decir, x = 2 o x = −5.</p>"))}
{caja("ojo", t("The key is the zero", "La clave es el cero"), t("<p>This property only works when the product <strong>equals zero</strong>. If a product equals 12, the factors could be 3 and 4, 2 and 6, 24 and 0.5… That is why the equation must equal zero (standard form) before you use it.</p>", "<p>Esta propiedad solo funciona cuando el producto es <strong>igual a cero</strong>. Si un producto da 12, los factores podrían ser 3 y 4, 2 y 6, 24 y 0.5… Por eso, antes de aplicarla, la ecuación debe estar igualada a cero (forma estándar).</p>"))}
{enlace(n, t("zero", "cero"), t("the zero product property", "la propiedad del producto cero"), t("Decide whether you can already use the property, and go from the factors to the solutions.", "Decida si ya se puede aplicar la propiedad y pase de los factores a las soluciones."))}'''

    s2 = f'''<p>{t("To solve a quadratic equation by factoring, always follow these steps:", "Para resolver una ecuación cuadrática por factorización se sigue siempre este procedimiento:")}</p>
{tabla(t("The five steps", "Los cinco pasos"), t("The five steps to solve a quadratic equation by factoring", "Los cinco pasos para resolver una ecuación cuadrática por factorización"), [t("Step", "Paso"), t("What to do", "Acción")],
  [["1", t("Write the equation in standard form: ax² + bx + c = 0.", "Llevar la ecuación a la forma estándar: ax² + bx + c = 0.")], ["2", t("Factor the left side.", "Factorizar el lado izquierdo.")], ["3", t("Set each factor equal to zero.", "Igualar cada factor a cero.")], ["4", t("Solve each linear equation.", "Resolver cada ecuación lineal.")], ["5", t("Check both solutions in the original equation.", "Verificar ambas soluciones en la ecuación original.")]])}
{ejemplo(t("Example 1: solve x² + 5x + 6 = 0.", "Ejemplo 1 · Resolver x² + 5x + 6 = 0."),
  [("1", t("It is already in standard form.", "Ya está en forma estándar."), ""), ("2", t("Factor.", "Se factoriza."), "(x + 2)(x + 3) = 0."), ("3", t("Each factor equals zero.", "Se iguala cada factor a cero."), t("x + 2 = 0 or x + 3 = 0.", "x + 2 = 0 o x + 3 = 0.")), ("4", t("Solve.", "Se resuelve."), t("x = −2 or x = −3.", "x = −2 o x = −3.")),
   ("5", t("Check.", "Verificación."), t("(−2)² + 5(−2) + 6 = 4 − 10 + 6 = 0. Right.", "(−2)² + 5(−2) + 6 = 4 − 10 + 6 = 0. Correcto.")), ("✓", t("Solutions.", "Soluciones."), t("<strong>x = −2 and x = −3</strong>.", "<strong>x = −2 y x = −3</strong>."))])}
{ejemplo(t("Example 2: with a difference of squares. Solve x² − 9 = 0.", "Ejemplo 2 · Con diferencia de cuadrados. Resolver x² − 9 = 0."),
  [("1", t("It is already in standard form.", "Ya está en forma estándar."), ""), ("2", t("Factor.", "Se factoriza."), "(x + 3)(x − 3) = 0."), ("3", t("Each factor equals zero.", "Se iguala cada factor a cero."), t("x + 3 = 0 or x − 3 = 0.", "x + 3 = 0 o x − 3 = 0.")),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = −3 and x = 3</strong>.", "<strong>x = −3 y x = 3</strong>."))])}
{practica("p1", t("Practice 1 — x² + 7x + 12 = 0", "Práctica 1 — x² + 7x + 12 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = 3 and x = 4", "x = 3 y x = 4")), ("b", t("x = −3 and x = 4", "x = −3 y x = 4")), ("c", t("x = −3 and x = −4", "x = −3 y x = −4"))])}
{practica("p2", t("Practice 2 — x² − x − 6 = 0", "Práctica 2 — x² − x − 6 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = 3 and x = −2", "x = 3 y x = −2")), ("b", t("x = −3 and x = 2", "x = −3 y x = 2")), ("c", t("x = 3 and x = 2", "x = 3 y x = 2"))])}
{practica("p3", t("Practice 3 — x² − 25 = 0", "Práctica 3 — x² − 25 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = 5 only", "x = 5 solamente")), ("b", t("x = 5 and x = −5", "x = 5 y x = −5")), ("c", t("x = 25 and x = −25", "x = 25 y x = −25"))])}
{enlace(n, t("steps", "pasos"), t("the five steps", "los cinco pasos"), t("See the five steps one at a time, then solve on your own and type both solutions.", "Vea los cinco pasos uno a uno y después resuelva por su cuenta escribiendo las dos soluciones."))}'''

    s3 = f'''<p>{t("Many equations do not come equal to zero. <strong>Step 1</strong> is always to rearrange them, moving every term to one side. When a term moves to the other side, its sign changes, because you do the same operation on both sides.", "Muchas ecuaciones no vienen igualadas a cero. El <strong>paso 1</strong> es siempre reorganizarlas pasando todos los términos a un lado. Al pasar un término al otro lado, cambia de signo, porque se hace la misma operación en ambos lados.")}</p>
{ejemplo(t("Example 3: solve x² = 9.", "Ejemplo 3 · Resolver x² = 9."),
  [("1", t("Standard form.", "Forma estándar."), "x² − 9 = 0."), ("2", t("Factor.", "Se factoriza."), "(x + 3)(x − 3) = 0."), ("✓", t("Solutions.", "Soluciones."), t("<strong>x = 3 and x = −3</strong>.", "<strong>x = 3 y x = −3</strong>."))])}
{ejemplo(t("Example 4: zero as a solution. Solve x² = 5x.", "Ejemplo 4 · El cero como solución. Resolver x² = 5x."),
  [("1", t("Standard form.", "Forma estándar."), "x² − 5x = 0."), ("2", t("Common factor.", "Factor común."), "x(x − 5) = 0."), ("3", t("Each factor equals zero.", "Cada factor igual a cero."), t("x = 0 or x − 5 = 0.", "x = 0 o x − 5 = 0.")),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = 0 and x = 5</strong>.", "<strong>x = 0 y x = 5</strong>."))])}
{caja("ojo", t("Do not divide by x", "No divida entre x"), t("<p>In x² = 5x, dividing both sides by x would lose the solution x = 0. Always move everything to one side and factor; that way you do not lose any solution.</p>", "<p>En x² = 5x, dividir ambos lados entre x haría perder la solución x = 0. Siempre se lleva todo a un lado y se factoriza; así no se pierde ninguna solución.</p>"))}
{practica("p4", t("Practice 4 — x² = 16", "Práctica 4 — x² = 16"), t("Rearrange to standard form and solve.", "Reorganice a forma estándar y resuelva."), [("a", t("x = 4 only", "x = 4 solamente")), ("b", t("x = 16 and x = −16", "x = 16 y x = −16")), ("c", t("x = 4 and x = −4", "x = 4 y x = −4"))])}
{practica("p5", t("Practice 5 — x² = 3x", "Práctica 5 — x² = 3x"), t("Rearrange to standard form and solve.", "Reorganice a forma estándar y resuelva."), [("a", t("x = 3 only", "x = 3 solamente")), ("b", t("x = 0 and x = 3", "x = 0 y x = 3")), ("c", t("x = 3 and x = −3", "x = 3 y x = −3"))])}
{practica("p6", t("Practice 6 — x² + 2x = 8", "Práctica 6 — x² + 2x = 8"), t("Rearrange to standard form and solve.", "Reorganice a forma estándar y resuelva."), [("a", t("x = −4 and x = 2", "x = −4 y x = 2")), ("b", t("x = 4 and x = −2", "x = 4 y x = −2")), ("c", t("x = −4 and x = −2", "x = −4 y x = −2"))])}
{enlace(n, t("standard-form", "forma-estandar"), t("standard form first", "la forma estándar primero"), t("Watch the typical mistake of factoring without the zero, move terms across, and solve.", "Observe el error típico de factorizar sin el cero, pase términos de un lado a otro y resuelva."))}'''

    s4 = f'''<p>{t("Quadratic equations model real situations, especially of area and motion. In these problems you must <strong>interpret</strong> the solutions: sometimes one of them makes no sense in the situation.", "Las ecuaciones cuadráticas modelan situaciones reales, especialmente de área y de movimiento. En estos problemas hay que <strong>interpretar</strong> las soluciones: a veces una de ellas no tiene sentido en el contexto.")}</p>
{ejemplo(t("Example 5: the area of a rectangle is 54 square feet. The length is 3 feet more than the width. How long is each side?", "Ejemplo 5 · El área de un rectángulo es de 54 pies cuadrados. El largo mide 3 pies más que el ancho. ¿Cuánto mide cada lado?"),
  [("1", t("Let x be the width. The length is x + 3.", "Sea x el ancho. El largo es x + 3."), t("Area: x(x + 3) = 54.", "Área: x(x + 3) = 54.")), ("2", t("Standard form.", "Forma estándar."), "x² + 3x − 54 = 0."), ("3", t("Factor.", "Se factoriza."), "(x + 9)(x − 6) = 0."), ("4", t("Solve.", "Se resuelve."), t("x = −9 or x = 6.", "x = −9 o x = 6.")),
   ("5", t("Interpret.", "Se interpreta."), t("A length cannot be negative, so x = 6.", "Una longitud no puede ser negativa, así que x = 6.")), ("✓", t("Answer.", "Respuesta."), t("<strong>The width is 6 feet and the length, 9 feet.</strong>", "<strong>El ancho mide 6 pies y el largo, 9 pies.</strong>"))])}
{caja("ojo", t("Interpret the situation", "Interprete el contexto"), t("<p>In problems about lengths, times, or amounts, throw out negative solutions or solutions that make no physical sense. Always ask: is this solution possible in the real situation?</p>", "<p>En problemas de longitudes, tiempos o cantidades, se descartan las soluciones negativas o sin sentido físico. Siempre vale la pena preguntarse: ¿esta solución es posible en la situación real?</p>"))}
{enlace(n, t("apply", "aplica"), t("word problems", "problemas aplicados"), t("Write the equation, solve it by factoring, and decide which of the two solutions makes sense.", "Plantee la ecuación, resuélvala por factorización y decida cuál de las dos soluciones tiene sentido."))}'''

    secciones = [("s-" + t("zero", "cero"), t("The zero product property", "La propiedad del producto cero"), s1),
                 ("s-" + t("steps", "pasos"), t("The five steps", "Los cinco pasos"), s2),
                 ("s-" + t("standard-form", "forma-estandar"), t("Standard form first", "Llevar a la forma estándar primero"), s3),
                 ("s-" + t("apply", "aplica"), t("Applications: area problems", "Aplicación: problemas de área"), s4)]

    lesson = {"next": t("Lesson 4.2", "Lección 4.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Substitute x = 3: 9 + 21 + 12 is not 0.", "Sustituya x = 3: 9 + 21 + 12 no es 0."), "b": t("(x + 3)(x + 4) = 0: each factor gives a negative value.", "(x + 3)(x + 4) = 0: cada factor da un valor negativo.")}, "right": t("(x + 3)(x + 4) = 0, so x = −3 or x = −4.", "(x + 3)(x + 4) = 0, así que x = −3 o x = −4."), "solution": t("x = −3 and x = −4.", "x = −3 y x = −4.")},
      "p2": {"ok": "a", "hints": {"b": t("(x − 3)(x + 2) = 0: x − 3 = 0 gives x = 3.", "(x − 3)(x + 2) = 0: x − 3 = 0 da x = 3."), "c": t("Substitute x = 2: 4 − 2 − 6 = −4, not 0.", "Sustituya x = 2: 4 − 2 − 6 = −4, no 0.")}, "right": t("(x − 3)(x + 2) = 0, so x = 3 or x = −2.", "(x − 3)(x + 2) = 0, así que x = 3 o x = −2."), "solution": t("x = 3 and x = −2.", "x = 3 y x = −2.")},
      "p3": {"ok": "b", "hints": {"a": t("(−5)² is also 25.", "(−5)² también es 25."), "c": t("25² is 625, not 25.", "25² es 625, no 25.")}, "right": t("(x + 5)(x − 5) = 0, so x = 5 or x = −5.", "(x + 5)(x − 5) = 0, así que x = 5 o x = −5."), "solution": t("x = 5 and x = −5.", "x = 5 y x = −5.")},
      "p4": {"ok": "c", "hints": {"a": t("(−4)² is also 16.", "(−4)² también es 16."), "b": t("16² is 256, not 16.", "16² es 256, no 16.")}, "right": t("x² − 16 = 0, (x + 4)(x − 4) = 0.", "x² − 16 = 0, (x + 4)(x − 4) = 0."), "solution": t("x = 4 and x = −4.", "x = 4 y x = −4.")},
      "p5": {"ok": "b", "hints": {"a": t("Do not divide by x: you lose x = 0.", "No divida entre x: se pierde x = 0."), "c": t("Substitute x = −3: 9 = −9 is false.", "Sustituya x = −3: 9 = −9 es falso.")}, "right": t("x² − 3x = 0, x(x − 3) = 0.", "x² − 3x = 0, x(x − 3) = 0."), "solution": t("x = 0 and x = 3.", "x = 0 y x = 3.")},
      "p6": {"ok": "a", "hints": {"b": t("(x + 4)(x − 2) = 0: x + 4 = 0 gives x = −4.", "(x + 4)(x − 2) = 0: x + 4 = 0 da x = −4."), "c": t("Substitute x = −2: 4 − 4 = 0, not 8.", "Sustituya x = −2: 4 − 4 = 0, no 8.")}, "right": t("x² + 2x − 8 = 0, (x + 4)(x − 2) = 0.", "x² + 2x − 8 = 0, (x + 4)(x − 2) = 0."), "solution": t("x = −4 and x = 2.", "x = −4 y x = 2.")},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("(x + 2)(x + 3) = 0: each factor gives a negative value.", "(x + 2)(x + 3) = 0: cada factor da un valor negativo."), "c": t("−1 · (−6) = 6, but −1 + (−6) = −7.", "−1 · (−6) = 6, pero −1 + (−6) = −7."), "d": t("Substitute x = 2: 4 + 10 + 6 is not 0.", "Sustituya x = 2: 4 + 10 + 6 no es 0.")}, "solution": t("x = −2 and x = −3.", "x = −2 y x = −3.")},
      "B": {"ok": "a", "hints": {"b": t("(x − 2)(x − 5) = 0: x − 2 = 0 gives x = 2.", "(x − 2)(x − 5) = 0: x − 2 = 0 da x = 2."), "c": t("Substitute x = −5: 25 + 35 + 10 is not 0.", "Sustituya x = −5: 25 + 35 + 10 no es 0."), "d": t("1 + 10 = 11, not 7.", "1 + 10 = 11, no 7.")}, "solution": t("x = 2 and x = 5.", "x = 2 y x = 5.")},
      "C": {"ok": "c", "hints": {"a": t("x − 4 = 0 gives x = 4, not −4.", "x − 4 = 0 da x = 4, no −4."), "b": t("x + 1 = 0 gives x = −1.", "x + 1 = 0 da x = −1."), "d": t("x − 4 = 0 gives x = 4.", "x − 4 = 0 da x = 4.")}, "solution": t("x = 4 and x = −1.", "x = 4 y x = −1.")},
      "D": {"ok": "d", "hints": {"a": t("(−4)² is also 16.", "(−4)² también es 16."), "b": t("16² is 256.", "16² es 256."), "c": t("8² is 64.", "8² es 64.")}, "solution": t("x = 4 and x = −4.", "x = 4 y x = −4.")},
      "E": {"ok": "d", "hints": {"a": t("Do not divide by x: you lose x = 0.", "No divida entre x: se pierde x = 0."), "b": t("Substitute x = −7: 49 = −49 is false.", "Sustituya x = −7: 49 = −49 es falso."), "c": t("x = 7 also works: 49 = 49.", "x = 7 también sirve: 49 = 49.")}, "solution": t("x = 0 and x = 7.", "x = 0 y x = 7.")},
      "F": {"ok": "a", "hints": {"b": t("x + 4 = 0 gives x = −4.", "x + 4 = 0 da x = −4."), "c": t("x = 0 is also a solution: x(x + 4) = 0.", "x = 0 también es solución: x(x + 4) = 0."), "d": t("Factor: x(x + 4) = 0.", "Factorice: x(x + 4) = 0.")}, "solution": t("x = 0 and x = −4.", "x = 0 y x = −4.")},
      "G": {"ok": "c", "hints": {"a": t("(x + 5)(x − 2) = 0: x + 5 = 0 gives x = −5.", "(x + 5)(x − 2) = 0: x + 5 = 0 da x = −5."), "b": t("Substitute x = −2: 4 − 6 = −2, not 10.", "Sustituya x = −2: 4 − 6 = −2, no 10."), "d": t("First make it equal zero: x² + 3x − 10 = 0.", "Primero iguale a cero: x² + 3x − 10 = 0.")}, "solution": t("x = −5 and x = 2.", "x = −5 y x = 2.")},
      "H": {"ok": "a", "hints": {"b": t("9 feet is the length (x + 3), not the width.", "9 pies es el largo (x + 3), no el ancho."), "c": t("54 is the area, not a side.", "54 es el área, no un lado."), "d": t("Solve x(x + 3) = 54.", "Resuelva x(x + 3) = 54.")}, "solution": t("6 feet.", "6 pies.")},
     }}

    quiz = [
     ("A", t("Solve x² + 5x + 6 = 0.", "Resuelva x² + 5x + 6 = 0."), [("a", t("x = 2 and x = 3", "x = 2 y x = 3")), ("b", t("x = −2 and x = −3", "x = −2 y x = −3")), ("c", t("x = −1 and x = −6", "x = −1 y x = −6")), ("d", t("x = 2 and x = −3", "x = 2 y x = −3"))]),
     ("B", t("Solve x² − 7x + 10 = 0.", "Resuelva x² − 7x + 10 = 0."), [("a", t("x = 2 and x = 5", "x = 2 y x = 5")), ("b", t("x = −2 and x = −5", "x = −2 y x = −5")), ("c", t("x = 2 and x = −5", "x = 2 y x = −5")), ("d", t("x = 1 and x = 10", "x = 1 y x = 10"))]),
     ("C", t("Solve (x − 4)(x + 1) = 0.", "Resuelva (x − 4)(x + 1) = 0."), [("a", t("x = −4 and x = 1", "x = −4 y x = 1")), ("b", t("x = 4 and x = 1", "x = 4 y x = 1")), ("c", t("x = 4 and x = −1", "x = 4 y x = −1")), ("d", t("x = −4 and x = −1", "x = −4 y x = −1"))]),
     ("D", t("Solve x² − 16 = 0.", "Resuelva x² − 16 = 0."), [("a", t("x = 4 only", "x = 4 solamente")), ("b", t("x = 16 and x = −16", "x = 16 y x = −16")), ("c", t("x = 8 and x = −8", "x = 8 y x = −8")), ("d", t("x = 4 and x = −4", "x = 4 y x = −4"))]),
     ("E", t("Solve x² = 7x.", "Resuelva x² = 7x."), [("a", t("x = 7 only", "x = 7 solamente")), ("b", t("x = 7 and x = −7", "x = 7 y x = −7")), ("c", t("x = 0 only", "x = 0 solamente")), ("d", t("x = 0 and x = 7", "x = 0 y x = 7"))]),
     ("F", t("Solve x² + 4x = 0.", "Resuelva x² + 4x = 0."), [("a", t("x = 0 and x = −4", "x = 0 y x = −4")), ("b", t("x = 0 and x = 4", "x = 0 y x = 4")), ("c", t("x = −4 only", "x = −4 solamente")), ("d", t("x = 4 only", "x = 4 solamente"))]),
     ("G", t("Solve x² + 3x = 10.", "Resuelva x² + 3x = 10."), [("a", t("x = 5 and x = −2", "x = 5 y x = −2")), ("b", t("x = −5 and x = −2", "x = −5 y x = −2")), ("c", t("x = −5 and x = 2", "x = −5 y x = 2")), ("d", t("x = 10 and x = −1", "x = 10 y x = −1"))]),
     ("H", t("The area of a rectangle is 54 square feet. The length is 3 feet more than the width. How wide is it?", "El área de un rectángulo es de 54 pies cuadrados. El largo mide 3 pies más que el ancho. ¿Cuánto mide el ancho?"), [("a", t("6 feet", "6 pies")), ("b", t("9 feet", "9 pies")), ("c", t("54 feet", "54 pies")), ("d", t("27 feet", "27 pies"))])]

    tarea = (t("For your own work, with your notebook open: (1) Solve eight equations by factoring, writing the five steps and how many different solutions you get in each: x² + 7x + 10 = 0, x² − 3x − 18 = 0, 2x² + 5x − 3 = 0, x² + 6x + 9 = 0, x² = 9, x² = 5x, x² − 8x = −15, and 3x² = 12x. The last four must first be written in standard form. (2) The rectangle: its length is 3 feet more than its width and its area is 54 square feet. Write the equation, solve it by factoring, and explain why one solution is thrown out. Then make up a similar problem and solve it. (3) I always check: substitute each solution in its equation and correct the ones that do not make it true, describing the mistake in one sentence. x² − 5x + 6 = 0 → x = 2 or x = 3; x² + x − 12 = 0 → x = −3 or x = 4; x² = 4x → x = 4. Then do a round of each activity on the practice page, solving each exercise on paper before you type the answer. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) Resuelva ocho ecuaciones por factorización, escribiendo los cinco pasos y cuántas soluciones distintas obtiene en cada una: x² + 7x + 10 = 0, x² − 3x − 18 = 0, 2x² + 5x − 3 = 0, x² + 6x + 9 = 0, x² = 9, x² = 5x, x² − 8x = −15 y 3x² = 12x. Las cuatro últimas hay que llevarlas primero a la forma estándar. (2) El rectángulo: su largo mide 3 pies más que su ancho y su área es de 54 pies cuadrados. Plantee la ecuación, resuélvala por factorización y explique por qué se descarta una de las soluciones. Después invente un problema parecido y resuélvalo. (3) Siempre verifico: sustituya cada solución en su ecuación y corrija las que no cumplan la igualdad, describiendo el error en una frase. x² − 5x + 6 = 0 → x = 2 o x = 3; x² + x − 12 = 0 → x = −3 o x = 4; x² = 4x → x = 4. Después haga una ronda de cada actividad de la página de práctica, resolviendo cada ejercicio en papel antes de escribir la respuesta. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Think of a garden, a rug, or a window at home whose length is a few feet more than its width. Measure it, find its area, and write the equation that would let someone find the width from the area alone.",
               "Piense en un jardín, una alfombra o una ventana de su casa cuyo largo sea unos pies mayor que su ancho. Mídalo, halle su área y escriba la ecuación que permitiría a otra persona hallar el ancho sabiendo solo el área."))

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Solve a quadratic equation by writing it equal to zero, factoring, and setting each factor equal to zero; then check and interpret the solutions.", "Resuelva una ecuación cuadrática igualándola a cero, factorizando e igualando cada factor a cero; después verifique e interprete las soluciones."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Understand and use</strong> the zero product property.", "<strong>Comprender y aplicar</strong> la propiedad del producto cero."),
         t("<strong>Solve</strong> quadratic equations by factoring with a five-step method.", "<strong>Resolver</strong> ecuaciones cuadráticas por factorización con un procedimiento de cinco pasos."),
         t("<strong>Write</strong> an equation in standard form ax² + bx + c = 0 before factoring.", "<strong>Llevar</strong> una ecuación a la forma estándar ax² + bx + c = 0 antes de factorizar."),
         t("<strong>Solve</strong> word problems and check both solutions in the original equation.", "<strong>Resolver</strong> problemas aplicados y verificar ambas soluciones en la ecuación original.")],
        secciones, tarea, quiz,
        t("Self-check checklist for solving by factoring", "Lista de autoevaluación de la resolución por factorización"),
        t("Self-check checklist: skills for solving quadratic equations by factoring", "Lista de autoevaluación: destrezas para resolver ecuaciones cuadráticas por factorización"),
        [(t("Standard form", "Forma estándar"), t("I write the equation as ax² + bx + c = 0, even with terms on both sides.", "Llevo la ecuación a ax² + bx + c = 0, incluso con términos en ambos lados."), t("I try, but I make mistakes when I move terms.", "Lo intento, pero me equivoco al pasar términos."), t("I do not make the equation equal zero.", "No igualo la ecuación a cero.")),
         (t("Zero product property", "Propiedad del producto cero"), t("I set each factor equal to zero and do not lose x = 0.", "Igualo cada factor a cero y no pierdo la solución x = 0."), t("I set only one factor equal to zero, or I solve the linear equation wrong.", "Igualo un solo factor o resuelvo mal la ecuación lineal."), t("I do not set the factors equal to zero.", "No igualo los factores a cero.")),
         (t("Checking and interpreting", "Verificar e interpretar"), t("I check both solutions and throw out the one that makes no sense.", "Verifico ambas soluciones y descarto la que no tiene sentido."), t("I check only one solution, or I do not throw out the impossible one.", "Verifico una sola solución o no descarto la imposible."), t("I do not check or interpret the solutions.", "No verifico ni interpreto las soluciones."))],
        t("<p>In this lesson you solved quadratic equations by <strong>factoring</strong>, using the <strong>zero product property</strong> with a five-step method, and you interpreted the solutions in area problems.</p>\n<p>But not every quadratic equation factors with whole numbers. In <strong>Lesson 4.2 · Completing the square</strong> you will learn a method that <strong>always</strong> works, whether the equation factors or not. Completing the square is also where the quadratic formula of Lesson 4.3 comes from.</p>",
          "<p>En esta lección se resolvieron ecuaciones cuadráticas por <strong>factorización</strong>, aplicando la <strong>propiedad del producto cero</strong> con un procedimiento de cinco pasos, y se interpretaron las soluciones en problemas de área.</p>\n<p>Pero no todas las ecuaciones cuadráticas se factorizan con números enteros. En la <strong>Lección 4.2 · Completar el cuadrado</strong> se aprenderá un método que funciona <strong>siempre</strong>, se factorice o no la ecuación. Además, completar el cuadrado es el origen de la fórmula cuadrática de la Lección 4.3.</p>"),
        ("4-2", ("", t("Lesson 4.2 · Completing the square", "Lección 4.2 · Completar el cuadrado"))),
        [(t("quadratic equation", "ecuación cuadrática"), t("An equation whose highest power of x is x².", "Una ecuación cuya mayor potencia de x es x².")),
         (t("standard form", "forma estándar"), "ax² + bx + c = 0"),
         (t("zero product property", "propiedad del producto cero"), t("If A · B = 0, then A = 0 or B = 0.", "Si A · B = 0, entonces A = 0 o B = 0.")),
         (t("solution (root)", "solución (raíz)"), t("A value of x that makes the equation true.", "Un valor de x que hace cierta la ecuación.")),
         (t("extraneous answer", "solución descartada"), t("A correct algebraic solution that makes no sense in the situation, such as a negative length.", "Una solución algebraica correcta que no tiene sentido en la situación, como una longitud negativa."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function F(k, m, f){ return {k: k, m: m || 0, f: f || []}; }
function bin(a, b){ return [b, a]; }
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
var SOL_AYUDA = T("Type both solutions separated by a comma, like: −2, 3. If there is only one, type it once.", "Escriba las dos soluciones separadas por una coma, como: −2, 3. Si solo hay una, escríbala una vez.");
var O = T(" or ", " o ");
/* Monic quadratic with integer roots r1, r2: its factored form (x(x − r) when a root is 0). */
function facR(r1, r2){ if (r1 === 0 && r2 === 0) return F(1, 2, []); if (r1 === 0 || r2 === 0){ var r = r1 || r2; return F(1, 1, [bin(1, -r)]); } return F(1, 0, [bin(1, -r1), bin(1, -r2)]); }
/* p evaluated at v, written out: (−5)² + 11(−5) + 42 = 12 */
function evalTxt(p, v){ var l = listaTerm(p); if (!l.length) return "0"; var val = 0; p.forEach(function(c, g){ val += c * Math.pow(v, g); });
  return l.map(function(t, i){ var c = t[0], g = t[1], a = Math.abs(c), cuerpo = g === 0 ? String(a) : (a === 1 ? "" : a) + "(" + sg(v) + ")" + (g === 2 ? "²" : "");
    return (c < 0 ? (i ? " − " : "−") : (i ? " + " : "")) + cuerpo; }).join("") + " = " + sg(val); }
function cerosTxt(FF){ var l = []; if (FF.m) l.push("x = 0"); FF.f.forEach(function(q){ l.push(pVis(q) + " = 0"); }); return l.join(O); }
function raicesF(FF){ var l = []; if (FF.m) l.push(0); FF.f.forEach(function(q){ var v = raizVal(q); if (l.indexOf(v) < 0) l.push(v); }); return l; }
function raicesTxt(FF){ var l = []; if (FF.m) l.push("0"); FF.f.forEach(function(q){ var v = raizTxt(q); if (l.indexOf(v) < 0) l.push(v); }); return l.map(function(v){ return "x = " + v; }).join(O); }

/* ===== MODULE 1 · Zero product property ===== */
OMR("zq", function(){
  var r1 = nz(-8, 8), r2 = nz(-8, 8), FF = Math.random() < .3 ? F(1, 1, [bin(1, -r1)]) : F(1, 0, [bin(1, -r1), bin(1, -r2)]), k = Math.random() < .5 ? 0 : elige([4, 6, 8, 10, 12, -6]);
  var enun = T("Can you already set each factor equal to zero in ", "¿Ya se puede igualar cada factor a cero en ") + envuelve(fVis(FF) + " = " + sg(k), fVoz(FF) + T(" equals ", " es igual a ") + sg(k)) + "?";
  return {enun: enun, correcta: k === 0 ? "si" : "no", opciones: [{clave: "si", html: T("Yes, the product equals zero", "Sí, el producto está igualado a cero")}, {clave: "no", html: T("No, first write it in standard form", "No, primero hay que llevarla a la forma estándar")}],
    porClave: {si: T("Look at the right side: it is " + sg(k) + ", not 0. Many pairs of numbers multiply to " + sg(k) + ".", "Mire el lado derecho: es " + sg(k) + ", no 0. Muchas parejas de números dan " + sg(k) + " al multiplicarse."), no: T("The right side is already 0, so you can use the property.", "El lado derecho ya es 0, así que se puede aplicar la propiedad.")},
    bien: k === 0 ? T("The product is zero, so one factor must be zero: ", "El producto es cero, así que un factor tiene que ser cero: ") + cerosTxt(FF) + "." : T("The product equals " + sg(k) + ": multiply out, move the " + sg(k) + " to the left side, and factor again.", "El producto es " + sg(k) + ": se multiplica, se pasa el " + sg(k) + " al lado izquierdo y se vuelve a factorizar.")};
});
function casoCero(){
  var tipo = elige(["dos", "dos", "x", "a", "doble"]), FF;
  if (tipo === "dos"){ var r1 = nz(-9, 9), r2; do { r2 = nz(-9, 9); } while (r2 === r1); FF = F(1, 0, [bin(1, -r1), bin(1, -r2)]); }
  else if (tipo === "x") FF = F(1, 1, [bin(1, nz(-9, 9))]);
  else if (tipo === "doble"){ var r = nz(-6, 6); FF = F(1, 0, [bin(1, -r), bin(1, -r)]); }
  else { var a, b; do { a = elige([2, 3, 4, 5]); b = nz(-7, 7); } while (mcd(a, Math.abs(b)) !== 1); FF = F(1, 0, [bin(a, b), bin(1, nz(-6, 6))]); }
  return {FF: FF, raices: raicesF(FF)};
}
creaPracticaLibre("zs", function(){ var c = casoCero();
  return {enun: T("Solve ", "Resuelva ") + envuelve(fVis(c.FF) + " = 0", fVoz(c.FF) + T(" equals 0", " es igual a 0")) + ". " + SOL_AYUDA,
    evalua: function(txt){ return evaluaSol(txt, c.raices); },
    solucion: T("Each factor equals zero: ", "Cada factor igual a cero: ") + cerosTxt(c.FF) + ". " + T("Solutions: ", "Soluciones: ") + raicesTxt(c.FF) + (c.raices.length === 1 && !c.FF.m ? T(" (the two factors are equal, so there is only one solution).", " (los dos factores son iguales, así que hay una sola solución).") : ".")};
});

/* ===== MODULE 2 · The five steps ===== */
function casoPasos(){
  var tipo = elige(["tri", "tri", "dif", "comun", "ac"]), FF, S;
  if (tipo === "tri"){ var r1 = nz(-9, 9), r2; do { r2 = nz(-9, 9); } while (r1 + r2 === 0); FF = facR(r1, r2); }
  else if (tipo === "dif"){ var r = aleatorio(1, 10); FF = F(1, 0, [bin(1, r), bin(1, -r)]); }
  else if (tipo === "comun"){ FF = facR(0, nz(-9, 9)); }
  else { var a, b; do { a = elige([2, 3]); b = nz(-5, 5); } while (mcd(a, Math.abs(b)) !== 1); FF = F(1, 0, [bin(a, b), bin(1, nz(-5, 5))]); }
  S = fProducto(FF);
  return {FF: FF, S: S, raices: raicesF(FF)};
}
function pasosCinco(c, inicio){
  var P = [inicio || T("It is already in standard form: ", "Ya está en forma estándar: ") + pVis(c.S) + " = 0."];
  P.push(T("Factor: ", "Se factoriza: ") + fVis(c.FF) + " = 0.");
  P.push(T("Each factor equals zero: ", "Cada factor igual a cero: ") + cerosTxt(c.FF) + ".");
  P.push(T("Solve each one: ", "Se resuelve cada una: ") + raicesTxt(c.FF) + ".");
  var v = c.raices.filter(function(x){ return x && x === Math.round(x); })[0], L = c.L || c.S, R = c.R || [0];
  if (v !== undefined) P.push(T("Check in the original equation with x = ", "Se verifica en la ecuación original con x = ") + sg(v) + ": " + (pGrado(R) === 0 && !R[0] ? evalTxt(L, v) : T("left side ", "lado izquierdo ") + evalTxt(L, v) + T("; right side ", "; lado derecho ") + evalTxt(R, v)) + ". ✓");
  P.push(T("Solutions: ", "Soluciones: ") + "<strong>" + raicesTxt(c.FF) + "</strong>.");
  return P;
}
pasoAPaso4("ps", function(){ var c = casoPasos(); return {enun: T("Solve ", "Resuelva ") + ecHTML(c.S, [0]) + ".", pasos: pasosCinco(c)}; });
creaPracticaLibre("pq", function(){ var c = casoPasos();
  return {enun: T("Solve ", "Resuelva ") + ecHTML(c.S, [0]) + ". " + SOL_AYUDA, evalua: function(txt){ return evaluaSol(txt, c.raices); }, solucion: pasosCinco(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 3 · Standard form first ===== */
var TIPOS_FE = {num: T("A number on the right: x² + bx = number", "Un número a la derecha: x² + bx = número"), xnum: T("x² equal to terms with x and numbers", "x² igual a términos con x y números"), ambos: T("Terms with x on both sides", "Términos con x en ambos lados"), nums: T("Numbers on both sides", "Números en ambos lados"), cuad: T("x² equal to a number", "x² igual a un número"), xx: T("x² equal to a term with x", "x² igual a un término con x")};
function casoFE(tipo){
  tipo = tipo && tipo !== "azar" ? tipo : elige(Object.keys(TIPOS_FE));
  var r1, r2, L, R;
  if (tipo === "cuad"){ r1 = aleatorio(1, 10); r2 = -r1; }
  else if (tipo === "xx"){ r1 = 0; r2 = nz(-9, 9); }
  else { do { r1 = nz(-8, 8); r2 = nz(-8, 8); } while (r1 + r2 === 0 || r1 === r2); }
  var FF = facR(r1, r2), S = fProducto(FF);
  if (tipo === "num"){ R = [-S[0]]; L = pSuma(S, R); }
  else if (tipo === "xnum" || tipo === "cuad" || tipo === "xx"){ L = [0, 0, 1]; R = pResta(L, S); }
  else if (tipo === "ambos"){ R = pDe({1: nz(-6, 6), 0: aleatorio(-9, 9)}); L = pSuma(S, R); if (!L[1]) return casoFE(tipo); }
  else { R = [nz(-12, 12)]; L = pSuma(S, R); if (!L[0]) return casoFE(tipo); }
  return {tipo: tipo, L: L, R: R, S: S, FF: FF, raices: raicesF(FF)};
}
function movidas(R){
  var l = [];
  if (R[1]) l.push((R[1] > 0 ? T("subtract ", "se resta ") : T("add ", "se suma ")) + tVis(Math.abs(R[1]), 1, true));
  if (R[0]) l.push((R[0] > 0 ? T("subtract ", "se resta ") : T("add ", "se suma ")) + Math.abs(R[0]));
  return l.join(Y2()) + T(" on both sides", " en ambos lados");
}
function Y2(){ return T(" and ", " y "); }
function pasosFE(c){
  var P = [T("Move everything to the left side: ", "Se pasa todo al lado izquierdo: ") + movidas(c.R) + ". " + T("Standard form: ", "Forma estándar: ") + pVis(c.S) + " = 0."];
  return P.concat(pasosCinco(c, "").slice(1));
}
pasoAPaso4("fe", function(){ var c = casoFE($("fe-tipo").value); return {enun: T("Solve ", "Resuelva ") + ecHTML(c.L, c.R) + ".", pasos: pasosFE(c)}; });
$("fe-tipo").addEventListener("change", function(){ $("fe-nuevo").click(); });
OMR("fs", function(){ var c = casoFE();
  var malos = [pSuma(c.L, c.R), pDe({2: 1, 1: (c.L[1] || 0) + (c.R[1] || 0), 0: (c.L[0] || 0) - (c.R[0] || 0)}), pDe({2: 1, 1: (c.L[1] || 0) - (c.R[1] || 0), 0: (c.L[0] || 0) + (c.R[0] || 0)}), pSuma(c.S, [elige([-1, 1]) * aleatorio(1, 3)])];
  var vistos = {}, ops = [{clave: pClave(c.S), html: envuelve(pVis(c.S) + " = 0", pVoz(c.S) + T(" equals 0", " es igual a 0"))}]; vistos[pClave(c.S)] = 1;
  malos.forEach(function(p){ var k = pClave(p); if (ops.length < 4 && !vistos[k]){ vistos[k] = 1; ops.push({clave: k, html: envuelve(pVis(p) + " = 0", pVoz(p) + T(" equals 0", " es igual a 0"))}); } });
  return {enun: T("Which is the standard form of ", "¿Cuál es la forma estándar de ") + ecHTML(c.L, c.R) + "?", correcta: pClave(c.S), opciones: ops,
    pista: T("Each term that moves to the other side changes its sign.", "Cada término que pasa al otro lado cambia de signo."), bien: movidas(c.R).replace(/^./, function(x){ return x.toUpperCase(); }) + ": " + pVis(c.S) + " = 0."};
});
creaPracticaLibre("fq", function(){ var c = casoFE();
  return {enun: T("Solve ", "Resuelva ") + ecHTML(c.L, c.R) + ". " + SOL_AYUDA, evalua: function(txt){ return evaluaSol(txt, c.raices); }, solucion: pasosFE(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 4 · Word problems ===== */
var AP = {}, AP_INT = 0;
function apNuevo(){
  var ctx = elige(["rect", "tri", "cons", "num"]), r, d, area;
  if (ctx === "rect"){ r = aleatorio(3, 12); d = aleatorio(2, 9); area = r * (r + d);
    AP = {texto: T("The area of a rectangle is " + area + " square feet. The length is " + d + " feet more than the width. How long is each side?", "El área de un rectángulo es de " + area + " pies cuadrados. El largo mide " + d + " pies más que el ancho. ¿Cuánto mide cada lado?"),
      plan: T("Let x be the width. The length is x + " + d + ", and the area is x(x + " + d + ") = " + area + ".", "Sea x el ancho. El largo es x + " + d + " y el área es x(x + " + d + ") = " + area + "."),
      motivo: T("A width cannot be negative.", "Un ancho no puede ser negativo."), resp: T("The width is " + r + " feet and the length is " + (r + d) + " feet.", "El ancho mide " + r + " pies y el largo, " + (r + d) + " pies.")}; }
  else if (ctx === "tri"){ do { r = aleatorio(3, 12); d = aleatorio(2, 9); } while ((r * (r + d)) % 2); area = r * (r + d) / 2;
    AP = {texto: T("A triangle has an area of " + area + " square inches. The base is " + d + " inches longer than the height. How long are the height and the base?", "Un triángulo tiene un área de " + area + " pulgadas cuadradas. La base mide " + d + " pulgadas más que la altura. ¿Cuánto miden la altura y la base?"),
      plan: T("Let x be the height. The area is (base × height) ÷ 2, so x(x + " + d + ") ÷ 2 = " + area + ", that is, x(x + " + d + ") = " + 2 * area + ".", "Sea x la altura. El área es (base × altura) ÷ 2, así que x(x + " + d + ") ÷ 2 = " + area + ", es decir, x(x + " + d + ") = " + 2 * area + "."),
      motivo: T("A height cannot be negative.", "Una altura no puede ser negativa."), resp: T("The height is " + r + " inches and the base is " + (r + d) + " inches.", "La altura mide " + r + " pulgadas y la base, " + (r + d) + " pulgadas.")}; area = 2 * area; }
  else if (ctx === "cons"){ r = aleatorio(4, 14); d = 1; area = r * (r + 1);
    AP = {texto: T("The product of two consecutive positive whole numbers is " + area + ". What are the numbers?", "El producto de dos números enteros positivos consecutivos es " + area + ". ¿Cuáles son esos números?"),
      plan: T("Let x be the smaller number. The next one is x + 1, and x(x + 1) = " + area + ".", "Sea x el número menor. El siguiente es x + 1, y x(x + 1) = " + area + "."),
      motivo: T("The problem asks for positive numbers.", "El problema pide números positivos."), resp: T("The numbers are " + r + " and " + (r + 1) + ".", "Los números son " + r + " y " + (r + 1) + ".")}; }
  else { r = aleatorio(2, 9); d = elige([2, 3, 4, 5]); area = r * (r + d);
    AP = {texto: T("A positive number times the number that is " + d + " more than it gives " + area + ". What is the number?", "Un número positivo multiplicado por el número que es " + d + " mayor que él da " + area + ". ¿Cuál es el número?"),
      plan: T("Let x be the number. Then x(x + " + d + ") = " + area + ".", "Sea x el número. Entonces x(x + " + d + ") = " + area + "."),
      motivo: T("The problem asks for a positive number.", "El problema pide un número positivo."), resp: T("The number is " + r + ".", "El número es " + r + ".")}; }
  AP.r = r; AP.otra = -(r + d); AP.S = pDe({2: 1, 1: d, 0: -area}); AP.FF = facR(r, -(r + d)); AP_INT = 0; AP.paso = 1;
  $("ap-enun").textContent = AP.texto; $("ap-plan").textContent = AP.plan;
  var ops = baraja([{clave: "ok", S: AP.S}, {clave: "m1", S: pDe({2: 1, 1: d, 0: area})}, {clave: "m2", S: pDe({2: 1, 1: -d, 0: -area})}]);
  $("ap-ops").innerHTML = ops.map(function(o){ return '<button type="button" class="btn-sec" data-c="' + o.clave + '">' + envuelve(pVis(o.S) + " = 0", pVoz(o.S) + T(" equals 0", " es igual a 0")) + "</button>"; }).join("");
  [].forEach.call($("ap-ops").querySelectorAll("button"), function(b){ b.addEventListener("click", function(){ apEcuacion(b); }); });
  $("ap-p2").hidden = $("ap-p3").hidden = true; $("ap-r").value = ""; $("ap-r").disabled = false; $("ap-comprobar").disabled = false; $("ap-fb").className = "fb"; $("ap-fb").innerHTML = "";
}
function apEcuacion(b){ var fb = $("ap-fb");
  if (AP.paso !== 1) return;
  if (b.getAttribute("data-c") === "ok"){ AP.paso = 2; AP_INT = 0; fb.className = "fb bien"; fb.innerHTML = TX.bien + T("Moving the " + -AP.S[0] + " to the left side gives the standard form.", "Al pasar el " + -AP.S[0] + " al lado izquierdo se obtiene la forma estándar."); [].forEach.call($("ap-ops").querySelectorAll("button"), function(x){ x.disabled = true; }); b.className = "btn"; b.disabled = false; b.setAttribute("aria-disabled", "true"); b.insertAdjacentHTML("beforeend", " ✓"); $("ap-p2").hidden = false; $("ap-r").focus(); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + T("Multiply x(x + " + AP.S[1] + ") and move the area to the left side: its sign changes.", "Multiplique x(x + " + AP.S[1] + ") y pase el área al lado izquierdo: cambia de signo."); }
}
$("ap-comprobar").addEventListener("click", function(){ if (AP.paso !== 2) return; var r = evaluaSol($("ap-r").value, [AP.r, AP.otra]), fb = $("ap-fb");
  if (r.estado === "invalido"){ fb.className = "fb pista"; fb.innerHTML = r.msg; return; }
  AP_INT++;
  if (r.estado === "bien" || AP_INT >= 2){ fb.className = r.estado === "bien" ? "fb bien" : "fb mal"; fb.innerHTML = (r.estado === "bien" ? TX.bien : TX.asi) + fVis(AP.FF) + " = 0, " + T("so ", "así que ") + "x = " + sg(AP.r) + O + "x = " + sg(AP.otra) + ".";
    AP.paso = 3; $("ap-r").disabled = true; $("ap-comprobar").disabled = true; $("ap-p3").hidden = false;
    $("ap-v").innerHTML = baraja([AP.r, AP.otra]).map(function(v){ return '<button type="button" class="btn-sec" data-v="' + v + '">x = ' + sg(v) + "</button>"; }).join("");
    [].forEach.call($("ap-v").querySelectorAll("button"), function(b){ b.addEventListener("click", function(){ apValida(b); }); }); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + r.msg + TX.otraVez; } });
function apValida(b){ var fb = $("ap-fb"), v = +b.getAttribute("data-v");
  if (AP.paso !== 3) return;
  if (v === AP.r){ AP.paso = 4; fb.className = "fb bien"; fb.innerHTML = TX.bien + AP.motivo + " " + T("So x = ", "Así que x = ") + AP.r + ". <strong>" + AP.resp + "</strong>"; [].forEach.call($("ap-v").querySelectorAll("button"), function(x){ x.disabled = true; }); b.className = "btn"; b.disabled = false; b.setAttribute("aria-disabled", "true"); b.insertAdjacentHTML("beforeend", " ✓"); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + AP.motivo + " " + T("Which value makes sense?", "¿Qué valor tiene sentido?"); } }
$("ap-otro").addEventListener("click", apNuevo); apNuevo();
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    sol = t("Solutions", "Soluciones")
    filas = [["+ 6", t("Subtract 6", "Se resta 6"), "− 6"], ["− 8", t("Add 8", "Se suma 8"), "+ 8"], ["+ 5x", t("Subtract 5x", "Se resta 5x"), "− 5x"], ["− 2x", t("Add 2x", "Se suma 2x"), "+ 2x"]]
    cab = [t("Term on the right side", "Término en el lado derecho"), t("Operation on both sides", "Operación en ambos lados"), t("How it appears on the left", "Cómo aparece en el lado izquierdo")]
    mov = (f'      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("When a term moves to the other side, its sign changes", "Al pasar un término al otro lado de la ecuación, cambia de signo")}</caption>'
           + "<thead><tr>" + "".join(f'<th scope="col">{c}</th>' for c in cab) + "</tr></thead><tbody>"
           + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas) + "</tbody></table></div>")
    tipos = [("azar", t("Any kind, at random", "Cualquiera, al azar")), ("num", t("A number on the right: x² + bx = number", "Un número a la derecha: x² + bx = número")), ("xnum", t("x² equal to terms with x and numbers", "x² igual a términos con x y números")), ("ambos", t("Terms with x on both sides", "Términos con x en ambos lados")), ("nums", t("Numbers on both sides", "Números en ambos lados")), ("cuad", t("x² equal to a number", "x² igual a un número")), ("xx", t("x² equal to a term with x", "x² igual a un término con x"))]
    mods = [
     (t("zero", "cero"), t("The zero product property", "La propiedad del producto cero"),
      f'''{n4.formula(t("If A · B = 0, then A = 0 or B = 0.", "Si A · B = 0, entonces A = 0 o B = 0."))}
      <p>{t("The property can only be used when the product equals zero. First decide whether you can use it yet; then go from the factors to the solutions.", "La propiedad solo se puede aplicar cuando el producto está igualado a cero. Primero decida si ya se puede aplicar; después pase de los factores a las soluciones.")}</p>
{B.om("zq", t("Practice: can you use the property yet?", "Practique: ¿se puede aplicar ya la propiedad?"))}
{libre("zs", t("Practice: from the factors to the solutions", "Practique: de los factores a las soluciones"), sol)}
      <div class="caja-tip">{t("The key is the zero. If a product is 12, there are many possible pairs of numbers. If it is 0, there is no other way: one of the factors has to be zero. If the two factors are equal, there is only one solution.", "La clave es el cero. Si un producto da 12, hay muchas parejas de números posibles. Si da 0, no hay alternativa: alguno de los factores tiene que valer cero. Si los dos factores son iguales, hay una sola solución.")}</div>'''),
     (t("steps", "pasos"), t("The five steps", "Los cinco pasos"),
      f'''      <p>{t("1. Standard form. 2. Factor. 3. Each factor equals zero. 4. Solve each linear equation. 5. Check in the original equation.", "1. Forma estándar. 2. Factorizar. 3. Igualar cada factor a cero. 4. Resolver cada ecuación lineal. 5. Verificar en la ecuación original.")}</p>
{n4.pasos("ps", t("Another equation", "Otra ecuación"))}
{libre("pq", t("Practice: solve and type both solutions", "Practique: resuelva y escriba las dos soluciones"), sol)}'''),
     (t("standard-form", "forma-estandar"), t("Standard form first", "Llevar a la forma estándar primero"),
      f'''      <p>{t("Many equations do not come equal to zero. Step 1 is always to move every term to one side until you reach the standard form ax² + bx + c = 0.", "Muchas ecuaciones no vienen igualadas a cero. El paso 1 es siempre pasar todos los términos a un lado hasta llegar a la forma estándar ax² + bx + c = 0.")}</p>
      <div class="caja-atencion"><strong>{t("Typical mistake: factoring without the zero.", "Error típico: factorizar sin igualar a cero.")}</strong> {t("x² + 5x = 6 → x(x + 5) = 6 → x = 6 or x + 5 = 6? Check x = 6: 36 + 30 = 66, not 6. The method does not work because the product is not zero. The right way: x² + 5x − 6 = 0, (x + 6)(x − 1) = 0, so x = −6 or x = 1. Check: (−6)² + 5(−6) = 36 − 30 = 6. ✓", "x² + 5x = 6 → x(x + 5) = 6 → ¿x = 6 o x + 5 = 6? Compruebe x = 6: 36 + 30 = 66, no 6. El método no vale, porque el producto no es cero. Lo correcto: x² + 5x − 6 = 0, (x + 6)(x − 1) = 0, así que x = −6 o x = 1. Comprobación: (−6)² + 5(−6) = 36 − 30 = 6. ✓")}</div>
{mov}
      <div class="panel"><div class="campos">{n4.lista("fe-tipo", t("Kind of equation", "Tipo de ecuación"), tipos)}</div></div>
{n4.pasos("fe", t("Another equation", "Otra ecuación"))}
      <div class="caja-tip">{t("Do not divide by x: in x² = 5x, dividing both sides by x loses the solution x = 0. Move everything to one side and factor.", "No divida entre x: en x² = 5x, dividir ambos lados entre x hace perder la solución x = 0. Se lleva todo a un lado y se factoriza.")}</div>
{B.om("fs", t("Practice: choose the standard form", "Practique: elija la forma estándar"))}
{libre("fq", t("Practice: standard form first, then solve", "Practique: forma estándar primero y después resuelva"), sol)}'''),
     (t("apply", "aplica"), t("Word problems: interpret the solution", "Problemas aplicados: interpretar la solución"),
      f'''      <p>{t("Write the equation, solve it by factoring, and then decide which of the two solutions makes sense in the real situation.", "Plantee la ecuación, resuélvala por factorización y decida después cuál de las dos soluciones tiene sentido en la situación real.")}</p>
      <div class="practica"><p class="enun" id="ap-enun"></p><p id="ap-plan"></p>
        <p><strong>{t("Step 1. Which is the equation in standard form?", "Paso 1. ¿Cuál es la ecuación en forma estándar?")}</strong></p>
        <div class="fila-btn" id="ap-ops"></div>
        <div id="ap-p2" hidden><p><strong>{t("Steps 2 to 4. Factor and find both solutions.", "Pasos 2 a 4. Factorice y halle las dos soluciones.")}</strong></p>
          <div class="campos"><div class="campo"><label for="ap-r">{sol}</label><input type="text" autocomplete="off" class="ancho" id="ap-r"></div></div>
          <div class="fila-btn"><button type="button" class="btn" id="ap-comprobar">{t("Check the solutions", "Comprobar las soluciones")}</button></div></div>
        <div id="ap-p3" hidden><p><strong>{t("Step 5. Which solution makes sense in the problem?", "Paso 5. ¿Qué solución tiene sentido en el problema?")}</strong></p><div class="fila-btn" id="ap-v"></div></div>
        <div class="fb" id="ap-fb" role="status"></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="ap-otro">{t("Another problem", "Otro problema")}</button></div></div>
      <div class="caja-atencion"><strong>{t("Interpret the situation.", "Interprete el contexto.")}</strong> {t("Lengths, areas, and times cannot be negative. A correct algebraic solution may not be a valid answer to the problem.", "Las longitudes, las áreas y los tiempos no pueden ser negativos. Una solución algebraica correcta puede no ser una respuesta válida del problema.")}</div>''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver ecuaciones cuadráticas por factorización")
