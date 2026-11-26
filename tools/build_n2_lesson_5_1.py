"""Level 2 · Lesson 5.1 · Percent: conversions and the three basic cases — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg
from n2 import fr

B.NIVEL = 2
N = "5-1"
TEMA = ("Percents", "Porcentajes")
TIT = ("Percent: conversions and the three basic cases", "El porcentaje: conversiones y los tres casos fundamentales")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def rejilla(k):
    c = 22
    s = "".join(f'<rect x="{2 + (i % 10) * c}" y="{2 + (i // 10) * c}" width="{c}" height="{c}" fill="{"#b33c00" if i < k else "#fff"}" stroke="#90a4ae" stroke-width="1"/>' for i in range(100))
    s += f'<rect x="2" y="2" width="{10 * c}" height="{10 * c}" fill="none" stroke="#263238" stroke-width="2"/>'
    return svg(f"0 0 {10 * c + 4} {10 * c + 4}", t(f"A grid of 100 squares with {k} squares shaded.", f"Una cuadrícula de 100 cuadritos con {k} coloreados."), s, 240)

def triangulo():
    d = ('<polygon points="150,10 290,205 10,205" fill="#fff3e0" stroke="#7a2800" stroke-width="3"/>'
         '<line x1="73" y1="118" x2="227" y2="118" stroke="#7a2800" stroke-width="3"/>'
         f'<text x="150" y="92" font-size="24" font-weight="700" text-anchor="middle" fill="#7a2800">{t("Part", "Parte")}</text>'
         '<text x="100" y="172" font-size="22" font-weight="700" text-anchor="middle" fill="#7a2800">%</text>'
         f'<text x="200" y="172" font-size="22" font-weight="700" text-anchor="middle" fill="#7a2800">{t("Whole", "Todo")}</text>'
         '<text x="150" y="176" font-size="20" text-anchor="middle" fill="#7a2800">×</text>')
    return svg("0 0 300 220", t("The percent triangle: Part on top; on the bottom, separated by a times sign, the percent and the Whole.", "El triángulo del porcentaje: arriba la Parte; abajo, separados por un signo de multiplicar, el porcentaje y el Todo."), d, 300)

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Topic 5. In Topic 4 you learned to compare quantities with ratios and to predict them with proportions. This topic is about one very special kind of ratio: the one whose second term is always 100. These ratios are called <strong>percents</strong>, and they show up in grades, discounts, taxes, statistics, and interest.",
"Bienvenido al Tema 5. En el Tema 4 aprendió a comparar cantidades con razones y a predecirlas con proporciones. Este tema se dedica a un caso muy especial: las razones cuyo segundo término es siempre 100. Se llaman <strong>porcentajes</strong> y aparecen en calificaciones, descuentos, impuestos, estadísticas e intereses.")}</p>
{caja("tip", t("Something to think about", "Para pensar desde ya"), t("<p>On a test with 25 questions, you got 18 right. What percent is that? You will solve it in section 4, in two different ways.</p>", "<p>En un examen de 25 preguntas contestó bien 18. ¿Qué porcentaje es? Lo resolverá en la sección 4, con dos métodos distintos.</p>"))}
<p>{t("The word <strong>percent</strong> comes from the Latin <em>per centum</em>, “for every hundred.” A percent is a ratio whose second term is always 100.", "La palabra <strong>porcentaje</strong> viene del latín <em>per centum</em>, «por cada cien». Un porcentaje es una razón cuyo segundo término es siempre 100.")}</p>
<p style="text-align:center;font-size:1.5rem;font-weight:700;color:#0d47a1">25% = {fr(25, 100)} = 0.25</p>
<div style="text-align:center">{rejilla(25)}</div>
<p>{t("The three forms show the same thing: 25 parts out of every 100. Only the notation changes.", "Las tres formas representan lo mismo: 25 partes de cada 100. Solo cambia la notación.")}</p>
{practica("p1", t("Practice 1 — The grid", "Práctica 1 — La cuadrícula"), t("In a grid of 100 squares, 40 are shaded. Which one is NOT the same amount?", "En una cuadrícula de 100 cuadritos hay 40 coloreados. ¿Cuál NO representa lo mismo?"),
          [("a", "40%"), ("b", "0.40"), ("c", fr(40, 100)), ("d", "4%")])}
{enlace(n, t("per-100", "razon-100"), t("percent as a ratio out of 100", "el porcentaje como razón de 100"), t("Shade the grid of 100 and say what percent it shows.", "Coloree la cuadrícula de 100 y diga qué porcentaje representa."))}'''

    s2 = f'''<p>{t("Any percent can be written as a decimal or as a fraction, and the other way around.", "Cualquier porcentaje se puede expresar como decimal o como fracción, y al revés.")}</p>
{tabla(t("How to convert", "Cómo convertir"), t("Rules for converting among the three forms", "Reglas de conversión entre las tres formas"),
       [t("Conversion", "Conversión"), t("How", "Procedimiento"), t("Example", "Ejemplo")],
       [[t("Percent → decimal", "Porcentaje → decimal"), t("Divide by 100: move the decimal point two places to the left.", "Dividir entre 100: el punto decimal se mueve dos lugares a la izquierda."), "45% = 0.45"],
        [t("Decimal → percent", "Decimal → porcentaje"), t("Multiply by 100: move the decimal point two places to the right.", "Multiplicar por 100: el punto decimal se mueve dos lugares a la derecha."), "0.07 = 7%"],
        [t("Percent → fraction", "Porcentaje → fracción"), t("Write it over 100 and simplify.", "Escribir sobre 100 y simplificar."), "40% = 40/100 = 2/5"],
        [t("Fraction → percent", "Fracción → porcentaje"), t("Divide the top by the bottom and multiply by 100.", "Dividir el numerador entre el denominador y multiplicar por 100."), "3/4 = 0.75 = 75%"]])}
{tabla(t("Equivalents to know by heart", "Equivalencias para reconocer al vuelo"), t("Common percents with their fractions and decimals", "Porcentajes comunes con su fracción y su decimal"),
       [t("Percent", "Porcentaje"), t("Fraction", "Fracción"), "Decimal"],
       [["1%", "1/100", "0.01"], ["10%", "1/10", "0.1"], ["12.5%", "1/8", "0.125"], ["20%", "1/5", "0.2"], ["25%", "1/4", "0.25"],
        ["33⅓%", "1/3", t("0.333… (about 0.33)", "0.333… (≈ 0.33)")], ["50%", "1/2", "0.5"], ["66⅔%", "2/3", t("0.666… (about 0.67)", "0.666… (≈ 0.67)")], ["75%", "3/4", "0.75"], ["100%", "1", "1.0"]])}
{caja("tip", t("More than 100% and less than 1%", "Más de 100% y menos de 1%"), t("<p>The rules do not change. 150% = 1.5 (one and a half times the whole), and 0.5% = 0.005 (half of one part out of every hundred). A percent greater than 100% means an amount greater than the whole.</p>", "<p>Las reglas no cambian. 150% = 1.5 (una vez y media el total) y 0.5% = 0.005 (medio punto de cada cien). Un porcentaje mayor que 100% indica una cantidad mayor que el total de referencia.</p>"))}
{caja("ojo", t("Common mistake", "Error frecuente"), t("<p>Mixing up 0.5 and 5%. They are different: 0.5 = 50%, but 5% = 0.05. The two-places rule for the decimal point prevents this mistake.</p>", "<p>Confundir 0.5 con 5%. Son distintos: 0.5 = 50%, mientras que 5% = 0.05. La regla de los dos lugares del punto decimal evita este error.</p>"))}
{calc(t("Percents on the calculator", "Porcentajes en la calculadora"), t(f"<p>To change 3/8 to a percent, type {T('3')} {T('÷')} {T('8')} {T('×')} {T('100')} {T('enter')}. The screen shows 37.5, so 3/8 = 37.5%.</p>", f"<p>Para pasar 3/8 a porcentaje, escriba {T('3')} {T('÷')} {T('8')} {T('×')} {T('100')} {T('enter')}. La pantalla muestra 37.5, así que 3/8 = 37.5%.</p>"))}
{practica("p2", t("Practice 2 — Percent to decimal", "Práctica 2 — De porcentaje a decimal"), t("60% as a decimal is:", "60% como decimal es:"), [("a", "6.0"), ("b", "0.6"), ("c", "0.06"), ("d", "60")])}
{practica("p3", t("Practice 3 — Decimal to percent", "Práctica 3 — De decimal a porcentaje"), t("0.08 as a percent is:", "0.08 como porcentaje es:"), [("a", "0.8%"), ("b", "80%"), ("c", "8%"), ("d", "0.08%")])}
{practica("p4", t("Practice 4 — Fraction to percent", "Práctica 4 — De fracción a porcentaje"), t(f"{fr(3, 8)} as a percent is:", f"{fr(3, 8)} como porcentaje es:"), [("a", "38%"), ("b", "3.8%"), ("c", "26.7%"), ("d", "37.5%")])}
{enlace(n, t("conversions", "conversiones"), t("fractions, decimals, and percents", "fracción, decimal y porcentaje"), t("Use the converter and practice moving among the three forms.", "Use el conversor y practique el paso entre las tres formas."))}'''

    s3 = f'''<p>{t("Every percent problem connects three things: the <strong>part</strong>, the <strong>whole</strong> (the total you compare to), and the <strong>percent</strong>. One formula joins them:", "Todo problema de porcentaje relaciona tres elementos: la <strong>parte</strong>, el <strong>todo</strong> (el total de referencia) y el <strong>porcentaje</strong>. Una sola fórmula los une:")}</p>
<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{t("Part = Percent × Whole", "Parte = Porcentaje × Todo")}</p>
<p>{t("Inside the formula, the percent is always written as a decimal (15% → 0.15). The triangle helps you remember which operation to use: cover the piece you are missing and read what is left. Pieces side by side are multiplied; one above the other, divided.", "Dentro de la fórmula, el porcentaje se usa siempre en forma decimal (15% → 0.15). El triángulo ayuda a recordar qué operación usar: se tapa el elemento que falta y se lee lo que queda. Lo que está lado a lado se multiplica; lo que está arriba y abajo se divide.")}</p>
<div style="text-align:center">{triangulo()}</div>
{tabla(t("What the triangle says", "Lo que dice el triángulo"), t("The operation for each missing piece", "La operación según el elemento que falta"),
       [t("Missing", "Me falta"), t("Cover it and you get", "Al taparlo queda"), t("Operation", "Operación")],
       [[t("the part", "la parte"), "% × " + t("Whole", "Todo"), t("multiply", "multiplicar")],
        [t("the percent", "el porcentaje"), t("Part ÷ Whole", "Parte ÷ Todo"), t("divide, then × 100", "dividir y × 100")],
        [t("the whole", "el todo"), t("Part ÷ %", "Parte ÷ %"), t("divide", "dividir")]])}
{enlace(n, t("triangle", "triangulo"), t("the percent triangle", "el triángulo del porcentaje"), t("Cover what you are missing and see which operation solves each problem.", "Tape lo que falta y descubra qué operación resuelve cada problema."))}'''

    s4 = f'''<p>{t("Depending on which of the three pieces is missing, there are <strong>three cases</strong>. The key question before you calculate is always: <strong>what am I missing?</strong>", "Según cuál de los tres elementos falte, hay <strong>tres casos</strong>. La pregunta clave antes de calcular es siempre: <strong>¿qué me falta?</strong>")}</p>
{ej(t("Case 1 · Find the part", "Caso 1 · Hallar la parte"), t("What is 15% of $80?", "¿Cuánto es el 15% de $80?"),
  [("1", t("What is missing?", "¿Qué falta?"), t("The part. You know the percent (15% = 0.15) and the whole ($80).", "La parte. Se conocen el porcentaje (15% = 0.15) y el todo ($80).")),
   ("2", t("Multiply.", "Multiplique."), t("Part = 0.15 × 80 = 12.", "Parte = 0.15 × 80 = 12.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>$12</strong>")])}
{ej(t("Case 2 · Find the whole", "Caso 2 · Hallar el todo"), t("30% of a number is 45. What is the number?", "El 30% de un número es 45. ¿Cuál es ese número?"),
  [("1", t("What is missing?", "¿Qué falta?"), t("The whole. You know the part (45) and the percent (30% = 0.30).", "El todo. Se conocen la parte (45) y el porcentaje (30% = 0.30).")),
   ("2", t("Divide.", "Divida."), t("Whole = Part ÷ % = 45 ÷ 0.30 = 150.", "Todo = Parte ÷ % = 45 ÷ 0.30 = 150.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>150</strong>. Check: 0.30 × 150 = 45. ✓", "<strong>150</strong>. Verificación: 0.30 × 150 = 45. ✓"))])}
{ej(t("Case 3 · Find the percent: the test from the start", "Caso 3 · Hallar el porcentaje: el examen del principio"), t("You got 18 of 25 questions right. What percent is that?", "Se contestaron bien 18 de 25 preguntas. ¿Qué porcentaje es?"),
  [("1", t("What is missing?", "¿Qué falta?"), t("The percent. Part = 18, whole = 25.", "El porcentaje. Parte = 18, todo = 25.")),
   ("2", t("Divide.", "Divida."), "18 ÷ 25 = 0.72."),
   ("3", t("Change to a percent.", "Pase a porcentaje."), "0.72 × 100 = 72."),
   ("✓", t("Answer.", "Respuesta."), "<strong>72%</strong>")])}
{caja("ojo", t("Which number is the whole?", "¿Cuál es el todo?"), t("<p>It is the reference amount, the one that comes after the word <strong>of</strong>: “15% <strong>of</strong> $80,” “18 <strong>of</strong> 25.” Mixing up the part and the whole is the most common mistake in case 3.</p>", "<p>Es la cantidad de referencia, la que aparece después de la palabra <strong>de</strong>: «el 15% <strong>de</strong> $80», «18 <strong>de</strong> 25». Confundir la parte con el todo es el error más común en el caso 3.</p>"))}
{practica("p5", t("Practice 5 — What am I missing?", "Práctica 5 — ¿Qué me falta?"), t("In a store, 40 of 160 customers paid in cash. What percent paid in cash?", "En una tienda, 40 de los 160 clientes pagaron en efectivo. ¿Qué porcentaje pagó en efectivo?"),
          [("a", t("The part is missing", "Falta la parte")), ("b", t("The percent is missing", "Falta el porcentaje")), ("c", t("The whole is missing", "Falta el todo"))])}
{practica("p6", t("Practice 6 — What am I missing?", "Práctica 6 — ¿Qué me falta?"), t("Today 27 students came, and that is 90% of the class. How many students are in the class?", "Hoy vinieron 27 estudiantes, que son el 90% del grupo. ¿Cuántos estudiantes tiene el grupo?"),
          [("a", t("The part is missing", "Falta la parte")), ("b", t("The percent is missing", "Falta el porcentaje")), ("c", t("The whole is missing", "Falta el todo"))])}
{practica("p7", t("Practice 7 — Find the part", "Práctica 7 — Halle la parte"), t("What is 25% of 240?", "¿Cuánto es el 25% de 240?"), [("a", "96"), ("b", "60"), ("c", "6,000"), ("d", "9.6")])}
{practica("p8", t("Practice 8 — Find the percent", "Práctica 8 — Halle el porcentaje"), t("What percent is 18 of 60?", "¿Qué porcentaje es 18 de 60?"), [("a", "18%"), ("b", "0.3%"), ("c", "333%"), ("d", "30%")])}
{enlace(n, t("three-cases", "tres-tipos"), t("the three kinds of problems", "los tres tipos de problemas"), t("Decide what you are looking for (part, whole, or percent) and solve it with the bar model.", "Identifique qué se busca —la parte, el total o el porcentaje— y resuelva con el modelo de barra."))}'''

    s5 = f'''<p>{t("Because a percent is a ratio out of 100, you can set up any percent problem as the direct proportion you studied in Lesson 4.2:", "Como un porcentaje es una razón de 100, cualquier problema se puede plantear como la proporción directa estudiada en la Lección 4.2:")}</p>
<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{fr(t("part", "parte"), t("whole", "todo"))} = {fr("%", 100)}</p>
<p>{t("Put in the three values you know, put x where the missing one goes, and solve with cross products.", "Se colocan los tres datos conocidos, la x en el lugar del que falta, y se resuelve con el producto cruzado.")}</p>
{ejemplo(t("Example: the three cases with a proportion", "Ejemplo: los tres casos con la proporción"),
  [("1", t("Part.", "Parte."), t(f"15% of 80 → {fr('x', 80)} = {fr(15, 100)} → 100x = 1,200 → x = 12.", f"15% de 80 → {fr('x', 80)} = {fr(15, 100)} → 100x = 1,200 → x = 12.")),
   ("2", t("Whole.", "Todo."), t(f"45 is 30% → {fr(45, 'x')} = {fr(30, 100)} → 30x = 4,500 → x = 150.", f"45 es el 30% → {fr(45, 'x')} = {fr(30, 100)} → 30x = 4,500 → x = 150.")),
   ("3", t("Percent.", "Porcentaje."), t(f"18 of 25 → {fr(18, 25)} = {fr('x', 100)} → 25x = 1,800 → x = 72%.", f"18 de 25 → {fr(18, 25)} = {fr('x', 100)} → 25x = 1,800 → x = 72%."))])}
{caja("tip", t("Which method is better?", "¿Qué método conviene?"), t("<p>Both give the same answer. The formula is faster with a calculator; the proportion helps when you do not know which operation to use, because you only have to place the data correctly. Learn both, and use one to check the other.</p>", "<p>Los dos dan el mismo resultado. La fórmula es más rápida con calculadora; la proporción ayuda cuando no se sabe qué operación hacer, porque solo pide colocar bien los datos. Conviene dominar ambos y usar uno para comprobar el otro.</p>"))}
{enlace(n, t("percent-proportion", "proporcion-porcentual"), t("the percent proportion", "la proporción porcentual"), t("Set up part/whole = %/100, place the x, and solve with cross products.", "Plantee parte/todo = %/100, coloque la x y resuelva con el producto cruzado."))}'''

    secciones = [("s-" + t("per-100", "razon-100"), t("A percent is a ratio out of 100", "El porcentaje como razón de 100"), s1),
                 ("s-" + t("conversions", "conversiones"), t("Converting among percents, decimals, and fractions", "Conversiones entre porcentaje, decimal y fracción"), s2),
                 ("s-" + t("triangle", "triangulo"), t("One formula: the percent triangle", "Una sola fórmula: el triángulo del porcentaje"), s3),
                 ("s-" + t("three-cases", "tres-casos"), t("The three basic cases", "Los tres casos fundamentales"), s4),
                 ("s-" + t("percent-proportion", "proporcion-porcentual"), t("Another method: the percent proportion", "Método alternativo: la proporción porcentual"), s5)]

    lesson = {"next": t("Lesson 5.2", "Lección 5.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "d", "hints": {"a": t("40% means 40 out of 100: it is the same.", "40% quiere decir 40 de 100: es lo mismo."), "b": t("0.40 is 40 hundredths: it is the same.", "0.40 son 40 centésimos: es lo mismo."), "c": t("40/100 is exactly 40 out of 100: it is the same.", "40/100 es exactamente 40 de 100: es lo mismo.")},
             "right": t("4% would be only 4 squares.", "4% serían solo 4 cuadritos."), "solution": t("40 out of 100 is 40% = 40/100 = 0.40. 4% is only 4 out of 100.", "40 de 100 es 40% = 40/100 = 0.40. 4% es solo 4 de 100.")},
      "p2": {"ok": "b", "hints": {"a": t("6.0 is 600%. Move the point two places to the left.", "6.0 es 600%. Mueva el punto dos lugares a la izquierda."), "c": t("0.06 is 6%. Check: 60 ÷ 100.", "0.06 es 6%. Revise: 60 ÷ 100."), "d": t("Divide by 100.", "Divida entre 100.")},
             "right": t("60 ÷ 100 = 0.6.", "60 ÷ 100 = 0.6."), "solution": t("Divide by 100: 60% = 0.60 = 0.6.", "Se divide entre 100: 60% = 0.60 = 0.6.")},
      "p3": {"ok": "c", "hints": {"a": t("You moved the point only one place.", "Movió el punto un solo lugar."), "b": t("80% is 0.80. Check the zero after the point.", "80% es 0.80. Revise el cero después del punto."), "d": t("Multiply by 100.", "Multiplique por 100.")},
             "right": t("0.08 × 100 = 8%.", "0.08 × 100 = 8%."), "solution": t("Multiply by 100: the point moves two places to the right. 0.08 = 8%.", "Se multiplica por 100: el punto se mueve dos lugares a la derecha. 0.08 = 8%.")},
      "p4": {"ok": "d", "hints": {"a": t("You put the 3 and the 8 together. Divide 3 by 8.", "Juntó el 3 y el 8. Divida 3 entre 8."), "b": t("3 ÷ 8 = 0.375. Multiply by 100.", "3 ÷ 8 = 0.375. Multiplique por 100."), "c": t("You divided 8 by 3. It is 3 ÷ 8.", "Dividió 8 entre 3. Es 3 ÷ 8.")},
             "right": t("3 ÷ 8 = 0.375 = 37.5%.", "3 ÷ 8 = 0.375 = 37.5%."), "solution": t("3 ÷ 8 = 0.375, and 0.375 × 100 = 37.5%.", "3 ÷ 8 = 0.375, y 0.375 × 100 = 37.5%.")},
      "p5": {"ok": "b", "hints": {"a": t("You know the part: 40 customers.", "Conoce la parte: 40 clientes."), "c": t("You know the whole: 160 customers.", "Conoce el todo: 160 clientes.")},
             "right": t("You know the part (40) and the whole (160).", "Conoce la parte (40) y el todo (160)."), "solution": t("Part = 40, whole = 160: the percent is missing. 40 ÷ 160 = 0.25 = 25%.", "Parte = 40, todo = 160: falta el porcentaje. 40 ÷ 160 = 0.25 = 25%.")},
      "p6": {"ok": "c", "hints": {"a": t("You know the part: 27 students came.", "Conoce la parte: vinieron 27."), "b": t("You know the percent: 90%.", "Conoce el porcentaje: 90%.")},
             "right": t("You know the part (27) and the percent (90%).", "Conoce la parte (27) y el porcentaje (90%)."), "solution": t("Part = 27, percent = 90%: the whole is missing. 27 ÷ 0.90 = 30 students.", "Parte = 27, porcentaje = 90%: falta el todo. 27 ÷ 0.90 = 30 estudiantes.")},
      "p7": {"ok": "b", "hints": {"a": t("You divided by 2.5. 25% = 0.25.", "Dividió entre 2.5. 25% = 0.25."), "c": t("Change 25% to a decimal first: 0.25.", "Primero pase 25% a decimal: 0.25."), "d": t("Check the decimal point: 0.25 × 240.", "Revise el punto decimal: 0.25 × 240.")},
             "right": t("0.25 × 240 = 60.", "0.25 × 240 = 60."), "solution": t("Part = 0.25 × 240 = 60. (25% is one fourth: 240 ÷ 4 = 60.)", "Parte = 0.25 × 240 = 60. (25% es la cuarta parte: 240 ÷ 4 = 60.)")},
      "p8": {"ok": "d", "hints": {"a": t("18 is the part, not the percent. Divide 18 by 60.", "18 es la parte, no el porcentaje. Divida 18 entre 60."), "b": t("18 ÷ 60 = 0.3. Multiply by 100.", "18 ÷ 60 = 0.3. Multiplique por 100."), "c": t("You divided 60 by 18. The whole goes on the bottom.", "Dividió 60 entre 18. El todo va abajo.")},
             "right": t("18 ÷ 60 = 0.3 = 30%.", "18 ÷ 60 = 0.3 = 30%."), "solution": t("% = Part ÷ Whole = 18 ÷ 60 = 0.3, and 0.3 × 100 = 30%.", "% = Parte ÷ Todo = 18 ÷ 60 = 0.3, y 0.3 × 100 = 30%.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("That is 3.5%.", "Eso es 3.5%."), "b": t("That is 350%.", "Eso es 350%."), "d": t("Divide 35 by 100.", "Divida 35 entre 100.")}, "solution": t("35% = 35 ÷ 100 = 0.35.", "35% = 35 ÷ 100 = 0.35.")},
      "B": {"ok": "a", "hints": {"b": t("0.5 is 50%, not 5%.", "0.5 es 50%, no 5%."), "c": t("Multiply by 100: two places to the right.", "Multiplique por 100: dos lugares a la derecha."), "d": t("Check: 0.5 × 100.", "Revise: 0.5 × 100.")}, "solution": t("0.5 × 100 = 50%.", "0.5 × 100 = 50%.")},
      "C": {"ok": "d", "hints": {"a": t("40/100 is right but not simplified.", "40/100 está bien, pero falta simplificar."), "b": t("4/10 can still be simplified.", "4/10 todavía se puede simplificar."), "c": t("Check: 40 ÷ 20 = 2 and 100 ÷ 20 = 5.", "Revise: 40 ÷ 20 = 2 y 100 ÷ 20 = 5.")}, "solution": t("40% = 40/100 = 2/5.", "40% = 40/100 = 2/5.")},
      "E": {"ok": "a", "hints": {"b": t("You divided. Part = 0.20 × 75.", "Dividió. Parte = 0.20 × 75."), "c": t("Change 20% to 0.20 first.", "Primero pase 20% a 0.20."), "d": t("Check: 75 × 0.2.", "Revise: 75 × 0.2.")}, "solution": t("0.20 × 75 = 15.", "0.20 × 75 = 15.")},
      "F": {"ok": "c", "hints": {"a": t("You multiplied. The whole is Part ÷ %.", "Multiplicó. El todo es Parte ÷ %."), "b": t("You added. Divide 12 by 0.40.", "Sumó. Divida 12 entre 0.40."), "d": t("Check: 12 ÷ 0.4.", "Revise: 12 ÷ 0.4.")}, "solution": t("Whole = 12 ÷ 0.40 = 30.", "Todo = 12 ÷ 0.40 = 30.")},
      "G": {"ok": "d", "hints": {"a": t("9 is the part. Divide 9 by 36.", "9 es la parte. Divida 9 entre 36."), "b": t("9 ÷ 36 = 0.25. Multiply by 100.", "9 ÷ 36 = 0.25. Multiplique por 100."), "c": t("You divided 36 by 9. The whole goes on the bottom.", "Dividió 36 entre 9. El todo va abajo.")}, "solution": t("9 ÷ 36 = 0.25 = 25%.", "9 ÷ 36 = 0.25 = 25%.")},
      "H": {"ok": "b", "hints": {"a": t("That is the part over the percent. Part over whole.", "Eso es parte sobre porcentaje. Va parte sobre todo."), "c": t("The whole goes on the bottom, with the part on top.", "El todo va abajo y la parte arriba."), "d": t("The 100 goes under the percent.", "El 100 va debajo del porcentaje.")}, "solution": t("part/whole = %/100: 12/x = 40/100.", "parte/todo = %/100: 12/x = 40/100.")}
     }}
    lesson["quiz"]["D"] = {"ok": "a", "hints": {"b": t("15 is 1,500%.", "15 es 1,500%."), "c": t("0.15 is 15%.", "0.15 es 15%."), "d": t("0.015 is 1.5%.", "0.015 es 1.5%.")}, "solution": t("150% = 150 ÷ 100 = 1.5.", "150% = 150 ÷ 100 = 1.5.")}

    quiz = [
     ("A", t("35% as a decimal is:", "35% como decimal es:"), [("a", "0.035"), ("b", "3.5"), ("c", "0.35"), ("d", "35")]),
     ("B", t("0.5 as a percent is:", "0.5 como porcentaje es:"), [("a", "50%"), ("b", "5%"), ("c", "0.5%"), ("d", "500%")]),
     ("C", t("40% as a simplified fraction is:", "40% como fracción simplificada es:"), [("a", fr(40, 100)), ("b", fr(4, 10)), ("c", fr(1, 4)), ("d", fr(2, 5))]),
     ("D", t("150% as a decimal is:", "150% como decimal es:"), [("a", "1.5"), ("b", "15"), ("c", "0.15"), ("d", "0.015")]),
     ("E", t("What is 20% of 75?", "¿Cuánto es el 20% de 75?"), [("a", "15"), ("b", "375"), ("c", "1,500"), ("d", "1.5")]),
     ("F", t("40% of a number is 12. What is the number?", "El 40% de un número es 12. ¿Cuál es el número?"), [("a", "4.8"), ("b", "52"), ("c", "30"), ("d", "3")]),
     ("G", t("What percent is 9 of 36?", "¿Qué porcentaje es 9 de 36?"), [("a", "9%"), ("b", "0.25%"), ("c", "400%"), ("d", "25%")]),
     ("H", t("Which proportion solves “40% of a number is 12”?", "¿Qué proporción resuelve «el 40% de un número es 12»?"),
      [("a", f"{fr(12, 40)} = {fr('x', 100)}"), ("b", f"{fr(12, 'x')} = {fr(40, 100)}"), ("c", f"{fr('x', 12)} = {fr(40, 100)}"), ("d", f"{fr(12, 'x')} = {fr(100, 40)}")])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Ratios out of 100: converting among percents, decimals, and fractions, and solving the three basic cases with one formula or with a proportion.", "Las razones por cada 100: convertir entre porcentaje, decimal y fracción, y resolver los tres casos fundamentales con una fórmula o con una proporción."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Understand</strong> a percent as a ratio out of 100.", "<strong>Comprender</strong> el porcentaje como una razón de 100."),
         t("<strong>Convert</strong> among percents, decimals, and fractions, including percents over 100% and under 1%.", "<strong>Convertir</strong> entre porcentaje, decimal y fracción, incluidos porcentajes mayores que 100% y menores que 1%."),
         t("<strong>Identify</strong> what is missing: the part, the whole, or the percent.", "<strong>Identificar</strong> qué falta: la parte, el todo o el porcentaje."),
         t("<strong>Solve</strong> the three cases with the formula Part = Percent × Whole.", "<strong>Resolver</strong> los tres casos con la fórmula Parte = Porcentaje × Todo."),
         t("<strong>Check</strong> with the percent proportion part/whole = %/100.", "<strong>Comprobar</strong> con la proporción porcentual parte/todo = %/100.")],
        secciones,
        (t("Do four conversions among percents, decimals, and fractions, including one percent greater than 100% and one less than 1%. Solve eight problems of the three cases: before you calculate, write what is missing; solve with the formula and check with the percent proportion.",
           "Haga cuatro conversiones entre porcentaje, decimal y fracción, incluido un porcentaje mayor que 100% y uno menor que 1%. Resuelva ocho problemas de los tres casos: antes de calcular, escriba qué le falta; resuelva con la fórmula y compruebe con la proporción porcentual."),
         t("Use your own data: find what percent three real results are, like the questions you got right in the practice pages of this site, or how much of your paycheck goes to rent.",
           "Use sus propios datos: calcule qué porcentaje representan tres resultados reales, como las respuestas que acertó en las páginas de práctica de este sitio o cuánto de su sueldo se va en la renta.")),
        quiz,
        t("Self-check checklist for percents and the three cases", "Lista de autoevaluación del porcentaje y los tres casos"),
        t("Self-check checklist: skills for percent conversions and the three basic cases", "Lista de autoevaluación: destrezas de conversiones y los tres casos fundamentales"),
        [(t("Convert among forms", "Convertir entre formas"), t("I convert both ways with no help, even over 100% and under 1%.", "Convierto en las dos direcciones sin ayuda, incluso más de 100% y menos de 1%."), t("I convert with help.", "Convierto con apoyo."), t("I mix up decimals and percents (0.5 and 5%).", "Confundo decimales con porcentajes (0.5 con 5%).")),
         (t("Identify the case", "Identificar el caso"), t("I find what is missing and spot the whole by the word “of.”", "Identifico qué falta y encuentro el todo por la palabra «de»."), t("I find the case with help.", "Identifico el caso con apoyo."), t("I do not know what is missing.", "No identifico qué valor falta.")),
         (t("Solve", "Resolver"), t("I solve with one method and check with the other.", "Resuelvo con un método y compruebo con el otro."), t("I solve with one method, with some mistakes.", "Resuelvo con un método y con errores."), t("I do not reach the answer.", "No llego al resultado."))],
        t("<p>In this lesson you used the proportions of Topic 4 for ratios <strong>out of 100</strong>. You can now convert among percents, decimals, and fractions, and solve the <strong>three basic cases</strong> with one formula or with the percent proportion.</p>\n<p>In <strong>Lesson 5.2 · Percent change: increase and decrease</strong> you will use percents to measure how much a quantity changes: how much a price went up, how much a temperature went down, or how much a salary grew, always compared to the original value.</p>",
          "<p>En esta lección aplicó las proporciones del Tema 4 a las razones <strong>por cada 100</strong>. Ya convierte entre porcentaje, decimal y fracción, y resuelve los <strong>tres casos fundamentales</strong> con una sola fórmula o con la proporción porcentual.</p>\n<p>En la <strong>Lección 5.2 · Cambio porcentual: aumento y disminución</strong> usará el porcentaje para medir cuánto cambia una cantidad: cuánto subió un precio, cuánto bajó una temperatura o cuánto creció un salario, siempre en relación con el valor original.</p>"),
        ("5-2", ("", t("Lesson 5.2 · Percent change: increase and decrease", "Lección 5.2 · Cambio porcentual: aumento y disminución"))),
        [(t("percent", "porcentaje"), t("A ratio out of 100. 25% = 25/100 = 0.25.", "Razón de 100. 25% = 25/100 = 0.25.")),
         (t("part", "parte"), t("The piece of the whole you are talking about.", "La porción del todo de la que se habla.")),
         (t("whole", "todo"), t("The reference amount, usually after the word “of.”", "La cantidad de referencia, casi siempre después de la palabra «de».")),
         (t("percent proportion", "proporción porcentual"), t("part/whole = %/100.", "parte/todo = %/100."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "vozGrid": "A grid of 100 squares with {k} shaded.", "cuadritos": "{k} of 100 squares shaded.", "cuadrito1": "1 of 100 squares shaded.",
  "queGrid": "What percent of the grid is shaded?", "sinColor": "That is the percent that is not shaded.", "bienGrid": "{k} of 100 squares: {k}%.",
  "escribe": "Type a percent (45%), a decimal (0.45), or a fraction (9/20).", "pct": "Percent", "dec": "Decimal", "frac": "Fraction", "aprox": " (rounded)",
  "comoDec": "{p} as a decimal is:", "expDec": "{p} ÷ 100 = {d}: the decimal point moves two places to the left.",
  "comoPct": "{d} as a percent is:", "expPct": "{d} × 100 = {p}: the decimal point moves two places to the right.",
  "comoFr": "{p} as a simplified fraction is:", "expFr": "{p} = {p0}/100 = {f}.",
  "frPct": "{f} as a percent is:", "expFrPct": "{a} ÷ {b} = {d}, and × 100 = {p}.",
  "tapaElige": "Choose what you are missing, and the triangle covers it.",
  "tapa": {"parte": ["<strong>Part = % × Whole</strong>: the % and the Whole are side by side, so you multiply.", "Example: 15% of $80 → 0.15 × 80 = <strong>$12</strong>."],
           "pct": ["<strong>% = Part ÷ Whole</strong> (then × 100): the Part is above the Whole, so you divide.", "Example: 18 of 25 → 18 ÷ 25 = 0.72 → <strong>72%</strong>."],
           "todo": ["<strong>Whole = Part ÷ %</strong>: the Part is above the %, so you divide.", "Example: 30% of a number is 45 → 45 ÷ 0.30 = <strong>150</strong>."]},
  "op0": "What is {p}% of {t}? Which operation solves it?", "op0a": "You know the whole: the part comes from multiplying, not dividing.", "opDec": "The percent goes in as a decimal: {p}% = {d}.", "op0s": "The part is missing: cover the Part, and % × Whole is left. {t} × {d} = {r}.",
  "op1": "{p}% of a number is {r}. Which operation gives the number?", "op1a": "Multiplying would give a number smaller than the part; the whole must be larger.", "op1s": "The whole is missing: cover the Whole, and Part ÷ % is left. {r} ÷ {d} = {t}.",
  "op2": "What percent is {r} of {t}? Which operation solves it?", "op2a": "Divide the part by the whole, not the other way around. The whole is the number after “of.”", "op2c": "That gives the decimal; multiply by 100 to get the percent.", "op2s": "The percent is missing: cover the %, and Part ÷ Whole is left. ({r} ÷ {t}) × 100 = {p}%.",
  "barraVoz": "A bar for the whole, {t}, with {p} percent shaded.",
  "deEs": "{p}% of {t}: {t} × {d} = <strong>{r}</strong>.", "alReves": "The other way: if {p}% of a number is {r}, the number is {r} ÷ {d} = {t}. And {r} of {t} is ({r} ÷ {t}) × 100 = {p}%.",
  "t0": "What is {p}% of {t}?", "t0a": "Here you know the whole: multiply by the percent as a decimal; do not divide.", "t0b": "Change the percent to a decimal first (divide by 100).", "t0s": "{t} × {d} = {r}.",
  "t1": "{p}% of a number is {r}. What is the number?", "t1a": "You are looking for the whole: divide the part by the percent as a decimal.", "t1s": "{r} ÷ {d} = {t}. Check: {t} × {d} = {r}.",
  "t2": ["Of {t} students, {r} passed the test. What percent passed?", "What percent is {r} of {t}?", "A team won {r} of its {t} games. What percent did it win?"],
  "t2a": "Divide the part by the whole, not the other way around.", "t2b": "Multiply by 100 to change to a percent.", "t2s": "({r} ÷ {t}) × 100 = {p}%.",
  "queBusca": " What are you looking for?", "busca": ["the part", "the whole", "the percent"], "seBusca": "You are looking for {x}",
  "expBusca": ["You know the whole and the percent: you are looking for the part.", "You know the part and the percent: you are looking for the whole.", "You know the part and the whole: you are looking for the percent."],
  "casos": {"parte": "What is {p}% of {t}?", "todo": "{p}% of a number is {r}. What is the number?", "pct": "What percent is {r} of {t}?"},
  "cruz": "Cross products: {a} = {b}", "planteaPP": " Set up part/whole = %/100.", "propo": "Proportion: ",
  "pp0": "x/{t} = {p}/100 → 100x = {tp} → x = {r}.", "pp0a": "After the cross products, divide by 100.",
  "pp1": "{r}/x = {p}/100 → {p}x = {r100} → x = {t}.", "pp1a": "The x goes on the bottom, where the whole goes: {r}/x = {p}/100.",
  "pp2": "{r}/{t} = x/100 → {t}x = {r100} → x = {p}%.", "pp2a": "The ratio is flipped: the part goes on top and the whole on the bottom.",
  "pp2b": "Of {t} students, {r} passed. What percent passed?"
 },
 "es": {
  "vozGrid": "Una cuadrícula de 100 cuadritos con {k} coloreados.", "cuadritos": "{k} cuadritos coloreados de 100.", "cuadrito1": "1 cuadrito coloreado de 100.",
  "queGrid": "¿Qué porcentaje de la cuadrícula está coloreado?", "sinColor": "Ese es el porcentaje sin colorear.", "bienGrid": "{k} de 100 cuadritos: {k}%.",
  "escribe": "Escriba un porcentaje (45%), un decimal (0.45) o una fracción (9/20).", "pct": "Porcentaje", "dec": "Decimal", "frac": "Fracción", "aprox": " (aproximado)",
  "comoDec": "{p} como decimal es:", "expDec": "{p} ÷ 100 = {d}: el punto decimal se mueve dos lugares a la izquierda.",
  "comoPct": "{d} como porcentaje es:", "expPct": "{d} × 100 = {p}: el punto decimal se mueve dos lugares a la derecha.",
  "comoFr": "{p} como fracción simplificada es:", "expFr": "{p} = {p0}/100 = {f}.",
  "frPct": "{f} como porcentaje es:", "expFrPct": "{a} ÷ {b} = {d}, y × 100 = {p}.",
  "tapaElige": "Elija qué le falta y el triángulo tapa ese elemento.",
  "tapa": {"parte": ["<strong>Parte = % × Todo</strong>: el % y el Todo quedan lado a lado, se multiplican.", "Ejemplo: el 15% de $80 → 0.15 × 80 = <strong>$12</strong>."],
           "pct": ["<strong>% = Parte ÷ Todo</strong> (y se multiplica por 100): la Parte queda arriba del Todo, se divide.", "Ejemplo: 18 de 25 → 18 ÷ 25 = 0.72 → <strong>72%</strong>."],
           "todo": ["<strong>Todo = Parte ÷ %</strong>: la Parte queda arriba del %, se divide.", "Ejemplo: el 30% de un número es 45 → 45 ÷ 0.30 = <strong>150</strong>."]},
  "op0": "¿Cuánto es el {p}% de {t}? ¿Qué operación lo resuelve?", "op0a": "Se conoce el todo: la parte se obtiene multiplicando, no dividiendo.", "opDec": "El porcentaje entra en decimal: {p}% = {d}.", "op0s": "Falta la parte: se tapa la Parte y quedan % × Todo. {t} × {d} = {r}.",
  "op1": "El {p}% de un número es {r}. ¿Qué operación da el número?", "op1a": "Multiplicar daría un número más chico que la parte; el todo tiene que ser mayor.", "op1s": "Falta el todo: se tapa el Todo y queda Parte ÷ %. {r} ÷ {d} = {t}.",
  "op2": "¿Qué porcentaje es {r} de {t}? ¿Qué operación lo resuelve?", "op2a": "Se divide la parte entre el todo, no al revés. El todo es el número que va después de «de».", "op2c": "Eso da el decimal; falta multiplicar por 100 para llegar al porcentaje.", "op2s": "Falta el porcentaje: se tapa el % y queda Parte ÷ Todo. ({r} ÷ {t}) × 100 = {p}%.",
  "barraVoz": "Barra del todo, {t}, con el {p} por ciento sombreado.",
  "deEs": "El {p}% de {t}: {t} × {d} = <strong>{r}</strong>.", "alReves": "Al revés: si el {p}% de un número es {r}, el número es {r} ÷ {d} = {t}. Y {r} de {t} es ({r} ÷ {t}) × 100 = {p}%.",
  "t0": "¿Cuánto es el {p}% de {t}?", "t0a": "Aquí se conoce el todo: se multiplica por el porcentaje en decimal, no se divide.", "t0b": "Falta pasar el porcentaje a decimal (dividir entre 100).", "t0s": "{t} × {d} = {r}.",
  "t1": "El {p}% de un número es {r}. ¿Cuál es ese número?", "t1a": "Se busca el todo: se divide la parte entre el porcentaje en decimal.", "t1s": "{r} ÷ {d} = {t}. Comprobación: {t} × {d} = {r}.",
  "t2": ["De {t} estudiantes, {r} aprobaron el examen. ¿Qué porcentaje aprobó?", "¿Qué porcentaje es {r} de {t}?", "Un equipo ganó {r} de sus {t} partidos. ¿Qué porcentaje ganó?"],
  "t2a": "Se divide la parte entre el todo, no al revés.", "t2b": "Falta multiplicar por 100 para pasar a porcentaje.", "t2s": "({r} ÷ {t}) × 100 = {p}%.",
  "queBusca": " ¿Qué se busca?", "busca": ["la parte", "el todo", "el porcentaje"], "seBusca": "Se busca {x}",
  "expBusca": ["Se conocen el todo y el porcentaje: se busca la parte.", "Se conocen la parte y el porcentaje: se busca el todo.", "Se conocen la parte y el todo: se busca el porcentaje."],
  "casos": {"parte": "¿Cuánto es el {p}% de {t}?", "todo": "El {p}% de un número es {r}. ¿Cuál es el número?", "pct": "¿Qué porcentaje es {r} de {t}?"},
  "cruz": "Producto cruzado: {a} = {b}", "planteaPP": " Plantee parte/todo = %/100.", "propo": "Proporción: ",
  "pp0": "x/{t} = {p}/100 → 100x = {tp} → x = {r}.", "pp0a": "Falta dividir entre 100 después del producto cruzado.",
  "pp1": "{r}/x = {p}/100 → {p}x = {r100} → x = {t}.", "pp1a": "La x va abajo, en el lugar del todo: {r}/x = {p}/100.",
  "pp2": "{r}/{t} = x/100 → {t}x = {r100} → x = {p}%.", "pp2a": "Se invirtió la razón: la parte va arriba y el todo abajo.",
  "pp2b": "De {t} estudiantes, {r} aprobaron. ¿Qué porcentaje aprobó?"
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function fq(a, b){ return '<span aria-hidden="true"><span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + '</span></span></span><span class="sr-only">' + a + '/' + b + '</span>'; }
function pc(x){ return nd(Math.round(x * 1000) / 1000) + "%"; }
function red(p, q){ var g = mcdR(p, q) || 1; return [p / g, q / g]; }
function sinPct(t){ return String(t).replace(/%/g, ""); }
function cuadricula(k, voz){
  var c = 26, s = '<svg class="figura" style="max-width:300px" viewBox="0 0 ' + (10 * c + 4) + ' ' + (10 * c + 4) + '" role="img" aria-label="' + voz + '">';
  for (var i = 0; i < 100; i++){ var x = 2 + (i % 10) * c, y = 2 + Math.floor(i / 10) * c; s += '<rect x="' + x + '" y="' + y + '" width="' + c + '" height="' + c + '" fill="' + (i < k ? "#b33c00" : "#fff") + '" stroke="#90a4ae" stroke-width="1"/>'; }
  return s + '<rect x="2" y="2" width="' + 10 * c + '" height="' + 10 * c + '" fill="none" stroke="#263238" stroke-width="2"/></svg>';
}
function datosPct(){
  for (var z = 0; z < 100; z++){
    var p = elige([10, 15, 20, 25, 30, 40, 50, 60, 75, 5, 8, 12]), tot = 20 * aleatorio(2, 20), parte = tot * p / 100;
    if (parte === Math.round(parte * 100) / 100) return { p: p, tot: tot, parte: parte, d: nd(p / 100) };
  }
}

/* ============ MODULE 1 · out of 100 ============ */
function pintaC1(){
  var p = +$("c1-p").value, r = red(p, 100); $("c1-pv").textContent = p + "%";
  $("c1-svg").innerHTML = cuadricula(p, F(TXT.vozGrid, { k: p }));
  $("c1-salida").innerHTML = '<div class="linea grande">' + p + '% = ' + fq(p, 100) + (p > 0 && r[1] !== 100 ? ' = ' + fq(r[0], r[1]) : '') + ' = ' + nd(p / 100) + '</div><div class="linea">' + (p === 1 ? TXT.cuadrito1 : F(TXT.cuadritos, { k: p })) + '</div>';
}
function genCuadricula(){
  var k = aleatorio(3, 97), vs = [k, 100 - k, k / 10, Math.min(100, k * 10)].filter(function(v, i, a){ return a.indexOf(v) === i; });
  var pist = {}; pist["p" + (100 - k)] = TXT.sinColor;
  return { enun: TXT.queGrid + cuadricula(k, F(TXT.vozGrid, { k: k })), opciones: vs.map(function(v){ return { html: pc(v), clave: "p" + v }; }), correcta: "p" + k, pistas: pist,
    bien: F(TXT.bienGrid, { k: k }), mal: F(TXT.bienGrid, { k: k }) };
}

/* ============ MODULE 2 · conversions ============ */
function leePct(s){
  var t = String(s).trim().replace(/\s+/g, ""), m;
  if ((m = t.match(/^(\d*\.?\d+)%$/))) return { v: parseFloat(m[1]) / 100 };
  if ((m = t.match(/^(\d+)\/(\d+)$/))){ if (+m[2] === 0) return null; return { v: +m[1] / +m[2], f: red(+m[1], +m[2]) }; }
  if ((m = t.match(/^(\d*\.?\d+)$/))) return { v: parseFloat(m[1]) };
  return null;
}
function aFrac(v){ for (var k = 0; k <= 6; k++){ var d = Math.pow(10, k); if (Math.abs(Math.round(v * d) - v * d) < 1e-9) return red(Math.round(v * d), d); } return null; }
function pintaCV(){
  var r = leePct($("cv-v").value), sal = $("cv-salida");
  if (!r){ sal.innerHTML = TXT.escribe; return; }
  var f = r.f || aFrac(r.v), dec = Math.round(r.v * 100000) / 100000;
  sal.innerHTML = '<div class="linea">' + TXT.pct + ': <strong>' + pc(r.v * 100) + '</strong></div><div class="linea">' + TXT.dec + ': <strong>' + nd(dec) + '</strong>' + (Math.abs(dec - r.v) > 1e-12 ? TXT.aprox : '') +
    '</div><div class="linea">' + TXT.frac + ': <strong>' + (f ? (f[1] === 1 ? f[0] : fq(f[0], f[1])) : "—") + '</strong></div>';
}
function uniq(o){ var v = {}; return o.filter(function(x){ if (v[x.clave]) return false; v[x.clave] = 1; return true; }); }
function genConv(){
  var tp = aleatorio(1, 4), p, exp;
  if (tp === 1){ p = elige([4, 6, 8, 12, 15, 35, 45, 60, 75, 5, 50, 150]); exp = F(TXT.expDec, { p: p + "%", d: nd(p / 100) });
    return { enun: F(TXT.comoDec, { p: p + "%" }), opciones: uniq([nd(p / 100), nd(p / 10), nd(p / 1000), String(p)].map(function(x){ return { html: x, clave: "d" + x }; })), correcta: "d" + nd(p / 100), bien: exp, mal: exp }; }
  if (tp === 2){ var d = elige([0.08, 0.5, 0.05, 0.35, 0.7, 0.125, 1.2, 0.03, 0.005]); exp = F(TXT.expPct, { d: nd(d), p: pc(d * 100) });
    return { enun: F(TXT.comoPct, { d: nd(d) }), opciones: uniq([pc(d * 100), pc(d * 10), pc(d * 1000), pc(d)].map(function(x){ return { html: x, clave: "p" + x }; })), correcta: "p" + pc(d * 100), bien: exp, mal: exp }; }
  if (tp === 3){ p = elige([20, 25, 40, 60, 75, 80, 10, 5, 30, 45]); var r = red(p, 100); exp = F(TXT.expFr, { p: p + "%", p0: p, f: r[0] + "/" + r[1] });
    var o = [{ html: fq(r[0], r[1]), clave: "ok" }, { html: fq(p, 10), clave: "a" }, { html: fq(r[1], r[0]), clave: "b" }, { html: fq(r[0] + 1, r[1]), clave: "c" }];
    return { enun: F(TXT.comoFr, { p: p + "%" }), opciones: o, correcta: "ok", bien: exp, mal: exp }; }
  var f = elige([[1, 4], [3, 4], [1, 5], [2, 5], [3, 8], [1, 8], [7, 20], [9, 25], [1, 2]]), v = f[0] / f[1];
  exp = F(TXT.expFrPct, { a: f[0], b: f[1], d: nd(v), p: pc(v * 100) });
  return { enun: F(TXT.frPct, { f: fq(f[0], f[1]) }), opciones: uniq([pc(v * 100), pc(v * 10), pc(f[0]), pc(f[1] / f[0])].map(function(x){ return { html: x, clave: "p" + x }; })), correcta: "p" + pc(v * 100), bien: exp, mal: exp };
}

/* ============ MODULE 3 · the triangle ============ */
var TAPA = { parte: [95, 62, 110, 40], pct: [60, 150, 80, 34], todo: [160, 150, 80, 34] };
function pintaTR(k){
  document.querySelectorAll("#tr-botones .eleccion").forEach(function(b){ b.setAttribute("aria-pressed", b.getAttribute("data-tapa") === k ? "true" : "false"); });
  var r = $("tr-tapa");
  if (!k){ r.setAttribute("width", 0); r.setAttribute("height", 0); $("tr-salida").innerHTML = '<div class="linea">' + TXT.tapaElige + '</div>'; return; }
  var tt = TAPA[k]; r.setAttribute("x", tt[0]); r.setAttribute("y", tt[1]); r.setAttribute("width", tt[2]); r.setAttribute("height", tt[3]);
  $("tr-salida").innerHTML = TXT.tapa[k].map(function(x){ return '<div class="linea">' + x + '</div>'; }).join("");
}
function genOperacion(){
  var d = datosPct(), tp = aleatorio(0, 2), Q = { pistas: {}, correcta: "ok" }, o = { p: d.p, t: d.tot, d: d.d, r: nd(d.parte) };
  if (tp === 0){ Q.enun = F(TXT.op0, o);
    Q.opciones = [{ html: d.tot + " × " + d.d, clave: "ok" }, { html: d.tot + " ÷ " + d.d, clave: "a" }, { html: d.d + " ÷ " + d.tot, clave: "b" }, { html: d.tot + " × " + d.p, clave: "c" }];
    Q.pistas = { a: TXT.op0a, c: F(TXT.opDec, o) }; Q.bien = Q.mal = F(TXT.op0s, o); }
  else if (tp === 1){ Q.enun = F(TXT.op1, o);
    Q.opciones = [{ html: nd(d.parte) + " ÷ " + d.d, clave: "ok" }, { html: nd(d.parte) + " × " + d.d, clave: "a" }, { html: d.d + " ÷ " + nd(d.parte), clave: "b" }, { html: nd(d.parte) + " ÷ " + d.p, clave: "c" }];
    Q.pistas = { a: TXT.op1a, c: F(TXT.opDec, o) }; Q.bien = Q.mal = F(TXT.op1s, o); }
  else { Q.enun = F(TXT.op2, o);
    Q.opciones = [{ html: "(" + nd(d.parte) + " ÷ " + d.tot + ") × 100", clave: "ok" }, { html: "(" + d.tot + " ÷ " + nd(d.parte) + ") × 100", clave: "a" }, { html: nd(d.parte) + " × " + d.tot, clave: "b" }, { html: nd(d.parte) + " ÷ " + d.tot, clave: "c" }];
    Q.pistas = { a: TXT.op2a, c: TXT.op2c }; Q.bien = Q.mal = F(TXT.op2s, o); }
  return Q;
}

/* ============ MODULE 4 · the three cases ============ */
function barra(total, p, parte){
  var x0 = 30, x1 = 610, w = (x1 - x0) * Math.min(p, 100) / 100;
  var s = '<svg class="figura" viewBox="0 0 640 110" role="img" aria-label="' + F(TXT.barraVoz, { t: total, p: p }) + '">';
  s += '<rect x="' + x0 + '" y="30" width="' + (x1 - x0) + '" height="40" fill="#fff" stroke="#263238" stroke-width="2"/><rect x="' + x0 + '" y="30" width="' + f1(w) + '" height="40" fill="#ef6c00"/>';
  for (var i = 1; i < 10; i++) s += linea([x0 + (x1 - x0) * i / 10, 30], [x0 + (x1 - x0) * i / 10, 70], "#b0bec5", 1);
  s += texto([x0 + w / 2, 50], parte, 16, "#fff") + '<text x="' + x0 + '" y="18" font-size="13" fill="#424242">0%</text><text x="' + x1 + '" y="18" font-size="13" font-weight="700" fill="#424242" text-anchor="end">100% = ' + total + '</text>' + texto([x0 + w, 88], p + "%", 14, "#263238");
  return s + '</svg>';
}
function pintaTT(){
  var tt = +$("tt-t").value, p = +$("tt-p").value, parte = tt * p / 100, o = { p: p, t: tt, d: nd(p / 100), r: nd(parte) };
  $("tt-tv").textContent = tt; $("tt-pv").textContent = p + "%";
  $("tt-svg").innerHTML = barra(tt, p, nd(parte));
  $("tt-salida").innerHTML = '<div class="linea">' + F(TXT.deEs, o) + '</div><div class="linea">' + F(TXT.alReves, o) + '</div>';
}
function problemaTipo(tp){
  var d = datosPct(), o = { p: d.p, t: d.tot, d: d.d, r: nd(d.parte) };
  if (tp === 0) return { txt: F(TXT.t0, o), res: d.parte, sol: F(TXT.t0s, o), pistas: [{ v: d.tot / (d.p / 100), msg: TXT.t0a }, { v: d.tot * d.p, msg: TXT.t0b }] };
  if (tp === 1) return { txt: F(TXT.t1, o), res: d.tot, sol: F(TXT.t1s, o), pistas: [{ v: d.parte * d.p / 100, msg: TXT.t1a }] };
  return { txt: F(elige(TXT.t2), o), res: d.p, sol: F(TXT.t2s, o), pistas: [{ v: d.tot / d.parte * 100, msg: TXT.t2a }, { v: d.parte / d.tot, msg: TXT.t2b }] };
}
function genQueBusca(){
  var tp = aleatorio(0, 2), q = problemaTipo(tp);
  return { enun: q.txt + TXT.queBusca, opciones: TXT.busca.map(function(x, i){ return { html: F(TXT.seBusca, { x: x }), clave: "t" + i }; }), correcta: "t" + tp, enOrden: true, bien: TXT.expBusca[tp], mal: TXT.expBusca[tp] };
}
function genTipos(){
  var q = problemaTipo(aleatorio(0, 2)), ev = numD(q.res, q.pistas.filter(function(x){ return Math.abs(x.v - q.res) > 0.01; }));
  return { enun: q.txt, correcta: nd(q.res), solucion: q.sol, evalua: function(s){ return ev(sinPct(s)); } };
}

/* ============ MODULE 5 · the percent proportion ============ */
var CASO_PP = "parte";
function pintaPP(){
  var tt = +$("pp-t").value, p = +$("pp-p").value, parte = tt * p / 100, o = { p: p, t: tt, r: nd(parte) }, h;
  $("pp-tv").textContent = tt; $("pp-pv").textContent = p + "%";
  document.querySelectorAll("#pp-botones .eleccion").forEach(function(b){ b.setAttribute("aria-pressed", b.getAttribute("data-caso") === CASO_PP ? "true" : "false"); });
  if (CASO_PP === "parte") h = [F(TXT.casos.parte, o), fq("x", tt) + ' = ' + fq(p, 100), F(TXT.cruz, { a: "100 × x", b: tt + " × " + p + " = " + nd(tt * p) }), 'x = ' + nd(tt * p) + ' ÷ 100 = <strong>' + nd(parte) + '</strong>'];
  else if (CASO_PP === "todo") h = [F(TXT.casos.todo, o), fq(nd(parte), "x") + ' = ' + fq(p, 100), F(TXT.cruz, { a: p + " × x", b: nd(parte) + " × 100 = " + nd(parte * 100) }), 'x = ' + nd(parte * 100) + ' ÷ ' + p + ' = <strong>' + tt + '</strong>'];
  else h = [F(TXT.casos.pct, o), fq(nd(parte), tt) + ' = ' + fq("x", 100), F(TXT.cruz, { a: tt + " × x", b: nd(parte) + " × 100 = " + nd(parte * 100) }), 'x = ' + nd(parte * 100) + ' ÷ ' + tt + ' = <strong>' + p + '%</strong>'];
  $("pp-salida").innerHTML = h.map(function(x, i){ return '<div class="linea' + (i === 1 ? ' grande' : '') + '">' + x + '</div>'; }).join("");
}
function genProporcion(){
  var d = datosPct(), tp = aleatorio(0, 2), o = { p: d.p, t: d.tot, r: nd(d.parte), tp: nd(d.tot * d.p), r100: nd(d.parte * 100) }, txt, res, prop, pist;
  if (tp === 0){ txt = F(TXT.casos.parte, o); res = d.parte; prop = F(TXT.pp0, o); pist = [{ v: d.tot * d.p, msg: TXT.pp0a }]; }
  else if (tp === 1){ txt = F(TXT.casos.todo, o); res = d.tot; prop = F(TXT.pp1, o); pist = [{ v: d.parte * d.p / 100, msg: F(TXT.pp1a, o) }]; }
  else { txt = F(elige([TXT.casos.pct, TXT.pp2b]), o); res = d.p; prop = F(TXT.pp2, o); pist = [{ v: Math.round(d.tot / d.parte * 10000) / 100, msg: TXT.pp2a }]; }
  var ev = numD(res, pist.filter(function(x){ return Math.abs(x.v - res) > 0.01; }));
  return { enun: txt + TXT.planteaPP, correcta: nd(res), solucion: TXT.propo + prop, evalua: function(s){ return ev(sinPct(s)); } };
}

/* ============ Start ============ */
$("c1-p").addEventListener("input", pintaC1); pintaC1();
creaPracticaOM("p1", genCuadricula);
$("cv-v").addEventListener("input", pintaCV); pintaCV();
creaPracticaOM("p2", genConv);
document.querySelectorAll("#tr-botones .eleccion").forEach(function(b){ b.addEventListener("click", function(){ pintaTR(b.getAttribute("data-tapa")); }); }); pintaTR(null);
creaPracticaOM("p3", genOperacion);
["tt-t", "tt-p"].forEach(function(id){ $(id).addEventListener("input", pintaTT); }); pintaTT();
creaPracticaOM("p4", genQueBusca);
creaPracticaLibre("p5", genTipos);
document.querySelectorAll("#pp-botones .eleccion").forEach(function(b){ b.addEventListener("click", function(){ CASO_PP = b.getAttribute("data-caso"); pintaPP(); }); });
["pp-t", "pp-p"].forEach(function(id){ $(id).addEventListener("input", pintaPP); }); pintaPP();
creaPracticaLibre("p6", genProporcion);
'''

def libre_p(pid, titulo, etiqueta):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."),
        t("Type only the number, with no % sign. It may have decimals, like 12.5.", "Escriba solo el número, sin el signo %. Puede llevar decimales, como 12.5."))

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    frm = '<span class="fracc"><span class="fa">{}</span><span class="fb2">{}</span></span>'
    mods = [
     (t("per-100", "razon-100"), t("A percent is a ratio out of 100", "El porcentaje como razón de 100"),
      f'''      <p>{t("<strong>Percent</strong> means “for every hundred.” A percent is a ratio whose second term is always 100: 25% is 25 parts out of every 100, which you can also write 25/100 or 0.25.", "<strong>Por ciento</strong> quiere decir «por cada cien». Un porcentaje es una razón cuyo segundo término es siempre 100: 25% son 25 partes de cada 100, que también se escribe 25/100 o 0.25.")}</p>
      <h3>{t("The grid of 100", "La cuadrícula de 100")}</h3>
      <div class="panel">
        {desl("c1-p", t("Percent", "Porcentaje"), 0, 100, 25)}
        <div id="c1-svg"></div>
        <div class="salida" id="c1-salida" aria-live="polite"></div>
      </div>
{B.om("p1", t("Practice: what percent is shaded?", "Practique: ¿qué porcentaje está coloreado?"))}'''),
     (t("conversions", "conversiones"), t("Fractions, decimals, and percents", "Fracción, decimal y porcentaje"),
      f'''      <table class="reglas">
        <caption>{t("How to go from one form to another", "Cómo pasar de una forma a otra")}</caption>
        <thead><tr><th scope="col">{t("Conversion", "Conversión")}</th><th scope="col">{t("How", "Procedimiento")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Percent → decimal", "Porcentaje → decimal")}</td><td>{t("divide by 100: move the point two places to the left", "dividir entre 100: el punto se mueve dos lugares a la izquierda")}</td><td>45% = 0.45</td></tr>
          <tr><td>{t("Decimal → percent", "Decimal → porcentaje")}</td><td>{t("multiply by 100: move the point two places to the right", "multiplicar por 100: el punto se mueve dos lugares a la derecha")}</td><td>0.07 = 7%</td></tr>
          <tr><td>{t("Percent → fraction", "Porcentaje → fracción")}</td><td>{t("write it over 100 and simplify", "escribir sobre 100 y simplificar")}</td><td>40% = 40/100 = 2/5</td></tr>
          <tr><td>{t("Fraction → percent", "Fracción → porcentaje")}</td><td>{t("divide and multiply by 100", "dividir y multiplicar por 100")}</td><td>3/4 = 0.75 = 75%</td></tr>
        </tbody>
      </table>
      <h3>{t("Converter", "Conversor")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="cv-v">{t("Type a percent (45%), a decimal (0.45), or a fraction (9/20)", "Escriba un porcentaje (45%), un decimal (0.45) o una fracción (9/20)")}</label><input type="text" autocomplete="off" class="ancho" id="cv-v" value="3/4"></div></div>
        <div class="salida" id="cv-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Common mistake:", "Error frecuente:")}</strong> {t("mixing up 0.5 and 5%. In fact 0.5 = 50%, and 5% = 0.05.", "confundir 0.5 con 5%. En realidad 0.5 = 50%, y 5% = 0.05.")}</div>
{B.om("p2", t("Practice: convert", "Practique: convierta"))}'''),
     (t("triangle", "triangulo"), t("The percent triangle", "El triángulo del porcentaje"),
      f'''      <p>{t("Every percent problem joins three pieces in one formula: <strong>Part = Percent × Whole</strong>, with the percent as a decimal. The triangle helps you remember which operation to use: <strong>cover</strong> what is missing and read what is left. Side by side, multiply; one above the other, divide.", "Todo problema de porcentaje une tres elementos en una sola fórmula: <strong>Parte = Porcentaje × Todo</strong>, con el porcentaje en decimal. El triángulo ayuda a recordar qué operación usar: se <strong>tapa</strong> lo que falta y se lee lo que queda. Lo que está lado a lado se multiplica; lo que está arriba y abajo se divide.")}</p>
      <h3>{t("Cover what you are missing", "Tape lo que le falta")}</h3>
      <div class="panel">
        <svg class="figura" style="max-width:320px" viewBox="0 0 300 220" role="img" aria-labelledby="tr-titulo">
          <title id="tr-titulo">{t("The percent triangle: Part on top; on the bottom, separated by a times sign, the percent and the Whole.", "Triángulo del porcentaje: arriba la Parte; abajo, separados por un signo de multiplicar, el porcentaje y el Todo.")}</title>
          <polygon points="150,10 290,205 10,205" fill="#fff3e0" stroke="#7a2800" stroke-width="3"/>
          <line x1="73" y1="118" x2="227" y2="118" stroke="#7a2800" stroke-width="3"/>
          <text x="150" y="92" font-size="24" font-weight="700" text-anchor="middle" fill="#7a2800">{t("Part", "Parte")}</text>
          <text x="100" y="172" font-size="22" font-weight="700" text-anchor="middle" fill="#7a2800">%</text>
          <text x="200" y="172" font-size="22" font-weight="700" text-anchor="middle" fill="#7a2800">{t("Whole", "Todo")}</text>
          <text x="150" y="176" font-size="20" text-anchor="middle" fill="#7a2800" aria-hidden="true">×</text>
          <rect id="tr-tapa" x="0" y="0" width="0" height="0" rx="10" fill="#7a2800"/>
        </svg>
        <div class="elecciones" id="tr-botones" role="group" aria-label="{t("Choose what is missing", "Elija qué valor falta")}">
          <button type="button" class="eleccion" data-tapa="parte" aria-pressed="false">{t("I am missing the part", "Me falta la parte")}</button>
          <button type="button" class="eleccion" data-tapa="pct" aria-pressed="false">{t("I am missing the percent", "Me falta el porcentaje")}</button>
          <button type="button" class="eleccion" data-tapa="todo" aria-pressed="false">{t("I am missing the whole", "Me falta el todo")}</button>
        </div>
        <div class="salida" id="tr-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Which number is the whole?", "¿Cuál es el todo?")}</strong> {t("It is the reference amount, the one after the word “of”: “15% <strong>of</strong> $80,” “18 <strong>of</strong> 25.”", "Es la cantidad de referencia, la que aparece después de la palabra «de»: «el 15% <strong>de</strong> $80», «18 <strong>de</strong> 25».")}</div>
{B.om("p3", t("Practice: which operation solves it?", "Practique: ¿qué operación lo resuelve?"))}'''),
     (t("three-cases", "tres-tipos"), t("The three kinds of problems", "Los tres tipos de problemas"),
      f'''      <p>{t("Every percent problem has three pieces: the <strong>part</strong>, the <strong>whole</strong>, and the <strong>percent</strong>. If you know two, you can find the third.", "Todo problema de porcentaje tiene tres elementos: la <strong>parte</strong>, el <strong>todo</strong> y el <strong>porcentaje</strong>. Si se conocen dos, se calcula el tercero.")}</p>
      <h3>{t("The bar model", "El modelo de barra")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("tt-t", t("Whole", "Todo"), 20, 400, 80, 10)}
          {desl("tt-p", t("Percent", "Porcentaje"), 5, 100, 15, 5)}
        </div>
        <div id="tt-svg"></div>
        <div class="salida" id="tt-salida" aria-live="polite"></div>
      </div>
{B.om("p4", t("Practice: what are you looking for?", "Practique: ¿qué se busca?"))}
{libre_p("p5", t("Practice: solve", "Practique: resuelva"), t("Answer", "Resultado"))}'''),
     (t("percent-proportion", "proporcion-porcentual"), t("The percent proportion", "La proporción porcentual"),
      f'''      <p>{t("Because a percent is a ratio out of 100, any problem can be set up as a direct proportion (Lesson 4.2). Put in the three values you know, put x where the missing one goes, and solve with <strong>cross products</strong>.", "Como un porcentaje es una razón de 100, cualquier problema se puede plantear como una proporción directa (Lección 4.2). Se colocan los tres datos conocidos, la x en el lugar del que falta, y se resuelve con el <strong>producto cruzado</strong>.")}</p>
      <div class="formula">{frm.format(t("part", "parte"), t("whole", "todo"))} = {frm.format("%", "100")}</div>
      <h3>{t("Set up the proportion", "Plantee la proporción")}</h3>
      <div class="panel">
        <div class="elecciones" id="pp-botones" role="group" aria-label="{t("Choose what you are looking for", "Elija qué se busca")}">
          <button type="button" class="eleccion" data-caso="parte" aria-pressed="true">{t("Find the part", "Se busca la parte")}</button>
          <button type="button" class="eleccion" data-caso="todo" aria-pressed="false">{t("Find the whole", "Se busca el todo")}</button>
          <button type="button" class="eleccion" data-caso="pct" aria-pressed="false">{t("Find the percent", "Se busca el porcentaje")}</button>
        </div>
        <div class="campos">
          {desl("pp-t", t("Whole", "Todo"), 20, 400, 80, 20)}
          {desl("pp-p", t("Percent", "Porcentaje"), 5, 100, 15, 5)}
        </div>
        <div class="salida" id="pp-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip"><strong>{t("Which method is better?", "¿Qué método conviene?")}</strong> {t("The formula is faster with a calculator; the proportion helps when you do not know which operation to use. Use one to check the other.", "La fórmula es más rápida con calculadora; la proporción ayuda cuando no se sabe qué operación hacer. Use uno para comprobar el otro.")}</div>
{libre_p("p6", t("Practice: solve with the proportion", "Practique: resuelva con la proporción"), t("Answer", "Resultado"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "El porcentaje: conversiones y los tres casos fundamentales")
