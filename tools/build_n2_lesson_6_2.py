"""Level 2 · Lesson 6.2 · Depreciation and other money applications — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "6-2"
TEMA = ("Money math and unit conversions", "Matemáticas financieras y conversiones de medidas")
TIT = ("Depreciation and other money applications", "Depreciación y otras aplicaciones financieras")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def barras_pc():
    """Valor contable de la computadora: 1,800 → 200 en 4 años."""
    vals = [1800, 1400, 1000, 600, 200]
    s, x0, x1, yb = "", 160, 620, 200
    w = (x1 - x0) / 5 * 0.62
    Y = lambda v: yb - v * 170 / 1800
    for k, v in enumerate(vals):
        x = x0 + (x1 - x0) * k / 5 + (x1 - x0) / 5 * 0.19
        s += f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{w:.1f}" height="{yb - Y(v):.1f}" fill="#00897b"/>'
        s += f'<text x="{x + w / 2:.1f}" y="{Y(v) - 6:.1f}" text-anchor="middle" font-size="13" font-weight="700" fill="#004d40">${v:,}</text>'
        s += f'<text x="{x + w / 2:.1f}" y="{yb + 16}" text-anchor="middle" font-size="13" fill="#424242">{k}</text>'
    s += f'<line x1="{x0 - 2}" y1="{Y(200):.1f}" x2="{x1}" y2="{Y(200):.1f}" stroke="#c62828" stroke-width="2" stroke-dasharray="6 4"/>'
    s += f'<text x="{x0 - 6}" y="{Y(200) + 4:.1f}" text-anchor="end" font-size="12" fill="#c62828">{t("salvage value $200", "valor residual $200")}</text>'
    s += f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#424242" stroke-width="2"/>'
    s += f'<text x="390" y="236" text-anchor="middle" font-size="13" font-weight="700" fill="#424242">{t("Year", "Año")}</text>'
    return svg("0 0 640 240", t("Bars for the book value of the computer: $1,800 in year 0, $1,400, $1,000, $600, and $200 in year 4. Each bar is $400 lower than the one before, and the last one reaches the dashed line of the $200 salvage value.",
                               "Barras del valor contable de la computadora: $1,800 en el año 0, $1,400, $1,000, $600 y $200 en el año 4. Cada barra es $400 más baja que la anterior, y la última llega a la línea punteada del valor residual de $200."), s, 640)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 6.1 money in savings grew by the same amount every year because of simple interest. Many things you buy go the opposite way: a car, a computer, or a work tool lose value with use and with time. When that loss is the same every year, it is called <strong>straight-line depreciation</strong>.", "En la Lección 6.1, el dinero ahorrado crecía en una cantidad fija cada año gracias al interés simple. Muchas cosas que se compran siguen el camino contrario: un carro, una computadora o una herramienta de trabajo pierden valor con el uso y el paso del tiempo. Cuando esa pérdida es la misma cada año, se llama <strong>depreciación lineal</strong>.")}</p>
{tabla(t("Two mirror images", "Dos imágenes en espejo"), t("Simple interest and straight-line depreciation", "Interés simple y depreciación lineal"),
       ["", t("Simple interest ↑", "Interés simple ↑"), t("Straight-line depreciation ↓", "Depreciación lineal ↓")],
       [[t("Every year", "Cada año"), t("the money <strong>gains</strong> the same amount", "el dinero <strong>gana</strong> la misma cantidad"), t("the item <strong>loses</strong> the same amount", "el bien <strong>pierde</strong> la misma cantidad")]])}
{tabla(t("Depreciation words", "Términos de la depreciación"), t("The vocabulary of depreciation", "El vocabulario de la depreciación"),
       [t("Term", "Término"), t("What it is", "Qué es")],
       [[t("asset", "activo o bien"), t("something of value you buy to use for several years (a car, a machine, a computer)", "algo de valor que se compra para usarlo varios años (un carro, una máquina, una computadora)")],
        [t("starting value (V₀)", "valor inicial (V₀)"), t("what the item cost when it was bought", "lo que costó el bien al comprarlo")],
        [t("useful life (n)", "vida útil (n)"), t("the number of years you expect to use it", "los años que se espera usar el bien")],
        [t("salvage value (Vr)", "valor residual (Vr)"), t("what it will still be worth at the end of its useful life, for example, what someone would pay for it used or for its parts", "lo que todavía valdrá al final de su vida útil; por ejemplo, lo que pagaría alguien por él como usado o por sus piezas")],
        [t("yearly depreciation (D)", "depreciación anual (D)"), t("the value it loses each year", "el valor que pierde cada año")],
        [t("book value", "valor contable"), t("what the item is worth, according to the calculations, at the end of a given year", "lo que vale el bien, según los cálculos, al final de un año determinado")]])}
{tabla(t("The same words in both languages", "Las mismas palabras en los dos idiomas"), t("Depreciation words in English and in Spanish", "Términos de la depreciación en inglés y en español"),
       [t("English", "Inglés"), t("Spanish", "Español")],
       [["straight-line depreciation", "depreciación lineal"], ["asset", "activo o bien"], ["salvage value (residual value)", "valor residual"], ["useful life", "vida útil"], ["book value", "valor contable"], ["accumulated depreciation", "depreciación acumulada"]])}
{enlace(n, t("vocabulary", "vocabulario"), t("depreciation vocabulary", "vocabulario de la depreciación"), t("Review starting value, salvage value, useful life, and book value.", "Repase el valor inicial, el valor residual, la vida útil y el valor contable."))}'''

    s2 = f'''<p>{t("Before you use a formula, it helps to see the pattern in a table.", "Antes de usar una fórmula, conviene ver el patrón con una tabla.")}</p>
{ej(t("Example: the office computer", "Ejemplo: la computadora de la oficina"), t("An office buys a computer for <strong>$1,800</strong>. It will be used for <strong>4 years</strong>, and at the end it can be sold for <strong>$200</strong>. What is it worth at the end of each year?", "Una oficina compra una computadora por <strong>$1,800</strong>. Se espera usarla <strong>4 años</strong>, y al final se podrá vender en <strong>$200</strong>. ¿Cuánto vale al final de cada año?"),
  [("1", t("Total loss.", "Pérdida total."), "1,800 − 200 = 1,600."),
   ("2", t("Split it into equal parts.", "Repártala en partes iguales."), t("1,600 ÷ 4 = 400 per year.", "1,600 ÷ 4 = 400 por año.")),
   ("3", t("Subtract year by year.", "Reste año tras año."), t("Each year, take $400 away from the year before.", "Cada año se restan $400 al valor del año anterior."))])}
{tabla(t("The computer, year by year", "La computadora, año por año"), t("Book value of the computer year by year", "Valor contable de la computadora año por año"),
       [t("Year", "Año"), t("Depreciation that year ($)", "Depreciación del año ($)"), t("Accumulated depreciation ($)", "Depreciación acumulada ($)"), t("Book value ($)", "Valor contable ($)")],
       [["0", "—", "0", "1,800"], ["1", "400", "400", "1,400"], ["2", "400", "800", "1,000"], ["3", "400", "1,200", "600"], ["4", "400", "1,600", "200"]])}
<div style="text-align:center">{barras_pc()}</div>
<p>{t("Each bar is $400 lower than the one before. The value never drops below the salvage value.", "Cada barra es $400 más baja que la anterior. El valor nunca baja del valor residual.")}</p>
{practica("p1", t("Practice 1 — Yearly depreciation", "Práctica 1 — Depreciación anual"), t("A store buys a commercial refrigerator for $2,600. Its useful life is 5 years and its salvage value is $600. How much does it lose each year?", "Una tienda compra un refrigerador comercial por $2,600. Su vida útil es de 5 años y su valor residual, $600. ¿Cuánto pierde cada año?"),
          [("a", "$520"), ("b", "$400"), ("c", "$2,000"), ("d", "$600")])}
{practica("p2", t("Practice 2 — Book value", "Práctica 2 — Valor contable"), t("With the same refrigerator, what is its book value at the end of year 3?", "Con el mismo refrigerador, ¿cuál es su valor contable al final del año 3?"),
          [("a", "$1,200"), ("b", "$1,040"), ("c", "$1,000"), ("d", "$1,400")])}
{enlace(n, t("table", "tabla"), t("first the table, then the formula", "primero la tabla, después la fórmula"), t("Fill in the book-value table year by year.", "Complete la tabla del valor contable año por año."))}'''

    s3 = f'''<p>{t("The steps of the computer example add up to two formulas.", "Los pasos del ejemplo de la computadora se resumen en dos fórmulas.")}</p>
{big("D = (V₀ − Vr) ÷ n")}
<p style="text-align:center">{t("D = yearly depreciation · V₀ = starting value · Vr = salvage value · n = useful life in years", "D = depreciación anual · V₀ = valor inicial · Vr = valor residual · n = vida útil en años")}</p>
{big(t("Book value in year t = V₀ − D × t", "Valor contable en el año t = V₀ − D × t"))}
<p style="text-align:center">{t("D × t is the accumulated depreciation up to that year.", "D × t es la depreciación acumulada hasta ese año.")}</p>
{caja("tip", t("The yearly rate", "La tasa anual"), t("<p>If an item lasts 4 years, each year it loses 1 of 4 equal parts of the value being depreciated: 1 ÷ 4 = 0.25 = 25% a year. In general, the yearly rate of straight-line depreciation is <strong>1 ÷ n</strong>. For the computer: 25% of $1,600 = $400, the same result.</p>", "<p>Si un bien dura 4 años, cada año pierde 1 de 4 partes iguales del valor que se va a depreciar: 1 ÷ 4 = 0.25 = 25% por año. En general, la tasa anual de depreciación lineal es <strong>1 ÷ n</strong>. En la computadora: 25% de $1,600 = $400, el mismo resultado.</p>"))}
{ej(t("Example: work equipment", "Ejemplo: equipo de trabajo"), t("A sewing shop buys an industrial machine for $3,000. Its useful life is 5 years and its salvage value is $500. Find the yearly depreciation, the yearly rate, and the book value at the end of year 3.", "Un taller de costura compra una máquina industrial por $3,000. Su vida útil es de 5 años y su valor residual, $500. Calcule la depreciación anual, la tasa anual y el valor contable al final del año 3."),
  [("1", t("Yearly depreciation.", "Depreciación anual."), t("D = (3,000 − 500) ÷ 5 = 2,500 ÷ 5 = 500 per year.", "D = (3,000 − 500) ÷ 5 = 2,500 ÷ 5 = 500 por año.")),
   ("2", t("Yearly rate.", "Tasa anual."), t("1 ÷ 5 = 0.20 = 20% a year.", "1 ÷ 5 = 0.20 = 20% por año.")),
   ("3", t("Book value in year 3.", "Valor contable en el año 3."), "3,000 − 500 × 3 = 3,000 − 1,500 = 1,500."),
   ("✓", t("Answer.", "Respuesta."), t("It loses <strong>$500 a year</strong> (20%), and at the end of year 3 it is worth <strong>$1,500</strong>.", "Pierde <strong>$500 por año</strong> (20%), y al final del año 3 vale <strong>$1,500</strong>."))])}
{ej(t("Example: in what year does it reach a value?", "Ejemplo: ¿en qué año llega a cierto valor?"), t("With the same machine: at the end of what year will its book value be $1,000?", "Con la misma máquina: ¿al final de qué año su valor contable será de $1,000?"),
  [("1", t("Value it must lose.", "Valor que tiene que perder."), "3,000 − 1,000 = 2,000."),
   ("2", t("Years needed.", "Años necesarios."), "2,000 ÷ 500 = 4."),
   ("✓", t("Answer.", "Respuesta."), t("At the end of <strong>year 4</strong>.", "Al final del <strong>año 4</strong>."))])}
{ej(t("Example: when the problem gives a percent of the cost", "Ejemplo: cuando el problema da un porcentaje del costo"), t("“A $30,000 delivery van depreciates 10% of its original cost each year.” What is it worth after 4 years?", "«Una camioneta de reparto de $30,000 se deprecia un 10% anual de su costo original». ¿Cuánto vale después de 4 años?"),
  [("1", t("Yearly depreciation.", "Depreciación anual."), "30,000 × 0.10 = 3,000."),
   ("2", t("Book value in year 4.", "Valor contable en el año 4."), "30,000 − 3,000 × 4 = 30,000 − 12,000 = 18,000."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$18,000</strong>. It is still straight-line depreciation: the loss is the same every year; only the way the data is given changes.", "<strong>$18,000</strong>. Sigue siendo depreciación lineal: la pérdida es la misma cada año; solo cambia la forma de dar el dato."))])}
{caja("ojo", t("Common mistake", "Error frecuente"), t("<p>Dividing the starting value by the useful life without first subtracting the salvage value. For the machine, 3,000 ÷ 5 = 600 is wrong: with that number the machine would end up worth $0, not the $500 the problem says.</p>", "<p>Dividir el valor inicial entre la vida útil sin restar antes el valor residual. En la máquina, 3,000 ÷ 5 = 600 es incorrecto: con esa cifra, la máquina terminaría valiendo $0 y no los $500 del enunciado.</p>"))}
{calc(t("Book value on the calculator", "El valor contable en la calculadora"), t(f"<p>For the machine in year 3: {T('(')} {T('3000')} {T('−')} {T('500')} {T(')')} {T('÷')} {T('5')} {T('enter')} gives 500. Then {T('3000')} {T('−')} {T('500')} {T('×')} {T('3')} {T('enter')} gives 1,500. The calculator multiplies before it subtracts.</p>", f"<p>Para la máquina en el año 3: {T('(')} {T('3000')} {T('−')} {T('500')} {T(')')} {T('÷')} {T('5')} {T('enter')} da 500. Después, {T('3000')} {T('−')} {T('500')} {T('×')} {T('3')} {T('enter')} da 1,500. La calculadora multiplica antes de restar.</p>"))}
{practica("p3", t("Practice 3 — A printer", "Práctica 3 — Una impresora"), t("A $900 printer has a salvage value of $100 and a useful life of 4 years. What is its yearly depreciation?", "Una impresora de $900 tiene un valor residual de $100 y una vida útil de 4 años. ¿Cuál es la depreciación anual?"),
          [("a", "$200"), ("b", "$225"), ("c", "$250"), ("d", "$800")])}
{practica("p4", t("Practice 4 — A drill", "Práctica 4 — Un taladro"), t("A $450 professional drill has a salvage value of $50 and a useful life of 5 years. What is its book value at the end of year 3?", "Un taladro profesional de $450 tiene un valor residual de $50 y una vida útil de 5 años. ¿Cuál es su valor contable al final del año 3?"),
          [("a", "$290"), ("b", "$240"), ("c", "$210"), ("d", "$80")])}
{practica("p5", t("Practice 5 — The yearly rate", "Práctica 5 — La tasa anual"), t("An item has a useful life of 8 years. What is its yearly rate of straight-line depreciation?", "Un bien tiene una vida útil de 8 años. ¿Cuál es su tasa anual de depreciación lineal?"),
          [("a", "12.5%"), ("b", "8%"), ("c", "80%"), ("d", "0.125%")])}
{enlace(n, t("formulas", "formulas"), t("the straight-line depreciation formulas", "las fórmulas de la depreciación lineal"), t("Find D = (V₀ − Vr) ÷ n, the yearly rate, and the value in any year.", "Calcule D = (V₀ − Vr) ÷ n, la tasa anual y el valor en cualquier año."))}'''

    s4 = f'''<p>{t("In real life, money decisions mix several ideas: the percent of a tax, the interest on a loan, and the loss of value of what you buy. The strategy: solve each part on its own, then put the results together.", "En la vida real, las decisiones de dinero mezclan varias ideas: el porcentaje de un impuesto, el interés de un préstamo y la pérdida de valor de lo que se compra. La estrategia es resolver cada parte por separado y después juntar los resultados.")}</p>
{ej(t("Example: the business van", "Ejemplo: la camioneta del negocio"), t("Rosa borrows $18,000 at 6% simple interest a year for 3 years to buy a van for her business. The van has a useful life of 6 years and a salvage value of $3,000. When she finishes paying the loan, how much has she paid in all, and what is the van worth?", "Rosa pide un préstamo de $18,000 al 6% de interés simple anual, a 3 años, para comprar una camioneta para su negocio. La camioneta tiene una vida útil de 6 años y un valor residual de $3,000. Al terminar de pagar el préstamo, ¿cuánto pagó en total y cuánto vale la camioneta?"),
  [("1", t("The loan.", "El préstamo."), t("I = 18,000 × 0.06 × 3 = 3,240; total paid A = 18,000 + 3,240 = 21,240.", "I = 18,000 × 0.06 × 3 = 3,240; total pagado A = 18,000 + 3,240 = 21,240.")),
   ("2", t("The depreciation.", "La depreciación."), t("D = (18,000 − 3,000) ÷ 6 = 2,500 per year.", "D = (18,000 − 3,000) ÷ 6 = 2,500 por año.")),
   ("3", t("Book value in year 3.", "Valor contable en el año 3."), "18,000 − 2,500 × 3 = 10,500."),
   ("4", t("What it means.", "Interpretación."), "21,240 − 10,500 = 10,740."),
   ("✓", t("Answer.", "Respuesta."), t("Rosa paid <strong>$21,240</strong> and the van is worth <strong>$10,500</strong>. Using it for three years really cost her $10,740.", "Rosa pagó <strong>$21,240</strong> y la camioneta vale <strong>$10,500</strong>. Usarla durante tres años le costó, en realidad, $10,740."))])}
{ej(t("Example: tax and depreciation", "Ejemplo: impuesto y depreciación"), t("A laptop costs $1,200 plus a 10% sales tax. It will be used for 3 years and at the end will be worth $120. What is it worth after 2 years?", "Una laptop cuesta $1,200 más un impuesto sobre ventas del 10%. Se usará 3 años y al final valdrá $120. ¿Cuánto vale después de 2 años?"),
  [("1", t("Starting value with tax (Lesson 5.3).", "Valor inicial con impuesto (Lección 5.3)."), "1,200 × 1.10 = 1,320."),
   ("2", t("Yearly depreciation.", "Depreciación anual."), "D = (1,320 − 120) ÷ 3 = 1,200 ÷ 3 = 400."),
   ("3", t("Book value in year 2.", "Valor contable en el año 2."), "1,320 − 400 × 2 = 520."),
   ("✓", t("Answer.", "Respuesta."), t("After 2 years it is worth <strong>$520</strong>.", "Después de 2 años vale <strong>$520</strong>."))])}
{practica("p6", t("Practice 6 — The real cost", "Práctica 6 — El costo real"), t("Ana borrows $10,000 at 5% simple interest a year for 2 years to buy a truck. The truck has a useful life of 5 years and a salvage value of $2,000. When she finishes paying, how much did using the truck really cost her (total paid − book value)?", "Ana pide un préstamo de $10,000 al 5% de interés simple anual, a 2 años, para comprar una camioneta. La camioneta tiene una vida útil de 5 años y un valor residual de $2,000. Al terminar de pagar, ¿cuánto le costó en realidad usar la camioneta (total pagado − valor contable)?"),
          [("a", "$1,000"), ("b", "$3,200"), ("c", "$6,800"), ("d", "$4,200")])}
{enlace(n, t("combined", "integrados"), t("combined money problems", "problemas financieros integrados"), t("Combine interest, tax, and depreciation in the same problem.", "Combine interés, impuesto y depreciación en un mismo problema."))}'''

    secciones = [("s-" + t("vocabulary", "vocabulario"), t("Depreciation vocabulary", "Vocabulario de la depreciación"), s1),
                 ("s-" + t("table", "tabla"), t("First the table, then the formula", "Primero la tabla, después la fórmula"), s2),
                 ("s-" + t("formulas", "formulas"), t("The straight-line depreciation formulas", "Las fórmulas de la depreciación lineal"), s3),
                 ("s-" + t("combined", "integrados"), t("Combined money problems", "Problemas financieros integrados"), s4)]

    lesson = {"next": t("Lesson 6.3", "Lección 6.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You divided $2,600 without first subtracting the salvage value.", "Dividió $2,600 sin restar antes el valor residual."), "c": t("$2,000 is the total loss. Split it among the 5 years.", "$2,000 es la pérdida total. Repártala entre los 5 años."), "d": t("$600 is the salvage value.", "$600 es el valor residual.")},
             "right": t("(2,600 − 600) ÷ 5 = $400 a year.", "(2,600 − 600) ÷ 5 = $400 por año."), "solution": t("D = (2,600 − 600) ÷ 5 = 2,000 ÷ 5 = 400.", "D = (2,600 − 600) ÷ 5 = 2,000 ÷ 5 = 400.")},
      "p2": {"ok": "d", "hints": {"a": t("$1,200 is the depreciation built up in 3 years. Subtract it from $2,600.", "$1,200 es la depreciación acumulada en 3 años. Réstela de $2,600."), "b": t("You used $520 a year. First subtract the salvage value.", "Usó $520 por año. Primero reste el valor residual."), "c": t("$1,000 is the value at the end of year 4.", "$1,000 es el valor al final del año 4.")},
             "right": t("2,600 − 400 × 3 = $1,400.", "2,600 − 400 × 3 = $1,400."), "solution": t("Book value = 2,600 − 400 × 3 = 2,600 − 1,200 = 1,400.", "Valor contable = 2,600 − 400 × 3 = 2,600 − 1,200 = 1,400.")},
      "p3": {"ok": "a", "hints": {"b": t("You divided $900 without subtracting the salvage value.", "Dividió $900 sin restar el valor residual."), "c": t("Check: 900 − 100 = 800, and 800 ÷ 4.", "Revise: 900 − 100 = 800, y 800 ÷ 4."), "d": t("$800 is the total loss. Divide by 4.", "$800 es la pérdida total. Divida entre 4.")},
             "right": t("(900 − 100) ÷ 4 = $200.", "(900 − 100) ÷ 4 = $200."), "solution": t("D = (900 − 100) ÷ 4 = 800 ÷ 4 = 200.", "D = (900 − 100) ÷ 4 = 800 ÷ 4 = 200.")},
      "p4": {"ok": "c", "hints": {"a": t("That is the value at the end of year 2.", "Ese es el valor al final del año 2."), "b": t("$240 is the depreciation for 3 years. Subtract it from $450.", "$240 es la depreciación de 3 años. Réstela de $450."), "d": t("$80 is the yearly depreciation.", "$80 es la depreciación anual.")},
             "right": t("D = 80; 450 − 80 × 3 = $210.", "D = 80; 450 − 80 × 3 = $210."), "solution": t("D = (450 − 50) ÷ 5 = 80. Book value = 450 − 80 × 3 = 210.", "D = (450 − 50) ÷ 5 = 80. Valor contable = 450 − 80 × 3 = 210.")},
      "p5": {"ok": "a", "hints": {"b": t("The rate is 1 ÷ n, not n.", "La tasa es 1 ÷ n, no n."), "c": t("Check: 1 ÷ 8 = 0.125.", "Revise: 1 ÷ 8 = 0.125."), "d": t("0.125 is the decimal. Multiply by 100.", "0.125 es el decimal. Multiplique por 100.")},
             "right": t("1 ÷ 8 = 0.125 = 12.5% a year.", "1 ÷ 8 = 0.125 = 12.5% por año."), "solution": t("Rate = 1 ÷ 8 = 0.125 = 12.5% a year.", "Tasa = 1 ÷ 8 = 0.125 = 12.5% por año.")},
      "p6": {"ok": "d", "hints": {"a": t("$1,000 is only the interest. Find the total paid and the book value.", "$1,000 es solo el interés. Halle el total pagado y el valor contable."), "b": t("$3,200 is the depreciation for 2 years; the interest is missing.", "$3,200 es la depreciación de 2 años; falta el interés."), "c": t("$6,800 is the book value. Subtract it from the total paid.", "$6,800 es el valor contable. Réstelo del total pagado.")},
             "right": t("Paid 11,000; worth 6,800; real cost $4,200.", "Pagó 11,000; vale 6,800; costo real $4,200."), "solution": t("I = 10,000 × 0.05 × 2 = 1,000, total 11,000. D = (10,000 − 2,000) ÷ 5 = 1,600; value = 10,000 − 3,200 = 6,800. Real cost = 11,000 − 6,800 = 4,200.", "I = 10,000 × 0.05 × 2 = 1,000, total 11,000. D = (10,000 − 2,000) ÷ 5 = 1,600; valor = 10,000 − 3,200 = 6,800. Costo real = 11,000 − 6,800 = 4,200.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("First subtract the salvage value.", "Primero reste el valor residual."), "c": t("That is the total loss.", "Esa es la pérdida total."), "d": t("You added the salvage value instead of subtracting it.", "Sumó el valor residual en lugar de restarlo.")}, "solution": t("(1,800 − 200) ÷ 4 = $400.", "(1,800 − 200) ÷ 4 = $400.")},
      "B": {"ok": "d", "hints": {"a": t("The rate is 1 ÷ n.", "La tasa es 1 ÷ n."), "b": t("0.2 is the decimal; write it as a percent.", "0.2 es el decimal; páselo a porcentaje."), "c": t("Check: 1 ÷ 5 = 0.2.", "Revise: 1 ÷ 5 = 0.2.")}, "solution": t("1 ÷ 5 = 0.20 = 20%.", "1 ÷ 5 = 0.20 = 20%.")},
      "C": {"ok": "a", "hints": {"b": t("You used 3,000 ÷ 5 = 600. Subtract the salvage value first.", "Usó 3,000 ÷ 5 = 600. Reste antes el valor residual."), "c": t("$1,000 is the value in year 4.", "$1,000 es el valor en el año 4."), "d": t("$500 is the salvage value, at the end of year 5.", "$500 es el valor residual, al final del año 5.")}, "solution": t("D = 500; 3,000 − 500 × 3 = $1,500.", "D = 500; 3,000 − 500 × 3 = $1,500.")},
      "D": {"ok": "c", "hints": {"a": t("In 2 years it loses only $1,000.", "En 2 años pierde solo $1,000."), "b": t("In year 5 it is worth the salvage value, $500.", "En el año 5 vale el valor residual, $500."), "d": t("In year 3 it is worth $1,500.", "En el año 3 vale $1,500.")}, "solution": t("It must lose 2,000; 2,000 ÷ 500 = 4.", "Tiene que perder 2,000; 2,000 ÷ 500 = 4.")},
      "E": {"ok": "b", "hints": {"a": t("$12,000 is the loss in 4 years.", "$12,000 es la pérdida en 4 años."), "c": t("You took 10% of each new value. Here it is 10% of the original cost.", "Tomó el 10% de cada valor nuevo. Aquí es el 10% del costo original."), "d": t("$27,000 is the value after only 1 year.", "$27,000 es el valor después de solo 1 año.")}, "solution": t("D = 3,000; 30,000 − 3,000 × 4 = $18,000.", "D = 3,000; 30,000 − 3,000 × 4 = $18,000.")},
      "F": {"ok": "d", "hints": {"a": t("The rate is 1 ÷ n, not n.", "La tasa es 1 ÷ n, no n."), "b": t("Check: 1 ÷ 8.", "Revise: 1 ÷ 8."), "c": t("0.125 is the decimal; multiply by 100.", "0.125 es el decimal; multiplique por 100.")}, "solution": t("1 ÷ 8 = 0.125 = 12.5%.", "1 ÷ 8 = 0.125 = 12.5%.")},
      "G": {"ok": "a", "hints": {"b": t("$3,240 is the interest. Add the loan.", "$3,240 es el interés. Sume el préstamo."), "c": t("That has only one year of interest.", "Eso tiene solo un año de interés."), "d": t("$10,500 is the van's book value.", "$10,500 es el valor contable de la camioneta.")}, "solution": t("I = 18,000 × 0.06 × 3 = 3,240; A = $21,240.", "I = 18,000 × 0.06 × 3 = 3,240; A = $21,240.")},
      "H": {"ok": "c", "hints": {"a": t("You left out the tax. The starting value is $1,320.", "Dejó fuera el impuesto. El valor inicial es $1,320."), "b": t("$800 is the depreciation in 2 years.", "$800 es la depreciación de 2 años."), "d": t("$920 is the value after only 1 year.", "$920 es el valor después de solo 1 año.")}, "solution": t("V₀ = 1,320; D = 400; 1,320 − 800 = $520.", "V₀ = 1,320; D = 400; 1,320 − 800 = $520.")}
     }}

    quiz = [
     ("A", t("A $1,800 computer has a salvage value of $200 and a useful life of 4 years. What is its yearly depreciation?", "Una computadora de $1,800 tiene un valor residual de $200 y una vida útil de 4 años. ¿Cuál es su depreciación anual?"), [("a", "$450"), ("b", "$400"), ("c", "$1,600"), ("d", "$500")]),
     ("B", t("An item has a useful life of 5 years. What is its yearly rate of straight-line depreciation?", "Un bien tiene una vida útil de 5 años. ¿Cuál es su tasa anual de depreciación lineal?"), [("a", "5%"), ("b", "0.2%"), ("c", "50%"), ("d", "20%")]),
     ("C", t("A $3,000 machine has a salvage value of $500 and a useful life of 5 years. What is its book value at the end of year 3?", "Una máquina de $3,000 tiene un valor residual de $500 y una vida útil de 5 años. ¿Cuál es su valor contable al final del año 3?"), [("a", "$1,500"), ("b", "$1,200"), ("c", "$1,000"), ("d", "$500")]),
     ("D", t("With the same machine, at the end of what year will its book value be $1,000?", "Con la misma máquina, ¿al final de qué año su valor contable será de $1,000?"), [("a", t("Year 2", "Año 2")), ("b", t("Year 5", "Año 5")), ("c", t("Year 4", "Año 4")), ("d", t("Year 3", "Año 3"))]),
     ("E", t("A $30,000 van depreciates 10% of its original cost each year. What is it worth after 4 years?", "Una camioneta de $30,000 se deprecia un 10% anual de su costo original. ¿Cuánto vale después de 4 años?"), [("a", "$12,000"), ("b", "$18,000"), ("c", "$19,683"), ("d", "$27,000")]),
     ("F", t("An item has a useful life of 8 years. What is its yearly rate of straight-line depreciation?", "Un bien tiene una vida útil de 8 años. ¿Cuál es su tasa anual de depreciación lineal?"), [("a", "8%"), ("b", "80%"), ("c", "0.125%"), ("d", "12.5%")]),
     ("G", t("Rosa borrows $18,000 at 6% simple interest a year for 3 years. How much does she pay back in all?", "Rosa pide un préstamo de $18,000 al 6% de interés simple anual, a 3 años. ¿Cuánto devuelve en total?"), [("a", "$21,240"), ("b", "$3,240"), ("c", "$19,080"), ("d", "$10,500")]),
     ("H", t("A laptop costs $1,200 plus a 10% tax. It will be used for 3 years and at the end will be worth $120. What is it worth after 2 years?", "Una laptop cuesta $1,200 más un 10% de impuesto. Se usará 3 años y al final valdrá $120. ¿Cuánto vale después de 2 años?"), [("a", "$480"), ("b", "$800"), ("c", "$520"), ("d", "$920")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("The mirror image of simple interest: things that lose the same amount of value every year. The book-value table, the formula D = (V₀ − Vr) ÷ n, and problems that mix interest, tax, and depreciation.", "El espejo del interés simple: bienes que pierden la misma cantidad de valor cada año. La tabla del valor contable, la fórmula D = (V₀ − Vr) ÷ n y problemas que combinan interés, impuesto y depreciación."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Explain</strong> starting value, salvage value, useful life, and book value.", "<strong>Explicar</strong> qué significan el valor inicial, el valor residual, la vida útil y el valor contable."),
         t("<strong>Build</strong> the book-value table year by year before using the formula.", "<strong>Construir</strong> la tabla del valor contable año por año antes de usar la fórmula."),
         t("<strong>Find</strong> the yearly straight-line depreciation, (V₀ − Vr) ÷ n, and its yearly rate.", "<strong>Calcular</strong> la depreciación lineal anual, (V₀ − Vr) ÷ n, y su tasa anual."),
         t("<strong>Find</strong> the book value of an item in a given year.", "<strong>Determinar</strong> el valor contable de un bien en un año específico."),
         t("<strong>Solve</strong> money problems that combine percent, simple interest, and depreciation.", "<strong>Resolver</strong> problemas financieros que combinan porcentaje, interés simple y depreciación.")],
        secciones,
        (t("Solve six straight-line depreciation problems: yearly depreciation, yearly rate, the table, and the book value in a given year. Then solve four review problems on simple interest (Lesson 6.1).",
           "Resuelva seis problemas de depreciación lineal: depreciación anual, tasa anual, tabla y valor contable en un año específico. Después, resuelva cuatro problemas de repaso de interés simple (Lección 6.1)."),
         t("Think of something you or your family use for work or at home: a car, a phone, a tool. Estimate what it cost, how many years it will last, and what it will be worth at the end. Build its book-value table.",
           "Piense en algo que usted o su familia usan para trabajar o en casa: un carro, un teléfono, una herramienta. Estime cuánto costó, cuántos años durará y cuánto valdrá al final. Construya su tabla de valor contable.")),
        quiz,
        t("Self-check checklist for depreciation", "Lista de autoevaluación de depreciación"),
        t("Self-check checklist: skills for money math", "Lista de autoevaluación: destrezas de matemáticas financieras"),
        [(t("Find the yearly depreciation and its rate", "Calcular la depreciación anual y su tasa"), t("I find D = (V₀ − Vr) ÷ n and the rate 1 ÷ n, and I also solve problems that give a percent of the original cost.", "Calculo D = (V₀ − Vr) ÷ n y la tasa 1 ÷ n, y también resuelvo problemas que dan un porcentaje del costo original."), t("I find D with help or with mistakes in the operations.", "Calculo D con apoyo o con errores de operación."), t("I divide the starting value by the useful life without subtracting the salvage value.", "Divido el valor inicial entre la vida útil sin restar el valor residual.")),
         (t("Build or read the book-value table", "Construir o interpretar la tabla de valor contable"), t("I build the full table, check it with V₀ − D × t, and find in what year a value is reached.", "Construyo la tabla completa, la compruebo con V₀ − D × t y hallo en qué año se alcanza un valor."), t("I build the table, with some subtraction mistakes.", "Construyo la tabla, con algunos errores de resta."), t("The table is incomplete or does not show the pattern.", "La tabla está incompleta o no muestra el patrón.")),
         (t("Solve a combined money problem", "Resolver un problema financiero integrado"), t("I solve the interest part and the depreciation part and explain what the result means, for example, the real cost of using an item.", "Resuelvo la parte del interés y la de la depreciación, y explico qué significa el resultado; por ejemplo, el costo real de usar un bien."), t("I solve only one of the two parts correctly.", "Resuelvo bien solo una de las dos partes."), t("I do not separate the interest part from the depreciation part.", "No separo la parte del interés de la parte de la depreciación."))],
        t("<p>Straight-line depreciation is the mirror image of simple interest: instead of adding a fixed amount every year, you <strong>subtract</strong> it. With the year-by-year table and the formula D = (V₀ − Vr) ÷ n you can tell what an item is worth at any time and what it really costs to use it.</p>\n<p>That completes the money part of Topic 6. <strong>Lesson 6.3 · Converting between U.S. customary and metric units</strong> changes the setting but not the tool: to convert between the two systems you also multiply by a fixed number, the conversion factor, with the same proportional reasoning as in Topic 4.</p>",
          "<p>La depreciación lineal es el espejo del interés simple: en lugar de sumar una cantidad fija cada año, se <strong>resta</strong>. Con la tabla año por año y la fórmula D = (V₀ − Vr) ÷ n se puede saber cuánto vale un bien en cualquier momento y cuánto cuesta en realidad usarlo.</p>\n<p>Con esto se completa la parte financiera del Tema 6. La <strong>Lección 6.3 · Conversiones entre el sistema inglés y el métrico</strong> cambia de terreno, pero no de herramienta: para convertir entre los dos sistemas también se multiplica por una cantidad fija, el factor de conversión, con el mismo razonamiento proporcional del Tema 4.</p>"),
        ("6-3", ("", t("Lesson 6.3 · Converting between U.S. customary and metric units", "Lección 6.3 · Conversiones entre el sistema inglés y el métrico"))),
        [(t("straight-line depreciation", "depreciación lineal"), t("A loss of value that is the same every year.", "Pérdida de valor que es la misma cada año.")),
         (t("salvage value (Vr)", "valor residual (Vr)"), t("What an item is still worth at the end of its useful life.", "Lo que todavía vale un bien al final de su vida útil.")),
         (t("useful life (n)", "vida útil (n)"), t("The number of years an item is expected to be used.", "Los años que se espera usar un bien.")),
         (t("book value", "valor contable"), t("What an item is worth, by the calculations, in a given year: V₀ − D × t.", "Lo que vale un bien, según los cálculos, en un año dado: V₀ − D × t."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "voc": [["What the item will be worth at the end of its useful life.", "Salvage value", "valor residual"], ["The number of years the item is expected to be used.", "Useful life", "vida útil"], ["What the item is worth, by the calculations, at the end of a given year.", "Book value", "valor contable"], ["What the item loses each year.", "Yearly depreciation", "depreciación anual"], ["What the item has lost up to a given year.", "Accumulated depreciation", "depreciación acumulada"], ["Something of value you buy to use for several years.", "Asset", "activo o bien"]],
  "vocOtro": "A document in Spanish says “{x}”. What is the term in English?", "vocDef": "Which term matches this definition? “{x}”", "vocSol": "It is the {t} (in Spanish, {o}).", "vocSol2": "“{o}” is the {t}.",
  "bienes": ["a commercial refrigerator", "a computer", "an industrial sewing machine", "a delivery van", "a bakery oven", "a copy machine"],
  "tbEnun": "A business buys {b} for <strong>{V}</strong>. Its useful life is <strong>{n} years</strong> and its salvage value is <strong>{R}</strong>. Find the yearly depreciation and fill in the book values.",
  "tbCap": "Book value year by year", "tbCab": ["Year", "Book value ($)"], "tbLab": "Book value in year {k}",
  "tbBien": "✓ All correct. D = ({V} − {R}) ÷ {n} = {D}, and in the last year exactly the salvage value is left.",
  "tbDok": "The yearly depreciation is right. ", "tbDmal": "Check the yearly depreciation: first the total loss, V₀ − Vr, then divide by the years. ", "tbV0": "It looks like you divided the starting value without first subtracting the salvage value. ",
  "tbFaltan": "{k} {v} to check (in red). Try again.", "tbUno": "value", "tbVarios": "values",
  "tbSol": "Here is the complete table. D = ({V} − {R}) ÷ {n} = {D}. Each year, subtract {D}. Try another item.",
  "tbVoz": "Book value year by year, going down {D} each year until {R}.", "anoW": "Year",
  "fm1": "{D} a year. Yearly rate: 1 ÷ {n} = {p}%.", "fm2": "Book value in year {t}: {V} − {D} × {t} = {x}", "fmNota": "After its useful life the item does not depreciate any more: it stays at its salvage value.",
  "fmRes": "D = ({V} − {R}) ÷ {n} = ",
  "obj": ["An industrial machine", "A truck", "A computer", "A sound system", "A commercial stove"],
  "fmBase": "{b} costs {V}, has a useful life of {n} years, and a salvage value of {R}. ",
  "fmQ1": "What is its yearly depreciation?", "fmQ2": "What is its yearly rate of depreciation, as a percent?", "fmQ3": "What is its book value at the end of year {t}?", "fmQ4": "At the end of what year will its book value be {M}?",
  "fmS1": "({V} − {R}) ÷ {n} = {D}.", "fmS2": "1 ÷ {n} = {d} = {p}%.", "fmS3": "D = {D}; {V} − {D2} × {t} = {x}.", "fmS4": "It must lose {L}; {L2} ÷ {D2} = {t}.",
  "fmP1": "First subtract the salvage value: the total loss is V₀ − Vr.", "fmP2": "Write it as a percent: multiply by 100.", "fmP3": "The yearly depreciation uses V₀ − Vr, not V₀ alone.", "fmP4": "That is the year before; check: {V} − {D2} × {k}.",
  "nombres": ["Rosa", "Pedro", "Carmen", "Luis"],
  "in1": "{n} borrows {C} at {r} simple interest a year for {t} years to buy a van for the business. The van has a useful life of {u} years and a salvage value of {R}. ",
  "in1a": "How much is paid back in all for the loan?", "in1b": "When the loan is paid off, what is the van worth?", "in1c": "When the loan is paid off, how much did using the van really cost (total paid − book value)?",
  "in1sa": "I = {C2} × {d} × {t} = {I}; total: {C} + {I} = {A}.", "in1sb": "D = ({C2} − {R2}) ÷ {u} = {D}; in {t} years: {C2} − {D2} × {t} = {x}.", "in1sc": "Paid: {A}. Worth: {C2} − {D2} × {t} = {V}. Real cost: {A} − {V} = {x}.",
  "in1pa": "That is the interest. The total paid is the loan plus the interest.", "in1pc": "That is only the depreciation; the interest is missing.",
  "in2": "A computer costs {P} plus {i} sales tax. It will be used for {n} years and then sold for {R}. The depreciation is figured on the price with tax. ",
  "in2a": "How much is paid when you buy it?", "in2b": "What is its book value at the end of year {k}?",
  "in2sa": "{P2} × {f} = {T}.", "in2sb": "V₀ = {P2} × {f} = {T}; D = ({T2} − {R2}) ÷ {n} = {D}; {T2} − {D2} × {k} = {x}.",
  "in2pa": "That is only the tax. Add it to the price.", "in2pb": "Start from the price with tax, {T}.",
  "in3": "{n} saves {S} at {r} simple interest a year for {t} years to buy a used car that costs {P}. How much money will be missing at the end?",
  "in3s": "A = {S2} + {S2} × {d} × {t} = {A}; missing: {P} − {A} = {x}.", "in3p": "Add the interest earned to the savings first."
 },
 "es": {
  "voc": [["Lo que valdrá el bien al final de su vida útil.", "Valor residual", "salvage value"], ["Los años que se espera usar el bien.", "Vida útil", "useful life"], ["Lo que vale el bien, según los cálculos, al final de un año dado.", "Valor contable", "book value"], ["Lo que pierde el bien cada año.", "Depreciación anual", "annual depreciation"], ["Lo que ha perdido el bien hasta un año dado.", "Depreciación acumulada", "accumulated depreciation"], ["Algo de valor que se compra para usarlo varios años.", "Activo o bien", "asset"]],
  "vocOtro": "En un documento en inglés aparece «{x}». ¿Qué término es en español?", "vocDef": "¿Qué término corresponde a esta definición? «{x}»", "vocSol": "Es el {t} (en inglés, {o}).", "vocSol2": "«{o}» es el {t}.",
  "bienes": ["un refrigerador comercial", "una computadora", "una máquina de coser industrial", "una camioneta de reparto", "un horno de panadería", "una fotocopiadora"],
  "tbEnun": "Un negocio compra {b} por <strong>{V}</strong>. Su vida útil es de <strong>{n} años</strong> y su valor residual, <strong>{R}</strong>. Calcule la depreciación anual y complete los valores contables.",
  "tbCap": "Valor contable año por año", "tbCab": ["Año", "Valor contable ($)"], "tbLab": "Valor contable del año {k}",
  "tbBien": "✓ Todo correcto. D = ({V} − {R}) ÷ {n} = {D}, y en el último año queda justo el valor residual.",
  "tbDok": "La depreciación anual está bien. ", "tbDmal": "Revise la depreciación anual: primero la pérdida total, V₀ − Vr, y después entre los años. ", "tbV0": "Parece que se dividió el valor inicial sin restar antes el valor residual. ",
  "tbFaltan": "Hay {k} {v} por revisar (en rojo). Inténtelo de nuevo.", "tbUno": "valor", "tbVarios": "valores",
  "tbSol": "Así queda la tabla completa. D = ({V} − {R}) ÷ {n} = {D}. Cada año se restan {D}. Pruebe con otro bien.",
  "tbVoz": "Valor contable año por año, bajando {D} cada año hasta {R}.", "anoW": "Año",
  "fm1": "{D} por año. Tasa anual: 1 ÷ {n} = {p}%.", "fm2": "Valor contable en el año {t}: {V} − {D} × {t} = {x}", "fmNota": "Después de la vida útil el bien ya no se deprecia más: se queda en su valor residual.",
  "fmRes": "D = ({V} − {R}) ÷ {n} = ",
  "obj": ["Una máquina industrial", "Un camión", "Una computadora", "Un equipo de sonido", "Una estufa comercial"],
  "fmBase": "{b} cuesta {V}, tiene una vida útil de {n} años y un valor residual de {R}. ",
  "fmQ1": "¿Cuál es la depreciación anual?", "fmQ2": "¿Cuál es la tasa anual de depreciación, en porcentaje?", "fmQ3": "¿Cuál es su valor contable al final del año {t}?", "fmQ4": "¿Al final de qué año su valor contable será de {M}?",
  "fmS1": "({V} − {R}) ÷ {n} = {D}.", "fmS2": "1 ÷ {n} = {d} = {p}%.", "fmS3": "D = {D}; {V} − {D2} × {t} = {x}.", "fmS4": "Tiene que perder {L}; {L2} ÷ {D2} = {t}.",
  "fmP1": "Primero hay que restar el valor residual: la pérdida total es V₀ − Vr.", "fmP2": "Escríbala en porcentaje: multiplique por 100.", "fmP3": "La depreciación anual se calcula con V₀ − Vr, no con V₀ solo.", "fmP4": "Ese es el año anterior; revise: {V} − {D2} × {k}.",
  "nombres": ["Rosa", "Pedro", "Carmen", "Luis"],
  "in1": "{n} pide un préstamo de {C} al {r} de interés simple anual, a {t} años, para comprar una camioneta para su negocio. La camioneta tiene una vida útil de {u} años y un valor residual de {R}. ",
  "in1a": "¿Cuánto se devuelve en total por el préstamo?", "in1b": "Al terminar de pagar el préstamo, ¿cuánto vale la camioneta?", "in1c": "Al terminar de pagar el préstamo, ¿cuánto costó en realidad usar la camioneta (total pagado − valor contable)?",
  "in1sa": "I = {C2} × {d} × {t} = {I}; total: {C} + {I} = {A}.", "in1sb": "D = ({C2} − {R2}) ÷ {u} = {D}; en {t} años: {C2} − {D2} × {t} = {x}.", "in1sc": "Pagado: {A}. Vale: {C2} − {D2} × {t} = {V}. Costo real: {A} − {V} = {x}.",
  "in1pa": "Ese es el interés. El total pagado es el préstamo más el interés.", "in1pc": "Eso es solo la depreciación; falta el interés.",
  "in2": "Una computadora cuesta {P} más un {i} de impuesto sobre ventas. Se usará {n} años y después se venderá en {R}. La depreciación se calcula sobre el precio con impuesto. ",
  "in2a": "¿Cuánto se paga al comprarla?", "in2b": "¿Cuál es su valor contable al final del año {k}?",
  "in2sa": "{P2} × {f} = {T}.", "in2sb": "V₀ = {P2} × {f} = {T}; D = ({T2} − {R2}) ÷ {n} = {D}; {T2} − {D2} × {k} = {x}.",
  "in2pa": "Eso es solo el impuesto. Súmelo al precio.", "in2pb": "Parta del precio con impuesto, {T}.",
  "in3": "{n} ahorra {S} al {r} de interés simple anual durante {t} años para comprar un carro usado de {P}. ¿Cuánto dinero le faltará al final?",
  "in3s": "A = {S2} + {S2} × {d} × {t} = {A}; faltan {P} − {A} = {x}.", "in3p": "Primero sume al ahorro el interés ganado."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function sinU(t){ return String(t).replace(/%/g, ""); }
function barrasV(vals, voz){
  var W = 640, H = 240, x0 = 70, x1 = 620, yb = 200, mx = Math.max.apply(null, vals), n = vals.length, w = (x1 - x0) / n * 0.62, s = '<svg class="figura" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + voz + '">';
  function Y(v){ return yb - v * 170 / mx; }
  vals.forEach(function(v, k){
    var x = x0 + (x1 - x0) * k / n + (x1 - x0) / n * 0.19;
    s += '<rect x="' + f1(x) + '" y="' + f1(Y(v)) + '" width="' + f1(w) + '" height="' + f1(yb - Y(v)) + '" fill="#00897b"/>';
    s += texto([x + w / 2, Y(v) - 6], dinero(v), 12, "#004d40", 700);
    s += texto([x + w / 2, yb + 16], k, 13, "#424242", 400);
  });
  return s + linea([x0, yb], [x1, yb], "#424242", 2) + texto([(x0 + x1) / 2, H - 4], TXT.anoW, 13, "#424242", 700) + '</svg>';
}

/* ============ MODULE 1 · vocabulary ============ */
function genVoc(){
  var i = aleatorio(0, TXT.voc.length - 1), v = TXT.voc[i], otro = Math.random() < 0.35;
  var otros = baraja(TXT.voc.filter(function(x, j){ return j !== i; })).slice(0, 3);
  var op = [v].concat(otros).map(function(x){ return { html: x[1], clave: x[1] }; });
  var sol = F(otro ? TXT.vocSol2 : TXT.vocSol, { t: v[1].toLowerCase(), o: v[2] });
  return { enun: F(otro ? TXT.vocOtro : TXT.vocDef, { x: otro ? v[2] : v[0] }), opciones: op, correcta: v[1], bien: sol, mal: sol };
}

/* ============ MODULE 2 · fill in the table (hint first, then the answer) ============ */
var TB = {};
function nuevoTB(ini){
  var n = aleatorio(3, 6), D = 50 * aleatorio(4, 40), Vr = 100 * aleatorio(1, 20), V0 = Vr + D * n;
  if (ini){ V0 = 2600; Vr = 600; n = 5; D = 400; }
  TB = { V0: V0, Vr: Vr, n: n, D: D, intentos: 0, listo: false };
  $("tb-enun").innerHTML = F(TXT.tbEnun, { b: ini ? TXT.bienes[0] : elige(TXT.bienes), V: dinero(V0), n: n, R: dinero(Vr) });
  var h = '<caption>' + TXT.tbCap + '</caption><thead><tr><th scope="col">' + TXT.tbCab[0] + '</th><th scope="col">' + TXT.tbCab[1] + '</th></tr></thead><tbody><tr><td>0</td><td>' + nd(V0) + '</td></tr>';
  for (var k = 1; k <= n; k++) h += '<tr><td>' + k + '</td><td id="tb-c' + k + '"><label class="sr-only" for="tb-v' + k + '">' + F(TXT.tbLab, { k: k }) + '</label><input type="text" inputmode="decimal" autocomplete="off" id="tb-v' + k + '"></td></tr>';
  $("tb-tabla").innerHTML = h + '</tbody>';
  $("tb-d").value = ""; $("tb-d").classList.remove("error"); $("tb-fb").className = "fb"; $("tb-fb").innerHTML = ""; $("tb-svg").innerHTML = ""; $("tb-comprobar").disabled = false;
}
function muestraBarras(){ var v = []; for (var k = 0; k <= TB.n; k++) v.push(TB.V0 - TB.D * k); $("tb-svg").innerHTML = barrasV(v, F(TXT.tbVoz, { D: dinero(TB.D), R: dinero(TB.Vr) })); }
function compruebaTB(){
  if (TB.listo) return;
  var d = leeD($("tb-d").value), bien = 0, fb = $("tb-fb"), o = { V: nd(TB.V0), R: nd(TB.Vr), n: TB.n, D: dinero(TB.D) };
  var okD = d !== null && Math.abs(d - TB.D) < 0.005;
  $("tb-d").classList.toggle("error", !okD);
  for (var k = 1; k <= TB.n; k++){ var v = leeD($("tb-v" + k).value), ok = v !== null && Math.abs(v - (TB.V0 - TB.D * k)) < 0.005; $("tb-c" + k).className = ok ? "bien" : "mal"; if (ok) bien++; }
  TB.intentos++;
  if (okD && bien === TB.n){ TB.listo = true; fb.className = "fb bien"; fb.innerHTML = F(TXT.tbBien, o); muestraBarras(); $("tb-comprobar").disabled = true; return; }
  if (TB.intentos >= 2){
    TB.listo = true; $("tb-d").value = nd(TB.D); $("tb-d").classList.remove("error");
    for (var j = 1; j <= TB.n; j++){ $("tb-v" + j).value = nd(TB.V0 - TB.D * j); $("tb-c" + j).className = ""; }
    fb.className = "fb mal"; fb.innerHTML = F(TXT.tbSol, o); muestraBarras(); $("tb-comprobar").disabled = true; return;
  }
  var falt = TB.n - bien, pista = okD ? TXT.tbDok : TXT.tbDmal + (d !== null && Math.abs(d - TB.V0 / TB.n) < 0.005 ? TXT.tbV0 : "");
  fb.className = "fb pista"; fb.innerHTML = pista + (falt ? F(TXT.tbFaltan, { k: falt, v: falt === 1 ? TXT.tbUno : TXT.tbVarios }) : "");
}

/* ============ MODULE 3 · formulas ============ */
function pintaFM(){
  var V0 = +$("fm-v").value, Vr = Math.min(+$("fm-r").value, V0), n = +$("fm-n").value, tq = +$("fm-t").value, tt = Math.min(tq, n), D = (V0 - Vr) / n;
  $("fm-vv").textContent = dinero(V0); $("fm-rv").textContent = dinero(Vr); $("fm-nv").textContent = n; $("fm-tv").textContent = tq;
  $("fm-salida").innerHTML = '<div class="linea">' + F(TXT.fmRes, { V: nd(V0), R: nd(Vr), n: n }) + F(TXT.fm1, { D: dinero2(D), n: n, p: nd(Math.round(10000 / n) / 100) }) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.fm2, { t: tt, V: nd(V0), D: dinero2(D), x: dinero2(V0 - D * tt) }) + '</div>' + (tq > n ? '<div class="linea">' + TXT.fmNota + '</div>' : '');
}
function genFM(){
  var n = elige([2, 4, 5, 8, 10]), D = 100 * aleatorio(2, 30), Vr = 100 * aleatorio(0, 20), V0 = Vr + D * n, tt = aleatorio(1, n), tp = aleatorio(1, 4), res, enun, sol, p = [];
  var o = { b: elige(TXT.obj), V: dinero(V0), n: n, R: dinero(Vr), D: dinero(D), D2: nd(D), t: tt };
  var base = F(TXT.fmBase, o);
  if (tp === 1){ res = D; enun = base + TXT.fmQ1; sol = F(TXT.fmS1, { V: nd(V0), R: nd(Vr), n: n, D: dinero(D) }); if (Vr) p.push({ v: V0 / n, msg: TXT.fmP1 }); }
  else if (tp === 2){ res = 100 / n; enun = base + TXT.fmQ2; sol = F(TXT.fmS2, { n: n, d: nd(1 / n), p: nd(100 / n) }); p.push({ v: 1 / n, msg: TXT.fmP2 }); }
  else if (tp === 3){ res = V0 - D * tt; enun = base + F(TXT.fmQ3, o); sol = F(TXT.fmS3, { D: dinero(D), V: nd(V0), D2: nd(D), t: tt, x: dinero(res) }); if (Vr) p.push({ v: V0 - V0 / n * tt, msg: TXT.fmP3 }); }
  else { var meta = V0 - D * tt; res = tt; enun = base + F(TXT.fmQ4, { M: dinero(meta) }); sol = F(TXT.fmS4, { L: dinero(V0 - meta), L2: nd(V0 - meta), D2: nd(D), t: tt });
    if (tt > 1) p.push({ v: tt - 1, msg: F(TXT.fmP4, { V: nd(V0), D2: nd(D), k: tt - 1 }) }); }
  p = p.filter(function(x){ return Math.abs(x.v - res) > 0.01; });
  var ev = numD(res, p, null, 0.006);
  return { enun: enun, correcta: tp === 2 ? nd(res) + "%" : (tp === 4 ? String(res) : dinero(res)), solucion: sol, evalua: function(s){ return ev(sinU(s)); } };
}

/* ============ MODULE 4 · combined problems ============ */
function genInt(){
  var tp = aleatorio(1, 3), res, enun, sol, p = [];
  if (tp === 1){
    var C = 1000 * aleatorio(10, 30), r = elige([4, 5, 6, 7]), tt = aleatorio(2, 4), I = C * r / 100 * tt, u = aleatorio(5, 8), R = 1000 * aleatorio(1, 4), D = (C - R) / u;
    if (D !== Math.round(D)) return genInt();
    var V = C - D * tt, q = aleatorio(1, 3), o = { n: elige(TXT.nombres), C: dinero(C), C2: nd(C), r: r + "%", d: nd(r / 100), t: tt, u: u, R: dinero(R), R2: nd(R), I: dinero(I), A: dinero(C + I), D: dinero(D), D2: nd(D), V: dinero(V) };
    enun = F(TXT.in1, o) + TXT["in1" + "abc"[q - 1]];
    if (q === 1){ res = C + I; o.x = dinero(res); sol = F(TXT.in1sa, o); p.push({ v: I, msg: TXT.in1pa }); }
    else if (q === 2){ res = V; o.x = dinero(res); sol = F(TXT.in1sb, o); }
    else { res = C + I - V; o.x = dinero(res); sol = F(TXT.in1sc, o); p.push({ v: D * tt, msg: TXT.in1pc }); }
  } else if (tp === 2){
    var P = 100 * aleatorio(8, 40), imp = elige([6, 7, 8, 9, 10]), Tt = Math.round(P * (100 + imp)) / 100, n2 = elige([3, 4, 5]), R2 = 10 * aleatorio(0, 30), D2 = (Tt - R2) / n2, k = aleatorio(1, n2 - 1);
    if (Math.abs(D2 * 100 - Math.round(D2 * 100)) > 1e-6) return genInt();
    var q2 = Math.random() < 0.4, o2 = { P: dinero(P), P2: nd(P), i: imp + "%", n: n2, R: dinero(R2), R2: nd(R2), f: nd(1 + imp / 100), T: dinero2(Tt), T2: nd(Tt), D: dinero2(D2), D2: nd(D2), k: k };
    res = q2 ? Tt : Tt - D2 * k; o2.x = dinero2(res);
    enun = F(TXT.in2, o2) + F(q2 ? TXT.in2a : TXT.in2b, o2); sol = F(q2 ? TXT.in2sa : TXT.in2sb, o2);
    if (q2) p.push({ v: Tt - P, msg: TXT.in2pa }); else p.push({ v: P - (P - R2) / n2 * k, msg: F(TXT.in2pb, o2) });
  } else {
    var S = 500 * aleatorio(4, 20), r3 = elige([3, 4, 5]), t3 = aleatorio(2, 5), A = S * (1 + r3 / 100 * t3), Pc = Math.round(A / 100) * 100 + 100 * aleatorio(1, 5);
    res = Pc - A;
    var o3 = { n: elige(TXT.nombres), S: dinero(S), S2: nd(S), r: r3 + "%", t: t3, P: dinero(Pc), d: nd(r3 / 100), A: dinero2(A), x: dinero2(res) };
    enun = F(TXT.in3, o3); sol = F(TXT.in3s, o3); p.push({ v: Pc - S, msg: TXT.in3p });
  }
  res = Math.round(res * 100) / 100;
  return { enun: enun, correcta: dinero(res), solucion: sol, evalua: numD(res, p.map(function(x){ return { v: Math.round(x.v * 100) / 100, msg: x.msg }; }).filter(function(x){ return Math.abs(x.v - res) > 0.011; }), null, 0.011) };
}

/* ============ Start ============ */
creaPracticaOM("p1", genVoc);
$("tb-comprobar").addEventListener("click", compruebaTB); $("tb-nuevo").addEventListener("click", function(){ nuevoTB(false); }); nuevoTB(true);
["fm-v", "fm-r", "fm-n", "fm-t"].forEach(function(id){ $(id).addEventListener("input", pintaFM); }); pintaFM();
creaPracticaLibre("p2", genFM);
creaPracticaLibre("p3", genInt);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:150px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    mods = [
     (t("vocabulary", "vocabulario"), t("Depreciation vocabulary", "Vocabulario de la depreciación"),
      f'''      <table class="reglas">
        <caption>{t("Depreciation words in English and in Spanish", "Términos de la depreciación, en español y en inglés")}</caption>
        <thead><tr><th scope="col">{t("Term", "Término")}</th><th scope="col">{t("What it is", "Qué es")}</th><th scope="col">{t("In Spanish", "En inglés")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Asset", "Activo o bien")}</td><td>{t("something of value used for several years", "algo de valor que se usa varios años")}</td><td>{t("activo o bien", "asset")}</td></tr>
          <tr><td>{t("Starting value (V₀)", "Valor inicial (V₀)")}</td><td>{t("what it cost when it was bought", "lo que costó al comprarlo")}</td><td>{t("valor inicial", "cost")}</td></tr>
          <tr><td>{t("Useful life (n)", "Vida útil (n)")}</td><td>{t("the years it is expected to be used", "los años que se espera usarlo")}</td><td>{t("vida útil", "useful life")}</td></tr>
          <tr><td>{t("Salvage value (Vr)", "Valor residual (Vr)")}</td><td>{t("what it will be worth at the end of its useful life", "lo que valdrá al final de su vida útil")}</td><td>{t("valor residual", "salvage value")}</td></tr>
          <tr><td>{t("Yearly depreciation (D)", "Depreciación anual (D)")}</td><td>{t("what it loses each year", "lo que pierde cada año")}</td><td>{t("depreciación anual", "annual depreciation")}</td></tr>
          <tr><td>{t("Book value", "Valor contable")}</td><td>{t("what it is worth, by the calculations, in a given year", "lo que vale según los cálculos en un año dado")}</td><td>{t("valor contable", "book value")}</td></tr>
          <tr><td>{t("Accumulated depreciation", "Depreciación acumulada")}</td><td>{t("what it has lost up to that year", "lo que ha perdido hasta ese año")}</td><td>{t("depreciación acumulada", "accumulated depreciation")}</td></tr>
        </tbody>
      </table>
{B.om("p1", t("Practice: vocabulary", "Practique: vocabulario"))}'''),
     (t("table", "tabla"), t("First the table, then the formula", "Primero la tabla, después la fórmula"),
      f'''      <p>{t("The total loss is the starting value minus the salvage value. It is split into equal parts among the years of useful life, and each year that amount is subtracted from the value of the year before. The value never drops below the salvage value.", "La pérdida total es el valor inicial menos el valor residual. Se reparte en partes iguales entre los años de vida útil, y cada año se resta esa cantidad al valor del año anterior. El valor nunca baja del valor residual.")}</p>
      <h3>{t("Fill in the table", "Complete la tabla")}</h3>
      <div class="panel">
        <p id="tb-enun"></p>
        <div class="campos"><div class="campo"><label for="tb-d">{t("Yearly depreciation D ($)", "Depreciación anual D ($)")}</label><input type="text" class="corto" id="tb-d" inputmode="decimal" autocomplete="off"></div></div>
        <div class="tabla-scroll"><table class="comparar tabla-dep" id="tb-tabla"></table></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="tb-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="tb-nuevo">{t("Another item", "Otro bien")}</button>
        </div>
        <div class="fb" id="tb-fb" role="status"></div>
        <div id="tb-svg"></div>
      </div>
      <p class="nota">{t("Type only numbers, without the $ sign if you like: 2,200 or 2200. If you make a mistake, you get a hint and another try; on the second try, the complete table appears.", "Escriba solo números; el signo $ es opcional: 2,200 o 2200. Si se equivoca, recibe una pista y otra oportunidad; en el segundo intento aparece la tabla completa.")}</p>'''),
     (t("formulas", "formulas"), t("The straight-line depreciation formulas", "Las fórmulas de la depreciación lineal"),
      f'''      <div class="formula">D = (V₀ − Vr) ÷ n &nbsp;&nbsp;&nbsp; {t("book value in year t = V₀ − D × t", "valor contable en el año t = V₀ − D × t")}</div>
      <p>{t("The yearly rate of straight-line depreciation is 1 ÷ n: if an item lasts 4 years, each year it loses one fourth (25%) of the value being depreciated.", "La tasa anual de la depreciación lineal es 1 ÷ n: si el bien dura 4 años, pierde cada año la cuarta parte (25%) de lo que se va a depreciar.")}</p>
      <h3>{t("Depreciation calculator", "Calculadora de depreciación")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("fm-v", t("Starting value", "Valor inicial"), 1000, 30000, 3000, 500)}
          {desl("fm-r", t("Salvage value", "Valor residual"), 0, 5000, 500, 100)}
          {desl("fm-n", t("Useful life (years)", "Vida útil (años)"), 2, 10, 5)}
          {desl("fm-t", t("Year", "Año"), 0, 10, 3)}
        </div>
        <div class="salida" id="fm-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Common mistake:", "Error frecuente:")}</strong> {t("dividing the starting value by the useful life without first subtracting the salvage value. With 3,000 ÷ 5 = 600, the machine would end up worth $0, not the $500 the problem says.", "dividir el valor inicial entre la vida útil sin restar antes el valor residual. Con 3,000 ÷ 5 = 600, la máquina terminaría valiendo $0 y no los $500 del enunciado.")}</div>
{libre_x("p2", t("Practice: straight-line depreciation", "Practique: depreciación lineal"), t("Answer", "Resultado"), t("Type only the number. If a rate is asked, write it as a percent (20 for 20%).", "Escriba solo el número. Si se pide una tasa, escríbala en porcentaje (20 para 20%)."))}'''),
     (t("combined", "integrados"), t("Combined money problems", "Problemas financieros integrados"),
      f'''      <p>{t("In real life a loan with interest, a tax, and the loss of value of what you buy all come together. The strategy: solve each part on its own, then put the results together.", "En la vida real se mezclan un préstamo con interés, un impuesto y la pérdida de valor de lo que se compra. La estrategia: resolver cada parte por separado y después juntar los resultados.")}</p>
      <table class="reglas">
        <caption>{t("The three tools of Topic 6 so far", "Las tres herramientas del Tema 6 hasta ahora")}</caption>
        <thead><tr><th scope="col">{t("Part of the problem", "Parte del problema")}</th><th scope="col">{t("Tool", "Herramienta")}</th></tr></thead>
        <tbody>
          <tr><td>{t("A tax or a discount", "Un impuesto o un descuento")}</td><td>{t("price × (1 + rate) or price × (1 − rate)", "precio × (1 + tasa) o precio × (1 − tasa)")}</td></tr>
          <tr><td>{t("A loan or savings", "Un préstamo o un ahorro")}</td><td>I = P × r × t; A = P + I</td></tr>
          <tr><td>{t("An item that loses value", "Un bien que pierde valor")}</td><td>D = (V₀ − Vr) ÷ n; V₀ − D × t</td></tr>
        </tbody>
      </table>
{libre_x("p3", t("Practice: combined problems", "Practique: problemas integrados"), t("Answer in dollars", "Resultado en dólares"), t("Type only the number. It may have cents, like 1,240.50; you may use the $ sign.", "Escriba solo el número. Puede llevar centavos, como 1,240.50; puede usar el signo $."))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Depreciación y otras aplicaciones financieras")
