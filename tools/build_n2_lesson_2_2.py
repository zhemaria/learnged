"""Level 2 · Lesson 2.2 · Positive integer exponents and powers of 10 — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import m, p, pot

B.NIVEL = 2
N = "2-2"
TEMA = ("Fractions, exponents, and roots", "Fracciones, exponentes y raíces")
TIT = ("Positive integer exponents and powers of 10", "Exponentes enteros positivos y potencias de base 10")

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 2.1 you finished your work with signed fractions. This lesson brings a new way of writing math: <strong>powers</strong>. A power is a short way to write a multiplication in which the same number repeats.",
"En la Lección 2.1 terminó el trabajo con las fracciones con signo. Esta lección trae una nueva forma de escribir matemáticas: las <strong>potencias</strong>. Una potencia es una manera corta de escribir una multiplicación en la que se repite el mismo número.")}</p>
<p style="text-align:center;font-size:1.3em"><strong>{pot(5, 3)} = 5 × 5 × 5 = 125</strong></p>
<ul>
<li>{t("The big number, <strong>5</strong>, is the <strong>base</strong>: the number that repeats.", "El número grande, <strong>5</strong>, es la <strong>base</strong>: el número que se repite.")}</li>
<li>{t("The small raised number, <strong>3</strong>, is the <strong>exponent</strong>: it tells how many times the base is a factor.", "El número pequeño y elevado, <strong>3</strong>, es el <strong>exponente</strong>: dice cuántas veces la base es factor.")}</li>
<li>{t("The answer, <strong>125</strong>, is the value of the power.", "El resultado, <strong>125</strong>, es el valor de la potencia.")}</li>
</ul>
<p>{t(f"You read {pot(5, 3)} as \"five to the third power\" or \"five cubed,\" and {pot(7, 2)} as \"seven to the second power\" or \"seven squared.\"", f"{pot(5, 3)} se lee «cinco elevado a la tercera» o «cinco al cubo», y {pot(7, 2)}, «siete elevado a la segunda» o «siete al cuadrado».")}</p>
{caja("ojo", t("The most common mistake", "El error más común"), t(f"<p>The exponent does not multiply the base. {pot(5, 3)} is <strong>not</strong> 5 × 3 = 15; it is 5 × 5 × 5 = 125. The exponent counts the factors; it is not one more factor.</p>",
f"<p>El exponente no multiplica a la base. {pot(5, 3)} <strong>no</strong> es 5 × 3 = 15; es 5 × 5 × 5 = 125. El exponente cuenta los factores; no es un factor más.</p>"))}
{ejemplo(t(f"Example: evaluate {pot(2, 5)}", f"Ejemplo: evalúe {pot(2, 5)}"),
  [("1", t("Step 1.", "Paso 1."), t("The base is 2 and the exponent is 5: multiply 2 five times.", "La base es 2 y el exponente es 5: se multiplica el 2 cinco veces.")),
   ("2", t("Step 2.", "Paso 2."), "2 × 2 = 4; 4 × 2 = 8; 8 × 2 = 16; 16 × 2 = 32."),
   ("✓", t("Result.", "Resultado."), f"{pot(2, 5)} = <strong>32</strong>")])}
{practica("p1", t("Practice 1 — Base and exponent", "Práctica 1 — Base y exponente"), t(f"What is {pot(4, 3)}?", f"¿Cuánto es {pot(4, 3)}?"),
          [("a", "12"), ("b", "64"), ("c", "7"), ("d", "16")])}
{enlace(n, t("base-exponent", "base-exponente"), t("base and exponent", "base y exponente"), t("Build powers by choosing the base and the exponent, and see the repeated multiplication.", "Construya potencias eligiendo la base y el exponente, y vea la multiplicación repetida."))}'''

    s2 = f'''<h3>{t("The exponent 1", "El exponente 1")}</h3>
<p>{t(f"Any number to the first power is the number itself: the factor appears only once. So {pot(9, 1)} = 9 and {pot(47, 1)} = 47.", f"Cualquier número elevado a la primera es el mismo número: el factor aparece una sola vez. Así, {pot(9, 1)} = 9 y {pot(47, 1)} = 47.")}</p>
<h3>{t("The exponent 0", "El exponente 0")}</h3>
<p>{t(f"Any number other than zero to the power 0 is <strong>1</strong>. So {pot(8, 0)} = 1 and {pot(250, 0)} = 1.", f"Cualquier número distinto de cero elevado a la potencia 0 es <strong>1</strong>. Así, {pot(8, 0)} = 1 y {pot(250, 0)} = 1.")}</p>
{tabla(t("Why the exponent 0 gives 1", "Por qué el exponente 0 da 1"), t("Powers of 2 from the exponent 3 down to 0: each time the exponent goes down 1, the value is divided by 2", "Potencias de 2 del exponente 3 al 0: cada vez que el exponente baja 1, el valor se divide entre 2"),
       [t("Power", "Potencia"), t("Value", "Valor"), t("When the exponent goes down 1", "Al bajar el exponente 1")],
       [[pot(2, 3), "8", "—"], [pot(2, 2), "4", t("divide by 2", "se divide entre 2")], [pot(2, 1), "2", t("divide by 2", "se divide entre 2")], [pot(2, 0), "<strong>1</strong>", t("divide by 2: 2 ÷ 2 = 1", "se divide entre 2: 2 ÷ 2 = 1")]])}
{caja("tip", t("Do not mix them up", "No los confunda"), t(f"<p>{pot('a', 0)} = 1 (always 1), but {pot('a', 1)} = a (the number itself). The exponent 0 gives 1; the exponent 1 gives the base.</p>", f"<p>{pot('a', 0)} = 1 (siempre 1), pero {pot('a', 1)} = a (el mismo número). El exponente 0 da 1; el exponente 1 da la base.</p>"))}
<h3>{t("A negative base", "Una base negativa")}</h3>
<p>{t("When the base is negative and in parentheses, the sign is multiplied too. By the sign rule from Topic 1, the answer is <strong>positive if the exponent is even</strong> and <strong>negative if it is odd</strong>.", "Cuando la base es negativa y está entre paréntesis, el signo también se multiplica. Por la regla de los signos del Tema 1, el resultado es <strong>positivo si el exponente es par</strong> y <strong>negativo si es impar</strong>.")}</p>
{ejemplo(t(f"Example: (−3)<sup>2</sup> and (−3)<sup>3</sup>", f"Ejemplo: (−3)<sup>2</sup> y (−3)<sup>3</sup>"),
  [("1", t("Even exponent.", "Exponente par."), t("(−3)<sup>2</sup> = (−3) × (−3) = 9. Same signs: positive.", "(−3)<sup>2</sup> = (−3) × (−3) = 9. Signos iguales: positivo.")),
   ("2", t("Odd exponent.", "Exponente impar."), t("(−3)<sup>3</sup> = (−3) × (−3) × (−3) = 9 × (−3) = −27.", "(−3)<sup>3</sup> = (−3) × (−3) × (−3) = 9 × (−3) = −27.")),
   ("✓", t("Result.", "Resultado."), t("(−3)<sup>2</sup> = <strong>9</strong> and (−3)<sup>3</sup> = <strong>−27</strong>", "(−3)<sup>2</sup> = <strong>9</strong> y (−3)<sup>3</sup> = <strong>−27</strong>"))])}
{caja("ojo", t("Watch out! Parentheses matter", "¡Ojo! Los paréntesis importan"), t("<p>(−3)<sup>2</sup> = 9, but −3<sup>2</sup> = −9. Without parentheses, the exponent applies only to the 3: −3<sup>2</sup> = −(3 × 3) = −9. The GED test checks this difference.</p>",
"<p>(−3)<sup>2</sup> = 9, pero −3<sup>2</sup> = −9. Sin paréntesis, el exponente afecta solo al 3: −3<sup>2</sup> = −(3 × 3) = −9. El examen de GED comprueba esta diferencia.</p>"))}
{practica("p2", t("Practice 2 — The exponent 0", "Práctica 2 — El exponente 0"), t(f"What is {pot(6, 0)}?", f"¿Cuánto es {pot(6, 0)}?"),
          [("a", "0"), ("b", "6"), ("c", "1"), ("d", "60")])}
{practica("p3", t("Practice 3 — A negative base", "Práctica 3 — Una base negativa"), t("What is (−2)<sup>4</sup>?", "¿Cuánto es (−2)<sup>4</sup>?"),
          [("a", "−16"), ("b", "16"), ("c", "−8"), ("d", "8")])}
{enlace(n, t("special-cases", "casos-especiales"), t("special cases of the exponent", "casos especiales del exponente"), t("Practice the exponent 0, the exponent 1, and negative bases with and without parentheses.", "Practique el exponente 0, el exponente 1 y las bases negativas con paréntesis y sin ellos."))}'''

    s3 = f'''<p>{t("Powers of 10 have a very useful pattern: the exponent tells how many zeros follow the 1.", "Las potencias de 10 tienen un patrón muy útil: el exponente dice cuántos ceros siguen al 1.")}</p>
{tabla(t("Powers of 10", "Potencias de 10"), t("Powers of 10 written as multiplications and as numbers", "Potencias de 10 escritas como multiplicación y como número"),
       [t("Power", "Potencia"), t("Multiplication", "Multiplicación"), t("Value", "Valor")],
       [[pot(10, 1), "10", "10"], [pot(10, 2), "10 × 10", "100"], [pot(10, 3), "10 × 10 × 10", "1,000"], [pot(10, 4), "10 × 10 × 10 × 10", "10,000"], [pot(10, 6), "10 × … × 10 " + t("(6 times)", "(6 veces)"), "1,000,000"]])}
<p>{t("Multiplying a number by a power of 10 moves the decimal point to the <strong>right</strong> as many places as the exponent says. Add zeros if you need them.", "Multiplicar un número por una potencia de 10 corre el punto decimal hacia la <strong>derecha</strong> tantos lugares como dice el exponente. Si hace falta, se agregan ceros.")}</p>
{ejemplo(t(f"Example: 5.3 × {pot(10, 3)}", f"Ejemplo: 5.3 × {pot(10, 3)}"),
  [("1", t("Step 1.", "Paso 1."), t("The exponent is 3: move the decimal point 3 places to the right.", "El exponente es 3: el punto decimal se corre 3 lugares a la derecha.")),
   ("2", t("Step 2.", "Paso 2."), t("5.3 → 53. → 530. → 5300. (add zeros when the digits run out)", "5.3 → 53. → 530. → 5300. (se agregan ceros cuando se acaban las cifras)")),
   ("✓", t("Result.", "Resultado."), f"5.3 × {pot(10, 3)} = <strong>5,300</strong>")])}
{caja("tip", t("Looking ahead", "Un adelanto"), t("<p>This pattern of the powers of 10 is the base of <strong>scientific notation</strong>, which you will study in Level 3. Learning it well now will make that topic much easier.</p>",
"<p>Este patrón de las potencias de 10 es la base de la <strong>notación científica</strong>, que estudiará en el Nivel 3. Dominarlo ahora hará ese tema mucho más fácil.</p>"))}
{calc(t("Powers on the calculator", "Las potencias en la calculadora"), t(f"""<p>For any power, use the {T("^")} key: for {pot(2, 5)}, press {T("2")} {T("^")} {T("5")} {T("enter")}. The screen shows 32. To square a number, the {T("x<sup>2</sup>")} key is faster: {T("1")}{T("3")} {T("x<sup>2</sup>")} {T("enter")} shows 169.</p>
<p>For a negative base, use parentheses: {T("(")} {T("(−)")} {T("3")} {T(")")} {T("x<sup>2</sup>")} {T("enter")} shows 9. Without the parentheses, the calculator gives −9.</p>""",
f"""<p>Para cualquier potencia, use la tecla {T("^")}: para {pot(2, 5)}, pulse {T("2")} {T("^")} {T("5")} {T("enter")}. La pantalla muestra 32. Para elevar al cuadrado, la tecla {T("x<sup>2</sup>")} es más rápida: {T("1")}{T("3")} {T("x<sup>2</sup>")} {T("enter")} muestra 169.</p>
<p>Con una base negativa, use paréntesis: {T("(")} {T("(−)")} {T("3")} {T(")")} {T("x<sup>2</sup>")} {T("enter")} muestra 9. Sin los paréntesis, la calculadora da −9.</p>"""))}
{practica("p4", t("Practice 4 — Powers of 10", "Práctica 4 — Potencias de 10"), t(f"What is 4.7 × {pot(10, 2)}?", f"¿Cuánto es 4.7 × {pot(10, 2)}?"),
          [("a", "47"), ("b", "4,700"), ("c", "470"), ("d", "9.4")])}
{enlace(n, t("powers-of-10", "base-10"), t("powers of 10", "potencias de base 10"), t("Move the decimal point as many places as the exponent says.", "Corra el punto decimal tantos lugares como indica el exponente."))}'''

    cuadrados = "".join(f'<li>{k}<sup>2</sup> = <strong>{k*k}</strong></li>' for k in range(1, 16))
    s4 = f'''<p>{t("A <strong>perfect square</strong> is the result of squaring a whole number. Knowing the first fifteen by heart is a key skill: they are the tool for square roots in the next lesson.", "Un <strong>cuadrado perfecto</strong> es el resultado de elevar al cuadrado un número entero. Saberse de memoria los quince primeros es una destreza clave: son la herramienta para las raíces cuadradas de la próxima lección.")}</p>
<ul style="columns:3;column-gap:24px;list-style:none;padding-left:0;font-size:1.08em;line-height:1.9" aria-label="{t("The perfect squares from 1 to 225", "Los cuadrados perfectos del 1 al 225")}">{cuadrados}</ul>
{caja("tip", t("How to learn them", "Cómo aprenderlos"), t("<p>Learn them in groups of five: 1 to 25, 36 to 100, and 121 to 225. Flash cards help: the power on one side and the value on the other. The practice page has a set of cards you can flip.</p>",
"<p>Apréndalos en bloques de cinco: 1 a 25, 36 a 100 y 121 a 225. Las tarjetas de repaso ayudan: en una cara la potencia y en la otra el valor. La página de práctica tiene un juego de tarjetas que se pueden voltear.</p>"))}
{practica("p5", t("Practice 5 — A perfect square", "Práctica 5 — Un cuadrado perfecto"), t("Which of these numbers is a perfect square?", "¿Cuál de estos números es un cuadrado perfecto?"),
          [("a", "50"), ("b", "200"), ("c", "90"), ("d", "144")])}
{practica("p6", t("Practice 6 — Squared", "Práctica 6 — Al cuadrado"), t(f"What is {pot(13, 2)}?", f"¿Cuánto es {pot(13, 2)}?"),
          [("a", "169"), ("b", "26"), ("c", "139"), ("d", "196")])}
{enlace(n, t("perfect-squares", "cuadrados"), t("the perfect squares from 1 to 225", "los cuadrados perfectos del 1 al 225"), t("Review the fifteen perfect squares with flash cards until you know them at a glance.", "Repase los quince cuadrados perfectos con tarjetas hasta reconocerlos de un vistazo."))}'''

    secciones = [("s-" + t("base-exponent", "base-exponente"), t("What a power is: base and exponent", "Qué es una potencia: base y exponente"), s1),
                 ("s-" + t("special-cases", "casos-especiales"), t("Special cases of the exponent", "Casos especiales del exponente"), s2),
                 ("s-" + t("powers-of-10", "base-10"), t("Powers of 10", "Potencias de base 10"), s3),
                 ("s-" + t("perfect-squares", "cuadrados"), t("The perfect squares from 1 to 225", "Los cuadrados perfectos del 1 al 225"), s4)]

    lesson = {"next": t("Lesson 2.3", "Lección 2.3"), "review": t("sections 1, 2, and 4", "las secciones 1, 2 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("That is 4 × 3. The exponent tells how many times 4 is a factor: 4 × 4 × 4.", "Eso es 4 × 3. El exponente dice cuántas veces 4 es factor: 4 × 4 × 4."),
                                   "c": t("That is 4 + 3. Multiply 4 by itself three times.", "Eso es 4 + 3. Multiplique 4 por sí mismo tres veces."),
                                   "d": t("16 is 4 × 4, only two factors. The exponent 3 asks for three.", "16 es 4 × 4, solo dos factores. El exponente 3 pide tres.")},
             "right": t("4 × 4 × 4 = 16 × 4 = 64.", "4 × 4 × 4 = 16 × 4 = 64."), "solution": t("The base 4 is a factor 3 times: 4 × 4 = 16, and 16 × 4 = 64.", "La base 4 es factor 3 veces: 4 × 4 = 16, y 16 × 4 = 64.")},
      "p2": {"ok": "c", "hints": {"a": t("With the exponent 0 the answer is 1, not 0.", "Con el exponente 0 el resultado es 1, no 0."),
                                   "b": t("6 would be the exponent 1. The exponent 0 always gives 1.", "6 sería el exponente 1. El exponente 0 siempre da 1."),
                                   "d": t("The exponent does not mean adding zeros to 6. Any number (not zero) to the power 0 is 1.", "El exponente no quiere decir agregar ceros al 6. Cualquier número (distinto de cero) elevado a 0 es 1.")},
             "right": t("Any number other than zero to the power 0 is 1.", "Cualquier número distinto de cero elevado a 0 es 1."), "solution": t(f"{pot(6, 0)} = 1. Follow the pattern: 6<sup>1</sup> = 6, and dividing by 6 once more gives 1.", f"{pot(6, 0)} = 1. Siga el patrón: 6<sup>1</sup> = 6, y al dividir otra vez entre 6 se obtiene 1.")},
      "p3": {"ok": "b", "hints": {"a": t("The value 16 is right. The exponent 4 is even: what sign does the answer get?", "El valor 16 está bien. El exponente 4 es par: ¿qué signo lleva el resultado?"),
                                   "c": t("That is (−2) × 4. The base is a factor 4 times.", "Eso es (−2) × 4. La base es factor 4 veces."),
                                   "d": t("That is 2 × 4. Multiply (−2) by itself four times.", "Eso es 2 × 4. Multiplique (−2) por sí mismo cuatro veces.")},
             "right": t("(−2) × (−2) × (−2) × (−2) = 16. An even exponent gives a positive answer.", "(−2) × (−2) × (−2) × (−2) = 16. Un exponente par da un resultado positivo."), "solution": t("(−2)<sup>4</sup> = (−2) × (−2) × (−2) × (−2) = 4 × 4 = 16. Even exponent: positive.", "(−2)<sup>4</sup> = (−2) × (−2) × (−2) × (−2) = 4 × 4 = 16. Exponente par: positivo.")},
      "p4": {"ok": "c", "hints": {"a": t("47 moves the point only 1 place. The exponent 2 asks for 2 places.", "47 corre el punto solo 1 lugar. El exponente 2 pide 2 lugares."),
                                   "b": t("4,700 moves the point 3 places. The exponent is 2.", "4,700 corre el punto 3 lugares. El exponente es 2."),
                                   "d": t("9.4 is 4.7 × 2. The exponent is not a factor: 10<sup>2</sup> = 100.", "9.4 es 4.7 × 2. El exponente no es un factor: 10<sup>2</sup> = 100.")},
             "right": t("Move the point 2 places to the right: 4.7 → 47. → 470.", "Se corre el punto 2 lugares a la derecha: 4.7 → 47. → 470."), "solution": t("10<sup>2</sup> = 100, so move the point 2 places to the right: 4.7 × 100 = 470.", "10<sup>2</sup> = 100, así que el punto se corre 2 lugares a la derecha: 4.7 × 100 = 470.")},
      "p5": {"ok": "d", "hints": {"a": t("7 × 7 = 49 and 8 × 8 = 64: 50 is between two perfect squares.", "7 × 7 = 49 y 8 × 8 = 64: 50 queda entre dos cuadrados perfectos."),
                                   "b": t("14 × 14 = 196 and 15 × 15 = 225: 200 is not a perfect square.", "14 × 14 = 196 y 15 × 15 = 225: 200 no es un cuadrado perfecto."),
                                   "c": t("9 × 9 = 81 and 10 × 10 = 100: 90 is not a perfect square.", "9 × 9 = 81 y 10 × 10 = 100: 90 no es un cuadrado perfecto.")},
             "right": t("144 = 12 × 12.", "144 = 12 × 12."), "solution": t("144 = 12 × 12, so it is a perfect square. The others are between two perfect squares.", "144 = 12 × 12, así que es un cuadrado perfecto. Los demás quedan entre dos cuadrados perfectos.")},
      "p6": {"ok": "a", "hints": {"b": t("That is 13 × 2. Squaring is 13 × 13.", "Eso es 13 × 2. Elevar al cuadrado es 13 × 13."),
                                   "c": t("Check the multiplication: 13 × 13 = 130 + 39.", "Revise la multiplicación: 13 × 13 = 130 + 39."),
                                   "d": t("196 is 14<sup>2</sup>. Look for 13 × 13.", "196 es 14<sup>2</sup>. Busque 13 × 13.")},
             "right": t("13 × 13 = 169.", "13 × 13 = 169."), "solution": t("13<sup>2</sup> = 13 × 13 = 130 + 39 = 169.", "13<sup>2</sup> = 13 × 13 = 130 + 39 = 169.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("That is 3 × 4. Multiply 3 by itself four times.", "Eso es 3 × 4. Multiplique 3 por sí mismo cuatro veces."), "b": t("27 is 3<sup>3</sup>, only three factors.", "27 es 3<sup>3</sup>, solo tres factores."), "d": t("That is 4<sup>3</sup>. The base is 3.", "Eso es 4<sup>3</sup>. La base es 3.")},
            "solution": t("3 × 3 × 3 × 3 = 9 × 9 = 81.", "3 × 3 × 3 × 3 = 9 × 9 = 81.")},
      "B": {"ok": "a", "hints": {"b": t("The exponent 0 always gives 1, not 0.", "El exponente 0 siempre da 1, no 0."), "c": t("7 would be the exponent 1.", "7 sería el exponente 1."), "d": t("The exponent 0 always gives 1.", "El exponente 0 siempre da 1.")},
            "solution": t("Any number other than zero to the power 0 is 1.", "Cualquier número distinto de cero elevado a 0 es 1.")},
      "C": {"ok": "d", "hints": {"a": t("The exponent 1 does not give 1: it gives the base.", "El exponente 1 no da 1: da la base."), "b": t("The exponent 1 does not give 0.", "El exponente 1 no da 0."), "c": t("The exponent is not a factor: it counts the factors.", "El exponente no es un factor: cuenta los factores.")},
            "solution": t("With the exponent 1, the base appears once: 9<sup>1</sup> = 9.", "Con el exponente 1, la base aparece una vez: 9<sup>1</sup> = 9.")},
      "D": {"ok": "b", "hints": {"a": t("The value 27 is right. The exponent 3 is odd: what sign is the answer?", "El valor 27 está bien. El exponente 3 es impar: ¿qué signo lleva el resultado?"), "c": t("That is (−3) × 3. The base is a factor 3 times.", "Eso es (−3) × 3. La base es factor 3 veces."), "d": t("That is (−3) × (−3), only two factors.", "Eso es (−3) × (−3), solo dos factores.")},
            "solution": t("(−3) × (−3) × (−3) = 9 × (−3) = −27. Odd exponent: negative.", "(−3) × (−3) × (−3) = 9 × (−3) = −27. Exponente impar: negativo.")},
      "E": {"ok": "c", "hints": {"a": t("The parentheses make the base −5: (−5) × (−5). Same signs.", "Los paréntesis hacen que la base sea −5: (−5) × (−5). Signos iguales."), "b": t("That is (−5) × 2. The base is a factor 2 times.", "Eso es (−5) × 2. La base es factor 2 veces."), "d": t("That is 5 × 2.", "Eso es 5 × 2.")},
            "solution": t("(−5)<sup>2</sup> = (−5) × (−5) = 25.", "(−5)<sup>2</sup> = (−5) × (−5) = 25.")},
      "F": {"ok": "a", "hints": {"b": t("Without parentheses, the exponent applies only to the 5. The minus sign stays.", "Sin paréntesis, el exponente afecta solo al 5. El signo menos se queda."), "c": t("That is −5 × 2.", "Eso es −5 × 2."), "d": t("That is 5 × 2.", "Eso es 5 × 2.")},
            "solution": t("−5<sup>2</sup> = −(5 × 5) = −25. Without parentheses, the minus sign is not part of the base.", "−5<sup>2</sup> = −(5 × 5) = −25. Sin paréntesis, el signo menos no es parte de la base.")},
      "G": {"ok": "d", "hints": {"a": t("That is 10 × 5.", "Eso es 10 × 5."), "b": t("10,000 has 4 zeros. The exponent 5 asks for 5 zeros.", "10,000 tiene 4 ceros. El exponente 5 pide 5 ceros."), "c": t("1,000,000 has 6 zeros. The exponent is 5.", "1,000,000 tiene 6 ceros. El exponente es 5.")},
            "solution": t("10<sup>5</sup> is 1 followed by 5 zeros: 100,000.", "10<sup>5</sup> es el 1 seguido de 5 ceros: 100,000.")},
      "H": {"ok": "b", "hints": {"a": t("That moves the point 3 places. The exponent is 4.", "Eso corre el punto 3 lugares. El exponente es 4."), "c": t("That is 8 × 4. 10<sup>4</sup> = 10,000.", "Eso es 8 × 4. 10<sup>4</sup> = 10,000."), "d": t("That moves the point 5 places. The exponent is 4.", "Eso corre el punto 5 lugares. El exponente es 4.")},
            "solution": t("10<sup>4</sup> = 10,000, so 8 × 10,000 = 80,000.", "10<sup>4</sup> = 10,000, así que 8 × 10,000 = 80,000.")}
     }}

    quiz = [
     ("A", t(f"What is {pot(3, 4)}?", f"¿Cuánto es {pot(3, 4)}?"), [("a", "12"), ("b", "27"), ("c", "81"), ("d", "64")]),
     ("B", t(f"What is {pot(7, 0)}?", f"¿Cuánto es {pot(7, 0)}?"), [("a", "1"), ("b", "0"), ("c", "7"), ("d", "70")]),
     ("C", t(f"What is {pot(9, 1)}?", f"¿Cuánto es {pot(9, 1)}?"), [("a", "1"), ("b", "0"), ("c", "10"), ("d", "9")]),
     ("D", t("What is (−3)<sup>3</sup>?", "¿Cuánto es (−3)<sup>3</sup>?"), [("a", "27"), ("b", "−27"), ("c", "−9"), ("d", "9")]),
     ("E", t("What is (−5)<sup>2</sup>?", "¿Cuánto es (−5)<sup>2</sup>?"), [("a", "−25"), ("b", "−10"), ("c", "25"), ("d", "10")]),
     ("F", t("What is −5<sup>2</sup> (no parentheses)?", "¿Cuánto es −5<sup>2</sup> (sin paréntesis)?"), [("a", "−25"), ("b", "25"), ("c", "−10"), ("d", "10")]),
     ("G", t(f"What is {pot(10, 5)}?", f"¿Cuánto es {pot(10, 5)}?"), [("a", "50"), ("b", "10,000"), ("c", "1,000,000"), ("d", "100,000")]),
     ("H", t(f"What is 8 × {pot(10, 4)}?", f"¿Cuánto es 8 × {pot(10, 4)}?"), [("a", "8,000"), ("b", "80,000"), ("c", "32"), ("d", "800,000")])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("A short way to write repeated multiplication: base and exponent, the exponents 0 and 1, powers of 10, and the perfect squares.", "Una forma corta de escribir la multiplicación repetida: base y exponente, los exponentes 0 y 1, las potencias de 10 y los cuadrados perfectos."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Tell</strong> the base from the exponent, and evaluate powers.", "<strong>Distinguir</strong> la base del exponente y evaluar potencias."),
         t("<strong>Use</strong> the exponent 0 and the exponent 1 correctly.", "<strong>Aplicar</strong> correctamente el exponente 0 y el exponente 1."),
         t("<strong>Evaluate</strong> powers with a negative base, with and without parentheses.", "<strong>Evaluar</strong> potencias de base negativa, con paréntesis y sin ellos."),
         t("<strong>Multiply</strong> by powers of 10 by moving the decimal point.", "<strong>Multiplicar</strong> por potencias de 10 corriendo el punto decimal."),
         t("<strong>Know</strong> the fifteen perfect squares from 1 to 225.", "<strong>Reconocer</strong> los quince cuadrados perfectos del 1 al 225.")],
        secciones,
        (t("Write and evaluate twelve powers, including some with the exponent 0 and some with a negative base (with and without parentheses). Then do four multiplications by powers of 10 in your head and check them on paper.",
           "Escriba y evalúe doce potencias, incluidas algunas con exponente 0 y otras con base negativa (con paréntesis y sin ellos). Después haga mentalmente cuatro multiplicaciones por potencias de 10 y compruébelas en papel."),
         t("Make fifteen flash cards for the perfect squares: 7<sup>2</sup> on one side, 49 on the other. Review them for five minutes a day this week, on the bus or during a break.",
           "Haga quince tarjetas de repaso de los cuadrados perfectos: 7<sup>2</sup> en una cara y 49 en la otra. Repáselas cinco minutos al día esta semana, en el autobús o en un descanso.")),
        quiz,
        t("Self-check checklist for exponents and powers of 10", "Lista de autoevaluación de los exponentes y las potencias de 10"),
        t("Self-check checklist: skills for exponents, powers of 10, and perfect squares", "Lista de autoevaluación: destrezas con exponentes, potencias de 10 y cuadrados perfectos"),
        [(t("Base and exponent", "Base y exponente"), t("I evaluate powers, also with a negative base, and can explain how.", "Evalúo potencias, también de base negativa, y sé explicar cómo."), t("I evaluate simple powers, but negative bases confuse me.", "Evalúo potencias sencillas, pero las bases negativas me confunden."), t("I multiply the base by the exponent.", "Multiplico la base por el exponente.")),
         (t("The exponents 0 and 1", "Los exponentes 0 y 1"), t("I use both and can explain why the exponent 0 gives 1.", "Aplico los dos y sé explicar por qué el exponente 0 da 1."), t("I use one of them, but I mix up the other.", "Aplico uno, pero confundo el otro."), t("I do not tell them apart yet.", "Todavía no los distingo.")),
         (t("Powers of 10", "Potencias de 10"), t("I move the decimal point the right number of places every time.", "Corro el punto decimal los lugares correctos siempre."), t("I move the point, but sometimes one place too many or too few.", "Corro el punto, pero a veces un lugar de más o de menos."), t("I multiply by the exponent instead.", "Multiplico por el exponente.")),
         (t("Perfect squares", "Cuadrados perfectos"), t("I know the fifteen by heart.", "Me sé los quince de memoria."), t("I know some and look up the rest.", "Me sé algunos y busco los demás."), t("I do not recognize them yet.", "Todavía no los reconozco."))],
        t("<p>You learned to write and evaluate powers: the base and the exponent, the exponents 0 and 1, negative bases, the powers of 10, and the fifteen perfect squares from 1 to 225.</p>\n<p>In <strong>Lesson 2.3 · Square roots of perfect squares</strong> you will finish Topic 2 with the operation that undoes squaring. If you know the perfect squares, you will find their square roots at once: they are, literally, the key to the next lesson.</p>",
          "<p>Aprendió a escribir y evaluar potencias: la base y el exponente, los exponentes 0 y 1, las bases negativas, las potencias de 10 y los quince cuadrados perfectos del 1 al 225.</p>\n<p>En la <strong>Lección 2.3 · Raíces cuadradas de cuadrados perfectos</strong> terminará el Tema 2 con la operación que deshace el elevar al cuadrado. Si conoce los cuadrados perfectos, hallará sus raíces de inmediato: son, literalmente, la llave de la próxima lección.</p>"),
        ("2-3", ("", t("Lesson 2.3 · Square roots of perfect squares", "Lección 2.3 · Raíces cuadradas de cuadrados perfectos"))),
        [(t("power", "potencia"), t("A short way to write a repeated multiplication: 5<sup>3</sup> = 5 × 5 × 5.", "Una forma corta de escribir una multiplicación repetida: 5<sup>3</sup> = 5 × 5 × 5.")),
         (t("base", "base"), t("The number that repeats as a factor.", "El número que se repite como factor.")),
         (t("exponent", "exponente"), t("The small raised number that tells how many times the base is a factor.", "El número pequeño y elevado que dice cuántas veces la base es factor.")),
         (t("squared / cubed", "al cuadrado / al cubo"), t("To the power 2 / to the power 3.", "Elevado a la 2 / elevado a la 3.")),
         (t("perfect square", "cuadrado perfecto"), t("The square of a whole number, like 1, 4, 9, 16, 25, …", "El cuadrado de un número entero, como 1, 4, 9, 16, 25, …")),
         (t("power of 10", "potencia de 10"), t("10 to some exponent: 1 followed by that many zeros.", "10 elevado a un exponente: el 1 seguido de esa cantidad de ceros."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "aparece": "The base {b} is a factor {e} {v}. Partial products: {p}.", "vez": "time", "veces": "times", "noEs": "It is not {b} × {e} = {r}.",
  "evalua": "Evaluate {p}.", "noMult": "The exponent does not multiply the base: it tells how many times the base is a factor.", "noSuma": "Do not add the base and the exponent.",
  "capPat": "The pattern of the powers of {b}", "cPot": "Power", "cVal": "Value", "cBaja": "When the exponent goes down 1", "divEntre": "divide by {b}",
  "conPar": "<strong>With parentheses:</strong> {p} = {m} = <strong>{r}</strong>. {s}", "impar": "Odd exponent: negative.", "par": "Even exponent: positive.", "imparL": "the exponent is odd, so the answer is negative.", "parL": "the exponent is even, so the answer is positive.",
  "sinPar": "<strong>Without parentheses:</strong> {p} = −({m}) = <strong>{r}</strong>. The minus sign is not part of the base: it applies at the end.",
  "exp0": "Any number other than zero to the power 0 is 1.", "no0": "With the exponent 0 the answer is 1, not 0.", "eso1": "That would be the exponent 1.",
  "exp1": "With the exponent 1, the base appears once: the answer is the base.",
  "pistaPar": "Count the minus signs that are multiplied: an even number of them gives a positive answer.",
  "conParE": "With parentheses, the sign is multiplied too: {s}", "sinParE": "Without parentheses, the exponent applies only to the {b}: {p} = −({v}) = {r}.", "pistaSinPar": "Is the minus sign inside the parentheses, as part of the base?",
  "igualesQ": "Are {a} and {b} equal?", "si1": "Yes, both are 1", "no0y": "No: {a} = 0 and {b} = {k}", "no1y": "No: {a} = 1 and {b} = {k}", "bienIg": "The exponent 0 gives 1; the exponent 1 gives the base.",
  "unoSeguido": "1 followed by {e} {z}", "cero": "zero", "ceros": "zeros", "corre": "The decimal point moves {e} {l} to the right{x}", "lugar": "place", "lugares": "places", "rellena": ", with zeros added if needed.", "porUno": ": multiplying by 1 changes nothing.",
  "cuantoVale": "What is {p}?", "noDiezPor": "It is not 10 × {e}: it is 1 followed by {e} zeros.", "bien10": "1 followed by {e} zeros.",
  "bienCorre": "The point moves {e} {l} to the right.", "pistaCorre": "The exponent tells how many places the point moves to the right.",
  "alCuad": "{n} squared", "es": " is {v}",
  "cuadradoQ": "What is {p}?", "noPor2": "Squaring is not multiplying by 2: it is multiplying the number by itself.",
  "raizQ": "The number {c} is the square of what positive number?", "noMitad": "Do not divide by 2: look for the number that times itself gives {c}.",
  "esCuadQ": "Which of these numbers is a perfect square?", "bienEsCuad": "{c} = {s} × {s}.", "pistaEsCuad": "Look for a number that is some whole number times itself.", "malEsCuad": "The perfect square is {c} = {s} × {s}. The others are not the square of any whole number."
 },
 "es": {
  "aparece": "La base {b} es factor {e} {v}. Productos parciales: {p}.", "vez": "vez", "veces": "veces", "noEs": "No es {b} × {e} = {r}.",
  "evalua": "Evalúe {p}.", "noMult": "El exponente no multiplica a la base: dice cuántas veces la base es factor.", "noSuma": "No se suman la base y el exponente.",
  "capPat": "El patrón de las potencias de {b}", "cPot": "Potencia", "cVal": "Valor", "cBaja": "Al bajar el exponente 1", "divEntre": "se divide entre {b}",
  "conPar": "<strong>Con paréntesis:</strong> {p} = {m} = <strong>{r}</strong>. {s}", "impar": "Exponente impar: negativo.", "par": "Exponente par: positivo.", "imparL": "el exponente es impar, así que el resultado es negativo.", "parL": "el exponente es par, así que el resultado es positivo.",
  "sinPar": "<strong>Sin paréntesis:</strong> {p} = −({m}) = <strong>{r}</strong>. El signo menos no es parte de la base: se aplica al final.",
  "exp0": "Cualquier número distinto de cero elevado a 0 es 1.", "no0": "Con el exponente 0 el resultado es 1, no 0.", "eso1": "Ese sería el exponente 1.",
  "exp1": "Con el exponente 1, la base aparece una sola vez: el resultado es la base.",
  "pistaPar": "Cuente los signos menos que se multiplican: una cantidad par da resultado positivo.",
  "conParE": "Con paréntesis, el signo también se multiplica: {s}", "sinParE": "Sin paréntesis, el exponente afecta solo al {b}: {p} = −({v}) = {r}.", "pistaSinPar": "¿El signo menos está dentro de los paréntesis, como parte de la base?",
  "igualesQ": "¿Valen lo mismo {a} y {b}?", "si1": "Sí, los dos valen 1", "no0y": "No: {a} = 0 y {b} = {k}", "no1y": "No: {a} = 1 y {b} = {k}", "bienIg": "El exponente 0 da 1; el exponente 1 da la base.",
  "unoSeguido": "el 1 seguido de {e} {z}", "cero": "cero", "ceros": "ceros", "corre": "El punto decimal se corre {e} {l} a la derecha{x}", "lugar": "lugar", "lugares": "lugares", "rellena": ", rellenando con ceros si hace falta.", "porUno": ": multiplicar por 1 no cambia nada.",
  "cuantoVale": "¿Cuánto vale {p}?", "noDiezPor": "No es 10 × {e}: es el 1 seguido de {e} ceros.", "bien10": "El 1 seguido de {e} ceros.",
  "bienCorre": "El punto se corre {e} {l} a la derecha.", "pistaCorre": "El exponente dice cuántos lugares se corre el punto a la derecha.",
  "alCuad": "{n} al cuadrado", "es": " es {v}",
  "cuadradoQ": "¿Cuánto vale {p}?", "noPor2": "Elevar al cuadrado no es multiplicar por 2: es multiplicar el número por sí mismo.",
  "raizQ": "El número {c} es el cuadrado de ¿qué número positivo?", "noMitad": "No se divide entre 2: se busca el número que multiplicado por sí mismo da {c}.",
  "esCuadQ": "¿Cuál de estos números es un cuadrado perfecto?", "bienEsCuad": "{c} = {s} × {s}.", "pistaEsCuad": "Busque un número que sea un entero multiplicado por sí mismo.", "malEsCuad": "El cuadrado perfecto es {c} = {s} × {s}. Los demás no son el cuadrado de ningún entero."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function esCuadrado(n){ var s = Math.round(Math.sqrt(n)); return s * s === n; }

/* ============ MODULE 1 · base and exponent ============ */
function pintaBE(){
  var b = +$("be-b").value, e = +$("be-e").value, fac = [], parc = [], v = 1;
  $("be-bv").textContent = b; $("be-ev").textContent = e;
  for (var i = 0; i < e; i++){ fac.push(b); v *= b; parc.push(com(v)); }
  $("be-salida").innerHTML = '<div class="linea grande">' + potH(b, e) + ' = ' + fac.join(" × ") + ' = ' + com(v) + '</div><div class="linea">' + F(TXT.aparece, { b: b, e: e, v: e === 1 ? TXT.vez : TXT.veces, p: parc.join(" → ") }) + '</div>' +
    (e > 1 ? '<div class="linea">' + F(TXT.noEs, { b: b, e: e, r: b * e }) + '</div>' : "");
}
function genPot(){
  var b = aleatorio(2, 10), e = b <= 3 ? aleatorio(2, 6) : (b <= 5 ? aleatorio(2, 4) : aleatorio(2, 3)), r = pw(b, e);
  return { enun: F(TXT.evalua, { p: potH(b, e) }), correcta: String(r), solucion: potH(b, e) + " = " + Array(e).fill(b).join(" × ") + " = " + com(r) + ".",
    evalua: numE(r, [{ v: b * e, msg: TXT.noMult }, { v: b + e, msg: TXT.noSuma }]) };
}

/* ============ MODULE 2 · special cases ============ */
function pintaCE(){
  var b = +$("ce-b").value, h = '<caption>' + F(TXT.capPat, { b: b }) + '</caption><thead><tr><th scope="col">' + TXT.cPot + '</th><th scope="col">' + TXT.cVal + '</th><th scope="col">' + TXT.cBaja + '</th></tr></thead><tbody>';
  for (var e = 4; e >= 0; e--) h += '<tr' + (e === 0 ? ' class="nueva"' : '') + '><td>' + potH(b, e) + '</td><td><strong>' + com(pw(b, e)) + '</strong></td><td>' + (e === 4 ? "—" : F(TXT.divEntre, { b: b })) + '</td></tr>';
  $("ce-tabla").innerHTML = h + '</tbody>';
}
function pintaBN(){
  var b = +$("bn-b").value, e = +$("bn-e").value, con = pw(b, e), sin = -pw(-b, e);
  $("bn-bv").textContent = ent(b); $("bn-ev").textContent = e;
  $("bn-salida").innerHTML = '<div class="linea">' + F(TXT.conPar, { p: potH(b, e, true), m: Array(e).fill("(" + ent(b) + ")").join(" × "), r: ent(con), s: e % 2 ? TXT.impar : TXT.par }) + '</div>' +
    '<div class="linea">' + F(TXT.sinPar, { p: "−" + (-b) + "<sup>" + e + "</sup>", m: Array(e).fill(-b).join(" × "), r: ent(sin) }) + '</div>';
}
function otro(r, b, e){ var c = [-b * e, b * e, -(b * e + 1), b * e + 1]; for (var i = 0; i < c.length; i++) if (c[i] !== r && c[i] !== -r) return c[i]; return r + 1; }
function genEspecial(){
  var tipo = aleatorio(1, 5), b = aleatorio(2, 50), pistas = {};
  function op(v){ return { html: ent(v), clave: "n" + v }; }
  if (tipo === 1){ pistas.n0 = TXT.no0; pistas["n" + b] = TXT.eso1; return { enun: potH(b, 0) + " =", opciones: [op(1), op(0), op(b)], correcta: "n1", pistas: pistas, pista: TXT.exp0, bien: TXT.exp0, mal: TXT.exp0 }; }
  if (tipo === 2) return { enun: potH(b, 1) + " =", opciones: [op(b), op(1), op(0)], correcta: "n" + b, pista: TXT.exp1, bien: TXT.exp1, mal: TXT.exp1 };
  var bb = aleatorio(2, 5), e = aleatorio(2, 4);
  if (tipo === 3){ var r = pw(-bb, e), s = F(TXT.conParE, { s: e % 2 ? TXT.imparL : TXT.parL }), x3 = otro(r, bb, e); return { enun: potH(-bb, e, true) + " =", opciones: [op(r), op(-r), op(x3)], correcta: "n" + r, pista: TXT.pistaPar, bien: s, mal: s }; }
  if (tipo === 4){ var r2 = -pw(bb, e), s2 = F(TXT.sinParE, { b: bb, p: "−" + bb + "<sup>" + e + "</sup>", v: pw(bb, e), r: ent(r2) }); var y3 = otro(r2, bb, e); return { enun: "−" + bb + "<sup>" + e + "</sup> =", opciones: [op(r2), op(-r2), op(y3)], correcta: "n" + r2, pista: TXT.pistaSinPar, bien: s2, mal: s2 }; }
  var a = aleatorio(2, 9);
  return { enun: F(TXT.igualesQ, { a: potH(a, 0), b: potH(a, 1) }), enOrden: true, opciones: [{ html: TXT.si1, clave: "s" }, { html: F(TXT.no0y, { a: potH(a, 0), b: potH(a, 1), k: a }), clave: "n1" }, { html: F(TXT.no1y, { a: potH(a, 0), b: potH(a, 1), k: a }), clave: "n2" }],
    correcta: "n2", pista: TXT.bienIg, bien: TXT.bienIg, mal: TXT.bienIg };
}

/* ============ MODULE 3 · powers of 10 ============ */
function porDiez(x, e){ var s = String(x), k = s.indexOf("."), en = k < 0 ? s : s.slice(0, k), de = k < 0 ? "" : s.slice(k + 1); while (de.length < e) de += "0"; var r = (en + de.slice(0, e)).replace(/^0+(?=\d)/, ""), resto = de.slice(e); return com(r) + (resto ? "." + resto : ""); }
function pintaB10(){
  var x = $("b10-x").value, e = +$("b10-e").value;
  $("b10-ev").textContent = e;
  $("b10-salida").innerHTML = '<div class="linea">' + potH(10, e) + ' = ' + (e === 0 ? "1" : F(TXT.unoSeguido, { e: e, z: e === 1 ? TXT.cero : TXT.ceros }) + " = " + com(pw(10, e))) + '.</div>' +
    '<div class="linea grande">' + x + ' × ' + potH(10, e) + ' = ' + porDiez(x, e) + '</div><div class="linea">' + F(TXT.corre, { e: e, l: e === 1 ? TXT.lugar : TXT.lugares, x: e > 0 ? TXT.rellena : TXT.porUno }) + '</div>';
}
function genB10(){
  if (Math.random() < 0.4){
    var e = aleatorio(2, 7), v = pw(10, e);
    return { enun: F(TXT.cuantoVale, { p: potH(10, e) }), opciones: [{ html: com(v), clave: "a" }, { html: com(v / 10), clave: "b" }, { html: com(v * 10), clave: "c" }, { html: String(10 * e), clave: "d" }], correcta: "a",
      pistas: { d: F(TXT.noDiezPor, { e: e }) }, pista: F(TXT.noDiezPor, { e: e }), bien: F(TXT.bien10, { e: e }), mal: F(TXT.bien10, { e: e }) + " " + com(v) + "." };
  }
  var x = elige(["4.7", "5.3", "8", "2.15", "6.08", "3.9", "0.75", "12.5"]), k = aleatorio(1, 4), bien = porDiez(x, k);
  var cand = [porDiez(x, k - 1), porDiez(x, k + 1), porDiez(x, k + 2)].filter(function(c){ return c !== bien; });
  var l = k === 1 ? TXT.lugar : TXT.lugares;
  return { enun: F(TXT.cuantoVale, { p: x + " × " + potH(10, k) }), opciones: [{ html: bien, clave: "a" }].concat(cand.map(function(c, i){ return { html: c, clave: "m" + i }; })), correcta: "a",
    pista: TXT.pistaCorre, bien: F(TXT.bienCorre, { e: k, l: l }), mal: F(TXT.bienCorre, { e: k, l: l }) + " " + x + " × " + potH(10, k) + " = " + bien + "." };
}

/* ============ MODULE 4 · perfect squares ============ */
function pintaTarjetas(){
  var h = "";
  for (var k = 1; k <= 15; k++) h += '<button type="button" aria-pressed="false" data-n="' + k + '" aria-label="' + F(TXT.alCuad, { n: k }) + '">' + k + '²</button>';
  $("cu-tarjetas").innerHTML = h;
  $("cu-tarjetas").querySelectorAll("button").forEach(function(b){ b.addEventListener("click", function(){ voltea(b, b.getAttribute("aria-pressed") !== "true"); }); });
}
function voltea(b, ver){ var k = +b.getAttribute("data-n"); b.setAttribute("aria-pressed", ver ? "true" : "false"); b.textContent = ver ? k + "² = " + k * k : k + "²"; b.setAttribute("aria-label", F(TXT.alCuad, { n: k }) + (ver ? F(TXT.es, { v: k * k }) : "")); }
function genCuadrado(){
  var k = aleatorio(2, 15);
  if (Math.random() < 0.5) return { enun: F(TXT.cuadradoQ, { p: potH(k, 2) }), correcta: String(k * k), solucion: k + " × " + k + " = " + k * k + ".", evalua: numE(k * k, [{ v: 2 * k, msg: TXT.noPor2 }]) };
  return { enun: F(TXT.raizQ, { c: k * k }), correcta: String(k), solucion: k + " × " + k + " = " + k * k + ".", evalua: numE(k, k * k % 2 ? [] : [{ v: k * k / 2, msg: F(TXT.noMitad, { c: k * k }) }]) };
}
function genEsCuadrado(){
  var s = aleatorio(4, 15), c = s * s, malos = [];
  while (malos.length < 3){ var mm = aleatorio(10, 230); if (!esCuadrado(mm) && malos.indexOf(mm) < 0) malos.push(mm); }
  return { enun: TXT.esCuadQ, opciones: [{ html: String(c), clave: "s" }].concat(malos.map(function(mm, i){ return { html: String(mm), clave: "m" + i }; })), correcta: "s",
    pista: TXT.pistaEsCuad, bien: F(TXT.bienEsCuad, { c: c, s: s }), mal: F(TXT.malEsCuad, { c: c, s: s }) };
}

/* ============ Start ============ */
["be-b", "be-e"].forEach(function(id){ $(id).addEventListener("input", pintaBE); }); pintaBE();
creaPracticaLibre("p1", genPot);
$("ce-b").addEventListener("change", pintaCE); pintaCE();
["bn-b", "bn-e"].forEach(function(id){ $(id).addEventListener("input", pintaBN); }); pintaBN();
creaPracticaOM("p2", genEspecial);
$("b10-x").addEventListener("change", pintaB10); $("b10-e").addEventListener("input", pintaB10); pintaB10();
creaPracticaOM("p3", genB10);
pintaTarjetas();
creaPracticaLibre("p4", genCuadrado);
creaPracticaOM("p5", genEsCuadrado);
'''

def libre_n(pid, titulo, etiqueta=None):
    """Respuesta escrita de un número positivo."""
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), t("Type only the number.", "Escriba solo el número."))

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    mods = [
     (t("base-exponent", "base-exponente"), t("Base and exponent", "Base y exponente"),
      f'''      <p>{t(f"A <strong>power</strong> is a repeated multiplication. The <strong>base</strong> is the number that repeats, and the <strong>exponent</strong> tells how many times it is a factor: {pot(5, 3)} = 5 × 5 × 5 = 125.", f"Una <strong>potencia</strong> es una multiplicación repetida. La <strong>base</strong> es el número que se repite y el <strong>exponente</strong> dice cuántas veces es factor: {pot(5, 3)} = 5 × 5 × 5 = 125.")}</p>
      <h3>{t("Build the power", "Construya la potencia")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("be-b", t("Base", "Base"), 1, 10, 2)}
          {deslizador("be-e", t("Exponent", "Exponente"), 1, 8, 5)}
        </div>
        <div class="salida" id="be-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("The most common mistake:", "El error más común:")}</strong> {t(f"the exponent does not multiply the base. {pot(5, 3)} is not 5 × 3 = 15; it is 5 × 5 × 5 = 125.", f"el exponente no multiplica a la base. {pot(5, 3)} no es 5 × 3 = 15; es 5 × 5 × 5 = 125.")}</div>
{libre_n("p1", t("Practice: evaluate the power", "Practique: evaluar la potencia"), t("Value", "Valor"))}'''),
     (t("special-cases", "casos-especiales"), t("Special cases of the exponent", "Casos especiales del exponente"),
      f'''      <p>{t(f"With the exponent 1, the answer is the base itself: {pot(9, 1)} = 9. With the exponent 0, the answer is always 1: {pot(8, 0)} = 1. And with a negative base in parentheses, the sign is multiplied too: positive if the exponent is even, negative if it is odd.", f"Con el exponente 1, el resultado es la base misma: {pot(9, 1)} = 9. Con el exponente 0, el resultado es siempre 1: {pot(8, 0)} = 1. Y con una base negativa entre paréntesis, el signo también se multiplica: positivo si el exponente es par y negativo si es impar.")}</p>
      <h3>{t("Why does the exponent 0 give 1? The pattern", "¿Por qué el exponente 0 da 1? El patrón")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="ce-b">{t("Base", "Base")}</label><select id="ce-b"><option>2</option><option>3</option><option>5</option><option>10</option></select></div></div>
        <div class="tabla-scroll"><table class="comparar patron" id="ce-tabla"></table></div>
      </div>
      <h3>{t("A negative base: with and without parentheses", "Una base negativa: con paréntesis y sin ellos")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("bn-b", t("Negative base", "Base negativa"), -6, -1, -3)}
          {deslizador("bn-e", t("Exponent", "Exponente"), 1, 6, 2)}
        </div>
        <div class="salida" id="bn-salida" aria-live="polite"></div>
      </div>
{B.om("p2", t("Practice: special cases", "Practique: casos especiales"))}'''),
     (t("powers-of-10", "base-10"), t("Powers of 10", "Potencias de base 10"),
      f'''      <p>{t(f"In the powers of 10, the exponent tells how many zeros follow the 1: {pot(10, 3)} = 1,000. And multiplying by 10<sup>n</sup> moves the decimal point n places to the right.", f"En las potencias de 10, el exponente dice cuántos ceros siguen al 1: {pot(10, 3)} = 1,000. Y multiplicar por 10<sup>n</sup> corre el punto decimal n lugares a la derecha.")}</p>
      <h3>{t("Move the point", "Corra el punto")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="b10-x">{t("Number", "Número")}</label><select id="b10-x"><option>5.3</option><option>4.7</option><option>8</option><option>2.15</option><option>0.6</option><option>1.25</option></select></div>
          {deslizador("b10-e", t("Exponent of 10", "Exponente de 10"), 0, 6, 3)}
        </div>
        <div class="salida" id="b10-salida" aria-live="polite"></div>
      </div>
{B.om("p3", t("Practice: powers of 10", "Practique: potencias de 10"))}'''),
     (t("perfect-squares", "cuadrados"), t("The perfect squares from 1 to 225", "Los cuadrados perfectos del 1 al 225"),
      f'''      <p>{t("A <strong>perfect square</strong> is the result of squaring a whole number. Learn the first fifteen by heart: they are the tool for square roots in the next lesson.", "Un <strong>cuadrado perfecto</strong> es el resultado de elevar un entero al cuadrado. Apréndase de memoria los quince primeros: son la herramienta para las raíces cuadradas de la próxima lección.")}</p>
      <h3>{t("Flash cards", "Tarjetas de repaso")}</h3>
      <p>{t("Each card shows a power; press it to see the value. Try to say the value before you flip the card.", "Cada tarjeta muestra una potencia; púlsela para ver el valor. Intente decirlo antes de voltearla.")}</p>
      <div class="tarjetas-c" id="cu-tarjetas"></div>
      <div class="caja-tip"><strong>{t("Strategy:", "Estrategia:")}</strong> {t("learn them in groups of five: 1 to 25, 36 to 100, and 121 to 225.", "apréndalos en bloques de cinco: 1 a 25, 36 a 100 y 121 a 225.")}</div>
{libre_n("p4", t("Practice: squares from memory", "Practique: cuadrados de memoria"))}
{B.om("p5", t("Practice: is it a perfect square?", "Practique: ¿es un cuadrado perfecto?"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Exponentes enteros positivos y potencias de base 10")
