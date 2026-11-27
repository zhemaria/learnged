"""LearnGED · Estudios sociales · Lección 2.2 · Medidas de tendencia central (EN/ES).
Fuente: sociales/soc-2-2.html. Histogramas con ciencia.grafica; diagramas de caja propios.
Uso: python3 tools/build_soc_2_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, cita

N = "2-2"
BA = [28, 31, 33, 35, 38, 40, 40, 45, 48, 52, 600]
BB = [34, 36, 38, 39, 40, 41, 42, 43, 44, 46, 48]
COM = [22, 24, 26, 27, 29, 30, 31, 33, 35, 36, 37]
TEC = [38, 42, 45, 50, 52, 55, 60, 65, 70, 80, 88]
F = 'font-family="Segoe UI, Arial, sans-serif"'


def titulo():
    return t("Measures of center in population and economic data", "Medidas de tendencia central en datos demográficos y económicos")


def cinco(v):
    o = sorted(v)
    m = lambda a: (a[len(a) // 2] if len(a) % 2 else (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2)
    h = len(o) // 2
    return o[0], m(o[:h]), m(o), m(o[-h:]), o[-1]


assert sum(BA) / 11 == 90 and sum(BB) / 11 == 41
assert cinco(COM) == (22, 26, 30, 35, 37) and cinco(TEC) == (38, 45, 55, 70, 88)


def svg_cajas():
    ml, W = 150, 520
    X = lambda v: ml + (v - 20) / (90 - 20) * W
    aria = t("Two box plots of yearly salaries in thousands of dollars, on the same scale from 20 to 90. Retail: minimum 22, first quartile 26, median 30, third quartile 35, maximum 37; a short, narrow box. Technology: minimum 38, first quartile 45, median 55, third quartile 70, maximum 88; a much wider box.",
             "Dos diagramas de caja de salarios anuales en miles de dólares, en la misma escala de 20 a 90. Comercio minorista: mínimo 22, primer cuartil 26, mediana 30, tercer cuartil 35, máximo 37; una caja corta y estrecha. Tecnología: mínimo 38, primer cuartil 45, mediana 55, tercer cuartil 70, máximo 88; una caja mucho más ancha.")
    s = [f'<svg class="diagrama" style="max-width:720px" viewBox="0 0 720 250" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">']
    for v in range(20, 91, 10):
        s.append(f'<line x1="{X(v):.1f}" y1="20" x2="{X(v):.1f}" y2="190" stroke="#eef0f2"/><text x="{X(v):.1f}" y="212" text-anchor="middle" {F} font-size="13" fill="#3d4753">{v}</text>')
    s.append(f'<line x1="{ml}" y1="192" x2="{ml + W}" y2="192" stroke="#1a2330" stroke-width="1.5"/>')
    s.append(f'<text x="{ml + W / 2}" y="240" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Yearly salary (thousands of $)", "Salario anual (miles de $)")}</text>')
    for y, nom, d, c in ((70, t("Retail", "Comercio minorista"), cinco(COM), "#7a4a2e"), (145, t("Technology", "Tecnología"), cinco(TEC), "#2a7f86")):
        mn, q1, me, q3, mx = d
        s.append(f'<text x="{ml - 12}" y="{y + 5}" text-anchor="end" {F} font-size="14" font-weight="700" fill="#1a2330">{nom}</text>')
        s.append(f'<line x1="{X(mn):.1f}" y1="{y}" x2="{X(q1):.1f}" y2="{y}" stroke="{c}" stroke-width="2.5"/><line x1="{X(q3):.1f}" y1="{y}" x2="{X(mx):.1f}" y2="{y}" stroke="{c}" stroke-width="2.5"/>')
        for v in (mn, mx):
            s.append(f'<line x1="{X(v):.1f}" y1="{y - 12}" x2="{X(v):.1f}" y2="{y + 12}" stroke="{c}" stroke-width="2.5"/>')
        s.append(f'<rect x="{X(q1):.1f}" y="{y - 20}" width="{X(q3) - X(q1):.1f}" height="40" fill="{c}" fill-opacity=".18" stroke="{c}" stroke-width="2.5"/>')
        s.append(f'<line x1="{X(me):.1f}" y1="{y - 20}" x2="{X(me):.1f}" y2="{y + 20}" stroke="{c}" stroke-width="4"/>')
    s.append("</svg>")
    return "".join(s)


def histo(barras, aria):
    spec = {"tipo": "barras", "xEtq": t("Yearly household income (thousands of $)", "Ingreso anual por hogar (miles de $)"), "yEtq": t("Number of households", "Número de hogares"), "barras": barras}
    return C.grafica(spec, aria, ancho=560, alto=300)


def lista(v):
    return '<p class="datos-lista">' + " · ".join(str(x) for x in v) + "</p>"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Three measures describe the <strong>center</strong> of a set of data. The fourth describes how <strong>spread out</strong> it is.", "Tres medidas describen el <strong>centro</strong> de un conjunto de datos. La cuarta describe cuánto se <strong>separan</strong>.")}</p>
{C.tabla(t("The four measures and how to find them", "Las cuatro medidas y cómo se obtienen"), [t("Measure", "Medida"), t("What it is", "Qué es"), t("How to find it", "Cómo se obtiene")],
  [[t("Mean (average)", "Media (promedio)"), t("An equal share", "El reparto por igual"), t("Add all the values and divide by how many there are.", "Se suman todos los valores y se divide entre cuántos son.")],
   [t("Median", "Mediana"), t("The middle value", "El valor de en medio"), t("Put the values in order and take the one in the middle. If there is an even number of values, take the mean of the two middle ones.", "Se ordenan de menor a mayor y se toma el del centro. Si son pares, la media de los dos centrales.")],
   [t("Mode", "Moda"), t("The most frequent value", "El valor que más se repite"), t("Count which value appears most. There may be none, or more than one.", "Se cuenta cuál aparece más veces. Puede no haber ninguna, o haber varias.")],
   [t("Range", "Rango"), t("How far apart the values are", "Cuánto se separan"), t("Largest value minus smallest value.", "El valor mayor menos el menor.")]])}
{C.caja("ojo", t("Always put the data in order first", "Ordenar primero, siempre"), "<p>" + t("The median does not exist until the data are in order. It is the most common mistake and the easiest to avoid: if you did not order the list, the number in the middle is not the median.", "La mediana no existe hasta que los datos están ordenados. Es el error más común y el más fácil de evitar: si no ordenó, el número del centro no es la mediana.") + "</p>")}
{C.ejemplo(t("Example · The ten values 12, 15, 15, 18, 22, 25, 25, 25, 31, 40", "Ejemplo · Los diez valores 12, 15, 15, 18, 22, 25, 25, 25, 31, 40"),
  [("1", t("<strong>Mean:</strong> the sum is 228, and 228 ÷ 10 = 22.8.", "<strong>Media:</strong> la suma es 228, y 228 ÷ 10 = 22.8.")),
   ("2", t("<strong>Median:</strong> ten values, so take the 5th and 6th: 22 and 25. (22 + 25) ÷ 2 = 23.5.", "<strong>Mediana:</strong> diez valores, así que se toman el 5.º y el 6.º: 22 y 25. (22 + 25) ÷ 2 = 23.5.")),
   ("3", t("<strong>Mode:</strong> 25 appears three times.", "<strong>Moda:</strong> 25 aparece tres veces.")),
   ("4", t("<strong>Range:</strong> 40 − 12 = 28.", "<strong>Rango:</strong> 40 − 12 = 28."))],
  t("Three different “centers” for the same data: 22.8, 23.5, and 25. None of them is wrong.", "Tres «centros» distintos para los mismos datos: 22.8, 23.5 y 25. Ninguno está mal."))}
{C.enlace(N, t("calculate", "calcular"), t("Calculate the four measures", "Calcule las cuatro medidas"), t("A new data set every time, with a hint if you mix up the measures.", "Un conjunto nuevo cada vez, con una pista si confunde las medidas."))}"""

    s2 = f"""<p>{t("Here are the yearly incomes of eleven households in each of two neighborhoods, in thousands of dollars, already in order. Illustrative data.", "Estos son los ingresos anuales de once hogares de cada uno de dos barrios, en miles de dólares, ya ordenados. Datos ilustrativos.")}</p>
<p><strong>{t("Neighborhood A", "Barrio A")}</strong></p>{lista(BA)}
<p><strong>{t("Neighborhood B", "Barrio B")}</strong></p>{lista(BB)}
{C.tabla(t("The four measures in the two neighborhoods, in thousands of dollars", "Las cuatro medidas en los dos barrios, en miles de dólares"), [t("Measure", "Medida"), t("Neighborhood A", "Barrio A"), t("Neighborhood B", "Barrio B")],
  [[t("Mean", "Media"), "90", "41"], [t("Median", "Mediana"), "40", "41"], [t("Mode", "Moda"), "40", t("none", "no hay")], [t("Range", "Rango"), "572", "14"]])}
<p>{t("Look at the mean row. Neighborhood A comes out at 90 thousand and B at 41: it looks as if people in A earn more than twice as much. Now look at the median: 40 and 41. Almost the same.", "Mire la fila de la media. El Barrio A sale con noventa mil y el B con cuarenta y uno: parece que en el A se gana más del doble. Ahora mire la mediana: cuarenta y cuarenta y uno. Casi idénticas.")}</p>
<p>{t("Both rows are correct. The difference comes from a single household, the one with 600 thousand, which pulls the mean up and does not move the median. Ten of the eleven households in A earn 52 thousand or less. <strong>None earns 90.</strong>", "Las dos filas son correctas. La diferencia la produce un solo hogar, el de seiscientos mil, que arrastra la media y no mueve la mediana. Diez de los once hogares del Barrio A ganan cincuenta y dos mil o menos. <strong>Ninguno gana noventa.</strong>")}</p>
{C.caja("tip", t("Why it happens", "Por qué ocurre"), "<p>" + t("The mean shares equally: if we added up all the money in the neighborhood and split it among the eleven households, each would get 90 thousand. But nobody shares anything. The median only counts positions, so a huge value takes up one position, no more. <strong>An outlier moves the mean and leaves the median alone.</strong> And the range is the warning: a range of 572 against one of 14 means something in A is very far from the rest.", "La media reparte por igual: si sumásemos todo el dinero del barrio y lo dividiésemos entre los once hogares, tocarían noventa mil. Pero nadie reparte nada. La mediana solo cuenta posiciones, así que un valor enorme ocupa una posición, no más. <strong>Un valor atípico mueve la media y deja quieta la mediana.</strong> Y el rango es el aviso: un rango de 572 frente a uno de 14 significa que en el A hay algo muy separado del resto.") + "</p>")}
{P(t("Practice 1 · The outlier", "Práctica 1 · El valor atípico"), t("If the household with 600 earned 6,000 instead, what would happen to the median of Neighborhood A?", "Si el hogar de 600 pasara a ganar 6,000, ¿qué le ocurriría a la mediana del Barrio A?"),
   [t("It would rise a lot", "Subiría mucho"), t("It would rise a little", "Subiría un poco"), t("It would not change: it would still be 40", "No cambiaría: seguiría siendo 40")], 2,
   {0: t("The median counts positions, not amounts.", "La mediana cuenta posiciones, no cantidades."), 1: t("Is 6,000 still in the last position?", "¿Sigue estando 6,000 en la última posición?")}, t("The 6th value is still 40. The mean, however, would jump to about 489.", "El 6.º valor sigue siendo 40. La media, en cambio, saltaría a unos 489."))}
{P(t("Practice 2 · The warning sign", "Práctica 2 · La señal de aviso"), t("Which measure warns you that there may be an outlier?", "¿Qué medida avisa de que puede haber un valor atípico?"),
   [t("The range, when it is huge compared with the values in the middle", "El rango, cuando es enorme comparado con los valores del centro"), t("The mode", "La moda"), t("None: you must check the values one by one", "Ninguna: hay que mirar los datos uno a uno")], 0,
   {1: t("The mode only tells the most frequent value.", "La moda solo dice el valor más frecuente."), 2: t("One of the four measures does warn you.", "Una de las cuatro medidas sí avisa.")}, t("A range of 572 when the middle values are near 40 is a red flag.", "Un rango de 572 cuando los valores centrales rondan 40 es una señal de alarma."))}"""

    sim = histo([{"etq": e, "valor": v} for e, v in [("20–29", 2), ("30–39", 5), ("40–49", 9), ("50–59", 5), ("60–69", 2)]],
                t("Histogram with a symmetric shape: 2, 5, 9, 5, and 2 households in the income ranges 20–29, 30–39, 40–49, 50–59, and 60–69 thousand dollars.", "Histograma de forma simétrica: 2, 5, 9, 5 y 2 hogares en los tramos de ingreso de 20–29, 30–39, 40–49, 50–59 y 60–69 mil dólares."))
    ses = histo([{"etq": e, "valor": v} for e, v in [("20–39", 9), ("40–59", 7), ("60–79", 4), ("80–99", 2), ("100–119", 1), ("120+", 1)]],
                t("Histogram skewed to the right: 9, 7, 4, 2, 1, and 1 households in the income ranges 20–39, 40–59, 60–79, 80–99, 100–119, and 120 thousand dollars or more.", "Histograma sesgado a la derecha: 9, 7, 4, 2, 1 y 1 hogares en los tramos de ingreso de 20–39, 40–59, 60–79, 80–99, 100–119 y 120 mil dólares o más."))
    s3 = f"""<p>{t("No measure is better than the others. One fits the <strong>shape</strong> of the data, and to see the shape you draw a <strong>histogram</strong>: the values are split into ranges, and you count how many fall in each one.", "No hay una medida mejor que otra. Hay una que encaja con la <strong>forma</strong> de los datos, y para verla se dibuja un <strong>histograma</strong>: se reparten los valores en tramos y se cuenta cuántos caen en cada uno.")}</p>
<h3>{t("Symmetric", "Simétrica")}</h3>{sim}<p>{t("Most values gather in the middle and drop off evenly on both sides. The mean and the median almost match. Illustrative data.", "La mayoría se agrupa en el centro y baja de forma pareja a los dos lados. La media y la mediana casi coinciden. Datos ilustrativos.")}</p>
<h3>{t("Skewed to the right", "Sesgada a la derecha")}</h3>{ses}<p>{t("Most values gather on the left, and a long tail stretches toward high values. The tail pulls the mean above the median. Illustrative data.", "La mayoría se agrupa a la izquierda y una cola larga se estira hacia los valores altos. Esa cola arrastra la media por encima de la mediana. Datos ilustrativos.")}</p>
<p>{t("Incomes, almost everywhere in the world, have the second shape. That is why the U.S. Census Bureau and other agencies usually publish the <strong>median household income</strong>, not the mean: it describes the ordinary family better.", "Los ingresos, en casi cualquier lugar del mundo, tienen la segunda forma. Por eso la Oficina del Censo de los Estados Unidos y otros organismos suelen publicar el <strong>ingreso mediano por hogar</strong>, y no la media: describe mejor a la familia corriente.")}</p>
{C.tabla(t("Which measure to use", "Qué medida usar"), [t("If the data…", "Si los datos…"), t("Use", "Use"), t("Because", "Porque")],
  [[t("are symmetric, with no extreme values", "son simétricos, sin valores extremos"), t("the mean", "la media"), t("it uses all the information and matches the median", "usa toda la información y coincide con la mediana")],
   [t("have outliers or a long tail", "tienen valores atípicos o una cola larga"), t("the median", "la mediana"), t("a few extreme values cannot pull it", "unos pocos valores extremos no la arrastran")],
   [t("are categories, not numbers", "son categorías, no números"), t("the mode", "la moda"), t("it is the only one that works: you cannot average a color or a language", "es la única que funciona: no se puede promediar un color ni un idioma")]])}
{P(t("Practice 3 · Choose the measure", "Práctica 3 · Elija la medida"), t("You asked 200 people what their first language is. Which measure of center makes sense?", "Preguntó a doscientas personas cuál es su idioma materno. ¿Qué medida de centro tiene sentido?"),
   [t("The mean", "La media"), t("The median", "La mediana"), t("The mode", "La moda")], 2,
   {0: t("Can you add up languages?", "¿Se pueden sumar idiomas?"), 1: t("Can you put languages in order from smallest to largest?", "¿Se pueden ordenar idiomas de menor a mayor?")}, t("Only the mode works with categories: the most common language.", "Con categorías solo funciona la moda: el idioma más frecuente."))}
{C.enlace(N, t("choose", "elegir"), t("Which measure?", "¿Qué medida?"), t("Situations to decide among mean, median, and mode, and questions about outliers.", "Situaciones para decidir entre media, mediana y moda, y preguntas sobre valores atípicos."))}"""

    s4 = f"""<p>{t("A single number never describes a set of data. Five numbers almost always do.", "Un solo número nunca describe un conjunto. Cinco, casi siempre.")}</p>
{C.tabla(t("The five-number summary", "El resumen de cinco números"), [t("Number", "Número"), t("What it is", "Qué es")],
  [[t("Minimum", "Mínimo"), t("The lowest value.", "El valor más bajo.")], [t("First quartile (Q1)", "Primer cuartil (Q1)"), t("The median of the lower half. One quarter of the data are below it.", "La mediana de la mitad de abajo. Por debajo queda la cuarta parte de los datos.")],
   [t("Median", "Mediana"), t("The middle.", "El centro.")], [t("Third quartile (Q3)", "Tercer cuartil (Q3)"), t("The median of the upper half. Three quarters of the data are below it.", "La mediana de la mitad de arriba. Por debajo quedan tres cuartas partes de los datos.")],
   [t("Maximum", "Máximo"), t("The highest value.", "El valor más alto.")]])}
<p>{t("A <strong>box plot</strong> draws those five numbers. The box goes from Q1 to Q3 and holds the middle half of the data; the line inside is the median; the whiskers reach the minimum and the maximum. Below: yearly salaries of eleven workers in each of two sectors, in thousands of dollars. Illustrative data.", "El <strong>diagrama de caja</strong> dibuja esos cinco números. La caja va de Q1 a Q3 y contiene la mitad central de los datos; la raya de dentro es la mediana; los bigotes llegan al mínimo y al máximo. Abajo: salarios anuales de once trabajadores de cada uno de dos sectores, en miles de dólares. Datos ilustrativos.")}</p>
{svg_cajas()}
{C.tabla(t("Five-number summary of the two sectors, in thousands of dollars", "Resumen de cinco números de los dos sectores, en miles de dólares"), [t("Sector", "Sector"), t("Minimum", "Mínimo"), "Q1", t("Median", "Mediana"), "Q3", t("Maximum", "Máximo")],
  [[t("Retail", "Comercio minorista")] + [str(x) for x in cinco(COM)], [t("Technology", "Tecnología")] + [str(x) for x in cinco(TEC)]])}
{C.caja("tip", t("What a wide box tells you", "Lo que enseña una caja ancha"), "<p>" + t("It is not only that technology pays more. Its box is much wider: inside the same sector, salaries are very unequal. In retail almost everyone earns about the same. The width of the box (Q3 − Q1) is where the middle half of the people are. <strong>Two groups can have the same median and very different lives.</strong>", "Lo que hay que ver no es solo que tecnología pague más. Su caja es mucho más ancha: dentro del mismo sector, los salarios son muy desiguales. En el comercio minorista casi todos cobran parecido. La anchura de la caja (Q3 − Q1) es donde vive la mitad central de la gente. <strong>Dos grupos pueden tener la misma mediana y vidas muy distintas.</strong>") + "</p>")}
{C.caja("tip", t("With eleven values", "Con once valores"), "<p>" + t("Once the eleven values are in order, the median is the 6th, Q1 is the 3rd, and Q3 is the 9th.", "Con los once valores ordenados, la mediana es el 6.º, Q1 es el 3.º y Q3 es el 9.º.") + "</p>")}
{P(t("Practice 4 · Read the boxes", "Práctica 4 · Lea las cajas"), t("Does the best-paid retail worker earn more or less than the lowest-paid technology worker?", "El trabajador mejor pagado del comercio minorista, ¿gana más o menos que el peor pagado de tecnología?"),
   [t("Less: 37 against 38; the two ranges do not overlap", "Menos: 37 frente a 38; los dos rangos no se solapan"), t("More", "Más"), t("The same", "Lo mismo")], 0,
   {1: t("Compare the maximum of retail with the minimum of technology.", "Compare el máximo del comercio con el mínimo de tecnología."), 2: t("Look at the exact numbers.", "Mire las cifras exactas.")}, t("Retail maximum 37; technology minimum 38.", "Máximo del comercio, 37; mínimo de tecnología, 38."))}
{C.enlace(N, t("quartiles", "cuartiles"), t("Five-number summary", "Resumen de cinco números"), t("Find the median, Q1, or Q3 of a new list of eleven values each time.", "Encuentre la mediana, Q1 o Q3 de una lista nueva de once valores cada vez."))}"""

    s5 = f"""<p>{t("Go back to Neighborhood A. Mean 90, median 40. Both numbers are correct, and both describe the same neighborhood. Now picture two people who must speak about that neighborhood in public.", "Vuelva al Barrio A. Media noventa, mediana cuarenta. Las dos cifras son correctas y las dos describen el mismo barrio. Ahora imagine dos personas que tienen que hablar de ese barrio en público.")}</p>
{C.tabla(t("Two true statements about the same neighborhood", "Dos afirmaciones verdaderas sobre el mismo barrio"), [t("Who speaks", "Quién habla"), t("What they say", "Qué dice"), t("Why", "Por qué")],
  [[t("An official who wants to attract investment", "Un funcionario que quiere atraer inversión"), t("“The average household income here is 90 thousand dollars.”", "«El ingreso medio de los hogares aquí es de noventa mil dólares»."), t("The mean makes the neighborhood look prosperous.", "La media hace que el barrio parezca próspero.")],
   [t("A group asking for public aid", "Un grupo que pide ayuda pública"), t("“The median household income here is 40 thousand dollars.”", "«El ingreso mediano de los hogares aquí es de cuarenta mil dólares»."), t("The median makes the need visible.", "La mediana hace visible la necesidad.")]])}
{C.caja("ojo", t("This is Lesson 1.3 again", "Esto es la Lección 1.3 otra vez"), "<p>" + t("Neither one lies, and neither one made a mistake in the arithmetic. One chose the mean and the other the median, just as the two weeklies of 1905 chose which facts to tell. Bias does not need lies: choosing is enough. The defense is always the same question: <strong>why this measure and not the other?</strong> When someone publishes a mean without the median, or the other way around, ask what looks better with the one they chose, and what stays hidden.", "Ninguno miente y ninguno se equivocó en una cuenta. Uno eligió la media y el otro la mediana, igual que los dos semanarios de 1905 eligieron qué hechos contar. El sesgo no necesita mentiras: le basta con elegir. La defensa es siempre la misma pregunta: <strong>¿por qué esta medida y no la otra?</strong> Cuando alguien publica una media sin la mediana, o al revés, pregúntese qué se ve mejor con la que eligió, y qué queda tapado.") + "</p>")}"""

    G = lambda *a: C.ged_item(P, *a)
    tabla_g = C.tabla(t("Yearly salaries of 7 workers at a small company, in thousands of dollars", "Salarios anuales de 7 trabajadores de una empresa pequeña, en miles de dólares"),
                      [t("Worker", "Trabajador"), "A", "B", "C", "D", "E", "F", t("Owner", "Dueña")], [[t("Salary", "Salario"), "31", "33", "33", "35", "38", "40", "250"]])
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK). You may use the calculator.",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SSP.11.a", "1", tabla_g + t("What is the <strong>median</strong> salary at this company?", "¿Cuál es el salario <strong>mediano</strong> de esta empresa?"),
   [t("$35 thousand", "35 mil dólares"), t("$65.7 thousand", "65.7 mil dólares"), t("$33 thousand", "33 mil dólares"), t("$219 thousand", "219 mil dólares")], 0,
   {1: t("That is the mean.", "Esa es la media."), 2: t("That is the mode.", "Esa es la moda."), 3: t("That is the range.", "Ese es el rango.")},
   t("Seven values in order; the 4th is 35.", "Siete valores ordenados; el 4.º es 35."))}
{G(2, "SSP.11.a", "2", tabla_g + t("The owner says: “The average salary here is about $66 thousand.” Why is this statement misleading?", "La dueña dice: «El salario medio aquí es de unos 66 mil dólares». ¿Por qué es engañosa esta afirmación?"),
   [t("Her own salary pulls the mean up; six of the seven people earn $40 thousand or less.", "Su propio salario sube la media; seis de las siete personas ganan 40 mil dólares o menos."), t("The mean was calculated wrong.", "La media está mal calculada."), t("The mode is higher than the mean.", "La moda es mayor que la media."), t("Salaries cannot be averaged.", "Los salarios no se pueden promediar.")], 0,
   {1: t("460 ÷ 7 ≈ 65.7: the arithmetic is right.", "460 ÷ 7 ≈ 65.7: la cuenta está bien."), 2: t("The mode is 33, much lower.", "La moda es 33, mucho más baja."), 3: t("They can; the question is whether the mean is typical.", "Se puede; la cuestión es si la media es típica.")},
   t("One outlier ($250 thousand) moves the mean; the median ($35 thousand) describes the typical worker better.", "Un valor atípico (250 mil) mueve la media; la mediana (35 mil) describe mejor al trabajador típico."))}
{G(3, "SSP.6.b", "2", t("<em>Look at the box plots in section 4.</em><br>Which statement is supported?", "<em>Observe los diagramas de caja de la sección 4.</em><br>¿Qué afirmación está sostenida?"),
   [t("Salaries vary much more within technology than within retail.", "Los salarios varían mucho más dentro de tecnología que dentro del comercio minorista."), t("Every technology worker earns more than $55 thousand.", "Todos los trabajadores de tecnología ganan más de 55 mil dólares."), t("Retail workers are less skilled.", "Los trabajadores del comercio están menos capacitados."), t("The two sectors have the same median.", "Los dos sectores tienen la misma mediana.")], 0,
   {1: t("55 is the median: half earn less.", "55 es la mediana: la mitad gana menos."), 2: t("The graph shows salaries, not skills.", "La gráfica muestra salarios, no capacitación."), 3: t("30 and 55 are not the same.", "30 y 55 no son iguales.")},
   t("The technology box (45 to 70) is much wider than the retail box (26 to 35).", "La caja de tecnología (45 a 70) es mucho más ancha que la del comercio (26 a 35)."))}
{G(4, "SSP.11.a", "2", t("<em>A survey asked 50 workers how they get to work: car, bus, train, bicycle, or walking.</em><br>Which measure best describes the typical answer?", "<em>Una encuesta preguntó a 50 trabajadores cómo van al trabajo: auto, autobús, tren, bicicleta o a pie.</em><br>¿Qué medida describe mejor la respuesta típica?"),
   [t("The mode", "La moda"), t("The mean", "La media"), t("The median", "La mediana"), t("The range", "El rango")], 0,
   {1: t("You cannot add “bus” and “train.”", "No se puede sumar «autobús» y «tren»."), 2: t("These answers have no order from smallest to largest.", "Estas respuestas no tienen un orden de menor a mayor."), 3: t("The range needs numbers.", "El rango necesita números.")},
   t("With categories, only the mode works: the most common way to get to work.", "Con categorías solo funciona la moda: la forma más común de ir al trabajo."))}"""

    secciones = [
        ("s1", t("The four measures", "Las cuatro medidas"), s1),
        ("s2", t("When the mean misleads", "Cuando la media engaña"), s2),
        ("s3", t("The shape decides the measure", "La forma decide la medida"), s3),
        ("s4", t("The five-number summary and the box plot", "El resumen de cinco números y el diagrama de caja"), s4),
        ("s5", t("Mean or median: a one-sided choice", "Media o mediana: la elección interesada"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("By hand and with the calculator (20 minutes).", "A mano y con la calculadora (20 minutos)."), t("Calculate the four measures of Neighborhood B by hand, then check them with the calculator. <em>Check:</em> mean 41, median 41, no mode, range 14.", "Calcule a mano las cuatro medidas del Barrio B y después compruébelas con la calculadora. <em>Compruebe:</em> media 41, mediana 41, sin moda, rango 14.")),
        (t("Mean or median (25 minutes).", "Media o mediana (25 minutos)."), t("With the data of Neighborhood A, write two short paragraphs about the same neighborhood: one to attract investment and one to ask for public aid. You cannot invent or change any data; you can only choose which measure to use and which numbers to mention. <em>Check:</em> if you had to invent a fact, go back.", "Con los datos del Barrio A, escriba dos párrafos cortos sobre el mismo barrio: uno para atraer inversión y otro para pedir una ayuda pública. No puede inventar ni cambiar ningún dato; solo puede elegir qué medida usa y qué cifras menciona. <em>Compruebe:</em> si tuvo que inventar un dato, vuelva atrás.")),
        (t("Your own five-number summary (30 minutes).", "Su propio resumen de cinco números (30 minutos)."), t("Collect eleven real values: the prices of eleven grocery items, the ages of eleven people you know, or your travel time to work on eleven days. Put them in order, find the five-number summary, and draw the box by hand on graph paper. <em>Check:</em> Q1 is the 3rd value and Q3 the 9th.", "Reúna once datos reales: el precio de once artículos del supermercado, las edades de once personas conocidas o los minutos que tardó en llegar al trabajo once días. Ordénelos, saque el resumen de cinco números y dibuje la caja a mano en papel cuadriculado. <em>Compruebe:</em> Q1 es el 3.º valor y Q3 el 9.º.")),
    ]
    Q = t
    quiz = [
        (Q("To find the median, the first thing to do is…", "Para hallar la mediana, lo primero es…"), [Q("add all the values", "sumar todos los valores"), Q("put the data in order", "ordenar los datos"), Q("find the most frequent value", "buscar el que más se repite"), Q("subtract the smallest from the largest", "restar el menor del mayor")], 1,
         {0: Q("That is for the mean.", "Eso es para la media."), 2: Q("That is the mode.", "Eso es la moda."), 3: Q("That is the range.", "Eso es el rango.")}, Q("No order, no median.", "Sin orden no hay mediana.")),
        (Q("The set 12, 15, 15, 18, 22, 25, 25, 25, 31, 40 adds up to 228. Its mean is…", "El conjunto 12, 15, 15, 18, 22, 25, 25, 25, 31, 40 suma 228. Su media es…"), ["23.5", "22.8", "25", "28"], 1,
         {0: Q("That is the median.", "Esa es la mediana."), 2: Q("That is the mode.", "Esa es la moda."), 3: Q("That is the range.", "Ese es el rango.")}, Q("228 ÷ 10 = 22.8.", "228 ÷ 10 = 22.8.")),
        (Q("In that same set of ten values, the median is…", "En ese mismo conjunto de diez valores, la mediana es…"), ["22", "25", "23.5", "22.8"], 2,
         {0: Q("With an even count, average the two middle values.", "Con una cantidad par, se promedian los dos centrales."), 1: Q("25 is the mode.", "25 es la moda."), 3: Q("That is the mean.", "Esa es la media.")}, Q("(22 + 25) ÷ 2 = 23.5.", "(22 + 25) ÷ 2 = 23.5.")),
        (Q("The range of a set is found by…", "El rango de un conjunto se obtiene…"), [Q("adding the largest and smallest", "sumando el mayor y el menor"), Q("subtracting the smallest from the largest", "restando el menor del mayor"), Q("dividing the largest by the smallest", "dividiendo el mayor entre el menor"), Q("counting the values", "contando los valores")], 1,
         {0: Q("It measures distance, not a total.", "Mide distancia, no un total."), 2: Q("It is a difference.", "Es una diferencia."), 3: Q("That is how many, not how spread out.", "Eso es cuántos, no cuánto se separan.")}, Q("Largest − smallest.", "Mayor − menor.")),
        (Q("In Neighborhood A the mean is 90 and the median 40. The difference comes from…", "En el Barrio A la media es 90 y la mediana 40. La diferencia se debe a…"), [Q("a calculation mistake", "un error de cálculo"), Q("one household with a very high income that pulls the mean", "un hogar con un ingreso muy alto que arrastra la media"), Q("too few households", "que hay pocos hogares"), Q("a badly ordered list", "una lista mal ordenada")], 1,
         {0: Q("Both are correct.", "Las dos son correctas."), 2: Q("The same eleven households give a median of 40.", "Los mismos once hogares dan una mediana de 40."), 3: Q("The list is in order.", "La lista está ordenada.")}, Q("The 600 thousand household.", "El hogar de 600 mil.")),
        (Q("A very high outlier affects…", "Un valor atípico muy alto afecta…"), [Q("the mean, not the median", "a la media, no a la mediana"), Q("the median, not the mean", "a la mediana, no a la media"), Q("both equally", "a las dos por igual"), Q("neither", "a ninguna")], 0,
         {1: Q("The median counts positions.", "La mediana cuenta posiciones."), 2: Q("One moves a lot, the other hardly at all.", "Una se mueve mucho y la otra casi nada."), 3: Q("The mean moves.", "La media se mueve.")}, Q("The mean shares amounts; the median counts positions.", "La media reparte cantidades; la mediana cuenta posiciones.")),
        (Q("To describe the income of an ordinary family in a neighborhood, publish…", "Para describir el ingreso de una familia corriente de un barrio, se publica…"), [Q("the mean", "la media"), Q("the median", "la mediana"), Q("the range", "el rango"), Q("the maximum", "el máximo")], 1,
         {0: Q("Incomes have a long tail that pulls the mean.", "Los ingresos tienen una cola larga que arrastra la media."), 2: Q("The range is spread, not center.", "El rango es dispersión, no centro."), 3: Q("The maximum is one household.", "El máximo es un solo hogar.")}, Q("Incomes are skewed to the right.", "Los ingresos están sesgados a la derecha.")),
        (Q("In a distribution skewed to the right…", "En una distribución sesgada a la derecha…"), [Q("the mean is greater than the median", "la media es mayor que la mediana"), Q("the mean is less than the median", "la media es menor que la mediana"), Q("they are equal", "son iguales"), Q("there is no median", "no hay mediana")], 0,
         {1: Q("The tail is on the high side.", "La cola está del lado alto."), 2: Q("That is a symmetric shape.", "Eso es una forma simétrica."), 3: Q("There is always a median.", "Siempre hay mediana.")}, Q("The tail pulls the mean up.", "La cola arrastra la media hacia arriba.")),
        (Q("What part of the data is inside the box of a box plot?", "¿Qué parte de los datos hay dentro de la caja?"), [Q("All of it", "Todos"), Q("The middle half", "La mitad central"), Q("One quarter", "La cuarta parte"), Q("Only the median", "Solo la mediana")], 1,
         {0: Q("The whiskers reach the rest.", "Los bigotes llegan al resto."), 2: Q("From Q1 to Q3 is two quarters.", "De Q1 a Q3 son dos cuartos."), 3: Q("The median is the line inside.", "La mediana es la raya de dentro.")}, Q("From Q1 to Q3: 50% of the data.", "De Q1 a Q3: el 50 % de los datos.")),
        (Q("In which sector is there more inequality of salaries inside the sector?", "¿En qué sector hay más desigualdad interna de salarios?"), [Q("Retail, because it pays less", "Comercio, porque paga menos"), Q("Both the same", "Los dos igual"), Q("Technology, because its box is much wider", "Tecnología, porque su caja es mucho más ancha"), Q("It cannot be known", "No se puede saber")], 2,
         {0: Q("Paying less is not the same as being unequal.", "Pagar menos no es lo mismo que ser desigual."), 1: Q("Compare the widths.", "Compare las anchuras."), 3: Q("The box shows it.", "La caja lo muestra.")}, Q("70 − 45 = 25 against 35 − 26 = 9.", "70 − 45 = 25 frente a 35 − 26 = 9.")),
        (Q("With eleven values in order, Q3 is the…", "Con once valores ordenados, Q3 es el…"), [Q("3rd value", "3.er valor"), Q("6th value", "6.º valor"), Q("9th value", "9.º valor"), Q("11th value", "11.º valor")], 2,
         {0: Q("That is Q1.", "Ese es Q1."), 1: Q("That is the median.", "Esa es la mediana."), 3: Q("That is the maximum.", "Ese es el máximo.")}, Q("The median of the top five values (7th to 11th) is the 9th.", "La mediana de los cinco de arriba (7.º a 11.º) es el 9.º.")),
        (Q("An official says the mean income; a community group says the median. Both are correct. The best question to ask is…", "Un funcionario dice la media; un grupo vecinal, la mediana. Las dos son correctas. La mejor pregunta es…"), [Q("Who calculated wrong?", "¿Quién calculó mal?"), Q("Why did each one choose that measure, and what does it hide?", "¿Por qué eligió cada uno esa medida y qué tapa?"), Q("Which one is lying?", "¿Cuál miente?"), Q("Which number is bigger?", "¿Qué cifra es mayor?")], 1,
         {0: Q("Nobody did.", "Nadie."), 2: Q("Nobody is lying.", "Nadie miente."), 3: Q("Size is not the point.", "El tamaño no es la cuestión.")}, Q("Choosing is the bias; asking why is the defense.", "Elegir es el sesgo; preguntar por qué es la defensa.")),
    ]
    filas = [
        (t("Calculate the four measures", "Calcula las cuatro medidas"), t("I get all four right, by hand and with the calculator, and I estimate first.", "Obtengo las cuatro sin errores, a mano y con la calculadora, y estimo antes."), t("The mean is fine, but I miss the median of an even set or the range.", "La media me sale, pero fallo la mediana de conjuntos pares o el rango."), t("I mix up mean and median, or find the median without ordering (<a href=\"#s1\">review section 1</a>).", "Confundo media y mediana, o busco la mediana sin ordenar (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("See the effect of an outlier", "Reconoce el efecto de un valor atípico"), t("I explain that it moves the mean and not the median, and I use the range as a warning.", "Explico que mueve la media y no la mediana, y uso el rango como aviso."), t("I know outliers matter but not which measure they move.", "Sé que los atípicos afectan, pero no a cuál medida."), t("I always take the mean as the typical value (<a href=\"#s2\">review section 2</a>).", "Tomo siempre la media como valor típico (<a href=\"#s2\">repase la sección 2</a>).")),
        (t("Choose the measure by the shape", "Elige la medida según la forma"), t("I justify my choice with the shape and say what the other measure would hide.", "Justifico mi elección con la forma y digo qué taparía la otra medida."), t("I choose between mean and median, but forget the mode for categories.", "Elijo entre media y mediana, pero olvido la moda con categorías."), t("I always use the mean (<a href=\"#s3\">review section 3</a>).", "Uso siempre la media (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Read a box plot", "Interpreta un diagrama de caja"), t("I compare two boxes and explain what a wider box means.", "Comparo dos cajas y explico qué significa que una sea más ancha."), t("I read the five numbers but not the width of the box.", "Leo los cinco números, pero no la anchura de la caja."), t("I only look at the median (<a href=\"#s4\">review section 4</a>).", "Solo miro la mediana (<a href=\"#s4\">repase la sección 4</a>).")),
    ]
    cierre = "<p>" + t("This lesson set up the tool: <strong>a single number never describes a set of data</strong>. Mean, median, mode, and range say different things about the same data, and the five-number summary says more than all four together. And it set up the suspicion, the same one as in Topic 1 in a new disguise: when someone publishes a mean without the median, the question is not whether they calculated right, but why they chose it.",
                         "Esta lección deja instalada la herramienta: <strong>un solo número nunca describe un conjunto</strong>. Media, mediana, moda y rango dicen cosas distintas de los mismos datos, y el resumen de cinco números dice más que los cuatro juntos. Y deja instalada la sospecha, la misma del Tema 1 con otro disfraz: cuando alguien publica una media sin la mediana, la pregunta no es si calculó bien, sino por qué eligió esa.") + "</p><p>" + \
             t("Lesson 2.3 closes the topic with percents, rates, map scales, and population density. And Agnes Holbrook’s 1895 survey from Lesson 1.2 comes back: a map that seems to measure density, by an author who warned in writing that her data do not support claims about density.",
               "La Lección 2.3 cierra el tema con los porcentajes, las tasas, las escalas de mapa y la densidad de población. Y vuelve el censo de Agnes Holbrook de 1895 de la Lección 1.2: un mapa que parece medir densidad, de una autora que advirtió por escrito que sus datos no sostienen afirmaciones sobre densidad.") + "</p>"
    glosario = [
        (t("Mean", "Media"), t("The sum of the values divided by how many there are; the average.", "La suma de los valores dividida entre cuántos son; el promedio.")),
        (t("Median", "Mediana"), t("The middle value of the ordered data.", "El valor central de los datos ordenados.")),
        (t("Mode", "Moda"), t("The most frequent value; the only measure of center for categories.", "El valor más frecuente; la única medida de centro para categorías.")),
        (t("Range", "Rango"), t("Largest value minus smallest value.", "El valor mayor menos el menor.")),
        (t("Outlier", "Valor atípico"), t("A value far away from the rest.", "Un valor muy separado del resto.")),
        (t("Skewed distribution", "Distribución sesgada"), t("Data with a long tail on one side; incomes are skewed to the right.", "Datos con una cola larga hacia un lado; los ingresos están sesgados a la derecha.")),
        (t("Quartiles and box plot", "Cuartiles y diagrama de caja"), t("Q1 and Q3 split the data into quarters; the box plot draws the minimum, Q1, median, Q3, and maximum.", "Q1 y Q3 dividen los datos en cuartos; el diagrama de caja dibuja mínimo, Q1, mediana, Q3 y máximo.")),
    ]
    estd = C.estandares(["SSP.11.a", "SSP.6.b", "SSP.7.b"], ["E.c", "E.f"], base=["SSP.10.a"])
    conexion = "<p>" + t("Lesson 2.1 taught you to read a graph before believing it, and it ended with an uncomfortable idea: a correlation allows four explanations, and the drawing cannot choose. Here we go one level deeper. Before the graph comes the number that sums it up, and those numbers are chosen too. When someone says “the typical income in the neighborhood is ninety thousand dollars,” they made a decision before speaking: they decided what <em>typical</em> means.",
                         "La Lección 2.1 enseñó a leer una gráfica antes de creerla, y terminó con una idea incómoda: una correlación admite cuatro explicaciones y el dibujo no permite elegir. Aquí se baja un nivel más. Antes que la gráfica está el número que la resume, y esos números también se eligen. Cuando alguien dice «el ingreso típico del barrio es de noventa mil dólares», tomó una decisión antes de hablar: decidió qué significa <em>típico</em>.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Mean, median, and mode can tell three different stories about the same data. Knowing which one fits is the skill.", "La media, la mediana y la moda pueden contar tres historias distintas de los mismos datos. Saber cuál encaja es la destreza."),
        ["SSP.11 · " + t("Mean, median, mode, range", "Media, mediana, moda, rango"), "SSP.6 · " + t("Box plots and histograms", "Cajas e histogramas")],
        [t("<strong>Calculate</strong> the mean, median, mode, and range of a set of social data.", "<strong>Calcular</strong> la media, la mediana, la moda y el rango de un conjunto de datos sociales."),
         t("<strong>Decide</strong> which measure best describes a set, according to its shape.", "<strong>Decidir</strong> cuál medida describe mejor un conjunto, según su forma."),
         t("<strong>Build</strong> the five-number summary and read a box plot.", "<strong>Construir</strong> el resumen de cinco números y leer un diagrama de caja."),
         t("<strong>Compare</strong> two groups and explain what it means that one box is wider than the other.", "<strong>Comparar</strong> dos grupos y explicar qué significa que una caja sea más ancha que otra.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("2-3", t("Percents, rates, map scales, and population density", "Porcentajes, tasas, escalas de mapas y densidad de población")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- la práctica
JS = r"""
function fmtN(x){ return String(Math.round(x * 100) / 100); }
function medi(o){ var n = o.length; return n % 2 ? o[(n - 1) / 2] : (o[n / 2 - 1] + o[n / 2]) / 2; }
function gMed(){
  var n = elige([5, 6, 7, 8, 9]), cx = elige(TXS.ctx), base = aleatorio(cx[1], cx[2]), d = [], i, que = elige(["media", "mediana", "moda", "rango"]);
  for (i = 0; i < n; i++) d.push(base + aleatorio(-9, 9));
  if (que === "moda"){ var k = aleatorio(0, n - 3); d[k + 1] = d[k]; d[k + 2] = d[k]; }
  var o = d.slice().sort(function(a, b){ return a - b; }), s = 0; d.forEach(function(v){ s += v; });
  if (que === "moda"){ var c = {}, best = null, emp = 0; o.forEach(function(v){ c[v] = (c[v] || 0) + 1; }); for (var v in c){ if (best === null || c[v] > c[best]){ best = v; emp = 0; } else if (c[v] === c[best]) emp = 1; } if (emp) return gMed(); best = +best; }
  if (que === "media" && Math.round(s / n * 100) !== s / n * 100) return gMed();
  var val = {media: s / n, mediana: medi(o), moda: best, rango: o[n - 1] - o[0]}, r = val[que], exp;
  if (que === "media") exp = TXS.suma + s + "; " + s + " ÷ " + n + " = " + fmtN(r) + ".";
  else if (que === "mediana") exp = TXS.ord + o.join(", ") + ". " + (n % 2 ? TXS.mid + fmtN(r) + "." : TXS.mids + o[n / 2 - 1] + " " + TXS.y + " " + o[n / 2] + " → " + fmtN(r) + ".");
  else if (que === "moda") exp = TXS.ord + o.join(", ") + ". " + best + TXS.modaT;
  else exp = TXS.ord + o.join(", ") + ". " + o[n - 1] + " − " + o[0] + " = " + r + ".";
  return {enun: "<p>" + cx[0] + "</p><p style=\"font-size:1.15em\"><strong>" + d.join(", ") + "</strong></p><p>" + TXS.pide[que] + "</p>", resp: leeNumero(fmtN(r)), explica: exp,
    pista: function(v){ for (var k in val) if (k !== que && val[k] !== null && val[k] !== r && igual(v, leeNumero(fmtN(val[k])))) return TXS.otra[k] + TXS.pi[que]; return TXS.pi[que]; }};
}
function gCuar(){
  var base = aleatorio(15, 60), d = [], i, que = elige(["q1", "mediana", "q3"]);
  for (i = 0; i < 11; i++) d.push(base + aleatorio(0, 40));
  var o = d.slice().sort(function(a, b){ return a - b; }), r = que === "q1" ? o[2] : (que === "q3" ? o[8] : o[5]);
  var exp = TXS.ord + o.join(", ") + ". " + TXS.pos[que] + " " + r + ".";
  return {enun: "<p>" + TXS.once + "</p><p style=\"font-size:1.15em\"><strong>" + d.join(", ") + "</strong></p><p>" + TXS.pideC[que] + "</p>", resp: leeNumero(String(r)), explica: exp,
    pista: function(v){ if (igual(v, leeNumero(String(d[que === "q1" ? 2 : (que === "q3" ? 8 : 5)])))) return TXS.desord; return TXS.pos[que].replace(":", "."); }};
}
"""


def tx():
    return {
        "ctx": [[t("Hourly wages, in dollars, at a group of restaurants:", "Salarios por hora, en dólares, en un grupo de restaurantes:"), 12, 20],
                [t("Ages of the members of a block club:", "Edades de los miembros de un club de vecinos:"), 30, 60],
                [t("Monthly rents in a building, in hundreds of dollars:", "Alquileres mensuales de un edificio, en cientos de dólares:"), 10, 20],
                [t("Number of voters at several polling places, in tens:", "Número de votantes en varios centros de votación, en decenas:"), 25, 60],
                [t("Minutes each worker takes to get to work:", "Minutos que tarda cada trabajador en llegar al trabajo:"), 20, 50]],
        "pide": {"media": t("Find the <strong>mean</strong>.", "Halle la <strong>media</strong>."), "mediana": t("Find the <strong>median</strong>.", "Halle la <strong>mediana</strong>."),
                 "moda": t("Find the <strong>mode</strong>.", "Halle la <strong>moda</strong>."), "rango": t("Find the <strong>range</strong>.", "Halle el <strong>rango</strong>.")},
        "pi": {"media": t("Mean: add all the values and divide by how many there are.", "Media: sume todos los valores y divida entre cuántos son."), "mediana": t("Median: put them in order first, then take the middle (or the mean of the two middle values).", "Mediana: ordénelos primero y tome el del centro (o la media de los dos centrales)."),
               "moda": t("Mode: the value that appears most often.", "Moda: el valor que más se repite."), "rango": t("Range: largest minus smallest.", "Rango: mayor menos menor.")},
        "otra": {"media": t("That is the mean. ", "Esa es la media. "), "mediana": t("That is the median. ", "Esa es la mediana. "), "moda": t("That is the mode. ", "Esa es la moda. "), "rango": t("That is the range. ", "Ese es el rango. ")},
        "suma": t("Sum: ", "Suma: "), "ord": t("In order: ", "Ordenados: "), "mid": t("The middle value is ", "El valor central es "), "mids": t("The two middle values are ", "Los dos centrales son "), "y": t("and", "y"),
        "modaT": t(" appears most often.", " es el que más se repite."),
        "once": t("Eleven values:", "Once valores:"),
        "pideC": {"q1": t("Find the <strong>first quartile (Q1)</strong>.", "Halle el <strong>primer cuartil (Q1)</strong>."), "mediana": t("Find the <strong>median</strong>.", "Halle la <strong>mediana</strong>."), "q3": t("Find the <strong>third quartile (Q3)</strong>.", "Halle el <strong>tercer cuartil (Q3)</strong>.")},
        "pos": {"q1": t("With eleven values, Q1 is the 3rd:", "Con once valores, Q1 es el 3.º:"), "mediana": t("With eleven values, the median is the 6th:", "Con once valores, la mediana es el 6.º:"), "q3": t("With eleven values, Q3 is the 9th:", "Con once valores, Q3 es el 9.º:")},
        "desord": t("That is the value in that position of the list as given. Put the values in order first!", "Ese es el valor de esa posición en la lista tal como viene. ¡Ordénelos primero!"),
    }


def banco_medida():
    M = [t("Mean", "Media"), t("Median", "Mediana"), t("Mode", "Moda")]
    datos = [
        (t("The typical home price in a city where a few mansions sell for millions.", "El precio típico de una vivienda en una ciudad donde unas pocas mansiones se venden por millones."), 1, t("A few huge prices would pull the mean up.", "Unos pocos precios enormes arrastrarían la media hacia arriba.")),
        (t("The most common shoe size sold in a store, to decide what to order.", "La talla de zapato que más se vende en una tienda, para decidir qué pedir."), 2, t("The store needs the most frequent size.", "La tienda necesita la talla más frecuente.")),
        (t("The average score on a test where all scores are between 70 and 90 with no extremes.", "La nota media de un examen donde todas las notas están entre 70 y 90, sin extremos."), 0, t("Symmetric data with no outliers: the mean uses all the information.", "Datos simétricos sin atípicos: la media usa toda la información.")),
        (t("The most common political party among the members of a union.", "El partido político más común entre los miembros de un sindicato."), 2, t("Parties are categories.", "Los partidos son categorías.")),
        (t("The typical household income in a county.", "El ingreso típico por hogar en un condado."), 1, t("Incomes are skewed to the right.", "Los ingresos están sesgados a la derecha.")),
        (t("The typical salary at a company where the CEO earns 300 times what the workers earn.", "El salario típico en una empresa donde el director gana 300 veces lo que ganan los trabajadores."), 1, t("One huge salary would distort the mean.", "Un salario enorme distorsionaría la media.")),
        (t("The average daily temperature in a month with no unusual days.", "La temperatura media diaria de un mes sin días fuera de lo común."), 0, t("No extremes, so the mean works well.", "Sin extremos, la media funciona bien.")),
        (t("The most common country of birth among the immigrants in a neighborhood.", "El país de nacimiento más común entre los inmigrantes de un barrio."), 2, t("Countries are categories.", "Los países son categorías.")),
    ]
    out = [{"enun": t("Which measure fits best?", "¿Qué medida encaja mejor?") + "<br><strong>" + s + "</strong>", "ops": M, "ok": k, "exp": f"<strong>{M[k]}.</strong> " + e, "enOrden": True} for s, k, e in datos]
    otros = [
        (t("A neighborhood’s mean income is $95,000 and its median is $41,000. What does that suggest?", "El ingreso medio de un barrio es de 95,000 dólares y el mediano de 41,000. ¿Qué sugiere?"),
         [t("A few very high incomes pull the mean up.", "Unos pocos ingresos muy altos suben la media."), t("Most households earn about $95,000.", "La mayoría de los hogares gana unos 95,000 dólares."), t("Someone made a mistake.", "Alguien se equivocó."), t("Half the households earn more than $95,000.", "La mitad de los hogares gana más de 95,000 dólares.")], t("When the mean is far above the median, there is a tail of high values.", "Cuando la media está muy por encima de la mediana, hay una cola de valores altos.")),
        (t("A city adds one new resident who earns $10 million a year. What happens to the median income of the city?", "Llega a una ciudad un nuevo residente que gana 10 millones al año. ¿Qué le pasa al ingreso mediano de la ciudad?"),
         [t("It barely changes.", "Casi no cambia."), t("It goes up by millions.", "Sube millones."), t("It goes down.", "Baja."), t("It doubles.", "Se duplica.")], t("One more value moves the middle position only a tiny bit.", "Un valor más mueve la posición central apenas un poco.")),
        (t("Two classes have the same median score, 75. In class A, the box goes from 70 to 80; in class B, from 55 to 90. What can you say?", "Dos clases tienen la misma nota mediana, 75. En la clase A la caja va de 70 a 80; en la B, de 55 a 90. ¿Qué se puede decir?"),
         [t("Scores in class B are much more spread out.", "Las notas de la clase B están mucho más dispersas."), t("The two classes did the same.", "Las dos clases rindieron igual."), t("Class A did better.", "La clase A lo hizo mejor."), t("Class B has more students.", "La clase B tiene más estudiantes.")], t("Same center, very different spread: a box of 10 points against one of 35.", "Mismo centro, dispersión muy distinta: una caja de 10 puntos frente a una de 35.")),
        (t("A mayor says that “the average family here has 2.4 children.” What does this number show?", "Un alcalde dice que «la familia media aquí tiene 2.4 hijos». ¿Qué muestra esa cifra?"),
         [t("It is a mean: no family has exactly 2.4 children.", "Es una media: ninguna familia tiene exactamente 2.4 hijos."), t("It is the mode.", "Es la moda."), t("Most families have 2.4 children.", "La mayoría de las familias tiene 2.4 hijos."), t("The number must be wrong.", "La cifra debe de estar mal.")], t("A mean can be a value that nobody has.", "Una media puede ser un valor que nadie tiene.")),
    ]
    out += [{"enun": "<strong>" + s + "</strong>", "ops": ops, "ok": 0, "exp": e} for s, ops, e in otros]
    return out


def practica():
    A = {"en": ["calculate", "choose", "quartiles"], "es": ["calcular", "elegir", "cuartiles"]}[C.L]
    mods = [
        (A[0], t("Calculate the four measures", "Calcule las cuatro medidas"), "      <p>" + t("A new data set every time. Read carefully which measure is asked. If the answer has decimals, write up to two.", "Un conjunto nuevo cada vez. Lea con atención qué medida se pide. Si el resultado tiene decimales, escriba hasta dos.") + "</p>\n" + C.dec_campo("m1", t("Answer", "Respuesta"))),
        (A[1], t("Which measure?", "¿Qué medida?"), C.om("m2", t("Ask: are there outliers or a long tail? Are the data categories? Then choose.", "Pregúntese: ¿hay valores atípicos o una cola larga? ¿Los datos son categorías? Después elija."))),
        (A[2], t("Five-number summary", "Resumen de cinco números"), "      <p>" + t("Eleven values, not in order. Order them first. Then: Q1 is the 3rd value, the median the 6th, and Q3 the 9th.", "Once valores, sin ordenar. Ordénelos primero. Después: Q1 es el 3.º valor, la mediana el 6.º y Q3 el 9.º.") + "</p>\n" + C.dec_campo("m3", t("Answer", "Respuesta"))),
    ]
    js = C.js_datos("TXS", tx()) + C.js_datos("MED", banco_medida()) + JS + 'creaPracticaDec("m1", gMed);\ncreaBanco("m2", MED);\ncreaPracticaDec("m3", gCuar);\n'
    return C.pagina_practica(N, titulo(), t("Three activities · new exercises every time · two tries in each one · calculator included", "Tres actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
