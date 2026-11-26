"""Level 3 · Lesson 2.1 · Scientific notation and orders of magnitude — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "2-1"
TEMA = ("Scientific notation", "Notación científica")
TIT = ("Scientific notation and orders of magnitude", "Conversión decimal ↔ científica y órdenes de magnitud")

def s(c, k):
    return f"{c} × 10<sup>{k}</sup>"

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("Topic 1 gave you the rules of exponents, including powers of 10 and negative exponents. Scientific notation is the most useful application of those rules: it uses powers of 10 (a positive exponent for large numbers and a negative one for small numbers) to write, in a short form, amounts as huge as the mass of the Sun or as tiny as the mass of an electron.",
"El Tema 1 dejó dominadas las reglas de los exponentes, incluidas las potencias de 10 y los exponentes negativos. La notación científica es la aplicación más útil de esas reglas: usa potencias de 10 (con exponente positivo para los números grandes y negativo para los pequeños) para escribir de forma compacta cantidades tan enormes como la masa del Sol o tan diminutas como la de un electrón.")}</p>
<p>{t("Scientific notation writes any number as the product of two parts: a <strong>coefficient</strong> and a <strong>power of 10</strong>.", "La notación científica expresa cualquier número como el producto de dos partes: un <strong>coeficiente</strong> y una <strong>potencia de 10</strong>.")}</p>
{big(t("a × 10<sup>n</sup>   with   1 ≤ a &lt; 10", "a × 10<sup>n</sup>   con   1 ≤ a &lt; 10"))}
<p>{t("The coefficient a is always at least 1 and less than 10: one digit, not zero, before the decimal point. The exponent n tells how many places the decimal point moved, and in which direction.", "El coeficiente a es siempre mayor o igual que 1 y menor que 10: un solo dígito, distinto de cero, antes del punto decimal. El exponente n indica cuántos lugares se movió el punto decimal y en qué dirección.")}</p>
{caja("tip", t("What it is for", "Para qué sirve"), t("<p>Writing 5,970,000,000,000,000,000,000,000 is easy to get wrong. In scientific notation it is 5.97 × 10<sup>24</sup> (the mass of the Earth in kilograms). Scientific notation makes numbers that would be impossible to read or compare easy to handle.</p>",
"<p>Escribir 5,970,000,000,000,000,000,000,000 se presta a errores. En notación científica es 5.97 × 10<sup>24</sup> (la masa de la Tierra en kilogramos). La notación científica hace manejables números que de otro modo serían imposibles de leer o comparar.</p>"))}'''

    s2 = f'''<p>{t("For a large number, move the decimal point <strong>to the left</strong> until only one digit (1 to 9) is left before the point. The number of places you moved it is the <strong>positive</strong> exponent of 10.", "Para un número grande, se mueve el punto decimal <strong>hacia la izquierda</strong> hasta que quede un solo dígito (de 1 a 9) antes del punto. La cantidad de lugares movidos es el exponente <strong>positivo</strong> de 10.")}</p>
{ejemplo(t("Example 1: write 4,500,000 in scientific notation", "Ejemplo 1: escriba 4,500,000 en notación científica"),
  [("1", t("Coefficient.", "Coeficiente."), t("Put the point after the first digit that is not zero: 4.5.", "Se coloca el punto después del primer dígito distinto de cero: 4.5.")),
   ("2", t("Count.", "Se cuenta."), t("The point moved 6 places to the left (from the end of 4500000).", "El punto se movió 6 lugares hacia la izquierda (desde el final de 4500000).")),
   ("3", t("Exponent.", "Exponente."), t("Large number: the exponent is +6.", "Número grande: el exponente es +6.")),
   ("✓", t("Answer.", "Respuesta."), f"4,500,000 = <strong>{s('4.5', 6)}</strong>")])}
{caja("ojo", t("The coefficient rules", "El coeficiente manda"), t(f"<p>{s(45, 5)} uses a power of 10, but it is not valid scientific notation, because 45 is not between 1 and 10. The right form is {s('4.5', 6)}.</p>", f"<p>{s(45, 5)} usa una potencia de 10, pero no es notación científica válida, porque 45 no está entre 1 y 10. La forma correcta es {s('4.5', 6)}.</p>"))}
{practica("p1", t("Practice 1 — A large number", "Práctica 1 — Un número grande"), t("What is 6,200 in scientific notation?", "¿Cómo se escribe 6,200 en notación científica?"),
          [("a", s("6.2", 3)), ("b", s("6.2", 2)), ("c", s(62, 2)), ("d", s("6.2", "−3"))])}
{practica("p2", t("Practice 2 — Count the places", "Práctica 2 — Cuente los lugares"), t("What is 410,000 in scientific notation?", "¿Cómo se escribe 410,000 en notación científica?"),
          [("a", s("4.1", 4)), ("b", s(41, 4)), ("c", s("4.1", 5)), ("d", s("4.1", 6))])}
{enlace(n, t("large", "grandes"), t("large numbers to scientific notation", "números grandes a notación científica"), t("Move the decimal point one place at a time and watch the exponent grow.", "Mueva el punto decimal un lugar cada vez y observe cómo crece el exponente."))}'''

    s3 = f'''<p>{t("For a small number (less than 1), move the decimal point <strong>to the right</strong> until it passes the first digit that is not zero. The number of places you moved it is the <strong>negative</strong> exponent of 10.", "Para un número pequeño (menor que 1), se mueve el punto decimal <strong>hacia la derecha</strong> hasta pasar el primer dígito distinto de cero. La cantidad de lugares movidos es el exponente <strong>negativo</strong> de 10.")}</p>
{ejemplo(t("Example 2: write 0.00032 in scientific notation", "Ejemplo 2: escriba 0.00032 en notación científica"),
  [("1", t("Coefficient.", "Coeficiente."), t("Move the point to the right until it passes the 3: 3.2.", "Se mueve el punto hacia la derecha hasta pasar el 3: 3.2.")),
   ("2", t("Count.", "Se cuenta."), t("4 places to the right.", "4 lugares hacia la derecha.")),
   ("3", t("Exponent.", "Exponente."), t("Small number: the exponent is negative, −4.", "Número pequeño: el exponente es negativo, −4.")),
   ("✓", t("Answer.", "Respuesta."), f"0.00032 = <strong>{s('3.2', '−4')}</strong>")])}
{caja("tip", t("The direction rule", "La regla de la dirección"), t("<p>A number 10 or larger → a positive exponent. A number less than 1 → a negative exponent. The sign of the exponent tells you right away whether the amount is huge or tiny.</p>", "<p>Número de 10 o más → exponente positivo. Número menor que 1 → exponente negativo. El signo del exponente dice de inmediato si la cantidad es enorme o diminuta.</p>"))}
{practica("p3", t("Practice 3 — A small number", "Práctica 3 — Un número pequeño"), t("What is 0.0072 in scientific notation?", "¿Cómo se escribe 0.0072 en notación científica?"),
          [("a", s("7.2", "−2")), ("b", s("7.2", "−3")), ("c", s("7.2", 3)), ("d", s(72, "−4"))])}
{enlace(n, t("small", "pequenos"), t("small numbers to scientific notation", "números pequeños a notación científica"), t("Move the point to the right past the zeros, and write large and small numbers yourself.", "Mueva el punto hacia la derecha pasando los ceros, y escriba usted números grandes y pequeños."))}'''

    s4 = f'''<p>{t("To go back, the exponent tells you which way the point moves and how many places. <strong>Positive</strong> exponent: the point moves to the right (the number grows). <strong>Negative</strong> exponent: the point moves to the left (the number gets smaller). Fill in with zeros as needed.", "El proceso inverso usa el exponente para decidir hacia dónde se mueve el punto y cuántos lugares. Exponente <strong>positivo</strong>: el punto va a la derecha (el número crece). Exponente <strong>negativo</strong>: el punto va a la izquierda (el número se achica). Se rellena con ceros según haga falta.")}</p>
{ejemplo(t(f"Example 3: write {s('3.7', 5)} as a decimal", f"Ejemplo 3: escriba {s('3.7', 5)} en notación decimal"),
  [("1", t("Direction.", "Dirección."), t("The exponent +5 says: move the point 5 places to the right.", "El exponente +5 indica mover el punto 5 lugares a la derecha.")),
   ("2", t("Fill in.", "Se rellena."), t("3.7 → 370000, adding the zeros you need.", "3.7 → 370000, agregando los ceros necesarios.")),
   ("✓", t("Answer.", "Respuesta."), f"{s('3.7', 5)} = <strong>370,000</strong>")])}
{ejemplo(t(f"Example 4: write {s('5.6', '−3')} as a decimal", f"Ejemplo 4: escriba {s('5.6', '−3')} en notación decimal"),
  [("1", t("Direction.", "Dirección."), t("The exponent −3 says: move the point 3 places to the left.", "El exponente −3 indica mover el punto 3 lugares a la izquierda.")),
   ("2", t("Fill in.", "Se rellena."), t("5.6 → 0.0056, adding zeros on the left.", "5.6 → 0.0056, agregando ceros a la izquierda.")),
   ("✓", t("Answer.", "Respuesta."), f"{s('5.6', '−3')} = <strong>0.0056</strong>")])}
{calc(t("Scientific notation on the calculator", "La notación científica en la calculadora"), t(f"<p>To type {s('3.7', 5)}, use the {T('×10<sup>n</sup>')} key: {T('3')} {T('.')} {T('7')} {T('×10<sup>n</sup>')} {T('5')} {T('enter')}. The screen shows 370000. For a negative exponent, use {T('(−)')}: {T('5')} {T('.')} {T('6')} {T('×10<sup>n</sup>')} {T('(−)')} {T('3')} {T('enter')} shows 0.0056.</p>",
f"<p>Para escribir {s('3.7', 5)}, use la tecla {T('×10<sup>n</sup>')}: {T('3')} {T('.')} {T('7')} {T('×10<sup>n</sup>')} {T('5')} {T('enter')}. La pantalla muestra 370000. Para un exponente negativo, use {T('(−)')}: {T('5')} {T('.')} {T('6')} {T('×10<sup>n</sup>')} {T('(−)')} {T('3')} {T('enter')} muestra 0.0056.</p>"))}
{practica("p4", t("Practice 4 — Back to a decimal", "Práctica 4 — De vuelta a decimal"), t(f"What is {s('4.8', 4)} as a decimal?", f"¿Cuánto es {s('4.8', 4)} en notación decimal?"),
          [("a", "480"), ("b", "48,000"), ("c", "4,800"), ("d", "480,000")])}
{practica("p5", t("Practice 5 — A negative exponent", "Práctica 5 — Un exponente negativo"), t(f"What is {s(3, '−3')} as a decimal?", f"¿Cuánto es {s(3, '−3')} en notación decimal?"),
          [("a", "0.03"), ("b", "300"), ("c", "0.003"), ("d", "−3,000")])}
{enlace(n, t("to-decimal", "a-decimal"), t("from scientific notation to a decimal", "de científica a decimal"), t("Choose the direction of the point yourself and fill in the zeros.", "Elija usted la dirección del punto y rellene con ceros."))}'''

    filas = [[t("Mass of the Sun", "Masa del Sol"), s("1.989", 30) + " kg", "10<sup>30</sup>"],
             [t("Distance from the Earth to the Sun", "Distancia de la Tierra al Sol"), s("1.496", 11) + " m", "10<sup>11</sup>"],
             [t("Mass of an electron", "Masa del electrón"), s("9.109", "−31") + " kg", "10<sup>−31</sup>"]]
    s5 = f'''<p>{t("The exponent of 10 is the <strong>order of magnitude</strong>: it tells the “size” of an amount. To compare two numbers in scientific notation, look at the <strong>exponent first</strong>. Only if the exponents are equal do you compare the coefficients.", "El exponente de 10 indica el <strong>orden de magnitud</strong>: el «tamaño» de una cantidad. Para comparar dos números en notación científica se mira <strong>primero el exponente</strong>; solo si los exponentes son iguales se comparan los coeficientes.")}</p>
{tabla(t("Real science data in scientific notation", "Datos científicos reales en notación científica"), t("Real science data in scientific notation: amount, scientific notation, and order of magnitude", "Datos científicos reales: cantidad, notación científica y orden de magnitud"),
       [t("Amount", "Cantidad"), t("Scientific notation", "Notación científica"), t("Order of magnitude", "Orden de magnitud")], filas)}
{ejemplo(t(f"Example 5: which is larger, {s(3, 8)} or {s(9, 7)}?", f"Ejemplo 5: ¿cuál es mayor, {s(3, 8)} o {s(9, 7)}?"),
  [("1", t("Exponents first.", "Primero los exponentes."), "8 > 7."),
   ("2", t("Decide.", "Se decide."), t("The number with the larger exponent is larger, whatever the coefficient.", "El número con el exponente mayor es mayor, sin importar el coeficiente.")),
   ("✓", t("Answer.", "Respuesta."), t(f"<strong>{s(3, 8)}</strong> is larger than {s(9, 7)}.", f"<strong>{s(3, 8)}</strong> es mayor que {s(9, 7)}."))])}
{caja("ojo", t("Do not be fooled by the coefficient", "No se deje engañar por el coeficiente"), t("<p>Even though 9 is larger than 3, the exponent 8 beats the 7. In scientific notation, the order of magnitude (the exponent) decides first. Each step up in the exponent multiplies the amount by 10.</p>", "<p>Aunque 9 sea mayor que 3, el exponente 8 supera al 7. En notación científica, el orden de magnitud (el exponente) decide primero. Cada unidad que sube el exponente multiplica la cantidad por 10.</p>"))}
{practica("p6", t("Practice 6 — Compare", "Práctica 6 — Compare"), t(f"Which amount is larger: {s(5, 6)} or {s(8, 5)}?", f"¿Cuál cantidad es mayor: {s(5, 6)} o {s(8, 5)}?"),
          [("a", s(5, 6)), ("b", s(8, 5)), ("c", t("They are equal", "Son iguales"))])}
{enlace(n, t("magnitude", "magnitud"), t("order of magnitude and comparing", "orden de magnitud y comparación"), t("Put real data from the universe in order and find how many times larger one amount is.", "Ordene datos reales del universo y averigüe cuántas veces mayor es una cantidad."))}'''

    secciones = [("s-" + t("what-is", "que-es"), t("What is scientific notation?", "¿Qué es la notación científica?"), s1),
                 ("s-" + t("large", "grandes"), t("From a decimal to scientific notation: large numbers", "De decimal a científica: números grandes"), s2),
                 ("s-" + t("small", "pequenos"), t("From a decimal to scientific notation: small numbers", "De decimal a científica: números pequeños"), s3),
                 ("s-" + t("to-decimal", "a-decimal"), t("From scientific notation to a decimal", "De científica a decimal"), s4),
                 ("s-" + t("magnitude", "magnitud"), t("Order of magnitude and comparing", "Orden de magnitud y comparación"), s5)]

    lesson = {"next": t("Lesson 2.2", "Lección 2.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Count again: from the end of 6200 to after the 6 there are 3 places.", "Cuente otra vez: desde el final de 6200 hasta después del 6 hay 3 lugares."), "c": t("62 is not between 1 and 10: it is not valid scientific notation.", "62 no está entre 1 y 10: no es notación científica válida."), "d": t("A large number has a positive exponent.", "Un número grande lleva exponente positivo.")},
             "right": t("The point moves 3 places to the left.", "El punto se mueve 3 lugares a la izquierda."), "solution": t(f"6,200 = 6.2 × 1,000 = {s('6.2', 3)}.", f"6,200 = 6.2 × 1,000 = {s('6.2', 3)}.")},
      "p2": {"ok": "c", "hints": {"a": t("Count the places again: there are 5.", "Cuente otra vez los lugares: son 5."), "b": t("41 is not between 1 and 10.", "41 no está entre 1 y 10."), "d": t("Count the places again: there is one too many.", "Cuente otra vez los lugares: sobra uno.")},
             "right": t("410000 → 4.10000: 5 places.", "410000 → 4.10000: 5 lugares."), "solution": t(f"The point moves 5 places to the left: {s('4.1', 5)}.", f"El punto se mueve 5 lugares a la izquierda: {s('4.1', 5)}.")},
      "p3": {"ok": "b", "hints": {"a": t("Count the places until you pass the 7: there are 3.", "Cuente los lugares hasta pasar el 7: son 3."), "c": t("A number less than 1 has a negative exponent.", "Un número menor que 1 lleva exponente negativo."), "d": t("72 is not between 1 and 10.", "72 no está entre 1 y 10.")},
             "right": t("0.0072 → 7.2: 3 places to the right.", "0.0072 → 7.2: 3 lugares a la derecha."), "solution": t(f"The point moves 3 places to the right, past the 7: {s('7.2', '−3')}.", f"El punto se mueve 3 lugares a la derecha, hasta pasar el 7: {s('7.2', '−3')}.")},
      "p4": {"ok": "b", "hints": {"a": t("That moves the point only 2 places. The exponent is 4.", "Así el punto se mueve solo 2 lugares. El exponente es 4."), "c": t("That moves the point 3 places. The exponent is 4.", "Así el punto se mueve 3 lugares. El exponente es 4."), "d": t("That moves the point 5 places. The exponent is 4.", "Así el punto se mueve 5 lugares. El exponente es 4.")},
             "right": t("4.8 → 48000: 4 places to the right.", "4.8 → 48000: 4 lugares a la derecha."), "solution": t("Move the point 4 places to the right: 48,000.", "Se mueve el punto 4 lugares a la derecha: 48,000.")},
      "p5": {"ok": "c", "hints": {"a": t("That moves the point only 2 places to the left.", "Así el punto se mueve solo 2 lugares a la izquierda."), "b": t("A negative exponent moves the point to the left: the number gets smaller.", "Un exponente negativo mueve el punto a la izquierda: el número se achica."), "d": t("A negative exponent does not make the number negative.", "Un exponente negativo no hace negativo al número.")},
             "right": t("3 → 0.003: 3 places to the left.", "3 → 0.003: 3 lugares a la izquierda."), "solution": t("Move the point 3 places to the left: 0.003.", "Se mueve el punto 3 lugares a la izquierda: 0.003.")},
      "p6": {"ok": "a", "hints": {"b": t("Look at the exponents first: 6 is larger than 5.", "Mire primero los exponentes: 6 es mayor que 5."), "c": t("5,000,000 and 800,000 are not equal.", "5,000,000 y 800,000 no son iguales.")},
             "right": t("The exponent 6 beats the 5.", "El exponente 6 supera al 5."), "solution": t(f"{s(5, 6)} = 5,000,000 and {s(8, 5)} = 800,000. The larger exponent decides.", f"{s(5, 6)} = 5,000,000 y {s(8, 5)} = 800,000. Decide el exponente mayor.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("Count the places again: there are 4.", "Cuente otra vez los lugares: son 4."), "b": t("52 is not between 1 and 10.", "52 no está entre 1 y 10."), "d": t("A large number has a positive exponent.", "Un número grande lleva exponente positivo.")}, "solution": t(f"52,000: the point moves 4 places to the left, {s('5.2', 4)}.", f"52,000: el punto se mueve 4 lugares a la izquierda, {s('5.2', 4)}.")},
      "B": {"ok": "a", "hints": {"b": t("Count again: there are 6 places.", "Cuente otra vez: son 6 lugares."), "c": t("83 is not between 1 and 10.", "83 no está entre 1 y 10."), "d": t("Count again: there is one too many.", "Cuente otra vez: sobra uno.")}, "solution": t(f"8,300,000: 6 places to the left, {s('8.3', 6)}.", f"8,300,000: 6 lugares a la izquierda, {s('8.3', 6)}.")},
      "C": {"ok": "d", "hints": {"a": t("A number less than 1 has a negative exponent.", "Un número menor que 1 lleva exponente negativo."), "b": t("Count until you pass the 6: there are 4 places.", "Cuente hasta pasar el 6: son 4 lugares."), "c": t("0.6 is not between 1 and 10.", "0.6 no está entre 1 y 10.")}, "solution": t(f"0.0006: 4 places to the right, {s(6, '−4')}.", f"0.0006: 4 lugares a la derecha, {s(6, '−4')}.")},
      "D": {"ok": "b", "hints": {"a": t("Count until you pass the 4: there are 4 places.", "Cuente hasta pasar el 4: son 4 lugares."), "c": t("45 is not between 1 and 10.", "45 no está entre 1 y 10."), "d": t("A number less than 1 has a negative exponent.", "Un número menor que 1 lleva exponente negativo.")}, "solution": t(f"0.00045: 4 places to the right, {s('4.5', '−4')}.", f"0.00045: 4 lugares a la derecha, {s('4.5', '−4')}.")},
      "E": {"ok": "a", "hints": {"b": t("That moves the point 4 places; the exponent is 5.", "Así el punto se mueve 4 lugares; el exponente es 5."), "c": t("That moves the point 6 places; the exponent is 5.", "Así el punto se mueve 6 lugares; el exponente es 5."), "d": t("A positive exponent moves the point to the right.", "Un exponente positivo mueve el punto a la derecha.")}, "solution": t("3.7 → 370000: 5 places to the right, 370,000.", "3.7 → 370000: 5 lugares a la derecha, 370,000.")},
      "F": {"ok": "c", "hints": {"a": t("That moves the point 2 places; the exponent is 3.", "Así el punto se mueve 2 lugares; el exponente es 3."), "b": t("That moves the point 4 places; the exponent is 3.", "Así el punto se mueve 4 lugares; el exponente es 3."), "d": t("A positive exponent moves the point to the right.", "Un exponente positivo mueve el punto a la derecha.")}, "solution": t("2.1 → 2100: 3 places to the right, 2,100.", "2.1 → 2100: 3 lugares a la derecha, 2,100.")},
      "G": {"ok": "b", "hints": {"a": t("That moves the point 4 places to the left; the exponent is −3.", "Así el punto se mueve 4 lugares a la izquierda; el exponente es −3."), "c": t("That moves the point only 2 places.", "Así el punto se mueve solo 2 lugares."), "d": t("A negative exponent moves the point to the left.", "Un exponente negativo mueve el punto a la izquierda.")}, "solution": t("9 → 0.009: 3 places to the left.", "9 → 0.009: 3 lugares a la izquierda.")},
      "H": {"ok": "a", "hints": {"b": t("Look at the exponents first: 8 is larger than 7.", "Mire primero los exponentes: 8 es mayor que 7."), "c": t("300,000,000 and 90,000,000 are not equal.", "300,000,000 y 90,000,000 no son iguales."), "d": t("You can always compare: look at the exponents first.", "Siempre se puede comparar: mire primero los exponentes.")}, "solution": t("The exponent 8 beats the 7, whatever the coefficient.", "El exponente 8 supera al 7, sin importar el coeficiente.")}
     }}

    quiz = [
     ("A", t("Write 52,000 in scientific notation.", "Escriba 52,000 en notación científica."), [("a", s("5.2", 3)), ("b", s(52, 3)), ("c", s("5.2", 4)), ("d", s("5.2", "−4"))]),
     ("B", t("Write 8,300,000 in scientific notation.", "Escriba 8,300,000 en notación científica."), [("a", s("8.3", 6)), ("b", s("8.3", 5)), ("c", s(83, 5)), ("d", s("8.3", 7))]),
     ("C", t("Write 0.0006 in scientific notation.", "Escriba 0.0006 en notación científica."), [("a", s(6, 4)), ("b", s(6, "−3")), ("c", s("0.6", "−3")), ("d", s(6, "−4"))]),
     ("D", t("Write 0.00045 in scientific notation.", "Escriba 0.00045 en notación científica."), [("a", s("4.5", "−3")), ("b", s("4.5", "−4")), ("c", s(45, "−5")), ("d", s("4.5", 4))]),
     ("E", t(f"Write {s('3.7', 5)} as a decimal.", f"Escriba {s('3.7', 5)} en notación decimal."), [("a", "370,000"), ("b", "37,000"), ("c", "3,700,000"), ("d", "0.000037")]),
     ("F", t(f"Write {s('2.1', 3)} as a decimal.", f"Escriba {s('2.1', 3)} en notación decimal."), [("a", "210"), ("b", "21,000"), ("c", "2,100"), ("d", "0.0021")]),
     ("G", t(f"Write {s(9, '−3')} as a decimal.", f"Escriba {s(9, '−3')} en notación decimal."), [("a", "0.0009"), ("b", "0.009"), ("c", "0.09"), ("d", "9,000")]),
     ("H", t(f"Which amount is larger: {s(3, 8)} or {s(9, 7)}?", f"¿Cuál cantidad es mayor: {s(3, 8)} o {s(9, 7)}?"), [("a", s(3, 8)), ("b", s(9, 7)), ("c", t("They are equal", "Son iguales")), ("d", t("You cannot tell", "No se puede saber"))])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("A short way to write huge and tiny numbers: a coefficient from 1 to 10 times a power of 10.", "Una manera corta de escribir números enormes y diminutos: un coeficiente entre 1 y 10 por una potencia de 10."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Tell</strong> what valid scientific notation is: a × 10<sup>n</sup> with 1 ≤ a &lt; 10.", "<strong>Reconocer</strong> la notación científica válida: a × 10<sup>n</sup> con 1 ≤ a &lt; 10."),
         t("<strong>Write</strong> large and small numbers in scientific notation.", "<strong>Escribir</strong> números grandes y pequeños en notación científica."),
         t("<strong>Write</strong> numbers in scientific notation as decimals.", "<strong>Escribir</strong> en notación decimal números dados en notación científica."),
         t("<strong>Compare and order</strong> amounts by their order of magnitude.", "<strong>Comparar y ordenar</strong> cantidades según su orden de magnitud.")],
        secciones,
        (t("Do four conversions from a decimal to scientific notation (two large numbers and two small ones), four from scientific notation to a decimal (two with a positive exponent and two with a negative one), and two exercises comparing and ordering amounts in scientific notation. Scientific notation is place value in different clothes: if moving the point and counting places comes easily, the conversion comes easily too.",
           "Haga cuatro conversiones de decimal a científica (dos números grandes y dos pequeños), cuatro de científica a decimal (dos con exponente positivo y dos con negativo) y dos ejercicios de comparar y ordenar cantidades en notación científica. La notación científica es valor posicional con otro traje: si mover el punto y contar lugares le sale sin pensar, la conversión sale sola."),
         t("Find two large numbers and two small ones in the news, on a food label, or on a medicine box (for example, a population, a budget, or a dose in grams). Write each one in scientific notation and say its order of magnitude.",
           "Busque dos números grandes y dos pequeños en las noticias, en una etiqueta de alimentos o en una caja de medicinas (por ejemplo, una población, un presupuesto o una dosis en gramos). Escriba cada uno en notación científica y diga su orden de magnitud.")),
        quiz,
        t("Self-check checklist for scientific notation and orders of magnitude", "Lista de autoevaluación de la notación científica y los órdenes de magnitud"),
        t("Self-check checklist: skills for scientific notation and orders of magnitude", "Lista de autoevaluación: destrezas de la notación científica y los órdenes de magnitud"),
        [(t("The coefficient (1 ≤ a &lt; 10)", "El coeficiente (1 ≤ a &lt; 10)"), t("My coefficient is always from 1 to 10, and I can fix one that is not.", "Mi coeficiente siempre queda entre 1 y 10, y sé corregir uno que no lo está."), t("I place the coefficient, with a few mistakes.", "Ubico el coeficiente, con algunos errores."), t("I leave coefficients like 45 × 10<sup>5</sup>.", "Dejo coeficientes como 45 × 10<sup>5</sup>.")),
         (t("The exponent of 10", "El exponente de 10"), t("I get the exponent and its sign right, and link it to how the point moves.", "Acierto el exponente y su signo, y lo relaciono con el movimiento del punto."), t("I get the number right, but sometimes the sign wrong.", "Acierto el número, pero a veces fallo el signo."), t("I mix up the sign or the number of places.", "Confundo el signo o la cantidad de lugares.")),
         (t("Comparing and ordering", "Comparar y ordenar"), t("I compare by the exponent first and can explain why.", "Comparo primero por el exponente y sé explicar por qué."), t("I compare, but I make mistakes when the exponents are different.", "Comparo, pero me equivoco cuando los exponentes son distintos."), t("I compare by the coefficient without looking at the exponent.", "Comparo por el coeficiente sin mirar el exponente."))],
        t("<p>You learned to move between decimals and scientific notation: the <strong>coefficient</strong> from 1 to 10 and the <strong>exponent</strong> of 10, positive for large numbers and negative for small ones. You also learned to compare amounts by their <strong>order of magnitude</strong>.</p>\n<p>In <strong>Lesson 2.2 · Multiplying and dividing in scientific notation</strong> you will use the product and quotient rules of Topic 1 with numbers in scientific notation, and learn to adjust the answer so it stays valid.</p>",
          "<p>Aprendió a pasar de decimal a notación científica y al revés: el <strong>coeficiente</strong> entre 1 y 10 y el <strong>exponente</strong> de 10, positivo para los números grandes y negativo para los pequeños. También aprendió a comparar cantidades por su <strong>orden de magnitud</strong>.</p>\n<p>En la <strong>Lección 2.2 · Multiplicación y división en notación científica</strong> usará las reglas del producto y del cociente del Tema 1 con números en notación científica, y aprenderá a ajustar el resultado para que siga siendo válido.</p>"),
        ("2-2", ("", t("Lesson 2.2 · Multiplying and dividing in scientific notation", "Lección 2.2 · Multiplicación y división en notación científica"))),
        [(t("scientific notation", "notación científica"), t("A number written as a × 10<sup>n</sup>, with a from 1 up to, but not including, 10.", "Un número escrito como a × 10<sup>n</sup>, con a mayor o igual que 1 y menor que 10.")),
         (t("coefficient", "coeficiente"), t("The first part, a. It has one digit, not zero, before the decimal point.", "La primera parte, a. Tiene un solo dígito, distinto de cero, antes del punto decimal.")),
         (t("order of magnitude", "orden de magnitud"), t("The exponent of 10. It tells the size of an amount.", "El exponente de 10. Indica el tamaño de una cantidad.")),
         (t("standard form (decimal)", "notación decimal"), t("The usual way of writing a number, like 370,000 or 0.0056.", "La forma habitual de escribir un número, como 370,000 o 0.0056."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ============ MODULES 1 and 2 · the point's trip (decimal → scientific) ============ */
function creaRecorrido(pre, primeros, genera, haciaIzq){
  var R = {n: null, D: "", p0: 0, p: 0, cola: primeros.slice()};
  function absN(n){ return normaliza({m: abs(n.m), e: n.e}); }
  function carga(n){
    R.n = n; var s = plano(n), i = s.indexOf(".");
    R.D = i < 0 ? s : s.slice(0, i) + s.slice(i + 1); R.p0 = i < 0 ? s.length : i; R.p = R.p0; pinta();
  }
  function pinta(){
    var s = R.p0 - R.p, html = "";
    for (var i = 0; i < R.D.length; i++){
      var salto = haciaIzq ? (i >= R.p && i < R.p0) : (i >= R.p0 && i < R.p);
      html += '<span class="celda' + (salto ? " saltado" : "") + '">' + (salto ? '<span class="marca">' + (haciaIzq ? (R.p0 - i) : (i - R.p0 + 1)) + "</span>" : "") + R.D.charAt(i) + "</span>";
      if (i === R.p - 1) html += '<span class="punto">.</span>';
    }
    $(pre + "-vis").innerHTML = html;
    var coef = porPot(R.n, -s), c = plano(coef), ok = esValida(c), l = Math.abs(s), dir = s > 0 ? T("to the left", "hacia la izquierda") : T("to the right", "hacia la derecha"), msg;
    if (s === 0) msg = T("The point is where it started. Move it until one digit, not zero, is left before the point.", "El punto está en su lugar de partida. Muévalo hasta que quede un solo dígito, distinto de cero, antes del punto.");
    else if (ok) msg = T("✓ Done: one digit before the point. You moved the point " + l + lugares(l) + " " + dir + ", so the exponent is " + (s > 0 ? "+" : "−") + l + ".", "✓ Listo: un solo dígito antes del punto. Movió el punto " + l + lugares(l) + " " + dir + ", así que el exponente es " + (s > 0 ? "+" : "−") + l + ".");
    else if (compara(absN(coef), N(10)) >= 0) msg = T("So far " + l + lugares(l) + ". The coefficient " + c + " is still 10 or more: keep moving the point.", "Lleva " + l + lugares(l) + ". El coeficiente " + c + " todavía es 10 o más: siga moviendo el punto.");
    else msg = T("So far " + l + lugares(l) + ". The coefficient " + c + " is less than 1: keep moving the point.", "Lleva " + l + lugares(l) + ". El coeficiente " + c + " es menor que 1: siga moviendo el punto.");
    $(pre + "-estado").innerHTML = '<span class="grande">' + conComas(R.n) + " = " + sciHTML(c, s) + "</span><br>" + msg;
    $(pre + "-izq").disabled = R.p <= 1 || (haciaIzq ? ok : R.p <= R.p0);
    $(pre + "-der").disabled = R.p >= R.D.length || (haciaIzq ? R.p >= R.p0 : ok);
  }
  $(pre + "-izq").addEventListener("click", function(){ if (R.p > 1){ R.p--; pinta(); } });
  $(pre + "-der").addEventListener("click", function(){ if (R.p < R.D.length){ R.p++; pinta(); } });
  $(pre + "-nuevo").addEventListener("click", function(){ carga(R.cola.length ? R.cola.shift() : genera()); });
  carga(R.cola.shift());
}
function grandeAzar(){ return sci(coefAzar(aleatorio(2, 3)), aleatorio(3, 9)); }
function pequenoAzar(){ return sci(coefAzar(aleatorio(1, 3)), -aleatorio(2, 7)); }
function escriba(n){ return T("Write ", "Escriba ") + conComas(n) + T(" in scientific notation.", " en notación científica."); }
function genGrandes(){
  var c = coefAzar(aleatorio(1, 3)), k = aleatorio(3, 9), n = sci(c, k), sin = leeNumero(c);
  var ops = [op(c, k), op(c, k - 1), op(c, k + 1), op(plano(porPot(sin, 1)), k - 1), op(c, -k)], q = {
    enun: escriba(n), opciones: [ops[0]].concat(baraja(ops.slice(1)).slice(0, 3)), correcta: ops[0].clave, porClave: {},
    bien: T("The point moves " + k + " places to the left and the coefficient " + c + " is from 1 to 10.", "El punto se mueve " + k + " lugares hacia la izquierda y el coeficiente " + c + " queda entre 1 y 10."),
    mal: T("The answer is ", "La respuesta es ") + sciHTML(c, k) + T(": the point moves " + k + " places to the left.", ": el punto se mueve " + k + " lugares hacia la izquierda.")};
  q.porClave[ops[3].clave] = T("That coefficient is not from 1 to 10, so it is not valid scientific notation.", "Ese coeficiente no está entre 1 y 10, así que no es notación científica válida.");
  q.porClave[ops[4].clave] = T("A large number has a positive exponent.", "Un número grande lleva exponente positivo.");
  q.porClave[ops[1].clave] = T("Count the places again: one is missing.", "Cuente de nuevo los lugares: falta uno.");
  q.porClave[ops[2].clave] = T("Count the places again: there is one too many.", "Cuente de nuevo los lugares: sobra uno.");
  return q;
}
function genPequenos(){
  var c = coefAzar(aleatorio(1, 3)), k = -aleatorio(2, 7), n = sci(c, k), sin = leeNumero(c);
  var ops = [op(c, k), op(c, k + 1), op(c, k - 1), op(c, -k), op(plano(porPot(sin, 1)), k - 1)], q = {
    enun: escriba(n), opciones: [ops[0]].concat(baraja(ops.slice(1)).slice(0, 3)), correcta: ops[0].clave, porClave: {},
    bien: T("The point moves " + (-k) + " places to the right, until it passes the first digit that is not zero.", "El punto se mueve " + (-k) + " lugares hacia la derecha, hasta pasar el primer dígito distinto de cero."),
    mal: T("The answer is ", "La respuesta es ") + sciHTML(c, k) + T(": the point moves " + (-k) + " places to the right.", ": el punto se mueve " + (-k) + " lugares hacia la derecha.")};
  q.porClave[ops[3].clave] = T("A number less than 1 has a negative exponent.", "Un número menor que 1 lleva exponente negativo.");
  q.porClave[ops[4].clave] = T("That coefficient is not from 1 to 10.", "Ese coeficiente no está entre 1 y 10.");
  q.porClave[ops[1].clave] = T("Count the places until you pass the first digit that is not zero: one is missing.", "Cuente los lugares hasta pasar el primer dígito distinto de cero: falta uno.");
  q.porClave[ops[2].clave] = T("Count the places until you pass the first digit that is not zero: there is one too many.", "Cuente los lugares hasta pasar el primer dígito distinto de cero: sobra uno.");
  return q;
}
function genMezcla(){
  var grande = Math.random() < 0.5, c = coefAzar(aleatorio(1, 3)), k = grande ? aleatorio(3, 9) : -aleatorio(2, 7), n = sci(c, k);
  return {enun: escriba(n), resp: n,
    explica: grande ? T("Large number: the point moves " + k + " places to the left and the exponent is positive.", "Número grande: el punto va " + k + " lugares a la izquierda y el exponente es positivo.")
                    : T("Small number: the point moves " + (-k) + " places to the right and the exponent is negative.", "Número pequeño: el punto va " + (-k) + " lugares a la derecha y el exponente es negativo."),
    diagnostico: function(v, cc, kk){ return (esValida(plano(cc)) && igual(cc, leeNumero(c)) && kk === -k) ? T("The coefficient is right, but the sign of the exponent is backward.", "El coeficiente está bien, pero el signo del exponente está al revés.") : null; }};
}

/* ============ MODULE 3 · from scientific notation to a decimal ============ */
var AD = {c: "", k: 0, celdas: [], pos: 1, pasos: 0, cola: [["3.7", 5], ["5.6", -3]]};
function cargaAD(pr){
  AD.c = pr[0]; AD.k = pr[1]; AD.pasos = 0; AD.pos = 1;
  AD.celdas = AD.c.replace(".", "").split("").map(function(d){ return {d: d, rel: false}; });
  $("ad-origen").innerHTML = '<span class="grande">' + sciHTML(AD.c, AD.k) + "</span>";
  $("ad-aviso").className = "caja-aviso"; $("ad-aviso").textContent = "";
  pintaAD();
}
function pintaAD(){
  var html = "";
  AD.celdas.forEach(function(x, i){ html += '<span class="celda' + (x.rel ? " relleno" : "") + '">' + x.d + "</span>"; if (i === AD.pos - 1 && AD.pos < AD.celdas.length) html += '<span class="punto">.</span>'; });
  $("ad-vis").innerHTML = html;
  var falta = Math.abs(AD.k) - AD.pasos, actual = porPot(leeNumero(AD.c), AD.k > 0 ? AD.pasos : -AD.pasos), rel = AD.celdas.filter(function(x){ return x.rel; }).length, msg, ak = Math.abs(AD.k);
  if (falta === 0) msg = '<span class="grande">✓ ' + sciHTML(AD.c, AD.k) + " = " + conComas(actual) + "</span><br>" +
    T("The point moved " + ak + lugares(ak) + (AD.k > 0 ? " to the right" : " to the left") + (rel ? " and " + rel + (rel === 1 ? " zero was" : " zeros were") + " filled in." : "."),
      "El punto se movió " + ak + lugares(ak) + (AD.k > 0 ? " a la derecha" : " a la izquierda") + (rel ? " y se agregaron " + rel + (rel === 1 ? " cero" : " ceros") + " de relleno." : "."));
  else msg = T("Number now: ", "Número actual: ") + "<strong>" + conComas(actual) + "</strong>. " + (AD.pasos === 0 ? T("Which way does the point go? Look at the sign of the exponent.", "¿Hacia dónde va el punto? Mire el signo del exponente.") : (falta === 1 ? T("1 place to go.", "Falta 1 lugar.") : T(falta + " places to go.", "Faltan " + falta + " lugares.")));
  $("ad-estado").innerHTML = msg;
  $("ad-izq").disabled = falta === 0; $("ad-der").disabled = falta === 0;
}
function mueveAD(der){
  if (AD.pasos >= Math.abs(AD.k)) return;
  if (der !== (AD.k > 0)){
    $("ad-aviso").className = "caja-aviso visible";
    $("ad-aviso").textContent = AD.k > 0 ? T("The exponent is positive: the number must grow, so the point goes to the right.", "El exponente es positivo: el número tiene que crecer, así que el punto va a la derecha.")
                                         : T("The exponent is negative: the number must get smaller, so the point goes to the left.", "El exponente es negativo: el número tiene que achicarse, así que el punto va a la izquierda.");
    return;
  }
  $("ad-aviso").className = "caja-aviso"; $("ad-aviso").textContent = "";
  if (der){ AD.pos++; if (AD.pos > AD.celdas.length) AD.celdas.push({d: "0", rel: true}); }
  else { AD.pos--; if (AD.pos < 1){ AD.celdas.unshift({d: "0", rel: true}); AD.pos = 1; } }
  AD.pasos++; pintaAD();
}
function azarAD(){ return [coefAzar(aleatorio(1, 3)), Math.random() < 0.5 ? aleatorio(2, 7) : -aleatorio(1, 5)]; }
function genDecimal(){
  var c = coefAzar(aleatorio(1, 3)), k = Math.random() < 0.5 ? aleatorio(2, 7) : -aleatorio(1, 5), resp = sci(c, k), ak = Math.abs(k);
  return {enun: T("Write ", "Escriba ") + sciHTML(c, k) + T(" as a decimal.", " en notación decimal."), resp: resp,
    explica: sciHTML(c, k) + " = <strong>" + conComas(resp) + "</strong>. " + T("The exponent " + expTexto(k) + " says: move the point " + ak + lugares(ak) + (k > 0 ? " to the right." : " to the left."), "El exponente " + expTexto(k) + " indica mover el punto " + ak + lugares(ak) + (k > 0 ? " a la derecha." : " a la izquierda.")),
    pista: function(v){
      if (igual(v, sci(c, -k))) return T("You moved the point the wrong way.", "Movió el punto hacia el lado contrario.");
      if (igual(v, sci(c, k + 1)) || igual(v, sci(c, k - 1))) return T("Check how many places: there is one too many or one too few.", "Revise cuántos lugares: le sobra o le falta uno.");
      return null; }};
}

/* ============ MODULE 4 · ordering real magnitudes ============ */
var CONJUNTOS = [
  {unidad: T("All the lengths are in meters (m).", "Todas las longitudes están en metros (m)."), u: "m", datos: [
    [T("The width of a hydrogen atom (approx.)", "El diámetro de un átomo de hidrógeno (aprox.)"), "1.06", -10], [T("A flu virus (approx.)", "Un virus de la gripe (aprox.)"), "1.2", -7],
    [T("A red blood cell (approx.)", "Un glóbulo rojo (aprox.)"), "8", -6], [T("A grain of fine sand (approx.)", "Un grano de arena fina (aprox.)"), "2", -4],
    [T("The height of an adult (approx.)", "La estatura de una persona adulta (aprox.)"), "1.7", 0], [T("The height of Mount Everest", "La altura del monte Everest"), "8.849", 3],
    [T("The width of the Earth", "El diámetro de la Tierra"), "1.2742", 7], [T("The distance from the Earth to the Moon", "La distancia de la Tierra a la Luna"), "3.844", 8],
    [T("The distance from the Earth to the Sun", "La distancia de la Tierra al Sol"), "1.496", 11]]},
  {unidad: T("All the masses are in kilograms (kg).", "Todas las masas están en kilogramos (kg)."), u: "kg", datos: [
    [T("An electron", "Un electrón"), "9.109", -31], [T("A proton", "Un protón"), "1.673", -27], [T("A grain of rice (approx.)", "Un grano de arroz (aprox.)"), "2.5", -5],
    [T("An adult (approx.)", "Una persona adulta (aprox.)"), "7", 1], [T("An African elephant (approx.)", "Un elefante africano (aprox.)"), "6", 3],
    [T("The Moon", "La Luna"), "7.35", 22], [T("The Earth", "La Tierra"), "5.97", 24], [T("The Sun", "El Sol"), "1.989", 30]]}];
var OR = {lista: [], u: ""};
function valorDe(d){ return sci(d[1], d[2]); }
function estaOrdenado(l){ for (var i = 1; i < l.length; i++) if (compara(valorDe(l[i - 1]), valorDe(l[i])) > 0) return false; return true; }
function nuevoOrden(){
  var cj = elige(CONJUNTOS), sel;
  do { sel = baraja(cj.datos).slice(0, 4); } while (estaOrdenado(sel));
  OR.lista = sel; OR.u = cj.u; $("or-unidad").textContent = cj.unidad;
  $("or-fb").className = "fb"; $("or-fb").textContent = ""; pintaOrden();
}
function pintaOrden(foco){
  var ol = $("or-lista"); ol.innerHTML = "";
  OR.lista.forEach(function(d, i){
    var li = document.createElement("li");
    li.innerHTML = '<span class="nombre">' + d[0] + "</span><span>" + sciHTML(d[1], d[2]) + " " + OR.u + '</span><span class="flechas"><button type="button" data-i="' + i + '" data-d="-1" aria-label="' + T("Move up: ", "Subir: ") + d[0] + '">↑</button><button type="button" data-i="' + i + '" data-d="1" aria-label="' + T("Move down: ", "Bajar: ") + d[0] + '">↓</button></span>';
    ol.appendChild(li);
  });
  ol.querySelectorAll("button").forEach(function(b){
    var i = +b.getAttribute("data-i"), d = +b.getAttribute("data-d");
    b.disabled = (d < 0 && i === 0) || (d > 0 && i === OR.lista.length - 1);
    b.addEventListener("click", function(){ var j = i + d; if (j < 0 || j >= OR.lista.length) return; var x = OR.lista[i]; OR.lista[i] = OR.lista[j]; OR.lista[j] = x; $("or-fb").className = "fb"; $("or-fb").textContent = ""; pintaOrden({i: j, d: d}); });
  });
  if (foco){ var b = ol.querySelector('button[data-i="' + foco.i + '"][data-d="' + foco.d + '"]'); if (!b || b.disabled) b = ol.querySelector('button[data-i="' + foco.i + '"]:not([disabled])'); if (b) b.focus(); }
}
function compruebaOrden(){
  var ok = true, bien = OR.lista.slice().sort(function(a, b){ return compara(valorDe(a), valorDe(b)); });
  Array.prototype.forEach.call($("or-lista").children, function(li, i){ var x = OR.lista[i] === bien[i]; if (!x) ok = false; li.className = x ? "bien" : "mal"; });
  $("or-fb").className = "fb " + (ok ? "bien" : "pista");
  $("or-fb").innerHTML = ok ? T("✓ The order is right. Notice that the exponents go up: the exponent decides first.", "✓ Orden correcto. Fíjese en que los exponentes van creciendo: el exponente decide primero.")
                            : T("The places in red are not in order. Compare the exponents first (remember that −7 is less than −4); only if two exponents are equal, look at the coefficient.", "Las posiciones en rojo no están en su lugar. Compare primero los exponentes (recuerde que −7 es menor que −4); solo si dos exponentes son iguales, mire el coeficiente.");
}
function vecesHTML(d){ var n = conComas(sci("1", d)); return '<span aria-hidden="true">' + n + T(" times (10<sup>", " veces (10<sup>") + d + '</sup>)</span><span class="sr-only">' + n + T(" times, 10 to the power of ", " veces, 10 elevado a ") + d + "</span>"; }
function genComparar(){
  var t = aleatorio(1, 4);
  if (t <= 2){
    var a1, a2, k1, k2, iguales = false;
    if (t === 1){ k1 = aleatorio(-8, 9); k2 = k1 + aleatorio(1, 3); a1 = String(aleatorio(6, 9)); a2 = Math.random() < 0.3 ? coefAzar(2) : String(aleatorio(1, 5)); }
    else if (Math.random() < 0.5){ k1 = k2 = aleatorio(-6, 9); a1 = coefAzar(2); a2 = coefAzar(2); while (a1 === a2) a2 = coefAzar(2); }
    else { k2 = aleatorio(-5, 8); a2 = coefAzar(2); a1 = plano(porPot(leeNumero(a2), 1)); k1 = k2 - 1; iguales = true; }
    var A = sci(a1, k1), Bn = sci(a2, k2), orden = compara(A, Bn);
    if (Math.random() < 0.5){ var ta = a1, tk = k1; a1 = a2; k1 = k2; a2 = ta; k2 = tk; orden = -orden; }
    var q = {enun: T("Which amount is larger: ", "¿Cuál cantidad es mayor: ") + sciHTML(a1, k1) + T(" or ", " o ") + sciHTML(a2, k2) + "?",
      opciones: [{html: sciHTML(a1, k1), clave: "A"}, {html: sciHTML(a2, k2), clave: "B"}, {html: T("They are equal", "Son iguales"), clave: "="}], enOrden: true,
      correcta: orden > 0 ? "A" : (orden < 0 ? "B" : "="), porClave: {}};
    if (iguales){ q.bien = T("Both are the same amount: ", "Las dos valen lo mismo: ") + sciHTML(a1, k1) + " = " + numSciHTML(A) + T(". Only one of them is valid scientific notation.", ". Solo una de ellas está en notación científica válida."); q.mal = T("They are equal: ", "Son iguales: ") + sciHTML(a1, k1) + T(" can be rewritten as ", " se reescribe como ") + numSciHTML(A) + "."; q.pista = T("Rewrite the one whose coefficient is not from 1 to 10, then compare.", "Reescriba la que tiene el coeficiente fuera de 1 a 10 y después compare."); }
    else if (k1 !== k2){ q.bien = T("The larger exponent decides, whatever the coefficient.", "El exponente mayor decide, sin importar el coeficiente."); q.mal = T("Look at the exponents first: ", "Mire primero los exponentes: ") + expTexto(Math.max(k1, k2)) + T(" is larger than ", " es mayor que ") + expTexto(Math.min(k1, k2)) + "."; q.pista = T("Look at the exponents first, not the coefficients.", "Mire primero los exponentes, no los coeficientes."); }
    else { q.bien = T("With the same exponent, the larger coefficient decides.", "Con el mismo exponente, decide el coeficiente mayor."); q.mal = T("The exponents are equal, so the larger coefficient decides.", "Los exponentes son iguales, así que decide el coeficiente mayor."); q.pista = T("The exponents are equal: compare the coefficients.", "Los exponentes son iguales: compare los coeficientes."); }
    return q;
  }
  var c = coefAzar(aleatorio(1, 2)), kb = aleatorio(-6, 6), d = aleatorio(1, 6), ka = kb + d;
  var q2 = {enun: T("How many times larger is ", "¿Cuántas veces mayor es ") + sciHTML(c, ka) + T(" than ", " que ") + sciHTML(c, kb) + "?",
    opciones: [{html: vecesHTML(d), clave: "p" + d}, {html: d + (d === 1 ? T(" time", " vez") : T(" times", " veces")), clave: "n" + d}, {html: vecesHTML(d + 1), clave: "p" + (d + 1)}, {html: vecesHTML(d > 1 ? d - 1 : d + 2), clave: "p" + (d > 1 ? d - 1 : d + 2)}],
    correcta: "p" + d, porClave: {}, pista: T("Subtract the exponents: each step is a factor of 10.", "Reste los exponentes: cada unidad es un factor de 10."),
    bien: T("The difference of the exponents is ", "La diferencia de exponentes es ") + expTexto(ka) + " − " + par(kb) + " = " + d + T(", and 10<sup>", ", y 10<sup>") + d + "</sup> = " + conComas(sci("1", d)) + ".",
    mal: T("Subtract the exponents: ", "Reste los exponentes: ") + expTexto(ka) + " − " + par(kb) + " = " + d + T(". Each step is a factor of 10, so it is " + conComas(sci("1", d)) + " times larger.", ". Cada unidad es un factor de 10, así que es " + conComas(sci("1", d)) + " veces mayor.")};
  q2.porClave["n" + d] = T("The difference of the exponents is not the number of times: each step multiplies by 10.", "La diferencia de exponentes no es el número de veces: cada unidad multiplica por 10.");
  return q2;
}

/* ============ Start ============ */
creaRecorrido("rg", [sci("4.5", 6)], grandeAzar, true);
creaRecorrido("rp", [sci("3.2", -4)], pequenoAzar, false);
OMS("p1", genGrandes);
OMS("p2", genPequenos);
creaPracticaSci("p3", genMezcla);
$("ad-izq").addEventListener("click", function(){ mueveAD(false); });
$("ad-der").addEventListener("click", function(){ mueveAD(true); });
$("ad-nuevo").addEventListener("click", function(){ cargaAD(AD.cola.length ? AD.cola.shift() : azarAD()); });
cargaAD(AD.cola.shift());
creaPracticaDec("p4", genDecimal);
$("or-comprobar").addEventListener("click", compruebaOrden);
$("or-nuevo").addEventListener("click", nuevoOrden);
nuevoOrden();
OMS("p5", genComparar);
'''

def recorrido(pre, izq, der, leyenda):
    return f'''      <div class="panel">
        <div class="recorrido" id="{pre}-vis" aria-hidden="true"></div>
        <div class="leyenda" aria-hidden="true"><span class="l-salto">{leyenda}</span></div>
        <div class="estado" id="{pre}-estado" aria-live="polite"></div>
        <div class="fila-btn" style="justify-content:center;">
          <button type="button" class="{izq[1]}" id="{pre}-izq">{izq[0]}</button>
          <button type="button" class="{der[1]}" id="{pre}-der">{der[0]}</button>
          <button type="button" class="btn-sec" id="{pre}-nuevo">{t("Another number", "Otro número")}</button>
        </div>
      </div>'''

def practica_pagina():
    n = N
    P = n3
    salto = t("a place the point has already jumped", "lugar que ya saltó el punto")
    mods = [
     (t("large", "grandes"), t("From a decimal to scientific notation: large numbers", "De decimal a científica: números grandes"),
      f'''      <p>{t("A number in scientific notation has two parts: a <strong>coefficient</strong> that is at least 1 and less than 10, and a <strong>power of 10</strong>.", "Un número en notación científica tiene dos partes: un <strong>coeficiente</strong> mayor o igual que 1 y menor que 10, y una <strong>potencia de 10</strong>.")}</p>
{P.formula(t("a × 10<sup>n</sup>   with   1 ≤ a &lt; 10", "a × 10<sup>n</sup>   con   1 ≤ a &lt; 10"))}
      <p>{t("For a large number, the decimal point moves <strong>to the left</strong> until one digit, not zero, is left before the point. The places it moved are the exponent, and it is <strong>positive</strong>.", "Para un número grande, el punto decimal se mueve <strong>hacia la izquierda</strong> hasta que quede un solo dígito, distinto de cero, antes del punto. Los lugares que se movió son el exponente, y es <strong>positivo</strong>.")}</p>
      <h3>{t("The point's trip", "El recorrido del punto")}</h3>
      <p>{t("Move the point one place at a time and watch the coefficient and the exponent change. The value never changes: what the coefficient loses, the power of 10 gains.", "Mueva el punto un lugar cada vez y observe cómo cambian el coeficiente y el exponente. El valor del número nunca cambia: lo que pierde el coeficiente lo gana la potencia de 10.")}</p>
{recorrido("rg", (t("← Move the point to the left", "← Mover el punto a la izquierda"), "btn"), (t("Undo one place →", "Deshacer un lugar →"), "btn-sec"), salto)}
{P.atencion(t("The coefficient rules:", "El coeficiente manda:"), t("45 × 10<sup>5</sup> has the same value as 4,500,000, but it is not valid scientific notation, because 45 is not between 1 and 10. The right form is 4.5 × 10<sup>6</sup>.", "45 × 10<sup>5</sup> vale lo mismo que 4,500,000, pero no es notación científica válida, porque 45 no está entre 1 y 10. La forma correcta es 4.5 × 10<sup>6</sup>."))}
{B.om("p1", t("Practice: which is the right scientific notation?", "Practique: ¿cuál es la notación científica correcta?"))}'''),
     (t("small", "pequenos"), t("From a decimal to scientific notation: small numbers", "De decimal a científica: números pequeños"),
      f'''      <p>{t("For a number less than 1, the point moves <strong>to the right</strong> until it passes the first digit that is not zero. The places it moved are the exponent, and now it is <strong>negative</strong>.", "Para un número menor que 1, el punto se mueve <strong>hacia la derecha</strong> hasta pasar el primer dígito distinto de cero. Los lugares que se movió son el exponente, y ahora es <strong>negativo</strong>.")}</p>
      <h3>{t("The point's trip to the right", "El recorrido del punto hacia la derecha")}</h3>
      <p>{t("The zeros the point leaves behind are exactly the ones the negative exponent “keeps.”", "Los ceros que el punto va dejando atrás son justamente los que el exponente negativo «guarda».")}</p>
{recorrido("rp", (t("← Undo one place", "← Deshacer un lugar"), "btn-sec"), (t("Move the point to the right →", "Mover el punto a la derecha →"), "btn"), salto)}
      <div class="caja-tip"><strong>{t("The direction rule:", "Regla de la dirección:")}</strong> {t("a number 10 or larger → positive exponent; a number less than 1 → negative exponent. The sign of the exponent tells you right away whether the amount is huge or tiny.", "número de 10 o más → exponente positivo; número menor que 1 → exponente negativo. El signo del exponente dice de inmediato si la cantidad es enorme o diminuta.")}</div>
{B.om("p2", t("Practice: small numbers", "Practique: números pequeños"))}
{n3.sci_input("p3", t("Write it yourself: large and small numbers mixed", "Escríbalo usted: números grandes y pequeños mezclados"))}'''),
     (t("to-decimal", "a-decimal"), t("From scientific notation to a decimal", "De científica a decimal"),
      f'''      <p>{t("Going back uses the exponent to decide which way the point moves and how many places:", "El proceso inverso usa el exponente para decidir hacia dónde se mueve el punto y cuántos lugares:")}</p>
      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("Direction of the point (table you can scroll sideways)", "Dirección del punto (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("Which way the point moves, by the sign of the exponent", "Dirección del punto según el signo del exponente")}</caption>
      <thead><tr><th scope="col">{t("Exponent", "Exponente")}</th><th scope="col">{t("The point moves", "El punto se mueve")}</th><th scope="col">{t("The number", "El número")}</th></tr></thead>
      <tbody><tr><td>{t("Positive", "Positivo")}</td><td>{t("to the right", "a la derecha")}</td><td>{t("grows", "crece")}</td></tr><tr><td>{t("Negative", "Negativo")}</td><td>{t("to the left", "a la izquierda")}</td><td>{t("gets smaller", "se achica")}</td></tr></tbody></table></div>
      <p>{t("When you run out of digits, fill in with zeros.", "Cuando se acaban los dígitos, se rellena con ceros.")}</p>
      <h3>{t("Unpack the power of 10", "Desempaquetar la potencia de 10")}</h3>
      <p>{t("You choose the direction. If you choose the wrong way, you get a warning before the point moves.", "Decida usted la dirección. Si elige mal, se le avisa antes de mover el punto.")}</p>
      <div class="panel">
        <div class="estado" id="ad-origen"></div>
        <div class="recorrido" id="ad-vis" aria-hidden="true"></div>
        <div class="leyenda" aria-hidden="true"><span class="l-relleno">{t("a zero filled in", "cero de relleno")}</span></div>
        <div class="caja-aviso" id="ad-aviso" role="alert"></div>
        <div class="estado" id="ad-estado" aria-live="polite"></div>
        <div class="fila-btn" style="justify-content:center;">
          <button type="button" class="btn" id="ad-izq">{t("← Move to the left", "← Mover a la izquierda")}</button>
          <button type="button" class="btn" id="ad-der">{t("Move to the right →", "Mover a la derecha →")}</button>
          <button type="button" class="btn-sec" id="ad-nuevo">{t("Another number", "Otro número")}</button>
        </div>
      </div>
{B.libre("p4", t("Practice: write the number as a decimal", "Practique: escriba el número en notación decimal"), t("Number as a decimal", "Número en notación decimal"), nota=False)}
      <p class="nota">{t("Thousands commas are optional: 370000 and 370,000 are both accepted.", "Las comas de los miles son opcionales: 370000 y 370,000 se aceptan igual.")}</p>'''),
     (t("magnitude", "magnitud"), t("Order of magnitude and comparing", "Orden de magnitud y comparación"),
      f'''      <p>{t("The exponent of 10 is the <strong>order of magnitude</strong>: it tells the “size” of an amount. To compare two numbers in scientific notation, look at the <strong>exponent first</strong>; only if the exponents are equal do you compare the coefficients.", "El exponente de 10 es el <strong>orden de magnitud</strong>: dice de qué «tamaño» es una cantidad. Para comparar dos números en notación científica se mira <strong>primero el exponente</strong>; solo si los exponentes son iguales se comparan los coeficientes.")}</p>
      <h3>{t("Put them in order from least to greatest", "Ordene de menor a mayor")}</h3>
      <p>{t("These are real data from the universe, all in the same unit. Use the ↑ and ↓ buttons to put them in order, then check.", "Son datos reales del universo, todos en la misma unidad. Use los botones ↑ y ↓ para ordenarlos y después compruebe.")}</p>
      <div class="panel">
        <p class="nota" id="or-unidad"></p>
        <ol class="lista-orden" id="or-lista" aria-describedby="or-unidad"></ol>
        <div class="fila-btn">
          <button type="button" class="btn" id="or-comprobar">{t("Check the order", "Comprobar el orden")}</button>
          <button type="button" class="btn-sec" id="or-nuevo">{t("Another set", "Otro conjunto")}</button>
        </div>
        <div class="fb" id="or-fb" role="status"></div>
      </div>
{P.atencion(t("Do not be fooled by the coefficient:", "No se deje engañar por el coeficiente:"), t("9 × 10<sup>7</sup> is less than 3 × 10<sup>8</sup>, even though 9 is larger than 3. The exponent 8 beats the 7, and that decides.", "9 × 10<sup>7</sup> es menor que 3 × 10<sup>8</sup>, aunque 9 sea mayor que 3. El exponente 8 supera al 7, y eso decide."))}
      <h3>{t("How many times larger?", "¿Cuántas veces mayor?")}</h3>
      <p>{t("Each step up in the exponent multiplies the amount by 10. If two numbers have the same coefficient, the difference of the exponents tells how many times one fits in the other: 10<sup>8</sup> is 10<sup>8 − 5</sup> = 10<sup>3</sup> = 1,000 times 10<sup>5</sup>.", "Cada unidad que sube el exponente multiplica la cantidad por 10. Si dos números tienen el mismo coeficiente, la diferencia de exponentes dice cuántas veces cabe uno en el otro: 10<sup>8</sup> es 10<sup>8 − 5</sup> = 10<sup>3</sup> = 1,000 veces 10<sup>5</sup>.")}</p>
{B.om("p5", t("Practice: compare and measure the distance between magnitudes", "Practique: comparar y medir la distancia entre magnitudes"))}''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_SCI, scripts=("/math/scinot.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Conversión decimal ↔ científica y órdenes de magnitud")
