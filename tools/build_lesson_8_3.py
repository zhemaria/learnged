"""Lesson 8.3 · Final project — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "8-3"
AZ, GR, TXC = "#1565c0", "#37474f", "#1a2330"

def txt(x, y, s, size=15, color=TXC, anchor="middle", peso=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{peso}" fill="{color}">{s}</text>'

def grafica_gastos():
    cats = [t("Food", "Comida"), t("Drinks", "Bebidas"), t("Cake", "Pastel"), t("Banner", "Cinta"), t("Tables", "Mesas")]
    vals = [170, 36, 45, 60, 37.5]
    x0, y0, W, H, tope, paso = 80, 40, 500, 240, 180, 20
    s = [txt(x0 + W / 2, 24, t("Party budget by category", "Presupuesto de la fiesta por categoría"), 17)]
    for v in range(0, tope + 1, paso):
        y = y0 + H - H * v / tope
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + W}" y2="{y:.1f}" stroke="#cfd8dc" stroke-width="1"/>' + txt(x0 - 8, y + 5, f"${v}", 14, TXC, "end", 400))
    bw = W / 5
    for i, (c, v) in enumerate(zip(cats, vals)):
        h = H * v / tope
        s.append(f'<rect x="{x0 + i * bw + bw * 0.18:.1f}" y="{y0 + H - h:.1f}" width="{bw * 0.64:.1f}" height="{h:.1f}" fill="{AZ}"/>' + txt(x0 + i * bw + bw / 2, y0 + H + 22, c))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/><line x1="{x0}" y1="{y0 + H}" x2="{x0 + W}" y2="{y0 + H}" stroke="{GR}" stroke-width="2"/>')
    return svg("0 0 620 320", t("A bar graph titled Party budget by category. The scale goes from 0 to 180 dollars by 20. Food: 170 dollars. Drinks: 36. Cake: 45. Banner: 60. Tables: 37.50.",
                                "Una gráfica de barras titulada Presupuesto de la fiesta por categoría. La escala va de 0 a 180 dólares de 20 en 20. Comida: 170 dólares. Bebidas: 36. Pastel: 45. Cinta: 60. Mesas: 37.50."), "".join(s), ancho=600)

def leccion():
    n = N
    s1 = f'''<p>{t("Congratulations: you have reached the end of Level 1! In this project you will use what you learned in all eight topics to solve one real problem, the way you will on the GED® test and in daily life.",
"¡Felicidades: llegó al final del Nivel 1! En este proyecto va a usar lo que aprendió en los ocho temas para resolver un solo problema real, como lo hará en el examen de GED® y en la vida diaria.")}</p>
{caja("tip", t("The project", "El proyecto"), t("<p>You are planning a <strong>family celebration for 20 guests</strong> with a budget of <strong>$500</strong>. You must decide what to buy, check that it fits the budget, plan the time and the space, and present your plan with a table and a graph.</p>",
"<p>Usted va a planear una <strong>celebración familiar para 20 invitados</strong> con un presupuesto de <strong>$500</strong>. Tiene que decidir qué comprar, comprobar que alcanza el dinero, planear el tiempo y el espacio, y presentar su plan con una tabla y una gráfica.</p>"))}
{tabla(t("The skills of Level 1 in this project", "Las destrezas del Nivel 1 en este proyecto"), t("Which Level 1 topic helps with each part of the project", "Qué tema del Nivel 1 ayuda en cada parte del proyecto"),
       [t("Part of the project", "Parte del proyecto"), t("Topic", "Tema")],
       [[t("add and subtract the costs", "sumar y restar los costos"), t("Topic 1 · Whole numbers", "Tema 1 · Números enteros")],
        [t("price for each guest, number of tables", "precio por invitado, cantidad de mesas"), t("Topic 2 · Multiplication and division", "Tema 2 · Multiplicación y división")],
        [t("prices with cents", "precios con centavos"), t("Topic 3 · Decimals", "Tema 3 · Decimales")],
        [t("part of the budget for each thing", "la parte del presupuesto para cada cosa"), t("Topic 4 · Fractions", "Tema 4 · Fracciones")],
        [t("write the problem as an equation", "escribir el problema como ecuación"), t("Topic 5 · Algebraic thinking", "Tema 5 · Pensamiento algebraico")],
        [t("gallons and cups, the schedule", "galones y tazas, el horario"), t("Topic 6 · Measurement and time", "Tema 6 · Medidas y tiempo")],
        [t("the banner around the room, the dance floor", "la cinta alrededor del salón, la pista de baile"), t("Topic 7 · Geometry", "Tema 7 · Geometría")],
        [t("the expense table and the graph", "la tabla de gastos y la gráfica"), t("Topic 8 · Tables and graphs", "Tema 8 · Tablas y gráficas")]])}'''

    s2 = f'''<p>{t("Start with the money. Decide how much of the budget each thing can use, and calculate each cost.", "Empiece por el dinero. Decida qué parte del presupuesto puede usar cada cosa, y calcule cada costo.")}</p>
{ejemplo(t("Example: food can use 2/5 of the budget. How much is that?", "Ejemplo: la comida puede usar 2/5 del presupuesto. ¿Cuánto es eso?"),
  [("1", t("A fraction of an amount.", "Una fracción de una cantidad."), t("$500 ÷ 5 = $100 (one fifth).", "$500 ÷ 5 = $100 (un quinto).")),
   ("✓", t("Two fifths.", "Dos quintos."), t("2 × $100 = <strong>$200</strong> for food.", "2 × $100 = <strong>$200</strong> para la comida."))])}
{ejemplo(t("Example: each plate of food costs $8.50. How much for 20 guests? Does it fit in $200?", "Ejemplo: cada plato de comida cuesta $8.50. ¿Cuánto cuesta para 20 invitados? ¿Cabe en $200?"),
  [("1", t("Multiply.", "Multiplique."), "20 × $8.50 = $170."),
   ("✓", t("Compare with the limit.", "Compare con el límite."), t("$170 is less than $200 ✓. There are <strong>$30</strong> left from the food budget.", "$170 es menos que $200 ✓. Sobran <strong>$30</strong> del dinero para la comida."))])}
{tabla(t("Expense table", "Tabla de gastos"), t("The expense table for the party: each item, how it is calculated, and its cost", "La tabla de gastos de la fiesta: cada cosa, cómo se calcula y su costo"),
       [t("Item", "Cosa"), t("Calculation", "Cálculo"), t("Cost", "Costo")],
       [[t("Food", "Comida"), "20 × $8.50", "$170.00"],
        [t("Drinks (3 gallons of juice)", "Bebidas (3 galones de jugo)"), "3 × $12", "$36.00"],
        [t("Cake", "Pastel"), "—", "$45.00"],
        [t("Banner around the room", "Cinta alrededor del salón"), t("80 ft × $0.75", "80 pies × $0.75"), "$60.00"],
        [t("Tables (rent)", "Mesas (alquiler)"), "3 × $12.50", "$37.50"],
        [t("<strong>Total</strong>", "<strong>Total</strong>"), "", "<strong>$348.50</strong>"]])}
{ejemplo(t("Example: how much of the $500 is left?", "Ejemplo: ¿cuánto queda de los $500?"),
  [("1", t("Write it as an equation.", "Escríbalo como ecuación."), t("$348.50 + x = $500, where x is the money left.", "$348.50 + x = $500, donde x es el dinero que queda.")),
   ("✓", t("Solve with the inverse operation.", "Resuelva con la operación inversa."), t("x = $500 − $348.50 = <strong>$151.50</strong> left for other things.", "x = $500 − $348.50 = <strong>$151.50</strong> para otras cosas."))])}
{practica("p1", t("Practice 1 — A cost with cents", "Práctica 1 — Un costo con centavos"), t("You rent <strong>3 tables</strong> at <strong>$12.50</strong> each. How much do they cost?", "Usted alquila <strong>3 mesas</strong> a <strong>$12.50</strong> cada una. ¿Cuánto cuestan?"),
          [("a", "$36.50"), ("b", "$37.50"), ("c", "$15.50"), ("d", "$375")])}
{practica("p2", t("Practice 2 — A part of the budget", "Práctica 2 — Una parte del presupuesto"), t("Decorations can use <strong>1/4</strong> of the <strong>$500</strong> budget. How much is that?", "La decoración puede usar <strong>1/4</strong> del presupuesto de <strong>$500</strong>. ¿Cuánto es eso?"),
          [("a", "$125"), ("b", "$100"), ("c", "$250"), ("d", "$2,000")])}
{enlace(n, t("budget", "presupuesto"), t("costs and budget", "costos y presupuesto"), t("Find costs with cents and how much money is left.", "Halle costos con centavos y cuánto dinero queda."))}'''

    s3 = f'''<p>{t("Now plan the <strong>space</strong> and the <strong>time</strong>. The room is 24 ft long and 16 ft wide. The party goes from 4:30 p.m. to 8:15 p.m.", "Ahora planee el <strong>espacio</strong> y el <strong>tiempo</strong>. El salón mide 24 pies de largo y 16 pies de ancho. La fiesta va de 4:30 p.m. a 8:15 p.m.")}</p>
{ejemplo(t("Example: a banner will go all the way around the room. How many feet of banner do you need?", "Ejemplo: una cinta va a darle toda la vuelta al salón. ¿Cuántos pies de cinta necesita?"),
  [("1", t("Around means perimeter.", "Alrededor quiere decir perímetro."), "P = 2 × 24 + 2 × 16 = 48 + 32 = 80."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>80 feet</strong> of banner (at $0.75 per foot, $60).", "<strong>80 pies</strong> de cinta (a $0.75 el pie, $60)."))])}
{ejemplo(t("Example: the dance floor is 12 ft by 10 ft. How much floor does it cover?", "Ejemplo: la pista de baile mide 12 pies por 10 pies. ¿Cuánto piso cubre?"),
  [("1", t("Covering means area.", "Cubrir quiere decir área."), "A = 12 × 10 = 120."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>120 square feet</strong>, out of 24 × 16 = 384 square feet in the room.", "<strong>120 pies cuadrados</strong>, de los 24 × 16 = 384 pies cuadrados del salón."))])}
{ejemplo(t("Example: 3 gallons of juice, served in 8-fluid-ounce cups. Is it enough for 2 cups per guest?", "Ejemplo: 3 galones de jugo, servidos en vasos de 8 onzas líquidas. ¿Alcanza para 2 vasos por invitado?"),
  [("1", t("Same unit.", "La misma unidad."), t("3 × 128 = 384 fluid ounces.", "3 × 128 = 384 onzas líquidas.")),
   ("2", t("Number of cups.", "Cantidad de vasos."), "384 ÷ 8 = 48."),
   ("✓", t("Compare.", "Compare."), t("20 guests × 2 = 40 cups, and 48 > 40 ✓. <strong>Yes, it is enough.</strong>", "20 invitados × 2 = 40 vasos, y 48 > 40 ✓. <strong>Sí alcanza.</strong>"))])}
{ejemplo(t("Example: how long is the party, from 4:30 p.m. to 8:15 p.m.?", "Ejemplo: ¿cuánto dura la fiesta, de 4:30 p.m. a 8:15 p.m.?"),
  [("1", t("Count up.", "Cuente hacia adelante."), t("4:30 → 5:00 is 30 min; 5:00 → 8:00 is 3 h; 8:00 → 8:15 is 15 min.", "4:30 → 5:00 son 30 min; 5:00 → 8:00 son 3 h; 8:00 → 8:15 son 15 min.")),
   ("✓", t("Add the jumps.", "Sume los saltos."), "<strong>3 h 45 min</strong>.")])}
{practica("p3", t("Practice 3 — The dance floor", "Práctica 3 — La pista de baile"), t("The dance floor is <strong>12 ft</strong> by <strong>10 ft</strong>. What is its area?", "La pista de baile mide <strong>12 pies</strong> por <strong>10 pies</strong>. ¿Cuál es su área?"),
          [("a", t("44 sq ft", "44 pies²")), ("b", t("22 sq ft", "22 pies²")), ("c", t("120 sq ft", "120 pies²")), ("d", t("1,200 sq ft", "1,200 pies²"))])}
{enlace(n, t("choose-tool", "elegir-herramienta"), t("choose the right tool", "elegir la herramienta correcta"), t("Decide: perimeter, area, elapsed time, conversion, or mean?", "Decida: ¿perímetro, área, tiempo transcurrido, conversión o media?"))}'''

    s4 = f'''<p>{t("Finally, <strong>organize and present</strong> your plan so another person can understand it with one look: an expense table, a bar graph, and a short summary.", "Por último, <strong>organice y presente</strong> su plan para que otra persona lo entienda con una mirada: una tabla de gastos, una gráfica de barras y un resumen corto.")}</p>
{grafica_gastos()}
{ejemplo(t("Example: the mean cost for each guest", "Ejemplo: el costo medio por invitado"),
  [("1", t("Total ÷ number of guests.", "Total ÷ cantidad de invitados."), "$348.50 ÷ 20 = $17.425."),
   ("✓", t("Round to the cent.", "Redondee al centavo."), t("About <strong>$17.43</strong> for each guest.", "Unos <strong>$17.43</strong> por cada invitado."))])}
{caja("tip", t("Your summary", "Su resumen"), t("<p>Write 3 or 4 sentences: the total cost, the money left, the biggest expense, and one decision you made with the numbers (for example: \"Food is half of the cost, so I chose a cheaper cake.\").</p>",
"<p>Escriba 3 o 4 oraciones: el costo total, el dinero que sobra, el gasto más grande, y una decisión que tomó con los números (por ejemplo: «La comida es la mitad del costo, así que elegí un pastel más barato»).</p>"))}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>The total: type {T("1")}{T("7")}{T("0")} {T("+")} {T("3")}{T("6")} {T("+")} {T("4")}{T("5")} {T("+")} {T("6")}{T("0")} {T("+")} {T("3")}{T("7")} {T(".")} {T("5")} {T("enter")}. The screen shows 348.5. Then type {T("÷")} {T("2")}{T("0")} {T("enter")}: 17.425.</p>""",
f"""<p>El total: escriba {T("1")}{T("7")}{T("0")} {T("+")} {T("3")}{T("6")} {T("+")} {T("4")}{T("5")} {T("+")} {T("6")}{T("0")} {T("+")} {T("3")}{T("7")} {T(".")} {T("5")} {T("enter")}. La pantalla muestra 348.5. Después escriba {T("÷")} {T("2")}{T("0")} {T("enter")}: 17.425.</p>"""))}
{practica("p4", t("Practice 4 — Cost per guest", "Práctica 4 — Costo por invitado"), t("A party for <strong>20 guests</strong> cost <strong>$380</strong>. What is the mean cost per guest?", "Una fiesta para <strong>20 invitados</strong> costó <strong>$380</strong>. ¿Cuál es el costo medio por invitado?"),
          [("a", "$400"), ("b", "$360"), ("c", "$7,600"), ("d", "$19")])}
{enlace(n, t("per-person", "por-persona"), t("cost per person", "costo por persona"), t("Divide a total among the guests.", "Reparta un total entre los invitados."))}
{enlace(n, t("review", "repaso"), t("mixed review", "repaso mixto"), t("Money problems from the project, mixed.", "Problemas de dinero del proyecto, mezclados."))}'''

    secciones = [("s-" + t("project", "proyecto"), t("The final project", "El proyecto final"), s1),
                 ("s-" + t("money", "dinero"), t("Step 1: the money", "Paso 1: el dinero"), s2),
                 ("s-" + t("space-time", "espacio-tiempo"), t("Step 2: space, measures, and time", "Paso 2: el espacio, las medidas y el tiempo"), s3),
                 ("s-" + t("present", "presentar"), t("Step 3: organize and present", "Paso 3: organizar y presentar"), s4)]

    lesson = {"next": t("Level 2", "siguiente etapa: el Nivel 2"), "review": t("the steps of the project", "los pasos del proyecto"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Check the cents: 3 × $0.50 = $1.50, not $0.50.", "Revise los centavos: 3 × $0.50 = $1.50, no $0.50."), "c": t("$15.50 adds $12.50 + $3. Each table costs $12.50: multiply.", "$15.50 suma $12.50 + $3. Cada mesa cuesta $12.50: multiplique."), "d": t("$375 moved the decimal point. 3 × 12.5 = 37.5.", "$375 movió el punto decimal. 3 × 12.5 = 37.5.")},
             "right": t("3 × $12.50 = $37.50.", "3 × $12.50 = $37.50."), "solution": t("3 × $12 = $36 and 3 × $0.50 = $1.50. Total: $37.50.", "3 × $12 = $36 y 3 × $0.50 = $1.50. Total: $37.50.")},
      "p2": {"ok": "a", "hints": {"b": t("$100 is 1/5. One fourth is $500 ÷ 4.", "$100 es 1/5. Un cuarto es $500 ÷ 4."), "c": t("$250 is 1/2. One fourth is half of that.", "$250 es 1/2. Un cuarto es la mitad de eso."), "d": t("$2,000 multiplies by 4. A fourth is smaller: divide.", "$2,000 multiplica por 4. Un cuarto es menos: divida.")},
             "right": t("$500 ÷ 4 = $125.", "$500 ÷ 4 = $125."), "solution": t("1/4 of $500 = $500 ÷ 4 = $125.", "1/4 de $500 = $500 ÷ 4 = $125.")},
      "p3": {"ok": "c", "hints": {"a": t("44 is the perimeter (12 + 10 + 12 + 10). The floor covers an area.", "44 es el perímetro (12 + 10 + 12 + 10). El piso cubre un área."), "b": t("22 is 12 + 10. Multiply length × width.", "22 es 12 + 10. Multiplique largo × ancho."), "d": t("1,200 has an extra zero: 12 × 10 = 120.", "1,200 tiene un cero de más: 12 × 10 = 120.")},
             "right": t("12 × 10 = 120 square feet.", "12 × 10 = 120 pies cuadrados."), "solution": t("Area = length × width = 12 × 10 = 120 square feet.", "Área = largo × ancho = 12 × 10 = 120 pies cuadrados.")},
      "p4": {"ok": "d", "hints": {"a": t("$400 is $380 + $20. Divide the total by the guests.", "$400 es $380 + $20. Divida el total entre los invitados."), "b": t("$360 is $380 − $20. Divide.", "$360 es $380 − $20. Divida."), "c": t("$7,600 multiplies. The cost is shared: divide.", "$7,600 multiplica. El costo se reparte: divida.")},
             "right": t("$380 ÷ 20 = $19.", "$380 ÷ 20 = $19."), "solution": t("Mean = total ÷ number of guests = $380 ÷ 20 = $19 per guest.", "Media = total ÷ cantidad de invitados = $380 ÷ 20 = $19 por invitado.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("$28.50 adds 20 + $8.50. Multiply.", "$28.50 suma 20 + $8.50. Multiplique."), "c": t("$1,700 moved the decimal point. 20 × 8.5 = 170.", "$1,700 movió el punto decimal. 20 × 8.5 = 170."), "d": t("$160 forgets the 50 cents: 20 × $0.50 = $10.", "$160 olvida los 50 centavos: 20 × $0.50 = $10.")}, "solution": t("20 × $8.50 = $170.", "20 × $8.50 = $170.")},
      "B": {"ok": "b", "hints": {"a": t("$250 is half. 2/5 is less than half.", "$250 es la mitad. 2/5 es menos que la mitad."), "c": t("$100 is 1/5. You need 2/5.", "$100 es 1/5. Necesita 2/5."), "d": t("$2.50 divides too much. 1/5 of $500 is $100.", "$2.50 divide de más. 1/5 de $500 es $100.")}, "solution": t("$500 ÷ 5 = $100, and 2 × $100 = $200.", "$500 ÷ 5 = $100, y 2 × $100 = $200.")},
      "C": {"ok": "c", "hints": {"a": t("40 is 24 + 16, only half of the way around.", "40 es 24 + 16, solo la mitad de la vuelta."), "b": t("384 is the area. A banner goes around: perimeter.", "384 es el área. Una cinta va alrededor: perímetro."), "d": t("64 is 4 × 16. The room has two lengths of 24.", "64 es 4 × 16. El salón tiene dos largos de 24.")}, "solution": t("P = 2 × 24 + 2 × 16 = 80 feet.", "P = 2 × 24 + 2 × 16 = 80 pies.")},
      "D": {"ok": "d", "hints": {"a": t("Count up: 4:30 → 5:00 is 30 minutes, then 3 whole hours to 8:00.", "Cuente hacia adelante: 4:30 → 5:00 son 30 minutos, y después 3 horas completas hasta las 8:00."), "b": t("85 minutes is more than an hour. Do not subtract times like decimals.", "85 minutos es más de una hora. No reste las horas como decimales."), "c": t("5:00 to 8:00 is 3 hours, and there are 30 + 15 = 45 minutes more.", "De 5:00 a 8:00 son 3 horas, y hay 30 + 15 = 45 minutos más.")}, "solution": t("30 min + 3 h + 15 min = 3 h 45 min.", "30 min + 3 h + 15 min = 3 h 45 min.")},
      "E": {"ok": "a", "hints": {"b": t("Check the subtraction: 500.00 − 455.75. Line up the decimal points.", "Revise la resta: 500.00 − 455.75. Alinee los puntos decimales."), "c": t("$955.75 adds. \"Left\" means subtract.", "$955.75 suma. «Lo que queda» quiere decir restar."), "d": t("Check the cents: 100 − 75 = 25 cents.", "Revise los centavos: 100 − 75 = 25 centavos.")}, "solution": t("$500.00 − $455.75 = $44.25.", "$500.00 − $455.75 = $44.25.")},
      "F": {"ok": "b", "hints": {"a": t("24 uses only 1 gallon... check: 3 gallons = 384 fl oz.", "24 no alcanza: 3 galones = 384 onzas líquidas."), "c": t("384 is the fluid ounces, not the cups. Divide by 8.", "384 son las onzas líquidas, no los vasos. Divida entre 8."), "d": t("96 divides by 4. Each cup holds 8 fluid ounces.", "96 divide entre 4. A cada vaso le caben 8 onzas líquidas.")}, "solution": t("3 × 128 = 384 fl oz, and 384 ÷ 8 = 48 cups.", "3 × 128 = 384 onzas líquidas, y 384 ÷ 8 = 48 vasos.")},
      "G": {"ok": "c", "hints": {"a": t("$440 subtracts. Share the total: divide.", "$440 resta. Reparta el total: divida."), "b": t("$480 adds. Divide the total by 20.", "$480 suma. Divida el total entre 20."), "d": t("$9,200 multiplies. Divide.", "$9,200 multiplica. Divida.")}, "solution": t("$460 ÷ 20 = $23 per guest.", "$460 ÷ 20 = $23 por invitado.")},
      "H": {"ok": "d", "hints": {"a": t("A line graph shows change over time. The categories are kinds of expenses.", "Una gráfica de líneas muestra un cambio con el tiempo. Las categorías son tipos de gastos."), "b": t("One number cannot show 5 categories.", "Un solo número no puede mostrar 5 categorías."), "c": t("Dates show time, not categories.", "Las fechas muestran tiempo, no categorías.")}, "solution": t("To compare categories, use a bar graph.", "Para comparar categorías, use una gráfica de barras.")}
     }}

    quiz = [
     ("A", t("Each plate costs <strong>$8.50</strong>. How much for <strong>20 guests</strong>?", "Cada plato cuesta <strong>$8.50</strong>. ¿Cuánto cuesta para <strong>20 invitados</strong>?"), [("a", "$170"), ("b", "$28.50"), ("c", "$1,700"), ("d", "$160")]),
     ("B", t("Food can use <strong>2/5</strong> of a <strong>$500</strong> budget. How much is that?", "La comida puede usar <strong>2/5</strong> de un presupuesto de <strong>$500</strong>. ¿Cuánto es eso?"), [("a", "$250"), ("b", "$200"), ("c", "$100"), ("d", "$2.50")]),
     ("C", t("A banner goes around a room <strong>24 ft by 16 ft</strong>. How many feet of banner do you need?", "Una cinta le da la vuelta a un salón de <strong>24 pies por 16 pies</strong>. ¿Cuántos pies de cinta necesita?"), [("a", "40"), ("b", "384"), ("c", "80"), ("d", "64")]),
     ("D", t("The party goes from <strong>4:30 p.m.</strong> to <strong>8:15 p.m.</strong> How long is it?", "La fiesta va de <strong>4:30 p.m.</strong> a <strong>8:15 p.m.</strong> ¿Cuánto dura?"), [("a", "4 h 45 min"), ("b", "3 h 85 min"), ("c", "4 h 15 min"), ("d", "3 h 45 min")]),
     ("E", t("The plan costs <strong>$455.75</strong>. The budget is <strong>$500</strong>. How much is left?", "El plan cuesta <strong>$455.75</strong>. El presupuesto es de <strong>$500</strong>. ¿Cuánto queda?"), [("a", "$44.25"), ("b", "$55.25"), ("c", "$955.75"), ("d", "$45.75")]),
     ("F", t("<strong>3 gallons</strong> of juice are served in <strong>8-fluid-ounce</strong> cups. How many cups can you fill? (1 gal = 128 fl oz.)", "Se sirven <strong>3 galones</strong> de jugo en vasos de <strong>8 onzas líquidas</strong>. ¿Cuántos vasos se pueden llenar? (1 galón = 128 onzas líquidas)."), [("a", "24"), ("b", "48"), ("c", "384"), ("d", "96")]),
     ("G", t("A party cost <strong>$460</strong> for <strong>20 guests</strong>. What is the mean cost per guest?", "Una fiesta costó <strong>$460</strong> para <strong>20 invitados</strong>. ¿Cuál es el costo medio por invitado?"), [("a", "$440"), ("b", "$480"), ("c", "$23"), ("d", "$9,200")]),
     ("H", t("What is the best way to show how the money was spent in <strong>5 categories</strong>?", "¿Cuál es la mejor forma de mostrar cómo se gastó el dinero en <strong>5 categorías</strong>?"), [("a", t("a line graph", "una gráfica de líneas")), ("b", t("a single number", "un solo número")), ("c", t("a list of dates", "una lista de fechas")), ("d", t("a bar graph", "una gráfica de barras"))])]

    return B.pagina_leccion(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"),
        t("Final project", "Proyecto final"),
        t("Plan a celebration for 20 guests with $500, and use everything you learned in Level 1.", "Planee una celebración para 20 invitados con $500, y use todo lo que aprendió en el Nivel 1."),
        ("🎉", t("All of Level 1 together", "Todo el Nivel 1 junto")),
        [t("<strong>Plan</strong> a real project with a budget, step by step.", "<strong>Planear</strong> un proyecto real con un presupuesto, paso a paso."),
         t("<strong>Use</strong> whole numbers, decimals, and fractions to find costs and parts of the budget.", "<strong>Usar</strong> números enteros, decimales y fracciones para hallar costos y partes del presupuesto."),
         t("<strong>Use</strong> measures, perimeter, area, and time to plan the space and the schedule.", "<strong>Usar</strong> medidas, perímetro, área y tiempo para planear el espacio y el horario."),
         t("<strong>Present</strong> the plan with a table, a bar graph, and a summary.", "<strong>Presentar</strong> el plan con una tabla, una gráfica de barras y un resumen.")],
        secciones,
        (t("Make your own plan: a celebration, a trip, or a home project (painting a room, a garden). Choose a budget. Make an expense table with at least 5 items, check that it fits the budget, find one perimeter or area and one elapsed time, make a bar graph of the costs, and write a summary of 3 or 4 sentences.",
           "Haga su propio plan: una celebración, un viaje o un proyecto en la casa (pintar un cuarto, un jardín). Elija un presupuesto. Haga una tabla de gastos con por lo menos 5 cosas, compruebe que alcanza el dinero, halle un perímetro o un área y un tiempo transcurrido, haga una gráfica de barras de los costos y escriba un resumen de 3 o 4 oraciones."),
         t("Present your plan to a family member or a classmate. Explain one decision you made with the numbers, and ask them to check one of your calculations.",
           "Presente su plan a alguien de su familia o a un compañero. Explique una decisión que tomó con los números, y pídale que revise uno de sus cálculos.")),
        quiz,
        t("Self-check checklist for the final project", "Lista de autoevaluación del proyecto final"),
        t("Self-check checklist: the parts of the final project", "Lista de autoevaluación: las partes del proyecto final"),
        [(t("Costs and budget", "Costos y presupuesto"), t("Every cost is correct, with cents, and I checked that the total fits the budget.", "Cada costo es correcto, con centavos, y comprobé que el total cabe en el presupuesto."), t("Most costs are correct.", "La mayoría de los costos son correctos."), t("I did not check the total against the budget.", "No comparé el total con el presupuesto.")),
         (t("Measures and time", "Medidas y tiempo"), t("I used perimeter, area, units, and elapsed time correctly, with their units.", "Usé bien el perímetro, el área, las unidades y el tiempo transcurrido, con sus unidades."), t("I used some of them correctly.", "Usé bien algunos."), t("I mixed up perimeter and area or forgot the units.", "Confundí perímetro y área, u olvidé las unidades.")),
         (t("Table and graph", "Tabla y gráfica"), t("My table and my bar graph have titles, labels, and a good scale.", "Mi tabla y mi gráfica de barras tienen título, rótulos y una buena escala."), t("They are missing a title or a label.", "Les falta un título o un rótulo."), t("I did not make a table or a graph.", "No hice una tabla o una gráfica.")),
         (t("Summary and decisions", "Resumen y decisiones"), t("My summary explains the total, the money left, and a decision based on the numbers.", "Mi resumen explica el total, el dinero que sobra y una decisión basada en los números."), t("My summary gives the numbers but no decision.", "Mi resumen da los números, pero ninguna decisión."), t("I did not write a summary.", "No escribí un resumen."))],
        t("<p><strong>You have finished Level 1.</strong> You can now work with whole numbers, decimals, and fractions, think algebraically, measure, find perimeter and area, and read tables and graphs. That is the foundation of the GED® Mathematical Reasoning test.</p>\n<p>Go back to any lesson whenever you need it: the practice pages change every time. Level 2 will build on everything you learned here.</p>",
          "<p><strong>Terminó el Nivel 1.</strong> Ya sabe trabajar con números enteros, decimales y fracciones, pensar de forma algebraica, medir, hallar el perímetro y el área, y leer tablas y gráficas. Esa es la base del examen de Razonamiento Matemático del GED®.</p>\n<p>Vuelva a cualquier lección cuando lo necesite: las páginas de práctica cambian cada vez. El Nivel 2 se construirá sobre todo lo que aprendió aquí.</p>"),
        (None, ("", t("Level 2 (coming soon)", "Nivel 2 (próximamente)"))),
        [(t("budget", "presupuesto"), t("The amount of money you can spend on something.", "La cantidad de dinero que se puede gastar en algo.")),
         (t("expense", "gasto"), t("Money that you spend.", "Dinero que se gasta.")),
         (t("estimate", "estimar"), t("To find an answer that is close, to check if a calculation makes sense.", "Hallar una respuesta cercana, para comprobar si un cálculo tiene sentido.")),
         (t("summary", "resumen"), t("A few sentences that tell the most important results.", "Unas pocas oraciones que dicen los resultados más importantes."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "cosas": [["plates of food", 6, 12], ["balloons", 1, 3], ["tablecloths", 4, 9], ["chairs (rent)", 2, 5], ["pizzas", 9, 16], ["gift bags", 2, 6]],
  "pregCosto": "You buy <strong>{n} {c}</strong> at <strong>${p}</strong> each. How many dollars do they cost?",
  "solCosto": "{n} × ${p} = $<strong>{r}</strong>.",
  "sumaCosto": "You added. Each one costs the same: multiply.",
  "centavos": "Check the cents: line up the decimal point.",
  "pregQueda": "Your budget is <strong>${b}</strong>. You have spent <strong>${g}</strong>. How many dollars are left?",
  "solQueda": "${b} − ${g} = $<strong>{r}</strong>.",
  "sumaQueda": "You added. \"Left\" means subtract.",
  "pregFrac": "<strong>{f}</strong> of a <strong>${b}</strong> budget is for {c}. How many dollars is that?",
  "usos": ["food", "decorations", "music", "drinks"],
  "solFrac": "${b} ÷ {d} = ${u}, and {n} × ${u} = $<strong>{r}</strong>.",
  "soloUno": "That is only 1/{d}. Multiply by {n}.",
  "pistaDinero": "Multiply for equal items, subtract for what is left, and divide by the denominator for a fraction.",
  "invalido": "Type a number. You can use a decimal point, like 37.50.",
  "pregPer": "{e} for <strong>{n} people</strong> cost <strong>${tot}</strong>. What is the mean cost per person, in dollars?",
  "eventos": ["A party", "A trip", "A dinner", "A picnic"],
  "solPer": "${tot} ÷ {n} = $<strong>{r}</strong> per person.",
  "perMult": "You multiplied. The cost is shared: divide.",
  "perResta": "Divide the total by the number of people.",
  "pistaPer": "Mean per person = total ÷ number of people.",
  "tareas": [["the length of ribbon to go around a table", "per"], ["how much carpet covers a floor", "area"], ["how long a party lasts, from start to end", "tiempo"], ["how many cups are in 2 gallons", "conv"], ["the typical amount each family spent", "media"], ["the fence around a garden", "per"], ["the paint for a wall", "area"], ["the hours between the start and the end of a shift", "tiempo"], ["how many inches are in 6 feet", "conv"], ["the average score of 5 tests", "media"]],
  "herr": {"per": "perimeter (add the sides)", "area": "area (length × width)", "tiempo": "elapsed time (count up)", "conv": "unit conversion (multiply or divide)", "media": "mean (add and divide)"},
  "pregTarea": "You need to find <strong>{x}</strong>. Which tool do you need?",
  "bienTarea": "For {x}, use <strong>{h}</strong>.",
  "pistaTarea": "Around → perimeter. Covering → area. From one time to another → elapsed time. Changing units → conversion. Typical value → mean."
 },
 "es": {
  "cosas": [["platos de comida", 6, 12], ["globos", 1, 3], ["manteles", 4, 9], ["sillas (alquiler)", 2, 5], ["pizzas", 9, 16], ["bolsitas de regalo", 2, 6]],
  "pregCosto": "Usted compra <strong>{n} {c}</strong> a <strong>${p}</strong> por unidad. ¿Cuántos dólares cuestan?",
  "solCosto": "{n} × ${p} = $<strong>{r}</strong>.",
  "sumaCosto": "Sumó. Cada uno cuesta lo mismo: multiplique.",
  "centavos": "Revise los centavos: alinee el punto decimal.",
  "pregQueda": "Su presupuesto es de <strong>${b}</strong>. Ha gastado <strong>${g}</strong>. ¿Cuántos dólares quedan?",
  "solQueda": "${b} − ${g} = $<strong>{r}</strong>.",
  "sumaQueda": "Sumó. «Lo que queda» quiere decir restar.",
  "pregFrac": "<strong>{f}</strong> de un presupuesto de <strong>${b}</strong> es para {c}. ¿Cuántos dólares son?",
  "usos": ["la comida", "la decoración", "la música", "las bebidas"],
  "solFrac": "${b} ÷ {d} = ${u}, y {n} × ${u} = $<strong>{r}</strong>.",
  "soloUno": "Eso es solo 1/{d}. Multiplique por {n}.",
  "pistaDinero": "Multiplique para cosas iguales, reste para lo que queda, y divida entre el denominador para una fracción.",
  "invalido": "Escriba un número. Puede usar el punto decimal, como en 37.50.",
  "pregPer": "{e} para <strong>{n} personas</strong> costó <strong>${tot}</strong>. ¿Cuál es el costo medio por persona, en dólares?",
  "eventos": ["Una fiesta", "Un viaje", "Una cena", "Un pícnic"],
  "solPer": "${tot} ÷ {n} = $<strong>{r}</strong> por persona.",
  "perMult": "Multiplicó. El costo se reparte: divida.",
  "perResta": "Divida el total entre la cantidad de personas.",
  "pistaPer": "Media por persona = total ÷ cantidad de personas.",
  "tareas": [["el largo de cinta para darle la vuelta a una mesa", "per"], ["cuánta alfombra cubre un piso", "area"], ["cuánto dura una fiesta, del inicio al final", "tiempo"], ["cuántas tazas hay en 2 galones", "conv"], ["la cantidad típica que gastó cada familia", "media"], ["la cerca alrededor de un jardín", "per"], ["la pintura para una pared", "area"], ["las horas entre el inicio y el final de un turno", "tiempo"], ["cuántas pulgadas hay en 6 pies", "conv"], ["el promedio de las notas de 5 pruebas", "media"]],
  "herr": {"per": "el perímetro (sumar los lados)", "area": "el área (largo × ancho)", "tiempo": "el tiempo transcurrido (contar hacia adelante)", "conv": "la conversión de unidades (multiplicar o dividir)", "media": "la media (sumar y dividir)"},
  "pregTarea": "Usted necesita hallar <strong>{x}</strong>. ¿Qué herramienta necesita?",
  "bienTarea": "Para {x}, use <strong>{h}</strong>.",
  "pistaTarea": "Alrededor → perímetro. Cubrir → área. De una hora a otra → tiempo transcurrido. Cambiar de unidad → conversión. Valor típico → media."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function din(x){ var c = Math.round(x * 100), e = Math.floor(c / 100), r = c % 100; return com(e) + (r ? "." + (r < 10 ? "0" : "") + r : ""); }
function numD(res, pistas, general){
  return function(t){
    var s = String(t).replace(/[\s,$]/g, "");
    if (!/^\d*\.?\d+$/.test(s)) return { estado: "invalido", msg: TXT.invalido };
    var v = parseFloat(s), cerca = function(a){ return Math.abs(v - a) < 0.005; };
    if (cerca(res)) return { estado: "bien" };
    for (var i = 0; i < pistas.length; i++) if (cerca(pistas[i].v)) return { estado: "mal", msg: pistas[i].msg };
    return { estado: "mal", msg: general };
  };
}

/* ============ MODULE 1 · costs and budget ============ */
function genDinero(){
  var r = Math.random(), p = [];
  if (r < 0.4){
    var c = elige(TXT.cosas), n = aleatorio(3, 20), pr = aleatorio(c[1] * 4, c[2] * 4) / 4, tot = Math.round(n * pr * 100) / 100;
    p.push({ v: n + pr, msg: TXT.sumaCosto });
    return { enun: F(TXT.pregCosto, { n: n, c: c[0], p: din(pr) }), solucion: F(TXT.solCosto, { n: n, p: din(pr), r: din(tot) }), evalua: numD(tot, p, TXT.pistaDinero) };
  }
  if (r < 0.7){
    var b = elige([300, 400, 500, 600, 750, 1000]), g = Math.round((b * aleatorio(40, 95) / 100 + aleatorio(0, 3) * 0.25) * 100) / 100, q = Math.round((b - g) * 100) / 100;
    p.push({ v: b + g, msg: TXT.sumaQueda }); p.push({ v: q + 1, msg: TXT.centavos }); p.push({ v: q - 1, msg: TXT.centavos });
    return { enun: F(TXT.pregQueda, { b: din(b), g: din(g) }), solucion: F(TXT.solQueda, { b: din(b), g: din(g), r: din(q) }), evalua: numD(q, p, TXT.pistaDinero) };
  }
  var d = elige([2, 4, 5, 10]), nn = aleatorio(1, d - 1), b2 = elige([200, 300, 400, 500, 600, 800, 1000]), u = b2 / d, res = u * nn;
  if (nn !== 1) p.push({ v: u, msg: F(TXT.soloUno, { d: d, n: nn }) });
  return { enun: F(TXT.pregFrac, { f: nn + "/" + d, b: din(b2), c: elige(TXT.usos) }), solucion: F(TXT.solFrac, { b: din(b2), d: d, u: din(u), n: nn, r: din(res) }), evalua: numD(res, p, TXT.pistaDinero) };
}

/* ============ MODULE 2 · choose the tool ============ */
function genHerr(){
  var x = elige(TXT.tareas), ks = ["per", "area", "tiempo", "conv", "media"], pistas = {};
  ks.forEach(function(k){ if (k !== x[1]) pistas[k] = TXT.pistaTarea; });
  var txt = F(TXT.bienTarea, { x: x[0], h: TXT.herr[x[1]] });
  return { enOrden: true, enun: F(TXT.pregTarea, { x: x[0] }), opciones: ks.map(function(k){ return { html: TXT.herr[k], clave: k }; }), correcta: x[1], pistas: pistas, pista: TXT.pistaTarea, bien: txt, mal: txt };
}

/* ============ MODULE 3 · cost per person ============ */
function genPer(){
  var n = aleatorio(4, 25), m = aleatorio(40, 160) / 4, tot = Math.round(n * m * 100) / 100, p = [];
  p.push({ v: tot * n, msg: TXT.perMult }); p.push({ v: tot - n, msg: TXT.perResta });
  return { enun: F(TXT.pregPer, { e: elige(TXT.eventos), n: n, tot: din(tot) }), solucion: F(TXT.solPer, { tot: din(tot), n: n, r: din(m) }), evalua: numD(m, p, TXT.pistaPer) };
}

/* ============ MODULE 4 · mixed review ============ */
function genRepaso(){
  var g = elige([genDinero, genPer, genDinero, genPer]);
  return g();
}

creaPracticaLibre("p1", genDinero);
creaPracticaOM("p2", genHerr);
creaPracticaLibre("p3", genPer);
creaPracticaLibre("p4", genRepaso);
'''

def practica_pagina():
    n = N
    mods = [
     (t("budget", "presupuesto"), t("Costs and budget", "Costos y presupuesto"),
      f'''      <p>{t("<strong>Equal items:</strong> multiply the number by the price. <strong>Money left:</strong> subtract what you spent from the budget. <strong>A fraction of the budget:</strong> divide by the denominator and multiply by the numerator.", "<strong>Cosas iguales:</strong> multiplique la cantidad por el precio. <strong>Lo que queda:</strong> reste lo gastado del presupuesto. <strong>Una fracción del presupuesto:</strong> divida entre el denominador y multiplique por el numerador.")}</p>
{B.libre("p1", t("Practice: the money", "Practique: el dinero"), t("Dollars", "Dólares"), nota=False)}
      <p class="nota">{t("Type only the number. You can use a decimal point, like 37.50.", "Escriba solo el número. Puede usar el punto decimal, como en 37.50.")}</p>'''),
     (t("choose-tool", "elegir-herramienta"), t("Choose the right tool", "Elegir la herramienta correcta"),
      f'''      <p>{t("A real project needs many tools. Before you calculate, decide which one the question needs.", "Un proyecto real necesita muchas herramientas. Antes de calcular, decida cuál necesita la pregunta.")}</p>
{B.om("p2", t("Practice: which tool?", "Practique: ¿qué herramienta?"))}'''),
     (t("per-person", "por-persona"), t("Cost per person", "Costo por persona"),
      f'''      <p>{t("The mean cost per person is the total divided by the number of people.", "El costo medio por persona es el total dividido entre la cantidad de personas.")}</p>
{B.libre("p3", t("Practice: share the cost", "Practique: repartir el costo"), t("Dollars", "Dólares"), nota=False)}
      <p class="nota">{t("Type only the number. You can use a decimal point, like 12.75.", "Escriba solo el número. Puede usar el punto decimal, como en 12.75.")}</p>'''),
     (t("review", "repaso"), t("Mixed review", "Repaso mixto"),
      f'''      <p>{t("A mix of money problems from the project. Read each one carefully: multiply, subtract, use a fraction, or divide?", "Una mezcla de problemas de dinero del proyecto. Lea cada uno con cuidado: ¿multiplicar, restar, usar una fracción o dividir?")}</p>
{B.libre("p4", t("Practice: mixed problems", "Practique: problemas mezclados"), t("Dollars", "Dólares"), nota=False)}
      <p class="nota">{t("Type only the number. You can use a decimal point.", "Escriba solo el número. Puede usar el punto decimal.")}</p>''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t("Tables, graphs, and final project", "Tablas, gráficas y proyecto final"), t("Final project", "Proyecto final"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Proyecto final")
