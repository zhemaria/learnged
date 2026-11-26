"""Level 2 · Lesson 4.1 · Ratios and unit rates — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import fr

B.NIVEL = 2
N = "4-1"
TEMA = ("Ratios, rates, and proportions", "Razones, proporciones y porcentajes")
TIT = ("Ratios and unit rates", "Razones y tasas unitarias")

def notaciones(a, b):
    def c(tit, x, lee):
        return f'<div style="flex:1;min-width:150px;background:#fff;border:2px solid #b2dfdb;border-radius:12px;padding:12px;text-align:center"><div style="font-size:.9rem;color:#455a64">{tit}</div><div style="font-size:1.7rem;font-weight:700;color:#0d47a1;margin:6px 0">{x}</div><div style="font-size:.9rem">{lee}</div></div>'
    lee = t(f"read “{a} to {b}”", f"se lee «{a} a {b}»")
    return ('<div style="display:flex;gap:12px;flex-wrap:wrap;margin:12px 0">'
            + c(t("With the word “to”", "Con la palabra «a»"), t(f"{a} to {b}", f"{a} a {b}"), lee)
            + c(t("With a colon", "Con dos puntos"), f"{a} : {b}", lee)
            + c(t("As a fraction", "Como fracción"), fr(a, b), lee) + "</div>")

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Topic 4. Until now, all of Level 2 has been about operating with numbers: integers, fractions, powers, roots, and PEMDAS. In Topic 4 the question changes. It is no longer “What does this operation give?” but “How do these two quantities compare?” This lesson opens the topic with the most basic idea of all: comparing two quantities.",
"Bienvenido al Tema 4. Hasta ahora todo el Nivel 2 se ha concentrado en operar con números: enteros, fracciones, potencias, raíces y PEMDAS. En el Tema 4 cambia la pregunta: ya no es «¿cuánto da esta operación?», sino «¿cómo se comparan estas dos cantidades?». Esta lección abre el tema con la idea más básica de todas: comparar dos cantidades.")}</p>
<p>{t("A <strong>ratio</strong> compares two quantities of the same kind. You read it “this to that” or “this for every that.” For example: in a classroom there are 12 students and 3 teachers. The ratio of students to teachers is 12 to 3, which simplifies to 4 to 1: there are 4 students for every teacher.",
"Una <strong>razón</strong> compara dos cantidades del mismo tipo. Se lee «esta a esa» o «esta por cada esa». Por ejemplo: en un aula hay 12 estudiantes y 3 maestros. La razón de estudiantes a maestros es 12 a 3, que se simplifica a 4 a 1: hay 4 estudiantes por cada maestro.")}</p>
<h3>{t("Three ways to write the same ratio", "Tres maneras de escribir la misma razón")}</h3>
{notaciones(4, 1)}
<p>{t("The fraction form is the most useful one for calculating: you simplify the ratio the same way you simplify a fraction, dividing both terms by their greatest common factor.", "La forma de fracción es la más útil para calcular: la razón se simplifica igual que una fracción, dividiendo los dos términos entre su máximo común divisor.")}</p>
{ejemplo(t("Example: simplify a ratio", "Ejemplo: simplificar una razón"),
  [("1", t("Write it.", "Se escribe."), t("A bakery has 15 loaves of wheat bread and 10 loaves of rye. The ratio of wheat to rye is 15 to 10, or " + fr(15, 10) + ".", "Una panadería tiene 15 panes de trigo y 10 panes de centeno. La razón de trigo a centeno es 15 a 10, o " + fr(15, 10) + ".")),
   ("2", t("Simplify.", "Simplifique."), t("The greatest common factor is 5: 15 ÷ 5 = 3 and 10 ÷ 5 = 2.", "El máximo común divisor es 5: 15 ÷ 5 = 3 y 10 ÷ 5 = 2.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>3 to 2</strong> (or 3 : 2, or 3/2). For every 3 loaves of wheat there are 2 of rye.", "<strong>3 a 2</strong> (o 3 : 2, o 3/2). Por cada 3 panes de trigo hay 2 de centeno."))])}
{caja("ojo", t("Order matters", "El orden importa"), t("<p>“Wheat to rye” is 3 to 2, but “rye to wheat” is 2 to 3. The quantity named first goes first in the ratio. Always.</p>", "<p>«Trigo a centeno» es 3 a 2, pero «centeno a trigo» es 2 a 3. La cantidad que se nombra primero va primero en la razón. Siempre.</p>"))}
{practica("p1", t("Practice 1 — Simplify", "Práctica 1 — Simplifique"), t("A parking lot has 18 cars and 24 spaces. What is the simplified ratio of cars to spaces?", "En un estacionamiento hay 18 carros y 24 espacios. ¿Cuál es la razón simplificada de carros a espacios?"),
          [("a", t("18 to 24", "18 a 24")), ("b", t("3 to 4", "3 a 4")), ("c", t("4 to 3", "4 a 3")), ("d", t("9 to 12", "9 a 12"))])}
{practica("p2", t("Practice 2 — Wins and losses", "Práctica 2 — Partidos ganados y perdidos"), t("A team won 8 games and lost 4. What is the ratio of games won to games lost?", "Un equipo ganó 8 partidos y perdió 4. ¿Cuál es la razón de partidos ganados a partidos perdidos?"),
          [("a", t("2 to 1", "2 a 1")), ("b", t("1 to 2", "1 a 2")), ("c", t("8 to 12", "8 a 12")), ("d", t("2 to 3", "2 a 3"))])}
{practica("p3", t("Practice 3 — Notation", "Práctica 3 — Notación"), t("The notation 5 : 3 is the same as:", "La notación 5 : 3 es lo mismo que:"),
          [("a", "5 + 3"), ("b", t("5 minus 3", "5 menos 3")), ("c", t("3 to 5", "3 a 5")), ("d", t("5 to 3, or 5/3", "5 a 3, o 5/3"))])}
{enlace(n, t("ratio", "razon"), t("what a ratio is", "qué es una razón"), t("Make equal groups, write ratios in their three forms, and simplify them.", "Forme grupos iguales, escriba razones en sus tres formas y simplifíquelas."))}'''

    s2 = f'''<p>{t("When the two quantities have <strong>different units</strong>, the ratio has a special name: a <strong>rate</strong>. Rates are everywhere: price per pound, miles per hour, words per minute, dollars per gallon.", "Cuando las dos cantidades tienen <strong>unidades distintas</strong>, la razón recibe un nombre especial: <strong>tasa</strong>. Las tasas están en todas partes: precio por libra, millas por hora, palabras por minuto, dólares por galón.")}</p>
{tabla(t("Ratio and rate", "Razón y tasa"), t("A ratio compares the same kind of quantity; a rate compares different units", "Una razón compara cantidades del mismo tipo; una tasa compara unidades distintas"),
       ["", t("Example", "Ejemplo"), t("Units", "Unidades")],
       [[t("<strong>Ratio</strong>", "<strong>Razón</strong>"), t("12 students to 3 teachers", "12 estudiantes a 3 maestros"), t("the same (people)", "las mismas (personas)")],
        [t("<strong>Rate</strong>", "<strong>Tasa</strong>"), t("240 miles in 4 hours", "240 millas en 4 horas"), t("different (miles and hours)", "distintas (millas y horas)")]])}
<p>{t("A <strong>unit rate</strong> is a rate whose second term is 1. To find it, <strong>divide the first term by the second</strong>. It is the most useful form, because it lets you compare options at a glance.", "La <strong>tasa unitaria</strong> es la tasa cuyo segundo término vale 1. Para hallarla, <strong>se divide el primer término entre el segundo</strong>. Es la forma más útil, porque permite comparar opciones de un vistazo.")}</p>
{ejemplo(t("Example: a unit rate", "Ejemplo: una tasa unitaria"),
  [("1", t("The rate.", "La tasa."), t("A car travels 240 miles in 4 hours.", "Un auto recorre 240 millas en 4 horas.")),
   ("2", t("Divide.", "Divida."), t("First term by second term: 240 ÷ 4 = 60.", "El primer término entre el segundo: 240 ÷ 4 = 60.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>60 miles per hour</strong>. “Per hour” tells you the second term is now 1.", "<strong>60 millas por hora</strong>. «Por hora» indica que el segundo término ya es 1."))])}
{caja("tip", t("Word clue", "Pista de lenguaje"), t("<p>The words <strong>per</strong>, <strong>each</strong>, and <strong>for one</strong> point to a unit rate. “$3 per pound” means 3 dollars for each pound; “60 miles per hour” means 60 miles in one hour.</p>", "<p>Las palabras <strong>por</strong>, <strong>cada</strong> y <strong>por uno</strong> señalan una tasa unitaria. «$3 por libra» quiere decir 3 dólares por cada libra; «60 millas por hora» quiere decir 60 millas en una hora.</p>"))}
{calc(t("Unit rates on the calculator", "Tasas unitarias en la calculadora"), t(f"<p>For 240 miles in 4 hours, type {T('240')} {T('÷')} {T('4')} {T('enter')}. The screen shows 60. Always divide in the order of the words: first term ÷ second term.</p>", f"<p>Para 240 millas en 4 horas, escriba {T('240')} {T('÷')} {T('4')} {T('enter')}. La pantalla muestra 60. Divida siempre en el orden de las palabras: primer término ÷ segundo término.</p>"))}
{practica("p4", t("Practice 4 — Miles per hour", "Práctica 4 — Millas por hora"), t("A bus travels 180 miles in 3 hours. What is its unit rate?", "Un autobús recorre 180 millas en 3 horas. ¿Cuál es su tasa unitaria?"),
          [("a", t("540 miles per hour", "540 millas por hora")), ("b", t("60 miles per hour", "60 millas por hora")), ("c", t("1/60 of a mile per hour", "1/60 de milla por hora")), ("d", t("90 miles per hour", "90 millas por hora"))])}
{practica("p5", t("Practice 5 — Price per pound", "Práctica 5 — Precio por libra"), t("4 pounds of chicken cost $12. What is the price per pound?", "4 libras de pollo cuestan $12. ¿Cuál es el precio por libra?"),
          [("a", "$48"), ("b", "$0.33"), ("c", "$3"), ("d", "$8")])}
{enlace(n, t("rate", "tasa"), t("the unit rate", "la tasa unitaria"), t("Divide the first term by the second and get the rate for one unit.", "Divida el primer término entre el segundo y obtenga la tasa por unidad."))}'''

    s3 = f'''<p>{t("The unit rate is the most practical tool for choosing between two sizes of the same product. Find the price per unit of each one, and the comparison becomes a matter of reading two numbers.", "La tasa unitaria es la herramienta más práctica para elegir entre dos tamaños del mismo producto. Se calcula el precio por unidad de cada uno, y la comparación se reduce a leer dos números.")}</p>
{ejemplo(t("Example: which bag of rice is the better buy?", "Ejemplo: ¿qué saco de arroz conviene?") + '<span style="display:block;font-weight:400;margin-top:6px">' + t("A 5-pound bag of rice costs $7.50, and a 10-pound bag costs $13.00.", "Un saco de 5 libras de arroz cuesta $7.50 y uno de 10 libras cuesta $13.00.") + '</span>',
  [   ("1", t("Bag A.", "Saco A."), t("$7.50 ÷ 5 pounds = $1.50 per pound.", "$7.50 ÷ 5 libras = $1.50 por libra.")),
   ("2", t("Bag B.", "Saco B."), t("$13.00 ÷ 10 pounds = $1.30 per pound.", "$13.00 ÷ 10 libras = $1.30 por libra.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Bag B</strong> is cheaper: each pound costs 20 cents less.", "<strong>El saco B</strong> es más barato: cada libra cuesta 20 centavos menos."))])}
{tabla(t("Comparing the two bags", "Comparación de los dos sacos"), t("Price per pound of each bag of rice", "Precio por libra de cada saco de arroz"),
       [t("Bag", "Saco"), t("Total price", "Precio total"), t("Amount", "Cantidad"), t("Price per pound", "Precio por libra")],
       [["A", "$7.50", "5 lb", "$1.50"], ["B", "$13.00", "10 lb", "<strong>$1.30</strong>"]])}
{caja("ojo", t("The lowest total price can fool you", "El precio total más bajo puede engañar"), t("<p>The 5-pound bag costs less in total, but more per pound. Only the unit rate lets you compare fairly.</p>", "<p>El saco de 5 libras cuesta menos en total, pero más por libra. Solo la tasa unitaria permite comparar de forma justa.</p>"))}
{practica("p6", t("Practice 6 — Apples", "Práctica 6 — Manzanas"), t("Option A: $6 for 2 pounds of apples. Option B: $9 for 4 pounds. Which one is cheaper per pound?", "Opción A: $6 por 2 libras de manzanas. Opción B: $9 por 4 libras. ¿Cuál es más barata por libra?"),
          [("a", t("Option A ($3 per pound)", "La opción A ($3 por libra)")), ("b", t("They cost the same", "Las dos cuestan lo mismo")), ("c", t("Option B ($2.25 per pound)", "La opción B ($2.25 por libra)"))])}
{enlace(n, t("compare", "comparar"), t("comparing options", "comparar opciones"), t("Find the price per unit of each option and see which one is the better buy.", "Calcule el precio por unidad de cada opción y descubra cuál conviene."))}'''

    s4 = f'''<p>{t("Ratios and unit rates show up in shopping, travel, recipes, sports, and work. Once you know the unit rate, you can multiply to find a total, or divide to find how many.", "Las razones y las tasas unitarias aparecen en las compras, los viajes, las recetas, los deportes y el trabajo. Conocida la tasa unitaria, se multiplica para hallar un total o se divide para saber cuántos.")}</p>
{ejemplo(t("Example: mixing paint", "Ejemplo: mezclar pintura") + '<span style="display:block;font-weight:400;margin-top:6px">' + t("A paint mix uses 2 parts blue for every 5 parts white. If you use 8 parts blue, how much white do you need to keep the same ratio?", "Una mezcla de pintura lleva 2 partes de azul por cada 5 de blanca. Si se usan 8 partes de azul, ¿cuánta blanca hace falta para mantener la misma razón?") + '</span>',
  [   ("1", t("The ratio.", "La razón."), t("Blue to white is 2 to 5, and it stays the same.", "Azul a blanca es 2 a 5, y se mantiene.")),
   ("2", t("Multiply both terms.", "Multiplique los dos términos."), t("Blue went from 2 to 8: it was multiplied by 4. White too: 5 × 4 = 20.", "El azul pasó de 2 a 8: se multiplicó por 4. La blanca también: 5 × 4 = 20.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>20 parts</strong> of white paint.", "<strong>20 partes</strong> de pintura blanca."))])}
{ejemplo(t("Example: miles per gallon", "Ejemplo: millas por galón") + '<span style="display:block;font-weight:400;margin-top:6px">' + t("Car A goes 320 miles on 16 gallons. Car B goes 270 miles on 9 gallons. Which car gets more miles per gallon?", "El auto A recorre 320 millas con 16 galones. El auto B recorre 270 millas con 9 galones. ¿Cuál rinde más millas por galón?") + '</span>',
  [   ("1", t("Car A.", "Auto A."), "320 ÷ 16 = 20."),
   ("2", t("Car B.", "Auto B."), "270 ÷ 9 = 30."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Car B</strong>, with 30 miles per gallon.", "<strong>El auto B</strong>, con 30 millas por galón."))])}
<div class="caja-formula" style="text-align:center;font-size:1.2rem;font-weight:700;color:#0d47a1;margin:12px 0">{t("distance = speed × time", "distancia = rapidez × tiempo")}</div>
{practica("p7", t("Practice 7 — A pack of juice", "Práctica 7 — Un paquete de jugos"), t("A pack of 6 juices costs $4.80. How much does each juice cost?", "Un paquete de 6 jugos cuesta $4.80. ¿Cuánto cuesta cada jugo?"),
          [("a", "$0.80"), ("b", "$0.60"), ("c", "$1.20"), ("d", "$28.80")])}
{practica("p8", t("Practice 8 — A recipe", "Práctica 8 — Una receta"), t("A recipe uses 3 cups of flour for every 2 eggs. If you use 9 cups of flour, how many eggs do you need?", "Una receta lleva 3 tazas de harina por cada 2 huevos. Si se usan 9 tazas de harina, ¿cuántos huevos hacen falta?"),
          [("a", t("5 eggs", "5 huevos")), ("b", t("6 eggs", "6 huevos")), ("c", t("4 eggs", "4 huevos")), ("d", t("8 eggs", "8 huevos"))])}
{enlace(n, t("speed", "rapidez"), t("speed and other rates in context", "rapidez y otras tasas en contexto"), t("Use the unit rate to find distances, times, pay, and gas use.", "Use la tasa unitaria para calcular distancias, tiempos, salarios y consumo de gasolina."))}'''

    secciones = [("s-" + t("ratio", "razon"), t("What a ratio is", "Qué es una razón"), s1),
                 ("s-" + t("rate", "tasa"), t("A rate: a ratio with different units", "La tasa: una razón con unidades distintas"), s2),
                 ("s-" + t("compare", "comparar"), t("Comparing options with unit rates", "Comparar opciones con tasas unitarias"), s3),
                 ("s-" + t("applications", "aplicaciones"), t("Real-life applications", "Aplicaciones a contextos reales"), s4)]

    lesson = {"next": t("Lesson 4.2", "Lección 4.2"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("That is the right ratio, but it is not simplified yet.", "Es la razón correcta, pero falta simplificarla."), "c": t("The order is reversed: cars are named first.", "El orden está invertido: los carros se nombran primero."), "d": t("You can still divide by 3.", "Todavía se puede dividir entre 3.")},
             "right": t("18 to 24 ÷ 6 = 3 to 4.", "18 a 24 ÷ 6 = 3 a 4."), "solution": t("The greatest common factor of 18 and 24 is 6: 18 ÷ 6 = 3 and 24 ÷ 6 = 4. The ratio is 3 to 4.", "El máximo común divisor de 18 y 24 es 6: 18 ÷ 6 = 3 y 24 ÷ 6 = 4. La razón es 3 a 4.")},
      "p2": {"ok": "a", "hints": {"b": t("The order is reversed: games won come first.", "El orden está invertido: primero los partidos ganados."), "c": t("12 is the total number of games. Compare won with lost.", "12 es el total de partidos. Compare ganados con perdidos."), "d": t("Check: 8 ÷ 4 = 2 and 4 ÷ 4 = 1.", "Revise: 8 ÷ 4 = 2 y 4 ÷ 4 = 1.")},
             "right": t("8 to 4 = 2 to 1.", "8 a 4 = 2 a 1."), "solution": t("8 to 4, divided by 4, is 2 to 1: 2 games won for every game lost.", "8 a 4, dividido entre 4, es 2 a 1: 2 partidos ganados por cada perdido.")},
      "p3": {"ok": "d", "hints": {"a": t("The colon is not an addition. It is read “to.”", "Los dos puntos no son una suma. Se leen «a»."), "b": t("The colon is not a subtraction. It is read “to.”", "Los dos puntos no son una resta. Se leen «a»."), "c": t("The order is reversed.", "El orden está invertido.")},
             "right": t("5 : 3 is read “5 to 3” and can be written 5/3.", "5 : 3 se lee «5 a 3» y se puede escribir 5/3."), "solution": t("5 : 3, 5 to 3, and 5/3 are the same ratio.", "5 : 3, 5 a 3 y 5/3 son la misma razón.")},
      "p4": {"ok": "b", "hints": {"a": t("You multiplied. For a unit rate, divide.", "Multiplicó. Para la tasa unitaria se divide."), "c": t("You divided in the wrong order: miles ÷ hours.", "Dividió al revés: millas ÷ horas."), "d": t("Check the division: 180 ÷ 3.", "Revise la división: 180 ÷ 3.")},
             "right": t("180 ÷ 3 = 60 miles per hour.", "180 ÷ 3 = 60 millas por hora."), "solution": t("First term by second term: 180 miles ÷ 3 hours = 60 miles per hour.", "El primer término entre el segundo: 180 millas ÷ 3 horas = 60 millas por hora.")},
      "p5": {"ok": "c", "hints": {"a": t("You multiplied 12 × 4. Divide.", "Multiplicó 12 × 4. Se divide."), "b": t("You divided pounds by dollars. It is dollars ÷ pounds.", "Dividió libras entre dólares. Es dólares ÷ libras."), "d": t("Check: 12 ÷ 4.", "Revise: 12 ÷ 4.")},
             "right": t("$12 ÷ 4 = $3 per pound.", "$12 ÷ 4 = $3 por libra."), "solution": t("$12 ÷ 4 pounds = $3 per pound.", "$12 ÷ 4 libras = $3 por libra.")},
      "p6": {"ok": "c", "hints": {"a": t("$6 ÷ 2 = $3 per pound, and $9 ÷ 4 = $2.25. Which is less?", "$6 ÷ 2 = $3 por libra, y $9 ÷ 4 = $2.25. ¿Cuál es menor?"), "b": t("Find the price per pound of each one: they are not equal.", "Calcule el precio por libra de cada una: no son iguales.")},
             "right": t("A: $3 per pound; B: $2.25 per pound. B is cheaper.", "A: $3 por libra; B: $2.25 por libra. B es más barata."), "solution": t("A: $6 ÷ 2 = $3 per pound. B: $9 ÷ 4 = $2.25 per pound. B is cheaper, even though its total price is higher.", "A: $6 ÷ 2 = $3 por libra. B: $9 ÷ 4 = $2.25 por libra. B es más barata, aunque su precio total sea mayor.")},
      "p7": {"ok": "a", "hints": {"b": t("Check the division: 4.80 ÷ 6.", "Revise la división: 4.80 ÷ 6."), "c": t("Check: 6 × $1.20 would be $7.20.", "Revise: 6 × $1.20 serían $7.20."), "d": t("You multiplied. Divide the price by 6.", "Multiplicó. Divida el precio entre 6.")},
             "right": t("$4.80 ÷ 6 = $0.80.", "$4.80 ÷ 6 = $0.80."), "solution": t("$4.80 ÷ 6 juices = $0.80 per juice.", "$4.80 ÷ 6 jugos = $0.80 por jugo.")},
      "p8": {"ok": "b", "hints": {"a": t("You added 3 to the eggs. In a ratio, both terms are multiplied by the same number.", "Le sumó 3 a los huevos. En una razón, los dos términos se multiplican por el mismo número."), "c": t("Flour went from 3 to 9: × 3. Eggs too: 2 × 3.", "La harina pasó de 3 a 9: × 3. Los huevos también: 2 × 3."), "d": t("Check: 9 ÷ 3 = 3, and 2 × 3 = 6.", "Revise: 9 ÷ 3 = 3, y 2 × 3 = 6.")},
             "right": t("9 ÷ 3 = 3; 2 × 3 = 6 eggs.", "9 ÷ 3 = 3; 2 × 3 = 6 huevos."), "solution": t("Flour was multiplied by 3 (3 → 9), so eggs are too: 2 × 3 = 6 eggs.", "La harina se multiplicó por 3 (3 → 9), así que los huevos también: 2 × 3 = 6 huevos.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The order is reversed: wheat comes first.", "El orden está invertido: primero el trigo."), "b": t("Simplify it: divide both terms by 5.", "Simplifíquela: divida los dos términos entre 5."), "d": t("Check: 10 ÷ 5 = 2, not 1.", "Revise: 10 ÷ 5 = 2, no 1.")}, "solution": t("15 to 10, divided by 5, is 3 to 2.", "15 a 10, dividido entre 5, es 3 a 2.")},
      "B": {"ok": "b", "hints": {"a": t("That is wheat to rye. The question asks for rye to wheat.", "Esa es trigo a centeno. Se pide centeno a trigo."), "c": t("25 is the total. Compare rye with wheat.", "25 es el total. Compare centeno con trigo."), "d": t("Rye to total is not what is asked.", "No se pide centeno al total.")}, "solution": t("Rye to wheat: 10 to 15 = 2 to 3.", "Centeno a trigo: 10 a 15 = 2 a 3.")},
      "C": {"ok": "b", "hints": {"a": t("Students and teachers are both people: same units. That is a ratio.", "Estudiantes y maestros son personas: mismas unidades. Es una razón."), "c": t("Cups and cups: same units.", "Tazas y tazas: mismas unidades."), "d": t("Games and games: same units.", "Partidos y partidos: mismas unidades.")}, "solution": t("Miles and hours are different units, so it is a rate.", "Millas y horas son unidades distintas: es una tasa.")},
      "D": {"ok": "a", "hints": {"b": t("You multiplied. Divide miles by gallons.", "Multiplicó. Divida millas entre galones."), "c": t("You divided gallons by miles.", "Dividió galones entre millas."), "d": t("You subtracted. Divide.", "Restó. Se divide.")}, "solution": t("300 ÷ 12 = 25 miles per gallon.", "300 ÷ 12 = 25 millas por galón.")},
      "E": {"ok": "b", "hints": {"a": t("$3.75 ÷ 5 = $0.75 per pound; $13 ÷ 20 = $0.65 per pound.", "$3.75 ÷ 5 = $0.75 por libra; $13 ÷ 20 = $0.65 por libra."), "c": t("Find each price per pound: they are different.", "Calcule cada precio por libra: son distintos."), "d": t("You can tell: divide each price by its pounds.", "Sí se puede saber: divida cada precio entre sus libras.")}, "solution": t("5 lb: $0.75 per pound. 20 lb: $0.65 per pound. The 20-pound bag is the better buy.", "5 lb: $0.75 por libra. 20 lb: $0.65 por libra. Conviene el saco de 20 libras.")},
      "F": {"ok": "d", "hints": {"a": t("You multiplied. Divide the pay by the hours.", "Multiplicó. Divida el pago entre las horas."), "b": t("You subtracted. Divide.", "Restó. Se divide."), "c": t("Check: 171 ÷ 9.", "Revise: 171 ÷ 9.")}, "solution": t("$171 ÷ 9 hours = $19 per hour.", "$171 ÷ 9 horas = $19 por hora.")},
      "G": {"ok": "c", "hints": {"a": t("You added 6 to the white paint. Multiply both terms by the same number.", "Le sumó 6 a la blanca. Multiplique los dos términos por el mismo número."), "b": t("Blue was multiplied by 4, so white is 5 × 4.", "El azul se multiplicó por 4, así que la blanca es 5 × 4."), "d": t("Check: 5 × 4 = 20, not 40.", "Revise: 5 × 4 = 20, no 40.")}, "solution": t("2 → 8 is × 4; 5 × 4 = 20 parts of white.", "2 → 8 es × 4; 5 × 4 = 20 partes de blanca.")},
      "H": {"ok": "d", "hints": {"a": t("You divided. Distance = speed × time.", "Dividió. distancia = rapidez × tiempo."), "b": t("You added. Multiply.", "Sumó. Se multiplica."), "c": t("Do not forget the half hour: 60 × 4.5.", "No olvide la media hora: 60 × 4.5.")}, "solution": t("60 × 4.5 = 270 miles.", "60 × 4.5 = 270 millas.")}
     }}

    quiz = [
     ("A", t("A bakery has 15 loaves of wheat bread and 10 of rye. What is the simplified ratio of wheat to rye?", "Una panadería tiene 15 panes de trigo y 10 de centeno. ¿Cuál es la razón simplificada de trigo a centeno?"), [("a", t("2 to 3", "2 a 3")), ("b", t("15 to 10", "15 a 10")), ("c", t("3 to 2", "3 a 2")), ("d", t("5 to 1", "5 a 1"))]),
     ("B", t("In the same bakery, what is the ratio of rye to wheat?", "En la misma panadería, ¿cuál es la razón de centeno a trigo?"), [("a", "3 : 2"), ("b", "2 : 3"), ("c", "10 : 25"), ("d", "2 : 5")]),
     ("C", t("Which one is a rate?", "¿Cuál de estas es una tasa?"), [("a", t("12 students to 3 teachers", "12 estudiantes a 3 maestros")), ("b", t("240 miles in 4 hours", "240 millas en 4 horas")), ("c", t("3 cups of flour to 2 cups of sugar", "3 tazas de harina a 2 tazas de azúcar")), ("d", t("5 wins to 3 losses", "5 victorias a 3 derrotas"))]),
     ("D", t("A car goes 300 miles on 12 gallons. How many miles per gallon is that?", "Un auto recorre 300 millas con 12 galones. ¿Cuántas millas por galón son?"), [("a", "25"), ("b", "3,600"), ("c", "0.04"), ("d", "288")]),
     ("E", t("Which bag of rice is the better buy?", "¿Qué saco de arroz conviene más?"), [("a", t("5 lb for $3.75", "5 lb por $3.75")), ("b", t("20 lb for $13.00", "20 lb por $13.00")), ("c", t("They cost the same per pound", "Cuestan lo mismo por libra")), ("d", t("You cannot tell", "No se puede saber"))]),
     ("F", t("A person earns $171 for 9 hours of work. How much is that per hour?", "Una persona gana $171 por 9 horas de trabajo. ¿Cuánto es por hora?"), [("a", "$1,539"), ("b", "$162"), ("c", "$21"), ("d", "$19")]),
     ("G", t("A paint mix uses 2 parts blue for every 5 parts white. With 8 parts blue, how many parts of white do you need?", "Una pintura lleva 2 partes de azul por cada 5 de blanca. Con 8 partes de azul, ¿cuántas de blanca hacen falta?"), [("a", "11"), ("b", "16"), ("c", "20"), ("d", "40")]),
     ("H", t("A truck travels at 60 miles per hour for 4.5 hours. How far does it go?", "Un camión viaja a 60 millas por hora durante 4.5 horas. ¿Qué distancia recorre?"), [("a", t("13.3 miles", "13.3 millas")), ("b", t("64.5 miles", "64.5 millas")), ("c", t("240 miles", "240 millas")), ("d", t("270 miles", "270 millas"))])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Compare two quantities: ratios in their three forms, unit rates, and the better buy.", "Comparar dos cantidades: las razones en sus tres formas, la tasa unitaria y la mejor compra."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Tell</strong> a ratio from a rate in everyday situations.", "<strong>Distinguir</strong> una razón de una tasa en situaciones cotidianas."),
         t("<strong>Write</strong> a ratio in its three equivalent forms.", "<strong>Escribir</strong> una razón en sus tres notaciones equivalentes."),
         t("<strong>Simplify</strong> a ratio.", "<strong>Simplificar</strong> una razón."),
         t("<strong>Find</strong> a unit rate by dividing the first term by the second.", "<strong>Calcular</strong> una tasa unitaria dividiendo el primer término entre el segundo."),
         t("<strong>Compare</strong> two real options (prices, speeds) with unit rates.", "<strong>Comparar</strong> dos opciones reales (precios, velocidades) con tasas unitarias.")],
        secciones,
        (t("Write and simplify five ratios in their three forms. Find five unit rates in real situations (shopping, travel, reading). Compare four pairs of options by their unit rate. Solve two mixing problems that keep a ratio the same.",
           "Escriba y simplifique cinco razones en sus tres notaciones. Calcule cinco tasas unitarias en situaciones reales (compras, viajes, lectura). Compare cuatro pares de opciones por su tasa unitaria. Resuelva dos problemas de mezcla que mantengan una razón constante."),
         t("Next time you shop, choose one product sold in two sizes. Find the price per unit of each one (it is often printed on the shelf label as “unit price”) and decide which one is the better buy.",
           "La próxima vez que vaya de compras, elija un producto que se venda en dos tamaños. Calcule el precio por unidad de cada uno (muchas veces viene en la etiqueta del estante como «unit price») y decida cuál conviene.")),
        quiz,
        t("Self-check checklist for ratios and unit rates", "Lista de autoevaluación de razones y tasas unitarias"),
        t("Self-check checklist: skills for ratios and unit rates", "Lista de autoevaluación: destrezas de razones y tasas unitarias"),
        [(t("Write and simplify ratios", "Escribir y simplificar razones"), t("I write them in the three forms, in the right order, and simplify them.", "Las escribo en las tres formas, en el orden correcto, y las simplifico."), t("I write them, but I forget to simplify.", "Las escribo, pero olvido simplificar."), t("I mix up the order of the terms.", "Confundo el orden de los términos.")),
         (t("Unit rates", "Tasas unitarias"), t("I divide in the right order and give the answer with its units.", "Divido en el orden correcto y doy la respuesta con sus unidades."), t("I find them in simple cases.", "Las calculo en casos sencillos."), t("I mix up a ratio with a unit rate.", "Confundo la razón con la tasa unitaria.")),
         (t("Compare options", "Comparar opciones"), t("I compare by unit price and explain why the total price can fool you.", "Comparo por precio unitario y explico por qué el precio total puede engañar."), t("I compare with help.", "Comparo con ayuda."), t("I choose by the total price.", "Elijo por el precio total."))],
        t("<p>You opened Topic 4 with the most basic way to compare: the <strong>ratio</strong>, its three forms, and how to simplify it. You also learned the <strong>unit rate</strong>, which turns comparing two options into a single division.</p>\n<p>In <strong>Lesson 4.2 · Direct proportions: the rule of three</strong> you will take the next step: a proportion is an equation between two ratios. You will use cross products to find a missing term.</p>",
          "<p>Abrió el Tema 4 con la forma más básica de comparar: la <strong>razón</strong>, sus tres notaciones y su simplificación. También aprendió la <strong>tasa unitaria</strong>, que convierte la comparación de dos opciones en una sola división.</p>\n<p>En la <strong>Lección 4.2 · Proporciones directas: regla de tres y resolver proporciones</strong> dará el siguiente paso: una proporción es una igualdad entre dos razones. Usará el producto cruzado para hallar un término desconocido.</p>"),
        ("4-2", ("", t("Lesson 4.2 · Direct proportions: the rule of three", "Lección 4.2 · Proporciones directas: regla de tres y resolver proporciones"))),
        [(t("ratio", "razón"), t("A comparison of two quantities of the same kind, like 3 to 2.", "Comparación de dos cantidades del mismo tipo, como 3 a 2.")),
         (t("rate", "tasa"), t("A ratio of two quantities with different units, like 240 miles in 4 hours.", "Razón entre dos cantidades con unidades distintas, como 240 millas en 4 horas.")),
         (t("unit rate", "tasa unitaria"), t("A rate whose second term is 1, like 60 miles per hour.", "Tasa cuyo segundo término es 1, como 60 millas por hora.")),
         (t("unit price", "precio unitario"), t("The price of one unit (one pound, one ounce, one item).", "El precio de una unidad (una libra, una onza, un artículo)."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "est": ["student", "students"], "mae": ["teacher", "teachers"],
  "razonDe": "Ratio of students to teachers: <strong>{a} to {b}</strong> = {a} : {b} = {f}.",
  "grupos": "They make {g} equal groups (divide by {g}, the greatest common factor). Simplified: <strong>{p} to {q}</strong>.",
  "yaSimple": "{a} and {b} have no common factor: the ratio is already in simplest form.",
  "porCada": "There {ser} {p} {e} for every {q2} {m}.", "hay": ["is", "are"],
  "aria": "{g} equal groups, each with {p} {e} and {q} {m}.",
  "ctx": [["cars", "spaces", "A parking lot has {a} cars and {b} spaces."], ["games won", "games lost", "A team won {a} games and lost {b}."], ["loaves of wheat bread", "loaves of rye", "A bakery has {a} loaves of wheat bread and {b} loaves of rye."], ["women", "men", "A class has {a} women and {b} men."], ["cups of water", "cups of rice", "A recipe uses {a} cups of water and {b} cups of rice."]],
  "simplDe": " What is the simplified ratio of {x} to {y}?", "a": " to ",
  "inv": "The order is reversed: {x} are named first.", "sin": "That ratio is right, but it is not simplified yet (divide by {k}).", "tot": "That one compares with the total, not with the {y}.",
  "bien1": "{a} to {b} divided by {k}: {r}.", "mal1": "{a} to {b} ÷ {k} = {r}, in the order the quantities are named.",
  "notacion": "The notation {p} : {q} is the same as:", "notOk": "{p} to {q}, or {p}/{q}", "menos": "{p} minus {q}",
  "bienNot": "The colon is read “to”: {p} to {q}, which can also be written {p}/{q}.",
  "pistaNot": "The colon is not an operation. It is read “to.”",
  "situ": [["Miles", "Hours", "miles per hour"], ["Dollars", "Pounds", "dollars per pound"], ["Words", "Minutes", "words per minute"], ["Dollars earned", "Hours worked", "dollars per hour"]],
  "dosPos": "Type two positive numbers.", "divide": "Divide the first term by the second: {a} ÷ {b} = {r}.",
  "ts": ["A car travels {t} miles in {q} hours. How many miles does it travel per hour?", "A {q}-pound pack of chicken costs {t}. What is the price per pound, in dollars?", "A person types {t} words in {q} minutes. How many words per minute is that?", "{q} hours of work pay {t}. How much is that per hour, in dollars?", "A car travels {t} miles on {q} gallons of gas. How many miles per gallon is that?"],
  "tsU": ["miles per hour", "dollars per pound", "words per minute", "dollars per hour", "miles per gallon"],
  "alReves": "You divided in the wrong order: the first term ({a}) goes over the second ({b}).", "noMult": "For a unit rate, divide; do not multiply.",
  "prod": [["rice", "pounds", "pound"], ["laundry detergent", "ounces", "ounce"], ["cereal", "ounces", "ounce"], ["juice", "ounces", "ounce"], ["eggs", "eggs", "egg"]],
  "opcion": "Option {l}", "opcionDe": "Option {l}: {n} {u} for {p}", "cual": "Which package of {x} is the better buy (the lowest price per {u})?",
  "linea": "Option {l}: {p} ÷ {n} ≈ ${r} per {u}", "conviene": ". Option {l} is the better buy.", "masBarata": ". The lowest price per {u} is option {l}.",
  "engana": "It has the lowest total price, but not the lowest price per {u}.", "pistaComp": "Divide each price by its amount and compare.",
  "rpAria": "A trip of {d} miles in {t} hours at {v} miles per hour.", "millas": "640 miles",
  "cadaHora": "Each hour the car moves {v} miles (each mark is one hour).", "dist": "distance = {v} × {t} = {d} miles",
  "rp1": "A bus travels at {v} miles per hour for {h} hours. How many miles does it go?", "rp1s": "{v} × {h} = {r} miles.", "rp1p": "Here you know the speed and want the distance: multiply.",
  "rp2": "A truck must travel {d} miles at {v} miles per hour. How many hours does it take?", "rp2s": "{d} ÷ {v} = {h} hours.", "rp2p": "For the time, divide the distance by the speed.",
  "rp3": "A person earns {s} per hour and works {h} hours this week. How much does the person earn in all, in dollars?", "rp3s": "{s} × {h} = {r}.",
  "rp4": "A car gets {m} miles per gallon. How many gallons does it need for a {d}-mile trip?", "rp4s": "{d} ÷ {m} = {g} gallons.", "rp4p": "Divide the distance by the miles per gallon.",
  "rp5": "A paint mix uses {a} parts blue for every {b} parts white. If you use {ak} parts blue, how many parts white do you need to keep the ratio?", "rp5s": "Blue was multiplied by {k} ({a} × {k} = {ak}), so white is too: {b} × {k} = {r}.", "rp5p": "In a ratio you do not add the same amount to both terms: multiply them by the same number.",
  "rp6": "A printer prints {p} pages per minute. How many pages does it print in {m} minutes?", "rp6s": "{p} × {m} = {r} pages."
 },
 "es": {
  "est": ["estudiante", "estudiantes"], "mae": ["maestro", "maestros"],
  "razonDe": "Razón de estudiantes a maestros: <strong>{a} a {b}</strong> = {a} : {b} = {f}.",
  "grupos": "Se forman {g} grupos iguales (se divide entre {g}, el máximo común divisor). Simplificada: <strong>{p} a {q}</strong>.",
  "yaSimple": "{a} y {b} no tienen divisores comunes: la razón ya está simplificada.",
  "porCada": "Hay {p} {e} por cada {q2} {m}.", "hay": ["", ""],
  "aria": "{g} grupos iguales, cada uno con {p} {e} y {q} {m}.",
  "ctx": [["carros", "espacios", "En un estacionamiento hay {a} carros y {b} espacios."], ["partidos ganados", "partidos perdidos", "Un equipo ganó {a} partidos y perdió {b}."], ["panes de trigo", "panes de centeno", "En una panadería hay {a} panes de trigo y {b} de centeno."], ["mujeres", "hombres", "En una clase hay {a} mujeres y {b} hombres."], ["tazas de agua", "tazas de arroz", "Una receta lleva {a} tazas de agua y {b} de arroz."]],
  "simplDe": " ¿Cuál es la razón simplificada de {x} a {y}?", "a": " a ",
  "inv": "El orden está invertido: se nombran primero los {x}.", "sin": "Es la razón correcta, pero falta simplificarla (dividir entre {k}).", "tot": "Esa compara con el total, no con los {y}.",
  "bien1": "{a} a {b} dividido entre {k}: {r}.", "mal1": "{a} a {b} ÷ {k} = {r}, en el orden en que se nombran las cantidades.",
  "notacion": "La notación {p} : {q} es lo mismo que:", "notOk": "{p} a {q}, o {p}/{q}", "menos": "{p} menos {q}",
  "bienNot": "Los dos puntos se leen «a»: {p} a {q}, que también se escribe {p}/{q}.",
  "pistaNot": "Los dos puntos no son una operación. Se leen «a».",
  "situ": [["Millas", "Horas", "millas por hora"], ["Dólares", "Libras", "dólares por libra"], ["Palabras", "Minutos", "palabras por minuto"], ["Dólares ganados", "Horas trabajadas", "dólares por hora"]],
  "dosPos": "Escriba dos números positivos.", "divide": "Se divide el primer término entre el segundo: {a} ÷ {b} = {r}.",
  "ts": ["Un auto recorre {t} millas en {q} horas. ¿Cuántas millas recorre por hora?", "Un paquete de {q} libras de pollo cuesta {t}. ¿Cuánto cuesta cada libra, en dólares?", "Una persona escribe {t} palabras en {q} minutos. ¿Cuántas palabras escribe por minuto?", "Por {q} horas de trabajo se cobran {t}. ¿Cuánto se gana por hora, en dólares?", "Un auto recorre {t} millas con {q} galones de gasolina. ¿Cuántas millas recorre por galón?"],
  "tsU": ["millas por hora", "dólares por libra", "palabras por minuto", "dólares por hora", "millas por galón"],
  "alReves": "Se dividió al revés: el primer término ({a}) va entre el segundo ({b}).", "noMult": "Para la tasa unitaria se divide, no se multiplica.",
  "prod": [["arroz", "libras", "libra"], ["detergente", "onzas", "onza"], ["cereal", "onzas", "onza"], ["jugo", "onzas", "onza"], ["huevos", "huevos", "huevo"]],
  "opcion": "Opción {l}", "opcionDe": "Opción {l}: {n} {u} por {p}", "cual": "¿Qué paquete de {x} conviene más (el precio más bajo por {u})?",
  "linea": "Opción {l}: {p} ÷ {n} ≈ ${r} por {u}", "conviene": ". Conviene la opción {l}.", "masBarata": ". La más barata por {u} es la opción {l}.",
  "engana": "Es la de menor precio total, pero no la más barata por {u}.", "pistaComp": "Divida cada precio entre su cantidad y compare.",
  "rpAria": "Un recorrido de {d} millas en {t} horas a {v} millas por hora.", "millas": "640 millas",
  "cadaHora": "Cada hora el auto avanza {v} millas (cada marca es una hora).", "dist": "distancia = {v} × {t} = {d} millas",
  "rp1": "Un autobús viaja a {v} millas por hora durante {h} horas. ¿Cuántas millas recorre?", "rp1s": "{v} × {h} = {r} millas.", "rp1p": "Aquí se conoce la rapidez y se busca la distancia: se multiplica.",
  "rp2": "Un camión tiene que recorrer {d} millas a {v} millas por hora. ¿Cuántas horas tarda?", "rp2s": "{d} ÷ {v} = {h} horas.", "rp2p": "Para el tiempo se divide la distancia entre la rapidez.",
  "rp3": "Una persona gana {s} por hora y trabaja {h} horas esta semana. ¿Cuánto gana en total, en dólares?", "rp3s": "{s} × {h} = {r}.",
  "rp4": "Un auto recorre {m} millas por galón. ¿Cuántos galones necesita para un viaje de {d} millas?", "rp4s": "{d} ÷ {m} = {g} galones.", "rp4p": "Se divide la distancia entre las millas por galón.",
  "rp5": "Una mezcla de pintura lleva {a} partes de azul por cada {b} de blanca. Si se usan {ak} partes de azul, ¿cuántas partes de blanca hacen falta para mantener la razón?", "rp5s": "El azul se multiplicó por {k} ({a} × {k} = {ak}), así que la blanca también: {b} × {k} = {r}.", "rp5p": "En una razón no se suma la misma cantidad a los dos términos: se multiplican por el mismo número.",
  "rp6": "Una impresora imprime {p} páginas por minuto. ¿Cuántas páginas imprime en {m} minutos?", "rp6s": "{p} × {m} = {r} páginas."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function rzT(a, b){ return a + TXT.a + b; }
function frH2(a, b){ return '<span aria-hidden="true"><span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + '</span></span></span><span class="sr-only">' + a + '/' + b + '</span>'; }
function pl(n, par){ return n === 1 ? par[0] : par[1]; }

/* ============ MODULE 1 · ratios ============ */
function pintaRZ(){
  var a = +$("rz-a").value, b = +$("rz-b").value, g = mcdR(a, b), p = a / g, q = b / g;
  $("rz-av").textContent = a; $("rz-bv").textContent = b;
  var h = "";
  for (var i = 0; i < g; i++) h += '<div class="grupo">' + '<span class="ico">🧑</span>'.repeat(p) + '<span class="ico">👩‍🏫</span>'.repeat(q) + '</div>';
  $("rz-grupos").innerHTML = h;
  $("rz-grupos-voz").textContent = F(TXT.aria, { g: g, p: p, q: q, e: pl(p, TXT.est), m: pl(q, TXT.mae) });
  $("rz-salida").innerHTML = '<div class="linea">' + F(TXT.razonDe, { a: a, b: b, f: frH2(a, b) }) + '</div>' +
    '<div class="linea">' + (g > 1 ? F(TXT.grupos, { g: g, p: p, q: q }) : F(TXT.yaSimple, { a: a, b: b })) + '</div>' +
    '<div class="linea veredicto">' + F(TXT.porCada, { ser: pl(p, TXT.hay), p: p, e: pl(p, TXT.est), q2: q === 1 ? (ES ? "" : "") : q, m: pl(q, TXT.mae) }).replace("  ", " ") + '</div>';
}
function genRazon(){
  var c = elige(TXT.ctx), k = aleatorio(2, 6), p = aleatorio(1, 6), q = aleatorio(1, 6);
  while (q === p || mcdR(p, q) > 1) q = aleatorio(1, 6);
  var a = p * k, b = q * k, tp = aleatorio(1, 3), enun = F(c[2], { a: a, b: b });
  function op(x, y, cl){ return { html: rzT(x, y), clave: cl }; }
  if (tp === 1) return { enun: enun + F(TXT.simplDe, { x: c[0], y: c[1] }), opciones: [op(p, q, "ok"), op(q, p, "inv"), op(a, b, "sin"), op(p, p + q, "tot")], correcta: "ok",
    pistas: { inv: F(TXT.inv, { x: c[0] }), sin: F(TXT.sin, { k: k }), tot: F(TXT.tot, { y: c[1] }) }, bien: F(TXT.bien1, { a: a, b: b, k: k, r: rzT(p, q) }), mal: F(TXT.mal1, { a: a, b: b, k: k, r: rzT(p, q) }) };
  if (tp === 2) return { enun: enun + F(TXT.simplDe, { x: c[1], y: c[0] }), opciones: [op(q, p, "ok"), op(p, q, "inv"), op(b, a, "sin"), op(q, p + q, "tot")], correcta: "ok",
    pistas: { inv: F(TXT.inv, { x: c[1] }), sin: F(TXT.sin, { k: k }), tot: F(TXT.tot, { y: c[0] }) }, bien: F(TXT.bien1, { a: b, b: a, k: k, r: rzT(q, p) }), mal: F(TXT.mal1, { a: b, b: a, k: k, r: rzT(q, p) }) };
  return { enun: F(TXT.notacion, { p: p, q: q }), opciones: [{ html: F(TXT.notOk, { p: p, q: q }), clave: "ok" }, { html: p + " + " + q, clave: "s" }, { html: F(TXT.menos, { p: p, q: q }), clave: "r" }, { html: rzT(q, p), clave: "i" }],
    correcta: "ok", pista: TXT.pistaNot, bien: F(TXT.bienNot, { p: p, q: q }), mal: F(TXT.bienNot, { p: p, q: q }) };
}

/* ============ MODULE 2 · unit rate ============ */
function pintaTS(){
  var c = TXT.situ[+$("ts-c").value]; $("ts-al").textContent = c[0]; $("ts-bl").textContent = c[1];
  var a = leeD($("ts-a").value), b = leeD($("ts-b").value), av = $("ts-aviso");
  if (a === null || b === null || b <= 0 || a < 0){ av.className = "caja-aviso visible"; av.textContent = TXT.dosPos; $("ts-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var r = Math.round(a / b * 100) / 100;
  $("ts-salida").innerHTML = '<div class="linea">' + F(TXT.divide, { a: nd(a), b: nd(b), r: (Math.abs(r - a / b) > 1e-9 ? "≈ " : "") + nd(r) }) + '</div><div class="linea veredicto">' + nd(r) + ' ' + c[2] + '</div>';
}
function genTasa(){
  var tp = aleatorio(0, 4), r, q;
  if (tp === 0){ r = 5 * aleatorio(8, 14); q = aleatorio(2, 6); }
  else if (tp === 1){ r = elige([1.25, 1.5, 2.25, 3, 3.5, 4.75]); q = aleatorio(2, 8); }
  else if (tp === 2){ r = 5 * aleatorio(6, 16); q = aleatorio(2, 10); }
  else if (tp === 3){ r = elige([12, 14.5, 15, 16.25, 18, 21]); q = aleatorio(4, 10); }
  else { r = aleatorio(20, 35); q = aleatorio(8, 15); }
  var tot = r * q, dn = tp === 1 || tp === 3, tt = dn ? dinero(tot) : nd(tot);
  var pist = [{ v: q / tot, msg: F(TXT.alReves, { a: tt, b: q }) }, { v: tot * q, msg: TXT.noMult }];
  return { enun: F(TXT.ts[tp], { t: tt, q: q }), correcta: dn ? dinero(r) : nd(r),
    solucion: tt + " ÷ " + q + " = " + (dn ? dinero(r) : nd(r)) + " " + TXT.tsU[tp] + ".", evalua: numD(r, pist) };
}

/* ============ MODULE 3 · the better buy ============ */
function genCompra(){
  for (var k = 0; k < 200; k++){
    var pi = aleatorio(0, 4), p = TXT.prod[pi], n = aleatorio(2, 3), ops = [];
    var base = pi === 4 ? [6, 12, 18, 24] : (pi === 0 ? [2, 5, 10, 20] : [16, 24, 32, 48, 64]);
    var tams = baraja(base).slice(0, n).sort(function(x, y){ return x - y; });
    tams.forEach(function(tm, i){
      var unit = Math.round((0.08 + Math.random() * 0.3) * (pi === 0 ? 8 : (pi === 4 ? 1.2 : 1)) * 100) / 100;
      unit = unit * (1 - 0.06 * i + (Math.random() - 0.5) * 0.18);
      var precio = Math.round(unit * tm * 4) / 4; ops.push({ t: tm, precio: precio, u: precio / tm, l: "ABC"[i] });
    });
    var us = ops.map(function(o){ return Math.round(o.u * 1000); });
    if (us.some(function(x, i){ return us.indexOf(x) !== i; }) || ops.some(function(o){ return o.precio <= 0; })) continue;
    var mejor = ops.reduce(function(m, o){ return o.u < m.u ? o : m; });
    if (mejor === ops[0] && Math.random() < 0.7) continue;
    var tabla = ops.map(function(o){ return F(TXT.linea, { l: o.l, p: dinero(o.precio), n: o.t, r: o.u.toFixed(3), u: p[2] }); }).join("; ");
    var o = ops.map(function(x){ return { html: F(TXT.opcionDe, { l: x.l, n: x.t, u: p[1], p: dinero(x.precio) }), clave: x.l }; });
    var pc = {}, barata = ops.reduce(function(m, x){ return x.precio < m.precio ? x : m; });
    if (barata !== mejor) pc[barata.l] = F(TXT.engana, { u: p[2] });
    return { enOrden: true, enun: F(TXT.cual, { x: p[0], u: p[2] }), opciones: o, correcta: mejor.l, pistas: pc, pista: TXT.pistaComp,
      bien: tabla + F(TXT.conviene, { l: mejor.l }), mal: tabla + F(TXT.masBarata, { u: p[2], l: mejor.l }) };
  }
}

/* ============ MODULE 4 · speed and other rates ============ */
function pintaRP(){
  var v = +$("rp-v").value, tm = +$("rp-t").value, d = v * tm, x0 = 30, x1 = 610, esc = (x1 - x0) / 640;
  $("rp-vv").textContent = v; $("rp-tv").textContent = nd(tm);
  var s = '<svg class="figura" viewBox="0 0 640 112" role="img" aria-label="' + F(TXT.rpAria, { d: nd(d), t: nd(tm), v: v }) + '">';
  s += '<rect x="' + x0 + '" y="40" width="' + (x1 - x0) + '" height="22" rx="4" fill="#eeeeee"/>';
  s += '<rect x="' + x0 + '" y="40" width="' + f1(d * esc) + '" height="22" rx="4" fill="#4db6ac"/>';
  for (var h = 1; h <= Math.floor(tm); h++) s += linea([x0 + v * h * esc, 34], [x0 + v * h * esc, 68], "#004d40", 2) + texto([x0 + v * h * esc, 84], h + " h", 13, "#004d40", 700);
  s += texto([x0 + d * esc, 22], "🚗", 22, "#000", 400);
  s += '<text x="' + x0 + '" y="104" font-size="13" fill="#424242">0</text><text x="' + x1 + '" y="104" font-size="13" fill="#424242" text-anchor="end">' + TXT.millas + '</text>';
  $("rp-svg").innerHTML = s + '</svg>';
  $("rp-salida").innerHTML = '<div class="linea">' + F(TXT.cadaHora, { v: v }) + '</div><div class="linea veredicto">' + F(TXT.dist, { v: v, t: nd(tm), d: nd(d) }) + '</div>';
}
function genRapidez(){
  var tp = aleatorio(1, 6), res, enun, sol, p = [];
  if (tp === 1){ var v = 5 * aleatorio(8, 14), h = aleatorio(2, 6); res = v * h; enun = F(TXT.rp1, { v: v, h: h }); sol = F(TXT.rp1s, { v: v, h: h, r: nd(res) }); p.push({ v: v / h, msg: TXT.rp1p }); }
  else if (tp === 2){ var v2 = 5 * aleatorio(8, 14), h2 = aleatorio(2, 6), d2 = v2 * h2; res = h2; enun = F(TXT.rp2, { d: nd(d2), v: v2 }); sol = F(TXT.rp2s, { d: nd(d2), v: v2, h: h2 }); p.push({ v: d2 * v2, msg: TXT.rp2p }); }
  else if (tp === 3){ var sal = elige([13.5, 15, 16, 17.25, 18.5]), hh = aleatorio(15, 40); res = sal * hh; enun = F(TXT.rp3, { s: dinero(sal), h: hh }); sol = F(TXT.rp3s, { s: dinero(sal), h: hh, r: dinero(res) }); }
  else if (tp === 4){ var mpg = aleatorio(22, 35), gal = aleatorio(4, 12), dist = mpg * gal; res = gal; enun = F(TXT.rp4, { m: mpg, d: nd(dist) }); sol = F(TXT.rp4s, { d: nd(dist), m: mpg, g: gal }); p.push({ v: dist * mpg, msg: TXT.rp4p }); }
  else if (tp === 5){ var az = aleatorio(2, 4), bl = aleatorio(3, 7); while (mcdR(az, bl) > 1) bl++; var k = aleatorio(2, 5); res = bl * k; enun = F(TXT.rp5, { a: az, b: bl, ak: az * k }); sol = F(TXT.rp5s, { a: az, b: bl, k: k, ak: az * k, r: res }); p.push({ v: az * k + (bl - az), msg: TXT.rp5p }); }
  else { var ppm = aleatorio(40, 70), mins = aleatorio(3, 10); res = ppm * mins; enun = F(TXT.rp6, { p: ppm, m: mins }); sol = F(TXT.rp6s, { p: ppm, m: mins, r: nd(res) }); }
  return { enun: enun, correcta: tp === 3 ? dinero(res) : nd(res), solucion: sol, evalua: numD(res, p.filter(function(x){ return Math.abs(x.v - res) > 0.01; })) };
}

/* ============ Start ============ */
["rz-a", "rz-b"].forEach(function(id){ $(id).addEventListener("input", pintaRZ); }); pintaRZ();
creaPracticaOM("p1", genRazon);
$("ts-c").addEventListener("change", pintaTS); ["ts-a", "ts-b"].forEach(function(id){ $(id).addEventListener("input", pintaTS); }); pintaTS();
creaPracticaLibre("p2", genTasa);
creaPracticaOM("p3", genCompra);
["rp-v", "rp-t"].forEach(function(id){ $(id).addEventListener("input", pintaRP); }); pintaRP();
creaPracticaLibre("p4", genRapidez);
'''

def libre_d(pid, titulo, etiqueta):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."),
        t("Type only the number. It may have decimals, like 1.25; for money you may use the $ sign.", "Escriba solo el número. Puede llevar decimales, como 1.25; si es dinero, puede usar el signo $."))

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    situ = TX[B.L]["situ"]
    opts = "".join(f'<option value="{i}">{s[0].lower()} / {s[1].lower()}</option>' for i, s in enumerate(situ))
    mods = [
     (t("ratio", "razon"), t("What a ratio is", "Qué es una razón"),
      f'''      <p>{t("A <strong>ratio</strong> compares two quantities of the same kind: “so many for every so many.” It can be written three ways that mean the same: <strong>4 to 1</strong>, <strong>4 : 1</strong>, or <strong>4/1</strong>. You simplify it like a fraction, dividing both terms by their greatest common factor.", "Una <strong>razón</strong> compara dos cantidades del mismo tipo: «tantos por cada tantos». Se escribe de tres formas que significan lo mismo: <strong>4 a 1</strong>, <strong>4 : 1</strong> o <strong>4/1</strong>. Se simplifica como una fracción, dividiendo los dos términos entre su máximo común divisor.")}</p>
      <h3>{t("Make the groups", "Forme los grupos")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("rz-a", t("Students 🧑", "Estudiantes 🧑"), 1, 24, 12)}
          {desl("rz-b", t("Teachers 👩‍🏫", "Maestros 👩‍🏫"), 1, 12, 3)}
        </div>
        <div class="grupos" id="rz-grupos" aria-hidden="true"></div>
        <p class="sr-only" id="rz-grupos-voz"></p>
        <div class="salida" id="rz-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Order matters:", "El orden importa:")}</strong> {t("“wheat to rye” is 3 to 2, but “rye to wheat” is 2 to 3. The quantity named first goes first.", "«trigo a centeno» es 3 a 2, pero «centeno a trigo» es 2 a 3. La cantidad que se nombra primero va primero.")}</div>
{B.om("p1", t("Practice: ratios", "Practique: razones"))}'''),
     (t("rate", "tasa"), t("The unit rate", "La tasa unitaria"),
      f'''      <p>{t("When the two quantities have <strong>different units</strong> (miles and hours, dollars and pounds), the ratio is called a <strong>rate</strong>. The <strong>unit rate</strong> has 1 as its second term: divide the first term by the second. The words “per” and “each” give it away.", "Cuando las dos cantidades tienen <strong>unidades distintas</strong> (millas y horas, dólares y libras), la razón se llama <strong>tasa</strong>. La <strong>tasa unitaria</strong> tiene 1 como segundo término: se divide el primer término entre el segundo. Las palabras «por» y «cada» la delatan.")}</p>
      <h3>{t("Find the unit rate", "Calcule la tasa unitaria")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="ts-c">{t("Situation", "Situación")}</label><select id="ts-c">{opts}</select></div>
          <div class="campo"><label for="ts-a" id="ts-al">{situ[0][0]}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="ts-a" value="240"></div>
          <div class="campo"><label for="ts-b" id="ts-bl">{situ[0][1]}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="ts-b" value="4"></div>
        </div>
        <div class="caja-aviso" id="ts-aviso" role="alert"></div>
        <div class="salida" id="ts-salida" aria-live="polite"></div>
      </div>
{libre_d("p2", t("Practice: unit rates", "Practique: tasas unitarias"), t("Unit rate", "Tasa unitaria"))}'''),
     (t("compare", "comparar"), t("Comparing options", "Comparar opciones"),
      f'''      <p>{t("To find the better buy, find the <strong>price per unit</strong> of each option. The lowest total price is not always the better buy: a small package costs less in all, but sometimes more per unit.", "Para saber qué opción conviene, se calcula el <strong>precio por unidad</strong> de cada una. El precio total más bajo no siempre es la mejor compra: un paquete pequeño cuesta menos en total, pero a veces más por unidad.")}</p>
{B.om("p3", t("Practice: which is the better buy?", "Practique: ¿cuál es la mejor compra?"))}'''),
     (t("speed", "rapidez"), t("Speed and other rates in context", "Rapidez y otras tasas en contexto"),
      f'''      <p>{t("Once you know the unit rate, use it: at 60 miles per hour, in 3 hours a car goes 60 × 3 = 180 miles, and 300 miles take 300 ÷ 60 = 5 hours. The same works for pay, gas use, and mixes.", "Conocida la tasa unitaria, se usa para calcular: a 60 millas por hora, en 3 horas un auto recorre 60 × 3 = 180 millas, y 300 millas le toman 300 ÷ 60 = 5 horas. Lo mismo sirve para salarios, consumo de gasolina o mezclas.")}</p>
      <div class="formula">{t("distance = speed × time", "distancia = rapidez × tiempo")}</div>
      <h3>{t("The trip", "El viaje")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("rp-v", t("Speed (miles per hour)", "Rapidez (millas por hora)"), 10, 80, 60, 5)}
          {desl("rp-t", t("Time (hours)", "Tiempo (horas)"), 0.5, 8, 3, 0.5)}
        </div>
        <div id="rp-svg"></div>
        <div class="salida" id="rp-salida" aria-live="polite"></div>
      </div>
{libre_d("p4", t("Practice: rates in context", "Practique: tasas en contexto"), t("Answer", "Resultado"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Razones y tasas unitarias")
