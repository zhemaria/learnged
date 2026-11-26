"""Level 3 · Lesson 7.2 · Box plots — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_7-2.html and algebra/n3-l7-2.html (GEDparaHispanos).
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n3
from build_n3_lesson_7_1 import ESTILO, SCRIPTS, TEMA

B.NIVEL = 3
N = "7-2"
TIT = ("Box plots", "Diagramas de caja y bigotes")

def figura_caja():
    X = lambda v: 40 + v * 5.5
    y = 90
    s = f'<line x1="{X(0)}" y1="150" x2="{X(90)}" y2="150" stroke="#424242" stroke-width="2"/>'
    for v in range(0, 91, 10):
        s += f'<line x1="{X(v)}" y1="144" x2="{X(v)}" y2="156" stroke="#424242" stroke-width="2"/><text x="{X(v)}" y="174" font-size="15" text-anchor="middle" fill="#222">{v}</text>'
    s += (f'<line x1="{X(10)}" y1="{y}" x2="{X(25)}" y2="{y}" stroke="#37474f" stroke-width="3"/><line x1="{X(55)}" y1="{y}" x2="{X(80)}" y2="{y}" stroke="#37474f" stroke-width="3"/>'
          f'<line x1="{X(10)}" y1="{y-12}" x2="{X(10)}" y2="{y+12}" stroke="#37474f" stroke-width="3"/><line x1="{X(80)}" y1="{y-12}" x2="{X(80)}" y2="{y+12}" stroke="#37474f" stroke-width="3"/>'
          f'<rect x="{X(25)}" y="{y-22}" width="{X(55)-X(25)}" height="44" fill="#cfd8dc" stroke="#37474f" stroke-width="3"/>'
          f'<line x1="{X(40)}" y1="{y-22}" x2="{X(40)}" y2="{y+22}" stroke="#b71c1c" stroke-width="4"/>')
    for v, et in ((10, t("Min", "Mín")), (25, "Q1"), (40, t("Median", "Mediana")), (55, "Q3"), (80, t("Max", "Máx"))):
        col = "#b71c1c" if v == 40 else "#424242"
        s += f'<text x="{X(v)}" y="38" font-size="15" font-weight="700" text-anchor="middle" fill="{col}">{et}</text><text x="{X(v)}" y="56" font-size="15" text-anchor="middle" fill="{col}">{v}</text>'
    return B.svg("0 0 560 186", t("A box plot on a number line from 0 to 90. The left whisker starts at the minimum, 10. The box goes from Q1 = 25 to Q3 = 55, with a line at the median, 40. The right whisker ends at the maximum, 80.",
                                  "Un diagrama de caja sobre una recta numérica de 0 a 90. El bigote izquierdo empieza en el mínimo, 10. La caja va de Q1 = 25 a Q3 = 55, con una línea en la mediana, 40. El bigote derecho termina en el máximo, 80."), s, 560)

def leccion():
    n = N
    s1 = f'''<p>{t("Lesson 7.1 measured how much fits inside a solid. This lesson turns to data: how to summarize a set of numbers so you can see it at a glance. A box plot shows, in a single picture, where the data are concentrated, how spread out they are, and whether there are unusual values.", "La Lección 7.1 midió cuánto cabe en un cuerpo sólido. Esta lección cambia el foco hacia los datos: cómo resumir un conjunto de números para verlo de un vistazo. El diagrama de caja y bigotes muestra, en una sola imagen, dónde se concentran los datos, qué tan dispersos están y si hay valores fuera de lo común.")}</p>
<p>{t("A box plot is built from five numbers that summarize the set: the <strong>minimum</strong>, the <strong>first quartile Q1</strong>, the <strong>median</strong> (Q2), the <strong>third quartile Q3</strong>, and the <strong>maximum</strong>. The box goes from Q1 to Q3, with a line at the median, and the whiskers reach the minimum and the maximum.", "Un diagrama de caja se construye con cinco números que resumen el conjunto: el <strong>mínimo</strong>, el <strong>primer cuartil Q1</strong>, la <strong>mediana</strong> (Q2), el <strong>tercer cuartil Q3</strong> y el <strong>máximo</strong>. La caja va de Q1 a Q3, con una línea en la mediana, y los bigotes llegan al mínimo y al máximo.")}</p>
{figura_caja()}
{caja("tip", t("Each part holds one quarter", "Cada zona, una cuarta parte"), t("<p>The quartiles split the data into four groups with 25% of the data each. The lowest 25% is between the minimum and Q1; the box (from Q1 to Q3) holds the middle 50% of the data.</p>", "<p>Los cuartiles dividen los datos en cuatro grupos del 25% cada uno. Entre el mínimo y Q1 está el 25% más bajo; la caja (de Q1 a Q3) contiene el 50% central de los datos.</p>"))}
{enlace(n, t("five-values", "cinco-valores"), t("the five key values", "los cinco valores clave"), t("Find the minimum, Q1, the median, Q3, and the maximum of a data set.", "Halle el mínimo, Q1, la mediana, Q3 y el máximo de un conjunto de datos."))}'''

    pasos = [t("Put the data in order from least to greatest.", "Ordenar los datos de menor a mayor."),
             t("Find the median (the middle value).", "Encontrar la mediana (el valor central)."),
             t("Find Q1 (the median of the lower half) and Q3 (the median of the upper half).", "Encontrar Q1 (mediana de la mitad inferior) y Q3 (mediana de la superior)."),
             t("Draw the box from Q1 to Q3, with a line at the median.", "Trazar la caja de Q1 a Q3 con la línea de la mediana."),
             t("Draw the whiskers out to the minimum and the maximum.", "Trazar los bigotes hasta el mínimo y el máximo.")]
    s2 = f'''<p>{t("The procedure has five steps in order.", "El procedimiento sigue cinco pasos ordenados.")}</p>
{tabla(t("Five steps to build a box plot", "Cinco pasos para construir un diagrama de caja"), t("Five steps to build a box plot", "Cinco pasos para construir un diagrama de caja y bigotes"), [t("Step", "Paso"), t("What to do", "Acción")], [[str(i + 1), p] for i, p in enumerate(pasos)])}
{ejemplo(t("Example 1: for the data 2, 4, 6, 8, 10, what is the median?", "Ejemplo 1 · Para los datos 2, 4, 6, 8, 10, ¿cuál es la mediana?"),
  [("1", t("They are already in order.", "Ya están ordenados."), t("There are five values, so the middle one is the third.", "Hay cinco valores, así que el central es el tercero.")),
   ("✓", t("Answer.", "Respuesta."), t("The median is <strong>6</strong>.", "La mediana es <strong>6</strong>."))])}
{caja("tip", t("Odd or even number of data", "Cantidad impar o par de datos"), t("<p>With an odd number of data, the median is the middle value, and it does not go into either half. With an even number, the median is the average of the two middle values, and each half keeps half of the data.</p>", "<p>Con una cantidad impar de datos, la mediana es el dato central y no entra en ninguna de las dos mitades. Con una cantidad par, la mediana es el promedio de los dos centrales, y cada mitad se queda con la mitad de los datos.</p>"))}
{practica("p1", t("Practice 1 — The median", "Práctica 1 — La mediana"), t("For the data 1, 3, 5, 7, 9, the median is…", "Para los datos 1, 3, 5, 7, 9, la mediana es…"), [("a", "4"), ("b", "5"), ("c", "7")])}
{practica("p2", t("Practice 2 — The IQR", "Práctica 2 — El IQR"), t("If Q1 = 10 and Q3 = 30, the IQR is…", "Si Q1 = 10 y Q3 = 30, el IQR es…"), [("a", "20"), ("b", "40"), ("c", "10")])}
{practica("p3", t("Practice 3 — Key values", "Práctica 3 — Valores clave"), t("How many key values does a box plot have?", "¿Cuántos valores clave tiene el diagrama de caja?"), [("a", "3"), ("b", "4"), ("c", "5")])}
{enlace(n, t("build", "construir"), t("building the plot", "construir el diagrama"), t("Draw the box and the whiskers from the five values, and read a plot.", "Trace la caja y los bigotes a partir de los cinco valores, y lea un diagrama."))}'''

    s3 = f'''<p>{t("The <strong>interquartile range</strong> (IQR) measures how spread out the middle half of the data is. Find it by subtracting:", "El <strong>rango intercuartílico</strong> (IQR, por sus siglas en inglés) mide qué tan dispersa está la mitad central de los datos. Se calcula restando:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">IQR = Q3 − Q1</p>
{ejemplo(t("Example 2: in the plot above, Q1 = 25 and Q3 = 55. What is the IQR?", "Ejemplo 2: en el diagrama de arriba, Q1 = 25 y Q3 = 55. ¿Cuál es el IQR?"),
  [("1", t("Subtract.", "Se resta."), "55 − 25 = 30."),
   ("✓", t("Answer.", "Respuesta."), t("The IQR is <strong>30</strong>. It is the width of the box.", "El IQR es <strong>30</strong>. Es el ancho de la caja."))])}
{caja("tip", t("The IQR resists extreme values", "El IQR resiste a los extremos"), t("<p>Unlike the range (max − min), the IQR is not affected by one or two very large or very small values, because it only looks at the middle 50%. That is why it is a reliable measure of spread.</p>", "<p>A diferencia del rango total (máx − mín), el IQR no se ve afectado por uno o dos valores muy grandes o muy pequeños, porque solo mira el 50% central. Por eso es una medida de dispersión confiable.</p>"))}
{enlace(n, "iqr", t("the interquartile range", "el rango intercuartílico"), t("Find the IQR and connect it with the percents of the data.", "Calcule el IQR y relaciónelo con los porcentajes de datos."))}'''

    s4 = f'''<p>{t("An <strong>outlier</strong> is a data value that is far away from the rest. The most common rule to find outliers uses the IQR: a value is an outlier if it is more than 1.5 × IQR above Q3 or below Q1.", "Un <strong>valor atípico</strong> es un dato que queda muy lejos del resto. La regla más usada para detectarlos emplea el IQR: un valor es atípico si está más allá de 1.5 × IQR por encima de Q3 o por debajo de Q1.")}</p>
<p class="formula" style="text-align:center;font-weight:700;">{t("lower limit = Q1 − 1.5 × IQR &nbsp;&nbsp;&nbsp; upper limit = Q3 + 1.5 × IQR", "límite inferior = Q1 − 1.5 × IQR &nbsp;&nbsp;&nbsp; límite superior = Q3 + 1.5 × IQR")}</p>
{ejemplo(t("Example 3: the upper limit. With Q3 = 55 and IQR = 30, what is the upper limit for outliers?", "Ejemplo 3 · Límite superior. Con Q3 = 55 e IQR = 30, ¿cuál es el límite superior para valores atípicos?"),
  [("1", t("Find 1.5 × IQR.", "Se calcula 1.5 × IQR."), "1.5 × 30 = 45."),
   ("2", t("Add it to Q3.", "Se suma a Q3."), "55 + 45 = 100."),
   ("✓", t("Answer.", "Respuesta."), t("Any value greater than <strong>100</strong> would be an outlier on the high side.", "Cualquier dato mayor que <strong>100</strong> sería un valor atípico por arriba."))])}
{practica("p4", t("Practice 4 — The rule", "Práctica 4 — La regla"), t("The rule for finding outliers uses…", "La regla para detectar valores atípicos usa el factor…"), [("a", t("2 × the mean", "2 × la media")), ("b", "Q2"), ("c", "1.5 × IQR")])}
{enlace(n, t("outliers", "atipicos"), t("outliers", "valores atípicos"), t("Use the 1.5 × IQR rule to find outliers.", "Aplique la regla de 1.5 × IQR para detectar datos atípicos."))}'''

    s5 = f'''<p>{t("The real value of a box plot is in reading it. A wide box means the data are spread out; a narrow box means the data are close together. Comparing two plots on the same scale shows which group has the higher median or more variability.", "El verdadero valor del diagrama está en interpretarlo. Una caja ancha indica datos muy dispersos; una caja angosta, datos concentrados. Comparando dos diagramas sobre la misma escala se ve cuál grupo tiene la mediana más alta o más variabilidad.")}</p>
{ejemplo(t("Example 4: comparing two groups. Group A has a median of 70 and a narrow box; group B has a median of 60 and a wide box. What can you conclude?", "Ejemplo 4 · Comparar dos grupos. El grupo A tiene mediana 70 y una caja angosta; el grupo B tiene mediana 60 y una caja ancha. ¿Qué se concluye?"),
  [("1", t("Compare the medians.", "Se comparan las medianas."), t("A's median (70) is higher than B's (60): A tends to have higher values.", "La mediana de A (70) es mayor que la de B (60): A tiende a valores más altos.")),
   ("2", t("Compare the boxes.", "Se comparan las cajas."), t("B's box is wider: B has more variability (a larger IQR).", "La caja de B es más ancha: B tiene mayor variabilidad (mayor IQR).")),
   ("✓", t("Answer.", "Respuesta."), t("A has higher, more consistent values; B is more spread out.", "A tiene valores más altos y más consistentes; B está más disperso."))])}
{caja("ojo", t("Median is not mean", "Mediana no es media"), t("<p>The line in the box is the median. A box plot does not show the mean (the average).</p>", "<p>La raya de la caja es la mediana. El diagrama de caja no muestra la media (el promedio).</p>"))}
{practica("p5", t("Practice 5 — The line in the box", "Práctica 5 — La raya de la caja"), t("The line inside the box shows…", "La línea dentro de la caja representa…"), [("a", t("the median", "la mediana")), ("b", t("the mean", "la media")), ("c", t("the minimum", "el mínimo"))])}
{practica("p6", t("Practice 6 — A wider box", "Práctica 6 — Una caja más ancha"), t("A wider box shows…", "Una caja más ancha indica…"), [("a", t("less variability", "menos variabilidad")), ("b", t("more variability", "más variabilidad")), ("c", t("a higher median", "mayor mediana"))])}
{enlace(n, t("compare", "comparar"), t("reading and comparing", "interpretar y comparar"), t("Compare two box plots: center, spread, and shape.", "Compare dos diagramas de caja: centro, dispersión y forma."))}'''

    secciones = [("s-" + t("five-values", "cinco-valores"), t("The five key values", "Los cinco valores clave"), s1),
                 ("s-" + t("build", "construir"), t("Building the plot", "Construir el diagrama"), s2),
                 ("s-iqr", t("The interquartile range (IQR)", "El rango intercuartílico (IQR)"), s3),
                 ("s-" + t("outliers", "atipicos"), t("Outliers", "Valores atípicos"), s4),
                 ("s-" + t("compare", "comparar"), t("Reading and comparing", "Interpretar y comparar"), s5)]

    lesson = {"next": t("Lesson 7.3", "Lección 7.3"), "review": t("sections 2 to 4", "las secciones 2 a 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The median is one of the data values here: the one in the middle.", "Aquí la mediana es uno de los datos: el del centro."), "c": t("7 is the fourth value. With five values, the middle one is the third.", "7 es el cuarto dato. Con cinco datos, el central es el tercero.")}, "right": t("The middle value of five is the third: 5.", "El central de cinco datos es el tercero: 5."), "solution": t("The median is 5.", "La mediana es 5.")},
      "p2": {"ok": "a", "hints": {"b": t("You added. The IQR is Q3 − Q1.", "Sumó. El IQR es Q3 − Q1."), "c": t("10 is Q1. Subtract: 30 − 10.", "10 es Q1. Reste: 30 − 10.")}, "right": "30 − 10 = 20.", "solution": "IQR = 30 − 10 = 20."},
      "p3": {"ok": "c", "hints": {"a": t("Count them: minimum, Q1, median, Q3, maximum.", "Cuéntelos: mínimo, Q1, mediana, Q3, máximo."), "b": t("Four is the number of parts. Count the values that separate them, plus the ends.", "Cuatro es el número de zonas. Cuente los valores que las separan, más los extremos.")}, "right": t("Minimum, Q1, median, Q3, and maximum: five.", "Mínimo, Q1, mediana, Q3 y máximo: cinco."), "solution": t("Five.", "Cinco.")},
      "p4": {"ok": "c", "hints": {"a": t("The rule uses the IQR, not the mean.", "La regla usa el IQR, no la media."), "b": t("The rule measures distance from Q1 and Q3 with the IQR.", "La regla mide la distancia a Q1 y Q3 con el IQR.")}, "right": t("Outliers are more than 1.5 × IQR beyond Q1 or Q3.", "Son atípicos los datos a más de 1.5 × IQR de Q1 o de Q3."), "solution": "1.5 × IQR."},
      "p5": {"ok": "a", "hints": {"b": t("A box plot does not show the mean.", "El diagrama de caja no muestra la media."), "c": t("The minimum is at the end of the left whisker.", "El mínimo está al final del bigote izquierdo.")}, "right": t("The line in the box is the median.", "La raya de la caja es la mediana."), "solution": t("The median.", "La mediana.")},
      "p6": {"ok": "b", "hints": {"a": t("A wider box means the middle data are farther apart.", "Una caja más ancha significa datos centrales más separados."), "c": t("The width shows spread, not the center.", "El ancho muestra la dispersión, no el centro.")}, "right": t("The width of the box is the IQR: wider means more spread out.", "El ancho de la caja es el IQR: más ancha, más dispersión."), "solution": t("More variability.", "Más variabilidad.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("5 is not in the data. With five values, the median is the third.", "5 no está en los datos. Con cinco datos, la mediana es el tercero."), "c": t("8 is the fourth value.", "8 es el cuarto dato."), "d": t("4 is the second value.", "4 es el segundo dato.")}, "solution": t("The median is 6.", "La mediana es 6.")},
      "B": {"ok": "d", "hints": {"a": t("You added. Subtract: Q3 − Q1.", "Sumó. Reste: Q3 − Q1."), "b": t("50 is Q3. Subtract Q1.", "50 es Q3. Falta restar Q1."), "c": t("20 is Q1. Subtract it from Q3.", "20 es Q1. Réstelo de Q3.")}, "solution": "50 − 20 = 30."},
      "C": {"ok": "a", "hints": {"b": t("The IQR is a difference, not a sum.", "El IQR es una resta, no una suma."), "c": t("Max − min is the range, not the IQR.", "Máx − mín es el rango, no el IQR."), "d": t("The median is the center, not a spread.", "La mediana es el centro, no una dispersión.")}, "solution": "IQR = Q3 − Q1."},
      "D": {"ok": "c", "hints": {"a": t("The factor is 1.5, not 2.", "El factor es 1.5, no 2."), "b": t("The rule uses the IQR.", "La regla usa el IQR."), "d": t("The rule uses the IQR, not the range.", "La regla usa el IQR, no el rango.")}, "solution": "1.5 × IQR."},
      "E": {"ok": "a", "hints": {"b": t("Multiply the IQR by 1.5 before adding.", "Multiplique el IQR por 1.5 antes de sumar."), "c": t("45 is 1.5 × IQR. Add it to Q3.", "45 es 1.5 × IQR. Súmelo a Q3."), "d": t("Find 1.5 × 30 = 45, then add 55.", "Calcule 1.5 × 30 = 45 y súmele 55.")}, "solution": "55 + 1.5 × 30 = 100."},
      "F": {"ok": "c", "hints": {"a": t("Q1 and Q3 are the ends of the box.", "Q1 y Q3 son los extremos de la caja."), "b": t("A box plot does not show the mean.", "El diagrama de caja no muestra la media."), "d": t("When there are outliers, the whiskers stop at the last value that is not an outlier.", "Si hay atípicos, los bigotes llegan solo hasta el último dato que no es atípico.")}, "solution": t("To the minimum and the maximum.", "Hasta el mínimo y el máximo.")},
      "G": {"ok": "b", "hints": {"a": t("A box plot does not show the mean.", "El diagrama de caja no muestra la media."), "c": t("The maximum is at the end of the right whisker.", "El máximo está al final del bigote derecho."), "d": t("The IQR is the width of the box, not a line.", "El IQR es el ancho de la caja, no una línea.")}, "solution": t("The median.", "La mediana.")},
      "H": {"ok": "d", "hints": {"a": t("A wider box means the middle data are farther apart.", "Una caja más ancha significa datos centrales más separados."), "b": t("Outliers are shown as separate points, not by the width of the box.", "Los atípicos se marcan como puntos aparte, no con el ancho de la caja."), "c": t("The width shows spread, not the center.", "El ancho muestra la dispersión, no el centro.")}, "solution": t("More variability.", "Mayor variabilidad.")}
     }}

    quiz = [
     ("A", t("For the ordered data 2, 4, 6, 8, 10, the median (Q2) is…", "Datos ordenados 2, 4, 6, 8, 10. La mediana (Q2) es…"), [("a", "5"), ("b", "6"), ("c", "8"), ("d", "4")]),
     ("B", t("If Q1 = 20 and Q3 = 50, the IQR is…", "Si Q1 = 20 y Q3 = 50, el IQR es…"), [("a", "70"), ("b", "50"), ("c", "20"), ("d", "30")]),
     ("C", t("The IQR is found with…", "El IQR se calcula como…"), [("a", "Q3 − Q1"), ("b", "Q3 + Q1"), ("c", t("max − min", "máx − mín")), ("d", t("the median", "la mediana"))]),
     ("D", t("The rule for finding outliers uses…", "La regla para detectar valores atípicos usa el factor…"), [("a", "2 × IQR"), ("b", t("the median", "la mediana")), ("c", "1.5 × IQR"), ("d", t("the range", "el rango"))]),
     ("E", t("If IQR = 30 and Q3 = 55, the upper limit (Q3 + 1.5 × IQR) is…", "Si IQR = 30 y Q3 = 55, el límite superior (Q3 + 1.5 × IQR) es…"), [("a", "100"), ("b", "85"), ("c", "45"), ("d", "75")]),
     ("F", t("In a box plot with no outliers, the whiskers reach…", "En un diagrama de caja sin valores atípicos, los bigotes llegan hasta…"), [("a", t("Q1 and Q3", "Q1 y Q3")), ("b", t("the mean", "la media")), ("c", t("the minimum and the maximum", "el mínimo y el máximo")), ("d", t("the outliers", "los valores atípicos"))]),
     ("G", t("The line inside the box shows…", "La línea dentro de la caja representa…"), [("a", t("the mean", "la media")), ("b", t("the median", "la mediana")), ("c", t("the maximum", "el máximo")), ("d", t("the IQR", "el IQR"))]),
     ("H", t("A group with a wider box has…", "Un grupo con una caja más ancha tiene…"), [("a", t("less variability", "menor variabilidad")), ("b", t("always more outliers", "siempre más valores atípicos")), ("c", t("a higher median", "mayor mediana")), ("d", t("more variability", "mayor variabilidad"))])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Summarize a data set with five key values, draw a box plot, find the IQR and the outliers, and compare two groups.", "Resuma un conjunto de datos con cinco valores clave, construya un diagrama de caja, halle el IQR y los valores atípicos, y compare dos grupos."),
        ("📊", t("Data at a glance", "Datos de un vistazo")),
        [t("<strong>Identify</strong> the five key values: minimum, Q1, median (Q2), Q3, and maximum.", "<strong>Identificar</strong> los cinco valores clave: mínimo, Q1, mediana (Q2), Q3 y máximo."),
         t("<strong>Build</strong> a box plot from ordered data.", "<strong>Construir</strong> un diagrama de caja y bigotes a partir de datos ordenados."),
         t("<strong>Find</strong> the interquartile range (IQR = Q3 − Q1).", "<strong>Calcular</strong> el rango intercuartílico (IQR = Q3 − Q1)."),
         t("<strong>Identify</strong> outliers with the 1.5 × IQR rule.", "<strong>Identificar</strong> valores atípicos usando la regla 1.5 × IQR."),
         t("<strong>Interpret</strong> spread and compare two distributions.", "<strong>Interpretar</strong> la dispersión y comparar dos distribuciones.")],
        secciones,
        (t("Take two data sets of 9 to 12 numbers each (for example, the scores of two classes). For each one, find the five key values, the IQR, and the limits for outliers, and draw both box plots on the same scale. Then write two sentences comparing the groups: one about the center and one about the spread.",
           "Tome dos conjuntos de 9 a 12 datos cada uno (por ejemplo, las calificaciones de dos grupos). En cada uno, halle los cinco valores clave, el IQR y los límites para valores atípicos, y dibuje los dos diagramas de caja sobre la misma escala. Después escriba dos oraciones que comparen los grupos: una sobre el centro y otra sobre la dispersión."),
         t("Write down how many minutes it takes you to get somewhere every day for two weeks (work, school, the store). Make a box plot of your times. Which days, if any, are outliers? What was going on those days?",
           "Anote durante dos semanas cuántos minutos tarda en llegar a algún lugar cada día (el trabajo, la escuela, la tienda). Haga un diagrama de caja con sus tiempos. ¿Qué días, si los hay, son atípicos? ¿Qué pasó esos días?")),
        quiz,
        t("Self-check checklist for box plots", "Lista de autoevaluación de diagramas de caja"),
        t("Self-check checklist: skills for box plots, the IQR, and outliers", "Lista de autoevaluación: destrezas de diagramas de caja, IQR y valores atípicos"),
        [(t("The five key values", "Los cinco valores clave"), t("I put the data in order and find the five key values, even with repeated values.", "Ordeno los datos e identifico los cinco valores clave, incluso con datos repetidos."), t("I find some values with mistakes.", "Identifico algunos valores con errores."), t("I do not find the five values.", "No identifico los cinco valores.")),
         (t("IQR and outliers", "IQR y valores atípicos"), t("I find the IQR and use the 1.5 × IQR rule on both sides.", "Calculo el IQR y aplico la regla 1.5 × IQR por arriba y por abajo."), t("I find the IQR but do not use the outlier rule.", "Calculo el IQR, pero no aplico la regla de atípicos."), t("I do not find the IQR.", "No calculo el IQR.")),
         (t("Building the plot", "Construir el diagrama"), t("I draw the plot to scale and label all the values.", "Construyo el diagrama a escala y rotulo todos los valores."), t("I draw the box with scale mistakes.", "Construyo la caja con errores de escala."), t("I do not draw the plot.", "No construyo el diagrama.")),
         (t("Reading the spread", "Interpretar la dispersión"), t("I read the spread and compare two distributions, and I know what a box plot cannot show.", "Interpreto la dispersión, comparo dos distribuciones y distingo lo que el diagrama no puede mostrar."), t("I read it partly or loosely.", "Interpreto de forma parcial o imprecisa."), t("I do not read the spread.", "No interpreto la dispersión."))],
        t("<p>In this lesson you learned to summarize a data set with the five key values, draw a box plot, find the IQR (Q3 − Q1), find outliers with the 1.5 × IQR rule, and compare distributions by their median and spread.</p>\n<p>In <strong>Lesson 7.3 · Histograms: make, read, and compare</strong> you will study another way to see data: the histogram, with bars that touch. You will describe the shape of a distribution (symmetric, skewed, one peak or two) and compare it with a box plot to choose the best display.</p>",
          "<p>En esta lección se aprendió a resumir un conjunto de datos con los cinco valores clave, a construir un diagrama de caja y bigotes, a calcular el IQR (Q3 − Q1), a detectar valores atípicos con la regla 1.5 × IQR y a comparar distribuciones por su mediana y dispersión.</p>\n<p>En la <strong>Lección 7.3 · Histogramas: construir, interpretar y comparar distribuciones</strong> se estudiará otra forma de ver los datos: el histograma, con sus barras contiguas. Se describirá la forma de la distribución (simétrica, sesgada, unimodal o bimodal) y se comparará con el diagrama de caja para elegir la mejor representación.</p>"),
        ("7-3", ("", t("Lesson 7.3 · Histograms: make, read, and compare", "Lección 7.3 · Histogramas: construir, interpretar y comparar distribuciones"))),
        [(t("quartiles", "cuartiles"), t("The values that split ordered data into four parts with 25% each: Q1, the median (Q2), and Q3.", "Los valores que dividen los datos ordenados en cuatro partes del 25%: Q1, la mediana (Q2) y Q3.")),
         (t("median", "mediana"), t("The middle value of ordered data, or the average of the two middle values.", "El valor central de los datos ordenados, o el promedio de los dos centrales.")),
         (t("interquartile range (IQR)", "rango intercuartílico (IQR)"), t("Q3 − Q1: the spread of the middle 50% of the data.", "Q3 − Q1: la dispersión del 50% central de los datos.")),
         (t("range", "rango"), t("Maximum − minimum.", "Máximo − mínimo.")),
         (t("outlier", "valor atípico"), t("A value more than 1.5 × IQR below Q1 or above Q3.", "Un dato a más de 1.5 × IQR por debajo de Q1 o por encima de Q3."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* MODULE 1 · The five values, step by step */
function pasosCinco(d){
  var c = cinco(d), o = c.o, n = o.length, m = Math.floor(n / 2), h = mitades(o), pasos = [];
  pasos.push(T("Put the data in order from least to greatest:", "Se ordenan los datos de menor a mayor:") + chips(o));
  pasos.push(T("The minimum is " + nm(c.min) + " and the maximum is " + nm(c.max) + ".", "El mínimo es " + nm(c.min) + " y el máximo es " + nm(c.max) + "."));
  var cm = o.map(function(v, i){ return (n % 2 ? i === m : (i === m - 1 || i === m)) ? "med" : ""; });
  pasos.push((n % 2 ? T("There are " + n + " values (odd): the median is the middle value, in place " + (m + 1) + ". Median = " + nm(c.med) + ".", "Hay " + n + " datos (impar): la mediana es el dato central, el que ocupa el lugar " + (m + 1) + ". Mediana = " + nm(c.med) + ".")
                    : T("There are " + n + " values (even): the median is the average of the two middle values, (" + nm(o[m - 1]) + " + " + nm(o[m]) + ") ÷ 2 = " + nm(c.med) + ".", "Hay " + n + " datos (par): la mediana es el promedio de los dos centrales, (" + nm(o[m - 1]) + " + " + nm(o[m]) + ") ÷ 2 = " + nm(c.med) + ".")) + chips(o, cm));
  var cq = o.map(function(v, i){ return i < h[0].length ? "baja" : (i >= n - h[1].length ? "alta" : "med"); });
  pasos.push(T("Q1 is the median of the lower half (" + listaN(h[0]) + "): Q1 = " + nm(c.q1) + ". Q3 is the median of the upper half (" + listaN(h[1]) + "): Q3 = " + nm(c.q3) + ".", "Q1 es la mediana de la mitad de abajo (" + listaN(h[0]) + "): Q1 = " + nm(c.q1) + ". Q3 es la mediana de la mitad de arriba (" + listaN(h[1]) + "): Q3 = " + nm(c.q3) + ".") + chips(o, cq));
  pasos.push('<span class="veredicto">' + T("The five values: minimum " + nm(c.min) + ", Q1 = " + nm(c.q1) + ", median = " + nm(c.med) + ", Q3 = " + nm(c.q3) + ", maximum " + nm(c.max) + ".", "Los cinco valores: mínimo " + nm(c.min) + ", Q1 = " + nm(c.q1) + ", mediana = " + nm(c.med) + ", Q3 = " + nm(c.q3) + ", máximo " + nm(c.max) + ".") + "</span>" +
             cajaSVG([{c: c}], T("Box plot: minimum ", "Diagrama de caja: mínimo ") + nm(c.min) + ", Q1 " + nm(c.q1) + T(", median ", ", mediana ") + nm(c.med) + ", Q3 " + nm(c.q3) + T(", maximum ", ", máximo ") + nm(c.max), {rotulos: true}));
  return pasos;
}
var CV_COLA = [[12, 7, 3, 15, 9, 20, 11], [25, 40, 10, 55, 30, 45, 20, 35]];
function nuevoCV(){ var d = CV_COLA.length ? CV_COLA.shift() : datosAzar(aleatorio(7, 12), 5, 60); $("cv-datos").textContent = listaN(d); CVS.carga(pasosCinco(d)); }
var NOMBRE5 = {med: T("the median", "la mediana"), q1: "Q1", q3: "Q3", rango: T("the range", "el rango"), iqr: T("the IQR", "el IQR"), min: T("the minimum", "el mínimo"), max: T("the maximum", "el máximo")};
function genCinco(){
  var d = datosAzar(aleatorio(7, 12), 1, 50), c = cinco(d), cual = elige(["med", "q1", "q3", "rango", "iqr", "min", "max"]);
  var res = {med: c.med, q1: c.q1, q3: c.q3, rango: c.max - c.min, iqr: c.q3 - c.q1, min: c.min, max: c.max}[cual];
  var pistas = [];
  if (cual === "med") pistas.push({v: mediana(d), msg: T("Put the data in order from least to greatest first.", "Primero hay que ordenar los datos de menor a mayor.")});
  if (cual === "iqr") pistas.push({v: c.max - c.min, msg: T("That is the range (max − min). The IQR is Q3 − Q1.", "Ese es el rango (máx − mín). El IQR es Q3 − Q1.")});
  if (cual === "rango") pistas.push({v: c.q3 - c.q1, msg: T("That is the IQR. The range is max − min.", "Ese es el IQR. El rango es máx − mín.")});
  if (cual === "q1") pistas.push({v: c.q3, msg: T("That is Q3. Q1 is the median of the lower half.", "Ese es Q3. Q1 es la mediana de la mitad de abajo.")});
  if (cual === "q3") pistas.push({v: c.q1, msg: T("That is Q1. Q3 is the median of the upper half.", "Ese es Q1. Q3 es la mediana de la mitad de arriba.")});
  return {enun: T("Data: ", "Datos: ") + listaN(d) + T(". What is " + NOMBRE5[cual] + "?", ". ¿Cuánto vale " + NOMBRE5[cual] + "?"),
    solucion: T("In order: ", "Ordenados: ") + listaN(c.o) + T(". Minimum ", ". Mínimo ") + nm(c.min) + ", Q1 = " + nm(c.q1) + T(", median = ", ", mediana = ") + nm(c.med) + ", Q3 = " + nm(c.q3) + T(", maximum ", ", máximo ") + nm(c.max) + "." +
              (cual === "rango" ? T(" Range = ", " Rango = ") + nm(c.max) + " − " + nm(c.min) + " = " + nm(res) + "." : "") + (cual === "iqr" ? " IQR = " + nm(c.q3) + " − " + nm(c.q1) + " = " + nm(res) + "." : ""),
    evalua: function(v){ var r = evaluaDec(v, res, pistas); if (r.estado === "mal" && !pistas.some(function(p){ return p.msg === r.msg; })) r.msg = T("Put the data in order and find the halves carefully.", "Ordene los datos y busque las mitades con cuidado."); return r; }};
}

/* MODULE 2 · Build and read */
function pintaCD(){
  var v = [0, 1, 2, 3, 4].map(function(i){ return leeDecimal($("cd-" + i).value); }), av = $("cd-aviso");
  if (v.some(function(x){ return x === null; }) || v.some(function(x, i){ return i > 0 && x < v[i - 1]; })){
    av.className = "caja-aviso visible"; av.textContent = T("Type five numbers in order: minimum ≤ Q1 ≤ median ≤ Q3 ≤ maximum.", "Escriba cinco números en orden: mínimo ≤ Q1 ≤ mediana ≤ Q3 ≤ máximo.");
    $("cd-svg").innerHTML = ""; $("cd-salida").innerHTML = ""; return;
  }
  av.className = "caja-aviso"; av.textContent = "";
  var c = {min: v[0], q1: v[1], med: v[2], q3: v[3], max: v[4]};
  $("cd-svg").innerHTML = cajaSVG([{c: c}], T("Box plot with minimum ", "Diagrama de caja con mínimo ") + nm(v[0]) + ", Q1 " + nm(v[1]) + T(", median ", ", mediana ") + nm(v[2]) + ", Q3 " + nm(v[3]) + T(", and maximum ", " y máximo ") + nm(v[4]), {rotulos: true});
  $("cd-salida").innerHTML = '<div class="linea">' + T("Each of the four parts (left whisker, the two parts of the box, and right whisker) holds <strong>25%</strong> of the data, even if some look longer than others.", "Cada una de las cuatro zonas (bigote izquierdo, las dos partes de la caja y bigote derecho) contiene el <strong>25%</strong> de los datos, aunque unas se vean más largas que otras.") + "</div>" +
    '<div class="linea">' + T("The box, from " + nm(v[1]) + " to " + nm(v[3]) + ", holds the middle 50%. A long part means those data are farther apart, not that there are more of them.", "La caja, de " + nm(v[1]) + " a " + nm(v[3]) + ", contiene el 50% central. Una zona larga significa que esos datos están más separados, no que haya más.") + "</div>";
}
function cincoMultiplos(){
  var base = 5 * aleatorio(0, 10), p = [0].concat(baraja([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).slice(0, 4)).sort(function(a, b){ return a - b; });
  var v = p.map(function(k){ return base + 5 * k; });
  return {min: v[0], q1: v[1], med: v[2], q3: v[3], max: v[4]};
}
function genLeer(){
  var c = cincoMultiplos(), cual = elige(["med", "q1", "q3", "max", "min", "rango", "iqr"]);
  var res = {med: c.med, q1: c.q1, q3: c.q3, max: c.max, min: c.min, rango: c.max - c.min, iqr: c.q3 - c.q1}[cual];
  var cand = [c.min, c.q1, c.med, c.q3, c.max, c.max - c.min, c.q3 - c.q1].filter(function(x, i, a){ return x !== res && a.indexOf(x) === i; });
  var o = [{html: String(res), clave: "n" + res}].concat(baraja(cand).slice(0, 3).map(function(x){ return {html: String(x), clave: "n" + x}; }));
  while (o.length < 4){ var extra = res + 5 * o.length; if (!o.some(function(z){ return z.clave === "n" + extra; })) o.push({html: String(extra), clave: "n" + extra}); }
  var exp = T("Minimum " + c.min + ", Q1 " + c.q1 + ", median " + c.med + " (the red line), Q3 " + c.q3 + ", maximum " + c.max + ".", "Mínimo " + c.min + ", Q1 " + c.q1 + ", mediana " + c.med + " (la raya roja), Q3 " + c.q3 + ", máximo " + c.max + ".") + (cual === "rango" ? T(" Range = maximum − minimum = ", " Rango = máximo − mínimo = ") + res + "." : "") + (cual === "iqr" ? " IQR = Q3 − Q1 = " + res + "." : "");
  return {enun: T("According to the plot, what is " + NOMBRE5[cual] + "?", "Según el diagrama, ¿cuánto vale " + NOMBRE5[cual] + "?") + cajaSVG([{c: c}], T("Box plot to read: minimum ", "Diagrama de caja para leer: mínimo ") + c.min + ", Q1 " + c.q1 + T(", median ", ", mediana ") + c.med + ", Q3 " + c.q3 + T(", maximum ", ", máximo ") + c.max + "."),
    opciones: o, correcta: "n" + res, porClave: {}, pista: T("Left to right: minimum, Q1 (left edge of the box), median (red line), Q3 (right edge), maximum.", "De izquierda a derecha: mínimo, Q1 (borde izquierdo de la caja), mediana (raya roja), Q3 (borde derecho), máximo.") + (cual === "rango" ? T(" The range is max − min.", " El rango es máx − mín.") : "") + (cual === "iqr" ? T(" The IQR is Q3 − Q1.", " El IQR es Q3 − Q1.") : ""), bien: exp, mal: exp};
}

/* MODULE 3 · IQR versus range */
var IQ_BASE = [12, 15, 18, 20, 22, 25, 27, 30];
function pintaIQ(){
  var X = +$("iq-max").value, d = IQ_BASE.concat([X]), c = cinco(d);
  $("iq-val").textContent = X; $("iq-datos").textContent = listaN(d);
  $("iq-svg").innerHTML = cajaSVG([{c: c}], T("Box plot with maximum ", "Diagrama de caja con máximo ") + X, {lo: 10, hi: 120, rotulos: true});
  $("iq-salida").innerHTML = '<div class="linea">' + T("Range = ", "Rango = ") + X + " − " + c.min + " = <strong>" + (X - c.min) + "</strong>" + (X > 40 ? T(": it changes with the extreme value.", ": cambia con el dato extremo.") : ".") + "</div>" +
    '<div class="linea">IQR = ' + nm(c.q3) + " − " + nm(c.q1) + " = <strong>" + nm(c.q3 - c.q1) + "</strong>" + T(": it does not change, because it only looks at the middle 50%.", ": no cambia, porque solo mira el 50% central.") + "</div>";
}
function genIQR(){
  var tp = aleatorio(1, 3);
  if (tp === 1){ var a = 5 * aleatorio(1, 10), b = a + 5 * aleatorio(2, 10), o = [{html: String(b - a), clave: "n" + (b - a)}, {html: String(a + b), clave: "n" + (a + b)}, {html: String(b), clave: "n" + b}, {html: String((a + b) / 2), clave: "n" + (a + b) / 2}], pc = {};
    pc["n" + (a + b)] = T("You added. The IQR is a difference.", "Sumó. El IQR es una resta."); pc["n" + b] = T("That is Q3. Subtract Q1 from it.", "Ese es Q3. Réstele Q1."); pc["n" + (a + b) / 2] = T("That is the number halfway between them, not the IQR.", "Ese es el número que está a la mitad, no el IQR.");
    return {enun: T("If Q1 = " + a + " and Q3 = " + b + ", what is the IQR?", "Si Q1 = " + a + " y Q3 = " + b + ", ¿cuánto vale el IQR?"), opciones: o, correcta: "n" + (b - a), porClave: pc, pista: "IQR = Q3 − Q1.", bien: "IQR = " + b + " − " + a + " = " + (b - a) + ".", mal: "IQR = Q3 − Q1 = " + b + " − " + a + " = " + (b - a) + "."}; }
  if (tp === 2){
    var pr = elige([[T("between Q1 and Q3", "entre Q1 y Q3"), 50], [T("above the median", "por encima de la mediana"), 50], [T("below Q1", "por debajo de Q1"), 25], [T("above Q3", "por encima de Q3"), 25], [T("between the minimum and Q3", "entre el mínimo y Q3"), 75], [T("between the median and Q3", "entre la mediana y Q3"), 25], [T("between Q1 and the maximum", "entre Q1 y el máximo"), 75]]);
    var o2 = [25, 50, 75, 100].map(function(p){ return {html: p + "%", clave: "p" + p}; });
    return {enun: T("What percent of the data is " + pr[0] + "?", "¿Qué porcentaje de los datos queda " + pr[0] + "?"), opciones: o2, correcta: "p" + pr[1], porClave: {}, pista: T("Count the parts: each one holds 25%.", "Cuente las zonas: cada una tiene el 25%."),
      bien: T("Each part of the plot holds 25%: " + pr[0] + " there " + (pr[1] === 25 ? "is 1 part" : "are " + (pr[1] / 25) + " parts") + ". Total: " + pr[1] + "%.", "Cada zona del diagrama tiene el 25%: " + pr[0] + " hay " + (pr[1] / 25) + (pr[1] === 25 ? " zona." : " zonas.") + " Total: " + pr[1] + "%."), mal: T("Each of the four parts holds 25% of the data; " + pr[0] + " is " + pr[1] + "%.", "Cada una de las cuatro zonas contiene el 25% de los datos; " + pr[0] + " queda el " + pr[1] + "%.")}; }
  return {enun: T("One box is wider than another. That shows…", "Una caja más ancha que otra indica…"), opciones: [{html: T("More variability in the middle 50%", "Más variabilidad en el 50% central"), clave: "v"}, {html: T("Less variability", "Menos variabilidad"), clave: "m"}, {html: T("A higher median", "Una mediana mayor"), clave: "med"}, {html: T("More data", "Más datos"), clave: "d"}], correcta: "v",
    porClave: {d: T("The width does not depend on how many data there are: each part always holds 25%.", "El ancho no depende de cuántos datos hay: cada zona tiene siempre el 25%."), med: T("The width shows spread, not the center.", "El ancho muestra la dispersión, no el centro.")}, pista: T("The width of the box is the IQR.", "El ancho de la caja es el IQR."),
    bien: T("The width of the box is the IQR: it measures the spread of the middle 50%.", "El ancho de la caja es el IQR: mide la dispersión del 50% central."), mal: T("The width of the box is the IQR: a wider box means more spread-out data.", "El ancho de la caja es el IQR: una caja más ancha significa datos más dispersos.")};
}

/* MODULE 4 · Outliers */
function datosConAtipico(){
  var d = datosAzar(aleatorio(9, 12), 20, 45), c = cinco(d), L = limites(c);
  if (Math.random() < 0.8) d.push(Math.ceil(L.sup) + aleatorio(3, 20));
  if (Math.random() < 0.3) d.push(Math.max(0, Math.floor(L.inf) - aleatorio(3, 10)));
  return d;
}
var AT_COLA = [[10, 25, 30, 35, 40, 45, 50, 55, 60, 120]];
function pintaAT(d){
  var c = cinco(d), L = limites(c), o = c.o, at = o.filter(function(v){ return v < L.inf || v > L.sup; }), ok = o.filter(function(v){ return v >= L.inf && v <= L.sup; });
  $("at-datos").innerHTML = o.map(function(v){ return '<span class="dato' + ((v < L.inf || v > L.sup) ? " atip" : "") + '">' + nm(v) + "</span>"; }).join("");
  $("at-voz").textContent = T("Data: ", "Datos: ") + listaN(o) + ".";
  $("at-svg").innerHTML = cajaSVG([{c: c, atip: at, bigMin: ok[0], bigMax: ok[ok.length - 1]}], T("Box plot with ", "Diagrama de caja con ") + (at.length ? T("outliers ", "valores atípicos ") + listaN(at) : T("no outliers", "ningún valor atípico")));
  $("at-salida").innerHTML = '<div class="linea">Q1 = ' + nm(c.q1) + ", Q3 = " + nm(c.q3) + ", IQR = " + nm(L.iqr) + T(", and 1.5 × IQR = ", ", y 1.5 × IQR = ") + nm(1.5 * L.iqr) + ".</div>" +
    '<div class="linea">' + T("Lower limit: ", "Límite inferior: ") + nm(c.q1) + " − " + nm(1.5 * L.iqr) + " = <strong>" + nm(L.inf) + "</strong>. " + T("Upper limit: ", "Límite superior: ") + nm(c.q3) + " + " + nm(1.5 * L.iqr) + " = <strong>" + nm(L.sup) + "</strong>.</div>" +
    '<div class="linea veredicto">' + (at.length ? T("Outliers: " + listaN(at) + ", outside the limits.", "Valores atípicos: " + listaN(at) + ", fuera de los límites.") : T("No value is outside the limits: there are no outliers.", "Ningún dato queda fuera de los límites: no hay valores atípicos.")) + "</div>";
}
function nuevoAT(){ pintaAT(AT_COLA.length ? AT_COLA.shift() : datosConAtipico()); }
function genLimite(){
  var q1 = 2 * aleatorio(5, 30), q3 = q1 + 2 * aleatorio(3, 20), iqr = q3 - q1, sup = Math.random() < 0.6, res = sup ? q3 + 1.5 * iqr : q1 - 1.5 * iqr;
  var pistas = [{v: sup ? q3 + iqr : q1 - iqr, msg: T("You forgot to multiply the IQR by 1.5.", "Faltó multiplicar el IQR por 1.5.")}, {v: sup ? q1 + 1.5 * iqr : q3 - 1.5 * iqr, msg: sup ? T("The upper limit starts from Q3.", "El límite superior se calcula desde Q3.") : T("The lower limit starts from Q1.", "El límite inferior se calcula desde Q1.")}, {v: 1.5 * iqr, msg: sup ? T("That is 1.5 × IQR: add it to Q3.", "Ese es 1.5 × IQR: falta sumárselo a Q3.") : T("That is 1.5 × IQR: subtract it from Q1.", "Ese es 1.5 × IQR: falta restárselo a Q1.")}];
  return {enun: T("With Q1 = " + q1 + " and Q3 = " + q3 + ", what is the " + (sup ? "upper" : "lower") + " limit for outliers?", "Con Q1 = " + q1 + " y Q3 = " + q3 + ", ¿cuál es el límite " + (sup ? "superior" : "inferior") + " para los valores atípicos?"),
    solucion: "IQR = " + q3 + " − " + q1 + " = " + iqr + "; 1.5 × " + iqr + " = " + nm(1.5 * iqr) + "; " + (sup ? q3 + " + " + nm(1.5 * iqr) : q1 + " − " + nm(1.5 * iqr)) + " = " + nm(res) + ".",
    evalua: function(v){ var r = evaluaDec(v, res, pistas); if (r.estado === "mal" && !pistas.some(function(p){ return p.msg === r.msg; })) r.msg = sup ? T("Upper limit = Q3 + 1.5 × IQR.", "Límite superior = Q3 + 1.5 × IQR.") : T("Lower limit = Q1 − 1.5 × IQR.", "Límite inferior = Q1 − 1.5 × IQR."); return r; }};
}

/* MODULE 5 · Comparing two groups */
function genComparar(){
  var A = cincoMultiplos(), B2 = cincoMultiplos(), tp = aleatorio(1, 4), pregunta, va, vb, bien, pista;
  if (tp === 1){ pregunta = T("Which group has the higher median?", "¿Qué grupo tiene la mediana más alta?"); va = A.med; vb = B2.med; bien = T("Median of A: " + A.med + "; of B: " + B2.med + ".", "Mediana de A: " + A.med + "; de B: " + B2.med + "."); pista = T("Compare the red lines.", "Compare las rayas rojas."); }
  else if (tp === 2){ pregunta = T("Which group has more variability in the middle 50% (a larger IQR)?", "¿Qué grupo tiene mayor variabilidad en el 50% central (mayor IQR)?"); va = A.q3 - A.q1; vb = B2.q3 - B2.q1; bien = T("IQR of A: ", "IQR de A: ") + A.q3 + " − " + A.q1 + " = " + va + T("; of B: ", "; de B: ") + B2.q3 + " − " + B2.q1 + " = " + vb + "."; pista = T("Compare the widths of the boxes.", "Compare el ancho de las cajas."); }
  else if (tp === 3){ pregunta = T("Which group has the greater range?", "¿Qué grupo tiene el mayor rango?"); va = A.max - A.min; vb = B2.max - B2.min; bien = T("Range of A: " + va + "; of B: " + vb + ".", "Rango de A: " + va + "; de B: " + vb + "."); pista = T("The range goes from the end of one whisker to the end of the other.", "El rango va del extremo de un bigote al extremo del otro."); }
  else { pregunta = T("Which group is more consistent (its middle data are closer together)?", "¿Qué grupo es más consistente (sus datos centrales están más juntos)?"); va = -(A.q3 - A.q1); vb = -(B2.q3 - B2.q1); bien = T("The more consistent group has the narrower box. IQR of A: " + (-va) + "; of B: " + (-vb) + ".", "El más consistente tiene la caja más angosta. IQR de A: " + (-va) + "; de B: " + (-vb) + "."); pista = T("Look for the narrower box.", "Busque la caja más angosta."); }
  var cl = va > vb ? "A" : (vb > va ? "B" : "=");
  return {enun: pregunta + cajaSVG([{nombre: "A", c: A, color: "#37474f"}, {nombre: "B", c: B2, color: "#6a1b9a", relleno: "#f3e5f5"}], T("Two box plots on the same scale. Group A: minimum ", "Dos diagramas de caja sobre la misma escala. Grupo A: mínimo ") + A.min + ", Q1 " + A.q1 + T(", median ", ", mediana ") + A.med + ", Q3 " + A.q3 + T(", maximum ", ", máximo ") + A.max + T(". Group B: minimum ", ". Grupo B: mínimo ") + B2.min + ", Q1 " + B2.q1 + T(", median ", ", mediana ") + B2.med + ", Q3 " + B2.q3 + T(", maximum ", ", máximo ") + B2.max + "."),
    opciones: [{html: T("Group A", "El grupo A"), clave: "A"}, {html: T("Group B", "El grupo B"), clave: "B"}, {html: T("Both are the same", "Los dos por igual"), clave: "="}], correcta: cl, porClave: {}, pista: pista, bien: bien, mal: bien};
}

/* Start */
var CVS = pasoAPaso("cv", []);
$("cv-nuevo").addEventListener("click", nuevoCV); nuevoCV();
creaPracticaLibre("p1", genCinco);
[0, 1, 2, 3, 4].forEach(function(i){ $("cd-" + i).addEventListener("input", pintaCD); }); pintaCD();
OMR("p2", genLeer);
$("iq-max").addEventListener("input", pintaIQ); pintaIQ();
OMR("p3", genIQR);
$("at-nuevo").addEventListener("click", nuevoAT); nuevoAT();
creaPracticaLibre("p4", genLimite);
OMR("p5", genComparar);
'''

def practica_pagina():
    n = N
    def libre(pid, tit, et, nota):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota}</p>\n        <div class="fila-btn">', 1)
    campos = "".join(f'<div class="campo"><label for="cd-{i}">{et}</label><input type="text" inputmode="decimal" class="corto" id="cd-{i}" value="{v}"></div>'
                     for i, (et, v) in enumerate(((t("Minimum", "Mínimo"), 5), ("Q1", 25), (t("Median", "Mediana"), 40), ("Q3", 55), (t("Maximum", "Máximo"), 80))))
    mods = [
     (t("five-values", "cinco-valores"), t("The five key values", "Los cinco valores clave"),
      f'''      <p>{t("A box plot summarizes a data set with five numbers: the <strong>minimum</strong>, the <strong>first quartile</strong> (Q1), the <strong>median</strong> (Q2), the <strong>third quartile</strong> (Q3), and the <strong>maximum</strong>. The quartiles split the ordered data into four parts with 25% of the data each.", "Un diagrama de caja resume un conjunto de datos con cinco números: el <strong>mínimo</strong>, el <strong>primer cuartil</strong> (Q1), la <strong>mediana</strong> (Q2), el <strong>tercer cuartil</strong> (Q3) y el <strong>máximo</strong>. Los cuartiles dividen los datos ordenados en cuatro partes con el 25% de los datos cada una.")}</p>
      <h3>{t("Find the five values step by step", "Encuentre los cinco valores paso a paso")}</h3>
      <div class="panel">
        <p class="enun"><strong>{t("Data:", "Datos:")}</strong> <span id="cv-datos"></span></p>
        <div class="fila-btn"><button type="button" class="btn" id="cv-sig"></button><button type="button" class="btn-sec" id="cv-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="cv-nuevo">{t("Other data", "Otros datos")}</button></div>
      </div>
      <div class="pasos" id="cv-pasos" aria-live="polite"></div>
      <div class="caja-tip">{t("<strong>Odd number of data:</strong> the median is the middle value and does not go into either half. <strong>Even number:</strong> the median is the average of the two middle values, and each half keeps half of the data.", "<strong>Cantidad impar de datos:</strong> la mediana es el dato central y no entra en ninguna de las dos mitades. <strong>Cantidad par:</strong> la mediana es el promedio de los dos centrales, y cada mitad se queda con la mitad de los datos.")}</div>
{libre("p1", t("Practice: find the value asked for", "Practique: halle el valor que se pide"), t("Value", "Valor"), t("Type the number; it can be a decimal, like 12.5.", "Escriba el número; puede ser decimal, como 12.5."))}'''),
     (t("build", "construir"), t("Building the plot", "Construir el diagrama"),
      f'''      <p>{t("With the five values you draw the box: it goes from Q1 to Q3, with a line at the median, and the whiskers reach the minimum and the maximum. Type or change the five values and watch the plot take shape.", "Con los cinco valores se dibuja la caja: va de Q1 a Q3, con una raya en la mediana, y los bigotes llegan hasta el mínimo y el máximo. Escriba o cambie los cinco valores y mire cómo se forma.")}</p>
      <div class="panel"><div class="campos">{campos}</div></div>
      <p class="caja-aviso" id="cd-aviso" role="alert"></p>
      <div id="cd-svg"></div>
{n3.salida("cd-salida")}
{B.om("p2", t("Practice: read the plot", "Practique: lea el diagrama"))}'''),
     ("iqr", t("The interquartile range", "El rango intercuartílico"),
      f'''      <p>{t("The interquartile range measures how spread out the middle half of the data is. It is the width of the box:", "El rango intercuartílico mide qué tan dispersa está la mitad central de los datos. Es el ancho de la caja:")}</p>
{n3.formula("IQR = Q3 − Q1")}
      <h3>{t("What changes it and what does not?", "¿Qué le afecta y qué no?")}</h3>
      <p>{t("Move the largest value in the set. Watch what happens to the range (max − min) and to the IQR.", "Mueva el dato más grande del conjunto. Observe qué pasa con el rango (máximo − mínimo) y con el IQR.")}</p>
      <div class="panel">
        <p><strong>{t("Data:", "Datos:")}</strong> <span id="iq-datos"></span></p>
        <div class="campo"><label for="iq-max">{t("Largest value:", "Valor del dato más grande:")} <span id="iq-val"></span></label><input type="range" id="iq-max" min="30" max="120" value="40"></div>
      </div>
      <div id="iq-svg"></div>
{n3.salida("iq-salida")}
{B.om("p3", t("Practice: IQR and percents", "Practique: IQR y porcentajes"))}'''),
     (t("outliers", "atipicos"), t("Outliers", "Valores atípicos"),
      f'''      <p>{t("An <strong>outlier</strong> is a value far away from the rest. The most common rule: it is an outlier if it is more than 1.5 × IQR above Q3 or below Q1.", "Un <strong>valor atípico</strong> es un dato muy alejado del resto. La regla más usada: es atípico si queda más allá de 1.5 × IQR por encima de Q3 o por debajo de Q1.")}</p>
{n3.formula(t("lower limit = Q1 − 1.5 × IQR &nbsp;&nbsp;&nbsp; upper limit = Q3 + 1.5 × IQR", "límite inferior = Q1 − 1.5 × IQR &nbsp;&nbsp;&nbsp; límite superior = Q3 + 1.5 × IQR"))}
      <h3>{t("Outlier detector", "Detector de atípicos")}</h3>
      <div class="panel">
        <p><strong>{t("Ordered data:", "Datos ordenados:")}</strong></p>
        <div class="datos" id="at-datos" aria-hidden="true"></div>
        <p class="sr-only" id="at-voz"></p>
        <div class="fila-btn"><button type="button" class="btn-sec" id="at-nuevo">{t("Other data", "Otros datos")}</button></div>
      </div>
      <div id="at-svg"></div>
{n3.salida("at-salida")}
      <div class="caja-tip">{t("In the plot, an outlier is marked with a separate point, and the whisker only reaches the last value that is not an outlier.", "En el diagrama, un valor atípico se marca con un punto aparte y el bigote llega solo hasta el último dato que no es atípico.")}</div>
{libre("p4", t("Practice: find the limit", "Practique: calcule el límite"), t("Limit", "Límite"), t("Type the number; it can be a decimal or negative.", "Escriba el número; puede ser decimal o negativo."))}'''),
     (t("compare", "comparar"), t("Reading and comparing", "Interpretar y comparar"),
      f'''      <p>{t("Two plots on the same scale let you compare groups at a glance: the center (the median), the spread (the width of the box and the range), and the shape (whether the box or a whisker is stretched to one side).", "Dos diagramas sobre la misma escala permiten comparar grupos de un vistazo: el centro (la mediana), la dispersión (el ancho de la caja y el rango) y la forma (si la caja o un bigote está estirado hacia un lado).")}</p>
{B.om("p5", t("Practice: compare the two groups", "Practique: compare los dos grupos"))}
      <div class="caja-tip">{t("<strong>Median is not mean:</strong> the line in the box is the median. A box plot does not show the mean.", "<strong>Mediana no es media:</strong> la raya de la caja es la mediana. El diagrama de caja no muestra el promedio.")}</div>''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Diagramas de caja y bigotes")
