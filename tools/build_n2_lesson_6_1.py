"""Level 2 · Lesson 6.1 · Simple interest: I = P × r × t — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "6-1"
TEMA = ("Money math and unit conversions", "Matemáticas financieras y conversiones de medidas")
TIT = ("Simple interest: I = P × r × t", "Interés simple: la fórmula I = P × r × t")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def escalera():
    """Barras del monto de $1,000 al 8% durante 10 años: principal oscuro, interés claro."""
    s, x0, x1, yb, mx = "", 60, 620, 200, 1800
    w = (x1 - x0) / 11 * 0.72
    Y = lambda v: yb - v * 170 / mx
    for k in range(11):
        v = 1000 + 80 * k
        x = x0 + (x1 - x0) * k / 11 + (x1 - x0) / 11 * 0.14
        s += f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{w:.1f}" height="{yb - Y(v):.1f}" fill="#b2dfdb"/>'
        s += f'<rect x="{x:.1f}" y="{Y(1000):.1f}" width="{w:.1f}" height="{yb - Y(1000):.1f}" fill="#00695c"/>'
        s += f'<text x="{x + w / 2:.1f}" y="{yb + 16}" text-anchor="middle" font-size="13" fill="#424242">{k}</text>'
    s += f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#424242" stroke-width="2"/>'
    s += f'<text x="340" y="236" text-anchor="middle" font-size="13" font-weight="700" fill="#424242">{t("Year", "Año")}</text>'
    s += f'<text x="54" y="{Y(1800) + 4:.1f}" text-anchor="end" font-size="12" fill="#424242">$1,800</text><text x="54" y="{Y(1000) + 4:.1f}" text-anchor="end" font-size="12" fill="#424242">$1,000</text>'
    return svg("0 0 640 240", t("Bars for each year from 0 to 10. The dark part of each bar, the $1,000 principal, stays the same; the light part, the interest, grows by $80 every year, up to $1,800 in year 10.",
                               "Barras de cada año, del 0 al 10. La parte oscura de cada barra, el principal de $1,000, no cambia; la parte clara, el interés, crece $80 cada año, hasta $1,800 en el año 10."), s, 640)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 5.3 you used percents for things that happen once: a discount, a tax, a tip. This lesson, the first of Topic 6, takes the next step: using a percent <strong>over time</strong>. Each year that money stays in an account or in a loan, the same percent is applied again.", "En la Lección 5.3 se aplicaron los porcentajes a situaciones de un solo momento: un descuento, un impuesto, una propina. Esta lección, primera del Tema 6, da el paso siguiente: aplicar un porcentaje <strong>a lo largo del tiempo</strong>. Cada año que el dinero pasa en una cuenta o en un préstamo, se aplica otra vez el mismo porcentaje.")}</p>
<p>{t("Before any formula, look at two familiar situations. In both there is interest, but from opposite sides.", "Antes de ver ninguna fórmula, conviene mirar dos situaciones conocidas. En las dos aparece el interés, pero desde lados opuestos.")}</p>
{tabla(t("Saving and borrowing", "Ahorrar y pedir prestado"), t("Two sides of interest: when you save and when you borrow", "Dos caras del interés: cuando se ahorra y cuando se pide prestado"),
       ["", t("When I save", "Cuando yo ahorro"), t("When I borrow", "Cuando yo pido prestado")],
       [[t("Situation", "Situación"), t("Guadalupe puts $1,500 in a savings account that pays 4% a year.", "Guadalupe deposita $1,500 en una cuenta de ahorro que paga el 4% anual."), t("Ernesto takes out a $3,000 loan at 10% a year for 6 months.", "Ernesto pide un préstamo de $3,000 al 10% anual por 6 meses.")],
        [t("One year", "Un año"), t("4% of $1,500 = $60", "El 4% de $1,500 = $60"), t("10% of $3,000 = $300", "El 10% de $3,000 = $300")],
        [t("The whole time", "Todo el plazo"), t("3 years: 60 + 60 + 60 = <strong>$180</strong>", "3 años: 60 + 60 + 60 = <strong>$180</strong>"), t("Half a year: half of $300 = <strong>$150</strong>", "Medio año: la mitad de $300 = <strong>$150</strong>")],
        [t("Who pays?", "¿Quién paga?"), t("The bank pays me for using my money.", "El banco me paga por usar mi dinero."), t("I pay the bank for using its money.", "Yo le pago al banco por usar su dinero.")]])}
{caja("tip", t("The key idea", "Idea esencial"), t("<p>You just figured simple interest without a formula. First you found the percent of the starting money for <strong>one year</strong>; then you multiplied by the <strong>number of years</strong>. The formula in section 3 just writes this idea with letters.</p>", "<p>Sin fórmula, ya se calculó interés simple. Primero se halló el porcentaje del dinero inicial para <strong>un año</strong>; después se multiplicó por el <strong>número de años</strong>. La fórmula de la sección 3 solo escribe esta idea con letras.</p>"))}'''

    s2 = f'''<p>{t("Every simple-interest problem uses five quantities. The letters are the same as on the GED formula sheet.", "Toda situación de interés simple gira en torno a cinco cantidades. Las letras son las mismas que aparecen en la hoja de fórmulas del examen GED.")}</p>
{tabla(t("The five quantities", "Las cinco cantidades"), t("The five quantities of simple interest", "Las cinco cantidades del interés simple"),
       [t("Letter", "Letra"), t("Name", "Nombre"), t("What it is", "Qué es")],
       [["P", t("principal", "principal o capital"), t("the starting money you deposit or borrow", "el dinero inicial que se deposita o se presta")],
        ["r", t("interest rate", "tasa de interés"), t("the percent charged or paid each period, almost always per year; in the formula it goes as a decimal", "el porcentaje que se cobra o se paga por cada período, casi siempre por año; en la fórmula va en decimal")],
        ["t", t("time", "tiempo o plazo"), t("how long the saving or the loan lasts, in the same unit as the rate (usually years)", "cuánto dura el ahorro o el préstamo, en la misma unidad que la tasa (normalmente, años)")],
        ["I", t("interest", "interés"), t("the extra money: a gain on savings, a cost on a loan", "el dinero adicional: una ganancia en un ahorro, un costo en un préstamo")],
        ["A", t("total amount", "monto total"), t("principal plus interest: what you take out at the end, or what you pay back in all", "el principal más el interés: lo que se retira al final, o lo que se devuelve en total")]])}
{tabla(t("The same words in both languages", "Las mismas palabras en los dos idiomas"), t("Money words in English and in Spanish", "Términos financieros en inglés y en español"),
       [t("English", "Inglés"), t("Spanish", "Español")],
       [["principal", "principal o capital"], ["simple interest", "interés simple"], ["annual interest rate", "tasa de interés anual"], ["term", "plazo"], ["total amount", "monto total"], [t("loan / savings account", "loan / savings account"), t("préstamo / cuenta de ahorro", "préstamo / cuenta de ahorro")]])}
{enlace(n, t("vocabulary", "vocabulario"), t("money vocabulary", "vocabulario financiero"), t("Review principal, rate, time, interest, and total amount.", "Repase qué son el capital, la tasa, el tiempo, el interés y el monto."))}'''

    s3 = f'''{big("I = P × r × t")}
<p style="text-align:center">{t("I = interest · P = principal · r = yearly rate as a decimal · t = time in years", "I = interés · P = principal · r = tasa anual en decimal · t = tiempo en años")}</p>
{big("A = P + I")}
<p style="text-align:center">{t("The total amount is the principal plus the interest.", "El monto total es el principal más el interés.")}</p>
{ej(t("Example: find the interest", "Ejemplo: calcular el interés"), t("How much interest do $3,500 earn at 4% simple interest a year for 6 years?", "¿Cuánto interés genera un ahorro de $3,500 al 4% de interés simple anual durante 6 años?"),
  [("1", t("Data.", "Datos."), "P = 3,500; r = 4% = 0.04; t = 6."),
   ("2", t("Formula.", "Fórmula."), "I = 3,500 × 0.04 × 6."),
   ("3", t("In parts.", "Por partes."), t("3,500 × 0.04 = 140 (one year's interest); 140 × 6 = 840.", "3,500 × 0.04 = 140 (interés de un año); 140 × 6 = 840.")),
   ("✓", t("Answer.", "Respuesta."), t("The interest is <strong>$840</strong>.", "El interés es de <strong>$840</strong>."))])}
{ej(t("Example: total amount of a savings account", "Ejemplo: monto total de un ahorro"), t("With the same data, how much money is in the account at the end of the 6 years?", "Con los mismos datos, ¿cuánto dinero hay en la cuenta al final de los 6 años?"),
  [("1", "A = P + I.", "A = 3,500 + 840 = 4,340."),
   ("✓", t("Answer.", "Respuesta."), "<strong>$4,340</strong>")])}
{ej(t("Example: total amount of a loan", "Ejemplo: monto total de un préstamo"), t("A $1,800 loan has 12% simple interest a year and is paid back in 2 years. How much is paid back in all?", "Un préstamo de $1,800 tiene un interés simple del 12% anual y se paga en 2 años. ¿Cuánto se devuelve en total?"),
  [("1", t("Interest.", "Interés."), "I = 1,800 × 0.12 × 2 = 432."),
   ("2", t("Total.", "Total."), "A = 1,800 + 432 = 2,232."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$2,232</strong>. The loan costs $432.", "<strong>$2,232</strong>. El préstamo cuesta $432."))])}
{calc(t("Simple interest on the calculator", "El interés simple en la calculadora"), t(f"<p>Type {T('3500')} {T('×')} {T('0.04')} {T('×')} {T('6')} {T('enter')}. The screen shows 840. Then {T('+')} {T('3500')} {T('enter')} gives the total amount, 4,340.</p>", f"<p>Escriba {T('3500')} {T('×')} {T('0.04')} {T('×')} {T('6')} {T('enter')}. La pantalla muestra 840. Después, {T('+')} {T('3500')} {T('enter')} da el monto total, 4,340.</p>"))}
{practica("p1", t("Practice 1 — Interest", "Práctica 1 — El interés"), t("P = $500, r = 6% a year, t = 2 years. How much is the interest?", "P = $500, r = 6% anual, t = 2 años. ¿Cuánto es el interés?"),
          [("a", "$60"), ("b", "$6,000"), ("c", "$30"), ("d", "$560")])}
{practica("p2", t("Practice 2 — Total amount", "Práctica 2 — El monto total"), t("P = $800, r = 3% a year, t = 4 years. What is the total amount A?", "P = $800, r = 3% anual, t = 4 años. ¿Cuál es el monto total A?"),
          [("a", "$96"), ("b", "$896"), ("c", "$824"), ("d", "$10,400")])}
{enlace(n, t("simple-interest", "interes-simple"), t("the simple-interest formula", "la fórmula del interés simple"), t("Use the interest calculator and practice with the rate as a decimal.", "Use la calculadora de interés y practique con la tasa en decimal."))}'''

    s4 = f'''<p>{t("The formula only works if the rate is a <strong>decimal</strong> and the rate and the time use <strong>the same unit</strong>. If the rate is per year, the time must be in years. This is where most mistakes happen.", "La fórmula solo funciona si la tasa está en <strong>decimal</strong> y si la tasa y el tiempo usan <strong>la misma unidad</strong>. Si la tasa es anual, el tiempo debe estar en años. Esta es la parte donde ocurren más errores.")}</p>
<p>{t("<strong>Percent to decimal:</strong> divide by 100 (move the point two places to the left): 3% = 0.03 · 4.5% = 0.045 · 12% = 0.12 · 0.5% = 0.005.", "<strong>De porcentaje a decimal:</strong> se divide entre 100 (el punto se corre dos lugares a la izquierda): 3% = 0.03 · 4.5% = 0.045 · 12% = 0.12 · 0.5% = 0.005.")}</p>
{tabla(t("Months to years", "De meses a años"), t("Time in months changed to years (divide by 12)", "El tiempo en meses pasado a años (se divide entre 12)"),
       [t("Months", "Meses"), "3", "6", "9", "18", "30"], [[t("Years", "Años"), "0.25", "0.5", "0.75", "1.5", "2.5"]])}
{tabla(t("Monthly rate to yearly rate", "De tasa mensual a tasa anual"), t("A monthly rate changed to a yearly rate (multiply by 12)", "La tasa mensual pasada a tasa anual (se multiplica por 12)"),
       [t("Monthly rate", "Tasa mensual"), "0.5%", "1%", "1.5%", "2%", "2.5%"], [[t("Yearly rate", "Tasa anual"), "6%", "12%", "18%", "24%", "30%"]])}
<p>{t("When the time is in <strong>days</strong>, divide by 365. Some banks use a “banker's year” of 360 days; the problem must say which one to use.", "Cuando el tiempo viene en <strong>días</strong>, se divide entre 365. Algunos bancos usan el año comercial de 360 días; el problema debe indicar cuál se usa.")}</p>
{ej(t("Example: time in months", "Ejemplo: tiempo en meses"), t("A $4,000 loan at 6% a year is paid back in 9 months. How much interest is paid?", "Un préstamo de $4,000 al 6% anual se paga en 9 meses. ¿Cuánto interés se paga?"),
  [("1", t("Change the time.", "Convierta el tiempo."), t("9 ÷ 12 = 0.75 years.", "9 ÷ 12 = 0.75 años.")),
   ("2", t("Formula.", "Fórmula."), "I = 4,000 × 0.06 × 0.75 = 180."),
   ("✓", t("Answer.", "Respuesta."), "<strong>$180</strong>")])}
{caja("ojo", t("Common mistake", "Error frecuente"), t("<p>Using t = 9 without changing it gives I = 4,000 × 0.06 × 9 = $2,160: more than half the loan in only 9 months. Before you answer, ask yourself whether the result makes sense.</p>", "<p>Usar t = 9 sin convertir da I = 4,000 × 0.06 × 9 = $2,160: más de la mitad del préstamo en solo 9 meses. Antes de dar una respuesta, pregúntese si el resultado tiene sentido.</p>"))}
{ej(t("Example: a monthly rate", "Ejemplo: tasa mensual"), t("A store finances a $1,200 purchase at 2% a month for 6 months. How much interest is paid?", "Una tienda financia una compra de $1,200 al 2% mensual durante 6 meses. ¿Cuánto interés se paga?"),
  [("A", t("Way A.", "Camino A."), t("The rate is monthly and the time is in months: they already match. I = 1,200 × 0.02 × 6 = 144.", "La tasa es mensual y el tiempo está en meses: ya coinciden. I = 1,200 × 0.02 × 6 = 144.")),
   ("B", t("Way B.", "Camino B."), t("Yearly rate = 2% × 12 = 24%; time = 6 ÷ 12 = 0.5 years. I = 1,200 × 0.24 × 0.5 = 144.", "Tasa anual = 2% × 12 = 24%; tiempo = 6 ÷ 12 = 0.5 años. I = 1,200 × 0.24 × 0.5 = 144.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$144</strong> either way. What matters is that the rate and the time match.", "<strong>$144</strong> por cualquiera de los dos caminos. Lo importante es que la tasa y el tiempo coincidan."))])}
{practica("p3", t("Practice 3 — Time in months", "Práctica 3 — Tiempo en meses"), t("P = $3,000, r = 5% a year, t = 8 months. How much is the interest?", "P = $3,000, r = 5% anual, t = 8 meses. ¿Cuánto es el interés?"),
          [("a", "$1,200"), ("b", "$150"), ("c", "$100"), ("d", "$120")])}
{enlace(n, t("same-unit", "misma-unidad"), t("the rate and the time in the same unit", "la tasa y el tiempo, en la misma unidad"), t("Change months and days to years, or see when they already match, before you calculate.", "Convierta meses y días a años, o reconozca cuándo ya coinciden, antes de calcular."))}'''

    s5 = f'''<p>{t("With <strong>simple</strong> interest, each year's interest is <strong>always the same</strong>, because it is figured on the original principal. That is why the money grows in equal steps: <strong>linear</strong> growth.", "En el interés <strong>simple</strong>, el interés de cada año es <strong>siempre el mismo</strong>, porque se calcula sobre el principal original. Por eso el dinero crece en escalones iguales: un crecimiento <strong>lineal</strong>.")}</p>
{tabla(t("$1,000 at 8%", "$1,000 al 8%"), t("A $1,000 principal at 8% simple interest a year", "Principal de $1,000 al 8% de interés simple anual"),
       [t("Year", "Año"), t("Interest that year ($)", "Interés del año ($)"), t("Interest so far ($)", "Interés acumulado ($)"), t("Total amount ($)", "Monto total ($)")],
       [["0", "—", "0", "1,000"], ["1", "80", "80", "1,080"], ["2", "80", "160", "1,160"], ["3", "80", "240", "1,240"], ["5", "80", "400", "1,400"], ["10", "80", "800", "1,800"]])}
<div style="text-align:center">{escalera()}</div>
<p>{t("The dark part (the principal) does not change. The light part (the interest so far) grows $80 every year.", "La parte oscura (el principal) no cambia. La parte clara (el interés acumulado) crece $80 cada año.")}</p>
{caja("tip", t("To learn more", "Para saber más"), t("<p>With <strong>compound</strong> interest, each year's interest is figured on the amount from the year before, and money grows faster. At this level you study only simple interest.</p>", "<p>En el interés <strong>compuesto</strong>, cada año el interés se calcula sobre el monto del año anterior, y el dinero crece más rápido. En este nivel se estudia solo el interés simple.</p>"))}
{practica("p4", t("Practice 4 — Year 5", "Práctica 4 — El año 5"), t("$1,000 at 8% simple interest a year. How much interest does it earn in year 5 alone?", "$1,000 al 8% de interés simple anual. ¿Cuánto interés gana solo en el año 5?"),
          [("a", "$400"), ("b", "$80"), ("c", "$1,400"), ("d", "$86")])}
{enlace(n, t("year-by-year", "ano-a-ano"), t("growth year by year", "crecimiento año tras año"), t("Move the principal and the rate and see the staircase of equal steps.", "Mueva el capital y la tasa y vea la escalera de escalones iguales."))}'''

    s6 = f'''<p>{t("Sometimes what you do not know is not the interest but another value: how much to deposit, what rate a loan charges, or how long to wait. With I = P × r × t you can find any of the four quantities if you know the other three.", "A veces lo que se desconoce no es el interés, sino otro dato: ¿cuánto hay que depositar?, ¿qué tasa cobra el préstamo?, ¿cuánto tiempo hay que esperar? Con I = P × r × t se puede hallar cualquiera de las cuatro cantidades si se conocen las otras tres.")}</p>
{tabla(t("Solving for P, r, or t", "Despejar P, r o t"), t("The formula solved for each quantity", "La fórmula despejada para cada cantidad"),
       [t("You want", "Se busca"), t("Formula", "Fórmula")],
       [[t("the principal", "el principal"), "P = I ÷ (r × t)"], [t("the rate", "la tasa"), t("r = I ÷ (P × t), then × 100 for the percent", "r = I ÷ (P × t), y × 100 para el porcentaje")], [t("the time", "el tiempo"), "t = I ÷ (P × r)"]])}
{caja("tip", t("One rule for all three", "Una sola regla para las tres"), t("<p>Divide the interest by the product of the other two values. If the problem gives the total amount A instead of the interest, first find I = A − P.</p>", "<p>Se divide el interés entre el producto de los otros dos datos. Si el problema da el monto total A en lugar del interés, primero se calcula I = A − P.</p>"))}
{ej(t("Example: find the rate", "Ejemplo: buscar la tasa"), t("A $2,000 loan for 4 years cost $560 in interest. What yearly rate was charged?", "Un préstamo de $2,000 a 4 años generó $560 de interés. ¿Qué tasa anual se cobró?"),
  [("1", "r = I ÷ (P × t).", "560 ÷ (2,000 × 4) = 560 ÷ 8,000 = 0.07."),
   ("✓", t("To a percent.", "A porcentaje."), t("0.07 × 100 = <strong>7% a year</strong>.", "0.07 × 100 = <strong>7% anual</strong>."))])}
{ej(t("Example: find the time", "Ejemplo: buscar el tiempo"), t("How long must $1,200 stay at 5% a year to earn $150 in interest?", "¿Cuánto tiempo deben estar $1,200 al 5% anual para ganar $150 de interés?"),
  [("1", "t = I ÷ (P × r).", "150 ÷ (1,200 × 0.05) = 150 ÷ 60 = 2.5."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>2.5 years</strong>, that is, 2 years and 6 months.", "<strong>2.5 años</strong>, es decir, 2 años y 6 meses."))])}
{ej(t("Example: find the principal", "Ejemplo: buscar el principal"), t("How much must you deposit at 4% a year to earn $360 in 3 years?", "¿Cuánto hay que depositar al 4% anual para ganar $360 en 3 años?"),
  [("1", "P = I ÷ (r × t).", "360 ÷ (0.04 × 3) = 360 ÷ 0.12 = 3,000."),
   ("2", t("Check.", "Compruebe."), "3,000 × 0.04 × 3 = 360. ✓"),
   ("✓", t("Answer.", "Respuesta."), "<strong>$3,000</strong>")])}
{ej(t("Example: when you are given the total amount", "Ejemplo: cuando el dato es el monto total"), t("For a $4,000 loan, $4,960 was paid back in all after 2 years. What yearly rate was charged?", "Por un préstamo de $4,000 se devolvieron $4,960 en total al cabo de 2 años. ¿Qué tasa anual se cobró?"),
  [("1", t("First the interest.", "Primero el interés."), "I = A − P = 4,960 − 4,000 = 960."),
   ("2", "r = I ÷ (P × t).", "960 ÷ (4,000 × 2) = 960 ÷ 8,000 = 0.12."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>12% a year</strong>", "<strong>12% anual</strong>"))])}
{practica("p5", t("Practice 5 — Find the principal", "Práctica 5 — Halle el principal"), t("A savings account at 4% a year earned $96 in 3 years. What is P?", "Un ahorro al 4% anual ganó $96 en 3 años. ¿Cuánto es P?"),
          [("a", "$11.52"), ("b", "$2,400"), ("c", "$800"), ("d", "$8")])}
{practica("p6", t("Practice 6 — Find the rate", "Práctica 6 — Halle la tasa"), t("A $2,500 loan for 2 years cost $275 in interest. What is the yearly rate?", "Un préstamo de $2,500 a 2 años generó $275 de interés. ¿Cuál es la tasa anual?"),
          [("a", "11%"), ("b", "5.5%"), ("c", "0.055%"), ("d", "18.2%")])}
{practica("p7", t("Practice 7 — Find the time", "Práctica 7 — Halle el tiempo"), t("$1,600 at 5% a year earned $200 in interest. How long was it?", "$1,600 al 5% anual ganaron $200 de interés. ¿Cuánto tiempo fue?"),
          [("a", t("2.5 years", "2.5 años")), ("b", t("40 years", "40 años")), ("c", t("0.4 years", "0.4 años")), ("d", t("25 years", "25 años"))])}
{enlace(n, t("solve-for", "despejar"), t("solving for the principal, the rate, or the time", "despejar el capital, la tasa o el tiempo"), t("Choose which value is missing and practice the three ways to solve, even from the total amount.", "Elija qué dato falta y practique los tres despejes, incluso a partir del monto total."))}'''

    secciones = [("s-" + t("two-sides", "dos-caras"), t("The bank and me: two sides of interest", "El banco y yo: dos caras del interés"), s1),
                 ("s-" + t("vocabulary", "vocabulario"), t("Money vocabulary", "Vocabulario financiero"), s2),
                 ("s-" + t("formula", "formula"), t("The simple-interest formula", "La fórmula del interés simple"), s3),
                 ("s-" + t("same-unit", "misma-unidad"), t("The rate and the time in the same unit", "La tasa y el tiempo, en la misma unidad"), s4),
                 ("s-" + t("year-by-year", "ano-a-ano"), t("Growth year by year", "Crecimiento año tras año"), s5),
                 ("s-" + t("solve-for", "despejar"), t("Solving for P, r, or t", "Despejar P, r o t"), s6)]

    lesson = {"next": t("Lesson 6.2", "Lección 6.2"), "review": t("sections 3, 4, and 6", "las secciones 3, 4 y 6"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("The rate goes in as a decimal: 6% = 0.06.", "La tasa va en decimal: 6% = 0.06."), "c": t("$30 is one year. Multiply by 2 years.", "$30 es un año. Multiplique por 2 años."), "d": t("That is the total amount. Only the interest is asked.", "Ese es el monto total. Se pide solo el interés.")},
             "right": t("500 × 0.06 × 2 = $60.", "500 × 0.06 × 2 = $60."), "solution": t("I = 500 × 0.06 × 2 = 60.", "I = 500 × 0.06 × 2 = 60.")},
      "p2": {"ok": "b", "hints": {"a": t("$96 is the interest. Add the principal.", "$96 es el interés. Sume el principal."), "c": t("$24 is one year's interest. Multiply by 4.", "$24 es el interés de un año. Multiplique por 4."), "d": t("The rate goes in as a decimal: 3% = 0.03.", "La tasa va en decimal: 3% = 0.03.")},
             "right": t("I = 96; A = 800 + 96 = $896.", "I = 96; A = 800 + 96 = $896."), "solution": t("I = 800 × 0.03 × 4 = 96; A = 800 + 96 = 896.", "I = 800 × 0.03 × 4 = 96; A = 800 + 96 = 896.")},
      "p3": {"ok": "c", "hints": {"a": t("You used 8 years. 8 months = 8 ÷ 12 of a year.", "Usó 8 años. 8 meses = 8 ÷ 12 de año."), "b": t("$150 is one full year.", "$150 es un año completo."), "d": t("Check: 150 × 8 ÷ 12.", "Revise: 150 × 8 ÷ 12.")},
             "right": t("3,000 × 0.05 × 8/12 = $100.", "3,000 × 0.05 × 8/12 = $100."), "solution": t("t = 8 ÷ 12 of a year. I = 3,000 × 0.05 × 8/12 = 150 × 8/12 = 100.", "t = 8 ÷ 12 de año. I = 3,000 × 0.05 × 8/12 = 150 × 8/12 = 100.")},
      "p4": {"ok": "b", "hints": {"a": t("$400 is the interest so far after 5 years.", "$400 es el interés acumulado en 5 años."), "c": t("$1,400 is the total amount after 5 years.", "$1,400 es el monto total a los 5 años."), "d": t("With simple interest, every year's interest is the same.", "En el interés simple, el interés de cada año es el mismo.")},
             "right": t("Every year: 1,000 × 0.08 = $80.", "Cada año: 1,000 × 0.08 = $80."), "solution": t("Simple interest is figured on the original principal: 1,000 × 0.08 = $80 every year.", "El interés simple se calcula sobre el principal original: 1,000 × 0.08 = $80 cada año.")},
      "p5": {"ok": "c", "hints": {"a": t("You multiplied. P = I ÷ (r × t).", "Multiplicó. P = I ÷ (r × t)."), "b": t("Check: 0.04 × 3 = 0.12, and 96 ÷ 0.12.", "Revise: 0.04 × 3 = 0.12, y 96 ÷ 0.12."), "d": t("You divided 96 by 12. Use the rate as a decimal: 0.12.", "Dividió 96 entre 12. Use la tasa en decimal: 0.12.")},
             "right": t("96 ÷ 0.12 = $800.", "96 ÷ 0.12 = $800."), "solution": t("P = 96 ÷ (0.04 × 3) = 96 ÷ 0.12 = 800.", "P = 96 ÷ (0.04 × 3) = 96 ÷ 0.12 = 800.")},
      "p6": {"ok": "b", "hints": {"a": t("That is for 2 years together. Divide by the time too.", "Eso es de los 2 años juntos. Divida también entre el tiempo."), "c": t("0.055 is the decimal. Multiply by 100.", "0.055 es el decimal. Multiplique por 100."), "d": t("Check: 275 ÷ (2,500 × 2).", "Revise: 275 ÷ (2,500 × 2).")},
             "right": t("275 ÷ 5,000 = 0.055 = 5.5%.", "275 ÷ 5,000 = 0.055 = 5.5%."), "solution": t("r = 275 ÷ (2,500 × 2) = 275 ÷ 5,000 = 0.055 → 5.5% a year.", "r = 275 ÷ (2,500 × 2) = 275 ÷ 5,000 = 0.055 → 5.5% anual.")},
      "p7": {"ok": "a", "hints": {"b": t("You used 5 instead of 0.05.", "Usó 5 en lugar de 0.05."), "c": t("You divided the wrong way: 80 ÷ 200.", "Dividió al revés: 80 ÷ 200."), "d": t("Check the decimal point: 200 ÷ 80.", "Revise el punto decimal: 200 ÷ 80.")},
             "right": t("200 ÷ (1,600 × 0.05) = 200 ÷ 80 = 2.5 years.", "200 ÷ (1,600 × 0.05) = 200 ÷ 80 = 2.5 años."), "solution": t("t = 200 ÷ (1,600 × 0.05) = 200 ÷ 80 = 2.5 years.", "t = 200 ÷ (1,600 × 0.05) = 200 ÷ 80 = 2.5 años.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("In the formula the rate is a decimal.", "En la fórmula la tasa va en decimal."), "b": t("0.45 is 45%.", "0.45 es 45%."), "d": t("Divide by 100.", "Divida entre 100.")}, "solution": t("4.5 ÷ 100 = 0.045.", "4.5 ÷ 100 = 0.045.")},
      "B": {"ok": "d", "hints": {"a": t("Change months to years.", "Pase los meses a años."), "b": t("Divide by 12, not by 10.", "Divida entre 12, no entre 10."), "c": t("Check: 18 ÷ 12.", "Revise: 18 ÷ 12.")}, "solution": t("18 ÷ 12 = 1.5 years.", "18 ÷ 12 = 1.5 años.")},
      "C": {"ok": "a", "hints": {"b": t("$140 is one year.", "$140 es un año."), "c": t("The rate goes in as a decimal.", "La tasa va en decimal."), "d": t("That is the total amount.", "Ese es el monto total.")}, "solution": t("3,500 × 0.04 × 6 = $840.", "3,500 × 0.04 × 6 = $840.")},
      "D": {"ok": "b", "hints": {"a": t("$432 is the interest. Add the loan.", "$432 es el interés. Sume el préstamo."), "c": t("That is only one year of interest.", "Eso es solo un año de interés."), "d": t("Check the interest: 1,800 × 0.12 × 2.", "Revise el interés: 1,800 × 0.12 × 2.")}, "solution": t("I = 432; A = 1,800 + 432 = $2,232.", "I = 432; A = 1,800 + 432 = $2,232.")},
      "E": {"ok": "c", "hints": {"a": t("You used 9 years.", "Usó 9 años."), "b": t("$240 is one full year.", "$240 es un año completo."), "d": t("Check: 240 × 0.75.", "Revise: 240 × 0.75.")}, "solution": t("4,000 × 0.06 × 0.75 = $180.", "4,000 × 0.06 × 0.75 = $180.")},
      "F": {"ok": "b", "hints": {"a": t("$400 is 5 years together.", "$400 son los 5 años juntos."), "c": t("$1,400 is the total amount.", "$1,400 es el monto total."), "d": t("Simple interest does not grow from year to year.", "El interés simple no crece de un año a otro.")}, "solution": t("Every year: 1,000 × 0.08 = $80.", "Cada año: 1,000 × 0.08 = $80.")},
      "G": {"ok": "d", "hints": {"a": t("0.07 is the decimal. Multiply by 100.", "0.07 es el decimal. Multiplique por 100."), "b": t("That is for the 4 years together.", "Eso es de los 4 años juntos."), "c": t("Check: 2,000 × 4 = 8,000.", "Revise: 2,000 × 4 = 8,000.")}, "solution": t("560 ÷ 8,000 = 0.07 = 7%.", "560 ÷ 8,000 = 0.07 = 7%.")},
      "H": {"ok": "a", "hints": {"b": t("You used the total amount as the interest. First I = A − P.", "Usó el monto total como interés. Primero I = A − P."), "c": t("That is for the 2 years together.", "Eso es de los 2 años juntos."), "d": t("Check: 960 ÷ 8,000.", "Revise: 960 ÷ 8,000.")}, "solution": t("I = 960; r = 960 ÷ 8,000 = 0.12 = 12%.", "I = 960; r = 960 ÷ 8,000 = 0.12 = 12%.")}
     }}

    quiz = [
     ("A", t("A rate of 4.5% goes into the formula as:", "Una tasa del 4.5% entra en la fórmula como:"), [("a", "4.5"), ("b", "0.45"), ("c", "0.045"), ("d", "45")]),
     ("B", t("18 months, in years, is:", "18 meses, en años, son:"), [("a", "18"), ("b", "1.8"), ("c", "0.18"), ("d", "1.5")]),
     ("C", t("How much interest do $3,500 earn at 4% a year for 6 years?", "¿Cuánto interés generan $3,500 al 4% anual durante 6 años?"), [("a", "$840"), ("b", "$140"), ("c", "$84,000"), ("d", "$4,340")]),
     ("D", t("A $1,800 loan at 12% a year is paid in 2 years. How much is paid back in all?", "Un préstamo de $1,800 al 12% anual se paga en 2 años. ¿Cuánto se devuelve en total?"), [("a", "$432"), ("b", "$2,232"), ("c", "$2,016"), ("d", "$1,843.20")]),
     ("E", t("A $4,000 loan at 6% a year for 9 months. How much is the interest?", "Un préstamo de $4,000 al 6% anual por 9 meses. ¿Cuánto es el interés?"), [("a", "$2,160"), ("b", "$240"), ("c", "$180"), ("d", "$18")]),
     ("F", t("$1,000 at 8% simple interest a year. How much interest does it earn in year 5 alone?", "$1,000 al 8% de interés simple anual. ¿Cuánto interés gana solo en el año 5?"), [("a", "$400"), ("b", "$80"), ("c", "$1,400"), ("d", "$86")]),
     ("G", t("A $2,000 loan for 4 years cost $560 in interest. What is the yearly rate?", "Un préstamo de $2,000 a 4 años generó $560 de interés. ¿Cuál es la tasa anual?"), [("a", "0.07%"), ("b", "28%"), ("c", "14%"), ("d", "7%")]),
     ("H", t("For a $4,000 loan, $4,960 was paid back in all after 2 years. What is the yearly rate?", "Por un préstamo de $4,000 se devolvieron $4,960 en total en 2 años. ¿Cuál es la tasa anual?"), [("a", "12%"), ("b", "62%"), ("c", "24%"), ("d", "6%")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Percents over time: interest on savings and loans with I = P × r × t, the total amount, matching the rate and the time, and solving for any value.", "El porcentaje a lo largo del tiempo: el interés de ahorros y préstamos con I = P × r × t, el monto total, la tasa y el tiempo en la misma unidad, y cómo despejar cualquier dato."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Name</strong> the five quantities: P, r, t, I, and A.", "<strong>Identificar</strong> las cinco cantidades: P, r, t, I y A."),
         t("<strong>Find</strong> the interest with I = P × r × t and the total amount with A = P + I.", "<strong>Calcular</strong> el interés con I = P × r × t y el monto total con A = P + I."),
         t("<strong>Change</strong> the rate to a decimal and the time to the same unit as the rate.", "<strong>Convertir</strong> la tasa a decimal y el tiempo a la misma unidad que la tasa."),
         t("<strong>Describe</strong> simple interest as growth in equal steps.", "<strong>Describir</strong> el interés simple como un crecimiento en escalones iguales."),
         t("<strong>Solve</strong> for the principal, the rate, or the time.", "<strong>Despejar</strong> el principal, la tasa o el tiempo.")],
        secciones,
        (t("Find the interest I in four problems (two with the time in months). Find the total amount A = P + I in three problems, with savings and with loans. Solve three problems for the principal, the rate, or the time.",
           "Calcule el interés I en cuatro ejercicios (dos con el tiempo en meses). Calcule el monto total A = P + I en tres ejercicios, con ahorros y con préstamos. Resuelva tres ejercicios en que haya que despejar el principal, la tasa o el tiempo."),
         t("Look at a real offer: a savings account, a store financing plan, or a loan ad. Write down P, r, and t, check whether the rate and the time use the same unit, and find the interest.",
           "Busque una oferta real: una cuenta de ahorro, un plan de financiamiento de una tienda o un anuncio de préstamo. Anote P, r y t, compruebe si la tasa y el tiempo usan la misma unidad y calcule el interés.")),
        quiz,
        t("Self-check checklist for simple interest", "Lista de autoevaluación de interés simple"),
        t("Self-check checklist: skills for simple interest", "Lista de autoevaluación: destrezas de interés simple"),
        [(t("Change the rate and the time", "Convertir la tasa y el tiempo"), t("I change the rate to a decimal and the time to years, and I know when there is no need to (monthly rate with time in months).", "Paso la tasa a decimal y el tiempo a años, y sé cuándo no hace falta (tasa mensual con tiempo en meses)."), t("I change the rate but make mistakes with the time, or the other way around.", "Convierto la tasa, pero me equivoco con el tiempo, o al revés."), t("I use the percent as is, or leave the time in months.", "Uso el porcentaje sin convertir o dejo el tiempo en meses.")),
         (t("Use I = P × r × t", "Aplicar I = P × r × t"), t("I find the interest and the total amount and check them with an estimate.", "Calculo el interés y el monto total y los compruebo con una estimación."), t("I find the interest, but make mistakes with the total amount.", "Calculo el interés, pero me equivoco con el monto total."), t("I mix up the letters.", "Confundo las variables.")),
         (t("Solve for the missing value", "Despejar el dato que falta"), t("I solve for P, r, or t, give the unit, and check; I also start from A.", "Despejo P, r o t, doy la unidad y compruebo; también parto de A."), t("I solve with help; I forget the units.", "Despejo con apoyo; olvido las unidades."), t("I do not know which value I am looking for.", "No identifico qué dato se busca."))],
        t("<p>Simple interest is a percent of the principal that repeats every year: that is why the money grows in <strong>equal amounts</strong>. With one formula, I = P × r × t, you can find the interest, the total amount, or any missing value.</p>\n<p>In <strong>Lesson 6.2 · Depreciation and other money applications</strong> you will study the opposite process: things like a car, a computer, or a work tool, which lose the same amount of value every year. That loss is called <strong>straight-line depreciation</strong>.</p>",
          "<p>El interés simple es un porcentaje del principal que se repite cada año: por eso el dinero crece en <strong>cantidades iguales</strong>. Con una sola fórmula, I = P × r × t, se calcula el interés, el monto total o cualquier dato que falte.</p>\n<p>En la <strong>Lección 6.2 · Depreciación y otras aplicaciones financieras</strong> estudiará el proceso contrario: bienes como un carro, una computadora o una herramienta de trabajo, que pierden una cantidad igual de valor cada año. Esa pérdida se llama <strong>depreciación lineal</strong>.</p>"),
        ("6-2", ("", t("Lesson 6.2 · Depreciation and other money applications", "Lección 6.2 · Depreciación y otras aplicaciones financieras"))),
        [(t("principal (P)", "principal (P)"), t("The starting money you deposit or borrow.", "El dinero inicial que se deposita o se presta.")),
         (t("simple interest", "interés simple"), t("Interest figured only on the principal: the same amount every year.", "Interés que se calcula solo sobre el principal: la misma cantidad cada año.")),
         (t("rate (r)", "tasa (r)"), t("The percent per period, written as a decimal in the formula.", "El porcentaje por período, escrito en decimal en la fórmula.")),
         (t("total amount (A)", "monto total (A)"), t("Principal plus interest: A = P + I.", "Principal más interés: A = P + I."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "nombres": ["Pedro", "María", "Luis", "Ana", "Rosa", "Jorge"], "sit": [["deposits", "in an account that pays"], ["borrows", "from a bank that charges"]],
  "enun": "{n} {v} {P} {s} {r} simple interest a year for {m} months.", "queRep": " What does {x} stand for?", "letras": ["Principal (P)", "Rate (r)", "Time (t)", "Interest (I)"],
  "esP": "It is the starting money: the principal.", "esR": "It is the yearly percent: the rate.",
  "queT": " What value of t goes into the formula?", "tAnos": "Time goes in years, not months: divide by 12.", "tSol": "{m} ÷ 12 = {t} years.",
  "queR": " What value of r goes into the formula?", "rDec": "The rate goes in as a decimal: divide by 100.", "rSol": "{p} = {d}.",
  "datos": "Data: P = {P}, r = {p} = {r}, t = {t}.", "unAno": "One year's interest: {P2} × {r} = {a}. In {t} {y}: {a} × {t} = <strong>{I}</strong>.", "ano": ["year", "years"],
  "resIS": "I = {I} · A = {P} + {I} = {A}",
  "isQ": "P = {P}, r = {p}, t = {t} {y}. How much is {x}?", "elI": "the interest I", "elA": "the total amount A",
  "isS": "I = {P} × {r} × {t} = {I}", "isS2": "; A = {P} + {I} = {A}",
  "isD": "The rate goes in as a decimal: {p} is {r}.", "isA": "That is the interest. The total amount is the principal plus the interest.", "isI": "That is the total amount. Only the interest is asked.", "isT": "You still need to multiply by the time.",
  "aaVoz": "Bars for the total amount each year: it grows {a} every year.", "aaCap": "A principal of {P} at {r} simple interest (the dark part of each bar is the principal)",
  "aaCab": ["Year", "Interest that year", "Interest so far", "Total amount"], "anoW": "Year",
  "aa1": "A principal of {P} earns {r} simple interest a year. How much interest does it earn in year {k}?",
  "aa2": "A principal of {P} at {r} simple interest a year. How much interest has built up by the end of year {k}?",
  "aa3": "A principal of {P} at {r} simple interest a year. What is the total amount at the end of year {k}?",
  "aaS": "Each year it earns {P2} × {d} = {a}. ", "aaS1": "With simple interest it is the same every year.", "aaS2": "{a} × {k} = {x}.", "aaS3": "{P} + {a} × {k} = {x}.",
  "aaP": "That is the interest so far. One year's interest is always the same.",
  "escribe": "Type a number in each box.",
  "coinc": "The rate is monthly and the time is in months: <strong>they already match</strong>, no need to change anything.",
  "aMeses": "The rate is monthly: change the time to months. ", "aAnos": "The rate is yearly: change the time to years. ", "yaAnos": "The rate is yearly and the time is in years: they already match.",
  "anosM": "{t} years × 12 = {m} months.", "diasM": "{t} days ÷ {d} ≈ {m} months.", "mesesA": "{t} months ÷ 12 = {a} years.", "diasA": "{t} days ÷ {d} = {a} years.",
  "tasaDec": "The rate as a decimal: {p} = {d} {u}.", "porMes": "per month", "porAno": "per year",
  "sinConv": "Without changing, you would get {P} × {r} × {t} = {I}: {x}", "grande": "far too large.", "chico": "far too small.",
  "mu1": "A {P} loan at {r} simple interest a year is paid back in {t} months. How much interest is paid?", "mu1s": "{t} months ÷ 12 = {a} years. I = {P2} × {d} × {a} = {I}.", "mu1p": "You used the months as if they were years. Divide the months by 12.",
  "mu2": "A store finances a {P} purchase at {r} <strong>a month</strong> for {t} months. How much interest is paid?", "mu2s": "Monthly rate and time in months: they already match. I = {P2} × {d} × {t} = {I}.", "mu2p": "The rate is monthly and the time is in months: do not divide by 12.",
  "mu3": "A {P} balance has {r} simple interest a year for {t} days. Use the banker's year of 360 days. How much interest is there?", "mu3s": "{t} ÷ 360 = {a} years. I = {P2} × {d} × {a} = {I}.", "mu3p": "Change the days to years: divide by 360.", "mu3q": "The problem says to use the banker's year: divide by 360, not 365.",
  "meses": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  "mu4": "A {P} certificate of deposit opens on {a} 1 and ends on {b} 1 of the same year, at {r} simple interest a year. How much interest does it earn?", "mu4s": "From {a} 1 to {b} 1 is {m} months = {y} years. I = {P2} × {d} × {y} = {I}.", "mu4p": "Count the months and change them to years (÷ 12).", "mu4q": "That is the interest for a whole year; the term is shorter.",
  "buscaP": "principal", "deP": "P = I ÷ (r × t) = {I} ÷ ({r} × {t}) = {I} ÷ {d}", "resP": "P = {x}", "compP": "Check: {x} × {r} × {t} = {I} ✓",
  "deR": "r = I ÷ (P × t) = {I} ÷ ({P} × {t}) = {I} ÷ {d} = {x}", "porCien": "For the percent, multiply by 100.", "resR": "r = {x}% a year",
  "deT": "t = I ÷ (P × r) = {I} ÷ ({P} × {r}) = {I} ÷ {d}", "resT": "t = {x} years", "yMeses": " ({a} years and {m} months)",
  "cero1": "The rate and the time cannot be 0.", "cero2": "The principal and the time cannot be 0.", "cero3": "The principal and the rate cannot be 0.",
  "de1": "How much must you deposit at {r} a year to earn {I} in interest in {t} years?", "de1s": "P = {I2} ÷ ({d} × {t}) = {I2} ÷ {q} = {P}.", "de1p": "You multiplied; to find the principal, divide the interest by (r × t).",
  "de2": "A {P} loan for {t} years cost {I} in interest. What yearly rate was charged (in %)?", "de2s": "r = {I2} ÷ ({P2} × {t}) = {d} → {r}%.", "de2p": "That is the decimal; multiply it by 100 for the percent.",
  "de3": "How many years must {P} stay at {r} a year to earn {I} in interest?", "de3s": "t = {I2} ÷ ({P2} × {d}) = {I2} ÷ {q} = {t} years.", "de3p": "That is in months; years are asked.",
  "de4": "For a {P} loan, {A} was paid back in all after {t} years. What yearly rate was charged (in %)?", "de4s": "First the interest: {A2} − {P2} = {I2}. r = {I2} ÷ ({P2} × {t}) = {d} → {r}%.", "de4p": "You used the total amount as if it were the interest. First subtract: I = A − P."
 },
 "es": {
  "nombres": ["Pedro", "María", "Luis", "Ana", "Rosa", "Jorge"], "sit": [["deposita", "en una cuenta que paga el"], ["pide prestados", "a un banco que cobra el"]],
  "enun": "{n} {v} {P} {s} {r} de interés simple anual durante {m} meses.", "queRep": " ¿Qué representa {x}?", "letras": ["Principal (P)", "Tasa (r)", "Tiempo (t)", "Interés (I)"],
  "esP": "Es el dinero inicial: el principal.", "esR": "Es el porcentaje anual: la tasa.",
  "queT": " ¿Qué valor de t se usa en la fórmula?", "tAnos": "El tiempo va en años, no en meses: se divide entre 12.", "tSol": "{m} ÷ 12 = {t} años.",
  "queR": " ¿Qué valor de r se usa en la fórmula?", "rDec": "La tasa va en decimal: se divide entre 100.", "rSol": "{p} = {d}.",
  "datos": "Datos: P = {P}, r = {p} = {r}, t = {t}.", "unAno": "Interés de un año: {P2} × {r} = {a}. En {t} {y}: {a} × {t} = <strong>{I}</strong>.", "ano": ["año", "años"],
  "resIS": "I = {I} · A = {P} + {I} = {A}",
  "isQ": "P = {P}, r = {p}, t = {t} {y}. ¿Cuánto es {x}?", "elI": "el interés I", "elA": "el monto total A",
  "isS": "I = {P} × {r} × {t} = {I}", "isS2": "; A = {P} + {I} = {A}",
  "isD": "La tasa va en decimal: {p} es {r}.", "isA": "Ese es el interés. El monto total es el principal más el interés.", "isI": "Ese es el monto total. Se pide solo el interés.", "isT": "Falta multiplicar por el tiempo.",
  "aaVoz": "Barras del monto año por año: crece {a} cada año.", "aaCap": "Principal de {P} al {r} de interés simple (la parte oscura de cada barra es el principal)",
  "aaCab": ["Año", "Interés del año", "Interés acumulado", "Monto total"], "anoW": "Año",
  "aa1": "Un principal de {P} gana el {r} de interés simple anual. ¿Cuánto interés gana en el año {k}?",
  "aa2": "Un principal de {P} al {r} de interés simple anual. ¿Cuánto interés se ha acumulado al final del año {k}?",
  "aa3": "Un principal de {P} al {r} de interés simple anual. ¿Cuál es el monto total al final del año {k}?",
  "aaS": "Cada año gana {P2} × {d} = {a}. ", "aaS1": "En interés simple es el mismo todos los años.", "aaS2": "{a} × {k} = {x}.", "aaS3": "{P} + {a} × {k} = {x}.",
  "aaP": "Eso es lo acumulado. El interés de un solo año es siempre el mismo.",
  "escribe": "Escriba un número en cada casilla.",
  "coinc": "La tasa es mensual y el tiempo está en meses: <strong>ya coinciden</strong>, no hace falta convertir.",
  "aMeses": "La tasa es mensual: el tiempo se pasa a meses. ", "aAnos": "La tasa es anual: el tiempo se pasa a años. ", "yaAnos": "La tasa es anual y el tiempo está en años: ya coinciden.",
  "anosM": "{t} años × 12 = {m} meses.", "diasM": "{t} días ÷ {d} ≈ {m} meses.", "mesesA": "{t} meses ÷ 12 = {a} años.", "diasA": "{t} días ÷ {d} = {a} años.",
  "tasaDec": "La tasa en decimal: {p} = {d} {u}.", "porMes": "por mes", "porAno": "por año",
  "sinConv": "Sin convertir, saldría {P} × {r} × {t} = {I}: {x}", "grande": "demasiado grande.", "chico": "demasiado pequeño.",
  "mu1": "Un préstamo de {P} al {r} de interés simple anual se paga en {t} meses. ¿Cuánto interés se paga?", "mu1s": "{t} meses ÷ 12 = {a} años. I = {P2} × {d} × {a} = {I}.", "mu1p": "Se usaron los meses como si fueran años. Divida los meses entre 12.",
  "mu2": "Una tienda financia una compra de {P} al {r} <strong>mensual</strong> durante {t} meses. ¿Cuánto interés se paga?", "mu2s": "Tasa mensual y tiempo en meses: ya coinciden. I = {P2} × {d} × {t} = {I}.", "mu2p": "La tasa es mensual y el tiempo está en meses: no hay que dividir entre 12.",
  "mu3": "Un saldo de {P} tiene un interés simple del {r} anual durante {t} días. Use el año comercial de 360 días. ¿Cuánto interés se genera?", "mu3s": "{t} ÷ 360 = {a} años. I = {P2} × {d} × {a} = {I}.", "mu3p": "Los días hay que pasarlos a años: divida entre 360.", "mu3q": "El problema pide el año comercial: divida entre 360, no entre 365.",
  "meses": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
  "mu4": "Un certificado de depósito de {P} se abre el 1 de {a} y vence el 1 de {b} del mismo año, al {r} de interés simple anual. ¿Cuánto interés genera?", "mu4s": "Del 1 de {a} al 1 de {b} hay {m} meses = {y} años. I = {P2} × {d} × {y} = {I}.", "mu4p": "Cuente los meses y páselos a años (÷ 12).", "mu4q": "Ese es el interés de un año completo; el plazo es más corto.",
  "buscaP": "principal", "deP": "P = I ÷ (r × t) = {I} ÷ ({r} × {t}) = {I} ÷ {d}", "resP": "P = {x}", "compP": "Comprobación: {x} × {r} × {t} = {I} ✓",
  "deR": "r = I ÷ (P × t) = {I} ÷ ({P} × {t}) = {I} ÷ {d} = {x}", "porCien": "Para el porcentaje se multiplica por 100.", "resR": "r = {x}% anual",
  "deT": "t = I ÷ (P × r) = {I} ÷ ({P} × {r}) = {I} ÷ {d}", "resT": "t = {x} años", "yMeses": " ({a} años y {m} meses)",
  "cero1": "La tasa y el tiempo no pueden ser 0.", "cero2": "El principal y el tiempo no pueden ser 0.", "cero3": "El principal y la tasa no pueden ser 0.",
  "de1": "¿Cuánto hay que depositar al {r} anual para ganar {I} de interés en {t} años?", "de1s": "P = {I2} ÷ ({d} × {t}) = {I2} ÷ {q} = {P}.", "de1p": "Se multiplicó; para hallar el principal se divide el interés entre (r × t).",
  "de2": "Un préstamo de {P} a {t} años generó {I} de interés. ¿Qué tasa anual se cobró (en %)?", "de2s": "r = {I2} ÷ ({P2} × {t}) = {d} → {r}%.", "de2p": "Ese es el decimal: multiplíquelo por 100 para el porcentaje.",
  "de3": "¿Cuántos años deben estar {P} al {r} anual para ganar {I} de interés?", "de3s": "t = {I2} ÷ ({P2} × {d}) = {I2} ÷ {q} = {t} años.", "de3p": "Eso está en meses; se piden años.",
  "de4": "Por un préstamo de {P} se devolvieron {A} en total al cabo de {t} años. ¿Qué tasa anual se cobró (en %)?", "de4s": "Primero el interés: {A2} − {P2} = {I2}. r = {I2} ÷ ({P2} × {t}) = {d} → {r}%.", "de4p": "Se usó el monto total como si fuera el interés. Primero reste: I = A − P."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function pc(x){ return nd(x) + "%"; }
function sinU(t){ return String(t).replace(/%|years?|años?/gi, ""); }
function leeC(id){ var v = leeD(String($(id).value).replace("%", "")); $(id).classList.toggle("error", v === null || v < 0); return v === null || v < 0 ? null : v; }
function pl(n, par){ return n === 1 ? par[0] : par[1]; }
function barrasAnios(vals, base, voz){
  var W = 640, H = 240, x0 = 70, x1 = 620, yb = 200, mx = Math.max.apply(null, vals), n = vals.length, w = (x1 - x0) / n * 0.72, s = '<svg class="figura" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + voz + '">';
  function Y(v){ return yb - v * 170 / mx; }
  vals.forEach(function(v, k){
    var x = x0 + (x1 - x0) * k / n + (x1 - x0) / n * 0.14;
    s += '<rect x="' + f1(x) + '" y="' + f1(Y(v)) + '" width="' + f1(w) + '" height="' + f1(yb - Y(v)) + '" fill="#b2dfdb"/>';
    if (base !== null) s += '<rect x="' + f1(x) + '" y="' + f1(Y(Math.min(base, v))) + '" width="' + f1(w) + '" height="' + f1(yb - Y(Math.min(base, v))) + '" fill="#00695c"/>';
    s += texto([x + w / 2, yb + 16], k, 13, "#424242", 400);
  });
  s += linea([x0, yb], [x1, yb], "#424242", 2) + texto([(x0 + x1) / 2, H - 4], TXT.anoW, 13, "#424242", 700);
  s += '<text x="' + (x0 - 6) + '" y="' + f1(Y(mx)) + '" font-size="12" fill="#424242" text-anchor="end">' + dinero(mx) + '</text>';
  return s + '</svg>';
}

/* ============ MODULE 1 · vocabulary ============ */
function genVocab(){
  var P = 500 * aleatorio(2, 20), r = elige([3, 4, 5, 6, 7.5, 8]), m = elige([12, 18, 24, 36, 6, 30]), tt = m / 12, si = elige(TXT.sit);
  var enun = F(TXT.enun, { n: elige(TXT.nombres), v: si[0], P: dinero(P), s: si[1], r: pc(r), m: m });
  var q = aleatorio(1, 3), claves = ["P", "r", "t", "I"];
  if (q === 1){ var c = Math.random() < 0.5 ? [dinero(P), "P", TXT.esP] : [pc(r), "r", TXT.esR];
    return { enun: enun + F(TXT.queRep, { x: c[0] }), opciones: TXT.letras.map(function(x, i){ return { html: x, clave: claves[i] }; }), correcta: c[1], enOrden: true, bien: c[2], mal: c[2] }; }
  var pist = {};
  if (q === 2){ var o = [nd(tt), String(m), nd(m / 10), nd(12 / m)].filter(function(x, i, a){ return a.indexOf(x) === i; }).map(function(x){ return { html: "t = " + x, clave: "t" + x }; });
    pist["t" + m] = TXT.tAnos;
    return { enun: enun + TXT.queT, opciones: o, correcta: "t" + nd(tt), pistas: pist, bien: F(TXT.tSol, { m: m, t: nd(tt) }), mal: TXT.tAnos + " " + F(TXT.tSol, { m: m, t: nd(tt) }) }; }
  var o2 = [nd(r / 100), nd(r), nd(r / 10), nd(r / 1000)].filter(function(x, i, a){ return a.indexOf(x) === i; }).map(function(x){ return { html: "r = " + x, clave: "r" + x }; });
  pist["r" + nd(r)] = TXT.rDec;
  return { enun: enun + TXT.queR, opciones: o2, correcta: "r" + nd(r / 100), pistas: pist, bien: F(TXT.rSol, { p: pc(r), d: nd(r / 100) }), mal: TXT.rDec + " " + F(TXT.rSol, { p: pc(r), d: nd(r / 100) }) };
}

/* ============ MODULE 2 · the formula ============ */
function pintaIS(){
  var P = +$("is-c").value, r = +$("is-r").value, tt = +$("is-t").value, an = P * r / 100, I = an * tt;
  $("is-cv").textContent = dinero(P); $("is-rv").textContent = pc(r); $("is-tv").textContent = nd(tt);
  $("is-salida").innerHTML = '<div class="linea">' + F(TXT.datos, { P: dinero(P), p: pc(r), r: nd(r / 100), t: nd(tt) }) + '</div>' +
    '<div class="linea">' + F(TXT.unAno, { P2: nd(P), r: nd(r / 100), a: dinero(an), t: nd(tt), y: pl(tt, TXT.ano), I: dinero(I) }) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.resIS, { I: dinero(I), P: dinero(P), A: dinero(P + I) }) + '</div>';
}
function genIS(){
  var P = 100 * aleatorio(5, 60), r = elige([2, 3, 4, 5, 6, 8, 2.5, 3.5]), tt = elige([1, 2, 3, 4, 5, 6, 1.5, 2.5]), I = P * r / 100 * tt, pideA = Math.random() < 0.4, res = pideA ? P + I : I;
  var pist = [{ v: P * r * tt + (pideA ? P : 0), msg: F(TXT.isD, { p: pc(r), r: nd(r / 100) }) }, { v: pideA ? I : P + I, msg: pideA ? TXT.isA : TXT.isI }, { v: P * r / 100 + (pideA ? P : 0), msg: TXT.isT }].filter(function(x){ return Math.abs(x.v - res) > 0.01; });
  return { enun: F(TXT.isQ, { P: dinero(P), p: pc(r), t: nd(tt), y: pl(tt, TXT.ano), x: pideA ? TXT.elA : TXT.elI }), correcta: dinero(res),
    solucion: F(TXT.isS, { P: nd(P), r: nd(r / 100), t: nd(tt), I: dinero(I) }) + (pideA ? F(TXT.isS2, { P: dinero(P), I: dinero(I), A: dinero(P + I) }) : "") + ".", evalua: numD(res, pist) };
}

/* ============ MODULE 3 · same unit ============ */
function pintaMU(){
  var c = leeC("mu-c"), r = leeC("mu-r"), tm = leeC("mu-t"), ru = $("mu-ru").value, tu = $("mu-tu").value, s = $("mu-salida");
  if (c === null || r === null || tm === null){ s.innerHTML = '<div class="linea">' + TXT.escribe + '</div>'; return; }
  var h = [], rd = r / 100, tt;
  if (ru === "m" && tu === "m"){ tt = tm; h.push(TXT.coinc); }
  else if (ru === "m"){ tt = tu === "a" ? tm * 12 : tm / (tu === "d360" ? 30 : 365 / 12);
    h.push(TXT.aMeses + (tu === "a" ? F(TXT.anosM, { t: nd(tm), m: nd(tt) }) : F(TXT.diasM, { t: nd(tm), d: tu === "d360" ? "30" : "30.42", m: nd(tt) }))); }
  else { tt = tu === "a" ? tm : (tu === "m" ? tm / 12 : tm / (tu === "d360" ? 360 : 365));
    h.push(tu === "a" ? TXT.yaAnos : TXT.aAnos + (tu === "m" ? F(TXT.mesesA, { t: nd(tm), a: nd(tt) }) : F(TXT.diasA, { t: nd(tm), d: tu === "d360" ? 360 : 365, a: nd(tt) }))); }
  var I = c * rd * tt;
  h.push(F(TXT.tasaDec, { p: pc(r), d: nd(rd), u: ru === "m" ? TXT.porMes : TXT.porAno }));
  h.push("I = " + nd(c) + " × " + nd(rd) + " × " + nd(tt) + " = <strong>" + dinero2(I) + "</strong>");
  if (!(ru === tu || (ru === "a" && tu === "a"))) h.push(F(TXT.sinConv, { P: nd(c), r: nd(rd), t: nd(tm), I: dinero2(c * rd * tm), x: c * rd * tm > I ? TXT.grande : TXT.chico }));
  s.innerHTML = h.map(function(x){ return '<div class="linea">' + x + '</div>'; }).join("");
}
function genMU(){
  var tp = aleatorio(1, 4), P, r, tt, I, enun, sol, pist = [];
  if (tp === 1){ P = 100 * aleatorio(10, 80); r = elige([3, 4, 5, 6, 8, 9, 10, 12]); tt = elige([3, 6, 8, 9, 15, 18, 20, 30]); I = P * r / 100 * tt / 12;
    enun = F(TXT.mu1, { P: dinero(P), r: pc(r), t: tt }); sol = F(TXT.mu1s, { t: tt, a: nd(tt / 12), P2: nd(P), d: nd(r / 100), I: dinero2(I) }); pist.push({ v: P * r / 100 * tt, msg: TXT.mu1p }); }
  else if (tp === 2){ P = 100 * aleatorio(6, 40); r = elige([1, 1.5, 2, 2.5]); tt = aleatorio(3, 12); I = P * r / 100 * tt;
    enun = F(TXT.mu2, { P: dinero(P), r: pc(r), t: tt }); sol = F(TXT.mu2s, { P2: nd(P), d: nd(r / 100), t: tt, I: dinero2(I) }); pist.push({ v: P * r / 100 * tt / 12, msg: TXT.mu2p }); }
  else if (tp === 3){ P = 100 * aleatorio(5, 50); r = elige([12, 18, 24, 6]); tt = elige([30, 60, 90, 120, 180]); I = P * r / 100 * tt / 360;
    enun = F(TXT.mu3, { P: dinero(P), r: pc(r), t: tt }); sol = F(TXT.mu3s, { t: tt, a: nd(tt / 360), P2: nd(P), d: nd(r / 100), I: dinero2(I) }); pist.push({ v: P * r / 100 * tt, msg: TXT.mu3p }, { v: P * r / 100 * tt / 365, msg: TXT.mu3q }); }
  else { var a = aleatorio(0, 5), m = elige([3, 4, 6]); P = 1000 * aleatorio(2, 20); r = elige([3, 4, 5, 6]); I = P * r / 100 * m / 12;
    enun = F(TXT.mu4, { P: dinero(P), a: TXT.meses[a], b: TXT.meses[a + m], r: pc(r) }); sol = F(TXT.mu4s, { a: TXT.meses[a], b: TXT.meses[a + m], m: m, y: nd(m / 12), P2: nd(P), d: nd(r / 100), I: dinero2(I) }); pist.push({ v: P * r / 100 * m, msg: TXT.mu4p }, { v: P * r / 100, msg: TXT.mu4q }); }
  I = Math.round(I * 100) / 100;
  return { enun: enun, correcta: dinero2(I), solucion: sol, evalua: numD(I, pist.map(function(p){ return { v: Math.round(p.v * 100) / 100, msg: p.msg }; }).filter(function(p){ return Math.abs(p.v - I) > 0.011; }), null, 0.011) };
}

/* ============ MODULE 4 · year by year ============ */
function pintaAA(){
  var P = +$("aa-c").value, r = +$("aa-r").value, an = P * r / 100, v = [];
  $("aa-cv").textContent = dinero(P); $("aa-rv").textContent = r + "%";
  for (var k = 0; k <= 10; k++) v.push(P + an * k);
  $("aa-svg").innerHTML = barrasAnios(v, P, F(TXT.aaVoz, { a: dinero(an) }));
  var h = '<table class="reglas"><caption>' + F(TXT.aaCap, { P: dinero(P), r: r + "%" }) + '</caption><thead><tr>' + TXT.aaCab.map(function(c){ return '<th scope="col">' + c + '</th>'; }).join("") + '</tr></thead><tbody>';
  [0, 1, 2, 3, 5, 10].forEach(function(k){ h += '<tr><td>' + k + '</td><td>' + (k ? dinero(an) : "—") + '</td><td>' + dinero(an * k) + '</td><td>' + dinero(P + an * k) + '</td></tr>'; });
  $("aa-tabla").innerHTML = h + '</tbody></table>';
}
function genAA(){
  var P = 100 * aleatorio(5, 50), r = elige([2, 3, 4, 5, 6, 8, 10]), an = P * r / 100, k = aleatorio(2, 10), tp = aleatorio(1, 3), res, o = { P: dinero(P), r: r + "%", k: k };
  res = tp === 1 ? an : (tp === 2 ? an * k : P + an * k);
  var sol = F(TXT.aaS, { P2: nd(P), d: nd(r / 100), a: dinero(an) }) + (tp === 1 ? TXT.aaS1 : F(tp === 2 ? TXT.aaS2 : TXT.aaS3, { a: dinero(an), k: k, P: dinero(P), x: dinero(res) }));
  return { enun: F(TXT["aa" + tp], o), correcta: dinero(res), solucion: sol, evalua: numD(res, tp === 1 ? [{ v: an * k, msg: TXT.aaP }] : []) };
}

/* ============ MODULE 5 · solve for P, r, or t ============ */
var BUSCA = "r";
function pintaDE(){
  document.querySelectorAll("#de-botones .eleccion").forEach(function(x){ x.setAttribute("aria-pressed", x.getAttribute("data-busca") === BUSCA ? "true" : "false"); });
  ["C", "r", "t"].forEach(function(k){ $("de-c" + k).style.display = k === BUSCA ? "none" : ""; });
  var P = leeC("de-C"), r = leeC("de-r"), tt = leeC("de-t"), I = leeC("de-I"), s = $("de-salida"), h;
  if ((BUSCA !== "C" && P === null) || (BUSCA !== "r" && r === null) || (BUSCA !== "t" && tt === null) || I === null){ s.innerHTML = '<div class="linea">' + TXT.escribe + '</div>'; return; }
  if (BUSCA === "C"){ var den = r / 100 * tt; if (!den){ s.innerHTML = '<div class="linea">' + TXT.cero1 + '</div>'; return; } var x = I / den;
    h = [F(TXT.deP, { I: nd(I), r: nd(r / 100), t: nd(tt), d: nd(den) }), '<span class="veredicto">' + F(TXT.resP, { x: dinero2(x) }) + '</span>', F(TXT.compP, { x: nd(Math.round(x * 100) / 100), r: nd(r / 100), t: nd(tt), I: dinero2(x * den) })]; }
  else if (BUSCA === "r"){ var d2 = P * tt; if (!d2){ s.innerHTML = '<div class="linea">' + TXT.cero2 + '</div>'; return; } var rr = I / d2;
    h = [F(TXT.deR, { I: nd(I), P: nd(P), t: nd(tt), d: nd(d2), x: nd(rr) }), TXT.porCien, '<span class="veredicto">' + F(TXT.resR, { x: nd(Math.round(rr * 10000) / 100) }) + '</span>']; }
  else { var d3 = P * r / 100; if (!d3){ s.innerHTML = '<div class="linea">' + TXT.cero3 + '</div>'; return; } var t2 = I / d3, frac = t2 % 1;
    h = [F(TXT.deT, { I: nd(I), P: nd(P), r: nd(r / 100), d: nd(d3) }), '<span class="veredicto">' + F(TXT.resT, { x: nd(t2) }) + (Math.abs(t2 * 12 - Math.round(t2 * 12)) < 1e-6 && frac ? F(TXT.yMeses, { a: Math.floor(t2), m: Math.round(frac * 12) }) : "") + '</span>']; }
  s.innerHTML = h.map(function(x){ return '<div class="linea">' + x + '</div>'; }).join("");
}
function genDE(){
  var P = 100 * aleatorio(5, 60), r = elige([2, 3, 4, 5, 6, 7, 8, 10, 12]), tt = elige([1, 1.5, 2, 2.5, 3, 4, 5, 6]), I = Math.round(P * r / 100 * tt * 100) / 100, tp = aleatorio(1, 4);
  var o = { P: dinero(P), P2: nd(P), r: r, I: dinero(I), I2: nd(I), t: nd(tt), d: nd(r / 100), q: nd(r / 100 * tt) };
  if (tp === 1){ o.r = pc(r); return { enun: F(TXT.de1, o), correcta: dinero(P), solucion: F(TXT.de1s, o), evalua: numD(P, [{ v: Math.round(I * r / 100 * tt * 100) / 100, msg: TXT.de1p }], null, 0.011) }; }
  if (tp === 2){ var ev2 = numD(r, [{ v: r / 100, msg: TXT.de2p }], null, 0.011); return { enun: F(TXT.de2, o), correcta: pc(r), solucion: F(TXT.de2s, o), evalua: function(s){ return ev2(sinU(s)); } }; }
  if (tp === 3){ o.r = pc(r); o.q = nd(P * r / 100); var ev3 = numD(tt, [{ v: tt * 12, msg: TXT.de3p }].filter(function(x){ return Math.abs(x.v - tt) > 0.01; }), null, 0.011); return { enun: F(TXT.de3, o), correcta: nd(tt), solucion: F(TXT.de3s, o), evalua: function(s){ return ev3(sinU(s)); } }; }
  var A = Math.round((P + I) * 100) / 100; o.A = dinero(A); o.A2 = nd(A);
  var ev4 = numD(r, [{ v: Math.round(A / (P * tt) * 10000) / 100, msg: TXT.de4p }], null, 0.011);
  return { enun: F(TXT.de4, o), correcta: pc(r), solucion: F(TXT.de4s, o), evalua: function(s){ return ev4(sinU(s)); } };
}

/* ============ Start ============ */
creaPracticaOM("p1", genVocab);
["is-c", "is-r", "is-t"].forEach(function(id){ $(id).addEventListener("input", pintaIS); }); pintaIS();
creaPracticaLibre("p2", genIS);
["mu-c", "mu-r", "mu-t"].forEach(function(id){ $(id).addEventListener("input", pintaMU); }); ["mu-ru", "mu-tu"].forEach(function(id){ $(id).addEventListener("change", pintaMU); }); pintaMU();
creaPracticaLibre("p3", genMU);
["aa-c", "aa-r"].forEach(function(id){ $(id).addEventListener("input", pintaAA); }); pintaAA();
creaPracticaLibre("p4", genAA);
document.querySelectorAll("#de-botones .eleccion").forEach(function(b){ b.addEventListener("click", function(){ BUSCA = b.getAttribute("data-busca"); pintaDE(); }); });
["de-C", "de-r", "de-t", "de-I"].forEach(function(id){ $(id).addEventListener("input", pintaDE); }); pintaDE();
creaPracticaLibre("p5", genDE);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA_D = ("Type only the number. It may have cents, like 1,240.50; you may use the $ sign.", "Escriba solo el número. Puede llevar centavos, como 1,240.50; puede usar el signo $.")

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:170px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    def caja_n(i, et, v, idc=None):
        c = f' id="{idc}"' if idc else ""
        return f'<div class="campo"{c}><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="{i}" value="{v}"></div>'
    mods = [
     (t("vocabulary", "vocabulario"), t("Money vocabulary", "Vocabulario financiero"),
      f'''      <table class="reglas">
        <caption>{t("The five quantities of simple interest", "Las cinco cantidades del interés simple")}</caption>
        <thead><tr><th scope="col">{t("Quantity", "Cantidad")}</th><th scope="col">{t("What it is", "Qué es")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Principal (P)", "Principal (P)")}</td><td>{t("the starting money you deposit or borrow", "el dinero inicial que se deposita o se presta")}</td></tr>
          <tr><td>{t("Rate (r)", "Tasa (r)")}</td><td>{t("the yearly percent applied to the principal", "el porcentaje anual que se aplica al principal")}</td></tr>
          <tr><td>{t("Time (t)", "Tiempo (t)")}</td><td>{t("how long, in years", "la duración, en años")}</td></tr>
          <tr><td>{t("Interest (I)", "Interés (I)")}</td><td>{t("the money the savings earn, or what the loan costs", "el dinero que genera el ahorro, o lo que cuesta el préstamo")}</td></tr>
          <tr><td>{t("Total amount (A)", "Monto total (A)")}</td><td>{t("principal plus interest: A = P + I", "principal más interés: A = P + I")}</td></tr>
        </tbody>
      </table>
      <div class="caja-atencion"><strong>{t("Time goes in years:", "El tiempo va en años:")}</strong> {t("18 months are 1.5 years, because 18 ÷ 12 = 1.5. And 6 months are half a year.", "18 meses son 1.5 años, porque 18 ÷ 12 = 1.5. Y 6 meses son medio año.")}</div>
{B.om("p1", t("Practice: identify the data", "Practique: identifique los datos"))}'''),
     (t("simple-interest", "interes-simple"), t("The simple-interest formula", "La fórmula del interés simple"),
      f'''      <div class="formula">I = P × r × t &nbsp;&nbsp;&nbsp; A = P + I</div>
      <p>{t("The rate goes into the formula <strong>as a decimal</strong>: 6% is written 0.06. That is the step where most mistakes happen.", "La tasa entra en la fórmula <strong>en decimal</strong>: el 6% se escribe 0.06. Ese es el paso donde más errores ocurren.")}</p>
      <h3>{t("Interest calculator", "Calculadora de interés")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("is-c", t("Principal", "Principal"), 500, 10000, 3500, 100)}
          {desl("is-r", t("Yearly rate", "Tasa anual"), 1, 12, 4, 0.5)}
          {desl("is-t", t("Time (years)", "Tiempo (años)"), 0.5, 10, 6, 0.5)}
        </div>
        <div class="salida" id="is-salida" aria-live="polite"></div>
      </div>
{libre_x("p2", t("Practice: interest and total amount", "Practique: interés y monto"), t("Answer in dollars", "Resultado en dólares"), t(*NOTA_D))}'''),
     (t("same-unit", "misma-unidad"), t("The rate and the time in the same unit", "La tasa y el tiempo, en la misma unidad"),
      f'''      <p>{t("The formula only works if the rate is a decimal and the rate and the time use <strong>the same unit</strong>. If the rate is yearly, the time goes in years: divide months by 12 and days by 365 (or by 360, if the problem says to use the banker's year). If the rate is monthly and the time is in months, they already match.", "La fórmula solo funciona si la tasa está en decimal y si la tasa y el tiempo usan <strong>la misma unidad</strong>. Si la tasa es anual, el tiempo va en años: los meses se dividen entre 12 y los días entre 365 (o entre 360, si el problema indica el año comercial). Si la tasa es mensual y el tiempo está en meses, ya coinciden.")}</p>
      <div class="caja-atencion"><strong>{t("Common mistake:", "Error frecuente:")}</strong> {t("using 9 months as if they were 9 years. A $4,000 loan at 6% a year for 9 months costs 4,000 × 0.06 × 0.75 = $180, not $2,160.", "usar 9 meses como si fueran 9 años. Un préstamo de $4,000 al 6% anual por 9 meses cuesta 4,000 × 0.06 × 0.75 = $180, no $2,160.")}</div>
      <h3>{t("Change and calculate", "Convierta y calcule")}</h3>
      <div class="panel">
        <div class="campos">
          {caja_n("mu-c", t("Principal ($)", "Principal ($)"), 4000)}
          {caja_n("mu-r", t("Rate (%)", "Tasa (%)"), 6)}
          <div class="campo"><label for="mu-ru">{t("The rate is…", "La tasa es…")}</label><select id="mu-ru"><option value="a">{t("yearly", "anual")}</option><option value="m">{t("monthly", "mensual")}</option></select></div>
          {caja_n("mu-t", t("Time", "Tiempo"), 9)}
          <div class="campo"><label for="mu-tu">{t("in…", "en…")}</label><select id="mu-tu"><option value="a">{t("years", "años")}</option><option value="m" selected>{t("months", "meses")}</option><option value="d365">{t("days (365-day year)", "días (año de 365)")}</option><option value="d360">{t("days (360-day banker's year)", "días (año comercial de 360)")}</option></select></div>
        </div>
        <div class="salida" id="mu-salida" aria-live="polite"></div>
      </div>
{libre_x("p3", t("Practice: change before you calculate", "Practique: convierta antes de calcular"), t("Interest ($)", "Interés ($)"), t(*NOTA_D))}'''),
     (t("year-by-year", "ano-a-ano"), t("Growth year by year", "Crecimiento año tras año"),
      f'''      <p>{t("With simple interest, each year's interest is <strong>always the same</strong>, because it is figured on the original principal. The money grows in a regular way: a staircase with equal steps.", "En el interés simple, el interés de cada año es <strong>siempre el mismo</strong>, porque se calcula sobre el principal original. Por eso el dinero crece de forma regular: una escalera de escalones iguales.")}</p>
      <h3>{t("The savings staircase", "La escalera del ahorro")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("aa-c", t("Principal", "Principal"), 500, 5000, 1000, 100)}
          {desl("aa-r", t("Yearly rate", "Tasa anual"), 1, 15, 8)}
        </div>
        <div id="aa-svg"></div>
        <div class="tabla-scroll" id="aa-tabla"></div>
      </div>
      <div class="caja-tip"><strong>{t("Compound interest is different:", "El interés compuesto es distinto:")}</strong> {t("there, each year's interest is figured on the amount from the year before, and money grows faster.", "ahí cada año el interés se calcula sobre el monto del año anterior, y el dinero crece más rápido.")}</div>
{libre_x("p4", t("Practice: year by year", "Practique: año tras año"), t("Answer in dollars", "Resultado en dólares"), t(*NOTA_D))}'''),
     (t("solve-for", "despejar"), t("Solving for the principal, the rate, or the time", "Despejar el principal, la tasa o el tiempo"),
      f'''      <p>{t("If you know three of the four quantities in I = P × r × t, you can find the missing one. <strong>One rule for all three:</strong> divide the interest by the product of the other two values.", "Si se conocen tres de las cuatro cantidades de I = P × r × t, se puede hallar la que falta. <strong>Una sola regla para las tres:</strong> se divide el interés entre el producto de los otros dos datos.")}</p>
      <table class="reglas">
        <caption>{t("The three ways to solve", "Los tres despejes")}</caption>
        <thead><tr><th scope="col">{t("You want", "Se busca")}</th><th scope="col">{t("Formula", "Fórmula")}</th></tr></thead>
        <tbody>
          <tr><td>{t("The principal", "El principal")}</td><td>P = I ÷ (r × t)</td></tr>
          <tr><td>{t("The rate", "La tasa")}</td><td>{t("r = I ÷ (P × t), then × 100 for the percent", "r = I ÷ (P × t), y se multiplica por 100 para el porcentaje")}</td></tr>
          <tr><td>{t("The time", "El tiempo")}</td><td>t = I ÷ (P × r)</td></tr>
        </tbody>
      </table>
      <div class="caja-tip"><strong>{t("If the problem gives the total amount A", "Si el problema da el monto total A")}</strong> {t("instead of the interest, first find I = A − P.", "en lugar del interés, primero se calcula I = A − P.")}</div>
      <h3>{t("Choose what you are looking for", "Elija qué busca")}</h3>
      <div class="panel">
        <div class="elecciones" id="de-botones" role="group" aria-label="{t("Choose what you are looking for", "Elija qué se busca")}">
          <button type="button" class="eleccion" data-busca="C" aria-pressed="false">{t("The principal", "El principal")}</button>
          <button type="button" class="eleccion" data-busca="r" aria-pressed="true">{t("The rate", "La tasa")}</button>
          <button type="button" class="eleccion" data-busca="t" aria-pressed="false">{t("The time", "El tiempo")}</button>
        </div>
        <div class="campos">
          {caja_n("de-C", t("Principal ($)", "Principal ($)"), 2000, "de-cC")}
          {caja_n("de-r", t("Yearly rate (%)", "Tasa anual (%)"), 7, "de-cr")}
          {caja_n("de-t", t("Time (years)", "Tiempo (años)"), 4, "de-ct")}
          {caja_n("de-I", t("Interest ($)", "Interés ($)"), 560)}
        </div>
        <div class="salida" id="de-salida" aria-live="polite"></div>
      </div>
{libre_x("p5", t("Practice: find the missing value", "Practique: halle el dato que falta"), t("Answer", "Resultado"), t("Type only the number: dollars, a percent (5 for 5%), or years (2.5).", "Escriba solo el número: dólares, porcentaje (5 para 5%) o años (2.5)."))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Interés simple: la fórmula I = P × r × t")
