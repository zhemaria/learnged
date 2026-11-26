"""Level 3 · Lesson 1.3 · Simplifying with several rules — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "1-3"
TEMA = ("Rules of exponents", "Reglas de los exponentes")
TIT = ("Simplifying with several rules", "Simplificar expresiones exponenciales con múltiples reglas")

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def fr(a, b):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{a}</span><span class="fb2">{b}</span></span><span class="cap-oculto">({a}) ÷ ({b})</span>'

def check_link():
    href = "topic-1-check.html" if B.L == "en" else "comprobacion-tema-1.html"
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{t("Open the Topic 1 check (opens in a new tab)", "Abrir la comprobación del Tema 1 (se abre en una pestaña nueva)")}">
<span class="ei-icono" aria-hidden="true">🎯</span>
<span class="ei-cuerpo"><span class="ei-titulo">{t("Topic 1 check: the five rules of exponents", "Comprobación del Tema 1: las cinco reglas de los exponentes")}</span><span class="ei-sub">{t("Twelve questions from the three lessons, with a report by lesson that you can print.", "Doce preguntas de las tres lecciones, con un informe por lección que puede imprimir.")}</span><span class="ei-cta">{t("Open the check", "Abrir la comprobación")} <span aria-hidden="true">›</span></span></span>
</a>'''

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 1.1 you learned the rules for multiplying (product, power of a power, and power of a product), and in Lesson 1.2 the rules for dividing, the zero exponent, and negative exponents. Those <strong>five rules</strong> are complete. This lesson adds no new rules: it teaches you to <strong>combine them in order</strong> in one expression and to give the answer in its cleanest form, with positive exponents.",
"En la Lección 1.1 aprendió las reglas de la multiplicación (producto, potencia de potencia y potencia de un producto) y en la Lección 1.2, las de la división, el exponente cero y los exponentes negativos. Esas <strong>cinco reglas</strong> ya están completas. Esta lección no añade reglas nuevas: enseña a <strong>combinarlas con orden</strong> dentro de una sola expresión y a presentar el resultado en su forma más limpia, con exponentes positivos.")}</p>
{tabla(t("The five rules of exponents", "Las cinco reglas de los exponentes"), t("The five rules of exponents: name, pattern, and example", "Las cinco reglas de los exponentes: nombre, patrón y ejemplo"),
       [t("Rule", "Regla"), t("Pattern", "Patrón"), t("Example", "Ejemplo")], [[a, b, d] for a, b, c, d in n3.tabla_reglas(True)])}
<p>{t("Every simplification in this lesson rests on this table. Keep it in view, or copy it into your notebook.", "Toda simplificación de esta lección se apoya en esta tabla. Téngala a la vista o cópiela en su cuaderno.")}</p>'''

    s2 = f'''<p>{t("When an expression combines several operations, follow the same route every time. This order prevents mistakes and gives consistent answers.", "Cuando una expresión combina varias operaciones, conviene seguir siempre la misma ruta. Este orden evita errores y da resultados consistentes.")}</p>
<ol class="lista-orden">
<li>{t("<strong>Parentheses with an exponent</strong> (power of a power and power of a product). Remember to raise the numbers too.", "<strong>Paréntesis con exponente</strong> (potencia de potencia y de un producto). Recuerde elevar también los coeficientes.")}</li>
<li>{t("<strong>Product and quotient</strong> of the same base: add or subtract exponents.", "<strong>Producto y cociente</strong> de las bases iguales: sumar o restar exponentes.")}</li>
<li>{t("<strong>Negative exponents</strong>: rewrite them as fractions with positive exponents.", "<strong>Exponentes negativos</strong>: reescribirlos como fracción con exponente positivo.")}</li>
<li>{t("<strong>Check</strong> that the answer is as simple as it can be.", "<strong>Revisar</strong> que el resultado quede en su forma más simple.")}</li>
</ol>
{ejemplo(t("Example 1: simplify (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>", "Ejemplo 1: simplifique (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>"),
  [("1", t("Parentheses.", "Paréntesis."), t("Power of a power: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>.", "Potencia de potencia: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>.")),
   ("2", t("Product.", "Producto."), "x<sup>6</sup> · x<sup>4</sup> = x<sup>6 + 4</sup>."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x<sup>10</sup></strong>")])}
{ejemplo(t("Example 2: simplify (2a<sup>3</sup>)<sup>2</sup> · a", "Ejemplo 2: simplifique (2a<sup>3</sup>)<sup>2</sup> · a"),
  [("1", t("Parentheses.", "Paréntesis."), t("Share out the exponent and raise the number: (2a<sup>3</sup>)<sup>2</sup> = 2<sup>2</sup> · a<sup>6</sup> = 4a<sup>6</sup>.", "Se reparte el exponente y se eleva el coeficiente: (2a<sup>3</sup>)<sup>2</sup> = 2<sup>2</sup> · a<sup>6</sup> = 4a<sup>6</sup>.")),
   ("2", t("Product.", "Producto."), t("4a<sup>6</sup> · a = 4a<sup>7</sup> (the a on its own is a<sup>1</sup>).", "4a<sup>6</sup> · a = 4a<sup>7</sup> (la a sola vale a<sup>1</sup>).")),
   ("✓", t("Answer.", "Respuesta."), "<strong>4a<sup>7</sup></strong>")])}
{practica("p1", t("Practice 1 — Two rules", "Práctica 1 — Dos reglas"), t("What is (x<sup>3</sup>)<sup>2</sup> · x?", "¿Cuánto es (x<sup>3</sup>)<sup>2</sup> · x?"),
          [("a", "x<sup>6</sup>"), ("b", "x<sup>7</sup>"), ("c", "x<sup>5</sup>"), ("d", "x<sup>12</sup>")])}
{practica("p2", t("Practice 2 — Raise the number", "Práctica 2 — Eleve el número"), t("What is (2y<sup>2</sup>)<sup>3</sup>?", "¿Cuánto es (2y<sup>2</sup>)<sup>3</sup>?"),
          [("a", "2y<sup>6</sup>"), ("b", "6y<sup>6</sup>"), ("c", "8y<sup>6</sup>"), ("d", "8y<sup>5</sup>")])}
{practica("p3", t("Practice 3 — Product, then quotient", "Práctica 3 — Producto y después cociente"), t("What is (a<sup>8</sup> · a<sup>2</sup>) ÷ a<sup>3</sup>?", "¿Cuánto es (a<sup>8</sup> · a<sup>2</sup>) ÷ a<sup>3</sup>?"),
          [("a", "a<sup>7</sup>"), ("b", "a<sup>13</sup>"), ("c", "a<sup>5</sup>"), ("d", "a<sup>16</sup>")])}
{enlace(n, t("order", "orden"), t("an order for simplifying", "un orden para simplificar"), t("Reveal each step of the route one at a time, and practice combining rules.", "Revele cada paso de la ruta uno a uno y practique cómo combinar reglas."))}'''

    s3 = f'''<p>{t("When the expression is a fraction, use the quotient rule on <strong>each base separately</strong>. If an exponent ends up negative, rewrite it as a fraction with a positive exponent in the last step.", "Cuando la expresión es una fracción, se aplica la regla del cociente <strong>a cada base por separado</strong>. Si algún exponente queda negativo, se reescribe como fracción de exponente positivo en el último paso.")}</p>
{ejemplo(t("Example 3: simplify ", "Ejemplo 3: simplifique ") + fr("x<sup>6</sup>y<sup>2</sup>", "x<sup>2</sup>y"),
  [("1", t("Each base.", "Cada base."), t("Subtract the exponents of each base separately: x<sup>6 − 2</sup> and y<sup>2 − 1</sup>.", "Se resta el exponente de cada base por separado: x<sup>6 − 2</sup> y y<sup>2 − 1</sup>.")),
   ("2", t("Work it out.", "Se calcula."), "x<sup>4</sup> · y<sup>1</sup> = x<sup>4</sup>y."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x<sup>4</sup>y</strong>")])}
{ejemplo(t("Example 4: simplify a<sup>4</sup> ÷ a<sup>6</sup>", "Ejemplo 4: simplifique a<sup>4</sup> ÷ a<sup>6</sup>"),
  [("1", t("Quotient.", "Cociente."), "a<sup>4 − 6</sup> = a<sup>−2</sup>."),
   ("2", t("Positive exponent.", "Exponente positivo."), t("The exponent is negative: write the reciprocal. a<sup>−2</sup> = 1/a<sup>2</sup>.", "El exponente quedó negativo: se escribe el recíproco. a<sup>−2</sup> = 1/a<sup>2</sup>.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>1/a<sup>2</sup></strong>")])}
{caja("ojo", t("The final form", "La forma final"), t("<p>An answer is not simplified while it still has negative exponents. x<sup>3</sup>y<sup>−2</sup> has the same value as x<sup>3</sup>/y<sup>2</sup>, but only the second is the answer the test expects. The last step is always to turn a<sup>−n</sup> into 1/a<sup>n</sup>.</p>",
"<p>Un resultado no está simplificado mientras tenga exponentes negativos. x<sup>3</sup>y<sup>−2</sup> vale lo mismo que x<sup>3</sup>/y<sup>2</sup>, pero solo la segunda es la respuesta que espera el examen. El último paso siempre es convertir a<sup>−n</sup> en 1/a<sup>n</sup>.</p>"))}
{practica("p4", t("Practice 4 — A fraction with two bases", "Práctica 4 — Una fracción con dos bases"), t("What is (a<sup>5</sup>b<sup>2</sup>) ÷ (a<sup>2</sup>b<sup>4</sup>)?", "¿Cuánto es (a<sup>5</sup>b<sup>2</sup>) ÷ (a<sup>2</sup>b<sup>4</sup>)?"),
          [("a", "a<sup>3</sup>b<sup>2</sup>"), ("b", "a<sup>3</sup>/b<sup>2</sup>"), ("c", "a<sup>3</sup>b<sup>−2</sup>"), ("d", "b<sup>2</sup>/a<sup>3</sup>")])}
{enlace(n, t("fractions", "fracciones"), t("fractions with negative exponents", "fracciones con exponentes negativos"), t("Simplify fractions with two bases and give the answer with positive exponents.", "Simplifique fracciones con dos bases y dé el resultado con exponentes positivos."))}'''

    s4 = f'''<p>{t("Knowing how to simplify includes noticing when someone else's answer is wrong. The mistakes almost always follow the same patterns: mixing up when to add and when to multiply, or forgetting to raise the number in front.", "Saber simplificar incluye reconocer cuándo una solución ajena está mal. Los errores casi siempre repiten los mismos patrones: confundir cuándo sumar y cuándo multiplicar, u olvidar elevar el coeficiente.")}</p>
{ejemplo(t("Example 5: someone wrote a<sup>5</sup> · a<sup>3</sup> = a<sup>15</sup>", "Ejemplo 5: alguien escribió a<sup>5</sup> · a<sup>3</sup> = a<sup>15</sup>"),
  [("1", t("Which rule?", "¿Qué regla?"), t("The powers are <em>multiplied</em> and have the same base: the product rule.", "Las potencias están <em>multiplicadas</em> y tienen la misma base: la regla del producto.")),
   ("2", t("The mistake.", "El error."), t("The exponents should be added, not multiplied: 5 + 3 = 8.", "Los exponentes deben sumarse, no multiplicarse: 5 + 3 = 8.")),
   ("✓", t("Correction.", "Corrección."), t("Wrong: a<sup>15</sup> → Right: <strong>a<sup>8</sup></strong>", "Incorrecto: a<sup>15</sup> → Correcto: <strong>a<sup>8</sup></strong>"))])}
{ejemplo(t("Example 6: someone wrote (3x)<sup>2</sup> = 3x<sup>2</sup>", "Ejemplo 6: alguien escribió (3x)<sup>2</sup> = 3x<sup>2</sup>"),
  [("1", t("Which rule?", "¿Qué regla?"), t("A power of a product: the exponent goes to <em>each</em> factor.", "Es una potencia de un producto: el exponente se reparte a <em>cada</em> factor.")),
   ("2", t("The mistake.", "El error."), t("The 3 must be squared too: 3<sup>2</sup> = 9.", "El coeficiente 3 también se eleva: 3<sup>2</sup> = 9.")),
   ("✓", t("Correction.", "Corrección."), t("Wrong: 3x<sup>2</sup> → Right: <strong>9x<sup>2</sup></strong>", "Incorrecto: 3x<sup>2</sup> → Correcto: <strong>9x<sup>2</sup></strong>"))])}
{practica("p5", t("Practice 5 — Referee", "Práctica 5 — Árbitro"), t("Someone wrote (a<sup>5</sup>)<sup>2</sup> = a<sup>7</sup>. What is the right call?", "Alguien escribió (a<sup>5</sup>)<sup>2</sup> = a<sup>7</sup>. ¿Qué corresponde?"),
          [("a", t("a<sup>7</sup> is correct.", "a<sup>7</sup> está correcto.")), ("b", t("The exponents are subtracted: a<sup>3</sup>.", "Los exponentes se restan: a<sup>3</sup>.")), ("c", t("The exponents are multiplied: a<sup>10</sup>.", "Los exponentes se multiplican: a<sup>10</sup>."))])}
{practica("p6", t("Practice 6 — Referee", "Práctica 6 — Árbitro"), t("Someone wrote x<sup>4</sup> · x<sup>2</sup> = x<sup>8</sup>. What is the right call?", "Alguien escribió x<sup>4</sup> · x<sup>2</sup> = x<sup>8</sup>. ¿Qué corresponde?"),
          [("a", t("x<sup>8</sup> is correct.", "x<sup>8</sup> está correcto.")), ("b", t("The exponents are added: x<sup>6</sup>.", "Los exponentes se suman: x<sup>6</sup>.")), ("c", t("The exponents are subtracted: x<sup>2</sup>.", "Los exponentes se restan: x<sup>2</sup>."))])}
{practica("p7", t("Practice 7 — Referee", "Práctica 7 — Árbitro"), t("Someone wrote (2x)<sup>3</sup> = 2x<sup>3</sup>. What is the right call?", "Alguien escribió (2x)<sup>3</sup> = 2x<sup>3</sup>. ¿Qué corresponde?"),
          [("a", t("The 2 is raised too: 8x<sup>3</sup>.", "El 2 también se eleva: 8x<sup>3</sup>.")), ("b", t("2x<sup>3</sup> is correct.", "2x<sup>3</sup> está correcto.")), ("c", t("The answer is 6x<sup>3</sup>.", "El resultado es 6x<sup>3</sup>."))])}
{enlace(n, t("referee", "arbitro"), t("the exponent referee", "el árbitro de exponentes"), t("Decide whether someone else's simplification is right and choose the correction.", "Decida si una simplificación ajena está bien y elija la corrección."))}'''

    s5 = f'''<p>{t("This example brings it all together: parentheses with an exponent, a number in front, a product, a quotient, and an answer with positive exponents.", "Este ejemplo reúne todo: paréntesis con exponente, coeficiente, producto, cociente y un resultado con exponentes positivos.")}</p>
{ejemplo(t("Example 7: simplify (2x<sup>3</sup>)<sup>2</sup> · x ÷ x<sup>9</sup>", "Ejemplo 7: simplifique (2x<sup>3</sup>)<sup>2</sup> · x ÷ x<sup>9</sup>"),
  [("1", t("Parentheses.", "Paréntesis."), "(2x<sup>3</sup>)<sup>2</sup> = 4x<sup>6</sup>."),
   ("2", t("Product.", "Producto."), "4x<sup>6</sup> · x = 4x<sup>7</sup>."),
   ("3", t("Quotient.", "Cociente."), "4x<sup>7</sup> ÷ x<sup>9</sup> = 4x<sup>7 − 9</sup> = 4x<sup>−2</sup>."),
   ("4", t("Positive exponent.", "Exponente positivo."), t("4x<sup>−2</sup> = 4/x<sup>2</sup>. The 4 stays on top: the negative exponent belongs only to the x.", "4x<sup>−2</sup> = 4/x<sup>2</sup>. El 4 se queda arriba: el exponente negativo es solo de la x.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>4/x<sup>2</sup></strong>")])}
{caja("tip", t("A quick check", "Una verificación rápida"), t("<p>Replace x with 2 in the original and in the answer. Original: (2 · 8)<sup>2</sup> · 2 ÷ 512 = 256 · 2 ÷ 512 = 1. Answer: 4 ÷ 2<sup>2</sup> = 1. They match, so the simplification is reliable.</p>",
"<p>Sustituya la x por 2 en la original y en el resultado. Original: (2 · 8)<sup>2</sup> · 2 ÷ 512 = 256 · 2 ÷ 512 = 1. Resultado: 4 ÷ 2<sup>2</sup> = 1. Coinciden: la simplificación es confiable.</p>"))}
{calc(t("Check with x = 2 on the calculator", "Compruebe con x = 2 en la calculadora"), t(f"<p>Type {T('(')} {T('2')} {T('×')} {T('2')} {T('^')} {T('3')} {T('▸')} {T(')')} {T('x<sup>2</sup>')} {T('×')} {T('2')} {T('÷')} {T('2')} {T('^')} {T('9')} {T('enter')}: the screen shows 1. Then {T('4')} {T('÷')} {T('2')} {T('x<sup>2</sup>')} {T('enter')} also shows 1.</p>",
f"<p>Escriba {T('(')} {T('2')} {T('×')} {T('2')} {T('^')} {T('3')} {T('▸')} {T(')')} {T('x<sup>2</sup>')} {T('×')} {T('2')} {T('÷')} {T('2')} {T('^')} {T('9')} {T('enter')}: la pantalla muestra 1. Después {T('4')} {T('÷')} {T('2')} {T('x<sup>2</sup>')} {T('enter')} también muestra 1.</p>"))}
{enlace(n, t("complete", "completa"), t("a complete expression, step by step", "una expresión completa, paso a paso"), t("Solve each step of the route yourself, with two tries per step.", "Resuelva usted cada paso de la ruta, con dos intentos por paso."))}
<p>{t("When you feel sure about the three lessons, take the Topic 1 check before you go on to Topic 2.", "Cuando se sienta seguro con las tres lecciones, haga la comprobación del Tema 1 antes de pasar al Tema 2.")}</p>
{check_link()}'''

    secciones = [("s-" + t("five-rules", "cinco-reglas"), t("The five rules in view", "Las cinco reglas a la vista"), s1),
                 ("s-" + t("order", "orden"), t("An order for simplifying", "Un orden para simplificar"), s2),
                 ("s-" + t("fractions", "fracciones"), t("Fractions and negative exponents", "Expresiones con fracciones y exponentes negativos"), s3),
                 ("s-" + t("referee", "arbitro"), t("The exponent referee: finding mistakes", "El árbitro de exponentes: detectar errores"), s4),
                 ("s-" + t("complete", "completa"), t("A complete expression, step by step", "Una expresión completa, paso a paso"), s5)]

    lesson = {"next": t("Topic 2", "el Tema 2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You left out the x at the end: it is x<sup>1</sup>.", "Le faltó la x del final: vale x<sup>1</sup>."), "c": t("In the parentheses, multiply 3 × 2, do not add.", "En el paréntesis se multiplica 3 × 2, no se suma."), "d": t("After the parentheses, x<sup>6</sup> · x adds exponents: 6 + 1.", "Después del paréntesis, x<sup>6</sup> · x suma exponentes: 6 + 1.")},
             "right": t("(x<sup>3</sup>)<sup>2</sup> = x<sup>6</sup>; x<sup>6</sup> · x = x<sup>7</sup>.", "(x<sup>3</sup>)<sup>2</sup> = x<sup>6</sup>; x<sup>6</sup> · x = x<sup>7</sup>."), "solution": t("Parentheses: 3 × 2 = 6. Product: 6 + 1 = 7. So x<sup>7</sup>.", "Paréntesis: 3 × 2 = 6. Producto: 6 + 1 = 7. Así que x<sup>7</sup>.")},
      "p2": {"ok": "c", "hints": {"a": t("The 2 is inside the parentheses: it is cubed too.", "El 2 está dentro del paréntesis: también se eleva al cubo."), "b": t("Cubing is not multiplying by 3: 2<sup>3</sup> = 8.", "Elevar al cubo no es multiplicar por 3: 2<sup>3</sup> = 8."), "d": t("For y<sup>2</sup> cubed, multiply 2 × 3.", "Para y<sup>2</sup> al cubo, multiplique 2 × 3.")},
             "right": t("2<sup>3</sup> = 8 and 2 × 3 = 6.", "2<sup>3</sup> = 8 y 2 × 3 = 6."), "solution": t("Share out the exponent: 2<sup>3</sup> = 8 and (y<sup>2</sup>)<sup>3</sup> = y<sup>6</sup>. So 8y<sup>6</sup>.", "Se reparte el exponente: 2<sup>3</sup> = 8 y (y<sup>2</sup>)<sup>3</sup> = y<sup>6</sup>. Así que 8y<sup>6</sup>.")},
      "p3": {"ok": "a", "hints": {"b": t("When you divide by a<sup>3</sup>, subtract 3, do not add it.", "Al dividir entre a<sup>3</sup>, se resta 3, no se suma."), "c": t("Inside the parentheses, add 8 + 2 first.", "Dentro del paréntesis, primero sume 8 + 2."), "d": t("Inside the parentheses the powers are multiplied: add the exponents, 8 + 2.", "Dentro del paréntesis las potencias se multiplican: se suman los exponentes, 8 + 2.")},
             "right": t("8 + 2 = 10; 10 − 3 = 7.", "8 + 2 = 10; 10 − 3 = 7."), "solution": t("Product: 8 + 2 = 10. Quotient: 10 − 3 = 7. So a<sup>7</sup>.", "Producto: 8 + 2 = 10. Cociente: 10 − 3 = 7. Así que a<sup>7</sup>.")},
      "p4": {"ok": "b", "hints": {"a": t("For b, subtract 2 − 4: the exponent is negative.", "Para la b, reste 2 − 4: el exponente queda negativo."), "c": t("It has the right value, but it still has a negative exponent: it is not in final form.", "Vale lo mismo, pero todavía tiene un exponente negativo: no está en forma final."), "d": t("The a has a positive exponent: it stays on top.", "La a tiene exponente positivo: se queda arriba.")},
             "right": t("a: 5 − 2 = 3; b: 2 − 4 = −2, so b goes to the bottom.", "a: 5 − 2 = 3; b: 2 − 4 = −2, así que la b baja."), "solution": t("a<sup>5 − 2</sup> = a<sup>3</sup> and b<sup>2 − 4</sup> = b<sup>−2</sup> = 1/b<sup>2</sup>. So a<sup>3</sup>/b<sup>2</sup>.", "a<sup>5 − 2</sup> = a<sup>3</sup> y b<sup>2 − 4</sup> = b<sup>−2</sup> = 1/b<sup>2</sup>. Así que a<sup>3</sup>/b<sup>2</sup>.")},
      "p5": {"ok": "c", "hints": {"a": t("A power raised to a power multiplies the exponents: 5 × 2 is not 7.", "Una potencia elevada a otra multiplica los exponentes: 5 × 2 no es 7."), "b": t("There is no division here. One power is raised to another.", "Aquí no hay división. Una potencia está elevada a otra.")},
             "right": "5 × 2 = 10.", "solution": t("Power of a power: 5 × 2 = 10, so a<sup>10</sup>. The mistake was adding.", "Potencia de una potencia: 5 × 2 = 10, así que a<sup>10</sup>. El error fue sumar.")},
      "p6": {"ok": "b", "hints": {"a": t("The powers are multiplied side by side: add the exponents, 4 + 2.", "Las potencias están multiplicadas una al lado de otra: se suman, 4 + 2."), "c": t("You subtract when you divide. Here you multiply.", "Se resta al dividir. Aquí se multiplica.")},
             "right": "4 + 2 = 6.", "solution": t("Product rule: 4 + 2 = 6, so x<sup>6</sup>. The mistake was multiplying the exponents.", "Regla del producto: 4 + 2 = 6, así que x<sup>6</sup>. El error fue multiplicar los exponentes.")},
      "p7": {"ok": "a", "hints": {"b": t("The 2 is inside the parentheses, so it is cubed too.", "El 2 está dentro del paréntesis: también se eleva al cubo."), "c": t("Cubing is not multiplying by 3: 2<sup>3</sup> = 8.", "Elevar al cubo no es multiplicar por 3: 2<sup>3</sup> = 8.")},
             "right": "2<sup>3</sup> = 8.", "solution": t("The exponent goes to each factor: 2<sup>3</sup> = 8, so 8x<sup>3</sup>.", "El exponente llega a cada factor: 2<sup>3</sup> = 8, así que 8x<sup>3</sup>.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("In the parentheses, multiply 2 × 3.", "En el paréntesis se multiplica 2 × 3."), "c": t("After the parentheses, add: 6 + 4.", "Después del paréntesis se suma: 6 + 4."), "d": t("Check: 2 × 3 = 6, then 6 + 4.", "Revise: 2 × 3 = 6, después 6 + 4.")}, "solution": t("(x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>; x<sup>6</sup> · x<sup>4</sup> = x<sup>10</sup>.", "(x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>; x<sup>6</sup> · x<sup>4</sup> = x<sup>10</sup>.")},
      "B": {"ok": "b", "hints": {"a": t("The 2 is squared too: 2<sup>2</sup> = 4.", "El 2 también se eleva al cuadrado: 2<sup>2</sup> = 4."), "c": t("For a<sup>3</sup> squared, multiply 3 × 2.", "Para a<sup>3</sup> al cuadrado, multiplique 3 × 2."), "d": t("Raise the 2, and multiply 3 × 2.", "Eleve el 2, y multiplique 3 × 2.")}, "solution": t("2<sup>2</sup> = 4 and 3 × 2 = 6: 4a<sup>6</sup>.", "2<sup>2</sup> = 4 y 3 × 2 = 6: 4a<sup>6</sup>.")},
      "C": {"ok": "c", "hints": {"a": t("You did not divide. Subtract 2 at the end.", "No dividió. Al final se resta 2."), "b": t("Check: 5 + 3 = 8, then 8 − 2.", "Revise: 5 + 3 = 8, después 8 − 2."), "d": t("Inside the parentheses, add 5 + 3.", "Dentro del paréntesis se suma 5 + 3.")}, "solution": t("5 + 3 = 8; 8 − 2 = 6: x<sup>6</sup>.", "5 + 3 = 8; 8 − 2 = 6: x<sup>6</sup>.")},
      "D": {"ok": "d", "hints": {"a": t("You left out the y at the end: it is y<sup>1</sup>.", "Le faltó la y del final: vale y<sup>1</sup>."), "b": t("Squaring 3 gives 9, not 6.", "3 al cuadrado da 9, no 6."), "c": t("The 3 is squared too: 9.", "El 3 también se eleva al cuadrado: 9.")}, "solution": t("(3y<sup>2</sup>)<sup>2</sup> = 9y<sup>4</sup>; 9y<sup>4</sup> · y = 9y<sup>5</sup>.", "(3y<sup>2</sup>)<sup>2</sup> = 9y<sup>4</sup>; 9y<sup>4</sup> · y = 9y<sup>5</sup>.")},
      "E": {"ok": "c", "hints": {"a": t("You added. Multiply each exponent by 3.", "Sumó. Multiplique cada exponente por 3."), "b": t("For y, multiply 2 × 3.", "Para la y, multiplique 2 × 3."), "d": t("Check the y: 2 × 3 = 6.", "Revise la y: 2 × 3 = 6.")}, "solution": t("x: 4 × 3 = 12; y: 2 × 3 = 6: x<sup>12</sup>y<sup>6</sup>.", "x: 4 × 3 = 12; y: 2 × 3 = 6: x<sup>12</sup>y<sup>6</sup>.")},
      "F": {"ok": "d", "hints": {"a": t("You did not divide by a<sup>2</sup>.", "No dividió entre a<sup>2</sup>."), "b": t("Inside, (a<sup>2</sup>)<sup>3</sup> = a<sup>6</sup>; then add 1; then subtract 2.", "Dentro, (a<sup>2</sup>)<sup>3</sup> = a<sup>6</sup>; después sume 1; después reste 2."), "c": t("You left out the a, which is a<sup>1</sup>.", "Le faltó la a, que vale a<sup>1</sup>.")}, "solution": t("(a<sup>2</sup>)<sup>3</sup> = a<sup>6</sup>; · a = a<sup>7</sup>; ÷ a<sup>2</sup> = a<sup>5</sup>.", "(a<sup>2</sup>)<sup>3</sup> = a<sup>6</sup>; · a = a<sup>7</sup>; ÷ a<sup>2</sup> = a<sup>5</sup>.")},
      "G": {"ok": "a", "hints": {"b": t("For x, 6 − 2 = 4.", "Para la x, 6 − 2 = 4."), "c": t("The y on the bottom is y<sup>1</sup>: subtract 2 − 1.", "La y de abajo es y<sup>1</sup>: reste 2 − 1."), "d": t("You added. When you divide, subtract.", "Sumó. Al dividir, se resta.")}, "solution": t("x: 6 − 2 = 4; y: 2 − 1 = 1: x<sup>4</sup>y.", "x: 6 − 2 = 4; y: 2 − 1 = 1: x<sup>4</sup>y.")},
      "H": {"ok": "c", "hints": {"a": t("There is a mistake: the 2 was not raised.", "Sí hay un error: no se elevó el 2."), "b": t("Cubing is not multiplying by 3.", "Elevar al cubo no es multiplicar por 3."), "d": t("The x is raised correctly; the problem is the 2.", "La x sí se elevó bien; el problema es el 2.")}, "solution": t("The 2 is raised too: (2x)<sup>3</sup> = 8x<sup>3</sup>.", "El 2 también se eleva: (2x)<sup>3</sup> = 8x<sup>3</sup>.")}
     }}

    quiz = [
     ("A", t("Simplify (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>.", "Simplifique (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>."), [("a", "x<sup>10</sup>"), ("b", "x<sup>9</sup>"), ("c", "x<sup>24</sup>"), ("d", "x<sup>5</sup>")]),
     ("B", t("Simplify (2a<sup>3</sup>)<sup>2</sup>.", "Simplifique (2a<sup>3</sup>)<sup>2</sup>."), [("a", "2a<sup>6</sup>"), ("b", "4a<sup>6</sup>"), ("c", "4a<sup>5</sup>"), ("d", "2a<sup>5</sup>")]),
     ("C", t("Simplify (x<sup>5</sup> · x<sup>3</sup>) ÷ x<sup>2</sup>.", "Simplifique (x<sup>5</sup> · x<sup>3</sup>) ÷ x<sup>2</sup>."), [("a", "x<sup>10</sup>"), ("b", "x<sup>7</sup>"), ("c", "x<sup>6</sup>"), ("d", "x<sup>13</sup>")]),
     ("D", t("Simplify (3y<sup>2</sup>)<sup>2</sup> · y.", "Simplifique (3y<sup>2</sup>)<sup>2</sup> · y."), [("a", "9y<sup>4</sup>"), ("b", "6y<sup>5</sup>"), ("c", "3y<sup>5</sup>"), ("d", "9y<sup>5</sup>")]),
     ("E", t("Simplify (x<sup>4</sup>y<sup>2</sup>)<sup>3</sup>.", "Simplifique (x<sup>4</sup>y<sup>2</sup>)<sup>3</sup>."), [("a", "x<sup>7</sup>y<sup>5</sup>"), ("b", "x<sup>12</sup>y<sup>5</sup>"), ("c", "x<sup>12</sup>y<sup>6</sup>"), ("d", "x<sup>12</sup>y<sup>8</sup>")]),
     ("F", t("Simplify ((a<sup>2</sup>)<sup>3</sup> · a) ÷ a<sup>2</sup>.", "Simplifique ((a<sup>2</sup>)<sup>3</sup> · a) ÷ a<sup>2</sup>."), [("a", "a<sup>7</sup>"), ("b", "a<sup>6</sup>"), ("c", "a<sup>4</sup>"), ("d", "a<sup>5</sup>")]),
     ("G", t("Simplify (x<sup>6</sup>y<sup>2</sup>) ÷ (x<sup>2</sup>y).", "Simplifique (x<sup>6</sup>y<sup>2</sup>) ÷ (x<sup>2</sup>y)."), [("a", "x<sup>4</sup>y"), ("b", "x<sup>3</sup>y"), ("c", "x<sup>4</sup>y<sup>2</sup>"), ("d", "x<sup>8</sup>y<sup>3</sup>")]),
     ("H", t("What is the mistake in “(2x)<sup>3</sup> = 2x<sup>3</sup>”?", "¿Cuál es el error en «(2x)<sup>3</sup> = 2x<sup>3</sup>»?"),
      [("a", t("There is no mistake", "No hay error")), ("b", t("The answer is 6x<sup>3</sup>", "El resultado es 6x<sup>3</sup>")), ("c", t("The 2 is raised too: 8x<sup>3</sup>", "El 2 también se eleva: 8x<sup>3</sup>")), ("d", t("The x is not raised", "La x no se eleva"))])]

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("No new rules: the five you know, combined in order, with an answer that has only positive exponents.", "Sin reglas nuevas: las cinco que ya conoce, combinadas con orden y con un resultado solo con exponentes positivos."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Simplify</strong> expressions that need two or more rules of exponents in a row.", "<strong>Simplificar</strong> expresiones que requieren aplicar dos o más reglas de los exponentes en secuencia."),
         t("<strong>Follow</strong> an order: parentheses with an exponent first, then products and quotients.", "<strong>Seguir</strong> un orden de trabajo: primero los paréntesis con exponente, luego los productos y cocientes."),
         t("<strong>Give</strong> the final answer with positive exponents only.", "<strong>Expresar</strong> siempre el resultado final con exponentes positivos."),
         t("<strong>Find and fix</strong> the most common mistakes in a simplification.", "<strong>Identificar y corregir</strong> los errores más comunes en una simplificación.")],
        secciones,
        (t("Simplify six expressions that combine three or more rules, following the order of the lesson and writing the rule at each step; and four expressions with fractions and negative exponents, with the answer in positive exponents. Then be the referee four times: write a simplification with one mistake, swap it with a classmate or check it the next day, and say in which step it went wrong. Last, solve one long expression twice, on different days, without looking at the first try, and compare.",
           "Simplifique seis expresiones que combinen tres o más reglas, siguiendo el orden de la lección y anotando la regla de cada paso; y cuatro expresiones con fracciones y exponentes negativos, con el resultado en exponentes positivos. Después sea árbitro cuatro veces: escriba una simplificación con un error, cámbiela con un compañero o revísela al día siguiente, y diga en qué paso se torció. Por último, resuelva una expresión larga dos veces, en días distintos, sin mirar la primera versión, y compare."),
         t("Explain the route (parentheses, then product and quotient, then positive exponents) to someone at home using one of your homework expressions. Teaching a method is one of the best ways to make it stick.",
           "Explíquele a alguien de su casa la ruta (paréntesis, después producto y cociente, después exponentes positivos) con una de las expresiones de su tarea. Enseñar un método es una de las mejores maneras de fijarlo.")),
        quiz,
        t("Self-check checklist for simplifying with several rules", "Lista de autoevaluación para simplificar con varias reglas"),
        t("Self-check checklist: skills for simplifying with several rules of exponents", "Lista de autoevaluación: destrezas para simplificar con varias reglas de los exponentes"),
        [(t("Choosing the rule", "Elegir la regla"), t("I use the right rule at each step and can say why I chose that order.", "Aplico la regla correcta en cada paso y sé explicar por qué elegí ese orden."), t("I use the rules, but sometimes in the wrong order.", "Aplico las reglas, pero a veces en el orden equivocado."), t("I do not know which rule to use at each step.", "No sé qué regla aplicar en cada paso.")),
         (t("Showing the steps", "Mostrar los pasos"), t("I write every step and the rule I used.", "Escribo cada paso y la regla que usé."), t("I show some steps and skip others.", "Muestro algunos pasos y me salto otros."), t("I jump to the answer without the work.", "Salto al resultado sin mostrar el proceso.")),
         (t("Positive exponents", "Exponentes positivos"), t("My answers have only positive exponents, and I check them with a number.", "Mis resultados solo tienen exponentes positivos y los compruebo con un número."), t("I rewrite some negative exponents, not all.", "Reescribo algunos exponentes negativos, no todos."), t("I leave negative exponents in the answer.", "Dejo exponentes negativos en el resultado.")),
         (t("Finding mistakes", "Detectar errores"), t("I find the wrong step, fix it, and name the rule that was misused.", "Encuentro el paso equivocado, lo corrijo y nombro la regla mal aplicada."), t("I see the mistake but do not fix it well.", "Veo el error, pero no lo corrijo bien."), t("I cannot tell if a solution is right.", "No sé decir si una solución está bien."))],
        t("<p>This lesson closes Topic 1. You know the <strong>five rules of exponents</strong> and, above all, how to <strong>combine them in order</strong>: parentheses first, then products and quotients, and an answer with <strong>positive exponents</strong>. You also learned to act as a referee and fix common mistakes.</p>\n<p>Topic 2 opens with <strong>Lesson 2.1 · Scientific notation and orders of magnitude</strong>, where these rules come to life: scientific notation uses powers of 10, with positive and negative exponents, to write numbers as large as the mass of the Sun or as small as the width of an atom.</p>",
          "<p>Con esta lección se cierra el Tema 1. Ya domina las <strong>cinco reglas de los exponentes</strong> y, sobre todo, cómo <strong>combinarlas con orden</strong>: primero los paréntesis, luego productos y cocientes, y un resultado con <strong>exponentes positivos</strong>. También aprendió a actuar como árbitro y a corregir los errores más frecuentes.</p>\n<p>El Tema 2 abre con la <strong>Lección 2.1 · Conversión decimal ↔ científica y órdenes de magnitud</strong>, donde estas reglas cobran vida: la notación científica usa potencias de 10, con exponentes positivos y negativos, para escribir números tan grandes como la masa del Sol o tan pequeños como el ancho de un átomo.</p>"),
        ("2-1", ("", t("Lesson 2.1 · Scientific notation and orders of magnitude", "Lección 2.1 · Conversión decimal ↔ científica y órdenes de magnitud"))),
        [(t("simplify", "simplificar"), t("Write an expression in its shortest equal form, with each base once and positive exponents.", "Escribir una expresión en su forma equivalente más corta, con cada base una sola vez y exponentes positivos.")),
         (t("final form", "forma final"), t("An answer with no parentheses left, each base written once, and no negative exponents.", "Un resultado sin paréntesis pendientes, con cada base una sola vez y sin exponentes negativos.")),
         (t("route", "ruta"), t("The fixed order of steps: parentheses, then product and quotient, then positive exponents.", "El orden fijo de pasos: paréntesis, después producto y cociente, después exponentes positivos.")),
         (t("test value", "valor de prueba"), t("A number, like 2 or 3, put in place of the letter to check that two expressions are equal.", "Un número, como 2 o 3, que se pone en lugar de la letra para comprobar que dos expresiones son iguales."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function sim(){ return T("Simplify ", "Simplifique "); }
function mx(c, v, e){ return mLinea(mono(c, e1(v, e))); }
var RP = T("product", "producto"), RPP = T("power of a power", "potencia de una potencia"), RPX = T("power of a product", "potencia de un producto"),
    RC = T("quotient", "cociente"), RN = T("negative exponent", "exponente negativo"), RF = T("final form", "forma final");

/* ============ MODULE 1 · the route, step by step (fixed examples) ============ */
var RUTAS = [
  { expr: porX(parX(xp("x", 2), 3), xp("x", 4)),
    pasos: [ver(igualX(parX(xp("x", 2), 3), xp("x", 6))) + T(": the exponents are multiplied, 2 × 3 = 6.", ": los exponentes se multiplican, 2 × 3 = 6.") + R_(RPP),
            ver(igualX(porX(xp("x", 6), xp("x", 4)), xp("x", 10))) + T(": they are added, 6 + 4 = 10.", ": se suman, 6 + 4 = 10.") + R_(RP),
            T("No negative exponents are left. Answer: ", "No quedan exponentes negativos. Resultado: ") + ver(xp("x", 10)) + "."] },
  { expr: porX(parX(mx(2, "a", 3), 2), X("a", "a")),
    pasos: [ver(igualX(parX(mx(2, "a", 3), 2), mx(4, "a", 6))) + T(": the 2 is raised too, 2<sup>2</sup> = 4; and 3 × 2 = 6.", ": el 2 también se eleva, 2<sup>2</sup> = 4; y 3 × 2 = 6.") + R_(RPX),
            ver(igualX(porX(mx(4, "a", 6), X("a", "a")), mx(4, "a", 7))) + T(": the a on its own is a<sup>1</sup>, 6 + 1 = 7.", ": la a sola vale a<sup>1</sup>, 6 + 1 = 7.") + R_(RP),
            T("Answer: ", "Resultado: ") + ver(mx(4, "a", 7)) + "."] },
  { expr: entreX(parX(porX(xp("a", 8), xp("a", 2))), xp("a", 3)),
    pasos: [T("Inside the parentheses: ", "Dentro del paréntesis: ") + ver(igualX(porX(xp("a", 8), xp("a", 2)), xp("a", 10))) + ", 8 + 2 = 10." + R_(RP),
            ver(igualX(entreX(xp("a", 10), xp("a", 3)), xp("a", 7))) + T(": they are subtracted, 10 − 3 = 7.", ": se restan, 10 − 3 = 7.") + R_(RC),
            T("Answer: ", "Resultado: ") + ver(xp("a", 7)) + "."] },
  { expr: entreX(parX(mx(3, "x", 2), 3), xp("x", 8)),
    pasos: [ver(igualX(parX(mx(3, "x", 2), 3), mx(27, "x", 6))) + T(": 3<sup>3</sup> = 27 and 2 × 3 = 6.", ": 3<sup>3</sup> = 27 y 2 × 3 = 6.") + R_(RPX),
            ver(igualX(entreX(mx(27, "x", 6), xp("x", 8)), mx(27, "x", -2))) + ": 6 − 8 = " + MENOS + "2." + R_(RC),
            ver(igualX(mx(27, "x", -2), fracX(X("27", "27"), xp("x", 2)))) + T(": the x moves to the bottom with a positive exponent; the 27 stays on top.", ": la x pasa abajo con exponente positivo; el 27 se queda arriba.") + R_(RN),
            T("Answer: ", "Resultado: ") + ver(fracX(X("27", "27"), xp("x", 2))) + "."] },
  { expr: entreX(porX(parX(mLinea(mono(1, {x: 4, y: 1})), 2), xp("y", 3)), xp("x", 5)),
    pasos: [ver(igualX(parX(mLinea(mono(1, {x: 4, y: 1})), 2), mLinea(mono(1, {x: 8, y: 2})))) + T(": the 2 goes to both the x and the y.", ": el 2 se reparte a la x y a la y.") + R_(RPX),
            T("Multiply by ", "Se multiplica por ") + ver(xp("y", 3)) + T(": the y becomes y<sup>2+3</sup> = y<sup>5</sup>; the x does not change.", ": la y pasa a y<sup>2+3</sup> = y<sup>5</sup>; la x no cambia.") + R_(RP),
            T("Divide by ", "Se divide entre ") + ver(xp("x", 5)) + T(": the x becomes x<sup>8−5</sup> = x<sup>3</sup>; the y does not change.", ": la x pasa a x<sup>8−5</sup> = x<sup>3</sup>; la y no cambia.") + R_(RC),
            T("Answer: ", "Resultado: ") + ver(mLinea(mono(1, {x: 3, y: 5}))) + T(". Each base is worked separately.", ". Cada base se trabaja por separado.")] },
  { expr: entreX(porX(parX(mx(2, "x", 3), 2), X("x", "x")), xp("x", 9)),
    pasos: [ver(igualX(parX(mx(2, "x", 3), 2), mx(4, "x", 6))) + T(": 2<sup>2</sup> = 4 and 3 × 2 = 6.", ": 2<sup>2</sup> = 4 y 3 × 2 = 6.") + R_(RPX),
            ver(igualX(porX(mx(4, "x", 6), X("x", "x")), mx(4, "x", 7))) + ": 6 + 1 = 7." + R_(RP),
            ver(igualX(entreX(mx(4, "x", 7), xp("x", 9)), mx(4, "x", -2))) + ": 7 − 9 = " + MENOS + "2." + R_(RC),
            ver(igualX(mx(4, "x", -2), fracX(X("4", "4"), xp("x", 2)))) + "." + R_(RN),
            T("Answer: ", "Resultado: ") + ver(fracX(X("4", "4"), xp("x", 2))) + T(". Check with x = 2: the original gives (2 · 8)<sup>2</sup> · 2 ÷ 512 = 1, and 4/2<sup>2</sup> = 1. They match.", ". Comprobación con x = 2: la original da (2 · 8)<sup>2</sup> · 2 ÷ 512 = 1, y 4/2<sup>2</sup> = 1. Coinciden.")] }
];
var O = {i: 0, paso: 0};
function llenaRutas(){
  RUTAS.forEach(function(r, i){
    var op = document.createElement("option");
    op.value = i; op.textContent = r.expr.h.replace(/<sup>/g, "^").replace(/<\/sup>/g, "").replace(/<[^>]+>/g, "").replace(/\s+/g, " ");
    $("o-expr").appendChild(op);
  });
}
function reiniciaRuta(){
  O.i = parseInt($("o-expr").value, 10) || 0; O.paso = 0;
  $("o-visual").innerHTML = ver(RUTAS[O.i].expr); $("o-pasos").innerHTML = "";
  $("o-siguiente").textContent = T("Show the first step", "Mostrar el primer paso"); $("o-siguiente").disabled = false;
}
function pintaPasosRuta(){
  var r = RUTAS[O.i];
  $("o-pasos").innerHTML = r.pasos.slice(0, O.paso).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i + 1) + "</span>" + p + "</div>"; }).join("");
  if (O.paso >= r.pasos.length){ $("o-siguiente").textContent = T("No more steps", "No hay más pasos"); $("o-siguiente").disabled = true; }
  else $("o-siguiente").textContent = T("Show step ", "Mostrar el paso ") + (O.paso + 1);
}
function opcionesConLinea(R, dis){
  var ops = opcionesMono(R, dis);
  if (R.o.some(function(v){ return (R.e[v] || 0) < 0; })){
    ops = ops.slice(0, 3);
    ops.push({x: mLinea(R), ok: false, fb: T("That has the same value, but it still has a negative exponent: it is not in final form.", "Esa expresión vale lo mismo, pero todavía tiene un exponente negativo: no está en forma final.")});
  }
  return ops;
}
function genOrden(){
  var t = ale(1, 3), v = elige(["x", "a", "m"]), R, ex, dis, sol;
  if (t === 1){
    var a = ale(2, 4), n = ale(2, 3), b = ale(1, 5), d = ale(2, 12), r = a * n + b - d;
    R = mDiv(mMul(xv(v, a * n), xv(v, b)), xv(v, d)); ex = entreX(porX(parX(xp(v, a), n), xp(v, b)), xp(v, d));
    dis = [[xv(v, a + n + b - d), T("In the parentheses the exponents are multiplied, not added.", "En el paréntesis los exponentes se multiplican, no se suman.")],
           [xv(v, -r), T("Check the subtraction of the quotient: top minus bottom.", "Revise la resta del cociente: arriba menos abajo.")],
           [xv(v, a * n * b - d), T("After the parentheses, the product adds exponents.", "Tras el paréntesis, el producto suma exponentes.")]];
    sol = pasosHTML([T("Parentheses: ", "Paréntesis: ") + a + " × " + n + " = " + (a * n) + "." + R_(RPP), T("Product: ", "Producto: ") + (a * n) + " + " + b + " = " + (a * n + b) + "." + R_(RP),
                     T("Quotient: ", "Cociente: ") + (a * n + b) + " − " + d + " = " + numTxt(r) + "." + R_(RC) + (r < 0 ? T(" The negative exponent moves to the bottom.", " El exponente negativo pasa abajo.") + R_(RN) : (r === 0 ? T(" And ", " Y ") + v + "<sup>0</sup> = 1." : ""))]);
  } else if (t === 2){
    var c = ale(2, 3), a2 = ale(1, 4), n2 = ale(2, 3), d2 = ale(2, 10), cn = Math.pow(c, n2);
    R = mDiv(mPow(mono(c, e1(v, a2)), n2), xv(v, d2)); ex = entreX(parX(mx(c, v, a2), n2), xp(v, d2));
    dis = [[mDiv(mono(c, e1(v, a2 * n2)), xv(v, d2)), T("The number still has to be raised: ", "Falta elevar el coeficiente: ") + c + "<sup>" + n2 + "</sup> = " + cn + "."],
           [mDiv(mono(c * n2, e1(v, a2 * n2)), xv(v, d2)), T("The number is raised, not multiplied by the exponent.", "El coeficiente se eleva, no se multiplica por el exponente.")],
           [mDiv(mono(cn, e1(v, a2 + n2)), xv(v, d2)), T("Inside the parentheses the exponents are multiplied.", "Dentro del paréntesis los exponentes se multiplican.")]];
    sol = pasosHTML([T("Parentheses: ", "Paréntesis: ") + c + "<sup>" + n2 + "</sup> = " + cn + T(" and ", " y ") + a2 + " × " + n2 + " = " + (a2 * n2) + "." + R_(RPX),
                     T("Quotient: ", "Cociente: ") + (a2 * n2) + " − " + d2 + " = " + numTxt(a2 * n2 - d2) + "." + R_(RC) + (a2 * n2 - d2 < 0 ? T(" The " + v + " moves to the bottom; the number stays on top.", " La " + v + " pasa abajo; el coeficiente se queda arriba.") + R_(RN) : "")]);
  } else {
    var p = ale(2, 7), q = ale(1, 5), d3 = ale(2, 9);
    R = mDiv(xv(v, p + q), xv(v, d3)); ex = entreX(parX(porX(xp(v, p), xp(v, q))), xp(v, d3));
    dis = [[xv(v, p * q - d3), T("There is a product inside the parentheses: the exponents are added.", "Dentro del paréntesis hay un producto: los exponentes se suman.")],
           [xv(v, d3 - p - q), T("Top minus bottom, not the other way around.", "Arriba menos abajo, no al revés.")],
           [xv(v, p + q + d3), T("When you divide, the exponents are subtracted.", "Al dividir, los exponentes se restan.")]];
    sol = pasosHTML([T("Product inside the parentheses: ", "Producto dentro del paréntesis: ") + p + " + " + q + " = " + (p + q) + "." + R_(RP), T("Quotient: ", "Cociente: ") + (p + q) + " − " + d3 + " = " + numTxt(p + q - d3) + "." + R_(RC)]);
  }
  return {enun: sim() + ver(ex) + T(" and leave no negative exponents.", " y deje el resultado sin exponentes negativos."), opciones: opcionesConLinea(R, dis), sol: sol};
}

/* ============ MODULE 2 · fractions with two bases ============ */
function genFracciones(){
  var pares = [[12, 4], [10, 2], [18, 6], [15, 5], [8, 12], [6, 9], [20, 8], [14, 21], [9, 3], [16, 4], [4, 10], [6, 4]];
  var cc = elige(pares), c1 = cc[0], c2 = cc[1], a = ale(1, 7), b = ale(1, 6), c = ale(1, 7), d = ale(1, 6);
  if (a === c) c = a + 2;
  var A = mono(c1, {x: a, y: b}), B = mono(c2, {x: c, y: d}), R = mDiv(A, B), g = mcd(c1, c2);
  var dis = [[M(c1, c2, {x: c - a, y: b - d}), T("For x you subtracted backward: it is always the top exponent minus the bottom one.", "Para la x restó al revés: siempre es el exponente de arriba menos el de abajo.")],
             [M(c1, c2, {x: a + c, y: b + d}), T("When you divide, the exponents are subtracted.", "Al dividir, los exponentes se restan.")],
             [M(c1 - c2 === 0 ? 1 : c1 - c2, 1, {x: a - c, y: b - d}), T("You subtracted the numbers; divide them like a fraction: ", "Restó los coeficientes; se dividen como una fracción: ") + c1 + "/" + c2 + "."]];
  var pasos = [T("Numbers: ", "Coeficientes: ") + c1 + "/" + c2 + (g > 1 ? " = " + (c1 / g) + (c2 / g === 1 ? "" : "/" + (c2 / g)) + T(" (divide top and bottom by ", " (se divide arriba y abajo entre ") + g + ")" : "") + ".",
               T("The x: ", "La x: ") + a + " − " + c + " = " + numTxt(a - c) + T(". The y: ", ". La y: ") + b + " − " + d + " = " + numTxt(b - d) + "." + R_(RC),
               T("Factors with a negative exponent move to the bottom with a positive exponent; factors with exponent 0 disappear.", "Los factores con exponente negativo pasan al denominador con exponente positivo; los de exponente 0 desaparecen.") + R_(RF)];
  return {enun: sim() + ver(fracX(mLinea(A), mLinea(B))) + ".", opciones: opcionesConLinea(R, dis), sol: pasosHTML(pasos)};
}

/* ============ MODULE 3 · the referee ============ */
function genArbitro(){
  var v = elige(["x", "a", "y"]), t = ale(1, 8), bien = Math.random() < 0.3, ex, cor, err, porque, falsa;
  var a = ale(2, 6), b = ale(2, 5), c = ale(2, 4);
  if (a === b) b = a + 1;
  function cv(k, e){ return X(k + v + "<sup>" + numTxt(e) + "</sup>", k + " " + v + VZ.pot + numVoz(e)); }
  if (t === 1){ ex = porX(xp(v, a), xp(v, b)); cor = xp(v, a + b); err = xp(v, a * b);
    porque = T("The exponents are added: ", "Los exponentes se suman: ") + a + " + " + b + " = " + (a + b) + "."; falsa = [xp(v, a - b > 0 ? a - b : a + b + 1), T("The exponents are subtracted", "Los exponentes se restan")]; }
  else if (t === 2){ ex = parX(xp(v, a), b); cor = xp(v, a * b); err = xp(v, a + b);
    porque = T("The exponents are multiplied: ", "Los exponentes se multiplican: ") + a + " × " + b + " = " + (a * b) + "."; falsa = [xp(v, a * b + 1), T("Add 1 to the product", "Hay que sumar 1 al producto")]; }
  else if (t === 3){ var n = ale(2, 3); if (c === 2 && n === 2) n = 3; ex = parX(X(c + v, c + " " + v), n); cor = cv(Math.pow(c, n), n); err = cv(c, n);
    porque = T("The " + c + " is raised too: ", "El " + c + " también se eleva: ") + c + "<sup>" + n + "</sup> = " + Math.pow(c, n) + "."; falsa = [cv(c * n, n), T("Multiply the number by the exponent", "Se multiplica el coeficiente por el exponente")]; }
  else if (t === 4){ var n4 = ale(2, 3); if (c === 2 && n4 === 2) n4 = 3; ex = parX(X(c + v, c + " " + v), n4); cor = cv(Math.pow(c, n4), n4); err = cv(c * n4, n4);
    porque = T("Raising is not multiplying: ", "Elevar no es multiplicar: ") + c + "<sup>" + n4 + "</sup> = " + Math.pow(c, n4) + T(", not ", ", no ") + c + " × " + n4 + "."; falsa = [cv(c, n4), T("The number is not touched", "El coeficiente no se toca")]; }
  else if (t === 5){ var m = b + ale(1, 5); ex = entreX(xp(v, m), xp(v, b)); cor = xp(v, m - b); err = fracX(X("1", "1"), xp(v, m - b));
    porque = T("It is the top exponent minus the bottom one: ", "Es el exponente de arriba menos el de abajo: ") + m + " − " + b + " = " + (m - b) + T("; the answer stays on top.", "; el resultado queda en el numerador."); falsa = [xp(v, m + b), T("When you divide, add the exponents", "Al dividir se suman los exponentes")]; }
  else if (t === 6){ ex = parX(X(c + v, c + " " + v), 0); cor = X("1", "1"); err = X("0", "0");
    porque = T("Any base other than zero to the power 0 is 1, not 0.", "Cualquier base distinta de cero con exponente 0 vale 1, no 0."); falsa = [X(String(c), String(c)), T("Only the " + v + " turns into 1", "Solo la " + v + " se convierte en 1")]; }
  else if (t === 7){ var k = ale(2, 4); ex = xp(String(c), -k); cor = X("1/" + Math.pow(c, k), "1" + VZ.sobre + Math.pow(c, k)); err = X(MENOS + Math.pow(c, k), numVoz(-Math.pow(c, k)));
    porque = T("A negative exponent means the reciprocal: ", "El exponente negativo indica el recíproco: ") + c + "<sup>" + MENOS + k + "</sup> = 1/" + Math.pow(c, k) + T(", a positive number.", ", un número positivo."); falsa = [X(MENOS + (c * k), numVoz(-c * k)), T("Multiply the base by the exponent", "Se multiplica la base por el exponente")]; }
  else { var k8 = ale(2, 5), c8 = ale(2, 7); ex = cv(c8, -k8); cor = fracX(X(String(c8), String(c8)), xp(v, k8)); err = fracX(X("1", "1"), cv(c8, k8));
    porque = T("The negative exponent belongs only to the " + v + ": the " + c8 + " stays on top.", "El exponente negativo solo afecta a la " + v + ": el " + c8 + " se queda arriba."); falsa = [X(MENOS + c8 + v + "<sup>" + k8 + "</sup>", T("minus ", "menos ") + c8 + " " + v + VZ.pot + k8), T("The sign of the exponent goes to the term", "El signo del exponente pasa al término")]; }
  var ops = bien
    ? [htmlOp(T("It is correct.", "Está correcto."), true, porque), htmlOp(T("Correction: ", "Corrección: ") + ver(err) + ".", false, T("That “correction” brings in the typical mistake. Look again at the rule.", "Esa «corrección» introduce el error típico. Revise otra vez la regla.")), htmlOp(falsa[1] + ": " + ver(falsa[0]) + ".", false, T("That is not how the rule works. Look again at the shape of the expression.", "La regla no funciona así. Revise otra vez la forma de la expresión."))]
    : [htmlOp(T("Correction: ", "Corrección: ") + ver(cor) + ".", true, porque), htmlOp(T("It is correct.", "Está correcto."), false, T("It has a mistake. Look again at which rule fits.", "Tiene un error. Revise otra vez qué regla corresponde.")), htmlOp(falsa[1] + ": " + ver(falsa[0]) + ".", false, T("That is not how the rule works. Look again at the shape of the expression.", "La regla no funciona así. Revise otra vez la forma de la expresión."))];
  return {enun: T("A student wrote ", "Un estudiante escribió ") + ver(igualX(ex, bien ? cor : err)) + T(". What is the right call?", ". ¿Qué corresponde?"), opciones: ops, sol: ""};
}

/* ============ MODULE 4 · a complete expression, box by box ============ */
var C = {q: null, intentos: [0, 0, 0, 0, 0], hechos: [false, false, false, false, false], ayuda: false, resueltas: 0, total: 0, cerrada: false};
function nuevaCompleta(){
  var c, a, n, b, d, e3;
  do { c = ale(2, 3); a = ale(1, 4); n = ale(2, 3); b = ale(1, 4); d = ale(2, 14); e3 = a * n + b - d; } while (e3 === 0 || Math.abs(e3) > 5 || Math.pow(c, n) > 27);
  C.q = {c: c, a: a, n: n, b: b, d: d, coef: Math.pow(c, n), e1: a * n, e2: a * n + b, e3: e3};
  C.intentos = [0, 0, 0, 0, 0]; C.hechos = [false, false, false, false, false]; C.ayuda = false; C.cerrada = false;
  var dentro = mx(c, "x", a);
  $("c-expr").innerHTML = ver(entreX(porX(parX(dentro, n), xp("x", b)), xp("x", d))) + ".";
  $("c-par").innerHTML = ver(parX(dentro, n));
  $("c-t2").innerHTML = T("Multiply the answer of step 1 by ", "Multiplique el resultado del paso 1 por ") + ver(xp("x", b)) + T(". The number does not change.", ". El coeficiente no cambia.");
  $("c-t3").innerHTML = T("Divide by ", "Divida entre ") + ver(xp("x", d)) + ".";
  $("c-t4").innerHTML = T("Leave no negative exponents. The number stays on top.", "Deje el resultado sin exponentes negativos. El coeficiente se queda en el numerador.");
  ["c-coef", "c-e1", "c-e2", "c-e3", "c-e4"].forEach(function(id){ $(id).value = ""; $(id).className = "corto"; });
  $("c-donde").value = ""; $("c-donde").className = "";
  for (var i = 1; i <= 4; i++){ $("c-fb" + i).className = "fb"; $("c-fb" + i).innerHTML = ""; }
  $("c-final").innerHTML = "";
  habilita();
}
function habilita(){
  [["c-coef", "c-e1", "c-v1"], ["c-e2", "c-v2"], ["c-e3", "c-v3"], ["c-donde", "c-e4", "c-v4"]].forEach(function(ids, i){
    var activo = !C.hechos[i + 1] && (i === 0 || C.hechos[i]);
    ids.forEach(function(id){ $(id).disabled = !activo; });
  });
}
function cierraPaso(k, bien, texto){
  var fb = $("c-fb" + k);
  if (bien){ C.hechos[k] = true; fb.className = "fb bien"; fb.innerHTML = "✓ " + texto; }
  else if (C.intentos[k] < 2){ fb.className = "fb pista"; fb.innerHTML = "<strong>" + T("Not yet.", "Todavía no.") + "</strong> " + texto + " <strong>" + T("You have one more try.", "Tiene un intento más.") + "</strong>"; return; }
  else { C.hechos[k] = true; C.ayuda = true; fb.className = "fb mal"; fb.innerHTML = texto; }
  habilita();
  if (k < 4) $(["c-e2", "c-e3", "c-donde"][k - 1]).focus(); else termina();
}
function marca(id, ok){ $(id).className = (id === "c-donde" ? "" : "corto ") + (ok ? "bien" : "error"); }
function verifica(k){
  var q = C.q;
  if (k === 1){
    var co = leeEnt($("c-coef").value), e = leeEnt($("c-e1").value);
    if (isNaN(co) || isNaN(e)){ $("c-fb1").className = "fb pista"; $("c-fb1").innerHTML = T("Type a whole number in each box.", "Escriba un número entero en cada casilla."); return; }
    C.intentos[1]++;
    var okC = co === q.coef, okE = e === q.e1; marca("c-coef", okC); marca("c-e1", okE);
    if (okC && okE) return cierraPaso(1, true, T("The number is ", "El coeficiente es ") + q.c + "<sup>" + q.n + "</sup> = " + q.coef + T(" and the exponent is ", " y el exponente ") + q.a + " × " + q.n + " = " + q.e1 + ".");
    var msg = [];
    if (!okC) msg.push(co === q.c ? T("the number is raised too", "el coeficiente también se eleva") : (co === q.c * q.n ? T("the number is raised, not multiplied by ", "el coeficiente se eleva, no se multiplica por ") + q.n : T("check ", "revise ") + q.c + "<sup>" + q.n + "</sup>"));
    if (!okE) msg.push(e === q.a + q.n ? T("inside the parentheses the exponents are multiplied", "dentro del paréntesis los exponentes se multiplican") : T("check ", "revise ") + q.a + " × " + q.n);
    if (C.intentos[1] >= 2){ $("c-coef").value = q.coef; $("c-e1").value = q.e1; marca("c-coef", true); marca("c-e1", true); }
    return cierraPaso(1, false, (C.intentos[1] >= 2 ? T("The answer was ", "La respuesta era ") + q.coef + "x<sup>" + q.e1 + "</sup>: " + msg.join("; ") : (function(s){ return s.charAt(0).toUpperCase() + s.slice(1); })(msg.join("; "))) + ".");
  }
  if (k === 2 || k === 3){
    var campo = k === 2 ? "c-e2" : "c-e3", v = leeEnt($(campo).value), esp = k === 2 ? q.e2 : q.e3;
    if (isNaN(v)){ $("c-fb" + k).className = "fb pista"; $("c-fb" + k).innerHTML = T("Type a whole number (it can start with a minus sign).", "Escriba un número entero (puede empezar con el signo menos)."); return; }
    C.intentos[k]++;
    if (v === esp){ marca(campo, true); return cierraPaso(k, true, k === 2 ? q.e1 + " + " + q.b + " = " + q.e2 + "." : q.e2 + " − " + q.d + " = " + numTxt(q.e3) + "."); }
    marca(campo, false);
    var pista = k === 2 ? (v === q.e1 * q.b ? T("In a product the exponents are added.", "En el producto los exponentes se suman.") : T("Add ", "Sume ") + q.e1 + " + " + q.b + ".")
                        : (v === q.d - q.e2 ? T("It is top minus bottom: ", "Es arriba menos abajo: ") + q.e2 + " − " + q.d + "." : T("Subtract ", "Reste ") + q.e2 + " − " + q.d + T("; the answer can be negative.", "; el resultado puede ser negativo."));
    if (C.intentos[k] >= 2){ $(campo).value = esp; marca(campo, true); }
    return cierraPaso(k, false, (C.intentos[k] >= 2 ? T("The answer was ", "La respuesta era ") + numTxt(esp) + ". " : "") + pista);
  }
  var donde = $("c-donde").value, e4 = leeEnt($("c-e4").value);
  if (!donde || isNaN(e4)){ $("c-fb4").className = "fb pista"; $("c-fb4").innerHTML = T("Choose where the x goes and type its exponent.", "Elija dónde queda la x y escriba su exponente."); return; }
  C.intentos[4]++;
  var dOk = q.e3 > 0 ? "arriba" : "abajo", eOk = Math.abs(q.e3);
  marca("c-donde", donde === dOk); marca("c-e4", e4 === eOk);
  if (donde === dOk && e4 === eOk) return cierraPaso(4, true, q.e3 < 0 ? T("The exponent " + numTxt(q.e3) + " becomes positive when the x moves to the bottom.", "El exponente " + numTxt(q.e3) + " se vuelve positivo al bajar la x al denominador.") : T("The exponent is already positive: the x stays on top.", "El exponente ya es positivo: la x se queda arriba."));
  var p4 = donde !== dOk ? (q.e3 < 0 ? T("With a negative exponent, the x moves to the bottom.", "Con exponente negativo, la x baja al denominador.") : T("With a positive exponent, the x stays on top.", "Con exponente positivo, la x se queda en el numerador.")) : T("When it crosses the bar, the exponent changes sign: it becomes ", "Al cruzar la barra, el exponente cambia de signo: queda ") + eOk + ".";
  if (C.intentos[4] >= 2){ $("c-donde").value = dOk; $("c-e4").value = eOk; marca("c-donde", true); marca("c-e4", true); }
  return cierraPaso(4, false, (C.intentos[4] >= 2 ? T("The right answer is now in the boxes. ", "La respuesta correcta ya está en las casillas. ") : "") + p4);
}
function termina(){
  if (C.cerrada) return;
  C.cerrada = true; C.total++; if (!C.ayuda) C.resueltas++;
  var q = C.q, R = M(q.coef, 1, {x: q.e3}), orig = mDiv(mMul(mPow(mono(q.c, {x: q.a}), q.n), xv("x", q.b)), xv("x", q.d));
  var vo = mValor(orig, {x: 2}), vr = mValor(R, {x: 2});
  $("c-final").innerHTML = '<div class="linea veredicto">' + T("Answer: ", "Resultado: ") + ver(mFinal(R)) + "</div>" +
    '<div class="linea">' + T("Check with x = 2: the original expression is ", "Comprobación con x = 2: la expresión original vale ") + ver(ratX(vo)) + T(" and the answer is ", " y el resultado vale ") + ver(ratX(vr)) + (ratIgual(vo, vr) ? T(". They match.", ". Coinciden.") : ".") + "</div>" +
    '<div class="linea">' + (C.ayuda ? T("You needed help on a step: try another expression to make it stick.", "Necesitó ayuda en algún paso: pruebe otra expresión para afianzarlo.") : T("Solved with no help. Well done!", "Resuelta sin ayuda. ¡Bien hecho!")) + "</div>";
  $("c-marc").textContent = T("Expressions solved with no help: ", "Expresiones resueltas sin ayuda: ") + C.resueltas + T(" of ", " de ") + C.total;
}
function solucionCompleta(){
  var q = C.q;
  $("c-coef").value = q.coef; $("c-e1").value = q.e1; $("c-e2").value = q.e2; $("c-e3").value = q.e3; $("c-donde").value = q.e3 > 0 ? "arriba" : "abajo"; $("c-e4").value = Math.abs(q.e3);
  ["c-coef", "c-e1", "c-e2", "c-e3", "c-donde", "c-e4"].forEach(function(id){ marca(id, true); });
  for (var k = 1; k <= 4; k++) if (!C.hechos[k]){ C.hechos[k] = true; C.ayuda = true; $("c-fb" + k).className = "fb"; $("c-fb" + k).innerHTML = T("Step shown by the solution.", "Paso mostrado por la solución."); }
  habilita(); termina();
}

/* ============ Start ============ */
llenaRutas();
$("o-expr").addEventListener("change", reiniciaRuta);
$("o-siguiente").addEventListener("click", function(){ if (O.paso < RUTAS[O.i].pasos.length){ O.paso++; pintaPasosRuta(); } });
$("o-todo").addEventListener("click", function(){ O.paso = RUTAS[O.i].pasos.length; pintaPasosRuta(); });
$("o-reiniciar").addEventListener("click", reiniciaRuta);
reiniciaRuta();
OM("p-orden", genOrden);
OM("p-fracciones", genFracciones);
OM("p-arbitro", genArbitro);
[1, 2, 3, 4].forEach(function(k){ $("c-v" + k).addEventListener("click", function(){ verifica(k); }); });
[["c-coef", 1], ["c-e1", 1], ["c-e2", 2], ["c-e3", 3], ["c-e4", 4]].forEach(function(p){ $(p[0]).addEventListener("keydown", function(e){ if (e.key === "Enter") verifica(p[1]); }); });
$("c-nuevo").addEventListener("click", function(){ nuevaCompleta(); $("c-coef").focus(); });
$("c-solucion").addEventListener("click", solucionCompleta);
nuevaCompleta();
'''

def caja_num(i, et):
    return f'<div class="campo"><label for="{i}">{et}</label><input type="text" autocomplete="off" class="corto" id="{i}"></div>'

def practica_pagina():
    n = N
    P = n3
    filas = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{d}</td></tr>" for a, b, c, d in n3.tabla_reglas(True))
    def paso(k, titulo, texto, campos, boton):
        return f'''        <div class="panel" id="c-paso{k}">
          <p><strong>{titulo}</strong> {texto}</p>
          <div class="campos">{campos}</div>
          <div class="fila-btn"><button type="button" class="btn" id="c-v{k}">{boton}</button></div>
          <div class="fb" id="c-fb{k}" role="status"></div>
        </div>'''
    href = "topic-1-check.html" if B.L == "en" else "comprobacion-tema-1.html"
    mods = [
     (t("order", "orden"), t("An order for simplifying", "Un orden para simplificar"),
      f'''      <p>{t("When an expression combines several rules, follow the same route every time:", "Cuando una expresión combina varias reglas, conviene seguir siempre la misma ruta:")}</p>
      <ol>
        <li>{t("<strong>Parentheses with an exponent:</strong> power of a power and power of a product, without forgetting to raise the numbers.", "<strong>Paréntesis con exponente:</strong> potencia de una potencia y potencia de un producto, sin olvidar elevar los coeficientes.")}</li>
        <li>{t("<strong>Product and quotient</strong> of the same bases: add or subtract exponents.", "<strong>Producto y cociente</strong> de las bases iguales: sumar o restar exponentes.")}</li>
        <li>{t("<strong>Negative exponents:</strong> rewrite them as fractions with positive exponents.", "<strong>Exponentes negativos:</strong> reescribirlos como fracción con exponente positivo.")}</li>
        <li>{t("<strong>Check</strong> that the answer is as simple as it can be.", "<strong>Revisar</strong> que el resultado quede en su forma más simple.")}</li>
      </ol>
      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("The five rules (table you can scroll sideways)", "Las cinco reglas (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("The five rules of exponents, to keep in view.", "Las cinco reglas de los exponentes, para tenerlas a la vista.")}</caption>
      <thead><tr><th scope="col">{t("Rule", "Regla")}</th><th scope="col">{t("Pattern", "Patrón")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead><tbody>{filas}</tbody></table></div>
      <h3>{t("The route, step by step", "La ruta, paso a paso")}</h3>
      <p>{t("Choose an expression and reveal one step at a time. Try to predict each step before you show it.", "Elija una expresión y vaya revelando un paso a la vez. Intente anticipar cada paso antes de mostrarlo.")}</p>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:260px;"><label for="o-expr">{t("Expression to simplify", "Expresión que se va a simplificar")}</label><select id="o-expr"></select></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="o-siguiente"></button>
          <button type="button" class="btn-sec" id="o-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button>
          <button type="button" class="btn-sec" id="o-reiniciar">{t("Start over", "Reiniciar")}</button>
        </div>
      </div>
      <div class="expr-grande" id="o-visual"></div>
      <div class="pasos" id="o-pasos" aria-live="polite"></div>
{B.om("p-orden", t("Practice: combine rules", "Practique: combinar reglas"))}'''),
     (t("fractions", "fracciones"), t("Fractions with negative exponents", "Fracciones con exponentes negativos"),
      f'''      <p>{t("When the expression is a fraction, the quotient rule works on <strong>each base separately</strong>, and the numbers are simplified like a fraction. If an exponent ends up negative, that factor moves to the bottom with a positive exponent in the last step.", "Cuando la expresión es una fracción, el cociente se aplica <strong>a cada base por separado</strong>, y los coeficientes se simplifican como una fracción numérica. Si algún exponente queda negativo, ese factor pasa al denominador con exponente positivo en el último paso.")}</p>
{P.atencion(t("The final form:", "Forma final exigida:"), t("an answer is not simplified while it has negative exponents. x<sup>3</sup>y<sup>−2</sup> has the same value as x<sup>3</sup>/y<sup>2</sup>, but only the second is the answer the test expects.", "un resultado no está simplificado mientras tenga exponentes negativos. x<sup>3</sup>y<sup>−2</sup> vale lo mismo que x<sup>3</sup>/y<sup>2</sup>, pero solo la segunda es la respuesta que espera el examen."))}
{B.om("p-fracciones", t("Practice: simplify the fraction", "Practique: simplifique la fracción"))}'''),
     (t("referee", "arbitro"), t("The exponent referee", "El árbitro de exponentes"),
      f'''      <p>{t("Read each student's work like a referee. If it is correct, say so. If it has a mistake, choose the right correction. Most mistakes repeat the same patterns: adding instead of multiplying, forgetting to raise the number, or thinking a negative exponent makes the number negative.", "Lea el trabajo de cada estudiante como un árbitro. Si está correcto, dígalo. Si tiene un error, elija la corrección adecuada. La mayoría de los errores repiten los mismos patrones: sumar en vez de multiplicar, olvidar elevar el coeficiente o creer que un exponente negativo hace negativo al número.")}</p>
{B.om("p-arbitro", t("Practice: what is the right call?", "Practique: ¿qué corresponde?"))}'''),
     (t("complete", "completa"), t("A complete expression, step by step", "Una expresión completa, paso a paso"),
      f'''      <p>{t("Here you solve each step of the route. Each box is checked separately: you have two tries per step and, if it does not work out, the answer is shown so you can keep going.", "Aquí resuelve usted cada paso de la ruta. Cada casilla se comprueba por separado: tiene dos intentos por paso y, si no sale, se muestra la respuesta para que pueda seguir.")}</p>
      <div class="practica">
        <div class="enun">{t("Simplify", "Simplifique")} <span id="c-expr"></span></div>
{paso(1, t("Step 1 · Parentheses.", "Paso 1 · Paréntesis."), t("Work out", "Resuelva") + ' <span id="c-par"></span>.', caja_num("c-coef", t("Coefficient", "Coeficiente")) + caja_num("c-e1", t("Exponent of x", "Exponente de x")), t("Check step 1", "Comprobar el paso 1"))}
{paso(2, t("Step 2 · Product.", "Paso 2 · Producto."), '<span id="c-t2"></span>', caja_num("c-e2", t("Exponent of x", "Exponente de x")), t("Check step 2", "Comprobar el paso 2"))}
{paso(3, t("Step 3 · Quotient.", "Paso 3 · Cociente."), '<span id="c-t3"></span>', caja_num("c-e3", t("Exponent of x (it can be negative)", "Exponente de x (puede ser negativo)")), t("Check step 3", "Comprobar el paso 3"))}
{paso(4, t("Step 4 · Final form.", "Paso 4 · Forma final."), '<span id="c-t4"></span>', f'<div class="campo"><label for="c-donde">{t("Where does the x go?", "¿Dónde queda la x?")}</label><select id="c-donde"><option value="">{t("Choose one", "Elija una opción")}</option><option value="arriba">{t("On the top (numerator)", "En el numerador")}</option><option value="abajo">{t("On the bottom (denominator)", "En el denominador")}</option></select></div>' + caja_num("c-e4", t("Positive exponent of x", "Exponente positivo de x")), t("Check step 4", "Comprobar el paso 4"))}
        <div class="salida" id="c-final" aria-live="polite"></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="c-nuevo">{t("Another expression", "Otra expresión")}</button>
          <button type="button" class="btn-sec" id="c-solucion">{t("See the full solution", "Ver la solución completa")}</button>
        </div>
        <p class="marcador" id="c-marc"></p>
      </div>'''),
     (t("check", "comprobacion"), t("Topic 1 check", "Comprobación del Tema 1"),
      f'''      <p>{t("When you feel sure about the three lessons, take the Topic 1 check: twelve questions on the five rules, with a report by lesson that you can print. If one lesson comes out weak, go back to its practice.", "Cuando se sienta seguro con las tres lecciones, haga la comprobación del tema: doce preguntas de las cinco reglas, con un informe por lección que puede imprimir. Si una lección sale floja, vuelva a su práctica.")}</p>
      <p><a class="btn" href="{href}">{t("Open the Topic 1 check", "Abrir la comprobación del Tema 1")} <span aria-hidden="true">›</span></a></p>''')]
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Four practice activities and the topic check on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica y la comprobación del tema en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_EXP, scripts=("/math/exponents.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Simplificar expresiones exponenciales con múltiples reglas")
