"""Level 2 · Lesson 5.3 · Discount, tax, tip, and mixed applications — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla

B.NIVEL = 2
N = "5-3"
TEMA = ("Percents", "Porcentajes")
TIT = ("Discount, tax, tip, and mixed applications", "Descuento, impuesto, propina y aplicaciones mixtas")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def recibo():
    def l(a, b, neg=False, bold=False):
        w = "font-weight:700;" if bold else ""
        return f'<div style="display:flex;justify-content:space-between;gap:10px;{w}"><span>{a}</span><span>{b}</span></div>'
    sep = '<div style="border-top:1px dashed #8d6e63;margin:6px 0"></div>'
    return ('<div role="group" aria-label="' + t("A sample store receipt", "Un recibo de tienda simulado") + '" style="font-family:Consolas,\'Courier New\',monospace;background:#fffdf7;border:1px dashed #8d6e63;max-width:380px;margin:14px auto;padding:14px 18px;font-size:15px">'
            f'<div style="text-align:center;font-weight:700;margin-bottom:8px">{t("SAVE-MORE STORE", "TIENDA EL AHORRO")}</div>'
            + l(t("Jacket", "Chaqueta"), "$60.00") + l(t("Discount 25%", "Descuento 25%"), "−$15.00") + l(t("T-shirt", "Camiseta"), "$12.00") + sep
            + l("Subtotal", "$57.00") + l(t("Tax 8.25%", "Impuesto 8.25%"), "$4.70") + sep + l("TOTAL", "$61.70", bold=True) + "</div>")

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 5.2 you met the change factor: multiply by (1 + r) to increase and by (1 − r) to decrease. This lesson, which closes Topic 5, uses it in the three most common percent situations in daily life: <strong>discounts</strong>, <strong>sales tax</strong>, and <strong>tips</strong>, and in the cases where they come together.", "En la Lección 5.2 apareció el factor de cambio: multiplicar por (1 + r) para aumentar y por (1 − r) para disminuir. Esta lección, que cierra el Tema 5, lo aplica a las tres situaciones de porcentaje más comunes en la vida diaria: el <strong>descuento</strong>, el <strong>impuesto sobre la venta</strong> y la <strong>propina</strong>, y a los casos en que se combinan.")}</p>
<p>{t("Before learning the steps, look at a receipt and check its numbers. This receipt is made up:", "Antes de aprender el procedimiento, conviene mirar un recibo y comprobar sus números. Este es un recibo simulado:")}</p>
{recibo()}
<p>{t("How was each line found? 25% of $60 is $15. The subtotal is 60 − 15 + 12 = $57. The tax is 8.25% of 57 = 4.7025, which rounds to <strong>$4.70</strong>. The total is 57 + 4.70 = $61.70.", "¿Cómo se obtuvo cada línea? El 25% de $60 es $15. El subtotal es 60 − 15 + 12 = $57. El impuesto es el 8.25% de 57 = 4.7025, que se redondea a <strong>$4.70</strong>. El total es 57 + 4.70 = $61.70.")}</p>
{caja("tip", t("About rounding", "Sobre el redondeo"), t("<p>Money is written with two decimal places (cents). Round at the end of each calculation, not in the middle steps. If the third decimal digit is 5 or more, round up one cent.</p>", "<p>El dinero se expresa con dos decimales (centavos). Se redondea al final de cada cálculo, no en los pasos intermedios. Si la tercera cifra decimal es 5 o más, se sube un centavo.</p>"))}
{caja("ojo", t("The tax rate depends on where you are", "La tasa de impuesto cambia según el lugar"), t("<p>Each state, county, and city sets its own rate, and it can change from year to year or by type of product. This lesson uses made-up rates; in real life, the rate is printed on the receipt.</p>", "<p>Cada estado, condado y ciudad fija la suya, y puede variar de un año a otro o según el tipo de producto. En esta lección se usan tasas supuestas; en la vida real, la tasa aplicada aparece impresa en el recibo.</p>"))}'''

    s2 = f'''<p>{t("A <strong>discount</strong> takes a percent off the original price. There are two ways that give the same answer.", "Un <strong>descuento</strong> resta un porcentaje del precio original. Hay dos caminos equivalentes.")}</p>
{ej(t("Example: two methods", "Ejemplo: dos métodos"), t("A pair of shoes costs $85 and has a 20% discount. What is the final price?", "Unos zapatos cuestan $85 y tienen un descuento del 20%. ¿Cuál es el precio final?"),
  [("A", t("Find it and subtract.", "Calcular y restar."), t("Discount = 0.20 × 85 = $17; final price = 85 − 17 = $68.", "Descuento = 0.20 × 85 = $17; precio final = 85 − 17 = $68.")),
   ("B", t("Change factor.", "Factor de cambio."), t("With 20% off, you pay 80%: 85 × 0.80 = $68.", "Si se descuenta el 20%, se paga el 80%: 85 × 0.80 = $68.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>$68</strong>")])}
{tabla(t("Common discounts", "Descuentos frecuentes"), t("Common discounts and the factor you multiply the price by", "Descuentos frecuentes y el factor por el que se multiplica el precio"),
       [t("Discount", "Descuento"), t("You pay", "Se paga"), t("Factor", "Factor"), t("A $40 price becomes", "Un precio de $40 queda en")],
       [["10%", "90%", "× 0.90", "$36"], ["20%", "80%", "× 0.80", "$32"], ["25%", "75%", "× 0.75", "$30"], ["30%", "70%", "× 0.70", "$28"], ["50%", "50%", "× 0.50", "$20"]])}
<h3>{t("Sales tax", "Impuesto sobre la venta")}</h3>
<p>{t("Tax <strong>adds</strong> a percent to the price. With the change factor: final price = price × (1 + rate).", "El impuesto <strong>suma</strong> un porcentaje al precio. Con el factor de cambio: precio final = precio × (1 + tasa).")}</p>
{ej(t("Example: sales tax", "Ejemplo: impuesto sobre la venta"), t("A $120 purchase has an 8% tax. What is the total?", "Una compra de $120 tiene un impuesto del 8%. ¿Cuál es el total a pagar?"),
  [("A", t("Find it and add.", "Calcular y sumar."), t("Tax = 0.08 × 120 = $9.60; total = 120 + 9.60 = $129.60.", "Impuesto = 0.08 × 120 = $9.60; total = 120 + 9.60 = $129.60.")),
   ("B", t("Factor.", "Factor."), "120 × 1.08 = $129.60."),
   ("✓", t("Answer.", "Respuesta."), "<strong>$129.60</strong>")])}
{calc(t("Discount and tax on the calculator", "Descuento e impuesto en la calculadora"), t(f"<p>For the shoes, type {T('85')} {T('×')} {T('0.80')} {T('enter')}: 68. For the purchase with tax, type {T('120')} {T('×')} {T('1.08')} {T('enter')}: 129.6, which you write as $129.60.</p>", f"<p>Para los zapatos, escriba {T('85')} {T('×')} {T('0.80')} {T('enter')}: 68. Para la compra con impuesto, escriba {T('120')} {T('×')} {T('1.08')} {T('enter')}: 129.6, que se escribe $129.60.</p>"))}
{practica("p1", t("Practice 1 — A sweater on sale", "Práctica 1 — Un suéter en oferta"), t("A $60 sweater has a 30% discount. What is the sale price?", "Un suéter de $60 tiene un 30% de descuento. ¿Cuál es el precio rebajado?"),
          [("a", "$42"), ("b", "$18"), ("c", "$78"), ("d", "$30")])}
{practica("p2", t("Practice 2 — A bill with tax", "Práctica 2 — Una factura con impuesto"), t("A $200 bill has a 7% tax. What is the total?", "Una factura de $200 tiene un impuesto del 7%. ¿Cuál es el total a pagar?"),
          [("a", "$186"), ("b", "$207"), ("c", "$214"), ("d", "$14")])}
{practica("p3", t("Practice 3 — The discount factor", "Práctica 3 — El factor del descuento"), t("What number do you multiply a price by to take 15% off?", "¿Por qué número se multiplica un precio para aplicarle un 15% de descuento?"),
          [("a", "0.15"), ("b", "0.85"), ("c", "1.15")])}
{enlace(n, t("everyday", "cotidianas"), t("everyday applications", "aplicaciones cotidianas"), t("Practice discounts, taxes, tips, and commissions at the store and the restaurant.", "Practique descuentos, impuestos, propinas y comisiones en la tienda y el restaurante."))}'''

    s3 = f'''<p>{t("In the United States, people usually leave a <strong>tip</strong> at restaurants and for other services. It is usually between 15% and 20% of the bill, most often <strong>before tax</strong>. It is a great calculation to do in your head:", "En Estados Unidos es costumbre dejar una <strong>propina</strong> en restaurantes y otros servicios. Suele calcularse entre el 15% y el 20% de la cuenta, habitualmente <strong>antes del impuesto</strong>. Es un cálculo ideal para hacer mentalmente:")}</p>
{ej(t("Example: a tip in your head on $48", "Ejemplo: propina mental sobre $48"), "",
  [("1", "10%.", t("Move the decimal point one place to the left: $4.80.", "Se mueve el punto decimal un lugar a la izquierda: $4.80.")),
   ("2", "5%.", t("Half of 10%: $2.40.", "La mitad del 10%: $2.40.")),
   ("3", "15%.", "10% + 5% = 4.80 + 2.40 = $7.20."),
   ("4", "20%.", t("Twice 10%: $9.60.", "El doble del 10%: $9.60.")),
   ("✓", t("Answer.", "Respuesta."), t("A fair tip is between <strong>$7.20 and $9.60</strong>.", "Una propina razonable está entre <strong>$7.20 y $9.60</strong>."))])}
{practica("p4", t("Practice 4 — A tip", "Práctica 4 — Una propina"), t("What is an 18% tip on a $55 bill?", "¿Cuánto es una propina del 18% sobre una cuenta de $55?"),
          [("a", "$5.50"), ("b", "$64.90"), ("c", "$99.00"), ("d", "$9.90")])}
{enlace(n, t("tip", "propina"), t("the tip in your head", "la propina mental"), t("Find 10%, 5%, 15%, and 20% in your head.", "Calcule el 10%, el 5%, el 15% y el 20% de cabeza."))}'''

    s4 = f'''<p>{t("Many purchases combine two or more percents. The golden rule: each percent is applied to the value at that moment, not to the original price.", "Muchas compras combinan dos o más porcentajes. La regla de oro: cada porcentaje se aplica sobre el valor que existe en ese momento, no sobre el precio original.")}</p>
{ej(t("Example: discount and then tax", "Ejemplo: descuento y luego impuesto"), t("A $600 TV has a 15% discount. An 8.25% tax is charged on the sale price. How much do you pay?", "Un televisor de $600 tiene un 15% de descuento. Sobre el precio rebajado se cobra un impuesto del 8.25%. ¿Cuánto se paga?"),
  [("1", t("Discount.", "Descuento."), "600 × 0.85 = $510."),
   ("2", t("Tax on the sale price.", "Impuesto sobre el precio rebajado."), "510 × 1.0825 = 552.075."),
   ("3", t("Round to the cent.", "Redondee al centavo."), "$552.08."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$552.08</strong>. In one step: 600 × 0.85 × 1.0825.", "<strong>$552.08</strong>. En un solo paso: 600 × 0.85 × 1.0825."))])}
<h3>{t("Does the order matter?", "¿Importa el orden?")}</h3>
<p>{t("When both changes are percents, the order does <strong>not</strong> change the answer, because you are multiplying factors: 600 × 0.85 × 1.0825 = 600 × 1.0825 × 0.85. What does matter is this:", "Cuando los dos cambios son porcentajes, el orden <strong>no</strong> altera el resultado, porque se multiplican factores: 600 × 0.85 × 1.0825 = 600 × 1.0825 × 0.85. Lo que sí importa es otra cosa:")}</p>
{caja("ojo", t("Mistake 1 · Adding the percents", "Error 1 · Sumar los porcentajes"), t("<p>A 20% discount followed by an extra 10% is not 30%. On $50: 50 × 0.80 = 40; 40 × 0.90 = <strong>$36</strong>. A 30% discount would give $35. The real discount is 1 − (0.80 × 0.90) = 1 − 0.72 = <strong>28%</strong>.</p>", "<p>Un 20% de descuento seguido de un 10% adicional no equivale a un 30%. Sobre $50: 50 × 0.80 = 40; 40 × 0.90 = <strong>$36</strong>. Un 30% daría $35. El descuento real es 1 − (0.80 × 0.90) = 1 − 0.72 = <strong>28%</strong>.</p>"))}
{caja("ojo", t("Mistake 2 · Forgetting that a dollar coupon does depend on the order", "Error 2 · Olvidar que un cupón fijo sí depende del orden"), t("<p>When you combine a percent with a fixed dollar amount, the order changes the answer. With a $60 price, a $10 coupon, and 20% off: coupon first, (60 − 10) × 0.80 = <strong>$40</strong>; percent first, 60 × 0.80 − 10 = <strong>$38</strong>. That is why stores say in what order they apply their offers.</p>", "<p>Cuando se combina un porcentaje con una cantidad fija en dólares, el orden cambia el resultado. Con un precio de $60, un cupón de $10 y un 20% de descuento: cupón primero, (60 − 10) × 0.80 = <strong>$40</strong>; porcentaje primero, 60 × 0.80 − 10 = <strong>$38</strong>. Por eso las tiendas indican en qué orden se aplican las promociones.</p>"))}
{practica("p5", t("Practice 5 — Headphones", "Práctica 5 — Audífonos"), t("$80 headphones have a 25% discount, and an 8% tax is charged on the sale price. How much do you pay?", "Unos audífonos de $80 tienen un 25% de descuento y se cobra un 8% de impuesto sobre el precio rebajado. ¿Cuánto se paga?"),
          [("a", "$66.40"), ("b", "$64.80"), ("c", "$60.00"), ("d", "$86.40")])}
{practica("p6", t("Practice 6 — Two discounts", "Práctica 6 — Dos descuentos"), t("A store gives 30% off and then an extra 10% off the sale price. What total discount is that?", "Una tienda ofrece 30% de descuento y luego un 10% adicional sobre el precio rebajado. ¿Qué descuento total equivale?"),
          [("a", "37%"), ("b", "40%"), ("c", "33%")])}
{practica("p7", t("Practice 7 — At the restaurant", "Práctica 7 — En el restaurante"), t("At a restaurant the bill is $40 before tax. The tax is 10%, and you leave a 15% tip on the $40. What is the total?", "En un restaurante la cuenta es de $40 antes de impuestos. El impuesto es del 10% y se deja un 15% de propina sobre los $40. ¿Cuál es el total?"),
          [("a", "$46.00"), ("b", "$50.60"), ("c", "$50.00")])}
{enlace(n, t("chained", "encadenados"), t("chained percents", "porcentajes encadenados"), t("Use the shopping simulator and apply each percent to the value at that moment.", "Use el simulador de compra y aplique cada porcentaje sobre el valor de ese momento."))}'''

    secciones = [("s-" + t("receipt", "recibo"), t("Start with a receipt", "Empezar por un recibo"), s1),
                 ("s-" + t("discount-tax", "descuento-impuesto"), t("Discount and sales tax", "Descuento e impuesto sobre la venta"), s2),
                 ("s-" + t("tip", "propina"), t("Tips", "Propina"), s3),
                 ("s-" + t("chained", "encadenados"), t("Chained percents", "Porcentajes encadenados"), s4)]

    lesson = {"next": t("Topic 6", "el Tema 6"), "review": t("sections 2 and 4", "las secciones 2 y 4"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("$18 is the discount. Subtract it from $60.", "$18 es el descuento. Réstelo de $60."), "c": t("A discount is subtracted, not added.", "El descuento se resta, no se suma."), "d": t("30% is not $30. Find 0.30 × 60.", "30% no son $30. Calcule 0.30 × 60.")},
             "right": t("60 × 0.70 = $42.", "60 × 0.70 = $42."), "solution": t("With 30% off you pay 70%: 60 × 0.70 = $42.", "Con 30% de descuento se paga el 70%: 60 × 0.70 = $42.")},
      "p2": {"ok": "c", "hints": {"a": t("Tax is added, not subtracted.", "El impuesto se suma, no se resta."), "b": t("7% of $200 is not $7. Find 0.07 × 200.", "El 7% de $200 no son $7. Calcule 0.07 × 200."), "d": t("$14 is only the tax. Add it to $200.", "$14 es solo el impuesto. Súmelo a $200.")},
             "right": t("200 × 1.07 = $214.", "200 × 1.07 = $214."), "solution": t("Tax = 0.07 × 200 = $14; total = 200 + 14 = $214.", "Impuesto = 0.07 × 200 = $14; total = 200 + 14 = $214.")},
      "p3": {"ok": "b", "hints": {"a": t("0.15 gives only the discount.", "0.15 da solo el descuento."), "c": t("1.15 is for adding 15%, like a tax.", "1.15 es para sumar un 15%, como un impuesto.")},
             "right": t("You pay 85%: × 0.85.", "Se paga el 85%: × 0.85."), "solution": t("1 − 0.15 = 0.85.", "1 − 0.15 = 0.85.")},
      "p4": {"ok": "d", "hints": {"a": t("$5.50 is only 10%.", "$5.50 es solo el 10%."), "b": t("That is the bill plus the tip. Only the tip is asked.", "Eso es la cuenta más la propina. Se pide solo la propina."), "c": t("18% is 0.18, not 1.8.", "18% es 0.18, no 1.8.")},
             "right": t("55 × 0.18 = $9.90.", "55 × 0.18 = $9.90."), "solution": t("55 × 0.18 = 9.9 → $9.90.", "55 × 0.18 = 9.9 → $9.90.")},
      "p5": {"ok": "b", "hints": {"a": t("You added the percents (−25% + 8%). Apply them one after the other.", "Sumó los porcentajes (−25% + 8%). Aplíquelos uno después del otro."), "c": t("$60 is the sale price. Add the tax.", "$60 es el precio rebajado. Falta el impuesto."), "d": t("You forgot the discount.", "Olvidó el descuento.")},
             "right": t("80 × 0.75 = 60; 60 × 1.08 = $64.80.", "80 × 0.75 = 60; 60 × 1.08 = $64.80."), "solution": t("Discount: 80 × 0.75 = $60. Tax on $60: 60 × 1.08 = $64.80.", "Descuento: 80 × 0.75 = $60. Impuesto sobre $60: 60 × 1.08 = $64.80.")},
      "p6": {"ok": "a", "hints": {"b": t("The percents are not added: the 10% is on a lower price.", "Los porcentajes no se suman: el 10% es sobre un precio menor."), "c": t("Multiply the factors: 0.70 × 0.90.", "Multiplique los factores: 0.70 × 0.90.")},
             "right": t("0.70 × 0.90 = 0.63: you pay 63%, so 37% off.", "0.70 × 0.90 = 0.63: se paga el 63%, así que el descuento es 37%."), "solution": t("You pay 0.70 × 0.90 = 0.63 = 63%. The total discount is 100% − 63% = 37%.", "Se paga 0.70 × 0.90 = 0.63 = 63%. El descuento total es 100% − 63% = 37%.")},
      "p7": {"ok": "c", "hints": {"a": t("You left out the tip.", "Olvidó la propina."), "b": t("The tip is on the $40, not on the bill with tax.", "La propina es sobre los $40, no sobre la cuenta con impuesto.")},
             "right": t("40 + 4 + 6 = $50.", "40 + 4 + 6 = $50."), "solution": t("Tax: 0.10 × 40 = $4. Tip: 0.15 × 40 = $6. Total: 40 + 4 + 6 = $50.", "Impuesto: 0.10 × 40 = $4. Propina: 0.15 × 40 = $6. Total: 40 + 4 + 6 = $50.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("$17 is the discount.", "$17 es el descuento."), "c": t("20% is not $20.", "20% no son $20."), "d": t("A discount is subtracted.", "El descuento se resta.")}, "solution": t("85 × 0.80 = $68.", "85 × 0.80 = $68.")},
      "B": {"ok": "d", "hints": {"a": t("$9.60 is only the tax.", "$9.60 es solo el impuesto."), "b": t("8% is not $8.", "8% no son $8."), "c": t("Tax is added.", "El impuesto se suma.")}, "solution": t("120 × 1.08 = $129.60.", "120 × 1.08 = $129.60.")},
      "C": {"ok": "a", "hints": {"b": t("0.25 gives only the discount.", "0.25 da solo el descuento."), "c": t("1.25 adds 25%.", "1.25 suma un 25%."), "d": t("Write 75% as a decimal.", "Escriba 75% en decimal.")}, "solution": t("You pay 75%: × 0.75.", "Se paga el 75%: × 0.75.")},
      "D": {"ok": "b", "hints": {"a": t("$4.80 is only 10%. Add 5%.", "$4.80 es solo el 10%. Sume el 5%."), "c": t("$9.60 is 20%.", "$9.60 es el 20%."), "d": t("That is the bill plus the tip.", "Eso es la cuenta más la propina.")}, "solution": t("10% = $4.80; 5% = $2.40; 15% = $7.20.", "10% = $4.80; 5% = $2.40; 15% = $7.20.")},
      "E": {"ok": "c", "hints": {"a": t("The percents are not added.", "Los porcentajes no se suman."), "b": t("Multiply 0.80 × 0.90.", "Multiplique 0.80 × 0.90."), "d": t("Check: you pay 72%.", "Revise: se paga el 72%.")}, "solution": t("0.80 × 0.90 = 0.72; 100% − 72% = 28%.", "0.80 × 0.90 = 0.72; 100% − 72% = 28%.")},
      "F": {"ok": "a", "hints": {"b": t("$510 is the sale price. Add the tax.", "$510 es el precio rebajado. Falta el impuesto."), "c": t("You added the percents. Apply them one after the other.", "Sumó los porcentajes. Aplíquelos uno tras otro."), "d": t("You forgot the discount.", "Olvidó el descuento.")}, "solution": t("600 × 0.85 = 510; 510 × 1.0825 = 552.075 → $552.08.", "600 × 0.85 = 510; 510 × 1.0825 = 552.075 → $552.08.")},
      "G": {"ok": "d", "hints": {"a": t("That is the percent first. Here the coupon goes first.", "Eso es con el porcentaje primero. Aquí va primero el cupón."), "b": t("20% is not $20.", "20% no son $20."), "c": t("You forgot the coupon.", "Olvidó el cupón.")}, "solution": t("(60 − 10) × 0.80 = $40.", "(60 − 10) × 0.80 = $40.")},
      "H": {"ok": "a", "hints": {"b": t("4.7025 rounds down: the third decimal digit is 2.", "4.7025 se redondea hacia abajo: la tercera cifra decimal es 2."), "c": t("Check: 0.0825 × 57.", "Revise: 0.0825 × 57."), "d": t("8.25% is 0.0825, not 0.825.", "8.25% es 0.0825, no 0.825.")}, "solution": t("57 × 0.0825 = 4.7025 → $4.70.", "57 × 0.0825 = 4.7025 → $4.70.")}
     }}

    quiz = [
     ("A", t("$85 shoes have a 20% discount. What is the final price?", "Unos zapatos de $85 tienen un 20% de descuento. ¿Cuál es el precio final?"), [("a", "$17"), ("b", "$68"), ("c", "$65"), ("d", "$102")]),
     ("B", t("A $120 purchase has an 8% tax. What is the total?", "Una compra de $120 tiene un 8% de impuesto. ¿Cuál es el total?"), [("a", "$9.60"), ("b", "$128.00"), ("c", "$110.40"), ("d", "$129.60")]),
     ("C", t("What do you multiply a price by to take 25% off?", "¿Por qué se multiplica un precio para descontarle un 25%?"), [("a", "0.75"), ("b", "0.25"), ("c", "1.25"), ("d", "75")]),
     ("D", t("What is a 15% tip on a $48 bill?", "¿Cuánto es una propina del 15% sobre una cuenta de $48?"), [("a", "$4.80"), ("b", "$7.20"), ("c", "$9.60"), ("d", "$55.20")]),
     ("E", t("A 20% discount and then an extra 10% on the sale price are the same as a discount of:", "Un 20% de descuento y luego un 10% adicional sobre el precio rebajado equivalen a un descuento de:"), [("a", "30%"), ("b", "32%"), ("c", "28%"), ("d", "18%")]),
     ("F", t("A $600 TV has 15% off, and 8.25% tax is charged on the sale price. How much do you pay?", "Un televisor de $600 tiene 15% de descuento y se cobra 8.25% de impuesto sobre el precio rebajado. ¿Cuánto se paga?"), [("a", "$552.08"), ("b", "$510.00"), ("c", "$559.50"), ("d", "$649.50")]),
     ("G", t("A $60 item has a $10 coupon applied first and then 20% off. How much do you pay?", "A un artículo de $60 se le aplica primero un cupón de $10 y después un 20% de descuento. ¿Cuánto se paga?"), [("a", "$38"), ("b", "$30"), ("c", "$48"), ("d", "$40")]),
     ("H", t("A receipt shows a $57 subtotal and 8.25% tax. What is the tax, rounded to the cent?", "Un recibo tiene un subtotal de $57 y un impuesto del 8.25%. ¿Cuánto es el impuesto, redondeado al centavo?"), [("a", "$4.70"), ("b", "$4.71"), ("c", "$5.70"), ("d", "$47.03")])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Percents in daily life: sale prices, sales tax, tips, and purchases that combine several percents.", "El porcentaje en la vida diaria: precios rebajados, impuesto sobre la venta, propinas y compras que combinan varios porcentajes."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Find</strong> a sale price by subtracting or with the factor (1 − r).", "<strong>Calcular</strong> un precio rebajado restando o con el factor (1 − r)."),
         t("<strong>Find</strong> a total with sales tax using the factor (1 + r), and round to the cent.", "<strong>Calcular</strong> un total con impuesto usando el factor (1 + r) y redondear al centavo."),
         t("<strong>Figure</strong> a 15% to 20% tip in your head.", "<strong>Calcular</strong> mentalmente una propina del 15% al 20%."),
         t("<strong>Apply</strong> chained percents to the value at each moment, and know when the order matters.", "<strong>Aplicar</strong> porcentajes encadenados sobre el valor de cada momento y saber cuándo importa el orden.")],
        secciones,
        (t("Solve two discount problems and two sales-tax problems in both ways (subtract or add, and the change factor). Figure two tips in your head with the 10% and 5% strategy, then check them on the calculator. Solve two chained problems: a discount plus tax, and two discounts in a row.",
           "Resuelva dos problemas de descuento y dos de impuesto sobre la venta por los dos métodos (restar o sumar, y factor de cambio). Calcule dos propinas mentalmente con la estrategia del 10% y del 5%, y compruébelas después con calculadora. Resuelva dos problemas encadenados: un descuento más impuesto, y dos descuentos seguidos."),
         t("Take one of your own receipts. Figure out each line again, check the tax rate, and check the rounding.",
           "Tome un recibo suyo. Recalcule cada línea y compruebe la tasa de impuesto y el redondeo.")),
        quiz,
        t("Self-check checklist for discount, tax, and tip", "Lista de autoevaluación de descuento, impuesto y propina"),
        t("Self-check checklist: skills for discounts, taxes, tips, and chained percents", "Lista de autoevaluación: destrezas de descuentos, impuestos, propinas y porcentajes encadenados"),
        [(t("Sale price", "Precio con descuento"), t("I find it both ways and check that they match.", "Lo calculo por los dos métodos y compruebo que coinciden."), t("I find the discount but forget to subtract it.", "Calculo el descuento pero olvido restarlo."), t("I mix up the discount and the final price.", "Confundo el descuento con el precio final.")),
         (t("Tax on the right price", "Impuesto sobre el precio correcto"), t("I figure tax on the right price and round to the cent.", "Calculo el impuesto sobre el precio que corresponde y redondeo al centavo."), t("I figure tax on the original price when it should be the sale price.", "Calculo el impuesto sobre el precio original cuando correspondía el rebajado."), t("I figure tax on the wrong amount.", "Calculo el impuesto sobre un valor equivocado.")),
         (t("A fair tip", "Propina razonable"), t("I figure it in my head with 10% and 5%.", "La calculo mentalmente con el 10% y el 5%."), t("I figure it with a calculator, with some mistakes.", "La calculo con calculadora y con errores."), t("I do not figure the tip.", "No calculo la propina.")),
         (t("Chained percents", "Porcentajes consecutivos"), t("I apply each percent to the current value and explain when the order matters.", "Aplico cada porcentaje sobre el valor vigente y explico cuándo importa el orden."), t("I apply them in a chain with help.", "Los aplico en cadena con apoyo."), t("I add the percents (20% + 10% = 30%).", "Sumo los porcentajes (20% + 10% = 30%)."))],
        t("<p>With this lesson you finish <strong>Topic 5</strong>. Percents went from a ratio out of 100 to a tool for daily life: converting, finding the part, the whole, or the percent, measuring percent change, and solving discounts, taxes, and tips, even chained together.</p>\n<p><strong>Topic 6 · Money math and unit conversions</strong> opens with Lesson 6.1 · Simple interest: I = P × r × t. There, percents work over <strong>time</strong>: how much a loan or a savings account grows at a fixed yearly rate.</p>",
          "<p>Con esta lección termina el <strong>Tema 5</strong>. El porcentaje pasó de ser una razón de 100 a una herramienta para la vida diaria: convertir, hallar la parte, el todo o el porcentaje, medir el cambio porcentual y resolver descuentos, impuestos y propinas, incluso encadenados.</p>\n<p>El <strong>Tema 6 · Matemáticas financieras y conversiones de medidas</strong> abre con la Lección 6.1 · Interés simple: la fórmula I = P × r × t. Allí el porcentaje se aplica a lo largo del <strong>tiempo</strong>: cuánto crece un préstamo o un ahorro con una tasa anual fija.</p>"),
        ("6-1", ("", t("Lesson 6.1 · Simple interest: I = P × r × t", "Lección 6.1 · Interés simple: la fórmula I = P × r × t"))),
        [(t("discount", "descuento"), t("A percent taken off the price. Factor: 1 − r.", "Porcentaje que se resta del precio. Factor: 1 − r.")),
         (t("sales tax", "impuesto sobre la venta"), t("A percent added to the price. Factor: 1 + r.", "Porcentaje que se suma al precio. Factor: 1 + r.")),
         (t("tip", "propina"), t("Money left for a service, usually 15% to 20% of the bill before tax.", "Dinero que se deja por un servicio, casi siempre del 15% al 20% de la cuenta antes del impuesto.")),
         (t("chained percents", "porcentajes encadenados"), t("Two or more percents applied one after the other, each on the current value.", "Dos o más porcentajes aplicados uno tras otro, cada uno sobre el valor del momento."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "c1": "An item that costs {P} has a {p}% discount. What is the final price?", "c1s": "{P} × {r} = {d} off; {P} − {d2} = {x}.", "c1a": "That is the discount. Subtract it from the original price.", "c1b": "A discount is subtracted, not added.",
  "c2": "A {P} purchase has a {p}% sales tax. What is the total?", "c2s": "{P} × {r} = {d}; {P} + {d2} = {x}.", "c2a": "That is the tax. Add it to the price.", "c2b": "Tax is added, not subtracted.",
  "c3": "A restaurant bill is {P}, and you leave a {p}% tip. How much do you pay in all?", "c3s": "{P} × {r} = {d}; {P} + {d2} = {x}.", "c3a": "That is the tip. Add it to the bill.",
  "c4": "A salesperson earns a {p}% commission on sales. If the person sold {P}, how much is the commission?", "c4s": "{P} × {r} = {x}.", "c4a": "The commission is only the percent: do not subtract it from the sales.",
  "c5": "A {P} sweater has a {p}% discount. How many dollars do you save?", "c5s": "{P} × {r} = {x}.", "c5a": "That is the final price. The question asks how much you save: the discount.",
  "escribeCuenta": "Type the total of the bill.", "t10": "<strong>10%:</strong> move the point: {c} → {a}.", "t5": "<strong>5%:</strong> half of 10%: {a}.",
  "t15": "<strong>15%</strong> = {a} + {b} = {c}.", "t20": "<strong>20%</strong> = twice 10% = {a}.", "tRaz": "A fair tip is between {a} and {b}.",
  "propQ": "The restaurant bill is {c}. How much is a {p}% tip?", "s15": "10% = {a}; 5% = {b}; 15% = {c}.", "s20": "10% = {a}; twice that is {c}.", "s10": "Move the point one place: {c}.", "s18": "{x} × 0.18 = {c}.",
  "pTotal": "That is the total with the tip. Only the tip is asked.", "pDec": "Write the percent as a decimal: {p}% = {r}.", "p10": "That is only 10%. Add 5% (half of 10%).",
  "revisa": "Check the data: type numbers only.", "recibo": "Receipt", "precio": "Price", "descuento": "Discount {p}%", "adicional": "Extra {p}% (on {s})", "impuesto": "Tax {p}%",
  "unPaso": "In one step: {f} = {x} (before rounding each line).", "equivalen": "The two discounts are the same as {a} off, not {b}.",
  "e1": "An item that costs {P} has a {d}% discount, and a {i}% tax is charged on the sale price. How much do you pay?", "e1s": "{P} × {f1} = {s}; {s} × {f2} = {x}.",
  "e1a": "Percents are not added or subtracted together: first the discount, then the tax on the sale price.", "e1b": "That is the sale price. Add the tax.", "e1c": "The tax is figured on the sale price, not on the original.",
  "e2": "A store gives {a}% off and then an extra {b}% off the sale price. What total discount is that?", "e2s": "You pay {f1} × {f2} = {q}, that is, {p}. The total discount is {x}.",
  "e2a": "The percents are not added: the second one is on a price that is already lower.", "e2b": "That is the percent you pay. The question asks for the discount.",
  "e3": "Shoes that cost {P} have a {d}% discount and, with the store card, an extra {e}% off the sale price. What is the final price?", "e3s": "{P} × {f1} × {f2} = {x}.", "e3a": "The discounts are not added: the {e}% is figured on the price that is already lower.",
  "cupPrim": "Coupon first", "pctPrim": "Percent first", "cupon": "Coupon", "queda": "Left", "pagas": "You pay",
  "coinciden": "With these numbers both orders give the same.", "dif": "Difference: {d}. It is better to apply the percent first: then the coupon comes off whole at the end.",
  "o3": "An item costs {P}, has a {d}% discount, and you have a {c} coupon. In which order is it better to apply them?",
  "oPc": "First the percent, then the coupon", "oCp": "First the coupon, then the percent", "oIg": "It is the same",
  "o3s": "Percent first: {P} × {f} − {c} = {b}. Coupon first: ({P} − {c}) × {f} = {a}. With the coupon at the end you save {d} more.",
  "o3i": "With two percents the order does not matter, but with a dollar coupon it changes the answer.",
  "o12": "An item costs {P}, has a {d}% discount, and a {c} coupon. The store applies {x}. How much do you pay?", "oCupPrim": "<strong>the coupon first</strong> and then the percent", "oPctPrim": "<strong>the percent first</strong> and then the coupon",
  "oOtro": "That answer goes with the other order.", "oFalta": "You still need to apply the coupon.", "oDol": "{d}% is not {d} dollars.",
  "oS1": "({P} − {c}) × {f} = {a}.", "oS2": "{P} × {f} = {m}; minus {c} = {b}."
 },
 "es": {
  "c1": "Un artículo de {P} tiene un {p}% de descuento. ¿Cuál es el precio final?", "c1s": "{P} × {r} = {d} de descuento; {P} − {d2} = {x}.", "c1a": "Ese es el descuento. Falta restarlo del precio original.", "c1b": "El descuento se resta, no se suma.",
  "c2": "Una compra de {P} tiene un impuesto sobre la venta del {p}%. ¿Cuál es el total a pagar?", "c2s": "{P} × {r} = {d}; {P} + {d2} = {x}.", "c2a": "Ese es el impuesto. Falta sumarlo al precio.", "c2b": "El impuesto se suma, no se resta.",
  "c3": "La cuenta de un restaurante es de {P} y se deja una propina del {p}%. ¿Cuánto se paga en total?", "c3s": "{P} × {r} = {d}; {P} + {d2} = {x}.", "c3a": "Esa es la propina. Falta sumarla a la cuenta.",
  "c4": "Un vendedor gana una comisión del {p}% sobre sus ventas. Si vendió {P}, ¿cuánto gana de comisión?", "c4s": "{P} × {r} = {x}.", "c4a": "La comisión es solo el porcentaje: no se resta de las ventas.",
  "c5": "Un suéter de {P} tiene un {p}% de descuento. ¿Cuántos dólares se ahorran?", "c5s": "{P} × {r} = {x}.", "c5a": "Ese es el precio final. Se pregunta cuánto se ahorra: el descuento.",
  "escribeCuenta": "Escriba el total de la cuenta.", "t10": "<strong>10%:</strong> se mueve el punto: {c} → {a}.", "t5": "<strong>5%:</strong> la mitad del 10%: {a}.",
  "t15": "<strong>15%</strong> = {a} + {b} = {c}.", "t20": "<strong>20%</strong> = el doble del 10% = {a}.", "tRaz": "Una propina razonable está entre {a} y {b}.",
  "propQ": "La cuenta del restaurante es de {c}. ¿Cuánto es una propina del {p}%?", "s15": "10% = {a}; 5% = {b}; 15% = {c}.", "s20": "10% = {a}; el doble es {c}.", "s10": "Se mueve el punto un lugar: {c}.", "s18": "{x} × 0.18 = {c}.",
  "pTotal": "Ese es el total con propina. Se pide solo la propina.", "pDec": "El porcentaje va en decimal: {p}% = {r}.", "p10": "Eso es solo el 10%. Falta sumar el 5% (la mitad del 10%).",
  "revisa": "Revise los datos: escriba solo números.", "recibo": "Recibo", "precio": "Precio", "descuento": "Descuento {p}%", "adicional": "Adicional {p}% (sobre {s})", "impuesto": "Impuesto {p}%",
  "unPaso": "En un solo paso: {f} = {x} (antes de redondear cada línea).", "equivalen": "Los dos descuentos equivalen a un {a}, no a un {b}.",
  "e1": "Un artículo de {P} tiene un {d}% de descuento, y sobre el precio rebajado se cobra un {i}% de impuesto. ¿Cuánto se paga?", "e1s": "{P} × {f1} = {s}; {s} × {f2} = {x}.",
  "e1a": "Los porcentajes no se suman ni se restan entre sí: primero el descuento, y el impuesto sobre el precio rebajado.", "e1b": "Ese es el precio rebajado. Falta sumar el impuesto.", "e1c": "El impuesto se calcula sobre el precio rebajado, no sobre el original.",
  "e2": "Una tienda ofrece un {a}% de descuento y luego un {b}% adicional sobre el precio rebajado. ¿Qué descuento total equivale?", "e2s": "Se paga {f1} × {f2} = {q}, es decir, el {p}. El descuento total es {x}.",
  "e2a": "Los porcentajes no se suman: el segundo se aplica sobre un precio ya rebajado.", "e2b": "Ese es el porcentaje que se paga. Se pregunta el descuento.",
  "e3": "Unos zapatos de {P} tienen un {d}% de descuento y, con la tarjeta de la tienda, un {e}% adicional sobre el precio rebajado. ¿Cuál es el precio final?", "e3s": "{P} × {f1} × {f2} = {x}.", "e3a": "Los descuentos no se suman: el {e}% se calcula sobre el precio ya rebajado.",
  "cupPrim": "Cupón primero", "pctPrim": "Porcentaje primero", "cupon": "Cupón", "queda": "Queda", "pagas": "Paga",
  "coinciden": "Con estos datos los dos órdenes coinciden.", "dif": "Diferencia: {d}. Conviene aplicar primero el porcentaje: así el cupón se resta completo al final.",
  "o3": "Un artículo de {P} tiene un {d}% de descuento y usted tiene un cupón de {c}. ¿En qué orden conviene aplicarlos?",
  "oPc": "Primero el porcentaje y después el cupón", "oCp": "Primero el cupón y después el porcentaje", "oIg": "Da lo mismo",
  "o3s": "Porcentaje primero: {P} × {f} − {c} = {b}. Cupón primero: ({P} − {c}) × {f} = {a}. Con el cupón al final se ahorran {d} más.",
  "o3i": "Con dos porcentajes sí da lo mismo, pero con un cupón fijo el orden cambia el resultado.",
  "o12": "Un artículo de {P} tiene un {d}% de descuento y un cupón de {c}. La tienda aplica {x}. ¿Cuánto se paga?", "oCupPrim": "<strong>primero el cupón</strong> y después el porcentaje", "oPctPrim": "<strong>primero el porcentaje</strong> y después el cupón",
  "oOtro": "Ese resultado corresponde al otro orden.", "oFalta": "Falta aplicar el cupón.", "oDol": "El {d}% no son {d} dólares.",
  "oS1": "({P} − {c}) × {f} = {a}.", "oS2": "{P} × {f} = {m}; menos {c} = {b}."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function pc(x){ return nd(Math.round(x * 1000) / 1000) + "%"; }
function cent(x){ return Math.round((x + 1e-9) * 100) / 100; }
function lee(id){ var v = leeD(String($(id).value).replace("%", "")); $(id).classList.toggle("error", v === null || v < 0); return v === null || v < 0 ? null : v; }
function lin(a, b, cl){ return '<div class="l' + (cl ? " " + cl : "") + '"><span>' + a + '</span><span>' + b + '</span></div>'; }
function sinPct(t){ return String(t).replace(/%/g, ""); }

/* ============ MODULE 1 · everyday ============ */
function genCotidiana(){
  var tp = aleatorio(1, 5), P, p, res, o, pist = [];
  if (tp === 1){ P = elige([40, 60, 85, 120, 75, 48, 150]); p = elige([10, 15, 20, 25, 30, 40]); var des = cent(P * p / 100); res = cent(P - des); o = { P: dinero(P), p: p, r: nd(p / 100), d: dinero(des), d2: nd(des), x: dinero(res) }; pist.push({ v: des, msg: TXT.c1a }, { v: P + des, msg: TXT.c1b }); }
  else if (tp === 2){ P = elige([120, 80, 45, 250, 60, 36]); p = elige([6, 7, 8, 9, 10]); var imp = cent(P * p / 100); res = cent(P + imp); o = { P: dinero(P), p: p, r: nd(p / 100), d: dinero(imp), d2: nd(imp), x: dinero(res) }; pist.push({ v: imp, msg: TXT.c2a }, { v: P - imp, msg: TXT.c2b }); }
  else if (tp === 3){ P = elige([48, 60, 36, 84, 52, 120]); p = elige([15, 18, 20]); var pr = cent(P * p / 100); res = cent(P + pr); o = { P: dinero(P), p: p, r: nd(p / 100), d: dinero(pr), d2: nd(pr), x: dinero(res) }; pist.push({ v: pr, msg: TXT.c3a }); }
  else if (tp === 4){ P = elige([2000, 1500, 3200, 850, 12000]); p = elige([3, 4, 5, 6, 8, 10]); res = cent(P * p / 100); o = { P: dinero(P), p: p, r: nd(p / 100), x: dinero(res) }; pist.push({ v: P - res, msg: TXT.c4a }); }
  else { P = elige([60, 80, 25, 45, 120]); p = elige([10, 20, 25, 30]); res = cent(P * p / 100); o = { P: dinero(P), p: p, r: nd(p / 100), x: dinero(res) }; pist.push({ v: P - res, msg: TXT.c5a }); }
  return { enun: F(TXT["c" + tp], o), correcta: dinero(res), solucion: F(TXT["c" + tp + "s"], o), evalua: numD(res, pist) };
}

/* ============ MODULE 2 · the tip ============ */
function pintaPR(){
  var c = lee("pr-c"), s = $("pr-salida");
  if (c === null){ s.innerHTML = '<div class="linea">' + TXT.escribeCuenta + '</div>'; return; }
  var t10 = cent(c / 10), t5 = cent(c / 20), t15 = cent(c * 0.15), t20 = cent(c * 0.2);
  s.innerHTML = '<div class="linea">' + F(TXT.t10, { c: dinero2(c), a: dinero2(t10) }) + '</div><div class="linea">' + F(TXT.t5, { a: dinero2(t5) }) + '</div>' +
    '<div class="linea">' + F(TXT.t15, { a: dinero2(t10), b: dinero2(t5), c: dinero2(t15) }) + '</div><div class="linea">' + F(TXT.t20, { a: dinero2(t20) }) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.tRaz, { a: dinero2(t15), b: dinero2(t20) }) + '</div>';
}
function genPropina(){
  var c = elige([24, 36, 42, 48, 52, 56, 64, 68, 72, 84, 96, 36.5, 42.5, 55, 45]), p = elige([10, 15, 20, 18]), tt = cent(c * p / 100);
  var sol = p === 15 ? F(TXT.s15, { a: dinero2(c / 10), b: dinero2(c / 20), c: dinero2(tt) }) : (p === 20 ? F(TXT.s20, { a: dinero2(c / 10), c: dinero2(tt) }) : (p === 10 ? F(TXT.s10, { c: dinero2(tt) }) : F(TXT.s18, { x: nd(c), c: dinero2(tt) })));
  var pist = [{ v: cent(c + tt), msg: TXT.pTotal }, { v: cent(c * p), msg: F(TXT.pDec, { p: p, r: nd(p / 100) }) }];
  if (p === 15) pist.push({ v: cent(c / 10), msg: TXT.p10 });
  return { enun: F(TXT.propQ, { c: dinero2(c), p: p }), correcta: dinero2(tt), solucion: sol, evalua: numD(tt, pist) };
}

/* ============ MODULE 3 · chained percents ============ */
function pintaSI(){
  var p = lee("si-p"), d = lee("si-d"), e = lee("si-d2"), i = lee("si-i"), s = $("si-salida");
  if ([p, d, e, i].some(function(x){ return x === null; })){ s.innerHTML = '<div class="salida"><div class="linea">' + TXT.revisa + '</div></div>'; return; }
  var desc1 = cent(p * d / 100), sub1 = cent(p - desc1), desc2 = cent(sub1 * e / 100), sub = cent(sub1 - desc2), imp = cent(sub * i / 100), tot = cent(sub + imp);
  var h = '<div class="recibo" role="group" aria-label="' + TXT.recibo + '"><h4>' + TXT.recibo + '</h4>' + lin(TXT.precio, dinero2(p));
  if (d > 0) h += lin(F(TXT.descuento, { p: nd(d) }), "−" + dinero2(desc1));
  if (e > 0) h += lin(F(TXT.adicional, { p: nd(e), s: dinero2(sub1) }), "−" + dinero2(desc2));
  h += '<div class="sep"></div>' + lin("Subtotal", dinero2(sub)) + lin(F(TXT.impuesto, { p: nd(i) }), dinero2(imp)) + '<div class="sep"></div>' + lin("TOTAL", dinero2(tot), "tot") + '</div>';
  var f = [nd(p)]; if (d > 0) f.push(nd(Math.round((1 - d / 100) * 10000) / 10000)); if (e > 0) f.push(nd(Math.round((1 - e / 100) * 10000) / 10000)); if (i > 0) f.push(nd(Math.round((1 + i / 100) * 10000) / 10000));
  h += '<div class="salida"><div class="linea">' + F(TXT.unPaso, { f: f.join(" × "), x: dinero2(p * (1 - d / 100) * (1 - e / 100) * (1 + i / 100)) }) + '</div>';
  if (d > 0 && e > 0){ var real = Math.round((1 - (1 - d / 100) * (1 - e / 100)) * 10000) / 100; h += '<div class="linea">' + F(TXT.equivalen, { a: pc(real), b: pc(d + e) }) + '</div>'; }
  s.innerHTML = h + '</div>';
}
function genEncadenado(){
  var tp = aleatorio(1, 3);
  if (tp === 1){
    var P = elige([80, 120, 600, 250, 45, 360, 95]), d = elige([10, 15, 20, 25, 30]), i = elige([6, 7, 8, 8.25, 9, 10]), sub = cent(P * (1 - d / 100)), tot = cent(sub + cent(sub * i / 100));
    var pist = [{ v: cent(P * (1 - d / 100 + i / 100)), msg: TXT.e1a }, { v: sub, msg: TXT.e1b }, { v: cent(P * (1 + i / 100) - P * d / 100), msg: TXT.e1c }].filter(function(x){ return Math.abs(x.v - tot) > 0.011; });
    return { enun: F(TXT.e1, { P: dinero(P), d: d, i: nd(i) }), correcta: dinero2(tot), solucion: F(TXT.e1s, { P: nd(P), f1: nd(1 - d / 100), s: dinero2(sub), f2: nd(1 + i / 100), x: dinero2(tot) }), evalua: numD(tot, pist, null, 0.011) };
  }
  if (tp === 2){
    var a = elige([10, 20, 25, 30, 40, 50]), b = elige([10, 15, 20, 25]), q = Math.round((1 - a / 100) * (1 - b / 100) * 10000) / 10000, eq = Math.round((1 - q) * 10000) / 100;
    var ev = numD(eq, [{ v: a + b, msg: TXT.e2a }, { v: 100 - eq, msg: TXT.e2b }], null, 0.051);
    return { enun: F(TXT.e2, { a: a, b: b }), correcta: pc(eq), solucion: F(TXT.e2s, { f1: nd(1 - a / 100), f2: nd(1 - b / 100), q: nd(q), p: pc(100 - eq), x: pc(eq) }), evalua: function(s){ return ev(sinPct(s)); } };
  }
  var P3 = elige([40, 60, 80, 120, 150]), d3 = elige([15, 20, 25, 30]), d4 = elige([10, 20]), fin = cent(P3 * (1 - d3 / 100) * (1 - d4 / 100));
  return { enun: F(TXT.e3, { P: dinero(P3), d: d3, e: d4 }), correcta: dinero2(fin), solucion: F(TXT.e3s, { P: nd(P3), f1: nd(1 - d3 / 100), f2: nd(1 - d4 / 100), x: dinero2(fin) }),
    evalua: numD(fin, [{ v: cent(P3 * (1 - (d3 + d4) / 100)), msg: F(TXT.e3a, { e: d4 }) }], null, 0.011) };
}

/* ============ MODULE 4 · order with a coupon ============ */
function pintaOR(){
  var p = lee("or-p"), c = lee("or-c"), d = lee("or-d"), s = $("or-salida");
  if ([p, c, d].some(function(x){ return x === null; })){ s.innerHTML = '<div class="salida"><div class="linea">' + TXT.revisa + '</div></div>'; return; }
  var f = 1 - d / 100, a = cent((p - c) * f), b = cent(p * f - c);
  s.innerHTML = '<div class="dos-col"><div class="recibo"><h4>' + TXT.cupPrim + '</h4>' + lin(TXT.precio, dinero2(p)) + lin(TXT.cupon, "−" + dinero2(c)) + lin(TXT.queda, dinero2(p - c)) + lin("× " + nd(f) + " (" + nd(d) + "%)", "") + '<div class="sep"></div>' + lin(TXT.pagas, dinero2(a), "tot") + '</div>' +
    '<div class="recibo"><h4>' + TXT.pctPrim + '</h4>' + lin(TXT.precio, dinero2(p)) + lin("× " + nd(f) + " (" + nd(d) + "%)", dinero2(cent(p * f))) + lin(TXT.cupon, "−" + dinero2(c)) + '<div class="sep"></div>' + lin(TXT.pagas, dinero2(b), "tot") + '</div></div>' +
    '<div class="salida"><div class="linea">' + (a === b ? TXT.coinciden : F(TXT.dif, { d: dinero2(Math.abs(a - b)) })) + '</div></div>';
}
function genOrden(){
  var P = elige([40, 50, 60, 80, 100, 120]), c = elige([5, 10, 15, 20]), d = elige([10, 20, 25, 30]), f = 1 - d / 100;
  if (c >= P / 2) c = 5;
  var a = cent((P - c) * f), b = cent(P * f - c), tp = aleatorio(1, 3), q = { pistas: {} }, o = { P: dinero(P), c: dinero(c), d: d, f: nd(f), a: dinero(a), b: dinero(b), m: dinero(cent(P * f)) };
  if (tp === 3){
    q.enun = F(TXT.o3, o); q.enOrden = true; q.correcta = "pc";
    q.opciones = [{ html: TXT.oPc, clave: "pc" }, { html: TXT.oCp, clave: "cp" }, { html: TXT.oIg, clave: "igual" }];
    o.d = dinero(cent(a - b)); q.bien = q.mal = F(TXT.o3s, o); q.pistas.igual = TXT.o3i;
    return q;
  }
  var cup = tp === 1, cor = cup ? a : b, otro = cup ? b : a, sinC = cent(P * f), dol = cent(P - c - d);
  q.enun = F(TXT.o12, { P: o.P, d: d, c: o.c, x: cup ? TXT.oCupPrim : TXT.oPctPrim });
  var vals = [cor, otro, sinC, dol].filter(function(v, i, arr){ return v > 0 && arr.indexOf(v) === i; });
  q.opciones = vals.map(function(v){ return { html: dinero2(v), clave: "v" + v }; }); q.correcta = "v" + cor;
  q.pistas["v" + otro] = TXT.oOtro; q.pistas["v" + sinC] = TXT.oFalta; q.pistas["v" + dol] = F(TXT.oDol, { d: d });
  q.bien = q.mal = F(cup ? TXT.oS1 : TXT.oS2, o);
  return q;
}

/* ============ Start ============ */
creaPracticaLibre("p1", genCotidiana);
$("pr-c").addEventListener("input", pintaPR); pintaPR();
creaPracticaLibre("p2", genPropina);
["si-p", "si-d", "si-d2", "si-i"].forEach(function(id){ $(id).addEventListener("input", pintaSI); }); pintaSI();
creaPracticaLibre("p3", genEncadenado);
["or-p", "or-c", "or-d"].forEach(function(id){ $(id).addEventListener("input", pintaOR); }); pintaOR();
creaPracticaOM("p4", genOrden);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA_D = ("Type only the number. It may have cents, like 9.90; you may use the $ sign.", "Escriba solo el número. Puede llevar centavos, como 9.90; puede usar el signo $.")

def practica_pagina():
    n = N
    def caja_n(i, et, v):
        return f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="{i}" value="{v}"></div>'
    mods = [
     (t("everyday", "cotidianas"), t("Everyday applications", "Aplicaciones cotidianas"),
      f'''      <p>{t("A <strong>discount</strong> is subtracted from the price; <strong>sales tax</strong> and a <strong>tip</strong> are added; a <strong>commission</strong> is a percent of the sales. In every case, first find the percent of the amount, then decide whether to add it, subtract it, or leave it alone.", "El <strong>descuento</strong> se resta del precio; el <strong>impuesto</strong> y la <strong>propina</strong> se suman; la <strong>comisión</strong> es un porcentaje de las ventas. En todos los casos, primero se calcula el porcentaje de la cantidad y después se decide si se suma, se resta o se deja así.")}</p>
{libre_x("p1", t("Practice: at the store and the restaurant", "Practique: en la tienda y en el restaurante"), t("Answer", "Resultado"), t(*NOTA_D))}'''),
     (t("tip", "propina"), t("The tip in your head", "La propina mental"),
      f'''      <p>{t("To find 10%, move the decimal point one place to the left. 5% is half of that, 15% is 10% + 5%, and 20% is twice 10%.", "Para hallar el 10% se mueve el punto decimal un lugar a la izquierda. El 5% es la mitad, el 15% es 10% + 5% y el 20% es el doble del 10%.")}</p>
      <h3>{t("Figure the tip step by step", "Calcule la propina paso a paso")}</h3>
      <div class="panel">
        <div class="campos">{caja_n("pr-c", t("Bill ($)", "Cuenta ($)"), 48)}</div>
        <div class="salida" id="pr-salida" aria-live="polite"></div>
      </div>
{libre_x("p2", t("Practice: tips", "Practique: propinas"), t("Tip ($)", "Propina ($)"), t(*NOTA_D))}'''),
     (t("chained", "encadenados"), t("Chained percents", "Porcentajes encadenados"),
      f'''      <p>{t("When a purchase has several percents, apply each one to the value <strong>at that moment</strong>. Two discounts in a row are not added: you multiply their factors.", "Cuando una compra tiene varios porcentajes, cada uno se aplica sobre el valor <strong>de ese momento</strong>. Dos descuentos seguidos no se suman: se multiplican sus factores.")}</p>
      <h3>{t("Shopping simulator", "Simulador de compra")}</h3>
      <div class="panel">
        <div class="campos">{caja_n("si-p", t("Price ($)", "Precio ($)"), 600)}{caja_n("si-d", t("Discount (%)", "Descuento (%)"), 15)}{caja_n("si-d2", t("Extra discount (%)", "Descuento adicional (%)"), 0)}{caja_n("si-i", t("Tax (%)", "Impuesto (%)"), 8.25)}</div>
        <div id="si-salida" aria-live="polite"></div>
      </div>
{libre_x("p3", t("Practice: chained purchases", "Practique: compras encadenadas"), t("Answer", "Resultado"), t("Type only the number, with no % sign. It may have decimals; for money you may use the $ sign.", "Escriba solo el número, sin el signo %. Puede llevar decimales; si es dinero, puede usar el signo $."))}'''),
     (t("order", "orden"), t("Does the order matter? The dollar coupon", "¿Importa el orden? El cupón fijo"),
      f'''      <p>{t("With two percents, the order does not change the answer. But with a percent and a fixed dollar coupon, it does: the coupon is worth more if it comes off at the end.", "Con dos porcentajes, el orden no cambia el resultado. Pero con un porcentaje y un cupón fijo en dólares, sí: el cupón vale más si se resta al final.")}</p>
      <h3>{t("Compare the two orders", "Compare los dos órdenes")}</h3>
      <div class="panel">
        <div class="campos">{caja_n("or-p", t("Price ($)", "Precio ($)"), 60)}{caja_n("or-c", t("Coupon ($)", "Cupón ($)"), 10)}{caja_n("or-d", t("Discount (%)", "Descuento (%)"), 20)}</div>
        <div id="or-salida" aria-live="polite"></div>
      </div>
{B.om("p4", t("Practice: how much do you pay?", "Practique: ¿cuánto se paga?"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    estilo = (".recibo{font-family:Consolas,'Courier New',monospace;background:#fffdf7;border:1px dashed #8d6e63;max-width:380px;margin:14px auto;padding:14px 18px;font-size:15px;}"
              ".recibo h4{text-align:center;margin:0 0 8px;color:#333;font-size:15px;} .recibo .l{display:flex;justify-content:space-between;gap:10px;}"
              ".recibo .sep{border-top:1px dashed #8d6e63;margin:6px 0;} .recibo .tot{font-weight:700;}"
              ".dos-col{display:grid;grid-template-columns:1fr 1fr;gap:14px;} .dos-col .recibo{width:100%;box-sizing:border-box;} @media (max-width:640px){ .dos-col{grid-template-columns:1fr;} }")
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=estilo, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Descuento, impuesto, propina y aplicaciones mixtas")
