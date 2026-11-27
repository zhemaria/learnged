"""LearnGED · Estudios sociales · Lección 2.1 · Gráficas, tablas y la calculadora TI-30XS (EN/ES).
Fuente: sociales/soc-2-1.html. Las gráficas se dibujan aquí (ciencia.grafica y SVG propios).
Uso: python3 tools/build_soc_2_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, cita

N = "2-1"
SAL = [(1938, 0.25), (1950, 0.75), (1961, 1.15), (1968, 1.60), (1974, 2.00), (1980, 3.10), (1990, 3.80), (1997, 5.15), (2009, 7.25)]
ESC = [(9, 31), (10, 33), (10, 29), (11, 36), (12, 38), (12, 42), (13, 45), (13, 40), (14, 48), (14, 53), (15, 52), (16, 61), (16, 55), (17, 66), (18, 71), (18, 64)]
TV = [(0, 3.6), (1, 3.5), (1, 3.2), (2, 3.3), (2, 3.0), (3, 3.1), (3, 2.8), (4, 2.9), (4, 2.6), (5, 2.5), (5, 2.8), (6, 2.3), (6, 2.5), (7, 2.1), (8, 2.2), (8, 1.9)]
APE = [(3, 2.6), (4, 3.4), (5, 2.2), (5, 3.1), (6, 2.9), (6, 2.4), (7, 3.5), (7, 2.7), (8, 2.3), (8, 3.2), (9, 2.8), (10, 3.3), (10, 2.5), (11, 3.0), (12, 2.4), (13, 3.1)]
F = 'font-family="Segoe UI, Arial, sans-serif"'


def titulo():
    return t("Graphs, tables, and the TI-30XS calculator", "Gráficas, tablas y la calculadora TI-30XS")


def din(v):
    return f"${v:.2f}"


def svg_escalones():
    """Las mismas nueve cifras con una línea recta y con escalones."""
    ml, mt, W, Hh = 66, 20, 620, 250
    X = lambda a: ml + (a - 1935) / (2015 - 1935) * W
    Y = lambda v: mt + Hh - v / 8 * Hh
    s = [f'<svg class="diagrama" style="max-width:720px" viewBox="0 0 720 340" role="img" aria-label="' +
         t("Line graph of the federal minimum wage from 1938 to 2009, drawn two ways. A solid line connects the nine values directly, so it looks like the wage rose a little every year. A dashed step line stays flat at each value until the next law and then jumps up, which is what really happened: for example, it stays at 5.15 dollars from 1997 to 2009 and then jumps to 7.25.",
           "Gráfica de líneas del salario mínimo federal de 1938 a 2009, dibujada de dos maneras. Una línea continua une directamente los nueve valores, así que parece que el salario subía un poco cada año. Una línea escalonada de trazos se queda plana en cada valor hasta la siguiente ley y luego salta, que es lo que de verdad pasó: por ejemplo, se queda en 5.15 dólares de 1997 a 2009 y luego salta a 7.25.") +
         '" xmlns="http://www.w3.org/2000/svg">']
    for v in range(0, 9):
        s.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{ml + W}" y2="{Y(v):.1f}" stroke="#e1e6ea"/><text x="{ml - 8}" y="{Y(v) + 5:.1f}" text-anchor="end" {F} font-size="13" fill="#3d4753">${v}</text>')
    for a in range(1940, 2016, 10):
        s.append(f'<text x="{X(a):.1f}" y="{mt + Hh + 20}" text-anchor="middle" {F} font-size="13" fill="#3d4753">{a}</text><line x1="{X(a):.1f}" y1="{mt + Hh}" x2="{X(a):.1f}" y2="{mt + Hh + 5}" stroke="#1a2330"/>')
    s.append(f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + Hh}" stroke="#1a2330" stroke-width="1.5"/><line x1="{ml}" y1="{mt + Hh}" x2="{ml + W}" y2="{mt + Hh}" stroke="#1a2330" stroke-width="1.5"/>')
    recta = " ".join(f"{X(a):.1f},{Y(v):.1f}" for a, v in SAL)
    esc = []
    for i, (a, v) in enumerate(SAL):
        if i:
            esc.append(f"{X(a):.1f},{Y(SAL[i - 1][1]):.1f}")
        esc.append(f"{X(a):.1f},{Y(v):.1f}")
    esc.append(f"{X(2014):.1f},{Y(7.25):.1f}")
    s.append(f'<polyline points="{recta}" fill="none" stroke="#7a4a2e" stroke-width="3"/>')
    s.append(f'<polyline points="{" ".join(esc)}" fill="none" stroke="#2a7f86" stroke-width="3" stroke-dasharray="7 4"/>')
    for a, v in SAL:
        s.append(f'<circle cx="{X(a):.1f}" cy="{Y(v):.1f}" r="4.5" fill="#1a2330"/>')
    s.append(f'<line x1="{ml + 14}" y1="{mt + 10}" x2="{ml + 44}" y2="{mt + 10}" stroke="#7a4a2e" stroke-width="3"/><text x="{ml + 50}" y="{mt + 15}" {F} font-size="13" font-weight="700" fill="#7a4a2e">{t("Straight line: suggests a little rise every year", "Línea recta: sugiere una pequeña subida cada año")}</text>')
    s.append(f'<line x1="{ml + 14}" y1="{mt + 32}" x2="{ml + 44}" y2="{mt + 32}" stroke="#2a7f86" stroke-width="3" stroke-dasharray="7 4"/><text x="{ml + 50}" y="{mt + 37}" {F} font-size="13" font-weight="700" fill="#1f5f66">{t("Steps: flat until a new law, then a jump", "Escalones: plano hasta una nueva ley, luego un salto")}</text>')
    s.append(f'<text x="{ml + W / 2}" y="{mt + Hh + 48}" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Year", "Año")}</text>')
    s.append(f'<text x="16" y="{mt + Hh / 2}" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330" transform="rotate(-90 16 {mt + Hh / 2})">{t("Dollars per hour", "Dólares por hora")}</text>')
    s.append("</svg>")
    return "".join(s)


def svg_circular():
    import math
    datos = [(t("Everything else", "Todo lo demás"), 27, "#7a4a2e"), (t("Health", "Salud"), 26, "#2a7f86"), (t("Social Security", "Seguridad Social"), 23, "#c99a2e"),
             (t("Defense", "Defensa"), 13, "#3949ab"), (t("Interest on the debt", "Intereses de la deuda"), 11, "#8d8d8d")]
    cx, cy, r = 170, 160, 130
    aria = t("Pie chart of an illustrative federal budget: everything else 27 percent, health 26 percent, Social Security 23 percent, defense 13 percent, interest on the debt 11 percent.",
             "Gráfica circular de un presupuesto federal ilustrativo: todo lo demás 27 %, salud 26 %, Seguridad Social 23 %, defensa 13 %, intereses de la deuda 11 %.")
    s = [f'<svg class="diagrama" style="max-width:620px" viewBox="0 0 620 320" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">']
    ang = -90
    for i, (n, p, c) in enumerate(datos):
        a2 = ang + p * 3.6
        x1, y1 = cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang))
        x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
        s.append(f'<path d="M{cx} {cy} L{x1:.1f} {y1:.1f} A{r} {r} 0 {1 if p > 50 else 0} 1 {x2:.1f} {y2:.1f} Z" fill="{c}" stroke="#fff" stroke-width="2"/>')
        am = math.radians((ang + a2) / 2)
        s.append(f'<text x="{cx + r * .66 * math.cos(am):.1f}" y="{cy + r * .66 * math.sin(am) + 5:.1f}" text-anchor="middle" {F} font-size="15" font-weight="700" fill="#fff">{p}%</text>')
        s.append(f'<rect x="340" y="{70 + i * 38}" width="20" height="20" rx="4" fill="{c}"/><text x="370" y="{86 + i * 38}" {F} font-size="15" fill="#1a2330">{n} · {p}%</text>')
        ang = a2
    s.append("</svg>")
    return "".join(s)


def disp(puntos, xe, ye, patron, py=None):
    spec = {"tipo": "puntos", "xEtq": xe, "yEtq": ye, "series": [{"nombre": "", "puntos": [list(p) for p in puntos]}], "patron": patron}
    if py:
        spec["py"] = py
    return C.grafica(spec, C.describe(spec), ancho=560, alto=320, y0=min(p[1] for p in puntos) - 0.01, y1=max(p[1] for p in puntos))


def leccion():
    P = C.Practicas()
    barras = {"tipo": "barras", "xEtq": t("Year the law took effect", "Año en que entró en vigor la ley"), "yEtq": t("Dollars per hour", "Dólares por hora"),
              "barras": [{"etq": str(a), "valor": v, "txt": din(v)} for a, v in SAL]}
    tabla_sal = C.tabla(t("Federal minimum wage per hour, in the year it took effect", "Salario mínimo federal por hora, en el año en que entró en vigor"),
                        [t("Year", "Año"), t("Wage per hour", "Salario por hora")], [[str(a), din(v)] for a, v in SAL])

    s1 = f"""<p>{t("Most mistakes on the test do not come from bad arithmetic. They come from answering before looking. These five steps take less than twenty seconds and prevent almost all of them.",
"La mayoría de los errores del examen no vienen de calcular mal, sino de contestar antes de haber mirado. Estos cinco pasos se hacen en menos de veinte segundos y evitan casi todos.")}</p>
{C.tabla(t("The five steps, always in this order", "Los cinco pasos, siempre en este orden"), [t("Step", "Paso"), t("Ask yourself", "Pregúntese")],
  [[t("1 · Title", "1 · Título"), t("What is this graph about, and what is it not about?", "¿De qué habla esta gráfica y de qué no?")],
   [t("2 · Axes", "2 · Ejes"), t("What is on the horizontal axis, and what is on the vertical axis?", "¿Qué hay en el eje horizontal y qué en el vertical?")],
   [t("3 · Units", "3 · Unidades"), t("Dollars, people, percents, thousands of people? Mixing up “thousands” and “ones” changes the answer a thousand times.", "¿Dólares, personas, porcentajes, miles de personas? Confundir «miles» con «unidades» cambia la respuesta mil veces.")],
   [t("4 · Scale", "4 · Escala"), t("Where does the vertical axis start? If it does not start at zero, differences look bigger than they are.", "¿Dónde empieza el eje vertical? Si no empieza en cero, las diferencias parecen más grandes de lo que son.")],
   [t("5 · Trend", "5 · Tendencia"), t("Only now: does it go up, go down, stay the same, or show no pattern?", "Solo ahora: ¿sube, baja, se mantiene o no hay patrón?")]])}
{C.caja("ojo", t("The step almost everyone skips", "El paso que casi todos saltan"), "<p>" + t("Step 4. A bar graph whose vertical axis starts at 40 instead of 0 can turn a difference of three points into a mountain. It is not faking: the numbers are correct. It is the same one-sided choice of Topic 1, made with a scale.", "El 4. Una gráfica de barras cuyo eje vertical empieza en 40 en vez de en 0 puede convertir una diferencia de tres puntos en una montaña. No es falsear: los números son correctos. Es la misma selección interesada del Tema 1, hecha con una escala.") + "</p>")}"""

    s2 = f"""<p>{t("Each kind of graph answers a different question. Choosing the wrong one is not a matter of style: it changes what the reader concludes.", "Cada tipo de gráfica sirve para una pregunta distinta. Elegir la equivocada no es una cuestión de estilo: cambia lo que el lector concluye.")}</p>
<h3>{t("Bar graph · comparing amounts", "Gráfica de barras · comparar cantidades")}</h3>
<p>{t("The federal minimum wage of the United States, in dollars per hour, in nine of the years when a law raised it. These are real historical figures (U.S. Department of Labor).", "El salario mínimo federal de los Estados Unidos, en dólares por hora, en nueve de los años en que una ley lo subió. Son cifras históricas reales (Departamento de Trabajo de los Estados Unidos).")}</p>
{C.grafica(barras, C.describe(barras), ancho=620, alto=330)}
{tabla_sal}
<h3>{t("Line graph · following a change over time", "Gráfica de líneas · seguir un cambio en el tiempo")}</h3>
<p>{t("The same nine numbers, now on a real time axis, drawn two ways.", "Las mismas nueve cifras, ahora sobre un eje de años real, dibujadas de dos maneras.")}</p>
{svg_escalones()}
{C.caja("ojo", t("The trap of this lesson", "La trampa de esta lección"), "<p>" + t("From 1997 to 2009 the federal minimum wage did not move: twelve years at $5.15. The straight line draws that stretch as a gentle slope, and someone reading quickly will conclude it rose little by little. The step line draws it flat and then a jump. <strong>A straight line between two points is a guess about what happened in between, and it is not always true.</strong>", "Entre 1997 y 2009 el salario mínimo federal no se movió: doce años en 5.15 dólares. La línea recta dibuja ese tramo como una cuesta suave, y quien la lea deprisa concluirá que subió poco a poco. La línea escalonada lo dibuja plano y luego un salto. <strong>Una línea recta entre dos puntos es una suposición sobre lo que pasó en medio, y no siempre es cierta.</strong>") + "</p>")}
<h3>{t("Circle graph · parts of a whole", "Gráfica circular · partes de un total")}</h3>
<p>{t("How a federal budget is split among five categories. Illustrative data, rounded so they add up to 100%.", "Cómo se reparte un presupuesto federal entre cinco categorías. Datos ilustrativos, redondeados para que sumen 100 %.")}</p>
{svg_circular()}
<p>{t("A circle graph only works when the parts add up to a whole and there are few of them. With more than five or six slices, the eye can no longer compare, and a table works better.", "El círculo solo sirve cuando las partes suman un todo y son pocas. Con más de cinco o seis sectores el ojo ya no compara, y una tabla informa mejor.")}</p>
{C.tabla(t("Which graph for which question", "Qué gráfica para qué pregunta"), [t("Graph", "Gráfica"), t("Use it to…", "Sirve para…")],
  [[t("Bar", "De barras"), t("compare amounts across categories", "comparar cantidades entre categorías")], [t("Line", "De líneas"), t("follow a change over time", "seguir un cambio en el tiempo")],
   [t("Circle", "Circular"), t("show the parts of one whole", "mostrar las partes de un todo")], [t("Scatter plot", "De dispersión"), t("see whether two measured things go together", "ver si dos cosas medidas van juntas")]])}
<h3>{t("Try it", "Inténtelo")}</h3>
{P(t("Practice 1 · Choose the graph", "Práctica 1 · Elija la gráfica"), t("You want to show how a city budget is split among four departments. Which graph do you choose?", "Quiere mostrar cómo se reparte un presupuesto municipal entre cuatro departamentos. ¿Qué gráfica elige?"),
   [t("Line graph", "De líneas"), t("Circle graph", "Circular"), t("Scatter plot", "De dispersión")], 1,
   {0: t("Nothing here changes over time.", "Aquí nada cambia en el tiempo."), 2: t("There are not two measured variables.", "No hay dos variables medidas.")}, t("Four parts of one whole: a circle graph (a bar graph would also work).", "Cuatro partes de un todo: una gráfica circular (también serviría una de barras)."))}
{P(t("Practice 2 · Read the table", "Práctica 2 · Lea la tabla"), t("According to the table, how long did the federal minimum wage stay at $5.15?", "Según la tabla, ¿cuánto tiempo estuvo el salario mínimo federal en 5.15 dólares?"),
   [t("One year", "Un año"), t("Five years", "Cinco años"), t("Twelve years, from 1997 to 2009", "Doce años, de 1997 a 2009")], 2,
   {0: t("Find 1997 and the next year in the table.", "Busque 1997 y el año siguiente en la tabla."), 1: t("Subtract: 2009 − 1997.", "Reste: 2009 − 1997.")}, t("2009 − 1997 = 12 years without a change.", "2009 − 1997 = 12 años sin cambio."))}
{C.enlace(N, t("graphs", "graficas"), t("Read the graph", "Lea la gráfica"), t("Questions about the minimum wage graph and choosing the right kind of graph.", "Preguntas sobre la gráfica del salario mínimo y sobre qué gráfica elegir."))}"""

    s3 = f"""<p>{t("As soon as a graph relates two measured things, you need to know which one leads.", "En cuanto una gráfica relaciona dos cosas medidas, hay que saber cuál manda.")}</p>
<ul><li>{t("The <strong>independent variable</strong> is the one that is supposed to act, the one that is chosen, or the one that simply happens first. It goes on the <strong>horizontal</strong> axis.", "La <strong>variable independiente</strong> es la que se supone que actúa, la que se elige o la que simplemente ocurre primero. Va en el eje <strong>horizontal</strong>.")}</li>
<li>{t("The <strong>dependent variable</strong> is the one that is supposed to respond. It goes on the <strong>vertical</strong> axis.", "La <strong>variable dependiente</strong> es la que se supone que responde. Va en el eje <strong>vertical</strong>.")}</li></ul>
{C.caja("tip", t("A trick that almost never fails", "Un truco que casi nunca falla"), "<p>" + t("Complete the sentence “if ______ changes, ______ will change.” The first blank is the independent variable and goes along the bottom. <strong>Time is always independent:</strong> nothing we measure makes the years change.", "Complete la frase «si cambia ______, cambiará ______». Lo primero es la independiente y va abajo. <strong>El tiempo es siempre independiente:</strong> nada de lo que midamos hace que cambien los años.") + "</p>")}
<h3>{t("Scatter plot · do two things go together?", "Gráfica de dispersión · ¿van juntas dos cosas?")}</h3>
<p>{t("Sixteen areas: average years of schooling and average yearly household income, in thousands of dollars. Illustrative data.", "Dieciséis territorios: años medios de escolaridad e ingreso medio anual por hogar, en miles de dólares. Datos ilustrativos.")}</p>
{disp(ESC, t("Years of schooling", "Años de escolaridad"), t("Income (thousands of $)", "Ingreso (miles de $)"), t("The points rise from left to right: a positive correlation, with a wide cloud.", "Los puntos suben de izquierda a derecha: una correlación positiva, con una nube ancha."), py=10)}
<p>{t("Each point is one area. The cloud rises from left to right: where there are more years of schooling, there tends to be more income. That is a <strong>positive correlation</strong>. Notice that the cloud is wide: some areas have the same schooling and very different incomes.", "Cada punto es un territorio. La nube sube de izquierda a derecha: donde hay más años de escolaridad, tiende a haber más ingreso. Eso es una <strong>correlación positiva</strong>. Fíjese en que la nube es ancha: hay territorios con la misma escolaridad y un ingreso muy distinto.")}</p>
<div class="dos-graficas">
<div><h4>{t("Negative correlation", "Correlación negativa")}</h4>{disp(TV, t("Hours of TV per day", "Horas de televisión al día"), t("Grade average", "Calificación media"), t("The points go down from left to right: a negative correlation.", "Los puntos bajan de izquierda a derecha: una correlación negativa."), py=0.5)}<p>{t("Hours of TV and grade average. The cloud goes down to the right: when one goes up, the other tends to go down. Illustrative data.", "Horas de televisión y calificación media. La nube baja hacia la derecha: cuando una sube, la otra tiende a bajar. Datos ilustrativos.")}</p></div>
<div><h4>{t("No correlation", "Sin correlación")}</h4>{disp(APE, t("Letters in last name", "Letras del apellido"), t("Grade average", "Calificación media"), t("The points are scattered with no direction: no correlation.", "Los puntos están dispersos sin dirección: no hay correlación."), py=0.5)}<p>{t("Letters in the last name and grade average. The points have no direction. Nobody expects a name to affect grades, so this is what a cloud looks like when there really is no relationship. Illustrative data.", "Letras del apellido y calificación media. Los puntos no tienen dirección. Nadie espera que el apellido influya en las notas, y por eso así se ve una nube cuando de verdad no hay relación. Datos ilustrativos.")}</p></div>
</div>"""

    s4 = f"""<p>{t("This is the central point of the lesson, and the one the test rewards. <strong>When two things rise together, that does not prove that one makes the other rise.</strong> For any correlation there are always four possible explanations, and the graph alone cannot choose among them.",
"Este es el punto central de la lección, y el que el examen premia. <strong>Que dos cosas suban juntas no prueba que una haga subir a la otra.</strong> Ante cualquier correlación hay siempre cuatro explicaciones posibles, y la gráfica por sí sola no permite elegir entre ellas.")}</p>
{C.tabla(t("Four explanations for the same cloud of points", "Cuatro explicaciones para la misma nube de puntos"), [t("Explanation", "Explicación"), t("Schooling and income", "Escolaridad e ingreso")],
  [[t("1 · A causes B", "1 · A causa B"), t("More years of school lead to better jobs.", "Más años de escuela llevan a mejores empleos.")],
   [t("2 · B causes A", "2 · B causa A"), t("Families with more income can keep their children in school longer.", "Las familias con más ingreso pueden mantener a sus hijos más años en la escuela.")],
   [t("3 · A third thing causes both", "3 · Una tercera cosa causa las dos"), t("A prosperous area has both better schools and better jobs.", "Un territorio próspero tiene a la vez mejores escuelas y mejores empleos.")],
   [t("4 · Chance", "4 · Casualidad"), t("With few data, two things can go together by luck.", "Con pocos datos, dos cosas pueden ir juntas por azar.")]])}
{C.caja("tip", t("How the answer that scores points sounds", "Cómo suena la respuesta que puntúa"), "<p>" + t("Not: “The graph proves that studying more makes you earn more.” Yes: “The graph shows a positive correlation between schooling and income; to know whether one causes the other, we would need data the graph does not give.” The right answer to a scatter plot never starts with “this proves that,” but with <strong>“this is consistent with.”</strong>", "No: «La gráfica demuestra que estudiar más hace ganar más». Sí: «La gráfica muestra una correlación positiva entre escolaridad e ingreso; para saber si una causa la otra harían falta datos que la gráfica no ofrece». La respuesta correcta ante una gráfica de dispersión nunca empieza por «esto demuestra que», sino por <strong>«esto es compatible con»</strong>.") + "</p>")}
{P(t("Practice 3 · Variables", "Práctica 3 · Variables"), t("In a graph of a city’s population from 1950 to 2020, what goes on the horizontal axis?", "En una gráfica de la población de una ciudad entre 1950 y 2020, ¿qué va en el eje horizontal?"),
   [t("The population, because it is what matters", "La población, porque es lo importante"), t("It depends on who draws the graph", "Depende de quién dibuje la gráfica"), t("The year, because time is always the independent variable", "El año, porque el tiempo es siempre la variable independiente")], 2,
   {0: t("Importance does not decide the axis.", "La importancia no decide el eje."), 1: t("There is a rule.", "Hay una regla.")}, t("Nothing we measure makes the years change.", "Nada de lo que midamos hace que cambien los años."))}
{P(t("Practice 4 · Correlation", "Práctica 4 · Correlación"), t("In a city, ice cream sales and the number of drownings go up and down together during the year. What best explains it?", "En una ciudad, la venta de helados y el número de ahogamientos suben y bajan juntos a lo largo del año. ¿Qué lo explica mejor?"),
   [t("A third variable, hot weather, causes both", "Una tercera variable, el calor, causa las dos"), t("Eating ice cream makes drowning more likely", "Comer helado aumenta el riesgo de ahogarse"), t("The correlation proves a cause", "La correlación demuestra una causa")], 0,
   {1: t("Is there a common reason for both?", "¿Hay una razón común para las dos?"), 2: t("Correlation never proves cause by itself.", "La correlación nunca demuestra una causa por sí sola.")}, t("In summer people buy more ice cream and swim more. Heat drives both.", "En verano se compra más helado y se nada más. El calor mueve las dos cosas."))}
{C.enlace(N, t("variables", "variables"), t("Variables and correlation", "Variables y correlación"), t("Find the independent variable and choose the explanation the data allow.", "Encuentre la variable independiente y elija la explicación que permiten los datos."))}"""

    s5 = f"""<p>{t("The <strong>TI-30XS MultiView</strong> is the calculator allowed on the GED® test; on the Social Studies test it appears on screen for many questions. Two things about it cause almost all avoidable mistakes.", "La <strong>TI-30XS MultiView</strong> es la calculadora que permite el examen del GED®; en el de Estudios Sociales aparece en pantalla en muchas preguntas. Dos cosas de ella causan casi todos los errores evitables.")}</p>
<h3>{t("The toggle key", "La tecla de alternancia")}</h3>
<p>{t("The calculator often gives results as fractions. If the question asks for a decimal and you copy the fraction, the answer counts as wrong even if the value is the same. The <strong>toggle key</strong> (◄ ►) switches the result on the screen between fraction and decimal.", "La calculadora devuelve muchos resultados en forma de fracción. Si la pregunta pide un decimal y usted copia la fracción, la respuesta cuenta como incorrecta aunque el valor sea el mismo. La <strong>tecla de alternancia</strong> (◄ ►) cambia el resultado de la pantalla entre fracción y decimal.")}</p>
{C.caja("tip", t("A habit worth making automatic", "Un hábito que conviene automatizar"), "<p>" + t("After every result, look at what the question asks for. If it asks for a decimal and you see a fraction, press the toggle key before you write anything.", "Después de cada resultado, mire qué pide la pregunta. Si pide decimal y ve una fracción, pulse la alternancia antes de escribir nada.") + "</p>")}
<h3>{t("The order of operations", "La jerarquía de operaciones")}</h3>
<p>{t("The calculator follows the math order: parentheses, then powers, then multiplication and division from left to right, and last addition and subtraction. That is good, but it means you must type the parentheses you have in your head.", "La calculadora respeta el orden matemático: primero paréntesis, después potencias, luego multiplicaciones y divisiones de izquierda a derecha, y por último sumas y restas. Eso es bueno, pero significa que hay que escribir los paréntesis que uno tiene en la cabeza.")}</p>
{C.ejemplo(t("The most expensive mistake: the percent change from 40 to 52", "El error más caro: el cambio porcentual de 40 a 52"),
  [("✗", t("<code>52 − 40 ÷ 40 =</code> gives <strong>51</strong>: the calculator divides 40 by 40 first.", "<code>52 − 40 ÷ 40 =</code> da <strong>51</strong>: la calculadora divide primero 40 entre 40.")),
   ("✓", t("<code>( 52 − 40 ) ÷ 40 =</code> gives <strong>0.3</strong>, that is, <strong>30%</strong>. With the toggle key you would see 3/10.", "<code>( 52 − 40 ) ÷ 40 =</code> da <strong>0.3</strong>, es decir, <strong>30 %</strong>. Con la alternancia vería 3/10."))],
  t("Both were typed correctly and the calculator answered both without complaint. But the first one answers a different question. A calculator never warns you that it answered something other than what you meant to ask.", "Las dos se teclearon bien y la calculadora resolvió las dos sin protestar. Pero la primera responde a otra pregunta. Una calculadora nunca avisa de que ha contestado algo distinto de lo que usted quería preguntar."))}
{P(t("Practice 5 · Calculator", "Práctica 5 · Calculadora"), t("What does the calculator show if you type <code>2 + 3 × 4 =</code>?", "¿Qué muestra la calculadora si se teclea <code>2 + 3 × 4 =</code>?"), ["14", "20", "24"], 0,
   {1: t("That would be (2 + 3) × 4.", "Eso sería (2 + 3) × 4."), 2: t("Multiplication first: 3 × 4.", "Primero la multiplicación: 3 × 4.")}, t("3 × 4 = 12, then 2 + 12 = 14.", "3 × 4 = 12, y después 2 + 12 = 14."))}
{C.enlace(N, t("calculator", "calculadora"), t("Calculator clinic", "Clínica de la calculadora"), t("New expressions every time: predict what the calculator will show.", "Expresiones nuevas cada vez: anticipe lo que mostrará la calculadora."))}"""

    G = lambda *a: C.ged_item(P, *a)
    paro = {"tipo": "linea", "xEtq": t("Year", "Año"), "yEtq": t("Unemployment rate (%)", "Tasa de desempleo (%)"), "px": 2, "py": 2,
            "series": [{"nombre": "", "puntos": [[2007, 4.6], [2008, 5.8], [2009, 9.3], [2010, 9.6], [2011, 8.9], [2012, 8.1], [2013, 7.4], [2014, 6.2], [2015, 5.3], [2016, 4.9]]}]}
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK). You may use the calculator.",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SSP.10.a", "2", t("<em>U.S. unemployment rate, yearly average (Bureau of Labor Statistics):</em>", "<em>Tasa de desempleo de los Estados Unidos, promedio anual (Oficina de Estadísticas Laborales):</em>") + C.grafica(paro, C.describe(paro), ancho=560, alto=300, y0=0, y1=10) +
   t("Which statement is supported by the graph?", "¿Qué afirmación sostiene la gráfica?"),
   [t("Unemployment peaked in 2010 and then fell every year through 2016.", "El desempleo llegó a su punto más alto en 2010 y después bajó todos los años hasta 2016."), t("Unemployment rose every year from 2007 to 2016.", "El desempleo subió todos los años de 2007 a 2016."), t("Unemployment was the same in 2007 and 2016.", "El desempleo fue igual en 2007 y en 2016."), t("A new law caused unemployment to fall after 2010.", "Una nueva ley hizo bajar el desempleo después de 2010.")], 0,
   {1: t("Look at the line after 2010.", "Mire la línea después de 2010."), 2: t("Compare 4.6 and 4.9.", "Compare 4.6 y 4.9."), 3: t("The graph shows no laws; it cannot show a cause.", "La gráfica no muestra leyes; no puede mostrar una causa.")},
   t("The highest point is 9.6% in 2010; after that each value is lower than the one before.", "El punto más alto es 9.6 % en 2010; después cada valor es menor que el anterior."))}
{G(2, "SSP.10.c", "2–3", t("<em>A study of U.S. counties finds that counties with more public libraries per person also have higher average incomes.</em><br>Which conclusion is best supported?", "<em>Un estudio de los condados de los Estados Unidos encuentra que los condados con más bibliotecas públicas por habitante también tienen ingresos medios más altos.</em><br>¿Qué conclusión está mejor sostenida?"),
   [t("The two are correlated, but the study does not show that libraries raise incomes.", "Las dos cosas están correlacionadas, pero el estudio no muestra que las bibliotecas suban los ingresos."), t("Building libraries will raise incomes in any county.", "Construir bibliotecas subirá los ingresos en cualquier condado."), t("High incomes cause people to read more.", "Los ingresos altos hacen que la gente lea más."), t("Libraries and income have nothing to do with each other.", "Las bibliotecas y el ingreso no tienen nada que ver.")], 0,
   {1: t("That claims a cause the study did not test.", "Eso afirma una causa que el estudio no puso a prueba."), 2: t("That also claims a cause, just in the other direction.", "Eso también afirma una causa, solo que al revés."), 3: t("The study found that they go together.", "El estudio encontró que van juntas.")},
   t("A third variable (for example, richer counties can pay for more libraries) could explain both.", "Una tercera variable (por ejemplo, que los condados más ricos pueden pagar más bibliotecas) podría explicar las dos."))}
{G(3, "SSP.10.b", "2", t("<em>A researcher wants to graph how the number of years a worker has been in a union relates to that worker’s hourly wage.</em><br>Where should each variable go?", "<em>Un investigador quiere hacer una gráfica de cómo se relacionan los años que un trabajador lleva en un sindicato y su salario por hora.</em><br>¿Dónde debe ir cada variable?"),
   [t("Years in the union on the horizontal axis; hourly wage on the vertical axis", "Los años en el sindicato en el eje horizontal; el salario por hora en el vertical"), t("Hourly wage on the horizontal axis; years in the union on the vertical axis", "El salario por hora en el eje horizontal; los años en el sindicato en el vertical"), t("Both on the vertical axis", "Las dos en el eje vertical"), t("It does not matter", "No importa")], 0,
   {1: t("Complete: “if ___ changes, ___ will change.”", "Complete: «si cambia ___, cambiará ___»."), 2: t("A graph of two variables needs two axes.", "Una gráfica de dos variables necesita dos ejes."), 3: t("The convention matters for reading the graph.", "La convención importa para leer la gráfica.")},
   t("The researcher thinks wage responds to years of membership, so years are independent (horizontal) and wage is dependent (vertical).", "El investigador piensa que el salario responde a los años de afiliación: los años son la independiente (horizontal) y el salario la dependiente (vertical)."))}
{G(4, "SSP.6.c", "2", tabla_sal + t("Between which two laws did the minimum wage rise by the largest <strong>amount</strong> in dollars?", "¿Entre qué dos leyes subió más el salario mínimo, en <strong>dólares</strong>?"),
   [t("1997 to 2009", "De 1997 a 2009"), t("1974 to 1980", "De 1974 a 1980"), t("1990 to 1997", "De 1990 a 1997"), t("1938 to 1950", "De 1938 a 1950")], 0,
   {1: t("$3.10 − $2.00 = $1.10.", "3.10 − 2.00 = 1.10 dólares."), 2: t("$5.15 − $3.80 = $1.35.", "5.15 − 3.80 = 1.35 dólares."), 3: t("$0.75 − $0.25 = $0.50.", "0.75 − 0.25 = 0.50 dólares.")},
   t("$7.25 − $5.15 = $2.10, the largest jump in dollars, even though it came after twelve years without a change.", "7.25 − 5.15 = 2.10 dólares, el mayor salto, aunque llegó después de doce años sin cambio."))}"""

    secciones = [
        ("s1", t("The five steps, always in this order", "Los cinco pasos, siempre en este orden"), s1),
        ("s2", t("Four ways to show data", "Cuatro formas de mostrar datos"), s2),
        ("s3", t("Which variable goes on which axis", "Qué variable va en cada eje"), s3),
        ("s4", t("Correlation is not causation", "Correlación no es causalidad"), s4),
        ("s5", t("The TI-30XS calculator clinic", "Clínica de la TI-30XS"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("The five steps out loud (15 minutes).", "Los cinco pasos en voz alta (15 minutos)."), t("Find three graphs in a newspaper or on a government website. For each one, say the five steps out loud before drawing any conclusion. Note which one has a vertical axis that does not start at zero. <em>Check:</em> if it took you more than thirty seconds per graph, you were reading the content instead of the structure.", "Busque tres gráficas en un periódico o en una página oficial. Con cada una, diga los cinco pasos en voz alta antes de sacar ninguna conclusión. Anote en cuál el eje vertical no empieza en cero. <em>Compruebe:</em> si tardó más de treinta segundos por gráfica, estaba leyendo el contenido en vez de la estructura.")),
        (t("Schooling and income (25 minutes).", "Escolaridad e ingreso (25 minutos)."), t("With the scatter plot of section 3, write three sentences: which variable is independent and why, how you would describe the correlation, and one explanation different from “studying more makes you earn more.” <em>Check:</em> if your third sentence uses the word “proves,” rewrite it.", "Con la gráfica de dispersión de la sección 3, escriba tres frases: cuál es la variable independiente y por qué, cómo describiría la correlación, y una explicación distinta de «estudiar más hace ganar más». <em>Compruebe:</em> si su tercera frase usa la palabra «demuestra», reescríbala.")),
        (t("Twelve calculations (30 minutes).", "Doce operaciones (30 minutos)."), t("With the calculator: the percent changes from 25 to 30, from 80 to 60, and from 12 to 15; the divisions 3 ÷ 8, 5 ÷ 16, and 7 ÷ 20; and 2 + 3 × 4, (2 + 3) × 4, 100 − 20 ÷ 5, (100 − 20) ÷ 5, 6 + 6 ÷ 6 + 6, and (6 + 6) ÷ (6 + 6). <em>Check:</em> 20%, −25%, 25%; 0.375, 0.3125, 0.35; 14, 20, 96, 16, 13, 1.", "Con la calculadora: los cambios porcentuales de 25 a 30, de 80 a 60 y de 12 a 15; las divisiones 3 ÷ 8, 5 ÷ 16 y 7 ÷ 20; y 2 + 3 × 4, (2 + 3) × 4, 100 − 20 ÷ 5, (100 − 20) ÷ 5, 6 + 6 ÷ 6 + 6 y (6 + 6) ÷ (6 + 6). <em>Compruebe:</em> 20 %, −25 %, 25 %; 0.375, 0.3125, 0.35; 14, 20, 96, 16, 13, 1.")),
    ]
    Q = t
    quiz = [
        (Q("Before drawing any conclusion from a graph, the first step is to…", "Antes de sacar cualquier conclusión de una gráfica, el primer paso es…"),
         [Q("find the highest value", "buscar el valor más alto"), Q("read the title, axes, units, and scale", "leer el título, los ejes, las unidades y la escala"), Q("subtract the first value from the last", "restar el primer dato del último"), Q("decide whether you agree", "decidir si está de acuerdo")], 1,
         {0: Q("Structure before content.", "La estructura antes que el contenido."), 2: Q("First know what the numbers measure.", "Primero hay que saber qué miden los números."), 3: Q("Agreeing comes much later, if at all.", "Estar de acuerdo viene mucho después, si acaso.")}, Q("Title, axes, units, scale, and only then the trend.", "Título, ejes, unidades, escala, y solo entonces la tendencia.")),
        (Q("According to the table, the federal minimum wage went from…", "Según la tabla, el salario mínimo federal pasó de…"),
         [Q("$0.25 in 1938 to $7.25 in 2009", "0.25 dólares en 1938 a 7.25 en 2009"), Q("$0.75 in 1938 to $7.25 in 2009", "0.75 dólares en 1938 a 7.25 en 2009"), Q("$0.25 in 1938 to $5.15 in 2009", "0.25 dólares en 1938 a 5.15 en 2009"), Q("$1.15 in 1950 to $7.25 in 2009", "1.15 dólares en 1950 a 7.25 en 2009")], 0,
         {1: Q("$0.75 is 1950.", "0.75 es de 1950."), 2: Q("$5.15 is 1997.", "5.15 es de 1997."), 3: Q("$1.15 is 1961.", "1.15 es de 1961.")}, Q("Read the first and last rows.", "Lea la primera y la última fila.")),
        (Q("A vertical axis that starts at 40 instead of 0 makes…", "Un eje vertical que empieza en 40 en vez de en 0 hace que…"),
         [Q("the data wrong", "los datos sean incorrectos"), Q("the differences look bigger than they are", "las diferencias parezcan mayores de lo que son"), Q("the graph impossible to read", "la gráfica no se pueda leer"), Q("the units change", "las unidades cambien")], 1,
         {0: Q("The numbers are still correct.", "Los números siguen siendo correctos."), 2: Q("It can be read; it just exaggerates.", "Se puede leer; solo exagera."), 3: Q("Units stay the same.", "Las unidades no cambian.")}, Q("The drawing exaggerates; the numbers do not lie.", "El dibujo exagera; los números no mienten.")),
        (Q("A circle graph works best when…", "Una gráfica circular conviene cuando…"),
         [Q("there are many categories", "hay muchas categorías"), Q("you follow a change over time", "se sigue un cambio en el tiempo"), Q("the parts add up to one whole and there are few", "las partes suman un todo y son pocas"), Q("you relate two measured variables", "se relacionan dos variables medidas")], 2,
         {0: Q("Too many slices cannot be compared.", "Demasiados sectores no se pueden comparar."), 1: Q("That is a line graph.", "Eso es una gráfica de líneas."), 3: Q("That is a scatter plot.", "Eso es una gráfica de dispersión.")}, Q("Parts of a whole, few slices.", "Partes de un todo, pocos sectores.")),
        (Q("The independent variable goes on the…", "La variable independiente va en el eje…"),
         [Q("vertical axis", "vertical"), Q("horizontal axis", "horizontal"), Q("axis the artist chooses", "que elija quien dibuja"), Q("title", "título")], 1,
         {0: Q("The vertical axis is for the one that responds.", "El vertical es para la que responde."), 2: Q("There is a convention.", "Hay una convención."), 3: Q("The title names the topic.", "El título nombra el tema.")}, Q("Horizontal: the one that acts.", "Horizontal: la que actúa.")),
        (Q("In a graph of a city’s population from 1950 to 2020, time is…", "En una gráfica de la población de una ciudad entre 1950 y 2020, el tiempo es…"),
         [Q("the dependent variable", "la variable dependiente"), Q("the independent variable", "la variable independiente"), Q("neither", "ninguna de las dos"), Q("it depends on the city", "depende de la ciudad")], 1,
         {0: Q("Nothing makes the years change.", "Nada hace que cambien los años."), 2: Q("It is one of the two.", "Es una de las dos."), 3: Q("Time is always independent.", "El tiempo es siempre independiente.")}, Q("Time always acts; it never responds.", "El tiempo siempre actúa; nunca responde.")),
        (Q("A cloud of points that goes down from left to right shows…", "Una nube de puntos que baja de izquierda a derecha muestra…"),
         [Q("a positive correlation", "una correlación positiva"), Q("a negative correlation", "una correlación negativa"), Q("no correlation", "ausencia de correlación"), Q("a cause", "una causa")], 1,
         {0: Q("Positive goes up.", "La positiva sube."), 2: Q("There is a direction.", "Hay una dirección."), 3: Q("A cloud never shows a cause by itself.", "Una nube nunca muestra una causa por sí sola.")}, Q("When one goes up, the other tends to go down.", "Cuando una sube, la otra tiende a bajar.")),
        (Q("Ice cream sales and drownings rise together every summer. The best explanation is…", "La venta de helados y los ahogamientos suben juntos cada verano. La mejor explicación es…"),
         [Q("ice cream makes drowning more likely", "el helado aumenta el riesgo de ahogarse"), Q("drownings make people buy ice cream", "los ahogamientos hacen vender helado"), Q("a third variable, hot weather, causes both", "una tercera variable, el calor, causa las dos"), Q("the correlation proves a cause", "la correlación demuestra la causa")], 2,
         {0: Q("Look for a common reason.", "Busque una razón común."), 1: Q("That reverses the cause and still misses it.", "Eso invierte la causa y sigue sin acertar."), 3: Q("It never does by itself.", "Nunca lo hace por sí sola.")}, Q("A third variable.", "Una tercera variable.")),
        (Q("Faced with a scatter plot, the answer that scores points begins…", "Ante una gráfica de dispersión, la respuesta que puntúa empieza por…"),
         [Q("“This proves that…”", "«Esto demuestra que…»"), Q("“This is consistent with…”", "«Esto es compatible con…»"), Q("“This confirms the cause of…”", "«Esto confirma la causa de…»"), Q("“This shows for sure that…”", "«Esto muestra con seguridad que…»")], 1,
         {0: Q("A scatter plot never proves a cause.", "Una dispersión nunca demuestra una causa."), 2: Q("Same mistake with other words.", "El mismo error con otras palabras."), 3: Q("Same mistake again.", "Otra vez el mismo error.")}, Q("A correlation is consistent with several explanations.", "Una correlación es compatible con varias explicaciones.")),
        (Q("For the percent change from 40 to 52 you type…", "Para el cambio porcentual de 40 a 52 se teclea…"),
         ["52 − 40 ÷ 40 =", "( 52 − 40 ) ÷ 40 =", "52 ÷ 40 − 40 =", "40 ÷ ( 52 − 40 ) ="], 1,
         {0: Q("Without parentheses it divides first and gives 51.", "Sin paréntesis divide primero y da 51."), 2: Q("That is not the formula.", "Esa no es la fórmula."), 3: Q("That is upside down.", "Eso está al revés.")}, Q("0.3 = 30%.", "0.3 = 30 %.")),
        (Q("The screen shows 3/8 and the question asks for a decimal. You…", "La pantalla muestra 3/8 y la pregunta pide un decimal. Usted…"),
         [Q("write 3/8, since it is the same value", "escribe 3/8, porque vale lo mismo"), Q("press the toggle key and write 0.375", "pulsa la alternancia y escribe 0.375"), Q("start over", "vuelve a empezar"), Q("round to 0.4", "redondea a 0.4")], 1,
         {0: Q("The format counts.", "El formato cuenta."), 2: Q("No need: one key does it.", "No hace falta: basta una tecla."), 3: Q("Do not round unless asked.", "No redondee si no se lo piden.")}, Q("The toggle key switches fraction and decimal.", "La alternancia cambia entre fracción y decimal.")),
        (Q("What does the calculator show for <code>100 − 20 ÷ 5 =</code>?", "¿Qué muestra la calculadora con <code>100 − 20 ÷ 5 =</code>?"), ["16", "96", "80", "4"], 1,
         {0: Q("That would need parentheses: (100 − 20) ÷ 5.", "Eso necesitaría paréntesis: (100 − 20) ÷ 5."), 2: Q("Divide first: 20 ÷ 5.", "Primero se divide: 20 ÷ 5."), 3: Q("That is only 20 ÷ 5.", "Eso es solo 20 ÷ 5.")}, Q("20 ÷ 5 = 4, then 100 − 4 = 96.", "20 ÷ 5 = 4, y después 100 − 4 = 96.")),
    ]
    filas = [
        (t("Read title, axes, units, and scale", "Lee título, ejes, unidades y escala"), t("I go through the five steps before concluding, and I notice when a scale exaggerates.", "Recorro los cinco pasos antes de concluir, y noto cuándo una escala exagera."), t("I read title and axes but miss the units or where the scale starts.", "Leo título y ejes, pero se me pasan las unidades o el origen de la escala."), t("I answer from the numbers without reading the axes (<a href=\"#s1\">review section 1</a>).", "Respondo con los números sin leer los ejes (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Tell independent from dependent", "Distingue variable independiente y dependiente"), t("I use “if ___ changes, ___ will change” and get it right easily.", "Uso «si cambia ___, cambiará ___» y acierto con soltura."), t("I get it when one variable is time, but doubt otherwise.", "Acierto cuando una es el tiempo, pero dudo en los demás casos."), t("I mix them up (<a href=\"#s3\">review section 3</a>).", "Las confundo (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Describe correlation without claiming cause", "Describe la correlación sin afirmar causa"), t("I describe it, say it is not enough for a cause, and give at least two other explanations.", "La describo, digo que no basta para una causa y doy al menos dos explicaciones más."), t("I avoid the word “cause” but leave it implied.", "Evito la palabra «causa», pero la dejo implícita."), t("I write that the graph proves a cause (<a href=\"#s4\">review section 4</a>).", "Escribo que la gráfica demuestra una causa (<a href=\"#s4\">repase la sección 4</a>).")),
        (t("Use the calculator well", "Usa la calculadora con soltura"), t("I group with parentheses, toggle to decimal when asked, and estimate first.", "Agrupo con paréntesis, cambio a decimal cuando lo piden y estimo antes."), t("I use parentheses sometimes, and give fractions when decimals are asked.", "Uso paréntesis a veces, y entrego fracciones cuando piden decimales."), t("I type straight through and accept the first number (<a href=\"#s5\">review section 5</a>).", "Tecleo de corrido y acepto el primer número (<a href=\"#s5\">repase la sección 5</a>).")),
    ]
    cierre = "<p>" + t("This lesson set up the tool of the topic: <strong>a graph is read by its structure before its content</strong>. And the sentence that earns the most points on the test: a correlation is consistent with four different explanations, and the graph cannot choose among them.",
                         "Esta lección deja instalada la herramienta del tema: <strong>una gráfica se lee por su estructura antes que por su contenido</strong>. Y la frase que más puntos da en el examen: una correlación es compatible con cuatro explicaciones distintas, y la gráfica no permite elegir entre ellas.") + "</p><p>" + \
             t("Lesson 2.2 goes one level deeper. Before the graph comes the number that sums it up, and those numbers are chosen too. With household incomes from two neighborhoods, you will calculate the mean and the median and see why they can be so different.",
               "La Lección 2.2 baja un nivel más. Antes que la gráfica está el número que la resume, y esos números también se eligen. Con los ingresos por hogar de dos barrios, calculará la media y la mediana y verá por qué pueden ser tan distintas.") + "</p>"
    glosario = [
        (t("Scale (of an axis)", "Escala (de un eje)"), t("The values marked along an axis and where they start.", "Los valores marcados a lo largo de un eje y dónde empiezan.")),
        (t("Independent variable", "Variable independiente"), t("The one that acts or comes first; it goes on the horizontal axis.", "La que actúa o va primero; va en el eje horizontal.")),
        (t("Dependent variable", "Variable dependiente"), t("The one that responds; it goes on the vertical axis.", "La que responde; va en el eje vertical.")),
        (t("Correlation", "Correlación"), t("A pattern in which two variables tend to change together (positive, negative, or none).", "Patrón en el que dos variables tienden a cambiar juntas (positiva, negativa o ninguna).")),
        (t("Causation", "Causalidad"), t("A relationship in which one thing actually makes another happen. A correlation alone does not show it.", "Relación en la que una cosa hace que ocurra otra. Una correlación sola no la demuestra.")),
        (t("Third variable", "Tercera variable"), t("A hidden factor that causes two things to change together.", "Factor oculto que hace que dos cosas cambien juntas.")),
        (t("Toggle key", "Tecla de alternancia"), t("The TI-30XS key that switches a result between fraction and decimal.", "La tecla de la TI-30XS que cambia un resultado entre fracción y decimal.")),
    ]
    estd = C.estandares(["SSP.10.a", "SSP.10.b", "SSP.10.c", "SSP.6.b"], ["E.e", "CG.f"], base=["SSP.6.c"])
    conexion = "<p>" + t("Topic 1 ended with two weeklies from 1905 that told the same meeting and seemed to tell two. Neither lied: each chose what to tell and with which words.",
                         "El Tema 1 terminó con dos semanarios de 1905 que contaban la misma reunión y parecían contar dos. Ninguno mentía: cada uno elegía qué contar y con qué palabras.") + "</p><p>" + \
               t("This topic carries the same suspicion over to numbers. A graph seems more objective than a paragraph, and that is why it is more dangerous: someone also drew it, and chose what to measure, in which units, and where the scale starts. A number does not speak for itself. We start with the most practical thing, which is reading, and with the tool the test lets you use, the calculator. <strong>Good preparation:</strong> Math Level 2 (graphs and percents).",
                 "Este tema traslada esa misma sospecha a los números. Una gráfica parece más objetiva que un párrafo, y por eso es más peligrosa: también la dibujó alguien, que eligió qué medir, en qué unidades y dónde empieza la escala. Un dato no habla solo. Se empieza por lo más práctico, que es saber leer, y por la herramienta que el examen permite usar, la calculadora. <strong>Buena preparación:</strong> el Nivel 2 de Matemáticas (gráficas y porcentajes).") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("A graph is read by its structure before its content. And when two things go together, that does not mean one causes the other.", "Una gráfica se lee por su estructura antes que por su contenido. Y que dos cosas vayan juntas no significa que una cause la otra."),
        ["SSP.10 · " + t("Graphs and correlation", "Gráficas y correlación"), "SSP.6 · " + t("Data in many forms", "Datos en varias formas")],
        [t("<strong>Read</strong> bar, line, circle, and scatter graphs, always starting with the title, axes, units, and scale.", "<strong>Leer</strong> gráficas de barras, de líneas, circulares y de dispersión, empezando siempre por el título, los ejes, las unidades y la escala."),
         t("<strong>Tell apart</strong> the independent and dependent variables and say which axis each one goes on.", "<strong>Distinguir</strong> la variable independiente de la dependiente y decir en qué eje va cada una."),
         t("<strong>Describe</strong> a correlation without claiming a cause, and suggest other explanations for a pattern.", "<strong>Describir</strong> una correlación sin afirmar una causa, y proponer otras explicaciones para un patrón."),
         t("<strong>Use</strong> the TI-30XS calculator with confidence: the toggle key and the order of operations.", "<strong>Usar</strong> la calculadora TI-30XS con soltura: la tecla de alternancia y la jerarquía de operaciones.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("2-2", t("Measures of center in population and economic data", "Medidas de tendencia central en datos demográficos y económicos")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- la práctica
def banco_graficas():
    T4 = [t("Bar graph", "Gráfica de barras"), t("Line graph", "Gráfica de líneas"), t("Circle graph", "Gráfica circular"), t("Scatter plot", "Gráfica de dispersión")]
    d1 = [
        (t("Show how the price of a gallon of milk changed every year from 2000 to 2024.", "Mostrar cómo cambió cada año el precio de un galón de leche entre 2000 y 2024."), 1),
        (t("Compare the number of voters in five Chicago wards in one election.", "Comparar el número de votantes de cinco distritos de Chicago en una elección."), 0),
        (t("Show what share of a family’s monthly spending goes to rent, food, transportation, and everything else.", "Mostrar qué parte del gasto mensual de una familia va a alquiler, comida, transporte y todo lo demás."), 2),
        (t("See whether countries with more doctors per person have longer life expectancy.", "Ver si los países con más médicos por habitante tienen mayor esperanza de vida."), 3),
        (t("Follow the population of Illinois in every census from 1900 to 2020.", "Seguir la población de Illinois en cada censo de 1900 a 2020."), 1),
        (t("Compare the average rent in four cities.", "Comparar el alquiler promedio de cuatro ciudades."), 0),
        (t("See whether students who sleep more get higher test scores.", "Ver si los estudiantes que duermen más sacan mejores notas."), 3),
        (t("Show how a state’s electricity comes from coal, gas, nuclear, wind, and solar.", "Mostrar cuánta electricidad de un estado viene del carbón, el gas, la energía nuclear, el viento y el sol."), 2),
    ]
    out = [{"enun": t("Which graph fits best?", "¿Qué gráfica encaja mejor?") + "<br><strong>" + s + "</strong>", "ops": T4, "ok": k, "exp": f"<strong>{T4[k]}.</strong>", "enOrden": True} for s, k in d1]
    tab = "<br>" + " · ".join(f"{a}: {din(v)}" for a, v in SAL)
    d2 = [
        (t("In which year did the minimum wage first reach $1 or more?", "¿En qué año llegó el salario mínimo por primera vez a 1 dólar o más?"), ["1961", "1950", "1968", "1974"], 0, t("$0.75 in 1950, then $1.15 in 1961.", "0.75 en 1950, después 1.15 en 1961.")),
        (t("How many times higher was the wage in 2009 than in 1938?", "¿Cuántas veces mayor era el salario en 2009 que en 1938?"), ["29", "7", "28", "7.25"], 0, t("7.25 ÷ 0.25 = 29.", "7.25 ÷ 0.25 = 29.")),
        (t("What was the increase in dollars from 1980 to 1990?", "¿Cuánto subió en dólares de 1980 a 1990?"), ["$0.70", "$3.80", "$0.07", "$1.70"], 0, t("3.80 − 3.10 = 0.70.", "3.80 − 3.10 = 0.70.")),
        (t("Which claim does the table <strong>not</strong> support?", "¿Qué afirmación <strong>no</strong> sostiene la tabla?"), [t("The wage rose a little every year between laws.", "El salario subió un poco cada año entre leyes."), t("The wage was higher in 2009 than in 1997.", "El salario era más alto en 2009 que en 1997."), t("A law raised the wage in 1974.", "Una ley subió el salario en 1974."), t("The wage never went down in these years.", "El salario nunca bajó en estos años.")], 0, t("The table only shows the years when a law changed it; between laws, it stayed the same.", "La tabla solo muestra los años en que una ley lo cambió; entre leyes se quedaba igual.")),
        (t("What was the percent change from 1997 to 2009? (Use the calculator; round to the nearest whole percent.)", "¿Cuál fue el cambio porcentual de 1997 a 2009? (Use la calculadora; redondee al entero más cercano)."), ["41%", "29%", "2.10%", "71%"], 0, t("(7.25 − 5.15) ÷ 5.15 = 0.4078 ≈ 41%.", "(7.25 − 5.15) ÷ 5.15 = 0.4078 ≈ 41 %.")),
    ]
    out += [{"enun": t("Use the minimum wage table:", "Use la tabla del salario mínimo:") + tab + "<br><strong>" + s + "</strong>", "ops": ops, "ok": k, "exp": e} for s, ops, k, e in d2]
    return out


def banco_variables():
    out = []
    pares = [
        (t("hours of job training", "horas de capacitación laboral"), t("hourly wage", "salario por hora")),
        (t("year", "año"), t("number of people who own a smartphone", "número de personas que tienen teléfono inteligente")),
        (t("price of gasoline", "precio de la gasolina"), t("gallons sold per week", "galones vendidos por semana")),
        (t("rainfall in a season", "lluvia de una temporada"), t("size of the corn harvest", "tamaño de la cosecha de maíz")),
        (t("distance from the city center", "distancia al centro de la ciudad"), t("average rent", "alquiler promedio")),
        (t("amount spent on a campaign", "dinero gastado en una campaña"), t("votes received", "votos recibidos")),
    ]
    for a, b in pares:
        ops = [a, b]
        out.append({"enun": t("A graph relates", "Una gráfica relaciona") + f" <strong>{a}</strong> " + t("and", "y") + f" <strong>{b}</strong>. " + t("Which is the <strong>independent</strong> variable (horizontal axis)?", "¿Cuál es la variable <strong>independiente</strong> (eje horizontal)?"),
                    "ops": ops, "ok": 0, "exp": t(f"“If {a} changes, {b} will change.” The first is independent.", f"«Si cambia {a}, cambiará {b}». La primera es la independiente."), "enOrden": True})
    E = [t("A causes B", "A causa B"), t("B causes A", "B causa A"), t("A third thing causes both", "Una tercera cosa causa las dos"), t("Chance", "Casualidad")]
    casos = [
        (t("Cities with more firefighters have more fires.", "Las ciudades con más bomberos tienen más incendios."), 2, t("Bigger cities have both more fires and more firefighters: size is the third thing. (Also, more fires lead cities to hire more firefighters: B causes A.)", "Las ciudades más grandes tienen más incendios y más bomberos: el tamaño es la tercera cosa. (Además, más incendios llevan a contratar más bomberos: B causa A).")),
        (t("Neighborhoods with more coffee shops have higher rents.", "Los barrios con más cafeterías tienen alquileres más altos."), 2, t("Wealthier neighborhoods attract both coffee shops and higher rents.", "Los barrios más ricos atraen a la vez cafeterías y alquileres altos.")),
        (t("In a class of 8 students, those whose names start with a vowel got better grades this month.", "En una clase de 8 estudiantes, los que tienen un nombre que empieza por vocal sacaron mejores notas este mes."), 3, t("With so few data, and no reasonable link, chance is the best explanation.", "Con tan pocos datos, y sin una relación razonable, la casualidad es la mejor explicación.")),
        (t("Workers who earn more own more expensive cars.", "Los trabajadores que ganan más tienen autos más caros."), 0, t("Higher income lets people buy more expensive cars (A causes B is reasonable here, though the correlation alone would not prove it).", "Un ingreso mayor permite comprar autos más caros (que A cause B es razonable aquí, aunque la correlación sola no lo demostraría).")),
        (t("People who are sick visit doctors more often.", "Las personas enfermas van más al médico."), 1, t("If A is “visits to the doctor” and B is “being sick,” the sickness causes the visits, not the other way around.", "Si A es «ir al médico» y B es «estar enfermo», la enfermedad causa las visitas, no al revés.")),
    ]
    for s, k, e in casos:
        out.append({"enun": t("Correlation:", "Correlación:") + f" <strong>{s}</strong><br>" + t("Which explanation is most reasonable?", "¿Qué explicación es la más razonable?"),
                    "ops": E, "ok": k, "exp": e, "enOrden": True})
    return out


def banco_teclas():
    datos = [
        (t("Percent change from 80 to 60", "Cambio porcentual de 80 a 60"), ["( 60 − 80 ) ÷ 80 =", "60 − 80 ÷ 80 =", "( 60 − 80 ) ÷ 60 =", "80 − 60 ÷ 80 ="], t("New minus old, in parentheses, divided by the old value: −0.25 = −25%.", "Nuevo menos viejo, entre paréntesis, dividido entre el viejo: −0.25 = −25 %.")),
        (t("The average of 12, 15, and 21", "El promedio de 12, 15 y 21"), ["( 12 + 15 + 21 ) ÷ 3 =", "12 + 15 + 21 ÷ 3 =", "12 + 15 + ( 21 ÷ 3 ) =", "( 12 + 15 ) + 21 ÷ 3 ="], t("The sum must be grouped before dividing: 48 ÷ 3 = 16.", "Hay que agrupar la suma antes de dividir: 48 ÷ 3 = 16.")),
        (t("Population density: 90,000 people on 150 square miles plus 50 square miles", "Densidad: 90,000 personas en 150 millas cuadradas más 50 millas cuadradas"), ["90000 ÷ ( 150 + 50 ) =", "90000 ÷ 150 + 50 =", "( 90000 ÷ 150 ) + 50 =", "90000 + 150 ÷ 50 ="], t("The area is the whole sum, so it goes in parentheses: 450 per square mile.", "La superficie es toda la suma, así que va entre paréntesis: 450 por milla cuadrada.")),
        (t("Percent change from 25 to 30", "Cambio porcentual de 25 a 30"), ["( 30 − 25 ) ÷ 25 =", "30 − 25 ÷ 25 =", "( 30 − 25 ) ÷ 30 =", "25 ÷ ( 30 − 25 ) ="], t("(30 − 25) ÷ 25 = 0.2 = 20%.", "(30 − 25) ÷ 25 = 0.2 = 20 %.")),
    ]
    return [{"enun": t("Which keystrokes give", "¿Qué teclas dan") + f" <strong>{s}</strong>?", "ops": ops, "ok": 0,
             "pistas": {1: t("Without parentheses, the calculator divides first.", "Sin paréntesis, la calculadora divide primero."), 2: t("Check what you divide by.", "Revise entre qué se divide."), 3: t("Check the order of operations.", "Revise el orden de las operaciones.")}, "exp": e} for s, ops, e in datos]


JS_EXPR = r"""
function gExpr(){
  var a = aleatorio(2, 20), b = aleatorio(2, 9), c = aleatorio(2, 9), tipo = aleatorio(0, 5), e, r, exp;
  if (tipo === 0){ e = a + " + " + b + " × " + c; r = a + b * c; exp = b + " × " + c + " = " + (b * c) + "; " + a + " + " + (b * c) + " = " + r + "."; }
  else if (tipo === 1){ e = "( " + a + " + " + b + " ) × " + c; r = (a + b) * c; exp = TX2.par + (a + b) + "; " + (a + b) + " × " + c + " = " + r + "."; }
  else if (tipo === 2){ var q = b * c; a = q + aleatorio(5, 40); e = a + " − " + q + " ÷ " + c; r = a - b; exp = q + " ÷ " + c + " = " + b + "; " + a + " − " + b + " = " + r + "."; }
  else if (tipo === 3){ var s2 = aleatorio(2, 9) * c; a = s2 + b; e = "( " + a + " − " + b + " ) ÷ " + c; r = s2 / c; exp = TX2.par + s2 + "; " + s2 + " ÷ " + c + " = " + r + "."; }
  else if (tipo === 4){ e = a + " − " + b + " × " + c; r = a - b * c; exp = b + " × " + c + " = " + (b * c) + "; " + a + " − " + (b * c) + " = " + r + "."; }
  else { e = b + "² + " + c; r = b * b + c; exp = TX2.pot + b + "² = " + (b * b) + "; " + (b * b) + " + " + c + " = " + r + "."; }
  return {enun: "<p>" + TX2.pre + " <code style=\"font-size:1.15em\">" + e + " =</code></p>", resp: leeNumero(String(r)), explica: exp,
    pista: function(v){ return TX2.pista; }};
}
"""


def practica():
    A = {"en": ["graphs", "variables", "calculator", "keys"], "es": ["graficas", "variables", "calculadora", "teclas"]}[C.L]
    tx2 = {"pre": t("What does the calculator show?", "¿Qué muestra la calculadora?"), "par": t("Parentheses first: ", "Primero el paréntesis: "),
           "pot": t("Powers first: ", "Primero la potencia: "), "pista": t("Remember the order: parentheses, powers, × and ÷, then + and −.", "Recuerde el orden: paréntesis, potencias, × y ÷, después + y −.")}
    mods = [
        (A[0], t("Read the graph", "Lea la gráfica"), C.om("m1", t("Choose the right kind of graph for each purpose, then answer questions about the minimum wage table. You may use the calculator.", "Elija la gráfica adecuada para cada propósito y después responda preguntas sobre la tabla del salario mínimo. Puede usar la calculadora."))),
        (A[1], t("Variables and correlation", "Variables y correlación"), C.om("m2", t("Use “if ___ changes, ___ will change.” Then, for each correlation, choose the most reasonable of the four explanations.", "Use «si cambia ___, cambiará ___». Después, en cada correlación, elija la más razonable de las cuatro explicaciones."))),
        (A[2], t("Calculator clinic", "Clínica de la calculadora"), "      <p>" + t("A new expression every time. Work out what the calculator will show, then check it with the calculator.", "Una expresión nueva cada vez. Calcule lo que mostrará la calculadora y después compruébelo con ella.") + "</p>\n" + C.dec_campo("m3", t("Result", "Resultado"))),
        (A[3], t("Which keys?", "¿Qué teclas?"), C.om("m4", t("Choose the keystrokes that answer the question you really mean to ask.", "Elija las teclas que responden a la pregunta que de verdad quiere hacer."))),
    ]
    js = (C.js_datos("GRA", banco_graficas()) + C.js_datos("VAR", banco_variables()) + C.js_datos("TEC", banco_teclas()) + C.js_datos("TX2", tx2) + JS_EXPR +
          'creaBanco("m1", GRA);\ncreaBanco("m2", VAR);\ncreaPracticaDec("m3", gExpr);\ncreaBanco("m4", TEC);\n')
    return C.pagina_practica(N, titulo(), t("Four activities · new exercises every time · two tries in each one · calculator included", "Cuatro actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
