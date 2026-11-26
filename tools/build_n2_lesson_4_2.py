"""Level 2 · Lesson 4.2 · Direct proportions: the rule of three — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import fr, pasos_panel

B.NIVEL = 2
N = "4-2"
TEMA = ("Ratios, rates, and proportions", "Razones, proporciones y porcentajes")
TIT = ("Direct proportions: the rule of three", "Proporciones directas: regla de tres y resolver proporciones")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def regla3(a, b, c, d):
    """Dos filas de la regla de tres."""
    f = lambda x, y: f'<span style="display:flex;gap:14px;justify-content:center;font-size:1.25rem;font-weight:700;color:#0d47a1"><span>{x}</span><span aria-hidden="true">→</span><span class="cap-oculto">{t("goes with", "corresponde a")}</span><span>{y}</span></span>'
    return f'<span style="display:block;background:#fff;border:2px solid #b2dfdb;border-radius:12px;padding:10px;margin:10px auto;max-width:320px">{f(a, b)}{f(c, d)}</span>'

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 4.1 you learned to write ratios and find unit rates to compare options. This lesson takes the natural next step: when two ratios show the same relationship, they form a <strong>proportion</strong>. A proportion lets you do more than compare: it lets you predict an unknown quantity. This lesson is about <strong>direct</strong> proportions; inverse proportions come in Lesson 4.3.",
"En la Lección 4.1 aprendió a escribir razones y a calcular tasas unitarias para comparar opciones. Esta lección da el paso natural: cuando dos razones representan la misma relación, forman una <strong>proporción</strong>. Las proporciones permiten más que comparar: permiten predecir una cantidad desconocida. Aquí se estudian las proporciones <strong>directas</strong>; las inversas quedan para la Lección 4.3.")}</p>
<p>{t("A <strong>proportion</strong> is an equation between two equivalent ratios. If two ratios simplify to the same result, they are equal, and together they form a proportion.", "Una <strong>proporción</strong> es una igualdad entre dos razones equivalentes. Si dos razones se simplifican al mismo resultado, son iguales y juntas forman una proporción.")}</p>
<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{fr("a", "b")} = {fr("c", "d")}</p>
<p>{t("It is read “a is to b as c is to d.”", "Se lee «a es a b como c es a d».")}</p>
{ej(t("Example: is it a proportion?", "Ejemplo: ¿es una proporción?"), t(f"Do the ratios {fr(2, 3)} and {fr(8, 12)} form a proportion?", f"¿Forman una proporción las razones {fr(2, 3)} y {fr(8, 12)}?"),
  [("1", t("Simplify.", "Simplifique."), t(f"{fr(8, 12)} = {fr(2, 3)} (divide by 4).", f"{fr(8, 12)} = {fr(2, 3)} (dividiendo entre 4).")),
   ("2", t("Or compare cross products.", "O compare los productos cruzados."), "2 × 12 = 24 " + t("and", "y") + " 3 × 8 = 24."),
   ("✓", t("Answer.", "Respuesta."), t(f"<strong>Yes</strong>: {fr(2, 3)} = {fr(8, 12)} is a proportion.", f"<strong>Sí</strong>: {fr(2, 3)} = {fr(8, 12)} es una proporción."))])}
{caja("tip", t("Key idea", "Idea clave"), t("<p>A proportion keeps the ratio between two quantities the same, even when their sizes change. That is why you can scale: a recipe for 2 people can become a recipe for 10 without changing the taste.</p>", "<p>Una proporción mantiene constante la razón entre dos cantidades, aunque cambien sus tamaños. Por eso permite escalar: una receta para 2 personas se puede convertir en una para 10 sin cambiar el sabor.</p>"))}
{practica("p1", t("Practice 1 — Is it a proportion?", "Práctica 1 — ¿Es una proporción?"), t(f"Do {fr(3, 5)} and {fr(9, 15)} form a proportion?", f"¿Forman una proporción {fr(3, 5)} y {fr(9, 15)}?"),
          [("a", t("Yes", "Sí")), ("b", "No")])}
{enlace(n, t("proportion", "proporcion"), t("what a proportion is", "qué es una proporción"), t("Decide whether two ratios form a proportion by simplifying them or comparing cross products.", "Decida si dos razones forman una proporción simplificándolas o comparando sus productos cruzados."))}'''

    s2 = f'''<p>{t("Two quantities are in <strong>direct proportion</strong> when, as one grows, the other grows <strong>in the same ratio</strong>: if one doubles, the other doubles; if one triples, the other triples. The test is simple: divide each pair of values. If the quotient is always the same, the relationship is proportional. That fixed quotient is the <strong>constant of proportionality</strong>.",
"Una relación entre dos cantidades es de <strong>proporcionalidad directa</strong> cuando, al aumentar una, la otra aumenta <strong>en la misma razón</strong>: si una se duplica, la otra se duplica; si una se triplica, la otra se triplica. La prueba es sencilla: se divide cada pareja de valores. Si el cociente es siempre el mismo, la relación es proporcional. Ese cociente fijo se llama <strong>constante de proporcionalidad</strong>.")}</p>
{tabla(t("Table A: pay at $15 an hour", "Tabla A: pago a $15 la hora"), t("Table A: hours worked, pay, and pay divided by hours", "Tabla A: horas trabajadas, pago y pago entre horas"),
       [t("Hours", "Horas"), "1", "2", "3", "4"], [[t("Pay ($)", "Pago ($)"), "15", "30", "45", "60"], [t("Pay ÷ hours", "Pago ÷ horas"), "15", "15", "15", "15"]])}
<p>{t("The quotient is always 15: Table A <strong>is</strong> proportional.", "El cociente es siempre 15: la Tabla A <strong>sí</strong> es proporcional.")}</p>
{tabla(t("Table B: a taxi with a $3.00 fixed charge plus $2.25 a mile", "Tabla B: taxi con $3.00 fijos más $2.25 por milla"), t("Table B: miles, cost, and cost divided by miles", "Tabla B: millas, costo y costo entre millas"),
       [t("Miles", "Millas"), "1", "2", "3", "4"], [[t("Cost ($)", "Costo ($)"), "5.25", "7.50", "9.75", "12.00"], [t("Cost ÷ miles", "Costo ÷ millas"), "5.25", "3.75", "3.25", "3.00"]])}
<p>{t("The cost grows with the miles, but the quotient <strong>changes</strong>. Table B is <strong>not</strong> proportional: 2 miles do not cost twice as much as 1 mile.", "El costo aumenta con las millas, pero el cociente <strong>cambia</strong>. La Tabla B <strong>no</strong> es proporcional: 2 millas no cuestan el doble que 1 milla.")}</p>
{caja("ojo", t("Growing together is not enough", "Crecer juntas no basta"), t("<p>Any fixed charge (a sign-up fee, the base fare of a taxi, the monthly fee of a phone plan) breaks the proportion, because the cost of zero units is not zero.</p>", "<p>Cualquier cargo fijo (una inscripción, el banderazo del taxi, la cuota de un plan de teléfono) rompe la proporcionalidad, porque el costo de cero unidades no es cero.</p>"))}
{practica("p2", t("Practice 2 — Gas and miles", "Práctica 2 — Gasolina y millas"), t("Gallons: 2, 4, 6. Miles: 50, 100, 150. Is it proportional?", "Galones: 2, 4, 6. Millas: 50, 100, 150. ¿Es proporcional?"),
          [("a", t("Yes, it is proportional", "Sí es proporcional")), ("b", t("No, it is not proportional", "No es proporcional"))])}
{practica("p3", t("Practice 3 — A data plan", "Práctica 3 — Un plan de datos"), t("Data: 1, 2, 3 GB. Monthly cost: $30, $40, $50. Is it proportional?", "Datos: 1, 2, 3 GB. Costo mensual: $30, $40, $50. ¿Es proporcional?"),
          [("a", t("Yes, it is proportional", "Sí es proporcional")), ("b", t("No, it is not proportional", "No es proporcional"))])}
{enlace(n, t("constant", "constante"), t("the constant-ratio test", "la prueba de la razón constante"), t("Divide each pair of values in a table and decide whether it is proportional.", "Divida cada pareja de valores de una tabla y decida si es proporcional."))}'''

    s3 = f'''<p>{t("The power of proportions is in one simple rule: if two ratios are equal, their <strong>cross products</strong> are equal too.", "El gran poder de las proporciones está en una regla muy simple: si dos razones son iguales, sus <strong>productos cruzados</strong> también son iguales.")}</p>
<p style="text-align:center;font-size:1.25rem;font-weight:700;color:#0d47a1">{t("If", "Si")} {fr("a", "b")} = {fr("c", "d")}, {t("then", "entonces")} a × d = b × c</p>
{ej(t("Example: find the missing term", "Ejemplo: hallar el término que falta"), t(f"Solve {fr(3, 8)} = {fr('x', 24)}.", f"Resuelva {fr(3, 8)} = {fr('x', 24)}."),
  [("1", t("Cross products.", "Productos cruzados."), "3 × 24 = 8 × x."),
   ("2", t("Work out the known side.", "Calcule el lado conocido."), "72 = 8x."),
   ("3", t("Solve for x.", "Despeje x."), t("Divide by 8: x = 72 ÷ 8 = 9.", "Se divide entre 8: x = 72 ÷ 8 = 9.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 9</strong>")])}
{caja("ojo", t("Only with two equal ratios", "Solo con dos razones iguales"), t("<p>Cross products work only when there is an equation between two ratios. They do not apply when you add or subtract fractions, or to a single fraction.</p>", "<p>El producto cruzado solo funciona cuando hay una igualdad entre dos razones. No se aplica al sumar o restar fracciones, ni a una fracción sola.</p>"))}
{practica("p4", t("Practice 4 — Find x", "Práctica 4 — Halle x"), t(f"Solve {fr(4, 6)} = {fr('x', 18)}.", f"Resuelva {fr(4, 6)} = {fr('x', 18)}."),
          [("a", "x = 16"), ("b", "x = 27"), ("c", "x = 12"), ("d", "x = 3")])}
{practica("p5", t("Practice 5 — x in the denominator", "Práctica 5 — La x abajo"), t(f"Solve {fr(5, 'x')} = {fr(15, 21)}.", f"Resuelva {fr(5, 'x')} = {fr(15, 21)}."),
          [("a", "x = 7"), ("b", "x = 63"), ("c", "x = 11"), ("d", "x = 3")])}
{enlace(n, t("cross-products", "producto-cruzado"), t("the cross-product rule", "la regla del producto cruzado"), t("Solve for the missing term, wherever it is, step by step.", "Despeje el término que falta, esté donde esté, paso a paso."))}'''

    s4 = f'''<p>{t("The <strong>rule of three</strong> is the traditional way to set up a proportion when you know three values and want the fourth. Write the data in two rows, with <strong>the same units in the same column</strong>.", "La <strong>regla de tres</strong> es la forma tradicional de plantear una proporción cuando se conocen tres datos y se busca el cuarto. Se colocan los datos en dos filas, con <strong>las mismas unidades en la misma columna</strong>.")}</p>
{ej(t("Example: at the market", "Ejemplo: en el mercado"), t("If 3 pounds of tomatoes cost $4.50, how much do 8 pounds cost?", "Si 3 libras de tomate cuestan $4.50, ¿cuánto cuestan 8 libras?") + regla3("3 lb", "$4.50", "8 lb", "x"),
  [("1", t("Is it direct?", "¿Es directa?"), t("More pounds, more money, in the same ratio: yes.", "Más libras, más dinero, en la misma razón: sí.")),
   ("2", t("Cross-multiply and divide.", "Multiplique en cruz y divida."), "x = (8 × 4.50) ÷ 3 = 36 ÷ 3 = 12."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$12.00</strong>", "<strong>$12.00</strong>"))])}
{caja("tip", t("Shortcut with the unit rate", "Atajo con la tasa unitaria"), t("<p>You can also find the price of 1 pound first ($4.50 ÷ 3 = $1.50) and multiply by 8 ($12.00). It is the unit rate from Lesson 4.1 put to work.</p>", "<p>También se puede hallar primero cuánto cuesta 1 libra ($4.50 ÷ 3 = $1.50) y multiplicar por 8 ($12.00). Es la tasa unitaria de la Lección 4.1 puesta a trabajar.</p>"))}
<p>{t("GED problems often show direct proportions in recipes, maps, currency exchange, and mixtures. The method is always the same: <strong>set up the ratios with the units lined up, solve, and check</strong>.", "Los problemas del GED suelen presentar proporciones directas en recetas, mapas, cambio de moneda y mezclas. El procedimiento es siempre el mismo: <strong>plantear con las unidades alineadas, resolver y verificar</strong>.")}</p>
{ej(t("Example: a recipe", "Ejemplo: una receta"), t("A recipe uses 4 cups of flour for 12 cookies. How much flour do you need for 30 cookies?", "Una receta usa 4 tazas de harina para 12 galletas. ¿Cuánta harina se necesita para 30 galletas?"),
  [("1", t("Set up.", "Plantee."), t(f"Flour on top, cookies on the bottom in both ratios: {fr(4, 12)} = {fr('x', 30)}.", f"Harina arriba y galletas abajo en las dos razones: {fr(4, 12)} = {fr('x', 30)}.")),
   ("2", t("Cross products.", "Productos cruzados."), "4 × 30 = 12x → 120 = 12x."),
   ("3", t("Solve.", "Despeje."), "x = 120 ÷ 12 = 10."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>10 cups</strong> of flour. Check: 4 × 30 = 120 and 12 × 10 = 120. ✓", "<strong>10 tazas</strong> de harina. Verificación: 4 × 30 = 120 y 12 × 10 = 120. ✓"))])}
{ej(t("Example: a map scale", "Ejemplo: la escala de un mapa"), t("On a map, 1 inch stands for 25 miles. What real distance do 3.5 inches stand for?", "En un mapa, 1 pulgada representa 25 millas. ¿Qué distancia real representan 3.5 pulgadas?"),
  [("1", t("Set up.", "Plantee."), t(f"Inches on top, miles on the bottom: {fr(1, 25)} = {fr(3.5, 'x')}.", f"Pulgadas arriba, millas abajo: {fr(1, 25)} = {fr(3.5, 'x')}.")),
   ("2", t("Cross products.", "Productos cruzados."), "1 × x = 25 × 3.5 = 87.5."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>87.5 miles</strong>", "<strong>87.5 millas</strong>"))])}
{ej(t("Example: changing money", "Ejemplo: cambio de moneda"), t("Suppose the bank gives 18.50 Mexican pesos for 1 dollar. How many pesos do you get for $40? (The real exchange rate changes every day; this one is made up.)", "Supongamos que el banco da 18.50 pesos mexicanos por 1 dólar. ¿Cuántos pesos se reciben por $40? (La tasa de cambio real varía cada día; esta es supuesta.)"),
  [("1", t("Set up.", "Plantee."), t(f"Dollars on top, pesos on the bottom: {fr(1, '18.50')} = {fr(40, 'x')}.", f"Dólares arriba, pesos abajo: {fr(1, '18.50')} = {fr(40, 'x')}.")),
   ("✓", t("Solve.", "Despeje."), t("x = 40 × 18.50 = <strong>740 pesos</strong>.", "x = 40 × 18.50 = <strong>740 pesos</strong>."))])}
{caja("ojo", t("Common mistake: mixed-up units", "Error frecuente: mezclar las unidades"), t("<p>If flour is on top in the first ratio, it must be on top in the second ratio too. Flipping only one ratio gives a wrong answer.</p>", "<p>Si en la primera razón la harina va arriba, en la segunda también debe ir arriba. Invertir una sola razón da un resultado equivocado.</p>"))}
{calc(t("The rule of three on the calculator", "La regla de tres en la calculadora"), t(f"<p>For the tomatoes, type {T('8')} {T('×')} {T('4.50')} {T('÷')} {T('3')} {T('enter')}. The screen shows 12.</p>", f"<p>Para los tomates, escriba {T('8')} {T('×')} {T('4.50')} {T('÷')} {T('3')} {T('enter')}. La pantalla muestra 12.</p>"))}
{practica("p6", t("Practice 6 — Pencils", "Práctica 6 — Lápices"), t("If 5 pencils cost $1.25, how much do 12 pencils cost?", "Si 5 lápices cuestan $1.25, ¿cuánto cuestan 12 lápices?"),
          [("a", "$2.40"), ("b", "$15.00"), ("c", "$2.75"), ("d", "$3.00")])}
{practica("p7", t("Practice 7 — A map", "Práctica 7 — Un mapa"), t("On a map, 1 inch stands for 40 miles. How many miles do 2.5 inches stand for?", "En un mapa, 1 pulgada equivale a 40 millas. ¿Cuántas millas representan 2.5 pulgadas?"),
          [("a", t("80 miles", "80 millas")), ("b", t("100 miles", "100 millas")), ("c", t("42.5 miles", "42.5 millas")), ("d", t("16 miles", "16 millas"))])}
{practica("p8", t("Practice 8 — Cheese", "Práctica 8 — Queso"), t("A recipe for 4 servings uses 6 ounces of cheese. How many ounces do you need for 10 servings?", "Una receta para 4 porciones lleva 6 onzas de queso. ¿Cuántas onzas se necesitan para 10 porciones?"),
          [("a", t("12 ounces", "12 onzas")), ("b", t("24 ounces", "24 onzas")), ("c", t("15 ounces", "15 onzas")), ("d", t("6.7 ounces", "6.7 onzas"))])}
{enlace(n, t("direct", "directas"), t("solving direct proportions", "resolver proporciones directas"), t("Set up the two ratios in the same order and solve recipes, maps, and purchases.", "Plantee las dos razones en el mismo orden y resuelva recetas, mapas y compras."))}'''

    secciones = [("s-" + t("proportion", "proporcion"), t("What a proportion is", "Qué es una proporción"), s1),
                 ("s-" + t("constant", "constante"), t("Is it proportional? The constant-ratio test", "¿Es proporcional? La prueba de la razón constante"), s2),
                 ("s-" + t("cross-products", "producto-cruzado"), t("The cross-product rule", "La regla del producto cruzado"), s3),
                 ("s-" + t("rule-of-three", "regla-de-tres"), t("The rule of three and direct-proportion problems", "La regla de tres y los problemas de proporción directa"), s4)]

    lesson = {"next": t("Lesson 4.3", "Lección 4.3"), "review": t("sections 1, 3, and 4", "las secciones 1, 3 y 4"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Simplify 9/15: divide by 3.", "Simplifique 9/15: divida entre 3.")},
             "right": t("9/15 = 3/5, and 3 × 15 = 5 × 9 = 45.", "9/15 = 3/5, y 3 × 15 = 5 × 9 = 45."), "solution": t("9/15 simplifies to 3/5. The cross products are 3 × 15 = 45 and 5 × 9 = 45: it is a proportion.", "9/15 se simplifica a 3/5. Los productos cruzados son 3 × 15 = 45 y 5 × 9 = 45: es una proporción.")},
      "p2": {"ok": "a", "hints": {"b": t("Divide each pair: 50 ÷ 2, 100 ÷ 4, 150 ÷ 6.", "Divida cada pareja: 50 ÷ 2, 100 ÷ 4, 150 ÷ 6.")},
             "right": t("Every quotient is 25 miles per gallon.", "Todos los cocientes valen 25 millas por galón."), "solution": t("50 ÷ 2 = 25, 100 ÷ 4 = 25, 150 ÷ 6 = 25. The quotient is constant: it is proportional.", "50 ÷ 2 = 25, 100 ÷ 4 = 25, 150 ÷ 6 = 25. El cociente es constante: es proporcional.")},
      "p3": {"ok": "b", "hints": {"a": t("Divide each pair: 30 ÷ 1, 40 ÷ 2, 50 ÷ 3. Are they equal?", "Divida cada pareja: 30 ÷ 1, 40 ÷ 2, 50 ÷ 3. ¿Son iguales?")},
             "right": t("30, 20, and about 16.67: the quotient changes.", "30, 20 y unos 16.67: el cociente cambia."), "solution": t("30 ÷ 1 = 30, 40 ÷ 2 = 20, 50 ÷ 3 ≈ 16.67. The quotient changes, so it is not proportional. The plan has a fixed charge of $20.", "30 ÷ 1 = 30, 40 ÷ 2 = 20, 50 ÷ 3 ≈ 16.67. El cociente cambia, así que no es proporcional. El plan tiene un cargo fijo de $20.")},
      "p4": {"ok": "c", "hints": {"a": t("You added 12 to the top. Use cross products: 4 × 18 = 6x.", "Le sumó 12 al numerador. Use el producto cruzado: 4 × 18 = 6x."), "b": t("You multiplied the wrong pair: 6 × 18 ÷ 4.", "Multiplicó la pareja equivocada: 6 × 18 ÷ 4."), "d": t("Check: 4 × 18 = 72, then 72 ÷ 6.", "Revise: 4 × 18 = 72, después 72 ÷ 6.")},
             "right": t("4 × 18 = 72; 72 ÷ 6 = 12.", "4 × 18 = 72; 72 ÷ 6 = 12."), "solution": t("Cross products: 4 × 18 = 6x, so 72 = 6x and x = 12.", "Producto cruzado: 4 × 18 = 6x, así que 72 = 6x y x = 12.")},
      "p5": {"ok": "a", "hints": {"b": t("You multiplied the wrong pair. Cross products: 5 × 21 = 15x.", "Multiplicó la pareja equivocada. Producto cruzado: 5 × 21 = 15x."), "c": t("You subtracted 10 from the bottom. Ratios do not work by adding or subtracting.", "Le restó 10 al denominador. Las razones no funcionan sumando ni restando."), "d": t("Check: 5 × 21 = 105, then 105 ÷ 15.", "Revise: 5 × 21 = 105, después 105 ÷ 15.")},
             "right": t("5 × 21 = 105; 105 ÷ 15 = 7.", "5 × 21 = 105; 105 ÷ 15 = 7."), "solution": t("Cross products: 5 × 21 = 15x, so 105 = 15x and x = 7.", "Producto cruzado: 5 × 21 = 15x, así que 105 = 15x y x = 7.")},
      "p6": {"ok": "d", "hints": {"a": t("Check the unit price: $1.25 ÷ 5 = $0.25.", "Revise el precio unitario: $1.25 ÷ 5 = $0.25."), "b": t("You multiplied 1.25 × 12. Divide by 5 too.", "Multiplicó 1.25 × 12. Falta dividir entre 5."), "c": t("You added. Use the rule of three: 12 × 1.25 ÷ 5.", "Sumó. Use la regla de tres: 12 × 1.25 ÷ 5.")},
             "right": t("12 × 1.25 ÷ 5 = $3.00.", "12 × 1.25 ÷ 5 = $3.00."), "solution": t("1 pencil costs $1.25 ÷ 5 = $0.25. 12 pencils cost 12 × $0.25 = $3.00.", "1 lápiz cuesta $1.25 ÷ 5 = $0.25. 12 lápices cuestan 12 × $0.25 = $3.00.")},
      "p7": {"ok": "b", "hints": {"a": t("That is 2 inches. Do not forget the half inch.", "Eso son 2 pulgadas. No olvide la media pulgada."), "c": t("You added. Multiply: 40 × 2.5.", "Sumó. Multiplique: 40 × 2.5."), "d": t("You divided. Multiply: 40 × 2.5.", "Dividió. Multiplique: 40 × 2.5.")},
             "right": t("40 × 2.5 = 100 miles.", "40 × 2.5 = 100 millas."), "solution": t("1/40 = 2.5/x, so x = 40 × 2.5 = 100 miles.", "1/40 = 2.5/x, así que x = 40 × 2.5 = 100 millas.")},
      "p8": {"ok": "c", "hints": {"a": t("You added. Use cross products: 6 × 10 = 4x.", "Sumó. Use el producto cruzado: 6 × 10 = 4x."), "b": t("Check: 6 × 10 = 60, then 60 ÷ 4.", "Revise: 6 × 10 = 60, después 60 ÷ 4."), "d": t("One ratio is flipped. Keep cheese on top in both.", "Una razón está invertida. Ponga el queso arriba en las dos.")},
             "right": t("6 × 10 ÷ 4 = 15 ounces.", "6 × 10 ÷ 4 = 15 onzas."), "solution": t("6/4 = x/10, so 4x = 60 and x = 15 ounces.", "6/4 = x/10, así que 4x = 60 y x = 15 onzas.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The cross products are equal, but check the other reason given.", "Los productos cruzados sí son iguales; revise las razones de las otras opciones."), "b": t("Multiply: 4 × 15 and 10 × 6.", "Multiplique: 4 × 15 y 10 × 6."), "d": t("Subtracting the terms does not tell you anything.", "Restar los términos no dice nada.")}, "solution": t("4 × 15 = 60 and 10 × 6 = 60: they form a proportion.", "4 × 15 = 60 y 10 × 6 = 60: forman una proporción.")},
      "B": {"ok": "b", "hints": {"a": t("5 ÷ 1 = 5, but 7 ÷ 2 = 3.5: the quotient changes.", "5 ÷ 1 = 5, pero 7 ÷ 2 = 3.5: el cociente cambia."), "c": t("Height grows with age, but not in the same ratio.", "La estatura crece con la edad, pero no en la misma razón."), "d": t("There is a fixed charge: 30, 20, 16.67…", "Hay un cargo fijo: 30, 20, 16.67…")}, "solution": t("12 ÷ 1 = 24 ÷ 2 = 36 ÷ 3 = 12: the quotient is constant.", "12 ÷ 1 = 24 ÷ 2 = 36 ÷ 3 = 12: el cociente es constante.")},
      "C": {"ok": "d", "hints": {"a": t("You multiplied the wrong pair: 8 × 24 ÷ 3.", "Multiplicó la pareja equivocada: 8 × 24 ÷ 3."), "b": t("You added 16. Ratios are not solved by adding.", "Sumó 16. Las razones no se resuelven sumando."), "c": t("Check: 3 × 24 = 72, then 72 ÷ 8.", "Revise: 3 × 24 = 72, después 72 ÷ 8.")}, "solution": t("3 × 24 = 8x, so 72 = 8x and x = 9.", "3 × 24 = 8x, así que 72 = 8x y x = 9.")},
      "D": {"ok": "a", "hints": {"b": t("You added 21. Use cross products: 12 × 28 = 7x.", "Sumó 21. Use el producto cruzado: 12 × 28 = 7x."), "c": t("You multiplied the wrong pair.", "Multiplicó la pareja equivocada."), "d": t("Check: 12 × 28 = 336, then 336 ÷ 7.", "Revise: 12 × 28 = 336, después 336 ÷ 7.")}, "solution": t("7x = 12 × 28 = 336, so x = 48.", "7x = 12 × 28 = 336, así que x = 48.")},
      "E": {"ok": "b", "hints": {"a": t("You added. Use the unit price: $4.50 ÷ 3 = $1.50.", "Sumó. Use el precio unitario: $4.50 ÷ 3 = $1.50."), "c": t("Check: $1.50 × 8.", "Revise: $1.50 × 8."), "d": t("You multiplied 4.50 × 8. Divide by 3 too.", "Multiplicó 4.50 × 8. Falta dividir entre 3.")}, "solution": t("8 × 4.50 ÷ 3 = $12.00.", "8 × 4.50 ÷ 3 = $12.00.")},
      "F": {"ok": "c", "hints": {"a": t("You added 18. Use cross products: 4 × 30 = 12x.", "Sumó 18. Use el producto cruzado: 4 × 30 = 12x."), "b": t("One ratio is flipped. Flour on top in both.", "Una razón está invertida. La harina va arriba en las dos."), "d": t("Check: 4 × 30 = 120, then 120 ÷ 12.", "Revise: 4 × 30 = 120, después 120 ÷ 12.")}, "solution": t("4/12 = x/30, so 12x = 120 and x = 10 cups.", "4/12 = x/30, así que 12x = 120 y x = 10 tazas.")},
      "G": {"ok": "d", "hints": {"a": t("You added. Multiply: 25 × 3.5.", "Sumó. Multiplique: 25 × 3.5."), "b": t("You divided. Multiply: 25 × 3.5.", "Dividió. Multiplique: 25 × 3.5."), "c": t("That is 3 inches. Do not forget the half inch.", "Eso son 3 pulgadas. No olvide la media pulgada.")}, "solution": t("1/25 = 3.5/x, so x = 25 × 3.5 = 87.5 miles.", "1/25 = 3.5/x, así que x = 25 × 3.5 = 87.5 millas.")},
      "H": {"ok": "a", "hints": {"b": t("You divided 40 by 18.50. Multiply.", "Dividió 40 entre 18.50. Multiplique."), "c": t("You added. Multiply.", "Sumó. Multiplique."), "d": t("Check the decimal point: 40 × 18.50 = 740.", "Revise el punto decimal: 40 × 18.50 = 740.")}, "solution": t("40 × 18.50 = 740 pesos.", "40 × 18.50 = 740 pesos.")}
     }}

    quiz = [
     ("A", t(f"Do {fr(4, 10)} and {fr(6, 15)} form a proportion?", f"¿Forman una proporción {fr(4, 10)} y {fr(6, 15)}?"),
      [("a", t("No, because 4 × 15 and 10 × 6 are different", "No, porque 4 × 15 y 10 × 6 son distintos")), ("b", t("You cannot tell without simplifying", "No se puede saber sin simplificar")), ("c", t("Yes: 4 × 15 = 60 and 10 × 6 = 60", "Sí: 4 × 15 = 60 y 10 × 6 = 60")), ("d", t("No, because 6 − 4 is not 15 − 10", "No, porque 6 − 4 no es 15 − 10"))]),
     ("B", t("Which table is proportional?", "¿Qué tabla es proporcional?"),
      [("a", t("Miles 1, 2, 3 → cost $5, $7, $9", "Millas 1, 2, 3 → costo $5, $7, $9")), ("b", t("Hours 1, 2, 3 → pay $12, $24, $36", "Horas 1, 2, 3 → pago $12, $24, $36")), ("c", t("Age 5, 10, 15 → height 44, 56, 64 inches", "Edad 5, 10, 15 → estatura 44, 56, 64 pulgadas")), ("d", t("GB 1, 2, 3 → cost $30, $40, $50", "GB 1, 2, 3 → costo $30, $40, $50"))]),
     ("C", t(f"Solve {fr(3, 8)} = {fr('x', 24)}.", f"Resuelva {fr(3, 8)} = {fr('x', 24)}."), [("a", "x = 64"), ("b", "x = 19"), ("c", "x = 8"), ("d", "x = 9")]),
     ("D", t(f"Solve {fr(7, 12)} = {fr(28, 'x')}.", f"Resuelva {fr(7, 12)} = {fr(28, 'x')}."), [("a", "x = 48"), ("b", "x = 33"), ("c", "x = 3"), ("d", "x = 16")]),
     ("E", t("3 pounds of tomatoes cost $4.50. How much do 8 pounds cost?", "3 libras de tomate cuestan $4.50. ¿Cuánto cuestan 8 libras?"), [("a", "$9.50"), ("b", "$12.00"), ("c", "$13.50"), ("d", "$36.00")]),
     ("F", t("A recipe uses 4 cups of flour for 12 cookies. How many cups do you need for 30 cookies?", "Una receta usa 4 tazas de harina para 12 galletas. ¿Cuántas tazas se necesitan para 30 galletas?"), [("a", "22"), ("b", "1.6"), ("c", "10"), ("d", "40")]),
     ("G", t("On a map, 1 inch stands for 25 miles. How many miles do 3.5 inches stand for?", "En un mapa, 1 pulgada representa 25 millas. ¿Cuántas millas representan 3.5 pulgadas?"), [("a", "28.5"), ("b", "7.14"), ("c", "75"), ("d", "87.5")]),
     ("H", t("At 18.50 pesos per dollar, how many pesos do you get for $40?", "A 18.50 pesos por dólar, ¿cuántos pesos se reciben por $40?"), [("a", "740"), ("b", "2.16"), ("c", "58.50"), ("d", "74")])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("From comparing to predicting: proportions, the constant-ratio test, cross products, and the rule of three.", "De comparar a predecir: las proporciones, la prueba de la razón constante, el producto cruzado y la regla de tres."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Recognize</strong> a proportion as an equation between two ratios.", "<strong>Reconocer</strong> una proporción como una igualdad entre dos razones."),
         t("<strong>Decide</strong> whether a table is proportional with the constant-ratio test.", "<strong>Decidir</strong> si una tabla es proporcional con la prueba de la razón constante."),
         t("<strong>Use</strong> cross products to find a missing term.", "<strong>Usar</strong> el producto cruzado para hallar un término desconocido."),
         t("<strong>Solve</strong> direct-proportion problems with the rule of three: recipes, maps, money.", "<strong>Resolver</strong> problemas de proporción directa con la regla de tres: recetas, mapas, dinero."),
         t("<strong>Check</strong> the answer by substituting it into the proportion.", "<strong>Verificar</strong> el resultado sustituyéndolo en la proporción.")],
        secciones,
        (t("Make three tables of values and decide whether each one is proportional; use real prices from your supermarket for one of them. Solve four proportions with cross products and check each answer. Solve three real direct-proportion problems: a recipe from home for a different number of servings, a distance on a map, and a currency exchange.",
           "Haga tres tablas de valores y decida si son proporcionales; use precios reales de su supermercado en una de ellas. Resuelva cuatro proporciones con el producto cruzado y verifique cada resultado. Resuelva tres problemas reales de proporción directa: una receta de su casa para otro número de porciones, una distancia en un mapa y un cambio de moneda."),
         t("Take a recipe you make at home and rewrite it for twice as many people, and then for half. Check that the ratios between the ingredients stay the same.",
           "Tome una receta que prepare en casa y reescríbala para el doble de personas y después para la mitad. Compruebe que las razones entre los ingredientes no cambian.")),
        quiz,
        t("Self-check checklist for direct proportions", "Lista de autoevaluación de proporciones directas"),
        t("Self-check checklist: skills for direct proportions", "Lista de autoevaluación: destrezas de proporciones directas"),
        [(t("Set up with the units lined up", "Plantear con las unidades alineadas"), t("I put the same units in the same place and explain why it is proportional.", "Pongo las mismas unidades en el mismo lugar y explico por qué es proporcional."), t("I set it up with help; sometimes I flip a ratio.", "Planteo con ayuda; a veces invierto una razón."), t("I place the data without looking at the units.", "Coloco los datos sin fijarme en las unidades.")),
         (t("Cross products", "Producto cruzado"), t("I use them and solve for x with no mistakes; I also check with the unit rate.", "Lo aplico y despejo x sin errores; también compruebo con la tasa unitaria."), t("I use them with help.", "Lo aplico con ayuda."), t("I do not know which numbers to multiply.", "No sé qué números multiplicar.")),
         (t("Check", "Verificar"), t("I substitute the answer and see if it makes sense in context.", "Sustituyo el resultado y veo si tiene sentido en el contexto."), t("I check only when asked.", "Verifico solo cuando me lo piden."), t("I do not check.", "No verifico."))],
        t("<p>In this lesson the ratios of Lesson 4.1 became a tool for <strong>predicting</strong>: the <strong>direct proportion</strong>, recognized by its constant ratio and solved with cross products or the rule of three.</p>\n<p>In <strong>Lesson 4.3 · Inverse proportions and mixed applications</strong> you will study situations where one quantity grows while the other shrinks, like more workers and fewer days. There, what stays the same is not the ratio but the <strong>product</strong>.</p>",
          "<p>En esta lección las razones de la Lección 4.1 se convirtieron en una herramienta para <strong>predecir</strong>: la <strong>proporción directa</strong>, reconocida por su razón constante y resuelta con el producto cruzado o la regla de tres.</p>\n<p>En la <strong>Lección 4.3 · Proporciones inversas y aplicaciones mixtas</strong> estudiará las situaciones en que una cantidad aumenta mientras la otra disminuye, como más trabajadores y menos días. Allí lo constante ya no es la razón, sino el <strong>producto</strong>.</p>"),
        ("4-3", ("", t("Lesson 4.3 · Inverse proportions and mixed applications", "Lección 4.3 · Proporciones inversas y aplicaciones mixtas"))),
        [(t("proportion", "proporción"), t("An equation between two equal ratios, like 2/3 = 8/12.", "Igualdad entre dos razones equivalentes, como 2/3 = 8/12.")),
         (t("cross products", "productos cruzados"), t("In a/b = c/d, the products a × d and b × c. In a proportion they are equal.", "En a/b = c/d, los productos a × d y b × c. En una proporción son iguales.")),
         (t("constant of proportionality", "constante de proporcionalidad"), t("The fixed quotient y ÷ x in a direct proportion.", "El cociente fijo y ÷ x de una proporción directa.")),
         (t("rule of three", "regla de tres"), t("A way to set up a proportion in two rows when you know three values and want the fourth.", "Forma de plantear una proporción en dos filas cuando se conocen tres datos y se busca el cuarto."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "cuatroPos": "Type four positive numbers.", "simpl": "In simplest form: {a} and {b}.",
  "productos": "Cross products: {a} × {d} = {p1} and {b} × {c} = {p2}.", "siProp": "They are equal: yes, it is a proportion.", "noProp": "They are different: it is not a proportion.",
  "forman": "Do {f1} and {f2} form a proportion?", "si": "Yes", "no": "No",
  "expProd": "Cross products: {a} × {d} = {p1} and {b} × {c} = {p2}{x}", "iguales": ": equal.", "distintos": ": different.",
  "sumarIgual": " Adding the same amount to the top and the bottom does not keep the ratio.",
  "tabla": "Is this table proportional?", "cociente": "{y} ÷ {x}", "cocientes": "Quotients {y} ÷ {x}: {q}.",
  "esCte": "The quotient is always {k}: it is proportional.", "noCte": "The quotient changes: it is not proportional.",
  "cargo": " There is a fixed charge, so zero units would not cost zero.",
  "ctxT": [["Hours", "Pay ($)", "hours"], ["Pounds", "Cost ($)", "pounds"], ["Gallons", "Miles", "gallons"], ["Tickets", "Cost ($)", "tickets"], ["Miles", "Taxi fare ($)", "miles"], ["Months", "Gym cost ($)", "months"]],
  "p1": "Cross products: {a} × {d} = {b} × {c}.", "p2": "Work out the known side: {m} × {n} = {pr}, so {o}x = {pr}.", "p3": "Divide by {o}: x = {pr} ÷ {o} = {r}.",
  "p4": "x = {r}. Check: the two ratios are equal.", "halla": "Find x: {e}", "diagonal": "Check which numbers you multiply: the two on the diagonal without x.",
  "d1": "A recipe uses {a} cups of flour for {b} cookies. How many cups do you need for {c} cookies?",
  "d2": "On a map, {a} inches stand for {b} miles. How many miles do {c} inches stand for?",
  "d3": "{a} pounds of apples cost {b}. How much do {c} pounds cost, in dollars?",
  "d4": "On {a} gallons of gas a car goes {b} miles. How many miles does it go on {c} gallons?",
  "d5": "A person earns {b} for {a} hours of work. How much does the person earn for {c} hours, in dollars?",
  "u": [["cups", "cookies"], ["in", "mi"], ["lb", "$"], ["gal", "mi"], ["h", "$"]],
  "plantea": "Set up {s} and solve with cross products: x = {r}.", "orden": "It looks like the ratios are in a different order: keep the same quantity on top in both."
 },
 "es": {
  "cuatroPos": "Escriba cuatro números positivos.", "simpl": "Simplificadas: {a} y {b}.",
  "productos": "Productos cruzados: {a} × {d} = {p1} y {b} × {c} = {p2}.", "siProp": "Son iguales: sí forman una proporción.", "noProp": "No son iguales: no forman una proporción.",
  "forman": "¿Forman una proporción {f1} y {f2}?", "si": "Sí", "no": "No",
  "expProd": "Productos cruzados: {a} × {d} = {p1} y {b} × {c} = {p2}{x}", "iguales": ": iguales.", "distintos": ": distintos.",
  "sumarIgual": " Sumar lo mismo arriba y abajo no mantiene la razón.",
  "tabla": "¿Es proporcional esta tabla?", "cociente": "{y} ÷ {x}", "cocientes": "Cocientes {y} ÷ {x}: {q}.",
  "esCte": "El cociente es siempre {k}: es proporcional.", "noCte": "El cociente cambia: no es proporcional.",
  "cargo": " Hay un cargo fijo, así que cero unidades no costarían cero.",
  "ctxT": [["Horas", "Pago ($)", "horas"], ["Libras", "Costo ($)", "libras"], ["Galones", "Millas", "galones"], ["Entradas", "Costo ($)", "entradas"], ["Millas", "Taxi ($)", "millas"], ["Meses", "Gimnasio ($)", "meses"]],
  "p1": "Producto cruzado: {a} × {d} = {b} × {c}.", "p2": "Se calcula el lado conocido: {m} × {n} = {pr}, así que {o}x = {pr}.", "p3": "Se divide entre {o}: x = {pr} ÷ {o} = {r}.",
  "p4": "x = {r}. Comprobación: las dos razones valen lo mismo.", "halla": "Halle x: {e}", "diagonal": "Revise qué números se multiplican: son los dos de la diagonal sin la x.",
  "d1": "Una receta usa {a} tazas de harina para {b} galletas. ¿Cuántas tazas se necesitan para {c} galletas?",
  "d2": "En un mapa, {a} pulgadas representan {b} millas. ¿Cuántas millas representan {c} pulgadas?",
  "d3": "{a} libras de manzanas cuestan {b}. ¿Cuánto cuestan {c} libras, en dólares?",
  "d4": "Con {a} galones de gasolina un auto recorre {b} millas. ¿Cuántas millas recorre con {c} galones?",
  "d5": "Una persona gana {b} por {a} horas de trabajo. ¿Cuánto gana por {c} horas, en dólares?",
  "u": [["tazas", "galletas"], ["pulg", "mi"], ["lb", "$"], ["gal", "mi"], ["h", "$"]],
  "plantea": "Se plantea {s} y se resuelve con el producto cruzado: x = {r}.", "orden": "Parece que se mezcló el orden de las razones: mantenga la misma cantidad arriba en las dos."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function fq(a, b){ return '<span aria-hidden="true"><span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + '</span></span></span><span class="sr-only">' + a + '/' + b + '</span>'; }

/* ============ MODULE 1 · proportion? ============ */
function pintaPC(){
  var v = ["a", "b", "c", "d"].map(function(k){ return leeD($("pc-" + k).value); }), av = $("pc-aviso");
  if (v.some(function(x){ return x === null || x <= 0; })){ av.className = "caja-aviso visible"; av.textContent = TXT.cuatroPos; $("pc-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var p1 = v[0] * v[3], p2 = v[1] * v[2], ok = Math.abs(p1 - p2) < 1e-9;
  var h = '<div class="linea grande">' + fq(nd(v[0]), nd(v[1])) + (ok ? " = " : " ≠ ") + fq(nd(v[2]), nd(v[3])) + '</div>';
  if (v.every(function(x){ return x === Math.round(x); })){ var g1 = mcdR(v[0], v[1]), g2 = mcdR(v[2], v[3]); h += '<div class="linea">' + F(TXT.simpl, { a: fq(v[0] / g1, v[1] / g1), b: fq(v[2] / g2, v[3] / g2) }) + '</div>'; }
  h += '<div class="linea">' + F(TXT.productos, { a: nd(v[0]), b: nd(v[1]), c: nd(v[2]), d: nd(v[3]), p1: nd(p1), p2: nd(p2) }) + '</div>';
  h += '<div class="linea veredicto">' + (ok ? TXT.siProp : TXT.noProp) + '</div>';
  $("pc-salida").innerHTML = h;
}
function genEsProp(){
  var a = aleatorio(1, 9), b = aleatorio(2, 12); while (b === a) b = aleatorio(2, 12);
  var k = aleatorio(2, 6), si = Math.random() < 0.5, c = a * k, d = b * k, sumo = false;
  if (!si){ if (Math.random() < 0.5) d += elige([-1, 1, 2]); else { c = a + k; d = b + k; sumo = true; } }
  var ok = a * d === b * c;
  var exp = F(TXT.expProd, { a: a, b: b, c: c, d: d, p1: a * d, p2: b * c, x: ok ? TXT.iguales : TXT.distintos }) + (!ok && sumo ? TXT.sumarIgual : "");
  return { enun: F(TXT.forman, { f1: fq(a, b), f2: fq(c, d) }), opciones: [{ html: TXT.si, clave: "s" }, { html: TXT.no, clave: "n" }], correcta: ok ? "s" : "n", enOrden: true, bien: exp, mal: exp };
}

/* ============ MODULE 2 · constant ratio ============ */
function genTabla(){
  var c = elige(TXT.ctxT), prop = Math.random() < 0.5, k = elige([2, 3, 4, 5, 6, 8, 12, 15, 25]), f = aleatorio(2, 9) * (k < 6 ? 2 : 1);
  var x0 = aleatorio(1, 3), paso = aleatorio(1, 3), xs = [x0, x0 + paso, x0 + 2 * paso, x0 + 3 * paso];
  var ys = xs.map(function(x){ return prop ? k * x : f + k * x; });
  var q = xs.map(function(x, i){ return nd(Math.round(ys[i] / x * 100) / 100); });
  var tab = '<div class="tabla-scroll"><table class="tabla-trad"><tbody><tr><th scope="row">' + c[0] + '</th>' + xs.map(function(x){ return '<td>' + x + '</td>'; }).join("") + '</tr><tr><th scope="row">' + c[1] + '</th>' + ys.map(function(y){ return '<td>' + nd(y) + '</td>'; }).join("") + '</tr></tbody></table></div>';
  var exp = F(TXT.cocientes, { y: c[1], x: c[0].toLowerCase(), q: q.join(", ") }) + " " + (prop ? F(TXT.esCte, { k: nd(k) }) : TXT.noCte + TXT.cargo);
  return { enun: TXT.tabla + tab, opciones: [{ html: TXT.si, clave: "s" }, { html: TXT.no, clave: "n" }], correcta: prop ? "s" : "n", enOrden: true, bien: exp, mal: exp };
}

/* ============ MODULE 3 · cross products ============ */
function propAzar(){
  var a = aleatorio(2, 12), b = aleatorio(2, 12); while (b === a) b = aleatorio(2, 12);
  var k = elige([2, 3, 4, 5, 1.5, 2.5]), tt = [a, b, a * k, b * k];
  if (tt.some(function(x){ return x !== Math.round(x); })){ k = elige([2, 3, 4]); tt = [a, b, a * k, b * k]; }
  return { t: tt, pos: aleatorio(0, 3) };
}
function termino(q, i){ return i === q.pos ? "x" : nd(q.t[i]); }
function pasosCR(q){
  var tt = q.t, x = q.pos, l1 = [0, 3], l2 = [1, 2], conX = l1.indexOf(x) >= 0 ? l1 : l2, sin = conX === l1 ? l2 : l1;
  var otro = conX[0] === x ? conX[1] : conX[0], prod = tt[sin[0]] * tt[sin[1]], res = prod / tt[otro];
  return { res: res, malo: tt[otro] * tt[sin[0]] / tt[sin[1]], pasos: [
    F(TXT.p1, { a: termino(q, 0), d: termino(q, 3), b: termino(q, 1), c: termino(q, 2) }),
    F(TXT.p2, { m: nd(tt[sin[0]]), n: nd(tt[sin[1]]), pr: nd(prod), o: nd(tt[otro]) }),
    F(TXT.p3, { o: nd(tt[otro]), pr: nd(prod), r: nd(res) }),
    '<span class="veredicto">' + F(TXT.p4, { r: nd(res) }) + '</span>'] };
}
var CR_COLA = [{ t: [3, 8, 9, 24], pos: 2 }], CRS;
function nuevoCR(){ var q = CR_COLA.length ? CR_COLA.shift() : propAzar(); $("cr-expr").innerHTML = fq(termino(q, 0), termino(q, 1)) + " = " + fq(termino(q, 2), termino(q, 3)); CRS.carga(pasosCR(q).pasos); }
function genCR(){
  var q = propAzar(), R = pasosCR(q), p = [];
  if (Math.abs(R.malo - R.res) > 1e-9) p.push({ v: R.malo, msg: TXT.diagonal });
  return { enun: F(TXT.halla, { e: fq(termino(q, 0), termino(q, 1)) + " = " + fq(termino(q, 2), termino(q, 3)) }), correcta: nd(R.res), solucion: R.pasos.slice(0, 3).join(" "), evalua: numD(R.res, p) };
}

/* ============ MODULE 4 · direct proportions ============ */
function genDirecta(){
  for (var z = 0; z < 50; z++){
    var tp = aleatorio(1, 5), a, b, c, res, s, din = false, U = TXT.u[tp - 1];
    if (tp === 1){ a = aleatorio(2, 5); b = 6 * aleatorio(1, 3); var k = elige([2, 3, 1.5, 2.5]); c = b * k; res = a * k; }
    else if (tp === 2){ a = aleatorio(2, 6); b = elige([5, 10, 25, 50]); c = aleatorio(3, 12); res = b * c / a; }
    else if (tp === 3){ a = aleatorio(2, 6); var pu = elige([1.5, 2, 2.5, 3, 4]); b = a * pu; c = aleatorio(3, 12); res = c * pu; din = true; }
    else if (tp === 4){ a = aleatorio(2, 5); b = aleatorio(60, 200); var k2 = elige([2, 3, 4]); c = a * k2; res = b * k2; }
    else { a = aleatorio(3, 8); b = 5 * aleatorio(4, 12); c = aleatorio(10, 30); res = b * c / a; din = true; }
    if (Math.abs(res * 100 - Math.round(res * 100)) > 1e-6) continue;
    var bt = din ? dinero(b) : nd(b);
    s = fq(nd(a) + " " + U[0], bt + (din ? "" : " " + U[1])) + " = " + fq(nd(c) + " " + U[0], "x");
    var mal = tp === 1 ? a * b / c : (tp === 2 ? a * c / b : null);
    var p = mal !== null && Math.abs(mal - res) > 0.01 ? [{ v: mal, msg: TXT.orden }] : [];
    return { enun: F(TXT["d" + tp], { a: nd(a), b: bt, c: nd(c) }), correcta: din ? dinero(res) : nd(res), solucion: F(TXT.plantea, { s: s, r: din ? dinero(res) : nd(res) }), evalua: numD(res, p) };
  }
}

/* ============ Start ============ */
["pc-a", "pc-b", "pc-c", "pc-d"].forEach(function(id){ $(id).addEventListener("input", pintaPC); }); pintaPC();
creaPracticaOM("p1", genEsProp);
creaPracticaOM("p2", genTabla);
CRS = pasoAPaso("cr", []); $("cr-nuevo").addEventListener("click", nuevoCR); nuevoCR();
creaPracticaLibre("p3", genCR);
creaPracticaLibre("p4", genDirecta);
'''

def libre_d(pid, titulo, etiqueta):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."),
        t("Type only the number. It may have decimals, like 1.25; for money you may use the $ sign.", "Escriba solo el número. Puede llevar decimales, como 1.25; si es dinero, puede usar el signo $."))

def practica_pagina():
    n = N
    def caja_n(i, v):
        return f'<div class="campo"><label for="pc-{i}">{i}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="pc-{i}" value="{v}"></div>'
    frm = '<span class="fracc"><span class="fa">{}</span><span class="fb2">{}</span></span>'
    mods = [
     (t("proportion", "proporcion"), t("What a proportion is", "Qué es una proporción"),
      f'''      <p>{t("A <strong>proportion</strong> is an equation between two equal ratios: “a is to b as c is to d.” To find out whether two ratios form a proportion, simplify both or compare their cross products.", "Una <strong>proporción</strong> es una igualdad entre dos razones equivalentes: «a es a b como c es a d». Para saber si dos razones forman una proporción, se simplifican las dos o se comparan sus productos cruzados.")}</p>
      <h3>{t("Do they form a proportion?", "¿Forman una proporción?")}</h3>
      <div class="panel">
        <div class="campos">{caja_n("a", 2)}{caja_n("b", 3)}{caja_n("c", 8)}{caja_n("d", 12)}</div>
        <div class="caja-aviso" id="pc-aviso" role="alert"></div>
        <div class="salida" id="pc-salida" aria-live="polite"></div>
      </div>
{B.om("p1", t("Practice: is it a proportion?", "Practique: ¿es una proporción?"))}'''),
     (t("constant", "constante"), t("The constant-ratio test", "La prueba de la razón constante"),
      f'''      <p>{t("Two quantities are in direct proportion when the quotient of each pair of values (second ÷ first) is <strong>always the same</strong>. If the quotient changes, it is not proportional, even if both quantities grow together. A fixed charge always breaks the proportion.", "Dos cantidades están en proporción directa cuando el cociente de cada pareja de valores (segunda ÷ primera) es <strong>siempre el mismo</strong>. Si el cociente cambia, no es proporcional, aunque las dos cantidades crezcan juntas. Un cargo fijo siempre rompe la proporción.")}</p>
{B.om("p2", t("Practice: is the table proportional?", "Practique: ¿es proporcional la tabla?"))}'''),
     (t("cross-products", "producto-cruzado"), t("The cross-product rule", "La regla del producto cruzado"),
      f'''      <p>{t("If two ratios are equal, their <strong>cross products</strong> are equal too. With that rule you solve for the missing term, wherever it is.", "Si dos razones son iguales, sus <strong>productos cruzados</strong> también lo son. Con esa regla se despeja el término que falta, esté donde esté.")}</p>
      <div class="formula">{t("If", "Si")} {frm.format("a", "b")} = {frm.format("c", "d")}, {t("then", "entonces")} a × d = b × c</div>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos_panel("cr", t("Another proportion", "Otra proporción"))}
      <div class="caja-atencion"><strong>{t("Cross products work only with an equation between two ratios.", "El producto cruzado solo funciona con una igualdad de dos razones.")}</strong> {t("They are not for adding or subtracting fractions, or for a single fraction.", "No sirve para sumar o restar fracciones, ni con una fracción sola.")}</div>
{libre_d("p3", t("Practice: find x", "Practique: halle x"), t("Value of x", "Valor de x"))}'''),
     (t("direct", "directas"), t("Solving direct proportions", "Resolver proporciones directas"),
      f'''      <p>{t("In a direct proportion, write the two ratios <strong>in the same order</strong>: if the flour of the first case is on top, the flour of the second case is on top too. Then use cross products.", "En una proporción directa se plantean las dos razones <strong>con el mismo orden</strong>: si arriba va la harina del primer caso, arriba va la harina del segundo. Después, producto cruzado.")}</p>
      <div class="formula">{frm.format(t("4 cups", "4 tazas"), t("12 cookies", "12 galletas"))} = {frm.format(t("x cups", "x tazas"), t("30 cookies", "30 galletas"))} &nbsp;→&nbsp; 12x = 120 &nbsp;→&nbsp; x = 10</div>
{libre_d("p4", t("Practice: direct proportions", "Practique: proporciones directas"), t("Answer", "Resultado"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js", "/math/rates.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Proporciones directas: regla de tres y resolver proporciones")
