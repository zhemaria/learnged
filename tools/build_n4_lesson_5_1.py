"""Level 4 · Lesson 5.1 · Simplifying rational expressions: factor and cancel — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_5-1.html and algebra/n4-l5-1.html (simplify step by step, excluded values,
factors and not terms). They are rebuilt here, inside LearnGED, with the rational-expression helpers of math/poly4.js.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "5-1"
TEMA = ("Rational expressions", "Expresiones racionales")
TIT = ("Simplifying rational expressions: factor and cancel", "Simplificar expresiones racionales: factorizar y cancelar")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)
ESTILO = n4.ESTILO + """
  .tachado{text-decoration:line-through;text-decoration-color:#c62828;text-decoration-thickness:3px;color:#78909c;}
  .fraccion-grande .fracc{font-size:22px;}
"""

def fr(a, b, voz=None):
    """A stacked fraction for the lesson (with a spoken version)."""
    v = voz or t(f"{a} over {b}", f"{a} sobre {b}")
    return f'<span class="ex" aria-hidden="true"><span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span></span><span class="cap-oculto">{v}</span>'

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Topics 3 and 4.</strong> In Topics 3 and 4, factoring was the key tool. It is again: a <strong>rational expression</strong> is a fraction whose numerator and denominator are polynomials. To simplify it you factor the top and the bottom and cancel the common factors, exactly as with fractions of numbers.",
 "<strong>Conexión con el tema anterior.</strong> En los Temas 3 y 4 la factorización fue la herramienta clave. Ahora vuelve a serlo: una <strong>expresión racional</strong> es una fracción cuyo numerador y denominador son polinomios. Para simplificarla se factoriza arriba y abajo y se cancelan los factores comunes, exactamente como con las fracciones de números.")}</p>
<p>{t("To simplify 12/18, you factor the top and the bottom and cancel the common factor:", "Para simplificar 12/18 se factoriza arriba y abajo y se cancela el factor común:")}</p>
<p class="formula" style="text-align:center;font-size:1.25rem;">{fr("12", "18")} = {fr("2 · <s style=\"text-decoration-color:#c62828;text-decoration-thickness:3px\">6</s>", "3 · <s style=\"text-decoration-color:#c62828;text-decoration-thickness:3px\">6</s>", t("2 times 6 over 3 times 6, with the 6 crossed out", "2 por 6 sobre 3 por 6, con el 6 tachado"))} = {fr("2", "3")}</p>
<p>{t("The 6 cancels because it is a factor (something that multiplies) on the top and on the bottom. With polynomials it works the same way:", "El 6 se cancela porque es un factor (algo que multiplica) presente arriba y abajo. Con polinomios el procedimiento es idéntico:")}</p>
<p class="formula" style="text-align:center;font-size:1.25rem;">{fr("<s style=\"text-decoration-color:#c62828;text-decoration-thickness:3px\">(x + 3)</s>(x − 3)", "<s style=\"text-decoration-color:#c62828;text-decoration-thickness:3px\">(x + 3)</s>(x − 2)", t("x plus 3 times x minus 3, over x plus 3 times x minus 2, with x plus 3 crossed out", "x más 3 por x menos 3, sobre x más 3 por x menos 2, con x más 3 tachado"))} = {fr("x − 3", "x − 2")}</p>
{enlace(n, t("simplify", "simplificar"), t("simplifying step by step", "simplificar paso a paso"), t("Watch the factors cancel on the fraction itself, one step at a time.", "Vea cómo se cancelan los factores sobre la propia fracción, un paso a la vez."))}'''

    s2 = f'''<p>{t("There are three steps: factor the numerator, factor the denominator, and cancel the common factors.", "El procedimiento tiene tres pasos: factorizar el numerador, factorizar el denominador y cancelar los factores comunes.")}</p>
{ejemplo(t("Example 1: monomials. Simplify 6x² / 9x.", "Ejemplo 1 · Monomios. Simplificar 6x² / 9x."),
  [("1", t("Write it in factors:", "Se escribe en factores:"), "(3 · 2 · x · x) / (3 · 3 · x)."), ("2", t("Cancel the 3 and one x.", "Se cancela el 3 y una x."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>2x / 3</strong>.")])}
{ejemplo(t("Example 2: with a trinomial. Simplify (x² + 5x + 6) / (x + 2).", "Ejemplo 2 · Con trinomio. Simplificar (x² + 5x + 6) / (x + 2)."),
  [("1", t("Factor the numerator:", "Se factoriza el numerador:"), "(x + 2)(x + 3)."), ("2", t("Cancel the common factor (x + 2).", "Se cancela el factor común (x + 2)."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>x + 3</strong>.")])}
{ejemplo(t("Example 3: simplify (x² − 4) / (x² − x − 2).", "Ejemplo 3 · Simplificar (x² − 4) / (x² − x − 2)."),
  [("1", t("Numerator:", "Numerador:"), "(x + 2)(x − 2). " + t("Denominator:", "Denominador:") + " (x − 2)(x + 1)."), ("2", t("Cancel (x − 2).", "Se cancela (x − 2)."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>(x + 2) / (x + 1)</strong>.")])}
{practica("p1", t("Practice 1 — 4x² / 6x", "Práctica 1 — 4x² / 6x"), t("Choose the simplified form.", "Seleccione la forma simplificada."), [("a", "2x² / 3"), ("b", "4x / 6"), ("c", "2x / 3")])}
{practica("p2", t("Practice 2 — (x² − 1) / (x − 1)", "Práctica 2 — (x² − 1) / (x − 1)"), t("Choose the simplified form.", "Seleccione la forma simplificada."), [("a", "x − 1"), ("b", "x + 1"), ("c", "x² − 1")])}
{practica("p3", t("Practice 3 — (x² + 4x + 4) / (x + 2)", "Práctica 3 — (x² + 4x + 4) / (x + 2)"), t("Choose the simplified form.", "Seleccione la forma simplificada."), [("a", "x + 2"), ("b", "x + 4"), ("c", "x² + 2")])}
{enlace(n, t("simplify", "simplificar"), t("simplifying", "la simplificación"), t("A step-by-step simplifier with the cancelled factors crossed out, and exercises that change every time.", "Simplificador paso a paso con la cancelación marcada sobre la fracción, y ejercicios que cambian cada vez."))}'''

    s3 = f'''<p>{t("A fraction can never have a denominator of zero: division by zero is not defined. The <strong>excluded values</strong> are the ones that make the <strong>original</strong> denominator zero (before cancelling). To find them, factor the denominator and set each factor equal to zero.", "Una fracción nunca puede tener denominador cero: la división entre cero no está definida. Los <strong>valores excluidos</strong> son los que hacen cero al denominador <strong>original</strong> (antes de cancelar). Para hallarlos se factoriza el denominador y se iguala cada factor a cero.")}</p>
{ejemplo(t("Example 4: which values are excluded in (x + 1) / (x² − 9)?", "Ejemplo 4 · ¿Qué valores se excluyen en (x + 1) / (x² − 9)?"),
  [("1", t("Factor the denominator:", "Se factoriza el denominador:"), "(x + 3)(x − 3)."), ("2", t("Set each factor equal to zero:", "Se iguala cada factor a cero:"), t("x + 3 = 0 or x − 3 = 0.", "x + 3 = 0 o x − 3 = 0.")), ("✓", t("Excluded values.", "Valores excluidos."), t("<strong>x = −3 and x = 3</strong>.", "<strong>x = −3 y x = 3</strong>."))])}
{caja("ojo", t("Write them down before cancelling", "Anótelos antes de cancelar"), t("<p>Even if a factor cancels when you simplify, the value that made it zero is still excluded. That is why you read the excluded values in the original denominator. And watch the sign: (x − 3) is zero at x = 3, and (x + 2) at x = −2.</p>", "<p>Aunque al simplificar se cancele un factor, el valor que lo anulaba sigue excluido del dominio. Por eso los valores excluidos se leen en el denominador original. Y cuide el signo: (x − 3) se anula en x = 3, y (x + 2) en x = −2.</p>"))}
{practica("p4", t("Practice 4 — 3 / (x − 5)", "Práctica 4 — 3 / (x − 5)"), t("Which values are excluded?", "¿Qué valores se excluyen?"), [("a", "x = 5"), ("b", "x = −5"), ("c", "x = 3")])}
{practica("p5", t("Practice 5 — (x + 1) / [(x − 4)(x + 2)]", "Práctica 5 — (x + 1) / [(x − 4)(x + 2)]"), t("Which values are excluded?", "¿Qué valores se excluyen?"), [("a", t("x = −4 and x = 2", "x = −4 y x = 2")), ("b", "x = −1"), ("c", t("x = 4 and x = −2", "x = 4 y x = −2"))])}
{practica("p6", t("Practice 6 — x / (x² − 16)", "Práctica 6 — x / (x² − 16)"), t("Which values are excluded?", "¿Qué valores se excluyen?"), [("a", "x = 16"), ("b", t("x = 4 and x = −4", "x = 4 y x = −4")), ("c", t("x = 4 only", "x = 4 solamente"))])}
{enlace(n, t("excluded", "excluidos"), t("excluded values", "los valores excluidos"), t("Build a denominator (x − p)(x − q), try values of x, and see what happens when the denominator becomes zero.", "Arme (x − p)(x − q), pruebe valores de x y compruebe qué ocurre cuando el denominador se vuelve cero."))}'''

    s4 = f'''<p>{t("You can only cancel <strong>factors</strong> (things that multiply everything), never <strong>terms</strong> (things that are added or subtracted).", "Solo se cancelan <strong>factores</strong> (cosas que multiplican a todo), nunca <strong>términos</strong> (cosas que se suman o restan).")}</p>
{tabla(t("Factor or term", "Factor o término"), t("The difference between a factor and a term in the numerator", "Diferencia entre factor y término en el numerador"), [t("Expression", "Expresión"), t("What is the x?", "¿Qué es la x?"), t("Can it cancel?", "¿Se puede cancelar?")],
  [["x(x + 4)", t("A factor: it multiplies the whole parentheses", "Un factor: multiplica a todo el paréntesis"), t("Yes", "Sí")], ["x + 4", t("A term: it is added", "Un término: está sumado"), "No"]])}
{ejemplo(t("Example 5: done right. Simplify (x + 2) / (x² − 4).", "Ejemplo 5 · Bien hecho. Simplificar (x + 2) / (x² − 4)."),
  [("1", t("Factor the denominator:", "Se factoriza el denominador:"), "(x + 2)(x − 2)."), ("2", t("(x + 2) is a common factor: it cancels.", "(x + 2) es un factor común: se cancela."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>1 / (x − 2)</strong>.")])}
{caja("ojo", t("A wrong cancellation", "Cancelación incorrecta"), t("<p>In (x + 4) / x you cannot cancel the x to get 4, because on top the x is added (it is a term, not a factor). In the same way, in (x + 3) / 3 the 3 is not a factor of the whole numerator, so it does not cancel. Cancelling terms is the most common mistake with algebraic fractions. The quick test: if there is a + or − sign between what you want to cancel and the rest, with no parentheses grouping them, it is a term.</p>",
 "<p>En (x + 4) / x no se puede cancelar la x para obtener 4, porque arriba la x está sumada (es un término, no un factor). De igual modo, en (x + 3) / 3 el 3 no es factor de todo el numerador, así que no se cancela. Cancelar términos es el error más común con fracciones algebraicas. La prueba rápida: si entre lo que quiere cancelar y el resto hay un signo + o − sin paréntesis que los agrupe, es un término.</p>"))}
{enlace(n, t("trap", "trampa"), t("factors, not terms", "factores, no términos"), t("Judge cancellations: some are valid and some are not, with the reason in each case.", "Juzgue cancelaciones: unas válidas y otras no, con la explicación de por qué en cada caso."))}'''

    secciones = [("s-" + t("analogy", "analogia"), t("Just like fractions of numbers", "La analogía con las fracciones numéricas"), s1),
                 ("s-" + t("simplify", "simplificar"), t("Simplifying algebraic fractions", "Simplificar fracciones algebraicas"), s2),
                 ("s-" + t("excluded", "excluidos"), t("Values excluded from the domain", "Valores excluidos del dominio"), s3),
                 ("s-" + t("trap", "trampa"), t("The trap: factors, not terms", "El error trampa: factores, no términos"), s4)]

    lesson = {"next": t("Lesson 5.2", "Lección 5.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("One x cancels: x² / x = x.", "Se cancela una x: x² / x = x."), "b": t("4/6 can still be simplified: divide by 2.", "4/6 todavía se simplifica: divida entre 2.")}, "right": "(2 · 2 · x · x) / (2 · 3 · x) = 2x / 3.", "solution": "2x / 3."},
      "p2": {"ok": "b", "hints": {"a": t("Factor x² − 1 = (x + 1)(x − 1) and cancel (x − 1).", "Factorice x² − 1 = (x + 1)(x − 1) y cancele (x − 1)."), "c": t("The denominator (x − 1) cancels with a factor of the numerator.", "El denominador (x − 1) se cancela con un factor del numerador.")}, "right": "(x + 1)(x − 1) / (x − 1) = x + 1.", "solution": "x + 1."},
      "p3": {"ok": "a", "hints": {"b": t("Factor: x² + 4x + 4 = (x + 2)(x + 2).", "Factorice: x² + 4x + 4 = (x + 2)(x + 2)."), "c": t("You cannot cancel terms: factor first.", "No se cancelan términos: primero factorice.")}, "right": "(x + 2)(x + 2) / (x + 2) = x + 2.", "solution": "x + 2."},
      "p4": {"ok": "a", "hints": {"b": t("x − 5 = 0 gives x = 5, not −5.", "x − 5 = 0 da x = 5, no −5."), "c": t("The 3 is in the numerator: it does not matter.", "El 3 está en el numerador: no importa.")}, "right": t("x − 5 = 0 at x = 5.", "x − 5 = 0 en x = 5."), "solution": "x = 5."},
      "p5": {"ok": "c", "hints": {"a": t("Watch the signs: x − 4 = 0 gives x = 4.", "Cuide los signos: x − 4 = 0 da x = 4."), "b": t("Excluded values come from the denominator, not the numerator.", "Los valores excluidos salen del denominador, no del numerador.")}, "right": t("x − 4 = 0 or x + 2 = 0.", "x − 4 = 0 o x + 2 = 0."), "solution": t("x = 4 and x = −2.", "x = 4 y x = −2.")},
      "p6": {"ok": "b", "hints": {"a": t("Factor x² − 16 = (x + 4)(x − 4).", "Factorice x² − 16 = (x + 4)(x − 4)."), "c": t("(−4)² is also 16.", "(−4)² también es 16.")}, "right": "(x + 4)(x − 4) = 0.", "solution": t("x = 4 and x = −4.", "x = 4 y x = −4.")},
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("One x cancels: x³ / x = x².", "Se cancela una x: x³ / x = x²."), "b": t("8/12 can still be simplified.", "8/12 todavía se simplifica."), "d": t("4/6 can still be simplified.", "4/6 todavía se simplifica.")}, "solution": "2x² / 3."},
      "B": {"ok": "d", "hints": {"a": t("(x + 3) is the factor that cancels.", "(x + 3) es el factor que se cancela."), "b": t("Factor: x² − 9 = (x + 3)(x − 3).", "Factorice: x² − 9 = (x + 3)(x − 3)."), "c": t("You cannot cancel terms.", "No se cancelan términos.")}, "solution": "x − 3."},
      "C": {"ok": "a", "hints": {"b": t("(x + 2) cancels; (x − 2) stays.", "(x + 2) se cancela; queda (x − 2)."), "c": t("The numerator becomes 1, so (x − 2) stays in the denominator.", "El numerador queda en 1, así que (x − 2) sigue abajo."), "d": t("(x + 2) cancels top and bottom.", "(x + 2) se cancela arriba y abajo.")}, "solution": "1 / (x − 2)."},
      "D": {"ok": "b", "hints": {"a": t("(x + 2) is the factor that cancels.", "(x + 2) es el factor que se cancela."), "c": t("Factor: (x + 2)(x + 3).", "Factorice: (x + 2)(x + 3)."), "d": t("You cannot cancel terms.", "No se cancelan términos.")}, "solution": "x + 3."},
      "E": {"ok": "a", "hints": {"b": t("x − 7 = 0 gives x = 7.", "x − 7 = 0 da x = 7."), "c": t("The 5 is in the numerator.", "El 5 está en el numerador."), "d": t("At x = 0 the denominator is −7, not 0.", "En x = 0 el denominador es −7, no 0.")}, "solution": "7."},
      "F": {"ok": "c", "hints": {"a": t("Factor: x² − 9 = (x + 3)(x − 3).", "Factorice: x² − 9 = (x + 3)(x − 3)."), "b": t("The numerator does not matter.", "El numerador no importa."), "d": t("(−3)² is also 9.", "(−3)² también es 9.")}, "solution": t("x = 3 and x = −3.", "x = 3 y x = −3.")},
      "G": {"ok": "d", "hints": {"a": t("Watch the signs: x − 2 = 0 gives x = 2.", "Cuide los signos: x − 2 = 0 da x = 2."), "b": t("The numerator does not matter.", "El numerador no importa."), "c": t("x + 5 = 0 also makes it zero.", "x + 5 = 0 también lo anula.")}, "solution": t("x = 2 and x = −5.", "x = 2 y x = −5.")},
      "H": {"ok": "b", "hints": {"a": t("x = −3 is still excluded even though (x + 3) cancels.", "x = −3 sigue excluido aunque (x + 3) se cancele."), "c": t("x = 2 also makes the original denominator zero.", "x = 2 también anula el denominador original."), "d": t("Factor: x² + x − 6 = (x + 3)(x − 2).", "Factorice: x² + x − 6 = (x + 3)(x − 2).")}, "solution": t("x = 2 and x = −3.", "x = 2 y x = −3.")},
     }}

    quiz = [
     ("A", t("Simplify 8x³ / 12x.", "Simplifique 8x³ / 12x."), [("a", "2x³ / 3"), ("b", "8x² / 12"), ("c", "2x² / 3"), ("d", "4x² / 6")]),
     ("B", t("Simplify (x² − 9) / (x + 3).", "Simplifique (x² − 9) / (x + 3)."), [("a", "x + 3"), ("b", "x − 9"), ("c", "x² − 3"), ("d", "x − 3")]),
     ("C", t("Simplify (x + 2) / (x² − 4).", "Simplifique (x + 2) / (x² − 4)."), [("a", "1 / (x − 2)"), ("b", "1 / (x + 2)"), ("c", "x − 2"), ("d", "(x + 2) / (x − 2)")]),
     ("D", t("Simplify (x² + 5x + 6) / (x + 2).", "Simplifique (x² + 5x + 6) / (x + 2)."), [("a", "x + 2"), ("b", "x + 3"), ("c", "x + 5"), ("d", "x² + 3")]),
     ("E", t("Which value is excluded in 5 / (x − 7)?", "¿Qué valor se excluye en 5 / (x − 7)?"), [("a", "7"), ("b", "−7"), ("c", "5"), ("d", "0")]),
     ("F", t("Which values are excluded in (x + 1) / (x² − 9)?", "¿Qué valores se excluyen en (x + 1) / (x² − 9)?"), [("a", "x = 9"), ("b", "x = −1"), ("c", t("x = 3 and x = −3", "x = 3 y x = −3")), ("d", t("x = 3 only", "x = 3 solamente"))]),
     ("G", t("Which values are excluded in x / [(x − 2)(x + 5)]?", "¿Qué valores se excluyen en x / [(x − 2)(x + 5)]?"), [("a", t("x = −2 and x = 5", "x = −2 y x = 5")), ("b", "x = 0"), ("c", t("x = 2 only", "x = 2 solamente")), ("d", t("x = 2 and x = −5", "x = 2 y x = −5"))]),
     ("H", t("When you simplify (x + 3) / (x² + x − 6), which values must be excluded?", "Al simplificar (x + 3) / (x² + x − 6), ¿qué valores hay que excluir?"), [("a", t("x = 2 only", "x = 2 solamente")), ("b", t("x = 2 and x = −3", "x = 2 y x = −3")), ("c", t("x = −3 only", "x = −3 solamente")), ("d", t("x = 3 and x = −2", "x = 3 y x = −2"))])]

    tarea = (t("For your own work, with your notebook open: (1) Which values do I exclude? Simplify these eight expressions and write down the excluded values from the original denominator: 6x / 9x², (x² − 9) / (x + 3), (x² + 5x + 6) / (x² − 4), (2x + 8) / (x² + 4x), (x² − x − 12) / (x² − 16), (3x − 6) / (x² − 4x + 4), (x² − 25) / (x² − 10x + 25), and (4x² − 1) / (2x² + x). Mark in each one the factor you cancelled. (2) Mistake hunters: each simplification is wrong. Explain in one sentence why it cannot be cancelled and correct it: (x + 5) / 5 = x; (x² + 4) / (x + 2) = x + 2; (x + 3) / (x + 6) = 1/2. (3) From numbers to polynomials: simplify 12/18 and, next to it, (x² + 5x + 6) / (x² + 6x + 9), writing the factor-and-cancel steps side by side. Then make up two more pairs. Then do several exercises of each activity on the practice page, solving them in your notebook first. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) ¿Qué valores excluyo? Simplifique estas ocho expresiones y anote los valores excluidos a partir del denominador original: 6x / 9x², (x² − 9) / (x + 3), (x² + 5x + 6) / (x² − 4), (2x + 8) / (x² + 4x), (x² − x − 12) / (x² − 16), (3x − 6) / (x² − 4x + 4), (x² − 25) / (x² − 10x + 25) y (4x² − 1) / (2x² + x). Señale en cada una el factor que canceló. (2) Cazadores del error: cada simplificación es incorrecta. Explique en una frase por qué no se puede cancelar y corríjala: (x + 5) / 5 = x; (x² + 4) / (x + 2) = x + 2; (x + 3) / (x + 6) = 1/2. (3) Del número al polinomio: simplifique 12/18 y, a su lado, (x² + 5x + 6) / (x² + 6x + 9), escribiendo los pasos de factorizar y cancelar en paralelo. Después invente dos pares más. Después haga varios ejercicios de cada actividad de la página de práctica, resolviéndolos primero en el cuaderno. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Explain to someone at home why (x + 4) / x is not 4. Ask them to try x = 2: (2 + 4) / 2 = 3, not 4. A number check like this catches a wrong cancellation every time.",
               "Explíquele a alguien en casa por qué (x + 4) / x no es 4. Pídale que pruebe con x = 2: (2 + 4) / 2 = 3, no 4. Una prueba con números como esta descubre siempre una cancelación incorrecta."))

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Simplify a rational expression by factoring the top and the bottom and cancelling only common factors, and find the values excluded from the domain.", "Simplifique una expresión racional factorizando arriba y abajo y cancelando solo factores comunes, e identifique los valores excluidos del dominio."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Relate</strong> simplifying rational expressions to simplifying fractions of numbers.", "<strong>Relacionar</strong> la simplificación de expresiones racionales con la de fracciones numéricas."),
         t("<strong>Simplify</strong> by factoring the numerator and the denominator and cancelling common factors.", "<strong>Simplificar</strong> factorizando numerador y denominador y cancelando los factores comunes."),
         t("<strong>Find</strong> the values excluded from the domain.", "<strong>Identificar</strong> los valores excluidos del dominio."),
         t("<strong>Tell</strong> a factor from a term, and avoid cancelling terms.", "<strong>Distinguir</strong> un factor de un término y evitar cancelar términos.")],
        secciones, tarea, quiz,
        t("Self-check checklist for simplifying rational expressions", "Lista de autoevaluación de la simplificación de expresiones racionales"),
        t("Self-check checklist: skills for simplifying rational expressions", "Lista de autoevaluación: destrezas para simplificar expresiones racionales"),
        [(t("Factoring top and bottom", "Factorizar numerador y denominador"), t("I factor both correctly and see the quickest pattern.", "Factorizo los dos correctamente y reconozco el patrón más eficiente."), t("I factor only one of them, or with mistakes.", "Factorizo uno de los dos o con errores."), t("I cannot factor them.", "No logro factorizar.")),
         (t("Cancelling only factors", "Cancelar solo factores"), t("I cancel only common factors and can explain why terms do not cancel.", "Cancelo únicamente factores comunes y sé explicar por qué no se cancelan términos."), t("I cancel factors, but sometimes I mix up terms.", "Cancelo factores, pero a veces confundo términos."), t("I cancel terms instead of factors.", "Cancelo términos en lugar de factores.")),
         (t("Excluded values", "Valores excluidos"), t("I find all of them, writing them down before cancelling.", "Identifico todos y los anoto antes de cancelar."), t("I find some, but I leave out the ones of the cancelled factor.", "Identifico algunos, pero omito los del factor cancelado."), t("I do not find excluded values.", "No identifico valores excluidos."))],
        t("<p>In this lesson you learned to simplify rational expressions by factoring and cancelling only common factors, and to find the values excluded from the domain.</p>\n<p>In <strong>Lesson 5.2 · Adding, subtracting, multiplying, and dividing rational expressions</strong> you will operate with these algebraic fractions: multiply (factor and cancel), divide (multiply by the reciprocal), and add or subtract with a common denominator and with different denominators, always just as with fractions of numbers.</p>",
          "<p>En esta lección se aprendió a simplificar expresiones racionales factorizando y cancelando solo factores comunes, y a identificar los valores excluidos del dominio.</p>\n<p>En la <strong>Lección 5.2 · Sumar, restar, multiplicar y dividir expresiones racionales</strong> se operará con estas fracciones algebraicas: multiplicar (factorizar y cancelar), dividir (multiplicar por el recíproco) y sumar o restar con denominador común y con denominadores diferentes, siempre por analogía con las fracciones numéricas.</p>"),
        ("5-2", ("", t("Lesson 5.2 · Adding, subtracting, multiplying, and dividing rational expressions", "Lección 5.2 · Sumar, restar, multiplicar y dividir expresiones racionales"))),
        [(t("rational expression", "expresión racional"), t("A fraction whose numerator and denominator are polynomials.", "Una fracción cuyo numerador y denominador son polinomios.")),
         (t("factor", "factor"), t("Something that multiplies the whole expression.", "Algo que multiplica a toda la expresión.")),
         (t("term", "término"), t("A part of an expression separated by + or −.", "Una parte de una expresión separada por + o −.")),
         (t("excluded value", "valor excluido"), t("A value of x that makes the original denominator zero.", "Un valor de x que hace cero al denominador original.")),
         (t("domain", "dominio"), t("All the values that x can take.", "Todos los valores que puede tomar x."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
var O = T(" or ", " o ");
var SOL_AYUDA = T("Type the excluded values separated by a comma, like: 3, −2.", "Escriba los valores excluidos separados por una coma, como: 3, −2.");
function bin(a, b){ return [b, a]; }
function casoSimp(){
  var tipo = elige(["mono", "bin", "bin", "bin", "comun"]), N, D;
  if (tipo === "mono"){ var g = elige([2, 3, 4, 5, 6]), a, b; do { a = aleatorio(1, 6); b = aleatorio(1, 6); } while (a === b || mcd(a, b) !== 1); var m1 = aleatorio(1, 4), m2 = aleatorio(1, 3); N = Fm(g * a, m1, []); D = Fm(g * b, m2, []); }
  else { var c = nz(-7, 7), u, v; do { u = nz(-7, 7); v = nz(-7, 7); } while (u === c || v === c || u === v);
    var forma = aleatorio(0, 3);
    if (forma === 0){ N = Fm(1, 0, [bin(1, c), bin(1, u)]); D = Fm(1, 0, [bin(1, c)]); }
    else if (forma === 1){ N = Fm(1, 0, [bin(1, c)]); D = Fm(1, 0, [bin(1, c), bin(1, v)]); }
    else { N = Fm(1, 0, [bin(1, c), bin(1, u)]); D = Fm(1, 0, [bin(1, c), bin(1, v)]); }
    if (tipo === "comun"){ N = Fm(elige([2, 3]), elige([0, 1]), [bin(1, c)]); D = Fm(1, 0, [bin(1, c), bin(1, v)]); } }
  var S = simplifica(N, D);
  return {N: N, D: D, S: S, Np: fProducto(N), Dp: fProducto(D)};
}
function pasosSimp(c){
  var S = c.S, P = [];
  P.push(T("Factor the numerator: ", "Se factoriza el numerador: ") + pVis(c.Np) + " = " + parteVis(c.N) + ".");
  P.push(T("Factor the denominator: ", "Se factoriza el denominador: ") + pVis(c.Dp) + " = " + parteVis(c.D) + ".");
  P.push(T("Excluded values (from the original denominator): ", "Valores excluidos (del denominador original): ") + exclTxt(c.D) + ".");
  var tn = S.cn, td = S.cd, mono = S.g > 1 || S.mm > 0;
  P.push(T("Cancel the common factors: ", "Se cancelan los factores comunes: ") + envuelve('<span class="fracc"><span class="fa">' + parteVis(c.N, tn, mono && false) + '</span><span class="fb2">' + parteVis(c.D, td) + "</span></span>", "") + (mono ? T(" and the common number and power of x", " y el número y la potencia de x comunes") + (S.g > 1 ? " (" + S.g + ")" : "") + (S.mm ? " (x" + (S.mm > 1 ? "<sup>" + S.mm + "</sup>" : "") + ")" : "") : "") + ".");
  P.push(T("Simplified form: ", "Forma simplificada: ") + "<strong>" + racF(S.N, S.D) + "</strong>.");
  return P;
}
var SIMP_FIJAS = [
  [Fm(6, 2, []), Fm(9, 1, [])], [Fm(1, 0, [bin(1, 2), bin(1, 3)]), Fm(1, 0, [bin(1, 2)])], [Fm(1, 0, [bin(1, 2), bin(1, -2)]), Fm(1, 0, [bin(1, -2), bin(1, 1)])],
  [Fm(1, 0, [bin(1, 3), bin(1, -3)]), Fm(1, 0, [bin(1, 3), bin(1, 4)])], [Fm(1, 0, [bin(1, 2), bin(1, 2)]), Fm(1, 0, [bin(1, 2)])], [Fm(2, 1, [bin(1, 3)]), Fm(1, 0, [bin(1, 3), bin(1, -3)])], [Fm(1, 0, [bin(1, 1), bin(1, -1)]), Fm(1, 0, [bin(1, 1), bin(1, 1)])]];
pasoAPaso4("sp", function(){
  var i = $("sp-ex").value, c;
  if (i === "azar") c = casoSimp(); else { var p = SIMP_FIJAS[+i]; c = {N: p[0], D: p[1], S: simplifica(p[0], p[1]), Np: fProducto(p[0]), Dp: fProducto(p[1])}; }
  return {enun: T("Simplify ", "Simplifique ") + racP(c.Np, c.Dp) + ".", pasos: pasosSimp(c)};
});
$("sp-ex").addEventListener("change", function(){ $("sp-nuevo").click(); });
OMR("sq", function(){
  var c = casoSimp(), S = c.S, ok = racF(S.N, S.D), vis = {}, ops = [];
  function mete(clave, N, D){ var h = racF(N, D); if (!vis[h]){ vis[h] = 1; ops.push({clave: clave, html: h}); } }
  mete("ok", S.N, S.D);
  mete("inv", S.D, S.N);
  if (S.N.f.length) mete("s1", Fm(S.N.k, S.N.m, [[-S.N.f[0][0], S.N.f[0][1]]].concat(S.N.f.slice(1))), S.D);
  if (S.D.f.length) mete("s2", S.N, Fm(S.D.k, S.D.m, [[-S.D.f[0][0], S.D.f[0][1]]].concat(S.D.f.slice(1))));
  mete("nada", c.N, c.D.f.length ? Fm(c.D.k, c.D.m, c.D.f.slice(1)) : Fm(c.D.k, c.D.m + 1, []));
  if (!S.N.f.length && !S.D.f.length){ mete("m1", Fm(S.N.k, S.N.m + 1, []), S.D); mete("m2", Fm(c.N.k, S.N.m, []), Fm(c.D.k, S.D.m, [])); }
  while (ops.length < 3) mete("e" + ops.length, Fm(S.N.k + ops.length, S.N.m, S.N.f), S.D);
  return {enun: T("Choose the simplified form of ", "Seleccione la forma simplificada de ") + racP(c.Np, c.Dp) + ".", correcta: "ok", opciones: baraja(ops.slice(0, 4)),
    porClave: {inv: T("The numerator stays on top and the denominator on the bottom.", "El numerador se queda arriba y el denominador abajo."), s1: T("Check the sign inside the parentheses.", "Revise el signo dentro del paréntesis."), s2: T("Check the sign inside the parentheses.", "Revise el signo dentro del paréntesis."), nada: T("Factor both parts first and cancel only the common factor.", "Primero factorice las dos partes y cancele solo el factor común.")},
    pista: T("Factor the top and the bottom, then cancel the common factors.", "Factorice arriba y abajo y después cancele los factores comunes."), bien: pasosSimp(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 2 · Excluded values ===== */
function exDibuja(){
  var p = leeSol($("ex-p").value), q = leeSol($("ex-q").value), x = leeSol($("ex-x").value), out = $("ex-txt");
  if (!p || !q || !x || p.length !== 1 || q.length !== 1 || x.length !== 1){ out.innerHTML = '<div class="linea">' + T("Type one number in each box.", "Escriba un número en cada casilla.") + "</div>"; return; }
  p = p[0]; q = q[0]; x = x[0];
  var den = "(" + pVis(bin(1, -p)) + ")(" + pVis(bin(1, -q)) + ")", f1 = x - p, f2 = x - q, v = f1 * f2, r = function(n){ return sg(Math.round(n * 1000) / 1000); };
  out.innerHTML = '<div class="linea">' + T("Denominator: ", "Denominador: ") + "<strong>" + den + "</strong></div>" +
    '<div class="linea">' + T("With x = ", "Con x = ") + r(x) + ": (" + r(x) + (p < 0 ? " + " + r(-p) : " − " + r(p)) + ")(" + r(x) + (q < 0 ? " + " + r(-q) : " − " + r(q)) + ") = (" + r(f1) + ")(" + r(f2) + ") = <strong>" + r(v) + "</strong></div>" +
    '<div class="linea">' + (v === 0 ? '<strong style="color:#c62828">' + T("The denominator is 0: the fraction is not defined. x = " + r(x) + " is an excluded value.", "El denominador vale 0: la fracción no está definida. x = " + r(x) + " es un valor excluido.") + "</strong>" : T("The denominator is not 0: x = " + r(x) + " is allowed. Try x = " + r(p) + " or x = " + r(q) + ".", "El denominador no es 0: x = " + r(x) + " está permitido. Pruebe con x = " + r(p) + " o con x = " + r(q) + ".")) + "</div>";
}
["ex-p", "ex-q", "ex-x"].forEach(function(id){ $(id).addEventListener("input", exDibuja); }); exDibuja();
creaPracticaLibre("eq", function(){
  var tipo = elige(["uno", "dos", "dos", "dif", "tri", "x"]), D, Np;
  if (tipo === "uno") D = Fm(1, 0, [bin(1, nz(-9, 9))]);
  else if (tipo === "dos"){ var a = nz(-9, 9), b; do { b = nz(-9, 9); } while (b === a); D = Fm(1, 0, [bin(1, a), bin(1, b)]); }
  else if (tipo === "dif"){ var r = aleatorio(1, 9); D = Fm(1, 0, [bin(1, r), bin(1, -r)]); }
  else if (tipo === "tri"){ var a2 = nz(-7, 7), b2; do { b2 = nz(-7, 7); } while (b2 === a2 || a2 + b2 === 0); D = Fm(1, 0, [bin(1, a2), bin(1, b2)]); }
  else D = Fm(1, 1, [bin(1, nz(-9, 9))]);
  Np = elige([[nz(1, 9)], [nz(-9, 9), 1], [0, 1]]);
  var muestra = tipo === "dos" ? envuelve('<span class="fracc"><span class="fa">' + pVis(Np) + '</span><span class="fb2">' + parteVis(D) + "</span></span>", pVoz(Np) + T(", over ", ", sobre ") + parteVoz(D)) : racP(Np, fProducto(D));
  var ex = excluidos(D);
  return {enun: T("Which values of x are excluded in ", "¿Qué valores de x se excluyen en ") + muestra + "? " + SOL_AYUDA,
    evalua: function(txt){ var v = leeSol(txt); if (v && v.length && v.every(function(x){ return Math.abs(pEval(Np, x)) < 1e-9; }) && !v.every(function(x){ return ex.indexOf(x) >= 0; })) return {estado: "mal", msg: T("Those values make the numerator zero, and that is allowed. Look at the denominator.", "Esos valores anulan el numerador, y eso está permitido. Mire el denominador.")}; return evaluaSol(txt, ex); },
    solucion: (D.f.length > 1 || D.m ? T("Factor the denominator: ", "Se factoriza el denominador: ") + parteVis(D) + ". " : "") + T("Set each factor equal to zero: ", "Se iguala cada factor a cero: ") + exclTxt(D) + "."};
});

/* ===== MODULE 3 · Factors, not terms ===== */
var BANCO3 = [
  {a: "x + 4", b: "x", c: "x", ok: false, e: T("On top the x is added to 4: it is a term, not a factor. (x + 4) / x does not simplify.", "Arriba la x está sumada al 4: es un término, no un factor. (x + 4) / x no se simplifica.")},
  {a: "(x + 2)(x − 3)", b: "(x + 2)", c: "(x + 2)", ok: true, e: T("(x + 2) multiplies everything on top and is the whole denominator: it is a common factor and it cancels. x − 3 is left.", "(x + 2) multiplica a todo arriba y es todo el denominador: es un factor común y sí se cancela. Queda x − 3.")},
  {a: "x + 3", b: "3", c: "3", ok: false, e: T("The 3 on top is added to x: it is a term. It could cancel only if it multiplied the whole numerator.", "El 3 de arriba está sumado a la x: es un término. Solo se podría cancelar si multiplicara a todo el numerador.")},
  {a: "2x + 6", b: "2", c: "2", ok: true, e: T("2x + 6 = 2(x + 3): the 2 is a factor of the whole numerator. It cancels and x + 3 is left.", "2x + 6 = 2(x + 3): el 2 sí es factor común de todo el numerador. Se cancela y queda x + 3.")},
  {a: "x² + 4", b: "x²", c: "x²", ok: false, e: T("On top x² is added to 4: it is a term. The expression does not simplify.", "Arriba x² está sumado al 4: es un término. La expresión no se simplifica.")},
  {a: "5(x − 1)", b: "10(x − 1)", c: "(x − 1)", ok: true, e: T("(x − 1) multiplies on top and on the bottom: it cancels. 5/10 also simplifies, and 1/2 is left.", "(x − 1) multiplica arriba y abajo: se cancela. También se simplifica 5/10, y queda 1/2.")},
  {a: "x² − 9", b: "x − 3", c: "(x − 3)", ok: true, e: T("Factor first: x² − 9 = (x + 3)(x − 3). Then (x − 3) is a common factor. x + 3 is left.", "Primero se factoriza: x² − 9 = (x + 3)(x − 3). Entonces (x − 3) sí es factor común. Queda x + 3.")},
  {a: "x − 5", b: "x", c: "x", ok: false, e: T("On top the x has 5 subtracted from it: it is a term. Cancelling it to leave −5 is the most common mistake.", "Arriba la x está restando 5: es un término. Cancelarla para dejar −5 es el error más común.")},
  {a: "x² + 4", b: "x + 2", c: "(x + 2)", ok: false, e: T("x² + 4 is a sum of squares: it does not factor, so (x + 2) is not a factor of the numerator.", "x² + 4 es una suma de cuadrados: no se factoriza, así que (x + 2) no es factor del numerador.")},
  {a: "x + 3", b: "x + 6", c: "x", ok: false, e: T("The x is a term on top and on the bottom. Check with x = 1: 4/7 is not 3/6 = 1/2.", "La x es un término arriba y abajo. Compruebe con x = 1: 4/7 no es 3/6 = 1/2.")},
  {a: "3x(x + 1)", b: "6x", c: "3x", ok: true, e: T("3x multiplies the whole numerator and 6x = 2 · 3x: it cancels and (x + 1)/2 is left.", "3x multiplica a todo el numerador y 6x = 2 · 3x: se cancela y queda (x + 1)/2.")}];
var B3 = -1;
OMR("tq", function(){ var i; do { i = aleatorio(0, BANCO3.length - 1); } while (i === B3); B3 = i; var b = BANCO3[i];
  return {enun: T("Is it correct to cancel ", "¿Es correcto cancelar ") + "<strong>" + b.c + "</strong>" + T(" in ", " en ") + envuelve('<span class="fracc"><span class="fa">' + b.a + '</span><span class="fb2">' + b.b + "</span></span>", b.a + T(", over ", ", sobre ") + b.b) + "?", correcta: b.ok ? "si" : "no",
    opciones: [{clave: "si", html: T("Yes: what cancels is a factor", "Sí: lo que se cancela es un factor")}, {clave: "no", html: T("No: what cancels is a term", "No: lo que se cancela es un término")}], enOrden: true,
    pista: T("Is there a + or − sign between it and the rest, with no parentheses grouping them?", "¿Hay un signo + o − entre eso y el resto, sin paréntesis que los agrupe?"), bien: b.e};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    ej = [("azar", t("A new one, at random", "Una nueva, al azar")), ("0", "6x² / 9x"), ("1", "(x² + 5x + 6) / (x + 2)"), ("2", "(x² − 4) / (x² − x − 2)"), ("3", "(x² − 9) / (x² + 7x + 12)"), ("4", "(x² + 4x + 4) / (x + 2)"), ("5", "(2x² + 6x) / (x² − 9)"), ("6", "(x² − 1) / (x² + 2x + 1)")]
    campo = lambda i, et, v: f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="numeric" autocomplete="off" id="{i}" value="{v}" style="width:6em"></div>'
    mods = [
     (t("simplify", "simplificar"), t("Simplifying algebraic fractions", "Simplificar fracciones algebraicas"),
      f'''      <p>{t("Simplifying an algebraic fraction is the same as simplifying 12/18: factor the top and the bottom and cancel the common factors. Three steps, always in the same order.", "Simplificar una fracción algebraica es lo mismo que simplificar 12/18: se factoriza arriba y abajo y se cancelan los factores comunes. Tres pasos, siempre en el mismo orden.")}</p>
      <div class="panel"><div class="campos">{n4.lista("sp-ex", t("Expression to simplify", "Expresión que se va a simplificar"), ej, "1")}</div></div>
{n4.pasos("sp", t("Another expression", "Otra expresión"))}
      <div class="caja-tip">{t("Write down the excluded values before cancelling: when a factor cancels, it disappears from the expression, but the value that made it zero is still not allowed. That is why you read the excluded values in the original denominator.", "Anote los valores excluidos antes de cancelar: al cancelar, el factor desaparece de la expresión, pero el valor que lo anulaba sigue prohibido. Por eso los valores excluidos se leen siempre en el denominador original.")}</div>
{B.om("sq", t("Practice: which is the simplified form?", "Practique: ¿cuál es la forma simplificada?"))}'''),
     (t("excluded", "excluidos"), t("Values excluded from the domain", "Valores excluidos del dominio"),
      f'''      <p>{t("A fraction can never have a denominator equal to zero: division by zero is not defined. The excluded values are the ones that make the denominator zero. To find them, factor the denominator and set each factor equal to zero.", "Una fracción nunca puede tener el denominador igual a cero: la división entre cero no está definida. Los valores excluidos son los que hacen cero al denominador. Para hallarlos se factoriza el denominador y se iguala cada factor a cero.")}</p>
      <div class="panel"><p><strong>{t("Denominator explorer.", "Explorador del denominador.")}</strong> {t("Build (x − p)(x − q) by choosing p and q, and try different values of x.", "Arme (x − p)(x − q) eligiendo p y q, y pruebe distintos valores de x.")}</p><div class="campos">{campo("ex-p", t("Value of p", "Valor de p"), 3)}{campo("ex-q", t("Value of q", "Valor de q"), -2)}{campo("ex-x", t("Try x =", "Pruebe con x ="), 1)}</div></div>
{n4.salida("ex-txt")}
      <div class="caja-atencion"><strong>{t("Watch the sign:", "Ojo con el signo:")}</strong> {t("the factor (x − 3) is zero at x = 3, and the factor (x + 2) is zero at x = −2. The excluded value is the one that makes the factor zero, not the number written in it.", "el factor (x − 3) se anula en x = 3, y el factor (x + 2) se anula en x = −2. El valor excluido es el que hace cero al factor, no el número que aparece escrito en él.")}</div>
{libre("eq", t("Practice: which values are excluded?", "Practique: ¿qué valores se excluyen?"), t("Excluded values", "Valores excluidos"))}'''),
     (t("trap", "trampa"), t("The trap: factors, not terms", "El error trampa: factores, no términos"),
      f'''      <p>{t("Only factors cancel: things that multiply the whole expression. Terms never cancel: they are the parts separated by plus or minus signs.", "Solo se cancelan factores, es decir, cosas que multiplican a toda la expresión. Nunca se cancelan términos, que son las partes separadas por signos de suma o resta.")}</p>
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("The difference between a factor and a term", "Diferencia entre factor y término")}</caption><thead><tr><th scope="col">{t("Expression", "Expresión")}</th><th scope="col">{t("What is the x?", "¿Qué es la x?")}</th><th scope="col">{t("Can it cancel?", "¿Se puede cancelar?")}</th></tr></thead><tbody><tr><td>x(x + 4)</td><td>{t("A factor: it multiplies the whole parentheses", "Un factor: multiplica a todo el paréntesis")}</td><td>{t("Yes", "Sí")}</td></tr><tr><td>x + 4</td><td>{t("A term: it is added", "Un término: está sumado")}</td><td>No</td></tr></tbody></table></div>
      <div class="caja-tip">{t("The quick test: if there is a + or − sign between what you want to cancel and the rest, with no parentheses grouping them, it is a term and it does not cancel. If it multiplies everything else, it is a factor and it cancels. When in doubt, try a number: with x = 2, (x + 4)/x = 3, not 4.", "La prueba rápida: si entre la parte que quiere cancelar y el resto hay un signo + o − sin paréntesis que los agrupe, es un término y no se cancela. Si multiplica a todo lo demás, es un factor y sí se cancela. En caso de duda, pruebe con un número: con x = 2, (x + 4)/x = 3, no 4.")}</div>
{B.om("tq", t("Practice: is this cancellation correct?", "Practique: ¿es correcta esta cancelación?"))}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Simplificar expresiones racionales: factorizar y cancelar")
