"""Level 2 · Lesson 2.1 · Fractions with negative signs — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import m, p, fr, frn, frp, mixto

B.NIVEL = 2
N = "2-1"
TEMA = ("Fractions, exponents, and roots", "Fracciones, exponentes y raíces")
TIT = ("Fractions with negative signs", "Fracciones complejas con coeficientes negativos")

def juego():
    """Tarjeta a Fracciomanía (un solo archivo bilingüe; el idioma va en el enlace)."""
    href = "/math/level-2/fracciomania.html?lang=" + t("en", "es")
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{t("Open the game: Fracciomanía (opens in a new tab)", "Abrir el juego: Fracciomanía (se abre en una pestaña nueva)")}">
<span class="ei-icono" aria-hidden="true">🎲</span>
<span class="ei-cuerpo"><span class="ei-titulo">{t("Game: Fracciomanía", "Juego: Fracciomanía")}</span><span class="ei-sub">{t("Review the four operations with fractions at your own pace, as a game with points and streaks.", "Repase las cuatro operaciones con fracciones a su ritmo, como un juego con puntos y rachas.")}</span><span class="ei-cta">{t("Open the game", "Abrir el juego")} <span aria-hidden="true">›</span></span></span>
</a>'''

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Topic 2. In Topic 1 you learned the key rule: <strong>same signs give a positive answer; different signs give a negative answer</strong>. That same rule opens this topic. In Level 1 fractions were always positive; now they get a sign. The good news: there are no new sign rules. Fractions follow exactly the same rules as integers.",
"Bienvenido al Tema 2. En el Tema 1 aprendió la regla esencial: <strong>signos iguales dan positivo; signos distintos dan negativo</strong>. Esa misma regla abre este tema. En el Nivel 1 las fracciones siempre fueron positivas; ahora llevan signo. La buena noticia: no hay reglas nuevas de signo. Las fracciones obedecen exactamente las mismas reglas que los enteros.")}</p>
<p>{t("A negative fraction can be written in three ways, and all three are <strong>the same number</strong>:", "Una fracción negativa se puede escribir de tres maneras, y las tres son <strong>el mismo número</strong>:")}</p>
<p style="text-align:center;font-size:1.25em">{frn(3, 4)} &nbsp;=&nbsp; {fr(-3, 4)} &nbsp;=&nbsp; {fr(3, -4)}</p>
<p>{t("The minus sign can go in front of the fraction, in the numerator, or in the denominator: the value does not change. Why? Because a fraction is a division, and −3 ÷ 4 and 3 ÷ (−4) both have different signs, so both are negative.",
"El signo menos puede ir delante de la fracción, en el numerador o en el denominador: el valor no cambia. ¿Por qué? Porque una fracción es una división, y −3 ÷ 4 y 3 ÷ (−4) tienen signos distintos: las dos son negativas.")}</p>
{caja("tip", t("The usual way", "La forma habitual"), t("<p>We usually write the minus sign in front of the fraction or in the numerator. A sign in the denominator is correct, but it is easy to misread.</p>", "<p>Normalmente el signo menos se escribe delante de la fracción o en el numerador. En el denominador es correcto, pero se presta a errores de lectura.</p>"))}
<h3>{t("Two minus signs make a positive fraction", "Dos signos menos dan una fracción positiva")}</h3>
<p>{t("If the numerator and the denominator are both negative, the fraction is <strong>positive</strong>: the two signs cancel, just as in dividing integers.", "Si el numerador y el denominador son negativos, la fracción es <strong>positiva</strong>: los dos signos se cancelan, igual que en la división de enteros.")}</p>
{ejemplo(t("Example: simplify the sign of", "Ejemplo: simplifique el signo de") + " " + fr(-6, -8),
  [("1", t("Step 1.", "Paso 1."), t("A fraction is a division: −6 ÷ (−8).", "Una fracción es una división: −6 ÷ (−8).")),
   ("2", t("Step 2.", "Paso 2."), t("Same signs (both negative): the answer is positive.", "Signos iguales (los dos negativos): el resultado es positivo.")),
   ("3", t("Step 3.", "Paso 3."), t("Simplify the value: 6/8 = 3/4.", "Se simplifica el valor: 6/8 = 3/4.")),
   ("✓", t("Result.", "Resultado."), f"{fr(-6, -8)} = <strong>{fr(3, 4)}</strong>")])}
{practica("p1", t("Practice 1 — The sign of a fraction", "Práctica 1 — El signo de una fracción"), t("Is the fraction", "¿La fracción") + f" {fr(-7, -2)} " + t("positive or negative?", "es positiva o negativa?"),
          [("a", t("Negative", "Negativa")), ("b", t("Positive", "Positiva"))])}
{practica("p2", t("Practice 2 — The same number", "Práctica 2 — El mismo número"), t("Which fraction is <strong>not</strong> equal to the other three?", "¿Qué fracción <strong>no</strong> es igual a las otras tres?"),
          [("a", frn(2, 5)), ("b", fr(-2, 5)), ("c", fr(-2, -5)), ("d", fr(2, -5))])}
{enlace(n, t("three-forms", "tres-formas"), t("the three forms of a negative fraction", "las tres formas de una fracción negativa"), t("Move the sign between the front, the numerator, and the denominator, and see that the value does not change.", "Mueva el signo entre delante, numerador y denominador y compruebe que el valor no cambia."))}'''

    s2 = f'''<p>{t("To multiply or divide fractions with signs, work in <strong>two separate steps</strong>: first decide the sign of the answer; then operate with the absolute values, as you did in Level 1.", "Para multiplicar o dividir fracciones con signo se trabaja en <strong>dos pasos separados</strong>: primero se decide el signo del resultado; después se opera con los valores absolutos, como en el Nivel 1.")}</p>
{tabla(t("Multiplying and dividing fractions with signs", "Multiplicar y dividir fracciones con signo"), t("How to find the value and how to decide the sign when you multiply or divide fractions", "Cómo se halla el valor y cómo se decide el signo al multiplicar o dividir fracciones"),
       [t("Operation", "Operación"), t("How to find the value", "Cómo se halla el valor"), t("How to decide the sign", "Cómo se decide el signo")],
       [[t("<strong>Multiplying</strong>", "<strong>Multiplicación</strong>"), t("numerator × numerator, denominator × denominator", "numerador × numerador, denominador × denominador"), t("sign rule: same (+), different (−)", "regla de los signos: iguales (+), distintos (−)")],
        [t("<strong>Dividing</strong>", "<strong>División</strong>"), t("multiply by the reciprocal of the second fraction", "se multiplica por el recíproco de la segunda fracción"), t("sign rule: same (+), different (−)", "regla de los signos: iguales (+), distintos (−)")]])}
{ejemplo(t("Example: multiply", "Ejemplo: multiplicar") + f" {frp(-3, 4)} × {frp(-2, 5)}",
  [("1", t("The sign.", "El signo."), t("Both fractions are negative: same signs, so the answer is positive.", "Las dos fracciones son negativas: signos iguales, así que el resultado es positivo.")),
   ("2", t("The value.", "El valor."), t("Multiply the numerators (3 × 2 = 6) and the denominators (4 × 5 = 20): 6/20.", "Se multiplican los numeradores (3 × 2 = 6) y los denominadores (4 × 5 = 20): 6/20.")),
   ("3", t("Simplify.", "Simplifique."), t("6/20 = 3/10.", "6/20 = 3/10.")),
   ("✓", t("Result.", "Resultado."), f"<strong>{fr(3, 10)}</strong>")])}
{ejemplo(t("Example: divide", "Ejemplo: dividir") + f" {fr(2, 3)} ÷ {frp(-4, 9)}",
  [("1", t("The sign.", "El signo."), t("One positive and one negative: different signs, so the answer is negative.", "Una positiva y otra negativa: signos distintos, así que el resultado es negativo.")),
   ("2", t("The reciprocal.", "El recíproco."), t("Dividing is multiplying by the reciprocal: 2/3 × 9/4.", "Dividir es multiplicar por el recíproco: 2/3 × 9/4.")),
   ("3", t("The value.", "El valor."), t("2 × 9 = 18 and 3 × 4 = 12: 18/12 = 3/2.", "2 × 9 = 18 y 3 × 4 = 12: 18/12 = 3/2.")),
   ("✓", t("Result.", "Resultado."), f"<strong>{frn(3, 2)}</strong> " + t("(or −1 1/2)", "(o −1 1/2)"))])}
{caja("ojo", t("Watch out!", "¡Ojo!"), t("<p>When you flip the second fraction to find its reciprocal, the sign does not get lost: you already decided it in step 1. That is why it helps to decide the sign <strong>first</strong>.</p>",
"<p>Al dar vuelta la segunda fracción para hallar su recíproco, el signo no se pierde: ya lo decidió en el paso 1. Por eso conviene decidir el signo <strong>primero</strong>.</p>"))}
{practica("p3", t("Practice 3 — The sign first", "Práctica 3 — Primero el signo"), t(f"Before you calculate: what sign will {frp(3, 7)} ÷ {frp(-2, 5)} have?", f"Antes de calcular: ¿qué signo tendrá {frp(3, 7)} ÷ {frp(-2, 5)}?"),
          [("a", t("Positive", "Positivo")), ("b", t("Negative", "Negativo"))])}
{practica("p4", t("Practice 4 — Multiply", "Práctica 4 — Multiplicar"), t("What is", "¿Cuánto es") + f" {frp(-2, 5)} × {fr(3, 7)}?",
          [("a", fr(6, 35)), ("b", frn(6, 35)), ("c", frn(5, 12)), ("d", frn(14, 15))])}
{enlace(n, t("multiply-divide", "multiplicar-dividir"), t("multiplying and dividing fractions with signs", "multiplicar y dividir fracciones con signo"), t("Decide the sign first, then work with the absolute values, step by step.", "Decida primero el signo y después opere con los valores absolutos, paso a paso."))}'''

    s3 = f'''<p>{t("To add or subtract fractions with signs, you need a <strong>common denominator</strong>, just as in Level 1. Once the denominators are the same, add or subtract the numerators with the rule for adding integers from Lesson 1.2.", "Para sumar o restar fracciones con signo se necesita un <strong>denominador común</strong>, igual que en el Nivel 1. Una vez igualados los denominadores, los numeradores se suman o se restan con la regla de la suma de enteros de la Lección 1.2.")}</p>
{ejemplo(t("Example: add", "Ejemplo: sumar") + f" {frp(-5, 6)} + {fr(1, 4)}",
  [("1", t("Step 1.", "Paso 1."), t("The common denominator of 6 and 4 is 12.", "El denominador común de 6 y 4 es 12.")),
   ("2", t("Step 2.", "Paso 2."), t("Rewrite: −5/6 = −10/12 and 1/4 = 3/12.", "Se reescriben: −5/6 = −10/12 y 1/4 = 3/12.")),
   ("3", t("Step 3.", "Paso 3."), t("Add the numerators as integers: −10 + 3 = −7.", "Se suman los numeradores como enteros: −10 + 3 = −7.")),
   ("✓", t("Result.", "Resultado."), f"<strong>{frn(7, 12)}</strong>")])}
{ejemplo(t("Example: subtract", "Ejemplo: restar") + f" {fr(1, 3)} − {frp(-2, 5)}",
  [("1", t("Step 1.", "Paso 1."), t("Subtracting a negative fraction is adding its opposite: 1/3 + 2/5.", "Restar una fracción negativa es sumar su opuesto: 1/3 + 2/5.")),
   ("2", t("Step 2.", "Paso 2."), t("The common denominator of 3 and 5 is 15: 1/3 = 5/15 and 2/5 = 6/15.", "El denominador común de 3 y 5 es 15: 1/3 = 5/15 y 2/5 = 6/15.")),
   ("3", t("Step 3.", "Paso 3."), t("Add the numerators: 5 + 6 = 11.", "Se suman los numeradores: 5 + 6 = 11.")),
   ("✓", t("Result.", "Resultado."), f"<strong>{fr(11, 15)}</strong>")])}
{caja("tip", t("Remember", "Recuerde"), t("<p>\"Subtracting is adding the opposite,\" from Lesson 1.2, works the same way with fractions. Subtracting −2/5 is adding +2/5: the two minus signs in a row become a plus sign.</p>",
"<p>«Restar es sumar el opuesto», de la Lección 1.2, funciona igual con fracciones. Restar −2/5 es sumar +2/5: los dos signos menos seguidos se vuelven un signo más.</p>"))}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>To type −5/6, press {T("(−)")} first and then the fraction: {T("(−)")} {T("n/d")} {T("5")} {T("▼")} {T("6")} {T("►")}. Then press {T("+")} {T("n/d")} {T("1")} {T("▼")} {T("4")} {T("►")} {T("enter")}. The screen shows −7/12.</p>""",
f"""<p>Para escribir −5/6, pulse primero {T("(−)")} y después la fracción: {T("(−)")} {T("n/d")} {T("5")} {T("▼")} {T("6")} {T("►")}. Luego pulse {T("+")} {T("n/d")} {T("1")} {T("▼")} {T("4")} {T("►")} {T("enter")}. La pantalla muestra −7/12.</p>"""))}
{practica("p5", t("Practice 5 — Same denominator", "Práctica 5 — Mismo denominador"), t("What is", "¿Cuánto es") + f" {frp(-3, 8)} + {fr(1, 8)}?",
          [("a", frn(1, 4)), ("b", fr(1, 4)), ("c", frn(1, 2)), ("d", frn(2, 16))])}
{enlace(n, t("add-subtract", "sumar-restar"), t("adding and subtracting fractions with signs", "sumar y restar fracciones con signo"), t("Find the common denominator and add the numerators with the rule for integers.", "Busque el denominador común y sume los numeradores con la regla de los enteros."))}'''

    s4 = f'''<p>{t("Some expressions mix an <strong>integer</strong> and a <strong>fraction</strong> with signs. Write the integer as a fraction with denominator 1, and then use everything above.", "Algunas expresiones mezclan un <strong>entero</strong> y una <strong>fracción</strong> con signo. El entero se escribe como fracción de denominador 1 y después se aplica todo lo anterior.")}</p>
{ejemplo(t("Example:", "Ejemplo:") + f" −2 + {frp(-3, 4)}",
  [("1", t("Step 1.", "Paso 1."), t("Write −2 with denominator 4: −2 = −8/4.", "Se escribe −2 con denominador 4: −2 = −8/4.")),
   ("2", t("Step 2.", "Paso 2."), t("Add the numerators as integers: −8 + (−3) = −11.", "Se suman los numeradores como enteros: −8 + (−3) = −11.")),
   ("3", t("Step 3.", "Paso 3."), t("The answer is −11/4. As a mixed number: −2 3/4.", "El resultado es −11/4. Como número mixto: −2 3/4.")),
   ("✓", t("Result.", "Resultado."), f"<strong>{frn(11, 4)}</strong> = <strong>{mixto(2, 3, 4, True)}</strong>")])}
{caja("ojo", t("A negative mixed number", "Un número mixto negativo"), t("<p>−2 3/4 means −(2 + 3/4): the minus sign applies to the whole number <strong>and</strong> to the fraction. It is not −2 + 3/4.</p>",
"<p>−2 3/4 quiere decir −(2 + 3/4): el signo menos afecta al entero <strong>y</strong> a la fracción. No es −2 + 3/4.</p>"))}
{practica("p6", t("Practice 6 — Integer and fraction", "Práctica 6 — Entero y fracción"), t("What is", "¿Cuánto es") + f" −1 + {fr(1, 3)}?",
          [("a", frn(4, 3)), ("b", fr(2, 3)), ("c", frn(2, 3)), ("d", frn(1, 3))])}
{enlace(n, t("integer-fraction", "combinadas"), t("expressions with an integer and a fraction", "expresiones con entero y fracción"), t("Write the integer as a fraction and combine; give the answer as a fraction or a mixed number.", "Convierta el entero en fracción y combine; dé el resultado como fracción o número mixto."))}
{juego()}'''

    secciones = [("s-" + t("three-forms", "tres-formas"), t("The three forms of a negative fraction", "Las tres formas de una fracción negativa"), s1),
                 ("s-" + t("multiply-divide", "multiplicar-dividir"), t("Multiplying and dividing fractions with signs", "Multiplicar y dividir fracciones con signo"), s2),
                 ("s-" + t("add-subtract", "sumar-restar"), t("Adding and subtracting fractions with signs", "Sumar y restar fracciones con signo"), s3),
                 ("s-" + t("integer-fraction", "combinadas"), t("Expressions with an integer and a fraction", "Expresiones con entero y fracción"), s4)]

    lesson = {"next": t("Lesson 2.2", "Lección 2.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {},
             "right": t("A fraction is a division: −7 ÷ (−2). Same signs give a positive answer.", "Una fracción es una división: −7 ÷ (−2). Signos iguales dan positivo."),
             "solution": t("The numerator and the denominator are both negative: same signs, so the fraction is positive. It is equal to 7/2.", "El numerador y el denominador son negativos: signos iguales, así que la fracción es positiva. Es igual a 7/2.")},
      "p2": {"ok": "c", "hints": {"a": t("−2/5 is negative. Look for the fraction with two minus signs.", "−2/5 es negativa. Busque la fracción con dos signos menos."),
                                   "b": t("One minus sign in the numerator: it is negative, like the others. Which one has two minus signs?", "Un signo menos en el numerador: es negativa, como las otras. ¿Cuál tiene dos signos menos?"),
                                   "d": t("One minus sign in the denominator: it is negative too. Which one has two minus signs?", "Un signo menos en el denominador: también es negativa. ¿Cuál tiene dos signos menos?")},
             "right": t("With two minus signs, the fraction is positive: it is 2/5. The other three are −2/5.", "Con dos signos menos, la fracción es positiva: es 2/5. Las otras tres son −2/5."),
             "solution": t("The three fractions with one minus sign are the same number, −2/5. The one with two minus signs is positive: 2/5.", "Las tres fracciones con un signo menos son el mismo número, −2/5. La que tiene dos signos menos es positiva: 2/5.")},
      "p3": {"ok": "b", "hints": {},
             "right": t("One positive and one negative: different signs, so the answer is negative.", "Una positiva y otra negativa: signos distintos, así que el resultado es negativo."),
             "solution": t("3/7 is positive and −2/5 is negative: different signs, so the quotient is negative. (Its value is −15/14.)", "3/7 es positiva y −2/5 es negativa: signos distintos, así que el cociente es negativo. (Su valor es −15/14.)")},
      "p4": {"ok": "b", "hints": {"a": t("The value 6/35 is right. One fraction is negative and one is positive: what sign is the product?", "El valor 6/35 está bien. Una fracción es negativa y otra positiva: ¿qué signo lleva el producto?"),
                                   "c": t("You added the numerators and the denominators. To multiply, multiply them.", "Sumó los numeradores y los denominadores. Para multiplicar, se multiplican."),
                                   "d": t("You flipped the second fraction. That is for dividing; here you multiply straight across.", "Dio vuelta la segunda fracción. Eso es para dividir; aquí se multiplica directamente.")},
             "right": t("Different signs: negative. 2 × 3 = 6 and 5 × 7 = 35: −6/35.", "Signos distintos: negativo. 2 × 3 = 6 y 5 × 7 = 35: −6/35."),
             "solution": t("Sign: different signs, negative. Value: 2 × 3 = 6 and 5 × 7 = 35. The answer is −6/35.", "Signo: signos distintos, negativo. Valor: 2 × 3 = 6 y 5 × 7 = 35. El resultado es −6/35.")},
      "p5": {"ok": "a", "hints": {"b": t("The value 1/4 is right. −3 + 1 is negative: check the sign.", "El valor 1/4 está bien. −3 + 1 es negativo: revise el signo."),
                                   "c": t("Check the numerators: −3 + 1 = −2, not −4.", "Revise los numeradores: −3 + 1 = −2, no −4."),
                                   "d": t("Do not add the denominators: they are already the same. Keep 8.", "No sume los denominadores: ya son iguales. Se queda el 8.")},
             "right": t("−3 + 1 = −2, so −2/8, which simplifies to −1/4.", "−3 + 1 = −2, así que −2/8, que se simplifica a −1/4."),
             "solution": t("Same denominator: add the numerators as integers, −3 + 1 = −2, and keep the 8: −2/8 = −1/4.", "Mismo denominador: se suman los numeradores como enteros, −3 + 1 = −2, y se conserva el 8: −2/8 = −1/4.")},
      "p6": {"ok": "c", "hints": {"a": t("−4/3 would be −1 − 1/3. Here you add 1/3, so you move toward zero.", "−4/3 sería −1 − 1/3. Aquí se suma 1/3, así que se acerca al cero."),
                                   "b": t("The value 2/3 is right, but −1 is larger in absolute value than 1/3: the answer is negative.", "El valor 2/3 está bien, pero −1 tiene mayor valor absoluto que 1/3: el resultado es negativo."),
                                   "d": t("Write −1 as −3/3 first. Then −3 + 1.", "Escriba primero −1 como −3/3. Después −3 + 1.")},
             "right": t("−1 = −3/3, and −3/3 + 1/3 = −2/3.", "−1 = −3/3, y −3/3 + 1/3 = −2/3."),
             "solution": t("Write −1 as −3/3. Then add the numerators: −3 + 1 = −2. The answer is −2/3.", "Se escribe −1 como −3/3. Después se suman los numeradores: −3 + 1 = −2. El resultado es −2/3.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("−3/4 is negative, like the others.", "−3/4 es negativa, como las otras."),
                                 "b": t("−3 over 4 is negative: different signs.", "−3 sobre 4 es negativa: signos distintos."),
                                 "c": t("3 over −4 is negative: different signs.", "3 sobre −4 es negativa: signos distintos.")},
            "solution": t("The three fractions with one minus sign are −3/4. The fraction 3/4 has no minus sign, so it is positive.", "Las tres fracciones con un signo menos valen −3/4. La fracción 3/4 no tiene signo menos: es positiva.")},
      "B": {"ok": "a", "hints": {"b": t("Two minus signs cancel: the fraction is positive.", "Dos signos menos se cancelan: la fracción es positiva."),
                                 "c": t("6/8 is right, but it can still be simplified.", "6/8 está bien, pero todavía se puede simplificar."),
                                 "d": t("Two minus signs cancel: the fraction is positive.", "Dos signos menos se cancelan: la fracción es positiva.")},
            "solution": t("Same signs: positive. 6/8 simplifies to 3/4.", "Signos iguales: positivo. 6/8 se simplifica a 3/4.")},
      "C": {"ok": "c", "hints": {"a": t("Both fractions are negative: same signs, so the product is positive.", "Las dos fracciones son negativas: signos iguales, así que el producto es positivo."),
                                 "b": t("You added. This is a multiplication.", "Sumó. Esto es una multiplicación."),
                                 "d": t("6/20 is right, but simplify it.", "6/20 está bien, pero simplifíquelo.")},
            "solution": t("Same signs: positive. 3 × 2 = 6 and 4 × 5 = 20: 6/20 = 3/10.", "Signos iguales: positivo. 3 × 2 = 6 y 4 × 5 = 20: 6/20 = 3/10.")},
      "D": {"ok": "b", "hints": {"a": t("The value 3/2 is right, but the signs are different.", "El valor 3/2 está bien, pero los signos son distintos."),
                                 "c": t("You multiplied without flipping the second fraction. To divide, multiply by the reciprocal.", "Multiplicó sin dar vuelta la segunda fracción. Para dividir, se multiplica por el recíproco."),
                                 "d": t("−2/3 is only the first fraction with a minus sign. Flip the second fraction and multiply: 2/3 × 9/4.", "−2/3 es solo la primera fracción con un signo menos. Dé vuelta la segunda fracción y multiplique: 2/3 × 9/4.")},
            "solution": t("Different signs: negative. 2/3 × 9/4 = 18/12 = 3/2. The answer is −3/2.", "Signos distintos: negativo. 2/3 × 9/4 = 18/12 = 3/2. El resultado es −3/2.")},
      "E": {"ok": "a", "hints": {"b": t("The value 7/12 is right. −10 + 3 is negative.", "El valor 7/12 está bien. −10 + 3 es negativo."),
                                 "c": t("You added the numerators and the denominators. Find a common denominator first.", "Sumó numeradores y denominadores. Primero busque un denominador común."),
                                 "d": t("With different signs, subtract the numerators: −10 + 3.", "Con signos distintos, se restan los numeradores: −10 + 3.")},
            "solution": t("Common denominator 12: −10/12 + 3/12 = −7/12.", "Denominador común 12: −10/12 + 3/12 = −7/12.")},
      "F": {"ok": "d", "hints": {"a": t("Subtracting −2/5 is adding +2/5. Check the sign.", "Restar −2/5 es sumar +2/5. Revise el signo."),
                                 "b": t("Subtracting −2/5 is adding +2/5: 5/15 + 6/15.", "Restar −2/5 es sumar +2/5: 5/15 + 6/15."),
                                 "c": t("You subtracted the numerators and the denominators. Find a common denominator.", "Restó numeradores y denominadores. Busque un denominador común.")},
            "solution": t("1/3 − (−2/5) = 1/3 + 2/5 = 5/15 + 6/15 = 11/15.", "1/3 − (−2/5) = 1/3 + 2/5 = 5/15 + 6/15 = 11/15.")},
      "G": {"ok": "b", "hints": {"a": t("−2 3/4 is −(2 + 3/4). Check: −2 + (−3/4) gets more negative.", "−2 3/4 es −(2 + 3/4). Compruebe: −2 + (−3/4) se vuelve más negativo."),
                                 "c": t("Both numbers are negative, so the sum is negative.", "Los dos números son negativos, así que la suma es negativa."),
                                 "d": t("Write −2 as −8/4 first. Then −8 + (−3).", "Escriba primero −2 como −8/4. Después −8 + (−3).")},
            "solution": t("−2 = −8/4. Then −8/4 + (−3/4) = −11/4 = −2 3/4.", "−2 = −8/4. Después −8/4 + (−3/4) = −11/4 = −2 3/4.")},
      "H": {"ok": "c", "hints": {"a": t("The value 2/9 is right, but the signs are different.", "El valor 2/9 está bien, pero los signos son distintos."),
                                 "b": t("4/18 is right, but simplify it.", "4/18 está bien, pero simplifíquelo."),
                                 "d": t("You added. This is a multiplication.", "Sumó. Esto es una multiplicación.")},
            "solution": t("Different signs: negative. 1 × 4 = 4 and 2 × 9 = 18: 4/18 = 2/9. The answer is −2/9.", "Signos distintos: negativo. 1 × 4 = 4 y 2 × 9 = 18: 4/18 = 2/9. El resultado es −2/9.")}
     }}

    quiz = [
     ("A", t("Which fraction is <strong>not</strong> equal to the other three?", "¿Qué fracción <strong>no</strong> es igual a las otras tres?"), [("a", frn(3, 4)), ("b", fr(-3, 4)), ("c", fr(3, -4)), ("d", fr(3, 4))]),
     ("B", t("What is", "¿Cuánto es") + f" {fr(-6, -8)} " + t("in simplest form?", "en su forma más simple?"), [("a", fr(3, 4)), ("b", frn(3, 4)), ("c", fr(6, 8)), ("d", frn(6, 8))]),
     ("C", t("What is", "¿Cuánto es") + f" {frp(-3, 4)} × {frp(-2, 5)}?", [("a", frn(3, 10)), ("b", frn(5, 9)), ("c", fr(3, 10)), ("d", fr(6, 20))]),
     ("D", t("What is", "¿Cuánto es") + f" {fr(2, 3)} ÷ {frp(-4, 9)}?", [("a", fr(3, 2)), ("b", frn(3, 2)), ("c", frn(8, 27)), ("d", frn(2, 3))]),
     ("E", t("What is", "¿Cuánto es") + f" {frp(-5, 6)} + {fr(1, 4)}?", [("a", frn(7, 12)), ("b", fr(7, 12)), ("c", frn(4, 10)), ("d", frn(13, 12))]),
     ("F", t("What is", "¿Cuánto es") + f" {fr(1, 3)} − {frp(-2, 5)}?", [("a", frn(11, 15)), ("b", frn(1, 15)), ("c", frn(1, 2)), ("d", fr(11, 15))]),
     ("G", t("What is", "¿Cuánto es") + f" −2 + {frp(-3, 4)}?", [("a", frn(5, 4)), ("b", mixto(2, 3, 4, True)), ("c", mixto(2, 3, 4)), ("d", frn(5, 6))]),
     ("H", t("What is", "¿Cuánto es") + f" {frp(-1, 2)} × {fr(4, 9)}?", [("a", fr(2, 9)), ("b", frn(4, 18)), ("c", frn(2, 9)), ("d", frn(5, 11))])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("The same sign rules as for integers, now with fractions: the three forms of a negative fraction and the four operations.", "Las mismas reglas de los signos de los enteros, ahora con fracciones: las tres formas de una fracción negativa y las cuatro operaciones."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Recognize</strong> the three equal forms of a negative fraction.", "<strong>Reconocer</strong> las tres formas iguales de una fracción negativa."),
         t("<strong>Decide</strong> the sign of a fraction, including one with two minus signs.", "<strong>Decidir</strong> el signo de una fracción, también con dos signos menos."),
         t("<strong>Multiply and divide</strong> fractions with signs: first the sign, then the value.", "<strong>Multiplicar y dividir</strong> fracciones con signo: primero el signo, después el valor."),
         t("<strong>Add and subtract</strong> fractions with signs using a common denominator.", "<strong>Sumar y restar</strong> fracciones con signo con un denominador común."),
         t("<strong>Combine</strong> an integer and a fraction, and write the answer as a fraction or a mixed number.", "<strong>Combinar</strong> un entero y una fracción, y dar el resultado como fracción o número mixto.")],
        secciones,
        (t("Write and solve three exercises that simplify the sign of a fraction (include one with two minus signs), four with the four operations with signed fractions, and three that mix an integer and a negative fraction. Decide the sign first in every one.",
           "Escriba y resuelva tres ejercicios de simplificar el signo de una fracción (uno con dos signos menos), cuatro con las cuatro operaciones con fracciones con signo y tres que mezclen un entero y una fracción negativa. Decida primero el signo en cada uno."),
         t("Look for signed fractions around you: a stock that went down 3/8 of a dollar, a temperature that dropped 1/2 degree each hour, a recipe you cut by 1/3. Write two of them as operations with signs and solve them.",
           "Busque fracciones con signo a su alrededor: una acción que bajó 3/8 de dólar, una temperatura que bajó 1/2 grado cada hora, una receta que redujo en 1/3. Escriba dos de ellas como operaciones con signo y resuélvalas.")),
        quiz,
        t("Self-check checklist for fractions with negative signs", "Lista de autoevaluación de las fracciones con signo"),
        t("Self-check checklist: skills for fractions with negative signs", "Lista de autoevaluación: destrezas con fracciones con signo"),
        [(t("The sign of a fraction", "El signo de una fracción"), t("I find the sign every time and can explain the three forms.", "Hallo el signo siempre y sé explicar las tres formas."), t("I find it in simple cases, but two minus signs confuse me.", "Lo hallo en casos sencillos, pero los dos signos menos me confunden."), t("I do not know how to find the sign of a fraction yet.", "Todavía no sé hallar el signo de una fracción.")),
         (t("Multiplying and dividing", "Multiplicar y dividir"), t("I decide the sign first and operate with no mistakes.", "Decido primero el signo y opero sin errores."), t("I get the value right, but sometimes the sign wrong.", "Acierto el valor, pero a veces me equivoco en el signo."), t("I can do it only with positive fractions.", "Solo sé hacerlo con fracciones positivas.")),
         (t("Adding and subtracting", "Sumar y restar"), t("I find the common denominator and add the numerators with the integer rule.", "Hallo el denominador común y sumo los numeradores con la regla de los enteros."), t("I find the common denominator, but I make sign mistakes.", "Hallo el denominador común, pero me equivoco en los signos."), t("I add the denominators or forget the signs.", "Sumo los denominadores u olvido los signos.")),
         (t("Integer and fraction", "Entero y fracción"), t("I write the integer as a fraction and give the answer as a fraction and a mixed number.", "Escribo el entero como fracción y doy el resultado como fracción y como número mixto."), t("I write the integer as a fraction, but I make mistakes when I combine.", "Escribo el entero como fracción, pero me equivoco al combinar."), t("I do not know how to write the integer as a fraction.", "No sé escribir el entero como fracción."))],
        t("<p>You gave fractions a sign. The big idea: <strong>signed fractions bring no new rules</strong>; they only combine what you already know about fractions and about signs.</p>\n<p>In <strong>Lesson 2.2 · Positive integer exponents and powers of 10</strong> the topic changes from fractions to <strong>powers</strong>. You will write and evaluate powers, tell the base from the exponent, use the exponent 0, and learn the perfect squares up to 225, which you will need for square roots.</p>",
          "<p>Les dio signo a las fracciones. La gran idea: <strong>las fracciones con signo no traen reglas nuevas</strong>; solo combinan lo que ya sabe de las fracciones y de los signos.</p>\n<p>En la <strong>Lección 2.2 · Exponentes enteros positivos y potencias de base 10</strong> el tema cambia de las fracciones a las <strong>potencias</strong>. Escribirá y evaluará potencias, distinguirá la base del exponente, usará el exponente 0 y aprenderá los cuadrados perfectos hasta el 225, que necesitará para las raíces cuadradas.</p>"),
        ("2-2", ("", t("Lesson 2.2 · Positive integer exponents and powers of 10", "Lección 2.2 · Exponentes enteros positivos y potencias de base 10"))),
        [(t("negative fraction", "fracción negativa"), t("A fraction less than zero. Its sign can go in front, in the numerator, or in the denominator: −3/4.", "Una fracción menor que cero. Su signo puede ir delante, en el numerador o en el denominador: −3/4.")),
         (t("reciprocal", "recíproco"), t("The fraction flipped: the reciprocal of 4/9 is 9/4. A number times its reciprocal is 1.", "La fracción dada vuelta: el recíproco de 4/9 es 9/4. Un número por su recíproco da 1.")),
         (t("common denominator", "denominador común"), t("A denominator that two fractions can share. You need it to add or subtract.", "Un denominador que comparten dos fracciones. Hace falta para sumar o restar.")),
         (t("improper fraction", "fracción impropia"), t("A fraction whose numerator is greater than or equal to its denominator in absolute value, like −11/4.", "Una fracción cuyo numerador es mayor o igual que el denominador en valor absoluto, como −11/4.")),
         (t("mixed number", "número mixto"), t("An integer and a fraction together. −2 3/4 means −(2 + 3/4).", "Un entero y una fracción juntos. −2 3/4 quiere decir −(2 + 3/4)."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "noCero": "The denominator cannot be 0: a division by zero is undefined.",
  "ceroEntre": "0 divided by any number that is not zero is 0.",
  "esDiv": "It is the division {n} ÷ {d}: {s}", "iguales": "same signs, so the fraction is <strong>positive</strong>.", "distintos": "different signs, so the fraction is <strong>negative</strong>.",
  "tresFormas": "The three forms of the same number:", "queda": "It is {v}.", "simplificada": "In simplest form: {v}.",
  "pregSigno": "Is the fraction {f} positive or negative?", "positiva": "Positive", "negativa": "Negative", "depende": "It depends on the size of the numbers",
  "pistaDepende": "The sign depends only on the signs of the numerator and the denominator.", "pistaSigno": "A fraction is a division. Look at the two signs: are they the same or different?",
  "bienIg": "Same signs: positive.", "bienDis": "Different signs: negative.",
  "cualNo": "Which fraction is <strong>not</strong> equal to the other three?", "bienNo": "{f} is positive; the other three are the same negative fraction written in three ways.", "pistaNo": "Count the minus signs in each fraction.",
  "signoMD": "<strong>Sign:</strong> the first fraction is {a} and the second is {b}: {s}", "pos": "positive", "neg": "negative",
  "sIg": "same signs, so the answer is <strong>positive</strong>.", "sDis": "different signs, so the answer is <strong>negative</strong>.",
  "recip": "<strong>Dividing is multiplying by the reciprocal:</strong> {a} ÷ {b} = {a} × {c}.",
  "valor": "<strong>Value:</strong> numerators {an} × {bn} = {n} and denominators {ad} × {bd} = {d}: {f}", "seSimpl": ", which simplifies to {v}",
  "resultado": "Answer: {e} = {r}", "calcula": "Calculate {e}.",
  "esMult": "That is the multiplication. To divide, multiply by the reciprocal of the second fraction.", "volteoMal": "You flipped the wrong fraction: use the reciprocal of the second one.",
  "opuesto": "Subtracting is adding the opposite: {a} − {b} = {a} + {c}.", "yaIguales": "The denominators are already the same: {d}.",
  "comun": "Common denominator: multiples of {a} ({ma}) and of {b} ({mb}). The first one they share is <strong>{d}</strong>.",
  "reescribe": "Rewrite: {a} = {a2} and {b} = {b2}.", "sumaNum": "Add the numerators as integers: {s}. That gives {f}",
  "denomSuma": "Do not add the denominators: find a common denominator first.", "revSigno": "Check the sign when you add the numerators.", "restaOp": "Subtracting {b} is adding its opposite, {c}.",
  "comb1": "{k} = {f}; then {s}, so the answer is {r}.", "comb2": "{k} − {f} = {k2} + {o} = {r}.", "comb3": "Multiply the integer by the numerator: {s}, over {d}: {r}.", "comoMixto": " As a mixed number: {m}."
 },
 "es": {
  "noCero": "El denominador no puede ser 0: la división entre cero no está definida.",
  "ceroEntre": "0 entre cualquier número distinto de cero es 0.",
  "esDiv": "Es la división {n} ÷ {d}: {s}", "iguales": "signos iguales, así que la fracción es <strong>positiva</strong>.", "distintos": "signos distintos, así que la fracción es <strong>negativa</strong>.",
  "tresFormas": "Las tres formas del mismo número:", "queda": "Es {v}.", "simplificada": "Simplificada: {v}.",
  "pregSigno": "¿La fracción {f} es positiva o negativa?", "positiva": "Positiva", "negativa": "Negativa", "depende": "Depende del tamaño de los números",
  "pistaDepende": "El signo depende solo de los signos del numerador y del denominador.", "pistaSigno": "Una fracción es una división. Mire los dos signos: ¿son iguales o distintos?",
  "bienIg": "Signos iguales: positiva.", "bienDis": "Signos distintos: negativa.",
  "cualNo": "¿Qué fracción <strong>no</strong> es igual a las otras tres?", "bienNo": "{f} es positiva; las otras tres son la misma fracción negativa escrita de tres formas.", "pistaNo": "Cuente los signos menos de cada fracción.",
  "signoMD": "<strong>Signo:</strong> la primera fracción es {a} y la segunda es {b}: {s}", "pos": "positiva", "neg": "negativa",
  "sIg": "signos iguales, así que el resultado es <strong>positivo</strong>.", "sDis": "signos distintos, así que el resultado es <strong>negativo</strong>.",
  "recip": "<strong>Dividir es multiplicar por el recíproco:</strong> {a} ÷ {b} = {a} × {c}.",
  "valor": "<strong>Valor:</strong> numeradores {an} × {bn} = {n} y denominadores {ad} × {bd} = {d}: {f}", "seSimpl": ", que se simplifica a {v}",
  "resultado": "Resultado: {e} = {r}", "calcula": "Calcule {e}.",
  "esMult": "Eso es la multiplicación. Para dividir, se multiplica por el recíproco de la segunda fracción.", "volteoMal": "Dio vuelta la fracción equivocada: se usa el recíproco de la segunda.",
  "opuesto": "Restar es sumar el opuesto: {a} − {b} = {a} + {c}.", "yaIguales": "Los denominadores ya son iguales: {d}.",
  "comun": "Denominador común: múltiplos de {a} ({ma}) y de {b} ({mb}). El primero que comparten es <strong>{d}</strong>.",
  "reescribe": "Se reescriben: {a} = {a2} y {b} = {b2}.", "sumaNum": "Se suman los numeradores como enteros: {s}. Queda {f}",
  "denomSuma": "Los denominadores no se suman: primero se busca un denominador común.", "revSigno": "Revise el signo al sumar los numeradores.", "restaOp": "Restar {b} es sumar su opuesto, {c}.",
  "comb1": "{k} = {f}; después, {s}, así que el resultado es {r}.", "comb2": "{k} − {f} = {k2} + {o} = {r}.", "comb3": "Se multiplica el entero por el numerador: {s}, sobre {d}: {r}.", "comoMixto": " Como número mixto: {m}."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
/* a fraction with small terms and a random sign */
function qAzar(maxD){ var d = aleatorio(2, maxD || 9), n = aleatorio(1, d + 3); while (mcdE(n, d) !== 1) n = aleatorio(1, d + 3); return q(Math.random() < 0.55 ? -n : n, d); }

/* ============ MODULE 1 · the three forms ============ */
function pintaTF(){
  var n = +$("tf-n").value, d = +$("tf-d").value, sal = $("tf-salida");
  $("tf-nv").textContent = ent(n); $("tf-dv").textContent = ent(d);
  if (d === 0){ sal.innerHTML = '<div class="linea veredicto">' + TXT.noCero + '</div>'; return; }
  var h = '<div class="linea grande">' + frH(n, d) + '</div>';
  if (n === 0){ sal.innerHTML = h + '<div class="linea veredicto">' + TXT.ceroEntre + '</div>'; return; }
  var v = q(n, d), an = Math.abs(n), ad = Math.abs(d);
  h += '<div class="linea">' + F(TXT.esDiv, { n: par(n), d: par(d), s: (n < 0) === (d < 0) ? TXT.iguales : TXT.distintos }) + '</div>';
  if (v.n < 0) h += '<div class="linea">' + TXT.tresFormas + '</div><div class="linea grande">' + qH(q(-an, ad)) + ' &nbsp;=&nbsp; ' + frH(-an, ad) + ' &nbsp;=&nbsp; ' + frH(an, -ad) + '</div>';
  else h += '<div class="linea">' + F(TXT.queda, { v: frH(an, ad) }) + '</div>';
  if (mcdE(an, ad) > 1) h += '<div class="linea">' + F(TXT.simplificada, { v: qH(v) }) + '</div>';
  sal.innerHTML = h;
}
function genSigno(){
  if (Math.random() < 0.6){
    var n = azarEnt(-12, 12, true), d = azarEnt(-12, 12, true); while (Math.abs(d) === 1) d = azarEnt(-12, 12, true);
    var pos = (n < 0) === (d < 0);
    return { enun: F(TXT.pregSigno, { f: frH(n, d) }), opciones: [{ html: TXT.positiva, clave: "p" }, { html: TXT.negativa, clave: "n" }, { html: TXT.depende, clave: "x" }], enOrden: true,
      correcta: pos ? "p" : "n", pistas: { x: TXT.pistaDepende }, pista: TXT.pistaSigno, bien: pos ? TXT.bienIg : TXT.bienDis, mal: pos ? TXT.bienIg : TXT.bienDis };
  }
  var a = aleatorio(1, 8), b = aleatorio(a + 1, 12); while (mcdE(a, b) !== 1) b = aleatorio(a + 1, 13);
  var o = [{ html: frH(-a, -b), clave: "x" }, { html: frH(-a, b), clave: "a" }, { html: frH(a, -b), clave: "b" }, { html: qH(q(-a, b)), clave: "c" }];
  return { enun: TXT.cualNo, opciones: o, correcta: "x", pista: TXT.pistaNo, bien: F(TXT.bienNo, { f: frH(-a, -b) }), mal: F(TXT.bienNo, { f: frH(-a, -b) }) };
}

/* ============ MODULE 2 · multiplying and dividing ============ */
function pasosMD(a, b, op){
  var neg = (a.n < 0) !== (b.n < 0), pasos = [], A = q(Math.abs(a.n), a.d), Bq = q(Math.abs(b.n), b.d);
  pasos.push(F(TXT.signoMD, { a: a.n < 0 ? TXT.neg : TXT.pos, b: b.n < 0 ? TXT.neg : TXT.pos, s: neg ? TXT.sDis : TXT.sIg }));
  if (op === "÷"){ pasos.push(F(TXT.recip, { a: qH(A), b: qH(Bq), c: frH(Bq.d, Bq.n) })); Bq = { n: Bq.d, d: Bq.n }; }
  var nn = A.n * Bq.n, dd = A.d * Bq.d, r = q(nn, dd);
  pasos.push(F(TXT.valor, { an: A.n, bn: Bq.n, n: nn, ad: A.d, bd: Bq.d, d: dd, f: frH(nn, dd) }) + (mcdE(nn, dd) > 1 ? F(TXT.seSimpl, { v: qH(r) }) : "") + ".");
  var res = neg ? qneg(r) : r;
  pasos.push('<span class="veredicto">' + F(TXT.resultado, { e: qP(a) + " " + op + " " + qP(b), r: qH(res) }) + '</span>');
  return { pasos: pasos, res: res };
}
var MD_COLA = [[q(-3, 4), q(-2, 5), "×"], [q(2, 3), q(-4, 9), "÷"]], MDS;
function nuevoMD(){ var e = MD_COLA.length ? MD_COLA.shift() : [qAzar(), qAzar(), elige(["×", "÷"])]; $("md-expr").innerHTML = qP(e[0]) + " " + e[2] + " " + qP(e[1]); MDS.carga(pasosMD(e[0], e[1], e[2]).pasos); }
function genMD(){
  var a = qAzar(), b = qAzar(), op = elige(["×", "÷"]), R = pasosMD(a, b, op), pistas = [];
  if (op === "÷") pistas.push({ v: qmul(a, b), msg: TXT.esMult }, { v: qdiv(b, a), msg: TXT.volteoMal });
  return { enun: F(TXT.calcula, { e: qP(a) + " " + op + " " + qP(b) }), correcta: qTxt(R.res), solucion: R.pasos.slice(0, -1).join(" "), evalua: evQ(R.res, pistas) };
}

/* ============ MODULE 3 · adding and subtracting ============ */
function multiplos(d, hasta){ var l = []; for (var i = 1; d * i <= hasta; i++) l.push(d * i); return l; }
function pasosSR(a, b, op){
  var pasos = [], b2 = op === "−" ? qneg(b) : b, D = mcmE(a.d, b2.d);
  if (op === "−") pasos.push(F(TXT.opuesto, { a: qP(a), b: qP(b), c: qP(b2) }));
  if (a.d === b2.d) pasos.push(F(TXT.yaIguales, { d: D }));
  else pasos.push(F(TXT.comun, { a: a.d, ma: multiplos(a.d, D).join(", "), b: b2.d, mb: multiplos(b2.d, D).join(", "), d: D }));
  var na = a.n * (D / a.d), nb = b2.n * (D / b2.d), s = na + nb, r = q(s, D);
  pasos.push(F(TXT.reescribe, { a: qH(a), a2: frH(na, D), b: qH(b2), b2: frH(nb, D) }));
  pasos.push(F(TXT.sumaNum, { s: ent(na) + " + " + par(nb) + " = " + ent(s), f: frH(s, D) }) + (r.d !== D ? F(TXT.seSimpl, { v: qH(r) }) : "") + ".");
  pasos.push('<span class="veredicto">' + F(TXT.resultado, { e: qP(a) + " " + op + " " + qP(b), r: qH(r) }) + '</span>');
  return { pasos: pasos, res: r };
}
var SR_COLA = [[q(-5, 6), q(1, 4), "+"], [q(1, 3), q(-2, 5), "−"]], SRS;
function nuevoSR(){ var e = SR_COLA.length ? SR_COLA.shift() : [qAzar(8), qAzar(8), elige(["+", "−"])]; $("sr-expr").innerHTML = qP(e[0]) + " " + e[2] + " " + qP(e[1]); SRS.carga(pasosSR(e[0], e[1], e[2]).pasos); }
function genSR(){
  var a = qAzar(8), b = qAzar(8), op = elige(["+", "−"]), R = pasosSR(a, b, op), b2 = op === "−" ? qneg(b) : b;
  var pistas = [{ v: q(a.n + b2.n, a.d + b2.d), msg: TXT.denomSuma }];
  if (op === "−") pistas.push({ v: qsum(a, b), msg: F(TXT.restaOp, { b: qP(b), c: qP(b2) }) });
  return { enun: F(TXT.calcula, { e: qP(a) + " " + op + " " + qP(b) }), correcta: qTxt(R.res), solucion: R.pasos.slice(0, -1).join(" "), evalua: evQ(R.res, pistas) };
}

/* ============ MODULE 4 · integer and fraction ============ */
function genCombinada(){
  var k = azarEnt(-5, 5, true), f = qAzar(8), tipo = aleatorio(1, 3), res, e, sol;
  if (tipo === 1){ res = qsum(q(k), f); e = ent(k) + " + " + qP(f); sol = F(TXT.comb1, { k: ent(k), f: frH(k * f.d, f.d), s: ent(k * f.d) + " + " + par(f.n) + " = " + ent(k * f.d + f.n), r: qH(res) }); }
  else if (tipo === 2){ res = qres(q(k), f); e = ent(k) + " − " + qP(f); sol = F(TXT.comb2, { k: ent(k), f: qP(f), k2: frH(k * f.d, f.d), o: qP(qneg(f)), r: qH(res) }); }
  else { res = qmul(q(k), f); e = par(k) + " × " + qP(f); sol = F(TXT.comb3, { s: par(k) + " × " + par(f.n) + " = " + ent(k * f.n), d: f.d, r: qH(res) }); }
  var mx = qMixto(res);
  return { enun: F(TXT.calcula, { e: e }), correcta: qTxt(res), solucion: sol + (mx ? F(TXT.comoMixto, { m: mx }) : ""), evalua: evQ(res, []) };
}

/* ============ Start ============ */
["tf-n", "tf-d"].forEach(function(id){ $(id).addEventListener("input", pintaTF); }); pintaTF();
creaPracticaOM("p1", genSigno);
MDS = pasoAPaso("md", []); $("md-nuevo").addEventListener("click", nuevoMD); nuevoMD();
creaPracticaLibre("p2", genMD);
SRS = pasoAPaso("sr", []); $("sr-nuevo").addEventListener("click", nuevoSR); nuevoSR();
creaPracticaLibre("p3", genSR);
creaPracticaLibre("p4", genCombinada);
'''

def pasos_panel(pre):
    return f'''      <div class="panel">
        <div class="estado"><span class="grande" id="{pre}-expr"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig"></button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all", "Mostrar todo")}</button><button type="button" class="btn-sec" id="{pre}-nuevo">{t("Another example", "Otro ejemplo")}</button></div>
        <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>
      </div>'''

def libre_q(pid, titulo, nota):
    return B.libre_e(pid, titulo).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    def deslizador(i, et, vmin, vmax, val):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" value="{val}"></div>'
    nota_fr = t("Type a fraction with a slash, like −3/10, with the minus sign in front if it is negative. Give it in simplest form.", "Escriba una fracción con la barra, como −3/10, con el signo menos delante si es negativa. Désela en su forma más simple.")
    mods = [
     (t("three-forms", "tres-formas"), t("The three forms of a negative fraction", "Las tres formas de una fracción negativa"),
      f'''      <p>{t("A fraction is a division, so its sign follows the sign rule. The minus sign can go <strong>in front</strong>, in the <strong>numerator</strong>, or in the <strong>denominator</strong>, and the value does not change. If the numerator and the denominator are both negative, the two signs cancel and the fraction is positive.", "Una fracción es una división, así que su signo sigue la regla de los signos. El signo menos puede ir <strong>delante</strong>, en el <strong>numerador</strong> o en el <strong>denominador</strong>, y el valor no cambia. Si el numerador y el denominador son negativos, los dos signos se cancelan y la fracción es positiva.")}</p>
      <h3>{t("Move the signs", "Mueva los signos")}</h3>
      <div class="panel">
        <div class="campos">
          {deslizador("tf-n", t("Numerator", "Numerador"), -12, 12, -6)}
          {deslizador("tf-d", t("Denominator", "Denominador"), -12, 12, 8)}
        </div>
        <div class="salida" id="tf-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip"><strong>{t("The usual way:", "La forma habitual:")}</strong> {t("write the minus sign in front of the fraction or in the numerator. In the denominator it is correct, but easy to misread.", "el signo menos se escribe delante de la fracción o en el numerador. En el denominador es correcto, pero se presta a errores de lectura.")}</div>
{B.om("p1", t("Practice: the sign of a fraction", "Practique: el signo de una fracción"))}'''),
     (t("multiply-divide", "multiplicar-dividir"), t("Multiplying and dividing fractions with signs", "Multiplicar y dividir fracciones con signo"),
      f'''      <p>{t("Work in two separate steps: <strong>first the sign</strong>, with the sign rule, and <strong>then the value</strong>, with the absolute values. To divide, multiply by the reciprocal of the second fraction.", "Se trabaja en dos pasos separados: <strong>primero el signo</strong>, con la regla de los signos, y <strong>después el valor</strong>, con los valores absolutos. Para dividir, se multiplica por el recíproco de la segunda fracción.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos_panel("md")}
      <div class="caja-atencion"><strong>{t("When you find the reciprocal,", "Al buscar el recíproco,")}</strong> {t("you flip the numbers, but the sign was already decided at the start with the sign rule: it does not get lost.", "se dan vuelta los números, pero el signo ya se decidió al principio con la regla de los signos: no se pierde en el camino.")}</div>
{libre_q("p2", t("Practice: multiply or divide", "Practique: multiplicar o dividir"), nota_fr)}'''),
     (t("add-subtract", "sumar-restar"), t("Adding and subtracting fractions with signs", "Sumar y restar fracciones con signo"),
      f'''      <p>{t("To add or subtract you need a <strong>common denominator</strong>. With the same denominators, add or subtract the numerators with the integer rules from Topic 1. And subtracting a negative fraction is adding its opposite.", "Para sumar o restar se necesita un <strong>denominador común</strong>. Con los denominadores iguales, los numeradores se suman o se restan con las reglas de los enteros del Tema 1. Y restar una fracción negativa es sumar su opuesto.")}</p>
      <h3>{t("The common denominator, step by step", "El denominador común, paso a paso")}</h3>
{pasos_panel("sr")}
{libre_q("p3", t("Practice: add or subtract", "Practique: sumar o restar"), nota_fr)}'''),
     (t("integer-fraction", "combinadas"), t("Expressions with an integer and a fraction", "Expresiones con entero y fracción"),
      f'''      <p>{t("Treat an integer as a fraction with denominator 1 and bring it to the common denominator. For example, −2 = −8/4. You can leave the answer as an improper fraction (−11/4) or as a mixed number (−2 3/4).", "Un entero se trata como una fracción de denominador 1 y se lleva al denominador común. Por ejemplo, −2 = −8/4. El resultado se puede dejar como fracción impropia (−11/4) o como número mixto (−2 3/4).")}</p>
{libre_q("p4", t("Practice: integer and fraction", "Practique: entero y fracción"), t("Type a fraction like −11/4 or a mixed number like −2 3/4 (with a space between the whole number and the fraction).", "Escriba una fracción como −11/4 o un número mixto como −2 3/4 (con un espacio entre el entero y la fracción)."))}'''),
     ("fracciomania", "Fracciomanía",
      f'''      <p>{t("To review the four operations with fractions at your own pace, play Fracciomanía: points, streaks, and a hint when you make a mistake. It opens in a new tab.", "Para repasar las cuatro operaciones con fracciones a su ritmo, juegue a Fracciomanía: puntos, rachas y una pista cuando se equivoca. Se abre en una pestaña nueva.")}</p>
      <div class="tarjetas">
        <a class="tarjeta-ext" href="/math/level-2/fracciomania.html?lang={t("en", "es")}" target="_blank" rel="noopener noreferrer"><strong>Fracciomanía</strong>{t("The fractions game of LearnGED.", "El juego de fracciones de LearnGED.")}<span class="ir">{t("Open in a new tab ›", "Abrir en una pestaña nueva ›")}</span></a>
      </div>''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities and a game on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica y un juego en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Fracciones complejas con coeficientes negativos")
