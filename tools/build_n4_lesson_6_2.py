"""Level 4 · Lesson 6.2 · Solving systems by elimination and classifying systems — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_6-2.html and algebra/n4-l6-2.html (elimination step by step, classifying systems with
their graph, choosing the method, and coins, tickets, mixtures, a boat, and ages). They are rebuilt here, inside LearnGED, with
math/sys4.js. US units and coins. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4
from build_n4_lesson_6_1 import ESTILO_SIS

B.NIVEL = 4
N = "6-2"
TEMA = ("Systems of linear equations", "Sistemas de ecuaciones lineales")
TIT = ("Solving systems by elimination and classifying systems", "Resolver sistemas por eliminación y clasificar sistemas")
SCRIPTS = n4.SCRIPTS + ("/math/sys4.js",)
ESTILO = n4.ESTILO + ESTILO_SIS

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 6.1.</strong> In Lesson 6.1 you solved systems by substitution. Substitution is ideal when a variable is already alone; but when both equations are in the form ax + by = c, the <strong>elimination</strong> method is usually faster: add the equations so that one variable disappears.", "<strong>Conexión con la lección anterior.</strong> En la Lección 6.1 se resolvieron sistemas por sustitución. La sustitución es ideal cuando una variable ya está despejada; pero cuando las dos ecuaciones están en la forma ax + by = c, suele ser más rápido el método de <strong>eliminación</strong>: sumar las ecuaciones para que una variable desaparezca.")}</p>
<p>{t("The idea is to make the coefficients of one variable opposites (for example, +y and −y), so that when you add the equations that variable is eliminated. Sometimes they are already opposites; other times you multiply one or both equations first.", "La idea es lograr que los coeficientes de una variable sean opuestos (por ejemplo, +y y −y) para que, al sumar las ecuaciones, esa variable se elimine. A veces ya están opuestos; otras veces hay que multiplicar una o ambas ecuaciones.")}</p>
{ejemplo(t("Example 1: coefficients already opposite. Solve x + y = 10 and x − y = 4.", "Ejemplo 1 · Coeficientes ya opuestos. Resolver x + y = 10 y x − y = 4."),
  [("1", t("Add the two equations:", "Se suman las dos ecuaciones:"), "(x + y) + (x − y) = 10 + 4."), ("2", t("The y disappears:", "La y se elimina:"), t("2x = 14, so x = 7.", "2x = 14, así que x = 7.")), ("3", t("Find y:", "Se halla y:"), "7 + y = 10, y = 3."), ("✓", t("Solution.", "Solución."), "<strong>(7, 3)</strong>.")])}
{ejemplo(t("Example 2: multiply one equation. Solve 2x + 3y = 13 and x − y = −1.", "Ejemplo 2 · Multiplicar una ecuación. Resolver 2x + 3y = 13 y x − y = −1."),
  [("1", t("Multiply the second by 3:", "Se multiplica la segunda por 3:"), "3x − 3y = −3."), ("2", t("Add it to the first:", "Se suma a la primera:"), "(2x + 3y) + (3x − 3y) = 13 + (−3)."), ("3", t("The y disappears:", "Se elimina la y:"), "5x = 10, x = 2."), ("4", t("Find y:", "Se halla y:"), "2 − y = −1, y = 3."), ("✓", t("Solution.", "Solución."), "<strong>(2, 3)</strong>.")])}
{ejemplo(t("Example 3: multiply both. Solve 2x + 3y = 7 and 3x + 2y = 8.", "Ejemplo 3 · Multiplicar ambas. Resolver 2x + 3y = 7 y 3x + 2y = 8."),
  [("1", t("To eliminate x: the first times 3 and the second times −2:", "Para eliminar x: la primera por 3 y la segunda por −2:"), "6x + 9y = 21; −6x − 4y = −16."), ("2", t("Add:", "Se suman:"), "5y = 5, y = 1."), ("3", t("Find x:", "Se halla x:"), "2x + 3(1) = 7, x = 2."), ("✓", t("Solution.", "Solución."), "<strong>(2, 1)</strong>.")])}
{practica("p1", t("Practice 1 — x + y = 8 ; x − y = 2", "Práctica 1 — x + y = 8 ; x − y = 2"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(5, 3)"), ("b", "(3, 5)"), ("c", "(5, 5)")])}
{practica("p2", t("Practice 2 — 2x + y = 7 ; x − y = 2", "Práctica 2 — 2x + y = 7 ; x − y = 2"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(1, 3)"), ("b", "(3, 1)"), ("c", "(3, 3)")])}
{practica("p3", t("Practice 3 — 3x + 2y = 12 ; x − 2y = −4", "Práctica 3 — 3x + 2y = 12 ; x − 2y = −4"), t("Choose the solution (x, y).", "Seleccione la solución (x, y)."), [("a", "(3, 2)"), ("b", "(2, 2)"), ("c", "(2, 3)")])}
{enlace(n, t("elimination", "eliminacion"), t("elimination", "la eliminación"), t("Systems step by step: coefficients already opposite, multiplying one equation, and multiplying both.", "Sistemas paso a paso: coeficientes ya opuestos, multiplicar una ecuación y multiplicar las dos."))}'''

    s2 = f'''<p>{t("Not every system has exactly one solution. Depending on the two lines, there are three kinds:", "No todos los sistemas tienen exactamente una solución. Según cómo sean las dos rectas, hay tres tipos:")}</p>
{tabla(t("Kinds of systems", "Tipos de sistemas"), t("How systems are classified by the number of solutions", "Clasificación de sistemas según el número de soluciones"), [t("Kind", "Tipo"), t("Lines", "Rectas"), t("Solutions", "Soluciones"), t("When you solve, you get…", "Al resolver aparece…")],
  [[t("Independent", "Independiente"), t("Cross at one point", "Se cruzan en un punto"), t("One solution", "Una solución"), "x = … , y = …"], [t("Inconsistent", "Inconsistente"), t("Parallel", "Paralelas"), t("None", "Ninguna"), t("Something false (like 0 = 5)", "Algo falso (p. ej. 0 = 5)")], [t("Dependent", "Dependiente"), t("The same line", "La misma recta"), t("Infinitely many", "Infinitas"), t("Something always true (0 = 0)", "Algo siempre cierto (0 = 0)")]])}
{caja("tip", t("The result tells you the kind", "El resultado avisa del tipo"), t("<p>If both variables disappear and a false statement is left (like 0 = 5), the system is inconsistent; if a statement that is always true is left (0 = 0), it is dependent.</p>", "<p>Si al eliminar las dos variables queda una igualdad falsa (como 0 = 5), el sistema es inconsistente; si queda una igualdad siempre cierta (0 = 0), es dependiente.</p>"))}
{practica("p4", t("Practice 4 — 0 = 5", "Práctica 4 — 0 = 5"), t("When you solve, you get 0 = 5. What kind of system is it?", "Al resolver, se obtiene 0 = 5. ¿Qué tipo es?"), [("a", t("Inconsistent (no solution)", "Inconsistente (sin solución)")), ("b", t("Dependent", "Dependiente")), ("c", t("Independent", "Independiente"))])}
{practica("p5", t("Practice 5 — 0 = 0", "Práctica 5 — 0 = 0"), t("When you solve, you get 0 = 0. What kind of system is it?", "Al resolver, se obtiene 0 = 0. ¿Qué tipo es?"), [("a", t("Inconsistent", "Inconsistente")), ("b", t("Independent", "Independiente")), ("c", t("Dependent (infinitely many solutions)", "Dependiente (infinitas soluciones)"))])}
{practica("p6", t("Practice 6 — x = 3, y = 1", "Práctica 6 — x = 3, y = 1"), t("When you solve, you get x = 3, y = 1. What kind of system is it?", "Al resolver, se obtiene x = 3, y = 1. ¿Qué tipo es?"), [("a", t("Inconsistent", "Inconsistente")), ("b", t("Independent (one solution)", "Independiente (una solución)")), ("c", t("Dependent", "Dependiente"))])}
{enlace(n, t("classify", "clasificar"), t("classifying systems", "la clasificación"), t("Choose a system and compare at the same time what you get when you solve it and how the lines look: crossing, parallel, or on top of each other.", "Elija un sistema y compare a la vez lo que sale al resolverlo y cómo quedan las rectas: cruzadas, paralelas o superpuestas."))}'''

    s3 = f'''<p>{t("Both methods lead to the same solution; what matters is choosing the faster one for each system.", "Ambos métodos llevan a la misma solución; lo importante es elegir el más rápido para cada sistema.")}</p>
{tabla(t("Substitution or elimination?", "¿Sustitución o eliminación?"), t("When substitution is best and when elimination is best", "Cuándo conviene usar sustitución y cuándo eliminación"), [t("Best method", "Conviene…"), t("When", "Cuándo")],
  [[t("Substitution", "Sustitución"), t("When a variable is already alone or has a coefficient of 1 or −1.", "Cuando una variable ya está despejada o tiene coeficiente 1 o −1.")], [t("Elimination", "Eliminación"), t("When both equations are in the form ax + by = c and the coefficients line up easily.", "Cuando las dos ecuaciones están en la forma ax + by = c y los coeficientes se alinean fácilmente.")]])}
{enlace(n, t("method", "metodo"), t("choosing the method", "la elección del método"), t("Systems to decide whether substitution or elimination is best, with the sign that gives it away in each case.", "Sistemas para decidir si conviene sustitución o eliminación, con la señal que lo delata en cada caso."))}'''

    s4 = f'''{ejemplo(t("Example 4: coins. There are 12 coins, some nickels (5¢) and some dimes (10¢), worth 95¢ in all. How many of each are there?", "Ejemplo 4 · Monedas. Hay 12 monedas, unas de 5¢ y otras de 10¢, que suman 95¢. ¿Cuántas hay de cada una?"),
  [("1", t("Let n be the number of nickels and d the number of dimes:", "Sea n el número de monedas de 5¢ y d el de 10¢:"), t("n + d = 12 and 5n + 10d = 95.", "n + d = 12 y 5n + 10d = 95.")), ("2", t("Divide the second by 5:", "Se divide la segunda entre 5:"), "n + 2d = 19."), ("3", t("Subtract the first:", "Se resta la primera:"), t("d = 7. Then n = 5.", "d = 7. Entonces n = 5.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>5 nickels and 7 dimes.</strong>", "<strong>5 monedas de 5¢ y 7 de 10¢.</strong>"))])}
{caja("tip", t("Two kinds of equations", "Dos clases de ecuaciones"), t("<p>In coin, ticket, and mixture problems there is almost always an equation of <strong>amount</strong> (how many in all) and one of <strong>value</strong> (how much money in all).</p>", "<p>En los problemas de monedas, boletos y mezclas casi siempre hay una ecuación de <strong>cantidad</strong> (cuántos hay en total) y otra de <strong>valor</strong> (cuánto dinero hay en total).</p>"))}
{practica("p7", t("Practice 7 — The dimes", "Práctica 7 — Las de 10¢"), t("With the example (12 nickels and dimes worth 95¢), how many are dimes?", "Con el ejemplo (12 monedas de 5¢ y 10¢ que suman 95¢), ¿cuántas son de 10¢?"), [("a", "7"), ("b", "5"), ("c", "12")])}
{practica("p8", t("Practice 8 — Two numbers", "Práctica 8 — Dos números"), t("Two numbers add up to 20 and their difference is 6. What is the bigger one?", "Dos números suman 20 y su diferencia es 6. ¿Cuál es el mayor?"), [("a", "7"), ("b", "13"), ("c", "10")])}
{enlace(n, t("applications", "aplicacion"), t("the applications", "las aplicaciones"), t("Situations set up step by step: coins, tickets, a coffee mixture, a boat and the current, and ages.", "Situaciones armadas paso a paso: monedas, boletos, mezcla de café, el bote con corriente y un problema de edades."))}'''

    secciones = [("s-" + t("elimination", "eliminacion"), t("The elimination method", "El método de eliminación"), s1),
                 ("s-" + t("classify", "clasificar"), t("Classifying systems", "Clasificar los sistemas"), s2),
                 ("s-" + t("method", "metodo"), t("Substitution or elimination?", "¿Sustitución o eliminación?"), s3),
                 ("s-" + t("applications", "aplicacion"), t("Application: mixtures, coins, and speeds", "Aplicación: mezclas, monedas y velocidades"), s4)]

    lesson = {"next": t("Lesson 6.3", "Lección 6.3"), "review": t("sections 1 and 2", "las secciones 1 y 2"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Write x first: x is the bigger one, since x − y = 2.", "Escriba primero x: x es el mayor, porque x − y = 2."), "c": t("5 − 5 = 0, not 2.", "5 − 5 = 0, no 2.")}, "right": t("2x = 10, x = 5, y = 3.", "2x = 10, x = 5, y = 3."), "solution": "(5, 3)."},
      "p2": {"ok": "b", "hints": {"a": t("Write x first: 3x = 9.", "Escriba primero x: 3x = 9."), "c": t("3 − 3 = 0, not 2.", "3 − 3 = 0, no 2.")}, "right": t("Add: 3x = 9, x = 3, y = 1.", "Se suman: 3x = 9, x = 3, y = 1."), "solution": "(3, 1)."},
      "p3": {"ok": "c", "hints": {"a": t("Write x first: 4x = 8.", "Escriba primero x: 4x = 8."), "b": t("Check 3x + 2y = 12: 6 + 4 = 10.", "Compruebe 3x + 2y = 12: 6 + 4 = 10.")}, "right": t("Add: 4x = 8, x = 2, y = 3.", "Se suman: 4x = 8, x = 2, y = 3."), "solution": "(2, 3)."},
      "p4": {"ok": "a", "hints": {"b": t("Dependent gives something always true, like 0 = 0.", "Dependiente da algo siempre cierto, como 0 = 0."), "c": t("Independent gives values of x and y.", "Independiente da valores de x e y.")}, "right": t("0 = 5 is false: parallel lines.", "0 = 5 es falso: rectas paralelas."), "solution": t("Inconsistent.", "Inconsistente.")},
      "p5": {"ok": "c", "hints": {"a": t("Inconsistent gives something false.", "Inconsistente da algo falso."), "b": t("Independent gives values of x and y.", "Independiente da valores de x e y.")}, "right": t("0 = 0 is always true: the same line.", "0 = 0 siempre es cierto: la misma recta."), "solution": t("Dependent.", "Dependiente.")},
      "p6": {"ok": "b", "hints": {"a": t("There is a solution: x = 3, y = 1.", "Sí hay solución: x = 3, y = 1."), "c": t("Dependent gives 0 = 0.", "Dependiente da 0 = 0.")}, "right": t("One point: the lines cross.", "Un punto: las rectas se cruzan."), "solution": t("Independent.", "Independiente.")},
      "p7": {"ok": "a", "hints": {"b": t("5 is the number of nickels.", "5 es el número de monedas de 5¢."), "c": t("12 is all the coins.", "12 son todas las monedas.")}, "right": t("n + 2d = 19 minus n + d = 12: d = 7.", "n + 2d = 19 menos n + d = 12: d = 7."), "solution": "7."},
      "p8": {"ok": "b", "hints": {"a": t("7 is the smaller one.", "7 es el menor."), "c": t("10 + 10 = 20, but the difference must be 6.", "10 + 10 = 20, pero la diferencia debe ser 6.")}, "right": t("2x = 26, x = 13; y = 7.", "2x = 26, x = 13; y = 7."), "solution": "13."},
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Write x first: 2x = 10.", "Escriba primero x: 2x = 10."), "c": t("5 − 5 = 0, not 1.", "5 − 5 = 0, no 1."), "d": t("9 + 1 = 10, not 9.", "9 + 1 = 10, no 9.")}, "solution": "(5, 4)."},
      "B": {"ok": "c", "hints": {"a": t("Write x first: 3x = 9.", "Escriba primero x: 3x = 9."), "b": t("3 − 3 = 0, not 1.", "3 − 3 = 0, no 1."), "d": t("Check 2x + y = 8: 2 + 2 = 4.", "Compruebe 2x + y = 8: 2 + 2 = 4.")}, "solution": "(3, 2)."},
      "C": {"ok": "d", "hints": {"a": t("Check 3x − 2y = 0: 9 − 4 = 5.", "Compruebe 3x − 2y = 0: 9 − 4 = 5."), "b": t("Check 3x + 2y = 12: 6 + 4 = 10.", "Compruebe 3x + 2y = 12: 6 + 4 = 10."), "c": t("Check 3x − 2y = 0: 0 − 12.", "Compruebe 3x − 2y = 0: 0 − 12.")}, "solution": "(2, 3)."},
      "D": {"ok": "a", "hints": {"b": t("Check 2x + 3y = 7: 2 + 6 = 8.", "Compruebe 2x + 3y = 7: 2 + 6 = 8."), "c": t("Check 2x + 3y = 7: 4 + 6 = 10.", "Compruebe 2x + 3y = 7: 4 + 6 = 10."), "d": t("Check 3x + 2y = 8: 9 + 2 = 11.", "Compruebe 3x + 2y = 8: 9 + 2 = 11.")}, "solution": "(2, 1)."},
      "E": {"ok": "c", "hints": {"a": t("Independent gives x and y.", "Independiente da x e y."), "b": t("Dependent gives 0 = 0.", "Dependiente da 0 = 0."), "d": t("0 = 7 is false: there is no solution.", "0 = 7 es falso: no hay solución.")}, "solution": t("Inconsistent (no solution).", "Inconsistente (sin solución).")},
      "F": {"ok": "a", "hints": {"b": t("Something false means no solution; 0 = 0 is true.", "Algo falso significa sin solución; 0 = 0 es cierto."), "c": t("One solution gives x and y.", "Una solución da x e y."), "d": t("Inconsistent gives something false.", "Inconsistente da algo falso.")}, "solution": t("Infinitely many (dependent).", "Infinitas soluciones (dependiente).")},
      "G": {"ok": "d", "hints": {"a": t("6 is the number of nickels.", "6 es el número de monedas de 5¢."), "b": t("Check: 5(5) + 25(5) = 150, not 130.", "Compruebe: 5(5) + 25(5) = 150, no 130."), "c": t("10 is all the coins.", "10 son todas las monedas.")}, "solution": "4."},
      "H": {"ok": "b", "hints": {"a": t("9 is the bigger one.", "9 es el mayor."), "c": t("7.5 + 7.5 = 15, but one is 3 more than the other.", "7.5 + 7.5 = 15, pero uno es 3 más que el otro."), "d": t("12 + 3 = 15, but 12 is not 3 more than 3.", "12 + 3 = 15, pero 12 no es 3 más que 3.")}, "solution": "6."},
     }}

    quiz = [
     ("A", t("Solve by elimination: x + y = 9 ; x − y = 1.", "Resuelva por eliminación: x + y = 9 ; x − y = 1."), [("a", "(4, 5)"), ("b", "(5, 4)"), ("c", "(5, 5)"), ("d", "(9, 1)")]),
     ("B", t("Solve: 2x + y = 8 ; x − y = 1.", "Resuelva: 2x + y = 8 ; x − y = 1."), [("a", "(2, 3)"), ("b", "(3, 3)"), ("c", "(3, 2)"), ("d", "(1, 2)")]),
     ("C", t("Solve: 3x + 2y = 12 ; 3x − 2y = 0.", "Resuelva: 3x + 2y = 12 ; 3x − 2y = 0."), [("a", "(3, 2)"), ("b", "(2, 2)"), ("c", "(0, 6)"), ("d", "(2, 3)")]),
     ("D", t("Solve: 2x + 3y = 7 ; 3x + 2y = 8.", "Resuelva: 2x + 3y = 7 ; 3x + 2y = 8."), [("a", "(2, 1)"), ("b", "(1, 2)"), ("c", "(2, 2)"), ("d", "(3, 1)")]),
     ("E", t("When you solve, you get 0 = 7. What kind of system is it?", "Al resolver, se obtiene 0 = 7. ¿Qué tipo de sistema es?"), [("a", t("Independent", "Independiente")), ("b", t("Dependent", "Dependiente")), ("c", t("Inconsistent (no solution)", "Inconsistente (sin solución)")), ("d", t("It has one solution", "Tiene una solución"))]),
     ("F", t("When you solve, you get 0 = 0. What kind of system is it?", "Al resolver, se obtiene 0 = 0. ¿Qué tipo de sistema es?"), [("a", t("Infinitely many solutions (dependent)", "Infinitas soluciones (dependiente)")), ("b", t("No solution", "Sin solución")), ("c", t("One solution", "Una solución")), ("d", t("Inconsistent", "Inconsistente"))]),
     ("G", t("There are 10 coins, nickels (5¢) and quarters (25¢), worth 130¢. How many are quarters?", "Hay 10 monedas de 5¢ y 25¢ que suman 130¢. ¿Cuántas son de 25¢?"), [("a", "6"), ("b", "5"), ("c", "10"), ("d", "4")]),
     ("H", t("Two numbers add up to 15 and one is 3 more than the other. What is the smaller one?", "Dos números suman 15 y uno es 3 más que el otro. ¿Cuál es el menor?"), [("a", "9"), ("b", "6"), ("c", "7.5"), ("d", "12")])]

    tarea = (t("For your own work, with your notebook open: (1) How many solutions does it have? Solve by elimination and classify each system as independent (one point), inconsistent (parallel), or dependent (the same line), using the result as your reason: x + y = 6 and x − y = 2; 2x + 3y = 12 and 2x − y = 4; 3x + 2y = 16 and x − 2y = 0; x + y = 4 and x + y = 9; 2x − y = 3 and 4x − 2y = 6. (2) Do I eliminate or substitute? Before solving, explain in two sentences which method is best: y = 3x − 1 and 2x + y = 9; 3x + 4y = 10 and 3x − 2y = 4; x = 2y and 5x − 3y = 14; 5x + 2y = 1 and 3x − 2y = 7. (3) Coins and mixtures: (a) you have 20 dimes and quarters worth $3.50; how many of each are there? (b) A store mixes coffee at $6 a pound with coffee at $10 a pound to get 20 pounds at $7 a pound; how many pounds of each does it use? Set up the system, solve it, and check. Then do several exercises of each activity on the practice page. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) ¿Cuántas soluciones tiene? Resuelva por eliminación y clasifique cada sistema como independiente (un punto), inconsistente (paralelas) o dependiente (la misma recta), justificando con el resultado: x + y = 6 y x − y = 2; 2x + 3y = 12 y 2x − y = 4; 3x + 2y = 16 y x − 2y = 0; x + y = 4 y x + y = 9; 2x − y = 3 y 4x − 2y = 6. (2) ¿Elimino o sustituyo? Antes de resolver, justifique en dos oraciones qué método conviene: y = 3x − 1 y 2x + y = 9; 3x + 4y = 10 y 3x − 2y = 4; x = 2y y 5x − 3y = 14; 5x + 2y = 1 y 3x − 2y = 7. (3) Monedas y mezclas: (a) tiene 20 monedas de 10¢ y de 25¢ que suman $3.50; ¿cuántas hay de cada tipo? (b) Se mezcla café de $6 la libra con café de $10 la libra para obtener 20 libras a $7 la libra; ¿cuántas libras de cada uno se usan? Plantee el sistema, resuélvalo y compruébelo. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Empty a jar or a pocket of coins of two kinds. Count how many there are and how much they are worth, and ask someone at home to find how many of each there are with a system.",
               "Vacíe un frasco o un bolsillo de monedas de dos clases. Cuente cuántas hay y cuánto valen, y pídale a alguien en casa que halle cuántas hay de cada una con un sistema."))

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Solve systems by elimination, classify them as independent, inconsistent, or dependent, and choose the best method.", "Resuelva sistemas por eliminación, clasifíquelos en independientes, inconsistentes o dependientes y elija el método más conveniente."),
        ("✏️", t("No calculator", "Sin calculadora")),
        [t("<strong>Solve</strong> systems by elimination, multiplying one or both equations when needed.", "<strong>Resolver</strong> sistemas por eliminación, multiplicando una o ambas ecuaciones cuando haga falta."),
         t("<strong>Classify</strong> systems as independent, inconsistent, or dependent.", "<strong>Clasificar</strong> sistemas en independientes, inconsistentes o dependientes."),
         t("<strong>Choose</strong> between substitution and elimination.", "<strong>Elegir</strong> entre sustitución y eliminación."),
         t("<strong>Solve</strong> coin, ticket, mixture, and speed problems.", "<strong>Resolver</strong> problemas de monedas, boletos, mezclas y velocidades.")],
        secciones, tarea, quiz,
        t("Self-check checklist for elimination", "Lista de autoevaluación de la eliminación"),
        t("Self-check checklist: skills for elimination and classifying systems", "Lista de autoevaluación: destrezas de la eliminación y la clasificación de sistemas"),
        [(t("Making opposite coefficients", "Lograr coeficientes opuestos"), t("I choose the multipliers well and multiply every term, including the constant.", "Elijo bien los multiplicadores y multiplico todos los términos, incluido el independiente."), t("I multiply, but I forget a term or a sign.", "Multiplico, pero olvido algún término o un signo."), t("I add the equations without making opposite coefficients.", "Sumo las ecuaciones sin lograr coeficientes opuestos.")),
         (t("Classifying", "Clasificar"), t("I read 0 = number or 0 = 0 and connect it with the graph.", "Leo 0 = número o 0 = 0 y lo relaciono con la gráfica."), t("I classify, but I mix up inconsistent and dependent.", "Clasifico, pero confundo inconsistente y dependiente."), t("I do not know what 0 = 5 or 0 = 0 means.", "No sé qué significa 0 = 5 o 0 = 0.")),
         (t("Setting up applications", "Plantear aplicaciones"), t("I write the amount and value equations and check the answer.", "Escribo las ecuaciones de cantidad y de valor y compruebo la respuesta."), t("I write one of the two equations correctly.", "Escribo bien una de las dos ecuaciones."), t("I do not set up the system.", "No planteo el sistema."))],
        t("<p>In this lesson you solved systems by elimination, classified them by their number of solutions, and chose the best method. You also solved coin, ticket, and mixture problems.</p>\n<p>In <strong>Lesson 6.3 · Graphing systems and modeling</strong> you will add a third view, the graph, connect it with the algebra, translate word problems into systems, and find the break-even point of a business.</p>",
          "<p>En esta lección se resolvieron sistemas por eliminación, se clasificaron según su número de soluciones y se eligió el método más conveniente. También se resolvieron problemas de monedas, boletos y mezclas.</p>\n<p>En la <strong>Lección 6.3 · El método gráfico y el modelado</strong> se añadirá una tercera mirada, la gráfica, se conectará con el álgebra, se traducirán problemas verbales a sistemas y se hallará el punto de equilibrio de un negocio.</p>"),
        ("6-3", ("", t("Lesson 6.3 · Graphing systems and modeling", "Lección 6.3 · El método gráfico y el modelado"))),
        [(t("elimination", "eliminación"), t("Adding the equations, after multiplying if needed, so that one variable disappears.", "Sumar las ecuaciones, tras multiplicar si hace falta, para que una variable desaparezca.")),
         (t("independent system", "sistema independiente"), t("One solution: the lines cross at one point.", "Una solución: las rectas se cruzan en un punto.")),
         (t("inconsistent system", "sistema inconsistente"), t("No solution: the lines are parallel.", "Ninguna solución: las rectas son paralelas.")),
         (t("dependent system", "sistema dependiente"), t("Infinitely many solutions: both equations are the same line.", "Infinitas soluciones: las dos ecuaciones son la misma recta."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function mcd2(u, v){ u = Math.abs(u); v = Math.abs(v); while (v){ var w = u % v; u = v; v = w; } return u; }
function mulL(L, k){ return L3(L.a * k, L.b * k, L.c * k); }
/* A system to solve by elimination: tipo 0 already opposite, 1 multiply one, 2 multiply both */
function sisElim(tipo){
  var x0 = nz(-6, 6), y0 = aleatorio(-6, 6), L1, L2, k = 0;
  tipo = tipo === undefined ? aleatorio(0, 2) : tipo;
  do {
    if (tipo === 0){ var b = aleatorio(1, 4), a1 = nz(-4, 4), a2 = nz(-4, 4); L1 = L3(a1, b, a1 * x0 + b * y0); L2 = L3(a2, -b, a2 * x0 - b * y0); }
    else if (tipo === 1){ var bb = elige([2, 3, 4]), c1 = nz(-4, 4), c2 = nz(-3, 3), s = elige([1, -1]); L1 = L3(c1, bb, c1 * x0 + bb * y0); L2 = L3(c2, s, c2 * x0 + s * y0); }
    else { var p = aleatorio(2, 5), q = aleatorio(2, 5), r = aleatorio(2, 5), u = aleatorio(2, 5) * elige([1, -1]); L1 = L3(p, q, p * x0 + q * y0); L2 = L3(r, u, r * x0 + u * y0); if (p === r || q === Math.abs(u) || p % r === 0 || r % p === 0 || q % Math.abs(u) === 0 || Math.abs(u) % q === 0){ k++; continue; } }
    k++;
  } while ((L1.a * L2.b - L2.a * L1.b === 0 || mcd2(mcd2(L1.a, L1.b), L1.c) > 1 && tipo !== 0) && k < 300);
  return {L1: L1, L2: L2, x: x0, y: y0, tipo: tipo};
}
/* Elimination of y (or of x when it is easier) */
function pasosElim(c){
  var L1 = c.L1, L2 = c.L2, P = [], elimY = true;
  if (c.tipo === 2 && Math.abs(L1.a) * Math.abs(L2.a) < Math.abs(L1.b) * Math.abs(L2.b)) elimY = false;
  var k1, k2, g;
  if (elimY){ g = mcd2(L1.b, L2.b); k1 = Math.abs(L2.b) / g; k2 = Math.abs(L1.b) / g; if (L1.b * L2.b > 0) k2 = -k2; }
  else { g = mcd2(L1.a, L2.a); k1 = Math.abs(L2.a) / g; k2 = Math.abs(L1.a) / g; if (L1.a * L2.a > 0) k2 = -k2; }
  var M1 = mulL(L1, k1), M2 = mulL(L2, k2), v = elimY ? "y" : "x", w = elimY ? "x" : "y";
  if (k1 === 1 && Math.abs(k2) === 1 && k2 === 1) P.push(T("The " + v + " coefficients are already opposites: ", "Los coeficientes de " + v + " ya son opuestos: ") + terminoXY(elimY ? L1.b : L1.a, v, true) + T(" and ", " y ") + terminoXY(elimY ? L2.b : L2.a, v, true) + ".");
  else { var l = []; if (k1 !== 1) l.push(T("the first by ", "la primera por ") + k1 + " (" + ecTxt(M1) + ")"); if (k2 !== 1) l.push(T("the second by ", "la segunda por ") + sg(k2) + " (" + ecTxt(M2) + ")"); P.push(T("To eliminate " + v + ", multiply ", "Para eliminar " + v + ", se multiplica ") + l.join(T(" and ", " y ")) + "."); }
  var A = elimY ? M1.a + M2.a : M1.b + M2.b, C = M1.c + M2.c, val = C / A;
  P.push(T("Add the equations: ", "Se suman las ecuaciones: ") + "(" + ecTxt(M1).split(" = ")[0] + ") + (" + ecTxt(M2).split(" = ")[0] + ") = " + sg(M1.c) + " + " + pn(M2.c) + " → " + terminoXY(A, w, true) + " = " + sg(C) + ", " + w + " = " + sg(val) + ".");
  var other = elimY ? (L1.c - L1.a * val) / L1.b : (L1.c - L1.b * val) / L1.a;
  P.push(T("Substitute into the first equation to find ", "Se sustituye en la primera ecuación para hallar ") + v + ": " + (elimY ? (L1.a === 1 ? "" : L1.a === -1 ? "−" : sg(L1.a)) + "(" + sg(val) + ")" + terminoXY(L1.b, "y", false) : terminoXY(L1.a, "x", true) + (L1.b < 0 ? " − " : " + ") + (Math.abs(L1.b) === 1 ? "" : Math.abs(L1.b)) + "(" + sg(val) + ")") + " = " + sg(L1.c) + ", " + v + " = " + sg(other) + ".");
  P.push(T("Check in both: ", "Se verifica en las dos: ") + sustTxt(L1, c.x, c.y) + " ✓; " + sustTxt(L2, c.x, c.y) + " ✓.");
  P.push(T("Solution: ", "Solución: ") + "<strong>" + par(c.x, c.y) + "</strong>.");
  return P;
}
pasoAPaso4("el", function(){ var c = sisElim(); return {enun: T("Solve by elimination: ", "Resuelva por eliminación: ") + sisHTML(c.L1, c.L2) + ".", pasos: pasosElim(c)}; });
creaPracticaPar("eq", function(){ var c = sisElim();
  return {enun: T("Solve by elimination: ", "Resuelva por eliminación: ") + sisHTML(c.L1, c.L2), x: c.x, y: c.y, diag: diagSis(c.L1, c.L2, c), solucion: pasosElim(c).join(" ").replace(/<\/?strong>/g, "")};
});

/* ===== MODULE 2 · Classifying ===== */
var CLAS = [[L3(1, 1, 4), L3(1, -1, 2)], [L3(1, 1, 4), L3(1, 1, 7)], [L3(1, 1, 4), L3(2, 2, 8)], [L3(2, -1, 3), L3(4, -2, 10)], [L3(-2, 1, 1, "y = 2x + 1"), L3(4, -2, -2)]];
function resultadoElim(L1, L2){
  var g = mcd2(L1.a, L2.a) || 1, k1 = Math.abs(L2.a) / g, k2 = Math.abs(L1.a) / g; if (L1.a * L2.a > 0) k2 = -k2;
  var M1 = mulL(L1, k1), M2 = mulL(L2, k2), B = M1.b + M2.b, C = M1.c + M2.c;
  return {M1: M1, M2: M2, B: B, C: C, txt: T("Multiply the first by ", "Se multiplica la primera por ") + k1 + T(" and the second by ", " y la segunda por ") + sg(k2) + T(" and add: ", " y se suman: ") + (B ? terminoXY(B, "y", true) + " = " + sg(C) : "0 = " + sg(C))};
}
function claseDe(L1, L2){ var r = resuelveSis(L1, L2); return r.tipo === "uno" ? "ind" : r.tipo === "ninguna" ? "inc" : "dep"; }
var NOM_CL = {ind: T("Independent: one solution", "Independiente: una solución"), inc: T("Inconsistent: no solution", "Inconsistente: ninguna solución"), dep: T("Dependent: infinitely many solutions", "Dependiente: infinitas soluciones")};
function clDibuja(){
  var S = CLAS[+$("cl-ex").value], L1 = S[0], L2 = S[1], r = resuelveSis(L1, L2), e = resultadoElim(L1, L2), cl = claseDe(L1, L2);
  $("cl-sis").innerHTML = sisHTML(L1, L2);
  $("cl-txt").innerHTML = '<div class="linea">' + T("Algebra: ", "Álgebra: ") + e.txt + (cl === "ind" ? "; " + T("then ", "luego ") + "x = " + sg(r.x) + ", y = " + sg(r.y) + "." : cl === "inc" ? T(" — false! ", " — ¡falso! ") : T(" — always true! ", " — ¡siempre cierto! ")) + "</div>" +
    '<div class="linea">' + T("Graph: ", "Gráfica: ") + (cl === "ind" ? T("the lines cross at ", "las rectas se cruzan en ") + par(r.x, r.y) : cl === "inc" ? T("the lines are parallel (same slope, different intercept).", "las rectas son paralelas (misma pendiente, distinto intercepto).") : T("the two equations are the same line.", "las dos ecuaciones son la misma recta.")) + "</div>" +
    '<div class="linea"><strong>' + NOM_CL[cl] + ".</strong></div>";
  $("cl-graf").innerHTML = grafSis(L1, L2, {etiquetas: cl === "dep" ? [ecTxt(L1), ecTxt(L2) + T(" (the same line)", " (la misma recta)")] : null});
}
$("cl-ex").addEventListener("change", clDibuja); clDibuja();
function sisClase(cl){
  var a = nz(-4, 4), b = nz(-4, 4), x0 = aleatorio(-4, 4), y0 = aleatorio(-4, 4), c = a * x0 + b * y0, k = elige([2, 3, -1, -2]);
  if (mcd2(a, b) > 1) b = b > 0 ? 1 : -1;
  c = a * x0 + b * y0;
  var L1 = L3(a, b, c);
  if (cl === "ind"){ var S = sisCon(x0, y0, {lim: 4}); return S; }
  if (cl === "dep") return [L1, L3(k * a, k * b, k * c)];
  return [L1, L3(k * a, k * b, k * c + nz(-6, 6) * (Math.abs(k) === 1 ? 1 : 1))];
}
OMR("cq", function(){ var cl = elige(["ind", "inc", "dep"]), S = sisClase(cl), e = resultadoElim(S[0], S[1]);
  return {enun: T("Classify the system ", "Clasifique el sistema ") + sisHTML(S[0], S[1]) + ".", correcta: claseDe(S[0], S[1]), enOrden: true, opciones: ["ind", "inc", "dep"].map(function(x){ return {clave: x, html: NOM_CL[x]}; }),
    pista: T("Eliminate a variable and look at what is left.", "Elimine una variable y mire lo que queda."), bien: e.txt + ". " + NOM_CL[claseDe(S[0], S[1])] + "."};
});

/* ===== MODULE 3 · Choosing the method ===== */
OMR("mq", function(){ var x0 = nz(-5, 5), y0 = aleatorio(-5, 5), sust = Math.random() < .5, S, motivo;
  if (sust){ var f = elige(["y", "x"]); S = sisCon(x0, y0, {f1: f, f2: "std", lim: 5}); motivo = T("The first equation already has " + f + " alone: substitute it into the second.", "La primera ecuación ya tiene " + f + " despejada: se sustituye en la segunda."); }
  else { var k = 0; do { S = sisCon(x0, y0, {lim: 6}); k++; } while ((Math.abs(S[0].a) === 1 || Math.abs(S[0].b) === 1 || Math.abs(S[1].a) === 1 || Math.abs(S[1].b) === 1) && k < 200);
    if (Math.random() < .5){ var b = aleatorio(2, 5), a1 = aleatorio(2, 5), a2 = aleatorio(2, 5); if (a1 !== a2) S = [L3(a1, b, a1 * x0 + b * y0), L3(a2, -b, a2 * x0 - b * y0)]; }
    motivo = T("Both equations are in the form ax + by = c and no coefficient is 1 or −1: solving for a variable would bring fractions. Eliminate.", "Las dos ecuaciones están en la forma ax + by = c y ningún coeficiente es 1 o −1: despejar traería fracciones. Conviene eliminar.");
    if (S[0].b === -S[1].b) motivo = T("The y coefficients are already opposites: add the equations.", "Los coeficientes de y ya son opuestos: basta con sumar las ecuaciones."); }
  return {enun: T("Which method is best for ", "¿Qué método conviene más para ") + sisHTML(S[0], S[1]) + "?", correcta: sust ? "s" : "e", enOrden: true,
    opciones: [{clave: "s", html: T("Substitution", "Sustitución")}, {clave: "e", html: T("Elimination", "Eliminación")}], pista: T("Is a variable already alone, or with a coefficient of 1 or −1?", "¿Hay una variable ya despejada, o con coeficiente 1 o −1?"), bien: motivo};
});

/* ===== MODULE 4 · Applications ===== */
var APL = [
  {enun: T("There are 12 coins, some nickels (5¢) and some dimes (10¢), worth 95¢ in all. How many of each are there?", "Hay 12 monedas, unas de 5 centavos y otras de 10 centavos, que en total suman 95 centavos. ¿Cuántas hay de cada clase?"),
   pasos: [T("Name: let <strong>n</strong> be the number of nickels and <strong>d</strong> the number of dimes.", "Nombrar: sea <strong>n</strong> el número de monedas de 5 centavos y <strong>d</strong> el de monedas de 10 centavos."), T("<strong>Amount</strong> equation: there are 12 coins in all → <strong>n + d = 12</strong>.", "Ecuación de <strong>cantidad</strong>: en total hay 12 monedas → <strong>n + d = 12</strong>."), T("<strong>Value</strong> equation: each nickel is worth 5 cents and each dime 10 → <strong>5n + 10d = 95</strong>.", "Ecuación de <strong>valor</strong>: cada moneda de 5¢ aporta 5 centavos y cada una de 10¢ aporta 10 → <strong>5n + 10d = 95</strong>."), T("Simplify the value equation by dividing it by 5: n + 2d = 19. Dividing a whole equation is allowed and leaves smaller numbers.", "Simplificar la de valor dividiéndola entre 5: n + 2d = 19. Dividir una ecuación entera es legítimo y deja números más pequeños."), T("Subtract the amount equation: (n + 2d) − (n + d) = 19 − 12, so <strong>d = 7</strong>; then n = 12 − 7 = <strong>5</strong>.", "Restar la de cantidad: (n + 2d) − (n + d) = 19 − 12, o sea <strong>d = 7</strong>; entonces n = 12 − 7 = <strong>5</strong>."), T("Reread the question: there are <strong>5 nickels and 7 dimes</strong>. Check: 5(5) + 10(7) = 25 + 70 = 95 ✓.", "Releer la pregunta: hay <strong>5 monedas de 5¢ y 7 de 10¢</strong>. Comprobación: 5(5) + 10(7) = 25 + 70 = 95 ✓.")]},
  {enun: T("A show sold 200 tickets and took in $1,450. An adult ticket costs $8 and a child ticket, $5. How many tickets of each kind were sold?", "En una función se vendieron 200 boletos y se recaudaron $1,450. El boleto de adulto cuesta $8 y el de niño, $5. ¿Cuántos boletos de cada tipo se vendieron?"),
   pasos: [T("Name: let <strong>a</strong> be the number of adult tickets and <strong>c</strong> the number of child tickets.", "Nombrar: sea <strong>a</strong> el número de boletos de adulto y <strong>n</strong> el de boletos de niño."), T("Amount equation: 200 tickets were sold → <strong>a + c = 200</strong>.", "Ecuación de cantidad: se vendieron 200 boletos → <strong>a + n = 200</strong>."), T("Value equation: each adult pays $8 and each child $5 → <strong>8a + 5c = 1,450</strong>.", "Ecuación de valor: cada adulto aporta 8 dólares y cada niño, 5 → <strong>8a + 5n = 1,450</strong>."), T("Multiply the amount equation by −5 to eliminate c: −5a − 5c = −1,000.", "Multiplicar la de cantidad por −5 para eliminar n: −5a − 5n = −1,000."), T("Add: <strong>3a = 450</strong> and <strong>a = 150</strong>; then c = 50.", "Sumar: <strong>3a = 450</strong> y <strong>a = 150</strong>; entonces n = 50."), T("Reread: <strong>150 adult tickets and 50 child tickets</strong> were sold. Check: 8(150) + 5(50) = 1,200 + 250 = 1,450 ✓.", "Releer: se vendieron <strong>150 boletos de adulto y 50 de niño</strong>. Comprobación: 8(150) + 5(50) = 1,200 + 250 = 1,450 ✓.")]},
  {enun: T("A store mixes coffee at $6 a pound with coffee at $9 a pound to get 30 pounds to sell at $7 a pound. How many pounds of each does it use?", "Una tienda mezcla café de $6 la libra con café de $9 la libra para obtener 30 libras que se venderán a $7 la libra. ¿Cuántas libras usa de cada uno?"),
   pasos: [T("Name: let <strong>x</strong> be the pounds of the $6 coffee and <strong>y</strong> the pounds of the $9 coffee.", "Nombrar: sea <strong>x</strong> las libras de café de $6 y <strong>y</strong> las libras de café de $9."), T("Amount equation: the mixture weighs 30 pounds → <strong>x + y = 30</strong>.", "Ecuación de cantidad: la mezcla pesa 30 libras → <strong>x + y = 30</strong>."), T("Value equation: the whole mixture is worth 30 · 7 = 210 dollars → <strong>6x + 9y = 210</strong>.", "Ecuación de valor: el valor total de la mezcla es 30 · 7 = 210 dólares → <strong>6x + 9y = 210</strong>."), T("Multiply the amount equation by −6: −6x − 6y = −180.", "Multiplicar la de cantidad por −6: −6x − 6y = −180."), T("Add: <strong>3y = 30</strong>, so <strong>y = 10</strong> and x = 30 − 10 = <strong>20</strong>.", "Sumar: <strong>3y = 30</strong>, entonces <strong>y = 10</strong> y x = 30 − 10 = <strong>20</strong>."), T("Reread: it uses <strong>20 pounds of the $6 coffee and 10 pounds of the $9 coffee</strong>. Check: 6(20) + 9(10) = 120 + 90 = 210 ✓.", "Releer: se usan <strong>20 libras del de $6 y 10 libras del de $9</strong>. Comprobación: 6(20) + 9(10) = 120 + 90 = 210 ✓.")]},
  {enun: T("A boat goes 36 miles downstream in 3 hours, and the same 36 miles upstream in 6 hours. How fast does the boat go in still water, and how fast is the current?", "Un bote recorre 36 millas a favor de la corriente en 3 horas, y las mismas 36 millas en contra en 6 horas. ¿Cuál es la velocidad del bote en agua quieta y la de la corriente?"),
   pasos: [T("Name: let <strong>v</strong> be the speed of the boat in still water and <strong>c</strong> the speed of the current, both in mph.", "Nombrar: sea <strong>v</strong> la velocidad del bote en agua quieta y <strong>c</strong> la velocidad de la corriente, las dos en mph."), T("Downstream the real speed is v + c, and it covers 36 miles in 3 hours: 36/3 = 12 → <strong>v + c = 12</strong>.", "A favor, la velocidad efectiva es v + c, y recorre 36 millas en 3 horas: 36/3 = 12 → <strong>v + c = 12</strong>."), T("Upstream the real speed is v − c, and it covers 36 miles in 6 hours: 36/6 = 6 → <strong>v − c = 6</strong>.", "En contra, la velocidad efectiva es v − c, y recorre 36 millas en 6 horas: 36/6 = 6 → <strong>v − c = 6</strong>."), T("The c coefficients are already opposites: this system calls for elimination.", "Los coeficientes de c ya son opuestos: este sistema pide eliminación."), T("Add: <strong>2v = 18</strong>, so <strong>v = 9</strong>; and from v + c = 12, <strong>c = 3</strong>.", "Sumar: <strong>2v = 18</strong>, entonces <strong>v = 9</strong>; y de v + c = 12 sale <strong>c = 3</strong>."), T("Reread: the boat goes <strong>9 mph</strong> in still water and the current, <strong>3 mph</strong>. Check: downstream, 12 mph for 3 hours is 36 miles ✓.", "Releer: el bote va a <strong>9 mph</strong> en agua quieta y la corriente, a <strong>3 mph</strong>. Comprobación: a favor, 12 mph durante 3 h son 36 millas ✓.")]},
  {enun: T("A father is three times as old as his son. In 10 years he will be only twice as old. How old is each one today?", "Un padre tiene el triple de la edad de su hijo. Dentro de 10 años tendrá solo el doble. ¿Qué edad tiene cada uno hoy?"),
   pasos: [T("Name: let <strong>f</strong> be the father's age today and <strong>s</strong> the son's.", "Nombrar: sea <strong>p</strong> la edad del padre hoy y <strong>h</strong> la del hijo hoy."), T("“Three times the son's age” → <strong>f = 3s</strong>.", "«El triple de la edad del hijo» → <strong>p = 3h</strong>."), T("In 10 years each will be 10 years older, and then the father will be twice as old → <strong>f + 10 = 2(s + 10)</strong>.", "Dentro de 10 años cada uno tendrá 10 años más, y entonces el padre tendrá el doble → <strong>p + 10 = 2(h + 10)</strong>."), T("Since f is already alone, substitution is best: 3s + 10 = 2(s + 10) = 2s + 20.", "Como p ya está despejada, conviene sustitución: 3h + 10 = 2(h + 10) = 2h + 20."), T("Solve: 3s − 2s = 20 − 10, so <strong>s = 10</strong> and f = 3(10) = <strong>30</strong>.", "Resolver: 3h − 2h = 20 − 10, entonces <strong>h = 10</strong> y p = 3(10) = <strong>30</strong>."), T("Reread: the son is <strong>10 years old</strong> and the father, <strong>30</strong>. Check: in 10 years they will be 20 and 40, which is twice ✓.", "Releer: el hijo tiene <strong>10 años</strong> y el padre, <strong>30</strong>. Comprobación: dentro de 10 años tendrán 20 y 40, que es el doble ✓.")]}];
pasoAPaso4("ap", function(){ var c = APL[+$("ap-ex").value]; return {enun: c.enun, pasos: c.pasos}; });
$("ap-ex").addEventListener("change", function(){ $("ap-nuevo").click(); });
function opNum(l, suf){ var vis = {}, ops = []; l.forEach(function(v, i){ var h = sg(v) + (suf || ""); if (!vis[h] && v > 0 && v === Math.round(v) && ops.length < 4){ vis[h] = 1; ops.push({clave: i ? "m" + i : "ok", html: h}); } }); return ops; }
OMR("aq", function(){ var tipo = aleatorio(0, 2);
  if (tipo === 0){ var M = elige([[5, 10, T("nickels", "de 5¢"), T("dimes", "de 10¢")], [10, 25, T("dimes", "de 10¢"), T("quarters", "de 25¢")], [5, 25, T("nickels", "de 5¢"), T("quarters", "de 25¢")]]), a = aleatorio(2, 12), b = aleatorio(2, 12), tot = a + b, val = M[0] * a + M[1] * b, q = Math.random() < .5;
    return {enun: T("There are " + tot + " coins, " + M[2] + " and " + M[3] + ", worth " + val + "¢ in all. How many " + (q ? M[3] : M[2]) + " are there?", "Hay " + tot + " monedas, unas " + M[2] + " y otras " + M[3] + ", que suman " + val + "¢. ¿Cuántas son " + (q ? M[3] : M[2]) + "?"), correcta: "ok", opciones: opNum([q ? b : a, q ? a : b, tot, Math.round(val / M[1])]),
      pista: T("Amount: x + y = " + tot + ". Value: " + M[0] + "x + " + M[1] + "y = " + val + ".", "Cantidad: x + y = " + tot + ". Valor: " + M[0] + "x + " + M[1] + "y = " + val + "."), bien: T("Amount: x + y = " + tot + "; value: " + M[0] + "x + " + M[1] + "y = " + val + ". Multiply the first by −" + M[0] + " and add: " + (M[1] - M[0]) + "y = " + (val - M[0] * tot) + ", y = " + b + "; x = " + a + ".", "Cantidad: x + y = " + tot + "; valor: " + M[0] + "x + " + M[1] + "y = " + val + ". Se multiplica la primera por −" + M[0] + " y se suma: " + (M[1] - M[0]) + "y = " + (val - M[0] * tot) + ", y = " + b + "; x = " + a + ".")}; }
  if (tipo === 1){ var pa = aleatorio(6, 15), pc = aleatorio(2, pa - 1), na = 10 * aleatorio(2, 15), nc = 10 * aleatorio(2, 15), tt = na + nc, din = pa * na + pc * nc, qa = Math.random() < .5;
    return {enun: T("A show sold " + tt + " tickets and took in $" + din.toLocaleString("en-US") + ". An adult ticket costs $" + pa + " and a child ticket, $" + pc + ". How many " + (qa ? "adult" : "child") + " tickets were sold?", "En una función se vendieron " + tt + " boletos y se recaudaron $" + din.toLocaleString("en-US") + ". El boleto de adulto cuesta $" + pa + " y el de niño, $" + pc + ". ¿Cuántos boletos de " + (qa ? "adulto" : "niño") + " se vendieron?"), correcta: "ok", opciones: opNum([qa ? na : nc, qa ? nc : na, tt, tt / 2]),
      pista: T("Amount: a + c = " + tt + ". Value: " + pa + "a + " + pc + "c = " + din + ".", "Cantidad: a + n = " + tt + ". Valor: " + pa + "a + " + pc + "n = " + din + "."), bien: T("Multiply the amount equation by −" + pc + " and add: " + (pa - pc) + "a = " + (din - pc * tt) + ", a = " + na + "; c = " + nc + ".", "Se multiplica la de cantidad por −" + pc + " y se suma: " + (pa - pc) + "a = " + (din - pc * tt) + ", a = " + na + "; n = " + nc + ".")}; }
  var p1 = elige([5, 6, 7]), p2 = p1 + elige([2, 3, 4, 6]), x = aleatorio(2, 15), y = aleatorio(2, 15), lb = x + y, tv = p1 * x + p2 * y, qq = Math.random() < .5;
  if (tv % lb){ y = x; lb = 2 * x; tv = (p1 + p2) * x; }
  var pm = tv / lb;
  return {enun: T("A store mixes coffee at $" + p1 + " a pound with coffee at $" + p2 + " a pound to get " + lb + " pounds worth $" + tv + " in all. How many pounds of the $" + (qq ? p2 : p1) + " coffee does it use?", "Una tienda mezcla café de $" + p1 + " la libra con café de $" + p2 + " la libra para obtener " + lb + " libras con un valor total de $" + tv + ". ¿Cuántas libras usa del café de $" + (qq ? p2 : p1) + "?"), correcta: "ok", opciones: opNum([qq ? y : x, qq ? x : y, lb, lb / 2 + 1]),
    pista: T("Amount: x + y = " + lb + ". Value: " + p1 + "x + " + p2 + "y = " + tv + ".", "Cantidad: x + y = " + lb + ". Valor: " + p1 + "x + " + p2 + "y = " + tv + "."), bien: T("Multiply the amount equation by −" + p1 + " and add: " + (p2 - p1) + "y = " + (tv - p1 * lb) + ", y = " + y + "; x = " + x + ".", "Se multiplica la de cantidad por −" + p1 + " y se suma: " + (p2 - p1) + "y = " + (tv - p1 * lb) + ", y = " + y + "; x = " + x + ".")};
});
'''

def practica_pagina():
    n = N
    cl = [("0", "x + y = 4 ; x − y = 2"), ("1", "x + y = 4 ; x + y = 7"), ("2", "x + y = 4 ; 2x + 2y = 8"), ("3", "2x − y = 3 ; 4x − 2y = 10"), ("4", "y = 2x + 1 ; 4x − 2y = −2")]
    ap = [("0", t("Nickels and dimes", "Monedas de 5¢ y de 10¢")), ("1", t("Adult and child tickets", "Boletos de adulto y de niño")), ("2", t("A coffee mixture", "Mezcla de café")), ("3", t("The boat and the current", "El bote y la corriente")), ("4", t("Ages", "Las edades"))]
    clase = (f'<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("The three kinds of systems", "Los tres tipos de sistemas")}</caption><thead><tr><th scope="col">{t("Kind", "Tipo")}</th><th scope="col">{t("Lines", "Rectas")}</th><th scope="col">{t("Solutions", "Soluciones")}</th><th scope="col">{t("When you solve…", "Al resolver…")}</th></tr></thead><tbody>'
             f'<tr><td>{t("Independent", "Independiente")}</td><td>{t("Cross", "Se cruzan")}</td><td>{t("One", "Una")}</td><td>x = …, y = …</td></tr>'
             f'<tr><td>{t("Inconsistent", "Inconsistente")}</td><td>{t("Parallel", "Paralelas")}</td><td>{t("None", "Ninguna")}</td><td>0 = 5 ({t("false", "falso")})</td></tr>'
             f'<tr><td>{t("Dependent", "Dependiente")}</td><td>{t("The same line", "La misma recta")}</td><td>{t("Infinitely many", "Infinitas")}</td><td>0 = 0 ({t("always true", "siempre cierto")})</td></tr></tbody></table></div>')
    mods = [
     (t("elimination", "eliminacion"), t("The elimination method", "El método de eliminación"),
      f'''      <p>{t("Make the coefficients of one variable opposites, multiplying one or both equations if needed (every term, the constant too). Then add the equations: that variable disappears.", "Se logra que los coeficientes de una variable sean opuestos, multiplicando una o ambas ecuaciones si hace falta (todos los términos, también el independiente). Después se suman las ecuaciones: esa variable desaparece.")}</p>
{n4.pasos("el", t("Another system", "Otro sistema"))}
{n4.par_libre("eq", t("Practice: solve by elimination", "Practique: resuelva por eliminación"))}'''),
     (t("classify", "clasificar"), t("Classifying systems", "Clasificar los sistemas"),
      f'''{clase}
      <div class="panel"><div class="campos">{n4.lista("cl-ex", t("System", "Sistema"), cl)}</div><p class="enun" id="cl-sis"></p></div>
{n4.salida("cl-txt")}
      <div id="cl-graf"></div>
{B.om("cq", t("Practice: classify the system", "Practique: clasifique el sistema"))}'''),
     (t("method", "metodo"), t("Substitution or elimination?", "¿Sustitución o eliminación?"),
      f'''      <p>{t("Both methods give the same solution. Substitution is best when a variable is already alone or has a coefficient of 1 or −1; elimination, when both equations are in the form ax + by = c and the coefficients line up easily.", "Los dos métodos dan la misma solución. La sustitución conviene cuando una variable ya está despejada o tiene coeficiente 1 o −1; la eliminación, cuando las dos ecuaciones están en la forma ax + by = c y los coeficientes se alinean fácilmente.")}</p>
{B.om("mq", t("Practice: which method is best?", "Practique: ¿qué método conviene?"))}'''),
     (t("applications", "aplicacion"), t("Mixtures, coins, and speeds", "Mezclas, monedas y velocidades"),
      f'''      <p>{t("Name the unknowns, write an amount equation and a value equation (or one for each fact), solve, and reread the question.", "Nombre las incógnitas, escriba una ecuación de cantidad y otra de valor (o una por cada dato), resuelva y relea la pregunta.")}</p>
      <div class="panel"><div class="campos">{n4.lista("ap-ex", t("Situation", "Situación"), ap)}</div></div>
{n4.pasos("ap", t("Start again", "Empezar de nuevo"))}
{B.om("aq", t("Practice: solve the situation", "Practique: resuelva la situación"))}''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver sistemas por eliminación y clasificar sistemas")
