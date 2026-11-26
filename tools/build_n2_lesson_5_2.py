"""Level 2 · Lesson 5.2 · Percent change: increase and decrease — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import fr

B.NIVEL = 2
N = "5-2"
TEMA = ("Percents", "Porcentajes")
TIT = ("Percent change: increase and decrease", "Cambio porcentual: aumento y disminución")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def leccion():
    n = N
    formula = f'<p style="text-align:center;font-size:1.3rem;font-weight:700;color:#0d47a1">{t("% change", "% de cambio")} = {fr(t("new value − original value", "valor nuevo − valor original"), t("original value", "valor original"))} × 100</p>'
    s1 = f'''<p>{t("In Lesson 5.1 you solved the three cases of percent. This lesson uses case 3 (finding the percent) for a very common question: <strong>how much did a quantity change?</strong> It is the tool behind sentences like “the price went up 12%” or “the population went down 3%.”", "En la Lección 5.1 resolvió los tres casos del porcentaje. Esta lección aplica el caso 3 (hallar el porcentaje) a una pregunta muy frecuente: <strong>¿cuánto cambió una cantidad?</strong> Es la herramienta detrás de frases como «el precio subió un 12%» o «la población bajó un 3%».")}</p>
<p>{t("A good habit is to <strong>estimate</strong> first whether the change is large or small compared with the starting value. That way you spot silly answers right away.", "Un buen hábito es <strong>estimar</strong> primero si el cambio es grande o pequeño en relación con el valor de partida. Así se detectan de inmediato los resultados absurdos.")}</p>
{ej(t("Example: a quick estimate", "Ejemplo: estimación rápida"), t("A price goes up from $40 to $52.", "Un precio sube de $40 a $52."),
  [("1", t("The change.", "El cambio."), t("The increase is $12.", "El aumento es de $12.")),
   ("2", t("Use 10%.", "Use el 10%."), t("10% of 40 is 4, and 12 is three times 4.", "El 10% de 40 es 4, y 12 es tres veces 4.")),
   ("✓", t("Estimate.", "Estimación."), t("About <strong>30%</strong>.", "Alrededor del <strong>30%</strong>."))])}
{caja("tip", t("Handy benchmarks", "Referencias útiles"), t("<p>To find 10%, move the decimal point one place to the left. 50% is half. An increase of 100% means the amount doubled.</p>", "<p>El 10% se obtiene moviendo el punto decimal un lugar a la izquierda. El 50% es la mitad. Un aumento del 100% significa que la cantidad se duplicó.</p>"))}
{practica("p1", t("Practice 1 — Estimate", "Práctica 1 — Estime"), t("A price goes from $60 to $75. About how big is the increase?", "Un precio pasa de $60 a $75. ¿De qué tamaño es, más o menos, el aumento?"),
          [("a", t("About 10%", "Alrededor del 10%")), ("b", t("About 25%", "Alrededor del 25%")), ("c", t("About 50%", "Alrededor del 50%")), ("d", t("About 75%", "Alrededor del 75%"))])}
{enlace(n, t("estimate", "estimar"), t("estimate before you calculate", "antes de calcular, estimar"), t("Estimate the size of the change with 10% and compare it with the exact answer.", "Estime el tamaño del cambio con el 10% y compárelo con el cálculo exacto."))}'''

    s2 = f'''{formula}
<p>{t("The top is the <strong>absolute change</strong> (how much it went up or down). The bottom is always the <strong>original value</strong>, because it is the reference point. If the answer is positive, it was an increase; if it is negative, it was a decrease.", "El numerador es el <strong>cambio absoluto</strong> (cuánto subió o bajó). El denominador es siempre el <strong>valor original</strong>, porque es el punto de referencia. Si el resultado es positivo, hubo aumento; si es negativo, hubo disminución.")}</p>
{caja("ojo", t("The most common mistake", "El error más frecuente"), t("<p>Dividing by the new value. If a stock goes down from $80 to $60, the change is −20, and you divide by 80 (the original): −25%. Dividing by 60 would give 33.3%, which is wrong.</p>", "<p>Dividir entre el valor nuevo. Si una acción baja de $80 a $60, el cambio es −20 y se divide entre 80 (el original): −25%. Dividir entre 60 daría 33.3%, que es incorrecto.</p>"))}
{ej(t("Example: a price increase", "Ejemplo: aumento de precio"), t("A product cost $40 and now costs $52. What was the percent increase?", "Un producto costaba $40 y ahora cuesta $52. ¿Cuál fue el porcentaje de aumento?"),
  [("1", t("Change.", "Cambio."), "52 − 40 = 12."),
   ("2", t("Divide by the original.", "Divida entre el original."), "12 ÷ 40 = 0.30."),
   ("✓", t("Times 100.", "Por 100."), t("<strong>30% increase</strong>. It matches the estimate.", "<strong>Aumento del 30%</strong>. Coincide con la estimación."))])}
{ej(t("Example: a raise", "Ejemplo: un aumento de sueldo"), t("A wage goes from $15.00 to $16.20 an hour. What percent raise did the worker get?", "Un salario pasa de $15.00 a $16.20 por hora. ¿Qué porcentaje de aumento recibió el trabajador?"),
  [("1", t("Change.", "Cambio."), "16.20 − 15.00 = 1.20."),
   ("✓", t("Divide and × 100.", "Divida y × 100."), t("1.20 ÷ 15.00 = 0.08 → <strong>8% raise</strong>.", "1.20 ÷ 15.00 = 0.08 → <strong>aumento del 8%</strong>."))])}
{ej(t("Example: temperature", "Ejemplo: temperatura"), t("The temperature went down from 80 °F to 68 °F. What was the percent decrease?", "La temperatura bajó de 80 °F a 68 °F. ¿Cuál fue el porcentaje de disminución?"),
  [("1", t("Change.", "Cambio."), t("68 − 80 = −12 (negative: a decrease).", "68 − 80 = −12 (negativo: disminución).")),
   ("✓", t("Divide and × 100.", "Divida y × 100."), t("−12 ÷ 80 = −0.15 → <strong>15% decrease</strong>.", "−12 ÷ 80 = −0.15 → <strong>disminución del 15%</strong>."))])}
{ej(t("Example: population", "Ejemplo: población"), t("A town had 2,500 people and now has 2,300. By what percent did the population go down?", "Un pueblo tenía 2,500 habitantes y ahora tiene 2,300. ¿En qué porcentaje disminuyó la población?"),
  [("1", t("Change.", "Cambio."), "2,300 − 2,500 = −200."),
   ("✓", t("Divide and × 100.", "Divida y × 100."), t("−200 ÷ 2,500 = −0.08 → <strong>8% decrease</strong>.", "−200 ÷ 2,500 = −0.08 → <strong>disminución del 8%</strong>."))])}
{calc(t("Percent change on the calculator", "El cambio porcentual en la calculadora"), t(f"<p>From $40 to $52: type {T('(')} {T('52')} {T('−')} {T('40')} {T(')')} {T('÷')} {T('40')} {T('×')} {T('100')} {T('enter')}. The screen shows 30. The parentheses make the subtraction go first.</p>", f"<p>De $40 a $52: escriba {T('(')} {T('52')} {T('−')} {T('40')} {T(')')} {T('÷')} {T('40')} {T('×')} {T('100')} {T('enter')}. La pantalla muestra 30. Los paréntesis hacen que la resta vaya primero.</p>"))}
{practica("p2", t("Practice 2 — An increase", "Práctica 2 — Un aumento"), t("What is the percent change from $50 to $65?", "¿Cuál es el cambio porcentual de $50 a $65?"),
          [("a", t("30% increase", "Aumento del 30%")), ("b", t("15% increase", "Aumento del 15%")), ("c", t("23% increase", "Aumento del 23%")), ("d", t("65% increase", "Aumento del 65%"))])}
{practica("p3", t("Practice 3 — A decrease", "Práctica 3 — Una disminución"), t("What is the percent change from 120 to 90?", "¿Cuál es el cambio porcentual de 120 a 90?"),
          [("a", t("25% increase", "Aumento del 25%")), ("b", t("33.3% decrease", "Disminución del 33.3%")), ("c", t("25% decrease", "Disminución del 25%")), ("d", t("30% decrease", "Disminución del 30%"))])}
{enlace(n, t("change", "cambio"), t("percent change", "cambio porcentual"), t("Compare the starting and ending values, and see why going up and down by the same percent does not leave things the same.", "Compare el valor inicial y el final, y compruebe por qué subir y bajar el mismo porcentaje no deja todo igual."))}'''

    s3 = f'''<p>{t("Is a $5 increase always the same percent? No. The <strong>absolute change</strong> tells how many units something changed; the <strong>relative change</strong> (the percent change) tells how big that change is compared with the starting point.", "¿Un aumento de $5 representa siempre el mismo porcentaje? No. El <strong>cambio absoluto</strong> dice cuántas unidades cambió algo; el <strong>cambio relativo</strong> (el porcentual) dice cuánto representa ese cambio en comparación con el punto de partida.")}</p>
{tabla(t("The same $5 increase", "El mismo aumento de $5"), t("The same $5 increase on different original values", "El mismo aumento de $5 sobre valores originales distintos"),
       [t("Item", "Artículo"), t("Original", "Original"), t("New", "Nuevo"), t("Absolute change", "Cambio absoluto"), t("Percent change", "Cambio porcentual")],
       [[t("Lunch", "Almuerzo"), "$10", "$15", "$5", "<strong>50%</strong>"], [t("Shoes", "Zapatos"), "$50", "$55", "$5", "<strong>10%</strong>"], [t("Bicycle", "Bicicleta"), "$200", "$205", "$5", "<strong>2.5%</strong>"]])}
<p>{t("That is why, to compare changes in quantities of different sizes, you use the percent.", "Por eso, para comparar cambios de cantidades de distinto tamaño, se usa el porcentaje.")}</p>
{caja("ojo", t("Up and down by the same percent is not a round trip", "Subir y bajar el mismo porcentaje no devuelve al valor original"), t("<p>If a $100 price goes up 10%, it becomes $110. If it then goes down 10%, the discount is figured on $110: 110 − 11 = <strong>$99</strong>. Each change is figured on the value at that moment.</p>", "<p>Si un precio de $100 sube un 10%, queda en $110. Si luego baja un 10%, la rebaja se calcula sobre $110: 110 − 11 = <strong>$99</strong>. Cada cambio se calcula sobre el valor vigente en ese momento.</p>"))}
{practica("p4", t("Practice 4 — Which changed more?", "Práctica 4 — ¿Cuál cambió más?"), t("Bread goes up from $2 to $3. A car goes up from $20,000 to $21,000. Which one had the greater percent change?", "El pan sube de $2 a $3. Un auto sube de $20,000 a $21,000. ¿Cuál tuvo el mayor cambio porcentual?"),
          [("a", t("The car, because it went up $1,000", "El auto, porque subió $1,000")), ("b", t("They both went up the same", "Los dos subieron lo mismo")), ("c", t("The bread, because it went up 50%", "El pan, porque subió 50%"))])}
{practica("p5", t("Practice 5 — Up and down", "Práctica 5 — Sube y baja"), t("A $100 price goes up 20% and then down 20%. What is the final price?", "Un precio de $100 sube 20% y luego baja 20%. ¿Cuál es el precio final?"),
          [("a", "$100"), ("b", "$96"), ("c", "$80"), ("d", "$104")])}
{enlace(n, t("absolute-relative", "absoluto-relativo"), t("absolute and relative change", "cambio absoluto y cambio relativo"), t("See how the same dollar increase weighs differently depending on the starting price.", "Vea cómo el mismo aumento en dólares pesa distinto según el precio de partida."))}'''

    s4 = f'''<p>{t("Sometimes you know the percent and want the new value. You can find the change and add it or subtract it, or you can multiply right away by a <strong>change factor</strong>:", "A veces se conoce el porcentaje y se quiere el valor nuevo. Se puede calcular el cambio y sumarlo o restarlo, o multiplicar directamente por un <strong>factor de cambio</strong>:")}</p>
{tabla(t("Change factors", "Factores de cambio"), t("The change factor for an increase and for a decrease", "El factor de cambio para un aumento y para una disminución"),
       ["", t("Formula", "Fórmula"), t("Example", "Ejemplo")],
       [[t("<strong>Increase</strong> of r%", "<strong>Aumento</strong> de r%"), t("new = original × (1 + r)", "nuevo = original × (1 + r)"), t("12% increase → × 1.12", "aumento de 12% → × 1.12")],
        [t("<strong>Decrease</strong> of r%", "<strong>Disminución</strong> de r%"), t("new = original × (1 − r)", "nuevo = original × (1 − r)"), t("15% decrease → × 0.85", "disminución de 15% → × 0.85")]])}
{ej(t("Example: rent", "Ejemplo: el alquiler"), t("A $1,250 rent goes up 4%. What is the new rent?", "Un alquiler de $1,250 aumenta un 4%. ¿Cuál es el nuevo alquiler?"),
  [("1", t("Factor.", "Factor."), "1 + 0.04 = 1.04."),
   ("2", t("Multiply.", "Multiplique."), "1,250 × 1.04 = 1,300."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$1,300</strong>. The change factor will be the main tool of Lesson 5.3.", "<strong>$1,300</strong>. El factor de cambio será la herramienta central de la Lección 5.3."))])}
{practica("p6", t("Practice 6 — The factor", "Práctica 6 — El factor"), t("What number do you multiply by to decrease a value by 15%?", "¿Por qué número se multiplica para disminuir un valor un 15%?"),
          [("a", "0.15"), ("b", "1.15"), ("c", "0.85"), ("d", "85")])}
{practica("p7", t("Practice 7 — New rent", "Práctica 7 — El nuevo alquiler"), t("A $1,250 rent goes up 4%. What is the new rent?", "Un alquiler de $1,250 sube un 4%. ¿Cuál es el nuevo alquiler?"),
          [("a", "$1,254"), ("b", "$1,300"), ("c", "$50"), ("d", "$1,200")])}
{enlace(n, t("factor", "factor"), t("the change factor", "el factor de cambio"), t("Multiply by (1 + r) or by (1 − r) and check that it gives the same as adding or subtracting the change.", "Multiplique por (1 + r) o por (1 − r) y compruebe que da lo mismo que sumar o restar el cambio."))}'''

    secciones = [("s-" + t("estimate", "estimar"), t("Estimate before you calculate", "Antes de calcular, estimar"), s1),
                 ("s-" + t("formula", "formula"), t("The percent-change formula: increase and decrease", "La fórmula del cambio porcentual: aumento y disminución"), s2),
                 ("s-" + t("absolute-relative", "absoluto-relativo"), t("Absolute change and relative change", "Cambio absoluto y cambio relativo"), s3),
                 ("s-" + t("factor", "factor"), t("From the percent to the new value: the change factor", "Del porcentaje al valor nuevo: el factor de cambio"), s4)]

    lesson = {"next": t("Lesson 5.3", "Lección 5.3"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("10% of 60 is 6, and the change is 15.", "El 10% de 60 es 6, y el cambio es 15."), "c": t("50% of 60 would be 30.", "El 50% de 60 serían 30."), "d": t("The new price is 75, but the change is only 15.", "El precio nuevo es 75, pero el cambio es solo 15.")},
             "right": t("15 is about 2.5 times 6 (10%): about 25%.", "15 son unas 2.5 veces 6 (el 10%): alrededor del 25%."), "solution": t("The change is 15. 10% of 60 is 6; 15 is 2.5 times 6, so about 25%. (Exact: 15 ÷ 60 = 25%.)", "El cambio es 15. El 10% de 60 es 6; 15 es 2.5 veces 6, así que alrededor del 25%. (Exacto: 15 ÷ 60 = 25%.)")},
      "p2": {"ok": "a", "hints": {"b": t("15 is the change in dollars. Divide it by 50.", "15 es el cambio en dólares. Divídalo entre 50."), "c": t("You divided by the new value. Divide by the original, 50.", "Dividió entre el valor nuevo. Se divide entre el original, 50."), "d": t("65 is the new price, not the change.", "65 es el precio nuevo, no el cambio.")},
             "right": t("15 ÷ 50 = 0.30 = 30%.", "15 ÷ 50 = 0.30 = 30%."), "solution": t("Change: 65 − 50 = 15. 15 ÷ 50 = 0.30 → 30% increase.", "Cambio: 65 − 50 = 15. 15 ÷ 50 = 0.30 → aumento del 30%.")},
      "p3": {"ok": "c", "hints": {"a": t("It went down, not up.", "Bajó, no subió."), "b": t("You divided by 90, the new value. Divide by 120.", "Dividió entre 90, el valor nuevo. Divida entre 120."), "d": t("Check: 30 ÷ 120.", "Revise: 30 ÷ 120.")},
             "right": t("−30 ÷ 120 = −0.25: 25% decrease.", "−30 ÷ 120 = −0.25: disminución del 25%."), "solution": t("Change: 90 − 120 = −30. −30 ÷ 120 = −0.25 → 25% decrease.", "Cambio: 90 − 120 = −30. −30 ÷ 120 = −0.25 → disminución del 25%.")},
      "p4": {"ok": "c", "hints": {"a": t("$1,000 is the absolute change. Compare it with $20,000: 5%.", "$1,000 es el cambio absoluto. Compárelo con $20,000: 5%."), "b": t("Find each percent: 1 ÷ 2 and 1,000 ÷ 20,000.", "Calcule cada porcentaje: 1 ÷ 2 y 1,000 ÷ 20,000.")},
             "right": t("Bread: 50%. Car: 5%.", "Pan: 50%. Auto: 5%."), "solution": t("Bread: $1 ÷ $2 = 50%. Car: $1,000 ÷ $20,000 = 5%. The bread had the greater relative change.", "Pan: $1 ÷ $2 = 50%. Auto: $1,000 ÷ $20,000 = 5%. El pan tuvo el mayor cambio relativo.")},
      "p5": {"ok": "b", "hints": {"a": t("The 20% decrease is figured on $120, not on $100.", "La rebaja del 20% se calcula sobre $120, no sobre $100."), "c": t("First it goes up to $120.", "Primero sube a $120."), "d": t("It ends below $100: the decrease is bigger in dollars.", "Termina por debajo de $100: la rebaja es mayor en dólares.")},
             "right": t("$120 × 0.80 = $96.", "$120 × 0.80 = $96."), "solution": t("$100 × 1.20 = $120. Then $120 × 0.80 = $96.", "$100 × 1.20 = $120. Después $120 × 0.80 = $96.")},
      "p6": {"ok": "c", "hints": {"a": t("0.15 gives only the change.", "0.15 da solo el cambio."), "b": t("1.15 is for an increase.", "1.15 es para un aumento."), "d": t("Write the percent as a decimal: 85% = 0.85.", "Escriba el porcentaje en decimal: 85% = 0.85.")},
             "right": t("1 − 0.15 = 0.85.", "1 − 0.15 = 0.85."), "solution": t("What is left is 85%: 1 − 0.15 = 0.85.", "Queda el 85%: 1 − 0.15 = 0.85.")},
      "p7": {"ok": "b", "hints": {"a": t("You added 4 dollars, not 4%.", "Sumó 4 dólares, no 4%."), "c": t("$50 is only the increase. Add it to $1,250.", "$50 es solo el aumento. Súmelo a $1,250."), "d": t("It is an increase, not a decrease.", "Es un aumento, no una disminución.")},
             "right": t("1,250 × 1.04 = 1,300.", "1,250 × 1.04 = 1,300."), "solution": t("Factor 1.04: 1,250 × 1.04 = $1,300.", "Factor 1.04: 1,250 × 1.04 = $1,300.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("12 is the change in dollars. Divide it by 40.", "12 es el cambio en dólares. Divídalo entre 40."), "b": t("You divided by 52. Divide by the original, 40.", "Dividió entre 52. Divida entre el original, 40."), "d": t("52 is the new price.", "52 es el precio nuevo.")}, "solution": t("12 ÷ 40 = 0.30 = 30% increase.", "12 ÷ 40 = 0.30 = aumento del 30%.")},
      "B": {"ok": "a", "hints": {"b": t("12 is the change in degrees.", "12 es el cambio en grados."), "c": t("You divided by 68. Divide by 80.", "Dividió entre 68. Divida entre 80."), "d": t("85% is what is left, not the change.", "85% es lo que queda, no el cambio.")}, "solution": t("−12 ÷ 80 = −0.15: 15% decrease.", "−12 ÷ 80 = −0.15: disminución del 15%.")},
      "C": {"ok": "b", "hints": {"a": t("You divided by 60. Divide by the original, 80.", "Dividió entre 60. Divida entre el original, 80."), "c": t("20 is the change in dollars.", "20 es el cambio en dólares."), "d": t("75% is what is left.", "75% es lo que queda.")}, "solution": t("−20 ÷ 80 = −0.25: 25% decrease.", "−20 ÷ 80 = −0.25: disminución del 25%.")},
      "D": {"ok": "c", "hints": {"a": t("$1,000 is the absolute change; it is only 5%.", "$1,000 es el cambio absoluto; es solo el 5%."), "b": t("Find each percent.", "Calcule cada porcentaje."), "d": t("You can tell: divide each change by its original value.", "Sí se puede saber: divida cada cambio entre su valor original.")}, "solution": t("Bread: 50%. Car: 5%.", "Pan: 50%. Auto: 5%.")},
      "E": {"ok": "b", "hints": {"a": t("The decrease is figured on $120.", "La rebaja se calcula sobre $120."), "c": t("First it goes up to $120.", "Primero sube a $120."), "d": t("It ends below $100.", "Termina por debajo de $100.")}, "solution": t("$100 × 1.20 = $120; $120 × 0.80 = $96.", "$100 × 1.20 = $120; $120 × 0.80 = $96.")},
      "F": {"ok": "d", "hints": {"a": t("0.12 gives only the change.", "0.12 da solo el cambio."), "b": t("0.88 is for a decrease.", "0.88 es para una disminución."), "c": t("Write the percent as a decimal.", "Escriba el porcentaje en decimal.")}, "solution": t("1 + 0.12 = 1.12.", "1 + 0.12 = 1.12.")},
      "G": {"ok": "a", "hints": {"b": t("$50 is only the increase.", "$50 es solo el aumento."), "c": t("You added 4 dollars, not 4%.", "Sumó 4 dólares, no 4%."), "d": t("It is an increase.", "Es un aumento.")}, "solution": t("1,250 × 1.04 = $1,300.", "1,250 × 1.04 = $1,300.")},
      "H": {"ok": "c", "hints": {"a": t("You divided by 2,300. Divide by 2,500.", "Dividió entre 2,300. Divida entre 2,500."), "b": t("200 is the change in people.", "200 es el cambio en personas."), "d": t("92% is what is left.", "92% es lo que queda.")}, "solution": t("−200 ÷ 2,500 = −0.08: 8% decrease.", "−200 ÷ 2,500 = −0.08: disminución del 8%.")}
     }}

    quiz = [
     ("A", t("A price goes from $40 to $52. What is the percent increase?", "Un precio pasa de $40 a $52. ¿Cuál es el porcentaje de aumento?"), [("a", "12%"), ("b", "23.1%"), ("c", "30%"), ("d", "52%")]),
     ("B", t("The temperature goes from 80 °F to 68 °F. What is the percent decrease?", "La temperatura pasa de 80 °F a 68 °F. ¿Cuál es el porcentaje de disminución?"), [("a", "15%"), ("b", "12%"), ("c", "17.6%"), ("d", "85%")]),
     ("C", t("A stock goes down from $80 to $60. What is the percent decrease?", "Una acción baja de $80 a $60. ¿Cuál es el porcentaje de disminución?"), [("a", "33.3%"), ("b", "25%"), ("c", "20%"), ("d", "75%")]),
     ("D", t("Bread goes from $2 to $3, and a car from $20,000 to $21,000. Which had the greater percent change?", "El pan pasa de $2 a $3 y un auto de $20,000 a $21,000. ¿Cuál tuvo el mayor cambio porcentual?"),
      [("a", t("The car", "El auto")), ("b", t("They are the same", "Son iguales")), ("c", t("The bread", "El pan")), ("d", t("You cannot tell", "No se puede saber"))]),
     ("E", t("A $100 price goes up 20% and then down 20%. What is the final price?", "Un precio de $100 sube 20% y luego baja 20%. ¿Cuál es el precio final?"), [("a", "$100"), ("b", "$96"), ("c", "$80"), ("d", "$104")]),
     ("F", t("What is the change factor for a 12% increase?", "¿Cuál es el factor de cambio para un aumento del 12%?"), [("a", "0.12"), ("b", "0.88"), ("c", "12"), ("d", "1.12")]),
     ("G", t("A $1,250 rent goes up 4%. What is the new rent?", "Un alquiler de $1,250 sube un 4%. ¿Cuál es el nuevo alquiler?"), [("a", "$1,300"), ("b", "$50"), ("c", "$1,254"), ("d", "$1,200")]),
     ("H", t("A town goes from 2,500 people to 2,300. What is the percent decrease?", "Un pueblo pasa de 2,500 habitantes a 2,300. ¿Cuál es el porcentaje de disminución?"), [("a", "8.7%"), ("b", "200%"), ("c", "8%"), ("d", "92%")])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("How much did it change? Percent increase and decrease, always compared with the original value, and the change factor.", "¿Cuánto cambió? El aumento y la disminución porcentual, siempre en relación con el valor original, y el factor de cambio."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Estimate</strong> the size of a change with benchmarks like 10% and 50%.", "<strong>Estimar</strong> el tamaño de un cambio con referencias como el 10% y el 50%."),
         t("<strong>Find</strong> the percent change, dividing by the original value.", "<strong>Calcular</strong> el cambio porcentual dividiendo entre el valor original."),
         t("<strong>Tell</strong> an increase from a decrease by the sign.", "<strong>Distinguir</strong> un aumento de una disminución por el signo."),
         t("<strong>Tell</strong> absolute change from relative change.", "<strong>Distinguir</strong> el cambio absoluto del relativo."),
         t("<strong>Use</strong> the change factor (1 + r) or (1 − r) to find the new value.", "<strong>Usar</strong> el factor de cambio (1 + r) o (1 − r) para hallar el valor nuevo.")],
        secciones,
        (t("Solve eight percent-change problems, four increases and four decreases, with prices, wages, and populations. Estimate before you calculate.",
           "Resuelva ocho ejercicios de cambio porcentual, cuatro de aumento y cuatro de disminución, con precios, salarios y poblaciones. Estime antes de calcular."),
         t("Find a real change (the price of something you buy every week, a bus fare, an electric bill). Find its percent change and decide if the change is large or small compared with the original value. Check your answer on the practice page.",
           "Busque un cambio real (el precio de algo que compra cada semana, una tarifa de transporte, un recibo de luz). Calcule su cambio porcentual y decida si es grande o pequeño en relación con el valor original. Compruebe el resultado en la página de práctica.")),
        quiz,
        t("Self-check checklist for percent change", "Lista de autoevaluación del cambio porcentual"),
        t("Self-check checklist: skills for percent change", "Lista de autoevaluación: destrezas del cambio porcentual"),
        [(t("Use the original value", "Usar el valor original"), t("I always divide by the original value and can explain why.", "Siempre divido entre el valor original y sé explicar por qué."), t("I find the original value with help.", "Identifico el original con apoyo."), t("I divide by the new value or by the difference.", "Divido entre el valor nuevo o entre la diferencia.")),
         (t("Find the change", "Calcular el cambio"), t("I find new − original with the right sign and estimate first.", "Calculo nuevo − original con el signo correcto y estimo antes."), t("I find the change with sign mistakes.", "Calculo el cambio con errores de signo."), t("I subtract in the wrong order.", "Resto en el orden incorrecto.")),
         (t("Answer and context", "Resultado y contexto"), t("I say whether it is an increase or a decrease and tell absolute from relative change.", "Digo si es aumento o disminución y distingo el cambio absoluto del relativo."), t("I give the percent without saying if it went up or down.", "Doy el porcentaje sin decir si subió o bajó."), t("I do not give the answer as a percent.", "No expreso el resultado como porcentaje."))],
        t("<p>In this lesson you learned to measure <strong>percent change</strong>, always compared with the <strong>original value</strong>, and to tell absolute change from relative change. You also met the <strong>change factor</strong>: multiply by (1 + r) to increase and by (1 − r) to decrease.</p>\n<p>In <strong>Lesson 5.3 · Discount, tax, tip, and mixed applications</strong> you will use that factor in daily life: the sale price in a store, the sales tax on a receipt, and the tip at a restaurant, including problems where several percents come together in one purchase.</p>",
          "<p>En esta lección aprendió a medir el <strong>cambio porcentual</strong>, siempre en relación con el <strong>valor original</strong>, y a distinguir el cambio absoluto del relativo. También conoció el <strong>factor de cambio</strong>: multiplicar por (1 + r) para aumentar y por (1 − r) para disminuir.</p>\n<p>En la <strong>Lección 5.3 · Descuento, impuesto, propina y aplicaciones mixtas</strong> usará ese factor en la vida diaria: el precio rebajado de una tienda, el impuesto sobre la venta de un recibo y la propina de un restaurante, incluidos los casos en que se combinan varios porcentajes en una misma compra.</p>"),
        ("5-3", ("", t("Lesson 5.3 · Discount, tax, tip, and mixed applications", "Lección 5.3 · Descuento, impuesto, propina y aplicaciones mixtas"))),
        [(t("percent change", "cambio porcentual"), t("(new − original) ÷ original × 100.", "(nuevo − original) ÷ original × 100.")),
         (t("absolute change", "cambio absoluto"), t("How many units something changed: new − original.", "Cuántas unidades cambió algo: nuevo − original.")),
         (t("relative change", "cambio relativo"), t("The change compared with the original value, as a percent.", "El cambio comparado con el valor original, en porcentaje.")),
         (t("change factor", "factor de cambio"), t("The number you multiply by: 1 + r for an increase, 1 − r for a decrease.", "El número por el que se multiplica: 1 + r para aumentar, 1 − r para disminuir."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "diez": "10% of {o} is {d} (move the decimal point one place).", "arriba": " up", "abajo": " down",
  "cambioEs": "The change is {c}{s}, which is {e}.", "menos10": "less than 10%", "veces": "about {k} times 10%: around {p}",
  "exacto": "Exact: {d} ÷ {o} × 100 = {r}", "sinCambio": "0%", "aum": "an increase of ", "dis": "a decrease of ",
  "ctxE": ["A price", "A rent", "An electric bill", "A bus fare", "A weekly paycheck"], "pasa": "{c} goes from {o} to {n}. Without doing the exact math, how big is {x}?",
  "elAum": "the increase", "laDis": "the decrease", "alrededor": "About {r}%",
  "expE": "10% of {o} is {d}. The change is {c}, about {k} times 10%: close to {r}%. (Exact: {x}.)",
  "antes": "Before", "despues": "After", "barrasVoz": "Bars for the starting value, {i}, and the ending value, {f}.",
  "cambio": "Change: {f} − {i} = {d}. Divide by the <strong>starting</strong> value: {d} ÷ {i} = {q}.",
  "noHubo": "No change: 0%.", "aumento": "Increase", "disminucion": "Decrease", "de": " of ",
  "sb1": "Start with $100. It goes up {p}%: 100 × {f} = {a}.", "sb2": "It goes down {p}%, but on {a}: {a2} × {g} = {b}.", "sb3": "It does not go back to $100: it ends at {b}. Each change is figured on the value at that moment.",
  "subeObj": ["A coffee", "A bike rental", "A movie ticket", "A train ticket"], "bajaObj": ["A shirt on sale", "A pair of shoes on sale", "A used book", "A blender on clearance"],
  "pasoDe": "{o} went from {i} to {f}. What was the percent {x}?", "aumentoW": "increase", "descuentoW": "decrease",
  "solC": "Change: {d}. {d2} ÷ {i} = {q}, and × 100 = {p}%.", "divFinal": "You divided by the ending value. Divide the change by the starting value.", "enDolares": "That is the change in dollars. Divide it by the starting value and multiply by 100.",
  "items": ["Lunch", "Shoes", "Bicycle"], "arCap": "The same increase of {d} on different original values",
  "arCab": ["Item", "Original", "New", "Absolute change", "Percent change"], "arNota": "The absolute change is the same for all three, but the percent change is not: {d} weighs a lot on $10.00 and almost nothing on $200.00.",
  "A": ["Bread", "A coffee", "A bus fare", "A pound of tomatoes"], "Bn": ["A used car", "A computer", "A sofa", "A TV"],
  "sube": "{n} goes up from {o} to {f}. ", "masPct": "Which one had the greater <strong>percent</strong> change?", "masDol": "Which one had the greater change <strong>in dollars</strong>?",
  "igual": "They both changed the same", "masDolNo": "{n} went up more dollars ({d}), but compared with its price it is small.", "relMayor": " The relative change is greater for {n}.",
  "pctSi": "In percent it did go up more, but the question asks about dollars.", "enDol": "In dollars: {a} compared with {b}. ",
  "escribeOrig": "Type an original value (a positive number).",
  "factorEs": "<strong>Factor:</strong> 1 {s} {r} = <strong>{f}</strong> ({x}).", "factorSube": "the new value is {p}% of the original", "factorBaja": "{p}% of the original is left",
  "conFactor": "<strong>With the factor:</strong> {o} × {f} = {n}.", "conCambio": "<strong>Finding the change:</strong> {o} × {r} = {c}; {o} {s} {c2} = {n}.", "dosCaminos": "Both ways give {n}.",
  "porQue": "What number do you multiply a value by to {x} it by {p}%?", "aumentar": "increase", "disminuir": "decrease",
  "fSube": "You pay 100% plus {p}%: 1 + {r} = {f}.", "fBaja": "{q}% is left: 1 − {r} = {f}.",
  "soloCambio": "That number gives only the change, not the new value.", "suma": "To increase, add: 1 + r.", "resta": "To decrease, subtract: 1 − r.", "enDecimal": "Write the percent as a decimal: {p}% = {r}.",
  "ctxSube": ["A rent of {o} goes up {p}%.", "A wage of {o} goes up {p}%.", "A fee of {o} goes up {p}%."], "ctxBaja": ["A coat that costs {o} goes down {p}%.", "A computer worth {o} loses {p}% of its value.", "A bill of {o} goes down {p}%."],
  "usaFactor": " Use the change factor: what is the new value?", "solF": "Factor: {f}. {o} × {f} = {n}.",
  "soloEl": "That is only the change. You still need to {x} the original value, or multiply by {f}.", "sumarlo": "add it to", "restarlo": "subtract it from",
  "esAum": "It is an increase: the factor is greater than 1.", "esDis": "It is a decrease: the factor is less than 1."
 },
 "es": {
  "diez": "El 10% de {o} es {d} (el punto se mueve un lugar).", "arriba": " hacia arriba", "abajo": " hacia abajo",
  "cambioEs": "El cambio es de {c}{s}, que es {e}.", "menos10": "menos que el 10%", "veces": "unas {k} veces el 10%: alrededor del {p}",
  "exacto": "Cálculo exacto: {d} ÷ {o} × 100 = {r}", "sinCambio": "0%", "aum": "aumento del ", "dis": "disminución del ",
  "ctxE": ["Un precio", "Un alquiler", "Una factura de luz", "El boleto de autobús", "Un salario semanal"], "pasa": "{c} pasa de {o} a {n}. Sin hacer la cuenta exacta, ¿de qué tamaño es {x}?",
  "elAum": "el aumento", "laDis": "la disminución", "alrededor": "Alrededor del {r}%",
  "expE": "El 10% de {o} es {d}. El cambio es de {c}, unas {k} veces el 10%: cerca del {r}%. (Exacto: {x}.)",
  "antes": "Antes", "despues": "Después", "barrasVoz": "Barras del valor inicial, {i}, y del final, {f}.",
  "cambio": "Cambio: {f} − {i} = {d}. Se divide entre el valor <strong>inicial</strong>: {d} ÷ {i} = {q}.",
  "noHubo": "No hubo cambio: 0%.", "aumento": "Aumento", "disminucion": "Disminución", "de": " del ",
  "sb1": "Se empieza con $100. Sube {p}%: 100 × {f} = {a}.", "sb2": "Baja {p}%, pero sobre {a}: {a2} × {g} = {b}.", "sb3": "No vuelve a $100: queda en {b}. Cada cambio se calcula sobre el valor de ese momento.",
  "subeObj": ["Un café", "El alquiler de una bicicleta", "Una entrada al cine", "Un boleto de tren"], "bajaObj": ["Una camisa rebajada", "Un par de zapatos en oferta", "Un libro usado", "Una licuadora en liquidación"],
  "pasoDe": "{o} pasó de {i} a {f}. ¿De qué porcentaje fue {x}?", "aumentoW": "el aumento", "descuentoW": "la disminución",
  "solC": "Cambio: {d}. {d2} ÷ {i} = {q}, y × 100 = {p}%.", "divFinal": "Se dividió entre el valor final. El cambio se divide entre el valor inicial.", "enDolares": "Ese es el cambio en dólares. Falta dividir entre el valor inicial y multiplicar por 100.",
  "items": ["Almuerzo", "Zapatos", "Bicicleta"], "arCap": "El mismo aumento de {d} sobre valores originales distintos",
  "arCab": ["Artículo", "Original", "Nuevo", "Cambio absoluto", "Cambio porcentual"], "arNota": "El cambio absoluto es el mismo en los tres, pero el porcentual no: {d} pesa mucho sobre $10.00 y casi nada sobre $200.00.",
  "A": ["El pan", "Un café", "El pasaje de autobús", "Una libra de tomates"], "Bn": ["Un carro usado", "Una computadora", "Un sofá", "Un televisor"],
  "sube": "{n} sube de {o} a {f}. ", "masPct": "¿Cuál tuvo el mayor cambio <strong>porcentual</strong>?", "masDol": "¿Cuál tuvo el mayor cambio <strong>en dólares</strong>?",
  "igual": "Los dos cambiaron lo mismo", "masDolNo": "{n} subió más dólares ({d}), pero comparado con su precio es poco.", "relMayor": " El cambio relativo es mayor en {n}.",
  "pctSi": "En porcentaje sí subió más, pero se pregunta por los dólares.", "enDol": "En dólares: {a} frente a {b}. ",
  "escribeOrig": "Escriba un valor original (un número positivo).",
  "factorEs": "<strong>Factor:</strong> 1 {s} {r} = <strong>{f}</strong> ({x}).", "factorSube": "el valor nuevo es el {p}% del original", "factorBaja": "queda el {p}% del original",
  "conFactor": "<strong>Con el factor:</strong> {o} × {f} = {n}.", "conCambio": "<strong>Calculando el cambio:</strong> {o} × {r} = {c}; {o} {s} {c2} = {n}.", "dosCaminos": "Los dos caminos dan {n}.",
  "porQue": "¿Por qué número se multiplica un valor para {x}lo un {p}%?", "aumentar": "aumentar", "disminuir": "disminuir",
  "fSube": "Se paga el 100% más el {p}%: 1 + {r} = {f}.", "fBaja": "Queda el {q}%: 1 − {r} = {f}.",
  "soloCambio": "Ese número da solo el cambio, no el valor nuevo.", "suma": "Para aumentar se suma: 1 + r.", "resta": "Para disminuir se resta: 1 − r.", "enDecimal": "El porcentaje va en decimal: {p}% = {r}.",
  "ctxSube": ["Un alquiler de {o} aumenta un {p}%.", "Un salario de {o} sube un {p}%.", "Una tarifa de {o} se encarece un {p}%."], "ctxBaja": ["Un abrigo de {o} baja un {p}%.", "Una computadora de {o} pierde el {p}% de su valor.", "Una factura de {o} se reduce un {p}%."],
  "usaFactor": " Use el factor de cambio: ¿cuál es el valor nuevo?", "solF": "Factor: {f}. {o} × {f} = {n}.",
  "soloEl": "Ese es solo el cambio. Falta {x} valor original, o multiplicar por {f}.", "sumarlo": "sumarlo al", "restarlo": "restarlo del",
  "esAum": "Es un aumento: el factor es mayor que 1.", "esDis": "Es una disminución: el factor es menor que 1."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function pc(x){ return nd(Math.round(x * 1000) / 1000) + "%"; }
function sinPct(t){ return String(t).replace(/%/g, ""); }

/* ============ MODULE 1 · estimate ============ */
function pintaES(){
  var o = +$("es-o").value, n = +$("es-n").value, d = n - o, diez = o / 10, k = Math.abs(d) / diez, c = d / o * 100, kk = Math.round(k * 2) / 2;
  $("es-ov").textContent = dinero(o); $("es-nv").textContent = dinero(n);
  var est = k < 0.75 ? TXT.menos10 : F(TXT.veces, { k: nd(kk), p: pc(kk * 10) });
  $("es-salida").innerHTML = '<div class="linea">' + F(TXT.diez, { o: dinero(o), d: dinero(diez) }) + '</div>' +
    '<div class="linea">' + F(TXT.cambioEs, { c: dinero(Math.abs(d)), s: d >= 0 ? TXT.arriba : TXT.abajo, e: est }) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.exacto, { d: nd(d), o: o, r: d === 0 ? TXT.sinCambio : (d > 0 ? TXT.aum : TXT.dis) + pc(Math.abs(Math.round(c * 10) / 10)) }) + '</div>';
}
var REFS = [5, 10, 25, 50, 100];
function genEstimar(){
  for (var z = 0; z < 300; z++){
    var ref = elige(REFS), o = 10 * aleatorio(3, 40), sube = ref === 100 ? true : Math.random() < 0.6;
    var ruido = 1 + (Math.random() - 0.5) * 0.16, cambio = Math.round(o * ref / 100 * ruido), n = sube ? o + cambio : o - cambio;
    if (n <= 0 || cambio === 0) continue;
    var real = Math.abs(n - o) / o * 100, orden = REFS.slice().sort(function(a, b){ return Math.abs(Math.log(a / real)) - Math.abs(Math.log(b / real)); });
    if (orden[0] !== ref || Math.abs(Math.log(orden[1] / real)) - Math.abs(Math.log(ref / real)) < 0.35) continue;
    var exp = F(TXT.expE, { o: dinero(o), d: dinero(o / 10), c: dinero(Math.abs(n - o)), k: nd(Math.round(Math.abs(n - o) / (o / 10) * 10) / 10), r: ref, x: pc(Math.round(real * 10) / 10) });
    return { enun: F(TXT.pasa, { c: elige(TXT.ctxE), o: dinero(o), n: dinero(n), x: sube ? TXT.elAum : TXT.laDis }),
      opciones: REFS.map(function(r){ return { html: F(TXT.alrededor, { r: r }), clave: "r" + r }; }), enOrden: true, correcta: "r" + ref, bien: exp, mal: exp };
  }
}

/* ============ MODULE 2 · percent change ============ */
function pintaCP(){
  var i = +$("cp-i").value, f = +$("cp-f").value, d = f - i, c = d / i * 100;
  $("cp-iv").textContent = dinero(i); $("cp-fv").textContent = dinero(f);
  var esc = 480 / Math.max(i, f);
  var s = '<svg class="figura" viewBox="0 0 640 110" role="img" aria-label="' + F(TXT.barrasVoz, { i: dinero(i), f: dinero(f) }) + '">';
  s += '<text x="10" y="35" font-size="14" font-weight="700" fill="#263238">' + TXT.antes + '</text><rect x="90" y="16" width="' + f1(i * esc) + '" height="28" fill="#ffb74d"/><text x="' + f1(98 + i * esc) + '" y="35" font-size="14" font-weight="700" fill="#263238">' + dinero(i) + '</text>';
  s += '<text x="10" y="85" font-size="14" font-weight="700" fill="#263238">' + TXT.despues + '</text><rect x="90" y="66" width="' + f1(f * esc) + '" height="28" fill="' + (d >= 0 ? "#2e7d32" : "#c62828") + '"/><text x="' + f1(98 + f * esc) + '" y="85" font-size="14" font-weight="700" fill="#263238">' + dinero(f) + '</text>';
  $("cp-svg").innerHTML = s + '</svg>';
  $("cp-salida").innerHTML = '<div class="linea">' + F(TXT.cambio, { f: f, i: i, d: nd(d), q: nd(Math.round(d / i * 10000) / 10000) }) + '</div>' +
    '<div class="linea veredicto">' + (d === 0 ? TXT.noHubo : (d > 0 ? TXT.aumento : TXT.disminucion) + TXT.de + (Math.abs(c - Math.round(c * 10) / 10) > 1e-9 ? "≈ " : "") + pc(Math.abs(Math.round(c * 10) / 10))) + '</div>';
}
function pintaSB(){
  var p = +$("sb-p").value, a = 100 * (1 + p / 100), b = a * (1 - p / 100);
  $("sb-pv").textContent = p + "%";
  $("sb-salida").innerHTML = '<div class="linea">' + F(TXT.sb1, { p: p, f: nd(1 + p / 100), a: dinero(a) }) + '</div><div class="linea">' + F(TXT.sb2, { p: p, a: dinero(a), a2: nd(a), g: nd(1 - p / 100), b: dinero(b) }) + '</div><div class="linea veredicto">' + F(TXT.sb3, { b: dinero(b) }) + '</div>';
}
function genCambio(){
  for (var z = 0; z < 100; z++){
    var ini = elige([20, 25, 40, 50, 60, 80, 120, 200, 250]), p = elige([5, 10, 15, 20, 25, 30, 40, 50]), sube = Math.random() < 0.5, fin = ini * (1 + (sube ? 1 : -1) * p / 100);
    if (fin !== Math.round(fin * 100) / 100) continue;
    var d = Math.abs(fin - ini), pist = [{ v: Math.round(d / fin * 1000) / 10, msg: TXT.divFinal }, { v: d, msg: TXT.enDolares }].filter(function(x){ return Math.abs(x.v - p) > 0.05; });
    var ev = numD(p, pist, null, 0.051);
    return { enun: F(TXT.pasoDe, { o: elige(sube ? TXT.subeObj : TXT.bajaObj), i: dinero(ini), f: dinero(fin), x: sube ? TXT.aumentoW : TXT.descuentoW }), correcta: p + "%",
      solucion: F(TXT.solC, { d: dinero(d), d2: nd(d), i: ini, q: nd(d / ini), p: p }), evalua: function(s){ return ev(sinPct(s).replace(/^\s*[−-]/, "")); } };
  }
}

/* ============ MODULE 3 · absolute and relative ============ */
function pintaAR(){
  var d = +$("ar-d").value, bases = [10, 50, 200]; $("ar-dv").textContent = dinero(d);
  $("ar-tabla").innerHTML = '<div class="tabla-scroll"><table class="reglas"><caption>' + F(TXT.arCap, { d: dinero(d) }) + '</caption><thead><tr>' + TXT.arCab.map(function(c){ return '<th scope="col">' + c + '</th>'; }).join("") + '</tr></thead><tbody>' +
    bases.map(function(b, i){ return '<tr><td>' + TXT.items[i] + '</td><td>' + dinero(b) + '</td><td>' + dinero(b + d) + '</td><td>' + dinero(d) + '</td><td><strong>' + pc(Math.round(d / b * 1000) / 10) + '</strong></td></tr>'; }).join("") + '</tbody></table></div>' +
    '<div class="salida"><div class="linea">' + F(TXT.arNota, { d: dinero(d) }) + '</div></div>';
}
function genAbsRel(){
  for (var z = 0; z < 300; z++){
    var A = { n: elige(TXT.A), o: aleatorio(2, 12) }, Bb = { n: elige(TXT.Bn), o: 100 * aleatorio(3, 150) };
    A.d = aleatorio(1, Math.max(1, Math.floor(A.o / 2))); Bb.d = 10 * aleatorio(Math.ceil(A.d / 10) + 1, Math.max(3, Math.floor(Bb.o / 40)));
    if (Bb.d <= A.d) continue;
    A.p = A.d / A.o * 100; Bb.p = Bb.d / Bb.o * 100;
    if (!(A.p > Bb.p * 1.5)) continue;
    var rel = Math.random() < 0.75;
    var txt = F(TXT.sube, { n: A.n, o: dinero(A.o), f: dinero(A.o + A.d) }) + F(TXT.sube, { n: Bb.n, o: dinero(Bb.o), f: dinero(Bb.o + Bb.d) });
    var exp = A.n + ": " + dinero(A.d) + " ÷ " + dinero(A.o) + " = " + pc(Math.round(A.p * 10) / 10) + ". " + Bb.n + ": " + dinero(Bb.d) + " ÷ " + dinero(Bb.o) + " = " + pc(Math.round(Bb.p * 10) / 10) + ".";
    var q = { enun: txt + (rel ? TXT.masPct : TXT.masDol), enOrden: true, pistas: {}, opciones: [{ html: A.n, clave: "A" }, { html: Bb.n, clave: "B" }, { html: TXT.igual, clave: "igual" }] };
    if (rel){ q.correcta = "A"; q.pistas.B = F(TXT.masDolNo, { n: Bb.n, d: dinero(Bb.d) }); q.bien = q.mal = exp + F(TXT.relMayor, { n: A.n }); }
    else { q.correcta = "B"; q.pistas.A = TXT.pctSi; q.bien = q.mal = F(TXT.enDol, { a: dinero(A.d), b: dinero(Bb.d) }) + exp; }
    return q;
  }
}

/* ============ MODULE 4 · the change factor ============ */
var SENTIDO = 1;
function pintaFA(){
  var o = leeD($("fa-o").value), p = +$("fa-p").value, s = $("fa-salida");
  $("fa-pv").textContent = p + "%";
  document.querySelectorAll("#fa-botones .eleccion").forEach(function(b){ b.setAttribute("aria-pressed", +b.getAttribute("data-sentido") === SENTIDO ? "true" : "false"); });
  $("fa-o").classList.toggle("error", o === null || o < 0);
  if (o === null || o < 0){ s.innerHTML = '<div class="linea">' + TXT.escribeOrig + '</div>'; return; }
  var f = Math.round((1 + SENTIDO * p / 100) * 10000) / 10000, c = o * p / 100, n = o * f;
  s.innerHTML = '<div class="linea">' + F(TXT.factorEs, { s: SENTIDO > 0 ? "+" : "−", r: nd(p / 100), f: nd(f), x: SENTIDO > 0 ? F(TXT.factorSube, { p: 100 + p }) : F(TXT.factorBaja, { p: 100 - p }) }) + '</div>' +
    '<div class="linea">' + F(TXT.conFactor, { o: nd(o), f: nd(f), n: dinero(n) }) + '</div>' +
    '<div class="linea">' + F(TXT.conCambio, { o: nd(o), r: nd(p / 100), c: dinero(c), s: SENTIDO > 0 ? "+" : "−", c2: nd(Math.round(c * 100) / 100), n: dinero(n) }) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.dosCaminos, { n: dinero(n) }) + '</div>';
}
function genFactor(){
  var tp = aleatorio(1, 3), p = elige([3, 4, 5, 8, 10, 12, 15, 20, 25, 30, 35, 40]), sube = Math.random() < 0.5, fr_ = Math.round((1 + (sube ? 1 : -1) * p / 100) * 100) / 100, r = nd(p / 100);
  if (tp === 1){
    var otro = Math.round((1 - (sube ? 1 : -1) * p / 100) * 100) / 100;
    return { enun: F(TXT.porQue, { x: sube ? TXT.aumentar : TXT.disminuir, p: p }), correcta: nd(fr_),
      solucion: sube ? F(TXT.fSube, { p: p, r: r, f: nd(fr_) }) : F(TXT.fBaja, { q: 100 - p, r: r, f: nd(fr_) }),
      evalua: numD(fr_, [{ v: p / 100, msg: TXT.soloCambio }, { v: otro, msg: sube ? TXT.suma : TXT.resta }, { v: p, msg: F(TXT.enDecimal, { p: p, r: r }) }], null, 0.0001) };
  }
  var o = elige([40, 60, 80, 120, 250, 500, 800, 1250, 1500, 2000, 36, 75]), n = Math.round(o * fr_ * 100) / 100;
  var ctx = F(elige(sube ? TXT.ctxSube : TXT.ctxBaja), { o: dinero(o), p: p });
  return { enun: ctx + TXT.usaFactor, correcta: dinero(n), solucion: F(TXT.solF, { f: nd(fr_), o: nd(o), n: dinero(n) }),
    evalua: numD(n, [{ v: Math.round(o * p) / 100, msg: F(TXT.soloEl, { x: sube ? TXT.sumarlo : TXT.restarlo, f: nd(fr_) }) }, { v: Math.round(o * (1 - (sube ? 1 : -1) * p / 100) * 100) / 100, msg: sube ? TXT.esAum : TXT.esDis }]) };
}

/* ============ Start ============ */
["es-o", "es-n"].forEach(function(id){ $(id).addEventListener("input", pintaES); }); pintaES();
creaPracticaOM("p1", genEstimar);
["cp-i", "cp-f"].forEach(function(id){ $(id).addEventListener("input", pintaCP); }); pintaCP();
$("sb-p").addEventListener("input", pintaSB); pintaSB();
creaPracticaLibre("p2", genCambio);
$("ar-d").addEventListener("input", pintaAR); pintaAR();
creaPracticaOM("p3", genAbsRel);
document.querySelectorAll("#fa-botones .eleccion").forEach(function(b){ b.addEventListener("click", function(){ SENTIDO = +b.getAttribute("data-sentido"); pintaFA(); }); });
$("fa-o").addEventListener("input", pintaFA); $("fa-p").addEventListener("input", pintaFA); pintaFA();
creaPracticaLibre("p4", genFactor);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    frm = '<span class="fracc"><span class="fa">{}</span><span class="fb2">{}</span></span>'
    mods = [
     (t("estimate", "estimar"), t("Estimate before you calculate", "Antes de calcular, estimar"),
      f'''      <p>{t("A good habit is to <strong>estimate</strong> first whether the change is large or small compared with the starting value. That way you spot silly answers right away.", "Un buen hábito es <strong>estimar</strong> primero si el cambio es grande o pequeño comparado con el valor de partida. Así se detectan de inmediato los resultados absurdos.")}</p>
      <div class="caja-tip"><strong>{t("Benchmarks:", "Referencias:")}</strong> {t("10% moves the decimal point one place to the left; 50% is half; 100% means the amount doubled.", "el 10% mueve el punto un lugar a la izquierda; el 50% es la mitad; el 100% quiere decir que la cantidad se duplicó.")}</div>
      <h3>{t("Estimate with 10%", "Estime con el 10%")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("es-o", t("Original value", "Valor original"), 20, 400, 40, 10)}
          {desl("es-n", t("New value", "Valor nuevo"), 5, 800, 52)}
        </div>
        <div class="salida" id="es-salida" aria-live="polite"></div>
      </div>
{B.om("p1", t("Practice: how big is the change?", "Practique: ¿de qué tamaño es el cambio?"))}'''),
     (t("change", "cambio"), t("Percent change", "Cambio porcentual"),
      f'''      <p>{t("Percent change tells how much a quantity grew or shrank, as a percent <strong>of the starting value</strong>.", "El cambio porcentual dice cuánto creció o disminuyó una cantidad, en porcentaje <strong>del valor inicial</strong>.")}</p>
      <div class="formula">{t("% change", "% de cambio")} = {frm.format(t("ending value − starting value", "valor final − valor inicial"), t("starting value", "valor inicial"))} × 100</div>
      <h3>{t("Before and after", "Antes y después")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("cp-i", t("Starting value", "Valor inicial"), 10, 200, 40, 5)}
          {desl("cp-f", t("Ending value", "Valor final"), 5, 300, 34)}
        </div>
        <div id="cp-svg"></div>
        <div class="salida" id="cp-salida" aria-live="polite"></div>
      </div>
      <h3>{t("Does going up 10% and down 10% leave things the same?", "¿Subir 10% y bajar 10% deja todo igual?")}</h3>
      <div class="panel">
        <div class="campos">{desl("sb-p", t("Percent up and then down", "Porcentaje que sube y después baja"), 5, 50, 10, 5)}</div>
        <div class="salida" id="sb-salida" aria-live="polite"></div>
      </div>
{libre_x("p2", t("Practice: percent change", "Practique: cambio porcentual"), t("Percent", "Porcentaje"), t("Type only the number, with no % sign. It may have decimals.", "Escriba solo el número, sin el signo %. Puede llevar decimales."))}'''),
     (t("absolute-relative", "absoluto-relativo"), t("Absolute change and relative change", "Cambio absoluto y cambio relativo"),
      f'''      <p>{t("The <strong>absolute change</strong> tells how many units something changed; the <strong>relative change</strong> (the percent) tells how big that change is compared with the starting point.", "El <strong>cambio absoluto</strong> dice cuántas unidades cambió algo; el <strong>cambio relativo</strong> (el porcentual) dice cuánto representa ese cambio comparado con el punto de partida.")}</p>
      <h3>{t("The same increase on different prices", "El mismo aumento sobre precios distintos")}</h3>
      <div class="panel">
        <div class="campos">{desl("ar-d", t("Increase in dollars", "Aumento en dólares"), 1, 20, 5)}</div>
        <div id="ar-tabla"></div>
      </div>
{B.om("p3", t("Practice: which one changed more?", "Practique: ¿cuál cambió más?"))}'''),
     (t("factor", "factor"), t("The change factor", "El factor de cambio"),
      f'''      <p>{t("If you know the percent and want the new value, you can find the change and add or subtract it, or multiply right away by the <strong>change factor</strong>: (1 + r) to increase, (1 − r) to decrease.", "Si se conoce el porcentaje y se quiere el valor nuevo, se puede calcular el cambio y sumarlo o restarlo, o multiplicar directamente por el <strong>factor de cambio</strong>: (1 + r) para aumentar, (1 − r) para disminuir.")}</p>
      <h3>{t("Try the factor", "Pruebe el factor")}</h3>
      <div class="panel">
        <div class="elecciones" id="fa-botones" role="group" aria-label="{t("Increase or decrease", "Aumento o disminución")}">
          <button type="button" class="eleccion" data-sentido="1" aria-pressed="true">{t("Increase", "Aumento")}</button>
          <button type="button" class="eleccion" data-sentido="-1" aria-pressed="false">{t("Decrease", "Disminución")}</button>
        </div>
        <div class="campos">
          <div class="campo"><label for="fa-o">{t("Original value ($)", "Valor original ($)")}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="fa-o" value="1250"></div>
          {desl("fa-p", t("Percent", "Porcentaje"), 1, 60, 4)}
        </div>
        <div class="salida" id="fa-salida" aria-live="polite"></div>
      </div>
{libre_x("p4", t("Practice: with the change factor", "Practique: con el factor de cambio"), t("Answer", "Resultado"), t("Type only the number. It may have decimals, like 1.12; for money you may use the $ sign.", "Escriba solo el número. Puede llevar decimales, como 1.12; si es dinero, puede usar el signo $."))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Cambio porcentual: aumento y disminución")
