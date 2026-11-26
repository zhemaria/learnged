"""Level 2 · Lesson 3.2 · PEMDAS with powers, roots, fractions, and signs — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import pasos_panel, fr, frn

B.NIVEL = 2
N = "3-2"
TEMA = ("The full order of operations (PEMDAS)", "PEMDAS completo")
TIT = ("PEMDAS with powers, roots, fractions, and signs", "PEMDAS con potencias, raíces, fracciones y signos")

def hl(x):
    return f'<mark style="background:#fff3e0;outline:2px solid #bf360c;border-radius:4px;padding:0 3px">{x}</mark>'
def rz(x):
    return f'√<span style="border-top:2px solid currentColor;padding:0 2px">{x}</span>'
def frx(a, b):
    """Barra de fracción con expresiones."""
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{a}</span><span class="fb2">{b}</span></span><span class="cap-oculto">({a}) ÷ ({b})</span>'

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 3.1 you learned the four levels of PEMDAS and worked nested grouping symbols with positive whole numbers. This lesson brings in every tool from Level 2: powers, square roots, fractions, and integers. The order does not change; only the ingredients are richer.",
"En la Lección 3.1 aprendió los cuatro niveles de PEMDAS y resolvió agrupadores anidados con enteros positivos. Esta lección incorpora todas las herramientas del Nivel 2: potencias, raíces cuadradas, fracciones y enteros con signo. El orden no cambia; solo cambian los ingredientes.")}</p>
<p>{t("In PEMDAS, the E for \"exponents\" also includes <strong>roots</strong>. Both share the second level: right after the grouping symbols, and before any multiplication, division, addition, or subtraction.", "En PEMDAS, la E de «exponentes» incluye también las <strong>raíces</strong>. Las dos comparten el segundo nivel: justo después de los agrupadores y antes de cualquier multiplicación, división, suma o resta.")}</p>
{ejemplo(t(f"Example: 3 + {rz(25)} × 2", f"Ejemplo: 3 + {rz(25)} × 2"),
  [("1", "E.", t(f"The root shares the level of exponents, so it goes first: {hl(rz(25))} = 5 → 3 + 5 × 2.", f"La raíz comparte nivel con los exponentes, así que va primero: {hl(rz(25))} = 5 → 3 + 5 × 2.")),
   ("2", "MD.", t(f"Multiply before adding: {hl('5 × 2')} = 10 → 3 + 10.", f"Se multiplica antes de sumar: {hl('5 × 2')} = 10 → 3 + 10.")),
   ("✓", "AS.", "3 + 10 = <strong>13</strong>")])}
{ejemplo(t(f"Example: 2<sup>3</sup> + {rz('16 + 9')}", f"Ejemplo: 2<sup>3</sup> + {rz('16 + 9')}"),
  [("1", "P.", t(f"Under the radical sign, add first: {hl('16 + 9')} = 25 → 2<sup>3</sup> + {rz(25)}.", f"Bajo la raíz, primero se suma: {hl('16 + 9')} = 25 → 2<sup>3</sup> + {rz(25)}.")),
   ("2", "E.", t(f"The power and the root: 2<sup>3</sup> = 8 and {rz(25)} = 5 → 8 + 5.", f"La potencia y la raíz: 2<sup>3</sup> = 8 y {rz(25)} = 5 → 8 + 5.")),
   ("✓", "AS.", "8 + 5 = <strong>13</strong>")])}
{caja("tip", t("The radical sign groups", "El signo radical agrupa"), t(f"<p>Everything under the √ sign is inside <strong>invisible parentheses</strong>. That is why {rz('16 + 9')} is not the same as {rz(16)} + {rz(9)}. The first one is {rz(25)} = 5; the second is 4 + 3 = 7.</p>",
f"<p>Todo lo que está bajo el signo √ está dentro de un <strong>paréntesis invisible</strong>. Por eso {rz('16 + 9')} no es lo mismo que {rz(16)} + {rz(9)}. El primero es {rz(25)} = 5; el segundo es 4 + 3 = 7.</p>"))}
{practica("p1", t("Practice 1 — A root in the middle", "Práctica 1 — Una raíz en medio"), t(f"What is 4 + {rz(36)} × 2?", f"¿Cuánto es 4 + {rz(36)} × 2?"),
          [("a", "20"), ("b", "16"), ("c", "8"), ("d", "76")])}
{practica("p2", t("Practice 2 — Under the root", "Práctica 2 — Bajo la raíz"), t(f"What is 5<sup>2</sup> − {rz('9 + 16')}?", f"¿Cuánto es 5<sup>2</sup> − {rz('9 + 16')}?"),
          [("a", "18"), ("b", "28"), ("c", "5"), ("d", "20")])}
{enlace(n, t("powers-roots", "potencias-raices"), t("powers and roots", "potencias y raíces"), t("Solve expressions where the radical sign groups like invisible parentheses.", "Resuelva expresiones en las que el radical agrupa como un paréntesis invisible."))}'''

    s2 = f'''<p>{t("Like the radical sign, the <strong>fraction bar</strong> groups what is above it and what is below it. Work out the numerator and the denominator separately, and divide at the end.", "Igual que el radical, la <strong>barra de fracción</strong> agrupa lo que está arriba y lo que está abajo. El numerador y el denominador se resuelven por separado, y al final se divide.")}</p>
{ejemplo(t("Example:", "Ejemplo:") + " " + frx("3<sup>2</sup> + 7", "2 × 4"),
  [("1", t("Numerator.", "Numerador."), t("3<sup>2</sup> + 7 = 9 + 7 = 16 (E before A).", "3<sup>2</sup> + 7 = 9 + 7 = 16 (E antes que A).")),
   ("2", t("Denominator.", "Denominador."), "2 × 4 = 8."),
   ("✓", t("Divide.", "Divida."), "16 ÷ 8 = <strong>2</strong>")])}
{caja("ojo", t("On one line or on the calculator", "En una línea o en la calculadora"), t("<p>When you write a fraction on one line, put <strong>parentheses</strong> around the numerator and around the denominator: (3<sup>2</sup> + 7) ÷ (2 × 4). Without them, the calculator reads 3<sup>2</sup> + 7 ÷ 2 × 4, which gives 23, a completely different answer.</p>",
"<p>Al escribir una fracción en una sola línea, ponga <strong>paréntesis</strong> alrededor del numerador y del denominador: (3<sup>2</sup> + 7) ÷ (2 × 4). Sin ellos, la calculadora lee 3<sup>2</sup> + 7 ÷ 2 × 4, que da 23, un resultado completamente distinto.</p>"))}
{calc(t("Fractions with expressions on the calculator", "Fracciones con expresiones en la calculadora"), t(f"""<p>Type the parentheses: {T("(")} {T("3")} {T("x<sup>2</sup>")} {T("+")} {T("7")} {T(")")} {T("÷")} {T("(")} {T("2")} {T("×")} {T("4")} {T(")")} {T("enter")}. The screen shows 2.</p>""",
f"""<p>Escriba los paréntesis: {T("(")} {T("3")} {T("x<sup>2</sup>")} {T("+")} {T("7")} {T(")")} {T("÷")} {T("(")} {T("2")} {T("×")} {T("4")} {T(")")} {T("enter")}. La pantalla muestra 2.</p>"""))}
{practica("p3", t("Practice 3 — The fraction bar", "Práctica 3 — La barra de fracción"), t("What is", "¿Cuánto es") + " " + frx("2<sup>2</sup> + 6", "5 − 3") + "?",
          [("a", "5"), ("b", "8"), ("c", "10"), ("d", "3")])}
{enlace(n, t("fraction-bar", "barra-fraccion"), t("the fraction bar as a grouping symbol", "la barra de fracción como agrupador"), t("Work out the numerator and the denominator separately and divide at the end.", "Resuelva numerador y denominador por separado y divida al final."))}'''

    s3 = f'''<p>{t("When minus signs appear, the key is to tell when the sign is part of the number and when it means a subtraction or an opposite.", "Cuando aparecen signos negativos, lo importante es distinguir cuándo el signo es parte del número y cuándo indica una resta o un opuesto.")}</p>
{ejemplo(t("Example: −6 + 2 × (−4)", "Ejemplo: −6 + 2 × (−4)"),
  [("1", "MD.", t(f"Multiplication before addition. Different signs, negative: {hl('2 × (−4)')} = −8 → −6 + (−8).", f"La multiplicación antes que la suma. Signos distintos, negativo: {hl('2 × (−4)')} = −8 → −6 + (−8).")),
   ("✓", "AS.", t("Same signs (both negative): −6 + (−8) = <strong>−14</strong>", "Mismo signo (los dos negativos): −6 + (−8) = <strong>−14</strong>"))])}
<h3>{t("A negative base with an exponent", "La base negativa con exponente")}</h3>
<p>{t("The difference between (−5)<sup>2</sup> and −5<sup>2</sup> is one of the finest points of PEMDAS. Look at it carefully.", "La diferencia entre (−5)<sup>2</sup> y −5<sup>2</sup> es uno de los detalles más finos de PEMDAS. Mírela con cuidado.")}</p>
{tabla(t("With and without parentheses", "Con paréntesis y sin ellos"), t("Two expressions that look alike: (−5) squared and the opposite of 5 squared", "Dos expresiones casi iguales: (−5) al cuadrado y el opuesto de 5 al cuadrado"),
       [t("You write", "Se escribe"), t("It means", "Quiere decir"), t("Value", "Valor")],
       [["(−5)<sup>2</sup>", t("square the number −5: the parentheses put the sign in the base", "elevar al cuadrado el número −5: el paréntesis mete el signo en la base"), "(−5) × (−5) = <strong>25</strong>"],
        ["−5<sup>2</sup>", t("the opposite of 5<sup>2</sup>: the exponent applies only to the 5", "el opuesto de 5<sup>2</sup>: el exponente solo afecta al 5"), "−(5 × 5) = <strong>−25</strong>"]])}
{caja("tip", t("The rule", "La regla"), t("<p>An exponent applies only to what is right before it. With no parentheses, the minus sign is out of the exponent's reach: E goes first, and the minus sign is applied after.</p>",
"<p>El exponente afecta solo a lo que tiene justo antes. Sin paréntesis, el signo menos queda fuera de su alcance: primero va la E y después se aplica el signo.</p>"))}
{calc(t("Negative bases on the calculator", "Bases negativas en la calculadora"), t(f"""<p>For (−5)<sup>2</sup>, type the parentheses: {T("(")} {T("(−)")} {T("5")} {T(")")} {T("x<sup>2</sup>")} {T("enter")} gives 25. If you type {T("(−)")} {T("5")} {T("x<sup>2</sup>")} {T("enter")}, the calculator reads −5<sup>2</sup> and gives −25.</p>""",
f"""<p>Para (−5)<sup>2</sup>, escriba los paréntesis: {T("(")} {T("(−)")} {T("5")} {T(")")} {T("x<sup>2</sup>")} {T("enter")} da 25. Si escribe {T("(−)")} {T("5")} {T("x<sup>2</sup>")} {T("enter")}, la calculadora lee −5<sup>2</sup> y da −25.</p>"""))}
{practica("p4", t("Practice 4 — With and without parentheses", "Práctica 4 — Con paréntesis y sin ellos"), t("What is −4<sup>2</sup> + 20?", "¿Cuánto es −4<sup>2</sup> + 20?"),
          [("a", "36"), ("b", "4"), ("c", "12"), ("d", "−36")])}
{enlace(n, t("negatives", "negativos"), t("PEMDAS with negative numbers", "PEMDAS con negativos"), t("Compare (−5)<sup>2</sup> with −5<sup>2</sup> and practice expressions with signs.", "Compare (−5)<sup>2</sup> con −5<sup>2</sup> y practique expresiones con signos."))}'''

    s4 = f'''<p>{t("An expression that brings it all together uses tools from all three topics of the level in one calculation. You solve it exactly like the others: PEMDAS, step by step, copying each line.", "Una expresión integradora usa en un solo cálculo herramientas de los tres temas del nivel. Se resuelve exactamente igual que las anteriores: PEMDAS, paso a paso, copiando cada línea.")}</p>
{ejemplo(t("Example:", "Ejemplo:") + f" (−3)<sup>2</sup> + {rz(64)} ÷ 2 − {fr(5, 2)} × 4",
  [("1", "E.", t(f"The power and the root: (−3)<sup>2</sup> = 9 and {rz(64)} = 8 → 9 + 8 ÷ 2 − 5/2 × 4.", f"La potencia y la raíz: (−3)<sup>2</sup> = 9 y {rz(64)} = 8 → 9 + 8 ÷ 2 − 5/2 × 4.")),
   ("2", "MD.", t("From left to right: 8 ÷ 2 = 4, and 5/2 × 4 = 20/2 = 10 → 9 + 4 − 10.", "De izquierda a derecha: 8 ÷ 2 = 4, y 5/2 × 4 = 20/2 = 10 → 9 + 4 − 10.")),
   ("3", "AS.", t("From left to right: 9 + 4 = 13; 13 − 10 = 3.", "De izquierda a derecha: 9 + 4 = 13; 13 − 10 = 3.")),
   ("✓", t("Result.", "Resultado."), "<strong>3</strong>")])}
{caja("tip", t("Check someone else's work", "Revise el trabajo de otro"), t("<p>A good way to learn the order is to find the mistake in someone else's work. The practice page has an activity called <em>The order referee</em>: you read a solution and decide in which step, if any, the order was broken.</p>",
"<p>Una buena manera de aprender el orden es encontrar el error en el trabajo de otro. La página de práctica tiene una actividad llamada <em>El árbitro del orden</em>: usted lee una resolución y decide en qué paso, si lo hay, se rompió el orden.</p>"))}
{practica("p5", t("Practice 5 — Bringing it together", "Práctica 5 — Integradora"), t(f"What is (−4)<sup>2</sup> − 10 ÷ 2?", f"¿Cuánto es (−4)<sup>2</sup> − 10 ÷ 2?"),
          [("a", "3"), ("b", "11"), ("c", "−21"), ("d", "6")])}
{practica("p6", t("Practice 6 — Find the mistake", "Práctica 6 — Busque el error"), t("Someone solved 10 − 2 × 3 like this: 10 − 2 = 8, then 8 × 3 = 24. What went wrong?", "Alguien resolvió 10 − 2 × 3 así: 10 − 2 = 8, después 8 × 3 = 24. ¿Qué salió mal?"),
          [("a", t("Nothing: 24 is right.", "Nada: 24 es correcto.")), ("b", t("The subtraction was done before the multiplication. The answer is 4.", "Se restó antes de multiplicar. El resultado es 4.")), ("c", t("You must always work from left to right. The answer is 24.", "Siempre se trabaja de izquierda a derecha. El resultado es 24."))])}
{enlace(n, t("referee", "arbitro"), t("the order referee", "el árbitro del orden de las operaciones"), t("Check other people's solutions and find the wrong step, if there is one.", "Revise resoluciones ajenas y encuentre el paso equivocado, si lo hay."))}'''

    secciones = [("s-" + t("powers-roots", "potencias-raices"), t("PEMDAS with powers and roots", "PEMDAS con potencias y raíces"), s1),
                 ("s-" + t("fraction-bar", "barra-fraccion"), t("The fraction bar groups", "La barra de fracción como agrupador"), s2),
                 ("s-" + t("negatives", "negativos"), t("PEMDAS with negative numbers", "PEMDAS con enteros negativos"), s3),
                 ("s-" + t("bring-together", "integradoras"), t("Bringing it all together", "Expresiones integradoras"), s4)]

    lesson = {"next": t("Lesson 3.3", "Lección 3.3"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You added 4 + 6 first. Multiply before adding.", "Sumó 4 + 6 primero. Se multiplica antes de sumar."), "c": t("The root of 36 is 6, then 6 × 2 = 12. Add 4.", "La raíz de 36 es 6, después 6 × 2 = 12. Sume 4."), "d": t("Find the square root of 36 first: it is 6, not 36.", "Primero saque la raíz de 36: es 6, no 36.")},
             "right": t("√36 = 6; 6 × 2 = 12; 4 + 12 = 16.", "√36 = 6; 6 × 2 = 12; 4 + 12 = 16."), "solution": t("E: √36 = 6. MD: 6 × 2 = 12. AS: 4 + 12 = 16.", "E: √36 = 6. MD: 6 × 2 = 12. AS: 4 + 12 = 16.")},
      "p2": {"ok": "d", "hints": {"a": t("You took two roots: √9 + √16 = 7. Add under the root first.", "Sacó dos raíces: √9 + √16 = 7. Primero se suma bajo la raíz."), "b": t("Subtract the root, do not add it.", "Se resta la raíz, no se suma."), "c": t("5 is the root. Now subtract it from 5<sup>2</sup> = 25.", "5 es la raíz. Ahora réstela de 5<sup>2</sup> = 25.")},
             "right": t("9 + 16 = 25; √25 = 5; 25 − 5 = 20.", "9 + 16 = 25; √25 = 5; 25 − 5 = 20."), "solution": t("Under the root: 9 + 16 = 25. E: 5<sup>2</sup> = 25 and √25 = 5. AS: 25 − 5 = 20.", "Bajo la raíz: 9 + 16 = 25. E: 5<sup>2</sup> = 25 y √25 = 5. AS: 25 − 5 = 20.")},
      "p3": {"ok": "a", "hints": {"b": t("You did not divide. The fraction bar means numerator ÷ denominator.", "No dividió. La barra de fracción quiere decir numerador ÷ denominador."), "c": t("Numerator: 2<sup>2</sup> + 6 = 4 + 6 = 10. Now divide by the denominator.", "Numerador: 2<sup>2</sup> + 6 = 4 + 6 = 10. Ahora divida entre el denominador."), "d": t("Check the numerator: 2<sup>2</sup> + 6 = 4 + 6 = 10.", "Revise el numerador: 2<sup>2</sup> + 6 = 4 + 6 = 10.")},
             "right": t("(4 + 6) ÷ (5 − 3) = 10 ÷ 2 = 5.", "(4 + 6) ÷ (5 − 3) = 10 ÷ 2 = 5."), "solution": t("Numerator: 2<sup>2</sup> + 6 = 10. Denominator: 5 − 3 = 2. Divide: 10 ÷ 2 = 5.", "Numerador: 2<sup>2</sup> + 6 = 10. Denominador: 5 − 3 = 2. Se divide: 10 ÷ 2 = 5.")},
      "p4": {"ok": "b", "hints": {"a": t("−4<sup>2</sup> has no parentheses: it is −16, not 16.", "−4<sup>2</sup> no tiene paréntesis: es −16, no 16."), "c": t("4<sup>2</sup> = 16, not 8.", "4<sup>2</sup> = 16, no 8."), "d": t("Check the sign of 20: it is added.", "Revise el signo del 20: se suma.")},
             "right": t("−4<sup>2</sup> = −16; −16 + 20 = 4.", "−4<sup>2</sup> = −16; −16 + 20 = 4."), "solution": t("Without parentheses, the exponent applies only to the 4: −4<sup>2</sup> = −16. Then −16 + 20 = 4.", "Sin paréntesis, el exponente afecta solo al 4: −4<sup>2</sup> = −16. Después −16 + 20 = 4.")},
      "p5": {"ok": "b", "hints": {"a": t("Check the division: 10 ÷ 2 = 5, then 16 − 5.", "Revise la división: 10 ÷ 2 = 5, después 16 − 5."), "c": t("(−4)<sup>2</sup> has parentheses: it is 16, positive.", "(−4)<sup>2</sup> tiene paréntesis: es 16, positivo."), "d": t("You subtracted 16 − 10 first. Divide first.", "Restó 16 − 10 primero. Primero se divide.")},
             "right": t("(−4)<sup>2</sup> = 16; 10 ÷ 2 = 5; 16 − 5 = 11.", "(−4)<sup>2</sup> = 16; 10 ÷ 2 = 5; 16 − 5 = 11."), "solution": t("E: (−4)<sup>2</sup> = 16. MD: 10 ÷ 2 = 5. AS: 16 − 5 = 11.", "E: (−4)<sup>2</sup> = 16. MD: 10 ÷ 2 = 5. AS: 16 − 5 = 11.")},
      "p6": {"ok": "b", "hints": {"a": t("Check the order: is there a multiplication that should go before the subtraction?", "Revise el orden: ¿hay una multiplicación que deba ir antes que la resta?"), "c": t("Left to right is only for operations on the same level. Multiplication is a higher level than subtraction.", "De izquierda a derecha es solo para operaciones del mismo nivel. La multiplicación está en un nivel más alto que la resta.")},
             "right": t("Multiply first: 2 × 3 = 6; 10 − 6 = 4.", "Primero se multiplica: 2 × 3 = 6; 10 − 6 = 4."), "solution": t("Multiplication comes before subtraction: 2 × 3 = 6, then 10 − 6 = 4. The mistake was subtracting first.", "La multiplicación va antes que la resta: 2 × 3 = 6, después 10 − 6 = 4. El error fue restar primero.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("You added 2 + 7 first. Find the root, then multiply.", "Sumó 2 + 7 primero. Saque la raíz y después multiplique."), "b": t("√49 = 7, not 49.", "√49 = 7, no 49."), "d": t("Check: 7 × 3 = 21, then 2 + 21.", "Revise: 7 × 3 = 21, después 2 + 21.")}, "solution": t("√49 = 7; 7 × 3 = 21; 2 + 21 = 23.", "√49 = 7; 7 × 3 = 21; 2 + 21 = 23.")},
      "B": {"ok": "a", "hints": {"b": t("√36 + √64 = 6 + 8 = 14. Add under the root first.", "√36 + √64 = 6 + 8 = 14. Primero se suma bajo la raíz."), "c": t("36 + 64 = 100. Now find the square root.", "36 + 64 = 100. Ahora saque la raíz cuadrada."), "d": t("Half of 100 is not its root.", "La mitad de 100 no es su raíz.")}, "solution": t("36 + 64 = 100; √100 = 10.", "36 + 64 = 100; √100 = 10.")},
      "C": {"ok": "d", "hints": {"a": t("You divided only the 2. The fraction bar groups the whole numerator.", "Dividió solo el 2. La barra de fracción agrupa todo el numerador."), "b": t("Numerator: 18 + 2 = 20. Denominator: 2<sup>2</sup> = 4.", "Numerador: 18 + 2 = 20. Denominador: 2<sup>2</sup> = 4."), "c": t("The denominator is 2<sup>2</sup> = 4, not 2.", "El denominador es 2<sup>2</sup> = 4, no 2.")}, "solution": t("(18 + 2) ÷ 2<sup>2</sup> = 20 ÷ 4 = 5.", "(18 + 2) ÷ 2<sup>2</sup> = 20 ÷ 4 = 5.")},
      "D": {"ok": "b", "hints": {"a": t("With parentheses, (−5)<sup>2</sup> = 25, positive.", "Con paréntesis, (−5)<sup>2</sup> = 25, positivo."), "c": t("That is (−5) × 2.", "Eso es (−5) × 2."), "d": t("That is 5 × 2.", "Eso es 5 × 2.")}, "solution": t("(−5)<sup>2</sup> = (−5) × (−5) = 25.", "(−5)<sup>2</sup> = (−5) × (−5) = 25.")},
      "E": {"ok": "a", "hints": {"b": t("Without parentheses, the exponent applies only to the 5: −5<sup>2</sup> = −25.", "Sin paréntesis, el exponente afecta solo al 5: −5<sup>2</sup> = −25."), "c": t("That is −5 × 2.", "Eso es −5 × 2."), "d": t("That is 5 × 2.", "Eso es 5 × 2.")}, "solution": t("−5<sup>2</sup> = −(5 × 5) = −25.", "−5<sup>2</sup> = −(5 × 5) = −25.")},
      "F": {"ok": "c", "hints": {"a": t("Check the sign: 3 × (−4) is negative.", "Revise el signo: 3 × (−4) es negativo."), "b": t("You added −2 + 3 first. Multiply first.", "Sumó −2 + 3 primero. Primero se multiplica."), "d": t("3 × (−4) = −12. Then −2 + (−12): same signs.", "3 × (−4) = −12. Después −2 + (−12): mismo signo.")}, "solution": t("3 × (−4) = −12; −2 + (−12) = −14.", "3 × (−4) = −12; −2 + (−12) = −14.")},
      "G": {"ok": "d", "hints": {"a": t("You subtracted 9 − 6 first. Divide first: 6 ÷ 2.", "Restó 9 − 6 primero. Primero divida: 6 ÷ 2."), "b": t("(−3)<sup>2</sup> = 9, not −9.", "(−3)<sup>2</sup> = 9, no −9."), "c": t("Check: 9 − 3 = 6.", "Revise: 9 − 3 = 6.")}, "solution": t("(−3)<sup>2</sup> = 9; 6 ÷ 2 = 3; 9 − 3 = 6.", "(−3)<sup>2</sup> = 9; 6 ÷ 2 = 3; 9 − 3 = 6.")},
      "H": {"ok": "b", "hints": {"a": t("Without parentheses the calculator reads 12 + 8 ÷ 4 = 14.", "Sin paréntesis la calculadora lee 12 + 8 ÷ 4 = 14."), "c": t("The fraction bar groups both parts: put parentheses around each one.", "La barra de fracción agrupa las dos partes: ponga paréntesis alrededor de cada una."), "d": t("Only the numerator has parentheses here.", "Aquí solo el numerador tiene paréntesis.")}, "solution": t("(12 + 8) ÷ 4 keeps the meaning of the fraction: 20 ÷ 4 = 5.", "(12 + 8) ÷ 4 conserva el sentido de la fracción: 20 ÷ 4 = 5.")}
     }}

    quiz = [
     ("A", t(f"What is 2 + {rz(49)} × 3?", f"¿Cuánto es 2 + {rz(49)} × 3?"), [("a", "27"), ("b", "149"), ("c", "23"), ("d", "21")]),
     ("B", t(f"What is {rz('36 + 64')}?", f"¿Cuánto es {rz('36 + 64')}?"), [("a", "10"), ("b", "14"), ("c", "100"), ("d", "50")]),
     ("C", t("What is", "¿Cuánto es") + " " + frx("18 + 2", "2<sup>2</sup>") + "?", [("a", "19"), ("b", "4"), ("c", "10"), ("d", "5")]),
     ("D", t("What is (−5)<sup>2</sup>?", "¿Cuánto es (−5)<sup>2</sup>?"), [("a", "−25"), ("b", "25"), ("c", "−10"), ("d", "10")]),
     ("E", t("What is −5<sup>2</sup>?", "¿Cuánto es −5<sup>2</sup>?"), [("a", "−25"), ("b", "25"), ("c", "−10"), ("d", "10")]),
     ("F", t("What is −2 + 3 × (−4)?", "¿Cuánto es −2 + 3 × (−4)?"), [("a", "10"), ("b", "−4"), ("c", "−14"), ("d", "−10")]),
     ("G", t("What is (−3)<sup>2</sup> − 6 ÷ 2?", "¿Cuánto es (−3)<sup>2</sup> − 6 ÷ 2?"), [("a", "1.5"), ("b", "−12"), ("c", "3"), ("d", "6")]),
     ("H", t("How do you write", "¿Cómo se escribe") + " " + frx("12 + 8", "4") + " " + t("on one line so the calculator gets it right?", "en una sola línea para que la calculadora lo haga bien?"), [("a", "12 + 8 ÷ 4"), ("b", "(12 + 8) ÷ 4"), ("c", "12 + (8 ÷ 4)"), ("d", "12 + 8 ÷ (4)")])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("The same order with all the tools of Level 2: roots and fraction bars that group, and negative numbers with exponents.", "El mismo orden con todas las herramientas del Nivel 2: raíces y barras de fracción que agrupan, y números negativos con exponentes."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Place</strong> powers and roots on the second level of PEMDAS.", "<strong>Ubicar</strong> las potencias y las raíces en el segundo nivel de PEMDAS."),
         t("<strong>Use</strong> the radical sign and the fraction bar as grouping symbols.", "<strong>Usar</strong> el signo radical y la barra de fracción como agrupadores."),
         t("<strong>Tell</strong> (−a)<sup>2</sup> from −a<sup>2</sup>.", "<strong>Distinguir</strong> (−a)<sup>2</sup> de −a<sup>2</sup>."),
         t("<strong>Solve</strong> expressions that combine integers, fractions, powers, and roots.", "<strong>Resolver</strong> expresiones que combinan enteros, fracciones, potencias y raíces."),
         t("<strong>Find</strong> the mistake in a solution that breaks the order.", "<strong>Encontrar</strong> el error en una resolución que rompe el orden.")],
        secciones,
        (t("Write and solve five expressions with powers and roots, five with a fraction bar, five with negative numbers (include (−a)<sup>2</sup> and −a<sup>2</sup>), and five that bring everything together. Then check two of them on the calculator, with the parentheses in the right places.",
           "Escriba y resuelva cinco expresiones con potencias y raíces, cinco con barra de fracción, cinco con números negativos (incluya (−a)<sup>2</sup> y −a<sup>2</sup>) y cinco integradoras. Después compruebe dos en la calculadora, con los paréntesis en su lugar."),
         t("Ask someone to solve 10 − 2 × 3 and −3<sup>2</sup> without a calculator. Compare their answers with the order of operations, and explain the right answers to them.",
           "Pídale a alguien que resuelva 10 − 2 × 3 y −3<sup>2</sup> sin calculadora. Compare sus respuestas con el orden de las operaciones y explíquele los resultados correctos.")),
        quiz,
        t("Self-check checklist for PEMDAS with powers, roots, fractions, and signs", "Lista de autoevaluación de PEMDAS con potencias, raíces, fracciones y signos"),
        t("Self-check checklist: skills for PEMDAS with powers, roots, fractions, and signs", "Lista de autoevaluación: destrezas de PEMDAS con potencias, raíces, fracciones y signos"),
        [(t("Powers and roots", "Potencias y raíces"), t("I find them on the second level and treat the root as a grouping symbol.", "Las resuelvo en el segundo nivel y trato la raíz como agrupador."), t("I find them, but sometimes I take the root of each part.", "Las resuelvo, pero a veces saco la raíz de cada parte."), t("I leave them for the end.", "Las dejo para el final.")),
         (t("The fraction bar", "La barra de fracción"), t("I work out the numerator and the denominator, and write the parentheses on the calculator.", "Resuelvo numerador y denominador, y escribo los paréntesis en la calculadora."), t("I work it out, but I forget the parentheses on one line.", "La resuelvo, pero olvido los paréntesis en una línea."), t("I divide only part of the numerator.", "Divido solo una parte del numerador.")),
         (t("Negative numbers", "Números negativos"), t("I tell (−a)<sup>2</sup> from −a<sup>2</sup> every time.", "Distingo (−a)<sup>2</sup> de −a<sup>2</sup> siempre."), t("I get the signs right, but −a<sup>2</sup> confuses me.", "Acierto los signos, pero −a<sup>2</sup> me confunde."), t("I make sign mistakes in most expressions.", "Me equivoco en los signos en la mayoría de las expresiones.")),
         (t("Finding mistakes", "Encontrar errores"), t("I find the wrong step and explain it.", "Encuentro el paso equivocado y lo explico."), t("I see that the answer is wrong, but not where.", "Veo que el resultado está mal, pero no dónde."), t("I cannot tell if a solution is right.", "No sé decir si una resolución está bien."))],
        t("<p>You added powers, roots, fraction bars, and negative numbers to PEMDAS. The radical sign and the fraction bar group like invisible parentheses, and the exponent reaches only what is right before it.</p>\n<p>In <strong>Lesson 3.3 · PEMDAS with fractions and in algebra</strong> you will finish Topic 3: you will operate with fractions inside PEMDAS and go from numbers to letters, evaluating expressions and GED formulas.</p>",
          "<p>Sumó a PEMDAS las potencias, las raíces, las barras de fracción y los números negativos. El radical y la barra de fracción agrupan como paréntesis invisibles, y el exponente alcanza solo lo que tiene justo antes.</p>\n<p>En la <strong>Lección 3.3 · PEMDAS en expresiones con fracciones y contexto algebraico</strong> terminará el Tema 3: operará con fracciones dentro de PEMDAS y pasará de los números a las letras, evaluando expresiones y fórmulas del GED.</p>"),
        ("3-3", ("", t("Lesson 3.3 · PEMDAS with fractions and in algebra", "Lección 3.3 · PEMDAS en expresiones con fracciones y contexto algebraico"))),
        [(t("radical sign", "signo radical"), t("The symbol √. What is under it is grouped, as if in parentheses.", "El símbolo √. Lo que está debajo queda agrupado, como entre paréntesis.")),
         (t("fraction bar", "barra de fracción"), t("The line of a fraction. It groups the numerator and the denominator and means division.", "La raya de una fracción. Agrupa el numerador y el denominador y quiere decir división.")),
         (t("base", "base"), t("The number that is raised to a power. In (−5)<sup>2</sup> the base is −5; in −5<sup>2</sup> it is 5.", "El número que se eleva a una potencia. En (−5)<sup>2</sup> la base es −5; en −5<sup>2</sup> es 5.")),
         (t("expression", "expresión"), t("Numbers and operations written together, like (−3)<sup>2</sup> + 8 ÷ 2.", "Números y operaciones escritos juntos, como (−3)<sup>2</sup> + 8 ÷ 2."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "conPar": "<strong>With parentheses:</strong> {e} = {m} = <strong>{r}</strong>. The base is −{b}; {s}",
  "impar": "odd exponent, negative.", "par": "even exponent, positive.",
  "sinPar": "<strong>Without parentheses:</strong> {e} = −({m}) = <strong>{r}</strong>. The base is {b}, and the minus sign is applied at the end.",
  "coinciden": "With an odd exponent the two are equal, but for different reasons.", "opuestos": "With an even exponent they are opposites: that is why the parentheses matter.",
  "arbitroQ": "Check this solution of {e}:", "pasoN": "Step {n}", "ninguno": "None: it is solved correctly",
  "bienSinError": "Every step follows PEMDAS; the answer {r} is right.", "errorEn": "The mistake is in step {n}. {x} The right answer is {r}.",
  "pistaArbitro": "Check each step: does it do the operation with the highest priority?",
  "explica": { "izqder": "An addition or subtraction was done before a multiplication or division.", "potmul": "A power was found by multiplying the base by the exponent, not the base by itself.", "negcuad": "In −a² the exponent applies only to the a: the answer is negative, not positive." }
 },
 "es": {
  "conPar": "<strong>Con paréntesis:</strong> {e} = {m} = <strong>{r}</strong>. La base es −{b}; {s}",
  "impar": "exponente impar, negativo.", "par": "exponente par, positivo.",
  "sinPar": "<strong>Sin paréntesis:</strong> {e} = −({m}) = <strong>{r}</strong>. La base es {b}, y el signo menos se aplica al final.",
  "coinciden": "Con exponente impar los dos coinciden, pero por razones distintas.", "opuestos": "Con exponente par dan resultados opuestos: por eso importan los paréntesis.",
  "arbitroQ": "Revise esta resolución de {e}:", "pasoN": "Paso {n}", "ninguno": "Ninguno: está bien resuelta",
  "bienSinError": "Todos los pasos respetan PEMDAS; el resultado {r} es correcto.", "errorEn": "El error está en el paso {n}. {x} El resultado correcto es {r}.",
  "pistaArbitro": "Revise cada paso: ¿hace la operación de mayor prioridad?",
  "explica": { "izqder": "Se hizo una suma o una resta antes que una multiplicación o una división.", "potmul": "Una potencia se calculó multiplicando la base por el exponente, en vez de multiplicar la base por sí misma.", "negcuad": "En −a² el exponente solo afecta a la a: el resultado es negativo, no positivo." }
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function n(a, b){ return nA(a, b); }
function raizDe(s){ var a = aleatorio(1, s * s - 1); return Rt([N(a), "+", N(s * s - a)]); }
function fabPot(){
  var tipo = aleatorio(1, 4), s = aleatorio(2, 12);
  if (tipo === 1) return [n(1, 20), "+", Rt([N(s * s)]), "×", n(2, 6)];
  if (tipo === 2) return [Pw(n(2, 5), aleatorio(2, 3)), "+", raizDe(aleatorio(3, 10))];
  if (tipo === 3) return [Pw(n(2, 9), 2), "−", Rt([N(s * s)]), "×", n(2, 5)];
  return [G("(", [n(2, 6), "+", n(1, 5)]), "×", n(2, 4), "−", Pw(n(2, 4), 2), "+", Rt([N(s * s)])];
}
function fabFrac(){
  var tipo = aleatorio(1, 3);
  if (tipo === 1) return [Fr([Pw(n(2, 6), 2), "+", n()], [n(2, 5), "×", n(2, 4)])];
  if (tipo === 2) return [Fr([n(10, 60), "−", n()], [n(2, 9)]), "+", n(1, 9), "×", n(2, 5)];
  return [n(1, 20), "+", Fr([n(2, 9), "×", n(2, 9)], [Pw(n(2, 3), 2), "−", n(1, 3)])];
}
function fabNeg(){
  var tipo = aleatorio(1, 4);
  if (tipo === 1) return [N(-aleatorio(1, 12)), "+", n(2, 9), "×", N(-aleatorio(1, 9))];
  if (tipo === 2) return [Mn(Pw(n(2, 6), 2)), "+", Pw(G("(", [N(-aleatorio(2, 6))]), aleatorio(2, 3))];
  if (tipo === 3) return [Mn(Pw(n(2, 7), 2)), "+", n(2, 6), "×", G("(", [N(-aleatorio(1, 9)), "+", n(1, 9)])];
  return [N(-aleatorio(10, 40)), "÷", n(2, 5), "−", Pw(G("(", [N(-aleatorio(1, 4))]), 2)];
}
function fabIzq(){ return [n(1, 20), elige(["+", "−"]), n(2, 9), elige(["×", "÷"]), n(2, 9), elige(["+", "−"]), Pw(n(2, 5), 2)]; }

/* ============ MODULE 3 · with and without parentheses ============ */
function pintaNG(){
  var b = +$("ng-b").value, e = +$("ng-e").value, con = Math.pow(-b, e), sin = -Math.pow(b, e);
  $("ng-bv").textContent = b; $("ng-ev").textContent = e;
  $("ng-salida").innerHTML = '<div class="linea">' + F(TXT.conPar, { e: exprHTML([Pw(G("(", [N(-b)]), e)]), m: Array(e).fill("(−" + b + ")").join(" × "), r: ent(con), b: b, s: e % 2 ? TXT.impar : TXT.par }) + '</div>' +
    '<div class="linea">' + F(TXT.sinPar, { e: exprHTML([Mn(Pw(N(b), e))]), m: Array(e).fill(b).join(" × "), r: ent(sin), b: b }) + '</div>' +
    '<div class="linea">' + (con === sin ? TXT.coinciden : TXT.opuestos) + '</div>';
}

/* ============ MODULE 4 · the referee ============ */
function genArbitro(){
  for (var k = 0; k < 300; k++){
    var sinError = Math.random() < 0.25, tipo = elige(["izqder", "potmul", "negcuad"]);
    var fab = { izqder: fabIzq, potmul: fabPot, negcuad: fabNeg }[tipo], x = generaExacta(fab, 400), modo = sinError ? null : { tipo: tipo }, R = sinError ? x.R : resolver(x.e, modo);
    if (!sinError && (!modo.usado || !R.exacto || R.res === x.R.res)) continue;
    if (R.pasos.length < 2 || R.pasos.length > 5) continue;
    var h = R.pasos.map(function(p, i){ return '<div class="expr-paso"><strong>' + F(TXT.pasoN, { n: i + 1 }) + ':</strong> ' + envuelve(rLista(p.hl), vozLista(p.antes)) + ' <span aria-hidden="true">→</span> ' + exprHTML(p.despues) + '</div>'; }).join("");
    var o = R.pasos.map(function(p, i){ return { html: F(TXT.pasoN, { n: i + 1 }), clave: "p" + i }; }).concat([{ html: TXT.ninguno, clave: "ok" }]);
    var cor = sinError ? "ok" : "p" + modo.paso;
    var exp = sinError ? F(TXT.bienSinError, { r: numTxt(R.res) }) : F(TXT.errorEn, { n: modo.paso + 1, x: TXT.explica[tipo], r: numTxt(x.R.res) });
    return { enOrden: true, enun: F(TXT.arbitroQ, { e: exprHTML(norm(x.e)) }) + h, opciones: o, correcta: cor, pista: TXT.pistaArbitro, bien: exp, mal: exp };
  }
}

/* ============ Start ============ */
stepper("pr", fabPot, [[N(3), "+", Rt([N(25)]), "×", N(2)], [Pw(N(2), 3), "+", Rt([N(16), "+", N(9)])]]);
creaPracticaLibre("p1", practicaDe(fabPot));
stepper("bf", fabFrac, [[Fr([Pw(N(3), 2), "+", N(7)], [N(2), "×", N(4)])]]);
creaPracticaLibre("p2", practicaDe(fabFrac));
["ng-b", "ng-e"].forEach(function(id){ $(id).addEventListener("input", pintaNG); }); pintaNG();
creaPracticaLibre("p3", practicaDe(fabNeg));
creaPracticaOM("p4", genArbitro);
'''

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    mods = [
     (t("powers-roots", "potencias-raices"), t("Powers and roots", "Potencias y raíces"),
      f'''      <p>{t("Powers and roots share the second level of PEMDAS. And everything under the √ sign is grouped as if it were in parentheses: √(16 + 9) = √25 = 5, not √16 + √9 = 7.", "Las potencias y las raíces comparten el segundo nivel de PEMDAS. Y todo lo que está bajo el signo √ queda agrupado como si estuviera entre paréntesis: √(16 + 9) = √25 = 5, no √16 + √9 = 7.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos_panel("pr", t("Another expression", "Otra expresión"))}
{B.libre_e("p1", t("Practice: powers and roots", "Practique: potencias y raíces"))}'''),
     (t("fraction-bar", "barra-fraccion"), t("The fraction bar groups", "La barra de fracción como agrupador"),
      f'''      <p>{t("The fraction bar groups the numerator and the denominator. Work out each one separately, and divide at the end. On one line: (numerator) ÷ (denominator).", "La barra de fracción agrupa el numerador y el denominador. Se resuelve cada uno por separado y al final se divide. En una línea: (numerador) ÷ (denominador).")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos_panel("bf", t("Another expression", "Otra expresión"))}
{B.libre_e("p2", t("Practice: with a fraction bar", "Practique: con barra de fracción"))}'''),
     (t("negatives", "negativos"), t("PEMDAS with negative numbers", "PEMDAS con negativos"),
      f'''      <p>{t("With parentheses, the sign is part of the base: (−5)<sup>2</sup> = 25. With no parentheses, the exponent applies only to the number, and the minus sign is applied at the end: −5<sup>2</sup> = −25.", "Con paréntesis, el signo es parte de la base: (−5)<sup>2</sup> = 25. Sin paréntesis, el exponente afecta solo al número, y el signo menos se aplica al final: −5<sup>2</sup> = −25.")}</p>
      <h3>{t("With and without parentheses", "Con paréntesis y sin ellos")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("ng-b", t("Number", "Número"), 1, 9, 5)}
          {deslizador("ng-e", t("Exponent", "Exponente"), 1, 5, 2)}
        </div>
        <div class="salida" id="ng-salida" aria-live="polite"></div>
      </div>
{B.libre_e("p3", t("Practice: with negative numbers", "Practique: con negativos"))}'''),
     (t("referee", "arbitro"), t("The order referee", "El árbitro del orden de las operaciones"),
      f'''      <p>{t("Read each solution like a referee. Is every step the operation with the highest priority? If a step breaks the order, choose it. If every step is right, choose \"None.\"", "Lea cada resolución como un árbitro. ¿Cada paso hace la operación de mayor prioridad? Si un paso rompe el orden, elíjalo. Si todos los pasos están bien, elija «Ninguno».")}</p>
{B.om("p4", t("Practice: in which step is the mistake?", "Practique: ¿en qué paso está el error?"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js", "/math/pemdas.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "PEMDAS con potencias, raíces, fracciones y signos")
