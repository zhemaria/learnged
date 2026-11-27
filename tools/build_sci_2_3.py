"""LearnGED · Ciencias · Lección 2.3 · Estadística y probabilidad de datos experimentales (EN/ES).
Fuente: clases_ciencias/leccion_2-3.html y los interactivos ciencias/estadistica (CientíEstad) y ciencias/arbol_probabilidad.
Uso: python3 tools/build_sci_2_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "2-3"


def titulo():
    return t("Statistics and probability with experimental data", "Estadística y probabilidad de datos experimentales")


def anc(en, es):
    return en if C.L == "en" else es


def caja_svg():
    """Diagrama de caja de las diez mediciones de la hoja: 84, 87, 88, 90, 95 mm."""
    x0, x1, v0, v1 = 60, 520, 82, 97
    X = lambda v: x0 + (v - v0) / (v1 - v0) * (x1 - x0)
    g = []
    for v in range(82, 98, 2):
        g.append(f'<line x1="{X(v):.0f}" y1="128" x2="{X(v):.0f}" y2="134" stroke="#1a2330"/><text x="{X(v):.0f}" y="150" text-anchor="middle" font-size="13" fill="#3d4753">{v}</text>')
    g.append(f'<line x1="{x0}" y1="128" x2="{x1}" y2="128" stroke="#1a2330"/>')
    g.append(f'<line x1="{X(84):.0f}" y1="70" x2="{X(87):.0f}" y2="70" stroke="#1a2330" stroke-width="2"/><line x1="{X(90):.0f}" y1="70" x2="{X(95):.0f}" y2="70" stroke="#1a2330" stroke-width="2"/>')
    g.append(f'<line x1="{X(84):.0f}" y1="56" x2="{X(84):.0f}" y2="84" stroke="#1a2330" stroke-width="2"/><line x1="{X(95):.0f}" y1="56" x2="{X(95):.0f}" y2="84" stroke="#1a2330" stroke-width="2"/>')
    g.append(f'<rect x="{X(87):.0f}" y="46" width="{X(90) - X(87):.0f}" height="48" fill="#e3f3f4" stroke="#1f6066" stroke-width="2"/><line x1="{X(88):.0f}" y1="46" x2="{X(88):.0f}" y2="94" stroke="#b5342a" stroke-width="4"/>')
    for v, n in ((84, t("min", "mín.")), (87, "Q1"), (88, t("median", "mediana")), (90, "Q3"), (95, t("max", "máx."))):
        g.append(f'<text x="{X(v):.0f}" y="{36 if v != 88 else 24}" text-anchor="middle" font-size="13" font-weight="700" fill="#1a2330">{n}</text>')
    g.append(f'<text x="{(x0 + x1) / 2:.0f}" y="172" text-anchor="middle" font-size="14" font-weight="700" fill="#1a2330">{t("Length of the leaf (mm)", "Longitud de la hoja (mm)")}</text>')
    aria = t("Box plot of the ten measurements of the leaf. Minimum 84, first quartile 87, median 88, third quartile 90, maximum 95 millimeters. The box goes from 87 to 90. The left whisker goes from 84 to 87, and the right whisker, much longer, from 90 to 95.",
             "Diagrama de caja de las diez mediciones de la hoja. Mínimo 84, primer cuartil 87, mediana 88, tercer cuartil 90, máximo 95 milímetros. La caja va de 87 a 90. El bigote izquierdo va de 84 a 87, y el derecho, mucho más largo, de 90 a 95.")
    return f'<svg viewBox="0 0 580 180" role="img" aria-label="{aria}" style="width:100%;max-width:580px;height:auto;display:block;margin:12px auto;">{"".join(g)}</svg>'


def arbol_svg():
    """Árbol de tres genes con dos alelos: 8 gametos."""
    g = []
    hojas = []
    def nodo(x, y, txt):
        g.append(f'<circle cx="{x}" cy="{y}" r="15" fill="#fff" stroke="#1f6066" stroke-width="2"/><text x="{x}" y="{y + 5}" text-anchor="middle" font-size="14" font-weight="700" fill="#1a2330">{txt}</text>')
    xs = [60, 200, 340, 480]
    for a, ya in (("A", 105), ("a", 265)):
        g.append(f'<line x1="20" y1="185" x2="{xs[0] - 15}" y2="{ya}" stroke="#90a4ae" stroke-width="2"/>')
        for b, yb in (("B", ya - 40), ("b", ya + 40)):
            g.append(f'<line x1="{xs[0] + 15}" y1="{ya}" x2="{xs[1] - 15}" y2="{yb}" stroke="#90a4ae" stroke-width="2"/>')
            for c, yc in (("C", yb - 18), ("c", yb + 18)):
                g.append(f'<line x1="{xs[1] + 15}" y1="{yb}" x2="{xs[2] - 15}" y2="{yc}" stroke="#90a4ae" stroke-width="2"/>')
                nodo(xs[2], yc, c)
                g.append(f'<text x="{xs[3]}" y="{yc + 5}" font-size="15" font-weight="700" fill="#1f6066">{a}{b}{c}</text>')
                hojas.append(a + b + c)
            nodo(xs[1], yb, b)
        nodo(xs[0], ya, a)
    g.append(f'<text x="{xs[0]}" y="22" text-anchor="middle" font-size="13" fill="#5b6675">{t("Gene 1", "Gen 1")}</text><text x="{xs[1]}" y="22" text-anchor="middle" font-size="13" fill="#5b6675">{t("Gene 2", "Gen 2")}</text><text x="{xs[2]}" y="22" text-anchor="middle" font-size="13" fill="#5b6675">{t("Gene 3", "Gen 3")}</text><text x="{xs[3] + 18}" y="22" text-anchor="middle" font-size="13" fill="#5b6675">{t("Gamete", "Gameto")}</text>')
    aria = t("Tree diagram with three genes, each with two alleles. Gene 1 gives A or a; each branch splits into B or b; each of those splits into C or c. There are 8 gametes at the end: ", "Diagrama de árbol con tres genes de dos alelos. El gen 1 da A o a; cada rama se divide en B o b; y cada una de esas, en C o c. Al final hay 8 gametos: ") + ", ".join(hojas) + "."
    return f'<svg viewBox="0 0 560 348" role="img" aria-label="{aria}" style="width:100%;max-width:560px;height:auto;display:block;margin:12px auto;">{"".join(g)}</svg>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("The first three measures tell where the <strong>center</strong> of the data is; the fourth, how <strong>spread out</strong> they are. None of them replaces the others, and the test often asks about the one you least expect.", "Las tres primeras medidas indican dónde está el <strong>centro</strong> de los datos; la cuarta, cuánto se <strong>dispersan</strong>. Ninguna sustituye a las demás, y el examen suele preguntar precisamente por la que menos se espera.")}</p>
{C.tabla(t("The four measures that summarize a data set, how to find each one, and when it fits best", "Las cuatro medidas de resumen de un conjunto de datos, cómo se obtiene cada una y cuándo conviene"),
 [t("Measure", "Medida"), t("How to find it", "Cómo se obtiene"), t("When to use it", "Cuándo conviene usarla")],
 [[t("Mean (average)", "Media (promedio)"), t("Add all the values and divide by how many there are.", "Se suman todos los valores y se divide entre la cantidad de datos."), t("When the data are even, with no extreme values. It uses all the information, but it is the most fragile.", "Cuando los datos son parejos y sin valores extremos. Es la más informativa, pero también la más frágil.")],
  [t("Median", "Mediana"), t("Put the data in order and take the middle value. With an even count, average the two middle values.", "Se ordenan los datos y se toma el valor central. Con una cantidad par, el promedio de los dos centrales."), t("When there is an outlier. The median is not pulled by it.", "Cuando hay un valor atípico. La mediana no se deja arrastrar por él.")],
  [t("Mode", "Moda"), t("The value that appears most often. There may be more than one, or none.", "El valor que más se repite. Puede haber más de una, o ninguna."), t("With data that are not numbers (flower color, blood type) and with measurements that repeat a lot.", "Con datos no numéricos —color de flor, tipo de sangre— y con mediciones muy repetidas.")],
  [t("Range", "Rango"), t("Subtract the smallest value from the largest.", "Se resta el valor menor del mayor."), t("To show at a glance how much the data vary. It says nothing about how the values in between are spread.", "Para expresar de un vistazo cuánta variabilidad hay. No dice nada sobre los datos intermedios.")]])}
{C.ejemplo(t("Example 1 · The four measures on one data set", "Ejemplo 1 · Las cuatro medidas sobre un mismo conjunto"),
 [("", t("A group measured the length of the same leaf ten times, in millimeters: 84, 86, 87, 87, 87, 89, 89, 90, 91, and 95.", "Un grupo midió diez veces la longitud de una misma hoja, en milímetros: 84, 86, 87, 87, 87, 89, 89, 90, 91 y 95.")),
  ("1", t("<strong>Mean:</strong> the sum is 885 and there are 10 values, so the mean is <strong>88.5 mm</strong>.", "<strong>Media:</strong> la suma es 885 y hay 10 datos, así que la media es <strong>88.5 mm</strong>.")),
  ("2", t("<strong>Median:</strong> the data are in order; the two middle values are 87 and 89, and their average is <strong>88 mm</strong>.", "<strong>Mediana:</strong> con los datos ordenados, los dos centrales son 87 y 89; su promedio es <strong>88 mm</strong>.")),
  ("3", t("<strong>Mode:</strong> 87 appears three times, more than any other: <strong>87 mm</strong>.", "<strong>Moda:</strong> el 87 aparece tres veces, más que ningún otro: <strong>87 mm</strong>.")),
  ("4", t("<strong>Range:</strong> 95 − 84 = <strong>11 mm</strong>.", "<strong>Rango:</strong> 95 − 84 = <strong>11 mm</strong>."))],
 t("<strong>What the comparison shows:</strong> the mean is larger than the median. That is no accident: the value 95, far from the rest, pulls the mean up without moving the median. If that measurement was a mistake, the median represents the real leaf better.", "<strong>Qué revela la comparación:</strong> la media es mayor que la mediana. No es casual: el 95, muy separado del resto, tira de la media hacia arriba sin afectar a la mediana. Si esa medición fue un descuido, la mediana representa mejor la hoja real."))}
{C.caja("ojo", t("The outlier and which measure to choose", "El valor atípico y la medida que se elige"), "<p>" + t("When one value is far from the others, the test often asks which measure “best represents” the data. The answer is almost always the <strong>median</strong>, and you should be able to say why: the mean uses the value of every data point, so one huge number moves it; the median only looks at the middle position, so it holds steady.", "Ante un conjunto con un dato muy separado, la pregunta del examen suele ser qué medida «representa mejor» los datos. La respuesta es casi siempre la <strong>mediana</strong>, y hay que saber explicar por qué: la media incorpora el valor de cada dato, así que un solo número desmesurado la desplaza; la mediana solo atiende a la posición central, y por eso resiste.") + "</p>")}
<p>{t("<strong>Use this data set for Try it 1 to 3:</strong> 12, 15, 15, 18, and 20.", "<strong>Use este conjunto para Pruebe 1 a 3:</strong> 12, 15, 15, 18 y 20.")}</p>
{P(t("Try it 1 · The mean", "Pruebe 1 · La media"), t("The mean of the data set is…", "La media del conjunto es…"), ["15", "16", "18"], 1,
   {0: t("15 is the median and the mode. Add all five values and divide by 5.", "15 es la mediana y la moda. Sume los cinco valores y divida entre 5."), 2: t("18 is one of the values. Add them all: 12 + 15 + 15 + 18 + 20.", "18 es uno de los valores. Súmelos todos: 12 + 15 + 15 + 18 + 20.")},
   t("12 + 15 + 15 + 18 + 20 = 80, and 80 ÷ 5 = 16.", "12 + 15 + 15 + 18 + 20 = 80, y 80 ÷ 5 = 16."))}
{P(t("Try it 2 · Median and mode", "Pruebe 2 · Mediana y moda"), t("The median and the mode of the data set are…", "La mediana y la moda del conjunto son, respectivamente…"), [t("15 and 15", "15 y 15"), t("16 and 15", "16 y 15"), t("15 and 20", "15 y 20")], 0,
   {1: t("16 is the mean, not the median. Which value is in the middle?", "16 es la media, no la mediana. ¿Qué valor está en el centro?"), 2: t("20 appears only once. Which value repeats?", "20 aparece una sola vez. ¿Qué valor se repite?")},
   t("The middle (third) value is 15, and 15 is the only value that appears twice.", "El valor central (el tercero) es 15, y 15 es el único que aparece dos veces."))}
{P(t("Try it 3 · An outlier", "Pruebe 3 · Un valor atípico"), t("If the value 96 were added to the data set, which measure would change the most?", "Si se añadiera el valor 96 al conjunto, ¿qué medida cambiaría más?"), [t("The mode", "La moda"), t("The median", "La mediana"), t("The mean", "La media")], 2,
   {0: t("15 would still appear most often.", "15 seguiría siendo el más repetido."), 1: t("The median would move only from 15 to 16.5. Which measure uses the value of every number?", "La mediana solo pasaría de 15 a 16.5. ¿Qué medida usa el valor de cada número?")},
   t("The mean would go from 16 to 176 ÷ 6 ≈ 29.3: one huge value pulls it a lot.", "La media pasaría de 16 a 176 ÷ 6 ≈ 29.3: un solo valor enorme la arrastra mucho."))}
{C.enlace(N, anc("measures", "medidas"), t("mean, median, mode, and range", "media, mediana, moda y rango"), t("New data sets every time: find the measure that is asked for.", "Conjuntos nuevos cada vez: halle la medida que se pide."))}"""

    tort = {"tipo": "barras", "xEtq": t("Shell length (cm)", "Longitud del caparazón (cm)"), "yEtq": t("Number of turtles", "Número de tortugas"), "py": 4,
            "barras": [{"etq": "80–90", "valor": 5}, {"etq": "90–100", "valor": 10}, {"etq": "100–110", "valor": 14}, {"etq": "110–120", "valor": 8}, {"etq": "120–130", "valor": 3}]}
    s2 = f"""<p>{t("A <strong>histogram</strong> groups the data into intervals and shows how many values fall in each one. The height of a bar is not a value but a <strong>frequency</strong> (how many). What you read in a histogram is, above all, the <strong>shape</strong> of the data.", "Un <strong>histograma</strong> agrupa los datos en intervalos y muestra cuántos caen en cada uno. La altura de una barra no es un valor, sino una <strong>frecuencia</strong> (cuántos). Lo que se lee en él es, sobre todo, la <strong>forma</strong> del conjunto.")}</p>
<p><strong>{t("Shell length of 40 sea turtles on a nesting beach", "Longitud del caparazón de 40 tortugas marinas en una playa de anidación")}</strong></p>
{C.grafica(tort, C.describe(tort))}
{C.tabla(t("The three things to read in a histogram, what you see, and what it means in an experiment", "Los tres elementos que se leen en un histograma, qué se observa y qué significa en un experimento"),
 [t("Element", "Elemento"), t("What you look at", "Qué se observa"), t("What it means in an experiment", "Qué significa en un experimento")],
 [[t("Shape", "Forma"), t("Whether it is symmetric, has a tail to one side, or has two peaks.", "Si es simétrico, si tiene una cola hacia un lado o si presenta dos picos."), t("Two peaks often mean two different groups were mixed and should be analyzed separately.", "Dos picos suelen indicar que se mezclaron dos grupos que convenía analizar por separado.")],
  [t("Center", "Centro"), t("Where the data pile up; around which value.", "Dónde se acumulan los datos, alrededor de qué valor."), t("The most likely value of what was measured.", "El valor más probable de la magnitud medida.")],
  [t("Spread", "Dispersión"), t("Whether the bars are in a few intervals or spread across many.", "Si las barras se concentran en pocos intervalos o se extienden por muchos."), t("How precise the procedure is: the narrower, the more repeatable.", "La precisión del procedimiento: cuanto más estrecha, más repetible la medición.")]])}"""

    s3 = f"""<p>{t("A box plot sums up a whole data set in five numbers: the <strong>minimum</strong>, the <strong>first quartile</strong> (Q1), the <strong>median</strong>, the <strong>third quartile</strong> (Q3), and the <strong>maximum</strong>. The box holds the middle half of the data; the whiskers, the ends.", "El diagrama de caja condensa un conjunto entero en cinco valores: el <strong>mínimo</strong>, el <strong>primer cuartil</strong> (Q1), la <strong>mediana</strong>, el <strong>tercer cuartil</strong> (Q3) y el <strong>máximo</strong>. La caja contiene la mitad central de los datos; los bigotes, los extremos.")}</p>
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t("<span class='raiz'>Quart-</span>, as in <em>quarter</em> and <em>quartet</em>, means four: the three <strong>quartiles</strong> split the ordered data into four parts with the same number of values each. The second quartile is the median itself. In the same family are <em>percentile</em> (one hundred parts) and <em>decile</em> (ten).", "<span class='raiz'>Cuart-</span>, como en <em>cuarto</em> y <em>cuarteto</em>, significa cuatro: los tres <strong>cuartiles</strong> dividen el conjunto ordenado en cuatro partes con la misma cantidad de datos. El segundo cuartil es la propia mediana. En la misma familia están <em>percentil</em> (cien partes) y <em>decil</em> (diez).")}</p>
{caja_svg()}
{C.tabla(t("The five numbers for the ten measurements of the leaf, with their value and meaning", "Los cinco números del resumen aplicados a las diez mediciones de la hoja"),
 [t("Number", "Número"), t("Value", "Valor"), t("What it tells you", "Qué indica")],
 [[t("Minimum", "Mínimo"), "84 mm", t("The smallest measurement.", "La medición más pequeña.")],
  [t("First quartile (Q1)", "Primer cuartil (Q1)"), "87 mm", t("One quarter of the data are below it. It is the median of the lower half: 84, 86, 87, 87, 87.", "Una cuarta parte de los datos queda por debajo. Es la mediana de la mitad inferior: 84, 86, 87, 87, 87.")],
  [t("Median", "Mediana"), "88 mm", t("Half of the data are below it and half above.", "La mitad de los datos queda por debajo y la otra mitad por encima.")],
  [t("Third quartile (Q3)", "Tercer cuartil (Q3)"), "90 mm", t("Three quarters of the data are below it. It is the median of the upper half: 89, 89, 90, 91, 95.", "Tres cuartas partes quedan por debajo. Es la mediana de la mitad superior: 89, 89, 90, 91, 95.")],
  [t("Maximum", "Máximo"), "95 mm", t("The largest measurement.", "La medición más grande.")]])}
{C.caja("tip", t("What a long whisker gives away", "Lo que delata un bigote largo"), "<p>" + t("Here the box is only 3 mm wide, while the right whisker stretches 5 mm. So the middle half of the measurements was very consistent, and one value moved away from the group. A whisker much longer than the other is the visual sign of an outlier. The first question a researcher should ask: is it a real effect or a measuring error?", "Aquí la caja mide solo 3 mm, mientras que el bigote derecho se extiende 5 mm. La mitad central de las mediciones fue muy consistente y un único dato se apartó. Un bigote mucho más largo que el otro es la señal visual de un valor atípico. La primera pregunta que debe hacerse un investigador: ¿es un fenómeno real o un error de medición?") + "</p>")}"""

    s4 = f"""<p>{t("Here we close a circle opened in Topic 1. There you studied the <strong>sources of error</strong> in a design; now you have the tools to <strong>measure</strong> them. The spread of repeated measurements is not a flaw of the experiment: it is the experiment telling you about itself.", "Aquí se cierra un círculo abierto en el Tema 1. Allí se estudiaron las <strong>fuentes de error</strong> de un diseño; ahora se tienen las herramientas para <strong>medirlas</strong>. La dispersión de mediciones repetidas no es un defecto del experimento: es su información sobre sí mismo.")}</p>
{C.tabla(t("Precision and accuracy in a set of measurements, and what each case reveals", "Precisión y exactitud en un conjunto de mediciones, y lo que revela cada situación"),
 [t("Case", "Situación"), t("What the data look like", "Qué se observa en los datos"), t("What it says about the experiment", "Qué indica sobre el experimento")],
 [[t("Precise and accurate", "Preciso y exacto"), t("Small range, with the center close to the true value.", "Rango pequeño y centro próximo al valor verdadero."), t("The procedure is repeatable and the instrument is well calibrated.", "El procedimiento es repetible y el instrumento está bien calibrado.")],
  [t("Precise but not accurate", "Preciso pero no exacto"), t("Small range, but the center is always off from the true value.", "Rango pequeño, pero el centro se aparta siempre del valor verdadero."), t("A systematic error: usually an instrument that is not calibrated and repeats the same shift every time.", "Un error sistemático: casi siempre un instrumento descalibrado que repite el mismo desvío.")],
  [t("Not precise", "Poco preciso"), t("Large range, data very spread out.", "Rango grande y datos muy dispersos."), t("Random error: the technique is not controlled, or the instrument is not sensitive enough.", "Error aleatorio: la técnica no está controlada o el instrumento no tiene la sensibilidad necesaria.")]])}
{C.caja("ojo", t("Repeating does not fix a systematic error", "Repetir no corrige un error sistemático"), "<p>" + t("More measurements reduce random error, because the ups and downs tend to cancel out. But if the scale always reads two grams too high, a thousand measurements give a mean that is still two grams too high. Repeating improves <strong>precision</strong>, not <strong>accuracy</strong>; calibration fixes accuracy.", "Aumentar el número de mediciones reduce el error aleatorio, porque los desvíos hacia arriba y hacia abajo se compensan. Pero si la balanza marca siempre dos gramos de más, mil mediciones darán una media igualmente desplazada. La repetición mejora la <strong>precisión</strong>, no la <strong>exactitud</strong>; esa la corrige la calibración.") + "</p>")}
{C.enlace(N, anc("precision", "precision"), t("precise or accurate?", "¿preciso o exacto?"), t("Six sets of measurements: find the kind of error and what would fix it.", "Seis conjuntos de mediciones: descubra el tipo de error y qué lo corregiría."))}
{C.enlace(N, anc("cientiestad", "cientiestad"), t("CientíEstad, statistics in science", "CientíEstad, estadística en ciencia"), t("Twenty-four questions from biology, chemistry, physics, and Earth science: center, spread, sampling, correlation, probability, and prediction.", "Veinticuatro preguntas de biología, química, física y ciencias de la Tierra: centro, dispersión, muestreo, correlación, probabilidad y predicción."))}"""

    s5 = f"""<p>{t("The last tool of the topic answers a different question: not what the data look like, but <strong>how many different outcomes are possible</strong>. In biology it shows up all the time, because it is the base of genetic calculations.", "La última herramienta del tema responde a otra pregunta: no cómo son los datos, sino <strong>cuántos resultados distintos son posibles</strong>. En biología aparece constantemente, porque es la base del cálculo genético.")}</p>
<h3>{t("The counting principle", "El principio fundamental del conteo")}</h3>
<p>{t("If one choice can be made in <em>m</em> ways and another, independent choice in <em>n</em> ways, both together can be made in <strong><em>m</em> × <em>n</em></strong> ways. The rule extends to as many steps as you need: multiply them all.", "Si una elección puede hacerse de <em>m</em> maneras y otra independiente de <em>n</em> maneras, ambas juntas pueden hacerse de <strong><em>m</em> × <em>n</em></strong> maneras. El principio se extiende a cuantas etapas haga falta, multiplicándolas todas.")}</p>
{arbol_svg()}
<h3>{t("Permutations and combinations", "Permutaciones y combinaciones")}</h3>
<p>{t("When you choose some items from a group, everything depends on one question: <strong>does the order matter?</strong>", "Cuando se eligen algunos elementos de un conjunto, todo depende de una sola pregunta: <strong>¿importa el orden?</strong>")}</p>
{C.tabla(t("Permutation and combination: the question that tells them apart and a science example of each", "Permutación y combinación: la pregunta que las distingue y un ejemplo científico de cada una"),
 [t("Idea", "Concepto"), t("Does the order matter?", "¿Importa el orden?"), t("Science example", "Ejemplo científico")],
 [[t("Permutation", "Permutación"), t("Yes. A different order gives a different result.", "Sí. Cambiar el orden produce un resultado distinto."), t("The steps of a lab procedure: staining then covering is not the same as covering then staining. Five steps can be put in 5 × 4 × 3 × 2 × 1 = 120 orders, and only one is right.", "Los pasos de un protocolo: colorear y después cubrir no es lo mismo que cubrir y después colorear. Cinco pasos admiten 5 × 4 × 3 × 2 × 1 = 120 ordenaciones, y solo una es correcta.")],
  [t("Combination", "Combinación"), t("No. Only which items were chosen matters.", "No. Solo importa qué elementos se eligieron."), t("Choosing 3 samples out of 8 to analyze: it does not matter which one is picked first. There are (8 × 7 × 6) ÷ (3 × 2 × 1) = 56 possible choices.", "Elegir 3 muestras de un lote de 8 para analizarlas: da igual cuál se tome primero. Hay (8 × 7 × 6) ÷ (3 × 2 × 1) = 56 selecciones posibles.")]])}
{C.ejemplo(t("Example 2 · Counting in genetics", "Ejemplo 2 · Conteo aplicado a la genética"),
 [("", t("How many different gametes (sex cells) can a living thing make if it has three genes with two alleles each?", "¿Cuántos gametos distintos puede producir un organismo con tres genes de dos alelos cada uno?")),
  ("1", t("Each gene gives a choice with two possibilities: the dominant allele or the recessive one.", "Cada gen aporta una elección con dos posibilidades: el alelo dominante o el recesivo.")),
  ("2", t("The three choices are independent, so the counting principle applies.", "Las tres elecciones son independientes, así que se aplica el principio del conteo.")),
  ("3", t("2 × 2 × 2 = <strong>8 different gametes</strong>, the eight shown by the tree.", "2 × 2 × 2 = <strong>8 gametos distintos</strong>, los ocho del diagrama de árbol."))],
 t("<strong>The general rule:</strong> with <em>n</em> genes of two alleles, the number of different gametes is 2 to the power <em>n</em>. Four genes give 16; five give 32. This count comes back in Topic 4 with genetic crosses and the Punnett square.", "<strong>La regla general:</strong> con <em>n</em> genes de dos alelos, el número de gametos distintos es 2 elevado a <em>n</em>. Con cuatro genes, 16; con cinco, 32. Esta cuenta reaparecerá en el Tema 4 con los cruces genéticos y el cuadro de Punnett."))}
{C.calc(t("nPr and nCr on the TI-30XS", "nPr y nCr en la TI-30XS"), "<p>" + t("The calculator counts for you with the <strong>prb</strong> key: choose <strong>nPr</strong> (order matters) or <strong>nCr</strong> (order does not matter). For 3 samples out of 8: type 8, prb, choose nCr, 3, enter → 56. Many students mix up P and C: P = permutation (order matters).", "La calculadora cuenta con la tecla <strong>prb</strong>: elija <strong>nPr</strong> (importa el orden) o <strong>nCr</strong> (no importa). Para 3 muestras de 8: teclee 8, prb, elija nCr, 3, enter → 56. Muchos alumnos confunden la P con la C: P = permutación (importa el orden).") + "</p>")}
{C.enlace(N, anc("counting", "conteo"), t("count the possibilities", "cuente las posibilidades"), t("Gametes, procedures, samples, and lab menus: new numbers every time. Plus: does the order matter?", "Gametos, protocolos, muestras y menús de laboratorio: números nuevos cada vez. Y además: ¿importa el orden?"))}"""

    s6 = f"""<p>{t("A short science text written for this level. Notice how the authors decide which measure to report.", "Texto científico breve adaptado al nivel. Observe cómo deciden los autores qué medida informar.")}</p>
{C.lectura(t("Ten measurements of the same piece", "Diez mediciones de una misma pieza"),
 [t("A team of students found the density of an aluminum block by repeating the measurement ten times with the same procedure. The values, in grams per cubic centimeter, were: 2.68, 2.71, 2.69, 2.70, 2.72, 2.70, 2.69, 2.71, 2.70, and 3.15.", "Un equipo de estudiantes determinó la densidad de un bloque de aluminio repitiendo la medición diez veces con el mismo procedimiento. Los valores, en gramos por centímetro cúbico, fueron: 2.68, 2.71, 2.69, 2.70, 2.72, 2.70, 2.69, 2.71, 2.70 y 3.15."),
  t("Nine of the ten were packed closely between 2.68 and 2.72. The tenth, 3.15, stood out sharply. Checking the lab notebook, the team found that this time the block had not been fully dried after being put in water, so the water stuck to it added mass without adding volume.", "Nueve de las diez se agruparon estrechamente entre 2.68 y 2.72. La décima, 3.15, se apartó de forma llamativa. Al revisar el cuaderno, el equipo halló que esa vez el bloque no se había secado del todo tras sumergirlo, de modo que el agua adherida añadió masa sin añadir volumen."),
  t("The team found both measures of center. The mean of all ten was 2.745 g/cm³; the median, 2.70 g/cm³. Leaving out the faulty measurement and averaging the other nine gave exactly 2.70 g/cm³.", "El equipo calculó las dos medidas de centro. La media de las diez fue 2.745 g/cm³; la mediana, 2.70 g/cm³. Al excluir la medición defectuosa y promediar las nueve restantes, se obtuvo exactamente 2.70 g/cm³."),
  t("The report gave the median as the result, with a note that recorded the discarded measurement and why it was discarded. The team argued that removing a value without a record would have been manipulation, while removing it with a written reason is part of the scientific procedure.", "En el informe se consignó la mediana como resultado, con una nota que documentaba la medición descartada y el motivo. El equipo argumentó que eliminar un dato sin dejar constancia habría sido una manipulación, mientras que eliminarlo dejando constancia del motivo es parte del procedimiento científico.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("Why does the median match the value found after leaving out the faulty measurement?", "¿Por qué la mediana coincide con el valor obtenido al descartar la medición defectuosa?"),
   [t("Because the median always equals the mean", "Porque la mediana siempre es igual a la media"), t("Because 3.15 was actually correct", "Porque el valor 3.15 era en realidad correcto"), t("Because the median uses the middle position, not each value, so the outlier does not move it", "Porque la mediana atiende a la posición central y no al valor de cada dato, de modo que el atípico no la desplaza")], 2,
   {0: t("Here the mean (2.745) and the median (2.70) are different.", "Aquí la media (2.745) y la mediana (2.70) son distintas."), 1: t("The text explains that 3.15 came from a wet block.", "El texto explica que 3.15 se debió al bloque mojado.")},
   t("The median only cares which value is in the middle; 3.15 sits at the end of the ordered list and does not move it.", "La mediana solo atiende a qué valor queda en el centro; 3.15 queda al final de la lista ordenada y no la mueve."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("The range of the ten measurements is…", "El rango de las diez mediciones es de…"), ["0.47 g/cm³", "0.04 g/cm³", "2.745 g/cm³"], 0,
   {1: t("0.04 is the range of the nine good values. Include 3.15.", "0.04 es el rango de las nueve buenas. Incluya 3.15."), 2: t("2.745 is the mean, not the range.", "2.745 es la media, no el rango.")},
   t("3.15 − 2.68 = 0.47 g/cm³.", "3.15 − 2.68 = 0.47 g/cm³."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("The 3.15 measurement is…", "La medición de 3.15 corresponde a…"),
   [t("a systematic error, present in every measurement", "un error sistemático, presente en todas las mediciones"), t("a one-time error whose cause was found", "un error puntual, cuya causa concreta se identificó"), t("the normal variation of any measurement", "la variación natural esperable en toda medición")], 1,
   {0: t("A systematic error would shift all ten. Here only one is off.", "Un error sistemático desplazaría las diez. Aquí solo una se aparta."), 2: t("Normal variation is like 2.68 to 2.72. 3.15 is far outside that.", "La variación natural es como de 2.68 a 2.72. 3.15 queda muy fuera.")},
   t("Only one measurement was off, and the team found why (the wet block).", "Solo una medición se apartó, y el equipo encontró la causa (el bloque mojado)."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("According to the text, what makes leaving out a value legitimate instead of manipulation?", "Según el texto, ¿qué distingue un descarte legítimo de una manipulación?"),
   [t("That the discarded value is the largest", "Que el dato descartado sea el mayor"), t("That more than one value is discarded at a time", "Que se descarte más de un dato a la vez"), t("That the discard and its reason are written down", "Que quede documentado el descarte y su motivo")], 2,
   {0: t("Being the largest is not a reason by itself.", "Ser el mayor no es motivo por sí solo."), 1: t("The number of values discarded is not the point.", "El número de datos descartados no es lo importante.")},
   t("The last paragraph: removing it with a written reason is part of the procedure.", "Último párrafo: eliminarlo dejando constancia del motivo es parte del procedimiento."))}
{P(t("Try it 4 · The box", "Pruebe 4 · La caja"), t("In the leaf box plot, what part of the data is inside the box?", "En el diagrama de caja de la hoja, ¿qué proporción de los datos queda dentro de la caja?"),
   [t("One quarter", "La cuarta parte"), t("The middle half", "La mitad central"), t("All of them", "La totalidad")], 1,
   {0: t("The box goes from Q1 to Q3. How many quarters is that?", "La caja va de Q1 a Q3. ¿Cuántos cuartos son?"), 2: t("The whiskers hold the rest.", "Los bigotes contienen el resto.")},
   t("From Q1 to Q3 there are two quarters: the middle half.", "De Q1 a Q3 hay dos cuartos: la mitad central."))}
{P(t("Try it 5 · A long whisker", "Pruebe 5 · Un bigote largo"), t("A right whisker much longer than the left one means…", "Un bigote derecho mucho más largo que el izquierdo indica que…"),
   [t("there are one or more high values far from the group", "hay uno o varios valores altos apartados del conjunto"), t("the median was calculated wrong", "la mediana está mal calculada"), t("the data are perfectly symmetric", "los datos son perfectamente simétricos")], 0,
   {1: t("The whisker does not depend on the median.", "El bigote no depende de la mediana."), 2: t("Symmetric data have whiskers of about the same length.", "Los datos simétricos tienen bigotes parecidos.")},
   t("The right whisker reaches the maximum: if it is long, some high values are far from the rest.", "El bigote derecho llega al máximo: si es largo, hay valores altos lejos del resto."))}
{P(t("Try it 6 · Five genes", "Pruebe 6 · Cinco genes"), t("A living thing with five genes of two alleles each can make…", "Un organismo con cinco genes de dos alelos puede producir…"),
   [t("10 different gametes", "10 gametos distintos"), t("25 different gametes", "25 gametos distintos"), t("32 different gametes", "32 gametos distintos")], 2,
   {0: t("That is 2 + 2 + 2 + 2 + 2. The counting principle multiplies.", "Eso es 2 + 2 + 2 + 2 + 2. El principio del conteo multiplica."), 1: t("That is 5 × 5. Each gene gives 2 choices, five times.", "Eso es 5 × 5. Cada gen da 2 opciones, cinco veces.")},
   t("2 × 2 × 2 × 2 × 2 = 2⁵ = 32.", "2 × 2 × 2 × 2 × 2 = 2⁵ = 32."))}
{P(t("Try it 7 · Two peaks", "Pruebe 7 · Dos picos"), t("A histogram with two separate peaks suggests mainly that…", "Un histograma con dos picos separados sugiere sobre todo que…"),
   [t("two groups were mixed that should be analyzed separately", "se mezclaron dos grupos que convenía analizar por separado"), t("the instrument was not calibrated", "el instrumento estaba descalibrado"), t("there is no spread in the data", "no hay dispersión en los datos")], 0,
   {1: t("A calibration error shifts all the data the same way; it does not create two peaks.", "Un error de calibración desplaza todos los datos igual; no crea dos picos."), 2: t("Two peaks far apart mean a lot of spread.", "Dos picos separados significan mucha dispersión.")},
   t("For example, mixing the heights of adults and children gives two peaks.", "Por ejemplo, mezclar estaturas de adultos y de niños da dos picos."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK). You may use the calculator.", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SP.8.a", "2", t("<em>A nurse measured a patient’s resting heart rate on five days: 68, 72, 70, 71, and 69 beats per minute.</em><br>What are the mean and the range?", "<em>Una enfermera midió el pulso en reposo de un paciente durante cinco días: 68, 72, 70, 71 y 69 latidos por minuto.</em><br>¿Cuáles son la media y el rango?"),
   [t("Mean 70, range 4", "Media 70, rango 4"), t("Mean 70, range 72", "Media 70, rango 72"), t("Mean 71, range 4", "Media 71, rango 4"), t("Mean 350, range 4", "Media 350, rango 4")], 0,
   {1: t("The range is the largest minus the smallest, not the largest.", "El rango es el mayor menos el menor, no el mayor."), 2: t("Add the five values and divide by 5.", "Sume los cinco valores y divida entre 5."), 3: t("350 is the sum. Divide it by 5.", "350 es la suma. Divídala entre 5.")},
   t("Sum = 350, and 350 ÷ 5 = 70. Range = 72 − 68 = 4.", "Suma = 350, y 350 ÷ 5 = 70. Rango = 72 − 68 = 4."))}
{G(2, "SP.8.c", "2", t("<em>In a mix of ions, 40% are Na⁺ and 60% are K⁺. Two ions are drawn at random, each one put back before the next draw.</em><br>What is the probability of drawing two Na⁺ ions in a row?", "<em>En una mezcla de iones, el 40 % son Na⁺ y el 60 % son K⁺. Se extraen dos iones al azar, devolviendo cada uno antes de la siguiente extracción.</em><br>¿Cuál es la probabilidad de extraer dos iones Na⁺ seguidos?"),
   [t("0.04 (4%)", "0.04 (4 %)"), t("0.16 (16%)", "0.16 (16 %)"), t("0.40 (40%)", "0.40 (40 %)"), t("0.80 (80%)", "0.80 (80 %)")], 1,
   {0: t("0.4 × 0.4 is not 0.04. Multiply carefully: 4 × 4 = 16, with two decimal places.", "0.4 × 0.4 no es 0.04. Multiplique con cuidado: 4 × 4 = 16, con dos decimales."), 2: t("That is the chance for one draw. Two draws in a row must both happen.", "Esa es la probabilidad de una extracción. Las dos tienen que ocurrir."), 3: t("For “this and then that,” multiply the probabilities; do not add them.", "Para «esto y después aquello», se multiplican las probabilidades; no se suman.")},
   t("Independent events: 0.40 × 0.40 = 0.16, that is, 16%.", "Sucesos independientes: 0.40 × 0.40 = 0.16, es decir, 16 %."))}
{G(3, "SP.8.b", "1–2", t("<em>A lab can choose 3 growing media, 4 temperatures, and 2 incubation times.</em><br>How many different setups are possible?", "<em>Un laboratorio puede elegir 3 medios de cultivo, 4 temperaturas y 2 tiempos de incubación.</em><br>¿Cuántos montajes distintos son posibles?"),
   ["9", "12", "24", "48"], 2,
   {0: t("3 + 4 + 2 = 9 adds the choices. The counting principle multiplies.", "3 + 4 + 2 = 9 suma las opciones. El principio del conteo multiplica."), 1: t("3 × 4 = 12 forgets the 2 times.", "3 × 4 = 12 olvida los 2 tiempos."), 3: t("Check: 3 × 4 × 2.", "Revise: 3 × 4 × 2.")},
   t("3 × 4 × 2 = 24.", "3 × 4 × 2 = 24."))}
{G(4, "SP.3.d", "2–3", t("<em>A biologist wants to estimate the average number of eggs per nest for a bird species in a large nesting area. She can check only 10 nests.</em><br>Which sample gives the most representative estimate?", "<em>Una bióloga quiere estimar el número medio de huevos por nido de un ave en una gran zona de anidación. Solo puede revisar 10 nidos.</em><br>¿Qué muestra da la estimación más representativa?"),
   [t("10 nests chosen at random from the whole area", "10 nidos elegidos al azar en toda la zona"), t("The 10 nests easiest to reach", "Los 10 nidos más fáciles de alcanzar"), t("10 nests she already studied in past years", "10 nidos que ya estudió en años anteriores"), t("Only nests she can see from the trail", "Solo los nidos que se ven desde el camino")], 0,
   {1: t("Easy places may have different conditions. That is selection bias.", "Los lugares fáciles pueden tener condiciones distintas. Es sesgo de selección."), 2: t("Nests studied before may not be typical.", "Los nidos ya estudiados podrían no ser típicos."), 3: t("Hidden nests would be left out.", "Los nidos escondidos quedarían fuera.")},
   t("A random sample gives every nest the same chance, so the sample looks like the whole population.", "Una muestra al azar da a cada nido la misma probabilidad, así que la muestra se parece a toda la población."))}
{G(5, "SP.4.a", "2–3", t("<em>Two students measured the speed of sound five times each (m/s). Student A: 340, 345, 343, 342, 345. Student B: 310, 375, 340, 360, 320. Both averages are close to 343 m/s, the accepted value.</em><br>Which claim do the data support?", "<em>Dos estudiantes midieron la velocidad del sonido cinco veces cada uno (m/s). Estudiante A: 340, 345, 343, 342, 345. Estudiante B: 310, 375, 340, 360, 320. Los dos promedios están cerca de 343 m/s, el valor aceptado.</em><br>¿Qué afirmación apoyan los datos?"),
   [t("Both students were equally precise, because their averages are similar.", "Los dos fueron igual de precisos, porque sus promedios se parecen."), t("Student A was more precise: his range is 5 m/s, against 65 m/s for student B.", "El estudiante A fue más preciso: su rango es de 5 m/s, frente a 65 m/s del B."), t("Student B was more precise, because his values vary more.", "El estudiante B fue más preciso, porque sus valores varían más."), t("Neither one was accurate.", "Ninguno fue exacto.")], 1,
   {0: t("Precision is about how close the repeated values are to each other, not about the average.", "La precisión trata de cuán cerca están entre sí las mediciones, no del promedio."), 2: t("More variation means less precision.", "Más variación significa menos precisión."), 3: t("Both averages are close to 343: both are accurate on average.", "Los dos promedios están cerca de 343: en promedio, ambos son exactos.")},
   t("Range A = 345 − 340 = 5; range B = 375 − 310 = 65. A’s values are tightly grouped: more precise.", "Rango A = 345 − 340 = 5; rango B = 375 − 310 = 65. Los valores de A están agrupados: más preciso."))}"""

    secciones = [
        ("s1", t("Four ways to summarize a data set", "Cuatro maneras de resumir un conjunto de datos"), s1),
        ("s2", t("Shape, center, and spread: the histogram", "Forma, centro y dispersión: el histograma"), s2),
        ("s3", t("The five-number summary and the box plot", "El resumen de cinco números y el diagrama de caja"), s3),
        ("s4", t("Spread as a measure of experimental error", "La dispersión como medida del error experimental"), s4),
        ("s5", t("Counting possibilities", "Contar posibilidades"), s5),
        ("s6", t("Science reading", "Lectura científica"), s6),
        ("s7", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Measure ten times.", "Mida diez veces."), t("With a ruler or tape measure, measure the same object at home ten times (a book, the kitchen table). Find the mean, median, mode, and range, and say in one sentence which measure of center represents it best and why.", "Con una regla o cinta, mida diez veces el mismo objeto de su casa (un libro, la mesa de la cocina). Halle la media, la mediana, la moda y el rango, y diga en una oración qué medida de centro lo representa mejor y por qué.")),
        (t("Draw the box.", "Dibuje la caja."), t("With your ten measurements, find the five-number summary and draw the box plot. Is one whisker longer than the other? What could explain it?", "Con sus diez mediciones, halle el resumen de cinco números y dibuje el diagrama de caja. ¿Un bigote es más largo que el otro? ¿Qué podría explicarlo?")),
        (t("Count.", "Cuente."), t("Draw a tree diagram for tossing a coin three times. How many outcomes are there? In how many do you get exactly two heads?", "Dibuje un diagrama de árbol para tres lanzamientos de una moneda. ¿Cuántos resultados hay? ¿En cuántos salen exactamente dos caras?")),
    ]
    quiz = [
        (t("A set of measurements is 6, 8, 8, 10, and 13. The mean is…", "Un conjunto de mediciones es 6, 8, 8, 10 y 13. La media es…"), ["8", "9", "8.5", "10"], 1,
         {0: t("8 is the median and the mode.", "8 es la mediana y la moda."), 2: t("Add all five: 45. Divide by 5.", "Sume los cinco: 45. Divida entre 5."), 3: t("10 is one of the values.", "10 es uno de los valores.")}, t("6 + 8 + 8 + 10 + 13 = 45; 45 ÷ 5 = 9.", "6 + 8 + 8 + 10 + 13 = 45; 45 ÷ 5 = 9.")),
        (t("For the same set (6, 8, 8, 10, 13), the median and the mode are…", "En el mismo conjunto (6, 8, 8, 10, 13), la mediana y la moda son…"), [t("9 and 8", "9 y 8"), t("8 and 8", "8 y 8"), t("8 and 13", "8 y 13"), t("9 and 9", "9 y 9")], 1,
         {0: t("9 is the mean. The median is the middle value.", "9 es la media. La mediana es el valor central."), 2: t("13 appears once.", "13 aparece una vez."), 3: t("9 is not in the data.", "9 no está en los datos.")}, t("Middle value: 8. Most repeated: 8.", "Valor central: 8. El más repetido: 8.")),
        (t("The range of 6, 8, 8, 10, and 13 is…", "El rango del conjunto 6, 8, 8, 10 y 13 es…"), ["13", "8", "9", "7"], 3,
         {0: t("13 is the largest value.", "13 es el valor mayor."), 1: t("8 is the median.", "8 es la mediana."), 2: t("9 is the mean.", "9 es la media.")}, t("13 − 6 = 7.", "13 − 6 = 7.")),
        (t("Ten measurements include one value far from the rest. Which measure represents the set best?", "Un conjunto de diez mediciones contiene un valor muy separado. ¿Qué medida lo representa mejor?"),
         [t("The mean, because it uses all the data", "La media, porque usa todos los datos"), t("The range, because it measures variation", "El rango, porque mide la variación"), t("The median, because the outlier does not move it", "La mediana, porque el atípico no la desplaza"), t("The mode, because it is the most frequent", "La moda, porque es la más frecuente")], 2,
         {0: t("Using all the data is the problem: the outlier pulls it.", "Usar todos los datos es el problema: el atípico la arrastra."), 1: t("The range is not a measure of center.", "El rango no es una medida de centro."), 3: t("There may be no repeated value at all.", "Puede no haber ningún valor repetido.")}, t("The median resists outliers.", "La mediana resiste los valores atípicos.")),
        (t("In a box plot, the thick line across the box shows…", "En un diagrama de caja, la línea gruesa que atraviesa la caja representa…"), [t("the mean", "la media"), t("the range", "el rango"), t("the maximum", "el valor máximo"), t("the median", "la mediana")], 3,
         {0: t("A box plot does not show the mean.", "El diagrama de caja no muestra la media."), 1: t("The range is the whole width, whisker to whisker.", "El rango es todo el ancho, de bigote a bigote."), 2: t("The maximum is the end of the right whisker.", "El máximo es el extremo del bigote derecho.")}, t("The line inside the box is the median (Q2).", "La línea dentro de la caja es la mediana (Q2).")),
        (t("The box of a box plot holds…", "La caja de un diagrama de caja contiene…"), [t("the middle half of the data", "la mitad central de los datos"), t("all the data", "todos los datos"), t("one quarter of the data", "la cuarta parte de los datos"), t("only the outliers", "solo los valores atípicos")], 0,
         {1: t("The whiskers hold the rest.", "Los bigotes contienen el resto."), 2: t("From Q1 to Q3 there are two quarters.", "De Q1 a Q3 hay dos cuartos."), 3: t("Outliers are at the ends.", "Los atípicos están en los extremos.")}, t("From Q1 to Q3: the middle 50%.", "De Q1 a Q3: el 50 % central.")),
        (t("A histogram has two clearly separate peaks. The most reasonable reading is that…", "Un histograma presenta dos picos claramente separados. La interpretación más razonable es que…"),
         [t("the data are perfectly symmetric", "los datos son perfectamente simétricos"), t("two different groups were mixed", "se mezclaron dos grupos distintos"), t("there is no spread", "no hay dispersión"), t("the mean equals the median", "la media es igual a la mediana")], 1,
         {0: t("Two peaks is not the same as symmetric.", "Dos picos no equivale a simetría."), 2: t("Two separate peaks mean a lot of spread.", "Dos picos separados significan mucha dispersión."), 3: t("That says nothing about the two peaks.", "Eso no explica los dos picos.")}, t("Two peaks usually mean two groups mixed together.", "Dos picos suelen indicar dos grupos mezclados.")),
        (t("Ten measurements are tightly grouped, but all are 2 grams above the true value. This means…", "Diez mediciones muy agrupadas, pero todas 2 gramos por encima del valor verdadero, indican…"),
         [t("random error: repeat more times", "error aleatorio: hace falta repetir más"), t("precise and accurate data", "datos precisos y exactos"), t("systematic error: the instrument is not calibrated", "error sistemático: el instrumento está descalibrado"), t("an outlier to discard", "un valor atípico que conviene descartar")], 2,
         {0: t("Repeating will not remove a shift that is always the same.", "Repetir no elimina un desvío que siempre es igual."), 1: t("They are precise, but not accurate.", "Son precisos, pero no exactos."), 3: t("All ten are off, not just one.", "Las diez se apartan, no solo una.")}, t("Same shift every time: systematic error, fixed by calibrating.", "El mismo desvío cada vez: error sistemático, que se corrige calibrando.")),
        (t("A living thing with four genes of two alleles each can make…", "Un organismo con cuatro genes de dos alelos cada uno puede producir…"), [t("8 different gametes", "8 gametos distintos"), t("16 different gametes", "16 gametos distintos"), t("4 different gametes", "4 gametos distintos"), t("24 different gametes", "24 gametos distintos")], 1,
         {0: t("8 is for three genes.", "8 es para tres genes."), 2: t("Each gene gives 2 choices; multiply.", "Cada gen da 2 opciones; multiplique."), 3: t("24 = 4 × 3 × 2 × 1 is a permutation, not this count.", "24 = 4 × 3 × 2 × 1 es una permutación, no este conteo.")}, t("2 × 2 × 2 × 2 = 16.", "2 × 2 × 2 × 2 = 16.")),
        (t("In how many different orders can the five steps of a lab procedure be arranged?", "¿De cuántas maneras distintas pueden ordenarse los cinco pasos de un protocolo?"), ["25", "10", "120", "5"], 2,
         {0: t("5 × 5 would let a step be used twice.", "5 × 5 permitiría usar un paso dos veces."), 1: t("10 is the number of pairs, not orders.", "10 es el número de pares, no de ordenaciones."), 3: t("5 is the number of steps.", "5 es el número de pasos.")}, t("5 × 4 × 3 × 2 × 1 = 120.", "5 × 4 × 3 × 2 × 1 = 120.")),
        (t("Three samples out of eight are chosen for analysis, and the order does not matter. How many choices are possible?", "De un lote de ocho muestras se eligen tres, sin que importe el orden. ¿Cuántas selecciones son posibles?"), ["56", "24", "336", "11"], 0,
         {1: t("24 = 4 × 3 × 2. Start from 8.", "24 = 4 × 3 × 2. Empiece por 8."), 2: t("336 = 8 × 7 × 6 counts each group 6 times. Divide by 3 × 2 × 1.", "336 = 8 × 7 × 6 cuenta cada grupo 6 veces. Divida entre 3 × 2 × 1."), 3: t("8 + 3 is not a count.", "8 + 3 no es un conteo.")}, t("(8 × 7 × 6) ÷ (3 × 2 × 1) = 336 ÷ 6 = 56.", "(8 × 7 × 6) ÷ (3 × 2 × 1) = 336 ÷ 6 = 56.")),
        (t("In which of these situations DOES the order matter?", "¿En cuál de estas situaciones IMPORTA el orden?"),
         [t("Choosing three samples to analyze", "Elegir tres muestras para analizarlas"), t("Choosing two flower colors for a cross", "Escoger dos colores de flor para un cruce"), t("Choosing four students for a team", "Seleccionar cuatro estudiantes para un equipo"), t("Setting the order of the steps of a procedure", "Establecer la secuencia de pasos de un procedimiento")], 3,
         {0: t("The same three samples are the same group in any order.", "Las mismas tres muestras forman el mismo grupo en cualquier orden."), 1: t("The pair is the same pair.", "La pareja es la misma."), 2: t("Without roles, the team is the same team.", "Sin cargos, el equipo es el mismo.")}, t("A different order of steps gives a different (often ruined) result.", "Otro orden de pasos da otro resultado (a menudo arruinado).")),
    ]
    filas = [
        (t("Find the measures of center", "Calcula las medidas de centro"), t("I find mean, median, mode, and range and say which one represents the data best.", "Calculo media, mediana, moda y rango y digo cuál representa mejor los datos."), t("I find the mean, but I make mistakes with the median or mode.", "Calculo bien la media, pero me equivoco en la mediana o la moda."), t("I mix them up, or forget to order the data for the median.", "Las confundo u olvido ordenar los datos para la mediana.")),
        (t("Read shape, center, and spread in a graph", "Interpreta forma, centro y dispersión"), t("I describe all three and can suggest why (for example, two groups mixed).", "Describo los tres y propongo una explicación (por ejemplo, dos grupos mezclados)."), t("I find the center, but not the shape or spread.", "Identifico el centro, pero no la forma ni la dispersión."), t("I read bar heights without thinking about the distribution.", "Leo alturas de barras sin relacionarlas con la distribución.")),
        (t("Count possibilities", "Aplica el principio del conteo"), t("I tell permutations from combinations and use the rule for any number of steps.", "Distingo permutación de combinación y aplico la regla a cualquier número de etapas."), t("I multiply, but I do not check whether the order matters.", "Multiplico, pero no distingo si el orden importa."), t("I add instead of multiplying.", "Sumo en lugar de multiplicar.")),
        (t("Connect spread with experimental error", "Relaciona la dispersión con el error experimental"), t("I tell random error from systematic error and explain why repeating does not fix a systematic one.", "Distingo el error aleatorio del sistemático y explico por qué repetir no corrige el sistemático."), t("I see the spread, but I do not interpret it.", "Reconozco la dispersión, pero no la interpreto."), t("I think any variation is the student’s fault.", "Creo que toda variación es un fallo del estudiante.")),
    ]
    cierre = "<p>" + t("This lesson closes Topic 2. You now have the complete set of number tools for the course: write any size in scientific notation, read it on a graph, and summarize it with the right measures. Together with the three tools of Topic 1, you have everything the test asks for <em>besides</em> the content.", "Con esta lección se cierra el Tema 2 y queda completo el andamiaje numérico del curso: escribir cualquier magnitud en notación científica, leerla en una gráfica y resumirla con las medidas adecuadas. Junto con las tres herramientas del Tema 1, ya tiene todo lo que el examen exige <em>además</em> del contenido.") + "</p><p>" + \
             t("Topic 3, Life science I, opens the first content area, the one that weighs the most on the test. Everything you built stays in use: the roots of Lesson 1.3 will help you take apart words like <em>mitochondrion</em> and <em>chloroplast</em>, and the tree diagram of this lesson will come back in Topic 4 as a genetic cross.", "El Tema 3, Ciencias de la vida I, abre el primer dominio de contenido, el de mayor peso en el examen. Todo lo construido sigue en uso: las raíces de la Lección 1.3 servirán para desmontar palabras como <em>mitocondria</em> o <em>cloroplasto</em>, y el diagrama de árbol de esta lección volverá en el Tema 4 convertido en cruce genético.") + "</p>"
    glosario = [
        (t("Mean", "Media"), t("The sum of the values divided by how many there are.", "La suma de los valores dividida entre la cantidad de datos.")),
        (t("Median", "Mediana"), t("The middle value of the ordered data.", "El valor central de los datos ordenados.")),
        (t("Mode", "Moda"), t("The value that appears most often.", "El valor que más se repite.")),
        (t("Range", "Rango"), t("The largest value minus the smallest.", "El valor mayor menos el menor.")),
        (t("Outlier", "Valor atípico"), t("A value far from the rest of the data.", "Un valor muy separado del resto de los datos.")),
        (t("Quartile", "Cuartil"), t("One of the three values that split ordered data into four equal parts.", "Cada uno de los tres valores que dividen los datos ordenados en cuatro partes iguales.")),
        (t("Precision", "Precisión"), t("How close repeated measurements are to each other.", "Cuán cerca están entre sí las mediciones repetidas.")),
        (t("Accuracy", "Exactitud"), t("How close a measurement is to the true value.", "Cuán cerca está una medición del valor verdadero.")),
        (t("Permutation / combination", "Permutación / combinación"), t("A choice where the order matters / where it does not.", "Una elección en la que importa el orden / en la que no importa.")),
    ]
    estd = C.estandares(["SP.8.a", "SP.8.b", "SP.8.c", "SP.3.d", "SP.4.a"], [], base=["SP.2.a"])
    conexion = "<p>" + t("Lesson 2.1 taught you to write sizes and Lesson 2.2 to read them on an axis. This lesson teaches you to <strong>summarize</strong> them: what to do when instead of one value there are thirty, and you need to say in one number what they are like.", "La Lección 2.1 enseñó a escribir las magnitudes y la 2.2 a leerlas en un eje. Esta enseña a <strong>resumirlas</strong>: qué hacer cuando en lugar de un dato hay treinta y hace falta decir en una sola cifra cómo son.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> work small data sets (eight or ten values) by hand first, and only then use the calculator for bigger ones. Working by hand fixes the meaning of each measure; the calculator only saves time. Math Level 2 (mean, median, probability) and Math Level 3, Topic 7 (quartiles and box plots) are a good bridge.", "<strong>Cómo estudiar esta lección:</strong> calcule primero a mano con conjuntos pequeños (ocho o diez datos) y solo después use la calculadora con conjuntos mayores. El cálculo a mano fija el significado de cada medida; la calculadora solo ahorra tiempo. El Nivel 2 de Matemáticas (media, mediana, probabilidad) y el Tema 7 del Nivel 3 (cuartiles y diagramas de caja) son un buen puente.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Thirty measurements, one number: summarize the data, measure the error, and count the possibilities.", "Treinta mediciones, una cifra: resumir los datos, medir el error y contar las posibilidades."),
        ["SP.8 · " + t("Statistics and probability", "Estadística y probabilidad"), "SP.3.d · " + t("Sampling", "Muestreo")],
        [t("<strong>Describe</strong> experimental data with the mean, median, mode, and range.", "<strong>Describir</strong> datos experimentales con la media, la mediana, la moda y el rango."),
         t("<strong>Decide</strong> which measure best represents data with an outlier.", "<strong>Decidir</strong> qué medida representa mejor un conjunto con un valor atípico."),
         t("<strong>Read</strong> a histogram (shape, center, spread) and a box plot (the five-number summary).", "<strong>Leer</strong> un histograma (forma, centro, dispersión) y un diagrama de caja (el resumen de cinco números)."),
         t("<strong>Connect</strong> the spread of the data with experimental error (precision and accuracy).", "<strong>Relacionar</strong> la dispersión de los datos con el error experimental (precisión y exactitud)."),
         t("<strong>Use</strong> the counting principle, permutations, and combinations in biology and genetics.", "<strong>Aplicar</strong> el principio del conteo, las permutaciones y las combinaciones a escenarios biológicos y genéticos.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("3-1", t("Cell theory, organelles, and the cell membrane", "Teoría celular, organelos y membrana plasmática")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- práctica
def js_medidas():
    if C.L == "en":
        M = {"media": "the mean", "mediana": "the median", "moda": "the mode", "rango": "the range", "q1": "the first quartile (Q1)", "q3": "the third quartile (Q3)"}
        tx = dict(enun='"<p>" + ctx + ": <strong>" + datos.join(", ") + "</strong>.</p><p>Find <strong>" + M[que] + "</strong>.</p>"',
                  ord_="In order: ", suma="Sum = ", ent=" ÷ ", mid="The middle value", mids="The two middle values are ", prom=", and their average is ", modaT="appears most often", rangoT="Largest − smallest = ",
                  q1T="Q1 is the median of the lower half: ", q3T="Q3 is the median of the upper half: ")
        PI = {"media": "Add all the values and divide by how many there are.", "mediana": "Put the data in order first. With an even count, average the two middle values.", "moda": "Which value appears most often?", "rango": "Largest value minus smallest value.", "q1": "Order the data, take the lower half, and find its median.", "q3": "Order the data, take the upper half, and find its median."}
        OTRA = "That is {m}, not the measure asked for. "
        CTX = [["Heights of plants (cm)", 15, 60], ["Reaction times (hundredths of a second)", 20, 35], ["Pulse rates (beats per minute)", 64, 88], ["Seeds that sprouted in each tray", 12, 30], ["Daily high temperatures (°C)", 14, 32], ["Masses of eggs (g)", 52, 64]]
    else:
        M = {"media": "la media", "mediana": "la mediana", "moda": "la moda", "rango": "el rango", "q1": "el primer cuartil (Q1)", "q3": "el tercer cuartil (Q3)"}
        tx = dict(enun='"<p>" + ctx + ": <strong>" + datos.join(", ") + "</strong>.</p><p>Halle <strong>" + M[que] + "</strong>.</p>"',
                  ord_="Ordenados: ", suma="Suma = ", ent=" ÷ ", mid="El valor central", mids="Los dos centrales son ", prom=", y su promedio es ", modaT="es el que más se repite",
                  rangoT="Mayor − menor = ", q1T="Q1 es la mediana de la mitad inferior: ", q3T="Q3 es la mediana de la mitad superior: ")
        PI = {"media": "Sume todos los valores y divida entre la cantidad de datos.", "mediana": "Ordene primero los datos. Si la cantidad es par, promedie los dos centrales.", "moda": "¿Qué valor se repite más?", "rango": "Valor mayor menos valor menor.", "q1": "Ordene los datos, tome la mitad inferior y halle su mediana.", "q3": "Ordene los datos, tome la mitad superior y halle su mediana."}
        OTRA = "Ese valor es {m}, no la medida que se pide. "
        CTX = [["Alturas de plantas (cm)", 15, 60], ["Tiempos de reacción (centésimas de segundo)", 20, 35], ["Pulsaciones (latidos por minuto)", 64, 88], ["Semillas germinadas en cada bandeja", 12, 30], ["Temperaturas máximas diarias (°C)", 14, 32], ["Masas de huevos (g)", 52, 64]]
    import json
    return f"""
var M = {json.dumps(M, ensure_ascii=False)}, CTX = {json.dumps(CTX, ensure_ascii=False)}, PI = {json.dumps(PI, ensure_ascii=False)}, OTRA = {json.dumps(OTRA, ensure_ascii=False)};
function med(a){{ var n = a.length, m = Math.floor(n / 2); return n % 2 ? a[m] : (a[m - 1] + a[m]) / 2; }}
function fmt(x){{ return String(Math.round(x * 1000) / 1000); }}
function gM(){{
  var n = elige([4, 5, 8, 10]), cx = elige(CTX), ctx = cx[0], base = aleatorio(cx[1], cx[2]), datos = [], i, que = elige(["media", "mediana", "moda", "rango", "q1", "q3"]);
  for (i = 0; i < n; i++) datos.push(base + aleatorio(-6, 6));
  if (que === "moda"){{ var k = aleatorio(0, n - 3); datos[k + 1] = datos[k]; datos[k + 2] = datos[k]; }}
  var o = datos.slice().sort(function(a, b){{ return a - b; }}), r, exp, s = 0;
  datos.forEach(function(v){{ s += v; }});
  if (que === "moda"){{ var c = {{}}, best = null; o.forEach(function(v){{ c[v] = (c[v] || 0) + 1; if (best === null || c[v] > c[best]) best = v; }}); var empate = Object.keys(c).filter(function(v){{ return c[v] === c[best]; }}).length > 1; if (empate) return gM(); }}
  if (que === "media"){{ r = s / n; exp = "{tx['suma']}" + s + "; " + s + "{tx['ent']}" + n + " = " + fmt(r) + "."; }}
  else if (que === "mediana"){{ r = med(o); exp = "{tx['ord_']}" + o.join(", ") + ". " + (n % 2 ? "{tx['mid']}: " + fmt(r) + "." : "{tx['mids']}" + o[n/2 - 1] + " / " + o[n/2] + "{tx['prom']}" + fmt(r) + "."); }}
  else if (que === "moda"){{ r = best; exp = "{tx['ord_']}" + o.join(", ") + ". " + best + " {tx['modaT']}."; }}
  else if (que === "rango"){{ r = o[n - 1] - o[0]; exp = "{tx['rangoT']}" + o[n - 1] + " − " + o[0] + " = " + r + "."; }}
  else {{ var h = Math.floor(n / 2), lo = o.slice(0, h), hi = o.slice(n - h); r = que === "q1" ? med(lo) : med(hi); exp = "{tx['ord_']}" + o.join(", ") + ". " + (que === "q1" ? "{tx['q1T']}" + lo.join(", ") : "{tx['q3T']}" + hi.join(", ")) + " → " + fmt(r) + "."; }}
  var h2 = Math.floor(n / 2), otras = {{media: s / n, mediana: med(o), rango: o[n - 1] - o[0], q1: med(o.slice(0, h2)), q3: med(o.slice(n - h2))}};
  return {{enun: {tx['enun']}, resp: leeNumero(fmt(r)), explica: exp, pista: function(v){{
    for (var k in otras) if (k !== que && otras[k] !== r && igual(v, leeNumero(fmt(otras[k])))) return OTRA.replace("{{m}}", M[k]) + PI[que];
    return PI[que]; }}}};
}}
"""


def js_conteo():
    if C.L == "en":
        return r"""
function gK(){
  var tipo = elige(["genes", "perm", "comb", "menu", "coin"]), r, enun, exp;
  if (tipo === "genes"){ var n = aleatorio(2, 6); r = Math.pow(2, n); enun = "A living thing has <strong>" + n + "</strong> genes, each with two alleles. How many different gametes can it make?"; exp = "Each gene gives 2 choices: " + Array(n).fill("2").join(" × ") + " = " + r + "."; }
  else if (tipo === "perm"){ var n = aleatorio(3, 6), f = 1, p = []; for (var i = n; i >= 1; i--){ f *= i; p.push(i); } r = f; enun = "A procedure has <strong>" + n + "</strong> steps. In how many different orders could the steps be arranged?"; exp = "Order matters (permutation): " + p.join(" × ") + " = " + r + "."; }
  else if (tipo === "comb"){ var n = aleatorio(5, 9), k = elige([2, 3]), num = 1, den = 1, a = [], b = []; for (var i = 0; i < k; i++){ num *= (n - i); a.push(n - i); den *= (i + 1); b.unshift(i + 1); } r = num / den; enun = "From <strong>" + n + "</strong> samples, <strong>" + k + "</strong> are chosen for the same test. The order does not matter. How many different choices are possible?"; exp = "Combination: (" + a.join(" × ") + ") ÷ (" + b.join(" × ") + ") = " + num + " ÷ " + den + " = " + r + ". (On the TI-30XS: " + n + ", prb, nCr, " + k + ".)"; }
  else if (tipo === "menu"){ var x = aleatorio(2, 5), y = aleatorio(2, 5), z = aleatorio(2, 4); r = x * y * z; enun = "An experiment can use <strong>" + x + "</strong> kinds of soil, <strong>" + y + "</strong> amounts of water, and <strong>" + z + "</strong> light levels. How many different setups are possible?"; exp = "Counting principle: " + x + " × " + y + " × " + z + " = " + r + "."; }
  else { var n = aleatorio(2, 6); r = Math.pow(2, n); enun = "A coin is tossed <strong>" + n + "</strong> times. How many different sequences of heads and tails are possible?"; exp = "2 choices each time: " + Array(n).fill("2").join(" × ") + " = " + r + "."; }
  return {enun: "<p>" + enun + "</p>", solucion: exp, evalua: numN(r, [], "Multiply the choices of each step (and divide if the order does not matter).")};
}
"""
    return r"""
function gK(){
  var tipo = elige(["genes", "perm", "comb", "menu", "coin"]), r, enun, exp;
  if (tipo === "genes"){ var n = aleatorio(2, 6); r = Math.pow(2, n); enun = "Un organismo tiene <strong>" + n + "</strong> genes con dos alelos cada uno. ¿Cuántos gametos distintos puede producir?"; exp = "Cada gen aporta 2 posibilidades: " + Array(n).fill("2").join(" × ") + " = " + r + "."; }
  else if (tipo === "perm"){ var n = aleatorio(3, 6), f = 1, p = []; for (var i = n; i >= 1; i--){ f *= i; p.push(i); } r = f; enun = "Un protocolo tiene <strong>" + n + "</strong> pasos. ¿De cuántas maneras distintas podrían ordenarse?"; exp = "Importa el orden (permutación): " + p.join(" × ") + " = " + r + "."; }
  else if (tipo === "comb"){ var n = aleatorio(5, 9), k = elige([2, 3]), num = 1, den = 1, a = [], b = []; for (var i = 0; i < k; i++){ num *= (n - i); a.push(n - i); den *= (i + 1); b.unshift(i + 1); } r = num / den; enun = "De <strong>" + n + "</strong> muestras se eligen <strong>" + k + "</strong> para el mismo análisis. No importa el orden. ¿Cuántas selecciones distintas son posibles?"; exp = "Combinación: (" + a.join(" × ") + ") ÷ (" + b.join(" × ") + ") = " + num + " ÷ " + den + " = " + r + ". (En la TI-30XS: " + n + ", prb, nCr, " + k + ".)"; }
  else if (tipo === "menu"){ var x = aleatorio(2, 5), y = aleatorio(2, 5), z = aleatorio(2, 4); r = x * y * z; enun = "Un experimento puede usar <strong>" + x + "</strong> tipos de suelo, <strong>" + y + "</strong> cantidades de agua y <strong>" + z + "</strong> niveles de luz. ¿Cuántos montajes distintos son posibles?"; exp = "Principio del conteo: " + x + " × " + y + " × " + z + " = " + r + "."; }
  else { var n = aleatorio(2, 6); r = Math.pow(2, n); enun = "Se lanza una moneda <strong>" + n + "</strong> veces. ¿Cuántas secuencias distintas de caras y cruces pueden salir?"; exp = "2 posibilidades cada vez: " + Array(n).fill("2").join(" × ") + " = " + r + "."; }
  return {enun: "<p>" + enun + "</p>", solucion: exp, evalua: numN(r, [], "Multiplique las posibilidades de cada etapa (y divida si no importa el orden).")};
}
"""


def banco_precision():
    O = [t("Precise and accurate", "Preciso y exacto"), t("Precise but not accurate (systematic error)", "Preciso pero no exacto (error sistemático)"), t("Not precise (random error)", "Poco preciso (error aleatorio)")]
    P = {0: t("Precise and accurate: values close together and close to the true value.", "Preciso y exacto: valores juntos y cerca del valor verdadero."),
         1: t("Systematic error: values close together but all shifted the same way.", "Error sistemático: valores juntos pero todos desplazados igual."),
         2: t("Random error: values far apart from each other.", "Error aleatorio: valores muy separados entre sí.")}
    d = [
        (t("True mass: 50.0 g. Measurements: 52.1, 52.0, 52.2, 52.1 g.", "Masa verdadera: 50.0 g. Mediciones: 52.1, 52.0, 52.2, 52.1 g."), 1, t("They are within 0.2 g of each other, but all about 2 g too high: the scale needs calibrating.", "Están a menos de 0.2 g entre sí, pero todas unos 2 g por encima: hay que calibrar la balanza.")),
        (t("True boiling point: 100 °C. Readings: 99.9, 100.1, 100.0, 99.9 °C.", "Punto de ebullición verdadero: 100 °C. Lecturas: 99.9, 100.1, 100.0, 99.9 °C."), 0, t("Close together and close to 100 °C.", "Juntas y cerca de 100 °C.")),
        (t("True length: 30.0 cm. Measurements: 27.5, 32.8, 29.1, 31.9 cm.", "Longitud verdadera: 30.0 cm. Mediciones: 27.5, 32.8, 29.1, 31.9 cm."), 2, t("A range of 5.3 cm: the technique is not controlled. Their average is close to 30, but each value is unreliable.", "Un rango de 5.3 cm: la técnica no está controlada. El promedio se acerca a 30, pero cada valor es poco fiable.")),
        (t("True time: 1.00 s. Timings: 1.21, 1.19, 1.20, 1.22 s (the student always presses the stopwatch late).", "Tiempo verdadero: 1.00 s. Mediciones: 1.21, 1.19, 1.20, 1.22 s (el estudiante siempre pulsa el cronómetro tarde)."), 1, t("Always about 0.2 s too long: a systematic error in the technique.", "Siempre unos 0.2 s de más: un error sistemático de la técnica.")),
        (t("True pH: 7.0. Readings: 5.9, 7.8, 6.4, 8.1.", "pH verdadero: 7.0. Lecturas: 5.9, 7.8, 6.4, 8.1."), 2, t("The readings jump around a lot: random error.", "Las lecturas saltan mucho: error aleatorio.")),
        (t("True volume: 25.0 mL. Readings: 25.1, 24.9, 25.0, 25.0 mL.", "Volumen verdadero: 25.0 mL. Lecturas: 25.1, 24.9, 25.0, 25.0 mL."), 0, t("Close together and on target.", "Juntas y en el blanco.")),
    ]
    return [{"enun": t("What kind of data are these?", "¿Qué tipo de datos son estos?") + "<br><strong>" + x + "</strong>", "ops": O, "ok": k, "enOrden": True,
             "pistas": {i: P[i] for i in range(3) if i != k}, "exp": f"<strong>{O[k]}.</strong> {e}"} for x, k, e in d]


def banco_orden():
    O = [t("Permutation: the order matters", "Permutación: el orden importa"), t("Combination: the order does not matter", "Combinación: el orden no importa")]
    d = [
        (t("Choosing 3 samples out of 10 to send to the lab, all for the same test.", "Elegir tres muestras de un lote de diez para el mismo análisis."), 1, t("Whichever is taken first, the group of three is the same.", "Da igual cuál se tome primero: el grupo de tres es el mismo.")),
        (t("Putting the 8 steps of a sample preparation in order.", "Ordenar los ocho pasos de una preparación de muestras."), 0, t("Staining then covering is not the same as covering then staining (Lesson 1.3).", "Colorear y después cubrir no es lo mismo que cubrir y colorear (Lección 1.3).")),
        (t("Forming a team of 4 students out of 18, with no roles.", "Formar un equipo de cuatro estudiantes entre dieciocho, sin cargos."), 1, t("Without roles, it is the same team in any order. With roles (leader, secretary…), it would be a permutation.", "Sin cargos, el equipo es el mismo en cualquier orden. Con cargos (coordinador, secretario…) sería permutación.")),
        (t("Recording the first, second, and third runners to finish a race.", "Registrar el primer, segundo y tercer corredor en llegar."), 0, t("First, second, third are positions: the order matters.", "Primero, segundo y tercero son posiciones: importa el orden.")),
        (t("Choosing 2 chemicals from a shelf of 6 to mix in a tube.", "Elegir dos reactivos de una estantería de seis para mezclarlos."), 1, t("For counting the possible mixtures, the pair is the same pair.", "Para contar las mezclas posibles, la pareja es la misma.")),
        (t("Creating a 4-digit code for a lab freezer.", "Crear un código de 4 cifras para el congelador del laboratorio."), 0, t("1234 and 4321 are different codes.", "1234 y 4321 son códigos distintos.")),
    ]
    return [{"enun": x, "ops": O, "ok": k, "enOrden": True, "exp": f"<strong>{O[k]}.</strong> {e}"} for x, k, e in d]


def banco_medida():
    d = [
        (t("Daily high temperatures for a week (°C): 28, 32, 30, 45, 31, 29, 33. The 45 °C day was an unusual heat wave. Which measure best represents a typical day?", "Temperaturas máximas de una semana (°C): 28, 32, 30, 45, 31, 29, 33. El día de 45 °C fue una ola de calor anómala. ¿Qué medida representa mejor un día típico?"),
         [t("The mean (32.6 °C), because it uses all the data", "La media (32.6 °C), porque usa todos los datos"), t("The median (31 °C), because the extreme value does not move it", "La mediana (31 °C), porque el valor extremo no la afecta"), t("The mode, because it is easiest", "La moda, porque es la más fácil"), t("The range, because it shows the variation", "El rango, porque muestra la variación")], 1,
         t("The median (31 °C) resists the 45 °C outlier; the mean is pulled up.", "La mediana (31 °C) resiste el atípico de 45 °C; la media sube arrastrada.")),
        (t("pH at seven points of a polluted river, in order: 5.8, 6.1, 6.3, 6.5, 6.8, 7.1, 8.2. What is the median, and why is it a good choice here?", "pH en siete puntos de un río contaminado, ordenados: 5.8, 6.1, 6.3, 6.5, 6.8, 7.1, 8.2. ¿Cuál es la mediana y por qué conviene aquí?"),
         [t("6.5; because 8.2 is extreme and would pull the mean", "6.5; porque 8.2 es extremo y arrastraría la media"), t("6.7; it is always better than the mean", "6.7; siempre es mejor que la media"), t("6.8; because it is the most common value", "6.8; porque es el valor más común"), t("7.0; there is no difference from the mean", "7.0; no hay diferencia con la media")], 0,
         t("With 7 ordered values, the median is the 4th: 6.5. The mean (about 6.69) is pulled up by 8.2.", "Con 7 datos ordenados, la mediana es el 4.º: 6.5. La media (unos 6.69) sube por el 8.2.")),
        (t("Flower colors in a garden: red, white, red, pink, red, white. Which measure makes sense?", "Colores de flores en un jardín: rojo, blanco, rojo, rosa, rojo, blanco. ¿Qué medida tiene sentido?"),
         [t("The mean", "La media"), t("The median", "La mediana"), t("The mode", "La moda"), t("The range", "El rango")], 2,
         t("Colors are not numbers, so you cannot add or order them. The mode (red) still works.", "Los colores no son números: no se pueden sumar ni ordenar. La moda (rojo) sí funciona.")),
        (t("Five timings of a ball falling: 1.02, 0.98, 1.05, 1.00, 0.99 s. What is the mean, to two decimal places?", "Cinco tiempos de caída de una pelota: 1.02, 0.98, 1.05, 1.00, 0.99 s. ¿Cuál es la media, con dos decimales?"),
         ["0.99 s", "1.00 s", "1.01 s", "1.05 s"], 2,
         t("Sum = 5.04; 5.04 ÷ 5 = 1.008, which rounds to 1.01 s.", "Suma = 5.04; 5.04 ÷ 5 = 1.008, que se redondea a 1.01 s.")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Look for an outlier, and ask whether the data are numbers.", "Busque un valor atípico y pregúntese si los datos son números."), "exp": e} for q, o, k, e in d]


def banco_cientiestad():
    A = {"bio": t("Biology", "Biología"), "qui": t("Chemistry", "Química"), "fis": t("Physics", "Física"), "tie": t("Earth science", "Ciencias de la Tierra")}
    def tb(cab, fila):
        return C.grafica({"tipo": "tabla", "encabezados": cab, "filas": [fila]}, t("Data table", "Tabla de datos"))
    def tb2(cab, filas):
        return C.grafica({"tipo": "tabla", "encabezados": cab, "filas": filas}, t("Data table", "Tabla de datos"))
    def hist(xe, ye, bars, py=None):
        sp = {"tipo": "barras", "xEtq": xe, "yEtq": ye, "barras": [{"etq": e, "valor": v} for e, v in bars]}
        if py:
            sp["py"] = py
        return C.grafica(sp, C.describe(sp), ancho=520, alto=290)
    def disp(xe, ye, pts, patron):
        sp = {"tipo": "puntos", "xEtq": xe, "yEtq": ye, "series": [{"nombre": "", "puntos": pts}], "patron": patron}
        return C.grafica(sp, C.describe(sp), ancho=520, alto=290)
    def lin(xe, ye, pts, px=None):
        sp = {"tipo": "linea", "xEtq": xe, "yEtq": ye, "series": [{"nombre": "", "puntos": pts}]}
        if px:
            sp["px"] = px
        return C.grafica(sp, C.describe(sp), ancho=520, alto=290)
    sube = t("The points rise from left to right in a narrow band: a strong positive correlation.", "Los puntos suben de izquierda a derecha en una franja estrecha: correlación positiva fuerte.")
    punnett = ('<table class="cuaderno" style="max-width:260px;margin:8px auto;text-align:center"><caption>' + t("Cross Bb × Bb", "Cruce Bb × Bb") + '</caption><thead><tr><th scope="col"></th><th scope="col">B</th><th scope="col">b</th></tr></thead>'
               '<tbody><tr><th scope="row">B</th><td>BB</td><td>Bb</td></tr><tr><th scope="row">b</th><td>Bb</td><td>bb</td></tr></tbody></table><p style="text-align:center">' + t("3 yellow : 1 green", "3 amarillas : 1 verde") + "</p>")
    d = [
        ("bio", t("A biologist measures the height (cm) of six tomato plants after 30 days with a new fertilizer: 18, 22, 19, 24, 20, 21.", "Una bióloga mide la altura (cm) de seis plantas de tomate tras 30 días con un fertilizante nuevo: 18, 22, 19, 24, 20, 21."), "",
         t("What is the mean height, rounded to the nearest centimeter?", "¿Cuál es la altura media, redondeada al centímetro?"), ["19 cm", "20.5 cm", "21 cm", "24 cm"], 2,
         t("Mean = (18 + 22 + 19 + 24 + 20 + 21) ÷ 6 = 124 ÷ 6 ≈ 20.67, which rounds to 21 cm. 20.5 cm is the median, not the mean.", "Media = (18 + 22 + 19 + 24 + 20 + 21) ÷ 6 = 124 ÷ 6 ≈ 20.67, que se redondea a 21 cm. 20.5 cm es la mediana, no la media.")),
        ("bio", t("In a cross of two pea plants Bb × Bb, B (yellow seed) is dominant over b (green seed). The Punnett square shows the expected results.", "En un cruce Bb × Bb, B (semilla amarilla) es dominante sobre b (semilla verde). El cuadro de Punnett muestra lo esperado."), punnett,
         t("Out of 200 seeds, about how many should be green (bb)?", "De 200 semillas, ¿aproximadamente cuántas se espera que sean verdes (bb)?"), ["25", "50", "100", "150"], 1,
         t("bb is 1 of 4 boxes: 1/4 = 0.25. 200 × 0.25 = 50 green seeds.", "bb es 1 de 4 casillas: 1/4 = 0.25. 200 × 0.25 = 50 semillas verdes.")),
        ("bio", t("A team measured the shell length (cm) of 40 sea turtles on a nesting beach and grouped the data in this histogram.", "Un equipo midió la longitud del caparazón (cm) de 40 tortugas marinas y agrupó los datos en este histograma."),
         hist(t("Shell length (cm)", "Longitud del caparazón (cm)"), t("Number of turtles", "Número de tortugas"), [("80–90", 5), ("90–100", 10), ("100–110", 14), ("110–120", 8), ("120–130", 3)], 4),
         t("In which interval are there the most turtles?", "¿En qué intervalo hay más tortugas?"), ["80–90 cm", "90–100 cm", "100–110 cm", "110–120 cm"], 2,
         t("The tallest bar is 100–110 cm, with 14 turtles: that is the modal interval.", "La barra más alta es 100–110 cm, con 14 tortugas: es el intervalo modal.")),
        ("bio", t("A study finds that in towns where people eat more ice cream, there are also more sunburns. The correlation is very strong.", "Un estudio observa que en los pueblos donde se come más helado también hay más quemaduras solares. La correlación es muy fuerte."),
         disp(t("Ice cream sales", "Venta de helado"), t("Sunburns", "Quemaduras solares"), [[10, 12], [20, 18], [30, 30], [40, 35], [50, 48], [60, 55], [70, 66], [80, 78]], sube),
         t("What is the scientifically correct conclusion?", "¿Cuál es la conclusión científicamente correcta?"),
         [t("Eating ice cream causes sunburns.", "Comer helado causa quemaduras solares."), t("Sunburns make people buy ice cream.", "Las quemaduras hacen que la gente compre helado."), t("A third variable (summer heat) probably causes both.", "Una tercera variable (el calor del verano) probablemente causa ambas."), t("There is no real relationship; it is a coincidence.", "No hay relación real; es coincidencia.")], 2,
         t("Correlation is not cause: hot, sunny days make people eat more ice cream and get more sunburns.", "Correlación no es causa: los días calurosos y soleados hacen comer más helado y quemarse más.")),
        ("bio", t("An ecologist wants to estimate the average number of eggs per nest of a migrating bird. She has four options for her sample.", "Una ecóloga quiere estimar el número medio de huevos por nido de un ave migratoria. Tiene cuatro opciones de muestra."), "",
         t("Which sample would give the most representative estimate?", "¿Qué muestra daría la estimación más representativa?"),
         [t("10 nests chosen at random from the whole nesting area", "10 nidos elegidos al azar en toda la zona"), t("10 nests from the easiest spot to reach", "10 nidos del lugar más accesible"), t("10 nests studied in earlier years", "10 nidos ya estudiados en años anteriores"), t("Only nests seen from the trail", "Solo nidos visibles desde el camino")], 0,
         t("A random sample reduces selection bias. The others are biased: easy spots may differ, old nests may not be typical, and hidden nests are left out.", "Una muestra al azar reduce el sesgo de selección. Las otras tienen sesgo: el lugar fácil puede ser distinto, los nidos ya estudiados quizá no sean típicos y los escondidos quedan fuera.")),
        ("bio", t("A bacteria culture doubles every 30 minutes. At 9:00 a.m. there are 1,000 bacteria.", "Un cultivo de bacterias se duplica cada 30 minutos. A las 9:00 hay 1,000 bacterias."),
         lin(t("Minutes after 9:00", "Minutos desde las 9:00"), t("Bacteria", "Bacterias"), [[0, 1000], [30, 2000], [60, 4000], [90, 8000], [120, 16000]], 30),
         t("If the trend continues, how many bacteria will there be at 11:00 a.m.?", "Si la tendencia continúa, ¿cuántas bacterias habrá a las 11:00?"), ["4,000", "8,000", "16,000", "32,000"], 2,
         t("Two hours = four 30-minute periods: 1,000 → 2,000 → 4,000 → 8,000 → 16,000.", "Dos horas = cuatro periodos de 30 minutos: 1,000 → 2,000 → 4,000 → 8,000 → 16,000.")),
        ("qui", t("A chemist measures the pH of a polluted river at seven points. In order: 5.8, 6.1, 6.3, 6.5, 6.8, 7.1, 8.2.", "Un químico mide el pH de un río contaminado en siete puntos. Ordenados: 5.8, 6.1, 6.3, 6.5, 6.8, 7.1, 8.2."), "",
         t("What is the median pH, and why is it better than the mean here?", "¿Cuál es la mediana del pH y por qué es preferible a la media aquí?"),
         [t("6.5; an extreme value (8.2) pulls the mean", "6.5; hay un valor extremo (8.2) que distorsiona la media"), t("6.7; it is always better", "6.7; siempre es preferible"), t("6.8; it is the most common value", "6.8; es el valor más común"), t("7.0; there is no difference", "7.0; no hay diferencia")], 0,
         t("With 7 ordered values the median is the 4th: 6.5. The mean (about 6.69) is pulled up by 8.2.", "Con 7 datos ordenados, la mediana es el 4.º: 6.5. La media (unos 6.69) sube por el 8.2.")),
        ("qui", t("To check a scale, a technician weighs the same sample five times: 12.45, 12.47, 12.46, 12.48, 12.44 g.", "Para evaluar una balanza, un técnico pesa la misma muestra cinco veces: 12.45, 12.47, 12.46, 12.48, 12.44 g."), "",
         t("What is the range of the measurements?", "¿Cuál es el rango de las mediciones?"), ["0.02 g", "0.04 g", "0.46 g", "12.46 g"], 1,
         t("12.48 − 12.44 = 0.04 g. A small range means good precision.", "12.48 − 12.44 = 0.04 g. Un rango pequeño indica buena precisión.")),
        ("qui", t("In a mix of ions, 40% are Na⁺ and 60% are K⁺. Two ions are drawn at random, with replacement.", "En una mezcla de iones, el 40 % son Na⁺ y el 60 % son K⁺. Se extraen dos al azar, con reemplazo."), "",
         t("What is the probability of drawing two Na⁺ ions in a row?", "¿Cuál es la probabilidad de extraer dos Na⁺ seguidos?"), ["0.04 (4%)", "0.16 (16%)", "0.40 (40%)", "0.80 (80%)"], 1,
         t("Independent events: 0.40 × 0.40 = 0.16.", "Sucesos independientes: 0.40 × 0.40 = 0.16.")),
        ("qui", t("In a reaction experiment, the reaction time (s) was measured in 20 trials of the same reaction.", "En un experimento de cinética se midió el tiempo de reacción (s) en 20 ensayos de la misma reacción."),
         hist(t("Reaction time (s)", "Tiempo de reacción (s)"), t("Number of trials", "Número de ensayos"), [("2–3", 2), ("3–4", 4), ("4–5", 7), ("5–6", 5), ("6–7", 2)], 2),
         t("About what percent of the trials took between 4 and 6 seconds?", "¿Qué porcentaje de los ensayos tardó, aproximadamente, entre 4 y 6 segundos?"), ["25%", "40%", "60%", "75%"], 2,
         t("4–5 s (7) + 5–6 s (5) = 12 trials out of 20: 12 ÷ 20 = 60%.", "4–5 s (7) + 5–6 s (5) = 12 de 20 ensayos: 12 ÷ 20 = 60 %.")),
        ("qui", t("A chemist graphs reaction speed against temperature, keeping all other variables the same.", "Un químico grafica la velocidad de una reacción contra la temperatura, controlando todas las demás variables."),
         disp(t("Temperature (°C)", "Temperatura (°C)"), t("Speed (mol/s)", "Velocidad (mol/s)"), [[10, 1.1], [20, 2.0], [30, 3.2], [40, 3.9], [50, 5.1], [60, 6.0]], sube),
         t("Unlike the ice cream example, why CAN we say here that temperature causes the change in speed?", "A diferencia del ejemplo del helado, ¿por qué SÍ podemos inferir aquí que la temperatura causa el cambio de velocidad?"),
         [t("Because the correlation is stronger.", "Porque la correlación es más fuerte."), t("Because it is a controlled experiment where only temperature changed.", "Porque es un experimento controlado en el que solo cambió la temperatura."), t("Because speed and temperature are always related.", "Porque siempre están relacionadas."), t("Because the chemist is an expert.", "Porque el químico es un experto.")], 1,
         t("The key is control: when you change one variable on purpose and keep the rest the same, you can infer cause. Observational studies cannot.", "La clave es el control: cuando se cambia una variable a propósito y se mantienen las demás, se puede inferir causa. Los estudios observacionales no.")),
        ("qui", t("A chemist measures the concentration of a reactant over time. The data follow a clear straight-line decrease.", "Un químico mide la concentración de un reactivo a distintos tiempos. Los datos siguen una clara tendencia lineal decreciente."),
         lin(t("Time (s)", "Tiempo (s)"), t("Concentration (M)", "Concentración (M)"), [[0, 1.00], [10, 0.84], [20, 0.68], [30, 0.52], [40, 0.36]], 10),
         t("If the trend continues, what will the concentration be at 50 seconds?", "Si la tendencia continúa, ¿cuál será la concentración a los 50 segundos?"), ["0.10 M", "0.20 M", "0.40 M", "0.50 M"], 1,
         t("It drops 0.16 M every 10 s: 0.36 − 0.16 = 0.20 M (if the trend continues).", "Baja 0.16 M cada 10 s: 0.36 − 0.16 = 0.20 M (si la tendencia se mantiene).")),
        ("fis", t("A student times a ball falling 4.9 m, five times: 1.02, 0.98, 1.05, 1.00, 0.99 s.", "Un estudiante cronometra cinco veces la caída de una pelota desde 4.9 m: 1.02, 0.98, 1.05, 1.00, 0.99 s."), "",
         t("What is the mean time, rounded to two decimal places?", "¿Cuál es el tiempo medio, redondeado a dos decimales?"), ["0.99 s", "1.00 s", "1.01 s", "1.05 s"], 2,
         t("Sum = 5.04; 5.04 ÷ 5 = 1.008, which rounds to 1.01 s. Averaging repeated measurements reduces random error.", "Suma = 5.04; 5.04 ÷ 5 = 1.008, que se redondea a 1.01 s. Promediar mediciones repetidas reduce el error aleatorio.")),
        ("fis", t("Two students measured the speed of sound five times each (m/s).", "Dos estudiantes midieron la velocidad del sonido cinco veces cada uno (m/s)."),
         tb2([t("Measurement", "Medición"), "1", "2", "3", "4", "5", t("Average", "Promedio")], [[t("Student A", "Estudiante A"), "340", "345", "343", "342", "345", "343"], [t("Student B", "Estudiante B"), "310", "375", "340", "360", "320", "341"]]),
         t("Which student measured more precisely, and why?", "¿Qué estudiante midió con más precisión, y por qué?"),
         [t("Student A, because his average is higher", "A, porque tiene mayor promedio"), t("Student B, because his values vary more", "B, porque sus valores son más diversos"), t("Student A, because his measurements have a smaller range", "A, porque sus mediciones tienen menor rango"), t("Neither; their averages are similar", "Ninguno; sus promedios son parecidos")], 2,
         t("Precision is how close repeated values are, not the average. Range A = 5 m/s; range B = 65 m/s.", "La precisión es cuán agrupadas están las mediciones, no el promedio. Rango A = 5 m/s; rango B = 65 m/s.")),
        ("fis", t("A radioactive isotope has a half-life of 10 years: in each 10-year period, each atom has a 50% chance of decaying.", "Un isótopo radiactivo tiene una vida media de 10 años: en cada periodo de 10 años, cada átomo tiene un 50 % de probabilidad de desintegrarse."), "",
         t("Starting with 800 atoms, how many are left after 30 years?", "Si se empieza con 800 átomos, ¿cuántos quedan después de 30 años?"), ["50", "100", "200", "400"], 1,
         t("Three half-lives: 800 → 400 → 200 → 100.", "Tres vidas medias: 800 → 400 → 200 → 100.")),
        ("fis", t("A physicist counts the waves detected by a seismograph in each frequency range.", "Un físico cuenta las ondas detectadas por un sismógrafo en cada rango de frecuencia."),
         tb2([t("Frequency (Hz)", "Frecuencia (Hz)"), "0–2", "2–4", "4–6", "6–8", "8–10"], [[t("Number of waves", "Número de ondas"), "8", "15", "22", "12", "3"]]),
         t("In which range were the MOST waves detected, and about what percent of the total are they?", "¿En qué rango se detectaron MÁS ondas, y qué porcentaje del total representan?"), [t("2–4 Hz, 25%", "2–4 Hz, 25 %"), t("4–6 Hz, 37%", "4–6 Hz, 37 %"), t("4–6 Hz, 22%", "4–6 Hz, 22 %"), t("6–8 Hz, 20%", "6–8 Hz, 20 %")], 1,
         t("Total = 60. The most is 4–6 Hz with 22: 22 ÷ 60 ≈ 0.367 ≈ 37%.", "Total = 60. El mayor es 4–6 Hz con 22: 22 ÷ 60 ≈ 0.367 ≈ 37 %.")),
        ("fis", t("In a pendulum experiment, the period (T) is graphed against the length (L) of several pendulums.", "En un experimento de péndulos se grafica el período (T) contra la longitud (L) de varios péndulos."),
         disp(t("Length L (m)", "Longitud L (m)"), t("Period T (s)", "Período T (s)"), [[0.2, 0.9], [0.4, 1.27], [0.6, 1.55], [0.8, 1.79], [1.0, 2.0], [1.2, 2.2]], sube),
         t("The correlation is strong and positive. What can you conclude DIRECTLY from the data?", "La correlación es fuerte y positiva. ¿Qué se puede concluir DIRECTAMENTE de los datos?"),
         [t("Length causes the period, nothing more.", "La longitud causa el período, sin más."), t("The longer the pendulum, the longer the period: a predictable relationship.", "A mayor longitud, mayor período: una relación predecible."), t("There is no way to know if they are related.", "No hay manera de saber si están relacionadas."), t("The period causes the length.", "El período causa la longitud.")], 1,
         t("From a correlation alone you can state the predictable relationship. (Here theory explains the cause, but the question asks what the data show.)", "De una correlación se puede afirmar la relación predecible. (Aquí la teoría explica la causa, pero la pregunta pide lo que muestran los datos.)")),
        ("fis", t("The distance covered by a car speeding up steadily was measured.", "Se midió la distancia recorrida por un auto que acelera de forma constante."),
         tb([t("Time (s)", "Tiempo (s)"), "1", "2", "3", "4"], [t("Distance (m)", "Distancia (m)"), "5", "20", "45", "80"]),
         t("The pattern is d = 5t². What distance is predicted at 5 seconds?", "El patrón es d = 5t². ¿Qué distancia se predice a los 5 segundos?"), ["100 m", "115 m", "125 m", "160 m"], 2,
         t("d = 5 × 5² = 5 × 25 = 125 m. The differences (15, 25, 35…) grow by 10 each step.", "d = 5 × 5² = 5 × 25 = 125 m. Las diferencias (15, 25, 35…) aumentan 10 cada vez.")),
        ("tie", t("The daily high temperatures (°C) in a city for one week were 28, 32, 30, 45, 31, 29, 33. The 45 °C day was an unusual heat wave.", "Las temperaturas máximas (°C) de una ciudad durante una semana fueron 28, 32, 30, 45, 31, 29, 33. El día de 45 °C fue una ola de calor anómala."), "",
         t("Which measure of center BEST represents a typical day?", "¿Qué medida de centro representa MEJOR un día típico?"),
         [t("The mean (32.6 °C), because it uses all the data", "La media (32.6 °C), porque usa todos los datos"), t("The median (31 °C), because the extreme value does not move it", "La mediana (31 °C), porque el valor extremo no la afecta"), t("The mode, because it is easiest", "La moda, porque es la más fácil"), t("The range, because it shows variation", "El rango, porque muestra la variación")], 1,
         t("The median (31 °C) resists outliers; the mean is pulled up by the 45 °C day.", "La mediana (31 °C) resiste los atípicos; la media sube por el día de 45 °C.")),
        ("tie", t("Last year, the earthquakes detected in a region ranged from magnitude 2.1 to 6.8.", "El año pasado, los sismos detectados en una región fueron de magnitud 2.1 a 6.8."), "",
         t("What is the range of magnitudes, and what does it say?", "¿Cuál es el rango de magnitudes y qué indica?"),
         [t("4.7; a lot of variation in strength", "4.7; mucha variación en la intensidad"), t("8.9; little variation", "8.9; poca variación"), t("6.8; only one big earthquake", "6.8; solo hubo un sismo grande"), t("2.1; all were small", "2.1; todos fueron pequeños")], 0,
         t("6.8 − 2.1 = 4.7: the region had both weak tremors and strong earthquakes.", "6.8 − 2.1 = 4.7: la región tuvo tanto temblores leves como sismos fuertes.")),
        ("tie", t("In the last 50 years, a coastal region has been hit by 15 hurricanes. Assume the frequency stays the same.", "En los últimos 50 años, una región costera ha recibido 15 huracanes. Suponga que la frecuencia se mantiene."), "",
         t("What is the estimated probability that a hurricane hits the region in any given year?", "¿Cuál es la probabilidad estimada de que un huracán la impacte en un año cualquiera?"), ["3%", "15%", "30%", "50%"], 2,
         t("15 ÷ 50 = 0.30 = 30%. Estimating probability from past frequency is common in climate and risk studies.", "15 ÷ 50 = 0.30 = 30 %. Estimar probabilidades a partir de frecuencias históricas es habitual en climatología.")),
        ("tie", t("This histogram shows the yearly rainfall (mm) at a weather station over 25 years.", "Este histograma muestra la precipitación anual (mm) de una estación meteorológica durante 25 años."),
         hist(t("Rainfall (mm)", "Precipitación (mm)"), t("Number of years", "Número de años"), [("200–400", 2), ("400–600", 6), ("600–800", 8), ("800–1000", 7), ("1000–1200", 2)], 2),
         t("How many years had between 600 and 1,000 mm of rain?", "¿Cuántos años tuvieron entre 600 y 1,000 mm de lluvia?"), ["8", "12", "15", "18"], 2,
         t("600–800 (8 years) + 800–1,000 (7 years) = 15 years.", "600–800 (8 años) + 800–1,000 (7 años) = 15 años.")),
        ("tie", t("Data from the last 100 years show a very strong correlation between CO₂ in the air and the global average temperature.", "Los datos de los últimos 100 años muestran una correlación muy fuerte entre el CO₂ atmosférico y la temperatura global media."),
         disp(t("CO₂ in the air (ppm)", "CO₂ atmosférico (ppm)"), t("Temperature anomaly (°C)", "Anomalía de temperatura (°C)"), [[300, -0.2], [310, -0.1], [320, 0.0], [340, 0.25], [360, 0.4], [380, 0.6], [400, 0.85], [415, 1.0]], sube),
         t("What is the strongest conclusion you can draw from these data alone?", "¿Cuál es la conclusión más sólida que se puede sacar de estos datos por sí solos?"),
         [t("CO₂ definitely causes the temperature rise.", "El CO₂ definitivamente causa el aumento de temperatura."), t("Temperature causes the CO₂ rise.", "La temperatura causa el aumento de CO₂."), t("There is a strong correlation; cause must be shown with experiments and physical models.", "Hay una correlación fuerte; la causa debe establecerse con experimentos y modelos físicos."), t("There is no meaningful relationship.", "No hay relación significativa.")], 2,
         t("Scientists do conclude that CO₂ causes warming, but that comes from the physics of the greenhouse effect, models, and experiments. THESE data alone only show correlation.", "La ciencia sí concluye que el CO₂ causa calentamiento, pero eso viene de la física del efecto invernadero, de modelos y de experimentos. ESTOS datos, por sí solos, solo muestran correlación.")),
        ("tie", t("The sea level at one station has risen an average of 3.2 mm per year for the last two decades.", "El nivel del mar en una estación ha subido una media de 3.2 mm por año en las dos últimas décadas."), "",
         t("If the rate stays the same, how much will the sea rise in the next 25 years?", "Si la tasa se mantiene, ¿cuánto subirá el mar en los próximos 25 años?"), ["3.2 mm", "32 mm", "80 mm", "320 mm"], 2,
         t("3.2 mm/year × 25 years = 80 mm (8 cm). This is a simple straight-line projection; models suggest the rate may speed up.", "3.2 mm/año × 25 años = 80 mm (8 cm). Es una proyección lineal simple; los modelos sugieren que la tasa podría acelerarse.")),
    ]
    PISTA = t("Read the question carefully: which measure, which interval, or which kind of conclusion does it ask for? Then check with the numbers.", "Lea con cuidado qué pide la pregunta: qué medida, qué intervalo o qué clase de conclusión. Después compruébelo con los números.")
    return [{"enun": f'<p><span class="chip-area">{A[a]}</span></p><p>{esc}</p>{vis}<p><strong>{q}</strong></p>', "ops": o, "ok": k, "pista": PISTA, "exp": e} for a, esc, vis, q, o, k, e in d]


def practica():
    A = {"en": ["measures", "best-measure", "precision", "counting", "order", "cientiestad"], "es": ["medidas", "mejor-medida", "precision", "conteo", "orden", "cientiestad"]}[C.L]
    mods = [
        (A[0], t("Mean, median, mode, range, and quartiles", "Media, mediana, moda, rango y cuartiles"),
         "      <p>" + t("A new data set every time. Order the data first. For quartiles, use the median of each half (if the count is odd, leave out the middle value).", "Un conjunto nuevo cada vez. Ordene primero los datos. Para los cuartiles, use la mediana de cada mitad (si la cantidad es impar, deje fuera el valor central).") + "</p>\n" + C.dec_campo("m1", t("Answer", "Respuesta"))),
        (A[1], t("Which measure fits best?", "¿Qué medida conviene?"), C.om("m2", t("Look for outliers, and ask whether the data are numbers.", "Busque valores atípicos y pregúntese si los datos son números."))),
        (A[2], t("Precise or accurate?", "¿Preciso o exacto?"), C.om("m3", t("Precise = close to each other. Accurate = close to the true value.", "Preciso = cerca entre sí. Exacto = cerca del valor verdadero."))),
        (A[3], t("Count the possibilities", "Cuente las posibilidades"),
         "      <p>" + t("Multiply the choices of each step. If the order does not matter, divide by the number of ways to arrange the chosen items.", "Multiplique las posibilidades de cada etapa. Si no importa el orden, divida entre las maneras de ordenar lo elegido.") + "</p>\n"
         + f'''      <div class="practica" id="m4">
        <div class="enun" id="m4-enun"></div>
        <div class="campos"><div class="campo"><label for="m4-r">{t("Answer", "Respuesta")}</label><input type="text" inputmode="numeric" autocomplete="off" class="ancho" id="m4-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="m4-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="m4-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="m4-fb" role="status"></div>
        <p class="marcador" id="m4-marcador"></p>
      </div>'''),
        (A[4], t("Does the order matter?", "¿Importa el orden?"), C.om("m5", t("If a different order gives a different result, it is a permutation.", "Si otro orden da otro resultado, es una permutación."))),
        (A[5], t("CientíEstad: statistics in science", "CientíEstad: estadística en ciencia"), C.om("m6", t("Twenty-four questions from biology, chemistry, physics, and Earth science, as on the GED® test.", "Veinticuatro preguntas de biología, química, física y ciencias de la Tierra, como en el examen GED®."))),
    ]
    js = (C.js_datos("MED", banco_medida()) + C.js_datos("PRE", banco_precision()) + C.js_datos("ORD", banco_orden()) + C.js_datos("EST", banco_cientiestad()) +
          js_medidas() + js_conteo() +
          'creaPracticaDec("m1", gM);\ncreaBanco("m2", MED);\ncreaBanco("m3", PRE);\ncreaPracticaLibre("m4", gK);\ncreaBanco("m5", ORD);\ncreaBanco("m6", EST);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one · calculator included", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
