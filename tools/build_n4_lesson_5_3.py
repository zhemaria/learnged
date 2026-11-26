"""Level 4 · Lesson 5.3 · Solving rational equations — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_5-3.html and algebra/n4-l5-3.html (clear the denominators with the LCD, the checker of
extraneous solutions, work together, and distance, speed, and time). They are rebuilt here, inside LearnGED, with typed solutions
read by math/poly4.js. US units (miles, miles per hour). Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "5-3"
TEMA = ("Rational expressions", "Expresiones racionales")
TIT = ("Solving rational equations", "Resolver ecuaciones racionales")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)
ESTILO = n4.ESTILO + """
  .enun .fracc,.paso4 .fracc,.salida .fracc{margin:4px 3px;}
  .barra-trabajo{display:flex;height:34px;border:2px solid #37474f;border-radius:6px;overflow:hidden;max-width:520px;margin:10px auto;}
  .barra-trabajo span{display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:14px;white-space:nowrap;overflow:hidden;}
"""

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 5.2.</strong> In Lesson 5.2 you added, subtracted, multiplied, and divided algebraic fractions. Now they appear inside equations. The strategy is direct: multiply by the LCD of all the denominators to clear them, and the rational equation becomes an equation you already know how to solve.", "<strong>Conexión con la lección anterior.</strong> En la Lección 5.2 se sumaron, restaron, multiplicaron y dividieron fracciones algebraicas. Ahora aparecen dentro de ecuaciones. La estrategia es directa: multiplicar por el MCM de todos los denominadores para «limpiarlos» y transformar la ecuación racional en una ecuación que ya se sabe resolver.")}</p>
<p>{t("Four moves: write down the excluded values, multiply both sides by the LCD of all the denominators, solve the equation that is left (with no fractions), and check the solution against the excluded values.", "Cuatro movimientos: anotar los valores excluidos, multiplicar ambos lados por el MCM de todos los denominadores, resolver la ecuación que queda (ya sin fracciones) y verificar la solución contra los valores excluidos.")}</p>
{ejemplo(t("Example 1: solve 6/x + 1 = 4.", "Ejemplo 1 · Resolver 6/x + 1 = 4."),
  [("1", t("LCD of the denominators:", "MCM de los denominadores:"), t("x. Excluded value: x = 0.", "x. Valor excluido: x = 0.")), ("2", t("Multiply everything by x:", "Se multiplica todo por x:"), "6 + x = 4x."), ("3", t("Solve:", "Se resuelve:"), t("6 = 3x, so x = 2.", "6 = 3x, así que x = 2.")), ("4", t("x = 2 does not make the denominator zero. It is valid.", "x = 2 no anula el denominador. Es válida."), ""),
   ("✓", t("Solution.", "Solución."), "<strong>x = 2</strong>.")])}
{ejemplo(t("Example 2: solve 1/(x − 2) = 3/x.", "Ejemplo 2 · Resolver 1/(x − 2) = 3/x."),
  [("1", t("LCD:", "MCM:"), "x(x − 2). " + t("Multiplying:", "Al multiplicar:") + " x = 3(x − 2)."), ("2", t("Solve:", "Se resuelve:"), t("x = 3x − 6, then −2x = −6, x = 3.", "x = 3x − 6, entonces −2x = −6, x = 3.")), ("3", t("x = 3 does not make any denominator zero. It is valid.", "x = 3 no anula ningún denominador. Es válida."), ""),
   ("✓", t("Solution.", "Solución."), "<strong>x = 3</strong>.")])}
{caja("tip", t("An equation is not a sum", "Una ecuación no es una suma"), t("<p>Multiplying by the LCD is not the same as adding fractions: here there is an equals sign, so you can multiply everything by the LCD and make the denominators disappear. In a sum with no equals sign, like the ones in Lesson 5.2, the denominators stay.</p>", "<p>Multiplicar por el MCM no es lo mismo que sumar fracciones: aquí hay un signo de igual, así que se puede multiplicar todo por el MCM y hacer desaparecer los denominadores. En una suma sin igual, como las de la lección anterior, los denominadores se conservan.</p>"))}
{practica("p1", t("Practice 1 — 3/x = 6", "Práctica 1 — 3/x = 6"), t("Choose the solution.", "Seleccione la solución."), [("a", "x = 2"), ("b", "x = 1/2"), ("c", "x = 3")])}
{practica("p2", t("Practice 2 — 4/x + 2 = 6", "Práctica 2 — 4/x + 2 = 6"), t("Choose the solution.", "Seleccione la solución."), [("a", "x = 1"), ("b", "x = 2"), ("c", "x = 4")])}
{practica("p3", t("Practice 3 — 1/(x − 2) = 3/x", "Práctica 3 — 1/(x − 2) = 3/x"), t("Choose the solution.", "Seleccione la solución."), [("a", "x = 2"), ("b", "x = −3"), ("c", "x = 3")])}
{enlace(n, t("lcd", "mcm"), t("solving with the LCD", "la resolución con el MCM"), t("Equations solved step by step, from writing down the excluded values to the final check, and equations to solve on your own.", "Ecuaciones resueltas paso a paso, desde anotar los valores excluidos hasta la verificación final, y ecuaciones para resolver por su cuenta."))}'''

    s2 = f'''<p>{t("When you multiply by the LCD, a “solution” may appear that actually makes a denominator of the original equation zero. That solution is <strong>extraneous</strong> and must be thrown out. That is why you must check every solution against the excluded values.", "Al multiplicar por el MCM puede aparecer una «solución» que en realidad anula un denominador de la ecuación original. Esa solución es <strong>extraña</strong> y debe descartarse. Por eso es obligatorio verificar cada solución contra los valores excluidos.")}</p>
{ejemplo(t("Example 3: solve x/(x − 3) = 3/(x − 3) + 2.", "Ejemplo 3 · Resolver x/(x − 3) = 3/(x − 3) + 2."),
  [("1", t("LCD:", "MCM:"), "(x − 3). " + t("Multiplying:", "Al multiplicar:") + " x = 3 + 2(x − 3)."), ("2", t("Solve:", "Se resuelve:"), t("x = 3 + 2x − 6, then x = 2x − 3, x = 3.", "x = 3 + 2x − 6, entonces x = 2x − 3, x = 3.")), ("3", t("But x = 3 makes the denominator (x − 3) zero. It is an extraneous solution.", "Pero x = 3 anula el denominador (x − 3). Es una solución extraña."), ""),
   ("✓", t("Result.", "Resultado."), t("<strong>The equation has no solution.</strong>", "<strong>La ecuación no tiene solución.</strong>"))])}
{caja("ojo", t("Always check", "Verifique siempre"), t("<p>A solution found with algebra that equals an excluded value is not valid. An extraneous solution is not an arithmetic mistake: multiplying by the LCD multiplied by something that is zero for that value of x. If every solution is extraneous, the equation has no solution.</p>", "<p>Una solución obtenida algebraicamente que coincide con un valor excluido no es válida. Una solución extraña no es un error de cuentas: al multiplicar por el MCM se multiplicó por algo que vale cero para ese valor de x. Si todas las soluciones resultan extrañas, la ecuación no tiene solución.</p>"))}
{enlace(n, t("extraneous", "extranas"), t("the checker of extraneous solutions", "el verificador de soluciones extrañas"), t("Type a value and see it substituted in each denominator of the original equation: which one becomes zero and why that solution is thrown out.", "Escriba un valor y vea cómo se sustituye en cada denominador de la ecuación original: cuál se anula y por qué esa solución se descarta."))}'''

    s3 = f'''<p>{t("If one person takes a hours to do a job and another takes b hours, working together they take t hours, where:", "Si una persona tarda a horas en hacer un trabajo y otra tarda b horas, trabajando juntas tardan t horas, donde:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">1/a + 1/b = 1/t</p>
<p>{t("Each fraction is the part of the job each one does in one hour.", "Cada fracción representa la parte del trabajo que cada quien hace en una hora.")}</p>
{ejemplo(t("Example 4: Ana paints a room in 3 hours; Luis, in 6 hours. How long do they take together?", "Ejemplo 4 · Ana pinta una sala en 3 horas; Luis, en 6 horas. ¿Cuánto tardan juntos?"),
  [("1", t("Set it up:", "Se plantea:"), "1/3 + 1/6 = 1/t."), ("2", t("Add:", "Se suma:"), "2/6 + 1/6 = 3/6 = 1/2."), ("3", t("So 1/2 = 1/t, and t = 2.", "Entonces 1/2 = 1/t, así que t = 2."), ""),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Together they take 2 hours.</strong>", "<strong>Juntos tardan 2 horas.</strong>"))])}
{caja("tip", t("A common-sense check", "Control de sentido común"), t("<p>Together they always take less time than the faster one alone. If your answer is greater than the shorter time, the setup is wrong: probably the times were added instead of the rates.</p>", "<p>Juntos siempre tardan menos que el más rápido de los dos por separado. Si su respuesta es mayor que el tiempo individual más corto, hay un error en el planteamiento: seguramente se sumaron los tiempos en vez de los ritmos.</p>"))}
{practica("p4", t("Practice 4 — 2 h and 2 h", "Práctica 4 — 2 h y 2 h"), t("A takes 2 hours and B takes 2 hours. How long do they take together?", "A tarda 2 h y B tarda 2 h. ¿Cuánto tardan juntos?"), [("a", "2 h"), ("b", "1 h"), ("c", "4 h")])}
{practica("p5", t("Practice 5 — 6 h and 3 h", "Práctica 5 — 6 h y 3 h"), t("A takes 6 hours and B takes 3 hours. How long do they take together?", "A tarda 6 h y B tarda 3 h. ¿Cuánto tardan juntos?"), [("a", "2 h"), ("b", "3 h"), ("c", "9 h")])}
{practica("p6", t("Practice 6 — The model", "Práctica 6 — El modelo"), t("Which formula models working together?", "¿Qué fórmula modela el trabajo conjunto?"), [("a", "a + b = t"), ("b", "a · b = t"), ("c", "1/a + 1/b = 1/t")])}
{enlace(n, t("work", "trabajo"), t("working together", "el trabajo conjunto"), t("Change each person's time and watch, on a bar, the part of the job each one does in one hour.", "Cambie los tiempos de cada persona y observe en una barra qué parte del trabajo hace cada quien en una hora."))}'''

    s4 = f'''<p>{t("Many GED problems use the relation time = distance / speed, which produces rational equations. A typical case is a boat or a plane helped or slowed by a current or the wind:", "Muchos problemas del GED usan la relación tiempo = distancia / velocidad, que produce ecuaciones racionales. Un caso típico es el de un bote o un avión afectado por una corriente o el viento:")}</p>
{tabla(t("The speed of a boat on a river", "La velocidad de un bote en un río"), t("The real speed of a boat depending on its direction compared with the current", "Velocidad efectiva de un bote según la dirección respecto a la corriente"), [t("Situation", "Situación"), t("Real speed", "Velocidad efectiva")],
  [[t("With the current (downstream)", "A favor de la corriente"), t("v + c (the current helps)", "v + c (la corriente ayuda)")], [t("Against the current (upstream)", "En contra de la corriente"), t("v − c (the current slows it)", "v − c (la corriente frena)")]])}
<p>{t("Here v is the speed in still water and c is the speed of the current. Writing each time as distance/speed gives a rational equation, which you solve with the LCD method.", "Donde v es la velocidad en agua quieta y c, la velocidad de la corriente. Al expresar los tiempos como distancia/velocidad, se obtiene una ecuación racional que se resuelve con el método del MCM.")}</p>
{ejemplo(t("Example 5: a boat goes 15 mph in still water. It takes the same time to go 20 miles downstream as 10 miles upstream. How fast is the current?", "Ejemplo 5 · Un bote avanza a 15 mph en agua quieta. Tarda lo mismo en recorrer 20 millas a favor de la corriente que 10 millas en contra. ¿Cuál es la velocidad de la corriente?"),
  [("1", t("Same time:", "Mismo tiempo:"), "20/(15 + c) = 10/(15 − c)."), ("2", t("Multiply by the LCD (15 + c)(15 − c):", "Se multiplica por el MCM (15 + c)(15 − c):"), "20(15 − c) = 10(15 + c)."), ("3", t("Solve:", "Se resuelve:"), t("300 − 20c = 150 + 10c, so 150 = 30c, c = 5.", "300 − 20c = 150 + 10c, así que 150 = 30c, c = 5.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>The current goes 5 mph.</strong> Check: 20/20 = 1 hour and 10/10 = 1 hour.", "<strong>La corriente va a 5 mph.</strong> Comprobación: 20/20 = 1 hora y 10/10 = 1 hora."))])}
{enlace(n, t("distance", "dvt"), t("distance, speed, and time", "distancia, velocidad y tiempo"), t("A boat-on-the-river simulator: change the speed, the current, and the distance, and see what happens when the current equals the speed of the boat.", "Simulador del bote en el río: cambie la velocidad, la corriente y la distancia, y mire qué ocurre cuando la corriente iguala a la velocidad del bote."))}'''

    secciones = [("s-" + t("lcd", "mcm"), t("Clearing the denominators with the LCD", "Limpiar los denominadores con el MCM"), s1),
                 ("s-" + t("extraneous", "extranas"), t("Extraneous solutions", "Soluciones extrañas"), s2),
                 ("s-" + t("work", "trabajo"), t("Application: working together", "Aplicación: problemas de trabajo conjunto"), s3),
                 ("s-" + t("distance", "dvt"), t("More applications: distance, speed, and time", "Otras aplicaciones: distancia, velocidad y tiempo"), s4)]

    lesson = {"next": t("Lesson 6.1", "Lección 6.1"), "review": t("sections 1 and 2", "las secciones 1 y 2"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Multiply by x: 3 = 6x, so x = 3/6.", "Multiplique por x: 3 = 6x, así que x = 3/6."), "c": t("Substitute: 3/3 = 1, not 6.", "Sustituya: 3/3 = 1, no 6.")}, "right": t("3 = 6x, x = 1/2.", "3 = 6x, x = 1/2."), "solution": "x = 1/2."},
      "p2": {"ok": "a", "hints": {"b": t("Substitute: 4/2 + 2 = 4, not 6.", "Sustituya: 4/2 + 2 = 4, no 6."), "c": t("Substitute: 4/4 + 2 = 3, not 6.", "Sustituya: 4/4 + 2 = 3, no 6.")}, "right": t("4 + 2x = 6x, 4 = 4x, x = 1.", "4 + 2x = 6x, 4 = 4x, x = 1."), "solution": "x = 1."},
      "p3": {"ok": "c", "hints": {"a": t("x = 2 makes x − 2 zero: it is excluded.", "x = 2 anula x − 2: está excluido."), "b": t("x = 3(x − 2) gives x = 3x − 6.", "x = 3(x − 2) da x = 3x − 6.")}, "right": t("x = 3x − 6, −2x = −6, x = 3.", "x = 3x − 6, −2x = −6, x = 3."), "solution": "x = 3."},
      "p4": {"ok": "b", "hints": {"a": t("Together they take less time than each one alone.", "Juntos tardan menos que cada uno por separado."), "c": t("Do not add the times: add the rates 1/2 + 1/2.", "No sume los tiempos: sume los ritmos 1/2 + 1/2.")}, "right": t("1/2 + 1/2 = 1 = 1/t, t = 1.", "1/2 + 1/2 = 1 = 1/t, t = 1."), "solution": "1 h."},
      "p5": {"ok": "a", "hints": {"b": t("Together they take less than the faster one (3 h).", "Juntos tardan menos que el más rápido (3 h)."), "c": t("Do not add the times: add 1/6 + 1/3.", "No sume los tiempos: sume 1/6 + 1/3.")}, "right": t("1/6 + 2/6 = 3/6 = 1/2, t = 2.", "1/6 + 2/6 = 3/6 = 1/2, t = 2."), "solution": "2 h."},
      "p6": {"ok": "c", "hints": {"a": t("Adding the times gives more time, not less.", "Sumar los tiempos da más tiempo, no menos."), "b": t("Multiplying the times does not make sense here.", "Multiplicar los tiempos no tiene sentido aquí.")}, "right": t("Each one does 1/a and 1/b of the job per hour.", "Cada uno hace 1/a y 1/b del trabajo por hora."), "solution": "1/a + 1/b = 1/t."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Multiply by x: 5 = 10x.", "Multiplique por x: 5 = 10x."), "c": t("Substitute: 5/5 = 1, not 10.", "Sustituya: 5/5 = 1, no 10."), "d": t("5 = 10x, so x = 5/10.", "5 = 10x, así que x = 5/10.")}, "solution": "x = 1/2."},
      "B": {"ok": "c", "hints": {"a": t("Substitute: 6/3 + 1 = 3, not 4.", "Sustituya: 6/3 + 1 = 3, no 4."), "b": t("Substitute: 6/6 + 1 = 2, not 4.", "Sustituya: 6/6 + 1 = 2, no 4."), "d": t("Substitute: 12 + 1 = 13, not 4.", "Sustituya: 12 + 1 = 13, no 4.")}, "solution": "x = 2."},
      "C": {"ok": "a", "hints": {"b": t("2(x + 3) = 8x gives 6 = 6x.", "2(x + 3) = 8x da 6 = 6x."), "c": t("x = −3 makes x + 3 zero: it is excluded.", "x = −3 anula x + 3: está excluido."), "d": t("Substitute: 2/2 = 1, but 8/5 is not 1.", "Sustituya: 2/2 = 1, pero 8/5 no es 1.")}, "solution": "x = 1."},
      "D": {"ok": "d", "hints": {"a": t("Multiply by 6: 3(x + 1) = 2x.", "Multiplique por 6: 3(x + 1) = 2x."), "b": t("3x + 3 = 2x gives x = −3.", "3x + 3 = 2x da x = −3."), "c": t("3x + 3 = 2x gives x = −3.", "3x + 3 = 2x da x = −3.")}, "solution": "x = −3."},
      "E": {"ok": "b", "hints": {"a": t("x = 4 makes x − 4 zero.", "x = 4 anula x − 4."), "c": t("A value that makes a denominator zero is never valid.", "Un valor que anula un denominador nunca es válido."), "d": t("Nothing gives x = 0 here.", "Nada da x = 0 aquí.")}, "solution": t("No, x = 4 is an excluded value.", "No, x = 4 es un valor excluido.")},
      "F": {"ok": "c", "hints": {"a": t("It is not a habit: there is a mathematical reason.", "No es costumbre: hay una razón matemática."), "b": t("It is necessary: some solutions are extraneous.", "Sí es necesario: algunas soluciones son extrañas."), "d": t("Checking is about the excluded values.", "Verificar tiene que ver con los valores excluidos.")}, "solution": t("To throw out excluded values (extraneous solutions).", "Para descartar valores excluidos (soluciones extrañas).")},
      "G": {"ok": "a", "hints": {"b": t("Together they take less than the faster one (3 h).", "Juntos tardan menos que el más rápido (3 h)."), "c": t("Do not add the times.", "No sume los tiempos."), "d": t("3 h is Ana alone; together it is less.", "3 h es Ana sola; juntos es menos.")}, "solution": "2 h."},
      "H": {"ok": "d", "hints": {"a": t("The current helps downstream: add it.", "A favor, la corriente ayuda: se suma."), "b": t("Speeds are added, not multiplied.", "Las velocidades se suman, no se multiplican."), "c": t("Speeds are added, not divided.", "Las velocidades se suman, no se dividen.")}, "solution": "v + c."},
     }}

    quiz = [
     ("A", t("Solve 5/x = 10.", "Resuelva 5/x = 10."), [("a", "x = 2"), ("b", "x = 1/2"), ("c", "x = 5"), ("d", "x = 50")]),
     ("B", t("Solve 6/x + 1 = 4.", "Resuelva 6/x + 1 = 4."), [("a", "x = 3"), ("b", "x = 6"), ("c", "x = 2"), ("d", "x = 1/2")]),
     ("C", t("Solve 2/x = 8/(x + 3).", "Resuelva 2/x = 8/(x + 3)."), [("a", "x = 1"), ("b", "x = 3"), ("c", "x = −3"), ("d", "x = 2")]),
     ("D", t("Solve (x + 1)/2 = x/3.", "Resuelva (x + 1)/2 = x/3."), [("a", "x = 3"), ("b", "x = 1"), ("c", "x = −1"), ("d", "x = −3")]),
     ("E", t("Solving x/(x − 4) = 4/(x − 4) gives x = 4. Is it valid?", "Al resolver x/(x − 4) = 4/(x − 4) se obtiene x = 4. ¿Es válida?"), [("a", t("Yes, x = 4", "Sí, x = 4")), ("b", t("No, x = 4 is an excluded value", "No, x = 4 es un valor excluido")), ("c", t("Yes, always", "Sí, siempre")), ("d", t("No, it must be x = 0", "No, debe ser x = 0"))]),
     ("F", t("Why do you check the solutions of rational equations?", "¿Por qué se verifican las soluciones en ecuaciones racionales?"), [("a", t("Out of habit", "Por costumbre")), ("b", t("It is not necessary", "No es necesario")), ("c", t("To throw out excluded values (extraneous solutions)", "Para descartar valores excluidos (soluciones extrañas)")), ("d", t("To add fractions", "Para sumar fracciones"))]),
     ("G", t("Ana paints a room in 3 h and Luis in 6 h. How long do they take together?", "Ana pinta una sala en 3 h y Luis en 6 h. ¿Cuánto tardan juntos?"), [("a", "2 h"), ("b", "4.5 h"), ("c", "9 h"), ("d", "3 h")]),
     ("H", t("A boat goes v in still water. With a current c helping it, its real speed is:", "Un bote tiene velocidad v en agua quieta. Con la corriente c a favor, su velocidad efectiva es:"), [("a", "v − c"), ("b", "v · c"), ("c", "v / c"), ("d", "v + c")])]

    tarea = (t("For your own work, with your notebook and the calculator: (1) Do we work together? Solve with 1/a + 1/b = 1/t and check that the time together is less than each time alone: Ana paints a room in 6 h and Luis in 3 h; one faucet fills a tank in 4 h and another in 12 h; one machine finishes an order in 5 h and another in 20 h. (2) With and against: a boat goes 15 mph in still water and takes the same time to go 20 miles downstream as 10 miles upstream; how fast is the current? A plane flies 500 mph with no wind and covers 1,200 miles with the wind in the same time as 800 miles against it; how fast is the wind? (3) Hunting extraneous solutions: solve, compare with the excluded values, and throw out the solution that makes a denominator zero: x/(x − 3) = 3/(x − 3) + 2; x²/(x − 1) = 1/(x − 1); 3/x + 1 = 4/x. Explain which one has no extraneous solution. Then do several exercises of each activity on the practice page. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno y la calculadora: (1) ¿Trabajamos juntos? Resuelva con 1/a + 1/b = 1/t y compruebe que el tiempo conjunto es menor que el de cada uno por separado: Ana pinta un cuarto en 6 h y Luis en 3 h; una llave llena un tanque en 4 h y otra en 12 h; una máquina termina un pedido en 5 h y otra en 20 h. (2) A favor y en contra: un bote avanza a 15 mph en agua tranquila y tarda lo mismo en recorrer 20 millas a favor de la corriente que 10 millas en contra; ¿cuál es la velocidad de la corriente? Un avión vuela a 500 mph sin viento y recorre 1,200 millas con viento a favor en el mismo tiempo que 800 millas en contra; ¿cuál es la velocidad del viento? (3) Caza de soluciones extrañas: resuelva, compare con los valores excluidos y descarte la solución que anule un denominador: x/(x − 3) = 3/(x − 3) + 2; x²/(x − 1) = 1/(x − 1); 3/x + 1 = 4/x. Explique en cuál no hay solución extraña. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Think of a chore you share at home, such as washing the dishes. Time how long each person takes alone, use 1/a + 1/b = 1/t to predict how long you take together, and then try it.",
               "Piense en una tarea que comparten en casa, como lavar los platos. Mida cuánto tarda cada persona sola, use 1/a + 1/b = 1/t para predecir cuánto tardan juntos y después compruébelo."))

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Solve a rational equation by multiplying by the LCD, check for extraneous solutions, and model work-together and distance problems.", "Resuelva una ecuación racional multiplicando por el MCM, descarte las soluciones extrañas y modele problemas de trabajo conjunto y de distancia."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Solve</strong> rational equations by multiplying by the LCD of all the denominators.", "<strong>Resolver</strong> ecuaciones racionales multiplicando por el MCM de todos los denominadores."),
         t("<strong>Check</strong> every solution and throw out the extraneous ones.", "<strong>Verificar</strong> cada solución y descartar las soluciones extrañas."),
         t("<strong>Model</strong> work-together problems with 1/a + 1/b = 1/t.", "<strong>Modelar</strong> problemas de trabajo conjunto con 1/a + 1/b = 1/t."),
         t("<strong>Solve</strong> distance, speed, and time problems with time = distance/speed.", "<strong>Resolver</strong> problemas de distancia, velocidad y tiempo con tiempo = distancia/velocidad.")],
        secciones, tarea, quiz,
        t("Self-check checklist for rational equations", "Lista de autoevaluación de las ecuaciones racionales"),
        t("Self-check checklist: skills for solving rational equations", "Lista de autoevaluación: destrezas para resolver ecuaciones racionales"),
        [(t("Multiplying by the LCD", "Multiplicar por el MCM"), t("I clear every denominator, multiplying every term by the LCD.", "Limpio todos los denominadores, multiplicando cada término por el MCM."), t("I multiply, but I forget a term.", "Multiplico, pero olvido algún término."), t("I do not find the LCD or I do not use it on every term.", "No identifico el MCM o no lo aplico a todos los términos.")),
         (t("Checking for extraneous solutions", "Verificar soluciones extrañas"), t("I check every solution and explain why one is thrown out.", "Verifico cada solución y justifico el descarte."), t("I check, but I do not throw out the extraneous one.", "Verifico, pero no descarto la solución extraña."), t("I do not check the solutions.", "No verifico las soluciones.")),
         (t("Modeling a problem", "Modelar una aplicación"), t("I set up and solve the problem with a rational equation and check that it makes sense.", "Planteo y resuelvo el problema con una ecuación racional y compruebo que tenga sentido."), t("I set up the equation, but I do not solve it or I interpret it wrong.", "Planteo la ecuación, pero no la resuelvo o la interpreto mal."), t("I do not set up the equation.", "No planteo la ecuación del problema."))],
        t("<p>This lesson closes Topic 5 · Rational expressions. You learned to solve rational equations by multiplying by the LCD, to throw out extraneous solutions, and to model real problems of working together and of distance, speed, and time.</p>\n<p>Topic 6 · Systems of linear equations begins with <strong>Lesson 6.1 · Solving systems of equations by substitution</strong>. You will go from one equation to two equations with two variables, solving one equation for a variable and substituting it in the other to find the solution of the system.</p>",
          "<p>Con esta lección se cierra el Tema 5 · Expresiones racionales. Se aprendió a resolver ecuaciones racionales multiplicando por el MCM, a descartar soluciones extrañas y a modelar problemas reales de trabajo conjunto y de distancia, velocidad y tiempo.</p>\n<p>El Tema 6 · Sistemas de ecuaciones lineales comienza con la <strong>Lección 6.1 · Resolver sistemas de ecuaciones por sustitución</strong>. Se pasará de una sola ecuación a dos ecuaciones con dos variables, despejando una variable y sustituyéndola en la otra para hallar la solución del sistema.</p>"),
        ("6-1", ("", t("Lesson 6.1 · Solving systems of equations by substitution", "Lección 6.1 · Resolver sistemas de ecuaciones por sustitución"))),
        [(t("rational equation", "ecuación racional"), t("An equation with x in a denominator.", "Una ecuación con x en algún denominador.")),
         (t("least common denominator (LCD)", "mínimo común múltiplo (MCM)"), t("The smallest expression that every denominator divides; multiplying by it clears the fractions.", "La menor expresión que todos los denominadores dividen; multiplicar por ella elimina las fracciones.")),
         (t("extraneous solution", "solución extraña"), t("A value found with algebra that makes a denominator of the original equation zero; it is thrown out.", "Un valor obtenido con el álgebra que anula un denominador de la ecuación original; se descarta.")),
         (t("rate of work", "ritmo de trabajo"), t("The part of a job done in one unit of time: 1/a if the whole job takes a hours.", "La parte de un trabajo que se hace en una unidad de tiempo: 1/a si el trabajo completo tarda a horas."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
var O = T(" or ", " o ");
function fr(a, b){ return '<span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + "</span></span>"; }
function bx(p){ return pVis([p, 1]); }
function r3(x){ return Math.round(x * 1000) / 1000; }
function num(x){ var g = r3(x); return Math.abs(g - Math.round(g)) < 1e-9 ? sg(Math.round(g)) : (function(){ for (var d = 2; d <= 12; d++){ var n = Math.round(x * d); if (Math.abs(n / d - x) < 1e-9) return frTxt(n, d); } return sg(g); })(); }
var SOL_AYUDA = T("Type the solution (if there are two, separate them with a comma). A fraction can be written as 1/2.", "Escriba la solución (si hay dos, sepárelas con una coma). Una fracción se escribe como 1/2.");

/* ===== MODULE 1 · Clear the denominators with the LCD ===== */
/* Each case: vis (aria-hidden picture), voz, excl (numbers), lcd (text), mult (equation after multiplying), solve (text), sols (valid numbers) */
function casoMCM(tipo){
  tipo = tipo || elige(["a", "a", "b", "c", "d"]);
  var k = 0;
  while (k++ < 300){
    if (tipo === "a"){ var x0 = nz(-6, 6), m = nz(-5, 5), K = x0 * m, c = nz(-6, 6), d = c + m; if (!K || !d) continue;
      return {vis: fr(sg(K), "x") + " " + (c < 0 ? "− " + -c : "+ " + c) + " = " + sg(d), voz: K + T(" over x, plus ", " sobre x, más ") + c + T(", equals ", ", es igual a ") + d, f: function(x){ return K / x + c - d; }, excl: [0], lcd: "x",
        mult: sg(K) + " " + (c < 0 ? "− " + -c + "x" : "+ " + c + "x") + " = " + sg(d) + "x", solve: sg(K) + " = " + tVis(d - c, 1, true) + ", x = " + num(K / (d - c)), sols: [K / (d - c)]}; }
    if (tipo === "b"){ var x1 = nz(-6, 6), p = nz(-6, 6), b = aleatorio(1, 6), a = b * (x1 + p) / x1; if (!(x1 + p) || a !== Math.round(a) || !a || a === b) continue;
      return {vis: fr(sg(a), bx(p)) + " = " + fr(sg(b), "x"), voz: a + T(" over ", " sobre ") + pVoz([p, 1]) + T(", equals ", ", es igual a ") + b + T(" over x", " sobre x"), f: function(x){ return a / (x + p) - b / x; }, excl: [-p, 0], lcd: "x(" + bx(p) + ")",
        mult: sg(a) + "x = " + b + "(" + bx(p) + ")", solve: sg(a) + "x = " + pVis([b * p, b]) + ", " + sg(a - b) + "x = " + sg(b * p) + ", x = " + num(b * p / (a - b)), sols: [b * p / (a - b)]}; }
    if (tipo === "c"){ var k1 = elige([2, 3, 4, 5]), k2 = elige([2, 3, 4, 5, 6]), q = nz(-6, 6); if (k1 === k2) continue; var xs = k2 * q / (k1 - k2); if (xs !== Math.round(xs)) continue;
      return {vis: fr(bx(q), k1) + " = " + fr("x", k2), voz: pVoz([q, 1]) + T(" over ", " sobre ") + k1 + T(", equals x over ", ", es igual a x sobre ") + k2, f: function(x){ return (x + q) / k1 - x / k2; }, excl: [], lcd: String(k1 * k2 / mcd(k1, k2)),
        mult: (k1 * k2 / mcd(k1, k2) / k1 === 1 ? "" : k1 * k2 / mcd(k1, k2) / k1) + "(" + bx(q) + ") = " + (k1 * k2 / mcd(k1, k2) / k2 === 1 ? "" : k1 * k2 / mcd(k1, k2) / k2) + "x", solve: "x = " + num(xs), sols: [xs]}; }
    if (tipo === "d"){ var r1 = nz(-6, 6), r2 = nz(-6, 6); if (r1 === r2 || r1 + r2 === 0) continue; var Kd = r1 * r2, s = r1 + r2;
      return {vis: "x " + (Kd < 0 ? "− " + fr(-Kd, "x") : "+ " + fr(Kd, "x")) + " = " + sg(s), voz: T("x plus ", "x más ") + Kd + T(" over x, equals ", " sobre x, es igual a ") + s, f: function(x){ return x + Kd / x - s; }, excl: [0], lcd: "x",
        mult: "x<sup>2</sup> " + (Kd < 0 ? "− " + -Kd : "+ " + Kd) + " = " + sg(s) + "x", solve: pVis([Kd, -s, 1]) + " = 0, " + fVis({k: 1, m: 0, f: [[-r1, 1], [-r2, 1]]}) + " = 0, x = " + sg(r1) + O + "x = " + sg(r2), sols: [r1, r2]}; }
  }
  return casoMCM("a");
}
function pasosMCM(c){
  var P = [T("Excluded values: ", "Valores excluidos: ") + (c.excl.length ? c.excl.map(function(v){ return "x = " + sg(v); }).join(T(" and ", " y ")) : T("none (there is no x in a denominator)", "ninguno (no hay x en un denominador)")) + "."];
  P.push(T("LCD of all the denominators: ", "MCM de todos los denominadores: ") + c.lcd + ".");
  P.push(T("Multiply both sides by the LCD: ", "Se multiplican los dos lados por el MCM: ") + c.mult + ".");
  P.push(T("Solve: ", "Se resuelve: ") + c.solve + ".");
  P.push(T("Check: ", "Verificación: ") + c.sols.map(function(v){ return "x = " + num(v); }).join(T(" and ", " y ")) + T(" do not make any denominator zero.", " no anula ningún denominador.").replace("no anula", c.sols.length > 1 ? "no anulan" : "no anula").replace(" do not", c.sols.length > 1 ? " do not" : " does not"));
  P.push(T("Solution: ", "Solución: ") + "<strong>" + c.sols.map(function(v){ return "x = " + num(v); }).join(O) + "</strong>.");
  return P;
}
pasoAPaso4("mc", function(){ var c = casoMCM(); return {enun: T("Solve ", "Resuelva ") + envuelve(c.vis, c.voz) + ".", pasos: pasosMCM(c)}; });
creaPracticaLibre("mq", function(){ var c = casoMCM();
  return {enun: T("Solve ", "Resuelva ") + envuelve(c.vis, c.voz) + ". " + SOL_AYUDA, evalua: function(txt){ var v = leeSol(txt); if (v && v.some(function(x){ return c.excl.indexOf(x) >= 0; })) return {estado: "mal", msg: T("That value makes a denominator zero: it is excluded.", "Ese valor anula un denominador: está excluido.")}; return evaluaSol(txt, c.sols, .006); },
    solucion: pasosMCM(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 2 · Extraneous solutions ===== */
function casoExt(i){
  var r = aleatorio(2, 6), cc = elige([2, 3]);
  var L = [
    {vis: fr("x", "x − " + r) + " = " + fr(r, "x − " + r) + " + " + cc, voz: T("x over x minus " + r + ", equals " + r + " over x minus " + r + ", plus " + cc, "x sobre x menos " + r + ", es igual a " + r + " sobre x menos " + r + ", más " + cc), den: [[-r, 1]], alg: [r], vale: [], f: function(x){ return x / (x - r) - r / (x - r) - cc; },
     mult: "x = " + r + " + " + cc + "(x − " + r + ")"},
    {vis: fr("x<sup>2</sup>", "x − " + r) + " = " + fr(r * r, "x − " + r), voz: T("x squared over x minus " + r + ", equals " + r * r + " over x minus " + r, "x al cuadrado sobre x menos " + r + ", es igual a " + r * r + " sobre x menos " + r), den: [[-r, 1]], alg: [r, -r], vale: [-r], f: function(x){ return (x * x - r * r) / (x - r); },
     mult: "x<sup>2</sup> = " + r * r},
    {vis: fr(cc + 1, "x") + " + 1 = " + fr(cc + 1 + r, "x"), voz: (cc + 1) + T(" over x, plus 1, equals ", " sobre x, más 1, es igual a ") + (cc + 1 + r) + T(" over x", " sobre x"), den: [[0, 1]], alg: [r], vale: [r], f: function(x){ return (cc + 1) / x + 1 - (cc + 1 + r) / x; },
     mult: (cc + 1) + " + x = " + (cc + 1 + r)},
    {vis: fr("x", "x + " + r) + " = " + fr("−" + r, "x + " + r) + " + " + cc, voz: T("x over x plus " + r + ", equals negative " + r + " over x plus " + r + ", plus " + cc, "x sobre x más " + r + ", es igual a menos " + r + " sobre x más " + r + ", más " + cc), den: [[r, 1]], alg: [-r], vale: [], f: null,
     mult: "x = −" + r + " + " + cc + "(x + " + r + ")"}];
  return L[i === undefined ? aleatorio(0, L.length - 1) : i];
}
var XT = null;
function xtNuevo(){ XT = casoExt(+$("xt-ex").value); $("xt-eq").innerHTML = envuelve(XT.vis, XT.voz); $("xt-x").value = ""; $("xt-txt").innerHTML = '<div class="linea">' + T("Multiplying by the LCD gives ", "Al multiplicar por el MCM queda ") + XT.mult + T(", and the algebra gives ", ", y el álgebra da ") + XT.alg.map(function(v){ return "x = " + sg(v); }).join(O) + ". " + T("Check each value.", "Verifique cada valor.") + "</div>"; }
function xtVerifica(vals){
  $("xt-txt").innerHTML = vals.map(function(x){
    var ceros = XT.den.filter(function(q){ return Math.abs(pEval(q, x)) < 1e-9; });
    return '<div class="linea">x = ' + sg(x) + ": " + XT.den.map(function(q){ return pVis(q) + " = " + sg(r3(pEval(q, x))); }).join("; ") + ". " + (ceros.length ? '<strong style="color:#c62828">' + T("A denominator is zero: x = " + sg(x) + " is extraneous and is thrown out.", "Un denominador vale cero: x = " + sg(x) + " es una solución extraña y se descarta.") + "</strong>" : '<strong style="color:#2e7d32">' + T("No denominator is zero" + (XT.alg.indexOf(x) >= 0 ? ": x = " + sg(x) + " is valid." : "."), "Ningún denominador vale cero" + (XT.alg.indexOf(x) >= 0 ? ": x = " + sg(x) + " es válida." : ".")) + "</strong>") + "</div>";
  }).join("") + (vals === XT.alg ? '<div class="linea"><strong>' + (XT.vale.length ? T("Solution: ", "Solución: ") + XT.vale.map(function(v){ return "x = " + sg(v); }).join(O) : T("Every solution is extraneous: the equation has no solution.", "Todas las soluciones son extrañas: la ecuación no tiene solución.")) + "</strong></div>" : "");
}
$("xt-ex").addEventListener("change", xtNuevo);
$("xt-ver").addEventListener("click", function(){ var v = leeSol($("xt-x").value); if (!v || v.length !== 1){ $("xt-txt").innerHTML = '<div class="linea">' + T("Type one number.", "Escriba un número.") + "</div>"; return; } xtVerifica(v); });
$("xt-alg").addEventListener("click", function(){ xtVerifica(XT.alg); });
xtNuevo();
OMR("xq", function(){ var c = casoExt();
  var ok = c.vale.length ? "v" + c.vale.join("") : "ninguna", ops = [{clave: "ninguna", html: T("No solution: every value is extraneous", "Ninguna solución: todos los valores son extraños")}];
  c.alg.forEach(function(v){ ops.push({clave: "v" + v, html: "x = " + sg(v) + T(" only", " solamente")}); });
  if (c.alg.length > 1) ops.push({clave: "ambas", html: c.alg.map(function(v){ return "x = " + sg(v); }).join(T(" and ", " y "))});
  return {enun: T("Solving ", "Al resolver ") + envuelve(c.vis, c.voz) + T(" with the LCD gives ", " con el MCM se obtiene ") + c.alg.map(function(v){ return "x = " + sg(v); }).join(O) + ". " + T("What is the solution?", "¿Cuál es la solución?"), correcta: ok, opciones: ops,
    pista: T("Substitute each value in the denominators of the original equation.", "Sustituya cada valor en los denominadores de la ecuación original."),
    bien: c.alg.map(function(v){ var z = c.den.some(function(q){ return Math.abs(pEval(q, v)) < 1e-9; }); return "x = " + sg(v) + (z ? T(" makes a denominator zero: extraneous.", " anula un denominador: extraña.") : T(" is valid.", " es válida.")); }).join(" ")};
});

/* ===== MODULE 3 · Working together ===== */
function trDibuja(){
  var a = leeSol($("tr-a").value), b = leeSol($("tr-b").value), out = $("tr-txt");
  if (!a || !b || a.length !== 1 || b.length !== 1 || a[0] <= 0 || b[0] <= 0){ out.innerHTML = '<div class="linea">' + T("Type two positive times.", "Escriba dos tiempos positivos.") + "</div>"; $("tr-barra").innerHTML = ""; return; }
  a = a[0]; b = b[0]; var t = a * b / (a + b), pa = 1 / a, pb = 1 / b;
  var ancho = function(p){ return Math.min(100, p * 100); };
  $("tr-barra").innerHTML = '<div class="barra-trabajo" role="img" aria-label="' + T("In one hour, the first person does " + num(pa) + " of the job and the second " + num(pb) + "; together, " + num(pa + pb) + ".", "En una hora, la primera persona hace " + num(pa) + " del trabajo y la segunda " + num(pb) + "; juntas, " + num(pa + pb) + ".") + '"><span style="width:' + ancho(pa) + '%;background:#1565c0">' + (pa >= .12 ? num(pa) : "") + '</span><span style="width:' + Math.min(100 - ancho(pa), ancho(pb)) + '%;background:#2e7d32">' + (pb >= .12 ? num(pb) : "") + '</span></div>';
  out.innerHTML = '<div class="linea">' + T("In one hour: ", "En una hora: ") + "1/" + num(a) + " + 1/" + num(b) + " = " + num(pa + pb) + T(" of the job.", " del trabajo.") + "</div>" +
    '<div class="linea">1/t = ' + num(pa + pb) + ", t = " + num(t) + (Math.abs(t - Math.round(t * 100) / 100) > 1e-9 ? " ≈ " + sg(Math.round(t * 100) / 100) : "") + T(" hours", " horas") + " (" + Math.round(t * 60) + T(" minutes).", " minutos).") + "</div>" +
    '<div class="linea">' + T("Check: " + num(t) + " h is less than the faster one alone (" + num(Math.min(a, b)) + " h). ✓", "Comprobación: " + num(t) + " h es menos que el más rápido solo (" + num(Math.min(a, b)) + " h). ✓") + "</div>";
}
["tr-a", "tr-b"].forEach(function(id){ $(id).addEventListener("input", trDibuja); }); trDibuja();
var PARES = [[2, 2], [3, 6], [4, 12], [6, 3], [5, 20], [10, 15], [12, 6], [4, 4], [6, 12], [8, 24], [2, 6], [3, 3], [12, 4], [20, 30], [6, 6], [9, 18]];
var CONTX = [[T("paints a room", "pinta un cuarto"), T("painting", "pintar")], [T("fills a tank (one faucet)", "llena un tanque (una llave)"), T("filling", "llenar")], [T("mows a lawn", "corta el césped de un jardín"), T("mowing", "cortar")], [T("prints an order (one printer)", "imprime un pedido (una impresora)"), T("printing", "imprimir")]];
OMR("wq", function(){ var p = elige(PARES), a = p[0], b = p[1], t = a * b / (a + b), ctx = elige(CONTX);
  var ops = [{clave: "ok", html: num(t) + " h"}, {clave: "suma", html: num(a + b) + " h"}, {clave: "media", html: num((a + b) / 2) + " h"}, {clave: "dif", html: num(Math.abs(a - b) || a / 4) + " h"}];
  var vis = {}; ops = ops.filter(function(o){ if (vis[o.html]) return false; vis[o.html] = 1; return true; });
  return {enun: T("One alone ", "Uno solo ") + ctx[0] + T(" in ", " en ") + a + T(" h; the other, in ", " h; el otro, en ") + b + T(" h. How long do they take working together?", " h. ¿Cuánto tardan trabajando juntos?"), correcta: "ok", opciones: ops,
    porClave: {suma: T("Do not add the times: together they take less, not more.", "No sume los tiempos: juntos tardan menos, no más."), media: T("The average is not right either: add the rates 1/a + 1/b.", "El promedio tampoco: sume los ritmos 1/a + 1/b."), dif: T("Use 1/a + 1/b = 1/t.", "Use 1/a + 1/b = 1/t.")},
    pista: T("Each one does 1/a and 1/b of the job per hour. Add them and flip.", "Cada uno hace 1/a y 1/b del trabajo por hora. Súmelos y voltee."), bien: "1/" + a + " + 1/" + b + " = " + num(1 / a + 1 / b) + " = 1/t, t = " + num(t) + " h."};
});

/* ===== MODULE 4 · Distance, speed, and time ===== */
function boDibuja(){
  var v = +$("bo-v").value, c = +$("bo-c").value, d = +$("bo-d").value, out = $("bo-txt");
  $("bo-vv").textContent = v; $("bo-cv").textContent = c; $("bo-dv").textContent = d;
  var baja = d / (v + c), sube = v - c > 0 ? d / (v - c) : null, h = function(x){ var m = Math.round(x * 60); return Math.floor(m / 60) + " h" + (m % 60 ? " " + (m % 60) + " min" : ""); };
  var W = 460, H = 120, s = '<rect x="10" y="30" width="440" height="60" rx="10" fill="#e3f2fd" stroke="#90caf9"/>';
  for (var i = 0; i < 4; i++) s += '<path d="M' + (40 + i * 110) + ' 60 h40" stroke="#1e88e5" stroke-width="3" marker-end="url(#fc)"/>';
  s += '<defs><marker id="fc" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="#1e88e5"/></marker></defs><text x="230" y="22" text-anchor="middle" font-size="13" fill="#1565c0">' + T("current: " + c + " mph", "corriente: " + c + " mph") + '</text><text x="230" y="112" text-anchor="middle" font-size="13" fill="#37474f">' + d + T(" miles each way", " millas en cada sentido") + "</text>";
  $("bo-svg").innerHTML = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("A river with a current of " + c + " miles per hour.", "Un río con una corriente de " + c + " millas por hora.") + '" style="display:block;margin:auto;max-width:' + W + 'px;width:100%">' + s + "</svg>";
  out.innerHTML = '<div class="linea">' + T("Downstream (with the current): speed ", "A favor de la corriente: velocidad ") + v + " + " + c + " = " + (v + c) + " mph; " + T("time ", "tiempo ") + d + "/" + (v + c) + " = " + num(baja) + " h (" + h(baja) + ").</div>" +
    '<div class="linea">' + T("Upstream (against the current): speed ", "En contra de la corriente: velocidad ") + v + " − " + c + " = " + (v - c) + " mph; " + (sube !== null ? T("time ", "tiempo ") + d + "/" + (v - c) + " = " + num(sube) + " h (" + h(sube) + ")." : '<strong style="color:#c62828">' + (v === c ? T("the denominator v − c is 0: the boat never moves forward. It is the same as an excluded value.", "el denominador v − c vale 0: el bote nunca avanza. Es lo mismo que un valor excluido.") : T("the speed is negative: the current pushes the boat back.", "la velocidad es negativa: la corriente arrastra el bote hacia atrás.")) + "</strong>") + "</div>";
}
["bo-v", "bo-c", "bo-d"].forEach(function(id){ $(id).addEventListener("input", boDibuja); }); boDibuja();
var BO_ULT = -1;
OMR("vq", function(){
  var tipo; do { tipo = aleatorio(0, 2); } while (tipo === BO_ULT); BO_ULT = tipo;
  var c = aleatorio(2, 6), v = c + aleatorio(3, 15), veh = elige([[T("A boat", "Un bote"), T("still water", "agua quieta"), T("the current", "la corriente"), T("the current", "de la corriente")], [T("A small plane", "Una avioneta"), T("calm air", "aire en calma"), T("the wind", "el viento"), T("the wind", "del viento")]]);
  if (veh[0] !== T("A boat", "Un bote")){ v *= 10; c *= 10; }
  if (tipo === 0){ var a = Math.random() < .5;
    return {enun: veh[0] + T(" goes ", " va a ") + v + T(" mph in ", " mph en ") + veh[1] + T(". With ", ". Con ") + veh[2] + " (" + c + " mph) " + (a ? T("helping it", "a favor") : T("against it", "en contra")) + T(", what is its real speed?", ", ¿cuál es su velocidad efectiva?"), correcta: "ok",
      opciones: [{clave: "ok", html: (a ? v + c : v - c) + " mph"}, {clave: "m", html: (a ? v - c : v + c) + " mph"}, {clave: "v", html: v + " mph"}, {clave: "p", html: v * c + " mph"}], pista: a ? T("Helping: add.", "A favor: se suma.") : T("Against: subtract.", "En contra: se resta."), bien: (a ? v + " + " + c + " = " + (v + c) : v + " − " + c + " = " + (v - c)) + " mph."}; }
  if (tipo === 1){ var k = aleatorio(1, 4), d = k * (v + c);
    return {enun: veh[0] + T(" goes ", " va a ") + v + T(" mph in ", " mph en ") + veh[1] + T(" and travels ", " y recorre ") + d + T(" miles with ", " millas con ") + veh[2] + " (" + c + " mph) " + T("helping it. How long does it take?", "a favor. ¿Cuánto tarda?"), correcta: "ok",
      opciones: [{clave: "ok", html: num(d / (v + c)) + " h"}, {clave: "m", html: num(d / (v - c)) + " h"}, {clave: "v", html: num(d / v) + " h"}, {clave: "x", html: num(d * (v + c) / 100) + " h"}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }),
      pista: T("time = distance / speed, with the real speed.", "tiempo = distancia / velocidad, con la velocidad efectiva."), bien: d + " / (" + v + " + " + c + ") = " + d + "/" + (v + c) + " = " + num(d / (v + c)) + " h."}; }
  var kk = aleatorio(1, 3), d1 = kk * (v + c), d2 = kk * (v - c);
  return {enun: veh[0] + T(" goes ", " va a ") + v + T(" mph in ", " mph en ") + veh[1] + T(". It takes the same time to go ", ". Tarda lo mismo en recorrer ") + d1 + T(" miles with ", " millas con ") + veh[2] + T(" as ", " a favor que ") + d2 + T(" miles against it. How fast is ", " millas en contra. ¿Cuál es la velocidad ") + veh[3] + "?", correcta: "ok",
    opciones: [{clave: "ok", html: c + " mph"}, {clave: "a", html: (c + aleatorio(1, 3)) + " mph"}, {clave: "b", html: Math.max(1, c - aleatorio(1, c - 1 || 1)) + " mph"}, {clave: "d", html: (d1 - d2) + " mph"}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }),
    pista: d1 + "/(" + v + " + c) = " + d2 + "/(" + v + " − c). " + T("Multiply by the LCD.", "Multiplique por el MCM."), bien: d1 + "(" + v + " − c) = " + d2 + "(" + v + " + c) → " + (d1 * v) + " − " + d1 + "c = " + (d2 * v) + " + " + d2 + "c → " + (d1 * v - d2 * v) + " = " + (d1 + d2) + "c → c = " + c + " mph."};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "")
    campo = lambda i, et, v: f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{i}" value="{v}" style="width:6em"></div>'
    eqs = [("0", "x/(x − r) = r/(x − r) + c"), ("1", "x²/(x − r) = r²/(x − r)"), ("2", "a/x + 1 = b/x"), ("3", "x/(x + r) = −r/(x + r) + c")]
    mods = [
     (t("lcd", "mcm"), t("Clearing the denominators with the LCD", "Limpiar los denominadores con el MCM"),
      f'''      <p>{t("Four moves: write down the excluded values, multiply both sides by the LCD of all the denominators, solve the equation that is left, and check the solution against the excluded values.", "Cuatro movimientos: anotar los valores excluidos, multiplicar los dos lados por el MCM de todos los denominadores, resolver la ecuación que queda y verificar la solución contra los valores excluidos.")}</p>
{n4.pasos("mc", t("Another equation", "Otra ecuación"))}
      <div class="caja-tip">{t("Multiplying by the LCD is not the same as adding fractions: here there is an equals sign, so you can multiply everything by the LCD and the denominators disappear. In a sum with no equals sign, the denominators stay.", "Multiplicar por el MCM no es lo mismo que sumar fracciones: aquí hay un signo de igual, así que se puede multiplicar todo por el MCM y los denominadores desaparecen. En una suma sin igual, los denominadores se conservan.")}</div>
{libre("mq", t("Practice: solve the equation", "Practique: resuelva la ecuación"), t("Solution", "Solución"))}'''),
     (t("extraneous", "extranas"), t("Extraneous solutions: the checker", "Soluciones extrañas: el verificador"),
      f'''      <p>{t("Multiplying by the LCD can produce a value that solves the equation without fractions but makes a denominator of the original equation zero. That value is an extraneous solution and is thrown out. The only way to catch it is to check.", "Al multiplicar por el MCM puede aparecer un valor que resuelve la ecuación sin fracciones pero que anula un denominador de la ecuación original. Ese valor es una solución extraña y hay que descartarlo. La única forma de detectarlo es verificar.")}</p>
      <div class="panel"><div class="campos">{n4.lista("xt-ex", t("Kind of equation", "Tipo de ecuación"), eqs)}</div>
        <p class="enun" id="xt-eq"></p>
        <div class="campos">{campo("xt-x", t("Check the value x =", "Verifique el valor x ="), "")}</div>
        <div class="fila-btn"><button type="button" class="btn" id="xt-ver">{t("Check", "Verificar")}</button><button type="button" class="btn-sec" id="xt-alg">{t("Use the values the algebra gives", "Usar los valores que da el álgebra")}</button></div></div>
{n4.salida("xt-txt")}
      <div class="caja-atencion"><strong>{t("An extraneous solution is not an arithmetic mistake.", "Una solución extraña no es un error de cuentas.")}</strong> {t("The algebra is right: multiplying by the LCD multiplied by something that is zero for that value of x, and that adds a solution the original equation did not have. If every solution is extraneous, the equation has no solution.", "El álgebra está bien hecha: al multiplicar por el MCM se multiplicó por algo que vale cero para ese valor de x, y eso agrega una solución que la ecuación original no tenía. Si todas las soluciones resultan extrañas, la ecuación no tiene solución.")}</div>
{B.om("xq", t("Practice: valid or extraneous?", "Practique: ¿válida o extraña?"))}'''),
     (t("work", "trabajo"), t("Working together", "Problemas de trabajo conjunto"),
      f'''{n4.formula("1/a + 1/b = 1/t")}
      <p>{t("If a person takes a hours to do a whole job, in one hour they do 1/a of it. That is the whole idea: add the parts each one does in one hour.", "Si una persona tarda a horas en hacer un trabajo completo, en una hora hace 1/a del trabajo. Esa es toda la idea: se suman las partes que cada quien hace en una hora.")}</p>
      <div class="panel"><div class="campos">{campo("tr-a", t("The first person takes (hours)", "La primera persona tarda (horas)"), 3)}{campo("tr-b", t("The second person takes (hours)", "La segunda persona tarda (horas)"), 6)}</div></div>
      <div id="tr-barra"></div>
{n4.salida("tr-txt")}
      <div class="caja-tip">{t("Common-sense check: together they always take less than the faster one alone. If the result is greater, the times were added instead of the rates.", "Control de sentido común: juntos siempre tardan menos que el más rápido de los dos por separado. Si el resultado sale mayor, se sumaron los tiempos en vez de los ritmos.")}</div>
{B.om("wq", t("Practice: working together", "Practique: trabajo conjunto"))}'''),
     (t("distance", "dvt"), t("Distance, speed, and time", "Distancia, velocidad y tiempo"),
      f'''{n4.formula(t("time = distance / speed", "tiempo = distancia / velocidad"))}
      <p>{t("Since the speed is in the denominator, as soon as the speed has a variable a rational equation appears. The classic case is a boat on a river or a plane in the wind: with the current the real speed is v + c, and against it, v − c.", "Como la velocidad está en el denominador, en cuanto la velocidad lleva una variable aparece una ecuación racional. El caso clásico es un bote en un río o un avión con viento: a favor, la velocidad efectiva es v + c, y en contra, v − c.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="bo-v">{t("Boat speed in still water:", "Velocidad del bote en agua quieta:")} <output id="bo-vv"></output> mph</label><input type="range" id="bo-v" min="4" max="30" step="1" value="15"></div>
        <div class="campo"><label for="bo-c">{t("Speed of the current:", "Velocidad de la corriente:")} <output id="bo-cv"></output> mph</label><input type="range" id="bo-c" min="0" max="20" step="1" value="5"></div>
        <div class="campo"><label for="bo-d">{t("Distance each way:", "Distancia en cada sentido:")} <output id="bo-dv"></output> {t("miles", "millas")}</label><input type="range" id="bo-d" min="5" max="60" step="5" value="20"></div></div></div>
      <div class="geo-svg" id="bo-svg"></div>
{n4.salida("bo-txt")}
      <div class="caja-tip">{t("Try making the current equal to the speed of the boat. The denominator v − c becomes zero and the upstream time stops existing: it is the excluded value of the first activity, told as a real story.", "Pruebe a poner la corriente igual que la velocidad del bote. El denominador v − c se vuelve cero y el tiempo de subida deja de existir: es el mismo valor excluido de la primera actividad, contado como historia real.")}</div>
{B.om("vq", t("Practice: distance, speed, and time", "Practique: distancia, velocidad y tiempo"))}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver ecuaciones racionales")
