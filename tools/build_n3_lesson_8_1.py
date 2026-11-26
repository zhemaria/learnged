"""Level 3 · Lesson 8.1 · The counting principle, permutations, and combinations — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_8-1.html and algebra/n3-l8-1.html (GEDparaHispanos).
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n3
from build_n3_lesson_7_1 import ESTILO

B.NIVEL = 3
N = "8-1"
TEMA = ("Counting and probability", "Combinatoria y probabilidad")
TIT = ("The counting principle, permutations, and combinations", "Principio fundamental del conteo, permutaciones y combinaciones")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js", "/math/data3.js", "/math/prob3.js")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def figura_arbol():
    platos = (t("Chicken", "Pollo"), t("Fish", "Pescado"))
    bebidas = (t("Water", "Agua"), t("Juice", "Jugo"), t("Coffee", "Café"))
    s = f'<circle cx="40" cy="150" r="6" fill="#424242"/><text x="40" y="132" font-size="14" text-anchor="middle" fill="#424242">{t("Start", "Inicio")}</text>'
    for i, p in enumerate(platos):
        y = 75 + i * 150
        s += f'<line x1="40" y1="150" x2="190" y2="{y}" stroke="#b71c1c" stroke-width="2.5"/><circle cx="190" cy="{y}" r="5" fill="#424242"/><text x="190" y="{y - 12}" font-size="15" font-weight="700" text-anchor="middle" fill="#b71c1c">{p}</text>'
        for j, b in enumerate(bebidas):
            yy = y - 45 + j * 45
            s += f'<line x1="190" y1="{y}" x2="340" y2="{yy}" stroke="#0d47a1" stroke-width="2"/><circle cx="340" cy="{yy}" r="4" fill="#424242"/><text x="350" y="{yy + 5}" font-size="14" fill="#0d47a1">{b}</text>'
    s += '<text x="470" y="155" font-size="22" font-weight="700" fill="#1b5e20">2 × 3 = 6</text>'
    return B.svg("0 0 600 300", t("A tree diagram. From the start, two branches: chicken and fish. Each one opens into three branches: water, juice, and coffee. In all there are 2 × 3 = 6 meals.",
                                  "Un diagrama de árbol. Desde el inicio salen dos ramas: pollo y pescado. Cada una se abre en tres ramas: agua, jugo y café. En total hay 2 × 3 = 6 comidas."), s, 560)

def leccion():
    n = N
    s1 = f'''<p>{t("Topic 7 summarized and interpreted data. Topic 8 opens <strong>combinatorics</strong>: the art of counting how many ways things can happen. Counting the possible outcomes is the direct basis of probability, which you will study in the next lesson. It is also the first step in closing Level 3.", "El Tema 7 resumió e interpretó datos. El Tema 8 abre la <strong>combinatoria</strong>: el arte de contar de cuántas formas pueden ocurrir las cosas. Saber contar resultados posibles es la base directa de la probabilidad, que se estudiará en la próxima lección. Es también el primer paso del cierre del Nivel 3.")}</p>
<p>{t("If one event can happen in m ways and another in n ways, then the two together can happen in m × n ways. The idea extends to more events: multiply the choices for each one.", "Si un evento puede ocurrir de m formas y otro de n formas, entonces los dos juntos pueden ocurrir de m × n formas. La idea se extiende a más eventos: se multiplican las opciones de cada uno.")}</p>
<p class="formula" style="text-align:center;font-weight:700;">{t("Total outcomes = (choices for the 1st) × (choices for the 2nd) × …", "Total de resultados = (opciones del 1.º) × (opciones del 2.º) × …")}</p>
{figura_arbol()}
{ejemplo(t("Example 1: a menu has 2 main dishes and 3 drinks. How many dish-and-drink pairs are there?", "Ejemplo 1: un menú ofrece 2 platos principales y 3 bebidas. ¿Cuántas combinaciones de plato y bebida hay?"),
  [("1", t("Multiply the choices.", "Se multiplican las opciones."), "2 × 3 = 6."),
   ("✓", t("Answer.", "Respuesta."), t("There are <strong>6</strong> possible pairs.", "Hay <strong>6</strong> combinaciones posibles."))])}
{practica("p1", t("Practice 1 — Outfits", "Práctica 1 — Conjuntos"), t("There are 4 shirts and 3 pairs of pants. How many different outfits can you make?", "Hay 4 camisas y 3 pantalones. ¿Cuántos conjuntos distintos se pueden formar?"), [("a", "7"), ("b", "12"), ("c", "43")])}
{enlace(n, t("counting", "conteo"), t("the counting principle", "el principio fundamental del conteo"), t("Count possibilities with a tree diagram and by multiplying.", "Cuente posibilidades con un diagrama de árbol y multiplicando."))}'''

    s2 = f'''<p>{t("The <strong>factorial</strong> of a number, written n!, is the product of all the whole numbers from 1 to n. It appears in the formulas for permutations and combinations.", "El <strong>factorial</strong> de un número, escrito n!, es el producto de todos los enteros desde 1 hasta n. Aparece en las fórmulas de permutaciones y combinaciones.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">n! = n × (n − 1) × … × 2 × 1</p>
{ejemplo(t("Example 2: find 5!.", "Ejemplo 2: calcular 5!."),
  [("1", t("Multiply the whole numbers from 5 down to 1.", "Se multiplican los enteros del 5 al 1."), "5 × 4 × 3 × 2 × 1 = 120."),
   ("✓", t("Answer.", "Respuesta."), "5! = <strong>120</strong>.")])}
{caja("tip", t("The special case 0!", "El caso especial 0!"), t("<p>By agreement, 0! = 1. That makes the formulas work correctly.</p>", "<p>Por convención, 0! = 1. Esto hace que las fórmulas funcionen correctamente.</p>"))}
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. It has keys for the factorial and for permutations and combinations: <strong>n!</strong>, <strong>nPr</strong>, and <strong>nCr</strong> (on the TI-30XS they are in the PRB menu). The calculator on this page has them too, although they may have other names or be in other places.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. Tiene teclas para el factorial y para las permutaciones y combinaciones: <strong>n!</strong>, <strong>nPr</strong> y <strong>nCr</strong> (en la TI-30XS están en el menú PRB). La calculadora de esta página también las tiene, aunque pueden tener otro nombre o estar en otro lugar.</p>"))}
{practica("p2", t("Practice 2 — A factorial", "Práctica 2 — Un factorial"), t("What is 4!?", "¿Cuánto es 4!?"), [("a", "24"), ("b", "12"), ("c", "4")])}
{enlace(n, t("factorial", "factorial"), t("the factorial", "el factorial"), t("Find factorials and simplify quotients of factorials.", "Calcule factoriales y simplifique cocientes de factoriales."))}'''

    s3 = f'''<p>{t("A <strong>permutation</strong> counts how many ways items can be put in order. Use it when the order matters (a podium, a code, the order of arrival).", "Una <strong>permutación</strong> cuenta de cuántas formas se pueden ordenar los elementos. Se usa cuando el orden sí importa (un podio, una clave, un orden de llegada).")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">P(n, r) = {fx("n!", "(n − r)!")}</p>
{ejemplo(t("Example 3: in how many ways can you arrange 3 books out of 5 on a shelf?", "Ejemplo 3: ¿de cuántas formas se pueden ordenar 3 libros de un total de 5 en un estante?"),
  [("1", t("Here n = 5 and r = 3, and the order matters.", "Aquí n = 5 y r = 3, y el orden importa."), f"P(5, 3) = {fx('5!', '(5 − 3)!')} = {fx('5!', '2!')}."),
   ("2", t("Calculate.", "Se calcula."), t("120 ÷ 2 = 60. (Or count the places: 5 × 4 × 3 = 60.)", "120 ÷ 2 = 60. (O se cuentan los lugares: 5 × 4 × 3 = 60.)")),
   ("✓", t("Answer.", "Respuesta."), t("There are <strong>60</strong> ways to arrange them.", "Hay <strong>60</strong> formas de ordenarlos."))])}
{practica("p3", t("Practice 3 — In a line", "Práctica 3 — En fila"), t("In how many ways can 3 people stand in a line?", "¿De cuántas formas se pueden ordenar 3 personas en una fila?"), [("a", "3"), ("b", "9"), ("c", "6")])}
{enlace(n, t("permutations", "permutaciones"), t("permutations: order matters", "permutaciones: el orden importa"), t("Count arrangements with P(n, r).", "Cuente ordenaciones con P(n, r)."))}'''

    filas = [[t("Yes", "Sí"), t("Permutation", "Permutación"), t("A podium (1st, 2nd, 3rd), a code", "Podio (1.º, 2.º, 3.º), una clave")],
             ["No", t("Combination", "Combinación"), t("A committee, a group of friends", "Un comité, un grupo de amigos")]]
    s4 = f'''<p>{t("A <strong>combination</strong> counts how many ways you can choose a group, when the order does not matter (a committee, a hand of cards, a group of friends). That is why its formula also divides by r!, which removes the repeated orders.", "Una <strong>combinación</strong> cuenta de cuántas formas se puede elegir un grupo, sin importar el orden (un comité, una mano de cartas, un grupo de amigos). Por eso su fórmula divide además entre r!, que elimina los órdenes repetidos.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">C(n, r) = {fx("n!", "r! (n − r)!")}</p>
{ejemplo(t("Example 4: in how many ways can you choose 3 books out of 5 to take on a trip (order does not matter)?", "Ejemplo 4: ¿de cuántas formas se pueden elegir 3 libros de 5 para llevar de viaje (sin importar el orden)?"),
  [("1", "n = 5, r = 3.", f"C(5, 3) = {fx('5!', '3! (5 − 3)!')} = {fx(120, '6 × 2')}."),
   ("2", t("Calculate.", "Se calcula."), "120 ÷ 12 = 10."),
   ("✓", t("Answer.", "Respuesta."), t("There are <strong>10</strong> ways to choose them.", "Hay <strong>10</strong> formas de elegirlos."))])}
{tabla(t("Permutation or combination?", "¿Permutación o combinación?"), t("How to tell a permutation from a combination", "Cómo distinguir entre permutación y combinación"), [t("Does order matter?", "¿El orden importa?"), t("Type", "Tipo"), t("Example", "Ejemplo")], filas)}
{caja("ojo", t("The key question", "La pregunta clave"), t("<p>Before you calculate, ask yourself: “Does the result change if I change the order?” If yes → permutation. If no → combination. Mixing them up is the most common mistake in this topic.</p>", "<p>Antes de calcular, conviene preguntarse: «¿cambia el resultado si cambio el orden?». Si sí → permutación. Si no → combinación. Confundir ambos es el error más frecuente del tema.</p>"))}
{practica("p4", t("Practice 4 — A committee", "Práctica 4 — Un comité"), t("Choosing a committee of 3 people from a group of 10 is a problem of…", "Elegir un comité de 3 personas de un grupo de 10 es un problema de…"), [("a", t("combination (order does not matter)", "combinación (el orden no importa)")), ("b", t("permutation (order matters)", "permutación (el orden importa)")), ("c", t("the counting principle only", "principio del conteo solamente"))])}
{practica("p5", t("Practice 5 — A race", "Práctica 5 — Una carrera"), t("Giving 1st, 2nd, and 3rd place to 5 runners is a problem of…", "Asignar 1.º, 2.º y 3.º lugar a 5 corredores es un problema de…"), [("a", t("combination (order does not matter)", "combinación (el orden no importa)")), ("b", t("the factorial of 3", "factorial de 3")), ("c", t("permutation (order matters)", "permutación (el orden importa)"))])}
{practica("p6", "C(4, 2)", t("What is C(4, 2)?", "¿Cuánto es C(4, 2)?"), [("a", "12"), ("b", "6"), ("c", "8")])}
{enlace(n, t("combinations", "combinaciones"), t("combinations: order does not matter", "combinaciones: el orden no importa"), t("Count groups with C(n, r).", "Cuente selecciones con C(n, r)."))}
{enlace(n, t("decide", "decidir"), t("does order matter?", "¿importa el orden?"), t("Decide whether each situation is a permutation, a combination, or the counting principle.", "Decida si cada situación es una permutación, una combinación o el principio del conteo."))}'''

    secciones = [("s-" + t("counting", "conteo"), t("The counting principle", "El principio fundamental del conteo"), s1),
                 ("s-factorial", t("The factorial", "El factorial"), s2),
                 ("s-" + t("permutations", "permutaciones"), t("Permutations: order matters", "Permutaciones: el orden importa"), s3),
                 ("s-" + t("combinations", "combinaciones"), t("Combinations: order does not matter", "Combinaciones: el orden no importa"), s4)]

    lesson = {"next": t("Lesson 8.2", "Lección 8.2"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You added. Each shirt goes with each pair of pants: multiply.", "Sumó. Cada camisa va con cada pantalón: se multiplica."), "c": t("You wrote the numbers side by side. Multiply them.", "Escribió los números juntos. Hay que multiplicarlos.")}, "right": "4 × 3 = 12.", "solution": "4 × 3 = 12."},
      "p2": {"ok": "a", "hints": {"b": t("12 is 4 × 3. Keep going: × 2 × 1.", "12 es 4 × 3. Siga: × 2 × 1."), "c": t("4! is not 4: multiply 4 × 3 × 2 × 1.", "4! no es 4: se multiplica 4 × 3 × 2 × 1.")}, "right": "4 × 3 × 2 × 1 = 24.", "solution": "4! = 24."},
      "p3": {"ok": "c", "hints": {"a": t("The first place has 3 choices, the second 2, and the third 1.", "El primer lugar tiene 3 opciones, el segundo 2 y el tercero 1."), "b": t("That is 3 × 3. Each person can only be in one place: 3 × 2 × 1.", "Eso es 3 × 3. Cada persona solo puede estar en un lugar: 3 × 2 × 1.")}, "right": "3! = 3 × 2 × 1 = 6.", "solution": "3! = 6."},
      "p4": {"ok": "a", "hints": {"b": t("In a committee everyone has the same role. Does the order change the committee?", "En un comité todos tienen el mismo papel. ¿El orden cambia el comité?"), "c": t("All the members come from the same group, and order does not matter.", "Todos los miembros salen del mismo grupo, y el orden no importa.")}, "right": t("Ana, Luis, and Rosa form the same committee in any order: combination.", "Ana, Luis y Rosa forman el mismo comité en cualquier orden: combinación."), "solution": t("Combination.", "Combinación.")},
      "p5": {"ok": "c", "hints": {"a": t("Is finishing first the same as finishing third?", "¿Es lo mismo llegar primero que tercero?"), "b": t("There are 5 runners, not 3: P(5, 3) = 5 × 4 × 3.", "Son 5 corredores, no 3: P(5, 3) = 5 × 4 × 3.")}, "right": t("The places are different, so order matters: permutation.", "Los lugares son distintos, así que el orden importa: permutación."), "solution": t("Permutation.", "Permutación.")},
      "p6": {"ok": "b", "hints": {"a": t("12 is P(4, 2), where order matters. Divide by 2! = 2.", "12 es P(4, 2), donde el orden importa. Divida entre 2! = 2."), "c": t("That is 4 × 2. Use C(4, 2) = (4 × 3) ÷ (2 × 1).", "Eso es 4 × 2. Use C(4, 2) = (4 × 3) ÷ (2 × 1).")}, "right": "(4 × 3) ÷ (2 × 1) = 6.", "solution": "C(4, 2) = 6."}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("You added. Multiply the choices.", "Sumó. Se multiplican las opciones."), "b": t("You wrote the numbers side by side. Multiply them.", "Escribió los números juntos. Hay que multiplicarlos."), "d": t("3 is only the number of appetizers.", "3 es solo el número de entradas.")}, "solution": "3 × 4 = 12."},
      "B": {"ok": "a", "hints": {"b": t("25 is 5 × 5. Multiply 5 × 4 × 3 × 2 × 1.", "25 es 5 × 5. Multiplique 5 × 4 × 3 × 2 × 1."), "c": t("You added 5 + 4 + 3 + 2 + 1. Multiply.", "Sumó 5 + 4 + 3 + 2 + 1. Hay que multiplicar."), "d": t("20 is 5 × 4. Keep going: × 3 × 2 × 1.", "20 es 5 × 4. Siga: × 3 × 2 × 1.")}, "solution": "5! = 120."},
      "C": {"ok": "c", "hints": {"a": t("12 is 4 × 3. Keep going: × 2 × 1.", "12 es 4 × 3. Siga: × 2 × 1."), "b": t("16 is 4 × 4. Each person can only take one place.", "16 es 4 × 4. Cada persona solo ocupa un lugar."), "d": t("4 is the number of people. The places: 4 × 3 × 2 × 1.", "4 es el número de personas. Los lugares: 4 × 3 × 2 × 1.")}, "solution": "4! = 24."},
      "D": {"ok": "b", "hints": {"a": t("10 is C(5, 2), where order does not matter.", "10 es C(5, 2), donde el orden no importa."), "c": t("25 is 5 × 5. Without repeating: 5 × 4.", "25 es 5 × 5. Sin repetir: 5 × 4."), "d": t("You added. Multiply 5 × 4.", "Sumó. Multiplique 5 × 4.")}, "solution": "P(5, 2) = 5 × 4 = 20."},
      "E": {"ok": "d", "hints": {"a": t("20 is P(5, 2). Divide by 2! = 2.", "20 es P(5, 2). Divida entre 2! = 2."), "b": t("25 is 5 × 5. Use (5 × 4) ÷ (2 × 1).", "25 es 5 × 5. Use (5 × 4) ÷ (2 × 1)."), "c": t("You added. Use (5 × 4) ÷ (2 × 1).", "Sumó. Use (5 × 4) ÷ (2 × 1).")}, "solution": "C(5, 2) = 20 ÷ 2 = 10."},
      "F": {"ok": "a", "hints": {"b": t("30 is P(6, 2). Divide by 2! = 2.", "30 es P(6, 2). Divida entre 2! = 2."), "c": t("12 is 6 × 2. Use (6 × 5) ÷ (2 × 1).", "12 es 6 × 2. Use (6 × 5) ÷ (2 × 1)."), "d": t("36 is 6 × 6. Use (6 × 5) ÷ (2 × 1).", "36 es 6 × 6. Use (6 × 5) ÷ (2 × 1).")}, "solution": "C(6, 2) = 30 ÷ 2 = 15."},
      "G": {"ok": "c", "hints": {"a": t("Does a salad change if you pick the fruits in another order?", "¿La ensalada cambia si se eligen las frutas en otro orden?"), "b": t("Only 3 of the 7 fruits are chosen.", "Solo se eligen 3 de las 7 frutas."), "d": t("All the fruits come from the same group, and order does not matter.", "Todas las frutas salen del mismo grupo, y el orden no importa.")}, "solution": t("Combination.", "Combinación.")},
      "H": {"ok": "d", "hints": {"a": t("Are gold and bronze the same prize?", "¿El oro y el bronce son el mismo premio?"), "b": t("Only 3 of the 8 athletes get a medal.", "Solo 3 de los 8 atletas reciben medalla."), "c": t("The medals go to people from the same group, and order matters.", "Las medallas van a personas del mismo grupo, y el orden importa.")}, "solution": t("Permutation: P(8, 3).", "Permutación: P(8, 3).")}
     }}

    quiz = [
     ("A", t("There are 3 appetizers and 4 main dishes. How many different meals (one of each) can you make?", "Hay 3 entradas y 4 platos principales. ¿Cuántas comidas distintas (una de cada) se pueden formar?"), [("a", "7"), ("b", "34"), ("c", "12"), ("d", "3")]),
     ("B", t("What is 5!?", "¿Cuánto es 5!?"), [("a", "120"), ("b", "25"), ("c", "15"), ("d", "20")]),
     ("C", t("In how many ways can 4 people stand in a line?", "¿De cuántas formas se pueden ordenar 4 personas en una fila?"), [("a", "12"), ("b", "16"), ("c", "24"), ("d", "4")]),
     ("D", t("What is P(5, 2)?", "¿Cuánto es P(5, 2)?"), [("a", "10"), ("b", "20"), ("c", "25"), ("d", "7")]),
     ("E", t("What is C(5, 2)?", "¿Cuánto es C(5, 2)?"), [("a", "20"), ("b", "25"), ("c", "7"), ("d", "10")]),
     ("F", t("What is C(6, 2)?", "¿Cuánto es C(6, 2)?"), [("a", "15"), ("b", "30"), ("c", "12"), ("d", "36")]),
     ("G", t("Choosing 3 fruits out of 7 for a salad (order does not matter) is…", "Elegir 3 frutas de 7 para una ensalada (sin importar el orden) es…"), [("a", t("a permutation", "permutación")), ("b", t("a factorial only", "solo factorial")), ("c", t("a combination", "combinación")), ("d", t("the counting principle", "principio del conteo"))]),
     ("H", t("Giving gold, silver, and bronze to 3 of 8 athletes is…", "Asignar oro, plata y bronce a 3 de 8 atletas es…"), [("a", t("a combination", "combinación")), ("b", t("the factorial of 8", "factorial de 8")), ("c", t("the counting principle only", "principio del conteo solamente")), ("d", t("a permutation", "permutación"))])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Count outcomes by multiplying, use the factorial, and tell when order matters (permutation) and when it does not (combination).", "Cuente resultados multiplicando, use el factorial y distinga cuándo el orden importa (permutación) y cuándo no (combinación)."),
        ("🧮", t("Keys n!, nPr, and nCr", "Teclas n!, nPr y nCr")),
        [t("<strong>Use</strong> the counting principle to find the total outcomes of events in a row.", "<strong>Aplicar</strong> el principio fundamental del conteo para hallar el total de resultados de eventos sucesivos."),
         t("<strong>Understand</strong> the factorial (n!) as the product of the whole numbers from 1 to n.", "<strong>Comprender</strong> el factorial (n!) como producto de los enteros del 1 al n."),
         t("<strong>Find</strong> permutations, where order matters: P(n, r) = n! / (n − r)!.", "<strong>Calcular</strong> permutaciones, donde el orden importa: P(n, r) = n! / (n − r)!."),
         t("<strong>Find</strong> combinations, where order does not matter: C(n, r) = n! / [r!(n − r)!].", "<strong>Calcular</strong> combinaciones, donde el orden no importa: C(n, r) = n! / [r!(n − r)!]."),
         t("<strong>Tell</strong> when a problem asks for a permutation and when it asks for a combination.", "<strong>Distinguir</strong> cuándo un problema pide una permutación y cuándo una combinación.")],
        secciones,
        (t("Solve three counting-principle problems (menus, outfits, codes), three permutations, and three combinations. For each one, write first whether order matters, then calculate by hand and check with the calculator's nPr and nCr keys.",
           "Resuelva tres problemas del principio del conteo (menús, conjuntos, claves), tres de permutaciones y tres de combinaciones. En cada uno, escriba primero si el orden importa; después calcule a mano y compruebe con las teclas nPr y nCr de la calculadora."),
         t("Count the outfits you could make with the shirts, pants, and shoes in your closet. Then think of a lock or a phone PIN: how many 4-digit codes are possible if digits can repeat? And if they cannot?",
           "Cuente los conjuntos que podría formar con las camisas, pantalones y zapatos de su clóset. Después piense en un candado o en el PIN de un teléfono: ¿cuántas claves de 4 dígitos hay si los dígitos se pueden repetir? ¿Y si no se pueden repetir?")),
        quiz,
        t("Self-check checklist for counting", "Lista de autoevaluación de conteo"),
        t("Self-check checklist: skills for the counting principle, permutations, and combinations", "Lista de autoevaluación: destrezas del principio del conteo, permutaciones y combinaciones"),
        [(t("The counting principle", "Principio del conteo"), t("I multiply the choices for each event and can check with a tree diagram.", "Multiplico las opciones de cada evento y puedo comprobar con un diagrama de árbol."), t("I multiply with occasional mistakes.", "Multiplico con errores ocasionales."), t("I do not multiply the choices for each event.", "No multiplico las opciones de cada evento.")),
         (t("Permutation or combination", "Permutación o combinación"), t("I decide whether the problem asks for a permutation or a combination, and explain why.", "Determino si el problema pide permutación o combinación, y lo justifico."), t("I tell them apart with some mistakes.", "Distingo el tipo con errores."), t("I cannot tell whether order matters.", "No distingo si el orden importa.")),
         (t("Using the formula", "Aplicar la fórmula"), t("I use the right formula without factorial mistakes and check with the calculator.", "Aplico la fórmula correcta sin errores de factorial y compruebo con la calculadora."), t("I use the formula with factorial mistakes.", "Aplico la fórmula con errores de factorial."), t("I do not use the factorial correctly.", "No uso correctamente el factorial."))],
        t("<p>In this lesson you learned to count possible outcomes: the counting principle (multiply the choices), the factorial, permutations (when order matters), and combinations (when it does not), and when to use each one.</p>\n<p>In <strong>Lesson 8.2 · Compound probability: with and without replacement</strong> you will use this counting to find the probability of two or more events: the probability that A happens and then B, and how the answer changes with or without replacement.</p>",
          "<p>En esta lección se aprendió a contar resultados posibles: el principio fundamental del conteo (multiplicar las opciones), el factorial, las permutaciones (cuando el orden importa) y las combinaciones (cuando no importa), distinguiendo cuándo aplicar cada una.</p>\n<p>En la <strong>Lección 8.2 · Probabilidad compuesta: con y sin reemplazo</strong> se usará este conteo para calcular probabilidades de dos o más eventos: la probabilidad de que ocurra A y luego B, viendo cómo cambia el resultado según haya o no reemplazo.</p>"),
        ("8-2", ("", t("Lesson 8.2 · Compound probability: with and without replacement", "Lección 8.2 · Probabilidad compuesta: con y sin reemplazo"))),
        [(t("counting principle", "principio fundamental del conteo"), t("If one event can happen in m ways and another in n ways, together they can happen in m × n ways.", "Si un evento ocurre de m formas y otro de n formas, juntos ocurren de m × n formas.")),
         (t("factorial", "factorial"), t("n! = n × (n − 1) × … × 1. By agreement, 0! = 1.", "n! = n × (n − 1) × … × 1. Por convención, 0! = 1.")),
         (t("permutation", "permutación"), t("An arrangement in which order matters: P(n, r).", "Una ordenación en la que el orden importa: P(n, r).")),
         (t("combination", "combinación"), t("A choice of a group in which order does not matter: C(n, r).", "Una elección de un grupo en la que el orden no importa: C(n, r)."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* MODULE 1 · The tree */
var OPCIONES = [[T("chicken", "pollo"), T("pasta", "pasta"), T("fish", "pescado"), T("rice", "arroz")], [T("water", "agua"), T("juice", "jugo"), T("coffee", "café"), T("tea", "té")], [T("flan", "flan"), T("fruit", "fruta"), T("ice cream", "helado")]];
var COL_AR = ["#b71c1c", "#0d47a1", "#1b5e20"];
function pintaArbol(){
  var ns = [+$("ar-a").value, +$("ar-b").value, +$("ar-c").value].filter(function(x, i){ return i < 2 || x > 0; });
  $("ar-av").textContent = $("ar-a").value; $("ar-bv").textContent = $("ar-b").value; $("ar-cv").textContent = $("ar-c").value === "0" ? T("none", "ninguno") : $("ar-c").value;
  var total = ns.reduce(function(a, b){ return a * b; }, 1), paso = total > 24 ? 12 : 22, H = Math.max(total * paso + 30, 160), niveles = ns.length;
  var xs = [30].concat(ns.map(function(x, i){ return 30 + (i + 1) * (niveles === 3 ? 170 : 230); }));
  var s = '<svg class="geo-svg" viewBox="0 0 640 ' + H + '" role="img" aria-label="' + T("Tree with " + total + " outcomes: " + ns.join(" times ") + ".", "Árbol de " + total + " combinaciones: " + ns.join(" por ") + ".") + '">';
  function nodo(nivel, y0, y1, ruta){
    var y = (y0 + y1) / 2;
    if (nivel === niveles){ if (total <= 24) s += textoA([xs[nivel] + 10, y], ruta.join(" · "), 13, "#424242", 400, "start"); return; }
    var n = ns[nivel], h = (y1 - y0) / n;
    for (var i = 0; i < n; i++){
      var yc = y0 + h * i + h / 2, nombre = OPCIONES[nivel][i];
      s += lineaG([xs[nivel], y], [xs[nivel + 1], yc], COL_AR[nivel], 2) + '<circle cx="' + xs[nivel + 1] + '" cy="' + f1(yc) + '" r="4" fill="#424242"/>';
      if (nivel < niveles - 1 || total <= 12) s += textoA([xs[nivel + 1] - 6, yc - 9], nombre, 13, COL_AR[nivel], 700, "end");
      nodo(nivel + 1, y0 + h * i, y0 + h * (i + 1), ruta.concat([nombre]));
    }
  }
  s += '<circle cx="30" cy="' + f1(H / 2) + '" r="6" fill="#424242"/>';
  nodo(0, 10, H - 10, []);
  $("ar-svg").innerHTML = s + "</svg>";
  $("ar-salida").innerHTML = '<div class="linea">' + T("Each dish opens into " + ns[1] + " drinks" + (niveles === 3 ? ", and each drink into " + ns[2] + " desserts" : "") + ".", "Cada plato se abre en " + ns[1] + " bebidas" + (niveles === 3 ? ", y cada bebida en " + ns[2] + " postres" : "") + ".") + "</div>" +
    '<div class="linea veredicto">' + T("Total: ", "Total: ") + ns.join(" × ") + " = " + total + T(" different meals.", " combinaciones distintas.") + "</div>";
}
function genConteo(){
  var tp = aleatorio(1, 5), enun, res, sol, pistas = [];
  if (tp === 1){ var a = aleatorio(3, 8), b = aleatorio(2, 6), c = aleatorio(2, 4); res = a * b * c; enun = T("You have " + a + " shirts, " + b + " pairs of pants, and " + c + " pairs of shoes. How many different outfits can you make?", "Usted tiene " + a + " camisas, " + b + " pantalones y " + c + " pares de zapatos. ¿Cuántos conjuntos distintos puede formar?"); sol = a + " × " + b + " × " + c + " = " + res + "."; pistas.push({v: a + b + c, msg: T("Multiply the choices for each decision; do not add them.", "Las opciones de cada decisión se multiplican, no se suman.")}); }
  else if (tp === 2){ var n = aleatorio(4, 10); res = Math.pow(2, n); enun = T("A test has " + n + " true-or-false questions. In how many different ways can it be answered?", "Un examen tiene " + n + " preguntas de verdadero o falso. ¿De cuántas formas distintas se puede contestar?"); sol = T("Each question has 2 choices: 2 multiplied " + n + " times = 2<sup>" + n + "</sup> = " + com(res) + ".", "Cada pregunta tiene 2 opciones: 2 multiplicado " + n + " veces = 2<sup>" + n + "</sup> = " + com(res) + "."); pistas.push({v: 2 * n, msg: T("There are " + n + " decisions with 2 choices each: multiply 2 × 2 × … (" + n + " times), not 2 × " + n + ".", "Son " + n + " decisiones de 2 opciones cada una: se multiplica 2 × 2 × … (" + n + " veces), no 2 × " + n + ".")}); }
  else if (tp === 3){ var d = aleatorio(3, 5); res = Math.pow(10, d); enun = T("A code has " + d + " digits, and digits can repeat. How many different codes are there?", "Una clave tiene " + d + " dígitos y se pueden repetir. ¿Cuántas claves distintas hay?"); sol = T("10 choices for each digit: 10<sup>" + d + "</sup> = " + com(res) + ".", "10 opciones para cada dígito: 10<sup>" + d + "</sup> = " + com(res) + "."); pistas.push({v: 10 * d, msg: T("There are " + d + " decisions with 10 choices each: multiply 10 × 10 × …", "Son " + d + " decisiones de 10 opciones: se multiplica 10 × 10 × …")}, {v: perm(10, d), msg: T("That would be the answer if digits could not repeat. Here they can: 10 choices each time.", "Así sería si los dígitos no se pudieran repetir. Aquí sí se repiten: 10 opciones cada vez.")}); }
  else if (tp === 4){ res = 26 * 26 * 10 * 10; enun = T("A license plate has 2 letters (out of 26) followed by 2 digits (0 to 9), and they can repeat. How many different plates are there?", "Una placa tiene 2 letras (de 26) seguidas de 2 dígitos (de 0 a 9), y se pueden repetir. ¿Cuántas placas distintas hay?"); sol = "26 × 26 × 10 × 10 = " + com(res) + "."; pistas.push({v: 26 + 26 + 10 + 10, msg: T("Multiply the choices; do not add them.", "Las opciones se multiplican, no se suman.")}); }
  else { var p = aleatorio(2, 5), q = aleatorio(2, 5), r = aleatorio(2, 4); res = p * q * r; enun = T("A restaurant has " + p + " appetizers, " + q + " main dishes, and " + r + " desserts. How many different three-course meals can you order?", "Un restaurante ofrece " + p + " entradas, " + q + " platos fuertes y " + r + " postres. ¿Cuántas comidas distintas de tres tiempos se pueden pedir?"); sol = p + " × " + q + " × " + r + " = " + res + "."; pistas.push({v: p + q + r, msg: T("Multiply the choices for each course.", "Las opciones de cada tiempo se multiplican.")}); }
  return {enun: enun, solucion: sol, evalua: function(v){ return evaluaEntero(v, res, pistas, T("Multiply the number of choices for each decision.", "Multiplique el número de opciones de cada decisión.")); }};
}

/* MODULE 2 · Factorial */
function pintaFC(){
  var n = +$("fc-n").value, k = +$("fc-k").value;
  if (k > n){ k = n; $("fc-k").value = n; }
  $("fc-nv").textContent = n; $("fc-kv").textContent = k;
  var exp = n === 0 ? T("1 (by agreement)", "1 (por convención)") : factores(n, n);
  var h = '<div class="linea grande">' + n + "! = " + exp + " = " + com(fact(n)) + "</div>";
  var arriba = n === 0 ? "1" : Array.from({length: n}, function(_, i){ var v = n - i; return v <= k ? '<span class="tok cancelado">' + v + "</span>" : v; }).join(" × ");
  var abajo = k === 0 ? "1" : Array.from({length: k}, function(_, i){ return '<span class="tok cancelado">' + (k - i) + "</span>"; }).join(" × ");
  var res = fact(n) / fact(k);
  h += '<div class="linea">' + T("To find " + n + "! ÷ " + k + "!, cross out the common factors:", "Para calcular " + n + "! ÷ " + k + "! se tachan los factores comunes:") + "</div>";
  h += '<div class="fraccion-grande" aria-hidden="true"><span class="frac"><span class="arriba">' + arriba + '</span><span class="abajo">' + abajo + "</span></span> = " + (n > k ? factores(n, n - k) + " = " : "") + com(res) + "</div>";
  h += '<p class="sr-only">' + T(n + " factorial divided by " + k + " factorial equals " + res + ".", n + " factorial entre " + k + " factorial es igual a " + res + ".") + "</p>";
  $("fc-salida").innerHTML = h;
}
function genFactorial(){
  var tp = aleatorio(1, 4), enun, res, sol, pistas = [];
  if (tp === 1){ var n = aleatorio(3, 7); res = fact(n); enun = T("What is " + n + "!?", "¿Cuánto es " + n + "!?"); sol = factores(n, n) + " = " + com(res) + "."; pistas.push({v: n * (n - 1), msg: T("The factorial multiplies all the whole numbers from " + n + " down to 1.", "El factorial multiplica todos los enteros desde " + n + " hasta 1.")}, {v: n * (n + 1) / 2, msg: T("You added. The factorial multiplies.", "Sumó. El factorial multiplica.")}); }
  else if (tp === 2){ var m = aleatorio(6, 12), k = m - aleatorio(2, 3); res = fact(m) / fact(k); enun = T("What is " + m + "! ÷ " + k + "!?", "¿Cuánto es " + m + "! ÷ " + k + "!?"); sol = T("The factors of " + k + "! cancel, and " + factores(m, m - k) + " = " + com(res) + " is left.", "Se cancelan los factores de " + k + "! y quedan " + factores(m, m - k) + " = " + com(res) + "."); pistas.push({v: fact(m - k), msg: T("Do not subtract inside the factorial: " + m + "! ÷ " + k + "! is not (" + m + " − " + k + ")!.", "No se restan los números dentro del factorial: " + m + "! ÷ " + k + "! no es (" + m + " − " + k + ")!.")}); }
  else if (tp === 3){ res = 1; enun = T("What is 0!?", "¿Cuánto es 0!?"); sol = T("By agreement, 0! = 1.", "Por convención, 0! = 1."); pistas.push({v: 0, msg: T("By agreement, 0! is 1, not 0.", "Por convención, 0! vale 1, no 0.")}); }
  else { var a = aleatorio(4, 7), b = aleatorio(1, a - 1); res = fact(a) / (fact(b) * fact(a - b)); enun = T("What is " + a + "! ÷ (" + b + "! × " + (a - b) + "!)?", "¿Cuánto es " + a + "! ÷ (" + b + "! × " + (a - b) + "!)?"); sol = com(fact(a)) + " ÷ (" + fact(b) + " × " + fact(a - b) + ") = " + com(res) + "."; pistas.push({v: fact(a) / fact(b), msg: T("Divide by both factorials in the parentheses.", "Hay que dividir entre los dos factoriales del paréntesis.")}); }
  return {enun: enun, solucion: sol, evalua: function(v){ return evaluaEntero(v, res, pistas, T("Write out the factors and cancel the common ones before multiplying.", "Escriba los factores y cancele los comunes antes de multiplicar.")); }};
}

/* MODULE 3 · Permutations */
function pintaPM(){
  var n = +$("pm-n").value, r = +$("pm-r").value; if (r > n){ r = n; $("pm-r").value = n; }
  $("pm-nv").textContent = n; $("pm-rv").textContent = r;
  var h = "";
  for (var i = 0; i < r; i++) h += '<div class="slot"><strong>' + (n - i) + "</strong><span>" + T(["1st", "2nd", "3rd"][i] || (i + 1) + "th", (i + 1) + ".º") + T(" place", " lugar") + "</span></div>";
  $("pm-slots").innerHTML = h;
  var P = perm(n, r), f = factores(n, r);
  var s = '<div class="linea">' + T("Choices for each place: ", "Opciones por lugar: ") + f + '.</div><div class="linea veredicto">P(' + n + ", " + r + ") = " + f + " = " + com(P) + T(" arrangements", " ordenamientos") + "</div>";
  s += '<div class="linea">' + T("With the formula: ", "Con la fórmula: ") + n + "! ÷ (" + n + " − " + r + ")! = " + com(fact(n)) + " ÷ " + com(fact(n - r)) + " = " + com(P) + ".</div>";
  if (P <= 60) s += '<p class="nota">' + T("All the arrangements with the people ", "Todos los ordenamientos con las personas ") + LETRAS.slice(0, n).join(", ") + ':</p><div class="arreglos">' + permutaciones(LETRAS.slice(0, n), r).map(function(p){ return "<span>" + p.join("") + "</span>"; }).join("") + "</div>";
  $("pm-salida").innerHTML = s;
}
function genPermutacion(){
  var tp = aleatorio(1, 4), n, r, enun;
  if (tp === 1){ n = aleatorio(5, 10); r = 3; enun = T("There are " + n + " runners in a race. In how many ways can 1st, 2nd, and 3rd place be given out?", "En una carrera hay " + n + " corredores. ¿De cuántas formas se pueden repartir el 1.º, 2.º y 3.º lugar?"); }
  else if (tp === 2){ n = aleatorio(6, 12); r = 3; enun = T("A club of " + n + " people chooses a president, a secretary, and a treasurer (different jobs). In how many ways can it do this?", "Un club de " + n + " personas elige presidente, secretario y tesorero (cargos distintos). ¿De cuántas formas puede hacerlo?"); }
  else if (tp === 3){ n = aleatorio(4, 7); r = n; enun = T("In how many ways can " + n + " different books be arranged on a shelf?", "¿De cuántas formas se pueden ordenar " + n + " libros distintos en un estante?"); }
  else { n = 10; r = aleatorio(3, 4); enun = T("A " + r + "-digit code cannot repeat any digit. How many different codes are there?", "Una clave de " + r + " dígitos no puede repetir ningún dígito. ¿Cuántas claves distintas hay?"); }
  var res = perm(n, r), pistas = [{v: comb(n, r), msg: T("That would be the combination. Here order matters: each different order counts.", "Esa sería la combinación. Aquí el orden importa: cada orden distinto cuenta.")}, {v: Math.pow(n, r), msg: T("That would be the answer with repeats. Without repeats, each place has one choice fewer than the one before.", "Así sería si se pudiera repetir. Sin repetir, cada lugar tiene una opción menos que el anterior.")}, {v: n * r, msg: T("Do not multiply n by r: multiply the choices for each place, which go down by one each time.", "No se multiplica n por r: se multiplican las opciones de cada lugar, que van bajando de uno en uno.")}];
  return {enun: enun, solucion: T("Order matters: P(", "El orden importa: P(") + n + ", " + r + ") = " + factores(n, r) + " = " + com(res) + ".",
    evalua: function(v){ return evaluaEntero(v, res, pistas, T("Count the choices for each place: " + n + ", then " + (n - 1) + ", and so on.", "Cuente las opciones de cada lugar: " + n + ", después " + (n - 1) + ", y así.")); }};
}

/* MODULE 4 · Combinations */
function pintaCB(){
  var n = +$("cb-n").value, r = +$("cb-r").value; if (r > n){ r = n; $("cb-r").value = n; }
  $("cb-nv").textContent = n; $("cb-rv").textContent = r;
  var P = perm(n, r), C = comb(n, r);
  $("cb-salida").innerHTML = '<div class="linea">' + T("If order mattered, there would be P(" + n + ", " + r + ") = " + com(P) + " arrangements.", "Si importara el orden habría P(" + n + ", " + r + ") = " + com(P) + " ordenamientos.") + "</div>" +
    '<div class="linea">' + T("But each group of " + r + " shows up " + r + "! = " + fact(r) + (fact(r) === 1 ? " time" : " times") + " (once for each order).", "Pero cada grupo de " + r + " aparece " + r + "! = " + fact(r) + (fact(r) === 1 ? " vez" : " veces") + " (una por cada orden).") + "</div>" +
    '<div class="linea veredicto">C(' + n + ", " + r + ") = " + com(P) + " ÷ " + fact(r) + " = " + com(C) + T(" groups", " grupos") + "</div>";
  var lista = combinaciones(LETRAS.slice(0, n), r);
  $("cb-lista").innerHTML = P <= 120 ? '<p class="nota">' + T("Each row is one group with all its orders:", "Cada fila es un grupo con todos sus órdenes:") + "</p>" + lista.map(function(g){ return '<div class="arreglos"><span class="grupo">{' + g.join(", ") + "}</span>" + permutaciones(g, r).map(function(p){ return "<span>" + p.join("") + "</span>"; }).join("") + "</div>"; }).join("") : '<p class="nota">' + T("There are too many to show them all.", "Son demasiados para mostrarlos todos.") + "</p>";
}
function genCombinacion(){
  var tp = aleatorio(1, 4), n, r, enun;
  if (tp === 1){ n = aleatorio(6, 12); r = 3; enun = T("From a group of " + n + " people, a committee of 3 is chosen (no titles). How many different committees can be formed?", "De un grupo de " + n + " personas se elige un comité de 3 (sin cargos). ¿Cuántos comités distintos se pueden formar?"); }
  else if (tp === 2){ n = aleatorio(6, 10); r = 2; enun = T("A pizza place offers " + n + " toppings, and you choose 2. How many different two-topping pizzas are there?", "Una pizzería ofrece " + n + " ingredientes y se eligen 2. ¿Cuántas pizzas distintas de dos ingredientes hay?"); }
  else if (tp === 3){ n = aleatorio(8, 12); r = elige([4, 5]); enun = T("A coach chooses " + r + " players out of " + n + " for a team. How many different teams can the coach make?", "Un entrenador elige " + r + " jugadores de " + n + " para un equipo. ¿Cuántos equipos distintos puede formar?"); }
  else { n = aleatorio(5, 8); r = 2; enun = T("At a meeting there are " + n + " people, and each one shakes hands with every other person once. How many handshakes are there?", "En una reunión hay " + n + " personas y cada una saluda a todas las demás una vez con un apretón de manos. ¿Cuántos apretones hay?"); }
  var res = comb(n, r), pistas = [{v: perm(n, r), msg: T("That is the permutation. In a group, order does not matter: divide by " + r + "! = " + fact(r) + ".", "Esa es la permutación. En un grupo el orden no importa: hay que dividir entre " + r + "! = " + fact(r) + ".")}];
  return {enun: enun, solucion: T("Order does not matter: C(", "El orden no importa: C(") + n + ", " + r + ") = P(" + n + ", " + r + ") ÷ " + r + "! = " + com(perm(n, r)) + " ÷ " + fact(r) + " = " + com(res) + ".",
    evalua: function(v){ return evaluaEntero(v, res, pistas, T("Find P(" + n + ", " + r + ") and divide by " + r + "!.", "Calcule P(" + n + ", " + r + ") y divida entre " + r + "!.")); }};
}

/* MODULE 5 · Deciding */
var SITUACIONES = [
  [T("Choosing a committee of 3 people from a group of 10.", "Elegir un comité de 3 personas de un grupo de 10."), "c", T("In a committee everyone has the same role: order does not matter.", "En un comité todos tienen el mismo papel: el orden no importa.")],
  [T("Giving 1st, 2nd, and 3rd place to 3 of 8 runners.", "Repartir 1.º, 2.º y 3.º lugar entre 8 corredores."), "p", T("Finishing first is not the same as finishing third: order matters.", "No es lo mismo llegar primero que tercero: el orden importa.")],
  [T("Putting together an outfit with a shirt, a pair of pants, and a pair of shoes.", "Formar un conjunto con una camisa, un pantalón y unos zapatos."), "f", T("These are decisions of different kinds: multiply the choices for each one.", "Son decisiones de tipos distintos: se multiplican las opciones de cada una.")],
  [T("Choosing a president and a vice president of a club of 15 people.", "Elegir presidente y vicepresidente de un club de 15 personas."), "p", T("The jobs are different: order matters.", "Los cargos son distintos: el orden importa.")],
  [T("Picking 2 ice cream flavors out of 12 for a cup.", "Escoger 2 sabores de helado de 12 para una copa."), "c", T("Chocolate and vanilla is the same cup as vanilla and chocolate.", "Chocolate y vainilla es la misma copa que vainilla y chocolate.")],
  [T("Making a 4-digit code whose digits can repeat.", "Crear una clave de 4 dígitos que se pueden repetir."), "f", T("Each digit is a decision with 10 choices, and they can repeat: the counting principle.", "Cada dígito es una decisión con 10 opciones, y se pueden repetir: principio del conteo.")],
  [T("Arranging 5 photos in a row on the wall.", "Ordenar 5 fotos en una fila en la pared."), "p", T("Changing the order of the photos gives a different row.", "Cambiar el orden de las fotos da otra fila distinta.")],
  [T("Choosing 5 cards from a deck to make a hand.", "Elegir 5 cartas de una baraja para formar una mano."), "c", T("A hand is the same no matter the order in which the cards came.", "Una mano es la misma sin importar el orden en que llegaron las cartas.")],
  [T("Ordering an appetizer, a main dish, and a dessert from a menu.", "Pedir una entrada, un plato fuerte y un postre de un menú."), "f", T("Three decisions of different kinds: multiply.", "Tres decisiones de tipos distintos: se multiplican.")],
  [T("Choosing 4 books out of 9 to take on a trip.", "Elegir 4 libros de 9 para llevar de viaje."), "c", T("You take the same books no matter the order in which you pick them.", "Se llevan los mismos libros sin importar el orden en que se escojan.")],
  [T("Giving 3 different shifts (morning, afternoon, and night) to 3 of 7 workers.", "Asignar 3 turnos distintos (mañana, tarde y noche) a 3 de 7 empleados."), "p", T("Each shift is different: order matters.", "Cada turno es distinto: el orden importa.")]];
function genDecidir(){
  var s = elige(SITUACIONES);
  return {enun: s[0] + T(" Which tool do you use?", " ¿Qué herramienta se usa?"), opciones: [{html: T("Permutation (order matters)", "Permutación (el orden importa)"), clave: "p"}, {html: T("Combination (order does not matter)", "Combinación (el orden no importa)"), clave: "c"}, {html: T("Counting principle (different decisions)", "Principio del conteo (decisiones distintas)"), clave: "f"}],
    correcta: s[1], porClave: {}, pista: T("Are the choices from the same group? If so, does the result change if you change the order?", "¿Las elecciones salen del mismo grupo? Si es así, ¿cambia el resultado si se cambia el orden?"), bien: s[2], mal: s[2]};
}

/* Start */
["ar-a", "ar-b", "ar-c"].forEach(function(id){ $(id).addEventListener("input", pintaArbol); }); pintaArbol();
creaPracticaLibre("p1", genConteo);
["fc-n", "fc-k"].forEach(function(id){ $(id).addEventListener("input", pintaFC); }); pintaFC();
creaPracticaLibre("p2", genFactorial);
["pm-n", "pm-r"].forEach(function(id){ $(id).addEventListener("input", pintaPM); }); pintaPM();
creaPracticaLibre("p3", genPermutacion);
["cb-n", "cb-r"].forEach(function(id){ $(id).addEventListener("input", pintaCB); }); pintaCB();
creaPracticaLibre("p4", genCombinacion);
OMR("p5", genDecidir);
'''

def practica_pagina():
    n = N
    def libre(pid, tit, et, nota):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota}</p>\n        <div class="fila-btn">', 1)
    def rango(i, et, v, mn, mx, mw=170):
        return f'<div class="campo" style="flex:1;min-width:{mw}px;"><label for="{i}">{et} <span id="{i}v"></span></label><input type="range" id="{i}" min="{mn}" max="{mx}" value="{v}"></div>'
    entero = t("Type a whole number.", "Escriba un número entero.")
    mods = [
     (t("counting", "conteo"), t("The counting principle", "El principio fundamental del conteo"),
      f'''      <p>{t("If one decision can be made in m ways and another in n ways, the two together can be made in m × n ways. With more decisions, keep multiplying the choices for each one.", "Si una decisión se puede tomar de m formas y otra de n formas, las dos juntas se pueden tomar de m × n formas. Con más decisiones, se siguen multiplicando las opciones de cada una.")}</p>
      <h3>{t("The growing tree", "El árbol que crece")}</h3>
      <p>{t("Put together a menu. Each branch of the tree is a choice; the leaves at the end are all the possible meals.", "Arme un menú. Cada rama del árbol es una elección; las hojas del final son todas las combinaciones posibles.")}</p>
      <div class="panel"><div class="campos">
        {rango("ar-a", t("Main dishes:", "Platos principales:"), 2, 1, 4)}
        {rango("ar-b", t("Drinks:", "Bebidas:"), 3, 1, 4)}
        {rango("ar-c", t("Desserts:", "Postres:"), 0, 0, 3)}</div></div>
      <div id="ar-svg"></div>
{n3.salida("ar-salida")}
{libre("p1", t("Practice: how many possibilities are there?", "Practique: ¿cuántas posibilidades hay?"), "Total", entero)}'''),
     ("factorial", t("The factorial", "El factorial"),
      f'''      <p>{t("The factorial of a number, n!, is the product of all the whole numbers from n down to 1. By agreement, 0! = 1. It grows very fast, so simplify quotients before you multiply.", "El factorial de un número, n!, es el producto de todos los enteros desde n hasta 1. Por convención, 0! = 1. Crece muy rápido: por eso conviene simplificar los cocientes antes de multiplicar.")}</p>
{n3.formula("n! = n × (n − 1) × … × 2 × 1")}
      <h3>{t("Factorial explorer", "Explorador de factoriales")}</h3>
      <div class="panel"><div class="campos">
        {rango("fc-n", "n:", 5, 0, 10)}
        {rango("fc-k", t("Divide by k! with k =", "Dividir entre k! con k ="), 3, 0, 10)}</div></div>
{n3.salida("fc-salida")}
{libre("p2", t("Practice: calculate", "Practique: calcule"), t("Result", "Resultado"), t("Type a whole number. Simplify before you multiply.", "Escriba un número entero. Simplifique antes de multiplicar."))}'''),
     (t("permutations", "permutaciones"), t("Permutations: order matters", "Permutaciones: el orden importa"),
      f'''      <p>{t("A <strong>permutation</strong> counts how many ways you can put in order r items chosen from n. Use it when the order changes the result: a podium, a code, an order of arrival.", "Una <strong>permutación</strong> cuenta de cuántas formas se pueden ordenar r elementos elegidos de n. Sirve cuando el orden cambia el resultado: un podio, una clave, un orden de llegada.")}</p>
{n3.formula('P(n, r) = <span class="fracc"><span class="fa">n!</span><span class="fb2">(n − r)!</span></span> = n × (n − 1) × … ' + t("(r factors)", "(r factores)"))}
      <h3>{t("Filling the places", "Los lugares que se llenan")}</h3>
      <p>{t("There are n people and r places. Anyone can go in the first place; in the second, one person fewer; and so on.", "Hay n personas y r lugares. En el primer lugar se puede poner a cualquiera; en el segundo, a una menos; y así.")}</p>
      <div class="panel"><div class="campos">
        {rango("pm-n", t("People (n):", "Personas (n):"), 5, 2, 8)}
        {rango("pm-r", t("Places (r):", "Lugares (r):"), 3, 1, 8)}</div>
        <div class="slots" id="pm-slots" aria-hidden="true"></div></div>
{n3.salida("pm-salida")}
{libre("p3", t("Practice: permutations", "Practique: permutaciones"), "Total", entero)}'''),
     (t("combinations", "combinaciones"), t("Combinations: order does not matter", "Combinaciones: el orden no importa"),
      f'''      <p>{t("A <strong>combination</strong> counts how many ways you can choose a group when order does not matter: a committee, a team, a hand of cards. It is the permutation divided by r!, because each group shows up r! times among the permutations, once for each order.", "Una <strong>combinación</strong> cuenta de cuántas formas se puede elegir un grupo, sin importar el orden: un comité, un equipo, una mano de cartas. Se calcula como la permutación dividida entre r!, porque cada grupo aparece r! veces en las permutaciones, una por cada orden.")}</p>
{n3.formula('C(n, r) = <span class="fracc"><span class="fa">n!</span><span class="fb2">r! (n − r)!</span></span> = <span class="fracc"><span class="fa">P(n, r)</span><span class="fb2">r!</span></span>')}
      <h3>{t("From order to group", "Del orden al grupo")}</h3>
      <p>{t("With small numbers you can see them all: each row is the different orders of one group.", "Con números pequeños se pueden ver todas: cada fila son los órdenes distintos de un mismo grupo.")}</p>
      <div class="panel"><div class="campos">
        {rango("cb-n", t("Items (n):", "Elementos (n):"), 4, 2, 6)}
        {rango("cb-r", t("Chosen (r):", "Se eligen (r):"), 2, 1, 4)}</div></div>
{n3.salida("cb-salida")}
      <div id="cb-lista"></div>
{libre("p4", t("Practice: combinations", "Practique: combinaciones"), "Total", entero)}'''),
     (t("decide", "decidir"), t("Does order matter?", "¿Importa el orden?"),
      f'''      <p>{t("Before you calculate, ask yourself: “If I change the order, does the result change?”", "Antes de calcular, pregúntese: «si cambio el orden, ¿cambia el resultado?»")}</p>
      <table class="reglas"><caption>{t("How to decide which tool to use", "Cómo decidir qué herramienta usar")}</caption>
        <thead><tr><th scope="col">{t("Situation", "Situación")}</th><th scope="col">{t("Tool", "Herramienta")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead>
        <tbody><tr><td>{t("Decisions of different kinds", "Decisiones de tipos distintos")}</td><td>{t("Counting principle", "Principio del conteo")}</td><td>{t("dish, drink, and dessert", "plato, bebida y postre")}</td></tr>
        <tr><td>{t("From the same group, and order matters", "Del mismo grupo, y el orden importa")}</td><td>{t("Permutation", "Permutación")}</td><td>{t("president, secretary, and treasurer", "presidente, secretario y tesorero")}</td></tr>
        <tr><td>{t("From the same group, and order does not matter", "Del mismo grupo, y el orden no importa")}</td><td>{t("Combination", "Combinación")}</td><td>{t("a committee of 3", "un comité de 3")}</td></tr></tbody></table>
{B.om("p5", t("Practice: which tool would you use?", "Practique: ¿qué herramienta usaría?"))}''')]
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Principio fundamental del conteo, permutaciones y combinaciones")
