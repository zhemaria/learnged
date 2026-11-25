"""Lesson 8.1 · Reading and understanding data tables — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "8-1"

def tabla_datos(titulo, cab, filas, aria):
    """A data table with a visible title; the first column is a row header."""
    th = "".join(f'<th scope="col">{c}</th>' for c in cab)
    tr = "\n".join("<tr>" + f'<th scope="row">{f[0]}</th>' + "".join(f"<td>{c}</td>" for c in f[1:]) + "</tr>" for f in filas)
    return (f'<p class="titulo-ej" aria-hidden="true" style="text-align:center;margin-bottom:4px;">{titulo}</p>\n'
            f'<div aria-label="{aria} (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">{titulo}</caption>\n'
            f'<thead><tr>{th}</tr></thead>\n<tbody>\n{tr}\n</tbody>\n</table></div>\n'
            '<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>')

def camion():
    return tabla_datos(t("Food truck sales (number sold)", "Ventas de un camión de comida (cantidad vendida)"),
        [t("Day", "Día"), "Tacos", "Tortas", t("Drinks", "Bebidas")],
        [[t("Monday", "lunes"), "45", "20", "60"], [t("Tuesday", "martes"), "38", "25", "52"], [t("Wednesday", "miércoles"), "50", "18", "70"], [t("Thursday", "jueves"), "43", "30", "65"]],
        t("Food truck sales", "Ventas del camión de comida"))

def horas():
    return tabla_datos(t("Hours worked", "Horas trabajadas"), [t("Employee", "Empleado"), t("Week 1", "Semana 1"), t("Week 2", "Semana 2")],
        [["Ana", "32", "40"], ["Luis", "28", "35"], ["Rosa", "40", "38"]], t("Hours worked", "Horas trabajadas"))

def leccion():
    n = N
    s1 = f'''<p>{t("A <strong>data table</strong> organizes information in <strong>rows</strong> (across) and <strong>columns</strong> (down). Tables are everywhere: bus schedules, pay stubs, nutrition labels, and many GED® questions.",
"Una <strong>tabla de datos</strong> organiza la información en <strong>filas</strong> (horizontales) y <strong>columnas</strong> (verticales). Las tablas están en todas partes: horarios de autobús, talones de pago, etiquetas de nutrición y muchas preguntas del examen de GED®.")}</p>
{camion()}
{tabla(t("The parts of a table", "Las partes de una tabla"), t("The parts of a data table and what each one tells you", "Las partes de una tabla de datos y lo que dice cada una"),
       [t("Part", "Parte"), t("What it tells you", "Lo que le dice"), t("In the food truck table", "En la tabla del camión de comida")],
       [[t("<strong>title</strong>", "<strong>título</strong>"), t("what the whole table is about", "de qué trata toda la tabla"), t("sales of a food truck", "las ventas de un camión de comida")],
        [t("<strong>column headers</strong>", "<strong>encabezados de columna</strong>"), t("what each column counts or measures", "qué cuenta o mide cada columna"), t("Tacos, Tortas, Drinks", "Tacos, Tortas, Bebidas")],
        [t("<strong>row labels</strong>", "<strong>rótulos de fila</strong>"), t("what each row is about", "de qué trata cada fila"), t("the days", "los días")],
        [t("<strong>cell</strong>", "<strong>celda</strong>"), t("one piece of data, where a row and a column meet", "un dato, donde se cruzan una fila y una columna"), t("38 tacos on Tuesday", "38 tacos el martes")]])}
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>To read a table, <strong>find the row, find the column, and look where they meet</strong>. Always read the title and the headers first, so you know what the numbers mean and in what unit.</p>",
"<p>Para leer una tabla, <strong>busque la fila, busque la columna y mire dónde se cruzan</strong>. Lea siempre primero el título y los encabezados, para saber qué quieren decir los números y en qué unidad están.</p>"))}'''

    s2 = f'''<p>{t("Most questions about a table ask you to <strong>find</strong> a value, to find the <strong>largest or the smallest</strong>, or to <strong>compare</strong> two values.", "La mayoría de las preguntas sobre una tabla le piden <strong>hallar</strong> un valor, hallar el <strong>mayor o el menor</strong>, o <strong>comparar</strong> dos valores.")}</p>
{ejemplo(t("Example: in the food truck table, how many tortas were sold on Thursday?", "Ejemplo: en la tabla del camión de comida, ¿cuántas tortas se vendieron el jueves?"),
  [("1", t("Find the row.", "Busque la fila."), t("Thursday is the last row.", "El jueves es la última fila.")),
   ("2", t("Find the column.", "Busque la columna."), t("Tortas is the third column.", "Tortas es la tercera columna.")),
   ("✓", t("Where they meet.", "Donde se cruzan."), t("<strong>30</strong> tortas.", "<strong>30</strong> tortas."))])}
{ejemplo(t("Example: which day sold the most drinks?", "Ejemplo: ¿qué día se vendieron más bebidas?"),
  [("1", t("Look down one column.", "Recorra una columna."), t("Drinks: 60, 52, 70, 65.", "Bebidas: 60, 52, 70, 65.")),
   ("✓", t("Find the largest.", "Busque el mayor."), t("70, on <strong>Wednesday</strong>.", "70, el <strong>miércoles</strong>."))])}
{ejemplo(t("Example: how many more tacos were sold on Wednesday than on Tuesday?", "Ejemplo: ¿cuántos tacos más se vendieron el miércoles que el martes?"),
  [("1", t("Find both values.", "Halle los dos valores."), t("Wednesday: 50. Tuesday: 38.", "Miércoles: 50. Martes: 38.")),
   ("✓", t("\"How many more\" means subtract.", "«Cuántos más» quiere decir restar."), t("50 − 38 = <strong>12</strong> more tacos.", "50 − 38 = <strong>12</strong> tacos más."))])}
{horas()}
{practica("p1", t("Practice 1 — Read a cell", "Práctica 1 — Leer una celda"), t("In the table of hours worked, how many hours did <strong>Luis</strong> work in <strong>Week 2</strong>?", "En la tabla de horas trabajadas, ¿cuántas horas trabajó <strong>Luis</strong> en la <strong>Semana 2</strong>?"),
          [("a", "28"), ("b", "35"), ("c", "40"), ("d", "38")])}
{practica("p2", t("Practice 2 — The largest", "Práctica 2 — El mayor"), t("Who worked the most hours in <strong>Week 1</strong>?", "¿Quién trabajó más horas en la <strong>Semana 1</strong>?"),
          [("a", "Ana"), ("b", "Luis"), ("c", "Rosa"), ("d", t("They all worked the same.", "Todos trabajaron lo mismo."))])}
{enlace(n, t("read", "leer"), t("read a table", "leer una tabla"), t("Find the row and the column, and read where they meet.", "Busque la fila y la columna, y lea dónde se cruzan."))}
{enlace(n, t("compare", "comparar"), t("compare and add", "comparar y sumar"), t("Answer \"how many more\" and \"how many in all\" questions.", "Responda preguntas de «cuántos más» y «cuántos en total»."))}'''

    s3 = f'''<p>{t("Tables also let you <strong>calculate</strong>: totals, differences, and two important summary numbers, the <strong>mean</strong> and the <strong>range</strong>.", "Las tablas también le permiten <strong>calcular</strong>: totales, diferencias y dos números importantes que resumen los datos, la <strong>media</strong> y el <strong>rango</strong>.")}</p>
{tabla(t("Summary numbers", "Números que resumen"), t("The mean and the range of a set of data", "La media y el rango de un grupo de datos"),
       [t("Number", "Número"), t("How to find it", "Cómo hallarlo"), t("What it tells you", "Lo que le dice")],
       [[t("<strong>mean</strong> (average)", "<strong>media</strong> (promedio)"), t("add all the values and divide by how many there are", "sume todos los valores y divida entre la cantidad de valores"), t("a typical value, \"if everything were shared equally\"", "un valor típico, «como si todo se repartiera por igual»")],
        [t("<strong>range</strong>", "<strong>rango</strong>"), t("largest value − smallest value", "valor mayor − valor menor"), t("how spread out the values are", "qué tan separados están los valores")]])}
{ejemplo(t("Example: the mean number of tacos sold per day", "Ejemplo: la media de tacos vendidos por día"),
  [("1", t("Add the values.", "Sume los valores."), "45 + 38 + 50 + 43 = 176."),
   ("2", t("Divide by how many values.", "Divida entre la cantidad de valores."), t("There are 4 days: 176 ÷ 4 = 44.", "Hay 4 días: 176 ÷ 4 = 44.")),
   ("✓", t("Answer.", "Respuesta."), t("The truck sold a mean of <strong>44 tacos</strong> per day.", "El camión vendió una media de <strong>44 tacos</strong> por día."))])}
{ejemplo(t("Example: the range of the drinks", "Ejemplo: el rango de las bebidas"),
  [("1", t("Largest and smallest.", "El mayor y el menor."), t("Largest: 70. Smallest: 52.", "Mayor: 70. Menor: 52.")),
   ("✓", t("Subtract.", "Reste."), t("70 − 52 = <strong>18</strong> drinks.", "70 − 52 = <strong>18</strong> bebidas."))])}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>The mean of the tacos: type {T("(")} {T("4")}{T("5")} {T("+")} {T("3")}{T("8")} {T("+")} {T("5")}{T("0")} {T("+")} {T("4")}{T("3")} {T(")")} {T("÷")} {T("4")} {T("enter")}. The screen shows 44. The parentheses make the calculator add first.</p>""",
f"""<p>La media de los tacos: escriba {T("(")} {T("4")}{T("5")} {T("+")} {T("3")}{T("8")} {T("+")} {T("5")}{T("0")} {T("+")} {T("4")}{T("3")} {T(")")} {T("÷")} {T("4")} {T("enter")}. La pantalla muestra 44. Los paréntesis hacen que la calculadora sume primero.</p>"""))}
{practica("p3", t("Practice 3 — A total", "Práctica 3 — Un total"), t("In the table of hours worked, how many hours did <strong>Ana</strong> work in the two weeks?", "En la tabla de horas trabajadas, ¿cuántas horas trabajó <strong>Ana</strong> en las dos semanas?"),
          [("a", "72"), ("b", "8"), ("c", "40"), ("d", "1,280")])}
{practica("p4", t("Practice 4 — The mean", "Práctica 4 — La media"), t("Ana worked <strong>32, 40, and 36</strong> hours in three weeks. What is the mean number of hours per week?", "Ana trabajó <strong>32, 40 y 36</strong> horas en tres semanas. ¿Cuál es la media de horas por semana?"),
          [("a", "108"), ("b", "8"), ("c", "40"), ("d", "36")])}
{enlace(n, t("mean-range", "media-rango"), t("mean and range", "media y rango"), t("Find the mean and the range of a set of numbers.", "Halle la media y el rango de un grupo de números."))}'''

    s4 = f'''<p>{t("Sometimes the data come as a long list, and <strong>you</strong> make the table. A <strong>frequency table</strong> counts how many times each answer appears. Tally marks (||||) help you count without losing your place.",
"A veces los datos vienen en una lista larga, y es <strong>usted</strong> quien hace la tabla. Una <strong>tabla de frecuencias</strong> cuenta cuántas veces aparece cada respuesta. Las marcas de conteo (||||) le ayudan a contar sin perderse.")}</p>
{ejemplo(t("Example: 12 people answered \"What is your favorite fruit?\"", "Ejemplo: 12 personas respondieron «¿Cuál es su fruta favorita?»"),
  [("1", t("The list.", "La lista."), t("apple, mango, banana, mango, apple, mango, grape, banana, mango, apple, mango, banana.", "manzana, mango, plátano, mango, manzana, mango, uva, plátano, mango, manzana, mango, plátano.")),
   ("2", t("Count each fruit.", "Cuente cada fruta."), t("apple 3, mango 5, banana 3, grape 1.", "manzana 3, mango 5, plátano 3, uva 1.")),
   ("✓", t("Check the total.", "Compruebe el total."), t("3 + 5 + 3 + 1 = 12 ✓, the same as the number of people.", "3 + 5 + 3 + 1 = 12 ✓, igual que la cantidad de personas."))])}
{tabla_datos(t("Favorite fruit", "Fruta favorita"), [t("Fruit", "Fruta"), t("Tally", "Conteo"), t("Frequency", "Frecuencia")],
   [[t("apple", "manzana"), "|||", "3"], ["mango", "<s>||||</s>", "5"], [t("banana", "plátano"), "|||", "3"], [t("grape", "uva"), "|", "1"]], t("Favorite fruit frequency table", "Tabla de frecuencias de la fruta favorita"))}
{caja("ojo", t("Watch out! Check the total", "¡Cuidado! Compruebe el total"), t("<p>The frequencies must add up to the number of answers. If they do not, you missed or repeated one. Cross out each answer in the list as you count it.</p>",
"<p>Las frecuencias tienen que sumar la cantidad de respuestas. Si no suman eso, se le pasó una o la contó dos veces. Tache cada respuesta de la lista a medida que la cuenta.</p>"))}
{enlace(n, t("frequency", "frecuencia"), t("frequency tables", "tablas de frecuencias"), t("Count the answers in a list.", "Cuente las respuestas de una lista."))}'''

    secciones = [("s-" + t("parts", "partes"), t("The parts of a table", "Las partes de una tabla"), s1),
                 ("s-" + t("find", "hallar"), t("Find, compare, and choose", "Hallar, comparar y escoger"), s2),
                 ("s-" + t("calculate", "calcular"), t("Calculate with a table: mean and range", "Calcular con una tabla: media y rango"), s3),
                 ("s-" + t("make", "hacer"), t("Make a frequency table", "Hacer una tabla de frecuencias"), s4)]

    lesson = {"next": t("Lesson 8.2", "Lección 8.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("28 is Luis in Week 1. Look in the Week 2 column.", "28 es Luis en la Semana 1. Mire en la columna de la Semana 2."), "c": t("40 is in the Week 2 column, but in Ana's row.", "40 está en la columna de la Semana 2, pero en la fila de Ana."), "d": t("38 is Rosa in Week 2. Find Luis's row.", "38 es Rosa en la Semana 2. Busque la fila de Luis.")},
             "right": t("Luis's row and the Week 2 column meet at 35.", "La fila de Luis y la columna de la Semana 2 se cruzan en 35."), "solution": t("Find Luis's row and the Week 2 column: 35 hours.", "Busque la fila de Luis y la columna de la Semana 2: 35 horas.")},
      "p2": {"ok": "c", "hints": {"a": t("Ana worked 32 hours in Week 1. Someone worked more.", "Ana trabajó 32 horas en la Semana 1. Alguien trabajó más."), "b": t("Luis worked 28 hours, the fewest.", "Luis trabajó 28 horas, la menor cantidad."), "d": t("Look at the Week 1 column: 32, 28, 40. They are different.", "Mire la columna de la Semana 1: 32, 28, 40. Son distintos.")},
             "right": t("Week 1: 32, 28, 40. The largest is 40, Rosa.", "Semana 1: 32, 28, 40. El mayor es 40, Rosa."), "solution": t("Look down the Week 1 column: 32, 28, 40. Rosa worked the most, 40 hours.", "Recorra la columna de la Semana 1: 32, 28, 40. Rosa trabajó más, 40 horas.")},
      "p3": {"ok": "a", "hints": {"b": t("8 is 40 − 32, the difference. \"In all\" means add.", "8 es 40 − 32, la diferencia. «En total» quiere decir sumar."), "c": t("40 is only Week 2. Add both weeks.", "40 es solo la Semana 2. Sume las dos semanas."), "d": t("1,280 multiplies. Add the two weeks.", "1,280 multiplica. Sume las dos semanas.")},
             "right": t("32 + 40 = 72 hours.", "32 + 40 = 72 horas."), "solution": t("Ana's row: 32 and 40. In all: 32 + 40 = 72 hours.", "La fila de Ana: 32 y 40. En total: 32 + 40 = 72 horas.")},
      "p4": {"ok": "d", "hints": {"a": t("108 is the sum. Now divide by 3, the number of weeks.", "108 es la suma. Ahora divida entre 3, la cantidad de semanas."), "b": t("8 is 40 − 32, the range, not the mean.", "8 es 40 − 32, el rango, no la media."), "c": t("40 is the largest value. The mean is in the middle.", "40 es el valor mayor. La media queda en medio.")},
             "right": t("(32 + 40 + 36) ÷ 3 = 108 ÷ 3 = 36.", "(32 + 40 + 36) ÷ 3 = 108 ÷ 3 = 36."), "solution": t("Add: 32 + 40 + 36 = 108. Divide by 3: 108 ÷ 3 = 36 hours.", "Sume: 32 + 40 + 36 = 108. Divida entre 3: 108 ÷ 3 = 36 horas.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("38 is the tacos on Tuesday. Look in the Tortas column.", "38 son los tacos del martes. Mire en la columna de Tortas."), "c": t("52 is the drinks on Tuesday.", "52 son las bebidas del martes."), "d": t("20 is the tortas on Monday. Find Tuesday's row.", "20 son las tortas del lunes. Busque la fila del martes.")}, "solution": t("Tuesday's row and the Tortas column meet at 25.", "La fila del martes y la columna de Tortas se cruzan en 25.")},
      "B": {"ok": "c", "hints": {"a": t("Monday: 60 drinks. Another day has more.", "Lunes: 60 bebidas. Otro día tiene más."), "b": t("Tuesday: 52 drinks, the fewest.", "Martes: 52 bebidas, la menor cantidad."), "d": t("Thursday: 65 drinks. Another day has more.", "Jueves: 65 bebidas. Otro día tiene más.")}, "solution": t("Drinks: 60, 52, 70, 65. The largest is 70, on Wednesday.", "Bebidas: 60, 52, 70, 65. La mayor es 70, el miércoles.")},
      "C": {"ok": "a", "hints": {"b": t("88 adds. \"How many more\" means subtract.", "88 suma. «Cuántos más» quiere decir restar."), "c": t("Check the subtraction: 50 − 38.", "Revise la resta: 50 − 38."), "d": t("Check the values: Wednesday 50, Tuesday 38.", "Revise los valores: miércoles 50, martes 38.")}, "solution": t("50 − 38 = 12 more tacos.", "50 − 38 = 12 tacos más.")},
      "D": {"ok": "d", "hints": {"a": t("30 is only Thursday. Add the four days.", "30 es solo el jueves. Sume los cuatro días."), "b": t("18 is only Wednesday. Add the four days.", "18 es solo el miércoles. Sume los cuatro días."), "c": t("Check the sum: 20 + 25 + 18 + 30.", "Revise la suma: 20 + 25 + 18 + 30.")}, "solution": t("20 + 25 + 18 + 30 = 93 tortas.", "20 + 25 + 18 + 30 = 93 tortas.")},
      "E": {"ok": "a", "hints": {"b": t("176 is the sum. Divide by 4, the number of days.", "176 es la suma. Divida entre 4, la cantidad de días."), "c": t("50 is the largest value. The mean is in the middle.", "50 es el valor mayor. La media queda en medio."), "d": t("38 is the smallest value. The mean is in the middle.", "38 es el valor menor. La media queda en medio.")}, "solution": t("45 + 38 + 50 + 43 = 176, and 176 ÷ 4 = 44 tacos.", "45 + 38 + 50 + 43 = 176, y 176 ÷ 4 = 44 tacos.")},
      "F": {"ok": "c", "hints": {"a": t("70 is the largest. The range is largest − smallest.", "70 es el mayor. El rango es mayor − menor."), "b": t("52 is the smallest. The range is largest − smallest.", "52 es el menor. El rango es mayor − menor."), "d": t("247 is the sum. The range subtracts.", "247 es la suma. El rango resta.")}, "solution": t("70 − 52 = 18 drinks.", "70 − 52 = 18 bebidas.")},
      "G": {"ok": "d", "hints": {"a": t("The title is above the table and tells what it is about.", "El título está arriba de la tabla y dice de qué trata."), "b": t("Rows go across, but the top row holds the column headers.", "Las filas son horizontales, pero la fila de arriba tiene los encabezados de columna."), "c": t("A cell is one piece of data.", "Una celda es un solo dato.")}, "solution": t("The words across the top tell what each column means: the column headers.", "Las palabras de arriba dicen qué quiere decir cada columna: los encabezados de columna.")},
      "H": {"ok": "b", "hints": {"a": t("8 is only the people who chose blue.", "8 son solo las personas que eligieron azul."), "c": t("3 is only green.", "3 es solo verde."), "d": t("5 is only red. Add all the frequencies.", "5 es solo rojo. Sume todas las frecuencias.")}, "solution": t("5 + 8 + 3 = 16 people.", "5 + 8 + 3 = 16 personas.")}
     }}

    quiz = [
     ("A", t("Use the food truck table. How many <strong>tortas</strong> were sold on <strong>Tuesday</strong>?", "Use la tabla del camión de comida. ¿Cuántas <strong>tortas</strong> se vendieron el <strong>martes</strong>?"), [("a", "38"), ("b", "25"), ("c", "52"), ("d", "20")]),
     ("B", t("Which day sold the most <strong>drinks</strong>?", "¿Qué día se vendieron más <strong>bebidas</strong>?"), [("a", t("Monday", "lunes")), ("b", t("Tuesday", "martes")), ("c", t("Wednesday", "miércoles")), ("d", t("Thursday", "jueves"))]),
     ("C", t("How many more tacos were sold on <strong>Wednesday</strong> than on <strong>Tuesday</strong>?", "¿Cuántos tacos más se vendieron el <strong>miércoles</strong> que el <strong>martes</strong>?"), [("a", "12"), ("b", "88"), ("c", "8"), ("d", "2")]),
     ("D", t("How many tortas were sold in all four days?", "¿Cuántas tortas se vendieron en total en los cuatro días?"), [("a", "30"), ("b", "18"), ("c", "75"), ("d", "93")]),
     ("E", t("What is the <strong>mean</strong> number of tacos sold per day?", "¿Cuál es la <strong>media</strong> de tacos vendidos por día?"), [("a", "44"), ("b", "176"), ("c", "50"), ("d", "38")]),
     ("F", t("What is the <strong>range</strong> of the drinks sold?", "¿Cuál es el <strong>rango</strong> de las bebidas vendidas?"), [("a", "70"), ("b", "52"), ("c", "18"), ("d", "247")]),
     ("G", t("In a table, the words across the top row are the:", "En una tabla, las palabras de la fila de arriba son los:"), [("a", t("title", "títulos")), ("b", t("rows", "filas")), ("c", t("cells", "celdas")), ("d", t("column headers", "encabezados de columna"))]),
     ("H", t("A frequency table shows: <strong>red 5, blue 8, green 3</strong>. How many people answered the survey?", "Una tabla de frecuencias muestra: <strong>rojo 5, azul 8, verde 3</strong>. ¿Cuántas personas respondieron la encuesta?"), [("a", "8"), ("b", "16"), ("c", "3"), ("d", "5")])]

    return B.pagina_leccion(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"),
        t("Reading and understanding data tables", "Leer e interpretar tablas de datos"),
        t("Rows, columns, and cells: read a table, compare its data, and summarize it with the mean and the range.", "Filas, columnas y celdas: lea una tabla, compare sus datos y resúmalos con la media y el rango."),
        ("📋", t("Row and column", "Fila y columna")),
        [t("<strong>Name</strong> the parts of a data table.", "<strong>Nombrar</strong> las partes de una tabla de datos."),
         t("<strong>Find</strong> a value and compare values in a table.", "<strong>Hallar</strong> un valor y comparar valores en una tabla."),
         t("<strong>Calculate</strong> totals, differences, the mean, and the range.", "<strong>Calcular</strong> totales, diferencias, la media y el rango."),
         t("<strong>Make</strong> a frequency table from a list of answers.", "<strong>Hacer</strong> una tabla de frecuencias a partir de una lista de respuestas.")],
        secciones,
        (t("Make a table of your expenses for one week: one row for each day and columns for food, transportation, and other. Find the total for each column and the mean spent per day.",
           "Haga una tabla de sus gastos de una semana: una fila para cada día y columnas para comida, transporte y otros. Halle el total de cada columna y la media gastada por día."),
         t("Ask 10 to 15 people a question with a few possible answers (favorite food, how they get to work). Make a frequency table with tally marks and check the total.",
           "Hágale a 10 o 15 personas una pregunta con pocas respuestas posibles (comida favorita, cómo llegan al trabajo). Haga una tabla de frecuencias con marcas de conteo y compruebe el total.")),
        quiz,
        t("Self-check checklist for data tables", "Lista de autoevaluación de tablas de datos"),
        t("Self-check checklist: skills for data tables", "Lista de autoevaluación: destrezas con tablas de datos"),
        [(t("The parts of a table", "Las partes de una tabla"), t("I read the title and the headers before the numbers.", "Leo el título y los encabezados antes que los números."), t("I sometimes skip the headers.", "A veces me salto los encabezados."), t("I look only at the numbers.", "Solo miro los números.")),
         (t("Find and compare", "Hallar y comparar"), t("I find any cell and answer \"how many more\" questions.", "Hallo cualquier celda y respondo preguntas de «cuántos más»."), t("I find cells, but comparing is harder.", "Hallo celdas, pero comparar me cuesta."), t("I mix up rows and columns.", "Confundo las filas y las columnas.")),
         (t("Mean and range", "Media y rango"), t("I find the mean and the range and explain what they mean.", "Hallo la media y el rango y explico lo que quieren decir."), t("I find the mean but forget to divide sometimes.", "Hallo la media, pero a veces olvido dividir."), t("I do not know how to find them yet.", "Todavía no sé hallarlos.")),
         (t("Frequency tables", "Tablas de frecuencias"), t("I make a frequency table and check the total.", "Hago una tabla de frecuencias y compruebo el total."), t("I make it, but I do not check the total.", "La hago, pero no compruebo el total."), t("I lose count of the answers.", "Pierdo la cuenta de las respuestas."))],
        t("<p>You can now read, compare, and summarize the data in a table.</p>\n<p>In <strong>Lesson 8.2 · Bar graphs and line graphs</strong> you will see the same kind of data as pictures, which make it easier to compare and to see how things change over time.</p>",
          "<p>Ya sabe leer, comparar y resumir los datos de una tabla.</p>\n<p>En la <strong>Lección 8.2 · Gráficas de barras y de líneas</strong> verá el mismo tipo de datos como dibujos, que facilitan comparar y ver cómo cambian las cosas con el tiempo.</p>"),
        ("8-2", ("", t("Lesson 8.2 · Bar graphs and line graphs", "Lección 8.2 · Gráficas de barras y de líneas"))),
        [(t("data", "datos"), t("Facts or numbers collected to answer a question.", "Hechos o números que se reúnen para responder una pregunta.")),
         (t("row and column", "fila y columna"), t("A row goes across a table; a column goes down.", "Una fila va horizontal en una tabla; una columna va vertical.")),
         (t("cell", "celda"), t("One box of a table, where a row and a column meet.", "Una casilla de una tabla, donde se cruzan una fila y una columna.")),
         (t("mean (average)", "media (promedio)"), t("The sum of the values divided by how many values there are.", "La suma de los valores dividida entre la cantidad de valores.")),
         (t("range", "rango"), t("The largest value minus the smallest value.", "El valor mayor menos el valor menor.")),
         (t("frequency", "frecuencia"), t("How many times something appears in a set of data.", "Cuántas veces aparece algo en un grupo de datos."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "ctx": [
   {"tit": "Food truck sales", "fila": "Day", "filas": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "cols": ["Tacos", "Tortas", "Drinks"], "colsQ": ["tacos", "tortas", "drinks"], "q": ["How many", "How many", "How many"], "rango": [15, 80],
    "preg": "{q} <strong>{c}</strong> were sold on <strong>{f}</strong>?", "mas": "{q} more <strong>{c}</strong> were sold on <strong>{f1}</strong> than on <strong>{f2}</strong>?", "total": "{q} <strong>{c}</strong> were sold in all?", "u": ""},
   {"tit": "Hours worked", "fila": "Employee", "filas": ["Ana", "Luis", "Rosa", "Marcos", "Carmen"], "cols": ["Week 1", "Week 2", "Week 3"], "colsQ": ["Week 1", "Week 2", "Week 3"], "q": ["", "", ""], "rango": [20, 45],
    "preg": "How many hours did <strong>{f}</strong> work in <strong>{c}</strong>?", "mas": "In <strong>{c}</strong>, how many more hours did <strong>{f1}</strong> work than <strong>{f2}</strong>?", "total": "How many hours did all the employees work in <strong>{c}</strong>?", "u": ""},
   {"tit": "Students in each class", "fila": "Class", "filas": ["Math", "Reading", "Science", "Social Studies", "Writing"], "cols": ["Monday", "Wednesday", "Friday"], "colsQ": ["Monday", "Wednesday", "Friday"], "q": ["", "", ""], "rango": [8, 30],
    "preg": "How many students were in <strong>{f}</strong> on <strong>{c}</strong>?", "mas": "On <strong>{c}</strong>, how many more students were in <strong>{f1}</strong> than in <strong>{f2}</strong>?", "total": "How many students were in all the classes on <strong>{c}</strong>?", "u": ""}],
  "filaMal": "That number is in the right row, but in another column.",
  "colMal": "That number is in the right column, but in another row.",
  "pistaLeer": "Find the row, find the column, and look where they meet.",
  "bienLeer": "The row {f} and the column {c} meet at <strong>{v}</strong>.",
  "solMas": "{f1}: {a}. {f2}: {b}. \"How many more\" means subtract: {a} − {b} = <strong>{r}</strong>.",
  "solTotal": "Add the {c} column: {suma} = <strong>{r}</strong>.",
  "sumaMas": "You added. \"How many more\" means subtract.",
  "unValor": "That is only one value. Add the whole column.",
  "pistaComp": "Find the values in the table first. \"How many more\": subtract. \"In all\": add.",
  "media": "{nom} {verbo} <strong>{lista}</strong>. What is the <strong>mean</strong>?",
  "rangoP": "{nom} {verbo} <strong>{lista}</strong>. What is the <strong>range</strong>?",
  "ctxM": [["The scores on five quizzes were", ""], ["A family's electric bills for {n} months were", "$"], ["The hours Rosa slept on {n} nights were", ""], ["The temperatures (°F) on {n} days were", ""]],
  "solMedia": "Add: {suma} = {s}. Divide by {n}: {s} ÷ {n} = <strong>{m}</strong>.",
  "solRango": "Largest: {M}. Smallest: {mi}. Range: {M} − {mi} = <strong>{r}</strong>.",
  "sinDividir": "That is the sum. Divide by how many values there are.",
  "esRango": "That is the range (largest − smallest), not the mean.",
  "esMedia": "That is the mean. The range is largest − smallest.",
  "mayorSolo": "That is the largest value. Subtract the smallest from it.",
  "pistaMedia": "Mean: add and divide by how many. Range: largest − smallest.",
  "y": "and",
  "frutas": ["apple", "mango", "banana", "grape", "orange"],
  "transporte": ["bus", "car", "train", "bike", "walking"],
  "pregFrec": "{q} Here are the answers:<br><span class=\"lista-datos\">{lista}</span><br>How many people answered <strong>{x}</strong>?",
  "preguntas": ["{n} people said their favorite fruit.", "{n} people said how they get to work."],
  "solFrec": "Count each \"{x}\" in the list: there are <strong>{r}</strong>.",
  "pistaFrec": "Count one answer at a time and cross it out, or make tally marks.",
  "frecTotal": "That is the total number of people. Count only \"{x}\"."
 },
 "es": {
  "ctx": [
   {"tit": "Ventas de un camión de comida", "fila": "Día", "filas": ["lunes", "martes", "miércoles", "jueves", "viernes"], "cols": ["Tacos", "Tortas", "Bebidas"], "colsQ": ["tacos", "tortas", "bebidas"], "q": ["Cuántos", "Cuántas", "Cuántas"], "rango": [15, 80],
    "preg": "¿{q} <strong>{c}</strong> se vendieron el <strong>{f}</strong>?", "mas": "¿{q} <strong>{c}</strong> más se vendieron el <strong>{f1}</strong> que el <strong>{f2}</strong>?", "total": "¿{q} <strong>{c}</strong> se vendieron en total?", "u": ""},
   {"tit": "Horas trabajadas", "fila": "Empleado", "filas": ["Ana", "Luis", "Rosa", "Marcos", "Carmen"], "cols": ["Semana 1", "Semana 2", "Semana 3"], "colsQ": ["Semana 1", "Semana 2", "Semana 3"], "q": ["", "", ""], "rango": [20, 45],
    "preg": "¿Cuántas horas trabajó <strong>{f}</strong> en la <strong>{c}</strong>?", "mas": "En la <strong>{c}</strong>, ¿cuántas horas más trabajó <strong>{f1}</strong> que <strong>{f2}</strong>?", "total": "¿Cuántas horas trabajaron todos los empleados en la <strong>{c}</strong>?", "u": ""},
   {"tit": "Estudiantes en cada clase", "fila": "Clase", "filas": ["Matemáticas", "Lectura", "Ciencias", "Estudios Sociales", "Escritura"], "cols": ["lunes", "miércoles", "viernes"], "colsQ": ["lunes", "miércoles", "viernes"], "q": ["", "", ""], "rango": [8, 30],
    "preg": "¿Cuántos estudiantes había en <strong>{f}</strong> el <strong>{c}</strong>?", "mas": "El <strong>{c}</strong>, ¿cuántos estudiantes más había en <strong>{f1}</strong> que en <strong>{f2}</strong>?", "total": "¿Cuántos estudiantes había en todas las clases el <strong>{c}</strong>?", "u": ""}],
  "filaMal": "Ese número está en la fila correcta, pero en otra columna.",
  "colMal": "Ese número está en la columna correcta, pero en otra fila.",
  "pistaLeer": "Busque la fila, busque la columna y mire dónde se cruzan.",
  "bienLeer": "La fila «{f}» y la columna «{c}» se cruzan en <strong>{v}</strong>.",
  "solMas": "{f1}: {a}. {f2}: {b}. «Cuántos más» quiere decir restar: {a} − {b} = <strong>{r}</strong>.",
  "solTotal": "Sume la columna «{c}»: {suma} = <strong>{r}</strong>.",
  "sumaMas": "Sumó. «Cuántos más» quiere decir restar.",
  "unValor": "Ese es un solo valor. Sume toda la columna.",
  "pistaComp": "Primero halle los valores en la tabla. «Cuántos más»: reste. «En total»: sume.",
  "media": "{nom} {verbo} <strong>{lista}</strong>. ¿Cuál es la <strong>media</strong>?",
  "rangoP": "{nom} {verbo} <strong>{lista}</strong>. ¿Cuál es el <strong>rango</strong>?",
  "ctxM": [["Las notas de cinco pruebas fueron", ""], ["Las facturas de luz de una familia durante {n} meses fueron", "$"], ["Las horas que Rosa durmió en {n} noches fueron", ""], ["Las temperaturas (°F) de {n} días fueron", ""]],
  "solMedia": "Sume: {suma} = {s}. Divida entre {n}: {s} ÷ {n} = <strong>{m}</strong>.",
  "solRango": "Mayor: {M}. Menor: {mi}. Rango: {M} − {mi} = <strong>{r}</strong>.",
  "sinDividir": "Esa es la suma. Divida entre la cantidad de valores.",
  "esRango": "Ese es el rango (mayor − menor), no la media.",
  "esMedia": "Esa es la media. El rango es mayor − menor.",
  "mayorSolo": "Ese es el valor mayor. Réstele el menor.",
  "pistaMedia": "Media: sume y divida entre la cantidad de valores. Rango: mayor − menor.",
  "y": "y",
  "frutas": ["manzana", "mango", "plátano", "uva", "naranja"],
  "transporte": ["autobús", "carro", "tren", "bicicleta", "a pie"],
  "pregFrec": "{q} Estas son las respuestas:<br><span class=\"lista-datos\">{lista}</span><br>¿Cuántas personas respondieron <strong>{x}</strong>?",
  "preguntas": ["{n} personas dijeron su fruta favorita.", "{n} personas dijeron cómo llegan al trabajo."],
  "solFrec": "Cuente cada «{x}» de la lista: hay <strong>{r}</strong>.",
  "pistaFrec": "Cuente una respuesta a la vez y táchela, o haga marcas de conteo.",
  "frecTotal": "Ese es el total de personas. Cuente solo «{x}»."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function hazTabla(){
  var c = elige(TXT.ctx), nf = 4, filas = c.filas.slice(0, nf), D = [];
  for (var i = 0; i < nf; i++){ var r = []; for (var j = 0; j < 3; j++) r.push(aleatorio(c.rango[0], c.rango[1])); D.push(r); }
  var h = '<p class="titulo-tabla" aria-hidden="true">' + c.tit + '</p><table class="reglas tabla-datos"><caption class="cap-oculto">' + c.tit + '</caption><thead><tr><th scope="col">' + c.fila + '</th>' + c.cols.map(function(x){ return '<th scope="col">' + x + '</th>'; }).join("") + '</tr></thead><tbody>';
  for (i = 0; i < nf; i++) h += '<tr><th scope="row">' + filas[i] + '</th>' + D[i].map(function(x){ return "<td>" + x + "</td>"; }).join("") + "</tr>";
  return { c: c, filas: filas, D: D, html: h + "</tbody></table>" };
}

/* ============ MODULE 1 · read a cell ============ */
function genLeer(){
  var T = hazTabla(), i = aleatorio(0, 3), j = aleatorio(0, 2), v = T.D[i][j], op = [{ html: String(v), clave: "ok" }], pistas = {};
  function mete(x, msg){ if (op.some(function(o){ return o.html === String(x); })) return; op.push({ html: String(x), clave: "k" + op.length }); pistas["k" + (op.length - 1)] = msg; }
  mete(T.D[i][(j + 1) % 3], TXT.filaMal); mete(T.D[(i + 1) % 4][j], TXT.colMal); mete(T.D[(i + 2) % 4][(j + 2) % 3], TXT.pistaLeer);
  if (op.length < 4) mete(T.D[(i + 3) % 4][j], TXT.colMal);
  for (var a = 0; a < 4 && op.length < 4; a++) for (var b = 0; b < 3 && op.length < 4; b++) if (a !== i || b !== j) mete(T.D[a][b], a === i ? TXT.filaMal : (b === j ? TXT.colMal : TXT.pistaLeer));
  var txt = F(TXT.bienLeer, { f: T.filas[i], c: T.c.cols[j], v: v });
  return { enun: T.html + F(T.c.preg, { c: T.c.colsQ[j], q: T.c.q[j], f: T.filas[i] }), opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaLeer, bien: txt, mal: txt };
}

/* ============ MODULE 2 · compare and add ============ */
function genComp(){
  var T = hazTabla(), j = aleatorio(0, 2), p = [];
  if (Math.random() < 0.6){
    var i1 = aleatorio(0, 3), i2 = (i1 + aleatorio(1, 3)) % 4, a = T.D[i1][j], b = T.D[i2][j];
    if (a === b){ T.D[i1][j] = a = b + aleatorio(2, 9); T = rehaz(T); }
    if (a < b){ var x = i1; i1 = i2; i2 = x; x = a; a = b; b = x; }
    p.push({ v: a + b, msg: TXT.sumaMas });
    return { enun: T.html + F(T.c.mas, { c: T.c.colsQ[j], q: T.c.q[j], f1: T.filas[i1], f2: T.filas[i2] }), solucion: F(TXT.solMas, { f1: T.filas[i1], f2: T.filas[i2], a: a, b: b, r: a - b }), evalua: numN(a - b, p, TXT.pistaComp) };
  }
  var col = T.D.map(function(r){ return r[j]; }), s = col.reduce(function(a, b){ return a + b; }, 0);
  col.forEach(function(v){ if (v !== s) p.push({ v: v, msg: TXT.unValor }); });
  return { enun: T.html + F(T.c.total, { c: T.c.colsQ[j], q: T.c.q[j] }), solucion: F(TXT.solTotal, { c: T.c.cols[j], suma: col.join(" + "), r: s }), evalua: numN(s, p, TXT.pistaComp) };
}
function rehaz(T){
  var c = T.c, h = '<p class="titulo-tabla" aria-hidden="true">' + c.tit + '</p><table class="reglas tabla-datos"><caption class="cap-oculto">' + c.tit + '</caption><thead><tr><th scope="col">' + c.fila + '</th>' + c.cols.map(function(x){ return '<th scope="col">' + x + '</th>'; }).join("") + '</tr></thead><tbody>';
  for (var i = 0; i < 4; i++) h += '<tr><th scope="row">' + T.filas[i] + '</th>' + T.D[i].map(function(x){ return "<td>" + x + "</td>"; }).join("") + "</tr>";
  T.html = h + "</tbody></table>"; return T;
}

/* ============ MODULE 3 · mean and range ============ */
function genMedia(){
  var k = aleatorio(0, TXT.ctxM.length - 1), n = k === 0 ? 5 : aleatorio(3, 6), base = [[60, 100], [40, 120], [5, 9], [55, 85]][k], m = aleatorio(base[0] + 3, base[1] - 3), L = [];
  for (var i = 0; i < n - 1; i++) L.push(aleatorio(base[0], base[1]));
  var ultimo = m * n - L.reduce(function(a, b){ return a + b; }, 0);
  if (ultimo < base[0] || ultimo > base[1]) return genMedia();
  L.push(ultimo); L = baraja(L);
  var pre = TXT.ctxM[k][1], lst = L.map(function(x){ return pre + x; }), lista = lst.slice(0, -1).join(", ") + " " + TXT.y + " " + lst[n - 1];
  var s = m * n, M = Math.max.apply(null, L), mi = Math.min.apply(null, L), p = [], nom = F(TXT.ctxM[k][0], { n: n });
  if (Math.random() < 0.65){
    p.push({ v: s, msg: TXT.sinDividir }); if (M - mi !== m) p.push({ v: M - mi, msg: TXT.esRango });
    return { enun: F(TXT.media, { nom: nom, verbo: "", lista: lista }).replace("  ", " "), solucion: F(TXT.solMedia, { suma: L.join(" + "), s: s, n: n, m: m }), evalua: numN(m, p, TXT.pistaMedia) };
  }
  if (m !== M - mi) p.push({ v: m, msg: TXT.esMedia }); if (M !== M - mi) p.push({ v: M, msg: TXT.mayorSolo });
  return { enun: F(TXT.rangoP, { nom: nom, verbo: "", lista: lista }).replace("  ", " "), solucion: F(TXT.solRango, { M: pre + M, mi: pre + mi, r: pre + (M - mi) }), evalua: numN(M - mi, p, TXT.pistaMedia) };
}

/* ============ MODULE 4 · frequency ============ */
function genFrec(){
  var g = Math.random() < 0.5 ? 0 : 1, ops = (g === 0 ? TXT.frutas : TXT.transporte).slice(0, aleatorio(3, 5)), n = aleatorio(10, 18), L = [];
  for (var i = 0; i < n; i++) L.push(elige(ops));
  var x = elige(ops), r = L.filter(function(y){ return y === x; }).length, p = [];
  if (r === 0) return genFrec();
  if (n !== r) p.push({ v: n, msg: F(TXT.frecTotal, { x: x }) });
  return { enun: F(TXT.pregFrec, { q: F(TXT.preguntas[g], { n: n }), lista: L.join(", "), x: x }), solucion: F(TXT.solFrec, { x: x, r: r }), evalua: numN(r, p, TXT.pistaFrec) };
}

creaPracticaOM("p1", genLeer);
creaPracticaLibre("p2", genComp);
creaPracticaLibre("p3", genMedia);
creaPracticaLibre("p4", genFrec);
'''

def practica_pagina():
    n = N
    mods = [
     (t("read", "leer"), t("Read a table", "Leer una tabla"),
      f'''      <p>{t("Read the title and the headers first. Then find the row, find the column, and look where they meet.", "Lea primero el título y los encabezados. Después busque la fila, busque la columna y mire dónde se cruzan.")}</p>
{B.om("p1", t("Practice: read a cell", "Practique: leer una celda"))}'''),
     (t("compare", "comparar"), t("Compare and add", "Comparar y sumar"),
      f'''      <p>{t("<strong>\"How many more\"</strong> means subtract the two values. <strong>\"In all\"</strong> means add the values.", "<strong>«Cuántos más»</strong> quiere decir restar los dos valores. <strong>«En total»</strong> quiere decir sumar los valores.")}</p>
{B.libre("p2", t("Practice: use the table", "Practique: use la tabla"), t("Answer", "Respuesta"))}'''),
     (t("mean-range", "media-rango"), t("Mean and range", "Media y rango"),
      f'''      <table class="reglas">
        <caption>{t("Summary numbers", "Números que resumen")}</caption>
        <tbody>
          <tr><td>{t("mean", "media")}</td><td>{t("add all the values and divide by how many there are", "sume todos los valores y divida entre la cantidad de valores")}</td></tr>
          <tr><td>{t("range", "rango")}</td><td>{t("largest value − smallest value", "valor mayor − valor menor")}</td></tr>
        </tbody>
      </table>
{B.libre("p3", t("Practice: mean or range", "Practique: media o rango"), t("Answer", "Respuesta"))}'''),
     (t("frequency", "frecuencia"), t("Frequency tables", "Tablas de frecuencias"),
      f'''      <p>{t("Count how many times one answer appears. Cross out each answer as you count it, or make tally marks: |||| for 4, and a line across for 5.", "Cuente cuántas veces aparece una respuesta. Tache cada respuesta a medida que la cuenta, o haga marcas de conteo: |||| para 4, y una raya atravesada para 5.")}</p>
{B.libre("p4", t("Practice: count the answers", "Practique: contar las respuestas"), t("Answer", "Respuesta"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"), t("Reading and understanding data tables", "Leer e interpretar tablas de datos"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun .titulo-tabla{text-align:center;margin:6px 0 2px;}\n.enun table.tabla-datos{margin:4px auto 12px;font-weight:400;min-width:280px;}\n.enun table.tabla-datos td{text-align:center;}\n.enun .lista-datos{display:block;font-weight:400;margin:6px 0;line-height:1.7;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Leer e interpretar tablas de datos")
