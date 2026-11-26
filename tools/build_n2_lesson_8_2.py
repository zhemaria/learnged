"""Level 2 · Lesson 8.2 · Circle graphs: read, interpret, and make — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json, math
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "8-2"
TEMA = ("Statistics and probability", "Estadística y probabilidad")
TIT = ("Circle graphs: read, interpret, and make", "Gráficos circulares: leer, interpretar y construir")
COLS = ["#c62828", "#1565c0", "#2e7d32", "#8a5a00", "#6a1b9a", "#00695c"]

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.3rem;font-weight:700;color:#0d47a1">{x}</p>'

def pie(datos, voz):
    cx, cy, R, a0 = 160, 150, 120, 90
    s = ""
    for i, (nom, p) in enumerate(datos):
        ang = 360 * p / 100
        a1 = a0 - ang
        P = lambda a, r=R: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
        p0, p1 = P(a0), P(a1)
        s += f'<path d="M{cx} {cy} L{p0[0]:.1f} {p0[1]:.1f} A{R} {R} 0 {1 if ang > 180 else 0} 1 {p1[0]:.1f} {p1[1]:.1f} Z" fill="{COLS[i]}" stroke="#fff" stroke-width="2"/>'
        pm = P(a0 - ang / 2, R * 0.64)
        s += f'<text x="{pm[0]:.1f}" y="{pm[1]:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="17" font-weight="700" fill="#fff">{p}%</text>'
        a0 = a1
        ly = 50 + i * 34
        s += f'<rect x="320" y="{ly - 10}" width="20" height="20" rx="3" fill="{COLS[i]}"/><text x="350" y="{ly}" dominant-baseline="middle" font-size="19" fill="#222">{nom} — {p}%</text>'
    return svg("0 0 640 300", voz, s, 640)

def presu():
    return [(t("Food", "Comida"), 35), (t("Rent", "Renta"), 30), (t("Transportation", "Transporte"), 15), (t("Health", "Salud"), 10), (t("Free time", "Ocio"), 10)]

def leccion():
    n = N
    PRESU = presu()
    voz = t("Circle graph of a monthly budget: food 35 percent, rent 30, transportation 15, health 10, and free time 10.", "Gráfico circular de un presupuesto mensual: comida 35 por ciento, renta 30, transporte 15, salud 10 y ocio 10.")
    s1 = f'''<p>{t("This lesson brings together two threads of Level 2. From Topic 5 comes the idea of a percent as a ratio out of 100; from Topic 7, the circle. A circle graph joins them: the whole circle stands for 100% of the data, and each slice is a part proportional to its percent. It is one of the most common ways to show data in newspapers, reports, and presentations.", "Esta lección reúne dos hilos del Nivel 2. Del Tema 5 viene la idea de porcentaje como razón con denominador 100; del Tema 7, el círculo. El gráfico circular los une: el círculo entero representa el 100% de los datos, y cada sector es una parte proporcional a su porcentaje. Es una de las formas más comunes de presentar datos en periódicos, informes y presentaciones.")}</p>
<p>{t("A <strong>circle graph</strong> (also called a <em>pie chart</em>) is a circle divided into slices, or <strong>sectors</strong>. The size of each sector matches the percent of its category. The most important rule: <strong>all the percents must add up to 100%</strong>, because the whole circle is the total.", "Un <strong>gráfico circular</strong> (en inglés, <em>pie chart</em>) es un círculo dividido en <strong>sectores</strong>. El tamaño de cada sector corresponde al porcentaje de su categoría. La regla más importante: <strong>todos los porcentajes deben sumar 100%</strong>, porque el círculo entero es el total.")}</p>
<div style="text-align:center">{pie(PRESU, voz)}</div>
<p>{t("At a glance you see that food is the largest category, followed by rent. Health and free time are the smallest and are tied. That instant visual reading is the great advantage of a circle graph: you can compare categories without reading a list of numbers.", "De un vistazo se ve que la comida es la mayor categoría, seguida por la renta. Salud y ocio son los sectores más pequeños y están empatados. Esa lectura visual instantánea es la gran ventaja del gráfico circular: permite comparar categorías sin leer una lista de números.")}</p>
{caja("tip", t("When a circle graph is a good choice", "Cuándo conviene un gráfico circular"), t("<p>It is ideal to show <strong>how a whole is divided</strong>: how a budget is spent, what percent of people live in each neighborhood, how a day is used. It is not the best choice to show change over time (that calls for a line graph) or for many very small categories (the slices become hard to read).</p>", "<p>Es ideal para mostrar <strong>cómo se reparte un total</strong>: cómo se gasta un presupuesto, qué porcentaje de la población vive en cada barrio, cómo se distribuye un día. No es la mejor opción para mostrar cambios a lo largo del tiempo (eso pide un gráfico de líneas) ni para muchas categorías muy pequeñas (los sectores se vuelven ilegibles).</p>"))}
{enlace(n, t("what-it-is", "que-es"), t("what a circle graph is", "qué es un gráfico circular"), t("Check that the sectors add up to 100% and find the missing percent.", "Compruebe que los sectores suman 100% y encuentre el porcentaje que falta."))}'''

    s2 = f'''<p>{t("To make a circle graph you change each percent into a <strong>central angle</strong>: the angle of the sector measured at the center of the circle. The whole circle is 360° and stands for 100%, so the rule is:", "Para construir un gráfico circular hace falta convertir cada porcentaje en un <strong>ángulo central</strong>: el ángulo del sector medido desde el centro del círculo. Como el círculo completo abarca 360° y representa el 100%, la regla es:")}</p>
{big(t("angle = 360° × (percent ÷ 100)", "ángulo = 360° × (porcentaje ÷ 100)"))}
<p style="text-align:center">{t("A direct proportion between percent and angle, like the ones in Topic 4.", "Una proporción directa entre porcentaje y ángulo, como las del Tema 4.")}</p>
{ej(t("Example: from percent to angle", "Ejemplo: del porcentaje al ángulo"), t("How many degrees does a 25% sector take up?", "¿Cuántos grados ocupa un sector del 25%?"),
  [("1", t("Formula.", "Fórmula."), "360° × (25 ÷ 100) = 360° × 0.25."),
   ("2", t("Multiply.", "Multiplique."), "360° × 0.25 = 90°."),
   ("✓", t("Answer.", "Respuesta."), t("The 25% sector has a central angle of <strong>90°</strong>: exactly one fourth of the circle.", "El sector del 25% ocupa un ángulo central de <strong>90°</strong>: exactamente un cuarto del círculo."))])}
{caja("tip", t("Handy shortcuts", "Atajos útiles"), t("<p>100% = 360° · 50% = 180° (half the circle) · 25% = 90° (a fourth) · 10% = 36° · 1% = 3.6°. Recognizing them quickly lets you check that a sector has a reasonable size.</p>", "<p>100% = 360° · 50% = 180° (medio círculo) · 25% = 90° (un cuarto) · 10% = 36° · 1% = 3.6°. Reconocerlos al vuelo permite comprobar que un sector tiene un tamaño razonable.</p>"))}
<p>{t("For the budget above, with a monthly income of $2,000, the full table shows the three equivalent forms: percent, angle, and dollar amount.", "Para el presupuesto anterior, con un ingreso mensual de $2,000, la tabla completa muestra las tres formas equivalentes: porcentaje, ángulo y cantidad en dólares.")}</p>
{tabla(t("The budget table", "La tabla del presupuesto"), t("Percent, central angle, and dollar amount of each category", "Porcentaje, ángulo central y cantidad en dólares de cada categoría"),
       [t("Category", "Categoría"), t("Percent", "Porcentaje"), t("Central angle", "Ángulo central"), t("Amount", "Cantidad")],
       [[PRESU[0][0], "35%", "126°", "$700"], [PRESU[1][0], "30%", "108°", "$600"], [PRESU[2][0], "15%", "54°", "$300"], [PRESU[3][0], "10%", "36°", "$200"], [PRESU[4][0], "10%", "36°", "$200"],
        [t("<strong>Total</strong>", "<strong>Total</strong>"), "<strong>100%</strong>", "<strong>360°</strong>", "<strong>$2,000</strong>"]])}
<p>{t("The <strong>Total</strong> row is your safety check: if the percents do not add to 100%, the angles to 360°, or the amounts to the real total, there is a mistake in some row. Always find it.", "La fila <strong>Total</strong> es el sello de seguridad: si los porcentajes no suman 100%, los ángulos no suman 360° o las cantidades no suman el total real, hay un error en alguna fila. Conviene calcularla siempre.")}</p>
{practica("p1", t("Practice 1 — 20%", "Práctica 1 — El 20%"), t("What central angle does a 20% sector take up?", "¿Qué ángulo central ocupa un sector del 20%?"), [("a", "20°"), ("b", "72°"), ("c", "7.2°"), ("d", "288°")])}
{practica("p2", t("Practice 2 — 75%", "Práctica 2 — El 75%"), t("What central angle does a 75% sector take up?", "¿Qué ángulo central ocupa un sector del 75%?"), [("a", "270°"), ("b", "75°"), ("c", "210°"), ("d", "300°")])}
{enlace(n, t("angle", "angulo"), t("the central angle of each sector", "el ángulo central de cada sector"), t("Move the sector and see how the percent and the degrees are related.", "Mueva el sector y vea la relación entre el porcentaje y los grados."))}'''

    s3 = f'''<p>{t("The three forms of a sector are connected. If you know any one of them and the real total, you can find the other two.", "Las tres formas de expresar un sector están conectadas. Conociendo cualquiera de ellas y el total real, se obtienen las otras dos.")}</p>
{ej(t("Example: from percent to amount", "Ejemplo: del porcentaje a la cantidad"), t("In the budget, “Health” is 10%. How many dollars is that, if the total is $2,000?", "En el presupuesto, «Salud» ocupa el 10%. ¿A cuántos dólares equivale, si el total es $2,000?"),
  [("1", t("The rule from Topic 5.", "La regla del Tema 5."), t("amount = total × (percent ÷ 100).", "cantidad = total × (porcentaje ÷ 100).")),
   ("2", t("Multiply.", "Multiplique."), "2,000 × 0.10 = $200."),
   ("✓", t("Answer.", "Respuesta."), t("“Health” is <strong>$200</strong> of the monthly budget.", "«Salud» equivale a <strong>$200</strong> del presupuesto mensual."))])}
{ej(t("Example: from angle to percent", "Ejemplo: del ángulo al porcentaje"), t("A sector has a central angle of 72°. What percent does it stand for?", "Un sector tiene un ángulo central de 72°. ¿Qué porcentaje representa?"),
  [("1", t("Solve the formula.", "Despeje la fórmula."), t("percent = (angle ÷ 360°) × 100.", "porcentaje = (ángulo ÷ 360°) × 100.")),
   ("2", t("Calculate.", "Calcule."), "(72 ÷ 360) × 100 = 0.2 × 100 = 20."),
   ("✓", t("Answer.", "Respuesta."), t("The sector stands for <strong>20%</strong> of the total.", "El sector representa el <strong>20%</strong> del total."))])}
{caja("ojo", t("Watch the units", "Atención a las unidades"), t("<p>Angles go in degrees (°), percents in %, and amounts in the unit of the problem ($, people, hours). Mixing them up is a common mistake. Before you write the answer, ask yourself: “What unit should this be in?”</p>", "<p>Los ángulos van en grados (°), los porcentajes en % y las cantidades en la unidad del problema ($, personas, horas). Confundirlos es un error frecuente. Antes de escribir la respuesta, pregúntese: «¿en qué unidad debe ir esto?».</p>"))}
{practica("p3", t("Practice 3 — From angle to percent", "Práctica 3 — Del ángulo al porcentaje"), t("A sector has a central angle of 72°. What percent is it?", "Un sector tiene un ángulo central de 72°. ¿Qué porcentaje es?"), [("a", "72%"), ("b", "25%"), ("c", "20%"), ("d", "259.2%")])}
{practica("p4", t("Practice 4 — From percent to amount", "Práctica 4 — Del porcentaje a la cantidad"), t("A monthly budget is $1,500. Rent is 40%. How much is the rent?", "Un presupuesto mensual es de $1,500. La renta es el 40%. ¿Cuánto es la renta?"), [("a", "$40"), ("b", "$144"), ("c", "$900"), ("d", "$600")])}
{enlace(n, t("conversions", "conversiones"), t("percent, angle, and amount", "porcentaje, ángulo y cantidad"), t("Change the income of the budget and go from one form to the other two.", "Cambie el ingreso del presupuesto y pase de una forma a las otras dos."))}'''

    s4 = f'''<p>{t("Making a circle graph by hand, with a compass and a protractor, helps you understand the geometry behind it. The steps are always the same:", "Construir un gráfico circular a mano, con compás y transportador, ayuda a entender la geometría que hay detrás. El procedimiento es siempre el mismo:")}</p>
{tabla(t("How to make a circle graph", "Cómo construir un gráfico circular"), t("Steps to make a circle graph", "Pasos para construir un gráfico circular"),
       [t("Step", "Paso"), t("What to do", "Qué hacer")],
       [["1", t("Check that the percents add up to 100%. If they do not, fix that first. (If you have counts, first divide each one by the total.)", "Compruebe que los porcentajes suman 100%. Si no, corríjalo antes de seguir. (Si tiene conteos, primero divida cada uno entre el total.)")],
        ["2", t("Find the central angle of each category: 360° × (percent ÷ 100).", "Calcule el ángulo central de cada categoría: 360° × (porcentaje ÷ 100).")],
        ["3", t("Draw a circle with the compass. Mark the center and draw a radius straight up as the starting line.", "Dibuje un círculo con el compás. Marque el centro y trace un radio vertical hacia arriba como punto de partida.")],
        ["4", t("Measure the first angle with the protractor from the starting radius and draw the second radius.", "Mida el primer ángulo con el transportador desde el radio inicial y trace el segundo radio.")],
        ["5", t("Keep going: measure each new angle from the <strong>last</strong> radius, not from the first one.", "Continúe: cada ángulo nuevo se mide desde el <strong>último</strong> radio, no desde el inicial.")],
        ["6", t("Color and label each sector with its category and percent.", "Coloree y rotule cada sector con su categoría y su porcentaje.")],
        ["7", t("Check: the last radius must land on the first one. If it does not, a measurement is off.", "Compruebe: el último radio debe coincidir con el primero. Si no, hay un error de medida.")]])}
{caja("tip", t("A visual tip", "Sugerencia visual"), t("<p>Ordering the categories from largest to smallest before you draw usually gives a cleaner graph. The smallest sectors end up together and are easier to label from outside, with guide lines if needed.</p>", "<p>Ordenar las categorías de mayor a menor antes de dibujar suele dar un gráfico más limpio. Los sectores más pequeños quedan juntos al final y son más fáciles de rotular por fuera, con líneas guía si hace falta.</p>"))}
{enlace(n, t("build", "construir"), t("making a circle graph", "construir un gráfico circular"), t("Type the counts of each category and watch the table and the graph build themselves.", "Escriba los conteos de cada categoría y vea cómo se arman la tabla y el gráfico."))}'''

    dia = [(t("Sleep", "Sueño"), 33), (t("Work", "Trabajo"), 38), (t("Meals", "Comidas"), 8), (t("Family", "Familia"), 13), (t("Free time", "Ocio"), 8)]
    s5 = f'''<p>{t("Reading a circle graph is the most common skill, on the GED test and in daily life. It means finding the largest and the smallest category, comparing two sectors, and sometimes finding the actual amount of one of them.", "Leer un gráfico circular es la habilidad más común, en el examen GED y en la vida cotidiana. Implica reconocer la categoría mayor y la menor, comparar dos sectores y, a veces, calcular la cantidad real de uno de ellos.")}</p>
<div style="text-align:center">{pie(dia, t("Circle graph of a worker's 24-hour day: sleep 33 percent, work 38, meals 8, family 13, and free time 8.", "Gráfico circular del día de 24 horas de un trabajador: sueño 33 por ciento, trabajo 38, comidas 8, familia 13 y ocio 8."))}</div>
{ej(t("Example: how a day is spent", "Ejemplo: cómo se reparte el día"), t("The graph shows how a worker spends a 24-hour day. Which is the largest category, and how many hours is it?", "El gráfico muestra cómo reparte su tiempo un trabajador en un día de 24 horas. ¿Cuál es la categoría mayor y cuántas horas son?"),
  [("1", t("Check the sum.", "Compruebe la suma."), "33 + 38 + 8 + 13 + 8 = 100%. ✓"),
   ("2", t("The largest.", "La mayor."), t("Work, with 38%.", "Trabajo, con un 38%.")),
   ("3", t("In hours.", "En horas."), t("24 × 0.38 = 9.12 hours, about 9 hours and 7 minutes.", "24 × 0.38 = 9.12 horas, unas 9 horas y 7 minutos.")),
   ("✓", t("Reading.", "Lectura."), t("The worker spends <strong>about 9 hours</strong> a day at work, more than on any other activity.", "El trabajador dedica al trabajo <strong>unas 9 horas</strong> diarias, más que a cualquier otra actividad."))])}
{practica("p5", t("Practice 5 — People", "Práctica 5 — Personas"), t("A sector is 50% of a population of 800 people. How many people does it stand for?", "Un sector vale el 50% de una población de 800 personas. ¿A cuántas personas representa?"), [("a", "200"), ("b", "400"), ("c", "50"), ("d", "800")])}
{practica("p6", t("Practice 6 — 180°", "Práctica 6 — 180°"), t("A sector with a central angle of 180° stands for…", "Un sector de ángulo central 180° representa…"), [("a", "50%"), ("b", "25%"), ("c", "33%"), ("d", "180%")])}
{practica("p7", t("Practice 7 — What it is for", "Práctica 7 — Para qué sirve"), t("A circle graph is most useful to show…", "Un gráfico circular sirve sobre todo para representar…"),
          [("a", t("change over time", "el cambio a lo largo del tiempo")), ("b", t("how a whole is divided", "cómo se reparte un total")), ("c", t("the exact value of each person", "el valor exacto de cada persona")), ("d", t("a list of dates", "una lista de fechas"))])}
{enlace(n, t("read", "leer"), t("reading real graphs", "leer e interpretar gráficos reales"), t("Find the largest sector, compare categories, and find the real amount of a part.", "Identifique el sector mayor, compare categorías y calcule la cantidad real de una parte."))}'''

    secciones = [("s-" + t("what-it-is", "que-es"), t("What a circle graph is", "Qué es un gráfico circular"), s1),
                 ("s-" + t("angle", "angulo"), t("The central angle of each sector", "El ángulo central de cada sector"), s2),
                 ("s-" + t("conversions", "conversiones"), t("Percent, angle, and amount", "Porcentaje, ángulo y cantidad"), s3),
                 ("s-" + t("build", "construir"), t("How to make a circle graph", "Cómo construir un gráfico circular"), s4),
                 ("s-" + t("read", "leer"), t("Reading real graphs", "Leer e interpretar gráficos reales"), s5)]

    lesson = {"next": t("Lesson 8.3", "Lección 8.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The percent is not the angle. Multiply 360° by 0.20.", "El porcentaje no es el ángulo. Multiplique 360° por 0.20."), "c": t("Check the decimal point: 360 × 0.20.", "Revise el punto decimal: 360 × 0.20."), "d": t("That is the angle of the rest of the circle.", "Ese es el ángulo del resto del círculo.")},
             "right": t("360° × 0.20 = 72°.", "360° × 0.20 = 72°."), "solution": t("360° × (20 ÷ 100) = 72°.", "360° × (20 ÷ 100) = 72°.")},
      "p2": {"ok": "a", "hints": {"b": t("The percent is not the angle.", "El porcentaje no es el ángulo."), "c": t("Check: 360 × 0.75.", "Revise: 360 × 0.75."), "d": t("Check: 360 × 0.75.", "Revise: 360 × 0.75.")},
             "right": t("360° × 0.75 = 270°: three fourths of the circle.", "360° × 0.75 = 270°: tres cuartos del círculo."), "solution": t("360° × 0.75 = 270°.", "360° × 0.75 = 270°.")},
      "p3": {"ok": "c", "hints": {"a": t("The angle is not the percent. Divide by 360.", "El ángulo no es el porcentaje. Divida entre 360."), "b": t("25% would be 90°.", "El 25% serían 90°."), "d": t("You multiplied by 3.6. To go from angle to percent, divide by 3.6.", "Multiplicó por 3.6. Del ángulo al porcentaje se divide entre 3.6.")},
             "right": t("72 ÷ 360 = 0.2 = 20%.", "72 ÷ 360 = 0.2 = 20%."), "solution": t("(72 ÷ 360) × 100 = 20%.", "(72 ÷ 360) × 100 = 20%.")},
      "p4": {"ok": "d", "hints": {"a": t("That is the percent. Multiply the total by 0.40.", "Ese es el porcentaje. Multiplique el total por 0.40."), "b": t("That is the angle (40% × 3.6). The question asks for dollars.", "Ese es el ángulo (40% × 3.6). Se piden dólares."), "c": t("That is the other 60%.", "Ese es el otro 60%.")},
             "right": t("1,500 × 0.40 = $600.", "1,500 × 0.40 = $600."), "solution": t("Amount = 1,500 × 0.40 = $600.", "Cantidad = 1,500 × 0.40 = $600.")},
      "p5": {"ok": "b", "hints": {"a": t("200 would be 25%.", "200 sería el 25%."), "c": t("50 is the percent, not the people.", "50 es el porcentaje, no las personas."), "d": t("800 is the whole population.", "800 es toda la población.")},
             "right": t("800 × 0.50 = 400 people.", "800 × 0.50 = 400 personas."), "solution": t("Half of 800 is 400.", "La mitad de 800 es 400.")},
      "p6": {"ok": "a", "hints": {"b": t("25% is 90°.", "El 25% son 90°."), "c": t("Check: 180 ÷ 360.", "Revise: 180 ÷ 360."), "d": t("The angle is not the percent. Divide by 360.", "El ángulo no es el porcentaje. Divida entre 360.")},
             "right": t("180° is half the circle: 50%.", "180° es medio círculo: el 50%."), "solution": t("180 ÷ 360 = 0.5 = 50%.", "180 ÷ 360 = 0.5 = 50%.")},
      "p7": {"ok": "b", "hints": {"a": t("Change over time calls for a line graph.", "El cambio en el tiempo pide un gráfico de líneas."), "c": t("A circle graph shows parts of a whole, not each person.", "El gráfico circular muestra partes de un total, no a cada persona."), "d": t("Dates go on a timeline.", "Las fechas van en una línea del tiempo.")},
             "right": t("A circle graph shows how a whole is divided.", "El gráfico circular muestra cómo se reparte un total."), "solution": t("Its job is to show the parts of a whole.", "Su función es mostrar las partes de un total.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("360 is for the angles, in degrees.", "360 es para los ángulos, en grados."), "c": t("The amounts add up to the total; the percents, to 100%.", "Las cantidades suman el total; los porcentajes, 100%."), "d": t("180° is half the circle.", "180° es medio círculo.")}, "solution": t("The percents always add up to 100%.", "Los porcentajes siempre suman 100%.")},
      "B": {"ok": "c", "hints": {"a": t("The percent is not the angle.", "El porcentaje no es el ángulo."), "b": t("Check: 360 × 0.25.", "Revise: 360 × 0.25."), "d": t("180° is 50%.", "180° es el 50%.")}, "solution": t("360° × 0.25 = 90°.", "360° × 0.25 = 90°.")},
      "C": {"ok": "a", "hints": {"b": t("The percent is not the angle.", "El porcentaje no es el ángulo."), "c": t("3.6° is 1%.", "3.6° es el 1%."), "d": t("Check: 360 × 0.10.", "Revise: 360 × 0.10.")}, "solution": t("360° × 0.10 = 36°.", "360° × 0.10 = 36°.")},
      "D": {"ok": "d", "hints": {"a": t("The angle is not the percent.", "El ángulo no es el porcentaje."), "b": t("25% would be 90°.", "El 25% serían 90°."), "c": t("0.2 is the decimal. Multiply by 100.", "0.2 es el decimal. Multiplique por 100.")}, "solution": t("72 ÷ 360 = 0.2 = 20%.", "72 ÷ 360 = 0.2 = 20%.")},
      "E": {"ok": "c", "hints": {"a": t("Check the decimal point: 2,000 × 0.10.", "Revise el punto decimal: 2,000 × 0.10."), "b": t("That is the angle.", "Ese es el ángulo."), "d": t("That is the other 90%.", "Ese es el otro 90%.")}, "solution": t("2,000 × 0.10 = $200.", "2,000 × 0.10 = $200.")},
      "F": {"ok": "a", "hints": {"b": t("38 is the percent, not the hours.", "38 es el porcentaje, no las horas."), "c": t("Check: 24 × 0.38.", "Revise: 24 × 0.38."), "d": t("That is the rest of the day.", "Eso es el resto del día.")}, "solution": t("24 × 0.38 = 9.12 hours.", "24 × 0.38 = 9.12 horas.")},
      "G": {"ok": "d", "hints": {"a": t("The percents add to 100; the angles, to 360°.", "Los porcentajes suman 100; los ángulos, 360°."), "b": t("180° is only half the circle.", "180° es solo medio círculo."), "c": t("270° is three fourths of the circle.", "270° son tres cuartos del círculo.")}, "solution": t("The whole circle is 360°.", "El círculo completo son 360°.")},
      "H": {"ok": "b", "hints": {"a": t("You added. Subtract the two percents.", "Sumó. Reste los dos porcentajes."), "c": t("35% is the food sector itself.", "35% es el sector de comida."), "d": t("Check: 35 − 30.", "Revise: 35 − 30.")}, "solution": t("35 − 30 = 5 percentage points.", "35 − 30 = 5 puntos porcentuales.")}
     }}

    quiz = [
     ("A", t("In a circle graph, all the percents must add up to…", "En un gráfico circular, todos los porcentajes deben sumar…"), [("a", "360"), ("b", "100%"), ("c", t("the real total", "el total real")), ("d", "180")]),
     ("B", t("What central angle does a 25% sector take up?", "¿Qué ángulo central ocupa un sector del 25%?"), [("a", "25°"), ("b", "45°"), ("c", "90°"), ("d", "180°")]),
     ("C", t("What central angle does a 10% sector take up?", "¿Qué ángulo central ocupa un sector del 10%?"), [("a", "36°"), ("b", "10°"), ("c", "3.6°"), ("d", "100°")]),
     ("D", t("A sector has a central angle of 72°. What percent is it?", "Un sector tiene un ángulo central de 72°. ¿Qué porcentaje es?"), [("a", "72%"), ("b", "25%"), ("c", "0.2%"), ("d", "20%")]),
     ("E", t("A budget of $2,000 spends 10% on health. How much is that?", "Un presupuesto de $2,000 dedica el 10% a salud. ¿Cuánto es?"), [("a", "$20"), ("b", "$36"), ("c", "$200"), ("d", "$1,800")]),
     ("F", t("A worker spends 38% of a 24-hour day at work. About how many hours is that?", "Un trabajador dedica al trabajo el 38% de un día de 24 horas. ¿Cuántas horas son, aproximadamente?"), [("a", t("9.12 hours", "9.12 horas")), ("b", t("38 hours", "38 horas")), ("c", t("3.8 hours", "3.8 horas")), ("d", t("14.88 hours", "14.88 horas"))]),
     ("G", t("In the table of a circle graph, the central angles must add up to…", "En la tabla de un gráfico circular, los ángulos centrales deben sumar…"), [("a", "100°"), ("b", "180°"), ("c", "270°"), ("d", "360°")]),
     ("H", t("In the budget graph, food is 35% and rent is 30%. How many percentage points more is food?", "En el gráfico del presupuesto, la comida es el 35% y la renta el 30%. ¿Cuántos puntos porcentuales más es la comida?"), [("a", "65"), ("b", "5"), ("c", "35"), ("d", "10")])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Percents meet the circle: how to read a circle graph, change each percent into a central angle and an amount, and make the graph step by step.", "Los porcentajes se encuentran con el círculo: cómo leer un gráfico circular, pasar cada porcentaje a un ángulo central y a una cantidad, y construir el gráfico paso a paso."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Read</strong> a circle graph: the largest and smallest categories and how they compare.", "<strong>Leer</strong> un gráfico circular: la categoría mayor, la menor y cómo se comparan."),
         t("<strong>Check</strong> that the percents add up to 100%.", "<strong>Comprobar</strong> que los porcentajes suman 100%."),
         t("<strong>Find</strong> the central angle of a sector: 360° × (percent ÷ 100).", "<strong>Calcular</strong> el ángulo central de un sector: 360° × (porcentaje ÷ 100)."),
         t("<strong>Change</strong> between percent, angle, and actual amount.", "<strong>Pasar</strong> de porcentaje a ángulo y a cantidad real, y viceversa."),
         t("<strong>Make</strong> a circle graph from data.", "<strong>Construir</strong> un gráfico circular a partir de datos.")],
        secciones,
        (t("Change five percents into central angles and three angles into percents. Build the full table (percent, angle, amount) for a budget of your choice and check the Total row. Then make that circle graph by hand with a compass and a protractor.",
           "Pase cinco porcentajes a ángulos centrales y tres ángulos a porcentajes. Arme la tabla completa (porcentaje, ángulo y cantidad) de un presupuesto que usted elija y compruebe la fila Total. Después, construya ese gráfico circular a mano, con compás y transportador."),
         t("Look for a circle graph in a newspaper, a website, or a bill (for example, where your tax dollars go). Write down the largest and the smallest category and find the actual amount of one sector.",
           "Busque un gráfico circular en un periódico, una página web o una factura (por ejemplo, en qué se gastan los impuestos). Anote la categoría mayor y la menor, y calcule la cantidad real de un sector.")),
        quiz,
        t("Self-check checklist for circle graphs", "Lista de autoevaluación de gráficos circulares"),
        t("Self-check checklist: skills for circle graphs", "Lista de autoevaluación: destrezas de los gráficos circulares"),
        [(t("Read the graph", "Leer el gráfico"), t("I find the largest and smallest sectors, compare them, and find the actual amount of any part.", "Identifico los sectores mayor y menor, los comparo y calculo la cantidad real de cualquier parte."), t("I read the graph with some help.", "Leo el gráfico con algo de apoyo."), t("I do not know what the sectors stand for.", "No sé qué representan los sectores.")),
         (t("Percent, angle, and amount", "Porcentaje, ángulo y cantidad"), t("I go between the three forms and check them with the Total row.", "Paso de una forma a otra y compruebo con la fila Total."), t("I do one of the conversions with help.", "Hago una de las conversiones con apoyo."), t("I mix up degrees, percents, and amounts.", "Confundo los grados, los porcentajes y las cantidades.")),
         (t("Make a graph", "Construir un gráfico"), t("I make a circle graph from counts, with each angle measured from the last radius.", "Construyo un gráfico circular a partir de conteos, midiendo cada ángulo desde el último radio."), t("I make it with the angles already given.", "Lo construyo con los ángulos ya dados."), t("I cannot change the data into angles.", "No sé pasar los datos a ángulos."))],
        t("<p>A circle graph joins the percents of Topic 5 with the circle of Topic 7: the whole circle is 100% and 360°, and each sector is a part of both. With the rule angle = 360° × (percent ÷ 100) and the Total row as a check, you can read, interpret, and make circle graphs.</p>\n<p>In <strong>Lesson 8.3 · Simple probability</strong>, the last lesson of Level 2, you will use fractions, decimals, and percents once more to measure how likely something is to happen, on a scale from 0 to 1.</p>",
          "<p>El gráfico circular une los porcentajes del Tema 5 con el círculo del Tema 7: el círculo completo es el 100% y los 360°, y cada sector es una parte de los dos. Con la regla ángulo = 360° × (porcentaje ÷ 100) y la fila Total como comprobación, ya se pueden leer, interpretar y construir gráficos circulares.</p>\n<p>En la <strong>Lección 8.3 · Probabilidad simple</strong>, la última del Nivel 2, se usarán otra vez las fracciones, los decimales y los porcentajes para medir qué tan posible es que algo ocurra, en una escala de 0 a 1.</p>"),
        ("8-3", ("", t("Lesson 8.3 · Simple probability", "Lección 8.3 · Probabilidad simple"))),
        [(t("circle graph", "gráfico circular"), t("A circle divided into sectors that show the parts of a whole.", "Un círculo dividido en sectores que muestran las partes de un total.")),
         (t("sector", "sector"), t("A slice of the circle, between two radii.", "Una porción del círculo, entre dos radios.")),
         (t("central angle", "ángulo central"), t("The angle of a sector measured at the center: 360° × (percent ÷ 100).", "El ángulo de un sector medido en el centro: 360° × (porcentaje ÷ 100).")),
         (t("percentage point", "punto porcentual"), t("The difference between two percents: 35% − 30% = 5 points.", "La diferencia entre dos porcentajes: 35% − 30% = 5 puntos."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "presu": [["Food", 35], ["Rent", 30], ["Transportation", 15], ["Health", 10], ["Free time", 10]],
  "temas": [["How a budget is spent", ["Food", "Rent", "Transportation", "Savings", "Other"]], ["How a day is spent", ["Sleep", "Work", "Commute", "Family", "Other"]], ["Language spoken at home", ["Spanish", "English", "Both", "Other"]], ["Favorite sport of a class", ["Soccer", "Baseball", "Basketball", "Other"]]],
  "presuVoz": "Monthly budget: food 35 percent, rent 30, transportation 15, health 10, and free time 10.",
  "faVoz": "Circle graph with one unknown percent.", "faQ": "{t}. What percent goes with “{c}”?", "faB": "All the sectors add up to 100%: 100 − {r} = {f}%.", "faM": "The others add up to {r}%; what is missing to reach 100% is {f}%.",
  "anVoz": "Sector of {p} percent, which takes up {a} degrees.", "elSector": "The sector", "elResto": "The rest",
  "anS1": "The sector takes up {a}° of the 360° of the circle.", "anRecto": " It is a right angle: a fourth of the circle.", "anMedia": " It is half a turn.",
  "agQ1": "What central angle, in degrees, does a {p}% sector take up?", "agS1": "360 × {d} = {a}°.", "agP1": "You divided the wrong way. The angle is 360 × (percent ÷ 100).", "agP2": "That is the angle of the rest of the circle.",
  "agQ2": "A sector has a central angle of {a}°. What percent of the total is it?", "agS2": "{a} ÷ 360 = {d}, and × 100 = {p}%.", "agP3": "To go from angle to percent, divide by 360 (and multiply by 100).",
  "cvCap": "Budget with an income of {T}", "cvCab": ["Category", "Percent", "Central angle", "Amount"], "cvTot": "Total", "cvVoz": "Circle graph of the monthly budget.",
  "cats": ["Rent", "Food", "Savings", "Transportation", "Health"],
  "cv1": "In a budget of {T}, “{c}” is {p}%. How many dollars is that?", "cv1S": "{T2} × {d} = {v}.", "cv1P": "That is the angle. The question asks for dollars: total × percent.",
  "cv2": "In a budget of {T}, the sector “{c}” takes up {a}°. How many dollars is that?", "cv2S": "{a} ÷ 360 = {d} ({p}%); {T2} × {d} = {v}.", "cv2P": "The angle is not a percent: first divide by 360.",
  "cv3": "Out of a budget of {T}, {v} is spent on “{c}”. What angle does that sector take up in the graph, in degrees?", "cv3S": "{v2} ÷ {T2} = {d}; 360 × {d} = {a}°.", "cv3P": "That is the percent. You still need to change it to degrees: × 3.6.",
  "coCat": "Category", "coCnt": "Count", "coCap": "From counts to a circle graph", "coCab": ["Category", "Count", "Percent", "Central angle"], "coVoz": "Circle graph built from the counts.", "coNada": "Type at least one count greater than 0.",
  "coNom": ["Bus", "Car", "Walking", "Bicycle"],
  "pcC": [["In a survey of {T} people, {c} prefer soccer."], ["Of {T} students, {c} come by bus."], ["A store sold {T} shirts, {c} of them blue."]],
  "pcQ": " What percent of the graph does that sector take up?", "pcS": "{c} ÷ {T} = {d}, and × 100 = {p}%. Its angle would be {a}°.", "pcP1": "Multiply by 100 to change it to a percent.", "pcP2": "Divide the part by the total, not the other way around.",
  "leVoz": "Circle graph: {x}.", "porc": " percent",
  "le1": "{t}. Which category is the largest?", "le1B": "{c} has the largest sector.", "le1M": "The largest is {c}, with {p}%.",
  "le2": "{t}. How many percentage points apart are “{a}” and “{b}”?", "le2o": " percentage points", "le2B": "{p} − {q} = {d} (the difference).", "le2M": "Subtract the two percents: the difference between {p} and {q} is {d}.",
  "le3": "{t} (total: {T}). How much is “{c}”?", "le3B": "{T} × {d} = {v}.", "le3M": "Multiply the total by the percent: {T} × {d} = {v}.",
  "le4": "{t}. What percent do “{a}” and “{b}” add up to together?", "le4B": "{p} + {q} = {s}%.", "le4M": "Add the two sectors: {p} + {q} = {s}%."
 },
 "es": {
  "presu": [["Comida", 35], ["Renta", 30], ["Transporte", 15], ["Salud", 10], ["Ocio", 10]],
  "temas": [["Cómo se reparte un presupuesto", ["Comida", "Renta", "Transporte", "Ahorro", "Otros"]], ["Cómo se distribuye un día", ["Dormir", "Trabajo", "Traslados", "Familia", "Otros"]], ["Idioma que se habla en casa", ["Español", "Inglés", "Los dos", "Otro"]], ["Deporte favorito de un salón", ["Fútbol", "Béisbol", "Básquetbol", "Otro"]]],
  "presuVoz": "Presupuesto mensual: comida 35 por ciento, renta 30, transporte 15, salud 10 y ocio 10.",
  "faVoz": "Gráfico circular con un porcentaje desconocido.", "faQ": "{t}. ¿Qué porcentaje corresponde a «{c}»?", "faB": "Todos los sectores suman 100%: 100 − {r} = {f}%.", "faM": "Los demás suman {r}%; lo que falta para llegar a 100% es {f}%.",
  "anVoz": "Sector del {p} por ciento, que ocupa {a} grados.", "elSector": "El sector", "elResto": "El resto",
  "anS1": "El sector ocupa {a}° de los 360° del círculo.", "anRecto": " Es un ángulo recto: un cuarto del círculo.", "anMedia": " Es media vuelta.",
  "agQ1": "Un sector del {p}%, ¿qué ángulo central ocupa, en grados?", "agS1": "360 × {d} = {a}°.", "agP1": "Se dividió al revés. El ángulo es 360 × (porcentaje ÷ 100).", "agP2": "Ese es el ángulo del resto del círculo.",
  "agQ2": "Un sector ocupa un ángulo central de {a}°. ¿Qué porcentaje del total representa?", "agS2": "{a} ÷ 360 = {d}, y × 100 = {p}%.", "agP3": "Para pasar del ángulo al porcentaje se divide entre 360 (y se multiplica por 100).",
  "cvCap": "Presupuesto con un ingreso de {T}", "cvCab": ["Categoría", "Porcentaje", "Ángulo central", "Cantidad"], "cvTot": "Total", "cvVoz": "Gráfico circular del presupuesto mensual.",
  "cats": ["Renta", "Comida", "Ahorro", "Transporte", "Salud"],
  "cv1": "En un presupuesto de {T}, «{c}» ocupa el {p}%. ¿Cuántos dólares son?", "cv1S": "{T2} × {d} = {v}.", "cv1P": "Ese es el ángulo. Se pide la cantidad en dólares: total × porcentaje.",
  "cv2": "En un presupuesto de {T}, el sector «{c}» ocupa {a}°. ¿Cuántos dólares son?", "cv2S": "{a} ÷ 360 = {d} ({p}%); {T2} × {d} = {v}.", "cv2P": "El ángulo no es un porcentaje: primero se divide entre 360.",
  "cv3": "De un presupuesto de {T}, se gastan {v} en «{c}». ¿Qué ángulo ocupa ese sector en el gráfico, en grados?", "cv3S": "{v2} ÷ {T2} = {d}; 360 × {d} = {a}°.", "cv3P": "Ese es el porcentaje. Falta pasarlo a grados: × 3.6.",
  "coCat": "Categoría", "coCnt": "Conteo", "coCap": "De los conteos al gráfico circular", "coCab": ["Categoría", "Conteo", "Porcentaje", "Ángulo central"], "coVoz": "Gráfico circular construido con los conteos.", "coNada": "Escriba por lo menos un conteo mayor que 0.",
  "coNom": ["Autobús", "Carro", "A pie", "Bicicleta"],
  "pcC": [["En una encuesta a {T} personas, {c} prefieren el fútbol."], ["De {T} estudiantes, {c} llegan en autobús."], ["Una tienda vendió {T} camisas, {c} de ellas azules."]],
  "pcQ": " ¿Qué porcentaje del gráfico ocupa ese sector?", "pcS": "{c} ÷ {T} = {d}, y × 100 = {p}%. Su ángulo sería {a}°.", "pcP1": "Falta multiplicar por 100 para pasar a porcentaje.", "pcP2": "Se divide la parte entre el total, no al revés.",
  "leVoz": "Gráfico circular: {x}.", "porc": " por ciento",
  "le1": "{t}. ¿Qué categoría es la mayor?", "le1B": "{c} tiene el sector más grande.", "le1M": "La mayor es {c}, con {p}%.",
  "le2": "{t}. ¿Cuántos puntos porcentuales de diferencia hay entre «{a}» y «{b}»?", "le2o": " puntos porcentuales", "le2B": "{p} − {q} = {d} (la diferencia).", "le2M": "Se restan los dos porcentajes: la diferencia entre {p} y {q} es {d}.",
  "le3": "{t} (total: {T}). ¿A cuánto equivale «{c}»?", "le3B": "{T} × {d} = {v}.", "le3M": "Se multiplica el total por el porcentaje: {T} × {d} = {v}.",
  "le4": "{t}. ¿Qué porcentaje suman «{a}» y «{b}» juntas?", "le4B": "{p} + {q} = {s}%.", "le4M": "Se suman los dos sectores: {p} + {q} = {s}%."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function r2(x){ return Math.round(x * 100) / 100; }
function sinPct(t){ return String(t).replace(/[%°]/g, ""); }
var PRESU = TXT.presu;

/* ============ MODULE 1 · what a circle graph is ============ */
function genFalta(){
  var tm = elige(TXT.temas), n = tm[1].length, p = repartoAzar(n), i = aleatorio(0, n - 1), f = p[i];
  var it = items(tm[1], p); it[i] = { nombre: tm[1][i], pct: f, etq: "?", color: "#757575" };
  var o = [f, f + 5, 100 - f, f - 5].filter(function(x, k, a){ return x > 0 && x < 100 && a.indexOf(x) === k; }).map(function(x){ return { html: x + "%", clave: "p" + x }; });
  return { enun: F(TXT.faQ, { t: tm[0], c: tm[1][i] }) + pieSVG(it, TXT.faVoz), opciones: baraja(o), correcta: "p" + f, bien: F(TXT.faB, { r: 100 - f, f: f }), mal: F(TXT.faM, { r: 100 - f, f: f }) };
}

/* ============ MODULE 2 · the central angle ============ */
function pintaAN(){
  var p = +$("an-p").value, a = 3.6 * p; $("an-pv").textContent = p + "%";
  $("an-svg").innerHTML = pieSVG([{ nombre: TXT.elSector, pct: p }, { nombre: TXT.elResto, pct: 100 - p, color: "#bdbdbd" }], F(TXT.anVoz, { p: p, a: nd(r2(a)) }), { sinPct: true });
  $("an-salida").innerHTML = '<div class="linea veredicto">360° × ' + nd(p / 100) + ' = ' + nd(r2(a)) + '°</div><div class="linea">' + F(TXT.anS1, { a: nd(r2(a)) }) + (p === 25 ? TXT.anRecto : (p === 50 ? TXT.anMedia : "")) + '</div>';
}
function genAng(){
  if (Math.random() < 0.65){
    var p = elige([5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 75, 12.5, 2.5]), a = 3.6 * p;
    var ev = numD(r2(a), [{ v: r2(p * 100 / 360), msg: TXT.agP1 }, { v: r2(360 - a), msg: TXT.agP2 }].filter(function(x){ return Math.abs(x.v - a) > 0.02; }), null, 0.011);
    return { enun: F(TXT.agQ1, { p: nd(p) }), correcta: nd(r2(a)), solucion: F(TXT.agS1, { d: nd(p / 100), a: nd(r2(a)) }), evalua: function(s){ return ev(sinPct(s)); } };
  }
  var ang = elige([36, 72, 90, 108, 126, 144, 180, 54, 18]), pc = ang / 3.6, ev2 = numD(pc, [{ v: r2(ang * 3.6), msg: TXT.agP3 }], null, 0.011);
  return { enun: F(TXT.agQ2, { a: ang }), correcta: nd(pc) + "%", solucion: F(TXT.agS2, { a: ang, d: nd(ang / 360), p: nd(pc) }), evalua: function(s){ return ev2(sinPct(s)); } };
}

/* ============ MODULE 3 · percent, angle, and amount ============ */
function pintaCV(){
  var Tt = +$("cv-t").value; $("cv-tv").textContent = dinero(Tt);
  var h = '<table class="comparar"><caption>' + F(TXT.cvCap, { T: dinero(Tt) }) + '</caption><thead><tr>' + TXT.cvCab.map(function(c){ return '<th scope="col">' + c + '</th>'; }).join("") + '</tr></thead><tbody>';
  PRESU.forEach(function(c){ h += '<tr><td>' + c[0] + '</td><td>' + c[1] + '%</td><td>' + nd(3.6 * c[1]) + '°</td><td>' + dinero(Tt * c[1] / 100) + '</td></tr>'; });
  h += '<tr><td><strong>' + TXT.cvTot + '</strong></td><td><strong>100%</strong></td><td><strong>360°</strong></td><td><strong>' + dinero(Tt) + '</strong></td></tr></tbody></table>';
  $("cv-tabla").innerHTML = pieSVG(items(PRESU.map(function(c){ return c[0]; }), PRESU.map(function(c){ return c[1]; })), TXT.cvVoz) + h;
}
function genConv(){
  var Tt = 100 * aleatorio(10, 60), p = elige([5, 10, 15, 20, 25, 30, 35, 40]), v = Tt * p / 100, a = 3.6 * p, tp = aleatorio(1, 3), o = { T: dinero(Tt), T2: nd(Tt), c: elige(TXT.cats), p: p, d: nd(p / 100), a: nd(a), v: dinero2(v).replace(".00", ""), v2: nd(v) };
  if (tp === 1) return { enun: F(TXT.cv1, o), correcta: dinero(v), solucion: F(TXT.cv1S, o), evalua: numD(v, [{ v: a, msg: TXT.cv1P }].filter(function(x){ return Math.abs(x.v - v) > 0.01; })) };
  if (tp === 2) return { enun: F(TXT.cv2, o), correcta: dinero(v), solucion: F(TXT.cv2S, o), evalua: numD(v, [{ v: Tt * a / 100, msg: TXT.cv2P }]) };
  var ev = numD(a, [{ v: p, msg: TXT.cv3P }], null, 0.011);
  return { enun: F(TXT.cv3, o), correcta: nd(a), solucion: F(TXT.cv3S, o), evalua: function(s){ return ev(sinPct(s)); } };
}

/* ============ MODULE 4 · making a circle graph ============ */
function pintaCO(){
  var c = [0, 1, 2, 3].map(function(i){ var v = leeD($("co-" + i).value); $("co-" + i).classList.toggle("error", v === null || v < 0); return v === null || v < 0 ? 0 : Math.round(v); });
  var tot = sumaDe(c);
  if (!tot){ $("co-salida").innerHTML = '<p>' + TXT.coNada + '</p>'; return; }
  var pc = c.map(function(x){ return x / tot * 100; });
  var h = '<table class="comparar"><caption>' + TXT.coCap + '</caption><thead><tr>' + TXT.coCab.map(function(x){ return '<th scope="col">' + x + '</th>'; }).join("") + '</tr></thead><tbody>';
  c.forEach(function(x, i){ h += '<tr><td>' + TXT.coNom[i] + '</td><td>' + x + '</td><td>' + x + ' ÷ ' + tot + ' ≈ ' + nd(r2(pc[i])) + '%</td><td>' + nd(r2(pc[i] * 3.6)) + '°</td></tr>'; });
  h += '<tr><td><strong>' + TXT.cvTot + '</strong></td><td><strong>' + tot + '</strong></td><td><strong>100%</strong></td><td><strong>360°</strong></td></tr></tbody></table>';
  $("co-salida").innerHTML = pieSVG(c.map(function(x, i){ return { nombre: TXT.coNom[i], pct: r2(pc[i]), etq: Math.round(pc[i]) + "%" }; }), TXT.coVoz) + '<div class="tabla-scroll">' + h + '</div>';
}
function genPct(){
  var tot = elige([20, 25, 40, 50, 80, 200]), p = elige([5, 10, 15, 20, 25, 30, 40, 45, 60]), c = tot * p / 100;
  if (c !== Math.round(c)) return genPct();
  var ev = numD(p, [{ v: c / tot, msg: TXT.pcP1 }, { v: r2(tot / c * 100), msg: TXT.pcP2 }], null, 0.011);
  return { enun: F(elige(TXT.pcC)[0], { T: tot, c: c }) + TXT.pcQ, correcta: p + "%", solucion: F(TXT.pcS, { c: c, T: tot, d: nd(c / tot), p: p, a: nd(3.6 * p) }), evalua: function(s){ return ev(sinPct(s)); } };
}

/* ============ MODULE 5 · reading real graphs ============ */
function genLeer(){
  var tm = elige(TXT.temas), n = tm[1].length, p, tp = aleatorio(1, 4);
  do { p = repartoAzar(n); } while (p.filter(function(x){ return x === Math.max.apply(null, p); }).length > 1 || p[0] === p[1]);
  var it = items(tm[1], p), sv = pieSVG(it, F(TXT.leVoz, { x: it.map(function(x){ return x.nombre + " " + x.pct + TXT.porc; }).join(", ") }));
  if (tp === 1){ var mx = tm[1][p.indexOf(Math.max.apply(null, p))];
    return { enun: F(TXT.le1, { t: tm[0] }) + sv, opciones: tm[1].map(function(x){ return { html: x, clave: x }; }), correcta: mx, enOrden: true, bien: F(TXT.le1B, { c: mx }), mal: F(TXT.le1M, { c: mx, p: Math.max.apply(null, p) }) }; }
  if (tp === 2){ var d = Math.abs(p[0] - p[1]), o = [d, p[0] + p[1], d + 5, Math.max(p[0], p[1])].filter(function(x, k, a){ return a.indexOf(x) === k; });
    return { enun: F(TXT.le2, { t: tm[0], a: tm[1][0], b: tm[1][1] }) + sv, opciones: baraja(o).map(function(x){ return { html: x + TXT.le2o, clave: "d" + x }; }), correcta: "d" + d, bien: F(TXT.le2B, { p: Math.max(p[0], p[1]), q: Math.min(p[0], p[1]), d: d }), mal: F(TXT.le2M, { p: p[0], q: p[1], d: d }) }; }
  if (tp === 3){ var Tt = elige([200, 400, 500, 1000, 2000]), k = aleatorio(0, n - 1), v = Tt * p[k] / 100, o2 = [v, p[k], Tt - v, v * 2].filter(function(x, q, a){ return a.indexOf(x) === q; });
    var oo = { t: tm[0], T: nd(Tt), c: tm[1][k], d: nd(p[k] / 100), v: nd(v) };
    return { enun: F(TXT.le3, oo) + sv, opciones: baraja(o2).map(function(x){ return { html: nd(x), clave: "v" + x }; }), correcta: "v" + v, bien: F(TXT.le3B, oo), mal: F(TXT.le3M, oo) }; }
  var s = p[0] + p[1], o3 = [s, 100 - s, Math.abs(p[0] - p[1]), s + 10].filter(function(x, q, a){ return x > 0 && a.indexOf(x) === q; });
  var o4 = { t: tm[0], a: tm[1][0], b: tm[1][1], p: p[0], q: p[1], s: s };
  return { enun: F(TXT.le4, o4) + sv, opciones: baraja(o3).map(function(x){ return { html: x + "%", clave: "s" + x }; }), correcta: "s" + s, bien: F(TXT.le4B, o4), mal: F(TXT.le4M, o4) };
}

/* ============ Start ============ */
$("qe-svg").innerHTML = pieSVG(items(PRESU.map(function(c){ return c[0]; }), PRESU.map(function(c){ return c[1]; })), TXT.presuVoz);
creaPracticaOM("p1", genFalta);
$("an-p").addEventListener("input", pintaAN); pintaAN();
creaPracticaLibre("p2", genAng);
$("cv-t").addEventListener("input", pintaCV); pintaCV();
creaPracticaLibre("p3", genConv);
[0, 1, 2, 3].forEach(function(i){ $("co-" + i).addEventListener("input", pintaCO); }); pintaCO();
creaPracticaLibre("p4", genPct);
creaPracticaOM("p5", genLeer);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    nombres = TX[B.L]["coNom"]
    conteos = [12, 6, 4, 2]
    campos = "".join(f'<div class="campo"><label for="co-{i}">{nombres[i]}</label><input type="text" inputmode="numeric" autocomplete="off" class="corto" id="co-{i}" value="{conteos[i]}"></div>' for i in range(4))
    mods = [
     (t("what-it-is", "que-es"), t("What a circle graph is", "Qué es un gráfico circular"),
      f'''      <p>{t("A circle graph is a circle divided into sectors. Each sector is the percent of one category, and <strong>all the percents add up to 100%</strong>, because the whole circle is the total.", "Un gráfico circular es un círculo dividido en sectores. Cada sector es el porcentaje de una categoría, y <strong>todos los porcentajes suman 100%</strong>, porque el círculo entero es el total.")}</p>
      <div id="qe-svg"></div>
      <div class="caja-tip">{t("It is ideal to show how a whole is divided (a budget, a day, a population). To show change over time, a line graph is better.", "Es ideal para mostrar cómo se reparte un total (un presupuesto, un día, una población). Para mostrar cambios en el tiempo conviene un gráfico de líneas.")}</div>
{B.om("p1", t("Practice: the missing percent", "Practique: el porcentaje que falta"))}'''),
     (t("angle", "angulo"), t("The central angle", "El ángulo central"),
      f'''      <div class="formula">{t("angle = 360° × (percent ÷ 100)", "ángulo = 360° × (porcentaje ÷ 100)")}</div>
      <p>{t("Shortcuts: 50% = 180° · 25% = 90° · 10% = 36° · 1% = 3.6°.", "Atajos: 50% = 180° · 25% = 90° · 10% = 36° · 1% = 3.6°.")}</p>
      <h3>{t("Move the sector", "Mueva el sector")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="an-p">{t("Percent", "Porcentaje")}: <span id="an-pv"></span></label><input type="range" id="an-p" min="1" max="100" value="25"></div></div>
        <div id="an-svg"></div>
        <div class="salida" id="an-salida" aria-live="polite"></div>
      </div>
{libre_x("p2", t("Practice: percent and angle", "Practique: porcentaje y ángulo"), t("Answer", "Resultado"), t("Type only the number: degrees (72) or percent (20).", "Escriba solo el número: grados (72) o porcentaje (20)."))}'''),
     (t("conversions", "conversiones"), t("Percent, angle, and amount", "Porcentaje, ángulo y cantidad"),
      f'''      <p>{t("amount = total × (percent ÷ 100) · percent = (angle ÷ 360°) × 100. The <strong>Total</strong> row checks everything: 100%, 360°, and the real total.", "cantidad = total × (porcentaje ÷ 100) · porcentaje = (ángulo ÷ 360°) × 100. La fila <strong>Total</strong> lo comprueba todo: 100%, 360° y el total real.")}</p>
      <h3>{t("The monthly budget", "El presupuesto mensual")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="cv-t">{t("Monthly income ($)", "Ingreso mensual ($)")}: <span id="cv-tv"></span></label><input type="range" id="cv-t" min="1000" max="6000" step="100" value="2000"></div></div>
        <div class="tabla-scroll" id="cv-tabla"></div>
      </div>
{libre_x("p3", t("Practice: percent, angle, and amount", "Practique: porcentaje, ángulo y cantidad"), t("Answer", "Resultado"), t("Type only the number: dollars or degrees.", "Escriba solo el número: dólares o grados."))}'''),
     (t("build", "construir"), t("Making a circle graph", "Construir un gráfico circular"),
      f'''      <p>{t("From counts: divide each count by the total to get the percent, multiply by 3.6 to get the angle, and draw each sector from the last radius. A class of 24 students says how they get to school:", "A partir de conteos: se divide cada conteo entre el total para obtener el porcentaje, se multiplica por 3.6 para obtener el ángulo y se dibuja cada sector desde el último radio. Un salón de 24 estudiantes dice cómo llega a la escuela:")}</p>
      <div class="panel">
        <div class="campos">{campos}</div>
        <div id="co-salida" aria-live="polite"></div>
      </div>
{libre_x("p4", t("Practice: from counts to percents", "Practique: de conteos a porcentajes"), t("Percent", "Porcentaje"), t("Type only the number (20 for 20%).", "Escriba solo el número (20 para 20%)."))}'''),
     (t("read", "leer"), t("Reading real graphs", "Leer gráficos reales"),
      f'''      <p>{t("Find the largest sector, compare two categories (the difference between two percents is measured in percentage points), and find the real amount of a part: total × percent.", "Identifique el sector mayor, compare dos categorías (la diferencia entre dos porcentajes se mide en puntos porcentuales) y calcule la cantidad real de una parte: total × porcentaje.")}</p>
{B.om("p5", t("Practice: read the graph", "Practique: lea el gráfico"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/stats.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Gráficos circulares: leer, interpretar y construir")
