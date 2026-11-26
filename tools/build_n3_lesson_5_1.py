"""Level 3 · Lesson 5.1 · Solving linear inequalities and graphing them on the number line — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "5-1"
TEMA = ("Inequalities and formulas", "Inecuaciones y fórmulas")
TIT = ("Solving linear inequalities and graphing them on the number line", "Resolver inecuaciones lineales y graficar en la recta numérica")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js")

def recta(v, r, lo=0, hi=5):
    """Static number line for the lesson: open or closed point at v and a ray."""
    der = r in (">", "≥")
    abierto = r in ("<", ">")
    W, y, x0, x1 = 640, 52, 40, 600
    X = lambda n: x0 + (n - lo) * (x1 - x0) / (hi - lo)
    rv = {"<": "&lt;", ">": "&gt;"}.get(r, r)
    lab = t(f"Number line from {lo} to {hi}: {'an open' if abierto else 'a closed'} point at {v} and an arrow to the {'right' if der else 'left'}, the graph of x {rv} {v}.",
            f"Recta numérica de {lo} a {hi}: punto {'abierto' if abierto else 'cerrado'} en {v} y flecha hacia la {'derecha' if der else 'izquierda'}, la gráfica de x {rv} {v}.")
    s = f'<figure style="margin:14px 0"><svg viewBox="0 0 {W} 100" role="img" aria-label="{lab}" style="max-width:640px;width:100%;height:auto;display:block;margin:0 auto">'
    s += f'<line x1="{x0 - 16}" y1="{y}" x2="{x1 + 16}" y2="{y}" stroke="#424242" stroke-width="2"/>'
    for n in range(lo, hi + 1):
        s += f'<line x1="{X(n)}" y1="{y - 9}" x2="{X(n)}" y2="{y + 9}" stroke="#424242" stroke-width="2"/><text x="{X(n)}" y="{y + 36}" text-anchor="middle" font-size="22">{n}</text>'
    xc, fin = X(v), (x1 + 20 if der else x0 - 20)
    s += f'<line x1="{xc}" y1="{y}" x2="{fin}" y2="{y}" stroke="#0d47a1" stroke-width="8"/>'
    s += f'<path d="M{fin + 10 if der else fin - 10} {y} l{-18 if der else 18} -12 v24 z" fill="#0d47a1"/>'
    s += f'<circle cx="{xc}" cy="{y}" r="11" fill="{"#fff" if abierto else "#0d47a1"}" stroke="#0d47a1" stroke-width="4"/></svg></figure>'
    return s

def leccion():
    n = N
    s1 = f'''<p>{t("In Topic 4 you solved linear equations, where the solution is a single value. An <strong>inequality</strong> uses the signs <, >, ≤, or ≥ instead of the equal sign, and its solution is not one number but a <strong>range</strong> of values. The good news: you solve it with the same steps as an equation. The only difference, and it is crucial, appears when you multiply or divide by a negative number.",
"En el Tema 4 se resolvieron ecuaciones lineales, donde la solución es un único valor. Una <strong>inecuación</strong> usa los signos <, >, ≤ o ≥ en lugar del igual, y su solución no es un solo número, sino un <strong>rango</strong> de valores. La buena noticia: se resuelve con los mismos pasos que una ecuación. La única diferencia —y es crucial— aparece al multiplicar o dividir por un número negativo.")}</p>
{tabla(t("The inequality signs", "Los signos de desigualdad"), t("Meaning of the inequality signs", "Significado de los signos de desigualdad"), [t("Sign", "Signo"), t("Meaning", "Significado"), t("Example", "Ejemplo")],
  [["&lt;", t("Less than", "Menor que"), "x &lt; 5"], ["&gt;", t("Greater than", "Mayor que"), "x &gt; 5"], ["≤", t("Less than or equal to", "Menor o igual que"), "x ≤ 5"], ["≥", t("Greater than or equal to", "Mayor o igual que"), "x ≥ 5"]])}
{caja("tip", t("A solution is a range", "Una solución es un rango"), t("<p>x > 3 does not mean one value, but every number greater than 3 (3.1, 4, 100, …). That is why the solution is shown on the number line, not as a single point.</p>", "<p>x > 3 no significa un valor, sino todos los números mayores que 3 (3.1, 4, 100, …). Por eso la solución se representa en la recta numérica, no como un punto único.</p>"))}'''

    s2 = f'''<p>{t("As long as you do not multiply or divide by a negative number, you solve an inequality exactly like an equation: add, subtract, multiply, or divide both sides.", "Mientras no se multiplique ni se divida por un número negativo, una inecuación se resuelve exactamente igual que una ecuación: sumando, restando, multiplicando o dividiendo ambos lados.")}</p>
{ejemplo(t("Example 1: solve x + 5 &lt; 12", "Ejemplo 1: resuelva x + 5 &lt; 12"),
  [("1", t("Subtract 5 from both sides.", "Restar 5 en ambos lados."), "x &lt; 7."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>x &lt; 7</strong> (every value less than 7).", "<strong>x &lt; 7</strong> (todos los valores menores que 7)."))])}
{ejemplo(t("Example 2: solve 3x ≤ 15", "Ejemplo 2: resuelva 3x ≤ 15"),
  [("1", t("Divide by 3.", "Dividir entre 3."), t("3 is positive, so the sign does not flip: x ≤ 5.", "3 es positivo, así que el signo no se invierte: x ≤ 5.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>x ≤ 5</strong>")])}
{enlace(n, t("solve", "resolver"), t("solving like an equation", "resolver como una ecuación"), t("Use the same steps as in an equation.", "Aplique los mismos pasos que en una ecuación."))}'''

    s3 = f'''<p>{t("When you <strong>multiply or divide</strong> both sides by a <strong>negative</strong> number, the inequality sign <strong>flips</strong>. This does not happen with equations; it is the only real difference.", "Al <strong>multiplicar o dividir</strong> ambos lados por un número <strong>negativo</strong>, el signo de la desigualdad <strong>se invierte</strong>. Esto no ocurre con las ecuaciones; es la única diferencia real.")}</p>
{caja("tip", t("Why it flips", "Por qué se invierte"), t("<p>You know that 6 > 4. If you multiply both sides by −1, you get −6 and −4. But −6 > −4 is false (−6 is farther to the left). For the statement to stay true, the sign has to flip: −6 < −4.</p>", "<p>Se sabe que 6 > 4. Si se multiplican ambos lados por −1, se obtiene −6 y −4. Pero −6 > −4 es falso (−6 está más a la izquierda). Para que siga siendo verdadero, el signo debe invertirse: −6 < −4.</p>"))}
{ejemplo(t("Example 3: solve −2x &lt; 8", "Ejemplo 3: resuelva −2x &lt; 8"),
  [("1", t("Divide both sides by −2.", "Dividir entre −2 en ambos lados."), t("You divide by a negative number…", "Se divide por un negativo…")),
   ("2", t("Flip the sign.", "Invertir el signo."), "x &gt; −4."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x &gt; −4</strong>")])}
{caja("ojo", t("Only with negatives", "Solo con negativos"), t("<p>The sign flips only when you multiply or divide by a negative number. Adding or subtracting a negative number does not flip it. The most common mistake is to flip it when you should not.</p>", "<p>El signo se invierte únicamente al multiplicar o dividir por un número negativo. Sumar o restar un negativo no lo invierte. El error más común es invertirlo sin que corresponda.</p>"))}
{practica("p1", t("Practice 1 — Divide by a negative", "Práctica 1 — Dividir entre un negativo"), "−3x &lt; 9", [("a", "x &lt; −3"), ("b", "x &gt; −3"), ("c", "x &gt; 3")])}
{practica("p2", t("Practice 2 — Divide by a positive", "Práctica 2 — Dividir entre un positivo"), "2x &gt; 10", [("a", "x &lt; 5"), ("b", "x &gt; 20"), ("c", "x &gt; 5")])}
{practica("p3", t("Practice 3 — A minus sign in front", "Práctica 3 — Un signo menos delante"), "−x ≤ 4", [("a", "x ≥ −4"), ("b", "x ≤ −4"), ("c", "x ≥ 4")])}
{enlace(n, t("flip", "invertir"), t("the critical rule: flipping the sign", "la regla crítica: invertir el signo"), t("See what happens when you multiply or divide by a negative number.", "Practique qué ocurre al multiplicar o dividir por un número negativo."))}'''

    s4 = f'''<p>{t("You draw the solution on the number line with two decisions: the kind of point and the direction of the arrow.", "La solución se dibuja en la recta numérica con dos decisiones: el tipo de punto y la dirección de la flecha.")}</p>
{tabla(t("Point and direction", "Punto y dirección"), t("Kind of point and direction of the arrow for each inequality sign", "Tipo de punto y dirección de la flecha según el signo de la inecuación"), [t("Sign", "Signo"), t("Point at the boundary", "Punto en el número límite"), t("Arrow", "Flecha")],
  [["x &lt; a", t("Open ○ (not included)", "Abierto ○ (no se incluye)"), t("To the left", "Hacia la izquierda")], ["x ≤ a", t("Closed ● (included)", "Cerrado ● (sí se incluye)"), t("To the left", "Hacia la izquierda")],
   ["x &gt; a", t("Open ○", "Abierto ○"), t("To the right", "Hacia la derecha")], ["x ≥ a", t("Closed ●", "Cerrado ●"), t("To the right", "Hacia la derecha")]])}
<p>{t("For example, the solution x ≥ 2 uses a closed point at 2 and an arrow to the right:", "Por ejemplo, la solución x ≥ 2 usa un punto cerrado en 2 y una flecha hacia la derecha:")}</p>
{recta(2, "≥")}
<p>{t("On the other hand, the solution x < 4 uses an open point at 4 and an arrow to the left:", "En cambio, la solución x < 4 usa un punto abierto en 4 y una flecha hacia la izquierda:")}</p>
{recta(4, "<")}
{practica("p4", t("Practice 4 — The point", "Práctica 4 — El punto"), t("To graph x ≤ 7, the point at 7 is…", "Para graficar x ≤ 7, el punto en 7 es…"), [("a", t("Open ○", "Abierto ○")), ("b", t("Not marked", "No se marca")), ("c", t("Closed ●", "Cerrado ●"))])}
{practica("p5", t("Practice 5 — A strict sign", "Práctica 5 — Un signo estricto"), t("To graph x &gt; 1, the point at 1 is…", "Para graficar x &gt; 1, el punto en 1 es…"), [("a", t("Open ○", "Abierto ○")), ("b", t("Closed ●", "Cerrado ●")), ("c", t("Not marked", "No se marca"))])}
{practica("p6", t("Practice 6 — The arrow", "Práctica 6 — La flecha"), t("For x ≥ 0, which way does the arrow go?", "En x ≥ 0, ¿hacia dónde va la flecha?"), [("a", t("To the left", "A la izquierda")), ("b", t("To the right", "A la derecha")), ("c", t("There is no arrow", "No hay flecha"))])}
{enlace(n, t("graph", "graficar"), t("graphing on the number line", "graficar en la recta numérica"), t("Choose an open or closed point and the direction of the arrow.", "Elija punto abierto o cerrado y la dirección de la flecha."))}'''

    s5 = f'''<p>{t("To check a solution, choose three values: one clearly inside the range, the boundary number, and one outside. When you substitute them, only the values in the range should make the inequality true.", "Para comprobar una solución, se eligen tres valores: uno claramente dentro del rango, el número límite y uno fuera. Al sustituirlos, solo los del rango deben hacer verdadera la inecuación.")}</p>
{ejemplo(t("Example 4: check the solution x &gt; −4 of −2x &lt; 8", "Ejemplo 4: compruebe la solución x &gt; −4 de −2x &lt; 8"),
  [("1", t("A value inside, x = 0.", "Un valor dentro, x = 0."), t("−2(0) = 0, and 0 < 8 is true. Correct.", "−2(0) = 0, y 0 < 8 es verdadero. Correcto.")),
   ("2", t("A value outside, x = −5.", "Un valor fuera, x = −5."), t("−2(−5) = 10, and 10 < 8 is false. It is right that it is left out.", "−2(−5) = 10, y 10 < 8 es falso. Correcto que quede fuera.")),
   ("✓", t("Answer.", "Respuesta."), t("The solution x > −4 is confirmed.", "La solución x > −4 se confirma."))])}
{enlace(n, t("test-value", "prueba"), t("checking with a test value", "verificar con un valor de prueba"), t("Choose a number and check it in the original inequality.", "Elija un número y compruébelo en la inecuación original."))}'''

    secciones = [("s-" + t("what-is", "que-es"), t("What is an inequality?", "¿Qué es una inecuación?"), s1),
                 ("s-" + t("same-steps", "mismos-pasos"), t("Solving with the same steps as an equation", "Resolver con los mismos pasos que una ecuación"), s2),
                 ("s-" + t("flip", "invertir"), t("The critical rule: flipping the sign", "La regla crítica: invertir el signo"), s3),
                 ("s-" + t("graph", "graficar"), t("Graphing on the number line", "Graficar en la recta numérica"), s4),
                 ("s-" + t("test-value", "prueba"), t("Checking with a test value", "Verificar con un valor de prueba"), s5)]

    AB, CE = t("Open ○", "Abierto ○"), t("Closed ●", "Cerrado ●")
    lesson = {"next": t("Lesson 5.2", "Lección 5.2"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The number is right, but you divided by −3: the sign has to flip.", "El número está bien, pero se dividió entre −3: el signo tiene que invertirse."), "c": t("9 ÷ (−3) = −3, not 3.", "9 ÷ (−3) = −3, no 3.")}, "right": t("Dividing by −3 flips the sign: x > −3.", "Al dividir entre −3 el signo se invierte: x > −3."), "solution": t("Divide by −3 and flip the sign: x > −3.", "Se divide entre −3 y se invierte el signo: x > −3.")},
      "p2": {"ok": "c", "hints": {"a": t("2 is positive: the sign does not flip.", "2 es positivo: el signo no se invierte."), "b": t("Divide by 2; do not multiply.", "Se divide entre 2, no se multiplica.")}, "right": "10 ÷ 2 = 5: x > 5.", "solution": t("Divide by 2 (positive): x > 5.", "Se divide entre 2 (positivo): x > 5.")},
      "p3": {"ok": "a", "hints": {"b": t("−x means −1 · x: dividing by −1 flips the sign.", "−x es −1 · x: al dividir entre −1 el signo se invierte."), "c": t("4 ÷ (−1) = −4.", "4 ÷ (−1) = −4.")}, "right": t("Dividing by −1 flips the sign: x ≥ −4.", "Al dividir entre −1 el signo se invierte: x ≥ −4."), "solution": t("Divide by −1 and flip the sign: x ≥ −4.", "Se divide entre −1 y se invierte el signo: x ≥ −4.")},
      "p4": {"ok": "c", "hints": {"a": t("≤ includes the 7.", "≤ incluye al 7."), "b": t("The boundary is always marked, open or closed.", "El límite siempre se marca, abierto o cerrado.")}, "right": t("≤ includes 7: closed point.", "≤ incluye al 7: punto cerrado."), "solution": t("Closed point, because ≤ includes the 7.", "Punto cerrado, porque ≤ incluye al 7.")},
      "p5": {"ok": "a", "hints": {"b": t("> does not include the 1.", "> no incluye al 1."), "c": t("The boundary is always marked, open or closed.", "El límite siempre se marca, abierto o cerrado.")}, "right": t("> does not include 1: open point.", "> no incluye al 1: punto abierto."), "solution": t("Open point, because > does not include the 1.", "Punto abierto, porque > no incluye al 1.")},
      "p6": {"ok": "b", "hints": {"a": t("≥ means greater: those numbers are to the right.", "≥ indica mayores: están a la derecha."), "c": t("The solution is a range, so there is an arrow.", "La solución es un rango, así que hay flecha.")}, "right": t("Greater numbers are to the right.", "Los números mayores están a la derecha."), "solution": t("To the right, toward the greater numbers.", "Hacia la derecha, hacia los números mayores.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Subtracting does not flip the sign.", "Restar no invierte el signo."), "c": t("Subtract 5; do not add it.", "Se resta 5, no se suma."), "d": t("Subtract 5 and keep the sign.", "Se resta 5 y se conserva el signo.")}, "solution": "x < 12 − 5 = 7."},
      "B": {"ok": "c", "hints": {"a": t("The number is right, but the sign must flip.", "El número está bien, pero el signo debe invertirse."), "b": t("8 ÷ (−2) = −4.", "8 ÷ (−2) = −4."), "d": t("Dividing by −2 flips the sign and gives −4.", "Dividir entre −2 invierte el signo y da −4.")}, "solution": t("Divide by −2 and flip: x > −4.", "Se divide entre −2 y se invierte: x > −4.")},
      "C": {"ok": "a", "hints": {"b": t("Dividing by −1 flips the sign.", "Dividir entre −1 invierte el signo."), "c": t("3 ÷ (−1) = −3.", "3 ÷ (−1) = −3."), "d": t("Flip the sign and change the number's sign.", "Invierta el signo y cambie el signo del número.")}, "solution": t("Divide by −1: x ≤ −3.", "Se divide entre −1: x ≤ −3.")},
      "D": {"ok": "c", "hints": {"a": t("≥ includes the 2.", "≥ incluye al 2."), "b": t("The boundary is always marked.", "El límite siempre se marca."), "d": t("It depends only on the sign.", "Depende solo del signo.")}, "solution": t("Closed, because ≥ includes the 2.", "Cerrado, porque ≥ incluye al 2.")},
      "E": {"ok": "b", "hints": {"a": t("< does not include 5, and it points to the smaller numbers.", "< no incluye al 5 y apunta a los menores."), "c": t("< points to the smaller numbers: left.", "< apunta a los menores: izquierda."), "d": t("< does not include 5: open point.", "< no incluye al 5: punto abierto.")}, "solution": t("Open point, arrow to the left.", "Punto abierto, flecha a la izquierda.")},
      "F": {"ok": "a", "hints": {"b": t("A closed point means the 3 is included.", "El punto cerrado indica que el 3 se incluye."), "c": t("To the right means greater.", "Hacia la derecha indica mayores."), "d": t("Closed and to the right.", "Cerrado y hacia la derecha.")}, "solution": "x ≥ 3."},
      "G": {"ok": "d", "hints": {"a": t("Is 4 less than 4?", "¿4 es menor que 4?"), "b": t("< does not include the boundary.", "< no incluye el límite."), "c": t("Substitute: 4 < 4 is false.", "Sustituya: 4 < 4 es falso.")}, "solution": t("4 < 4 is false.", "4 < 4 es falso.")},
      "H": {"ok": "a", "hints": {"b": t("−1 is to the right of −3.", "−1 está a la derecha de −3."), "c": t("Many values work, not only −3.", "Funcionan muchos valores, no solo −3."), "d": t("−1 is a real number.", "−1 es un número real.")}, "solution": t("−1 ≥ −3 is true.", "−1 ≥ −3 es verdadero.")}
     }}

    quiz = [
     ("A", t("Solve: x + 5 &lt; 12.", "Resuelva: x + 5 &lt; 12."), [("a", "x &gt; 7"), ("b", "x &lt; 7"), ("c", "x &lt; 17"), ("d", "x &gt; 17")]),
     ("B", t("Solve: −2x &lt; 8.", "Resuelva: −2x &lt; 8."), [("a", "x &lt; −4"), ("b", "x &gt; 4"), ("c", "x &gt; −4"), ("d", "x &lt; 4")]),
     ("C", t("Solve: −x ≥ 3.", "Resuelva: −x ≥ 3."), [("a", "x ≤ −3"), ("b", "x ≥ −3"), ("c", "x ≤ 3"), ("d", "x ≥ 3")]),
     ("D", t("To graph x ≥ 2, the point at 2 is…", "Para graficar x ≥ 2, el punto en 2 es…"), [("a", AB), ("b", t("Not marked", "No se marca")), ("c", CE), ("d", t("It depends on the value", "Depende del valor"))]),
     ("E", t("To graph x &lt; 5: point and direction?", "Para graficar x &lt; 5, ¿punto y dirección?"), [("a", t("Closed ●, arrow to the right", "Cerrado ●, flecha a la derecha")), ("b", t("Open ○, arrow to the left", "Abierto ○, flecha a la izquierda")), ("c", t("Open ○, arrow to the right", "Abierto ○, flecha a la derecha")), ("d", t("Closed ●, arrow to the left", "Cerrado ●, flecha a la izquierda"))]),
     ("F", t("Which inequality shows “closed point at 3, arrow to the right”?", "¿Qué desigualdad muestra «punto cerrado en 3, flecha a la derecha»?"), [("a", "x ≥ 3"), ("b", "x &gt; 3"), ("c", "x ≤ 3"), ("d", "x &lt; 3")]),
     ("G", t("Does x = 4 satisfy x &lt; 4?", "¿x = 4 satisface x &lt; 4?"), [("a", t("Yes", "Sí")), ("b", t("Yes, because 4 = 4", "Sí, porque 4 = 4")), ("c", t("Only sometimes", "Solo a veces")), ("d", t("No, because 4 is not less than 4", "No, porque 4 no es menor que 4"))]),
     ("H", t("Does x = −1 satisfy x ≥ −3?", "¿x = −1 satisface x ≥ −3?"), [("a", t("Yes", "Sí")), ("b", "No"), ("c", t("Only if x = −3", "Solo si x = −3")), ("d", t("It is not a real number", "No es un número real"))])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Solve inequalities with the same steps as equations, flip the sign when you multiply or divide by a negative, and graph the solution.", "Resuelva inecuaciones con los mismos pasos que las ecuaciones, invierta el signo al multiplicar o dividir por un negativo y grafique la solución."),
        ("✏️", t("No calculator needed", "Sin calculadora")),
        [t("<strong>Solve</strong> linear inequalities in one variable with the same steps as an equation.", "<strong>Resolver</strong> inecuaciones lineales en una variable con los mismos pasos que una ecuación."),
         t("<strong>Apply</strong> the critical rule: flip the inequality sign when you multiply or divide by a negative number.", "<strong>Aplicar</strong> la regla crítica: invertir el signo de la desigualdad al multiplicar o dividir por un número negativo."),
         t("<strong>Graph</strong> the solution on the number line (open or closed point; direction of the arrow).", "<strong>Graficar</strong> la solución en la recta numérica (punto abierto o cerrado; dirección de la flecha)."),
         t("<strong>Recognize</strong> when the point is open (<, >) and when it is closed (≤, ≥).", "<strong>Reconocer</strong> cuándo el punto es abierto (<, >) y cuándo es cerrado (≤, ≥)."),
         t("<strong>Check</strong> the solution with a test value.", "<strong>Verificar</strong> la solución con un valor de prueba.")],
        secciones,
        (t("Solve four inequalities, at least two of which require flipping the sign. Graph the solution of three inequalities on the number line, and decide for three given values whether they satisfy the inequality.",
           "Resuelva cuatro inecuaciones, al menos dos que requieran invertir el signo. Grafique en la recta numérica la solución de tres inecuaciones y decida en tres casos si un valor dado satisface la inecuación."),
         t("Look for limits in your day written as inequalities: a speed limit of 55 mph (s ≤ 55), a minimum age of 18 to vote (a ≥ 18), an elevator for fewer than 13 people (p < 13). Write three of them, graph each one, and say whether the boundary is included.",
           "Busque en su día límites que se escriben como inecuaciones: una velocidad máxima de 55 mph (v ≤ 55), una edad mínima de 18 años para votar (e ≥ 18), un ascensor para menos de 13 personas (p < 13). Escriba tres, grafique cada una y diga si el límite se incluye.")),
        quiz,
        t("Self-check checklist for linear inequalities", "Lista de autoevaluación para inecuaciones lineales"),
        t("Self-check checklist: skills for solving, graphing, and checking inequalities", "Lista de autoevaluación: destrezas para resolver, graficar y verificar inecuaciones"),
        [(t("Solving and flipping the sign", "Resolver e invertir el signo"), t("I solve like an equation and flip the sign only when I multiply or divide by a negative.", "Resuelvo como una ecuación e invierto el signo solo al multiplicar o dividir por un negativo."), t("I flip the sign inconsistently.", "Invierto el signo de forma inconsistente."), t("I never flip the sign, or I flip it for no reason.", "Nunca invierto el signo, o lo invierto sin motivo.")),
         (t("Graphing the solution", "Graficar la solución"), t("I graph with the right point and direction, and I can read a graph back as an inequality.", "Grafico con el punto correcto y la dirección adecuada, y sé leer la gráfica de vuelta como desigualdad."), t("I graph with mistakes in the point or the direction.", "Grafico con errores en el punto o la dirección."), t("I do not graph, or I mix up the kind of point.", "No grafico o confundo el tipo de punto.")),
         (t("Checking", "Verificación"), t("I check with a value inside, the boundary, and a value outside.", "Verifico con un valor dentro, el límite y uno fuera."), t("I check only one value.", "Verifico solo un valor."), t("I do not check with a test value.", "No verifico con un valor de prueba."))],
        t("<p>You learned to solve inequalities with the same steps as an equation, remembering the critical rule: flip the sign when you multiply or divide by a negative number. The solution, which is a range, is graphed on the number line with an open or closed point and an arrow, and you check it with a test value.</p>\n<p>In <strong>Lesson 5.2 · Inequalities that need simplifying, and word problems</strong> you will solve inequalities that you must simplify first (distribute, combine terms, move variables), and you will translate sentences into inequalities to solve real budget, time, and planning problems.</p>",
          "<p>En esta lección se aprendió a resolver inecuaciones con los mismos pasos que una ecuación, recordando la regla crítica de invertir el signo al multiplicar o dividir por un negativo. La solución, que es un rango, se grafica en la recta numérica con un punto abierto o cerrado y una flecha, y se verifica con un valor de prueba.</p>\n<p>En la <strong>Lección 5.2 · Inecuaciones que requieren simplificación y problemas verbales</strong> se resolverán inecuaciones que primero hay que simplificar (distribuir, combinar términos, mover variables), y se traducirán enunciados verbales a inecuaciones para resolver problemas reales de presupuesto, tiempo y planificación.</p>"),
        ("5-2", ("", t("Lesson 5.2 · Inequalities that need simplifying, and word problems", "Lección 5.2 · Inecuaciones que requieren simplificación y problemas verbales"))),
        [(t("inequality", "inecuación"), t("A statement that compares two expressions with <, >, ≤, or ≥.", "Una expresión que compara dos lados con <, >, ≤ o ≥.")),
         (t("boundary number", "número límite"), t("The number where the solution starts, like 7 in x < 7.", "El número donde empieza la solución, como el 7 en x < 7.")),
         (t("open point", "punto abierto"), t("A hollow circle on the number line: the boundary is not included (< or >).", "Un círculo vacío en la recta: el límite no se incluye (< o >).")),
         (t("closed point", "punto cerrado"), t("A filled circle on the number line: the boundary is included (≤ or ≥).", "Un círculo relleno en la recta: el límite sí se incluye (≤ o ≥)."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function ineqPositiva(){
  var tp = aleatorio(1, 3), a = aleatorio(2, 7), v = aleatorio(-5, 9), b = nz(), r = elige(RELS);
  if (tp === 1) return {izq: L(1, b), r: r, der: L(0, v + b)};
  if (tp === 2) return {izq: L(a, 0), r: r, der: L(0, a * v)};
  return {izq: L(a, b), r: r, der: L(0, a * v + b)};
}
function pasosLista(pasos, visto){ return pasos.slice(0, visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join(""); }
function botonPasos(pre, S){ var b = $(pre + "-sig"); b.disabled = S.visto >= S.pasos.length; $(pre + "-todo").disabled = b.disabled; b.textContent = S.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso")); }

/* ============ MODULE 1 · solving ============ */
var RS = {pasos: [], visto: 0, sol: null, cola: [{izq: L(1, 5), r: "<", der: L(0, 12)}, {izq: L(3, 0), r: "≤", der: L(0, 15)}, {izq: L(2, 5), r: ">", der: L(0, 13)}]};
function nuevoRS(){
  var e = RS.cola.length ? RS.cola.shift() : ineqPositiva(), R = pasosIneq(e.izq, e.r, e.der);
  var menores = !derecha(R.r);
  RS.pasos = R.pasos.concat(['<span class="veredicto">' + T("Solution: ", "Solución: ") + solHTML(R.r, R.v) + ". " +
     T("These are all the numbers " + (menores ? "less" : "greater") + " than " + fTxt(R.v) + (REL_ESTRICTO[R.r] ? ", not including it." : ", including " + fTxt(R.v) + " itself."),
       "Son todos los números " + (menores ? "menores" : "mayores") + " que " + fTxt(R.v) + (REL_ESTRICTO[R.r] ? ", sin incluirlo." : ", incluido el " + fTxt(R.v) + ".")) + "</span>"]);
  RS.sol = R; RS.visto = 0;
  $("rs-ec").innerHTML = ineqHTML(e.izq, e.r, e.der);
  pintaRS();
}
function pintaRS(){
  $("rs-pasos").innerHTML = pasosLista(RS.pasos, RS.visto);
  $("rs-recta").innerHTML = RS.visto >= RS.pasos.length ? ineqSVG(RS.sol.v, RS.sol.r) : "";
  botonPasos("rs", RS);
}
function genResolver(){
  var e = ineqPositiva(), R = pasosIneq(e.izq, e.r, e.der);
  return {enun: T("Solve ", "Resuelva ") + ineqHTML(e.izq, e.r, e.der) + ".", r: R.r, v: R.v, invierte: R.invierte,
    explica: T("You solve it like an equation; the coefficient is positive, so the sign stays the same.", "Se resuelve como una ecuación; el coeficiente es positivo, así que el signo se conserva.")};
}

/* ============ MODULE 2 · flipping the sign, checked with numbers ============ */
function pintaIV(){
  var p = leeEntero($("iv-p").value), q = leeEntero($("iv-q").value), k = leeEntero($("iv-k").value), op = $("iv-op").value, av = $("iv-aviso");
  function aviso(m){ av.className = "caja-aviso visible"; av.textContent = m; $("iv-salida").innerHTML = ""; }
  if (p === null || q === null || k === null || Math.abs(p) > 99 || Math.abs(q) > 99 || Math.abs(k) > 20) return aviso(T("Type whole numbers (from −99 to 99; the number for the operation from −20 to 20).", "Escriba números enteros (de −99 a 99; el número de la operación, de −20 a 20)."));
  if (p === q) return aviso(T("Choose two different numbers, so there is an inequality.", "Elija dos números distintos, para que haya una desigualdad."));
  if (k === 0 && (op === "*" || op === "/")) return aviso(op === "/" ? T("You cannot divide by 0.", "No se puede dividir entre 0.") : T("Multiplying by 0 leaves 0 = 0, and the information is lost. Choose another number.", "Multiplicar por 0 deja 0 = 0 y se pierde la información. Elija otro número."));
  av.className = "caja-aviso"; av.textContent = "";
  var r = p > q ? ">" : "<", P2, Q2, nombre;
  if (op === "+"){ P2 = fr(p + k); Q2 = fr(q + k); nombre = T("adding ", "sumar ") + menosV(k); }
  else if (op === "-"){ P2 = fr(p - k); Q2 = fr(q - k); nombre = T("subtracting ", "restar ") + menosV(k); }
  else if (op === "*"){ P2 = fr(p * k); Q2 = fr(q * k); nombre = T("multiplying by ", "multiplicar por ") + menosV(k); }
  else { P2 = fr(p, k); Q2 = fr(q, k); nombre = T("dividing by ", "dividir entre ") + menosV(k); }
  var conserva = cumple(P2, r, Q2), ri = REL_INV[r], V = T("true", "verdadero"), F = T("false", "falso");
  var h = '<div class="linea">' + T("Before: ", "Antes: ") + menosV(p) + " " + relVis(r) + " " + menosV(q) + ' <span class="verdad si">(' + V + ")</span>.</div>";
  h += '<div class="linea">' + T("After ", "Después de ") + nombre + T(" on both sides: ", " en ambos lados: ") + numHTML(P2) + T(" and ", " y ") + numHTML(Q2) + ".</div>";
  h += '<div class="linea">' + T("With the same sign: ", "Con el mismo signo: ") + numHTML(P2) + " " + relVis(r) + " " + numHTML(Q2) + ' <span class="verdad ' + (conserva ? "si" : "no") + '">(' + (conserva ? V : F) + ")</span>.</div>";
  if (!conserva) h += '<div class="linea">' + T("With the sign flipped: ", "Con el signo invertido: ") + numHTML(P2) + " " + relVis(ri) + " " + numHTML(Q2) + ' <span class="verdad si">(' + V + ")</span>.</div>";
  h += '<div class="linea veredicto">' + (conserva ? T("The sign stays the same. ", "El signo se conserva. ") : T("The sign flips. ", "El signo se invierte. ")) +
       ((op === "*" || op === "/") ? (k < 0 ? T("That always happens when you multiply or divide by a negative number: the order of the numbers on the line turns around.", "Así pasa siempre al multiplicar o dividir por un negativo: el orden de los números se da vuelta en la recta.") : T("Multiplying or dividing by a positive number keeps the order.", "Multiplicar o dividir por un positivo conserva el orden."))
                                   : T("Adding or subtracting, even a negative number, only shifts both numbers by the same amount.", "Sumar o restar, aunque sea un negativo, solo desplaza los dos números por igual.")) + "</div>";
  $("iv-salida").innerHTML = h;
}
function genSigno(){
  var tp = aleatorio(1, 4), r = elige(RELS), v, izq, der;
  if (tp === 1){ var a = -aleatorio(2, 6); v = aleatorio(-6, 6); izq = L(a, 0); der = L(0, a * v); }
  else if (tp === 2){ v = aleatorio(-6, 6); if (v === 0) v = 4; izq = L(-1, 0); der = L(0, -v); }
  else if (tp === 3){ var a3 = aleatorio(2, 6); v = aleatorio(-6, 6); izq = L(a3, 0); der = L(0, a3 * v); }
  else { var b = -aleatorio(2, 9); v = aleatorio(-4, 8); izq = L(1, b); der = L(0, v + b); }
  var R = pasosIneq(izq, r, der), o = [], pc = {}, usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opSol(R.r, R.v));
  mete(opSol(REL_INV[R.r], R.v), R.invierte ? T("You divided by a negative number: the sign has to flip.", "Se dividió entre un negativo: el signo tiene que invertirse.") : (tp === 4 ? T("Adding or subtracting, even a negative number, does not flip the sign.", "Sumar o restar, aunque sea un negativo, no invierte el signo.") : T("You divided by a positive number: the sign does not flip.", "Se dividió entre un positivo: el signo no se invierte.")));
  if (!fcero(R.v)){ mete(opSol(R.r, fneg(R.v)), T("Check the sign of the boundary number.", "Revise el signo del número límite.")); mete(opSol(REL_INV[R.r], fneg(R.v)), T("Check the sign of the boundary number and the inequality sign.", "Revise el signo del número límite y el de la desigualdad.")); }
  else { mete(opSol(REL_ESTRICTO[R.r] ? (R.r === "<" ? "≤" : "≥") : (R.r === "≤" ? "<" : ">"), R.v), T("Check whether the boundary is included.", "Revise si el límite se incluye.")); mete(opSol(R.r, fr(1)), T("Check the boundary number.", "Revise el número límite.")); }
  return {enun: T("Solve ", "Resuelva ") + ineqHTML(izq, r, der) + ".", opciones: o, correcta: o[0].clave, porClave: pc,
    bien: R.pasos.join(" "), mal: T("The solution is ", "La solución es ") + solHTML(R.r, R.v) + ". " + R.pasos.join(" ")};
}

/* ============ MODULE 3 · graphing ============ */
var GR = {r: "<", v: fr(0), punto: null, dir: null, resuelto: false, intentos: 0, primero: 0, pista: 0, total: 0};
function nuevoGR(){
  GR.r = elige(RELS); GR.v = fr(aleatorio(-5, 5)); GR.punto = null; GR.dir = null; GR.resuelto = false; GR.intentos = 0;
  $("gr-sol").innerHTML = solHTML(GR.r, GR.v);
  ["gr-punto", "gr-dir"].forEach(function(id){ Array.prototype.forEach.call($(id).children, function(b){ b.setAttribute("aria-pressed", "false"); b.disabled = false; }); });
  $("gr-comprobar").disabled = false; $("gr-fb").className = "fb"; $("gr-fb").innerHTML = "";
  pintaGR();
}
function relDe(punto, dir){ return dir === "der" ? (punto === "abierto" ? ">" : "≥") : (punto === "abierto" ? "<" : "≤"); }
function nombrePunto(p){ return p === "abierto" ? T("open", "abierto") : T("closed", "cerrado"); }
function pintaGR(){
  if (GR.punto && GR.dir) $("gr-recta").innerHTML = ineqSVG(GR.v, relDe(GR.punto, GR.dir), {voz: T("Your graph: " + nombrePunto(GR.punto) + " point at " + fTxt(GR.v) + " and arrow to the " + (GR.dir === "der" ? "right" : "left"), "Su gráfica: punto " + nombrePunto(GR.punto) + " en " + fTxt(GR.v) + " y flecha hacia la " + (GR.dir === "der" ? "derecha" : "izquierda"))});
  else $("gr-recta").innerHTML = ineqSVG(GR.v, null, {voz: T("Empty number line. Choose the point and the direction.", "Recta numérica vacía. Elija el punto y la dirección.")});
}
function eligeGR(grupo, b){
  if (GR.resuelto) return;
  Array.prototype.forEach.call($(grupo).children, function(x){ x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
  if (grupo === "gr-punto") GR.punto = b.getAttribute("data-v"); else GR.dir = b.getAttribute("data-v");
  pintaGR();
}
function compruebaGR(){
  if (GR.resuelto) return;
  var fb = $("gr-fb");
  if (!GR.punto || !GR.dir){ fb.className = "fb pista"; fb.innerHTML = T("Choose the kind of point and the direction of the arrow.", "Elija el tipo de punto y la dirección de la flecha."); return; }
  GR.intentos++;
  var bienP = (GR.punto === "abierto") === REL_ESTRICTO[GR.r], bienD = (GR.dir === "der") === derecha(GR.r);
  var exp = T("With " + relVis(GR.r) + " the point is " + (REL_ESTRICTO[GR.r] ? "open, because " + fTxt(GR.v) + " is not included" : "closed, because " + fTxt(GR.v) + " is included") + ", and the arrow goes to the " + (derecha(GR.r) ? "right (greater numbers)." : "left (smaller numbers)."),
              "Con " + relVis(GR.r) + " el punto es " + (REL_ESTRICTO[GR.r] ? "abierto, porque el " + fTxt(GR.v) + " no se incluye" : "cerrado, porque el " + fTxt(GR.v) + " sí se incluye") + ", y la flecha va hacia la " + (derecha(GR.r) ? "derecha (números mayores)." : "izquierda (números menores)."));
  if (bienP && bienD){
    GR.resuelto = true; GR.total++; if (GR.intentos === 1) GR.primero++; else GR.pista++;
    fb.className = "fb bien"; fb.innerHTML = TX.bien + exp;
  } else if (GR.intentos >= 2){
    GR.resuelto = true; GR.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + exp + TX.nuevo;
    $("gr-recta").innerHTML = ineqSVG(GR.v, GR.r, {voz: T("Correct graph: ", "Gráfica correcta: ") + exp});
  } else {
    fb.className = "fb pista";
    fb.innerHTML = TX.todavia + (!bienP && !bienD ? T("Neither the point nor the direction matches.", "El punto y la dirección no corresponden.") : (!bienP ? T("The direction is right, but the point is not: is the boundary included?", "La dirección está bien, pero el punto no: ¿se incluye el límite?") : T("The point is right, but the direction is not: are the solutions greater or smaller?", "El punto está bien, pero la dirección no: ¿las soluciones son mayores o menores?"))) + TX.unoMas;
  }
  if (GR.resuelto){ ["gr-punto", "gr-dir"].forEach(function(id){ Array.prototype.forEach.call($(id).children, function(b){ b.disabled = true; }); }); $("gr-comprobar").disabled = true; }
  $("gr-marcador").textContent = GR.total ? TX.resueltos(GR.primero + GR.pista, GR.primero, GR.total) : "";
}
function genLeerGrafica(){
  var r = elige(RELS), v = fr(aleatorio(-5, 5)), pc = {};
  RELS.forEach(function(x){ if (x !== r){ var bp = REL_ESTRICTO[x] === REL_ESTRICTO[r], bd = derecha(x) === derecha(r); pc[x + v.n + "/" + v.d] = bp ? T("Look at the direction of the arrow.", "Fíjese en la dirección de la flecha.") : (bd ? T("Look at the point: open or closed?", "Fíjese en el punto: ¿abierto o cerrado?") : T("Look at the point and at the arrow.", "Fíjese en el punto y en la flecha.")); } });
  return {enun: T("Which inequality does this graph show?", "¿Qué inecuación muestra esta gráfica?") + ineqSVG(v, r, {voz: T("Graph: ", "Gráfica: ") + (REL_ESTRICTO[r] ? T("open", "abierto") : T("closed", "cerrado")) + T(" point at ", ", punto en ") + fTxt(v) + T(", arrow to the ", ", flecha hacia la ") + (derecha(r) ? T("right", "derecha") : T("left", "izquierda"))}),
    opciones: RELS.map(function(x){ return opSol(x, v); }), correcta: r + v.n + "/" + v.d, porClave: pc, enOrden: true,
    bien: T((REL_ESTRICTO[r] ? "Open" : "Closed") + " point and arrow to the " + (derecha(r) ? "right" : "left") + ": ", "Punto " + (REL_ESTRICTO[r] ? "abierto" : "cerrado") + " y flecha hacia la " + (derecha(r) ? "derecha" : "izquierda") + ": ") + solHTML(r, v) + ".",
    mal: T("The " + (REL_ESTRICTO[r] ? "open point means < or >" : "closed point means ≤ or ≥") + ", and the arrow to the " + (derecha(r) ? "right means greater" : "left means smaller") + ": ", "El punto " + (REL_ESTRICTO[r] ? "abierto indica < o >" : "cerrado indica ≤ o ≥") + ", y la flecha hacia la " + (derecha(r) ? "derecha indica mayores" : "izquierda indica menores") + ": ") + solHTML(r, v) + "."};
}

/* ============ MODULE 4 · test value ============ */
function ineqGeneral(){
  if (Math.random() < 0.5) return ineqPositiva();
  var a = -aleatorio(1, 5), v = aleatorio(-5, 5), b = nz(), r = elige(RELS);
  return {izq: L(a, b), r: r, der: L(0, a * v + b)};
}
var PV = {e: null, R: null, cola: [{izq: L(-2, 0), r: "<", der: L(0, 8)}]};
function nuevoPV(){
  PV.e = PV.cola.length ? PV.cola.shift() : ineqGeneral(); PV.R = pasosIneq(PV.e.izq, PV.e.r, PV.e.der);
  var c = fval(PV.R.v);
  $("pv-x").min = Math.floor(c) - 6; $("pv-x").max = Math.floor(c) + 6; $("pv-x").value = Math.round(c) + (derecha(PV.R.r) ? 2 : -2);
  $("pv-ec").innerHTML = ineqHTML(PV.e.izq, PV.e.r, PV.e.der);
  $("pv-sol").innerHTML = solHTML(PV.R.r, PV.R.v);
  pintaPV();
}
function pintaPV(){
  var x = parseInt($("pv-x").value, 10), X = fr(x), li = evalLado(PV.e.izq, X), ld = evalLado(PV.e.der, X), verdad = cumple(li, PV.e.r, ld), enSol = cumple(X, PV.R.r, PV.R.v);
  $("pv-val").textContent = menosV(x); $("pv-x").setAttribute("aria-valuetext", menosV(x));
  $("pv-recta").innerHTML = ineqSVG(PV.R.v, PV.R.r, {marca: fval(X), voz: T("Solution x ", "Solución x ") + REL_VOZ[PV.R.r] + " " + numVoz(PV.R.v) + T("; the red mark is at ", "; la marca roja está en ") + x});
  var h = '<div class="linea">' + T("With x = " + menosV(x) + ": the left side equals ", "Con x = " + menosV(x) + ": el lado izquierdo vale ") + numHTML(li) + T(" and the right side ", " y el derecho ") + numHTML(ld) + ".</div>";
  h += '<div class="linea">' + numHTML(li) + " " + relVis(PV.e.r) + " " + numHTML(ld) + T(" is ", " es ") + '<span class="verdad ' + (verdad ? "si" : "no") + '">' + (verdad ? T("true", "verdadero") : T("false", "falso")) + "</span>.</div>";
  h += '<div class="linea veredicto">' + (figual(X, PV.R.v) ? T("It is the boundary number: ", "Es el número límite: ") + (REL_ESTRICTO[PV.R.r] ? T("it is not included (open point).", "no se incluye (punto abierto).") : T("it is included (closed point).", "sí se incluye (punto cerrado).")) :
       (enSol ? T("It is inside the range of the solution", "Está dentro del rango de la solución") : T("It is outside the range of the solution", "Está fuera del rango de la solución"))) + (verdad === enSol && !figual(X, PV.R.v) ? T(", and the original inequality confirms it.", " y la inecuación original lo confirma.") : (figual(X, PV.R.v) ? "" : ".")) + "</div>";
  $("pv-salida").innerHTML = h;
}
function genValor(){
  var e = ineqGeneral(), R = pasosIneq(e.izq, e.r, e.der), c = fval(R.v), cands = [], i;
  for (i = Math.floor(c) - 4; i <= Math.floor(c) + 4; i++) cands.push(i);
  var dentro = cands.filter(function(z){ return cumple(fr(z), R.r, R.v); }), fuera = cands.filter(function(z){ return !cumple(fr(z), R.r, R.v); });
  var ok = elige(dentro), malos = baraja(fuera).slice(0, 3), pc = {};
  var o = [{html: "x = " + menosV(ok), clave: "v" + ok}].concat(malos.map(function(z){ pc["v" + z] = (REL_ESTRICTO[R.r] && z === c) ? T("It is the boundary number and the sign is strict (" + relVis(R.r) + "): it is not included.", "Es el número límite y el signo es estricto (" + relVis(R.r) + "): no se incluye.") : T("Substitute it into the original inequality: it gives a false statement.", "Sustitúyalo en la inecuación original: da una afirmación falsa."); return {html: "x = " + menosV(z), clave: "v" + z}; }));
  return {enun: T("Which of these values is a solution of ", "¿Cuál de estos valores es solución de ") + ineqHTML(e.izq, e.r, e.der) + "?", opciones: o, correcta: "v" + ok, porClave: pc,
    bien: T("The solution is ", "La solución es ") + solHTML(R.r, R.v) + T(", and " + menosV(ok) + " meets that condition.", ", y " + menosV(ok) + " cumple esa condición."), mal: T("The solution is ", "La solución es ") + solHTML(R.r, R.v) + T(": only " + menosV(ok) + " meets it.", ": solo " + menosV(ok) + " la cumple.")};
}

/* ============ Start ============ */
$("rs-sig").addEventListener("click", function(){ if (RS.visto < RS.pasos.length){ RS.visto++; pintaRS(); } });
$("rs-todo").addEventListener("click", function(){ RS.visto = RS.pasos.length; pintaRS(); });
$("rs-nuevo").addEventListener("click", nuevoRS);
nuevoRS();
creaPracticaDesig("p1", genResolver);
["iv-p", "iv-q", "iv-k"].forEach(function(id){ $(id).addEventListener("input", pintaIV); });
$("iv-op").addEventListener("change", pintaIV);
pintaIV();
OMR("p2", genSigno);
Array.prototype.forEach.call($("gr-punto").children, function(b){ b.addEventListener("click", function(){ eligeGR("gr-punto", b); }); });
Array.prototype.forEach.call($("gr-dir").children, function(b){ b.addEventListener("click", function(){ eligeGR("gr-dir", b); }); });
$("gr-comprobar").addEventListener("click", compruebaGR);
$("gr-nuevo").addEventListener("click", nuevoGR);
nuevoGR();
OMR("p3", genLeerGrafica);
$("pv-x").addEventListener("input", pintaPV);
$("pv-nuevo").addEventListener("click", nuevoPV);
nuevoPV();
OMR("p4", genValor);
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}\n  input[type=range]{width:100%;accent-color:var(--tema);}"

def campo(i, etiqueta, valor):
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="text" class="corto" id="{i}" value="{valor}"></div>'

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("solve", "resolver"), t("Solving like an equation", "Resolver como una ecuación"),
      f'''      <p>{t("An inequality compares two expressions with one of these signs:", "Una inecuación compara dos expresiones con uno de estos signos:")}</p>
      <table class="reglas">
        <caption>{t("Meaning of the inequality signs", "Significado de los signos de desigualdad")}</caption>
        <thead><tr><th scope="col">{t("Sign", "Signo")}</th><th scope="col">{t("Meaning", "Significado")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead>
        <tbody>
          <tr><td>&lt;</td><td>{t("less than", "menor que")}</td><td>x &lt; 5</td></tr>
          <tr><td>&gt;</td><td>{t("greater than", "mayor que")}</td><td>x &gt; 5</td></tr>
          <tr><td>≤</td><td>{t("less than or equal to", "menor o igual que")}</td><td>x ≤ 5</td></tr>
          <tr><td>≥</td><td>{t("greater than or equal to", "mayor o igual que")}</td><td>x ≥ 5</td></tr>
        </tbody>
      </table>
      <p>{t("As long as you do not multiply or divide by a negative number, you solve an inequality <strong>exactly like</strong> an equation. The difference is in the answer: it is not one number, but a <strong>range</strong> of numbers.", "Mientras no se multiplique ni se divida por un número negativo, una inecuación se resuelve <strong>exactamente igual</strong> que una ecuación. La diferencia está en la respuesta: no es un número, sino un <strong>rango</strong> de números.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <div class="estado"><span class="grande" id="rs-ec"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="rs-sig"></button><button type="button" class="btn-sec" id="rs-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="rs-nuevo">{t("Another inequality", "Otra inecuación")}</button></div>
      </div>
      <div class="pasos" id="rs-pasos" aria-live="polite"></div>
      <div id="rs-recta"></div>
{P.desig("p1", t("Practice: solve the inequality", "Practique: resuelva la inecuación"))}'''),
     (t("flip", "invertir"), t("The critical rule: flipping the sign", "La regla crítica: invertir el signo"),
      f'''      <p>{t("When you <strong>multiply or divide</strong> both sides by a <strong>negative</strong> number, the inequality sign flips. It is the only real difference from equations.", "Al <strong>multiplicar o dividir</strong> ambos lados por un número <strong>negativo</strong>, el signo de la desigualdad se invierte. Es la única diferencia real con las ecuaciones.")}</p>
      <h3>{t("Check it with numbers", "Compruébelo con números")}</h3>
      <p>{t("Start with a true inequality between two numbers and do the same operation to both sides. See whether the inequality is still true.", "Empiece con una desigualdad verdadera entre dos números y aplique la misma operación a los dos lados. Mire si la desigualdad sigue siendo verdadera.")}</p>
      <div class="panel"><div class="campos">
        {campo("iv-p", t("Left number", "Número de la izquierda"), 6)}
        {campo("iv-q", t("Right number", "Número de la derecha"), 4)}
        <div class="campo"><label for="iv-op">{t("Operation on both sides", "Operación en ambos lados")}</label><select id="iv-op"><option value="+">{t("Add", "Sumar")}</option><option value="-">{t("Subtract", "Restar")}</option><option value="*" selected>{t("Multiply by", "Multiplicar por")}</option><option value="/">{t("Divide by", "Dividir entre")}</option></select></div>
        {campo("iv-k", t("Number", "Número"), -1)}
      </div></div>
{P.aviso("iv-aviso")}
{P.salida("iv-salida")}
{P.atencion(t("Only with negatives, and only when you multiply or divide:", "Solo con negativos, y solo al multiplicar o dividir:"), t("adding or subtracting a negative number does not flip the sign. The most common mistake is to flip it when you should not.", "sumar o restar un negativo no invierte el signo. El error más común es invertirlo sin que corresponda."))}
{B.om("p2", t("Practice: what happens to the sign?", "Practique: ¿qué pasa con el signo?"))}'''),
     (t("graph", "graficar"), t("Graphing on the number line", "Graficar en la recta numérica"),
      f'''      <p>{t("Graphing the solution takes two decisions: the kind of point at the boundary number and the direction of the arrow.", "Graficar la solución requiere dos decisiones: el tipo de punto en el número límite y la dirección de la flecha.")}</p>
      <table class="reglas">
        <caption>{t("Point and direction for each sign", "Punto y dirección según el signo")}</caption>
        <thead><tr><th scope="col">{t("Sign", "Signo")}</th><th scope="col">{t("Point at the boundary", "Punto en el límite")}</th><th scope="col">{t("Arrow", "Flecha")}</th></tr></thead>
        <tbody>
          <tr><td>x &lt; a</td><td>{t("open ○ (not included)", "abierto ○ (no se incluye)")}</td><td>{t("to the left", "hacia la izquierda")}</td></tr>
          <tr><td>x ≤ a</td><td>{t("closed ● (included)", "cerrado ● (sí se incluye)")}</td><td>{t("to the left", "hacia la izquierda")}</td></tr>
          <tr><td>x &gt; a</td><td>{t("open ○", "abierto ○")}</td><td>{t("to the right", "hacia la derecha")}</td></tr>
          <tr><td>x ≥ a</td><td>{t("closed ●", "cerrado ●")}</td><td>{t("to the right", "hacia la derecha")}</td></tr>
        </tbody>
      </table>
      <h3>{t("Build the graph", "Arme la gráfica")}</h3>
      <div class="panel">
        <div class="estado">{t("Graph", "Grafique")} <span class="grande" id="gr-sol"></span></div>
        <p><strong>{t("The point at the boundary is…", "El punto en el límite es…")}</strong></p>
        <div class="elecciones" id="gr-punto"><button type="button" class="eleccion" data-v="abierto" aria-pressed="false">{t("Open ○", "Abierto ○")}</button><button type="button" class="eleccion" data-v="cerrado" aria-pressed="false">{t("Closed ●", "Cerrado ●")}</button></div>
        <p><strong>{t("The arrow goes…", "La flecha va hacia…")}</strong></p>
        <div class="elecciones" id="gr-dir"><button type="button" class="eleccion" data-v="izq" aria-pressed="false">{t("← to the left", "← la izquierda")}</button><button type="button" class="eleccion" data-v="der" aria-pressed="false">{t("to the right →", "la derecha →")}</button></div>
        <div id="gr-recta"></div>
        <div class="fila-btn"><button type="button" class="btn" id="gr-comprobar">Check</button><button type="button" class="btn-sec" id="gr-nuevo">{t("Another solution", "Otra solución")}</button></div>
        <div class="fb" id="gr-fb" role="status"></div>
        <p class="marcador" id="gr-marcador"></p>
      </div>
{B.om("p3", t("Practice: which inequality does the graph show?", "Practique: ¿qué inecuación muestra la gráfica?"))}'''),
     (t("test-value", "prueba"), t("Checking with a test value", "Verificar con un valor de prueba"),
      f'''      <p>{t("To check a solution, choose three values: one clearly inside the range, the boundary number, and one outside. Substitute them into the <strong>original inequality</strong>: only the values in the range should make it true.", "Para comprobar una solución se eligen tres valores: uno claramente dentro del rango, el número límite y uno fuera. Se sustituyen en la <strong>inecuación original</strong>: solo los del rango deben hacerla verdadera.")}</p>
      <h3>{t("Value tester", "Probador de valores")}</h3>
      <div class="panel">
        <div class="estado">{t("Inequality:", "Inecuación:")} <span class="grande" id="pv-ec"></span></div>
        <p class="centro">{t("Proposed solution:", "Solución propuesta:")} <strong id="pv-sol"></strong></p>
        <div class="campo"><label for="pv-x">{t("Test value:", "Valor de prueba:")} <span id="pv-val"></span></label><input type="range" id="pv-x" min="-10" max="10" step="1" value="0"></div>
        <div id="pv-recta"></div>
{P.salida("pv-salida")}
        <div class="fila-btn"><button type="button" class="btn-sec" id="pv-nuevo">{t("Another inequality", "Otra inecuación")}</button></div>
      </div>
{B.om("p4", t("Practice: which value is a solution?", "Practique: ¿qué valor es solución?"))}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver inecuaciones lineales y graficar en la recta numérica")
