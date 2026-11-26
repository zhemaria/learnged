"""Level 4 · Lesson 6.1 · Solving systems of equations by substitution — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_6-1.html and algebra/n4-l6-1.html (the five steps of substitution with the graph of the
system, the ordered-pair checker, and setting up word problems). They are rebuilt here, inside LearnGED, with math/sys4.js.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "6-1"
TEMA = ("Systems of linear equations", "Sistemas de ecuaciones lineales")
TIT = ("Solving systems of equations by substitution", "Resolver sistemas de ecuaciones por sustitución")
SCRIPTS = n4.SCRIPTS + ("/math/sys4.js",)
ESTILO_SIS = """
  .sistema{display:inline-flex;align-items:center;gap:4px;vertical-align:middle;margin:2px 4px;}
  .sistema .llave{font-size:2.5em;line-height:1;font-weight:300;}
  .sistema .ecs{display:flex;flex-direction:column;line-height:1.35;}
"""
ESTILO = n4.ESTILO + ESTILO_SIS

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Topic 5.</strong> Until now you solved one equation with one unknown. In Topic 6 you work with two equations at once, each with two variables (x and y). Solving the system means finding the pair (x, y) that makes both equations true at the same time. On a graph, it is the point where the two lines cross.", "<strong>Conexión con el tema anterior.</strong> Hasta ahora se resolvía una ecuación con una incógnita. En el Tema 6 se trabaja con dos ecuaciones a la vez, cada una con dos variables (x e y). Resolver el sistema es encontrar el par (x, y) que cumple las dos ecuaciones al mismo tiempo. Gráficamente, es el punto donde se cruzan las dos rectas.")}</p>
<p>{t("A <strong>system of linear equations</strong> is a set of two equations with the same two variables. Its <strong>solution</strong> is the ordered pair (x, y) that makes both equations true.", "Un <strong>sistema de ecuaciones lineales</strong> es un conjunto de dos ecuaciones con las mismas dos variables. La <strong>solución</strong> es el par ordenado (x, y) que hace verdaderas ambas ecuaciones.")}</p>
{caja("tip", t("The key idea", "Idea clave"), t("<p>For the system x + y = 5 and x − y = 1, the pair (3, 2) is the solution because it works in both: 3 + 2 = 5 and 3 − 2 = 1. No other pair works in both at once.</p>", "<p>Para el sistema x + y = 5 y x − y = 1, el par (3, 2) es la solución porque cumple las dos: 3 + 2 = 5 y 3 − 2 = 1. Ningún otro par cumple ambas a la vez.</p>"))}
{caja("ojo", t("Both equations, always", "Las dos ecuaciones, siempre"), t("<p>A solution must work in both equations: it is not enough for a pair to work in one of them. That is why, at the end, you always check in both.</p>", "<p>Una solución debe cumplir las dos ecuaciones: no basta con que un par satisfaga una de ellas. Por eso, al final, siempre se verifica en ambas.</p>"))}
{enlace(n, t("check", "verificar"), t("checking ordered pairs", "la verificación de pares ordenados"), t("Type any pair (x, y): it is substituted in both equations and placed on the graph next to the lines.", "Escriba cualquier par (x, y): se sustituye en las dos ecuaciones y se sitúa en la gráfica junto a las rectas."))}'''

    s2 = f'''{tabla(t("The five steps of substitution", "Los cinco pasos de la sustitución"), t("The five steps to solve a system by substitution", "Los cinco pasos para resolver un sistema por sustitución"), [t("Step", "Paso"), t("What to do", "Acción")],
  [["1", t("Solve one of the equations for one variable.", "Despejar una variable en una de las ecuaciones.")], ["2", t("Substitute that expression into the other equation.", "Sustituir esa expresión en la otra ecuación.")], ["3", t("Solve the equation you get (it has only one variable).", "Resolver la ecuación resultante (queda una sola variable).")], ["4", t("Substitute that value to find the other variable.", "Sustituir ese valor para hallar la otra variable.")], ["5", t("Check the solution in both original equations.", "Verificar la solución en las dos ecuaciones originales.")]])}
{ejemplo(t("Example 1: solve the system y = 2x + 1 and 3x + y = 11.", "Ejemplo 1 · Resolver el sistema y = 2x + 1 y 3x + y = 11."),
  [("1", t("The first equation already has y alone:", "La primera ecuación ya tiene y despejada:"), "y = 2x + 1."), ("2", t("Substitute into the other:", "Se sustituye en la otra:"), "3x + (2x + 1) = 11."), ("3", t("Solve:", "Se resuelve:"), t("5x + 1 = 11, so x = 2.", "5x + 1 = 11, así que x = 2.")), ("4", t("Find y:", "Se halla y:"), "y = 2(2) + 1 = 5."), ("5", t("Check:", "Verificación:"), t("3(2) + 5 = 11. Right.", "3(2) + 5 = 11. Correcto.")),
   ("✓", t("Solution.", "Solución."), "<strong>(2, 5)</strong>.")])}
{ejemplo(t("Example 2: solve first. Solve the system x + y = 7 and 2x − y = 2.", "Ejemplo 2 · Despejar primero. Resolver el sistema x + y = 7 y 2x − y = 2."),
  [("1", t("Solve the first for y:", "Se despeja y en la primera:"), "y = 7 − x."), ("2", t("Substitute:", "Se sustituye:"), "2x − (7 − x) = 2."), ("3", t("Solve:", "Se resuelve:"), t("3x − 7 = 2, so x = 3.", "3x − 7 = 2, así que x = 3.")), ("4", t("Find y:", "Se halla y:"), "y = 7 − 3 = 4."), ("✓", t("Solution.", "Solución."), "<strong>(3, 4)</strong>.")])}
{caja("tip", t("Choose the easiest variable", "Elija la variable más fácil de despejar"), t("<p>Solve for the variable whose coefficient is 1 or −1: that way you avoid fractions. And use parentheses when you substitute, especially after a minus sign: 2x − (7 − x) = 2x − 7 + x.</p>", "<p>Conviene despejar la variable cuyo coeficiente es 1 o −1: así se evitan fracciones. Y use paréntesis al sustituir, sobre todo después de un signo menos: 2x − (7 − x) = 2x − 7 + x.</p>"))}
{practica("p1", t("Practice 1 — y = x + 2 ; 2x + y = 8", "Práctica 1 — y = x + 2 ; 2x + y = 8"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(4, 2)"), ("b", "(2, 4)"), ("c", "(2, 2)")])}
{practica("p2", t("Practice 2 — x = y + 1 ; x + 2y = 10", "Práctica 2 — x = y + 1 ; x + 2y = 10"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(3, 4)"), ("b", "(1, 3)"), ("c", "(4, 3)")])}
{practica("p3", t("Practice 3 — y = 3x ; x + y = 8", "Práctica 3 — y = 3x ; x + y = 8"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(2, 6)"), ("b", "(6, 2)"), ("c", "(2, 2)")])}
{enlace(n, t("substitution", "sustitucion"), t("substitution", "la sustitución"), t("Systems solved step by step, with the two lines drawn and the crossing point that appears when you check.", "Sistemas resueltos paso a paso, con las dos rectas dibujadas y el punto de cruce que aparece al verificar."))}'''

    s3 = f'''<p>{t("To check whether a pair (x, y) is a solution of a system, substitute it in both equations. If it works in both, it is a solution; if it fails in one, it is not.", "Para comprobar si un par (x, y) es solución de un sistema, se sustituye en las dos ecuaciones. Si cumple ambas, es solución; si falla en una, no lo es.")}</p>
{ejemplo(t("Example 3: is (4, 1) a solution of x + y = 5 and x − y = 3?", "Ejemplo 3 · ¿Es (4, 1) solución de x + y = 5 y x − y = 3?"),
  [("1", t("First:", "Primera:"), t("4 + 1 = 5. Right.", "4 + 1 = 5. Correcto.")), ("2", t("Second:", "Segunda:"), t("4 − 1 = 3. Right.", "4 − 1 = 3. Correcto.")), ("✓", t("Answer.", "Respuesta."), t("<strong>Yes, (4, 1) is a solution.</strong>", "<strong>Sí, (4, 1) es solución.</strong>"))])}
{practica("p4", t("Practice 4 — (3, 2)", "Práctica 4 — (3, 2)"), t("Is (3, 2) a solution of x + y = 5 and x − y = 1?", "¿Es (3, 2) solución de x + y = 5 y x − y = 1?"), [("a", "No"), ("b", t("Only of the first", "Solo de la primera")), ("c", t("Yes, it works in both", "Sí, cumple ambas"))])}
{practica("p5", t("Practice 5 — (1, 4)", "Práctica 5 — (1, 4)"), t("Is (1, 4) a solution of 2x + y = 6 and x + y = 5?", "¿Es (1, 4) solución de 2x + y = 6 y x + y = 5?"), [("a", "No"), ("b", t("Yes, it works in both", "Sí, cumple ambas")), ("c", t("Only of the second", "Solo de la segunda"))])}
{practica("p6", t("Practice 6 — (2, 1)", "Práctica 6 — (2, 1)"), t("Is (2, 1) a solution of x + y = 3 and 2x − y = 2?", "¿Es (2, 1) solución de x + y = 3 y 2x − y = 2?"), [("a", t("No, it fails the second", "No, falla la segunda")), ("b", t("Yes, it works in both", "Sí, cumple ambas")), ("c", t("No, it fails the first", "No, falla la primera"))])}
{enlace(n, t("check", "verificar"), t("checking ordered pairs", "la verificación de pares ordenados"), t("Type any pair (x, y) and see it substituted in both equations and placed on the graph next to the lines.", "Escriba cualquier par (x, y) y véalo sustituido en las dos ecuaciones y situado en la gráfica junto a las rectas."))}'''

    s4 = f'''<p>{t("Many real problems have two unknowns and two facts. Give each unknown a variable, write two equations, and solve the system.", "Muchos problemas reales tienen dos incógnitas y dos datos. Se asigna una variable a cada incógnita, se plantean dos ecuaciones y se resuelve el sistema.")}</p>
{ejemplo(t("Example 4: at a coffee shop, 2 coffees and 1 tea cost $7; 1 coffee and 1 tea cost $5. How much does each one cost?", "Ejemplo 4 · En una cafetería, 2 cafés y 1 té cuestan $7; 1 café y 1 té cuestan $5. ¿Cuánto cuesta cada uno?"),
  [("1", t("Let c be the price of a coffee and t the price of a tea:", "Sea c el precio del café y t el del té:"), t("2c + t = 7 and c + t = 5.", "2c + t = 7 y c + t = 5.")), ("2", t("Solve the second for t:", "Se despeja t en la segunda:"), "t = 5 − c."), ("3", t("Substitute:", "Se sustituye:"), t("2c + (5 − c) = 7, so c + 5 = 7, c = 2.", "2c + (5 − c) = 7, así que c + 5 = 7, c = 2.")), ("4", t("Find t:", "Se halla t:"), "t = 5 − 2 = 3."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>The coffee costs $2 and the tea, $3.</strong>", "<strong>El café cuesta $2 y el té, $3.</strong>"))])}
{practica("p7", t("Practice 7 — The coffee", "Práctica 7 — El café"), t("With the system of the example (2c + t = 7 ; c + t = 5), how much does the coffee cost?", "Con el sistema del ejemplo (2c + t = 7 ; c + t = 5), ¿cuánto cuesta el café?"), [("a", "$3"), ("b", "$2"), ("c", "$5")])}
{practica("p8", t("Practice 8 — Two numbers", "Práctica 8 — Dos números"), t("Two numbers add up to 10 and their difference is 4. What are they?", "Dos números suman 10 y su diferencia es 4. ¿Cuáles son?"), [("a", t("7 and 3", "7 y 3")), ("b", t("6 and 4", "6 y 4")), ("c", t("5 and 5", "5 y 5"))])}
{enlace(n, t("context", "contexto"), t("setting up problems", "el planteamiento de problemas"), t("Real situations set up step by step: name the unknowns, turn each fact into an equation, and reread the answer.", "Situaciones reales armadas paso a paso: nombrar las incógnitas, traducir cada dato en una ecuación y releer la respuesta."))}'''

    secciones = [("s-" + t("system", "sistema"), t("What is a system and what is its solution?", "¿Qué es un sistema y qué es su solución?"), s1),
                 ("s-" + t("substitution", "sustitucion"), t("The five steps of substitution", "Los cinco pasos de la sustitución"), s2),
                 ("s-" + t("check", "verificar"), t("Checking an ordered pair", "Verificar un par ordenado"), s3),
                 ("s-" + t("context", "contexto"), t("Application: prices", "Aplicación: el sistema de precios"), s4)]

    lesson = {"next": t("Lesson 6.2", "Lección 6.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Write x first: (x, y).", "Escriba primero x: (x, y)."), "c": t("Check y = x + 2: 2 + 2 = 4, not 2.", "Compruebe y = x + 2: 2 + 2 = 4, no 2.")}, "right": t("2x + (x + 2) = 8, 3x = 6, x = 2, y = 4.", "2x + (x + 2) = 8, 3x = 6, x = 2, y = 4."), "solution": "(2, 4)."},
      "p2": {"ok": "c", "hints": {"a": t("Check x = y + 1: 4 + 1 = 5, not 3.", "Compruebe x = y + 1: 4 + 1 = 5, no 3."), "b": t("Check x + 2y = 10: 1 + 6 = 7, not 10.", "Compruebe x + 2y = 10: 1 + 6 = 7, no 10.")}, "right": t("(y + 1) + 2y = 10, 3y = 9, y = 3, x = 4.", "(y + 1) + 2y = 10, 3y = 9, y = 3, x = 4."), "solution": "(4, 3)."},
      "p3": {"ok": "a", "hints": {"b": t("Write x first: y = 3x, so y is the bigger one.", "Escriba primero x: y = 3x, así que y es el mayor."), "c": t("Check y = 3x: 3 · 2 = 6, not 2.", "Compruebe y = 3x: 3 · 2 = 6, no 2.")}, "right": t("x + 3x = 8, x = 2, y = 6.", "x + 3x = 8, x = 2, y = 6."), "solution": "(2, 6)."},
      "p4": {"ok": "c", "hints": {"a": t("Substitute: 3 + 2 = 5 and 3 − 2 = 1.", "Sustituya: 3 + 2 = 5 y 3 − 2 = 1."), "b": t("Check the second too: 3 − 2 = 1.", "Compruebe también la segunda: 3 − 2 = 1.")}, "right": t("3 + 2 = 5 ✓ and 3 − 2 = 1 ✓.", "3 + 2 = 5 ✓ y 3 − 2 = 1 ✓."), "solution": t("Yes, it works in both.", "Sí, cumple ambas.")},
      "p5": {"ok": "b", "hints": {"a": t("Substitute: 2(1) + 4 = 6 and 1 + 4 = 5.", "Sustituya: 2(1) + 4 = 6 y 1 + 4 = 5."), "c": t("Check the first too: 2(1) + 4 = 6.", "Compruebe también la primera: 2(1) + 4 = 6.")}, "right": t("2 + 4 = 6 ✓ and 1 + 4 = 5 ✓.", "2 + 4 = 6 ✓ y 1 + 4 = 5 ✓."), "solution": t("Yes, it works in both.", "Sí, cumple ambas.")},
      "p6": {"ok": "a", "hints": {"b": t("Check the second: 2(2) − 1 = 3, not 2.", "Compruebe la segunda: 2(2) − 1 = 3, no 2."), "c": t("The first works: 2 + 1 = 3.", "La primera sí se cumple: 2 + 1 = 3.")}, "right": t("2 + 1 = 3 ✓, but 4 − 1 = 3, not 2.", "2 + 1 = 3 ✓, pero 4 − 1 = 3, no 2."), "solution": t("No, it fails the second.", "No, falla la segunda.")},
      "p7": {"ok": "b", "hints": {"a": t("$3 is the tea.", "$3 es el té."), "c": t("$5 is one coffee and one tea together.", "$5 es un café y un té juntos.")}, "right": t("t = 5 − c, 2c + 5 − c = 7, c = 2.", "t = 5 − c, 2c + 5 − c = 7, c = 2."), "solution": "$2."},
      "p8": {"ok": "a", "hints": {"b": t("6 − 4 = 2, not 4.", "6 − 4 = 2, no 4."), "c": t("5 − 5 = 0, not 4.", "5 − 5 = 0, no 4.")}, "right": t("x + y = 10, x − y = 4: x = 7, y = 3.", "x + y = 10, x − y = 4: x = 7, y = 3."), "solution": t("7 and 3.", "7 y 3.")},
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("Check y = 2x: 2 · 6 = 12, not 3.", "Compruebe y = 2x: 2 · 6 = 12, no 3."), "c": t("Check y = 2x: 2 · 3 = 6.", "Compruebe y = 2x: 2 · 3 = 6."), "d": t("Check y = 2x: 2 · 9 = 18.", "Compruebe y = 2x: 2 · 9 = 18.")}, "solution": "(3, 6)."},
      "B": {"ok": "b", "hints": {"a": t("Check x = y + 2: 4 + 2 = 6, not 2.", "Compruebe x = y + 2: 4 + 2 = 6, no 2."), "c": t("Check x = y + 2: 4 + 2 = 6.", "Compruebe x = y + 2: 4 + 2 = 6."), "d": t("Check 2x + y = 10: 4 + 2 = 6.", "Compruebe 2x + y = 10: 4 + 2 = 6.")}, "solution": "(4, 2)."},
      "C": {"ok": "d", "hints": {"a": t("Check y = x − 1: 2 − 1 = 1, not 3.", "Compruebe y = x − 1: 2 − 1 = 1, no 3."), "b": t("Check y = x − 1: 3 − 1 = 2.", "Compruebe y = x − 1: 3 − 1 = 2."), "c": t("Check 3x − y = 7: 3 − 2 = 1.", "Compruebe 3x − y = 7: 3 − 2 = 1.")}, "solution": "(3, 2)."},
      "D": {"ok": "c", "hints": {"a": t("5 + 2 = 7: the first works.", "5 + 2 = 7: la primera se cumple."), "b": t("5 − 2 = 3: the second works.", "5 − 2 = 3: la segunda se cumple."), "d": t("Substitute in each one.", "Sustituya en cada una.")}, "solution": t("Yes, it works in both.", "Sí, cumple ambas.")},
      "E": {"ok": "a", "hints": {"b": t("Check the second: 1 + 2(3) = 7, not 8.", "Compruebe la segunda: 1 + 2(3) = 7, no 8."), "c": t("The first works: 2 + 3 = 5.", "La primera se cumple: 2 + 3 = 5."), "d": t("Check the second: 1 + 6 = 7.", "Compruebe la segunda: 1 + 6 = 7.")}, "solution": t("No, it fails the second equation.", "No, falla la segunda ecuación.")},
      "F": {"ok": "c", "hints": {"a": t("$5 is the child ticket.", "$5 es el boleto de niño."), "b": t("$15 is one adult and one child together.", "$15 es un adulto y un niño juntos."), "d": t("2a + n = 25 and a + n = 15: subtract them.", "2a + n = 25 y a + n = 15: réstelas.")}, "solution": "$10."},
      "G": {"ok": "b", "hints": {"a": t("$10 is the adult ticket.", "$10 es el boleto de adulto."), "c": t("$15 is both tickets together.", "$15 son los dos boletos juntos."), "d": t("n = 15 − a = 15 − 10.", "n = 15 − a = 15 − 10.")}, "solution": "$5."},
      "H": {"ok": "d", "hints": {"a": t("4 is the smaller number.", "4 es el número menor."), "b": t("6 + 6 = 12, but one must be double the other.", "6 + 6 = 12, pero uno debe ser el doble del otro."), "c": t("12 is the sum.", "12 es la suma.")}, "solution": "8."},
     }}

    quiz = [
     ("A", t("Solve: y = 2x ; x + y = 9.", "Resuelva: y = 2x ; x + y = 9."), [("a", "(3, 6)"), ("b", "(6, 3)"), ("c", "(3, 3)"), ("d", "(9, 0)")]),
     ("B", t("Solve: x = y + 2 ; 2x + y = 10.", "Resuelva: x = y + 2 ; 2x + y = 10."), [("a", "(2, 4)"), ("b", "(4, 2)"), ("c", "(4, 4)"), ("d", "(2, 2)")]),
     ("C", t("Solve: y = x − 1 ; 3x − y = 7.", "Resuelva: y = x − 1 ; 3x − y = 7."), [("a", "(2, 3)"), ("b", "(3, 3)"), ("c", "(1, 2)"), ("d", "(3, 2)")]),
     ("D", t("Is (5, 2) a solution of x + y = 7 and x − y = 3?", "¿Es (5, 2) solución de x + y = 7 y x − y = 3?"), [("a", t("No, it fails the first", "No, falla la primera")), ("b", t("No, it fails the second", "No, falla la segunda")), ("c", t("Yes, it works in both", "Sí, cumple ambas")), ("d", t("It works in neither", "No cumple ninguna"))]),
     ("E", t("Is (1, 3) a solution of 2x + y = 5 and x + 2y = 8?", "¿Es (1, 3) solución de 2x + y = 5 y x + 2y = 8?"), [("a", t("No, it fails the second equation", "No, falla la segunda ecuación")), ("b", t("Yes, it works in both", "Sí, cumple ambas")), ("c", t("No, it fails the first", "No, falla la primera")), ("d", t("Yes, both exactly", "Sí, ambas exactas"))]),
     ("F", t("Two adult tickets and one child ticket cost $25; one adult and one child cost $15. What is the price of the adult ticket?", "Dos boletos de adulto y uno de niño cuestan $25; un adulto y un niño cuestan $15. ¿Precio del boleto de adulto?"), [("a", "$5"), ("b", "$15"), ("c", "$10"), ("d", "$12")]),
     ("G", t("With the same system, how much does the child ticket cost?", "Con el mismo sistema anterior, ¿cuánto cuesta el boleto de niño?"), [("a", "$10"), ("b", "$5"), ("c", "$15"), ("d", "$20")]),
     ("H", t("Two numbers add up to 12 and one is double the other. Which is the bigger one?", "La suma de dos números es 12 y uno es el doble del otro. ¿Cuál es el mayor?"), [("a", "4"), ("b", "6"), ("c", "12"), ("d", "8")])]

    tarea = (t("For your own work, with your notebook open: (1) Six systems by substitution, writing the five steps: y = 2x and x + y = 9; y = x + 1 and 2x + y = 10; x + y = 8 and x − y = 2; x = 3y and 2x − y = 10; 3x + y = 7 and 2x − 3y = 1. The sixth is a price problem: at another coffee shop, 3 coffees and 2 teas cost $13, and 1 coffee and 1 tea cost $5. (2) Which variable do I solve for? In each system, decide which variable is best to solve for (the one with coefficient 1 or −1), explain why that avoids fractions, and solve it: 2x + y = 11 and 3x − 2y = 6; x − 4y = 2 and 3x + 5y = 23; 5x − y = 3 and 2x + 3y = 25; 4x + 3y = 10 and −x + 2y = 3. (3) I always check in both: check each pair in both equations. If it is not a solution, say which equation it fails and find the right solution: (2, 5) in y = x + 3 and x + y = 7; (4, 1) in x − y = 3 and 2x + y = 12; (3, −2) in x + y = 1 and 2x − y = 5. Then do several exercises of each activity on the practice page. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) Seis sistemas por sustitución, escribiendo los cinco pasos: y = 2x y x + y = 9; y = x + 1 y 2x + y = 10; x + y = 8 y x − y = 2; x = 3y y 2x − y = 10; 3x + y = 7 y 2x − 3y = 1. El sexto es un problema de precios: en otra cafetería, 3 cafés y 2 tés cuestan $13, y 1 café y 1 té cuestan $5. (2) ¿Qué variable despejo? En cada sistema, decida qué variable conviene despejar (la de coeficiente 1 o −1), explique por qué así se evitan fracciones y resuélvalo: 2x + y = 11 y 3x − 2y = 6; x − 4y = 2 y 3x + 5y = 23; 5x − y = 3 y 2x + 3y = 25; 4x + 3y = 10 y −x + 2y = 3. (3) Siempre verifico en ambas: compruebe cada par en las dos ecuaciones. Si no es solución, diga en qué ecuación falla y halle la solución correcta: (2, 5) en y = x + 3 y x + y = 7; (4, 1) en x − y = 3 y 2x + y = 12; (3, −2) en x + y = 1 y 2x − y = 5. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Look at a receipt from a store or restaurant where you bought two kinds of things. Write a system with the prices as unknowns and the receipt totals as the facts, and ask someone at home to solve it.",
               "Busque un recibo de una tienda o un restaurante donde compró dos clases de cosas. Escriba un sistema con los precios como incógnitas y los totales del recibo como datos, y pídale a alguien en casa que lo resuelva."))

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Solve a system of two linear equations by substitution: solve for one variable, substitute, solve, and check in both equations.", "Resuelva un sistema de dos ecuaciones lineales por sustitución: despeje una variable, sustituya, resuelva y verifique en las dos ecuaciones."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Explain</strong> what a system is and what its solution is.", "<strong>Explicar</strong> qué es un sistema y qué es su solución."),
         t("<strong>Solve</strong> systems by substitution with five steps.", "<strong>Resolver</strong> sistemas por sustitución con cinco pasos."),
         t("<strong>Check</strong> whether an ordered pair is a solution of a system.", "<strong>Verificar</strong> si un par ordenado es solución de un sistema."),
         t("<strong>Set up</strong> and solve word problems with two unknowns.", "<strong>Plantear</strong> y resolver problemas de contexto con dos incógnitas.")],
        secciones, tarea, quiz,
        t("Self-check checklist for substitution", "Lista de autoevaluación de la sustitución"),
        t("Self-check checklist: skills for solving systems by substitution", "Lista de autoevaluación: destrezas para resolver sistemas por sustitución"),
        [(t("Solving for a variable", "Despejar una variable"), t("I always choose the easiest variable to solve for.", "Elijo siempre la variable más fácil de despejar."), t("I solve for one, but I choose the hardest or make mistakes.", "Despejo, pero elijo la más difícil o cometo errores."), t("I cannot solve for any variable.", "No logro despejar ninguna variable.")),
         (t("Substituting without sign mistakes", "Sustituir sin errores de signo"), t("I substitute easily, even with parentheses and subtractions.", "Sustituyo con fluidez incluso con paréntesis y restas."), t("I substitute, but I make sign mistakes.", "Sustituyo, pero cometo errores de signo."), t("I do not substitute correctly.", "No sustituyo correctamente.")),
         (t("Finding both variables and checking", "Resolver ambas variables y verificar"), t("I find both values, write the ordered pair, and check it in both equations.", "Hallo los dos valores, escribo el par ordenado y lo verifico en las dos ecuaciones."), t("I find one and make a mistake with the other, or I check in only one equation.", "Hallo una y me equivoco con la otra, o verifico en una sola ecuación."), t("I find one variable or none, and I do not check.", "Obtengo una sola variable o ninguna, y no verifico."))],
        t("<p>In this lesson you solved systems of two equations by substitution, with a five-step method, and checked each solution in both equations. You also set up word problems with two unknowns.</p>\n<p>In <strong>Lesson 6.2 · Solving systems by elimination and classifying systems</strong> you will learn another method (adding the equations to eliminate a variable) and how to classify systems as independent (one solution), inconsistent (none), or dependent (infinitely many).</p>",
          "<p>En esta lección se resolvieron sistemas de dos ecuaciones por sustitución, con un procedimiento de cinco pasos, y se verificó cada solución en las dos ecuaciones. También se plantearon problemas de contexto con dos incógnitas.</p>\n<p>En la <strong>Lección 6.2 · Resolver sistemas por eliminación y clasificar sistemas</strong> se aprenderá otro método (sumar las ecuaciones para eliminar una variable) y a clasificar los sistemas en independiente (una solución), inconsistente (ninguna) o dependiente (infinitas).</p>"),
        ("6-2", ("", t("Lesson 6.2 · Solving systems by elimination and classifying systems", "Lección 6.2 · Resolver sistemas por eliminación y clasificar sistemas"))),
        [(t("system of equations", "sistema de ecuaciones"), t("Two equations with the same two variables.", "Dos ecuaciones con las mismas dos variables.")),
         (t("solution of a system", "solución de un sistema"), t("The ordered pair (x, y) that makes both equations true; on the graph, the crossing point.", "El par ordenado (x, y) que hace verdaderas las dos ecuaciones; en la gráfica, el punto de cruce.")),
         (t("substitution", "sustitución"), t("Solving one equation for a variable and putting that expression into the other equation.", "Despejar una variable en una ecuación y poner esa expresión en la otra.")),
         (t("ordered pair", "par ordenado"), t("(x, y): the x value always first.", "(x, y): siempre primero el valor de x."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function exprCF(p, q, v){ if (!q) return exprTxt(p, 0, v); return sg(q) + (p < 0 ? " − " : " + ") + terminoXY(Math.abs(p), v, true); }
function exprTxt(p, q, v){ var s = terminoXY(p, v, true); if (q) s += s ? (q < 0 ? " − " + -q : " + " + q) : sg(q); return s || "0"; }
function nuevoSis(){ var x0 = nz(-6, 6), y0 = aleatorio(-6, 6), f1 = elige(["y", "y", "x", "uno"]); var S = sisCon(x0, y0, {f1: f1, f2: "std", lim: 4}); return {L1: S[0], L2: S[1], x: x0, y: y0}; }
/* Substitution steps for a system where L1 has a coefficient 1 or −1 */
function pasosSust(c){
  var L1 = c.L1, L2 = c.L2, P = [], despY = Math.abs(L1.b) === 1 && (L1.vis ? /^y/.test(L1.vis) : true) || Math.abs(L1.a) !== 1;
  var p, q, ot, v, w;
  if (despY){ p = -L1.a / L1.b; q = L1.c / L1.b; v = "y"; w = "x"; } else { p = -L1.b / L1.a; q = L1.c / L1.a; v = "x"; w = "y"; }
  var expr = exprTxt(p, q, w);
  P.push(L1.vis ? T("The first equation already has " + v + " alone: ", "La primera ecuación ya tiene " + v + " despejada: ") + v + " = " + expr + "." : T("Solve the first equation for " + v + ": ", "Se despeja " + v + " en la primera ecuación: ") + v + " = " + expr + ".");
  var kw = despY ? L2.a : L2.b, kv = despY ? L2.b : L2.a;
  var sustit = (despY ? terminoXY(kw, w, true) + (kv < 0 ? " − " : " + ") + (Math.abs(kv) === 1 ? "" : Math.abs(kv)) + "(" + expr + ")" : (kv === 1 ? "" : kv === -1 ? "−" : sg(kv)) + "(" + expr + ")" + terminoXY(kw, w, false)) + " = " + sg(L2.c);
  P.push(T("Substitute it into the other equation: ", "Se sustituye en la otra ecuación: ") + sustit + ".");
  var A = kw + kv * p, Bc = kv * q, val = (L2.c - Bc) / A;
  P.push(T("Solve: ", "Se resuelve: ") + terminoXY(A, w, true) + (Bc ? (Bc < 0 ? " − " + -Bc : " + " + Bc) : "") + " = " + sg(L2.c) + (Bc ? ", " + terminoXY(A, w, true) + " = " + sg(L2.c - Bc) : "") + ", " + w + " = " + sg(val) + ".");
  var otro = p * val + q;
  P.push(T("Find ", "Se halla ") + v + ": " + v + " = " + (p ? (p === 1 ? "" : p === -1 ? "−" : p) + "(" + sg(val) + ")" + (q ? (q < 0 ? " − " + -q : " + " + q) : "") : sg(q)) + " = " + sg(otro) + ".");
  P.push(T("Check in both equations: ", "Se verifica en las dos ecuaciones: ") + sustTxt(L1, c.x, c.y) + " ✓; " + sustTxt(L2, c.x, c.y) + " ✓.");
  P.push(T("Solution: ", "Solución: ") + "<strong>" + par(c.x, c.y) + "</strong>. " + T("On the graph, it is the point where the two lines cross.", "En la gráfica es el punto donde se cruzan las dos rectas."));
  return P;
}
var SU = null;
pasoAPaso4("su", function(){ SU = nuevoSis(); return {enun: T("Solve the system ", "Resuelva el sistema ") + sisHTML(SU.L1, SU.L2) + ".", pasos: pasosSust(SU), inicio: function(){ $("su-graf").innerHTML = '<p class="nota">' + T("The graph appears when you reach the check.", "La gráfica aparece al llegar a la verificación.") + "</p>"; }, fin: function(){ $("su-graf").innerHTML = grafSis(SU.L1, SU.L2); }}; });
creaPracticaPar("sq", function(){ var c = nuevoSis();
  return {enun: T("Solve by substitution: ", "Resuelva por sustitución: ") + sisHTML(c.L1, c.L2), x: c.x, y: c.y, diag: diagSis(c.L1, c.L2, c), solucion: pasosSust(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 2 · Checking an ordered pair ===== */
var VE = null;
function veNuevo(){ VE = nuevoSis(); $("ve-sis").innerHTML = sisHTML(VE.L1, VE.L2); $("ve-x").value = ""; $("ve-y").value = ""; $("ve-txt").innerHTML = ""; $("ve-graf").innerHTML = grafSis(VE.L1, VE.L2, {sinPunto: true}); }
$("ve-ver").addEventListener("click", function(){
  var x = leeDecimal($("ve-x").value), y = leeDecimal($("ve-y").value);
  if (x === null || y === null){ $("ve-txt").innerHTML = '<div class="linea">' + T("Type a number in each box.", "Escriba un número en cada casilla.") + "</div>"; return; }
  var c1 = cumple(VE.L1, x, y), c2 = cumple(VE.L2, x, y), ok = '<strong style="color:#2e7d32">✓</strong>', no = '<strong style="color:#c62828">✗</strong>';
  $("ve-txt").innerHTML = '<div class="linea">' + T("First: ", "Primera: ") + sustTxt(VE.L1, x, y) + (c1 ? " = " + sg(VE.L1.c) + " " + ok : T(", not ", ", no ") + sg(VE.L1.c) + " " + no) + "</div>" +
    '<div class="linea">' + T("Second: ", "Segunda: ") + sustTxt(VE.L2, x, y) + (c2 ? " = " + sg(VE.L2.c) + " " + ok : T(", not ", ", no ") + sg(VE.L2.c) + " " + no) + "</div>" +
    '<div class="linea"><strong>' + (c1 && c2 ? T("It works in both: " + par(x, y) + " is the solution. It is where the lines cross.", "Cumple las dos: " + par(x, y) + " es la solución. Es donde se cruzan las rectas.") : c1 || c2 ? T("It works in only one: the point is on one line but not on the other. It is not the solution.", "Cumple solo una: el punto está sobre una recta pero no sobre la otra. No es la solución.") : T("It works in neither: the point is on neither line.", "No cumple ninguna: el punto no está en ninguna de las dos rectas.")) + "</strong></div>";
  $("ve-graf").innerHTML = grafSis(VE.L1, VE.L2, {sinPunto: !(c1 && c2), punto: c1 && c2 ? null : [x, y]});
});
$("ve-otro").addEventListener("click", veNuevo); veNuevo();
OMR("vq", function(){ var c = nuevoSis(), tipo = elige(["ambas", "primera", "segunda", "ninguna"]), x = c.x, y = c.y, k = 0;
  if (tipo !== "ambas"){ do { if (tipo === "primera"){ var t = nz(-3, 3); if (c.L1.b){ x = c.x + t * c.L1.b; y = c.y - t * c.L1.a; } } else if (tipo === "segunda"){ var u = nz(-3, 3); x = c.x + u * c.L2.b; y = c.y - u * c.L2.a; } else { x = c.x + nz(-3, 3); y = c.y + nz(-3, 3); } k++; } while (((cumple(c.L1, x, y) ? 1 : 0) + (cumple(c.L2, x, y) ? 2 : 0)) !== {ambas: 3, primera: 1, segunda: 2, ninguna: 0}[tipo] && k < 50); }
  var r = (cumple(c.L1, x, y) ? 1 : 0) + (cumple(c.L2, x, y) ? 2 : 0), ok = ["ninguna", "primera", "segunda", "ambas"][r];
  return {enun: T("Is ", "¿Es ") + par(x, y) + T(" a solution of ", " solución de ") + sisHTML(c.L1, c.L2) + "?", correcta: ok, enOrden: true,
    opciones: [{clave: "ambas", html: T("Yes, it works in both", "Sí, cumple ambas")}, {clave: "primera", html: T("No: it works only in the first", "No: solo cumple la primera")}, {clave: "segunda", html: T("No: it works only in the second", "No: solo cumple la segunda")}, {clave: "ninguna", html: T("No: it works in neither", "No: no cumple ninguna")}],
    pista: T("Substitute the pair in each equation, with parentheses.", "Sustituya el par en cada ecuación, con paréntesis."), bien: T("First: ", "Primera: ") + sustTxt(c.L1, x, y) + (r & 1 ? " ✓" : T(" (should be ", " (debería dar ") + sg(c.L1.c) + ")") + ". " + T("Second: ", "Segunda: ") + sustTxt(c.L2, x, y) + (r & 2 ? " ✓" : T(" (should be ", " (debería dar ") + sg(c.L2.c) + ")") + "."};
});

/* ===== MODULE 3 · Setting up word problems ===== */
var ART = [
  {n: [T("coffee", "café"), T("tea", "té")], un: [T("one coffee", "un café"), T("one tea", "un té")], v: ["c", "t"], intro: T("At a coffee shop", "En una cafetería"), pl: [T("coffees", "cafés"), T("teas", "tés")], p: [2, 3]},
  {n: [T("empanada", "empanada"), T("soda", "refresco")], un: [T("one empanada", "una empanada"), T("one soda", "un refresco")], v: ["e", "r"], intro: T("At a food stand", "En un puesto de comida"), pl: [T("empanadas", "empanadas"), T("sodas", "refrescos")], p: [2, 3]},
  {n: [T("adult ticket", "entrada de adulto"), T("child ticket", "entrada de niño")], un: [T("one adult ticket", "una entrada de adulto"), T("one child ticket", "una entrada de niño")], v: ["a", "n"], intro: T("At the movies", "En el cine"), pl: [T("adult tickets", "entradas de adulto"), T("child tickets", "entradas de niño")], p: [8, 5]},
  {n: [T("notebook", "cuaderno"), T("pen", "pluma")], un: [T("one notebook", "un cuaderno"), T("one pen", "una pluma")], v: ["c", "p"], intro: T("At a store", "En una papelería"), pl: [T("notebooks", "cuadernos"), T("pens", "plumas")], p: [3, 1]}];
function casoPrecio(fijo){
  var it = fijo !== undefined ? ART[fijo] : elige(ART), p1 = fijo !== undefined ? it.p[0] : aleatorio(2, 9), p2 = fijo !== undefined ? it.p[1] : aleatorio(1, 8), k1, k2, j1, j2;
  if (fijo !== undefined){ k1 = [2, 3, 2, 3][fijo]; k2 = [1, 2, 3, 2][fijo]; j1 = 1; j2 = [1, 2, 1, 1][fijo]; }
  else { do { k1 = aleatorio(1, 4); k2 = aleatorio(1, 4); j1 = 1; j2 = elige([1, 1, 2]); p2 = aleatorio(1, 8); } while (k1 * j2 === k2 * j1 || p1 === p2); }
  var L1 = L3(k1, k2, k1 * p1 + k2 * p2), L2 = L3(j1, j2, j1 * p1 + j2 * p2), cnt = function(k, i){ return k + " " + (k === 1 ? it.n[i] : it.pl[i]); };
  var txt = it.intro + ", " + cnt(k1, 0) + T(" and ", " y ") + cnt(k2, 1) + T(" cost $", " cuestan $") + L1.c + "; " + cnt(j1, 0) + T(" and ", " y ") + cnt(j2, 1) + T(" cost $", " cuestan $") + L2.c + ".";
  return {it: it, p1: p1, p2: p2, L1: L1, L2: L2, txt: txt};
}
function pasosPrecio(c){ var v = c.it.v, L2 = c.L2, L1 = c.L1;
  var expr = exprCF(-L2.b, L2.c, v[1]);
  return [T("Name the unknowns: let ", "Nombrar las incógnitas: sea ") + "<strong>" + v[0] + "</strong>" + T(" be the price of ", " el precio de ") + c.it.un[0] + T(" and ", " y ") + "<strong>" + v[1] + "</strong>" + T(" the price of ", " el de ") + c.it.un[1] + T(", in dollars.", ", en dólares."),
    T("First fact: ", "Primer dato: ") + "<strong>" + ecTxt(L1, v[0], v[1]) + "</strong>.", T("Second fact: ", "Segundo dato: ") + "<strong>" + ecTxt(L2, v[0], v[1]) + "</strong>.",
    T("Solve the second for ", "Se despeja ") + v[0] + T(": ", " en la segunda: ") + v[0] + " = " + expr + ".",
    T("Substitute: ", "Se sustituye: ") + (L1.a === 1 ? "" : L1.a) + "(" + expr + ") + " + terminoXY(L1.b, v[1], true) + " = " + L1.c + " → <strong>" + v[1] + " = " + c.p2 + "</strong>; " + v[0] + " = " + sg(L2.c) + " − " + (L2.b === 1 ? "" : L2.b) + "(" + c.p2 + ")" + " = <strong>" + c.p1 + "</strong>.",
    T("Reread the question: ", "Releer la pregunta: ") + c.it.un[0] + T(" costs ", " cuesta ") + "<strong>$" + c.p1 + "</strong>" + T(" and ", " y ") + c.it.un[1] + ", <strong>$" + c.p2 + "</strong>. " + T("Check: ", "Comprobación: ") + sustTxt(L1, c.p1, c.p2) + " ✓."]; }
function pasosNumeros(s, d){ var x = (s + d) / 2, y = (s - d) / 2; return [T("Name: let x be the bigger number and y the smaller.", "Nombrar: sean x el número mayor e y el menor."), T("“Their sum is " + s + "” → ", "«Su suma es " + s + "» → ") + "<strong>x + y = " + s + "</strong>.", T("“Their difference is " + d + "” → ", "«Su diferencia es " + d + "» → ") + "<strong>x − y = " + d + "</strong>.", T("Solve the second for x: x = y + " + d + ".", "Se despeja x en la segunda: x = y + " + d + "."), T("Substitute: (y + " + d + ") + y = " + s + ", so 2y = " + (s - d) + ", <strong>y = " + y + "</strong>, and x = <strong>" + x + "</strong>.", "Se sustituye: (y + " + d + ") + y = " + s + ", así que 2y = " + (s - d) + ", <strong>y = " + y + "</strong>, y x = <strong>" + x + "</strong>."), T("Reread: the numbers are <strong>" + x + " and " + y + "</strong>. Check: " + x + " + " + y + " = " + s + " ✓ and " + x + " − " + y + " = " + d + " ✓.", "Releer: los números son <strong>" + x + " y " + y + "</strong>. Comprobación: " + x + " + " + y + " = " + s + " ✓ y " + x + " − " + y + " = " + d + " ✓.")]; }
function pasosPerimetro(P2, d){ var A = (P2 / 2 - d) / 2, L = A + d; return [T("Name: let L be the length and W the width, in feet.", "Nombrar: sea L el largo y A el ancho, en pies."), T("The perimeter of a rectangle is 2L + 2W → <strong>2L + 2W = " + P2 + "</strong>; divide by 2: L + W = " + P2 / 2 + ".", "El perímetro de un rectángulo es 2L + 2A → <strong>2L + 2A = " + P2 + "</strong>; se divide entre 2: L + A = " + P2 / 2 + "."), T("“The length is " + d + " feet more than the width” → <strong>L = W + " + d + "</strong>. It is already solved for L.", "«El largo mide " + d + " pies más que el ancho» → <strong>L = A + " + d + "</strong>. Ya viene despejado."), T("Substitute: (W + " + d + ") + W = " + P2 / 2 + ".", "Se sustituye: (A + " + d + ") + A = " + P2 / 2 + "."), T("Solve: 2W = " + (P2 / 2 - d) + ", <strong>W = " + A + "</strong>, and L = <strong>" + L + "</strong>.", "Se resuelve: 2A = " + (P2 / 2 - d) + ", <strong>A = " + A + "</strong>, y L = <strong>" + L + "</strong>."), T("Reread: the length is <strong>" + L + " ft</strong> and the width, <strong>" + A + " ft</strong>. Check: 2(" + L + ") + 2(" + A + ") = " + P2 + " ✓.", "Releer: el largo mide <strong>" + L + " pies</strong> y el ancho, <strong>" + A + " pies</strong>. Comprobación: 2(" + L + ") + 2(" + A + ") = " + P2 + " ✓.")]; }
var CASOS_CT = [function(){ var c = casoPrecio(0); return {enun: c.txt + T(" How much does each one cost?", " ¿Cuánto cuesta cada uno?"), pasos: pasosPrecio(c)}; },
  function(){ var c = casoPrecio(1); return {enun: c.txt + T(" How much does each thing cost?", " ¿Cuánto cuesta cada cosa?"), pasos: pasosPrecio(c)}; },
  function(){ var c = casoPrecio(2); return {enun: c.txt + T(" How much is each ticket?", " ¿Cuánto vale cada entrada?"), pasos: pasosPrecio(c)}; },
  function(){ return {enun: T("Two numbers add up to 20 and their difference is 4. What are they?", "La suma de dos números es 20 y su diferencia es 4. ¿Cuáles son?"), pasos: pasosNumeros(20, 4)}; },
  function(){ return {enun: T("A rectangular yard has a perimeter of 26 feet. The length is 3 feet more than the width. How long is each side?", "Un terreno rectangular tiene 26 pies de perímetro. El largo mide 3 pies más que el ancho. ¿Cuánto mide cada lado?"), pasos: pasosPerimetro(26, 3)}; }];
pasoAPaso4("ct", function(){ return CASOS_CT[+$("ct-ex").value](); });
$("ct-ex").addEventListener("change", function(){ $("ct-nuevo").click(); });
OMR("cq", function(){
  if (Math.random() < .3){ var y = aleatorio(1, 12), x = y + aleatorio(1, 10), s = x + y, d = x - y, preg = Math.random() < .5;
    return {enun: T("Two numbers add up to " + s + " and their difference is " + d + ". ", "Dos números suman " + s + " y su diferencia es " + d + ". ") + (preg ? T("What is the bigger one?", "¿Cuál es el mayor?") : T("What is the smaller one?", "¿Cuál es el menor?")), correcta: "ok",
      opciones: racOpcionesNum([preg ? x : y, preg ? y : x, s, d, s / 2]), pista: T("x + y = " + s + " and x − y = " + d + ". Add or substitute.", "x + y = " + s + " y x − y = " + d + ". Sume o sustituya."), bien: pasosNumeros(s, d).slice(-2).join(" ").replace(/<\/?strong>/g, "")}; }
  var c = casoPrecio(), q = Math.random() < .5 ? 0 : 1, val = q ? c.p2 : c.p1, otro = q ? c.p1 : c.p2;
  return {enun: c.txt + T(" How much does ", " ¿Cuánto cuesta ") + c.it.un[q] + T(" cost?", "?"), correcta: "ok", opciones: racOpcionesNum([val, otro, c.L2.c, Math.abs(c.L1.c - c.L2.c)], "$"),
    pista: T("Write the two equations, solve one for a variable, and substitute.", "Escriba las dos ecuaciones, despeje una variable y sustituya."), bien: pasosPrecio(c).slice(1).join(" ").replace(/<\/?strong>/g, "")};
});
function racOpcionesNum(l, pre){ var vis = {}, ops = []; l.forEach(function(v, i){ var h = (pre || "") + sg(v); if (!vis[h] && v > 0 && ops.length < 4){ vis[h] = 1; ops.push({clave: i ? "m" + i : "ok", html: h}); } }); return ops; }
'''

def practica_pagina():
    n = N
    ctx = [("0", t("Coffee and tea", "Cafés y tés")), ("1", t("Empanadas and sodas", "Empanadas y refrescos")), ("2", t("Adult and child tickets", "Entradas de adulto y de niño")), ("3", t("Two numbers", "Dos números")), ("4", t("The perimeter of a yard", "El perímetro del terreno"))]
    campo = lambda i, et: f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{i}" style="width:6em"></div>'
    mods = [
     (t("substitution", "sustitucion"), t("The five steps of substitution", "Los cinco pasos de la sustitución"),
      f'''      <p>{t("1. Solve one equation for one variable. 2. Substitute that expression into the other. 3. Solve the equation with one variable. 4. Substitute that value to find the other variable. 5. Check in both equations.", "1. Despejar una variable en una de las ecuaciones. 2. Sustituir esa expresión en la otra. 3. Resolver la ecuación de una variable. 4. Sustituir ese valor para hallar la otra variable. 5. Verificar en las dos ecuaciones.")}</p>
{n4.pasos("su", t("Another system", "Otro sistema"))}
      <div id="su-graf"></div>
      <div class="caja-tip">{t("Solve for the variable whose coefficient is 1 or −1, to avoid fractions, and use parentheses when you substitute.", "Despeje la variable de coeficiente 1 o −1, para evitar fracciones, y use paréntesis al sustituir.")}</div>
{n4.par_libre("sq", t("Practice: solve by substitution", "Practique: resuelva por sustitución"))}'''),
     (t("check", "verificar"), t("Checking an ordered pair", "Verificar un par ordenado"),
      f'''      <p>{t("Type any pair (x, y). It is substituted in both equations and placed on the graph. Only the crossing point works in both.", "Escriba cualquier par (x, y). Se sustituye en las dos ecuaciones y se sitúa en la gráfica. Solo el punto de cruce cumple las dos.")}</p>
      <div class="panel"><p class="enun" id="ve-sis"></p><div class="campos">{campo("ve-x", "x =")}{campo("ve-y", "y =")}</div>
        <div class="fila-btn"><button type="button" class="btn" id="ve-ver">{t("Check the pair", "Verificar el par")}</button><button type="button" class="btn-sec" id="ve-otro">{t("Another system", "Otro sistema")}</button></div></div>
{n4.salida("ve-txt")}
      <div id="ve-graf"></div>
{B.om("vq", t("Practice: is it a solution?", "Practique: ¿es solución?"))}'''),
     (t("context", "contexto"), t("Setting up word problems", "Plantear problemas de contexto"),
      f'''      <p>{t("Name the unknowns, turn each fact into an equation, solve the system, and reread the question to answer what it asks.", "Nombre las incógnitas, traduzca cada dato en una ecuación, resuelva el sistema y relea la pregunta para responder lo que pide.")}</p>
      <div class="panel"><div class="campos">{n4.lista("ct-ex", t("Situation", "Situación"), ctx)}</div></div>
{n4.pasos("ct", t("Start again", "Empezar de nuevo"))}
{B.om("cq", t("Practice: solve the situation", "Practique: resuelva la situación"))}''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver sistemas de ecuaciones por sustitución")
