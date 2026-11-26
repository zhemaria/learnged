"""Level 3 · Lesson 2.2 · Multiplying and dividing in scientific notation — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "2-2"
TEMA = ("Scientific notation", "Notación científica")
TIT = ("Multiplying and dividing in scientific notation", "Multiplicación y división en notación científica")

def s(c, k):
    return f"{c} × 10<sup>{k}</sup>"

def pasos3(items):
    return '<ol class="lista-tarea">' + "".join(f"<li>{x}</li>" for x in items) + "</ol>"

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 2.1 you converted between decimals and scientific notation and compared amounts by their order of magnitude. Now you will calculate with those amounts. The key is that a number in scientific notation has two separate parts, the coefficient and the power of 10, and each one is worked on its own: the coefficients with ordinary arithmetic, and the powers of 10 with the rules of exponents from Topic 1.",
"En la Lección 2.1 convirtió entre notación decimal y científica y comparó por orden de magnitud. Ahora va a operar con esas cantidades. La clave es que un número en notación científica tiene dos partes independientes, el coeficiente y la potencia de 10, y cada una se trata por separado: los coeficientes con aritmética común y las potencias de 10 con las reglas de los exponentes del Tema 1.")}</p>
<p><strong>{t("To multiply, always follow the same three steps:", "Para multiplicar se siguen siempre los mismos tres pasos:")}</strong></p>
{pasos3([t("<strong>Multiply</strong> the coefficients.", "<strong>Multiplicar</strong> los coeficientes."), t("<strong>Add</strong> the exponents of the powers of 10 (the product rule).", "<strong>Sumar</strong> los exponentes de las potencias de 10 (regla del producto)."), t("<strong>Check</strong> that the coefficient is from 1 to 10, and adjust it if needed.", "<strong>Verificar</strong> que el coeficiente quede entre 1 y 10, y ajustar si hace falta.")])}
{ejemplo(t(f"Example 1: find ({s(3, 4)})({s(2, 5)})", f"Ejemplo 1: calcule ({s(3, 4)})({s(2, 5)})"),
  [("1", t("Coefficients.", "Coeficientes."), "3 × 2 = 6."),
   ("2", t("Powers of 10.", "Potencias de 10."), t("Add the exponents: 4 + 5 = 9.", "Se suman los exponentes: 4 + 5 = 9.")),
   ("3", t("Check.", "Verificar."), t("6 is from 1 to 10: no adjustment needed.", "6 está entre 1 y 10: no hace falta ajustar.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s(6, 9)}</strong>")])}
{enlace(n, t("multiply", "multiplicar"), t("multiplying in three steps", "multiplicar en tres pasos"), t("Reveal the three steps one at a time, with your own numbers or with examples.", "Revele los tres pasos uno a uno, con sus propios números o con ejemplos."))}'''

    s2 = f'''<p>{t("Sometimes the product of the coefficients is 10 or more. Then the answer is not yet valid scientific notation, and you have to rewrite the coefficient, which changes the exponent.", "A veces el producto de los coeficientes es 10 o más. En ese caso el resultado todavía no está en notación científica válida y hay que reescribir el coeficiente, lo que cambia el exponente.")}</p>
{ejemplo(t(f"Example 2: find ({s(5, 3)})({s(4, 2)})", f"Ejemplo 2: calcule ({s(5, 3)})({s(4, 2)})"),
  [("1", t("Coefficients.", "Coeficientes."), "5 × 4 = 20."),
   ("2", t("Powers of 10.", "Potencias de 10."), t(f"3 + 2 = 5. Partial answer: {s(20, 5)}.", f"3 + 2 = 5. Resultado parcial: {s(20, 5)}.")),
   ("3", t("Adjust.", "Ajustar."), t(f"20 is not from 1 to 10: rewrite 20 = {s('2.0', 1)}, and add that exponent to the 5.", f"20 no está entre 1 y 10: se reescribe 20 = {s('2.0', 1)}, y ese exponente se suma al 5.")),
   ("✓", t("Answer.", "Respuesta."), f"{s(20, 5)} = <strong>{s(2, 6)}</strong>")])}
{tabla(t("How the exponent makes up for the adjustment", "Cómo se compensa el exponente al ajustar"), t("How the exponent makes up for the adjustment of the coefficient", "Cómo se compensa el exponente al ajustar el coeficiente"),
       [t("If the coefficient…", "Si el coeficiente…"), t("The point moves", "El punto se mueve"), t("The exponent", "El exponente")],
       [[t("is 10 or more", "es 10 o más"), t("to the left", "a la izquierda"), t("goes up 1 for each place", "sube 1 por cada lugar")],
        [t("is less than 1", "es menor que 1"), t("to the right", "a la derecha"), t("goes down 1 for each place", "baja 1 por cada lugar")]])}
{caja("tip", t("What one loses, the other gains", "Lo que pierde uno lo gana el otro"), t("<p>If the coefficient becomes 10 times smaller, the power of 10 becomes 10 times larger. That is why the value of the number does not change when you adjust.</p>", "<p>Si el coeficiente se hace 10 veces más pequeño, la potencia de 10 se hace 10 veces más grande. Por eso el valor del número no cambia al ajustar.</p>"))}
{practica("p1", t("Practice 1 — Multiply", "Práctica 1 — Multiplique"), t(f"What is ({s(2, 4)})({s(4, 3)})?", f"¿Cuánto es ({s(2, 4)})({s(4, 3)})?"),
          [("a", s(8, 7)), ("b", s(8, 12)), ("c", s(6, 7)), ("d", s(8, 1))])}
{practica("p2", t("Practice 2 — Adjust", "Práctica 2 — Ajuste"), t(f"What is ({s(5, 3)})({s(4, 2)}) in valid scientific notation?", f"¿Cuánto es ({s(5, 3)})({s(4, 2)}) en notación científica válida?"),
          [("a", s(20, 5)), ("b", s(2, 6)), ("c", s(2, 5)), ("d", s(9, 5))])}
{enlace(n, t("adjust", "ajustar"), t("adjusting the coefficient", "ajustar el coeficiente"), t("Move the point of the coefficient and watch the exponent make up for it.", "Mueva el punto del coeficiente y observe cómo lo compensa el exponente."))}'''

    s3 = f'''<p>{t("Division follows the same logic with the opposite operations: the coefficients are <strong>divided</strong> and the exponents of 10 are <strong>subtracted</strong> (the quotient rule).", "La división sigue la misma lógica con las operaciones inversas: los coeficientes se <strong>dividen</strong> y los exponentes de 10 se <strong>restan</strong> (regla del cociente).")}</p>
{pasos3([t("<strong>Divide</strong> the coefficients.", "<strong>Dividir</strong> los coeficientes."), t("<strong>Subtract</strong> the exponents: the top one minus the bottom one.", "<strong>Restar</strong> los exponentes: el del numerador menos el del denominador."), t("<strong>Check</strong> the coefficient and adjust it. In division it often ends up less than 1.", "<strong>Verificar</strong> y ajustar el coeficiente. En la división suele quedar menor que 1.")])}
{ejemplo(t(f"Example 3: find ({s(8, 7)}) ÷ ({s(2, 3)})", f"Ejemplo 3: calcule ({s(8, 7)}) ÷ ({s(2, 3)})"),
  [("1", t("Coefficients.", "Coeficientes."), "8 ÷ 2 = 4."),
   ("2", t("Powers of 10.", "Potencias de 10."), t("Subtract the exponents: 7 − 3 = 4.", "Se restan los exponentes: 7 − 3 = 4.")),
   ("3", t("Check.", "Verificar."), t("4 is from 1 to 10: no adjustment needed.", "4 está entre 1 y 10: no hace falta ajustar.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s(4, 4)}</strong>")])}
{ejemplo(t(f"Example 4: find ({s(3, 4)}) ÷ ({s(6, 7)})", f"Ejemplo 4: calcule ({s(3, 4)}) ÷ ({s(6, 7)})"),
  [("1", t("Coefficients.", "Coeficientes."), "3 ÷ 6 = 0.5."),
   ("2", t("Powers of 10.", "Potencias de 10."), t(f"4 − 7 = −3. Partial answer: {s('0.5', '−3')}.", f"4 − 7 = −3. Resultado parcial: {s('0.5', '−3')}.")),
   ("3", t("Adjust.", "Ajustar."), t(f"0.5 is less than 1: rewrite 0.5 = {s(5, '−1')}, and add that exponent to the −3.", f"0.5 es menor que 1: se reescribe 0.5 = {s(5, '−1')}, y ese exponente se suma al −3.")),
   ("✓", t("Answer.", "Respuesta."), f"{s('0.5', '−3')} = <strong>{s(5, '−4')}</strong>")])}
{caja("ojo", t("A common mistake", "Error frecuente"), t(f"<p>Leaving the answer as {s('0.5', '−3')} or {s(20, 5)}. Even if the arithmetic is right, it is not valid scientific notation until the coefficient is from 1 to 10.</p>", f"<p>Dejar el resultado como {s('0.5', '−3')} o {s(20, 5)}. Aunque la aritmética sea correcta, no es notación científica válida hasta que el coeficiente quede entre 1 y 10.</p>"))}
{practica("p3", t("Practice 3 — Divide", "Práctica 3 — Divida"), t(f"What is ({s(9, 5)}) ÷ ({s(3, '−2')})?", f"¿Cuánto es ({s(9, 5)}) ÷ ({s(3, '−2')})?"),
          [("a", s(3, 3)), ("b", s(3, 7)), ("c", s(3, "−10")), ("d", s(6, 7))])}
{practica("p4", t("Practice 4 — Divide and adjust", "Práctica 4 — Divida y ajuste"), t(f"What is ({s(4, 3)}) ÷ ({s(8, 5)})?", f"¿Cuánto es ({s(4, 3)}) ÷ ({s(8, 5)})?"),
          [("a", s("0.5", "−2")), ("b", s(5, "−2")), ("c", s(5, "−3")), ("d", s(2, "−2"))])}
{enlace(n, t("divide", "dividir"), t("dividing in scientific notation", "dividir en notación científica"), t("Divide the coefficients, subtract the exponents, and adjust.", "Divida los coeficientes, reste los exponentes y ajuste."))}'''

    s4 = f'''<p>{t("In a word problem, the first thing to decide is the operation. A useful hint:", "En los problemas de contexto, lo primero es decidir la operación. Una pista útil:")}</p>
<ul>
<li>{t("<strong>Multiply</strong> when an amount repeats many times: speed times time, amount per day times number of days.", "<strong>Multiplicar</strong> cuando una cantidad se repite muchas veces: velocidad por tiempo, cantidad por día por número de días.")}</li>
<li>{t("<strong>Divide</strong> when a total is shared out, or the question asks “how many fit” or “how much for each one.”", "<strong>Dividir</strong> cuando se reparte un total o se pregunta «cuántos caben» o «cuánto por cada uno».")}</li>
</ul>
{ejemplo(t(f"Example 5: light travels {s(3, 5)} km per second. How far does it go in {s(2, 2)} seconds?", f"Ejemplo 5: la luz viaja a {s(3, 5)} km por segundo. ¿Qué distancia recorre en {s(2, 2)} segundos?"),
  [("1", t("Operation.", "Operación."), t(f"Distance = speed × time: ({s(3, 5)})({s(2, 2)}).", f"Distancia = velocidad × tiempo: ({s(3, 5)})({s(2, 2)}).")),
   ("2", t("Three steps.", "Tres pasos."), t("3 × 2 = 6; 5 + 2 = 7; 6 is already valid.", "3 × 2 = 6; 5 + 2 = 7; 6 ya es válido.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s(6, 7)} km</strong>")])}
{calc(t("Check with the calculator", "Compruebe con la calculadora"), t(f"<p>Type each number with the {T('×10<sup>n</sup>')} key: {T('3')} {T('×10<sup>n</sup>')} {T('5')} {T('×')} {T('2')} {T('×10<sup>n</sup>')} {T('2')} {T('enter')}. The screen shows 60000000, that is, {s(6, 7)}. The key puts in the power of 10 without typing “× 10,” which prevents mistakes with very large or very small numbers. Work it out by hand first, then use the calculator to check.</p>",
f"<p>Escriba cada número con la tecla {T('×10<sup>n</sup>')}: {T('3')} {T('×10<sup>n</sup>')} {T('5')} {T('×')} {T('2')} {T('×10<sup>n</sup>')} {T('2')} {T('enter')}. La pantalla muestra 60000000, es decir, {s(6, 7)}. La tecla introduce la potencia de 10 sin escribir «× 10», lo que evita errores con números muy grandes o muy pequeños. Resuelva primero a mano y use la calculadora para comprobar.</p>"))}
{enlace(n, t("real", "real"), t("a real calculation", "un cálculo real"), t("Choose the operation and solve science and technology problems.", "Elija la operación y resuelva problemas de ciencia y tecnología."))}'''

    secciones = [("s-" + t("multiply", "multiplicar"), t("Multiplying in three steps", "Multiplicar: el procedimiento en tres pasos"), s1),
                 ("s-" + t("adjust", "ajustar"), t("When the coefficient needs adjusting", "Cuando hay que ajustar el coeficiente"), s2),
                 ("s-" + t("divide", "dividir"), t("Dividing in scientific notation", "Dividir en notación científica"), s3),
                 ("s-" + t("real", "real"), t("A real calculation and the calculator", "Un cálculo real y la calculadora"), s4)]

    lesson = {"next": t("Lesson 2.3", "Lección 2.3"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("You multiplied the exponents. With powers of 10, add them: 4 + 3.", "Multiplicó los exponentes. Con potencias de 10 se suman: 4 + 3."), "c": t("You added the coefficients. Multiply them: 2 × 4.", "Sumó los coeficientes. Se multiplican: 2 × 4."), "d": t("You subtracted the exponents. When you multiply, add them.", "Restó los exponentes. Al multiplicar se suman.")},
             "right": t("2 × 4 = 8 and 4 + 3 = 7.", "2 × 4 = 8 y 4 + 3 = 7."), "solution": t(f"Coefficients: 2 × 4 = 8. Exponents: 4 + 3 = 7. So {s(8, 7)}.", f"Coeficientes: 2 × 4 = 8. Exponentes: 4 + 3 = 7. Así que {s(8, 7)}.")},
      "p2": {"ok": "b", "hints": {"a": t("The value is right, but 20 is not from 1 to 10: adjust it.", "El valor es correcto, pero 20 no está entre 1 y 10: ajústelo."), "c": t("When the coefficient goes from 20 to 2, the exponent must go up 1.", "Al pasar el coeficiente de 20 a 2, el exponente tiene que subir 1."), "d": t("You added the coefficients. Multiply them: 5 × 4.", "Sumó los coeficientes. Se multiplican: 5 × 4.")},
             "right": t(f"{s(20, 5)} = {s(2, 6)}.", f"{s(20, 5)} = {s(2, 6)}."), "solution": t(f"5 × 4 = 20 and 3 + 2 = 5: {s(20, 5)}. Adjust: 20 = {s(2, 1)}, so {s(2, 6)}.", f"5 × 4 = 20 y 3 + 2 = 5: {s(20, 5)}. Se ajusta: 20 = {s(2, 1)}, así que {s(2, 6)}.")},
      "p3": {"ok": "b", "hints": {"a": t("5 − (−2) is not 3. Subtracting a negative number is adding.", "5 − (−2) no es 3. Restar un negativo es sumar."), "c": t("Subtract the top exponent minus the bottom one: 5 − (−2).", "Se resta el de arriba menos el de abajo: 5 − (−2)."), "d": t("Divide the coefficients: 9 ÷ 3 = 3.", "Divida los coeficientes: 9 ÷ 3 = 3.")},
             "right": t("9 ÷ 3 = 3 and 5 − (−2) = 7.", "9 ÷ 3 = 3 y 5 − (−2) = 7."), "solution": t(f"Coefficients: 9 ÷ 3 = 3. Exponents: 5 − (−2) = 5 + 2 = 7. So {s(3, 7)}.", f"Coeficientes: 9 ÷ 3 = 3. Exponentes: 5 − (−2) = 5 + 2 = 7. Así que {s(3, 7)}.")},
      "p4": {"ok": "c", "hints": {"a": t("The value is right, but 0.5 is less than 1: adjust it.", "El valor es correcto, pero 0.5 es menor que 1: ajústelo."), "b": t("When the coefficient goes from 0.5 to 5, the exponent must go down 1.", "Al pasar el coeficiente de 0.5 a 5, el exponente tiene que bajar 1."), "d": t("You divided 8 ÷ 4. It is 4 ÷ 8, top divided by bottom.", "Dividió 8 ÷ 4. Es 4 ÷ 8, arriba entre abajo.")},
             "right": t(f"{s('0.5', '−2')} = {s(5, '−3')}.", f"{s('0.5', '−2')} = {s(5, '−3')}."), "solution": t(f"4 ÷ 8 = 0.5 and 3 − 5 = −2: {s('0.5', '−2')}. Adjust: 0.5 = {s(5, '−1')}, so {s(5, '−3')}.", f"4 ÷ 8 = 0.5 y 3 − 5 = −2: {s('0.5', '−2')}. Se ajusta: 0.5 = {s(5, '−1')}, así que {s(5, '−3')}.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("You multiplied the exponents. Add them.", "Multiplicó los exponentes. Se suman."), "b": t("You added the coefficients. Multiply them.", "Sumó los coeficientes. Se multiplican."), "c": t("You subtracted the exponents. Add them.", "Restó los exponentes. Se suman.")}, "solution": t(f"2 × 3 = 6; 3 + 4 = 7: {s(6, 7)}.", f"2 × 3 = 6; 3 + 4 = 7: {s(6, 7)}.")},
      "B": {"ok": "c", "hints": {"a": t("Add the exponents: 2 + 3 = 5, not 6.", "Sume los exponentes: 2 + 3 = 5, no 6."), "b": t("You added the coefficients. Multiply them.", "Sumó los coeficientes. Se multiplican."), "d": t("30 is not from 1 to 10.", "30 no está entre 1 y 10.")}, "solution": t(f"1.5 × 2 = 3; 2 + 3 = 5: {s(3, 5)}.", f"1.5 × 2 = 3; 2 + 3 = 5: {s(3, 5)}.")},
      "C": {"ok": "a", "hints": {"b": t("You multiplied the exponents. Add them: −2 + 5.", "Multiplicó los exponentes. Se suman: −2 + 5."), "c": t("You added the coefficients. Multiply them.", "Sumó los coeficientes. Se multiplican."), "d": t("Check the sign: −2 + 5 = 3.", "Revise el signo: −2 + 5 = 3.")}, "solution": t(f"3 × 3 = 9; −2 + 5 = 3: {s(9, 3)}.", f"3 × 3 = 9; −2 + 5 = 3: {s(9, 3)}.")},
      "D": {"ok": "d", "hints": {"a": t("Check the subtraction: 6 − 2.", "Revise la resta: 6 − 2."), "b": t("You subtracted the coefficients. Divide them.", "Restó los coeficientes. Se dividen."), "c": t("You added the exponents. When you divide, subtract them.", "Sumó los exponentes. Al dividir se restan.")}, "solution": t(f"8 ÷ 2 = 4; 6 − 2 = 4: {s(4, 4)}.", f"8 ÷ 2 = 4; 6 − 2 = 4: {s(4, 4)}.")},
      "E": {"ok": "a", "hints": {"b": t("Subtract top minus bottom: 4 − 7 = −3.", "Se resta arriba menos abajo: 4 − 7 = −3."), "c": t("You added the exponents. Subtract them.", "Sumó los exponentes. Se restan."), "d": t("Check: 4 − 7 = −3.", "Revise: 4 − 7 = −3.")}, "solution": t(f"6 ÷ 2 = 3; 4 − 7 = −3: {s(3, '−3')}.", f"6 ÷ 2 = 3; 4 − 7 = −3: {s(3, '−3')}.")},
      "F": {"ok": "c", "hints": {"a": t("−3 − 2 is not −1.", "−3 − 2 no es −1."), "b": t("Subtract: −3 − 2, not add.", "Se resta: −3 − 2, no se suma."), "d": t("Check: −3 − 2 = −5.", "Revise: −3 − 2 = −5.")}, "solution": t(f"5 ÷ 5 = 1; −3 − 2 = −5: {s(1, '−5')}.", f"5 ÷ 5 = 1; −3 − 2 = −5: {s(1, '−5')}.")},
      "G": {"ok": "d", "hints": {"a": t("24 is not from 1 to 10.", "24 no está entre 1 y 10."), "b": t("When the coefficient goes from 24 to 2.4, the exponent goes up, not down.", "Al pasar de 24 a 2.4, el exponente sube, no baja."), "c": t("0.24 is less than 1.", "0.24 es menor que 1.")}, "solution": t(f"24 = {s('2.4', 1)}, so {s(24, 5)} = {s('2.4', 6)}.", f"24 = {s('2.4', 1)}, así que {s(24, 5)} = {s('2.4', 6)}.")},
      "H": {"ok": "b", "hints": {"a": t("0.5 is less than 1.", "0.5 es menor que 1."), "c": t("When the coefficient goes from 0.5 to 5, the exponent goes down, not up.", "Al pasar de 0.5 a 5, el exponente baja, no sube."), "d": t("50 is not from 1 to 10.", "50 no está entre 1 y 10.")}, "solution": t(f"0.5 = {s(5, '−1')}, so {s('0.5', 4)} = {s(5, 3)}.", f"0.5 = {s(5, '−1')}, así que {s('0.5', 4)} = {s(5, 3)}.")}
     }}

    quiz = [
     ("A", f"({s(2, 3)})({s(3, 4)}) =", [("a", s(6, 12)), ("b", s(5, 7)), ("c", s(6, 1)), ("d", s(6, 7))]),
     ("B", f"({s('1.5', 2)})({s(2, 3)}) =", [("a", s(3, 6)), ("b", s("3.5", 5)), ("c", s(3, 5)), ("d", s(30, 5))]),
     ("C", f"({s(3, '−2')})({s(3, 5)}) =", [("a", s(9, 3)), ("b", s(9, "−10")), ("c", s(6, 3)), ("d", s(9, 7))]),
     ("D", f"({s(8, 6)}) ÷ ({s(2, 2)}) =", [("a", s(4, 3)), ("b", s(6, 4)), ("c", s(4, 8)), ("d", s(4, 4))]),
     ("E", f"({s(6, 4)}) ÷ ({s(2, 7)}) =", [("a", s(3, "−3")), ("b", s(3, 3)), ("c", s(3, 11)), ("d", s(3, "−11"))]),
     ("F", f"({s(5, '−3')}) ÷ ({s(5, 2)}) =", [("a", s(1, "−1")), ("b", s(1, 5)), ("c", s(1, "−5")), ("d", s(1, "−6"))]),
     ("G", t(f"A product came out as {s(24, 5)}. What is the valid scientific notation?", f"Un producto dio {s(24, 5)}. ¿Cuál es la notación científica válida?"), [("a", s(24, 5)), ("b", s("2.4", 4)), ("c", s("0.24", 7)), ("d", s("2.4", 6))]),
     ("H", t(f"A quotient came out as {s('0.5', 4)}. What is the valid scientific notation?", f"Un cociente dio {s('0.5', 4)}. ¿Cuál es la notación científica válida?"), [("a", s("0.5", 4)), ("b", s(5, 3)), ("c", s(5, 5)), ("d", s(50, 2))])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("The coefficients with ordinary arithmetic, the powers of 10 with the rules of exponents, and a final adjustment.", "Los coeficientes con aritmética común, las potencias de 10 con las reglas de los exponentes y un ajuste final."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Multiply</strong> numbers in scientific notation in three steps.", "<strong>Multiplicar</strong> números en notación científica en tres pasos."),
         t("<strong>Divide</strong> numbers in scientific notation in three steps.", "<strong>Dividir</strong> números en notación científica en tres pasos."),
         t("<strong>Adjust</strong> a coefficient that is 10 or more, or less than 1, and change the exponent to match.", "<strong>Ajustar</strong> un coeficiente que queda de 10 o más, o menor que 1, y compensar el exponente."),
         t("<strong>Solve</strong> science problems and check them on the calculator.", "<strong>Resolver</strong> problemas de ciencia y comprobarlos con la calculadora.")],
        secciones,
        (t("Do four multiplications in scientific notation (at least one that needs adjusting), four divisions (at least one with a coefficient less than 1), and two science problems with the answer in valid scientific notation. The coefficient is multiplied or divided like any decimal; what you need to make automatic is adding and subtracting the exponents.",
           "Haga cuatro multiplicaciones en notación científica (al menos una que necesite ajuste), cuatro divisiones (al menos una con coeficiente menor que 1) y dos problemas de ciencia con el resultado en notación científica válida. El coeficiente se multiplica o se divide como cualquier decimal; lo que hay que automatizar es sumar y restar los exponentes."),
         t("The U.S. population is about 3.4 × 10<sup>8</sup> people. If each person uses about 8 × 10<sup>1</sup> gallons of water a day, how many gallons does the country use in a day? Solve it in scientific notation and check it on the calculator.",
           "La población de los Estados Unidos es de unas 3.4 × 10<sup>8</sup> personas. Si cada persona usa unos 8 × 10<sup>1</sup> galones de agua al día, ¿cuántos galones usa el país en un día? Resuélvalo en notación científica y compruébelo en la calculadora.")),
        quiz,
        t("Self-check checklist for multiplying and dividing in scientific notation", "Lista de autoevaluación de la multiplicación y la división en notación científica"),
        t("Self-check checklist: skills for multiplying and dividing in scientific notation", "Lista de autoevaluación: destrezas de la multiplicación y la división en notación científica"),
        [(t("Working with the coefficients", "Operar los coeficientes"), t("I multiply or divide them correctly and keep them apart from the powers of 10.", "Los multiplico o divido bien y los mantengo separados de las potencias de 10."), t("I work with them, with a few mistakes.", "Los opero, con algunos errores."), t("I mix up the coefficients and the powers of 10.", "Mezclo los coeficientes con las potencias de 10.")),
         (t("The rules for the powers of 10", "Las reglas en las potencias de 10"), t("I add when I multiply and subtract when I divide, and I get the sign right.", "Sumo al multiplicar y resto al dividir, y acierto el signo."), t("I add or subtract, with sign mistakes.", "Sumo o resto, con errores de signo."), t("I do not use the product and quotient rules.", "No aplico las reglas del producto y del cociente.")),
         (t("Adjusting to valid form", "Ajustar a la forma válida"), t("I adjust the coefficient and explain how the exponent changes.", "Ajusto el coeficiente y explico cómo cambia el exponente."), t("I see it needs adjusting, but I move the exponent the wrong way.", "Veo que hay que ajustar, pero muevo mal el exponente."), t("I leave answers like 20 × 10<sup>5</sup> or 0.5 × 10<sup>−3</sup>.", "Dejo resultados como 20 × 10<sup>5</sup> o 0.5 × 10<sup>−3</sup>."))],
        t("<p>You learned to multiply and divide in scientific notation: work the <strong>coefficients</strong> with ordinary arithmetic, <strong>add or subtract the exponents</strong> of 10, and <strong>adjust</strong> the coefficient so it stays from 1 to 10.</p>\n<p>In <strong>Lesson 2.3 · Adding, subtracting, and using scientific notation</strong> you will add and subtract, where the exponents must be made equal first, and you will solve mixed science and technology problems.</p>",
          "<p>Aprendió a multiplicar y dividir en notación científica: se operan los <strong>coeficientes</strong> con aritmética común, se <strong>suman o restan los exponentes</strong> de 10 y se <strong>ajusta</strong> el coeficiente para que quede entre 1 y 10.</p>\n<p>En la <strong>Lección 2.3 · Suma, resta y aplicaciones en ciencia y tecnología</strong> sumará y restará, donde primero hay que igualar los exponentes, y resolverá problemas mezclados de ciencia y tecnología.</p>"),
        ("2-3", ("", t("Lesson 2.3 · Adding, subtracting, and using scientific notation", "Lección 2.3 · Suma, resta y aplicaciones en ciencia y tecnología"))),
        [(t("adjust", "ajustar"), t("Rewrite a coefficient that is 10 or more, or less than 1, so it is from 1 to 10, changing the exponent to keep the same value.", "Reescribir un coeficiente de 10 o más, o menor que 1, para que quede entre 1 y 10, cambiando el exponente para conservar el valor.")),
         (t("product rule", "regla del producto"), t("10<sup>m</sup> × 10<sup>n</sup> = 10<sup>m+n</sup>: the exponents are added.", "10<sup>m</sup> × 10<sup>n</sup> = 10<sup>m+n</sup>: los exponentes se suman.")),
         (t("quotient rule", "regla del cociente"), t("10<sup>m</sup> ÷ 10<sup>n</sup> = 10<sup>m−n</sup>: the exponents are subtracted.", "10<sup>m</sup> ÷ 10<sup>n</sup> = 10<sup>m−n</sup>: los exponentes se restan.")),
         (t("×10<sup>n</sup> key", "tecla ×10<sup>n</sup>"), t("The calculator key that types the power of 10 of a number in scientific notation. Some books call it EE.", "La tecla de la calculadora que escribe la potencia de 10 de un número en notación científica. Algunos libros la llaman EE."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ============ MODULES 1 and 3 · the three-step calculator (× and ÷) ============ */
function creaCalculadora(pre, divide_, ejemplos, genEjemplo){
  var C = {pasos: [], visto: 0, cola: ejemplos.slice()};
  function lee(){
    var a = $(pre + "-a").value.trim(), b = $(pre + "-b").value.trim(), m = $(pre + "-m").value.trim().replace(/[−–]/g, "-"), n = $(pre + "-n").value.trim().replace(/[−–]/g, "-"), av = $(pre + "-aviso");
    if (!leeNumero(a) || !leeNumero(b) || !/^-?\d{1,2}$/.test(m) || !/^-?\d{1,2}$/.test(n)){ av.className = "caja-aviso visible"; av.textContent = T("Type the coefficients with a decimal point and the exponents as whole numbers (from −99 to 99).", "Escriba los coeficientes con punto decimal y los exponentes como números enteros (entre −99 y 99)."); return null; }
    if (!esValida(a) || !esValida(b)){ av.className = "caja-aviso visible"; av.textContent = T("Each number must be in scientific notation: its coefficient must be at least 1 and less than 10.", "Cada número tiene que estar en notación científica: su coeficiente debe ser mayor o igual que 1 y menor que 10."); return null; }
    av.className = "caja-aviso"; av.textContent = "";
    return {a: plano(leeNumero(a)), b: plano(leeNumero(b)), m: parseInt(m, 10), n: parseInt(n, 10)};
  }
  function prepara(){
    var d = lee(); C.pasos = []; C.visto = 0; $(pre + "-pasos").innerHTML = "";
    if (!d){ $(pre + "-expr").innerHTML = ""; boton(); return; }
    var A = leeNumero(d.a), Bn = leeNumero(d.b), p, exacta = true, sm, so;
    if (divide_){ var r = divide(A, Bn); p = r.n; exacta = r.exacta; sm = d.m - d.n; so = " ÷ "; } else { p = mul(A, Bn); sm = d.m + d.n; so = " × "; }
    var pc = plano(p), ap = exacta ? " = " : " ≈ ";
    var expr = divide_ ? "(" + sciHTML(d.a, d.m) + ") ÷ (" + sciHTML(d.b, d.n) + ")" : "(" + sciHTML(d.a, d.m) + ")(" + sciHTML(d.b, d.n) + ")";
    $(pre + "-expr").innerHTML = expr;
    C.pasos.push("<strong>" + T("Coefficients:", "Coeficientes:") + "</strong> " + d.a + so + d.b + ap + pc + ".");
    C.pasos.push("<strong>" + T("Powers of 10:", "Potencias de 10:") + "</strong> " + (divide_ ? T("subtract", "se restan") : T("add", "se suman")) + T(" the exponents, ", " los exponentes, ") + expTexto(d.m) + (divide_ ? " − " : " + ") + par(d.n) + " = " + expTexto(sm) + T(". Partial answer: ", ". Resultado parcial: ") + sciHTML(pc, sm) + ".");
    var j = exponenteSci(p), fin = porPot(p, sm);
    if (j === 0) C.pasos.push("<strong>" + T("Adjust:", "Ajustar:") + "</strong> " + T("the coefficient " + pc + " is already from 1 to 10, so no adjustment is needed.", "el coeficiente " + pc + " ya está entre 1 y 10, así que no hace falta ajustar."));
    else C.pasos.push("<strong>" + T("Adjust:", "Ajustar:") + "</strong> " + pc + (j > 0 ? T(" is 10 or more. ", " es 10 o más. ") : T(" is less than 1. ", " es menor que 1. ")) + T("Rewrite ", "Se reescribe ") + pc + " = " + sciHTML(coefCon(p, j), j) + T(", and add that exponent: ", ", y ese exponente se suma: ") + expTexto(sm) + " + " + par(j) + " = " + expTexto(sm + j) + ".");
    C.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + expr + ap + numSciHTML(fin) + "</span>" + (exacta ? "" : ' <span class="nota">' + T("(rounded to four significant digits)", "(redondeado a cuatro cifras significativas)") + "</span>"));
    boton();
  }
  function pinta(){
    $(pre + "-pasos").innerHTML = C.pasos.slice(0, C.visto).map(function(x, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i < 3 ? i + 1 : "✓") + "</span>" + x + "</div>"; }).join("");
    boton();
  }
  function boton(){
    var b = $(pre + "-sig"); b.disabled = !C.pasos.length || C.visto >= C.pasos.length;
    b.textContent = C.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (C.visto >= C.pasos.length ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
    $(pre + "-todo").disabled = b.disabled;
  }
  $(pre + "-sig").addEventListener("click", function(){ if (C.visto < C.pasos.length){ C.visto++; pinta(); } });
  $(pre + "-todo").addEventListener("click", function(){ C.visto = C.pasos.length; pinta(); });
  $(pre + "-azar").addEventListener("click", function(){ var e = C.cola.length ? C.cola.shift() : genEjemplo(); $(pre + "-a").value = e[0]; $(pre + "-m").value = expTexto(e[1]); $(pre + "-b").value = e[2]; $(pre + "-n").value = expTexto(e[3]); prepara(); });
  ["-a", "-m", "-b", "-n"].forEach(function(x){ $(pre + x).addEventListener("input", prepara); });
  prepara();
}
function parMultiplicar(){
  var a = coefAzar(aleatorio(1, 2)), b = coefAzar(aleatorio(1, 2));
  while (a === "1") a = coefAzar(aleatorio(1, 2));
  while (b === "1") b = coefAzar(aleatorio(1, 2));
  while (abs(mul(leeNumero(a), leeNumero(b)).m).toString().length > 3) b = coefAzar(1);
  return [a, aleatorio(-6, 9), b, aleatorio(-6, 9)];
}
var DIVISORES = ["2", "4", "5", "8", "2.5", "1.6", "3", "6", "1.5", "1.2"];
function parDividir(ajuste){
  if (ajuste === undefined) ajuste = Math.random() < 0.5;
  for (var i = 0; i < 200; i++){
    var b = elige(DIVISORES), q = ajuste ? plano(sci(coefAzar(aleatorio(1, 2)), -1)) : coefAzar(aleatorio(1, 2)), a = mul(leeNumero(q), leeNumero(b));
    if (esValida(plano(a)) && abs(a.m).toString().length <= 3) return [plano(a), aleatorio(-6, 9), b, aleatorio(-6, 9)];
  }
  return ["3", 4, "6", 7];
}
function genMultiplicar(){
  var pp = parMultiplicar(), a = pp[0], m = pp[1], b = pp[2], n = pp[3], p = mul(leeNumero(a), leeNumero(b)), j = exponenteSci(p), res = porPot(p, m + n), rs = aSci(res);
  var o = [opNum(res)], pc = {};
  var x1 = op(rs.c, m * n + j); o.push(x1); pc[x1.clave] = T("With powers of 10, the exponents are added, not multiplied.", "En el producto de potencias de 10 los exponentes se suman, no se multiplican.");
  var x2 = opNum(porPot(suma(leeNumero(a), leeNumero(b)), m + n)); o.push(x2); pc[x2.clave] = T("The coefficients are multiplied, not added.", "Los coeficientes se multiplican, no se suman.");
  if (j > 0){
    var x3 = op(plano(p), m + n); o.push(x3); pc[x3.clave] = T("That value is right, but the coefficient is not from 1 to 10: it still needs adjusting.", "Ese valor es correcto, pero el coeficiente no está entre 1 y 10: falta ajustar.");
    var x4 = op(rs.c, m + n); o.push(x4); pc[x4.clave] = T("When the coefficient is put in valid form, the exponent must go up too.", "Al pasar el coeficiente a la forma válida, el exponente también tiene que subir.");
  }
  o.push(op(rs.c, rs.e + 1));
  return {enun: T("Find ", "Calcule ") + "(" + sciHTML(a, m) + ")(" + sciHTML(b, n) + ").", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("Coefficients: ", "Coeficientes: ") + a + " × " + b + " = " + plano(p) + T(". Exponents: ", ". Exponentes: ") + expTexto(m) + " + " + par(n) + " = " + expTexto(m + n) + "." + (j > 0 ? T(" Since " + plano(p) + " is 10 or more, it is adjusted and the exponent goes up to " + expTexto(rs.e) + ".", " Como " + plano(p) + " es 10 o más, se ajusta y el exponente sube a " + expTexto(rs.e) + ".") : ""),
    mal: T("Coefficients: ", "Coeficientes: ") + a + " × " + b + " = " + plano(p) + T(". Exponents: ", ". Exponentes: ") + expTexto(m) + " + " + par(n) + " = " + expTexto(m + n) + ". " + T("The answer is ", "La respuesta es ") + numSciHTML(res) + "."};
}

/* ============ MODULE 2 · the adjuster ============ */
var AJ = {c: null, k: 0, s: 0, cola: [["20", 5], ["0.5", -3]]};
var MALOS = ["20", "45", "345", "12.5", "60", "0.5", "0.04", "0.25", "0.8", "250", "0.075", "18"];
function cargaAJ(x){ AJ.c = leeNumero(x[0]); AJ.k = x[1]; AJ.s = 0; pintaAJ(); }
function pintaAJ(){
  var act = porPot(AJ.c, -AJ.s), ca = plano(act), ex = AJ.k + AJ.s, ok = esValida(ca), as = Math.abs(AJ.s), msg;
  var linea = '<span class="grande">' + sciHTML(plano(AJ.c), AJ.k) + (AJ.s ? " = " + sciHTML(ca, ex) : "") + "</span>";
  if (AJ.s === 0) msg = T("The coefficient " + plano(AJ.c) + (compara(AJ.c, N(10)) >= 0 ? " is 10 or more." : " is less than 1.") + " Which way must the point go?", "El coeficiente " + plano(AJ.c) + (compara(AJ.c, N(10)) >= 0 ? " es 10 o más." : " es menor que 1.") + " ¿Hacia dónde tiene que ir el punto?");
  else if (ok) msg = T("✓ Valid scientific notation. The point moved " + as + lugares(as) + (AJ.s > 0 ? " to the left and the exponent went up " : " to the right and the exponent went down ") + as + ".", "✓ Notación científica válida. El punto se movió " + as + lugares(as) + (AJ.s > 0 ? " a la izquierda y el exponente subió " : " a la derecha y el exponente bajó ") + as + ".");
  else if (compara(act, N(10)) >= 0) msg = T("The coefficient " + ca + " is 10 or more: the point must go to the left.", "El coeficiente " + ca + " es 10 o más: el punto tiene que ir a la izquierda.");
  else msg = T("The coefficient " + ca + " is less than 1: the point must go to the right.", "El coeficiente " + ca + " es menor que 1: el punto tiene que ir a la derecha.");
  $("aj-estado").innerHTML = linea + "<br>" + msg;
  $("aj-izq").disabled = ok || AJ.s >= 6; $("aj-der").disabled = ok || AJ.s <= -6;
}
function genAjuste(){
  var c = elige(MALOS), k = aleatorio(-8, 9), resp = porPot(leeNumero(c), k), j = exponenteSci(leeNumero(c)), rs = aSci(resp), aj = Math.abs(j);
  return {enun: T("Write ", "Escriba ") + sciHTML(c, k) + T(" in valid scientific notation.", " en notación científica válida."), resp: resp,
    explica: T("The point of the coefficient moves " + aj + lugares(aj) + (j > 0 ? " to the left, so the exponent goes up " : " to the right, so the exponent goes down ") + aj + ": ", "El punto del coeficiente se mueve " + aj + lugares(aj) + (j > 0 ? " a la izquierda, así que el exponente sube " : " a la derecha, así que el exponente baja ") + aj + ": ") + expTexto(k) + (j > 0 ? " + " : " − ") + aj + " = " + expTexto(rs.e) + ".",
    diagnostico: function(v, cc, kk){
      if (igual(cc, leeNumero(rs.c)) && kk === k - j) return T("The coefficient is right, but the exponent moved the wrong way: if the coefficient gets smaller, the exponent goes up, and the other way around.", "El coeficiente está bien, pero el exponente se movió al revés: si el coeficiente se achica, el exponente sube, y al contrario.");
      if (igual(cc, leeNumero(rs.c)) && kk === k) return T("The coefficient is right, but the exponent still has to make up for it.", "El coeficiente está bien, pero falta compensar el exponente.");
      return null; }};
}

/* ============ MODULE 3 · dividing ============ */
function genDividir(){
  var pp = parDividir(), a = pp[0], m = pp[1], b = pp[2], n = pp[3], q = divide(leeNumero(a), leeNumero(b)).n, j = exponenteSci(q), res = porPot(q, m - n), rs = aSci(res);
  var o = [opNum(res)], pc = {};
  var x1 = op(rs.c, m + n + j); o.push(x1); pc[x1.clave] = T("When you divide, the exponents are subtracted, not added.", "En la división los exponentes se restan, no se suman.");
  var x2 = op(rs.c, n - m + j); o.push(x2); pc[x2.clave] = T("Subtract in order: the exponent on top minus the exponent on the bottom.", "La resta va en orden: exponente del numerador menos exponente del denominador.");
  if (j < 0){
    var x3 = op(plano(q), m - n); o.push(x3); pc[x3.clave] = T("That value is right, but " + plano(q) + " is less than 1: it still needs adjusting.", "Ese valor es correcto, pero " + plano(q) + " es menor que 1: falta ajustar.");
    var x4 = op(rs.c, m - n); o.push(x4); pc[x4.clave] = T("When the coefficient is put in valid form, the exponent must go down too.", "Al pasar el coeficiente a la forma válida, el exponente también tiene que bajar.");
  }
  o.push(op(rs.c, rs.e - 1));
  var expl = T("Coefficients: ", "Coeficientes: ") + a + " ÷ " + b + " = " + plano(q) + T(". Exponents: ", ". Exponentes: ") + expTexto(m) + " − " + par(n) + " = " + expTexto(m - n) + "." + (j < 0 ? T(" Since " + plano(q) + " is less than 1, it is adjusted and the exponent goes down to " + expTexto(rs.e) + ".", " Como " + plano(q) + " es menor que 1, se ajusta y el exponente baja a " + expTexto(rs.e) + ".") : "");
  return {enun: T("Find ", "Calcule ") + "(" + sciHTML(a, m) + ") ÷ (" + sciHTML(b, n) + ").", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: expl, mal: expl + " " + T("The answer is ", "La respuesta es ") + numSciHTML(res) + "."};
}

/* ============ MODULE 4 · word problems ============ */
function genReal(){
  var t = aleatorio(1, 5), c, k;
  if (t === 1){
    c = coefAzar(aleatorio(1, 2)); k = aleatorio(1, 4);
    return {operacion: "×", resp: mul(sci("3", 5), sci(c, k)), porQueOp: T("distance is speed times time: multiply.", "la distancia es velocidad por tiempo: se multiplica."),
      enun: T("Light travels ", "La luz viaja a ") + sciHTML("3", 5) + T(" kilometers per second. How far does it go in ", " kilómetros por segundo. ¿Qué distancia recorre en ") + sciHTML(c, k) + T(" seconds? Give the answer in kilometers.", " segundos? Dé la respuesta en kilómetros."),
      explica: T("Distance = speed × time: (", "Distancia = velocidad × tiempo: (") + sciHTML("3", 5) + ")(" + sciHTML(c, k) + ") km."};
  }
  if (t === 2){
    var d = sci(coefAzar(1), aleatorio(1, 3)), ar = sci(coefAzar(aleatorio(1, 2)), aleatorio(2, 5)), P = mul(d, ar);
    return {operacion: "÷", resp: d, porQueOp: T("“per square mile” asks you to share the population over the area: divide.", "«por milla cuadrada» pide repartir la población entre el área: se divide."),
      enun: T("A region has ", "Una región tiene ") + numSciHTML(P) + T(" people and an area of ", " habitantes y un área de ") + numSciHTML(ar) + T(" square miles. On average, how many people live in each square mile?", " millas cuadradas. ¿Cuántos habitantes hay, en promedio, por milla cuadrada?"),
      explica: T("Density = population ÷ area.", "Densidad = población ÷ área.")};
  }
  if (t === 3){
    var cn = sci(coefAzar(1), aleatorio(3, 7)), f = sci(coefAzar(1), aleatorio(3, 7)), D = mul(cn, f);
    return {operacion: "÷", resp: cn, porQueOp: T("“how many fit” shares the capacity over the size of each file: divide.", "«cuántos caben» reparte la capacidad entre el tamaño de cada archivo: se divide."),
      enun: T("A drive holds ", "Un disco guarda ") + numSciHTML(D) + T(" bytes, and each file takes up ", " bytes y cada archivo ocupa ") + numSciHTML(f) + T(" bytes. How many files fit on the drive?", " bytes. ¿Cuántos archivos caben en el disco?"),
      explica: T("Number of files = capacity ÷ size of each file.", "Cantidad de archivos = capacidad ÷ tamaño de cada archivo.")};
  }
  if (t === 4){
    var lat = elige([["1", 5], ["1.1", 5], ["1.2", 5]]), dias = elige([["3", 1, T("30 days", "30 días")], ["3.65", 2, T("365 days, that is, one year", "365 días, es decir, un año")], ["7", 0, T("one week (7 days)", "una semana (7 días)")]]);
    return {operacion: "×", resp: mul(sci(lat[0], lat[1]), sci(dias[0], dias[1])), porQueOp: T("the same amount repeats every day: multiply.", "se repite la misma cantidad cada día: se multiplica."),
      enun: T("A human heart beats about ", "Un corazón humano late unas ") + sciHTML(lat[0], lat[1]) + T(" times a day. How many times does it beat in ", " veces al día. ¿Cuántas veces late en ") + dias[2] + T("? Write the answer in scientific notation.", "? Escriba el resultado en notación científica."),
      explica: T("Total beats = beats per day × number of days.", "Latidos totales = latidos por día × número de días.")};
  }
  var cel = sci(coefAzar(1), -aleatorio(4, 6)), nn = sci(coefAzar(1), aleatorio(2, 4)), L = mul(cel, nn);
  return {operacion: "÷", resp: nn, porQueOp: T("“how many fit” in a length: divide the total length by the width of one cell.", "«cuántas caben» en una longitud: se divide la longitud total entre el ancho de una célula."),
    enun: T("A cell is ", "Una célula mide ") + numSciHTML(cel) + T(" meters wide. How many cells, set in a row, cover ", " metros de ancho. ¿Cuántas células, puestas en fila, cubren ") + numSciHTML(L) + T(" meters?", " metros?"),
    explica: T("Number = total length ÷ width of one cell.", "Cantidad = longitud total ÷ ancho de una célula.")};
}

/* ============ Start ============ */
creaCalculadora("cm", false, [["5", 3, "4", 2]], parMultiplicar);
creaCalculadora("cd", true, [["8", 7, "2", 3]], function(){ return parDividir(); });
OMS("p1", genMultiplicar);
$("aj-izq").addEventListener("click", function(){ AJ.s++; pintaAJ(); });
$("aj-der").addEventListener("click", function(){ AJ.s--; pintaAJ(); });
$("aj-nuevo").addEventListener("click", function(){ cargaAJ(AJ.cola.length ? AJ.cola.shift() : [elige(MALOS), aleatorio(-8, 9)]); });
cargaAJ(AJ.cola.shift());
creaPracticaSci("p2", genAjuste);
OMS("p3", genDividir);
creaPracticaSci("p4", genReal);
'''

def calculadora(pre, etiquetas, valores):
    campos = "".join(f'<div class="campo"><label for="{pre}-{k}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{pre}-{k}" value="{v}"{" class=\"corto\"" if k in "mn" else ""}></div>' for k, et, v in zip("ambn", etiquetas, valores))
    return f'''      <div class="panel">
        <div class="campos">{campos}</div>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pre}-sig"></button>
          <button type="button" class="btn-sec" id="{pre}-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button>
          <button type="button" class="btn-sec" id="{pre}-azar">{t("Another example", "Otro ejemplo")}</button>
        </div>
      </div>
      <div class="caja-aviso" id="{pre}-aviso" role="alert"></div>
      <div class="fraccion-grande" id="{pre}-expr"></div>
      <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>'''

def lista_pasos(items):
    return '      <div class="pasos">' + "".join(f'<div class="paso"><span class="n" aria-hidden="true">{i + 1}</span>{x}</div>' for i, x in enumerate(items)) + "</div>"

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("multiply", "multiplicar"), t("Multiplying in three steps", "Multiplicar en tres pasos"),
      f'''      <p>{t("To multiply two numbers in scientific notation, the coefficients and the powers of 10 are worked <strong>separately</strong> and then put together:", "Para multiplicar dos números en notación científica, los coeficientes y las potencias de 10 se trabajan <strong>por separado</strong> y después se reúnen:")}</p>
{lista_pasos([t("<strong>Multiply the coefficients</strong>.", "Se <strong>multiplican los coeficientes</strong>."), t("<strong>Add the exponents</strong> of the powers of 10 (the product rule).", "Se <strong>suman los exponentes</strong> de las potencias de 10 (regla del producto)."), t("Check that the coefficient is from 1 to 10, and <strong>adjust</strong> it if needed.", "Se verifica que el coeficiente quede entre 1 y 10, y se <strong>ajusta</strong> si hace falta.")])}
      <h3>{t("Three-step calculator", "Calculadora de tres pasos")}</h3>
      <p>{t("Type two numbers in scientific notation, or ask for an example, and reveal the steps one at a time. Try to predict each step before you show it.", "Escriba dos números en notación científica, o pida un ejemplo, y revele los pasos uno por uno. Intente anticipar cada paso antes de mostrarlo.")}</p>
{calculadora("cm", [t("First coefficient", "Primer coeficiente"), t("First exponent", "Primer exponente"), t("Second coefficient", "Segundo coeficiente"), t("Second exponent", "Segundo exponente")], ["3", "4", "2", "5"])}
{B.om("p1", t("Practice: multiply", "Practique: multiplicar"))}'''),
     (t("adjust", "ajustar"), t("Adjusting the coefficient", "Ajustar el coeficiente"),
      f'''      <p>{t("When you multiply or divide, the coefficient can end up <strong>10 or more</strong> (like 20 × 10<sup>5</sup>) or <strong>less than 1</strong> (like 0.5 × 10<sup>−3</sup>). The value is right, but it is not yet valid scientific notation. To fix it, move the point of the coefficient and make up for it with the exponent.", "Al multiplicar o dividir, el coeficiente puede salir <strong>de 10 en adelante</strong> (como 20 × 10<sup>5</sup>) o <strong>menor que 1</strong> (como 0.5 × 10<sup>−3</sup>). El valor es correcto, pero todavía no es notación científica válida. Para arreglarlo se mueve el punto del coeficiente y se compensa con el exponente.")}</p>
      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("Adjusting (table you can scroll sideways)", "Ajuste (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("How the exponent makes up for adjusting the coefficient", "Cómo se compensa el exponente al ajustar el coeficiente")}</caption>
      <thead><tr><th scope="col">{t("If the coefficient…", "Si el coeficiente…")}</th><th scope="col">{t("The point moves", "El punto se mueve")}</th><th scope="col">{t("The exponent", "El exponente")}</th></tr></thead>
      <tbody><tr><td>{t("is 10 or more", "es 10 o más")}</td><td>{t("to the left", "a la izquierda")}</td><td>{t("goes up 1 for each place", "sube 1 por cada lugar")}</td></tr><tr><td>{t("is less than 1", "es menor que 1")}</td><td>{t("to the right", "a la derecha")}</td><td>{t("goes down 1 for each place", "baja 1 por cada lugar")}</td></tr></tbody></table></div>
      <h3>{t("The adjuster", "El ajustador")}</h3>
      <p>{t("Move the point of the coefficient and watch the exponent make up for each move.", "Mueva el punto del coeficiente y observe cómo el exponente compensa cada movimiento.")}</p>
      <div class="panel">
        <div class="estado" id="aj-estado" aria-live="polite"></div>
        <div class="fila-btn" style="justify-content:center;">
          <button type="button" class="btn" id="aj-izq">{t("← Point to the left", "← Punto a la izquierda")}</button>
          <button type="button" class="btn" id="aj-der">{t("Point to the right →", "Punto a la derecha →")}</button>
          <button type="button" class="btn-sec" id="aj-nuevo">{t("Another coefficient", "Otro coeficiente")}</button>
        </div>
      </div>
      <div class="caja-tip"><strong>{t("What one loses, the other gains:", "Lo que pierde uno lo gana el otro:")}</strong> {t("if the coefficient becomes 10 times smaller, the power of 10 becomes 10 times larger. That is why the value does not change when you adjust.", "si el coeficiente se hace 10 veces más pequeño, la potencia de 10 se hace 10 veces más grande. Por eso el valor del número no cambia al ajustar.")}</div>
{P.sci_input("p2", t("Practice: write it in valid scientific notation", "Practique: escríbalo en notación científica válida"))}'''),
     (t("divide", "dividir"), t("Dividing in scientific notation", "Dividir en notación científica"),
      f'''      <p>{t("Division follows the same logic with the opposite operations:", "La división sigue la misma lógica con las operaciones inversas:")}</p>
{lista_pasos([t("<strong>Divide the coefficients</strong>.", "Se <strong>dividen los coeficientes</strong>."), t("<strong>Subtract the exponents</strong>: the one on top minus the one on the bottom (the quotient rule).", "Se <strong>restan los exponentes</strong>: el del numerador menos el del denominador (regla del cociente)."), t("Check and <strong>adjust</strong> the coefficient. In division it often ends up less than 1.", "Se verifica y se <strong>ajusta</strong> el coeficiente. En la división suele quedar menor que 1.")])}
      <h3>{t("Three-step calculator for dividing", "Calculadora de tres pasos para dividir")}</h3>
      <p>{t("The first number is the dividend (on top) and the second is the divisor (on the bottom).", "El primer número es el dividendo (numerador) y el segundo, el divisor (denominador).")}</p>
{calculadora("cd", [t("Coefficient of the dividend", "Coeficiente del dividendo"), t("Exponent of the dividend", "Exponente del dividendo"), t("Coefficient of the divisor", "Coeficiente del divisor"), t("Exponent of the divisor", "Exponente del divisor")], ["3", "4", "6", "7"])}
{P.atencion(t("A common mistake:", "Error frecuente:"), t("leaving the answer as 0.5 × 10<sup>−3</sup>. The arithmetic is right, but it is not valid scientific notation until the coefficient is from 1 to 10: 5 × 10<sup>−4</sup>.", "dejar el resultado como 0.5 × 10<sup>−3</sup>. El cálculo está bien, pero no es notación científica válida hasta que el coeficiente quede entre 1 y 10: 5 × 10<sup>−4</sup>."))}
{B.om("p3", t("Practice: divide", "Practique: dividir"))}'''),
     (t("real", "real"), t("A real calculation", "Un cálculo real"),
      f'''      <p>{t("In a word problem, decide the operation first. A useful hint:", "En los problemas de contexto, lo primero es decidir la operación. Una pista útil:")}</p>
      <ul>
        <li>{t("<strong>Multiply</strong> when an amount repeats many times: speed times time, amount per day times number of days.", "<strong>Multiplicar</strong> cuando se repite una cantidad muchas veces: velocidad por tiempo, cantidad por día por número de días.")}</li>
        <li>{t("<strong>Divide</strong> when a total is shared out, or the question asks “how many fit” or “how much for each one.”", "<strong>Dividir</strong> cuando se reparte un total o se pregunta «cuántos caben» o «cuánto por cada uno».")}</li>
      </ul>
      <p>{t("Then use the three steps and write the answer in valid scientific notation, with its unit.", "Después se aplican los tres pasos y se escribe el resultado en notación científica válida, con su unidad.")}</p>
{P.sci_input("p4", t("Practice: science and technology problems", "Practique: problemas de ciencia y tecnología"), ops=[("×", t("Multiply", "Multiplicar")), ("÷", t("Divide", "Dividir"))])}
      <div class="caja-tip"><strong>{t("On the test:", "En el examen:")}</strong> {t("solve it by hand first and use the calculator to confirm. On the TI-30XS, scientific notation is typed with the ×10<sup>n</sup> key: 3 × 10<sup>5</sup> is typed as 3, that key, and 5.", "resuelva primero a mano y use la calculadora para confirmar. En la TI-30XS, la notación científica se escribe con la tecla ×10<sup>n</sup>: 3 × 10<sup>5</sup> se teclea como 3, esa tecla y 5.")} <button type="button" class="btn-calc" data-gph-calculadora>🧮 {t("Open the calculator", "Abrir la calculadora")}</button></div>''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_SCI, scripts=("/math/scinot.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Multiplicación y división en notación científica")
