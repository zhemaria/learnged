"""Level 4 · Lesson 3.3 · Factoring trinomials (a = 1 and a ≠ 1) — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_3-3.html and algebra/interactivo_3-3_factorizacion_trinomios (two numbers,
the ac method and the "aspa simple", special cases and complete factoring). They are rebuilt here, inside LearnGED, with typed
factored answers read by math/poly4.js. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "3-3"
TEMA = ("Multiplying and factoring", "Multiplicación y factorización")
TIT = ("Factoring trinomials (a = 1 and a ≠ 1)", "Factorización de trinomios (a = 1 y a ≠ 1)")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 3.2.</strong> In Lesson 3.2 you factored by taking out the common factor and by recognizing a difference of squares. Now you factor <strong>trinomials</strong> (three terms), which are exactly what you get when you multiply two binomials with FOIL. To factor a trinomial is to ask: which two binomials, multiplied, give this trinomial?",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 3.2 se factorizó extrayendo el factor común y reconociendo diferencias de cuadrados. Ahora se factorizan <strong>trinomios</strong> (tres términos), que son justamente el resultado de multiplicar dos binomios con FOIL. Factorizar un trinomio es preguntarse: ¿qué dos binomios, multiplicados, dan este trinomio?")}</p>
<p>{t("To factor x² + bx + c, look for two numbers that do two things at the same time:", "Para factorizar x² + bx + c se buscan dos números que cumplan dos condiciones a la vez:")}</p>
<ul><li>{t("multiplied, they give <strong>c</strong> (the constant term);", "que multiplicados den <strong>c</strong> (el término independiente);")}</li>
<li>{t("added, they give <strong>b</strong> (the coefficient of x).", "que sumados den <strong>b</strong> (el coeficiente de x).")}</li></ul>
<p>{t("Those two numbers go in the binomials: x² + bx + c = (x + number₁)(x + number₂). The signs of c and b guide the search:", "Esos dos números son los que van en los binomios: x² + bx + c = (x + número₁)(x + número₂). Los signos de c y b orientan la búsqueda:")}</p>
{tabla(t("Signs of the trinomial and of the two numbers", "Signos del trinomio y de los dos números"), t("How the signs of c and b tell you the signs of the two numbers", "Relación entre los signos del trinomio y los signos de los dos números buscados"),
  [t("Sign of c", "Signo de c"), t("Sign of b", "Signo de b"), t("The two numbers are…", "Los dos números son…")],
  [[t("positive (+)", "positivo (+)"), t("positive (+)", "positivo (+)"), t("both positive", "ambos positivos")],
   [t("positive (+)", "positivo (+)"), t("negative (−)", "negativo (−)"), t("both negative", "ambos negativos")],
   [t("negative (−)", "negativo (−)"), t("either", "cualquiera"), t("one positive and one negative", "uno positivo y uno negativo")]])}
{ejemplo(t("Example 1: factor x² + 7x + 12.", "Ejemplo 1 · Factorizar x² + 7x + 12."),
  [("1", t("Two numbers with product 12 and sum 7.", "Dos números que multiplicados den 12 y sumados den 7."), ""), ("2", t("They are 3 and 4.", "Son 3 y 4."), "3 · 4 = 12 " + t("and", "y") + " 3 + 4 = 7."), ("3", t("Write the binomials.", "Se escriben los binomios."), "(x + 3)(x + 4)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>(x + 3)(x + 4)</strong>.")])}
{ejemplo(t("Example 2: with a negative constant. Factor x² − x − 12.", "Ejemplo 2 · Con un término independiente negativo. Factorizar x² − x − 12."),
  [("1", t("Two numbers with product −12 and sum −1.", "Dos números que multiplicados den −12 y sumados den −1."), ""), ("2", t("They are −4 and 3.", "Son −4 y 3."), "(−4) · 3 = −12 " + t("and", "y") + " −4 + 3 = −1."),
   ("✓", t("Answer.", "Respuesta."), "<strong>(x − 4)(x + 3)</strong>.")])}
{practica("p1", t("Practice 1 — x² + 5x + 6", "Práctica 1 — x² + 5x + 6"), t("Choose the correct factorization of x² + 5x + 6.", "Seleccione la factorización correcta de x² + 5x + 6."), [("a", "(x + 1)(x + 6)"), ("b", "(x + 2)(x + 3)"), ("c", "(x − 2)(x − 3)")])}
{practica("p2", t("Practice 2 — x² − x − 6", "Práctica 2 — x² − x − 6"), t("Choose the correct factorization of x² − x − 6.", "Seleccione la factorización correcta de x² − x − 6."), [("a", "(x + 3)(x − 2)"), ("b", "(x − 2)(x − 3)"), ("c", "(x − 3)(x + 2)")])}
{practica("p3", t("Practice 3 — x² − 9x + 20", "Práctica 3 — x² − 9x + 20"), t("Choose the correct factorization of x² − 9x + 20.", "Seleccione la factorización correcta de x² − 9x + 20."), [("a", "(x − 4)(x − 5)"), ("b", "(x + 4)(x + 5)"), ("c", "(x − 2)(x − 10)")])}
{enlace(n, t("a-one", "a-uno"), t("trinomials with a = 1", "trinomios con a = 1"), t("Look at the factor pairs, find the two numbers that multiply and add, and type the binomials.", "Mire los pares de factores, halle los dos números que multiplican y suman, y escriba los binomios."))}'''

    s2 = f'''<p>{t("When the coefficient of x² is not 1, use the <strong>ac method</strong>:", "Cuando el coeficiente de x² no es 1, se usa el <strong>método ac</strong>:")}</p>
<ol><li>{t("Multiply a · c.", "Multiplicar a · c.")}</li>
<li>{t("Find two numbers whose product is ac and whose sum is b.", "Buscar dos números que multiplicados den ac y sumados den b.")}</li>
<li>{t("Rewrite the middle term (bx) with those two numbers.", "Reescribir el término del medio (bx) usando esos dos números.")}</li>
<li>{t("Group two and two and take out the common factor of each group.", "Agrupar de dos en dos y extraer el factor común de cada grupo.")}</li></ol>
{ejemplo(t("Example 3: factor 2x² + 7x + 3.", "Ejemplo 3 · Factorizar 2x² + 7x + 3."),
  [("1", "a · c = 2 · 3 = 6.", ""), ("2", t("Two numbers with product 6 and sum 7:", "Dos números que multipliquen 6 y sumen 7:"), t("6 and 1.", "6 y 1.")), ("3", t("Rewrite.", "Se reescribe."), "2x² + 6x + x + 3."), ("4", t("Group.", "Se agrupa."), "2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>(2x + 1)(x + 3)</strong>.")])}
{ejemplo(t("Example 4: with signs. Factor 3x² − 10x + 8.", "Ejemplo 4 · Con signos. Factorizar 3x² − 10x + 8."),
  [("1", "a · c = 3 · 8 = 24.", ""), ("2", t("Two numbers with product 24 and sum −10:", "Dos números que multipliquen 24 y sumen −10:"), t("−6 and −4.", "−6 y −4.")), ("3", t("Rewrite.", "Se reescribe."), "3x² − 6x − 4x + 8."), ("4", t("Group.", "Se agrupa."), "3x(x − 2) − 4(x − 2) = (3x − 4)(x − 2)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>(3x − 4)(x − 2)</strong>.")])}
{caja("tip", t("The trick is in the middle term", "El truco está en el término del medio"), t("<p>The two numbers of the ac method “split” the term bx in two. When you group, the <strong>same binomial</strong> must appear in both groups; if it does not, check the signs.</p>", "<p>Los dos números del método ac sirven para «partir» el término bx en dos. Al agrupar, debe aparecer el <strong>mismo binomio</strong> en ambos grupos; si no aparece, conviene revisar los signos.</p>"))}
{caja("tip", t("Another road: multiply and divide by a", "Otro camino: el aspa simple"), t("<p>You can also multiply and divide by a, factor as if a were 1, and simplify. For 2x² + 7x + 3: [(2x)² + 7(2x) + 6] ÷ 2 = (2x + 6)(2x + 1) ÷ 2 = (x + 3)(2x + 1). The two numbers are the same ones (6 and 1), and the divisor always disappears when you simplify. If it does not, one of the numbers is wrong.</p>",
 "<p>También se puede multiplicar y dividir por a, factorizar como si a fuera 1 y simplificar. Para 2x² + 7x + 3: [(2x)² + 7(2x) + 6] ÷ 2 = (2x + 6)(2x + 1) ÷ 2 = (x + 3)(2x + 1). Los dos números son los mismos (6 y 1), y el divisor siempre desaparece al simplificar. Si no desaparece, uno de los números está mal.</p>"))}
{practica("p4", t("Practice 4 — 2x² + 5x + 2", "Práctica 4 — 2x² + 5x + 2"), t("Choose the correct factorization of 2x² + 5x + 2.", "Seleccione la factorización correcta de 2x² + 5x + 2."), [("a", "(2x + 2)(x + 1)"), ("b", "(2x + 1)(x + 2)"), ("c", "(x + 1)(x + 2)")])}
{practica("p5", t("Practice 5 — 3x² + 7x + 2", "Práctica 5 — 3x² + 7x + 2"), t("Choose the correct factorization of 3x² + 7x + 2.", "Seleccione la factorización correcta de 3x² + 7x + 2."), [("a", "(3x + 1)(x + 2)"), ("b", "(3x + 2)(x + 1)"), ("c", "(x + 1)(x + 2)")])}
{practica("p6", t("Practice 6 — 2x² − 7x + 3", "Práctica 6 — 2x² − 7x + 3"), t("Choose the correct factorization of 2x² − 7x + 3.", "Seleccione la factorización correcta de 2x² − 7x + 3."), [("a", "(2x − 3)(x − 1)"), ("b", "(2x + 1)(x − 3)"), ("c", "(2x − 1)(x − 3)")])}
{enlace(n, "ac", t("the ac method and multiplying and dividing by a", "el método ac y el aspa simple"), t("Choose a road, see the steps, and type the two binomials.", "Elija un camino, vea los pasos y escriba los dos binomios."))}'''

    s3 = f'''<p>{t("Some trinomials are <strong>perfect squares</strong>: they come from squaring a binomial. For example, 4x² − 12x + 9 = (2x − 3)², because (2x)² = 4x², 3² = 9 and 2 · 2x · 3 = 12x.", "Algunos trinomios son <strong>cuadrados perfectos</strong>: provienen de elevar un binomio al cuadrado. Por ejemplo, 4x² − 12x + 9 = (2x − 3)², porque (2x)² = 4x², 3² = 9 y 2 · 2x · 3 = 12x.")}</p>
<p>{t("And, as always, before you factor a trinomial, take out the common factor if there is one. Some trinomials, such as x² + x + 1, cannot be factored with whole numbers: no two whole numbers multiply to 1 and add to 1.", "Y, como siempre, antes de factorizar un trinomio conviene sacar primero el factor común si lo hay. Algunos trinomios, como x² + x + 1, no se pueden factorizar con números enteros: no hay dos enteros que multiplicados den 1 y sumados den 1.")}</p>
{ejemplo(t("Example 5: common factor first. Factor 2x² + 10x + 12 completely.", "Ejemplo 5 · Factor común primero. Factorizar 2x² + 10x + 12 completamente."),
  [("1", t("Common factor 2.", "Factor común 2."), "2(x² + 5x + 6)."), ("2", t("Factor the trinomial.", "Se factoriza el trinomio."), "x² + 5x + 6 = (x + 2)(x + 3)."), ("3", t("The complete result.", "Resultado completo."), "2(x + 2)(x + 3)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>2(x + 2)(x + 3)</strong>.")])}
{caja("ojo", t("Always check by expanding", "Verifique siempre por expansión"), t("<p>When you multiply the factors, including the common factor, you must get the original trinomial back. If something does not match, check the two numbers and the signs.</p>", "<p>Al multiplicar los factores, incluido el factor común, debe recuperarse el trinomio original. Si algo no cuadra, revise los dos números y los signos.</p>"))}
{practica("p7", t("Practice 7 — All the way", "Práctica 7 — Hasta el final"), t("Factor 3x² − 12x + 12 completely.", "Factorice completamente 3x² − 12x + 12."), [("a", "3(x² − 4x + 4)"), ("b", "3(x − 2)²"), ("c", "(3x − 6)(x − 2)")])}
{enlace(n, t("complete", "completa"), t("special cases and complete factoring", "casos especiales y factorización completa"), t("Take out the common factor, decide what kind of trinomial is left, and finish the factorization.", "Extraiga el factor común, decida qué clase de trinomio queda y termine la factorización."))}'''

    secciones = [("s-" + t("a-one", "a-uno"), t("Trinomials with a = 1: two numbers", "Trinomios con a = 1: dos números"), s1),
                 ("s-ac", t("Trinomials with a ≠ 1: the ac method", "Trinomios con a ≠ 1: el método ac"), s2),
                 ("s-" + t("complete", "completa"), t("Special cases and complete factoring", "Casos especiales y factorización completa"), s3)]

    unos = t("One sign is +, the other −.", "Un signo es +, el otro −.")
    lesson = {"next": t("Lesson 4.1", "Lección 4.1"), "review": t("sections 1 and 2", "las secciones 1 y 2"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("1 · 6 = 6, but 1 + 6 = 7, not 5.", "1 · 6 = 6, pero 1 + 6 = 7, no 5."), "c": t("−2 + (−3) = −5, not +5.", "−2 + (−3) = −5, no +5.")}, "right": t("2 · 3 = 6 and 2 + 3 = 5.", "2 · 3 = 6 y 2 + 3 = 5."), "solution": "(x + 2)(x + 3)."},
      "p2": {"ok": "c", "hints": {"a": t("3 + (−2) = 1, not −1.", "3 + (−2) = 1, no −1."), "b": t("(−2)(−3) = +6, not −6.", "(−2)(−3) = +6, no −6.")}, "right": t("(−3) · 2 = −6 and −3 + 2 = −1.", "(−3) · 2 = −6 y −3 + 2 = −1."), "solution": "(x − 3)(x + 2)."},
      "p3": {"ok": "a", "hints": {"b": t("4 + 5 = 9, but the middle term is −9x.", "4 + 5 = 9, pero el término del medio es −9x."), "c": t("−2 + (−10) = −12, not −9.", "−2 + (−10) = −12, no −9.")}, "right": t("(−4)(−5) = 20 and −4 + (−5) = −9.", "(−4)(−5) = 20 y −4 + (−5) = −9."), "solution": "(x − 4)(x − 5)."},
      "p4": {"ok": "b", "hints": {"a": t("2x + 2 has a common factor 2, but 2x² + 5x + 2 does not.", "2x + 2 tiene factor común 2, pero 2x² + 5x + 2 no."), "c": t("(x + 1)(x + 2) starts with x², not 2x².", "(x + 1)(x + 2) empieza con x², no con 2x².")}, "right": "(2x + 1)(x + 2) = 2x² + 5x + 2.", "solution": "(2x + 1)(x + 2)."},
      "p5": {"ok": "a", "hints": {"b": t("Multiply: the middle term is 3x + 2x = 5x, not 7x.", "Multiplique: el término del medio es 3x + 2x = 5x, no 7x."), "c": t("(x + 1)(x + 2) starts with x², not 3x².", "(x + 1)(x + 2) empieza con x², no con 3x².")}, "right": "(3x + 1)(x + 2) = 3x² + 7x + 2.", "solution": "(3x + 1)(x + 2)."},
      "p6": {"ok": "c", "hints": {"a": t("Multiply: the middle term is −2x − 3x = −5x.", "Multiplique: el término del medio es −2x − 3x = −5x."), "b": t("1 · (−3) = −3, but the constant is +3.", "1 · (−3) = −3, pero el término independiente es +3.")}, "right": "(2x − 1)(x − 3) = 2x² − 7x + 3.", "solution": "(2x − 1)(x − 3)."},
      "p7": {"ok": "b", "hints": {"a": t("x² − 4x + 4 can still be factored: it is a perfect square.", "x² − 4x + 4 todavía se puede factorizar: es un cuadrado perfecto."), "c": t("3x − 6 still has a common factor 3.", "3x − 6 todavía tiene factor común 3.")}, "right": "3(x − 2)² = 3(x² − 4x + 4) = 3x² − 12x + 12.", "solution": "3(x − 2)²."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("1 + 15 = 16, not 8.", "1 + 15 = 16, no 8."), "c": t("−3 + (−5) = −8, not +8.", "−3 + (−5) = −8, no +8."), "d": t("4 · 4 = 16, not 15.", "4 · 4 = 16, no 15.")}, "solution": "(x + 3)(x + 5)."},
      "B": {"ok": "c", "hints": {"a": t("3 + 4 = 7, but the middle term is −7x.", "3 + 4 = 7, pero el término del medio es −7x."), "b": t("−2 + (−6) = −8.", "−2 + (−6) = −8."), "d": t("−1 + (−12) = −13.", "−1 + (−12) = −13.")}, "solution": "(x − 3)(x − 4)."},
      "C": {"ok": "d", "hints": {"a": t("−5 + 3 = −2, not +2.", "−5 + 3 = −2, no +2."), "b": t("15 + (−1) = 14.", "15 + (−1) = 14."), "c": t("5 · 3 = +15, not −15.", "5 · 3 = +15, no −15.")}, "solution": "(x + 5)(x − 3)."},
      "D": {"ok": "a", "hints": {"b": t("4 + (−2) = 2, not −2.", "4 + (−2) = 2, no −2."), "c": t("−8 + 1 = −7.", "−8 + 1 = −7."), "d": t("(−4)(−2) = +8, not −8.", "(−4)(−2) = +8, no −8.")}, "solution": "(x − 4)(x + 2)."},
      "E": {"ok": "d", "hints": {"a": t("Multiply: the middle term is 2x + 3x = 5x.", "Multiplique: el término del medio es 2x + 3x = 5x."), "b": t("It must start with 2x².", "Debe empezar con 2x²."), "c": t("1 · 1 = 1, not 3.", "1 · 1 = 1, no 3.")}, "solution": "(2x + 1)(x + 3)."},
      "F": {"ok": "c", "hints": {"a": t("Multiply: the middle term is −12x − 2x = −14x.", "Multiplique: el término del medio es −12x − 2x = −14x."), "b": t("The middle term is negative: both numbers are negative.", "El término del medio es negativo: los dos números son negativos."), "d": t("It must start with 3x².", "Debe empezar con 3x².")}, "solution": "(3x − 4)(x − 2)."},
      "G": {"ok": "a", "hints": {"b": t("Multiply: the middle term is 6x − x = 5x, not −5x.", "Multiplique: el término del medio es 6x − x = 5x, no −5x."), "c": t("Multiply: the middle term is 2x − 3x = −x.", "Multiplique: el término del medio es 2x − 3x = −x."), "d": t("Multiply: the middle term is −2x + 3x = x.", "Multiplique: el término del medio es −2x + 3x = x.")}, "solution": "(2x + 1)(x − 3)."},
      "H": {"ok": "b", "hints": {"a": t("x² − x − 2 can still be factored.", "x² − x − 2 todavía se puede factorizar."), "c": t("3x − 6 still has a common factor 3.", "3x − 6 todavía tiene factor común 3."), "d": t("3(x + 2)(x − 1) = 3x² + 3x − 6: the middle sign is wrong.", "3(x + 2)(x − 1) = 3x² + 3x − 6: el signo del medio no coincide.")}, "solution": "3(x − 2)(x + 1)."},
     }}

    quiz = [
     ("A", t("Factor x² + 8x + 15.", "Factorice x² + 8x + 15."), [("a", "(x + 1)(x + 15)"), ("b", "(x + 3)(x + 5)"), ("c", "(x − 3)(x − 5)"), ("d", "(x + 4)(x + 4)")]),
     ("B", t("Factor x² − 7x + 12.", "Factorice x² − 7x + 12."), [("a", "(x + 3)(x + 4)"), ("b", "(x − 2)(x − 6)"), ("c", "(x − 3)(x − 4)"), ("d", "(x − 1)(x − 12)")]),
     ("C", t("Factor x² + 2x − 15.", "Factorice x² + 2x − 15."), [("a", "(x − 5)(x + 3)"), ("b", "(x + 15)(x − 1)"), ("c", "(x + 5)(x + 3)"), ("d", "(x + 5)(x − 3)")]),
     ("D", t("Factor x² − 2x − 8.", "Factorice x² − 2x − 8."), [("a", "(x − 4)(x + 2)"), ("b", "(x + 4)(x − 2)"), ("c", "(x − 8)(x + 1)"), ("d", "(x − 4)(x − 2)")]),
     ("E", t("Factor 2x² + 7x + 3.", "Factorice 2x² + 7x + 3."), [("a", "(2x + 3)(x + 1)"), ("b", "(x + 1)(x + 3)"), ("c", "(2x + 1)(x + 1)"), ("d", "(2x + 1)(x + 3)")]),
     ("F", t("Factor 3x² − 10x + 8.", "Factorice 3x² − 10x + 8."), [("a", "(3x − 2)(x − 4)"), ("b", "(3x + 4)(x + 2)"), ("c", "(3x − 4)(x − 2)"), ("d", "(x − 4)(x − 2)")]),
     ("G", t("Factor 2x² − 5x − 3.", "Factorice 2x² − 5x − 3."), [("a", "(2x + 1)(x − 3)"), ("b", "(2x − 1)(x + 3)"), ("c", "(2x − 3)(x + 1)"), ("d", "(2x + 3)(x − 1)")]),
     ("H", t("Factor 3x² − 3x − 6 completely.", "Factorice completamente 3x² − 3x − 6."), [("a", "3(x² − x − 2)"), ("b", "3(x − 2)(x + 1)"), ("c", "(3x − 6)(x + 1)"), ("d", "3(x + 2)(x − 1)")])]

    tarea = (t("For your own work, with your notebook open and no calculator: (1) The factoring ladder, at your own pace. Level 1: x² + 7x + 12 and x² − 5x + 6. Level 2: x² − x − 12 and x² + 3x − 10. Level 3: 2x² + 7x + 3 and 3x² − 10x + 8. Level 4: 4x² − 12x + 9 (a perfect square). (2) Product and sum: for x² + 9x + 20, x² − 2x − 15, 2x² + 11x + 5, and 6x² + x − 2, first complete the sentence “two numbers that multiply to ___ and add to ___,” and only then write the binomials. (3) All the way: factor 2x² + 10x + 12, 3x² − 12x + 12, and 5x² − 5 completely, taking out the common factor first. Check each one by expanding and explain why the factorization is complete. Then do a round of each activity on the practice page, solving each exercise on paper before you type the answer. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto y sin calculadora: (1) La escalera de factorización, a su ritmo. Nivel 1: x² + 7x + 12 y x² − 5x + 6. Nivel 2: x² − x − 12 y x² + 3x − 10. Nivel 3: 2x² + 7x + 3 y 3x² − 10x + 8. Nivel 4: 4x² − 12x + 9 (cuadrado perfecto). (2) Producto y suma: para x² + 9x + 20, x² − 2x − 15, 2x² + 11x + 5 y 6x² + x − 2, complete primero la frase «dos números que multiplican a ___ y suman ___» y solo después escriba los binomios. (3) Hasta el final: factorice por completo 2x² + 10x + 12, 3x² − 12x + 12 y 5x² − 5, sacando primero el factor común. Verifique cada una expandiendo y explique por qué la factorización está completa. Después haga una ronda de cada actividad de la página de práctica, resolviendo cada ejercicio en papel antes de escribir la respuesta. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Make a set of cards: on one side a trinomial (x² + 7x + 12, x² − x − 6, 2x² + 7x + 3, …), on the other its factors. Shuffle them and play with someone at home: one reads the factors and the other multiplies to find the trinomial.",
               "Haga unas tarjetas: por un lado un trinomio (x² + 7x + 12, x² − x − 6, 2x² + 7x + 3, …) y por el otro sus factores. Barájelas y juegue con alguien en casa: uno lee los factores y el otro multiplica para hallar el trinomio."))

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Factor trinomials by finding two numbers whose product and sum fit, use the ac method when a ≠ 1, and always factor completely.", "Factorice trinomios hallando dos números cuyo producto y suma encajen, use el método ac cuando a ≠ 1 y factorice siempre por completo."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Factor</strong> x² + bx + c by finding two numbers whose product is c and whose sum is b.", "<strong>Factorizar</strong> trinomios x² + bx + c hallando dos números cuyo producto sea c y cuya suma sea b."),
         t("<strong>Factor</strong> ax² + bx + c (a ≠ 1) with the ac method (product and sum).", "<strong>Factorizar</strong> trinomios ax² + bx + c (a ≠ 1) con el método ac (producto y suma)."),
         t("<strong>Combine</strong> the common factor with factoring trinomials when needed.", "<strong>Combinar</strong> el factor común con la factorización de trinomios cuando sea necesario."),
         t("<strong>Check</strong> every factorization by expanding.", "<strong>Verificar</strong> cada factorización expandiendo.")],
        secciones, tarea, quiz,
        t("Self-check checklist for factoring trinomials", "Lista de autoevaluación de la factorización de trinomios"),
        t("Self-check checklist: skills for factoring trinomials", "Lista de autoevaluación: destrezas de la factorización de trinomios"),
        [(t("Trinomials with a = 1", "Trinomios con a = 1"), t("I find the two numbers (product and sum) and read the sign pattern quickly.", "Hallo los dos números (producto y suma) y reconozco el patrón de signos al instante."), t("I find the numbers but make a mistake with a sign.", "Hallo los números, pero me equivoco en el signo."), t("I do not find the two numbers or I ignore the signs.", "No hallo los dos números o ignoro los signos.")),
         (t("Trinomials with a ≠ 1", "Trinomios con a ≠ 1"), t("I use the ac method surely and check the common binomial.", "Aplico el método ac con seguridad y verifico el binomio común."), t("I use the ac method but make mistakes when I group.", "Aplico el método ac, pero fallo al agrupar."), t("I do not use the ac method.", "No aplico el método ac.")),
         (t("Combining with the common factor", "Combinar con factor común"), t("I factor completely and check by expanding.", "Factorizo por completo y verifico expandiendo."), t("I take out the common factor but do not factor the trinomial left.", "Saco el factor común, pero no factorizo el trinomio que queda."), t("I forget to take out the common factor.", "Olvido sacar el factor común."))],
        t("<p>This lesson closes Topic 3. You learned to factor trinomials with a = 1 (finding two numbers whose product is c and whose sum is b) and with a ≠ 1 (the ac method and grouping), always combining with the common factor and checking by expanding.</p>\n<p>Topic 4 · Quadratic equations begins with <strong>Lesson 4.1 · Solving quadratic equations by factoring</strong>. All this factoring now has a powerful purpose: finding the solutions of an equation. With the zero product property (if A · B = 0, then A = 0 or B = 0), each factor will give you a solution.</p>",
          "<p>Con esta lección se cierra el Tema 3. Se aprendió a factorizar trinomios con a = 1 (buscando dos números cuyo producto es c y cuya suma es b) y con a ≠ 1 (método ac y agrupación), combinando siempre con el factor común y verificando por expansión.</p>\n<p>El Tema 4 · Ecuaciones cuadráticas comienza con la <strong>Lección 4.1 · Resolver ecuaciones cuadráticas por factorización</strong>. Toda esta destreza de factorizar tendrá ahora un propósito potente: hallar las soluciones de una ecuación. Usando la propiedad del producto cero (si A · B = 0, entonces A = 0 o B = 0), cada factor revelará una solución.</p>"),
        ("4-1", ("", t("Lesson 4.1 · Solving quadratic equations by factoring", "Lección 4.1 · Resolver ecuaciones cuadráticas por factorización"))),
        [(t("trinomial", "trinomio"), t("A polynomial with three terms, such as x² + 7x + 12.", "Un polinomio de tres términos, como x² + 7x + 12.")),
         (t("ac method", "método ac"), t("Find two numbers with product a · c and sum b, split the middle term with them, and group.", "Buscar dos números de producto a · c y suma b, partir con ellos el término del medio y agrupar.")),
         (t("grouping", "agrupación"), t("Taking out the common factor of each pair of terms so that the same binomial appears.", "Extraer el factor común de cada par de términos para que aparezca el mismo binomio.")),
         (t("perfect square trinomial", "trinomio cuadrado perfecto"), "a² ± 2ab + b² = (a ± b)²"),
         (t("factored completely", "factorizado completamente"), t("When no factor can be factored any further.", "Cuando ningún factor se puede seguir factorizando."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function F(k, m, f){ return {k: k, m: m || 0, f: f || []}; }
function bin(a, b){ return [b, a]; }
function tri(a, b, c){ return pDe({2: a, 1: b, 0: c}); }
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function mas(v){ return (v < 0 ? " − " : " + ") + Math.abs(v); }
function binV(a, b){ return "(" + tVis(a, 1, true) + mas(b) + ")"; }
var FAC_AYUDA = T("Type the factors with parentheses, like (x\u00a0+\u00a03)(x\u00a0−\u00a04) or 2(x\u00a0+\u00a01)(x\u00a0+\u00a05).", "Escriba los factores con paréntesis, como (x\u00a0+\u00a03)(x\u00a0−\u00a04) o 2(x\u00a0+\u00a01)(x\u00a0+\u00a05).");
var Y = T(" and ", " y ");

/* ===== MODULE 1 · a = 1: two numbers ===== */
function casoUno(){ var p, q; do { p = nz(-9, 9); q = nz(-9, 9); } while (p + q === 0 || Math.abs(p * q) > 60); return {p: p, q: q, b: p + q, c: p * q, poly: tri(1, p + q, p * q), FF: F(1, 0, [bin(1, p), bin(1, q)])}; }
function signosUno(b, c){ return c > 0 ? (b > 0 ? T("c is positive and b is positive: both numbers are positive.", "c es positivo y b es positivo: los dos números son positivos.") : T("c is positive and b is negative: both numbers are negative.", "c es positivo y b es negativo: los dos números son negativos.")) : T("c is negative: one number is positive and the other negative.", "c es negativo: un número es positivo y el otro negativo."); }
function paresDe(c){ var l = [], a = Math.abs(c); for (var d = 1; d * d <= a; d++) if (a % d === 0){ var e = a / d; if (c > 0){ l.push([d, e]); l.push([-d, -e]); } else { l.push([d, -e]); l.push([-d, e]); } } return l; }
var PU = casoUno();
function puDibuja(marca){
  $("pu-enun").innerHTML = T("Trinomial: ", "Trinomio: ") + pHTML(PU.poly) + ". " + T("Look for two numbers with product ", "Se buscan dos números de producto ") + sg(PU.c) + T(" and sum ", " y suma ") + sg(PU.b) + ".";
  var filas = paresDe(PU.c).map(function(pq){ var ok = pq[0] + pq[1] === PU.b; if (ok) PU.par = sg(pq[0]) + Y + sg(pq[1]); return '<tr' + (marca && ok ? ' class="fila-ok"' : "") + '><td>' + sg(pq[0]) + "</td><td>" + sg(pq[1]) + "</td><td>" + sg(pq[0] * pq[1]) + "</td><td>" + sg(pq[0] + pq[1]) + (marca && ok ? " ✓" : "") + "</td></tr>"; }).join("");
  $("pu-tabla").innerHTML = filas;
  $("pu-txt").innerHTML = '<div class="linea">' + signosUno(PU.b, PU.c) + "</div>" + (marca ? '<div class="linea">' + T("The pair is ", "El par es ") + PU.par + ": " + pVis(PU.poly) + " = " + fVis(PU.FF) + ".</div>" : "");
}
$("pu-marca").addEventListener("click", function(){ puDibuja(true); });
$("pu-otro").addEventListener("click", function(){ PU = casoUno(); puDibuja(false); });
puDibuja(false);
function parClave(a, b){ return [a, b].sort(function(x, y){ return x - y; }).join(","); }
OMR("un", function(){
  var c = casoUno(), ok = parClave(c.p, c.q), vistos = {}, ops = [{clave: ok, html: sg(c.p) + Y + sg(c.q)}]; vistos[ok] = 1;
  var cand = [[-c.p, -c.q], [c.p, -c.q], [-c.p, c.q]].concat(paresDe(c.c)).concat([[c.p + 1, c.q - 1], [c.p - 1, c.q + 1]]);
  cand.forEach(function(pq){ var k = parClave(pq[0], pq[1]); if (ops.length < 4 && !vistos[k] && pq[0] && pq[1]){ vistos[k] = 1; ops.push({clave: k, html: sg(pq[0]) + Y + sg(pq[1])}); } });
  var pistas = {}; ops.forEach(function(o){ if (o.clave === ok) return; var v = o.clave.split(",").map(Number); pistas[o.clave] = v[0] * v[1] !== c.c ? T("Their product is ", "Su producto es ") + sg(v[0] * v[1]) + T(", not ", ", no ") + sg(c.c) + "." : T("Their sum is ", "Su suma es ") + sg(v[0] + v[1]) + T(", not ", ", no ") + sg(c.b) + "."; });
  return {enun: T("Which two numbers factor ", "¿Qué dos números factorizan ") + pHTML(c.poly) + "?", correcta: ok, opciones: ops, porClave: pistas,
    pista: T("Multiply them and add them.", "Multiplíquelos y súmelos."), bien: sg(c.p) + " · " + pn(c.q) + " = " + sg(c.c) + Y + sg(c.p) + " + " + pn(c.q) + " = " + sg(c.b) + ". " + pVis(c.poly) + " = " + fVis(c.FF) + "."};
});
creaPracticaLibre("uq", function(){ var c = casoUno();
  return {enun: T("Factor ", "Factorice ") + pHTML(c.poly) + ". " + FAC_AYUDA,
    evalua: function(txt){ return evaluaF(txt, c.poly, [{F: F(1, 0, [bin(1, -c.p), bin(1, -c.q)]), msg: T("The numbers are right but the signs are not. Check the sign rule.", "Los números están bien, pero los signos no. Revise la regla de los signos.")}]); },
    solucion: T("Two numbers with product ", "Dos números de producto ") + sg(c.c) + T(" and sum ", " y suma ") + sg(c.b) + ": " + sg(c.p) + Y + sg(c.q) + ". " + pVis(c.poly) + " = " + fVis(c.FF) + "."};
});

/* ===== MODULE 2 · a ≠ 1: the ac method and multiplying and dividing by a ===== */
var RUTA = "ac";
function casoAC(){
  var a1, a2, b1, b2, a, b, c, n = 0;
  do { a1 = elige([2, 2, 3, 3, 4, 5]); a2 = elige([1, 1, 1, 2, 3]); b1 = nz(-7, 7); b2 = nz(-7, 7); a = a1 * a2; b = a1 * b2 + a2 * b1; c = b1 * b2; n++; }
  while ((mcd(a1, b1) !== 1 || mcd(a2, b2) !== 1 || a < 2 || !b || Math.abs(b) > 40 || Math.abs(c) > 49 || mcd(mcd(a, Math.abs(b)), Math.abs(c)) !== 1) && n < 300);
  return {a1: a1, b1: b1, a2: a2, b2: b2, a: a, b: b, c: c, m: a1 * b2, nn: a2 * b1, poly: tri(a, b, c), FF: F(1, 0, [bin(a1, b1), bin(a2, b2)])};
}
function pasosAC(k, ruta){
  var a = k.a, b = k.b, c = k.c, m = k.m, n = k.nn, P = [];
  P.push("a · c = " + a + " · " + pn(c) + " = <strong>" + sg(a * c) + "</strong>.");
  P.push(T("Two numbers with product ", "Dos números de producto ") + sg(a * c) + T(" and sum ", " y suma ") + sg(b) + ": <strong>" + sg(m) + Y + sg(n) + "</strong>.");
  if (ruta === "ac"){
    P.push(T("Split the middle term: ", "Se parte el término del medio: ") + tVis(a, 2, true) + (m < 0 ? " − " : " + ") + tVis(Math.abs(m), 1, true) + (n < 0 ? " − " : " + ") + tVis(Math.abs(n), 1, true) + mas(c) + ".");
    P.push(T("Group two and two: ", "Se agrupa de dos en dos: ") + tVis(k.a1, 1, true) + binV(k.a2, k.b2) + (k.b1 < 0 ? " − " : " + ") + Math.abs(k.b1) + binV(k.a2, k.b2) + ". " + T("The same binomial appears twice.", "El mismo binomio aparece dos veces."));
  } else {
    P.push(T("Multiply and divide by ", "Se multiplica y se divide por ") + a + ": [(" + a + "x)<sup>2</sup>" + (b < 0 ? " − " : " + ") + Math.abs(b) + "(" + a + "x)" + mas(a * c) + "] ÷ " + a + ".");
    P.push(T("Factor as if the coefficient were 1, with the two numbers: ", "Se factoriza como si el coeficiente fuera 1, con los dos números: ") + "[" + binV(a, m) + binV(a, n) + "] ÷ " + a + ".");
    var s1 = binV(a, m) + " = " + k.a1 + binV(k.a2, k.b2), s2 = k.a2 > 1 ? binV(a, n) + " = " + k.a2 + binV(k.a1, k.b1) : binV(a, n) + T(" stays the same", " queda igual");
    P.push(T("Simplify: ", "Se simplifica: ") + s1 + Y + s2 + ". " + (k.a2 > 1 ? k.a1 + " · " + k.a2 + " = " + a + T(", which cancels the divisor.", ", que cancela el divisor.") : T("The factor ", "El factor ") + k.a1 + T(" cancels the divisor.", " cancela el divisor.")));
  }
  P.push(T("Result: ", "Resultado: ") + "<strong>" + binV(k.a1, k.b1) + binV(k.a2, k.b2) + "</strong>. " + T("Multiplying gives back ", "Al multiplicar se recupera ") + pVis(k.poly) + ".");
  return P;
}
pasoAPaso4("ac", function(){ var k = casoAC(); return {enun: T("Factor ", "Factorice ") + pHTML(k.poly) + (RUTA === "ac" ? T(" with the ac method.", " con el método ac.") : T(" by multiplying and dividing by a.", " con el aspa simple (multiplicar y dividir por a).")), pasos: pasosAC(k, RUTA)}; });
function ruta(r){ RUTA = r; $("ru-ac").setAttribute("aria-pressed", r === "ac" ? "true" : "false"); $("ru-aspa").setAttribute("aria-pressed", r === "aspa" ? "true" : "false"); $("ac-nuevo").click(); }
$("ru-ac").addEventListener("click", function(){ ruta("ac"); });
$("ru-aspa").addEventListener("click", function(){ ruta("aspa"); });
creaPracticaLibre("aq", function(){ var k = casoAC();
  return {enun: T("Factor ", "Factorice ") + pHTML(k.poly) + ". " + FAC_AYUDA,
    evalua: function(txt){ return evaluaF(txt, k.poly, [{F: F(1, 0, [bin(k.a1, k.b2), bin(k.a2, k.b1)]), msg: T("The numbers are in the wrong binomials. Multiply to check the middle term.", "Los números están en el binomio equivocado. Multiplique para comprobar el término del medio.")},
      {F: F(1, 0, [bin(k.a1, -k.b1), bin(k.a2, -k.b2)]), msg: T("The numbers are right but the signs are not.", "Los números están bien, pero los signos no.")}].filter(function(tp){ return !pIgual(fProducto(tp.F), k.poly); })); },
    solucion: pasosAC(k, "ac").join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 3 · Special cases and complete factoring ===== */
var TIPOS = {cuad: T("A perfect square trinomial", "Un trinomio cuadrado perfecto"), dos: T("A trinomial that factors into two different binomials", "Un trinomio que se factoriza en dos binomios distintos"), no: T("A trinomial that cannot be factored with whole numbers", "Un trinomio que no se puede factorizar con números enteros")};
function casoComp(tipo){
  tipo = tipo || elige(["cuad", "dos", "dos", "no"]);
  var g = elige([1, 2, 2, 3, 3, 4, 5]), dentro, FF, a, b, p, q;
  if (tipo === "cuad"){ do { p = elige([1, 1, 2, 3]); q = nz(-6, 6); } while (mcd(p, Math.abs(q)) !== 1); dentro = pMul(bin(p, q), bin(p, q)); FF = F(g, 0, [bin(p, q), bin(p, q)]); }
  else if (tipo === "dos"){ if (Math.random() < .6){ do { p = nz(-7, 7); q = nz(-7, 7); } while (p === q || p + q === 0); dentro = tri(1, p + q, p * q); FF = F(g, 0, [bin(1, p), bin(1, q)]); } else { var k = casoAC(); while (k.a1 === k.a2 && k.b1 === k.b2) k = casoAC(); while (k.a > 6 || (k.a1 === k.a2 && k.b1 === k.b2)) k = casoAC(); dentro = k.poly; FF = k.FF; FF.k = g; } }
  else { do { b = nz(-7, 7); a = nz(-9, 12); } while (b * b - 4 * a >= 0 && esCuadrado(b * b - 4 * a)); dentro = tri(1, b, a); FF = F(g, 0, [dentro]); }
  if (g === 1 && tipo === "no") g = elige([2, 3]), FF.k = g;
  return {tipo: tipo, g: g, dentro: dentro, FF: FF, poly: pEsc(dentro, g)};
}
function pasosComp(k){
  var P = [k.g > 1 ? T("Common factor first: ", "Primero el factor común: ") + pVis(k.poly) + " = " + k.g + "(" + pVis(k.dentro) + ")." : T("There is no common factor (only 1).", "No hay factor común (solo 1).")];
  if (k.tipo === "cuad"){ var r = k.FF.f[0]; P.push(T("The trinomial inside is a perfect square: ", "El trinomio de dentro es un cuadrado perfecto: ") + pVis(k.dentro) + " = " + binV(r[1], r[0]) + "<sup>2</sup>."); }
  else if (k.tipo === "dos") P.push(T("The trinomial inside factors: ", "El trinomio de dentro se factoriza: ") + pVis(k.dentro) + " = " + fVis(F(1, 0, k.FF.f)) + ".");
  else P.push(T("The trinomial inside cannot be factored with whole numbers: no two whole numbers multiply to ", "El trinomio de dentro no se puede factorizar con enteros: no hay dos enteros que multiplicados den ") + sg(k.dentro[0]) + T(" and add to ", " y sumados den ") + sg(k.dentro[1]) + ".");
  P.push(T("Complete factorization: ", "Factorización completa: ") + "<strong>" + fVis(k.FF) + "</strong>.");
  return P;
}
pasoAPaso4("cp", function(){ var k = casoComp(); return {enun: T("Factor completely: ", "Factorice completamente: ") + pHTML(k.poly) + ".", pasos: pasosComp(k)}; });
OMR("ct", function(){ var k = casoComp(); while (k.g === 1) k = casoComp(k.tipo);
  var ops = ["cuad", "dos", "no"].map(function(x){ return {clave: x, html: TIPOS[x]}; });
  return {enun: T("Take out the common factor of ", "Extraiga el factor común de ") + pHTML(k.poly) + ": " + k.g + "(" + pHTML(k.dentro) + "). " + T("What is left inside the parentheses?", "¿Qué queda dentro del paréntesis?"), correcta: k.tipo, opciones: ops,
    porClave: {cuad: T("Is the first term a square, the last a square, and the middle twice their product?", "¿Es el primer término un cuadrado, el último un cuadrado y el del medio el doble de su producto?"), dos: T("Look for two whole numbers with the right product and sum. Do they exist? Are they different?", "Busque dos enteros con el producto y la suma correctos. ¿Existen? ¿Son distintos?"), no: T("Look again: there are two whole numbers with that product and that sum.", "Mire otra vez: sí hay dos enteros con ese producto y esa suma.")},
    pista: T("Try to find the two numbers.", "Intente hallar los dos números."), bien: pasosComp(k).slice(1).join(" ").replace(/<\/?strong>/g, "")};
});
creaPracticaLibre("pq", function(){ var k = casoComp(elige(["cuad", "dos", "dos"]));
  return {enun: T("Factor completely: ", "Factorice completamente: ") + pHTML(k.poly) + ". " + FAC_AYUDA + T(" For a square you can write (x + 3)^2.", " Para un cuadrado puede escribir (x + 3)^2."),
    evalua: function(txt){ return evaluaF(txt, k.poly, k.g > 1 ? [{p: k.dentro, msg: T("You lost the common factor " + k.g + ": multiply and you will see that you do not get the trinomial back.", "Se perdió el factor común " + k.g + ": multiplique y verá que no recupera el trinomio.")}] : []); },
    solucion: pasosComp(k).join(" ").replace(/<\/?strong>/g, "")};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    mods = [
     (t("a-one", "a-uno"), t("Trinomials with a = 1: two numbers", "Trinomios con a = 1: dos números"),
      f'''      <p>{t("To factor x² + bx + c, look for two numbers whose product is c and whose sum is b. The table lists every pair of whole numbers with product c; look at the sum column and find b.", "Para factorizar x² + bx + c se buscan dos números cuyo producto sea c y cuya suma sea b. La tabla muestra todos los pares de enteros de producto c; mire la columna de la suma y busque b.")}</p>
      <div class="panel"><p class="enun" id="pu-enun"></p>
        <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Pairs of whole numbers with product c and their sums", "Pares de enteros de producto c y sus sumas")}</caption><thead><tr><th scope="col">{t("number 1", "número 1")}</th><th scope="col">{t("number 2", "número 2")}</th><th scope="col">{t("product", "producto")}</th><th scope="col">{t("sum", "suma")}</th></tr></thead><tbody id="pu-tabla"></tbody></table></div>
        <div class="fila-btn"><button type="button" class="btn" id="pu-marca">{t("Show the pair that works", "Mostrar el par que sirve")}</button><button type="button" class="btn-sec" id="pu-otro">{t("Another trinomial", "Otro trinomio")}</button></div></div>
{n4.salida("pu-txt")}
      <div class="caja-tip">{t("The signs give you a head start. If c is positive, both numbers have the same sign, the sign of b. If c is negative, one is positive and the other negative.", "Los signos avisan. Si c es positivo, los dos números tienen el mismo signo, el de b. Si c es negativo, uno es positivo y el otro negativo.")}</div>
{B.om("un", t("Practice: choose the two numbers", "Practique: elija los dos números"))}
{libre("uq", t("Practice: type the two binomials", "Practique: escriba los dos binomios"), t("Factored form", "Forma factorizada"))}'''),
     ("ac", t("Trinomials with a ≠ 1: the ac method", "Trinomios con a ≠ 1: el método ac"),
      f'''      <p>{t("Both roads start the same way: find two numbers whose product is a · c and whose sum is b. They also end the same way. Choose a road and compare.", "Los dos caminos empiezan igual —hay que hallar dos números que multiplicados den a · c y sumados den b— y llegan al mismo resultado. Elija un camino y compare.")}</p>
      <div class="modos" role="group" aria-label="{t("Road", "Camino")}"><button type="button" class="btn-sec" id="ru-ac" aria-pressed="true">{t("ac method (grouping)", "Método ac (agrupación)")}</button><button type="button" class="btn-sec" id="ru-aspa" aria-pressed="false">{t("Multiply and divide by a", "Aspa simple (multiplicar y dividir por a)")}</button></div>
{n4.pasos("ac", t("Another trinomial", "Otro trinomio"))}
      <div class="caja-tip">{t("Multiplying and dividing by the same number does not change the trinomial. That is why the divisor must disappear when you simplify: if it does not, one of the two numbers is wrong.", "El aspa simple no cambia el trinomio: multiplicar y dividir por el mismo número deja la expresión igual. Por eso, al final, el divisor tiene que desaparecer al simplificar: si no desaparece, hubo un error en los dos números.")}</div>
{libre("aq", t("Practice: factor the trinomial", "Practique: factorice el trinomio"), t("Factored form", "Forma factorizada"))}'''),
     (t("complete", "completa"), t("Special cases and complete factoring", "Casos especiales y factorización completa"),
      f'''      <p>{t("The order of work never changes: first the common factor, then the trinomial. Some trinomials are perfect squares, and some cannot be factored with whole numbers.", "El orden de trabajo es siempre el mismo: primero el factor común, después el trinomio. Hay trinomios que son cuadrados perfectos y otros que no se pueden factorizar con números enteros.")}</p>
{n4.pasos("cp", t("Another polynomial", "Otro polinomio"))}
{B.om("ct", t("Practice: what is left inside?", "Practique: ¿qué queda dentro?"))}
{libre("pq", t("Practice: factor completely", "Practique: factorice completamente"), t("Factored form", "Forma factorizada"))}
      <div class="caja-atencion"><strong>{t("Check by multiplying.", "Verifique multiplicando.")}</strong> {t("When you expand the factors, including the common factor, the original trinomial must come back. That check catches almost every mistake.", "Al expandir los factores, incluido el factor común, debe reaparecer el trinomio original. Esa comprobación elimina casi todos los errores.")}</div>''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO + ".fila-ok td{background:#e8f5e9;font-weight:700;}", scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Factorización de trinomios (a = 1 y a ≠ 1)")
