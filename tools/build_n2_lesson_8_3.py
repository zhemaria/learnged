"""Level 2 · Lesson 8.3 · Simple probability — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "8-3"
TEMA = ("Statistics and probability", "Estadística y probabilidad")
TIT = ("Simple probability", "Probabilidad simple")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.3rem;font-weight:700;color:#0d47a1">{x}</p>'

def escala():
    x0, x1, y = 70, 570, 90
    s = f'<defs><linearGradient id="gr83" x1="0" x2="1"><stop offset="0" stop-color="#ffcdd2"/><stop offset="0.5" stop-color="#fff9c4"/><stop offset="1" stop-color="#c8e6c9"/></linearGradient></defs>'
    s += f'<rect x="{x0}" y="{y - 14}" width="{x1 - x0}" height="28" rx="14" fill="url(#gr83)" stroke="#37474f" stroke-width="2"/>'
    for v, et, sub in [(0, "0", t("impossible", "imposible")), (0.5, "½ = 0.5 = 50%", t("as likely as not", "igual de posible que no")), (1, "1", t("certain", "seguro"))]:
        x = x0 + (x1 - x0) * v
        s += f'<line x1="{x:.0f}" y1="{y - 22}" x2="{x:.0f}" y2="{y + 22}" stroke="#37474f" stroke-width="3"/>'
        s += f'<text x="{x:.0f}" y="{y - 34}" text-anchor="middle" font-size="18" font-weight="700" fill="#222">{et}</text>'
        s += f'<text x="{x:.0f}" y="{y + 44}" text-anchor="middle" font-size="16" fill="#37474f">{sub}</text>'
    s += f'<text x="320" y="{y + 78}" text-anchor="middle" font-size="16" font-weight="700" fill="#0d47a1">{t("possible: between 0 and 1", "posible: entre 0 y 1")}</text>'
    return svg("0 0 640 190", t("A probability scale from 0 to 1. At 0, impossible; at one half, or 50 percent, as likely as not; at 1, certain. Everything between 0 and 1 is possible.",
                                "Una escala de probabilidad de 0 a 1. En 0, imposible; en un medio, o 50 por ciento, igual de posible que no; en 1, seguro. Todo lo que está entre 0 y 1 es posible."), s, 640)

def frac(a, b):
    return f'<span aria-hidden="true" style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.15;margin:0 3px"><span style="display:block;border-bottom:2px solid currentColor;padding:0 4px">{a}</span><span style="display:block;padding:0 4px">{b}</span></span><span class="cap-oculto">{a}{t(" over ", " sobre ")}{b}</span>'

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to the last lesson of Level 2. Here you meet <strong>probability</strong>, which measures how likely an event is to happen, on a universal scale from 0 to 1. You will learn to find a simple probability, to write it in three equivalent ways (fraction, decimal, and percent), and to tell impossible, possible, and certain events apart.", "Bienvenida a la última lección del Nivel 2. Aquí se presenta la <strong>probabilidad</strong>, que mide qué tan posible es que ocurra un evento, en una escala universal de 0 a 1. Se aprende a calcular la probabilidad simple, a expresarla de tres formas equivalentes (fracción, decimal y porcentaje) y a distinguir los eventos imposibles, posibles y seguros.")}</p>
<p>{t("The probability of an event is a number that tells how likely it is to happen. You find it with a simple ratio:", "La probabilidad de un evento es un número que indica qué tan posible es que ocurra. Se calcula con una razón muy sencilla:")}</p>
{big(t("P(A) = favorable outcomes ÷ total outcomes", "P(A) = casos favorables ÷ casos totales"))}
<p>{t("The numerator counts the outcomes that match what you are looking for; the denominator counts all the possible outcomes. The set of all possible outcomes of an experiment is the <strong>sample space</strong>. Listing it correctly is the first step of any probability problem.", "El numerador cuenta los resultados que cumplen lo que se busca; el denominador cuenta todos los resultados posibles. El conjunto de todos los resultados posibles de un experimento se llama <strong>espacio muestral</strong>. Listarlo bien es el primer paso de cualquier cálculo de probabilidad.")}</p>
{tabla(t("Sample spaces", "Espacios muestrales"), t("Examples of sample spaces", "Ejemplos de espacios muestrales"),
       [t("Experiment", "Experimento"), t("Sample space", "Espacio muestral"), t("Outcomes", "Resultados")],
       [[t("Toss a coin", "Lanzar una moneda"), t("{heads, tails}", "{cara, cruz}"), "2"],
        [t("Roll a number cube (die)", "Lanzar un dado"), "{1, 2, 3, 4, 5, 6}", "6"],
        [t("Draw a marble from a bag with 3 red and 2 blue", "Sacar una bola de una bolsa con 3 rojas y 2 azules"), t("5 marbles", "5 bolas"), "5"]])}
{ej(t("Example: rolling a die", "Ejemplo: lanzar un dado"), t("You roll a six-sided die. What is the probability of getting an even number?", "Se lanza un dado de seis caras. ¿Cuál es la probabilidad de obtener un número par?"),
  [("1", t("Sample space.", "Espacio muestral."), t("{1, 2, 3, 4, 5, 6}: 6 total outcomes.", "{1, 2, 3, 4, 5, 6}: 6 casos totales.")),
   ("2", t("Favorable outcomes.", "Casos favorables."), t("The even numbers {2, 4, 6}: 3.", "Los pares {2, 4, 6}: 3.")),
   ("3", t("Formula.", "Fórmula."), "P(" + t("even", "par") + ") = 3/6 = 1/2."),
   ("✓", t("Answer.", "Respuesta."), t("The probability is <strong>1/2</strong>, or 0.5, or 50%. The three forms are the same.", "La probabilidad es <strong>1/2</strong>, o 0.5, o 50%. Las tres formas son equivalentes."))])}
{enlace(n, t("sample-space", "espacio-muestral"), t("the definition of probability", "la definición de probabilidad simple"), t("Explore the sample space of a die, a coin, a bag of marbles, and a spinner, and count the favorable outcomes.", "Explore el espacio muestral del dado, la moneda, la bolsa de bolas y la ruleta, y cuente los casos favorables."))}'''

    s2 = f'''<p>{t("A probability is a ratio, so you can write it in the three ways from Topic 5: fraction, decimal, and percent.", "Como la probabilidad es una razón, se puede expresar de las tres maneras vistas en el Tema 5: fracción, decimal y porcentaje.")}</p>
{big(t("P(heads) = ", "P(cara) = ") + frac(1, 2) + " = 0.5 = 50%")}
<p>{t("The three numbers say the same thing. Choose the form that fits: the fraction is handy for calculating, the decimal goes straight into the calculator, and the percent is easy to understand in conversation.", "Los tres números dicen lo mismo. Se elige el formato según el contexto: la fracción es cómoda para calcular, el decimal va directo a la calculadora y el porcentaje se entiende rápido en una conversación.")}</p>
<h3>{t("The probability scale", "La escala de probabilidades")}</h3>
<p>{t("Every probability is a number from 0 to 1, including 0 and 1. The scale works in any situation, from rolling a die to forecasting the weather.", "Toda probabilidad es un número entre 0 y 1, ambos incluidos. Esa escala vale en cualquier situación, desde lanzar un dado hasta pronosticar el clima.")}</p>
<div style="text-align:center">{escala()}</div>
{tabla(t("Three kinds of events", "Tres tipos de eventos"), t("Impossible, possible, and certain events", "Eventos imposibles, posibles y seguros"),
       [t("Event", "Evento"), t("Probability", "Probabilidad"), t("Example with a die", "Ejemplo con un dado")],
       [[t("Impossible", "Imposible"), "P = 0", t("rolling a 7", "sacar un 7")],
        [t("Possible", "Posible"), "0 < P < 1", t("rolling an even number", "sacar un número par")],
        [t("Certain", "Seguro"), "P = 1", t("rolling a number from 1 to 6", "sacar un número del 1 al 6")]])}
{caja("ojo", t("Watch out", "Atención"), t("<p>A probability can never be negative or greater than 1. If a calculation gives a number outside 0 to 1, there is a mistake. It is a quick check worth doing every time.</p>", "<p>Una probabilidad nunca puede ser negativa ni mayor que 1. Si un cálculo da un número fuera del intervalo de 0 a 1, hay un error. Es una comprobación rápida que conviene hacer siempre.</p>"))}
{practica("p1", t("Practice 1 — An even number", "Práctica 1 — Un número par"), t("Rolling an even number on a six-sided die is…", "Sacar un número par al lanzar un dado de seis caras es…"),
          [("a", t("Impossible (P = 0)", "Imposible (P = 0)")), ("b", t("Certain (P = 1)", "Seguro (P = 1)")), ("c", t("Possible (0 < P < 1)", "Posible (0 < P < 1)"))])}
{practica("p2", t("Practice 2 — 24 hours", "Práctica 2 — 24 horas"), t("That a day has 24 hours is…", "Que el día tenga 24 horas es…"),
          [("a", t("Certain (P = 1)", "Seguro (P = 1)")), ("b", t("Impossible (P = 0)", "Imposible (P = 0)")), ("c", t("Possible (0 < P < 1)", "Posible (0 < P < 1)"))])}
{practica("p3", t("Practice 3 — A 10", "Práctica 3 — Un 10"), t("Rolling a 10 on a six-sided die is…", "Sacar un 10 al lanzar un dado de seis caras es…"),
          [("a", t("Possible (0 < P < 1)", "Posible (0 < P < 1)")), ("b", t("Impossible (P = 0)", "Imposible (P = 0)")), ("c", t("Certain (P = 1)", "Seguro (P = 1)"))])}
{enlace(n, t("three-forms", "tres-formas"), t("fraction, decimal, and percent", "fracción, decimal y porcentaje"), t("Write the same probability in the three forms and place it between impossible and certain.", "Exprese una misma probabilidad de las tres formas y ubíquela entre imposible y seguro."))}'''

    s3 = f'''{ej(t("Example: a number greater than 4", "Ejemplo: un número mayor que 4"), t("You roll a die. What is the probability of getting a number greater than 4?", "Se lanza un dado. ¿Cuál es la probabilidad de obtener un número mayor que 4?"),
  [("1", t("Total outcomes.", "Casos totales."), "6."),
   ("2", t("Favorable outcomes.", "Casos favorables."), t("Numbers greater than 4: {5, 6}, that is, 2.", "Números mayores que 4: {5, 6}, es decir, 2.")),
   ("3", "P.", "2/6 = 1/3 ≈ 0.333 ≈ 33.3%."),
   ("✓", t("Answer.", "Respuesta."), t("The probability is <strong>1/3</strong>, about 33%.", "La probabilidad es <strong>1/3</strong>, aproximadamente el 33%."))])}
{ej(t("Example: a bag of marbles", "Ejemplo: una bolsa de bolas"), t("A bag has 5 red marbles, 3 blue, and 2 green. You pick one without looking. What is the probability that it is blue?", "Una bolsa tiene 5 bolas rojas, 3 azules y 2 verdes. Se saca una sin mirar. ¿Cuál es la probabilidad de que sea azul?"),
  [("1", t("Total outcomes.", "Casos totales."), t("5 + 3 + 2 = 10 marbles.", "5 + 3 + 2 = 10 bolas.")),
   ("2", t("Favorable outcomes.", "Casos favorables."), t("3 blue.", "3 azules.")),
   ("3", "P.", "3/10 = 0.3 = 30%."),
   ("✓", t("Answer.", "Respuesta."), t("The probability is <strong>3/10</strong>, or 30%.", "La probabilidad es <strong>3/10</strong>, o 30%."))])}
{ej(t("Example: a small deck of cards", "Ejemplo: una baraja pequeña"), t("A small deck has 20 cards, 5 of each suit (hearts, diamonds, clubs, spades). You draw one at random. What is the probability of a heart?", "Una baraja pequeña tiene 20 cartas, 5 de cada palo (corazones, diamantes, tréboles y picas). Se saca una al azar. ¿Cuál es la probabilidad de sacar un corazón?"),
  [("1", t("Total outcomes.", "Casos totales."), t("20 cards.", "20 cartas.")),
   ("2", t("Favorable outcomes.", "Casos favorables."), t("5 hearts.", "5 corazones.")),
   ("3", "P.", "5/20 = 1/4 = 0.25 = 25%."),
   ("✓", t("Answer.", "Respuesta."), t("The probability is <strong>1/4</strong>, or 25%.", "La probabilidad es <strong>1/4</strong>, o 25%."))])}
{calc(t("Fraction to percent on the calculator", "De fracción a porcentaje en la calculadora"), t(f"<p>For 3/10: {T('3')} {T('÷')} {T('10')} {T('enter')} gives 0.3. Then {T('×')} {T('100')} {T('enter')} gives 30, that is, 30%.</p>", f"<p>Para 3/10: {T('3')} {T('÷')} {T('10')} {T('enter')} da 0.3. Después, {T('×')} {T('100')} {T('enter')} da 30, es decir, 30%.</p>"))}
{practica("p4", t("Practice 4 — A 6", "Práctica 4 — Un 6"), t("What is P(rolling a 6 on a die)?", "¿Cuánto es P(sacar un 6 al lanzar un dado)?"), [("a", frac(5, 6)), ("b", frac(1, 2)), ("c", frac(1, 6)), ("d", "6")])}
{practica("p5", t("Practice 5 — Heads", "Práctica 5 — Cara"), t("What is P(heads when you toss a coin)?", "¿Cuánto es P(sacar cara al lanzar una moneda)?"), [("a", frac(1, 2)), ("b", "1"), ("c", "2"), ("d", frac(1, 4))])}
{practica("p6", t("Practice 6 — An odd number", "Práctica 6 — Un número impar"), t("What is P(rolling an odd number on a die)?", "¿Cuánto es P(sacar un número impar al lanzar un dado)?"), [("a", frac(1, 3)), ("b", frac(2, 3)), ("c", "1"), ("d", frac(1, 2))])}
{practica("p7", t("Practice 7 — Blue marble", "Práctica 7 — Bola azul"), t("A bag has 5 red, 3 blue, and 2 green marbles. What is P(blue)?", "Una bolsa tiene 5 bolas rojas, 3 azules y 2 verdes. ¿Cuánto es P(azul)?"), [("a", frac(3, 7)), ("b", "30%"), ("c", "3%"), ("d", frac(1, 3))])}
{enlace(n, t("calculations", "calculos"), t("typical probability problems", "cálculos típicos de probabilidad"), t("Find probabilities with dice, marbles, and cards, including the probability of “not” getting something.", "Calcule probabilidades con dados, bolas y barajas, incluso la de «no sacar» algo."))}'''

    s4 = f'''<p>{t("The probability you find with the formula, favorable ÷ total, is the <strong>theoretical probability</strong>. If you actually do the experiment many times and record the results, you get the <strong>experimental probability</strong> (also called the relative frequency).", "La probabilidad calculada con la fórmula, favorables ÷ totales, se llama <strong>probabilidad teórica</strong>. Si se realiza el experimento muchas veces y se anotan los resultados, se obtiene la <strong>probabilidad experimental</strong> (también llamada frecuencia relativa).")}</p>
{big(t("experimental probability = times it happened ÷ total tries", "probabilidad experimental = veces que ocurrió ÷ veces totales"))}
{ej(t("Example: tossing a coin 20 times", "Ejemplo: lanzar una moneda 20 veces"), t("You toss a coin 20 times and get 12 heads and 8 tails. Compare the experimental probability of heads with the theoretical one.", "Al lanzar una moneda 20 veces se obtienen 12 caras y 8 cruces. Compare la probabilidad experimental de «cara» con la teórica."),
  [("1", t("Experimental.", "Experimental."), "12 ÷ 20 = 0.6 = 60%."),
   ("2", t("Theoretical.", "Teórica."), "1/2 = 0.5 = 50%."),
   ("✓", t("Comparison.", "Comparación."), t("A difference of 10 percentage points, which is normal with a small number of tries.", "Una diferencia de 10 puntos porcentuales, normal en una muestra pequeña."))])}
{caja("tip", t("The law of large numbers (simple version)", "La ley de los grandes números (versión sencilla)"), t("<p>The more times you repeat an experiment, the closer the experimental probability gets to the theoretical one. With 20 tosses, being 10 points off is normal; with 10,000 tosses, the share of heads will be very close to 50%.</p>", "<p>Cuantas más veces se repite un experimento, más se acerca la probabilidad experimental a la teórica. Con 20 lanzamientos, una diferencia de 10 puntos es normal; con 10,000 lanzamientos, la proporción de caras quedará muy cerca del 50%.</p>"))}
{practica("p8", t("Practice 8 — 20 tosses", "Práctica 8 — 20 lanzamientos"), t("A coin was tossed 20 times and landed heads 12 times. What is the experimental probability of heads?", "Se lanzó una moneda 20 veces y salió cara 12 veces. ¿Cuál es la probabilidad experimental de cara?"), [("a", "50%"), ("b", "12%"), ("c", "60%"), ("d", "40%")])}
{enlace(n, t("experiment", "experimento"), t("experiment and theory", "experimento y teoría"), t("Roll a die 10, 100, or 1,000 times and watch the frequency get closer to the theoretical probability.", "Lance un dado 10, 100 o 1,000 veces y vea cómo la frecuencia se acerca a la probabilidad teórica."))}'''

    secciones = [("s-" + t("sample-space", "espacio-muestral"), t("What simple probability is", "La definición de probabilidad simple"), s1),
                 ("s-" + t("three-forms", "tres-formas"), t("Three ways to write a probability", "Las tres formas de expresar una probabilidad"), s2),
                 ("s-" + t("calculations", "calculos"), t("Typical probability problems", "Cálculos típicos de probabilidad"), s3),
                 ("s-" + t("experiment", "experimento"), t("Experiment and theory", "Experimento y teoría"), s4)]

    lesson = {"next": t("Level 3", "Nivel 3"), "review": t("sections 1 and 3", "las secciones 1 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("There are favorable outcomes: 2, 4, and 6.", "Hay casos favorables: 2, 4 y 6."), "b": t("Odd numbers can come up too.", "También pueden salir números impares.")},
             "right": t("3 of the 6 outcomes are favorable.", "3 de los 6 casos son favorables."), "solution": t("Some outcomes are favorable, but not all: possible.", "Algunos casos son favorables, pero no todos: posible.")},
      "p2": {"ok": "a", "hints": {"b": t("Every day has 24 hours.", "Todos los días tienen 24 horas."), "c": t("It always happens.", "Ocurre siempre.")},
             "right": t("It always happens: P = 1.", "Ocurre siempre: P = 1."), "solution": t("Every case is favorable: certain.", "Todos los casos son favorables: seguro.")},
      "p3": {"ok": "b", "hints": {"a": t("A six-sided die only goes up to 6.", "Un dado de seis caras solo llega al 6."), "c": t("It can never happen.", "No puede ocurrir nunca.")},
             "right": t("No outcome is a 10: P = 0.", "Ningún resultado es 10: P = 0."), "solution": t("There are no favorable outcomes: impossible.", "No hay casos favorables: imposible.")},
      "p4": {"ok": "c", "hints": {"a": t("That is the probability of NOT getting a 6.", "Esa es la probabilidad de NO sacar un 6."), "b": t("Only one face out of six is a 6.", "Solo una cara de las seis es un 6."), "d": t("A probability is never more than 1.", "Una probabilidad nunca pasa de 1.")},
             "right": t("1 favorable out of 6: 1/6.", "1 favorable de 6: 1/6."), "solution": t("P = 1/6.", "P = 1/6.")},
      "p5": {"ok": "a", "hints": {"b": t("Tails can come up too.", "También puede salir cruz."), "c": t("A probability is never more than 1.", "Una probabilidad nunca pasa de 1."), "d": t("A coin has only two sides.", "La moneda tiene solo dos lados.")},
             "right": t("1 out of 2: 1/2.", "1 de 2: 1/2."), "solution": t("P = 1/2.", "P = 1/2.")},
      "p6": {"ok": "d", "hints": {"a": t("The odd numbers are 1, 3, and 5: three of them.", "Los impares son 1, 3 y 5: tres."), "b": t("Count the odd numbers: 1, 3, 5.", "Cuente los impares: 1, 3, 5."), "c": t("Even numbers can come up too.", "También pueden salir pares.")},
             "right": t("3/6 = 1/2.", "3/6 = 1/2."), "solution": t("Odd: {1, 3, 5}; 3/6 = 1/2.", "Impares: {1, 3, 5}; 3/6 = 1/2.")},
      "p7": {"ok": "b", "hints": {"a": t("The denominator is all the marbles: 10.", "El denominador son todas las bolas: 10."), "c": t("Check: 3 ÷ 10 = 0.3 = 30%.", "Revise: 3 ÷ 10 = 0.3 = 30%."), "d": t("There are 3 blue out of 10, not 3 colors.", "Hay 3 azules de 10, no 3 colores.")},
             "right": t("3/10 = 30%.", "3/10 = 30%."), "solution": t("Total 10; blue 3; 3/10 = 30%.", "Total 10; azules 3; 3/10 = 30%.")},
      "p8": {"ok": "c", "hints": {"a": t("50% is the theoretical probability. Use what happened.", "50% es la probabilidad teórica. Use lo que ocurrió."), "b": t("12 is the count. Divide by 20.", "12 es el conteo. Divida entre 20."), "d": t("40% is the share of tails.", "40% es la proporción de cruces.")},
             "right": t("12 ÷ 20 = 0.6 = 60%.", "12 ÷ 20 = 0.6 = 60%."), "solution": t("12 ÷ 20 = 60%.", "12 ÷ 20 = 60%.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("The even numbers are 2, 4, and 6: three.", "Los pares son 2, 4 y 6: tres."), "c": t("A probability is never more than 1.", "Una probabilidad nunca pasa de 1."), "d": t("Count the even numbers again.", "Cuente otra vez los pares.")}, "solution": t("3/6 = 1/2.", "3/6 = 1/2.")},
      "B": {"ok": "c", "hints": {"a": t("1 is a certain event.", "1 es un evento seguro."), "b": t("0.5 is as likely as not.", "0.5 es igual de posible que no."), "d": t("A probability is never negative.", "Una probabilidad nunca es negativa.")}, "solution": t("Impossible: P = 0.", "Imposible: P = 0.")},
      "C": {"ok": "a", "hints": {"b": t("0 is a valid probability: impossible.", "0 es una probabilidad válida: imposible."), "c": t("0.75 is between 0 and 1.", "0.75 está entre 0 y 1."), "d": t("3/5 is between 0 and 1.", "3/5 está entre 0 y 1.")}, "solution": t("1.2 is greater than 1: it cannot be a probability.", "1.2 es mayor que 1: no puede ser una probabilidad.")},
      "D": {"ok": "d", "hints": {"a": t("Greater than 4 means 5 or 6 only.", "Mayor que 4 son solo el 5 y el 6."), "b": t("Count: 5 and 6.", "Cuente: 5 y 6."), "c": t("There are two favorable numbers.", "Hay dos números favorables.")}, "solution": t("2/6 = 1/3.", "2/6 = 1/3.")},
      "E": {"ok": "b", "hints": {"a": t("The denominator is all 10 marbles.", "El denominador son las 10 bolas."), "c": t("Check: 3 ÷ 10.", "Revise: 3 ÷ 10."), "d": t("A probability is never more than 1.", "Una probabilidad nunca pasa de 1.")}, "solution": t("3/10 = 0.3.", "3/10 = 0.3.")},
      "F": {"ok": "c", "hints": {"a": t("5 is the count. Divide by 20.", "5 es el conteo. Divida entre 20."), "b": t("Check: 5 ÷ 20.", "Revise: 5 ÷ 20."), "d": t("You divided the other way.", "Dividió al revés.")}, "solution": t("5/20 = 1/4 = 25%.", "5/20 = 1/4 = 25%.")},
      "G": {"ok": "a", "hints": {"b": t("0.5 is the decimal. Multiply by 100.", "0.5 es el decimal. Multiplique por 100."), "c": t("1/2 does not mean the digits 1 and 2.", "1/2 no son los dígitos 1 y 2."), "d": t("Divide 1 by 2 and multiply by 100.", "Divida 1 entre 2 y multiplique por 100.")}, "solution": t("1 ÷ 2 = 0.5 = 50%.", "1 ÷ 2 = 0.5 = 50%.")},
      "H": {"ok": "d", "hints": {"a": t("Try it with the die in the practice page.", "Pruébelo con el dado de la página de práctica."), "b": t("With few tries they can be quite different.", "Con pocos intentos pueden ser bastante distintas."), "c": t("It does not go to 0.", "No se va a 0.")}, "solution": t("With many tries, it gets closer to the theoretical probability.", "Con muchos intentos, se acerca a la teórica.")}
     }}

    quiz = [
     ("A", t("You roll a die. What is the probability of an even number?", "Se lanza un dado. ¿Cuál es la probabilidad de sacar un número par?"), [("a", frac(1, 3)), ("b", frac(1, 2)), ("c", "3"), ("d", frac(2, 3))]),
     ("B", t("The probability of an impossible event is…", "La probabilidad de un evento imposible es…"), [("a", "1"), ("b", "0.5"), ("c", "0"), ("d", "−1")]),
     ("C", t("Which of these values <strong>cannot</strong> be a probability?", "¿Cuál de estos valores <strong>no</strong> puede ser una probabilidad?"), [("a", "1.2"), ("b", "0"), ("c", "0.75"), ("d", frac(3, 5))]),
     ("D", t("You roll a die. What is P(a number greater than 4)?", "Se lanza un dado. ¿Cuánto es P(un número mayor que 4)?"), [("a", frac(4, 6)), ("b", frac(1, 2)), ("c", frac(1, 6)), ("d", frac(1, 3))]),
     ("E", t("A bag has 5 red, 3 blue, and 2 green marbles. What is P(blue)?", "Una bolsa tiene 5 bolas rojas, 3 azules y 2 verdes. ¿Cuánto es P(azul)?"), [("a", frac(3, 7)), ("b", "0.3"), ("c", "0.03"), ("d", "3")]),
     ("F", t("A deck of 20 cards has 5 hearts. What is P(heart)?", "Una baraja de 20 cartas tiene 5 corazones. ¿Cuánto es P(corazón)?"), [("a", "5%"), ("b", "20%"), ("c", "25%"), ("d", "4%")]),
     ("G", t("A probability of 1/2 written as a percent is…", "Una probabilidad de 1/2 escrita como porcentaje es…"), [("a", "50%"), ("b", "0.5%"), ("c", "12%"), ("d", "2%")]),
     ("H", t("When you repeat an experiment many, many times, the experimental probability…", "Cuando se repite un experimento muchísimas veces, la probabilidad experimental…"), [("a", t("gets farther from the theoretical one", "se aleja de la teórica")), ("b", t("equals the theoretical one from the start", "es igual a la teórica desde el principio")), ("c", t("goes down to 0", "baja hasta 0")), ("d", t("gets closer to the theoretical one", "se acerca a la teórica"))])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("How likely is it? Favorable ÷ total outcomes, the scale from 0 to 1, fraction, decimal, and percent, and the difference between theoretical and experimental probability.", "¿Qué tan posible es? Casos favorables ÷ casos totales, la escala de 0 a 1, fracción, decimal y porcentaje, y la diferencia entre la probabilidad teórica y la experimental."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>List</strong> the sample space of an experiment.", "<strong>Listar</strong> el espacio muestral de un experimento."),
         t("<strong>Find</strong> a simple probability: favorable ÷ total outcomes.", "<strong>Calcular</strong> la probabilidad simple: casos favorables ÷ casos totales."),
         t("<strong>Write</strong> a probability as a fraction, a decimal, and a percent.", "<strong>Expresar</strong> una probabilidad como fracción, decimal y porcentaje."),
         t("<strong>Tell</strong> impossible, possible, and certain events apart on the 0-to-1 scale.", "<strong>Distinguir</strong> los eventos imposibles, posibles y seguros en la escala de 0 a 1."),
         t("<strong>Compare</strong> experimental and theoretical probability.", "<strong>Comparar</strong> la probabilidad experimental con la teórica.")],
        secciones,
        (t("Find eight simple probabilities (dice, coins, marbles, and cards) and write each one as a fraction, a decimal, and a percent. Classify six events as impossible, possible, or certain.",
           "Calcule ocho probabilidades simples (dados, monedas, bolas y cartas) y escriba cada una como fracción, decimal y porcentaje. Clasifique seis eventos como imposibles, posibles o seguros."),
         t("Toss a coin 20 times (or roll a die 30 times) and record the results. Find the experimental probability and compare it with the theoretical one. Then put your results together with someone else's: does it get closer?",
           "Lance una moneda 20 veces (o un dado 30 veces) y anote los resultados. Calcule la probabilidad experimental y compárela con la teórica. Después, junte sus resultados con los de otra persona: ¿se acerca más?")),
        quiz,
        t("Self-check checklist for probability", "Lista de autoevaluación de probabilidad"),
        t("Self-check checklist: skills for simple probability", "Lista de autoevaluación: destrezas de probabilidad simple"),
        [(t("Find the probability", "Calcular la probabilidad"), t("I list the sample space, count the favorable outcomes, and simplify the fraction.", "Listo el espacio muestral, cuento los casos favorables y simplifico la fracción."), t("I find it with some help.", "La calculo con algo de apoyo."), t("I mix up favorable and total outcomes.", "Confundo los casos favorables con los totales.")),
         (t("Three forms and the scale", "Tres formas y la escala"), t("I write it as a fraction, decimal, and percent, and I check that it is between 0 and 1.", "La escribo como fracción, decimal y porcentaje, y compruebo que esté entre 0 y 1."), t("I write it in one or two forms.", "La escribo de una o dos formas."), t("I give probabilities greater than 1.", "Doy probabilidades mayores que 1.")),
         (t("Experiment and theory", "Experimento y teoría"), t("I find the experimental probability and explain why it gets closer to the theoretical one with many tries.", "Calculo la probabilidad experimental y explico por qué se acerca a la teórica con muchos intentos."), t("I find it with some help.", "La calculo con algo de apoyo."), t("I do not tell the two apart.", "No distingo una de la otra."))],
        t("<p>In this lesson you built the idea of <strong>simple probability</strong>: favorable outcomes ÷ total outcomes, always on the scale from <strong>0 to 1</strong>. You learned to list the sample space, to write a probability as a fraction, a decimal, and a percent, to tell impossible, possible, and certain events apart, and to compare experimental and theoretical probability.</p>\n<p><strong>This completes Level 2.</strong> Simple probability is the foundation on which Level 3 builds compound probability. Congratulations on all your work!</p>",
          "<p>En esta lección se construyó el concepto de <strong>probabilidad simple</strong>: casos favorables ÷ casos totales, siempre en la escala de <strong>0 a 1</strong>. Se aprendió a listar el espacio muestral, a escribir una probabilidad como fracción, decimal y porcentaje, a distinguir los eventos imposibles, posibles y seguros, y a comparar la probabilidad experimental con la teórica.</p>\n<p><strong>Con esto se completa el Nivel 2.</strong> La probabilidad simple es la base sobre la que el Nivel 3 construirá la probabilidad compuesta. ¡Felicidades por todo su trabajo!</p>"),
        (None, ("", t("Level 3 (coming soon)", "Nivel 3 (próximamente)"))),
        [(t("probability", "probabilidad"), t("A number from 0 to 1 that tells how likely an event is.", "Un número de 0 a 1 que indica qué tan posible es un evento.")),
         (t("sample space", "espacio muestral"), t("The set of all possible outcomes of an experiment.", "El conjunto de todos los resultados posibles de un experimento.")),
         (t("favorable outcome", "caso favorable"), t("An outcome that matches what you are looking for.", "Un resultado que cumple lo que se busca.")),
         (t("experimental probability", "probabilidad experimental"), t("Times it happened ÷ total tries.", "Veces que ocurrió ÷ veces totales."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "exp": {"dado": [["an even number", "par"], ["a number greater than 4", "may4"], ["a 7", "nunca"], ["a number from 1 to 6", "siempre"], ["a multiple of 3", "mul3"]],
          "moneda": [["heads", "cara"], ["heads or tails", "siempre"]],
          "urna": [["a red marble (R)", "R"], ["a blue marble (B)", "A"], ["a marble that is not green", "noV"], ["a black marble", "nunca"]],
          "ruleta": [["an odd number", "impar"], ["a number less than 3", "men3"], ["the 8", "ocho"]]},
  "monedaEsp": ["heads", "tails"], "urnaEsp": ["R", "R", "R", "B", "B", "G"],
  "espacio": "Sample space ({n} outcomes):", "favs": "Favorable (filled in color): {f} of {n}.", "ninguno": "none", "favVoz": "Favorable: {x}.",
  "evento": " — {x} event", "tipos": {"i": "impossible", "p": "possible", "s": "certain"},
  "evt": [["Rolling an even number on a die.", "p"], ["That a day has 24 hours.", "s"], ["Rolling a 10 on a six-sided die.", "i"], ["Drawing a red marble from a bag with 4 red and 6 blue.", "p"], ["Drawing a green marble from a bag with 5 red and 5 blue.", "i"], ["Getting heads or tails when you toss a coin.", "s"], ["Drawing an ace from a full deck of cards.", "p"], ["Rolling a number less than 7 on a die.", "s"], ["That a week has 8 days.", "i"]],
  "nomT": {"i": "Impossible (P = 0)", "p": "Possible (0 < P < 1)", "s": "Certain (P = 1)"}, "bienT": {"i": "There are no favorable outcomes.", "p": "There are favorable outcomes, but not all of them are.", "s": "Every outcome is favorable."}, "malT": "It is {x}.",
  "tfNo": "Write a fraction (3/8), a decimal (0.375), or a percent (37.5%).", "tfFr": "Fraction", "tfDe": "Decimal", "tfPc": "Percent",
  "tfFuera": "That value cannot be a probability: it must be from 0 to 1.", "tfImp": "Impossible event.", "tfSeg": "Certain event.", "tfVal": "A valid probability: the event is possible.",
  "t1Q": "The probability {f} written as a decimal is:", "t1": "{a} ÷ {b} = {d}.", "t2Q": "The probability {f} written as a percent is:", "t2B": "{d} × 100 = {p}%.", "t2M": "{a} ÷ {b} = {d}, and × 100 = {p}%.",
  "t3Q": "Which of these values <strong>cannot</strong> be a probability?", "t3B": "{x} is outside the range from 0 to 1.", "t3M": "The one that cannot be is {x}: every probability is from 0 to 1.",
  "dado": "You roll a die. What is the probability of getting {x}?", "evD": [["a number greater than 4", 2], ["an even number", 3], ["a 1 or a 6", 2], ["a number less than 5", 4], ["a multiple of 3", 2]],
  "urna1": "A bag has {r} red, {a} blue, and {v} green marbles. You pick one without looking. What is the probability that it is {c}?", "colores": ["red", "blue", "green"], "urnaP": "The denominator is the total number of marbles, not the ones that are not {c}.",
  "urna2": "A bag has {r} red, {a} blue, and {v} green marbles. What is the probability that the marble is <strong>not</strong> green?", "urna2P": "That is the probability that it IS green. You want the opposite: 1 minus that.",
  "carta": "You draw a card from a deck of 52. What is the probability of drawing {x}?", "cartas": [["a heart", 13], ["an ace", 4], ["a red card", 26], ["a face card (J, Q, or K)", 12], ["the king of spades", 1]],
  "letra": "The letters of the word {w} are written on cards, and you draw one at random. What is the probability of drawing an “{l}”?", "palabras": ["MATHEMATICS", "PROBABILITY", "CHICAGO", "STATISTICS"],
  "calcS": "Favorable outcomes: {f}; total outcomes: {n}. P = {x}.",
  "exVoz": "Experimental frequency of each face of the die compared with the theoretical one sixth.", "exTeo": "theoretical probability: 1/6 ≈ 16.7%",
  "exN": "Rolls: <strong>{n}</strong>. ", "exF": "Frequencies: {x}.", "exNada": "No rolls yet.", "exDif": "The bar farthest from the red line is {d} percentage points away. ", "exPocos": "With few rolls the differences are large.", "exMuchos": "With many rolls, all the bars get close to the theoretical probability.",
  "g1Q": "A die was rolled {n} times and landed on 3 {c} times. What is the experimental probability of a 3?", "g1T": "That is the theoretical probability. The experimental one uses what happened: {c} out of {n}.", "g1B": "Frequency ÷ tries: {c}/{n}.", "g1M": "The experimental probability is frequency ÷ tries: {c}/{n}.",
  "g2Q": "A coin is tossed 10 times and lands heads 7 times. What can you conclude?", "g2": ["It is normal with few tosses; the theoretical probability is still 1/2", "The coin is surely unfair", "The probability of heads is 7/10 forever"], "g2B": "With few tries the experimental probability can be far from the theoretical one.", "g2M": "With only 10 tosses, 7 heads is normal; with thousands, the share would get close to 1/2.",
  "g3Q": "What happens to the experimental probability when you repeat an experiment many, many times?", "g3": ["It gets closer to the theoretical probability", "It gets farther and farther from the theoretical one", "It always equals the theoretical one from the start"], "g3B": "With many tries, the relative frequency gets close to the theoretical one. Check it with the die above.", "g3M": "It gets closer to the theoretical one. Try rolling the die 1,000 times above."
 },
 "es": {
  "exp": {"dado": [["un número par", "par"], ["un número mayor que 4", "may4"], ["un 7", "nunca"], ["un número del 1 al 6", "siempre"], ["un múltiplo de 3", "mul3"]],
          "moneda": [["cara", "cara"], ["cara o cruz", "siempre"]],
          "urna": [["una bola roja (R)", "R"], ["una bola azul (A)", "A"], ["una bola que no sea verde", "noV"], ["una bola negra", "nunca"]],
          "ruleta": [["un número impar", "impar"], ["un número menor que 3", "men3"], ["el 8", "ocho"]]},
  "monedaEsp": ["cara", "cruz"], "urnaEsp": ["R", "R", "R", "A", "A", "V"],
  "espacio": "Espacio muestral ({n} resultados):", "favs": "Favorables (rellenos de color): {f} de {n}.", "ninguno": "ninguno", "favVoz": "Favorables: {x}.",
  "evento": " — evento {x}", "tipos": {"i": "imposible", "p": "posible", "s": "seguro"},
  "evt": [["Sacar un número par al lanzar un dado.", "p"], ["Que un día tenga 24 horas.", "s"], ["Sacar un 10 al lanzar un dado de seis caras.", "i"], ["Sacar una bola roja de una bolsa con 4 rojas y 6 azules.", "p"], ["Sacar una bola verde de una bolsa con 5 rojas y 5 azules.", "i"], ["Que salga cara o cruz al lanzar una moneda.", "s"], ["Sacar un as de una baraja completa.", "p"], ["Sacar un número menor que 7 al lanzar un dado.", "s"], ["Que una semana tenga 8 días.", "i"]],
  "nomT": {"i": "Imposible (P = 0)", "p": "Posible (0 < P < 1)", "s": "Seguro (P = 1)"}, "bienT": {"i": "No hay ningún caso favorable.", "p": "Hay casos favorables, pero no todos lo son.", "s": "Todos los casos son favorables."}, "malT": "Es {x}.",
  "tfNo": "Escriba una fracción (3/8), un decimal (0.375) o un porcentaje (37.5%).", "tfFr": "Fracción", "tfDe": "Decimal", "tfPc": "Porcentaje",
  "tfFuera": "Ese valor no puede ser una probabilidad: tiene que estar entre 0 y 1.", "tfImp": "Evento imposible.", "tfSeg": "Evento seguro.", "tfVal": "Probabilidad válida: el evento es posible.",
  "t1Q": "La probabilidad {f} escrita como decimal es:", "t1": "{a} ÷ {b} = {d}.", "t2Q": "La probabilidad {f} escrita como porcentaje es:", "t2B": "{d} × 100 = {p}%.", "t2M": "{a} ÷ {b} = {d}, y × 100 = {p}%.",
  "t3Q": "¿Cuál de estos valores <strong>no</strong> puede ser una probabilidad?", "t3B": "{x} está fuera del intervalo de 0 a 1.", "t3M": "El que no puede ser es {x}: toda probabilidad está entre 0 y 1.",
  "dado": "Se lanza un dado. ¿Cuál es la probabilidad de obtener {x}?", "evD": [["un número mayor que 4", 2], ["un número par", 3], ["un 1 o un 6", 2], ["un número menor que 5", 4], ["un múltiplo de 3", 2]],
  "urna1": "Una bolsa tiene {r} bolas rojas, {a} azules y {v} verdes. Se saca una sin mirar. ¿Cuál es la probabilidad de que sea {c}?", "colores": ["roja", "azul", "verde"], "urnaP": "El denominador es el total de bolas, no las que no son de ese color.",
  "urna2": "Una bolsa tiene {r} bolas rojas, {a} azules y {v} verdes. ¿Cuál es la probabilidad de que la bola <strong>no</strong> sea verde?", "urna2P": "Esa es la probabilidad de que SÍ sea verde. Se pide lo contrario: 1 menos eso.",
  "carta": "Se saca una carta de una baraja de 52. ¿Cuál es la probabilidad de sacar {x}?", "cartas": [["un corazón", 13], ["un as", 4], ["una carta roja", 26], ["una figura (J, Q o K)", 12], ["el rey de picas", 1]],
  "letra": "Se escriben las letras de la palabra {w} en tarjetas y se saca una al azar. ¿Cuál es la probabilidad de sacar una «{l}»?", "palabras": ["MATEMATICAS", "PROBABILIDAD", "CHICAGO", "ESTADISTICA"],
  "calcS": "Casos favorables: {f}; casos totales: {n}. P = {x}.",
  "exVoz": "Frecuencia experimental de cada cara del dado frente a la teórica de un sexto.", "exTeo": "probabilidad teórica: 1/6 ≈ 16.7%",
  "exN": "Lanzamientos: <strong>{n}</strong>. ", "exF": "Frecuencias: {x}.", "exNada": "Todavía no se ha lanzado.", "exDif": "La barra más alejada de la línea roja se separa {d} puntos porcentuales. ", "exPocos": "Con pocos lanzamientos las diferencias son grandes.", "exMuchos": "Con muchos lanzamientos, todas las barras se acercan a la teórica.",
  "g1Q": "Se lanzó un dado {n} veces y salió el 3 en {c} ocasiones. ¿Cuál es la probabilidad experimental de sacar un 3?", "g1T": "Esa es la probabilidad teórica. La experimental usa lo que pasó: {c} de {n}.", "g1B": "Frecuencia ÷ intentos: {c}/{n}.", "g1M": "La experimental es frecuencia ÷ intentos: {c}/{n}.",
  "g2Q": "Se lanza una moneda 10 veces y sale cara 7 veces. ¿Qué se puede concluir?", "g2": ["Es normal con pocos lanzamientos; la probabilidad teórica sigue siendo 1/2", "La moneda está trucada seguro", "La probabilidad de cara es 7/10 para siempre"], "g2B": "Con pocos intentos la experimental puede alejarse mucho de la teórica.", "g2M": "Con solo 10 lanzamientos es normal que salgan 7 caras; con miles, la proporción se acercaría a 1/2.",
  "g3Q": "¿Qué pasa con la probabilidad experimental cuando se repite un experimento muchísimas veces?", "g3": ["Se acerca a la probabilidad teórica", "Se aleja cada vez más de la teórica", "Siempre es igual a la teórica desde el principio"], "g3B": "Con muchos intentos, la frecuencia relativa se acerca a la teórica. Compruébelo con el dado de arriba.", "g3M": "Se acerca a la teórica. Pruebe a lanzar el dado 1,000 veces arriba."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }

/* ============ MODULE 1 · sample space ============ */
var PRUEBA = { par: function(x){ return +x % 2 === 0; }, may4: function(x){ return +x > 4; }, nunca: function(){ return false; }, siempre: function(){ return true; }, mul3: function(x){ return +x % 3 === 0; },
  cara: function(x){ return x === TXT.monedaEsp[0]; }, R: function(x){ return x === "R"; }, A: function(x){ return x === TXT.urnaEsp[3]; }, noV: function(x){ return x !== TXT.urnaEsp[5]; },
  impar: function(x){ return +x % 2 === 1; }, men3: function(x){ return +x < 3; }, ocho: function(x){ return x === "8"; } };
var ESP = { dado: ["1", "2", "3", "4", "5", "6"], moneda: TXT.monedaEsp, urna: TXT.urnaEsp, ruleta: ["1", "2", "3", "4", "5", "6", "7", "8"] };
function llenaEv(){ var e = TXT.exp[$("em-x").value]; $("em-e").innerHTML = e.map(function(v, i){ return '<option value="' + i + '">' + v[0] + '</option>'; }).join(""); }
function pintaEM(){
  var x = $("em-x").value, esp = ESP[x], ev = TXT.exp[x][+$("em-e").value], f = PRUEBA[ev[1]], fav = esp.filter(f), n = esp.length, k = fav.length;
  $("em-vis").innerHTML = '<p>' + F(TXT.espacio, { n: n }) + '</p>' + chipsN(esp.map(function(_, i){ return i; }), esp.map(function(v){ return f(v) ? "med" : ""; }), esp) + '<span class="sr-only">' + F(TXT.favVoz, { x: fav.join(", ") || TXT.ninguno }) + '</span>';
  var tipo = k === 0 ? "i" : (k === n ? "s" : "p");
  $("em-salida").innerHTML = '<div class="linea">' + F(TXT.favs, { f: k, n: n }) + '</div><div class="linea veredicto">P = ' + (k === 0 ? "0" : (k === n ? "1" : tresF(k, n))) + F(TXT.evento, { x: TXT.tipos[tipo] }) + '</div>';
}
function genTipo(){
  var e = elige(TXT.evt);
  return { enun: e[0], opciones: ["i", "p", "s"].map(function(k){ return { html: TXT.nomT[k], clave: k }; }), correcta: e[1], enOrden: true, bien: TXT.bienT[e[1]], mal: F(TXT.malT, { x: TXT.nomT[e[1]].toLowerCase() }) };
}

/* ============ MODULE 2 · three forms ============ */
function aFr(v){ for (var k = 0; k <= 6; k++){ var d = Math.pow(10, k); if (Math.abs(Math.round(v * d) - v * d) < 1e-9) return reduce(Math.round(v * d), d); } return null; }
function pintaTF(){
  var s = $("tf-v").value, v = leeProb(s), sal = $("tf-salida");
  if (v === null){ $("tf-v").classList.add("error"); sal.innerHTML = '<div class="linea">' + TXT.tfNo + '</div>'; return; }
  $("tf-v").classList.remove("error");
  var m = String(s).trim().replace(/\s+/g, "").match(/^(\d+)\/(\d+)$/), fr = m ? reduce(+m[1], +m[2]) : aFr(v);
  sal.innerHTML = '<div class="linea">' + TXT.tfFr + ': <strong>' + (fr ? fracHTML(fr.p, fr.q) : "—") + '</strong> · ' + TXT.tfDe + ': <strong>' + nd(Math.round(v * 10000) / 10000) + '</strong> · ' + TXT.tfPc + ': <strong>' + nd(Math.round(v * 100000) / 1000) + '%</strong></div>' +
    '<div class="linea veredicto">' + (v < 0 || v > 1 ? TXT.tfFuera : (v === 0 ? TXT.tfImp : (v === 1 ? TXT.tfSeg : TXT.tfVal))) + '</div>';
}
function genTres(){
  var pr = elige([[1, 2], [1, 4], [3, 4], [1, 5], [2, 5], [3, 10], [1, 8], [3, 8], [7, 20], [1, 10]]), v = pr[0] / pr[1], tp = aleatorio(1, 3), o = { a: pr[0], b: pr[1], d: nd(v), p: nd(v * 100), f: fracHTML(pr[0], pr[1]) };
  if (tp === 1){ var op = [nd(v), nd(pr[1] / pr[0]), nd(v * 10), pr[0] + "." + pr[1]].filter(function(x, i, a){ return a.indexOf(x) === i; });
    return { enun: F(TXT.t1Q, o), opciones: baraja(op).map(function(x){ return { html: x, clave: "d" + x }; }), correcta: "d" + nd(v), bien: F(TXT.t1, o), mal: F(TXT.t1, o) }; }
  if (tp === 2){ var op2 = [nd(v * 100) + "%", nd(v) + "%", nd(v * 1000) + "%", pr[0] + "%"].filter(function(x, i, a){ return a.indexOf(x) === i; });
    return { enun: F(TXT.t2Q, o), opciones: baraja(op2).map(function(x){ return { html: x, clave: "p" + x }; }), correcta: "p" + nd(v * 100) + "%", bien: F(TXT.t2B, o), mal: F(TXT.t2M, o) }; }
  var malo = elige(["1.5", "120%", "−0.2", "5/4"]), buenos = baraja(["0", "1", "0.99", "3%", "7/8", "100%"]).slice(0, 3);
  return { enun: TXT.t3Q, opciones: baraja([{ html: malo, clave: "m" }].concat(buenos.map(function(b, i){ return { html: b, clave: "b" + i }; }))), correcta: "m", bien: F(TXT.t3B, { x: malo }), mal: F(TXT.t3M, { x: malo }) };
}

/* ============ MODULE 3 · typical problems ============ */
function genCalc(){
  var tp = aleatorio(1, 5), fav, tot, enun, p = [];
  if (tp === 1){ var ev = elige(TXT.evD); fav = ev[1]; tot = 6; enun = F(TXT.dado, { x: ev[0] }); }
  else if (tp === 2){ var r = aleatorio(2, 8), a = aleatorio(1, 6), v = aleatorio(1, 5), k = aleatorio(0, 2), cnt = [r, a, v][k]; fav = cnt; tot = r + a + v;
    enun = F(TXT.urna1, { r: r, a: a, v: v, c: TXT.colores[k] }); if (tot - fav > 0) p.push({ v: fav / (tot - fav), msg: F(TXT.urnaP, { c: TXT.colores[k] }) }); }
  else if (tp === 3){ var r2 = aleatorio(2, 8), a2 = aleatorio(2, 8), vv = aleatorio(1, 5); tot = r2 + a2 + vv; fav = tot - vv; enun = F(TXT.urna2, { r: r2, a: a2, v: vv }); p.push({ v: vv / tot, msg: TXT.urna2P }); }
  else if (tp === 4){ var c = elige(TXT.cartas); fav = c[1]; tot = 52; enun = F(TXT.carta, { x: c[0] }); }
  else { var w = elige(TXT.palabras), letras = w.split(""), rep = letras.filter(function(x, i, a){ return a.indexOf(x) !== a.lastIndexOf(x); }), l = elige(rep.length ? rep : letras);
    fav = letras.filter(function(x){ return x === l; }).length; tot = letras.length; enun = F(TXT.letra, { w: w, l: l }); }
  var val = fav / tot;
  return { enun: enun, correcta: fav + "/" + tot, solucion: F(TXT.calcS, { f: fav, n: tot, x: tresF(fav, tot) }), evalua: evaluaProb(val, p.filter(function(x){ return Math.abs(x.v - val) > 0.001; })) };
}

/* ============ MODULE 4 · experiment and theory ============ */
var EXPD = { c: [0, 0, 0, 0, 0, 0], n: 0 };
function lanza(k){ for (var i = 0; i < k; i++){ EXPD.c[Math.floor(Math.random() * 6)]++; EXPD.n++; } pintaEX(); }
function pintaEX(){
  var W = 640, x0 = 60, yb = 220, w = 60, g = 30, mx = 0.3, yT = yb - (1 / 6) / mx * 170;
  var s = '<svg class="figura" viewBox="0 0 640 260" role="img" aria-label="' + TXT.exVoz + '">';
  EXPD.c.forEach(function(c, i){ var f = EXPD.n ? c / EXPD.n : 0, h = Math.min(f, mx) / mx * 170, x = x0 + i * (w + g);
    s += '<rect x="' + x + '" y="' + f1(yb - h) + '" width="' + w + '" height="' + f1(h) + '" fill="#1565c0"/>' + texto([x + w / 2, yb + 18], i + 1, 16, "#222");
    if (EXPD.n) s += h > 26 ? texto([x + w / 2, yb - h + 14], nd(Math.round(f * 1000) / 10) + "%", 13, "#fff", 700) : texto([x + w / 2, yb - h - 10], nd(Math.round(f * 1000) / 10) + "%", 13, "#0d47a1", 700); });
  s += '<line x1="' + (x0 - 10) + '" y1="' + f1(yT) + '" x2="' + (W - 30) + '" y2="' + f1(yT) + '" stroke="#b71c1c" stroke-width="2" stroke-dasharray="7 5"/>';
  s += '<line x1="' + x0 + '" y1="22" x2="' + (x0 + 40) + '" y2="22" stroke="#b71c1c" stroke-width="2" stroke-dasharray="7 5"/><text x="' + (x0 + 48) + '" y="22" dominant-baseline="middle" font-size="15" font-weight="700" fill="#b71c1c">' + TXT.exTeo + '</text>';
  $("ex-svg").innerHTML = s + '</svg>';
  var dif = EXPD.n ? Math.max.apply(null, EXPD.c.map(function(c){ return Math.abs(c / EXPD.n - 1 / 6); })) : 0;
  $("ex-salida").innerHTML = '<div class="linea">' + F(TXT.exN, { n: nd(EXPD.n) }) + (EXPD.n ? F(TXT.exF, { x: EXPD.c.map(function(c, i){ return (i + 1) + ": " + c; }).join(" · ") }) : TXT.exNada) + '</div>' +
    (EXPD.n ? '<div class="linea">' + F(TXT.exDif, { d: nd(Math.round(dif * 1000) / 10) }) + (EXPD.n < 100 ? TXT.exPocos : TXT.exMuchos) + '</div>' : '');
}
function genExp(){
  var tp = aleatorio(1, 3);
  if (tp === 1){ var n = elige([20, 50, 100, 200]), c = Math.round(n / 6) + aleatorio(-5, 5); if (c === Math.round(n / 6)) c++; var pc = {}; pc.t = F(TXT.g1T, { c: c, n: n });
    return { enun: F(TXT.g1Q, { n: n, c: c }), opciones: baraja([{ html: fracHTML(c, n), clave: "e" }, { html: fracHTML(1, 6), clave: "t" }, { html: fracHTML(c, 6), clave: "x" }, { html: fracHTML(3, n), clave: "y" }]), correcta: "e", pistas: pc, bien: F(TXT.g1B, { c: c, n: n }), mal: F(TXT.g1M, { c: c, n: n }) }; }
  var k = tp === 2 ? "g2" : "g3";
  return { enun: TXT[k + "Q"], opciones: baraja(TXT[k].map(function(x, i){ return { html: x, clave: "abc"[i] }; })), correcta: "a", bien: TXT[k + "B"], mal: TXT[k + "M"] };
}

/* ============ Start ============ */
$("em-x").addEventListener("change", function(){ llenaEv(); pintaEM(); }); $("em-e").addEventListener("change", pintaEM); llenaEv(); pintaEM();
creaPracticaOM("p1", genTipo);
$("tf-v").addEventListener("input", pintaTF); pintaTF();
creaPracticaOM("p2", genTres);
creaPracticaLibre("p3", genCalc);
$("ex-10").addEventListener("click", function(){ lanza(10); }); $("ex-100").addEventListener("click", function(){ lanza(100); }); $("ex-1000").addEventListener("click", function(){ lanza(1000); }); $("ex-0").addEventListener("click", function(){ EXPD = { c: [0, 0, 0, 0, 0, 0], n: 0 }; pintaEX(); }); pintaEX();
creaPracticaOM("p4", genExp);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    mods = [
     (t("sample-space", "espacio-muestral"), t("What simple probability is", "La definición de probabilidad simple"),
      f'''      <div class="formula">{t("P(A) = favorable outcomes ÷ total outcomes", "P(A) = casos favorables ÷ casos totales")}</div>
      <p>{t("The <strong>sample space</strong> is the list of all possible outcomes. Choose an experiment and an event, and count the favorable outcomes.", "El <strong>espacio muestral</strong> es la lista de todos los resultados posibles. Elija un experimento y un evento, y cuente los casos favorables.")}</p>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="em-x">{t("Experiment", "Experimento")}</label><select id="em-x"><option value="dado">{t("Roll a die", "Lanzar un dado")}</option><option value="moneda">{t("Toss a coin", "Lanzar una moneda")}</option><option value="urna">{t("Draw a marble (3 red, 2 blue, 1 green)", "Sacar una bola (3 rojas, 2 azules, 1 verde)")}</option><option value="ruleta">{t("Spin a spinner from 1 to 8", "Girar una ruleta del 1 al 8")}</option></select></div>
          <div class="campo"><label for="em-e">{t("Event", "Evento")}</label><select id="em-e"></select></div>
        </div>
        <div id="em-vis"></div>
        <div class="salida" id="em-salida" aria-live="polite"></div>
      </div>
{B.om("p1", t("Practice: impossible, possible, or certain?", "Practique: ¿imposible, posible o seguro?"))}'''),
     (t("three-forms", "tres-formas"), t("Fraction, decimal, and percent", "Fracción, decimal y porcentaje"),
      f'''      <p>{t("The same probability can be written in three ways: 1/2 = 0.5 = 50%. Every probability is from 0 (impossible) to 1 (certain).", "Una misma probabilidad se escribe de tres maneras: 1/2 = 0.5 = 50%. Toda probabilidad está entre 0 (imposible) y 1 (seguro).")}</p>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="tf-v">{t("Probability (fraction, decimal, or percent)", "Probabilidad (fracción, decimal o porcentaje)")}</label><input type="text" class="ancho" id="tf-v" autocomplete="off" value="3/8"></div></div>
        <div class="salida" id="tf-salida" aria-live="polite"></div>
      </div>
{B.om("p2", t("Practice: the three forms", "Practique: las tres formas"))}'''),
     (t("calculations", "calculos"), t("Typical probability problems", "Cálculos típicos de probabilidad"),
      f'''      <p>{t("Count the total outcomes (all the marbles, all the cards, all the faces) and the favorable ones. The probability of <strong>not</strong> getting something is 1 minus the probability of getting it.", "Cuente los casos totales (todas las bolas, todas las cartas, todas las caras) y los favorables. La probabilidad de <strong>no</strong> sacar algo es 1 menos la probabilidad de sacarlo.")}</p>
      <div class="caja-tip">{t("A standard deck has 52 cards: 4 suits (hearts and diamonds are red; clubs and spades are black) of 13 cards each (A, 2–10, J, Q, K).", "Una baraja estándar tiene 52 cartas: 4 palos (corazones y diamantes son rojos; tréboles y picas son negros) de 13 cartas cada uno (A, 2–10, J, Q, K).")}</div>
{libre_x("p3", t("Practice: find the probability", "Practique: calcule la probabilidad"), t("Probability", "Probabilidad"), t("Write it as a fraction (3/8), a decimal (0.375), or a percent (37.5%).", "Escríbala como fracción (3/8), decimal (0.375) o porcentaje (37.5%)."))}'''),
     (t("experiment", "experimento"), t("Experiment and theory", "Experimento y teoría"),
      f'''      <p>{t("The theoretical probability of each face of a die is 1/6 ≈ 16.7%. Roll the die and watch the experimental probability of each face.", "La probabilidad teórica de cada cara de un dado es 1/6 ≈ 16.7%. Lance el dado y observe la probabilidad experimental de cada cara.")}</p>
      <div class="panel">
        <div class="fila-btn">
          <button type="button" class="btn" id="ex-10">{t("Roll 10 times", "Lanzar 10 veces")}</button>
          <button type="button" class="btn" id="ex-100">{t("Roll 100 times", "Lanzar 100 veces")}</button>
          <button type="button" class="btn" id="ex-1000">{t("Roll 1,000 times", "Lanzar 1,000 veces")}</button>
          <button type="button" class="btn-sec" id="ex-0">{t("Start over", "Empezar de nuevo")}</button>
        </div>
        <div id="ex-svg"></div>
        <div class="salida" id="ex-salida" aria-live="polite"></div>
      </div>
{B.om("p4", t("Practice: experiment and theory", "Practique: experimento y teoría"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/stats.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Probabilidad simple")
