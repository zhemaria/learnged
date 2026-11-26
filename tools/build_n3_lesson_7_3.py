"""Level 3 · Lesson 7.3 · Histograms: make, read, and compare — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_7-3.html and algebra/n3-l7-3.html (GEDparaHispanos).
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n3
from build_n3_lesson_7_1 import ESTILO, SCRIPTS, TEMA

B.NIVEL = 3
N = "7-3"
TIT = ("Histograms: make, read, and compare", "Histogramas: construir, interpretar y comparar distribuciones")
ESTILO_H = ESTILO + """
  #hc-tabla{border-collapse:collapse;margin:10px 0;font-size:17px;}
  #hc-tabla caption{text-align:left;font-size:14px;color:var(--gris);padding-bottom:6px;}
  #hc-tabla th,#hc-tabla td{border:1px solid #c8c8c8;padding:6px 12px;text-align:center;}
  #hc-tabla th{background:var(--tema-bg);color:var(--tema-d);}
  #hc-tabla input{width:64px;font-size:17px;padding:4px 6px;text-align:center;}
  #hc-tabla td.bien{background:#e8f5e9;} #hc-tabla td.mal{background:#ffebee;}"""

def figura_hist():
    f = [2, 5, 8, 4, 1]
    x0, yb, w, k = 70, 200, 80, 20
    s = ""
    for v in range(0, 9, 2):
        s += f'<line x1="{x0}" y1="{yb - v * k}" x2="{x0 + 5 * w}" y2="{yb - v * k}" stroke="#e0e0e0"/><text x="{x0 - 8}" y="{yb - v * k + 5}" font-size="14" text-anchor="end" fill="#424242">{v}</text>'
    for i, v in enumerate(f):
        s += f'<rect x="{x0 + i * w}" y="{yb - v * k}" width="{w}" height="{v * k}" fill="#90a4ae" stroke="#37474f" stroke-width="2"/><text x="{x0 + i * w + w / 2}" y="{yb - v * k - 6}" font-size="14" font-weight="700" text-anchor="middle" fill="#222">{v}</text>'
    for i, v in enumerate(range(0, 30, 5)):
        s += f'<text x="{x0 + i * w}" y="{yb + 18}" font-size="14" text-anchor="middle" fill="#222">{v}</text>'
    s += (f'<line x1="{x0}" y1="{yb}" x2="{x0 + 5 * w}" y2="{yb}" stroke="#424242" stroke-width="2"/><line x1="{x0}" y1="{yb}" x2="{x0}" y2="20" stroke="#424242" stroke-width="2"/>'
          f'<text x="22" y="110" font-size="14" font-weight="700" fill="#424242" text-anchor="middle" transform="rotate(-90 22 110)">{t("Frequency", "Frecuencia")}</text>'
          f'<text x="{x0 + 2.5 * w}" y="{yb + 40}" font-size="14" font-weight="700" fill="#424242" text-anchor="middle">{t("Intervals of the data", "Intervalos de datos")}</text>')
    return B.svg("0 0 490 250", t("A histogram with five bars that touch, for the intervals 0–5, 5–10, 10–15, 15–20, and 20–25. Their frequencies are 2, 5, 8, 4, and 1.",
                                  "Un histograma con cinco barras pegadas, para los intervalos 0–5, 5–10, 10–15, 15–20 y 20–25. Sus frecuencias son 2, 5, 8, 4 y 1."), s, 490)

def leccion():
    n = N
    s1 = f'''<p>{t("The box plot in Lesson 7.2 summarizes data with five numbers. The histogram gives another view: it shows how many data values fall in each interval, which reveals the whole shape of the distribution. Together, the two graphs give a richer picture of the same data set.", "El diagrama de caja de la Lección 7.2 resume los datos en cinco números. El histograma ofrece otra mirada: muestra cuántos datos caen en cada intervalo, revelando la forma completa de la distribución. Juntas, ambas gráficas dan una imagen más rica de un mismo conjunto de datos.")}</p>
<p>{t("A <strong>histogram</strong> groups the data into intervals and draws one bar for each, whose height is the <strong>frequency</strong> (how many data values fall in that interval). Unlike a bar graph, its bars touch, because they show continuous data.", "Un <strong>histograma</strong> agrupa los datos en intervalos y dibuja una barra por cada uno, cuya altura es la <strong>frecuencia</strong> (cuántos datos caen en ese intervalo). A diferencia de la gráfica de barras, sus barras están pegadas, porque representan datos continuos.")}</p>
{figura_hist()}
{caja("ojo", t("A histogram is not a bar graph", "Histograma no es gráfica de barras"), t("<p>In a bar graph, the columns stand for separate categories and have spaces between them. In a histogram, the bars stand for intervals of continuous data and touch each other. That is the key difference when you need to tell them apart.</p>", "<p>En una gráfica de barras las columnas representan categorías separadas (y van con espacios), mientras que en el histograma las barras representan intervalos de un dato continuo y van pegadas. Es la diferencia clave a la hora de identificar cada gráfica.</p>"))}'''

    s2 = f'''<p>{t("Start from a frequency table: each row gives an interval and how many data values fall in it. The height of each bar is that frequency.", "Se parte de una tabla de frecuencias: cada fila indica un intervalo y cuántos datos caen en él. La altura de cada barra es esa frecuencia.")}</p>
{ejemplo(t("Example 1: a table shows that the interval 10–15 has a frequency of 8. How tall is its bar?", "Ejemplo 1: una tabla indica que el intervalo 10–15 tiene una frecuencia de 8. ¿Qué altura tiene su barra?"),
  [("1", t("The height of the bar equals the frequency of the interval.", "La altura de la barra es igual a la frecuencia del intervalo."), ""),
   ("✓", t("Answer.", "Respuesta."), t("The bar for 10–15 reaches a height of <strong>8</strong>.", "La barra del intervalo 10–15 llega hasta la altura <strong>8</strong>."))])}
{caja("tip", t("Intervals of the same width", "Intervalos del mismo ancho"), t("<p>So that the histogram is easy to read, all the intervals should have the same width (for example, every 5 years). Then comparing the heights is the same as comparing the frequencies. Each interval includes its left end but not its right end: 10–15 includes 10 but not 15.</p>", "<p>Para que el histograma sea fácil de leer, todos los intervalos deben tener el mismo ancho (por ejemplo, de 5 en 5 años). Así, comparar las alturas equivale directamente a comparar las frecuencias. Cada intervalo incluye su extremo izquierdo, pero no el derecho: 10–15 incluye el 10 y no el 15.</p>"))}
{practica("p1", t("Practice 1 — The bars", "Práctica 1 — Las barras"), t("In a histogram, the bars are…", "En un histograma, las barras están…"), [("a", t("separated", "separadas")), ("b", t("in a circle", "en círculo")), ("c", t("touching each other", "pegadas (contiguas)"))])}
{practica("p2", t("Practice 2 — The vertical axis", "Práctica 2 — El eje vertical"), t("The vertical axis of a histogram shows…", "El eje vertical de un histograma muestra…"), [("a", t("the name of each category", "el nombre de cada categoría")), ("b", t("the frequency", "la frecuencia")), ("c", t("the total", "el total"))])}
{practica("p3", t("Practice 3 — The height of a bar", "Práctica 3 — La altura de una barra"), t("An interval with a frequency of 6 has a bar with a height of…", "Un intervalo con frecuencia 6 tiene una barra de altura…"), [("a", "6"), ("b", "3"), ("c", "12")])}
{enlace(n, t("build", "construir"), t("making a histogram", "construir un histograma"), t("Count the data in each interval and draw the bars.", "Organice los datos en intervalos y dibuje las barras."))}'''

    formas = [(t("Symmetric", "Simétrica"), t("The same shape on both sides of the center.", "La misma forma a ambos lados del centro.")),
              (t("Skewed right", "Sesgada a la derecha"), t("A long tail toward the high values.", "Una cola larga hacia los valores altos.")),
              (t("Skewed left", "Sesgada a la izquierda"), t("A long tail toward the low values.", "Una cola larga hacia los valores bajos.")),
              (t("Unimodal", "Unimodal"), t("One peak (one bar that is highest).", "Un solo pico (una sola barra más alta).")),
              (t("Bimodal", "Bimodal"), t("Two separate peaks.", "Dos picos separados.")),
              (t("Uniform", "Uniforme"), t("All the bars are about the same height; there is no clear peak.", "Todas las barras tienen más o menos la misma altura; no hay un pico claro."))]
    s3 = f'''<p>{t("The great advantage of a histogram is that it shows the shape of the data at a glance. The shape is described with precise words:", "La gran ventaja del histograma es que muestra la forma de los datos de un solo vistazo. Se describe con un vocabulario preciso:")}</p>
{tabla(t("Shapes of a distribution", "Formas de una distribución"), t("Shapes of a distribution and what they look like", "Formas de una distribución y su descripción"), [t("Shape", "Forma"), t("What it looks like", "Descripción")], [list(f) for f in formas])}
{ejemplo(t("Example 2: a histogram rises to a peak in the center and falls about the same way on both sides. What shape does it have?", "Ejemplo 2: un histograma sube hasta un pico en el centro y baja a ambos lados de forma parecida. ¿Qué forma tiene?"),
  [("1", t("It has one peak.", "Tiene un solo pico."), t("So it is unimodal.", "Así que es unimodal.")),
   ("2", t("The two sides are alike.", "Los lados son parecidos."), t("So it is about symmetric.", "Así que es aproximadamente simétrica.")),
   ("✓", t("Answer.", "Respuesta."), t("It is a <strong>unimodal</strong>, about <strong>symmetric</strong> distribution.", "Es una distribución <strong>unimodal</strong> y aproximadamente <strong>simétrica</strong>."))])}
{caja("ojo", t("Skew is named by the tail", "El sesgo se nombra por la cola"), t("<p>Skew is named by the tail, not by the peak: “skewed right” has its peak on the left and a long tail toward the high values.</p>", "<p>El sesgo se nombra por la cola, no por el pico: «sesgada a la derecha» tiene el pico a la izquierda y una cola larga hacia los valores altos.</p>"))}
{enlace(n, t("shape", "forma"), t("the shape of a distribution", "la forma de la distribución"), t("Recognize symmetric, skewed, and bimodal distributions.", "Reconozca distribuciones simétricas, sesgadas y bimodales."))}'''

    preguntas = [(t("What is the detailed shape of the data?", "¿Cuál es la forma detallada de los datos?"), t("Histogram", "Histograma")),
                 (t("What are the quartiles and the outliers?", "¿Cuáles son los cuartiles y los valores atípicos?"), t("Box plot", "Diagrama de caja")),
                 (t("Are there one or two peaks?", "¿Hay uno o dos picos?"), t("Histogram", "Histograma")),
                 (t("How spread out is the middle half?", "¿Qué tan dispersa está la mitad central?"), t("Box plot", "Diagrama de caja"))]
    s4 = f'''<p>{t("The two graphs describe the same data from different angles. It helps to know when to use each one.", "Las dos gráficas describen el mismo conjunto desde ángulos distintos. Conviene saber cuándo usar cada una.")}</p>
{tabla(t("Which graph shows it better", "Qué muestra mejor cada gráfica"), t("What each graph shows better", "Qué muestra mejor cada representación gráfica"), [t("Question", "Pregunta"), t("Better display", "Mejor representación")], [list(p) for p in preguntas])}
{practica("p4", t("Practice 4 — A long tail", "Práctica 4 — Una cola larga"), t("A histogram with a long tail toward the high values is…", "Un histograma con una cola larga hacia los valores altos está…"), [("a", t("skewed left", "sesgado a la izquierda")), ("b", t("symmetric", "simétrico")), ("c", t("skewed right", "sesgado a la derecha"))])}
{practica("p5", t("Practice 5 — Two peaks", "Práctica 5 — Dos picos"), t("A distribution with two peaks is…", "Una distribución con dos picos es…"), [("a", t("bimodal", "bimodal")), ("b", t("unimodal", "unimodal")), ("c", t("uniform", "uniforme"))])}
{practica("p6", t("Practice 6 — The quartiles", "Práctica 6 — Los cuartiles"), t("Which graph shows the quartiles better?", "¿Qué gráfica muestra mejor los cuartiles?"), [("a", t("The histogram", "El histograma")), ("b", t("The box plot", "El diagrama de caja")), ("c", t("The bar graph", "La gráfica de barras"))])}
{enlace(n, t("compare", "comparar"), t("histogram versus box plot", "histograma frente a diagrama de caja"), t("See what each graph of the same data set tells you.", "Vea qué información ofrece cada gráfica del mismo conjunto de datos."))}'''

    s5 = f'''<p>{t("There is no “best” graph in general: it depends on the question. To see the shape and the peaks, use a histogram; to compare spread and find outliers between groups, use box plots.", "No hay una gráfica «mejor» en abstracto: depende de la pregunta. Para ver la forma y los picos, conviene el histograma; para comparar la dispersión y detectar valores atípicos entre grupos, el diagrama de caja.")}</p>
{ejemplo(t("Example 3: choosing by the question. You want to know whether the ages in a class split into two very different age groups. Which graph should you use?", "Ejemplo 3 · Elegir según la pregunta. Se quiere saber si las edades de un salón se reparten en dos grupos de edad bien distintos. ¿Qué gráfica conviene?"),
  [("1", t("The question is about shape.", "La pregunta es sobre la forma."), t("Are there one or two peaks?", "¿Hay uno o dos picos?")),
   ("2", t("Compare the graphs.", "Se comparan las gráficas."), t("The histogram shows the peaks directly; the box plot does not.", "El histograma muestra los picos directamente; el diagrama de caja no.")),
   ("✓", t("Answer.", "Respuesta."), t("Use the <strong>histogram</strong>, because it shows whether the distribution is bimodal.", "Conviene el <strong>histograma</strong>, porque revela si la distribución es bimodal."))])}
{caja("tip", t("And for categories?", "¿Y para categorías?"), t("<p>When the data are separate categories (countries, colors, days of the week), neither one fits: use a bar graph.</p>", "<p>Cuando los datos son categorías separadas (países, colores, días de la semana), no sirve ninguna de las dos: conviene la gráfica de barras.</p>"))}
{enlace(n, t("choose", "elegir"), t("choosing the most useful display", "elegir la representación más informativa"), t("Decide which graph fits the question.", "Decida qué gráfica conviene según la pregunta."))}'''

    secciones = [("s-" + t("what-is", "que-es"), t("What is a histogram?", "¿Qué es un histograma?"), s1),
                 ("s-" + t("build", "construir"), t("Making a histogram", "Construir un histograma"), s2),
                 ("s-" + t("shape", "forma"), t("The shape of a distribution", "La forma de la distribución"), s3),
                 ("s-" + t("compare", "comparar"), t("Histogram versus box plot", "Comparar histograma y diagrama de caja"), s4),
                 ("s-" + t("choose", "elegir"), t("Choosing the most useful display", "Elegir la representación más informativa"), s5)]

    lesson = {"next": t("Lesson 8.1", "Lección 8.1"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Separate bars belong to a bar graph of categories.", "Las barras separadas son de la gráfica de barras de categorías."), "b": t("Pieces in a circle belong to a circle graph.", "Las porciones en círculo son de la gráfica circular.")}, "right": t("The intervals are continuous, so the bars touch.", "Los intervalos son continuos, así que las barras van pegadas."), "solution": t("They touch.", "Pegadas.")},
      "p2": {"ok": "b", "hints": {"a": t("A histogram has intervals, not categories, and they go on the horizontal axis.", "Un histograma tiene intervalos, no categorías, y van en el eje horizontal."), "c": t("The vertical axis shows how many values fall in each interval.", "El eje vertical muestra cuántos datos caen en cada intervalo.")}, "right": t("The height of each bar is its frequency.", "La altura de cada barra es su frecuencia."), "solution": t("The frequency.", "La frecuencia.")},
      "p3": {"ok": "a", "hints": {"b": t("Do not divide: the height is the frequency itself.", "No se divide: la altura es la frecuencia misma."), "c": t("Do not double it: the height is the frequency itself.", "No se duplica: la altura es la frecuencia misma.")}, "right": t("The height equals the frequency: 6.", "La altura es igual a la frecuencia: 6."), "solution": "6."},
      "p4": {"ok": "c", "hints": {"a": t("Skew is named by the tail. Where does the tail go?", "El sesgo se nombra por la cola. ¿Hacia dónde va la cola?"), "b": t("A long tail on one side means it is not symmetric.", "Una cola larga hacia un lado significa que no es simétrico.")}, "right": t("The tail goes toward the high values (to the right).", "La cola va hacia los valores altos (a la derecha)."), "solution": t("Skewed right.", "Sesgado a la derecha.")},
      "p5": {"ok": "a", "hints": {"b": t("Uni- means one. Two peaks is bi-.", "Uni- significa uno. Dos picos es bi-."), "c": t("Uniform means there is no clear peak.", "Uniforme significa que no hay un pico claro.")}, "right": t("Bi- means two: two peaks.", "Bi- significa dos: dos picos."), "solution": t("Bimodal.", "Bimodal.")},
      "p6": {"ok": "b", "hints": {"a": t("The histogram shows the shape, not the quartiles.", "El histograma muestra la forma, no los cuartiles."), "c": t("A bar graph is for categories.", "La gráfica de barras es para categorías.")}, "right": t("The box plot draws Q1, the median, and Q3.", "El diagrama de caja dibuja Q1, la mediana y Q3."), "solution": t("The box plot.", "El diagrama de caja.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Separate bars belong to a bar graph.", "Las barras separadas son de la gráfica de barras."), "c": t("Circles belong to a circle graph.", "Los círculos son de la gráfica circular."), "d": t("The heights change with the frequencies.", "Las alturas cambian con las frecuencias.")}, "solution": t("They touch.", "Contiguas.")},
      "B": {"ok": "a", "hints": {"b": t("A histogram has intervals, not categories.", "Un histograma tiene intervalos, no categorías."), "c": t("A histogram does not show the average.", "El histograma no muestra el promedio."), "d": t("The IQR belongs to the box plot.", "El IQR es del diagrama de caja.")}, "solution": t("The frequency.", "La frecuencia.")},
      "C": {"ok": "c", "hints": {"a": t("15 is the right end of the interval, not its frequency.", "15 es el extremo derecho del intervalo, no su frecuencia."), "b": t("10 is the left end of the interval.", "10 es el extremo izquierdo del intervalo."), "d": t("5 is the width of the interval.", "5 es el ancho del intervalo.")}, "solution": "8."},
      "D": {"ok": "d", "hints": {"a": t("A skewed distribution has a long tail on one side.", "Una distribución sesgada tiene una cola larga de un lado."), "b": t("Bimodal means two peaks.", "Bimodal significa dos picos."), "c": t("Uniform means no clear peak.", "Uniforme significa sin un pico claro.")}, "solution": t("Symmetric.", "Simétrica.")},
      "E": {"ok": "b", "hints": {"a": t("Skew is named by the tail, and here the tail goes to the high values.", "El sesgo se nombra por la cola, y aquí la cola va a los valores altos."), "c": t("A long tail on one side means it is not symmetric.", "Una cola larga hacia un lado significa que no es simétrica."), "d": t("It does have a peak, on the left.", "Sí tiene pico, a la izquierda.")}, "solution": t("Skewed right.", "Sesgada a la derecha.")},
      "F": {"ok": "c", "hints": {"a": t("Uni- means one peak.", "Uni- significa un pico."), "b": t("Symmetric is about the two sides, not the number of peaks.", "Simétrica habla de los dos lados, no del número de picos."), "d": t("Uniform means no clear peak.", "Uniforme significa sin un pico claro.")}, "solution": t("Bimodal.", "Bimodal.")},
      "G": {"ok": "a", "hints": {"b": t("The box plot shows the quartiles, not the detailed shape.", "El diagrama de caja muestra los cuartiles, no la forma detallada."), "c": t("One of them does show the shape.", "Una de ellas sí muestra la forma."), "d": t("A box plot cannot show peaks.", "El diagrama de caja no puede mostrar los picos.")}, "solution": t("The histogram.", "El histograma.")},
      "H": {"ok": "c", "hints": {"a": t("The histogram shows the shape.", "El histograma muestra la forma."), "b": t("A circle graph shows parts of a whole.", "La gráfica circular muestra partes de un todo."), "d": t("One of them does show them.", "Una de ellas sí los muestra.")}, "solution": t("The box plot.", "El diagrama de caja.")}
     }}

    quiz = [
     ("A", t("In a histogram, the bars are…", "En un histograma, las barras son…"), [("a", t("separated", "separadas")), ("b", t("touching (next to each other)", "contiguas (se tocan)")), ("c", t("circular", "circulares")), ("d", t("always the same", "siempre iguales"))]),
     ("B", t("The vertical axis of a histogram shows…", "El eje vertical de un histograma muestra…"), [("a", t("the frequency", "la frecuencia")), ("b", t("the name of each category", "el nombre de cada categoría")), ("c", t("the average", "el promedio")), ("d", t("the IQR", "el IQR"))]),
     ("C", t("If the interval 10–15 has a frequency of 8, its bar has a height of…", "Si el intervalo 10–15 tiene frecuencia 8, su barra tiene altura…"), [("a", "15"), ("b", "10"), ("c", "8"), ("d", "5")]),
     ("D", t("A distribution with the same shape on both sides of the center is…", "Una distribución con la misma forma a ambos lados del centro es…"), [("a", t("skewed right", "sesgada a la derecha")), ("b", t("bimodal", "bimodal")), ("c", t("uniform", "uniforme")), ("d", t("symmetric", "simétrica"))]),
     ("E", t("A distribution with a long tail toward the high values is…", "Una distribución con una cola larga hacia los valores altos es…"), [("a", t("skewed left", "sesgada a la izquierda")), ("b", t("skewed right", "sesgada a la derecha")), ("c", t("symmetric", "simétrica")), ("d", t("without a peak", "sin pico"))]),
     ("F", t("A distribution with two peaks is…", "Una distribución con dos picos es…"), [("a", t("unimodal", "unimodal")), ("b", t("symmetric", "simétrica")), ("c", t("bimodal", "bimodal")), ("d", t("uniform", "uniforme"))]),
     ("G", t("Which graph best shows the detailed shape of a distribution?", "¿Qué gráfica muestra mejor la forma detallada de la distribución?"), [("a", t("The histogram", "El histograma")), ("b", t("The box plot", "El diagrama de caja")), ("c", t("Neither", "Ninguna")), ("d", t("Both equally", "Las dos por igual"))]),
     ("H", t("Which graph best shows the quartiles and the outliers?", "¿Qué gráfica muestra mejor los cuartiles y los valores atípicos?"), [("a", t("The histogram", "El histograma")), ("b", t("The circle graph", "La gráfica circular")), ("c", t("The box plot", "El diagrama de caja")), ("d", t("Neither", "Ninguna"))])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Make a histogram from a frequency table, describe the shape of a distribution, and choose between a histogram and a box plot.", "Construya un histograma a partir de una tabla de frecuencias, describa la forma de una distribución y elija entre un histograma y un diagrama de caja."),
        ("📊", t("The shape of the data", "La forma de los datos")),
        [t("<strong>Tell</strong> a histogram from a bar graph (bars that touch = continuous data).", "<strong>Distinguir</strong> un histograma de una gráfica de barras (barras contiguas = datos continuos)."),
         t("<strong>Make</strong> a histogram from a frequency table.", "<strong>Construir</strong> un histograma a partir de una tabla de frecuencias."),
         t("<strong>Describe</strong> the shape of a distribution (symmetric, skewed, unimodal, bimodal).", "<strong>Describir</strong> la forma de la distribución (simétrica, sesgada, unimodal, bimodal)."),
         t("<strong>Compare</strong> a histogram with a box plot of the same data.", "<strong>Comparar</strong> un histograma con un diagrama de caja del mismo conjunto."),
         t("<strong>Choose</strong> the most useful graph for each situation.", "<strong>Elegir</strong> la representación gráfica más informativa para cada contexto.")],
        secciones,
        (t("Take a set of 20 data values (for example, the ages of 20 people). Make a frequency table with intervals of the same width, draw the histogram, and describe its shape in one sentence. Then find the five key values, draw the box plot of the same data, and write what each graph shows that the other does not.",
           "Tome un conjunto de 20 datos (por ejemplo, las edades de 20 personas). Haga una tabla de frecuencias con intervalos del mismo ancho, dibuje el histograma y describa su forma en una oración. Después halle los cinco valores clave, dibuje el diagrama de caja de los mismos datos y escriba qué muestra cada gráfica que la otra no muestra."),
         t("Look for a histogram in a newspaper, a website, or a report from your job (for example, ages of customers or waiting times). What shape does it have? What question does it answer well? Would a box plot answer it better or worse?",
           "Busque un histograma en un periódico, una página web o un informe de su trabajo (por ejemplo, edades de clientes o tiempos de espera). ¿Qué forma tiene? ¿Qué pregunta responde bien? ¿Un diagrama de caja la respondería mejor o peor?")),
        quiz,
        t("Self-check checklist for histograms", "Lista de autoevaluación de histogramas"),
        t("Self-check checklist: skills for making, reading, and comparing histograms", "Lista de autoevaluación: destrezas para construir, interpretar y comparar histogramas"),
        [(t("Making the histogram", "Construir el histograma"), t("I make the histogram with the right intervals and frequencies, with equal widths and bars that touch.", "Construyo el histograma con los intervalos y frecuencias correctos, de igual ancho y con barras contiguas."), t("I make it with mistakes in the intervals or frequencies.", "Lo construyo con errores de intervalo o frecuencia."), t("I do not connect the frequency with the height of the bar.", "No relaciono la frecuencia con la altura de la barra.")),
         (t("Describing the shape", "Describir la forma"), t("I describe the shape with the right words (symmetry, skew, number of peaks).", "Describo la forma con la terminología correcta (simetría, sesgo, número de picos)."), t("I describe the shape with loose words.", "Describo la forma con terminología imprecisa."), t("I do not describe the shape.", "No describo la forma de la distribución.")),
         (t("Comparing distributions", "Comparar distribuciones"), t("I compare two distributions with at least two features, using the histogram and the box plot.", "Comparo dos distribuciones con al menos dos características, usando el histograma y el diagrama de caja."), t("I compare with only one feature.", "Comparo usando una sola característica."), t("I do not compare the two displays.", "No comparo las dos representaciones.")),
         (t("Choosing the display", "Elegir la representación"), t("I choose the most useful graph and explain why.", "Elijo la representación más informativa y explico por qué."), t("I choose without explaining.", "Elijo sin justificar."), t("I do not choose by the situation.", "No elijo según el contexto."))],
        t("<p>This lesson closes Topic 7. You can now find the volume of solids and analyze data with two tools that complete each other: the box plot (five values, IQR, outliers) and the histogram (the shape of the distribution). You also know how to choose the most useful graph for each question.</p>\n<p>Topic 8 closes Level 3. It opens with <strong>Lesson 8.1 · The counting principle, permutations, and combinations</strong>, where you will learn to count the ways events can happen, the basis of probability. The topic ends with a final project and preparation for the GED Mathematical Reasoning test.</p>",
          "<p>Con esta lección se cierra el Tema 7. Ya se calcula el volumen de sólidos y se analizan datos con dos herramientas complementarias: el diagrama de caja (cinco valores, IQR, atípicos) y el histograma (forma de la distribución). También se sabe elegir la gráfica más informativa según la pregunta.</p>\n<p>El Tema 8 cierra el Nivel 3. Abrirá con la <strong>Lección 8.1 · Principio fundamental del conteo, permutaciones y combinaciones</strong>, donde se aprenderá a contar de cuántas formas pueden ocurrir los eventos, base de la probabilidad. El tema culmina con un proyecto final integrador y la preparación para el examen GED de Razonamiento Matemático.</p>"),
        ("8-1", ("", t("Lesson 8.1 · The counting principle, permutations, and combinations", "Lección 8.1 · Principio fundamental del conteo, permutaciones y combinaciones"))),
        [(t("histogram", "histograma"), t("A graph of intervals of continuous data, with bars that touch; each height is a frequency.", "Una gráfica de intervalos de datos continuos, con barras pegadas; cada altura es una frecuencia.")),
         (t("frequency", "frecuencia"), t("How many data values fall in an interval.", "Cuántos datos caen en un intervalo.")),
         (t("symmetric", "simétrica"), t("A distribution with the same shape on both sides of its center.", "Una distribución con la misma forma a ambos lados de su centro.")),
         (t("skewed", "sesgada"), t("A distribution with a long tail on one side; it is named by the side of the tail.", "Una distribución con una cola larga de un lado; se nombra por el lado de la cola.")),
         (t("bimodal", "bimodal"), t("A distribution with two peaks.", "Una distribución con dos picos."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* MODULE 1 · Make a histogram by counting */
var CONTEXTOS = [
  {t: T("Ages of 20 students in an evening class (years)", "Edades de 20 estudiantes de una clase nocturna (años)"), lo: 18, hi: 59, eje: T("Age (years)", "Edad (años)")},
  {t: T("Minutes it takes 20 people to get to work", "Minutos que tardan 20 personas en llegar al trabajo"), lo: 5, hi: 54, eje: T("Minutes", "Minutos")},
  {t: T("Scores on 20 tests (out of 100)", "Calificaciones de 20 exámenes (sobre 100)"), lo: 40, hi: 99, eje: T("Score", "Calificación")}];
var HC = {d: [], ctx: null, clases: []};
function nuevoHC(){
  HC.ctx = elige(CONTEXTOS); HC.d = datosAzar(20, HC.ctx.lo, HC.ctx.hi);
  $("hc-titulo").textContent = HC.ctx.t + ":";
  $("hc-datos").innerHTML = HC.d.map(function(v){ return '<span class="dato">' + v + "</span>"; }).join("");
  $("hc-voz").textContent = T("Data: ", "Datos: ") + HC.d.join(", ") + ".";
  armaTabla();
}
function armaTabla(){
  var w = +$("hc-ancho").value, a0 = Math.floor(Math.min.apply(null, HC.d) / w) * w, b1 = Math.max.apply(null, HC.d), clases = [];
  for (var a = a0; a <= b1; a += w) clases.push({a: a, b: a + w, f: HC.d.filter(function(v){ return v >= a && v < a + w; }).length});
  HC.clases = clases;
  var h = "<caption>" + T("Frequency table: type how many values are in each interval", "Tabla de frecuencias: escriba cuántos datos hay en cada intervalo") + '</caption><thead><tr><th scope="col">' + T("Interval", "Intervalo") + '</th><th scope="col">' + T("Frequency", "Frecuencia") + "</th></tr></thead><tbody>";
  clases.forEach(function(c, i){ h += "<tr><td>" + c.a + "–" + c.b + '</td><td id="hc-c' + i + '"><label class="sr-only" for="hc-f' + i + '">' + T("Frequency of the interval from " + c.a + " to " + c.b, "Frecuencia del intervalo de " + c.a + " a " + c.b) + '</label><input type="text" inputmode="numeric" autocomplete="off" id="hc-f' + i + '"></td></tr>'; });
  $("hc-tabla").innerHTML = h + "</tbody>";
  clases.forEach(function(c, i){ $("hc-f" + i).addEventListener("input", dibujaHC); });
  $("hc-fb").className = "fb"; $("hc-fb").innerHTML = ""; HC.intentos = 0;
  dibujaHC();
}
function dibujaHC(){
  var cl = HC.clases.map(function(c, i){ var v = leeEntero($("hc-f" + i).value); return {a: c.a, b: c.b, f: v === null ? 0 : Math.max(0, v)}; });
  $("hc-svg").innerHTML = histSVG(cl, T("Histogram with your frequencies: ", "Histograma con sus frecuencias: ") + cl.map(function(c){ return c.a + T(" to ", " a ") + c.b + ": " + c.f; }).join("; "), {eje: HC.ctx.eje});
}
function compruebaHC(){
  var bien = 0, fb = $("hc-fb");
  HC.clases.forEach(function(c, i){ var v = leeEntero($("hc-f" + i).value), ok = v === c.f; $("hc-c" + i).className = ok ? "bien" : "mal"; if (ok) bien++; });
  var total = HC.clases.reduce(function(s, c, i){ var v = leeEntero($("hc-f" + i).value); return s + (v || 0); }, 0), faltan = HC.clases.length - bien;
  if (!faltan){ fb.className = "fb bien"; fb.innerHTML = TX.bien + T("All the frequencies are right. They add up to " + total + ", the number of data values.", "Todas las frecuencias están bien. Suman " + total + ", el total de datos."); return; }
  HC.intentos = (HC.intentos || 0) + 1;
  var msg = T(faltan + (faltan === 1 ? " interval needs" : " intervals need") + " checking (in red). Your frequencies add up to " + total + " and should add up to 20. Remember that the right end is not included.", "Hay " + faltan + (faltan === 1 ? " intervalo" : " intervalos") + " por revisar (en rojo). Sus frecuencias suman " + total + " y deben sumar 20. Recuerde que el extremo derecho no se incluye.");
  if (HC.intentos >= 2){ fb.className = "fb mal"; fb.innerHTML = msg + " " + T("Press <strong>Count for me</strong> to see the right frequencies.", "Pulse <strong>Contar por mí</strong> para ver las frecuencias correctas."); }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas; }
}
function contarHC(){ HC.clases.forEach(function(c, i){ $("hc-f" + i).value = c.f; $("hc-c" + i).className = ""; }); dibujaHC(); $("hc-fb").className = "fb bien"; $("hc-fb").innerHTML = T("Frequencies counted. Change the width of the intervals to see how the histogram changes.", "Frecuencias contadas. Cambie el ancho de los intervalos para ver cómo cambia el histograma."); }

/* MODULE 2 · Shapes */
var FORMAS = {
  sim: {f: [1, 3, 6, 9, 9, 6, 3, 1], nombre: T("Symmetric", "Simétrica"), d: T("The same shape on both sides of the center, with one peak. The mean and the median are in almost the same place.", "La misma forma a ambos lados del centro, con un solo pico. La media y la mediana quedan casi en el mismo lugar.")},
  der: {f: [3, 9, 10, 7, 4, 2, 1, 1], nombre: T("Skewed right", "Sesgada a la derecha"), d: T("The peak is on the left and the long tail goes toward the high values. The few large values pull the mean to the right: the mean is greater than the median.", "El pico está a la izquierda y la cola larga va hacia los valores altos. Los pocos valores grandes arrastran la media hacia la derecha: media mayor que mediana.")},
  izq: {f: [1, 1, 2, 4, 7, 10, 9, 3], nombre: T("Skewed left", "Sesgada a la izquierda"), d: T("The peak is on the right and the long tail goes toward the low values. The mean is below the median.", "El pico está a la derecha y la cola larga va hacia los valores bajos. La media queda por debajo de la mediana.")},
  uni: {f: [5, 6, 5, 5, 6, 5, 5, 6], nombre: T("Uniform", "Uniforme"), d: T("All the bars are about the same height: there is no clear peak.", "Todas las barras tienen más o menos la misma altura: no hay un pico claro.")},
  bim: {f: [2, 7, 9, 4, 3, 8, 9, 3], nombre: T("Bimodal", "Bimodal"), d: T("It has two separate peaks: this often means there are two different groups in the data.", "Tiene dos picos separados: suele indicar que en los datos hay dos grupos distintos.")}};
function clasesDe(f, a0, w){ return f.map(function(x, i){ return {a: a0 + i * w, b: a0 + (i + 1) * w, f: x}; }); }
function mediaMediana(cl){
  var n = cl.reduce(function(s, c){ return s + c.f; }, 0), suma = cl.reduce(function(s, c){ return s + c.f * (c.a + c.b) / 2; }, 0), acum = 0, med = null;
  for (var i = 0; i < cl.length; i++){ if (acum + cl[i].f >= n / 2){ med = cl[i].a + (n / 2 - acum) / cl[i].f * (cl[i].b - cl[i].a); break; } acum += cl[i].f; }
  return {media: suma / n, med: med};
}
function pintaFO(){
  var k = $("fo-sel").value, F = FORMAS[k], cl = clasesDe(F.f, 0, 10), mm = mediaMediana(cl);
  $("fo-svg").innerHTML = histSVG(cl, T("Histogram with a " + F.nombre.toLowerCase() + " shape. Frequencies: ", "Histograma de forma " + F.nombre.toLowerCase() + ". Frecuencias: ") + F.f.join(", "));
  $("fo-salida").innerHTML = '<div class="linea"><strong>' + F.nombre + ".</strong> " + F.d + "</div>" +
    '<div class="linea">' + T("With these data, the mean is about " + aprox(mm.media, 1) + " and the median about " + aprox(mm.med, 1) + ".", "Con estos datos, la media es aproximadamente " + aprox(mm.media, 1) + " y la mediana " + aprox(mm.med, 1) + ".") + "</div>";
}
function ruido(f){ return f.map(function(x){ return Math.max(0, x + elige([-1, 0, 0, 1])); }); }
function genForma(){
  var k = elige(["sim", "der", "izq", "uni", "bim"]), f = ruido(FORMAS[k].f);
  if (k === "sim"){ f = f.slice(0, 4); f = f.concat(f.slice().reverse()); }
  var o = ["sim", "der", "izq", "uni", "bim"].map(function(x){ return {html: FORMAS[x].nombre, clave: x}; }), pc = {};
  if (k === "izq") pc.der = T("Look at where the long tail goes: here it goes toward the low values (left).", "Fíjese hacia dónde va la cola larga: aquí va hacia los valores bajos (izquierda).");
  if (k === "der") pc.izq = T("Look at where the long tail goes: here it goes toward the high values (right).", "Fíjese hacia dónde va la cola larga: aquí va hacia los valores altos (derecha).");
  return {enun: T("What shape does this distribution have?", "¿Qué forma tiene esta distribución?") + histSVG(clasesDe(f, 0, 10), T("Histogram to classify. Frequencies: ", "Histograma para clasificar. Frecuencias: ") + f.join(", ")), opciones: o, correcta: k, porClave: pc,
    pista: T("Count the peaks, and look at whether one side has a long tail.", "Cuente los picos y fíjese si un lado tiene una cola larga."), bien: FORMAS[k].d, mal: T("It is ", "Es ") + FORMAS[k].nombre.toLowerCase() + ". " + FORMAS[k].d};
}

/* MODULE 3 · Histogram and box plot of the same data */
function datosDeForma(f, a0, w){ var d = []; f.forEach(function(x, i){ for (var j = 0; j < x; j++) d.push(a0 + i * w + aleatorio(0, w - 1)); }); return d; }
var CM_DATOS = {};
function pintaCM(){
  var k = $("cm-sel").value;
  if (!CM_DATOS[k]) CM_DATOS[k] = datosDeForma(FORMAS[k].f, 0, 10);
  var d = CM_DATOS[k], c = cinco(d), cl = clasesDe(FORMAS[k].f, 0, 10);
  $("cm-hist").innerHTML = histSVG(cl, T("Histogram of the data. Frequencies: ", "Histograma de los datos. Frecuencias: ") + FORMAS[k].f.join(", "));
  $("cm-caja").innerHTML = cajaSVG([{c: c}], T("Box plot of the same data: minimum ", "Diagrama de caja de los mismos datos: mínimo ") + c.min + ", Q1 " + nm(c.q1) + T(", median ", ", mediana ") + nm(c.med) + ", Q3 " + nm(c.q3) + T(", maximum ", ", máximo ") + c.max, {lo: 0, hi: 80, x0: 64, x1: 620});
  var nota = {sim: T("Both show a balanced set: the median is in the middle of the box and the whiskers are alike.", "Los dos muestran un conjunto equilibrado: la mediana queda en el centro de la caja y los bigotes son parecidos."),
    der: T("In the box plot, the skew shows as a long right whisker and the median closer to the left of the box. The histogram also shows where the peak is.", "En la caja, el sesgo se ve como un bigote derecho largo y la mediana corrida a la izquierda de la caja. El histograma muestra además dónde está el pico."),
    izq: T("In the box plot, the skew shows as a long left whisker. The histogram shows the tail toward the low values.", "En la caja, el sesgo se ve como un bigote izquierdo largo. El histograma muestra la cola hacia los valores bajos."),
    bim: T("The histogram clearly shows two peaks. The box plot cannot show them: it looks like a set with a wide box and nothing more. So for questions about peaks, use the histogram.", "El histograma muestra claramente dos picos. El diagrama de caja no puede mostrarlos: se ve como un conjunto con una caja ancha y nada más. Por eso, para preguntas sobre picos, conviene el histograma.")}[k];
  $("cm-salida").innerHTML = '<div class="linea">' + nota + "</div>";
}
function genMediana(){
  var f; do { f = datosAzar(6, 1, 9); } while (f.reduce(function(a, b){ return a + b; }, 0) % 2 === 0);
  var w = elige([5, 10]), a0 = elige([0, 10, 20]), cl = clasesDe(f, a0, w), n = f.reduce(function(a, b){ return a + b; }, 0), pos = (n + 1) / 2, acum = 0, idx = 0;
  for (var i = 0; i < f.length; i++){ if (acum + f[i] >= pos){ idx = i; break; } acum += f[i]; }
  var o = cl.map(function(c, i){ return {html: c.a + "–" + c.b, clave: "i" + i}; }), masAlta = f.indexOf(Math.max.apply(null, f)), pc = {};
  if (masAlta !== idx) pc["i" + masAlta] = T("That is the most frequent interval (the tallest bar), not necessarily the one with the median.", "Ese es el intervalo más frecuente (la barra más alta), no necesariamente el de la mediana.");
  var sel = [o[idx]].concat(baraja(o.filter(function(x, i){ return i !== idx; })).slice(0, 3)), suma = f.slice(0, idx + 1).join(" + ") + " = " + (acum + f[idx]);
  return {enun: T("This histogram has " + n + " data values. Which interval has the median?", "Este histograma tiene " + n + " datos. ¿En qué intervalo está la mediana?") + histSVG(cl, T("Histogram with intervals ", "Histograma con intervalos ") + cl.map(function(c){ return c.a + "–" + c.b; }).join(", ") + T(" and frequencies ", " y frecuencias ") + f.join(", ")), opciones: sel, correcta: "i" + idx, porClave: pc,
    pista: T("With " + n + " values, the median is value number " + pos + ". Add the frequencies from the left until you reach it.", "Con " + n + " datos, la mediana es el dato número " + pos + ". Sume las frecuencias desde la izquierda hasta llegar a él."),
    bien: T("The median is value number " + pos + ". Adding frequencies from the left (" + suma + "), you reach it in the interval " + cl[idx].a + "–" + cl[idx].b + ".", "La mediana es el dato número " + pos + ". Sumando frecuencias desde la izquierda (" + suma + "), se llega a él en el intervalo " + cl[idx].a + "–" + cl[idx].b + "."),
    mal: T("With " + n + " values, the median is value number " + pos + ". Add the frequencies from the left until you reach it: " + suma + ", in the interval " + cl[idx].a + "–" + cl[idx].b + ".", "Con " + n + " datos, la mediana es el dato número " + pos + ". Se suman las frecuencias desde la izquierda hasta llegar a él: " + suma + ", en el intervalo " + cl[idx].a + "–" + cl[idx].b + ".")};
}

/* MODULE 4 · Choosing the graph */
var ESCENARIOS = [
  [T("You want to know whether the ages in a group form one group or two very different groups.", "Se quiere saber si las edades de un grupo forman uno o dos grupos bien distintos."), "h", T("The question is about shape (one or two peaks?): the histogram shows it.", "La pregunta es sobre la forma (¿uno o dos picos?): lo muestra el histograma.")],
  [T("You want to compare the spread of the salaries at two companies.", "Se quiere comparar la dispersión de los salarios de dos empresas."), "c", T("To compare spread between groups, two box plots on the same scale are the clearest.", "Para comparar dispersión entre grupos, dos diagramas de caja sobre la misma escala son lo más claro.")],
  [T("You want to find out whether there are any unusual waiting times.", "Se quiere detectar si hay tiempos de espera atípicos."), "c", T("The box plot marks the outliers with the 1.5 × IQR rule.", "El diagrama de caja marca los valores atípicos con la regla de 1.5 × IQR.")],
  [T("You want to show how many students come from each country.", "Se quiere mostrar cuántos estudiantes vienen de cada país."), "b", T("Countries are separate categories: bar graph.", "Los países son categorías separadas: gráfica de barras.")],
  [T("You want to see whether the waiting times are skewed and where they are concentrated.", "Se quiere ver si los tiempos de espera están sesgados y dónde se concentran."), "h", T("The detailed shape and where the data are concentrated are seen best in the histogram.", "La forma detallada y la concentración se ven mejor en el histograma.")],
  [T("You want to know the quartiles of the scores on a test.", "Se quieren conocer los cuartiles de las calificaciones de un examen."), "c", T("The quartiles are exactly the values a box plot draws.", "Los cuartiles son justo los valores que dibuja el diagrama de caja.")],
  [T("You want to know which interval of heights is the most common.", "Se quiere saber qué intervalo de estaturas es el más frecuente."), "h", T("The most frequent interval is the tallest bar of the histogram.", "El intervalo más frecuente es la barra más alta del histograma.")],
  [T("You want to show the number of sales on each day of the week.", "Se quiere mostrar el número de ventas de cada día de la semana."), "b", T("The days are categories: bar graph.", "Los días son categorías: gráfica de barras.")],
  [T("You want to compare the medians of three groups of workers.", "Se quiere comparar la mediana de tres grupos de trabajadores."), "c", T("Three box plots on the same scale show the three medians at a glance.", "Tres diagramas de caja en la misma escala muestran las tres medianas de un vistazo.")],
  [T("You want to show the car color that customers like best.", "Se quiere mostrar el color de auto preferido por los clientes."), "b", T("Colors are categories: bar graph.", "Los colores son categorías: gráfica de barras.")]];
function genElegir(){
  var e = elige(ESCENARIOS);
  return {enun: e[0] + T(" Which graph should you use?", " ¿Qué gráfica conviene?"), opciones: [{html: T("Histogram", "Histograma"), clave: "h"}, {html: T("Box plot", "Diagrama de caja"), clave: "c"}, {html: T("Bar graph", "Gráfica de barras"), clave: "b"}], correcta: e[1], porClave: {},
    pista: T("Is the question about shape, about quartiles and spread, or about separate categories?", "¿La pregunta es sobre la forma, sobre los cuartiles y la dispersión, o sobre categorías separadas?"), bien: e[2], mal: e[2]};
}

/* Start */
$("hc-ancho").addEventListener("change", armaTabla);
$("hc-comprobar").addEventListener("click", compruebaHC);
$("hc-contar").addEventListener("click", contarHC);
$("hc-nuevo").addEventListener("click", nuevoHC);
nuevoHC();
$("fo-sel").addEventListener("change", pintaFO); pintaFO();
OMR("p1", genForma);
$("cm-sel").addEventListener("change", pintaCM); pintaCM();
OMR("p2", genMediana);
OMR("p3", genElegir);
'''

def practica_pagina():
    n = N
    formas = "".join(f'<option value="{k}">{v}</option>' for k, v in (("sim", t("Symmetric", "Simétrica")), ("der", t("Skewed right", "Sesgada a la derecha")), ("izq", t("Skewed left", "Sesgada a la izquierda")), ("uni", t("Uniform", "Uniforme")), ("bim", t("Bimodal", "Bimodal"))))
    conj = "".join(f'<option value="{k}">{v}</option>' for k, v in (("sim", t("Symmetric", "Simétrico")), ("der", t("Skewed right", "Sesgado a la derecha")), ("bim", t("Bimodal", "Bimodal")), ("izq", t("Skewed left", "Sesgado a la izquierda"))))
    mods = [
     (t("build", "construir"), t("Making a histogram", "Construir un histograma"),
      f'''      <p>{t("A histogram groups the data in intervals of the same width and draws one bar per interval, whose height is the <strong>frequency</strong>: how many values fall in it. The bars touch, because the intervals are continuous. In a bar graph, on the other hand, each bar is a category and they are separated.", "Un histograma agrupa los datos en intervalos del mismo ancho y dibuja una barra por intervalo, cuya altura es la <strong>frecuencia</strong>: cuántos datos caen en él. Las barras van pegadas, porque los intervalos son continuos. En una gráfica de barras, en cambio, cada barra es una categoría y van separadas.")}</p>
      <h3>{t("Count and draw", "Cuente y dibuje")}</h3>
      <p>{t("Count how many values fall in each interval and type the frequency. The histogram is drawn with your numbers. Each interval includes its left end but not its right end: 20–30 includes 20 but not 30.", "Cuente cuántos datos caen en cada intervalo y escriba la frecuencia. El histograma se dibuja con sus números. Cada intervalo incluye su extremo izquierdo, pero no el derecho: 20–30 incluye el 20 y no el 30.")}</p>
      <div class="panel">
        <p><strong id="hc-titulo"></strong></p>
        <div class="datos" id="hc-datos" aria-hidden="true"></div>
        <p class="sr-only" id="hc-voz"></p>
        <div class="campo"><label for="hc-ancho">{t("Width of the intervals", "Ancho de los intervalos")}</label><select id="hc-ancho"><option value="10">10</option><option value="5">5</option></select></div>
      </div>
      <table id="hc-tabla"></table>
      <div id="hc-svg"></div>
      <div class="fila-btn"><button type="button" class="btn" id="hc-comprobar">{t("Check the frequencies", "Comprobar frecuencias")}</button><button type="button" class="btn-sec" id="hc-contar">{t("Count for me", "Contar por mí")}</button><button type="button" class="btn-sec" id="hc-nuevo">{t("Other data", "Otros datos")}</button></div>
      <div class="fb" id="hc-fb" role="status"></div>'''),
     (t("shape", "forma"), t("The shape of a distribution", "La forma de la distribución"),
      f'''      <p>{t("The great advantage of a histogram is that it shows the shape of the data at a glance.", "La gran ventaja del histograma es que muestra la forma de los datos de un vistazo.")}</p>
      <h3>{t("Gallery of shapes", "Galería de formas")}</h3>
      <div class="panel"><div class="campo"><label for="fo-sel">{t("Shape", "Forma")}</label><select id="fo-sel">{formas}</select></div></div>
      <div id="fo-svg"></div>
{n3.salida("fo-salida")}
      <div class="caja-tip">{t("<strong>Skew is named by the tail, not by the peak:</strong> “skewed right” has its peak on the left and a long tail toward the high values.", "<strong>El sesgo se nombra por la cola, no por el pico:</strong> «sesgada a la derecha» tiene el pico a la izquierda y una cola larga hacia los valores altos.")}</div>
{B.om("p1", t("Practice: what shape does it have?", "Practique: ¿qué forma tiene?"))}'''),
     (t("compare", "comparar"), t("Histogram versus box plot", "Histograma frente a diagrama de caja"),
      f'''      <p>{t("The two graphs describe the same data from different angles. The histogram shows the shape and the peaks; the box plot shows the quartiles, the middle spread, and the outliers.", "Las dos gráficas describen el mismo conjunto desde ángulos distintos. El histograma muestra la forma y los picos; el diagrama de caja muestra los cuartiles, la dispersión central y los valores atípicos.")}</p>
      <h3>{t("The same data, two graphs", "Los mismos datos, dos gráficas")}</h3>
      <div class="panel"><div class="campo"><label for="cm-sel">{t("Data set", "Conjunto de datos")}</label><select id="cm-sel">{conj}</select></div></div>
      <div id="cm-hist"></div>
      <div id="cm-caja"></div>
{n3.salida("cm-salida")}
{B.om("p2", t("Practice: which interval has the median?", "Practique: ¿en qué intervalo está la mediana?"))}'''),
     (t("choose", "elegir"), t("Choosing the most useful display", "Elegir la representación más informativa"),
      f'''      <p>{t("There is no “best” graph in general: it depends on the question.", "No hay una gráfica «mejor» en abstracto: depende de la pregunta.")}</p>
      <table class="reglas"><caption>{t("Which graph answers each kind of question better", "Qué gráfica responde mejor cada tipo de pregunta")}</caption>
        <thead><tr><th scope="col">{t("If the question is about…", "Si la pregunta es sobre…")}</th><th scope="col">{t("Use", "Conviene")}</th></tr></thead>
        <tbody><tr><td>{t("the shape, the peaks, or the most frequent interval", "la forma, los picos o el intervalo más frecuente")}</td><td>{t("the histogram", "el histograma")}</td></tr>
        <tr><td>{t("the quartiles, the middle spread, or the outliers, or comparing groups", "los cuartiles, la dispersión central o los valores atípicos, o comparar grupos")}</td><td>{t("the box plot", "el diagrama de caja")}</td></tr>
        <tr><td>{t("separate categories (countries, colors, days of the week)", "categorías separadas (países, colores, días de la semana)")}</td><td>{t("the bar graph", "la gráfica de barras")}</td></tr></tbody></table>
{B.om("p3", t("Practice: which graph should you use?", "Practique: ¿qué gráfica conviene?"))}''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO_H, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Histogramas: construir, interpretar y comparar distribuciones")
