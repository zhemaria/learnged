"""LearnGED · Estudios sociales · Lección 5.3 · Impuestos, presupuesto y política fiscal (EN/ES).
Fuente: sociales/soc-5-3.html (incluido el interactivo «Clasifique seis impuestos»).
Datos reales: CBO, Monthly Budget Review: Summary for Fiscal Year 2026 (9 de noviembre de 2026); SSA (tope salarial de 2026: $184,500);
la deuda bruta superó los $40 billones (trillion) el 19 de agosto de 2026 (Tesoro).
Uso: python3 tools/build_soc_5_3.py
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, documento, cita

N = "5-3"
F = 'font-family="Segoe UI, Arial, sans-serif"'

# CBO, año fiscal 2026, miles de millones de dólares
ING = [("ind", 2846), ("nom", 1812), ("soc", 381), ("adu", 173), ("otr", 191)]
GAS = [("ss", 1654), ("int", 1142), ("med", 1069), ("def", 917), ("mcd", 723), ("res", 1891)]
TOT_I, TOT_G = 5403, 7396


def titulo():
    return t("Taxes, the budget, and fiscal policy", "Impuestos, presupuesto y política fiscal")


def pct(a, b):
    return round(a / b * 100, 1)


def graf_ingresos():
    nom = {"ind": t("Individual\nincome tax", "Renta de\nlas personas"), "nom": t("Payroll\ntaxes", "Retenciones\nde nómina"), "soc": t("Corporate\nincome tax", "Renta de\nsociedades"),
           "adu": t("Customs duties\n(tariffs)", "Aduanas\n(aranceles)"), "otr": t("Other", "Otros")}
    spec = {"tipo": "barras", "xEtq": t("Source", "Fuente"), "yEtq": t("Percent of federal revenue", "Porcentaje de los ingresos federales"),
            "barras": [{"etq": nom[k], "valor": pct(v, TOT_I), "txt": f"{pct(v, TOT_I)}%"} for k, v in ING]}
    return C.grafica(spec, C.describe(spec), ancho=620, alto=330, y0=0, y1=60)


def graf_gastos():
    nom = {"ss": t("Social\nSecurity", "Seguro\nSocial"), "int": t("Interest\non the debt", "Intereses\nde la deuda"), "med": "Medicare", "def": t("Defense", "Defensa"), "mcd": "Medicaid", "res": t("Everything\nelse", "Todo\nlo demás")}
    spec = {"tipo": "barras", "xEtq": t("Category", "Categoría"), "yEtq": t("Percent of federal spending", "Porcentaje del gasto federal"),
            "barras": [{"etq": nom[k], "valor": pct(v, TOT_G), "txt": f"{pct(v, TOT_G)}%"} for k, v in GAS]}
    return C.grafica(spec, C.describe(spec), ancho=660, alto=330, y0=0, y1=30)


DEF = [5, 8, 6, 9, 7, 3, 6, 9, 8, 7]


def deuda():
    d, out = 20, []
    for x in DEF:
        d += x
        out.append(d)
    return out


def graf_deficit():
    spec = {"tipo": "barras", "xEtq": t("Year", "Año"), "yEtq": t("Deficit (made-up units)", "Déficit (unidades inventadas)"), "barras": [{"etq": str(i + 1), "valor": v} for i, v in enumerate(DEF)]}
    return C.grafica(spec, C.describe(spec), ancho=420, alto=280, y0=0, y1=10)


def graf_deuda():
    spec = {"tipo": "linea", "xEtq": t("Year", "Año"), "yEtq": t("Debt (made-up units)", "Deuda (unidades inventadas)"), "series": [{"nombre": t("Debt", "Deuda"), "puntos": [[i + 1, v] for i, v in enumerate(deuda())]}]}
    return C.grafica(spec, C.describe(spec), ancho=420, alto=280, y0=0, y1=100)


def svg_ciclo():
    aria = t("The business cycle. A wavy line rises and falls over time around a slowly rising trend. It rises during an expansion to a peak, falls during a contraction (recession) to a trough, and then rises again in a new expansion. Expansionary fiscal policy is used near the trough; contractionary policy near the peak.",
             "El ciclo económico. Una línea ondulada sube y baja con el tiempo alrededor de una tendencia que crece despacio. Sube durante la expansión hasta un pico, baja durante la contracción (recesión) hasta un valle, y vuelve a subir en una nueva expansión. La política fiscal expansiva se usa cerca del valle; la restrictiva, cerca del pico.")
    pts = []
    for x in range(60, 681, 5):
        y = 220 - 0.12 * (x - 60) - 50 * math.sin(2 * math.pi * (x - 60) / 400 - math.pi / 2)
        pts.append(f"{x},{y:.1f}")
    s = [f'<svg class="diagrama" style="max-width:720px" viewBox="0 0 720 320" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">',
         '<line x1="50" y1="285" x2="700" y2="285" stroke="#3d4753" stroke-width="2"/><line x1="50" y1="285" x2="50" y2="20" stroke="#3d4753" stroke-width="2"/>',
         f'<text x="690" y="306" text-anchor="end" {F} font-size="13" fill="#3d4753">{t("Time →", "Tiempo →")}</text>',
         f'<text x="22" y="160" text-anchor="middle" transform="rotate(-90 22 160)" {F} font-size="13" fill="#3d4753">{t("Economic activity (real GDP)", "Actividad económica (PIB real)")}</text>',
         '<line x1="60" y1="220" x2="680" y2="145.6" stroke="#9aa4ae" stroke-width="1.5" stroke-dasharray="6 5"/>',
         f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2e6b30" stroke-width="4" stroke-linejoin="round"/>',
         f'<circle cx="260" cy="146" r="6" fill="#9c3d1c"/><text x="260" y="130" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#9c3d1c">{t("Peak", "Pico")}</text>',
         f'<circle cx="460" cy="222" r="6" fill="#283593"/><text x="460" y="250" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#283593">{t("Trough", "Valle")}</text>',
         f'<text x="135" y="178" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#2e6b30">{t("Expansion", "Expansión")}</text>',
         f'<text x="350" y="122" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Contraction", "Contracción")}</text>',
         f'<text x="350" y="138" text-anchor="middle" {F} font-size="12.5" fill="#1a2330">{t("(recession)", "(recesión)")}</text>',
         f'<text x="590" y="236" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#2e6b30">{t("Expansion", "Expansión")}</text>',
         f'<text x="250" y="60" text-anchor="middle" {F} font-size="12.5" fill="#9c3d1c">{t("Near the peak: slow down", "Cerca del pico: frenar")}</text>',
         f'<text x="250" y="76" text-anchor="middle" {F} font-size="12.5" fill="#9c3d1c">{t("(contractionary)", "(restrictiva)")}</text>',
         f'<text x="470" y="278" text-anchor="middle" {F} font-size="12.5" fill="#283593">{t("Near the trough: speed up (expansionary)", "Cerca del valle: acelerar (expansiva)")}</text>',
         "</svg>"]
    return "".join(s)


def leccion():
    P = C.Practicas()
    nomina = [[t("Gross pay", "Salario bruto"), "—", "$2,000.00", "—"],
              [t("Social Security", "Seguro Social"), "6.2%", "$124.00", t("Retirement and disability benefits", "Pensiones de jubilación e invalidez")],
              ["Medicare", "1.45%", "$29.00", t("Health insurance for people 65 and older", "Seguro médico para mayores de 65 años")],
              [t("Federal income tax withheld", "Retención federal sobre la renta"), t("varies", "variable"), "$180.00", t("The general fund: defense, interest, and everything else", "El fondo general: defensa, intereses y todo lo demás")],
              [t("Illinois income tax", "Impuesto de Illinois sobre la renta"), t("4.95% flat", "4.95 % fijo"), "$99.00", t("The state budget, not the federal one", "El presupuesto del estado, no el federal")],
              [t("Total withheld", "Total retenido"), "21.6%", "$432.00", "—"],
              [t("Net pay", "Salario neto"), "—", "$1,568.00", "—"]]
    s1 = f"""<p>{t("This is a paycheck for two weeks with the usual deductions of an Illinois worker. The federal withholding is an example; the other rates are the ones in effect in 2026.", "Esta es una nómina quincenal con las retenciones habituales de un trabajador de Illinois. La retención federal es un ejemplo; las demás tasas son las vigentes en 2026.")}</p>
{C.tabla(t("A two-week paycheck and where each deduction goes", "Una nómina quincenal y adónde va cada retención"), [t("Item", "Concepto"), t("Rate", "Tasa"), t("Amount", "Importe"), t("Where it goes", "Adónde va")], nomina)}
{C.caja("tip", t("Two things to notice in that table", "Dos cosas que conviene notar en esa tabla"), "<p>" + t("First: the 6.2% and the 1.45% do not go to the general fund but to two specific programs, which is why they appear with their names. Second: the Illinois line never travels to Washington. That is the federalism of Lesson 3.3, showing up on a pay stub.", "Primera: el 6.2 % y el 1.45 % no van al fondo general, sino a dos programas concretos, y por eso aparecen con su nombre. Segunda: la línea de Illinois no viaja a Washington. Es el federalismo de la Lección 3.3, apareciendo en un recibo de sueldo.") + "</p>")}
<h3>{t("Where federal revenue comes from", "De dónde salen los ingresos federales")}</h3>
{graf_ingresos()}
<p class="fuente">{t("Real data for fiscal year 2026 (October 2025 to September 2026). Source: Congressional Budget Office, report of November 9, 2026. Total revenue: $5.4 trillion.", "Datos reales del año fiscal 2026 (de octubre de 2025 a septiembre de 2026). Fuente: Oficina de Presupuesto del Congreso (CBO), informe del 9 de noviembre de 2026. Ingresos totales: $5.4 billones (en inglés, <em lang=\"en\">trillion</em>).")}</p>
<p>{t("Add the first two bars: about <strong>86 of every 100 dollars</strong> the federal government collects come from people’s paychecks and incomes, one way or the other. The pay stub above is not a small example: it is the main source.", "Sume las dos primeras barras: unos <strong>86 de cada 100 dólares</strong> que recauda el gobierno federal salen de la nómina y la renta de las personas, por una vía o por la otra. El recibo de arriba no es un ejemplo pequeño: es la fuente principal.")}</p>
<h3>{t("Where federal spending goes", "Adónde va el gasto federal")}</h3>
{graf_gastos()}
<p class="fuente">{t("Real data for fiscal year 2026. Source: Congressional Budget Office, report of November 9, 2026. Total spending: $7.4 trillion. “Everything else” includes veterans, food assistance, education, transportation, and the rest of the government.", "Datos reales del año fiscal 2026. Fuente: Oficina de Presupuesto del Congreso (CBO), informe del 9 de noviembre de 2026. Gasto total: $7.4 billones. «Todo lo demás» incluye veteranos, asistencia alimentaria, educación, transporte y el resto del gobierno.")}</p>
{C.caja("ojo", t("Look at the interest bar", "Fíjese en la barra de los intereses"), "<p>" + t("In 2026 interest on the debt (15.4%) was <strong>larger than defense</strong> (12.4%), and it buys no service at all: it is the cost of money borrowed in earlier years. Section 3 explains where it comes from.", "En 2026 los intereses de la deuda (15.4 %) fueron <strong>mayores que la defensa</strong> (12.4 %), y no compran ningún servicio: son el costo del dinero que se pidió prestado en años anteriores. La sección 3 explica de dónde salen.") + "</p>")}
{P(t("Practice 1 · The budget", "Práctica 1 · El presupuesto"), t("Where does most federal revenue come from?", "¿De dónde procede la mayor parte de los ingresos federales?"),
   [t("Corporate income taxes", "Del impuesto de sociedades"), t("Tariffs", "De los aranceles"), t("Individual income taxes and payroll taxes", "De la renta de las personas y las retenciones de nómina")], 2,
   {0: t("Only about 7%.", "Solo alrededor del 7 %."), 1: t("About 3%.", "Alrededor del 3 %.")}, t("About 86% together.", "Juntas, alrededor del 86 %."))}"""

    s2 = f"""<p>{t("The three words describe what <strong>percent of a person’s income</strong> the tax takes as income goes up. That is the key almost everyone misses: it is measured against income, not against the purchase.", "Las tres palabras describen qué <strong>porcentaje del ingreso de una persona</strong> se lleva el impuesto a medida que sube el ingreso. Esa es la clave que casi todo el mundo pasa por alto: se mide contra el ingreso, no contra la compra.")}</p>
{C.tabla(t("The three shapes of a tax", "Las tres formas de un impuesto"), [t("Type", "Tipo"), t("As income rises, the percent paid…", "Al subir el ingreso, el porcentaje pagado…"), t("Example", "Ejemplo")],
  [[t("Progressive", "Progresivo"), t("goes up", "sube"), t("The federal income tax, with its brackets", "El impuesto federal sobre la renta, con sus tramos")],
   [t("Proportional (flat)", "Proporcional"), t("stays the same", "se mantiene igual"), t("Illinois’s 4.95% income tax", "El impuesto de Illinois sobre la renta, del 4.95 %")],
   [t("Regressive", "Regresivo"), t("goes down", "baja"), t("The sales tax", "El impuesto sobre las ventas")]])}
<h3>{t("Why the sales tax is regressive if the rate is the same for everyone", "Por qué el impuesto sobre las ventas es regresivo si la tasa es igual para todos")}</h3>
{C.ejemplo(t("The same rate, two different burdens (10% sales tax, monthly)", "La misma tasa, dos cargas distintas (impuesto sobre las ventas del 10 %, al mes)"), [
   ("A", t("Person A earns $2,000 and spends $1,600 on taxed goods. Tax: $160. That is 160 ÷ 2,000 = <strong>8%</strong> of her income.", "La persona A gana $2,000 y gasta $1,600 en cosas gravadas. Impuesto: $160. Eso es 160 ÷ 2,000 = el <strong>8 %</strong> de su ingreso.")),
   ("B", t("Person B earns $10,000 and spends $4,000 on taxed goods. Tax: $400, more dollars. But that is 400 ÷ 10,000 = <strong>4%</strong> of his income.", "La persona B gana $10,000 y gasta $4,000 en cosas gravadas. Impuesto: $400, más dólares. Pero eso es 400 ÷ 10,000 = el <strong>4 %</strong> de su ingreso."))],
   t("Same rate, and A’s burden is twice B’s. People who earn less spend a larger share of what they earn; people who earn more save or invest part of it, and that part is not taxed at the register.", "Misma tasa, y la carga de A es el doble que la de B. Quien gana menos gasta una parte mayor de lo que ingresa; quien gana más ahorra o invierte una parte, y esa parte no paga impuesto en la caja."))}
{C.caja("ojo", t("The subtle case: Social Security", "El caso sutil: el Seguro Social"), "<p>" + t("Its rate is 6.2% for everyone, which looks proportional. But it is paid only up to a wage cap: <strong>$184,500 in 2026</strong>. Above that, nothing more is paid. Someone who earns $50,000 pays $3,100, which is 6.2% of income. Someone who earns $500,000 pays the maximum, $11,439, which is about <strong>2.3%</strong> of income. The printed rate is the same; the effective rate falls. That is why it is classified as regressive, and why you must always look at the <strong>effective rate on income</strong>, not the printed one. (Medicare, by contrast, has no cap: 1.45% on every dollar, plus an extra 0.9% above $200,000.)", "Su tasa es del 6.2 % para todos, lo que parece proporcional. Pero solo se paga hasta un tope de salario: <strong>$184,500 en 2026</strong>. Por encima de esa cifra no se paga más. Quien gana $50,000 paga $3,100, que es el 6.2 % de su ingreso. Quien gana $500,000 paga el máximo, $11,439, que es alrededor del <strong>2.3 %</strong> de su ingreso. La tasa impresa es la misma; la efectiva baja. Por eso se clasifica como regresivo, y por eso hay que mirar siempre la <strong>tasa efectiva sobre el ingreso</strong>, no la impresa. (Medicare, en cambio, no tiene tope: 1.45 % de cada dólar, más un 0.9 % adicional por encima de $200,000).") + "</p>")}
{P(t("Practice 2 · The shape of a tax", "Práctica 2 · La forma de un impuesto"), t("Why is a sales tax with the same rate for everyone regressive?", "¿Por qué es regresivo un impuesto sobre las ventas con la misma tasa para todos?"),
   [t("People who earn more pay fewer dollars", "Porque quien gana más paga menos dólares"), t("The rate changes from store to store", "Porque la tasa cambia según la tienda"), t("People who earn less spend a larger share of their income", "Porque quien gana menos gasta una parte mayor de su ingreso")], 2,
   {0: t("In dollars, they usually pay more.", "En dólares, suelen pagar más."), 1: t("The rate is the same.", "La tasa es la misma.")}, t("It is measured against income.", "Se mide contra el ingreso."))}
{C.enlace(N, t("tax-types", "tipos-de-impuesto"), t("Progressive, proportional, or regressive?", "¿Progresivo, proporcional o regresivo?"), t("Sort eight real taxes.", "Clasifique ocho impuestos reales."))}
{C.enlace(N, t("burden", "carga"), t("The real burden of a sales tax", "La carga real de un impuesto sobre las ventas"), t("New numbers every time: what percent of income does it take?", "Números nuevos cada vez: ¿qué porcentaje del ingreso se lleva?"))}"""

    s3 = f"""<p>{t("They are mixed up in the news every day, and the difference is simple:", "Se confunden a diario en las noticias, y la diferencia es sencilla:")}</p>
{C.tabla(t("Deficit and debt, compared", "Déficit y deuda, comparados"), ["", t("Deficit", "Déficit"), t("Debt", "Deuda")],
  [[t("What it measures", "Qué mide"), t("How much more was spent than collected in <strong>one year</strong>", "Cuánto se gastó de más de lo que se recaudó en <strong>un año</strong>"), t("How much is owed <strong>in total</strong>, added up", "Cuánto se debe <strong>en total</strong>, acumulado")],
   [t("Period", "Periodo"), t("One fiscal year", "Un año fiscal"), t("All of history up to today", "Toda la historia hasta hoy")],
   [t("At home, it is like…", "En casa, es como…"), t("what you overspent this month", "lo que gastó de más este mes"), t("the balance on your credit card", "el saldo que debe en la tarjeta")],
   [t("Real figure (November 2026)", "Cifra real (noviembre de 2026)"), t("$2.0 trillion in fiscal year 2026 (CBO)", "$2.0 billones en el año fiscal 2026 (CBO)"), t("Passed $40 trillion in August 2026 (Treasury)", "Superó los $40 billones en agosto de 2026 (Tesoro)")]])}
<p>{t("Ten years of deficits, and the debt they leave behind (made-up numbers; what matters is the shape):", "Diez años de déficit, y la deuda que van dejando (números inventados; lo que importa es la forma):")}</p>
<div class="dos-graficas"><div><h4>{t("Deficit each year", "Déficit de cada año")}</h4>{graf_deficit()}</div><div><h4>{t("Total debt", "Deuda total")}</h4>{graf_deuda()}</div></div>
<p>{t("The deficit bars go down in five of the ten years. The debt line does not go down even once. That is the whole difference: <strong>as long as there is a deficit, however small, the debt keeps growing</strong>.", "Las barras del déficit bajan en cinco de los diez años. La línea de la deuda no baja ni una sola vez. Ahí está toda la diferencia: <strong>mientras haya déficit, por pequeño que sea, la deuda sigue creciendo</strong>.")}</p>
{C.caja("tip", t("The sentence that clears up most headlines", "La frase que resuelve casi todos los titulares"), "<p>" + t("“The deficit went down” and “the debt went down” do not mean the same thing, and the first does not imply the second. A smaller deficit still adds to the debt; for the debt to go down, the government has to spend less than it collects, which is a <strong>surplus</strong>. And this connects with section 1: interest on the debt is what all the earlier deficits cost together. The larger the debt, the larger that part of the budget that buys no service.", "«El déficit ha bajado» y «la deuda ha bajado» no significan lo mismo, y lo primero no implica lo segundo. Un déficit menor sigue sumando a la deuda; para que la deuda baje, el gobierno tiene que gastar menos de lo que recauda, y eso es un <strong>superávit</strong>. Y esto conecta con la sección 1: los intereses de la deuda son lo que cuestan todos los déficits anteriores juntos. Cuanto mayor es la deuda, mayor es esa parte del presupuesto que no compra ningún servicio.") + "</p>")}
{P(t("Practice 3 · Deficit and debt", "Práctica 3 · Déficit y deuda"), t("This year’s deficit is smaller than last year’s. What happens to the debt?", "El déficit de este año es menor que el del año pasado. ¿Qué le pasa a la deuda?"),
   [t("It goes down too", "Baja también"), t("It keeps going up, but more slowly", "Sigue subiendo, aunque más despacio"), t("It stays exactly the same", "Se queda exactamente igual")], 1,
   {0: t("Only a surplus lowers the debt.", "Solo un superávit baja la deuda."), 2: t("Any deficit adds to the debt.", "Todo déficit suma a la deuda.")}, t("A smaller deficit is still added.", "Un déficit menor se sigue sumando."))}
{C.enlace(N, t("debt", "deuda"), t("Adding up the debt", "Sumar la deuda"), t("New numbers every time: from the deficits to the debt.", "Números nuevos cada vez: de los déficits a la deuda."))}"""

    s4 = f"""<p>{t("The government can use taxes and spending to influence the economy. There are only two directions. But first, it helps to know what is being acted on: the economy does not grow in a straight line, but in cycles.", "El gobierno puede usar los impuestos y el gasto para influir en la economía. Solo hay dos direcciones. Pero antes conviene saber sobre qué se actúa: la economía no crece en línea recta, sino en ciclos.")}</p>
{svg_ciclo()}
{C.tabla(t("The two directions of fiscal policy", "Las dos direcciones de la política fiscal"), ["", t("Expansionary · speed up", "Expansiva · acelerar"), t("Contractionary · slow down", "Restrictiva · frenar")],
  [[t("What it does", "Qué hace"), t("Spend more, cut taxes, or both", "Gastar más, bajar impuestos, o las dos cosas"), t("Spend less, raise taxes, or both", "Gastar menos, subir impuestos, o las dos cosas")],
   [t("When it is used", "Cuándo se usa"), t("When the economy cools: high unemployment, little activity", "Cuando la economía se enfría: mucho desempleo, poca actividad"), t("When the economy overheats and prices rise fast", "Cuando la economía se recalienta y los precios suben deprisa")],
   [t("How it works", "Cómo funciona"), t("Puts more money in circulation, which supports spending and jobs", "Pone más dinero en circulación, lo que sostiene el consumo y el empleo"), t("Takes money out of circulation and cools demand", "Retira dinero de circulación y modera la demanda")],
   [t("Its risk", "Su riesgo"), t("A bigger deficit, and it can push prices up", "Un déficit mayor, y puede empujar los precios al alza"), t("It can brake too hard and cause unemployment", "Puede frenar de más y provocar desempleo")]])}
{C.caja("ojo", t("Here there is real disagreement, and the course does not settle it", "Aquí hay desacuerdo real, y el curso no lo resuelve"), "<p>" + t("How much to use each policy, how strongly, and when, is argued among economists and among parties, and that argument mixes technical judgments with judgments about what a government should do. What the test asks, and what this lesson asks, is that you recognize <strong>which direction a measure pushes</strong>: does it put money into circulation or take it out? That is description, and it can be done without taking a side.", "Cuánto conviene usar cada política, con qué intensidad y en qué momento se discute entre economistas y entre partidos, y esa discusión mezcla juicios técnicos con juicios sobre lo que debe hacer un gobierno. Lo que pide el examen, y lo que pide esta lección, es reconocer <strong>en qué dirección empuja una medida</strong>: ¿pone dinero en circulación o lo retira? Eso es descripción, y se puede hacer sin tomar partido.") + "</p>")}
{P(t("Practice 4 · Direction", "Práctica 4 · Dirección"), t("The government cuts taxes. Which direction does that measure push?", "El gobierno baja los impuestos. ¿En qué dirección empuja esa medida?"),
   [t("Expansionary", "Expansiva"), t("Contractionary", "Restrictiva"), t("Neither", "En ninguna")], 0,
   {1: t("People keep more money to spend.", "La gente se queda con más dinero para gastar."), 2: t("It does push.", "Sí empuja.")}, t("More money in circulation: expansionary.", "Más dinero en circulación: expansiva."))}
{C.enlace(N, t("direction", "direccion"), t("Speed up or slow down?", "¿Acelerar o frenar?"), t("Decide which direction each measure pushes.", "Decida en qué dirección empuja cada medida."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK). You may use the calculator.",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SSP.6.b", "2", t("Look at the graph of federal spending in section 1. Which statement is supported by the graph?", "Mire la gráfica del gasto federal de la sección 1. ¿Qué afirmación respalda la gráfica?"),
   [t("In 2026 the government spent more on interest on the debt than on defense.", "En 2026 el gobierno gastó más en intereses de la deuda que en defensa."), t("Defense was the largest single category.", "La defensa fue la categoría individual más grande."), t("Medicaid cost more than Social Security.", "Medicaid costó más que el Seguro Social."), t("Interest on the debt was less than 5% of spending.", "Los intereses de la deuda fueron menos del 5 % del gasto.")], 0,
   {1: t("Social Security was larger.", "El Seguro Social fue mayor."), 2: t("9.8% is less than 22.4%.", "9.8 % es menos que 22.4 %."), 3: t("It was 15.4%.", "Fue el 15.4 %.")},
   t("15.4% is more than 12.4%.", "15.4 % es más que 12.4 %."))}
{G(2, "SSP.10.a", "2", t("<em>A family earns $3,000 a month and spends $2,400 on goods with an 8% sales tax.</em><br>What percent of the family’s income goes to sales tax?", "<em>Una familia gana $3,000 al mes y gasta $2,400 en productos con un impuesto sobre las ventas del 8 %.</em><br>¿Qué porcentaje del ingreso de la familia se va en impuesto sobre las ventas?"),
   ["6.4%", "8%", "$192", "80%"], 0,
   {1: t("That is the rate on purchases, not on income.", "Esa es la tasa sobre las compras, no sobre el ingreso."), 2: t("That is the tax in dollars; now divide by income.", "Ese es el impuesto en dólares; ahora divida entre el ingreso."), 3: t("That is the share of income spent.", "Esa es la parte del ingreso que se gasta.")},
   t("$2,400 × 0.08 = $192; 192 ÷ 3,000 = 0.064 = 6.4%.", "$2,400 × 0.08 = $192; 192 ÷ 3,000 = 0.064 = 6.4 %."))}
{G(3, "SSP.4.a", "2", t("<em>A news report says: “The federal deficit fell this year.”</em><br>What does this mean?", "<em>Una noticia dice: «El déficit federal bajó este año».</em><br>¿Qué significa?"),
   [t("The government overspent by less this year than last year, but the debt still grew.", "El gobierno gastó de más menos que el año pasado, pero la deuda siguió creciendo."), t("The national debt got smaller.", "La deuda nacional se hizo más pequeña."), t("The government collected more than it spent.", "El gobierno recaudó más de lo que gastó."), t("Taxes went down.", "Los impuestos bajaron.")], 0,
   {1: t("Only a surplus lowers the debt.", "Solo un superávit baja la deuda."), 2: t("That would be a surplus.", "Eso sería un superávit."), 3: t("The report says nothing about taxes.", "La noticia no dice nada de impuestos.")},
   t("A deficit is yearly; the debt is the total.", "El déficit es anual; la deuda es el total."))}
{G(4, "SSP.3.c", "2–3", t("<em>Unemployment has risen to 9%, and many stores are closing. Congress passes a plan to build roads and bridges and to send a tax rebate to families.</em><br>What is the plan most likely meant to do?", "<em>El desempleo ha subido al 9 % y muchas tiendas están cerrando. El Congreso aprueba un plan para construir carreteras y puentes y enviar una devolución de impuestos a las familias.</em><br>¿Qué busca con más probabilidad el plan?"),
   [t("Put more money into the economy to support spending and jobs", "Poner más dinero en la economía para sostener el consumo y el empleo"), t("Slow down an economy that is growing too fast", "Frenar una economía que crece demasiado deprisa"), t("Reduce the national debt", "Reducir la deuda nacional"), t("Raise prices", "Subir los precios")], 0,
   {1: t("The economy is cooling, not overheating.", "La economía se está enfriando, no recalentando."), 2: t("More spending and lower taxes usually add to the debt.", "Más gasto y menos impuestos suelen sumar a la deuda."), 3: t("Higher prices are a risk, not the goal.", "La subida de precios es un riesgo, no el objetivo.")},
   t("Expansionary policy near a trough.", "Política expansiva cerca de un valle."))}
{G(5, "SSP.7.b", "3", t("Which statement is an informed claim supported by the information in this lesson, rather than an unsupported claim?", "¿Qué afirmación está fundamentada en la información de esta lección, y no es una afirmación sin respaldo?"),
   [t("If the debt keeps growing, interest will take a larger part of the federal budget.", "Si la deuda sigue creciendo, los intereses ocuparán una parte mayor del presupuesto federal."), t("Taxes on the rich are always too high.", "Los impuestos a los ricos siempre son demasiado altos."), t("Cutting taxes always ends a recession.", "Bajar los impuestos siempre acaba con una recesión."), t("The government will never pay its debt.", "El gobierno nunca pagará su deuda.")], 0,
   {1: t("“Too high” is a value judgment.", "«Demasiado altos» es un juicio de valor."), 2: t("“Always” is not supported; policies have risks.", "El «siempre» no está respaldado; las políticas tienen riesgos."), 3: t("A prediction with no evidence given.", "Una predicción sin pruebas.")},
   t("Interest is the cost of the debt; a bigger debt costs more, other things equal.", "Los intereses son el costo de la deuda; una deuda mayor cuesta más, si lo demás no cambia."))}"""

    secciones = [
        ("s1", t("From your paycheck to the federal budget", "De su nómina al presupuesto federal"), s1),
        ("s2", t("Progressive, regressive, proportional", "Progresivo, regresivo, proporcional"), s2),
        ("s3", t("Deficit and debt are not the same", "Déficit y deuda no son lo mismo"), s3),
        ("s4", t("Fiscal policy: speed up or slow down", "Política fiscal: acelerar o frenar"), s4),
        ("s5", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Your own pay stub (20 minutes).", "Su propio recibo de sueldo (20 minutos)."), t("Take a pay stub (yours or an example online) and find each line of the table in section 1. Compute each deduction as a percent of gross pay. <em>Check:</em> Social Security should be 6.2% and Medicare 1.45%.", "Tome un recibo de sueldo (el suyo o un ejemplo en internet) y busque cada línea de la tabla de la sección 1. Calcule cada retención como porcentaje del salario bruto. <em>Compruebe:</em> el Seguro Social debe ser el 6.2 % y Medicare el 1.45 %.")),
        (t("The effective rate (15 minutes).", "La tasa efectiva (15 minutos)."), t("Repeat the sales tax example with Chicago’s rate of 10.25% for two incomes of your choice. <em>Check:</em> the lower income must show the higher percent.", "Repita el ejemplo del impuesto sobre las ventas con la tasa de Chicago, del 10.25 %, para dos ingresos que usted elija. <em>Compruebe:</em> el ingreso menor debe dar el porcentaje mayor.")),
        (t("A headline, read carefully (15 minutes).", "Un titular, leído con cuidado (15 minutos)."), t("Find a news story about the deficit or the debt. Write which of the two it is about and what that means for the other. <em>Check:</em> if it says the deficit fell, the debt still rose.", "Busque una noticia sobre el déficit o la deuda. Escriba de cuál de los dos habla y qué significa eso para el otro. <em>Compruebe:</em> si dice que el déficit bajó, la deuda siguió subiendo.")),
    ]
    Q = t
    quiz = [
        (Q("Which tax takes a higher percent as income rises?", "¿Qué impuesto se lleva un porcentaje mayor a medida que sube el ingreso?"), [Q("A progressive tax", "Un impuesto progresivo"), Q("A regressive tax", "Un impuesto regresivo"), Q("A proportional tax", "Un impuesto proporcional"), Q("A sales tax", "Un impuesto sobre las ventas")], 0, {1: Q("That one falls.", "Ese baja."), 2: Q("That one stays the same.", "Ese se mantiene."), 3: Q("That one is regressive.", "Ese es regresivo.")}, Q("Progressive: the percent rises.", "Progresivo: el porcentaje sube.")),
        (Q("Illinois taxes every income at 4.95%. That tax is…", "Illinois grava todo ingreso al 4.95 %. Ese impuesto es…"), [Q("proportional", "proporcional"), Q("progressive", "progresivo"), Q("regressive", "regresivo"), Q("a tariff", "un arancel")], 0, {1: Q("The rate does not rise.", "La tasa no sube."), 2: Q("The rate does not fall.", "La tasa no baja."), 3: Q("No.", "No.")}, Q("The same percent for everyone.", "El mismo porcentaje para todos.")),
        (Q("Why is the Social Security tax regressive?", "¿Por qué es regresivo el impuesto del Seguro Social?"), [Q("It stops at a wage cap, so the effective rate falls for high incomes", "Se detiene en un tope salarial, así que la tasa efectiva baja para los ingresos altos"), Q("Its rate is higher for the poor", "Su tasa es mayor para los pobres"), Q("Only the rich pay it", "Solo lo pagan los ricos"), Q("It is a sales tax", "Es un impuesto sobre las ventas")], 0, {1: Q("The printed rate is 6.2% for all.", "La tasa impresa es 6.2 % para todos."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("$184,500 cap in 2026.", "Tope de $184,500 en 2026.")),
        (Q("About what share of federal revenue comes from individual income and payroll taxes?", "¿Qué parte, aproximadamente, de los ingresos federales sale de la renta de las personas y de las retenciones de nómina?"), [Q("About 86%", "Alrededor del 86 %"), Q("About 50%", "Alrededor del 50 %"), Q("About 25%", "Alrededor del 25 %"), Q("About 7%", "Alrededor del 7 %")], 0, {1: Q("That is the income tax alone.", "Esa es solo la renta."), 2: Q("No.", "No."), 3: Q("That is corporate tax.", "Ese es el impuesto de sociedades.")}, Q("52.7% + 33.5%.", "52.7 % + 33.5 %.")),
        (Q("Which was larger in 2026?", "¿Qué fue mayor en 2026?"), [Q("Interest on the debt", "Los intereses de la deuda"), Q("Defense", "La defensa"), Q("They were equal", "Fueron iguales"), Q("Neither was in the budget", "Ninguno estaba en el presupuesto")], 0, {1: Q("12.4% vs 15.4%.", "12.4 % frente a 15.4 %."), 2: Q("No.", "No."), 3: Q("Both were.", "Los dos estaban.")}, Q("Interest: 15.4%.", "Intereses: 15.4 %.")),
        (Q("Which item on a paycheck goes to the state, not to the federal government?", "¿Qué línea de una nómina va al estado, y no al gobierno federal?"), [Q("The Illinois income tax", "El impuesto de Illinois sobre la renta"), Q("Social Security", "El Seguro Social"), Q("Medicare", "Medicare"), Q("Federal withholding", "La retención federal")], 0, {1: Q("Federal.", "Federal."), 2: Q("Federal.", "Federal."), 3: Q("Federal.", "Federal.")}, Q("Federalism on a pay stub.", "El federalismo en un recibo.")),
        (Q("The deficit is…", "El déficit es…"), [Q("how much more is spent than collected in one year", "cuánto se gasta de más de lo que se recauda en un año"), Q("the total owed", "el total que se debe"), Q("the interest on the debt", "los intereses de la deuda"), Q("a tax on imports", "un impuesto a las importaciones")], 0, {1: Q("That is the debt.", "Esa es la deuda."), 2: Q("No.", "No."), 3: Q("That is a tariff.", "Eso es un arancel.")}, Q("One year.", "Un año.")),
        (Q("What has to happen for the debt to go down?", "¿Qué tiene que ocurrir para que baje la deuda?"), [Q("A surplus", "Un superávit"), Q("A smaller deficit", "Un déficit menor"), Q("Lower interest rates", "Tipos de interés más bajos"), Q("A new President", "Un nuevo presidente")], 0, {1: Q("A smaller deficit still adds.", "Un déficit menor sigue sumando."), 2: Q("That slows the growth of interest only.", "Eso solo frena el crecimiento de los intereses."), 3: Q("No.", "No.")}, Q("Collect more than you spend.", "Recaudar más de lo que se gasta.")),
        (Q("Debt starts at 50. Deficits are 4, 6, and 3. What is the debt at the end?", "La deuda empieza en 50. Los déficits son 4, 6 y 3. ¿Cuánto es la deuda al final?"), ["63", "53", "13", "50"], 0, {1: Q("That adds only the last deficit.", "Eso suma solo el último déficit."), 2: Q("That is only the deficits.", "Eso son solo los déficits."), 3: Q("Every deficit adds.", "Todo déficit suma.")}, Q("50 + 4 + 6 + 3 = 63.", "50 + 4 + 6 + 3 = 63.")),
        (Q("Raising taxes to cool an overheated economy is…", "Subir los impuestos para enfriar una economía recalentada es…"), [Q("contractionary fiscal policy", "política fiscal restrictiva"), Q("expansionary fiscal policy", "política fiscal expansiva"), Q("a deficit", "un déficit"), Q("a tariff", "un arancel")], 0, {1: Q("That speeds up.", "Eso acelera."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("Takes money out of circulation.", "Retira dinero de circulación.")),
        (Q("The lowest point of the business cycle is the…", "El punto más bajo del ciclo económico es el…"), [Q("trough", "valle"), Q("peak", "pico"), Q("expansion", "expansión"), Q("surplus", "superávit")], 0, {1: Q("Highest point.", "El punto más alto."), 2: Q("Rising phase.", "Fase de subida."), 3: Q("No.", "No.")}, Q("Trough.", "Valle.")),
        (Q("Which is a main risk of expansionary policy?", "¿Cuál es un riesgo principal de la política expansiva?"), [Q("A bigger deficit and rising prices", "Un déficit mayor y la subida de precios"), Q("Higher unemployment", "Más desempleo"), Q("A surplus", "Un superávit"), Q("Lower spending", "Menos gasto")], 0, {1: Q("That is the risk of braking too hard.", "Ese es el riesgo de frenar de más."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("More money in circulation.", "Más dinero en circulación.")),
    ]
    filas = [
        (t("Read where the money comes from and goes", "Lee de dónde sale el dinero y adónde va"), t("I read both graphs and explain why interest buys no service.", "Leo las dos gráficas y explico por qué los intereses no compran ningún servicio."), t("I read the graphs but miss the connection with the debt.", "Leo las gráficas, pero no veo la conexión con la deuda."), t("I do not know where federal money comes from (<a href=\"#s1\">review section 1</a>).", "No sé de dónde sale el dinero federal (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Classify a tax", "Clasifica un impuesto"), t("I classify by the effective rate on income, including the Social Security case.", "Clasifico por la tasa efectiva sobre el ingreso, incluido el caso del Seguro Social."), t("I classify by the printed rate.", "Clasifico por la tasa impresa."), t("I mix up the three words (<a href=\"#s2\">review section 2</a>).", "Confundo las tres palabras (<a href=\"#s2\">repase la sección 2</a>).")),
        (t("Tell deficit from debt", "Distingue déficit de deuda"), t("I explain why a smaller deficit still raises the debt.", "Explico por qué un déficit menor sigue subiendo la deuda."), t("I know the definitions but fall for headlines.", "Sé las definiciones, pero caigo con los titulares."), t("I use them as the same word (<a href=\"#s3\">review section 3</a>).", "Las uso como si fueran lo mismo (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Recognize the direction of a measure", "Reconoce la dirección de una medida"), t("I say whether a measure puts money in or takes it out, and when each is used.", "Digo si una medida pone o retira dinero, y cuándo se usa cada una."), t("I know the names but mix up the cases.", "Sé los nombres, pero confundo los casos."), t("I do not know what fiscal policy is (<a href=\"#s4\">review section 4</a>).", "No sé qué es la política fiscal (<a href=\"#s4\">repase la sección 4</a>).")),
    ]
    cierre = ("<p>" + t("This lesson followed the money: from a paycheck to the federal budget, through the three shapes a tax can take, to the difference between a year’s deficit and the accumulated debt, and finally to the two directions of fiscal policy. The main habit it asks for is the same as in Topic 2: always ask what a number is being divided by. A tax rate against the purchase and against income are two different stories.",
                     "Esta lección siguió al dinero: de una nómina al presupuesto federal, por las tres formas que puede tener un impuesto, hasta la diferencia entre el déficit de un año y la deuda acumulada, y por último a las dos direcciones de la política fiscal. El hábito principal que pide es el mismo del Tema 2: preguntarse siempre entre qué se está dividiendo. Una tasa contra la compra y contra el ingreso cuentan dos historias distintas.") + "</p><p>" +
              t("This ends Topic 5 and the civics block. Topic 6 changes the question: no longer how government works, but why it came to be this way. That is U.S. history, read as cause and change.",
                "Con esto termina el Tema 5 y el bloque de cívica. El Tema 6 cambia de pregunta: ya no cómo funciona el gobierno, sino por qué llegó a ser así. Es la historia de los Estados Unidos, leída como causalidad y cambio.") + "</p>")
    glosario = [
        (t("Progressive tax", "Impuesto progresivo"), t("A tax that takes a higher percent of income as income rises.", "Impuesto que se lleva un porcentaje mayor del ingreso a medida que este sube.")),
        (t("Proportional (flat) tax", "Impuesto proporcional"), t("A tax that takes the same percent of every income.", "Impuesto que se lleva el mismo porcentaje de cualquier ingreso.")),
        (t("Regressive tax", "Impuesto regresivo"), t("A tax that takes a lower percent of income as income rises.", "Impuesto que se lleva un porcentaje menor del ingreso a medida que este sube.")),
        (t("Effective rate", "Tasa efectiva"), t("The tax paid as a percent of total income.", "El impuesto pagado como porcentaje del ingreso total.")),
        (t("Deficit", "Déficit"), t("How much more the government spends than it collects in one year.", "Cuánto gasta el gobierno de más de lo que recauda en un año.")),
        (t("Surplus", "Superávit"), t("How much more the government collects than it spends in one year.", "Cuánto recauda el gobierno de más de lo que gasta en un año.")),
        (t("Debt", "Deuda"), t("The total the government owes, the sum of past deficits minus surpluses.", "Lo que el gobierno debe en total: la suma de los déficits pasados menos los superávits.")),
        (t("Fiscal policy", "Política fiscal"), t("Using taxes and government spending to influence the economy.", "Uso de los impuestos y del gasto público para influir en la economía.")),
    ]
    estd = C.estandares(["SSP.3.c", "SSP.4.a", "SSP.6.b", "SSP.7.b", "SSP.10.a"], ["CG.f", "E.e", "E.f"], base=["SSP.6.a", "SSP.11.a"])
    conexion = "<p>" + t("The two previous lessons were about rights and votes. This one is about money, which is where political decisions stop being statements and become numbers. And it starts where all this stops being abstract for anyone who works: on a paycheck.",
                         "Las dos lecciones anteriores trataron de derechos y de votos. Esta trata del dinero, que es donde las decisiones políticas dejan de ser declaraciones y se convierten en cifras. Y empieza donde todo esto deja de ser abstracto para cualquiera que trabaje: en una nómina.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("A tax is measured against income, not the purchase; and a smaller deficit still makes the debt grow.", "Un impuesto se mide contra el ingreso, no contra la compra; y un déficit menor sigue haciendo crecer la deuda."),
        ["SSP.6 · " + t("Reading budget graphs", "Leer gráficas de presupuesto"), "SSP.10 · " + t("Percents of income", "Porcentajes del ingreso"), "SSP.3 · " + t("Cause and effect", "Causa y efecto")],
        [t("<strong>Tell apart</strong> a progressive, a regressive, and a proportional tax, and classify real examples.", "<strong>Distinguir</strong> un impuesto progresivo de uno regresivo y de uno proporcional, y clasificar ejemplos reales."),
         t("<strong>Read</strong> where federal revenue comes from and where spending goes.", "<strong>Leer</strong> de dónde salen los ingresos federales y adónde va el gasto."),
         t("<strong>Explain</strong> the difference between deficit and debt.", "<strong>Explicar</strong> la diferencia entre déficit y deuda."),
         t("<strong>Tell apart</strong> expansionary and contractionary fiscal policy.", "<strong>Distinguir</strong> una política fiscal expansiva de una restrictiva.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("6-1", t("Colonies, the Revolution, and building a nation", "Colonias, Revolución y construcción de la nación")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- la práctica
def casos_impuestos():
    G = [t("Progressive", "Progresivo"), t("Proportional", "Proporcional"), t("Regressive", "Regresivo")]
    PI = [t("Does the percent of income go up as income rises?", "¿Sube el porcentaje del ingreso al subir el ingreso?"), t("Is it the same percent of every income?", "¿Es el mismo porcentaje para cualquier ingreso?"), t("Does a person who earns less pay a larger share of income?", "¿Paga una parte mayor de su ingreso quien gana menos?")]
    def caso(tit, piezas):
        return {"titulo": tit, "intro": t("Classify each tax by the effective rate on income, not by the printed rate.", "Clasifique cada impuesto por la tasa efectiva sobre el ingreso, no por la tasa impresa."), "grupos": G, "etiqueta": t("This tax is…", "Este impuesto es…"),
                "piezas": [{"t": a, "v": v, "pista": PI[v]} for a, v in piezas]}
    return [
        caso(t("Set 1", "Serie 1"), [(t("The federal income tax, with its brackets", "El impuesto federal sobre la renta, con sus tramos"), 0), (t("The sales tax", "El impuesto sobre las ventas"), 2),
                                      (t("Illinois’s 4.95% income tax", "El impuesto de Illinois sobre la renta, del 4.95 %"), 1), (t("The Social Security tax, 6.2% up to a wage cap", "La retención del Seguro Social, del 6.2 % hasta un tope salarial"), 2)]),
        caso(t("Set 2", "Serie 2"), [(t("The gasoline tax, a fixed amount per gallon", "El impuesto sobre la gasolina, una cantidad fija por galón"), 2), (t("The basic Medicare tax, 1.45% of every dollar", "La retención básica de Medicare, del 1.45 % de cada dólar"), 1),
                                      (t("The federal estate tax, paid only on very large inheritances", "El impuesto federal sobre herencias, que solo pagan las herencias muy grandes"), 0), (t("A tax of a fixed amount on each pack of cigarettes", "Un impuesto de una cantidad fija por cada cajetilla de cigarrillos"), 2)]),
    ]


def banco_direccion():
    E, R, Nn = t("Expansionary (speeds up)", "Expansiva (acelera)"), t("Contractionary (slows down)", "Restrictiva (frena)"), t("Neither: it is not fiscal policy", "Ninguna: no es política fiscal")
    D = [(t("Congress cuts income taxes for all families.", "El Congreso baja el impuesto sobre la renta a todas las familias."), 0, t("People keep more money to spend.", "La gente se queda con más dinero para gastar.")),
         (t("The government builds new highways during a recession.", "El gobierno construye autopistas nuevas durante una recesión."), 0, t("More government spending puts money in circulation.", "Más gasto público pone dinero en circulación.")),
         (t("Congress raises income taxes when prices are rising fast.", "El Congreso sube el impuesto sobre la renta cuando los precios suben deprisa."), 1, t("Takes money out of circulation.", "Retira dinero de circulación.")),
         (t("The government cuts spending on new projects to cool the economy.", "El gobierno recorta el gasto en proyectos nuevos para enfriar la economía."), 1, t("Less spending, less demand.", "Menos gasto, menos demanda.")),
         (t("Families receive a one-time payment from the Treasury.", "Las familias reciben un pago único del Tesoro."), 0, t("A transfer puts money in people’s hands.", "Una transferencia pone dinero en manos de la gente.")),
         (t("Congress ends a temporary tax cut early because the economy is overheating.", "El Congreso termina antes de tiempo una rebaja temporal de impuestos porque la economía se recalienta."), 1, t("Taxes go back up: money is taken out.", "Los impuestos vuelven a subir: se retira dinero.")),
         (t("A company raises the prices of its own products.", "Una empresa sube los precios de sus propios productos."), 2, t("Fiscal policy is government taxes and spending.", "La política fiscal son los impuestos y el gasto del gobierno.")),
         (t("A state changes the color of its license plates.", "Un estado cambia el color de sus placas de matrícula."), 2, t("No change in taxes or spending.", "No cambian ni impuestos ni gasto."))]
    ops = [E, R, Nn]
    return [{"enun": "<strong>" + s + "</strong><br>" + t("Which direction does this push?", "¿En qué dirección empuja?"), "ops": [ops[k]] + [o for i, o in enumerate(ops) if i != k], "ok": 0, "exp": e} for s, k, e in D]


def tx():
    return {"carga": t("A person earns ${i} a month and spends ${g} on goods with a {r}% sales tax. What percent of the person’s <strong>income</strong> goes to sales tax?", "Una persona gana ${i} al mes y gasta ${g} en productos con un impuesto sobre las ventas del {r} %. ¿Qué porcentaje de su <strong>ingreso</strong> se va en impuesto sobre las ventas?"),
            "pidePct": t("Write the percent as a number, rounded to one decimal (for example, 6.4).", "Escriba el porcentaje como número, redondeado a un decimal (por ejemplo, 6.4)."),
            "esDolares": t("That is the tax in dollars. Now divide it by the income and multiply by 100.", "Ese es el impuesto en dólares. Ahora divídalo entre el ingreso y multiplique por 100."),
            "esTasa": t("That is the rate on purchases. The question asks for the percent of income.", "Esa es la tasa sobre las compras. La pregunta pide el porcentaje del ingreso."),
            "cargaP": t("First the tax: spending × rate. Then tax ÷ income × 100.", "Primero el impuesto: gasto × tasa. Después impuesto ÷ ingreso × 100."),
            "deuda": t("At the start of year 1, the debt is {d}. The deficits of the next years are {l}. What is the debt at the end?", "Al empezar el año 1, la deuda es {d}. Los déficits de los años siguientes son {l}. ¿Cuánto es la deuda al final?"),
            "unidades": t("(In billions of dollars.)", "(En miles de millones de dólares)."),
            "soloDef": t("That is only the sum of the deficits. Add them to the starting debt.", "Eso es solo la suma de los déficits. Súmela a la deuda inicial."),
            "ultimo": t("You added only one deficit. Every deficit adds to the debt.", "Solo sumó un déficit. Todos los déficits suman a la deuda."),
            "resta": t("Deficits add to the debt; they never subtract.", "Los déficits suman a la deuda; nunca restan."),
            "deudaP": t("Debt at the end = starting debt + every deficit.", "Deuda final = deuda inicial + todos los déficits."),
            "y": t(" and ", " y ")}


JS = r"""
function rd1(x){ return Math.round(x * 10) / 10; }
function gCarga(){
  var i, g, r, imp, p, intento = 0;
  do {
    i = elige([1800, 2000, 2400, 2500, 3000, 3200, 4000, 5000, 6000, 8000, 10000]);
    var parte = i <= 2500 ? elige([0.7, 0.75, 0.8]) : (i <= 5000 ? elige([0.55, 0.6, 0.65]) : elige([0.35, 0.4, 0.45]));
    g = Math.round(i * parte / 100) * 100; r = elige([5, 6, 7, 8, 9, 10]);
    imp = g * r / 100; p = imp / i * 100; intento++;
  } while (Math.abs(p * 10 - Math.round(p * 10)) > 1e-9 && intento < 200);
  p = rd1(p);
  var enun = "<p>" + TXS.carga.replace("{i}", com(i)).replace("{g}", com(g)).replace("{r}", r) + "</p><p>" + TXS.pidePct + "</p>";
  return {enun: enun, resp: leeNumero(String(p)), explica: "$" + com(g) + " × " + r + "% = $" + com(imp) + "; " + com(imp) + " ÷ " + com(i) + " × 100 = " + p + "%.",
    pista: function(x){ if (igual(x, leeNumero(String(imp)))) return TXS.esDolares; if (igual(x, leeNumero(String(r)))) return TXS.esTasa; return TXS.cargaP; }};
}
function gDeuda(){
  var d = elige([400, 500, 650, 800, 1000, 1200]), n = elige([3, 4]), l = [], s = 0, k;
  for (k = 0; k < n; k++){ var x = elige([40, 55, 60, 75, 80, 90, 110, 120, 150]); l.push(x); s += x; }
  var fin = d + s;
  var lista = l.slice(0, -1).join(", ") + TXS.y + l[l.length - 1];
  var enun = "<p>" + TXS.deuda.replace("{d}", com(d)).replace("{l}", lista) + " " + TXS.unidades + "</p>";
  return {enun: enun, resp: leeNumero(String(fin)), explica: com(d) + " + " + l.join(" + ") + " = " + com(fin) + ".",
    pista: function(x){ if (igual(x, leeNumero(String(s)))) return TXS.soloDef; if (igual(x, leeNumero(String(d + l[l.length - 1])))) return TXS.ultimo; if (igual(x, leeNumero(String(d - s)))) return TXS.resta; return TXS.deudaP; }};
}
"""


def practica():
    A = {"en": ["tax-types", "burden", "debt", "direction"], "es": ["tipos-de-impuesto", "carga", "deuda", "direccion"]}[C.L]
    mods = [
        (A[0], t("Progressive, proportional, or regressive?", "¿Progresivo, proporcional o regresivo?"), C.clasifica("m1", t("Look at the effective rate on income. If something is not right, the taxes marked in yellow get a hint.", "Mire la tasa efectiva sobre el ingreso. Si algo no está bien, los impuestos marcados en amarillo reciben una pista."))),
        (A[1], t("The real burden of a sales tax", "La carga real de un impuesto sobre las ventas"), "      <p>" + t("New numbers every time. Tax = spending × rate; then tax ÷ income × 100.", "Números nuevos cada vez. Impuesto = gasto × tasa; después impuesto ÷ ingreso × 100.") + "</p>\n" + C.dec_campo("m2", t("Percent of income", "Porcentaje del ingreso"))),
        (A[2], t("Adding up the debt", "Sumar la deuda"), "      <p>" + t("New numbers every time. Every deficit adds to the debt.", "Números nuevos cada vez. Todo déficit suma a la deuda.") + "</p>\n" + C.dec_campo("m3", t("Debt at the end", "Deuda final"))),
        (A[3], t("Speed up or slow down?", "¿Acelerar o frenar?"), C.om("m4", t("Ask: does the measure put money into circulation or take it out? And is it government taxes or spending at all?", "Pregúntese: ¿la medida pone dinero en circulación o lo retira? ¿Y se trata de impuestos o gasto del gobierno?"))),
    ]
    js = (C.js_datos("TXS", tx()) + C.js_datos("IMP", casos_impuestos()) + C.js_datos("DIR", banco_direccion()) + JS +
          'creaClasifica("m1", IMP);\ncreaPracticaDec("m2", gCarga);\ncreaPracticaDec("m3", gDeuda);\ncreaBanco("m4", DIR);\n')
    return C.pagina_practica(N, titulo(), t("Four activities · new exercises every time · two tries in each one · calculator included", "Cuatro actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"), mods, js,
                             scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
