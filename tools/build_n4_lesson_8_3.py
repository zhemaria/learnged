"""Level 4 · Lesson 8.3 · Final project and practice GED math test — builds the lesson and its practice page in English and in Spanish.
Source: clase_mate4/leccion_8-3.html (GEDparaHispanos).
The practice page is the Level 4 review: a mixed practice of the eight topics and an index, with search, of every practice activity of the
level (read from the practice pages already built, so build every other lesson first).
The project template and the final check are built by tools/build_n4_proyecto.py and tools/build_n4_final.py.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import os, re, html as H
import bilingue as B
from bilingue import t, practica, enlace, caja, tabla, calc
import n4
from build_n4_lesson_8_1 import TEMA, SCRIPTS

B.NIVEL = 4
N = "8-3"
TIT = ("Final project and practice GED math test", "Proyecto final integrador y simulacro GED")
TEMAS = [("1", ("Analytic geometry", "Geometría analítica")), ("2", ("3D volume and polynomials", "Volumen 3D y polinomios")), ("3", ("Multiplying and factoring", "Multiplicación y factorización")),
         ("4", ("Quadratic equations", "Ecuaciones cuadráticas")), ("5", ("Rational expressions", "Expresiones racionales")), ("6", ("Systems of linear equations", "Sistemas de ecuaciones lineales")),
         ("7", ("Systems of inequalities and functions", "Sistemas de desigualdades y funciones")), ("8", ("Modeling with functions", "Modelado de funciones"))]
ESTILO = n4.ESTILO + """
  #ix-lista section h3{margin-top:18px;}
  #ix-lista li{margin:6px 0;}
"""

def proyecto(): return t('<a href="project-level-4.html">Final project template: My mathematical model</a>', '<a href="proyecto-nivel-4.html">Plantilla del proyecto final: Mi modelo matemático</a>')
def final(): return t('<a href="final-check-level-4.html">Level 4 final check</a>', '<a href="evaluacion-final-nivel-4.html">Evaluación final del Nivel 4</a>')

def leccion():
    n = N
    partes = [[t("1. Real situation", "1. Situación real"), t("Describe what happens and explain why it is quadratic or exponential.", "Describir el fenómeno y justificar por qué es cuadrático o exponencial.")],
              [t("2. The function", "2. La función"), t("Write the function that models the situation.", "Escribir la función que modela la situación.")],
              [t("3. The graph", "3. La gráfica"), t("Graph it with axes, scale, units, and the name of the function.", "Graficar con ejes, escala, unidades y nombre de la función.")],
              [t("4. Algebraic analysis", "4. Análisis algebraico"), t("Find the vertex or the growth rate, and the value at a specific point.", "Hallar el vértice o la tasa de crecimiento y el valor en un punto específico.")],
              [t("5. Written interpretation", "5. Interpretación escrita"), t("Explain in words what the result means in the real situation.", "Explicar, en palabras, qué significa el resultado en el contexto real.")]]
    s1 = f'''<p>{t("<strong>The close of the level.</strong> This is the last lesson of Level 4. It brings everything together: analytic geometry, polynomials, quadratic equations, rational expressions, systems, and functions. The goal is twofold: present your project and show, on a final check, that you are ready for the GED test.", "<strong>Conexión y cierre.</strong> Esta es la última lección del Nivel 4. Aquí se integra todo: geometría analítica, polinomios, ecuaciones cuadráticas, expresiones racionales, sistemas y funciones. El objetivo es doble: presentar su proyecto y demostrar, en una evaluación final, que está listo para el GED.")}</p>
<p>{t("The project, <strong>“My mathematical model”</strong>, is to model a real situation with a <strong>quadratic or exponential</strong> function. It must include five parts:", "El proyecto, <strong>«Mi modelo matemático»</strong>, consiste en modelar una situación real con una función <strong>cuadrática o exponencial</strong>. Debe incluir cinco partes:")}</p>
{tabla(t("The five parts of the project", "Las cinco partes del proyecto"), t("The five parts of the project “My mathematical model”", "Las cinco partes del proyecto «Mi modelo matemático»"), [t("Part", "Parte"), t("What to include", "Qué incluir")], partes)}
{caja("tip", t("Good situations", "Buenas situaciones"), t(f"<p>The path of a ball (quadratic), savings with compound interest (exponential), the greatest area of a garden with a fixed fence (quadratic), or the growth of followers on social media (exponential). Use the {proyecto()}: you type your function and your work, and it draws the graph, checks your vertex or your values, and saves everything in this browser.</p>", f"<p>La trayectoria de una pelota (cuadrática), el ahorro con interés compuesto (exponencial), el área máxima de un jardín con cerca fija (cuadrática) o el crecimiento de seguidores en una red (exponencial). Use la {proyecto()}: usted escribe su función y su trabajo, y la plantilla dibuja la gráfica, comprueba su vértice o sus valores y guarda todo en este navegador.</p>"))}
{practica("p1", t("Practice 1 — The function", "Práctica 1 — La función"), t("The project models a situation with a function that is…", "El proyecto modela una situación con una función…"), [("a", t("linear only", "solo lineal")), ("b", t("quadratic or exponential", "cuadrática o exponencial")), ("c", t("any shape, with no formula", "de cualquier forma, sin fórmula"))])}
{practica("p2", t("Practice 2 — The analysis", "Práctica 2 — El análisis"), t("For a quadratic model, the algebraic analysis finds…", "En un modelo cuadrático, el análisis algebraico halla…"), [("a", t("the vertex and a value at a point", "el vértice y un valor en un punto")), ("b", t("only the title", "solo el título")), ("c", t("the color of the graph", "el color de la gráfica"))])}
{practica("p3", t("Practice 3 — The graph", "Práctica 3 — La gráfica"), t("The graph of the project must have…", "La gráfica del proyecto debe tener…"), [("a", t("no labels, to keep it clean", "ninguna etiqueta, para que se vea limpia")), ("b", t("only the curve", "solo la curva")), ("c", t("axes, scale, units, and the name of the function", "ejes, escala, unidades y el nombre de la función"))])}'''

    s2 = f'''<p>{t("Present your model in <strong>3 to 4 minutes</strong>: explain the situation, show the graph, and talk about the analysis, to someone you trust (a relative, a friend, or a study partner) or recording yourself on your phone. Ask them to ask you questions, or, if you record yourself, ask them yourself as you watch the video. What counts is the clear and precise use of <strong>mathematical vocabulary</strong> (vertex, growth rate, intercept, domain, and so on).", "Presente su modelo en <strong>3 a 4 minutos</strong>: explique la situación, muestre la gráfica y comente el análisis, ante alguien de confianza (un familiar, un amigo o un compañero de estudio) o grabándose con el teléfono. Pida que le hagan preguntas o, si se graba, hágaselas usted al ver el video. Se valora el uso claro y preciso del <strong>vocabulario matemático</strong> (vértice, tasa de crecimiento, intercepto, dominio, etc.).")}</p>
{caja("tip", t("A tip for the presentation", "Consejo para la presentación"), t("<p>Practice out loud once before. Start with the real situation (to catch interest), then show the function and the graph, and end with the interpretation: “this means that…”.</p>", "<p>Practique en voz alta una vez antes. Empiece por la situación real (para enganchar), luego muestre la función y la gráfica, y termine con la interpretación: «esto significa que…».</p>"))}'''

    estr = [[t("Manage your time", "Manejo del tiempo"), t("Do not spend too long on one question; flag it and come back at the end.", "No se detenga demasiado en una pregunta; márquela y vuelva al final.")],
            [t("Rule out choices", "Descarte de opciones"), t("Cross out the impossible answers before you calculate.", "Elimine las respuestas imposibles antes de calcular.")],
            [t("The formula sheet", "Hoja de fórmulas"), t("Use it with confidence; you already know where each formula is.", "Úsela con confianza; ya sabe dónde está cada fórmula.")],
            [t("The TI-30XS calculator", "Calculadora TI-30XS"), t("Clear it before each calculation; check what you type.", "Límpiela antes de cada cálculo; verifique lo que escribe.")],
            [t("Read what is asked", "Leer lo que se pregunta"), t("Underline the question and the units. Many wrong answers are right answers to a different question.", "Subraye la pregunta y las unidades. Muchas respuestas incorrectas son respuestas correctas a otra pregunta.")]]
    s3 = f'''<p>{t("The final check works like the real test. These strategies help you do your best:", "La evaluación final reproduce las condiciones del examen real. Estas estrategias ayudan a rendir mejor:")}</p>
{tabla(t("Strategies for the GED math test", "Estrategias para el examen GED"), t("Strategies for the GED Mathematical Reasoning test", "Estrategias para el examen GED Mathematical Reasoning"), [t("Strategy", "Estrategia"), t("How to use it", "Cómo aplicarla")], estr)}
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. The calculator on this page does the same operations, although some keys have other names or are in other places. If you have a TI-30XS, practice with it too so you learn where its keys are.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. La calculadora de esta página hace las mismas operaciones, aunque algunas teclas tienen otro nombre o están en otro lugar. Si tiene una TI-30XS, practique también con ella para conocer la ubicación de sus teclas.</p>"))}
{caja("ojo", t("Real test conditions", "Condiciones reales"), t(f"<p>Take the {final()} in one sitting: time yourself, do not look at the lessons, and use only the calculator and the formula sheet. Breathe, read calmly, and trust what you learned.</p>", f"<p>Haga la {final()} de una sentada: tome el tiempo, no consulte las lecciones y use solo la calculadora y la hoja de fórmulas. Respire, lea con calma y confíe en lo aprendido.</p>"))}'''

    mapa = [[t("1. Analytic geometry", "1. Geometría analítica"), t("Distance, midpoint, slope, and the equations of a line.", "Distancia, punto medio, pendiente y ecuaciones de la recta.")],
            [t("2. Volume and polynomials", "2. Volumen y polinomios"), t("Spheres, cones, pyramids, surface area; adding and multiplying polynomials.", "Esferas, conos, pirámides, área de superficie; suma y producto de polinomios.")],
            [t("3. Factoring", "3. Factorización"), t("FOIL, special products, common factor, trinomials.", "FOIL, identidades notables, factor común, trinomios.")],
            [t("4. Quadratic equations", "4. Ecuaciones cuadráticas"), t("Factoring, completing the square, the quadratic formula.", "Factorización, completar el cuadrado, fórmula cuadrática.")],
            [t("5. Rational expressions", "5. Expresiones racionales"), t("Simplifying, operating, and solving rational equations.", "Simplificar, operar y resolver ecuaciones racionales.")],
            [t("6. Systems of equations", "6. Sistemas de ecuaciones"), t("Substitution, elimination, graphing, and modeling.", "Sustitución, eliminación, método gráfico y modelado.")],
            [t("7. Inequalities and functions", "7. Desigualdades y funciones"), t("Feasible regions, f(x), domain and range, rate of change.", "Regiones factibles, f(x), dominio y rango, tasa de cambio.")],
            [t("8. Modeling", "8. Modelado"), t("Quadratic and exponential functions, compound interest.", "Funciones cuadráticas y exponenciales, interés compuesto.")]]
    s4 = f'''<p>{t("Level 4 covered eight topics. This is the full map of what you learned, which the final check will test.", "El Nivel 4 recorrió ocho temas. Este es el mapa completo de lo aprendido, que la evaluación final pondrá a prueba.")}</p>
{tabla(t("The eight topics of Level 4", "Los ocho temas del Nivel 4"), t("Map of the eight topics of Level 4", "Mapa de los ocho temas del Nivel 4"), [t("Topic", "Tema"), t("Main content", "Contenido principal")], mapa)}
{practica("p4", t("Practice 4 — Slope", "Práctica 4 — Pendiente"), t("The slope between (1, 2) and (3, 8) is:", "La pendiente entre (1, 2) y (3, 8) es:"), [("a", "2"), ("b", "3"), ("c", "1/3")])}
{practica("p5", t("Practice 5 — Factoring", "Práctica 5 — Factorizar"), t("Factor x² − 5x + 6.", "Factorice x² − 5x + 6."), [("a", "(x + 2)(x + 3)"), ("b", "(x − 1)(x − 6)"), ("c", "(x − 2)(x − 3)")])}
{practica("p6", t("Practice 6 — The vertex", "Práctica 6 — El vértice"), t("The vertex of f(x) = x² − 4x + 3 is:", "El vértice de f(x) = x² − 4x + 3 es:"), [("a", "(2, −1)"), ("b", "(−2, −1)"), ("c", "(4, 3)")])}
{enlace(n, t("mixed", "mezcla"), t("mixed review of the eight topics", "repaso mezclado de los ocho temas"), t("One question at a time from any topic, with a hint and a second try.", "Una pregunta a la vez de cualquier tema, con pista y segunda oportunidad."))}
{enlace(n, t("index", "indice"), t("every practice of Level 4", "todas las prácticas del Nivel 4"), t("Search by word and go straight to the practice you need.", "Busque por palabra y vaya directo a la práctica que necesita."))}
{caja("tip", t("The final check", "La evaluación final"), t(f"<p>When you are ready, take the {final()}: 30 questions from the eight topics, answered all at once, with a report by topic that tells you what to review. You pass with 21 right answers (70%).</p>", f"<p>Cuando esté listo, haga la {final()}: 30 preguntas de los ocho temas, respondidas de una sola vez, con un informe por tema que le dice qué repasar. Se aprueba con 21 aciertos (70 %).</p>"))}'''

    secciones = [("s-" + t("project", "proyecto"), t("The final project “My mathematical model”", "El proyecto final «Mi modelo matemático»"), s1),
                 ("s-" + t("presentation", "presentacion"), t("The oral presentation", "La presentación oral"), s2),
                 ("s-" + t("strategies", "estrategias"), t("Strategies for the GED test", "Estrategias para el examen GED"), s3),
                 ("s-" + t("review", "repaso"), t("Review of the eight topics", "Repaso integrador de los ocho temas"), s4)]

    lesson = {"next": t("the GED test", "el examen GED"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Level 4 ends with the two great models of the GED test.", "El Nivel 4 termina con los dos grandes modelos del GED."), "c": t("The model is a formula you can analyze.", "El modelo es una fórmula que se puede analizar.")}, "right": t("A quadratic or exponential function.", "Una función cuadrática o exponencial."), "solution": t("Quadratic or exponential.", "Cuadrática o exponencial.")},
      "p2": {"ok": "a", "hints": {"b": t("The title is not an analysis.", "El título no es un análisis."), "c": t("The color is not an analysis.", "El color no es un análisis.")}, "right": t("The vertex and a value at a point.", "El vértice y un valor en un punto."), "solution": t("The vertex and a value at a point.", "El vértice y un valor en un punto.")},
      "p3": {"ok": "c", "hints": {"a": t("Without labels, nobody can read the graph.", "Sin etiquetas, nadie puede leer la gráfica."), "b": t("The curve alone does not say what it measures.", "La curva sola no dice qué mide.")}, "right": t("A complete graph can be read on its own.", "Una gráfica completa se lee por sí sola."), "solution": t("Axes, scale, units, and the name.", "Ejes, escala, unidades y nombre.")},
      "p4": {"ok": "b", "hints": {"a": t("Change in y: 8 − 2 = 6; change in x: 3 − 1 = 2.", "Cambio en y: 8 − 2 = 6; cambio en x: 3 − 1 = 2."), "c": t("The fraction is upside down: y on top.", "La fracción está al revés: la y va arriba.")}, "right": "6 / 2 = 3.", "solution": "3."},
      "p5": {"ok": "c", "hints": {"a": t("That gives + 5x; you need − 5x.", "Eso da + 5x; se necesita − 5x."), "b": t("(−1)(−6) = 6, but −1 − 6 = −7, not −5.", "(−1)(−6) = 6, pero −1 − 6 = −7, no −5.")}, "right": t("−2 and −3: product 6, sum −5.", "−2 y −3: producto 6, suma −5."), "solution": "(x − 2)(x − 3)."},
      "p6": {"ok": "a", "hints": {"b": t("x = −(−4)/2 = 2, positive.", "x = −(−4)/2 = 2, positivo."), "c": t("Use x = −b/(2a), not b and c.", "Use x = −b/(2a), no b y c.")}, "right": "x = 2; f(2) = −1.", "solution": "(2, −1)."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Count: situation, function, graph, analysis, interpretation.", "Cuente: situación, función, gráfica, análisis, interpretación."), "c": t("Count: situation, function, graph, analysis, interpretation.", "Cuente: situación, función, gráfica, análisis, interpretación."), "d": t("One part is not enough.", "Una parte no basta.")}, "solution": t("Five parts.", "Cinco partes.")},
      "B": {"ok": "d", "hints": {"a": t("The graph shows; the interpretation explains.", "La gráfica muestra; la interpretación explica."), "b": t("The title says nothing about the result.", "El título no dice nada del resultado."), "c": t("The calculations are needed, but the meaning is the key.", "Los cálculos son necesarios, pero lo clave es el significado.")}, "solution": t("Explaining what the result means.", "Explicar qué significa el resultado.")},
      "C": {"ok": "c", "hints": {"a": t("That can use up the time for the others.", "Eso puede agotar el tiempo de las demás."), "b": t("A blank answer is always wrong.", "Una respuesta en blanco siempre es incorrecta."), "d": t("Guessing first wastes the chance to come back.", "Adivinar primero desperdicia la oportunidad de volver.")}, "solution": t("Flag it and come back.", "Marcarla y volver.")},
      "D": {"ok": "a", "hints": {"b": t("The GED test gives you a formula sheet.", "El examen GED entrega una hoja de fórmulas."), "c": t("The formulas are given: learn where they are.", "Las fórmulas se dan: hay que saber dónde están."), "d": t("You can use it on the whole test.", "Se puede usar en todo el examen.")}, "solution": t("Know where each formula is.", "Saber dónde está cada fórmula.")},
      "E": {"ok": "d", "hints": {"a": t("√(3² + 4²): do not add the sides.", "√(3² + 4²): no se suman los lados."), "b": t("25 is d²; take the square root.", "25 es d²; falta la raíz."), "c": t("√(9 + 16) = √25.", "√(9 + 16) = √25.")}, "solution": "√25 = 5."},
      "F": {"ok": "b", "hints": {"a": t("The middle term 8x is missing.", "Falta el término del medio, 8x."), "c": t("The middle term is 2 · 4 · x = 8x.", "El término del medio es 2 · 4 · x = 8x."), "d": t("4² = 16, not 8.", "4² = 16, no 8.")}, "solution": "x² + 8x + 16."},
      "G": {"ok": "c", "hints": {"a": t("Check: 3 + 6 = 9 but 3 ≠ 2(6).", "Compruebe: 3 + 6 = 9, pero 3 ≠ 2(6)."), "b": t("x + y = 6, not 9.", "x + y = 6, no 9."), "d": t("0 ≠ 2(9).", "0 ≠ 2(9).")}, "solution": "(3, 6)."},
      "H": {"ok": "a", "hints": {"b": t("3 is the base: it multiplies each time.", "3 es la base: multiplica cada vez."), "c": t("x is in the exponent, not squared.", "La x está en el exponente, no al cuadrado."), "d": t("x is not in a denominator.", "La x no está en un denominador.")}, "solution": t("Exponential.", "Exponencial.")},
     }}

    quiz = [
     ("A", t("How many parts must the final project have?", "¿Cuántas partes debe tener el proyecto final?"), [("a", "3"), ("b", "5"), ("c", "4"), ("d", "1")]),
     ("B", t("The written interpretation of the project means…", "La interpretación escrita del proyecto consiste en…"), [("a", t("copying the graph", "copiar la gráfica")), ("b", t("writing the title", "escribir el título")), ("c", t("listing the calculations", "enumerar los cálculos")), ("d", t("explaining what the result means in the real situation", "explicar qué significa el resultado en la situación real"))]),
     ("C", t("A question is taking you too long. The best thing to do is…", "Una pregunta le está tomando demasiado tiempo. Lo mejor es…"), [("a", t("stay on it until you finish", "quedarse en ella hasta terminar")), ("b", t("leave it blank and forget it", "dejarla en blanco y olvidarla")), ("c", t("flag it and come back at the end", "marcarla y volver al final")), ("d", t("guess right away and never come back", "adivinar enseguida y no volver"))]),
     ("D", t("On the GED test, the best use of the formula sheet is…", "En el examen GED, lo mejor con la hoja de fórmulas es…"), [("a", t("knowing where each formula is and how to use it", "saber dónde está cada fórmula y cómo usarla")), ("b", t("memorizing it, because it is not given", "memorizarla, porque no se entrega")), ("c", t("ignoring it", "ignorarla")), ("d", t("using it only on the first question", "usarla solo en la primera pregunta"))]),
     ("E", t("The distance between (0, 0) and (3, 4) is:", "La distancia entre (0, 0) y (3, 4) es:"), [("a", "7"), ("b", "25"), ("c", "12"), ("d", "5")]),
     ("F", "(x + 4)² =", [("a", "x² + 16"), ("b", "x² + 8x + 16"), ("c", "x² + 4x + 16"), ("d", "x² + 8x + 8")]),
     ("G", t("Solve the system y = 2x and x + y = 9.", "Resuelva el sistema y = 2x ; x + y = 9."), [("a", "(6, 3)"), ("b", "(3, 3)"), ("c", "(3, 6)"), ("d", "(9, 0)")]),
     ("H", t("f(x) = 3ˣ is a function that is:", "f(x) = 3ˣ es una función:"), [("a", t("exponential", "exponencial")), ("b", t("linear", "lineal")), ("c", t("quadratic", "cuadrática")), ("d", t("rational", "racional"))])]
    lesson["quiz"]["G"]["hints"] = {"a": t("Check y = 2x: is 3 = 2 · 6?", "Compruebe y = 2x: ¿3 = 2 · 6?"), "b": t("3 + 3 = 6, not 9.", "3 + 3 = 6, no 9."), "d": t("Check y = 2x: is 0 = 2 · 9?", "Compruebe y = 2x: ¿0 = 2 · 9?")}

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Bring Level 4 together in your own mathematical model, present it, learn strategies for the GED math test, and take the final check.", "Reúna el Nivel 4 en su propio modelo matemático, preséntelo, aprenda estrategias para el examen GED y haga la evaluación final."),
        ("🎓", t("The close of Level 4", "El cierre del Nivel 4")),
        [t("<strong>Model</strong> a real situation with a quadratic or exponential function.", "<strong>Modelar</strong> una situación real con una función cuadrática o exponencial."),
         t("<strong>Present</strong> the project “My mathematical model” with clear mathematical vocabulary.", "<strong>Presentar</strong> el proyecto «Mi modelo matemático» con vocabulario matemático preciso."),
         t("<strong>Use</strong> test strategies, the formula sheet, and the calculator for the GED Mathematical Reasoning test.", "<strong>Aplicar</strong> estrategias de examen, la hoja de fórmulas y la calculadora para el GED Mathematical Reasoning."),
         t("<strong>Answer</strong> GED-style questions that combine the eight topics of the level.", "<strong>Responder</strong> preguntas tipo GED que integran los ocho temas del nivel.")],
        secciones,
        (t(f"This is the last homework of Level 4. Do it in this order, over several days: (1) Complete the project “My mathematical model” in the {proyecto()}, with its five parts (situation, function, graph, analysis, and interpretation), grade it with the rubric, and fix what does not reach “Proficient.” Save it as a PDF. (2) Present your model in 3 to 4 minutes to someone you trust, or record yourself on your phone, and check that you used the mathematical vocabulary precisely. (3) Take the {final()} in real conditions: in one sitting, timing yourself, and only with the calculator and the formula sheet. (4) My final study plan: with the report of the final check, write which topics to review, with which practices (the index on the practice page of this lesson gathers them all), and in what order. End with a concrete goal for the week before your test. About 3 hours, spread over several days; the final check needs a block with no interruptions.",
           f"Esta es la última tarea del Nivel 4. Hágala en este orden, repartida en varios días: (1) Complete el proyecto «Mi modelo matemático» en la {proyecto()}, con sus cinco partes (situación, función, gráfica, análisis e interpretación), califíquese con la rúbrica y corrija lo que no llegue a «Competente». Guárdelo en PDF. (2) Presente su modelo en 3 a 4 minutos a alguien de confianza, o grábese con el teléfono, y compruebe que usó el vocabulario matemático con precisión. (3) Haga la {final()} en condiciones reales: de una sentada, tomando el tiempo y solo con la calculadora y la hoja de fórmulas. (4) Mi plan de preparación final: con el informe de la evaluación, anote qué temas debe repasar, con qué prácticas (el índice de la página de práctica de esta lección las reúne todas) y en qué orden. Termine con una meta concreta para la semana anterior al examen. Unas 3 horas, repartidas en varios días; la evaluación final requiere un bloque sin interrupciones."),
         t("Choose the situation for your model from your own life: the savings you want to build, the price of something you plan to buy, a ball you throw with your children, or the garden you would like to fence.",
           "Elija la situación de su modelo de su propia vida: el ahorro que quiere reunir, el precio de algo que piensa comprar, una pelota que lanza con sus hijos o el jardín que le gustaría cercar.")),
        quiz,
        t("Rubric for the final project", "Rúbrica del proyecto final"),
        t("Rubric for the final project “My mathematical model”", "Rúbrica del proyecto final «Mi modelo matemático»"),
        [(t("Real situation and reasons", "Situación real y justificación"), t("I describe a real situation and explain why it is quadratic or exponential.", "Describo una situación real y justifico por qué es cuadrática o exponencial."), t("I describe it, but I do not explain the kind of function.", "La describo, pero no justifico el tipo de función."), t("There is no situation, or it cannot be modeled.", "No hay situación o no se puede modelar.")),
         (t("Graph with labels", "Gráfica con etiquetas"), t("A correct graph with axes, scale, units, and the name of the function.", "Gráfica correcta con ejes, escala, unidades y nombre de la función."), t("A graph with missing labels.", "Gráfica a la que le faltan etiquetas."), t("No graph, or a wrong one.", "Sin gráfica o incorrecta.")),
         (t("Algebraic analysis", "Análisis algebraico"), t("I find the vertex or the rate and a value at a point, with no mistakes.", "Hallo el vértice o la tasa y un valor en un punto, sin errores."), t("A partial analysis, or with mistakes.", "Análisis parcial o con errores."), t("No analysis.", "Sin análisis.")),
         (t("Interpretation and presentation", "Interpretación y presentación"), t("I explain the result in context and present it with precise vocabulary.", "Explico el resultado en contexto y lo presento con vocabulario preciso."), t("I explain it partly, or with vague words.", "Lo explico en parte o con palabras vagas."), t("I do not explain the result.", "No interpreto el resultado."))],
        t("<p>You did it! This lesson closes Topic 8 and, with it, all of Level 4. You went through analytic geometry, 3D volume, polynomials and factoring, quadratic equations, rational expressions, systems of equations and inequalities, and modeling with quadratic and exponential functions.</p>\n<p>Finishing this level means you are <strong>ready for the GED® Mathematical Reasoning test</strong>. You arrive prepared: with the formula sheet, the TI-30XS calculator, and, above all, your own mathematical reasoning. Good luck on your test!</p>",
          "<p>¡Lo logró! Con esta lección se cierra el Tema 8 y, con él, el Nivel 4 completo. Ha recorrido geometría analítica, volumen 3D, polinomios y factorización, ecuaciones cuadráticas, expresiones racionales, sistemas de ecuaciones y desigualdades, y el modelado con funciones cuadráticas y exponenciales.</p>\n<p>Completar este nivel significa que está <strong>listo para el GED® Mathematical Reasoning</strong>. Llega preparado: con la hoja de fórmulas, la calculadora TI-30XS y, sobre todo, con su propio razonamiento matemático. ¡Mucho éxito en su examen!</p>"),
        (None, ("", t("The GED Mathematical Reasoning test", "El examen GED Mathematical Reasoning"))),
        [(t("model", "modelo"), t("A function that describes a real situation.", "Una función que describe una situación real.")),
         (t("interpretation", "interpretación"), t("A written explanation of what a result means in context.", "Una explicación escrita de lo que significa un resultado en su contexto.")),
         (t("formula sheet", "hoja de fórmulas"), t("The page of formulas the GED test gives you during the math test.", "La página de fórmulas que el examen GED entrega durante la prueba de matemáticas.")),
         (t("rule out", "descartar"), t("To cross out impossible answers before calculating.", "Eliminar las respuestas imposibles antes de calcular."))],
        lesson)

# ---------------- practice page: the Level 4 review ----------------
def indice_practicas():
    """Reads every Level 4 practice page in the current language and lists its modules: (topic, lesson, lesson title, href, module title, text)."""
    base = os.path.join(B.ROOT, "math/level-4" if B.L == "en" else "es/matematicas/nivel-4")
    pref = "practice-" if B.L == "en" else "practica-"
    filas = []
    for tema, _ in TEMAS:
        for k in (1, 2, 3):
            n = f"{tema}-{k}"
            ruta = os.path.join(base, f"{pref}{n}.html")
            if n == N or not os.path.exists(ruta):
                continue
            s = open(ruta, encoding="utf-8").read()
            m = re.search(r"<h1>(.*?)</h1>", s, re.S)
            tit = H.unescape(re.sub(r"<[^>]+>", "", m.group(1))).split(" · ", 1)[-1] if m else n
            for mid, mt, cuerpo in re.findall(r'<details class="modulo" id="([^"]+)"[^>]*>\s*<summary>.*?<h2>(.*?)</h2>(.*?)</details>', s, re.S):
                texto = H.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", cuerpo, flags=re.S))))[:700]
                filas.append((tema, n, tit, f"{pref}{n}.html#{mid}", H.unescape(re.sub(r"<[^>]+>", "", mt)), texto))
    return filas

LOGICA = r'''
/* MODULE 1 · Mixed review: one question at a time from any topic of Level 4 */
function uniq(l){ return l.filter(function(o, i){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }); }
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function ptxt(x, y){ return "(" + sg(x) + ", " + sg(y) + ")"; }
function bin(r){ return "(x " + (r < 0 ? "+ " + -r : "− " + r) + ")"; }
var MEZCLA = [
 function(){ var t = aleatorio(0, 2), x1 = aleatorio(-5, 5), y1 = aleatorio(-5, 5), tr = elige([[3, 4, 5], [6, 8, 10], [5, 12, 13]]), sx = elige([1, -1]), sy = elige([1, -1]);
   if (t === 0){ var x2 = x1 + sx * tr[0], y2 = y1 + sy * tr[1];
     return {tema: 1, enun: T("What is the distance between ", "¿Cuál es la distancia entre ") + ptxt(x1, y1) + T(" and ", " y ") + ptxt(x2, y2) + "?", correcta: "ok", opciones: uniq([{clave: "ok", html: String(tr[2])}, {clave: "s", html: String(tr[0] + tr[1])}, {clave: "c", html: String(tr[2] * tr[2])}, {clave: "m", html: String(tr[2] + 1)}]),
       pista: "d = √((x₂ − x₁)² + (y₂ − y₁)²).", porClave: {s: T("Do not add the differences: square them, add, and take the root.", "No sume las diferencias: elévelas al cuadrado, súmelas y saque la raíz.")}, bien: "√(" + tr[0] + "² + " + tr[1] + "²) = √" + tr[2] * tr[2] + " = " + tr[2] + "."}; }
   var x3 = x1 + 2 * aleatorio(-3, 3), y3 = y1 + 2 * aleatorio(-3, 3);
   if (t === 1) return {tema: 1, enun: T("What is the midpoint of ", "¿Cuál es el punto medio de ") + ptxt(x1, y1) + T(" and ", " y ") + ptxt(x3, y3) + "?", correcta: "ok", opciones: uniq([{clave: "ok", html: ptxt((x1 + x3) / 2, (y1 + y3) / 2)}, {clave: "s", html: ptxt(x1 + x3, y1 + y3)}, {clave: "d", html: ptxt((x3 - x1) / 2, (y3 - y1) / 2)}, {clave: "w", html: ptxt((y1 + y3) / 2, (x1 + x3) / 2)}, {clave: "u", html: ptxt((x1 + x3) / 2 + 1, (y1 + y3) / 2)}, {clave: "v", html: ptxt((x1 + x3) / 2, (y1 + y3) / 2 - 1)}]).slice(0, 4),
     pista: T("Average the x's and average the y's.", "Promedie las x y promedie las y."), bien: "((" + sg(x1) + " + " + (x3 < 0 ? "(" + sg(x3) + ")" : x3) + ") / 2, (" + sg(y1) + " + " + (y3 < 0 ? "(" + sg(y3) + ")" : y3) + ") / 2) = " + ptxt((x1 + x3) / 2, (y1 + y3) / 2) + "."};
   var dx = nz(1, 4), m = nz(-3, 4), y4 = y1 + m * dx;
   return {tema: 1, enun: T("What is the slope between ", "¿Cuál es la pendiente entre ") + ptxt(x1, y1) + T(" and ", " y ") + ptxt(x1 + dx, y4) + "?", correcta: "ok", opciones: uniq([{clave: "ok", html: sg(m)}, {clave: "i", html: (m < 0 ? "−" : "") + "1/" + Math.abs(m)}, {clave: "s", html: sg(-m)}, {clave: "d", html: sg(m * dx)}]),
     pista: "m = (y₂ − y₁) / (x₂ − x₁).", bien: "(" + sg(y4) + " − " + (y1 < 0 ? "(" + sg(y1) + ")" : y1) + ") / " + dx + " = " + sg(m * dx) + " / " + dx + " = " + sg(m) + "."}; },
 function(){ var t = aleatorio(0, 1), r = aleatorio(2, 6);
   if (t === 0){ var h = 3 * aleatorio(1, 4);
     return {tema: 2, enun: T("A cone has radius " + r + " in and height " + h + " in. Its volume (V = ⅓πr²h) is:", "Un cono tiene radio " + r + " pulg y altura " + h + " pulg. Su volumen (V = ⅓πr²h) es:"), correcta: "ok",
       opciones: uniq([{clave: "ok", html: r * r * h / 3 + T("π cubic inches", "π pulgadas cúbicas")}, {clave: "c", html: r * r * h + T("π cubic inches", "π pulgadas cúbicas")}, {clave: "s", html: r * h / 3 + T("π cubic inches", "π pulgadas cúbicas")}, {clave: "d", html: 2 * r * h / 3 + T("π cubic inches", "π pulgadas cúbicas")}]),
       pista: T("Square the radius, multiply by the height, and divide by 3.", "Eleve el radio al cuadrado, multiplique por la altura y divida entre 3."), porClave: {c: T("That is the cylinder; a cone is one third of it.", "Ese es el cilindro; el cono es un tercio.")}, bien: "⅓ · " + r + "² · " + h + " = " + r * r * h / 3 + "π."}; }
   var a = nz(-5, 5), b = nz(-6, 6), c = nz(-5, 5), d = nz(-6, 6);
   return {tema: 2, enun: T("Add: ", "Sume: ") + "(" + pVis([b, a]) + ") + (" + pVis([d, c]) + ")", correcta: "ok", opciones: uniq([{clave: "ok", html: pVis([b + d, a + c])}, {clave: "m", html: pVis([b * d, 0, a * c])}, {clave: "s", html: pVis([b - d, a - c])}, {clave: "x", html: pVis([0, a + c + b + d])}]),
     pista: T("Add the x terms together and the numbers together.", "Sume los términos en x entre sí y los números entre sí."), bien: "(" + sg(a) + " + " + (c < 0 ? "(" + sg(c) + ")" : c) + ")x + (" + sg(b) + " + " + (d < 0 ? "(" + sg(d) + ")" : d) + ") = " + pVis([b + d, a + c]) + "."}; },
 function(){ var r1 = nz(-7, 7), r2; do { r2 = nz(-7, 7); } while (r2 === r1 || r2 === -r1); var p = pMul([-r1, 1], [-r2, 1]);
   return {tema: 3, enun: T("Factor: ", "Factorice: ") + pVis(p), correcta: "ok", opciones: uniq([{clave: "ok", html: bin(r1) + bin(r2)}, {clave: "s", html: bin(-r1) + bin(-r2)}, {clave: "m", html: bin(r1) + bin(-r2)}, {clave: "n", html: bin(-r1) + bin(r2)}]),
     pista: T("Find two numbers whose product is " + sg(p[0]) + " and whose sum is " + sg(p[1]) + ".", "Busque dos números cuyo producto sea " + sg(p[0]) + " y cuya suma sea " + sg(p[1]) + "."), bien: T("The numbers ", "Los números ") + sg(-r1) + T(" and ", " y ") + sg(-r2) + ": " + bin(r1) + bin(r2) + "."}; },
 function(){ var r1 = aleatorio(-7, 7), r2; do { r2 = aleatorio(-7, 7); } while (r2 === r1); var p = pMul([-r1, 1], [-r2, 1]), lo = Math.min(r1, r2), hi = Math.max(r1, r2), y = function(u, v){ return "x = " + sg(u) + T(" and ", " y ") + "x = " + sg(v); };
   return {tema: 4, enun: T("Solve: ", "Resuelva: ") + pVis(p) + " = 0", correcta: "ok", opciones: uniq([{clave: "ok", html: y(lo, hi)}, {clave: "s", html: y(-hi, -lo)}, {clave: "m", html: y(lo, -hi)}, {clave: "c", html: "x = " + sg(p[0])}]),
     pista: T("Factor and set each factor equal to 0.", "Factorice e iguale cada factor a 0."), bien: bin(r1).replace("(x − 0)", "x") + bin(r2).replace("(x − 0)", "x") + " = 0 → " + y(lo, hi) + "."}; },
 function(){ var t = aleatorio(0, 1), a = aleatorio(2, 9);
   if (t === 0) return {tema: 5, enun: T("Simplify ", "Simplifique ") + "(x² − " + a * a + ") / (x − " + a + ")" + T(", with x ≠ ", ", con x ≠ ") + a + ".", correcta: "ok", opciones: uniq([{clave: "ok", html: "x + " + a}, {clave: "m", html: "x − " + a}, {clave: "s", html: "x + " + a * a}, {clave: "u", html: String(a)}]),
     pista: T("Factor the top as a difference of squares.", "Factorice el numerador como diferencia de cuadrados."), bien: "(x + " + a + ")(x − " + a + ") / (x − " + a + ") = x + " + a + "."};
   var b = nz(-9, 9);
   return {tema: 5, enun: T("For which value is ", "¿Para qué valor NO está definida ") + "5 / (x " + (b < 0 ? "+ " + -b : "− " + b) + ")" + T(" NOT defined?", "?"), correcta: "ok", opciones: uniq([{clave: "ok", html: "x = " + sg(b)}, {clave: "s", html: "x = " + sg(-b)}, {clave: "z", html: "x = 0"}, {clave: "c", html: "x = 5"}]),
     pista: T("A fraction is not defined when its denominator is 0.", "Una fracción no está definida cuando su denominador vale 0."), bien: "x " + (b < 0 ? "+ " + -b : "− " + b) + " = 0 → x = " + sg(b) + "."}; },
 function(){ var x = aleatorio(-5, 9), y; do { y = aleatorio(-5, 9); } while (y === x || y === -x || y === 0); var s = x + y, d = x - y;
   return {tema: 6, enun: T("Solve the system: x + y = ", "Resuelva el sistema: x + y = ") + sg(s) + " ; x − y = " + sg(d) + ".", correcta: "ok", opciones: uniq([{clave: "ok", html: ptxt(x, y)}, {clave: "w", html: ptxt(y, x)}, {clave: "s", html: ptxt(s, d)}, {clave: "m", html: ptxt(x, -y)}]),
     pista: T("Add the two equations: the y's cancel.", "Sume las dos ecuaciones: las y se cancelan."), bien: "2x = " + sg(s + d) + ", x = " + sg(x) + "; y = " + sg(s) + " − " + (x < 0 ? "(" + sg(x) + ")" : x) + " = " + sg(y) + "."}; },
 function(){ var t = aleatorio(0, 1);
   if (t === 0){ var p = [aleatorio(-5, 5), nz(-4, 4), nz(-2, 2)], a = aleatorio(-3, 3), v = pEval(p, a), err = p[0] + p[1] * a - p[2] * a * a;
     return {tema: 7, enun: T("If f(x) = ", "Si f(x) = ") + pVis(p) + T(", what is f(", ", ¿cuánto vale f(") + sg(a) + ")?", correcta: "ok", opciones: uniq([{clave: "ok", html: sg(v)}, {clave: "e", html: sg(err)}, {clave: "m", html: sg(v + 2)}, {clave: "n", html: sg(-v)}, {clave: "u", html: sg(v - 1)}]).slice(0, 4),
       pista: T("Put the input in parentheses and use PEMDAS: powers first.", "Escriba la entrada entre paréntesis y use PEMDAS: primero las potencias."), bien: "f(" + sg(a) + ") = " + sustP(p, a) + " = " + sg(v) + "."}; }
   var a2 = aleatorio(0, 3), b2 = a2 + aleatorio(1, 4), m = nz(-6, 6), fa = aleatorio(-10, 10), fb = fa + m * (b2 - a2);
   return {tema: 7, enun: T("f(" + a2 + ") = " + sg(fa) + " and f(" + b2 + ") = " + sg(fb) + ". What is the average rate of change?", "f(" + a2 + ") = " + sg(fa) + " y f(" + b2 + ") = " + sg(fb) + ". ¿Cuál es la tasa de cambio promedio?"), correcta: "ok", opciones: uniq([{clave: "ok", html: sg(m)}, {clave: "t", html: sg(fb - fa)}, {clave: "s", html: sg(-m)}, {clave: "x", html: sg(b2 - a2)}, {clave: "u", html: sg(m + 1)}, {clave: "v", html: sg(m - 1)}]).slice(0, 4),
     pista: "(f(b) − f(a)) / (b − a).", bien: "(" + sg(fb) + " − " + (fa < 0 ? "(" + sg(fa) + ")" : fa) + ") / (" + b2 + " − " + a2 + ") = " + sg(fb - fa) + " / " + (b2 - a2) + " = " + sg(m) + "."}; },
 function(){ var t = aleatorio(0, 1);
   if (t === 0){ var a = elige([1, -1, 2]), h = aleatorio(-4, 4), k = aleatorio(-6, 6), b = -2 * a * h, c = a * h * h + k;
     return {tema: 8, enun: T("What is the vertex of f(x) = ", "¿Cuál es el vértice de f(x) = ") + pVis([c, b, a]) + "?", correcta: "ok", opciones: uniq([{clave: "ok", html: ptxt(h, k)}, {clave: "s", html: ptxt(-h, k)}, {clave: "c", html: ptxt(h, c)}, {clave: "w", html: ptxt(k, h)}, {clave: "n", html: ptxt(h, -k || k + 2)}, {clave: "u", html: ptxt(h + 1, k)}]).slice(0, 4),
       pista: T("x = −b/(2a); then evaluate f at that x.", "x = −b/(2a); después evalúe f en esa x."), bien: "x = −(" + sg(b) + ") / (2 · " + (a < 0 ? "(" + sg(a) + ")" : a) + ") = " + sg(h) + "; f(" + sg(h) + ") = " + sg(k) + "."}; }
   var P = elige([1000, 2000, 500]), r = elige([5, 10, 20]), A = P * (1 + r / 100);
   return {tema: 8, enun: T("$" + P.toLocaleString("en-US") + " at " + r + "% a year, compounded yearly, for 1 year gives:", "$" + P.toLocaleString("en-US") + " al " + r + " % anual, capitalizado una vez al año, en 1 año dan:"), correcta: "ok",
     opciones: uniq([{clave: "ok", html: "$" + A.toLocaleString("en-US")}, {clave: "i", html: "$" + (P * r / 100).toLocaleString("en-US")}, {clave: "d", html: "$" + (P * (1 + r)).toLocaleString("en-US")}, {clave: "m", html: "$" + (P + r).toLocaleString("en-US")}]),
     pista: "A = P(1 + r)" + T(", with r as a decimal.", ", con r en decimal."), bien: "A = " + P.toLocaleString("en-US") + "(1 + " + r / 100 + ") = $" + A.toLocaleString("en-US") + "."}; }];
var NOMBRES_T = [TEMA_N1, TEMA_N2, TEMA_N3, TEMA_N4, TEMA_N5, TEMA_N6, TEMA_N7, TEMA_N8];
function genMezcla(){
  var sel = [].map.call(document.querySelectorAll("#mz-temas input:checked"), function(c){ return +c.value; });
  if (!sel.length) sel = [1, 2, 3, 4, 5, 6, 7, 8];
  var q = MEZCLA[elige(sel) - 1]();
  q.enun = '<span class="nota">' + T("Topic ", "Tema ") + q.tema + " · " + NOMBRES_T[q.tema - 1] + "</span><br>" + q.enun;
  return q;
}

/* MODULE 2 · Search in the index of practices */
function busca(){
  var qv = $("ix-q").value.trim().toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""), hay = 0;
  Array.prototype.forEach.call(document.querySelectorAll("#ix-lista li[data-txt]"), function(li){ var ok = !qv || li.getAttribute("data-txt").indexOf(qv) >= 0; li.hidden = !ok; if (ok) hay++; });
  Array.prototype.forEach.call(document.querySelectorAll("#ix-lista section"), function(sec){ sec.hidden = !sec.querySelector("li[data-txt]:not([hidden])"); });
  $("ix-nada").hidden = hay > 0;
  $("ix-cuenta").textContent = qv ? T(hay + (hay === 1 ? " practice found." : " practices found."), (hay === 1 ? "Se encontró 1 práctica." : "Se encontraron " + hay + " prácticas.")) : "";
}
OMR("mz", genMezcla);
$("ix-q").addEventListener("input", busca);
'''

def practica_pagina():
    n = N
    nombres = [t(*nm) for _, nm in TEMAS]
    js = LOGICA
    for i, nmb in enumerate(nombres, 1):
        js = js.replace(f"TEMA_N{i}", '"' + nmb.replace('"', '\\"') + '"')
    casillas = "".join(f'<label class="casilla"><input type="checkbox" value="{k}" checked> {k}. {nombres[int(k) - 1]}</label>' for k, _ in TEMAS)
    filas = indice_practicas()
    secs = []
    for tema, nm_ in TEMAS:
        items = [f for f in filas if f[0] == tema]
        if not items:
            continue
        li = "".join(f'<li data-txt="{H.escape((lt + " " + mt + " " + tx).lower(), quote=True)}"><a href="{href}">{mt}</a> <span class="nota">· {t("Lesson", "Lección")} {lec.replace("-", ".")} · {lt}</span></li>' for _, lec, lt, href, mt, tx in items)
        secs.append(f'<section><h3>{tema}. {t(*nm_)}</h3><ul>{li}</ul></section>')
    lista = re.sub(r'data-txt="([^"]*)"', lambda m: 'data-txt="' + __import__("unicodedata").normalize("NFD", H.unescape(m.group(1))).encode("ascii", "ignore").decode().replace('"', "") + '"', "\n".join(secs))
    mods = [
     (t("mixed", "mezcla"), t("Mixed review of the eight topics", "Repaso mezclado de los ocho temas"),
      f'''      <p>{t("One question at a time from any topic of Level 4. If you make a mistake, you get a hint and another try. Uncheck the topics you do not want to practice.", "Una pregunta a la vez de cualquier tema del Nivel 4. Si se equivoca, recibe una pista y otra oportunidad. Desmarque los temas que no quiera practicar.")}</p>
      <fieldset class="panel" id="mz-temas"><legend>{t("Topics", "Temas")}</legend><div class="casillas">{casillas}</div></fieldset>
{B.om("mz", t("Practice: mixed review", "Practique: repaso mezclado"))}'''),
     (t("index", "indice"), t("Every practice of Level 4", "Todas las prácticas del Nivel 4"),
      f'''      <p>{t("All the practice activities of the eight topics, in one place. Each link opens exactly the practice you need, not the whole page. If the final check pointed out a topic, find it here and go straight to it.", "Las prácticas de los ocho temas, reunidas en un solo sitio. Cada enlace abre directamente la práctica que necesita, no la página entera. Si la evaluación final señaló un tema, búsquelo aquí y vaya al grano.")}</p>
      <div class="panel"><div class="campo"><label for="ix-q">{t("Search by word", "Buscar por palabra")}</label><input type="search" id="ix-q" class="ancho" autocomplete="off" placeholder="{t("for example: vertex, cone, elimination", "por ejemplo: vértice, cono, eliminación")}"></div>
        <p class="nota" id="ix-cuenta" aria-live="polite"></p></div>
      <p class="caja-aviso visible" id="ix-nada" hidden>{t("No practice has that word. Try a shorter word or clear the search.", "No hay ninguna práctica con esa palabra. Pruebe con un término más corto o borre la búsqueda.")}</p>
      <div id="ix-lista">
{lista}
      </div>''')]
    return B.pagina_practica(n, 8, t(*TEMA), t("Level 4 review", "Repaso del Nivel 4"),
        t("A mixed practice of the eight topics and an index of every practice of the level. The exercises change every time.", "Una práctica mezclada de los ocho temas y un índice de todas las prácticas del nivel. Los ejercicios cambian cada vez."),
        mods, js, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Proyecto final integrador y simulacro GED")
