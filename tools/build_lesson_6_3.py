"""Lesson 6.3 · Applied measurement problems — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "6-3"

def tabla_madera():
    """A 96-inch board cut into 18-inch pieces, with a 6-inch leftover."""
    x0, w = 30, 580
    s = []
    for i in range(5):
        x = x0 + w * 18 * i / 96
        s.append(f'<rect x="{x:.1f}" y="30" width="{w * 18 / 96:.1f}" height="50" fill="#d7a86e" stroke="#5d4037" stroke-width="2"/><text x="{x + w * 9 / 96:.1f}" y="62" text-anchor="middle" font-size="17" font-weight="700" fill="#3e2723">18 in</text>')
    x = x0 + w * 90 / 96
    s.append(f'<rect x="{x:.1f}" y="30" width="{w * 6 / 96:.1f}" height="50" fill="#eeeeee" stroke="#5d4037" stroke-width="2" stroke-dasharray="5 4"/><text x="{x + w * 3 / 96:.1f}" y="62" text-anchor="middle" font-size="14" font-weight="700" fill="#5d4037">6</text>')
    s.append(f'<text x="{x0 + w / 2}" y="112" text-anchor="middle" font-size="17" font-weight="700" fill="#0d47a1">{t("8 ft = 96 in", "8 pies = 96 pulgadas")}</text>')
    return svg("0 0 640 130", t("A board 96 inches long cut into 5 pieces of 18 inches each. A piece of 6 inches is left over, too short to use.",
                                "Una tabla de 96 pulgadas cortada en 5 pedazos de 18 pulgadas cada uno. Sobra un pedazo de 6 pulgadas, demasiado corto para usarlo."), "".join(s))

def leccion():
    n = N
    s1 = f'''<p>{t("In real life, measurement problems rarely take a single step. A recipe has to be doubled, a board has to be cut, a shift has a break that is not paid. In this lesson you will put together everything from Topic 6 and solve problems with <strong>two or more steps</strong>.",
"En la vida real, los problemas de medición casi nunca son de un solo paso. Hay que duplicar una receta, cortar una tabla, o descontar un descanso que no se paga. En esta lección va a juntar todo el Tema 6 y resolver problemas de <strong>dos o más pasos</strong>.")}</p>
{caja("tip", t("The 4 steps for measurement problems", "Los 4 pasos para problemas de medición"), t("""<p class="paso"><span aria-hidden="true" class="n">1</span><strong>What do they ask, and in what unit?</strong> Underline the question and the unit of the answer.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Put everything in the same unit.</strong> Convert before you calculate.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Calculate</strong>, one step at a time.</p>
<p class="paso"><span aria-hidden="true" class="n">4</span><strong>Check:</strong> does the answer make sense, and does it have the unit they asked for?</p>""",
"""<p class="paso"><span aria-hidden="true" class="n">1</span><strong>¿Qué preguntan y en qué unidad?</strong> Subraye la pregunta y la unidad de la respuesta.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Ponga todo en la misma unidad.</strong> Convierta antes de calcular.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Calcule</strong>, un paso a la vez.</p>
<p class="paso"><span aria-hidden="true" class="n">4</span><strong>Compruebe:</strong> ¿la respuesta tiene sentido, y lleva la unidad que le pidieron?</p>"""))}'''

    s2 = f'''<p>{t("The most common trap in measurement problems is to calculate with two different units. <strong>Convert first.</strong>", "La trampa más común en los problemas de medición es calcular con dos unidades distintas. <strong>Convierta primero.</strong>")}</p>
{ejemplo(t("Example: a board is 8 feet long. How many 18-inch pieces can you cut from it?", "Ejemplo: una tabla mide 8 pies. ¿Cuántos pedazos de 18 pulgadas se pueden cortar de ella?"),
  [("1", t("Same unit.", "La misma unidad."), t("8 feet = 8 × 12 = 96 inches.", "8 pies = 8 × 12 = 96 pulgadas.")),
   ("2", t("Divide.", "Divida."), t("96 ÷ 18 = 5, remainder 6.", "96 ÷ 18 = 5, residuo 6.")),
   ("✓", t("Interpret the remainder.", "Interprete el residuo."), t("The 6 inches left over are not enough for another piece. You can cut <strong>5 pieces</strong>.", "Las 6 pulgadas que sobran no alcanzan para otro pedazo. Se pueden cortar <strong>5 pedazos</strong>."))])}
{tabla_madera()}
{ejemplo(t("Example: a recipe uses 2 cups of milk. You will make it 6 times. How many quarts of milk do you need?", "Ejemplo: una receta lleva 2 tazas de leche. Usted la va a hacer 6 veces. ¿Cuántos cuartos de leche necesita?"),
  [("1", t("Total in cups.", "El total en tazas."), t("6 × 2 = 12 cups.", "6 × 2 = 12 tazas.")),
   ("2", t("Convert to quarts.", "Convierta a cuartos."), t("1 quart = 4 cups, so 12 ÷ 4 = 3.", "1 cuarto = 4 tazas, así que 12 ÷ 4 = 3.")),
   ("✓", t("Answer.", "Respuesta."), t("You need <strong>3 quarts</strong> of milk.", "Necesita <strong>3 cuartos</strong> de leche."))])}
{caja("ojo", t("Watch out! The remainder", "¡Cuidado! El residuo"), t("<p>When you cut or fill things, a remainder usually means \"not enough for one more.\" But if you must <strong>buy</strong> enough, a remainder means you need <strong>one more</strong>: to carry 50 people in vans of 12, you need 5 vans, not 4.</p>",
"<p>Cuando se corta o se llena algo, un residuo casi siempre quiere decir «no alcanza para uno más». Pero si hay que <strong>comprar</strong> lo suficiente, un residuo quiere decir que se necesita <strong>uno más</strong>: para llevar a 50 personas en camionetas de 12, se necesitan 5 camionetas, no 4.</p>"))}
{practica("p1", t("Practice 1 — Cut a ribbon", "Práctica 1 — Cortar una cinta"), t("A ribbon is <strong>4 yards</strong> long. How many pieces of <strong>9 inches</strong> can you cut from it?", "Una cinta mide <strong>4 yardas</strong>. ¿Cuántos pedazos de <strong>9 pulgadas</strong> se pueden cortar de ella?"),
          [("a", "36"), ("b", "16"), ("c", "48"), ("d", "1,296")])}
{practica("p2", t("Practice 2 — Glasses of lemonade", "Práctica 2 — Vasos de limonada"), t("You make <strong>2 gallons</strong> of lemonade. Each glass holds <strong>8 fluid ounces</strong>. How many glasses can you fill? (1 gallon = 128 fluid ounces.)", "Usted prepara <strong>2 galones</strong> de limonada. A cada vaso le caben <strong>8 onzas líquidas</strong>. ¿Cuántos vasos puede llenar? (1 galón = 128 onzas líquidas).") ,
          [("a", "32"), ("b", "16"), ("c", "64"), ("d", "8")])}
{enlace(n, t("same-unit", "misma-unidad"), t("same unit first", "primero la misma unidad"), t("Convert, then divide, and decide what to do with the remainder.", "Convierta, después divida, y decida qué hacer con el residuo."))}'''

    s3 = f'''<p>{t("Many everyday problems mix <strong>time</strong> with money or distance: how much you earn in a shift, or how long a trip takes.", "Muchos problemas de todos los días mezclan el <strong>tiempo</strong> con el dinero o la distancia: cuánto gana en un turno, o cuánto dura un viaje.")}</p>
{ejemplo(t("Example: Ana works from 8:30 a.m. to 4:00 p.m. Her 30-minute lunch is not paid. She earns $16 per hour. How much does she earn that day?", "Ejemplo: Ana trabaja de 8:30 a.m. a 4:00 p.m. Su almuerzo de 30 minutos no se paga. Gana $16 por hora. ¿Cuánto gana ese día?"),
  [("1", t("Elapsed time.", "Tiempo transcurrido."), t("8:30 → 9:00 is 30 min, 9:00 → 4:00 is 7 h: in total 7 h 30 min.", "8:30 → 9:00 son 30 min, 9:00 → 4:00 son 7 h: en total 7 h 30 min.")),
   ("2", t("Take away the break.", "Quite el descanso."), t("7 h 30 min − 30 min = 7 paid hours.", "7 h 30 min − 30 min = 7 horas pagadas.")),
   ("3", t("Multiply by the pay per hour.", "Multiplique por el pago por hora."), "7 × $16 = $112."),
   ("✓", t("Answer.", "Respuesta."), t("Ana earns <strong>$112</strong> that day.", "Ana gana <strong>$112</strong> ese día."))])}
<p>{t("A <strong>speed</strong> like 45 miles per hour is a <strong>rate</strong>: it says how many miles for each hour. Distance = speed × time.", "Una <strong>velocidad</strong> como 45 millas por hora es una <strong>tasa</strong>: dice cuántas millas por cada hora. Distancia = velocidad × tiempo.")}</p>
{ejemplo(t("Example: a bus travels 45 miles each hour. How long does it take to travel 180 miles?", "Ejemplo: un autobús recorre 45 millas cada hora. ¿Cuánto tarda en recorrer 180 millas?"),
  [("1", t("Equal groups of 45 miles.", "Grupos iguales de 45 millas."), t("How many groups of 45 fit in 180? Divide: 180 ÷ 45 = 4.", "¿Cuántos grupos de 45 caben en 180? Divida: 180 ÷ 45 = 4.")),
   ("✓", t("Check and answer.", "Compruebe y responda."), t("4 × 45 = 180 ✓. The trip takes <strong>4 hours</strong>.", "4 × 45 = 180 ✓. El viaje dura <strong>4 horas</strong>."))])}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>Ana's pay: type {T("7")} {T("×")} {T("1")}{T("6")} {T("enter")}. The screen shows 112.</p>
<p>The bus: type {T("1")}{T("8")}{T("0")} {T("÷")} {T("4")}{T("5")} {T("enter")}. The screen shows 4.</p>""",
f"""<p>El pago de Ana: escriba {T("7")} {T("×")} {T("1")}{T("6")} {T("enter")}. La pantalla muestra 112.</p>
<p>El autobús: escriba {T("1")}{T("8")}{T("0")} {T("÷")} {T("4")}{T("5")} {T("enter")}. La pantalla muestra 4.</p>"""))}
{practica("p3", t("Practice 3 — A day of work", "Práctica 3 — Un día de trabajo"), t("Rosa works from <strong>9:00 a.m.</strong> to <strong>5:30 p.m.</strong> Her <strong>30-minute</strong> lunch is not paid. She earns <strong>$14 per hour</strong>. How much does she earn that day?", "Rosa trabaja de <strong>9:00 a.m.</strong> a <strong>5:30 p.m.</strong> Su almuerzo de <strong>30 minutos</strong> no se paga. Gana <strong>$14 por hora</strong>. ¿Cuánto gana ese día?"),
          [("a", "$119"), ("b", "$126"), ("c", "$112"), ("d", "$98")])}
{enlace(n, t("work-pay", "pago"), t("time and pay", "tiempo y pago"), t("Find the paid hours of a shift and the pay for the day.", "Halle las horas pagadas de un turno y el pago del día."))}
{enlace(n, t("speed", "velocidad"), t("distance, speed, and time", "distancia, velocidad y tiempo"), t("Use miles per hour to find a distance or a time.", "Use millas por hora para hallar una distancia o un tiempo."))}'''

    s4 = f'''<p>{t("Sometimes you add or subtract measures written with <strong>two units</strong>, like 2 ft 9 in. Add each unit by itself, and then <strong>regroup</strong>, as you carry in addition. The difference: you regroup at 12 inches, 16 ounces, or 60 minutes, <strong>not at 10</strong>.",
"A veces se suman o se restan medidas escritas con <strong>dos unidades</strong>, como 2 pies 9 pulgadas. Sume cada unidad por separado, y después <strong>reagrupe</strong>, como cuando lleva en una suma. La diferencia: se reagrupa a las 12 pulgadas, a las 16 onzas o a los 60 minutos, <strong>no a las 10</strong>.")}</p>
{ejemplo(t("Example: 2 ft 9 in + 1 ft 8 in", "Ejemplo: 2 pies 9 pulgadas + 1 pie 8 pulgadas"),
  [("1", t("Add each unit.", "Sume cada unidad."), t("2 + 1 = 3 ft and 9 + 8 = 17 in: 3 ft 17 in.", "2 + 1 = 3 pies y 9 + 8 = 17 pulgadas: 3 pies 17 pulgadas.")),
   ("2", t("Regroup.", "Reagrupe."), t("17 in = 1 ft 5 in (because 12 in = 1 ft).", "17 pulgadas = 1 pie 5 pulgadas (porque 12 pulgadas = 1 pie).")),
   ("✓", t("Answer.", "Respuesta."), t("3 ft + 1 ft 5 in = <strong>4 ft 5 in</strong>.", "3 pies + 1 pie 5 pulgadas = <strong>4 pies 5 pulgadas</strong>."))])}
{ejemplo(t("Example: 5 h 15 min − 2 h 40 min", "Ejemplo: 5 h 15 min − 2 h 40 min"),
  [("1", t("Not enough minutes.", "No alcanzan los minutos."), t("15 min − 40 min cannot be done. Borrow 1 hour = 60 minutes: 5 h 15 min = 4 h 75 min.", "15 min − 40 min no se puede. Pida prestada 1 hora = 60 minutos: 5 h 15 min = 4 h 75 min.")),
   ("2", t("Subtract each unit.", "Reste cada unidad."), t("4 − 2 = 2 h and 75 − 40 = 35 min.", "4 − 2 = 2 h y 75 − 40 = 35 min.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>2 h 35 min</strong>.")])}
{caja("ojo", t("The most common mistake", "El error más común"), t("<p>Regrouping at 10, as with whole numbers. 17 inches is not \"1 ft 7 in\": a foot has 12 inches, so 17 in = 1 ft 5 in.</p>",
"<p>Reagrupar a las 10, como con los números enteros. 17 pulgadas no son «1 pie 7 pulgadas»: un pie tiene 12 pulgadas, así que 17 pulgadas = 1 pie 5 pulgadas.</p>"))}
{practica("p4", t("Practice 4 — Add with regrouping", "Práctica 4 — Sumar reagrupando"), t("<strong>3 lb 10 oz + 2 lb 9 oz</strong> = ?", "<strong>3 libras 10 onzas + 2 libras 9 onzas</strong> = ?"),
          [("a", t("6 lb 9 oz", "6 libras 9 onzas")), ("b", t("5 lb 3 oz", "5 libras 3 onzas")), ("c", t("6 lb 19 oz", "6 libras 19 onzas")), ("d", t("6 lb 3 oz", "6 libras 3 onzas"))])}
{enlace(n, t("regroup", "reagrupar"), t("add and subtract with two units", "sumar y restar con dos unidades"), t("Regroup at 12 inches, 16 ounces, or 60 minutes.", "Reagrupe a las 12 pulgadas, a las 16 onzas o a los 60 minutos."))}'''

    secciones = [("s-" + t("steps", "pasos"), t("Problems with several steps", "Problemas de varios pasos"), s1),
                 ("s-" + t("same-unit", "misma-unidad"), t("First, the same unit", "Primero, la misma unidad"), s2),
                 ("s-" + t("time-money", "tiempo-dinero"), t("Time, money, and speed", "Tiempo, dinero y velocidad"), s3),
                 ("s-" + t("regroup", "reagrupar"), t("Add and subtract with two units", "Sumar y restar con dos unidades"), s4)]

    lesson = {"next": t("Lesson 7.1", "Lección 7.1"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("36 is the inches in one yard. Find the inches in 4 yards first.", "36 son las pulgadas de una yarda. Halle primero las pulgadas de 4 yardas."),
                                   "c": t("48 is 4 × 12, as if a yard were 12 inches. 1 yard = 36 inches.", "48 es 4 × 12, como si una yarda fueran 12 pulgadas. 1 yarda = 36 pulgadas."),
                                   "d": t("1,296 multiplies 144 × 9. Each piece takes 9 inches: divide.", "1,296 multiplica 144 × 9. Cada pedazo usa 9 pulgadas: divida.")},
             "right": t("4 yd = 144 in, and 144 ÷ 9 = 16 pieces.", "4 yardas = 144 pulgadas, y 144 ÷ 9 = 16 pedazos."),
             "solution": t("Same unit first: 4 × 36 = 144 inches. Then 144 ÷ 9 = 16 pieces.", "Primero la misma unidad: 4 × 36 = 144 pulgadas. Después 144 ÷ 9 = 16 pedazos.")},
      "p2": {"ok": "a", "hints": {"b": t("16 is 128 ÷ 8, the glasses from just 1 gallon. You have 2 gallons.", "16 es 128 ÷ 8, los vasos de solo 1 galón. Usted tiene 2 galones."),
                                   "c": t("64 divides 256 by 4. Each glass holds 8 fluid ounces.", "64 divide 256 entre 4. A cada vaso le caben 8 onzas líquidas."),
                                   "d": t("8 is the size of one glass, not the number of glasses.", "8 es el tamaño de un vaso, no la cantidad de vasos.")},
             "right": t("2 gal = 256 fl oz, and 256 ÷ 8 = 32 glasses.", "2 galones = 256 onzas líquidas, y 256 ÷ 8 = 32 vasos."),
             "solution": t("Same unit first: 2 × 128 = 256 fluid ounces. Then 256 ÷ 8 = 32 glasses.", "Primero la misma unidad: 2 × 128 = 256 onzas líquidas. Después 256 ÷ 8 = 32 vasos.")},
      "p3": {"ok": "c", "hints": {"a": t("$119 pays 8.5 hours. The 30-minute lunch is not paid: take it away.", "$119 paga 8.5 horas. El almuerzo de 30 minutos no se paga: quítelo."),
                                   "b": t("$126 pays 9 hours. Count again: 9:00 to 5:30 is 8 h 30 min.", "$126 paga 9 horas. Cuente otra vez: de 9:00 a 5:30 son 8 h 30 min."),
                                   "d": t("$98 pays only 7 hours. 8 h 30 min − 30 min = 8 hours.", "$98 paga solo 7 horas. 8 h 30 min − 30 min = 8 horas.")},
             "right": t("8 h 30 min − 30 min = 8 h, and 8 × $14 = $112.", "8 h 30 min − 30 min = 8 h, y 8 × $14 = $112."),
             "solution": t("9:00 to 5:30 is 8 h 30 min. Without lunch: 8 paid hours. 8 × $14 = $112.", "De 9:00 a 5:30 son 8 h 30 min. Sin el almuerzo: 8 horas pagadas. 8 × $14 = $112.")},
      "p4": {"ok": "d", "hints": {"a": t("You regrouped at 10. A pound has 16 ounces: 19 oz = 1 lb 3 oz.", "Reagrupó a las 10. Una libra tiene 16 onzas: 19 onzas = 1 libra 3 onzas."),
                                   "b": t("You took away 16 ounces but did not add the 1 pound.", "Quitó 16 onzas, pero no sumó la 1 libra."),
                                   "c": t("19 ounces is more than a pound: regroup it.", "19 onzas es más de una libra: reagrúpelas.")},
             "right": t("5 lb 19 oz = 6 lb 3 oz.", "5 libras 19 onzas = 6 libras 3 onzas."),
             "solution": t("3 + 2 = 5 lb and 10 + 9 = 19 oz. 19 oz = 1 lb 3 oz, so the total is 6 lb 3 oz.", "3 + 2 = 5 libras y 10 + 9 = 19 onzas. 19 onzas = 1 libra 3 onzas, así que el total es 6 libras 3 onzas.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("6 pieces would need 6 × 18 = 108 inches, but the board is 96 inches.", "6 pedazos necesitan 6 × 18 = 108 pulgadas, pero la tabla mide 96 pulgadas."), "c": t("Convert the feet to inches first: 8 ft = 96 in.", "Convierta primero los pies a pulgadas: 8 pies = 96 pulgadas."), "d": t("96 ÷ 18 is more than 4: 4 × 18 is only 72.", "96 ÷ 18 es más que 4: 4 × 18 es solo 72.")},
            "solution": t("8 ft = 96 in. 96 ÷ 18 = 5, remainder 6. The 6 inches are not enough for another piece: 5 pieces.", "8 pies = 96 pulgadas. 96 ÷ 18 = 5, residuo 6. Las 6 pulgadas no alcanzan para otro pedazo: 5 pedazos.")},
      "B": {"ok": "b", "hints": {"a": t("12 is the cups. The question asks for quarts: 1 quart = 4 cups.", "12 son las tazas. La pregunta pide cuartos: 1 cuarto = 4 tazas."), "c": t("4 is the cups in one quart, not the answer.", "4 son las tazas de un cuarto, no la respuesta."), "d": t("8 is 2 + 6. First find the total cups: 6 × 2.", "8 es 2 + 6. Primero halle el total de tazas: 6 × 2.")},
            "solution": t("6 × 2 = 12 cups, and 12 ÷ 4 = 3 quarts.", "6 × 2 = 12 tazas, y 12 ÷ 4 = 3 cuartos.")},
      "C": {"ok": "c", "hints": {"a": t("8 h 30 min is the whole shift. Take away the 30-minute lunch.", "8 h 30 min es todo el turno. Quite el almuerzo de 30 minutos."), "b": t("8:00 to 4:30 is 8 h 30 min, not 9 hours.", "De 8:00 a 4:30 son 8 h 30 min, no 9 horas."), "d": t("You took away the lunch twice.", "Quitó el almuerzo dos veces.")},
            "solution": t("8:00 a.m. to 4:30 p.m. is 8 h 30 min. Minus 30 minutes of lunch: 8 paid hours.", "De 8:00 a.m. a 4:30 p.m. son 8 h 30 min. Menos 30 minutos de almuerzo: 8 horas pagadas.")},
      "D": {"ok": "d", "hints": {"a": t("$90 is one day: 6 × $15. He works 5 days.", "$90 es un solo día: 6 × $15. Trabaja 5 días."), "b": t("$26 adds the numbers. Multiply.", "$26 suma los números. Multiplique."), "c": t("$75 is 5 × $15, one hour each day. He works 6 hours a day.", "$75 es 5 × $15, una hora cada día. Trabaja 6 horas al día.")},
            "solution": t("6 × 5 = 30 hours, and 30 × $15 = $450.", "6 × 5 = 30 horas, y 30 × $15 = $450.")},
      "E": {"ok": "d", "hints": {"a": t("You regrouped at 10. A foot is 12 inches: 17 in = 1 ft 5 in.", "Reagrupó a las 10. Un pie son 12 pulgadas: 17 pulgadas = 1 pie 5 pulgadas."), "b": t("You took away 12 inches but did not add the 1 foot.", "Quitó 12 pulgadas, pero no sumó el pie."), "c": t("17 inches is more than a foot: regroup it.", "17 pulgadas es más de un pie: reagrúpelas.")},
            "solution": t("3 ft 17 in, and 17 in = 1 ft 5 in. Total: 4 ft 5 in.", "3 pies 17 pulgadas, y 17 pulgadas = 1 pie 5 pulgadas. Total: 4 pies 5 pulgadas.")},
      "F": {"ok": "b", "hints": {"a": t("You subtracted 10 − 4 the other way. Borrow 1 lb = 16 oz.", "Restó 10 − 4 al revés. Pida prestada 1 libra = 16 onzas."), "c": t("You borrowed 10. A pound has 16 ounces.", "Pidió prestado 10. Una libra tiene 16 onzas."), "d": t("After borrowing, the pounds go down by 1: 4 − 2 = 2.", "Después de pedir prestado, las libras bajan 1: 4 − 2 = 2.")},
            "solution": t("5 lb 4 oz = 4 lb 20 oz. 4 − 2 = 2 lb and 20 − 10 = 10 oz: 2 lb 10 oz.", "5 libras 4 onzas = 4 libras 20 onzas. 4 − 2 = 2 libras y 20 − 10 = 10 onzas: 2 libras 10 onzas.")},
      "G": {"ok": "a", "hints": {"b": t("135 is 180 − 45. How many groups of 45 fit in 180?", "135 es 180 − 45. ¿Cuántos grupos de 45 caben en 180?"), "c": t("8,100 multiplies. The miles are split into groups of 45: divide.", "8,100 multiplica. Las millas se reparten en grupos de 45: divida."), "d": t("225 adds. Divide 180 by 45.", "225 suma. Divida 180 entre 45.")},
            "solution": t("180 ÷ 45 = 4 hours. Check: 4 × 45 = 180.", "180 ÷ 45 = 4 horas. Comprobación: 4 × 45 = 180.")},
      "H": {"ok": "c", "hints": {"a": t("6,000 is the meters. The question asks for kilometers.", "6,000 son los metros. La pregunta pide kilómetros."), "b": t("1 km = 1,000 m, so divide by 1,000, not 100.", "1 km = 1,000 m, así que divida entre 1,000, no entre 100."), "d": t("0.6 divides by 10,000. 1 km = 1,000 m.", "0.6 divide entre 10,000. 1 km = 1,000 m.")},
            "solution": t("15 × 400 = 6,000 m, and 6,000 ÷ 1,000 = 6 km.", "15 × 400 = 6,000 m, y 6,000 ÷ 1,000 = 6 km.")}
     }}

    quiz = [
     ("A", t("A board is <strong>8 feet</strong> long. How many pieces of <strong>18 inches</strong> can you cut from it?", "Una tabla mide <strong>8 pies</strong>. ¿Cuántos pedazos de <strong>18 pulgadas</strong> se pueden cortar de ella?"), [("a", "5"), ("b", "6"), ("c", "2"), ("d", "4")]),
     ("B", t("A recipe uses <strong>2 cups</strong> of milk. You will make it <strong>6 times</strong>. How many quarts of milk do you need?", "Una receta lleva <strong>2 tazas</strong> de leche. La va a hacer <strong>6 veces</strong>. ¿Cuántos cuartos de leche necesita?"), [("a", "12"), ("b", "3"), ("c", "4"), ("d", "8")]),
     ("C", t("A shift goes from <strong>8:00 a.m.</strong> to <strong>4:30 p.m.</strong>, with a <strong>30-minute</strong> lunch that is not paid. How many hours are paid?", "Un turno va de <strong>8:00 a.m.</strong> a <strong>4:30 p.m.</strong>, con un almuerzo de <strong>30 minutos</strong> que no se paga. ¿Cuántas horas se pagan?"), [("a", "8 h 30 min"), ("b", "9 h"), ("c", "8 h"), ("d", "7 h 30 min")]),
     ("D", t("Luis earns <strong>$15 per hour</strong>. He works <strong>6 hours</strong> a day for <strong>5 days</strong>. How much does he earn?", "Luis gana <strong>$15 por hora</strong>. Trabaja <strong>6 horas</strong> al día durante <strong>5 días</strong>. ¿Cuánto gana?"), [("a", "$90"), ("b", "$26"), ("c", "$75"), ("d", "$450")]),
     ("E", t("<strong>2 ft 9 in + 1 ft 8 in</strong> = ?", "<strong>2 pies 9 pulgadas + 1 pie 8 pulgadas</strong> = ?"), [("a", t("4 ft 7 in", "4 pies 7 pulgadas")), ("b", t("3 ft 5 in", "3 pies 5 pulgadas")), ("c", t("4 ft 17 in", "4 pies 17 pulgadas")), ("d", t("4 ft 5 in", "4 pies 5 pulgadas"))]),
     ("F", t("<strong>5 lb 4 oz − 2 lb 10 oz</strong> = ?", "<strong>5 libras 4 onzas − 2 libras 10 onzas</strong> = ?"), [("a", t("3 lb 6 oz", "3 libras 6 onzas")), ("b", t("2 lb 10 oz", "2 libras 10 onzas")), ("c", t("2 lb 4 oz", "2 libras 4 onzas")), ("d", t("3 lb 10 oz", "3 libras 10 onzas"))]),
     ("G", t("A bus travels <strong>45 miles</strong> each hour. How long does it take to travel <strong>180 miles</strong>?", "Un autobús recorre <strong>45 millas</strong> cada hora. ¿Cuánto tarda en recorrer <strong>180 millas</strong>?"), [("a", t("4 hours", "4 horas")), ("b", t("135 hours", "135 horas")), ("c", t("8,100 hours", "8,100 horas")), ("d", t("225 hours", "225 horas"))]),
     ("H", t("A runner runs <strong>400 meters</strong>, <strong>15 times</strong>. How many kilometers does she run?", "Una corredora corre <strong>400 metros</strong>, <strong>15 veces</strong>. ¿Cuántos kilómetros corre?"), [("a", "6,000 km"), ("b", "60 km"), ("c", "6 km"), ("d", "0.6 km")])]

    return B.pagina_leccion(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"),
        t("Applied measurement problems", "Problemas aplicados de medición en contexto real"),
        t("Recipes, boards, work shifts, and trips: put all of Topic 6 to work in problems with several steps.", "Recetas, tablas, turnos de trabajo y viajes: ponga a trabajar todo el Tema 6 en problemas de varios pasos."),
        ("🧰", t("Convert first", "Primero convertir")),
        [t("<strong>Plan</strong> a measurement problem with several steps.", "<strong>Planear</strong> un problema de medición de varios pasos."),
         t("<strong>Convert</strong> to the same unit before you calculate.", "<strong>Convertir</strong> a la misma unidad antes de calcular."),
         t("<strong>Solve</strong> problems with time, money, and speed.", "<strong>Resolver</strong> problemas de tiempo, dinero y velocidad."),
         t("<strong>Add and subtract</strong> measures with two units, regrouping correctly.", "<strong>Sumar y restar</strong> medidas con dos units, reagrupando bien.").replace("dos units", "dos unidades")],
        secciones,
        (t("Write two measurement problems from your own life with two steps each: one about a recipe or shopping, and one about your work schedule or a trip. Solve them with the 4 steps.",
           "Escriba dos problemas de medición de su propia vida, de dos pasos cada uno: uno sobre una receta o las compras, y otro sobre su horario de trabajo o un viaje. Resuélvalos con los 4 pasos."),
         t("Next time you work or travel, write the start and end times and find the total time. If you are paid by the hour, find your pay for that day.",
           "La próxima vez que trabaje o viaje, anote la hora de inicio y la hora final y halle el tiempo total. Si le pagan por hora, halle su pago de ese día.")),
        quiz,
        t("Self-check checklist for applied measurement problems", "Lista de autoevaluación de problemas aplicados de medición"),
        t("Self-check checklist: skills for applied measurement problems", "Lista de autoevaluación: destrezas para problemas aplicados de medición"),
        [(t("Plan the steps", "Planear los pasos"), t("I find the question and the unit of the answer before I calculate.", "Encuentro la pregunta y la unidad de la respuesta antes de calcular."), t("I plan most problems.", "Planeo la mayoría de los problemas."), t("I start calculating without a plan.", "Empiezo a calcular sin un plan.")),
         (t("Same unit first", "Primero la misma unidad"), t("I always convert to the same unit before I calculate.", "Siempre convierto a la misma unidad antes de calcular."), t("I convert, but sometimes after calculating.", "Convierto, pero a veces después de calcular."), t("I calculate with two different units.", "Calculo con dos unidades distintas.")),
         (t("Time, money, and speed", "Tiempo, dinero y velocidad"), t("I find paid hours, pay, distances, and times correctly.", "Hallo bien las horas pagadas, el pago, las distancias y los tiempos."), t("I solve them with some help.", "Los resuelvo con un poco de ayuda."), t("I forget to take away breaks or mix up the operations.", "Olvido quitar los descansos o confundo las operaciones.")),
         (t("Regroup with two units", "Reagrupar con dos unidades"), t("I regroup at 12, 16, or 60, as each unit needs.", "Reagrupo a las 12, 16 o 60, según la unidad."), t("I regroup, but sometimes at 10.", "Reagrupo, pero a veces a las 10."), t("I do not regroup.", "No reagrupo."))],
        t("<p>You have finished Topic 6. You can now choose units, convert them, and solve real measurement problems with several steps.</p>\n<p>In <strong>Topic 7 · Geometry</strong> you will use measurement to describe shapes: their sides and angles, their perimeter, and their area.</p>",
          "<p>Terminó el Tema 6. Ya sabe elegir unidades, convertirlas y resolver problemas reales de medición de varios pasos.</p>\n<p>En el <strong>Tema 7 · Geometría</strong> usará la medición para describir figuras: sus lados y ángulos, su perímetro y su área.</p>"),
        ("7-1", (t("Topic 7 · ", "Tema 7 · "), t("Lesson 7.1 · Classifying 2D shapes", "Lección 7.1 · Clasificación de figuras 2D: atributos y vocabulario"))),
        [(t("multistep problem", "problema de varios pasos"), t("A problem that needs two or more operations to solve.", "Un problema que necesita dos o más operaciones para resolverse.")),
         (t("remainder", "residuo"), t("What is left over after a division. In real problems you must decide what it means.", "Lo que sobra después de una división. En los problemas reales hay que decidir qué quiere decir.")),
         (t("rate", "tasa"), t("A comparison of two different units, like miles per hour or dollars per hour.", "Una comparación de dos unidades distintas, como millas por hora o dólares por hora.")),
         (t("speed", "velocidad"), t("The distance traveled in each unit of time. Distance = speed × time.", "La distancia recorrida en cada unidad de tiempo. Distancia = velocidad × tiempo.")),
         (t("regroup", "reagrupar"), t("To change 12 inches into 1 foot (or 16 ounces into 1 pound, or 60 minutes into 1 hour) when you add or subtract measures.", "Cambiar 12 pulgadas por 1 pie (o 16 onzas por 1 libra, o 60 minutos por 1 hora) al sumar o restar medidas."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "u": {"in": ["inch", "inches"], "ft": ["foot", "feet"], "yd": ["yard", "yards"], "oz": ["ounce", "ounces"], "lb": ["pound", "pounds"], "floz": ["fluid ounce", "fluid ounces"], "gal": ["gallon", "gallons"], "h": ["hour", "hours"], "min": ["minute", "minutes"], "qt": ["quart", "quarts"]},
  "pregCorte": "A {cosa} is <strong>{L} {big}</strong> long. How many pieces of <strong>{p} {small}</strong> can you cut from it?",
  "cosas": ["board", "ribbon", "pipe", "rope"],
  "solCorte": "Same unit first: {L} × {f} = {T} {small}. Then {T} ÷ {p} = {q}{resto}. You can cut <strong>{q}</strong> pieces.",
  "resto": ", remainder {r}: the {r} {small} left over are not enough for another piece",
  "pregVasos": "You have <strong>{g} {gal}</strong> of juice. Each glass holds <strong>{s} fluid ounces</strong>. How many glasses can you fill? (1 gallon = 128 fluid ounces.)",
  "solVasos": "Same unit first: {g} × 128 = {T} fluid ounces. Then {T} ÷ {s} = <strong>{q}</strong> glasses.",
  "sinConvertir": "Convert to the same unit first.",
  "redondeo": "The leftover piece is too short to use: do not count it.",
  "pistaMisma": "Put both measures in the same unit, then divide.",
  "pregPago": "{nom} works a shift that starts at <strong>{a}</strong> and ends at <strong>{b}</strong>, with a <strong>{d}-minute</strong> break that is not paid. {nom} earns <strong>${r} per hour</strong>. How much does {nom} earn that day?",
  "la": "", "las": "",
  "nombres": ["Ana", "Luis", "Rosa", "Marcos", "Carmen", "José"],
  "solPago": "From {a} to {b} is {tot}. Minus the {d}-minute break: {H} paid hours. {H} × ${r} = $<strong>{p}</strong>.",
  "pagoDescanso": "Do not pay the break: take it away first.",
  "pistaPago": "Find the elapsed time, take away the break, and multiply by the pay per hour.",
  "am": "a.m.", "pm": "p.m.", "dur": "{h} h {m} min", "durH": "{h} h",
  "pregDist": "A truck travels <strong>{v} miles each hour</strong>. How many miles does it travel in <strong>{h} hours</strong>?",
  "solDist": "Distance = speed × time: {v} × {h} = <strong>{d}</strong> miles.",
  "pregTiempo": "A truck travels <strong>{v} miles each hour</strong>. How many hours does it take to travel <strong>{d} miles</strong>?",
  "solTiempo": "How many groups of {v} miles fit in {d} miles? {d} ÷ {v} = <strong>{h}</strong> hours.",
  "velSuma": "Adding or subtracting does not work here: the miles come in equal groups, one for each hour.",
  "velMal": "Check the operation: distance = speed × time, and time = distance ÷ speed.",
  "pistaVel": "Each hour adds the same number of miles: equal groups.",
  "pregSuma": "<strong>{a} + {b}</strong> = ?", "pregResta": "<strong>{a} − {b}</strong> = ?",
  "dos": "{q} {g} {r} {p}",
  "solSuma": "{q1} + {q2} = {Q} {gp} and {r1} + {r2} = {R} {pp}. {R} {pp} = 1 {g1} {rr} {prr}, so the total is {ans}.",
  "solResta": "{r1} {p1} − {r2} {p2} cannot be done: borrow 1 {g1} = {f} {pp}. {A} − {q2} = {Q} {gp} and {B} − {r2} = {R} {pr}. The answer is {ans}.",
  "pistaDiez": "You regrouped at 10. Here 1 {g1} = {f} {pp}.",
  "pistaSinLlevar": "You took away {f} {pp} but did not add the 1 {g1}.",
  "pistaAlReves": "You subtracted the small unit the other way around. Borrow 1 {g1} = {f} {pp}.",
  "pistaSinBajar": "After borrowing, the {gp} go down by 1.",
  "pistaReag": "Work with each unit, then regroup at {f}, not at 10."
 },
 "es": {
  "u": {"in": ["pulgada", "pulgadas"], "ft": ["pie", "pies"], "yd": ["yarda", "yardas"], "oz": ["onza", "onzas"], "lb": ["libra", "libras"], "floz": ["onza líquida", "onzas líquidas"], "gal": ["galón", "galones"], "h": ["hora", "horas"], "min": ["minuto", "minutos"], "qt": ["cuarto", "cuartos"]},
  "pregCorte": "{cosa} mide <strong>{L} {big}</strong>. ¿Cuántos pedazos de <strong>{p} {small}</strong> se pueden cortar?",
  "cosas": ["Una tabla", "Una cinta", "Un tubo", "Una soga"],
  "solCorte": "Primero la misma unidad: {L} × {f} = {T} {small}. Después {T} ÷ {p} = {q}{resto}. Se pueden cortar <strong>{q}</strong> pedazos.",
  "resto": ", residuo {r}: lo que sobra ({r} {small}) no alcanza para otro pedazo",
  "pregVasos": "Usted tiene <strong>{g} {gal}</strong> de jugo. A cada vaso le caben <strong>{s} onzas líquidas</strong>. ¿Cuántos vasos puede llenar? (1 galón = 128 onzas líquidas).",
  "solVasos": "Primero la misma unidad: {g} × 128 = {T} onzas líquidas. Después {T} ÷ {s} = <strong>{q}</strong> vasos.",
  "sinConvertir": "Primero convierta a la misma unidad.",
  "redondeo": "El pedazo que sobra es demasiado corto para usarlo: no lo cuente.",
  "pistaMisma": "Ponga las dos medidas en la misma unidad, y después divida.",
  "pregPago": "{nom} trabaja un turno que empieza a {la1}<strong>{a}</strong> y termina a {la2}<strong>{b}</strong>, con un descanso de <strong>{d} minutos</strong> que no se paga. Gana <strong>${r} por hora</strong>. ¿Cuánto gana ese día?",
  "la": "la ", "las": "las ",
  "nombres": ["Ana", "Luis", "Rosa", "Marcos", "Carmen", "José"],
  "solPago": "De {a} a {b} son {tot}. Menos el descanso de {d} minutos: {H} horas pagadas. {H} × ${r} = $<strong>{p}</strong>.",
  "pagoDescanso": "El descanso no se paga: quítelo primero.",
  "pistaPago": "Halle el tiempo transcurrido, quite el descanso y multiplique por el pago por hora.",
  "am": "a.m.", "pm": "p.m.", "dur": "{h} h {m} min", "durH": "{h} h",
  "pregDist": "Un camión recorre <strong>{v} millas cada hora</strong>. ¿Cuántas millas recorre en <strong>{h} horas</strong>?",
  "solDist": "Distancia = velocidad × tiempo: {v} × {h} = <strong>{d}</strong> millas.",
  "pregTiempo": "Un camión recorre <strong>{v} millas cada hora</strong>. ¿Cuántas horas tarda en recorrer <strong>{d} millas</strong>?",
  "solTiempo": "¿Cuántos grupos de {v} millas caben en {d} millas? {d} ÷ {v} = <strong>{h}</strong> horas.",
  "velSuma": "Sumar o restar no sirve aquí: las millas vienen en grupos iguales, uno por cada hora.",
  "velMal": "Revise la operación: distancia = velocidad × tiempo, y tiempo = distancia ÷ velocidad.",
  "pistaVel": "Cada hora suma la misma cantidad de millas: grupos iguales.",
  "pregSuma": "<strong>{a} + {b}</strong> = ?", "pregResta": "<strong>{a} − {b}</strong> = ?",
  "dos": "{q} {g} {r} {p}",
  "solSuma": "{q1} + {q2} = {Q} {gp} y {r1} + {r2} = {R} {pp}. {R} {pp} = 1 {g1} {rr} {prr}, así que el total es {ans}.",
  "solResta": "{r1} {p1} − {r2} {p2} no se puede: pida prestado 1 {g1} = {f} {pp}. {A} − {q2} = {Q} {gp} y {B} − {r2} = {R} {pr}. La respuesta es {ans}.",
  "pistaDiez": "Reagrupó a las 10. Aquí 1 {g1} = {f} {pp}.",
  "pistaSinLlevar": "Quitó {f} {pp}, pero no sumó la unidad grande que se forma (1 {g1}).",
  "pistaAlReves": "Restó la unidad pequeña al revés. Pida prestado 1 {g1} = {f} {pp}.",
  "pistaSinBajar": "Después de pedir prestado, la unidad grande baja 1.",
  "pistaReag": "Trabaje cada unidad, y después reagrupe a las {f}, no a las 10."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function un(k, n){ return TXT.u[k][n === 1 ? 0 : 1]; }
function hora(m){ var h = Math.floor(m / 60), mi = m % 60, h12 = h % 12 === 0 ? 12 : h % 12; return h12 + ":" + (mi < 10 ? "0" : "") + mi + " " + (h < 12 ? TXT.am : TXT.pm); }

/* ============ MODULE 1 · same unit first ============ */
var CORTE = [["ft", "in", 12, [4, 12], [5, 20]], ["yd", "in", 36, [2, 8], [6, 30]], ["yd", "ft", 3, [5, 20], [2, 7]]];
function genMisma(){
  var p = [];
  if (Math.random() < 0.7){
    var c = elige(CORTE), L = aleatorio(c[3][0], c[3][1]), pz = aleatorio(c[4][0], c[4][1]), T = L * c[2], q = Math.floor(T / pz), r = T % pz;
    if (q < 2) return genMisma();
    if (r > 0) p.push({ v: q + 1, msg: TXT.redondeo });
    if (Math.floor(L / pz) !== q && L >= pz) p.push({ v: Math.floor(L / pz), msg: TXT.sinConvertir });
    return { enun: F(TXT.pregCorte, { cosa: elige(TXT.cosas), L: L, big: un(c[0], L), p: pz, small: un(c[1], pz) }),
      solucion: F(TXT.solCorte, { L: L, f: c[2], T: com(T), small: TXT.u[c[1]][1], p: pz, q: q, resto: r ? F(TXT.resto, { r: r, small: un(c[1], r) }) : "" }),
      evalua: numN(q, p, TXT.pistaMisma) };
  }
  var g = aleatorio(1, 5), s = elige([4, 8, 16]), T = 128 * g, q = T / s;
  if (q !== g * s) p.push({ v: g * s, msg: TXT.sinConvertir });
  if (Math.floor(g / s) > 0) p.push({ v: Math.floor(g / s), msg: TXT.sinConvertir });
  return { enun: F(TXT.pregVasos, { g: g, gal: un("gal", g), s: s }), solucion: F(TXT.solVasos, { g: g, T: com(T), s: s, q: q }), evalua: numN(q, p, TXT.pistaMisma) };
}

/* ============ MODULE 2 · time and pay ============ */
function genPago(){
  var ini = aleatorio(13, 20) * 30, H = aleatorio(5, 9), d = elige([30, 60]), r = aleatorio(12, 25), fin = ini + H * 60 + d, tot = H * 60 + d;
  var totTxt = F(tot % 60 ? TXT.dur : TXT.durH, { h: Math.floor(tot / 60), m: tot % 60 }), nom = elige(TXT.nombres), p = [];
  var sin = tot / 60 * r; if (sin === Math.round(sin)) p.push({ v: sin, msg: TXT.pagoDescanso });
  var art = function(m){ return Math.floor((m % 720) / 60) === 1 ? TXT.la : TXT.las; };
  return { enun: F(TXT.pregPago, { nom: nom, a: hora(ini), b: hora(fin), d: d, r: r, la1: art(ini), la2: art(fin) }),
    solucion: F(TXT.solPago, { a: hora(ini), b: hora(fin), tot: totTxt, d: d, H: H, r: r, p: com(H * r) }),
    evalua: numN(H * r, p, TXT.pistaPago) };
}

/* ============ MODULE 3 · regroup ============ */
var REAG = [["ft", "in", 12], ["lb", "oz", 16], ["h", "min", 60], ["gal", "qt", 4]];
function dos(par, q, r){ return F(TXT.dos, { q: q, g: un(par[0], q), r: r, p: un(par[1], r) }); }
function genReag(){
  var par = elige(REAG), f = par[2], op = [], pistas = {}, ans, txt, o = { f: f, g1: TXT.u[par[0]][0], pp: TXT.u[par[1]][1], gp: TXT.u[par[0]][1] };
  function mete(q, r, msg){ if (q < 0 || r < 0 || r >= f + 10) return; var h = dos(par, q, r); if (op.some(function(x){ return x.html === h; })) return; op.push({ html: h, clave: "k" + op.length }); if (msg) pistas["k" + (op.length - 1)] = msg; }
  if (Math.random() < 0.5){
    var q1 = aleatorio(1, 6), q2 = aleatorio(1, 5), r1 = aleatorio(Math.ceil(f / 2), f - 1), r2 = aleatorio(f - r1, f - 1), R = r1 + r2, Q = q1 + q2 + 1, rr = R - f;
    ans = dos(par, Q, rr); mete(Q, rr);
    if (R - 10 >= 0 && f !== 10) mete(Q, R - 10, F(TXT.pistaDiez, o));
    mete(Q - 1, rr, F(TXT.pistaSinLlevar, o));
    mete(Q, R, F(TXT.pistaReag, o));
    if (op.length < 4) mete(Q + 1, rr, F(TXT.pistaReag, o));
    if (op.length < 4) mete(Q, (rr + 1) % f, F(TXT.pistaReag, o));
    txt = F(TXT.solSuma, { q1: q1, q2: q2, Q: q1 + q2, gp: TXT.u[par[0]][1], r1: r1, r2: r2, R: R, pp: TXT.u[par[1]][1], g1: TXT.u[par[0]][0], rr: rr, prr: un(par[1], rr), ans: ans });
    return { enun: F(TXT.pregSuma, { a: dos(par, q1, r1), b: dos(par, q2, r2) }), opciones: op, correcta: "k0", pistas: pistas, pista: F(TXT.pistaReag, o), bien: txt, mal: txt };
  }
  var q2 = aleatorio(1, 4), q1 = q2 + aleatorio(2, 5), r1 = aleatorio(0, Math.floor(f / 2)), r2 = aleatorio(r1 + 1, f - 1), Q = q1 - 1 - q2, R = r1 + f - r2;
  ans = dos(par, Q, R); mete(Q, R);
  mete(q1 - q2, r2 - r1, F(TXT.pistaAlReves, o));
  if (r1 + 10 - r2 >= 0 && f !== 10) mete(Q, r1 + 10 - r2, F(TXT.pistaDiez, o));
  mete(Q + 1, R, F(TXT.pistaSinBajar, o));
  if (op.length < 4) mete(Q, (R + 1) % f, F(TXT.pistaReag, o));
  if (op.length < 4) mete(Q + 2, R, F(TXT.pistaReag, o));
  if (op.length < 3) mete(Q, (R + 2) % f, F(TXT.pistaReag, o));
  txt = F(TXT.solResta, { r1: r1, p1: un(par[1], r1), r2: r2, p2: un(par[1], r2), g1: TXT.u[par[0]][0], f: f, pp: TXT.u[par[1]][1], A: q1 - 1, q2: q2, Q: Q, gp: TXT.u[par[0]][1], B: r1 + f, R: R, pr: un(par[1], R), ans: ans });
  return { enun: F(TXT.pregResta, { a: dos(par, q1, r1), b: dos(par, q2, r2) }), opciones: op, correcta: "k0", pistas: pistas, pista: F(TXT.pistaReag, o), bien: txt, mal: txt };
}

/* ============ MODULE 4 · distance, speed, and time ============ */
function genVel(){
  var v = aleatorio(5, 13) * 5, h = aleatorio(2, 9), d = v * h, p = [];
  if (Math.random() < 0.5){
    p.push({ v: v + h, msg: TXT.velSuma });
    return { enun: F(TXT.pregDist, { v: v, h: h }), solucion: F(TXT.solDist, { v: v, h: h, d: com(d) }), evalua: numN(d, p, TXT.velMal) };
  }
  p.push({ v: d - v, msg: TXT.velSuma }); p.push({ v: d + v, msg: TXT.velSuma }); p.push({ v: d * v, msg: TXT.velMal });
  return { enun: F(TXT.pregTiempo, { v: v, d: com(d) }), solucion: F(TXT.solTiempo, { v: v, d: com(d), h: h }), evalua: numN(h, p, TXT.velMal) };
}

creaPracticaLibre("p1", genMisma);
creaPracticaLibre("p2", genPago);
creaPracticaOM("p3", genReag);
creaPracticaLibre("p4", genVel);
'''

def practica_pagina():
    n = N
    mods = [
     (t("same-unit", "misma-unidad"), t("Same unit first", "Primero la misma unidad"),
      f'''      <p>{t("Convert first, then calculate. If a division has a remainder, ask what it means: a piece that is too short does not count.", "Convierta primero, y después calcule. Si una división tiene residuo, pregúntese qué quiere decir: un pedazo demasiado corto no cuenta.")}</p>
      <table class="reglas">
        <caption>{t("Equivalences", "Equivalencias")}</caption>
        <tbody><tr><td>1 ft = 12 in</td><td>1 yd = 3 ft = 36 in</td><td>{t("1 gal = 128 fl oz", "1 galón = 128 onzas líquidas")}</td></tr></tbody>
      </table>
{B.libre("p1", t("Practice: solve the problem", "Practique: resolver el problema"), t("Answer", "Respuesta"))}'''),
     (t("work-pay", "pago"), t("Time and pay", "Tiempo y pago"),
      f'''      <p>{t("1. Find the time from the start to the end. 2. Take away the break that is not paid. 3. Multiply the paid hours by the pay per hour.", "1. Halle el tiempo del inicio al final. 2. Quite el descanso que no se paga. 3. Multiplique las horas pagadas por el pago por hora.")}</p>
{B.libre("p2", t("Practice: pay for the day", "Practique: el pago del día"), t("Pay in dollars", "Pago en dólares"))}'''),
     (t("regroup", "reagrupar"), t("Add and subtract with two units", "Sumar y restar con dos unidades"),
      f'''      <div class="caja-atencion"><strong>{t("Regroup at the size of the unit, not at 10:", "Reagrupe al tamaño de la unidad, no a las 10:")}</strong> {t("12 inches = 1 foot, 16 ounces = 1 pound, 60 minutes = 1 hour, 4 quarts = 1 gallon.", "12 pulgadas = 1 pie, 16 onzas = 1 libra, 60 minutos = 1 hora, 4 cuartos = 1 galón.")}</div>
{B.om("p3", t("Practice: add or subtract", "Practique: sumar o restar"))}'''),
     (t("speed", "velocidad"), t("Distance, speed, and time", "Distancia, velocidad y tiempo"),
      f'''      <p>{t("<strong>Distance = speed × time.</strong> To find the time, divide: time = distance ÷ speed.", "<strong>Distancia = velocidad × tiempo.</strong> Para hallar el tiempo, divida: tiempo = distancia ÷ velocidad.")}</p>
{B.libre("p4", t("Practice: miles and hours", "Practique: millas y horas"), t("Answer", "Respuesta"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"), t("Applied measurement problems", "Problemas aplicados de medición en contexto real"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Problemas aplicados de medición en contexto real")
