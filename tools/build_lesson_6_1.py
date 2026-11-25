"""Lesson 6.1 · U.S. customary units — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "6-1"

def regla():
    """A 12-inch ruler next to a 1-foot bar."""
    x0, w = 40, 560
    s = [f'<rect x="{x0}" y="30" width="{w}" height="60" rx="6" fill="#fff3c4" stroke="#8d6e00" stroke-width="2"/>']
    for i in range(13):
        x = x0 + w * i / 12
        s.append(f'<line x1="{x:.1f}" y1="30" x2="{x:.1f}" y2="{62 if i % 12 else 70}" stroke="#5d4600" stroke-width="2"/>')
        if 0 < i < 12:
            s.append(f'<line x1="{x - w / 24:.1f}" y1="30" x2="{x - w / 24:.1f}" y2="46" stroke="#5d4600" stroke-width="1.5"/>')
        s.append(f'<text x="{x:.1f}" y="84" text-anchor="middle" font-size="15" font-weight="700" fill="#3e2f00">{i}</text>')
    s.append(f'<line x1="{x0 + w * 11 / 12 + w / 24:.1f}" y1="30" x2="{x0 + w * 11 / 12 + w / 24:.1f}" y2="46" stroke="#5d4600" stroke-width="1.5"/>')
    s.append(f'<rect x="{x0}" y="110" width="{w}" height="34" rx="6" fill="#1565c0"/><text x="{x0 + w / 2}" y="133" text-anchor="middle" font-size="18" font-weight="700" fill="#fff">{t("1 foot = 12 inches", "1 pie = 12 pulgadas")}</text>')
    return svg("0 0 640 160", t("A ruler marked from 0 to 12 inches. Below it, a bar of the same length labeled 1 foot equals 12 inches.",
                                "Una regla marcada de 0 a 12 pulgadas. Debajo, una barra del mismo largo con el rótulo 1 pie es igual a 12 pulgadas."), "".join(s))

def galon():
    """1 gallon = 4 quarts = 8 pints = 16 cups, as stacked bars."""
    filas = [(1, t("gallon", "galón"), "#0d47a1"), (4, t("quarts", "cuartos"), "#1565c0"), (8, t("pints", "pintas"), "#1e88e5"), (16, t("cups", "tazas"), "#64b5f6")]
    x0, w, s = 150, 450, []
    for k, (n, nom, c) in enumerate(filas):
        y = 18 + k * 46
        s.append(f'<text x="{x0 - 12}" y="{y + 25}" text-anchor="end" font-size="16" font-weight="700" fill="#1a2330">{n} {nom}</text>')
        for i in range(n):
            s.append(f'<rect x="{x0 + w * i / n:.1f}" y="{y}" width="{w / n:.1f}" height="36" fill="{c}" stroke="#fff" stroke-width="2"/>')
    return svg("0 0 640 200", t("Four bars of the same length. The first is 1 gallon. The second is split into 4 quarts, the third into 8 pints, and the fourth into 16 cups.",
                                "Cuatro barras del mismo largo. La primera es 1 galón. La segunda está dividida en 4 cuartos, la tercera en 8 pintas y la cuarta en 16 tazas."), "".join(s))

def leccion():
    n = N
    s1 = f'''<p>{t("To measure something, we compare it with a <strong>unit</strong>: a fixed amount we all agree on. In the United States, people use the <strong>U.S. customary system</strong> (inches, pounds, gallons…). It is the system you see on rulers, scales, recipes, and road signs, and it appears on the GED® test.",
"Para medir algo, lo comparamos con una <strong>unidad</strong>: una cantidad fija en la que todos estamos de acuerdo. En los Estados Unidos se usa el <strong>sistema inglés</strong> (pulgadas, libras, galones…), también llamado sistema usual de los Estados Unidos. Es el sistema que se ve en las reglas, las básculas, las recetas y las señales de tránsito, y aparece en el examen de GED®.")}</p>
<p>{t("In this lesson you will work with three kinds of measures:", "En esta lección va a trabajar con tres tipos de medidas:")}</p>
<ul>
<li><strong>{t("Length", "Longitud")}</strong>: {t("how long, how tall, or how far.", "qué tan largo, qué tan alto o qué tan lejos.")}</li>
<li><strong>{t("Weight", "Peso")}</strong>: {t("how heavy.", "qué tan pesado.")}</li>
<li><strong>{t("Capacity", "Capacidad")}</strong>: {t("how much liquid a container holds.", "cuánto líquido cabe en un recipiente.")}</li>
</ul>
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>To compare, add, or subtract two measures, they must be in the <strong>same unit</strong>. That is why we learn to <strong>convert</strong>: to change a measure from one unit to another without changing its size.</p>",
"<p>Para comparar, sumar o restar dos medidas, tienen que estar en la <strong>misma unidad</strong>. Por eso aprendemos a <strong>convertir</strong>: a cambiar una medida de una unidad a otra sin cambiar su tamaño.</p>"))}'''

    s2 = f'''<p>{t("The four units of length you will use most are the inch, the foot, the yard, and the mile.", "Las cuatro unidades de longitud que más va a usar son la pulgada, el pie, la yarda y la milla.")}</p>
{regla()}
{tabla(t("Units of length and their equivalences", "Unidades de longitud y sus equivalencias"), t("Units of length in the U.S. customary system", "Unidades de longitud del sistema inglés"),
       [t("Unit", "Unidad"), t("Abbreviation", "Abreviatura"), t("Equivalence", "Equivalencia"), t("About the size of…", "Más o menos el tamaño de…")],
       [[t("inch", "pulgada"), "in", "—", t("the width of a quarter", "el ancho de una moneda de 25 centavos")],
        [t("foot", "pie"), "ft", t("1 ft = 12 in", "1 pie = 12 pulgadas"), t("a sheet of paper, the long way", "una hoja de papel, a lo largo")],
        [t("yard", "yarda"), "yd", t("1 yd = 3 ft = 36 in", "1 yarda = 3 pies = 36 pulgadas"), t("a big step of an adult", "un paso largo de una persona adulta")],
        [t("mile", "milla"), "mi", t("1 mi = 5,280 ft", "1 milla = 5,280 pies"), t("about 20 minutes walking", "unos 20 minutos caminando")]])}
{caja("ojo", t("Abbreviations", "Las abreviaturas"), t("<p>The abbreviations (in, ft, yd, mi) are the ones you will see on rulers, maps, and the GED® test. Do not mix up <strong>ft</strong> (foot) and <strong>in</strong> (inch): 6 ft is a tall person; 6 in is a short pencil.</p>",
"<p>Las abreviaturas vienen del inglés (in, ft, yd, mi): son las que verá en reglas, mapas y en el examen de GED®. No confunda <strong>ft</strong> (pie) con <strong>in</strong> (pulgada): 6 ft es una persona alta; 6 in es un lápiz corto.</p>"))}
{ejemplo(t("Example: how many inches tall is a door that is 7 feet tall?", "Ejemplo: ¿cuántas pulgadas de alto tiene una puerta de 7 pies?"),
  [("1", t("Find the equivalence.", "Busque la equivalencia."), t("1 foot = 12 inches.", "1 pie = 12 pulgadas.")),
   ("2", t("Each foot is 12 inches.", "Cada pie son 12 pulgadas."), t("7 feet are 7 groups of 12: 7 × 12 = 84.", "7 pies son 7 grupos de 12: 7 × 12 = 84.")),
   ("✓", t("Answer.", "Respuesta."), t("The door is <strong>84 inches</strong> tall.", "La puerta tiene <strong>84 pulgadas</strong> de alto."))])}
{practica("p1", t("Practice 1 — Units of length", "Práctica 1 — Unidades de longitud"), t("How many feet are in <strong>4 yards</strong>?", "¿Cuántos pies hay en <strong>4 yardas</strong>?"),
          [("a", t("7 feet", "7 pies")), ("b", t("12 feet", "12 pies")), ("c", t("48 feet", "48 pies")), ("d", t("1 foot", "1 pie"))])}
{enlace(n, t("choose-unit", "elegir-unidad"), t("choose the right unit", "elegir la unidad correcta"), t("Decide which unit fits best to measure everyday things.", "Decida qué unidad conviene más para medir cosas de todos los días."))}'''

    s3 = f'''<p>{t("<strong>Weight</strong> tells how heavy something is. <strong>Capacity</strong> tells how much liquid a container holds.", "El <strong>peso</strong> dice qué tan pesado es algo. La <strong>capacidad</strong> dice cuánto líquido cabe en un recipiente.")}</p>
{tabla(t("Units of weight and their equivalences", "Unidades de peso y sus equivalencias"), t("Units of weight in the U.S. customary system", "Unidades de peso del sistema inglés"),
       [t("Unit", "Unidad"), t("Abbreviation", "Abreviatura"), t("Equivalence", "Equivalencia"), t("About the weight of…", "Más o menos el peso de…")],
       [[t("ounce", "onza"), "oz", "—", t("a slice of bread", "una rebanada de pan")],
        [t("pound", "libra"), "lb", t("1 lb = 16 oz", "1 libra = 16 onzas"), t("a loaf of bread", "un pan de molde entero")],
        [t("ton", "tonelada"), "T", t("1 T = 2,000 lb", "1 tonelada = 2,000 libras"), t("a small car", "un carro pequeño")]])}
<p>{t("For capacity, picture a gallon of milk. It holds 4 quarts, or 8 pints, or 16 cups:", "Para la capacidad, imagine un galón de leche. Le caben 4 cuartos, u 8 pintas, o 16 tazas:")}</p>
{galon()}
{tabla(t("Units of capacity and their equivalences", "Unidades de capacidad y sus equivalencias"), t("Units of capacity in the U.S. customary system", "Unidades de capacidad del sistema inglés"),
       [t("Unit", "Unidad"), t("Abbreviation", "Abreviatura"), t("Equivalence", "Equivalencia")],
       [[t("fluid ounce", "onza líquida"), "fl oz", "—"],
        [t("cup", "taza"), "c", t("1 c = 8 fl oz", "1 taza = 8 onzas líquidas")],
        [t("pint", "pinta"), "pt", t("1 pt = 2 c", "1 pinta = 2 tazas")],
        [t("quart", "cuarto (de galón)"), "qt", t("1 qt = 2 pt = 4 c", "1 cuarto = 2 pintas = 4 tazas")],
        [t("gallon", "galón"), "gal", t("1 gal = 4 qt = 16 c", "1 galón = 4 cuartos = 16 tazas")]])}
{caja("ojo", t("Watch out! Two kinds of ounces", "¡Cuidado! Dos tipos de onzas"), t("<p>An <strong>ounce</strong> (oz) measures weight. A <strong>fluid ounce</strong> (fl oz) measures capacity. A label that says \"12 fl oz\" tells how much drink is in the can, not how heavy the can is.</p>",
"<p>La <strong>onza</strong> (oz) mide peso. La <strong>onza líquida</strong> (fl oz) mide capacidad. Una etiqueta que dice «12 fl oz» dice cuánta bebida trae la lata, no cuánto pesa la lata.</p>"))}
{practica("p2", t("Practice 2 — Capacity", "Práctica 2 — Capacidad"), t("How many cups are in <strong>1 gallon</strong>?", "¿Cuántas tazas hay en <strong>1 galón</strong>?"),
          [("a", t("4 cups", "4 tazas")), ("b", t("8 cups", "8 tazas")), ("c", t("16 cups", "16 tazas")), ("d", t("2 cups", "2 tazas"))])}'''

    s4 = f'''<p>{t("To convert, ask yourself one question: <strong>am I going to a smaller unit or to a bigger unit?</strong>", "Para convertir, hágase una sola pregunta: <strong>¿voy a una unidad más pequeña o a una más grande?</strong>")}</p>
{tabla(t("The rule for converting units", "La regla para convertir unidades"), t("When to multiply and when to divide to convert units", "Cuándo multiplicar y cuándo dividir para convertir unidades"),
       [t("You go from…", "Va de…"), t("You need…", "Necesita…"), t("So you…", "Así que…"), t("Example", "Ejemplo")],
       [[t("a big unit to a small unit", "una unidad grande a una pequeña"), t("more units", "más unidades"), t("<strong>multiply</strong>", "<strong>multiplica</strong>"), t("3 ft = 3 × 12 = 36 in", "3 pies = 3 × 12 = 36 pulgadas")],
        [t("a small unit to a big unit", "una unidad pequeña a una grande"), t("fewer units", "menos unidades"), t("<strong>divide</strong>", "<strong>divide</strong>"), t("48 oz = 48 ÷ 16 = 3 lb", "48 onzas = 48 ÷ 16 = 3 libras")]])}
{caja("tip", t("A way to remember", "Una forma de recordarlo"), t("<p>Small units are like small coins: you need <strong>more</strong> of them. 1 dollar is 4 quarters. In the same way, 1 foot is 12 inches. Going to a smaller unit, the number gets bigger.</p>",
"<p>Las unidades pequeñas son como las monedas pequeñas: se necesitan <strong>más</strong>. 1 dólar son 4 monedas de 25 centavos. De la misma manera, 1 pie son 12 pulgadas. Al ir a una unidad más pequeña, el número se hace más grande.</p>"))}
{ejemplo(t("Example: how many pounds are 80 ounces?", "Ejemplo: ¿cuántas libras son 80 onzas?"),
  [("1", t("Big or small?", "¿Grande o pequeña?"), t("Ounces are small; pounds are big. You go to a bigger unit, so you divide.", "Las onzas son pequeñas; las libras son grandes. Va a una unidad más grande, así que divide.")),
   ("2", t("Divide by the equivalence.", "Divida entre la equivalencia."), t("1 lb = 16 oz, so 80 ÷ 16 = 5.", "1 libra = 16 onzas, así que 80 ÷ 16 = 5.")),
   ("✓", t("Check it.", "Compruébelo."), t("5 × 16 = 80 ✓. 80 ounces are <strong>5 pounds</strong>.", "5 × 16 = 80 ✓. 80 onzas son <strong>5 libras</strong>."))])}
<p>{t("Sometimes the division is not exact. Then we write the answer with <strong>two units</strong>, as on a growth chart: 75 inches = 6 feet and 3 inches.", "A veces la división no es exacta. Entonces escribimos la respuesta con <strong>dos unidades</strong>, como en una tabla de estatura: 75 pulgadas = 6 pies y 3 pulgadas.")}</p>
{ejemplo(t("Example: write 75 inches in feet and inches", "Ejemplo: escriba 75 pulgadas en pies y pulgadas"),
  [("1", t("Divide by 12.", "Divida entre 12."), t("75 ÷ 12 = 6, remainder 3 (because 6 × 12 = 72, and 75 − 72 = 3).", "75 ÷ 12 = 6, residuo 3 (porque 6 × 12 = 72, y 75 − 72 = 3).")),
   ("2", t("Read the result.", "Lea el resultado."), t("The quotient is the feet; the remainder is the inches left over.", "El cociente son los pies; el residuo son las pulgadas que sobran.")),
   ("✓", t("Answer.", "Respuesta."), t("75 inches = <strong>6 ft 3 in</strong>.", "75 pulgadas = <strong>6 pies 3 pulgadas</strong>."))])}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>Convert 7 feet to inches: type {T("7")} {T("×")} {T("1")}{T("2")} {T("enter")}. The screen shows 84.</p>
<p>Convert 80 ounces to pounds: type {T("8")}{T("0")} {T("÷")} {T("1")}{T("6")} {T("enter")}. The screen shows 5.</p>""",
f"""<p>Convierta 7 pies a pulgadas: escriba {T("7")} {T("×")} {T("1")}{T("2")} {T("enter")}. La pantalla muestra 84.</p>
<p>Convierta 80 onzas a libras: escriba {T("8")}{T("0")} {T("÷")} {T("1")}{T("6")} {T("enter")}. La pantalla muestra 5.</p>"""))}
{practica("p3", t("Practice 3 — From small to big", "Práctica 3 — De pequeña a grande"), t("How many pounds are <strong>96 ounces</strong>? (Use 1 lb = 16 oz.)", "¿Cuántas libras son <strong>96 onzas</strong>? (Use 1 libra = 16 onzas)."),
          [("a", t("6 pounds", "6 libras")), ("b", t("1,536 pounds", "1,536 libras")), ("c", t("80 pounds", "80 libras")), ("d", t("112 pounds", "112 libras"))])}
{practica("p4", t("Practice 4 — Two units", "Práctica 4 — Dos unidades"), t("A board is <strong>100 inches</strong> long. How long is it in feet and inches?", "Una tabla mide <strong>100 pulgadas</strong> de largo. ¿Cuánto mide en pies y pulgadas?"),
          [("a", t("10 ft 0 in", "10 pies 0 pulgadas")), ("b", t("8 ft 4 in", "8 pies 4 pulgadas")), ("c", t("8 ft 2 in", "8 pies 2 pulgadas")), ("d", t("9 ft 4 in", "9 pies 4 pulgadas"))])}
{enlace(n, t("convert", "convertir"), t("convert units", "convertir unidades"), t("Multiply or divide by the equivalence, and check your answer.", "Multiplique o divida entre la equivalencia, y compruebe su respuesta."))}
{enlace(n, t("two-units", "dos-unidades"), t("measures with two units", "medidas con dos unidades"), t("Write measures like 75 inches as 6 ft 3 in.", "Escriba medidas como 75 pulgadas en la forma 6 pies 3 pulgadas."))}
{enlace(n, t("compare", "comparar"), t("compare measures", "comparar medidas"), t("Put both measures in the same unit and decide which is more.", "Ponga las dos medidas en la misma unidad y decida cuál es mayor."))}'''

    secciones = [("s-" + t("units", "unidades"), t("Measuring with U.S. units", "Medir con el sistema inglés"), s1),
                 ("s-" + t("length", "longitud"), t("Length: inch, foot, yard, mile", "Longitud: pulgada, pie, yarda, milla"), s2),
                 ("s-" + t("weight-capacity", "peso-capacidad"), t("Weight and capacity", "Peso y capacidad"), s3),
                 ("s-" + t("convert", "convertir"), t("Convert: multiply or divide?", "Convertir: ¿multiplicar o dividir?"), s4)]

    lesson = {"next": t("Lesson 6.2", "Lección 6.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {
          "a": t("7 is 4 + 3. Each yard is 3 feet, so 4 yards are 4 groups of 3.", "7 es 4 + 3. Cada yarda son 3 pies, así que 4 yardas son 4 grupos de 3."),
          "c": t("48 is 4 × 12. That uses inches. 1 yard = 3 feet.", "48 es 4 × 12. Eso usa pulgadas. 1 yarda = 3 pies."),
          "d": t("Feet are smaller than yards, so you need more feet, not fewer.", "Los pies son más pequeños que las yardas, así que necesita más pies, no menos.")},
       "right": t("1 yd = 3 ft, so 4 yd = 4 × 3 = 12 ft.", "1 yarda = 3 pies, así que 4 yardas = 4 × 3 = 12 pies."),
       "solution": t("Each yard is 3 feet. 4 yards are 4 × 3 = 12 feet.", "Cada yarda son 3 pies. 4 yardas son 4 × 3 = 12 pies.")},
      "p2": {"ok": "c", "hints": {
          "a": t("4 is the number of quarts in a gallon. Each quart is 4 cups.", "4 es la cantidad de cuartos en un galón. Cada cuarto son 4 tazas."),
          "b": t("8 is the number of pints in a gallon. Each pint is 2 cups.", "8 es la cantidad de pintas en un galón. Cada pinta son 2 tazas."),
          "d": t("2 cups make 1 pint, not 1 gallon. A gallon is much bigger.", "2 tazas forman 1 pinta, no 1 galón. Un galón es mucho más grande.")},
       "right": t("1 gallon = 4 quarts, and each quart is 4 cups: 4 × 4 = 16 cups.", "1 galón = 4 cuartos, y cada cuarto son 4 tazas: 4 × 4 = 16 tazas."),
       "solution": t("1 gallon = 4 quarts = 8 pints = 16 cups.", "1 galón = 4 cuartos = 8 pintas = 16 tazas.")},
      "p3": {"ok": "a", "hints": {
          "b": t("1,536 is 96 × 16. You go from a small unit to a big unit, so divide.", "1,536 es 96 × 16. Va de una unidad pequeña a una grande, así que divida."),
          "c": t("80 is 96 − 16. Divide by 16; do not subtract.", "80 es 96 − 16. Divida entre 16; no reste."),
          "d": t("112 is 96 + 16. Divide by 16 to find how many groups of 16 ounces there are.", "112 es 96 + 16. Divida entre 16 para hallar cuántos grupos de 16 onzas hay.")},
       "right": t("96 ÷ 16 = 6 pounds. Check: 6 × 16 = 96.", "96 ÷ 16 = 6 libras. Comprobación: 6 × 16 = 96."),
       "solution": t("Ounces → pounds goes to a bigger unit: divide. 96 ÷ 16 = 6 pounds.", "De onzas a libras va a una unidad más grande: divida. 96 ÷ 16 = 6 libras.")},
      "p4": {"ok": "b", "hints": {
          "a": t("A foot is 12 inches, not 10. Divide 100 by 12.", "Un pie son 12 pulgadas, no 10. Divida 100 entre 12."),
          "c": t("8 × 12 = 96, so the inches left over are 100 − 96 = 4, not 2.", "8 × 12 = 96, así que las pulgadas que sobran son 100 − 96 = 4, no 2."),
          "d": t("9 ft is 108 inches, which is more than 100.", "9 pies son 108 pulgadas, más que 100.")},
       "right": t("100 ÷ 12 = 8, remainder 4: 8 ft 4 in.", "100 ÷ 12 = 8, residuo 4: 8 pies 4 pulgadas."),
       "solution": t("100 ÷ 12 = 8 with remainder 4 (8 × 12 = 96, 100 − 96 = 4). The board is 8 ft 4 in.", "100 ÷ 12 = 8 con residuo 4 (8 × 12 = 96, 100 − 96 = 4). La tabla mide 8 pies 4 pulgadas.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("We count by tens with money, but a foot has 12 inches.", "Con el dinero contamos de diez en diez, pero un pie tiene 12 pulgadas."), "c": t("3 is the number of feet in a yard.", "3 es la cantidad de pies en una yarda."), "d": t("36 is the number of inches in a yard.", "36 es la cantidad de pulgadas en una yarda.")},
            "solution": t("1 foot = 12 inches. Look at a ruler: it is 12 inches long.", "1 pie = 12 pulgadas. Mire una regla: mide 12 pulgadas.")},
      "B": {"ok": "d", "hints": {"a": t("Inches are for small things, like a pencil.", "Las pulgadas son para cosas pequeñas, como un lápiz."), "b": t("Feet are for things like a room or a person's height.", "Los pies son para cosas como un cuarto o la estatura de una persona."), "c": t("Yards are for things like a football field.", "Las yardas son para cosas como una cancha de fútbol americano.")},
            "solution": t("Distances between cities are long: we measure them in miles.", "Las distancias entre ciudades son largas: se miden en millas.")},
      "C": {"ok": "a", "hints": {"b": t("16 is 4 + 12. Each foot is 12 inches: multiply.", "16 es 4 + 12. Cada pie son 12 pulgadas: multiplique."), "c": t("You go to a smaller unit, so the number gets bigger, not smaller.", "Va a una unidad más pequeña, así que el número se hace más grande, no más pequeño."), "d": t("36 inches is 3 feet, not 4.", "36 pulgadas son 3 pies, no 4.")},
            "solution": t("4 feet = 4 × 12 = 48 inches.", "4 pies = 4 × 12 = 48 pulgadas.")},
      "D": {"ok": "c", "hints": {"a": t("1,024 is 64 × 16. Pounds are bigger than ounces, so divide.", "1,024 es 64 × 16. Las libras son más grandes que las onzas, así que divida."), "b": t("48 is 64 − 16. Divide by 16; do not subtract.", "48 es 64 − 16. Divida entre 16; no reste."), "d": t("80 is 64 + 16. Divide by 16.", "80 es 64 + 16. Divida entre 16.")},
            "solution": t("64 ÷ 16 = 4 pounds.", "64 ÷ 16 = 4 libras.")},
      "E": {"ok": "b", "hints": {"a": t("7 is 3 + 4. Each gallon is 4 quarts: multiply.", "7 es 3 + 4. Cada galón son 4 cuartos: multiplique."), "c": t("6 is 3 × 2. A gallon is 4 quarts, not 2.", "6 es 3 × 2. Un galón son 4 cuartos, no 2."), "d": t("Quarts are smaller than gallons, so you need more quarts.", "Los cuartos son más pequeños que los galones, así que necesita más cuartos.")},
            "solution": t("3 gallons = 3 × 4 = 12 quarts.", "3 galones = 3 × 4 = 12 cuartos.")},
      "F": {"ok": "d", "hints": {"a": t("50 inches is not 5 feet: a foot is 12 inches, not 10.", "50 pulgadas no son 5 pies: un pie son 12 pulgadas, no 10."), "b": t("12 inches make another foot, so 4 ft 12 in is 5 ft, which is 60 inches.", "12 pulgadas forman otro pie, así que 4 pies 12 pulgadas son 5 pies, es decir, 60 pulgadas."), "c": t("6 ft is 72 inches, more than 50.", "6 pies son 72 pulgadas, más que 50.")},
            "solution": t("50 ÷ 12 = 4, remainder 2 (4 × 12 = 48). 50 inches = 4 ft 2 in.", "50 ÷ 12 = 4, residuo 2 (4 × 12 = 48). 50 pulgadas = 4 pies 2 pulgadas.")},
      "G": {"ok": "a", "hints": {"b": t("Put both in ounces: 2 pounds = 2 × 16 = 32 ounces.", "Ponga las dos en onzas: 2 libras = 2 × 16 = 32 onzas."), "c": t("2 pounds are 32 ounces, not 30.", "2 libras son 32 onzas, no 30."), "d": t("You can tell: convert to the same unit and compare.", "Sí se puede saber: convierta a la misma unidad y compare.")},
            "solution": t("2 pounds = 32 ounces, and 32 > 30. So 2 pounds is more.", "2 libras = 32 onzas, y 32 > 30. Así que 2 libras es más.")},
      "H": {"ok": "c", "hints": {"a": t("A quart is bigger than a cup: 1 quart = 4 cups.", "Un cuarto es más grande que una taza: 1 cuarto = 4 tazas."), "b": t("1 quart is already 4 cups, more than the 3 cups you need.", "1 cuarto ya son 4 tazas, más que las 3 tazas que necesita."), "d": t("1 quart is 4 cups, not 3.", "1 cuarto son 4 tazas, no 3.")},
            "solution": t("1 quart = 4 cups, and 4 cups is more than 3 cups. Yes, it is enough, with 1 cup left over.", "1 cuarto = 4 tazas, y 4 tazas es más que 3 tazas. Sí alcanza, y sobra 1 taza.")}
     }}

    quiz = [
     ("A", t("How many inches are in <strong>1 foot</strong>?", "¿Cuántas pulgadas hay en <strong>1 pie</strong>?"), [("a", "10"), ("b", "12"), ("c", "3"), ("d", "36")]),
     ("B", t("Which unit would you use to measure the distance between two cities?", "¿Qué unidad usaría para medir la distancia entre dos ciudades?"), [("a", t("inches", "pulgadas")), ("b", t("feet", "pies")), ("c", t("yards", "yardas")), ("d", t("miles", "millas"))]),
     ("C", t("<strong>4 feet</strong> = ___ inches", "<strong>4 pies</strong> = ___ pulgadas"), [("a", "48"), ("b", "16"), ("c", "3"), ("d", "36")]),
     ("D", t("<strong>64 ounces</strong> = ___ pounds", "<strong>64 onzas</strong> = ___ libras"), [("a", "1,024"), ("b", "48"), ("c", "4"), ("d", "80")]),
     ("E", t("<strong>3 gallons</strong> = ___ quarts", "<strong>3 galones</strong> = ___ cuartos"), [("a", "7"), ("b", "12"), ("c", "6"), ("d", "1")]),
     ("F", t("How do you write <strong>50 inches</strong> in feet and inches?", "¿Cómo se escriben <strong>50 pulgadas</strong> en pies y pulgadas?"), [("a", t("5 ft 0 in", "5 pies 0 pulgadas")), ("b", t("4 ft 12 in", "4 pies 12 pulgadas")), ("c", t("6 ft 2 in", "6 pies 2 pulgadas")), ("d", t("4 ft 2 in", "4 pies 2 pulgadas"))]),
     ("G", t("Which is more: <strong>2 pounds</strong> or <strong>30 ounces</strong>?", "¿Qué es más: <strong>2 libras</strong> o <strong>30 onzas</strong>?"), [("a", t("2 pounds", "2 libras")), ("b", t("30 ounces", "30 onzas")), ("c", t("They are equal.", "Son iguales.")), ("d", t("You cannot tell.", "No se puede saber."))]),
     ("H", t("A recipe needs <strong>3 cups</strong> of milk. You have <strong>1 quart</strong>. Is that enough?", "Una receta necesita <strong>3 tazas</strong> de leche. Usted tiene <strong>1 cuarto</strong>. ¿Le alcanza?"),
      [("a", t("No, 1 quart is less than 3 cups.", "No, 1 cuarto es menos que 3 tazas.")), ("b", t("No, you need 2 more quarts.", "No, necesita 2 cuartos más.")), ("c", t("Yes: 1 quart is 4 cups, more than 3 cups.", "Sí: 1 cuarto son 4 tazas, más que 3 tazas.")), ("d", t("Yes: 1 quart is exactly 3 cups.", "Sí: 1 cuarto son exactamente 3 tazas."))])]

    return B.pagina_leccion(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"),
        t("U.S. customary units: length, weight, and capacity", "Sistema inglés: longitud, peso y capacidad"),
        t("Inches, pounds, and gallons: learn the units you use every day, and how to change from one to another.", "Pulgadas, libras y galones: aprenda las unidades que usa todos los días y cómo pasar de una a otra."),
        ("📏", t("Multiply or divide?", "¿Multiplicar o dividir?")),
        [t("<strong>Choose</strong> the right unit to measure length, weight, or capacity.", "<strong>Elegir</strong> la unidad correcta para medir longitud, peso o capacidad."),
         t("<strong>Use</strong> the equivalences between U.S. customary units.", "<strong>Usar</strong> las equivalencias entre las unidades del sistema inglés."),
         t("<strong>Convert</strong> a measure to a bigger or a smaller unit.", "<strong>Convertir</strong> una medida a una unidad más grande o más pequeña."),
         t("<strong>Write</strong> a measure with two units, like 6 ft 3 in, and compare measures.", "<strong>Escribir</strong> una medida con dos unidades, como 6 pies 3 pulgadas, y comparar medidas.")],
        secciones,
        (t("Measure five things at home with a ruler or a tape measure: a table, a door, a window, your bed, and your height. Write each measure in inches, and then convert it to feet and inches.",
           "Mida cinco cosas de su casa con una regla o una cinta métrica: una mesa, una puerta, una ventana, su cama y su estatura. Escriba cada medida en pulgadas, y después conviértala a pies y pulgadas."),
         t("Look at the labels of three products in your kitchen: one in ounces, one in pounds, and one in fluid ounces or gallons. Convert each one to another unit (for example, a 32 oz bag to pounds).",
           "Mire las etiquetas de tres productos de su cocina: uno en onzas, uno en libras y uno en onzas líquidas o galones. Convierta cada uno a otra unidad (por ejemplo, una bolsa de 32 oz a libras).")),
        quiz,
        t("Self-check checklist for U.S. customary units", "Lista de autoevaluación del sistema inglés"),
        t("Self-check checklist: skills for U.S. customary units", "Lista de autoevaluación: destrezas con el sistema inglés"),
        [(t("Choose the right unit", "Elegir la unidad correcta"), t("I choose the best unit for length, weight, and capacity without hesitating.", "Elijo la mejor unidad de longitud, peso y capacidad sin dudar."), t("I choose well most of the time.", "Elijo bien la mayoría de las veces."), t("I mix up the kinds of units (for example, ounces and fluid ounces).", "Confundo los tipos de unidades (por ejemplo, onzas y onzas líquidas)."))
         , (t("Know the equivalences", "Conocer las equivalencias"), t("I know the main equivalences by heart or find them quickly in a table.", "Me sé las equivalencias principales o las encuentro rápido en una tabla."), t("I know some and look up the rest.", "Me sé algunas y busco las demás."), t("I do not know where to find them.", "No sé dónde encontrarlas."))
         , (t("Multiply or divide", "Multiplicar o dividir"), t("I always know whether to multiply or divide, and I check my answer.", "Siempre sé si multiplicar o dividir, y compruebo mi respuesta."), t("I get it right most of the time.", "Acierto la mayoría de las veces."), t("I often multiply when I should divide, or the other way around.", "Con frecuencia multiplico cuando debo dividir, o al revés."))
         , (t("Two units and comparing", "Dos unidades y comparar"), t("I write measures like 6 ft 3 in and compare measures in different units.", "Escribo medidas como 6 pies 3 pulgadas y comparo medidas en unidades distintas."), t("I do it with some help.", "Lo hago con un poco de ayuda."), t("I compare the numbers without converting first.", "Comparo los números sin convertir primero."))],
        t("<p>You can now choose U.S. customary units, use their equivalences, and convert from one unit to another. These skills appear in many GED® problems.</p>\n<p>In <strong>Lesson 6.2 · Metric system, time, and temperature</strong> you will meet the metric system, which works with tens like our decimals, and you will also measure time and temperature.</p>",
          "<p>Ya sabe elegir unidades del sistema inglés, usar sus equivalencias y convertir de una unidad a otra. Estas destrezas aparecen en muchos problemas del examen de GED®.</p>\n<p>En la <strong>Lección 6.2 · Sistema métrico, tiempo y temperatura</strong> conocerá el sistema métrico, que trabaja con dieces como nuestros decimales, y también medirá el tiempo y la temperatura.</p>"),
        ("6-2", ("", t("Lesson 6.2 · Metric system, time, and temperature", "Lección 6.2 · Sistema métrico, tiempo y temperatura"))),
        [(t("unit", "unidad"), t("A fixed amount used to measure, like an inch or a pound.", "Una cantidad fija que se usa para medir, como una pulgada o una libra.")),
         (t("length", "longitud"), t("How long, how tall, or how far something is.", "Qué tan largo, qué tan alto o qué tan lejos está algo.")),
         (t("weight", "peso"), t("How heavy something is.", "Qué tan pesado es algo.")),
         (t("capacity", "capacidad"), t("How much liquid a container holds.", "Cuánto líquido cabe en un recipiente.")),
         (t("equivalence", "equivalencia"), t("Two measures that are the same size, like 1 ft = 12 in.", "Dos medidas del mismo tamaño, como 1 pie = 12 pulgadas.")),
         (t("convert", "convertir"), t("To change a measure to another unit without changing its size.", "Cambiar una medida a otra unidad sin cambiar su tamaño."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "u": {"in": ["inch", "inches"], "ft": ["foot", "feet"], "yd": ["yard", "yards"], "mi": ["mile", "miles"], "oz": ["ounce", "ounces"], "lb": ["pound", "pounds"], "T": ["ton", "tons"],
        "floz": ["fluid ounce", "fluid ounces"], "c": ["cup", "cups"], "pt": ["pint", "pints"], "qt": ["quart", "quarts"], "gal": ["gallon", "gallons"]},
  "obj": [["the length of a pencil", "in"], ["the height of a door", "ft"], ["the distance from Chicago to Detroit", "mi"], ["the length of a football field", "yd"], ["the width of a phone", "in"], ["the distance you drive to work", "mi"], ["the length of a room", "ft"],
          ["the weight of a letter", "oz"], ["the weight of a bag of potatoes", "lb"], ["the weight of a truck", "T"], ["the weight of a slice of cheese", "oz"], ["the weight of a person", "lb"], ["the weight of an elephant", "T"],
          ["the juice in a small bottle", "floz"], ["the milk for a pancake recipe", "c"], ["the water in a bathtub", "gal"], ["the gas in a car's tank", "gal"], ["the milk in a carton for a family breakfast", "qt"]],
  "pregUnidad": "Which unit is best to measure <strong>{o}</strong>?",
  "chica": "That unit is too small for this: you would need a huge number of them.",
  "grande": "That unit is too big for this: the measure would be a tiny part of one.",
  "pistaUnidad": "Picture the thing and compare it with each unit.",
  "bienUnidad": "The best unit to measure {o} is <strong>{u}</strong>.",
  "cuantos": {"in": "How many", "ft": "How many", "yd": "How many", "mi": "How many", "oz": "How many", "lb": "How many", "T": "How many", "floz": "How many", "c": "How many", "pt": "How many", "qt": "How many", "gal": "How many"},
  "art": {"in": "the inch", "ft": "the foot", "yd": "the yard", "mi": "the mile", "oz": "the ounce", "lb": "the pound", "T": "the ton", "floz": "the fluid ounce", "c": "the cup", "pt": "the pint", "qt": "the quart", "gal": "the gallon"},
  "pregConv": "{c} <strong>{u2}</strong> are in <strong>{n} {u1}</strong>?",
  "solMult": "You go from a big unit to a small unit, so multiply. 1 {g} = {f} {p}, so {n} × {f} = <strong>{r}</strong> {u2}.",
  "solDiv": "You go from a small unit to a big unit, so divide. 1 {g} = {f} {p}, so {n} ÷ {f} = <strong>{r}</strong> {u2}.",
  "trampaMult": "You multiplied, but you go from a small unit to a big unit: there will be fewer units. Divide.",
  "trampaDiv": "You divided, but you go from a big unit to a small unit: there will be more units. Multiply.",
  "trampaSuma": "Adding the equivalence does not convert. Multiply or divide by {f}.",
  "pistaConv": "Find the equivalence. Big to small: multiply. Small to big: divide.",
  "pregDos": "Write <strong>{n} {u1}</strong> in {g} and {p}.",
  "dosU": "{q} {g} {r} {p}",
  "bienDos": "{n} ÷ {f} = {q}, remainder {r} ({q} × {f} = {m}). So {n} {u1} = {q} {g} {r} {p}.",
  "dosDigitos": "Careful: 1 {g1} is {f} {p}, not 10. Divide {n} by {f}.",
  "dosSinSimplificar": "{r} {p} make at least one more {g1}. The remainder must be less than {f}.",
  "dosUnoMas": "That is {m2} {p}, more than {n}. Check the quotient.",
  "pistaDos": "Divide by the equivalence: the quotient is the big unit, and the remainder is the small unit.",
  "pregComp": "Which is more: <strong>{a}</strong> or <strong>{b}</strong>?",
  "iguales": "They are equal.",
  "bienComp": "Put both in {p}: {a} = {n} × {f} = {v} {p}. {cmp}",
  "mayor": "{v} is more than {b}, so {a} is more.",
  "menor": "{v} is less than {b}, so {b2} is more.",
  "igual": "{v} = {b}, so they are equal.",
  "pistaComp": "Convert the big unit to the small unit first, then compare the numbers."
 },
 "es": {
  "u": {"in": ["pulgada", "pulgadas"], "ft": ["pie", "pies"], "yd": ["yarda", "yardas"], "mi": ["milla", "millas"], "oz": ["onza", "onzas"], "lb": ["libra", "libras"], "T": ["tonelada", "toneladas"],
        "floz": ["onza líquida", "onzas líquidas"], "c": ["taza", "tazas"], "pt": ["pinta", "pintas"], "qt": ["cuarto", "cuartos"], "gal": ["galón", "galones"]},
  "obj": [["el largo de un lápiz", "in"], ["la altura de una puerta", "ft"], ["la distancia de Chicago a Detroit", "mi"], ["el largo de una cancha de fútbol americano", "yd"], ["el ancho de un teléfono", "in"], ["la distancia que maneja hasta el trabajo", "mi"], ["el largo de un cuarto", "ft"],
          ["el peso de una carta", "oz"], ["el peso de un saco de papas", "lb"], ["el peso de un camión", "T"], ["el peso de una lonja de queso", "oz"], ["el peso de una persona", "lb"], ["el peso de un elefante", "T"],
          ["el jugo de una botellita", "floz"], ["la leche para una receta de panqueques", "c"], ["el agua de una bañera", "gal"], ["la gasolina del tanque de un carro", "gal"], ["la leche de un cartón para el desayuno de la familia", "qt"]],
  "pregUnidad": "¿Qué unidad conviene más para medir <strong>{o}</strong>?",
  "chica": "Esa unidad es demasiado pequeña para esto: necesitaría muchísimas.",
  "grande": "Esa unidad es demasiado grande para esto: la medida sería una partecita de una.",
  "pistaUnidad": "Imagine la cosa y compárela con cada unidad.",
  "bienUnidad": "La mejor unidad para medir {o} es <strong>{u}</strong>.",
  "cuantos": {"in": "Cuántas", "ft": "Cuántos", "yd": "Cuántas", "mi": "Cuántas", "oz": "Cuántas", "lb": "Cuántas", "T": "Cuántas", "floz": "Cuántas", "c": "Cuántas", "pt": "Cuántas", "qt": "Cuántos", "gal": "Cuántos"},
  "art": {"in": "la pulgada", "ft": "el pie", "yd": "la yarda", "mi": "la milla", "oz": "la onza", "lb": "la libra", "T": "la tonelada", "floz": "la onza líquida", "c": "la taza", "pt": "la pinta", "qt": "el cuarto", "gal": "el galón"},
  "pregConv": "¿{c} <strong>{u2}</strong> hay en <strong>{n} {u1}</strong>?",
  "solMult": "Va de una unidad grande a una pequeña, así que multiplique. 1 {g} = {f} {p}, así que {n} × {f} = <strong>{r}</strong> {u2}.",
  "solDiv": "Va de una unidad pequeña a una grande, así que divida. 1 {g} = {f} {p}, así que {n} ÷ {f} = <strong>{r}</strong> {u2}.",
  "trampaMult": "Multiplicó, pero va de una unidad pequeña a una grande: habrá menos unidades. Divida.",
  "trampaDiv": "Dividió, pero va de una unidad grande a una pequeña: habrá más unidades. Multiplique.",
  "trampaSuma": "Sumar la equivalencia no convierte. Multiplique o divida entre {f}.",
  "pistaConv": "Busque la equivalencia. De grande a pequeña: multiplique. De pequeña a grande: divida.",
  "pregDos": "Escriba <strong>{n} {u1}</strong> en {g} y {p}.",
  "dosU": "{q} {g} {r} {p}",
  "bienDos": "{n} ÷ {f} = {q}, residuo {r} ({q} × {f} = {m}). Así que {n} {u1} = {q} {g} {r} {p}.",
  "dosDigitos": "Cuidado: 1 {g1} son {f} {p}, no 10. Divida {n} entre {f}.",
  "dosSinSimplificar": "{r} {p} forman por lo menos 1 {g1} más. El residuo tiene que ser menor que {f}.",
  "dosUnoMas": "Eso es {m2} {p}, más que {n}. Revise el cociente.",
  "pistaDos": "Divida entre la equivalencia: el cociente es la unidad grande, y el residuo es la unidad pequeña.",
  "pregComp": "¿Qué es más: <strong>{a}</strong> o <strong>{b}</strong>?",
  "iguales": "Son iguales.",
  "bienComp": "Ponga las dos en {p}: {a} = {n} × {f} = {v} {p}. {cmp}",
  "mayor": "{v} es más que {b}, así que {a} es más.",
  "menor": "{v} es menos que {b}, así que {b2} es más.",
  "igual": "{v} = {b}, así que son iguales.",
  "pistaComp": "Primero convierta la unidad grande a la pequeña, y después compare los números."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
var GRUPOS = { in: ["in", "ft", "yd", "mi"], ft: ["in", "ft", "yd", "mi"], yd: ["in", "ft", "yd", "mi"], mi: ["in", "ft", "yd", "mi"],
  oz: ["oz", "lb", "T"], lb: ["oz", "lb", "T"], T: ["oz", "lb", "T"], floz: ["floz", "c", "qt", "gal"], c: ["floz", "c", "qt", "gal"], qt: ["floz", "c", "qt", "gal"], gal: ["floz", "c", "qt", "gal"] };
/* [big, small, how many small in one big, largest number of big units to use] */
var EQ = [["ft", "in", 12, 12], ["yd", "ft", 3, 15], ["yd", "in", 36, 6], ["mi", "ft", 5280, 4], ["lb", "oz", 16, 10], ["T", "lb", 2000, 6],
          ["gal", "qt", 4, 15], ["qt", "pt", 2, 15], ["pt", "c", 2, 15], ["gal", "c", 16, 8], ["c", "floz", 8, 10]];
function un(k, n){ return TXT.u[k][n === 1 ? 0 : 1]; }

/* ============ MODULE 1 · choose the unit ============ */
function genUnidad(){
  var o = elige(TXT.obj), g = GRUPOS[o[1]], iok = g.indexOf(o[1]), pistas = {};
  g.forEach(function(k, i){ if (k !== o[1]) pistas[k] = i < iok ? TXT.chica : TXT.grande; });
  var txt = F(TXT.bienUnidad, { o: o[0], u: TXT.art[o[1]] });
  return { enOrden: true, enun: F(TXT.pregUnidad, { o: o[0] }), opciones: g.map(function(k){ return { html: TXT.u[k][1], clave: k }; }),
    correcta: o[1], pistas: pistas, pista: TXT.pistaUnidad, bien: txt, mal: txt };
}

/* ============ MODULE 2 · convert ============ */
function genConv(){
  var e = elige(EQ), big = e[0], small = e[1], f = e[2], k = aleatorio(2, e[3]), p = [];
  var base = { g: TXT.u[big][0], f: com(f), p: TXT.u[small][1] };
  if (Math.random() < 0.5){
    var r = k * f;
    if (k + f !== r) p.push({ v: k + f, msg: F(TXT.trampaSuma, base) });
    return { enun: F(TXT.pregConv, { c: TXT.cuantos[small], u2: TXT.u[small][1], n: com(k), u1: un(big, k) }),
      solucion: F(TXT.solMult, Object.assign({ n: com(k), r: com(r), u2: TXT.u[small][1] }, base)),
      evalua: numN(r, p, TXT.pistaConv) };
  }
  var n = k * f;
  if (n * f !== k) p.push({ v: n * f, msg: TXT.trampaMult });
  if (n + f !== k) p.push({ v: n + f, msg: F(TXT.trampaSuma, base) });
  if (n - f !== k && n - f > 0) p.push({ v: n - f, msg: F(TXT.trampaSuma, base) });
  return { enun: F(TXT.pregConv, { c: TXT.cuantos[big], u2: TXT.u[big][1], n: com(n), u1: un(small, n) }),
    solucion: F(TXT.solDiv, Object.assign({ n: com(n), r: com(k), u2: TXT.u[big][1] }, base)),
    evalua: numN(k, p, TXT.pistaConv) };
}

/* ============ MODULE 3 · two units ============ */
var DOS = [["ft", "in", 12, 2, 9], ["lb", "oz", 16, 2, 9], ["yd", "ft", 3, 3, 15], ["gal", "qt", 4, 2, 12]];
function genDos(){
  var d = elige(DOS), f = d[2], q = aleatorio(d[3], d[4]), r = aleatorio(1, f - 1), n = q * f + r;
  var o = { n: n, u1: TXT.u[d[1]][1], g: TXT.u[d[0]][q === 1 ? 0 : 1], g1: TXT.u[d[0]][0], p: TXT.u[d[1]][r === 1 ? 0 : 1], f: f, q: q, r: r, m: q * f };
  var cor = F(TXT.dosU, o), op = [{ html: cor, clave: "ok" }], pistas = {};
  function mete(q2, r2, msg){
    var h = F(TXT.dosU, { q: q2, g: TXT.u[d[0]][q2 === 1 ? 0 : 1], r: r2, p: TXT.u[d[1]][r2 === 1 ? 0 : 1] });
    if (op.some(function(x){ return x.html === h; }) || q2 < 0 || r2 < 0) return;
    op.push({ html: h, clave: "k" + op.length }); pistas["k" + (op.length - 1)] = msg;
  }
  if (n >= 10 && f !== 10) mete(Math.floor(n / 10), n % 10, F(TXT.dosDigitos, o));
  mete(q - 1, r + f, F(TXT.dosSinSimplificar, { r: r + f, p: TXT.u[d[1]][1], g1: TXT.u[d[0]][0], f: f }));
  mete(q + 1, r, F(TXT.dosUnoMas, { m2: (q + 1) * f + r, p: TXT.u[d[1]][1], n: n }));
  if (op.length < 4) mete(q, (r + 2) % f || 1, TXT.pistaDos);
  var txt = F(TXT.bienDos, o);
  return { enun: F(TXT.pregDos, { n: n, u1: TXT.u[d[1]][1], g: TXT.u[d[0]][1], p: TXT.u[d[1]][1] }), opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaDos, bien: txt, mal: txt };
}

/* ============ MODULE 4 · compare ============ */
function genComp(){
  var e = elige(EQ.filter(function(x){ return x[2] <= 36; })), f = e[2], n = aleatorio(2, Math.min(e[3], 9)), v = n * f;
  var b = Math.random() < 0.25 ? v : v + elige([-3, -2, -1, 1, 2, 3]) * Math.max(1, Math.round(f / 4));
  if (b <= 0) b = v + 1;
  var A = n + " " + un(e[0], n), Bt = b + " " + un(e[1], b);
  var cmp = v > b ? F(TXT.mayor, { v: v, b: b, a: A }) : (v < b ? F(TXT.menor, { v: v, b: b, b2: Bt }) : F(TXT.igual, { v: v, b: b }));
  var txt = F(TXT.bienComp, { p: TXT.u[e[1]][1], a: A, n: n, f: f, v: v, cmp: cmp });
  return { enOrden: true, enun: F(TXT.pregComp, { a: A, b: Bt }), opciones: [{ html: A, clave: "a" }, { html: Bt, clave: "b" }, { html: TXT.iguales, clave: "=" }],
    correcta: v > b ? "a" : (v < b ? "b" : "="), pista: TXT.pistaComp, bien: txt, mal: txt };
}

creaPracticaOM("p1", genUnidad);
creaPracticaLibre("p2", genConv);
creaPracticaOM("p3", genDos);
creaPracticaOM("p4", genComp);
'''

def practica_pagina():
    n = N
    mods = [
     (t("choose-unit", "elegir-unidad"), t("Choose the right unit", "Elegir la unidad correcta"),
      f'''      <p>{t("Picture the thing you want to measure. Small things use small units (inch, ounce, fluid ounce); big things use big units (mile, ton, gallon).", "Imagine lo que quiere medir. Las cosas pequeñas usan unidades pequeñas (pulgada, onza, onza líquida); las grandes usan unidades grandes (milla, tonelada, galón).")}</p>
      <table class="reglas">
        <caption>{t("The units, from small to big", "Las unidades, de pequeña a grande")}</caption>
        <thead><tr><th scope="col">{t("Measure", "Medida")}</th><th scope="col">{t("Units", "Unidades")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Length", "Longitud")}</td><td>{t("inch → foot → yard → mile", "pulgada → pie → yarda → milla")}</td></tr>
          <tr><td>{t("Weight", "Peso")}</td><td>{t("ounce → pound → ton", "onza → libra → tonelada")}</td></tr>
          <tr><td>{t("Capacity", "Capacidad")}</td><td>{t("fluid ounce → cup → pint → quart → gallon", "onza líquida → taza → pinta → cuarto → galón")}</td></tr>
        </tbody>
      </table>
{B.om("p1", t("Practice: which unit?", "Practique: ¿qué unidad?"))}'''),
     (t("convert", "convertir"), t("Convert units", "Convertir unidades"),
      f'''      <table class="reglas">
        <caption>{t("Equivalences", "Equivalencias")}</caption>
        <thead><tr><th scope="col">{t("Length", "Longitud")}</th><th scope="col">{t("Weight", "Peso")}</th><th scope="col">{t("Capacity", "Capacidad")}</th></tr></thead>
        <tbody>
          <tr><td>1 ft = 12 in</td><td>1 lb = 16 oz</td><td>1 c = 8 fl oz</td></tr>
          <tr><td>1 yd = 3 ft = 36 in</td><td>1 T = 2,000 lb</td><td>1 pt = 2 c · 1 qt = 2 pt</td></tr>
          <tr><td>1 mi = 5,280 ft</td><td></td><td>1 gal = 4 qt = 16 c</td></tr>
        </tbody>
      </table>
      <div class="caja-atencion"><strong>{t("Big to small: multiply. Small to big: divide.", "De grande a pequeña: multiplique. De pequeña a grande: divida.")}</strong> {t("Going to a smaller unit, you need more of them.", "Al ir a una unidad más pequeña, se necesitan más.")}</div>
{B.libre("p2", t("Practice: convert", "Practique: convertir"), t("Answer", "Respuesta"))}'''),
     (t("two-units", "dos-unidades"), t("Measures with two units", "Medidas con dos unidades"),
      f'''      <p>{t("Divide by the equivalence. The <strong>quotient</strong> is the big unit, and the <strong>remainder</strong> is the small unit: 75 in ÷ 12 = 6, remainder 3, so 75 in = 6 ft 3 in.", "Divida entre la equivalencia. El <strong>cociente</strong> es la unidad grande, y el <strong>residuo</strong> es la unidad pequeña: 75 pulgadas ÷ 12 = 6, residuo 3, así que 75 pulgadas = 6 pies 3 pulgadas.")}</p>
{B.om("p3", t("Practice: write it with two units", "Practique: escribirlo con dos unidades"))}'''),
     (t("compare", "comparar"), t("Compare measures", "Comparar medidas"),
      f'''      <p>{t("To compare 2 pounds and 30 ounces, first put both in the <strong>same unit</strong>: 2 lb = 32 oz. Now compare 32 and 30.", "Para comparar 2 libras y 30 onzas, primero ponga las dos en la <strong>misma unidad</strong>: 2 libras = 32 onzas. Ahora compare 32 y 30.")}</p>
{B.om("p4", t("Practice: which is more?", "Practique: ¿qué es más?"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"), t("U.S. customary units: length, weight, and capacity", "Sistema inglés: longitud, peso y capacidad"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Sistema inglés: longitud, peso y capacidad")
