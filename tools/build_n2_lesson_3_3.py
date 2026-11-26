"""Level 2 · Lesson 3.3 · PEMDAS with fractions and in algebra — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import fr

B.NIVEL = 2
N = "3-3"
TEMA = ("The full order of operations (PEMDAS)", "PEMDAS completo")
TIT = ("PEMDAS with fractions and in algebra", "PEMDAS en expresiones con fracciones y contexto algebraico")

def hl(x):
    return f'<mark style="background:#fff3e0;outline:2px solid #bf360c;border-radius:4px;padding:0 3px">{x}</mark>'
def S(x):
    """Valor sustituido, entre paréntesis y resaltado."""
    return f'<span style="color:#0d47a1;font-weight:700">({x})</span>'
def frx(a, b):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{a}</span><span class="fb2">{b}</span></span><span class="cap-oculto">({a}) ÷ ({b})</span>'
def P(a, b):
    """Fracción entre paréntesis."""
    return f"({fr(a, b)})"

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 3.2 you added powers, roots, and negative numbers to PEMDAS, and saw that the fraction bar groups. This lesson closes Topic 3 with two more steps: working with fractions inside PEMDAS, and going from numbers to <strong>letters</strong>, that is, substituting values into algebraic expressions. That is exactly what the GED asks every time it gives you a formula.",
"En la Lección 3.2 incorporó potencias, raíces y números negativos a PEMDAS, y vio que la barra de fracción agrupa. Esta lección cierra el Tema 3 con dos pasos más: operar con fracciones dentro de PEMDAS y pasar de los números a las <strong>letras</strong>, es decir, sustituir valores en expresiones algebraicas. Es exactamente lo que pide el GED cada vez que entrega una fórmula.")}</p>
<p>{t("Fractions do not change the order of operations. What changes is how you do each operation, which you studied in Topic 2: to add or subtract, find a common denominator; to multiply, multiply the numerators and the denominators; to divide, multiply by the reciprocal.",
"Las fracciones no cambian el orden de las operaciones. Lo que cambia es la manera de hacer cada operación, que ya estudió en el Tema 2: para sumar y restar se busca un denominador común; para multiplicar, numerador por numerador y denominador por denominador; para dividir, se multiplica por el recíproco.")}</p>
{ejemplo(t("Example:", "Ejemplo:") + f" {fr(1, 2)} + {fr(3, 4)} × {fr(2, 3)}",
  [("1", "MD.", t(f"Multiplication before addition: {hl(fr(3, 4) + ' × ' + fr(2, 3))} = {fr(6, 12)} = {fr(1, 2)}.", f"La multiplicación antes que la suma: {hl(fr(3, 4) + ' × ' + fr(2, 3))} = {fr(6, 12)} = {fr(1, 2)}.")),
   ("2", "AS.", f"{fr(1, 2)} + {fr(1, 2)} = {fr(2, 2)} = 1."),
   ("✓", t("Answer.", "Respuesta."), t(f"<strong>1</strong>. If you had added first, you would get {fr(5, 4)} × {fr(2, 3)} = {fr(5, 6)}, which is wrong.", f"<strong>1</strong>. Si hubiera sumado primero, obtendría {fr(5, 4)} × {fr(2, 3)} = {fr(5, 6)}, que es incorrecto."))])}
{ejemplo(t("Example:", "Ejemplo:") + f" {P(2, 3)}<sup>2</sup> − {fr(1, 9)} ÷ {fr(1, 3)}",
  [("1", "E.", f"{P(2, 3)}<sup>2</sup> = {fr('2 × 2', '3 × 3')} = {fr(4, 9)}."),
   ("2", "MD.", t(f"Divide by multiplying by the reciprocal: {fr(1, 9)} × {fr(3, 1)} = {fr(3, 9)}.", f"Se divide multiplicando por el recíproco: {fr(1, 9)} × {fr(3, 1)} = {fr(3, 9)}.")),
   ("3", "AS.", f"{fr(4, 9)} − {fr(3, 9)} = {fr(1, 9)}."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{fr(1, 9)}</strong>")])}
{caja("ojo", t("Watch the exponent", "Cuidado con el exponente"), t(f"<p>{P(2, 3)}<sup>2</sup> = {fr(4, 9)}, because the parentheses raise the whole fraction. But {fr('2<sup>2</sup>', 3)} = {fr(4, 3)}, because the exponent applies only to the 2. It is the same idea as (−5)<sup>2</sup> and −5<sup>2</sup>: the exponent reaches only what is right before it.</p>",
f"<p>{P(2, 3)}<sup>2</sup> = {fr(4, 9)}, porque el paréntesis eleva la fracción completa. En cambio, {fr('2<sup>2</sup>', 3)} = {fr(4, 3)}, porque el exponente solo afecta al 2. Es la misma idea de (−5)<sup>2</sup> frente a −5<sup>2</sup>: el exponente alcanza únicamente lo que tiene justo antes.</p>"))}
{ejemplo(t("Example with signs:", "Ejemplo con signos:") + " " + frx("12 − 2<sup>3</sup>", "1 − 3"),
  [("1", t("Numerator.", "Numerador."), t("E before S: 2<sup>3</sup> = 8, so 12 − 8 = 4.", "E antes que R: 2<sup>3</sup> = 8, así que 12 − 8 = 4.")),
   ("2", t("Denominator.", "Denominador."), "1 − 3 = −2."),
   ("✓", t("Divide.", "Divida."), t("4 ÷ (−2) = <strong>−2</strong> (different signs, negative).", "4 ÷ (−2) = <strong>−2</strong> (signos distintos, negativo)."))])}
{practica("p1", t("Practice 1 — Multiply first", "Práctica 1 — Primero se multiplica"), t(f"What is {fr(1, 3)} + {fr(2, 3)} × {fr(3, 4)}?", f"¿Cuánto es {fr(1, 3)} + {fr(2, 3)} × {fr(3, 4)}?"),
          [("a", fr(3, 4)), ("b", fr(5, 6)), ("c", "1"), ("d", fr(1, 2))])}
{practica("p2", t("Practice 2 — The power of a fraction", "Práctica 2 — La potencia de una fracción"), t(f"What is {P(3, 4)}<sup>2</sup> × 16?", f"¿Cuánto es {P(3, 4)}<sup>2</sup> × 16?"),
          [("a", "24"), ("b", "12"), ("c", "9"), ("d", "36")])}
{enlace(n, t("fractions", "fracciones"), t("PEMDAS with fractions", "PEMDAS con fracciones"), t("Solve expressions with fractions and type the answer in simplest form.", "Resuelva expresiones con fracciones y escriba el resultado simplificado."))}'''

    s2 = f'''<p>{t("A <strong>variable</strong> is a letter that takes the place of a number. To <strong>evaluate</strong> an algebraic expression, you replace each letter with its given value and calculate with PEMDAS. There are two golden rules.",
"Una <strong>variable</strong> es una letra que ocupa el lugar de un número. <strong>Evaluar</strong> una expresión algebraica quiere decir reemplazar cada letra por el valor indicado y calcular con PEMDAS. Hay dos reglas de oro.")}</p>
{caja("tip", t("Two golden rules", "Dos reglas de oro"), t("<p><strong>Rule 1 · Always substitute inside parentheses.</strong> If x = −2, write (−2) every place x appears. The parentheses protect the sign of the number.</p><p><strong>Rule 2 · A letter next to a number means multiplication.</strong> 3x means 3 × x; 2ab means 2 × a × b.</p>",
"<p><strong>Regla 1 · Sustituya siempre entre paréntesis.</strong> Si x = −2, escriba (−2) en cada lugar donde aparece x. El paréntesis protege el signo del número.</p><p><strong>Regla 2 · La letra pegada a un número indica multiplicación.</strong> 3x quiere decir 3 × x; 2ab quiere decir 2 × a × b.</p>"))}
{ejemplo(t("Example: evaluate 4x − 7 for x = 3", "Ejemplo: evalúe 4x − 7 para x = 3"),
  [("1", t("Substitute.", "Sustituya."), f"4{S(3)} − 7"),
   ("2", "MD.", "4 × 3 = 12 → 12 − 7."),
   ("✓", "AS.", "12 − 7 = <strong>5</strong>")])}
{ejemplo(t("Example: evaluate x<sup>2</sup> − 3x + 2 for x = −2", "Ejemplo: evalúe x<sup>2</sup> − 3x + 2 para x = −2"),
  [("1", t("Substitute.", "Sustituya."), f"{S('−2')}<sup>2</sup> − 3{S('−2')} + 2"),
   ("2", "E.", t("(−2)<sup>2</sup> = 4. Thanks to the parentheses, the sign is squared too → 4 − 3(−2) + 2.", "(−2)<sup>2</sup> = 4. Gracias al paréntesis, el signo también se eleva al cuadrado → 4 − 3(−2) + 2.")),
   ("3", "MD.", t("3 × (−2) = −6, and subtracting −6 is the same as adding 6 → 4 + 6 + 2.", "3 × (−2) = −6, y restar −6 es lo mismo que sumar 6 → 4 + 6 + 2.")),
   ("✓", "AS.", "4 + 6 + 2 = <strong>12</strong>")])}
{caja("ojo", t("The most common GED mistake", "El error más frecuente del GED"), t(f"<p>Evaluate −x<sup>2</sup> for x = −3. The exponent applies only to the x, so you calculate −{S('−3')}<sup>2</sup> = −(9) = <strong>−9</strong>, not 9. First raise the value you substituted; then apply the sign that was in front.</p>",
f"<p>Evaluar −x<sup>2</sup> para x = −3. Como el exponente solo afecta a la x, se calcula −{S('−3')}<sup>2</sup> = −(9) = <strong>−9</strong>, no 9. Primero se eleva el valor sustituido; después se aplica el signo que estaba delante.</p>"))}
{ejemplo(t("Example: evaluate", "Ejemplo: evalúe") + " " + frx("a + b", "a − b") + " " + t("for a = 5 and b = −3", "para a = 5 y b = −3"),
  [("1", t("Substitute.", "Sustituya."), frx(f"{S(5)} + {S('−3')}", f"{S(5)} − {S('−3')}")),
   ("2", t("Numerator and denominator.", "Numerador y denominador."), t("5 + (−3) = 2. 5 − (−3) = 5 + 3 = 8.", "5 + (−3) = 2. 5 − (−3) = 5 + 3 = 8.")),
   ("✓", t("Divide and simplify.", "Divida y simplifique."), f"{fr(2, 8)} = <strong>{fr(1, 4)}</strong>")])}
{ejemplo(t("Example with a fraction: evaluate 2x + ", "Ejemplo con fracción: evalúe 2x + ") + fr(1, 2) + t(" for x = ", " para x = ") + fr(3, 4),
  [("1", t("Substitute.", "Sustituya."), f"2{S(fr(3, 4))} + {fr(1, 2)}"),
   ("2", "MD.", f"2 × {fr(3, 4)} = {fr(6, 4)} = {fr(3, 2)}."),
   ("✓", "AS.", f"{fr(3, 2)} + {fr(1, 2)} = {fr(4, 2)} = <strong>2</strong>")])}
{practica("p3", t("Practice 3 — A negative value", "Práctica 3 — Un valor negativo"), t("Evaluate 3x + 4 for x = −5.", "Evalúe 3x + 4 para x = −5."),
          [("a", "19"), ("b", "−11"), ("c", "−19"), ("d", "2")])}
{practica("p4", t("Practice 4 — A square", "Práctica 4 — Un cuadrado"), t("Evaluate x<sup>2</sup> + 2x for x = −3.", "Evalúe x<sup>2</sup> + 2x para x = −3."),
          [("a", "15"), ("b", "−15"), ("c", "−3"), ("d", "3")])}
{practica("p5", t("Practice 5 — Two variables", "Práctica 5 — Dos variables"), t("Evaluate 2(a − b)<sup>2</sup> for a = 1 and b = 4.", "Evalúe 2(a − b)<sup>2</sup> para a = 1 y b = 4."),
          [("a", "36"), ("b", "−18"), ("c", "18"), ("d", "−12")])}
{enlace(n, t("substitute", "sustituir"), t("substituting and evaluating", "sustituir y evaluar"), t("Replace each letter with its value in parentheses, see the PEMDAS steps, and then practice.", "Cambie cada letra por su valor entre paréntesis, vea los pasos de PEMDAS y después practique."))}'''

    s3 = f'''<p>{t("The GED Math test gives you a <strong>formula sheet</strong>. You do not have to memorize anything: you have to know which value goes with each letter, substitute, and apply PEMDAS. It is the same skill as in the last section, with words around it.",
"El examen GED de Matemáticas entrega una <strong>hoja de fórmulas</strong>. No hay que memorizar nada: hay que saber qué valor corresponde a cada letra, sustituir y aplicar PEMDAS. Es la misma destreza de la sección anterior, con palabras alrededor.")}</p>
{ejemplo(t("Example · Temperature", "Ejemplo · Temperatura") + '<span style="display:block;font-weight:400;margin-top:6px">' + t(f"The formula F = {fr(9, 5)}C + 32 changes degrees Celsius to degrees Fahrenheit. How many degrees Fahrenheit is 25 °C?", f"La fórmula F = {fr(9, 5)}C + 32 convierte grados Celsius en grados Fahrenheit. ¿Cuántos grados Fahrenheit son 25 °C?") + '</span>',
  [   ("1", t("Substitute.", "Sustituya."), f"F = {fr(9, 5)}{S(25)} + 32"),
   ("2", "MD.", f"{fr(9, 5)} × 25 = {fr(225, 5)} = 45."),
   ("3", "AS.", "45 + 32 = 77."),
   ("✓", t("Answer.", "Respuesta."), "<strong>77 °F</strong>")])}
{ejemplo(t("Example · Area of a trapezoid", "Ejemplo · Área de un trapecio") + '<span style="display:block;font-weight:400;margin-top:6px">' + t(f"The area of a trapezoid is A = {fr(1, 2)}(b<sub>1</sub> + b<sub>2</sub>)h. Find the area if b<sub>1</sub> = 6 feet, b<sub>2</sub> = 10 feet, and h = 5 feet.", f"El área de un trapecio es A = {fr(1, 2)}(b<sub>1</sub> + b<sub>2</sub>)h. Calcule el área si b<sub>1</sub> = 6 pies, b<sub>2</sub> = 10 pies y h = 5 pies.") + '</span>',
  [   ("1", t("Substitute.", "Sustituya."), f"A = {fr(1, 2)}({S(6)} + {S(10)}){S(5)}"),
   ("2", "P.", "6 + 10 = 16."),
   ("3", "MD.", t(f"From left to right: {fr(1, 2)} × 16 = 8; 8 × 5 = 40.", f"De izquierda a derecha: {fr(1, 2)} × 16 = 8; 8 × 5 = 40.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>40 square feet</strong>", "<strong>40 pies cuadrados</strong>"))])}
{ejemplo(t("Example · Simple interest", "Ejemplo · Interés simple") + '<span style="display:block;font-weight:400;margin-top:6px">' + t("The simple interest formula is I = Prt. How much interest do $1,200 earn at a yearly rate of 5% for 3 years?", "La fórmula del interés simple es I = Prt. ¿Cuánto interés producen $1,200 a una tasa anual del 5% durante 3 años?") + '</span>',
  [   ("1", t("The values.", "Los valores."), t("P = 1,200; r = 5% = 0.05; t = 3.", "P = 1,200; r = 5% = 0.05; t = 3.")),
   ("2", "MD.", "1,200 × 0.05 = 60; 60 × 3 = 180."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>$180</strong>. You will study this formula in depth in Lesson 6.1.", "<strong>$180</strong>. Esta fórmula se estudiará a fondo en la Lección 6.1."))])}
{caja("tip", t("A strategy for formula problems", "Estrategia para problemas con fórmula"), t("<ol><li>Write the formula.</li><li>Write the value of each letter under it.</li><li>Substitute inside parentheses.</li><li>Apply PEMDAS.</li><li>Answer with the right unit, and ask yourself if the answer makes sense.</li></ol>",
"<ol><li>Escriba la fórmula.</li><li>Anote debajo el valor de cada letra.</li><li>Sustituya entre paréntesis.</li><li>Aplique PEMDAS.</li><li>Responda con la unidad correcta y pregúntese si el resultado tiene sentido.</li></ol>"))}
{calc(t("Formulas on the calculator", "Fórmulas en la calculadora"), t(f"""<p>For F = {fr(9, 5)}C + 32 with C = 25, type {T("9")} {T("÷")} {T("5")} {T("×")} {T("25")} {T("+")} {T("32")} {T("enter")}. The screen shows 77. If C is negative, type it in parentheses with the {T("(−)")} key.</p>""",
f"""<p>Para F = {fr(9, 5)}C + 32 con C = 25, escriba {T("9")} {T("÷")} {T("5")} {T("×")} {T("25")} {T("+")} {T("32")} {T("enter")}. La pantalla muestra 77. Si C es negativo, escríbalo entre paréntesis con la tecla {T("(−)")}.</p>"""))}
{practica("p6", t("Practice 6 — A taxi ride", "Práctica 6 — Un viaje en taxi"), t("A taxi charges by the formula C = 3.50 + 2.25m, where m is the number of miles. How much does an 8-mile ride cost?", "Un taxi cobra según la fórmula C = 3.50 + 2.25m, donde m es el número de millas. ¿Cuánto cuesta un viaje de 8 millas?"),
          [("a", "$46.00"), ("b", "$13.75"), ("c", "$21.50"), ("d", "$18.00")])}
{practica("p7", t("Practice 7 — From Fahrenheit to Celsius", "Práctica 7 — De Fahrenheit a Celsius"), t(f"The formula C = {fr(5, 9)}(F − 32) changes Fahrenheit to Celsius. How many degrees Celsius is 68 °F?", f"La fórmula C = {fr(5, 9)}(F − 32) convierte Fahrenheit en Celsius. ¿Cuántos grados Celsius son 68 °F?"),
          [("a", "20 °C"), ("b", "36 °C"), ("c", "5.8 °C"), ("d", "68 °C")])}
{practica("p8", t("Practice 8 — Perimeter", "Práctica 8 — Perímetro"), t("The perimeter of a rectangle is P = 2(l + w). What is the perimeter if l = 7.5 inches and w = 4 inches?", "El perímetro de un rectángulo es P = 2(l + w). ¿Cuál es el perímetro si l = 7.5 pulgadas y w = 4 pulgadas?"),
          [("a", t("19 inches", "19 pulgadas")), ("b", t("30 inches", "30 pulgadas")), ("c", t("34 inches", "34 pulgadas")), ("d", t("23 inches", "23 pulgadas"))])}
{enlace(n, t("formulas", "formulas"), t("formulas in context", "fórmulas en contexto"), t("Try the GED formulas with your own values and answer GED-style questions.", "Pruebe las fórmulas del GED con sus propios valores y responda preguntas tipo examen."))}'''

    secciones = [("s-" + t("fractions", "fracciones"), t("PEMDAS with fractions", "Operar con fracciones siguiendo PEMDAS"), s1),
                 ("s-" + t("substitute", "sustituir"), t("From numbers to letters: substitute and evaluate", "Del número a la letra: sustituir y evaluar"), s2),
                 ("s-" + t("formulas", "formulas"), t("Formulas in context: how the GED asks", "Fórmulas en contexto: así pregunta el GED"), s3)]

    lesson = {"next": t("Topic 4", "el Tema 4"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You added 1/3 + 2/3 = 1 first. Multiply first.", "Sumó 1/3 + 2/3 = 1 primero. Primero se multiplica."), "c": t("Check the product: 2/3 × 3/4 = 6/12 = 1/2.", "Revise el producto: 2/3 × 3/4 = 6/12 = 1/2."), "d": t("1/2 is only the product. Now add 1/3.", "1/2 es solo el producto. Ahora sume 1/3.")},
             "right": t("2/3 × 3/4 = 1/2; 1/3 + 1/2 = 2/6 + 3/6 = 5/6.", "2/3 × 3/4 = 1/2; 1/3 + 1/2 = 2/6 + 3/6 = 5/6."), "solution": t("MD: 2/3 × 3/4 = 6/12 = 1/2. AS: 1/3 + 1/2 = 2/6 + 3/6 = 5/6.", "MD: 2/3 × 3/4 = 6/12 = 1/2. AS: 1/3 + 1/2 = 2/6 + 3/6 = 5/6.")},
      "p2": {"ok": "c", "hints": {"a": t("(3/4)<sup>2</sup> is 9/16, not 3/4 × 2.", "(3/4)<sup>2</sup> es 9/16, no 3/4 × 2."), "b": t("You did not square: 3/4 × 16 = 12. Raise the fraction first.", "No elevó al cuadrado: 3/4 × 16 = 12. Primero eleve la fracción."), "d": t("The parentheses raise the whole fraction: 3 × 3 over 4 × 4.", "El paréntesis eleva la fracción completa: 3 × 3 sobre 4 × 4.")},
             "right": t("(3/4)<sup>2</sup> = 9/16; 9/16 × 16 = 9.", "(3/4)<sup>2</sup> = 9/16; 9/16 × 16 = 9."), "solution": t("E: (3/4)<sup>2</sup> = 9/16. MD: 9/16 × 16 = 144/16 = 9.", "E: (3/4)<sup>2</sup> = 9/16. MD: 9/16 × 16 = 144/16 = 9.")},
      "p3": {"ok": "b", "hints": {"a": t("You used x = 5. The value is −5, in parentheses.", "Usó x = 5. El valor es −5, entre paréntesis."), "c": t("Check: 3 × (−5) = −15, and −15 + 4 is not −19.", "Revise: 3 × (−5) = −15, y −15 + 4 no es −19."), "d": t("3x means 3 × x, not 3 + x.", "3x quiere decir 3 × x, no 3 + x.")},
             "right": t("3(−5) + 4 = −15 + 4 = −11.", "3(−5) + 4 = −15 + 4 = −11."), "solution": t("Substitute: 3(−5) + 4. MD: 3 × (−5) = −15. AS: −15 + 4 = −11.", "Se sustituye: 3(−5) + 4. MD: 3 × (−5) = −15. AS: −15 + 4 = −11.")},
      "p4": {"ok": "d", "hints": {"a": t("2x for x = −3 is −6, not 6.", "2x para x = −3 es −6, no 6."), "b": t("(−3)<sup>2</sup> = 9, positive, because of the parentheses.", "(−3)<sup>2</sup> = 9, positivo, gracias al paréntesis."), "c": t("(−3)<sup>2</sup> is 9, not −6.", "(−3)<sup>2</sup> es 9, no −6.")},
             "right": t("(−3)<sup>2</sup> + 2(−3) = 9 − 6 = 3.", "(−3)<sup>2</sup> + 2(−3) = 9 − 6 = 3."), "solution": t("Substitute: (−3)<sup>2</sup> + 2(−3). E: 9. MD: 2 × (−3) = −6. AS: 9 − 6 = 3.", "Se sustituye: (−3)<sup>2</sup> + 2(−3). E: 9. MD: 2 × (−3) = −6. AS: 9 − 6 = 3.")},
      "p5": {"ok": "c", "hints": {"a": t("You multiplied by 2 before squaring: (2 × (−3))<sup>2</sup>. The exponent goes first.", "Multiplicó por 2 antes de elevar: (2 × (−3))<sup>2</sup>. El exponente va primero."), "b": t("(−3)<sup>2</sup> is positive: 9.", "(−3)<sup>2</sup> es positivo: 9."), "d": t("Squaring is not multiplying by 2: (−3)<sup>2</sup> = 9.", "Elevar al cuadrado no es multiplicar por 2: (−3)<sup>2</sup> = 9.")},
             "right": t("2(1 − 4)<sup>2</sup> = 2(−3)<sup>2</sup> = 2 × 9 = 18.", "2(1 − 4)<sup>2</sup> = 2(−3)<sup>2</sup> = 2 × 9 = 18."), "solution": t("P: 1 − 4 = −3. E: (−3)<sup>2</sup> = 9. MD: 2 × 9 = 18.", "P: 1 − 4 = −3. E: (−3)<sup>2</sup> = 9. MD: 2 × 9 = 18.")},
      "p6": {"ok": "c", "hints": {"a": t("You added 3.50 + 2.25 first. Multiply first.", "Sumó 3.50 + 2.25 primero. Primero se multiplica."), "b": t("2.25m means 2.25 × m, not 2.25 + m.", "2.25m quiere decir 2.25 × m, no 2.25 + m."), "d": t("$18.00 is only 2.25 × 8. Add the fixed charge.", "$18.00 es solo 2.25 × 8. Sume el cargo fijo.")},
             "right": t("2.25 × 8 = 18; 3.50 + 18 = $21.50.", "2.25 × 8 = 18; 3.50 + 18 = $21.50."), "solution": t("MD: 2.25 × 8 = 18. AS: 3.50 + 18 = 21.50. The ride costs $21.50.", "MD: 2.25 × 8 = 18. AS: 3.50 + 18 = 21.50. El viaje cuesta $21.50.")},
      "p7": {"ok": "a", "hints": {"b": t("36 is only 68 − 32. Now multiply by 5/9.", "36 es solo 68 − 32. Ahora multiplique por 5/9."), "c": t("The parentheses go first: subtract 32 before multiplying.", "El paréntesis va primero: reste 32 antes de multiplicar."), "d": t("68 is the temperature in Fahrenheit. Use the formula.", "68 es la temperatura en Fahrenheit. Use la fórmula.")},
             "right": t("68 − 32 = 36; 5/9 × 36 = 20 °C.", "68 − 32 = 36; 5/9 × 36 = 20 °C."), "solution": t("P: 68 − 32 = 36. MD: 5/9 × 36 = 180/9 = 20. The answer is 20 °C.", "P: 68 − 32 = 36. MD: 5/9 × 36 = 180/9 = 20. El resultado es 20 °C.")},
      "p8": {"ok": "d", "hints": {"a": t("19 = 2 × 7.5 + 4. The 2 multiplies the whole parentheses.", "19 = 2 × 7.5 + 4. El 2 multiplica a todo el paréntesis."), "b": t("30 = 7.5 × 4 is the area, not the perimeter.", "30 = 7.5 × 4 es el área, no el perímetro."), "c": t("Check the sum: 7.5 + 4 = 11.5.", "Revise la suma: 7.5 + 4 = 11.5.")},
             "right": t("2(7.5 + 4) = 2 × 11.5 = 23 inches.", "2(7.5 + 4) = 2 × 11.5 = 23 pulgadas."), "solution": t("P: 7.5 + 4 = 11.5. MD: 2 × 11.5 = 23. The perimeter is 23 inches.", "P: 7.5 + 4 = 11.5. MD: 2 × 11.5 = 23. El perímetro es 23 pulgadas.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Without parentheses, the calculator divides only the 6.", "Sin paréntesis, la calculadora divide solo el 6."), "c": t("The fraction bar groups both parts.", "La barra de fracción agrupa las dos partes."), "d": t("Only the denominator has parentheses here.", "Aquí solo el denominador tiene paréntesis.")}, "solution": t("(10 + 6) ÷ (5 − 1) = 16 ÷ 4 = 4.", "(10 + 6) ÷ (5 − 1) = 16 ÷ 4 = 4.")},
      "B": {"ok": "d", "hints": {"a": t("You added first. Multiply 1/2 × 1/3 first.", "Sumó primero. Primero multiplique 1/2 × 1/3."), "b": t("1/6 is only the product. Now add 1/2.", "1/6 es solo el producto. Ahora sume 1/2."), "c": t("1/2 + 1/6 = 3/6 + 1/6 = 4/6. Simplify it.", "1/2 + 1/6 = 3/6 + 1/6 = 4/6. Simplifíquelo.")}, "solution": t("1/2 × 1/3 = 1/6; 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3.", "1/2 × 1/3 = 1/6; 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3.")},
      "C": {"ok": "a", "hints": {"b": t("The parentheses raise the whole fraction: 1/4.", "El paréntesis eleva la fracción completa: 1/4."), "c": t("(1/2)<sup>2</sup> is not 1/2 × 2.", "(1/2)<sup>2</sup> no es 1/2 × 2."), "d": t("Check: 1/4 × 8 = 8/4 = 2.", "Revise: 1/4 × 8 = 8/4 = 2.")}, "solution": t("(1/2)<sup>2</sup> = 1/4; 1/4 × 8 = 2.", "(1/2)<sup>2</sup> = 1/4; 1/4 × 8 = 2.")},
      "D": {"ok": "c", "hints": {"a": t("You used x = 4. The value is −4.", "Usó x = 4. El valor es −4."), "b": t("Check: 5 × (−4) = −20, and −20 − 1 is not −19.", "Revise: 5 × (−4) = −20, y −20 − 1 no es −19."), "d": t("Check the sign: 5 × (−4) is negative.", "Revise el signo: 5 × (−4) es negativo.")}, "solution": t("5(−4) − 1 = −20 − 1 = −21.", "5(−4) − 1 = −20 − 1 = −21.")},
      "E": {"ok": "b", "hints": {"a": t("In −x<sup>2</sup> the exponent applies only to x: −(−3)<sup>2</sup> = −9.", "En −x<sup>2</sup> el exponente solo afecta a la x: −(−3)<sup>2</sup> = −9."), "c": t("(−3)<sup>2</sup> = 9, not 6.", "(−3)<sup>2</sup> = 9, no 6."), "d": t("Square first, then apply the sign in front.", "Primero eleve; después aplique el signo de delante.")}, "solution": t("−(−3)<sup>2</sup> = −(9) = −9.", "−(−3)<sup>2</sup> = −(9) = −9.")},
      "F": {"ok": "d", "hints": {"a": t("Denominator: 4 − (−2) = 4 + 2 = 6.", "Denominador: 4 − (−2) = 4 + 2 = 6."), "b": t("Numerator: 4 + (−2) = 2.", "Numerador: 4 + (−2) = 2."), "c": t("2/6 simplifies to 1/3.", "2/6 se simplifica a 1/3.")}, "solution": t("(4 + (−2)) ÷ (4 − (−2)) = 2 ÷ 6 = 1/3.", "(4 + (−2)) ÷ (4 − (−2)) = 2 ÷ 6 = 1/3.")},
      "G": {"ok": "a", "hints": {"b": t("You added 9/5 + 32 before multiplying.", "Sumó antes de multiplicar."), "c": t("Add 32 after multiplying.", "Falta sumar 32 después de multiplicar."), "d": t("Multiply 10 by 9/5 first.", "Primero multiplique 10 por 9/5.")}, "solution": t("9/5 × 10 = 18; 18 + 32 = 50 °F.", "9/5 × 10 = 18; 18 + 32 = 50 °F.")},
      "H": {"ok": "c", "hints": {"a": t("Do not forget the 1/2.", "No olvide el 1/2."), "b": t("The h multiplies; it is not added.", "La h multiplica; no se suma."), "d": t("Add the bases first: 4 + 8 = 12.", "Primero sume las bases: 4 + 8 = 12.")}, "solution": t("1/2(4 + 8)(3) = 1/2 × 12 × 3 = 18 square feet.", "1/2(4 + 8)(3) = 1/2 × 12 × 3 = 18 pies cuadrados.")}
     }}

    quiz = [
     ("A", t("How do you write", "¿Cómo se escribe") + " " + frx("10 + 6", "5 − 1") + " " + t("on one line?", "en una sola línea?"), [("a", "10 + 6 ÷ 5 − 1"), ("b", "(10 + 6) ÷ (5 − 1)"), ("c", "10 + (6 ÷ 5) − 1"), ("d", "10 + 6 ÷ (5 − 1)")]),
     ("B", t(f"What is {fr(1, 2)} + {fr(1, 2)} × {fr(1, 3)}?", f"¿Cuánto es {fr(1, 2)} + {fr(1, 2)} × {fr(1, 3)}?"), [("a", fr(1, 3)), ("b", fr(1, 6)), ("c", fr(4, 12)), ("d", fr(2, 3))]),
     ("C", t(f"What is {P(1, 2)}<sup>2</sup> × 8?", f"¿Cuánto es {P(1, 2)}<sup>2</sup> × 8?"), [("a", "2"), ("b", "4"), ("c", "8"), ("d", "1")]),
     ("D", t("Evaluate 5x − 1 for x = −4.", "Evalúe 5x − 1 para x = −4."), [("a", "19"), ("b", "−19"), ("c", "−21"), ("d", "21")]),
     ("E", t("Evaluate −x<sup>2</sup> for x = −3.", "Evalúe −x<sup>2</sup> para x = −3."), [("a", "9"), ("b", "−9"), ("c", "6"), ("d", "−6")]),
     ("F", t("Evaluate", "Evalúe") + " " + frx("a + b", "a − b") + " " + t("for a = 4 and b = −2.", "para a = 4 y b = −2."), [("a", "1"), ("b", "3"), ("c", fr(2, 6)), ("d", fr(1, 3))]),
     ("G", t(f"Use F = {fr(9, 5)}C + 32. How many degrees Fahrenheit is 10 °C?", f"Use F = {fr(9, 5)}C + 32. ¿Cuántos grados Fahrenheit son 10 °C?"), [("a", "50 °F"), ("b", "75.6 °F"), ("c", "18 °F"), ("d", "42 °F")]),
     ("H", t(f"Use A = {fr(1, 2)}(b<sub>1</sub> + b<sub>2</sub>)h with b<sub>1</sub> = 4 ft, b<sub>2</sub> = 8 ft, and h = 3 ft.", f"Use A = {fr(1, 2)}(b<sub>1</sub> + b<sub>2</sub>)h con b<sub>1</sub> = 4 pies, b<sub>2</sub> = 8 pies y h = 3 pies."),
      [("a", t("36 sq ft", "36 pies cuadrados")), ("b", t("9 sq ft", "9 pies cuadrados")), ("c", t("18 sq ft", "18 pies cuadrados")), ("d", t("10 sq ft", "10 pies cuadrados"))])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Fractions inside PEMDAS, and the step from numbers to letters: substitute in parentheses, evaluate, and use GED formulas.", "Las fracciones dentro de PEMDAS y el paso de los números a las letras: sustituir entre paréntesis, evaluar y usar las fórmulas del GED."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Operate</strong> with fractions (add, subtract, multiply, divide, and raise to a power) following PEMDAS.", "<strong>Operar</strong> con fracciones (sumar, restar, multiplicar, dividir y elevar) respetando PEMDAS."),
         t("<strong>Tell</strong> (a/b)<sup>2</sup> from a<sup>2</sup>/b.", "<strong>Distinguir</strong> (a/b)<sup>2</sup> de a<sup>2</sup>/b."),
         t("<strong>Substitute</strong> positive, negative, and fraction values into algebraic expressions, and evaluate them.", "<strong>Sustituir</strong> valores positivos, negativos y fraccionarios en expresiones algebraicas y evaluarlas."),
         t("<strong>Apply</strong> GED formulas to problems in context.", "<strong>Aplicar</strong> fórmulas de la hoja del GED a problemas con contexto."),
         t("<strong>Check</strong> answers on the calculator with the parentheses you need.", "<strong>Verificar</strong> resultados con la calculadora usando los paréntesis necesarios.")],
        secciones,
        (t("Solve eight PEMDAS expressions with fractions (fraction bars, operations with fractions, and powers of fractions), one line per step. Then evaluate four expressions from this lesson with new values: one positive, one negative, and one fraction. Last, choose three GED formulas (temperature, area of a trapezoid, and cost with a fixed charge), make up reasonable values, evaluate them, and check them on the calculator.",
           "Resuelva ocho expresiones de PEMDAS con fracciones (barras de fracción, operaciones entre fracciones y potencias de fracciones), una línea por paso. Después evalúe cuatro expresiones de esta lección con valores nuevos: uno positivo, uno negativo y uno fraccionario. Por último, elija tres fórmulas del GED (temperatura, área del trapecio y costo con cargo fijo), invente valores razonables, evalúelas y compruébelas en la calculadora."),
         t("Find a formula in your daily life: a phone plan, a taxi or ride app, a gym, or a repair shop that charges a fixed fee plus a rate. Write it as C = fixed + rate × units, and find the cost for two different amounts.",
           "Busque una fórmula de su vida diaria: un plan de teléfono, un taxi o una aplicación de viajes, un gimnasio o un taller que cobre un cargo fijo más una tarifa. Escríbala como C = cargo fijo + tarifa × unidades y calcule el costo para dos cantidades distintas.")),
        quiz,
        t("Self-check checklist for PEMDAS with fractions and in algebra", "Lista de autoevaluación de PEMDAS con fracciones y en álgebra"),
        t("Self-check checklist: skills for PEMDAS with fractions and in algebra", "Lista de autoevaluación: destrezas de PEMDAS con fracciones y en álgebra"),
        [(t("Fractions with PEMDAS", "Fracciones con PEMDAS"), t("I follow the order and simplify the answer.", "Sigo el orden y simplifico el resultado."), t("I follow the order, but I make mistakes with common denominators.", "Sigo el orden, pero me equivoco con los denominadores comunes."), t("I add before I multiply.", "Sumo antes de multiplicar.")),
         (t("Substitution", "Sustitución"), t("I always substitute in parentheses, with positive, negative, and fraction values.", "Siempre sustituyo entre paréntesis, con valores positivos, negativos y fraccionarios."), t("I do well with positive values, but I lose signs with negative ones.", "Me va bien con valores positivos, pero pierdo signos con los negativos."), t("I substitute without parentheses.", "Sustituyo sin paréntesis.")),
         (t("−x<sup>2</sup> and (−x)<sup>2</sup>", "−x<sup>2</sup> y (−x)<sup>2</sup>"), t("I tell them apart and explain why.", "Los distingo y explico por qué."), t("I tell them apart only sometimes.", "Los distingo solo a veces."), t("I give the same answer for both.", "Doy el mismo resultado para los dos.")),
         (t("Formulas", "Fórmulas"), t("I find the value of each letter, answer with the unit, and check if it makes sense.", "Identifico el valor de cada letra, respondo con la unidad y compruebo que tenga sentido."), t("I substitute, but I forget the unit.", "Sustituyo, pero olvido la unidad."), t("I do not know which value goes with each letter.", "No sé qué valor corresponde a cada letra."))],
        t("<p>With this lesson you finish <strong>Topic 3</strong>. PEMDAS now works with every tool of Level 2: integers, powers, roots, fractions and, for the first time, expressions with <strong>variables</strong>. Substituting a value in parentheses and following the order of operations is the skill the GED asks for every time it gives you a formula.</p>\n<p><strong>Topic 4 · Ratios, rates, and proportions</strong> opens with Lesson 4.1 · Ratios and unit rates. From calculating expressions you will move to <strong>comparing quantities</strong>: unit prices, speeds, and rates of use. The fractions you practiced today come back as ratios.</p>",
          "<p>Con esta lección termina el <strong>Tema 3</strong>. PEMDAS ya funciona con todas las herramientas del Nivel 2: enteros, potencias, raíces, fracciones y, por primera vez, expresiones con <strong>variables</strong>. Sustituir un valor entre paréntesis y respetar el orden de las operaciones es la destreza que el GED exige cada vez que presenta una fórmula.</p>\n<p>El <strong>Tema 4 · Razones, tasas unitarias y proporciones</strong> abre con la Lección 4.1 · Razones y tasas unitarias en contexto. Del cálculo de expresiones pasará a <strong>comparar cantidades</strong>: precios por unidad, velocidades y consumos. Las fracciones que practicó hoy reaparecerán como razones.</p>"),
        ("4-1", ("", t("Lesson 4.1 · Ratios and unit rates", "Lección 4.1 · Razones y tasas unitarias en contexto"))),
        [(t("variable", "variable"), t("A letter that takes the place of a number, like x.", "Una letra que ocupa el lugar de un número, como x.")),
         (t("evaluate", "evaluar"), t("To replace each letter with its value and calculate.", "Reemplazar cada letra por su valor y calcular.")),
         (t("substitute", "sustituir"), t("To put a number in place of a letter, always inside parentheses.", "Poner un número en el lugar de una letra, siempre entre paréntesis.")),
         (t("formula", "fórmula"), t("A rule written with letters, like P = 2(l + w).", "Una regla escrita con letras, como P = 2(l + w)."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "calcula": "What is {e}? Write it in simplest form.",
  "multPrimero": "MD before AS: {b} × {c} = {p}.", "luegoSuma": "Then AS: {a} + {p} = {r}.",
  "potPrimero": "E: {a}² = {p}.", "divRecip": "MD: divide by multiplying by the reciprocal: {b} ÷ {c} = {d}.", "luegoResta": "AS: {p} − {d} = {r}.",
  "parPrimero": "P: {a} − {b} = {s}.", "luegoMult": "MD: {s} × {k} = {r}.",
  "barraNum": "Numerator: {n}.", "barraDen": "Denominator: {d}.", "barraDiv": "Divide and simplify: {r}.",
  "sumoAntes": "You added before multiplying. Multiply first.", "restoAntes": "You subtracted before dividing. Divide first.",
  "potSolo": "The parentheses raise the whole fraction: square the numerator and the denominator.",
  "divMal": "To divide, multiply by the reciprocal of the second fraction.", "parAntes": "The parentheses go first: subtract inside them, then multiply.",
  "restaNeg": "In the denominator, subtracting a negative is adding.",
  "evalua": "Evaluate {e}.", "para": " for ", "y": " and ",
  "sustituyendo": "Substituting: {s}.", "numDen": "Numerator: {n}. Denominator: {d}. Answer: {r}.",
  "pSuma": "{a}x means {a} × x, not {a} + x.", "pSigno": "Check the sign: the value you substitute is {x}.",
  "pCuad": "Without parentheses, {x}² reads as −({b}²). With parentheses, ({x})² = {c}.",
  "pNegCuad": "In −x² the exponent applies only to the x: square first, then apply the sign in front.",
  "pAntesMul": "The exponent goes before multiplying by {a}: square only what is inside the parentheses.",
  "pPor2": "Squaring is multiplying the number by itself, not by 2.", "pB2": "With parentheses, ({b})² is positive: {c}.",
  "susti": "<strong>Substitute in parentheses:</strong> ", "enNum": "In the numerator: {a} + {b} = {n}.",
  "enDen": "In the denominator: {a} − {b} = {d}{x}", "restarNeg": " (subtracting a negative is adding).",
  "denCero": "The denominator is 0, and you cannot divide by 0. Choose other values.",
  "barra": "The fraction bar: {n} ÷ {d}{x}", "simpl": ", which in simplest form is {q}.", "resultado": "Answer: ",
  "escribeNum": "Type a number in each box to see the work.",
  "taxi": ["<strong>Substitute:</strong> C = 3.50 + 2.25{m}", "Multiplication first: 2.25 × {m2} = {u}.", "Then the addition: 3.50 + {u} = {r}.", "The ride costs {d}."],
  "taxiNeg": "With negative miles the answer makes no sense: a distance cannot be negative.",
  "cf": ["<strong>Substitute:</strong> F = (9/5){C} + 32", "Multiplication first: 9/5 × {C2} = {u}.", "Then the addition: {u} + 32 = {r}.", "{C3} °C = {r} °F"],
  "fc": ["<strong>Substitute:</strong> C = (5/9)({F} − 32)", "Parentheses first: {F2} − 32 = {d}.", "Then the multiplication: 5/9 × {d2} = {r}{x}.", "{F2} °F = {r} °C"], "redondeado": " (rounded)",
  "per": ["<strong>Substitute:</strong> P = 2({l} + {w})", "Parentheses first: {l2} + {w2} = {s}.", "Then the multiplication: 2 × {s} = {r}.", "The perimeter is {r} inches."],
  "perNeg": "A length or width of 0 or less makes no sense for a rectangle.",
  "tra": ["<strong>Substitute:</strong> A = ½({b1} + {b2}){h}", "Parentheses first: {b12} + {b22} = {s}.", "Multiplications from left to right: ½ × {s} = {m}; {m} × {h2} = {r}.", "The area is {r} square feet."],
  "int": ["<strong>Substitute:</strong> I = {P}{r}{t}", "Write the rate as a decimal: {rp}% = {rd}.", "Multiplications from left to right: {P2} × {rd} = {u}; {u} × {t2} = {i}.", "The interest is {d}."],
  "fTaxi": [["Taxi", "A taxi charges by the formula C = {f} + {t}m, where m is the number of miles. How much does a {n}-mile ride cost?"], ["Gym", "A gym charges C = {f} + {t}m, where m is the number of months. How much does a person pay for {n} months?"], ["Plumber", "A plumber charges C = {f} + {t}h, where h is the number of hours. How much does a {n}-hour job cost?"]],
  "mSumaAntes": "You added before multiplying; PEMDAS says to multiply first.", "mFijo": "You need to add the fixed charge of {f}.", "mLetra": "A letter next to a number means multiplication, not addition.",
  "solTaxi": "Multiply first: {t} × {n} = {u}; then add the fixed charge: {f} + {u} = {c}.",
  "qCF": "The formula F = (9/5)C + 32 changes degrees Celsius to degrees Fahrenheit. How many degrees Fahrenheit is {C} °C?",
  "mFalta32": "You need to add 32 after multiplying.", "m32Antes": "You added 32 before multiplying; the multiplication goes first.", "mFalta95": "You need to multiply by 9/5.",
  "solCF": "9/5 × {C} = {u}; {u} + 32 = {F} °F.",
  "qFC": "The formula C = (5/9)(F − 32) changes degrees Fahrenheit to degrees Celsius. How many degrees Celsius is {F} °F?",
  "mParPrimero": "The parentheses go first: subtract 32 before multiplying.", "mFalta59": "You need to multiply by 5/9.", "mFaltaRestar": "You need to subtract 32 inside the parentheses.",
  "solFC": "Parentheses: {F} − 32 = {d}; 5/9 × {d2} = {C} °C.",
  "qPer": "The perimeter of a rectangle is P = 2(l + w). What is the perimeter if l = {l} inches and w = {w} inches?", "pulg": " inches",
  "mTodo2": "The 2 multiplies the whole parentheses: add l + w first.", "mFalta2": "You need to multiply by 2.", "mArea": "That is the area (l × w), not the perimeter.",
  "solPer": "Parentheses: {l} + {w} = {s}; 2 × {s} = {P} inches.",
  "qTra": "The area of a trapezoid is A = ½(b₁ + b₂)h. Find the area if b₁ = {b1} feet, b₂ = {b2} feet, and h = {h} feet.", "pies2": " square feet",
  "mFaltaMedio": "You need to multiply by ½.", "mMedioTodo": "The ½ and the h multiply the whole sum in the parentheses.", "mHSuma": "The h next to the parentheses means multiplication, not addition.",
  "solTra": "Parentheses: {b1} + {b2} = {s}; ½ × {s} = {m}; {m} × {h} = {A} square feet.",
  "qInt": "The simple interest formula is I = Prt. How much interest do {P} earn at a yearly rate of {r}% for {t} years?",
  "mTasaDec": "Write the rate as a decimal: {r}% = {rd}.", "mUnAno": "That is the interest for one year only; multiply by {t}.", "mMonto": "That is the final amount (principal plus interest), not the interest.",
  "solInt": "{P} × {rd} = {u}; {u} × {t} = {I}.",
  "tpl": ["4x − 7", "x² − 3x + 2", "−x² + 4", "2(a − b)²", "(a + b) ÷ (a − b)"]
 },
 "es": {
  "calcula": "¿Cuánto es {e}? Escríbalo simplificado.",
  "multPrimero": "MD antes que AS: {b} × {c} = {p}.", "luegoSuma": "Después AS: {a} + {p} = {r}.",
  "potPrimero": "E: {a}² = {p}.", "divRecip": "MD: se divide multiplicando por el recíproco: {b} ÷ {c} = {d}.", "luegoResta": "AS: {p} − {d} = {r}.",
  "parPrimero": "P: {a} − {b} = {s}.", "luegoMult": "MD: {s} × {k} = {r}.",
  "barraNum": "Numerador: {n}.", "barraDen": "Denominador: {d}.", "barraDiv": "Se divide y se simplifica: {r}.",
  "sumoAntes": "Sumó antes de multiplicar. Primero se multiplica.", "restoAntes": "Restó antes de dividir. Primero se divide.",
  "potSolo": "El paréntesis eleva la fracción completa: eleve el numerador y el denominador.",
  "divMal": "Para dividir, multiplique por el recíproco de la segunda fracción.", "parAntes": "El paréntesis va primero: reste dentro de él y después multiplique.",
  "restaNeg": "En el denominador, restar un negativo es sumar.",
  "evalua": "Evalúe {e}.", "para": " para ", "y": " y ",
  "sustituyendo": "Sustituyendo: {s}.", "numDen": "Numerador: {n}. Denominador: {d}. Resultado: {r}.",
  "pSuma": "{a}x quiere decir {a} × x, no {a} + x.", "pSigno": "Revise el signo: el valor que se sustituye es {x}.",
  "pCuad": "Sin paréntesis, {x}² se lee como −({b}²). Con paréntesis, ({x})² = {c}.",
  "pNegCuad": "En −x² el exponente solo afecta a la x: primero se eleva y después se aplica el signo de delante.",
  "pAntesMul": "El exponente va antes que la multiplicación por {a}: solo se eleva lo que está dentro del paréntesis.",
  "pPor2": "Elevar al cuadrado es multiplicar el número por sí mismo, no por 2.", "pB2": "Con paréntesis, ({b})² es positivo: {c}.",
  "susti": "<strong>Sustituir entre paréntesis:</strong> ", "enNum": "En el numerador: {a} + {b} = {n}.",
  "enDen": "En el denominador: {a} − {b} = {d}{x}", "restarNeg": " (restar un negativo es sumar).",
  "denCero": "El denominador da 0, y no se puede dividir entre 0. Elija otros valores.",
  "barra": "La barra de fracción: {n} ÷ {d}{x}", "simpl": ", que simplificado queda {q}.", "resultado": "Resultado: ",
  "escribeNum": "Escriba un número en cada casilla para ver el cálculo.",
  "taxi": ["<strong>Sustituir:</strong> C = 3.50 + 2.25{m}", "Primero la multiplicación: 2.25 × {m2} = {u}.", "Después la suma: 3.50 + {u} = {r}.", "El viaje cuesta {d}."],
  "taxiNeg": "Con millas negativas el resultado no tiene sentido: una distancia no puede ser negativa.",
  "cf": ["<strong>Sustituir:</strong> F = (9/5){C} + 32", "Primero la multiplicación: 9/5 × {C2} = {u}.", "Después la suma: {u} + 32 = {r}.", "{C3} °C = {r} °F"],
  "fc": ["<strong>Sustituir:</strong> C = (5/9)({F} − 32)", "Primero el paréntesis: {F2} − 32 = {d}.", "Después la multiplicación: 5/9 × {d2} = {r}{x}.", "{F2} °F = {r} °C"], "redondeado": " (redondeado)",
  "per": ["<strong>Sustituir:</strong> P = 2({l} + {w})", "Primero el paréntesis: {l2} + {w2} = {s}.", "Después la multiplicación: 2 × {s} = {r}.", "El perímetro es {r} pulgadas."],
  "perNeg": "Un largo o un ancho de 0 o menos no tiene sentido en un rectángulo.",
  "tra": ["<strong>Sustituir:</strong> A = ½({b1} + {b2}){h}", "Primero el paréntesis: {b12} + {b22} = {s}.", "Multiplicaciones de izquierda a derecha: ½ × {s} = {m}; {m} × {h2} = {r}.", "El área es {r} pies cuadrados."],
  "int": ["<strong>Sustituir:</strong> I = {P}{r}{t}", "La tasa se escribe en decimal: {rp}% = {rd}.", "Multiplicaciones de izquierda a derecha: {P2} × {rd} = {u}; {u} × {t2} = {i}.", "El interés es {d}."],
  "fTaxi": [["Taxi", "Un taxi cobra según la fórmula C = {f} + {t}m, donde m es el número de millas. ¿Cuánto cuesta un viaje de {n} millas?"], ["Gimnasio", "Un gimnasio cobra C = {f} + {t}m, donde m es el número de meses. ¿Cuánto paga una persona por {n} meses?"], ["Plomero", "Un plomero cobra C = {f} + {t}h, donde h es el número de horas. ¿Cuánto cobra por un trabajo de {n} horas?"]],
  "mSumaAntes": "Se sumó antes de multiplicar; PEMDAS pide multiplicar primero.", "mFijo": "Falta sumar el cargo fijo de {f}.", "mLetra": "La letra pegada al número indica multiplicación, no suma.",
  "solTaxi": "Primero se multiplica: {t} × {n} = {u}; después se suma el cargo fijo: {f} + {u} = {c}.",
  "qCF": "La fórmula F = (9/5)C + 32 convierte grados Celsius en grados Fahrenheit. ¿Cuántos grados Fahrenheit son {C} °C?",
  "mFalta32": "Falta sumar 32 después de multiplicar.", "m32Antes": "Se sumó 32 antes de multiplicar; la multiplicación va primero.", "mFalta95": "Falta multiplicar por 9/5.",
  "solCF": "9/5 × {C} = {u}; {u} + 32 = {F} °F.",
  "qFC": "La fórmula C = (5/9)(F − 32) convierte grados Fahrenheit en grados Celsius. ¿Cuántos grados Celsius son {F} °F?",
  "mParPrimero": "El paréntesis va primero: hay que restar 32 antes de multiplicar.", "mFalta59": "Falta multiplicar por 5/9.", "mFaltaRestar": "Falta restar 32 dentro del paréntesis.",
  "solFC": "Paréntesis: {F} − 32 = {d}; 5/9 × {d2} = {C} °C.",
  "qPer": "El perímetro de un rectángulo es P = 2(l + w). ¿Cuál es el perímetro si l = {l} pulgadas y w = {w} pulgadas?", "pulg": " pulgadas",
  "mTodo2": "El 2 multiplica a todo el paréntesis: primero se suma l + w.", "mFalta2": "Falta multiplicar por 2.", "mArea": "Eso es el área (l × w), no el perímetro.",
  "solPer": "Paréntesis: {l} + {w} = {s}; 2 × {s} = {P} pulgadas.",
  "qTra": "El área de un trapecio es A = ½(b₁ + b₂)h. Calcule el área si b₁ = {b1} pies, b₂ = {b2} pies y h = {h} pies.", "pies2": " pies cuadrados",
  "mFaltaMedio": "Falta multiplicar por ½.", "mMedioTodo": "El ½ y la h multiplican a toda la suma del paréntesis.", "mHSuma": "La h pegada al paréntesis indica multiplicación, no suma.",
  "solTra": "Paréntesis: {b1} + {b2} = {s}; ½ × {s} = {m}; {m} × {h} = {A} pies cuadrados.",
  "qInt": "La fórmula del interés simple es I = Prt. ¿Cuánto interés producen {P} a una tasa anual del {r}% durante {t} años?",
  "mTasaDec": "La tasa se escribe en decimal: {r}% = {rd}.", "mUnAno": "Ese es el interés de un solo año; falta multiplicar por {t}.", "mMonto": "Ese es el monto final (capital más interés), no el interés.",
  "solInt": "{P} × {rd} = {u}; {u} × {t} = {I}.",
  "tpl": ["4x − 7", "x² − 3x + 2", "−x² + 4", "2(a − b)²", "(a + b) ÷ (a − b)"]
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function S(v){ return '<span class="sust">(' + (typeof v === "number" ? ent(v) : v) + ')</span>'; }
function mk(v){ return G("(", [N(v)]); }
function fmt(x){ return menos(Number(x).toLocaleString("en-US", { maximumFractionDigits: 2 })); }
function dinero(x){ return (x < 0 ? "−" : "") + "$" + Math.abs(x).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
function redondea(x, d){ var p = Math.pow(10, d === undefined ? 2 : d); return Math.round(x * p) / p; }
function lineas(arr){ return arr.map(function(h){ return '<div class="linea">' + h + '</div>'; }).join(""); }
function signoTxt(b){ return b < 0 ? " − " + Math.abs(b) : " + " + b; }
function nzr(a, b){ var n; do { n = aleatorio(a, b); } while (n === 0); return n; }
function quita(pistas, res){ return pistas.filter(function(p){ return p.v !== res; }); }

/* ============ MODULE 1 · fractions with PEMDAS ============ */
function rq(){ var d = aleatorio(2, 6); return q(aleatorio(1, d - 1), d); }
function genFrac(){
  var tipo = aleatorio(1, 4), a, b, c, r, e, sol, pistas = [];
  if (tipo === 1){
    a = rq(); b = rq(); c = rq(); var p = qmul(b, c); r = qsum(a, p);
    e = qH(a) + " + " + qH(b) + " × " + qH(c);
    sol = F(TXT.multPrimero, { b: qH(b), c: qH(c), p: qH(p) }) + " " + F(TXT.luegoSuma, { a: qH(a), p: qH(p), r: qH(r) });
    pistas.push({ v: qmul(qsum(a, b), c), msg: TXT.sumoAntes });
  } else if (tipo === 2){
    do { a = rq(); b = rq(); c = rq(); var pw2 = qmul(a, a), d = qdiv(b, c); r = qres(pw2, d); } while (Math.abs(r.n) > 40 || r.d > 72);
    e = "(" + qH(a) + ")<sup>2</sup> − " + qH(b) + " ÷ " + qH(c);
    sol = F(TXT.potPrimero, { a: "(" + qH(a) + ")", p: qH(pw2) }) + " " + F(TXT.divRecip, { b: qH(b), c: qH(c), d: qH(d) }) + " " + F(TXT.luegoResta, { p: qH(pw2), d: qH(d), r: qH(r) });
    pistas.push({ v: qres(q(a.n * a.n, a.d), d), msg: TXT.potSolo });
    pistas.push({ v: qdiv(qres(pw2, b), c), msg: TXT.restoAntes });
    pistas.push({ v: qres(pw2, qmul(b, c)), msg: TXT.divMal });
  } else if (tipo === 3){
    a = rq(); if (Math.random() < 0.4) a = qneg(a); b = rq(); var k = aleatorio(2, 12), s = qres(a, b); r = qmul(s, q(k));
    e = "(" + qH(a) + " − " + qH(b) + ") × " + k;
    sol = F(TXT.parPrimero, { a: qH(a), b: qH(b), s: qH(s) }) + " " + F(TXT.luegoMult, { s: qP(s), k: k, r: qH(r) });
    pistas.push({ v: qres(a, qmul(b, q(k))), msg: TXT.parAntes });
  } else {
    var n1, n2, d1, d2;
    do { n1 = nzr(-9, 9); n2 = nzr(-9, 9); d1 = nzr(-9, 9); d2 = nzr(-9, 9); } while (d1 === d2 || n1 + n2 === 0 || (n1 + n2) % (d1 - d2) === 0 && Math.random() < 0.6);
    r = q(n1 + n2, d1 - d2);
    e = '<span class="fracc"><span class="fa">' + ent(n1) + signoTxt(n2).replace("-", "−") + '</span><span class="fb2">' + ent(d1) + " − " + par(d2) + '</span></span>';
    sol = F(TXT.barraNum, { n: ent(n1) + signoTxt(n2) + " = " + ent(n1 + n2) }) + " " + F(TXT.barraDen, { d: ent(d1) + " − " + par(d2) + " = " + ent(d1 - d2) }) + " " + F(TXT.barraDiv, { r: qH(r) });
    if (d2 < 0) pistas.push({ v: q(n1 + n2, d1 + d2), msg: TXT.restaNeg });
  }
  pistas = pistas.filter(function(p){ return p.v.d && !qigual(p.v, r); });
  return { enun: F(TXT.calcula, { e: '<span class="ex">' + e + '</span>' }), correcta: qTxt(r), solucion: sol, evalua: evQ(r, pistas) };
}

/* ============ MODULE 2 · substitute and evaluate ============ */
var TPL = [
  { vars: ["x"], vis: function(v){ return "4" + S(v.x) + " − 7"; }, e: function(v){ return [N(4), "×", mk(v.x), "−", N(7)]; } },
  { vars: ["x"], vis: function(v){ return S(v.x) + "<sup>2</sup> − 3" + S(v.x) + " + 2"; }, e: function(v){ return [Pw(mk(v.x), 2), "−", N(3), "×", mk(v.x), "+", N(2)]; } },
  { vars: ["x"], vis: function(v){ return "−" + S(v.x) + "<sup>2</sup> + 4"; }, e: function(v){ return [Mn(Pw(mk(v.x), 2)), "+", N(4)]; } },
  { vars: ["a", "b"], vis: function(v){ return "2(" + S(v.a) + " − " + S(v.b) + ")<sup>2</sup>"; }, e: function(v){ return [N(2), "×", Pw(G("(", [mk(v.a), "−", mk(v.b)]), 2)]; } },
  { vars: ["a", "b"], frac: true, vis: function(v){ return '<span class="fracc"><span class="fa">' + S(v.a) + " + " + S(v.b) + '</span><span class="fb2">' + S(v.a) + " − " + S(v.b) + '</span></span>'; } }
];
function pintaSU(){
  var tp = TPL[+$("su-expr").value], v = { x: +$("su-x").value, a: +$("su-a").value, b: +$("su-b").value };
  $("su-xv").textContent = ent(v.x); $("su-av").textContent = ent(v.a); $("su-bv").textContent = ent(v.b);
  $("su-cx").style.display = tp.vars.indexOf("x") >= 0 ? "" : "none";
  $("su-ca").style.display = tp.vars.indexOf("a") >= 0 ? "" : "none";
  $("su-cb").style.display = tp.vars.indexOf("b") >= 0 ? "" : "none";
  var h = [TXT.susti + '<span class="ex">' + tp.vis(v) + '</span>'];
  if (tp.frac){
    var nu = v.a + v.b, de = v.a - v.b;
    h.push(F(TXT.enNum, { a: ent(v.a), b: par(v.b), n: ent(nu) }));
    h.push(F(TXT.enDen, { a: ent(v.a), b: par(v.b), d: ent(de), x: v.b < 0 ? TXT.restarNeg : "." }));
    if (de === 0) h.push('<span class="veredicto">' + TXT.denCero + '</span>');
    else { var qq = q(nu, de); h.push(F(TXT.barra, { n: ent(nu), d: par(de), x: qq.d === 1 ? "." : F(TXT.simpl, { q: qH(qq) }) })); h.push('<span class="veredicto">' + TXT.resultado + qH(qq) + '</span>'); }
  } else h = h.concat(pasosHTML(resolver(tp.e(v))));
  $("su-salida").innerHTML = lineas(h);
}
function genSustituir(){
  var tipo = aleatorio(1, 6), e, enun, res, pistas = [], sust;
  if (tipo === 1){
    var a = aleatorio(2, 9), b = nzr(-12, 12), x = nzr(-6, 6);
    enun = a + "x" + signoTxt(b) + TXT.para + "x = " + ent(x);
    e = [N(a), "×", mk(x), b < 0 ? "−" : "+", N(Math.abs(b))]; sust = a + S(x) + signoTxt(b);
    res = a * x + b;
    pistas.push({ v: a + x + b, msg: F(TXT.pSuma, { a: a }) });
    pistas.push({ v: a * Math.abs(x) + b, msg: F(TXT.pSigno, { x: ent(x) }) });
  } else if (tipo === 2){
    var b2 = nzr(-6, 6), c = aleatorio(-9, 9), x2 = aleatorio(-6, -1);
    enun = "x<sup>2</sup>" + signoTxt(b2) + "x" + (c ? signoTxt(c) : "") + TXT.para + "x = " + ent(x2);
    e = [Pw(mk(x2), 2), b2 < 0 ? "−" : "+", N(Math.abs(b2)), "×", mk(x2)].concat(c ? [c < 0 ? "−" : "+", N(Math.abs(c))] : []);
    sust = S(x2) + "<sup>2</sup>" + signoTxt(b2) + S(x2) + (c ? signoTxt(c) : "");
    res = x2 * x2 + b2 * x2 + c;
    pistas.push({ v: -x2 * x2 + b2 * x2 + c, msg: F(TXT.pCuad, { x: ent(x2), b: Math.abs(x2), c: x2 * x2 }) });
  } else if (tipo === 3){
    var x3 = nzr(-6, 6), c3 = aleatorio(1, 20);
    enun = "−x<sup>2</sup> + " + c3 + TXT.para + "x = " + ent(x3);
    e = [Mn(Pw(mk(x3), 2)), "+", N(c3)]; sust = "−" + S(x3) + "<sup>2</sup> + " + c3;
    res = -x3 * x3 + c3;
    pistas.push({ v: x3 * x3 + c3, msg: TXT.pNegCuad });
  } else if (tipo === 4){
    var a4 = aleatorio(2, 4), b4 = aleatorio(-5, 5), x4; do { x4 = aleatorio(-5, 5); } while (x4 === b4);
    enun = (b4 === 0 ? a4 + "x<sup>2</sup>" : a4 + "(x" + signoTxt(-b4) + ")<sup>2</sup>") + TXT.para + "x = " + ent(x4);
    e = b4 === 0 ? [N(a4), "×", Pw(mk(x4), 2)] : [N(a4), "×", Pw(G("(", [mk(x4), b4 > 0 ? "−" : "+", N(Math.abs(b4))]), 2)];
    sust = b4 === 0 ? a4 + S(x4) + "<sup>2</sup>" : a4 + "(" + S(x4) + signoTxt(-b4) + ")<sup>2</sup>";
    var d4 = x4 - b4; res = a4 * d4 * d4;
    pistas.push({ v: a4 * a4 * d4 * d4, msg: F(TXT.pAntesMul, { a: a4 }) });
    pistas.push({ v: a4 * d4 * 2, msg: TXT.pPor2 });
  } else if (tipo === 5){
    var a5, b5; do { a5 = nzr(-9, 9); b5 = nzr(-9, 9); } while (a5 === b5 || a5 + b5 === 0);
    enun = '<span class="fracc"><span class="fa">a + b</span><span class="fb2">a − b</span></span>' + TXT.para + "a = " + ent(a5) + TXT.y + "b = " + ent(b5);
    sust = '<span class="fracc"><span class="fa">' + S(a5) + " + " + S(b5) + '</span><span class="fb2">' + S(a5) + " − " + S(b5) + '</span></span>';
    var obj = q(a5 + b5, a5 - b5), pf = [];
    if (b5 < 0) pf.push({ v: q(a5 + b5, a5 + b5), msg: TXT.restaNeg });
    pf = pf.filter(function(p){ return !qigual(p.v, obj); });
    return { enun: F(TXT.evalua, { e: '<span class="ex">' + enun + '</span>' }), correcta: qTxt(obj),
      solucion: F(TXT.sustituyendo, { s: sust }) + " " + F(TXT.numDen, { n: ent(a5 + b5), d: ent(a5 - b5), r: qH(obj) }), evalua: evQ(obj, pf) };
  } else {
    var a6 = aleatorio(-8, 8), b6 = aleatorio(-6, -1);
    enun = "2a + b<sup>2</sup>" + TXT.para + "a = " + ent(a6) + TXT.y + "b = " + ent(b6);
    e = [N(2), "×", mk(a6), "+", Pw(mk(b6), 2)]; sust = "2" + S(a6) + " + " + S(b6) + "<sup>2</sup>";
    res = 2 * a6 + b6 * b6;
    pistas.push({ v: 2 * a6 - b6 * b6, msg: F(TXT.pB2, { b: ent(b6), c: b6 * b6 }) });
  }
  var R = resolver(e);
  return { enun: F(TXT.evalua, { e: '<span class="ex">' + enun + '</span>' }), correcta: String(res),
    solucion: F(TXT.sustituyendo, { s: sust }) + " " + R.pasos.map(function(p){ return p.desc; }).join(" "), evalua: numE(res, quita(pistas, res)) };
}

/* ============ MODULE 3 · formulas ============ */
var CAMPOS = {
  taxi: [["m", 8]], cf: [["C", 25]], fc: [["F", 68]], per: [["l", 7.5], ["w", 4]], tra: [["b1", 6], ["b2", 10], ["h", 5]], int: [["P", 1200], ["r", 5], ["t", 3]]
};
function leeNum(s){ s = String(s).trim().replace(/[−–]/g, "-").replace(/,/g, ""); return /^-?\d*\.?\d+$/.test(s) ? parseFloat(s) : null; }
function armaCamposFO(){
  var k = $("fo-sel").value;
  $("fo-form").innerHTML = FORMULA[k];
  $("fo-campos").innerHTML = CAMPOS[k].map(function(c){
    return '<div class="campo"><label for="fo-' + c[0] + '">' + ETIQ[k + "-" + c[0]] + '</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="fo-' + c[0] + '" value="' + c[1] + '"></div>';
  }).join("");
  CAMPOS[k].forEach(function(c){ $("fo-" + c[0]).addEventListener("input", pintaFO); });
  pintaFO();
}
function pintaFO(){
  var k = $("fo-sel").value, v = {}, malo = false;
  CAMPOS[k].forEach(function(c){ var x = leeNum($("fo-" + c[0]).value); $("fo-" + c[0]).classList.toggle("error", x === null); if (x === null) malo = true; v[c[0]] = x; });
  if (malo){ $("fo-salida").innerHTML = lineas([TXT.escribeNum]); return; }
  var h, r, L, u;
  function arma(L, o){ return L.map(function(s, i){ var x = F(s, o); return i === L.length - 1 ? '<span class="veredicto">' + x + '</span>' : x; }); }
  if (k === "taxi"){ u = redondea(2.25 * v.m); r = redondea(3.50 + u); h = arma(TXT.taxi, { m: S(fmt(v.m)), m2: par(v.m), u: fmt(u), r: fmt(r), d: dinero(r) }); if (v.m < 0) h.push(TXT.taxiNeg); }
  if (k === "cf"){ u = redondea(9 / 5 * v.C); r = redondea(u + 32); h = arma(TXT.cf, { C: S(fmt(v.C)), C2: par(v.C), C3: fmt(v.C), u: fmt(u), r: fmt(r) }); }
  if (k === "fc"){ var d = redondea(v.F - 32); r = redondea(5 / 9 * d); h = arma(TXT.fc, { F: S(fmt(v.F)), F2: fmt(v.F), d: fmt(d), d2: d < 0 ? "(" + fmt(d) + ")" : fmt(d), r: fmt(r), x: Math.abs(5 / 9 * d - r) > 1e-9 ? TXT.redondeado : "" }); }
  if (k === "per"){ var s = redondea(v.l + v.w); r = redondea(2 * s); h = arma(TXT.per, { l: S(fmt(v.l)), w: S(fmt(v.w)), l2: fmt(v.l), w2: fmt(v.w), s: fmt(s), r: fmt(r) }); if (v.l <= 0 || v.w <= 0) h.push(TXT.perNeg); }
  if (k === "tra"){ var s2 = redondea(v.b1 + v.b2), m = redondea(s2 / 2); r = redondea(m * v.h); h = arma(TXT.tra, { b1: S(fmt(v.b1)), b2: S(fmt(v.b2)), h: S(fmt(v.h)), b12: fmt(v.b1), b22: fmt(v.b2), h2: par(v.h), s: fmt(s2), m: fmt(m), r: fmt(r) }); }
  if (k === "int"){ var rd = v.r / 100; u = redondea(v.P * rd); r = redondea(u * v.t); h = arma(TXT.int, { P: S(fmt(v.P)), r: S(fmt(rd)), t: S(fmt(v.t)), rp: fmt(v.r), rd: fmt(rd), P2: fmt(v.P), u: fmt(u), t2: par(v.t), i: fmt(r), d: dinero(r) }); }
  $("fo-salida").innerHTML = lineas(h);
}
function genFormula(){
  var tipo = aleatorio(1, 6), Q = { opciones: [], pistas: {} };
  function ok(txt){ Q.opciones.push({ html: txt, clave: txt }); Q.correcta = txt; }
  function mal(txt, msg){ if (txt === Q.correcta || Q.pistas[txt]) return; Q.opciones.push({ html: txt, clave: txt }); Q.pistas[txt] = msg; }
  if (tipo === 1){
    var i = aleatorio(0, 2), f, tr, n;
    if (i === 0){ f = elige([2.5, 3, 3.5, 4]); tr = elige([1.75, 2, 2.25, 2.5]); n = aleatorio(3, 15); }
    else if (i === 1){ f = 5 * aleatorio(4, 10); tr = 5 * aleatorio(3, 8); n = aleatorio(2, 12); }
    else { f = 5 * aleatorio(9, 16); tr = 5 * aleatorio(7, 12); n = aleatorio(2, 6); }
    var c = redondea(f + tr * n), u = redondea(tr * n);
    Q.enun = F(TXT.fTaxi[i][1], { f: fmt(f), t: fmt(tr), n: n }); ok(dinero(c));
    mal(dinero(redondea((f + tr) * n)), TXT.mSumaAntes); mal(dinero(u), F(TXT.mFijo, { f: dinero(f) })); mal(dinero(redondea(f + tr + n)), TXT.mLetra);
    Q.bien = Q.mal = F(TXT.solTaxi, { t: fmt(tr), n: n, u: fmt(u), f: fmt(f), c: dinero(c) });
  } else if (tipo === 2){
    var C = 5 * aleatorio(-2, 8), Fv = 9 * C / 5 + 32;
    Q.enun = F(TXT.qCF, { C: ent(C) }); ok(fmt(Fv) + " °F");
    mal(fmt(9 * C / 5) + " °F", TXT.mFalta32); mal(fmt(redondea(9 / 5 * (C + 32), 1)) + " °F", TXT.m32Antes); mal(fmt(C + 32) + " °F", TXT.mFalta95);
    Q.bien = Q.mal = F(TXT.solCF, { C: par(C), u: fmt(9 * C / 5), F: fmt(Fv) });
  } else if (tipo === 3){
    var kk = aleatorio(-2, 8), Cc = 5 * kk, Ff = 9 * kk + 32;
    Q.enun = F(TXT.qFC, { F: ent(Ff) }); ok(fmt(Cc) + " °C");
    mal(fmt(redondea(5 / 9 * Ff - 32, 1)) + " °C", TXT.mParPrimero); mal(fmt(Ff - 32) + " °C", TXT.mFalta59); mal(fmt(redondea(5 / 9 * Ff, 1)) + " °C", TXT.mFaltaRestar);
    Q.bien = Q.mal = F(TXT.solFC, { F: ent(Ff), d: ent(Ff - 32), d2: par(Ff - 32), C: fmt(Cc) });
  } else if (tipo === 4){
    var l = aleatorio(6, 40) / 2, w = aleatorio(2, 12), Pp = 2 * (l + w);
    Q.enun = F(TXT.qPer, { l: fmt(l), w: w }); ok(fmt(Pp) + TXT.pulg);
    mal(fmt(2 * l + w) + TXT.pulg, TXT.mTodo2); mal(fmt(l + w) + TXT.pulg, TXT.mFalta2); mal(fmt(l * w) + TXT.pulg, TXT.mArea);
    Q.bien = Q.mal = F(TXT.solPer, { l: fmt(l), w: w, s: fmt(l + w), P: fmt(Pp) });
  } else if (tipo === 5){
    var b1 = aleatorio(3, 14), b2; do { b2 = aleatorio(4, 18); } while ((b1 + b2) % 2 || b2 === b1);
    var h = aleatorio(2, 10), A = (b1 + b2) / 2 * h;
    Q.enun = F(TXT.qTra, { b1: b1, b2: b2, h: h }); ok(fmt(A) + TXT.pies2);
    mal(fmt((b1 + b2) * h) + TXT.pies2, TXT.mFaltaMedio); mal(fmt(b1 / 2 + b2 * h) + TXT.pies2, TXT.mMedioTodo); mal(fmt((b1 + b2) / 2 + h) + TXT.pies2, TXT.mHSuma);
    Q.bien = Q.mal = F(TXT.solTra, { b1: b1, b2: b2, s: b1 + b2, m: (b1 + b2) / 2, h: h, A: fmt(A) });
  } else {
    var Pc = 100 * aleatorio(5, 50), r = aleatorio(2, 8), tt = aleatorio(2, 6), I = Pc * r / 100 * tt;
    Q.enun = F(TXT.qInt, { P: dinero(Pc), r: r, t: tt }); ok(dinero(I));
    mal(dinero(Pc * r * tt), F(TXT.mTasaDec, { r: r, rd: fmt(r / 100) })); mal(dinero(Pc * r / 100), F(TXT.mUnAno, { t: tt })); mal(dinero(Pc + I), TXT.mMonto);
    Q.bien = Q.mal = F(TXT.solInt, { P: fmt(Pc), rd: fmt(r / 100), u: fmt(Pc * r / 100), t: tt, I: dinero(I) });
  }
  return Q;
}

/* ============ Start ============ */
creaPracticaLibre("p1", genFrac);
$("su-expr").addEventListener("change", pintaSU);
["su-x", "su-a", "su-b"].forEach(function(id){ $(id).addEventListener("input", pintaSU); });
pintaSU();
creaPracticaLibre("p2", genSustituir);
$("fo-sel").addEventListener("change", armaCamposFO); armaCamposFO();
creaPracticaOM("p3", genFormula);
'''

FORMULA = {
 "taxi": "C = 3.50 + 2.25m", "cf": "F = (9/5)C + 32", "fc": "C = (5/9)(F − 32)", "per": "P = 2(l + w)",
 "tra": "A = ½(b<sub>1</sub> + b<sub>2</sub>)h", "int": "I = Prt"}
ETIQ = {
 "en": {"taxi-m": "Miles (m)", "cf-C": "Degrees Celsius (C)", "fc-F": "Degrees Fahrenheit (F)", "per-l": "Length in inches (l)", "per-w": "Width in inches (w)",
        "tra-b1": "Base b₁ in feet", "tra-b2": "Base b₂ in feet", "tra-h": "Height h in feet", "int-P": "Principal P in dollars", "int-r": "Rate r in %", "int-t": "Time t in years"},
 "es": {"taxi-m": "Millas (m)", "cf-C": "Grados Celsius (C)", "fc-F": "Grados Fahrenheit (F)", "per-l": "Largo en pulgadas (l)", "per-w": "Ancho en pulgadas (w)",
        "tra-b1": "Base b₁ en pies", "tra-b2": "Base b₂ en pies", "tra-h": "Altura h en pies", "int-P": "Capital P en dólares", "int-r": "Tasa r en %", "int-t": "Tiempo t en años"}}

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val, idc):
        return f'<div class="campo" style="flex:1;min-width:180px;" id="{idc}"><label for="{i}">{et} = <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    opts = "".join(f'<option value="{i}">{x}</option>' for i, x in enumerate(TX[B.L]["tpl"]))
    fopts = [("taxi", t("Taxi", "Taxi")), ("cf", t("Celsius to Fahrenheit", "Celsius a Fahrenheit")), ("fc", t("Fahrenheit to Celsius", "Fahrenheit a Celsius")),
             ("per", t("Perimeter of a rectangle", "Perímetro del rectángulo")), ("tra", t("Area of a trapezoid", "Área del trapecio")), ("int", t("Simple interest", "Interés simple"))]
    fsel = "".join(f'<option value="{k}">{nm}: {FORMULA[k].replace("<sub>1</sub>", "₁").replace("<sub>2</sub>", "₂")}</option>' for k, nm in fopts)
    nota_q = t("Type an integer or a fraction like −7/2, in simplest form. If it is negative, start with the minus sign.", "Escriba un entero o una fracción como −7/2, simplificada. Si es negativa, empiece con el signo menos.")
    def libre_q(pid, titulo):
        return B.libre_e(pid, titulo).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota_q)
    mods = [
     (t("fractions", "fracciones"), t("PEMDAS with fractions", "PEMDAS con fracciones"),
      f'''      <p>{t("Fractions do not change the order. To add or subtract, find a common denominator; to multiply, multiply straight across; to divide, multiply by the reciprocal. And the parentheses in (a/b)<sup>2</sup> raise the whole fraction.", "Las fracciones no cambian el orden. Para sumar o restar se busca un denominador común; para multiplicar, numerador por numerador y denominador por denominador; para dividir, se multiplica por el recíproco. Y el paréntesis de (a/b)<sup>2</sup> eleva la fracción completa.")}</p>
{libre_q("p1", t("Practice: fractions with PEMDAS", "Practique: fracciones con PEMDAS"))}'''),
     (t("substitute", "sustituir"), t("Substitute and evaluate", "Sustituir y evaluar"),
      f'''      <p>{t("Rule 1: always substitute inside parentheses; they protect the sign. Rule 2: a letter next to a number means multiplication: 3x = 3 × x.", "Regla 1: sustituya siempre entre paréntesis; el paréntesis protege el signo. Regla 2: la letra pegada a un número indica multiplicación: 3x = 3 × x.")}</p>
      <h3>{t("Substitute and see the steps", "Sustituya y vea los pasos")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo" style="flex:1;min-width:220px;"><label for="su-expr">{t("Expression", "Expresión")}</label><select id="su-expr">{opts}</select></div>
        </div>
        <div class="campos" style="margin-top:10px;">
          {deslizador("su-x", "x", -6, 6, -2, "su-cx")}
          {deslizador("su-a", "a", -6, 6, 5, "su-ca")}
          {deslizador("su-b", "b", -6, 6, -3, "su-cb")}
        </div>
        <div class="salida" id="su-salida" aria-live="polite"></div>
      </div>
{libre_q("p2", t("Practice: substitute and evaluate", "Practique: sustituir y evaluar"))}'''),
     (t("formulas", "formulas"), t("Formulas in context", "Fórmulas en contexto"),
      f'''      <p>{t("Write the formula, write the value of each letter, substitute in parentheses, apply PEMDAS, and answer with the unit.", "Escriba la fórmula, anote el valor de cada letra, sustituya entre paréntesis, aplique PEMDAS y responda con la unidad.")}</p>
      <h3>{t("Try the formula", "Pruebe la fórmula")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo" style="flex:1;min-width:240px;"><label for="fo-sel">{t("Formula", "Fórmula")}</label><select id="fo-sel">{fsel}</select></div>
        </div>
        <div class="formula-sel" id="fo-form"></div>
        <div class="campos" id="fo-campos" style="margin-top:8px;"></div>
        <div class="salida" id="fo-salida" aria-live="polite"></div>
      </div>
{B.om("p3", t("Practice: GED-style questions", "Practique: preguntas tipo GED"))}''')]
    js = ("var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\nvar FORMULA = " + json.dumps(FORMULA, ensure_ascii=False)
          + ";\nvar ETIQ = " + json.dumps(ETIQ[B.L], ensure_ascii=False) + ";\n" + LOGICA)
    estilo = ".sust{color:#0d47a1;font-weight:700;} .formula-sel{font-size:22px;font-weight:700;text-align:center;margin:12px 0;color:var(--tema-d);}"
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=estilo, scripts=("/math/integers.js", "/math/pemdas.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "PEMDAS en expresiones con fracciones y contexto algebraico")
