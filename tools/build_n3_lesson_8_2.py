"""Level 3 · Lesson 8.2 · Compound probability: with and without replacement — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_8-2.html and algebra/n3-l8-2.html (GEDparaHispanos). The explore pages come from build_n3_explora_8.py.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n3
from build_n3_lesson_8_1 import TEMA, SCRIPTS
from build_n3_explora_8 import ESTILO8

B.NIVEL = 3
N = "8-2"
TIT = ("Compound probability: with and without replacement", "Probabilidad compuesta: con y sin reemplazo")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def figura_arbol():
    R, A = "#c62828", "#1565c0"
    def fr(x, y, n, d, c): return f'<text x="{x}" y="{y - 3}" font-size="15" font-weight="700" text-anchor="middle" fill="{c}">{n}</text><line x1="{x - 12}" y1="{y}" x2="{x + 12}" y2="{y}" stroke="{c}"/><text x="{x}" y="{y + 15}" font-size="15" font-weight="700" text-anchor="middle" fill="{c}">{d}</text>'
    def bola(x, y, c, l): return f'<circle cx="{x}" cy="{y}" r="15" fill="{c}"/><text x="{x}" y="{y + 6}" font-size="15" font-weight="700" text-anchor="middle" fill="#fff">{l}</text>'
    rl, al = "R", t("B", "A")
    s = (f'<text x="40" y="155" font-size="15" font-weight="700" text-anchor="middle" fill="#5d4037">{t("Bag", "Bolsa")}</text>'
         f'<line x1="65" y1="150" x2="215" y2="70" stroke="{R}" stroke-width="3"/><line x1="65" y1="150" x2="215" y2="230" stroke="{A}" stroke-width="3"/>'
         + fr(130, 92, 4, 7, R) + fr(130, 212, 3, 7, A) + bola(230, 70, R, rl) + bola(230, 230, A, al) +
         f'<line x1="245" y1="70" x2="395" y2="30" stroke="{R}" stroke-width="3"/><line x1="245" y1="70" x2="395" y2="110" stroke="{A}" stroke-width="3"/>'
         + fr(318, 32, 3, 6, R) + fr(318, 118, 3, 6, A) + bola(410, 30, R, rl) + bola(410, 110, A, al) +
         f'<text x="440" y="116" font-size="16" font-weight="700" fill="#1b5e20">4/7 × 3/6</text>')
    return B.svg("0 0 560 260", t("A tree diagram for a bag with 4 red and 3 blue candies, without replacement. First draw: red 4/7, blue 3/7. After a red one: red 3/6, blue 3/6. The path red then blue is 4/7 × 3/6.",
                                  "Un diagrama de árbol de una bolsa con 4 caramelos rojos y 3 azules, sin reemplazo. Primera extracción: rojo 4/7, azul 3/7. Después de un rojo: rojo 3/6, azul 3/6. El camino rojo y luego azul es 4/7 × 3/6."), s, 540)

def leccion():
    n = N
    azar = t('<a href="explore-chance.html">Explore: chance experiments</a>', '<a href="explorar-azar.html">Explorar: experimentos de azar</a>')
    arbol = t('<a href="explore-tree.html">Explore: from the tree to the table</a>', '<a href="explorar-arbol.html">Explorar: del árbol a la tabla</a>')
    s1 = f'''<p>{t("In Lesson 8.1 you learned to count the possible outcomes. Probability uses that counting: it compares the favorable cases with the possible cases. This lesson studies the probability of two or more events together, and the key difference between doing it with replacement and without replacement.", "En la Lección 8.1 se aprendió a contar los resultados posibles. La probabilidad usa ese conteo: compara los casos favorables con los casos posibles. Esta lección estudia la probabilidad de dos o más eventos juntos, y la diferencia clave entre hacerlo con reemplazo y sin reemplazo.")}</p>
<p>{t("The probability of an event measures how likely it is to happen. It is the ratio of the favorable cases to the possible cases.", "La probabilidad de un evento mide qué tan probable es que ocurra. Se calcula como la razón entre los casos favorables y los casos posibles.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">{t("P(event) = ", "P(evento) = ")}{fx(t("favorable cases", "casos favorables"), t("possible cases", "casos posibles"))}</p>
{ejemplo(t("Example 1: a bag has 4 red candies, 3 blue, and 2 green (9 in all). What is the probability of drawing a red one?", "Ejemplo 1: una bolsa tiene 4 caramelos rojos, 3 azules y 2 verdes (9 en total). ¿Cuál es la probabilidad de sacar uno rojo?"),
  [("1", t("Count.", "Se cuenta."), t("Favorable cases (red): 4. Possible cases (total): 9.", "Casos favorables (rojos): 4. Casos posibles (total): 9.")),
   ("✓", t("Answer.", "Respuesta."), f"P({t('red', 'rojo')}) = <strong>4/9</strong>.")])}
{caja("tip", t("Theoretical and experimental", "Teórica y experimental"), t(f"<p>In {azar} you can roll dice, draw cards, and spin a spinner hundreds of times, and watch the experimental probability get close to the theoretical one.</p>", f"<p>En {azar} puede lanzar dados, sacar cartas y girar una ruleta cientos de veces, y ver cómo la probabilidad experimental se acerca a la teórica.</p>"))}
{enlace(n, t("one-event", "un-evento"), t("the probability of one event", "probabilidad de un evento"), t("Review probability as favorable cases out of possible cases.", "Repase la probabilidad como casos favorables entre casos posibles."))}'''

    s2 = f'''<p>{t("When the object is put back after the first event (<strong>with replacement</strong>), the second event is not affected: the events are <strong>independent</strong>. The probability that both happen is the product of their probabilities.", "Cuando después del primer evento se devuelve el objeto (<strong>con reemplazo</strong>), el segundo evento no se ve afectado: los eventos son <strong>independientes</strong>. La probabilidad de que ocurran ambos es el producto de sus probabilidades.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">{t("P(A and B) = P(A) × P(B)", "P(A y B) = P(A) × P(B)")}</p>
{ejemplo(t("Example 2: with replacement. From the bag (4 red, 3 blue, 2 green; 9 in all), you draw a candy, put it back, and draw another. What is the probability of red and then blue?", "Ejemplo 2 · Con reemplazo. De la bolsa (4 rojos, 3 azules, 2 verdes; 9 en total) se saca un caramelo, se devuelve, y se saca otro. ¿Cuál es la probabilidad de sacar rojo y luego azul?"),
  [("1", f"P({t('red', 'rojo')}) = 4/9.", t("Since it goes back, the total is still 9.", "Como se devuelve, el total sigue siendo 9.")),
   ("2", f"P({t('blue', 'azul')}) = 3/9.", t(f"Multiply: {fx(4, 9)} × {fx(3, 9)} = {fx(12, 81)}.", f"Se multiplican: {fx(4, 9)} × {fx(3, 9)} = {fx(12, 81)}.")),
   ("✓", t("Answer.", "Respuesta."), t(f"P(red and then blue) = {fx(12, 81)}, which simplifies to <strong>{fx(4, 27)}</strong>.", f"P(rojo y luego azul) = {fx(12, 81)}, que se simplifica a <strong>{fx(4, 27)}</strong>."))])}
{practica("p1", t("Practice 1 — One green", "Práctica 1 — Uno verde"), t("Same bag (4 red, 3 blue, 2 green; 9 in all). P(green) in one draw is…", "Misma bolsa (4 rojos, 3 azules, 2 verdes; 9 en total). P(verde) en una sola extracción es…"), [("a", "2/7"), ("b", "9/2"), ("c", "2/9")])}
{practica("p2", t("Practice 2 — Red twice, with replacement", "Práctica 2 — Dos rojos, con reemplazo"), t("With replacement, P(red and then red) is…", "Con reemplazo, P(rojo y luego rojo) es…"), [("a", "4/9 × 3/8"), ("b", "4/9 × 4/9 = 16/81"), ("c", "8/9")])}
{practica("p3", t("Practice 3 — The total", "Práctica 3 — El total"), t("With replacement, does the total number of candies change between the first and the second draw?", "Con reemplazo, ¿cambia el total de caramelos entre la primera y la segunda extracción?"), [("a", t("No, it is still 9", "No, sigue siendo 9")), ("b", t("Yes, it drops to 8", "Sí, baja a 8")), ("c", t("Yes, it goes up to 10", "Sí, sube a 10"))])}
{enlace(n, t("with", "con"), t("two events with replacement", "dos eventos con reemplazo"), t("Multiply probabilities when the denominator does not change.", "Multiplique probabilidades cuando el denominador no cambia."))}'''

    filas = [[t("With replacement (it goes back)", "Con reemplazo (se devuelve)"), t("Independent", "Independientes"), t("Does not change", "No cambia")],
             [t("Without replacement (it stays out)", "Sin reemplazo (no se devuelve)"), t("Dependent", "Dependientes"), t("Goes down by 1", "Disminuye en 1")]]
    s3 = f'''<p>{t("When the object is not put back, the second event does change: there is one object fewer in all (and one fewer of the kind that came out). The events are <strong>dependent</strong>.", "Cuando el objeto no se devuelve, el segundo evento sí cambia: hay un objeto menos en total (y uno menos del tipo que salió). Los eventos son <strong>dependientes</strong>.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">{t("P(A and B) = P(A) × P(B after A)", "P(A y B) = P(A) × P(B después de A)")}</p>
{figura_arbol()}
{ejemplo(t("Example 3: without replacement. From a bag with 4 red and 3 blue candies (7 in all), you draw one and do not put it back; then you draw another. What is the probability of red and then blue?", "Ejemplo 3 · Sin reemplazo. De una bolsa con 4 rojos y 3 azules (7 en total) se saca uno y no se devuelve; luego se saca otro. ¿Cuál es la probabilidad de rojo y luego azul?"),
  [("1", f"P({t('red', 'rojo')}) = 4/7.", ""),
   ("2", t("Without replacement, 6 candies are left, 3 of them blue.", "Ya sin reemplazo quedan 6 caramelos, 3 de ellos azules."), f"P({t('blue after', 'azul después')}) = 3/6."),
   ("3", t("Multiply.", "Se multiplican."), f"{fx(4, 7)} × {fx(3, 6)} = {fx(12, 42)} = {fx(2, 7)}."),
   ("✓", t("Answer.", "Respuesta."), t(f"P(red and then blue) = <strong>{fx(2, 7)}</strong>.", f"P(rojo y luego azul) = <strong>{fx(2, 7)}</strong>."))])}
{tabla(t("With and without replacement", "Con y sin reemplazo"), t("The difference between probability with and without replacement", "Diferencia entre probabilidad con reemplazo y sin reemplazo"), [t("Situation", "Situación"), t("Kind of events", "Tipo de eventos"), t("The denominator…", "El denominador…")], filas)}
{caja("ojo", t("Adjust both numbers", "Ajustar los dos números"), t("<p>Without replacement, on the second draw both the numerator (if an object of that kind came out) and the denominator (always down by 1) change. Forgetting to adjust the denominator is the most common mistake.</p>", "<p>Sin reemplazo, en la segunda extracción cambian tanto el numerador (si salió un objeto de ese tipo) como el denominador (siempre baja en 1). Olvidar ajustar el denominador es el error más común.</p>"))}
{practica("p4", t("Practice 4 — What is left", "Práctica 4 — Lo que queda"), t("A bag has 5 chips; one is taken out and not put back. How many are left for the second draw?", "Una bolsa tiene 5 fichas; se saca una sin reemplazo. ¿Cuántas quedan para la segunda extracción?"), [("a", "4"), ("b", "5"), ("c", "6")])}
{practica("p5", t("Practice 5 — Red twice, without replacement", "Práctica 5 — Dos rojos, sin reemplazo"), t("A bag has 4 red and 2 blue (6 in all). Without replacement, P(red and then red) is…", "Bolsa con 4 rojos y 2 azules (6 en total). Sin reemplazo, P(rojo y luego rojo) es…"), [("a", "4/6 × 4/6"), ("b", "4/6 × 3/5"), ("c", "4/6 + 3/5")])}
{practica("p6", t("Practice 6 — Independent events", "Práctica 6 — Eventos independientes"), t("Which events are independent?", "¿Qué eventos son independientes?"), [("a", t("The draws without replacement", "Los de una extracción sin reemplazo")), ("b", t("There are never independent events", "Nunca hay eventos independientes")), ("c", t("The draws with replacement", "Los de una extracción con reemplazo"))])}
{caja("tip", t("From the tree to the table", "Del árbol a la tabla"), t(f"<p>In {arbol} you can build a tree diagram step by step, with or without replacement, and see how each path becomes a cell of a two-way table.</p>", f"<p>En {arbol} puede construir un diagrama de árbol paso a paso, con o sin reemplazo, y ver cómo cada camino pasa a una celda de una tabla de doble entrada.</p>"))}
{enlace(n, t("without", "sin"), t("two events without replacement", "dos eventos sin reemplazo"), t("Adjust the numerator and the denominator after the first draw.", "Ajuste el numerador y el denominador después de la primera extracción."))}'''

    s4 = f'''<p>{t("A probability can be written as a fraction, a decimal, or a percent. The GED test often asks for one of the three, so it helps to know how to convert between them.", "Una probabilidad se puede escribir como fracción, decimal o porcentaje. El examen GED suele pedir una de las tres, así que conviene saber convertir entre ellas.")}</p>
{ejemplo(t("Example 4: write the probability 1/4 in the three forms.", "Ejemplo 4: expresar la probabilidad 1/4 de las tres formas."),
  [("1", t("As a fraction.", "Como fracción."), "1/4."),
   ("2", t("As a decimal.", "Como decimal."), "1 ÷ 4 = 0.25."),
   ("3", t("As a percent.", "Como porcentaje."), "0.25 × 100 = 25%."),
   ("✓", t("Answer.", "Respuesta."), "<strong>1/4 = 0.25 = 25%</strong>.")])}
{caja("ojo", t("Every probability is between 0 and 1", "Toda probabilidad está entre 0 y 1"), t("<p>A value of 0 means impossible, and 1 (or 100%) means certain. If a calculation gives a probability greater than 1, there is a mistake: you probably added when you needed to multiply.</p>", "<p>Un valor de 0 significa imposible y 1 (o 100%) significa seguro. Si un cálculo da una probabilidad mayor que 1, hay un error: probablemente se sumó cuando se debía multiplicar.</p>"))}
{enlace(n, t("three-forms", "tres-formas"), t("fraction, decimal, and percent", "fracción, decimal y porcentaje"), t("Write the answer in the three forms.", "Exprese el resultado de las tres formas."))}'''

    secciones = [("s-" + t("one-event", "un-evento"), t("Review: the probability of one event", "Repaso: probabilidad de un evento"), s1),
                 ("s-" + t("with", "con"), t("Two events with replacement", "Dos eventos con reemplazo"), s2),
                 ("s-" + t("without", "sin"), t("Two events without replacement", "Dos eventos sin reemplazo"), s3),
                 ("s-" + t("three-forms", "tres-formas"), t("Three ways to write the answer", "Expresar el resultado de tres formas"), s4)]

    lesson = {"next": t("Lesson 8.3", "Lección 8.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("The denominator is the total of all the candies, not only the ones that are not green.", "El denominador es el total de caramelos, no solo los que no son verdes."), "b": t("The fraction is upside down, and a probability is never more than 1.", "La fracción está al revés, y una probabilidad nunca pasa de 1.")}, "right": t("2 green out of 9 in all: 2/9.", "2 verdes de 9 en total: 2/9."), "solution": "2/9."},
      "p2": {"ok": "b", "hints": {"a": t("That would be without replacement. Here the candy goes back.", "Así sería sin reemplazo. Aquí el caramelo se devuelve."), "c": t("You added. For both events, multiply.", "Sumó. Para los dos eventos se multiplica.")}, "right": t("With replacement the bag does not change: 4/9 × 4/9 = 16/81.", "Con reemplazo la bolsa no cambia: 4/9 × 4/9 = 16/81."), "solution": "4/9 × 4/9 = 16/81."},
      "p3": {"ok": "a", "hints": {"b": t("The candy goes back into the bag.", "El caramelo se devuelve a la bolsa."), "c": t("No new candies are added.", "No se agregan caramelos nuevos.")}, "right": t("The candy goes back, so the total is still 9.", "El caramelo se devuelve, así que el total sigue en 9."), "solution": t("No, it is still 9.", "No, sigue siendo 9.")},
      "p4": {"ok": "a", "hints": {"b": t("The chip is not put back.", "La ficha no se devuelve."), "c": t("A chip was taken out, not added.", "Se sacó una ficha, no se agregó.")}, "right": "5 − 1 = 4.", "solution": t("4 chips.", "4 fichas.")},
      "p5": {"ok": "b", "hints": {"a": t("That would be with replacement. Without it, adjust the second fraction.", "Así sería con reemplazo. Sin reemplazo, hay que ajustar la segunda fracción."), "c": t("For both events, multiply; do not add.", "Para los dos eventos se multiplica, no se suma.")}, "right": t("After a red one, 3 red are left out of 5: 4/6 × 3/5.", "Después de un rojo quedan 3 rojos de 5: 4/6 × 3/5."), "solution": "4/6 × 3/5 = 12/30 = 2/5."},
      "p6": {"ok": "c", "hints": {"a": t("Without replacement, the second draw depends on the first.", "Sin reemplazo, la segunda depende de la primera."), "b": t("With replacement, the bag is the same for the second draw.", "Con reemplazo, la bolsa queda igual para la segunda.")}, "right": t("With replacement, the first draw does not affect the second.", "Con reemplazo, la primera no afecta a la segunda."), "solution": t("With replacement.", "Con reemplazo.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The denominator is the total, 8, not the blue ones.", "El denominador es el total, 8, no los azules."), "b": t("5/8 is the probability of blue.", "5/8 es la probabilidad de azul."), "d": t("The fraction is upside down.", "La fracción está al revés.")}, "solution": "3/8."},
      "B": {"ok": "d", "hints": {"a": t("Dependent is without replacement.", "Dependientes es sin reemplazo."), "b": t("They can happen.", "Sí pueden ocurrir."), "c": t("They do not have to be equal.", "No tienen por qué ser iguales.")}, "solution": t("Independent.", "Independientes.")},
      "C": {"ok": "b", "hints": {"a": t("For “A and B”, multiply.", "Para «A y B» se multiplica."), "c": t("For “A and B”, multiply.", "Para «A y B» se multiplica."), "d": t("For “A and B”, multiply.", "Para «A y B» se multiplica.")}, "solution": "P(A) × P(B)."},
      "D": {"ok": "a", "hints": {"b": t("You added. A probability is never more than 1.", "Sumó. Una probabilidad nunca pasa de 1."), "c": t("That is one toss. There are two.", "Eso es un lanzamiento. Son dos."), "d": t("A probability is never more than 1.", "Una probabilidad nunca pasa de 1.")}, "solution": "1/2 × 1/2 = 1/4."},
      "E": {"ok": "c", "hints": {"a": t("The chip is not put back.", "La ficha no se devuelve."), "b": t("A chip was taken out, not added.", "Se sacó una ficha, no se agregó."), "d": t("Only one chip was taken out.", "Solo se sacó una ficha.")}, "solution": "5 − 1 = 4."},
      "F": {"ok": "a", "hints": {"b": t("Without replacement, the second total is 6, not 7.", "Sin reemplazo, el segundo total es 6, no 7."), "c": t("For both events, multiply.", "Para los dos eventos se multiplica."), "d": t("The second draw is blue: 3 blue are left.", "La segunda es azul: quedan 3 azules.")}, "solution": "4/7 × 3/6 = 2/7."},
      "G": {"ok": "b", "hints": {"a": t("1 ÷ 4 = 0.25.", "1 ÷ 4 = 0.25."), "c": t("1 ÷ 4 = 0.25, not 0.14.", "1 ÷ 4 = 0.25, no 0.14."), "d": t("You divided the other way around.", "Dividió al revés.")}, "solution": "1/4 = 0.25 = 25%."},
      "H": {"ok": "c", "hints": {"a": t("0 means impossible: that is allowed.", "0 significa imposible: sí está permitido."), "b": t("1 means certain: that is allowed.", "1 significa seguro: sí está permitido."), "d": t("Probabilities are often fractions.", "Las probabilidades muchas veces son fracciones.")}, "solution": t("Greater than 1.", "Mayor que 1.")}
     }}

    quiz = [
     ("A", t("A bag has 3 red and 5 blue (8 in all). P(red) is…", "Una bolsa tiene 3 rojas y 5 azules (8 en total). P(roja) es…"), [("a", "3/5"), ("b", "5/8"), ("c", "3/8"), ("d", "8/3")]),
     ("B", t("With replacement, the two events are…", "Con reemplazo, los dos eventos son…"), [("a", t("dependent", "dependientes")), ("b", t("impossible", "imposibles")), ("c", t("always equal", "siempre iguales")), ("d", t("independent", "independientes"))]),
     ("C", t("With replacement, P(A and B) is found with…", "Con reemplazo, P(A y B) se calcula como…"), [("a", "P(A) + P(B)"), ("b", "P(A) × P(B)"), ("c", "P(A) − P(B)"), ("d", "P(A) / P(B)")]),
     ("D", t("A coin is tossed twice. P(heads and then heads) is…", "Una moneda se lanza 2 veces. P(cara y luego cara) es…"), [("a", "1/2 × 1/2 = 1/4"), ("b", "1/2 + 1/2 = 1"), ("c", "1/2"), ("d", "2")]),
     ("E", t("A bag has 5 chips; one is taken out without replacement. For the second draw there are…", "Bolsa con 5 fichas; se saca una sin reemplazo. Para la segunda quedan…"), [("a", "5"), ("b", "6"), ("c", "4"), ("d", "3")]),
     ("F", t("A bag has 4 red and 3 blue (7). Without replacement, P(red and then blue) is…", "Bolsa de 4 rojas y 3 azules (7). Sin reemplazo, P(roja y luego azul) es…"), [("a", "4/7 × 3/6"), ("b", "4/7 × 3/7"), ("c", "4/7 + 3/6"), ("d", "4/7 × 4/6")]),
     ("G", t("Which probability is equal to 1/4?", "¿Qué probabilidad equivale a 1/4?"), [("a", "0.40 = 40%"), ("b", "0.25 = 25%"), ("c", "0.14 = 14%"), ("d", "4.0 = 400%")]),
     ("H", t("A valid probability can never be…", "Una probabilidad válida nunca puede ser…"), [("a", t("equal to 0", "igual a 0")), ("b", t("equal to 1", "igual a 1")), ("c", t("greater than 1", "mayor que 1")), ("d", t("a fraction", "una fracción"))])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Find the probability of two events in a row, with and without replacement, and write it as a fraction, a decimal, and a percent.", "Calcule la probabilidad de dos eventos seguidos, con y sin reemplazo, y exprésela como fracción, decimal y porcentaje."),
        ("🎲", t("Chance and the tree diagram", "El azar y el diagrama de árbol")),
        [t("<strong>Find</strong> the probability of a simple event as favorable cases over possible cases.", "<strong>Calcular</strong> la probabilidad de un evento simple como casos favorables sobre casos posibles."),
         t("<strong>Find</strong> the probability of two events with replacement (independent): P(A and B) = P(A) × P(B).", "<strong>Calcular</strong> la probabilidad de dos eventos con reemplazo (independientes): P(A y B) = P(A) × P(B)."),
         t("<strong>Find</strong> the probability without replacement (dependent): P(A and B) = P(A) × P(B after A).", "<strong>Calcular</strong> la probabilidad sin reemplazo (dependientes): P(A y B) = P(A) × P(B después de A)."),
         t("<strong>Tell</strong> how replacement changes the probabilities.", "<strong>Distinguir</strong> el efecto del reemplazo en las probabilidades."),
         t("<strong>Write</strong> the answer as a fraction, a decimal, and a percent.", "<strong>Expresar</strong> el resultado en fracción, decimal y porcentaje.")],
        secciones,
        (t(f"Solve three probability problems with replacement and three without replacement, drawing the tree diagram for each one. Write every answer as a fraction, a decimal, and a percent. Then check two of them in {arbol}.",
           f"Resuelva tres problemas de probabilidad con reemplazo y tres sin reemplazo, dibujando el diagrama de árbol de cada uno. Escriba cada respuesta como fracción, decimal y porcentaje. Después compruebe dos de ellos en {arbol}."),
         t("Put 5 coins of two kinds in a cup (for example, 3 pennies and 2 nickels). Draw two without looking, without putting the first back, and write down the result. Repeat 20 times. Compare how often you got two pennies with the probability 3/5 × 2/4.",
           "Ponga 5 monedas de dos tipos en un vaso (por ejemplo, 3 de un centavo y 2 de cinco). Saque dos sin mirar, sin devolver la primera, y anote el resultado. Repita 20 veces. Compare cuántas veces salieron dos de un centavo con la probabilidad 3/5 × 2/4.")),
        quiz,
        t("Self-check checklist for compound probability", "Lista de autoevaluación de probabilidad compuesta"),
        t("Self-check checklist: skills for compound probability with and without replacement", "Lista de autoevaluación: destrezas de probabilidad compuesta con y sin reemplazo"),
        [(t("Classifying the events", "Clasificar el tipo de evento"), t("I tell independent from dependent events and explain the effect of replacement.", "Clasifico el evento (independiente o dependiente) y explico el efecto del reemplazo."), t("I classify with occasional mistakes.", "Clasifico con errores ocasionales."), t("I cannot tell independent from dependent.", "No distingo independiente de dependiente.")),
         (t("Using the right formula", "Aplicar la fórmula correcta"), t("I use the right formula and adjust the numerator and denominator without replacement.", "Aplico la fórmula correcta y ajusto numerador y denominador sin reemplazo."), t("I multiply, but I do not adjust without replacement.", "Multiplico, pero no ajusto el caso sin reemplazo."), t("I do not multiply the probabilities.", "No multiplico las probabilidades.")),
         (t("Finding and writing the answer", "Calcular y expresar el resultado"), t("I calculate without mistakes, simplify, and write the answer as a fraction, a decimal, and a percent.", "Calculo sin errores, simplifico y expreso el resultado en fracción, decimal y porcentaje."), t("I make a mistake or do not simplify.", "Calculo con algún error o no simplifico."), t("I make fraction mistakes.", "Cometo errores de fracción."))],
        t("<p>In this lesson you found the compound probability of two events: with replacement (independent, the denominator does not change) and without replacement (dependent, the denominator goes down by 1), using the tree diagram and writing the answer as a fraction, a decimal, and a percent.</p>\n<p><strong>Lesson 8.3 · Final project and strategies for the GED math test</strong> closes Level 3. You will bring together everything you learned in a data project and practice strategies for the GED test, including a final review of the eight topics.</p>",
          "<p>En esta lección se calculó la probabilidad compuesta de dos eventos: con reemplazo (independientes, el denominador no cambia) y sin reemplazo (dependientes, el denominador baja en 1), usando el diagrama de árbol y expresando el resultado en fracción, decimal y porcentaje.</p>\n<p>La <strong>Lección 8.3 · Proyecto final integrador y estrategias para el GED</strong> cierra el Nivel 3. Se reunirá todo lo aprendido en un proyecto de análisis de datos y se practicarán estrategias para el examen GED, incluido un repaso final de los ocho temas del nivel.</p>"),
        ("8-3", ("", t("Lesson 8.3 · Final project and strategies for the GED math test", "Lección 8.3 · Proyecto final integrador y estrategias para el GED"))),
        [(t("probability", "probabilidad"), t("Favorable cases ÷ possible cases. It is always between 0 and 1.", "Casos favorables ÷ casos posibles. Siempre está entre 0 y 1.")),
         (t("with replacement", "con reemplazo"), t("The object goes back before the next draw; the events are independent.", "El objeto se devuelve antes de la siguiente extracción; los eventos son independientes.")),
         (t("without replacement", "sin reemplazo"), t("The object stays out; the events are dependent.", "El objeto no se devuelve; los eventos son dependientes.")),
         (t("independent events", "eventos independientes"), t("Events in which one does not change the probability of the other.", "Eventos en los que uno no cambia la probabilidad del otro.")),
         (t("tree diagram", "diagrama de árbol"), t("A drawing with one branch for each outcome; multiply along a path.", "Un dibujo con una rama por cada resultado; se multiplica a lo largo de un camino."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var COLORES = [{n: T("red", "rojo"), pl: T("red", "rojos"), l: "R", c: "#c62828"}, {n: T("blue", "azul"), pl: T("blue", "azules"), l: T("B", "A"), c: "#1565c0"}, {n: T("green", "verde"), pl: T("green", "verdes"), l: T("G", "V"), c: "#2e7d32"}];
function cuenta(k, i){ return k + " " + (k === 1 ? COLORES[i].n : COLORES[i].pl); }
function textoBolsa(n){ var T0 = n[0] + n[1] + n[2]; return T("A bag has " + n[0] + " red, " + n[1] + " blue, and " + n[2] + " green candies (" + T0 + " in all).", "Una bolsa tiene " + cuenta(n[0], 0) + ", " + cuenta(n[1], 1) + " y " + cuenta(n[2], 2) + " (" + T0 + " caramelos en total)."); }
function bolsaAzar(){ var n; do { n = [aleatorio(1, 6), aleatorio(1, 6), aleatorio(0, 4)]; } while (n[0] + n[1] + n[2] < 5); return n; }
function coloresConHay(n){ return [0, 1, 2].filter(function(i){ return n[i] > 0; }); }

/* MODULE 1 · One event */
function opF(p, q){ var r = reduce(p, q); return {html: fracHTML(p, q), clave: "f" + r.p + "/" + r.q}; }
function genSimple(){
  var tp = aleatorio(1, 3), f, T0, enun, o, pc = {}, pista;
  if (tp === 1){ var n = bolsaAzar(); T0 = n[0] + n[1] + n[2]; var c = elige(coloresConHay(n)); f = n[c];
    enun = textoBolsa(n) + T(" What is the probability of drawing a " + COLORES[c].n + " one?", " ¿Cuál es la probabilidad de sacar uno " + COLORES[c].n + "?");
    o = [opF(f, T0), opF(f, T0 - f), opF(T0, f), opF(f, T0 + 1)]; var r1_ = reduce(f, T0 - f); pc["f" + r1_.p + "/" + r1_.q] = T("The denominator is the total number of possible cases, not the ones that are not " + COLORES[c].n + ".", "El denominador es el total de casos posibles, no los que no son " + COLORES[c].pl + "."); pista = T("Favorable: the " + COLORES[c].n + " candies. Possible: all of them.", "Favorables: los caramelos " + COLORES[c].pl + ". Posibles: todos."); }
  else if (tp === 2){ var ev = elige([[T("an even number", "un número par"), 3], [T("a number greater than 4", "un número mayor que 4"), 2], [T("a 6", "un 6"), 1], [T("a number less than 3", "un número menor que 3"), 2], [T("a multiple of 3", "un múltiplo de 3"), 2]]); T0 = 6; f = ev[1];
    enun = T("A six-sided die is rolled. What is the probability of getting " + ev[0] + "?", "Se lanza un dado de seis caras. ¿Cuál es la probabilidad de obtener " + ev[0] + "?"); o = [opF(f, 6), opF(6 - f, 6), opF(f, 5), opF(1, f + 1 === 6 ? 7 : f + 1)]; pista = T("A die has 6 possible results. How many of them are favorable?", "Un dado tiene 6 resultados posibles. ¿Cuántos son favorables?"); }
  else { var ev2 = elige([[T("a heart", "un corazón"), 13], [T("an ace", "un as"), 4], [T("a face card (J, Q, or K)", "una figura (J, Q o K)"), 12], [T("a red card", "una carta roja"), 26], [T("the ace of spades", "el as de picas"), 1]]); T0 = 52; f = ev2[1];
    enun = T("A card is drawn from a deck of 52. What is the probability of drawing " + ev2[0] + "?", "Se saca una carta de una baraja de 52. ¿Cuál es la probabilidad de sacar " + ev2[0] + "?"); o = [opF(f, 52), opF(52 - f, 52), opF(f, 13), opF(1, f)]; pista = T("A deck has 52 cards: 4 suits of 13, and each suit has 1 ace and 3 face cards.", "Una baraja tiene 52 cartas: 4 palos de 13, y cada palo tiene 1 as y 3 figuras."); }
  return {enun: enun, opciones: o, correcta: o[0].clave, porClave: pc, pista: pista, bien: T("Favorable cases: " + f + "; possible cases: " + T0 + ".", "Casos favorables: " + f + "; casos posibles: " + T0 + "."), mal: T("P = favorable cases ÷ possible cases = " + f + "/" + T0 + ".", "P = casos favorables ÷ casos posibles = " + f + "/" + T0 + ".")};
}

/* MODULES 2 and 3 · The bag of candies */
function bolsaSVG(cuentas, quitado, titulo){
  var items = []; cuentas.forEach(function(k, i){ for (var j = 0; j < k; j++) items.push(i); });
  var porFila = 9, filas = Math.ceil(items.length / porFila) || 1, W = 300, H = 76 + filas * 32, s = '<svg class="geo-svg" style="max-width:300px" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + titulo + '">';
  s += '<path d="M20 20 Q20 ' + (H - 6) + " 150 " + (H - 6) + " Q280 " + (H - 6) + ' 280 20 Z" fill="#fff8e1" stroke="#8d6e63" stroke-width="3"/>';
  var marcado = false;
  items.forEach(function(ci, j){
    var x = 44 + (j % porFila) * 27, y = 52 + Math.floor(j / porFila) * 32, col = COLORES[ci], fuera = quitado !== null && quitado !== undefined && ci === quitado && !marcado; if (fuera) marcado = true;
    s += '<circle cx="' + x + '" cy="' + y + '" r="12" fill="' + (fuera ? "#fff" : col.c) + '" stroke="' + col.c + '" stroke-width="2"' + (fuera ? ' stroke-dasharray="3 3"' : "") + "/>" + texto([x, y + 1], col.l, 12, fuera ? col.c : "#fff");
  });
  return s + "</svg>";
}
function creaBolsa(pre, reemplazo){
  var panel = $(pre + "-panel");
  var sel = function(id, def){ return '<select id="' + pre + "-" + id + '">' + COLORES.map(function(c, i){ return '<option value="' + i + '"' + (i === def ? " selected" : "") + ">" + c.n + "</option>"; }).join("") + "</select>"; };
  panel.innerHTML = '<div class="campos">' + COLORES.map(function(c, i){ return '<div class="campo"><label for="' + pre + "-n" + i + '">' + T(c.n.charAt(0).toUpperCase() + c.n.slice(1) + " candies", "Caramelos " + c.pl) + '</label><input type="text" inputmode="numeric" class="corto" id="' + pre + "-n" + i + '" value="' + [4, 3, 2][i] + '"></div>'; }).join("") + "</div>" +
    '<div class="campos" style="margin-top:8px;"><div class="campo"><label for="' + pre + '-c1">' + T("First comes out", "Primero sale") + "</label>" + sel("c1", 0) + '</div><div class="campo"><label for="' + pre + '-c2">' + T("Then comes out", "Después sale") + "</label>" + sel("c2", reemplazo ? 1 : 0) + "</div></div>" +
    '<p class="caja-aviso" id="' + pre + '-aviso" role="alert"></p>' +
    '<div class="lado-a-lado"><div><p><strong>' + T("1st draw", "1.ª extracción") + '</strong></p><div id="' + pre + '-b1"></div></div><div><p><strong>' + T("2nd draw", "2.ª extracción") + '</strong></p><div id="' + pre + '-b2"></div></div></div>' +
    '<div class="salida" id="' + pre + '-salida" aria-live="polite"></div>';
  function pinta(){
    var n = [0, 1, 2].map(function(i){ return leeEntero($(pre + "-n" + i).value); }), av = $(pre + "-aviso");
    if (n.some(function(x){ return x === null || x < 0 || x > 9; })){ av.className = "caja-aviso visible"; av.textContent = T("Type whole numbers from 0 to 9.", "Escriba cantidades enteras de 0 a 9."); return; }
    var c1 = +$(pre + "-c1").value, c2 = +$(pre + "-c2").value, T0 = n[0] + n[1] + n[2];
    if (T0 < 2 || n[c1] === 0){ av.className = "caja-aviso visible"; av.textContent = T("The bag needs at least 2 candies and at least one of the first color you chose.", "La bolsa necesita al menos 2 caramelos y alguno del primer color elegido."); return; }
    av.className = "caja-aviso"; av.textContent = "";
    var n2 = n.slice(); if (!reemplazo) n2[c1]--;
    var T2 = reemplazo ? T0 : T0 - 1, f2 = n2[c2];
    $(pre + "-b1").innerHTML = bolsaSVG(n, null, T("Bag with " + n[0] + " red, " + n[1] + " blue, and " + n[2] + " green.", "Bolsa con " + n[0] + " rojos, " + n[1] + " azules y " + n[2] + " verdes."));
    $(pre + "-b2").innerHTML = bolsaSVG(n, reemplazo ? null : c1, reemplazo ? T("The same bag: the candy went back.", "La misma bolsa: el caramelo se devolvió.") : T("The bag without the " + COLORES[c1].n + " candy that came out: " + T2 + " are left.", "Bolsa sin el caramelo " + COLORES[c1].n + " que salió: quedan " + T2 + "."));
    var h = '<div class="linea">P(' + COLORES[c1].n + T(" first) = ", " primero) = ") + fracHTML(n[c1], T0) + ".</div>";
    h += '<div class="linea">' + (reemplazo ? T("It goes back: the bag still has " + T0 + " candies, " + n[c2] + " " + COLORES[c2].n + ".", "Se devuelve: la bolsa sigue con " + T0 + " caramelos, " + cuenta(n[c2], c2) + ".") :
          T("It does not go back: " + T2 + " candies are left, " + f2 + " " + COLORES[c2].n + (c1 === c2 ? " (one fewer, because one of that color already came out)." : "."), "No se devuelve: quedan " + T2 + " caramelos, " + cuenta(f2, c2) + (c1 === c2 ? " (uno menos, porque ya salió uno de ese color)." : "."))) +
          " P(" + COLORES[c2].n + T(" next) = ", " después) = ") + fracHTML(f2, T2) + ".</div>";
    var num = n[c1] * f2, den = T0 * T2;
    h += '<div class="linea veredicto">P(' + COLORES[c1].n + T(" and then ", " y luego ") + COLORES[c2].n + ") = " + fracHTML(n[c1], T0) + " × " + fracHTML(f2, T2) + " = " + (num === 0 ? "0" : tresFormas(num, den)) + "</div>";
    var otra = reemplazo ? n[c1] * (n[c2] - (c1 === c2 ? 1 : 0)) : n[c1] * n[c2], otroDen = reemplazo ? T0 * (T0 - 1) : T0 * T0;
    h += '<div class="linea nota">' + (reemplazo ? T("Without replacement", "Sin reemplazo") : T("With replacement", "Con reemplazo")) + T(" it would be ", " daría ") + fracHTML(Math.max(otra, 0), otroDen) + " ≈ " + nm(Math.round(Math.max(otra, 0) / otroDen * 10000) / 10000) + ".</div>";
    $(pre + "-salida").innerHTML = h;
  }
  panel.querySelectorAll("input").forEach(function(x){ x.addEventListener("input", pinta); });
  panel.querySelectorAll("select").forEach(function(x){ x.addEventListener("change", pinta); });
  pinta();
}
function genCon(){
  var n = bolsaAzar(), T0 = n[0] + n[1] + n[2], c = coloresConHay(n), a = elige(c), b = elige(c), p = fr(n[a] * n[b], T0 * T0);
  return {enun: textoBolsa(n) + T(" You draw a candy, <strong>put it back</strong>, and draw another. What is the probability of " + COLORES[a].n + " and then " + COLORES[b].n + "?", " Se saca un caramelo, <strong>se devuelve</strong> y se saca otro. ¿Cuál es la probabilidad de sacar " + COLORES[a].n + " y luego " + COLORES[b].n + "?"),
    solucion: T("With replacement the total is still " + T0 + ": ", "Con reemplazo el total sigue siendo " + T0 + ": ") + fracHTML(n[a], T0) + " × " + fracHTML(n[b], T0) + " = " + fracHTML(n[a] * n[b], T0 * T0) + (mcd(n[a] * n[b], T0 * T0) > 1 ? " = " + fracHTML(p.n, p.d) : "") + ".",
    evalua: function(v){ return evaluaProb(v, p, [{v: fr(n[a] * (n[b] - (a === b ? 1 : 0)), T0 * (T0 - 1)), msg: T("That would be without replacement. Here the candy goes back: the bag does not change.", "Así sería sin reemplazo. Aquí el caramelo se devuelve: la bolsa no cambia.")}, {v: fr(n[a] + n[b], T0), msg: T("For both events to happen, multiply the probabilities; do not add them.", "Para que ocurran los dos eventos se multiplican las probabilidades, no se suman.")}]); }};
}
function genSin(){
  var n = bolsaAzar(), T0 = n[0] + n[1] + n[2], c = coloresConHay(n), a = elige(c), b = elige(c);
  if (a === b && n[a] < 2) b = elige(c.filter(function(x){ return x !== a; }).concat([a]));
  var f2 = n[b] - (a === b ? 1 : 0), p = fr(n[a] * f2, T0 * (T0 - 1));
  var pistas = [{v: fr(n[a] * n[b], T0 * T0), msg: T("That would be with replacement. Without replacement, there is one candy fewer for the second draw.", "Así sería con reemplazo. Sin reemplazo, en la segunda extracción queda un caramelo menos.")}];
  if (a === b) pistas.push({v: fr(n[a] * n[b], T0 * (T0 - 1)), msg: T("The denominator is right, but the numerator goes down too: a " + COLORES[a].n + " candy already came out.", "El denominador está bien, pero también baja el numerador: ya salió un caramelo " + COLORES[a].n + ".")});
  return {enun: textoBolsa(n) + T(" You draw a candy, <strong>do not put it back</strong>, and draw another. What is the probability of " + COLORES[a].n + " and then " + COLORES[b].n + "?", " Se saca un caramelo, <strong>no se devuelve</strong>, y se saca otro. ¿Cuál es la probabilidad de sacar " + COLORES[a].n + " y luego " + COLORES[b].n + "?"),
    solucion: T("First ", "Primero ") + fracHTML(n[a], T0) + T("; then " + (T0 - 1) + " candies are left and " + f2 + " are " + COLORES[b].n + ": ", "; después quedan " + (T0 - 1) + " caramelos y " + cuenta(f2, b) + ": ") + fracHTML(f2, T0 - 1) + T(". Product: ", ". Producto: ") + fracHTML(n[a] * f2, T0 * (T0 - 1)) + (p.n !== 0 && mcd(n[a] * f2, T0 * (T0 - 1)) > 1 ? " = " + fracHTML(p.n, p.d) : "") + ".",
    evalua: function(v){ return evaluaProb(v, p, pistas, T("After the first draw, take 1 away from the total (and from the color that came out, if it is the same).", "Después de la primera extracción, reste 1 al total (y al color que salió, si es el mismo).")); }};
}

/* MODULE 4 · Three forms */
function aFraccionDec(v){ for (var k = 0; k <= 6; k++){ var d = Math.pow(10, k); if (Math.abs(Math.round(v * d) - v * d) < 1e-9) return reduce(Math.round(v * d), d); } return null; }
function pintaTF(){
  var s = $("tf-v").value, v = leeProb(s), sal = $("tf-salida");
  if (v === null){ sal.innerHTML = '<div class="linea">' + T("Type a fraction (3/8), a decimal (0.375), or a percent (37.5%).", "Escriba una fracción (3/8), un decimal (0.375) o un porcentaje (37.5%).") + "</div>"; return; }
  var f = leeFraccion(String(s).trim().replace(/\s+/g, "")), fr_ = f && f.q !== 1 ? reduce(f.p, f.q) : aFraccionDec(v);
  var h = '<div class="linea">' + T("Fraction: ", "Fracción: ") + (fr_ ? fracHTML(fr_.p, fr_.q) : "—") + '</div><div class="linea">' + T("Decimal: ", "Decimal: ") + nm(Math.round(v * 10000) / 10000) + '</div><div class="linea">' + T("Percent: ", "Porcentaje: ") + nm(Math.round(v * 100000) / 1000) + "%</div>";
  if (v < 0 || v > 1) h += '<div class="linea veredicto">' + T("That value cannot be a probability: every probability is between 0 and 1 (between 0% and 100%).", "Ese valor no puede ser una probabilidad: toda probabilidad está entre 0 y 1 (entre 0% y 100%).") + "</div>";
  else h += '<div class="linea veredicto">' + (v === 0 ? T("Probability 0: the event is impossible.", "Probabilidad 0: el evento es imposible.") : (v === 1 ? T("Probability 1: the event is certain.", "Probabilidad 1: el evento es seguro.") : T("It is a valid probability: it is between 0 and 1.", "Es una probabilidad válida: está entre 0 y 1."))) + "</div>";
  sal.innerHTML = h;
}
function genTres(){
  var tp = aleatorio(1, 4), par = elige([[1, 4], [3, 4], [1, 2], [1, 5], [2, 5], [3, 8], [1, 8], [7, 10], [3, 20], [9, 25]]), v = par[0] / par[1], o, pc = {};
  if (tp === 1){ var d = nm(v); o = [{html: d, clave: "a"}, {html: nm(v + 0.1), clave: "b"}, {html: nm(par[1] / par[0]), clave: "c"}, {html: (par[0] + "." + par[1] === nm(par[1] / par[0]) ? nm(v * 10) : par[0] + "." + par[1]), clave: "d"}];
    pc.c = T("Divide the numerator by the denominator, not the other way around.", "Se divide el numerador entre el denominador, no al revés."); if (par[0] + "." + par[1] !== nm(par[1] / par[0])) pc.d = T("You cannot convert a fraction by joining its numbers with a point.", "Una fracción no se convierte juntando sus números con un punto.");
    return {enun: T("Write ", "Escriba ") + fracHTML(par[0], par[1]) + T(" as a decimal.", " como decimal."), opciones: o, correcta: "a", porClave: pc, pista: T("Divide the numerator by the denominator.", "Divida el numerador entre el denominador."), bien: par[0] + " ÷ " + par[1] + " = " + d + ".", mal: par[0] + " ÷ " + par[1] + " = " + d + "."}; }
  if (tp === 2){ var pp = nm(v * 100); o = [{html: pp + "%", clave: "a"}, {html: nm(v) + "%", clave: "b"}, {html: nm(v * 1000) + "%", clave: "c"}, {html: par[0] + "%", clave: "d"}];
    pc.b = T("You still need to multiply the decimal by 100.", "Falta multiplicar el decimal por 100."); pc.c = T("Multiply by 100, not by 1,000.", "Se multiplica por 100, no por 1,000.");
    return {enun: T("Write ", "Escriba ") + fracHTML(par[0], par[1]) + T(" as a percent.", " como porcentaje."), opciones: o, correcta: "a", porClave: pc, pista: T("First divide to get the decimal, then multiply by 100.", "Primero divida para obtener el decimal y después multiplique por 100."), bien: par[0] + " ÷ " + par[1] + " = " + nm(v) + T(", and × 100 = ", ", y × 100 = ") + pp + "%.", mal: par[0] + " ÷ " + par[1] + " = " + nm(v) + T(", and × 100 = ", ", y × 100 = ") + pp + "%."}; }
  if (tp === 3){ var pc100 = Math.round(v * 100); if (Math.abs(pc100 - v * 100) > 1e-9) return genTres(); var r = reduce(pc100, 100);
    o = [opF(r.p, r.q), opF(pc100, 10), {html: fracHTML(1, pc100), clave: "inv"}, opF(pc100 + 5, 100)];
    return {enun: T("Write " + pc100 + "% as a simplified fraction.", "Escriba " + pc100 + "% como fracción simplificada."), opciones: o, correcta: o[0].clave, porClave: {}, pista: T("Write it over 100 and simplify.", "Escríbalo sobre 100 y simplifique."), bien: pc100 + "% = " + fracHTML(pc100, 100) + " = " + fracHTML(r.p, r.q) + ".", mal: pc100 + "% = " + fracHTML(pc100, 100) + " = " + fracHTML(r.p, r.q) + "."}; }
  var malo = elige([["1.2", T("is greater than 1", "es mayor que 1")], ["120%", T("is more than 100%", "pasa del 100%")], ["−0.3", T("is negative", "es negativo")], [fracHTML(5, 4), T("is greater than 1", "es mayor que 1")]]);
  var buenos = baraja(["0.95", "3%", fracHTML(7, 8), "0", "100%", "0.5"]).slice(0, 3);
  o = [{html: malo[0], clave: "m"}].concat(buenos.map(function(b, i){ return {html: b, clave: "b" + i}; }));
  return {enun: T("Which of these values <strong>cannot</strong> be a probability?", "¿Cuál de estos valores <strong>no</strong> puede ser una probabilidad?"), opciones: o, correcta: "m", porClave: {}, pista: T("A probability is between 0 and 1, that is, between 0% and 100%.", "Una probabilidad está entre 0 y 1, es decir, entre 0% y 100%."),
    bien: T("It " + malo[1] + ": a probability is always between 0 and 1.", "Ese valor " + malo[1] + ": una probabilidad está siempre entre 0 y 1."), mal: T("The one that cannot be is ", "El que no puede ser es ") + malo[0] + T(", because it " + malo[1] + ".", ", porque " + malo[1] + ".")};
}

/* Start */
OMR("p1", genSimple);
creaBolsa("bc", true);
creaPracticaLibre("p2", genCon);
creaBolsa("bs", false);
creaPracticaLibre("p3", genSin);
$("tf-v").addEventListener("input", pintaTF); pintaTF();
OMR("p4", genTres);
'''

def practica_pagina():
    n = N
    azar = t('<a href="explore-chance.html">Explore: chance experiments</a>', '<a href="explorar-azar.html">Explorar: experimentos de azar</a>')
    arbol = t('<a href="explore-tree.html">Explore: from the tree to the table</a>', '<a href="explorar-arbol.html">Explorar: del árbol a la tabla</a>')
    def libre(pid, tit, et, nota):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota}</p>\n        <div class="fila-btn">', 1)
    fx_ = lambda a, b: f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'
    mods = [
     (t("one-event", "un-evento"), t("The probability of one event", "Probabilidad de un evento"),
      f'''      <p>{t("The probability of an event is the ratio of the favorable cases to the possible cases. It is always between 0 (impossible) and 1 (certain).", "La probabilidad de un evento es la razón entre los casos favorables y los casos posibles. Siempre está entre 0 (imposible) y 1 (seguro).")}</p>
{n3.formula(t("P(event) = ", "P(evento) = ") + fx_(t("favorable cases", "casos favorables"), t("possible cases", "casos posibles")))}
      <div class="caja-tip">{t(f"<strong>Chance experiments:</strong> in {azar} you can roll two dice, draw cards, and spin a spinner 1, 10, or 100 times, and compare the theoretical probability (the formula) with the experimental one (what happens when you repeat it).", f"<strong>Experimentos de azar:</strong> en {azar} puede lanzar dos dados, sacar cartas y girar una ruleta 1, 10 o 100 veces, y comparar la probabilidad teórica (la de la fórmula) con la experimental (la que sale al repetir).")}</div>
{B.om("p1", t("Practice: the probability of one event", "Practique: probabilidad de un evento"))}'''),
     (t("with", "con"), t("Two events with replacement", "Dos eventos con reemplazo"),
      f'''      <p>{t("If the object goes back after the first draw, the bag is the same for the second one: the events are <strong>independent</strong>. The probability of both is the product.", "Si después de la primera extracción el objeto se devuelve, la bolsa queda igual para la segunda: los eventos son <strong>independientes</strong>. La probabilidad de los dos es el producto.")}</p>
{n3.formula(t("P(A and B) = P(A) × P(B)", "P(A y B) = P(A) × P(B)"))}
      <h3>{t("The bag that does not change", "La bolsa que no cambia")}</h3>
      <div class="panel" id="bc-panel"></div>
{libre("p2", t("Practice: with replacement", "Practique: con reemplazo"), t("Probability", "Probabilidad"), t("Write a fraction (like 4/27), a decimal, or a percent. You do not need to simplify.", "Escriba una fracción (como 4/27), un decimal o un porcentaje. No hace falta simplificar."))}'''),
     (t("without", "sin"), t("Two events without replacement", "Dos eventos sin reemplazo"),
      f'''      <p>{t("If the object does not go back, the bag changes: there is one fewer in all, and one fewer of the kind that came out. The events are <strong>dependent</strong>.", "Si el objeto no se devuelve, la bolsa cambia: queda uno menos en total, y uno menos del tipo que salió. Los eventos son <strong>dependientes</strong>.")}</p>
{n3.formula(t("P(A and B) = P(A) × P(B after A)", "P(A y B) = P(A) × P(B después de A)"))}
      <h3>{t("The bag that loses one", "La bolsa que pierde un elemento")}</h3>
      <div class="panel" id="bs-panel"></div>
      <div class="caja-tip">{t("<strong>Adjust both numbers:</strong> on the second draw the denominator always goes down by 1, and the numerator goes down by 1 only if you want the same color that already came out.", "<strong>Ajuste los dos números:</strong> en la segunda extracción el denominador siempre baja en 1, y el numerador baja en 1 solo si se busca el mismo color que ya salió.")}</div>
{libre("p3", t("Practice: without replacement", "Practique: sin reemplazo"), t("Probability", "Probabilidad"), t("Write a fraction (like 2/7), a decimal, or a percent. You do not need to simplify.", "Escriba una fracción (como 2/7), un decimal o un porcentaje. No hace falta simplificar."))}'''),
     (t("tree", "arbol"), t("From the tree to the table", "Del árbol a la tabla"),
      f'''      <p>{t("A tree diagram shows all the possibilities of two draws: on each branch you write its probability, and the probability of a whole path is the product of its branches. The probabilities of all the paths add up to 1. A two-way table organizes the same results.", "Un diagrama de árbol muestra todas las posibilidades de dos extracciones: en cada rama se escribe su probabilidad, y la probabilidad de un camino completo es el producto de sus ramas. Las probabilidades de todos los caminos suman 1. Una tabla de doble entrada organiza los mismos resultados.")}</p>
      <div class="caja-tip">{t(f"Build a tree step by step, with or without replacement, and see it become a table in {arbol}.", f"Construya un árbol paso a paso, con o sin reemplazo, y véalo convertirse en tabla en {arbol}.")}</div>
      <div class="caja-tip">{t("<strong>To check a tree:</strong> add the probabilities of all the paths. If they do not add up to 1, a branch is wrong.", "<strong>Para comprobar un árbol:</strong> sume las probabilidades de todos los caminos. Si no da 1, hay una rama mal calculada.")}</div>'''),
     (t("three-forms", "tres-formas"), t("Fraction, decimal, and percent", "Fracción, decimal y porcentaje"),
      f'''      <p>{t("A probability can be written in three ways. The test often asks for one in particular.", "Una probabilidad se puede escribir de tres formas. El examen suele pedir una en particular.")}</p>
      <table class="reglas"><caption>{t("How to go from one form to another", "Cómo pasar de una forma a otra")}</caption>
        <thead><tr><th scope="col">{t("From", "De")}</th><th scope="col">{t("To", "A")}</th><th scope="col">{t("What to do", "Se hace")}</th></tr></thead>
        <tbody><tr><td>{t("Fraction", "Fracción")}</td><td>{t("Decimal", "Decimal")}</td><td>{t("divide the numerator by the denominator", "se divide el numerador entre el denominador")}</td></tr>
        <tr><td>{t("Decimal", "Decimal")}</td><td>{t("Percent", "Porcentaje")}</td><td>{t("multiply by 100", "se multiplica por 100")}</td></tr>
        <tr><td>{t("Percent", "Porcentaje")}</td><td>{t("Fraction", "Fracción")}</td><td>{t("write it over 100 and simplify", "se escribe sobre 100 y se simplifica")}</td></tr></tbody></table>
      <h3>{t("Converter", "Conversor")}</h3>
      <div class="panel"><div class="campo"><label for="tf-v">{t("Probability (fraction, decimal, or percent)", "Probabilidad (fracción, decimal o porcentaje)")}</label><input type="text" id="tf-v" class="ancho" value="3/8" autocomplete="off"></div></div>
{n3.salida("tf-salida")}
      <div class="caja-tip">{t("<strong>Every probability is between 0 and 1:</strong> if a calculation gives more than 1 (or more than 100%), there is a mistake; you probably added when you needed to multiply.", "<strong>Toda probabilidad está entre 0 y 1:</strong> si un cálculo da más de 1 (o más de 100%), hay un error; probablemente se sumó cuando había que multiplicar.")}</div>
{B.om("p4", t("Practice: the three forms", "Practique: las tres formas"))}''')]
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO8, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Probabilidad compuesta: con y sin reemplazo")
