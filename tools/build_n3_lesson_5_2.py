"""Level 3 · Lesson 5.2 · Inequalities that need simplifying, and word problems — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "5-2"
TEMA = ("Inequalities and formulas", "Inecuaciones y fórmulas")
TIT = ("Inequalities that need simplifying, and word problems", "Inecuaciones que requieren simplificación y problemas verbales")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js")

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 5.1 you solved simple inequalities and graphed their solutions. This lesson adds two layers. First, inequalities that, like the equations of Topic 4, need simplifying before you solve: distribute, combine like terms, and move variables. Second, word problems: translate a real situation into an inequality and explain what the solution means.",
"En la Lección 5.1 se resolvieron inecuaciones sencillas y se graficó su solución. Esta lección añade dos capas. Primero, inecuaciones que —igual que las ecuaciones del Tema 4— requieren simplificar antes de resolver: distribuir, combinar términos semejantes y mover variables. Segundo, los problemas verbales: traducir un enunciado real a una inecuación e interpretar qué significa la solución.")}</p>
<p>{t("When an inequality has parentheses or repeated terms, first simplify it with the usual algebra tools, then solve it. The sign rule still holds if you divide by a negative number.", "Cuando una inecuación tiene paréntesis o términos repetidos, primero se simplifica con las mismas herramientas del álgebra, y después se resuelve. La regla del cambio de signo sigue vigente si se divide por un negativo.")}</p>
{ejemplo(t("Example 1: solve 2(x + 3) &gt; 10", "Ejemplo 1: resuelva 2(x + 3) &gt; 10"),
  [("1", t("Distribute.", "Distribuir."), "2x + 6 &gt; 10."),
   ("2", t("Subtract 6.", "Restar 6."), "2x &gt; 4."),
   ("3", t("Divide by 2.", "Dividir entre 2."), t("2 is positive, so the sign does not flip: x > 2.", "2 es positivo, así que el signo no se invierte: x > 2.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>x &gt; 2</strong>")])}
{ejemplo(t("Example 2: solve 5x − 3 &gt; 2x + 9", "Ejemplo 2: resuelva 5x − 3 &gt; 2x + 9"),
  [("1", t("Subtract 2x from both sides.", "Restar 2x en ambos lados."), "3x − 3 &gt; 9."),
   ("2", t("Add 3.", "Sumar 3."), "3x &gt; 12."),
   ("3", t("Divide by 3.", "Dividir entre 3."), "x &gt; 4."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x &gt; 4</strong>")])}
{caja("ojo", t("Do not forget the sign rule", "No olvide la regla del signo"), t("<p>If after simplifying you must divide by a negative number (for example, in −2(x − 1) ≥ 8), the inequality sign flips, just as in Lesson 5.1.</p>", "<p>Si tras simplificar hay que dividir por un negativo (por ejemplo, en −2(x − 1) ≥ 8), el signo de la desigualdad se invierte, igual que en la Lección 5.1.</p>"))}
{enlace(n, t("simplify", "simplificar"), t("inequalities that need simplifying", "inecuaciones que requieren simplificar"), t("Distribute and combine terms before you solve.", "Distribuya y combine términos antes de despejar."))}'''

    s2 = f'''<p>{t("To translate a sentence, certain words always point to the same inequality sign.", "Para traducir un enunciado, ciertas palabras señalan siempre el mismo signo de desigualdad.")}</p>
{tabla(t("Inequality words", "Vocabulario de las inecuaciones"), t("Words in a sentence and their inequality sign", "Vocabulario verbal y su signo de desigualdad correspondiente"), [t("Phrase", "Frase verbal"), t("Sign", "Signo")],
  [[t("at least · a minimum of · no less than", "al menos · mínimo · no menos de"), "≥"], [t("no more than · at most · a maximum of · does not exceed", "no más de · como máximo · máximo · no excede"), "≤"],
   [t("more than · greater than", "más que · mayor que"), "&gt;"], [t("less than · fewer than", "menos que · menor que"), "&lt;"]])}
{caja("tip", t("“At least” and “at most” include the boundary", "«Al menos» y «como máximo» incluyen el límite"), t("<p>“At least 10” means 10 or more (≥ 10), and it includes 10. “At most 10” means 10 or less (≤ 10), and it includes 10. That is why they use the signs with the little bar (≤, ≥) and a closed point on the graph.</p>", "<p>«Al menos 10» significa 10 o más (≥ 10), e incluye el 10. «Como máximo 10» significa 10 o menos (≤ 10), e incluye el 10. Por eso usan los signos con la rayita (≤, ≥) y un punto cerrado al graficar.</p>"))}
{practica("p1", t("Practice 1 — At least", "Práctica 1 — Al menos"), t("“A number x is at least 8”", "«Un número x es al menos 8»"), [("a", "x ≥ 8"), ("b", "x ≤ 8"), ("c", "x &gt; 8")])}
{practica("p2", t("Practice 2 — No more than", "Práctica 2 — No más de"), t("“A number x is no more than 15”", "«Un número x no es más de 15»"), [("a", "x ≥ 15"), ("b", "x ≤ 15"), ("c", "x &lt; 15")])}
{practica("p3", t("Practice 3 — More than", "Práctica 3 — Más que"), t("“A number x is more than 3”", "«Un número x es más que 3»"), [("a", "x ≥ 3"), ("b", "x &lt; 3"), ("c", "x &gt; 3")])}
{enlace(n, t("vocabulary", "vocabulario"), t("the language of inequalities", "el vocabulario de las inecuaciones"), t("Translate “at least,” “no more than,” and other phrases into the right symbol.", "Traduzca «al menos», «no más de» y otras expresiones al símbolo correcto."))}'''

    s3 = f'''<p>{t("To solve a word problem: identify the variable, translate the sentence into an inequality with the key words, and solve it.", "Para resolver un problema verbal: se identifica la variable, se traduce el enunciado a una inecuación usando el vocabulario y se resuelve.")}</p>
{ejemplo(t("Example 3: “A number increased by 5 is at least 12.”", "Ejemplo 3: «Un número aumentado en 5 es al menos 12.»"),
  [("1", t("Translate.", "Traducir."), t("“Increased by 5” is x + 5; “at least 12” is ≥ 12. You get x + 5 ≥ 12.", "«Aumentado en 5» es x + 5; «al menos 12» es ≥ 12. Queda x + 5 ≥ 12.")),
   ("2", t("Subtract 5.", "Restar 5."), "x ≥ 7."),
   ("✓", t("Answer.", "Respuesta."), t("The number must be <strong>7 or greater</strong>.", "El número debe ser <strong>7 o mayor</strong>."))])}
{ejemplo(t("Example 4: “Twice a number does not exceed 14.”", "Ejemplo 4: «El doble de un número no excede 14.»"),
  [("1", t("Translate.", "Traducir."), t("“Twice” is 2x; “does not exceed 14” is ≤ 14. You get 2x ≤ 14.", "«El doble» es 2x; «no excede 14» es ≤ 14. Queda 2x ≤ 14.")),
   ("2", t("Divide by 2.", "Dividir entre 2."), "x ≤ 7."),
   ("✓", t("Answer.", "Respuesta."), t("The number must be <strong>7 or less</strong>.", "El número debe ser <strong>7 o menor</strong>."))])}'''

    s4 = f'''<p>{t("Inequalities model real-life limits: a budget you cannot go over, a minimum number of hours you must work, a maximum number of items you can buy.", "Las inecuaciones modelan límites de la vida real: un presupuesto que no se puede superar, un mínimo de horas que hay que cumplir, un máximo de artículos que se pueden comprar.")}</p>
{ejemplo(t("Example 5: a budget", "Ejemplo 5: presupuesto"),
  [("1", t("The situation.", "La situación."), t("You have at most $50. You already spent $30. How much more (x) can you spend? The total cannot exceed 50: 30 + x ≤ 50.", "Se dispone de $50 como máximo. Ya se gastaron $30. ¿Cuánto más (x) se puede gastar? El gasto total no puede exceder 50: 30 + x ≤ 50.")),
   ("2", t("Subtract 30.", "Restar 30."), "x ≤ 20."),
   ("✓", t("Answer.", "Respuesta."), t("You can spend <strong>at most $20 more</strong>.", "Se puede gastar <strong>como máximo $20 más</strong>."))])}
{ejemplo(t("Example 6: time", "Ejemplo 6: tiempo"),
  [("1", t("The situation.", "La situación."), t("A project needs at least 24 hours. You already worked 9. How many more hours (x) do you need? The total must be at least 24: 9 + x ≥ 24.", "Un proyecto necesita al menos 24 horas. Ya se trabajaron 9. ¿Cuántas horas más (x) hacen falta? El total debe ser al menos 24: 9 + x ≥ 24.")),
   ("2", t("Subtract 9.", "Restar 9."), "x ≥ 15."),
   ("✓", t("Answer.", "Respuesta."), t("You need <strong>at least 15 more hours</strong>.", "Hacen falta <strong>al menos 15 horas más</strong>."))])}
{practica("p4", t("Practice 4 — Distribute first", "Práctica 4 — Distribuir primero"), t("Solve 4(x − 1) ≤ 12.", "Resuelva 4(x − 1) ≤ 12."), [("a", "x ≥ 4"), ("b", "x ≤ 4"), ("c", "x ≤ 3")])}
{practica("p5", t("Practice 5 — Both sides", "Práctica 5 — Ambos lados"), t("Solve 2x + 5 &gt; x + 9.", "Resuelva 2x + 5 &gt; x + 9."), [("a", "x &lt; 4"), ("b", "x &gt; 14"), ("c", "x &gt; 4")])}
{practica("p6", t("Practice 6 — A budget", "Práctica 6 — Presupuesto"), t("You have at most $40 and you already spent $25. How much more (x) can you spend?", "Se dispone de $40 como máximo y ya se gastaron $25. ¿Cuánto más (x) se puede gastar?"), [("a", "x ≤ 15"), ("b", "x ≥ 15"), ("c", "x ≤ 40")])}
{enlace(n, t("context", "contexto"), t("budget and time problems", "problemas de presupuesto y tiempo"), t("Set up, solve, and explain everyday inequalities.", "Plantee, resuelva e interprete inecuaciones de la vida diaria."))}'''

    s5 = f'''<p>{t("The last part of a word problem is to explain the solution in words, with units. The inequality gives a range; the situation tells you which value of that range is the “maximum” or the “minimum” you are looking for.", "La parte final de un problema verbal es interpretar la solución en palabras, con unidades. La inecuación da un rango; el contexto indica qué valor de ese rango es el «máximo» o el «mínimo» buscado.")}</p>
{ejemplo(t("Example 7: from the range to the limit", "Ejemplo 7: del rango al límite"),
  [("1", t("The range.", "El rango."), t("The solution of a shopping problem is x ≤ 6, where x is the number of items. The range includes 0, 1, 2, … up to 6.", "La solución de un problema de compras es x ≤ 6, donde x es el número de artículos. El rango incluye 0, 1, 2, … hasta 6.")),
   ("2", t("Whole items.", "Artículos enteros."), t("You do not buy parts of an item, so the greatest whole number possible is 6.", "Como no se compran fracciones de artículo, el máximo entero posible es 6.")),
   ("✓", t("Answer.", "Respuesta."), t("You can buy <strong>at most 6 items</strong>.", "Se pueden comprar <strong>como máximo 6 artículos</strong>."))])}
{caja("ojo", t("Answer in words", "Responder en palabras"), t("<p>A word problem does not end with “x ≤ 6.” It ends with a sentence like “you can buy at most 6 items.” Explaining the result in the situation is part of the answer. If the solution is x ≤ 6.4 items, the most is 6 (round down); if it is x ≥ 3.2 days, the least is 4 (round up), because 3 days are not enough.</p>", "<p>Un problema verbal no termina con «x ≤ 6». Termina con una oración como «se pueden comprar como máximo 6 artículos». Interpretar el resultado en el contexto es parte de la respuesta. Si la solución es x ≤ 6.4 artículos, el máximo es 6 (se redondea hacia abajo); si es x ≥ 3.2 días, el mínimo es 4 (se redondea hacia arriba), porque 3 días no alcanzan.</p>"))}'''

    secciones = [("s-" + t("simplify", "simplificar"), t("Inequalities that need simplifying", "Inecuaciones que requieren simplificar"), s1),
                 ("s-" + t("vocabulary", "vocabulario"), t("The language of inequalities", "El vocabulario de las inecuaciones"), s2),
                 ("s-" + t("translate", "traducir"), t("Translating and solving sentences", "Traducir y resolver enunciados"), s3),
                 ("s-" + t("context", "contexto"), t("Problems in context: budget and time", "Problemas de contexto: presupuesto y tiempo"), s4),
                 ("s-" + t("interpret", "interpretar"), t("Explaining the solution", "Interpretar la solución"), s5)]

    lesson = {"next": t("Lesson 5.3", "Lección 5.3"), "review": t("sections 1, 2, and 4", "las secciones 1, 2 y 4"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("“At least” means that number or more.", "«Al menos» quiere decir ese número o más."), "c": t("“At least 8” includes the 8.", "«Al menos 8» incluye el 8.")}, "right": t("“At least” is ≥ and includes the 8.", "«Al menos» es ≥ e incluye el 8."), "solution": "x ≥ 8."},
      "p2": {"ok": "b", "hints": {"a": t("“No more than” means that number or less.", "«No más de» quiere decir ese número o menos."), "c": t("“No more than 15” includes the 15.", "«No más de 15» incluye el 15.")}, "right": t("“No more than” is ≤ and includes the 15.", "«No más de» es ≤ e incluye el 15."), "solution": "x ≤ 15."},
      "p3": {"ok": "c", "hints": {"a": t("“More than 3” does not include the 3.", "«Más que 3» no incluye el 3."), "b": t("“More” points to the greater numbers.", "«Más» apunta a los números mayores.")}, "right": t("“More than” is > and does not include the 3.", "«Más que» es > y no incluye el 3."), "solution": "x > 3."},
      "p4": {"ok": "b", "hints": {"a": t("4 is positive: the sign does not flip.", "4 es positivo: el signo no se invierte."), "c": t("Distribute the 4 to the 1 too: 4x − 4 ≤ 12.", "Distribuya el 4 también al 1: 4x − 4 ≤ 12.")}, "right": "4x − 4 ≤ 12, 4x ≤ 16, x ≤ 4.", "solution": t("Distribute: 4x − 4 ≤ 12; add 4: 4x ≤ 16; divide by 4: x ≤ 4.", "Se distribuye: 4x − 4 ≤ 12; se suma 4: 4x ≤ 16; se divide entre 4: x ≤ 4.")},
      "p5": {"ok": "c", "hints": {"a": t("You never divided by a negative number: the sign stays.", "Nunca se dividió por un negativo: el signo se conserva."), "b": t("Subtract 5, do not add it: 9 − 5 = 4.", "Se resta 5, no se suma: 9 − 5 = 4.")}, "right": "x + 5 > 9, x > 4.", "solution": t("Subtract x: x + 5 > 9; subtract 5: x > 4.", "Se resta x: x + 5 > 9; se resta 5: x > 4.")},
      "p6": {"ok": "a", "hints": {"b": t("“At most” is ≤.", "«Como máximo» es ≤."), "c": t("You already spent $25 of the $40.", "Ya se gastaron $25 de los $40.")}, "right": "25 + x ≤ 40, x ≤ 15.", "solution": t("25 + x ≤ 40, so x ≤ 15: at most $15 more.", "25 + x ≤ 40, así que x ≤ 15: como máximo $15 más.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("Distribute: 2x + 6 > 10.", "Distribuya: 2x + 6 > 10."), "b": t("2 is positive: the sign does not flip.", "2 es positivo: el signo no se invierte."), "c": t("2x > 4: divide by 2.", "2x > 4: divida entre 2.")}, "solution": "2x + 6 > 10, 2x > 4, x > 2."},
      "B": {"ok": "b", "hints": {"a": t("2 is positive: the sign does not flip.", "2 es positivo: el signo no se invierte."), "c": t("2x ≤ 6: divide by 2.", "2x ≤ 6: divida entre 2."), "d": t("Subtract 2, do not add it.", "Se resta 2, no se suma.")}, "solution": "2x + 2 ≤ 8, 2x ≤ 6, x ≤ 3."},
      "C": {"ok": "a", "hints": {"b": t("The number is right, but you divide by −2: flip the sign.", "El número está bien, pero se divide entre −2: invierta el signo."), "c": t("6 ÷ (−2) = −3.", "6 ÷ (−2) = −3."), "d": t("6 ÷ (−2) = −3, and the sign flips.", "6 ÷ (−2) = −3, y el signo se invierte.")}, "solution": t("−2x + 2 ≥ 8, −2x ≥ 6, x ≤ −3 (the sign flips).", "−2x + 2 ≥ 8, −2x ≥ 6, x ≤ −3 (el signo se invierte).")},
      "D": {"ok": "c", "hints": {"a": t("“At least” means 10 or more.", "«Al menos» es 10 o más."), "b": t("“At least 10” includes the 10.", "«Al menos 10» incluye el 10."), "d": t("“At least” means 10 or more.", "«Al menos» es 10 o más.")}, "solution": "x ≥ 10."},
      "E": {"ok": "b", "hints": {"a": t("“Does not exceed” means 20 or less.", "«No excede» es 20 o menos."), "c": t("“Does not exceed 20” includes the 20.", "«No excede 20» incluye el 20."), "d": t("It is a range, not one value.", "Es un rango, no un solo valor.")}, "solution": "x ≤ 20."},
      "F": {"ok": "d", "hints": {"a": t("“More than” is >.", "«Más que» es >."), "b": t("“More than 14” does not include the 14.", "«Más que 14» no incluye el 14."), "c": t("“Twice” is 2x, not x + 2.", "«El doble» es 2x, no x + 2.")}, "solution": "2x > 14."},
      "G": {"ok": "c", "hints": {"a": t("“At most” is ≤.", "«Como máximo» es ≤."), "b": t("“At most 50” includes 20 more.", "«Como máximo 50» incluye 20 más."), "d": t("Subtract the $30 already spent.", "Reste los $30 ya gastados.")}, "solution": "30 + x ≤ 50, x ≤ 20."},
      "H": {"ok": "b", "hints": {"a": t("x ≤ 7 includes the 7.", "x ≤ 7 incluye el 7."), "c": t("8 is more than 7.", "8 es más que 7."), "d": t("There is a limit: 7.", "Hay un límite: 7.")}, "solution": t("7 hours.", "7 horas.")}
     }}

    quiz = [
     ("A", t("Solve: 2(x + 3) &gt; 10.", "Resuelva: 2(x + 3) &gt; 10."), [("a", "x &gt; 8"), ("b", "x &lt; 2"), ("c", "x &gt; 5"), ("d", "x &gt; 2")]),
     ("B", t("Solve: 3x + 2 ≤ x + 8.", "Resuelva: 3x + 2 ≤ x + 8."), [("a", "x ≥ 3"), ("b", "x ≤ 3"), ("c", "x ≤ 5"), ("d", "x ≤ 10")]),
     ("C", t("Solve: −2(x − 1) ≥ 8.", "Resuelva: −2(x − 1) ≥ 8."), [("a", "x ≤ −3"), ("b", "x ≥ −3"), ("c", "x ≤ 3"), ("d", "x ≥ 3")]),
     ("D", t("Translate: “a number x is at least 10.”", "Traduzca: «un número x es al menos 10»."), [("a", "x ≤ 10"), ("b", "x &gt; 10"), ("c", "x ≥ 10"), ("d", "x &lt; 10")]),
     ("E", t("Translate: “a number x does not exceed 20.”", "Traduzca: «un número x no excede 20»."), [("a", "x ≥ 20"), ("b", "x ≤ 20"), ("c", "x &lt; 20"), ("d", "x = 20")]),
     ("F", t("Translate: “twice a number is more than 14.”", "Traduzca: «el doble de un número es más que 14»."), [("a", "2x &lt; 14"), ("b", "2x ≥ 14"), ("c", "x + 2 &gt; 14"), ("d", "2x &gt; 14")]),
     ("G", t("You can spend at most $50 and you already spent $30. How much more (x)?", "Se puede gastar como máximo $50 y ya se gastaron $30. ¿Cuánto más (x)?"), [("a", "x ≥ 20"), ("b", "x &lt; 30"), ("c", "x ≤ 20"), ("d", "x ≤ 80")]),
     ("H", t("If x ≤ 7 stands for the number of hours, what is the most hours?", "Si x ≤ 7 representa el número de horas, ¿cuál es el máximo de horas?"), [("a", t("6 hours", "6 horas")), ("b", t("7 hours", "7 horas")), ("c", t("8 hours", "8 horas")), ("d", t("Infinitely many", "Infinitas"))])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Simplify before you solve, translate sentences into inequalities, and explain the solution in words.", "Simplifique antes de resolver, traduzca enunciados a inecuaciones e interprete la solución en palabras."),
        ("✏️", t("No calculator needed", "Sin calculadora")),
        [t("<strong>Solve</strong> inequalities that require distributing, combining like terms, and moving variables.", "<strong>Resolver</strong> inecuaciones que requieren distribuir, combinar términos semejantes y mover variables de lado."),
         t("<strong>Recognize</strong> the language of inequalities (at least, no more than, minimum, maximum, does not exceed).", "<strong>Reconocer</strong> el vocabulario verbal de las inecuaciones (al menos, no más de, mínimo, máximo, no excede)."),
         t("<strong>Translate</strong> sentences into inequalities and solve them.", "<strong>Traducir</strong> enunciados verbales a inecuaciones y resolverlas."),
         t("<strong>Explain</strong> the solution in the situation, with units.", "<strong>Interpretar</strong> la solución en el contexto del problema, con unidades."),
         t("<strong>Apply</strong> inequalities to real budget and time problems.", "<strong>Aplicar</strong> las inecuaciones a problemas reales de presupuesto y tiempo.")],
        secciones,
        (t("Solve four inequalities that require simplifying (distributing or combining) first. Translate four sentences into inequalities and solve them. Solve two problems in context and explain the solution in words, with units.",
           "Resuelva cuatro inecuaciones que requieran simplificar (distribuir o combinar) antes de resolver. Traduzca cuatro enunciados verbales a una inecuación y resuélvalos. Resuelva dos problemas de contexto e interprete la solución en palabras, con unidades."),
         t("Plan a real purchase: decide on a maximum budget, write down a fixed cost (for example, delivery) and the price of each item, and write an inequality for the number of items you can buy. Solve it and answer in a sentence.",
           "Planifique una compra real: decida un presupuesto máximo, anote un costo fijo (por ejemplo, el envío) y el precio de cada artículo, y escriba una inecuación para el número de artículos que puede comprar. Resuélvala y responda con una oración.")),
        quiz,
        t("Self-check checklist for inequalities and word problems", "Lista de autoevaluación para inecuaciones y problemas verbales"),
        t("Self-check checklist: skills for simplifying inequalities, translating sentences, and explaining the solution", "Lista de autoevaluación: destrezas para simplificar inecuaciones, traducir enunciados e interpretar la solución"),
        [(t("Simplifying before solving", "Simplificar antes de resolver"), t("I distribute, combine, and move variables correctly, and I use the sign rule when needed.", "Distribuyo, combino y muevo variables correctamente, y aplico la regla del signo cuando toca."), t("I simplify only partly.", "Simplifico de forma incompleta."), t("I try to solve without simplifying first.", "Intento resolver sin simplificar primero.")),
         (t("Translating the sentence", "Traducir el enunciado"), t("I find the key word and write the right inequality.", "Identifico la palabra clave y escribo la inecuación correcta."), t("I translate with some sign mistakes.", "Traduzco con errores ocasionales de signo."), t("I choose the wrong inequality sign.", "Elijo el signo de desigualdad incorrecto.")),
         (t("Explaining in context", "Interpretar en contexto"), t("I explain the solution in words, with units, and identify the maximum or minimum.", "Interpreto la solución en palabras, con unidades, e identifico el máximo o el mínimo."), t("I explain without units or not precisely.", "Interpreto sin unidades o de forma imprecisa."), t("I do not explain the solution.", "No interpreto la solución."))],
        t("<p>You solved inequalities that you must simplify first, and you learned to translate sentences into inequalities with the key words (at least, no more than, at most…), to solve real budget and time problems, and to explain the solution in words.</p>\n<p>In <strong>Lesson 5.3 · Solving literal formulas, and a general strategy</strong> you will close Topic 5 by using everything you learned on formulas: you will solve for a specific variable in geometry, money, and science formulas (like d = rt or A = bh), treating the other letters as if they were numbers.</p>",
          "<p>En esta lección se resolvieron inecuaciones que primero hay que simplificar y se aprendió a traducir enunciados verbales a inecuaciones, usando el vocabulario clave (al menos, no más de, máximo…), para resolver problemas reales de presupuesto y tiempo e interpretar la solución en palabras.</p>\n<p>En la <strong>Lección 5.3 · Despeje de fórmulas literales y estrategia general de resolución</strong> se cerrará el Tema 5 aplicando todo lo aprendido a las fórmulas: se despejará una variable específica en fórmulas de geometría, finanzas y física (como d = rt o A = bh), tratando las demás letras como si fueran números.</p>"),
        ("5-3", ("", t("Lesson 5.3 · Solving literal formulas, and a general strategy", "Lección 5.3 · Despeje de fórmulas literales y estrategia general de resolución"))),
        [(t("at least", "al menos"), t("That number or more: ≥.", "Ese número o más: ≥.")),
         (t("at most", "como máximo"), t("That number or less: ≤.", "Ese número o menos: ≤.")),
         (t("does not exceed", "no excede"), t("Is not more than: ≤.", "No es mayor que: ≤.")),
         (t("interpret", "interpretar"), t("To say what the solution means in the situation, in words and with units.", "Decir qué significa la solución en el contexto, en palabras y con unidades."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function pasosLista(pasos, visto){ return pasos.slice(0, visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join(""); }
function botonPasos(pre, S){ var b = $(pre + "-sig"); b.disabled = S.visto >= S.pasos.length; $(pre + "-todo").disabled = b.disabled; b.textContent = S.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso")); }

/* ============ MODULE 1 · inequalities that need simplifying ============ */
function ineqCompuesta(tp){
  var r = elige(RELS), v = aleatorio(-5, 8), m, p, a, b, c, d, e, vis, pre = [], izq, der;
  if (tp === undefined) tp = aleatorio(1, 4);
  if (tp === 1){ m = aleatorio(2, 6); p = nz(); izq = L(m, m * p); der = L(0, m * (v + p));
    vis = auto(m + "(" + P(tm(1, "x"), tm(p)) + ")") + " " + relVis(r) + " " + menosV(der.k.n);
    pre.push(T("Distribute: ", "Se distribuye: ") + ineqHTML(izq, r, der) + "."); }
  else if (tp === 2){ do { a = aleatorio(2, 8); c = aleatorio(1, 7); } while (a === c); b = nz(); d = a * v + b - c * v; izq = L(a, b); der = L(c, d);
    vis = ineqHTML(izq, r, der); }
  else if (tp === 3){ m = -aleatorio(2, 5); p = nz(); izq = L(m, m * p); der = L(0, m * (v + p));
    vis = auto(menosV(m) + "(" + P(tm(1, "x"), tm(p)) + ")") + " " + relVis(r) + " " + menosV(der.k.n);
    pre.push(T("Distribute the " + menosV(m) + " to each term: ", "Se distribuye el " + menosV(m) + " a cada término: ") + ineqHTML(izq, r, der) + "."); }
  else { a = aleatorio(2, 6); e = elige([1, 2, 3, -1]); b = nz(); izq = L(a + e, b); der = L(0, (a + e) * v + b);
    vis = auto(P(tm(a, "x"), tm(b), tm(e, "x"))) + " " + relVis(r) + " " + menosV(der.k.n);
    pre.push(T("Combine the x terms: ", "Se combinan los términos en x: ") + ineqHTML(izq, r, der) + "."); }
  var R = pasosIneq(izq, r, der);
  return {vis: vis, pasos: pre.concat(R.pasos), r: R.r, v: R.v, invierte: R.invierte};
}
var SM = {pasos: [], visto: 0, sol: null, cola: [1, 2, 3]};
function nuevoSM(){
  var E = ineqCompuesta(SM.cola.length ? SM.cola.shift() : undefined);
  SM.pasos = E.pasos.concat(['<span class="veredicto">' + T("Solution: ", "Solución: ") + solHTML(E.r, E.v) + "</span>"]); SM.sol = E; SM.visto = 0;
  $("sm-ec").innerHTML = E.vis;
  pintaSM();
}
function pintaSM(){
  $("sm-pasos").innerHTML = pasosLista(SM.pasos, SM.visto);
  $("sm-recta").innerHTML = SM.visto >= SM.pasos.length ? ineqSVG(SM.sol.v, SM.sol.r) : "";
  botonPasos("sm", SM);
}
function genCompuesta(){ var E = ineqCompuesta(); return {enun: T("Solve ", "Resuelva ") + E.vis + ".", r: E.r, v: E.v, invierte: E.invierte, explica: E.pasos.join(" ")}; }

/* ============ MODULE 2 · the language of inequalities ============ */
var FRASES = ES ? [
  ["es al menos", "≥"], ["es como mínimo", "≥"], ["no es menos de", "≥"], ["es mayor o igual que", "≥"],
  ["es como máximo", "≤"], ["es a lo sumo", "≤"], ["no es más de", "≤"], ["no excede", "≤"],
  ["es más que", ">"], ["es mayor que", ">"], ["supera", ">"],
  ["es menos que", "<"], ["es menor que", "<"], ["no llega a", "<"]
] : [
  ["is at least", "≥"], ["is no less than", "≥"], ["is not less than", "≥"], ["is greater than or equal to", "≥"],
  ["is at most", "≤"], ["is no more than", "≤"], ["is not more than", "≤"], ["does not exceed", "≤"],
  ["is more than", ">"], ["is greater than", ">"], ["exceeds", ">"],
  ["is less than", "<"], ["is smaller than", "<"], ["is below", "<"]
];
function llenaVO(){ var sel = $("vo-sel"); FRASES.forEach(function(f, i){ var o = document.createElement("option"); o.value = i; o.textContent = T("A number ", "Un número ") + f[0] + " 10"; sel.appendChild(o); }); }
function pintaVO(){
  var f = FRASES[+$("vo-sel").value], r = f[1], incl = !REL_ESTRICTO[r];
  $("vo-salida").innerHTML = '<div class="linea grande">' + T("“A number " + f[0] + " 10” → ", "«Un número " + f[0] + " 10» → ") + solHTML(r, fr(10)) + "</div>" +
    '<div class="linea">' + (incl ? T("10 <strong>is</strong> included: closed point.", "El 10 <strong>sí</strong> se incluye: punto cerrado.") : T("10 is <strong>not</strong> included: open point.", "El 10 <strong>no</strong> se incluye: punto abierto.")) +
    T(" The numbers that work are the ones " + (derecha(r) ? "greater" : "less") + " than 10" + (incl ? ", and 10 itself." : "."), " Los números que cumplen son los " + (derecha(r) ? "mayores" : "menores") + " que 10" + (incl ? ", y el propio 10." : ".")) + "</div>";
  $("vo-recta").innerHTML = ineqSVG(fr(10), r);
}
function genVocabulario(){
  var n = aleatorio(5, 30), f = elige(FRASES), r = f[1], pc = {};
  function pistaRel(x){ return REL_ESTRICTO[x] !== REL_ESTRICTO[r] ? T("Check whether “" + f[0] + "” includes the boundary.", "Revise si «" + f[0] + "» incluye el límite.") : T("Check the direction: greater or less?", "Revise la dirección: ¿mayores o menores?"); }
  if (Math.random() < 0.45){
    RELS.forEach(function(x){ if (x !== r) pc[x + n + "/1"] = pistaRel(x); });
    return {enun: T("Translate: “A number x " + f[0] + " " + n + ".”", "Traduzca: «Un número x " + f[0] + " " + n + "»."), opciones: RELS.map(function(x){ return opSol(x, fr(n)); }), correcta: r + n + "/1", porClave: pc, enOrden: true,
      bien: T("“" + f[0] + "” matches ", "«" + f[0] + "» corresponde a ") + relVis(r) + ".", mal: T("“" + f[0] + "” matches ", "«" + f[0] + "» corresponde a ") + relVis(r) + ": " + solHTML(r, fr(n)) + "."};
  }
  var k = aleatorio(2, 9), tipo = elige(["doble", "aumentado", "disminuido", "veces"]), izq, frase;
  if (tipo === "doble"){ izq = L(2, 0); frase = T("Twice a number", "El doble de un número"); }
  else if (tipo === "aumentado"){ izq = L(1, k); frase = T("A number increased by " + k, "Un número aumentado en " + k); }
  else if (tipo === "disminuido"){ izq = L(1, -k); frase = T("A number decreased by " + k, "Un número disminuido en " + k); }
  else { izq = L(k, 0); frase = T(k + " times a number", k + " veces un número"); }
  var der = L(0, n), op = function(rr, l){ return {html: ineqHTML(l, rr, der), clave: rr + ladoVis(l)}; };
  var otroL = tipo === "doble" ? L(1, 2) : (tipo === "aumentado" ? L(k, 0) : (tipo === "disminuido" ? L(-1, k) : L(1, k)));
  var rEst = REL_ESTRICTO[r] ? (r === "<" ? "≤" : "≥") : (r === "≤" ? "<" : ">");
  var o2 = [op(r, izq), op(REL_INV[r], izq), op(rEst, izq), op(r, otroL)];
  pc[o2[1].clave] = pistaRel(REL_INV[r]); pc[o2[2].clave] = pistaRel(rEst);
  pc[o2[3].clave] = T("Check the translation of “" + frase.toLowerCase() + ".”", "Revise la traducción de «" + frase.toLowerCase() + "».");
  return {enun: T("Translate: “" + frase + " " + f[0] + " " + n + ".”", "Traduzca: «" + frase + " " + f[0] + " " + n + "»."), opciones: o2, correcta: o2[0].clave, porClave: pc,
    bien: T("“" + frase + "” is ", "«" + frase + "» es ") + ladoHTML(izq) + T(" and “" + f[0] + "” is ", " y «" + f[0] + "» es ") + relVis(r) + ".", mal: T("The translation is ", "La traducción es ") + ineqHTML(izq, r, der) + "."};
}

/* ============ MODULE 3 · problems in context ============ */
function problemaAzar(){
  var tp = aleatorio(1, 5), q;
  function sinEntero(base, paso, lim){ var tries = 0, v; do { v = lim(); tries++; } while (tries < 50 && (v - base) % paso === 0); return v; }
  if (tp === 1){
    var G = aleatorio(5, 30), p = aleatorio(3, 12), B = sinEntero(G, p, function(){ return G + p * aleatorio(2, 8) + aleatorio(0, p - 1); });
    q = {txt: T("You have at most $" + B + " to spend. You already spent $" + G + ", and each notebook costs $" + p + ". What is the greatest number of notebooks you can buy?", "Usted tiene como máximo $" + B + " para gastar. Ya gastó $" + G + " y cada cuaderno cuesta $" + p + ". ¿Cuántos cuadernos puede comprar como máximo?"),
         izq: L(p, G), r: "≤", der: L(0, B), max: true, unidad: T("notebooks", "cuadernos"), etq: T("Most notebooks", "Máximo de cuadernos")};
  } else if (tp === 2){
    var h = aleatorio(2, 10), d = aleatorio(3, 6), H = sinEntero(h, d, function(){ return h + d * aleatorio(2, 7) + aleatorio(0, d - 1); });
    q = {txt: T("A project needs at least " + H + " hours of work. " + h + " hours are already done, and " + d + " more hours are worked each day. What is the least number of days still needed?", "Un proyecto necesita al menos " + H + " horas de trabajo. Ya se trabajaron " + h + " horas y cada día se trabajan " + d + " horas más. ¿Cuántos días más hacen falta como mínimo?"),
         izq: L(d, h), r: "≥", der: L(0, H), max: false, unidad: T("days", "días"), etq: T("Fewest days", "Mínimo de días")};
  } else if (tp === 3){
    var s = aleatorio(2, 6) * 50, c = aleatorio(2, 6) * 5, M = sinEntero(s, c, function(){ return s + c * aleatorio(4, 20) + aleatorio(1, c - 1); });
    q = {txt: T("A salesperson earns $" + s + " a week plus $" + c + " for each sale. She wants to earn at least $" + M + " this week. What is the least number of sales she needs?", "Una vendedora gana $" + s + " fijos a la semana más $" + c + " por cada venta. Quiere ganar al menos $" + M + " esta semana. ¿Cuántas ventas necesita como mínimo?"),
         izq: L(c, s), r: "≥", der: L(0, M), max: false, unidad: T("sales", "ventas"), etq: T("Fewest sales", "Mínimo de ventas")};
  } else if (tp === 4){
    var b = aleatorio(2, 5), k = aleatorio(2, 4), Tt = sinEntero(b, k, function(){ return b + k * aleatorio(3, 10) + aleatorio(1, k - 1); });
    q = {txt: T("A taxi charges $" + b + " to start plus $" + k + " per mile. You do not want to spend more than $" + Tt + ". What is the greatest number of whole miles you can ride?", "Un taxi cobra $" + b + " al subir más $" + k + " por cada milla. Usted no quiere gastar más de $" + Tt + ". ¿Cuántas millas enteras puede recorrer como máximo?"),
         izq: L(k, b), r: "≤", der: L(0, Tt), max: true, unidad: T("miles", "millas"), etq: T("Most miles", "Máximo de millas")};
  } else {
    var W = elige([1500, 1800, 2000, 2200, 2500]), o = aleatorio(150, 210), cj = elige([60, 75, 90, 100]);
    q = {txt: T("An elevator holds at most " + W.toLocaleString("en-US") + " pounds. A worker who weighs " + o + " pounds rides with boxes of " + cj + " pounds each. What is the greatest number of boxes he can take in one trip?", "Un ascensor soporta a lo sumo " + W.toLocaleString("en-US") + " libras. Un operario de " + o + " libras sube con cajas de " + cj + " libras cada una. ¿Cuántas cajas puede llevar como máximo en un viaje?"),
         izq: L(cj, o), r: "≤", der: L(0, W), max: true, unidad: T("boxes", "cajas"), etq: T("Most boxes", "Máximo de cajas")};
  }
  var R = resuelveIneq(q.izq, q.r, q.der);
  q.lim = R.v; q.resp = q.max ? Math.floor(fval(R.v) + 1e-9) : Math.ceil(fval(R.v) - 1e-9);
  return q;
}
var CX = {q: null, elegida: null, primero: 0, pista: 0, total: 0, resuelta: false, intentos: 0};
function pintaCX(){
  var q = CX.q = problemaAzar(); CX.elegida = null; CX.resuelta = false; CX.intentos = 0;
  $("cx-enun").textContent = q.txt;
  var alt = [{l: q.izq, r: q.r, clave: "b"}, {l: q.izq, r: REL_INV[q.r], clave: "inv"}, (figual(q.izq.k, q.izq.x) ? {l: L(q.izq.x, 0), r: q.r, clave: "cruz"} : {l: L(q.izq.k, q.izq.x), r: q.r, clave: "cruz"}), {l: q.izq, r: q.r === "≤" ? "<" : ">", clave: "estr"}];
  var cont = $("cx-opciones"); cont.innerHTML = "";
  baraja(alt).forEach(function(a){
    var b = document.createElement("button"); b.type = "button"; b.className = "opcion"; b.setAttribute("aria-pressed", "false");
    b.setAttribute("data-clave", a.clave); b.innerHTML = ineqHTML(a.l, a.r, q.der);
    b.addEventListener("click", function(){ if (CX.resuelta) return; CX.elegida = a.clave; Array.prototype.forEach.call(cont.children, function(x){ x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); });
    cont.appendChild(b);
  });
  $("cx-rlab").textContent = "2. " + q.etq;
  $("cx-r").value = ""; $("cx-r").disabled = false; $("cx-comprobar").disabled = false;
  $("cx-fb").className = "fb"; $("cx-fb").innerHTML = "";
}
function compruebaCX(){
  if (CX.resuelta) return;
  var q = CX.q, fb = $("cx-fb"), n = leeEntero($("cx-r").value), vd = leeDecimal($("cx-r").value);
  if (!CX.elegida || (n === null && vd === null)){ fb.className = "fb pista"; fb.innerHTML = T("Choose the setup and type your answer.", "Elija el planteamiento y escriba su respuesta."); return; }
  CX.intentos++;
  var okP = CX.elegida === "b", okR = n === q.resp, msgs = [];
  if (!okP){
    if (CX.elegida === "inv") msgs.push(T("The sign of the setup is backward: ", "El signo del planteamiento está al revés: ") + (q.max ? T("“at most” or “no more than” is ≤.", "«como máximo» o «no más de» es ≤.") : T("“at least” is ≥.", "«al menos» es ≥.")));
    else if (CX.elegida === "cruz") msgs.push(figual(q.izq.k, q.izq.x) ? T("The setup must include the fixed amount too.", "El planteamiento también tiene que incluir la cantidad fija.") : T("In the setup, x multiplies the amount for each unit, not the fixed amount.", "En el planteamiento, x multiplica al valor de cada unidad, no a la cantidad fija."));
    else msgs.push(T("The limit is included: use " + relVis(q.r) + ", not the strict sign.", "El límite se incluye: use " + relVis(q.r) + ", no el signo estricto."));
  }
  if (!okR){
    if (n === null || Math.abs(vd - fval(q.lim)) < 1e-6) msgs.push(T("The solution of the inequality is ", "La solución de la inecuación es ") + solHTML(q.max ? "≤" : "≥", q.lim) + T(", but the answer has to be a whole number of " + q.unidad + ".", ", pero la respuesta tiene que ser un número entero de " + q.unidad + "."));
    else if (n === q.resp + (q.max ? 1 : -1)) msgs.push(q.max ? T("With " + n + " you go over the limit. Since it is a maximum, round down.", "Con " + n + " se pasa del límite. Al ser un máximo, se redondea hacia abajo.") : T("With " + n + " you do not reach the minimum. Since it is a minimum, round up.", "Con " + n + " no se llega al mínimo. Al ser un mínimo, se redondea hacia arriba."));
    else msgs.push(T("Check the answer: solve the inequality, then round " + (q.max ? "down." : "up."), "Revise la respuesta: resuelva la inecuación y después redondee " + (q.max ? "hacia abajo." : "hacia arriba.")));
  }
  var R = resuelveIneq(q.izq, q.r, q.der);
  var sol = ineqHTML(q.izq, q.r, q.der) + " → " + solHTML(R.r, R.v) + (fent(R.v) ? "" : " (≈ " + aprox(fval(R.v), 2) + ")") + ". " +
            T("Since x counts " + q.unidad + ", the " + (q.max ? "greatest" : "least") + " whole number is " + q.resp + ": " + (q.max ? "at most " : "at least ") + q.resp + " " + q.unidad + ".",
              "Como x cuenta " + q.unidad + ", " + (q.max ? "el máximo entero es " : "el mínimo entero es ") + q.resp + ": " + (q.max ? "como máximo " : "como mínimo ") + q.resp + " " + q.unidad + ".");
  if (okP && okR){ CX.resuelta = true; CX.total++; if (CX.intentos === 1) CX.primero++; else CX.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + sol; }
  else if (CX.intentos >= 2){ CX.resuelta = true; CX.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + sol + TX.nuevo; }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msgs.join(" ") + TX.unoMas; }
  if (CX.resuelta){
    $("cx-r").disabled = true; $("cx-comprobar").disabled = true;
    Array.prototype.forEach.call($("cx-opciones").children, function(b){ b.disabled = true; if (b.getAttribute("data-clave") === "b") b.className = "opcion correcta"; else if (b.getAttribute("data-clave") === CX.elegida) b.className = "opcion incorrecta"; });
  }
  $("cx-marcador").textContent = CX.total ? TX.resueltos(CX.primero + CX.pista, CX.primero, CX.total) : "";
}

/* ============ Start ============ */
$("sm-sig").addEventListener("click", function(){ if (SM.visto < SM.pasos.length){ SM.visto++; pintaSM(); } });
$("sm-todo").addEventListener("click", function(){ SM.visto = SM.pasos.length; pintaSM(); });
$("sm-nuevo").addEventListener("click", nuevoSM);
nuevoSM();
creaPracticaDesig("p1", genCompuesta);
llenaVO();
$("vo-sel").addEventListener("change", pintaVO);
pintaVO();
OMR("p2", genVocabulario);
$("cx-comprobar").addEventListener("click", compruebaCX);
$("cx-r").addEventListener("keydown", function(ev){ if (ev.key === "Enter") compruebaCX(); });
$("cx-nuevo").addEventListener("click", pintaCX);
pintaCX();
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}\n  .opcion[aria-pressed=true]{border-color:var(--tema);background:var(--tema-bg);font-weight:700;}"

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("simplify", "simplificar"), t("Inequalities that need simplifying", "Inecuaciones que requieren simplificar"),
      f'''      <p>{t("When there are parentheses or repeated terms, first simplify with the tools from Topic 4 (distribute and combine), then solve. The sign rule still holds: if at the end you divide by a negative number, the sign flips.", "Cuando hay paréntesis o términos repetidos, primero se simplifica con las herramientas del Tema 4 (distribuir y combinar) y después se resuelve. La regla del signo sigue vigente: si al final se divide por un negativo, el signo se invierte.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <div class="estado"><span class="grande" id="sm-ec"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="sm-sig"></button><button type="button" class="btn-sec" id="sm-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="sm-nuevo">{t("Another inequality", "Otra inecuación")}</button></div>
      </div>
      <div class="pasos" id="sm-pasos" aria-live="polite"></div>
      <div id="sm-recta"></div>
{P.desig("p1", t("Practice: simplify and solve", "Practique: simplifique y resuelva"))}'''),
     (t("vocabulary", "vocabulario"), t("The language of inequalities", "El vocabulario de las inecuaciones"),
      f'''      <p>{t("Certain words always point to the same sign. The ones that talk about a minimum or a maximum <strong>include</strong> the boundary; the ones that say “more than” or “less than” do not.", "Ciertas palabras señalan siempre el mismo signo. Las que hablan de un mínimo o de un máximo <strong>incluyen</strong> el límite; las que hablan de «más que» o «menos que» no lo incluyen.")}</p>
      <h3>{t("From the sentence to the sign", "Del enunciado al signo")}</h3>
      <div class="panel"><div class="campos"><div class="campo" style="flex:1;min-width:240px;"><label for="vo-sel">{t("Phrase", "Frase")}</label><select id="vo-sel"></select></div></div></div>
{P.salida("vo-salida")}
      <div id="vo-recta"></div>
{P.atencion(t("“At least” and “at most” include the boundary:", "«Al menos» y «como máximo» incluyen el límite:"), t("“at least 10” is 10 or more (≥ 10), and “at most 10” is 10 or less (≤ 10). That is why they are graphed with a closed point.", "«al menos 10» es 10 o más (≥ 10) y «como máximo 10» es 10 o menos (≤ 10). Por eso se grafican con punto cerrado."))}
{B.om("p2", t("Practice: translate into an inequality", "Practique: traduzca a inecuación"))}'''),
     (t("context", "contexto"), t("Budget and time problems", "Problemas de presupuesto y tiempo"),
      f'''      <p>{t("Inequalities model real-life limits: a budget you cannot go over, a minimum number of hours you must work. You solve them in three parts: <strong>set up</strong>, <strong>solve</strong>, and <strong>explain</strong>.", "Las inecuaciones modelan límites de la vida real: un presupuesto que no se puede superar, un mínimo de horas que hay que cumplir. Se resuelven en tres partes: <strong>plantear</strong>, <strong>resolver</strong> e <strong>interpretar</strong>.")}</p>
      <div class="caja-tip"><strong>{t("Explaining with whole numbers:", "Interpretar con enteros:")}</strong> {t("you do not buy parts of an item or work parts of a day. If the solution is x ≤ 6.4 and x counts items, the most is 6 (round down). If it is x ≥ 3.2 and x counts days, the least is 4 (round up), because 3 days are not enough.", "no se compran fracciones de artículo ni se trabajan fracciones de día. Si la solución es x ≤ 6.4 y x cuenta artículos, el máximo es 6 (se redondea hacia abajo). Si es x ≥ 3.2 y x cuenta días, el mínimo es 4 (se redondea hacia arriba), porque 3 días no alcanzan.")}</div>
      <h3>{t("Practice: set up, solve, and explain", "Practique: plantee, resuelva e interprete")}</h3>
      <div class="practica" id="cx">
        <div class="enun" id="cx-enun"></div>
        <p><strong>{t("1. Which inequality represents the problem?", "1. ¿Qué inecuación representa el problema?")}</strong></p>
        <div class="opciones" id="cx-opciones" role="group" aria-label="{t("Possible setups", "Planteamientos posibles")}"></div>
        <div class="campos" style="margin-top:12px;"><div class="campo"><label for="cx-r" id="cx-rlab">{t("2. Answer", "2. Respuesta")}</label><input type="text" autocomplete="off" class="corto" id="cx-r"></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="cx-comprobar">Check</button><button type="button" class="btn-sec" id="cx-nuevo">{t("Another problem", "Otro problema")}</button></div>
        <div class="fb" id="cx-fb" role="status"></div>
        <p class="marcador" id="cx-marcador"></p>
      </div>
{P.atencion(t("Answer in words:", "Responder en palabras:"), t("a word problem does not end with “x ≤ 6,” but with a sentence like “you can buy at most 6 items.”", "un problema verbal no termina con «x ≤ 6», sino con una oración como «se pueden comprar como máximo 6 artículos»."))}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Inecuaciones que requieren simplificación y problemas verbales")
