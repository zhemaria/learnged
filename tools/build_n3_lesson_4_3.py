"""Level 3 · Lesson 4.3 · Equations with fractions, decimals, and special cases — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "4-3"
TEMA = ("Linear algebra", "Álgebra lineal")
TIT = ("Equations with fractions, decimals, and special cases", "Ecuaciones con coeficientes fraccionarios, decimales y casos especiales")
SCRIPTS = ("/math/radicals.js", "/math/linear.js")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def leccion():
    n = N
    tipos = [[t("x = a number", "x = un número"), t("One solution", "Una solución"), t("Exactly one value makes the equation true.", "Un único valor hace verdadera la ecuación.")],
             [t("Something false (5 = 9)", "Algo falso (5 = 9)"), t("No solution", "Sin solución"), t("No value works (a contradiction).", "Ningún valor funciona (contradicción).")],
             [t("Something true (6 = 6)", "Algo verdadero (6 = 6)"), t("Infinitely many solutions", "Infinitas soluciones"), t("Every value works (an identity).", "Todo valor funciona (identidad).")]]
    s1 = f'''<p>{t("In Lesson 4.2 you solved linear equations with the five-step strategy. This lesson adds two tools for harder cases: a way to “clean up” fractions and decimals before you solve, so the equation has only whole numbers, and how to recognize two special results that do not give a single value: no solution and infinitely many solutions.",
"En la Lección 4.2 se resolvieron ecuaciones lineales con la estrategia de cinco pasos. Esta lección añade dos herramientas para los casos más difíciles: una estrategia para «limpiar» fracciones y decimales antes de resolver, de modo que la ecuación quede con números enteros, y el reconocimiento de dos resultados especiales que no dan un único valor: sin solución e infinitas soluciones.")}</p>
<p>{t("An equation with fractions becomes much easier if you clear the fractions first. To do that, multiply every term on both sides by the <strong>least common multiple (LCM)</strong> of the denominators.", "Una ecuación con fracciones se vuelve mucho más fácil si primero se eliminan las fracciones. Para ello, se multiplican todos los términos de ambos lados por el <strong>mínimo común múltiplo (MCM)</strong> de los denominadores.")}</p>
{ejemplo(t(f"Example 1: solve {fx('x', 2)} + 3 = 7", f"Ejemplo 1: resuelva {fx('x', 2)} + 3 = 7"),
  [("1", t("Multiply every term by 2.", "Multiplicar cada término por 2."), t(f"The only denominator is 2: 2 · ({fx('x', 2)}) + 2 · 3 = 2 · 7.", f"El único denominador es 2: 2 · ({fx('x', 2)}) + 2 · 3 = 2 · 7.")),
   ("2", t("Simplify.", "Simplificar."), "x + 6 = 14."),
   ("3", t("Subtract 6.", "Restar 6."), "x = 8."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 8</strong>")])}
{ejemplo(t(f"Example 2: solve {fx('x', 2)} + {fx('x', 4)} = 6", f"Ejemplo 2: resuelva {fx('x', 2)} + {fx('x', 4)} = 6"),
  [("1", t("The LCM of 2 and 4 is 4.", "El MCM de 2 y 4 es 4."), f"4 · ({fx('x', 2)}) + 4 · ({fx('x', 4)}) = 4 · 6."),
   ("2", t("Simplify.", "Simplificar."), t("2x + x = 24, that is, 3x = 24.", "2x + x = 24, es decir, 3x = 24.")),
   ("3", t("Divide by 3.", "Dividir entre 3."), "x = 8."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 8</strong>")])}
{caja("ojo", t("Multiply every term", "Multiplicar todos los términos"), t("<p>The LCM must multiply every term, including the ones with no fraction (like the 3 in Example 1 or the 6 in Example 2). Forgetting a term is the most common mistake when you clear fractions.</p>", "<p>El MCM debe multiplicar cada término, incluidos los que no tienen fracción (como el 3 del Ejemplo 1 o el 6 del Ejemplo 2). Olvidar un término es el error más frecuente al limpiar fracciones.</p>"))}
{enlace(n, t("fractions", "fracciones"), t("clearing fractions with the LCM", "limpiar fracciones con el MCM"), t("Multiply the whole equation by the LCM of the denominators.", "Multiplique toda la ecuación por el MCM de los denominadores."))}'''

    s2 = f'''<p>{t("With decimal coefficients the idea is the same: multiply every term by 10, 100, or 1000, depending on the greatest number of decimal places, to turn the decimals into whole numbers.", "Con coeficientes decimales se aplica la misma idea: se multiplican todos los términos por 10, 100 o 1000, según la mayor cantidad de cifras decimales, para convertir los decimales en enteros.")}</p>
{ejemplo(t("Example 3: solve 0.2x + 1 = 3", "Ejemplo 3: resuelva 0.2x + 1 = 3"),
  [("1", t("One decimal place.", "Una cifra decimal."), t("The most decimal places is one, so multiply every term by 10.", "La mayor cantidad de decimales es una cifra: se multiplica cada término por 10.")),
   ("2", t("Whole numbers.", "Enteros."), "2x + 10 = 30."),
   ("3", t("Solve.", "Resolver."), t("Subtract 10 and divide by 2: 2x = 20, x = 10.", "Se resta 10 y se divide entre 2: 2x = 20, x = 10.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 10</strong>")])}
{caja("tip", t("Which power to use", "Qué potencia usar"), t("<p>One decimal place → × 10; two places (like 0.25) → × 100; three places → × 1000. Choose it from the term with the most decimal places, and multiply the whole equation by that same power.</p>", "<p>Una cifra decimal → × 10; dos cifras (como 0.25) → × 100; tres cifras → × 1000. Se elige según el término con más decimales y se multiplica toda la ecuación por esa misma potencia.</p>"))}
{calc(t("Decimals on the calculator", "Decimales en la calculadora"), t(f"<p>To check x = 10 in 0.2x + 1 = 3: {T('.')} {T('2')} {T('×')} {T('1')} {T('0')} {T('+')} {T('1')} {T('enter')} shows 3, the same as the right side.</p>", f"<p>Para comprobar x = 10 en 0.2x + 1 = 3: {T('.')} {T('2')} {T('×')} {T('1')} {T('0')} {T('+')} {T('1')} {T('enter')} muestra 3, igual que el lado derecho.</p>"))}
{practica("p1", t("Practice 1 — A fraction", "Práctica 1 — Una fracción"), f"{fx('x', 2)} = 9", [("a", "x = 11"), ("b", "x = 4.5"), ("c", "x = 18")])}
{practica("p2", t("Practice 2 — Fraction and constant", "Práctica 2 — Fracción y constante"), f"{fx('x', 5)} + 2 = 6", [("a", "x = 4"), ("b", "x = 20"), ("c", "x = 40")])}
{practica("p3", t("Practice 3 — A decimal", "Práctica 3 — Un decimal"), "0.5x = 7", [("a", "x = 14"), ("b", "x = 3.5"), ("c", "x = 7")])}
{enlace(n, t("decimals", "decimales"), t("clearing decimals with a power of 10", "limpiar decimales con una potencia de 10"), t("Choose the power of 10 that clears all the decimals.", "Elija la potencia de 10 que elimina todos los decimales."))}'''

    s3 = f'''<p>{t("Sometimes, as you solve, the variables disappear and you are left with a false statement, like 5 = 9. That means no value of the variable can make the equation true: it is a <strong>contradiction</strong>, and the equation has <strong>no solution</strong>.", "A veces, al resolver, las variables desaparecen y queda una afirmación falsa, como 5 = 9. Eso significa que ningún valor de la variable puede hacer verdadera la ecuación: es una <strong>contradicción</strong> y la ecuación <strong>no tiene solución</strong>.")}</p>
{ejemplo(t("Example 4: solve 2x + 5 = 2x + 9", "Ejemplo 4: resuelva 2x + 5 = 2x + 9"),
  [("1", t("Subtract 2x from both sides.", "Restar 2x en ambos lados."), "5 = 9."),
   ("2", t("The variable is gone.", "La variable desapareció."), t("5 = 9 is false.", "Queda 5 = 9, que es falso.")),
   ("✓", t("Answer.", "Respuesta."), t("The equation has <strong>no solution</strong> (a contradiction).", "La ecuación <strong>no tiene solución</strong> (contradicción)."))])}'''

    s4 = f'''<p>{t("In other cases, the variables disappear and you are left with a statement that is always true, like 0 = 0. That means every value of the variable works: it is an <strong>identity</strong>, and the equation has <strong>infinitely many solutions</strong>.", "En otros casos, al resolver, las variables desaparecen y queda una afirmación siempre verdadera, como 0 = 0. Eso significa que cualquier valor de la variable funciona: es una <strong>identidad</strong> y la ecuación tiene <strong>infinitas soluciones</strong>.")}</p>
{ejemplo(t("Example 5: solve 3(x + 2) = 3x + 6", "Ejemplo 5: resuelva 3(x + 2) = 3x + 6"),
  [("1", t("Distribute on the left.", "Distribuir a la izquierda."), "3x + 6 = 3x + 6."),
   ("2", t("Subtract 3x from both sides.", "Restar 3x en ambos lados."), t("6 = 6, which is always true.", "6 = 6, que es siempre verdadero.")),
   ("✓", t("Answer.", "Respuesta."), t("The equation has <strong>infinitely many solutions</strong> (an identity).", "La ecuación tiene <strong>infinitas soluciones</strong> (identidad)."))])}
{tabla(t("Types of solution", "Tipos de solución"), t("Types of solution of a linear equation, by what is left when you solve it", "Tipos de solución de una ecuación lineal según el resultado al resolver"), [t("When you solve, you get…", "Al resolver queda…"), t("Type of solution", "Tipo de solución"), t("Meaning", "Significado")], tipos)}
{practica("p4", t("Practice 4 — Same x terms", "Práctica 4 — Las mismas x"), "2x + 3 = 2x + 8", [("a", t("No solution", "Sin solución")), ("b", t("One solution", "Una solución")), ("c", t("Infinitely many solutions", "Infinitas soluciones"))])}
{practica("p5", t("Practice 5 — Distribute first", "Práctica 5 — Distribuir primero"), "5(x + 1) = 5x + 5", [("a", t("No solution", "Sin solución")), ("b", t("One solution", "Una solución")), ("c", t("Infinitely many solutions", "Infinitas soluciones"))])}
{practica("p6", t("Practice 6 — An ordinary one", "Práctica 6 — Una común"), "3x + 1 = 7", [("a", t("No solution", "Sin solución")), ("b", t("One solution", "Una solución")), ("c", t("Infinitely many solutions", "Infinitas soluciones"))])}
{enlace(n, t("special-cases", "casos-especiales"), t("one, none, or infinitely many solutions?", "¿una, ninguna o infinitas soluciones?"), t("Recognize when the equation is a contradiction or an identity.", "Reconozca cuándo la ecuación es una contradicción o una identidad."))}'''

    secciones = [("s-" + t("fractions", "fracciones"), t("Clearing fractions: multiply by the LCM", "Limpiar fracciones: multiplicar por el MCM"), s1),
                 ("s-" + t("decimals", "decimales"), t("Clearing decimals: multiply by a power of 10", "Limpiar decimales: multiplicar por una potencia de 10"), s2),
                 ("s-" + t("no-solution", "sin-solucion"), t("A special case: no solution", "Caso especial: ecuación sin solución"), s3),
                 ("s-" + t("infinite", "infinitas"), t("A special case: infinitely many solutions", "Caso especial: infinitas soluciones"), s4)]

    SIN, UNA, INF = t("No solution", "Sin solución"), t("One solution", "Una solución"), t("Infinitely many solutions", "Infinitas soluciones")
    lesson = {"next": t("Lesson 5.1", "Lección 5.1"), "review": t("sections 1 to 4", "las secciones 1 a 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("x/2 means x divided by 2: undo it by multiplying, not adding.", "x/2 es x dividida entre 2: se deshace multiplicando, no sumando."), "b": t("Multiply both sides by 2; do not divide.", "Se multiplica por 2 en ambos lados; no se divide.")}, "right": "2 · 9 = 18.", "solution": t("Multiply both sides by 2: x = 18.", "Se multiplica por 2 en ambos lados: x = 18.")},
      "p2": {"ok": "b", "hints": {"a": t("After subtracting 2 you get x/5 = 4: you still have to multiply by 5.", "Al restar 2 queda x/5 = 4: falta multiplicar por 5."), "c": t("Multiply every term by 5, including the 2: x + 10 = 30.", "Multiplique cada término por 5, también el 2: x + 10 = 30.")}, "right": "x + 10 = 30, x = 20.", "solution": t("Multiply everything by 5: x + 10 = 30, so x = 20.", "Se multiplica todo por 5: x + 10 = 30, así que x = 20.")},
      "p3": {"ok": "a", "hints": {"b": t("Divide 7 by 0.5; do not multiply.", "Se divide 7 entre 0.5; no se multiplica."), "c": t("0.5x is half of x, so x is bigger than 7.", "0.5x es la mitad de x, así que x es mayor que 7.")}, "right": "5x = 70, x = 14.", "solution": t("Multiply by 10: 5x = 70, so x = 14.", "Se multiplica por 10: 5x = 70, así que x = 14.")},
      "p4": {"ok": "a", "hints": {"b": t("Subtract 2x from both sides: what is left?", "Reste 2x en ambos lados: ¿qué queda?"), "c": t("You get 3 = 8. Is that true?", "Queda 3 = 8. ¿Es verdadero?")}, "right": t("3 = 8 is false: a contradiction.", "3 = 8 es falso: contradicción."), "solution": t("Subtracting 2x leaves 3 = 8, which is false: no solution.", "Al restar 2x queda 3 = 8, que es falso: sin solución.")},
      "p5": {"ok": "c", "hints": {"a": t("Distribute first: 5x + 5 = 5x + 5.", "Primero distribuya: 5x + 5 = 5x + 5."), "b": t("After distributing, both sides are the same.", "Al distribuir, los dos lados son iguales.")}, "right": t("5 = 5 is always true: an identity.", "5 = 5 es siempre verdadero: identidad."), "solution": t("5x + 5 = 5x + 5 leaves 5 = 5: infinitely many solutions.", "5x + 5 = 5x + 5 deja 5 = 5: infinitas soluciones.")},
      "p6": {"ok": "b", "hints": {"a": t("The x does not disappear here.", "Aquí la x no desaparece."), "c": t("Only x = 2 works.", "Solo x = 2 funciona.")}, "right": "3x = 6, x = 2.", "solution": t("3x = 6, x = 2: one solution.", "3x = 6, x = 2: una solución.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Multiply the 3 by 2 too.", "El 3 también se multiplica por 2."), "c": t("x/2 = 4, so x = 8.", "x/2 = 4, así que x = 8."), "d": t("Check it: 20/2 + 3 = 13.", "Compruébelo: 20/2 + 3 = 13.")}, "solution": t("Multiply by 2: x + 6 = 14, x = 8.", "Por 2: x + 6 = 14, x = 8.")},
      "B": {"ok": "c", "hints": {"a": t("Check it: 6/2 + 6/4 = 4.5.", "Compruébelo: 6/2 + 6/4 = 4.5."), "b": t("3x = 24: divide by 3.", "3x = 24: divida entre 3."), "d": t("Check it: 1 + 0.5 = 1.5.", "Compruébelo: 1 + 0.5 = 1.5.")}, "solution": t("Multiply by 4: 2x + x = 24, 3x = 24, x = 8.", "Por 4: 2x + x = 24, 3x = 24, x = 8.")},
      "C": {"ok": "a", "hints": {"b": t("3 does not clear x/6.", "El 3 no elimina x/6."), "c": t("2 does not clear x/3.", "El 2 no elimina x/3."), "d": t("9 does not clear x/6.", "El 9 no elimina x/6.")}, "solution": t("The LCM of 3 and 6 is 6.", "El MCM de 3 y 6 es 6.")},
      "D": {"ok": "d", "hints": {"a": t("Multiply the 1 and the 3 by 10 too.", "El 1 y el 3 también se multiplican por 10."), "b": t("2x = 20: divide by 2.", "2x = 20: divida entre 2."), "c": t("Check it: 0.2(4) + 1 = 1.8.", "Compruébelo: 0.2(4) + 1 = 1.8.")}, "solution": t("By 10: 2x + 10 = 30, 2x = 20, x = 10.", "Por 10: 2x + 10 = 30, 2x = 20, x = 10.")},
      "E": {"ok": "c", "hints": {"a": t("0.25 has two decimal places.", "0.25 tiene dos cifras decimales."), "b": t("Use a power of 10.", "Use una potencia de 10."), "d": t("100 is enough: the most decimal places is two.", "Basta con 100: la mayor cantidad de cifras es dos.")}, "solution": "25x + 50 = 100."},
      "F": {"ok": "a", "hints": {"b": t("5 = 9 is false.", "5 = 9 es falso."), "c": t("5 = 9 is false, not always true.", "5 = 9 es falso, no siempre verdadero."), "d": t("The x disappeared: no value works.", "La x desapareció: ningún valor funciona.")}, "solution": t("A false statement: no solution.", "Afirmación falsa: sin solución.")},
      "G": {"ok": "d", "hints": {"a": t("0 = 0 is true.", "0 = 0 es verdadero."), "b": t("Every value works, not only one.", "Funciona todo valor, no solo uno."), "c": t("Every value works, not only 3.", "Funciona todo valor, no solo 3.")}, "solution": t("Always true: infinitely many solutions.", "Siempre verdadero: infinitas soluciones.")},
      "H": {"ok": "a", "hints": {"b": t("You found a value: x = 2.", "Se encontró un valor: x = 2."), "c": t("Only x = 2 works.", "Solo x = 2 funciona."), "d": t("x = 2 is one solution.", "x = 2 es una solución.")}, "solution": t("x = 2: one solution.", "x = 2: una solución.")}
     }}

    quiz = [
     ("A", t(f"Solve: {fx('x', 2)} + 3 = 7.", f"Resuelva: {fx('x', 2)} + 3 = 7."), [("a", "x = 5"), ("b", "x = 8"), ("c", "x = 2"), ("d", "x = 20")]),
     ("B", t(f"Solve: {fx('x', 2)} + {fx('x', 4)} = 6.", f"Resuelva: {fx('x', 2)} + {fx('x', 4)} = 6."), [("a", "x = 6"), ("b", "x = 24"), ("c", "x = 8"), ("d", "x = 2")]),
     ("C", t(f"To solve {fx('x', 3)} + {fx('x', 6)} = 2, what number should you multiply by?", f"Para resolver {fx('x', 3)} + {fx('x', 6)} = 2, ¿por cuánto conviene multiplicar?"), [("a", "6"), ("b", "3"), ("c", "2"), ("d", "9")]),
     ("D", t("Solve: 0.2x + 1 = 3.", "Resuelva: 0.2x + 1 = 3."), [("a", "x = 2"), ("b", "x = 20"), ("c", "x = 4"), ("d", "x = 10")]),
     ("E", t("To clear 0.25x + 0.5 = 1, what do you multiply by?", "Para limpiar 0.25x + 0.5 = 1, ¿por cuánto se multiplica?"), [("a", "10"), ("b", "25"), ("c", "100"), ("d", "1000")]),
     ("F", t("The equation 2x + 5 = 2x + 9 leads to 5 = 9. What type is it?", "La ecuación 2x + 5 = 2x + 9 lleva a 5 = 9. ¿Qué tipo es?"), [("a", SIN), ("b", UNA), ("c", INF), ("d", "x = 0")]),
     ("G", t("The equation 3(x + 1) = 3x + 3 leads to 0 = 0. What type is it?", "La ecuación 3(x + 1) = 3x + 3 lleva a 0 = 0. ¿Qué tipo es?"), [("a", SIN), ("b", UNA), ("c", "x = 3"), ("d", INF)]),
     ("H", t("The equation 4x + 2 = 10 leads to x = 2. What type is it?", "La ecuación 4x + 2 = 10 lleva a x = 2. ¿Qué tipo es?"), [("a", UNA), ("b", SIN), ("c", INF), ("d", t("None of the above", "Ninguna de las anteriores"))])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Clear fractions and decimals before you solve, and recognize equations with no solution or with infinitely many solutions.", "Limpie fracciones y decimales antes de resolver, y reconozca las ecuaciones sin solución o con infinitas soluciones."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Solve</strong> equations with fraction coefficients by clearing the fractions (multiply by the LCM).", "<strong>Resolver</strong> ecuaciones con coeficientes fraccionarios eliminando las fracciones (multiplicar por el MCM)."),
         t("<strong>Solve</strong> equations with decimal coefficients by multiplying by the right power of 10.", "<strong>Resolver</strong> ecuaciones con coeficientes decimales multiplicando por la potencia de 10 adecuada."),
         t("<strong>Identify</strong> an equation with no solution (a contradiction: 0 = 5).", "<strong>Identificar</strong> la ecuación sin solución (contradicción: 0 = 5)."),
         t("<strong>Identify</strong> an equation with infinitely many solutions (an identity: 0 = 0).", "<strong>Identificar</strong> la ecuación con infinitas soluciones (identidad: 0 = 0)."),
         t("<strong>Classify</strong> the result of an equation: one solution, no solution, or infinitely many.", "<strong>Clasificar</strong> el resultado de una ecuación: una solución, sin solución o infinitas soluciones.")],
        secciones,
        (t("Solve four equations with fraction coefficients (clear them with the LCM) and three with decimal coefficients (clear them with a power of 10). Then classify the type of solution of three special-case equations.",
           "Resuelva cuatro ecuaciones con coeficientes fraccionarios (limpiándolas con el MCM) y tres con coeficientes decimales (limpiándolas con una potencia de 10). Después clasifique el tipo de solución de tres ecuaciones de casos especiales."),
         t("A recipe uses 3/4 cup of rice per person plus 1/2 cup extra for the pot. Write and solve an equation to find for how many people you can cook with 5 cups of rice. Then a phone plan costs $0.15 per text plus $12.50 a month: how many texts can you send for $20?",
           "Una receta usa 3/4 de taza de arroz por persona más 1/2 taza extra para la olla. Escriba y resuelva una ecuación para hallar para cuántas personas puede cocinar con 5 tazas de arroz. Después, un plan de teléfono cuesta $0.15 por mensaje más $12.50 al mes: ¿cuántos mensajes puede enviar con $20?")),
        quiz,
        t("Self-check checklist for equations with fractions, decimals, and special cases", "Lista de autoevaluación para ecuaciones con fracciones, decimales y casos especiales"),
        t("Self-check checklist: skills for clearing fractions and decimals and classifying special cases", "Lista de autoevaluación: destrezas para limpiar fracciones y decimales y clasificar casos especiales"),
        [(t("Clearing fractions and decimals", "Eliminar fracciones y decimales"), t("I multiply every term by the LCM or by the right power of 10.", "Multiplico todos los términos por el MCM o por la potencia de 10 correcta."), t("I multiply, but I forget a term or use the wrong power.", "Multiplico, pero olvido algún término o uso una potencia incorrecta."), t("I do not find the LCM or the power of 10.", "No identifico el MCM ni la potencia de 10.")),
         (t("Solving the clean equation", "Resolver la ecuación limpia"), t("I solve the equation correctly and check the solution.", "Resuelvo correctamente la ecuación resultante y verifico la solución."), t("I solve it with a sign or operation mistake.", "La resuelvo con algún error de signo u operación."), t("I make mistakes solving the clean equation.", "Cometo errores al resolver la ecuación limpia.")),
         (t("Classifying special cases", "Clasificar casos especiales"), t("I tell one solution, no solution, and infinitely many apart and explain each one.", "Distingo una solución, sin solución e infinitas, y explico cada caso."), t("I classify the special cases with some mistakes.", "Clasifico con errores los casos especiales."), t("I do not tell a contradiction from an identity.", "No distingo contradicción de identidad."))],
        t("<p>This lesson closes Topic 4. You can now solve linear equations of any kind: with the five-step strategy, clearing fractions with the LCM and decimals with a power of 10, and recognizing the special cases of no solution (a contradiction) and infinitely many solutions (an identity).</p>\n<p>Topic 5 opens with <strong>Lesson 5.1 · Solving linear inequalities and graphing them on the number line</strong>. Inequalities are solved with the same steps as equations, with one new and crucial rule: when you multiply or divide by a negative number, the inequality sign flips. Everything you learned here is the direct base for that new topic.</p>",
          "<p>Con esta lección se cierra el Tema 4. Ya se resuelven ecuaciones lineales de cualquier tipo: con la estrategia de cinco pasos, limpiando fracciones con el MCM y decimales con una potencia de 10, y reconociendo los casos especiales de sin solución (contradicción) e infinitas soluciones (identidad).</p>\n<p>El Tema 5 abrirá con la <strong>Lección 5.1 · Resolver inecuaciones lineales y graficar en la recta numérica</strong>. Las inecuaciones se resuelven con los mismos pasos que las ecuaciones, con una sola regla nueva y crucial: al multiplicar o dividir por un número negativo, el signo de la desigualdad se invierte. Todo lo aprendido aquí será la base directa de ese nuevo tema.</p>"),
        ("5-1", ("", t("Lesson 5.1 · Solving linear inequalities and graphing them on the number line", "Lección 5.1 · Resolver inecuaciones lineales y graficar en la recta numérica"))),
        [(t("least common multiple (LCM)", "mínimo común múltiplo (MCM)"), t("The smallest number that all the denominators divide into. The LCM of 2 and 4 is 4.", "El número más pequeño que todos los denominadores dividen. El MCM de 2 y 4 es 4.")),
         (t("contradiction", "contradicción"), t("An equation that leads to something false, like 5 = 9: it has no solution.", "Una ecuación que lleva a algo falso, como 5 = 9: no tiene solución.")),
         (t("identity", "identidad"), t("An equation that leads to something always true, like 0 = 0: every value is a solution.", "Una ecuación que lleva a algo siempre verdadero, como 0 = 0: todo valor es solución.")),
         (t("power of 10", "potencia de 10"), t("10, 100, 1000…: multiplying by one of them moves the decimal point.", "10, 100, 1000…: multiplicar por una de ellas corre el punto decimal."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function P(){ return polVis(Array.prototype.slice.call(arguments)); }
/* Loose terms {c: fraction, v: "x" or ""}, to show each term multiplied */
function TT(c, v){ return {c: c.n !== undefined ? c : fr(c), v: v || ""}; }
function listaVis(l, modo){ if (!l.length) return "0"; return l.map(function(tt, i){ return tt.v ? termXVis(tt.c, modo, i === 0) : constVis(tt.c, modo, i === 0); }).join(""); }
function listaVoz(l){ if (!l.length) return "0"; return l.map(function(tt, i){ return tt.v ? termXVoz(tt.c, i === 0) : constVoz(tt.c, i === 0); }).join(""); }
function ecLista(i, d, modo){ return envuelve(listaVis(i, modo) + " = " + listaVis(d, modo), listaVoz(i) + T(" equals ", " es igual a ") + listaVoz(d)); }
function aLado(l){ var x = fr(0), k = fr(0); l.forEach(function(tt){ if (tt.v) x = fsum(x, tt.c); else k = fsum(k, tt.c); }); return L(x, k); }
function valLista(l, s){ return l.reduce(function(a, tt){ return fsum(a, tt.v ? fmul(tt.c, s) : tt.c); }, fr(0)); }
function porM(l, M){ return l.map(function(tt){ return TT(fmul(tt.c, fr(M)), tt.v); }); }
function denoms(l){ return l.map(function(tt){ return tt.c.d; }).filter(function(d){ return d > 1; }); }
function mcmLista(ds){ return ds.reduce(function(a, b){ return mcm(a, b); }, 1); }
function numTxt(c, modo){ return modo === "dec" && fDecimal(c) !== null ? fDecimal(c) : fracVis(c.n, c.d); }

/* Steps for an equation with no fractions left */
function pasosEntera(izq, der){
  var pasos = [], li = aLado(izq), ld = aLado(der);
  var combinar = izq.length > (fcero(li.x) ? 0 : 1) + (fcero(li.k) ? 0 : 1) || der.length > (fcero(ld.x) ? 0 : 1) + (fcero(ld.k) ? 0 : 1);
  if (combinar) pasos.push(T("Combine like terms on each side: ", "Se combinan los términos semejantes de cada lado: ") + ecHTML(li, ld) + ".");
  if (!fcero(ld.x)){
    var nx = fres(li.x, ld.x);
    pasos.push(T("Subtract ", "Se resta ") + ladoHTML(L(ld.x, 0)) + T(" from both sides to gather the x terms: ", " en ambos lados para reunir las x: ") + ecHTML(L(nx, li.k), L(0, ld.k)) + ".");
    li = L(nx, li.k); ld = L(0, ld.k);
  }
  if (fcero(li.x)) return {pasos: pasos, especial: true};
  if (!fcero(li.k)){
    var nk = fres(ld.k, li.k);
    pasos.push((li.k.n > 0 ? T("Subtract " + fTxt(li.k) + " from both sides: ", "Se resta " + fTxt(li.k) + " en ambos lados: ") : T("Add " + fTxt(fneg(li.k)) + " to both sides: ", "Se suma " + fTxt(fneg(li.k)) + " en ambos lados: ")) + ecHTML(L(li.x, 0), L(0, nk)) + ".");
    li = L(li.x, 0); ld = L(0, nk);
  }
  var sol = fdiv(ld.k, li.x);
  if (!figual(li.x, fr(1))) pasos.push(T("Divide both sides by " + fTxt(li.x) + ": ", "Se divide entre " + fTxt(li.x) + " en ambos lados: ") + xIgual(sol, "dec") + ".");
  return {pasos: pasos, sol: sol};
}
function explicaProductos(l, M, modo){
  return l.map(function(tt, i){
    var a = fr(Math.abs(tt.c.n), tt.c.d), dentro = tt.v ? termXVis(a, modo, true) : numTxt(a, modo);
    if (i === 0 && tt.c.n < 0) return M + " · (−" + dentro + ")";
    return (i === 0 ? "" : (tt.c.n < 0 ? " − " : " + ")) + M + " · " + (tt.c.d > 1 && modo !== "dec" ? "(" + dentro + ")" : dentro);
  }).join("");
}

/* ============ Equations with fractions and with decimals ============ */
function ecFraccion(){
  var tp = aleatorio(1, 4), a, b, n, izq, der, M, s;
  if (tp === 1){ a = elige([2, 3, 4, 5, 6]); s = a * elige([-3, -2, -1, 1, 2, 3, 4, 5]); b = nz(); izq = [TT(fr(1, a), "x"), TT(b)]; der = [TT(fsum(fr(s, a), fr(b)))]; }
  else if (tp === 2){ var p = elige([[2, 4], [2, 3], [3, 6], [4, 6], [2, 5], [3, 4]]); a = p[0]; b = p[1]; M = mcm(a, b); s = M * elige([-2, -1, 1, 2, 3]);
    izq = [TT(fr(1, a), "x"), TT(fr(1, b), "x")]; der = [TT(fsum(fr(s, a), fr(s, b)))]; }
  else if (tp === 3){ a = elige([3, 4, 5]); n = elige([2, 3]); if (n === a) n = 2; s = a * elige([-2, -1, 1, 2, 3, 4]); b = aleatorio(1, 9);
    izq = [TT(fr(n, a), "x"), TT(-b)]; der = [TT(fres(fr(n * s, a), fr(b)))]; }
  else { var q = elige([[2, 3], [3, 4], [2, 5], [4, 6], [2, 6]]); a = q[0]; b = q[1]; M = mcm(a, b); s = M * elige([-2, -1, 1, 2, 3]); var k = nz();
    izq = [TT(fr(1, a), "x"), TT(k)]; der = [TT(fr(1, b), "x"), TT(fres(fsum(fr(s, a), fr(k)), fr(s, b)))]; }
  return {izq: izq, der: der, s: fr(s), modo: "frac"};
}
function decimalAzar(k){ var d = Math.pow(10, k), n; do { n = aleatorio(1, 3 * d); } while (n % 10 === 0); return fr(n, d); }
function ecDecimal(){
  var tp = aleatorio(1, 3), izq, der, s = fr(elige([-4, -2, -1, 1, 2, 3, 4, 5, 6, 8, 10, 12]));
  if (Math.random() < 0.25) s = fr(elige([-3, 1, 3, 5, 7]), 2);
  if (tp === 1){ var a = decimalAzar(aleatorio(1, 2)), b = fr(aleatorio(1, 9)); izq = [TT(a, "x"), TT(b)]; der = [TT(fsum(fmul(a, s), b))]; }
  else if (tp === 2){ var a2 = decimalAzar(2), b2 = decimalAzar(1); izq = [TT(a2, "x"), TT(fneg(b2))]; der = [TT(fres(fmul(a2, s), b2))]; }
  else { var a3 = fsum(fr(1), decimalAzar(1)), c3 = decimalAzar(1), b3 = decimalAzar(aleatorio(1, 2)); if (figual(a3, c3)) a3 = fsum(a3, fr(1));
    izq = [TT(a3, "x"), TT(b3)]; der = [TT(c3, "x"), TT(fres(fsum(fmul(a3, s), b3), fmul(c3, s)))]; }
  return {izq: izq, der: der, s: s, modo: "dec"};
}
function potenciaNecesaria(e){
  var k = 0;
  e.izq.concat(e.der).forEach(function(tt){ var j = 0; while (fmul(tt.c, fr(Math.pow(10, j))).d !== 1 && j < 6) j++; if (j > k) k = j; });
  return k;
}
function pasosLimpiar(e){
  var pasos = [], M, todos = e.izq.concat(e.der);
  if (e.modo === "frac"){
    var ds = denoms(todos), unicos = ds.filter(function(d, i){ return ds.indexOf(d) === i; });
    M = mcmLista(ds);
    pasos.push(unicos.length === 1 ? T("The only denominator is " + unicos[0] + ": multiply everything by " + M + ".", "El único denominador es " + unicos[0] + ": se multiplica todo por " + M + ".")
                                   : T("The denominators are " + yLista(unicos) + ". The LCM is " + M + ": the smallest number they all divide into.", "Los denominadores son " + yLista(unicos) + ". El MCM es " + M + ": el número más pequeño que todos dividen."));
  } else {
    var k = potenciaNecesaria(e); M = Math.pow(10, k);
    pasos.push(T("The term with the most decimals has " + k + (k === 1 ? " decimal place" : " decimal places") + ": multiply everything by " + M + ".", "El término con más decimales tiene " + k + (k === 1 ? " cifra decimal" : " cifras decimales") + ": se multiplica todo por " + M + "."));
  }
  pasos.push(T("Multiply <strong>every term on both sides</strong> by ", "Se multiplica <strong>cada término de ambos lados</strong> por ") + M + ": " + auto(explicaProductos(e.izq, M, e.modo) + " = " + explicaProductos(e.der, M, e.modo)) + ".");
  var i2 = porM(e.izq, M), d2 = porM(e.der, M);
  pasos.push((e.modo === "frac" ? T("You get an equation with no fractions: ", "Queda una ecuación sin fracciones: ") : T("You get an equation with no decimals: ", "Queda una ecuación sin decimales: ")) + ecLista(i2, d2, "frac") + ".");
  pasos = pasos.concat(pasosEntera(i2, d2).pasos);
  pasos.push("<strong>" + T("Check", "Verificar") + "</strong> " + T("in the original equation: with x = " + numTxt(e.s, e.modo) + ", both sides equal " + numTxt(valLista(e.izq, e.s), e.modo) + ".", "en la ecuación original: con x = " + numTxt(e.s, e.modo) + ", los dos lados valen " + numTxt(valLista(e.izq, e.s), e.modo) + "."));
  pasos.push('<span class="veredicto">' + T("Solution: ", "Solución: ") + xIgual(e.s, e.modo) + "</span>");
  return {pasos: pasos, M: M, i2: i2, d2: d2};
}
function creaPasoAPaso(pre, lista, genera){
  var S = {lista: lista, pasos: [], visto: 0};
  function texto(e){ return (listaVis(e.izq, e.modo) + " = " + listaVis(e.der, e.modo)).replace(/<span class="fracc"><span class="fa">(.*?)<\/span><span class="fb2">(.*?)<\/span><\/span>/g, "$1/$2").replace(/<[^>]+>/g, ""); }
  function llena(){ var sel = $(pre + "-sel"); sel.innerHTML = ""; S.lista.forEach(function(e, i){ var o = document.createElement("option"); o.value = i; o.textContent = texto(e); sel.appendChild(o); }); }
  function prepara(){
    var e = S.lista[+$(pre + "-sel").value];
    S.pasos = pasosLimpiar(e).pasos; S.visto = 0;
    $(pre + "-expr").innerHTML = '<span class="grande">' + ecLista(e.izq, e.der, e.modo) + "</span>";
    pinta();
  }
  function pinta(){
    $(pre + "-pasos").innerHTML = S.pasos.slice(0, S.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === S.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
    var b = $(pre + "-sig"); b.disabled = S.visto >= S.pasos.length; $(pre + "-todo").disabled = b.disabled;
    b.textContent = S.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
  }
  $(pre + "-sel").addEventListener("change", prepara);
  $(pre + "-sig").addEventListener("click", function(){ if (S.visto < S.pasos.length){ S.visto++; pinta(); } });
  $(pre + "-todo").addEventListener("click", function(){ S.visto = S.pasos.length; pinta(); });
  $(pre + "-azar").addEventListener("click", function(){ S.lista.push(genera()); llena(); $(pre + "-sel").value = S.lista.length - 1; prepara(); });
  llena(); prepara();
  return S;
}
var EJ_FRAC = [
  {izq: [TT(fr(1, 2), "x"), TT(3)], der: [TT(7)], s: fr(8), modo: "frac"},
  {izq: [TT(fr(1, 2), "x"), TT(fr(1, 4), "x")], der: [TT(6)], s: fr(8), modo: "frac"},
  {izq: [TT(fr(2, 3), "x"), TT(-1)], der: [TT(5)], s: fr(9), modo: "frac"},
  {izq: [TT(fr(1, 3), "x"), TT(2)], der: [TT(fr(1, 2), "x")], s: fr(12), modo: "frac"}
];
var EJ_DEC = [
  {izq: [TT(fr(2, 10), "x"), TT(1)], der: [TT(3)], s: fr(10), modo: "dec"},
  {izq: [TT(fr(25, 100), "x"), TT(fr(-5, 10))], der: [TT(fr(15, 10))], s: fr(8), modo: "dec"},
  {izq: [TT(fr(15, 10), "x"), TT(fr(3, 10))], der: [TT(fr(1), "x"), TT(fr(33, 10))], s: fr(6), modo: "dec"}
];

function genMCM(){
  var e = ecFraccion(), ds = denoms(e.izq.concat(e.der)), M = mcmLista(ds), unicos = ds.filter(function(d, i){ return ds.indexOf(d) === i; });
  var prod = unicos.reduce(function(a, b){ return a * b; }, 1), mayor = Math.max.apply(null, ds), suma = unicos.reduce(function(a, b){ return a + b; }, 0);
  var o = [], pc = {}, usadas = {};
  function mete(v, msg){ var k = "m" + v; if (usadas[k]) return; usadas[k] = 1; o.push({html: String(v), clave: k}); if (msg) pc[k] = msg; }
  mete(M);
  mete(prod, T("Multiplying by the product also clears the fractions, but it gives bigger numbers than you need: the LCM is smaller.", "Multiplicar por el producto también limpia las fracciones, pero da números más grandes de lo necesario: el MCM es más pequeño."));
  mete(mayor, T("The largest denominator does not always work: every denominator has to divide into it.", "El mayor denominador no siempre sirve: tiene que ser divisible entre todos los denominadores."));
  mete(suma, T("You do not add the denominators: look for the smallest number they all divide into.", "Los denominadores no se suman: se busca el número más pequeño que todos dividen."));
  mete(2 * M, T("That works, but it is not the smallest: the LCM is half of it.", "Funciona, pero no es el más pequeño: el MCM es la mitad."));
  mete(M + 1, T("Not every denominator divides into that number.", "No todos los denominadores dividen a ese número."));
  return {enun: T("To clear the fractions of ", "Para limpiar las fracciones de ") + ecLista(e.izq, e.der, "frac") + T(", what number should you multiply by?", ", ¿por qué número conviene multiplicar?"),
    opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("The LCM of the denominators is " + M + ".", "El MCM de los denominadores es " + M + "."), mal: T("The LCM of the denominators is " + M + ": the smallest number they all divide into.", "El MCM de los denominadores es " + M + ": el número más pequeño que todos dividen.")};
}
function genQueda(){
  var e, M;
  do { e = ecFraccion(); M = mcmLista(denoms(e.izq.concat(e.der))); } while (!e.izq.concat(e.der).some(function(tt){ return tt.c.d === 1; }));
  var bien = [porM(e.izq, M), porM(e.der, M)];
  var soloFr = function(l){ return l.map(function(tt){ return tt.c.d > 1 ? TT(fmul(tt.c, fr(M)), tt.v) : tt; }); };
  var numMal = function(l){ return l.map(function(tt){ return tt.c.d > 1 ? TT(fr(tt.c.n * M), tt.v) : TT(fmul(tt.c, fr(M)), tt.v); }); };
  var o = [{html: ecLista(bien[0], bien[1], "frac"), clave: "b"}], pc = {};
  o.push({html: ecLista(soloFr(e.izq), soloFr(e.der), "frac"), clave: "f"}); pc.f = T("You forgot to multiply the terms that have no fraction.", "Faltó multiplicar los términos que no tienen fracción.");
  o.push({html: ecLista(porM(e.izq, M), e.der, "frac"), clave: "i"}); pc.i = T("Only one side was multiplied: the balance is broken.", "Se multiplicó solo un lado: la balanza se desequilibra.");
  o.push({html: ecLista(numMal(e.izq), numMal(e.der), "frac"), clave: "n"}); pc.n = T("When you multiply a fraction by " + M + ", divide by its denominator too. For example, " + M + " · (x/2) = " + (M / 2) + "x.", "Al multiplicar una fracción por " + M + " hay que dividir entre su denominador. Por ejemplo, " + M + " · (x/2) = " + (M / 2) + "x.");
  var vistos = {}; o = o.filter(function(x){ if (vistos[x.html]) return false; vistos[x.html] = 1; return true; });
  return {enun: T("When you multiply each term of ", "Al multiplicar cada término de ") + ecLista(e.izq, e.der, "frac") + T(" by " + M + ", what equation do you get?", " por " + M + ", ¿qué ecuación queda?"),
    opciones: o, correcta: "b", porClave: pc, pista: T("Multiply every term, on both sides, by " + M + ".", "Multiplique cada término, de los dos lados, por " + M + "."),
    bien: T("Every term, on both sides, is multiplied by " + M + ".", "Cada término, de los dos lados, se multiplica por " + M + "."), mal: T("You get ", "Queda ") + ecLista(bien[0], bien[1], "frac") + "."};
}
function genResolverFr(){
  var e = ecFraccion(), M = mcmLista(denoms(e.izq.concat(e.der))), pistas = [];
  var soloFr = function(l){ return l.map(function(tt){ return tt.c.d > 1 ? TT(fmul(tt.c, fr(M)), tt.v) : tt; }); };
  var r = resuelve(aLado(soloFr(e.izq)), aLado(soloFr(e.der)));
  if (r.tipo === "una") pistas.push({v: r.x, msg: T("It looks like you forgot to multiply a term with no fraction by " + M + ".", "Parece que olvidó multiplicar por " + M + " algún término sin fracción.")});
  var R = pasosLimpiar(e);
  return {enun: T("Solve ", "Resuelva ") + ecLista(e.izq, e.der, "frac") + ".",
    solucion: T("Multiply everything by " + M + ": ", "Se multiplica todo por " + M + ": ") + ecLista(R.i2, R.d2, "frac") + T(", and x = ", ", y x = ") + numTxt(e.s, "frac") + ".",
    evalua: function(txt){ return evaluaNumero(txt, e.s, pistas); }};
}
function genPotencia(){
  var e = ecDecimal(), k = potenciaNecesaria(e), M = Math.pow(10, k), o = [{html: String(M), clave: "p" + M}], pc = {};
  [10, 100, 1000, 10000].forEach(function(v){ if (v !== M){ o.push({html: String(v), clave: "p" + v}); pc["p" + v] = v < M ? T("With " + v + " some decimals would still be left.", "Con " + v + " todavía quedarían decimales.") : T("It works, but it gives bigger numbers than you need.", "Funciona, pero da números más grandes de lo necesario."); } });
  return {enun: T("To clear the decimals of ", "Para limpiar los decimales de ") + ecLista(e.izq, e.der, "dec") + T(", what power of 10 should you multiply by?", ", ¿por qué potencia de 10 conviene multiplicar?"),
    opciones: o.slice(0, 4), correcta: "p" + M, porClave: pc, enOrden: true,
    bien: T("The term with the most decimals has " + k + (k === 1 ? " decimal place" : " decimal places") + ", so multiply by " + M + ".", "El término con más decimales tiene " + k + (k === 1 ? " cifra" : " cifras") + ", así que se multiplica por " + M + "."),
    mal: T("Look at the term with the most decimal places: it has " + k + ", so multiply by " + M + ".", "Se mira el término con más cifras decimales: tiene " + k + ", así que se multiplica por " + M + ".")};
}
function genResolverDec(){
  var e = ecDecimal(), R = pasosLimpiar(e);
  return {enun: T("Solve ", "Resuelva ") + ecLista(e.izq, e.der, "dec") + ".",
    solucion: T("Multiply everything by " + R.M + ": ", "Se multiplica todo por " + R.M + ": ") + ecLista(R.i2, R.d2, "frac") + T(", and x = ", ", y x = ") + numTxt(e.s, "dec") + ".",
    evalua: function(txt){ return evaluaNumero(txt, e.s, []); }};
}

/* ============ MODULE 3 · special cases ============ */
function pintaCE(){
  var a = leeEntero($("ce-a").value), b = leeEntero($("ce-b").value), c = leeEntero($("ce-c").value), d = leeEntero($("ce-d").value), av = $("ce-aviso");
  if ([a, b, c, d].some(function(v){ return v === null || Math.abs(v) > 20; }) || a === 0){
    av.className = "caja-aviso visible"; av.textContent = T("Type whole numbers from −20 to 20 (a cannot be 0).", "Escriba números enteros entre −20 y 20 (a distinto de 0).");
    $("ce-ec").innerHTML = ""; $("ce-tabla").innerHTML = ""; $("ce-salida").innerHTML = ""; return;
  }
  av.className = "caja-aviso"; av.textContent = "";
  var der = L(c, d);
  $("ce-ec").innerHTML = auto(menosV(a) + "(" + polVis([tm(1, "x"), tm(b)]) + ") = " + ladoVis(der));
  var h = '<table class="comparar"><caption>' + T("The value of each side for several values of x", "Valor de cada lado para varios valores de x") + '</caption><thead><tr><th scope="col">x</th><th scope="col">' + T("Left side", "Lado izquierdo") + '</th><th scope="col">' + T("Right side", "Lado derecho") + '</th><th scope="col">' + T("Do they match?", "¿Coinciden?") + "</th></tr></thead><tbody>";
  [-2, -1, 0, 1, 2, 3].forEach(function(x){
    var vi = a * (x + b), vd = c * x + d, si = vi === vd;
    h += "<tr><td>" + menosV(x) + "</td><td>" + menosV(vi) + "</td><td>" + menosV(vd) + '</td><td class="' + (si ? "si" : "no") + '">' + (si ? T("Yes", "Sí") : "No") + "</td></tr>";
  });
  $("ce-tabla").innerHTML = h + "</tbody></table>";
  var li = L(a, a * b), r = resuelve(li, der), s = '<div class="linea">' + T("Distribute: ", "Se distribuye: ") + ecHTML(li, der) + ".</div>";
  if (r.tipo === "una"){
    s += '<div class="linea">' + T("Subtract ", "Se resta ") + ladoHTML(L(c, 0)) + T(" from both sides: ", " en ambos lados: ") + ecHTML(L(a - c, a * b), L(0, d)) + ".</div>";
    s += '<div class="linea veredicto">' + T("One solution: ", "Una solución: ") + xIgual(r.x, "frac") + ". " + (fent(r.x) && r.x.n >= -2 && r.x.n <= 3 ? T("In the table it is the only row with “Yes.”", "En la tabla es la única fila con «Sí».") : T("It is outside the table, so no row matches: try that value.", "Está fuera de la tabla, por eso ninguna fila coincide: pruebe con ese valor.")) + "</div>";
  } else {
    s += '<div class="linea">' + T("Subtract ", "Se resta ") + ladoHTML(L(c, 0)) + T(" from both sides and the x terms disappear: you get ", " en ambos lados y las x desaparecen: queda ") + menosV(a * b) + " = " + menosV(d) + ".</div>";
    s += r.tipo === "ninguna" ? '<div class="linea veredicto">' + T("That is false: the equation has no solution. No row in the table matches, and no other value will.", "Eso es falso: la ecuación no tiene solución. En la tabla ninguna fila coincide, y ningún otro valor lo hará.") + "</div>"
                              : '<div class="linea veredicto">' + T("That is always true: the equation has infinitely many solutions. Every row in the table matches, and so does any other value.", "Eso es siempre verdadero: la ecuación tiene infinitas soluciones. En la tabla coinciden todas las filas, y cualquier otro valor también.") + "</div>";
  }
  $("ce-salida").innerHTML = s;
}
function ponCE(v){ ["ce-a", "ce-b", "ce-c", "ce-d"].forEach(function(id, i){ $(id).value = v[i]; }); pintaCE(); }
function genCasos(){
  var tp = aleatorio(1, 6), vis, tipo, resto, a = aleatorio(2, 7), b = nz(), m = aleatorio(2, 6), p = nz(), c, d;
  if (tp === 1){ d = b + elige([1, 2, 3, -2, -4]); vis = auto(P(tm(a, "x"), tm(b)) + " = " + P(tm(a, "x"), tm(d))); tipo = "ninguna"; resto = menosV(b) + " = " + menosV(d); }
  else if (tp === 2){ vis = auto(m + "(" + P(tm(1, "x"), tm(p)) + ") = " + P(tm(m, "x"), tm(m * p))); tipo = "infinitas"; resto = menosV(m * p) + " = " + menosV(m * p); }
  else if (tp === 3){ d = m * p + elige([1, -1, 2, 3]); vis = auto(m + "(" + P(tm(1, "x"), tm(p)) + ") = " + P(tm(m, "x"), tm(d))); tipo = "ninguna"; resto = menosV(m * p) + " = " + menosV(d); }
  else if (tp === 4){ c = aleatorio(1, 4); vis = auto(P(tm(a, "x"), tm(b), tm(c, "x")) + " = " + P(tm(b), tm(a + c, "x"))); tipo = "infinitas"; resto = menosV(b) + " = " + menosV(b); }
  else if (tp === 5){ do { c = aleatorio(1, 8); } while (c === a); d = nz(); vis = auto(P(tm(a, "x"), tm(b)) + " = " + P(tm(c, "x"), tm(d))); tipo = "una"; resto = "x = " + fTxt(fr(d - b, a - c)); }
  else { do { c = aleatorio(1, 8); } while (c === m); d = nz(); vis = auto(m + "(" + P(tm(1, "x"), tm(p)) + ") = " + P(tm(c, "x"), tm(d))); tipo = "una"; resto = "x = " + fTxt(fr(d - m * p, m - c)); }
  var exp = tipo === "una" ? T("The x terms do not disappear: you get " + resto + ".", "Las x no desaparecen: queda " + resto + ".") :
            T("When you gather the x terms, they disappear and you get " + resto, "Al reunir las x, desaparecen y queda " + resto) + (tipo === "ninguna" ? T(", which is false: a contradiction.", ", que es falso: contradicción.") : T(", which is always true: an identity.", ", que es siempre verdadero: identidad."));
  return {enun: T("How many solutions does ", "¿Cuántas soluciones tiene ") + vis + T(" have?", "?"), enOrden: true,
    opciones: [{html: T("One solution", "Una solución"), clave: "una"}, {html: T("No solution", "Sin solución"), clave: "ninguna"}, {html: T("Infinitely many solutions", "Infinitas soluciones"), clave: "infinitas"}],
    correcta: tipo, porClave: {}, pista: T("Gather the x terms on one side. Do they disappear? If so, is what is left true or false?", "Reúna las x en un lado. ¿Desaparecen? Si es así, ¿lo que queda es verdadero o falso?"), bien: exp, mal: exp};
}

/* ============ Start ============ */
creaPasoAPaso("lf", EJ_FRAC, ecFraccion);
OMR("p1", genMCM);
OMR("p2", genQueda);
creaPracticaLibre("p3", genResolverFr);
creaPasoAPaso("ld", EJ_DEC, ecDecimal);
OMR("p4", genPotencia);
creaPracticaLibre("p5", genResolverDec);
["ce-a", "ce-b", "ce-c", "ce-d"].forEach(function(id){ $(id).addEventListener("input", pintaCE); });
$("ce-ej1").addEventListener("click", function(){ ponCE([2, 3, 2, 9]); });
$("ce-ej2").addEventListener("click", function(){ ponCE([3, 2, 3, 6]); });
$("ce-ej3").addEventListener("click", function(){ ponCE([2, 1, 1, 5]); });
pintaCE();
OMR("p6", genCasos);
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}"

def paso_a_paso(pre):
    return f'''      <div class="panel">
        <div class="campos"><div class="campo"><label for="{pre}-sel">{t("Equation", "Ecuación")}</label><select id="{pre}-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig"></button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="{pre}-azar">{t("Another one at random", "Otra al azar")}</button></div>
      </div>
      <div class="fraccion-grande" id="{pre}-expr"></div>
      <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>'''

def campo(i, etiqueta, valor):
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="text" class="corto" id="{i}" value="{valor}"></div>'

def libre(pid, titulo, nota):
    return B.libre(pid, titulo, t("Value of x", "Valor de x"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + nota + '</p>\n        <div class="fila-btn">', 1)

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("fractions", "fracciones"), t("Clearing fractions with the LCM", "Limpiar fracciones con el MCM"),
      f'''      <p>{t("An equation with fractions becomes much easier if you clear the fractions first. To do that, multiply <strong>every term on both sides</strong> by the least common multiple (LCM) of the denominators.", "Una ecuación con fracciones se vuelve mucho más fácil si primero se eliminan las fracciones. Para eso se multiplican <strong>todos los términos de ambos lados</strong> por el mínimo común múltiplo (MCM) de los denominadores.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{paso_a_paso("lf")}
{P.atencion(t("Multiply every term:", "Multiplicar todos los términos:"), t("the LCM multiplies each term, including the ones with no fraction. Forgetting a term is the most common mistake when you clear fractions.", "el MCM multiplica cada término, incluidos los que no tienen fracción. Olvidar un término es el error más frecuente al limpiar fracciones."))}
{B.om("p1", t("Practice: what do you multiply by?", "Practique: ¿por cuánto se multiplica?"))}
{B.om("p2", t("Practice: what equation do you get?", "Practique: ¿qué ecuación queda?"))}
{libre("p3", t("Practice: solve the equation", "Practique: resuelva la ecuación"), t("Type the number; it can be negative or a fraction like 3/2.", "Escriba el número; puede ser negativo o una fracción como 3/2."))}'''),
     (t("decimals", "decimales"), t("Clearing decimals with a power of 10", "Limpiar decimales con una potencia de 10"),
      f'''      <p>{t("With decimals the idea is the same: multiply every term by 10, 100, or 1000 to turn the decimals into whole numbers. Choose the power from the term with the <strong>most decimal places</strong>.", "Con decimales se aplica la misma idea: se multiplican todos los términos por 10, 100 o 1000 para convertir los decimales en enteros. La potencia se elige según el término con <strong>más cifras decimales</strong>.")}</p>
      <table class="reglas">
        <caption>{t("Which power of 10 to use", "Qué potencia de 10 usar")}</caption>
        <thead><tr><th scope="col">{t("Most decimal places", "Más cifras decimales")}</th><th scope="col">{t("Example", "Ejemplo")}</th><th scope="col">{t("Multiply by", "Se multiplica por")}</th></tr></thead>
        <tbody><tr><td>{t("One", "Una")}</td><td>0.2</td><td>10</td></tr><tr><td>{t("Two", "Dos")}</td><td>0.25</td><td>100</td></tr><tr><td>{t("Three", "Tres")}</td><td>0.125</td><td>1000</td></tr></tbody>
      </table>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{paso_a_paso("ld")}
{B.om("p4", t("Practice: which power of 10?", "Practique: ¿qué potencia de 10?"))}
{libre("p5", t("Practice: solve the equation", "Practique: resuelva la ecuación"), t("Type the number; it can be a decimal, like 2.5.", "Escriba el número; puede ser decimal, como 2.5."))}'''),
     (t("special-cases", "casos-especiales"), t("One, none, or infinitely many solutions?", "¿Una, ninguna o infinitas soluciones?"),
      f'''      <p>{t("Sometimes, as you solve, the variables disappear. What is left decides the type of equation:", "A veces, al resolver, las variables desaparecen. Lo que queda decide el tipo de ecuación:")}</p>
      <table class="reglas">
        <caption>{t("Types of solution of a linear equation", "Tipos de solución de una ecuación lineal")}</caption>
        <thead><tr><th scope="col">{t("When you solve, you get…", "Al resolver queda…")}</th><th scope="col">{t("Type of solution", "Tipo de solución")}</th><th scope="col">{t("Meaning", "Significado")}</th></tr></thead>
        <tbody>
          <tr><td>{t("x = a number", "x = un número")}</td><td>{t("One solution", "Una solución")}</td><td>{t("Exactly one value makes the equation true.", "Un único valor hace verdadera la ecuación.")}</td></tr>
          <tr><td>{t("Something false (5 = 9)", "Algo falso (5 = 9)")}</td><td>{t("No solution", "Sin solución")}</td><td>{t("No value works (a contradiction).", "Ningún valor funciona (contradicción).")}</td></tr>
          <tr><td>{t("Something true (6 = 6)", "Algo verdadero (6 = 6)")}</td><td>{t("Infinitely many solutions", "Infinitas soluciones")}</td><td>{t("Every value works (an identity).", "Todo valor funciona (identidad).")}</td></tr>
        </tbody>
      </table>
      <h3>{t("Explorer: try several values of x", "Explorador: pruebe varios valores de x")}</h3>
      <p>{t("Build an equation of the form a(x + b) = cx + d. The table tries six values of x and marks where the two sides match.", "Arme una ecuación de la forma a(x + b) = cx + d. La tabla prueba seis valores de x y marca dónde coinciden los dos lados.")}</p>
      <div class="panel">
        <div class="campos">{campo("ce-a", "a", 3)}{campo("ce-b", "b", 2)}{campo("ce-c", "c", 3)}{campo("ce-d", "d", 6)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="ce-ej1">{t("Example with no solution", "Ejemplo sin solución")}</button><button type="button" class="btn-sec" id="ce-ej2">{t("Example with infinitely many", "Ejemplo con infinitas")}</button><button type="button" class="btn-sec" id="ce-ej3">{t("Example with one", "Ejemplo con una")}</button></div>
      </div>
{P.aviso("ce-aviso")}
      <div class="estado"><span class="grande" id="ce-ec"></span></div>
      <div class="tabla-scroll" id="ce-tabla"></div>
{P.salida("ce-salida")}
{B.om("p6", t("Practice: how many solutions does it have?", "Practique: ¿cuántas soluciones tiene?"))}''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Ecuaciones con coeficientes fraccionarios, decimales y casos especiales")
