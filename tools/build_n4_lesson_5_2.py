"""Level 4 · Lesson 5.2 · Adding, subtracting, multiplying, and dividing rational expressions — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_5-2.html and algebra/n4-l5-2.html (multiply, divide, add and subtract with the same
denominator and with different denominators). They are rebuilt here, inside LearnGED, with the rational-expression helpers of math/poly4.js.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "5-2"
TEMA = ("Rational expressions", "Expresiones racionales")
TIT = ("Adding, subtracting, multiplying, and dividing rational expressions", "Sumar, restar, multiplicar y dividir expresiones racionales")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)
ESTILO = n4.ESTILO + """
  .tachado{text-decoration:line-through;text-decoration-color:#c62828;text-decoration-thickness:3px;color:#78909c;}
  .enun .fracc,.paso4 .fracc,.opciones .fracc{margin:4px 3px;}
"""

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 5.1.</strong> In Lesson 5.1 you simplified rational expressions by factoring and cancelling. Now you operate with them. The good news: each operation is the same as with fractions of numbers. If you can operate with 2/3 and 1/4, you can operate with fractions of polynomials.", "<strong>Conexión con la lección anterior.</strong> En la Lección 5.1 se simplificaron expresiones racionales factorizando y cancelando. Ahora se opera con ellas. La buena noticia: cada operación es idéntica a la de las fracciones numéricas. Si se sabe operar con 2/3 y 1/4, se sabe operar con fracciones de polinomios.")}</p>
<p>{t("To multiply fractions, factor, cancel any common factor (a top one with a bottom one), and multiply the numerators and the denominators. Cancelling before multiplying saves a lot of work.", "Para multiplicar fracciones se factoriza, se cancela cualquier factor común (de arriba con abajo) y se multiplican los numeradores y los denominadores. Cancelar antes de multiplicar ahorra mucho trabajo.")}</p>
{ejemplo(t("Example 1: multiply (x + 2)/(x − 3) · (x − 3)/(x + 5).", "Ejemplo 1 · Multiplicar (x + 2)/(x − 3) · (x − 3)/(x + 5)."),
  [("1", t("Cancel the common factor (x − 3).", "Se cancela el factor común (x − 3)."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>(x + 2)/(x + 5)</strong>.")])}
{ejemplo(t("Example 2: multiply 6x/(x + 1) · (x + 1)/3.", "Ejemplo 2 · Multiplicar 6x/(x + 1) · (x + 1)/3."),
  [("1", t("Cancel (x + 1).", "Se cancela (x + 1)."), ""), ("2", t("6x/3 is left, and 6 ÷ 3 = 2.", "Queda 6x/3, y 6 ÷ 3 = 2."), ""), ("✓", t("Answer.", "Respuesta."), "<strong>2x</strong>.")])}
{practica("p1", t("Practice 1 — (x/4) · (8/x)", "Práctica 1 — (x/4) · (8/x)"), t("Choose the simplified product.", "Seleccione el producto simplificado."), [("a", "x/2"), ("b", "2"), ("c", "8/x")])}
{practica("p2", t("Practice 2 — [(x + 3)/(x − 1)] · [(x − 1)/(x + 2)]", "Práctica 2 — [(x + 3)/(x − 1)] · [(x − 1)/(x + 2)]"), t("Choose the simplified product.", "Seleccione el producto simplificado."), [("a", "(x − 1)/(x + 2)"), ("b", "(x + 3)/(x − 1)"), ("c", "(x + 3)/(x + 2)")])}
{practica("p3", t("Practice 3 — (10/x) · (x/5)", "Práctica 3 — (10/x) · (x/5)"), t("Choose the simplified product.", "Seleccione el producto simplificado."), [("a", "2"), ("b", "5"), ("c", "10/(5x)")])}
{enlace(n, t("multiply", "multiplicar"), t("multiplying", "la multiplicación"), t("Products solved step by step, with the cross-cancelling marked on the fractions, and exercises that change every time.", "Productos resueltos paso a paso, con la cancelación en cruz marcada sobre las fracciones, y ejercicios que cambian cada vez."))}'''

    s2 = f'''<p>{t("Dividing is multiplying by the reciprocal: flip the second fraction and multiply. The rule is “keep, change, flip.”", "Dividir es multiplicar por el recíproco: se voltea la segunda fracción y se multiplica. La regla se resume como «deja, cambia, voltea».")}</p>
<p class="formula" style="text-align:center;font-size:1.25rem;font-weight:700;">a/b ÷ c/d = a/b · d/c</p>
{ejemplo(t("Example 3: divide (x/2) ÷ (x²/6).", "Ejemplo 3 · Dividir (x/2) ÷ (x²/6)."),
  [("1", t("Multiply by the reciprocal:", "Se multiplica por el recíproco:"), "(x/2) · (6/x²)."), ("2", t("Cancel:", "Se cancela:"), "6x / (2x²) = 3/x."), ("✓", t("Answer.", "Respuesta."), "<strong>3/x</strong>.")])}
{practica("p4", t("Practice 4 — (x/2) ÷ (x/8)", "Práctica 4 — (x/2) ÷ (x/8)"), t("Choose the simplified quotient.", "Seleccione el cociente simplificado."), [("a", "1/4"), ("b", "x²/16"), ("c", "4")])}
{practica("p5", t("Practice 5 — [(x + 1)/3] ÷ [(x + 1)/9]", "Práctica 5 — [(x + 1)/3] ÷ [(x + 1)/9]"), t("Choose the simplified quotient.", "Seleccione el cociente simplificado."), [("a", "1/3"), ("b", "3"), ("c", "(x + 1)/3")])}
{practica("p6", t("Practice 6 — [x/(x + 2)] ÷ [x²/(x + 2)]", "Práctica 6 — [x/(x + 2)] ÷ [x²/(x + 2)]"), t("Choose the simplified quotient.", "Seleccione el cociente simplificado."), [("a", "1/x"), ("b", "x"), ("c", "x²")])}
{enlace(n, t("divide", "dividir"), t("dividing", "la división"), t("“Keep, change, flip” step by step: watch the second fraction flip before cancelling.", "«Deja, cambia, voltea» paso a paso: se ve cómo se invierte la segunda fracción antes de cancelar."))}'''

    s3 = f'''<p>{t("When the denominators are the same, combine the numerators and keep the denominator, just as 2/7 + 3/7 = 5/7.", "Cuando los denominadores son iguales, se combinan los numeradores y se conserva el denominador. Igual que 2/7 + 3/7 = 5/7.")}</p>
{ejemplo(t("Example 4: add 3x/(x + 2) + 4/(x + 2).", "Ejemplo 4 · Sumar 3x/(x + 2) + 4/(x + 2)."),
  [("1", t("Same denominator: add the numerators,", "Mismo denominador: se suman los numeradores,"), "3x + 4."), ("✓", t("Answer.", "Respuesta."), "<strong>(3x + 4)/(x + 2)</strong>.")])}
{ejemplo(t("Example 5: subtraction. Subtract 5x/(x − 3) − 2x/(x − 3).", "Ejemplo 5 · Resta. Restar 5x/(x − 3) − 2x/(x − 3)."),
  [("1", t("Subtract the numerators:", "Se restan los numeradores:"), "5x − 2x = 3x."), ("✓", t("Answer.", "Respuesta."), "<strong>3x/(x − 3)</strong>.")])}
{caja("ojo", t("When you subtract, use parentheses", "Al restar, use paréntesis"), t("<p>The minus sign goes to the whole second numerator: (2x + 1) − (x − 3) = 2x + 1 − x + 3 = x + 4. Forgetting the parentheses gives x − 2, which is wrong. And the denominator does not change: you never add the denominators.</p>", "<p>El signo menos se reparte a todo el segundo numerador: (2x + 1) − (x − 3) = 2x + 1 − x + 3 = x + 4. Si se olvida el paréntesis sale x − 2, que es incorrecto. Y el denominador no cambia: nunca se suman los denominadores.</p>"))}
{enlace(n, t("same", "sumar-igual"), t("adding and subtracting with the same denominator", "la suma y la resta con igual denominador"), t("It includes the “See the common mistake” button, which shows what happens when you forget the parentheses in a subtraction.", "Incluye el botón «Ver el error frecuente», que muestra qué pasa cuando se olvida el paréntesis al restar el segundo numerador."))}'''

    s4 = f'''<p>{t("When the denominators are different, find the least common denominator (LCD), rewrite each fraction with it, and then combine the numerators. It is the same process as 1/2 + 1/3 = 3/6 + 2/6 = 5/6.", "Cuando los denominadores son distintos, se busca el mínimo común múltiplo (MCM) de los denominadores, se reescriben las fracciones con ese denominador común y luego se combinan los numeradores. Es el mismo proceso que en 1/2 + 1/3 = 3/6 + 2/6 = 5/6.")}</p>
{ejemplo(t("Example 6: add 1/x + 1/(2x).", "Ejemplo 6 · Sumar 1/x + 1/(2x)."),
  [("1", t("LCD of x and 2x:", "MCM de x y 2x:"), "2x."), ("2", t("Rewrite:", "Se reescribe:"), "2/(2x) + 1/(2x)."), ("3", t("Add the numerators:", "Se suman los numeradores:"), "(2 + 1)/(2x)."), ("✓", t("Answer.", "Respuesta."), "<strong>3/(2x)</strong>.")])}
{ejemplo(t("Example 7: add 3/x + 2/x².", "Ejemplo 7 · Sumar 3/x + 2/x²."),
  [("1", t("LCD of x and x²:", "MCM de x y x²:"), "x²."), ("2", t("Rewrite:", "Se reescribe:"), "3x/x² + 2/x²."), ("✓", t("Answer.", "Respuesta."), "<strong>(3x + 2)/x²</strong>.")])}
{ejemplo(t("Example 8: two binomials. Add 2/x + 1/(x + 1).", "Ejemplo 8 · Dos binomios. Sumar 2/x + 1/(x + 1)."),
  [("1", t("LCD:", "MCM:"), "x(x + 1)."), ("2", t("Rewrite:", "Se reescribe:"), "2(x + 1)/[x(x + 1)] + x/[x(x + 1)]."), ("3", t("Add the numerators:", "Se suman los numeradores:"), "2x + 2 + x = 3x + 2."), ("✓", t("Answer.", "Respuesta."), "<strong>(3x + 2)/[x(x + 1)]</strong>.")])}
{caja("tip", t("The same method as with numbers", "El mismo método que con números"), t("<p>Find the LCD, rewrite each fraction, and combine the numerators. The only new thing is that the denominators are now expressions with variables.</p>", "<p>Hallar el MCM, reescribir cada fracción y combinar los numeradores. Lo único nuevo es que ahora los denominadores son expresiones con variables.</p>"))}
{practica("p7", t("Practice 7 — 2x/(x + 3) + 5/(x + 3)", "Práctica 7 — 2x/(x + 3) + 5/(x + 3)"), t("Choose the simplified result.", "Seleccione el resultado simplificado."), [("a", "(2x + 5)/(x + 3)"), ("b", "(2x + 5)/(2x + 6)"), ("c", "7x/(x + 3)")])}
{practica("p8", t("Practice 8 — (4/x) − (1/x)", "Práctica 8 — (4/x) − (1/x)"), t("Choose the simplified result.", "Seleccione el resultado simplificado."), [("a", "3"), ("b", "3/x"), ("c", "5/x")])}
{practica("p9", t("Practice 9 — (1/x) + 1/(3x)", "Práctica 9 — (1/x) + 1/(3x)"), t("Choose the simplified result.", "Seleccione el resultado simplificado."), [("a", "2/(4x)"), ("b", "1/(3x)"), ("c", "4/(3x)")])}
{enlace(n, t("different", "sumar-distinto"), t("different denominators", "los denominadores diferentes"), t("Sums and differences solved step by step: find the LCD, rewrite each fraction, and combine the numerators.", "Sumas y restas resueltas paso a paso: hallar el MCM, reescribir cada fracción y combinar los numeradores."))}'''

    secciones = [("s-" + t("multiply", "multiplicar"), t("Multiplying", "Multiplicar"), s1),
                 ("s-" + t("divide", "dividir"), t("Dividing", "Dividir"), s2),
                 ("s-" + t("same", "sumar-igual"), t("Adding and subtracting with the same denominator", "Sumar y restar con igual denominador"), s3),
                 ("s-" + t("different", "sumar-distinto"), t("Adding and subtracting with different denominators", "Sumar y restar con denominadores diferentes"), s4)]

    lesson = {"next": t("Lesson 5.3", "Lección 5.3"), "review": t("sections 2 and 4", "las secciones 2 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The x cancels too: one on top, one on the bottom.", "También se cancela la x: una arriba y otra abajo."), "c": t("Multiply both fractions, not just the second one.", "Multiplique las dos fracciones, no solo la segunda.")}, "right": t("8x/(4x) = 2.", "8x/(4x) = 2."), "solution": "2."},
      "p2": {"ok": "c", "hints": {"a": t("(x − 1) is the factor that cancels.", "(x − 1) es el factor que se cancela."), "b": t("(x − 1) appears top and bottom: it cancels.", "(x − 1) aparece arriba y abajo: se cancela.")}, "right": t("Cancel (x − 1).", "Se cancela (x − 1)."), "solution": "(x + 3)/(x + 2)."},
      "p3": {"ok": "a", "hints": {"b": t("10/5 = 2.", "10/5 = 2."), "c": t("The x cancels, and 10/5 = 2.", "La x se cancela, y 10/5 = 2.")}, "right": t("10x/(5x) = 2.", "10x/(5x) = 2."), "solution": "2."},
      "p4": {"ok": "c", "hints": {"a": t("Flip the second fraction: (x/2) · (8/x).", "Voltee la segunda fracción: (x/2) · (8/x)."), "b": t("To divide, multiply by the reciprocal.", "Para dividir, multiplique por el recíproco.")}, "right": t("(x/2) · (8/x) = 8x/(2x) = 4.", "(x/2) · (8/x) = 8x/(2x) = 4."), "solution": "4."},
      "p5": {"ok": "b", "hints": {"a": t("Flip the second fraction: · 9/(x + 1).", "Voltee la segunda fracción: · 9/(x + 1)."), "c": t("(x + 1) cancels.", "(x + 1) se cancela.")}, "right": t("[(x + 1)/3] · [9/(x + 1)] = 9/3 = 3.", "[(x + 1)/3] · [9/(x + 1)] = 9/3 = 3."), "solution": "3."},
      "p6": {"ok": "a", "hints": {"b": t("Flip: [x/(x + 2)] · [(x + 2)/x²] = x/x².", "Voltee: [x/(x + 2)] · [(x + 2)/x²] = x/x²."), "c": t("To divide, multiply by the reciprocal.", "Para dividir, multiplique por el recíproco.")}, "right": t("x/x² = 1/x.", "x/x² = 1/x."), "solution": "1/x."},
      "p7": {"ok": "a", "hints": {"b": t("The denominator stays: do not add the denominators.", "El denominador se conserva: no se suman los denominadores."), "c": t("2x and 5 are not like terms.", "2x y 5 no son términos semejantes.")}, "right": t("Add the numerators and keep (x + 3).", "Se suman los numeradores y se conserva (x + 3)."), "solution": "(2x + 5)/(x + 3)."},
      "p8": {"ok": "b", "hints": {"a": t("The denominator x stays.", "El denominador x se conserva."), "c": t("It is a subtraction: 4 − 1.", "Es una resta: 4 − 1.")}, "right": t("(4 − 1)/x = 3/x.", "(4 − 1)/x = 3/x."), "solution": "3/x."},
      "p9": {"ok": "c", "hints": {"a": t("Do not add the denominators: find the LCD, 3x.", "No sume los denominadores: busque el MCM, 3x."), "b": t("Rewrite 1/x as 3/(3x) first.", "Primero reescriba 1/x como 3/(3x).")}, "right": t("3/(3x) + 1/(3x) = 4/(3x).", "3/(3x) + 1/(3x) = 4/(3x)."), "solution": "4/(3x)."},
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("The x cancels.", "La x se cancela."), "b": t("Multiply both fractions.", "Multiplique las dos fracciones."), "c": t("The x cancels; 4/2 = 2.", "La x se cancela; 4/2 = 2.")}, "solution": "2."},
      "B": {"ok": "b", "hints": {"a": t("(x − 2) is the factor that cancels.", "(x − 2) es el factor que se cancela."), "c": t("(x − 2) cancels.", "(x − 2) se cancela."), "d": t("Only (x − 2) cancels.", "Solo se cancela (x − 2).")}, "solution": "(x + 1)/(x + 3)."},
      "C": {"ok": "a", "hints": {"b": t("Flip the second fraction: (x/3) · (6/x).", "Voltee la segunda fracción: (x/3) · (6/x)."), "c": t("To divide, multiply by the reciprocal.", "Para dividir, multiplique por el recíproco."), "d": t("6/3 = 2.", "6/3 = 2.")}, "solution": "2."},
      "D": {"ok": "a", "hints": {"b": t("Flip the second fraction: · (x − 1)/x².", "Voltee la segunda fracción: · (x − 1)/x²."), "c": t("To divide, multiply by the reciprocal.", "Para dividir, multiplique por el recíproco."), "d": t("x/x² is not 1.", "x/x² no es 1.")}, "solution": "1/x."},
      "E": {"ok": "d", "hints": {"a": t("The denominator stays the same.", "El denominador se conserva."), "b": t("3x and 4 are not like terms.", "3x y 4 no son términos semejantes."), "c": t("The denominator stays the same, not squared.", "El denominador se conserva, sin elevarlo al cuadrado.")}, "solution": "(3x + 4)/(x + 2)."},
      "F": {"ok": "b", "hints": {"a": t("The denominator stays.", "El denominador se conserva."), "c": t("It is a subtraction.", "Es una resta."), "d": t("The denominator stays the same.", "El denominador se conserva.")}, "solution": "3x/(x − 3)."},
      "G": {"ok": "b", "hints": {"a": t("Do not add the denominators: the LCD is 2x.", "No sume los denominadores: el MCM es 2x."), "c": t("Rewrite 1/x as 2/(2x) first.", "Primero reescriba 1/x como 2/(2x)."), "d": t("2/(2x) + 1/(2x) = 3/(2x).", "2/(2x) + 1/(2x) = 3/(2x).")}, "solution": "3/(2x)."},
      "H": {"ok": "a", "hints": {"b": t("Do not add the denominators: the LCD is x(x + 1).", "No sume los denominadores: el MCM es x(x + 1)."), "c": t("2(x + 1) + x = 3x + 2.", "2(x + 1) + x = 3x + 2."), "d": t("x(x + 1) = x² + x, not x² + 1.", "x(x + 1) = x² + x, no x² + 1.")}, "solution": "(3x + 2)/[x(x + 1)]."},
     }}

    quiz = [
     ("A", t("Multiply (x/2) · (4/x).", "Multiplique (x/2) · (4/x)."), [("a", "x"), ("b", "4/x"), ("c", "2x"), ("d", "2")]),
     ("B", t("Multiply [(x + 1)/(x − 2)] · [(x − 2)/(x + 3)].", "Multiplique [(x + 1)/(x − 2)] · [(x − 2)/(x + 3)]."), [("a", "(x − 2)/(x + 3)"), ("b", "(x + 1)/(x + 3)"), ("c", "(x + 1)/(x − 2)"), ("d", "1")]),
     ("C", t("Divide (x/3) ÷ (x/6).", "Divida (x/3) ÷ (x/6)."), [("a", "2"), ("b", "1/2"), ("c", "x²/18"), ("d", "6")]),
     ("D", t("Divide [x/(x − 1)] ÷ [x²/(x − 1)].", "Divida [x/(x − 1)] ÷ [x²/(x − 1)]."), [("a", "1/x"), ("b", "x"), ("c", "x²"), ("d", "1")]),
     ("E", t("Add 3x/(x + 2) + 4/(x + 2).", "Sume 3x/(x + 2) + 4/(x + 2)."), [("a", "(3x + 4)/(2x + 4)"), ("b", "7x/(x + 2)"), ("c", "(3x + 4)/(x + 2)²"), ("d", "(3x + 4)/(x + 2)")]),
     ("F", t("Subtract 5x/(x − 3) − 2x/(x − 3).", "Reste 5x/(x − 3) − 2x/(x − 3)."), [("a", "3x"), ("b", "3x/(x − 3)"), ("c", "7x/(x − 3)"), ("d", "3x/(x − 3)²")]),
     ("G", t("Add 1/x + 1/(2x).", "Sume 1/x + 1/(2x)."), [("a", "2/(3x)"), ("b", "3/(2x)"), ("c", "1/(2x)"), ("d", "2/(2x)")]),
     ("H", t("Add 2/x + 1/(x + 1).", "Sume 2/x + 1/(x + 1)."), [("a", "(3x + 2)/[x(x + 1)]"), ("b", "3/(2x + 1)"), ("c", "(2x + 2)/[x(x + 1)]"), ("d", "(3x + 2)/(x² + 1)")])]

    tarea = (t("For your own work, with your notebook open. Work the four operations as if they were four stations: (1) Multiply (factor and cancel before you operate): (x² − 9)/(x + 2) · (x + 2)/(x − 3); 2x/(x² − 1) · (x + 1)/(4x²); (x² + 3x)/(x − 5) · (x² − 25)/(x² + 8x + 15). (2) Divide (multiply by the reciprocal): (x² − 4)/(3x) ÷ (x + 2)/(6x²); (x + 1)/(x² − x) ÷ (x² − 1)/x; (x² + 2x − 8)/(x² − 9) ÷ (x + 4)/(x + 3). (3) Add and subtract with the same denominator: 3/x + 5/x; (2x + 1)/(x − 4) − (x − 3)/(x − 4); x²/(x + 2) − 4/(x + 2). In the subtractions, give the minus sign to the whole numerator. (4) Add and subtract with different denominators (write the LCD first): 2/x + 3/(x + 1); 5/(x − 2) − 1/(x + 3); x/(x² − 9) + 2/(x + 3). Solve 1/4 + 1/6 next to them to compare the steps. (5) Checking: in one problem of each station, substitute a value of x that is not excluded in the original expression and in your result. If they do not match, find the mistake. Then do several exercises of each activity on the practice page. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto. Trabaje las cuatro operaciones como si fueran cuatro estaciones: (1) Multiplicar (factorice y cancele antes de operar): (x² − 9)/(x + 2) · (x + 2)/(x − 3); 2x/(x² − 1) · (x + 1)/(4x²); (x² + 3x)/(x − 5) · (x² − 25)/(x² + 8x + 15). (2) Dividir (multiplique por el recíproco): (x² − 4)/(3x) ÷ (x + 2)/(6x²); (x + 1)/(x² − x) ÷ (x² − 1)/x; (x² + 2x − 8)/(x² − 9) ÷ (x + 4)/(x + 3). (3) Sumar y restar con igual denominador: 3/x + 5/x; (2x + 1)/(x − 4) − (x − 3)/(x − 4); x²/(x + 2) − 4/(x + 2). En las restas, reparta el signo menos a todo el numerador. (4) Sumar y restar con denominadores diferentes (escriba primero el MCM): 2/x + 3/(x + 1); 5/(x − 2) − 1/(x + 3); x/(x² − 9) + 2/(x + 3). Resuelva al lado 1/4 + 1/6 para comparar los pasos. (5) Verificación: en un problema de cada estación, sustituya un valor de x que no esté excluido en la expresión original y en su resultado. Si no dan lo mismo, busque el error. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Write 1/2 + 1/3 and 1/x + 1/(x + 1) side by side on a card. Explain to someone at home that the steps are the same, and check the second one with x = 1: 1/1 + 1/2 = 3/2, and (2x + 1)/[x(x + 1)] = 3/2.",
               "Escriba en una tarjeta 1/2 + 1/3 y 1/x + 1/(x + 1), una al lado de la otra. Explíquele a alguien en casa que los pasos son los mismos y compruebe la segunda con x = 1: 1/1 + 1/2 = 3/2, y (2x + 1)/[x(x + 1)] = 3/2."))

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Operate with rational expressions just as with fractions of numbers: factor and cancel to multiply, flip to divide, and use a common denominator to add and subtract.", "Opere con expresiones racionales igual que con fracciones numéricas: factorice y cancele para multiplicar, voltee para dividir y use un denominador común para sumar y restar."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Multiply</strong> rational expressions by factoring and cancelling first.", "<strong>Multiplicar</strong> expresiones racionales factorizando y cancelando primero."),
         t("<strong>Divide</strong> by multiplying by the reciprocal.", "<strong>Dividir</strong> multiplicando por el recíproco."),
         t("<strong>Add and subtract</strong> with the same denominator, giving the minus sign to the whole numerator.", "<strong>Sumar y restar</strong> con igual denominador, repartiendo el signo menos a todo el numerador."),
         t("<strong>Add and subtract</strong> with different denominators, using the LCD.", "<strong>Sumar y restar</strong> con denominadores diferentes, usando el MCM.")],
        secciones, tarea, quiz,
        t("Self-check checklist for operations with rational expressions", "Lista de autoevaluación de las operaciones con expresiones racionales"),
        t("Self-check checklist: skills for operating with rational expressions", "Lista de autoevaluación: destrezas para operar con expresiones racionales"),
        [(t("Multiplying and dividing", "Multiplicar y dividir"), t("I factor and cancel before multiplying, and I flip only the second fraction to divide.", "Factorizo y cancelo antes de multiplicar, y volteo solo la segunda fracción para dividir."), t("I multiply correctly, but I do not always cancel or flip.", "Multiplico bien, pero no siempre cancelo o volteo."), t("I multiply without factoring or cancelling.", "Multiplico sin factorizar ni cancelar.")),
         (t("Same denominator", "Igual denominador"), t("I combine the numerators, keep the denominator, and use parentheses to subtract.", "Combino los numeradores, conservo el denominador y uso paréntesis al restar."), t("I keep the denominator, but I forget the parentheses in subtractions.", "Conservo el denominador, pero olvido el paréntesis al restar."), t("I add the denominators.", "Sumo los denominadores.")),
         (t("Different denominators", "Denominadores diferentes"), t("I find the LCD, rewrite each fraction, and combine the numerators.", "Hallo el MCM, reescribo cada fracción y combino los numeradores."), t("I find the LCD, but I make mistakes rewriting the numerators.", "Hallo el MCM, pero me equivoco al reescribir los numeradores."), t("I add numerators and denominators directly.", "Sumo numeradores y denominadores directamente."))],
        t("<p>In this lesson you learned to multiply, divide, add, and subtract rational expressions, always just as with fractions of numbers: factor and cancel, flip to divide, and use the LCD to add and subtract.</p>\n<p>In <strong>Lesson 5.3 · Solving rational equations</strong> you will solve equations that have fractions with x in the denominator. Multiplying the whole equation by the LCD clears the fractions, but you will have to check every solution, because some may be excluded values.</p>",
          "<p>En esta lección se aprendió a multiplicar, dividir, sumar y restar expresiones racionales, siempre por analogía con las fracciones numéricas: factorizar y cancelar, voltear para dividir y usar el MCM para sumar y restar.</p>\n<p>En la <strong>Lección 5.3 · Resolver ecuaciones racionales</strong> se resolverán ecuaciones con fracciones que tienen x en el denominador. Multiplicar toda la ecuación por el MCM elimina las fracciones, pero habrá que comprobar cada solución, porque algunas pueden ser valores excluidos.</p>"),
        ("5-3", ("", t("Lesson 5.3 · Solving rational equations", "Lección 5.3 · Resolver ecuaciones racionales"))),
        [(t("reciprocal", "recíproco"), t("A fraction flipped: the reciprocal of a/b is b/a.", "Una fracción volteada: el recíproco de a/b es b/a.")),
         (t("keep, change, flip", "deja, cambia, voltea"), t("To divide fractions: keep the first, change ÷ to ·, flip the second.", "Para dividir fracciones: se deja la primera, se cambia ÷ por · y se voltea la segunda.")),
         (t("least common denominator (LCD)", "mínimo común múltiplo (MCM)"), t("The smallest expression that every denominator divides.", "La menor expresión que todos los denominadores dividen.")),
         (t("like denominators", "denominadores iguales"), t("Fractions with the same denominator: combine only the numerators.", "Fracciones con el mismo denominador: se combinan solo los numeradores."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function X(c){ return [c, 1]; }
function R(N, D){ return {N: N, D: D}; }
var POR = envuelve(" · ", T(" times ", " por ")), ENTRE = envuelve(" ÷ ", T(" divided by ", " entre "));
function frPD(Np, D){ return envuelve('<span class="fracc"><span class="fa">' + pVis(Np) + '</span><span class="fb2">' + parteVis(D) + "</span></span>", pVoz(Np) + T(", over ", ", sobre ") + parteVoz(D)); }
function frPDvis(Np, D){ return '<span class="fracc"><span class="fa">' + pVis(Np) + '</span><span class="fb2">' + parteVis(D) + "</span></span>"; }
function distintos(n, lim){ var l = []; while (l.length < n){ var v = nz(-lim, lim); if (l.indexOf(v) < 0) l.push(v); } return l; }
/* Wrong answers built from the right one: flipped, a sign changed, a number changed */
function malas(S){
  var l = [{clave: "inv", N: S.D, D: S.N}];
  if (S.N.f.length) l.push({clave: "sn", N: Fm(S.N.k, S.N.m, [[-S.N.f[0][0], 1]].concat(S.N.f.slice(1))), D: S.D});
  if (S.D.f.length) l.push({clave: "sd", N: S.N, D: Fm(S.D.k, S.D.m, [[-S.D.f[0][0], 1]].concat(S.D.f.slice(1)))});
  l.push({clave: "k", N: Fm(S.N.k * 2, S.N.m, S.N.f), D: S.D});
  l.push({clave: "m", N: Fm(S.N.k, S.N.m + 1, S.N.f), D: S.D});
  return l;
}
var PISTAS_RAC = {inv: T("The result is upside down: check which part goes on top.", "El resultado está al revés: revise qué parte va arriba."), sn: T("Check the sign inside the parentheses.", "Revise el signo dentro del paréntesis."), sd: T("Check the sign inside the parentheses.", "Revise el signo dentro del paréntesis."), k: T("Check the numbers: divide the top and bottom numbers by their common factor.", "Revise los números: divida los números de arriba y de abajo entre su factor común."), m: T("Check the powers of x: one x on top cancels one x on the bottom.", "Revise las potencias de x: una x de arriba cancela una x de abajo.")};

/* ===== MODULE 1 · Multiply ===== */
function casoMul(){
  var t = aleatorio(0, 3), A, B2, v = distintos(3, 7), a = X(v[0]), b = X(v[1]), c = X(v[2]);
  if (t === 0){ A = R(Fm(1, 0, [a]), Fm(1, 0, [b])); B2 = R(Fm(1, 0, [b]), Fm(1, 0, [c])); }
  else if (t === 1){ var q = elige([2, 3, 4, 5]), k2 = elige([2, 3, 4]); A = R(Fm(q * k2, 1, []), Fm(1, 0, [a])); B2 = R(Fm(1, 0, [a]), Fm(k2, 0, [])); }
  else if (t === 2){ var k1 = elige([2, 4, 6, 8, 10, 12]), k3 = elige([2, 3, 4, 5]); A = R(Fm(k1, 0, []), Fm(1, 1, [])); B2 = R(Fm(1, 1, []), Fm(k3, 0, [])); }
  else { var r = aleatorio(1, 6), kk = elige([2, 3, 4]); A = R(Fm(1, 0, [X(r), X(-r)]), Fm(kk, 1, [])); B2 = R(Fm(kk * elige([1, 2]), 2, []), Fm(1, 0, [X(r)])); }
  var P = racMul(A, B2), S = simplifica(P.N, P.D);
  return {A: A, B: B2, P: P, S: S, t: t};
}
function verRac(A, expandir){ return expandir ? racP(fProducto(A.N), fProducto(A.D)) : racF(A.N, A.D); }
function pasosMul(c, extra){
  var P = extra || [], S = c.S;
  if (c.t === 3) P.push(T("Factor first: ", "Primero se factoriza: ") + pVis(fProducto(c.A.N)) + " = " + parteVis(c.A.N) + ".");
  P.push(T("Write it as one fraction, numerators times numerators and denominators times denominators: ", "Se escribe como una sola fracción, numeradores por numeradores y denominadores por denominadores: ") + envuelve('<span class="fracc"><span class="fa">' + parteVis(c.P.N, S.cn, false) + '</span><span class="fb2">' + parteVis(c.P.D, S.cd) + "</span></span>", "") + (S.cn.length ? T(" (the common factors are crossed out)", " (se tachan los factores comunes)") : "") + ".");
  if (S.g > 1 || S.mm) P.push(T("Simplify the numbers and the powers of x: ", "Se simplifican los números y las potencias de x: ") + (S.g > 1 ? T("divide by ", "se divide entre ") + S.g : "") + (S.g > 1 && S.mm ? T(" and ", " y ") : "") + (S.mm ? T("cancel ", "se cancela ") + "x" + (S.mm > 1 ? "<sup>" + S.mm + "</sup>" : "") : "") + ".");
  P.push(T("Result: ", "Resultado: ") + "<strong>" + racR(S) + "</strong>.");
  return P;
}
pasoAPaso4("mu", function(){ var c = casoMul(); return {enun: T("Multiply ", "Multiplique ") + verRac(c.A, c.t === 3) + POR + racR(c.B) + ".", pasos: pasosMul(c)}; });
OMR("mq", function(){ var c = casoMul();
  return {enun: T("Choose the simplified product: ", "Seleccione el producto simplificado: ") + verRac(c.A, c.t === 3) + POR + racR(c.B) + ".", correcta: "ok", opciones: baraja(racOpciones([{clave: "ok", N: c.S.N, D: c.S.D}].concat(malas(c.S)), 4)),
    porClave: PISTAS_RAC, pista: T("Cancel the common factors (a top one with a bottom one), then multiply.", "Cancele los factores comunes (de arriba con abajo) y después multiplique."), bien: pasosMul(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 2 · Divide ===== */
function casoDiv(){ var c = casoMul(); c.Bdiv = racInv(c.B); return c; }
function pasosDiv(c){ return pasosMul(c, [T("Keep, change, flip: ", "Deja, cambia, voltea: ") + verRac(c.A, c.t === 3) + ENTRE + racR(c.Bdiv) + " = " + verRac(c.A, c.t === 3) + POR + racR(c.B) + "."]); }
pasoAPaso4("dv", function(){ var c = casoDiv(); return {enun: T("Divide ", "Divida ") + verRac(c.A, c.t === 3) + ENTRE + racR(c.Bdiv) + ".", pasos: pasosDiv(c)}; });
OMR("dq", function(){ var c = casoDiv(), sinVoltear = racMul(c.A, c.Bdiv), S2 = simplifica(sinVoltear.N, sinVoltear.D);
  return {enun: T("Choose the simplified quotient: ", "Seleccione el cociente simplificado: ") + verRac(c.A, c.t === 3) + ENTRE + racR(c.Bdiv) + ".", correcta: "ok", opciones: baraja(racOpciones([{clave: "ok", N: c.S.N, D: c.S.D}, {clave: "nv", N: S2.N, D: S2.D}].concat(malas(c.S)), 4)),
    porClave: Object.assign({nv: T("That is the product without flipping. To divide, flip the second fraction first.", "Ese es el producto sin voltear. Para dividir, primero voltee la segunda fracción.")}, PISTAS_RAC), pista: T("Keep the first fraction, change ÷ to ·, and flip the second.", "Deje la primera fracción, cambie ÷ por · y voltee la segunda."), bien: pasosDiv(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 3 · Same denominator ===== */
function casoIgual(op){
  op = op || elige(["+", "−", "−"]);
  var D = Math.random() < .3 ? Fm(1, 1, []) : Fm(1, 0, [X(nz(-8, 8))]), raiz = D.m ? 0 : -D.f[0][0], n1, n2, res;
  do { n1 = [aleatorio(-9, 9), aleatorio(1, 6)]; n2 = Math.random() < .5 ? [aleatorio(1, 9), 0] : [aleatorio(-9, 9), aleatorio(1, 5)]; n1 = pLimpia(n1); n2 = pLimpia(n2); res = op === "+" ? pSuma(n1, n2) : pResta(n1, n2); }
  while (pGrado(res) === 0 && !res[0] || Math.abs(pEval(res, raiz)) < 1e-9 || (res.length > 1 && res[0] && mcd(Math.abs(res[0]), Math.abs(res[1])) > 1 && !D.m) || (D.m && !res[0]));
  return {op: op, D: D, n1: n1, n2: n2, res: res};
}
function errorResta(c){ return pLimpia([(c.n1[0] || 0) + (c.n2[0] || 0), (c.n1[1] || 0) - (c.n2[1] || 0)]); }
function pasosIgual(c){
  var P = [T("The denominators are the same: keep ", "Los denominadores son iguales: se conserva ") + parteVis(c.D) + T(" and combine the numerators.", " y se combinan los numeradores.")];
  if (c.op === "+") P.push("(" + pVis(c.n1) + ") + (" + pVis(c.n2) + ") = " + pVis(c.res) + ".");
  else P.push(T("The minus sign goes to the whole second numerator: ", "El signo menos se reparte a todo el segundo numerador: ") + "(" + pVis(c.n1) + ") − (" + pVis(c.n2) + ") = " + pVis(c.n1) + " " + pVis(pEsc(c.n2, -1)).replace(/^−/, "− ").replace(/^(?=\d|x)/, "+ ") + " = " + pVis(c.res) + ".");
  P.push(T("Result: ", "Resultado: ") + "<strong>" + frPD(c.res, c.D) + "</strong>.");
  return P;
}
var IG = null;
function igNuevo(){ IG = casoIgual("−"); $("ig-enun").innerHTML = T("Subtract ", "Reste ") + frPD(IG.n1, IG.D) + envuelve(" − ", T(" minus ", " menos ")) + frPD(IG.n2, IG.D) + "."; $("ig-txt").innerHTML = ""; }
$("ig-bien").addEventListener("click", function(){ $("ig-txt").innerHTML = pasosIgual(IG).map(function(x){ return '<div class="linea">' + x + "</div>"; }).join(""); });
$("ig-error").addEventListener("click", function(){ var e = errorResta(IG);
  $("ig-txt").innerHTML = '<div class="linea"><strong style="color:#c62828">' + T("The common mistake:", "El error frecuente:") + "</strong> " + pVis(IG.n1) + " − " + pVis(IG.n2) + " = " + pVis(e) + T(" (only the first term was subtracted).", " (solo se restó el primer término).") + "</div>" +
    '<div class="linea">' + T("Check with x = 1: the right result gives ", "Compruebe con x = 1: el resultado correcto da ") + sg(pEval(IG.res, 1)) + T(" on top, the mistake gives ", " arriba, el error da ") + sg(pEval(e, 1)) + ". " + T("With parentheses: ", "Con paréntesis: ") + "(" + pVis(IG.n1) + ") − (" + pVis(IG.n2) + ") = " + pVis(IG.res) + ".</div>"; });
$("ig-otro").addEventListener("click", igNuevo); igNuevo();
OMR("iq", function(){ var c = casoIgual(), ops = [{clave: "ok", html: frPD(c.res, c.D)}, {clave: "dd", html: envuelve('<span class="fracc"><span class="fa">' + pVis(c.res) + '</span><span class="fb2">' + pVis(pEsc(fProducto(c.D), 2)) + "</span></span>", "")}, {clave: "d2", html: envuelve('<span class="fracc"><span class="fa">' + pVis(c.res) + '</span><span class="fb2">' + (c.D.m ? "x<sup>2</sup>" : "(" + pVis(c.D.f[0]) + ")<sup>2</sup>") + "</span></span>", "")}];
  if (c.op === "−" && pClave(errorResta(c)) !== pClave(c.res) && pGrado(errorResta(c)) >= 0 && (errorResta(c)[0] || errorResta(c)[1])) ops.push({clave: "par", html: frPD(errorResta(c), c.D)});
  else ops.push({clave: "sn", html: pVis(c.res)});
  var vis = {}; ops = ops.filter(function(o){ if (vis[o.html]) return false; vis[o.html] = 1; return true; });
  return {enun: (c.op === "+" ? T("Add ", "Sume ") : T("Subtract ", "Reste ")) + frPD(c.n1, c.D) + envuelve(" " + c.op + " ", c.op === "+" ? T(" plus ", " más ") : T(" minus ", " menos ")) + frPD(c.n2, c.D) + ".", correcta: "ok", opciones: baraja(ops),
    porClave: {dd: T("The denominator stays the same: denominators are not added.", "El denominador se conserva: los denominadores no se suman."), d2: T("The denominator stays the same, not squared.", "El denominador se conserva, sin elevarlo al cuadrado."), par: T("The minus sign goes to the whole second numerator: use parentheses.", "El signo menos se reparte a todo el segundo numerador: use paréntesis."), sn: T("The denominator does not disappear.", "El denominador no desaparece.")},
    pista: T("Same denominator: combine only the numerators.", "Mismo denominador: combine solo los numeradores."), bien: pasosIgual(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 4 · Different denominators ===== */
function cociente(L, D){ var f = L.f.slice(); D.f.forEach(function(q){ for (var i = 0; i < f.length; i++) if (pClave(f[i]) === pClave(q)){ f.splice(i, 1); break; } }); return Fm(L.k / D.k, L.m - D.m, f); }
function casoDist(){
  var t = aleatorio(0, 2), D1, D2, L, n1, n2, op = elige(["+", "+", "−"]), res, k = 0;
  do {
    if (t === 0){ var a = elige([1, 1, 2, 3]), b = elige([2, 3, 4, 6]), m1 = elige([1, 1, 2]), m2 = elige([1, 2]); if (a === b && m1 === m2) b = a * 2; D1 = Fm(a, m1, []); D2 = Fm(b, m2, []); var l = a * b / mcd(a, b); L = Fm(l, Math.max(m1, m2), []); }
    else if (t === 1){ var v = distintos(2, 6); D1 = Fm(1, 0, [X(v[0])]); D2 = Fm(1, 0, [X(v[1])]); L = Fm(1, 0, [X(v[0]), X(v[1])]); }
    else { var w = nz(-6, 6); D1 = Fm(1, 1, []); D2 = Fm(1, 0, [X(w)]); L = Fm(1, 1, [X(w)]); }
    n1 = [nz(1, 7)]; n2 = [nz(1, 7)];
    var q1 = fProducto(cociente(L, D1)), q2 = fProducto(cociente(L, D2)), t1 = pMul(n1, q1), t2 = pMul(n2, q2);
    res = op === "+" ? pSuma(t1, t2) : pResta(t1, t2); k++;
  } while ((excluidos(L).some(function(x){ return Math.abs(pEval(res, x)) < 1e-9; }) || (pGrado(res) === 0 && !res[0]) || (L.k > 1 && contenido(res) > 1 && mcd(contenido(res), L.k) > 1)) && k < 200);
  return {t: t, D1: D1, D2: D2, L: L, n1: n1, n2: n2, op: op, res: res, q1: cociente(L, D1), q2: cociente(L, D2), t1: t1, t2: t2};
}
function pasosDist(c){
  var P = [T("Least common denominator of ", "MCM de ") + parteVis(c.D1) + T(" and ", " y ") + parteVis(c.D2) + ": <strong>" + parteVis(c.L) + "</strong>."];
  P.push(T("Rewrite each fraction with the LCD: ", "Se reescribe cada fracción con el MCM: ") + envuelve(frPDvis(c.n1, c.D1) + " = " + frPDvis(c.t1, c.L) + "; " + frPDvis(c.n2, c.D2) + " = " + frPDvis(c.t2, c.L), "") + " " + T("(multiply the top and the bottom by what is missing: ", "(se multiplica arriba y abajo por lo que falta: ") + parteVis(c.q1) + T(" and ", " y ") + parteVis(c.q2) + ").");
  P.push(T("Combine the numerators: ", "Se combinan los numeradores: ") + "(" + pVis(c.t1) + ") " + c.op + " (" + pVis(c.t2) + ") = " + pVis(c.res) + ".");
  P.push(T("Result: ", "Resultado: ") + "<strong>" + frPD(c.res, c.L) + "</strong>.");
  return P;
}
pasoAPaso4("di", function(){ var c = casoDist(); return {enun: (c.op === "+" ? T("Add ", "Sume ") : T("Subtract ", "Reste ")) + frPD(c.n1, c.D1) + envuelve(" " + c.op + " ", c.op === "+" ? T(" plus ", " más ") : T(" minus ", " menos ")) + frPD(c.n2, c.D2) + ".", pasos: pasosDist(c)}; });
OMR("eq", function(){ var c = casoDist(), sumaD = pSuma(fProducto(c.D1), fProducto(c.D2)), sumaN = c.op === "+" ? pSuma(c.n1, c.n2) : pResta(c.n1, c.n2);
  var ops = [{clave: "ok", html: frPD(c.res, c.L)}, {clave: "nd", html: envuelve('<span class="fracc"><span class="fa">' + pVis(sumaN) + '</span><span class="fb2">' + pVis(sumaD) + "</span></span>", "")}, {clave: "nl", html: frPD(sumaN, c.L)}, {clave: "sg", html: frPD(c.op === "+" ? pResta(c.t1, c.t2) : pSuma(c.t1, c.t2), c.L)}];
  var vis = {}; ops = ops.filter(function(o){ if (vis[o.html] || /fa">0</.test(o.html)) return false; vis[o.html] = 1; return true; });
  return {enun: (c.op === "+" ? T("Add ", "Sume ") : T("Subtract ", "Reste ")) + frPD(c.n1, c.D1) + envuelve(" " + c.op + " ", c.op === "+" ? T(" plus ", " más ") : T(" minus ", " menos ")) + frPD(c.n2, c.D2) + ".", correcta: "ok", opciones: baraja(ops),
    porClave: {nd: T("Numerators and denominators are not added directly: find the LCD.", "No se suman numeradores y denominadores directamente: busque el MCM."), nl: T("The LCD is right, but each numerator must be multiplied by what its denominator is missing.", "El MCM está bien, pero cada numerador debe multiplicarse por lo que le falta a su denominador."), sg: T("Check the operation: " + (c.op === "+" ? "it is an addition." : "it is a subtraction."), "Revise la operación: " + (c.op === "+" ? "es una suma." : "es una resta."))},
    pista: T("Find the LCD, rewrite each fraction, and combine the numerators.", "Halle el MCM, reescriba cada fracción y combine los numeradores."), bien: pasosDist(c).join(" ").replace(/<\/?strong>/g, "")};
});
'''

def practica_pagina():
    n = N
    mods = [
     (t("multiply", "multiplicar"), t("Multiplying", "Multiplicar"),
      f'''      <p>{t("Factor, cancel any common factor (a top one with a bottom one, even across the two fractions), and multiply what is left. Cancelling before multiplying saves a lot of work.", "Se factoriza, se cancela cualquier factor común (de arriba con abajo, incluso en cruz entre las dos fracciones) y se multiplica lo que queda. Cancelar antes de multiplicar ahorra mucho trabajo.")}</p>
{n4.pasos("mu", t("Another product", "Otro producto"))}
{B.om("mq", t("Practice: choose the simplified product", "Practique: elija el producto simplificado"))}'''),
     (t("divide", "dividir"), t("Dividing", "Dividir"),
      f'''{n4.formula("a/b ÷ c/d = a/b · d/c")}
      <p>{t("Dividing is multiplying by the reciprocal: keep the first fraction, change ÷ to ·, and flip the second. Then it is a multiplication.", "Dividir es multiplicar por el recíproco: se deja la primera fracción, se cambia ÷ por · y se voltea la segunda. A partir de ahí es una multiplicación.")}</p>
{n4.pasos("dv", t("Another quotient", "Otro cociente"))}
{B.om("dq", t("Practice: choose the simplified quotient", "Practique: elija el cociente simplificado"))}'''),
     (t("same", "sumar-igual"), t("Adding and subtracting with the same denominator", "Sumar y restar con igual denominador"),
      f'''      <p>{t("When the denominators are the same, combine the numerators and keep the denominator. In a subtraction, the minus sign goes to the whole second numerator.", "Cuando los denominadores son iguales, se combinan los numeradores y se conserva el denominador. En una resta, el signo menos se reparte a todo el segundo numerador.")}</p>
      <div class="panel"><p class="enun" id="ig-enun"></p>
        <div class="fila-btn"><button type="button" class="btn" id="ig-bien">{t("See it done right", "Ver la resolución correcta")}</button><button type="button" class="btn-sec" id="ig-error">{t("See the common mistake", "Ver el error frecuente")}</button><button type="button" class="btn-sec" id="ig-otro">{t("Another subtraction", "Otra resta")}</button></div></div>
{n4.salida("ig-txt")}
{B.om("iq", t("Practice: add or subtract", "Practique: sume o reste"))}'''),
     (t("different", "sumar-distinto"), t("Adding and subtracting with different denominators", "Sumar y restar con denominadores diferentes"),
      f'''      <p>{t("Find the least common denominator (LCD), rewrite each fraction with it, and combine the numerators: the same process as 1/2 + 1/3 = 3/6 + 2/6 = 5/6.", "Se busca el mínimo común múltiplo (MCM) de los denominadores, se reescribe cada fracción con él y se combinan los numeradores: el mismo proceso que 1/2 + 1/3 = 3/6 + 2/6 = 5/6.")}</p>
{n4.pasos("di", t("Another sum or difference", "Otra suma o resta"))}
      <div class="caja-tip">{t("The LCD of numbers and powers of x: the LCM of the numbers and the highest power of x (for x and 2x², it is 2x²). The LCD of two different binomials is their product.", "El MCM de números y potencias de x: el MCM de los números y la mayor potencia de x (para x y 2x², es 2x²). El MCM de dos binomios distintos es su producto.")}</div>
{B.om("eq", t("Practice: choose the result", "Practique: elija el resultado"))}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Sumar, restar, multiplicar y dividir expresiones racionales")
