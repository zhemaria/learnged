"""Level 3 · Lesson 3.1 · Simplifying radicals with perfect-square factors — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "3-1"
TEMA = ("Radicals and the real numbers", "Radicales y números reales")
TIT = ("Simplifying radicals with perfect-square factors", "Simplificar radicales: factorización en cuadrados perfectos")

def r(k, n=None):
    """k√n, or √k when n is None."""
    if n is None:
        return f'<span class="rad">√<span class="rc">{k}</span></span>'
    return f'{k}<span class="rad">√<span class="rc">{n}</span></span>'

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    filas = [[str(i), str(i * i)] for i in range(1, 16)]
    s1 = f'''<p>{t("Topic 2 finished the work with powers of 10 and scientific notation. The square root is the opposite of squaring: if 6<sup>2</sup> = 36, then √36 = 6. In Level 2 you worked with the roots of perfect squares; now you will learn to simplify radicals whose radicand is not a perfect square, taking out of it the largest square part you can.",
"El Tema 2 cerró el trabajo con potencias de 10 y notación científica. La raíz cuadrada es la operación inversa de elevar al cuadrado: si 6<sup>2</sup> = 36, entonces √36 = 6. En el Nivel 2 trabajó las raíces de los cuadrados perfectos; ahora aprenderá a simplificar radicales cuyo radicando no es un cuadrado perfecto, extrayendo de él la mayor parte cuadrada posible.")}</p>
<p>{t("The key idea is that the root of a product can be split into the product of the roots:", "La idea central para simplificar es que la raíz de un producto se puede separar en el producto de las raíces:")}</p>
{big(f'√(a · b) = {r("a")} · {r("b")}')}
<p>{t("This property lets you “take out” of the radical any factor that is a perfect square, and leave inside only what is not. To spot those factors, you need the perfect squares at your fingertips.", "Esta propiedad permite «sacar» del radical cualquier factor que sea un cuadrado perfecto y dejar dentro solo lo que no lo es. Para ver esos factores hace falta tener a mano los cuadrados perfectos.")}</p>
{tabla(t("Perfect squares from 1 to 15", "Cuadrados perfectos del 1 al 15"), t("Perfect squares: each number from 1 to 15 and its square", "Cuadrados perfectos: cada número del 1 al 15 y su cuadrado"), ["n", "n<sup>2</sup>"], filas)}
{enlace(n, t("product", "producto"), t("the product property of radicals", "la propiedad del producto de radicales"), t("Split a radical with each perfect square that divides it and compare what is left inside.", "Parta un radical con cada cuadrado perfecto que lo divide y compare lo que queda dentro."))}'''

    s2 = f'''<p>{t("The procedure: find the <strong>largest</strong> perfect square that divides the radicand, split it off with the product property, and take its root.", "El procedimiento busca el <strong>mayor</strong> cuadrado perfecto que divide al radicando, lo separa con la propiedad del producto y extrae su raíz.")}</p>
{big(f'{r(72)} = √(36 · 2) = {r(36)} · {r(2)} = {r(6, 2)}')}
{ejemplo(t(f"Example 1: simplify {r(50)}", f"Ejemplo 1: simplifique {r(50)}"),
  [("1", t("Largest square.", "Mayor cuadrado."), t("The largest perfect square that divides 50 is 25: 50 = 25 · 2.", "El mayor cuadrado perfecto que divide a 50 es 25: 50 = 25 · 2.")),
   ("2", t("Split.", "Separar."), f"{r(50)} = {r(25)} · {r(2)}."),
   ("3", t("Take the root.", "Extraer la raíz."), f"{r(25)} = 5."),
   ("✓", t("Answer.", "Respuesta."), f"{r(50)} = <strong>{r(5, 2)}</strong>")])}
{ejemplo(t(f"Example 2: simplify {r(48)}", f"Ejemplo 2: simplifique {r(48)}"),
  [("1", t("Largest square.", "Mayor cuadrado."), "48 = 16 · 3."),
   ("2", t("Split and take the root.", "Separar y extraer."), f"{r(48)} = {r(16)} · {r(3)} = {r(4, 3)}."),
   ("✓", t("Answer.", "Respuesta."), f"{r(48)} = <strong>{r(4, 3)}</strong>")])}
{caja("ojo", t("Look for the largest", "Busque el mayor"), t(f"<p>If you use a small perfect square, there is still something left to simplify. For example, {r(72)} = √(4 · 18) = {r(2, 18)}, but {r(18)} can still be reduced. Look for the largest one right away: 36.</p>", f"<p>Si se usa un cuadrado perfecto pequeño, todavía quedará algo por simplificar. Por ejemplo, {r(72)} = √(4 · 18) = {r(2, 18)}, pero {r(18)} aún se puede reducir. Conviene buscar de una vez el mayor: 36.</p>"))}
{practica("p1", t("Practice 1 — A small one", "Práctica 1 — Uno pequeño"), t(f"What is {r(8)} simplified?", f"¿Cuál es la forma simplificada de {r(8)}?"),
          [("a", r(4, 2)), ("b", r(2, 2)), ("c", t(f"{r(8)} is already simple", f"{r(8)} ya es simple")), ("d", r(2, 4))])}
{practica("p2", t("Practice 2 — Find the square", "Práctica 2 — Encuentre el cuadrado"), t(f"What is {r(75)} simplified?", f"¿Cuál es la forma simplificada de {r(75)}?"),
          [("a", r(5, 3)), ("b", r(3, 5)), ("c", r(25, 3)), ("d", r(15, 5))])}
{practica("p3", t("Practice 3 — A larger one", "Práctica 3 — Uno mayor"), t(f"What is {r(98)} simplified?", f"¿Cuál es la forma simplificada de {r(98)}?"),
          [("a", r(2, 7)), ("b", r(49, 2)), ("c", r(7, 2)), ("d", r(14, 7))])}
{enlace(n, t("numbers", "numericos"), t("simplifying number radicals", "simplificar radicales numéricos"), t("Reveal the steps one at a time, then simplify radicals yourself.", "Revele los pasos uno a uno y después simplifique radicales usted."))}'''

    s3 = f'''<p>{t(f"A variable with an <strong>even</strong> exponent is a perfect square, because its square root is the same variable with half the exponent: {r('x<sup>4</sup>')} = x<sup>2</sup>, since (x<sup>2</sup>)<sup>2</sup> = x<sup>4</sup>. In this lesson x is always positive, as in the problems on the test.",
f"Una variable con exponente <strong>par</strong> es un cuadrado perfecto, porque su raíz cuadrada es la misma variable con la mitad del exponente: {r('x<sup>4</sup>')} = x<sup>2</sup>, ya que (x<sup>2</sup>)<sup>2</sup> = x<sup>4</sup>. En esta lección x es siempre positiva, como en los problemas del examen.")}</p>
{ejemplo(t(f"Example 3: simplify {r('x<sup>6</sup>')}", f"Ejemplo 3: simplifique {r('x<sup>6</sup>')}"),
  [("1", t("Even exponent.", "Exponente par."), t("6 is even, so x<sup>6</sup> is a perfect square.", "6 es par, así que x<sup>6</sup> es un cuadrado perfecto.")),
   ("2", t("Half.", "La mitad."), "6 ÷ 2 = 3."),
   ("✓", t("Answer.", "Respuesta."), f"{r('x<sup>6</sup>')} = <strong>x<sup>3</sup></strong>")])}
{ejemplo(t(f"Example 4: simplify {r('9x<sup>2</sup>')}", f"Ejemplo 4: simplifique {r('9x<sup>2</sup>')}"),
  [("1", t("Split.", "Separar."), f"{r(9)} · {r('x<sup>2</sup>')}."),
   ("2", t("Take each root.", "Cada raíz."), f"{r(9)} = 3 " + t("and", "y") + f" {r('x<sup>2</sup>')} = x."),
   ("✓", t("Answer.", "Respuesta."), f"{r('9x<sup>2</sup>')} = <strong>3x</strong>")])}
{caja("tip", t("When is it simple?", "¿Cuándo ya está simple?"), t(f"<p>A radical is in its simplest form when the radicand has no factor (other than 1) that is a perfect square. {r(15)} is already simple, because 15 = 3 · 5 and neither 3 nor 5 is a perfect square. With an <strong>odd</strong> exponent, one x stays inside: {r('x<sup>5</sup>')} = x<sup>2</sup>{r('x')}.</p>",
f"<p>Un radical está en su forma más simple cuando el radicando no tiene ningún factor (distinto de 1) que sea un cuadrado perfecto. {r(15)} ya es simple, porque 15 = 3 · 5 y ni 3 ni 5 son cuadrados perfectos. Con exponente <strong>impar</strong>, una x se queda dentro: {r('x<sup>5</sup>')} = x<sup>2</sup>{r('x')}.</p>"))}
{practica("p4", t("Practice 4 — An even exponent", "Práctica 4 — Un exponente par"), t(f"What is {r('x<sup>8</sup>')}?", f"¿Cuánto es {r('x<sup>8</sup>')}?"),
          [("a", "x<sup>4</sup>"), ("b", "x<sup>8</sup>"), ("c", "x<sup>16</sup>"), ("d", "x<sup>6</sup>")])}
{practica("p5", t("Practice 5 — A number and a letter", "Práctica 5 — Número y letra"), t(f"What is {r('25x<sup>2</sup>')}?", f"¿Cuánto es {r('25x<sup>2</sup>')}?"),
          [("a", "25x"), ("b", "5x"), ("c", "5x<sup>2</sup>"), ("d", "12.5x")])}
{practica("p6", t("Practice 6 — Already simple?", "Práctica 6 — ¿Ya es simple?"), t("Which radical is already in its simplest form?", "¿Cuál radical ya está en su forma más simple?"),
          [("a", r(18)), ("b", r(50)), ("c", r(7)), ("d", r(12))])}
{enlace(n, t("variables", "variables"), t("radicals with variables", "radicales con variables"), t("Take the even exponents out of the radical and leave inside what is left.", "Saque del radical los exponentes pares y deje dentro lo que sobra."))}'''

    s4 = f'''<p>{t("Simplifying does not change the value of the radical, only its form. A reliable check is to work out both expressions on the calculator: they must give the same decimal.", "Simplificar no cambia el valor del radical, solo su forma. Una comprobación confiable es calcular las dos expresiones en la calculadora: deben dar el mismo decimal.")}</p>
{ejemplo(t(f"Example 5: check that {r(72)} = {r(6, 2)}", f"Ejemplo 5: compruebe que {r(72)} = {r(6, 2)}"),
  [("1", t("On the calculator.", "En la calculadora."), f"{r(72)} ≈ 8.485."),
   ("2", t("The other side.", "El otro lado."), f"6 × {r(2)} ≈ 6 × 1.414 = 8.485."),
   ("✓", t("Answer.", "Respuesta."), t(f"Both give 8.485, so {r(72)} = {r(6, 2)} is right.", f"Las dos dan 8.485, así que {r(72)} = {r(6, 2)} es correcto."))])}
{calc(t("Square roots on the calculator", "La raíz cuadrada en la calculadora"), t(f"<p>The square root is the second function of the {T('x<sup>2</sup>')} key: {T('2nd')} {T('x<sup>2</sup>')} {T('7')} {T('2')} {T('enter')} shows 8.485281374. Then {T('6')} {T('×')} {T('2nd')} {T('x<sup>2</sup>')} {T('2')} {T('enter')} shows the same number.</p>",
f"<p>La raíz cuadrada es la segunda función de la tecla {T('x<sup>2</sup>')}: {T('2nd')} {T('x<sup>2</sup>')} {T('7')} {T('2')} {T('enter')} muestra 8.485281374. Después {T('6')} {T('×')} {T('2nd')} {T('x<sup>2</sup>')} {T('2')} {T('enter')} muestra el mismo número.</p>"))}
{caja("ojo", t("Same value is not enough", "El mismo valor no basta"), t(f"<p>Matching decimals show the value is right, but not that the answer is <strong>finished</strong>. {r(2, 18)} has the same value as {r(72)} and can still be simplified. Checking does not replace the procedure; it confirms it.</p>", f"<p>Que los decimales coincidan muestra que el valor es correcto, pero no que la respuesta esté <strong>terminada</strong>. {r(2, 18)} vale lo mismo que {r(72)} y todavía se puede simplificar. Verificar no reemplaza el procedimiento: lo confirma.</p>"))}
{enlace(n, t("check", "verificar"), t("checking the answer", "verificar el resultado"), t("Decide whether a simplification is right, unfinished, or wrong.", "Decida si una simplificación es correcta, incompleta o equivocada."))}'''

    secciones = [("s-" + t("product", "producto"), t("The product property of radicals", "La propiedad del producto de radicales"), s1),
                 ("s-" + t("numbers", "numericos"), t("Simplifying number radicals", "Simplificar radicales numéricos"), s2),
                 ("s-" + t("variables", "variables"), t("Simplifying radicals with variables", "Simplificar radicales con variables"), s3),
                 ("s-" + t("check", "verificar"), t("Checking with the calculator", "Verificar con la calculadora"), s4)]

    lesson = {"next": t("Lesson 3.2", "Lección 3.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("When you take out the 4, write its root (2), not the 4.", "Al sacar el 4, se escribe su raíz (2), no el 4."), "c": t("8 = 4 · 2, and 4 is a perfect square.", "8 = 4 · 2, y 4 es un cuadrado perfecto."), "d": t("The 2 that comes out goes in front; the 2 that stays goes inside.", "El 2 que sale va delante; el 2 que queda va dentro.")},
             "right": t(f"8 = 4 · 2, so {r(8)} = {r(2, 2)}.", f"8 = 4 · 2, así que {r(8)} = {r(2, 2)}."), "solution": t(f"{r(8)} = {r(4)} · {r(2)} = {r(2, 2)}.", f"{r(8)} = {r(4)} · {r(2)} = {r(2, 2)}.")},
      "p2": {"ok": "a", "hints": {"b": t("The number outside and the number inside were swapped.", "Se intercambiaron el número de fuera y el de dentro."), "c": t("When you take out the 25, write its root (5).", "Al sacar el 25, se escribe su raíz (5)."), "d": t("75 = 25 · 3. Look for the perfect square that divides 75.", "75 = 25 · 3. Busque el cuadrado perfecto que divide a 75.")},
             "right": t(f"75 = 25 · 3, so {r(75)} = {r(5, 3)}.", f"75 = 25 · 3, así que {r(75)} = {r(5, 3)}."), "solution": t(f"{r(75)} = {r(25)} · {r(3)} = {r(5, 3)}.", f"{r(75)} = {r(25)} · {r(3)} = {r(5, 3)}.")},
      "p3": {"ok": "c", "hints": {"a": t("The number outside and the number inside were swapped.", "Se intercambiaron el número de fuera y el de dentro."), "b": t("When you take out the 49, write its root (7).", "Al sacar el 49, se escribe su raíz (7)."), "d": t("98 = 49 · 2. Which perfect square divides 98?", "98 = 49 · 2. ¿Qué cuadrado perfecto divide a 98?")},
             "right": t(f"98 = 49 · 2, so {r(98)} = {r(7, 2)}.", f"98 = 49 · 2, así que {r(98)} = {r(7, 2)}."), "solution": t(f"{r(98)} = {r(49)} · {r(2)} = {r(7, 2)}.", f"{r(98)} = {r(49)} · {r(2)} = {r(7, 2)}.")},
      "p4": {"ok": "a", "hints": {"b": t("Taking the root halves the exponent.", "Sacar la raíz divide el exponente entre 2."), "c": t("You doubled the exponent. Take half: 8 ÷ 2.", "Duplicó el exponente. Tome la mitad: 8 ÷ 2."), "d": t("Take half the exponent, do not subtract 2.", "Se toma la mitad del exponente, no se le resta 2.")},
             "right": "(x<sup>4</sup>)<sup>2</sup> = x<sup>8</sup>.", "solution": t(f"8 ÷ 2 = 4, so {r('x<sup>8</sup>')} = x<sup>4</sup>.", f"8 ÷ 2 = 4, así que {r('x<sup>8</sup>')} = x<sup>4</sup>.")},
      "p5": {"ok": "b", "hints": {"a": t("Take the root of the number too: √25 = 5.", "También hay que sacar la raíz del número: √25 = 5."), "c": t("√(x<sup>2</sup>) = x, not x<sup>2</sup>.", "√(x<sup>2</sup>) = x, no x<sup>2</sup>."), "d": t("The square root of 25 is 5, not half of 25.", "La raíz de 25 es 5, no la mitad de 25.")},
             "right": t("√25 = 5 and √(x<sup>2</sup>) = x.", "√25 = 5 y √(x<sup>2</sup>) = x."), "solution": t(f"{r(25)} · {r('x<sup>2</sup>')} = 5 · x = 5x.", f"{r(25)} · {r('x<sup>2</sup>')} = 5 · x = 5x.")},
      "p6": {"ok": "c", "hints": {"a": t("18 = 9 · 2, and 9 is a perfect square.", "18 = 9 · 2, y 9 es un cuadrado perfecto."), "b": t("50 = 25 · 2, and 25 is a perfect square.", "50 = 25 · 2, y 25 es un cuadrado perfecto."), "d": t("12 = 4 · 3, and 4 is a perfect square.", "12 = 4 · 3, y 4 es un cuadrado perfecto.")},
             "right": t("7 has no perfect-square factor other than 1.", "7 no tiene ningún factor cuadrado perfecto distinto de 1."), "solution": t(f"{r(7)} is simple. The others have a perfect square inside: 18 = 9 · 2, 50 = 25 · 2, 12 = 4 · 3.", f"{r(7)} es simple. Los demás tienen un cuadrado perfecto dentro: 18 = 9 · 2, 50 = 25 · 2, 12 = 4 · 3.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("Write the root of 25 (5), not 25.", "Escriba la raíz de 25 (5), no el 25."), "c": t("50 = 25 · 2: it has a perfect square.", "50 = 25 · 2: tiene un cuadrado perfecto."), "d": t("√25 = 5, not 10.", "√25 = 5, no 10.")}, "solution": t(f"50 = 25 · 2: {r(5, 2)}.", f"50 = 25 · 2: {r(5, 2)}.")},
      "B": {"ok": "b", "hints": {"a": t("Write the root of 9 (3), not 9.", "Escriba la raíz de 9 (3), no el 9."), "c": t("Swapped: the 3 goes outside and the 2 inside.", "Al revés: el 3 va fuera y el 2 dentro."), "d": t("18 = 9 · 2: it has a perfect square.", "18 = 9 · 2: tiene un cuadrado perfecto.")}, "solution": t(f"18 = 9 · 2: {r(3, 2)}.", f"18 = 9 · 2: {r(3, 2)}.")},
      "C": {"ok": "d", "hints": {"a": t("45 = 9 · 5, not 25 · 3.", "45 = 9 · 5, no 25 · 3."), "b": t("Write the root of 9 (3), not 9.", "Escriba la raíz de 9 (3), no el 9."), "c": t("45 = 9 · 5: it has a perfect square.", "45 = 9 · 5: tiene un cuadrado perfecto.")}, "solution": t(f"45 = 9 · 5: {r(3, 5)}.", f"45 = 9 · 5: {r(3, 5)}.")},
      "D": {"ok": "c", "hints": {"a": t("72 = 36 · 2, and √36 = 6.", "72 = 36 · 2, y √36 = 6."), "b": t("Use the largest perfect square, 36.", "Use el mayor cuadrado perfecto, 36."), "d": t("Write the root of 36 (6), not 36.", "Escriba la raíz de 36 (6), no el 36.")}, "solution": t(f"72 = 36 · 2: {r(6, 2)}.", f"72 = 36 · 2: {r(6, 2)}.")},
      "E": {"ok": "b", "hints": {"a": t("√100 = 10: take the root.", "√100 = 10: saque la raíz."), "c": t("200 = 100 · 2, and √100 = 10.", "200 = 100 · 2, y √100 = 10."), "d": t("Write the root of 100 (10), not 100.", "Escriba la raíz de 100 (10), no el 100.")}, "solution": t(f"200 = 100 · 2: {r(10, 2)}.", f"200 = 100 · 2: {r(10, 2)}.")},
      "F": {"ok": "c", "hints": {"a": t("Half of 6 is 3, not 2.", "La mitad de 6 es 3, no 2."), "b": t("Taking the root halves the exponent.", "Sacar la raíz divide el exponente entre 2."), "d": t("You did not halve it.", "No lo dividió entre 2.")}, "solution": t("6 ÷ 2 = 3: x<sup>3</sup>.", "6 ÷ 2 = 3: x<sup>3</sup>.")},
      "G": {"ok": "b", "hints": {"a": t("12 = 4 · 3: it has a perfect square.", "12 = 4 · 3: tiene un cuadrado perfecto."), "c": t("20 = 4 · 5: it has a perfect square.", "20 = 4 · 5: tiene un cuadrado perfecto."), "d": t("8 = 4 · 2: it has a perfect square.", "8 = 4 · 2: tiene un cuadrado perfecto.")}, "solution": t(f"15 = 3 · 5 has no perfect square: {r(15)} is simple.", f"15 = 3 · 5 no tiene cuadrados perfectos: {r(15)} es simple.")},
      "H": {"ok": "c", "hints": {"a": t("Take the root of the 9 too: 3.", "También se saca la raíz del 9: 3."), "b": t("√(x<sup>2</sup>) = x, not x<sup>2</sup>.", "√(x<sup>2</sup>) = x, no x<sup>2</sup>."), "d": t("You squared the 9 instead of taking its root.", "Elevó el 9 al cuadrado en vez de sacar su raíz.")}, "solution": t("√9 · √(x<sup>2</sup>) = 3x.", "√9 · √(x<sup>2</sup>) = 3x.")}
     }}

    quiz = [
     ("A", t(f"Simplify {r(50)}.", f"Simplifique {r(50)}."), [("a", r(5, 2)), ("b", r(25, 2)), ("c", t(f"{r(50)} is already simple", f"{r(50)} ya es simple")), ("d", r(10, 2))]),
     ("B", t(f"Simplify {r(18)}.", f"Simplifique {r(18)}."), [("a", r(9, 2)), ("b", r(3, 2)), ("c", r(2, 3)), ("d", t(f"{r(18)} is already simple", f"{r(18)} ya es simple"))]),
     ("C", t(f"Simplify {r(45)}.", f"Simplifique {r(45)}."), [("a", r(5, 3)), ("b", r(9, 5)), ("c", t(f"{r(45)} is already simple", f"{r(45)} ya es simple")), ("d", r(3, 5))]),
     ("D", t(f"Simplify {r(72)}.", f"Simplifique {r(72)}."), [("a", r(8, 2)), ("b", r(2, 6)), ("c", r(6, 2)), ("d", r(36, 2))]),
     ("E", t(f"Simplify {r(200)}.", f"Simplifique {r(200)}."), [("a", r(2, 100)), ("b", r(10, 2)), ("c", r(20, 2)), ("d", r(100, 2))]),
     ("F", t(f"Simplify {r('x<sup>6</sup>')}.", f"Simplifique {r('x<sup>6</sup>')}."), [("a", "x<sup>2</sup>"), ("b", "x<sup>6</sup>"), ("c", "x<sup>3</sup>"), ("d", "x<sup>9</sup>")]),
     ("G", t("Which radical is already in its simplest form?", "¿Cuál radical ya está en su forma más simple?"), [("a", r(12)), ("b", r(15)), ("c", r(20)), ("d", r(8))]),
     ("H", t(f"Simplify {r('9x<sup>2</sup>')}.", f"Simplifique {r('9x<sup>2</sup>')}."), [("a", "9x"), ("b", "3x<sup>2</sup>"), ("c", "3x"), ("d", "81x")])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Take the largest perfect square out of the radical and leave inside only what cannot come out.", "Saque del radical el mayor cuadrado perfecto y deje dentro solo lo que no puede salir."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Use</strong> the product property: √(a · b) = √a · √b.", "<strong>Aplicar</strong> la propiedad del producto: √(a · b) = √a · √b."),
         t("<strong>Simplify</strong> number radicals by taking out the largest perfect square.", "<strong>Simplificar</strong> radicales numéricos extrayendo el mayor cuadrado perfecto."),
         t("<strong>Simplify</strong> radicals with variables (x positive).", "<strong>Simplificar</strong> radicales con variables (x positiva)."),
         t("<strong>Tell</strong> when a radical is in its simplest form, and check it on the calculator.", "<strong>Reconocer</strong> cuándo un radical está en su forma más simple y comprobarlo con la calculadora.")],
        secciones,
        (t("Simplify six number radicals by taking out the largest perfect square, two radicals with variables, and decide for two more whether they are already simple, explaining why. Review the perfect squares up to 400 (20<sup>2</sup>): without them in your head, you cannot see the perfect square hiding in the radicand.",
           "Simplifique seis radicales numéricos extrayendo el mayor cuadrado perfecto y dos radicales con variables, y decida para otros dos si ya están simples, explicando por qué. Repase los cuadrados perfectos hasta 400 (20<sup>2</sup>): sin ellos en la cabeza no hay forma de ver el cuadrado perfecto escondido en el radicando."),
         t("A square patio has an area of 72 square feet. Its side is √72 feet. Write it in simplest form and find it as a decimal on the calculator. Then measure a square floor tile at home and find its side from its area.",
           "Un patio cuadrado tiene un área de 72 pies cuadrados. Su lado mide √72 pies. Escríbalo en su forma más simple y calcúlelo como decimal en la calculadora. Después mida una baldosa cuadrada de su casa y halle su lado a partir del área.")),
        quiz,
        t("Self-check checklist for simplifying radicals", "Lista de autoevaluación para simplificar radicales"),
        t("Self-check checklist: skills for simplifying radicals with perfect-square factors", "Lista de autoevaluación: destrezas para simplificar radicales con cuadrados perfectos"),
        [(t("Factoring the radicand", "Factorizar el radicando"), t("I find the largest perfect square that divides it and can say why I chose it.", "Encuentro el mayor cuadrado perfecto que lo divide y sé decir por qué lo elegí."), t("I use a perfect square, but not the largest.", "Uso un cuadrado perfecto, pero no el mayor."), t("I do not see the perfect squares in the radicand.", "No veo los cuadrados perfectos en el radicando.")),
         (t("The product property", "La propiedad del producto"), t("I use √(a · b) = √a · √b correctly, also with variables.", "Aplico √(a · b) = √a · √b correctamente, también con variables."), t("I split the root, with some mistakes.", "Separo la raíz, con algunos errores."), t("I do not split the root of the product.", "No separo la raíz del producto.")),
         (t("The simplest form", "La forma más simple"), t("I give the simplest form and check it on the calculator.", "Doy la forma más simple y la compruebo con la calculadora."), t("I take the root, but I do not put the coefficient outside.", "Saco la raíz, pero no pongo el coeficiente fuera."), t("I leave the answer only partly simplified.", "Dejo el resultado simplificado a medias."))],
        t("<p>You learned to simplify radicals: find the <strong>largest perfect square</strong> that divides the radicand, split it off with the product property, and take its root. With variables, an even exponent comes out at half its value.</p>\n<p>In <strong>Lesson 3.2 · Adding, subtracting, and multiplying radicals</strong> you will add and subtract like radicals, simplifying first, and multiply radicals, including with the distributive property.</p>",
          "<p>Aprendió a simplificar radicales: se busca el <strong>mayor cuadrado perfecto</strong> que divide al radicando, se separa con la propiedad del producto y se extrae su raíz. Con variables, un exponente par sale a la mitad.</p>\n<p>En la <strong>Lección 3.2 · Operaciones con radicales: suma, resta y multiplicación</strong> sumará y restará radicales semejantes, simplificando primero, y multiplicará radicales, también con la propiedad distributiva.</p>"),
        ("3-2", ("", t("Lesson 3.2 · Adding, subtracting, and multiplying radicals", "Lección 3.2 · Operaciones con radicales: suma, resta y multiplicación"))),
        [(t("radical", "radical"), t("An expression with the root sign √, like √50.", "Una expresión con el signo de raíz √, como √50.")),
         (t("radicand", "radicando"), t("The number or expression inside the radical sign. In √50, the radicand is 50.", "El número o la expresión que está dentro del signo radical. En √50, el radicando es 50.")),
         (t("perfect square", "cuadrado perfecto"), t("A number that is a whole number times itself: 1, 4, 9, 16, 25…", "Un número que es un entero por sí mismo: 1, 4, 9, 16, 25…")),
         (t("simplest form", "forma más simple"), t("A radical whose radicand has no perfect-square factor other than 1, like 5√2.", "Un radical cuyo radicando no tiene ningún factor cuadrado perfecto distinto de 1, como 5√2."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ============ MODULE 1 · splitting the radical ============ */
var PR_COLA = [48, 200, 180, 50, 15];
function pintaPR(){
  var x = $("pr-n").value.trim(), n = /^\d+$/.test(x) ? parseInt(x, 10) : NaN, sal = $("pr-salida"), ops = $("pr-opciones");
  ops.innerHTML = "";
  if (!(n >= 2 && n <= 400)){ $("pr-tabla").innerHTML = ""; $("pr-tabla-voz").textContent = ""; sal.innerHTML = T("Type a whole number from 2 to 400.", "Escriba un número entero de 2 a 400."); return; }
  var divs = cuadradosQueDividen(n), mayor = divs.length ? divs[divs.length - 1] : 0, h = "";
  for (var s = 2; s * s <= 400; s++) h += '<div class="cuadro' + (n % (s * s) === 0 ? (s === mayor ? " mayor" : " divide") : "") + '">' + s + "²<strong>" + (s * s) + "</strong></div>";
  $("pr-tabla").innerHTML = h;
  $("pr-tabla-voz").textContent = divs.length ? T("Perfect squares that divide " + n + ": " + yLista(divs.map(function(s){ return s * s; })) + ". The largest is " + (mayor * mayor) + ".", "Cuadrados perfectos que dividen a " + n + ": " + yLista(divs.map(function(s){ return s * s; })) + ". El mayor es " + (mayor * mayor) + ".") : T("No perfect square greater than 1 divides " + n + ".", "Ningún cuadrado perfecto mayor que 1 divide a " + n + ".");
  if (!divs.length){ sal.innerHTML = '<div class="linea veredicto">' + T(n + " has no perfect-square factors (other than 1), so " + radHTML(1, n) + " is already in simplest form.", n + " no tiene factores que sean cuadrados perfectos (salvo el 1), así que " + radHTML(1, n) + " ya está en su forma más simple.") + "</div>"; return; }
  divs.forEach(function(s){
    var b = document.createElement("button"); b.type = "button"; b.className = "eleccion"; b.textContent = T("With ", "Con ") + (s * s); b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function(){ Array.prototype.forEach.call(ops.children, function(z){ z.setAttribute("aria-pressed", z === b ? "true" : "false"); }); partePR(n, s, mayor); });
    ops.appendChild(b);
  });
  sal.innerHTML = T("Choose one of the perfect squares above to split ", "Elija arriba uno de los cuadrados perfectos para partir ") + radHTML(1, n) + ".";
}
function partePR(n, s, mayor){
  var b = n / (s * s), h = '<div class="linea grande">' + radHTML(1, n) + " = √(" + (s * s) + " · " + b + ") = " + radHTML(1, s * s) + " · " + radHTML(1, b) + " = " + radHTML(s, b) + "</div>";
  if (b === 1) h += '<div class="linea veredicto">✓ ' + T(n + " is a perfect square: ", n + " es un cuadrado perfecto: ") + radHTML(1, n) + " = " + s + ".</div>";
  else if (s === mayor) h += '<div class="linea veredicto">✓ ' + T("Simplest form: you used the largest perfect square, and " + b + " is left inside, which has no perfect squares.", "Forma más simple: usó el mayor cuadrado perfecto y dentro queda " + b + ", que ya no tiene cuadrados perfectos.") + "</div>";
  else { var q = simplRad(b);
    h += '<div class="linea veredicto">' + T("Not finished yet: ", "Todavía no está terminado: ") + radHTML(1, b) + T(" can be simplified, because " + b + " contains the square " + (q.k * q.k) + ".", " se puede simplificar, porque " + b + " contiene el cuadrado " + (q.k * q.k) + ".") + "</div>" +
         '<div class="linea">' + T("If you keep going: ", "Si sigue: ") + radHTML(s, b) + " = " + s + " · " + radHTML(q.k, q.r) + " = " + radHTML(s * q.k, q.r) + T(". With " + (mayor * mayor) + " you would have gotten there in one step.", ". Con el " + (mayor * mayor) + " habría llegado en un solo paso.") + "</div>"; }
  $("pr-salida").innerHTML = h;
}
function genMayor(){
  var n, divs;
  do { n = radicandoAzar(300); divs = cuadradosQueDividen(n); } while (!divs.length);
  var mayor = divs[divs.length - 1], o = [{html: String(mayor * mayor), clave: "c" + mayor * mayor}], pc = {};
  divs.slice(0, -1).forEach(function(s){ o.push({html: String(s * s), clave: "c" + s * s}); pc["c" + s * s] = T((s * s) + " does divide " + n + ", but it is not the largest: something would still be left to simplify.", (s * s) + " sí divide a " + n + ", pero no es el mayor: con él todavía quedaría algo por simplificar."); });
  for (var s = 2; s <= 12 && o.length < 7; s++) if (n % (s * s) !== 0 && s * s < 2 * n){ o.push({html: String(s * s), clave: "c" + s * s}); pc["c" + s * s] = T((s * s) + " does not divide " + n + ": " + n + " ÷ " + (s * s) + " is not a whole number.", (s * s) + " no divide a " + n + ": " + n + " ÷ " + (s * s) + " no da un número entero."); }
  return {enun: T("What is the largest perfect square that divides " + n + "?", "¿Cuál es el mayor cuadrado perfecto que divide a " + n + "?"), opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: n + " = " + (mayor * mayor) + " · " + (n / (mayor * mayor)) + T(", so ", ", así que ") + radHTML(1, n) + " = " + radHTML(mayor, n / (mayor * mayor)) + ".",
    mal: T("The largest is ", "El mayor es ") + (mayor * mayor) + ": " + n + " = " + (mayor * mayor) + " · " + (n / (mayor * mayor)) + "."};
}

/* ============ MODULE 2 · step-by-step simplifier ============ */
var NS = {lista: [50, 48, 72, 8, 75, 98, 200, 180, 36, 15], pasos: [], visto: 0};
function llenaNS(){ var sel = $("ns-sel"); sel.innerHTML = ""; NS.lista.forEach(function(n){ var o = document.createElement("option"); o.value = n; o.textContent = "√" + n; sel.appendChild(o); }); }
function preparaNS(){
  var n = parseInt($("ns-sel").value, 10), q = simplRad(n); NS.pasos = []; NS.visto = 0;
  $("ns-expr").innerHTML = '<span class="grande">' + radHTML(1, n) + "</span>";
  if (q.k === 1){ NS.pasos.push(T("Look for perfect squares that divide " + n + " (4, 9, 16, 25, …). None does.", "Se buscan cuadrados perfectos que dividan a " + n + " (4, 9, 16, 25, …). Ninguno lo divide.")); NS.pasos.push('<span class="veredicto">' + radHTML(1, n) + T(" is already in simplest form.", " ya está en su forma más simple.") + "</span>"); }
  else if (q.r === 1){ NS.pasos.push(T(n + " is a perfect square: ", n + " es un cuadrado perfecto: ") + q.k + " × " + q.k + " = " + n + "."); NS.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + radHTML(1, n) + " = " + q.k + ".</span>"); }
  else {
    NS.pasos.push(T("The largest perfect square that divides " + n + " is " + (q.k * q.k) + ": ", "El mayor cuadrado perfecto que divide a " + n + " es " + (q.k * q.k) + ": ") + n + " = " + (q.k * q.k) + " · " + q.r + ".");
    NS.pasos.push(T("Split it with the product property: ", "Se separa con la propiedad del producto: ") + radHTML(1, n) + " = " + radHTML(1, q.k * q.k) + " · " + radHTML(1, q.r) + ".");
    NS.pasos.push(T("Take the root of the perfect square: ", "Se extrae la raíz del cuadrado perfecto: ") + radHTML(1, q.k * q.k) + " = " + q.k + ".");
    NS.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + radHTML(1, n) + " = " + radHTML(q.k, q.r) + ".</span>");
  }
  pintaNS();
}
function pintaNS(){
  $("ns-pasos").innerHTML = NS.pasos.slice(0, NS.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === NS.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("ns-sig"); b.disabled = NS.visto >= NS.pasos.length; $("ns-todo").disabled = b.disabled;
  b.textContent = NS.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function genSimpl(){
  var n = radicandoAzar(300), q = simplRad(n), o = [opRad(q.k, q.r)], pc = {};
  var a = opRad(q.k * q.k, q.r); o.push(a); pc[a.clave] = T("When you take out the perfect square, write its root (" + q.k + "), not the square (" + (q.k * q.k) + ").", "Al sacar el cuadrado perfecto se escribe su raíz (" + q.k + "), no el cuadrado (" + (q.k * q.k) + ").");
  if (q.r !== q.k){ var b = opRad(q.r, q.k); o.push(b); pc[b.clave] = T("The number outside and the number inside were swapped.", "Se intercambiaron el número de fuera y el de dentro."); }
  cuadradosQueDividen(n).slice(0, -1).forEach(function(s){ var c = opRad(s, n / (s * s)); o.push(c); pc[c.clave] = T("It has the same value, but it can still be simplified: " + (n / (s * s)) + " contains a perfect square.", "Tiene el mismo valor, pero todavía se puede simplificar: " + (n / (s * s)) + " contiene un cuadrado perfecto."); });
  o.push({html: radHTML(1, n) + T(" is already in simplest form", " ya está en su forma más simple"), clave: "simple"}); pc.simple = T(n + " does have a perfect-square factor: " + (q.k * q.k) + ".", n + " sí tiene un factor que es cuadrado perfecto: " + (q.k * q.k) + ".");
  o.push(opRad(q.k + 1, q.r));
  return {enun: T("Simplify ", "Simplifique ") + radHTML(1, n) + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: n + " = " + (q.k * q.k) + " · " + q.r + T(", and ", ", y ") + radHTML(1, q.k * q.k) + " = " + q.k + ".",
    mal: T("The answer is ", "La respuesta es ") + radHTML(q.k, q.r) + T(", because ", ", porque ") + n + " = " + (q.k * q.k) + " · " + q.r + "."};
}
function genEscribe(){
  var u = Math.random(), n;
  if (u < 0.1) n = elige(LIBRES.concat([17, 19, 21, 22, 23, 26, 30, 33, 35]));
  else if (u < 0.2){ var s = aleatorio(4, 15); n = s * s; }
  else n = radicandoAzar(300);
  var q = simplRad(n);
  return {enun: T("Simplify ", "Simplifique ") + radHTML(1, n) + ".", k: q.k, r: q.r,
    explica: q.k === 1 ? T(n + " has no perfect-square factors, so it is already simple.", n + " no tiene factores que sean cuadrados perfectos, así que ya está simple.") : (q.r === 1 ? T(n + " is a perfect square.", n + " es un cuadrado perfecto.") : n + " = " + (q.k * q.k) + " · " + q.r + ".")};
}

/* ============ MODULE 3 · radicals with variables (x positive) ============ */
function xVis(e){ return e === 0 ? "" : (e === 1 ? "x" : "x" + supH(e)); }
function xVoz(e){ return e === 0 ? "" : (e === 1 ? "x" : T("x to the power of ", "x a la ") + e); }
function varVis(k, e, r, xin){ var hay = r > 1 || xin, out = ""; if (k !== 1 || (e === 0 && !hay)) out += k; out += xVis(e); if (hay) out += '<span class="rad">√<span class="rc">' + (r > 1 ? r : "") + (xin ? "x" : "") + "</span></span>"; return out; }
function varVoz(k, e, r, xin){ var hay = r > 1 || xin, p = []; if (k !== 1 || (e === 0 && !hay)) p.push(String(k)); if (e) p.push(xVoz(e)); if (hay) p.push(RAIZ + (r > 1 ? r + (xin ? " x" : "") : "x")); return p.join(T(" times ", " por ")); }
function varHTML(k, e, r, xin){ return envuelve(varVis(k, e, r, xin), varVoz(k, e, r, xin)); }
function opVar(k, e, r, xin){ return {html: varHTML(k, e, r, xin), clave: [k, e, r, xin ? 1 : 0].join("|")}; }
function entradaHTML(a, n){ return envuelve('<span class="rad">√<span class="rc">' + (a > 1 ? a : "") + xVis(n) + "</span></span>", RAIZ + (a > 1 ? a + " " : "") + xVoz(n)); }
function resuelveVar(a, n){ var s = simplRad(a); return {k: s.k, e: Math.floor(n / 2), r: s.r, xin: n % 2 === 1}; }
function pintaVA(){
  var a = parseInt($("va-a").value, 10), x = $("va-n").value.trim(), n = /^\d+$/.test(x) ? parseInt(x, 10) : NaN, av = $("va-aviso");
  if (!(n >= 1 && n <= 12)){ av.className = "caja-aviso visible"; av.textContent = T("Type a whole-number exponent from 1 to 12.", "Escriba un exponente entero de 1 a 12."); $("va-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var R = resuelveVar(a, n), s = simplRad(a), h = '<div class="linea grande">' + entradaHTML(a, n) + " = " + varHTML(R.k, R.e, R.r, R.xin) + "</div>";
  if (a > 1){
    h += '<div class="linea">' + T("Split the product: ", "Se separa el producto: ") + entradaHTML(a, n) + " = " + radHTML(1, a) + " · " + entradaHTML(1, n) + ".</div>";
    h += '<div class="linea">' + T("The number: ", "El número: ") + (s.r === 1 ? radHTML(1, a) + " = " + s.k + T(", because " + a + " is a perfect square.", ", porque " + a + " es un cuadrado perfecto.") : (s.k === 1 ? radHTML(1, a) + T(" does not simplify and stays inside.", " no se simplifica y se queda dentro.") : radHTML(1, a) + " = " + radHTML(s.k, s.r) + ".")) + "</div>";
  }
  if (n % 2 === 0) h += '<div class="linea">' + T("The variable: " + n + " is even, so x" + supH(n) + " is a perfect square and its root is x" + supH(n / 2) + " (half the exponent).", "La variable: " + n + " es par, así que x" + supH(n) + " es un cuadrado perfecto y su raíz es x" + supH(n / 2) + " (la mitad del exponente).") + "</div>";
  else if (n === 1) h += '<div class="linea">' + T("The variable: the exponent 1 is odd and there is no even part to take out, so x stays inside the radical.", "La variable: el exponente 1 es impar y no hay parte par que sacar, así que x se queda dentro del radical.") + "</div>";
  else h += '<div class="linea">' + T("The variable: " + n + " is odd. Split x" + supH(n) + " = x" + supH(n - 1) + " · x. The even part comes out as " + xVis((n - 1) / 2) + ", and the extra x stays inside.", "La variable: " + n + " es impar. Se separa x" + supH(n) + " = x" + supH(n - 1) + " · x. La parte par sale como " + xVis((n - 1) / 2) + " y la x sobrante se queda dentro.") + "</div>";
  $("va-salida").innerHTML = h;
}
var COEF_VAR = [1, 4, 9, 16, 25, 36, 49, 2, 3, 5, 8, 12, 18, 20, 27, 50];
function genVariables(){
  if (Math.random() < 0.3){
    var buenos = [[1, 0, 7, false], [1, 0, 1, true], [1, 0, 15, true], [2, 1, 5, false], [3, 2, 1, true], [1, 0, 6, false], [5, 3, 2, true]];
    var malos = [["√18", RAIZ + "18"], ["√x" + supH(4), RAIZ + "x" + T(" to the power of 4", " a la 4")], ["√(12x)", RAIZ + "12 x"], ["√50", RAIZ + "50"], ["√(9x" + supH(3) + ")", RAIZ + "9 x" + T(" to the power of 3", " a la 3")], ["√(20x)", RAIZ + "20 x"], ["x√x" + supH(2), "x" + T(" times ", " por ") + RAIZ + "x" + T(" squared", " al cuadrado")]];
    var b = elige(buenos), o = [{html: varHTML(b[0], b[1], b[2], b[3]), clave: "s"}], pc = {};
    baraja(malos).slice(0, 3).forEach(function(m, i){ o.push({html: envuelve(m[0], m[1]), clave: "m" + i}); pc["m" + i] = T("Inside this one there is still a perfect square or an exponent of 2 or more.", "Dentro de esta todavía queda un cuadrado perfecto o un exponente de 2 o más."); });
    return {enun: T("Which of these expressions is already in simplest form?", "¿Cuál de estas expresiones ya está en su forma más simple?"), opciones: o, correcta: "s", porClave: pc,
      bien: T("No perfect square is left inside the radical: no numbers like 4 or 9, and no exponents of 2 or more.", "Dentro del radical no queda ningún cuadrado perfecto: ni números como 4 o 9, ni exponentes de 2 o más."),
      mal: T("The only simple one is ", "La única simple es ") + varHTML(b[0], b[1], b[2], b[3]) + T(". In the others, a perfect square or an exponent of 2 or more is still inside.", ". En las demás queda dentro un cuadrado perfecto o un exponente de 2 o más.")};
  }
  var a = elige(COEF_VAR), n = aleatorio(2, 12), R = resuelveVar(a, n), o2 = [opVar(R.k, R.e, R.r, R.xin)], pc2 = {};
  var c1 = opVar(R.k, n, R.r, false); o2.push(c1); pc2[c1.clave] = T("Taking the root halves the exponent of x.", "El exponente de x se divide entre 2 al sacar la raíz.");
  if (n >= 5){ var c2 = opVar(R.k, n - 2, R.r, R.xin); o2.push(c2); pc2[c2.clave] = T("Taking the root halves the exponent; it does not subtract 2.", "Al sacar la raíz, el exponente se divide entre 2; no se le resta 2."); }
  if (esCuadrado(a) && a > 1){ var c3 = opVar(a, R.e, 1, R.xin); o2.push(c3); pc2[c3.clave] = T("Take the root of the number too: ", "También hay que sacar la raíz del número: ") + radHTML(1, a) + " = " + R.k + "."; }
  if (R.xin){ var c4 = opVar(R.k, R.e + 1, R.r, false); o2.push(c4); pc2[c4.clave] = T("With an odd exponent, one x stays inside the radical: it cannot all come out.", "Con exponente impar, una x se queda dentro del radical: no se puede sacar entera."); }
  else if (R.r > 1){ var c5 = opVar(R.k, R.e, R.r, true); o2.push(c5); pc2[c5.clave] = T("The exponent is even: the x comes out whole and leaves nothing inside.", "El exponente es par: la x sale completa y no deja nada dentro."); }
  o2.push(opVar(R.k, R.e + 1, R.r, R.xin));
  var sa = simplRad(a);
  return {enun: T("Simplify ", "Simplifique ") + entradaHTML(a, n) + ".", opciones: [o2[0]].concat(baraja(o2.slice(1)).slice(0, 3)), correcta: o2[0].clave, porClave: pc2,
    bien: (n % 2 === 0 ? T("The exponent " + n + " is even: x" + supH(n) + " comes out as " + xVis(n / 2) + ".", "El exponente " + n + " es par: x" + supH(n) + " sale como " + xVis(n / 2) + ".") : T("The exponent " + n + " is odd: " + xVis((n - 1) / 2) + " comes out and one x stays inside.", "El exponente " + n + " es impar: sale " + xVis((n - 1) / 2) + " y una x se queda dentro.")) + (a > 1 ? T(" And ", " Y ") + radHTML(1, a) + " = " + radHTML(sa.k, sa.r) + "." : ""),
    mal: T("The answer is ", "La respuesta es ") + varHTML(R.k, R.e, R.r, R.xin) + "."};
}

/* ============ MODULE 4 · checking ============ */
var P5 = null;
function genVerificar(){
  var n = radicandoAzar(300), q = simplRad(n), u = Math.random(), k, rr, tipo, parc = cuadradosQueDividen(n).slice(0, -1);
  if (u < 0.35){ k = q.k; rr = q.r; tipo = "s"; }
  else if (u < 0.6 && parc.length){ var s = elige(parc); k = s; rr = n / (s * s); tipo = "t"; }
  else { var f = [[q.k * q.k, q.r], [q.k + 1, q.r], [q.k, q.r + 1]]; if (q.r !== q.k) f.push([q.r, q.k]); var g = elige(f); k = g[0]; rr = g[1]; tipo = "m"; }
  var expl = tipo === "s" ? T("The decimals match and no perfect square is left inside the radical.", "Los decimales coinciden y dentro del radical ya no queda ningún cuadrado perfecto.")
           : (tipo === "t" ? T("The decimals match, but " + rr + " still contains a perfect square: the final form is ", "Los decimales coinciden, pero " + rr + " todavía contiene un cuadrado perfecto: la forma final es ") + radHTML(q.k, q.r) + "."
                           : T("The decimals do not match. The right simplification is ", "Los decimales no coinciden. La simplificación correcta es ") + radHTML(q.k, q.r) + ".");
  P5 = {n: n, k: k, rr: rr};
  if ($("p5-dec")){ $("p5-dec").style.display = "none"; $("p5-dec").innerHTML = ""; }
  return {enun: T("Someone wrote: ", "Alguien escribió: ") + radHTML(1, n) + " = " + radHTML(k, rr) + T(". What do you think?", ". ¿Qué opina?"), enOrden: true,
    opciones: [{html: T("Right, and in simplest form", "Correcta y en su forma más simple"), clave: "s"}, {html: T("Same value, but it can still be simplified", "Tiene el mismo valor, pero todavía se puede simplificar"), clave: "t"}, {html: T("Wrong: the values do not match", "Incorrecta: los valores no coinciden"), clave: "m"}],
    correcta: tipo, porClave: {}, pista: T("Work out the two decimals, then look inside the radical for a perfect square.", "Calcule los dos decimales y después busque un cuadrado perfecto dentro del radical."), bien: expl, mal: expl};
}
function muestraDecimales(){
  if (!P5) return; var d = $("p5-dec"); d.style.display = "block";
  d.innerHTML = '<div class="linea">' + radHTML(1, P5.n) + " ≈ " + aprox(Math.sqrt(P5.n), 3) + '</div><div class="linea">' + radHTML(P5.k, P5.rr) + " = " + P5.k + " × " + radHTML(1, P5.rr) + " ≈ " + aprox(P5.k * Math.sqrt(P5.rr), 3) + "</div>";
}

/* ============ Start ============ */
$("pr-n").addEventListener("input", pintaPR);
$("pr-azar").addEventListener("click", function(){ $("pr-n").value = PR_COLA.length ? PR_COLA.shift() : radicandoAzar(400); pintaPR(); });
pintaPR();
OMR("p1", genMayor);
llenaNS();
$("ns-sel").addEventListener("change", preparaNS);
$("ns-sig").addEventListener("click", function(){ if (NS.visto < NS.pasos.length){ NS.visto++; pintaNS(); } });
$("ns-todo").addEventListener("click", function(){ NS.visto = NS.pasos.length; pintaNS(); });
$("ns-azar").addEventListener("click", function(){ var n = radicandoAzar(300); if (NS.lista.indexOf(n) < 0){ NS.lista.push(n); llenaNS(); } $("ns-sel").value = n; preparaNS(); });
preparaNS();
OMR("p2", genSimpl);
creaPracticaRad("p3", genEscribe);
$("va-a").addEventListener("change", pintaVA);
$("va-n").addEventListener("input", pintaVA);
pintaVA();
OMR("p4", genVariables);
OMR("p5", genVerificar);
$("p5-calc").addEventListener("click", muestraDecimales);
$("p5-opciones").addEventListener("click", function(ev){ if (ev.target.closest(".opcion")) muestraDecimales(); });
'''

def rad_input(pid, titulo):
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos campos-sci">
          <div class="campo"><label for="{pid}-k">{t("Coefficient", "Coeficiente")}</label><input type="text" inputmode="numeric" autocomplete="off" class="corto" id="{pid}-k"></div>
          <div class="campo" aria-hidden="true" style="font-size:24px;font-weight:700;padding-bottom:6px;">√</div>
          <div class="campo"><label for="{pid}-r">{t("Radicand", "Radicando")}</label><input type="text" inputmode="numeric" autocomplete="off" class="corto" id="{pid}-r"></div>
        </div>
        <p class="nota">{t("For example, for 6√2 type 6 and 2. If there is no coefficient left (as in √15), leave the first box blank. If no radical is left (as in √36 = 6), type 1 as the radicand.", "Por ejemplo, para 6√2 escriba 6 y 2. Si no queda coeficiente (como en √15), deje vacío el primer campo. Si no queda radical (como en √36 = 6), escriba 1 como radicando.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("product", "producto"), t("The product property of radicals", "La propiedad del producto de radicales"),
      f'''      <p>{t("The root of a product can be split into the product of the roots. That lets you “take out” of the radical any factor that is a perfect square and leave inside only what is not.", "La raíz de un producto se puede separar en el producto de las raíces. Eso permite «sacar» del radical cualquier factor que sea un cuadrado perfecto y dejar dentro solo lo que no lo es.")}</p>
{P.formula("√(a · b) = √a · √b")}
      <h3>{t("Split the radical", "Partir el radical")}</h3>
      <p>{t("Type a number. The table marks the perfect squares that divide it, and the darkest one is the largest. Try splitting the radical with each one and compare what is left inside.", "Escriba un número. La tabla marca los cuadrados perfectos que lo dividen, y el más oscuro es el mayor. Pruebe a partir el radical con cada uno y compare lo que queda dentro.")}</p>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="pr-n">{t("Number inside the radical (2 to 400)", "Número dentro del radical (de 2 a 400)")}</label><input type="text" inputmode="numeric" class="corto" id="pr-n" value="72"></div></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="pr-azar">{t("Another number", "Otro número")}</button></div>
        <div class="cuadros" id="pr-tabla" aria-hidden="true"></div>
        <p class="sr-only" id="pr-tabla-voz" aria-live="polite"></p>
        <p><strong>{t("Split with the perfect square…", "Partir con el cuadrado perfecto…")}</strong></p>
        <div class="elecciones" id="pr-opciones"></div>
      </div>
{P.salida("pr-salida")}
{P.atencion(t("Look for the largest:", "Busque el mayor:"), t("if you use a small perfect square, something is still left to simplify. √72 = √(4 · 18) = 2√18, but √18 can still be reduced. With the largest, 36, you get there at once: √72 = 6√2.", "si se usa un cuadrado perfecto pequeño, todavía queda algo por simplificar. √72 = √(4 · 18) = 2√18, pero √18 aún se reduce. Con el mayor, 36, se llega de una vez: √72 = 6√2."))}
{B.om("p1", t("Practice: what is the largest perfect square that divides it?", "Practique: ¿cuál es el mayor cuadrado perfecto que lo divide?"))}'''),
     (t("numbers", "numericos"), t("Simplifying number radicals", "Simplificar radicales numéricos"),
      f'''      <p>{t("The procedure has three steps: find the largest perfect square that divides the radicand, split it off with the product property, and take its root.", "El procedimiento tiene tres pasos: buscar el mayor cuadrado perfecto que divide al radicando, separarlo con la propiedad del producto y extraer su raíz.")}</p>
      <h3>{t("Step-by-step simplifier", "Simplificador paso a paso")}</h3>
      <p>{t("Choose a radical and reveal one step at a time. Try to predict each step before you show it.", "Elija un radical y revele un paso a la vez. Intente anticipar cada paso antes de mostrarlo.")}</p>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="ns-sel">{t("Radical to simplify", "Radical que se va a simplificar")}</label><select id="ns-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="ns-sig"></button><button type="button" class="btn-sec" id="ns-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="ns-azar">{t("Another one at random", "Otro al azar")}</button></div>
      </div>
      <div class="fraccion-grande" id="ns-expr"></div>
      <div class="pasos" id="ns-pasos" aria-live="polite"></div>
      <div class="caja-tip"><strong>{t("When is it simple?", "¿Cuándo está simple?")}</strong> {t("When the radicand has no factor, other than 1, that is a perfect square. √15 is already simple, because 15 = 3 · 5 and neither 3 nor 5 is a perfect square.", "Cuando el radicando no tiene ningún factor, distinto de 1, que sea un cuadrado perfecto. √15 ya es simple, porque 15 = 3 · 5 y ni 3 ni 5 son cuadrados perfectos.")}</div>
{B.om("p2", t("Practice: choose the simplified form", "Practique: elija la forma simplificada"))}
{rad_input("p3", t("Write it yourself: simplify the radical", "Escríbalo usted: simplifique el radical"))}'''),
     (t("variables", "variables"), t("Radicals with variables", "Radicales con variables"),
      f'''      <p>{t("A variable with an <strong>even</strong> exponent is a perfect square: its root is the same variable with half the exponent, because (x<sup>3</sup>)<sup>2</sup> = x<sup>6</sup>. If the exponent is <strong>odd</strong>, split off one x: the even part comes out and the extra x stays inside.", "Una variable con exponente <strong>par</strong> es un cuadrado perfecto: su raíz es la misma variable con la mitad del exponente, porque (x<sup>3</sup>)<sup>2</sup> = x<sup>6</sup>. Si el exponente es <strong>impar</strong>, se separa una x: la parte par sale y la x sobrante se queda dentro.")}</p>
      <p class="nota">{t("In this whole module, x is positive, as in the problems on the test.", "En todo este módulo se supone que x es positiva, como en los problemas del examen.")}</p>
      <h3>{t("Exponent explorer", "Explorador de exponentes")}</h3>
{P.panel(P.lista("va-a", t("Number inside the radical", "Número dentro del radical"), [(v, str(v)) for v in (1, 4, 9, 16, 25, 2, 3, 12, 18, 50)], 9), '<div class="campo"><label for="va-n">' + t("Exponent of x (1 to 12)", "Exponente de x (de 1 a 12)") + '</label><input type="text" inputmode="numeric" class="corto" id="va-n" value="2"></div>')}
{P.aviso("va-aviso")}
{P.salida("va-salida")}
{B.om("p4", t("Practice: radicals with variables", "Practique: radicales con variables"))}'''),
     (t("check", "verificar"), t("Checking the answer", "Verificar el resultado"),
      f'''      <p>{t("Simplifying does not change the value of the radical, only its form. So a reliable check is to work out both expressions on the calculator: they must give the same decimal. For example, √72 ≈ 8.485 and 6 × √2 ≈ 8.485.", "Simplificar no cambia el valor del radical, solo su forma. Por eso una comprobación confiable es calcular las dos expresiones con la calculadora: deben dar el mismo decimal. Por ejemplo, √72 ≈ 8.485 y 6 × √2 ≈ 8.485.")}</p>
      <p>{t("But careful: matching decimals are not enough for the answer to be <strong>finished</strong>. 2√18 has the same value as √72, and it can still be simplified.", "Pero ojo: que los decimales coincidan no basta para que la respuesta esté <strong>terminada</strong>. 2√18 vale lo mismo que √72 y, aun así, todavía se puede simplificar.")}</p>
      <h3>{t("Practice: is this simplification right?", "Practique: ¿es correcta esta simplificación?")}</h3>
      <div class="fila-btn" style="margin:0 0 10px;"><button type="button" class="btn-sec" id="p5-calc">{t("Work out both decimals", "Calcular los dos decimales")}</button></div>
      <div class="salida" id="p5-dec" aria-live="polite" style="display:none;"></div>
{B.om("p5", "").replace("<h3></h3>", "")}
      <div class="caja-tip"><strong>{t("Using the calculator:", "Uso de la calculadora:")}</strong> {t("checking does not replace the procedure, but it confirms that the simplification keeps the value. It is a great tool for catching a factoring mistake.", "verificar no reemplaza el procedimiento, pero confirma que la simplificación conserva el valor. Es una herramienta excelente para detectar un error de factorización.")}</div>''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_RAD, scripts=("/math/radicals.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Simplificar radicales: factorización en cuadrados perfectos")
