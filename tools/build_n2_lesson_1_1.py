"""Level 2 · Lesson 1.1 · The number line, absolute value, and opposites — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import m, p, recta, ROJO, VERDE, AZUL, GRIS

B.NIVEL = 2
N = "1-1"
TEMA = ("Integers", "Enteros con signo")

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Level 2. In Level 1 you worked with numbers from zero up: you read them, compared them, and operated with them. Now the world of numbers grows <strong>to the left of zero</strong>. Negative numbers describe everything that is \"below\" a starting point: a temperature below zero, a debt, a depth below sea level.",
"Bienvenido al Nivel 2. En el Nivel 1 trabajó con los números desde el cero hacia arriba: los leyó, los comparó y operó con ellos. Ahora el mundo de los números crece <strong>a la izquierda del cero</strong>. Los números negativos describen todo lo que está «por debajo» de un punto de partida: una temperatura bajo cero, una deuda, una profundidad bajo el nivel del mar.")}</p>
<p>{t("The <strong>number line</strong> is a line where every point is a number. <strong>Zero</strong> is in the center. The <strong>positive numbers</strong> (1, 2, 3, …) are to its right, and the <strong>negative numbers</strong> (−1, −2, −3, …) are to its left. Together, the whole numbers, their negatives, and zero are called <strong>integers</strong>.",
"La <strong>recta numérica</strong> es una línea en la que cada punto es un número. El <strong>cero</strong> está en el centro. Los <strong>números positivos</strong> (1, 2, 3, …) están a su derecha y los <strong>negativos</strong> (−1, −2, −3, …), a su izquierda. Los números naturales, sus negativos y el cero forman los <strong>números enteros</strong>.")}</p>
{recta(-8, 8, t("A number line from −8 to 8. Zero is in the center, the negative numbers are to its left, and the positive numbers are to its right.", "Una recta numérica de −8 a 8. El cero está en el centro, los negativos a su izquierda y los positivos a su derecha."),
       marcas=[(-5, "−5", ROJO, False), (3, "3", VERDE, False)], paso=1)}
<p>{t("Three ideas about the number line:", "Tres ideas sobre la recta numérica:")}</p>
<ul>
<li>{t("<strong>The numbers grow to the right.</strong> Any number is greater than every number to its left. That is why −2 is greater than −5, even though \"5\" looks bigger than \"2\": −2 is closer to zero, so it is farther to the right.",
"<strong>Los números crecen hacia la derecha.</strong> Cualquier número es mayor que todos los que tiene a su izquierda. Por eso −2 es mayor que −5, aunque «5» parezca más grande que «2»: −2 está más cerca del cero y, por tanto, más a la derecha.")}</li>
<li>{t("<strong>The sign shows the direction.</strong> When the minus sign is in front of a number alone, it does not mean \"subtract\": it means the number is to the left of zero. You read −8 as \"negative eight.\"",
"<strong>El signo indica la dirección.</strong> Cuando el signo menos acompaña a un número solo, no quiere decir «restar»: indica que el número está a la izquierda del cero. −8 se lee «menos ocho» o «negativo ocho».")}</li>
<li>{t("<strong>Each number has one place.</strong> So you can compare any two integers just by seeing which one is farther to the right.",
"<strong>Cada número tiene un solo lugar.</strong> Por eso se pueden comparar dos enteros cualesquiera con solo mirar cuál está más a la derecha.")}</li>
</ul>
{caja("tip", t("In real life", "En la vida real"), t("<p>A thermometer is a number line standing up. Zero is a reference point; degrees above zero are positive and degrees below zero are negative. A temperature of −10 °F is lower, and colder, than −3 °F.</p>",
"<p>Un termómetro es una recta numérica de pie. El cero es un punto de referencia; los grados sobre cero son positivos y los grados bajo cero son negativos. Una temperatura de −10 °F está más abajo, y es más fría, que −3 °F.</p>"))}
{tabla(t("Words for positive and negative", "Palabras para positivo y negativo"), t("Situations that use positive and negative numbers", "Situaciones que usan números positivos y negativos"),
       [t("Situation", "Situación"), t("Positive (+)", "Positivo (+)"), t("Negative (−)", "Negativo (−)"), t("What 0 means", "Qué significa el 0")],
       [[t("temperature", "temperatura"), t("above zero", "sobre cero"), t("below zero", "bajo cero"), "0 °F"],
        [t("money", "dinero"), t("a deposit, a gain", "un depósito, una ganancia"), t("a debt, a loss, an overdraft", "una deuda, una pérdida, un sobregiro"), t("you have nothing and owe nothing", "no tiene nada ni debe nada")],
        [t("height", "altura"), t("above sea level", "sobre el nivel del mar"), t("below sea level", "bajo el nivel del mar"), t("sea level", "el nivel del mar")],
        [t("an elevator", "un elevador"), t("floors above the street", "pisos sobre la calle"), t("basement floors", "sótanos"), t("the ground floor", "la planta baja")]])}
{ejemplo(t("Example: order from least to greatest: −4, 3, −7, 0, −1", "Ejemplo: ordene de menor a mayor: −4, 3, −7, 0, −1"),
  [("1", t("Step 1.", "Paso 1."), t("Picture the numbers on the line. The negatives are to the left of 0, and the positives are to the right.", "Imagine los números en la recta. Los negativos quedan a la izquierda del 0 y los positivos, a la derecha.")),
   ("2", t("Step 2.", "Paso 2."), t("The one farthest to the left is the least: −7.", "El que está más a la izquierda es el menor: −7.")),
   ("3", t("Step 3.", "Paso 3."), t("Move to the right: −7, −4, −1, 0, 3.", "Avance hacia la derecha: −7, −4, −1, 0, 3.")),
   ("✓", t("Result.", "Resultado."), "−7 &lt; −4 &lt; −1 &lt; 0 &lt; 3")])}
{caja("ojo", t("Watch out!", "¡Ojo!"), t("<p>Between two negative numbers, the one with the bigger \"number\" is the <strong>smaller</strong> one: −9 &lt; −2. Ask yourself which one is closer to zero. The one closer to zero is greater.</p>",
"<p>Entre dos números negativos, el que tiene el «número» más grande es el <strong>menor</strong>: −9 &lt; −2. Pregúntese cuál está más cerca del cero. El que está más cerca del cero es el mayor.</p>"))}
{practica("p1", t("Practice 1 — Compare", "Práctica 1 — Comparar"), t("Which symbol goes in the blank? &nbsp; −6 ___ −2", "¿Qué símbolo va en el espacio? &nbsp; −6 ___ −2"),
          [("a", "&gt;"), ("b", "="), ("c", "&lt;")])}
{practica("p2", t("Practice 2 — The colder temperature", "Práctica 2 — La temperatura más fría"), t("Which temperature is colder?", "¿Cuál temperatura es más fría?"),
          [("a", "−3 °F"), ("b", "0 °F"), ("c", "−11 °F"), ("d", "4 °F")])}
{enlace(n, t("number-line", "recta"), t("the number line", "la recta numérica"), t("Place integers on the number line, compare them, and put them in order.", "Ubique enteros en la recta, compárelos y ordénelos."))}'''

    s2 = f'''<p>{t("The <strong>absolute value</strong> of a number is its <strong>distance from zero</strong> on the number line. A distance is never negative, so the absolute value is always positive or zero.",
"El <strong>valor absoluto</strong> de un número es su <strong>distancia al cero</strong> en la recta numérica. Una distancia nunca es negativa, así que el valor absoluto siempre es positivo o cero.")}</p>
<p>{t("You write it with two vertical bars around the number, and you read it \"the absolute value of.\"", "Se escribe con dos barras verticales alrededor del número, y se lee «el valor absoluto de».")}</p>
{recta(-7, 7, t("A number line from −7 to 7. The numbers −5 and 5 are marked. Each one is 5 units from zero, one to the left and one to the right.", "Una recta numérica de −7 a 7. Están marcados −5 y 5. Cada uno está a 5 unidades del cero, uno a la izquierda y otro a la derecha."),
       marcas=[(-5, "−5", ROJO, True), (5, "5", VERDE, True)], saltos=[(0, -5, t("5 units", "5 unidades"), ROJO), (0, 5, t("5 units", "5 unidades"), VERDE)], paso=1)}
{tabla(t("Absolute value", "Valor absoluto"), t("Examples of absolute value and what each one means", "Ejemplos de valor absoluto y lo que significa cada uno"),
       [t("You write", "Se escribe"), t("It is", "Es igual a"), t("Because", "Porque")],
       [["|5|", "5", t("5 is 5 units from zero.", "el 5 está a 5 unidades del cero.")],
        ["|−5|", "5", t("−5 is also 5 units from zero.", "el −5 también está a 5 unidades del cero.")],
        ["|0|", "0", t("zero is 0 units from itself.", "el cero está a 0 unidades de sí mismo.")]])}
{caja("ojo", t("Watch out!", "¡Ojo!"), t("<p>The absolute value measures <strong>distance</strong>. That is why |−12| = 12 and |12| = 12: both numbers are exactly the same distance from zero, on opposite sides. But a minus sign <strong>outside</strong> the bars stays: −|−6| means \"the opposite of |−6|,\" so −|−6| = −6.</p>",
"<p>El valor absoluto mide <strong>distancia</strong>. Por eso |−12| = 12 y |12| = 12: los dos números están exactamente a la misma distancia del cero, en lados opuestos. Pero un signo menos <strong>fuera</strong> de las barras se queda: −|−6| quiere decir «el opuesto de |−6|», así que −|−6| = −6.</p>"))}
<h3>{t("Compare sizes with the absolute value", "Comparar tamaños con el valor absoluto")}</h3>
<p>{t("The absolute value tells you the <strong>size</strong> of a quantity, whatever its sign. A debt of $80 (a balance of −$80) is a bigger debt than one of $30 (−$30), because |−80| &gt; |−30|. But on the number line, −80 is the smaller number.",
"El valor absoluto dice el <strong>tamaño</strong> de una cantidad, sea cual sea su signo. Una deuda de $80 (un saldo de −$80) es una deuda más grande que una de $30 (−$30), porque |−80| &gt; |−30|. Pero en la recta numérica, −80 es el número menor.")}</p>
{ejemplo(t("Example: |−7| + |4|", "Ejemplo: |−7| + |4|"),
  [("1", t("Step 1.", "Paso 1."), t("|−7| = 7, the distance from −7 to zero.", "|−7| = 7, la distancia de −7 al cero.")),
   ("2", t("Step 2.", "Paso 2."), t("|4| = 4, the distance from 4 to zero.", "|4| = 4, la distancia de 4 al cero.")),
   ("✓", t("Result.", "Resultado."), "7 + 4 = <strong>11</strong>")])}
{practica("p3", t("Practice 3 — Absolute value", "Práctica 3 — Valor absoluto"), t("What is |−15|?", "¿Cuánto es |−15|?"),
          [("a", "−15"), ("b", "0"), ("c", "15"), ("d", "30")])}
{practica("p4", t("Practice 4 — Two absolute values", "Práctica 4 — Dos valores absolutos"), t("What is |−9| + |−6|?", "¿Cuánto es |−9| + |−6|?"),
          [("a", "15"), ("b", "−15"), ("c", "3"), ("d", "−3")])}
{enlace(n, t("absolute-value", "valor-absoluto"), t("absolute value", "el valor absoluto"), t("Measure the distance from a number to zero, and see why it is never negative.", "Mida la distancia de un número al cero y compruebe por qué nunca es negativa."))}'''

    s3 = f'''<p>{t("Two numbers are <strong>opposites</strong> when they are the same distance from zero but on opposite sides of the number line. The opposite of 6 is −6, and the opposite of −6 is 6. Zero is its own opposite: it is not on either side.",
"Dos números son <strong>opuestos</strong> cuando están a la misma distancia del cero pero en lados contrarios de la recta. El opuesto de 6 es −6, y el opuesto de −6 es 6. El cero es su propio opuesto: no está a ningún lado.")}</p>
{recta(-8, 8, t("A number line from −8 to 8 with 6 and −6 marked, the same distance from zero, on opposite sides.", "Una recta numérica de −8 a 8 con 6 y −6 marcados, a la misma distancia del cero, en lados contrarios."),
       marcas=[(-6, "−6", ROJO, True), (6, "6", AZUL, True)], saltos=[(0, -6, "", ROJO), (0, 6, "", AZUL)], paso=1)}
{caja("tip", t("Key idea", "Idea clave"), t("<p>A number and its opposite always add up to zero: 6 + (−6) = 0. That is why the opposite is also called the <strong>additive inverse</strong>. You will use this idea in the next lesson to add integers.</p>",
"<p>Un número y su opuesto siempre suman cero: 6 + (−6) = 0. Por eso al opuesto también se le llama <strong>inverso aditivo</strong>. Usará esta idea en la próxima lección para sumar enteros.</p>"))}
{ejemplo(t("Example: the opposite and the absolute value", "Ejemplo: el opuesto y el valor absoluto"),
  [("1", t("Step 1.", "Paso 1."), t("The opposite of −13 is 13. Both have an absolute value of 13.", "El opuesto de −13 es 13. Los dos tienen un valor absoluto de 13.")),
   ("2", t("Step 2.", "Paso 2."), t("The opposite of 40 is −40. Both have an absolute value of 40.", "El opuesto de 40 es −40. Los dos tienen un valor absoluto de 40.")),
   ("✓", t("Result.", "Resultado."), t("Two opposites always have the same absolute value.", "Dos opuestos siempre tienen el mismo valor absoluto."))])}
<h3>{t("Two minus signs", "Dos signos menos")}</h3>
<p>{t("A minus sign in front of a number means \"the opposite of.\" So −(−8) means \"the opposite of −8,\" which is 8. Two minus signs in a row cancel each other.",
"El signo «−» delante de un número quiere decir «el opuesto de». Por eso −(−8) se lee «el opuesto de −8», que es 8. Dos signos menos seguidos se cancelan.")}</p>
{ejemplo(t("Example: simplify −(−25)", "Ejemplo: simplifique −(−25)"),
  [("1", t("Step 1.", "Paso 1."), t("−(−25) means \"the opposite of −25.\"", "−(−25) quiere decir «el opuesto de −25».")),
   ("✓", t("Result.", "Resultado."), t("The opposite of −25 is <strong>25</strong>.", "El opuesto de −25 es <strong>25</strong>."))])}
{calc(t("Negative numbers on the calculator", "Los números negativos en la calculadora"), t(f"""<p>The calculator has <strong>two different minus keys</strong>. {T("−")} subtracts. {T("(−)")} writes a negative number. To find −(−25), press {T("(−)")} {T("(")} {T("(−)")} {T("2")}{T("5")} {T(")")} {T("enter")}. The screen shows 25.</p>
<p>If you press {T("−")} to start a negative number, the calculator shows an error. On the GED test, use {T("(−)")} for every negative number.</p>""",
f"""<p>La calculadora tiene <strong>dos teclas distintas para el menos</strong>. {T("−")} resta. {T("(−)")} escribe un número negativo. Para hallar −(−25), pulse {T("(−)")} {T("(")} {T("(−)")} {T("2")}{T("5")} {T(")")} {T("enter")}. La pantalla muestra 25.</p>
<p>Si pulsa {T("−")} para empezar un número negativo, la calculadora da error. En el examen de GED, use {T("(−)")} para cada número negativo.</p>"""))}
{practica("p5", t("Practice 5 — The opposite", "Práctica 5 — El opuesto"), t("What is the opposite of −17?", "¿Cuál es el opuesto de −17?"),
          [("a", "−17"), ("b", "17"), ("c", "0"), ("d", "1/17")])}
{practica("p6", t("Practice 6 — Two minus signs", "Práctica 6 — Dos signos menos"), t("What is −(−42)?", "¿Cuánto es −(−42)?"),
          [("a", "−42"), ("b", "−84"), ("c", "0"), ("d", "42")])}
{enlace(n, t("opposites", "opuestos"), t("opposites", "los opuestos"), t("Reflect numbers to the other side of zero and practice the double minus sign.", "Refleje números al otro lado del cero y practique el doble signo menos."))}'''

    secciones = [("s-" + t("number-line", "recta"), t("The full number line", "La recta numérica completa"), s1),
                 ("s-" + t("absolute-value", "valor-absoluto"), t("Absolute value: the distance from zero", "El valor absoluto: la distancia al cero"), s2),
                 ("s-" + t("opposites", "opuestos"), t("Opposites", "Los opuestos"), s3)]

    lesson = {"next": t("Lesson 1.2", "Lección 1.2"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Look at the number line: which one is farther to the right? Between two negatives, the one closer to zero is greater.", "Mire la recta: ¿cuál está más a la derecha? Entre dos negativos, el que está más cerca del cero es el mayor."),
                                   "b": t("They are different numbers, so they are not equal.", "Son números distintos, así que no son iguales.")},
             "right": t("−6 is to the left of −2, so −6 is less: −6 &lt; −2.", "−6 está a la izquierda de −2, así que es menor: −6 &lt; −2."),
             "solution": t("On the number line, −6 is farther to the left than −2. The number to the left is the smaller one: −6 &lt; −2.", "En la recta, −6 está más a la izquierda que −2. El número de la izquierda es el menor: −6 &lt; −2.")},
      "p2": {"ok": "c", "hints": {"a": t("−3 °F is cold, but there is a lower temperature in the list.", "−3 °F es frío, pero hay una temperatura más baja en la lista."),
                                   "b": t("0 °F is higher than any temperature below zero.", "0 °F es más alto que cualquier temperatura bajo cero."),
                                   "d": t("4 °F is above zero. Look for the lowest temperature.", "4 °F está sobre cero. Busque la temperatura más baja.")},
             "right": t("−11 °F is the lowest on the thermometer, so it is the coldest.", "−11 °F es la más baja del termómetro, así que es la más fría."),
             "solution": t("The colder temperature is the lower one. In order: −11 &lt; −3 &lt; 0 &lt; 4. The coldest is −11 °F.", "La temperatura más fría es la más baja. En orden: −11 &lt; −3 &lt; 0 &lt; 4. La más fría es −11 °F.")},
      "p3": {"ok": "c", "hints": {"a": t("A distance is never negative.", "Una distancia nunca es negativa."),
                                   "b": t("Only zero has an absolute value of 0.", "Solo el cero tiene valor absoluto 0."),
                                   "d": t("−15 is 15 units from zero, not 30.", "−15 está a 15 unidades del cero, no a 30.")},
             "right": t("−15 is 15 units from zero.", "−15 está a 15 unidades del cero."),
             "solution": t("The absolute value is the distance from zero. −15 is 15 units from zero, so |−15| = 15.", "El valor absoluto es la distancia al cero. −15 está a 15 unidades del cero, así que |−15| = 15.")},
      "p4": {"ok": "a", "hints": {"b": t("Each absolute value is positive: |−9| = 9 and |−6| = 6. Now add them.", "Cada valor absoluto es positivo: |−9| = 9 y |−6| = 6. Ahora súmelos."),
                                   "c": t("You subtracted. The problem adds the two absolute values.", "Restó. El problema suma los dos valores absolutos."),
                                   "d": t("First find each absolute value; both are positive.", "Primero halle cada valor absoluto; los dos son positivos.")},
             "right": t("|−9| = 9 and |−6| = 6, so 9 + 6 = 15.", "|−9| = 9 y |−6| = 6, así que 9 + 6 = 15."),
             "solution": t("First the absolute values: |−9| = 9 and |−6| = 6. Then add: 9 + 6 = 15.", "Primero los valores absolutos: |−9| = 9 y |−6| = 6. Después se suma: 9 + 6 = 15.")},
      "p5": {"ok": "b", "hints": {"a": t("That is the same number. The opposite is on the other side of zero.", "Ese es el mismo número. El opuesto está al otro lado del cero."),
                                   "c": t("Zero is the opposite only of zero.", "El cero es el opuesto solamente del cero."),
                                   "d": t("1/17 is the reciprocal, a different idea. The opposite changes the side of zero.", "1/17 es el recíproco, otra idea distinta. El opuesto cambia el lado del cero.")},
             "right": t("17 is the same distance from zero as −17, on the other side.", "17 está a la misma distancia del cero que −17, del otro lado."),
             "solution": t("The opposite is the same distance from zero, on the other side: the opposite of −17 is 17. Check: −17 + 17 = 0.", "El opuesto está a la misma distancia del cero, del otro lado: el opuesto de −17 es 17. Compruebe: −17 + 17 = 0.")},
      "p6": {"ok": "d", "hints": {"a": t("The first minus sign means \"the opposite of.\" What is the opposite of −42?", "El primer signo menos quiere decir «el opuesto de». ¿Cuál es el opuesto de −42?"),
                                   "b": t("Nothing is being added here. −(−42) means \"the opposite of −42.\"", "Aquí no se suma nada. −(−42) quiere decir «el opuesto de −42»."),
                                   "c": t("A number plus its opposite is 0, but this is only the opposite of −42.", "Un número más su opuesto da 0, pero esto es solo el opuesto de −42.")},
             "right": t("The opposite of −42 is 42. Two minus signs in a row cancel.", "El opuesto de −42 es 42. Dos signos menos seguidos se cancelan."),
             "solution": t("−(−42) is \"the opposite of −42,\" which is 42.", "−(−42) es «el opuesto de −42», que es 42.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("−2 is close to zero. Look for the number farthest to the left.", "−2 está cerca del cero. Busque el número que está más a la izquierda."),
                                 "b": t("Zero is greater than any negative number.", "El cero es mayor que cualquier número negativo."),
                                 "d": t("5 is the greatest of the four.", "5 es el mayor de los cuatro.")},
            "solution": t("On the number line, −9 is the farthest to the left, so it is the least.", "En la recta, −9 es el que está más a la izquierda, así que es el menor.")},
      "B": {"ok": "b", "hints": {"a": t("Between two negatives, the one closer to zero is greater. Which one is closer to zero?", "Entre dos negativos, el más cercano al cero es el mayor. ¿Cuál está más cerca del cero?"),
                                 "c": t("They are different numbers.", "Son números distintos."),
                                 "d": t("Any two integers can be compared on the number line.", "Dos enteros cualesquiera se pueden comparar en la recta.")},
            "solution": t("−4 is to the left of −1, so −4 &lt; −1.", "−4 está a la izquierda de −1, así que −4 &lt; −1.")},
      "C": {"ok": "d", "hints": {"a": t("The absolute value is a distance, and a distance is never negative.", "El valor absoluto es una distancia, y una distancia nunca es negativa."),
                                 "b": t("Only zero has an absolute value of 0.", "Solo el cero tiene valor absoluto 0."),
                                 "c": t("−20 is 20 units from zero, not 40.", "−20 está a 20 unidades del cero, no a 40.")},
            "solution": t("−20 is 20 units from zero, so |−20| = 20.", "−20 está a 20 unidades del cero, así que |−20| = 20.")},
      "D": {"ok": "a", "hints": {"b": t("That is the same number. The opposite is on the other side of zero.", "Ese es el mismo número. El opuesto está al otro lado del cero."),
                                 "c": t("Only zero is the opposite of zero.", "Solo el cero es el opuesto del cero."),
                                 "d": t("The opposite keeps the same distance from zero: 31 units.", "El opuesto conserva la misma distancia al cero: 31 unidades.")},
            "solution": t("The opposite of 31 is −31: the same distance from zero, on the other side.", "El opuesto de 31 es −31: la misma distancia al cero, del otro lado.")},
      "E": {"ok": "c", "hints": {"a": t("The first minus sign means \"the opposite of.\" The opposite of −14 is on the positive side.", "El primer signo menos quiere decir «el opuesto de». El opuesto de −14 está del lado positivo."),
                                 "b": t("Nothing is being added. −(−14) is the opposite of −14.", "Aquí no se suma nada. −(−14) es el opuesto de −14."),
                                 "d": t("−14 + 14 would be 0, but this asks only for the opposite of −14.", "−14 + 14 daría 0, pero aquí se pide solo el opuesto de −14.")},
            "solution": t("−(−14) is the opposite of −14, which is 14.", "−(−14) es el opuesto de −14, que es 14.")},
      "F": {"ok": "b", "hints": {"a": t("−7 is farther below zero than −2. Is that warmer?", "−7 está más abajo del cero que −2. ¿Eso es más cálido?"),
                                 "c": t("−7 and −2 are different temperatures.", "−7 y −2 son temperaturas distintas."),
                                 "d": t("You can compare them on a thermometer, like on a number line.", "Se pueden comparar en un termómetro, como en una recta numérica.")},
            "solution": t("−7 is lower than −2 on the thermometer, so −7 °F is colder.", "−7 está más abajo que −2 en el termómetro, así que −7 °F es más fría.")},
      "G": {"ok": "d", "hints": {"a": t("You subtracted. First find each absolute value, then add.", "Restó. Primero halle cada valor absoluto y después sume."),
                                 "b": t("Each absolute value is positive, so the sum is positive.", "Cada valor absoluto es positivo, así que la suma es positiva."),
                                 "c": t("You multiplied. The problem adds.", "Multiplicó. El problema suma.")},
            "solution": t("|−6| = 6 and |5| = 5, so 6 + 5 = 11.", "|−6| = 6 y |5| = 5, así que 6 + 5 = 11.")},
      "H": {"ok": "a", "hints": {"b": t("−8 is farther left than −3, so −8 comes first.", "−8 está más a la izquierda que −3, así que va primero."),
                                 "c": t("That is from greatest to least. Start with the one farthest to the left.", "Ese orden va de mayor a menor. Empiece por el que está más a la izquierda."),
                                 "d": t("Zero is greater than every negative number.", "El cero es mayor que cualquier número negativo.")},
            "solution": t("From left to right on the number line: −8, −3, 0, 2.", "De izquierda a derecha en la recta: −8, −3, 0, 2.")}
     }}

    quiz = [
     ("A", t("Which of these numbers is the <strong>least</strong>?", "¿Cuál de estos números es el <strong>menor</strong>?"), [("a", "−2"), ("b", "0"), ("c", "−9"), ("d", "5")]),
     ("B", t("Which comparison is true?", "¿Qué comparación es verdadera?"), [("a", "−4 &gt; −1"), ("b", "−4 &lt; −1"), ("c", "−4 = −1"), ("d", t("They cannot be compared.", "No se pueden comparar."))]),
     ("C", t("What is |−20|?", "¿Cuánto es |−20|?"), [("a", "−20"), ("b", "0"), ("c", "40"), ("d", "20")]),
     ("D", t("What is the opposite of 31?", "¿Cuál es el opuesto de 31?"), [("a", "−31"), ("b", "31"), ("c", "0"), ("d", "−62")]),
     ("E", t("What is −(−14)?", "¿Cuánto es −(−14)?"), [("a", "−14"), ("b", "−28"), ("c", "14"), ("d", "0")]),
     ("F", t("Compared with −2 °F, a temperature of −7 °F is:", "Comparada con −2 °F, una temperatura de −7 °F es:"), [("a", t("warmer", "más cálida")), ("b", t("colder", "más fría")), ("c", t("the same", "igual")), ("d", t("impossible to compare", "imposible de comparar"))]),
     ("G", t("What is |−6| + |5|?", "¿Cuánto es |−6| + |5|?"), [("a", "1"), ("b", "−11"), ("c", "30"), ("d", "11")]),
     ("H", t("Put −3, 2, −8, and 0 in order from <strong>least to greatest</strong>.", "Ordene −3, 2, −8 y 0 de <strong>menor a mayor</strong>."), [("a", "−8, −3, 0, 2"), ("b", "−3, −8, 0, 2"), ("c", "2, 0, −3, −8"), ("d", "0, −3, −8, 2")])]

    return B.pagina_leccion(n, 1, t(*TEMA),
        t("The number line, absolute value, and opposites", "La recta numérica, el valor absoluto y los opuestos"),
        t("Numbers to the left of zero: place them on the number line, compare them, and measure how far they are from zero.", "Los números a la izquierda del cero: ubíquelos en la recta, compárelos y mida qué tan lejos están del cero."),
        ("🎯", t("No calculator", "Sin calculadora")),
        [t("<strong>Place</strong> positive and negative integers on the number line.", "<strong>Ubicar</strong> enteros positivos y negativos en la recta numérica."),
         t("<strong>Compare and order</strong> integers with the symbols &gt;, &lt;, and =.", "<strong>Comparar y ordenar</strong> enteros con los símbolos &gt;, &lt; e =."),
         t("<strong>Find</strong> the absolute value of a number, and explain it as a distance from zero.", "<strong>Hallar</strong> el valor absoluto de un número y explicarlo como su distancia al cero."),
         t("<strong>Name</strong> the opposite (additive inverse) of any integer.", "<strong>Identificar</strong> el opuesto (inverso aditivo) de cualquier entero."),
         t("<strong>Use</strong> integers to describe real situations: temperature, money, and height.", "<strong>Usar</strong> enteros para describir situaciones reales: temperatura, dinero y altura.")],
        secciones,
        (t("Write and solve ten exercises that compare or order integers with &gt;, &lt;, and =; five that find an absolute value, like |−8| + |3|; and five that find an opposite, including some with two minus signs, like −(−9). Check each one on a number line you draw.",
           "Escriba y resuelva diez ejercicios de comparar u ordenar enteros con &gt;, &lt; e =; cinco de hallar un valor absoluto, como |−8| + |3|; y cinco de hallar un opuesto, incluidos algunos con dos signos menos, como −(−9). Compruebe cada uno en una recta numérica que dibuje usted."),
         t("Find three situations in your week that use negative numbers: a weather report, a bank balance, a basement floor. Write each one as an integer, and say what zero means in each case.",
           "Busque en su semana tres situaciones que usen números negativos: el pronóstico del tiempo, el saldo del banco, un sótano. Escriba cada una como un entero y diga qué significa el cero en cada caso.")),
        quiz,
        t("Self-check checklist for the number line, absolute value, and opposites", "Lista de autoevaluación de la recta numérica, el valor absoluto y los opuestos"),
        t("Self-check checklist: skills for the number line, absolute value, and opposites", "Lista de autoevaluación: destrezas con la recta numérica, el valor absoluto y los opuestos"),
        [(t("Place integers on the number line", "Ubicar enteros en la recta"), t("I place positives and negatives without help and explain the order.", "Ubico positivos y negativos sin ayuda y explico el orden."), t("I place negatives if I draw the line first.", "Ubico los negativos si primero dibujo la recta."), t("I mix up where the negatives go.", "Confundo dónde van los negativos.")),
         (t("Compare integers", "Comparar enteros"), t("I compare any two integers with the right symbol.", "Comparo dos enteros cualesquiera con el símbolo correcto."), t("I make mistakes when both numbers are negative.", "Me equivoco cuando los dos números son negativos."), t("I can compare only positive numbers.", "Solo sé comparar números positivos.")),
         (t("Absolute value", "Valor absoluto"), t("I find it and explain it as a distance from zero.", "Lo hallo y lo explico como distancia al cero."), t("I find it for single numbers, but not in expressions.", "Lo hallo con números sueltos, pero no en expresiones."), t("I do not recognize the bars yet.", "Todavía no reconozco las barras.")),
         (t("Opposites", "Opuestos"), t("I find opposites, including two minus signs, and use them in real situations.", "Hallo opuestos, también con dos signos menos, y los uso en situaciones reales."), t("I find simple opposites, but two minus signs confuse me.", "Hallo opuestos sencillos, pero los dos signos menos me confunden."), t("I do not know how to find the opposite yet.", "Todavía no sé hallar el opuesto."))],
        t("<p>You built the ground for all of Level 2: the full number line, comparing integers, absolute value as a distance from zero, and opposites. Remember one idea above all: <strong>a number and its opposite always add up to zero</strong>.</p>\n<p>In <strong>Lesson 1.2 · Adding and subtracting integers</strong> you will put that idea to work. You will add with the number line and with two-color counters, and you will discover that <strong>subtracting is adding the opposite</strong>.</p>",
          "<p>Construyó la base de todo el Nivel 2: la recta numérica completa, la comparación de enteros, el valor absoluto como distancia al cero y los opuestos. Recuerde una idea por encima de todas: <strong>un número y su opuesto siempre suman cero</strong>.</p>\n<p>En la <strong>Lección 1.2 · Suma y resta de enteros con signo</strong> pondrá esa idea a trabajar. Sumará con la recta numérica y con fichas de dos colores, y descubrirá que <strong>restar es sumar el opuesto</strong>.</p>"),
        ("1-2", ("", t("Lesson 1.2 · Adding and subtracting integers", "Lección 1.2 · Suma y resta de enteros con signo"))),
        [(t("integers", "números enteros"), t("The whole numbers, their opposites, and zero: …, −3, −2, −1, 0, 1, 2, 3, …", "Los números naturales, sus opuestos y el cero: …, −3, −2, −1, 0, 1, 2, 3, …")),
         (t("positive number", "número positivo"), t("A number greater than zero. It is to the right of zero on the number line.", "Un número mayor que cero. Está a la derecha del cero en la recta numérica.")),
         (t("negative number", "número negativo"), t("A number less than zero. It is to the left of zero and has a minus sign: −4.", "Un número menor que cero. Está a la izquierda del cero y lleva el signo menos: −4.")),
         (t("number line", "recta numérica"), t("A line where every point is a number. The numbers grow to the right.", "Una línea en la que cada punto es un número. Los números crecen hacia la derecha.")),
         (t("absolute value", "valor absoluto"), t("The distance from a number to zero. It is never negative: |−5| = 5.", "La distancia de un número al cero. Nunca es negativo: |−5| = 5.")),
         (t("opposite (additive inverse)", "opuesto (inverso aditivo)"), t("The number at the same distance from zero, on the other side. A number plus its opposite is 0.", "El número que está a la misma distancia del cero, del otro lado. Un número más su opuesto da 0."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "A": "Number A", "B": "Number B",
  "mismo": "A and B are at the same point: {a} = {b}.",
  "derecha": "<strong>{x}</strong> is farther to the right, so it is greater: {a} {s} {b}.",
  "dosNeg": " Between two negative numbers, the one closer to zero is greater.",
  "vozRC": "Number line with A at {a} and B at {b}.",
  "fria": "Which temperature is colder: {a} °F or {b} °F?", "iguales": "They are the same",
  "bienFria": "The colder one is lower on the thermometer: {f} °F.", "pistaFria": "Picture a thermometer. The colder temperature is the lower one.",
  "compara": "Which symbol goes in the blank? &nbsp; {a} ___ {b}",
  "pistaDosNeg": "Careful: between two negatives, the one with the bigger \"number\" is the smaller one. Which one is closer to zero?",
  "pistaComp": "Which one is farther to the right on the number line?",
  "bienComp": "{M} is farther to the right on the number line.", "mismoNum": "They are the same number.",
  "subir": "Move {v} up", "bajar": "Move {v} down",
  "ordenBien": "Correct order: ", "ordenPista": "Some numbers are not in place yet (marked in red). Start with the one farthest to the left: the negative farthest from zero. Fix the order and check again.",
  "ordenMal": "The correct order is: ", "ordenMal2": " Start with the negative farthest from zero.",
  "vozVA": "Number line: {n} is {d} units from zero.",
  "unidad": "unit", "unidades": "units",
  "cero0": "Zero is 0 units from itself.",
  "salidaVA": "{n} is {d} {u} from zero. Its opposite, {o} (in gray), is the same distance away: |{o}| = {d}.",
  "solAbs1": "{a} is {r} units from zero, so |{a}| = {r}.", "distNeg": "A distance is never negative.",
  "solAbs2": "|{a}| = {x} and |{b}| = {y}; then {x} + {y} = {r}.", "antesSumar": "First find each absolute value, then add.",
  "solAbs3": "|{a}| = {x} and |{b}| = {y}; then {x} − {y} = {r}.",
  "solAbs4": "|{a}| = {k}, and the minus sign outside the bars stays: −{k}.", "fuera": "The minus sign is outside the bars. It stays after you find the absolute value.",
  "deuda": "An account has a balance of −${d}. How many dollars does the person owe? (That is, what is |−{d}|?)", "solDeuda": "|−{d}| = {d}: the person owes ${d}.",
  "vozOP": "Number line with {n} and its opposite {o}, the same distance from zero.",
  "propio": "Zero is its own opposite: it is in the center.",
  "salidaOP": "The opposite of {n} is <strong>{o}</strong>: both are {d} units from zero, on opposite sides.",
  "suman": "{n} + {po} = 0. And −({n}) = {o}.",
  "opDe": "What is the opposite of {v}?", "bienOp": "The opposite of {v} is {o}: the same distance from zero, on the other side.",
  "pistaOp": "The opposite is the same distance from zero, on the other side.",
  "dobleQ": "What is −(−{k})?", "bienDoble": "−(−{k}) is \"the opposite of −{k},\" which is {k}.", "pistaDoble": "Read the first minus sign as \"the opposite of.\"",
  "propioQ": "Which number is its own opposite?", "ninguno": "None of them", "bienPropio": "Zero: it is not on either side of zero.", "pistaPropio": "Which number is in the center of the number line?",
  "sumaQ": "{a} + {k} =", "bienSuma": "A number and its opposite always add up to zero.", "pistaSuma": "{k} is the opposite of {a}. What do a number and its opposite add up to?",
  "comunQ": "{k} and −{k} are opposites. What do they have in common?",
  "c1": "They have the same absolute value", "c2": "They have the same sign", "c3": "They add up to {d}", "c4": "One is double the other",
  "bienComun": "Both are {k} units from zero: |{k}| = |−{k}| = {k}.", "pistaComun": "Think about their distance from zero."
 },
 "es": {
  "A": "Número A", "B": "Número B",
  "mismo": "A y B están en el mismo punto: {a} = {b}.",
  "derecha": "<strong>{x}</strong> está más a la derecha, así que es mayor: {a} {s} {b}.",
  "dosNeg": " Entre dos números negativos, el que está más cerca del cero es el mayor.",
  "vozRC": "Recta numérica con A en {a} y B en {b}.",
  "fria": "¿Cuál temperatura es más fría: {a} °F o {b} °F?", "iguales": "Son iguales",
  "bienFria": "La más fría es la que está más abajo en el termómetro: {f} °F.", "pistaFria": "Imagine un termómetro. La temperatura más fría es la más baja.",
  "compara": "¿Qué símbolo va en el espacio? &nbsp; {a} ___ {b}",
  "pistaDosNeg": "Cuidado: entre dos negativos, el que tiene el «número» más grande es el menor. ¿Cuál está más cerca del cero?",
  "pistaComp": "¿Cuál está más a la derecha en la recta numérica?",
  "bienComp": "{M} está más a la derecha en la recta numérica.", "mismoNum": "Son el mismo número.",
  "subir": "Subir el {v}", "bajar": "Bajar el {v}",
  "ordenBien": "Orden correcto: ", "ordenPista": "Algunos números todavía no están en su lugar (marcados en rojo). Empiece por el que está más a la izquierda: el negativo más lejano del cero. Corrija el orden y compruebe otra vez.",
  "ordenMal": "El orden correcto es: ", "ordenMal2": " Se empieza por el negativo más lejano del cero.",
  "vozVA": "Recta numérica: {n} está a {d} unidades del cero.",
  "unidad": "unidad", "unidades": "unidades",
  "cero0": "El cero está a 0 unidades de sí mismo.",
  "salidaVA": "{n} está a {d} {u} del cero. Su opuesto, {o} (en gris), está a la misma distancia: |{o}| = {d}.",
  "solAbs1": "{a} está a {r} unidades del cero, así que |{a}| = {r}.", "distNeg": "Una distancia nunca es negativa.",
  "solAbs2": "|{a}| = {x} y |{b}| = {y}; después, {x} + {y} = {r}.", "antesSumar": "Primero halle cada valor absoluto y después sume.",
  "solAbs3": "|{a}| = {x} y |{b}| = {y}; después, {x} − {y} = {r}.",
  "solAbs4": "|{a}| = {k}, y el signo menos de afuera se queda: −{k}.", "fuera": "El signo menos está fuera de las barras. Se queda después de hallar el valor absoluto.",
  "deuda": "Una cuenta tiene un saldo de −${d}. ¿Cuántos dólares debe la persona? (Es decir, ¿cuánto es |−{d}|?)", "solDeuda": "|−{d}| = {d}: la persona debe ${d}.",
  "vozOP": "Recta numérica con {n} y su opuesto {o}, a la misma distancia del cero.",
  "propio": "El cero es su propio opuesto: está en el centro.",
  "salidaOP": "El opuesto de {n} es <strong>{o}</strong>: los dos están a {d} unidades del cero, en lados contrarios.",
  "suman": "{n} + {po} = 0. Y −({n}) = {o}.",
  "opDe": "¿Cuál es el opuesto de {v}?", "bienOp": "El opuesto de {v} es {o}: la misma distancia al cero, del otro lado.",
  "pistaOp": "El opuesto está a la misma distancia del cero, del otro lado.",
  "dobleQ": "¿Cuánto es −(−{k})?", "bienDoble": "−(−{k}) es «el opuesto de −{k}», que es {k}.", "pistaDoble": "Lea el primer signo menos como «el opuesto de».",
  "propioQ": "¿Qué número es su propio opuesto?", "ninguno": "Ninguno", "bienPropio": "El cero: no está a ningún lado del cero.", "pistaPropio": "¿Qué número está en el centro de la recta?",
  "sumaQ": "{a} + {k} =", "bienSuma": "Un número y su opuesto siempre suman cero.", "pistaSuma": "{k} es el opuesto de {a}. ¿Cuánto suman un número y su opuesto?",
  "comunQ": "{k} y −{k} son opuestos. ¿Qué tienen en común?",
  "c1": "Tienen el mismo valor absoluto", "c2": "Tienen el mismo signo", "c3": "Suman {d}", "c4": "Uno es el doble del otro",
  "bienComun": "Los dos están a {k} unidades del cero: |{k}| = |−{k}| = {k}.", "pistaComun": "Piense en su distancia al cero."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function simb(a, b){ return a < b ? "&lt;" : (a > b ? "&gt;" : "="); }

/* ============ MODULE 1 · the number line ============ */
function pintaRC(){
  var a = +$("rc-a").value, b = +$("rc-b").value;
  $("rc-av").textContent = ent(a); $("rc-bv").textContent = ent(b);
  $("rc-svg").innerHTML = rectaEnt(-10, 10, [{ v: a, txt: "A", color: "#b71c1c" }, { v: b, txt: "B", color: "#0d47a1", abajo: a === b }], [], F(TXT.vozRC, { a: ent(a), b: ent(b) }));
  var h;
  if (a === b) h = F(TXT.mismo, { a: ent(a), b: ent(b) });
  else { h = F(TXT.derecha, { x: a > b ? "A" : "B", a: ent(a), s: simb(a, b), b: ent(b) }); if (a < 0 && b < 0) h += TXT.dosNeg; }
  $("rc-salida").innerHTML = '<div class="linea">' + h + '</div>';
}
function genComparar(){
  var tipo = aleatorio(1, 3), a, b;
  if (tipo === 3){
    a = -aleatorio(1, 20); b = -aleatorio(1, 20); while (b === a) b = -aleatorio(1, 20);
    var fria = Math.min(a, b);
    return { enun: F(TXT.fria, { a: ent(a), b: ent(b) }), opciones: [{ html: ent(a) + " °F", clave: "t" + a }, { html: ent(b) + " °F", clave: "t" + b }, { html: TXT.iguales, clave: "=" }],
      correcta: "t" + fria, pista: TXT.pistaFria, bien: F(TXT.bienFria, { f: ent(fria) }), mal: F(TXT.bienFria, { f: ent(fria) }) };
  }
  if (tipo === 1){ a = -aleatorio(1, 15); b = -aleatorio(1, 15); while (b === a) b = -aleatorio(1, 15); }
  else { a = azarEnt(-15, 15); b = azarEnt(-15, 15); if (Math.random() < 0.15) b = a; }
  var r = a < b ? "<" : (a > b ? ">" : "=");
  var o = [{ html: "&lt;", clave: "<" }, { html: "&gt;", clave: ">" }, { html: "=", clave: "=" }], pistas = {};
  if (a < 0 && b < 0) pistas[r === "<" ? ">" : "<"] = TXT.pistaDosNeg;
  var exp = a === b ? TXT.mismoNum : F(TXT.bienComp, { M: ent(Math.max(a, b)) });
  return { enun: F(TXT.compara, { a: ent(a), b: ent(b) }), opciones: o, enOrden: true, correcta: r, pistas: pistas, pista: TXT.pistaComp, bien: exp, mal: exp + " " + ent(a) + " " + simb(a, b) + " " + ent(b) + "." };
}
var OR = { lista: [], primero: 0, pista: 0, total: 0, resuelto: false, intentos: 0 };
function nuevoOR(){
  var s = []; while (s.length < 5){ var n = azarEnt(-15, 15); if (s.indexOf(n) < 0) s.push(n); }
  if (s.filter(function(x){ return x < 0; }).length < 2){ s[0] = -Math.abs(s[0]) || -3; s[1] = -Math.abs(s[1]) || -8; if (s[0] === s[1]) s[1]--; }
  OR.lista = baraja(s); OR.resuelto = false; OR.intentos = 0; $("or-fb").className = "fb"; $("or-fb").innerHTML = "";
  $("or-comprobar").disabled = false; pintaOR();
}
function pintaOR(foco, marcas){
  var ol = $("or-lista"); ol.innerHTML = "";
  OR.lista.forEach(function(v, i){
    var li = document.createElement("li");
    if (marcas) li.className = marcas[i] ? "bien" : "mal";
    li.innerHTML = '<span class="nombre">' + ent(v) + '</span><span class="flechas"><button type="button" class="btn-sec" data-i="' + i + '" data-d="-1" aria-label="' + F(TXT.subir, { v: ent(v) }) + '">↑</button><button type="button" class="btn-sec" data-i="' + i + '" data-d="1" aria-label="' + F(TXT.bajar, { v: ent(v) }) + '">↓</button></span>';
    ol.appendChild(li);
  });
  ol.querySelectorAll("button").forEach(function(b){
    var i = +b.getAttribute("data-i"), d = +b.getAttribute("data-d");
    b.disabled = OR.resuelto || (d < 0 && i === 0) || (d > 0 && i === OR.lista.length - 1);
    b.addEventListener("click", function(){ var j = i + d, x = OR.lista[i]; OR.lista[i] = OR.lista[j]; OR.lista[j] = x; pintaOR({ i: j, d: d }); });
  });
  if (foco){ var bb = ol.querySelector('button[data-i="' + foco.i + '"][data-d="' + foco.d + '"]'); if (!bb || bb.disabled) bb = ol.querySelector('button[data-i="' + foco.i + '"]:not([disabled])'); if (bb) bb.focus(); }
}
function compruebaOR(){
  if (OR.resuelto) return;
  var bien = OR.lista.slice().sort(function(a, b){ return a - b; }), marcas = OR.lista.map(function(v, i){ return v === bien[i]; }), ok = marcas.every(Boolean), fb = $("or-fb");
  OR.intentos++;
  if (ok){
    OR.resuelto = true; OR.total++; if (OR.intentos === 1) OR.primero++; else OR.pista++;
    fb.className = "fb bien"; fb.innerHTML = TX.bien + TXT.ordenBien + bien.map(ent).join(" &lt; ") + ". <em>" + (OR.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
  } else if (OR.intentos === 1){
    fb.className = "fb pista"; fb.innerHTML = TX.todavia + TXT.ordenPista; pintaOR(null, marcas); return;
  } else {
    OR.resuelto = true; OR.total++;
    fb.className = "fb mal"; fb.innerHTML = TX.asi + TXT.ordenMal + bien.map(ent).join(" &lt; ") + "." + TXT.ordenMal2;
  }
  $("or-comprobar").disabled = OR.resuelto;
  $("or-marcador").textContent = TX.resueltos(OR.primero + OR.pista, OR.primero, OR.total);
  pintaOR(null, marcas);
}

/* ============ MODULE 2 · absolute value ============ */
function pintaVA(){
  var n = +$("va-n").value, d = Math.abs(n); $("va-nv").textContent = ent(n);
  $("va-svg").innerHTML = rectaEnt(-10, 10, [{ v: n, txt: ent(n), color: "#b71c1c", abajo: true }, { v: -n, txt: n === 0 ? "" : ent(-n), color: "#757575", abajo: true }], n === 0 ? [] : [{ de: 0, a: n, txt: d + " " + (d === 1 ? TXT.unidad : TXT.unidades), color: "#b71c1c" }],
    F(TXT.vozVA, { n: ent(n), d: d }), { de: 0, a: n, color: "#ffcdd2" });
  $("va-salida").innerHTML = '<div class="linea grande">|' + ent(n) + '| = ' + d + '</div><div class="linea">' + (n === 0 ? TXT.cero0 : F(TXT.salidaVA, { n: ent(n), d: d, u: d === 1 ? TXT.unidad : TXT.unidades, o: ent(-n) })) + '</div>';
}
function genAbsoluto(){
  var tipo = aleatorio(1, 5), a = azarEnt(-30, 30, true), b = azarEnt(-20, 20, true), enun, res, sol, pistas = [];
  if (tipo === 1){ if (a > 0 && Math.random() < 0.7) a = -a; res = Math.abs(a); enun = "|" + ent(a) + "| ="; sol = F(TXT.solAbs1, { a: ent(a), r: res }); if (a < 0) pistas.push({ v: a, msg: TXT.distNeg }); }
  else if (tipo === 2){ res = Math.abs(a) + Math.abs(b); enun = "|" + ent(a) + "| + |" + ent(b) + "| ="; sol = F(TXT.solAbs2, { a: ent(a), b: ent(b), x: Math.abs(a), y: Math.abs(b), r: res }); if (Math.abs(a + b) !== res) pistas.push({ v: Math.abs(a + b), msg: TXT.antesSumar }); if (a + b !== res) pistas.push({ v: a + b, msg: TXT.antesSumar }); }
  else if (tipo === 3){ var x = Math.max(Math.abs(a), Math.abs(b)), y = Math.min(Math.abs(a), Math.abs(b)), A = Math.abs(a) === x ? a : b, Bb = Math.abs(a) === x ? b : a; res = x - y; enun = "|" + ent(A) + "| − |" + ent(Bb) + "| ="; sol = F(TXT.solAbs3, { a: ent(A), b: ent(Bb), x: x, y: y, r: res }); }
  else if (tipo === 4){ var k = aleatorio(2, 25); res = -k; enun = "−|" + ent(-k) + "| ="; sol = F(TXT.solAbs4, { a: ent(-k), k: k }); pistas.push({ v: k, msg: TXT.fuera }); }
  else { var dd = aleatorio(20, 200); res = dd; enun = F(TXT.deuda, { d: dd }); sol = F(TXT.solDeuda, { d: dd }); pistas.push({ v: -dd, msg: TXT.distNeg }); }
  return { enun: enun, correcta: String(res), solucion: sol, evalua: numE(res, pistas) };
}

/* ============ MODULE 3 · opposites ============ */
function pintaOP(){
  var n = +$("op-n").value; $("op-nv").textContent = ent(n);
  $("op-svg").innerHTML = rectaEnt(-10, 10, [{ v: n, txt: ent(n), color: "#b71c1c", abajo: true }, { v: -n, txt: n === 0 ? "" : ent(-n), color: "#0d47a1", abajo: true }], n === 0 ? [] : [{ de: 0, a: n, color: "#b71c1c" }, { de: 0, a: -n, color: "#0d47a1" }],
    F(TXT.vozOP, { n: ent(n), o: ent(-n) }));
  $("op-salida").innerHTML = '<div class="linea">' + (n === 0 ? TXT.propio : F(TXT.salidaOP, { n: ent(n), o: ent(-n), d: Math.abs(n) })) + '</div><div class="linea">' + F(TXT.suman, { n: ent(n), po: par(-n), o: ent(-n) }) + '</div>';
}
function genOpuesto(){
  var tipo = aleatorio(1, 5), k = aleatorio(2, 50);
  function op(v){ return { html: ent(v), clave: "n" + v }; }
  if (tipo === 1){ var v = elige([k, -k]); return { enun: F(TXT.opDe, { v: ent(v) }), opciones: [op(-v), op(v), op(0), op(2 * v)], correcta: "n" + (-v), pista: TXT.pistaOp, bien: F(TXT.bienOp, { v: ent(v), o: ent(-v) }), mal: F(TXT.bienOp, { v: ent(v), o: ent(-v) }) }; }
  if (tipo === 2) return { enun: F(TXT.dobleQ, { k: k }), opciones: [op(k), op(-k), op(-2 * k), op(0)], correcta: "n" + k, pista: TXT.pistaDoble, bien: F(TXT.bienDoble, { k: k }), mal: F(TXT.bienDoble, { k: k }) };
  if (tipo === 3) return { enun: TXT.propioQ, opciones: [op(0), op(1), op(-1), { html: TXT.ninguno, clave: "x" }], correcta: "n0", pista: TXT.pistaPropio, bien: TXT.bienPropio, mal: TXT.bienPropio };
  if (tipo === 4) return { enun: F(TXT.sumaQ, { a: ent(-k), k: k }), opciones: [op(0), op(2 * k), op(-2 * k), op(k)], correcta: "n0", pista: F(TXT.pistaSuma, { a: ent(-k), k: k }), bien: TXT.bienSuma, mal: TXT.bienSuma };
  return { enun: F(TXT.comunQ, { k: k }), opciones: [{ html: TXT.c1, clave: "a" }, { html: TXT.c2, clave: "s" }, { html: F(TXT.c3, { d: 2 * k }), clave: "u" }, { html: TXT.c4, clave: "d" }],
    correcta: "a", pista: TXT.pistaComun, bien: F(TXT.bienComun, { k: k }), mal: F(TXT.bienComun, { k: k }) };
}

/* ============ Start ============ */
["rc-a", "rc-b"].forEach(function(id){ $(id).addEventListener("input", pintaRC); }); pintaRC();
creaPracticaOM("p1", genComparar);
$("or-comprobar").addEventListener("click", compruebaOR); $("or-nuevo").addEventListener("click", nuevoOR); nuevoOR();
$("va-n").addEventListener("input", pintaVA); pintaVA();
creaPracticaLibre("p2", genAbsoluto);
$("op-n").addEventListener("input", pintaOP); pintaOP();
creaPracticaOM("p3", genOpuesto);
'''

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val):
        return f'<div class="campo" style="flex:1;min-width:200px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    mods = [
     (t("number-line", "recta"), t("The full number line", "La recta numérica completa"),
      f'''      <p>{t("Zero is in the center of the number line: the positive numbers are to the right and the negative numbers are to the left. The numbers <strong>grow to the right</strong>: any number is greater than every number to its left. That is why −2 is greater than −5.",
"En la recta numérica, el cero está en el centro: los positivos a la derecha y los negativos a la izquierda. Los números <strong>crecen hacia la derecha</strong>: cualquier número es mayor que todos los que tiene a su izquierda. Por eso −2 es mayor que −5.")}</p>
      <h3>{t("Compare two integers", "Compare dos enteros")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("rc-a", t("Number A", "Número A"), -10, 10, -5)}
          {deslizador("rc-b", t("Number B", "Número B"), -10, 10, -2)}
        </div>
        <div id="rc-svg"></div>
        <div class="salida" id="rc-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip"><strong>{t("In real life:", "En la vida real:")}</strong> {t("a thermometer is a number line standing up. −10 °F is lower, and colder, than −3 °F.", "un termómetro es una recta numérica de pie. −10 °F está más abajo, y es más fría, que −3 °F.")}</div>
{B.om("p1", t("Practice: compare", "Practique: comparar"))}
      <h3>{t("Practice: order from least to greatest", "Practique: ordenar de menor a mayor")}</h3>
      <div class="panel">
        <p>{t("Use the arrows to move the numbers. The least goes first.", "Use las flechas para mover los números. El menor va primero.")}</p>
        <ol class="lista-orden" id="or-lista"></ol>
        <div class="fila-btn">
          <button type="button" class="btn" id="or-comprobar">{t("Check the order", "Comprobar el orden")}</button>
          <button type="button" class="btn-sec" id="or-nuevo">{t("Other numbers", "Otros números")}</button>
        </div>
        <div class="fb" id="or-fb" role="status"></div>
        <p class="marcador" id="or-marcador"></p>
      </div>'''),
     (t("absolute-value", "valor-absoluto"), t("Absolute value: the distance from zero", "El valor absoluto: la distancia al cero"),
      f'''      <p>{t("The <strong>absolute value</strong> of a number is its <strong>distance from zero</strong>. A distance is never negative, so the absolute value is always positive or zero. You write it between two bars: |−5| = 5 and |5| = 5.",
"El <strong>valor absoluto</strong> de un número es su <strong>distancia al cero</strong>. Una distancia nunca es negativa, así que el valor absoluto siempre es positivo o cero. Se escribe entre dos barras: |−5| = 5 y |5| = 5.")}</p>
      <h3>{t("Measure the distance", "Mida la distancia")}</h3>
      <div class="panel">
        <div class="campos">{deslizador("va-n", t("Number", "Número"), -10, 10, -7)}</div>
        <div id="va-svg"></div>
        <div class="salida" id="va-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("The absolute value measures distance.", "El valor absoluto mide distancia.")}</strong> {t("A minus sign outside the bars stays: in −|−6|, first |−6| = 6, and then the minus sign outside makes it −6.", "Un signo menos fuera de las barras se queda: en −|−6|, primero |−6| = 6, y después el signo de afuera lo vuelve −6.")}</div>
{B.libre_e("p2", t("Practice: absolute value", "Practique: valor absoluto"))}'''),
     (t("opposites", "opuestos"), t("Opposites", "Los opuestos"),
      f'''      <p>{t("Two numbers are <strong>opposites</strong> when they are the same distance from zero, on opposite sides. A number and its opposite always <strong>add up to zero</strong>, so the opposite is also called the additive inverse. Zero is its own opposite.",
"Dos números son <strong>opuestos</strong> cuando están a la misma distancia del cero, en lados contrarios. Un número y su opuesto siempre <strong>suman cero</strong>; por eso al opuesto también se le llama inverso aditivo. El cero es su propio opuesto.")}</p>
      <h3>{t("Zero is a mirror", "El cero es un espejo")}</h3>
      <div class="panel">
        <div class="campos">{deslizador("op-n", t("Number", "Número"), -10, 10, 6)}</div>
        <div id="op-svg"></div>
        <div class="salida" id="op-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip"><strong>{t("Two minus signs:", "Dos signos menos:")}</strong> {t("the minus sign in front of a number means \"the opposite of.\" So −(−8) is \"the opposite of −8,\" which is 8.", "el signo menos delante de un número quiere decir «el opuesto de». Así, −(−8) es «el opuesto de −8», que es 8.")}</div>
{B.om("p3", t("Practice: opposites", "Practique: opuestos"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 1, t(*TEMA), t("The number line, absolute value, and opposites", "La recta numérica, el valor absoluto y los opuestos"),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "La recta numérica, el valor absoluto y los opuestos")
