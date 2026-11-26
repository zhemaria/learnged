"""Level 4 · Lesson 7.3 · Average rate of change and kinds of functions — builds the lesson and its practice page in English and in
Spanish. Sources (GEDparaHispanos): clase_mate4/leccion_7-3.html and algebra/n4-l7-3.html (the average rate of change with the secant
line, six situations read with their units, and the pattern detector for tables). They are rebuilt here, inside LearnGED, with
math/func4.js and math/poly4.js; all units are U.S. customary. Then run tools/ged_standards.py, tools/ged_standards_es.py and
tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "7-3"
TEMA = ("Systems of inequalities and functions", "Sistemas de desigualdades y funciones")
TIT = ("Average rate of change and kinds of functions", "Tasa de cambio promedio e identificar tipos de funciones")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js", "/math/func4.js")
ESTILO = n4.ESTILO + """
  .tabla-lados.centro td,.tabla-lados.centro th{text-align:center;}
  .tabla-lados td.cte{background:#e8f5e9;color:#1b5e20;font-weight:700;}
"""

def fig_secante():
    p = n4.Plano(-1, 7, -1, 10, 30, paso=1)
    pts = [(x / 20, (x / 20) ** 2) for x in range(-20, 64)]
    for a, b in zip(pts, pts[1:]):
        p.seg(a, b, "#1565c0", 3.5)
    p.seg((0.5, -1), (3.25, 10), "#c62828", 2.5)
    p.seg((1, 1), (3, 1), "#2e7d32", 2.5, "6 5").seg((3, 1), (3, 9), "#2e7d32", 2.5, "6 5")
    p.texto((2.5, 1), "Δx = 2", "#2e7d32", 13, "middle", 0, -9).texto((3, 5), "Δy = 8", "#2e7d32", 13, "start", 8, 0)
    p.punto((1, 1), "#263238", "(1, 1)", "se").punto((3, 9), "#263238", "(3, 9)", "nw")
    p.texto((6.9, 3.6), t("rate = 8/2 = 4", "tasa = 8/2 = 4"), "#c62828", 14, "end", 0, 0)
    p.texto((6.9, 8.3), "f(x) = x²", "#1565c0", 14, "end", 0, 0)
    return p.svg(t("The graph of f of x = x squared with the points 1, 1 and 3, 9 joined by a red secant line. From x = 1 to x = 3, x changes by 2 and y changes by 8, so the average rate of change is 8 divided by 2, which is 4: the slope of the secant line.",
                   "Gráfica de f de x = x al cuadrado con los puntos 1, 1 y 3, 9 unidos por una recta secante roja. De x = 1 a x = 3, x cambia 2 e y cambia 8, así que la tasa de cambio promedio es 8 entre 2, que es 4: la pendiente de la recta secante."), 340)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 7.2.</strong> In Lesson 7.2 you learned what a function is and how to evaluate f(x). Now you study how a function <strong>changes</strong>: how fast it goes up or down between two points. That measure is the <strong>average rate of change</strong>, and its pattern reveals the kind of function.", "<strong>Conexión con la lección anterior.</strong> En la Lección 7.2 se aprendió qué es una función y a evaluar f(x). Ahora se estudia cómo <strong>cambia</strong> una función: qué tan rápido sube o baja entre dos puntos. Esa medida es la <strong>tasa de cambio promedio</strong>, y su patrón revela el tipo de función.")}</p>
<p>{t("The average rate of change of a function on the interval from x = a to x = b measures how much the output changes for each unit of input. It is the slope between the points (a, f(a)) and (b, f(b)).", "La tasa de cambio promedio de una función en el intervalo de x = a a x = b mide cuánto cambia la salida por cada unidad de entrada. Es, en esencia, la pendiente entre los puntos (a, f(a)) y (b, f(b)).")}</p>
{n4.formula(t("rate = (f(b) − f(a)) / (b − a)", "tasa = (f(b) − f(a)) / (b − a)"))}
{fig_secante()}
<p>{t("In the graph, Δx (read “delta x”) means the change in x and Δy the change in y. From (1, 1) to (3, 9), Δy / Δx = 8 / 2 = 4.", "En la gráfica, Δx (se lee «delta x») significa el cambio en x, y Δy, el cambio en y. De (1, 1) a (3, 9), Δy / Δx = 8 / 2 = 4.")}</p>
{ejemplo(t("Example 1: if f(2) = 10 and f(5) = 25, what is the average rate of change on [2, 5]?", "Ejemplo 1 · Si f(2) = 10 y f(5) = 25, ¿cuál es la tasa de cambio promedio en [2, 5]?"),
  [("1", t("Use the formula:", "Se aplica la fórmula:"), "(25 − 10) / (5 − 2)."), ("2", t("Compute:", "Se calcula:"), "15 / 3 = 5."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>On average, the function goes up 5 units for each unit of x.</strong>", "<strong>La función crece, en promedio, 5 unidades por cada unidad de x.</strong>"))])}
{caja("tip", t("Rate of change = slope", "Tasa de cambio = pendiente"), t("<p>Finding the average rate of change between two points is exactly the same as finding the slope of the line that joins them (the secant line). In a linear function, that rate is the same on every interval.</p>", "<p>Calcular la tasa de cambio promedio entre dos puntos es exactamente lo mismo que calcular la pendiente de la recta que los une (la recta secante). En una función lineal, esa tasa es la misma en todo intervalo.</p>"))}
{practica("p1", t("Practice 1 — Find the rate", "Práctica 1 — Calcular la tasa"), t("f(1) = 3 and f(4) = 12. The average rate of change is:", "f(1) = 3 y f(4) = 12. Tasa de cambio promedio:"), [("a", "9"), ("b", "3"), ("c", "4")])}
{practica("p2", t("Practice 2 — The same height", "Práctica 2 — La misma altura"), t("f(0) = 5 and f(2) = 5. The average rate of change is:", "f(0) = 5 y f(2) = 5. Tasa de cambio promedio:"), [("a", "5"), ("b", "2"), ("c", "0")])}
{practica("p3", t("Practice 3 — Another interval", "Práctica 3 — Otro intervalo"), t("f(2) = 8 and f(6) = 20. The average rate of change is:", "f(2) = 8 y f(6) = 20. Tasa de cambio promedio:"), [("a", "3"), ("b", "12"), ("c", "4")])}
{enlace(n, t("rate", "tasa"), t("the average rate of change", "la tasa de cambio promedio"), t("Choose a function and the two ends of the interval: the change in y over the change in x, with the secant line drawn between the two points.", "Elija una función y los dos extremos del intervalo: el cambio en y entre el cambio en x, con la recta secante dibujada entre los dos puntos."))}'''

    s2 = f'''<p>{t("The average rate of change makes sense with <strong>units</strong>: dollars per year, feet per second, people per month. The unit is always “unit of output per unit of input.”", "La tasa de cambio promedio cobra sentido con <strong>unidades</strong>: dólares por año, pies por segundo, personas por mes. La unidad es siempre «unidad de salida por unidad de entrada».")}</p>
{ejemplo(t("Example 2: a savings account goes from $100 to $160 in 3 years. What is the average rate of change?", "Ejemplo 2 · Una cuenta de ahorro pasa de $100 a $160 en 3 años. ¿Cuál es la tasa de cambio promedio?"),
  [("1", t("Change in the money:", "Cambio en el dinero:"), t("160 − 100 = 60 dollars.", "160 − 100 = 60 dólares.")), ("2", t("In 3 years:", "En 3 años:"), "60 / 3 = 20."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>On average, the account grows $20 per year.</strong>", "<strong>La cuenta crece, en promedio, $20 por año.</strong>"))])}
{caja("ojo", t("A negative rate", "Una tasa negativa"), t("<p>Always take the final value minus the starting value. If the quantity goes down, the rate is negative: a tank that goes from 400 to 100 gallons in 6 hours changes at −50 gallons per hour. The minus sign is not a mistake: it says the quantity decreases.</p>", "<p>Siempre se resta el valor final menos el inicial. Si la cantidad baja, la tasa es negativa: un tanque que pasa de 400 a 100 galones en 6 horas cambia a −50 galones por hora. El signo menos no es un error: avisa de que la cantidad disminuye.</p>"))}
{practica("p4", t("Practice 4 — Savings", "Práctica 4 — Ahorro"), t("An account goes from $200 to $260 in 3 years. The rate is:", "Una cuenta pasa de $200 a $260 en 3 años. La tasa es:"), [("a", t("$20 per year", "$20 por año")), ("b", t("$60 per year", "$60 por año")), ("c", t("$260 per year", "$260 por año"))])}
{practica("p5", t("Practice 5 — Speed", "Práctica 5 — Velocidad"), t("A car goes from 0 to 150 feet in 5 seconds. The rate is:", "Un auto recorre de 0 a 150 pies en 5 segundos. La tasa es:"), [("a", t("150 ft/s", "150 pies/s")), ("b", t("30 ft/s", "30 pies/s")), ("c", t("5 ft/s", "5 pies/s"))])}
{practica("p6", t("Practice 6 — The unit", "Práctica 6 — La unidad"), t("The average rate of change is measured in:", "La tasa de cambio promedio se mide en:"), [("a", t("dollars only", "solo dólares")), ("b", t("feet only", "solo pies")), ("c", t("units of output per unit of input", "unidades de salida por unidad de entrada"))])}
{enlace(n, t("context", "contexto"), t("reading the rate with units", "la interpretación con unidades"), t("Six situations solved step by step (savings, speed, a tank that drains, population, a bill, and temperature), including negative rates.", "Seis situaciones resueltas paso a paso (ahorro, velocidad, un tanque que se vacía, población, factura y temperatura), incluidas las tasas negativas."))}'''

    s3 = f'''<p>{t("The pattern of the outputs reveals the kind of function. Look at the differences or the ratios between consecutive values (with equally spaced inputs):", "El patrón de los valores de salida revela el tipo de función. Conviene mirar las diferencias o las razones entre valores consecutivos (con entradas igualmente espaciadas):")}</p>
{tabla(t("The pattern of each kind", "El patrón de cada tipo"), t("The pattern of the outputs that identifies each kind of function", "Patrón de salida que identifica cada tipo de función"), [t("Kind", "Tipo"), t("Pattern in the table", "Patrón en la tabla"), t("Example outputs", "Ejemplo de salidas")],
  [[t("Linear", "Lineal"), t("Constant difference (adds the same)", "Diferencia constante (suma lo mismo)"), "2, 5, 8, 11 (+3)"], [t("Quadratic", "Cuadrática"), t("Constant second difference", "Segunda diferencia constante"), t("0, 1, 4, 9 (differences 1, 3, 5)", "0, 1, 4, 9 (dif.: 1, 3, 5)")], [t("Exponential", "Exponencial"), t("Constant ratio (multiplies by the same)", "Razón constante (multiplica lo mismo)"), "1, 2, 4, 8 (×2)"]])}
{caja("tip", t("Adds the same or multiplies by the same", "Suma constante o producto constante"), t("<p>If to go from one value to the next you always add the same amount, the function is linear; if you always multiply by the same number, it is exponential; if the second difference is constant, it is quadratic.</p>", "<p>Si para pasar de un valor al siguiente se suma siempre lo mismo, es lineal; si se multiplica siempre por lo mismo, es exponencial; si la segunda diferencia es constante, es cuadrática.</p>"))}
{practica("p7", t("Practice 7 — Adds 3", "Práctica 7 — Suma 3"), t("Outputs: 2, 5, 8, 11 (add 3 each time). The function is:", "Salidas: 2, 5, 8, 11 (se suma 3 cada vez). La función es:"), [("a", t("quadratic", "cuadrática")), ("b", t("linear", "lineal")), ("c", t("exponential", "exponencial"))])}
{practica("p8", t("Practice 8 — Times 2", "Práctica 8 — Por 2"), t("Outputs: 1, 2, 4, 8 (multiply by 2 each time). The function is:", "Salidas: 1, 2, 4, 8 (se multiplica por 2 cada vez). La función es:"), [("a", t("exponential", "exponencial")), ("b", t("linear", "lineal")), ("c", t("quadratic", "cuadrática"))])}
{practica("p9", t("Practice 9 — Second difference", "Práctica 9 — Segunda diferencia"), t("Outputs: 0, 1, 4, 9 (constant second difference). The function is:", "Salidas: 0, 1, 4, 9 (segunda diferencia constante). La función es:"), [("a", t("linear", "lineal")), ("b", t("exponential", "exponencial")), ("c", t("quadratic", "cuadrática"))])}
{enlace(n, t("kind", "tipo"), t("identifying the kind of function", "la identificación del tipo de función"), t("A pattern detector: it finds the differences, the second differences, and the ratios, marks the constant column, and accepts tables you type yourself.", "Detector de patrones: calcula diferencias, segundas diferencias y razones, resalta la columna constante y admite tablas escritas por usted."))}'''

    secciones = [("s-" + t("rate", "tasa"), t("The average rate of change", "La tasa de cambio promedio"), s1),
                 ("s-" + t("context", "contexto"), t("Reading the rate in context", "Interpretar la tasa en contexto"), s2),
                 ("s-" + t("kind", "tipo"), t("Identifying the kind of function", "Identificar el tipo de función"), s3)]

    lesson = {"next": t("Lesson 8.1", "Lección 8.1"), "review": t("sections 1 and 3", "las secciones 1 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("9 is the change in y; divide it by the change in x, 3.", "9 es el cambio en y; divídalo entre el cambio en x, 3."), "c": t("Change in y: 12 − 3 = 9. Change in x: 4 − 1 = 3.", "Cambio en y: 12 − 3 = 9. Cambio en x: 4 − 1 = 3.")}, "right": "9 / 3 = 3.", "solution": "3."},
      "p2": {"ok": "c", "hints": {"a": t("5 is the height, not the change: 5 − 5 = 0.", "5 es la altura, no el cambio: 5 − 5 = 0."), "b": t("2 is the change in x. The output did not change.", "2 es el cambio en x. La salida no cambió.")}, "right": "0 / 2 = 0.", "solution": "0."},
      "p3": {"ok": "a", "hints": {"b": t("12 is the change in y; divide it by 4.", "12 es el cambio en y; divídalo entre 4."), "c": t("4 is the change in x. Divide 12 by it.", "4 es el cambio en x. Divida 12 entre él.")}, "right": "(20 − 8) / (6 − 2) = 12 / 4 = 3.", "solution": "3."},
      "p4": {"ok": "a", "hints": {"b": t("$60 is the total change; divide it by 3 years.", "$60 es el cambio total; divídalo entre 3 años."), "c": t("$260 is the final amount, not the change.", "$260 es la cantidad final, no el cambio.")}, "right": t("60 / 3 = $20 per year.", "60 / 3 = $20 por año."), "solution": t("$20 per year.", "$20 por año.")},
      "p5": {"ok": "b", "hints": {"a": t("150 feet is the total distance; divide it by 5 seconds.", "150 pies es la distancia total; divídala entre 5 segundos."), "c": t("5 is the time. Divide 150 by 5.", "5 es el tiempo. Divida 150 entre 5.")}, "right": t("150 / 5 = 30 ft/s.", "150 / 5 = 30 pies/s."), "solution": t("30 ft/s.", "30 pies/s.")},
      "p6": {"ok": "c", "hints": {"a": t("It depends on the situation: dollars, feet, people…", "Depende de la situación: dólares, pies, personas…"), "b": t("It depends on the situation: dollars, feet, people…", "Depende de la situación: dólares, pies, personas…")}, "right": t("Output per input.", "Salida por entrada."), "solution": t("Units of output per unit of input.", "Unidades de salida por unidad de entrada.")},
      "p7": {"ok": "b", "hints": {"a": t("Quadratic has a constant SECOND difference.", "La cuadrática tiene constante la SEGUNDA diferencia."), "c": t("Exponential multiplies; this one adds.", "La exponencial multiplica; esta suma.")}, "right": t("It adds the same: linear.", "Suma lo mismo: lineal."), "solution": t("Linear.", "Lineal.")},
      "p8": {"ok": "a", "hints": {"b": t("Linear adds the same; this one multiplies.", "La lineal suma lo mismo; esta multiplica."), "c": t("The differences 1, 2, 4 are not a quadratic pattern: the ratio is constant.", "Las diferencias 1, 2, 4 no son patrón cuadrático: la razón es constante.")}, "right": t("It multiplies by the same: exponential.", "Multiplica por lo mismo: exponencial."), "solution": t("Exponential.", "Exponencial.")},
      "p9": {"ok": "c", "hints": {"a": t("The first differences 1, 3, 5 are not constant.", "Las primeras diferencias 1, 3, 5 no son constantes."), "b": t("The ratios are not constant (1 to 4 is ×4, 4 to 9 is ×2.25).", "Las razones no son constantes (de 1 a 4 es ×4, de 4 a 9 es ×2.25).")}, "right": t("Constant second difference: quadratic.", "Segunda diferencia constante: cuadrática."), "solution": t("Quadratic.", "Cuadrática.")},
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("15 is the change in y; divide it by 3.", "15 es el cambio en y; divídalo entre 3."), "b": t("3 is the change in x.", "3 es el cambio en x."), "c": t("Subtract the outputs, do not add them.", "Reste las salidas, no las sume.")}, "solution": "(25 − 10) / (5 − 2) = 5."},
      "B": {"ok": "c", "hints": {"a": t("7 is the height, not the change.", "7 es la altura, no el cambio."), "b": t("Subtract the outputs: 7 − 7.", "Reste las salidas: 7 − 7."), "d": t("2 is the change in x.", "2 es el cambio en x.")}, "solution": "0 / 2 = 0."},
      "C": {"ok": "b", "hints": {"a": t("The output goes down: the rate is negative.", "La salida baja: la tasa es negativa."), "c": t("9 is the size of the change in y; divide by 3.", "9 es el tamaño del cambio en y; divida entre 3."), "d": t("Divide −9 by the change in x, 3.", "Divida −9 entre el cambio en x, 3.")}, "solution": "(3 − 12) / (6 − 3) = −9 / 3 = −3."},
      "D": {"ok": "c", "hints": {"a": t("Quadratic has a constant second difference.", "La cuadrática tiene constante la segunda diferencia."), "b": t("Exponential multiplies by the same number.", "La exponencial multiplica por lo mismo."), "d": t("Rational has x in a denominator.", "La racional tiene x en un denominador.")}, "solution": t("Linear.", "Lineal.")},
      "E": {"ok": "b", "hints": {"a": t("Linear adds the same number.", "La lineal suma lo mismo."), "c": t("Multiplying by the same is not quadratic.", "Multiplicar por lo mismo no es cuadrático."), "d": t("The values change: it is not constant.", "Los valores cambian: no es constante.")}, "solution": t("Exponential.", "Exponencial.")},
      "F": {"ok": "d", "hints": {"a": t("The first differences 3, 5, 7 change.", "Las primeras diferencias 3, 5, 7 cambian."), "b": t("The ratios are not constant.", "Las razones no son constantes."), "c": t("Rational has x in a denominator.", "La racional tiene x en un denominador.")}, "solution": t("Quadratic.", "Cuadrática.")},
      "G": {"ok": "a", "hints": {"b": t("$60 is the total change; divide by 2 years.", "$60 es el cambio total; divida entre 2 años."), "c": t("$360 is the final amount.", "$360 es la cantidad final."), "d": t("A rate needs its unit: per year.", "Una tasa lleva su unidad: por año.")}, "solution": t("60 / 2 = $30 per year.", "60 / 2 = $30 por año.")},
      "H": {"ok": "c", "hints": {"a": t("60 ft is the total change, and it goes down.", "60 pies es el cambio total, y baja."), "b": t("It goes down: the rate is negative.", "Baja: la tasa es negativa."), "d": t("Divide −60 by 3 seconds.", "Divida −60 entre 3 segundos.")}, "solution": t("(20 − 80) / 3 = −20 ft/s.", "(20 − 80) / 3 = −20 pies/s.")},
     }}

    quiz = [
     ("A", t("f(2) = 10 and f(5) = 25. What is the average rate of change?", "f(2) = 10 y f(5) = 25. ¿Tasa de cambio promedio?"), [("a", "15"), ("b", "3"), ("c", "35"), ("d", "5")]),
     ("B", t("f(1) = 7 and f(3) = 7. What is the average rate of change?", "f(1) = 7 y f(3) = 7. ¿Tasa de cambio promedio?"), [("a", "7"), ("b", "14"), ("c", "0"), ("d", "2")]),
     ("C", t("f(3) = 12 and f(6) = 3. What is the average rate of change?", "f(3) = 12 y f(6) = 3. ¿Tasa de cambio promedio?"), [("a", "3"), ("b", "−3"), ("c", "9"), ("d", "−9")]),
     ("D", t("Outputs 3, 6, 9, 12 (constant difference). What kind of function?", "Salidas 3, 6, 9, 12 (diferencia constante). ¿Tipo de función?"), [("a", t("quadratic", "cuadrática")), ("b", t("exponential", "exponencial")), ("c", t("linear", "lineal")), ("d", t("rational", "racional"))]),
     ("E", t("Outputs 2, 6, 18, 54 (multiply by 3). What kind of function?", "Salidas 2, 6, 18, 54 (se multiplica por 3). ¿Tipo de función?"), [("a", t("linear", "lineal")), ("b", t("exponential", "exponencial")), ("c", t("quadratic", "cuadrática")), ("d", t("constant", "constante"))]),
     ("F", t("Outputs 1, 4, 9, 16 (constant second difference). What kind of function?", "Salidas 1, 4, 9, 16 (segunda diferencia constante). ¿Tipo de función?"), [("a", t("linear", "lineal")), ("b", t("exponential", "exponencial")), ("c", t("rational", "racional")), ("d", t("quadratic", "cuadrática"))]),
     ("G", t("An account grows from $300 to $360 in 2 years. What is the average rate of change?", "Una cuenta crece de $300 a $360 en 2 años. ¿Tasa de cambio promedio?"), [("a", t("$30 per year", "$30 por año")), ("b", t("$60 per year", "$60 por año")), ("c", t("$360 per year", "$360 por año")), ("d", "$30")]),
     ("H", t("An object goes down from 80 feet to 20 feet in 3 seconds. What is the average rate of change?", "Un objeto baja de 80 pies a 20 pies en 3 segundos. ¿Tasa de cambio promedio?"), [("a", t("60 ft/s", "60 pies/s")), ("b", t("20 ft/s", "20 pies/s")), ("c", t("−20 ft/s", "−20 pies/s")), ("d", t("−60 ft/s", "−60 pies/s"))])]

    tarea = (t("For your own work, with your notebook and the calculator: (1) Savings, a falling object, and a viral post: find the average rate of change on the two intervals given and explain each result with its units. (a) A savings account with A(t) = 500 + 50t dollars, t in months: from 0 to 6 and from 6 to 12. (b) An object dropped from 100 feet, h(t) = 100 − 16t², t in seconds: from 0 to 1 and from 1 to 2. (c) A viral post with V(d) = 10 · 2ᵈ views, d in days: from 0 to 3 and from 3 to 5. Explain why only in the first one the rate does not change. (2) The pattern detective: classify each table (x = 0, 1, 2, 3, 4) as linear, quadratic, or exponential and write the evidence (constant difference, constant second difference, or constant ratio). A: 3, 5, 7, 9, 11. B: 1, 3, 9, 27, 81. C: 0, 1, 4, 9, 16. D: 10, 7, 4, 1, −2. E: 2, 3, 6, 11, 18. F: 64, 32, 16, 8, 4. (3) Slope and rate: with f(x) = −3x + 5, find the average rate of change from 0 to 2, from −1 to 4, and from 3 to 10. Check that it is always the same and explain why that number is the slope of the line. Then do several exercises of each activity on the practice page. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y la calculadora: (1) Ahorro, caída libre y publicación viral: calcule la tasa de cambio promedio en los dos intervalos indicados e interprete cada resultado con sus unidades. (a) Una cuenta de ahorro con A(t) = 500 + 50t dólares, t en meses: de 0 a 6 y de 6 a 12. (b) Un objeto que cae desde 100 pies, h(t) = 100 − 16t², t en segundos: de 0 a 1 y de 1 a 2. (c) Una publicación viral con V(d) = 10 · 2ᵈ vistas, d en días: de 0 a 3 y de 3 a 5. Explique por qué solo en la primera la tasa no cambia. (2) El detective de patrones: clasifique cada tabla (x = 0, 1, 2, 3, 4) en lineal, cuadrática o exponencial y escriba la evidencia (diferencia constante, segunda diferencia constante o razón constante). A: 3, 5, 7, 9, 11. B: 1, 3, 9, 27, 81. C: 0, 1, 4, 9, 16. D: 10, 7, 4, 1, −2. E: 2, 3, 6, 11, 18. F: 64, 32, 16, 8, 4. (3) Pendiente y tasa: con f(x) = −3x + 5, calcule la tasa de cambio promedio de 0 a 2, de −1 a 4 y de 3 a 10. Compruebe que siempre da lo mismo y explique por qué ese número es la pendiente de la recta. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Find a quantity in your life that changes over time (a bill, your savings, the price of gas). Write two values with their dates and find its average rate of change with its units.",
               "Busque una cantidad de su vida que cambie con el tiempo (una factura, sus ahorros, el precio de la gasolina). Escriba dos valores con sus fechas y halle su tasa de cambio promedio con sus unidades."))

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Find the average rate of change on an interval, read it with its units, and tell linear, quadratic, and exponential functions apart by their pattern.", "Calcule la tasa de cambio promedio en un intervalo, interprétela con sus unidades y distinga las funciones lineales, cuadráticas y exponenciales por su patrón."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Find</strong> the average rate of change with (f(b) − f(a)) / (b − a).", "<strong>Calcular</strong> la tasa de cambio promedio con (f(b) − f(a)) / (b − a)."),
         t("<strong>Connect</strong> the rate of change with the slope of the secant line.", "<strong>Relacionar</strong> la tasa de cambio con la pendiente de la recta secante."),
         t("<strong>Explain</strong> the rate in context, with its units and its sign.", "<strong>Interpretar</strong> la tasa en contexto, con sus unidades y su signo."),
         t("<strong>Identify</strong> linear, quadratic, and exponential functions from a table.", "<strong>Identificar</strong> funciones lineales, cuadráticas y exponenciales a partir de una tabla.")],
        secciones, tarea, quiz,
        t("Self-check checklist for the rate of change", "Lista de autoevaluación de la tasa de cambio"),
        t("Self-check checklist: skills for the average rate of change and the kinds of functions", "Lista de autoevaluación: destrezas de la tasa de cambio promedio y los tipos de funciones"),
        [(t("Finding the rate", "Calcular la tasa"), t("I use (f(b) − f(a)) / (b − a) correctly, with the right signs.", "Aplico (f(b) − f(a)) / (b − a) correctamente, con los signos correctos."), t("I use it, but I mix up the order or the signs.", "La aplico, pero confundo el orden o los signos."), t("I do not use the formula.", "No aplico la fórmula.")),
         (t("Reading the rate in context", "Interpretar la tasa en contexto"), t("I explain the rate with its units and what a negative rate means.", "Explico la tasa con sus unidades y lo que significa una tasa negativa."), t("I find the number but forget the units.", "Hallo el número pero olvido las unidades."), t("I do not explain what the rate means.", "No explico qué significa la tasa.")),
         (t("Identifying the kind of function", "Identificar el tipo de función"), t("I find differences, second differences, and ratios, and I classify the table.", "Calculo diferencias, segundas diferencias y razones, y clasifico la tabla."), t("I classify some tables, without evidence.", "Clasifico algunas tablas, sin evidencia."), t("I do not tell the kinds apart.", "No distingo los tipos."))],
        t("<p>This lesson closes Topic 7 · Systems of inequalities and functions. You graphed systems of inequalities, worked with functions (f(x), domain and range, composition), found the average rate of change, and told the kinds of functions apart by their pattern.</p>\n<p>Topic 8 · Modeling with functions and the GED practice test begins with <strong>Lesson 8.1 · Quadratic functions: the parabola, the vertex, and the intercepts</strong>, where you will graph parabolas and read their key points.</p>",
          "<p>Con esta lección se cierra el Tema 7 · Sistemas de desigualdades y funciones. Se graficaron sistemas de desigualdades, se trabajó con funciones (f(x), dominio y rango, composición), se calculó la tasa de cambio promedio y se distinguieron los tipos de funciones por su patrón.</p>\n<p>El Tema 8 · Modelado de funciones y simulacro GED comienza con la <strong>Lección 8.1 · Funciones cuadráticas: la parábola, el vértice y los interceptos</strong>, donde se graficarán parábolas y se leerán sus puntos clave.</p>"),
        ("8-1", ("", t("Lesson 8.1 · Quadratic functions: the parabola, the vertex, and the intercepts", "Lección 8.1 · Funciones cuadráticas: la parábola, el vértice y los interceptos"))),
        [(t("average rate of change", "tasa de cambio promedio"), t("(f(b) − f(a)) / (b − a): how much the output changes per unit of input.", "(f(b) − f(a)) / (b − a): cuánto cambia la salida por unidad de entrada.")),
         (t("secant line", "recta secante"), t("The line that joins two points of a graph; its slope is the average rate of change.", "La recta que une dos puntos de una gráfica; su pendiente es la tasa de cambio promedio.")),
         (t("second difference", "segunda diferencia"), t("The difference of the differences; it is constant in a quadratic function.", "La diferencia de las diferencias; es constante en una función cuadrática.")),
         (t("ratio", "razón"), t("The quotient of two consecutive values; it is constant in an exponential function.", "El cociente de dos valores consecutivos; es constante en una función exponencial."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function leeNumF(txt){ var s = String(txt).trim().replace(/\s+/g, "").replace(/[−–]/g, "-"), m = s.match(/^(-?\d+(?:\.\d+)?)\/(-?\d+(?:\.\d+)?)$/); if (m){ var d = parseFloat(m[2]); return d ? parseFloat(m[1]) / d : null; } return leeDecimal(s); }
function pn(v){ return v < 0 ? "(" + nf(v) + ")" : nf(v); }

/* ===== MODULE 1 · The average rate of change ===== */
var FUNS = [
 {p: [1, 2], txt: "f(x) = 2x + 1", min: -4, max: 6, R: {x0: -5, x1: 7, y0: -8, y1: 16}, nota: T("It is linear: the rate is 2 on every interval, which is its slope.", "Es lineal: la tasa de cambio vale 2 en cualquier intervalo, que es justamente su pendiente.")},
 {p: [6, -1], txt: "f(x) = −x + 6", min: -2, max: 8, R: {x0: -3, x1: 9, y0: -4, y1: 10}, nota: T("The rate is always −1: for each unit x moves forward, the output goes down one unit.", "La tasa sale −1 siempre: por cada unidad que avanza x, la salida baja una unidad.")},
 {p: [0, 0, 1], txt: "f(x) = x²", min: -4, max: 6, R: {x0: -5, x1: 7, y0: -4, y1: 38}, nota: T("It is quadratic: each interval gives a different rate. The farther right, the steeper the secant line.", "Es cuadrática: cada intervalo da una tasa distinta. Cuanto más a la derecha, más empinada la recta.")},
 {p: [0, -4, 1], txt: "f(x) = x² − 4x", min: -2, max: 6, R: {x0: -3, x1: 7, y0: -6, y1: 14}, nota: T("Try the interval from 0 to 4: the rate is 0, because the function goes down and comes back up to the same height.", "Pruebe el intervalo de 0 a 4: la tasa sale 0, porque la función baja y vuelve a subir hasta la misma altura.")},
 {e: true, txt: "f(x) = 2ˣ", min: -2, max: 5, R: {x0: -3, x1: 6, y0: -4, y1: 34}, nota: T("It is exponential: the rate grows faster and faster, because each step multiplies the value by 2.", "Es exponencial: la tasa crece cada vez más rápido, porque cada paso multiplica el valor por 2.")}];
function fv(F, x){ return F.e ? Math.pow(2, x) : pEval(F.p, x); }
function taDibuja(){ var F = FUNS[+$("s-fun").value];
  ["s-a", "s-b"].forEach(function(id){ $(id).min = F.min; $(id).max = F.max; if (+$(id).value < F.min) $(id).value = F.min; if (+$(id).value > F.max) $(id).value = F.max; });
  var a = +$("s-a").value, b = +$("s-b").value; $("s-av").textContent = sg(a); $("s-bv").textContent = sg(b);
  var o = {rango: F.R, curvas: [{f: function(x){ return fv(F, x); }}], voz: T("Graph of ", "Gráfica de ") + F.txt + "."};
  if (a === b){ $("s-graf").innerHTML = grafFun(o); $("s-txt").innerHTML = '<div class="linea"><strong>' + T("The two ends are equal.", "Los dos extremos son iguales.") + "</strong> " + T("With a = b, the denominator b − a would be 0, and you cannot divide by zero: you need a real interval, with two different values.", "Con a = b, el denominador b − a sería 0, y la división entre cero no está definida: hace falta un intervalo de verdad, con dos valores distintos.") + "</div>"; return; }
  var fa = fv(F, a), fb = fv(F, b), m = (fb - fa) / (b - a), lado = Math.abs(F.R.x1 - F.R.x0);
  o.segmentos = [[[F.R.x0, fa + m * (F.R.x0 - a)], [F.R.x1, fa + m * (F.R.x1 - a)], "#c62828", null, 2.5], [[a, fa], [b, fa], "#2e7d32", "6 5", 2.5], [[b, fa], [b, fb], "#2e7d32", "6 5", 2.5]];
  var izq = Math.min(a, b), der = Math.max(a, b);
  o.puntos = [[a, fa, "#263238", "(" + nf(a) + ", " + nf(fa) + ")", 6.5, true, a === der || a - F.R.x0 < 2.2], [b, fb, "#263238", "(" + nf(b) + ", " + nf(fb) + ")", 6.5, true, b === der || b - F.R.x0 < 2.2]];
  o.voz = T("Graph of ", "Gráfica de ") + F.txt + T(" with the secant line through ", " con la recta secante por ") + par(a, fa) + T(" and ", " y ") + par(b, fb) + T(". Its slope is ", ". Su pendiente es ") + nf(m) + ".";
  $("s-graf").innerHTML = grafFun(o);
  var fr = F.e ? nf(m) : fracTxt(fb - fa, b - a);
  $("s-txt").innerHTML = '<div class="linea">f(' + sg(a) + ") = " + nf(fa) + "; f(" + sg(b) + ") = " + nf(fb) + '.</div><div class="linea">' + T("rate = ", "tasa = ") + tasaTxt(fa, fb, a, b) + " = " + nf(fb - fa) + " / " + nf(b - a) + " = <strong>" + fr + (fr.indexOf("/") > 0 ? " = " + nf(m) : "") + "</strong></div>" +
    '<div class="linea">' + (m > 0 ? T("On average, the output goes up " + nf(m) + " for each unit of x.", "En promedio, la salida sube " + nf(m) + " por cada unidad de x.") : m < 0 ? T("On average, the output goes down " + nf(-m) + " for each unit of x.", "En promedio, la salida baja " + nf(-m) + " por cada unidad de x.") : T("On average there is no change: the output ends at the same height.", "En promedio no hay cambio: la salida termina a la misma altura.")) + " " + F.nota + "</div>"; }
["s-a", "s-b"].forEach(function(id){ $(id).addEventListener("input", taDibuja); }); $("s-fun").addEventListener("change", taDibuja); taDibuja();
creaPracticaLibre("sq", function(){ var t = aleatorio(0, 2), a, b, fa, fb, enun, F;
  do { a = aleatorio(-3, 4); b = a + aleatorio(1, 4); } while (a === b);
  if (t === 0){ var m = nz(-6, 8) * elige([1, 1, .5]); fa = aleatorio(-10, 20); fb = fa + m * (b - a); if (fb !== Math.round(fb)){ fb = Math.round(fb); } enun = "f(" + sg(a) + ") = " + nf(fa) + T(" and ", " y ") + "f(" + sg(b) + ") = " + nf(fb) + T(". What is the average rate of change on [", ". ¿Cuál es la tasa de cambio promedio en [") + sg(a) + ", " + sg(b) + "]?"; }
  else if (t === 1){ F = [aleatorio(-5, 5), nz(-4, 4), nz(-2, 2)]; fa = pEval(F, a); fb = pEval(F, b); enun = T("For ", "Para ") + fDef(F) + T(", what is the average rate of change from x = ", ", ¿cuál es la tasa de cambio promedio de x = ") + sg(a) + T(" to x = ", " a x = ") + sg(b) + "?"; }
  else { a = aleatorio(0, 3); b = a + aleatorio(1, 3); var base = elige([2, 3]), k = elige([1, 2, 3]); fa = k * Math.pow(base, a); fb = k * Math.pow(base, b); enun = T("For ", "Para ") + "f(x) = " + (k === 1 ? "" : k + " · ") + base + '<sup>x</sup>' + T(", what is the average rate of change from x = ", ", ¿cuál es la tasa de cambio promedio de x = ") + a + T(" to x = ", " a x = ") + b + "?"; }
  var res = (fb - fa) / (b - a);
  return {enun: enun,
    evalua: function(txt){ var v = leeNumF(txt); if (v === null) return {estado: "invalido", msg: T("Type a number or a fraction, such as 4, −2.5, or 7/2.", "Escriba un número o una fracción, como 4, −2.5 o 7/2.")};
      if (Math.abs(v - res) < .011) return {estado: "bien"};
      if (fb !== fa && Math.abs(v - (b - a) / (fb - fa)) < .011) return {estado: "mal", msg: T("You divided upside down: the change in y goes on top, the change in x on the bottom.", "Dividió al revés: el cambio en y va arriba y el cambio en x, abajo.")};
      if (Math.abs(v + res) < .011) return {estado: "mal", msg: T("Check the sign: subtract in the same order on top and on the bottom (final minus starting).", "Revise el signo: reste en el mismo orden arriba y abajo (final menos inicial).")};
      if (Math.abs(v - (fb - fa)) < .011) return {estado: "mal", msg: T("That is the change in y. Now divide it by the change in x, " + nf(b - a) + ".", "Ese es el cambio en y. Ahora divídalo entre el cambio en x, " + nf(b - a) + ".")};
      return {estado: "mal", msg: T("Find f(" + sg(a) + ") and f(" + sg(b) + "), subtract them, and divide by " + sg(b) + " − " + pn(a) + ".", "Halle f(" + sg(a) + ") y f(" + sg(b) + "), réstelos y divida entre " + sg(b) + " − " + pn(a) + ".")}; },
    solucion: (t > 0 ? "f(" + sg(a) + ") = " + nf(fa) + ", f(" + sg(b) + ") = " + nf(fb) + ". " : "") + tasaTxt(fa, fb, a, b) + " = " + nf(fb - fa) + " / " + nf(b - a) + " = <strong>" + nf(res) + "</strong>."};
});

/* ===== MODULE 2 · Reading the rate in context ===== */
var CASOS = [
 {enun: T("A savings account goes from $100 to $160 in 3 years. What is the average rate of change, and what does it mean?", "Una cuenta de ahorro pasa de $100 a $160 en 3 años. ¿Cuál es la tasa de cambio promedio y qué significa?"),
  pasos: [T("Input: time in <strong>years</strong>. Output: money in <strong>dollars</strong>. The rate will be in dollars per year.", "Entrada: el <strong>tiempo en años</strong>. Salida: el <strong>dinero en dólares</strong>. La unidad de la tasa será dólares por año."), T("Change in the output: 160 − 100 = <strong>60 dollars</strong>.", "Cambio de la salida: 160 − 100 = <strong>60 dólares</strong>."), T("Change in the input: 3 − 0 = <strong>3 years</strong>.", "Cambio de la entrada: 3 − 0 = <strong>3 años</strong>."), T("Divide: 60 / 3 = <strong>20</strong>.", "Dividir: 60 / 3 = <strong>20</strong>."), T("On average, the account grows <strong>$20 per year</strong>. It is an average: some years it may have grown more and others less.", "La cuenta crece, en promedio, <strong>$20 por año</strong>. Es un promedio: algunos años pudo subir más y otros menos.")]},
 {enun: T("A car starts from rest and travels 150 feet in 5 seconds. What is its average rate of change?", "Un auto parte del reposo y recorre 150 pies en 5 segundos. ¿Cuál es su tasa de cambio promedio?"),
  pasos: [T("Input: time in seconds. Output: distance in feet. The rate will be in feet per second.", "Entrada: el tiempo en segundos. Salida: la distancia en pies. La unidad será pies por segundo."), T("Change in the output: 150 − 0 = <strong>150 feet</strong>.", "Cambio de la salida: 150 − 0 = <strong>150 pies</strong>."), T("Change in the input: 5 − 0 = <strong>5 seconds</strong>.", "Cambio de la entrada: 5 − 0 = <strong>5 segundos</strong>."), T("Divide: 150 / 5 = <strong>30</strong>.", "Dividir: 150 / 5 = <strong>30</strong>."), T("On average, the car goes <strong>30 feet per second</strong>. That is its average speed.", "El auto avanza, en promedio, <strong>30 pies por segundo</strong>. Eso es justamente su velocidad promedio.")]},
 {enun: T("A tank holds 400 gallons, and six hours later it has 100 gallons left. What is the average rate of change?", "Un tanque tiene 400 galones y, seis horas después, le quedan 100. ¿Cuál es la tasa de cambio promedio?"),
  pasos: [T("Input: hours. Output: gallons. The rate will be in gallons per hour.", "Entrada: horas. Salida: galones. La unidad será galones por hora."), T("Change in the output: 100 − 400 = <strong>−300 gallons</strong>. The order matters: always final minus starting.", "Cambio de la salida: 100 − 400 = <strong>−300 galones</strong>. El orden importa: siempre el valor final menos el inicial."), T("Change in the input: 6 − 0 = <strong>6 hours</strong>.", "Cambio de la entrada: 6 − 0 = <strong>6 horas</strong>."), T("Divide: −300 / 6 = <strong>−50</strong>.", "Dividir: −300 / 6 = <strong>−50</strong>."), T("The tank loses <strong>50 gallons per hour</strong>. The minus sign is not a mistake: it says the amount goes down.", "El tanque pierde <strong>50 galones por hora</strong>. El signo negativo no es un error: avisa de que la cantidad disminuye.")]},
 {enun: T("A town goes from 1,200 to 1,500 people in 4 years. What is the average rate of change?", "Un pueblo pasa de 1,200 a 1,500 habitantes en 4 años. ¿Cuál es la tasa de cambio promedio?"),
  pasos: [T("Input: years. Output: people. The rate will be in people per year.", "Entrada: años. Salida: habitantes. La unidad será habitantes por año."), T("Change in the output: 1,500 − 1,200 = <strong>300 people</strong>.", "Cambio de la salida: 1,500 − 1,200 = <strong>300 habitantes</strong>."), T("Change in the input: <strong>4 years</strong>.", "Cambio de la entrada: <strong>4 años</strong>."), T("Divide: 300 / 4 = <strong>75</strong>.", "Dividir: 300 / 4 = <strong>75</strong>."), T("The town gains, on average, <strong>75 people per year</strong>.", "El pueblo gana, en promedio, <strong>75 habitantes por año</strong>.")]},
 {enun: T("A phone bill goes up from $45 to $60 when the minutes used go from 300 to 600. What is the average rate of change?", "La factura del teléfono sube de $45 a $60 cuando los minutos usados pasan de 300 a 600. ¿Cuál es la tasa de cambio promedio?"),
  pasos: [T("Input: minutes used. Output: dollars. The rate will be in dollars per minute.", "Entrada: minutos usados. Salida: dólares. La unidad será dólares por minuto."), T("Change in the output: 60 − 45 = <strong>15 dollars</strong>.", "Cambio de la salida: 60 − 45 = <strong>15 dólares</strong>."), T("Change in the input: 600 − 300 = <strong>300 minutes</strong>.", "Cambio de la entrada: 600 − 300 = <strong>300 minutos</strong>."), T("Divide: 15 / 300 = <strong>0.05</strong>.", "Dividir: 15 / 300 = <strong>0.05</strong>."), T("Each extra minute costs, on average, <strong>5 cents</strong>. When the result is a small decimal, saying it in cents makes it clearer.", "Cada minuto extra cuesta, en promedio, <strong>5 centavos</strong>. Cuando el resultado es un decimal pequeño, conviene decirlo en centavos para que se entienda.")]},
 {enun: T("At 3 p.m. it is 72 °F, and at 7 p.m. it is 60 °F. What is the average rate of change?", "A las 3 de la tarde hay 72 °F y a las 7 hay 60 °F. ¿Cuál es la tasa de cambio promedio?"),
  pasos: [T("Input: hours. Output: degrees Fahrenheit. The rate will be in degrees per hour.", "Entrada: horas. Salida: grados Fahrenheit. La unidad será grados por hora."), T("Change in the output: 60 − 72 = <strong>−12 degrees</strong>.", "Cambio de la salida: 60 − 72 = <strong>−12 grados</strong>."), T("Change in the input: 7 − 3 = <strong>4 hours</strong>.", "Cambio de la entrada: 7 − 3 = <strong>4 horas</strong>."), T("Divide: −12 / 4 = <strong>−3</strong>.", "Dividir: −12 / 4 = <strong>−3</strong>."), T("The temperature drops, on average, <strong>3 °F per hour</strong> during the afternoon.", "La temperatura baja, en promedio, <strong>3 °F por hora</strong> durante la tarde.")]}];
pasoAPaso4("ct", function(){ var C = CASOS[+$("ct-caso").value]; return {enun: C.enun, pasos: C.pasos}; });
$("ct-caso").addEventListener("change", function(){ $("ct-nuevo").click(); });
OMR("iq", function(){ var t = aleatorio(0, 4), a0, a1, d, u, ue, us, v0, v1, contexto;
  if (t === 0){ d = aleatorio(2, 6); u = aleatorio(10, 60) * 5; v0 = aleatorio(10, 50) * 10; v1 = v0 + u * d; ue = T("years", "años"); us = T(" per year", " por año");
    contexto = T("A savings account goes from $" + v0 + " to $" + v1 + " in " + d + " years.", "Una cuenta de ahorro pasa de $" + v0 + " a $" + v1 + " en " + d + " años."); return armaIQ(v1 - v0, d, "$", us, contexto); }
  if (t === 1){ d = aleatorio(2, 8); u = aleatorio(5, 40); contexto = T("A runner covers " + u * d + " feet in " + d + " seconds.", "Una corredora recorre " + u * d + " pies en " + d + " segundos."); return armaIQ(u * d, d, "", T(" ft/s", " pies/s"), contexto); }
  if (t === 2){ d = aleatorio(2, 6); u = aleatorio(4, 30); v0 = u * d + aleatorio(2, 30) * 10; v1 = v0 - u * d; contexto = T("A tank goes from " + v0 + " gallons to " + v1 + " gallons in " + d + " hours.", "Un tanque pasa de " + v0 + " galones a " + v1 + " galones en " + d + " horas."); return armaIQ(v1 - v0, d, "", T(" gallons per hour", " galones por hora"), contexto); }
  if (t === 3){ d = aleatorio(2, 5); u = aleatorio(2, 6); v0 = aleatorio(60, 90); v1 = v0 - u * d * elige([1, -1]); a0 = aleatorio(1, 4); a1 = a0 + d;
    contexto = T("At " + a0 + " p.m. it is " + v0 + " °F, and at " + a1 + " p.m. it is " + v1 + " °F.", "A las " + a0 + " de la tarde hay " + v0 + " °F y a las " + a1 + " hay " + v1 + " °F."); return armaIQ(v1 - v0, d, "", T(" °F per hour", " °F por hora"), contexto); }
  d = aleatorio(2, 6); u = aleatorio(5, 60) * 5; v0 = aleatorio(20, 90) * 100; v1 = v0 + u * d;
  contexto = T("A town goes from " + v0.toLocaleString("en-US") + " to " + v1.toLocaleString("en-US") + " people in " + d + " years.", "Un pueblo pasa de " + v0.toLocaleString("en-US") + " a " + v1.toLocaleString("en-US") + " habitantes en " + d + " años."); return armaIQ(v1 - v0, d, "", T(" people per year", " habitantes por año"), contexto); });
function armaIQ(dy, dx, pre, suf, contexto){ var r = dy / dx, f = function(v){ return (v < 0 ? "−" : "") + pre + Math.abs(Math.round(v * 100) / 100).toLocaleString("en-US") + suf; };
  return {enun: contexto + T(" What is the average rate of change?", " ¿Cuál es la tasa de cambio promedio?"), correcta: "ok",
    opciones: [{clave: "ok", html: f(r)}, {clave: "t", html: f(dy)}, {clave: "s", html: f(-r)}, {clave: "i", html: f(Math.round(dx / dy * 1000) / 1000)}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }),
    pista: T("Change in the output (final minus starting) divided by the change in the input.", "Cambio de la salida (final menos inicial) entre el cambio de la entrada."),
    porClave: {t: T("That is the total change. Divide it by " + dx + ".", "Ese es el cambio total. Divídalo entre " + dx + "."), s: T("Check the sign: does the quantity go up or down?", "Revise el signo: ¿la cantidad sube o baja?")},
    bien: nf(dy) + " / " + dx + " = " + nf(r) + ": " + (r < 0 ? T("it goes down ", "baja ") + f(-r) : T("it goes up ", "sube ") + f(r)) + T(", on average.", ", en promedio.")}; }

/* ===== MODULE 3 · Kind of function ===== */
var TABLAS = [[2, 5, 8, 11, 14], [0, 1, 4, 9, 16], [1, 2, 4, 8, 16], [20, 17, 14, 11, 8], [81, 27, 9, 3, 1], [3, 4, 7, 12, 19], [5, 10, 20, 40, 80]];
function tablaTipo(ys){ var d1 = difs(ys), d2 = difs(d1), q = razones(ys), k = tipoTabla(ys);
  var fila = function(et, l, cte, desde){ var s = '<tr><th scope="row">' + et + "</th>"; for (var i = 0; i < ys.length; i++){ var j = i - desde; s += "<td" + (cte && j >= 0 && j < l.length ? ' class="cte"' : "") + ">" + (j >= 0 && j < l.length ? (isFinite(l[j]) ? nf(l[j]) : "—") : "") + "</td>"; } return s + "</tr>"; };
  var html = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("The outputs with their differences and ratios", "Las salidas con sus diferencias y razones") + '</caption><tbody>' +
    fila("x", ys.map(function(v, i){ return i; }), false, 0) + fila("y", ys, false, 0) + fila(T("difference", "diferencia"), d1, k === "lin", 1) + fila(T("2nd difference", "2.ª diferencia"), d2, k === "cuad", 2) + fila(T("ratio", "razón"), q, k === "exp", 1) + "</tbody></table></div>";
  var conc = {lin: T("The differences are all " + nf(d1[0]) + ": it adds the same each time. <strong>Linear.</strong>", "Las diferencias valen todas " + nf(d1[0]) + ": suma lo mismo cada vez. <strong>Lineal.</strong>"),
    cuad: T("The first differences change, but the second differences are all " + nf(d2[0]) + ". <strong>Quadratic.</strong>", "Las primeras diferencias cambian, pero las segundas valen todas " + nf(d2[0]) + ". <strong>Cuadrática.</strong>"),
    exp: T("The ratios are all " + nf(q[0]) + ": it multiplies by the same each time. <strong>Exponential.</strong>", "Las razones valen todas " + nf(q[0]) + ": multiplica por lo mismo cada vez. <strong>Exponencial.</strong>"),
    otra: T("No column is constant: the table is not linear, quadratic, or exponential (or it has too few values to tell).", "Ninguna columna es constante: la tabla no es lineal, ni cuadrática, ni exponencial (o tiene muy pocos valores para saberlo).")}[k];
  return html + '<div class="linea">' + conc + "</div>"; }
function tiDibuja(ys){ $("ti-txt").innerHTML = tablaTipo(ys); }
$("ti-tabla").addEventListener("change", function(){ tiDibuja(TABLAS[+$("ti-tabla").value]); });
$("ti-usar").addEventListener("click", function(){ var l = $("ti-propia").value.split(/[,;\s]+/).filter(function(s){ return s; }).map(leeDecimal);
  if (l.length < 4 || l.some(function(v){ return v === null; })){ $("ti-txt").innerHTML = '<div class="linea">' + T("Type at least 4 numbers separated by commas, such as 3, 7, 11, 15.", "Escriba al menos 4 números separados por comas, como 3, 7, 11, 15.") + "</div>"; return; }
  tiDibuja(l.slice(0, 7)); });
tiDibuja(TABLAS[0]);
OMR("kq", function(){ var k = elige(["lin", "cuad", "exp"]), ys = [], i, x0 = 0;
  if (k === "lin"){ var a = aleatorio(-10, 20), m = nz(-6, 7); for (i = 0; i < 5; i++) ys.push(a + m * i); }
  else if (k === "cuad"){ var A = nz(-2, 3), b = aleatorio(-4, 4), c = aleatorio(-5, 10); for (i = 0; i < 5; i++) ys.push(A * i * i + b * i + c); }
  else { var r = elige([2, 3, .5, 4]), c0 = r === .5 ? elige([64, 128, 160]) : elige([1, 2, 3, 5]); for (i = 0; i < 5; i++) ys.push(c0 * Math.pow(r, i)); }
  var tb = '<div class="tabla-scroll"><table class="tabla-lados centro"><caption class="sr-only">' + T("Table of values", "Tabla de valores") + '</caption><tbody><tr><th scope="row">x</th>' + ys.map(function(v, j){ return "<td>" + j + "</td>"; }).join("") + '</tr><tr><th scope="row">y</th>' + ys.map(function(v){ return "<td>" + nf(v) + "</td>"; }).join("") + "</tr></tbody></table></div>";
  var d1 = difs(ys), d2 = difs(d1), q = razones(ys);
  return {enun: T("What kind of function does this table show?", "¿Qué tipo de función muestra esta tabla?") + tb, correcta: k, enOrden: true,
    opciones: ["lin", "cuad", "exp"].map(function(z){ return {clave: z, html: nomTipo(z)}; }),
    pista: T("Find the differences between consecutive outputs. If they are not constant, try the second differences and the ratios.", "Calcule las diferencias entre salidas consecutivas. Si no son constantes, pruebe con las segundas diferencias y con las razones."),
    bien: T("Differences: ", "Diferencias: ") + d1.map(nf).join(", ") + (k === "lin" ? "" : T("; second differences: ", "; segundas diferencias: ") + d2.map(nf).join(", ")) + (k === "exp" ? T("; ratios: ", "; razones: ") + q.map(nf).join(", ") : "") + ". " + nomTipo(k).charAt(0).toUpperCase() + nomTipo(k).slice(1) + "."};
});
'''

def practica_pagina():
    n = N
    funs = [("0", t("f(x) = 2x + 1 (linear)", "f(x) = 2x + 1 (lineal)")), ("1", t("f(x) = −x + 6 (linear, decreasing)", "f(x) = −x + 6 (lineal decreciente)")), ("2", t("f(x) = x² (quadratic)", "f(x) = x² (cuadrática)")), ("3", t("f(x) = x² − 4x (quadratic with a minimum)", "f(x) = x² − 4x (cuadrática con mínimo)")), ("4", t("f(x) = 2ˣ (exponential)", "f(x) = 2ˣ (exponencial)"))]
    casos = [("0", t("The savings account", "La cuenta de ahorro")), ("1", t("The moving car", "El auto en movimiento")), ("2", t("The tank that drains", "El tanque que se vacía")), ("3", t("The town's population", "La población del pueblo")), ("4", t("The phone bill", "La factura del teléfono")), ("5", t("The afternoon temperature", "La temperatura de la tarde"))]
    tablas = [(str(i), v) for i, v in enumerate(["2, 5, 8, 11, 14", "0, 1, 4, 9, 16", "1, 2, 4, 8, 16", "20, 17, 14, 11, 8", "81, 27, 9, 3, 1", "3, 4, 7, 12, 19", "5, 10, 20, 40, 80"])]
    rango = lambda i, et, v: f'<div class="campo"><label for="{i}">{et} <output id="{i}v"></output></label><input type="range" id="{i}" min="-4" max="6" step="1" value="{v}"></div>'
    mods = [
     (t("rate", "tasa"), t("The average rate of change", "La tasa de cambio promedio"),
      f'''      <p>{t("The average rate of change from x = a to x = b is the change in y over the change in x: the slope of the <strong>secant line</strong> (red) that joins the two points.", "La tasa de cambio promedio de x = a a x = b es el cambio en y entre el cambio en x: la pendiente de la <strong>recta secante</strong> (roja) que une los dos puntos.")}</p>
{n4.formula(t("rate = (f(b) − f(a)) / (b − a)", "tasa = (f(b) − f(a)) / (b − a)"))}
      <div class="panel"><div class="campos">{n4.lista("s-fun", t("Function", "Función"), funs)}{rango("s-a", "a =", 1)}{rango("s-b", "b =", 3)}</div></div>
      <div id="s-graf"></div>
{n4.salida("s-txt")}
{B.libre("sq", t("Practice: find the rate", "Practique: calcule la tasa"), t("Rate", "Tasa"), nota=False)}
      <p class="nota">{t("You can type a whole number, a decimal, or a fraction such as 7/2.", "Puede escribir un número entero, un decimal o una fracción como 7/2.")}</p>'''),
     (t("context", "contexto"), t("Reading the rate in context", "Interpretar la tasa en contexto"),
      f'''      <p>{t("In context, the rate always has a unit: unit of output per unit of input. Choose a situation and go through it step by step.", "En contexto, la tasa lleva siempre su unidad: unidad de salida por unidad de entrada. Elija una situación y recórrala paso a paso.")}</p>
      <div class="panel"><div class="campos">{n4.lista("ct-caso", t("Situation", "Situación"), casos)}</div></div>
{n4.pasos("ct", t("Start again", "Empezar de nuevo"))}
{B.om("iq", t("Practice: find and read the rate", "Practique: calcule e interprete"))}'''),
     (t("kind", "tipo"), t("Identifying the kind of function", "Identificar el tipo de función"),
      f'''      <p>{t("With equally spaced inputs, look for the constant column: differences (linear), second differences (quadratic), or ratios (exponential).", "Con entradas igualmente espaciadas, busque la columna constante: diferencias (lineal), segundas diferencias (cuadrática) o razones (exponencial).")}</p>
      <div class="panel"><div class="campos">{n4.lista("ti-tabla", t("Outputs for x = 0, 1, 2, 3, 4", "Salidas para x = 0, 1, 2, 3, 4"), tablas)}</div>
        <div class="campos"><div class="campo"><label for="ti-propia">{t("Or type your own outputs", "O escriba sus propias salidas")}</label><input type="text" id="ti-propia" autocomplete="off" placeholder="3, 7, 11, 15" style="width:14em"></div></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="ti-usar">{t("Use my table", "Usar mi tabla")}</button></div></div>
{n4.salida("ti-txt")}
{B.om("kq", t("Practice: classify the pattern", "Practique: clasifique el patrón"))}''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Tasa de cambio promedio e identificar tipos de funciones")
