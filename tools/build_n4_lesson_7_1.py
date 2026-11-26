"""Level 4 · Lesson 7.1 · Systems of linear inequalities: graphing the solution region — builds the lesson and its practice page in
English and in Spanish. Sources (GEDparaHispanos): clase_mate4/leccion_7-1.html and algebra/n4-l7-1.html (graphing one inequality,
the test point, the feasible region of a system, and checking a point). They are rebuilt here, inside LearnGED, with math/ineq4.js.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4
from build_n4_lesson_6_1 import ESTILO_SIS

B.NIVEL = 4
N = "7-1"
TEMA = ("Systems of inequalities and functions", "Sistemas de desigualdades y funciones")
TIT = ("Systems of linear inequalities: graphing the solution region", "Sistemas de desigualdades lineales: graficar la región solución")
SCRIPTS = n4.SCRIPTS + ("/math/ineq4.js",)
ESTILO = n4.ESTILO + ESTILO_SIS + """
  .tabla-lados td.si{color:#1b5e20;font-weight:700;}
  .tabla-lados td.no{color:#b71c1c;font-weight:700;}
  .veredicto{font-weight:700;}
"""

def fig_semiplano():
    p = n4.Plano(-5, 5, -5, 5, 34, paso=1)
    p.poli([(-5, -5), (5, -5), (5, 5), (4, 5), (-5, -4)], "rgba(21,101,192,.2)", "none", 0)
    p.seg((-5, -4), (4, 5), "#1565c0", 3.5)
    p.texto((-2.2, 1.7), "y ≤ x + 1", "#1565c0", 15, "middle")
    p.punto((0, 0), "#263238").texto((0.25, -1.4), t("test (0, 0)", "prueba (0, 0)"), "#263238", 14, "start")
    return p.svg(t("Graph of y is less than or equal to x plus 1: a solid line, with the side below it shaded. The test point 0, 0 is in the shaded side.",
                   "Gráfica de y menor o igual que x + 1: línea sólida, con el lado de abajo sombreado. El punto de prueba 0, 0 queda en el lado sombreado."), 340)

def fig_triangulo():
    p = n4.Plano(-2, 6, -2, 6, 34, paso=1)
    p.poli([(0, 0), (4, 0), (0, 4)], "rgba(46,125,50,.32)", "#2e7d32", 0)
    p.seg((0, -2), (0, 6), "#c62828", 3).seg((-2, 0), (6, 0), "#6a1b9a", 3).seg((-2, 6), (6, -2), "#1565c0", 3)
    p.texto((3.4, 2.6), "x + y ≤ 4", "#1565c0", 15, "start", 0, 0).texto((0, 5.3), "x ≥ 0", "#c62828", 14, "start", 8, 0).texto((5, 0), "y ≥ 0", "#6a1b9a", 14, "middle", 0, -14)
    for v in [(0, 0), (4, 0), (0, 4)]:
        p.punto(v, "#2e7d32")
    return p.svg(t("The feasible region of x greater than or equal to 0, y greater than or equal to 0, and x plus y less than or equal to 4: the triangle with vertices 0, 0; 4, 0; and 0, 4, shaded in green.",
                   "La región factible de x mayor o igual que 0, y mayor o igual que 0, y x + y menor o igual que 4: el triángulo de vértices 0, 0; 4, 0 y 0, 4, sombreado en verde."), 340)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Topic 6.</strong> In Topic 6, the solution of a system of equations was a <strong>point</strong>. In Topic 7 the equal sign (=) becomes an inequality sign (&lt;, ≤, &gt;, ≥), and the solution is no longer a point but a whole <strong>region</strong> of the plane: many points meet the conditions at the same time.", "<strong>Conexión con el tema anterior.</strong> En el Tema 6, la solución de un sistema de ecuaciones era un <strong>punto</strong>. En el Tema 7 las igualdades (=) se cambian por desigualdades (&lt;, ≤, &gt;, ≥), y la solución ya no es un punto sino toda una <strong>región</strong> del plano: muchos puntos cumplen las condiciones a la vez.")}</p>
<p>{t("Graphing an inequality has two parts: the <strong>boundary line</strong> and the <strong>shading</strong> of the correct side.", "Graficar una desigualdad tiene dos partes: la <strong>línea frontera</strong> y el <strong>sombreado</strong> del lado correcto.")}</p>
{tabla(t("Solid or dashed", "Sólida o punteada"), t("How to draw the boundary line for each inequality symbol", "Cómo dibujar la línea frontera según el símbolo de la desigualdad"), [t("Symbol", "Símbolo"), t("Boundary line", "Línea frontera")],
  [[t("&lt; or &gt;", "&lt; o &gt;"), t("Dashed (the boundary is not included)", "Punteada (la frontera no se incluye)")], [t("≤ or ≥", "≤ o ≥"), t("Solid (the boundary is included)", "Sólida (la frontera sí se incluye)")]])}
{fig_semiplano()}
<p>{t("On the graph, y ≤ x + 1 has a solid line (because of the ≤), and the side below the line is shaded: the side where the test point (0, 0) is.", "En la gráfica, y ≤ x + 1 tiene línea sólida (por el ≤) y se sombrea el lado de abajo, donde está el punto de prueba (0, 0).")}</p>
{enlace(n, t("graph", "graficar"), t("graphing an inequality", "la gráfica de una desigualdad"), t("Choose the symbol, the slope, and the intercept: the line turns solid or dashed and the shading moves as you change them.", "Elija el símbolo, la pendiente y el intercepto: la línea se vuelve sólida o punteada y el sombreado cambia al moverlos."))}'''

    s2 = f'''<p>{t("To decide which side of the line to shade, choose a <strong>test point</strong> that is not on the line (almost always (0, 0)) and substitute it into the inequality.", "Para decidir qué lado de la recta se sombrea, se elige un <strong>punto de prueba</strong> que no esté sobre la recta (casi siempre (0, 0)) y se sustituye en la desigualdad.")}</p>
{ejemplo(t("Example 1: graph 2x + y > 4.", "Ejemplo 1 · Graficar 2x + y > 4."),
  [("1", t("The line is dashed", "La línea es punteada"), t("(because of the &gt; symbol).", "(por el símbolo &gt;).")), ("2", t("Test (0, 0):", "Se prueba (0, 0):"), t("2(0) + 0 &gt; 4, that is, 0 &gt; 4. False.", "2(0) + 0 &gt; 4, es decir, 0 &gt; 4. Falso.")),
   ("✓", t("Shade.", "Se sombrea."), t("<strong>Because it is false, shade the side opposite the origin.</strong>", "<strong>Como es falso, se sombrea el lado contrario al origen.</strong>"))])}
{caja("tip", t("True or false", "Verdadero o falso"), t("<p>If the test point makes the inequality true, shade its side; if it makes it false, shade the other side. If the line goes through (0, 0), use another point, such as (1, 0).</p>", "<p>Si el punto de prueba cumple la desigualdad, se sombrea su lado; si no la cumple, se sombrea el lado contrario. Si la recta pasa por (0, 0), se usa otro punto, como (1, 0).</p>"))}
{practica("p1", t("Practice 1 — The line", "Práctica 1 — La línea"), t("For y ≤ x, the boundary line is drawn:", "Para y ≤ x, la línea frontera se dibuja:"), [("a", t("solid", "sólida")), ("b", t("dashed", "punteada")), ("c", t("no line at all", "de ningún tipo"))])}
{practica("p2", t("Practice 2 — y > 3", "Práctica 2 — y > 3"), t("For y > 3, the boundary line is drawn:", "Para y > 3, la línea frontera se dibuja:"), [("a", t("solid", "sólida")), ("b", t("dashed", "punteada")), ("c", t("double", "doble"))])}
{practica("p3", t("Practice 3 — The side", "Práctica 3 — El lado"), t("For y < x + 2, test (0, 0): 0 < 2 is true. You shade:", "En y < x + 2 se prueba (0, 0): 0 < 2 es verdadero. Se sombrea:"), [("a", t("the opposite side", "el lado opuesto")), ("b", t("only the line", "solo la recta")), ("c", t("the side of the origin", "el lado del origen"))])}
{enlace(n, t("test-point", "punto-prueba"), t("the test point", "el punto de prueba"), t("Choose an inequality, move the test point, and see whether the substitution comes out true or false, with a warning when the point falls on the boundary.", "Elija una desigualdad, mueva el punto de prueba y compruebe si la sustitución resulta verdadera o falsa, con un aviso cuando el punto cae sobre la frontera."))}'''

    s3 = f'''<p>{t("A system of inequalities is graphed one inequality at a time. The <strong>feasible region</strong> is where all the shadings overlap: the intersection of the half-planes. Every point of that region meets all the inequalities at once.", "Un sistema de desigualdades se grafica desigualdad por desigualdad. La <strong>región factible</strong> es la zona donde se traslapan todos los sombreados: la intersección de los semiplanos. Cualquier punto de esa región cumple todas las desigualdades a la vez.")}</p>
{fig_triangulo()}
<p>{t("The shaded triangle is the feasible region of the system x ≥ 0, y ≥ 0, and x + y ≤ 4. All its points meet the three conditions.", "El triángulo sombreado es la región factible del sistema x ≥ 0, y ≥ 0 y x + y ≤ 4. Todos sus puntos cumplen las tres condiciones.")}</p>
{caja("ojo", t("Each inequality cuts, never adds", "Cada desigualdad recorta, nunca agranda"), t("<p>When you add one more condition, the region can only stay the same or get smaller. Sometimes it disappears completely: then the system has no solution.</p>", "<p>Al añadir una condición más, la región solo puede quedarse igual o hacerse más pequeña. A veces desaparece del todo: entonces el sistema no tiene solución.</p>"))}
{enlace(n, t("region", "region"), t("the feasible region", "la región factible"), t("Add the inequalities of a system one at a time and watch the region get cut, including the case where it disappears completely.", "Añada las desigualdades del sistema una a una y observe cómo la región se va recortando, incluido el caso en que desaparece por completo."))}'''

    s4 = f'''<p>{t("To check whether a point is in the solution region, substitute it into <strong>all</strong> the inequalities of the system. If it meets all of them, it belongs to the region; if it fails even one, it does not.", "Para comprobar si un punto está en la región solución, se sustituye en <strong>todas</strong> las desigualdades del sistema. Si las cumple todas, pertenece a la región; si falla en una, no.")}</p>
{ejemplo(t("Example 2: is (1, 1) in the region of the system y ≤ x + 1 and y ≥ 0?", "Ejemplo 2 · ¿Está (1, 1) en la región del sistema y ≤ x + 1 ; y ≥ 0?"),
  [("1", t("First:", "Primera:"), t("1 ≤ 1 + 1, that is, 1 ≤ 2. True.", "1 ≤ 1 + 1, es decir, 1 ≤ 2. Verdadero.")), ("2", t("Second:", "Segunda:"), t("1 ≥ 0. True.", "1 ≥ 0. Verdadero.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Yes, (1, 1) belongs to the region.</strong>", "<strong>Sí, (1, 1) pertenece a la región.</strong>"))])}
{practica("p4", t("Practice 4 — One inequality", "Práctica 4 — Una desigualdad"), t("Is (1, 1) in y ≤ x + 1?", "¿Está (1, 1) en y ≤ x + 1?"), [("a", t("No", "No")), ("b", t("Only on the line", "Solo en la recta")), ("c", t("Yes", "Sí"))])}
{practica("p5", t("Practice 5 — y ≤ 2x", "Práctica 5 — y ≤ 2x"), t("Is (2, 5) in y ≤ 2x?", "¿Está (2, 5) en y ≤ 2x?"), [("a", t("Yes", "Sí")), ("b", t("No", "No")), ("c", t("On the line", "En la recta"))])}
{practica("p6", t("Practice 6 — A system", "Práctica 6 — Un sistema"), t("Is (0, 0) in the system y ≥ 0 and x ≥ 0?", "¿Está (0, 0) en el sistema y ≥ 0 ; x ≥ 0?"), [("a", t("Yes, it meets both", "Sí, cumple ambas")), ("b", t("No", "No")), ("c", t("Only one", "Solo una"))])}
{enlace(n, t("check", "verificar"), t("checking points", "la verificación de puntos"), t("Type any point: a table shows whether it meets each inequality, and the graph shows it inside or outside the region.", "Escriba cualquier punto: una tabla muestra si cumple cada desigualdad y la gráfica lo sitúa dentro o fuera de la región."))}'''

    secciones = [("s-" + t("graph", "graficar"), t("Graphing a linear inequality", "Graficar una desigualdad lineal"), s1),
                 ("s-" + t("test-point", "punto-prueba"), t("The test point method", "El método del punto de prueba"), s2),
                 ("s-" + t("system", "sistema"), t("A system of inequalities: the feasible region", "El sistema de desigualdades: la región factible"), s3),
                 ("s-" + t("check", "verificar"), t("Checking whether a point is in the region", "Verificar si un punto pertenece a la región"), s4)]

    lesson = {"next": t("Lesson 7.2", "Lección 7.2"), "review": t("sections 1 and 2", "las secciones 1 y 2"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Dashed is for &lt; and &gt;. This one has ≤.", "Punteada es para &lt; y &gt;. Esta tiene ≤."), "c": t("Every inequality has a boundary line.", "Toda desigualdad tiene línea frontera.")}, "right": t("≤ includes the line: solid.", "≤ incluye la recta: sólida."), "solution": t("Solid.", "Sólida.")},
      "p2": {"ok": "b", "hints": {"a": t("Solid is for ≤ and ≥. This one has &gt;.", "Sólida es para ≤ y ≥. Esta tiene &gt;."), "c": t("There is no double line.", "No existe la línea doble.")}, "right": t("&gt; does not include the line: dashed.", "&gt; no incluye la recta: punteada."), "solution": t("Dashed.", "Punteada.")},
      "p3": {"ok": "c", "hints": {"a": t("The test was true: the origin is on the right side.", "La prueba fue verdadera: el origen está del lado correcto."), "b": t("You shade a whole side, not only the line.", "Se sombrea todo un lado, no solo la recta.")}, "right": t("True: shade the side of (0, 0).", "Verdadero: se sombrea el lado de (0, 0)."), "solution": t("The side of the origin.", "El lado del origen.")},
      "p4": {"ok": "c", "hints": {"a": t("Substitute: 1 ≤ 1 + 1, that is, 1 ≤ 2.", "Sustituya: 1 ≤ 1 + 1, es decir, 1 ≤ 2."), "b": t("On the line, y would equal x + 1 = 2, but y = 1.", "En la recta, y valdría x + 1 = 2, pero y = 1.")}, "right": t("1 ≤ 2 is true.", "1 ≤ 2 es verdadero."), "solution": t("Yes.", "Sí.")},
      "p5": {"ok": "b", "hints": {"a": t("Substitute: 5 ≤ 2(2), that is, 5 ≤ 4.", "Sustituya: 5 ≤ 2(2), es decir, 5 ≤ 4."), "c": t("On the line, y would be 4, but y = 5.", "En la recta, y valdría 4, pero y = 5.")}, "right": t("5 ≤ 4 is false.", "5 ≤ 4 es falso."), "solution": t("No.", "No.")},
      "p6": {"ok": "a", "hints": {"b": t("0 ≥ 0 is true: ≥ includes the equal case.", "0 ≥ 0 es verdadero: ≥ incluye el caso igual."), "c": t("Check both: 0 ≥ 0 and 0 ≥ 0.", "Revise las dos: 0 ≥ 0 y 0 ≥ 0.")}, "right": t("0 ≥ 0 twice: true.", "0 ≥ 0 dos veces: verdadero."), "solution": t("Yes.", "Sí.")},
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("Solid is for ≤ and ≥.", "Sólida es para ≤ y ≥."), "c": t("The thickness does not matter.", "El grosor no importa."), "d": t("The color does not matter.", "El color no importa.")}, "solution": t("Dashed.", "Punteada.")},
      "B": {"ok": "c", "hints": {"a": t("Dashed is for &lt; and &gt;.", "Punteada es para &lt; y &gt;."), "b": t("The thickness does not matter.", "El grosor no importa."), "d": t("The boundary is always drawn.", "La frontera siempre se dibuja.")}, "solution": t("Solid.", "Sólida.")},
      "C": {"ok": "b", "hints": {"a": t("The slope gives the tilt, not the side.", "La pendiente da la inclinación, no el lado."), "c": t("The y-axis does not decide the side.", "El eje y no decide el lado."), "d": t("Lines have no vertex.", "Las rectas no tienen vértice.")}, "solution": t("The test point (0, 0).", "El punto de prueba (0, 0).")},
      "D": {"ok": "d", "hints": {"a": t("The lines are only the boundaries.", "Las rectas son solo las fronteras."), "b": t("It is not the x-axis.", "No es el eje x."), "c": t("It is a whole region, not one point.", "Es toda una región, no un punto.")}, "solution": t("The intersection of the half-planes.", "La intersección de los semiplanos.")},
      "E": {"ok": "a", "hints": {"b": t("Meeting all of them puts it inside.", "Cumplirlas todas lo pone dentro."), "c": t("It may or may not be on a line.", "Puede estar o no en una recta."), "d": t("Yes, you can tell: it meets all.", "Sí se puede saber: las cumple todas.")}, "solution": t("It is in the feasible region.", "Está en la región factible.")},
      "F": {"ok": "c", "hints": {"a": t("One point is the answer for systems of equations.", "Un punto es la respuesta de los sistemas de ecuaciones."), "b": t("Usually the region exists.", "Por lo general la región existe."), "d": t("A region has infinitely many points.", "Una región tiene infinitos puntos.")}, "solution": t("Many: a whole region.", "Muchas: toda una región.")},
      "G": {"ok": "a", "hints": {"b": t("Substitute: 0 ≤ 0 + 2.", "Sustituya: 0 ≤ 0 + 2."), "c": t("On the line, y would be 2.", "En la recta, y valdría 2."), "d": t("You can always substitute.", "Siempre se puede sustituir.")}, "solution": t("Yes: 0 ≤ 2.", "Sí: 0 ≤ 2.")},
      "H": {"ok": "b", "hints": {"a": t("Substitute: 1 &gt; 3?", "Sustituya: ¿1 &gt; 3?"), "c": t("On the line, y would be 3.", "En la recta, y valdría 3."), "d": t("1 &gt; 3 is false.", "1 &gt; 3 es falso.")}, "solution": t("No: 1 &gt; 3 is false.", "No: 1 &gt; 3 es falso.")},
     }}

    quiz = [
     ("A", t("For y < 2x + 1, the boundary line is drawn:", "Para y < 2x + 1, la línea frontera se dibuja:"), [("a", t("dashed", "punteada")), ("b", t("solid", "sólida")), ("c", t("thick", "gruesa")), ("d", t("in red", "roja"))]),
     ("B", t("For y ≥ x − 3, the boundary line is drawn:", "Para y ≥ x − 3, la línea frontera se dibuja:"), [("a", t("dashed", "punteada")), ("b", t("thick", "gruesa")), ("c", t("solid", "sólida")), ("d", t("not at all", "invisible"))]),
     ("C", t("To decide which side to shade, you use:", "Para decidir qué lado sombrear, se usa:"), [("a", t("the slope", "la pendiente")), ("b", t("the test point (0, 0)", "el punto de prueba (0, 0)")), ("c", t("the y-axis", "el eje y")), ("d", t("the vertex", "el vértice"))]),
     ("D", t("The feasible region of a system of inequalities is:", "La región factible de un sistema de desigualdades es:"), [("a", t("the union of the lines", "la unión de las rectas")), ("b", t("the x-axis", "el eje x")), ("c", t("a single point", "un solo punto")), ("d", t("the intersection of the half-planes", "la intersección de los semiplanos"))]),
     ("E", t("If a point satisfies all the inequalities of the system, then:", "Si un punto satisface todas las desigualdades del sistema, entonces:"), [("a", t("it is in the feasible region", "está en la región factible")), ("b", t("it is outside", "está fuera")), ("c", t("it is on the line", "está en la recta")), ("d", t("you cannot tell", "no se puede saber"))]),
     ("F", t("How many solutions does a system of inequalities usually have?", "¿Cuántas soluciones suele tener un sistema de desigualdades?"), [("a", t("one", "una")), ("b", t("none", "ninguna")), ("c", t("many (a whole region)", "muchas (toda una región)")), ("d", t("exactly two", "exactamente dos"))]),
     ("G", t("Is (0, 0) in the region y ≤ x + 2?", "¿Está (0, 0) en la región y ≤ x + 2?"), [("a", t("Yes", "Sí")), ("b", t("No", "No")), ("c", t("Only on the line", "Solo en la recta")), ("d", t("You cannot tell", "No se puede saber"))]),
     ("H", t("Is (3, 1) in the region y > x?", "¿Está (3, 1) en la región y > x?"), [("a", t("Yes", "Sí")), ("b", t("No", "No")), ("c", t("On the line", "En la recta")), ("d", t("Yes, just barely", "Sí, justo"))])]

    tarea = (t("For your own work, with your notebook and graph paper: (1) The production budget: a workshop makes x chairs and y tables. Each chair takes 2 hours and each table 4, with at most 40 hours (2x + 4y ≤ 40). Each chair uses 1 board and each table 3, and there are 24 boards (x + 3y ≤ 24). Also, x ≥ 0 and y ≥ 0. Graph the system, shade the feasible region, and write three combinations (x, y) that can be made and one that cannot. (2) Solid or dashed: for each inequality, decide how to draw the line and which side to shade, using the test point (0, 0): y > 2x − 1; y ≤ −x + 3; 2x + y ≥ 4; x − y < 2; y ≥ 3; x < −1. (3) A viable point? With the system y ≤ x + 2, y > −x, x ≤ 3, substitute each point into the three inequalities and say whether it belongs to the region: (0, 1), (2, −3), (3, 5), (4, 0), and (−1, 1). For those that do not, explain in one sentence which inequality they fail. Pay close attention to the ones that fall on a line. Then do several exercises of each activity on the practice page. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y papel cuadriculado: (1) El presupuesto de producción: un taller fabrica x sillas e y mesas. Cada silla lleva 2 horas y cada mesa 4, y hay como máximo 40 horas (2x + 4y ≤ 40). Cada silla usa 1 tabla y cada mesa 3, y hay 24 tablas (x + 3y ≤ 24). Además, x ≥ 0 e y ≥ 0. Grafique el sistema, sombree la región factible y escriba tres combinaciones (x, y) que sí se pueden fabricar y una que no. (2) Sólida o punteada: para cada desigualdad, decida cómo se traza la línea y qué lado se sombrea, usando el punto de prueba (0, 0): y > 2x − 1; y ≤ −x + 3; 2x + y ≥ 4; x − y < 2; y ≥ 3; x < −1. (3) ¿Punto viable? Con el sistema y ≤ x + 2, y > −x, x ≤ 3, sustituya cada punto en las tres desigualdades y diga si pertenece a la región: (0, 1), (2, −3), (3, 5), (4, 0) y (−1, 1). Para los que no, explique en una frase qué desigualdad no cumplen. Fíjese bien en los que caen sobre una línea. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Think of two limits in your own week, such as hours of work and hours of study. Write them as inequalities and find one combination that fits both.",
               "Piense en dos límites de su propia semana, como horas de trabajo y horas de estudio. Escríbalos como desigualdades y busque una combinación que cumpla los dos."))

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Graph linear inequalities with a solid or dashed line, choose the side with the test point, find the feasible region of a system, and check points.", "Grafique desigualdades lineales con línea sólida o punteada, elija el lado con el punto de prueba, halle la región factible de un sistema y verifique puntos."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Graph</strong> a linear inequality: a solid or dashed line and the correct shaded side.", "<strong>Graficar</strong> una desigualdad lineal: línea sólida o punteada y sombreado del semiplano correcto."),
         t("<strong>Use</strong> the test point (0, 0) to choose the side to shade.", "<strong>Usar</strong> el punto de prueba (0, 0) para elegir el lado que se sombrea."),
         t("<strong>Graph</strong> a system of inequalities and find the feasible region (the intersection).", "<strong>Graficar</strong> un sistema de desigualdades y hallar la región factible (la intersección)."),
         t("<strong>Check</strong> whether a point belongs to the solution region.", "<strong>Verificar</strong> si un punto pertenece a la región solución.")],
        secciones, tarea, quiz,
        t("Self-check checklist for systems of inequalities", "Lista de autoevaluación de los sistemas de desigualdades"),
        t("Self-check checklist: skills for graphing inequalities and their systems", "Lista de autoevaluación: destrezas para graficar desigualdades y sus sistemas"),
        [(t("Drawing the line (solid or dashed)", "Dibujar la línea (sólida o punteada)"), t("I draw the right line for the symbol and graph it accurately.", "Dibujo la línea correcta según el símbolo y la grafico con precisión."), t("I sometimes mix up solid and dashed.", "A veces confundo sólida con punteada."), t("I do not tell the kinds of line apart.", "No distingo el tipo de línea.")),
         (t("Choosing the half-plane (test point)", "Identificar el semiplano (punto de prueba)"), t("I shade the right side with the test point, even when the line goes through the origin.", "Sombreo el lado correcto con el punto de prueba, incluso cuando la recta pasa por el origen."), t("I use it, but I read the result the wrong way.", "Lo uso, pero interpreto mal el resultado."), t("I do not use the test point.", "No uso el punto de prueba.")),
         (t("The feasible region and checking a point", "La región factible y verificar un punto"), t("I find the region and check points in all the inequalities.", "Hallo la región y verifico puntos en todas las desigualdades."), t("I find the region with some mistakes.", "Identifico la región con errores."), t("I do not find the intersection.", "No identifico la intersección."))],
        t("<p>In this lesson you graphed linear inequalities (a solid or dashed line and shading with the test point) and found the feasible region of a system as the intersection of the half-planes.</p>\n<p>In <strong>Lesson 7.2 · Relations and functions, f(x) notation, and domain and range</strong> the subject changes: you will study what a <strong>function</strong> is, how to recognize one with the vertical line test, how to evaluate f(x), and how to find the domain and the range.</p>",
          "<p>En esta lección se graficaron desigualdades lineales (línea sólida o punteada y sombreado con el punto de prueba) y se halló la región factible de un sistema como la intersección de los semiplanos.</p>\n<p>En la <strong>Lección 7.2 · Relaciones y funciones, notación f(x), dominio y rango</strong> se cambia de tema: se estudiará qué es una <strong>función</strong>, cómo reconocerla con la prueba de la línea vertical, cómo evaluar f(x) y cómo identificar el dominio y el rango.</p>"),
        ("7-2", ("", t("Lesson 7.2 · Relations and functions, f(x) notation, and domain and range", "Lección 7.2 · Relaciones y funciones, notación f(x), dominio y rango"))),
        [(t("boundary line", "línea frontera"), t("The line ax + by = c that separates the two half-planes.", "La recta ax + by = c que separa los dos semiplanos.")),
         (t("half-plane", "semiplano"), t("Each of the two sides into which a line divides the plane.", "Cada uno de los dos lados en que una recta divide el plano.")),
         (t("test point", "punto de prueba"), t("A point off the line, usually (0, 0), substituted to choose the side to shade.", "Un punto fuera de la recta, casi siempre (0, 0), que se sustituye para elegir el lado que se sombrea.")),
         (t("feasible region", "región factible"), t("The points that meet all the inequalities of a system at once.", "Los puntos que cumplen todas las desigualdades de un sistema a la vez."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var OPS = ["<", "<=", ">", ">="];
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function yDes(m, b, op){ var s = (m ? (m === 1 ? "" : m === -1 ? "−" : sg(m)) + "x" : "") + (b ? (m ? (b < 0 ? " − " + -b : " + " + b) : sg(b)) : (m ? "" : "0")); return D4(-m, 1, b, op, "y " + SIMB[op] + " " + s); }
var NOMLIN = function(D){ return estricta(D) ? T("dashed", "punteada") : T("solid", "sólida"); };
var LADO = function(D){ /* "above"/"below" for y op …, "right"/"left" for x op … */
  if (D.b){ var op = D.b < 0 ? VOLTEA[D.op] : D.op; return op.charAt(0) === ">" ? T("above", "arriba") : T("below", "abajo"); }
  var op2 = D.a < 0 ? VOLTEA[D.op] : D.op; return op2.charAt(0) === ">" ? T("to the right", "a la derecha") : T("to the left", "a la izquierda"); };

/* ===== MODULE 1 · Graphing one inequality ===== */
function grDibuja(){
  var m = +$("g-m").value, b = +$("g-b").value, op = $("g-op").value, D = yDes(m, b, op);
  $("g-mv").textContent = sg(m); $("g-bv").textContent = sg(b);
  $("g-txt").innerHTML = '<div class="linea">' + dHTML(D) + "</div>" +
    '<div class="linea">' + (estricta(D) ? T("The symbol " + SIMB[op] + " does not include the equal case: the boundary line is <strong>dashed</strong>.", "El símbolo " + SIMB[op] + " no incluye el caso igual: la línea frontera es <strong>punteada</strong>.") : T("The symbol " + SIMB[op] + " includes the equal case: the boundary line is <strong>solid</strong>.", "El símbolo " + SIMB[op] + " incluye el caso igual: la línea frontera es <strong>sólida</strong>.")) + "</div>" +
    '<div class="linea">' + T("y " + SIMB[op] + " … : the shading goes <strong>" + LADO(D) + "</strong> the line, where y is " + (op.charAt(0) === ">" ? "greater" : "less") + ".", "y " + SIMB[op] + " … : se sombrea <strong>" + LADO(D) + "</strong> de la recta, donde y es " + (op.charAt(0) === ">" ? "mayor" : "menor") + ".") + "</div>";
  $("g-graf").innerHTML = grafDes([D]);
}
["g-m", "g-b"].forEach(function(id){ $(id).addEventListener("input", grDibuja); }); $("g-op").addEventListener("change", grDibuja); grDibuja();
/* practice: which inequality is graphed? */
OMR("gq", function(){ var m = elige([-3, -2, -1, 1, 2, 3, 0]), b = aleatorio(-4, 4), op = elige(OPS), D = yDes(m, b, op), vert = Math.random() < .15, k;
  if (vert){ k = nz(-5, 5); D = D4(1, 0, k, op, "x " + SIMB[op] + " " + sg(k)); }
  var otros = OPS.filter(function(o){ return o !== op; }).map(function(o){ return vert ? D4(1, 0, k, o, "x " + SIMB[o] + " " + sg(k)) : yDes(m, b, o); });
  return {enun: T("Which inequality is graphed?", "¿Qué desigualdad está graficada?") + grafDes([D], {etiquetas: false}), correcta: "ok",
    opciones: [{clave: "ok", html: dHTML(D)}].concat(otros.map(function(E, i){ return {clave: "m" + i, html: dHTML(E)}; })),
    pista: T("Look at two things: is the line solid or dashed? Is the shading " + (vert ? "to the right or to the left" : "above or below") + "?", "Fíjese en dos cosas: ¿la línea es sólida o punteada? ¿El sombreado está " + (vert ? "a la derecha o a la izquierda" : "arriba o abajo") + "?"),
    bien: T("The line is " + NOMLIN(D) + " and the shading is " + LADO(D) + ": ", "La línea es " + NOMLIN(D) + " y el sombreado está " + LADO(D) + ": ") + dTxt(D) + "."};
});

/* ===== MODULE 2 · The test point ===== */
var DES_T = [D4(2, 1, 4, ">"), D4(-1, 1, 1, "<=", "y ≤ x + 1"), D4(-2, 1, -3, ">=", "y ≥ 2x − 3"), D4(1, 1, 5, "<"), D4(-2, 1, 0, "<", "y < 2x"), D4(3, -2, 6, ">=")];
function tpItem(){ return DES_T[+$("t-des").value]; }
function tpDibuja(){
  var D = tpItem(), x = leeDecimal($("t-x").value), y = leeDecimal($("t-y").value), out = $("t-txt");
  if (x === null || y === null){ out.innerHTML = '<div class="linea">' + T("Type a number for x and for y.", "Escriba un número en x y en y.") + "</div>"; return; }
  var S = dSust(D, x, y), v = dVerdad(S), fr = enFrontera(D, x, y);
  out.innerHTML = '<div class="linea">' + T("Substitute ", "Se sustituye ") + par(x, y) + ": " + S.txt + " → " + sg(r4(S.izq)) + " " + SIMB[S.op] + " " + sg(r4(S.der)) + "</div>" +
    '<div class="linea veredicto" style="color:' + (v ? "#1b5e20" : "#b71c1c") + '">' + (v ? T("True.", "Verdadero.") : T("False.", "Falso.")) + "</div>" +
    '<div class="linea">' + (fr ? T("<strong>Careful:</strong> this point is ON the boundary line, so it does not tell you which side to shade. Choose a point off the line.", "<strong>Cuidado:</strong> este punto está SOBRE la línea frontera, así que no sirve para decidir el lado. Elija un punto fuera de la recta.") :
      v ? T("The point makes it true: shade <strong>the side of the point</strong>.", "El punto la cumple: se sombrea <strong>el lado del punto</strong>.") : T("The point makes it false: shade <strong>the other side</strong>.", "El punto no la cumple: se sombrea <strong>el lado contrario</strong>.")) + "</div>";
  $("t-graf").innerHTML = grafDes([D], {prueba: [x, y]});
}
["t-x", "t-y"].forEach(function(id){ $(id).addEventListener("input", tpDibuja); }); $("t-des").addEventListener("change", tpDibuja);
$("t-origen").addEventListener("click", function(){ $("t-x").value = 0; $("t-y").value = 0; tpDibuja(); }); tpDibuja();
OMR("tq", function(){ var a = nz(-4, 4), b = nz(-3, 3), c = Math.random() < .2 ? 0 : nz(-8, 8), op = elige(OPS), D = D4(a, b, c, op), pr = c ? [0, 0] : [1, 0];
  if (a < 0 && b < 0){ D.a = -a; D.b = -b; D.c = -c; D.op = VOLTEA[op]; }
  var g = dMcd(dMcd(D.a, D.b), D.c) || 1; D.a /= g; D.b /= g; D.c /= g;
  if (!c && enFrontera(D, 1, 0)) pr = [0, 1];
  var S = dSust(D, pr[0], pr[1]), v = dVerdad(S), txt = dStd(D);
  return {enun: T("To graph ", "Para graficar ") + envuelve(txt, dVoz(txt)) + T(", which side do you shade?", ", ¿qué lado se sombrea?"), correcta: v ? "mismo" : "otro", enOrden: true,
    opciones: [{clave: "mismo", html: T("the side of ", "el lado de ") + par(pr[0], pr[1])}, {clave: "otro", html: T("the side opposite ", "el lado contrario a ") + par(pr[0], pr[1])}, {clave: "linea", html: T("only the line", "solo la recta")}],
    pista: (c ? "" : T("The line goes through (0, 0), so use " + par(pr[0], pr[1]) + ". ", "La recta pasa por (0, 0), así que se usa " + par(pr[0], pr[1]) + ". ")) + T("Substitute the test point and see whether it comes out true.", "Sustituya el punto de prueba y vea si resulta verdadero."),
    porClave: {linea: T("You always shade a whole side (a half-plane).", "Siempre se sombrea todo un lado (un semiplano).")},
    bien: (c ? "" : T("The line goes through the origin, so the test point is " + par(pr[0], pr[1]) + ". ", "La recta pasa por el origen, así que el punto de prueba es " + par(pr[0], pr[1]) + ". ")) + S.txt + " → " + sg(r4(S.izq)) + " " + SIMB[S.op] + " " + sg(r4(S.der)) + ": " + (v ? T("true, so shade its side.", "verdadero, se sombrea su lado.") : T("false, so shade the other side.", "falso, se sombrea el lado contrario.")) + grafDes([D], {prueba: pr})};
});

/* ===== MODULE 3 · The feasible region ===== */
var R0 = {x0: -3, x1: 8, y0: -3, y1: 8}, R7 = {x0: -7, x1: 7, y0: -7, y1: 7}, R9 = {x0: -2, x1: 9, y0: -2, y1: 9};
var SISTEMAS = [
 {r: R0, ds: [D4(1, 0, 0, ">=", "x ≥ 0"), D4(0, 1, 0, ">=", "y ≥ 0"), D4(1, 1, 4, "<=", "x + y ≤ 4")],
  com: [T("x ≥ 0 keeps the right half of the plane, including the y-axis.", "x ≥ 0 deja la mitad derecha del plano, incluido el eje y."), T("y ≥ 0 adds the top half: only the first quadrant is left.", "y ≥ 0 añade la mitad de arriba: queda solo el primer cuadrante."), T("x + y ≤ 4 cuts the quadrant with a diagonal and leaves a triangle with vertices (0, 0), (4, 0), and (0, 4).", "x + y ≤ 4 recorta el cuadrante con una diagonal y deja un triángulo de vértices (0, 0), (4, 0) y (0, 4).")]},
 {r: R7, ds: [D4(-1, 1, 1, "<=", "y ≤ x + 1"), D4(0, 1, 0, ">=", "y ≥ 0")],
  com: [T("Everything below the line y = x + 1, including the line itself.", "Todo lo que queda por debajo de la recta y = x + 1, incluida la propia recta."), T("y ≥ 0 removes everything below the x-axis: a wedge open to the right is left.", "y ≥ 0 elimina lo que está por debajo del eje x: queda una cuña abierta hacia la derecha.")]},
 {r: R7, ds: [D4(-2, 1, -3, ">", "y > 2x − 3"), D4(1, 1, 4, "<", "y < −x + 4")],
  com: [T("Everything above the line y = 2x − 3; the line is dashed because it is not included.", "Todo lo que queda por encima de la recta y = 2x − 3; la línea va punteada porque no se incluye."), T("The second one cuts from above and leaves a wedge with both boundaries dashed: no point of the lines belongs to the region.", "La segunda recorta por arriba y deja una cuña con las dos fronteras punteadas: ningún punto de las líneas pertenece a la región.")]},
 {r: R9, ds: [D4(1, 0, 0, ">=", "x ≥ 0"), D4(0, 1, 0, ">=", "y ≥ 0"), D4(2, 1, 8, "<=", "2x + y ≤ 8"), D4(1, 1, 5, "<=", "x + y ≤ 5")],
  com: [T("x ≥ 0: the right half.", "x ≥ 0: la mitad derecha."), T("y ≥ 0: the first quadrant, with no negative values.", "y ≥ 0: el primer cuadrante, sin valores negativos."), T("2x + y ≤ 8 leaves a triangle with vertices (0, 0), (4, 0), and (0, 8).", "2x + y ≤ 8 deja un triángulo de vértices (0, 0), (4, 0) y (0, 8)."), T("x + y ≤ 5 cuts one more corner: a quadrilateral with vertices (0, 0), (4, 0), (3, 2), and (0, 5). This is the typical shape of production problems.", "x + y ≤ 5 recorta una esquina más: un cuadrilátero de vértices (0, 0), (4, 0), (3, 2) y (0, 5). Es la forma típica de los problemas de producción.")]},
 {r: R7, ds: [D4(-1, 1, 2, ">=", "y ≥ x + 2"), D4(-1, 1, -1, "<=", "y ≤ x − 1")],
  com: [T("Everything above the line y = x + 2.", "Todo lo que queda por encima de la recta y = x + 2."), T("The second asks to be below y = x − 1, a parallel line three units lower. No point meets both: the region disappears and the system has no solution.", "La segunda pide estar por debajo de y = x − 1, una paralela tres unidades más abajo. Ningún punto cumple las dos: la región desaparece y el sistema no tiene solución.")]}];
var rEst = {i: 0, n: 0};
function rPinta(){
  var S = SISTEMAS[rEst.i], L = S.ds.slice(0, rEst.n);
  $("r-graf").innerHTML = grafDes(L, {rango: S.r, cada: false, region: true});
  $("r-txt").innerHTML = S.ds.slice(0, rEst.n).map(function(D, k){ return '<div class="linea"><strong>' + (k + 1) + ".</strong> " + S.com[k] + "</div>"; }).join("") || '<div class="linea">' + T("Press the button to add the first inequality.", "Pulse el botón para añadir la primera desigualdad.") + "</div>";
  var fin = rEst.n >= S.ds.length; $("r-sig").disabled = fin; $("r-todo").disabled = fin;
  $("r-sig").textContent = rEst.n ? T("Add the next inequality", "Añadir la siguiente desigualdad") : T("Add the first inequality", "Añadir la primera desigualdad");
}
$("r-sis").addEventListener("change", function(){ rEst = {i: +$("r-sis").value, n: 0}; rPinta(); });
$("r-sig").addEventListener("click", function(){ rEst.n++; rPinta(); });
$("r-todo").addEventListener("click", function(){ rEst.n = SISTEMAS[rEst.i].ds.length; rPinta(); });
$("r-reinicia").addEventListener("click", function(){ rEst.n = 0; rPinta(); }); rPinta();
/* practice: which system has this region? */
function sisAzar(){ var L, ok, k = 0;
  do { var m1 = elige([-2, -1, 1, 2, 0]), m2, b1 = aleatorio(-3, 3), b2;
    do { m2 = elige([-2, -1, 1, 2, 0]); } while (m2 === m1); b2 = aleatorio(-3, 3);
    L = [yDes(m1, b1, elige(OPS)), yDes(m2, b2, elige(OPS))]; var reg = verticesReg(L, R7); ok = reg.length > 2 && areaPoli(reg) > 4; k++; } while (!ok && k < 100);
  return L; }
OMR("rq", function(){ var L = sisAzar(), op0 = L[0].op, op1 = L[1].op;
  var cambia = function(D){ var m = -D.a, b = D.c; return yDes(m, b, VOLTEA[D.op]); };
  var opc = [[cambia(L[0]), L[1]], [L[0], cambia(L[1])], [cambia(L[0]), cambia(L[1])]];
  return {enun: T("The green region is the solution of which system?", "La región verde es la solución de ¿qué sistema?") + grafDes(L, {cada: false, etiquetas: false}), correcta: "ok",
    opciones: [{clave: "ok", html: sisDesHTML(L)}].concat(opc.map(function(S, i){ return {clave: "m" + i, html: sisDesHTML(S)}; })),
    pista: T("Look at each line on its own: is the green region above or below it? Is it solid or dashed?", "Mire cada recta por separado: ¿la región verde queda arriba o abajo de ella? ¿Es sólida o punteada?"),
    bien: L.map(function(D){ return dTxt(D) + ": " + T("the region is ", "la región está ") + LADO(D) + T(" the ", " de la línea ") + NOMLIN(D) + (ES ? "" : " line"); }).join("; ") + "."};
});

/* ===== MODULE 4 · Checking a point ===== */
function veDibuja(){
  var S = SISTEMAS[+$("v-sis").value], x = leeDecimal($("v-x").value), y = leeDecimal($("v-y").value), out = $("v-txt");
  if (x === null || y === null){ out.innerHTML = '<div class="linea">' + T("Type a number for x and for y.", "Escriba un número en x y en y.") + "</div>"; $("v-graf").innerHTML = grafDes(S.ds, {rango: S.r}); return; }
  var todas = true, filas = S.ds.map(function(D){ var Sb = dSust(D, x, y), v = dVerdad(Sb); if (!v) todas = false;
    return "<tr><td>" + dTxt(D) + "</td><td>" + Sb.txt + " → " + sg(r4(Sb.izq)) + " " + SIMB[Sb.op] + " " + sg(r4(Sb.der)) + (enFrontera(D, x, y) ? T(" (on the line)", " (sobre la línea)") : "") + '</td><td class="' + (v ? "si" : "no") + '">' + (v ? T("✓ true", "✓ verdadero") : T("✗ false", "✗ falso")) + "</td></tr>"; }).join("");
  out.innerHTML = '<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">' + T("Substitution of the point in each inequality", "Sustitución del punto en cada desigualdad") + '</caption><thead><tr><th scope="col">' + T("Inequality", "Desigualdad") + '</th><th scope="col">' + T("Substitution", "Sustitución") + '</th><th scope="col">' + T("Result", "Resultado") + "</th></tr></thead><tbody>" + filas + "</tbody></table></div>" +
    '<div class="linea veredicto" style="color:' + (todas ? "#1b5e20" : "#b71c1c") + '">' + (todas ? T(par(x, y) + " meets all of them: it IS in the region.", par(x, y) + " las cumple todas: SÍ está en la región.") : T(par(x, y) + " fails at least one: it is NOT in the region.", par(x, y) + " falla en al menos una: NO está en la región.")) + "</div>";
  $("v-graf").innerHTML = grafDes(S.ds, {rango: S.r, punto: [x, y]});
}
["v-x", "v-y"].forEach(function(id){ $(id).addEventListener("input", veDibuja); }); $("v-sis").addEventListener("change", veDibuja); veDibuja();
OMR("vq", function(){ var L = sisAzar(), x, y, k = 0, frontera = Math.random() < .35;
  if (frontera){ var D = elige(L); do { x = aleatorio(-5, 5); y = (D.c - D.a * x) / D.b; k++; } while ((y !== Math.round(y) || Math.abs(y) > 6) && k < 50); if (k >= 50){ x = aleatorio(-5, 5); y = aleatorio(-5, 5); } }
  else { x = aleatorio(-5, 5); y = aleatorio(-5, 5); }
  var res = L.map(function(D){ return dVerdad(dSust(D, x, y)); }), dentro = res[0] && res[1];
  return {enun: T("Is ", "¿Está ") + par(x, y) + T(" in the region of ", " en la región de ") + sisDesHTML(L) + "?", correcta: dentro ? "si" : res[0] || res[1] ? "una" : "ninguna", enOrden: true,
    opciones: [{clave: "si", html: T("Yes: it meets both", "Sí: cumple las dos")}, {clave: "una", html: T("No: it meets only one", "No: cumple solo una")}, {clave: "ninguna", html: T("No: it meets neither", "No: no cumple ninguna")}],
    pista: T("Substitute the point in each inequality. Careful with points on a line: ≤ and ≥ include them, &lt; and &gt; do not.", "Sustituya el punto en cada desigualdad. Cuidado con los puntos sobre una línea: ≤ y ≥ los incluyen, &lt; y &gt; no."),
    bien: L.map(function(D, i){ var S = dSust(D, x, y); return S.txt + " → " + sg(r4(S.izq)) + " " + SIMB[S.op] + " " + sg(r4(S.der)) + ": " + (res[i] ? T("true", "verdadero") : T("false", "falso")) + (enFrontera(D, x, y) ? T(" (on the line)", " (sobre la línea)") : ""); }).join("; ") + "." + grafDes(L, {punto: [x, y]})};
});
'''

def practica_pagina():
    n = N
    rango = lambda i, et, mn, mx, st, v: f'<div class="campo"><label for="{i}">{et} <output id="{i}v"></output></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    campo = lambda i, et, v: f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{i}" value="{v}" style="width:5em"></div>'
    ops = [("<", "&lt;"), ("<=", "≤"), (">", "&gt;"), (">=", "≥")]
    des = [("0", "2x + y &gt; 4"), ("1", "y ≤ x + 1"), ("2", "y ≥ 2x − 3"), ("3", "x + y &lt; 5"), ("4", "y &lt; 2x"), ("5", "3x − 2y ≥ 6")]
    sis = [("0", "x ≥ 0 ; y ≥ 0 ; x + y ≤ 4"), ("1", "y ≤ x + 1 ; y ≥ 0"), ("2", "y &gt; 2x − 3 ; y &lt; −x + 4"), ("3", "x ≥ 0 ; y ≥ 0 ; 2x + y ≤ 8 ; x + y ≤ 5"), ("4", t("y ≥ x + 2 ; y ≤ x − 1 (no solution)", "y ≥ x + 2 ; y ≤ x − 1 (sin solución)"))]
    mods = [
     (t("graph", "graficar"), t("Graphing a linear inequality", "Graficar una desigualdad lineal"),
      f'''      <p>{t("Choose the symbol and move the slope (m) and the intercept (b) of y … mx + b. Watch the line turn solid or dashed and the shading move.", "Elija el símbolo y mueva la pendiente (m) y el intercepto (b) de y … mx + b. Observe cómo la línea se vuelve sólida o punteada y cómo se mueve el sombreado.")}</p>
      <div class="panel"><div class="campos">{n4.lista("g-op", t("Symbol: y", "Símbolo: y"), ops, "<=")}{rango("g-m", "m =", -4, 4, 1, 1)}{rango("g-b", "b =", -6, 6, 1, 1)}</div></div>
{n4.salida("g-txt")}
      <div id="g-graf"></div>
{B.om("gq", t("Practice: which inequality is graphed?", "Practique: ¿qué desigualdad está graficada?"))}'''),
     (t("test-point", "punto-prueba"), t("The test point method", "El método del punto de prueba"),
      f'''      <p>{t("Choose an inequality and a test point. The point is substituted: if it makes the inequality true, shade its side; if not, shade the other side.", "Elija una desigualdad y un punto de prueba. El punto se sustituye: si cumple la desigualdad, se sombrea su lado; si no, el lado contrario.")}</p>
      <div class="panel"><div class="campos">{n4.lista("t-des", t("Inequality", "Desigualdad"), des)}{campo("t-x", t("Test point · x", "Punto de prueba · x"), 0)}{campo("t-y", "y", 0)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="t-origen">{t("Use the origin (0, 0)", "Usar el origen (0, 0)")}</button></div></div>
{n4.salida("t-txt")}
      <div id="t-graf"></div>
{B.om("tq", t("Practice: which side do you shade?", "Practique: ¿qué lado se sombrea?"))}'''),
     (t("region", "region"), t("The system and the feasible region", "El sistema y la región factible"),
      f'''      <p>{t("A system is graphed one inequality at a time. The <strong>feasible region</strong> (in green) is where all the shadings overlap. Add the inequalities and watch the region get cut.", "Un sistema se grafica una desigualdad a la vez. La <strong>región factible</strong> (en verde) es la zona donde se traslapan todos los sombreados. Añada las desigualdades y observe cómo se recorta la región.")}</p>
      <div class="panel"><div class="campos">{n4.lista("r-sis", t("System", "Sistema"), sis)}</div>
        <div class="fila-btn"><button type="button" class="btn" id="r-sig">{t("Add the first inequality", "Añadir la primera desigualdad")}</button><button type="button" class="btn-sec" id="r-todo">{t("Show the whole region", "Mostrar la región completa")}</button><button type="button" class="btn-sec" id="r-reinicia">{t("Start again", "Reiniciar")}</button></div></div>
      <div id="r-graf"></div>
{n4.salida("r-txt")}
      <div class="caja-tip">{t("<strong>Each inequality cuts, never adds.</strong> With one more condition, the region can only stay the same or get smaller, and sometimes it disappears: then the system has no solution.", "<strong>Cada desigualdad recorta, nunca agranda.</strong> Con una condición más, la región solo puede quedarse igual o hacerse más pequeña, y a veces desaparece: entonces el sistema no tiene solución.")}</div>
{B.om("rq", t("Practice: which system has this region?", "Practique: ¿qué sistema tiene esta región?"))}'''),
     (t("check", "verificar"), t("Checking whether a point is in the region", "Verificar si un punto pertenece a la región"),
      f'''      <p>{t("You do not need the picture to know whether a point is in the region: substitute it into <strong>all</strong> the inequalities. If it meets all of them, it is inside; if it fails even one, it is outside.", "Para saber si un punto pertenece a la región no hace falta el dibujo: se sustituye en <strong>todas</strong> las desigualdades. Si las cumple todas, está dentro; si falla en una sola, está fuera.")}</p>
      <div class="panel"><div class="campos">{n4.lista("v-sis", t("System", "Sistema"), sis)}{campo("v-x", t("Point · x", "Punto · x"), 1)}{campo("v-y", "y", 1)}</div>
        <p class="nota">{t("Try points right on a boundary: that is where &lt; and ≤ make a difference.", "Pruebe puntos justo sobre una frontera: ahí se nota la diferencia entre &lt; y ≤.")}</p></div>
{n4.salida("v-txt")}
      <div id="v-graf"></div>
{B.om("vq", t("Practice: is it in the region?", "Practique: ¿está en la región?"))}''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Sistemas de desigualdades lineales: graficar la región solución")
