"""Level 3 · Lesson 1.1 · The product rule, power of a power, and power of a product — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "1-1"
TEMA = ("Rules of exponents", "Reglas de los exponentes")
TIT = ("The product rule, power of a power, and power of a product", "Regla del producto, potencia de potencia y potencia de un producto")

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("In Level 2 you met the exponent as a short way to write repeated multiplication: 2<sup>4</sup> means 2 · 2 · 2 · 2. That idea is the starting point of Level 3. In this topic, instead of writing out every power by hand, you will learn <strong>rules</strong> that let you work with exponents directly. This first lesson sets out the three rules for multiplying; the next one adds division, the zero exponent, and negative exponents.",
"En el Nivel 2 conoció el exponente como una manera corta de escribir una multiplicación repetida: 2<sup>4</sup> significa 2 · 2 · 2 · 2. Esa idea es el punto de partida del Nivel 3. En este tema, en lugar de desarrollar cada potencia a mano, aprenderá <strong>reglas</strong> que permiten operar con los exponentes de manera directa. Esta primera lección presenta las tres reglas de la multiplicación; la siguiente añade la división, el exponente cero y los exponentes negativos.")}</p>
<p>{t("A power has two parts. In a<sup>n</sup>, the number a is the <strong>base</strong> (the factor that repeats) and n is the <strong>exponent</strong> (how many times the factor repeats).",
"Una potencia tiene dos partes. En a<sup>n</sup>, el número a es la <strong>base</strong> (el factor que se repite) y n es el <strong>exponente</strong> (cuántas veces se repite el factor).")}</p>
{big(t("a<sup>n</sup> = a · a · a · … · a  (n factors)", "a<sup>n</sup> = a · a · a · … · a  (n factores)"))}
<p>{t("So a<sup>5</sup> = a · a · a · a · a. Every rule in this lesson comes from this definition and from counting factors.", "Así, a<sup>5</sup> = a · a · a · a · a. Toda regla de esta lección sale de esta definición y de contar factores.")}</p>
{caja("tip", t("The key idea", "La idea central"), t("<p>The exponent <strong>counts factors</strong>. If you count correctly how many times the base appears as a factor, you always get the right exponent, even if you do not remember the rule.</p>",
"<p>El exponente <strong>cuenta factores</strong>. Si cuenta bien cuántas veces aparece la base como factor, siempre llega al exponente correcto, aunque no recuerde la regla.</p>"))}
{caja("ojo", t("Parentheses decide the base", "El paréntesis decide la base"), t("<p>In (−3)<sup>4</sup> the base is −3, so the sign is multiplied four times and the answer is positive: 81. In −3<sup>4</sup> the base is only the 3; the minus sign stays outside, and the answer is −81.</p>",
"<p>En (−3)<sup>4</sup> la base es −3: el signo se multiplica cuatro veces y el resultado es positivo, 81. En −3<sup>4</sup> la base es solo el 3; el signo menos queda fuera y el resultado es −81.</p>"))}
{enlace(n, t("notation", "notacion"), t("exponential notation", "la notación exponencial"), t("Find the base and the exponent, and write repeated products as powers.", "Identifique la base y el exponente, y escriba productos repetidos como potencias."))}'''

    s2 = f'''<p>{t("When you multiply two powers <strong>with the same base</strong>, the factors simply pile up. Write them out to see the rule:", "Cuando se multiplican dos potencias <strong>de la misma base</strong>, los factores simplemente se acumulan. Al desarrollarlas se descubre la regla:")}</p>
{big("a<sup>3</sup> · a<sup>2</sup> = (a · a · a)(a · a) = a<sup>5</sup>")}
<p>{t("Three factors plus two factors make five factors. The exponent of the answer is the <strong>sum</strong> of the exponents:", "Tres factores más dos factores dan cinco factores. El exponente del resultado es la <strong>suma</strong> de los exponentes:")}</p>
{big("a<sup>m</sup> · a<sup>n</sup> = a<sup>m + n</sup>")}
{ejemplo(t("Example 1: simplify x<sup>4</sup> · x<sup>6</sup>", "Ejemplo 1: simplifique x<sup>4</sup> · x<sup>6</sup>"),
  [("1", t("Same base.", "Misma base."), t("Both powers have base x, so the product rule applies.", "Las dos potencias tienen base x: se aplica la regla del producto.")),
   ("2", t("Add.", "Se suman."), "4 + 6 = 10."),
   ("✓", t("Answer.", "Respuesta."), "x<sup>4</sup> · x<sup>6</sup> = <strong>x<sup>10</sup></strong>")])}
{ejemplo(t("Example 2: simplify 2<sup>3</sup> · 2<sup>5</sup>", "Ejemplo 2: simplifique 2<sup>3</sup> · 2<sup>5</sup>"),
  [("1", t("Same base.", "Misma base."), t("The base is 2: add the exponents, 3 + 5 = 8.", "La base es 2: se suman los exponentes, 3 + 5 = 8.")),
   ("2", t("Value.", "Valor."), t("2<sup>8</sup> = 256. The base stays 2; it is not 4<sup>8</sup>.", "2<sup>8</sup> = 256. La base sigue siendo 2; no es 4<sup>8</sup>.")),
   ("✓", t("Answer.", "Respuesta."), "2<sup>3</sup> · 2<sup>5</sup> = <strong>2<sup>8</sup> = 256</strong>")])}
{caja("ojo", t("Two common mistakes", "Dos errores frecuentes"), t("<p>The exponents are <strong>added</strong>, not multiplied: a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>, not a<sup>6</sup>. And the rule works only with the <strong>same base</strong>: x<sup>2</sup> · y<sup>3</sup> cannot be combined.</p><p>A letter with no exponent has exponent 1: a = a<sup>1</sup>. So a<sup>7</sup> · a = a<sup>8</sup>.</p>",
"<p>Los exponentes se <strong>suman</strong>, no se multiplican: a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>, no a<sup>6</sup>. Y la regla solo vale con la <strong>misma base</strong>: x<sup>2</sup> · y<sup>3</sup> no se puede combinar.</p><p>Una letra sin exponente tiene exponente 1: a = a<sup>1</sup>. Por eso a<sup>7</sup> · a = a<sup>8</sup>.</p>"))}
{calc(t("Check a product of powers", "Compruebe un producto de potencias"), t(f"""<p>Type {T("2")} {T("^")} {T("3")} {T("▸")} {T("×")} {T("2")} {T("^")} {T("5")} {T("enter")}: the screen shows 256. Now type {T("2")} {T("^")} {T("8")} {T("enter")}: it also shows 256. On the calculator, the right arrow {T("▸")} gets you out of the exponent.</p>""",
f"""<p>Escriba {T("2")} {T("^")} {T("3")} {T("▸")} {T("×")} {T("2")} {T("^")} {T("5")} {T("enter")}: la pantalla muestra 256. Ahora escriba {T("2")} {T("^")} {T("8")} {T("enter")}: también muestra 256. En la calculadora, la flecha {T("▸")} lo saca del exponente.</p>"""))}
{practica("p1", t("Practice 1 — Add the exponents", "Práctica 1 — Sume los exponentes"), t("What is x<sup>4</sup> · x<sup>5</sup>?", "¿Cuánto es x<sup>4</sup> · x<sup>5</sup>?"),
          [("a", "x<sup>20</sup>"), ("b", "x<sup>9</sup>"), ("c", "x<sup>1</sup>"), ("d", "2x<sup>9</sup>")])}
{practica("p2", t("Practice 2 — A letter on its own", "Práctica 2 — Una letra sola"), t("What is a<sup>7</sup> · a?", "¿Cuánto es a<sup>7</sup> · a?"),
          [("a", "a<sup>7</sup>"), ("b", "a<sup>8</sup>"), ("c", "2a<sup>7</sup>"), ("d", "a<sup>0</sup>")])}
{practica("p3", t("Practice 3 — Three powers", "Práctica 3 — Tres potencias"), t("What is y<sup>2</sup> · y<sup>3</sup> · y<sup>4</sup>?", "¿Cuánto es y<sup>2</sup> · y<sup>3</sup> · y<sup>4</sup>?"),
          [("a", "y<sup>24</sup>"), ("b", "y<sup>7</sup>"), ("c", "y<sup>9</sup>"), ("d", "3y<sup>9</sup>")])}
{enlace(n, t("product", "producto"), t("the product rule", "la regla del producto"), t("Multiply powers with the same base by adding the exponents, also with coefficients.", "Multiplique potencias de la misma base sumando los exponentes, también con coeficientes."))}'''

    s3 = f'''<p>{t("When a power is raised to another exponent, the whole power repeats as a factor. Writing it out shows why the exponents are multiplied:", "Cuando una potencia se eleva a otro exponente, la potencia entera se repite como factor. Al desarrollarla se ve por qué los exponentes se multiplican:")}</p>
{big("(a<sup>2</sup>)<sup>3</sup> = a<sup>2</sup> · a<sup>2</sup> · a<sup>2</sup> = a<sup>6</sup>")}
<p>{t("a<sup>2</sup> repeats three times. By the product rule, 2 + 2 + 2 = 6, which is the same as 2 × 3. The exponent of the answer is the <strong>product</strong> of the exponents:", "a<sup>2</sup> se repite tres veces. Por la regla del producto, 2 + 2 + 2 = 6, que es lo mismo que 2 × 3. El exponente del resultado es el <strong>producto</strong> de los exponentes:")}</p>
{big("(a<sup>m</sup>)<sup>n</sup> = a<sup>m · n</sup>")}
{ejemplo(t("Example 3: simplify (x<sup>5</sup>)<sup>4</sup>", "Ejemplo 3: simplifique (x<sup>5</sup>)<sup>4</sup>"),
  [("1", t("Look at the shape.", "Mire la forma."), t("A power is raised to another power.", "Es una potencia elevada a otra potencia.")),
   ("2", t("Multiply.", "Se multiplican."), "5 × 4 = 20."),
   ("✓", t("Answer.", "Respuesta."), "(x<sup>5</sup>)<sup>4</sup> = <strong>x<sup>20</sup></strong>")])}
{caja("ojo", t("Do not mix up the two rules", "No confunda las dos reglas"), t("<p>In a<sup>5</sup> · a<sup>4</sup> the powers are <em>multiplied</em>, so the exponents are added: a<sup>9</sup>. In (a<sup>5</sup>)<sup>4</sup> one power is <em>raised</em> to the other, so the exponents are multiplied: a<sup>20</sup>. Look for parentheses with an exponent outside.</p>",
"<p>En a<sup>5</sup> · a<sup>4</sup> las potencias están <em>multiplicadas</em>: los exponentes se suman, a<sup>9</sup>. En (a<sup>5</sup>)<sup>4</sup> una potencia está <em>elevada</em> a la otra: los exponentes se multiplican, a<sup>20</sup>. Fíjese si hay un paréntesis con un exponente afuera.</p>"))}
{practica("p4", t("Practice 4 — Power of a power", "Práctica 4 — Potencia de una potencia"), t("What is (a<sup>3</sup>)<sup>5</sup>?", "¿Cuánto es (a<sup>3</sup>)<sup>5</sup>?"),
          [("a", "a<sup>8</sup>"), ("b", "a<sup>15</sup>"), ("c", "a<sup>35</sup>"), ("d", "a<sup>243</sup>")])}
{enlace(n, t("power-of-a-power", "potencia-potencia"), t("the power of a power", "la potencia de una potencia"), t("Count groups of factors and decide when to add and when to multiply.", "Cuente grupos de factores y decida cuándo sumar y cuándo multiplicar."))}'''

    s4 = f'''<p>{t("When the thing being raised is a <strong>product</strong> of several factors, the exponent is shared out to each factor:", "Cuando lo que se eleva es un <strong>producto</strong> de varios factores, el exponente se reparte a cada factor:")}</p>
{big("(ab)<sup>3</sup> = (ab)(ab)(ab) = a<sup>3</sup>b<sup>3</sup>")}
{big("(a · b)<sup>n</sup> = a<sup>n</sup> · b<sup>n</sup>")}
{ejemplo(t("Example 4: simplify (2x)<sup>3</sup>", "Ejemplo 4: simplifique (2x)<sup>3</sup>"),
  [("1", t("Share out.", "Se reparte."), t("The exponent 3 goes to <em>each</em> factor: to the 2 and to the x.", "El exponente 3 llega a <em>cada</em> factor: al 2 y a la x.")),
   ("2", t("Raise.", "Se eleva."), "2<sup>3</sup> = 8 · x<sup>3</sup> = x<sup>3</sup>."),
   ("✓", t("Answer.", "Respuesta."), "(2x)<sup>3</sup> = <strong>8x<sup>3</sup></strong>")])}
{ejemplo(t("Example 5: simplify (3y<sup>2</sup>)<sup>2</sup>", "Ejemplo 5: simplifique (3y<sup>2</sup>)<sup>2</sup>"),
  [("1", t("Share out.", "Se reparte."), "(3)<sup>2</sup> · (y<sup>2</sup>)<sup>2</sup>."),
   ("2", t("Two rules.", "Dos reglas."), t("3<sup>2</sup> = 9, and for (y<sup>2</sup>)<sup>2</sup> multiply the exponents: y<sup>4</sup>.", "3<sup>2</sup> = 9, y para (y<sup>2</sup>)<sup>2</sup> se multiplican los exponentes: y<sup>4</sup>.")),
   ("✓", t("Answer.", "Respuesta."), "(3y<sup>2</sup>)<sup>2</sup> = <strong>9y<sup>4</sup></strong>")])}
{caja("ojo", t("The most common mistake", "El error más frecuente"), t("<p>Forgetting to raise the number. (2x)<sup>3</sup> is <strong>not</strong> 2x<sup>3</sup>: the 2 is also cubed, so the answer is 8x<sup>3</sup>. And it is not 6x<sup>3</sup> either: cubing is not multiplying by 3.</p>",
"<p>Olvidar elevar el número. (2x)<sup>3</sup> <strong>no</strong> es 2x<sup>3</sup>: el 2 también se eleva al cubo y el resultado es 8x<sup>3</sup>. Y tampoco es 6x<sup>3</sup>: elevar al cubo no es multiplicar por 3.</p>"))}
{practica("p5", t("Practice 5 — Raise the number too", "Práctica 5 — Eleve también el número"), t("What is (2x)<sup>4</sup>?", "¿Cuánto es (2x)<sup>4</sup>?"),
          [("a", "2x<sup>4</sup>"), ("b", "8x<sup>4</sup>"), ("c", "16x<sup>4</sup>"), ("d", "16x")])}
{practica("p6", t("Practice 6 — Two letters", "Práctica 6 — Dos letras"), t("What is (x<sup>2</sup>y)<sup>3</sup>?", "¿Cuánto es (x<sup>2</sup>y)<sup>3</sup>?"),
          [("a", "x<sup>5</sup>y<sup>3</sup>"), ("b", "x<sup>6</sup>y"), ("c", "x<sup>6</sup>y<sup>3</sup>"), ("d", "x<sup>8</sup>y<sup>3</sup>")])}
{enlace(n, t("power-of-a-product", "potencia-producto"), t("the power of a product", "la potencia de un producto"), t("Share the exponent out to each factor, the coefficient too.", "Reparta el exponente a cada factor, también al coeficiente."))}'''

    filas = [[a, b + f" ({c})", d] for a, b, c, d in n3.tabla_reglas(False)]
    s5 = f'''<p>{t("These three rules cover all multiplication with exponents. The table sums them up.", "Estas tres reglas describen toda la multiplicación con exponentes. La tabla las resume.")}</p>
{tabla(t("The three rules for multiplying with exponents", "Las tres reglas de la multiplicación con exponentes"), t("The three rules for multiplying with exponents: name, pattern, and example", "Las tres reglas de la multiplicación con exponentes: nombre, patrón y ejemplo"),
       [t("Rule", "Regla"), t("Pattern", "Patrón"), t("Example", "Ejemplo")], filas)}
{ejemplo(t("Example 6: simplify (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>", "Ejemplo 6: simplifique (x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup>"),
  [("1", t("Parentheses first.", "Primero el paréntesis."), t("Power of a power: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>.", "Potencia de una potencia: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup>.")),
   ("2", t("Then the product.", "Después el producto."), "x<sup>6</sup> · x<sup>4</sup> = x<sup>6 + 4</sup>."),
   ("✓", t("Answer.", "Respuesta."), "(x<sup>2</sup>)<sup>3</sup> · x<sup>4</sup> = <strong>x<sup>10</sup></strong>")])}
{caja("tip", t("A strategy", "Una estrategia"), t("<p>When there are parentheses with an exponent, work them out first (power of a power or power of a product). Then combine with the product rule. Working <strong>from the inside out</strong> prevents most mistakes.</p>",
"<p>Cuando hay paréntesis con exponente, resuélvalos primero (potencia de una potencia o de un producto). Después combine con la regla del producto. Trabajar <strong>de adentro hacia afuera</strong> evita la mayoría de los errores.</p>"))}
{practica("p7", t("Practice 7 — Which rule?", "Práctica 7 — ¿Qué regla?"), t("Which rule do you use to simplify (x<sup>4</sup>)<sup>3</sup>?", "¿Qué regla se usa para simplificar (x<sup>4</sup>)<sup>3</sup>?"),
          [("a", t("Add the exponents", "Sumar los exponentes")), ("b", t("Multiply the exponents", "Multiplicar los exponentes")), ("c", t("Share the exponent out", "Repartir el exponente")), ("d", t("Subtract the exponents", "Restar los exponentes"))])}
{enlace(n, t("three-rules", "tres-reglas"), t("the three rules together", "las tres reglas juntas"), t("Decide which rule fits each step, and see which rule you need to review.", "Decida qué regla corresponde en cada paso y vea qué regla necesita repasar."))}'''

    secciones = [("s-" + t("notation", "notacion"), t("Review: exponential notation", "Repaso: la notación exponencial"), s1),
                 ("s-" + t("product", "producto"), t("The product rule", "La regla del producto"), s2),
                 ("s-" + t("power-of-a-power", "potencia-potencia"), t("The power of a power", "La potencia de una potencia"), s3),
                 ("s-" + t("power-of-a-product", "potencia-producto"), t("The power of a product", "La potencia de un producto"), s4),
                 ("s-" + t("three-rules", "tres-reglas"), t("The three rules together", "Las tres reglas juntas"), s5)]

    lesson = {"next": t("Lesson 1.2", "Lección 1.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("You multiplied the exponents. With the same base, add them.", "Multiplicó los exponentes. Con la misma base, se suman."), "c": t("You subtracted. When you multiply powers, the exponents are added.", "Restó. Al multiplicar potencias, los exponentes se suman."), "d": t("No 2 appears: x<sup>4</sup> · x<sup>5</sup> has no number in front.", "No aparece ningún 2: x<sup>4</sup> · x<sup>5</sup> no tiene número delante.")},
             "right": t("Same base: 4 + 5 = 9.", "Misma base: 4 + 5 = 9."), "solution": t("Same base x: add the exponents, 4 + 5 = 9, so x<sup>9</sup>.", "Misma base x: se suman los exponentes, 4 + 5 = 9, así que x<sup>9</sup>.")},
      "p2": {"ok": "b", "hints": {"a": t("The a on its own is a<sup>1</sup>: it adds one more factor.", "La a sola es a<sup>1</sup>: aporta un factor más."), "c": t("The two powers are multiplied, not added: no 2 appears.", "Las dos potencias se multiplican, no se suman: no aparece ningún 2."), "d": t("a = a<sup>1</sup>, not a<sup>0</sup>. Add 7 + 1.", "a = a<sup>1</sup>, no a<sup>0</sup>. Sume 7 + 1.")},
             "right": t("a = a<sup>1</sup>: 7 + 1 = 8.", "a = a<sup>1</sup>: 7 + 1 = 8."), "solution": t("A letter with no exponent has exponent 1: a<sup>7</sup> · a<sup>1</sup> = a<sup>8</sup>.", "Una letra sin exponente tiene exponente 1: a<sup>7</sup> · a<sup>1</sup> = a<sup>8</sup>.")},
      "p3": {"ok": "c", "hints": {"a": t("You multiplied the exponents: 2 × 3 × 4. Add them.", "Multiplicó los exponentes: 2 × 3 × 4. Se suman."), "b": t("You left one out. There are three exponents to add.", "Le faltó uno. Hay tres exponentes que sumar."), "d": t("There is no 3 in front: the three powers are multiplied, not added.", "No hay un 3 delante: las tres potencias se multiplican, no se suman.")},
             "right": t("2 + 3 + 4 = 9.", "2 + 3 + 4 = 9."), "solution": t("Add the three exponents: 2 + 3 + 4 = 9, so y<sup>9</sup>.", "Se suman los tres exponentes: 2 + 3 + 4 = 9, así que y<sup>9</sup>.")},
      "p4": {"ok": "b", "hints": {"a": t("You added. A power raised to a power: multiply the exponents.", "Sumó. Una potencia elevada a otra: los exponentes se multiplican."), "c": t("You wrote the two exponents side by side. Multiply them: 3 × 5.", "Escribió los dos exponentes juntos. Multiplíquelos: 3 × 5."), "d": t("You raised 3 to the 5th power. Just multiply the exponents.", "Elevó 3 a la quinta. Basta con multiplicar los exponentes.")},
             "right": t("3 × 5 = 15.", "3 × 5 = 15."), "solution": t("Power of a power: multiply the exponents, 3 × 5 = 15, so a<sup>15</sup>.", "Potencia de una potencia: se multiplican los exponentes, 3 × 5 = 15, así que a<sup>15</sup>.")},
      "p5": {"ok": "c", "hints": {"a": t("The 2 is inside the parentheses, so it is raised too.", "El 2 está dentro del paréntesis: también se eleva."), "b": t("2<sup>4</sup> = 2 · 2 · 2 · 2. Count again.", "2<sup>4</sup> = 2 · 2 · 2 · 2. Cuente otra vez."), "d": t("The x is raised to the 4th power as well.", "La x también se eleva a la cuarta.")},
             "right": t("2<sup>4</sup> = 16 and x<sup>4</sup>.", "2<sup>4</sup> = 16 y x<sup>4</sup>."), "solution": t("Share out the exponent: 2<sup>4</sup> = 16 and x<sup>4</sup>, so 16x<sup>4</sup>.", "Se reparte el exponente: 2<sup>4</sup> = 16 y x<sup>4</sup>, así que 16x<sup>4</sup>.")},
      "p6": {"ok": "c", "hints": {"a": t("For x you added 2 + 3. A power of a power multiplies: 2 × 3.", "Para la x sumó 2 + 3. La potencia de una potencia multiplica: 2 × 3."), "b": t("The y is inside the parentheses too: it is raised to the 3rd power.", "La y también está dentro del paréntesis: se eleva al cubo."), "d": t("Check the x: 2 × 3 = 6.", "Revise la x: 2 × 3 = 6.")},
             "right": t("x: 2 × 3 = 6; y: 1 × 3 = 3.", "x: 2 × 3 = 6; y: 1 × 3 = 3."), "solution": t("The 3 goes to each factor: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup> and y<sup>3</sup>, so x<sup>6</sup>y<sup>3</sup>.", "El 3 llega a cada factor: (x<sup>2</sup>)<sup>3</sup> = x<sup>6</sup> y y<sup>3</sup>, así que x<sup>6</sup>y<sup>3</sup>.")},
      "p7": {"ok": "b", "hints": {"a": t("You add when two powers are multiplied side by side. Here one power is raised to another.", "Se suma cuando dos potencias están multiplicadas una al lado de otra. Aquí una potencia está elevada a otra."), "c": t("You share out an exponent when there is a product inside the parentheses. Here there is only x<sup>4</sup>.", "Se reparte cuando hay un producto dentro del paréntesis. Aquí solo hay x<sup>4</sup>."), "d": t("You subtract when you divide. There is no division here.", "Se resta al dividir. Aquí no hay división.")},
             "right": t("(x<sup>4</sup>)<sup>3</sup> = x<sup>12</sup>.", "(x<sup>4</sup>)<sup>3</sup> = x<sup>12</sup>."), "solution": t("A power raised to a power: multiply the exponents. (x<sup>4</sup>)<sup>3</sup> = x<sup>12</sup>.", "Una potencia elevada a otra: se multiplican los exponentes. (x<sup>4</sup>)<sup>3</sup> = x<sup>12</sup>.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("You multiplied the exponents. Add them.", "Multiplicó los exponentes. Se suman."), "c": t("You subtracted. Add them.", "Restó. Se suman."), "d": t("You wrote 4 and 3 side by side. Add them.", "Escribió el 4 y el 3 juntos. Súmelos.")}, "solution": t("Same base: 4 + 3 = 7, so a<sup>7</sup>.", "Misma base: 4 + 3 = 7, así que a<sup>7</sup>.")},
      "B": {"ok": "c", "hints": {"a": t("The x on its own is x<sup>1</sup>: it adds one factor.", "La x sola es x<sup>1</sup>: aporta un factor."), "b": t("You subtracted. Add the exponents.", "Restó. Se suman los exponentes."), "d": t("You multiplied 5 × 5. Add 5 + 1.", "Multiplicó 5 × 5. Sume 5 + 1.")}, "solution": t("x = x<sup>1</sup>: 5 + 1 = 6, so x<sup>6</sup>.", "x = x<sup>1</sup>: 5 + 1 = 6, así que x<sup>6</sup>.")},
      "C": {"ok": "d", "hints": {"a": t("You added. A power of a power: multiply.", "Sumó. Potencia de una potencia: se multiplican."), "b": t("You wrote 3 and 4 side by side. Multiply them.", "Escribió el 3 y el 4 juntos. Multiplíquelos."), "c": t("You raised 3 to the 4th power. Just multiply 3 × 4.", "Elevó 3 a la cuarta. Basta con multiplicar 3 × 4.")}, "solution": t("(a<sup>3</sup>)<sup>4</sup>: 3 × 4 = 12, so a<sup>12</sup>.", "(a<sup>3</sup>)<sup>4</sup>: 3 × 4 = 12, así que a<sup>12</sup>.")},
      "D": {"ok": "c", "hints": {"a": t("The 4 is outside the parentheses: it reaches the a too.", "El 4 está fuera del paréntesis: también llega a la a."), "b": t("The 4 reaches the b too.", "El 4 también llega a la b."), "d": t("Raising to the 4th power is not multiplying by 4.", "Elevar a la cuarta no es multiplicar por 4.")}, "solution": t("The exponent goes to each factor: (ab)<sup>4</sup> = a<sup>4</sup>b<sup>4</sup>.", "El exponente llega a cada factor: (ab)<sup>4</sup> = a<sup>4</sup>b<sup>4</sup>.")},
      "E": {"ok": "a", "hints": {"b": t("The 2 is inside the parentheses, so it is cubed too.", "El 2 está dentro del paréntesis: también se eleva al cubo."), "c": t("Cubing is not multiplying by 3: 2<sup>3</sup> = 8.", "Elevar al cubo no es multiplicar por 3: 2<sup>3</sup> = 8."), "d": t("The x is cubed as well.", "La x también se eleva al cubo.")}, "solution": t("2<sup>3</sup> = 8 and x<sup>3</sup>, so 8x<sup>3</sup>.", "2<sup>3</sup> = 8 y x<sup>3</sup>, así que 8x<sup>3</sup>.")},
      "F": {"ok": "c", "hints": {"a": t("The 3 is squared too: 3<sup>2</sup> = 9.", "El 3 también se eleva al cuadrado: 3<sup>2</sup> = 9."), "b": t("For y<sup>2</sup> squared, multiply 2 × 2.", "Para y<sup>2</sup> al cuadrado, multiplique 2 × 2."), "d": t("Squaring 3 gives 9, not 6.", "3 al cuadrado da 9, no 6.")}, "solution": t("3<sup>2</sup> = 9 and (y<sup>2</sup>)<sup>2</sup> = y<sup>4</sup>, so 9y<sup>4</sup>.", "3<sup>2</sup> = 9 y (y<sup>2</sup>)<sup>2</sup> = y<sup>4</sup>, así que 9y<sup>4</sup>.")},
      "G": {"ok": "b", "hints": {"a": t("Inside the parentheses, the y also gets the 2: 3 × 2 = 6.", "Dentro del paréntesis, la y también recibe el 2: 3 × 2 = 6."), "c": t("For y you added 3 + 2. Multiply.", "Para la y sumó 3 + 2. Se multiplica."), "d": t("The x also gets the 2: 2 × 2 = 4.", "La x también recibe el 2: 2 × 2 = 4.")}, "solution": t("x: 2 × 2 = 4; y: 3 × 2 = 6. So x<sup>4</sup>y<sup>6</sup>.", "x: 2 × 2 = 4; y: 3 × 2 = 6. Así que x<sup>4</sup>y<sup>6</sup>.")},
      "H": {"ok": "d", "hints": {"a": t("Nothing is wrong with the base: it is a in both.", "La base no tiene nada de malo: es a en las dos."), "b": t("Subtracting is for division. Here the powers are multiplied.", "Restar es para dividir. Aquí las potencias se multiplican."), "c": t("There is a mistake: 3 + 2 is not 6.", "Sí hay un error: 3 + 2 no es 6.")}, "solution": t("The exponents were multiplied. They should be added: a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>.", "Se multiplicaron los exponentes. Deben sumarse: a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>.")}
     }}

    quiz = [
     ("A", t("Simplify a<sup>4</sup> · a<sup>3</sup>.", "Simplifique a<sup>4</sup> · a<sup>3</sup>."), [("a", "a<sup>7</sup>"), ("b", "a<sup>12</sup>"), ("c", "a<sup>1</sup>"), ("d", "a<sup>43</sup>")]),
     ("B", t("Simplify x<sup>5</sup> · x.", "Simplifique x<sup>5</sup> · x."), [("a", "x<sup>5</sup>"), ("b", "x<sup>4</sup>"), ("c", "x<sup>6</sup>"), ("d", "x<sup>25</sup>")]),
     ("C", t("Simplify (a<sup>3</sup>)<sup>4</sup>.", "Simplifique (a<sup>3</sup>)<sup>4</sup>."), [("a", "a<sup>7</sup>"), ("b", "a<sup>34</sup>"), ("c", "a<sup>81</sup>"), ("d", "a<sup>12</sup>")]),
     ("D", t("Simplify (ab)<sup>4</sup>.", "Simplifique (ab)<sup>4</sup>."), [("a", "ab<sup>4</sup>"), ("b", "a<sup>4</sup>b"), ("c", "a<sup>4</sup>b<sup>4</sup>"), ("d", "4ab")]),
     ("E", t("Simplify (2x)<sup>3</sup>.", "Simplifique (2x)<sup>3</sup>."), [("a", "8x<sup>3</sup>"), ("b", "2x<sup>3</sup>"), ("c", "6x<sup>3</sup>"), ("d", "8x")]),
     ("F", t("Simplify (3y<sup>2</sup>)<sup>2</sup>.", "Simplifique (3y<sup>2</sup>)<sup>2</sup>."), [("a", "3y<sup>4</sup>"), ("b", "9y<sup>2</sup>"), ("c", "9y<sup>4</sup>"), ("d", "6y<sup>4</sup>")]),
     ("G", t("Simplify (x<sup>2</sup>y<sup>3</sup>)<sup>2</sup>.", "Simplifique (x<sup>2</sup>y<sup>3</sup>)<sup>2</sup>."), [("a", "x<sup>4</sup>y<sup>3</sup>"), ("b", "x<sup>4</sup>y<sup>6</sup>"), ("c", "x<sup>4</sup>y<sup>5</sup>"), ("d", "x<sup>2</sup>y<sup>6</sup>")]),
     ("H", t("What is the mistake in “a<sup>3</sup> · a<sup>2</sup> = a<sup>6</sup>”?", "¿Cuál es el error en «a<sup>3</sup> · a<sup>2</sup> = a<sup>6</sup>»?"),
      [("a", t("The base is wrong", "La base es incorrecta")), ("b", t("The exponents should be subtracted: a<sup>1</sup>", "Los exponentes deben restarse: a<sup>1</sup>")), ("c", t("There is no mistake", "No hay error")), ("d", t("The exponents should be added: a<sup>5</sup>", "Los exponentes deben sumarse: a<sup>5</sup>"))])]

    return B.pagina_leccion(n, 1, t(*TEMA), t(*TIT),
        t("Three rules for multiplying with exponents. Each one comes from counting factors.", "Tres reglas para multiplicar con exponentes. Cada una sale de contar factores."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Use</strong> the product rule: a<sup>m</sup> · a<sup>n</sup> = a<sup>m+n</sup>.", "<strong>Aplicar</strong> la regla del producto: a<sup>m</sup> · a<sup>n</sup> = a<sup>m+n</sup>."),
         t("<strong>Use</strong> the power of a power rule: (a<sup>m</sup>)<sup>n</sup> = a<sup>m·n</sup>.", "<strong>Aplicar</strong> la regla de la potencia de una potencia: (a<sup>m</sup>)<sup>n</sup> = a<sup>m·n</sup>."),
         t("<strong>Use</strong> the power of a product rule: (a · b)<sup>n</sup> = a<sup>n</sup> · b<sup>n</sup>.", "<strong>Aplicar</strong> la regla de la potencia de un producto: (a · b)<sup>n</sup> = a<sup>n</sup> · b<sup>n</sup>."),
         t("<strong>Check</strong> each answer by writing the powers out as repeated multiplication.", "<strong>Comprobar</strong> cada resultado desarrollando las potencias como multiplicación repetida."),
         t("<strong>Choose</strong> the right rule from the shape of the expression.", "<strong>Elegir</strong> la regla que corresponde según la forma de la expresión.")],
        secciones,
        (t("Write and simplify eight products of powers with the same base (four with numbers, four with letters), writing the sum of the exponents before the answer. Then six powers of a power, two of them with a number in front; six powers of a product; and four expressions that need all three rules, writing the rule you used at each step.",
           "Escriba y simplifique ocho productos de potencias de la misma base (cuatro con números y cuatro con letras), anotando la suma de los exponentes antes del resultado. Después, seis potencias de potencia, dos con un número delante; seis potencias de un producto; y cuatro expresiones que exijan las tres reglas, anotando qué regla usó en cada paso."),
         t("Area and volume use exponents: a square room 12 feet on each side has an area of 12<sup>2</sup> square feet. Find two square or cube-shaped things at home, measure them, and write their area or volume as a power. Then check the value on the calculator.",
           "El área y el volumen usan exponentes: un cuarto cuadrado de 12 pies por lado tiene un área de 12<sup>2</sup> pies cuadrados. Busque en casa dos objetos cuadrados o en forma de cubo, mídalos y escriba su área o su volumen como una potencia. Después compruebe el valor en la calculadora.")),
        quiz,
        t("Self-check checklist for the three rules for multiplying with exponents", "Lista de autoevaluación de las tres reglas de la multiplicación con exponentes"),
        t("Self-check checklist: skills for the product rule, power of a power, and power of a product", "Lista de autoevaluación: destrezas de la regla del producto, la potencia de una potencia y la potencia de un producto"),
        [(t("The product rule", "La regla del producto"), t("I add the exponents of the same base and can explain it by counting factors.", "Sumo los exponentes de la misma base y sé explicarlo contando factores."), t("I add them, but sometimes I miss a factor, like a<sup>1</sup>.", "Los sumo, pero a veces se me escapa un factor, como a<sup>1</sup>."), t("I multiply the exponents or combine different bases.", "Multiplico los exponentes o combino bases distintas.")),
         (t("Power of a power and of a product", "Potencia de potencia y de un producto"), t("I multiply the exponents and give the exponent to every factor, the number too.", "Multiplico los exponentes y reparto el exponente a todos los factores, también al número."), t("I use the rule, but I forget to raise the number in front.", "Aplico la regla, pero olvido elevar el número de delante."), t("I mix up when to add and when to multiply.", "Confundo cuándo sumar y cuándo multiplicar.")),
         (t("Combined expressions", "Expresiones combinadas"), t("I work from the inside out and write the rule I use at each step.", "Trabajo de adentro hacia afuera y anoto la regla que uso en cada paso."), t("I use the rules, but in no clear order.", "Aplico las reglas, pero sin un orden claro."), t("I do not know which rule to use first.", "No sé qué regla aplicar primero."))],
        t("<p>You learned the three rules for <strong>multiplying with exponents</strong>: the product rule (exponents are <strong>added</strong>), the power of a power (they are <strong>multiplied</strong>), and the power of a product (the exponent is <strong>shared out</strong> to each factor). All of them come from counting factors.</p>\n<p>In <strong>Lesson 1.2 · The quotient rule, zero exponents, and negative exponents</strong> you will divide powers, where the exponents are subtracted, and you will discover why a<sup>0</sup> = 1 and what a negative exponent means.</p>",
          "<p>Aprendió las tres reglas de la <strong>multiplicación con exponentes</strong>: el producto (los exponentes se <strong>suman</strong>), la potencia de una potencia (se <strong>multiplican</strong>) y la potencia de un producto (el exponente se <strong>reparte</strong> a cada factor). Todas salen de contar factores.</p>\n<p>En la <strong>Lección 1.2 · Regla del cociente, exponente cero y exponentes negativos</strong> dividirá potencias, donde los exponentes se restan, y descubrirá por qué a<sup>0</sup> = 1 y qué significa un exponente negativo.</p>"),
        ("1-2", ("", t("Lesson 1.2 · The quotient rule, zero exponents, and negative exponents", "Lección 1.2 · Regla del cociente, exponente cero y exponentes negativos"))),
        [(t("base", "base"), t("The factor that repeats in a power. In a<sup>5</sup>, the base is a.", "El factor que se repite en una potencia. En a<sup>5</sup>, la base es a.")),
         (t("exponent", "exponente"), t("The small number that says how many times the base repeats as a factor.", "El número pequeño que dice cuántas veces se repite la base como factor.")),
         (t("power", "potencia"), t("A base with an exponent, like 2<sup>3</sup> or x<sup>5</sup>.", "Una base con un exponente, como 2<sup>3</sup> o x<sup>5</sup>.")),
         (t("coefficient", "coeficiente"), t("The number that multiplies the letters in a term. In 8x<sup>3</sup>, the coefficient is 8.", "El número que multiplica a las letras de un término. En 8x<sup>3</sup>, el coeficiente es 8.")),
         (t("factor", "factor"), t("Each of the numbers or letters that are multiplied.", "Cada uno de los números o letras que se multiplican."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var VARS = ["x", "y", "a", "m", "n", "b"];
function fac(n){ return n === 1 ? T(" factor", " factor") : T(" factors", " factores"); }

/* ============ MODULE 1 · exponential notation ============ */
function actualizaNotacion(){
  var n = leeEntero("n-exp", 1, 8, "n-aviso", T("exponent", "exponente"));
  if (n === null){ $("n-salida").innerHTML = ""; return; }
  limpiaAviso("n-aviso");
  var bv = $("n-base").value, h = "", f = [], esVar = isNaN(parseInt(bv, 10));
  if (esVar){
    for (var i = 0; i < n; i++) f.push(bv);
    h += '<div class="linea">' + T("Base", "Base") + ': <strong>' + bv + "</strong> · " + T("exponent", "exponente") + ": <strong>" + n + "</strong></div>";
    h += '<div class="linea">' + T("Written out", "Forma desarrollada") + ": " + ver(igualX(xp(bv, n), X(f.join(" · "), f.join(VZ.por)))) + "</div>";
    h += '<div class="linea veredicto">' + n + fac(n) + T(" of ", " de ") + bv + (n === 1 ? T(". A letter on its own already has exponent 1, even if you do not write it.", ". Una letra sola ya tiene exponente 1, aunque no se escriba.") : ".") + "</div>";
  } else {
    var b = parseInt(bv, 10), bH = b < 0 ? "(" + numTxt(b) + ")" : String(b), bS = b < 0 ? VZ.abre + numVoz(b) + VZ.cierra : String(b);
    for (var j = 0; j < n; j++) f.push(bH);
    var valor = Math.pow(b, n);
    h += '<div class="linea">' + T("Base", "Base") + ": <strong>" + numTxt(b) + "</strong> · " + T("exponent", "exponente") + ": <strong>" + n + "</strong></div>";
    h += '<div class="linea">' + ver(igualX(potX(bH, bS, n), X(f.join(" · "), f.join(VZ.por)))) + " = <strong>" + fmt(valor) + "</strong></div>";
    if (b < 0){
      var sinPar = -Math.pow(-b, n);
      h += '<div class="linea">' + T("Without parentheses", "Sin paréntesis") + ": " + ver(potX(MENOS + Math.abs(b), numVoz(b), n)) + " = " + MENOS + "(" + Array(n + 1).join(String(-b) + " · ").slice(0, -3) + ") = <strong>" + fmt(sinPar) + "</strong></div>";
      h += '<div class="linea veredicto">' + (n % 2 === 0
        ? T("With an even exponent, (" + numTxt(b) + ")<sup>" + n + "</sup> is positive; without parentheses the answer is negative. They are not the same.", "Con exponente par, (" + numTxt(b) + ")<sup>" + n + "</sup> es positivo; sin paréntesis el resultado es negativo. No son lo mismo.")
        : T("With an odd exponent the two answers are equal, but for different reasons: look at where the sign is.", "Con exponente impar los dos resultados coinciden, pero por razones distintas: fíjese en dónde está el signo.")) + "</div>";
    } else h += '<div class="linea veredicto">' + n + fac(n) + T(" of ", " de ") + b + T(": the value is ", ": el valor es ") + fmt(valor) + ".</div>";
  }
  $("n-salida").innerHTML = h;
}
function genNotacion(){
  var t = ale(1, 3);
  if (t === 1){
    var b, n;
    do { b = ale(2, 5); n = ale(2, 4); } while ((b === 2 && n === 2) || Math.pow(b, n) > 625);
    var v = Math.pow(b, n);
    return { enun: T("What is ", "¿Cuánto vale ") + ver(xp(String(b), n)) + "?",
      opciones: unicas([numOp(v, true),
        numOp(b * n, false, T("You multiplied the base by the exponent. The exponent says how many times the base repeats as a factor.", "Multiplicó la base por el exponente. El exponente dice cuántas veces se repite la base como factor.")),
        numOp(Math.pow(n, b), false, T("You swapped the base and the exponent.", "Intercambió la base y el exponente.")),
        numOp(Math.pow(b, n - 1), false, T("One factor is missing: count again how many times the base appears.", "Le falta un factor: cuente otra vez cuántas veces aparece la base.")),
        numOp(v + b, false, "")]),
      sol: ver(xp(String(b), n)) + " = " + Array(n + 1).join(b + " · ").slice(0, -3) + " = " + v + "." };
  }
  if (t === 2){
    var b2 = ale(2, 4), n2 = ale(2, 4), con = Math.random() < 0.5;
    if (b2 === 2 && n2 === 2) n2 = 3;
    var val = con ? Math.pow(-b2, n2) : -Math.pow(b2, n2);
    var ex = con ? potX("(" + MENOS + b2 + ")", VZ.abre + numVoz(-b2) + VZ.cierra, n2) : potX(MENOS + b2, numVoz(-b2), n2);
    var expl = con
      ? T("The base is " + MENOS + b2 + ": the sign is multiplied " + n2 + " times, and with an " + (n2 % 2 === 0 ? "even exponent the answer is positive." : "odd exponent the answer is negative."),
          "La base es " + MENOS + b2 + ": el signo se multiplica " + n2 + " veces, y con exponente " + (n2 % 2 === 0 ? "par el resultado es positivo." : "impar el resultado es negativo."))
      : T("With no parentheses, the base is only the " + b2 + ": first " + b2 + "<sup>" + n2 + "</sup> = " + Math.pow(b2, n2) + ", then the minus sign goes in front.",
          "Sin paréntesis, la base es solo el " + b2 + ": primero " + b2 + "<sup>" + n2 + "</sup> = " + Math.pow(b2, n2) + ", y después el signo menos se pone delante.");
    return { enun: T("What is ", "¿Cuánto vale ") + ver(ex) + "?",
      opciones: unicas([numOp(val, true),
        numOp(-val, false, T("The sign is wrong: check whether the minus sign is inside the parentheses or outside.", "El signo no es el correcto: fíjese si el signo menos está dentro del paréntesis o fuera.")),
        numOp(-b2 * n2, false, T("You multiplied the base by the exponent.", "Multiplicó la base por el exponente.")),
        numOp(b2 * n2, false, T("You multiplied the base by the exponent and lost the sign.", "Multiplicó la base por el exponente y además perdió el signo."))]),
      sol: expl };
  }
  var v3 = elige(VARS), k = ale(3, 7), f = [];
  for (var i = 0; i < k; i++) f.push(v3);
  return { enun: T("How do you write ", "¿Cómo se escribe ") + ver(X(f.join(" · "), f.join(VZ.por))) + T(" with an exponent?", " con un exponente?"),
    opciones: [{x: xp(v3, k), ok: true},
      {x: X(k + v3, k + " " + v3), ok: false, fb: T(k + v3 + " means " + v3 + " + " + v3 + " + …, a repeated addition, not a repeated multiplication.", k + v3 + " significa " + v3 + " + " + v3 + " + …, una suma repetida, no una multiplicación repetida.")},
      {x: X(k + "<sup>" + v3 + "</sup>", k + VZ.pot + v3), ok: false, fb: T("The base is " + v3 + " and the exponent is " + k + ": you swapped them.", "La base es " + v3 + " y el exponente es " + k + ": los puso al revés.")},
      {x: xp(v3, k - 1), ok: false, fb: T("Count the factors again: there are " + k + ".", "Cuente otra vez los factores: son " + k + ".")}],
    sol: T("There are " + k + " factors of " + v3 + ", so the exponent is " + k + ".", "Hay " + k + " factores de " + v3 + ", así que el exponente es " + k + ".") };
}

/* ============ MODULE 2 · the product rule ============ */
function actualizaProducto(){
  var m = leeEntero("pr-m", 1, 7, "pr-aviso", T("first exponent", "primer exponente"));
  var n = m === null ? null : leeEntero("pr-n", 1, 7, "pr-aviso", T("second exponent", "segundo exponente"));
  if (m === null || n === null){ $("pr-fichas").innerHTML = ""; $("pr-salida").innerHTML = ""; return; }
  limpiaAviso("pr-aviso");
  $("pr-fichas").innerHTML = '<span class="grupo">' + fichas("a", m) + '</span><span class="signo">·</span><span class="grupo">' + fichas("a", n, "b") + '</span><span class="signo">=</span><span class="grupo">' + fichas("a", m) + fichas("a", n, "b") + "</span>";
  var h = '<div class="linea">' + ver(igualX(porX(xp("a", m), xp("a", n)), xp("a", m + n))) + "</div>";
  h += '<div class="linea veredicto">' + m + fac(m) + T(" plus ", " más ") + n + fac(n) + T(" make ", " son ") + (m + n) + T(" factors: ", " factores: ") + m + " + " + n + " = " + (m + n) + ".</div>";
  if (m === 1 || n === 1) h += '<div class="linea">' + T("An a on its own counts as a<sup>1</sup>: it adds one factor.", "Una a sola cuenta como a<sup>1</sup>: aporta un factor.") + "</div>";
  $("pr-salida").innerHTML = h;
}
function genProducto1(){
  var t = ale(1, 4), v = elige(VARS), a, b, c, et = T("Exponent of the answer", "Exponente del resultado");
  if (t === 1){
    a = ale(2, 9); b = ale(2, 9);
    return { enun: ver(igualX(porX(xp(v, a), xp(v, b)), preg(v))), etiqueta: et, resp: a + b,
      pista: function(x){ return x === a * b ? T("You multiplied the exponents. When powers are multiplied, the exponents are added.", "Multiplicó los exponentes. Cuando las potencias están multiplicadas, los exponentes se suman.") : null; },
      sol: T("Same base: add the exponents, " + a + " + " + b + " = " + (a + b) + ".", "Misma base: se suman los exponentes, " + a + " + " + b + " = " + (a + b) + ".") };
  }
  if (t === 2){
    a = ale(2, 6); b = ale(2, 6); c = ale(2, 6);
    return { enun: ver(igualX(porX(porX(xp(v, a), xp(v, b)), xp(v, c)), preg(v))), etiqueta: et, resp: a + b + c,
      pista: function(x){ return x === a * b * c ? T("You multiplied the exponents; with powers that are multiplied, add them.", "Multiplicó los exponentes; con potencias multiplicadas se suman.") : (x === a + b || x === b + c || x === a + c ? T("You left out one of the three exponents.", "Le faltó uno de los tres exponentes.") : null); },
      sol: T("Add the three exponents: ", "Se suman los tres exponentes: ") + a + " + " + b + " + " + c + " = " + (a + b + c) + "." };
  }
  if (t === 3){
    a = ale(2, 9);
    var ex = Math.random() < 0.5 ? porX(X(v, v), xp(v, a)) : porX(xp(v, a), X(v, v));
    return { enun: ver(igualX(ex, preg(v))), etiqueta: et, resp: a + 1,
      pista: function(x){ return x === a ? T("The " + v + " on its own is not zero factors: it is " + v + "<sup>1</sup>, one factor.", "La " + v + " sola no vale cero factores: vale " + v + "<sup>1</sup>, un factor.") : null; },
      sol: T("Remember that ", "Recuerde que ") + v + " = " + v + "<sup>1</sup>: " + a + " + 1 = " + (a + 1) + "." };
  }
  var base = ale(2, 5), bs = String(base); a = ale(2, 6); b = ale(2, 6);
  return { enun: ver(igualX(porX(xp(bs, a), xp(bs, b)), preg(bs))), etiqueta: et, resp: a + b,
    pista: function(x){ return x === a * b ? T("You multiplied the exponents; add them.", "Multiplicó los exponentes; se suman.") : null; },
    sol: T("The base " + base + " stays the same and the exponents are added: " + a + " + " + b + " = " + (a + b) + ". The base is not multiplied: it is not " + (base * base) + "<sup>" + (a + b) + "</sup>.",
           "La base " + base + " se mantiene y se suman los exponentes: " + a + " + " + b + " = " + (a + b) + ". La base no se multiplica: no es " + (base * base) + "<sup>" + (a + b) + "</sup>.") };
}
function genProducto2(){
  var t = ale(1, 3), v = elige(["x", "a", "m"]), sim = T("Simplify ", "Simplifique ");
  if (t === 1){
    var c1 = ale(2, 7), c2 = ale(2, 7), a = ale(2, 6), b = ale(2, 6);
    if (a === 2 && b === 2) b = 3;
    var A = mono(c1, e1(v, a)), B = mono(c2, e1(v, b)), R = mMul(A, B);
    return { enun: sim + ver(porX(parX(mLinea(A)), parX(mLinea(B)))) + ".",
      opciones: opcionesMono(R, [
        [mono(c1 + c2, R.e), T("You added the numbers. They are multiplied: ", "Sumó los coeficientes. Se multiplican: ") + c1 + " · " + c2 + " = " + (c1 * c2) + "."],
        [mono(c1 * c2, e1(v, a * b)), T("You multiplied the exponents. They are added.", "Multiplicó los exponentes. Se suman.")],
        [mono(c1 + c2, e1(v, a * b)), T("You swapped the two operations: the numbers are multiplied and the exponents are added.", "Cambió las dos operaciones: los coeficientes se multiplican y los exponentes se suman.")]]),
      sol: T("Numbers: ", "Coeficientes: ") + c1 + " · " + c2 + " = " + (c1 * c2) + T(". Exponents of ", ". Exponentes de ") + v + ": " + a + " + " + b + " = " + (a + b) + "." };
  }
  if (t === 2){
    var p = ale(1, 5), q = ale(1, 4), r = ale(1, 5), s = ale(1, 4), k1 = ale(1, 5), k2 = ale(2, 5);
    var A2 = mono(k1, {x: p, y: q}), B2 = mono(k2, {x: r, y: s}), R2 = mMul(A2, B2);
    return { enun: sim + ver(porX(parX(mLinea(A2)), parX(mLinea(B2)))) + ".",
      opciones: opcionesMono(R2, [
        [mono(k1 * k2, {x: p + s, y: q + r}), T("You crossed the exponents: each base adds only its own exponents.", "Cruzó los exponentes: cada base suma solo sus propios exponentes.")],
        [mono(k1 + k2, R2.e), T("You added the numbers; they are multiplied.", "Sumó los coeficientes; se multiplican.")],
        [mono(k1 * k2, {x: p * r, y: q * s}), T("You multiplied the exponents; they are added.", "Multiplicó los exponentes; se suman.")],
        [mono(k1 * k2, {x: p + q + r + s}), T("You put different bases together: x and y do not combine.", "Juntó bases distintas: la x y la y no se combinan entre sí.")]]),
      sol: T("Numbers: ", "Coeficientes: ") + k1 + " · " + k2 + " = " + (k1 * k2) + T(". Exponents of x: ", ". Exponentes de x: ") + p + " + " + r + " = " + (p + r) + T(". Exponents of y: ", ". Exponentes de y: ") + q + " + " + s + " = " + (q + s) + "." };
  }
  var ea = ale(2, 6), eb = ale(2, 6);
  if (ea + eb === ea * eb) eb = 3;
  return { enun: sim + ver(porX(xp("x", ea), xp("y", eb))) + ".",
    opciones: [
      {html: ver(mLinea(mono(1, {x: ea, y: eb}))) + T(" (it is already simplified)", " (ya está simplificada)"), ok: true, fb: T("The bases are different: there is nothing to combine.", "Las bases son distintas: no hay nada que combinar.")},
      {x: parX(X("xy", "x y"), ea + eb), ok: false, fb: T("Adding exponents works only with the same base; x and y are different bases.", "Sumar los exponentes solo vale con la misma base; x e y son bases distintas.")},
      {x: xp("x", ea + eb), ok: false, fb: T("The y cannot disappear or turn into an x.", "La y no puede desaparecer ni convertirse en x.")},
      {x: parX(X("xy", "x y"), ea * eb), ok: false, fb: T("With different bases no rule applies: the expression stays as it is.", "Con bases distintas no se aplica ninguna regla: la expresión se queda como está.")}],
    sol: T("The product rule needs the same base. x<sup>" + ea + "</sup>y<sup>" + eb + "</sup> is already as simple as it gets.", "La regla del producto exige la misma base. x<sup>" + ea + "</sup>y<sup>" + eb + "</sup> es la forma más simple.") };
}

/* ============ MODULE 3 · power of a power ============ */
function actualizaPotPot(){
  var m = leeEntero("pp-m", 1, 5, "pp-aviso", T("inside exponent", "exponente de dentro"));
  var n = m === null ? null : leeEntero("pp-n", 1, 4, "pp-aviso", T("outside exponent", "exponente de fuera"));
  if (m === null || n === null){ $("pp-fichas").innerHTML = ""; $("pp-salida").innerHTML = ""; return; }
  limpiaAviso("pp-aviso");
  var g = [];
  for (var i = 0; i < n; i++) g.push('<span class="grupo">' + fichas("a", m, i % 2 ? "b" : "") + "</span>");
  $("pp-fichas").innerHTML = g.join('<span class="signo">·</span>');
  var rep = [];
  for (var j = 0; j < n; j++) rep.push(xp("a", m));
  var des = rep.reduce(function(acc, x){ return acc ? porX(acc, x) : x; }, null);
  var h = '<div class="linea">' + ver(igualX(igualX(parX(xp("a", m), n), des), xp("a", m * n))) + "</div>";
  h += '<div class="linea veredicto">' + n + (n === 1 ? T(" group", " grupo") : T(" groups", " grupos")) + T(" of ", " de ") + m + fac(m) + T(" make ", " son ") + (m * n) + T(" factors: ", " factores: ") + m + " × " + n + " = " + (m * n) + ".</div>";
  if (n > 1) h += '<div class="linea">' + T("It is the same as adding ", "Es lo mismo que sumar ") + Array(n + 1).join(m + " + ").slice(0, -3) + " = " + (m * n) + T(": multiplying is adding the same number several times.", ": multiplicar es sumar el mismo número varias veces.") + "</div>";
  $("pp-salida").innerHTML = h;
}
function genPotPot(){
  var v = elige(VARS), a, n, sim = T("Simplify ", "Simplifique ");
  do { a = ale(2, 6); n = ale(2, 5); } while (a + n === a * n);
  if (Math.random() < 0.6){
    var dis = [[xv(v, a + n), T("You added the exponents. Here one power is raised to another: multiply them.", "Sumó los exponentes. Aquí una potencia está elevada a otra: se multiplican.")]];
    if (Math.pow(a, n) <= 81) dis.push([xv(v, Math.pow(a, n)), T("You raised one exponent to the other; just multiply them.", "Elevó un exponente al otro; basta con multiplicarlos.")]);
    dis.push([xv(v, a * n + 1), T("Check the multiplication of the exponents.", "Revise la multiplicación de los exponentes.")]);
    dis.push([xv(v, Math.abs(a - n) || a + 1), ""]);
    return { enun: sim + ver(parX(xp(v, a), n)) + ".", opciones: opcionesMono(xv(v, a * n), dis),
      sol: T("Power of a power: ", "Potencia de una potencia: ") + a + " × " + n + " = " + (a * n) + "." };
  }
  var b = n;
  return { enun: sim + ver(porX(xp(v, a), xp(v, b))) + ".",
    opciones: opcionesMono(xv(v, a + b), [
      [xv(v, a * b), T("You multiplied the exponents. There are no parentheses here: the powers are multiplied, so the exponents are added.", "Multiplicó los exponentes. Aquí no hay paréntesis: las potencias están multiplicadas y los exponentes se suman.")],
      [xv(v, a + b + 1), T("Check the sum of the exponents.", "Revise la suma de los exponentes.")],
      [xv(v, Math.abs(a - b) || a * b + 1), ""]]),
    sol: T("Product rule: ", "Regla del producto: ") + a + " + " + b + " = " + (a + b) + "." };
}

/* ============ MODULE 4 · power of a product ============ */
function actualizaPotProd(){
  var c = leeEntero("px-c", 1, 5, "px-aviso", T("coefficient", "coeficiente"));
  var a = c === null ? null : leeEntero("px-a", 1, 4, "px-aviso", T("exponent of x", "exponente de x"));
  var b = a === null ? null : leeEntero("px-b", 0, 3, "px-aviso", T("exponent of y", "exponente de y"));
  var n = b === null ? null : leeEntero("px-n", 2, 4, "px-aviso", T("outside exponent", "exponente de fuera"));
  if (n === null){ $("px-salida").innerHTML = ""; return; }
  limpiaAviso("px-aviso");
  var e = {x: a}; if (b > 0) e.y = b;
  var A = mono(c, e), R = mPow(A, n), piezas = [];
  if (c !== 1) piezas.push(xp(String(c), n));
  piezas.push(a === 1 ? xp("x", n) : parX(xp("x", a), n));
  if (b > 0) piezas.push(b === 1 ? xp("y", n) : parX(xp("y", b), n));
  var rep = piezas.reduce(function(acc, x){ return acc ? porX(acc, x) : x; }, null);
  var h = '<div class="linea">' + ver(igualX(igualX(parX(mLinea(A), n), rep), mFinal(R))) + "</div>", det = [];
  if (c !== 1) det.push(T("the number: ", "el coeficiente: ") + c + "<sup>" + n + "</sup> = " + Math.pow(c, n));
  det.push(T("the x: ", "la x: ") + a + " × " + n + " = " + (a * n));
  if (b > 0) det.push(T("the y: ", "la y: ") + b + " × " + n + " = " + (b * n));
  h += '<div class="linea veredicto">' + T("The exponent " + n + " reaches each factor — ", "El exponente " + n + " llega a cada factor — ") + det.join("; ") + ".</div>";
  if (c === 1) h += '<div class="linea">' + T("A coefficient of 1 is not written: 1 raised to any exponent is still 1.", "Con coeficiente 1 no se escribe: 1 elevado a cualquier exponente sigue siendo 1.") + "</div>";
  $("px-salida").innerHTML = h;
}
function genPotProd(){
  var c, a = ale(1, 4), n = ale(2, 4), conY = Math.random() < 0.45, b = ale(1, 3), neg = Math.random() < 0.25;
  do { c = neg ? -ale(2, 3) : ale(2, 5); } while (Math.pow(Math.abs(c), n) > 625 || Math.abs(c) === n);
  var e = {x: a}; if (conY) e.y = b;
  var A = mono(c, e), R = mPow(A, n);
  var dis = [[mono(c, R.e), T("You forgot to raise the number: the " + numTxt(c) + " is inside the parentheses too.", "Olvidó elevar el coeficiente: el " + numTxt(c) + " también está dentro del paréntesis.")],
             [mono(c * n, R.e), T("You multiplied the number by " + n + "; raise it instead: " + numTxt(c) + "<sup>" + n + "</sup>.", "Multiplicó el coeficiente por " + n + "; hay que elevarlo: " + numTxt(c) + "<sup>" + n + "</sup>.")]];
  if (neg) dis.unshift([mono(-R.n, R.e), T("The sign is raised too: with an " + (n % 2 === 0 ? "even exponent the answer is positive." : "odd exponent the answer is negative."), "El signo también se eleva: con exponente " + (n % 2 === 0 ? "par el resultado es positivo." : "impar el resultado es negativo."))]);
  var eS = {x: a + n}; if (conY) eS.y = b + n;
  dis.push([mono(R.n, eS), T("You added the exponents of the letters; in a power of a product they are multiplied.", "Sumó los exponentes de las variables; en la potencia de un producto se multiplican.")]);
  return { enun: T("Simplify ", "Simplifique ") + ver(parX(mLinea(A), n)) + ".", opciones: opcionesMono(R, dis),
    sol: T("Share out the exponent: ", "Se reparte el exponente: ") + numTxt(c) + "<sup>" + n + "</sup> = " + numTxt(Math.pow(c, n)) + "; x: " + a + " × " + n + " = " + (a * n) + (conY ? "; y: " + b + " × " + n + " = " + (b * n) : "") + "." };
}

/* ============ MODULE 5 · the three rules together ============ */
function genTres(){
  var tipo = elige(["producto", "potpot", "potprod", "combinada", "combinada"]), v = elige(["x", "a", "y"]), R, ex, pasos, dis;
  function ee(k){ return e1(v, k); }
  var rP = T("product", "producto"), rPP = T("power of a power", "potencia de una potencia"), rPX = T("power of a product", "potencia de un producto");
  if (tipo === "producto"){
    var a = ale(2, 6), b = ale(1, 5), c = ale(2, 6);
    R = xv(v, a + b + c); ex = porX(porX(xp(v, a), xp(v, b)), xp(v, c));
    dis = [[xv(v, a * b * c), T("You multiplied the exponents; they are added.", "Multiplicó los exponentes; se suman.")],
           [xv(v, a + c), T("You skipped a factor: ", "Se saltó un factor: ") + v + (b === 1 ? T(" on its own is ", " sola vale ") + v + "<sup>1</sup>." : "<sup>" + b + "</sup>" + T(" counts too.", " también cuenta."))], [xv(v, a + b + c + 1), ""]];
    pasos = [T("Product rule: ", "Regla del producto: ") + a + " + " + b + " + " + c + " = " + (a + b + c) + "."];
  } else if (tipo === "potpot"){
    var p, q; do { p = ale(2, 6); q = ale(2, 5); } while (p + q === p * q);
    R = xv(v, p * q); ex = parX(xp(v, p), q);
    dis = [[xv(v, p + q), T("You added; with a power raised to a power, the exponents are multiplied.", "Sumó; con una potencia elevada a otra, los exponentes se multiplican.")], [xv(v, p * q + q), ""], [xv(v, p * q - 1), ""]];
    pasos = [T("Power of a power: ", "Potencia de una potencia: ") + p + " × " + q + " = " + (p * q) + "."];
  } else if (tipo === "potprod"){
    var k = ale(2, 4), r = ale(1, 4), s; do { s = ale(2, 3); } while (s === k);
    R = mPow(mono(k, ee(r)), s); ex = parX(mLinea(mono(k, ee(r))), s);
    dis = [[mono(k, R.e), T("The number still has to be raised.", "Falta elevar el coeficiente.")], [mono(k * s, R.e), T("The number is raised, not multiplied by the exponent.", "El coeficiente se eleva, no se multiplica por el exponente.")], [mono(R.n, ee(r + s)), T("The exponents are multiplied, not added.", "Los exponentes se multiplican, no se suman.")]];
    pasos = [T("Power of a product: ", "Potencia de un producto: ") + k + "<sup>" + s + "</sup> = " + Math.pow(k, s) + T(" and ", " y ") + r + " × " + s + " = " + (r * s) + "."];
  } else {
    var sub = ale(1, 3);
    if (sub === 1){
      var a1 = ale(2, 5), n1 = ale(2, 4), b1 = ale(1, 6);
      if (a1 + n1 === a1 * n1) n1 = 3;
      R = mMul(xv(v, a1 * n1), xv(v, b1)); ex = porX(parX(xp(v, a1), n1), xp(v, b1));
      dis = [[xv(v, a1 + n1 + b1), T("You added everything. The parentheses go first, and there the exponents are multiplied.", "Sumó todo. El paréntesis va primero y allí los exponentes se multiplican.")],
             [xv(v, a1 * n1 * b1), T("You multiplied everything. After the parentheses, the product adds exponents.", "Multiplicó todo. Después del paréntesis, el producto suma exponentes.")],
             [xv(v, a1 * (n1 + b1)), T("The outside exponent affects only what is inside the parentheses.", "El exponente de fuera solo afecta a lo que está dentro del paréntesis.")]];
      pasos = [T("Parentheses first: ", "Paréntesis primero: ") + "(" + v + "<sup>" + a1 + "</sup>)<sup>" + n1 + "</sup> = " + v + "<sup>" + (a1 * n1) + "</sup>." + R_(rPP),
               T("Product: ", "Producto: ") + (a1 * n1) + " + " + b1 + " = " + (a1 * n1 + b1) + "." + R_(rP)];
    } else if (sub === 2){
      var k2 = ale(2, 3), a2 = ale(1, 4), n2 = ale(2, 3), b2 = ale(1, 5);
      R = mMul(mPow(mono(k2, ee(a2)), n2), xv(v, b2)); ex = porX(parX(mLinea(mono(k2, ee(a2))), n2), xp(v, b2));
      dis = [[mono(k2, R.e), T("The number inside the parentheses still has to be raised.", "Falta elevar el coeficiente dentro del paréntesis.")],
             [mono(R.n, ee(a2 + n2 + b2)), T("Inside the parentheses the exponents are multiplied.", "En el paréntesis los exponentes se multiplican.")],
             [mono(k2 * n2, R.e), T("The number is raised: ", "El coeficiente se eleva: ") + k2 + "<sup>" + n2 + "</sup>."]];
      pasos = [T("Parentheses: ", "Paréntesis: ") + k2 + "<sup>" + n2 + "</sup> = " + Math.pow(k2, n2) + T(" and ", " y ") + a2 + " × " + n2 + " = " + (a2 * n2) + "." + R_(rPX),
               T("Product: ", "Producto: ") + (a2 * n2) + " + " + b2 + " = " + (a2 * n2 + b2) + "." + R_(rP)];
    } else {
      var a3 = ale(2, 4), n3 = ale(2, 3), b3 = ale(1, 3), m3 = ale(2, 4);
      R = mMul(xv(v, a3 * n3), xv(v, b3 * m3)); ex = porX(parX(xp(v, a3), n3), parX(xp(v, b3), m3));
      dis = [[xv(v, a3 + n3 + b3 + m3), T("You added all the exponents; parentheses multiply.", "Sumó todos los exponentes; los paréntesis multiplican.")],
             [xv(v, a3 * n3 * b3 * m3), T("After the parentheses, the two powers are multiplied: add the exponents.", "Tras resolver los paréntesis, las dos potencias están multiplicadas: se suman.")],
             [xv(v, a3 * n3 + b3), T("The second parentheses have to be worked out too.", "El segundo paréntesis también hay que resolverlo.")]];
      pasos = [T("First parentheses: ", "Primer paréntesis: ") + a3 + " × " + n3 + " = " + (a3 * n3) + T("; second: ", "; segundo: ") + b3 + " × " + m3 + " = " + (b3 * m3) + "." + R_(rPP),
               T("Product: ", "Producto: ") + (a3 * n3) + " + " + (b3 * m3) + " = " + (a3 * n3 + b3 * m3) + "." + R_(rP)];
    }
  }
  return {enun: T("Simplify ", "Simplifique ") + ver(ex) + ".", opciones: opcionesMono(R, dis), sol: pasosHTML(pasos), regla: tipo};
}

/* ============ Start ============ */
$("n-base").addEventListener("change", actualizaNotacion);
$("n-exp").addEventListener("input", actualizaNotacion);
actualizaNotacion();
OM("p-notacion", genNotacion);
["pr-m", "pr-n"].forEach(function(id){ $(id).addEventListener("input", actualizaProducto); });
actualizaProducto();
ESCRITA("p-producto1", genProducto1);
OM("p-producto2", genProducto2);
["pp-m", "pp-n"].forEach(function(id){ $(id).addEventListener("input", actualizaPotPot); });
actualizaPotPot();
OM("p-potpot", genPotPot);
["px-c", "px-a", "px-b", "px-n"].forEach(function(id){ $(id).addEventListener("input", actualizaPotProd); });
actualizaPotProd();
OM("p-potprod", genPotProd);
OM("p-tres", genTres, [["producto", T("Product of powers", "Producto de potencias")], ["potpot", T("Power of a power", "Potencia de una potencia")], ["potprod", T("Power of a product", "Potencia de un producto")], ["combinada", T("Rules combined", "Reglas combinadas")]]);
'''

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("notation", "notacion"), t("Exponential notation", "La notación exponencial"),
      f'''      <p>{t("In a power a<sup>n</sup>, the <strong>base</strong> a is the factor that repeats and the <strong>exponent</strong> n says how many times it repeats. <strong>The exponent counts factors</strong>: if you can count the factors, you always get the right exponent, even if you do not remember the rule.", "En una potencia a<sup>n</sup>, la <strong>base</strong> a es el factor que se repite y el <strong>exponente</strong> n dice cuántas veces se repite. <strong>El exponente cuenta factores</strong>: si sabe contar los factores, siempre llega al exponente correcto, aunque no recuerde la regla.")}</p>
      <h3>{t("Power explorer", "Explorador de potencias")}</h3>
      <p>{t("Choose a base and an exponent, and look at the written-out form and the value.", "Elija una base y un exponente, y observe la forma desarrollada y el valor.")}</p>
{P.panel(P.lista("n-base", t("Base", "Base"), [(2, "2"), (3, "3"), (5, "5"), (10, "10"), (-2, "−2"), (-3, "−3"), ("x", "x"), ("a", "a")], 3), P.numero("n-exp", t("Exponent (1 to 8)", "Exponente (de 1 a 8)"), 4, 1, 8))}
{P.aviso("n-aviso")}
{P.salida("n-salida")}
{P.atencion(t("Parentheses decide the base:", "El paréntesis manda:"), t("in (−3)<sup>4</sup> the base is −3 and the sign is multiplied four times, so the answer is positive. In −3<sup>4</sup> the base is only the 3; the minus sign stays outside and the answer is −81. Choose a negative base in the explorer to see it.", "en (−3)<sup>4</sup> la base es −3 y el signo se multiplica cuatro veces, así que el resultado es positivo. En −3<sup>4</sup> la base es solo el 3; el signo menos queda fuera y el resultado es −81. Elija una base negativa en el explorador para verlo."))}
{B.om("p-notacion", t("Practice: powers and the written-out form", "Practique: potencias y forma desarrollada"))}'''),
     (t("product", "producto"), t("The product rule", "La regla del producto"),
      f'''      <p>{t("When you multiply two powers with the <strong>same base</strong>, the factors pile up. That is why the exponents are <strong>added</strong>:", "Al multiplicar dos potencias de la <strong>misma base</strong>, los factores se acumulan. Por eso los exponentes <strong>se suman</strong>:")}</p>
{P.formula("a<sup>m</sup> · a<sup>n</sup> = a<sup>m + n</sup>")}
      <h3>{t("Factor counter", "Contador de factores")}</h3>
      <p>{t("Change the two exponents and count the chips: each chip is one factor of the base.", "Cambie los dos exponentes y cuente las fichas: cada ficha es un factor de la base.")}</p>
{P.panel(P.numero("pr-m", t("First exponent", "Primer exponente"), 3, 1, 7), P.numero("pr-n", t("Second exponent", "Segundo exponente"), 2, 1, 7))}
{P.aviso("pr-aviso")}
      <div class="fichas" id="pr-fichas" aria-hidden="true"></div>
{P.salida("pr-salida")}
{P.atencion(t("Two common mistakes:", "Dos errores frecuentes:"), t("the exponents are added, not multiplied (a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>, not a<sup>6</sup>). And the rule works only with the same base: x<sup>2</sup> · y<sup>3</sup> stays as it is.", "los exponentes se suman, no se multiplican (a<sup>3</sup> · a<sup>2</sup> = a<sup>5</sup>, no a<sup>6</sup>). Y la regla solo vale para bases iguales: x<sup>2</sup> · y<sup>3</sup> se queda como está."))}
{P.escrita("p-producto1", t("Practice: write the exponent of the answer", "Practique: escriba el exponente del resultado"), t("Exponent of the answer", "Exponente del resultado"))}
      <h3>{t("Practice: with numbers in front and with two bases", "Practique: con coeficientes y con varias bases")}</h3>
      <p>{t("The numbers in front are <strong>multiplied</strong>; the exponents of each base are <strong>added</strong> separately.", "Los coeficientes numéricos se <strong>multiplican</strong>; los exponentes de cada base se <strong>suman</strong> por separado.")}</p>
{B.om("p-producto2", "").replace("<h3></h3>", "")}'''),
     (t("power-of-a-power", "potencia-potencia"), t("The power of a power", "La potencia de una potencia"),
      f'''      <p>{t("When a power is raised to another exponent, the whole power repeats as a factor. Count the chips and you will see that the exponents are <strong>multiplied</strong>:", "Cuando una potencia se eleva a otro exponente, la potencia entera se repite como factor. Al contar las fichas se ve que los exponentes <strong>se multiplican</strong>:")}</p>
{P.formula("(a<sup>m</sup>)<sup>n</sup> = a<sup>m · n</sup>")}
      <h3>{t("Groups of factors", "Grupos de factores")}</h3>
      <p>{t("The inside exponent says how many chips each group has; the outside exponent says how many groups there are.", "El exponente de dentro dice cuántas fichas tiene cada grupo; el de fuera, cuántos grupos hay.")}</p>
{P.panel(P.numero("pp-m", t("Inside exponent", "Exponente de dentro"), 2, 1, 5), P.numero("pp-n", t("Outside exponent", "Exponente de fuera"), 3, 1, 4))}
{P.aviso("pp-aviso")}
      <div class="fichas" id="pp-fichas" aria-hidden="true"></div>
{P.salida("pp-salida")}
{P.atencion(t("Do not mix up the two rules:", "No confunda las dos reglas:"), t("in a<sup>5</sup> · a<sup>4</sup> the powers are <em>multiplied</em> and the exponents are added (a<sup>9</sup>); in (a<sup>5</sup>)<sup>4</sup> one power is <em>raised</em> to the other and the exponents are multiplied (a<sup>20</sup>).", "en a<sup>5</sup> · a<sup>4</sup> las potencias están <em>multiplicadas</em> y los exponentes se suman (a<sup>9</sup>); en (a<sup>5</sup>)<sup>4</sup> una potencia está <em>elevada</em> a la otra y los exponentes se multiplican (a<sup>20</sup>)."))}
      <h3>{t("Practice: add or multiply?", "Practique: ¿sumar o multiplicar?")}</h3>
      <p>{t("Both shapes are mixed here. Before you choose, look for parentheses with an exponent.", "Aquí se mezclan las dos formas. Antes de elegir, fíjese si hay paréntesis con exponente.")}</p>
{B.om("p-potpot", "").replace("<h3></h3>", "")}'''),
     (t("power-of-a-product", "potencia-producto"), t("The power of a product", "La potencia de un producto"),
      f'''      <p>{t("When the thing being raised is a product, the exponent is <strong>shared out to each factor</strong>, the number in front too:", "Cuando lo que se eleva es un producto, el exponente <strong>se reparte a cada factor</strong>, incluido el coeficiente numérico:")}</p>
{P.formula("(a · b)<sup>n</sup> = a<sup>n</sup> · b<sup>n</sup>")}
      <h3>{t("Exponent sharer", "Repartidor del exponente")}</h3>
      <p>{t("Build a product inside the parentheses and watch the outside exponent reach each factor.", "Arme un producto dentro del paréntesis y observe cómo el exponente de fuera llega a cada factor.")}</p>
{P.panel(P.numero("px-c", t("Coefficient", "Coeficiente"), 2, 1, 5), P.numero("px-a", t("Exponent of x", "Exponente de x"), 1, 1, 4), P.numero("px-b", t("Exponent of y (0 = no y)", "Exponente de y (0 = sin y)"), 0, 0, 3), P.numero("px-n", t("Outside exponent", "Exponente de fuera"), 3, 2, 4))}
{P.aviso("px-aviso")}
{P.salida("px-salida")}
{P.atencion(t("The most common mistake:", "El error más frecuente:"), t("forgetting to raise the number. (2x)<sup>3</sup> is not 2x<sup>3</sup>: the 2 is also cubed, and the answer is 8x<sup>3</sup>. It is not 6x<sup>3</sup> either: cubing is not multiplying by 3.", "olvidar elevar el coeficiente. (2x)<sup>3</sup> no es 2x<sup>3</sup>: el 2 también se eleva al cubo y el resultado es 8x<sup>3</sup>. Y tampoco es 6x<sup>3</sup>: elevar al cubo no es multiplicar por 3."))}
{B.om("p-potprod", t("Practice: share out the exponent", "Practique: reparta el exponente"))}'''),
     (t("three-rules", "tres-reglas"), t("The three rules together", "Las tres reglas juntas"),
      f'''{tabla_html()}
      <div class="caja-tip"><strong>{t("Strategy:", "Estrategia:")}</strong> {t("work out the parentheses with an exponent first (power of a power or of a product), then combine with the product rule. Working from the inside out prevents most mistakes.", "resuelva primero los paréntesis con exponente (potencia de una potencia o de un producto) y después combine con la regla del producto. Trabajar de adentro hacia afuera evita la mayoría de los errores.")}</div>
      <h3>{t("Practice: mixed expressions", "Practique: expresiones mixtas")}</h3>
      <p>{t("Each exercise uses one rule or combines them. The table under the exercise shows which rule you need to review.", "Cada ejercicio se centra en una regla o las combina. La tabla de debajo del ejercicio le dice qué regla necesita repasar.")}</p>
{B.om("p-tres", "").replace("<h3></h3>", "")}''')]
    js = LOGICA
    return B.pagina_practica(n, 1, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=n3.ESTILO_EXP, scripts=("/math/exponents.js",))

def tabla_html():
    filas = "".join(f"<tr><td>{a}</td><td>{b} ({c})</td><td>{d}</td></tr>" for a, b, c, d in n3.tabla_reglas(False))
    return (f'      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("The three rules (table you can scroll sideways)", "Las tres reglas (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("The three rules for multiplying with exponents: name, pattern, and example.", "Las tres reglas de la multiplicación con exponentes: nombre, patrón y ejemplo.")}</caption>'
            f'<thead><tr><th scope="col">{t("Rule", "Regla")}</th><th scope="col">{t("Pattern", "Patrón")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead><tbody>{filas}</tbody></table></div>')

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Regla del producto, potencia de potencia y potencia de un producto")
