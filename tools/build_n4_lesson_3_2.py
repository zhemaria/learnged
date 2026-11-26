"""Level 4 · Lesson 3.2 · Factoring: common factor and difference of squares — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_3-2.html, algebra/n4-l3-2.html (factoring undoes multiplying) and
algebra/interactivo_3-2_factor_comun_diferencia_cuadrados (common factor, difference of squares, both together). They are rebuilt here,
inside LearnGED, with typed factored answers read by math/poly4.js. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "3-2"
TEMA = ("Multiplying and factoring", "Multiplicación y factorización")
TIT = ("Factoring: common factor and difference of squares", "Factorización: factor común y diferencia de cuadrados")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def leccion():
    n = N
    flecha = B.svg("0 0 520 120", t("3(x + 2) and 3x + 6. Multiplying goes from 3(x + 2) to 3x + 6; factoring goes back from 3x + 6 to 3(x + 2).", "3(x + 2) y 3x + 6. Multiplicar va de 3(x + 2) a 3x + 6; factorizar vuelve de 3x + 6 a 3(x + 2)."),
        '<text x="90" y="68" font-size="26" font-weight="700" text-anchor="middle" fill="#0d47a1">3(x + 2)</text><text x="430" y="68" font-size="26" font-weight="700" text-anchor="middle" fill="#1b5e20">3x + 6</text>'
        '<path d="M170 45 H350" stroke="#0d47a1" stroke-width="3" marker-end="url(#fl1)"/><path d="M350 85 H170" stroke="#1b5e20" stroke-width="3" marker-end="url(#fl2)"/>'
        '<defs><marker id="fl1" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#0d47a1"/></marker><marker id="fl2" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#1b5e20"/></marker></defs>'
        f'<text x="260" y="35" font-size="16" font-weight="700" text-anchor="middle" fill="#0d47a1">{t("multiply", "multiplicar")}</text><text x="260" y="108" font-size="16" font-weight="700" text-anchor="middle" fill="#1b5e20">{t("factor", "factorizar")}</text>', 460)
    s1 = f'''<p>{t("<strong>A link with Lesson 3.1.</strong> In Lesson 3.1 you multiplied binomials to get a polynomial. <strong>Factoring is the way back</strong>: you start from the polynomial and find the factors that produced it. That is why the best way to check a factorization is to <strong>multiply again</strong>: if you get the original polynomial, the factorization is right.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 3.1 se multiplicaron binomios para obtener un polinomio. <strong>Factorizar es el camino inverso</strong>: se parte del polinomio y se descubren los factores que lo produjeron. Por eso la mejor manera de comprobar una factorización es <strong>volver a multiplicar</strong>: si se obtiene el polinomio original, la factorización es correcta.")}</p>
<p>{t("To <strong>factor</strong> a polynomial means to write it as a product. It is the opposite of multiplying. With numbers it is the same: 3 · 4 = 12 is a multiplication, and writing 12 as 3 · 4 is factoring it.", "<strong>Factorizar</strong> un polinomio significa escribirlo como un producto. Es lo contrario de multiplicar. Con números pasa lo mismo: 3 · 4 = 12 es una multiplicación, y escribir 12 como 3 · 4 es factorizarlo.")}</p>
{flecha}
{caja("tip", t("Always check", "Verificar siempre"), t("<p>After you factor, multiply the factors. If you get the original polynomial, the answer is right. This check catches almost every mistake: the sign (3(x − 2) gives 3x − 6, not 3x + 6) and the incomplete factor (3(x + 6) gives 3x + 18, not 3x + 6).</p>", "<p>Después de factorizar, multiplique los factores. Si obtiene el polinomio original, la respuesta es correcta. Esta comprobación descubre casi todos los errores: el de signo (3(x − 2) da 3x − 6, no 3x + 6) y el de factor incompleto (3(x + 6) da 3x + 18, no 3x + 6).</p>"))}
{enlace(n, t("undo", "deshacer"), t("factoring undoes multiplying", "factorizar deshace la multiplicación"), t("Go from the factored form to the product and back, checking by multiplying.", "Pase de la forma factorizada al producto y vuelva, comprobando al multiplicar."))}'''

    s2 = f'''<p>{t("The first step of any factoring is to look for a <strong>common factor</strong> in all the terms. Take out:", "El primer paso de cualquier factorización es buscar un <strong>factor común</strong> a todos los términos. Se extrae:")}</p>
<ul><li>{t("the <strong>greatest common factor (GCF)</strong> of the coefficients;", "el <strong>máximo común divisor (MCD)</strong> de los coeficientes;")}</li>
<li>{t("the variable with the <strong>smallest exponent</strong> that appears in every term.", "la variable con el <strong>menor exponente</strong> que aparezca en todos los términos.")}</li></ul>
{ejemplo(t("Example 1: factor 6x + 9.", "Ejemplo 1 · Factorizar 6x + 9."),
  [("1", t("GCF of 6 and 9.", "MCD de 6 y 9."), "3."), ("2", t("Take out the 3.", "Se saca el 3."), "6x + 9 = 3(2x + 3)."), ("3", t("Check.", "Verificación."), "3(2x + 3) = 6x + 9. ✓"),
   ("✓", t("Answer.", "Respuesta."), "<strong>3(2x + 3)</strong>.")])}
{ejemplo(t("Example 2: with a variable. Factor 4x² + 8x.", "Ejemplo 2 · Con variable. Factorizar 4x² + 8x."),
  [("1", t("GCF of 4 and 8 is 4; the common variable with the smallest exponent is x.", "El MCD de 4 y 8 es 4; la variable común con menor exponente es x."), ""), ("2", t("Take out 4x.", "Se saca 4x."), "4x² + 8x = 4x(x + 2)."), ("3", t("Check.", "Verificación."), "4x(x + 2) = 4x² + 8x. ✓"),
   ("✓", t("Answer.", "Respuesta."), "<strong>4x(x + 2)</strong>.")])}
{ejemplo(t("Example 3: factor 10x³ − 15x².", "Ejemplo 3 · Factorizar 10x³ − 15x²."),
  [("1", t("GCF of 10 and 15 is 5; the smallest power of x is x².", "El MCD de 10 y 15 es 5; la menor potencia de x es x²."), ""), ("2", t("Take out 5x².", "Se saca 5x²."), "10x³ − 15x² = 5x²(2x − 3)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>5x²(2x − 3)</strong>.")])}
{caja("ojo", t("When a term leaves a 1", "Cuando un término deja un 1"), t("<p>If the whole term is the common factor, a 1 stays in its place: 3x + 3 = 3(x + 1), not 3(x). And the factor must be the greatest one: 2(4x + 6) is not finished, because 4x + 6 still has a common factor 2.</p>", "<p>Si el término entero es el factor común, en su lugar queda un 1: 3x + 3 = 3(x + 1), no 3(x). Y el factor debe ser el mayor: 2(4x + 6) no está terminado, porque 4x + 6 todavía tiene un factor común 2.</p>"))}
{practica("p1", t("Practice 1 — A number in common", "Práctica 1 — Un número en común"), t("Factor 6x + 9.", "Factorice 6x + 9."), [("a", "2(3x + 4)"), ("b", "3(2x + 3)"), ("c", "3(2x + 9)")])}
{practica("p2", t("Practice 2 — With x in common", "Práctica 2 — Con x en común"), t("Factor 4x² + 8x.", "Factorice 4x² + 8x."), [("a", "4x(x + 2)"), ("b", "2x(2x + 4)"), ("c", "4(x² + 2x)")])}
{practica("p3", t("Practice 3 — With x²", "Práctica 3 — Con x²"), t("Factor 10x³ − 15x².", "Factorice 10x³ − 15x²."), [("a", "5x(2x² − 3x)"), ("b", "5x²(2x − 15)"), ("c", "5x²(2x − 3)")])}
{enlace(n, t("common", "comun"), t("the common factor", "el factor común"), t("Find the GCF of the numbers and the smallest power of x, take them out, and check what is left inside.", "Halle el MCD de los coeficientes y la menor potencia de x, extráigalos y compruebe lo que queda dentro."))}'''

    s3 = f'''<p>{t("A binomial of the form a² − b² (a square minus a square) is factored with the identity from Lesson 3.1, now backwards:", "Un binomio de la forma a² − b² (un cuadrado menos otro cuadrado) se factoriza con la identidad de la Lección 3.1, ahora al revés:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">a² − b² = (a + b)(a − b)</p>
{tabla(t("Perfect squares", "Cuadrados perfectos"), t("The perfect squares from 1 to 12", "Los cuadrados perfectos del 1 al 12"), [t("Number", "Número")] + [str(i) for i in range(1, 13)], [[t("Square", "Cuadrado")] + [str(i * i) for i in range(1, 13)]])}
{ejemplo(t("Example 4: factor x² − 9.", "Ejemplo 4 · Factorizar x² − 9."),
  [("1", t("Recognize it.", "Se reconoce."), t("x² is the square of x; 9 is the square of 3.", "x² es el cuadrado de x; 9 es el cuadrado de 3.")), ("2", t("Use the identity.", "Se aplica la identidad."), "x² − 9 = (x + 3)(x − 3)."), ("3", t("Check.", "Verificación."), "(x + 3)(x − 3) = x² − 9. ✓"),
   ("✓", t("Answer.", "Respuesta."), "<strong>(x + 3)(x − 3)</strong>.")])}
{ejemplo(t("Example 5: with a coefficient. Factor 4x² − 25.", "Ejemplo 5 · Con coeficiente. Factorizar 4x² − 25."),
  [("1", t("Recognize it.", "Se reconoce."), t("4x² is the square of 2x; 25 is the square of 5.", "4x² es el cuadrado de 2x; 25 es el cuadrado de 5.")), ("2", t("Use the identity.", "Se aplica la identidad."), "4x² − 25 = (2x + 5)(2x − 5)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>(2x + 5)(2x − 5)</strong>.")])}
{caja("ojo", t("Only differences, not sums", "Solo restas, no sumas"), t("<p>A difference of squares needs a minus sign. A <strong>sum</strong> of squares such as x² + 9 cannot be factored with real numbers. Both terms must also be perfect squares: x² − 10 is not a difference of squares with whole numbers.</p>", "<p>La diferencia de cuadrados requiere un signo menos. Una <strong>suma</strong> de cuadrados como x² + 9 no se factoriza con números reales. Además, los dos términos deben ser cuadrados perfectos: x² − 10 no es una diferencia de cuadrados con números enteros.</p>"))}
{practica("p4", t("Practice 4 — x² − 9", "Práctica 4 — x² − 9"), t("Factor x² − 9.", "Factorice x² − 9."), [("a", "(x − 3)(x − 3)"), ("b", "(x + 9)(x − 1)"), ("c", "(x + 3)(x − 3)")])}
{practica("p5", t("Practice 5 — x² − 49", "Práctica 5 — x² − 49"), t("Factor x² − 49.", "Factorice x² − 49."), [("a", "(x + 7)(x + 7)"), ("b", "(x + 7)(x − 7)"), ("c", "(x − 7)(x − 7)")])}
{practica("p6", t("Practice 6 — 9x² − 1", "Práctica 6 — 9x² − 1"), t("Factor 9x² − 1.", "Factorice 9x² − 1."), [("a", "(3x + 1)(3x − 1)"), ("b", "(3x − 1)(3x − 1)"), ("c", "(9x + 1)(x − 1)")])}
{enlace(n, t("squares", "cuadrados"), t("the difference of squares", "la diferencia de cuadrados"), t("Decide first whether it is a difference of squares, then write the two factors. It includes sums of squares and numbers that are not perfect squares.", "Decida primero si es una diferencia de cuadrados y después escriba los dos factores. Incluye sumas de cuadrados y números que no son cuadrados perfectos."))}'''

    s4 = f'''<p>{t("The golden rule is to <strong>always take out the common factor first</strong>. Then check whether what is left inside the parentheses is a difference of squares.", "La regla de oro es <strong>sacar siempre primero el factor común</strong>. Después se revisa si lo que queda dentro del paréntesis es una diferencia de cuadrados.")}</p>
{ejemplo(t("Example 6: factor 2x² − 50 completely.", "Ejemplo 6 · Factorizar 2x² − 50 completamente."),
  [("1", t("Common factor 2.", "Factor común 2."), "2x² − 50 = 2(x² − 25)."), ("2", t("Inside there is a difference of squares.", "Dentro hay una diferencia de cuadrados."), "x² − 25 = (x + 5)(x − 5)."), ("3", t("The complete result.", "Resultado completo."), "2(x + 5)(x − 5)."),
   ("✓", t("Answer.", "Respuesta."), "<strong>2(x + 5)(x − 5)</strong>.")])}
{caja("ojo", t("“Completely” means all the way", "«Completamente» significa hasta el final"), t("<p>A factorization is complete when no factor can be factored any further. So after you take out the common factor, always check whether the binomial left is a difference of squares.</p>", "<p>Una factorización está completa cuando ningún factor se puede seguir factorizando. Por eso, tras sacar el factor común, siempre se revisa si el binomio que queda es una diferencia de cuadrados.</p>"))}
{enlace(n, t("combine", "combinar"), t("common factor and then difference of squares", "factor común y luego diferencia de cuadrados"), t("Take out the common factor, decide whether what is left can be factored, and reach the complete factorization.", "Extraiga el factor común, decida si lo que queda se puede seguir factorizando y llegue a la factorización completa."))}'''

    secciones = [("s-" + t("undo", "deshacer"), t("Factoring undoes multiplying", "Factorizar es deshacer la multiplicación"), s1),
                 ("s-" + t("common", "comun"), t("The common factor", "Factor común"), s2),
                 ("s-" + t("squares", "cuadrados"), t("Difference of squares", "Diferencia de cuadrados"), s3),
                 ("s-" + t("combine", "combinar"), t("Both together: common factor, then difference of squares", "Combinar: factor común y luego diferencia de cuadrados"), s4)]

    lesson = {"next": t("Lesson 3.3", "Lección 3.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Multiply to check: 2(3x + 4) = 6x + 8.", "Multiplique para comprobar: 2(3x + 4) = 6x + 8."), "c": t("Multiply to check: 3 · 9 = 27, not 9.", "Multiplique para comprobar: 3 · 9 = 27, no 9.")}, "right": "3(2x + 3) = 6x + 9.", "solution": "3(2x + 3)."},
      "p2": {"ok": "a", "hints": {"b": t("2x + 4 still has a common factor 2.", "2x + 4 todavía tiene factor común 2."), "c": t("x is in both terms too: take it out.", "La x también está en los dos términos: sáquela.")}, "right": "4x(x + 2) = 4x² + 8x.", "solution": "4x(x + 2)."},
      "p3": {"ok": "c", "hints": {"a": t("x² is in both terms: take out 5x².", "x² está en los dos términos: saque 5x²."), "b": t("Divide −15x² by 5x²: −3.", "Divida −15x² entre 5x²: −3.")}, "right": "5x²(2x − 3) = 10x³ − 15x².", "solution": "5x²(2x − 3)."},
      "p4": {"ok": "c", "hints": {"a": t("(x − 3)(x − 3) = x² − 6x + 9. One sign is +, the other −.", "(x − 3)(x − 3) = x² − 6x + 9. Un signo es +, el otro −."), "b": t("Use the square roots: x and 3.", "Use las raíces cuadradas: x y 3.")}, "right": "(x + 3)(x − 3) = x² − 9.", "solution": "(x + 3)(x − 3)."},
      "p5": {"ok": "b", "hints": {"a": t("(x + 7)(x + 7) = x² + 14x + 49.", "(x + 7)(x + 7) = x² + 14x + 49."), "c": t("(x − 7)(x − 7) = x² − 14x + 49.", "(x − 7)(x − 7) = x² − 14x + 49.")}, "right": "(x + 7)(x − 7) = x² − 49.", "solution": "(x + 7)(x − 7)."},
      "p6": {"ok": "a", "hints": {"b": t("One sign is +, the other −.", "Un signo es +, el otro −."), "c": t("9x² is the square of 3x.", "9x² es el cuadrado de 3x.")}, "right": "(3x + 1)(3x − 1) = 9x² − 1.", "solution": "(3x + 1)(3x − 1)."},
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("2 is not the greatest: 15 is odd.", "2 no es el mayor: 15 es impar."), "b": t("6(x + 15) = 6x + 90.", "6(x + 15) = 6x + 90."), "d": t("3 · 15 = 45, not 15.", "3 · 15 = 45, no 15.")}, "solution": "3(2x + 5)."},
      "B": {"ok": "b", "hints": {"a": t("4x + 6 still has a factor 2.", "4x + 6 todavía tiene factor 2."), "c": t("x is also common.", "La x también es común."), "d": t("4x · 12 = 48x.", "4x · 12 = 48x.")}, "solution": "4x(2x + 3)."},
      "C": {"ok": "d", "hints": {"a": t("x² is in both terms.", "x² está en los dos términos."), "b": t("−15x² ÷ 5x² = −3.", "−15x² ÷ 5x² = −3."), "c": t("The GCF of 10 and 15 is 5.", "El MCD de 10 y 15 es 5.")}, "solution": "5x²(2x − 3)."},
      "D": {"ok": "c", "hints": {"a": t("(x − 4)(x − 4) = x² − 8x + 16.", "(x − 4)(x − 4) = x² − 8x + 16."), "b": t("Use the square roots: x and 4.", "Use las raíces cuadradas: x y 4."), "d": t("(x + 4)(x + 4) = x² + 8x + 16.", "(x + 4)(x + 4) = x² + 8x + 16.")}, "solution": "(x + 4)(x − 4)."},
      "E": {"ok": "d", "hints": {"a": t("4x² is the square of 2x.", "4x² es el cuadrado de 2x."), "b": t("One sign is +, the other −.", "Un signo es +, el otro −."), "c": t("9 is the square of 3.", "9 es el cuadrado de 3.")}, "solution": "(2x + 3)(2x − 3)."},
      "F": {"ok": "a", "hints": {"b": t("One sign is +, the other −.", "Un signo es +, el otro −."), "c": t("25x² is the square of 5x.", "25x² es el cuadrado de 5x."), "d": t("One sign is +, the other −.", "Un signo es +, el otro −.")}, "solution": "(5x + 1)(5x − 1)."},
      "G": {"ok": "b", "hints": {"a": t("x² − 25 can still be factored.", "x² − 25 todavía se puede factorizar."), "c": t("2x + 10 still has a factor 2.", "2x + 10 todavía tiene factor 2."), "d": t("One sign is +, the other −.", "Un signo es +, el otro −.")}, "solution": "2(x + 5)(x − 5)."},
      "H": {"ok": "d", "hints": {"a": t("x² − 4 can still be factored.", "x² − 4 todavía se puede factorizar."), "b": t("3x + 6 still has a factor 3.", "3x + 6 todavía tiene factor 3."), "c": t("One sign is +, the other −.", "Un signo es +, el otro −.")}, "solution": "3(x + 2)(x − 2)."},
     }}

    quiz = [
     ("A", t("Factor 6x + 15.", "Factorice 6x + 15."), [("a", "2(3x + 5)"), ("b", "6(x + 15)"), ("c", "3(2x + 5)"), ("d", "3(2x + 15)")]),
     ("B", t("Factor 8x² + 12x.", "Factorice 8x² + 12x."), [("a", "2x(4x + 6)"), ("b", "4x(2x + 3)"), ("c", "4(2x² + 3x)"), ("d", "4x(2x + 12)")]),
     ("C", t("Factor 10x³ − 15x².", "Factorice 10x³ − 15x²."), [("a", "5x(2x² − 3x)"), ("b", "5x²(2x − 15)"), ("c", "10x²(x − 15)"), ("d", "5x²(2x − 3)")]),
     ("D", t("Factor x² − 16.", "Factorice x² − 16."), [("a", "(x − 4)(x − 4)"), ("b", "(x + 8)(x − 2)"), ("c", "(x + 4)(x − 4)"), ("d", "(x + 4)(x + 4)")]),
     ("E", t("Factor 4x² − 9.", "Factorice 4x² − 9."), [("a", "(4x + 3)(x − 3)"), ("b", "(2x − 3)(2x − 3)"), ("c", "(2x + 9)(2x − 1)"), ("d", "(2x + 3)(2x − 3)")]),
     ("F", t("Factor 25x² − 1.", "Factorice 25x² − 1."), [("a", "(5x + 1)(5x − 1)"), ("b", "(5x − 1)(5x − 1)"), ("c", "(25x + 1)(x − 1)"), ("d", "(5x + 1)(5x + 1)")]),
     ("G", t("Factor 2x² − 50 completely.", "Factorice completamente 2x² − 50."), [("a", "2(x² − 25)"), ("b", "2(x + 5)(x − 5)"), ("c", "(2x + 10)(x − 5)"), ("d", "2(x − 5)(x − 5)")]),
     ("H", t("Factor 3x² − 12 completely.", "Factorice completamente 3x² − 12."), [("a", "3(x² − 4)"), ("b", "(3x + 6)(x − 2)"), ("c", "3(x − 2)(x − 2)"), ("d", "3(x + 2)(x − 2)")])]

    tarea = (t("For your own work, with your notebook open and no calculator: (1) The factor detective: before you factor each polynomial, decide whether it needs only a common factor, only a difference of squares, or both: 6x + 18, 4x² − 12x, 12x³ + 8x², x² − 49, 9x² − 16, 3x² − 27, 5x³ − 20x, and 2x² − 50. (2) I always check: expand each of the eight factorizations and check that you get back the original polynomial. If it does not match, find the step where you went wrong. (3) When it equals zero: factor x² − 25, x² − 81, and 4x² − 9, and find which values of x make each factor zero. You will use this idea in Topic 4 to solve equations. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto y sin calculadora: (1) El detective de factores: antes de factorizar cada polinomio, decida si necesita solo factor común, solo diferencia de cuadrados o ambas técnicas: 6x + 18, 4x² − 12x, 12x³ + 8x², x² − 49, 9x² − 16, 3x² − 27, 5x³ − 20x y 2x² − 50. (2) Siempre verifico: expanda cada una de las ocho factorizaciones y compruebe que recupera el polinomio original. Si no coincide, localice el paso en que se equivocó. (3) Cuando vale cero: factorice x² − 25, x² − 81 y 4x² − 9, y halle qué valores de x hacen cero cada factor. Esta idea se usará en el Tema 4 para resolver ecuaciones. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Mental math with a difference of squares: 21 × 19 = (20 + 1)(20 − 1) = 400 − 1 = 399. Try 31 × 29, 52 × 48, and 99 × 101 in your head, then check them with a calculator. Show the trick to someone at home.",
               "Cálculo mental con la diferencia de cuadrados: 21 × 19 = (20 + 1)(20 − 1) = 400 − 1 = 399. Pruebe de cabeza 31 × 29, 52 × 48 y 99 × 101, y compruébelos con la calculadora. Enséñele el truco a alguien en casa."))

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Factor a polynomial by taking out the common factor and by recognizing a difference of squares, and always check by multiplying.", "Factorice un polinomio sacando el factor común y reconociendo la diferencia de cuadrados, y compruebe siempre multiplicando."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Explain</strong> that factoring undoes multiplying, and check by expanding.", "<strong>Explicar</strong> que factorizar deshace la multiplicación, y comprobar expandiendo."),
         t("<strong>Take out</strong> the greatest common factor (number and variable).", "<strong>Extraer</strong> el máximo factor común (número y variable)."),
         t("<strong>Factor</strong> a difference of squares, a² − b² = (a + b)(a − b).", "<strong>Factorizar</strong> una diferencia de cuadrados, a² − b² = (a + b)(a − b)."),
         t("<strong>Combine</strong> both techniques to factor completely.", "<strong>Combinar</strong> las dos técnicas para factorizar completamente.")],
        secciones, tarea, quiz,
        t("Self-check checklist for factoring", "Lista de autoevaluación de la factorización"),
        t("Self-check checklist: skills for the common factor and the difference of squares", "Lista de autoevaluación: destrezas del factor común y la diferencia de cuadrados"),
        [(t("Taking out the common factor", "Extraer el factor común"), t("I take out the GCF of the numbers and the variable, and check what is left inside.", "Extraigo el MCD de los coeficientes y la variable, y reviso lo que queda dentro."), t("I take out the number but forget the variable.", "Saco el MCD numérico, pero olvido la variable."), t("I do not find the common factor, or I take out only part of it.", "No identifico el factor común o lo saco incompleto.")),
         (t("Difference of squares", "Diferencia de cuadrados"), t("I factor it surely and know when it does not apply (a sum of squares).", "La factorizo con seguridad y sé cuándo no aplica (suma de cuadrados)."), t("I recognize it but write the signs wrong.", "La reconozco, pero escribo mal los signos."), t("I do not recognize a difference of squares.", "No reconozco la diferencia de cuadrados.")),
         (t("Checking by expanding", "Verificar expandiendo"), t("I always check and factor completely, combining techniques.", "Verifico siempre y factorizo por completo, combinando técnicas."), t("I check but make mistakes when I expand.", "Verifico, pero me equivoco al expandir."), t("I do not check my result.", "No verifico el resultado."))],
        t("<p>In this lesson you learned to <strong>factor</strong> by taking out the <strong>common factor</strong> and by recognizing the <strong>difference of squares</strong>, a² − b² = (a + b)(a − b), always checking by expanding.</p>\n<p>In <strong>Lesson 3.3 · Factoring trinomials (a = 1 and a ≠ 1)</strong> you will factor expressions with three terms such as x² + 7x + 12, looking for two numbers whose product and sum meet the conditions, and you will extend the method to trinomials whose leading coefficient is not 1. Remember: the first step will always be to look for a common factor.</p>",
          "<p>En esta lección se aprendió a <strong>factorizar</strong> extrayendo el <strong>factor común</strong> y reconociendo la <strong>diferencia de cuadrados</strong>, a² − b² = (a + b)(a − b), verificando siempre por expansión.</p>\n<p>En la <strong>Lección 3.3 · Factorización de trinomios (a = 1 y a ≠ 1)</strong> se factorizarán expresiones de tres términos como x² + 7x + 12, buscando dos números cuyo producto y suma cumplan las condiciones, y se extenderá la técnica a trinomios con coeficiente principal distinto de 1. Recuerde: el primer paso siempre será buscar el factor común.</p>"),
        ("3-3", ("", t("Lesson 3.3 · Factoring trinomials (a = 1 and a ≠ 1)", "Lección 3.3 · Factorización de trinomios (a = 1 y a ≠ 1)"))),
        [(t("factor", "factorizar"), t("To write a polynomial as a product.", "Escribir un polinomio como un producto.")),
         (t("greatest common factor (GCF)", "máximo común divisor (MCD)"), t("The largest number (and power of x) that divides every term.", "El mayor número (y potencia de x) que divide a todos los términos.")),
         (t("perfect square", "cuadrado perfecto"), t("A number or term that is the square of another: 49 = 7², 4x² = (2x)².", "Un número o término que es el cuadrado de otro: 49 = 7², 4x² = (2x)².")),
         (t("difference of squares", "diferencia de cuadrados"), "a² − b² = (a + b)(a − b)"),
         (t("factored completely", "factorizado completamente"), t("When no factor can be factored any further.", "Cuando ningún factor se puede seguir factorizando."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function F(k, m, f){ return {k: k, m: m || 0, f: f || []}; }
function bin(a, b){ return [b, a]; }
function monoV(c, g){ return tVis(c, g, true); }
var FAC_AYUDA = T("Type the factors with parentheses, like 3(x\u00a0+\u00a02) or (x\u00a0−\u00a04)(x\u00a0+\u00a04).", "Escriba los factores con paréntesis, como 3(x\u00a0+\u00a02) o (x\u00a0−\u00a04)(x\u00a0+\u00a04).");

/* ===== MODULE 1 · Undoing the multiplication ===== */
var DES = [F(3, 0, [bin(1, 2)]), F(5, 0, [bin(1, -4)]), F(4, 1, [bin(1, 3)]), F(1, 0, [bin(1, 3), bin(1, -3)]), F(2, 0, [bin(1, 5), bin(1, -5)]), F(1, 0, [bin(1, 2), bin(1, 5)])];
function deDibuja(){
  var F0 = DES[+$("de-ex").value], dir = $("de-dir").getAttribute("data-d"), prod = fProducto(F0);
  $("de-izq").innerHTML = fHTML(F0); $("de-der").innerHTML = pHTML(prod);
  $("de-fm").style.opacity = dir === "m" ? 1 : .25; $("de-ff").style.opacity = dir === "f" ? 1 : .25;
  $("de-txt").innerHTML = '<div class="linea">' + (dir === "m" ? T("Multiplying: start from the factors and distribute. ", "Multiplicar: se parte de los factores y se distribuye. ") + fVis(F0) + " = " + pVis(prod) : T("Factoring: start from the polynomial and find the factors that produce it. ", "Factorizar: se parte del polinomio y se buscan los factores que lo producen. ") + pVis(prod) + " = " + fVis(F0)) + "</div>";
}
$("de-ex").addEventListener("change", deDibuja);
$("de-m").addEventListener("click", function(){ $("de-dir").setAttribute("data-d", "m"); $("de-m").setAttribute("aria-pressed", "true"); $("de-f").setAttribute("aria-pressed", "false"); deDibuja(); });
$("de-f").addEventListener("click", function(){ $("de-dir").setAttribute("data-d", "f"); $("de-f").setAttribute("aria-pressed", "true"); $("de-m").setAttribute("aria-pressed", "false"); deDibuja(); });
deDibuja();
OMR("dq", function(){
  var k = aleatorio(2, 7), b; do { b = aleatorio(-9, 9); } while (!b); var a = aleatorio(1, 4), F0 = F(k, 0, [bin(a, b)]), prod = fProducto(F0);
  if (Math.random() < .5){
    var ops = [opP(prod), opP(pDe({1: k * a, 0: -k * b})), opP(pDe({1: k * a, 0: b})), opP(pDe({1: a, 0: k * b}))];
    return {enun: T("Multiply to get the expanded form of ", "Multiplique para obtener la forma desarrollada de ") + fHTML(F0) + ".", correcta: pClave(prod), opciones: ops,
      porClave: (function(){ var o = {}; o[pClave(pDe({1: k * a, 0: b}))] = T("The number outside must multiply every term.", "El número de fuera debe multiplicar a todos los términos."); o[pClave(pDe({1: k * a, 0: -k * b}))] = T("Check the sign of the last term.", "Revise el signo del último término."); return o; })(),
      pista: T("Distribute: the number outside multiplies each term inside.", "Distribuya: el número de fuera multiplica a cada término de dentro."), bien: fVis(F0) + " = " + pVis(prod) + "."};
  }
  var malos = [F(k, 0, [bin(a, -b)]), F(k, 0, [bin(a, k * b)]), F(1, 0, [bin(k * a, b)])];
  return {enun: T("Which is the factored form of ", "¿Cuál es la forma factorizada de ") + pHTML(prod) + T("? Check by multiplying.", "? Compruebe multiplicando."), correcta: fClave(F0), opciones: [opF(F0)].concat(malos.map(opF)),
    pista: T("Multiply each option: only one gives back the polynomial exactly.", "Multiplique cada opción: solo una devuelve exactamente el polinomio."), bien: fVis(F0) + " → " + pVis(prod) + "."};
});

/* ===== MODULE 2 · Common factor ===== */
/* Only the common factor is asked here: what is left inside may be any polynomial with no common factor and a constant term. */
function evaluaComun(txt, ok){
  var r = fLee(txt);
  if (!r) return {estado: "invalido", msg: FAC_AYUDA};
  if (!pIgual(r.prod, ok)) return {estado: "mal", msg: T("Multiply to check: your answer does not give back the polynomial. Look at the signs and at what is left inside.", "Multiplique para comprobar: su respuesta no devuelve el polinomio. Revise los signos y lo que queda dentro.")};
  var F0 = r.F;
  if (F0.f.length !== 1) return evaluaF(txt, ok, []);
  if (pGrado(F0.f[0]) === pGrado(ok) && Math.abs(F0.k) === 1 && !F0.m) return {estado: "mal", msg: T("That is the same polynomial. Take out the common factor.", "Ese es el mismo polinomio. Saque el factor común.")};
  if (contenido(F0.f[0]) !== 1) return {estado: "mal", msg: T("The product is right, but inside the parentheses there is still a common number. Take out the greatest one.", "El producto está bien, pero dentro del paréntesis todavía queda un número común. Saque el mayor.")};
  if (!F0.f[0][0]) return {estado: "mal", msg: T("The product is right, but every term inside still has x. Take out x too.", "El producto está bien, pero todos los términos de dentro todavía tienen x. Saque también la x.")};
  return {estado: "bien"};
}
function casoComun(){
  var g = elige([2, 3, 4, 5, 6]), m = aleatorio(0, 2), n = elige([2, 2, 3]), dentro, ok;
  do { var o = {}; var grs = baraja([0, 1, 2, 3]).slice(0, n); if (grs.indexOf(0) < 0) grs[0] = 0; grs.forEach(function(e){ var c; do { c = aleatorio(-6, 6); } while (!c); o[e] = c; }); dentro = pDe(o); } while (contenido(dentro) !== 1 || pGrado(dentro) === 0);
  if (dentro[pGrado(dentro)] < 0 && Math.random() < .5) dentro = pEsc(dentro, -1);
  var FF = F(g, m, [dentro]), poly = fProducto(FF);
  var lista = listaTerm(poly), coefs = lista.map(function(t){ return Math.abs(t[0]); }), menor = Math.min.apply(null, lista.map(function(t){ return t[1]; }));
  var pasos = [T("GCF of the numbers ", "MCD de los coeficientes ") + coefs.join(", ") + ": <strong>" + g + "</strong>.",
    T("Smallest power of x in every term: ", "Menor potencia de x presente en todos los términos: ") + (menor ? "<strong>" + monoV(1, menor) + "</strong>" : T("none (one term has no x)", "ninguna (un término no tiene x)")) + ".",
    T("Divide each term by ", "Se divide cada término entre ") + monoV(g, m) + ": " + lista.map(function(t){ return tVis(t[0], t[1], true) + " ÷ " + monoV(g, m) + " = " + tVis(t[0] / g, t[1] - m, true); }).join("; ") + ".",
    T("Result: ", "Resultado: ") + "<strong>" + fVis(FF) + "</strong>. " + T("Check: multiplying gives ", "Comprobación: al multiplicar se obtiene ") + pVis(poly) + "."];
  return {FF: FF, poly: poly, g: g, m: m, pasos: pasos};
}
pasoAPaso4("cm", function(){ var c = casoComun(); return {enun: T("Factor ", "Factorice ") + pHTML(c.poly) + ".", pasos: c.pasos}; });
creaPracticaLibre("cq", function(){ var c = casoComun();
  return {enun: T("Take out the greatest common factor: ", "Extraiga el máximo factor común: ") + pHTML(c.poly) + ". " + FAC_AYUDA, evalua: function(txt){ return evaluaComun(txt, c.poly); }, solucion: c.pasos.join(" ").replace(/<\/?strong>/g, "")}; });

/* ===== MODULE 3 · Difference of squares ===== */
var DC = {};
function dcNuevo(){
  var a = elige([1, 1, 1, 2, 3, 4, 5]), b; do { b = aleatorio(1, 11); } while (mcd(a, b) !== 1); var tipo = elige(["dif", "dif", "dif", "suma", "noCuad"]), p;
  if (tipo === "dif") p = pDe({2: a * a, 0: -b * b}); else if (tipo === "suma") p = pDe({2: a * a, 0: b * b}); else { var n; do { n = aleatorio(2, 50); } while (esCuadrado(n)); p = pDe({2: a * a, 0: -n}); }
  DC = {p: p, es: tipo === "dif", a: a, b: b, tipo: tipo};
  $("dc-enun").innerHTML = T("Factor, if possible: ", "Factorice, si se puede: ") + pHTML(p) + ".";
  $("dc-fb").className = "fb"; $("dc-fb").innerHTML = ""; $("dc-paso2").hidden = true; $("dc-r").value = ""; $("dc-si").disabled = $("dc-no").disabled = false;
}
$("dc-si").addEventListener("click", function(){ var fb = $("dc-fb");
  if (DC.es){ fb.className = "fb bien"; fb.innerHTML = TX.bien + T("Both terms are perfect squares and they are subtracted.", "Los dos términos son cuadrados perfectos y están restados."); $("dc-paso2").hidden = false; $("dc-si").disabled = $("dc-no").disabled = true; $("dc-r").focus(); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + (DC.tipo === "suma" ? T("It is a <strong>sum</strong> of squares: it cannot be factored with real numbers.", "Es una <strong>suma</strong> de cuadrados: no se factoriza con números reales.") : T(String(-DC.p[0]) + " is not a perfect square.", String(-DC.p[0]) + " no es un cuadrado perfecto.")); } });
$("dc-no").addEventListener("click", function(){ var fb = $("dc-fb");
  if (!DC.es){ fb.className = "fb bien"; fb.innerHTML = TX.bien + (DC.tipo === "suma" ? T("A sum of squares cannot be factored this way.", "Una suma de cuadrados no se factoriza así.") : T(String(-DC.p[0]) + " is not a perfect square, so this method does not work.", String(-DC.p[0]) + " no es un cuadrado perfecto, así que este método no sirve.")); $("dc-si").disabled = $("dc-no").disabled = true; }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + T("Look again: " + (DC.a > 1 ? DC.a * DC.a + "x² = (" + DC.a + "x)²" : "x² = (x)²") + " and " + DC.b * DC.b + " = " + DC.b + "², and they are subtracted.", "Mire otra vez: " + (DC.a > 1 ? DC.a * DC.a + "x² = (" + DC.a + "x)²" : "x² = (x)²") + " y " + DC.b * DC.b + " = " + DC.b + "², y están restados."); } });
$("dc-comprobar").addEventListener("click", function(){
  var a = DC.a, b = DC.b, r = evaluaF($("dc-r").value, DC.p, [{F: F(1, 0, [bin(a, -b), bin(a, -b)]), msg: T("One factor has +, the other −: (a + b)(a − b).", "Un factor lleva +, el otro −: (a + b)(a − b).")}, {F: F(1, 0, [bin(a, b), bin(a, b)]), msg: T("One factor has +, the other −: (a + b)(a − b).", "Un factor lleva +, el otro −: (a + b)(a − b).")}, {F: F(1, 0, [bin(a * a, b), bin(1, -b)]), msg: T("Use the square root of the first term: " + tVis(a, 1, true) + ".", "Use la raíz cuadrada del primer término: " + tVis(a, 1, true) + ".")}].slice(0, a > 1 ? 3 : 2)), fb = $("dc-fb");
  if (r.estado === "bien"){ fb.className = "fb bien"; fb.innerHTML = TX.bien + pVis(DC.p) + " = (" + tVis(a, 1, true) + " + " + b + ")(" + tVis(a, 1, true) + " − " + b + ")."; }
  else { fb.className = "fb pista"; fb.innerHTML = (r.estado === "mal" ? TX.todavia : "") + r.msg; }
});
$("dc-otro").addEventListener("click", dcNuevo); dcNuevo();

/* ===== MODULE 4 · Both together ===== */
function casoComb(){
  var g = elige([2, 3, 4, 5]), m = elige([0, 0, 1]), a = elige([1, 1, 2, 3]), b; do { b = aleatorio(1, a > 1 ? 5 : 9); } while (mcd(a, b) !== 1); var sigue = Math.random() < .75, dentro = sigue ? pDe({2: a * a, 0: -b * b}) : pDe({2: a * a, 0: b * b});
  var FF = sigue ? F(g, m, [bin(a, b), bin(a, -b)]) : F(g, m, [dentro]), poly = pMul(pMono(g, m), dentro);
  var pasos = [T("Common factor first: ", "Primero el factor común: ") + pVis(poly) + " = " + monoV(g, m) + "(" + pVis(dentro) + ").",
    sigue ? T("Inside there is a difference of squares: ", "Dentro hay una diferencia de cuadrados: ") + pVis(dentro) + " = (" + tVis(a, 1, true) + " + " + b + ")(" + tVis(a, 1, true) + " − " + b + ")." : T("Inside there is a <strong>sum</strong> of squares: it cannot be factored further.", "Dentro hay una <strong>suma</strong> de cuadrados: no se puede seguir factorizando."),
    T("Complete factorization: ", "Factorización completa: ") + "<strong>" + fVis(FF) + "</strong>."];
  return {FF: FF, poly: poly, pasos: pasos, g: g, m: m, dentro: dentro};
}
pasoAPaso4("cb", function(){ var c = casoComb(); return {enun: T("Factor completely: ", "Factorice completamente: ") + pHTML(c.poly) + ".", pasos: c.pasos}; });
creaPracticaLibre("bq", function(){ var c = casoComb();
  return {enun: T("Factor completely: ", "Factorice completamente: ") + pHTML(c.poly) + ". " + FAC_AYUDA, evalua: function(txt){ return evaluaF(txt, c.poly, [{F: F(c.g, c.m, [c.dentro]), msg: c.FF.f.length > 1 ? T("Good start, but the factor inside is a difference of squares: keep going.", "Buen comienzo, pero el factor de dentro es una diferencia de cuadrados: siga factorizando.") : ""}].filter(function(x){ return x.msg; })); }, solucion: c.pasos.join(" ").replace(/<\/?strong>/g, "")}; });
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    ej = [("0", "3(x + 2) ⇄ 3x + 6"), ("1", "5(x − 4) ⇄ 5x − 20"), ("2", "4x(x + 3) ⇄ 4x² + 12x"), ("3", "(x + 3)(x − 3) ⇄ x² − 9"), ("4", "2(x + 5)(x − 5) ⇄ 2x² − 50"), ("5", "(x + 2)(x + 5) ⇄ x² + 7x + 10")]
    cuad = "".join(f"<td>{i}</td>" for i in range(1, 13)), "".join(f"<td>{i * i}</td>" for i in range(1, 13))
    mods = [
     (t("undo", "deshacer"), t("Factoring undoes multiplying", "Factorizar es deshacer la multiplicación"),
      f'''      <p>{t("Factoring a polynomial means writing it as a product. When you multiply you start from the factors and reach the polynomial; when you factor you start from the polynomial and find which factors produced it. That is why the best check of a factorization is to multiply again. Choose an expression and change the direction.", "Factorizar un polinomio significa escribirlo como un producto. Al multiplicar se parte de los factores y se llega al polinomio; al factorizar se parte del polinomio y se descubre qué factores lo produjeron. Por eso la mejor comprobación de una factorización es volver a multiplicar. Elija una expresión y cambie la dirección.")}</p>
      <div class="panel"><div class="campos">{n4.lista("de-ex", t("Expression", "Expresión"), ej)}</div>
        <div class="modos" id="de-dir" data-d="m" role="group" aria-label="{t("Direction", "Dirección")}"><button type="button" class="btn-sec" id="de-m" aria-pressed="true">{t("Multiply →", "Multiplicar →")}</button><button type="button" class="btn-sec" id="de-f" aria-pressed="false">{t("← Factor", "← Factorizar")}</button></div></div>
      <div class="tarjetas" style="align-items:center;text-align:center;font-size:24px;font-weight:700;"><div class="tarjeta" id="de-izq"></div><div style="flex:0 0 120px;font-size:15px;"><div id="de-fm" style="color:#0d47a1">{t("multiply", "multiplicar")} ⟶</div><div id="de-ff" style="color:#1b5e20">⟵ {t("factor", "factorizar")}</div></div><div class="tarjeta" id="de-der"></div></div>
{n4.salida("de-txt")}
      <div class="caja-tip">{t("Two mistakes the check catches. The sign: 3(x − 2) gives 3x − 6, not 3x + 6. And the incomplete factor, when the number outside does not multiply every term: 3(x + 6) gives 3x + 18, not 3x + 6.", "Dos errores que la comprobación descubre. El de signo: 3(x − 2) da 3x − 6, no 3x + 6. Y el de factor incompleto, cuando el número de fuera no multiplica a todos los términos: 3(x + 6) da 3x + 18, no 3x + 6.")}</div>
{B.om("dq", t("Practice: factored form, expanded form, and the check", "Practique: forma factorizada, forma desarrollada y comprobación"))}'''),
     (t("common", "comun"), t("The common factor", "Factor común"),
      f'''      <p>{t("The common factor is made of the greatest common factor (GCF) of the numbers and the smallest power of x that appears in every term. If a term has no x, no x comes out. Check by multiplying: if you do not get the original polynomial back, the factor was wrong or a sign failed.", "El factor común se forma con el máximo común divisor (MCD) de los coeficientes y la menor potencia de x que aparece en todos los términos. Si en un término no hay x, no sale x. Compruebe multiplicando: si no recupera el polinomio original, el factor no era el correcto o falló un signo.")}</p>
{n4.pasos("cm", t("Another polynomial", "Otro polinomio"))}
{libre("cq", t("Practice: take out the common factor", "Practique: extraiga el factor común"), t("Factored form", "Forma factorizada"))}'''),
     (t("squares", "cuadrados"), t("Difference of squares", "Diferencia de cuadrados"),
      f'''{n4.formula("a² − b² = (a + b)(a − b)")}
      <p>{t("A binomial is a difference of squares when both terms are perfect squares and they are subtracted. First decide; then write the two factors.", "Un binomio es una diferencia de cuadrados cuando los dos términos son cuadrados perfectos y están restados. Primero decida; después escriba los dos factores.")}</p>
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Perfect squares for reference", "Cuadrados perfectos de referencia")}</caption><tbody><tr><th scope="row">n</th>{cuad[0]}</tr><tr><th scope="row">n²</th>{cuad[1]}</tr></tbody></table></div>
      <div class="practica"><p class="enun" id="dc-enun"></p>
        <p><strong>{t("Step 1. Is it a difference of squares?", "Paso 1. ¿Es una diferencia de cuadrados?")}</strong></p>
        <div class="fila-btn"><button type="button" class="btn-sec" id="dc-si">{t("Yes, it can be factored", "Sí, se puede factorizar")}</button><button type="button" class="btn-sec" id="dc-no">{t("No, it cannot be factored this way", "No se puede factorizar así")}</button></div>
        <div id="dc-paso2" hidden><p><strong>{t("Step 2. Write the two factors.", "Paso 2. Escriba los dos factores.")}</strong></p>
          <div class="campos"><div class="campo"><label for="dc-r">{t("Factored form", "Forma factorizada")}</label><input type="text" autocomplete="off" class="ancho" id="dc-r"></div></div>
          <div class="fila-btn"><button type="button" class="btn" id="dc-comprobar">{t("Check the factors", "Comprobar los factores")}</button></div></div>
        <div class="fb" id="dc-fb" role="status"></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="dc-otro">{t("New exercise", "Otro ejercicio")}</button></div></div>
      <div class="caja-atencion"><strong>{t("A sum of squares does not factor.", "La suma de cuadrados no se factoriza.")}</strong> {t("x² + 25 has no factorization with real numbers. Only the subtraction gives two binomials.", "x² + 25 no tiene factorización con números reales. Solo la resta produce dos binomios.")}</div>'''),
     (t("combine", "combinar"), t("Both together: common factor, then difference of squares", "Combinar: factor común y luego diferencia de cuadrados"),
      f'''      <p>{t("The order never changes: first take out the common factor, then look at what is left inside the parentheses. Sometimes you can keep factoring, and sometimes you cannot. An expression is factored completely when no factor can be broken down any further.", "El orden nunca cambia: primero se extrae el factor común y después se examina lo que queda dentro del paréntesis. A veces se puede seguir factorizando y a veces no. Una expresión está completamente factorizada cuando ninguno de sus factores admite ya otra descomposición.")}</p>
{n4.pasos("cb", t("Another polynomial", "Otro polinomio"))}
{libre("bq", t("Practice: factor completely", "Practique: factorice completamente"), t("Factored form", "Forma factorizada"))}''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Factorización: factor común y diferencia de cuadrados")
