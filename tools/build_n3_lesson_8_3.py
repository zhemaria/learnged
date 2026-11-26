"""Level 3 · Lesson 8.3 · Final project and strategies for the GED math test — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_8-3.html and algebra/n3-repaso.html (GEDparaHispanos).
The practice page is the Level 3 review: a mixed practice of the eight topics and an index, with search, of every practice activity of the level
(read from the practice pages already built, so build every other lesson first).
The project template and the final check are built by tools/build_n3_proyecto.py and tools/build_n3_final.py.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import os, re, html as H
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n3
from build_n3_lesson_8_1 import TEMA, SCRIPTS
from build_n3_explora_8 import ESTILO8

B.NIVEL = 3
N = "8-3"
TIT = ("Final project and strategies for the GED math test", "Proyecto final integrador y estrategias para el GED")
TEMAS = [("1", ("Rules of exponents", "Reglas de los exponentes")), ("2", ("Scientific notation", "Notación científica")), ("3", ("Radicals and the real numbers", "Radicales y números reales")),
         ("4", ("Linear algebra", "Álgebra lineal")), ("5", ("Inequalities and formulas", "Inecuaciones y fórmulas")), ("6", ("Geometry: angles, Pythagoras, and similarity", "Geometría: ángulos, Pitágoras y semejanza")),
         ("7", ("Volume and data analysis", "Volumen y análisis de datos")), ("8", ("Counting and probability", "Combinatoria y probabilidad"))]

def proyecto(): return t('<a href="project-level-3.html">Final project template: My data analysis</a>', '<a href="proyecto-nivel-3.html">Plantilla del proyecto final: Mi análisis de datos</a>')
def final(): return t('<a href="final-check-level-3.html">Level 3 final check</a>', '<a href="evaluacion-final-nivel-3.html">Evaluación final del Nivel 3</a>')

def leccion():
    n = N
    comps = [[t("Data set", "Conjunto de datos"), t("Real data (ages, expenses, temperatures…) described with their source.", "Datos reales (edades, gastos, temperaturas…) descritos con su fuente.")],
             [t("Graph", "Gráfica"), t("A box plot or a histogram, with all its labels.", "Un diagrama de caja o un histograma, con todas sus etiquetas.")],
             [t("Statistics", "Estadísticos"), t("At least three calculations: mean, median, IQR, or another one.", "Al menos tres cálculos: media, mediana, IQR u otro.")],
             [t("Interpretation", "Interpretación"), t("A text that explains what the data say.", "Un texto que explique qué dicen los datos.")],
             [t("Probability", "Probabilidad"), t("At least one probability calculation connected to the context.", "Al menos un cálculo de probabilidad vinculado al contexto.")]]
    s1 = f'''<p>{t("This lesson closes Level 3. It brings together the number sense of Topics 1 to 3 (exponents, scientific notation, real numbers), the algebra of Topics 4 and 5 (equations, inequalities, formulas), the geometry of Topics 6 and 7 (Pythagoras, similarity, volume), and the statistics and probability of Topics 7 and 8. The final project and the preparation for the GED test put everything into practice at once.", "Esta lección cierra el Nivel 3. Reúne el sentido numérico de los Temas 1 al 3 (exponentes, notación científica, números reales), el álgebra de los Temas 4 y 5 (ecuaciones, inecuaciones, fórmulas), la geometría de los Temas 6 y 7 (Pitágoras, semejanza, volumen) y la estadística y probabilidad de los Temas 7 y 8. El proyecto integrador y la preparación para el examen GED ponen todo en práctica a la vez.")}</p>
<p>{t("The final project, <strong>“My data analysis”</strong>, is to analyze a real data set and present it completely. It must include five parts:", "El proyecto final, <strong>«Mi análisis de datos»</strong>, consiste en analizar un conjunto de datos real y presentarlo de forma completa. Debe incluir cinco componentes:")}</p>
{tabla(t("Parts of the final project", "Componentes del proyecto"), t("The five parts of the final project “My data analysis”", "Componentes del proyecto integrador «Mi análisis de datos»"), [t("Part", "Componente"), t("What is expected", "Qué se espera")], comps)}
{caja("tip", t("Data from your own life are more interesting", "Datos cercanos motivan más"), t("<p>Choose a data set from your own world: your expenses for the month, the ages in your family, the temperatures this week. Analyzing something of your own makes the project more meaningful and easier to interpret.</p>", "<p>Conviene elegir un conjunto de datos del propio entorno: los gastos del mes, las edades de la familia, las temperaturas de la semana. Analizar algo propio hace el proyecto más significativo y fácil de interpretar.</p>"))}'''

    pasos = [t("Collect 10 to 20 real data values and put them in order.", "Reunir entre 10 y 20 datos reales y ordenarlos."),
             t("Find the statistics (mean, median, Q1, Q3, IQR).", "Calcular los estadísticos (media, mediana, Q1, Q3, IQR)."),
             t("Draw the graph you chose (box plot or histogram) with its labels.", "Construir la gráfica elegida (diagrama de caja o histograma) con sus etiquetas."),
             t("Write the interpretation: shape, center, and spread of the data.", "Escribir la interpretación: forma, centro y dispersión de los datos."),
             t("Ask and answer a probability question about the context.", "Plantear y calcular una probabilidad ligada al contexto.")]
    s2 = f'''<p>{t("Build the project in a clear order, using the tools of Topics 7 and 8.", "El proyecto se arma siguiendo un orden claro, usando las herramientas de los Temas 7 y 8.")}</p>
<ol>{"".join(f"<li>{p}</li>" for p in pasos)}</ol>
{caja("ojo", t("The interpretation is the key", "La interpretación es clave"), t("<p>The project does not end with the graph. The most valuable part is the text that explains what the data mean: where they are concentrated, how spread out they are, and what you can conclude. A graph with no interpretation is incomplete.</p>", "<p>El proyecto no termina con la gráfica. Lo más valioso es el texto que explica qué significan los datos: dónde se concentran, qué tan dispersos están y qué se puede concluir. Una gráfica sin interpretación queda incompleta.</p>"))}
{caja("tip", t("The project template", "La plantilla del proyecto"), t(f"<p>Use the {proyecto()}. You type your data and your work, and it checks your statistics, draws the graph, checks your probability, and saves your work in this browser. When you finish, save it as a PDF.</p>", f"<p>Use la {proyecto()}. Usted escribe sus datos y su trabajo, y la plantilla comprueba sus estadísticos, dibuja la gráfica, verifica su probabilidad y guarda su trabajo en este navegador. Al terminar, guárdelo como PDF.</p>"))}
{practica("p1", t("Practice 1 — The data set", "Práctica 1 — El conjunto de datos"), t("The data set of the project must be…", "El conjunto de datos del proyecto debe ser…"), [("a", t("made up at random", "inventado al azar")), ("b", t("only two numbers", "de solo dos números")), ("c", t("real, with its source described", "real, con su fuente descrita"))])}
{practica("p2", t("Practice 2 — The graph", "Práctica 2 — La gráfica"), t("The graph of the project can be…", "La gráfica del proyecto puede ser…"), [("a", t("only a circle graph", "solo una gráfica circular")), ("b", t("a box plot or a histogram", "un diagrama de caja o un histograma")), ("c", t("only a table with no graph", "solo una tabla sin gráfica"))])}
{practica("p3", t("Practice 3 — What else?", "Práctica 3 — ¿Qué más?"), t("Besides the graph and the statistics, the project asks for…", "Además de la gráfica y los estadísticos, el proyecto pide…"), [("a", t("at least one probability calculation", "al menos un cálculo de probabilidad")), ("b", t("only the title", "solo el título")), ("c", t("a decorative photo", "una fotografía decorativa"))])}'''

    estr = [[t("Use the formula sheet", "Usar la hoja de fórmulas"), t("The test gives you formulas for area, volume, and more: you do not memorize them, you learn where they are and how to use them.", "El examen provee fórmulas de área, volumen y otras: no hay que memorizarlas, sino saber localizarlas y usarlas.")],
            [t("Manage your time", "Manejar el tiempo"), t("Do not spend too long on one question; flag it and come back at the end.", "No detenerse demasiado en una pregunta; marcarla y volver al final.")],
            [t("Use the TI-30XS calculator", "Usar la calculadora TI-30XS"), t("Use it for roots, powers, π, nPr, and nCr; clear it before each calculation.", "Aprovecharla para raíces, potencias, π, nPr y nCr; limpiarla antes de cada cálculo.")],
            [t("Estimate first", "Estimar primero"), t("A quick estimate helps you rule out choices that make no sense in multiple-choice questions.", "Una estimación rápida ayuda a descartar opciones absurdas en las preguntas de opción múltiple.")],
            [t("Read what is asked", "Leer lo que se pregunta"), t("Underline the question and the units. Many wrong answers are right answers to a different question.", "Subraye la pregunta y las unidades. Muchas respuestas incorrectas son respuestas correctas a otra pregunta.")]]
    s3 = f'''<p>{t("The GED Mathematical Reasoning test measures reasoning, not only calculation. These strategies help you do your best:", "El examen GED de Razonamiento Matemático evalúa el razonamiento, no solo el cálculo. Estas estrategias ayudan a rendir mejor:")}</p>
{tabla(t("Strategies for the GED math test", "Estrategias para el examen GED"), t("Strategies for the GED Mathematical Reasoning test", "Estrategias para el examen GED de Razonamiento Matemático"), [t("Strategy", "Estrategia"), t("How to use it", "Cómo aplicarla")], estr)}
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. The calculator on this page does the same operations, although some keys have other names or are in other places. If you have a TI-30XS, practice with it too so you learn where its keys are.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. La calculadora de esta página hace las mismas operaciones, aunque algunas teclas tienen otro nombre o están en otro lugar. Si tiene una TI-30XS, practique también con ella para conocer la ubicación de sus teclas.</p>"))}
{caja("tip", t("The formula sheet is your friend", "La hoja de fórmulas es una aliada"), t("<p>Since the test gives it to you, practice with it from now on, so that on test day you know exactly where each formula is. Open it with the Reference sheet button on this page. Level 4 will build on this preparation.</p>", "<p>Como el examen la provee, conviene practicar con ella desde ahora, para llegar al día de la prueba sabiendo exactamente dónde está cada fórmula. Ábrala con el botón Hoja de referencia de esta página. El Nivel 4 reforzará esta preparación.</p>"))}'''

    mapa = [[t("1. Exponents", "1. Exponentes"), t("Product, quotient, and power rules, and negative exponents.", "Reglas del producto, cociente, potencias y exponentes negativos.")],
            [t("2. Scientific notation", "2. Notación científica"), t("Converting and operating with powers of 10.", "Conversión y operaciones con potencias de 10.")],
            [t("3. Real numbers", "3. Números reales"), t("Radicals, rational and irrational numbers, the number line.", "Radicales, racionales e irracionales, recta numérica.")],
            [t("4. Linear algebra", "4. Álgebra lineal"), t("Variables, expressions, and equations in one variable.", "Variables, expresiones y ecuaciones en una variable.")],
            [t("5. Inequalities and formulas", "5. Inecuaciones y fórmulas"), t("Inequalities, word problems, and solving formulas.", "Inecuaciones, problemas verbales y despeje de fórmulas.")],
            [t("6. Geometry", "6. Geometría"), t("Angles, Pythagoras, similarity, and scale.", "Ángulos, Pitágoras, semejanza y escala.")],
            [t("7. Volume and data", "7. Volumen y datos"), t("Volume of solids, box plots, histograms.", "Volumen de sólidos, caja y bigotes, histogramas.")],
            [t("8. Probability", "8. Probabilidad"), t("Counting, permutations, combinations, and compound probability.", "Conteo, permutaciones, combinaciones y probabilidad compuesta.")]]
    s4 = f'''<p>{t("Level 3 covered eight topics. This is the full map of what you learned, which the final check will test.", "El Nivel 3 recorrió ocho temas. Este es el mapa completo de lo aprendido, que la evaluación final pondrá a prueba.")}</p>
{tabla(t("The eight topics of Level 3", "Los ocho temas del Nivel 3"), t("Map of the eight topics of Level 3", "Mapa de los ocho temas del Nivel 3"), [t("Topic", "Tema"), t("Main content", "Contenido principal")], mapa)}
{practica("p4", t("Practice 4 — Exponents", "Práctica 4 — Exponentes"), t("Simplify: x⁵ · x³.", "Simplifique: x⁵ · x³."), [("a", "x⁸"), ("b", "x¹⁵"), ("c", "x²")])}
{practica("p5", t("Practice 5 — An equation", "Práctica 5 — Una ecuación"), t("Solve: 2x + 3 = 11.", "Resuelva: 2x + 3 = 11."), [("a", "x = 7"), ("b", "x = 5"), ("c", "x = 4")])}
{practica("p6", t("Practice 6 — Pythagoras", "Práctica 6 — Pitágoras"), t("The legs measure 6 and 8. The hypotenuse measures…", "Catetos 6 y 8: la hipotenusa mide…"), [("a", "14"), ("b", "10"), ("c", "48")])}
{enlace(n, t("mixed", "mezcla"), t("mixed review of the eight topics", "repaso mezclado de los ocho temas"), t("One question at a time from any topic, with a hint and a second try.", "Una pregunta a la vez de cualquier tema, con pista y segunda oportunidad."))}
{enlace(n, t("index", "indice"), t("every practice of Level 3", "todas las prácticas del Nivel 3"), t("Search by word and go straight to the practice you need.", "Busque por palabra y vaya directo a la práctica que necesita."))}
{caja("tip", t("The final check", "La evaluación final"), t(f"<p>When you are ready, take the {final()}: 25 questions from the eight topics, answered all at once, with a report by topic that tells you what to review. You pass with 18 right answers (70%).</p>", f"<p>Cuando esté listo, haga la {final()}: 25 preguntas de los ocho temas, respondidas de una sola vez, con un informe por tema que le dice qué repasar. Se aprueba con 18 aciertos (70%).</p>"))}'''

    secciones = [("s-" + t("project", "proyecto"), t("The project “My data analysis”", "El proyecto «Mi análisis de datos»"), s1),
                 ("s-" + t("build", "construir"), t("How to build the project", "Cómo construir el proyecto"), s2),
                 ("s-" + t("strategies", "estrategias"), t("Strategies for the GED test", "Estrategias para el examen GED"), s3),
                 ("s-" + t("review", "repaso"), t("Review of the eight topics", "Repaso integrador de los ocho temas"), s4)]

    lesson = {"next": t("Level 4", "Nivel 4"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Made-up data do not tell you anything about the real world.", "Los datos inventados no dicen nada del mundo real."), "b": t("Two numbers are not enough to find quartiles or draw a graph.", "Dos números no alcanzan para hallar cuartiles ni dibujar una gráfica.")}, "right": t("Real data, 10 to 20 values, with their source described.", "Datos reales, de 10 a 20 valores, con su fuente descrita."), "solution": t("Real, with its source described.", "Real, con su fuente descrita.")},
      "p2": {"ok": "b", "hints": {"a": t("A circle graph is for categories; the project analyzes numerical data.", "La gráfica circular es para categorías; el proyecto analiza datos numéricos."), "c": t("The project asks for a graph.", "El proyecto pide una gráfica.")}, "right": t("A box plot or a histogram, with all its labels.", "Un diagrama de caja o un histograma, con todas sus etiquetas."), "solution": t("A box plot or a histogram.", "Un diagrama de caja o un histograma.")},
      "p3": {"ok": "a", "hints": {"b": t("The title alone is not one of the five parts.", "El título solo no es uno de los cinco componentes."), "c": t("A photo does not analyze anything.", "Una fotografía no analiza nada.")}, "right": t("The fifth part is a probability calculation connected to the data.", "El quinto componente es un cálculo de probabilidad ligado a los datos."), "solution": t("At least one probability calculation.", "Al menos un cálculo de probabilidad.")},
      "p4": {"ok": "a", "hints": {"b": t("The exponents are added, not multiplied.", "Los exponentes se suman, no se multiplican."), "c": t("The exponents are added, not subtracted.", "Los exponentes se suman, no se restan.")}, "right": "5 + 3 = 8.", "solution": "x⁸."},
      "p5": {"ok": "c", "hints": {"a": t("Subtract 3 first: 2x = 8.", "Primero reste 3: 2x = 8."), "b": t("Check: 2 · 5 + 3 = 13, not 11.", "Compruebe: 2 · 5 + 3 = 13, no 11.")}, "right": "2x = 8, x = 4.", "solution": "x = 4."},
      "p6": {"ok": "b", "hints": {"a": t("You added the legs. Add their squares and take the root.", "Sumó los catetos. Hay que sumar sus cuadrados y sacar la raíz."), "c": t("You multiplied the legs.", "Multiplicó los catetos.")}, "right": "36 + 64 = 100, √100 = 10.", "solution": "10."}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("The project uses real data, not made-up data.", "El proyecto usa datos reales, no inventados."), "c": t("Count them: data, graph, statistics, interpretation, probability.", "Cuéntelos: datos, gráfica, estadísticos, interpretación, probabilidad."), "d": t("A single statistic is not enough.", "Un solo estadístico no basta.")}, "solution": t("Five parts.", "Cinco componentes.")},
      "B": {"ok": "d", "hints": {"a": t("The graph shows the data, but it does not explain them.", "La gráfica muestra los datos, pero no los explica."), "b": t("The title alone says nothing about the data.", "El título solo no dice nada de los datos."), "c": t("The calculations are needed, but they are not the most valuable part.", "Los cálculos son necesarios, pero no son lo más valioso.")}, "solution": t("The written interpretation.", "La interpretación escrita.")},
      "C": {"ok": "a", "hints": {"b": t("The GED test gives you a formula sheet.", "El examen GED provee una hoja de fórmulas."), "c": t("The formulas are given: learn where they are.", "Las fórmulas se dan: hay que saber dónde están."), "d": t("You can use it on the whole math test.", "Se puede usar en todo el examen de matemáticas.")}, "solution": t("Know where each formula is and how to use it.", "Saber dónde está cada fórmula y cómo usarla.")},
      "D": {"ok": "c", "hints": {"a": t("That can use up the time for the other questions.", "Eso puede agotar el tiempo de las demás preguntas."), "b": t("A blank answer is always wrong; flag it and come back.", "Una respuesta en blanco siempre es incorrecta; márquela y vuelva."), "d": t("Guessing first wastes the chance to come back with more time.", "Adivinar primero desperdicia la oportunidad de volver con más tiempo.")}, "solution": t("Flag it and come back at the end.", "Marcarla y volver al final.")},
      "E": {"ok": "b", "hints": {"a": t("Estimating does not replace the calculation; it helps you check.", "Estimar no reemplaza el cálculo; ayuda a comprobar."), "c": t("A quick estimate takes seconds.", "Una estimación rápida toma segundos."), "d": t("The estimate is a check, not the final answer.", "La estimación es una comprobación, no la respuesta final.")}, "solution": t("To rule out choices that make no sense.", "Para descartar opciones absurdas.")},
      "F": {"ok": "c", "hints": {"a": t("The exponents are added, not multiplied.", "Los exponentes se suman, no se multiplican."), "b": t("The exponents are added, not subtracted.", "Los exponentes se suman, no se restan."), "d": t("That is 4 × 4. Add the exponents: 4 + 2.", "Eso es 4 × 4. Sume los exponentes: 4 + 2.")}, "solution": "x⁶."},
      "G": {"ok": "a", "hints": {"b": t("You subtracted 3. Divide by 3.", "Restó 3. Hay que dividir entre 3."), "c": t("You added 3. Divide by 3.", "Sumó 3. Hay que dividir entre 3."), "d": t("You multiplied. Divide by 3.", "Multiplicó. Hay que dividir entre 3.")}, "solution": "x = 7."},
      "H": {"ok": "d", "hints": {"a": t("3/2 compares red with blue, not red with the total.", "3/2 compara rojas con azules, no con el total."), "b": t("The fraction is upside down.", "La fracción está al revés."), "c": t("The fraction is upside down.", "La fracción está al revés.")}, "solution": "3/5."}
     }}

    quiz = [
     ("A", t("How many parts must the final project have?", "¿Cuántos componentes debe tener el proyecto final?"), [("a", "3"), ("b", "5"), ("c", "4"), ("d", "1")]),
     ("B", t("The most valuable part of the project is…", "Lo más valioso del proyecto es…"), [("a", t("the graph", "la gráfica")), ("b", t("the title", "el título")), ("c", t("the calculations", "los cálculos")), ("d", t("the written interpretation", "la interpretación escrita"))]),
     ("C", t("On the GED test, the best use of the formula sheet is…", "En el examen GED, lo mejor con la hoja de fórmulas es…"), [("a", t("knowing where each formula is and how to use it", "saber dónde está cada fórmula y cómo usarla")), ("b", t("memorizing it, because it is not given", "memorizarla, porque no se entrega")), ("c", t("ignoring it", "ignorarla")), ("d", t("using it only on the first question", "usarla solo en la primera pregunta"))]),
     ("D", t("A question is taking you too long. The best thing to do is…", "Una pregunta le está tomando demasiado tiempo. Lo mejor es…"), [("a", t("stay on it until you finish", "quedarse en ella hasta terminar")), ("b", t("leave it blank and forget it", "dejarla en blanco y olvidarla")), ("c", t("flag it and come back at the end", "marcarla y volver al final")), ("d", t("guess right away and never come back", "adivinar enseguida y no volver"))]),
     ("E", t("Why estimate before you calculate?", "¿Para qué sirve estimar antes de calcular?"), [("a", t("To avoid calculating", "Para no calcular")), ("b", t("To rule out choices that make no sense", "Para descartar opciones absurdas")), ("c", t("To use more time", "Para gastar más tiempo")), ("d", t("To replace the answer", "Para reemplazar la respuesta"))]),
     ("F", t("Simplify: x⁴ · x².", "Simplifique: x⁴ · x²."), [("a", "x⁸"), ("b", "x²"), ("c", "x⁶"), ("d", "x¹⁶")]),
     ("G", t("Solve: 3x = 21.", "Resuelva: 3x = 21."), [("a", "x = 7"), ("b", "x = 18"), ("c", "x = 24"), ("d", "x = 63")]),
     ("H", t("A bag has 3 red and 2 blue (5). P(red in one draw) is…", "Bolsa con 3 rojas y 2 azules (5). P(roja en una extracción) es…"), [("a", "3/2"), ("b", "5/3"), ("c", "2/3"), ("d", "3/5")])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Bring Level 3 together in your own data project, learn strategies for the GED math test, and review the eight topics.", "Reúna el Nivel 3 en un proyecto con sus propios datos, aprenda estrategias para el examen GED y repase los ocho temas."),
        ("🎓", t("The close of Level 3", "El cierre del Nivel 3")),
        [t("<strong>Present</strong> the final project “My data analysis” with all its parts.", "<strong>Presentar</strong> el proyecto integrador «Mi análisis de datos» con todos sus componentes."),
         t("<strong>Bring together</strong> in one piece of work what you learned in statistics, probability, and calculation.", "<strong>Reunir</strong> en un solo trabajo lo aprendido en estadística, probabilidad y cálculo."),
         t("<strong>Use</strong> test strategies for the GED Mathematical Reasoning test.", "<strong>Aplicar</strong> estrategias de examen para el GED de Razonamiento Matemático."),
         t("<strong>Use</strong> the official GED formula sheet and manage the time of the test.", "<strong>Usar</strong> la hoja de fórmulas oficial del GED y manejar el tiempo de la prueba."),
         t("<strong>Answer</strong> GED-style questions that combine the eight topics of the level.", "<strong>Responder</strong> preguntas tipo GED que integran los ocho temas del nivel.")],
        secciones,
        (t(f"This is the last homework of Level 3 and the longest: give yourself two or three calm sessions. (1) Complete “My data analysis” in the {proyecto()}, with its five parts, and save it as a PDF. (2) Let it rest for a day; then read it as if it were someone else's, with the rubric in hand, and explain it out loud for three or four minutes: what you cannot explain yet, you do not understand yet. (3) Review the whole GED formula sheet and mark the formulas you used in this level. (4) Take the {final()} in one sitting, with no interruptions and without looking at the lessons.",
           f"Esta es la última tarea del Nivel 3 y la más larga: dese dos o tres sesiones tranquilas. (1) Complete «Mi análisis de datos» en la {proyecto()}, con sus cinco componentes, y guárdelo en PDF. (2) Déjelo reposar un día; después léalo como si fuera de otra persona, con la rúbrica en la mano, y explíquelo en voz alta durante tres o cuatro minutos: lo que no logre explicar todavía no lo entendió. (3) Repase entera la hoja de fórmulas del GED y marque las fórmulas que usó en este nivel. (4) Haga la {final()} de una sentada, sin interrupciones y sin consultar las lecciones."),
         t("Choose the data for your project from your own life: what you spend each day for two weeks, the minutes you sleep each night, the prices of a product in several stores, or the temperatures of the month in your city.",
           "Elija los datos de su proyecto de su propia vida: lo que gasta cada día durante dos semanas, los minutos que duerme cada noche, los precios de un producto en varias tiendas o las temperaturas del mes en su ciudad.")),
        quiz,
        t("Rubric for the final project", "Rúbrica del proyecto final"),
        t("Rubric for the final project “My data analysis”", "Rúbrica del proyecto final «Mi análisis de datos»"),
        [(t("Data set", "Conjunto de datos"), t("Real, relevant data, with the source and context explained.", "Datos reales, relevantes y con su fuente y contexto explicados."), t("Real data, but with no clear source.", "Datos reales, pero sin fuente clara."), t("Made-up data, or data with no description.", "Datos inventados o sin describir.")),
         (t("Graph", "Representación gráfica"), t("A correct box plot or histogram with all its labels, right for the data.", "Caja o histograma correcto, con todas sus etiquetas y adecuado a los datos."), t("A graph with mistakes or no labels.", "Gráfica con errores o sin etiquetas."), t("No valid graph.", "No incluye una gráfica válida.")),
         (t("Statistics", "Cálculo de estadísticos"), t("At least three statistics with no mistakes, connected to each other.", "Al menos tres estadísticos sin errores, relacionados entre sí."), t("Fewer than three, or with mistakes.", "Menos de tres o con errores."), t("No statistics.", "No calcula estadísticos.")),
         (t("Written interpretation", "Interpretación escrita"), t("A clear interpretation that matches the data (center, spread, and shape).", "Interpretación clara y coherente con los datos (centro, dispersión y forma)."), t("A vague interpretation, or one that does not match the data.", "Interpretación vaga o incoherente con los datos."), t("No interpretation.", "No interpreta los datos.")),
         (t("Probability", "Cálculo de probabilidad"), t("A correct probability, well explained and connected to the analysis.", "Probabilidad correcta, bien explicada y ligada al análisis."), t("A probability with mistakes.", "Cálculo de probabilidad con errores."), t("No probability.", "No incluye probabilidad."))],
        t("<p>This lesson closes all of Level 3. Across eight topics you built a solid path: from number sense (exponents, scientific notation, and real numbers) to algebra (equations, inequalities, and formulas), from geometry (Pythagoras, similarity, and volume) to statistics and probability (box plots, histograms, counting, and compound probability). The final project brought everything together in an analysis of your own.</p>\n<p>The next step is <strong>Level 4</strong>, where algebra goes deeper with polynomials, factoring, quadratic equations, systems of equations, and functions, completing your preparation for the GED Mathematical Reasoning test. Congratulations on reaching the end of Level 3!</p>",
          "<p>Con esta lección se cierra el Nivel 3 completo. A lo largo de ocho temas se construyó un recorrido sólido: del sentido numérico (exponentes, notación científica y números reales) al álgebra (ecuaciones, inecuaciones y fórmulas), de la geometría (Pitágoras, semejanza y volumen) a la estadística y la probabilidad (caja, histograma, conteo y probabilidad compuesta). El proyecto integrador reunió todo en un análisis propio.</p>\n<p>El siguiente paso es el <strong>Nivel 4</strong>, donde el álgebra se profundiza con polinomios, factorización, ecuaciones cuadráticas, sistemas de ecuaciones y funciones, completando la preparación para el examen GED de Razonamiento Matemático. ¡Enhorabuena por llegar al final del Nivel 3!</p>"),
        (None, ("", t("Level 4", "Nivel 4"))),
        [(t("data set", "conjunto de datos"), t("The group of values you collect and analyze.", "El grupo de valores que se reúnen y se analizan.")),
         (t("interpretation", "interpretación"), t("A written explanation of what the data say: center, spread, and shape.", "Una explicación escrita de lo que dicen los datos: centro, dispersión y forma.")),
         (t("formula sheet", "hoja de fórmulas"), t("The page of formulas the GED test gives you during the math test.", "La página de fórmulas que el examen GED entrega durante la prueba de matemáticas.")),
         (t("estimate", "estimar"), t("To find an approximate answer quickly, to check the exact one.", "Hallar rápidamente una respuesta aproximada, para comprobar la exacta."))],
        lesson)

# ---------------- practice page: the Level 3 review ----------------
def indice_practicas():
    """Reads every Level 3 practice page in the current language and lists its modules: (topic, lesson, lesson title, module id, module title)."""
    base = os.path.join(B.ROOT, "math/level-3" if B.L == "en" else "es/matematicas/nivel-3")
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
                texto = H.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", cuerpo)))[:700]
                filas.append((tema, n, tit, f"{pref}{n}.html#{mid}", H.unescape(re.sub(r"<[^>]+>", "", mt)), texto))
    return filas

LOGICA = r'''
/* MODULE 1 · Mixed review: one question at a time from any topic */
function sup(n){ return "<sup>" + n + "</sup>"; }
var MEZCLA = [
 function(){ var v = elige(["x", "y", "a"]), a = aleatorio(2, 7), b = aleatorio(2, 6); if (a * b === a + b) b = 3;
   return {tema: 1, enun: T("Simplify: ", "Simplifique: ") + v + sup(a) + " · " + v + sup(b), opciones: [{html: v + sup(a + b), clave: "b"}, {html: v + sup(a * b), clave: "m"}, {html: (a === b ? "2" : "") + v + sup(Math.abs(a - b) || 1), clave: "r"}], correcta: "b",
     porClave: {m: T("Add the exponents; multiply them only for a power of a power.", "Los exponentes se suman; se multiplican solo en la potencia de una potencia.")}, pista: T("Same base: add the exponents.", "Misma base: se suman los exponentes."), bien: a + " + " + b + " = " + (a + b) + ".", mal: T("Same base: add the exponents, ", "Misma base: se suman los exponentes, ") + a + " + " + b + " = " + (a + b) + "."}; },
 function(){ var c = aleatorio(2, 9), e = aleatorio(3, 6), num = c * Math.pow(10, e);
   return {tema: 2, enun: T("Write " + com(num) + " in scientific notation.", "Escriba " + com(num) + " en notación científica."), opciones: [{html: c + " × 10" + sup(e), clave: "b"}, {html: c + " × 10" + sup(e + 1), clave: "m"}, {html: (c * 10) + " × 10" + sup(e - 1), clave: "d"}], correcta: "b",
     porClave: {m: T("Count the places the decimal point moves: " + e + ".", "Cuente los lugares que se mueve el punto: " + e + "."), d: T("The first factor must be at least 1 and less than 10.", "El primer factor debe ser mayor o igual que 1 y menor que 10.")}, pista: T("The first number goes from 1 to 9.99…; count the places the point moves.", "El primer número va de 1 a 9.99…; cuente los lugares que se mueve el punto."), bien: com(num) + " = " + c + " × 10" + sup(e) + ".", mal: com(num) + " = " + c + " × 10" + sup(e) + "."}; },
 function(){ var k = elige([2, 3, 5]), q = elige([2, 3, 5, 6, 7]); while (q === k) q = elige([2, 3, 6, 7]); var n = k * k * q;
   return {tema: 3, enun: T("Simplify: √" + n, "Simplifique: √" + n), opciones: [{html: k + "√" + q, clave: "b"}, {html: q + "√" + k, clave: "m"}, {html: (k * k) + "√" + q, clave: "c"}], correcta: "b",
     porClave: {c: T("Take the square root of the perfect square: √" + (k * k) + " = " + k + ".", "Se saca la raíz del cuadrado perfecto: √" + (k * k) + " = " + k + ".")}, pista: T("Find the largest perfect square that divides " + n + ".", "Busque el mayor cuadrado perfecto que divide a " + n + "."), bien: "√" + n + " = √" + (k * k) + " · √" + q + " = " + k + "√" + q + ".", mal: "√" + n + " = √" + (k * k) + " · √" + q + " = " + k + "√" + q + "."}; },
 function(){ var a, x, b, c; do { a = aleatorio(2, 6); x = aleatorio(2, 9); b = aleatorio(1, 15); c = a * x + b; } while (Math.abs((c + b) / a - (c - b)) < 1e-9);
   return {tema: 4, enun: T("Solve: ", "Resuelva: ") + a + "x + " + b + " = " + c, opciones: [{html: "x = " + x, clave: "b"}, {html: "x = " + nm(Math.round((c + b) / a * 100) / 100), clave: "s"}, {html: "x = " + (c - b), clave: "d"}], correcta: "b",
     porClave: {s: T("To undo + " + b + ", subtract it; do not add it.", "Para deshacer + " + b + " se resta, no se suma."), d: T("You still need to divide by " + a + ".", "Falta dividir entre " + a + ".")}, pista: T("First subtract " + b + ", then divide by " + a + ".", "Primero reste " + b + " y después divida entre " + a + "."), bien: a + "x = " + (c - b) + ", x = " + x + ".", mal: a + "x = " + (c - b) + ", x = " + x + "."}; },
 function(){ var a = aleatorio(2, 5), k = aleatorio(2, 9), c = a * k;
   return {tema: 5, enun: T("Solve: −", "Resuelva: −") + a + "x > " + c, opciones: [{html: "x &lt; −" + k, clave: "b"}, {html: "x &gt; −" + k, clave: "m"}, {html: "x &lt; " + k, clave: "s"}], correcta: "b",
     porClave: {m: T("Dividing by a negative number flips the sign.", "Al dividir entre un número negativo, el signo se invierte.")}, pista: T("You divide by −" + a + ": what happens to the sign?", "Se divide entre −" + a + ": ¿qué le pasa al signo?"), bien: T("Divide by −" + a + " and flip the sign: x < −" + k + ".", "Se divide entre −" + a + " y se invierte el signo: x < −" + k + "."), mal: T("Divide by −" + a + " and flip the sign: x < −" + k + ".", "Se divide entre −" + a + " y se invierte el signo: x < −" + k + ".")}; },
 function(){ var tr = elige([[3, 4, 5], [6, 8, 10], [5, 12, 13], [8, 15, 17]]);
   return {tema: 6, enun: T("The legs of a right triangle measure " + tr[0] + " and " + tr[1] + ". The hypotenuse measures…", "Los catetos de un triángulo rectángulo miden " + tr[0] + " y " + tr[1] + ". La hipotenusa mide…"), opciones: [{html: String(tr[2]), clave: "b"}, {html: String(tr[0] + tr[1]), clave: "s"}, {html: String(tr[0] * tr[0] + tr[1] * tr[1]), clave: "c"}], correcta: "b",
     porClave: {s: T("Add the squares, not the sides.", "Se suman los cuadrados, no los lados."), c: T("That is c². Take the square root.", "Ese es c². Falta la raíz cuadrada.")}, pista: "a² + b² = c².", bien: tr[0] + "² + " + tr[1] + "² = " + (tr[2] * tr[2]) + ", √" + (tr[2] * tr[2]) + " = " + tr[2] + ".", mal: tr[0] + "² + " + tr[1] + "² = " + (tr[2] * tr[2]) + ", √" + (tr[2] * tr[2]) + " = " + tr[2] + "."}; },
 function(){ var d, m, media; do { d = ordena(datosAzar(elige([5, 7]), 1, 20)); m = d[(d.length - 1) / 2]; media = Math.round(d.reduce(function(s, x){ return s + x; }, 0) / d.length * 10) / 10; } while (media === m || d[d.length - 1] - d[0] === m || d[d.length - 1] - d[0] === media);
   var o = [{html: String(m), clave: "b"}, {html: nm(media), clave: "me"}, {html: String(d[d.length - 1] - d[0]), clave: "r"}];
   return {tema: 7, enun: T("Data: ", "Datos: ") + d.join(", ") + T(". What is the median?", ". ¿Cuál es la mediana?"), opciones: o, correcta: "b", porClave: {me: T("That is the mean (the average). The median is the middle value.", "Esa es la media (el promedio). La mediana es el dato central."), r: T("That is the range.", "Ese es el rango.")}, pista: T("The data are already in order: find the middle one.", "Los datos ya están ordenados: busque el del centro."), bien: T("The middle value is " + m + ".", "El dato central es " + m + "."), mal: T("The middle value is " + m + ".", "El dato central es " + m + ".")}; },
 function(){ var n = aleatorio(5, 8), r = 2;
   return {tema: 8, enun: T("In how many ways can you choose 2 people out of " + n + " for a team (order does not matter)?", "¿De cuántas formas se pueden elegir 2 personas de " + n + " para un equipo (sin importar el orden)?"), opciones: [{html: String(comb(n, r)), clave: "b"}, {html: String(perm(n, r)), clave: "p"}, {html: String(n * n), clave: "m"}], correcta: "b",
     porClave: {p: T("That is the permutation. Order does not matter: divide by 2.", "Esa es la permutación. El orden no importa: divida entre 2.")}, pista: T("C(n, 2) = n × (n − 1) ÷ 2.", "C(n, 2) = n × (n − 1) ÷ 2."), bien: "C(" + n + ", 2) = " + n + " × " + (n - 1) + " ÷ 2 = " + comb(n, r) + ".", mal: "C(" + n + ", 2) = " + n + " × " + (n - 1) + " ÷ 2 = " + comb(n, r) + "."}; }];
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
OMR("p1", genMezcla);
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
    # make the search work without accents too
    lista = re.sub(r'data-txt="([^"]*)"', lambda m: 'data-txt="' + __import__("unicodedata").normalize("NFD", H.unescape(m.group(1))).encode("ascii", "ignore").decode().replace('"', "") + '"', "\n".join(secs))
    mods = [
     (t("mixed", "mezcla"), t("Mixed review of the eight topics", "Repaso mezclado de los ocho temas"),
      f'''      <p>{t("One question at a time from any topic of Level 3. If you make a mistake, you get a hint and another try. Uncheck the topics you do not want to practice.", "Una pregunta a la vez de cualquier tema del Nivel 3. Si se equivoca, recibe una pista y otra oportunidad. Desmarque los temas que no quiera practicar.")}</p>
      <fieldset class="panel" id="mz-temas"><legend>{t("Topics", "Temas")}</legend><div class="casillas">{casillas}</div></fieldset>
{B.om("p1", t("Practice: mixed review", "Practique: repaso mezclado"))}'''),
     (t("index", "indice"), t("Every practice of Level 3", "Todas las prácticas del Nivel 3"),
      f'''      <p>{t("All the practice activities of the eight topics, in one place. Each link opens exactly the practice you need, not the whole page. If the final check pointed out a topic, find it here and go straight to it.", "Las prácticas de los ocho temas, reunidas en un solo sitio. Cada enlace abre directamente la práctica que necesita, no la página entera. Si la evaluación final señaló un tema, búsquelo aquí y vaya al grano.")}</p>
      <div class="panel"><div class="campo"><label for="ix-q">{t("Search by word", "Buscar por palabra")}</label><input type="search" id="ix-q" class="ancho" autocomplete="off" placeholder="{t("for example: shadow, outlier, cylinder", "por ejemplo: sombra, atípico, cilindro")}"></div>
        <p class="nota" id="ix-cuenta" aria-live="polite"></p></div>
      <p class="caja-aviso visible" id="ix-nada" hidden>{t("No practice has that word. Try a shorter word or clear the search.", "No hay ninguna práctica con esa palabra. Pruebe con un término más corto o borre la búsqueda.")}</p>
      <div id="ix-lista">
{lista}
      </div>''')]
    return B.pagina_practica(n, 8, t(*TEMA), t("Level 3 review", "Repaso del Nivel 3"),
        t("A mixed practice of the eight topics and an index of every practice of the level. The exercises change every time.", "Una práctica mezclada de los ocho temas y un índice de todas las prácticas del nivel. Los ejercicios cambian cada vez."),
        mods, js, estilo=ESTILO8, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Proyecto final integrador y estrategias para el GED")
