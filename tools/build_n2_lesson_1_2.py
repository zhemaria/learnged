"""Level 2 · Lesson 1.2 · Adding and subtracting integers — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import m, p, recta, fichas, ROJO, VERDE, AZUL, GRIS

B.NIVEL = 2
N = "1-2"
TEMA = ("Integers", "Enteros con signo")

def complemento():
    """Tarjeta al interactivo «Tengo y debo» (un solo archivo bilingüe; el idioma va en el enlace)."""
    href = "/math/level-2/tengo-debo.html?lang=" + t("en", "es")
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{t("Open the complement: What I have and what I owe (opens in a new tab)", "Abrir el complemento: Tengo y debo (se abre en una pestaña nueva)")}">
<span class="ei-icono" aria-hidden="true">📘</span>
<span class="ei-cuerpo"><span class="ei-titulo">{t("Complement: What I have and what I owe", "Complemento: Tengo y debo")}</span><span class="ei-sub">{t("Add and subtract with coins (what you have) and debts (what you owe), without memorizing rules. A good start if the signs confuse you.", "Sume y reste con monedas (lo que tiene) y deudas (lo que debe), sin memorizar reglas. Un buen comienzo si los signos lo confunden.")}</span><span class="ei-cta">{t("Open the complement", "Abrir el complemento")} <span aria-hidden="true">›</span></span></span>
</a>'''

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 1.1 you learned two tools: every number has an <strong>opposite</strong>, and the <strong>absolute value</strong> is the distance from zero. Now you will use them to add and subtract integers.",
"En la Lección 1.1 aprendió dos herramientas: cada número tiene un <strong>opuesto</strong>, y el <strong>valor absoluto</strong> es la distancia al cero. Ahora las usará para sumar y restar enteros.")}</p>
<p>{t("You can think of adding as <strong>moving on the number line</strong>. Start at the first number, then move:", "Sumar se puede pensar como un <strong>movimiento en la recta numérica</strong>. Se parte del primer número y se avanza:")}</p>
<ul>
<li>{t("To add a <strong>positive</strong> number, move to the <strong>right</strong>.", "Si se suma un número <strong>positivo</strong>, se avanza hacia la <strong>derecha</strong>.")}</li>
<li>{t("To add a <strong>negative</strong> number, move to the <strong>left</strong>.", "Si se suma un número <strong>negativo</strong>, se avanza hacia la <strong>izquierda</strong>.")}</li>
</ul>
{recta(-8, 8, t("A number line from −8 to 8. An arrow starts at −5 and jumps 8 places to the right, to 3.", "Una recta numérica de −8 a 8. Una flecha parte de −5 y salta 8 lugares hacia la derecha, hasta 3."),
       marcas=[(-5, t("start", "inicio"), GRIS, True), (3, "3", ROJO, True)], saltos=[(-5, 3, "+8", VERDE)], paso=1)}
<p style="text-align:center">{t("−5 + 8: start at −5 and move 8 places to the right. You land on <strong>3</strong>.", "−5 + 8: se parte de −5 y se avanzan 8 lugares hacia la derecha. Se llega a <strong>3</strong>.")}</p>
{recta(-8, 8, t("A number line from −8 to 8. An arrow starts at 2 and jumps 6 places to the left, to −4.", "Una recta numérica de −8 a 8. Una flecha parte de 2 y salta 6 lugares hacia la izquierda, hasta −4."),
       marcas=[(2, t("start", "inicio"), GRIS, True), (-4, "−4", ROJO, True)], saltos=[(2, -4, "−6", ROJO)], paso=1)}
<p style="text-align:center">{t("2 + (−6): start at 2 and move 6 places to the left. You land on <strong>−4</strong>.", "2 + (−6): se parte de 2 y se avanzan 6 lugares hacia la izquierda. Se llega a <strong>−4</strong>.")}</p>
{caja("tip", t("Parentheses", "Los paréntesis"), t("<p>When a negative number comes after a + or − sign, we write it in parentheses so the two signs do not run together: 2 + (−6), not 2 + −6.</p>",
"<p>Cuando un número negativo va después de un signo + o −, se escribe entre paréntesis para que los dos signos no queden pegados: 2 + (−6), no 2 + −6.</p>"))}
{practica("p1", t("Practice 1 — On the number line", "Práctica 1 — En la recta"), t("Start at −3 and add 7. Where do you land?", "Se parte de −3 y se suma 7. ¿Dónde se llega?"),
          [("a", "−10"), ("b", "4"), ("c", "10"), ("d", "−4")])}
{enlace(n, t("add-on-line", "recta-suma"), t("adding on the number line", "sumar en la recta numérica"), t("Choose the starting point and the number to add, and see the jump on the line.", "Elija el punto de partida y el número que se suma, y vea el recorrido en la recta."))}'''

    s2 = f'''<p>{t("Another way to see addition is with <strong>two-color counters</strong>. A yellow counter (+) is worth <strong>+1</strong>, and a red counter (−) is worth <strong>−1</strong>. One yellow and one red together make a <strong>zero pair</strong>, because +1 + (−1) = 0.",
"Otra forma de ver la suma es con <strong>fichas de dos colores</strong>. Una ficha amarilla (+) vale <strong>+1</strong> y una ficha roja (−) vale <strong>−1</strong>. Una amarilla y una roja juntas forman un <strong>par cero</strong>, porque +1 + (−1) = 0.")}</p>
{fichas(-6, 4, t("Two rows of counters: 6 red counters for −6 and 4 yellow counters for 4.", "Dos filas de fichas: 6 fichas rojas para −6 y 4 fichas amarillas para 4."))}
{ejemplo(t("Example: −6 + 4 with counters", "Ejemplo: −6 + 4 con fichas"),
  [("1", t("Step 1.", "Paso 1."), t("Put down 6 red counters (−6) and 4 yellow counters (+4).", "Se colocan 6 fichas rojas (−6) y 4 fichas amarillas (+4).")),
   ("2", t("Step 2.", "Paso 2."), t("Match each yellow counter with a red one. That makes 4 zero pairs. Take them away: they are worth 0.", "Se empareja cada ficha amarilla con una roja. Se forman 4 pares cero. Se retiran: valen 0.")),
   ("3", t("Step 3.", "Paso 3."), t("2 red counters are left without a partner.", "Quedan 2 fichas rojas sin pareja.")),
   ("✓", t("Result.", "Resultado."), "−6 + 4 = <strong>−2</strong>")])}
{fichas(-6, 4, t("The same counters after matching: 4 zero pairs are crossed out, and 2 red counters are left.", "Las mismas fichas después de emparejarlas: 4 pares cero tachados y quedan 2 fichas rojas."), pares=True)}
{caja("tip", t("Why it works", "Por qué funciona"), t("<p>Zero pairs do not change the total, so you can take them away. What is <strong>left</strong> is the answer: if red counters are left, the answer is negative; if yellow counters are left, it is positive.</p>",
"<p>Los pares cero no cambian el total, así que se pueden retirar. Lo que <strong>queda</strong> es el resultado: si quedan fichas rojas, es negativo; si quedan amarillas, es positivo.</p>"))}
{practica("p2", t("Practice 2 — Counters", "Práctica 2 — Fichas"), t("You have 3 yellow counters and 7 red counters. After you take away the zero pairs, what is left?", "Hay 3 fichas amarillas y 7 fichas rojas. Después de retirar los pares cero, ¿qué queda?"),
          [("a", t("4 yellow: +4", "4 amarillas: +4")), ("b", t("10 red: −10", "10 rojas: −10")), ("c", t("4 red: −4", "4 rojas: −4")), ("d", t("nothing: 0", "nada: 0"))])}
{enlace(n, t("counters", "fichas"), t("the counter model", "el modelo de fichas"), t("Make zero pairs with yellow and red counters and see what is left.", "Forme pares cero con fichas amarillas y rojas y descubra qué queda."))}
{complemento()}'''

    s3 = f'''<p>{t("The number line and the counters lead to a rule. With it, you can add without drawing:", "La recta y las fichas llevan a una regla. Con ella se puede sumar sin dibujar:")}</p>
{tabla(t("The rule for adding integers", "La regla de la suma de enteros"), t("The rule for adding integers: what to do with the absolute values and what sign the answer gets", "La regla de la suma de enteros: qué se hace con los valores absolutos y qué signo lleva el resultado"),
       [t("Case", "Caso"), t("What to do with the absolute values", "Qué se hace con los valores absolutos"), t("Sign of the answer", "Signo del resultado")],
       [[t("<strong>Same sign</strong>", "<strong>Mismo signo</strong>"), t("Add them.", "Se suman."), t("The sign they share.", "El signo que comparten.")],
        [t("<strong>Different signs</strong>", "<strong>Signos distintos</strong>"), t("Subtract the smaller from the larger.", "Se resta el menor del mayor."), t("The sign of the number with the larger absolute value.", "El signo del número con mayor valor absoluto.")]])}
{ejemplo(t("Example: same sign: −9 + (−7)", "Ejemplo con el mismo signo: −9 + (−7)"),
  [("1", t("Step 1.", "Paso 1."), t("Both numbers are negative: same sign.", "Los dos son negativos: mismo signo.")),
   ("2", t("Step 2.", "Paso 2."), t("Add the absolute values: 9 + 7 = 16.", "Se suman los valores absolutos: 9 + 7 = 16.")),
   ("3", t("Step 3.", "Paso 3."), t("Keep the sign they share: negative.", "Se conserva el signo común: negativo.")),
   ("✓", t("Result.", "Resultado."), "−9 + (−7) = <strong>−16</strong>")])}
{ejemplo(t("Example: different signs: −13 + 8", "Ejemplo con signos distintos: −13 + 8"),
  [("1", t("Step 1.", "Paso 1."), t("One is negative and one is positive: different signs.", "Uno es negativo y otro positivo: signos distintos.")),
   ("2", t("Step 2.", "Paso 2."), t("|−13| = 13 and |8| = 8. Subtract: 13 − 8 = 5.", "|−13| = 13 y |8| = 8. Se resta: 13 − 8 = 5.")),
   ("3", t("Step 3.", "Paso 3."), t("13 is the larger absolute value, and −13 is negative: the answer is negative.", "13 es el mayor valor absoluto, y −13 es negativo: el resultado es negativo.")),
   ("✓", t("Result.", "Resultado."), "−13 + 8 = <strong>−5</strong>")])}
{caja("ojo", t("The most common mistake", "El error más común"), t("<p>With different signs, do <strong>not</strong> add the absolute values. In the example above, adding would give −21, which is wrong. With different signs, you always subtract.</p>",
"<p>Con signos distintos, <strong>no</strong> se suman los valores absolutos. En el ejemplo anterior, sumar daría −21, que es incorrecto. Con signos distintos, siempre se resta.</p>"))}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>Use {T("(−)")} for each negative number. For −9 + (−7), press {T("(−)")} {T("9")} {T("+")} {T("(−)")} {T("7")} {T("enter")}. The screen shows −16.</p>""",
f"""<p>Use {T("(−)")} para cada número negativo. Para −9 + (−7), pulse {T("(−)")} {T("9")} {T("+")} {T("(−)")} {T("7")} {T("enter")}. La pantalla muestra −16.</p>"""))}
{practica("p3", t("Practice 3 — Same sign", "Práctica 3 — Mismo signo"), t("What is −8 + (−5)?", "¿Cuánto es −8 + (−5)?"),
          [("a", "−3"), ("b", "13"), ("c", "3"), ("d", "−13")])}
{practica("p4", t("Practice 4 — Different signs", "Práctica 4 — Signos distintos"), t("What is 14 + (−9)?", "¿Cuánto es 14 + (−9)?"),
          [("a", "5"), ("b", "−5"), ("c", "23"), ("d", "−23")])}
{enlace(n, t("addition-rule", "regla-suma"), t("the addition rule", "la regla de la suma"), t("Add with the same sign and with different signs, without drawing: first the sign, then the value.", "Sume con el mismo signo y con signos distintos sin dibujar: primero el signo, después el valor."))}'''

    s4 = f'''<p>{t("Subtracting integers becomes easy with one change: <strong>subtracting a number is the same as adding its opposite</strong>.", "La resta de enteros se vuelve sencilla con un solo cambio: <strong>restar un número es lo mismo que sumar su opuesto</strong>.")}</p>
<p style="text-align:center;font-size:1.15em"><strong>a − b = a + (−b)</strong></p>
<p>{t("Once the subtraction is an addition, use the addition rule from section 3. There are no new rules to memorize.", "Una vez convertida la resta en suma, se aplica la regla de la sección 3. No hay reglas nuevas que memorizar.")}</p>
{ejemplo(t("Example: 5 − 12", "Ejemplo: 5 − 12"),
  [("1", t("Step 1.", "Paso 1."), t("Change it to adding the opposite: 5 + (−12).", "Se cambia por la suma del opuesto: 5 + (−12).")),
   ("2", t("Step 2.", "Paso 2."), t("Different signs: 12 − 5 = 7.", "Signos distintos: 12 − 5 = 7.")),
   ("3", t("Step 3.", "Paso 3."), t("The larger absolute value, 12, belongs to a negative number: the answer is negative.", "El mayor valor absoluto, 12, es de un número negativo: el resultado es negativo.")),
   ("✓", t("Result.", "Resultado."), "5 − 12 = <strong>−7</strong>")])}
{ejemplo(t("Example: subtract a negative: −4 − (−9)", "Ejemplo: restar un negativo: −4 − (−9)"),
  [("1", t("Step 1.", "Paso 1."), t("Subtracting −9 is adding its opposite, +9: −4 + 9.", "Restar −9 es sumar su opuesto, +9: −4 + 9.")),
   ("2", t("Step 2.", "Paso 2."), t("Different signs: 9 − 4 = 5.", "Signos distintos: 9 − 4 = 5.")),
   ("3", t("Step 3.", "Paso 3."), t("The larger absolute value, 9, is positive: the answer is positive.", "El mayor valor absoluto, 9, es positivo: el resultado es positivo.")),
   ("✓", t("Result.", "Resultado."), "−4 − (−9) = <strong>5</strong>")])}
{caja("tip", t("Two minus signs", "Dos signos menos"), t("<p>Two minus signs in a row become a plus sign: \"− (−9)\" becomes \"+ 9\". In real life, taking away a debt is like receiving money.</p>",
"<p>Dos signos menos seguidos se convierten en un signo más: «− (−9)» se vuelve «+ 9». En la vida real, quitar una deuda es como recibir dinero.</p>"))}
{calc(t("Two minus keys", "Las dos teclas del menos"), t(f"""<p>For −4 − (−9), the first and the last minus signs are negative numbers, and the one in the middle subtracts. Press {T("(−)")} {T("4")} {T("−")} {T("(−)")} {T("9")} {T("enter")}. The screen shows 5.</p>""",
f"""<p>En −4 − (−9), el primer y el último menos son números negativos, y el del medio resta. Pulse {T("(−)")} {T("4")} {T("−")} {T("(−)")} {T("9")} {T("enter")}. La pantalla muestra 5.</p>"""))}
{practica("p5", t("Practice 5 — Rewrite it", "Práctica 5 — Reescribir"), t("How do you write 7 − 15 as an addition?", "¿Cómo se escribe 7 − 15 como una suma?"),
          [("a", "7 + 15"), ("b", "−7 + 15"), ("c", "7 + (−15)"), ("d", "−7 + (−15)")])}
{practica("p6", t("Practice 6 — Subtract a negative", "Práctica 6 — Restar un negativo"), t("What is −6 − (−8)?", "¿Cuánto es −6 − (−8)?"),
          [("a", "2"), ("b", "−14"), ("c", "−2"), ("d", "14")])}
{enlace(n, t("subtract", "restar"), t("subtracting is adding the opposite", "restar es sumar el opuesto"), t("Rewrite each subtraction as an addition of the opposite and solve it.", "Reescriba cada resta como suma del opuesto y resuélvala."))}'''

    s5 = f'''<p>{t("Adding and subtracting integers describes many everyday situations. The key is to give each amount the right sign:", "La suma y la resta de enteros describen muchas situaciones cotidianas. La clave es darle a cada cantidad el signo correcto:")}</p>
{tabla(t("Words and signs", "Palabras y signos"), t("Words that usually mean a positive amount and words that usually mean a negative amount", "Palabras que suelen indicar una cantidad positiva y palabras que suelen indicar una cantidad negativa"),
       [t("Positive (+)", "Positivo (+)"), t("Negative (−)", "Negativo (−)")],
       [[t("rises, goes up, above zero", "sube, aumenta, sobre cero"), t("drops, goes down, below zero", "baja, disminuye, bajo cero")],
        [t("deposit, gain, income", "depósito, ganancia, ingreso"), t("withdrawal, loss, debt, overdraft", "retiro, pérdida, deuda, sobregiro")],
        [t("above sea level, moves forward", "sobre el nivel del mar, avanza"), t("below sea level, moves back", "bajo el nivel del mar, retrocede")]])}
{ejemplo(t("Example: temperature", "Ejemplo: temperatura"),
  [("1", t("The problem.", "El problema."), t("At 6 a.m. the temperature was −8 °F. By noon it had risen 15 degrees. What was the temperature at noon?", "A las 6 de la mañana la temperatura era de −8 °F. Para el mediodía había subido 15 grados. ¿Qué temperatura hacía al mediodía?")),
   ("2", t("The signs.", "Los signos."), t("\"Risen 15 degrees\" is +15: −8 + 15.", "«Subió 15 grados» es +15: −8 + 15.")),
   ("3", t("Add.", "Sume."), t("Different signs: 15 − 8 = 7, with the sign of 15 (positive).", "Signos distintos: 15 − 8 = 7, con el signo del 15 (positivo).")),
   ("✓", t("Result.", "Resultado."), t("At noon it was <strong>7 °F</strong>.", "Al mediodía hacía <strong>7 °F</strong>."))])}
{ejemplo(t("Example: a bank balance", "Ejemplo: saldo bancario"),
  [("1", t("The problem.", "El problema."), t("An account has a balance of −$45 (it is overdrawn). The owner deposits $30. What is the new balance?", "Una cuenta tiene un saldo de −$45 (está sobregirada). El dueño deposita $30. ¿Cuál es el nuevo saldo?")),
   ("2", t("The signs.", "Los signos."), t("The overdraft is −45 and the deposit is +30: −45 + 30.", "El sobregiro es −45 y el depósito, +30: −45 + 30.")),
   ("3", t("Add.", "Sume."), t("Different signs: 45 − 30 = 15, with the sign of −45 (negative).", "Signos distintos: 45 − 30 = 15, con el signo del −45 (negativo).")),
   ("✓", t("Result.", "Resultado."), t("The balance is <strong>−$15</strong>. The account is still overdrawn.", "El saldo es <strong>−$15</strong>. La cuenta sigue sobregirada."))])}
{practica("p7", t("Practice 7 — Temperature", "Práctica 7 — Temperatura"), t("At night the temperature was 4 °F. By morning it had dropped 10 degrees. What was the temperature in the morning?", "En la noche la temperatura era de 4 °F. Para la mañana había bajado 10 grados. ¿Qué temperatura hacía en la mañana?"),
          [("a", "14 °F"), ("b", "−6 °F"), ("c", "6 °F"), ("d", "−14 °F")])}
{enlace(n, t("real-life", "contexto"), t("real-life problems", "problemas de la vida real"), t("Turn temperatures, deposits, and debts into additions and subtractions with signs.", "Traduzca temperaturas, depósitos y deudas a sumas y restas con signo."))}'''

    secciones = [("s-" + t("number-line", "recta"), t("Adding on the number line", "Sumar en la recta numérica"), s1),
                 ("s-" + t("counters", "fichas"), t("Two-color counters", "El modelo de fichas de dos colores"), s2),
                 ("s-" + t("addition-rule", "regla-suma"), t("The rule for adding integers", "La regla de la suma de enteros"), s3),
                 ("s-" + t("subtract", "restar"), t("Subtracting is adding the opposite", "Restar es sumar el opuesto"), s4),
                 ("s-" + t("real-life", "contexto"), t("Real-life problems", "Problemas de la vida real"), s5)]

    lesson = {"next": t("Lesson 1.3", "Lección 1.3"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Adding a positive number moves you to the right, not to the left.", "Sumar un número positivo lo mueve hacia la derecha, no hacia la izquierda."),
                                   "c": t("You started at 3. The starting point is −3.", "Partió del 3. El punto de partida es −3."),
                                   "d": t("Count again: from −3, move 7 places to the right: −2, −1, 0, 1, 2, 3, 4.", "Cuente otra vez: desde −3, avance 7 lugares hacia la derecha: −2, −1, 0, 1, 2, 3, 4.")},
             "right": t("From −3, 7 places to the right: −3 + 7 = 4.", "Desde −3, 7 lugares a la derecha: −3 + 7 = 4."),
             "solution": t("Start at −3 and move 7 places to the right: −2, −1, 0, 1, 2, 3, 4. So −3 + 7 = 4.", "Desde −3, avance 7 lugares hacia la derecha: −2, −1, 0, 1, 2, 3, 4. Así, −3 + 7 = 4.")},
      "p2": {"ok": "c", "hints": {"a": t("There are more red counters than yellow ones. Which color is left over?", "Hay más fichas rojas que amarillas. ¿Qué color sobra?"),
                                   "b": t("Do not count all the counters together. Each yellow cancels one red.", "No cuente todas las fichas juntas. Cada amarilla cancela una roja."),
                                   "d": t("3 and 7 are different, so not all the counters make pairs.", "3 y 7 son distintos, así que no todas las fichas forman pareja.")},
             "right": t("3 zero pairs are taken away, and 4 red counters are left: 3 + (−7) = −4.", "Se retiran 3 pares cero y quedan 4 fichas rojas: 3 + (−7) = −4."),
             "solution": t("Each yellow counter cancels one red: 3 zero pairs. 7 − 3 = 4 red counters are left, so 3 + (−7) = −4.", "Cada amarilla cancela una roja: 3 pares cero. Quedan 7 − 3 = 4 fichas rojas, así que 3 + (−7) = −4.")},
      "p3": {"ok": "d", "hints": {"a": t("Both numbers are negative: same sign. With the same sign, you add the absolute values.", "Los dos son negativos: mismo signo. Con el mismo signo, se suman los valores absolutos."),
                                   "b": t("The value 13 is right, but two negatives add up to a negative.", "El valor 13 está bien, pero dos negativos suman un negativo."),
                                   "c": t("With the same sign, you add the absolute values: 8 + 5.", "Con el mismo signo, se suman los valores absolutos: 8 + 5.")},
             "right": t("Same sign: 8 + 5 = 13, and the sign is negative.", "Mismo signo: 8 + 5 = 13, y el signo es negativo."),
             "solution": t("Both are negative. Add the absolute values, 8 + 5 = 13, and keep the negative sign: −13.", "Los dos son negativos. Se suman los valores absolutos, 8 + 5 = 13, y se conserva el signo negativo: −13.")},
      "p4": {"ok": "a", "hints": {"b": t("The value 5 is right. Which number has the larger absolute value, 14 or −9?", "El valor 5 está bien. ¿Cuál tiene mayor valor absoluto, 14 o −9?"),
                                   "c": t("With different signs, you subtract the absolute values: 14 − 9.", "Con signos distintos, se restan los valores absolutos: 14 − 9."),
                                   "d": t("With different signs, you subtract the absolute values, and 14 is positive.", "Con signos distintos, se restan los valores absolutos, y 14 es positivo.")},
             "right": t("Different signs: 14 − 9 = 5, with the sign of 14 (positive).", "Signos distintos: 14 − 9 = 5, con el signo del 14 (positivo)."),
             "solution": t("Different signs: subtract 14 − 9 = 5. The larger absolute value, 14, is positive, so the answer is 5.", "Signos distintos: se resta 14 − 9 = 5. El mayor valor absoluto, 14, es positivo, así que el resultado es 5.")},
      "p5": {"ok": "c", "hints": {"a": t("When you change − to +, the number you subtract changes to its opposite.", "Al cambiar − por +, el número que se resta cambia por su opuesto."),
                                   "b": t("The first number does not change. Only the number you subtract changes.", "El primer número no cambia. Solo cambia el que se resta."),
                                   "d": t("The first number does not change. Only the number you subtract changes.", "El primer número no cambia. Solo cambia el que se resta.")},
             "right": t("Keep the 7 and add the opposite of 15: 7 + (−15) = −8.", "Se conserva el 7 y se suma el opuesto de 15: 7 + (−15) = −8."),
             "solution": t("Subtracting 15 is adding −15: 7 − 15 = 7 + (−15), which is −8.", "Restar 15 es sumar −15: 7 − 15 = 7 + (−15), que da −8.")},
      "p6": {"ok": "a", "hints": {"b": t("You added −8 instead of its opposite. Subtracting −8 is adding +8.", "Sumó −8 en vez de su opuesto. Restar −8 es sumar +8."),
                                   "c": t("Check the sign: −6 + 8. Which number has the larger absolute value?", "Revise el signo: −6 + 8. ¿Cuál tiene mayor valor absoluto?"),
                                   "d": t("Rewrite it first: −6 − (−8) = −6 + 8. Different signs: subtract.", "Primero reescríbalo: −6 − (−8) = −6 + 8. Signos distintos: se resta.")},
             "right": t("−6 − (−8) = −6 + 8 = 2.", "−6 − (−8) = −6 + 8 = 2."),
             "solution": t("Subtracting −8 is adding 8: −6 + 8. Different signs: 8 − 6 = 2, with the sign of 8 (positive). The answer is 2.", "Restar −8 es sumar 8: −6 + 8. Signos distintos: 8 − 6 = 2, con el signo del 8 (positivo). El resultado es 2.")},
      "p7": {"ok": "b", "hints": {"a": t("\"Dropped\" means the temperature went down. Subtract 10.", "«Bajó» quiere decir que la temperatura descendió. Reste 10."),
                                   "c": t("The value 6 is right, but 4 − 10 goes below zero.", "El valor 6 está bien, pero 4 − 10 queda bajo cero."),
                                   "d": t("Start at 4, not at −4: 4 − 10.", "Parta de 4, no de −4: 4 − 10.")},
             "right": t("4 − 10 = 4 + (−10) = −6 °F.", "4 − 10 = 4 + (−10) = −6 °F."),
             "solution": t("\"Dropped 10\" is −10: 4 + (−10). Different signs: 10 − 4 = 6, with the sign of −10. It was −6 °F.", "«Bajó 10» es −10: 4 + (−10). Signos distintos: 10 − 4 = 6, con el signo del −10. Hacía −6 °F.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("The value 16 is right, but two negatives add up to a negative.", "El valor 16 está bien, pero dos negativos suman un negativo."),
                                 "c": t("With the same sign, you add the absolute values: 9 + 7.", "Con el mismo signo, se suman los valores absolutos: 9 + 7."),
                                 "d": t("With the same sign, you add the absolute values: 9 + 7.", "Con el mismo signo, se suman los valores absolutos: 9 + 7.")},
            "solution": t("Same sign: 9 + 7 = 16, negative. −9 + (−7) = −16.", "Mismo signo: 9 + 7 = 16, negativo. −9 + (−7) = −16.")},
      "B": {"ok": "c", "hints": {"a": t("With different signs, you subtract: 13 − 8. Do not add.", "Con signos distintos, se resta: 13 − 8. No se suma."),
                                 "b": t("The value 5 is right. Which number has the larger absolute value?", "El valor 5 está bien. ¿Cuál tiene mayor valor absoluto?"),
                                 "d": t("With different signs, you subtract the absolute values: 13 − 8.", "Con signos distintos, se restan los valores absolutos: 13 − 8.")},
            "solution": t("Different signs: 13 − 8 = 5, with the sign of −13 (negative): −5.", "Signos distintos: 13 − 8 = 5, con el signo del −13 (negativo): −5.")},
      "C": {"ok": "a", "hints": {"b": t("The value 7 is right, but 12 is larger than 5, and you subtract 12.", "El valor 7 está bien, pero 12 es mayor que 5, y se resta 12."),
                                 "c": t("Rewrite it: 5 + (−12). Different signs: subtract.", "Reescríbalo: 5 + (−12). Signos distintos: se resta."),
                                 "d": t("The first number, 5, stays positive. Rewrite: 5 + (−12).", "El primer número, 5, sigue positivo. Reescriba: 5 + (−12).")},
            "solution": t("5 − 12 = 5 + (−12). Different signs: 12 − 5 = 7, negative: −7.", "5 − 12 = 5 + (−12). Signos distintos: 12 − 5 = 7, negativo: −7.")},
      "D": {"ok": "d", "hints": {"a": t("You added −9 instead of its opposite. Subtracting −9 is adding +9.", "Sumó −9 en vez de su opuesto. Restar −9 es sumar +9."),
                                 "b": t("Check the sign of −4 + 9. Which number has the larger absolute value?", "Revise el signo de −4 + 9. ¿Cuál tiene mayor valor absoluto?"),
                                 "c": t("Rewrite it first: −4 + 9. Different signs: subtract.", "Primero reescríbalo: −4 + 9. Signos distintos: se resta.")},
            "solution": t("−4 − (−9) = −4 + 9 = 5.", "−4 − (−9) = −4 + 9 = 5.")},
      "E": {"ok": "c", "hints": {"a": t("The temperature rose: add 15 to −8.", "La temperatura subió: sume 15 a −8."),
                                 "b": t("The value 7 is right. Did the temperature end above or below zero?", "El valor 7 está bien. ¿La temperatura quedó sobre o bajo cero?"),
                                 "d": t("You added the absolute values. With different signs, you subtract.", "Sumó los valores absolutos. Con signos distintos, se resta.")},
            "solution": t("−8 + 15: different signs, 15 − 8 = 7, positive. It was 7 °F.", "−8 + 15: signos distintos, 15 − 8 = 7, positivo. Hacía 7 °F.")},
      "F": {"ok": "a", "hints": {"b": t("The value 15 is right, but the debt was larger than the deposit.", "El valor 15 está bien, pero la deuda era mayor que el depósito."),
                                 "c": t("A deposit adds money: −45 + 30, not −45 − 30.", "Un depósito suma dinero: −45 + 30, no −45 − 30."),
                                 "d": t("A deposit adds money, and the balance started at −45.", "Un depósito suma dinero, y el saldo empezaba en −45.")},
            "solution": t("−45 + 30: different signs, 45 − 30 = 15, negative. The balance is −$15.", "−45 + 30: signos distintos, 45 − 30 = 15, negativo. El saldo es −$15.")},
      "G": {"ok": "b", "hints": {"a": t("Subtracting −2 is adding its opposite. What is the opposite of −2?", "Restar −2 es sumar su opuesto. ¿Cuál es el opuesto de −2?"),
                                 "c": t("The first number, 6, does not change.", "El primer número, 6, no cambia."),
                                 "d": t("The first number, 6, does not change.", "El primer número, 6, no cambia.")},
            "solution": t("Subtracting −2 is adding 2: 6 − (−2) = 6 + 2 = 8.", "Restar −2 es sumar 2: 6 − (−2) = 6 + 2 = 8.")},
      "H": {"ok": "d", "hints": {"a": t("There are more red counters than yellow ones, so the answer is negative.", "Hay más fichas rojas que amarillas, así que el resultado es negativo."),
                                 "b": t("Each yellow counter cancels one red one. Do not count them all.", "Cada ficha amarilla cancela una roja. No las cuente todas."),
                                 "c": t("Count the pairs again: 5 yellow and 8 red make 5 zero pairs.", "Cuente otra vez los pares: 5 amarillas y 8 rojas forman 5 pares cero.")},
            "solution": t("5 zero pairs are taken away, and 3 red counters are left: 5 + (−8) = −3.", "Se retiran 5 pares cero y quedan 3 fichas rojas: 5 + (−8) = −3.")}
     }}

    quiz = [
     ("A", t("What is −9 + (−7)?", "¿Cuánto es −9 + (−7)?"), [("a", "16"), ("b", "−16"), ("c", "−2"), ("d", "2")]),
     ("B", t("What is −13 + 8?", "¿Cuánto es −13 + 8?"), [("a", "−21"), ("b", "5"), ("c", "−5"), ("d", "21")]),
     ("C", t("What is 5 − 12?", "¿Cuánto es 5 − 12?"), [("a", "−7"), ("b", "7"), ("c", "17"), ("d", "−17")]),
     ("D", t("What is −4 − (−9)?", "¿Cuánto es −4 − (−9)?"), [("a", "−13"), ("b", "−5"), ("c", "13"), ("d", "5")]),
     ("E", t("At 6 a.m. it was −8 °F. By noon the temperature had risen 15 degrees. What was the temperature at noon?", "A las 6 de la mañana hacía −8 °F. Para el mediodía la temperatura había subido 15 grados. ¿Qué temperatura hacía al mediodía?"), [("a", "−23 °F"), ("b", "−7 °F"), ("c", "7 °F"), ("d", "23 °F")]),
     ("F", t("A bank account has a balance of −$45. The owner deposits $30. What is the new balance?", "Una cuenta bancaria tiene un saldo de −$45. El dueño deposita $30. ¿Cuál es el nuevo saldo?"), [("a", "−$15"), ("b", "$15"), ("c", "−$75"), ("d", "$75")]),
     ("G", t("Which addition is equal to 6 − (−2)?", "¿Qué suma es igual a 6 − (−2)?"), [("a", "6 + (−2)"), ("b", "6 + 2"), ("c", "−6 + 2"), ("d", "−6 + (−2)")]),
     ("H", t("You have 5 yellow counters (+1 each) and 8 red counters (−1 each). What is the total?", "Hay 5 fichas amarillas (+1 cada una) y 8 fichas rojas (−1 cada una). ¿Cuál es el total?"), [("a", "3"), ("b", "13"), ("c", "−13"), ("d", "−3")])]

    return B.pagina_leccion(n, 1, t(*TEMA),
        t("Adding and subtracting integers", "Suma y resta de enteros con signo"),
        t("Add with the number line and with counters, learn the rule for the signs, and discover that subtracting is adding the opposite.", "Sume con la recta numérica y con fichas, aprenda la regla de los signos y descubra que restar es sumar el opuesto."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Add</strong> integers with the number line and with two-color counters.", "<strong>Sumar</strong> enteros con la recta numérica y con fichas de dos colores."),
         t("<strong>Use</strong> the rule for adding: the same sign, add; different signs, subtract.", "<strong>Aplicar</strong> la regla de la suma: mismo signo, se suma; signos distintos, se resta."),
         t("<strong>Explain</strong> why subtracting is adding the opposite: a − b = a + (−b).", "<strong>Explicar</strong> por qué restar es sumar el opuesto: a − b = a + (−b)."),
         t("<strong>Check</strong> the size of an answer with the absolute value.", "<strong>Comprobar</strong> el tamaño de un resultado con el valor absoluto."),
         t("<strong>Solve</strong> real-life problems with adding and subtracting integers.", "<strong>Resolver</strong> problemas de la vida real con sumas y restas de enteros.")],
        secciones,
        (t("Write and solve four additions with the same sign, four with different signs, and four subtractions. Rewrite each subtraction as an addition of the opposite before you solve it. Check two of them with counters you draw.",
           "Escriba y resuelva cuatro sumas con el mismo signo, cuatro con signos distintos y cuatro restas. Reescriba cada resta como suma del opuesto antes de resolverla. Compruebe dos de ellas con fichas que dibuje."),
         t("Write two problems from your life, one about temperature and one about money (a deposit, a payment, a debt). Write each one as an addition or a subtraction with signs, and solve it.",
           "Escriba dos problemas de su vida, uno de temperatura y otro de dinero (un depósito, un pago, una deuda). Escriba cada uno como suma o resta con signos y resuélvalo.")),
        quiz,
        t("Self-check checklist for adding and subtracting integers", "Lista de autoevaluación de la suma y la resta de enteros"),
        t("Self-check checklist: skills for adding and subtracting integers", "Lista de autoevaluación: destrezas de la suma y la resta de enteros"),
        [(t("The sign rule for adding", "La regla de los signos en la suma"), t("I use the rule in both cases and can explain it with counters.", "Aplico la regla en los dos casos y sé explicarla con fichas."), t("I use the rule, but sometimes I get the sign wrong.", "Aplico la regla, pero a veces me equivoco en el signo."), t("I mix up the same-sign case and the different-signs case.", "Confundo el caso del mismo signo con el de signos distintos.")),
         (t("The size of the answer", "El tamaño del resultado"), t("I find the value every time and check it with the absolute value.", "Hallo el valor siempre y lo compruebo con el valor absoluto."), t("I make an occasional arithmetic mistake.", "Cometo algún error de cálculo."), t("I add when I should subtract the absolute values, or the other way around.", "Sumo cuando debo restar los valores absolutos, o al revés.")),
         (t("Subtracting as adding the opposite", "La resta como suma del opuesto"), t("I rewrite and solve any subtraction, even with two minus signs.", "Reescribo y resuelvo cualquier resta, también con dos signos menos."), t("I rewrite simple subtractions, but two minus signs confuse me.", "Reescribo restas sencillas, pero los dos signos menos me confunden."), t("I do not rewrite the subtraction as an addition.", "No reescribo la resta como suma.")),
         (t("Real-life problems", "Problemas de la vida real"), t("I give each amount the right sign and explain the answer.", "Le doy a cada cantidad su signo y explico el resultado."), t("I set up the problem, but I sometimes choose the wrong sign.", "Planteo el problema, pero a veces elijo mal el signo."), t("I do not know which operation to use.", "No sé qué operación usar."))],
        t("<p>You can now add integers with the number line, with counters, and with the sign rule, and you know that <strong>subtracting is adding the opposite</strong>.</p>\n<p>In <strong>Lesson 1.3 · Multiplying and dividing integers; applications</strong> you will finish Topic 1 with the other two operations. You will learn the sign rule for multiplying and dividing, see why a negative times a negative is positive, and solve problems that use all four operations.</p>",
          "<p>Ya sabe sumar enteros con la recta numérica, con fichas y con la regla de los signos, y sabe que <strong>restar es sumar el opuesto</strong>.</p>\n<p>En la <strong>Lección 1.3 · Multiplicación y división de enteros; aplicaciones</strong> terminará el Tema 1 con las otras dos operaciones. Aprenderá la regla de los signos para multiplicar y dividir, verá por qué negativo por negativo da positivo y resolverá problemas con las cuatro operaciones.</p>"),
        ("1-3", ("", t("Lesson 1.3 · Multiplying and dividing integers; applications", "Lección 1.3 · Multiplicación y división de enteros; aplicaciones"))),
        [(t("sum", "suma"), t("The answer to an addition.", "El resultado de una suma.")),
         (t("difference", "diferencia"), t("The answer to a subtraction.", "El resultado de una resta.")),
         (t("zero pair", "par cero"), t("A +1 and a −1 together. They add up to 0.", "Un +1 y un −1 juntos. Suman 0.")),
         (t("same sign / different signs", "mismo signo / signos distintos"), t("Two numbers that are both positive or both negative / one positive and one negative.", "Dos números que son los dos positivos o los dos negativos / uno positivo y otro negativo.")),
         (t("adding the opposite", "sumar el opuesto"), t("The way to subtract integers: a − b = a + (−b).", "La forma de restar enteros: a − b = a + (−b).")),
         (t("overdraft", "sobregiro"), t("A bank balance below zero: the account owes money.", "Un saldo bancario bajo cero: la cuenta debe dinero."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "inicio": "start", "derecha": "right", "izquierda": "left",
  "vozRS": "Number line: start at {a} and move {n} places to the {d}, to {r}.",
  "salidaRS": "Start at {a} and move {n} {l} to the {d} ({por}).", "lugar": "place", "lugares": "places", "porMas": "you are adding a positive number", "porMenos": "you are adding a negative number", "suma0": "Adding 0 does not change the number.",
  "enunRS": "Start at {a} and add {b}.", "vozRS2": "Number line with the starting point at {a}.", "preguntaRS": "What is {s}?",
  "solRS": "Move {n} places to the {d} from {a}: you land on {r}.",
  "amarilla": "yellow counter", "amarillas": "yellow counters", "roja": "red counter", "rojas": "red counters",
  "hay": "There are {p} {pa} and {q} {qr}.", "pulse": "Press \"Make the zero pairs\" to see what is left.",
  "pares1": "{k} zero pair is made and taken away.", "paresN": "{k} zero pairs are made and taken away.",
  "quedan0": "Nothing is left: every counter has a partner.", "quedanP": "{x} {c} are left without a partner.", "quedan1": "{x} {c} is left without a partner.",
  "vozFC": "Counters: {p} yellow and {q} red.", "vozFC2": "; {k} zero pairs crossed out",
  "enunFC": "What is left after you take away the zero pairs? Write the answer to {s}.", "vozFC3": "Counters: a row for {a} and a row for {b}.",
  "mismoSigno": "Same sign: {x} + {y} = {r}, and the answer keeps the {sg} sign.", "positivo": "positive", "negativo": "negative",
  "distintos": "Different signs: {x} − {y} = {r}", "conSigno": ", with the sign of {M}, which has the larger absolute value.",
  "pistaDist": "With different signs, you do not add the absolute values: you subtract the smaller from the larger.",
  "pistaSigno": "The value is right, but not the sign: the answer gets the sign of the number with the larger absolute value.",
  "calcula": "Calculate {s}.",
  "reescribe": "How do you write {a} − {b} as an addition?",
  "pistaOpuesto": "When you change − to +, the number you subtract changes to its opposite.", "pistaPrimero": "The first number does not change. Only the number you subtract changes.",
  "bienRe": "Keep the {a} and add the opposite of {b}, which is {o}. The answer is {r}.", "malRe": "Keep the first number and add the opposite of the second: {a} + {po} = {r}.",
  "sumoNum": "It looks like you added the number instead of its opposite. Subtracting {pb} is adding {po}.",
  "vozRT": "Number line: {a} plus {o} is {r}.", "cambio": "Change the subtraction to an addition and {b} to its opposite, {o}. ",
  "c1": "At 6 a.m. the temperature was {a} °F. By noon it had risen {b} degrees. What was the temperature at noon, in °F?", "s1": "\"Risen\" is +{b}: {a} + {b} = {r} °F.",
  "c2": "In the afternoon the temperature was {a} °F. During the night it dropped {b} degrees. What was the temperature at night, in °F?", "s2": "\"Dropped\" is −{b}: {a} − {b} = {r} °F.",
  "c3": "An account has a balance of −${d} (it is overdrawn). The owner deposits ${b}. What is the new balance, in dollars?", "s3": "{a} + {b} = {r}.", "s3b": " The account is still overdrawn.",
  "c4": "A diver is {d} feet below sea level and goes down {b} more feet. Where is the diver now, compared with sea level? (Below sea level is negative.)", "s4": "{a} − {b} = {r} feet.",
  "c5": "A football team gains {a} yards, loses {b}, and then gains {c}. What is the total change, in yards?", "s5": "{a} − {b} + {c} = {r} yards.",
  "c6": "An elevator is on floor {a} and goes down {b} floors. The basements are numbered with negatives (−1, −2, …), and the ground floor is 0. What floor is it on now?", "s6": "{a} − {b} = {r}."
 },
 "es": {
  "inicio": "inicio", "derecha": "derecha", "izquierda": "izquierda",
  "vozRS": "Recta numérica: se parte de {a} y se avanzan {n} lugares hacia la {d}, hasta {r}.",
  "salidaRS": "Se parte de {a} y se avanzan {n} {l} hacia la {d} ({por}).", "lugar": "lugar", "lugares": "lugares", "porMas": "se suma un positivo", "porMenos": "se suma un negativo", "suma0": "Sumar 0 no cambia el número.",
  "enunRS": "Se parte de {a} y se suma {b}.", "vozRS2": "Recta numérica con el punto de partida en {a}.", "preguntaRS": "¿Cuánto es {s}?",
  "solRS": "Desde {a} se avanzan {n} lugares hacia la {d}: se llega a {r}.",
  "amarilla": "ficha amarilla", "amarillas": "fichas amarillas", "roja": "ficha roja", "rojas": "fichas rojas",
  "hay": "Hay {p} {pa} y {q} {qr}.", "pulse": "Pulse «Formar los pares cero» para ver qué sobra.",
  "pares1": "Se forma {k} par cero, que se retira.", "paresN": "Se forman {k} pares cero, que se retiran.",
  "quedan0": "No queda nada: todas las fichas tienen pareja.", "quedanP": "Quedan {x} {c} sin pareja.", "quedan1": "Queda {x} {c} sin pareja.",
  "vozFC": "Fichas: {p} amarillas y {q} rojas.", "vozFC2": "; {k} pares cero tachados",
  "enunFC": "¿Qué queda después de retirar los pares cero? Escriba el resultado de {s}.", "vozFC3": "Fichas: una fila para {a} y otra para {b}.",
  "mismoSigno": "Mismo signo: {x} + {y} = {r}, y el resultado conserva el signo {sg}.", "positivo": "positivo", "negativo": "negativo",
  "distintos": "Signos distintos: {x} − {y} = {r}", "conSigno": ", con el signo del {M}, que tiene mayor valor absoluto.",
  "pistaDist": "Con signos distintos no se suman los valores absolutos: se resta el menor del mayor.",
  "pistaSigno": "El valor está bien, pero el signo no: el resultado lleva el signo del número con mayor valor absoluto.",
  "calcula": "Calcule {s}.",
  "reescribe": "¿Cómo se escribe {a} − {b} como una suma?",
  "pistaOpuesto": "Al cambiar − por +, el número que se resta cambia por su opuesto.", "pistaPrimero": "El primer número no cambia. Solo cambia el que se resta.",
  "bienRe": "Se conserva el {a} y se suma el opuesto de {b}, que es {o}. El resultado es {r}.", "malRe": "Se conserva el primer número y se suma el opuesto del segundo: {a} + {po} = {r}.",
  "sumoNum": "Parece que sumó el número en vez de su opuesto. Restar {pb} es sumar {po}.",
  "vozRT": "Recta numérica: {a} más {o} es {r}.", "cambio": "Se cambia la resta por una suma y el {b} por su opuesto, {o}. ",
  "c1": "A las 6 de la mañana la temperatura era de {a} °F. Para el mediodía había subido {b} grados. ¿Qué temperatura hacía al mediodía, en °F?", "s1": "«Subió» es +{b}: {a} + {b} = {r} °F.",
  "c2": "En la tarde la temperatura era de {a} °F. Durante la noche bajó {b} grados. ¿Qué temperatura hacía en la noche, en °F?", "s2": "«Bajó» es −{b}: {a} − {b} = {r} °F.",
  "c3": "Una cuenta tiene un saldo de −${d} (está sobregirada). El dueño deposita ${b}. ¿Cuál es el nuevo saldo, en dólares?", "s3": "{a} + {b} = {r}.", "s3b": " La cuenta sigue sobregirada.",
  "c4": "Un buzo está a {d} pies bajo el nivel del mar y desciende {b} pies más. ¿Dónde queda ahora respecto del nivel del mar? (Bajo el nivel del mar es negativo.)", "s4": "{a} − {b} = {r} pies.",
  "c5": "Un equipo de fútbol americano gana {a} yardas, pierde {b} y luego gana {c}. ¿Cuál es el cambio total, en yardas?", "s5": "{a} − {b} + {c} = {r} yardas.",
  "c6": "Un elevador está en el piso {a} y baja {b} pisos. Los sótanos se numeran con negativos (−1, −2, …) y la planta baja es el piso 0. ¿En qué piso queda?", "s6": "{a} − {b} = {r}."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function suma(a, b){ return ent(a) + " + " + par(b); }
function pistasSuma(a, b){
  var r = a + b, p = [];
  if ((a < 0) !== (b < 0) && a !== 0 && b !== 0){ var mal = (Math.abs(a) + Math.abs(b)) * (Math.abs(a) > Math.abs(b) ? Math.sign(a) : Math.sign(b)); if (mal !== r) p.push({ v: mal, msg: TXT.pistaDist }); }
  if (-r !== r) p.push({ v: -r, msg: TXT.pistaSigno });
  return p;
}
function explicaSuma(a, b){
  var r = a + b;
  if (a === 0 || b === 0) return TXT.suma0;
  if ((a < 0) === (b < 0)) return F(TXT.mismoSigno, { x: Math.abs(a), y: Math.abs(b), r: Math.abs(r), sg: a < 0 ? TXT.negativo : TXT.positivo });
  var M = Math.abs(a) > Math.abs(b) ? a : b;
  return F(TXT.distintos, { x: Math.max(Math.abs(a), Math.abs(b)), y: Math.min(Math.abs(a), Math.abs(b)), r: Math.abs(r) }) + (r === 0 ? "." : F(TXT.conSigno, { M: ent(M) }));
}

/* ============ MODULE 1 · adding on the number line ============ */
function pintaRS(){
  var a = +$("rs-a").value, b = +$("rs-b").value, r = a + b, lo = Math.min(-10, r - 1), hi = Math.max(10, r + 1), d = b >= 0 ? TXT.derecha : TXT.izquierda, n = Math.abs(b);
  $("rs-av").textContent = ent(a); $("rs-bv").textContent = ent(b);
  $("rs-svg").innerHTML = rectaEnt(lo, hi, [{ v: a, txt: TXT.inicio, color: "#424242", abajo: true }, { v: r, txt: ent(r), color: "#b71c1c", abajo: true }], b === 0 ? [] : [{ de: a, a: r, txt: (b > 0 ? "+" : "−") + n, color: b > 0 ? "#1b5e20" : "#b71c1c" }],
    F(TXT.vozRS, { a: ent(a), n: n, d: d, r: ent(r) }));
  $("rs-salida").innerHTML = '<div class="linea">' + (b === 0 ? TXT.suma0 : F(TXT.salidaRS, { a: ent(a), n: n, l: n === 1 ? TXT.lugar : TXT.lugares, d: d, por: b > 0 ? TXT.porMas : TXT.porMenos })) + '</div><div class="linea veredicto">' + suma(a, b) + ' = ' + ent(r) + '</div>';
}
function genRecta(){
  var a = azarEnt(-10, 10), b = azarEnt(-10, 10, true), r = a + b;
  return { enun: F(TXT.enunRS, { a: ent(a), b: par(b) }) + rectaEnt(Math.min(-10, r - 1), Math.max(10, r + 1), [{ v: a, txt: TXT.inicio, color: "#424242", abajo: true }], [], F(TXT.vozRS2, { a: ent(a) })) + F(TXT.preguntaRS, { s: suma(a, b) }),
    correcta: String(r), solucion: F(TXT.solRS, { n: Math.abs(b), d: b > 0 ? TXT.derecha : TXT.izquierda, a: ent(a), r: ent(r) }), evalua: numE(r, pistasSuma(a, b)) };
}

/* ============ MODULE 2 · counters ============ */
var FC = { pares: false };
function pintaFC(){
  var a = +$("fc-a").value, b = +$("fc-b").value, r = a + b, pos = Math.max(a, 0) + Math.max(b, 0), neg = Math.max(-a, 0) + Math.max(-b, 0), k = Math.min(pos, neg);
  $("fc-av").textContent = ent(a); $("fc-bv").textContent = ent(b);
  $("fc-svg").innerHTML = fichasSVG(a, b, FC.pares, F(TXT.vozFC, { p: pos, q: neg }) + (FC.pares ? F(TXT.vozFC2, { k: k }) : "") + ".");
  var h = '<div class="linea">' + F(TXT.hay, { p: pos, pa: pos === 1 ? TXT.amarilla : TXT.amarillas, q: neg, qr: neg === 1 ? TXT.roja : TXT.rojas }) + '</div>';
  if (FC.pares){
    var x = Math.abs(r), c = r > 0 ? (x === 1 ? TXT.amarilla : TXT.amarillas) : (x === 1 ? TXT.roja : TXT.rojas);
    h += '<div class="linea">' + (k ? F(k === 1 ? TXT.pares1 : TXT.paresN, { k: k }) + " " : "") + (r === 0 ? TXT.quedan0 : F(x === 1 ? TXT.quedan1 : TXT.quedanP, { x: x, c: c })) + '</div><div class="linea veredicto">' + suma(a, b) + ' = ' + ent(r) + '</div>';
  } else h += '<div class="linea">' + TXT.pulse + '</div>';
  $("fc-salida").innerHTML = h;
}
function genFichas(){
  var a = azarEnt(-9, 9, true), b = azarEnt(-9, 9, true), r = a + b;
  return { enun: fichasSVG(a, b, false, F(TXT.vozFC3, { a: ent(a), b: ent(b) })) + F(TXT.enunFC, { s: suma(a, b) }),
    correcta: String(r), solucion: explicaSuma(a, b), evalua: numE(r, pistasSuma(a, b)) };
}

/* ============ MODULE 3 · the addition rule ============ */
function genRegla(){
  var a = azarEnt(-25, 25, true), b = azarEnt(-25, 25, true);
  return { enun: F(TXT.calcula, { s: suma(a, b) }), res: a + b, explica: explicaSuma(a, b) };
}

/* ============ MODULE 4 · subtracting ============ */
function pintaRT(){
  var a = +$("rt-a").value, b = +$("rt-b").value, r = a - b, lo = Math.min(-10, r - 1), hi = Math.max(10, r + 1);
  $("rt-av").textContent = ent(a); $("rt-bv").textContent = ent(b);
  $("rt-salida").innerHTML = '<div class="linea grande">' + ent(a) + ' − ' + par(b) + ' = ' + ent(a) + ' + ' + par(-b) + ' = ' + ent(r) + '</div><div class="linea">' + F(TXT.cambio, { b: ent(b), o: ent(-b) }) + explicaSuma(a, -b) + '</div>';
  $("rt-svg").innerHTML = rectaEnt(lo, hi, [{ v: a, txt: TXT.inicio, color: "#424242", abajo: true }, { v: r, txt: ent(r), color: "#b71c1c", abajo: true }], -b === 0 ? [] : [{ de: a, a: r, txt: (-b > 0 ? "+" : "−") + Math.abs(b), color: -b > 0 ? "#1b5e20" : "#b71c1c" }], F(TXT.vozRT, { a: ent(a), o: ent(-b), r: ent(r) }));
}
function genReescribe(){
  var a = azarEnt(-15, 15, true), b = azarEnt(-15, 15, true);
  var o = [{ html: ent(a) + " + " + par(-b), clave: "b" }, { html: ent(a) + " + " + par(b), clave: "m1" }, { html: ent(-a) + " + " + par(-b), clave: "m2" }, { html: ent(-a) + " + " + par(b), clave: "m3" }];
  return { enun: F(TXT.reescribe, { a: ent(a), b: par(b) }), opciones: o, correcta: "b", pistas: { m1: TXT.pistaOpuesto, m2: TXT.pistaPrimero, m3: TXT.pistaPrimero }, pista: TXT.pistaOpuesto,
    bien: F(TXT.bienRe, { a: ent(a), b: ent(b), o: ent(-b), r: ent(a - b) }), mal: F(TXT.malRe, { a: ent(a), po: par(-b), r: ent(a - b) }) };
}
function genResta(){
  var a = azarEnt(-20, 20, true), b = azarEnt(-20, 20, true), r = a - b, p = [];
  if (a + b !== r) p.push({ v: a + b, msg: F(TXT.sumoNum, { pb: par(b), po: par(-b) }) });
  return { enun: F(TXT.calcula, { s: ent(a) + " − " + par(b) }), correcta: String(r), solucion: ent(a) + " − " + par(b) + " = " + ent(a) + " + " + par(-b) + " = " + ent(r) + ". " + explicaSuma(a, -b), evalua: numE(r, p) };
}

/* ============ MODULE 5 · real life ============ */
function genContexto(){
  var tipo = aleatorio(1, 6), a, b, c, r, enun, sol;
  if (tipo === 1){ a = -aleatorio(2, 15); b = aleatorio(5, 25); r = a + b; enun = F(TXT.c1, { a: ent(a), b: b }); sol = F(TXT.s1, { a: ent(a), b: b, r: ent(r) }); }
  else if (tipo === 2){ a = aleatorio(-5, 20); b = aleatorio(10, 30); r = a - b; enun = F(TXT.c2, { a: ent(a), b: b }); sol = F(TXT.s2, { a: ent(a), b: b, r: ent(r) }); }
  else if (tipo === 3){ a = -aleatorio(10, 90); b = aleatorio(10, 80); r = a + b; enun = F(TXT.c3, { d: -a, b: b }); sol = F(TXT.s3, { a: ent(a), b: b, r: ent(r) }) + (r < 0 ? TXT.s3b : ""); }
  else if (tipo === 4){ a = -aleatorio(10, 60); b = aleatorio(5, 40); r = a - b; enun = F(TXT.c4, { d: -a, b: b }); sol = F(TXT.s4, { a: ent(a), b: b, r: ent(r) }); }
  else if (tipo === 5){ a = aleatorio(3, 12); b = aleatorio(3, 15); c = aleatorio(2, 10); r = a - b + c; enun = F(TXT.c5, { a: a, b: b, c: c }); sol = F(TXT.s5, { a: a, b: b, c: c, r: ent(r) }); }
  else { a = aleatorio(1, 8); b = aleatorio(a + 1, a + 6); r = a - b; enun = F(TXT.c6, { a: a, b: b }); sol = F(TXT.s6, { a: a, b: b, r: ent(r) }); }
  return { enun: enun, correcta: String(r), solucion: sol, evalua: numE(r, []) };
}

/* ============ Start ============ */
["rs-a", "rs-b"].forEach(function(id){ $(id).addEventListener("input", pintaRS); }); pintaRS();
creaPracticaLibre("p1", genRecta);
["fc-a", "fc-b"].forEach(function(id){ $(id).addEventListener("input", function(){ FC.pares = false; pintaFC(); }); });
$("fc-pares").addEventListener("click", function(){ FC.pares = true; pintaFC(); });
$("fc-reinicia").addEventListener("click", function(){ FC.pares = false; pintaFC(); });
pintaFC();
creaPracticaLibre("p2", genFichas);
creaSignoValor("p3", genRegla);
["rt-a", "rt-b"].forEach(function(id){ $(id).addEventListener("input", pintaRT); }); pintaRT();
creaPracticaOM("p4", genReescribe);
creaPracticaLibre("p5", genResta);
creaPracticaLibre("p6", genContexto);
'''

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val):
        return f'<div class="campo" style="flex:1;min-width:200px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    mods = [
     (t("add-on-line", "recta-suma"), t("Adding on the number line", "Sumar en la recta numérica"),
      f'''      <p>{t("Adding is moving on the number line: start at the first number and move. To add a positive number, move to the <strong>right</strong>; to add a negative number, move to the <strong>left</strong>.", "Sumar es moverse en la recta: se parte del primer número y se avanza. Si se suma un positivo, se avanza hacia la <strong>derecha</strong>; si se suma un negativo, hacia la <strong>izquierda</strong>.")}</p>
      <h3>{t("The jump", "El recorrido")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("rs-a", t("Starting point", "Punto de partida"), -10, 10, -5)}
          {deslizador("rs-b", t("Number you add", "Número que se suma"), -10, 10, 8)}
        </div>
        <div id="rs-svg"></div>
        <div class="salida" id="rs-salida" aria-live="polite"></div>
      </div>
{B.libre_e("p1", t("Practice: where do you land?", "Practique: ¿dónde se llega?"))}'''),
     (t("counters", "fichas"), t("Two-color counters", "El modelo de fichas de dos colores"),
      f'''      <p>{t("Each yellow counter (+) is worth +1, and each red counter (−) is worth −1. One yellow and one red make a <strong>zero pair</strong>, because +1 + (−1) = 0. Take away the zero pairs: <strong>what is left is the answer</strong>.", "Cada ficha amarilla (+) vale +1 y cada ficha roja (−) vale −1. Una amarilla y una roja forman un <strong>par cero</strong>, porque +1 + (−1) = 0. Se retiran los pares cero: <strong>lo que queda es el resultado</strong>.")}</p>
      <h3>{t("Make the zero pairs", "Forme los pares cero")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("fc-a", t("First number", "Primer número"), -12, 12, -6)}
          {deslizador("fc-b", t("Second number", "Segundo número"), -12, 12, 4)}
        </div>
        <div class="fila-btn"><button type="button" class="btn" id="fc-pares">{t("Make the zero pairs", "Formar los pares cero")}</button><button type="button" class="btn-sec" id="fc-reinicia">{t("Start over", "Empezar de nuevo")}</button></div>
        <div id="fc-svg"></div>
        <div class="salida" id="fc-salida" aria-live="polite"></div>
      </div>
      <p>{t("Want to understand it with money? Open the complement <a href=\"/math/level-2/tengo-debo.html?lang=en\" target=\"_blank\" rel=\"noopener noreferrer\">What I have and what I owe</a> (opens in a new tab): coins are what you have, and debts are what you owe.", "¿Quiere entenderlo con dinero? Abra el complemento <a href=\"/math/level-2/tengo-debo.html?lang=es\" target=\"_blank\" rel=\"noopener noreferrer\">Tengo y debo</a> (se abre en una pestaña nueva): las monedas son lo que tiene y las deudas, lo que debe.")}</p>
{B.libre_e("p2", t("Practice: what is left?", "Practique: ¿qué queda?"))}'''),
     (t("addition-rule", "regla-suma"), t("The addition rule", "La regla de la suma"),
      f'''      <p>{t("The number line and the counters lead to a rule that lets you add without drawing:", "La recta y las fichas llevan a una regla que permite sumar sin dibujar:")}</p>
      <table class="reglas">
        <caption>{t("The rule for adding integers", "La regla de la suma de enteros")}</caption>
        <thead><tr><th scope="col">{t("Case", "Caso")}</th><th scope="col">{t("The absolute values", "Los valores absolutos")}</th><th scope="col">{t("Sign of the answer", "Signo del resultado")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Same sign", "Mismo signo")}</td><td>{t("add them", "se suman")}</td><td>{t("the sign they share", "el signo común")}</td></tr>
          <tr><td>{t("Different signs", "Signos distintos")}</td><td>{t("subtract the smaller from the larger", "se resta el menor del mayor")}</td><td>{t("the sign of the number with the larger absolute value", "el del número con mayor valor absoluto")}</td></tr>
        </tbody>
      </table>
      <div class="caja-atencion"><strong>{t("The most common mistake:", "El error más común:")}</strong> {t("with different signs, do not add the absolute values. −13 + 8 is not −21: it is −5.", "con signos distintos no se suman los valores absolutos. −13 + 8 no es −21: es −5.")}</div>
{B.signo_valor("p3", t("Practice: first the sign, then the value", "Practique: primero el signo, después el valor"))}'''),
     (t("subtract", "restar"), t("Subtracting is adding the opposite", "Restar es sumar el opuesto"),
      f'''      <p>{t("Every subtraction can become an addition: <strong>subtracting a number is adding its opposite</strong>. Then use the addition rule. There are no new rules to memorize.", "Toda resta se convierte en una suma: <strong>restar un número es sumar su opuesto</strong>. Después se aplica la regla de la suma. No hay reglas nuevas que memorizar.")}</p>
      <div class="formula">a − b = a + (−b)</div>
      <h3>{t("Rewrite and solve", "Reescriba y resuelva")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("rt-a", t("First number", "Primer número"), -10, 10, -4)}
          {deslizador("rt-b", t("Number you subtract", "Número que se resta"), -10, 10, -9)}
        </div>
        <div class="salida" id="rt-salida" aria-live="polite"></div>
        <div id="rt-svg"></div>
      </div>
      <div class="caja-tip"><strong>{t("Two minus signs in a row become a plus sign:", "Dos signos menos seguidos se convierten en un signo más:")}</strong> {t("\"− (−9)\" is \"+ 9\". Taking away a debt is like receiving money.", "«− (−9)» es «+ 9». Quitar una deuda es como recibir dinero.")}</div>
{B.om("p4", t("Practice: how do you rewrite it?", "Practique: ¿cómo se reescribe?"))}
{B.libre_e("p5", t("Practice: subtract", "Practique: restar"))}'''),
     (t("real-life", "contexto"), t("Real-life problems", "Problemas de la vida real"),
      f'''      <p>{t("The key is to give each amount the right sign: what goes up, is gained, or is deposited is positive; what goes down, is lost, or is taken out is negative.", "La clave está en darle a cada cantidad su signo: lo que sube, se gana o se deposita es positivo; lo que baja, se pierde o se retira es negativo.")}</p>
      <table class="reglas">
        <caption>{t("Words and signs", "Palabras y signos")}</caption>
        <thead><tr><th scope="col">{t("Positive (+)", "Positivo (+)")}</th><th scope="col">{t("Negative (−)", "Negativo (−)")}</th></tr></thead>
        <tbody>
          <tr><td>{t("rises, goes up, above zero", "sube, aumenta, sobre cero")}</td><td>{t("drops, goes down, below zero", "baja, disminuye, bajo cero")}</td></tr>
          <tr><td>{t("deposit, gain, income", "depósito, ganancia, ingreso")}</td><td>{t("withdrawal, loss, debt, overdraft", "retiro, pérdida, deuda, sobregiro")}</td></tr>
          <tr><td>{t("above sea level, moves forward", "sobre el nivel del mar, avanza")}</td><td>{t("below sea level, moves back", "bajo el nivel del mar, retrocede")}</td></tr>
        </tbody>
      </table>
{B.libre_e("p6", t("Practice: problems with integers", "Practique: problemas con enteros"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 1, t(*TEMA), t("Adding and subtracting integers", "Suma y resta de enteros con signo"),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Suma y resta de enteros con signo")
