"""Level 4 · Lesson 4.3 · The quadratic formula, the discriminant, and applications — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_4-3.html and algebra/n4-l4-3.html (the discriminant with the graph of the parabola,
the formula step by step, the path of a ball, and choosing the method). They are rebuilt here, inside LearnGED. Heights in feet.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "4-3"
TEMA = ("Quadratic equations", "Ecuaciones cuadráticas")
TIT = ("The quadratic formula, the discriminant, and applications", "La fórmula cuadrática, el discriminante y aplicaciones")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 4.2.</strong> In Lesson 4.2 you saw that completing the square in the general equation produces the quadratic formula. Now you use the formula directly: it solves any quadratic equation, whether it factors or not. In this lesson you may use the calculator and the GED formula sheet.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 4.2 se vio que completar el cuadrado en la ecuación general produce la fórmula cuadrática. Ahora se usará esa fórmula directamente: con ella se resuelve cualquier ecuación cuadrática, se factorice o no. En esta lección se permite el uso de la calculadora y de la hoja de fórmulas del GED.")}</p>
<p>{t("For any equation in standard form ax² + bx + c = 0, the solutions are:", "Para cualquier ecuación en forma estándar ax² + bx + c = 0, las soluciones son:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">x = (−b ± √(b² − 4ac)) / 2a</p>
<p>{t("The first step is always to identify a, b, and c with their signs. For example, in 2x² − 4x − 3 = 0: a = 2, b = −4, c = −3.", "El primer paso siempre es identificar a, b y c con sus signos. Por ejemplo, en 2x² − 4x − 3 = 0: a = 2, b = −4, c = −3.")}</p>
{caja("ojo", t("Watch the signs of b and c", "Cuide los signos de b y c"), t("<p>The value of b includes its sign. In −b, a negative b becomes positive. Substituting with parentheses, for example (−4)², avoids the most common sign mistakes: (−4)² = 16, never −16.</p>", "<p>El valor de b incluye su signo. En −b, un b negativo se vuelve positivo. Sustituir con paréntesis, por ejemplo (−4)², evita los errores de signo más frecuentes: (−4)² = 16, nunca −16.</p>"))}
{enlace(n, "formula", t("the quadratic formula step by step", "la fórmula cuadrática paso a paso"), t("Type the coefficients you want and reveal one step at a time.", "Escriba los coeficientes que quiera y vaya revelando un paso a la vez."))}'''

    s2 = f'''<p>{t("The part of the formula inside the square root, b² − 4ac, is called the <strong>discriminant</strong>. Its sign tells you how many real solutions the equation has before you solve it:", "La parte de la fórmula que está dentro de la raíz, b² − 4ac, se llama <strong>discriminante</strong>. Su signo revela cuántas soluciones reales tiene la ecuación antes de resolverla:")}</p>
{tabla(t("The discriminant and the number of solutions", "El discriminante y el número de soluciones"), t("How the sign of the discriminant tells the number of real solutions", "Relación entre el signo del discriminante y el número de soluciones reales"), [t("Discriminant b² − 4ac", "Discriminante b² − 4ac"), t("Real solutions", "Soluciones reales"), t("The parabola and the x-axis", "La parábola y el eje x")],
  [[t("greater than 0", "mayor que 0"), t("2 different solutions", "2 soluciones distintas"), t("crosses it at 2 points", "lo corta en 2 puntos")], [t("equal to 0", "igual a 0"), t("1 solution (a double one)", "1 solución (doble)"), t("touches it at 1 point", "lo toca en 1 punto")], [t("less than 0", "menor que 0"), t("no real solutions", "ninguna solución real"), t("does not touch it", "no lo toca")]])}
{ejemplo(t("Example 1: how many solutions does x² + 3x + 5 = 0 have?", "Ejemplo 1 · ¿Cuántas soluciones tiene x² + 3x + 5 = 0?"),
  [("1", "a = 1, b = 3, c = 5.", ""), ("2", t("Discriminant:", "Discriminante:"), "(3)² − 4(1)(5) = 9 − 20 = −11."), ("3", t("Since −11 < 0, there are no real solutions.", "Como −11 < 0, no hay soluciones reales."), ""),
   ("✓", t("Answer.", "Respuesta."), t("<strong>No real solution.</strong>", "<strong>Ninguna solución real.</strong>"))])}
{caja("tip", t("Find the discriminant first", "Calcule primero el discriminante"), t("<p>Before you solve, ask: how many solutions do I expect? Then you will know whether the equation has two, one, or none, and you will catch a mistake if your result does not match.</p>", "<p>Antes de resolver, pregúntese: «¿cuántas soluciones espero?». Así sabrá si la ecuación tiene dos, una o ninguna, y detectará errores si su resultado no coincide con esa predicción.</p>"))}
{practica("p1", t("Practice 1 — x² − 5x + 6 = 0", "Práctica 1 — x² − 5x + 6 = 0"), t("Find b² − 4ac and the number of real solutions.", "Calcule b² − 4ac e indique el número de soluciones reales."), [("a", t("1 → 2 solutions", "1 → 2 soluciones")), ("b", t("0 → 1 solution", "0 → 1 solución")), ("c", t("−1 → none", "−1 → ninguna"))])}
{practica("p2", t("Practice 2 — x² − 6x + 9 = 0", "Práctica 2 — x² − 6x + 9 = 0"), t("Find b² − 4ac and the number of real solutions.", "Calcule b² − 4ac e indique el número de soluciones reales."), [("a", t("36 → 2 solutions", "36 → 2 soluciones")), ("b", t("−36 → none", "−36 → ninguna")), ("c", t("0 → 1 solution", "0 → 1 solución"))])}
{practica("p3", t("Practice 3 — 2x² + x + 4 = 0", "Práctica 3 — 2x² + x + 4 = 0"), t("Find b² − 4ac and the number of real solutions.", "Calcule b² − 4ac e indique el número de soluciones reales."), [("a", t("33 → 2 solutions", "33 → 2 soluciones")), ("b", t("−31 → none", "−31 → ninguna")), ("c", t("0 → 1 solution", "0 → 1 solución"))])}
{enlace(n, t("discriminant", "discriminante"), t("the discriminant", "el discriminante"), t("A calculator for b² − 4ac with the graph of the parabola, and exercises to predict how many real solutions there are.", "Calculadora de b² − 4ac con la gráfica de la parábola y ejercicios para predecir cuántas soluciones reales hay."))}'''

    s3 = f'''{ejemplo(t("Example 2: whole-number solutions. Solve x² + 5x + 6 = 0 with the formula.", "Ejemplo 2 · Soluciones enteras. Resolver x² + 5x + 6 = 0 con la fórmula."),
  [("1", "a = 1, b = 5, c = 6.", ""), ("2", t("Discriminant:", "Discriminante:"), "5² − 4(1)(6) = 25 − 24 = 1."), ("3", "x = (−5 ± √1) / 2 = (−5 ± 1) / 2.", ""), ("4", t("x = −2 or x = −3.", "x = −2 o x = −3."), ""),
   ("✓", t("Solutions.", "Soluciones."), t("<strong>x = −2 and x = −3</strong>.", "<strong>x = −2 y x = −3</strong>."))])}
{ejemplo(t("Example 3: with the calculator (the root is not exact). Solve 2x² − 4x − 3 = 0.", "Ejemplo 3 · Con calculadora (raíz no exacta). Resolver 2x² − 4x − 3 = 0."),
  [("1", "a = 2, b = −4, c = −3.", ""), ("2", t("Discriminant:", "Discriminante:"), "(−4)² − 4(2)(−3) = 16 + 24 = 40."), ("3", "x = (4 ± √40) / 4.", t("With the calculator, √40 ≈ 6.32.", "Con calculadora, √40 ≈ 6.32.")), ("4", t("x ≈ (4 + 6.32) / 4 ≈ 2.58 or x ≈ (4 − 6.32) / 4 ≈ −0.58.", "x ≈ (4 + 6.32) / 4 ≈ 2.58 o x ≈ (4 − 6.32) / 4 ≈ −0.58."), ""),
   ("✓", t("Solutions (rounded).", "Soluciones (aproximadas)."), t("<strong>x ≈ 2.58 and x ≈ −0.58</strong>.", "<strong>x ≈ 2.58 y x ≈ −0.58</strong>."))])}
{practica("p4", t("Practice 4 — x² + 7x + 10 = 0", "Práctica 4 — x² + 7x + 10 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = −2 and x = −5", "x = −2 y x = −5")), ("b", t("x = 2 and x = 5", "x = 2 y x = 5")), ("c", t("x = −2 and x = 5", "x = −2 y x = 5"))])}
{practica("p5", t("Practice 5 — x² − 3x − 10 = 0", "Práctica 5 — x² − 3x − 10 = 0"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x = −5 and x = 2", "x = −5 y x = 2")), ("b", t("x = 5 and x = −2", "x = 5 y x = −2")), ("c", t("x = 5 and x = 2", "x = 5 y x = 2"))])}
{practica("p6", t("Practice 6 — x² − 2x − 1 = 0 (use the calculator)", "Práctica 6 — x² − 2x − 1 = 0 (use la calculadora)"), t("Choose the solutions.", "Seleccione las soluciones."), [("a", t("x ≈ 1.41 and x ≈ −1.41", "x ≈ 1.41 y x ≈ −1.41")), ("b", t("x = 1 only", "x = 1 solamente")), ("c", t("x ≈ 2.41 and x ≈ −0.41", "x ≈ 2.41 y x ≈ −0.41"))])}
{enlace(n, "formula", t("solving with the formula", "resolver con la fórmula"), t("Step by step with the coefficients you choose, and exercises to solve on your own.", "Resolución paso a paso con los coeficientes que elija, más ejercicios para resolver por su cuenta."))}'''

    s4 = f'''<p>{t("Quadratic functions model the height of an object thrown into the air. If h(t) is the height (in feet) after t seconds, solving h(t) = 0 tells you when it hits the ground, and solving h(t) = a value tells you when it reaches that height.", "Las funciones cuadráticas modelan la altura de un objeto lanzado al aire. Si h(t) es la altura (en pies) a los t segundos, resolver h(t) = 0 indica cuándo toca el suelo, y resolver h(t) = un valor indica cuándo alcanza esa altura.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">h(t) = −16t² + v₀t + h₀</p>
<p>{t("v₀ is the starting speed (in feet per second) and h₀ is the height it is thrown from (in feet). The −16 comes from gravity and is always the same when you measure in feet.", "v₀ es la velocidad inicial (en pies por segundo) y h₀ es la altura desde la que se lanza (en pies). El −16 viene de la gravedad y siempre es el mismo cuando se mide en pies.")}</p>
{ejemplo(t("Example 4: a ball is thrown and its height is h(t) = −16t² + 96t + 5. When does it hit the ground? (use the calculator)", "Ejemplo 4 · Una pelota se lanza y su altura es h(t) = −16t² + 96t + 5. ¿Cuándo toca el suelo? (usar calculadora)"),
  [("1", t("Hitting the ground means h(t) = 0:", "Tocar el suelo significa h(t) = 0:"), "−16t² + 96t + 5 = 0."), ("2", "a = −16, b = 96, c = 5.", ""), ("3", t("Discriminant:", "Discriminante:"), "96² − 4(−16)(5) = 9,216 + 320 = 9,536. √9,536 ≈ 97.65."), ("4", "t = (−96 ± 97.65) / (−32).", t("t ≈ −0.05 or t ≈ 6.05.", "t ≈ −0.05 o t ≈ 6.05.")),
   ("5", t("Throw out the negative root; t ≈ 6.05 is left.", "Se descarta la raíz negativa; queda t ≈ 6.05."), ""), ("✓", t("Answer.", "Respuesta."), t("<strong>The ball hits the ground after about 6.05 seconds.</strong>", "<strong>La pelota toca el suelo a los 6.05 segundos, aproximadamente.</strong>"))])}
{caja("ojo", t("Interpret the situation", "Interprete el contexto"), t("<p>In problems about time and height, negative solutions make no sense (time is not negative). The valid solution is the one that fits the real situation.</p>", "<p>En problemas de tiempo y altura, las soluciones negativas no tienen sentido (el tiempo no es negativo). La solución válida es la que corresponde a la situación real descrita.</p>"))}
{enlace(n, t("projectile", "proyectil"), t("the path of a ball", "la trayectoria de un proyectil"), t("A launch simulator: change the speed and the starting height, watch the curve, and answer questions about the situation.", "Simulador de lanzamiento: cambie la velocidad y la altura inicial, observe la curva y responda preguntas de contexto."))}'''

    s5 = f'''<p>{t("You now know three ways to solve a quadratic equation. Knowing which to choose saves time:", "Ya se conocen tres formas de resolver una ecuación cuadrática. Saber elegir ahorra tiempo:")}</p>
{tabla(t("The three methods", "Los tres métodos"), t("The three methods to solve quadratic equations and when each one is best", "Comparación de los tres métodos para resolver ecuaciones cuadráticas y cuándo conviene cada uno"), [t("Method", "Método"), t("When is it best?", "¿Cuándo conviene?")],
  [[t("Factoring", "Factorización"), t("When the trinomial factors easily with whole numbers.", "Cuando el trinomio se factoriza fácilmente con enteros.")], [t("Completing the square", "Completar el cuadrado"), t("When a = 1 and b is even; useful to understand the structure.", "Cuando a = 1 y b es par; útil para entender la estructura.")], [t("Quadratic formula", "Fórmula cuadrática"), t("Always works; best when it does not factor or the roots are not whole numbers.", "Siempre funciona; ideal cuando no se factoriza o las raíces no son enteras.")]])}
{caja("tip", t("Three questions, in order", "Tres preguntas, en orden"), t("<p>Does the trinomial factor easily with whole numbers? Then factor. If not, is a = 1 and b even? Then complete the square. In any other case, use the quadratic formula, which always works.</p>", "<p>¿El trinomio se factoriza fácilmente con enteros? Entonces factorice. Si no, ¿a = 1 y b es par? Entonces complete el cuadrado. En cualquier otro caso, use la fórmula cuadrática, que siempre funciona.</p>"))}
{enlace(n, t("methods", "metodos"), t("choosing the method", "cómo elegir el método"), t("Decide when it is best to factor, complete the square, or use the formula, and compare the three roads on the same equation.", "Decida cuándo conviene factorizar, completar el cuadrado o usar la fórmula, y compare los tres caminos en una misma ecuación."))}'''

    secciones = [("s-formula", t("The quadratic formula", "La fórmula cuadrática"), s1),
                 ("s-" + t("discriminant", "discriminante"), t("The discriminant: how many solutions?", "El discriminante: ¿cuántas soluciones?"), s2),
                 ("s-" + t("solve", "resolver"), t("Solving with the formula", "Resolver con la fórmula"), s3),
                 ("s-" + t("projectile", "proyectil"), t("Application: the path of a ball", "Aplicación: la trayectoria de un proyectil"), s4),
                 ("s-" + t("methods", "metodos"), t("Three methods: which one is best?", "Tres métodos: ¿cuál conviene?"), s5)]

    lesson = {"next": t("Lesson 5.1", "Lección 5.1"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("(−5)² − 4(1)(6) = 25 − 24.", "(−5)² − 4(1)(6) = 25 − 24."), "c": t("(−5)² is +25, not −25.", "(−5)² es +25, no −25.")}, "right": t("25 − 24 = 1 > 0: two solutions (x = 2 and x = 3).", "25 − 24 = 1 > 0: dos soluciones (x = 2 y x = 3)."), "solution": t("1 → 2 solutions.", "1 → 2 soluciones.")},
      "p2": {"ok": "c", "hints": {"a": t("Do not forget to subtract 4ac = 36.", "No olvide restar 4ac = 36."), "b": t("(−6)² is +36.", "(−6)² es +36.")}, "right": t("36 − 36 = 0: one double solution, x = 3.", "36 − 36 = 0: una solución doble, x = 3."), "solution": t("0 → 1 solution.", "0 → 1 solución.")},
      "p3": {"ok": "b", "hints": {"a": t("4ac = 4(2)(4) = 32 is subtracted, not added.", "4ac = 4(2)(4) = 32 se resta, no se suma."), "c": t("1² − 4(2)(4) = 1 − 32.", "1² − 4(2)(4) = 1 − 32.")}, "right": t("1 − 32 = −31 < 0: no real solutions.", "1 − 32 = −31 < 0: ninguna solución real."), "solution": t("−31 → none.", "−31 → ninguna.")},
      "p4": {"ok": "a", "hints": {"b": t("x = (−7 ± 3)/2: both are negative.", "x = (−7 ± 3)/2: las dos son negativas."), "c": t("Substitute x = 5: 25 + 35 + 10 is not 0.", "Sustituya x = 5: 25 + 35 + 10 no es 0.")}, "right": t("D = 49 − 40 = 9, x = (−7 ± 3)/2.", "D = 49 − 40 = 9, x = (−7 ± 3)/2."), "solution": t("x = −2 and x = −5.", "x = −2 y x = −5.")},
      "p5": {"ok": "b", "hints": {"a": t("−b = −(−3) = +3: x = (3 ± 7)/2.", "−b = −(−3) = +3: x = (3 ± 7)/2."), "c": t("Substitute x = 2: 4 − 6 − 10 is not 0.", "Sustituya x = 2: 4 − 6 − 10 no es 0.")}, "right": t("D = 9 + 40 = 49, x = (3 ± 7)/2.", "D = 9 + 40 = 49, x = (3 ± 7)/2."), "solution": t("x = 5 and x = −2.", "x = 5 y x = −2.")},
      "p6": {"ok": "c", "hints": {"a": t("x = (2 ± √8)/2 = 1 ± 1.41: do not forget the 1.", "x = (2 ± √8)/2 = 1 ± 1.41: no olvide el 1."), "b": t("D = 4 + 4 = 8 > 0: there are two solutions.", "D = 4 + 4 = 8 > 0: hay dos soluciones.")}, "right": t("D = 8, x = (2 ± 2.83)/2.", "D = 8, x = (2 ± 2.83)/2."), "solution": t("x ≈ 2.41 and x ≈ −0.41.", "x ≈ 2.41 y x ≈ −0.41.")},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("b includes its sign: b = −2.", "b incluye su signo: b = −2."), "c": t("c = +1.", "c = +1."), "d": t("a = 3, positive.", "a = 3, positivo.")}, "solution": "a = 3, b = −2, c = 1."},
      "B": {"ok": "a", "hints": {"b": t("25 − 24 is not 0.", "25 − 24 no es 0."), "c": t("(−5)² = +25.", "(−5)² = +25."), "d": t("Subtract 4ac: 25 − 24.", "Reste 4ac: 25 − 24.")}, "solution": t("1 → 2 solutions.", "1 → 2 soluciones.")},
      "C": {"ok": "d", "hints": {"a": t("Subtract 4ac = 16.", "Reste 4ac = 16."), "b": t("4² = 16 and 4ac = 16: 16 − 16.", "4² = 16 y 4ac = 16: 16 − 16."), "c": t("b² − 4ac = 16 − 16.", "b² − 4ac = 16 − 16.")}, "solution": t("0 → 1 solution.", "0 → 1 solución.")},
      "D": {"ok": "c", "hints": {"a": t("4ac = 12 is subtracted.", "4ac = 12 se resta."), "b": t("1 − 12 is not 0.", "1 − 12 no es 0."), "d": t("1 − 12 = −11, negative.", "1 − 12 = −11, negativo.")}, "solution": t("−11 → none.", "−11 → ninguna.")},
      "E": {"ok": "a", "hints": {"b": t("Substitute x = −3: 9 − 18 + 9 = 0. And x = 3?", "Sustituya x = −3: 9 − 18 + 9 = 0. ¿Y x = 3?"), "c": t("D = 36 − 36 = 0: only one solution.", "D = 36 − 36 = 0: una sola solución."), "d": t("D = 0, not negative.", "D = 0, no negativo.")}, "solution": t("x = 3 (a double solution).", "x = 3 (solución doble).")},
      "F": {"ok": "b", "hints": {"a": t("x = (−5 ± 7)/4: (−5 + 7)/4 = 1/2.", "x = (−5 ± 7)/4: (−5 + 7)/4 = 1/2."), "c": t("Substitute x = 3: 18 + 15 − 3 is not 0.", "Sustituya x = 3: 18 + 15 − 3 no es 0."), "d": t("(−5 + 7)/4 is positive.", "(−5 + 7)/4 es positivo.")}, "solution": t("x = 1/2 and x = −3.", "x = 1/2 y x = −3.")},
      "G": {"ok": "c", "hints": {"a": t("−16t² + 32t = −16t(t − 2) = 0.", "−16t² + 32t = −16t(t − 2) = 0."), "b": t("−16t(t − 2) = 0.", "−16t(t − 2) = 0."), "d": t("At t = 1 the ball is at its highest point.", "En t = 1 la pelota está en su punto más alto.")}, "solution": t("After 2 seconds.", "A los 2 segundos.")},
      "H": {"ok": "a", "hints": {"b": t("Guessing does not always work.", "Adivinar no siempre funciona."), "c": t("A common factor is not always there.", "No siempre hay factor común."), "d": t("Dividing by x loses solutions.", "Dividir entre x hace perder soluciones.")}, "solution": t("The quadratic formula.", "La fórmula cuadrática.")},
     }}

    quiz = [
     ("A", t("In 3x² − 2x + 1 = 0, what are a, b, and c?", "En 3x² − 2x + 1 = 0, ¿cuánto valen a, b y c?"), [("a", "a = 3, b = 2, c = 1"), ("b", "a = 3, b = −2, c = 1"), ("c", "a = 3, b = −2, c = −1"), ("d", "a = −3, b = 2, c = 1")]),
     ("B", t("The discriminant of x² − 5x + 6 = 0 and the number of solutions.", "Discriminante de x² − 5x + 6 = 0 y número de soluciones."), [("a", t("1 → 2 solutions", "1 → 2 soluciones")), ("b", t("0 → 1 solution", "0 → 1 solución")), ("c", t("−1 → none", "−1 → ninguna")), ("d", t("49 → 2 solutions", "49 → 2 soluciones"))]),
     ("C", t("The discriminant of x² + 4x + 4 = 0 and the number of solutions.", "Discriminante de x² + 4x + 4 = 0 y número de soluciones."), [("a", t("16 → 2 solutions", "16 → 2 soluciones")), ("b", t("−16 → none", "−16 → ninguna")), ("c", t("8 → 2 solutions", "8 → 2 soluciones")), ("d", t("0 → 1 solution", "0 → 1 solución"))]),
     ("D", t("The discriminant of x² + x + 3 = 0 and the number of solutions.", "Discriminante de x² + x + 3 = 0 y número de soluciones."), [("a", t("13 → 2 solutions", "13 → 2 soluciones")), ("b", t("0 → 1 solution", "0 → 1 solución")), ("c", t("−11 → none", "−11 → ninguna")), ("d", t("11 → 2 solutions", "11 → 2 soluciones"))]),
     ("E", t("Solve x² − 6x + 9 = 0.", "Resuelva x² − 6x + 9 = 0."), [("a", t("x = 3 (a double solution)", "x = 3 (solución doble)")), ("b", t("x = 3 and x = −3", "x = 3 y x = −3")), ("c", t("x = 9 and x = 1", "x = 9 y x = 1")), ("d", t("no solution", "ninguna solución"))]),
     ("F", t("Solve 2x² + 5x − 3 = 0.", "Resuelva 2x² + 5x − 3 = 0."), [("a", t("x = −1/2 and x = 3", "x = −1/2 y x = 3")), ("b", t("x = 1/2 and x = −3", "x = 1/2 y x = −3")), ("c", t("x = 1/2 and x = 3", "x = 1/2 y x = 3")), ("d", t("x = −1/2 and x = −3", "x = −1/2 y x = −3"))]),
     ("G", t("A ball has height h(t) = −16t² + 32t. When does it hit the ground (h = 0)?", "Una pelota tiene altura h(t) = −16t² + 32t. ¿Cuándo toca el suelo (h = 0)?"), [("a", t("after 16 seconds", "a los 16 segundos")), ("b", t("after 32 seconds", "a los 32 segundos")), ("c", t("after 2 seconds", "a los 2 segundos")), ("d", t("after 1 second", "a 1 segundo"))]),
     ("H", t("Which method is the safest when an equation does not factor with whole numbers?", "¿Qué método es el más seguro cuando una ecuación no se factoriza con enteros?"), [("a", t("The quadratic formula", "La fórmula cuadrática")), ("b", t("Guessing", "Adivinar")), ("c", t("Common factor", "Factor común")), ("d", t("Dividing by x", "Dividir entre x"))])]

    tarea = (t("For your own work, with your notebook, the calculator, and the GED formula sheet: (1) The ball: the height of a ball is h(t) = −16t² + 96t + 5 (in feet, with t in seconds). Find when it hits the ground and at what moments it is at 120 feet. Explain what each solution means and which one you throw out. (2) How many solutions do I expect? Before solving, find the discriminant of each equation and predict whether it has two, one, or no real solutions. Then check with the formula the ones that have solutions: x² − 6x + 9 = 0, x² + 2x + 5 = 0, 2x² − 3x − 2 = 0, x² − 4x + 1 = 0, 4x² + 4x + 1 = 0, and 3x² + x + 2 = 0. (3) The best method: decide and explain whether it is best to factor, take a square root, or use the formula, and solve with the method you chose: x² − 7x + 12 = 0, x² + 3x − 1 = 0, x² = 49, 2x² − 5x − 3 = 0, x² + 6x − 2 = 0, and 5x² = 20x. Then do several exercises of each activity on the practice page, solving them in your notebook first, and write down the ones you miss to review them. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, la calculadora y la hoja de fórmulas del GED: (1) El proyectil: la altura de una pelota es h(t) = −16t² + 96t + 5 (en pies, con t en segundos). Calcule cuándo toca el suelo y en qué momentos está a 120 pies. Explique qué significa cada solución y cuál descarta. (2) ¿Cuántas soluciones espero? Antes de resolver, calcule el discriminante de cada ecuación y prediga si tiene dos, una o ninguna solución real. Después compruebe con la fórmula las que tengan solución: x² − 6x + 9 = 0, x² + 2x + 5 = 0, 2x² − 3x − 2 = 0, x² − 4x + 1 = 0, 4x² + 4x + 1 = 0 y 3x² + x + 2 = 0. (3) El método más eficiente: decida y justifique si conviene factorizar, sacar raíz cuadrada o usar la fórmula, y resuelva por el método elegido: x² − 7x + 12 = 0, x² + 3x − 1 = 0, x² = 49, 2x² − 5x − 3 = 0, x² + 6x − 2 = 0 y 5x² = 20x. Después haga varios ejercicios de cada actividad de la página de práctica, resolviéndolos primero en el cuaderno, y anote los que falle para repasarlos. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Toss a ball straight up outside and count the seconds until it lands. Use h(t) = −16t² + v₀t + 4 (your hand is about 4 feet high) and try values of v₀ until the landing time matches what you counted. What starting speed did you throw it with?",
               "Lance una pelota hacia arriba al aire libre y cuente los segundos hasta que cae. Use h(t) = −16t² + v₀t + 4 (su mano está a unos 4 pies de altura) y pruebe valores de v₀ hasta que el tiempo de caída coincida con lo que contó. ¿Con qué velocidad inicial la lanzó?"))

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Solve any quadratic equation with the formula, predict the number of solutions with the discriminant, and model the path of a ball.", "Resuelva cualquier ecuación cuadrática con la fórmula, prediga el número de soluciones con el discriminante y modele la trayectoria de un proyectil."),
        ("🧮", t("Calculator and formula sheet allowed", "Se permiten calculadora y hoja de fórmulas")),
        [t("<strong>Identify</strong> a, b, and c with their signs and use the quadratic formula.", "<strong>Identificar</strong> a, b y c con sus signos y aplicar la fórmula cuadrática."),
         t("<strong>Find</strong> the discriminant and use it to predict the number of real solutions.", "<strong>Calcular</strong> el discriminante y usarlo para predecir el número de soluciones reales."),
         t("<strong>Solve</strong> problems about the path of a ball and interpret the solutions.", "<strong>Resolver</strong> problemas de la trayectoria de un proyectil e interpretar las soluciones."),
         t("<strong>Choose</strong> the best method: factoring, completing the square, or the formula.", "<strong>Elegir</strong> el método más conveniente: factorización, completar el cuadrado o la fórmula.")],
        secciones, tarea, quiz,
        t("Self-check checklist for the quadratic formula", "Lista de autoevaluación de la fórmula cuadrática"),
        t("Self-check checklist: skills for the quadratic formula and the discriminant", "Lista de autoevaluación: destrezas de la fórmula cuadrática y el discriminante"),
        [(t("Identifying a, b, c", "Identificar a, b, c"), t("I identify the coefficients with their signs in any form of the equation.", "Identifico los coeficientes con sus signos en cualquier forma de la ecuación."), t("I identify them but make a sign mistake.", "Los identifico, pero con un error de signo."), t("I mix up the coefficients or their signs.", "Confundo los coeficientes o sus signos.")),
         (t("The discriminant", "El discriminante"), t("I find b² − 4ac and use it to predict and check the result.", "Calculo b² − 4ac y lo uso para anticipar y verificar el resultado."), t("I find it, but I read the number of solutions wrong.", "Lo calculo, pero interpreto mal el número de soluciones."), t("I do not find the discriminant.", "No calculo el discriminante.")),
         (t("Using the formula and interpreting", "Aplicar la fórmula e interpretar"), t("I solve without substitution mistakes, even with inexact roots, and throw out impossible answers.", "Resuelvo sin errores de sustitución, incluso con raíces no exactas, y descarto lo imposible."), t("I use the formula with sign or calculation mistakes.", "Aplico la fórmula con errores de signo o de cálculo."), t("My substitution has mistakes that ruin the result.", "Sustituyo con errores que invalidan el resultado."))],
        t("<p>This lesson closes Topic 4 · Quadratic equations. You mastered the three methods of solving (factoring, completing the square, and the quadratic formula), the discriminant to predict the number of solutions, and modeling real situations such as the path of a ball.</p>\n<p>Topic 5 · Rational expressions begins with <strong>Lesson 5.1 · Simplifying rational expressions: factor and cancel</strong>. All the factoring of Topic 3 will be center stage again: now it will help you simplify fractions made of polynomials and find the values excluded from the domain.</p>",
          "<p>Con esta lección se cierra el Tema 4 · Ecuaciones cuadráticas. Se dominaron los tres métodos de resolución (factorización, completar el cuadrado y la fórmula cuadrática), el uso del discriminante para predecir el número de soluciones y el modelado de situaciones reales como la trayectoria de un proyectil.</p>\n<p>El Tema 5 · Expresiones racionales comienza con la <strong>Lección 5.1 · Simplificar expresiones racionales: factorizar y cancelar</strong>. Toda la destreza de factorización del Tema 3 volverá a ser protagonista: ahora servirá para simplificar fracciones con polinomios e identificar los valores excluidos del dominio.</p>"),
        ("5-1", ("", t("Lesson 5.1 · Simplifying rational expressions: factor and cancel", "Lección 5.1 · Simplificar expresiones racionales: factorizar y cancelar"))),
        [(t("quadratic formula", "fórmula cuadrática"), "x = (−b ± √(b² − 4ac)) / 2a"),
         (t("discriminant", "discriminante"), t("b² − 4ac: positive, two solutions; zero, one; negative, none that are real.", "b² − 4ac: positivo, dos soluciones; cero, una; negativo, ninguna real.")),
         (t("double solution", "solución doble"), t("When the discriminant is 0, the two solutions are the same number.", "Cuando el discriminante es 0, las dos soluciones son el mismo número.")),
         (t("parabola", "parábola"), t("The U-shaped graph of a quadratic function. Its x-intercepts are the real solutions.", "La gráfica en forma de U de una función cuadrática. Sus cortes con el eje x son las soluciones reales.")),
         (t("vertex", "vértice"), t("The highest (or lowest) point of a parabola; for a ball, its maximum height.", "El punto más alto (o más bajo) de una parábola; en un lanzamiento, la altura máxima."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function r2(x){ return Math.round(x * 100) / 100; }
function nd2(x){ return sg(r2(x)).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,"); }
function mil(n){ return sg(n).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,"); }
var O = T(" or ", " o ");
function disc(a, b, c){ return b * b - 4 * a * c; }
function cuantasTxt(n){ return n === 2 ? T("2 different real solutions", "2 soluciones reales distintas") : n === 1 ? T("1 real solution (a double one)", "1 solución real (doble)") : T("No real solution", "Ninguna solución real"); }
function cuantas(D){ return D > 0 ? 2 : D === 0 ? 1 : 0; }
function raicesQ(a, b, c){ var D = disc(a, b, c); if (D < 0) return []; var s = Math.sqrt(D); return D === 0 ? [-b / (2 * a)] : [(-b + s) / (2 * a), (-b - s) / (2 * a)]; }
function exacta(D){ return D >= 0 && esCuadrado(D); }
function eqH(a, b, c){ var p = pDe({2: a, 1: b, 0: c}); return envuelve(pVis(p) + " = 0", pVoz(p) + T(" equals 0", " es igual a 0")); }
function eqV(a, b, c){ return pVis(pDe({2: a, 1: b, 0: c})) + " = 0"; }
function discTxt(a, b, c){ var D = disc(a, b, c), q = 4 * a * c; return "(" + sg(b) + ")² − 4(" + sg(a) + ")(" + sg(c) + ") = " + mil(b * b) + (q < 0 ? " + " + mil(-q) : " − " + mil(q)) + " = " + mil(D); }
function solsTxt(a, b, c){ var D = disc(a, b, c); if (D < 0) return T("no real solution", "ninguna solución real");
  if (exacta(D)){ var s = Math.round(Math.sqrt(D)), l = ["x = " + frTxt(-b + s, 2 * a)]; if (s) l.push("x = " + frTxt(-b - s, 2 * a)); return l.join(O); }
  return raicesQ(a, b, c).map(function(v){ return "x ≈ " + nd2(v); }).join(O); }
function pasosFormula(a, b, c, v){
  v = v || "x"; var D = disc(a, b, c), P = [];
  P.push("a = " + sg(a) + ", b = " + sg(b) + ", c = " + sg(c) + ".");
  P.push(T("Discriminant: ", "Discriminante: ") + "b² − 4ac = " + discTxt(a, b, c) + ".");
  P.push(D > 0 ? T("It is positive: there are 2 different real solutions.", "Es positivo: hay 2 soluciones reales distintas.") : D === 0 ? T("It is zero: there is 1 real solution (a double one).", "Es cero: hay 1 solución real (doble).") : T("It is negative: there is no real solution. The parabola does not touch the x-axis.", "Es negativo: no hay ninguna solución real. La parábola no toca el eje x."));
  if (D < 0) return P;
  var s = Math.sqrt(D), den = 2 * a, menos = sg(-b);
  P.push(v + " = (−b ± √(b² − 4ac)) / 2a = (" + menos + " ± √" + mil(D) + ") / " + pn(den) + (exacta(D) ? " = (" + menos + " ± " + Math.round(s) + ") / " + pn(den) : T(". With the calculator, √", ". Con calculadora, √") + mil(D) + " ≈ " + nd2(s)) + ".");
  if (exacta(D)){ var k = Math.round(s); P.push(D === 0 ? v + " = " + menos + " / " + pn(den) + " = " + frTxt(-b, den) + "." : v + " = (" + menos + " + " + k + ") / " + pn(den) + " = " + frTxt(-b + k, den) + O + v + " = (" + menos + " − " + k + ") / " + pn(den) + " = " + frTxt(-b - k, den) + "."); }
  else P.push(v + " ≈ (" + menos + " + " + nd2(s) + ") / " + pn(den) + " ≈ " + nd2((-b + s) / den) + O + v + " ≈ (" + menos + " − " + nd2(s) + ") / " + pn(den) + " ≈ " + nd2((-b - s) / den) + ".");
  P.push(T("Solutions: ", "Soluciones: ") + "<strong>" + solsTxt(a, b, c).replace(/x/g, v) + "</strong>.");
  return P;
}
/* The parabola y = ax² + bx + c, with its x-intercepts marked */
function parabolaSVG(a, b, c, voz){
  var xv = -b / (2 * a), rs = raicesQ(a, b, c), w = 5; rs.forEach(function(r){ w = Math.max(w, Math.abs(r - xv) + 2); }); w = Math.min(w, 14);
  var x0 = xv - w, x1 = xv + w, f = function(x){ return a * x * x + b * x + c; }, ys = [], i, N = 80;
  for (i = 0; i <= N; i++) ys.push(f(x0 + (x1 - x0) * i / N));
  var yv = f(xv), y0 = Math.min(0, yv), y1 = Math.max(0, yv), alto = Math.max(Math.abs(yv), 6) * 1.6;
  if (a > 0){ y0 = Math.min(0, yv) - alto * .15; y1 = Math.max(0, yv) + alto; } else { y1 = Math.max(0, yv) + alto * .15; y0 = Math.min(0, yv) - alto; }
  var W = 440, H = 300, m = 34, X = function(x){ return m + (x - x0) / (x1 - x0) * (W - 2 * m); }, Y = function(y){ return H - m - (y - y0) / (y1 - y0) * (H - 2 * m); };
  var s = '<rect x="' + m + '" y="' + m + '" width="' + (W - 2 * m) + '" height="' + (H - 2 * m) + '" fill="#fafafa" stroke="#eceff1"/>';
  var paso = w > 8 ? 2 : 1;
  var marcas = "";
  for (i = Math.ceil(x0); i <= Math.floor(x1); i++) if (i % paso === 0){ s += '<line x1="' + X(i).toFixed(1) + '" y1="' + Y(0).toFixed(1) + '" x2="' + X(i).toFixed(1) + '" y2="' + (Y(0) + 5).toFixed(1) + '" stroke="#455a64"/>'; if (i) marcas += '<text x="' + X(i).toFixed(1) + '" y="' + (Y(0) + 21).toFixed(1) + '" font-size="11" text-anchor="middle" fill="#455a64" paint-order="stroke" stroke="#fff" stroke-width="3">' + sg(i) + "</text>"; }
  s += '<line x1="' + m + '" y1="' + Y(0).toFixed(1) + '" x2="' + (W - m) + '" y2="' + Y(0).toFixed(1) + '" stroke="#263238" stroke-width="2"/><text x="' + (W - m + 6) + '" y="' + (Y(0) + 5).toFixed(1) + '" font-size="15" font-style="italic" font-weight="700" fill="#263238">x</text>';
  if (x0 < 0 && x1 > 0) s += '<line x1="' + X(0).toFixed(1) + '" y1="' + m + '" x2="' + X(0).toFixed(1) + '" y2="' + (H - m) + '" stroke="#263238" stroke-width="2"/><text x="' + (X(0) + 6).toFixed(1) + '" y="' + (m + 12) + '" font-size="15" font-style="italic" font-weight="700" fill="#263238">y</text>';
  var d = ""; for (i = 0; i <= N; i++){ var x = x0 + (x1 - x0) * i / N, y = Math.max(y0 - 1e6, Math.min(y1 + 1e6, ys[i])); d += (i ? " L" : "M") + X(x).toFixed(1) + " " + Math.max(-50, Math.min(H + 50, Y(y))).toFixed(1); }
  s += '<clipPath id="cp-par"><rect x="' + m + '" y="' + m + '" width="' + (W - 2 * m) + '" height="' + (H - 2 * m) + '"/></clipPath><path d="' + d + '" fill="none" stroke="#1565c0" stroke-width="3" clip-path="url(#cp-par)"/>';
  rs.forEach(function(r){ s += '<circle cx="' + X(r).toFixed(1) + '" cy="' + Y(0).toFixed(1) + '" r="6" fill="#c62828" stroke="#fff" stroke-width="2"/>'; });
  s += marcas;
  return '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '" style="display:block;margin:auto;max-width:' + W + 'px;width:100%">' + s + "</svg>";
}

/* ===== MODULE 1 · The discriminant ===== */
function leeCoef(id){ var v = leeSol($(id).value); return v && v.length === 1 && v[0] === Math.round(v[0]) && Math.abs(v[0]) <= 50 ? v[0] : null; }
function diDibuja(){
  var a = leeCoef("di-a"), b = leeCoef("di-b"), c = leeCoef("di-c");
  if (a === null || b === null || c === null || !a){ $("di-txt").innerHTML = '<div class="linea">' + T("Type whole numbers from −50 to 50; a cannot be 0.", "Escriba números enteros de −50 a 50; a no puede ser 0.") + "</div>"; $("di-svg").innerHTML = ""; return; }
  var D = disc(a, b, c), n = cuantas(D);
  $("di-txt").innerHTML = '<div class="linea">' + eqV(a, b, c) + "</div>" + '<div class="linea">b² − 4ac = ' + discTxt(a, b, c) + "</div>" + '<div class="linea"><strong>' + cuantasTxt(n) + "</strong>" + (n ? ": " + solsTxt(a, b, c) : "") + ". " + (n === 2 ? T("The parabola crosses the x-axis at 2 points.", "La parábola corta el eje x en 2 puntos.") : n === 1 ? T("The parabola touches the x-axis at 1 point.", "La parábola toca el eje x en 1 punto.") : T("The parabola does not touch the x-axis.", "La parábola no toca el eje x.")) + "</div>";
  $("di-svg").innerHTML = parabolaSVG(a, b, c, T("Graph of y = ", "Gráfica de y = ") + pVoz(pDe({2: a, 1: b, 0: c})) + ". " + cuantasTxt(n) + ".");
}
["di-a", "di-b", "di-c"].forEach(function(id){ $(id).addEventListener("input", diDibuja); }); diDibuja();
function casoDisc(n){
  var a, b, c, D, k = 0;
  do { a = elige([1, 1, 1, 2, 3, -1]); b = aleatorio(-10, 10);
    if (n === 1){ var r = nz(-6, 6), p = elige([1, 1, 2, 3]); a = p * p * (a < 0 ? -1 : 1); b = -2 * a * r / p; c = a * r * r / (p * p); }
    else c = aleatorio(-12, 12);
    D = disc(a, b, c); k++; } while ((cuantas(D) !== n || b !== Math.round(b) || c !== Math.round(c) || !c) && k < 500);
  return {a: a, b: b, c: c, D: D};
}
OMR("dq", function(){ var n = elige([0, 1, 2]), k = casoDisc(n);
  return {enun: T("How many real solutions does ", "¿Cuántas soluciones reales tiene ") + eqH(k.a, k.b, k.c) + T(" have?", "?"), correcta: String(n), opciones: [2, 1, 0].map(function(x){ return {clave: String(x), html: cuantasTxt(x)}; }),
    pista: T("Find b² − 4ac first, with parentheses: (b)² − 4(a)(c).", "Calcule primero b² − 4ac, con paréntesis: (b)² − 4(a)(c)."), bien: "b² − 4ac = " + discTxt(k.a, k.b, k.c) + ". " + cuantasTxt(n) + "."};
});

/* ===== MODULE 2 · The formula ===== */
pasoAPaso4("fm", function(){
  var a = leeCoef("fm-a"), b = leeCoef("fm-b"), c = leeCoef("fm-c");
  if (a === null || b === null || c === null || !a) return {enun: T("Type whole numbers from −50 to 50 in a, b, and c (a cannot be 0), then press “Start with these coefficients”.", "Escriba números enteros de −50 a 50 en a, b y c (a no puede ser 0) y pulse «Empezar con estos coeficientes»."), pasos: [T("Check the coefficients.", "Revise los coeficientes.")]};
  return {enun: T("Solve ", "Resuelva ") + eqH(a, b, c) + T(" with the quadratic formula.", " con la fórmula cuadrática."), pasos: pasosFormula(a, b, c)};
});
["fm-a", "fm-b", "fm-c"].forEach(function(id){ $(id).addEventListener("change", function(){ $("fm-nuevo").click(); }); });
function casoFormula(){
  var tipo = elige(["ent", "ent", "frac", "aprox", "aprox"]), a, b, c;
  if (tipo === "ent"){ var r1 = nz(-9, 9), r2 = nz(-9, 9); a = 1; b = -(r1 + r2); c = r1 * r2; }
  else if (tipo === "frac"){ var p = elige([2, 3]), q, r = nz(-6, 6); do { q = nz(-7, 7); } while (mcd(p, Math.abs(q)) !== 1); a = p; b = -(q + p * r); c = q * r; }
  else { do { a = elige([1, 1, 2, 3]); b = aleatorio(-9, 9); c = nz(-9, 9); } while (disc(a, b, c) <= 0 || exacta(disc(a, b, c))); }
  return {a: a, b: b, c: c, tipo: tipo};
}
creaPracticaLibre("fq", function(){ var k = casoFormula(), rs = raicesQ(k.a, k.b, k.c);
  return {enun: T("Solve with the quadratic formula: ", "Resuelva con la fórmula cuadrática: ") + eqH(k.a, k.b, k.c) + ". " + (k.tipo === "aprox" ? T("The root is not exact: round each solution to the hundredths, like 2.58, −0.58.", "La raíz no es exacta: redondee cada solución a las centésimas, como 2.58, −0.58.") : T("Type both solutions separated by a comma; a fraction can be written as 1/2.", "Escriba las dos soluciones separadas por una coma; una fracción se escribe como 1/2.")),
    evalua: function(txt){ return evaluaSol(txt, rs, .006); }, solucion: pasosFormula(k.a, k.b, k.c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 3 · The path of a ball ===== */
function prDibuja(){
  var v0 = +$("pr-v").value, h0 = +$("pr-h").value, tq = +$("pr-t").value;
  $("pr-vv").textContent = v0; $("pr-hv").textContent = h0;
  var tv = v0 / 32, hm = h0 + v0 * v0 / 64, D = v0 * v0 + 64 * h0, ts = (-v0 - Math.sqrt(D)) / -32, h = function(t){ return -16 * t * t + v0 * t + h0; };
  if (tq > ts) tq = ts; $("pr-tv").textContent = tq.toFixed(1);
  $("pr-t").max = Math.ceil(ts * 2) / 2;
  var W = 460, H = 290, m = 44, tmax = Math.max(ts, 1), hmaxEje = Math.max(hm, 40) * 1.12, X = function(t){ return m + t / tmax * (W - m - 20); }, Y = function(y){ return H - m + 6 - y / hmaxEje * (H - m - 20); };
  var s = '<line x1="' + m + '" y1="' + Y(0) + '" x2="' + (W - 12) + '" y2="' + Y(0) + '" stroke="#263238" stroke-width="2"/><line x1="' + m + '" y1="' + Y(0) + '" x2="' + m + '" y2="14" stroke="#263238" stroke-width="2"/>';
  var pt = tmax > 6 ? 2 : 1, i;
  for (i = 0; i <= tmax + 1e-9; i += pt) s += '<text x="' + X(i).toFixed(1) + '" y="' + (Y(0) + 17) + '" font-size="11" text-anchor="middle" fill="#455a64">' + i + "</text>";
  var ph = hmaxEje > 300 ? 100 : hmaxEje > 120 ? 50 : 20;
  for (i = ph; i < hmaxEje; i += ph) s += '<line x1="' + m + '" y1="' + Y(i).toFixed(1) + '" x2="' + (W - 12) + '" y2="' + Y(i).toFixed(1) + '" stroke="#eceff1"/><text x="' + (m - 6) + '" y="' + (Y(i) + 4).toFixed(1) + '" font-size="11" text-anchor="end" fill="#455a64">' + i + "</text>";
  s += '<text x="' + (W - 12) + '" y="' + (Y(0) + 32) + '" font-size="12" text-anchor="end" fill="#263238">' + T("t (seconds)", "t (segundos)") + '</text><text x="' + (m + 6) + '" y="12" font-size="12" fill="#263238">' + T("height (feet)", "altura (pies)") + "</text>";
  var d = ""; for (i = 0; i <= 60; i++){ var t = ts * i / 60; d += (i ? " L" : "M") + X(t).toFixed(1) + " " + Y(Math.max(0, h(t))).toFixed(1); }
  s += '<path d="' + d + '" fill="none" stroke="#1565c0" stroke-width="3"/>';
  s += '<line x1="' + X(tv).toFixed(1) + '" y1="' + Y(0) + '" x2="' + X(tv).toFixed(1) + '" y2="' + Y(hm).toFixed(1) + '" stroke="#ef6c00" stroke-width="1.5" stroke-dasharray="5 4"/><circle cx="' + X(tv).toFixed(1) + '" cy="' + Y(hm).toFixed(1) + '" r="5" fill="#ef6c00"/>';
  s += '<circle cx="' + X(tq).toFixed(1) + '" cy="' + Y(h(tq)).toFixed(1) + '" r="7" fill="#2e7d32" stroke="#fff" stroke-width="2"/><circle cx="' + X(ts).toFixed(1) + '" cy="' + Y(0) + '" r="5" fill="#c62828"/>';
  $("pr-svg").innerHTML = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("The height of the ball over time: it starts at " + h0 + " feet, rises to " + nd2(hm) + " feet at " + nd2(tv) + " seconds, and lands at " + nd2(ts) + " seconds.", "La altura de la pelota con el tiempo: sale de " + h0 + " pies, sube hasta " + nd2(hm) + " pies a los " + nd2(tv) + " segundos y cae a los " + nd2(ts) + " segundos.") + '" style="display:block;margin:auto;max-width:' + W + 'px;width:100%">' + s + "</svg>";
  $("pr-txt").innerHTML = '<div class="linea"><strong>h(t) = −16t² + ' + v0 + "t" + (h0 ? " + " + h0 : "") + "</strong></div>" +
    '<div class="linea">' + T("Highest point (vertex): t = −b/2a = ", "Punto más alto (vértice): t = −b/2a = ") + v0 + " / 32 = " + nd2(tv) + T(" s, height ", " s, altura ") + nd2(hm) + T(" ft.", " pies.") + "</div>" +
    '<div class="linea">' + T("It hits the ground (h = 0) at t ", "Toca el suelo (h = 0) a los t ") + (Math.abs(ts - Math.round(ts)) < 1e-9 ? "= " : "≈ ") + nd2(ts) + T(" s (the other solution, ", " s (la otra solución, ") + nd2((-v0 + Math.sqrt(D)) / -32) + T(", is thrown out).", ", se descarta).") + "</div>" +
    '<div class="linea">' + T("At t = ", "En t = ") + tq.toFixed(1) + " s: h = " + nd2(h(tq)) + T(" ft.", " pies.") + "</div>";
}
["pr-v", "pr-h", "pr-t"].forEach(function(id){ $(id).addEventListener("input", prDibuja); }); prDibuja();
var PR_ULT = -1;
OMR("pq", function(){
  var T0 = aleatorio(2, 6), v0 = 16 * aleatorio(1, T0), h0 = 16 * T0 * T0 - v0 * T0, tv = v0 / 32, hm = h0 + v0 * v0 / 64, otra = -h0 / (16 * T0), q, k = aleatorio(1, T0 - 1);
  do { q = aleatorio(0, 4); } while (q === PR_ULT); PR_ULT = q;
  var hf = function(t){ return -16 * t * t + v0 * t + h0; }, mod = "h(t) = −16t² + " + v0 + "t" + (h0 ? " + " + h0 : ""), enun = T("A ball is thrown and its height in feet is ", "Se lanza una pelota y su altura en pies es ") + "<strong>" + mod + "</strong>. ", ops, ok, bien;
  var u = function(x, uni){ return nd2(x) + " " + uni; }, ft = T("feet", "pies"), sec = T("seconds", "segundos");
  if (q === 0){ enun += T("From what height was it thrown?", "¿Desde qué altura se lanzó?"); ok = u(h0, ft); ops = [ok, u(v0, ft), u(hm, ft)]; bien = T("The starting height is h(0) = ", "La altura inicial es h(0) = ") + h0 + T(" feet: the constant term.", " pies: el término independiente."); }
  else if (q === 1){ enun += T("After how many seconds does it reach its highest point?", "¿A los cuántos segundos alcanza su altura máxima?"); ok = u(tv, sec); ops = [ok, u(v0 / 16, sec), u(T0, sec)]; bien = T("The vertex is at t = −b/2a = −", "El vértice está en t = −b/2a = −") + v0 + " / (2 · (−16)) = " + nd2(tv) + T(" seconds.", " segundos."); }
  else if (q === 2){ enun += T("What is its greatest height?", "¿Cuál es su altura máxima?"); ok = u(hm, ft); ops = [ok, u(hm + 16, ft), u(h0 + v0, ft)]; bien = "h(" + nd2(tv) + ") = −16" + pn(r2(tv * tv)) + " + " + v0 + "(" + nd2(tv) + ")" + (h0 ? " + " + h0 : "") + " = " + nd2(hm) + T(" feet.", " pies."); }
  else if (q === 3){ enun += T("After how many seconds does it hit the ground?", "¿A los cuántos segundos toca el suelo?"); ok = u(T0, sec); ops = [ok, u(tv, sec), u(T0 + 1, sec)]; bien = T("Solving h(t) = 0 gives t = ", "Al resolver h(t) = 0 se obtiene t = ") + T0 + (h0 ? O + "t = " + nd2(otra) + T("; the negative one is thrown out, because time cannot be negative.", "; se descarta la negativa, porque el tiempo no puede serlo.") : O + T("t = 0 (the moment it is thrown).", "t = 0 (el momento del lanzamiento).")); }
  else { enun += T("How high is it after " + k + " seconds?", "¿A qué altura está a los " + k + " segundos?"); ok = u(hf(k), ft); ops = [ok, u(16 * k * k + v0 * k + h0, ft), u(-16 * k + v0 * k + h0, ft)]; bien = "h(" + k + ") = −16(" + k * k + ") + " + v0 + "(" + k + ")" + (h0 ? " + " + h0 : "") + " = " + nd2(hf(k)) + T(" feet.", " pies."); }
  var vis = {}, opciones = []; ops.forEach(function(x, j){ if (!vis[x]){ vis[x] = 1; opciones.push({clave: j ? "m" + j : "ok", html: x}); } });
  while (opciones.length < 3){ var extra = q === 1 || q === 3 ? u(T0 + opciones.length + 1, sec) : u(hm + 32 * opciones.length, ft); if (!vis[extra]){ vis[extra] = 1; opciones.push({clave: "e" + opciones.length, html: extra}); } }
  return {enun: enun, correcta: "ok", opciones: opciones, pista: q === 1 ? T("The highest point is at t = −b/2a.", "El punto más alto está en t = −b/2a.") : q === 3 ? T("Solve h(t) = 0 and keep the positive time.", "Resuelva h(t) = 0 y quédese con el tiempo positivo.") : q === 0 ? T("At the start, t = 0.", "Al principio, t = 0.") : T("Substitute the time in h(t), with parentheses.", "Sustituya el tiempo en h(t), con paréntesis."), bien: bien};
});

/* ===== MODULE 4 · Choosing the method ===== */
var MET = {fact: T("Factoring", "Factorización"), cs: T("Completing the square", "Completar el cuadrado"), formula: T("Quadratic formula", "Fórmula cuadrática")};
function casoMet(tipo){
  tipo = tipo || elige(["fact", "cs", "formula"]); var a, b, c, FF = null;
  if (tipo === "fact"){ var r1 = nz(-9, 9), r2 = nz(-9, 9); if (Math.random() < .25){ var p = 2, q; do { q = nz(-7, 7); } while (q % 2 === 0); a = 2; b = -(q + 2 * r1); c = q * r1; FF = {k: 1, m: 0, f: [[-q, 2], [-r1, 1]]}; } else { a = 1; b = -(r1 + r2); c = r1 * r2; FF = {k: 1, m: 0, f: [[-r1, 1], [-r2, 1]]}; } }
  else if (tipo === "cs"){ var h, m; do { h = nz(-6, 6); m = aleatorio(2, 30); } while (esCuadrado(m)); a = 1; b = 2 * h; c = h * h - m; }
  else { do { a = elige([1, 2, 3, 5]); b = aleatorio(-9, 9); c = nz(-9, 9); } while (disc(a, b, c) <= 0 || exacta(disc(a, b, c)) || (a === 1 && b % 2 === 0)); }
  return {tipo: tipo, a: a, b: b, c: c, FF: FF};
}
function porque(k){ var D = disc(k.a, k.b, k.c);
  if (k.tipo === "fact") return T("b² − 4ac = " + mil(D) + " is a perfect square, so the trinomial factors with whole numbers: factoring is the shortest road.", "b² − 4ac = " + mil(D) + " es un cuadrado perfecto, así que el trinomio se factoriza con enteros: factorizar es el camino más corto.");
  if (k.tipo === "cs") return T("It does not factor with whole numbers (b² − 4ac = " + mil(D) + " is not a perfect square), but a = 1 and b is even, so (b/2)² is a whole number: complete the square.", "No se factoriza con enteros (b² − 4ac = " + mil(D) + " no es un cuadrado perfecto), pero a = 1 y b es par, así que (b/2)² es un entero: conviene completar el cuadrado.");
  return T("It does not factor with whole numbers (b² − 4ac = " + mil(D) + " is not a perfect square), and " + (k.a !== 1 ? "a is not 1" : "b is odd") + ", so completing the square brings fractions: use the formula.", "No se factoriza con enteros (b² − 4ac = " + mil(D) + " no es un cuadrado perfecto), y " + (k.a !== 1 ? "a no es 1" : "b es impar") + ", así que completar el cuadrado trae fracciones: conviene la fórmula."); }
function viaFact(k){ return k.FF ? [T("Factor: ", "Se factoriza: ") + fVis(k.FF) + " = 0.", T("Each factor equals zero: ", "Cada factor igual a cero: ") + solsTxt(k.a, k.b, k.c) + "."] : [T("It does not factor with whole numbers: b² − 4ac = " + mil(disc(k.a, k.b, k.c)) + " is not a perfect square. This road gets stuck.", "No se factoriza con enteros: b² − 4ac = " + mil(disc(k.a, k.b, k.c)) + " no es un cuadrado perfecto. Este camino se atasca.")]; }
function viaCS(k){ var a = k.a, b = k.b, c = k.c, h = frTxt(b, 2 * a), D = disc(a, b, c), P = [];
  if (a !== 1) P.push(T("Divide by ", "Se divide entre ") + a + T(" (fractions appear): ", " (aparecen fracciones): ") + "x² " + (b < 0 ? "− " : "+ ") + frTxt(Math.abs(b), a) + "x " + (c < 0 ? "− " : "+ ") + frTxt(Math.abs(c), a) + " = 0.");
  P.push(T("Add (b/2)² = (", "Se suma (b/2)² = (") + h + ")² = " + frTxt(b * b, 4 * a * a) + T(" to both sides: ", " a ambos lados: ") + "(x " + (b < 0 ? "− " : "+ ") + frTxt(Math.abs(b), 2 * a) + ")² = " + frTxt(D, 4 * a * a) + ".");
  P.push(T("Square root with ±: ", "Raíz con ±: ") + solsTxt(a, b, c) + "."); return P; }
function meNuevo(){ var k = casoMet(); MEK = k; $("me-enun").innerHTML = T("Equation: ", "Ecuación: ") + eqH(k.a, k.b, k.c); $("me-rec").innerHTML = '<div class="linea"><strong>' + T("Recommended: ", "Conviene: ") + MET[k.tipo] + ".</strong> " + porque(k) + "</div>"; $("me-via").innerHTML = ""; }
var MEK = null;
$("me-otro").addEventListener("click", meNuevo);
$("me-f").addEventListener("click", function(){ $("me-via").innerHTML = viaFact(MEK).map(function(x){ return '<div class="linea">' + x + "</div>"; }).join(""); });
$("me-c").addEventListener("click", function(){ $("me-via").innerHTML = viaCS(MEK).map(function(x){ return '<div class="linea">' + x + "</div>"; }).join(""); });
$("me-q").addEventListener("click", function(){ $("me-via").innerHTML = pasosFormula(MEK.a, MEK.b, MEK.c).map(function(x){ return '<div class="linea">' + x + "</div>"; }).join(""); });
meNuevo();
OMR("mq", function(){ var k = casoMet();
  return {enun: T("Which method is best for ", "¿Qué método conviene más para ") + eqH(k.a, k.b, k.c) + "?", correcta: k.tipo, opciones: ["fact", "cs", "formula"].map(function(x){ return {clave: x, html: MET[x]}; }),
    porClave: {fact: T("Does it factor with whole numbers? Look for two numbers, or check whether b² − 4ac is a perfect square.", "¿Se factoriza con enteros? Busque los dos números o compruebe si b² − 4ac es un cuadrado perfecto."), cs: T("Completing the square is easy only when a = 1 and b is even.", "Completar el cuadrado es cómodo solo cuando a = 1 y b es par."), formula: T("The formula works, but there is a shorter road here.", "La fórmula funciona, pero aquí hay un camino más corto.")},
    bien: porque(k)};
});
creaPracticaLibre("mr", function(){ var k = casoMet(), rs = raicesQ(k.a, k.b, k.c), exa = exacta(disc(k.a, k.b, k.c));
  return {enun: T("Solve with the method you think is best: ", "Resuelva con el método que más convenga: ") + eqH(k.a, k.b, k.c) + ". " + (exa ? T("Type both solutions separated by a comma.", "Escriba las dos soluciones separadas por una coma.") : T("The root is not exact: round to the hundredths.", "La raíz no es exacta: redondee a las centésimas.")),
    evalua: function(txt){ return evaluaSol(txt, rs, .006); }, solucion: MET[k.tipo] + ". " + (k.tipo === "fact" ? viaFact(k) : k.tipo === "cs" ? viaCS(k) : pasosFormula(k.a, k.b, k.c)).join(" ").replace(/<\/?strong>/g, "")};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    sol = t("Solutions", "Soluciones")
    def coefs(pre, a, b, c):
        return "".join(f'<div class="campo"><label for="{pre}-{k}">{k} {t("(cannot be 0)", "(no puede ser 0)") if k == "a" else ""}</label><input type="text" inputmode="numeric" autocomplete="off" id="{pre}-{k}" value="{v}" style="width:6em"></div>' for k, v in (("a", a), ("b", b), ("c", c)))
    disc_t = (f'<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("How the sign of the discriminant tells the number of real solutions", "Relación entre el signo del discriminante y el número de soluciones reales")}</caption><thead><tr><th scope="col">{t("Discriminant b² − 4ac", "Discriminante b² − 4ac")}</th><th scope="col">{t("Real solutions", "Soluciones reales")}</th><th scope="col">{t("The parabola and the x-axis", "La parábola y el eje x")}</th></tr></thead><tbody>'
              f'<tr><td>{t("Greater than 0", "Mayor que 0")}</td><td>{t("2 different solutions", "2 soluciones distintas")}</td><td>{t("Crosses it at 2 points", "Lo corta en 2 puntos")}</td></tr>'
              f'<tr><td>{t("Equal to 0", "Igual a 0")}</td><td>{t("1 solution (a double one)", "1 solución (doble)")}</td><td>{t("Touches it at 1 point", "Lo toca en 1 punto")}</td></tr>'
              f'<tr><td>{t("Less than 0", "Menor que 0")}</td><td>{t("No real solution", "Ninguna solución real")}</td><td>{t("Does not touch it", "No lo toca")}</td></tr></tbody></table></div>')
    met_t = (f'<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("The three methods and when each one is best", "Los tres métodos y cuándo conviene cada uno")}</caption><thead><tr><th scope="col">{t("Method", "Método")}</th><th scope="col">{t("When is it best?", "¿Cuándo conviene?")}</th></tr></thead><tbody>'
             f'<tr><td>{t("Factoring", "Factorización")}</td><td>{t("When the trinomial factors easily with whole numbers.", "Cuando el trinomio se factoriza fácilmente con enteros.")}</td></tr>'
             f'<tr><td>{t("Completing the square", "Completar el cuadrado")}</td><td>{t("When a = 1 and b is even.", "Cuando a = 1 y b es par.")}</td></tr>'
             f'<tr><td>{t("Quadratic formula", "Fórmula cuadrática")}</td><td>{t("Always works; best when it does not factor or the roots are not whole numbers.", "Siempre funciona; ideal cuando no se factoriza o las raíces no son enteras.")}</td></tr></tbody></table></div>')
    mods = [
     (t("discriminant", "discriminante"), t("The discriminant: how many solutions?", "El discriminante: ¿cuántas soluciones?"),
      f'''      <p>{t("The discriminant is the part inside the square root of the quadratic formula: b² − 4ac. Its sign tells how many real solutions the equation has before you solve it.", "El discriminante es la parte que está dentro de la raíz de la fórmula cuadrática: b² − 4ac. Su signo dice cuántas soluciones reales tiene la ecuación antes de resolverla.")}</p>
{disc_t}
      <p class="nota">{t("What does “no real solution” mean? No real number solves the equation, so the parabola never crosses the x-axis. The answer lives in a larger set of numbers (the complex numbers) studied in later courses; it is not part of this level or of the GED test.", "¿Qué significa «ninguna solución real»? Que ningún número real resuelve la ecuación, por eso la parábola nunca cruza el eje x. La respuesta vive en un conjunto más amplio (los números complejos), que se estudia en cursos posteriores y no entra en este nivel ni en el examen GED.")}</p>
      <div class="panel"><p><strong>{t("Discriminant calculator.", "Calculadora del discriminante.")}</strong> {t("Type the coefficients of ax² + bx + c = 0.", "Escriba los coeficientes de ax² + bx + c = 0.")}</p><div class="campos">{coefs("di", 1, -2, -3)}</div></div>
{n4.salida("di-txt")}
      <div class="geo-svg" id="di-svg"></div>
      <div class="caja-tip">{t("Before solving, ask: how many solutions do I expect? If you get a different number at the end, there is a sign mistake somewhere.", "Antes de resolver, pregúntese: «¿cuántas soluciones espero?». Si al terminar obtiene un número distinto, hay un error de signos en algún paso.")}</div>
{B.om("dq", t("Practice: how many real solutions?", "Practique: ¿cuántas soluciones reales?"))}'''),
     ("formula", t("Solving with the quadratic formula", "Resolver con la fórmula cuadrática"),
      f'''{n4.formula("x = (−b ± √(b² − 4ac)) / 2a")}
      <p>{t("Type the coefficients and reveal one step at a time. Try to predict each step before you show it.", "Escriba los coeficientes y vaya revelando un paso a la vez. Intente anticipar cada paso antes de mostrarlo.")}</p>
      <div class="panel"><div class="campos">{coefs("fm", 2, -4, -3)}</div></div>
{n4.pasos("fm", t("Start with these coefficients", "Empezar con estos coeficientes"))}
      <div class="caja-atencion"><strong>{t("The most common mistake:", "El error más común:")}</strong> {t("forgetting that −b changes the sign of b. If b = −4, then −b = +4, and b² = (−4)² = 16, never −16.", "olvidar que −b cambia el signo de b. Si b = −4, entonces −b = +4, y b² = (−4)² = 16, nunca −16.")}</div>
{libre("fq", t("Practice: solve the equation", "Practique: resuelva la ecuación"), sol)}'''),
     (t("projectile", "proyectil"), t("The path of a ball", "La trayectoria de un proyectil"),
      f'''{n4.formula("h(t) = −16t² + v₀t + h₀")}
      <p>{t("v₀ is the starting speed (feet per second) and h₀ is the height it is thrown from (feet). The −16 comes from gravity and is always the same in feet.", "v₀ es la velocidad inicial (pies por segundo) y h₀ es la altura desde la que se lanza (pies). El −16 viene de la gravedad y siempre es el mismo en pies.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="pr-v">{t("Starting speed v₀:", "Velocidad inicial v₀:")} <output id="pr-vv"></output> {t("ft/s", "pies/s")}</label><input type="range" id="pr-v" min="16" max="96" step="16" value="64"></div>
        <div class="campo"><label for="pr-h">{t("Starting height h₀:", "Altura inicial h₀:")} <output id="pr-hv"></output> {t("ft", "pies")}</label><input type="range" id="pr-h" min="0" max="160" step="16" value="80"></div>
        <div class="campo"><label for="pr-t">{t("Look at t =", "Evaluar en t =")} <output id="pr-tv"></output> s</label><input type="range" id="pr-t" min="0" max="6" step="0.5" value="2"></div></div></div>
      <div class="geo-svg" id="pr-svg"></div>
{n4.salida("pr-txt")}
      <div class="caja-atencion"><strong>{t("Interpret the situation.", "Interprete el contexto.")}</strong> {t("Solving h(t) = 0 gives two solutions, but time cannot be negative. The valid answer is the positive one.", "Al resolver h(t) = 0 aparecen dos soluciones, pero el tiempo no puede ser negativo. La respuesta válida es la positiva.")}</div>
{B.om("pq", t("Practice: read the launch", "Practique: interprete el lanzamiento"))}'''),
     (t("methods", "metodos"), t("Three methods: which one is best?", "Tres métodos: ¿cuál conviene?"),
      f'''      <p>{t("Factoring, completing the square, and the formula reach the same solutions, but they do not take the same work.", "Factorización, completar el cuadrado y la fórmula llegan a las mismas soluciones, pero no cuestan el mismo trabajo.")}</p>
{met_t}
      <div class="caja-tip">{t("Ask three questions, in this order. Does the trinomial factor easily with whole numbers? Then factor. If not, is a = 1 and b even? Then complete the square. In any other case, use the formula, which always works.", "Hágase tres preguntas, en este orden. ¿El trinomio se factoriza fácilmente con enteros? Entonces factorice. Si no, ¿a = 1 y b es par? Entonces complete el cuadrado. En cualquier otro caso, use la fórmula, que siempre funciona.")}</div>
      <div class="panel"><p class="enun" id="me-enun"></p>
{n4.salida("me-rec")}
        <p><strong>{t("See the solution by each method:", "Ver la resolución por cada método:")}</strong></p>
        <div class="fila-btn"><button type="button" class="btn-sec" id="me-f">{t("By factoring", "Por factorización")}</button><button type="button" class="btn-sec" id="me-c">{t("By completing the square", "Completando el cuadrado")}</button><button type="button" class="btn-sec" id="me-q">{t("With the formula", "Con la fórmula cuadrática")}</button></div>
        <div class="salida" id="me-via" aria-live="polite"></div>
        <div class="fila-btn"><button type="button" class="btn" id="me-otro">{t("Another equation", "Otra ecuación")}</button></div></div>
{B.om("mq", t("Practice: which method is best?", "Practique: ¿qué método conviene más?"))}
{libre("mr", t("Practice: choose the method and solve", "Practique: elija el método y resuelva"), sol)}''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "La fórmula cuadrática, el discriminante y aplicaciones")
