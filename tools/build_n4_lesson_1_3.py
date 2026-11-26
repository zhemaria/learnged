"""Level 4 · Lesson 1.3 · Equations of a line: slope-intercept, point-slope, and standard form — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_1-3.html and algebra/n4-l1-3.html (slope-intercept, point-slope, converting between
the forms, parallel and perpendicular lines). They are rebuilt here, inside LearnGED.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4
from n4 import Plano, AZUL, ROJO

B.NIVEL = 4
N = "1-3"
TEMA = ("Analytic geometry", "Geometría analítica")
TIT = ("Equations of a line: slope-intercept, point-slope, and standard form", "Ecuaciones de la recta: pendiente-intercepto, punto-pendiente y forma estándar")
SCRIPTS = n4.SCRIPTS

def fig_mb():
    p = Plano(-4, 4, -3, 6, 36)
    p.seg((-2, -3), (2.5, 6), AZUL, 3)
    p.seg((1, 3), (2, 3), "#1565c0", 3, "7 5").seg((2, 3), (2, 5), "#c62828", 3, "7 5")
    p.texto((1.5, 3), "1", "#1565c0", 14, dy=16).texto((2, 4), "2", "#c62828", 14, "start", dx=10).texto((2.6, 4.2), "m = 2", "#10174f", 15, "start", dx=8)
    p.punto((0, 1), ROJO, "b = 1", "nw")
    return p.svg(t("The line y = 2x + 1. It crosses the y-axis at (0, 1), so b = 1. For each unit it moves to the right it goes up 2, so m = 2.",
                   "La recta y = 2x + 1. Cruza el eje y en (0, 1), así que b = 1. Por cada unidad que avanza a la derecha sube 2, así que m = 2."), 320)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 1.2.</strong> In Lesson 1.2 you found the slope (m) of a line. A line, though, is fixed by two facts: how steep it is (the slope) and where it goes through (a point or the intercept). This lesson puts the two together to <strong>write the equation</strong> of any line and change it between three equivalent forms. It is the tool that lets you model real linear situations (fees, pay, usage) with one algebraic expression.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 1.2 se calculó la pendiente (m) de una recta. Una recta, sin embargo, queda definida por dos datos: cuán inclinada está (la pendiente) y por dónde pasa (un punto o el intercepto). Esta lección une ambos para <strong>escribir la ecuación</strong> de cualquier recta y traducirla entre tres formas equivalentes. Es la herramienta que permite modelar situaciones lineales reales (tarifas, salarios, consumo) con una sola expresión algebraica.")}</p>
<p>{t("The most direct way to write a line is the <strong>slope-intercept form</strong>:", "La forma más directa de escribir una recta es la <strong>pendiente-intercepto</strong>:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">y = mx + b</p>
<p>{t("Here <strong>m</strong> is the slope (how much the line goes up or down for each unit to the right) and <strong>b</strong> is the <strong>y-intercept</strong>: the value of y where the line crosses the vertical axis, that is, the point (0, b).", "Aquí <strong>m</strong> es la pendiente (cuánto sube o baja la recta por cada unidad hacia la derecha) y <strong>b</strong> es el <strong>intercepto en y</strong>: el valor de y donde la recta cruza el eje vertical, es decir, el punto (0, b).")}</p>
{fig_mb()}
{ejemplo(t("Example 1: from the slope and the intercept. A line has slope 2 and crosses the y-axis at 3. What is its equation?", "Ejemplo 1 · Desde la pendiente y el intercepto. Una recta tiene pendiente 2 y cruza el eje y en 3. ¿Cuál es su ecuación?"),
  [("1", t("Name the facts.", "Se identifican los datos."), "m = 2 " + t("and", "y") + " b = 3."),
   ("2", t("Substitute in y = mx + b.", "Se sustituyen en y = mx + b."), ""),
   ("✓", t("Answer.", "Respuesta."), "<strong>y = 2x + 3</strong>.")])}
{ejemplo(t("Example 2: reading the slope and the intercept. For the line y = −3x + 5, find its slope and its intercept.", "Ejemplo 2 · Leer la pendiente y el intercepto. Dada la recta y = −3x + 5, identificar su pendiente y su intercepto."),
  [("1", t("The number in front of x is the slope.", "El coeficiente de x es la pendiente."), "m = −3."),
   ("2", t("The number by itself is the intercept.", "El término independiente es el intercepto."), t("b = 5, so the line goes through (0, 5).", "b = 5, es decir, pasa por (0, 5).")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>m = −3</strong> (the line goes down) and <strong>b = 5</strong>.", "<strong>m = −3</strong> (la recta baja) y <strong>b = 5</strong>."))])}
{caja("tip", t("Why y = mx + b is so handy", "La ventaja de y = mx + b"), t("<p>Just by looking at the equation you know what the line looks like: the sign of m tells you whether it goes up or down, and b tells you where it crosses the y-axis. That is why it is the favorite form for graphing. When m = 0, the line is horizontal and its equation is just y = b.</p>", "<p>Con solo mirar la ecuación se sabe cómo se ve la recta: el signo de m dice si sube o baja, y b dice por dónde corta el eje y. Por eso es la forma preferida para graficar. Cuando m = 0, la recta es horizontal y su ecuación queda y = b.</p>"))}
{enlace(n, t("slope-intercept", "pendiente-intercepto"), t("the slope-intercept form", "la forma pendiente-intercepto"), t("Move the slope and the intercept and watch the line; read m and b from an equation or a graph.", "Mueva la pendiente y el intercepto y observe la recta; lea m y b de una ecuación o de una gráfica."))}'''

    s2 = f'''<p>{t("When you know the slope and any point of the line (not necessarily the intercept), use the <strong>point-slope form</strong>:", "Cuando se conoce la pendiente y un punto cualquiera de la recta (no necesariamente el intercepto), conviene la forma <strong>punto-pendiente</strong>:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">y − y₁ = m(x − x₁)</p>
<p>{t("Here (x₁, y₁) is the known point. From this form you can always solve for y to get to y = mx + b.", "donde (x₁, y₁) es el punto conocido. Desde esta forma siempre se puede despejar y para llegar a y = mx + b.")}</p>
{ejemplo(t("Example 3: a point and the slope. Write the equation of the line with slope 3 through the point (2, 5).", "Ejemplo 3 · Dados un punto y la pendiente. Escribir la ecuación de la recta de pendiente 3 que pasa por el punto (2, 5)."),
  [("1", t("Substitute in the point-slope form.", "Se sustituye en la forma punto-pendiente."), "y − 5 = 3(x − 2)."),
   ("2", t("Distribute.", "Se distribuye."), "y − 5 = 3x − 6."),
   ("3", t("Solve for y.", "Se despeja y."), "y = 3x − 6 + 5."),
   ("✓", t("Answer.", "Respuesta."), "<strong>y = 3x − 1</strong>.")])}
{ejemplo(t("Example 4: two points. Write the equation of the line through (1, 2) and (3, 8).", "Ejemplo 4 · Dados dos puntos. Escribir la ecuación de la recta que pasa por (1, 2) y (3, 8)."),
  [("1", t("First, the slope.", "Primero la pendiente."), "m = (8 − 2) ÷ (3 − 1) = 6 ÷ 2 = 3."),
   ("2", t("Use one point, for example (1, 2).", "Se usa un punto, por ejemplo (1, 2)."), "y − 2 = 3(x − 1)."),
   ("3", t("Distribute and solve for y.", "Se distribuye y se despeja."), "y − 2 = 3x − 3 → y = 3x − 1."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>y = 3x − 1</strong>. (You get the same line with the other point.)", "<strong>y = 3x − 1</strong>. (Se obtiene lo mismo usando el otro punto.)"))])}
{caja("ojo", t("With two points, the slope comes first", "Con dos puntos, primero la pendiente"), t("<p>The point-slope form needs a value of m. So when you are given only two points, the first step is always to find the slope with m = (y₂ − y₁) ÷ (x₂ − x₁). Watch the signs: with the point (−2, 4), the form is y − 4 = m(x + 2).</p>", "<p>La forma punto-pendiente necesita un valor de m. Por eso, cuando solo se dan dos puntos, el primer paso siempre es calcular la pendiente con m = (y₂ − y₁) ÷ (x₂ − x₁). Cuidado con los signos: con el punto (−2, 4), la forma queda y − 4 = m(x + 2).</p>"))}
{practica("p1", t("Practice 1 — From m and b", "Práctica 1 — Desde m y b"), t("Slope 4 and y-intercept −2. The equation is…", "Pendiente 4 e intercepto en y igual a −2. La ecuación es…"), [("a", "y = −2x + 4"), ("b", "y = 4x + 2"), ("c", "y = 4x − 2")])}
{practica("p2", t("Practice 2 — Reading the slope", "Práctica 2 — Leer la pendiente"), t("What is the slope of y = −5x + 7?", "¿Cuál es la pendiente de y = −5x + 7?"), [("a", "7"), ("b", "−5"), ("c", "5")])}
{practica("p3", t("Practice 3 — A point on the y-axis", "Práctica 3 — Un punto del eje y"), t("The line with slope 2 that goes through (0, 4) is…", "La recta de pendiente 2 que pasa por (0, 4) es…"), [("a", "y = 2x + 4"), ("b", "y = 4x + 2"), ("c", "y = 2x − 4")])}
{enlace(n, t("point-slope", "punto-pendiente"), t("the point-slope form", "la forma punto-pendiente"), t("Cases step by step, with a point and the slope or with two points, and the line drawn at the end.", "Casos paso a paso, con un punto y la pendiente o con dos puntos, y la recta dibujada al terminar."))}'''

    s3 = f'''<p>{t("The <strong>standard form</strong> of the equation of a line is:", "La <strong>forma estándar</strong> de la ecuación de una recta es:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">Ax + By = C</p>
<p>{t("Here A, B, and C are whole numbers and, by custom, A is positive. The three forms describe the same line; you choose one or another depending on what you need.", "donde A, B y C son números enteros y, por convención, A es positivo. Las tres formas describen la misma recta; se elige una u otra según lo que se necesite.")}</p>
{tabla(t("The three forms of the equation of a line", "Las tres formas de la ecuación de la recta"), t("The three forms of the equation of a line, with the general expression and when to use each", "Las tres formas de la ecuación de la recta, con su expresión general y su uso principal"),
  [t("Form", "Forma"), t("Expression", "Expresión"), t("When to use it", "Cuándo conviene")],
  [[t("Slope-intercept", "Pendiente-intercepto"), "y = mx + b", t("To graph, and to see m and b at once.", "Para graficar y ver m y b de inmediato.")],
   [t("Point-slope", "Punto-pendiente"), "y − y₁ = m(x − x₁)", t("To write the line from a point and the slope.", "Para escribir la recta desde un punto y la pendiente.")],
   [t("Standard", "Estándar"), "Ax + By = C", t("A common format on the GED test; useful for systems of equations.", "Formato habitual del GED; útil para sistemas de ecuaciones.")]])}
{ejemplo(t("Example 5: from slope-intercept to standard. Change y = 2x + 3 to standard form.", "Ejemplo 5 · De pendiente-intercepto a estándar. Convertir y = 2x + 3 a la forma estándar."),
  [("1", t("Move the x-term to the left side.", "Se pasa el término con x al lado izquierdo."), "−2x + y = 3."),
   ("2", t("Multiply by −1 so that A is positive.", "Se multiplica por −1 para que A sea positivo."), "2x − y = −3."),
   ("✓", t("Answer.", "Respuesta."), "<strong>2x − y = −3</strong>.")])}
{ejemplo(t("Example 6: from standard to slope-intercept. Change 2x + 3y = 12 to slope-intercept form.", "Ejemplo 6 · De estándar a pendiente-intercepto. Convertir 2x + 3y = 12 a la forma pendiente-intercepto."),
  [("1", t("Leave the y-term alone.", "Se despeja el término con y."), "3y = −2x + 12."),
   ("2", t("Divide everything by 3.", "Se divide todo entre 3."), "y = −(2/3)x + 4."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>y = −(2/3)x + 4</strong>, with slope −2/3 and intercept 4.", "<strong>y = −(2/3)x + 4</strong>, con pendiente −2/3 e intercepto 4."))])}
{caja("tip", t("A check that never fails", "Comprobación que nunca falla"), t("<p>Choose a value of x, for example x = 3, and evaluate both forms. If both give the same y, the conversion is right. In Example 6: 2(3) + 3y = 12 gives y = 2, and −(2/3)(3) + 4 = 2 too.</p>", "<p>Elija un valor de x, por ejemplo x = 3, y evalúe las dos formas. Si ambas dan la misma y, la conversión está bien hecha. En el Ejemplo 6: 2(3) + 3y = 12 da y = 2, y −(2/3)(3) + 4 = 2 también.</p>"))}
{enlace(n, t("forms", "formas"), t("changing between the three forms", "la conversión entre las tres formas"), t("Conversions step by step, including the ones that leave a fraction for the slope and the ones where you must clear a fraction first.", "Conversiones paso a paso, incluidas las que dejan pendiente fraccionaria y las que obligan a quitar la fracción antes."))}'''

    s4 = f'''<p>{t("The slopes show how two lines are related:", "Las pendientes revelan la relación entre dos rectas:")}</p>
<ul><li>{t("<strong>Parallel</strong> lines have the <strong>same slope</strong> (m₁ = m₂). They never cross.", "Las rectas <strong>paralelas</strong> tienen la <strong>misma pendiente</strong> (m₁ = m₂). Nunca se cruzan.")}</li>
<li>{t("<strong>Perpendicular</strong> lines have <strong>negative reciprocal</strong> slopes; their product is −1 (m₁ × m₂ = −1). They cross at a right angle.", "Las rectas <strong>perpendiculares</strong> tienen pendientes <strong>recíprocas negativas</strong>; su producto es −1 (m₁ × m₂ = −1). Se cruzan formando un ángulo recto.")}</li></ul>
{ejemplo(t("Example 7: classifying two lines. How are y = 2x + 1 and y = 2x − 4 related? And y = 2x + 1 and y = −(1/2)x + 3?", "Ejemplo 7 · Clasificar dos rectas. ¿Qué relación tienen y = 2x + 1 e y = 2x − 4? ¿Y y = 2x + 1 con y = −(1/2)x + 3?"),
  [("1", t("The first two have the same slope (2).", "Las dos primeras tienen la misma pendiente (2)."), t("They are <strong>parallel</strong>.", "Son <strong>paralelas</strong>.")),
   ("2", t("For y = 2x + 1 and y = −(1/2)x + 3, multiply the slopes.", "Para y = 2x + 1 e y = −(1/2)x + 3 se multiplican las pendientes."), "2 × (−1/2) = −1."),
   ("✓", t("Answer.", "Respuesta."), t("y = 2x + 1 and y = −(1/2)x + 3 are <strong>perpendicular</strong>.", "y = 2x + 1 e y = −(1/2)x + 3 son <strong>perpendiculares</strong>."))])}
{ejemplo(t("Example 8: writing a parallel line. Write the equation of the line parallel to y = 3x − 2 that goes through (0, 5).", "Ejemplo 8 · Escribir una recta paralela. Escribir la ecuación de la recta paralela a y = 3x − 2 que pasa por (0, 5)."),
  [("1", t("Parallel means the same slope.", "Paralela significa misma pendiente."), "m = 3."),
   ("2", t("It goes through (0, 5).", "Pasa por (0, 5)."), "b = 5."),
   ("✓", t("Answer.", "Respuesta."), "<strong>y = 3x + 5</strong>.")])}
{caja("ojo", t("The negative reciprocal: two moves, not one", "La recíproca negativa: dos movimientos, no uno"), t("<p>To find the slope perpendicular to a given one, flip the fraction <strong>and</strong> change the sign. The perpendicular to m = 3 (that is, 3/1) is −1/3; the perpendicular to m = −2/5 is 5/2. Stopping halfway (flipping without changing the sign) is the most common mistake.</p>", "<p>Para hallar la pendiente perpendicular a una dada, se invierte la fracción <strong>y</strong> se cambia el signo. La perpendicular a m = 3 (es decir, 3/1) es −1/3; la perpendicular a m = −2/5 es 5/2. Quedarse a medio camino (invertir sin cambiar el signo) es el error más frecuente.</p>"))}
{practica("p4", t("Practice 4 — From standard form", "Práctica 4 — Desde la forma estándar"), t("The slope-intercept form of 4x + 2y = 10 is…", "La forma pendiente-intercepto de 4x + 2y = 10 es…"), [("a", "y = 4x + 5"), ("b", "y = −2x + 5"), ("c", "y = 2x − 5")])}
{practica("p5", t("Practice 5 — A perpendicular slope", "Práctica 5 — Una pendiente perpendicular"), t("The slope of a line perpendicular to y = 4x + 1 is…", "La pendiente de una recta perpendicular a y = 4x + 1 es…"), [("a", "−1/4"), ("b", "4"), ("c", "1/4")])}
{practica("p6", t("Practice 6 — A parallel line", "Práctica 6 — Una recta paralela"), t("Which line is parallel to y = −3x + 2?", "¿Qué recta es paralela a y = −3x + 2?"), [("a", "y = 3x + 2"), ("b", "y = (1/3)x − 1"), ("c", "y = −3x − 7")])}
{enlace(n, t("parallel", "paralelas"), t("parallel and perpendicular lines", "las rectas paralelas y perpendiculares"), t("Pairs of lines with their graph, and a negative-reciprocal calculator that shows the two moves.", "Pares de rectas con su gráfica y una calculadora de la recíproca negativa que muestra los dos movimientos."))}'''

    secciones = [("s-" + t("slope-intercept", "pendiente-intercepto"), t("The slope-intercept form: y = mx + b", "La forma pendiente-intercepto: y = mx + b"), s1),
                 ("s-" + t("point-slope", "punto-pendiente"), t("The point-slope form: y − y₁ = m(x − x₁)", "La forma punto-pendiente: y − y₁ = m(x − x₁)"), s2),
                 ("s-" + t("forms", "formas"), t("The standard form and changing between forms", "La forma estándar y la conversión entre formas"), s3),
                 ("s-" + t("parallel", "paralelas"), t("Parallel and perpendicular lines", "Rectas paralelas y perpendiculares"), s4)]

    lesson = {"next": t("Lesson 2.1", "Lección 2.1"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("You swapped m and b. The slope goes with x.", "Intercambió m y b. La pendiente va con la x."), "b": t("The intercept is −2, so the constant is − 2.", "El intercepto es −2, así que el término independiente es − 2.")}, "right": "m = 4, b = −2: y = 4x − 2.", "solution": "y = 4x − 2."},
      "p2": {"ok": "b", "hints": {"a": t("7 is the intercept b. The slope is the number with x.", "7 es el intercepto b. La pendiente es el número que acompaña a la x."), "c": t("Keep the sign: the number with x is −5.", "Conserve el signo: el número que acompaña a la x es −5.")}, "right": t("The number in front of x: m = −5.", "El coeficiente de x: m = −5."), "solution": "m = −5."},
      "p3": {"ok": "a", "hints": {"b": t("You swapped m and b.", "Intercambió m y b."), "c": t("(0, 4) means b = +4.", "(0, 4) quiere decir b = +4.")}, "right": t("(0, 4) is the intercept: b = 4.", "(0, 4) es el intercepto: b = 4."), "solution": "y = 2x + 4."},
      "p4": {"ok": "b", "hints": {"a": t("When 4x moves to the right side it becomes −4x, and then everything is divided by 2.", "Al pasar 4x al otro lado queda −4x, y después se divide todo entre 2."), "c": t("Check the signs: 2y = −4x + 10, so y = −2x + 5.", "Revise los signos: 2y = −4x + 10, así que y = −2x + 5.")}, "right": "2y = −4x + 10 → y = −2x + 5.", "solution": "y = −2x + 5."},
      "p5": {"ok": "a", "hints": {"b": t("4 is the parallel slope. Perpendicular: flip and change the sign.", "4 es la pendiente paralela. Perpendicular: se invierte y se cambia el signo."), "c": t("You flipped it, but you also need to change the sign.", "La invirtió, pero falta cambiar el signo.")}, "right": t("Flip 4/1 to 1/4 and change the sign: −1/4.", "Se invierte 4/1 a 1/4 y se cambia el signo: −1/4."), "solution": "−1/4."},
      "p6": {"ok": "c", "hints": {"a": t("Parallel needs the same slope, sign included: −3.", "Paralela pide la misma pendiente, con su signo: −3."), "b": t("(1/3) is not the same slope as −3.", "(1/3) no es la misma pendiente que −3.")}, "right": t("Same slope, −3: parallel.", "Misma pendiente, −3: paralelas."), "solution": "y = −3x − 7."},
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("You swapped m and b.", "Intercambió m y b."), "c": t("The intercept is −1, not +1.", "El intercepto es −1, no +1."), "d": t("The slope is 5: it goes with x.", "La pendiente es 5: va con la x.")}, "solution": "y = 5x − 1."},
      "B": {"ok": "c", "hints": {"a": t("6 is the intercept, not the slope.", "6 es el intercepto, no la pendiente."), "b": t("The slope is −2, not 2.", "La pendiente es −2, no 2."), "d": t("(0, 6) means b = +6.", "(0, 6) quiere decir b = +6.")}, "solution": "y = −2x + 6."},
      "C": {"ok": "d", "hints": {"a": t("3 is y₁, not b. Use y − 3 = 4(x − 1).", "3 es y₁, no b. Use y − 3 = 4(x − 1)."), "b": t("You swapped the slope and the y-coordinate.", "Intercambió la pendiente y la coordenada y."), "c": t("Check the sign: y − 3 = 4x − 4, so y = 4x − 1.", "Revise el signo: y − 3 = 4x − 4, así que y = 4x − 1.")}, "solution": "y − 3 = 4(x − 1) → y = 4x − 1."},
      "D": {"ok": "b", "hints": {"a": t("(0, −2) means b = −2.", "(0, −2) quiere decir b = −2."), "c": t("You divided the run by the rise: m = 8 ÷ 4 = 2.", "Dividió el avance entre la elevación: m = 8 ÷ 4 = 2."), "d": t("The line goes up from (0, −2) to (4, 6): the slope is positive.", "La recta sube de (0, −2) a (4, 6): la pendiente es positiva.")}, "solution": "m = (6 − (−2)) ÷ 4 = 2, b = −2: y = 2x − 2."},
      "E": {"ok": "d", "hints": {"a": t("In standard form both variables are on the left and A is positive.", "En la forma estándar las dos variables van a la izquierda y A es positivo."), "b": t("A must be positive: multiply by −1.", "A debe ser positivo: multiplique por −1."), "c": t("The x-term goes first and A must be positive.", "El término con x va primero y A debe ser positivo.")}, "solution": "−3x + y = 5 → 3x − y = −5."},
      "F": {"ok": "d", "hints": {"a": t("You did not divide by 3.", "No dividió entre 3."), "b": t("Check the signs: 3y = −6x + 9.", "Revise los signos: 3y = −6x + 9."), "c": t("9 ÷ 3 = +3.", "9 ÷ 3 = +3.")}, "solution": "3y = −6x + 9 → y = −2x + 3."},
      "G": {"ok": "c", "hints": {"a": t("That is the same slope (parallel).", "Esa es la misma pendiente (paralela)."), "b": t("You flipped it, but you also need to change the sign.", "La invirtió, pero falta cambiar el signo."), "d": t("You changed the sign, but you also need to flip it.", "Cambió el signo, pero falta invertirla.")}, "solution": t("Flip 2/3 → 3/2 and change the sign: −3/2.", "Se invierte 2/3 → 3/2 y se cambia el signo: −3/2.")},
      "H": {"ok": "b", "hints": {"a": t("Parallel lines have the same slope. These are 4 and −1/4.", "Las paralelas tienen la misma pendiente. Estas tienen 4 y −1/4."), "c": t("The slopes are different, so they are not the same line.", "Las pendientes son distintas, así que no son la misma recta."), "d": t("Multiply the slopes: 4 × (−1/4) = −1.", "Multiplique las pendientes: 4 × (−1/4) = −1.")}, "solution": "4 × (−1/4) = −1: " + t("perpendicular.", "perpendiculares.")},
     }}

    quiz = [
     ("A", t("Slope 5 and y-intercept −1. The equation is…", "Pendiente 5 e intercepto en y igual a −1. La ecuación es…"), [("a", "y = 5x − 1"), ("b", "y = −x + 5"), ("c", "y = 5x + 1"), ("d", "y = x − 5")]),
     ("B", t("The line with slope −2 that goes through (0, 6) is…", "La recta de pendiente −2 que pasa por (0, 6) es…"), [("a", "y = 6x − 2"), ("b", "y = 2x + 6"), ("c", "y = −2x + 6"), ("d", "y = −2x − 6")]),
     ("C", t("The line with slope 4 that goes through (1, 3), in slope-intercept form, is…", "La recta de pendiente 4 que pasa por (1, 3), en forma pendiente-intercepto, es…"), [("a", "y = 4x + 3"), ("b", "y = 3x + 4"), ("c", "y = 4x + 1"), ("d", "y = 4x − 1")]),
     ("D", t("The line through (0, −2) and (4, 6) is…", "La recta que pasa por (0, −2) y (4, 6) es…"), [("a", "y = 2x + 2"), ("b", "y = 2x − 2"), ("c", "y = (1/2)x − 2"), ("d", "y = −2x + 4")]),
     ("E", t("The standard form of y = 3x + 5 (with A positive) is…", "La forma estándar de y = 3x + 5 (con A positivo) es…"), [("a", "3x + y = 5"), ("b", "−3x + y = 5"), ("c", "y − 3x = 5"), ("d", "3x − y = −5")]),
     ("F", t("The slope-intercept form of 6x + 3y = 9 is…", "La forma pendiente-intercepto de 6x + 3y = 9 es…"), [("a", "y = 6x + 3"), ("b", "y = 2x − 3"), ("c", "y = −2x − 3"), ("d", "y = −2x + 3")]),
     ("G", t("The slope perpendicular to m = 2/3 is…", "La pendiente perpendicular a m = 2/3 es…"), [("a", "2/3"), ("b", "3/2"), ("c", "−3/2"), ("d", "−2/3")]),
     ("H", t("How are y = 4x + 1 and y = −(1/4)x + 9 related?", "¿Qué relación tienen y = 4x + 1 e y = −(1/4)x + 9?"), [("a", t("Parallel", "Paralelas")), ("b", t("Perpendicular", "Perpendiculares")), ("c", t("They are the same line", "Son la misma recta")), ("d", t("Neither", "Ninguna de las dos"))])]

    tarea = (t("For your own work, with a notebook and graph paper: (1) Four lines in slope-intercept form: two from m and b, and two reading the slope and the intercept on a graph that you draw. (2) Four lines in point-slope form, two with a point and the slope and two with two points; then change each one to slope-intercept form. (3) Three equations changed between the three forms, one of them with a fraction for the slope. (4) Six pairs of lines sorted as parallel, perpendicular, or neither, with the slopes as your reason. (5) A real problem: a taxi charges $2.50 to start plus $1.80 per mile. Write the equation of the cost in the three forms and find how much a 12-mile ride costs. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y papel cuadriculado: (1) Cuatro rectas en forma pendiente-intercepto: dos a partir de m y b, y dos leyendo la pendiente y el intercepto en una gráfica que usted dibuje. (2) Cuatro rectas en forma punto-pendiente, dos con un punto y la pendiente y dos con dos puntos; después pase cada una a la forma pendiente-intercepto. (3) Tres ecuaciones convertidas entre las tres formas, una de ellas con pendiente fraccionaria. (4) Seis pares de rectas clasificados como paralelas, perpendiculares o ninguna de las dos, justificando cada decisión con las pendientes. (5) Un problema real: un taxi cobra $2.50 de arranque más $1.80 por milla. Escriba la ecuación del costo en las tres formas y calcule cuánto cuesta un viaje de 12 millas. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Find a price with a fixed part and a part per unit: a cell phone plan, a gym membership with a sign-up fee, a delivery fee plus a price per pound. Write it as y = mx + b, say what m and b mean in that situation, and graph it for the first 10 units. Compare two plans: are their lines parallel? What would that mean?",
               "Busque un precio con una parte fija y una parte por unidad: un plan de teléfono, un gimnasio con cuota de inscripción, un cargo de envío más un precio por libra. Escríbalo como y = mx + b, diga qué significan m y b en esa situación y grafíquelo para las primeras 10 unidades. Compare dos planes: ¿sus rectas son paralelas? ¿Qué significaría eso?"))

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("Write the equation of a line in slope-intercept, point-slope, and standard form, change between them, and tell parallel and perpendicular lines by their slopes.", "Escriba la ecuación de una recta en forma pendiente-intercepto, punto-pendiente y estándar, convierta entre ellas y reconozca rectas paralelas y perpendiculares por sus pendientes."),
        ("📐", t("Graph paper", "Papel cuadriculado")),
        [t("<strong>Write</strong> the equation of a line in slope-intercept form (y = mx + b) and read m and b.", "<strong>Escribir</strong> la ecuación de una recta en forma pendiente-intercepto (y = mx + b) e identificar m y b."),
         t("<strong>Use</strong> the point-slope form to write the line through a point with a given slope, or through two points.", "<strong>Usar</strong> la forma punto-pendiente para escribir la recta que pasa por un punto con una pendiente dada, o por dos puntos."),
         t("<strong>Change</strong> between slope-intercept, point-slope, and standard form (Ax + By = C).", "<strong>Convertir</strong> entre las formas pendiente-intercepto, punto-pendiente y estándar (Ax + By = C)."),
         t("<strong>Recognize</strong> parallel and perpendicular lines by their slopes.", "<strong>Reconocer</strong> rectas paralelas y perpendiculares a partir de sus pendientes.")],
        secciones, tarea, quiz,
        t("Self-check checklist for the equations of a line", "Lista de autoevaluación de las ecuaciones de la recta"),
        t("Self-check checklist: skills for writing and changing the equation of a line", "Lista de autoevaluación: destrezas para escribir y convertir la ecuación de la recta"),
        [(t("Slope-intercept form", "Forma pendiente-intercepto"), t("I write and read y = mx + b with ease and match it to its graph.", "Escribo y leo y = mx + b con fluidez y la asocio a su gráfica."), t("I find m and b with occasional sign mistakes.", "Identifico m y b con errores ocasionales de signo."), t("I mix up the slope and the intercept.", "Confundo la pendiente con el intercepto.")),
         (t("Point-slope form", "Forma punto-pendiente"), t("I use it with ease, even starting from two points.", "La aplico con fluidez, incluso partiendo de dos puntos."), t("I make mistakes when I distribute or solve for y.", "Cometo errores al distribuir o despejar."), t("I do not write the form, or I substitute in the wrong place.", "No planteo la forma o sustituyo en el lugar equivocado.")),
         (t("Changing between forms", "Conversión entre formas"), t("I change between the three forms with no mistakes and choose the most useful one.", "Convierto entre las tres formas sin errores y elijo la más útil."), t("I change forms with algebra mistakes.", "Convierto con errores algebraicos al despejar."), t("I cannot get from one form to another.", "No logro pasar de una forma a otra.")),
         (t("Parallel and perpendicular", "Paralelas y perpendiculares"), t("I decide with the slopes and write parallel and perpendicular lines with the right negative reciprocal.", "Decido con las pendientes y escribo paralelas y perpendiculares con la recíproca negativa correcta."), t("I recognize parallel lines but mix up the condition for perpendicular.", "Reconozco las paralelas, pero confundo la condición de perpendicular."), t("I do not connect the slopes with how the lines sit.", "No relaciono las pendientes con la posición de las rectas."))],
        t("<p>This lesson closes <strong>Topic 1</strong>. You learned to write the equation of a line in three forms, <strong>slope-intercept</strong> (y = mx + b), <strong>point-slope</strong>, and <strong>standard</strong> (Ax + By = C), to change between them, and to recognize <strong>parallel</strong> and <strong>perpendicular</strong> lines by their slopes. With Lessons 1.1 and 1.2 you now have the whole basic toolkit of analytic geometry.</p>\n<p>In <strong>Topic 2</strong> you will go back to geometry in three dimensions: <strong>Lesson 2.1 · Volume of spheres, cones, and pyramids</strong>.</p>",
          "<p>Con esta lección se cierra el <strong>Tema 1</strong>. Se aprendió a escribir la ecuación de una recta en tres formas, <strong>pendiente-intercepto</strong> (y = mx + b), <strong>punto-pendiente</strong> y <strong>estándar</strong> (Ax + By = C), a convertir entre ellas y a reconocer rectas <strong>paralelas</strong> y <strong>perpendiculares</strong> por sus pendientes. Con las Lecciones 1.1 y 1.2 ya se tiene completa la caja de herramientas básica de la geometría analítica.</p>\n<p>En el <strong>Tema 2</strong> se volverá a la geometría en tres dimensiones: <strong>Lección 2.1 · Volumen de esferas, conos y pirámides</strong>.</p>"),
        ("2-1", ("", t("Lesson 2.1 · Volume of spheres, cones, and pyramids", "Lección 2.1 · Volumen de esferas, conos y pirámides"))),
        [(t("slope-intercept form", "forma pendiente-intercepto"), t("y = mx + b, where m is the slope and b the y-intercept.", "y = mx + b, donde m es la pendiente y b el intercepto en y.")),
         (t("y-intercept", "intercepto en y"), t("The point (0, b) where the line crosses the y-axis.", "El punto (0, b) donde la recta cruza el eje y.")),
         (t("point-slope form", "forma punto-pendiente"), "y − y₁ = m(x − x₁)"),
         (t("standard form", "forma estándar"), t("Ax + By = C, with whole numbers and A positive.", "Ax + By = C, con números enteros y A positivo.")),
         (t("negative reciprocal", "recíproca negativa"), t("The slope of a perpendicular line: flip the fraction and change the sign.", "La pendiente de una recta perpendicular: se invierte la fracción y se cambia el signo."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function F(n, d){ return fr(n, d === undefined ? 1 : d); }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function pnF(f){ return f.n < 0 ? "(" + fTxt(f) + ")" : fTxt(f); }
function opEq(txt, clave){ return {clave: clave || txt, html: eqHTML(txt)}; }
/* the right answer plus at most three different wrong ones */
function opsEq(ok, malos){ var vistos = {}, l = [opEq(ok)]; vistos[ok] = 1; baraja(malos).forEach(function(x){ if (!vistos[x] && l.length < 4){ vistos[x] = 1; l.push(opEq(x)); } }); return l; }
var PEND = [F(-3), F(-2), F(-3, 2), F(-1), F(-2, 3), F(-1, 2), F(0), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3)];
function grafRecta(lineas, ptos, voz, ancho){
  var P = Plano({xmin: -8, xmax: 8, ymin: -8, ymax: 8, u: 26, paso: 2}), s = "";
  lineas.forEach(function(l){ s += rectaPor(P, [0, fval(l.b)], [l.m.d, fval(l.b) + l.m.n], l.color || C4.azul, 3); });
  (ptos || []).forEach(function(p){ s += P.punto(p.p, p.color || C4.rojo, p.nombre, p.lado); });
  return P.svg(s, voz, ancho);
}
/* ===== MODULE 1 · y = mx + b ===== */
function siPinta(){
  var m = PEND[+$("si-m").value], b = +$("si-b").value;
  $("si-mv").innerHTML = mHTML(m); $("si-bv").textContent = sg(b);
  var P = Plano({xmin: -8, xmax: 8, ymin: -8, ymax: 8, u: 28, paso: 2}), s = rectaPor(P, [0, b], [m.d, b + m.n], C4.azul, 3.5);
  if (m.n !== 0){ var a = [0, b], c = [m.d, b], e = [m.d, b + m.n]; if (e[1] <= 8 && e[1] >= -8) s += P.seg(a, c, "#1565c0", 3, "7 5") + P.seg(c, e, "#c62828", 3, "7 5") + P.texto([m.d / 2, b], String(m.d), "#1565c0", 13, "middle", 0, m.n > 0 ? 14 : -12) + P.texto([m.d, b + m.n / 2], sg(m.n), "#c62828", 13, "start", 8, 0); }
  s += P.punto([0, b], C4.rojo, "(0, " + sg(b) + ")", "nw");
  var eq = eqSI(m, F(b));
  $("si-svg").innerHTML = P.svg(s, T("Graph of ", "Gráfica de ") + vozEq(eq) + T(". It crosses the y-axis at (0, ", ". Cruza el eje y en (0, ") + sg(b) + ").", 480);
  $("si-eq").innerHTML = '<div class="linea veredicto" style="font-size:22px">' + eqHTML(eq) + "</div>" +
    '<div class="linea">' + (m.n === 0 ? T("With m = 0 the line lies flat: it does not go up or down, and its equation is just y = b. Its slope is not missing: it is zero.", "Con m = 0 la recta se acuesta: no sube ni baja, y su ecuación queda y = b. No es una recta «sin pendiente»: su pendiente vale cero.") :
      T("From (0, ", "Desde (0, ") + sg(b) + T("), each time you move ", "), cada vez que avanza ") + m.d + T(" to the right the line goes ", " a la derecha, la recta ") + (m.n > 0 ? T("up ", "sube ") : T("down ", "baja ")) + Math.abs(m.n) + ".") + "</div>";
}
$("si-m").addEventListener("input", siPinta); $("si-b").addEventListener("input", siPinta); siPinta();
OMR("sq", function(){
  var m = elige(PEND.filter(function(x){ return x.n !== 0; })), b = F(aleatorio(-6, 6)), r = Math.random(), eq = eqSI(m, b);
  var malos = [eqSI(fneg(m), b), eqSI(m, fneg(b)), m.d === 1 && b.n !== 0 && b.d === 1 ? eqSI(b, m) : eqSI(fdiv(F(1), m), b), eqSI(fneg(m), fneg(b))];
  if (r < 0.4){
    return {enun: T("Which equation matches this line?", "¿Qué ecuación corresponde a esta recta?") + grafRecta([{m: m, b: b}], [{p: [0, fval(b)], nombre: "", color: C4.rojo}], T("A line on the coordinate plane that crosses the y-axis at ", "Una recta en el plano que cruza el eje y en ") + fTxt(b) + T(" and goes ", " y que ") + (m.n > 0 ? T("up ", "sube ") : T("down ", "baja ")) + Math.abs(m.n) + T(" for every ", " por cada ") + m.d + T(" to the right.", " a la derecha."), 300),
      correcta: eq, opciones: opsEq(eq, malos),
      pista: T("Find b where the line crosses the y-axis. Then count the rise and the run from that point: m = rise ÷ run.", "Busque b donde la recta corta el eje y. Después cuente la elevación y el avance desde ese punto: m = elevación ÷ avance."), bien: eqHTML(eq) + "."};
  }
  if (r < 0.7){
    var ok = "m = " + fTxt(m) + ", b = " + fTxt(b);
    return {enun: T("What are the slope and the y-intercept of ", "¿Cuáles son la pendiente y el intercepto de ") + eqHTML(eq) + "?", correcta: ok,
      opciones: [ok, "m = " + fTxt(b) + ", b = " + fTxt(m), "m = " + fTxt(fneg(m)) + ", b = " + fTxt(b), "m = " + fTxt(m) + ", b = " + fTxt(fneg(b))].map(function(x){ return {clave: x, html: x}; }),
      pista: T("m is the number with x (keep its sign); b is the number by itself.", "m es el número que acompaña a la x (con su signo); b es el número solo."), bien: ok + "."};
  }
  return {enun: T("A line has slope ", "Una recta tiene pendiente ") + fTxt(m) + T(" and crosses the y-axis at ", " y cruza el eje y en ") + fTxt(b) + T(". What is its equation?", ". ¿Cuál es su ecuación?"), correcta: eq,
    opciones: opsEq(eq, malos), pista: T("Put m with x and b by itself: y = mx + b.", "Ponga m con la x y b sola: y = mx + b."), bien: eqHTML(eq) + "."};
});

/* ===== MODULE 2 · Point-slope ===== */
function casoPS(){
  var dos = Math.random() < 0.5, m, x1, y1, x2, y2;
  if (dos){ do { m = F(elige([-3, -2, -1, 1, 2, 3])); x1 = aleatorio(-4, 3); y1 = aleatorio(-5, 5); var d = elige([1, 2, 3]); x2 = x1 + d; y2 = y1 + m.n * d; } while (y2 > 8 || y2 < -8); }
  else { m = elige([F(-3), F(-2), F(2), F(3), F(4), F(-1), F(1, 2), F(-1, 2)]); x1 = m.d === 2 ? elige([-4, -2, 2, 4]) : aleatorio(-4, 4); y1 = aleatorio(-5, 5); if (x1 === 0) x1 = 1; }
  var b = fsum(F(y1), fmul(fneg(m), F(x1))), eq = eqSI(m, b), mx1 = fmul(m, F(x1)), pasos = [];
  if (dos) pasos.push(T("First, the slope: ", "Primero la pendiente: ") + "m = (" + sg(y2) + " − " + pn(y1) + ") ÷ (" + sg(x2) + " − " + pn(x1) + ") = " + sg(y2 - y1) + " ÷ " + sg(x2 - x1) + " = <strong>" + fTxt(m) + "</strong>.");
  pasos.push(T("Substitute m and the point (", "Se sustituyen m y el punto (") + sg(x1) + ", " + sg(y1) + T(") in y − y₁ = m(x − x₁): ", ") en y − y₁ = m(x − x₁): ") + eqHTML(eqPS(m, F(x1), F(y1))) + ".");
  pasos.push(T("Distribute m: ", "Se distribuye m: ") + eqHTML(restaTxt("y", F(y1)) + " = " + coefX(m) + constTxt(fneg(mx1))) + ".");
  pasos.push(T("Solve for y (", "Se despeja y (") + (y1 >= 0 ? T("add ", "se suma ") + y1 : T("subtract ", "se resta ") + Math.abs(y1)) + T(" on both sides): ", " a los dos lados): ") + eqHTML(eq) + ".");
  return {m: m, x1: x1, y1: y1, x2: x2, y2: y2, b: b, eq: eq, dos: dos, pasos: pasos};
}
pasoAPaso4("ps", function(){
  var c = casoPS();
  return {enun: c.dos ? T("Write the equation of the line through ", "Escriba la ecuación de la recta que pasa por ") + parHTML(c.x1, c.y1) + T(" and ", " y ") + parHTML(c.x2, c.y2) + "." :
      T("Write the equation of the line with slope ", "Escriba la ecuación de la recta de pendiente ") + fTxt(c.m) + T(" through ", " que pasa por ") + parHTML(c.x1, c.y1) + ".",
    pasos: c.pasos, inicio: function(){ $("ps-svg").innerHTML = ""; },
    fin: function(){ var pts = [{p: [c.x1, c.y1], nombre: par(c.x1, c.y1), color: C4.rojo}]; if (c.dos) pts.push({p: [c.x2, c.y2], nombre: par(c.x2, c.y2), color: C4.morado});
      $("ps-svg").innerHTML = grafRecta([{m: c.m, b: c.b}], pts, T("The line ", "La recta ") + vozEq(c.eq) + T(" with the given points marked.", " con los puntos del enunciado marcados."), 420); }};
});
OMR("pq", function(){
  var c = casoPS(), eq = c.eq;
  var malos = [eqSI(c.m, F(c.y1)), eqSI(c.m, fsum(F(c.y1), fmul(c.m, F(c.x1)))), eqSI(c.m, fneg(c.b)), eqSI(fneg(c.m), c.b)];
  return {enun: (c.dos ? T("Which is the line through ", "¿Cuál es la recta que pasa por ") + parHTML(c.x1, c.y1) + T(" and ", " y ") + parHTML(c.x2, c.y2) + "?" :
      T("Which is the line with slope ", "¿Cuál es la recta de pendiente ") + fTxt(c.m) + T(" through ", " que pasa por ") + parHTML(c.x1, c.y1) + "?"),
    correcta: eq, opciones: opsEq(eq, malos),
    pista: (c.dos ? T("Find the slope first. ", "Calcule primero la pendiente. ") : "") + T("Then use y − y₁ = m(x − x₁), distribute, and solve for y. Check: the point must make the equation true.", "Después use y − y₁ = m(x − x₁), distribuya y despeje y. Compruebe: el punto debe cumplir la ecuación."),
    bien: eqHTML(eq) + T(". Check: ", ". Comprobación: ") + fTxt(c.m) + " · " + pn(c.x1) + " " + (c.b.n < 0 ? "− " + fTxt(fneg(c.b)) : "+ " + fTxt(c.b)) + " = " + sg(c.y1) + "."};
});

/* ===== MODULE 3 · Converting ===== */
function casoForma(tipo){
  var m, b, e, pasos = [], enun, res;
  if (tipo === "si-std"){
    m = elige([F(2), F(-3), F(4), F(1, 2), F(-2, 3), F(3, 4), F(-1), F(5)]); b = F(aleatorio(-6, 6)); if (b.n === 0) b = F(3);
    e = estandar(m, b);
    enun = T("Change ", "Convierta ") + eqHTML(eqSI(m, b)) + T(" to standard form.", " a la forma estándar.");
    pasos.push(T("Move the x-term to the left side: ", "Se pasa el término con x al lado izquierdo: ") + eqHTML(coefX(fneg(m)) + " + y = " + fTxt(b)) + ".");
    var k = m.d;
    if (k > 1) pasos.push(T("Multiply everything by ", "Se multiplica todo por ") + k + T(" to clear the fraction: ", " para quitar la fracción: ") + eqHTML(eqStd({A: -m.n, B: k, C: b.n * k})) + ".");
    if (-m.n < 0) pasos.push(T("Multiply by −1 so that A is positive: ", "Se multiplica por −1 para que A sea positivo: ") + eqHTML(eqStd(e)) + ".");
    pasos.push(T("Standard form: ", "Forma estándar: ") + "<strong>" + eqHTML(eqStd(e)) + "</strong>.");
    res = eqStd(e);
  } else if (tipo === "std-si"){
    var A = elige([1, 2, 3, 4, 5, 6]), Bv = elige([1, 2, 3, -1, -2, -3]), C = elige([-12, -6, 4, 6, 8, 12, 9, 10]); e = {A: A, B: Bv, C: C};
    m = F(-A, Bv); b = F(C, Bv);
    enun = T("Change ", "Convierta ") + eqHTML(eqStd(e)) + T(" to slope-intercept form.", " a la forma pendiente-intercepto.");
    pasos.push(T("Leave the y-term alone (move the x-term to the right): ", "Se deja solo el término con y (el término con x pasa a la derecha): ") + eqHTML((Bv === 1 ? "" : Bv === -1 ? "−" : sg(Bv)) + "y = " + coefX(F(-A)) + constTxt(F(C))) + ".");
    if (Bv !== 1) pasos.push(T("Divide every term by ", "Se divide cada término entre ") + pn(Bv) + ": " + eqHTML(eqSI(m, b)) + ".");
    pasos.push(T("Slope ", "Pendiente ") + fTxt(m) + T(", intercept ", ", intercepto ") + fTxt(b) + ": <strong>" + eqHTML(eqSI(m, b)) + "</strong>.");
    res = eqSI(m, b);
  } else {
    m = elige([F(2), F(-3), F(4), F(-1), F(1, 2), F(-1, 2)]); var x1 = m.d === 2 ? elige([-4, -2, 2, 4]) : aleatorio(-4, 4), y1 = aleatorio(-5, 5); if (!x1) x1 = 2;
    b = fsum(F(y1), fmul(fneg(m), F(x1)));
    enun = T("Change ", "Convierta ") + eqHTML(eqPS(m, F(x1), F(y1))) + T(" to slope-intercept form.", " a la forma pendiente-intercepto.");
    pasos.push(T("Distribute: ", "Se distribuye: ") + eqHTML(restaTxt("y", F(y1)) + " = " + coefX(m) + constTxt(fneg(fmul(m, F(x1))))) + ".");
    pasos.push(T("Solve for y: ", "Se despeja y: ") + "<strong>" + eqHTML(eqSI(m, b)) + "</strong>.");
    res = eqSI(m, b);
  }
  return {enun: enun, pasos: pasos, res: res, m: m, b: b, tipo: tipo};
}
pasoAPaso4("fc", function(){ var c = casoForma(elige(["si-std", "std-si", "ps-si"])); return {enun: c.enun, pasos: c.pasos}; });
OMR("fq", function(){
  var c = casoForma(elige(["si-std", "std-si", "std-si", "ps-si"])), malos;
  if (c.tipo === "si-std"){ var e = estandar(c.m, c.b); malos = [eqStd({A: e.A, B: e.B, C: -e.C}), eqStd({A: e.A, B: -e.B, C: e.C}), eqStd({A: -e.A, B: e.B, C: e.C})]; }
  else { malos = [eqSI(fneg(c.m), c.b), eqSI(c.m, fneg(c.b)), eqSI(fneg(c.m), fneg(c.b))]; }
  return {enun: c.enun.replace(T("Change ", "Convierta "), T("Which is ", "¿Cuál es ")).replace(T(" to standard form.", " a la forma estándar."), T(" in standard form?", " en forma estándar?")).replace(T(" to slope-intercept form.", " a la forma pendiente-intercepto."), T(" in slope-intercept form?", " en forma pendiente-intercepto?")),
    correcta: c.res, opciones: opsEq(c.res, malos),
    pista: T("Do one step at a time and watch the signs when a term changes sides. Check with a value of x: both forms must give the same y.", "Haga un paso a la vez y cuide los signos cuando un término cambia de lado. Compruebe con un valor de x: las dos formas deben dar la misma y."),
    bien: c.pasos.map(function(p){ return p.replace(/<strong>|<\/strong>/g, ""); }).join(" ")};
});

/* ===== MODULE 4 · Parallel and perpendicular ===== */
var PARES = [[F(2), F(1), F(2), F(-4)], [F(2), F(1), F(-1, 2), F(3)], [F(3), F(-2), F(1, 3), F(1)], [F(-2, 5), F(1), F(5, 2), F(-3)], [F(4), F(0), F(4), F(5)], [F(1), F(2), F(-1), F(2)]];
function relacion(m1, m2){ if (figual(m1, m2)) return "par"; if (figual(fmul(m1, m2), F(-1))) return "perp"; return "nin"; }
var NOMREL = {par: T("parallel", "paralelas"), perp: T("perpendicular", "perpendiculares"), nin: T("neither parallel nor perpendicular", "ni paralelas ni perpendiculares")};
function prPinta(){
  var q = PARES[+$("pa-par").value], e1 = eqSI(q[0], q[1]), e2 = eqSI(q[2], q[3]), r = relacion(q[0], q[2]);
  $("pa-svg").innerHTML = grafRecta([{m: q[0], b: q[1], color: C4.azul}, {m: q[2], b: q[3], color: "#e65100"}], [], T("The lines ", "Las rectas ") + vozEq(e1) + T(" (blue) and ", " (azul) y ") + vozEq(e2) + T(" (orange).", " (naranja)."), 420);
  $("pa-res").innerHTML = '<div class="linea"><span style="color:' + C4.azul + ';font-weight:700">' + eqHTML(e1) + "</span> → m₁ = " + fTxt(q[0]) + "</div>" +
    '<div class="linea"><span style="color:#e65100;font-weight:700">' + eqHTML(e2) + "</span> → m₂ = " + fTxt(q[2]) + "</div>" +
    '<div class="linea veredicto">' + (r === "par" ? T("The slopes are equal: the lines are parallel.", "Las pendientes son iguales: las rectas son paralelas.") :
      "m₁ × m₂ = " + fTxt(q[0]) + " × " + pnF(q[2]) + " = " + fTxt(fmul(q[0], q[2])) + (r === "perp" ? T(": the lines are perpendicular.", ": las rectas son perpendiculares.") : T(", not −1, and the slopes are different: neither parallel nor perpendicular.", ", no −1, y las pendientes son distintas: ni paralelas ni perpendiculares.") + (figual(q[2], fdiv(F(1), q[0])) ? " " + T("(The fraction was flipped, but the sign was not changed.)", "(Se invirtió la fracción, pero no se cambió el signo.)") : ""))) + "</div>";
}
$("pa-par").addEventListener("change", prPinta); prPinta();
function rcCalcula(){
  var n = leeEntero($("rc-n").value), d = leeEntero($("rc-d").value), o = $("rc-res");
  if (n === null || d === null || d === 0){ o.innerHTML = '<div class="linea">' + T("Type a whole number in each box; the bottom cannot be 0.", "Escriba un número entero en cada casilla; el denominador no puede ser 0.") + "</div>"; return; }
  var m = F(n, d);
  if (m.n === 0){ o.innerHTML = '<div class="linea">' + T("m = 0 is a horizontal line. Its perpendicular is a vertical line, whose slope is undefined.", "m = 0 es una recta horizontal. Su perpendicular es una recta vertical, de pendiente indefinida.") + "</div>"; return; }
  var inv = F(m.d, m.n), p = fneg(inv);
  o.innerHTML = '<div class="linea">m = ' + fracHTML(m.n, m.d) + "</div>" +
    '<div class="linea">1 · ' + T("Flip the fraction: ", "Se invierte la fracción: ") + fracHTML(inv.n, inv.d) + "</div>" +
    '<div class="linea">2 · ' + T("Change the sign: ", "Se cambia el signo: ") + fracHTML(p.n, p.d) + "</div>" +
    '<div class="linea veredicto">' + T("Perpendicular slope: ", "Pendiente perpendicular: ") + fracHTML(p.n, p.d) + T(". Check: ", ". Comprobación: ") + fTxt(m) + " × " + pnF(p) + " = −1.</div>";
}
["rc-n", "rc-d"].forEach(function(i){ $(i).addEventListener("input", rcCalcula); }); rcCalcula();
OMR("pa", function(){
  var r = Math.random(), m1 = elige(PEND.filter(function(x){ return x.n !== 0; })), recip = F(m1.d, m1.n), perp = fneg(recip);
  if (r < 0.35){
    var k = elige(["par", "perp", "nin", "nin2"]), m2 = k === "par" ? m1 : (k === "perp" ? perp : (k === "nin" ? recip : fneg(m1))), b1 = F(aleatorio(-5, 5)), b2 = F(aleatorio(-5, 5));
    if (k === "par" && figual(b1, b2)) b2 = fsum(b2, F(2));
    var rel = relacion(m1, m2);
    return {enun: T("How are ", "¿Qué relación tienen ") + eqHTML(eqSI(m1, b1)) + T(" and ", " y ") + eqHTML(eqSI(m2, b2)) + T(" related?", "?"), correcta: rel, enOrden: true,
      opciones: [{clave: "par", html: T("Parallel", "Paralelas")}, {clave: "perp", html: T("Perpendicular", "Perpendiculares")}, {clave: "nin", html: T("Neither", "Ninguna de las dos")}],
      pista: T("Compare the slopes. Equal: parallel. Product −1: perpendicular.", "Compare las pendientes. Iguales: paralelas. Producto −1: perpendiculares."), bien: "m₁ = " + fTxt(m1) + ", m₂ = " + fTxt(m2) + ": " + NOMREL[rel] + "."};
  }
  if (r < 0.7){
    var quiere = Math.random() < 0.5 ? "perp" : "par", ok = quiere === "perp" ? perp : m1;
    var ops = [m1, perp, recip, fneg(m1)].filter(function(x, i, a){ return a.findIndex(function(y){ return figual(x, y); }) === i; });
    return {enun: T("What is the slope of a line ", "¿Cuál es la pendiente de una recta ") + (quiere === "perp" ? T("perpendicular", "perpendicular") : T("parallel", "paralela")) + T(" to ", " a ") + eqHTML(eqSI(m1, F(aleatorio(-5, 5)))) + "?", correcta: fTxt(ok),
      opciones: ops.map(function(x){ return {clave: fTxt(x), html: fracHTML(x.n, x.d)}; }),
      porClave: (function(){ var o = {}; o[fTxt(recip)] = T("You flipped it, but you also need to change the sign.", "La invirtió, pero falta cambiar el signo."); o[fTxt(fneg(m1))] = T("You changed the sign, but you also need to flip it.", "Cambió el signo, pero falta invertirla."); return o; })(),
      pista: quiere === "perp" ? T("Perpendicular: flip the fraction and change the sign.", "Perpendicular: se invierte la fracción y se cambia el signo.") : T("Parallel: the same slope, sign included.", "Paralela: la misma pendiente, con su signo."), bien: fTxt(ok) + "."};
  }
  var quiere2 = Math.random() < 0.5 ? "perp" : "par", mm = quiere2 === "perp" ? perp : m1, x1 = mm.d === 1 ? aleatorio(-3, 3) : mm.d * elige([-1, 1]), y1 = aleatorio(-4, 4), bb = fsum(F(y1), fmul(fneg(mm), F(x1))), eq = eqSI(mm, bb);
  var malos = [eqSI(quiere2 === "perp" ? m1 : perp, bb), eqSI(mm, F(y1)), eqSI(quiere2 === "perp" ? recip : fneg(m1), bb)];
  return {enun: T("Which line is ", "¿Qué recta es ") + (quiere2 === "perp" ? T("perpendicular", "perpendicular") : T("parallel", "paralela")) + T(" to ", " a ") + eqHTML(eqSI(m1, F(aleatorio(-5, 5)))) + T(" and goes through ", " y pasa por ") + parHTML(x1, y1) + "?", correcta: eq,
    opciones: opsEq(eq, malos),
    pista: T("First the slope (", "Primero la pendiente (") + (quiere2 === "perp" ? T("flip and change the sign", "se invierte y se cambia el signo") : T("the same one", "la misma")) + T("), then use the point in y − y₁ = m(x − x₁).", "), después use el punto en y − y₁ = m(x − x₁)."), bien: "m = " + fTxt(mm) + ": " + eqHTML(eq) + "."};
});
'''

def practica_pagina():
    n = N
    def pasos(pre, otro):
        return f'''      <div class="panel"><p class="enun" id="{pre}-enun"></p>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig">{t("Show the next step", "Mostrar el siguiente paso")}</button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="{pre}-nuevo">{otro}</button></div></div>
      <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>'''
    pend = ["−3", "−2", "−3/2", "−1", "−2/3", "−1/2", "0", "1/2", "2/3", "1", "3/2", "2", "3"]
    mods = [
     (t("slope-intercept", "pendiente-intercepto"), t("The slope-intercept form: y = mx + b", "La forma pendiente-intercepto: y = mx + b"),
      f'''      <p>{t("In y = mx + b the two numbers tell you everything about the line: m is the slope (how much it goes up or down for each unit to the right) and b is the y-intercept, the point (0, b) where it crosses the vertical axis. Move both and watch.", "En y = mx + b los dos números dicen todo lo que hay que saber de la recta: m es la pendiente (cuánto sube o baja por cada unidad hacia la derecha) y b es el intercepto en y, el punto (0, b) por donde cruza el eje vertical. Mueva los dos y obsérvelo.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo" style="flex:1;min-width:220px;"><label for="si-m">{t("Slope", "Pendiente")} m = <span id="si-mv"></span></label><input type="range" id="si-m" min="0" max="{len(pend) - 1}" step="1" value="11" aria-describedby="si-mlista"><span class="sr-only" id="si-mlista">{t("Slopes from −3 to 3: ", "Pendientes de −3 a 3: ")}{", ".join(pend)}</span></div>
        <div class="campo" style="flex:1;min-width:220px;"><label for="si-b">{t("Intercept", "Intercepto")} b = <span id="si-bv"></span></label><input type="range" id="si-b" min="-6" max="6" step="1" value="1"></div></div></div>
      <div id="si-svg"></div>
{n4.salida("si-eq")}
{B.om("sq", t("Practice: slope and intercept", "Practique: pendiente e intercepto"))}'''),
     (t("point-slope", "punto-pendiente"), t("The point-slope form", "La forma punto-pendiente"),
      f'''      <p>{t("When the known point is not the intercept, start with the point-slope form, which works with any point of the line:", "Cuando el punto conocido no es el intercepto, conviene empezar por la forma punto-pendiente, que admite cualquier punto de la recta:")}</p>
{n4.formula("y − y₁ = m(x − x₁)")}
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos("ps", t("Another case", "Otro caso"))}
      <div id="ps-svg"></div>
      <div class="caja-tip">{t("With two points, the slope comes first: the point-slope form needs a value of m, so step zero is always (y₂ − y₁) ÷ (x₂ − x₁). It does not matter which of the two points you use next: you get the same line.", "Con dos puntos, primero la pendiente: la forma punto-pendiente necesita un valor de m, así que el paso cero siempre es (y₂ − y₁) ÷ (x₂ − x₁). Da igual cuál de los dos puntos se use después: la recta que sale es la misma.")}</div>
{B.om("pq", t("Practice: write the equation", "Practique: escriba la ecuación"))}'''),
     (t("forms", "formas"), t("Changing between the three forms", "Convertir entre las tres formas"),
      f'''      <p>{t("The three forms describe the same line; only the outfit changes. It pays to know how to go from one to another, because each one is good for something different.", "Las tres formas describen la misma recta; cambia solo el traje. Conviene saber pasar de una a otra, porque cada una sirve para algo distinto.")}</p>
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("The three forms and what each one is for", "Las tres formas y para qué sirve cada una")}</caption>
        <thead><tr><th scope="col">{t("Form", "Forma")}</th><th scope="col">{t("Expression", "Expresión")}</th><th scope="col">{t("When to use it", "Cuándo conviene")}</th></tr></thead><tbody>
        <tr><td>{t("Slope-intercept", "Pendiente-intercepto")}</td><td>y = mx + b</td><td>{t("To graph: m and b can be read at a glance.", "Para graficar: m y b se leen de un vistazo.")}</td></tr>
        <tr><td>{t("Point-slope", "Punto-pendiente")}</td><td>y − y₁ = m(x − x₁)</td><td>{t("To write the line from any point.", "Para escribir la recta desde un punto cualquiera.")}</td></tr>
        <tr><td>{t("Standard", "Estándar")}</td><td>Ax + By = C</td><td>{t("A common GED format, and the form for systems of equations.", "Formato habitual del GED y de los sistemas de ecuaciones.")}</td></tr></tbody></table></div>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos("fc", t("Another conversion", "Otra conversión"))}
      <div class="caja-tip">{t("A check that never fails: choose a value of x, for example x = 2, and evaluate both forms. If both give the same y, the conversion is right.", "Comprobación que nunca falla: elija un valor de x, por ejemplo x = 2, y evalúe las dos formas. Si ambas dan la misma y, la conversión está bien hecha.")}</div>
{B.om("fq", t("Practice: change the equation", "Practique: convierta la ecuación"))}'''),
     (t("parallel", "paralelas"), t("Parallel and perpendicular lines", "Rectas paralelas y perpendiculares"),
      f'''      <p>{t("You decide how two lines are related by looking only at the slopes: equal means parallel; negative reciprocals (their product is −1) mean perpendicular.", "La relación entre dos rectas se decide mirando solo las pendientes: iguales quiere decir paralelas; recíprocas negativas (producto igual a −1) quiere decir perpendiculares.")}</p>
      <div class="panel"><div class="campos">{n4.lista("pa-par", t("Pair of lines", "Par de rectas"), [("0", "y = 2x + 1 · y = 2x − 4"), ("1", "y = 2x + 1 · y = −(1/2)x + 3"), ("2", "y = 3x − 2 · y = (1/3)x + 1"), ("3", "y = −(2/5)x + 1 · y = (5/2)x − 3"), ("4", "y = 4x · y = 4x + 5"), ("5", "y = x + 2 · y = −x + 2")])}</div></div>
      <div id="pa-svg"></div>
{n4.salida("pa-res")}
      <h3>{t("Negative-reciprocal calculator", "Calculadora de la recíproca negativa")}</h3>
      <p>{t("Type a slope as a fraction and get the perpendicular slope. For a whole number, leave the bottom as 1.", "Escriba una pendiente como fracción y obtenga la perpendicular. Para un número entero, deje el denominador en 1.")}</p>
      <div class="panel"><div class="campos"><div class="campo"><label for="rc-n">{t("Top of m (numerator)", "Numerador de m")}</label><input type="text" inputmode="numeric" class="corto" id="rc-n" value="2"></div><div class="campo"><label for="rc-d">{t("Bottom of m (denominator)", "Denominador de m")}</label><input type="text" inputmode="numeric" class="corto" id="rc-d" value="3"></div></div></div>
{n4.salida("rc-res")}
      <div class="caja-atencion"><strong>{t("Two moves, not one.", "Dos movimientos, no uno.")}</strong> {t("The perpendicular slope comes from flipping the fraction and changing the sign. Stopping halfway (flipping without changing the sign) is the most common mistake here.", "La perpendicular se halla invirtiendo la fracción y cambiando el signo. Quedarse a medio camino (invertir sin cambiar el signo) es el error más frecuente de esta sección.")}</div>
{B.om("pa", t("Practice: parallel and perpendicular", "Practique: paralelas y perpendiculares"))}''')]
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO + "\n  .eq{white-space:nowrap;}", scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Ecuaciones de la recta: pendiente-intercepto, punto-pendiente y forma estándar")
