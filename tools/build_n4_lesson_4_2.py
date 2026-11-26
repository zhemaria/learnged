"""Level 4 · Lesson 4.2 · Completing the square — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_4-2.html and algebra/n4-l4-2.html (the area model, the five steps, dividing by a first,
how much to add, and the origin of the quadratic formula). They are rebuilt here, inside LearnGED.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "4-2"
TEMA = ("Quadratic equations", "Ecuaciones cuadráticas")
TIT = ("Completing the square", "Completar el cuadrado")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def area_svg(etiqueta):
    """Static area model of x² + 6x + 9 = (x + 3)²."""
    x0, y0, X, h = 60, 30, 170, 85
    return B.svg("0 0 420 330", etiqueta,
        f'<rect x="{x0}" y="{y0}" width="{X}" height="{X}" fill="#e3f2fd" stroke="#0d47a1" stroke-width="2.5"/>'
        f'<rect x="{x0 + X}" y="{y0}" width="{h}" height="{X}" fill="#e8f5e9" stroke="#1b5e20" stroke-width="2.5"/>'
        f'<rect x="{x0}" y="{y0 + X}" width="{X}" height="{h}" fill="#e8f5e9" stroke="#1b5e20" stroke-width="2.5"/>'
        f'<rect x="{x0 + X}" y="{y0 + X}" width="{h}" height="{h}" fill="#fff3e0" stroke="#e65100" stroke-width="2.5" stroke-dasharray="7 5"/>'
        f'<text x="{x0 + X / 2}" y="{y0 + X / 2 + 9}" font-size="26" font-weight="700" text-anchor="middle" fill="#0d47a1">x²</text>'
        f'<text x="{x0 + X + h / 2}" y="{y0 + X / 2 + 8}" font-size="22" font-weight="700" text-anchor="middle" fill="#1b5e20">3x</text>'
        f'<text x="{x0 + X / 2}" y="{y0 + X + h / 2 + 8}" font-size="22" font-weight="700" text-anchor="middle" fill="#1b5e20">3x</text>'
        f'<text x="{x0 + X + h / 2}" y="{y0 + X + h / 2 + 8}" font-size="24" font-weight="700" text-anchor="middle" fill="#e65100">9</text>'
        f'<text x="{x0 + X / 2}" y="{y0 - 8}" font-size="17" text-anchor="middle" fill="#37474f">x</text><text x="{x0 + X + h / 2}" y="{y0 - 8}" font-size="17" text-anchor="middle" fill="#37474f">3</text>'
        f'<text x="{x0 - 10}" y="{y0 + X / 2 + 6}" font-size="17" text-anchor="end" fill="#37474f">x</text><text x="{x0 - 10}" y="{y0 + X + h / 2 + 6}" font-size="17" text-anchor="end" fill="#37474f">3</text>', 380)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 4.1.</strong> In Lesson 4.1 you solved quadratic equations by factoring. But some equations do not factor with whole numbers. <strong>Completing the square</strong> is a method that always works, whether the equation factors or not, and it is also where the quadratic formula comes from.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 4.1 se resolvieron ecuaciones cuadráticas por factorización. Pero hay ecuaciones que no se factorizan con números enteros. <strong>Completar el cuadrado</strong> es un método que funciona siempre, factorice o no la ecuación, y además es la base de la fórmula cuadrática.")}</p>
<p>{t("The expression x² + 6x can be drawn as a square with side x plus a rectangle of area 6x. If you cut that rectangle in half and place one half on each side of the square, only a small corner is missing to make a big square. That corner is (6/2)² = 9.", "La expresión x² + 6x se puede representar como un cuadrado de lado x más un rectángulo de área 6x. Si ese rectángulo se parte por la mitad y se coloca una mitad a cada lado, falta un pedacito cuadrado para «completar» un cuadrado grande. Ese pedacito es (6/2)² = 9.")}</p>
{area_svg(t("Area model: a square x by x, two rectangles 3 by x of area 3x each, and the missing corner 3 by 3 of area 9. Together they form a square with side x + 3.", "Modelo del área: un cuadrado de x por x, dos rectángulos de 3 por x de área 3x cada uno y la esquina que falta, de 3 por 3 y área 9. Juntos forman un cuadrado de lado x + 3."))}
<p class="formula" style="text-align:center;font-size:1.25rem;font-weight:700;">x² + 6x + 9 = (x + 3)²</p>
<p>{t("Adding that missing term turns x² + 6x + 9 into the perfect square (x + 3)². That is the central idea: add just the right term to form a binomial squared.", "Al sumar ese término que falta, x² + 6x + 9 se convierte en el cuadrado perfecto (x + 3)². Esa es la idea central: agregar el término justo para formar un binomio al cuadrado.")}</p>
{enlace(n, "visual", t("the area model", "el modelo del área"), t("Change b and complete the missing corner to see x² + bx become a binomial squared.", "Cambie el valor de b y complete la esquina que falta para ver cómo x² + bx se convierte en un binomio al cuadrado."))}'''

    s2 = f'''{tabla(t("The five steps", "Los cinco pasos"), t("The five steps to solve a quadratic equation by completing the square", "Los cinco pasos para resolver una ecuación cuadrática completando el cuadrado"), [t("Step", "Paso"), t("What to do", "Acción")],
  [["1", t("Leave the terms with x on one side: x² + bx = −c.", "Dejar los términos con x a un lado: x² + bx = −c.")], ["2", t("Add (b/2)² to both sides.", "Sumar (b/2)² a ambos lados.")], ["3", t("Write the left side as (x + b/2)².", "Escribir el lado izquierdo como (x + b/2)².")], ["4", t("Take the square root of both sides, with ±.", "Sacar la raíz cuadrada de ambos lados, con ±.")], ["5", t("Solve for x.", "Resolver para x.")]])}
{ejemplo(t("Example 1: solve x² + 6x − 7 = 0.", "Ejemplo 1 · Resolver x² + 6x − 7 = 0."),
  [("1", "x² + 6x = 7.", ""), ("2", t("(6/2)² = 9. Add 9 to both sides:", "(6/2)² = 9. Se suma 9 a ambos lados:"), "x² + 6x + 9 = 16."), ("3", "(x + 3)² = 16.", ""), ("4", "x + 3 = ±4.", ""), ("5", t("x = −3 + 4 = 1 or x = −3 − 4 = −7.", "x = −3 + 4 = 1 o x = −3 − 4 = −7."), ""),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = 1 and x = −7</strong>.", "<strong>x = 1 y x = −7</strong>."))])}
{ejemplo(t("Example 2: solve x² − 4x − 5 = 0.", "Ejemplo 2 · Resolver x² − 4x − 5 = 0."),
  [("1", "x² − 4x = 5.", ""), ("2", t("(−4/2)² = 4. Add 4:", "(−4/2)² = 4. Se suma 4:"), "x² − 4x + 4 = 9."), ("3", "(x − 2)² = 9.", ""), ("4", "x − 2 = ±3.", ""), ("5", t("x = 5 or x = −1.", "x = 5 o x = −1."), ""),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = 5 and x = −1</strong>.", "<strong>x = 5 y x = −1</strong>."))])}
{caja("ojo", t("Do not forget the ± sign", "No olvide el signo ±"), t("<p>When you take the square root of both sides, there are two results, the positive one and the negative one. Leaving out the ± loses one of the two solutions.</p>", "<p>Al sacar la raíz cuadrada de ambos lados aparecen dos resultados, el positivo y el negativo. Omitir el signo ± hace perder una de las dos soluciones.</p>"))}
{practica("p1", t("Practice 1 — x² + 4x − 5 = 0", "Práctica 1 — x² + 4x − 5 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = −1 and x = 5", "x = −1 y x = 5")), ("b", t("x = 1 and x = 5", "x = 1 y x = 5")), ("c", t("x = 1 and x = −5", "x = 1 y x = −5"))])}
{practica("p2", t("Practice 2 — x² − 2x − 8 = 0", "Práctica 2 — x² − 2x − 8 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = 4 and x = −2", "x = 4 y x = −2")), ("b", t("x = −4 and x = 2", "x = −4 y x = 2")), ("c", t("x = 4 and x = 2", "x = 4 y x = 2"))])}
{practica("p3", t("Practice 3 — x² + 6x + 5 = 0", "Práctica 3 — x² + 6x + 5 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = 1 and x = 5", "x = 1 y x = 5")), ("b", t("x = −1 and x = −5", "x = −1 y x = −5")), ("c", t("x = −1 and x = 5", "x = −1 y x = 5"))])}
{enlace(n, t("steps", "pasos"), t("the five steps", "los cinco pasos"), t("Follow a case step by step, then solve on your own with two tries and the full solution.", "Siga un caso paso a paso y después resuelva por su cuenta, con dos intentos y la solución completa."))}'''

    s3 = f'''<p>{t("The five steps assume the coefficient of x² is 1. If it is not, the first move is to divide the whole equation by a.", "El método de los cinco pasos asume que el coeficiente de x² es 1. Si no lo es, el primer movimiento es dividir toda la ecuación entre a.")}</p>
{ejemplo(t("Example 3: solve 2x² + 8x − 10 = 0.", "Ejemplo 3 · Resolver 2x² + 8x − 10 = 0."),
  [("1", t("Divide everything by 2:", "Se divide todo entre 2:"), "x² + 4x − 5 = 0."), ("2", "x² + 4x = 5.", ""), ("3", t("(4/2)² = 4. Add 4:", "(4/2)² = 4. Se suma 4:"), "(x + 2)² = 9."), ("4", "x + 2 = ±3.", ""), ("5", t("x = 1 or x = −5.", "x = 1 o x = −5."), ""),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = 1 and x = −5</strong>.", "<strong>x = 1 y x = −5</strong>."))])}
{caja("tip", t("Divide the whole equation", "Divida la ecuación completa"), t("<p>When you divide by a, divide every term, including the constant. Then the coefficient of x² is 1 and the five steps work just as before.</p>", "<p>Al dividir entre a, se dividen todos los términos, incluido el término independiente. Así el coeficiente de x² queda en 1 y los cinco pasos funcionan tal cual.</p>"))}
{enlace(n, t("divide", "dividir"), t("dividing by a first", "dividir primero entre a"), t("Divide the equation by a before you complete the square, and check that all three terms are divided.", "Divida la ecuación entre a antes de completar el cuadrado y compruebe que se dividen los tres términos."))}'''

    s4 = f'''<p>{t("The heart of the method is (b/2)²: half the coefficient of x, squared. It is worth practicing by itself:", "El corazón del método es calcular (b/2)²: la mitad del coeficiente de x, elevada al cuadrado. Conviene practicarlo por separado:")}</p>
{tabla(t("The term that completes the square", "El término que completa el cuadrado"), t("Examples of the term that completes the square for each coefficient of x", "Ejemplos del término que completa el cuadrado según el coeficiente de x"), [t("Expression", "Expresión"), "b/2", t("Add (b/2)²", "Se suma (b/2)²")],
  [["x² + 8x", "4", "16"], ["x² − 10x", "−5", "25"], ["x² + 12x", "6", "36"], ["x² − 6x", "−3", "9"], ["x² + 5x", "5/2", "25/4"]])}
{caja("tip", t("Always positive", "Siempre positivo"), t("<p>Even when b is negative, (b/2)² is positive: (−5)² = 25. When b is odd, the result is a fraction: (5/2)² = 25/4.</p>", "<p>Aunque b sea negativo, (b/2)² es positivo: (−5)² = 25. Cuando b es impar, el resultado es una fracción: (5/2)² = 25/4.</p>"))}
{practica("p4", t("Practice 4 — x² + 12x", "Práctica 4 — x² + 12x"), t("Which term completes the square?", "¿Qué término completa el cuadrado?"), [("a", "24"), ("b", "144"), ("c", "36")])}
{practica("p5", t("Practice 5 — x² − 6x", "Práctica 5 — x² − 6x"), t("Which term completes the square?", "¿Qué término completa el cuadrado?"), [("a", "3"), ("b", "9"), ("c", "36")])}
{practica("p6", t("Practice 6 — x² + 5x", "Práctica 6 — x² + 5x"), t("Which term completes the square?", "¿Qué término completa el cuadrado?"), [("a", "25/4"), ("b", "5/2"), ("c", "25")])}
{enlace(n, t("add", "sumar"), t("how much to add", "cuánto hay que sumar"), t("Find (b/2)² for any b, also when b is odd and the result is a fraction.", "Calcule (b/2)² para cualquier b, también cuando b es impar y el resultado es una fracción."))}'''

    pasos_d = [("1", t("Divide everything by a:", "Se divide todo entre a:"), "x² + (b/a)x + c/a = 0."),
               ("2", t("Move the constant to the other side:", "Se pasa la constante al otro lado:"), "x² + (b/a)x = −c/a."),
               ("3", t("Add half the coefficient of x, squared, to both sides: (b/2a)² = b²/4a².", "Se suma la mitad del coeficiente de x, al cuadrado, en ambos lados: (b/2a)² = b²/4a²."), "x² + (b/a)x + b²/4a² = b²/4a² − c/a."),
               ("4", t("The left side is a perfect square; write the right side with a common denominator:", "El lado izquierdo es un cuadrado perfecto, y el derecho se escribe con denominador común:"), "(x + b/2a)² = (b² − 4ac)/4a²."),
               ("5", t("Take the square root, without forgetting ±:", "Se saca raíz cuadrada sin olvidar el ±:"), "x + b/2a = ±√(b² − 4ac) / 2a."),
               ("6", t("Subtract b/2a to get x alone:", "Se despeja x restando b/2a:"), "x = (−b ± √(b² − 4ac)) / 2a."),
               ("✓", t("Result:", "Resultado:"), t("the quadratic formula, the same one on the GED formula sheet.", "la fórmula cuadrática, la misma que aparece en la hoja de fórmulas del GED."))]
    s5 = f'''<p>{t("If you complete the square in the general equation ax² + bx + c = 0 (no numbers, only letters), the result is exactly the quadratic formula:", "Si se completa el cuadrado en la ecuación general ax² + bx + c = 0 (sin números, solo letras), el resultado es exactamente la fórmula cuadrática:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">x = (−b ± √(b² − 4ac)) / 2a</p>
<p>{t("That is why this method matters so much: it is not an isolated trick, it is the proof of where the formula of Lesson 4.3 comes from.", "Por eso este método es tan importante: no es un truco aislado, sino la demostración de dónde proviene la fórmula que se usará en la Lección 4.3 para resolver cualquier ecuación cuadrática.")}</p>
{ejemplo(t("The derivation, step by step (the same steps as in section 3, with letters)", "La derivación, paso a paso (los mismos pasos de la sección 3, con letras)"), pasos_d)}
{enlace(n, t("origin", "origen"), t("the origin of the quadratic formula", "el origen de la fórmula cuadrática"), t("Follow the derivation with letters and with numbers, and answer questions about each step.", "Siga la derivación con letras y con números, y responda preguntas sobre cada paso."))}'''

    secciones = [("s-visual", t("The visual idea: completing a square", "La idea visual: completar un cuadrado"), s1),
                 ("s-" + t("steps", "pasos"), t("The five steps (when a = 1)", "Los cinco pasos (cuando a = 1)"), s2),
                 ("s-" + t("divide", "dividir"), t("When a ≠ 1: divide first", "Cuando a ≠ 1: dividir primero"), s3),
                 ("s-" + t("add", "sumar"), t("How much do you add?", "¿Cuánto hay que sumar?"), s4),
                 ("s-" + t("origin", "origen"), t("The origin of the quadratic formula", "El origen de la fórmula cuadrática"), s5)]

    lesson = {"next": t("Lesson 4.3", "Lección 4.3"), "review": t("sections 2 and 4", "las secciones 2 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("(x + 2)² = 9 gives x + 2 = 3 or x + 2 = −3.", "(x + 2)² = 9 da x + 2 = 3 o x + 2 = −3."), "b": t("Substitute x = 5: 25 + 20 − 5 is not 0.", "Sustituya x = 5: 25 + 20 − 5 no es 0.")}, "right": t("(x + 2)² = 9, x + 2 = ±3.", "(x + 2)² = 9, x + 2 = ±3."), "solution": t("x = 1 and x = −5.", "x = 1 y x = −5.")},
      "p2": {"ok": "a", "hints": {"b": t("(x − 1)² = 9 gives x − 1 = ±3, so x = 1 ± 3.", "(x − 1)² = 9 da x − 1 = ±3, así que x = 1 ± 3."), "c": t("Substitute x = 2: 4 − 4 − 8 is not 0.", "Sustituya x = 2: 4 − 4 − 8 no es 0.")}, "right": t("(x − 1)² = 9, x − 1 = ±3.", "(x − 1)² = 9, x − 1 = ±3."), "solution": t("x = 4 and x = −2.", "x = 4 y x = −2.")},
      "p3": {"ok": "b", "hints": {"a": t("(x + 3)² = 4 gives x = −3 ± 2.", "(x + 3)² = 4 da x = −3 ± 2."), "c": t("Substitute x = 5: 25 + 30 + 5 is not 0.", "Sustituya x = 5: 25 + 30 + 5 no es 0.")}, "right": t("(x + 3)² = 4, x + 3 = ±2.", "(x + 3)² = 4, x + 3 = ±2."), "solution": t("x = −1 and x = −5.", "x = −1 y x = −5.")},
      "p4": {"ok": "c", "hints": {"a": t("24 is 2 · 12. Take half of 12, then square it.", "24 es 2 · 12. Saque la mitad de 12 y elévela al cuadrado."), "b": t("144 is 12². First take half of 12.", "144 es 12². Primero saque la mitad de 12.")}, "right": t("12 ÷ 2 = 6 and 6² = 36.", "12 ÷ 2 = 6 y 6² = 36."), "solution": "36."},
      "p5": {"ok": "b", "hints": {"a": t("3 is half of 6. Now square it.", "3 es la mitad de 6. Ahora elévelo al cuadrado."), "c": t("36 is 6². First take half of 6.", "36 es 6². Primero saque la mitad de 6.")}, "right": t("−6 ÷ 2 = −3 and (−3)² = 9.", "−6 ÷ 2 = −3 y (−3)² = 9."), "solution": "9."},
      "p6": {"ok": "a", "hints": {"b": t("5/2 is half of 5. Now square it.", "5/2 es la mitad de 5. Ahora elévelo al cuadrado."), "c": t("25 is 5². First take half of 5.", "25 es 5². Primero saque la mitad de 5.")}, "right": t("(5/2)² = 25/4.", "(5/2)² = 25/4."), "solution": "25/4."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("8 is b. Take half, then square.", "8 es b. Saque la mitad y elévela al cuadrado."), "c": t("64 is 8². First take half of 8.", "64 es 8². Primero saque la mitad de 8."), "d": t("4 is half of 8. Now square it.", "4 es la mitad de 8. Ahora elévelo al cuadrado.")}, "solution": "16."},
      "B": {"ok": "c", "hints": {"a": t("100 is 10². First take half of 10.", "100 es 10². Primero saque la mitad de 10."), "b": t("10 is b. Take half, then square.", "10 es b. Saque la mitad y elévela al cuadrado."), "d": t("5 is half of 10. Now square it.", "5 es la mitad de 10. Ahora elévelo al cuadrado.")}, "solution": "25."},
      "C": {"ok": "a", "hints": {"b": t("(x + 3)² = 16 gives x = −3 ± 4.", "(x + 3)² = 16 da x = −3 ± 4."), "c": t("Substitute x = 7: 49 + 42 − 7 is not 0.", "Sustituya x = 7: 49 + 42 − 7 no es 0."), "d": t("Substitute x = −1: 1 − 6 − 7 is not 0.", "Sustituya x = −1: 1 − 6 − 7 no es 0.")}, "solution": t("x = 1 and x = −7.", "x = 1 y x = −7.")},
      "D": {"ok": "d", "hints": {"a": t("(x − 2)² = 9 gives x = 2 ± 3.", "(x − 2)² = 9 da x = 2 ± 3."), "b": t("Substitute x = 1: 1 − 4 − 5 is not 0.", "Sustituya x = 1: 1 − 4 − 5 no es 0."), "c": t("(x − 2)² = 9 gives x = 2 ± 3.", "(x − 2)² = 9 da x = 2 ± 3.")}, "solution": t("x = 5 and x = −1.", "x = 5 y x = −1.")},
      "E": {"ok": "c", "hints": {"a": t("(x + 1)² = 4 gives x = −1 ± 2.", "(x + 1)² = 4 da x = −1 ± 2."), "b": t("Substitute x = 3: 9 + 6 − 3 is not 0.", "Sustituya x = 3: 9 + 6 − 3 no es 0."), "d": t("Substitute x = −1: 1 − 2 − 3 is not 0.", "Sustituya x = −1: 1 − 2 − 3 no es 0.")}, "solution": t("x = 1 and x = −3.", "x = 1 y x = −3.")},
      "F": {"ok": "d", "hints": {"a": t("(x − 4)² = 4 gives x = 4 ± 2.", "(x − 4)² = 4 da x = 4 ± 2."), "b": t("(x − 4)² = 4 gives x = 4 ± 2.", "(x − 4)² = 4 da x = 4 ± 2."), "c": t("(x − 4)² = 4 gives x = 4 ± 2.", "(x − 4)² = 4 da x = 4 ± 2.")}, "solution": t("x = 6 and x = 2.", "x = 6 y x = 2.")},
      "G": {"ok": "b", "hints": {"a": t("Divide by 2: x² + 4x − 5 = 0, then (x + 2)² = 9.", "Divida entre 2: x² + 4x − 5 = 0, y después (x + 2)² = 9."), "c": t("Divide the whole equation by 2 first.", "Primero divida toda la ecuación entre 2."), "d": t("Substitute x = 5: 50 + 40 − 10 is not 0.", "Sustituya x = 5: 50 + 40 − 10 no es 0.")}, "solution": t("x = 1 and x = −5.", "x = 1 y x = −5.")},
      "H": {"ok": "a", "hints": {"b": t("The coefficient of x² must be 1 first.", "Primero el coeficiente de x² tiene que ser 1."), "c": t("Moving 15 comes later; first make the coefficient of x² equal 1.", "Pasar el 15 viene después; primero el coeficiente de x² debe ser 1."), "d": t("Multiplying makes the coefficient of x² bigger, not 1.", "Multiplicar hace más grande el coeficiente de x², no 1.")}, "solution": t("Divide everything by 3.", "Dividir todo entre 3.")},
     }}

    quiz = [
     ("A", t("What do you add to complete the square of x² + 8x?", "¿Qué se suma para completar el cuadrado de x² + 8x?"), [("a", "8"), ("b", "16"), ("c", "64"), ("d", "4")]),
     ("B", t("What do you add to complete the square of x² − 10x?", "¿Qué se suma para completar el cuadrado de x² − 10x?"), [("a", "100"), ("b", "10"), ("c", "25"), ("d", "5")]),
     ("C", t("Solve x² + 6x − 7 = 0.", "Resuelva x² + 6x − 7 = 0."), [("a", t("x = 1 and x = −7", "x = 1 y x = −7")), ("b", t("x = −1 and x = 7", "x = −1 y x = 7")), ("c", t("x = 1 and x = 7", "x = 1 y x = 7")), ("d", t("x = −1 and x = −7", "x = −1 y x = −7"))]),
     ("D", t("Solve x² − 4x − 5 = 0.", "Resuelva x² − 4x − 5 = 0."), [("a", t("x = −5 and x = 1", "x = −5 y x = 1")), ("b", t("x = 5 and x = 1", "x = 5 y x = 1")), ("c", t("x = −5 and x = −1", "x = −5 y x = −1")), ("d", t("x = 5 and x = −1", "x = 5 y x = −1"))]),
     ("E", t("Solve x² + 2x − 3 = 0.", "Resuelva x² + 2x − 3 = 0."), [("a", t("x = −1 and x = 3", "x = −1 y x = 3")), ("b", t("x = 1 and x = 3", "x = 1 y x = 3")), ("c", t("x = 1 and x = −3", "x = 1 y x = −3")), ("d", t("x = −1 and x = −3", "x = −1 y x = −3"))]),
     ("F", t("Solve x² − 8x + 12 = 0.", "Resuelva x² − 8x + 12 = 0."), [("a", t("x = −6 and x = −2", "x = −6 y x = −2")), ("b", t("x = 6 and x = −2", "x = 6 y x = −2")), ("c", t("x = −6 and x = 2", "x = −6 y x = 2")), ("d", t("x = 6 and x = 2", "x = 6 y x = 2"))]),
     ("G", t("Solve 2x² + 8x − 10 = 0.", "Resuelva 2x² + 8x − 10 = 0."), [("a", t("x = −1 and x = 5", "x = −1 y x = 5")), ("b", t("x = 1 and x = −5", "x = 1 y x = −5")), ("c", t("x = 2 and x = −10", "x = 2 y x = −10")), ("d", t("x = 1 and x = 5", "x = 1 y x = 5"))]),
     ("H", t("To solve 3x² + 12x − 15 = 0 by completing the square, what is the first step?", "Para resolver 3x² + 12x − 15 = 0 completando el cuadrado, ¿cuál es el primer paso?"), [("a", t("Divide everything by 3", "Dividir todo entre 3")), ("b", t("Add 12", "Sumar 12")), ("c", t("Subtract 15", "Restar 15")), ("d", t("Multiply by 3", "Multiplicar por 3"))])]

    tarea = (t("For your own work, with your notebook open: (1) From the picture to the method: solve x² + 6x = 7 and x² + 4x = 12 by drawing the area model. Then use the five steps on x² + 8x + 7 = 0, x² − 10x + 16 = 0, x² + 2x − 8 = 0, x² − 6x − 3 = 0, 2x² + 8x − 10 = 0, and 3x² − 12x + 6 = 0. In each one, write down the term (b/2)² that completes the square. (2) The derivation: after you study the six steps of section 5, close the lesson and complete the square yourself in ax² + bx + c = 0 until you reach the quadratic formula. Compare your result with the GED formula sheet. (3) I do not lose solutions: in each solution below, the ± was forgotten. Find the missing solution and write both: (x + 2)² = 9 → x = 1; (x − 4)² = 25 → x = 9; (x + 1)² = 7 → x = −1 + √7. Then do several exercises of each activity on the practice page, solving them in your notebook first, and write down the ones you miss to review them. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) De la figura al algoritmo: resuelva x² + 6x = 7 y x² + 4x = 12 dibujando el modelo del área. Luego aplique los cinco pasos a x² + 8x + 7 = 0, x² − 10x + 16 = 0, x² + 2x − 8 = 0, x² − 6x − 3 = 0, 2x² + 8x − 10 = 0 y 3x² − 12x + 6 = 0. En cada una, anote cuál es el término (b/2)² que completa el cuadrado. (2) La derivación: después de estudiar los seis pasos de la sección 5, cierre la lección y complete usted el cuadrado en ax² + bx + c = 0 hasta llegar a la fórmula cuadrática. Compare su resultado con la hoja de fórmulas del GED. (3) No pierdo soluciones: en cada resolución se olvidó el signo ±. Encuentre la solución que falta y escriba las dos: (x + 2)² = 9 → x = 1; (x − 4)² = 25 → x = 9; (x + 1)² = 7 → x = −1 + √7. Después haga varios ejercicios de cada actividad de la página de práctica, resolviéndolos primero en el cuaderno, y anote los que falle para repasarlos. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Cut a square of paper and two equal strips, as in the area model. Show someone at home how the missing corner “completes” the square, and ask them to find the corner for x² + 10x.",
               "Recorte un cuadrado de papel y dos tiras iguales, como en el modelo del área. Muéstrele a alguien en casa cómo la esquina que falta «completa» el cuadrado y pídale que halle la esquina de x² + 10x."))

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Complete the square to solve any quadratic equation: add (b/2)², write a binomial squared, and take the square root with ±.", "Complete el cuadrado para resolver cualquier ecuación cuadrática: sume (b/2)², escriba un binomio al cuadrado y saque la raíz con ±."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Explain</strong> completing the square with the area model.", "<strong>Explicar</strong> la idea de completar el cuadrado con el modelo del área."),
         t("<strong>Solve</strong> quadratic equations by completing the square with five steps.", "<strong>Resolver</strong> ecuaciones cuadráticas completando el cuadrado con cinco pasos."),
         t("<strong>Divide</strong> by a first when the coefficient of x² is not 1, and find (b/2)², even as a fraction.", "<strong>Dividir</strong> primero entre a cuando el coeficiente de x² no es 1, y calcular (b/2)², incluso como fracción."),
         t("<strong>Follow</strong> how completing the square leads to the quadratic formula.", "<strong>Seguir</strong> cómo completar el cuadrado conduce a la fórmula cuadrática.")],
        secciones, tarea, quiz,
        t("Self-check checklist for completing the square", "Lista de autoevaluación de completar el cuadrado"),
        t("Self-check checklist: skills for completing the square", "Lista de autoevaluación: destrezas de completar el cuadrado"),
        [(t("Finding (b/2)²", "Calcular (b/2)²"), t("I find (b/2)² easily, even with fractions.", "Calculo (b/2)² con fluidez, incluso con fracciones."), t("I find b/2 but forget to square it.", "Calculo b/2, pero no lo elevo al cuadrado."), t("I do not find the term that completes the square.", "No calculo el término que completa el cuadrado.")),
         (t("Keeping the equation balanced", "Mantener la igualdad"), t("I add (b/2)² to both sides and write (x + b/2)² correctly.", "Sumo (b/2)² a ambos lados y escribo (x + b/2)² correctamente."), t("I add to both sides, but make arithmetic mistakes.", "Sumo a ambos lados, pero con errores aritméticos."), t("I add the term to only one side.", "Sumo el término a un solo lado.")),
         (t("Square root with ±", "Raíz con ±"), t("I take the root with ± and get both solutions, also when a ≠ 1.", "Saco la raíz con ± y obtengo ambas soluciones, también con a ≠ 1."), t("I take the root but lose a solution.", "Saco la raíz, pero pierdo una solución."), t("I do not take the root or I ignore the ±.", "No saco la raíz o ignoro el signo ±."))],
        t("<p>In this lesson you learned to <strong>complete the square</strong>: a method that always works, adding (b/2)² to form a binomial squared and taking the root with ±. You also saw that this process, used on the general equation, produces the quadratic formula.</p>\n<p>In <strong>Lesson 4.3 · The quadratic formula, the discriminant, and applications</strong> you will use that formula to solve any quadratic equation directly, predict the number of solutions with the discriminant, and model real situations such as the path of a ball.</p>",
          "<p>En esta lección se aprendió a <strong>completar el cuadrado</strong>: un método que funciona siempre, sumando (b/2)² para formar un binomio al cuadrado y sacando la raíz con el signo ±. También se vio que este procedimiento, aplicado a la ecuación general, produce la fórmula cuadrática.</p>\n<p>En la <strong>Lección 4.3 · La fórmula cuadrática, el discriminante y aplicaciones</strong> se usará esa fórmula para resolver cualquier ecuación cuadrática de forma directa, se aprenderá a predecir el número de soluciones con el discriminante y se modelarán situaciones reales como la trayectoria de un proyectil.</p>"),
        ("4-3", ("", t("Lesson 4.3 · The quadratic formula, the discriminant, and applications", "Lección 4.3 · La fórmula cuadrática, el discriminante y aplicaciones"))),
        [(t("completing the square", "completar el cuadrado"), t("Adding (b/2)² to x² + bx to make a binomial squared.", "Sumar (b/2)² a x² + bx para formar un binomio al cuadrado.")),
         (t("perfect square trinomial", "trinomio cuadrado perfecto"), "x² + bx + (b/2)² = (x + b/2)²"),
         ("±", t("“Plus or minus”: a number and its opposite, the two square roots.", "«Más o menos»: un número y su opuesto, las dos raíces cuadradas.")),
         (t("quadratic formula", "fórmula cuadrática"), "x = (−b ± √(b² − 4ac)) / 2a")],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
var O = T(" or ", " o ");
var SOL_AYUDA = T("Type both solutions separated by a comma, like: −2, 3.", "Escriba las dos soluciones separadas por una coma, como: −2, 3.");
function xmas(h){ return "x" + (h < 0 ? " − " + Math.abs(h) : h > 0 ? " + " + h : ""); }
function cuadTxt(h){ return "(" + xmas(h) + ")²"; }
function eqV(p, d){ return pVis(p) + " = " + (d === undefined ? "0" : sg(d)); }
function eqH(p, d){ return envuelve(eqV(p, d), pVoz(p) + T(" equals ", " es igual a ") + (d === undefined ? "0" : sg(d))); }

/* ===== MODULE 1 · The area model ===== */
function viDibuja(){
  var b = +$("vi-b").value, h = b / 2, k = h * h, X = 150, u = 16, w = Math.abs(h) * u, x0 = 70, y0 = 40, lleno = $("vi-esq").getAttribute("aria-pressed") === "true";
  $("vi-bv").textContent = sg(b);
  var hv = frTxt(b, 2), kv = frTxt(b * b, 4), s = "";
  s += '<rect x="' + x0 + '" y="' + y0 + '" width="' + X + '" height="' + X + '" fill="#e3f2fd" stroke="#0d47a1" stroke-width="2.5"/>';
  s += '<rect x="' + (x0 + X) + '" y="' + y0 + '" width="' + w + '" height="' + X + '" fill="#e8f5e9" stroke="#1b5e20" stroke-width="2.5"/>';
  s += '<rect x="' + x0 + '" y="' + (y0 + X) + '" width="' + X + '" height="' + w + '" fill="#e8f5e9" stroke="#1b5e20" stroke-width="2.5"/>';
  s += '<rect x="' + (x0 + X) + '" y="' + (y0 + X) + '" width="' + w + '" height="' + w + '" fill="' + (lleno ? "#ffcc80" : "#fff") + '" stroke="#e65100" stroke-width="2.5" stroke-dasharray="' + (lleno ? "none" : "6 4") + '"/>';
  s += '<text x="' + (x0 + X / 2) + '" y="' + (y0 + X / 2 + 9) + '" font-size="26" font-weight="700" text-anchor="middle" fill="#0d47a1">x²</text>';
  var et = (Math.abs(h) === 1 ? "" : String(Math.abs(h)).replace(".5", "½")) + "x";
  if (w >= 34){ s += '<text x="' + (x0 + X + w / 2) + '" y="' + (y0 + X / 2 + 7) + '" font-size="18" font-weight="700" text-anchor="middle" fill="#1b5e20">' + et + '</text>'; }
  s += '<text x="' + (x0 + X / 2) + '" y="' + (y0 + X + w / 2 + 7) + '" font-size="18" font-weight="700" text-anchor="middle" fill="#1b5e20">' + (w >= 22 ? et : "") + '</text>';
  if (lleno && w >= 28) s += '<text x="' + (x0 + X + w / 2) + '" y="' + (y0 + X + w / 2 + 7) + '" font-size="17" font-weight="700" text-anchor="middle" fill="#bf360c">' + kv + '</text>';
  s += '<text x="' + (x0 + X / 2) + '" y="' + (y0 - 10) + '" font-size="16" text-anchor="middle" fill="#37474f">x</text><text x="' + (x0 + X + w / 2) + '" y="' + (y0 - 10) + '" font-size="16" text-anchor="middle" fill="#37474f">' + frTxt(Math.abs(b), 2) + '</text>';
  s += '<text x="' + (x0 - 10) + '" y="' + (y0 + X / 2 + 6) + '" font-size="16" text-anchor="end" fill="#37474f">x</text><text x="' + (x0 - 10) + '" y="' + (y0 + X + w / 2 + 6) + '" font-size="16" text-anchor="end" fill="#37474f">' + frTxt(Math.abs(b), 2) + '</text>';
  var W = x0 + X + w + 30, H = y0 + X + w + 20;
  $("vi-svg").innerHTML = '<svg style="display:block;margin:auto" viewBox="0 0 ' + W + " " + H + '" width="' + Math.min(420, W * 1.25) + '" role="img" aria-label="' + T("Area model of x² + ", "Modelo del área de x² + ") + Math.abs(b) + "x" + (lleno ? T(" with the corner of " + kv + " completed", " con la esquina de " + kv + " completada") : T(" with the corner still missing", " con la esquina todavía vacía")) + '">' + s + "</svg>";
  var p = [0, b, 1];
  $("vi-txt").innerHTML = '<div class="linea">' + T("Half of ", "La mitad de ") + sg(b) + " = " + hv + "; " + T("the corner is ", "la esquina es ") + "(" + hv + ")² = " + kv + ".</div>" +
    (lleno ? '<div class="linea"><strong>' + pVis(p) + " + " + kv + " = (x " + (b < 0 ? "−" : "+") + " " + frTxt(Math.abs(b), 2) + ")²</strong>. " + T("The big square has side x + b/2.", "El cuadrado grande tiene lado x + b/2.") + "</div>" : '<div class="linea">' + T("Press “Complete the corner”.", "Pulse «Completar la esquina».") + "</div>");
}
$("vi-b").addEventListener("input", function(){ $("vi-esq").setAttribute("aria-pressed", "false"); viDibuja(); });
$("vi-esq").addEventListener("click", function(){ $("vi-esq").setAttribute("aria-pressed", $("vi-esq").getAttribute("aria-pressed") === "true" ? "false" : "true"); viDibuja(); });
viDibuja();
OMR("vq", function(){
  var h = nz(-9, 9), b = 2 * h, k = h * h;
  var ops = [{clave: "ok", html: cuadTxt(h)}, {clave: "s", html: cuadTxt(-h)}, {clave: "b", html: cuadTxt(b)}, {clave: "k", html: "(x " + (h < 0 ? "− " : "+ ") + k + ")²"}];
  var vistos = {}; ops = ops.filter(function(o){ if (vistos[o.html]) return false; vistos[o.html] = 1; return true; });
  return {enun: T("Which binomial squared is ", "¿Qué binomio al cuadrado es ") + envuelve(pVis([k, b, 1]), pVoz([k, b, 1])) + "?", correcta: "ok", opciones: ops,
    porClave: {s: T("Look at the sign of the middle term: it goes inside the parentheses.", "Mire el signo del término del medio: es el que va dentro del paréntesis."), b: T("Inside goes half of b, not b.", "Dentro va la mitad de b, no b."), k: T("Inside goes half of b, not the last term.", "Dentro va la mitad de b, no el último término.")},
    pista: T("Half of the coefficient of x goes inside the parentheses.", "Dentro del paréntesis va la mitad del coeficiente de x."), bien: pVis([k, b, 1]) + " = " + cuadTxt(h) + T(", because half of ", ", porque la mitad de ") + sg(b) + T(" is ", " es ") + sg(h) + T(" and ", " y ") + pn(h) + "² = " + k + "."};
});

/* ===== MODULE 2 · The five steps ===== */
function casoCC(a){
  var r1, r2; do { r1 = nz(-9, 9); r2 = nz(-9, 9); } while ((r1 + r2) % 2 || r1 === r2 || r1 + r2 === 0);
  var b = -(r1 + r2), c = r1 * r2, h = b / 2, D = h * h - c;
  return {a: a || 1, r1: Math.max(r1, r2), r2: Math.min(r1, r2), b: b, c: c, h: h, k: h * h, D: D, d: Math.sqrt(D)};
}
function pasosCC(k){
  return [T("Leave the x terms on one side: ", "Se dejan los términos con x a un lado: ") + pVis([0, k.b, 1]) + " = " + sg(-k.c) + ".",
    T("Half of ", "La mitad de ") + sg(k.b) + T(" is ", " es ") + sg(k.h) + T("; squared, ", "; al cuadrado, ") + k.k + ". " + T("Add ", "Se suma ") + k.k + T(" to both sides: ", " a ambos lados: ") + pVis([0, k.b, 1]) + " + " + k.k + " = " + sg(-k.c) + " + " + k.k + " = " + sg(k.D) + ".",
    T("The left side is a binomial squared: ", "El lado izquierdo es un binomio al cuadrado: ") + cuadTxt(k.h) + " = " + k.D + ".",
    T("Square root with ±: ", "Raíz cuadrada con ±: ") + xmas(k.h) + " = ±" + k.d + ".",
    T("Solve: ", "Se resuelve: ") + "x = " + sg(-k.h) + " + " + k.d + " = " + sg(k.r1) + O + "x = " + sg(-k.h) + " − " + k.d + " = " + sg(k.r2) + ".",
    T("Solutions: ", "Soluciones: ") + "<strong>x = " + sg(k.r1) + O + "x = " + sg(k.r2) + "</strong>."];
}
pasoAPaso4("cs", function(){ var k = casoCC(); return {enun: T("Solve by completing the square: ", "Resuelva completando el cuadrado: ") + eqH([k.c, k.b, 1]) + ".", pasos: pasosCC(k)}; });
creaPracticaLibre("sq", function(){ var k = casoCC();
  return {enun: T("Solve by completing the square: ", "Resuelva completando el cuadrado: ") + eqH([k.c, k.b, 1]) + ". " + SOL_AYUDA,
    evalua: function(txt){ var v = leeSol(txt); if (v && v.length === 2 && v.some(function(x){ return x === k.h + k.d || x === k.h - k.d; }) && !v.every(function(x){ return x === k.r1 || x === k.r2; })) return {estado: "mal", msg: T("After x + b/2 = ±d, subtract b/2: x = −b/2 ± d. Watch the sign.", "Después de x + b/2 = ±d, se resta b/2: x = −b/2 ± d. Cuide el signo.")}; return evaluaSol(txt, [k.r1, k.r2]); },
    solucion: pasosCC(k).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 3 · Divide first ===== */
function pasosDiv(k){
  var A = k.a;
  return [T("Divide every term by ", "Se divide cada término entre ") + A + ": " + eqV([k.c, k.b, 1]) + "."].concat(pasosCC(k));
}
pasoAPaso4("dv", function(){ var k = casoCC(elige([2, 3, 4, 5])); return {enun: T("Solve by completing the square: ", "Resuelva completando el cuadrado: ") + eqH([k.a * k.c, k.a * k.b, k.a]) + ".", pasos: pasosDiv(k)}; });
OMR("dq", function(){ var k = casoCC(elige([2, 3, 4, 5])), A = k.a, P = [A * k.c, A * k.b, A];
  var ops = [{clave: "ok", html: eqH([k.c, k.b, 1])}, {clave: "c", html: eqH([A * k.c, k.b, 1])}, {clave: "b", html: eqH([k.c, A * k.b, 1])}, {clave: "x", html: eqH([k.c, k.b, A])}];
  return {enun: T("Divide ", "Divida ") + eqH(P) + T(" by ", " entre ") + A + T(". Which equation do you get?", ". ¿Qué ecuación queda?"), correcta: "ok", opciones: ops,
    porClave: {c: T("The constant must be divided too.", "También hay que dividir el término independiente."), b: T("The x term must be divided too.", "También hay que dividir el término con x."), x: T("x² must be divided too: its coefficient becomes 1.", "También se divide x²: su coeficiente queda en 1.")},
    pista: T("Divide all three terms.", "Divida los tres términos."), bien: T("All three terms are divided by ", "Se dividen los tres términos entre ") + A + ": " + eqV([k.c, k.b, 1]) + "."};
});
creaPracticaLibre("dsq", function(){ var k = casoCC(elige([2, 3])), P = [k.a * k.c, k.a * k.b, k.a];
  return {enun: T("Solve by completing the square: ", "Resuelva completando el cuadrado: ") + eqH(P) + ". " + SOL_AYUDA, evalua: function(txt){ return evaluaSol(txt, [k.r1, k.r2]); }, solucion: pasosDiv(k).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 4 · How much to add ===== */
function suDibuja(){
  var r = leeSol($("su-b").value), out = $("su-txt");
  if (!r || r.length !== 1 || r[0] !== Math.round(r[0])){ out.innerHTML = '<div class="linea">' + T("Type a whole number for b, like 8 or −7.", "Escriba un número entero para b, como 8 o −7.") + "</div>"; return; }
  var b = r[0];
  out.innerHTML = '<div class="linea">x² ' + (b < 0 ? "− " : "+ ") + (Math.abs(b) === 1 ? "" : Math.abs(b)) + "x: b/2 = " + frTxt(b, 2) + T("; you add ", "; se suma ") + "(b/2)² = (" + frTxt(b, 2) + ")² = <strong>" + frTxt(b * b, 4) + "</strong>.</div>" +
    '<div class="linea">' + pVis([0, b, 1]) + " + " + frTxt(b * b, 4) + " = (x " + (b < 0 ? "−" : "+") + " " + frTxt(Math.abs(b), 2) + ")²" + (b % 2 ? T(". b is odd, so the result is a fraction.", ". b es impar, así que el resultado es una fracción.") : ".") + "</div>";
}
$("su-b").addEventListener("input", suDibuja); suDibuja();
creaPracticaLibre("aq", function(){ var b = nz(-15, 15), k = b * b / 4;
  return {enun: T("What do you add to complete the square of ", "¿Qué se suma para completar el cuadrado de ") + envuelve(pVis([0, b, 1]), pVoz([0, b, 1])) + T("? A fraction can be written as 25/4.", "? Una fracción se escribe como 25/4."),
    evalua: function(txt){ var v = leeSol(txt); if (!v || v.length !== 1) return {estado: "invalido", msg: T("Type one number.", "Escriba un número.")}; var x = v[0];
      if (Math.abs(x - k) < 1e-9) return {estado: "bien"};
      if (Math.abs(x - b / 2) < 1e-9 || Math.abs(x + b / 2) < 1e-9) return {estado: "mal", msg: T("That is half of b. Now square it.", "Esa es la mitad de b. Ahora elévela al cuadrado.")};
      if (Math.abs(x - b * b) < 1e-9) return {estado: "mal", msg: T("That is b². First take half of b, then square it.", "Eso es b². Primero saque la mitad de b y después elévela al cuadrado.")};
      if (Math.abs(x + k) < 1e-9) return {estado: "mal", msg: T("A square is never negative.", "Un cuadrado nunca es negativo.")};
      return {estado: "mal", msg: T("Take half of the coefficient of x and square it.", "Saque la mitad del coeficiente de x y elévela al cuadrado.")}; },
    solucion: "b/2 = " + frTxt(b, 2) + "; (" + frTxt(b, 2) + ")² = " + frTxt(b * b, 4) + "."};
});

/* ===== MODULE 5 · The origin of the formula ===== */
var OR_EXPR = ["ax² + bx + c = 0", "x² + (b/a)x + c/a = 0", "x² + (b/a)x = −c/a", "x² + (b/a)x + b²/4a² = b²/4a² − c/a", "(x + b/2a)² = (b² − 4ac)/4a²", "x + b/2a = ±√(b² − 4ac) / 2a", "x = (−b ± √(b² − 4ac)) / 2a"];
var OR_ACC = ["", T("Divide everything by a", "Se divide todo entre a"), T("Move the constant to the other side", "Se pasa la constante al otro lado"), T("Add (b/2a)² = b²/4a² to both sides", "Se suma (b/2a)² = b²/4a² en ambos lados"), T("Factor the perfect square and use a common denominator", "Se factoriza el cuadrado perfecto y se usa denominador común"), T("Take the square root without forgetting the ±", "Se saca raíz cuadrada sin olvidar el ±"), T("Subtract b/2a to get x alone", "Se despeja x restando b/2a")];
var OR_MAL = ["", T("Divide only the bx term by a", "Se divide entre a solo el término bx"), T("Move the (b/a)x term to the other side", "Se pasa el término (b/a)x al otro lado"), T("Add half, b/2a, to both sides", "Se suma la mitad, b/2a, en ambos lados"), T("Multiply everything by 4a² to clear denominators", "Se multiplica todo por 4a² para quitar denominadores"), T("Take the square root of the left side only", "Se saca raíz cuadrada solo del lado izquierdo"), T("Add b/2a to get x alone", "Se despeja x sumando b/2a")];
var OR_EXPR_MAL = [[], ["x² + bx + c/a = 0", "x² + (b/a)x + c = 0", "x² + (a/b)x + c/a = 0"], ["x² + (b/a)x = c/a", "x² = −(b/a)x − c/a", "x² + (b/a)x = −c"], ["x² + (b/a)x + b/2a = b/2a − c/a", "x² + (b/a)x + b²/4a² = −c/a", "x² + (b/a)x + b²/4a² = b²/4a² + c/a"], ["(x + b/a)² = (b² − 4ac)/4a²", "(x + b/2a)² = (b² − 4c)/4a²", "(x + b/2a)² = (b² − 4ac)/2a"], ["x + b/2a = √(b² − 4ac) / 2a", "x + b/2a = ±√(b² − 4ac) / 4a²", "x + b/2a = ±(b² − 4ac) / 2a"], ["x = (b ± √(b² − 4ac)) / 2a", "x = −b/2a ± √(b² − 4ac)", "x = (−b ± √(b² + 4ac)) / 2a"]];
var OR_EXPL = ["", T("So that the coefficient of x² is 1, all three terms are divided by a: bx ÷ a = (b/a)x and c ÷ a = c/a.", "Para que el coeficiente de x² sea 1, se dividen los tres términos entre a: bx ÷ a = (b/a)x y c ÷ a = c/a."), T("Subtract c/a on both sides, leaving only the x terms on the left: −c/a is on the right.", "Se resta c/a en ambos lados, para dejar a un lado solo los términos con x: queda −c/a a la derecha."), T("Half the coefficient of x is (b/a) ÷ 2 = b/2a; squared, b²/4a². It is added to both sides to keep the equation balanced.", "La mitad del coeficiente de x es (b/a) ÷ 2 = b/2a, y al cuadrado queda b²/4a². Se suma en ambos lados para mantener la igualdad."), T("On the left, x² + (b/a)x + b²/4a² = (x + b/2a)². On the right, with the common denominator 4a²: b²/4a² − 4ac/4a² = (b² − 4ac)/4a².", "A la izquierda, x² + (b/a)x + b²/4a² = (x + b/2a)². A la derecha, con denominador común 4a²: b²/4a² − 4ac/4a² = (b² − 4ac)/4a²."), T("The square root gives two signs (±). Also, √(4a²) = 2a, so the denominator is 2a.", "Al sacar la raíz aparecen dos signos (±). Además, √(4a²) = 2a, por eso el denominador queda 2a."), T("Subtract b/2a on both sides; both terms have denominator 2a, so they are written together.", "Se resta b/2a en ambos lados; como los dos términos tienen denominador 2a, se escriben juntos.")];
pasoAPaso4("ol", function(){ var P = []; for (var i = 1; i <= 6; i++) P.push(OR_ACC[i] + ": <strong>" + OR_EXPR[i] + "</strong>. " + OR_EXPL[i]); P.push(T("Result: the quadratic formula, the same one on the GED formula sheet.", "Resultado: la fórmula cuadrática, la misma que aparece en la hoja de fórmulas del GED.")); return {enun: T("Complete the square in ", "Completar el cuadrado en ") + "<strong>ax² + bx + c = 0</strong>.", pasos: P}; });
function casoNum(){ var a = aleatorio(2, 4), k = casoCC(a); k.B = a * k.b; k.C = a * k.c; k.delta = k.B * k.B - 4 * a * k.C; return k; }
pasoAPaso4("on", function(){ var k = casoNum(), a = k.a, raiz = Math.sqrt(k.delta);
  var P = [T("Divide everything by ", "Se divide todo entre ") + a + ": " + eqV([k.c, k.b, 1]) + ".", T("Move the constant: ", "Se pasa la constante: ") + pVis([0, k.b, 1]) + " = " + sg(-k.c) + ".",
    T("Add (b/2a)² = (", "Se suma (b/2a)² = (") + sg(k.B) + "/" + 2 * a + ")² = " + k.k + ": " + cuadTxt(k.h) + " = " + k.D + ". " + T("With letters: (b² − 4ac)/4a² = ", "Con letras: (b² − 4ac)/4a² = ") + k.delta + "/" + 4 * a * a + " = " + k.D + ".",
    T("Square root with ±: ", "Raíz cuadrada con ±: ") + xmas(k.h) + " = ±" + k.d + ".", T("x = ", "x = ") + sg(k.r1) + O + "x = " + sg(k.r2) + ".",
    T("With the formula: x = (", "Con la fórmula: x = (") + sg(-k.B) + " ± √" + k.delta + ") / " + 2 * a + " = (" + sg(-k.B) + " ± " + raiz + ") / " + 2 * a + ": <strong>x = " + sg(k.r1) + O + "x = " + sg(k.r2) + "</strong>. " + T("Both methods give the same solutions.", "Los dos métodos dan las mismas soluciones.")];
  return {enun: T("Solve ", "Resuelva ") + eqH([k.C, k.B, a]) + " (a = " + a + ", b = " + sg(k.B) + ", c = " + sg(k.C) + ").", pasos: P}; });
var OR_ULT = -1;
OMR("oq", function(){
  var tipo; do { tipo = aleatorio(0, 3); } while (tipo === OR_ULT); OR_ULT = tipo;
  if (tipo === 0){ var n = aleatorio(1, 6), otros = []; for (var i = 1; i <= 6; i++) if (i !== n && Math.abs(i - n) <= 2) otros.push(OR_ACC[i]); otros = baraja(otros);
    return {enun: T("In the derivation, ", "En la derivación, ") + "«" + OR_EXPR[n - 1] + "» " + T("becomes", "se convierte en") + " «" + OR_EXPR[n] + "». " + T("What was done in this step?", "¿Qué se hizo en este paso?"), correcta: "ok", opciones: [{clave: "ok", html: OR_ACC[n]}, {clave: "m", html: OR_MAL[n]}, {clave: "o1", html: otros[0]}, {clave: "o2", html: otros[1]}], pista: OR_EXPL[n], bien: T("Step ", "Paso ") + n + ": " + OR_EXPL[n]}; }
  if (tipo === 1){ var m = aleatorio(1, 6);
    return {enun: T("You have ", "Se tiene ") + "«" + OR_EXPR[m - 1] + "». " + T("Next step: ", "Siguiente paso: ") + OR_ACC[m].charAt(0).toLowerCase() + OR_ACC[m].slice(1) + ". " + T("Which equation do you get?", "¿Qué ecuación queda?"), correcta: "ok", opciones: [{clave: "ok", html: OR_EXPR[m]}].concat(OR_EXPR_MAL[m].map(function(e, j){ return {clave: "m" + j, html: e}; })), pista: OR_EXPL[m], bien: T("Step ", "Paso ") + m + ": " + OR_EXPL[m]}; }
  var k; do { k = casoNum(); } while (Math.abs(k.h) < 2);
  if (tipo === 2){ var cand = [k.k, k.a * k.a * k.k, k.h, k.b * k.b, k.a * k.k, 2 * k.k], ops = [], vis = {};
    cand.forEach(function(v, j){ if (!vis[v] && ops.length < 4){ vis[v] = 1; ops.push({clave: j ? "m" + j : "ok", html: sg(v)}); } });
    return {enun: T("To solve ", "Para resolver ") + eqH([k.C, k.B, k.a]) + T(" by completing the square, first divide by ", " completando el cuadrado, primero se divide entre ") + k.a + T(" to get ", " y queda ") + eqH([k.c, k.b, 1]) + ". " + T("What number do you add to both sides?", "¿Qué número se suma en ambos lados?"), correcta: "ok", opciones: ops,
      pista: T("Half the coefficient of x, squared.", "La mitad del coeficiente de x, al cuadrado."), bien: T("After dividing, the coefficient of x is ", "Después de dividir, el coeficiente de x es ") + sg(k.b) + T("; half is ", "; su mitad es ") + sg(k.h) + T(", and squared, ", " y al cuadrado, ") + k.k + "."}; }
  var cand2 = [k.delta, k.B * k.B + 4 * k.a * k.C, k.B * k.B - 4 * k.C, k.D, k.B * k.B - 2 * k.a * k.C], ops2 = [], vis2 = {};
  cand2.forEach(function(v, j){ if (!vis2[v] && ops2.length < 4){ vis2[v] = 1; ops2.push({clave: j ? "m" + j : "ok", html: sg(v)}); } });
  return {enun: T("Completing the square in ", "Al completar el cuadrado en ") + eqH([k.C, k.B, k.a]) + T(" gives ", " se llega a ") + cuadTxt(k.h) + " = " + k.D + T(". That ", ". Ese ") + k.D + T(" is (b² − 4ac)/4a². What is b² − 4ac for this equation?", " es (b² − 4ac)/4a². ¿Cuánto vale b² − 4ac en esta ecuación?"), correcta: "ok", opciones: ops2,
    pista: "a = " + k.a + ", b = " + sg(k.B) + ", c = " + sg(k.C) + ".", bien: "b² − 4ac = " + pn(k.B) + "² − 4(" + k.a + ")" + pn(k.C) + " = " + k.delta + ". " + k.delta + "/" + 4 * k.a * k.a + " = " + k.D + "."};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    sol = t("Solutions", "Soluciones")
    mods = [
     ("visual", t("The visual idea: completing a square", "La idea visual: completar un cuadrado"),
      f'''      <p>{t("x² + bx is drawn as a square with side x plus a rectangle of area bx. Cut the rectangle in half and put one half on each side of the square: only one corner is missing to form a big square. That corner measures b/2 by b/2, so its area is (b/2)².", "x² + bx se dibuja como un cuadrado de lado x más un rectángulo de área bx. Si ese rectángulo se parte por la mitad y se coloca una mitad a cada lado del cuadrado, falta solo una esquina para formar un cuadrado grande. Esa esquina mide b/2 por b/2, así que su área es (b/2)².")}</p>
      <div class="panel"><div class="campos"><div class="campo"><label for="vi-b">{t("Coefficient of x: b =", "Coeficiente de x: b =")} <output id="vi-bv"></output></label><input type="range" id="vi-b" min="1" max="12" step="1" value="6"></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="vi-esq" aria-pressed="false">{t("Complete the corner", "Completar la esquina")}</button></div></div>
      <div class="geo-svg" id="vi-svg"></div>
{n4.salida("vi-txt")}
      <div class="caja-tip">{t("If b is negative, the picture is the same with b/2 negative: x² − 6x + 9 = (x − 3)². The number you add, (b/2)², is always positive.", "Si b es negativo, el dibujo es el mismo con b/2 negativo: x² − 6x + 9 = (x − 3)². El número que se suma, (b/2)², siempre es positivo.")}</div>
{B.om("vq", t("Practice: which binomial squared is it?", "Practique: ¿qué binomio al cuadrado queda?"))}'''),
     (t("steps", "pasos"), t("The five steps (when a = 1)", "Los cinco pasos (cuando a = 1)"),
      f'''      <p>{t("1. Leave the x terms on one side. 2. Add (b/2)² to both sides. 3. Write the left side as (x + b/2)². 4. Take the square root with ±. 5. Solve for x.", "1. Dejar los términos con x a un lado. 2. Sumar (b/2)² a ambos lados. 3. Escribir el lado izquierdo como (x + b/2)². 4. Sacar la raíz cuadrada con ±. 5. Resolver para x.")}</p>
{n4.pasos("cs", t("Another case", "Otro caso"))}
      <div class="caja-atencion"><strong>{t("Do not forget the ±.", "No olvide el ±.")}</strong> {t("The square root gives two results, the positive one and the negative one. Without the ± you lose a solution.", "Al sacar la raíz cuadrada aparecen dos resultados, el positivo y el negativo. Sin el ± se pierde una solución.")}</div>
{libre("sq", t("Practice: solve by completing the square", "Practique: resuelva completando el cuadrado"), sol)}'''),
     (t("divide", "dividir"), t("When a ≠ 1: divide first", "Cuando a ≠ 1: dividir primero"),
      f'''      <p>{t("The five steps work when the coefficient of x² is 1. If it is not, first divide the whole equation by a, including the constant.", "Los cinco pasos funcionan cuando el coeficiente de x² es 1. Si no lo es, primero se divide toda la ecuación entre a, incluido el término independiente.")}</p>
{n4.pasos("dv", t("Another case", "Otro caso"))}
{B.om("dq", t("Practice: which equation do you get when you divide?", "Practique: ¿qué ecuación queda al dividir?"))}
{libre("dsq", t("Practice: divide, complete the square, and solve", "Practique: divida, complete el cuadrado y resuelva"), sol)}'''),
     (t("add", "sumar"), t("How much do you add?", "¿Cuánto hay que sumar?"),
      f'''      <p>{t("The heart of the method is (b/2)²: half the coefficient of x, squared. When b is odd, the result is a fraction.", "El corazón del método es (b/2)²: la mitad del coeficiente de x, elevada al cuadrado. Cuando b es impar, el resultado es una fracción.")}</p>
      <div class="panel"><div class="campos"><div class="campo"><label for="su-b">{t("Type b", "Escriba b")}</label><input type="text" autocomplete="off" id="su-b" value="5"></div></div></div>
{n4.salida("su-txt")}
{libre("aq", t("Practice: the term that completes the square", "Practique: el término que completa el cuadrado"), t("Term to add", "Término que se suma"))}'''),
     (t("origin", "origen"), t("The origin of the quadratic formula", "El origen de la fórmula cuadrática"),
      f'''{n4.formula("x = (−b ± √(b² − 4ac)) / 2a")}
      <p>{t("Completing the square in the general equation ax² + bx + c = 0, with letters, gives exactly the quadratic formula. It is not an isolated trick: it is the proof of where the formula of Lesson 4.3 comes from.", "Completar el cuadrado en la ecuación general ax² + bx + c = 0, con letras, da exactamente la fórmula cuadrática. No es un truco aislado: es la demostración de dónde proviene la fórmula de la Lección 4.3.")}</p>
      <h3>{t("Watch: the derivation, step by step", "Observe: la derivación, paso a paso")}</h3>
{n4.pasos("ol", t("Start again", "Empezar de nuevo"))}
      <h3>{t("Watch: the same steps with numbers", "Observe: los mismos pasos con números")}</h3>
{n4.pasos("on", t("Another case", "Otro caso"))}
      <div class="caja-tip">{t("Look at step 4: the right side, (b² − 4ac)/4a², is exactly what goes inside the square root in the formula. And √(4a²) = 2a: that is where the denominator 2a comes from.", "Fíjese en el paso 4: el lado derecho, (b² − 4ac)/4a², es justo lo que queda dentro de la raíz en la fórmula. Y √(4a²) = 2a: de ahí sale el denominador 2a.")}</div>
{B.om("oq", t("Practice: follow the derivation", "Practique: siga la derivación"))}''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Completar el cuadrado")
