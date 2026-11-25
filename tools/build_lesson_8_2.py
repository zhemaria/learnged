"""Lesson 8.2 · Bar graphs and line graphs — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "8-2"
AZ, GR, TXC = "#1565c0", "#37474f", "#1a2330"

def txt(x, y, s, size=15, color=TXC, anchor="middle", peso=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{peso}" fill="{color}">{s}</text>'

def grafica_barras(titulo, eje_y, cats, vals, paso, tope, aria):
    x0, y0, W, H = 70, 40, 520, 240
    s = [txt(x0 + W / 2, 24, titulo, 17)]
    for v in range(0, tope + 1, paso):
        y = y0 + H - H * v / tope
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + W}" y2="{y:.1f}" stroke="#cfd8dc" stroke-width="1"/>' + txt(x0 - 8, y + 5, str(v), 14, TXC, "end", 400))
    bw = W / len(cats)
    for i, (c, v) in enumerate(zip(cats, vals)):
        h = H * v / tope
        s.append(f'<rect x="{x0 + i * bw + bw * 0.18:.1f}" y="{y0 + H - h:.1f}" width="{bw * 0.64:.1f}" height="{h:.1f}" fill="{AZ}"/>')
        s.append(txt(x0 + i * bw + bw / 2, y0 + H + 22, c, 15))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/><line x1="{x0}" y1="{y0 + H}" x2="{x0 + W}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/>')
    s.append(f'<text x="18" y="{y0 + H / 2}" transform="rotate(-90 18 {y0 + H / 2})" text-anchor="middle" font-size="15" font-weight="700" fill="{TXC}">{eje_y}</text>')
    return svg("0 0 620 320", aria, "".join(s), ancho=600)

def grafica_lineas(titulo, eje_y, cats, vals, paso, tope, aria, base=0):
    x0, y0, W, H = 80, 40, 500, 240
    s = [txt(x0 + W / 2, 24, titulo, 17)]
    for v in range(base, tope + 1, paso):
        y = y0 + H - H * (v - base) / (tope - base)
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + W}" y2="{y:.1f}" stroke="#cfd8dc" stroke-width="1"/>' + txt(x0 - 8, y + 5, f"${v}", 14, TXC, "end", 400))
    dx = W / (len(cats) - 1)
    pts = [(x0 + i * dx, y0 + H - H * (v - base) / (tope - base)) for i, v in enumerate(vals)]
    s.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{AZ}" stroke-width="3.5"/>')
    for (x, y), c in zip(pts, cats):
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{AZ}"/>' + txt(x, y0 + H + 22, c, 15))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/><line x1="{x0}" y1="{y0 + H}" x2="{x0 + W}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/>')
    s.append(f'<text x="18" y="{y0 + H / 2}" transform="rotate(-90 18 {y0 + H / 2})" text-anchor="middle" font-size="15" font-weight="700" fill="{TXC}">{eje_y}</text>')
    return svg("0 0 620 320", aria, "".join(s), ancho=600)

def barras_trabajo():
    return grafica_barras(t("How people get to work", "Cómo llegan las personas al trabajo"), t("Number of people", "Cantidad de personas"),
        [t("Bus", "Autobús"), t("Car", "Carro"), t("Train", "Tren"), t("Bike", "Bicicleta"), t("Walk", "A pie")], [12, 18, 6, 4, 8], 2, 20,
        t("A bar graph titled How people get to work. The scale goes from 0 to 20 by 2. Bus: 12 people. Car: 18. Train: 6. Bike: 4. Walk: 8.",
          "Una gráfica de barras titulada Cómo llegan las personas al trabajo. La escala va de 0 a 20 de 2 en 2. Autobús: 12 personas. Carro: 18. Tren: 6. Bicicleta: 4. A pie: 8."))

def lineas_luz():
    meses = [t("Jan", "ene"), t("Feb", "feb"), t("Mar", "mar"), t("Apr", "abr"), t("May", "may"), t("Jun", "jun")]
    return grafica_lineas(t("Electric bill, January to June", "Factura de luz, de enero a junio"), t("Amount (dollars)", "Cantidad (dólares)"), meses, [120, 110, 90, 70, 80, 105], 10, 130,
        t("A line graph titled Electric bill, January to June. The scale goes from 60 to 130 dollars by 10. January: 120 dollars. February: 110. March: 90. April: 70. May: 80. June: 105.",
          "Una gráfica de líneas titulada Factura de luz, de enero a junio. La escala va de 60 a 130 dólares de 10 en 10. Enero: 120 dólares. Febrero: 110. Marzo: 90. Abril: 70. Mayo: 80. Junio: 105."), base=60)

def leccion():
    n = N
    s1 = f'''<p>{t("A <strong>graph</strong> shows data as a picture. With one look you can see which value is the largest, which is the smallest, and how the values change. Newspapers, bills, and the GED® test use graphs all the time.",
"Una <strong>gráfica</strong> muestra los datos como un dibujo. Con una mirada se ve cuál valor es el mayor, cuál es el menor y cómo cambian los valores. Los periódicos, las facturas y el examen de GED® usan gráficas todo el tiempo.")}</p>
{barras_trabajo()}
{tabla(t("The parts of a graph", "Las partes de una gráfica"), t("The parts of a graph and what each one tells you", "Las partes de una gráfica y lo que dice cada una"),
       [t("Part", "Parte"), t("What it tells you", "Lo que le dice")],
       [[t("<strong>title</strong>", "<strong>título</strong>"), t("what the graph is about", "de qué trata la gráfica")],
        [t("<strong>horizontal axis</strong> (bottom)", "<strong>eje horizontal</strong> (abajo)"), t("the categories or the times", "las categorías o los momentos")],
        [t("<strong>vertical axis</strong> (side)", "<strong>eje vertical</strong> (al lado)"), t("what is counted or measured, and its unit", "lo que se cuenta o se mide, y su unidad")],
        [t("<strong>scale</strong>", "<strong>escala</strong>"), t("how much each line on the vertical axis is worth", "cuánto vale cada línea del eje vertical")]])}
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>Before you read a graph, read its <strong>title</strong>, its <strong>axes</strong>, and its <strong>scale</strong>. In the graph above, each line is worth <strong>2 people</strong>, not 1.</p>",
"<p>Antes de leer una gráfica, lea su <strong>título</strong>, sus <strong>ejes</strong> y su <strong>escala</strong>. En la gráfica de arriba, cada línea vale <strong>2 personas</strong>, no 1.</p>"))}'''

    s2 = f'''<p>{t("A <strong>bar graph</strong> compares <strong>categories</strong>: kinds of things, places, or groups. The taller the bar, the larger the value.", "Una <strong>gráfica de barras</strong> compara <strong>categorías</strong>: tipos de cosas, lugares o grupos. Mientras más alta la barra, mayor el valor.")}</p>
{ejemplo(t("Example: how many people take the bus?", "Ejemplo: ¿cuántas personas toman el autobús?"),
  [("1", t("Find the bar.", "Busque la barra."), t("The first bar is Bus.", "La primera barra es Autobús.")),
   ("2", t("Go across to the scale.", "Vaya de lado hasta la escala."), t("The top of the bar is on the line for 12.", "La punta de la barra está en la línea del 12.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>12 people</strong> take the bus.", "<strong>12 personas</strong> toman el autobús."))])}
{ejemplo(t("Example: how many more people drive a car than take the bus?", "Ejemplo: ¿cuántas personas más van en carro que en autobús?"),
  [("1", t("Read both bars.", "Lea las dos barras."), t("Car: 18. Bus: 12.", "Carro: 18. Autobús: 12.")),
   ("✓", t("Subtract.", "Reste."), t("18 − 12 = <strong>6</strong> more people.", "18 − 12 = <strong>6</strong> personas más."))])}
{caja("ojo", t("Watch out! A bar between two lines", "¡Cuidado! Una barra entre dos líneas"), t("<p>If a bar ends halfway between two lines, its value is halfway between them. On a scale by 2, a bar halfway between 4 and 6 is worth 5.</p>",
"<p>Si una barra termina a la mitad entre dos líneas, su valor está a la mitad entre ellas. En una escala de 2 en 2, una barra a la mitad entre 4 y 6 vale 5.</p>"))}
{practica("p1", t("Practice 1 — Read a bar", "Práctica 1 — Leer una barra"), t("In the graph, how many people <strong>walk</strong> to work?", "En la gráfica, ¿cuántas personas van <strong>a pie</strong> al trabajo?"),
          [("a", "4"), ("b", "8"), ("c", "16"), ("d", "9")])}
{practica("p2", t("Practice 2 — How many more?", "Práctica 2 — ¿Cuántos más?"), t("How many more people take the <strong>bus</strong> than <strong>walk</strong>?", "¿Cuántas personas más toman el <strong>autobús</strong> que van <strong>a pie</strong>?"),
          [("a", "20"), ("b", "2"), ("c", "4"), ("d", "8")])}
{enlace(n, t("read-bars", "leer-barras"), t("read a bar graph", "leer una gráfica de barras"), t("Use the scale to read the height of each bar.", "Use la escala para leer la altura de cada barra."))}
{enlace(n, t("compare-bars", "comparar-barras"), t("compare with a bar graph", "comparar con una gráfica de barras"), t("Answer \"how many more\" and \"how many in all\".", "Responda «cuántos más» y «cuántos en total»."))}'''

    s3 = f'''<p>{t("A <strong>line graph</strong> shows how a value <strong>changes over time</strong>: by hour, by month, by year. Each point is a value, and the line joins the points in order.", "Una <strong>gráfica de líneas</strong> muestra cómo <strong>cambia un valor con el tiempo</strong>: por hora, por mes, por año. Cada punto es un valor, y la línea une los puntos en orden.")}</p>
{lineas_luz()}
{caja("ojo", t("Watch out! This scale does not start at 0", "¡Cuidado! Esta escala no empieza en 0"), t("<p>The vertical axis starts at $60, so the changes look bigger than they are. Always read the numbers on the scale, not only the shape of the line.</p>",
"<p>El eje vertical empieza en $60, así que los cambios se ven más grandes de lo que son. Lea siempre los números de la escala, no solo la forma de la línea.</p>"))}
{tabla(t("Reading a line graph", "Cómo leer una gráfica de líneas"), t("What the line in a line graph tells you", "Lo que dice la línea de una gráfica de líneas"),
       [t("The line…", "La línea…"), t("means the value…", "quiere decir que el valor…")],
       [[t("goes up ↗", "sube ↗"), t("increased", "aumentó")], [t("goes down ↘", "baja ↘"), t("decreased", "disminuyó")], [t("is flat →", "está plana →"), t("stayed the same", "se mantuvo igual")], [t("is steepest", "está más empinada"), t("changed the most", "cambió más")]])}
{ejemplo(t("Example: between which two months did the bill go up the most?", "Ejemplo: ¿entre qué dos meses subió más la factura?"),
  [("1", t("Find where the line goes up.", "Busque dónde sube la línea."), t("April → May (70 → 80) and May → June (80 → 105).", "Abril → mayo (70 → 80) y mayo → junio (80 → 105).")),
   ("2", t("Find each change.", "Halle cada cambio."), t("80 − 70 = 10 and 105 − 80 = 25.", "80 − 70 = 10 y 105 − 80 = 25.")),
   ("✓", t("Answer.", "Respuesta."), t("The bill went up the most from <strong>May to June</strong>, by $25.", "La factura subió más de <strong>mayo a junio</strong>, $25."))])}
{practica("p3", t("Practice 3 — The trend", "Práctica 3 — La tendencia"), t("From <strong>January to April</strong>, the electric bill:", "De <strong>enero a abril</strong>, la factura de luz:"),
          [("a", t("went down", "bajó")), ("b", t("went up", "subió")), ("c", t("stayed the same", "se mantuvo igual")), ("d", t("went up and then down", "subió y después bajó"))])}
{enlace(n, t("line-graphs", "graficas-lineas"), t("read a line graph", "leer una gráfica de líneas"), t("Read points and find where the line goes up or down the most.", "Lea puntos y halle dónde la línea sube o baja más."))}'''

    s4 = f'''<p>{t("Each kind of graph has its job. Choose the graph that fits the question:", "Cada tipo de gráfica tiene su trabajo. Elija la gráfica que se ajusta a la pregunta:")}</p>
{tabla(t("Which graph to use", "Qué gráfica usar"), t("When to use a bar graph and when to use a line graph", "Cuándo usar una gráfica de barras y cuándo una de líneas"),
       [t("Use a…", "Use una…"), t("to…", "para…"), t("Example", "Ejemplo")],
       [[t("<strong>bar graph</strong>", "<strong>gráfica de barras</strong>"), t("compare categories", "comparar categorías"), t("sales of 5 products", "las ventas de 5 productos")],
        [t("<strong>line graph</strong>", "<strong>gráfica de líneas</strong>"), t("show change over time", "mostrar un cambio con el tiempo"), t("your weight each month for a year", "su peso cada mes durante un año")]])}
<p>{t("To <strong>make</strong> a bar graph from a table:", "Para <strong>hacer</strong> una gráfica de barras a partir de una tabla:")}</p>
{ejemplo(t("Steps to make a bar graph", "Pasos para hacer una gráfica de barras"),
  [("1", t("Title and axes.", "Título y ejes."), t("Write a title. Label the bottom axis with the categories and the side axis with what you count.", "Escriba un título. Rotule el eje de abajo con las categorías y el eje del lado con lo que cuenta.")),
   ("2", t("Choose the scale.", "Elija la escala.")  , t("Look at the largest value. Count by 1, 2, 5, or 10 so it fits, always starting at 0.", "Mire el valor mayor. Cuente de 1 en 1, de 2 en 2, de 5 en 5 o de 10 en 10 para que quepa, siempre empezando en 0.")),
   ("✓", t("Draw the bars.", "Dibuje las barras."), t("Make each bar as tall as its value, all the same width, with spaces between them.", "Haga cada barra tan alta como su valor, todas del mismo ancho, con espacios entre ellas."))])}
{practica("p4", t("Practice 4 — Choose the graph", "Práctica 4 — Elegir la gráfica"), t("You want to compare the sales of <strong>5 different products</strong>. Which is the best choice?", "Usted quiere comparar las ventas de <strong>5 productos distintos</strong>. ¿Qué conviene más?"),
          [("a", t("a line graph", "una gráfica de líneas")), ("b", t("a single number", "un solo número")), ("c", t("a list of dates", "una lista de fechas")), ("d", t("a bar graph", "una gráfica de barras"))])}
{enlace(n, t("choose-graph", "elegir-grafica"), t("choose the right graph", "elegir la gráfica correcta"), t("Decide between a bar graph and a line graph.", "Decida entre una gráfica de barras y una de líneas."))}'''

    secciones = [("s-" + t("parts", "partes"), t("The parts of a graph", "Las partes de una gráfica"), s1),
                 ("s-" + t("bar", "barras"), t("Bar graphs: compare categories", "Gráficas de barras: comparar categorías"), s2),
                 ("s-" + t("line", "lineas"), t("Line graphs: change over time", "Gráficas de líneas: el cambio con el tiempo"), s3),
                 ("s-" + t("choose", "elegir"), t("Choose and make a graph", "Elegir y hacer una gráfica"), s4)]

    lesson = {"next": t("Lesson 8.3", "Lección 8.3"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("4 is the Bike bar. Find the Walk bar.", "4 es la barra de Bicicleta. Busque la barra de A pie."), "c": t("Each line is worth 2, not 1: the Walk bar reaches 8.", "Cada línea vale 2, no 1: la barra de A pie llega a 8."), "d": t("The bar ends right on a line. Read the number on the scale.", "La barra termina justo en una línea. Lea el número de la escala.")},
             "right": t("The Walk bar reaches the line for 8.", "La barra de A pie llega a la línea del 8."), "solution": t("The Walk bar ends on the line for 8: 8 people walk.", "La barra de A pie termina en la línea del 8: 8 personas van a pie.")},
      "p2": {"ok": "c", "hints": {"a": t("20 is 12 + 8. \"How many more\" means subtract.", "20 es 12 + 8. «Cuántos más» quiere decir restar."), "b": t("Read the bars again: Bus 12, Walk 8.", "Lea otra vez las barras: Autobús 12, A pie 8."), "d": t("8 is only the Walk bar. Subtract it from the Bus bar.", "8 es solo la barra de A pie. Réstela de la barra de Autobús.")},
             "right": t("12 − 8 = 4 more people.", "12 − 8 = 4 personas más."), "solution": t("Bus: 12. Walk: 8. 12 − 8 = 4 more people.", "Autobús: 12. A pie: 8. 12 − 8 = 4 personas más.")},
      "p3": {"ok": "a", "hints": {"b": t("Look at the line from Jan to Apr: it goes down.", "Mire la línea de ene a abr: baja."), "c": t("The values change: 120, 110, 90, 70.", "Los valores cambian: 120, 110, 90, 70."), "d": t("From January to April the line only goes down. It goes up later, in May.", "De enero a abril la línea solo baja. Sube después, en mayo.")},
             "right": t("120 → 110 → 90 → 70: it went down every month.", "120 → 110 → 90 → 70: bajó cada mes."), "solution": t("The values are 120, 110, 90, and 70. Each one is smaller: the bill went down.", "Los valores son 120, 110, 90 y 70. Cada uno es menor: la factura bajó.")},
      "p4": {"ok": "d", "hints": {"a": t("A line graph shows change over time. The products are categories.", "Una gráfica de líneas muestra un cambio con el tiempo. Los productos son categorías."), "b": t("One number cannot compare 5 products.", "Un solo número no puede comparar 5 productos."), "c": t("Dates show time, not products.", "Las fechas muestran el tiempo, no los productos.")},
             "right": t("Bar graphs compare categories, like products.", "Las gráficas de barras comparan categorías, como productos."), "solution": t("To compare categories, use a bar graph: one bar for each product.", "Para comparar categorías, use una gráfica de barras: una barra para cada producto.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("Each line is worth 2, not 1.", "Cada línea vale 2, no 1."), "c": t("12 is the Bus bar.", "12 es la barra de Autobús."), "d": t("The Train bar ends right on a line.", "La barra de Tren termina justo en una línea.")}, "solution": t("The Train bar reaches 6.", "La barra de Tren llega a 6.")},
      "B": {"ok": "b", "hints": {"a": t("Bus is 12. There is a taller bar.", "Autobús es 12. Hay una barra más alta."), "c": t("Walk is 8. There is a taller bar.", "A pie es 8. Hay una barra más alta."), "d": t("Train is 6, one of the shortest.", "Tren es 6, de las más bajas.")}, "solution": t("The tallest bar is Car, with 18 people.", "La barra más alta es Carro, con 18 personas.")},
      "C": {"ok": "c", "hints": {"a": t("30 is 18 + 12. Subtract.", "30 es 18 + 12. Reste."), "b": t("12 is only the Bus bar.", "12 es solo la barra de Autobús."), "d": t("18 is only the Car bar.", "18 es solo la barra de Carro.")}, "solution": t("18 − 12 = 6 more people.", "18 − 12 = 6 personas más.")},
      "D": {"ok": "d", "hints": {"a": t("18 is only the tallest bar. Add all the bars.", "18 es solo la barra más alta. Sume todas las barras."), "b": t("5 is the number of bars, not of people.", "5 es la cantidad de barras, no de personas."), "c": t("Check the sum: 12 + 18 + 6 + 4 + 8.", "Revise la suma: 12 + 18 + 6 + 4 + 8.")}, "solution": t("12 + 18 + 6 + 4 + 8 = 48 people.", "12 + 18 + 6 + 4 + 8 = 48 personas.")},
      "E": {"ok": "b", "hints": {"a": t("$80 is May.", "$80 es mayo."), "c": t("Read the scale carefully: March is on the line for 90.", "Lea la escala con cuidado: marzo está en la línea del 90."), "d": t("$110 is February.", "$110 es febrero.")}, "solution": t("The point for March is on the line for $90.", "El punto de marzo está en la línea de $90.")},
      "F": {"ok": "c", "hints": {"a": t("January was $120, one of the highest.", "Enero fue $120, de los más altos."), "b": t("May was $80. One month was lower.", "Mayo fue $80. Un mes fue más bajo."), "d": t("June was $105.", "Junio fue $105.")}, "solution": t("The lowest point is April, $70.", "El punto más bajo es abril, $70.")},
      "G": {"ok": "d", "hints": {"a": t("From January to February the bill went down.", "De enero a febrero la factura bajó."), "b": t("April to May went up only $10.", "De abril a mayo subió solo $10."), "c": t("From February to March the bill went down.", "De febrero a marzo la factura bajó.")}, "solution": t("May to June: 105 − 80 = $25, the biggest increase.", "De mayo a junio: 105 − 80 = $25, el mayor aumento.")},
      "H": {"ok": "a", "hints": {"b": t("A bar graph compares categories. Months show change over time.", "Una gráfica de barras compara categorías. Los meses muestran un cambio con el tiempo."), "c": t("A frequency table counts answers; it does not show change over time well.", "Una tabla de frecuencias cuenta respuestas; no muestra bien el cambio con el tiempo."), "d": t("A list does not show the change as clearly as a graph.", "Una lista no muestra el cambio tan claro como una gráfica.")}, "solution": t("Change over time, month by month: use a line graph.", "Un cambio con el tiempo, mes a mes: use una gráfica de líneas.")}
     }}

    quiz = [
     ("A", t("Use the bar graph. How many people take the <strong>train</strong>?", "Use la gráfica de barras. ¿Cuántas personas toman el <strong>tren</strong>?"), [("a", "6"), ("b", "3"), ("c", "12"), ("d", "7")]),
     ("B", t("Which way to get to work is the most common?", "¿Cuál es la forma más común de llegar al trabajo?"), [("a", t("bus", "autobús")), ("b", t("car", "carro")), ("c", t("walking", "a pie")), ("d", t("train", "tren"))]),
     ("C", t("How many more people go by <strong>car</strong> than by <strong>bus</strong>?", "¿Cuántas personas más van en <strong>carro</strong> que en <strong>autobús</strong>?"), [("a", "30"), ("b", "12"), ("c", "6"), ("d", "18")]),
     ("D", t("How many people answered in all?", "¿Cuántas personas respondieron en total?"), [("a", "18"), ("b", "5"), ("c", "40"), ("d", "48")]),
     ("E", t("Use the line graph. How much was the electric bill in <strong>March</strong>?", "Use la gráfica de líneas. ¿Cuánto fue la factura de luz en <strong>marzo</strong>?"), [("a", "$80"), ("b", "$90"), ("c", "$100"), ("d", "$110")]),
     ("F", t("In which month was the bill the <strong>lowest</strong>?", "¿En qué mes fue <strong>más baja</strong> la factura?"), [("a", t("January", "enero")), ("b", t("May", "mayo")), ("c", t("April", "abril")), ("d", t("June", "junio"))]),
     ("G", t("Between which two months did the bill go <strong>up the most</strong>?", "¿Entre qué dos meses <strong>subió más</strong> la factura?"), [("a", t("January and February", "enero y febrero")), ("b", t("April and May", "abril y mayo")), ("c", t("February and March", "febrero y marzo")), ("d", t("May and June", "mayo y junio"))]),
     ("H", t("What is the best way to show how your weight changes each month for a year?", "¿Cuál es la mejor forma de mostrar cómo cambia su peso cada mes durante un año?"), [("a", t("a line graph", "una gráfica de líneas")), ("b", t("a bar graph", "una gráfica de barras")), ("c", t("a frequency table", "una tabla de frecuencias")), ("d", t("a list of numbers", "una lista de números"))])]

    return B.pagina_leccion(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"),
        t("Bar graphs and line graphs", "Gráficas de barras y de líneas"),
        t("Bars to compare, lines to see change: read any graph by its title, its axes, and its scale.", "Barras para comparar, líneas para ver el cambio: lea cualquier gráfica por su título, sus ejes y su escala."),
        ("📊", t("Read the scale first", "Primero la escala")),
        [t("<strong>Name</strong> the parts of a graph and read its scale.", "<strong>Nombrar</strong> las partes de una gráfica y leer su escala."),
         t("<strong>Read and compare</strong> the bars of a bar graph.", "<strong>Leer y comparar</strong> las barras de una gráfica de barras."),
         t("<strong>Read</strong> a line graph and describe how a value changes over time.", "<strong>Leer</strong> una gráfica de líneas y describir cómo cambia un valor con el tiempo."),
         t("<strong>Choose and make</strong> the right graph for a set of data.", "<strong>Elegir y hacer</strong> la gráfica correcta para un grupo de datos.")],
        secciones,
        (t("Make a bar graph of the frequency table you made in Lesson 8.1 (or of five of your monthly expenses). Choose a good scale, label both axes, and give it a title.",
           "Haga una gráfica de barras con la tabla de frecuencias que hizo en la Lección 8.1 (o con cinco de sus gastos del mes). Elija una buena escala, rotule los dos ejes y póngale un título."),
         t("Find a graph in a newspaper, on a bill, or online. Write its title, what each axis shows, its scale, and one thing the graph tells you.",
           "Busque una gráfica en un periódico, en una factura o en internet. Escriba su título, lo que muestra cada eje, su escala y una cosa que le dice la gráfica.")),
        quiz,
        t("Self-check checklist for graphs", "Lista de autoevaluación de gráficas"),
        t("Self-check checklist: skills for bar graphs and line graphs", "Lista de autoevaluación: destrezas con gráficas de barras y de líneas"),
        [(t("The parts and the scale", "Las partes y la escala"), t("I read the title, the axes, and the scale before the bars or the line.", "Leo el título, los ejes y la escala antes que las barras o la línea."), t("I sometimes forget to check the scale.", "A veces olvido revisar la escala."), t("I count each line as 1.", "Cuento cada línea como 1.")),
         (t("Bar graphs", "Gráficas de barras"), t("I read and compare bars, including bars between two lines.", "Leo y comparo barras, incluso barras entre dos líneas."), t("I read bars that end on a line.", "Leo las barras que terminan en una línea."), t("I mix up the bars.", "Confundo las barras.")),
         (t("Line graphs", "Gráficas de líneas"), t("I read points and find where the line changes the most.", "Leo puntos y hallo dónde la línea cambia más."), t("I see if the line goes up or down.", "Veo si la línea sube o baja."), t("I do not know how to read a line graph yet.", "Todavía no sé leer una gráfica de líneas.")),
         (t("Choose and make a graph", "Elegir y hacer una gráfica"), t("I choose the right graph and make a bar graph with a good scale.", "Elijo la gráfica correcta y hago una gráfica de barras con una buena escala."), t("I make a graph with some help.", "Hago una gráfica con un poco de ayuda."), t("I do not know which graph to use.", "No sé qué gráfica usar."))],
        t("<p>You can now read, compare, and make bar graphs and line graphs.</p>\n<p>In <strong>Lesson 8.3 · Final project</strong> you will put together everything you learned in Level 1 to plan a real project: a budget for a celebration or a home project, with measures, money, tables, and a graph.</p>",
          "<p>Ya sabe leer, comparar y hacer gráficas de barras y de líneas.</p>\n<p>En la <strong>Lección 8.3 · Proyecto final</strong> juntará todo lo que aprendió en el Nivel 1 para planear un proyecto real: un presupuesto para una celebración o un proyecto en la casa, con medidas, dinero, tablas y una gráfica.</p>"),
        ("8-3", ("", t("Lesson 8.3 · Final project", "Lección 8.3 · Proyecto final"))),
        [(t("graph", "gráfica"), t("A picture that shows data.", "Un dibujo que muestra datos.")),
         (t("axis (plural: axes)", "eje"), t("One of the two lines of a graph: horizontal (bottom) or vertical (side).", "Una de las dos líneas de una gráfica: horizontal (abajo) o vertical (al lado).")),
         (t("scale", "escala"), t("The numbers on an axis, and how much each line is worth.", "Los números de un eje, y cuánto vale cada línea.")),
         (t("bar graph", "gráfica de barras"), t("A graph that uses bars to compare categories.", "Una gráfica que usa barras para comparar categorías.")),
         (t("line graph", "gráfica de líneas"), t("A graph that uses points joined by a line to show change over time.", "Una gráfica que usa puntos unidos por una línea para mostrar un cambio con el tiempo.")),
         (t("trend", "tendencia"), t("The general direction of a line graph: going up, going down, or staying the same.", "La dirección general de una gráfica de líneas: subir, bajar o mantenerse igual."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "ctxB": [
   {"tit": "Favorite fruit", "eje": "Number of people", "cats": ["Apple", "Mango", "Banana", "Grape", "Orange"], "q": "How many people chose <strong>{c}</strong>?", "mas": "How many more people chose <strong>{a}</strong> than <strong>{b}</strong>?", "tot": "How many people chose <strong>{a}</strong> or <strong>{b}</strong>?"},
   {"tit": "Books read by each class", "eje": "Number of books", "cats": ["Class A", "Class B", "Class C", "Class D", "Class E"], "q": "How many books did <strong>{c}</strong> read?", "mas": "How many more books did <strong>{a}</strong> read than <strong>{b}</strong>?", "tot": "How many books did <strong>{a}</strong> and <strong>{b}</strong> read together?"},
   {"tit": "Cars sold each day", "eje": "Number of cars", "cats": ["Mon", "Tue", "Wed", "Thu", "Fri"], "q": "How many cars were sold on <strong>{c}</strong>?", "mas": "How many more cars were sold on <strong>{a}</strong> than on <strong>{b}</strong>?", "tot": "How many cars were sold on <strong>{a}</strong> and <strong>{b}</strong> together?"}],
  "ariaB": "A bar graph titled {tit}. The scale goes from 0 to {tope} by {paso}. {datos}",
  "escala": "Each line is worth {paso}, not 1. Count by {paso}.",
  "otraBarra": "That is the value of another bar. Find the bar for {c}.",
  "mitad": "The bar ends halfway between two lines: its value is halfway between them.",
  "pistaB": "Find the bar, go across to the scale, and read the number. Check how much each line is worth.",
  "bienB": "The bar for {c} reaches <strong>{v}</strong>.",
  "solMas": "{a}: {va}. {b}: {vb}. {va} − {vb} = <strong>{r}</strong>.",
  "solTot": "{a}: {va}. {b}: {vb}. {va} + {vb} = <strong>{r}</strong>.",
  "sumaMas": "You added. \"How many more\" means subtract.",
  "restaTot": "You subtracted. \"Together\" means add.",
  "pistaComp": "Read both bars with the scale, then subtract (how many more) or add (together).",
  "ctxL": [{"tit": "Temperature during the day", "eje": "Degrees (°F)", "cats": ["8 a.m.", "10 a.m.", "12 p.m.", "2 p.m.", "4 p.m.", "6 p.m."], "u": "°F", "pre": ""},
           {"tit": "Savings each month", "eje": "Dollars", "cats": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "u": "", "pre": "$"},
           {"tit": "Visitors to a library", "eje": "Number of visitors", "cats": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], "u": "", "pre": ""}],
  "ariaL": "A line graph titled {tit}. The scale goes from {lo} to {hi} by {paso}. {datos}",
  "qMax": "When was the value the <strong>highest</strong>?",
  "qMin": "When was the value the <strong>lowest</strong>?",
  "qSube": "Between which two times did the value go <strong>up the most</strong>?",
  "qVal": "What was the value at <strong>{c}</strong>?",
  "y": "and",
  "bienMax": "The highest point is {c}: {v}.",
  "bienMin": "The lowest point is {c}: {v}.",
  "bienSube": "The biggest increase is from {a} to {b}: {va} → {vb}, up {r}.",
  "bienVal": "The point for {c} is at {v}.",
  "pistaL": "Look at the points and the scale. Up means increase; down means decrease.",
  "noMayor": "There is a higher point.", "noMenor": "There is a lower point.", "noSube": "Find each increase and compare them.", "otroPunto": "That is the value of another point.",
  "sit": [["the price of gas every week for a year", "line"], ["the number of students in 5 different classes", "bar"], ["the temperature every hour of a day", "line"], ["the favorite sport of the people in a survey", "bar"],
          ["how much a baby weighs each month", "line"], ["the sales of 4 different stores", "bar"], ["your savings at the end of each month", "line"], ["the number of votes for each candidate", "bar"]],
  "pregSit": "You want to show <strong>{s}</strong>. Which graph is best?",
  "bar": "a bar graph", "line": "a line graph",
  "bienBar": "These are categories to compare: a <strong>bar graph</strong>.",
  "bienLine": "This is a change over time: a <strong>line graph</strong>.",
  "pistaSit": "Ask: are you comparing categories (bars) or showing change over time (line)?"
 },
 "es": {
  "ctxB": [
   {"tit": "Fruta favorita", "eje": "Cantidad de personas", "cats": ["Manzana", "Mango", "Plátano", "Uva", "Naranja"], "q": "¿Cuántas personas eligieron <strong>{c}</strong>?", "mas": "¿Cuántas personas más eligieron <strong>{a}</strong> que <strong>{b}</strong>?", "tot": "¿Cuántas personas eligieron <strong>{a}</strong> o <strong>{b}</strong>?"},
   {"tit": "Libros leídos por cada clase", "eje": "Cantidad de libros", "cats": ["Clase A", "Clase B", "Clase C", "Clase D", "Clase E"], "q": "¿Cuántos libros leyó la <strong>{c}</strong>?", "mas": "¿Cuántos libros más leyó la <strong>{a}</strong> que la <strong>{b}</strong>?", "tot": "¿Cuántos libros leyeron juntas la <strong>{a}</strong> y la <strong>{b}</strong>?"},
   {"tit": "Carros vendidos cada día", "eje": "Cantidad de carros", "cats": ["lun", "mar", "mié", "jue", "vie"], "q": "¿Cuántos carros se vendieron el <strong>{c}</strong>?", "mas": "¿Cuántos carros más se vendieron el <strong>{a}</strong> que el <strong>{b}</strong>?", "tot": "¿Cuántos carros se vendieron entre el <strong>{a}</strong> y el <strong>{b}</strong>?"}],
  "ariaB": "Una gráfica de barras titulada {tit}. La escala va de 0 a {tope} de {paso} en {paso}. {datos}",
  "escala": "Cada línea vale {paso}, no 1. Cuente de {paso} en {paso}.",
  "otraBarra": "Ese es el valor de otra barra. Busque la barra de {c}.",
  "mitad": "La barra termina a la mitad entre dos líneas: su valor está a la mitad entre ellas.",
  "pistaB": "Busque la barra, vaya de lado hasta la escala y lea el número. Revise cuánto vale cada línea.",
  "bienB": "La barra de {c} llega a <strong>{v}</strong>.",
  "solMas": "{a}: {va}. {b}: {vb}. {va} − {vb} = <strong>{r}</strong>.",
  "solTot": "{a}: {va}. {b}: {vb}. {va} + {vb} = <strong>{r}</strong>.",
  "sumaMas": "Sumó. «Cuántos más» quiere decir restar.",
  "restaTot": "Restó. «Juntos» o «entre los dos» quiere decir sumar.",
  "pistaComp": "Lea las dos barras con la escala, y después reste (cuántos más) o sume (juntos).",
  "ctxL": [{"tit": "Temperatura durante el día", "eje": "Grados (°F)", "cats": ["8 a.m.", "10 a.m.", "12 p.m.", "2 p.m.", "4 p.m.", "6 p.m."], "u": "°F", "pre": ""},
           {"tit": "Ahorros de cada mes", "eje": "Dólares", "cats": ["ene", "feb", "mar", "abr", "may", "jun"], "u": "", "pre": "$"},
           {"tit": "Visitantes de una biblioteca", "eje": "Cantidad de visitantes", "cats": ["lun", "mar", "mié", "jue", "vie", "sáb"], "u": "", "pre": ""}],
  "ariaL": "Una gráfica de líneas titulada {tit}. La escala va de {lo} a {hi} de {paso} en {paso}. {datos}",
  "qMax": "¿Cuándo fue <strong>más alto</strong> el valor?",
  "qMin": "¿Cuándo fue <strong>más bajo</strong> el valor?",
  "qSube": "¿Entre qué dos momentos <strong>subió más</strong> el valor?",
  "qVal": "¿Cuál fue el valor en <strong>{c}</strong>?",
  "y": "y",
  "bienMax": "El punto más alto es {c}: {v}.",
  "bienMin": "El punto más bajo es {c}: {v}.",
  "bienSube": "El mayor aumento es de {a} a {b}: {va} → {vb}, subió {r}.",
  "bienVal": "El punto de {c} está en {v}.",
  "pistaL": "Mire los puntos y la escala. Subir quiere decir aumentar; bajar quiere decir disminuir.",
  "noMayor": "Hay un punto más alto.", "noMenor": "Hay un punto más bajo.", "noSube": "Halle cada aumento y compárelos.", "otroPunto": "Ese es el valor de otro punto.",
  "sit": [["el precio de la gasolina cada semana durante un año", "line"], ["la cantidad de estudiantes de 5 clases distintas", "bar"], ["la temperatura cada hora de un día", "line"], ["el deporte favorito de las personas de una encuesta", "bar"],
          ["cuánto pesa un bebé cada mes", "line"], ["las ventas de 4 tiendas distintas", "bar"], ["sus ahorros al final de cada mes", "line"], ["la cantidad de votos de cada candidato", "bar"]],
  "pregSit": "Usted quiere mostrar <strong>{s}</strong>. ¿Qué gráfica conviene más?",
  "bar": "una gráfica de barras", "line": "una gráfica de líneas",
  "bienBar": "Son categorías para comparar: una <strong>gráfica de barras</strong>.",
  "bienLine": "Es un cambio con el tiempo: una <strong>gráfica de líneas</strong>.",
  "pistaSit": "Pregúntese: ¿compara categorías (barras) o muestra un cambio con el tiempo (líneas)?"
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function ejeY(s, x, y, txt){ return '<text x="' + x + '" y="' + y + '" transform="rotate(-90 ' + x + ' ' + y + ')" text-anchor="middle" font-size="15" font-weight="700" fill="#1a2330">' + txt + '</text>'; }
function hazBarras(){
  var c = elige(TXT.ctxB), paso = elige([2, 5, 10]), tope = paso * 10, mitades = paso !== 5 && Math.random() < 0.3;
  var V = c.cats.map(function(){ return paso * aleatorio(1, 9) + (mitades && Math.random() < 0.4 ? paso / 2 : 0); });
  var x0 = 70, y0 = 40, W = 520, H = 240, s = '<text x="' + (x0 + W / 2) + '" y="24" text-anchor="middle" font-size="17" font-weight="700" fill="#1a2330">' + c.tit + '</text>';
  for (var v = 0; v <= tope; v += paso){ var y = y0 + H - H * v / tope; s += linea([x0, y], [x0 + W, y], "#cfd8dc", 1) + '<text x="' + (x0 - 8) + '" y="' + f1(y + 5) + '" text-anchor="end" font-size="14" fill="#1a2330">' + v + '</text>'; }
  var bw = W / 5;
  V.forEach(function(v, i){ var h = H * v / tope; s += '<rect x="' + f1(x0 + i * bw + bw * 0.18) + '" y="' + f1(y0 + H - h) + '" width="' + f1(bw * 0.64) + '" height="' + f1(h) + '" fill="#1565c0"/>' + texto([x0 + i * bw + bw / 2, y0 + H + 22], c.cats[i], 15, "#1a2330"); });
  s += linea([x0, y0], [x0, y0 + H], "#37474f", 2) + linea([x0, y0 + H], [x0 + W, y0 + H], "#37474f", 2) + ejeY(s, 18, y0 + H / 2, c.eje);
  var datos = c.cats.map(function(k, i){ return k + ": " + V[i]; }).join(". ") + ".";
  return { c: c, V: V, paso: paso, svg: '<svg class="figura" viewBox="0 0 620 320" role="img" aria-label="' + F(TXT.ariaB, { tit: c.tit, tope: tope, paso: paso, datos: datos }) + '">' + s + '</svg>' };
}

/* ============ MODULE 1 · read a bar ============ */
function genLeerB(){
  var G = hazBarras(), i = aleatorio(0, 4), v = G.V[i], op = [{ html: String(v), clave: "ok" }], pistas = {};
  function mete(x, msg){ if (x <= 0 || op.some(function(o){ return o.html === String(x); })) return; op.push({ html: String(x), clave: "k" + op.length }); pistas["k" + (op.length - 1)] = msg; }
  if (G.paso !== 1) mete(v / G.paso, F(TXT.escala, { paso: G.paso }));
  if (v % G.paso) mete(v - G.paso / 2, TXT.mitad);
  mete(G.V[(i + 1) % 5], F(TXT.otraBarra, { c: G.c.cats[i] })); mete(G.V[(i + 2) % 5], F(TXT.otraBarra, { c: G.c.cats[i] }));
  mete(v + G.paso, TXT.pistaB); mete(v - G.paso, TXT.pistaB);
  op = op.slice(0, 4);
  var txt = F(TXT.bienB, { c: G.c.cats[i], v: v });
  return { enun: G.svg + F(G.c.q, { c: G.c.cats[i] }), opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaB, bien: txt, mal: txt };
}

/* ============ MODULE 2 · compare bars ============ */
function genCompB(){
  var G = hazBarras(), i = aleatorio(0, 4), j = (i + aleatorio(1, 4)) % 5, a = G.V[i], b = G.V[j], p = [];
  if (a === b) return genCompB();
  if (Math.random() < 0.6){
    if (a < b){ var x = i; i = j; j = x; x = a; a = b; b = x; }
    p.push({ v: a + b, msg: TXT.sumaMas });
    return { enun: G.svg + F(G.c.mas, { a: G.c.cats[i], b: G.c.cats[j] }), solucion: F(TXT.solMas, { a: G.c.cats[i], b: G.c.cats[j], va: a, vb: b, r: a - b }), evalua: numN(a - b, p, TXT.pistaComp) };
  }
  p.push({ v: Math.abs(a - b), msg: TXT.restaTot });
  return { enun: G.svg + F(G.c.tot, { a: G.c.cats[i], b: G.c.cats[j] }), solucion: F(TXT.solTot, { a: G.c.cats[i], b: G.c.cats[j], va: a, vb: b, r: a + b }), evalua: numN(a + b, p, TXT.pistaComp) };
}

/* ============ MODULE 3 · line graphs ============ */
function genLinea(){
  var c = elige(TXT.ctxL), paso = elige([5, 10]), lo = paso * aleatorio(2, 6), hi = lo + paso * 8, V = [];
  V.push(lo + paso * aleatorio(1, 7));
  for (var i = 1; i < 6; i++){ var nv = V[i - 1] + paso * elige([-2, -1, 1, 1, 2, 3]); V.push(Math.max(lo, Math.min(hi, nv))); }
  for (i = 1; i < 6; i++) if (V[i] === V[i - 1]) V[i] = V[i] + paso <= hi ? V[i] + paso : V[i] - paso;
  var x0 = 80, y0 = 40, W = 500, H = 240, dx = W / 5, s = '<text x="' + (x0 + W / 2) + '" y="24" text-anchor="middle" font-size="17" font-weight="700" fill="#1a2330">' + c.tit + '</text>';
  for (var v = lo; v <= hi; v += paso){ var y = y0 + H - H * (v - lo) / (hi - lo); s += linea([x0, y], [x0 + W, y], "#cfd8dc", 1) + '<text x="' + (x0 - 8) + '" y="' + f1(y + 5) + '" text-anchor="end" font-size="14" fill="#1a2330">' + c.pre + v + '</text>'; }
  var P = V.map(function(v, i){ return [x0 + i * dx, y0 + H - H * (v - lo) / (hi - lo)]; });
  s += '<polyline points="' + P.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="none" stroke="#1565c0" stroke-width="3.5"/>';
  P.forEach(function(p, i){ s += '<circle cx="' + f1(p[0]) + '" cy="' + f1(p[1]) + '" r="6" fill="#1565c0"/>' + texto([p[0], y0 + H + 22], c.cats[i], 14, "#1a2330"); });
  s += linea([x0, y0], [x0, y0 + H], "#37474f", 2) + linea([x0, y0 + H], [x0 + W, y0 + H], "#37474f", 2) + ejeY(s, 18, y0 + H / 2, c.eje);
  var fmt = function(v){ return c.pre + v + (c.u ? " " + c.u : ""); };
  var datos = c.cats.map(function(k, i){ return k + ": " + fmt(V[i]); }).join(". ") + ".";
  var svg = '<svg class="figura" viewBox="0 0 620 320" role="img" aria-label="' + F(TXT.ariaL, { tit: c.tit, lo: c.pre + lo, hi: c.pre + hi, paso: paso, datos: datos }) + '">' + s + '</svg>';
  var tipo = elige(["max", "min", "sube", "val"]), op = [], pistas = {}, ok, txt, k;
  if (tipo === "max" || tipo === "min"){
    var ext = tipo === "max" ? Math.max.apply(null, V) : Math.min.apply(null, V);
    if (V.filter(function(x){ return x === ext; }).length > 1) return genLinea();
    k = V.indexOf(ext);
    baraja([0, 1, 2, 3, 4, 5].filter(function(x){ return x !== k; })).slice(0, 3).concat([k]).sort().forEach(function(x){ op.push({ html: c.cats[x], clave: String(x) }); if (x !== k) pistas[String(x)] = tipo === "max" ? TXT.noMayor : TXT.noMenor; });
    txt = F(tipo === "max" ? TXT.bienMax : TXT.bienMin, { c: c.cats[k], v: fmt(ext) });
    return { enOrden: true, enun: svg + (tipo === "max" ? TXT.qMax : TXT.qMin), opciones: op, correcta: String(k), pistas: pistas, pista: TXT.pistaL, bien: txt, mal: txt };
  }
  if (tipo === "sube"){
    var D = []; for (i = 1; i < 6; i++) D.push(V[i] - V[i - 1]);
    var mx = Math.max.apply(null, D);
    if (mx <= 0 || D.filter(function(x){ return x === mx; }).length > 1) return genLinea();
    k = D.indexOf(mx);
    baraja([0, 1, 2, 3, 4].filter(function(x){ return x !== k; })).slice(0, 3).concat([k]).sort().forEach(function(x){ op.push({ html: c.cats[x] + " " + TXT.y + " " + c.cats[x + 1], clave: String(x) }); if (x !== k) pistas[String(x)] = TXT.noSube; });
    txt = F(TXT.bienSube, { a: c.cats[k], b: c.cats[k + 1], va: fmt(V[k]), vb: fmt(V[k + 1]), r: fmt(mx) });
    return { enOrden: true, enun: svg + TXT.qSube, opciones: op, correcta: String(k), pistas: pistas, pista: TXT.pistaL, bien: txt, mal: txt };
  }
  k = aleatorio(0, 5); op.push({ html: fmt(V[k]), clave: "ok" });
  [V[(k + 1) % 6], V[(k + 2) % 6], V[k] + paso, V[k] - paso, V[k] + 2 * paso].forEach(function(x){ if (op.length < 4 && !op.some(function(o){ return o.html === fmt(x); })){ op.push({ html: fmt(x), clave: "k" + op.length }); pistas["k" + (op.length - 1)] = TXT.otroPunto; } });
  txt = F(TXT.bienVal, { c: c.cats[k], v: fmt(V[k]) });
  return { enun: svg + F(TXT.qVal, { c: c.cats[k] }), opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaL, bien: txt, mal: txt };
}

/* ============ MODULE 4 · choose the graph ============ */
function genSit(){
  var s = elige(TXT.sit), ok = s[1], txt = ok === "bar" ? TXT.bienBar : TXT.bienLine, pistas = {};
  pistas[ok === "bar" ? "line" : "bar"] = TXT.pistaSit;
  return { enOrden: true, enun: F(TXT.pregSit, { s: s[0] }), opciones: [{ html: TXT.bar, clave: "bar" }, { html: TXT.line, clave: "line" }], correcta: ok, pistas: pistas, pista: TXT.pistaSit, bien: txt, mal: txt };
}

creaPracticaOM("p1", genLeerB);
creaPracticaLibre("p2", genCompB);
creaPracticaOM("p3", genLinea);
creaPracticaOM("p4", genSit);
'''

def practica_pagina():
    n = N
    mods = [
     (t("read-bars", "leer-barras"), t("Read a bar graph", "Leer una gráfica de barras"),
      f'''      <p>{t("First check the scale: how much is each line worth? Then find the bar, go across to the scale, and read the number. A bar that ends halfway between two lines is worth the number halfway between them.", "Primero revise la escala: ¿cuánto vale cada línea? Después busque la barra, vaya de lado hasta la escala y lea el número. Una barra que termina a la mitad entre dos líneas vale el número que está a la mitad entre ellas.")}</p>
{B.om("p1", t("Practice: read the bar", "Practique: leer la barra"))}'''),
     (t("compare-bars", "comparar-barras"), t("Compare with a bar graph", "Comparar con una gráfica de barras"),
      f'''      <p>{t("<strong>\"How many more\"</strong>: subtract the two bars. <strong>\"Together\"</strong>: add them.", "<strong>«Cuántos más»</strong>: reste las dos barras. <strong>«Juntos»</strong>: súmelas.")}</p>
{B.libre("p2", t("Practice: compare", "Practique: comparar"), t("Answer", "Respuesta"))}'''),
     (t("line-graphs", "graficas-lineas"), t("Read a line graph", "Leer una gráfica de líneas"),
      f'''      <p>{t("Each point is a value at one time. The line goes up when the value increases and down when it decreases. The steepest part is where it changed the most. Read the scale: it may not start at 0.", "Cada punto es un valor en un momento. La línea sube cuando el valor aumenta y baja cuando disminuye. La parte más empinada es donde más cambió. Lea la escala: puede que no empiece en 0.")}</p>
{B.om("p3", t("Practice: read the line", "Practique: leer la línea"))}'''),
     (t("choose-graph", "elegir-grafica"), t("Choose the right graph", "Elegir la gráfica correcta"),
      f'''      <p>{t("<strong>Bar graph</strong>: to compare categories (products, places, groups). <strong>Line graph</strong>: to show change over time (hours, months, years).", "<strong>Gráfica de barras</strong>: para comparar categorías (productos, lugares, grupos). <strong>Gráfica de líneas</strong>: para mostrar un cambio con el tiempo (horas, meses, años).")}</p>
{B.om("p4", t("Practice: which graph?", "Practique: ¿qué gráfica?"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"), t("Bar graphs and line graphs", "Gráficas de barras y de líneas"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun svg.figura{display:block;width:100%;max-width:560px;height:auto;margin:10px auto;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Gráficas de barras y de líneas")
