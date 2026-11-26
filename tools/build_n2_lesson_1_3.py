"""Level 2 · Lesson 1.3 · Multiplying and dividing integers; applications — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import m, p

B.NIVEL = 2
N = "1-3"
TEMA = ("Integers", "Enteros con signo")

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 1.2 you learned to add and subtract integers. This lesson finishes Topic 1 with the other two operations: <strong>multiplying</strong> and <strong>dividing</strong>. The good news: both use one sign rule, and it is shorter than the rule for adding.",
"En la Lección 1.2 aprendió a sumar y restar enteros. Esta lección termina el Tema 1 con las otras dos operaciones: la <strong>multiplicación</strong> y la <strong>división</strong>. La buena noticia: las dos usan una sola regla de los signos, más corta que la de la suma.")}</p>
<p>{t("To multiply two integers, multiply the absolute values as you always do. What is new is the <strong>sign</strong>, and it depends only on the signs of the two factors.", "Para multiplicar dos enteros, se multiplican los valores absolutos como siempre. Lo nuevo es el <strong>signo</strong>, que depende solo de los signos de los dos factores.")}</p>
{tabla(t("The sign rule for multiplying", "La regla de los signos de la multiplicación"), t("The sign of the product for each pair of signs of the factors", "El signo del producto para cada pareja de signos de los factores"),
       [t("Factor 1", "Factor 1"), t("Factor 2", "Factor 2"), t("Product", "Producto")],
       [[t("positive", "positivo"), t("positive", "positivo"), t("<strong>positive (+)</strong>", "<strong>positivo (+)</strong>")],
        [t("negative", "negativo"), t("negative", "negativo"), t("<strong>positive (+)</strong>", "<strong>positivo (+)</strong>")],
        [t("positive", "positivo"), t("negative", "negativo"), t("<strong>negative (−)</strong>", "<strong>negativo (−)</strong>")],
        [t("negative", "negativo"), t("positive", "positivo"), t("<strong>negative (−)</strong>", "<strong>negativo (−)</strong>")]])}
{caja("tip", t("The short rule", "La regla breve"), t("<p><strong>Same signs give a positive product. Different signs give a negative product.</strong> One sentence covers the four rows of the table.</p>",
"<p><strong>Signos iguales dan producto positivo. Signos distintos dan producto negativo.</strong> Una sola frase resume las cuatro filas de la tabla.</p>"))}
{ejemplo(t("Example: (−7) × (−6)", "Ejemplo: (−7) × (−6)"),
  [("1", t("Step 1.", "Paso 1."), t("Multiply the absolute values: 7 × 6 = 42.", "Se multiplican los valores absolutos: 7 × 6 = 42.")),
   ("2", t("Step 2.", "Paso 2."), t("Both factors are negative: same signs.", "Los dos factores son negativos: signos iguales.")),
   ("✓", t("Result.", "Resultado."), t("Same signs give a positive product: (−7) × (−6) = <strong>42</strong>", "Signos iguales dan producto positivo: (−7) × (−6) = <strong>42</strong>"))])}
{ejemplo(t("Example: 9 × (−4)", "Ejemplo: 9 × (−4)"),
  [("1", t("Step 1.", "Paso 1."), t("Multiply the absolute values: 9 × 4 = 36.", "Se multiplican los valores absolutos: 9 × 4 = 36.")),
   ("2", t("Step 2.", "Paso 2."), t("One factor is positive and one is negative: different signs.", "Un factor positivo y otro negativo: signos distintos.")),
   ("✓", t("Result.", "Resultado."), t("Different signs give a negative product: 9 × (−4) = <strong>−36</strong>", "Signos distintos dan producto negativo: 9 × (−4) = <strong>−36</strong>"))])}
{caja("ojo", t("Watch out!", "¡Ojo!"), t("<p>This rule is for <strong>multiplying and dividing</strong>. For adding, the rule is different: −7 + (−6) = −13, but (−7) × (−6) = 42. Before you choose a rule, look at the operation.</p>",
"<p>Esta regla es para <strong>multiplicar y dividir</strong>. Para sumar, la regla es otra: −7 + (−6) = −13, pero (−7) × (−6) = 42. Antes de elegir una regla, mire la operación.</p>"))}
{practica("p1", t("Practice 1 — Different signs", "Práctica 1 — Signos distintos"), t("What is (−8) × 5?", "¿Cuánto es (−8) × 5?"),
          [("a", "40"), ("b", "−40"), ("c", "−13"), ("d", "−3")])}
{practica("p2", t("Practice 2 — Same signs", "Práctica 2 — Signos iguales"), t("What is (−6) × (−7)?", "¿Cuánto es (−6) × (−7)?"),
          [("a", "42"), ("b", "−42"), ("c", "−13"), ("d", "13")])}
{enlace(n, t("signs", "signos"), t("the sign rule", "la regla de los signos"), t("Predict the sign of each product, then find its value.", "Prediga el signo de cada producto y después halle su valor."))}'''

    filas = [(3, -2), (2, -2), (1, -2), (0, -2), (-1, -2), (-2, -2)]
    s2 = f'''<p>{t("\"A negative times a negative is positive\" is not a random rule: you can <strong>discover</strong> it in a pattern. Multiply −2 by a list of numbers that goes down by one. Each product goes <strong>up by 2</strong>:",
"«Negativo por negativo da positivo» no es un capricho: se puede <strong>descubrir</strong> en un patrón. Multiplique −2 por una lista de números que baja de uno en uno. Cada producto <strong>aumenta 2</strong>:")}</p>
{tabla(t("The pattern", "El patrón"), t("Products of a list that goes down by one, times −2, and how much each product changes", "Productos de una lista que baja de uno en uno por −2, y cuánto cambia cada producto"),
       [t("Multiplication", "Multiplicación"), t("Product", "Producto"), t("Change", "Cambio")],
       [[f"{p(a)} × {p(b)}", f"<strong>{m(a*b)}</strong>", "—" if i == 0 else t("went up 2", "aumentó 2") + (t(" (the pattern says it must be positive)", " (el patrón obliga a que sea positivo)") if a == -1 else "")] for i, (a, b) in enumerate(filas)])}
<p>{t("For the pattern to keep going, the product of two negatives <strong>has to be</strong> positive. There is no other way to continue it without breaking it.",
"Para que el patrón siga igual, el producto de dos negativos <strong>tiene que ser</strong> positivo. No hay otra forma de continuarlo sin romperlo.")}</p>
{caja("tip", t("In everyday language", "En el lenguaje de todos los días"), t("<p>Taking away a debt again and again makes you richer. If a debt of $5 (−5) is taken away 3 times (−3), you gain $15: (−3) × (−5) = 15.</p>",
"<p>Quitar una deuda una y otra vez lo hace más rico. Si se le quita 3 veces (−3) una deuda de $5 (−5), gana $15: (−3) × (−5) = 15.</p>"))}
<p>{t("You do not need to repeat the pattern every time. It only shows that the rule makes sense. In practice, use the short rule: same signs, positive; different signs, negative.",
"No hace falta repetir el patrón cada vez. Solo muestra que la regla tiene sentido. En la práctica, use la regla breve: signos iguales, positivo; signos distintos, negativo.")}</p>
{practica("p3", t("Practice 3 — Continue the pattern", "Práctica 3 — Siga el patrón"), t("1 × (−3) = −3, &nbsp; 0 × (−3) = 0, &nbsp; (−1) × (−3) = ?", "1 × (−3) = −3, &nbsp; 0 × (−3) = 0, &nbsp; (−1) × (−3) = ?"),
          [("a", "−3"), ("b", "0"), ("c", "3"), ("d", "−4")])}
{enlace(n, t("why", "por-que"), t("why a negative times a negative is positive", "por qué negativo por negativo da positivo"), t("Follow the pattern of products across zero and see why the rule works.", "Siga el patrón de productos al cruzar el cero y vea por qué la regla funciona."))}'''

    s3 = f'''<p>{t("Dividing integers uses <strong>exactly the same sign rule</strong> as multiplying. There is nothing new to memorize: same signs give a positive quotient; different signs give a negative quotient.",
"La división de enteros usa <strong>exactamente la misma regla de los signos</strong> que la multiplicación. No hay nada nuevo que memorizar: signos iguales dan cociente positivo; signos distintos dan cociente negativo.")}</p>
{ejemplo(t("Example: (−45) ÷ (−9)", "Ejemplo: (−45) ÷ (−9)"),
  [("1", t("Step 1.", "Paso 1."), t("Divide the absolute values: 45 ÷ 9 = 5.", "Se dividen los valores absolutos: 45 ÷ 9 = 5.")),
   ("2", t("Step 2.", "Paso 2."), t("Both numbers are negative: same signs, so the quotient is positive.", "Los dos son negativos: signos iguales, así que el cociente es positivo.")),
   ("✓", t("Result.", "Resultado."), "(−45) ÷ (−9) = <strong>5</strong>")])}
{ejemplo(t("Example: (−56) ÷ 8", "Ejemplo: (−56) ÷ 8"),
  [("1", t("Step 1.", "Paso 1."), t("Divide the absolute values: 56 ÷ 8 = 7.", "Se dividen los valores absolutos: 56 ÷ 8 = 7.")),
   ("2", t("Step 2.", "Paso 2."), t("One is negative and one is positive: different signs, so the quotient is negative.", "Uno es negativo y otro positivo: signos distintos, así que el cociente es negativo.")),
   ("✓", t("Result.", "Resultado."), "(−56) ÷ 8 = <strong>−7</strong>")])}
{caja("tip", t("Check by multiplying", "Compruebe multiplicando"), t("<p>You can always check a division with a multiplication. If (−45) ÷ (−9) = 5, then 5 × (−9) must be −45. It is, so both the value and the sign are right.</p>",
"<p>Una división siempre se puede comprobar con una multiplicación. Si (−45) ÷ (−9) = 5, entonces 5 × (−9) debe dar −45. Así es, de modo que el valor y el signo están bien.</p>"))}
<h3>{t("Zero in a division", "El cero en una división")}</h3>
<p>{t("Zero divided by any other number is 0: 0 ÷ 5 = 0, because 0 × 5 = 0. But <strong>you cannot divide by zero</strong>: 5 ÷ 0 has no answer, because no number times 0 gives 5. We say that a division by zero is <strong>undefined</strong>.",
"Cero entre cualquier otro número da 0: 0 ÷ 5 = 0, porque 0 × 5 = 0. Pero <strong>no se puede dividir entre cero</strong>: 5 ÷ 0 no tiene respuesta, porque ningún número multiplicado por 0 da 5. Se dice que una división entre cero <strong>no está definida</strong>.")}</p>
{caja("ojo", t("On the GED", "En el examen de GED"), t("<p>A question may ask when an expression is <strong>undefined</strong>. Look for a division where the number you divide by is (or becomes) 0. On the calculator, a division by zero gives an error.</p>",
"<p>Una pregunta puede pedirle que diga cuándo una expresión <strong>no está definida</strong>. Busque una división en la que el número entre el que se divide sea 0 (o termine siendo 0). En la calculadora, una división entre cero da error.</p>"))}
{practica("p4", t("Practice 4 — Divide", "Práctica 4 — Dividir"), t("What is (−48) ÷ 6?", "¿Cuánto es (−48) ÷ 6?"),
          [("a", "8"), ("b", "−42"), ("c", "−8"), ("d", "−54")])}
{practica("p5", t("Practice 5 — Zero", "Práctica 5 — El cero"), t("Which expression is <strong>undefined</strong>?", "¿Qué expresión <strong>no está definida</strong>?"),
          [("a", "0 ÷ (−7)"), ("b", "(−7) × 0"), ("c", "0 − 7"), ("d", "(−7) ÷ 0")])}
{enlace(n, t("divide", "dividir"), t("dividing integers", "la división de enteros"), t("Divide with the same sign rule and check by multiplying.", "Divida con la misma regla de los signos y compruebe multiplicando."))}'''

    s4 = f'''<p>{t("Many expressions mix adding, subtracting, multiplying, and dividing integers. For now, with no parentheses and no powers, follow one simple rule: <strong>first multiply and divide, from left to right; then add and subtract, from left to right</strong>. You will study the full order of operations in Topic 3.",
"Muchas expresiones mezclan la suma, la resta, la multiplicación y la división de enteros. Por ahora, sin paréntesis ni potencias, se sigue una regla sencilla: <strong>primero las multiplicaciones y divisiones, de izquierda a derecha; después las sumas y restas, de izquierda a derecha</strong>. El orden completo de las operaciones se estudia en el Tema 3.")}</p>
{ejemplo(t("Example: (−4) × 3 + (−10) ÷ 2", "Ejemplo: (−4) × 3 + (−10) ÷ 2"),
  [("1", t("Step 1.", "Paso 1."), t("The multiplication: (−4) × 3 = −12.", "La multiplicación: (−4) × 3 = −12.")),
   ("2", t("Step 2.", "Paso 2."), t("The division: (−10) ÷ 2 = −5.", "La división: (−10) ÷ 2 = −5.")),
   ("3", t("Step 3.", "Paso 3."), t("Now there is only an addition: −12 + (−5) = −17.", "Queda solo una suma: −12 + (−5) = −17.")),
   ("✓", t("Result.", "Resultado."), "(−4) × 3 + (−10) ÷ 2 = <strong>−17</strong>")])}
{caja("ojo", t("The most common mistake", "El error más común"), t("<p>Working from left to right without looking at the operations. In the example, adding −4 and 3 first would give a wrong answer. Multiplying and dividing come <strong>first</strong>.</p>",
"<p>Resolver de izquierda a derecha sin mirar las operaciones. En el ejemplo, sumar primero −4 y 3 daría un resultado incorrecto. La multiplicación y la división van <strong>primero</strong>.</p>"))}
{calc(t("The calculator knows the order", "La calculadora conoce el orden"), t(f"""<p>The calculator follows the same order. For (−4) × 3 + (−10) ÷ 2, press {T("(−)")} {T("4")} {T("×")} {T("3")} {T("+")} {T("(−)")} {T("1")}{T("0")} {T("÷")} {T("2")} {T("enter")}. The screen shows −17. Solve it on paper first, then check.</p>""",
f"""<p>La calculadora sigue el mismo orden. Para (−4) × 3 + (−10) ÷ 2, pulse {T("(−)")} {T("4")} {T("×")} {T("3")} {T("+")} {T("(−)")} {T("1")}{T("0")} {T("÷")} {T("2")} {T("enter")}. La pantalla muestra −17. Resuélvalo primero en papel y después compruebe.</p>"""))}
{practica("p6", t("Practice 6 — Four operations", "Práctica 6 — Las cuatro operaciones"), t("What is (−5) × 4 + 6?", "¿Cuánto es (−5) × 4 + 6?"),
          [("a", "−14"), ("b", "−50"), ("c", "26"), ("d", "−26")])}
{enlace(n, t("four-operations", "cuatro-operaciones"), t("expressions with the four operations", "expresiones con las cuatro operaciones"), t("Solve step by step: first multiply and divide, then add and subtract.", "Resuelva paso a paso: primero multiplicar y dividir, después sumar y restar."))}'''

    s5 = f'''<p>{t("You multiply when an amount with a sign <strong>repeats</strong>, and you divide when it is <strong>shared</strong> into equal parts. A loss, a drop, or a debt has a negative sign.",
"Se multiplica cuando una cantidad con signo <strong>se repite</strong>, y se divide cuando <strong>se reparte</strong> en partes iguales. Una pérdida, un descenso o una deuda llevan signo negativo.")}</p>
{ejemplo(t("Example: a dropping temperature", "Ejemplo: una temperatura que baja"),
  [("1", t("The problem.", "El problema."), t("The temperature in a freezer room drops 3 °F every hour. How much has it changed after 5 hours?", "La temperatura de una cámara frigorífica baja 3 °F cada hora. ¿Cuánto ha cambiado después de 5 horas?")),
   ("2", t("The signs.", "Los signos."), t("\"Drops 3 °F\" is −3 per hour, and it repeats 5 times: (−3) × 5.", "«Baja 3 °F» es −3 por hora, y se repite 5 veces: (−3) × 5.")),
   ("✓", t("Result.", "Resultado."), t("Different signs, negative: −15. The temperature dropped 15 °F, a change of <strong>−15 °F</strong>.", "Signos distintos, negativo: −15. La temperatura bajó 15 °F, un cambio de <strong>−15 °F</strong>."))])}
{ejemplo(t("Example: a shared loss", "Ejemplo: una pérdida repartida"),
  [("1", t("The problem.", "El problema."), t("A small business lost a total of $84 in 7 days, the same amount each day. What was the change each day?", "Un pequeño negocio perdió en total $84 en 7 días, la misma cantidad cada día. ¿Cuál fue el cambio de cada día?")),
   ("2", t("The signs.", "Los signos."), t("The total loss is −84, shared among 7 days: (−84) ÷ 7.", "La pérdida total es −84, repartida en 7 días: (−84) ÷ 7.")),
   ("✓", t("Result.", "Resultado."), t("Different signs, negative: <strong>−$12</strong> a day, a loss of $12 each day.", "Signos distintos, negativo: <strong>−$12</strong> por día, una pérdida de $12 cada día."))])}
{practica("p7", t("Practice 7 — A diver", "Práctica 7 — Un buzo"), t("A diver goes down 6 feet each minute from the surface. Where is the diver after 4 minutes, compared with the surface?", "Un buzo baja 6 pies cada minuto desde la superficie. ¿Dónde está después de 4 minutos, respecto de la superficie?"),
          [("a", t("24 feet", "24 pies")), ("b", t("−10 feet", "−10 pies")), ("c", t("−2 feet", "−2 pies")), ("d", t("−24 feet", "−24 pies"))])}
{enlace(n, t("real-life", "contexto"), t("real-life problems", "problemas de la vida real"), t("Solve problems where an amount with a sign repeats or is shared.", "Resuelva problemas en que una cantidad con signo se repite o se reparte."))}
{enlace(n, t("topic-check", "comprobacion"), t("Topic 1 check", "comprobación del Tema 1"), t("When you finish the three lessons, mix all four operations with integers.", "Cuando termine las tres lecciones, mezcle las cuatro operaciones con enteros."))}'''

    secciones = [("s-" + t("signs", "signos"), t("The sign rule for multiplying", "La regla de los signos en la multiplicación"), s1),
                 ("s-" + t("why", "por-que"), t("Why is a negative times a negative positive?", "¿Por qué negativo por negativo da positivo?"), s2),
                 ("s-" + t("divide", "dividir"), t("Dividing integers", "La división de enteros"), s3),
                 ("s-" + t("four-operations", "cuatro-operaciones"), t("Expressions with the four operations", "Expresiones con las cuatro operaciones"), s4),
                 ("s-" + t("real-life", "contexto"), t("Real-life problems", "Problemas de la vida real"), s5)]

    lesson = {"next": t("Lesson 2.1", "Lección 2.1"), "review": t("sections 1, 3, and 4", "las secciones 1, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The value 40 is right. The signs are different: what sign does the product get?", "El valor 40 está bien. Los signos son distintos: ¿qué signo lleva el producto?"),
                                   "c": t("You added. This is a multiplication: 8 × 5.", "Sumó. Esto es una multiplicación: 8 × 5."),
                                   "d": t("You added. This is a multiplication: 8 × 5.", "Sumó. Esto es una multiplicación: 8 × 5.")},
             "right": t("8 × 5 = 40, and different signs give a negative product: −40.", "8 × 5 = 40, y signos distintos dan producto negativo: −40."),
             "solution": t("Multiply the absolute values: 8 × 5 = 40. Different signs give a negative product: (−8) × 5 = −40.", "Se multiplican los valores absolutos: 8 × 5 = 40. Signos distintos dan producto negativo: (−8) × 5 = −40.")},
      "p2": {"ok": "a", "hints": {"b": t("Both factors are negative: same signs. What sign does the product get?", "Los dos factores son negativos: signos iguales. ¿Qué signo lleva el producto?"),
                                   "c": t("−13 is what you get when you add. This is a multiplication.", "−13 es lo que da la suma. Esto es una multiplicación."),
                                   "d": t("This is a multiplication: 6 × 7.", "Esto es una multiplicación: 6 × 7.")},
             "right": t("6 × 7 = 42, and same signs give a positive product.", "6 × 7 = 42, y signos iguales dan producto positivo."),
             "solution": t("6 × 7 = 42. Both factors are negative (same signs), so the product is positive: 42.", "6 × 7 = 42. Los dos factores son negativos (signos iguales), así que el producto es positivo: 42.")},
      "p3": {"ok": "c", "hints": {"a": t("Look at the change: each time, the product goes up 3. What comes 3 more than 0?", "Mire el cambio: cada vez, el producto aumenta 3. ¿Qué número es 3 más que 0?"),
                                   "b": t("0 is the product before. The pattern keeps going up by 3.", "0 es el producto anterior. El patrón sigue aumentando de 3 en 3."),
                                   "d": t("The products go −3, 0, …: they go up by 3 each time.", "Los productos van −3, 0, …: aumentan de 3 en 3.")},
             "right": t("−3, 0, 3: each product goes up 3. So (−1) × (−3) = 3.", "−3, 0, 3: cada producto aumenta 3. Así, (−1) × (−3) = 3."),
             "solution": t("From −3 to 0 the product goes up 3. Going up 3 more gives 3, so (−1) × (−3) = 3: a negative times a negative is positive.", "De −3 a 0 el producto aumenta 3. Si aumenta 3 más, da 3; así, (−1) × (−3) = 3: negativo por negativo da positivo.")},
      "p4": {"ok": "c", "hints": {"a": t("The value 8 is right. The signs are different: what sign does the quotient get?", "El valor 8 está bien. Los signos son distintos: ¿qué signo lleva el cociente?"),
                                   "b": t("You added. This is a division: 48 ÷ 6.", "Sumó. Esto es una división: 48 ÷ 6."),
                                   "d": t("You subtracted. This is a division: 48 ÷ 6.", "Restó. Esto es una división: 48 ÷ 6.")},
             "right": t("48 ÷ 6 = 8, and different signs give a negative quotient: −8.", "48 ÷ 6 = 8, y signos distintos dan cociente negativo: −8."),
             "solution": t("48 ÷ 6 = 8. Different signs give a negative quotient: −8. Check: (−8) × 6 = −48.", "48 ÷ 6 = 8. Signos distintos dan cociente negativo: −8. Compruebe: (−8) × 6 = −48.")},
      "p5": {"ok": "d", "hints": {"a": t("0 ÷ (−7) = 0, because 0 × (−7) = 0. It has an answer.", "0 ÷ (−7) = 0, porque 0 × (−7) = 0. Tiene respuesta."),
                                   "b": t("Any number times 0 is 0. It has an answer.", "Cualquier número por 0 da 0. Tiene respuesta."),
                                   "c": t("0 − 7 = −7. It has an answer.", "0 − 7 = −7. Tiene respuesta.")},
             "right": t("You cannot divide by zero: no number times 0 gives −7.", "No se puede dividir entre cero: ningún número por 0 da −7."),
             "solution": t("(−7) ÷ 0 would need a number that times 0 gives −7, and there is none. A division by zero is undefined.", "(−7) ÷ 0 necesitaría un número que multiplicado por 0 diera −7, y no lo hay. Una división entre cero no está definida.")},
      "p6": {"ok": "a", "hints": {"b": t("You added −5 and 4 first. Multiply first: (−5) × 4.", "Sumó primero −5 y 4. Primero se multiplica: (−5) × 4."),
                                   "c": t("Check the sign of (−5) × 4: different signs.", "Revise el signo de (−5) × 4: signos distintos."),
                                   "d": t("(−5) × 4 = −20. Now add 6: −20 + 6.", "(−5) × 4 = −20. Ahora sume 6: −20 + 6.")},
             "right": t("(−5) × 4 = −20, and −20 + 6 = −14.", "(−5) × 4 = −20, y −20 + 6 = −14."),
             "solution": t("First the multiplication: (−5) × 4 = −20. Then the addition: −20 + 6 = −14.", "Primero la multiplicación: (−5) × 4 = −20. Después la suma: −20 + 6 = −14.")},
      "p7": {"ok": "d", "hints": {"a": t("The value 24 is right, but the diver goes down: below the surface is negative.", "El valor 24 está bien, pero el buzo baja: bajo la superficie es negativo."),
                                   "b": t("−6 and 4 were added. Going down 6 feet each minute for 4 minutes repeats −6 four times.", "Se sumaron −6 y 4. Bajar 6 pies cada minuto durante 4 minutos repite −6 cuatro veces."),
                                   "c": t("−6 and 4 were added. Going down 6 feet each minute for 4 minutes repeats −6 four times.", "Se sumaron −6 y 4. Bajar 6 pies cada minuto durante 4 minutos repite −6 cuatro veces.")},
             "right": t("(−6) × 4 = −24: 24 feet below the surface.", "(−6) × 4 = −24: 24 pies bajo la superficie."),
             "solution": t("Going down is −6 each minute, 4 times: (−6) × 4 = −24. The diver is 24 feet below the surface.", "Bajar es −6 cada minuto, 4 veces: (−6) × 4 = −24. El buzo está 24 pies bajo la superficie.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The value 42 is right. Both factors are negative: same signs.", "El valor 42 está bien. Los dos factores son negativos: signos iguales."),
                                 "b": t("−13 is what you get when you add. This is a multiplication.", "−13 es lo que da la suma. Esto es una multiplicación."),
                                 "d": t("This is a multiplication: 7 × 6.", "Esto es una multiplicación: 7 × 6.")},
            "solution": t("7 × 6 = 42, and same signs give a positive product: 42.", "7 × 6 = 42, y signos iguales dan producto positivo: 42.")},
      "B": {"ok": "a", "hints": {"b": t("The value 36 is right. The signs are different.", "El valor 36 está bien. Los signos son distintos."),
                                 "c": t("You added. This is a multiplication.", "Sumó. Esto es una multiplicación."),
                                 "d": t("You subtracted. This is a multiplication.", "Restó. Esto es una multiplicación.")},
            "solution": t("9 × 4 = 36, and different signs give a negative product: −36.", "9 × 4 = 36, y signos distintos dan producto negativo: −36.")},
      "C": {"ok": "d", "hints": {"a": t("The value 5 is right. Both numbers are negative: same signs.", "El valor 5 está bien. Los dos números son negativos: signos iguales."),
                                 "b": t("You added. This is a division: 45 ÷ 9.", "Sumó. Esto es una división: 45 ÷ 9."),
                                 "c": t("You subtracted. This is a division: 45 ÷ 9.", "Restó. Esto es una división: 45 ÷ 9.")},
            "solution": t("45 ÷ 9 = 5, and same signs give a positive quotient: 5.", "45 ÷ 9 = 5, y signos iguales dan cociente positivo: 5.")},
      "E": {"ok": "b", "hints": {"a": t("Check the division: (−10) ÷ 2 = −5. Then −12 + (−5).", "Revise la división: (−10) ÷ 2 = −5. Después −12 + (−5)."),
                                 "c": t("You worked from left to right. Multiply and divide first, then add: −12 + (−5).", "Resolvió de izquierda a derecha. Primero multiplique y divida, después sume: −12 + (−5)."),
                                 "d": t("The value 17 is right. Two negatives add up to a negative.", "El valor 17 está bien. Dos negativos suman un negativo.")},
            "solution": t("(−4) × 3 = −12 and (−10) ÷ 2 = −5. Then −12 + (−5) = −17.", "(−4) × 3 = −12 y (−10) ÷ 2 = −5. Después −12 + (−5) = −17.")},
      "D": {"ok": "b", "hints": {"a": t("The value 7 is right. The signs are different.", "El valor 7 está bien. Los signos son distintos."),
                                 "c": t("You subtracted. This is a division: 56 ÷ 8.", "Restó. Esto es una división: 56 ÷ 8."),
                                 "d": t("You added. This is a division: 56 ÷ 8.", "Sumó. Esto es una división: 56 ÷ 8.")},
            "solution": t("56 ÷ 8 = 7, and different signs give a negative quotient: −7.", "56 ÷ 8 = 7, y signos distintos dan cociente negativo: −7.")},
      "F": {"ok": "a", "hints": {"b": t("Check the sign of 20 ÷ (−4): different signs, so −5. Then −5 − 3.", "Revise el signo de 20 ÷ (−4): signos distintos, así que −5. Después −5 − 3."),
                                 "c": t("20 ÷ (−4) = −5. Now subtract 3: −5 − 3 = −5 + (−3).", "20 ÷ (−4) = −5. Ahora reste 3: −5 − 3 = −5 + (−3)."),
                                 "d": t("Divide first: 20 ÷ (−4). Then subtract 3.", "Primero divida: 20 ÷ (−4). Después reste 3.")},
            "solution": t("20 ÷ (−4) = −5. Then −5 − 3 = −5 + (−3) = −8.", "20 ÷ (−4) = −5. Después −5 − 3 = −5 + (−3) = −8.")},
      "G": {"ok": "c", "hints": {"a": t("The value 15 is right, but the temperature drops: the change is negative.", "El valor 15 está bien, pero la temperatura baja: el cambio es negativo."),
                                 "b": t("The drop repeats 5 times: multiply (−3) × 5.", "El descenso se repite 5 veces: multiplique (−3) × 5."),
                                 "d": t("The drop repeats 5 times: multiply (−3) × 5.", "El descenso se repite 5 veces: multiplique (−3) × 5.")},
            "solution": t("(−3) × 5 = −15: the temperature changed −15 °F.", "(−3) × 5 = −15: la temperatura cambió −15 °F.")},
      "H": {"ok": "d", "hints": {"a": t("0 ÷ 12 = 0, but this is (−12) ÷ 0. What number times 0 gives −12?", "0 ÷ 12 = 0, pero esto es (−12) ÷ 0. ¿Qué número por 0 da −12?"),
                                 "b": t("Check it with a multiplication: −12 × 0 = 0, not −12.", "Compruébelo con una multiplicación: −12 × 0 = 0, no −12."),
                                 "c": t("Check it with a multiplication: 12 × 0 = 0, not −12.", "Compruébelo con una multiplicación: 12 × 0 = 0, no −12.")},
            "solution": t("No number times 0 gives −12, so (−12) ÷ 0 is undefined. You cannot divide by zero.", "Ningún número por 0 da −12, así que (−12) ÷ 0 no está definida. No se puede dividir entre cero.")}
     }}

    quiz = [
     ("A", t("What is (−7) × (−6)?", "¿Cuánto es (−7) × (−6)?"), [("a", "−42"), ("b", "−13"), ("c", "42"), ("d", "13")]),
     ("B", t("What is 9 × (−4)?", "¿Cuánto es 9 × (−4)?"), [("a", "−36"), ("b", "36"), ("c", "5"), ("d", "13")]),
     ("C", t("What is (−45) ÷ (−9)?", "¿Cuánto es (−45) ÷ (−9)?"), [("a", "−5"), ("b", "−54"), ("c", "−36"), ("d", "5")]),
     ("D", t("What is (−56) ÷ 8?", "¿Cuánto es (−56) ÷ 8?"), [("a", "7"), ("b", "−7"), ("c", "−64"), ("d", "−48")]),
     ("E", t("What is (−4) × 3 + (−10) ÷ 2?", "¿Cuánto es (−4) × 3 + (−10) ÷ 2?"), [("a", "−7"), ("b", "−17"), ("c", "−11"), ("d", "17")]),
     ("F", t("What is 20 ÷ (−4) − 3?", "¿Cuánto es 20 ÷ (−4) − 3?"), [("a", "−8"), ("b", "2"), ("c", "−2"), ("d", "−20")]),
     ("G", t("The temperature in a freezer room drops 3 °F every hour. What is the change in temperature after 5 hours?", "La temperatura de una cámara frigorífica baja 3 °F cada hora. ¿Cuál es el cambio de temperatura después de 5 horas?"), [("a", "15 °F"), ("b", "2 °F"), ("c", "−15 °F"), ("d", "−8 °F")]),
     ("H", t("What is (−12) ÷ 0?", "¿Cuánto es (−12) ÷ 0?"), [("a", "0"), ("b", "−12"), ("c", "12"), ("d", t("It is undefined.", "No está definida."))])]

    return B.pagina_leccion(n, 1, t(*TEMA),
        t("Multiplying and dividing integers; applications", "Multiplicación y división de enteros; aplicaciones"),
        t("One sign rule for multiplying and dividing, why it works, and problems that use all four operations with integers.", "Una sola regla de los signos para multiplicar y dividir, por qué funciona, y problemas con las cuatro operaciones con enteros."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Multiply and divide</strong> integers with the sign rule.", "<strong>Multiplicar y dividir</strong> enteros con la regla de los signos."),
         t("<strong>Explain</strong> with a pattern why a negative times a negative is positive.", "<strong>Explicar</strong> con un patrón por qué negativo por negativo da positivo."),
         t("<strong>Recognize</strong> that a division by zero is undefined.", "<strong>Reconocer</strong> que una división entre cero no está definida."),
         t("<strong>Solve</strong> expressions with the four operations: first multiply and divide, then add and subtract.", "<strong>Resolver</strong> expresiones con las cuatro operaciones: primero multiplicar y dividir, después sumar y restar."),
         t("<strong>Use</strong> multiplying and dividing integers to solve real-life problems.", "<strong>Usar</strong> la multiplicación y la división de enteros para resolver problemas de la vida real.")],
        secciones,
        (t("Write and solve ten products and quotients of integers: predict the sign before you calculate, and check each division with a multiplication. Then write and solve five expressions that use all four operations, step by step.",
           "Escriba y resuelva diez productos y cocientes de enteros: prediga el signo antes de calcular y compruebe cada división con una multiplicación. Después escriba y resuelva, paso a paso, cinco expresiones con las cuatro operaciones."),
         t("Write three problems from your life where an amount with a sign repeats or is shared: a temperature that drops every hour, a debt paid in equal payments, a price that goes down each week. Solve each one and explain the sign of the answer.",
           "Escriba tres problemas de su vida en que una cantidad con signo se repita o se reparta: una temperatura que baja cada hora, una deuda pagada en cuotas iguales, un precio que baja cada semana. Resuelva cada uno y explique el signo del resultado.")),
        quiz,
        t("Self-check checklist for multiplying and dividing integers", "Lista de autoevaluación de la multiplicación y la división de enteros"),
        t("Self-check checklist: skills for multiplying and dividing integers", "Lista de autoevaluación: destrezas de la multiplicación y la división de enteros"),
        [(t("The sign rule for multiplying", "La regla de los signos en la multiplicación"), t("I use the rule every time and can explain it with the pattern.", "Aplico la regla siempre y sé explicarla con el patrón."), t("I use the rule with an occasional sign mistake.", "Aplico la regla con algún error de signo."), t("I do not know when the product is positive or negative.", "No sé cuándo el producto es positivo o negativo.")),
         (t("The sign rule for dividing", "La regla de los signos en la división"), t("I divide with the right sign and check by multiplying.", "Divido con el signo correcto y compruebo multiplicando."), t("I divide, but I make some sign mistakes.", "Divido, pero cometo algunos errores de signo."), t("I do not see that the rule is the same as for multiplying.", "No veo que la regla es la misma que la de la multiplicación.")),
         (t("Expressions with four operations", "Expresiones con cuatro operaciones"), t("I multiply and divide first, and I can explain the order.", "Multiplico y divido primero, y sé explicar el orden."), t("I follow the order when I have an example to look at.", "Sigo el orden cuando tengo un ejemplo a la vista."), t("I work from left to right without looking at the operations.", "Resuelvo de izquierda a derecha sin mirar las operaciones.")),
         (t("Real-life problems", "Problemas de la vida real"), t("I choose the operation and explain the sign of the answer.", "Elijo la operación y explico el signo del resultado."), t("I set up the operation, but I get the sign wrong sometimes.", "Planteo la operación, pero a veces me equivoco en el signo."), t("I do not see which operation the situation needs.", "No veo qué operación necesita la situación."))],
        t("<p>You finished Topic 1. You can now add, subtract, multiply, and divide integers, and use them to solve real problems. Before you go on, do the <strong>Topic 1 check</strong> on the practice page.</p>\n<p>In <strong>Lesson 2.1 · Fractions with negative signs</strong> you will use the same sign rules with fractions. Then, in the rest of Topic 2, you will work with powers and square roots.</p>",
          "<p>Terminó el Tema 1. Ya sabe sumar, restar, multiplicar y dividir enteros, y usarlos para resolver problemas reales. Antes de seguir, haga la <strong>comprobación del Tema 1</strong> en la página de práctica.</p>\n<p>En la <strong>Lección 2.1 · Fracciones complejas con coeficientes negativos</strong> usará las mismas reglas de los signos con fracciones. Después, en el resto del Tema 2, trabajará con potencias y raíces cuadradas.</p>"),
        ("2-1", ("", t("Lesson 2.1 · Fractions with negative signs", "Lección 2.1 · Fracciones complejas con coeficientes negativos"))),
        [(t("product", "producto"), t("The answer to a multiplication.", "El resultado de una multiplicación.")),
         (t("quotient", "cociente"), t("The answer to a division.", "El resultado de una división.")),
         (t("factor", "factor"), t("Each of the numbers you multiply.", "Cada uno de los números que se multiplican.")),
         (t("sign rule", "regla de los signos"), t("To multiply or divide: same signs give a positive answer; different signs give a negative answer.", "Para multiplicar o dividir: signos iguales dan resultado positivo; signos distintos, negativo.")),
         (t("undefined", "no definida"), t("An expression with no answer, like a division by zero.", "Una expresión que no tiene resultado, como una división entre cero.")),
         (t("order of operations", "orden de las operaciones"), t("The order to solve an expression. For now: multiply and divide first, then add and subtract.", "El orden para resolver una expresión. Por ahora: primero multiplicar y dividir, después sumar y restar."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "calcula": "Calculate {s}.",
  "iguales": "Same signs → positive.", "distintos": "Different signs → negative.",
  "explica": "{x} {o} {y} = {r}. ", "comprueba": " Check: {c} = {a}.",
  "pistaMult": "First decide the sign: are the two signs the same or different?",
  "cap": "Products of a list that goes down by one, times {m}",
  "cMult": "Multiplication", "cProd": "Product", "cCambio": "Change from the row before", "subio": "went up {d}",
  "pt1": "Each time the first factor goes down 1, the product goes up {d}. What should happen in the next row?",
  "pt2": "0 × {pm} = 0: the pattern reaches zero, going up {d} again.",
  "pt3": "To keep going up {d}, the products have to become positive: (−1) × {pm} = {r}. That is why <strong>a negative times a negative is positive</strong>.",
  "noDef": "It is undefined", "expCero0": "Zero times any number, or zero divided by any number that is not zero, is 0.",
  "expCeroX": "No number times 0 gives {v}: you cannot divide by zero, so it is undefined.",
  "pistaCero": "Check it with a multiplication. What number times the divisor gives the dividend?",
  "primeroLa": "First the {op}: {a} {o} {b} = {r}. Now you have {q}.", "despuesLa": "Then the {op}: {a} {o} {b} = {r}.",
  "mult": "multiplication", "div": "division", "suma": "addition", "resta": "subtraction",
  "resultado": "Answer: {e} = {r}",
  "resuelve": "Solve {e}.", "izqDer": "It looks like you worked from left to right without the order: multiply and divide first.",
  "c1": "The temperature in a freezer room drops {a} °F every hour. How much has it changed after {b} hours? (A drop is negative.)", "s1": "{pa} × {b} = {r} °F.",
  "c2": "A store lost a total of ${t} in {b} days, the same amount each day. What was the change each day, in dollars?", "s2": "{pt} ÷ {b} = {r}: a loss of ${a} a day.",
  "c3": "A diver goes down {a} feet each minute from the surface. Where is the diver after {b} minutes? (Below the surface is negative.)", "s3": "{pa} × {b} = {r} feet.",
  "c4": "The price of a stock goes down ${a} each day for {b} days. What is the total change in price, in dollars?", "s4": "{pa} × {b} = {r}.",
  "c5": "The low temperatures for {n} days were {l} °F. What was the mean (average), in °F?", "s5": "Sum: {s}; ÷ {n} = {r} °F.",
  "c6": "{b} friends share a debt of ${t} equally. What change does it mean for each one, in dollars?", "s6": "{pt} ÷ {b} = {r}.",
  "pistaCtx": "The value is right, but a loss, a drop, or a debt has a negative sign.",
  "mezcla": "Calculate {e}."
 },
 "es": {
  "calcula": "Calcule {s}.",
  "iguales": "Signos iguales → positivo.", "distintos": "Signos distintos → negativo.",
  "explica": "{x} {o} {y} = {r}. ", "comprueba": " Comprobación: {c} = {a}.",
  "pistaMult": "Primero decida el signo: ¿los dos signos son iguales o distintos?",
  "cap": "Productos de una lista que baja de uno en uno por {m}",
  "cMult": "Multiplicación", "cProd": "Producto", "cCambio": "Cambio respecto de la fila anterior", "subio": "aumentó {d}",
  "pt1": "Cada vez que el primer factor baja 1, el producto aumenta {d}. ¿Qué debería pasar en la fila siguiente?",
  "pt2": "0 × {pm} = 0: el patrón llega al cero, aumentando {d} otra vez.",
  "pt3": "Para seguir aumentando {d}, los productos tienen que volverse positivos: (−1) × {pm} = {r}. Por eso <strong>negativo por negativo da positivo</strong>.",
  "noDef": "No está definida", "expCero0": "Cero por cualquier número, o cero entre cualquier número distinto de cero, da 0.",
  "expCeroX": "Ningún número multiplicado por 0 da {v}: no se puede dividir entre cero, así que no está definida.",
  "pistaCero": "Compruébelo con una multiplicación. ¿Qué número multiplicado por el divisor da el dividendo?",
  "primeroLa": "Primero la {op}: {a} {o} {b} = {r}. Queda {q}.", "despuesLa": "Después la {op}: {a} {o} {b} = {r}.",
  "mult": "multiplicación", "div": "división", "suma": "suma", "resta": "resta",
  "resultado": "Resultado: {e} = {r}",
  "resuelve": "Resuelva {e}.", "izqDer": "Parece que resolvió de izquierda a derecha sin respetar el orden: primero se multiplica y se divide.",
  "c1": "La temperatura de una cámara frigorífica baja {a} °F cada hora. ¿Cuánto ha cambiado después de {b} horas? (Un descenso es negativo.)", "s1": "{pa} × {b} = {r} °F.",
  "c2": "Una tienda perdió en total ${t} en {b} días, la misma cantidad cada día. ¿Cuál fue el cambio de cada día, en dólares?", "s2": "{pt} ÷ {b} = {r}: una pérdida de ${a} por día.",
  "c3": "Un buzo baja {a} pies cada minuto desde la superficie. ¿Dónde está después de {b} minutos? (Bajo la superficie es negativo.)", "s3": "{pa} × {b} = {r} pies.",
  "c4": "El precio de una acción baja ${a} cada día durante {b} días. ¿Cuál es el cambio total del precio, en dólares?", "s4": "{pa} × {b} = {r}.",
  "c5": "Las temperaturas mínimas de {n} días fueron {l} °F. ¿Cuál fue la media (promedio), en °F?", "s5": "Suma: {s}; ÷ {n} = {r} °F.",
  "c6": "{b} amigos comparten por igual una deuda de ${t}. ¿Qué cambio representa para cada uno, en dólares?", "s6": "{pt} ÷ {b} = {r}.",
  "pistaCtx": "El valor está bien, pero una pérdida, un descenso o una deuda llevan signo negativo.",
  "mezcla": "Calcule {e}."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function prod(a, b){ return par(a) + " × " + par(b); }
function coc(a, b){ return par(a) + " ÷ " + par(b); }
function explicaSigno(a, b, o){
  var r = o === "×" ? a * b : a / b;
  return F(TXT.explica, { x: Math.abs(a), o: o, y: Math.abs(b), r: Math.abs(r) }) + ((a < 0) === (b < 0) ? TXT.iguales : TXT.distintos);
}

/* ============ MODULES 1 and 3 · two steps ============ */
function genMult(){ var a = azarEnt(-12, 12, true), b = azarEnt(-12, 12, true); return { enun: F(TXT.calcula, { s: prod(a, b) }), res: a * b, explica: explicaSigno(a, b, "×"), pista: TXT.pistaMult }; }
function genDiv(){ var q = azarEnt(-12, 12, true), b = azarEnt(-9, 9, true), a = q * b; return { enun: F(TXT.calcula, { s: coc(a, b) }), res: q, explica: explicaSigno(a, b, "÷") + F(TXT.comprueba, { c: prod(q, b), a: ent(a) }), pista: TXT.pistaMult }; }
function genCero(){
  var k = aleatorio(2, 30), tipo = aleatorio(1, 4), v = elige([k, -k]), enun, r;
  var o = [{ html: "0", clave: "0" }, { html: ent(v), clave: "v" }, { html: ent(-v), clave: "w" }, { html: TXT.noDef, clave: "x" }];
  if (tipo === 1){ enun = "0 ÷ " + par(v) + " ="; r = "0"; }
  else if (tipo === 2){ enun = par(v) + " ÷ 0 ="; r = "x"; }
  else if (tipo === 3){ enun = par(v) + " × 0 ="; r = "0"; }
  else { enun = "0 × " + par(v) + " ="; r = "0"; }
  var exp = r === "x" ? F(TXT.expCeroX, { v: ent(v) }) : TXT.expCero0;
  return { enun: enun, opciones: o, enOrden: true, correcta: r, pista: TXT.pistaCero, bien: exp, mal: exp };
}

/* ============ MODULE 2 · the pattern ============ */
var PT = { visto: 3 };
function pintaPT(){
  var mm = +$("pt-m").value, filas = [3, 2, 1, 0, -1, -2, -3], d = Math.abs(mm);
  var h = '<caption>' + F(TXT.cap, { m: ent(mm) }) + '</caption><thead><tr><th scope="col">' + TXT.cMult + '</th><th scope="col">' + TXT.cProd + '</th><th scope="col">' + TXT.cCambio + '</th></tr></thead><tbody>';
  filas.slice(0, PT.visto).forEach(function(k, i){
    h += '<tr' + (k < 0 ? ' class="nueva"' : '') + '><td>' + par(k) + ' × ' + par(mm) + '</td><td><strong>' + ent(k * mm) + '</strong></td><td>' + (i === 0 ? "—" : F(TXT.subio, { d: d })) + '</td></tr>';
  });
  $("pt-tabla").innerHTML = h + '</tbody>';
  $("pt-sig").disabled = PT.visto >= filas.length;
  var s = PT.visto <= 3 ? F(TXT.pt1, { d: d }) : (PT.visto === 4 ? F(TXT.pt2, { pm: par(mm), d: d }) : F(TXT.pt3, { d: d, pm: par(mm), r: ent(-mm) }));
  $("pt-salida").innerHTML = '<div class="linea">' + s + '</div>';
}

/* ============ MODULE 4 · four operations ============ */
function exprAzar(){
  var tipo = aleatorio(1, 4), a, b, c, d, q;
  if (tipo === 1){ a = azarEnt(-9, 9, true); b = azarEnt(-9, 9, true); q = azarEnt(-9, 9, true); d = azarEnt(-5, 5, true); c = q * d; return [a, "×", b, "+", c, "÷", d]; }
  if (tipo === 2){ a = azarEnt(-20, 20, true); b = azarEnt(-9, 9, true); c = azarEnt(-9, 9, true); return [a, "−", b, "×", c]; }
  if (tipo === 3){ q = azarEnt(-9, 9, true); b = azarEnt(-6, 6, true); a = q * b; c = azarEnt(-9, 9, true); d = azarEnt(-6, 6, true); return [a, "÷", b, "−", c, "×", d]; }
  a = azarEnt(-15, 15, true); b = azarEnt(-9, 9, true); c = azarEnt(-9, 9, true); d = azarEnt(-15, 15, true); return [a, "+", b, "×", c, "−", d];
}
function expTxt(tk){ return tk.map(function(x, i){ return typeof x === "number" ? (i === 0 ? ent(x) : par(x)) : " " + x + " "; }).join(""); }
function opera(a, o, b){ return o === "×" ? a * b : (o === "÷" ? a / b : (o === "+" ? a + b : a - b)); }
var NOMBRE = { "×": "mult", "÷": "div", "+": "suma", "−": "resta" };
function resuelveExpr(tk){
  var x = tk.slice(), pasos = [];
  for (var i = 1; i < x.length; ){
    if (x[i] === "×" || x[i] === "÷"){ var r = opera(x[i - 1], x[i], x[i + 1]), sig = x.slice(0, i - 1).concat([r], x.slice(i + 2)); pasos.push(F(TXT.primeroLa, { op: TXT[NOMBRE[x[i]]], a: par(x[i - 1]), o: x[i], b: par(x[i + 1]), r: ent(r), q: expTxt(sig) })); x = sig; }
    else i += 2;
  }
  while (x.length > 1){ var r2 = opera(x[0], x[1], x[2]); pasos.push(F(TXT.despuesLa, { op: TXT[NOMBRE[x[1]]], a: ent(x[0]), o: x[1], b: par(x[2]), r: ent(r2) })); x = [r2].concat(x.slice(3)); }
  pasos.push('<span class="veredicto">' + F(TXT.resultado, { e: expTxt(tk), r: ent(x[0]) }) + '</span>');
  return { pasos: pasos, res: x[0] };
}
function izqDer(tk){ var v = tk[0]; for (var i = 1; i < tk.length; i += 2) v = opera(v, tk[i], tk[i + 1]); return v; }
var CU_COLA = [[-4, "×", 3, "+", -10, "÷", 2]], CUS;
function nuevoCU(){ var tk = CU_COLA.length ? CU_COLA.shift() : exprAzar(); $("cu-expr").textContent = expTxt(tk); CUS.carga(resuelveExpr(tk).pasos); }
function genCuatro(){
  var tk = exprAzar(), R = resuelveExpr(tk), p = [], mm = izqDer(tk);
  if (mm !== R.res && mm === Math.round(mm)) p.push({ v: mm, msg: TXT.izqDer });
  return { enun: F(TXT.resuelve, { e: expTxt(tk) }), correcta: String(R.res), solucion: R.pasos.slice(0, -1).join(" "), evalua: numE(R.res, p) };
}

/* ============ MODULE 5 · real life ============ */
function genContexto(){
  var tipo = aleatorio(1, 6), a, b, r, enun, sol;
  if (tipo === 1){ a = aleatorio(2, 6); b = aleatorio(3, 8); r = -a * b; enun = F(TXT.c1, { a: a, b: b }); sol = F(TXT.s1, { pa: par(-a), b: b, r: ent(r) }); }
  else if (tipo === 2){ b = aleatorio(3, 9); a = aleatorio(4, 25); r = -a; enun = F(TXT.c2, { t: com(a * b), b: b }); sol = F(TXT.s2, { pt: par(-a * b), b: b, r: ent(r), a: a }); }
  else if (tipo === 3){ a = aleatorio(3, 12); b = aleatorio(2, 9); r = -a * b; enun = F(TXT.c3, { a: a, b: b }); sol = F(TXT.s3, { pa: par(-a), b: b, r: ent(r) }); }
  else if (tipo === 4){ a = aleatorio(2, 9); b = aleatorio(3, 7); r = -a * b; enun = F(TXT.c4, { a: a, b: b }); sol = F(TXT.s4, { pa: par(-a), b: b, r: ent(r) }); }
  else if (tipo === 5){ var n = aleatorio(3, 5), prom = -aleatorio(2, 9), ts = []; for (var i = 0; i < n - 1; i++) ts.push(prom + aleatorio(-4, 4)); ts.push(prom * n - ts.reduce(function(s, x){ return s + x; }, 0)); r = prom;
    enun = F(TXT.c5, { n: n, l: ts.map(ent).join(", ") }); sol = F(TXT.s5, { s: ent(prom * n), n: n, r: ent(r) }); }
  else { b = aleatorio(2, 6); a = aleatorio(10, 60); r = -a; enun = F(TXT.c6, { b: b, t: com(a * b) }); sol = F(TXT.s6, { pt: par(-a * b), b: b, r: ent(r) }); }
  return { enun: enun, correcta: String(r), solucion: sol, evalua: numE(r, [{ v: -r, msg: TXT.pistaCtx }]) };
}

/* ============ MODULE 6 · Topic 1 check: the four operations mixed ============ */
function genMezcla(){
  var tipo = aleatorio(1, 5), a = azarEnt(-20, 20, true), b = azarEnt(-12, 12, true), r, e, p = [];
  if (tipo === 1){ r = a + b; e = ent(a) + " + " + par(b); if ((a < 0) !== (b < 0)){ var mal = (Math.abs(a) + Math.abs(b)) * (Math.abs(a) > Math.abs(b) ? Math.sign(a) : Math.sign(b)); if (mal !== r) p.push({ v: mal, msg: ES ? "Con signos distintos, en la suma se restan los valores absolutos." : "With different signs, an addition subtracts the absolute values." }); } }
  else if (tipo === 2){ r = a - b; e = ent(a) + " − " + par(b); if (a + b !== r) p.push({ v: a + b, msg: ES ? "Restar " + par(b) + " es sumar " + par(-b) + "." : "Subtracting " + par(b) + " is adding " + par(-b) + "." }); }
  else if (tipo === 3){ a = azarEnt(-12, 12, true); r = a * b; e = par(a) + " × " + par(b); }
  else if (tipo === 4){ var q = azarEnt(-12, 12, true); a = q * b; r = q; e = par(a) + " ÷ " + par(b); }
  else { var tk = exprAzar(), R = resuelveExpr(tk); r = R.res; e = expTxt(tk); var mm = izqDer(tk); if (mm !== r && mm === Math.round(mm)) p.push({ v: mm, msg: TXT.izqDer });
    return { enun: F(TXT.mezcla, { e: e }), correcta: String(r), solucion: R.pasos.slice(0, -1).join(" "), evalua: numE(r, p) }; }
  return { enun: F(TXT.mezcla, { e: e }), correcta: String(r), solucion: e + " = " + ent(r) + ".", evalua: numE(r, p) };
}

/* ============ Start ============ */
creaSignoValor("p1", genMult);
$("pt-m").addEventListener("change", function(){ PT.visto = 3; pintaPT(); });
$("pt-sig").addEventListener("click", function(){ PT.visto++; pintaPT(); });
$("pt-reinicia").addEventListener("click", function(){ PT.visto = 3; pintaPT(); });
pintaPT();
creaSignoValor("p2", genDiv);
creaPracticaOM("p3", genCero);
CUS = pasoAPaso("cu", []);
$("cu-nuevo").addEventListener("click", nuevoCU); nuevoCU();
creaPracticaLibre("p4", genCuatro);
creaPracticaLibre("p5", genContexto);
creaPracticaLibre("p6", genMezcla);
'''

def practica_pagina():
    n = N
    mods = [
     (t("signs", "signos"), t("The sign rule", "La regla de los signos"),
      f'''      <p>{t("To multiply two integers, multiply the absolute values as always. What is new is the sign: <strong>same signs give a positive answer; different signs give a negative answer</strong>.", "Para multiplicar dos enteros, se multiplican los valores absolutos como siempre. Lo nuevo es el signo: <strong>signos iguales dan positivo; signos distintos dan negativo</strong>.")}</p>
      <table class="reglas">
        <caption>{t("The sign rule", "La regla de los signos")}</caption>
        <thead><tr><th scope="col">{t("Factor 1", "Factor 1")}</th><th scope="col">{t("Factor 2", "Factor 2")}</th><th scope="col">{t("Product", "Producto")}</th></tr></thead>
        <tbody>
          <tr><td>{t("positive", "positivo")}</td><td>{t("positive", "positivo")}</td><td>{t("positive (+)", "positivo (+)")}</td></tr>
          <tr><td>{t("negative", "negativo")}</td><td>{t("negative", "negativo")}</td><td>{t("positive (+)", "positivo (+)")}</td></tr>
          <tr><td>{t("positive", "positivo")}</td><td>{t("negative", "negativo")}</td><td>{t("negative (−)", "negativo (−)")}</td></tr>
          <tr><td>{t("negative", "negativo")}</td><td>{t("positive", "positivo")}</td><td>{t("negative (−)", "negativo (−)")}</td></tr>
        </tbody>
      </table>
{B.signo_valor("p1", t("Practice: multiply in two steps", "Practique: multiplicar en dos pasos"))}'''),
     (t("why", "por-que"), t("Why is a negative times a negative positive?", "¿Por qué negativo por negativo da positivo?"),
      f'''      <p>{t("The rule comes from a pattern. Multiply a negative number by a list that goes down by one: each product <strong>goes up</strong> by the same amount. For the pattern to keep going past zero, the products of two negatives have to be positive.", "La regla sale de un patrón. Multiplique un número negativo por una lista que baja de uno en uno: cada producto <strong>aumenta</strong> siempre lo mismo. Para que el patrón siga igual al pasar el cero, los productos de dos negativos tienen que ser positivos.")}</p>
      <h3>{t("Follow the pattern", "Siga el patrón")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="pt-m">{t("Negative number to multiply by", "Número negativo por el que se multiplica")}</label><select id="pt-m"><option value="-2">−2</option><option value="-3">−3</option><option value="-4">−4</option><option value="-5">−5</option></select></div>
        </div>
        <div class="tabla-scroll"><table class="comparar patron" id="pt-tabla"></table></div>
        <div class="fila-btn"><button type="button" class="btn" id="pt-sig">{t("Next row", "Fila siguiente")}</button><button type="button" class="btn-sec" id="pt-reinicia">{t("Start over", "Empezar de nuevo")}</button></div>
        <div class="salida" id="pt-salida" aria-live="polite"></div>
      </div>'''),
     (t("divide", "dividir"), t("Dividing integers", "La división de enteros"),
      f'''      <p>{t("Dividing uses <strong>exactly the same sign rule</strong> as multiplying. And you can check it by multiplying: if (−45) ÷ (−9) = 5, then 5 × (−9) must be −45.", "La división usa <strong>exactamente la misma regla de los signos</strong> que la multiplicación. Y se comprueba multiplicando: si (−45) ÷ (−9) = 5, entonces 5 × (−9) debe dar −45.")}</p>
      <div class="caja-atencion"><strong>{t("You cannot divide by zero:", "No se puede dividir entre cero:")}</strong> {t("0 ÷ 5 = 0, but 5 ÷ 0 has no answer, because no number times 0 gives 5. A division by zero is undefined.", "0 ÷ 5 = 0, pero 5 ÷ 0 no tiene respuesta, porque ningún número multiplicado por 0 da 5. Una división entre cero no está definida.")}</div>
{B.signo_valor("p2", t("Practice: divide in two steps", "Practique: dividir en dos pasos"))}
{B.om("p3", t("Practice: what about zero?", "Practique: ¿y el cero?"))}'''),
     (t("four-operations", "cuatro-operaciones"), t("Expressions with the four operations", "Expresiones con las cuatro operaciones"),
      f'''      <p>{t("When the four operations are mixed, <strong>multiply and divide first</strong>, from left to right, and <strong>then add and subtract</strong>, from left to right. You will study the full order in Topic 3.", "Cuando se mezclan las cuatro operaciones, van <strong>primero las multiplicaciones y divisiones</strong>, de izquierda a derecha, y <strong>después las sumas y restas</strong>, de izquierda a derecha. El orden completo se estudia en el Tema 3.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <div class="estado"><span class="grande" id="cu-expr"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="cu-sig"></button><button type="button" class="btn-sec" id="cu-todo">{t("Show all", "Mostrar todo")}</button><button type="button" class="btn-sec" id="cu-nuevo">{t("Another expression", "Otra expresión")}</button></div>
        <div class="pasos" id="cu-pasos" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("The most common mistake:", "El error más común:")}</strong> {t("working from left to right without looking at the operations. In (−4) × 3 + (−10) ÷ 2, the multiplication and the division come first: −12 + (−5) = −17.", "resolver de izquierda a derecha sin mirar las operaciones. En (−4) × 3 + (−10) ÷ 2, la multiplicación y la división van primero: −12 + (−5) = −17.")}</div>
{B.libre_e("p4", t("Practice: solve the expression", "Practique: resolver la expresión"))}'''),
     (t("real-life", "contexto"), t("Real-life problems", "Problemas de la vida real"),
      f'''      <p>{t("Multiply when an amount with a sign <strong>repeats</strong>, and divide when it is <strong>shared</strong> into equal parts. A loss, a drop, or a debt has a negative sign.", "Se multiplica cuando una cantidad con signo <strong>se repite</strong>, y se divide cuando <strong>se reparte</strong> en partes iguales. Una pérdida, un descenso o una deuda llevan signo negativo.")}</p>
{B.libre_e("p5", t("Practice: multiplying and dividing problems", "Practique: problemas de multiplicación y división"))}'''),
     (t("topic-check", "comprobacion"), t("Topic 1 check", "Comprobación del Tema 1"),
      f'''      <p>{t("When you finish the practice for the three lessons, check the whole topic. The exercises mix adding, subtracting, multiplying, and dividing integers. Before you answer, ask yourself: <strong>which operation is it, and which sign rule goes with it?</strong>", "Cuando termine las prácticas de las tres lecciones, compruebe el tema completo. Los ejercicios mezclan la suma, la resta, la multiplicación y la división de enteros. Antes de responder, pregúntese: <strong>¿qué operación es y qué regla de los signos le corresponde?</strong>")}</p>
      <table class="reglas">
        <caption>{t("The two sign rules", "Las dos reglas de los signos")}</caption>
        <thead><tr><th scope="col">{t("Operation", "Operación")}</th><th scope="col">{t("Rule", "Regla")}</th></tr></thead>
        <tbody>
          <tr><td>{t("adding", "suma")}</td><td>{t("same sign: add the absolute values; different signs: subtract them and use the sign of the larger one", "mismo signo: se suman los valores absolutos; signos distintos: se restan y se usa el signo del mayor")}</td></tr>
          <tr><td>{t("subtracting", "resta")}</td><td>{t("add the opposite, then use the rule for adding", "se suma el opuesto y después se usa la regla de la suma")}</td></tr>
          <tr><td>{t("multiplying and dividing", "multiplicación y división")}</td><td>{t("same signs: positive; different signs: negative", "signos iguales: positivo; signos distintos: negativo")}</td></tr>
        </tbody>
      </table>
{B.libre_e("p6", t("Practice: the four operations mixed", "Practique: las cuatro operaciones mezcladas"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 1, t(*TEMA), t("Multiplying and dividing integers; applications", "Multiplicación y división de enteros; aplicaciones"),
        t("Six practice activities on one page. The last one checks the whole topic. The exercises change every time. If you make a mistake, you get a hint and another try.", "Seis actividades de práctica en una sola página. La última comprueba todo el tema. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Multiplicación y división de enteros; aplicaciones")
