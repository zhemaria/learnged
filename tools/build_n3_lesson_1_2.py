"""Level 3 · Lesson 1.2 · The quotient rule, zero exponents, and negative exponents — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "1-2"
TEMA = ("Rules of exponents", "Reglas de los exponentes")
TIT = ("The quotient rule, zero exponents, and negative exponents", "Regla del cociente, exponente cero y exponentes negativos")

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def fr(a, b):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{a}</span><span class="fb2">{b}</span></span><span class="cap-oculto">{a}/{b}</span>'

def patron(base, desde, hasta, label):
    cab = "".join(f'<th scope="col">{base}<sup>{"−" if e < 0 else ""}{abs(e)}</sup></th>' for e in range(desde, hasta - 1, -1))
    val = "".join(f'<td>{base ** e if e >= 0 else "1/" + str(base ** -e)}</td>' for e in range(desde, hasta - 1, -1))
    return (f'<div class="tabla-scroll" role="region" tabindex="0" aria-label="{label} (table you can scroll sideways)"><table class="tabla-trad"><caption class="cap-oculto">{label}</caption>'
            f'<thead><tr>{cab}</tr></thead><tbody><tr>{val}</tr></tbody></table></div>')

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 1.1 you learned that when you multiply powers with the same base, the exponents are <strong>added</strong>. This lesson takes on the opposite operation, <strong>division</strong>, where the exponents are <strong>subtracted</strong>. Followed all the way, that rule also explains two surprising ideas: the <strong>zero</strong> exponent and <strong>negative</strong> exponents.",
"En la Lección 1.1 aprendió que al multiplicar potencias de la misma base los exponentes se <strong>suman</strong>. Esta lección trata la operación opuesta, la <strong>división</strong>, donde los exponentes se <strong>restan</strong>. Llevada hasta el final, esa regla explica también dos ideas sorprendentes: el exponente <strong>cero</strong> y los exponentes <strong>negativos</strong>.")}</p>
<p>{t("When you divide two powers with the same base, each factor on the bottom cancels a factor on the top. Write it out to see it:", "Al dividir dos potencias de la misma base, cada factor de abajo cancela un factor de arriba. Al desarrollarlo se ve:")}</p>
{big(fr("a<sup>5</sup>", "a<sup>2</sup>") + " = " + fr("a · a · a · <s>a</s> · <s>a</s>", "<s>a</s> · <s>a</s>") + " = a<sup>3</sup>")}
<p>{t("Five factors on top minus two on the bottom leave three factors. The exponent of the answer is the <strong>difference</strong> of the exponents, always top minus bottom:", "Cinco factores arriba menos dos abajo dejan tres factores. El exponente del resultado es la <strong>resta</strong> de los exponentes, siempre el de arriba menos el de abajo:")}</p>
{big(t("a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m − n</sup>  (a ≠ 0)", "a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m − n</sup>  (a ≠ 0)"))}
{ejemplo(t("Example 1: simplify x<sup>9</sup> ÷ x<sup>4</sup>", "Ejemplo 1: simplifique x<sup>9</sup> ÷ x<sup>4</sup>"),
  [("1", t("Same base.", "Misma base."), t("Both have base x: the quotient rule applies.", "Las dos tienen base x: se aplica la regla del cociente.")),
   ("2", t("Subtract.", "Se restan."), "9 − 4 = 5."),
   ("✓", t("Answer.", "Respuesta."), "x<sup>9</sup> ÷ x<sup>4</sup> = <strong>x<sup>5</sup></strong>")])}
{ejemplo(t("Example 2: simplify 10<sup>6</sup> ÷ 10<sup>4</sup>", "Ejemplo 2: simplifique 10<sup>6</sup> ÷ 10<sup>4</sup>"),
  [("1", t("Same base.", "Misma base."), t("The base is 10: 6 − 4 = 2.", "La base es 10: 6 − 4 = 2.")),
   ("✓", t("Answer.", "Respuesta."), "10<sup>6</sup> ÷ 10<sup>4</sup> = <strong>10<sup>2</sup> = 100</strong>")])}
{caja("ojo", t("Watch the order", "Cuidado con el orden"), t("<p>Always subtract the top exponent minus the bottom exponent, never the other way around. The base cannot be zero, because dividing by zero is not defined.</p>", "<p>Se resta siempre el exponente de arriba menos el de abajo, nunca al revés. La base no puede ser cero, porque dividir entre cero no está definido.</p>"))}
{practica("p1", t("Practice 1 — Subtract the exponents", "Práctica 1 — Reste los exponentes"), t("What is x<sup>9</sup> ÷ x<sup>5</sup>?", "¿Cuánto es x<sup>9</sup> ÷ x<sup>5</sup>?"),
          [("a", "x<sup>14</sup>"), ("b", "x<sup>4</sup>"), ("c", "x<sup>45</sup>"), ("d", "x<sup>−4</sup>")])}
{practica("p2", t("Practice 2 — With numbers in front", "Práctica 2 — Con coeficientes"), t("What is 12m<sup>10</sup> ÷ 3m<sup>4</sup>?", "¿Cuánto es 12m<sup>10</sup> ÷ 3m<sup>4</sup>?"),
          [("a", "9m<sup>6</sup>"), ("b", "4m<sup>14</sup>"), ("c", "4m<sup>6</sup>"), ("d", "36m<sup>6</sup>")])}
{enlace(n, t("quotient", "cociente"), t("the quotient rule", "la regla del cociente"), t("Cancel factors one by one and divide powers with the same base, also with coefficients.", "Cancele factores uno a uno y divida potencias de la misma base, también con coeficientes."))}'''

    s2 = f'''<p>{t("What happens when you divide a power by itself? On one hand, any number other than zero divided by itself is <strong>1</strong>. On the other hand, the quotient rule gives a zero exponent:", "¿Qué ocurre al dividir una potencia entre sí misma? Por un lado, cualquier número distinto de cero dividido entre sí mismo da <strong>1</strong>. Por otro lado, la regla del cociente da un exponente cero:")}</p>
{big(t("a<sup>3</sup> ÷ a<sup>3</sup> = 1   and also   a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>3 − 3</sup> = a<sup>0</sup>", "a<sup>3</sup> ÷ a<sup>3</sup> = 1   y también   a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>3 − 3</sup> = a<sup>0</sup>"))}
<p>{t("Both describe the same division, so they must be equal:", "Las dos describen la misma división, así que tienen que ser iguales:")}</p>
{big("a<sup>0</sup> = 1  (a ≠ 0)")}
<p>{t("A pattern of shrinking powers gives the same answer: each time the exponent goes down by one, the value is divided by the base.", "Un patrón de potencias decrecientes da la misma respuesta: cada vez que el exponente baja una unidad, el valor se divide entre la base.")}</p>
{patron(2, 3, 0, t("Powers of 2 going down: 8, 4, 2, 1", "Potencias de 2 que bajan: 8, 4, 2, 1"))}
<p>{t("8 ÷ 2 = 4, 4 ÷ 2 = 2, and 2 ÷ 2 = 1. Dividing by the base once more leads naturally to 2<sup>0</sup> = 1. This works for any base other than zero: 5<sup>0</sup> = 1, 100<sup>0</sup> = 1, (3x)<sup>0</sup> = 1.", "8 ÷ 2 = 4, 4 ÷ 2 = 2, y 2 ÷ 2 = 1. Seguir dividiendo entre la base lleva de forma natural a 2<sup>0</sup> = 1. Vale para cualquier base distinta de cero: 5<sup>0</sup> = 1, 100<sup>0</sup> = 1, (3x)<sup>0</sup> = 1.")}</p>
{caja("ojo", t("The zero affects only its own base", "El cero solo afecta a su base"), t("<p>(3x)<sup>0</sup> = 1, because the zero reaches everything in the parentheses. But 3x<sup>0</sup> = 3 · 1 = 3, because the zero reaches only the x. In the same way, −5<sup>0</sup> = −1, while (−5)<sup>0</sup> = 1.</p>",
"<p>(3x)<sup>0</sup> = 1, porque el cero alcanza todo el paréntesis. Pero 3x<sup>0</sup> = 3 · 1 = 3, porque el cero solo alcanza a la x. Del mismo modo, −5<sup>0</sup> = −1, mientras que (−5)<sup>0</sup> = 1.</p>"))}
{practica("p3", t("Practice 3 — The zero exponent", "Práctica 3 — El exponente cero"), t("What is 9<sup>0</sup>?", "¿Cuánto vale 9<sup>0</sup>?"),
          [("a", "0"), ("b", "9"), ("c", "1"), ("d", "90")])}
{practica("p4", t("Practice 4 — Where is the zero?", "Práctica 4 — ¿Dónde está el cero?"), t("What is 4y<sup>0</sup>?", "¿Cuánto vale 4y<sup>0</sup>?"),
          [("a", "1"), ("b", "4"), ("c", "0"), ("d", "4y")])}
{enlace(n, t("zero", "cero"), t("the zero exponent", "el exponente cero"), t("Follow the pattern down to zero and tell (−5)<sup>0</sup> from −5<sup>0</sup>.", "Siga el patrón hasta el cero y distinga (−5)<sup>0</sup> de −5<sup>0</sup>."))}'''

    s3 = f'''<p>{t("If the pattern keeps going past zero, each step still divides by the base, and fractions appear:", "Si el patrón sigue más allá del cero, cada paso sigue dividiendo entre la base, y aparecen las fracciones:")}</p>
{patron(2, 1, -3, t("Powers of 2 going below zero: 2, 1, 1/2, 1/4, 1/8", "Potencias de 2 por debajo de cero: 2, 1, 1/2, 1/4, 1/8"))}
<p>{t("A negative exponent means the <strong>reciprocal</strong> of the power with a positive exponent:", "Un exponente negativo indica el <strong>recíproco</strong> de la potencia con exponente positivo:")}</p>
{big("a<sup>−n</sup> = " + fr("1", "a<sup>n</sup>") + "  (a ≠ 0)")}
{ejemplo(t("Example 3: write 2<sup>−3</sup> as a fraction", "Ejemplo 3: escriba 2<sup>−3</sup> como fracción"),
  [("1", t("Reciprocal.", "Recíproco."), "2<sup>−3</sup> = 1 ÷ 2<sup>3</sup>."),
   ("2", t("Power.", "Potencia."), "2<sup>3</sup> = 8."),
   ("✓", t("Answer.", "Respuesta."), "2<sup>−3</sup> = <strong>1/8 = 0.125</strong>")])}
{ejemplo(t("Example 4: rewrite x<sup>−4</sup> with a positive exponent", "Ejemplo 4: reescriba x<sup>−4</sup> con exponente positivo"),
  [("1", t("Definition.", "Definición."), t("A negative exponent means the reciprocal.", "El exponente negativo indica el recíproco.")),
   ("✓", t("Answer.", "Respuesta."), "x<sup>−4</sup> = <strong>1/x<sup>4</sup></strong>")])}
{caja("tip", t("Crossing the fraction bar", "Cruzar la barra de fracción"), t("<p>Moving a factor from the top of a fraction to the bottom, or from the bottom to the top, changes the sign of its exponent. So 1 ÷ a<sup>−2</sup> = a<sup>2</sup>: when the factor moves up, the exponent goes from negative to positive.</p>",
"<p>Mover un factor de arriba abajo en una fracción, o de abajo arriba, cambia el signo de su exponente. Así, 1 ÷ a<sup>−2</sup> = a<sup>2</sup>: al subir el factor, el exponente pasa de negativo a positivo.</p>"))}
{caja("ojo", t("A negative exponent does not make the number negative", "Un exponente negativo no hace negativo al número"), t("<p>2<sup>−3</sup> is not −8 and not −6: it is the positive fraction 1/8. The sign of the exponent only means “reciprocal,” never the sign of the answer.</p>",
"<p>2<sup>−3</sup> no es −8 ni −6: es la fracción positiva 1/8. El signo del exponente solo indica «recíproco», nunca el signo del resultado.</p>"))}
{practica("p5", t("Practice 5 — A negative exponent", "Práctica 5 — Un exponente negativo"), t("What is x<sup>−3</sup> equal to?", "¿A qué equivale x<sup>−3</sup>?"),
          [("a", "−x<sup>3</sup>"), ("b", "1/x<sup>3</sup>"), ("c", "3/x"), ("d", "−3x")])}
{practica("p6", t("Practice 6 — Across the bar", "Práctica 6 — Al cruzar la barra"), t("What is 1 ÷ a<sup>−2</sup> equal to?", "¿A qué equivale 1 ÷ a<sup>−2</sup>?"),
          [("a", "a<sup>2</sup>"), ("b", "1/a<sup>2</sup>"), ("c", "−a<sup>2</sup>"), ("d", "−2a")])}
{enlace(n, t("negatives", "negativos"), t("negative exponents", "los exponentes negativos"), t("Continue the pattern below zero and rewrite negative exponents as fractions.", "Continúe el patrón por debajo de cero y reescriba exponentes negativos como fracciones."))}'''

    s4 = f'''<p>{t("With Lesson 1.1 and this one, the set of exponent rules is complete. Keep this table in view.", "Con la lección anterior y esta, el conjunto de reglas de los exponentes queda completo. Tenga esta tabla a la vista.")}</p>
{tabla(t("The five rules of exponents", "Las cinco reglas de los exponentes"), t("The five rules of exponents: name, pattern, and example", "Las cinco reglas de los exponentes: nombre, patrón y ejemplo"),
       [t("Rule", "Regla"), t("Pattern", "Patrón"), t("Example", "Ejemplo")], [[a, b, d] for a, b, c, d in n3.tabla_reglas(True)])}
{practica("p7", t("Practice 7 — Which rule?", "Práctica 7 — ¿Qué regla?"), t("Which rule explains why a<sup>0</sup> = 1?", "¿Qué regla justifica que a<sup>0</sup> = 1?"),
          [("a", t("The product rule", "La regla del producto")), ("b", t("The quotient rule", "La regla del cociente")), ("c", t("The power of a product", "La potencia de un producto")), ("d", t("The power of a power", "La potencia de una potencia"))])}
{enlace(n, t("five-rules", "cinco-reglas"), t("the five rules of exponents", "las cinco reglas de los exponentes"), t("Say which rule explains each step, and see which rule you need to review.", "Reconozca qué regla justifica cada paso y vea cuál necesita repasar."))}'''

    s5 = f'''<p>{t("Negative exponents show up when you measure very small amounts, an idea you will use again in scientific notation in Topic 2. The calculator lets you check any answer.", "Los exponentes negativos aparecen al medir cantidades muy pequeñas, una idea que volverá en la notación científica del Tema 2. La calculadora permite comprobar cualquier resultado.")}</p>
{ejemplo(t("Example 5: check that 5<sup>−2</sup> = 1/25", "Ejemplo 5: compruebe que 5<sup>−2</sup> = 1/25"),
  [("1", t("By hand.", "A mano."), "5<sup>−2</sup> = 1 ÷ 5<sup>2</sup> = 1 ÷ 25 = 0.04."),
   ("2", t("On the calculator.", "En la calculadora."), t(f"{T('5')} {T('^')} {T('(−)')} {T('2')} {T('enter')} shows 0.04.", f"{T('5')} {T('^')} {T('(−)')} {T('2')} {T('enter')} muestra 0.04.")),
   ("✓", t("Answer.", "Respuesta."), "5<sup>−2</sup> = <strong>1/25 = 0.04</strong>")])}
{calc(t("The negative sign of an exponent", "El signo negativo del exponente"), t(f"<p>Type the minus sign of the exponent with the {T('(−)')} key, not with the subtraction key {T('−')}. Before you start, clear the screen with {T('clear')} so old values are not carried along.</p>",
f"<p>El signo menos del exponente se escribe con la tecla {T('(−)')}, no con la tecla de resta {T('−')}. Antes de empezar, borre la pantalla con {T('clear')} para no arrastrar valores anteriores.</p>"))}
{caja("tip", t("Check with a number", "Compruebe con un número"), t("<p>A correct simplification gives the <strong>same number</strong> as the original expression for any value of the letter. Replace x with 2 or 3 in both: if the values are different, there is a mistake. Do not use 0 (there may be a division by zero) or 1 (every power of 1 is 1, so the test tells you nothing).</p>",
"<p>Una simplificación correcta da el <strong>mismo número</strong> que la expresión original para cualquier valor de la letra. Sustituya la x por 2 o 3 en las dos: si los valores son distintos, hay un error. No use el 0 (puede haber una división entre cero) ni el 1 (toda potencia de 1 vale 1, así que la prueba no distingue nada).</p>"))}
{practica("p8", t("Practice 8 — Check with x = 2", "Práctica 8 — Compruebe con x = 2"), t("Someone wrote x<sup>5</sup> ÷ x<sup>2</sup> = x<sup>7</sup>. With x = 2, the left side is 32 ÷ 4 = 8. What is the right side, and is the work correct?", "Alguien escribió x<sup>5</sup> ÷ x<sup>2</sup> = x<sup>7</sup>. Con x = 2, el lado izquierdo vale 32 ÷ 4 = 8. ¿Cuánto vale el lado derecho y está bien el trabajo?"),
          [("a", t("128; it is wrong", "128; está mal")), ("b", t("8; it is right", "8; está bien")), ("c", t("14; it is wrong", "14; está mal"))])}
{enlace(n, t("check", "verificar"), t("checking with numbers", "verificar con valores numéricos"), t("Test someone else's work with a number and decide whether it is right.", "Pruebe con un número el trabajo de otra persona y decida si está bien."))}'''

    secciones = [("s-" + t("quotient", "cociente"), t("The quotient rule", "La regla del cociente"), s1),
                 ("s-" + t("zero", "cero"), t("The zero exponent", "El exponente cero"), s2),
                 ("s-" + t("negatives", "negativos"), t("Negative exponents", "Los exponentes negativos"), s3),
                 ("s-" + t("five-rules", "cinco-reglas"), t("The five rules of exponents", "Las cinco reglas de los exponentes"), s4),
                 ("s-" + t("check", "verificar"), t("Checking with the calculator and with numbers", "Verificar con la calculadora y con números"), s5)]

    lesson = {"next": t("Lesson 1.3", "Lección 1.3"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You added. When you divide, subtract the exponents.", "Sumó. Al dividir, los exponentes se restan."), "c": t("You wrote 4 and 5 side by side. Subtract 9 − 5.", "Escribió el 4 y el 5 juntos. Reste 9 − 5."), "d": t("You subtracted in the wrong order: top minus bottom, 9 − 5.", "Restó al revés: arriba menos abajo, 9 − 5.")},
             "right": "9 − 5 = 4.", "solution": t("Same base: 9 − 5 = 4, so x<sup>4</sup>.", "Misma base: 9 − 5 = 4, así que x<sup>4</sup>.")},
      "p2": {"ok": "c", "hints": {"a": t("You subtracted the numbers. Divide them: 12 ÷ 3.", "Restó los coeficientes. Se dividen: 12 ÷ 3."), "b": t("You added the exponents. When you divide, subtract them.", "Sumó los exponentes. Al dividir, se restan."), "d": t("You multiplied the numbers. Divide them: 12 ÷ 3.", "Multiplicó los coeficientes. Se dividen: 12 ÷ 3.")},
             "right": t("12 ÷ 3 = 4 and 10 − 4 = 6.", "12 ÷ 3 = 4 y 10 − 4 = 6."), "solution": t("Numbers: 12 ÷ 3 = 4. Exponents: 10 − 4 = 6. So 4m<sup>6</sup>.", "Coeficientes: 12 ÷ 3 = 4. Exponentes: 10 − 4 = 6. Así que 4m<sup>6</sup>.")},
      "p3": {"ok": "c", "hints": {"a": t("The zero exponent does not wipe the number out: 9<sup>0</sup> is 9 ÷ 9.", "El exponente cero no anula el número: 9<sup>0</sup> es 9 ÷ 9."), "b": t("With exponent zero the value is always 1, whatever the base (not zero).", "Con exponente cero el valor siempre es 1, sea cual sea la base (distinta de cero)."), "d": t("The exponent is not a digit you write next to the base.", "El exponente no es una cifra que se escribe al lado de la base.")},
             "right": t("Any base other than zero to the power 0 is 1.", "Cualquier base distinta de cero con exponente 0 vale 1."), "solution": t("9<sup>0</sup> = 9 ÷ 9 = 1.", "9<sup>0</sup> = 9 ÷ 9 = 1.")},
      "p4": {"ok": "b", "hints": {"a": t("With no parentheses, the zero reaches only the y. The 4 stays.", "Sin paréntesis, el cero solo alcanza a la y. El 4 se queda."), "c": t("y<sup>0</sup> is 1, not 0.", "y<sup>0</sup> vale 1, no 0."), "d": t("y<sup>0</sup> is not y: it is 1.", "y<sup>0</sup> no es y: es 1.")},
             "right": "4 · y<sup>0</sup> = 4 · 1 = 4.", "solution": t("The zero affects only the y: 4y<sup>0</sup> = 4 · 1 = 4.", "El cero solo afecta a la y: 4y<sup>0</sup> = 4 · 1 = 4.")},
      "p5": {"ok": "b", "hints": {"a": t("A negative exponent does not make the answer negative: it means reciprocal.", "El exponente negativo no hace negativo al resultado: indica el recíproco."), "c": t("The exponent does not come down as a number: x keeps its exponent 3 on the bottom.", "El exponente no baja como número: la x se queda con su exponente 3 en el denominador."), "d": t("Do not multiply by the exponent. Write the reciprocal.", "No se multiplica por el exponente. Se escribe el recíproco.")},
             "right": "x<sup>−3</sup> = 1/x<sup>3</sup>.", "solution": t("A negative exponent means the reciprocal: x<sup>−3</sup> = 1/x<sup>3</sup>.", "El exponente negativo indica el recíproco: x<sup>−3</sup> = 1/x<sup>3</sup>.")},
      "p6": {"ok": "a", "hints": {"b": t("When the factor moves up across the bar, its exponent changes sign and the 1 is no longer needed.", "Al subir el factor por la barra, su exponente cambia de signo y el 1 ya no hace falta."), "c": t("The answer is not negative.", "El resultado no es negativo."), "d": t("Do not multiply by the exponent.", "No se multiplica por el exponente.")},
             "right": "1 ÷ a<sup>−2</sup> = a<sup>2</sup>.", "solution": t("Moving a<sup>−2</sup> to the top changes the sign of its exponent: a<sup>2</sup>.", "Al subir a<sup>−2</sup> al numerador, su exponente cambia de signo: a<sup>2</sup>.")},
      "p7": {"ok": "b", "hints": {"a": t("The product rule is for multiplying. a<sup>0</sup> = 1 comes from dividing a power by itself.", "La regla del producto es para multiplicar. a<sup>0</sup> = 1 sale de dividir una potencia entre sí misma."), "c": t("The power of a product shares out an exponent; it does not explain the zero.", "La potencia de un producto reparte un exponente; no explica el cero."), "d": t("The power of a power multiplies exponents; it does not explain the zero.", "La potencia de una potencia multiplica exponentes; no explica el cero.")},
             "right": t("a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>0</sup> and it is also 1.", "a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>0</sup> y también vale 1."), "solution": t("Dividing a power by itself gives 1, and the quotient rule gives a<sup>0</sup>. So a<sup>0</sup> = 1.", "Dividir una potencia entre sí misma da 1, y la regla del cociente da a<sup>0</sup>. Por eso a<sup>0</sup> = 1.")},
      "p8": {"ok": "a", "hints": {"b": t("Replace x with 2 in x<sup>7</sup>: 2<sup>7</sup> = 128, not 8.", "Sustituya la x por 2 en x<sup>7</sup>: 2<sup>7</sup> = 128, no 8."), "c": t("2<sup>7</sup> is not 2 × 7: it is 2 multiplied by itself seven times.", "2<sup>7</sup> no es 2 × 7: es 2 multiplicado por sí mismo siete veces.")},
             "right": t("2<sup>7</sup> = 128, and 128 ≠ 8. The right answer is x<sup>3</sup>.", "2<sup>7</sup> = 128, y 128 ≠ 8. Lo correcto es x<sup>3</sup>."), "solution": t("With x = 2, x<sup>7</sup> = 128, but the left side is 8. The values are different, so there is a mistake: the exponents were added. The right answer is x<sup>3</sup> (and 2<sup>3</sup> = 8).", "Con x = 2, x<sup>7</sup> = 128, pero el lado izquierdo vale 8. Los valores son distintos, así que hay un error: se sumaron los exponentes. Lo correcto es x<sup>3</sup> (y 2<sup>3</sup> = 8).")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("You added. When you divide, subtract.", "Sumó. Al dividir, se resta."), "c": t("Check the subtraction: 7 − 3.", "Revise la resta: 7 − 3."), "d": t("You multiplied the exponents. Subtract them.", "Multiplicó los exponentes. Se restan.")}, "solution": t("7 − 3 = 4, so a<sup>4</sup>.", "7 − 3 = 4, así que a<sup>4</sup>.")},
      "B": {"ok": "c", "hints": {"a": t("The x on the bottom is x<sup>1</sup>: subtract 1.", "La x de abajo es x<sup>1</sup>: reste 1."), "b": t("You added. When you divide, subtract.", "Sumó. Al dividir, se resta."), "d": t("x = x<sup>1</sup>, so subtract 1, not 2.", "x = x<sup>1</sup>: se resta 1, no 2.")}, "solution": t("x = x<sup>1</sup>: 8 − 1 = 7, so x<sup>7</sup>.", "x = x<sup>1</sup>: 8 − 1 = 7, así que x<sup>7</sup>.")},
      "C": {"ok": "b", "hints": {"a": t("The zero exponent gives 1, not 0.", "El exponente cero da 1, no 0."), "c": t("The zero reaches everything inside the parentheses.", "El cero alcanza todo lo que está dentro del paréntesis."), "d": t("The 3 is inside the parentheses, so it is affected by the zero too.", "El 3 está dentro del paréntesis: el cero también lo afecta.")}, "solution": t("The zero applies to the whole parentheses: (3x)<sup>0</sup> = 1.", "El cero afecta a todo el paréntesis: (3x)<sup>0</sup> = 1.")},
      "D": {"ok": "c", "hints": {"a": t("A negative exponent does not make the number negative.", "Un exponente negativo no hace negativo al número."), "b": t("Take the reciprocal: 1 over 2<sup>3</sup>.", "Tome el recíproco: 1 entre 2<sup>3</sup>."), "d": t("Do not multiply 2 by 3, and the answer is not negative.", "No se multiplica 2 por 3, y el resultado no es negativo.")}, "solution": t("2<sup>−3</sup> = 1/2<sup>3</sup> = 1/8.", "2<sup>−3</sup> = 1/2<sup>3</sup> = 1/8.")},
      "E": {"ok": "d", "hints": {"a": t("The exponent's sign does not go to the number.", "El signo del exponente no pasa al número."), "b": t("The exponent does not come down as a number.", "El exponente no baja como número."), "c": t("You dropped the minus sign without taking the reciprocal.", "Quitó el signo menos sin tomar el recíproco.")}, "solution": t("x<sup>−4</sup> = 1/x<sup>4</sup>.", "x<sup>−4</sup> = 1/x<sup>4</sup>.")},
      "F": {"ok": "b", "hints": {"a": t("When the factor moves up, its exponent changes sign: the 1 on top is no longer needed.", "Al subir el factor, su exponente cambia de signo: el 1 de arriba ya no hace falta."), "c": t("The answer is not negative.", "El resultado no es negativo."), "d": t("The exponent does not come down as a number.", "El exponente no baja como número.")}, "solution": t("1 ÷ y<sup>−2</sup> = y<sup>2</sup>.", "1 ÷ y<sup>−2</sup> = y<sup>2</sup>.")},
      "G": {"ok": "d", "hints": {"a": t("No factor of m is left: they all cancel.", "No queda ningún factor de m: se cancelan todos."), "b": t("A number other than zero divided by itself is 1, not 0.", "Un número distinto de cero dividido entre sí mismo da 1, no 0."), "c": t("You added. When you divide, subtract: 5 − 5.", "Sumó. Al dividir, se resta: 5 − 5.")}, "solution": t("m<sup>5 − 5</sup> = m<sup>0</sup> = 1.", "m<sup>5 − 5</sup> = m<sup>0</sup> = 1.")},
      "H": {"ok": "a", "hints": {"b": t("3<sup>2</sup> is 3 · 3 = 9, not 3 · 2.", "3<sup>2</sup> es 3 · 3 = 9, no 3 · 2."), "c": t("A negative exponent does not make the number negative.", "Un exponente negativo no hace negativo al número."), "d": t("Take the reciprocal of 9.", "Tome el recíproco de 9.")}, "solution": t("3<sup>−2</sup> = 1/3<sup>2</sup> = 1/9.", "3<sup>−2</sup> = 1/3<sup>2</sup> = 1/9.")}
     }}

    quiz = [
     ("A", t("Simplify a<sup>7</sup> ÷ a<sup>3</sup>.", "Simplifique a<sup>7</sup> ÷ a<sup>3</sup>."), [("a", "a<sup>4</sup>"), ("b", "a<sup>10</sup>"), ("c", "a<sup>2</sup>"), ("d", "a<sup>21</sup>")]),
     ("B", t("Simplify x<sup>8</sup> ÷ x.", "Simplifique x<sup>8</sup> ÷ x."), [("a", "x<sup>8</sup>"), ("b", "x<sup>9</sup>"), ("c", "x<sup>7</sup>"), ("d", "x<sup>6</sup>")]),
     ("C", t("What is (3x)<sup>0</sup>?", "¿Cuánto vale (3x)<sup>0</sup>?"), [("a", "0"), ("b", "1"), ("c", "3x"), ("d", "3")]),
     ("D", t("Write 2<sup>−3</sup> as a fraction.", "Escriba 2<sup>−3</sup> como fracción."), [("a", "−8"), ("b", "8"), ("c", "1/8"), ("d", "−6")]),
     ("E", t("Rewrite x<sup>−4</sup> with a positive exponent.", "Reescriba x<sup>−4</sup> con exponente positivo."), [("a", "−x<sup>4</sup>"), ("b", "4/x"), ("c", "x<sup>4</sup>"), ("d", "1/x<sup>4</sup>")]),
     ("F", t("What is 1 ÷ y<sup>−2</sup> equal to?", "¿A qué equivale 1 ÷ y<sup>−2</sup>?"), [("a", "1/y<sup>2</sup>"), ("b", "y<sup>2</sup>"), ("c", "−y<sup>2</sup>"), ("d", "2/y")]),
     ("G", t("Simplify m<sup>5</sup> ÷ m<sup>5</sup>.", "Simplifique m<sup>5</sup> ÷ m<sup>5</sup>."), [("a", "m"), ("b", "0"), ("c", "m<sup>10</sup>"), ("d", "1")]),
     ("H", t("Write 3<sup>−2</sup> as a fraction.", "Reescriba 3<sup>−2</sup> como fracción."), [("a", "1/9"), ("b", "1/6"), ("c", "−9"), ("d", "9")])]

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("Dividing powers: the exponents are subtracted. And from that rule come a<sup>0</sup> = 1 and negative exponents.", "Dividir potencias: los exponentes se restan. Y de esa regla salen a<sup>0</sup> = 1 y los exponentes negativos."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Use</strong> the quotient rule: a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m−n</sup> (a ≠ 0).", "<strong>Aplicar</strong> la regla del cociente: a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m−n</sup> (con a ≠ 0)."),
         t("<strong>Explain</strong> why a<sup>0</sup> = 1 (a ≠ 0) with the quotient rule.", "<strong>Justificar</strong> por qué a<sup>0</sup> = 1 (con a ≠ 0) usando la regla del cociente."),
         t("<strong>Define</strong> a negative exponent as a reciprocal: a<sup>−n</sup> = 1 ÷ a<sup>n</sup>.", "<strong>Definir</strong> el exponente negativo como recíproco: a<sup>−n</sup> = 1 ÷ a<sup>n</sup>."),
         t("<strong>Rewrite</strong> negative exponents as fractions with positive exponents, and back.", "<strong>Reescribir</strong> expresiones con exponentes negativos como fracciones de exponentes positivos, y viceversa."),
         t("<strong>Check</strong> answers with the calculator and with a test number.", "<strong>Verificar</strong> los resultados con la calculadora y con un número de prueba.")],
        secciones,
        (t("Write and simplify six quotients of powers with the same base (two of them with a negative exponent in the answer); four expressions with a zero exponent, including one like (−5)<sup>0</sup> and one like −5<sup>0</sup>, with a sentence explaining why they are not equal; and six expressions with negative exponents rewritten as fractions. Then check four of your answers on the calculator.",
           "Escriba y simplifique seis cocientes de potencias de la misma base (dos de ellos con exponente negativo en el resultado); cuatro expresiones con exponente cero, una del tipo (−5)<sup>0</sup> y otra del tipo −5<sup>0</sup>, con una frase que explique por qué no valen lo mismo; y seis expresiones con exponentes negativos reescritas como fracción. Después compruebe cuatro de sus resultados en la calculadora."),
         t("Halving shows negative powers of 2: cut a sheet of paper in half, then in half again, three times. Each piece is 2<sup>−1</sup>, then 2<sup>−2</sup>, then 2<sup>−3</sup> = 1/8 of the sheet. Count the pieces to check.",
           "Partir a la mitad muestra potencias negativas de 2: corte una hoja de papel a la mitad, y otra vez a la mitad, tres veces. Cada trozo es 2<sup>−1</sup>, después 2<sup>−2</sup> y después 2<sup>−3</sup> = 1/8 de la hoja. Cuente los trozos para comprobarlo.")),
        quiz,
        t("Self-check checklist for the quotient rule, zero exponents, and negative exponents", "Lista de autoevaluación de la regla del cociente, el exponente cero y los exponentes negativos"),
        t("Self-check checklist: skills for the quotient rule, zero exponents, and negative exponents", "Lista de autoevaluación: destrezas de la regla del cociente, el exponente cero y los exponentes negativos"),
        [(t("The quotient rule", "La regla del cociente"), t("I subtract top minus bottom and can explain it by cancelling factors.", "Resto el de arriba menos el de abajo y sé explicarlo cancelando factores."), t("I subtract, but sometimes in the wrong order.", "Resto, pero a veces en el orden equivocado."), t("I add the exponents or subtract backward.", "Sumo los exponentes o resto al revés.")),
         (t("The zero exponent", "El exponente cero"), t("I know a<sup>0</sup> = 1, explain why, and tell (3x)<sup>0</sup> from 3x<sup>0</sup>.", "Sé que a<sup>0</sup> = 1, explico por qué y distingo (3x)<sup>0</sup> de 3x<sup>0</sup>."), t("I remember a<sup>0</sup> = 1 but cannot explain it.", "Recuerdo que a<sup>0</sup> = 1, pero no sé justificarlo."), t("I think a<sup>0</sup> is 0.", "Creo que a<sup>0</sup> es 0.")),
         (t("Negative exponents", "Exponentes negativos"), t("I rewrite a<sup>−n</sup> = 1/a<sup>n</sup> both ways and check on the calculator.", "Reescribo a<sup>−n</sup> = 1/a<sup>n</sup> en los dos sentidos y lo compruebo en la calculadora."), t("I write the reciprocal, with some mistakes.", "Escribo el recíproco, con algunos errores."), t("I make the number negative.", "Hago negativo al número."))],
        t("<p>You completed the rules of exponents: when you divide, the exponents are <strong>subtracted</strong>; any base other than zero to the power zero is <strong>1</strong>; and a <strong>negative</strong> exponent means the reciprocal, never a negative number.</p>\n<p>In <strong>Lesson 1.3 · Simplifying with several rules</strong> you will put everything together: expressions that need two or more rules in a row, answers with <strong>positive exponents</strong> only, and finding the most common mistakes.</p>",
          "<p>Completó las reglas de los exponentes: al dividir, los exponentes se <strong>restan</strong>; cualquier base distinta de cero elevada a cero da <strong>1</strong>; y un exponente <strong>negativo</strong> indica el recíproco, nunca un número negativo.</p>\n<p>En la <strong>Lección 1.3 · Simplificar expresiones exponenciales con múltiples reglas</strong> reunirá todo: expresiones que exigen dos o más reglas seguidas, resultados solo con <strong>exponentes positivos</strong> y la detección de los errores más comunes.</p>"),
        ("1-3", ("", t("Lesson 1.3 · Simplifying with several rules", "Lección 1.3 · Simplificar expresiones exponenciales con múltiples reglas"))),
        [(t("quotient", "cociente"), t("The answer to a division.", "El resultado de una división.")),
         (t("reciprocal", "recíproco"), t("The number you multiply by to get 1. The reciprocal of 8 is 1/8.", "El número por el que se multiplica para obtener 1. El recíproco de 8 es 1/8.")),
         (t("zero exponent", "exponente cero"), t("a<sup>0</sup> = 1 for any base other than zero.", "a<sup>0</sup> = 1 para cualquier base distinta de cero.")),
         (t("negative exponent", "exponente negativo"), t("It means the reciprocal: a<sup>−n</sup> = 1/a<sup>n</sup>. It does not make the number negative.", "Indica el recíproco: a<sup>−n</sup> = 1/a<sup>n</sup>. No hace negativo al número."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var VARS = ["x", "y", "a", "m", "n", "b"];
function fac(n){ return n === 1 ? T(" factor", " factor") : T(" factors", " factores"); }
function sim(){ return T("Simplify ", "Simplifique "); }

/* ============ MODULE 1 · factor canceller ============ */
function actualizaCociente(){
  var m = leeEntero("co-m", 1, 7, "co-aviso", T("top exponent", "exponente de arriba"));
  var n = m === null ? null : leeEntero("co-n", 1, 7, "co-aviso", T("bottom exponent", "exponente de abajo"));
  if (m === null || n === null){ $("co-fichas").innerHTML = ""; $("co-salida").innerHTML = ""; return; }
  limpiaAviso("co-aviso");
  var k = Math.min(m, n);
  $("co-fichas").innerHTML = '<div class="fichas">' + fichas("a", m, "", k) + '</div><div class="barra"></div><div class="fichas">' + fichas("a", n, "b", k) + "</div>";
  var cu = ver(fracX(xp("a", m), xp("a", n)));
  var h = '<div class="linea">' + T(k + (k === 1 ? " pair" : " pairs") + " of factors cancel (the crossed-out chips).", "Se cancelan " + k + (k === 1 ? " pareja" : " parejas") + " de factores (las fichas tachadas).") + "</div>";
  if (m > n){
    h += '<div class="linea">' + cu + " = " + ver(xp("a", m - n)) + "</div>";
    h += '<div class="linea veredicto">' + T((m - n) + fac(m - n) + " left on top: ", "Quedan " + (m - n) + fac(m - n) + " arriba: ") + m + " − " + n + " = " + (m - n) + ".</div>";
  } else if (m === n){
    h += '<div class="linea">' + cu + T(" = 1, because no factor is left.", " = 1, porque no queda ningún factor.") + "</div>";
    h += '<div class="linea veredicto">' + T("The rule gives ", "La regla da ") + m + " − " + n + T(" = 0, that is, a<sup>0</sup>. Both answers must agree: a<sup>0</sup> = 1. You will see it in module 2.", " = 0, es decir, a<sup>0</sup>. Las dos respuestas tienen que coincidir: a<sup>0</sup> = 1. Lo verá en el módulo 2.") + "</div>";
  } else {
    h += '<div class="linea">' + cu + " = " + ver(fracX(X("1", "1"), xp("a", n - m))) + "</div>";
    h += '<div class="linea veredicto">' + T((n - m) + fac(n - m) + " left on the bottom. The rule gives ", "Quedan " + (n - m) + fac(n - m) + " abajo. La regla da ") + m + " − " + n + " = " + numTxt(m - n) +
         T(": a<sup>" + numTxt(m - n) + "</sup> means the same as 1/" + xp("a", n - m).h + ". You will see it in module 3.", ": a<sup>" + numTxt(m - n) + "</sup> significa lo mismo que 1/" + xp("a", n - m).h + ". Lo verá en el módulo 3.") + "</div>";
  }
  $("co-salida").innerHTML = h;
}
function genCociente1(){
  var numerica = Math.random() < 0.35, v = elige(VARS), n = ale(2, 6), m = n + ale(1, 7), base = numerica ? String(elige([2, 3, 5, 10])) : v;
  return { enun: ver(igualX(entreX(xp(base, m), xp(base, n)), preg(base))), etiqueta: T("Exponent of the answer", "Exponente del resultado"), resp: m - n,
    pista: function(x){
      if (x === n - m) return T("You subtracted backward: it is always the top exponent minus the bottom one.", "Restó al revés: siempre es el exponente de arriba menos el de abajo.");
      if (x === m + n) return T("You added the exponents; when you divide, subtract them.", "Sumó los exponentes; al dividir se restan.");
      if (n !== 0 && x === m / n) return T("You divided the exponents; subtract them.", "Dividió los exponentes; se restan.");
      return null; },
    sol: T("Same base: ", "Misma base: ") + m + " − " + n + " = " + (m - n) + "." + (numerica ? T(" The base " + base + " does not change.", " La base " + base + " no cambia.") : "") };
}
function genCociente2(){
  var v = elige(["x", "a", "m"]), c2 = ale(2, 6), q = ale(2, 6), c1 = c2 * q, b = ale(1, 5), a = b + ale(1, 6);
  var A = mono(c1, e1(v, a)), B = mono(c2, e1(v, b)), R = mDiv(A, B);
  var dis = [[mono(c1 - c2, R.e), T("You subtracted the numbers; they are divided: ", "Restó los coeficientes; los números se dividen: ") + c1 + " ÷ " + c2 + " = " + q + "."],
             [mono(c1, R.e), T("The numbers still have to be divided.", "Falta dividir los coeficientes.")],
             [mono(q, e1(v, a + b)), T("You added the exponents; when you divide, subtract them.", "Sumó los exponentes; al dividir se restan.")]];
  if (a % b === 0 && a / b !== a - b) dis.push([mono(q, e1(v, a / b)), T("You divided the exponents; subtract them.", "Dividió los exponentes; se restan.")]);
  return { enun: sim() + ver(fracX(mLinea(A), mLinea(B))) + ".", opciones: opcionesMono(R, dis),
    sol: T("Numbers: ", "Coeficientes: ") + c1 + " ÷ " + c2 + " = " + q + T(". Exponents of ", ". Exponentes de ") + v + ": " + a + " − " + b + " = " + (a - b) + "." };
}

/* ============ MODULE 2 · the pattern down to zero ============ */
function actualizaCero(){
  var b = parseInt($("ce-base").value, 10), cab = "", val = "", div = "";
  for (var e = 4; e >= 0; e--){
    cab += "<th scope=\"col\">" + b + "<sup>" + e + "</sup></th>";
    val += "<td" + (e === 0 ? ' class="cero"' : "") + ">" + fmt(Math.pow(b, e)) + "</td>";
    div += '<td class="dividir">' + (e > 0 ? "÷ " + b + " →" : "") + "</td>";
  }
  $("ce-tabla").innerHTML = '<div style="overflow-x:auto"><table class="tabla-patron"><caption>' + T("Powers of " + b + " going down: each step to the right divides by " + b + ".", "Potencias decrecientes de " + b + ": cada paso a la derecha divide entre " + b + ".") +
    "</caption><thead><tr>" + cab + "</tr></thead><tbody><tr>" + val + "</tr><tr>" + div + '</tr></tbody></table></div><p class="nota" style="text-align:center">' + b + " ÷ " + b + T(" = 1: the pattern leads naturally to ", " = 1: el patrón llega de forma natural a ") + b + "<sup>0</sup> = 1.</p>";
}
function genCero(){
  var t = ale(1, 7), k = ale(2, 99), c = ale(2, 9), v = elige(["x", "y", "a"]), a = ale(2, 8);
  function op(x, ok, fb){ return {x: X(fmt(x), numVoz(x)), ok: ok, fb: fb || ""}; }
  var cuanto = T("What is ", "¿Cuánto vale ");
  if (t === 1) return {enun: cuanto + ver(xp(String(k), 0)) + "?",
    opciones: unicas([op(1, true), op(0, false, T("The zero exponent does not wipe out the number: it means the power was divided by itself.", "El exponente cero no anula el número: indica que se ha dividido la potencia entre sí misma.")), op(k, false, T("With exponent zero the value is always 1, whatever the base (other than zero).", "Con exponente cero el valor siempre es 1, sea cual sea la base (distinta de cero)."))]),
    sol: T("Any base other than zero to the power 0 is 1.", "Cualquier base distinta de cero con exponente 0 vale 1.")};
  if (t === 2) return {enun: cuanto + ver(parX(X(c + v, c + " " + v), 0)) + "?",
    opciones: [op(1, true), op(0, false, T("The zero exponent gives 1, not 0.", "El exponente cero da 1, no 0.")), op(c, false, T("The zero affects the whole parentheses, the number too.", "El cero afecta a todo el paréntesis, coeficiente incluido.")), htmlOp(ver(X(c + v, c + " " + v)), false, T("The zero exponent does not just disappear: it turns the whole parentheses into 1.", "El exponente cero no desaparece sin más: convierte todo el paréntesis en 1."))],
    sol: T("The exponent 0 affects everything in the parentheses: (", "El exponente 0 afecta a todo lo que está dentro del paréntesis: (") + c + v + ")<sup>0</sup> = 1."};
  if (t === 3) return {enun: cuanto + ver(X(c + v + "<sup>0</sup>", c + " " + v + VZ.pot + "0")) + "?",
    opciones: [op(c, true), op(1, false, T("The zero affects only the " + v + ", not the " + c + ": with no parentheses, the number stays outside.", "El cero solo afecta a la " + v + ", no al " + c + ": sin paréntesis, el coeficiente queda fuera.")), op(0, false, v + "<sup>0</sup>" + T(" is 1, not 0.", " vale 1, no 0.")), htmlOp(ver(X(c + v, c + " " + v)), false, v + "<sup>0</sup>" + T(" is not " + v + ": it is 1.", " no es " + v + ": es 1."))],
    sol: c + v + "<sup>0</sup> = " + c + " · " + v + "<sup>0</sup> = " + c + " · 1 = " + c + "."};
  if (t === 4) return {enun: cuanto + ver(potX(MENOS + k, numVoz(-k), 0)) + "?",
    opciones: unicas([op(-1, true), op(1, false, T("With no parentheses, the base is only the " + k + ": the minus sign stays outside.", "Sin paréntesis, la base es solo el " + k + ": el signo menos queda fuera y se conserva.")), op(0, false, T("The zero exponent gives 1, not 0.", "El exponente cero da 1, no 0.")), op(-k, false, "")]),
    sol: T("The base is ", "La base es ") + k + ": " + MENOS + k + "<sup>0</sup> = " + MENOS + "(" + k + "<sup>0</sup>) = " + MENOS + "1."};
  if (t === 5) return {enun: cuanto + ver(potX("(" + MENOS + k + ")", VZ.abre + numVoz(-k) + VZ.cierra, 0)) + "?",
    opciones: unicas([op(1, true), op(-1, false, T("With parentheses, the base is the whole " + MENOS + k + ", and any base other than zero to the power 0 is 1.", "Con paréntesis, la base es " + MENOS + k + " completa, y cualquier base distinta de cero con exponente 0 vale 1.")), op(0, false, T("The zero exponent gives 1, not 0.", "El exponente cero da 1, no 0.")), op(-k, false, "")]),
    sol: T("The base is " + MENOS + k + ", not zero: (", "La base es " + MENOS + k + ", distinta de cero: (") + MENOS + k + ")<sup>0</sup> = 1."};
  if (t === 6) return {enun: sim() + ver(entreX(xp(v, a), xp(v, a))) + ".",
    opciones: [op(1, true), op(0, false, T("A number other than zero divided by itself is 1, not 0.", "Un número distinto de cero dividido entre sí mismo da 1, no 0.")), htmlOp(ver(X(v, v)), false, T("No factor of " + v + " is left: they all cancel.", "No queda ningún factor de " + v + ": se cancelan todos.")), htmlOp(ver(xp(v, a)), false, T("The exponents are subtracted: ", "Los exponentes se restan: ") + a + " − " + a + " = 0.")],
    sol: T("By the quotient rule, ", "Por la regla del cociente, ") + v + "<sup>" + a + "−" + a + "</sup> = " + v + "<sup>0</sup> = 1."};
  return {enun: sim() + ver(porX(xp(v, 0), xp(v, a))) + ".",
    opciones: [{x: xp(v, a), ok: true, fb: ""}, op(0, false, v + "<sup>0</sup>" + T(" is 1, not 0: it does not wipe out the product.", " vale 1, no 0: no anula el producto.")), op(1, false, T("Only " + v + "<sup>0</sup> is 1; the other power stays.", "Solo " + v + "<sup>0</sup> vale 1; la otra potencia se conserva.")), {x: xp(v, a + 1), ok: false, fb: T("The zero exponent adds 0, not 1.", "El exponente cero suma 0, no 1.")}],
    sol: v + "<sup>0</sup> · " + v + "<sup>" + a + "</sup> = 1 · " + v + "<sup>" + a + "</sup> = " + v + "<sup>" + a + "</sup>. " + T("With the product rule: 0 + ", "Con la regla del producto: 0 + ") + a + " = " + a + "."};
}

/* ============ MODULE 3 · negative exponents ============ */
function actualizaNegativos(){
  var b = parseInt($("ne-base").value, 10), n = parseInt($("ne-n").value, 10), cab = "", val = "";
  for (var e = 3; e >= -4; e--){
    cab += "<th scope=\"col\">" + b + "<sup>" + numTxt(e) + "</sup></th>";
    val += "<td" + (e === 0 ? ' class="cero"' : (e < 0 ? ' class="neg"' : "")) + ">" + (e >= 0 ? fmt(Math.pow(b, e)) : "1/" + fmt(Math.pow(b, -e))) + "</td>";
  }
  $("ne-tabla").innerHTML = '<div style="overflow-x:auto"><table class="tabla-patron"><caption>' + T("Powers of " + b + " from exponent 3 down to −4: each step to the right divides by " + b + ".", "Potencias de " + b + " desde el exponente 3 hasta el −4: cada paso a la derecha divide entre " + b + ".") + "</caption><thead><tr>" + cab + "</tr></thead><tbody><tr>" + val + "</tr></tbody></table></div>";
  var p = Math.pow(b, n), dec = b === 3 ? "≈ " + (1 / p).toFixed(4) + T(" (a repeating decimal)", " (decimal periódico)") : "= " + String(1 / p);
  $("ne-salida").innerHTML = '<div class="linea">' + ver(igualX(xp(String(b), -n), fracX(X("1", "1"), xp(String(b), n)))) + " = " + ver(fracX(X("1", "1"), X(fmt(p), String(p)))) + " " + dec + "</div>" +
    '<div class="linea veredicto">' + T("The answer is a small positive number: the exponent −" + n + " says “reciprocal of " + b + "<sup>" + n + "</sup>,” not “negative.”", "El resultado es un número positivo y pequeño: el exponente −" + n + " dice «recíproco de " + b + "<sup>" + n + "</sup>», no «negativo».") + "</div>";
}
function genNegativos(){
  var t = ale(1, 5), v = elige(["x", "y", "a", "m"]), n = ale(2, 5), eq = T("What is ", "¿A qué equivale "), eq2 = T(" equal to?", "?");
  if (t === 1){
    var b = ale(2, 5), k = ale(1, 3); if (b === 2 && k === 1) k = 2;
    var p = Math.pow(b, k), f = function(a, d){ return X(a + "/" + d, a + VZ.sobre + d); };
    return {enun: T("What is ", "¿Cuánto vale ") + ver(xp(String(b), -k)) + "?",
      opciones: unicas([{x: f(1, p), ok: true},
        {x: X(MENOS + p, numVoz(-p)), ok: false, fb: T("A negative exponent does not make the number negative: it means the reciprocal.", "El exponente negativo no hace negativo al número: indica el recíproco.")},
        {x: X(MENOS + (b * k), numVoz(-b * k)), ok: false, fb: T("Do not multiply the base by the exponent, and the answer is not negative.", "No se multiplica la base por el exponente, y el resultado no es negativo.")},
        {x: f(1, b * k), ok: false, fb: T("Take the reciprocal of the power " + b + "<sup>" + k + "</sup> = " + p + ", not of the product " + b + " · " + k + ".", "El recíproco es de la potencia " + b + "<sup>" + k + "</sup> = " + p + ", no del producto " + b + " · " + k + ".")},
        {x: X(String(p), String(p)), ok: false, fb: T("You still need to take the reciprocal.", "Falta tomar el recíproco.")}]),
      sol: b + "<sup>" + MENOS + k + "</sup> = 1/" + b + "<sup>" + k + "</sup> = 1/" + p + "."};
  }
  if (t === 2) return {enun: eq + ver(xp(v, -n)) + eq2,
    opciones: [{x: fracX(X("1", "1"), xp(v, n)), ok: true},
      {x: X(MENOS + v + "<sup>" + n + "</sup>", T("minus ", "menos ") + v + VZ.pot + n), ok: false, fb: T("The sign of the exponent does not go to the number.", "El signo del exponente no pasa al número.")},
      {x: fracX(X(String(n), String(n)), X(v, v)), ok: false, fb: T("The exponent does not come down as a number: " + v + " keeps its exponent " + n + " on the bottom.", "El exponente no baja como coeficiente: " + v + " se queda con su exponente " + n + " en el denominador.")},
      {x: fracX(X("1", "1"), xp(v, -n)), ok: false, fb: T("When it crosses the fraction bar, the sign of the exponent changes.", "Al cruzar la barra de fracción, el signo del exponente cambia.")}],
    sol: v + "<sup>" + MENOS + n + "</sup> = 1/" + v + "<sup>" + n + "</sup>."};
  if (t === 3) return {enun: eq + ver(fracX(X("1", "1"), xp(v, -n))) + eq2,
    opciones: [{x: xp(v, n), ok: true},
      {x: fracX(X("1", "1"), xp(v, n)), ok: false, fb: T("When the factor moves up, its exponent changes sign and the 1 on top is no longer needed.", "Si el factor sube, su exponente cambia de signo y el 1 de arriba ya no hace falta.")},
      {x: X(MENOS + v + "<sup>" + n + "</sup>", T("minus ", "menos ") + v + VZ.pot + n), ok: false, fb: T("The answer is not negative.", "El resultado no es negativo.")},
      {x: xp(v, -n), ok: false, fb: T("When it crosses the bar, the negative exponent becomes positive.", "Al cruzar la barra, el exponente negativo pasa a positivo.")}],
    sol: T("Moving " + v + "<sup>" + MENOS + n + "</sup> to the top changes the sign of its exponent: ", "Al subir " + v + "<sup>" + MENOS + n + "</sup> al numerador, el exponente cambia de signo: ") + v + "<sup>" + n + "</sup>."};
  if (t === 4){
    var c = ale(2, 9);
    return {enun: eq + ver(X(c + v + "<sup>" + MENOS + n + "</sup>", c + " " + v + VZ.pot + numVoz(-n))) + eq2,
      opciones: [{x: fracX(X(String(c), String(c)), xp(v, n)), ok: true},
        {x: fracX(X("1", "1"), X(c + v + "<sup>" + n + "</sup>", c + " " + v + VZ.pot + n)), ok: false, fb: T("The negative exponent affects only the " + v + ": the " + c + " stays on top.", "El exponente negativo solo afecta a la " + v + ": el " + c + " se queda arriba.")},
        {x: X(MENOS + c + v + "<sup>" + n + "</sup>", T("minus ", "menos ") + c + " " + v + VZ.pot + n), ok: false, fb: T("The sign of the exponent does not make the term negative.", "El signo del exponente no hace negativo al término.")},
        {x: X(c + v + "<sup>" + n + "</sup>", c + " " + v + VZ.pot + n), ok: false, fb: T("The " + v + " still has to move to the bottom.", "Falta llevar la " + v + " al denominador.")}],
      sol: c + v + "<sup>" + MENOS + n + "</sup> = " + c + " · 1/" + v + "<sup>" + n + "</sup> = " + c + "/" + v + "<sup>" + n + "</sup>."};
  }
  var a = ale(1, 6), bb = ale(2, 8), R = mMul(xv(v, a), xv(v, -bb));
  return {enun: sim() + ver(porX(xp(v, a), xp(v, -bb))) + T(" and leave no negative exponents.", " y deje el resultado sin exponentes negativos."),
    opciones: opcionesMono(R, [[xv(v, a + bb), T("The exponent " + MENOS + bb + " is negative: adding it means subtracting " + bb + ".", "El exponente " + MENOS + bb + " es negativo: sumarlo es restar " + bb + ".")],
      [xv(v, -(a + bb)), ""], [xv(v, bb - a), T("Check the sign: ", "Revise el signo: ") + a + " + (" + MENOS + bb + ") = " + numTxt(a - bb) + "."]]),
    sol: T("Product rule: ", "Regla del producto: ") + a + " + (" + MENOS + bb + ") = " + numTxt(a - bb) + (a - bb < 0 ? T(", and the negative exponent moves to the bottom.", ", y el exponente negativo se pasa al denominador.") : a - bb === 0 ? T(", and ", ", y ") + v + "<sup>0</sup> = 1." : ".")};
}

/* ============ MODULE 4 · which rule was used? ============ */
var REGLAS5 = [["producto", T("Product of powers", "Producto de potencias")], ["potpot", T("Power of a power", "Potencia de una potencia")], ["potprod", T("Power of a product", "Potencia de un producto")],
               ["cociente", T("Quotient of powers", "Cociente de potencias")], ["cero", T("Zero exponent", "Exponente cero")], ["negativo", T("Negative exponent", "Exponente negativo")]];
function genCinco(){
  var r = elige(REGLAS5), v = elige(["x", "y", "a"]), paso, a = ale(2, 7), b = ale(2, 6), c = ale(2, 5), bb = b > 4 ? 3 : b;
  if (r[0] === "producto") paso = igualX(porX(xp(v, a), xp(v, b)), xp(v, a + b));
  else if (r[0] === "potpot") paso = igualX(parX(xp(v, a), b), xp(v, a * b));
  else if (r[0] === "potprod") paso = igualX(parX(X(c + v, c + " " + v), bb), X(Math.pow(c, bb) + v + "<sup>" + bb + "</sup>", Math.pow(c, bb) + " " + v + VZ.pot + bb));
  else if (r[0] === "cociente") paso = igualX(entreX(xp(v, a + b), xp(v, b)), xp(v, a));
  else if (r[0] === "cero") paso = igualX(parX(X(c + v, c + " " + v), 0), X("1", "1"));
  else paso = igualX(xp(v, -a), fracX(X("1", "1"), xp(v, a)));
  var otras = mezcla(REGLAS5.filter(function(x){ return x[0] !== r[0]; })).slice(0, 3);
  var porque = {producto: T("Two powers with the same base are multiplied: the exponents are added.", "Dos potencias de la misma base multiplicadas: los exponentes se suman."),
    potpot: T("A power raised to a power: the exponents are multiplied.", "Una potencia elevada a otra: los exponentes se multiplican."),
    potprod: T("A product raised to an exponent: the exponent goes to each factor, the number too.", "Un producto elevado a un exponente: el exponente se reparte a cada factor, coeficiente incluido."),
    cociente: T("Two powers with the same base are divided: the exponents are subtracted.", "Dos potencias de la misma base divididas: los exponentes se restan."),
    cero: T("Any base other than zero to the power 0 is 1.", "Cualquier base distinta de cero con exponente 0 vale 1."),
    negativo: T("A negative exponent means the reciprocal of the positive power.", "El exponente negativo indica el recíproco de la potencia positiva.")};
  var ops = [htmlOp(r[1], true)].concat(otras.map(function(o){ return htmlOp(o[1], false, T("That rule does not fit this step. Look at the operation on the left of the equal sign.", "Esa regla no corresponde a este paso. Fíjese en la operación a la izquierda del signo igual.")); }));
  return {enun: T("Which rule explains this step? ", "¿Qué regla justifica este paso? ") + ver(paso), opciones: ops, sol: porque[r[0]], regla: r[0]};
}

/* ============ MODULE 5 · checking with numbers ============ */
var V = {caso: null};
function genCaso(){
  var t = ale(1, 5), bien = Math.random() < 0.5, orig, R, P, error;
  if (t === 1){
    var c1 = ale(2, 5), c2 = ale(2, 5), a = ale(2, 4), b = ale(2, 4), A = mono(c1, {x: a}), B = mono(c2, {x: b});
    orig = porX(parX(mLinea(A)), parX(mLinea(B))); R = mMul(A, B);
    if (Math.random() < 0.5 && !(a === 2 && b === 2)){ P = mono(c1 * c2, {x: a * b}); error = T("The exponents were multiplied; in a product they are added.", "Se multiplicaron los exponentes; en un producto se suman."); }
    else { P = mono(c1 + c2, {x: a + b}); error = T("The numbers were added; they are multiplied.", "Se sumaron los coeficientes; se multiplican."); }
  } else if (t === 2){
    var c = ale(2, 4), a2 = ale(1, 3), n = ale(2, 3), A2 = mono(c, {x: a2});
    orig = parX(mLinea(A2), n); R = mPow(A2, n); P = mono(c, R.e); error = T("The number was not raised: ", "Faltó elevar el coeficiente: ") + c + "<sup>" + n + "</sup> = " + Math.pow(c, n) + ".";
  } else if (t === 3){
    var b3 = ale(2, 4), a3 = b3 + ale(1, 4);
    orig = entreX(xp("x", a3), xp("x", b3)); R = xv("x", a3 - b3); P = xv("x", b3 - a3); error = T("The subtraction was done backward: it is the top exponent minus the bottom one.", "Se restó al revés: es el exponente de arriba menos el de abajo.");
  } else if (t === 4){
    var a4 = ale(2, 5), b4 = ale(1, 4); if (b4 === a4) b4 = a4 + 1;
    orig = porX(xp("x", a4), xp("x", -b4)); R = xv("x", a4 - b4); P = xv("x", a4 + b4); error = T("The sign of the negative exponent was ignored: ", "Se ignoró el signo del exponente negativo: ") + a4 + " + (" + MENOS + b4 + ") = " + numTxt(a4 - b4) + ".";
  } else {
    var k = ale(2, 7), a5 = ale(2, 5);
    orig = porX(X(k + "x<sup>0</sup>", k + " x" + VZ.pot + "0"), xp("x", a5)); R = mono(k, {x: a5}); P = xv("x", a5); error = T("The zero exponent affects only the x: " + k + "x<sup>0</sup> is " + k + ", not 1.", "El exponente cero solo afecta a la x: " + k + "x<sup>0</sup> vale " + k + ", no 1.");
  }
  if (bien) P = R;
  return {orig: orig, R: R, P: P, bien: mIgual(P, R), error: error};
}
function pruebaValor(x){
  var o = mValor(V.caso.R, {x: x}), p = mValor(V.caso.P, {x: x});
  var h = '<div class="linea">' + T("With x = " + numTxt(x) + ", the original expression is ", "Con x = " + numTxt(x) + ", la expresión original vale ") + "<strong>" + ver(valX(o)) + "</strong>.</div>" +
          '<div class="linea">' + T("With x = " + numTxt(x) + ", the proposed answer is ", "Con x = " + numTxt(x) + ", la simplificación propuesta vale ") + "<strong>" + ver(valX(p)) + "</strong>.</div>";
  h += '<div class="linea veredicto">' + (ratIgual(o, p)
        ? T("The two values match.", "Los dos valores coinciden.") + (Math.abs(x) === 1 ? T(" But with x = " + numTxt(x) + " almost every power gives the same: try 2 or 3 before you trust it.", " Pero con x = " + numTxt(x) + " casi todas las potencias dan lo mismo: pruebe con 2 o con 3 antes de fiarse.") : T(" That is a good sign; if they also match with another value, the answer is almost surely right.", " Es buena señal; si coinciden también con otro valor, la simplificación es casi con seguridad correcta."))
        : T("The values do not match: the work has a mistake.", "Los valores no coinciden: la simplificación tiene un error.")) + "</div>";
  return h;
}
function probar(){
  if (!V.caso) return;
  var x = leeEntero("v-x", -5, 5, "v-aviso", T("test value", "valor de prueba"));
  if (x === null) return;
  if (x === 0){ $("v-x").classList.add("error"); $("v-aviso").className = "caja-aviso visible"; $("v-aviso").textContent = T("With x = 0 there are divisions by zero or powers that are not defined. Choose another value, like 2 or 3.", "Con x = 0 hay divisiones entre cero o potencias sin definir. Elija otro valor, como 2 o 3."); return; }
  limpiaAviso("v-aviso");
  $("v-salida").innerHTML = pruebaValor(x);
}
function genVerifica(){
  var c = genCaso(); V.caso = c;
  if ($("v-salida")){ $("v-salida").innerHTML = ""; limpiaAviso("v-aviso"); }
  var expl = c.bien ? T("The work is correct: ", "La simplificación es correcta: ") + ver(igualX(c.orig, mFinal(c.R))) + "."
                    : T("The work has a mistake. ", "La simplificación tiene un error. ") + c.error + T(" The right answer is ", " Lo correcto es ") + ver(mFinal(c.R)) + ".";
  return {enun: T("Someone simplified it like this: ", "Alguien simplificó así: ") + ver(igualX(c.orig, mFinal(c.P))), enOrden: true,
    opciones: [htmlOp(T("The work is correct", "La simplificación es correcta"), c.bien), htmlOp(T("The work has a mistake", "La simplificación tiene un error"), !c.bien)],
    sol: expl + " " + T("Test with x = 2: ", "Prueba con x = 2: ") + (function(){ var o = mValor(c.R, {x: 2}), p = mValor(c.P, {x: 2}); return T("the original gives ", "la original da ") + ver(valX(o)) + T(" and the proposed answer gives ", " y la propuesta da ") + ver(valX(p)) + "."; })()};
}

/* ============ Start ============ */
["co-m", "co-n"].forEach(function(id){ $(id).addEventListener("input", actualizaCociente); });
actualizaCociente();
ESCRITA("p-cociente1", genCociente1);
OM("p-cociente2", genCociente2);
$("ce-base").addEventListener("change", actualizaCero);
actualizaCero();
OM("p-cero", genCero);
$("ne-base").addEventListener("change", actualizaNegativos);
$("ne-n").addEventListener("change", actualizaNegativos);
actualizaNegativos();
OM("p-negativos", genNegativos);
OM("p-cinco", genCinco, REGLAS5);
OM("p-verifica", genVerifica);
$("v-probar").addEventListener("click", probar);
$("v-x").addEventListener("keydown", function(e){ if (e.key === "Enter") probar(); });
'''

def practica_pagina():
    n = N
    P = n3
    filas = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{d}</td></tr>" for a, b, c, d in n3.tabla_reglas(True))
    mods = [
     (t("quotient", "cociente"), t("The quotient rule", "La regla del cociente"),
      f'''      <p>{t("When you divide two powers with the <strong>same base</strong>, each factor on the bottom cancels a factor on the top. That is why the exponents are <strong>subtracted</strong>, always the top one minus the bottom one:", "Al dividir dos potencias de la <strong>misma base</strong>, cada factor de abajo cancela un factor de arriba. Por eso los exponentes <strong>se restan</strong>, siempre el de arriba menos el de abajo:")}</p>
{P.formula("a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m − n</sup>")}
      <h3>{t("Factor canceller", "Cancelador de factores")}</h3>
      <p>{t("Change the top and bottom exponents. Also try the same number in both, or a bigger one on the bottom: that is how you discover the ideas of the next two modules.", "Cambie los exponentes de arriba y de abajo. Pruebe también el mismo número en los dos, o uno mayor abajo: así se descubren las ideas de los dos módulos siguientes.")}</p>
{P.panel(P.numero("co-m", t("Top exponent", "Exponente de arriba"), 5, 1, 7), P.numero("co-n", t("Bottom exponent", "Exponente de abajo"), 2, 1, 7))}
{P.aviso("co-aviso")}
      <div class="linea-frac" id="co-fichas" aria-hidden="true"></div>
{P.salida("co-salida")}
{P.atencion(t("Watch the order:", "Cuidado con el orden:"), t("subtract the top exponent minus the bottom one, never the other way around. And the base cannot be zero, because dividing by zero is not defined.", "se resta el exponente de arriba menos el de abajo, nunca al revés. Y la base no puede ser cero, porque dividir entre cero no está definido."))}
{P.escrita("p-cociente1", t("Practice: write the exponent of the answer", "Practique: escriba el exponente del resultado"), t("Exponent of the answer", "Exponente del resultado"))}
      <h3>{t("Practice: with numbers in front", "Practique: con coeficientes")}</h3>
      <p>{t("The numbers are <strong>divided</strong>; the exponents are <strong>subtracted</strong>.", "Los coeficientes se <strong>dividen</strong>; los exponentes se <strong>restan</strong>.")}</p>
{B.om("p-cociente2", "").replace("<h3></h3>", "")}'''),
     (t("zero", "cero"), t("The zero exponent", "El exponente cero"),
      f'''      <p>{t("If you divide a power by itself, the answer is 1, because any number other than zero divided by itself is 1. But the quotient rule gives a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>0</sup>. Both describe the same division, so they must be equal:", "Si divide una potencia entre sí misma, el resultado es 1, porque todo número distinto de cero dividido entre sí mismo da 1. Pero la regla del cociente da a<sup>3</sup> ÷ a<sup>3</sup> = a<sup>0</sup>. Las dos cosas describen la misma división, así que tienen que ser iguales:")}</p>
{P.formula("a<sup>0</sup> = 1  (a ≠ 0)")}
      <h3>{t("The pattern of shrinking powers", "El patrón de potencias decrecientes")}</h3>
      <p>{t("Each time the exponent goes down by one, the value is divided by the base. Choose a base and follow the pattern down to zero.", "Cada vez que el exponente baja una unidad, el valor se divide entre la base. Elija una base y siga el patrón hasta el cero.")}</p>
{P.panel(P.lista("ce-base", t("Base", "Base"), [(2, "2"), (3, "3"), (5, "5"), (10, "10")]))}
      <div id="ce-tabla" aria-live="polite"></div>
{P.atencion(t("The zero affects only its own base:", "El exponente cero solo afecta a su base:"), t("(3x)<sup>0</sup> = 1, because the zero reaches the whole parentheses; but 3x<sup>0</sup> = 3 · 1 = 3, because the zero reaches only the x. In the same way, −5<sup>0</sup> = −1, while (−5)<sup>0</sup> = 1.", "(3x)<sup>0</sup> = 1, porque el cero afecta a todo el paréntesis; pero 3x<sup>0</sup> = 3 · 1 = 3, porque el cero solo afecta a la x. Del mismo modo, −5<sup>0</sup> = −1, mientras que (−5)<sup>0</sup> = 1."))}
{B.om("p-cero", t("Practice: what is it worth?", "Practique: ¿cuánto vale?"))}'''),
     (t("negatives", "negativos"), t("Negative exponents", "Los exponentes negativos"),
      f'''      <p>{t("If the pattern keeps going past zero, each step still divides by the base, and fractions appear. A negative exponent means the <strong>reciprocal</strong> of the power with a positive exponent:", "Si el patrón sigue más allá del cero, cada paso sigue dividiendo entre la base y aparecen las fracciones. Un exponente negativo indica el <strong>recíproco</strong> de la potencia con exponente positivo:")}</p>
{P.formula("a<sup>−n</sup> = 1/a<sup>n</sup>  (a ≠ 0)")}
      <h3>{t("The pattern keeps going", "El patrón continúa")}</h3>
{P.panel(P.lista("ne-base", t("Base", "Base"), [(2, "2"), (3, "3"), (5, "5"), (10, "10")]), P.lista("ne-n", t("Negative exponent to study", "Exponente negativo que quiere estudiar"), [(1, "−1"), (2, "−2"), (3, "−3"), (4, "−4")], 2))}
      <div id="ne-tabla"></div>
{P.salida("ne-salida")}
      <div class="caja-tip"><strong>{t("Crossing the fraction bar:", "Cruzar la barra de fracción:")}</strong> {t("moving a factor from top to bottom, or from bottom to top, changes the sign of its exponent. So x<sup>−4</sup> = 1/x<sup>4</sup> and also 1/a<sup>−2</sup> = a<sup>2</sup>.", "mover un factor de arriba abajo, o de abajo arriba, cambia el signo de su exponente. Así, x<sup>−4</sup> = 1/x<sup>4</sup> y también 1/a<sup>−2</sup> = a<sup>2</sup>.")}</div>
{P.atencion(t("A negative exponent does not make the number negative.", "Un exponente negativo no hace negativo al número."), t("2<sup>−3</sup> is not −8 and not −6: it is the positive fraction 1/8. The sign of the exponent only says “reciprocal.”", "2<sup>−3</sup> no es −8 ni −6: es la fracción positiva 1/8. El signo del exponente solo dice «recíproco»."))}
{B.om("p-negativos", t("Practice: negative exponents", "Practique: exponentes negativos"))}'''),
     (t("five-rules", "cinco-reglas"), t("The five rules of exponents", "Las cinco reglas de los exponentes"),
      f'''      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("The five rules (table you can scroll sideways)", "Las cinco reglas (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("The five rules of exponents: name, pattern, and example.", "Las cinco reglas de los exponentes: nombre, patrón y ejemplo.")}</caption>
      <thead><tr><th scope="col">{t("Rule", "Regla")}</th><th scope="col">{t("Pattern", "Patrón")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead><tbody>{filas}</tbody></table></div>
      <h3>{t("Practice: which rule was used?", "Practique: ¿qué regla se aplicó?")}</h3>
      <p>{t("Each exercise shows a step that is already done, and done correctly. Your job is to say which rule explains it. The table under the exercise shows which rule you need to review.", "Cada ejercicio muestra un paso ya hecho, y bien hecho. Su tarea es reconocer qué regla lo justifica. La tabla de debajo del ejercicio le dice qué regla necesita repasar.")}</p>
{B.om("p-cinco", "").replace("<h3></h3>", "")}'''),
     (t("check", "verificar"), t("Checking with numbers", "Verificar con valores numéricos"),
      f'''      <p>{t("A correct simplification gives the <strong>same number</strong> as the original expression for any value of the letter. If you replace the letter with a number and get different values, there is a mistake for sure. It is the same check you would do on the calculator.", "Una simplificación correcta da el <strong>mismo número</strong> que la expresión original para cualquier valor de la variable. Si al sustituir un número salen valores distintos, hay un error seguro. Es la misma comprobación que haría con la calculadora.")}</p>
{P.atencion(t("Choose the test number well:", "Elija bien el número de prueba:"), t("0 does not work when there are divisions or negative exponents, and with 1 every power is 1, so the test tells you nothing. Use 2 or 3.", "el 0 no sirve cuando hay divisiones o exponentes negativos, y con el 1 cualquier potencia vale 1, así que la prueba no distingue nada. Use 2 o 3."))}
      <h3>{t("Practice: is the work correct?", "Practique: ¿la simplificación es correcta?")}</h3>
      <p>{t("First test with one or two values of x. Then decide.", "Primero pruebe con uno o dos valores de x. Después decida.")}</p>
      <div class="panel"><div class="campos">{P.numero("v-x", t("Value of x for the test", "Valor de x para la prueba"), 2, -5, 5)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="v-probar">{t("Test this value", "Probar este valor")}</button></div></div>
{P.aviso("v-aviso")}
{P.salida("v-salida")}
{B.om("p-verifica", "").replace("<h3></h3>", "")}''')]
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_EXP, scripts=("/math/exponents.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Regla del cociente, exponente cero y exponentes negativos")
