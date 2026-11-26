"""Level 3 · Lesson 3.3 · The real number system — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "3-3"
TEMA = ("Radicals and the real numbers", "Radicales y números reales")
TIT = ("The real number system: rational, irrational, and the number line", "El sistema de números reales: racionales, irracionales y la recta numérica")

def r(k, n=None):
    if n is None:
        return f'<span class="rad">√<span class="rc">{k}</span></span>'
    return f'{k}<span class="rad">√<span class="rc">{n}</span></span>'

def diagrama():
    """Nested sets of the real numbers (static SVG)."""
    R_, Q_, Z_, N_, I_ = t("Real numbers", "Números reales"), t("Rational", "Racionales"), t("Integers", "Enteros"), t("Natural", "Naturales"), t("Irrational", "Irracionales")
    lab = t("Diagram of the real numbers. Inside the real numbers there are two parts: the rational numbers and the irrational numbers. Inside the rational numbers are the integers, and inside the integers are the natural numbers. Examples: natural 1, 2, 3, 4; integers −2, −1, 0; rational 1/2, 0.75, −3/4, 0.333…; irrational √2, √3, π, √5.",
            "Diagrama de los números reales. Dentro de los reales hay dos partes: los racionales y los irracionales. Dentro de los racionales están los enteros, y dentro de los enteros, los naturales. Ejemplos: naturales 1, 2, 3, 4; enteros −2, −1, 0; racionales 1/2, 0.75, −3/4, 0.333…; irracionales √2, √3, π, √5.")
    return f'''<figure style="margin:18px 0"><svg viewBox="0 0 560 330" role="img" aria-label="{lab}" style="max-width:560px;width:100%;height:auto;display:block;margin:0 auto">
<rect x="5" y="5" width="550" height="320" rx="14" fill="#f5f7fa" stroke="#37474f" stroke-width="2"/><text x="20" y="28" font-size="16" font-weight="700" fill="#263238">{R_}</text>
<rect x="22" y="42" width="350" height="270" rx="14" fill="#e3f2fd" stroke="#0d47a1" stroke-width="2"/><text x="36" y="64" font-size="16" font-weight="700" fill="#0d47a1">{Q_}</text>
<text x="197" y="292" text-anchor="middle" font-size="16" fill="#0d47a1">1/2 · 0.75 · −3/4 · 0.333…</text>
<rect x="40" y="80" width="314" height="182" rx="14" fill="#e0f2f1" stroke="#004d40" stroke-width="2"/><text x="54" y="102" font-size="16" font-weight="700" fill="#004d40">{Z_}</text>
<text x="197" y="248" text-anchor="middle" font-size="16" fill="#004d40">… −2 · −1 · 0 …</text>
<rect x="58" y="118" width="278" height="100" rx="14" fill="#fff" stroke="#2e7d32" stroke-width="2"/><text x="72" y="140" font-size="16" font-weight="700" fill="#1b5e20">{N_}</text>
<text x="197" y="190" text-anchor="middle" font-size="18" fill="#1b5e20">1 · 2 · 3 · 4 …</text>
<rect x="388" y="42" width="150" height="270" rx="14" fill="#fff3e0" stroke="#e65100" stroke-width="2"/><text x="400" y="64" font-size="16" font-weight="700" fill="#bf360c">{I_}</text>
<text x="463" y="150" text-anchor="middle" font-size="18" fill="#bf360c">√2 · √3</text><text x="463" y="190" text-anchor="middle" font-size="18" fill="#bf360c">π · √5</text>
</svg></figure>'''

def recta():
    lab = t("Number line from 0 to 4 with the square root of 2 at about 1.41, the square root of 3 at about 1.73, and pi at about 3.14.", "Recta numérica de 0 a 4 con la raíz de 2 cerca de 1.41, la raíz de 3 cerca de 1.73 y pi cerca de 3.14.")
    x = lambda v: 40 + v * 140
    ticks = "".join(f'<line x1="{x(i)}" y1="80" x2="{x(i)}" y2="100" stroke="#424242" stroke-width="2"/><text x="{x(i)}" y="126" text-anchor="middle" font-size="20">{i}</text>' for i in range(5))
    marcas = "".join(f'<path d="M{x(v)} 86 l-9 -15 h18 z" fill="{c}"/><text x="{x(v)}" y="{y}" text-anchor="middle" font-size="18" font-weight="700" fill="{c}">{s}</text>' for v, s, c, y in ((1.414, "√2", "#0d47a1", 60), (1.732, "√3", "#004d40", 36), (3.1416, "π", "#bf360c", 60)))
    return f'<figure style="margin:18px 0"><svg viewBox="0 0 640 140" role="img" aria-label="{lab}" style="max-width:640px;width:100%;height:auto;display:block;margin:0 auto"><line x1="30" y1="90" x2="610" y2="90" stroke="#424242" stroke-width="2"/>{ticks}{marcas}</svg></figure>'

def leccion():
    n = N
    s1 = f'''<p>{t("Lessons 3.1 and 3.2 worked with radicals like √2 and √3, which have no exact decimal value. These numbers belong to a special family: the irrational numbers. This lesson places the radicals in the full picture of the numbers, separating the rational from the irrational and showing how together they make up the real number system.",
"Las Lecciones 3.1 y 3.2 trabajaron con radicales como √2 o √3, que no tienen un valor decimal exacto. Esos números pertenecen a una familia especial: los irracionales. Esta lección sitúa los radicales dentro del panorama completo de los números, distingue los racionales de los irracionales y muestra cómo todos juntos forman el sistema de los números reales.")}</p>
<p>{t("The real numbers are organized in sets that fit inside one another. The <strong>natural numbers</strong> (1, 2, 3, …) are inside the <strong>integers</strong> (…, −2, −1, 0, 1, 2, …), which are inside the <strong>rational numbers</strong> (the ones you can write as a fraction). Apart from them are the <strong>irrational numbers</strong>. Together, rational and irrational numbers make up the <strong>real numbers</strong>.",
"Los números reales se organizan en conjuntos que se contienen unos a otros. Los <strong>naturales</strong> (1, 2, 3, …) están dentro de los <strong>enteros</strong> (…, −2, −1, 0, 1, 2, …), que están dentro de los <strong>racionales</strong> (los que se pueden escribir como fracción). Aparte están los <strong>irracionales</strong>. Juntos, racionales e irracionales forman los <strong>reales</strong>.")}</p>
{diagrama()}
{caja("tip", t("How to read the diagram", "Cómo leer el diagrama"), t("<p>Each number belongs to the smallest set that contains it and to every set around it. The number 3 is natural, but it is also an integer, rational, and real. On the other hand, √2 is irrational and real, but it is not rational or an integer.</p>", "<p>Cada número pertenece al conjunto más pequeño que lo contiene y a todos los que lo rodean. El número 3 es natural, pero también es entero, racional y real. En cambio, √2 es irracional y real, pero no es racional ni entero.</p>"))}
{enlace(n, t("classify", "clasificar"), t("the real number system", "el sistema de los números reales"), t("Place each number in the most specific set it belongs to.", "Ubique cada número en el conjunto más específico al que pertenece."))}'''

    s2 = f'''<p>{t("A number is <strong>rational</strong> if you can write it as a fraction of two integers (with a denominator that is not zero). Its decimal form always ends (like 0.75) or repeats a pattern (like 0.333…).", "Un número es <strong>racional</strong> si se puede escribir como una fracción de dos enteros (con denominador distinto de cero). Su forma decimal siempre termina (como 0.75) o se repite en un patrón (como 0.333…).")}</p>
{tabla(t("Rational numbers and their decimal form", "Números racionales y su forma decimal"), t("Examples of rational numbers, written as a fraction and as a decimal", "Ejemplos de números racionales, como fracción y como decimal"), [t("Number", "Número"), t("As a fraction", "Como fracción"), t("Decimal form", "Forma decimal")],
  [["0.75", "3/4", t("Ends", "Termina")], ["0.333…", "1/3", t("Repeats", "Se repite")], ["5", "5/1", t("Ends", "Termina")], [r(9), "3 = 3/1", t("Ends (√9 = 3)", "Termina (√9 = 3)")]])}
{caja("ojo", t("Careful with roots", "Cuidado con las raíces"), t(f"<p>Not every root is irrational. {r(9)} = 3 is rational, because 9 is a perfect square. Only the roots that do not come out exact, like {r(2)} or {r(5)}, are irrational.</p>", f"<p>No toda raíz es irracional. {r(9)} = 3 es racional, porque 9 es un cuadrado perfecto. Solo son irracionales las raíces que no dan un resultado exacto, como {r(2)} o {r(5)}.</p>"))}'''

    s3 = f'''<p>{t("A number is <strong>irrational</strong> if you cannot write it as a fraction of two integers. Its decimal form does not end and does not repeat any pattern. The best-known examples are √2, √3, √5, and the number π.", "Un número es <strong>irracional</strong> si no se puede escribir como fracción de dos enteros. Su forma decimal no termina y no se repite en ningún patrón. Los ejemplos más conocidos son √2, √3, √5 y el número π.")}</p>
{ejemplo(t(f"Example 1: why {r(2)} is irrational", f"Ejemplo 1: por qué {r(2)} es irracional"),
  [("1", t("On the calculator.", "En la calculadora."), t(f"{r(2)} = 1.41421356…, and the digits go on without ending or repeating a pattern.", f"{r(2)} = 1.41421356…, y las cifras continúan sin terminar ni repetir un patrón.")),
   ("2", t("If it were rational…", "Si fuera racional…"), t("it could be written as an exact fraction of integers. But no fraction squared gives exactly 2, and its decimal never closes a cycle.", "podría escribirse como una fracción exacta de enteros. Pero ninguna fracción al cuadrado da exactamente 2, y su decimal nunca cierra un ciclo.")),
   ("✓", t("Conclusion.", "Conclusión."), t(f"{r(2)} cannot be written as a fraction: it is <strong>irrational</strong>.", f"{r(2)} no se puede escribir como fracción: es <strong>irracional</strong>."))])}
{caja("tip", t("The number π", "El número π"), t("<p>π ≈ 3.14159265… is the ratio of the circumference to the diameter of any circle. Its decimals go on forever without repeating, so π is irrational, just like radicals that do not come out exact. 22/7 and 3.14 are only approximations of π, and both are rational.</p>", "<p>π ≈ 3.14159265… representa la razón entre la circunferencia y el diámetro de cualquier círculo. Sus decimales continúan infinitamente sin repetirse, por lo que π es irracional, igual que los radicales no exactos. 22/7 y 3.14 son solo aproximaciones de π, y las dos son racionales.</p>"))}
{practica("p1", t("Practice 1 — A fraction", "Práctica 1 — Una fracción"), t("How do you classify 1/2?", "¿Cómo se clasifica 1/2?"),
          [("a", t("Rational", "Racional")), ("b", t("Irrational", "Irracional")), ("c", t("Integer", "Entero"))])}
{practica("p2", t("Practice 2 — The number π", "Práctica 2 — El número π"), t("How do you classify π?", "¿Cómo se clasifica π?"),
          [("a", t("Rational", "Racional")), ("b", t("Irrational", "Irracional")), ("c", t("Integer", "Entero"))])}
{practica("p3", t("Practice 3 — A negative number", "Práctica 3 — Un negativo"), t("What is the most specific set for −4?", "¿Cuál es el conjunto más específico de −4?"),
          [("a", t("Natural", "Natural")), ("b", t("Irrational", "Irracional")), ("c", t("Integer", "Entero"))])}
{enlace(n, t("rational-irrational", "racional-irracional"), t("rational or irrational?", "¿racional o irracional?"), t("Tell apart the decimals that end, repeat, or follow no pattern.", "Distinga los decimales que terminan, se repiten o no siguen ningún patrón."))}'''

    s4 = f'''<p>{t("Even though an irrational number has no exact decimal value, it has a precise place on the number line. To place it, use its decimal approximation and find which whole numbers it falls between.", "Aunque un irracional no tenga un valor decimal exacto, sí ocupa un lugar preciso en la recta numérica. Para ubicarlo, se usa su aproximación decimal y se busca entre qué enteros cae.")}</p>
{recta()}
{ejemplo(t(f"Example 2: place {r(3)}", f"Ejemplo 2: ubique {r(3)}"),
  [("1", t("Trap it.", "Acorralar."), t(f"1 &lt; 3 &lt; 4, so 1 &lt; {r(3)} &lt; 2.", f"1 &lt; 3 &lt; 4, así que 1 &lt; {r(3)} &lt; 2.")),
   ("2", t("Approximate.", "Aproximar."), t(f"{r(3)} ≈ 1.73, closer to 2 than to 1.", f"{r(3)} ≈ 1.73, más cerca del 2 que del 1.")),
   ("✓", t("Answer.", "Respuesta."), t(f"{r(3)} is between <strong>1 and 2</strong> on the number line.", f"{r(3)} se ubica entre <strong>1 y 2</strong> en la recta numérica."))])}
{caja("tip", t("Comparing without a calculator", "Comparar sin calculadora"), t(f"<p>To compare a root with a whole number, compare their squares. Is {r(10)} greater than 3? Since 10 &gt; 9 = 3<sup>2</sup>, yes: {r(10)} &gt; 3.</p>", f"<p>Para comparar una raíz con un entero, compare sus cuadrados. ¿{r(10)} es mayor que 3? Como 10 &gt; 9 = 3<sup>2</sup>, sí: {r(10)} &gt; 3.</p>"))}
{enlace(n, t("number-line", "recta"), t("placing irrational numbers on the number line", "ubicar irracionales en la recta numérica"), t("Place √n and π on the number line from their approximations.", "Coloque √n y π en la recta numérica a partir de su aproximación."))}'''

    s5 = f'''<p>{t("A repeating decimal is rational, because you can always write it as a fraction. There is an algebra procedure to find that fraction.", "Un decimal periódico (que repite un patrón) es racional, porque siempre se puede escribir como fracción. Existe un procedimiento algebraico para encontrarla.")}</p>
{ejemplo(t("Example 3: write 0.666… as a fraction", "Ejemplo 3: escriba 0.666… como fracción"),
  [("1", t("Name it.", "Nombrarlo."), "x = 0.666…"),
   ("2", t("Multiply by 10.", "Multiplicar por 10."), "10x = 6.666…"),
   ("3", t("Subtract.", "Restar."), t("10x − x = 6.666… − 0.666…, that is, 9x = 6.", "10x − x = 6.666… − 0.666…, es decir, 9x = 6.")),
   ("4", t("Solve.", "Despejar."), "x = 6/9 = 2/3."),
   ("✓", t("Answer.", "Respuesta."), t("0.666… = <strong>2/3</strong>, a rational number.", "0.666… = <strong>2/3</strong>, un número racional."))])}
{caja("tip", t("How much to multiply by?", "¿Por cuánto multiplicar?"), t("<p>By 10 if one digit repeats; by 100 if two digits repeat. So 0.272727… gives 100x − x = 27, and x = 27/99 = 3/11. Being able to write the decimal as a fraction is the proof that it is rational. With √2 you never reach an exact fraction, and that is why it is irrational.</p>", "<p>Por 10 si se repite una cifra; por 100 si se repiten dos. Así, 0.272727… da 100x − x = 27, y x = 27/99 = 3/11. Poder escribir el decimal como fracción es la prueba de que es racional. Con √2 nunca se llega a una fracción exacta, y por eso es irracional.</p>"))}
{practica("p4", t("Practice 4 — Place it", "Práctica 4 — Ubicar"), t(f"Between which whole numbers is {r(5)} (≈ 2.24)?", f"¿Entre qué enteros está {r(5)} (≈ 2.24)?"),
          [("a", t("Between 2 and 3", "Entre 2 y 3")), ("b", t("Between 1 and 2", "Entre 1 y 2")), ("c", t("Between 3 and 4", "Entre 3 y 4"))])}
{practica("p5", t("Practice 5 — Convert", "Práctica 5 — Convertir"), t("What fraction is equal to 0.222…?", "¿Qué fracción equivale a 0.222…?"),
          [("a", "2/10"), ("b", "1/5"), ("c", "2/9")])}
{practica("p6", t("Practice 6 — An exact root", "Práctica 6 — Una raíz exacta"), t(f"Is {r(16)} rational or irrational?", f"¿{r(16)} es racional o irracional?"),
          [("a", t("Irrational", "Irracional")), ("b", t("Rational (it is 4)", "Racional (es 4)")), ("c", t("It is not a real number", "No es un número real"))])}
{enlace(n, t("repeating", "periodicos"), t("repeating decimals to fractions", "decimales periódicos a fracciones"), t("Turn a repeating decimal into a fraction, step by step.", "Convierta un decimal periódico en fracción, paso a paso."))}'''

    secciones = [("s-" + t("real-numbers", "numeros-reales"), t("The real number system", "El sistema de los números reales"), s1),
                 ("s-" + t("rational", "racionales"), t("Rational numbers", "Números racionales"), s2),
                 ("s-" + t("irrational", "irracionales"), t("Irrational numbers", "Números irracionales"), s3),
                 ("s-" + t("number-line", "recta"), t("Placing irrational numbers on the number line", "Ubicar irracionales en la recta numérica"), s4),
                 ("s-" + t("repeating", "periodicos"), t("Repeating decimals to fractions", "Decimales periódicos a fracciones"), s5)]

    lesson = {"next": t("Lesson 4.1", "Lección 4.1"), "review": t("sections 1, 4, and 5", "las secciones 1, 4 y 5"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("1/2 is a fraction of two integers.", "1/2 es una fracción de dos enteros."), "c": t("1/2 = 0.5 is not a whole number.", "1/2 = 0.5 no es un número entero.")}, "right": t("1/2 is a fraction of integers: it is rational.", "1/2 es una fracción de enteros: es racional."), "solution": t("1/2 = 0.5, a fraction of integers whose decimal ends: rational.", "1/2 = 0.5, una fracción de enteros cuyo decimal termina: racional.")},
      "p2": {"ok": "b", "hints": {"a": t("3.14 and 22/7 are only approximations of π.", "3.14 y 22/7 son solo aproximaciones de π."), "c": t("π ≈ 3.14159…: it has decimals.", "π ≈ 3.14159…: tiene decimales.")}, "right": t("Its decimals do not end or repeat.", "Sus decimales no terminan ni se repiten."), "solution": t("π ≈ 3.14159… never ends or repeats: irrational.", "π ≈ 3.14159… nunca termina ni se repite: irracional.")},
      "p3": {"ok": "c", "hints": {"a": t("The natural numbers start at 1; they are not negative.", "Los naturales empiezan en 1; no son negativos."), "b": t("−4 = −4/1 can be written as a fraction.", "−4 = −4/1 se puede escribir como fracción.")}, "right": t("−4 is a negative whole number: an integer.", "−4 es un número entero negativo: es entero."), "solution": t("−4 is an integer (and also rational and real), but not natural.", "−4 es entero (y también racional y real), pero no natural.")},
      "p4": {"ok": "a", "hints": {"b": t("2.24 is greater than 2.", "2.24 es mayor que 2."), "c": t("2.24 is less than 3.", "2.24 es menor que 3.")}, "right": "4 &lt; 5 &lt; 9, " + t("so", "así que") + f" 2 &lt; {r(5)} &lt; 3.", "solution": f"{r(4)} = 2 " + t("and", "y") + f" {r(9)} = 3, " + t("so", "así que") + f" {r(5)} " + t("is between 2 and 3.", "está entre 2 y 3.")},
      "p5": {"ok": "c", "hints": {"a": t("2/10 = 0.2 ends; it does not repeat.", "2/10 = 0.2 termina; no se repite."), "b": t("1/5 = 0.2 ends; it does not repeat.", "1/5 = 0.2 termina; no se repite.")}, "right": "10x − x = 2, " + t("so", "así que") + " 9x = 2 " + t("and", "y") + " x = 2/9.", "solution": "x = 0.222…; 10x = 2.222…; 9x = 2; x = 2/9."},
      "p6": {"ok": "b", "hints": {"a": t("16 is a perfect square.", "16 es un cuadrado perfecto."), "c": t("√16 = 4, a real number.", "√16 = 4, un número real.")}, "right": f"{r(16)} = 4 = 4/1.", "solution": t(f"16 is a perfect square: {r(16)} = 4, which is rational.", f"16 es un cuadrado perfecto: {r(16)} = 4, que es racional.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("7 has no decimals.", "El 7 no tiene decimales."), "b": t("There is a more specific set.", "Hay un conjunto más específico."), "c": t("7 is positive.", "El 7 es positivo.")}, "solution": t("7 is a counting number: natural.", "7 es un número de contar: natural.")},
      "B": {"ok": "a", "hints": {"b": t("2 is not a perfect square.", "2 no es un cuadrado perfecto."), "c": t("√2 ≈ 1.414… has decimals.", "√2 ≈ 1.414… tiene decimales."), "d": t("√2 ≈ 1.414… has decimals.", "√2 ≈ 1.414… tiene decimales.")}, "solution": t("√2 ≈ 1.41421…: irrational.", "√2 ≈ 1.41421…: irracional.")},
      "C": {"ok": "c", "hints": {"a": t("9 is a perfect square.", "9 es un cuadrado perfecto."), "b": t("√9 = 3, a real number.", "√9 = 3, un número real."), "d": t("√9 = 3 exactly.", "√9 = 3 exactamente.")}, "solution": "√9 = 3 = 3/1."},
      "D": {"ok": "b", "hints": {"a": t("√2 ≈ 1.41.", "√2 ≈ 1.41."), "c": t("√2 is less than √4 = 2.", "√2 es menor que √4 = 2."), "d": t("√2 is less than √4 = 2.", "√2 es menor que √4 = 2.")}, "solution": t("1 < 2 < 4, so 1 < √2 < 2.", "1 < 2 < 4, así que 1 < √2 < 2.")},
      "E": {"ok": "c", "hints": {"a": t("π ≈ 3.14.", "π ≈ 3.14."), "b": t("π ≈ 3.14.", "π ≈ 3.14."), "d": t("π has decimals: 3.14…", "π tiene decimales: 3.14…")}, "solution": t("π ≈ 3.14: between 3 and 4.", "π ≈ 3.14: entre 3 y 4.")},
      "F": {"ok": "a", "hints": {"b": t("3/10 = 0.3 ends.", "3/10 = 0.3 termina."), "c": t("1/30 = 0.0333…", "1/30 = 0.0333…"), "d": t("33/100 = 0.33 ends.", "33/100 = 0.33 termina.")}, "solution": "9x = 3: x = 3/9 = 1/3."},
      "G": {"ok": "b", "hints": {"a": t("6/10 = 0.6 ends.", "6/10 = 0.6 termina."), "c": t("3/2 = 1.5.", "3/2 = 1.5."), "d": t("66/100 = 0.66 ends.", "66/100 = 0.66 termina.")}, "solution": "9x = 6: x = 6/9 = 2/3."},
      "H": {"ok": "d", "hints": {"a": t("√2 is positive.", "√2 es positivo."), "b": t("Many rational numbers are greater than 1.", "Muchos racionales son mayores que 1."), "c": t("√2 ≈ 1.414 is not a whole number.", "√2 ≈ 1.414 no es un entero.")}, "solution": t("Its decimal does not end or repeat, so it is not a fraction.", "Su decimal no termina ni se repite, así que no es una fracción.")}
     }}

    quiz = [
     ("A", t("What is the most specific set for the number 7?", "¿A qué conjunto más específico pertenece el número 7?"), [("a", t("Irrational", "Irracional")), ("b", t("Only real", "Solo real")), ("c", t("Negative", "Negativo")), ("d", t("Natural", "Natural"))]),
     ("B", t(f"How do you classify {r(2)}?", f"¿Cómo se clasifica {r(2)}?"), [("a", t("Irrational", "Irracional")), ("b", t("Rational", "Racional")), ("c", t("Integer", "Entero")), ("d", t("Natural", "Natural"))]),
     ("C", t(f"How do you classify {r(9)}?", f"¿Cómo se clasifica {r(9)}?"), [("a", t("Irrational", "Irracional")), ("b", t("Not a real number", "No es real")), ("c", t("Rational (it is 3)", "Racional (es 3)")), ("d", t("Only between 3 and 4", "Solo entre 3 y 4"))]),
     ("D", t(f"Between which whole numbers is {r(2)}?", f"¿Entre qué enteros está {r(2)}?"), [("a", t("Between 0 and 1", "Entre 0 y 1")), ("b", t("Between 1 and 2", "Entre 1 y 2")), ("c", t("Between 2 and 3", "Entre 2 y 3")), ("d", t("Between 3 and 4", "Entre 3 y 4"))]),
     ("E", t("Where is π on the number line?", "¿Dónde se ubica π en la recta numérica?"), [("a", t("Between 2 and 3", "Entre 2 y 3")), ("b", t("Between 4 and 5", "Entre 4 y 5")), ("c", t("Between 3 and 4", "Entre 3 y 4")), ("d", t("Exactly at 3", "En el 3 exacto"))]),
     ("F", t("What fraction is equal to 0.333…?", "¿Qué fracción equivale a 0.333…?"), [("a", "1/3"), ("b", "3/10"), ("c", "1/30"), ("d", "33/100")]),
     ("G", t("What fraction is equal to 0.666…?", "¿Qué fracción equivale a 0.666…?"), [("a", "6/10"), ("b", "2/3"), ("c", "3/2"), ("d", "66/100")]),
     ("H", t(f"Why is {r(2)} irrational?", f"¿Por qué {r(2)} es irracional?"), [("a", t("Because it is negative", "Porque es negativo")), ("b", t("Because it is greater than 1", "Porque es mayor que 1")), ("c", t("Because it is an integer", "Porque es un entero")), ("d", t("Because its decimal does not end or repeat", "Porque su decimal no termina ni se repite"))])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Sort numbers into rational and irrational, place irrational numbers on the number line, and turn repeating decimals into fractions.", "Clasifique números en racionales e irracionales, ubique irracionales en la recta numérica y convierta decimales periódicos en fracciones."),
        ("✏️", t("No calculator needed", "Sin calculadora")),
        [t("<strong>Classify</strong> numbers in the real number system (natural, integer, rational, irrational).", "<strong>Clasificar</strong> números en el sistema de los números reales (naturales, enteros, racionales, irracionales)."),
         t("<strong>Recognize</strong> how the sets fit inside one another: natural ⊂ integers ⊂ rational ⊂ real.", "<strong>Reconocer</strong> la relación de contención entre los conjuntos: naturales ⊂ enteros ⊂ racionales ⊂ reales."),
         t("<strong>Explain</strong> why √2 and π are irrational.", "<strong>Justificar</strong> por qué √2 y π son irracionales."),
         t("<strong>Place</strong> irrational numbers on the number line using approximations.", "<strong>Ubicar</strong> números irracionales en la recta numérica usando aproximaciones."),
         t("<strong>Convert</strong> a repeating decimal to a fraction to show that it is rational.", "<strong>Convertir</strong> un decimal periódico a fracción para mostrar que es racional.")],
        secciones,
        (t(f"Classify four numbers in the real number system, place three irrational numbers between two whole numbers on the number line, and convert three repeating decimals to fractions. When you have mastered the lesson, test your speed with <a href=\"speed-irrationals.html\">Irrational numbers against the clock</a>: twenty questions to classify, place, approximate, convert, and compare real numbers, each with its explanation.",
           f"Clasifique cuatro números en el sistema de los números reales, ubique tres irracionales entre dos enteros en la recta numérica y convierta tres decimales periódicos a fracción. Cuando domine la lección, ponga a prueba su agilidad con <a href=\"rapidez-irracionales.html\">Números irracionales contra reloj</a>: veinte preguntas para clasificar, ubicar, aproximar, convertir y comparar números reales, cada una con su explicación."),
         t("Look for numbers in your day: a price ($4.99), a recipe (3/4 cup), the temperature (−5 °F), the diagonal of a square tile 1 foot on each side (√2 feet). Write each one and its most specific set. Which of them could you write exactly as a fraction?",
           "Busque números en su día: un precio ($4.99), una receta (3/4 de taza), la temperatura (−5 °F), la diagonal de una baldosa cuadrada de 1 pie de lado (√2 pies). Escriba cada uno y su conjunto más específico. ¿Cuáles se pueden escribir exactamente como fracción?")),
        quiz,
        t("Self-check checklist for the real number system", "Lista de autoevaluación para el sistema de los números reales"),
        t("Self-check checklist: skills for classifying real numbers, placing them on the number line, and converting repeating decimals", "Lista de autoevaluación: destrezas para clasificar números reales, ubicarlos en la recta y convertir decimales periódicos"),
        [(t("Classifying real numbers", "Clasificar en el sistema real"), t("I put each number in its most specific set and can explain how the sets fit inside one another.", "Ubico cada número en su conjunto más específico y sé explicar la contención entre conjuntos."), t("I make mistakes in tricky cases (√9, decimals).", "Me equivoco en los casos límite (√9, decimales)."), t("I mix up rational and irrational numbers.", "Confundo racionales con irracionales.")),
         (t("Placing irrational numbers", "Ubicar irracionales en la recta"), t("I place the irrational number between the two right whole numbers and estimate where it falls.", "Ubico el irracional entre los dos enteros correctos y estimo su posición."), t("I approximate, but I place it between the wrong whole numbers.", "Aproximo, pero lo ubico entre enteros incorrectos."), t("I do not approximate or place irrational numbers.", "No aproximo ni ubico los irracionales.")),
         (t("Converting repeating decimals", "Convertir decimales periódicos"), t("I convert the repeating decimal to a fraction and explain why the number is rational.", "Convierto el decimal periódico a fracción y justifico que el número es racional."), t("I use the procedure, with some mistakes.", "Aplico el procedimiento con errores."), t("I do not use the algebra procedure.", "No aplico el procedimiento algebraico."))],
        t("<p>This lesson closes Topic 3. You now understand the real number system: the natural numbers inside the integers, inside the rational numbers; and the irrational numbers, like √2 and π, apart but also real. You learned to classify numbers, to place irrational numbers on the number line, and to turn repeating decimals into fractions to prove they are rational.</p>\n<p>With number sense complete (exponents, scientific notation, and the real numbers), Level 3 turns to algebra. Topic 4 opens with <strong>Lesson 4.1 · Variables, algebraic expressions, and translating</strong>, where letters stand for unknown amounts and you translate between words and algebra.</p>",
          "<p>Con esta lección se cierra el Tema 3. Ya comprende el sistema de los números reales: los naturales dentro de los enteros, dentro de los racionales; los irracionales —como √2 y π— aparte, pero también reales. Aprendió a clasificar, a ubicar irracionales en la recta numérica y a convertir decimales periódicos en fracciones para probar que son racionales.</p>\n<p>Con el sentido numérico ya completo (exponentes, notación científica y números reales), el Nivel 3 da un giro hacia el álgebra. El Tema 4 abre con la <strong>Lección 4.1 · Variables, expresiones algebraicas y traducción</strong>, donde las letras representan cantidades desconocidas y se traduce entre el lenguaje verbal y el algebraico.</p>"),
        ("4-1", ("", t("Lesson 4.1 · Variables, algebraic expressions, and translating", "Lección 4.1 · Variables, expresiones algebraicas y traducción"))),
        [(t("rational number", "número racional"), t("A number you can write as a fraction of two integers, like 3/4, 5, or 0.333…", "Un número que se puede escribir como fracción de dos enteros, como 3/4, 5 o 0.333…")),
         (t("irrational number", "número irracional"), t("A number whose decimal does not end or repeat, like √2 or π.", "Un número cuyo decimal no termina ni se repite, como √2 o π.")),
         (t("real numbers", "números reales"), t("All the rational and irrational numbers together: every point on the number line.", "Todos los racionales y los irracionales juntos: cada punto de la recta numérica.")),
         (t("repeating decimal", "decimal periódico"), t("A decimal in which a group of digits repeats forever, like 0.272727…", "Un decimal en el que un grupo de cifras se repite sin fin, como 0.272727…"))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ============ MODULE 1 · classifying in the real number system ============ */
var CONJ = {N: T("Natural", "Naturales"), Z: T("Integers", "Enteros"), Q: T("Rational", "Racionales"), I: T("Irrational", "Irracionales"), R: T("Real", "Reales")};
var CONJ1 = {N: T("natural", "natural"), Z: T("an integer", "entero"), Q: T("rational", "racional"), I: T("irrational", "irracional"), R: T("real", "real")};
var PERTENECE = {N: ["N", "Z", "Q", "R"], Z: ["Z", "Q", "R"], Q: ["Q", "R"], I: ["I", "R"]};
function num(vis, voz, txt, tp, nota){ return {html: envuelve(vis, voz), txt: txt, t: tp, nota: nota || ""}; }
var NUMEROS = [
  num("3", "3", "3", "N"), num("12", "12", "12", "N"),
  num(radVis(1, 9), radVoz(1, 9), "√9", "N", T("√9 = 3, which is natural.", "√9 = 3, que es natural.")),
  num(radVis(1, 25), radVoz(1, 25), "√25", "N", T("√25 = 5, which is natural.", "√25 = 5, que es natural.")),
  num(fracVis(6, 3), fracVoz(6, 3), "6/3", "N", T("6/3 = 2, which is natural.", "6/3 = 2, que es natural.")),
  num("0", "0", "0", "Z", T("0 is an integer, but not natural: the natural numbers start at 1.", "El 0 es entero, pero no natural: los naturales empiezan en 1.")),
  num("−4", T("negative 4", "menos 4"), "−4", "Z"), num("−15", T("negative 15", "menos 15"), "−15", "Z"),
  num("−" + radVis(1, 16), T("negative square root of 16", "menos raíz cuadrada de 16"), "−√16", "Z", T("−√16 = −4, which is an integer.", "−√16 = −4, que es entero.")),
  num(fracVis(1, 2), fracVoz(1, 2), "1/2", "Q"), num("0.75", "0.75", "0.75", "Q", "0.75 = 3/4."),
  num(fracVis(-3, 4), fracVoz(-3, 4), "−3/4", "Q"), num("0.333…", T("0.3 repeating", "0.3 periódico"), "0.333…", "Q", T("0.333… = 1/3: its decimal repeats.", "0.333… = 1/3: su decimal se repite.")),
  num("2.5", "2.5", "2.5", "Q", "2.5 = 5/2."), num("−1.2", T("negative 1.2", "menos 1.2"), "−1.2", "Q", "−1.2 = −6/5."),
  num(fracVis(22, 7), fracVoz(22, 7), "22/7", "Q", T("22/7 is close to π, but it is a fraction of integers.", "22/7 se parece a π, pero es una fracción de enteros.")),
  num(radVis(1, 2), radVoz(1, 2), "√2", "I", T("2 is not a perfect square.", "2 no es un cuadrado perfecto.")), num(radVis(1, 3), radVoz(1, 3), "√3", "I"),
  num("π", "pi", "π", "I", T("The decimals of π do not end or repeat.", "Los decimales de π no terminan ni se repiten.")),
  num("−" + radVis(1, 5), T("negative square root of 5", "menos raíz cuadrada de 5"), "−√5", "I"), num(radVis(1, 10), radVoz(1, 10), "√10", "I"),
  num("0.1010010001…", T("0.1010010001, with more and more zeros", "0.1010010001, con cada vez más ceros"), "0.1010010001…", "I", T("It has an order, but no fixed group that repeats.", "Tiene un orden, pero ningún grupo fijo que se repita."))
];
function lista(cs, una){ return yLista(cs.map(function(c){ return una ? CONJ1[c] : CONJ[c].toLowerCase(); })); }
function diagramaSVG(n){
  var dentro = n ? PERTENECE[n.t] : [];
  function caja(id, x, yy, w, h, ex, ey){
    var on = dentro.indexOf(id) >= 0;
    return '<rect x="' + x + '" y="' + yy + '" width="' + w + '" height="' + h + '" rx="14" fill="' + (on ? "#e0f2f1" : "#ffffff") + '" stroke="' + (on ? "#004d40" : "#9e9e9e") +
           '" stroke-width="' + (on ? 4 : 2) + '"/><text x="' + ex + '" y="' + ey + '" font-size="16" font-weight="700" fill="' + (on ? "#00352c" : "#424242") + '">' + CONJ[id] + "</text>";
  }
  var s = '<svg class="diagrama" viewBox="0 0 560 330" role="img" aria-label="' +
          (n ? T("Diagram of the sets: " + n.txt + " belongs to these sets: " + lista(dentro), "Diagrama de conjuntos: " + n.txt + " pertenece a estos conjuntos: " + lista(dentro)) : T("Diagram of the sets of the real numbers", "Diagrama de conjuntos de los números reales")) + '">';
  s += caja("R", 5, 5, 550, 320, 20, 28) + caja("Q", 22, 42, 350, 270, 36, 64) + caja("Z", 40, 80, 314, 200, 54, 102) + caja("N", 58, 118, 278, 118, 72, 140) + caja("I", 388, 42, 150, 270, 400, 64);
  if (n){
    var pos = {N: [197, 195], Z: [197, 262], Q: [197, 300], I: [463, 185]}[n.t];
    s += '<text x="' + pos[0] + '" y="' + pos[1] + '" text-anchor="middle" font-size="24" font-weight="700" fill="#0d47a1">' + n.txt + "</text>";
  }
  return s + "</svg>";
}
var CL = {n: null, resuelto: false, intentos: 0, cola: []};
function nuevoCL(){
  if (!CL.cola.length) CL.cola = baraja(NUMEROS);
  CL.n = CL.cola.shift(); CL.resuelto = false; CL.intentos = 0;
  $("cl-num").innerHTML = CL.n.html;
  var ops = $("cl-opciones"); ops.innerHTML = "";
  ["N", "Z", "Q", "I"].forEach(function(c){
    var b = document.createElement("button"); b.type = "button"; b.className = "eleccion"; b.textContent = CONJ[c];
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function(){ respondeCL(c, b); });
    ops.appendChild(b);
  });
  $("cl-fb").className = "fb"; $("cl-fb").innerHTML = "";
  $("cl-diagrama").innerHTML = diagramaSVG(null);
}
function respondeCL(c, b){
  if (CL.resuelto) return;
  var n = CL.n, fb = $("cl-fb");
  Array.prototype.forEach.call($("cl-opciones").children, function(x){ x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
  var resumen = n.nota + " " + T("It belongs to these sets: " + lista(PERTENECE[n.t]) + ".", "Pertenece a: " + lista(PERTENECE[n.t]) + ".");
  CL.intentos++;
  if (c === n.t){
    CL.resuelto = true; fb.className = "fb bien";
    fb.innerHTML = TX.bien + T("The smallest set is the " + CONJ[c].toLowerCase() + " numbers. ", "El conjunto más pequeño es el de los " + CONJ[c].toLowerCase() + ". ") + resumen;
    $("cl-diagrama").innerHTML = diagramaSVG(n);
  } else if (CL.intentos >= 2){
    CL.resuelto = true; fb.className = "fb mal";
    fb.innerHTML = TX.asi + T("The smallest set is the " + CONJ[n.t].toLowerCase() + " numbers. ", "El conjunto más pequeño es el de los " + CONJ[n.t].toLowerCase() + ". ") + resumen;
    $("cl-diagrama").innerHTML = diagramaSVG(n);
  } else {
    fb.className = "fb pista";
    var pista = c === "I" ? T("This number can be written as a fraction.", "Este número sí se puede escribir como fracción.") :
               (n.t === "I" ? T("This number cannot be written as a fraction of integers.", "Este número no se puede escribir como fracción de enteros.") :
               (PERTENECE[n.t].indexOf(c) >= 0 ? T("It does belong to that set, but there is a smaller set that also contains it.", "Sí pertenece a ese conjunto, pero hay uno más pequeño que también lo contiene.") : T("It does not belong to that set.", "No pertenece a ese conjunto.")));
    fb.innerHTML = TX.todavia + pista + TX.unoMas;
  }
}

/* Practice 1 · check boxes, two tries */
var P1 = {primero: 0, pista: 0, total: 0, n: null, resuelta: false, intentos: 0, cola: []};
function pintaP1(){
  if (!P1.cola.length) P1.cola = baraja(NUMEROS);
  P1.n = P1.cola.shift(); P1.resuelta = false; P1.intentos = 0;
  $("p1-enun").innerHTML = T("Which sets does ", "¿A qué conjuntos pertenece ") + P1.n.html + T(" belong to? Check all that apply.", "? Marque todos los que correspondan.");
  var cont = $("p1-casillas"); cont.innerHTML = "";
  ["N", "Z", "Q", "I", "R"].forEach(function(c){
    var lab = document.createElement("label"); lab.className = "casilla";
    lab.innerHTML = '<input type="checkbox" value="' + c + '"> ' + CONJ[c];
    cont.appendChild(lab);
  });
  $("p1-comprobar").disabled = false;
  $("p1-fb").className = "fb"; $("p1-fb").innerHTML = "";
}
function compruebaP1(){
  if (P1.resuelta) return;
  var cajas = $("p1-casillas").querySelectorAll("input"), marcadas = [], fb = $("p1-fb");
  cajas.forEach(function(x){ if (x.checked) marcadas.push(x.value); });
  if (!marcadas.length){ fb.className = "fb pista"; fb.innerHTML = T("Check at least one set.", "Marque al menos un conjunto."); return; }
  P1.intentos++;
  var bien = PERTENECE[P1.n.t], ok = marcadas.length === bien.length && bien.every(function(c){ return marcadas.indexOf(c) >= 0; });
  var falta = bien.filter(function(c){ return marcadas.indexOf(c) < 0; }), sobra = marcadas.filter(function(c){ return bien.indexOf(c) < 0; });
  if (!ok && P1.intentos < 2){
    fb.className = "fb pista";
    fb.innerHTML = TX.todavia + (falta.length ? T("It belongs to more sets than the ones you checked. ", "Pertenece a más conjuntos de los que marcó. ") : "") + (sobra.length ? T("You checked at least one set it does not belong to. ", "Marcó al menos un conjunto al que no pertenece. ") : "") +
      (falta.indexOf("R") >= 0 ? T("Remember that all of these numbers are real.", "Recuerde que todos estos números son reales.") : T("Remember: a number in a set also belongs to every set around it.", "Recuerde: un número de un conjunto pertenece también a todos los que lo rodean.")) + TX.unoMas;
    return;
  }
  P1.resuelta = true; P1.total++;
  cajas.forEach(function(x){
    var debe = bien.indexOf(x.value) >= 0;
    x.disabled = true;
    if (debe) x.parentNode.classList.add("correcta");
    else if (x.checked) x.parentNode.classList.add("incorrecta");
  });
  var frase = T("It belongs to these sets: " + lista(bien) + ". ", "Pertenece a los " + lista(bien) + ". ") + P1.n.nota;
  if (ok){ if (P1.intentos === 1) P1.primero++; else P1.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + frase + " <em>" + elige(P1.intentos === 1 ? ELOGIO : ELOGIO2) + "</em>"; }
  else { fb.className = "fb mal"; fb.innerHTML = TX.asi + frase + TX.nuevo; }
  $("p1-comprobar").disabled = true;
  $("p1-marcador").textContent = TX.resueltos(P1.primero + P1.pista, P1.primero, P1.total);
}

/* ============ MODULE 2 · fractions and roots ============ */
function divisionLarga(p, q){
  var ent = Math.floor(p / q), rr = p % q, cifras = "", vistos = {}, i = 0;
  while (rr !== 0 && !(rr in vistos) && i < 200){ vistos[rr] = i; rr *= 10; cifras += Math.floor(rr / q); rr = rr % q; i++; }
  if (rr === 0) return {ent: ent, noRep: cifras, per: ""};
  var k = vistos[rr]; return {ent: ent, noRep: cifras.slice(0, k), per: cifras.slice(k)};
}
function pintaFX(){
  var pt = $("fx-p").value.trim(), qt = $("fx-q").value.trim(), sal = $("fx-salida");
  if (!/^\d+$/.test(pt) || !/^\d+$/.test(qt) || +qt < 1 || +qt > 999 || +pt > 99999){ sal.innerHTML = T("Type a whole-number numerator from 0 to 99999 and a whole-number denominator from 1 to 999.", "Escriba un numerador entero de 0 a 99999 y un denominador entero de 1 a 999."); return; }
  var p = +pt, q = +qt, d = divisionLarga(p, q), h;
  if (!d.per){
    var dec = d.ent + (d.noRep ? "." + d.noRep : "");
    h = '<div class="linea grande">' + fracHTML(p, q) + " = " + dec + '</div><div class="linea veredicto">' + T("The decimal ends: it is a rational number.", "El decimal termina: es un número racional.") + "</div>";
  } else {
    var vis = d.ent + "." + d.noRep + '<span class="periodo">' + d.per + "</span>";
    var largo = d.ent + "." + d.noRep + d.per + d.per + (d.per.length < 4 ? d.per : "") + "…";
    h = '<div class="linea grande">' + fracHTML(p, q) + " = " + envuelve(vis, d.ent + T(" point ", " punto ") + (d.noRep ? d.noRep + T(", and then ", ", y luego ") : "") + T("the repeating group ", "el periodo ") + d.per.split("").join(" ")) + "</div>" +
        '<div class="linea">' + T("That is, " + largo + " The group " + d.per + " repeats forever", "Es decir, " + largo + " El grupo " + d.per + " se repite sin fin") + (d.per.length > 6 ? T(" (its repeating group has " + d.per.length + " digits)", " (su periodo tiene " + d.per.length + " cifras)") : "") + ".</div>" +
        '<div class="linea veredicto">' + T("The decimal repeats: it is a rational number.", "El decimal se repite: es un número racional.") + "</div>";
  }
  sal.innerHTML = h;
}
function pintaRX(){
  var tx = $("rx-n").value.trim(), sal = $("rx-salida");
  if (!/^\d+$/.test(tx) || +tx > 10000){ sal.innerHTML = T("Type a whole number from 0 to 10000.", "Escriba un número entero de 0 a 10000."); return; }
  var n = +tx, s = Math.sqrt(n);
  if (esCuadrado(n)) sal.innerHTML = '<div class="linea grande">' + radHTML(1, n) + " = " + Math.round(s) + '</div><div class="linea veredicto">' + T(n + " is a perfect square: the root is exact and the number is rational (" + Math.round(s) + " = " + Math.round(s) + "/1).", n + " es un cuadrado perfecto: la raíz es exacta y el número es racional (" + Math.round(s) + " = " + Math.round(s) + "/1).") + "</div>";
  else sal.innerHTML = '<div class="linea grande">' + radHTML(1, n) + " ≈ " + s.toFixed(10) + '…</div><div class="linea veredicto">' + T(n + " is not a perfect square: the decimals do not end or repeat, so it is irrational.", n + " no es un cuadrado perfecto: los decimales no terminan ni se repiten, así que es irracional.") + "</div>";
}
function genRacional(){
  var tp = aleatorio(1, 12), h, c, exp;
  if (tp === 1){ var q = elige([3, 7, 9, 11, 12, 13]), p = aleatorio(1, q - 1); h = fracHTML(p, q); c = "R"; exp = T("It is a fraction of integers: its decimal repeats, but it is rational.", "Es una fracción de enteros: su decimal se repite, pero es racional."); }
  else if (tp === 2){ var d = (aleatorio(1, 999) / 1000).toString(); h = d; c = "R"; exp = T(d + " is a decimal that ends: it can be written as a fraction.", d + " es un decimal que termina: se puede escribir como fracción."); }
  else if (tp === 3){ var per = String(aleatorio(12, 98)); h = periodicoHTML("0", "", per); c = "R"; exp = T("The group " + per + " repeats: it is a repeating decimal, so it is rational.", "El grupo " + per + " se repite: es un decimal periódico, y por eso racional."); }
  else if (tp === 4){ var s = aleatorio(2, 15); h = radHTML(1, s * s); c = "R"; exp = T((s * s) + " is a perfect square: the root is " + s + ", a rational number.", (s * s) + " es un cuadrado perfecto: la raíz es " + s + ", un número racional."); }
  else if (tp === 5 || tp === 6){ var n; do { n = aleatorio(2, 99); } while (esCuadrado(n)); h = (tp === 6 ? envuelve("−" + radVis(1, n), T("negative ", "menos ") + radVoz(1, n)) : radHTML(1, n)); c = "I"; exp = T(n + " is not a perfect square: the root is irrational.", n + " no es un cuadrado perfecto: la raíz es irracional."); }
  else if (tp === 7){ h = envuelve("π", "pi"); c = "I"; exp = T("The decimals of π do not end or repeat.", "Los decimales de π no terminan ni se repiten."); }
  else if (tp === 8){ h = fracHTML(22, 7); c = "R"; exp = T("22/7 is an approximation of π, but it is a fraction of integers: it is rational.", "22/7 es una aproximación de π, pero es una fracción de enteros: es racional."); }
  else if (tp === 9){ h = "3.14"; c = "R"; exp = T("3.14 is a decimal that ends (= 314/100). It looks like π, but it is rational.", "3.14 es un decimal que termina (= 314/100). Se parece a π, pero es racional."); }
  else if (tp === 10){ h = envuelve("0.1010010001…", T("0.1010010001, with more and more zeros", "0.1010010001, con cada vez más ceros")); c = "I"; exp = T("It follows an order, but no fixed group repeats: it is not a repeating decimal, so it is irrational.", "Sigue un orden, pero ningún grupo fijo se repite: no es periódico, así que es irracional."); }
  else if (tp === 11){ var m = elige([4, 9, 16, 25, 36]); h = envuelve('<span class="rad">√<span class="rc">−' + m + "</span></span>", T("square root of negative " + m, "raíz cuadrada de menos " + m)); c = "X"; exp = T("No real number squared gives a negative result: this root is not a real number.", "Ningún número real al cuadrado da un resultado negativo: esta raíz no es un número real."); }
  else { h = envuelve('<span class="rad">√<span class="rc">' + fracVis(4, 9) + "</span></span>", T("square root of 4 ninths", "raíz cuadrada de 4 novenos")); c = "R"; exp = T("√(4/9) = 2/3, because (2/3)² = 4/9. It is rational.", "√(4/9) = 2/3, porque (2/3)² = 4/9. Es racional."); }
  return {enun: T("How do you classify ", "¿Cómo se clasifica ") + h + "?", enOrden: true,
    opciones: [{html: T("Rational", "Racional"), clave: "R"}, {html: T("Irrational", "Irracional"), clave: "I"}, {html: T("Not a real number", "No es un número real"), clave: "X"}],
    correcta: c, porClave: {}, pista: T("Ask yourself: can it be written as a fraction of integers? Does its decimal end or repeat?", "Pregúntese: ¿se puede escribir como fracción de enteros? ¿Su decimal termina o se repite?"), bien: exp, mal: exp};
}

/* ============ MODULE 3 · the number line ============ */
var RE = {v: 0, txt: "", html: "", n: 0, resuelto: false, intentos: 0, primero: 0, pista: 0, total: 0};
function nuevoRE(){
  if (Math.random() < 0.15){ RE.v = Math.PI; RE.txt = "π"; RE.html = envuelve("π", "pi"); RE.n = 0; }
  else { var n; do { n = aleatorio(2, 48); } while (esCuadrado(n)); RE.v = Math.sqrt(n); RE.n = n; RE.txt = "√" + n; RE.html = radHTML(1, n); }
  RE.resuelto = false; RE.intentos = 0;
  $("re-num").innerHTML = RE.html;
  $("re-pos").value = 0; $("re-pos").disabled = false; $("re-comprobar").disabled = false;
  $("re-fb").className = "fb"; $("re-fb").innerHTML = "";
  pintaRE();
}
function pintaRE(){
  var x = parseFloat($("re-pos").value), marcas = [{v: x, txt: T("your mark", "su marca"), color: "#0d47a1"}];
  if (RE.resuelto) marcas.push({v: RE.v, txt: RE.txt + " ≈ " + aprox(RE.v, 2), color: "#00352c", alto: true});
  $("re-val").textContent = x.toFixed(2);
  $("re-pos").setAttribute("aria-valuetext", x.toFixed(2));
  $("re-recta").innerHTML = rectaSVG(0, 7, 0.5, marcas, T("Number line from 0 to 7. Your mark is at " + x.toFixed(2), "Recta numérica de 0 a 7. Su marca está en " + x.toFixed(2)) + (RE.resuelto ? T(". The real value is " + aprox(RE.v, 2), ". El valor real es " + aprox(RE.v, 2)) : ""));
}
function compruebaRE(){
  if (RE.resuelto) return;
  var x = parseFloat($("re-pos").value), err = Math.abs(x - RE.v), a = Math.floor(RE.v), fb = $("re-fb");
  var razon = RE.n ? (a * a) + " &lt; " + RE.n + " &lt; " + ((a + 1) * (a + 1)) + T(", so ", ", así que ") + RE.html + T(" is between " + a + " and " + (a + 1) + ".", " está entre " + a + " y " + (a + 1) + ".") : T("π ≈ 3.14, a little more than 3.", "π ≈ 3.14, un poco más que 3.");
  RE.intentos++;
  if (err > 0.15 && RE.intentos < 2){
    fb.className = "fb pista";
    fb.innerHTML = TX.todavia + (Math.floor(x) !== a ? (RE.n ? T("Look for the perfect squares around " + RE.n + ": which whole numbers is the root between?", "Busque los cuadrados perfectos que rodean a " + RE.n + ": ¿entre qué enteros está la raíz?") : T("π is a little more than 3.", "π es un poco más que 3.")) : T("The whole numbers are right; now move closer: is it nearer " + a + " or " + (a + 1) + "?", "Los enteros están bien; ahora afine: ¿está más cerca del " + a + " o del " + (a + 1) + "?")) + TX.unoMas;
    return;
  }
  RE.resuelto = true; RE.total++;
  if (err <= 0.15){ if (RE.intentos === 1) RE.primero++; else RE.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + T("Well placed! ", "¡Bien ubicado! ") + RE.html + " ≈ " + aprox(RE.v, 2) + ". " + razon; }
  else { fb.className = "fb mal"; fb.innerHTML = TX.asi + RE.html + " ≈ " + aprox(RE.v, 2) + T("; your mark was " + aprox(err, 2) + " away. ", "; su marca quedó a " + aprox(err, 2) + " de distancia. ") + razon; }
  $("re-pos").disabled = true; $("re-comprobar").disabled = true;
  $("re-marcador").textContent = TX.resueltos(RE.primero + RE.pista, RE.primero, RE.total);
  pintaRE();
}
function genMayor(){
  var tp = aleatorio(1, 4), A, B, vA, vB, exp;
  if (tp === 1){ var n = aleatorio(2, 80), k = Math.round(Math.sqrt(n)) + elige([-1, 0, 0, 1]); if (k < 1) k = 1;
    A = radHTML(1, n); B = String(k); vA = n; vB = k * k; exp = T("Compare the squares: (√" + n + ")² = " + n + " and " + k + "² = " + (k * k) + ".", "Compare los cuadrados: (√" + n + ")² = " + n + " y " + k + "² = " + (k * k) + "."); }
  else if (tp === 2){ var m = elige([8, 9, 10, 11, 12]); A = radHTML(1, m); B = envuelve("π", "pi"); vA = Math.sqrt(m); vB = Math.PI;
    exp = radHTML(1, m) + " ≈ " + aprox(Math.sqrt(m), 2) + T(" and π ≈ 3.14.", " y π ≈ 3.14."); }
  else if (tp === 3){ var a1 = aleatorio(2, 60), a2 = aleatorio(2, 60); while (a2 === a1) a2 = aleatorio(2, 60);
    A = radHTML(1, a1); B = radHTML(1, a2); vA = a1; vB = a2; exp = T("Of two square roots, the one with the greater radicand is greater.", "Entre dos raíces cuadradas, es mayor la del radicando mayor."); }
  else { var nn; do { nn = aleatorio(2, 60); } while (esCuadrado(nn)); var d = (Math.round(Math.sqrt(nn) * 10) / 10 + elige([-0.1, 0.1])).toFixed(1);
    A = radHTML(1, nn); B = d; vA = nn; vB = parseFloat(d) * parseFloat(d);
    exp = T("Square the decimal: " + d + "² = " + (parseFloat(d) * parseFloat(d)).toFixed(2) + ", and compare it with " + nn + ".", "Eleve al cuadrado el decimal: " + d + "² = " + (parseFloat(d) * parseFloat(d)).toFixed(2) + ", y compárelo con " + nn + "."); }
  if (Math.random() < 0.5){ var x = A; A = B; B = x; var y2 = vA; vA = vB; vB = y2; }
  var clave = Math.abs(vA - vB) < 1e-9 ? "=" : (vA > vB ? "A" : "B");
  return {enun: T("Which is greater: ", "¿Cuál es mayor: ") + A + T(" or ", " o ") + B + "?", enOrden: true,
    opciones: [{html: A, clave: "A"}, {html: B, clave: "B"}, {html: T("They are equal", "Son iguales"), clave: "="}],
    correcta: clave, porClave: {}, pista: T("Compare the squares of the two numbers, or approximate each one.", "Compare los cuadrados de los dos números o aproxime cada uno."), bien: exp, mal: exp};
}

/* ============ MODULE 4 · repeating decimals to fractions ============ */
function p10(k){ return Math.pow(10, k); }
function aFraccion(d){
  var E = +d.ent, P = +d.per, L = d.per.length;
  if (!d.noRep){ var den = p10(L) - 1; return {num: E * den + P, den: den}; }
  var A = +d.noRep;
  return {num: (E * p10(L + 1) + A * p10(L) + P) - (10 * E + A), den: p10(L + 1) - 10};
}
function perVis(ent, noRep, per){ return periodicoHTML(String(ent), noRep, per); }
var PE = {lista: [{ent: "0", noRep: "", per: "6"}, {ent: "0", noRep: "", per: "2"}, {ent: "0", noRep: "", per: "27"}, {ent: "0", noRep: "1", per: "6"},
                  {ent: "0", noRep: "8", per: "3"}, {ent: "0", noRep: "", per: "45"}, {ent: "1", noRep: "", per: "3"}], pasos: [], visto: 0};
function etiquetaPE(d){ return d.ent + "." + d.noRep + d.per + d.per + d.per + "…"; }
function llenaPE(){
  var sel = $("pe-sel"); sel.innerHTML = "";
  PE.lista.forEach(function(d, i){ var o = document.createElement("option"); o.value = i; o.textContent = etiquetaPE(d); sel.appendChild(o); });
}
function preparaPE(){
  var d = PE.lista[+$("pe-sel").value], L = d.per.length, F = aFraccion(d), rr = reduce(F.num, F.den), E = +d.ent, P = +d.per;
  var desp = T("Solve: x = ", "Se despeja: x = ") + fracHTML(F.num, F.den) + (rr.q !== F.den ? T(", which simplifies to ", ", que se simplifica a ") + fracHTML(rr.p, rr.q) : "") + ".";
  PE.pasos = []; PE.visto = 0;
  $("pe-expr").innerHTML = '<span class="grande">' + perVis(d.ent, d.noRep, d.per) + "</span>";
  PE.pasos.push(T("Call the number x: x = ", "Se llama x al número: x = ") + perVis(d.ent, d.noRep, d.per));
  if (!d.noRep){
    var m = p10(L);
    PE.pasos.push(T("The repeating group has " + L + (L === 1 ? " digit" : " digits") + ", so multiply by " + m + ": ", "El periodo tiene " + L + (L === 1 ? " cifra" : " cifras") + ", así que se multiplica por " + m + ": ") + m + "x = " + perVis(E * m + P, "", d.per));
    PE.pasos.push(T("Subtract the first equation from the second. The repeating part disappears: ", "Se resta la primera igualdad de la segunda. La parte que se repite desaparece: ") + m + "x − x = " + (m - 1) + "x = " + F.num + ".");
  } else {
    var A = +d.noRep, m2 = p10(L + 1);
    PE.pasos.push(T("There is one digit before the repeating group. Multiply by 10 to move it to the left of the point: ", "Hay una cifra antes del periodo. Se multiplica por 10 para dejarla a la izquierda del punto: ") + "10x = " + perVis(10 * E + A, "", d.per));
    PE.pasos.push(T("Multiply by " + m2 + " to move a full repeating group too: ", "Se multiplica por " + m2 + " para correr también un periodo completo: ") + m2 + "x = " + perVis(E * m2 + A * p10(L) + P, "", d.per));
    PE.pasos.push(T("Subtract the two equations, and the repeating part disappears: ", "Se restan las dos igualdades y la parte que se repite desaparece: ") + m2 + "x − 10x = " + (m2 - 10) + "x = " + F.num + ".");
  }
  PE.pasos.push(desp);
  PE.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + perVis(d.ent, d.noRep, d.per) + " = " + fracHTML(rr.p, rr.q) + T(". It is a fraction, so the number is rational.", ". Es una fracción, así que el número es racional.") + "</span>");
  pintaPE();
}
function pintaPE(){
  $("pe-pasos").innerHTML = PE.pasos.slice(0, PE.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === PE.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("pe-sig"); b.disabled = PE.visto >= PE.pasos.length; $("pe-todo").disabled = b.disabled;
  b.textContent = PE.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function periodicoAzar(){
  var u = Math.random();
  if (u < 0.4) return {ent: "0", noRep: "", per: String(aleatorio(1, 8))};
  if (u < 0.75){ var a, b; do { a = aleatorio(0, 9); b = aleatorio(0, 9); } while (a === b || (a === 9 && b === 9)); return {ent: "0", noRep: "", per: "" + a + b}; }
  var x, y; do { x = aleatorio(1, 9); y = aleatorio(1, 8); } while (x === y);
  return {ent: "0", noRep: String(x), per: String(y)};
}
function azarPE(){ PE.lista.push(periodicoAzar()); llenaPE(); $("pe-sel").value = PE.lista.length - 1; preparaPE(); }
function opFrac(p, q){ var rr = reduce(p, q); return {html: fracHTML(rr.p, rr.q), clave: "f" + rr.p + "/" + rr.q}; }
function genElegirFrac(){
  var d = periodicoAzar(), F = aFraccion(d), rr = reduce(F.num, F.den), L = d.per.length, o = [], pc = {}, usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opFrac(F.num, F.den));
  if (!d.noRep){
    mete(opFrac(+d.per, p10(L)), T("That fraction is the decimal 0." + d.per + " that ends, not the one that repeats.", "Esa fracción es el decimal que termina 0." + d.per + ", no el que se repite."));
    mete(opFrac(+d.per + 1, p10(L) - 1), T("The numerator is the repeating group itself: " + d.per + ".", "El numerador es el mismo periodo: " + d.per + "."));
    mete(opFrac(+d.per, p10(L + 1) - 1), T("The denominator depends on how many digits repeat: " + (p10(L) - 1) + ".", "El denominador depende de cuántas cifras tiene el periodo: " + (p10(L) - 1) + "."));
  } else {
    mete(opFrac(+(d.noRep + d.per), 99), T("Only the second digit repeats: it is not a two-digit repeating group.", "Solo se repite la segunda cifra: no es un periodo de dos cifras."));
    mete(opFrac(+(d.noRep + d.per), 100), T("That fraction is the decimal 0." + d.noRep + d.per + " that ends.", "Esa fracción es el decimal que termina 0." + d.noRep + d.per + "."));
    mete(opFrac(+d.per, 9), T("That fraction is 0." + d.per + d.per + "…: you still need the digit " + d.noRep + " before the repeating group.", "Esa fracción es 0." + d.per + d.per + "…: falta tener en cuenta la cifra " + d.noRep + " antes del periodo."));
  }
  return {enun: T("What fraction is equal to ", "¿Qué fracción equivale a ") + perVis(d.ent, d.noRep, d.per) + "?",
    opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("With the procedure: x = ", "Con el procedimiento: x = ") + fracHTML(F.num, F.den) + (rr.q !== F.den ? " = " + fracHTML(rr.p, rr.q) : "") + ".",
    mal: T("The fraction is ", "La fracción es ") + fracHTML(rr.p, rr.q) + T(". Review the procedure in the step-by-step panel above.", ". Revise el procedimiento en el paso a paso de arriba.")};
}
function genEscribeFrac(){
  var d = periodicoAzar(), F = aFraccion(d), rr = reduce(F.num, F.den);
  return {enun: T("Convert ", "Convierta ") + perVis(d.ent, d.noRep, d.per) + T(" to a fraction in simplest form.", " en una fracción simplificada."),
    solucion: perVis(d.ent, d.noRep, d.per) + " = " + fracHTML(F.num, F.den) + (rr.q !== F.den ? " = " + fracHTML(rr.p, rr.q) : "") + ".",
    evalua: function(txt){
      var f = leeFraccion(txt);
      if (!f) return {estado: "invalido", msg: T("Write the fraction with a slash, for example 2/3.", "Escriba la fracción con una barra, por ejemplo 2/3.")};
      if (f.p * rr.q === rr.p * f.q){
        if (mcd(f.p, f.q) === 1) return {estado: "bien", msg: ""};
        return {estado: "mal", msg: T("It has the same value, but it can still be simplified.", "Tiene el mismo valor, pero todavía se puede simplificar.")};
      }
      return {estado: "mal", msg: d.noRep ? T("There is one digit before the repeating group: use 10x and " + p10(d.per.length + 1) + "x.", "Hay una cifra antes del periodo: use 10x y " + p10(d.per.length + 1) + "x.") : T("The repeating group has " + d.per.length + (d.per.length === 1 ? " digit: multiply by 10." : " digits: multiply by 100."), "El periodo tiene " + d.per.length + (d.per.length === 1 ? " cifra: multiplique por 10." : " cifras: multiplique por 100."))};
    }};
}

/* ============ Start ============ */
$("cl-nuevo").addEventListener("click", nuevoCL);
CL.cola = [NUMEROS[0], NUMEROS[16]].concat(baraja(NUMEROS));
nuevoCL();
$("p1-comprobar").addEventListener("click", compruebaP1);
$("p1-nuevo").addEventListener("click", pintaP1);
pintaP1();
["fx-p", "fx-q"].forEach(function(id){ $(id).addEventListener("input", pintaFX); });
pintaFX();
$("rx-n").addEventListener("input", pintaRX);
pintaRX();
OMR("p2", genRacional);
$("re-pos").addEventListener("input", pintaRE);
$("re-comprobar").addEventListener("click", compruebaRE);
$("re-nuevo").addEventListener("click", nuevoRE);
nuevoRE();
OMR("p3", genMayor);
llenaPE();
$("pe-sel").addEventListener("change", preparaPE);
$("pe-sig").addEventListener("click", function(){ if (PE.visto < PE.pasos.length){ PE.visto++; pintaPE(); } });
$("pe-todo").addEventListener("click", function(){ PE.visto = PE.pasos.length; pintaPE(); });
$("pe-azar").addEventListener("click", azarPE);
preparaPE();
OMR("p4", genElegirFrac);
creaPracticaLibre("p5", genEscribeFrac);
'''

def campo(i, etiqueta, valor):
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="text" inputmode="numeric" class="corto" id="{i}" value="{valor}"></div>'

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("classify", "clasificar"), t("The real number system", "El sistema de los números reales"),
      f'''      <p>{t("The real numbers are organized in sets that fit inside one another: the <strong>natural numbers</strong> (1, 2, 3, …) are inside the <strong>integers</strong> (…, −2, −1, 0, 1, 2, …), and these are inside the <strong>rational numbers</strong> (the ones you can write as a fraction). Apart from them are the <strong>irrational numbers</strong>. Together they make up the <strong>real numbers</strong>.", "Los números reales se organizan en conjuntos que se contienen unos a otros: los <strong>naturales</strong> (1, 2, 3, …) están dentro de los <strong>enteros</strong> (…, −2, −1, 0, 1, 2, …), y estos dentro de los <strong>racionales</strong> (los que se pueden escribir como fracción). Aparte están los <strong>irracionales</strong>. Juntos forman los <strong>reales</strong>.")}</p>
      <h3>{t("Where does this number live?", "¿Dónde vive este número?")}</h3>
      <p>{t("Choose the smallest set that contains the number. Then the diagram shows every set it belongs to.", "Elija el conjunto más pequeño que contiene al número. Después el diagrama muestra todos los conjuntos a los que pertenece.")}</p>
      <div class="panel">
        <div class="estado"><span class="grande" id="cl-num"></span></div>
        <div class="elecciones" id="cl-opciones" style="justify-content:center;"></div>
        <div class="fb" id="cl-fb" role="status"></div>
        <div id="cl-diagrama"></div>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn-sec" id="cl-nuevo">{t("Another number", "Otro número")}</button></div>
      </div>
      <div class="caja-tip"><strong>{t("How to read the diagram:", "Cómo leer el diagrama:")}</strong> {t("each number belongs to the smallest set that contains it and to every set around it. 3 is natural, but it is also an integer, rational, and real. On the other hand, √2 is irrational and real, but it is not rational or an integer.", "cada número pertenece al conjunto más pequeño que lo contiene y a todos los que lo rodean. El 3 es natural, pero también entero, racional y real. En cambio, √2 es irracional y real, pero no es racional ni entero.")}</div>
      <h3>{t("Practice: check every set it belongs to", "Practique: marque todos los conjuntos a los que pertenece")}</h3>
      <div class="practica" id="p1">
        <div class="enun" id="p1-enun"></div>
        <div class="casillas" id="p1-casillas"></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="p1-comprobar">Check</button>
          <button type="button" class="btn-sec" id="p1-nuevo">{t("Another number", "Otro número")}</button>
        </div>
        <div class="fb" id="p1-fb" role="status"></div>
        <p class="marcador" id="p1-marcador"></p>
      </div>'''),
     (t("rational-irrational", "racional-irracional"), t("Rational or irrational?", "¿Racional o irracional?"),
      f'''      <p>{t("A number is <strong>rational</strong> if you can write it as a fraction of two integers. Its decimal <strong>ends</strong> (like 0.75) or <strong>repeats</strong> a pattern (like 0.333…). A number is <strong>irrational</strong> if its decimal does not end and does not repeat, like √2 or π.", "Un número es <strong>racional</strong> si se puede escribir como fracción de dos enteros. Su decimal <strong>termina</strong> (como 0.75) o <strong>se repite</strong> en un patrón (como 0.333…). Un número es <strong>irracional</strong> si su decimal no termina y no se repite, como √2 o π.")}</p>
      <h3>{t("Fraction explorer", "Explorador de fracciones")}</h3>
      <p>{t("Every fraction gives a decimal that ends or repeats. Check it with long division: the repeating group has a bar over it.", "Toda fracción da un decimal que termina o que se repite. Compruébelo con la división de siempre: el periodo aparece con una raya encima.")}</p>
      <div class="panel"><div class="campos">
        {campo("fx-p", t("Numerator", "Numerador"), 1)}
        {campo("fx-q", t("Denominator (1 to 999)", "Denominador (de 1 a 999)"), 6)}
      </div></div>
{P.salida("fx-salida")}
      <h3>{t("Root explorer", "Explorador de raíces")}</h3>
      <p>{t("A root is rational only if the radicand is a perfect square.", "Una raíz es racional solo si el radicando es un cuadrado perfecto.")}</p>
      <div class="panel"><div class="campos">{campo("rx-n", t("Radicand (0 to 10000)", "Radicando (de 0 a 10000)"), 9)}</div></div>
{P.salida("rx-salida")}
{P.atencion(t("Careful with roots:", "Cuidado con las raíces:"), t("not every root is irrational. √9 = 3 is rational, because 9 is a perfect square. And be careful with 22/7 too: it is a good approximation of π, but it is a fraction, so it is rational.", "no toda raíz es irracional. √9 = 3 es racional, porque 9 es un cuadrado perfecto. Y cuidado también con 22/7: es una buena aproximación de π, pero es una fracción, así que es racional."))}
{B.om("p2", t("Practice: rational or irrational?", "Practique: ¿racional o irracional?"))}'''),
     (t("number-line", "recta"), t("Placing irrational numbers on the number line", "Ubicar irracionales en la recta numérica"),
      f'''      <p>{t("Even though an irrational number has no exact decimal, it has a precise place on the number line. To place it, trap it between two whole numbers with the perfect squares, then narrow it down with its decimal approximation.", "Aunque un irracional no tenga un decimal exacto, ocupa un lugar preciso en la recta numérica. Para ubicarlo se acorrala entre dos enteros con los cuadrados perfectos y se afina con la aproximación decimal.")}</p>
      <h3>{t("Place the number", "Coloque el número")}</h3>
      <p>{t("Move the slider to where you think the number is and press “Check.” You can also use the arrow keys.", "Mueva el deslizador hasta donde crea que está el número y pulse «Comprobar». También puede usar las flechas del teclado.")}</p>
      <div class="panel">
        <div class="estado">{t("Place", "Ubique")} <span class="grande" id="re-num"></span></div>
        <div id="re-recta"></div>
        <div class="campo">
          <label for="re-pos">{t("Position on the number line:", "Posición en la recta:")} <span id="re-val">0.00</span></label>
          <input type="range" id="re-pos" min="0" max="7" step="0.05" value="0">
        </div>
        <div class="fila-btn">
          <button type="button" class="btn" id="re-comprobar">Check</button>
          <button type="button" class="btn-sec" id="re-nuevo">{t("Another number", "Otro número")}</button>
        </div>
        <div class="fb" id="re-fb" role="status"></div>
        <p class="marcador" id="re-marcador"></p>
      </div>
{B.om("p3", t("Practice: which is greater?", "Practique: ¿cuál es mayor?"))}'''),
     (t("repeating", "periodicos"), t("Repeating decimals to fractions", "Decimales periódicos a fracciones"),
      f'''      <p>{t("A repeating decimal is rational because you can always write it as a fraction. The trick is to multiply by a power of 10 that shifts the repeating group and then subtract, so the repeating part disappears.", "Un decimal periódico es racional porque siempre se puede escribir como fracción. El truco es multiplicar por una potencia de 10 que corra el periodo y restar, para que la parte que se repite desaparezca.")}</p>
      <h3>{t("The procedure, step by step", "El procedimiento, paso a paso")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="pe-sel">{t("Repeating decimal", "Decimal periódico")}</label><select id="pe-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="pe-sig"></button><button type="button" class="btn-sec" id="pe-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="pe-azar">{t("Another one at random", "Otro al azar")}</button></div>
      </div>
      <div class="fraccion-grande" id="pe-expr"></div>
      <div class="pasos" id="pe-pasos" aria-live="polite"></div>
      <div class="caja-tip"><strong>{t("How much to multiply by?", "¿Por cuánto multiplicar?")}</strong> {t("By 10 if one digit repeats, by 100 if two digits repeat. If there is a digit before the repeating group (as in 0.1666…), use two multiplications, by 10 and by 100, and subtract.", "Por 10 si se repite una cifra, por 100 si se repiten dos. Si hay una cifra antes del periodo (como en 0.1666…), se usan dos multiplicaciones, por 10 y por 100, y se restan.")}</div>
{B.om("p4", t("Practice: choose the fraction", "Practique: elija la fracción"))}
{B.libre("p5", t("Write it yourself: convert to a fraction", "Escríbalo usted: convierta a fracción"), t("Equivalent fraction", "Fracción equivalente"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Write it with a slash, for example 2/3, in simplest form.", "Escríbala con una barra, por ejemplo 2/3, y simplificada al máximo.") + '</p>\n        <div class="fila-btn">', 1)}
      <div class="caja-tip"><strong>{t("Against the clock:", "Contra reloj:")}</strong> {t('when you have mastered this page, test your speed with <a href="speed-irrationals.html">Irrational numbers against the clock</a>.', 'cuando domine esta página, ponga a prueba su agilidad con <a href="rapidez-irracionales.html">Números irracionales contra reloj</a>.')}</div>''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:2rem;font-weight:700;color:var(--acento);}\n  input[type=range]{width:100%;accent-color:var(--tema);}", scripts=("/math/radicals.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "El sistema de números reales: racionales, irracionales y la recta numérica")
