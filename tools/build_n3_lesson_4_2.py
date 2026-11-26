"""Level 3 · Lesson 4.2 · Solving linear equations — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "4-2"
TEMA = ("Linear algebra", "Álgebra lineal")
TIT = ("Solving linear equations: properties of equality and variables on both sides", "Resolver ecuaciones lineales: propiedades de igualdad y variables en ambos lados")
SCRIPTS = ("/math/radicals.js", "/math/linear.js")

def leccion():
    n = N
    pasos5 = [t("Distribute to clear the parentheses, if there are any.", "Distribuir los paréntesis, si los hay."),
              t("Combine like terms on each side.", "Combinar los términos semejantes de cada lado."),
              t("Move the variables to one side of the equal sign.", "Pasar las variables a un solo lado del igual."),
              t("Isolate the variable with the properties of equality.", "Aislar la variable con las propiedades de igualdad."),
              t("Check by substituting the solution into the original equation.", "Verificar sustituyendo la solución en la ecuación original.")]
    s1 = f'''<p>{t("In Lesson 4.1 you learned to simplify and evaluate algebraic expressions. When two expressions are joined by an equal sign, you get an <strong>equation</strong>: 2x + 3 = 11. Unlike an expression, an equation has a <strong>solution</strong>, the value of the variable that makes it true, and this lesson teaches you to find it step by step.",
"En la Lección 4.1 se aprendió a simplificar y evaluar expresiones algebraicas. Cuando dos expresiones se unen con un signo de igual, se forma una <strong>ecuación</strong>: 2x + 3 = 11. A diferencia de una expresión, una ecuación tiene una <strong>solución</strong> —el valor de la variable que la hace verdadera—, y esta lección enseña a encontrarla de forma metódica.")}</p>
<p>{t("An equation is like a balance scale: what is on the left of the equal sign weighs the same as what is on the right. To keep it balanced, whatever you do to one side you must do to the other. That is the idea of the <strong>properties of equality</strong>: you can add, subtract, multiply, or divide both sides by the same number.",
"Una ecuación es como una balanza en equilibrio: lo que está a la izquierda del signo igual pesa lo mismo que lo que está a la derecha. Para mantener el equilibrio, cualquier operación que se haga en un lado debe hacerse igual en el otro. Esa es la idea de las <strong>propiedades de igualdad</strong>: se puede sumar, restar, multiplicar o dividir ambos lados por el mismo número.")}</p>
<p>{t("The goal is always the same: get the variable alone on one side of the equal sign (<strong>isolate</strong> it). Each operation you use undoes something around the variable, using the <strong>inverse operation</strong>.", "El objetivo siempre es el mismo: dejar la variable sola de un lado del igual (<strong>aislarla</strong>). Cada operación que se aplica busca deshacer lo que rodea a la variable, usando la <strong>operación inversa</strong>.")}</p>
{enlace(n, t("balance", "balanza"), t("the equation as a balance scale", "la ecuación como una balanza"), t("Whatever you do to one side, you do to the other.", "Lo que se hace en un lado se hace en el otro."))}'''

    s2 = f'''<p>{t("Undo the operations in the reverse of the PEMDAS order: first the addition or subtraction, then the multiplication or division.", "Se deshacen las operaciones en orden inverso al de PEMDAS: primero la suma o resta, luego la multiplicación o división.")}</p>
{ejemplo(t("Example 1: solve x + 7 = 15", "Ejemplo 1: resuelva x + 7 = 15"),
  [("1", t("Undo “+ 7.”", "Deshacer «+ 7»."), t("Subtract 7 from both sides: x + 7 − 7 = 15 − 7.", "Se resta 7 en ambos lados: x + 7 − 7 = 15 − 7.")),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 8</strong>")])}
{ejemplo(t("Example 2: solve 2x + 5 = 13", "Ejemplo 2: resuelva 2x + 5 = 13"),
  [("1", t("Subtract 5 from both sides.", "Restar 5 en ambos lados."), "2x = 8."),
   ("2", t("Divide both sides by 2.", "Dividir entre 2 en ambos lados."), "x = 4."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 4</strong>")])}
{caja("tip", t("Reverse order", "Orden inverso"), t("<p>In 2x + 5, the variable is first multiplied by 2 and then 5 is added. To undo it, go backward: first remove the + 5 (subtract), and last the × 2 (divide).</p>", "<p>En 2x + 5, la variable está primero multiplicada por 2 y luego se le suma 5. Para deshacerlo se procede al revés: primero se quita el + 5 (resta) y al final el × 2 (división).</p>"))}'''

    s3 = f'''<p>{t("For any linear equation, this ordered list is a reliable guide.", "Para cualquier ecuación lineal, esta lista ordenada funciona como una guía confiable.")}</p>
<ol>{"".join(f"<li>{p}</li>" for p in pasos5)}</ol>
{practica("p1", t("Practice 1 — One step", "Práctica 1 — Un paso"), "x − 6 = 10", [("a", "x = 4"), ("b", "x = −16"), ("c", "x = 16")])}
{practica("p2", t("Practice 2 — Divide", "Práctica 2 — Dividir"), "4x = 28", [("a", "x = 7"), ("b", "x = 24"), ("c", "x = 32")])}
{practica("p3", t("Practice 3 — Two steps", "Práctica 3 — Dos pasos"), "3x − 2 = 13", [("a", "x = 11"), ("b", "x = 5"), ("c", "x = 15")])}
{enlace(n, t("steps", "pasos"), t("one-step and multi-step equations", "ecuaciones de uno y varios pasos"), t("Use the five-step strategy to isolate the variable.", "Aplique la estrategia de cinco pasos para aislar la variable."))}'''

    s4 = f'''<p>{t("When the variable appears on both sides of the equal sign, first gather all the variables on one side (by subtracting one of them from both sides) and all the constants on the other. Then isolate the variable as usual.", "Cuando la variable aparece en los dos lados del igual, primero se reúnen todas las variables en un solo lado (restando una de ellas en ambos lados) y todas las constantes en el otro. Después se aísla la variable como siempre.")}</p>
{ejemplo(t("Example 3: solve 5x + 2 = 3x + 10", "Ejemplo 3: resuelva 5x + 2 = 3x + 10"),
  [("1", t("Subtract 3x from both sides.", "Restar 3x en ambos lados."), "2x + 2 = 10."),
   ("2", t("Subtract 2 from both sides.", "Restar 2 en ambos lados."), "2x = 8."),
   ("3", t("Divide by 2.", "Dividir entre 2."), "x = 4."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 4</strong>")])}
{ejemplo(t("Example 4: solve 7x + 1 = 2x + 16", "Ejemplo 4: resuelva 7x + 1 = 2x + 16"),
  [("1", t("Subtract 2x from both sides.", "Restar 2x en ambos lados."), "5x + 1 = 16."),
   ("2", t("Subtract 1 from both sides.", "Restar 1 en ambos lados."), "5x = 15."),
   ("3", t("Divide by 5.", "Dividir entre 5."), "x = 3."),
   ("✓", t("Answer.", "Respuesta."), "<strong>x = 3</strong>")])}
{caja("tip", t("A useful trick", "Truco práctico"), t("<p>Move the variables to the side where the coefficient stays positive. In Example 3, subtracting 3x (the smaller one) leaves 2x, which is positive, so you avoid working with a negative coefficient.</p>", "<p>Conviene mover las variables al lado donde el coeficiente quede positivo. En el Ejemplo 3, restar 3x (el menor) deja 2x positivo, lo que evita trabajar con un coeficiente negativo.</p>"))}
{practica("p4", t("Practice 4 — Both sides", "Práctica 4 — Ambos lados"), "6x = 2x + 12", [("a", "x = 3"), ("b", "x = 6"), ("c", "x = 12")])}
{practica("p5", t("Practice 5 — Gather the x terms", "Práctica 5 — Reunir las x"), "5x + 1 = 3x + 9", [("a", "x = 5"), ("b", "x = 2"), ("c", "x = 4")])}
{practica("p6", t("Practice 6 — With subtraction", "Práctica 6 — Con resta"), "8x − 5 = 6x + 7", [("a", "x = 1"), ("b", "x = 6"), ("c", "x = 12")])}
{enlace(n, t("both-sides", "ambos-lados"), t("variables on both sides", "variables en ambos lados"), t("Gather the variable terms on one side of the equation.", "Reúna los términos con variable en un solo lado de la ecuación."))}'''

    s5 = f'''<p>{t("You check every solution by substituting it into the original equation. If both sides give the same value, the solution is right.", "Toda solución se comprueba sustituyéndola en la ecuación original. Si ambos lados dan el mismo valor, la solución es correcta.")}</p>
{ejemplo(t("Example 5: check that x = 4 solves 2x + 1 = 9", "Ejemplo 5: compruebe que x = 4 resuelve 2x + 1 = 9"),
  [("1", t("Substitute.", "Sustituir."), "2(4) + 1."),
   ("2", t("Work it out.", "Calcular."), "8 + 1 = 9."),
   ("✓", t("Answer.", "Respuesta."), t("The left side gives 9, the same as the right side: x = 4 is correct.", "El lado izquierdo da 9, igual que el derecho: la solución x = 4 es correcta."))])}
{caja("ojo", t("Checking is not optional", "Verificar no es opcional"), t("<p>Substituting the solution is the best way to catch a sign mistake made along the way. One minute of checking keeps you from losing all the points on a problem.</p>", "<p>Sustituir la solución es la mejor forma de detectar un error de signo cometido durante el proceso. Un minuto de verificación evita perder todos los puntos del problema.</p>"))}
{enlace(n, t("check", "verificar"), t("checking the solution", "verificar la solución"), t("Substitute the solution and check that both sides match.", "Sustituya la solución y compruebe que los dos lados coinciden."))}'''

    secciones = [("s-" + t("balance", "balanza"), t("The equation as a balance scale", "La ecuación como una balanza"), s1),
                 ("s-" + t("isolate", "aislar"), t("Isolating the variable: one-step and multi-step equations", "Aislar la variable: ecuaciones de uno y varios pasos"), s2),
                 ("s-" + t("five-steps", "cinco-pasos"), t("The five-step strategy", "La estrategia de cinco pasos"), s3),
                 ("s-" + t("both-sides", "ambos-lados"), t("Variables on both sides", "Variables en ambos lados"), s4),
                 ("s-" + t("check", "verificar"), t("Checking the solution", "Verificar la solución"), s5)]

    lesson = {"next": t("Lesson 4.3", "Lección 4.3"), "review": t("sections 2 to 4", "las secciones 2 a 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("To undo “− 6,” add 6; do not subtract it.", "Para deshacer «− 6» se suma 6; no se resta."), "b": t("Add 6 to both sides: 10 + 6.", "Sume 6 en ambos lados: 10 + 6.")}, "right": t("Add 6 to both sides: x = 16.", "Se suma 6 en ambos lados: x = 16."), "solution": "x − 6 + 6 = 10 + 6, x = 16."},
      "p2": {"ok": "a", "hints": {"b": t("4x means 4 times x: undo it by dividing.", "4x significa 4 por x: se deshace dividiendo."), "c": t("4x means 4 times x: undo it by dividing.", "4x significa 4 por x: se deshace dividiendo.")}, "right": "28 ÷ 4 = 7.", "solution": t("Divide both sides by 4: x = 7.", "Se divide entre 4 en ambos lados: x = 7.")},
      "p3": {"ok": "b", "hints": {"a": t("Undo the − 2 first (add 2), then divide by 3.", "Primero se deshace el − 2 (sumando 2) y después se divide entre 3."), "c": t("After adding 2 you get 3x = 15: you still have to divide.", "Al sumar 2 queda 3x = 15: todavía falta dividir.")}, "right": "3x = 15, x = 5.", "solution": t("Add 2: 3x = 15. Divide by 3: x = 5.", "Se suma 2: 3x = 15. Se divide entre 3: x = 5.")},
      "p4": {"ok": "a", "hints": {"b": t("Subtract 2x from both sides: 4x = 12.", "Reste 2x en ambos lados: 4x = 12."), "c": t("After subtracting 2x you get 4x = 12: divide by 4.", "Al restar 2x queda 4x = 12: divida entre 4.")}, "right": "4x = 12, x = 3.", "solution": "6x − 2x = 12, 4x = 12, x = 3."},
      "p5": {"ok": "c", "hints": {"a": t("Check by substituting: 5(5) + 1 = 26, but 3(5) + 9 = 24.", "Compruébelo: 5(5) + 1 = 26, pero 3(5) + 9 = 24."), "b": t("After subtracting 3x: 2x + 1 = 9. Then subtract 1.", "Al restar 3x: 2x + 1 = 9. Después reste 1.")}, "right": "2x + 1 = 9, 2x = 8, x = 4.", "solution": "5x − 3x + 1 = 9, 2x = 8, x = 4."},
      "p6": {"ok": "b", "hints": {"a": t("To undo “− 5,” add 5: 7 + 5 = 12.", "Para deshacer «− 5» se suma 5: 7 + 5 = 12."), "c": t("You get 2x = 12: you still have to divide by 2.", "Queda 2x = 12: falta dividir entre 2.")}, "right": "2x − 5 = 7, 2x = 12, x = 6.", "solution": "8x − 6x − 5 = 7, 2x = 12, x = 6."}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("Subtract 7; do not add it.", "Se resta 7, no se suma."), "b": t("15 − 7 = 8.", "15 − 7 = 8."), "c": t("15 − 7 is positive.", "15 − 7 es positivo.")}, "solution": "x = 15 − 7 = 8."},
      "B": {"ok": "a", "hints": {"b": t("Subtract 5 first: 2x = 8.", "Primero reste 5: 2x = 8."), "c": t("2x = 8, so x = 8 ÷ 2.", "2x = 8, así que x = 8 ÷ 2."), "d": t("Check it: 2(6) + 5 = 17.", "Compruébelo: 2(6) + 5 = 17.")}, "solution": "2x = 8, x = 4."},
      "C": {"ok": "b", "hints": {"a": t("Check it: 5(6) + 2 = 32, 3(6) + 10 = 28.", "Compruébelo: 5(6) + 2 = 32, 3(6) + 10 = 28."), "c": t("2x + 2 = 10, so 2x = 8.", "2x + 2 = 10, así que 2x = 8."), "d": t("2x = 8: divide by 2.", "2x = 8: divida entre 2.")}, "solution": "2x + 2 = 10, 2x = 8, x = 4."},
      "D": {"ok": "c", "hints": {"a": t("Add 3 to both sides: 2x = 10.", "Sume 3 en ambos lados: 2x = 10."), "b": t("2x = 10, so x = 5.", "2x = 10, así que x = 5."), "d": t("2x = 10: you still have to divide.", "2x = 10: falta dividir.")}, "solution": "2x − 3 = 7, 2x = 10, x = 5."},
      "E": {"ok": "b", "hints": {"a": t("5x + 1 = 16, so 5x = 15.", "5x + 1 = 16, así que 5x = 15."), "c": t("Subtract 1, do not add it.", "Se resta 1, no se suma."), "d": t("5x = 15: divide by 5.", "5x = 15: divida entre 5.")}, "solution": "5x + 1 = 16, 5x = 15, x = 3."},
      "F": {"ok": "a", "hints": {"b": t("Dividing by 18 does not undo anything.", "Dividir entre 18 no deshace nada."), "c": t("The x is inside the parentheses.", "La x está dentro del paréntesis."), "d": t("The 2 is inside the parentheses: distribute first.", "El 2 está dentro del paréntesis: distribuya primero.")}, "solution": t("Distribute first: 3x + 6 = 18.", "Primero se distribuye: 3x + 6 = 18.")},
      "G": {"ok": "d", "hints": {"a": t("That puts more x terms on the left side.", "Eso pone más x en el lado izquierdo."), "b": t("First gather the x terms.", "Primero se reúnen las x."), "c": t("First gather the x terms on one side.", "Primero se reúnen las x en un lado.")}, "solution": t("Subtract 2x from both sides: 3x + 4 = 13.", "Se resta 2x en ambos lados: 3x + 4 = 13.")},
      "H": {"ok": "a", "hints": {"b": t("That changes the equation; it does not check it.", "Eso cambia la ecuación; no la verifica."), "c": t("That is a step for solving, not for checking.", "Eso es un paso para resolver, no para verificar."), "d": t("You can always check by substituting.", "Siempre se puede verificar sustituyendo.")}, "solution": t("2(4) + 1 = 9: both sides match.", "2(4) + 1 = 9: los dos lados coinciden.")}
     }}

    quiz = [
     ("A", t("Solve: x + 7 = 15.", "Resuelva: x + 7 = 15."), [("a", "x = 22"), ("b", "x = 7"), ("c", "x = −8"), ("d", "x = 8")]),
     ("B", t("Solve: 2x + 5 = 13.", "Resuelva: 2x + 5 = 13."), [("a", "x = 4"), ("b", "x = 9"), ("c", "x = 3"), ("d", "x = 6")]),
     ("C", t("Solve: 5x + 2 = 3x + 10.", "Resuelva: 5x + 2 = 3x + 10."), [("a", "x = 6"), ("b", "x = 4"), ("c", "x = 3"), ("d", "x = 2")]),
     ("D", t("Solve: 4x − 3 = 2x + 7.", "Resuelva: 4x − 3 = 2x + 7."), [("a", "x = 2"), ("b", "x = 4"), ("c", "x = 5"), ("d", "x = 10")]),
     ("E", t("Solve: 7x + 1 = 2x + 16.", "Resuelva: 7x + 1 = 2x + 16."), [("a", "x = 5"), ("b", "x = 3"), ("c", "x = 17"), ("d", "x = 15")]),
     ("F", t("For 3(x + 2) = 18, what is a good first step?", "Para 3(x + 2) = 18, ¿cuál es un buen primer paso?"), [("a", t("Distribute: 3x + 6 = 18", "Distribuir: 3x + 6 = 18")), ("b", t("Divide everything by 18", "Dividir todo entre 18")), ("c", t("Subtract x", "Restar x")), ("d", t("Add 2", "Sumar 2"))]),
     ("G", t("For 5x + 4 = 2x + 13, what is a good first step?", "Para 5x + 4 = 2x + 13, ¿cuál es un buen primer paso?"), [("a", t("Add 5x", "Sumar 5x")), ("b", t("Divide by 4", "Dividir entre 4")), ("c", t("Subtract 13", "Restar 13")), ("d", t("Subtract 2x from both sides", "Restar 2x en ambos lados"))]),
     ("H", t("How do you check that x = 4 solves 2x + 1 = 9?", "¿Cómo se verifica que x = 4 resuelve 2x + 1 = 9?"), [("a", t("Substitute x = 4 into the equation", "Sustituir x = 4 en la ecuación")), ("b", t("Add 4 to both sides", "Sumar 4 a ambos lados")), ("c", t("Divide by 2", "Dividir entre 2")), ("d", t("It cannot be checked", "No se puede verificar"))])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Treat the equation as a balance scale and follow five steps to find the value of the variable.", "Trate la ecuación como una balanza y siga cinco pasos para encontrar el valor de la variable."),
        ("✏️", t("No calculator needed", "Sin calculadora")),
        [t("<strong>Solve</strong> linear equations in one variable with the properties of equality.", "<strong>Resolver</strong> ecuaciones lineales en una variable aplicando las propiedades de igualdad."),
         t("<strong>Solve</strong> one-step and multi-step equations by isolating the variable.", "<strong>Resolver</strong> ecuaciones de uno y de varios pasos aislando la variable."),
         t("<strong>Solve</strong> equations with variables on both sides.", "<strong>Resolver</strong> ecuaciones con variables en ambos lados."),
         t("<strong>Follow</strong> an ordered five-step strategy.", "<strong>Seguir</strong> una estrategia ordenada de cinco pasos."),
         t("<strong>Check</strong> the solution by substituting it into the original equation.", "<strong>Verificar</strong> la solución sustituyéndola en la ecuación original.")],
        secciones,
        (t("Solve four equations with two or three steps, four equations with variables on both sides, and two equations with parentheses that you must distribute first. Check two given solutions by substitution. Check every solution before you count the exercise as done.",
           "Resuelva cuatro ecuaciones de dos o tres pasos, cuatro ecuaciones con variables en ambos lados y dos ecuaciones con paréntesis que requieran distribuir primero. Verifique por sustitución dos soluciones dadas. Compruebe cada solución antes de dar el ejercicio por bueno."),
         t("A taxi charges $3 to start plus $2 per mile, and a ride share charges $7 to start plus $1.50 per mile. Write an equation to find the number of miles at which both cost the same, solve it, and check your answer. Which would you choose for a 5-mile trip?",
           "Un taxi cobra $3 de arranque más $2 por milla, y un servicio de viajes compartidos cobra $7 de arranque más $1.50 por milla. Escriba una ecuación para hallar con cuántas millas los dos cuestan lo mismo, resuélvala y verifique la respuesta. ¿Cuál elegiría para un viaje de 5 millas?")),
        quiz,
        t("Self-check checklist for solving linear equations", "Lista de autoevaluación para resolver ecuaciones lineales"),
        t("Self-check checklist: skills for solving and checking linear equations", "Lista de autoevaluación: destrezas para resolver y verificar ecuaciones lineales"),
        [(t("Properties of equality", "Propiedades de igualdad"), t("I do the same operation to both sides and choose the right inverse operation.", "Aplico la misma operación a ambos lados y elijo la operación inversa adecuada."), t("I use the properties with some mistakes.", "Aplico las propiedades con errores ocasionales."), t("I work on only one side of the equation.", "Opero solo un lado de la ecuación.")),
         (t("Variables on both sides", "Variables en ambos lados"), t("I gather the variables on the side that keeps the coefficient positive.", "Reúno las variables en el lado que deja el coeficiente positivo."), t("I gather the variables with sign mistakes.", "Reúno las variables con errores de signo."), t("I do not gather the variables on one side.", "No reúno las variables en un solo lado.")),
         (t("Isolating and checking", "Aislar y verificar"), t("I isolate the variable without sign mistakes and check by substituting into the original equation.", "Aíslo la variable sin errores de signo y verifico sustituyendo en la ecuación original."), t("I isolate the variable, but I do not always check.", "Aíslo la variable, pero no siempre verifico."), t("I make sign mistakes and do not check the solution.", "Cometo errores de signo y no verifico la solución."))],
        t("<p>You learned to solve linear equations by treating the equation as a balance scale: whatever you do to one side, you do to the other. With the five-step strategy you solved multi-step equations and equations with variables on both sides, and you checked each solution by substitution.</p>\n<p>In <strong>Lesson 4.3 · Equations with fractions, decimals, and special cases</strong> you will use the same steps on equations that are easier after you “clean them up”: you will clear fractions by multiplying by the least common multiple and decimals by multiplying by a power of 10. You will also meet equations with a special result: no solution or infinitely many solutions.</p>",
          "<p>En esta lección se aprendió a resolver ecuaciones lineales tratando la ecuación como una balanza: lo que se hace a un lado se hace al otro. Con la estrategia de cinco pasos se resolvieron ecuaciones de varios pasos y con variables en ambos lados, y se comprobó cada solución por sustitución.</p>\n<p>En la <strong>Lección 4.3 · Ecuaciones con coeficientes fraccionarios, decimales y casos especiales</strong> se aplicarán estos mismos pasos a ecuaciones que primero conviene «limpiar»: se eliminarán las fracciones multiplicando por el mínimo común múltiplo y los decimales multiplicando por una potencia de 10. Además, se descubrirán ecuaciones con un resultado especial: sin solución o con infinitas soluciones.</p>"),
        ("4-3", ("", t("Lesson 4.3 · Equations with fractions, decimals, and special cases", "Lección 4.3 · Ecuaciones con coeficientes fraccionarios, decimales y casos especiales"))),
        [(t("equation", "ecuación"), t("Two expressions joined by an equal sign, like 2x + 3 = 11.", "Dos expresiones unidas por un signo de igual, como 2x + 3 = 11.")),
         (t("solution", "solución"), t("The value of the variable that makes the equation true.", "El valor de la variable que hace verdadera la ecuación.")),
         (t("inverse operation", "operación inversa"), t("The operation that undoes another: subtraction undoes addition, and division undoes multiplication.", "La operación que deshace a otra: la resta deshace la suma y la división deshace la multiplicación.")),
         (t("isolate", "aislar"), t("To get the variable alone on one side of the equal sign.", "Dejar la variable sola en un lado del signo igual."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function P(){ return polVis(Array.prototype.slice.call(arguments)); }
function sumaResta(k){ return k > 0 ? T("Subtract " + k + " from both sides", "Se resta " + k + " en ambos lados") : T("Add " + (-k) + " to both sides", "Se suma " + (-k) + " en ambos lados"); }

/* ============ MODULE 1 · the balance scale ============ */
var BZ = {a: 1, x: 1, k: 0, r: 0, hist: []};
function nuevaBZ(e){
  if (!e){ do { e = [aleatorio(1, 3), aleatorio(1, 5), aleatorio(1, 7)]; } while (e[0] * e[1] + e[2] > 18); }
  BZ.a = e[0]; BZ.x = e[1]; BZ.k = e[2]; BZ.r = e[0] * e[1] + e[2]; BZ.hist = [];
  $("bz-aviso").className = "caja-aviso"; $("bz-aviso").textContent = "";
  $("bz-fb").className = "fb"; $("bz-fb").innerHTML = "";
  pintaBZ();
}
function objetosSVG(cx, yBase, cajas, circulos){
  var s = "", items = [], i;
  for (i = 0; i < cajas; i++) items.push("c"); for (i = 0; i < circulos; i++) items.push("o");
  var porFila = 6, ancho = 32;
  items.forEach(function(tp, j){
    var fila = Math.floor(j / porFila), col = j % porFila, enFila = Math.min(porFila, items.length - fila * porFila);
    var x = cx - (enFila * ancho) / 2 + col * ancho + ancho / 2, y = yBase - 18 - fila * 34;
    if (tp === "c") s += '<rect x="' + (x - 15) + '" y="' + (y - 15) + '" width="30" height="30" rx="4" fill="#bf360c"/><text x="' + x + '" y="' + (y + 7) + '" text-anchor="middle" font-size="18" font-weight="700" fill="#fff">x</text>';
    else s += '<circle cx="' + x + '" cy="' + y + '" r="13" fill="#fff8e1" stroke="#5c3900" stroke-width="2"/><text x="' + x + '" y="' + (y + 6) + '" text-anchor="middle" font-size="15" font-weight="700" fill="#5c3900">1</text>';
  });
  return s;
}
function cuenta(n, uno, varios){ return n + " " + (n === 1 ? uno : varios); }
function pintaBZ(){
  var izq = BZ.a * BZ.x + BZ.k, dif = izq - BZ.r, tp = dif > 0 ? 1 : (dif < 0 ? -1 : 0), dy = 22 * tp;
  var yl = 170 + dy, yr = 170 - dy;
  var lab = T("Balance scale: on the left " + cuenta(BZ.a, "box", "boxes") + " x and " + cuenta(BZ.k, "circle", "circles") + "; on the right " + cuenta(BZ.r, "circle", "circles") + ". " + (tp === 0 ? "It is balanced." : (tp > 0 ? "It tips to the left." : "It tips to the right.")),
              "Balanza: a la izquierda " + cuenta(BZ.a, "caja", "cajas") + " x y " + cuenta(BZ.k, "círculo", "círculos") + "; a la derecha " + cuenta(BZ.r, "círculo", "círculos") + ". " + (tp === 0 ? "Está en equilibrio." : (tp > 0 ? "Se inclina hacia la izquierda." : "Se inclina hacia la derecha.")));
  var s = '<svg class="balanza" viewBox="0 0 600 320" role="img" aria-label="' + lab + '">';
  s += '<polygon points="300,175 270,300 330,300" fill="#9e9e9e"/><rect x="230" y="298" width="140" height="12" rx="4" fill="#757575"/>';
  s += '<line x1="110" y1="' + yl + '" x2="490" y2="' + yr + '" stroke="#424242" stroke-width="8" stroke-linecap="round"/><circle cx="300" cy="170" r="9" fill="#424242"/>';
  [[110, yl], [490, yr]].forEach(function(p){
    s += '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + (p[0] - 80) + '" y2="' + (p[1] + 60) + '" stroke="#757575" stroke-width="2"/>';
    s += '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + (p[0] + 80) + '" y2="' + (p[1] + 60) + '" stroke="#757575" stroke-width="2"/>';
    s += '<rect x="' + (p[0] - 100) + '" y="' + (p[1] + 58) + '" width="200" height="10" rx="5" fill="#616161"/>';
  });
  s += objetosSVG(110, yl + 58, BZ.a, BZ.k) + objetosSVG(490, yr + 58, 0, BZ.r) + "</svg>";
  $("bz-svg").innerHTML = s;
  $("bz-ec").innerHTML = ecHTML(L(BZ.a, BZ.k), L(0, BZ.r)) + (tp === 0 ? "" : ' <span class="nota">' + T("(out of balance!)", "(¡desequilibrada!)") + "</span>");
  var eq = tp === 0;
  $("bz-ambos").disabled = !eq || BZ.k === 0 || BZ.r === 0;
  $("bz-uno").disabled = !eq || BZ.k === 0;
  $("bz-dividir").disabled = !eq || BZ.k !== 0 || BZ.a === 1;
  $("bz-dividir").textContent = BZ.a > 1 ? T("Split into " + BZ.a + " equal groups", "Repartir en " + BZ.a + " grupos iguales") : T("Split into equal groups", "Repartir en grupos iguales");
  $("bz-deshacer").disabled = !BZ.hist.length;
  if (eq && BZ.a === 1 && BZ.k === 0){ $("bz-fb").className = "fb bien"; $("bz-fb").innerHTML = TX.bien + T("The box is alone and the scale is still balanced: x = " + BZ.r + ".", "La caja quedó sola y la balanza sigue en equilibrio: x = " + BZ.r + "."); }
}
function accionBZ(tipo){
  var av = $("bz-aviso"), fb = $("bz-fb");
  av.className = "caja-aviso"; av.textContent = ""; fb.className = "fb"; fb.innerHTML = "";
  BZ.hist.push([BZ.a, BZ.k, BZ.r]);
  if (tipo === "ambos"){ BZ.k--; BZ.r--; fb.className = "fb bien"; fb.innerHTML = T("You took 1 away from both sides: the scale is still balanced.", "Se quitó 1 en ambos lados: la balanza sigue en equilibrio."); }
  else if (tipo === "uno"){ BZ.k--; av.className = "caja-aviso visible"; av.textContent = T("The balance is broken! You took a circle off the left side only, and now that side weighs less. Whatever you do to one side, you do to the other. Press “Undo.”", "¡Se rompió el equilibrio! Quitó un círculo solo de la izquierda y ahora ese lado pesa menos. Lo que se hace en un lado se hace en el otro. Pulse «Deshacer»."); }
  else if (tipo === "dividir"){ var a = BZ.a; BZ.r = BZ.r / a; BZ.a = 1; fb.className = "fb bien"; fb.innerHTML = T("Each side was split into " + a + " equal groups and one group was kept: that is dividing both sides by " + a + ".", "Cada lado se repartió en " + a + " grupos iguales y se dejó uno: eso es dividir entre " + a + " en ambos lados."); }
  pintaBZ();
}
function deshacerBZ(){
  var h = BZ.hist.pop(); if (!h) return;
  BZ.a = h[0]; BZ.k = h[1]; BZ.r = h[2];
  $("bz-aviso").className = "caja-aviso"; $("bz-aviso").textContent = ""; $("bz-fb").className = "fb"; $("bz-fb").innerHTML = "";
  pintaBZ();
}
function genPrimerPaso(){
  var tp = aleatorio(1, 5), a = aleatorio(2, 9), b = aleatorio(2, 12), c = aleatorio(1, 20), ec, bueno, malos, exp;
  while (b === a) b = aleatorio(2, 12);
  var RA = function(k){ return T("Subtract " + k + " from both sides", "Restar " + k + " en ambos lados"); }, SA = function(k){ return T("Add " + k + " to both sides", "Sumar " + k + " en ambos lados"); };
  var DA = function(k){ return T("Divide both sides by " + k, "Dividir entre " + k + " en ambos lados"); }, MA = function(k){ return T("Multiply both sides by " + k, "Multiplicar por " + k + " en ambos lados"); };
  if (tp === 1){ ec = ecHTML(L(1, b), L(0, c)); bueno = RA(b); malos = [[SA(b), T("Adding makes it worse: + " + b + " is undone by subtracting.", "Sumar lo empeora: «+ " + b + "» se deshace restando.")], [T("Subtract " + b + " from the left side only", "Restar " + b + " solo del lado izquierdo"), T("Whatever you do to one side, you do to the other.", "Lo que se hace en un lado se hace en el otro.")], [DA(b), T("The " + b + " is added, not multiplied.", "El " + b + " se suma, no multiplica.")]]; exp = T("To undo “+ " + b + ",” subtract " + b + " from both sides.", "Para deshacer «+ " + b + "» se resta " + b + ", en los dos lados."); }
  else if (tp === 2){ ec = ecHTML(L(1, -b), L(0, c)); bueno = SA(b); malos = [[RA(b), T("Subtracting makes it worse: − " + b + " is undone by adding.", "Restar lo empeora: «− " + b + "» se deshace sumando.")], [T("Add " + b + " to the right side only", "Sumar " + b + " solo del lado derecho"), T("Whatever you do to one side, you do to the other.", "Lo que se hace en un lado se hace en el otro.")], [MA(b), T("The " + b + " is subtracted, not divided.", "El " + b + " se resta, no divide.")]]; exp = T("To undo “− " + b + ",” add " + b + " to both sides.", "Para deshacer «− " + b + "» se suma " + b + ", en los dos lados."); }
  else if (tp === 3){ ec = ecHTML(L(a, 0), L(0, a * c)); bueno = DA(a); malos = [[RA(a), T(a + "x means " + a + " times x: it is undone by dividing.", a + "x significa " + a + " por x: se deshace dividiendo.")], [MA(a), T("Multiplying makes it worse.", "Multiplicar lo empeora.")], [T("Divide the left side only by " + a, "Dividir entre " + a + " solo del lado izquierdo"), T("Whatever you do to one side, you do to the other.", "Lo que se hace en un lado se hace en el otro.")]]; exp = T(a + "x means " + a + " times x: undo it by dividing both sides by " + a + ".", a + "x significa " + a + " por x: se deshace dividiendo entre " + a + "."); }
  else if (tp === 4){ ec = ecHTML(L(fr(1, a), 0), L(0, c)); bueno = MA(a); malos = [[DA(a), T("Dividing again makes it worse.", "Dividir otra vez lo empeora.")], [RA(a), T("x is divided by " + a + ": undo it by multiplying.", "La x está dividida entre " + a + ": se deshace multiplicando.")], [SA(a), T("x is divided by " + a + ": undo it by multiplying.", "La x está dividida entre " + a + ": se deshace multiplicando.")]]; exp = T("x/" + a + " means x divided by " + a + ": undo it by multiplying both sides by " + a + ".", "x/" + a + " significa x dividida entre " + a + ": se deshace multiplicando por " + a + "."); }
  else { ec = ecHTML(L(a, b), L(0, a * aleatorio(1, 5) + b)); bueno = RA(b); malos = [[DA(b), T("The " + b + " is added, not multiplied.", "El " + b + " se suma, no multiplica.")], [RA(a), T("The " + a + " multiplies x: it is undone by dividing, at the end.", "El " + a + " multiplica a la x: se deshace dividiendo, al final.")], [SA(b), T("+ " + b + " is undone by subtracting.", "«+ " + b + "» se deshace restando.")]]; exp = T("In reverse order: first remove the addition (subtract " + b + "), and divide by " + a + " at the end.", "En orden inverso: primero se quita la suma (restando " + b + ") y al final se divide entre " + a + "."); }
  var o = [{html: bueno, clave: "b"}], pc = {};
  malos.forEach(function(m, i){ o.push({html: m[0], clave: "m" + i}); pc["m" + i] = m[1]; });
  return {enun: T("To solve ", "Para resolver ") + ec + T(", what is the first step?", ", ¿cuál es el primer paso?"), opciones: o, correcta: "b", porClave: pc, bien: exp, mal: exp};
}

/* ============ Equations of several kinds (modules 2 and 4) ============ */
function ecuacionForma(f){
  var sol = aleatorio(-6, 9), a, b, c, d, e, pasos = [], A, K, vis, izq;
  if (sol === 0) sol = 4;
  if (f === 1){
    a = elige([2, 3, 4, 5, 6, 7, -2, -3]); b = nz(); c = a * sol + b; A = a; K = b;
    vis = auto(P(tm(a, "x"), tm(b)) + " = " + menosV(c)); izq = function(v){ return a * v + b; };
  } else if (f === 2){
    a = elige([2, 3, 4, 5, -2, -3]); b = nz(); c = a * (sol + b); A = a; K = a * b;
    vis = auto(menosV(a) + "(" + P(tm(1, "x"), tm(b)) + ") = " + menosV(c)); izq = function(v){ return a * (v + b); };
    pasos.push("<strong>" + T("Distribute:", "Distribuir:") + "</strong> " + auto("(" + menosV(a) + ")(x) = " + P(tm(a, "x"))) + T(" and ", " y ") + auto("(" + menosV(a) + ")(" + menosV(b) + ") = " + menosV(a * b)) + T(". You get ", ". Queda ") + auto(P(tm(a, "x"), tm(a * b)) + " = " + menosV(c)) + ".");
  } else if (f === 3){
    a = elige([2, 3, 4, 5]); b = nz(); d = nz(); c = a * (sol + b) + d; A = a; K = a * b + d;
    vis = auto(a + "(" + P(tm(1, "x"), tm(b)) + ")" + termVis(tm(d), false) + " = " + menosV(c)); izq = function(v){ return a * (v + b) + d; };
    pasos.push("<strong>" + T("Distribute:", "Distribuir:") + "</strong> " + auto(a + "(" + P(tm(1, "x"), tm(b)) + ") = " + P(tm(a, "x"), tm(a * b))) + T(". You get ", ". Queda ") + auto(P(tm(a, "x"), tm(a * b), tm(d)) + " = " + menosV(c)) + ".");
    pasos.push("<strong>" + T("Combine", "Combinar") + "</strong> " + T("the constants on the left side: ", "las constantes del lado izquierdo: ") + auto(menosV(a * b) + termVis(tm(d), false) + " = " + menosV(a * b + d)) + T(". You get ", ". Queda ") + auto(P(tm(a, "x"), tm(a * b + d)) + " = " + menosV(c)) + ".");
  } else {
    a = aleatorio(2, 7); e = elige([1, 2, 3, -1]); b = nz(); c = (a + e) * sol + b; A = a + e; K = b;
    vis = auto(P(tm(a, "x"), tm(b), tm(e, "x")) + " = " + menosV(c)); izq = function(v){ return a * v + b + e * v; };
    pasos.push("<strong>" + T("Combine", "Combinar") + "</strong> " + T("the x terms: ", "los términos en x: ") + auto(P(tm(a, "x")) + termVis(tm(e, "x"), false) + " = " + P(tm(a + e, "x"))) + T(". You get ", ". Queda ") + auto(P(tm(A, "x"), tm(b)) + " = " + menosV(c)) + ".");
  }
  if (K !== 0) pasos.push("<strong>" + T("Isolate:", "Aislar:") + "</strong> " + sumaResta(K).toLowerCase().replace(/^./, function(z){ return z; }) + ": " + auto(P(tm(A, "x")) + " = " + menosV(c) + (K > 0 ? " − " + K : " + " + (-K)) + " = " + menosV(c - K)) + ".");
  if (A !== 1) pasos.push("<strong>" + T("Isolate:", "Aislar:") + "</strong> " + T("divide both sides by ", "se divide entre ") + menosV(A) + T("", " en ambos lados") + ": " + auto("x = " + menosV(c - K) + " ÷ " + (A < 0 ? "(" + menosV(A) + ")" : A) + " = " + menosV(sol)) + ".");
  pasos.push("<strong>" + T("Check:", "Verificar:") + "</strong> " + T("with x = " + menosV(sol) + ", the left side equals " + menosV(izq(sol)) + " and the right side " + menosV(c) + ". They match.", "con x = " + menosV(sol) + ", el lado izquierdo vale " + menosV(izq(sol)) + " y el derecho " + menosV(c) + ". Coinciden."));
  pasos.push('<span class="veredicto">' + T("Solution: x = ", "Solución: x = ") + menosV(sol) + "</span>");
  return {vis: vis, izq: izq, der: function(){ return c; }, sol: sol, pasos: pasos, A: A, K: K, c: c, f: f, a: a, b: b};
}
var PS = {pasos: [], visto: 0, cola: [1, 2, 3, 4]};
function nuevoPS(){
  var E = ecuacionForma(PS.cola.length ? PS.cola.shift() : aleatorio(1, 4));
  PS.pasos = E.pasos; PS.visto = 0;
  $("ps-ec").innerHTML = E.vis;
  pintaPS();
}
function pintaPS(){
  $("ps-pasos").innerHTML = PS.pasos.slice(0, PS.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === PS.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("ps-sig"); b.disabled = PS.visto >= PS.pasos.length; $("ps-todo").disabled = b.disabled;
  b.textContent = PS.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function genResolver(){
  var E = ecuacionForma(aleatorio(1, 4)), pistas = [];
  pistas.push({v: fr(E.c + E.K, E.A), msg: T("Check the sign when you move the constant: to undo “" + (E.K > 0 ? "+ " + E.K : "− " + (-E.K)) + ",” " + (E.K > 0 ? "subtract" : "add") + " on both sides.", "Revise el signo al pasar la constante: para deshacer «" + (E.K > 0 ? "+ " + E.K : "− " + (-E.K)) + "» se " + (E.K > 0 ? "resta" : "suma") + " en ambos lados.")});
  pistas.push({v: fr(E.c - E.K, -E.A), msg: T("Check the sign when you divide by " + menosV(E.A) + ".", "Revise el signo al dividir entre " + menosV(E.A) + ".")});
  pistas.push({v: fsum(fr(E.c, E.A), fr(-E.K)), msg: T("Reverse order: remove the constant first and divide at the end.", "Orden inverso: primero se quita la constante y al final se divide.")});
  if (E.f === 2) pistas.push({v: fr(E.c - E.b, E.a), msg: T("Distribute first: the " + menosV(E.a) + " also multiplies the " + menosV(E.b) + ".", "Primero hay que distribuir: el " + menosV(E.a) + " multiplica también al " + menosV(E.b) + ".")});
  return {enun: T("Solve ", "Resuelva ") + E.vis + ".",
    solucion: T("The solution is x = " + menosV(E.sol) + ". With x = " + menosV(E.sol) + " both sides equal " + menosV(E.c) + ".", "La solución es x = " + menosV(E.sol) + ". Con x = " + menosV(E.sol) + " los dos lados valen " + menosV(E.c) + "."),
    evalua: function(txt){ return evaluaNumero(txt, fr(E.sol), pistas); }};
}

/* ============ MODULE 3 · variables on both sides ============ */
function ambosAzar(){
  var a, c; do { a = aleatorio(2, 9); c = aleatorio(1, 8); } while (a === c);
  var sol = aleatorio(-5, 8); if (sol === 0) sol = 3;
  var b = nz(), d = a * sol + b - c * sol;
  return {a: a, b: b, c: c, d: d, sol: sol};
}
var AL = {e: null, cola: [{a: 5, b: 2, c: 3, d: 10, sol: 4}, {a: 7, b: 1, c: 2, d: 16, sol: 3}]};
function nuevoAL(){
  var e = AL.e = AL.cola.length ? AL.cola.shift() : ambosAzar();
  $("al-ec").innerHTML = ecHTML(L(e.a, e.b), L(e.c, e.d));
  $("al-der").textContent = T("Subtract " + (e.c === 1 ? "" : e.c) + "x from both sides", "Restar " + (e.c === 1 ? "" : e.c) + "x en ambos lados");
  $("al-izq").textContent = T("Subtract " + e.a + "x from both sides", "Restar " + e.a + "x en ambos lados");
  $("al-pasos").innerHTML = "";
}
function caminoAL(restaDer){
  var e = AL.e, pasos = [], coef, R, h = "";
  if (restaDer){
    coef = e.a - e.c;
    pasos.push(T("Subtract ", "Se resta ") + P(tm(e.c, "x")) + T(" from both sides: ", " en ambos lados: ") + ecHTML(L(coef, e.b), L(0, e.d)) + ".");
    if (e.b) pasos.push(sumaResta(e.b) + ": " + ecHTML(L(coef, 0), L(0, e.d - e.b)) + ".");
    R = e.d - e.b;
  } else {
    coef = e.c - e.a;
    pasos.push(T("Subtract ", "Se resta ") + P(tm(e.a, "x")) + T(" from both sides: ", " en ambos lados: ") + ecHTML(L(0, e.b), L(coef, e.d)) + ".");
    if (e.d) pasos.push(sumaResta(e.d) + ": " + ecHTML(L(0, e.b - e.d), L(coef, 0)) + ".");
    R = e.b - e.d;
  }
  if (coef !== 1) pasos.push(T("Divide both sides by ", "Se divide entre ") + menosV(coef) + T("", " en ambos lados") + ": " + auto(menosV(R) + " ÷ " + (coef < 0 ? "(" + menosV(coef) + ")" : coef) + " = " + menosV(e.sol)) + ".");
  h += "<p><strong>" + T("Path chosen: subtract ", "Camino elegido: restar ") + P(tm(restaDer ? e.c : e.a, "x")) + ".</strong></p>";
  pasos.forEach(function(p, i){ h += '<div class="paso"><span class="n" aria-hidden="true">' + (i + 1) + "</span>" + p + "</div>"; });
  h += '<div class="paso"><span class="n" aria-hidden="true">✓</span><span class="veredicto">x = ' + menosV(e.sol) + ".</span> " +
       (coef > 0 ? T("This path left a positive coefficient (" + coef + "x).", "Este camino dejó el coeficiente positivo (" + coef + "x).") : T("This path left a negative coefficient (" + menosV(coef) + "x): you get the same answer, but you must be more careful with the signs.", "Este camino dejó el coeficiente negativo (" + menosV(coef) + "x): se llega a lo mismo, pero con más cuidado con los signos.")) + "</div>";
  $("al-pasos").innerHTML = h;
}
function genAmbos(){
  var e = ambosAzar(), o = [], pc = {}, usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opX(fr(e.sol)));
  mete(opX(fr(e.d - e.b, e.a + e.c)), T("To gather the x terms, subtract ", "Para reunir las x se resta ") + P(tm(e.c, "x")) + T("; do not add it.", "; no se suma."));
  mete(opX(fr(e.d + e.b, e.a - e.c)), T("Check the sign when you move the constant ", "Revise el signo al pasar la constante ") + menosV(e.b) + ".");
  mete(opX(fr(e.b - e.d, e.a - e.c)), T("Check the order of the subtraction of the constants.", "Revise el orden de la resta de las constantes."));
  mete(opX(fr(e.sol + 1)), T("Check your answer by substituting it.", "Compruebe su respuesta sustituyéndola."));
  mete(opX(fr(e.sol - 1)), T("Check your answer by substituting it.", "Compruebe su respuesta sustituyéndola."));
  return {enun: T("Solve ", "Resuelva ") + ecHTML(L(e.a, e.b), L(e.c, e.d)) + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("Subtract ", "Se resta ") + P(tm(e.c, "x")) + ": " + ecHTML(L(e.a - e.c, e.b), L(0, e.d)) + T(", and solve: x = ", ", y se despeja x = ") + menosV(e.sol) + ".",
    mal: T("Subtract ", "Se resta ") + P(tm(e.c, "x")) + T(" from both sides: ", " en ambos lados: ") + ecHTML(L(e.a - e.c, e.b), L(0, e.d)) + T(". Then solve: x = ", ". Después se despeja: x = ") + menosV(e.sol) + "."};
}

/* ============ MODULE 4 · checking ============ */
var VF = {primero: 0, pista: 0, total: 0, resuelta: false, intentos: 0, q: null};
function pintaVF(){
  var q;
  if (Math.random() < 0.3){ var e = ambosAzar(); q = {vis: ecHTML(L(e.a, e.b), L(e.c, e.d)), izq: function(v){ return e.a * v + e.b; }, der: function(v){ return e.c * v + e.d; }, sol: e.sol}; }
  else q = ecuacionForma(aleatorio(1, 4));
  var v = Math.random() < 0.5 ? q.sol : elige([q.sol + 1, q.sol - 1, -q.sol, q.sol + 2].filter(function(z){ return z !== q.sol; }));
  q.v = v; VF.q = q; VF.resuelta = false; VF.intentos = 0;
  $("vf-enun").innerHTML = T("Is x = " + menosV(v) + " a solution of ", "¿Es x = " + menosV(v) + " solución de ") + q.vis + T("? Substitute into both sides.", "? Sustituya en los dos lados.");
  ["vf-i", "vf-d"].forEach(function(id){ $(id).value = ""; $(id).disabled = false; $(id).classList.remove("error"); });
  $("vf-s").value = ""; $("vf-s").disabled = false; $("vf-comprobar").disabled = false;
  $("vf-fb").className = "fb"; $("vf-fb").innerHTML = "";
}
function compruebaVF(){
  if (VF.resuelta) return;
  var q = VF.q, I = leeEntero($("vf-i").value), D = leeEntero($("vf-d").value), s = $("vf-s").value, fb = $("vf-fb");
  $("vf-i").classList.toggle("error", I === null); $("vf-d").classList.toggle("error", D === null);
  if (I === null || D === null || !s){ fb.className = "fb pista"; fb.innerHTML = T("Fill in all three boxes: the value of each side (a whole number) and your conclusion.", "Complete los tres campos: el valor de cada lado (número entero) y su conclusión."); return; }
  var vi = q.izq(q.v), vd = q.der(q.v), es = vi === vd ? "si" : "no", msgs = [];
  if (I !== vi) msgs.push(T("Check the left side.", "Revise el lado izquierdo."));
  if (D !== vd) msgs.push(T("Check the right side.", "Revise el lado derecho."));
  if (!msgs.length && s !== es) msgs.push(T("The values are right, but the conclusion is not: ", "Los valores están bien, pero la conclusión no: ") + (es === "si" ? T("both sides match.", "los dos lados coinciden.") : T("the two sides are different.", "los dos lados son distintos.")));
  VF.intentos++;
  var resumen = T("With x = " + menosV(q.v) + ": the left side equals " + menosV(vi) + " and the right side " + menosV(vd) + ". ", "Con x = " + menosV(q.v) + ": el lado izquierdo vale " + menosV(vi) + " y el derecho " + menosV(vd) + ". ") +
                (es === "si" ? T("They match: x = " + menosV(q.v) + " is the solution.", "Coinciden: x = " + menosV(q.v) + " es la solución.") : T("They do not match: x = " + menosV(q.v) + " is not a solution. The solution is x = " + menosV(q.sol) + ".", "No coinciden: x = " + menosV(q.v) + " no es solución. La solución es x = " + menosV(q.sol) + "."));
  if (!msgs.length){ VF.resuelta = true; VF.total++; if (VF.intentos === 1) VF.primero++; else VF.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + resumen; }
  else if (VF.intentos >= 2){ VF.resuelta = true; VF.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + resumen + TX.nuevo; }
  else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msgs.join(" ") + T(" Remember to write the value in parentheses when you substitute.", " Recuerde escribir el valor entre paréntesis al sustituir.") + TX.unoMas; }
  if (VF.resuelta) ["vf-i", "vf-d", "vf-s", "vf-comprobar"].forEach(function(id){ $(id).disabled = true; });
  $("vf-marcador").textContent = VF.total ? TX.resueltos(VF.primero + VF.pista, VF.primero, VF.total) : "";
}

/* ============ Start ============ */
$("bz-ambos").addEventListener("click", function(){ accionBZ("ambos"); });
$("bz-uno").addEventListener("click", function(){ accionBZ("uno"); });
$("bz-dividir").addEventListener("click", function(){ accionBZ("dividir"); });
$("bz-deshacer").addEventListener("click", deshacerBZ);
$("bz-nuevo").addEventListener("click", function(){ nuevaBZ(); });
nuevaBZ([2, 4, 5]);
OMR("p1", genPrimerPaso);
$("ps-sig").addEventListener("click", function(){ if (PS.visto < PS.pasos.length){ PS.visto++; pintaPS(); } });
$("ps-todo").addEventListener("click", function(){ PS.visto = PS.pasos.length; pintaPS(); });
$("ps-nuevo").addEventListener("click", nuevoPS);
nuevoPS();
creaPracticaLibre("p2", genResolver);
$("al-der").addEventListener("click", function(){ caminoAL(true); });
$("al-izq").addEventListener("click", function(){ caminoAL(false); });
$("al-nuevo").addEventListener("click", nuevoAL);
nuevoAL();
OMR("p3", genAmbos);
$("vf-comprobar").addEventListener("click", compruebaVF);
$("vf-nuevo").addEventListener("click", pintaVF);
pintaVF();
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}"

def practica_pagina():
    n = N
    P = n3
    pasos5 = [t("Distribute to clear the parentheses, if there are any.", "Distribuir los paréntesis, si los hay."),
              t("Combine like terms on each side.", "Combinar los términos semejantes de cada lado."),
              t("Move the variables to one side of the equal sign.", "Pasar las variables a un solo lado del igual."),
              t("Isolate the variable with the properties of equality.", "Aislar la variable con las propiedades de igualdad."),
              t("Check by substituting into the original equation.", "Verificar sustituyendo en la ecuación original.")]
    lista5 = "\n".join(f'        <div class="paso"><span class="n" aria-hidden="true">{i + 1}</span>{p}</div>' for i, p in enumerate(pasos5))
    mods = [
     (t("balance", "balanza"), t("The equation as a balance scale", "La ecuación como una balanza"),
      f'''      <p>{t("An equation is a <strong>balanced scale</strong>: what is on the left of the equal sign weighs the same as what is on the right. To keep the balance, whatever you do to one side <strong>you do to the other</strong>. The goal is to leave the x box alone.", "Una ecuación es una <strong>balanza en equilibrio</strong>: lo que está a la izquierda del igual pesa lo mismo que lo que está a la derecha. Para no romper el equilibrio, lo que se hace en un lado <strong>se hace igual en el otro</strong>. El objetivo es dejar la caja x sola.")}</p>
      <h3>{t("Solve with the balance scale", "Resuelva con la balanza")}</h3>
      <p>{t("Each box weighs x and each circle weighs 1. Also try taking a weight off one side only to see what happens.", "Cada caja pesa x y cada círculo pesa 1. Pruebe también a quitar una pesa de un solo lado para ver qué pasa.")}</p>
      <div class="panel">
        <div class="estado"><span class="grande" id="bz-ec" aria-live="polite"></span></div>
        <div id="bz-svg"></div>
        <div class="fila-btn" style="justify-content:center;">
          <button type="button" class="btn" id="bz-ambos">{t("Take a circle off each side", "Quitar un círculo de cada lado")}</button>
          <button type="button" class="btn-sec" id="bz-uno">{t("Take a circle off the left side only", "Quitar un círculo solo de la izquierda")}</button>
          <button type="button" class="btn" id="bz-dividir"></button>
        </div>
        <div class="fila-btn" style="justify-content:center;">
          <button type="button" class="btn-sec" id="bz-deshacer">{t("Undo", "Deshacer")}</button>
          <button type="button" class="btn-sec" id="bz-nuevo">{t("Another equation", "Otra ecuación")}</button>
        </div>
{P.aviso("bz-aviso")}
        <div class="fb" id="bz-fb" role="status"></div>
      </div>
      <div class="caja-tip"><strong>{t("Inverse operations:", "Operación inversa:")}</strong> {t("to undo addition, subtract; to undo subtraction, add; to undo multiplication, divide; and to undo division, multiply. Always on both sides.", "para deshacer una suma se resta; para deshacer una resta se suma; para deshacer una multiplicación se divide, y para deshacer una división se multiplica. Siempre en los dos lados.")}</div>
{B.om("p1", t("Practice: what do you do to both sides?", "Practique: ¿qué se hace en ambos lados?"))}'''),
     (t("steps", "pasos"), t("One-step and multi-step equations", "Ecuaciones de uno y varios pasos"),
      f'''      <p>{t("Undo the operations in <strong>reverse order</strong>: in 2x + 5, x is first multiplied by 2 and then 5 is added; to undo it, first remove the 5 and last the 2. This five-step strategy works for any linear equation:", "Las operaciones se deshacen en <strong>orden inverso</strong>: en 2x + 5, a la x primero se la multiplica por 2 y luego se le suma 5; para deshacerlo, primero se quita el 5 y al final el 2. Para cualquier ecuación lineal sirve esta estrategia de cinco pasos:")}</p>
      <div class="pasos">
{lista5}
      </div>
      <h3>{t("The strategy in action", "La estrategia en acción")}</h3>
      <div class="panel">
        <div class="estado"><span class="grande" id="ps-ec"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="ps-sig"></button><button type="button" class="btn-sec" id="ps-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="ps-nuevo">{t("Another equation", "Otra ecuación")}</button></div>
      </div>
      <div class="pasos" id="ps-pasos" aria-live="polite"></div>
{B.libre("p2", t("Practice: solve the equation", "Practique: resuelva la ecuación"), t("Value of x", "Valor de x"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Type only the number, for example 4 or −3.", "Escriba solo el número, por ejemplo 4 o −3.") + '</p>\n        <div class="fila-btn">', 1)}'''),
     (t("both-sides", "ambos-lados"), t("Variables on both sides", "Variables en ambos lados"),
      f'''      <p>{t("When x appears on both sides, first gather all the x terms on one side by subtracting one of the terms from both sides, and the constants on the other. Then isolate the variable as usual.", "Cuando la x aparece en los dos lados, primero se reúnen todas las x en un solo lado, restando uno de los términos en ambos lados, y las constantes en el otro. Después se aísla la variable como siempre.")}</p>
      <h3>{t("Which x do you move?", "¿Qué x se mueve?")}</h3>
      <p>{t("Both choices lead to the same solution. Compare which one leaves a positive coefficient.", "Las dos elecciones llevan a la misma solución. Compare cuál deja el coeficiente positivo.")}</p>
      <div class="panel">
        <div class="estado"><span class="grande" id="al-ec"></span></div>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn" id="al-der"></button><button type="button" class="btn" id="al-izq"></button><button type="button" class="btn-sec" id="al-nuevo">{t("Another equation", "Otra ecuación")}</button></div>
      </div>
      <div class="pasos" id="al-pasos" aria-live="polite"></div>
      <div class="caja-tip"><strong>{t("A useful trick:", "Truco práctico:")}</strong> {t("subtract the term with the <strong>smaller</strong> coefficient. That way x keeps a positive coefficient and you avoid sign mistakes.", "conviene restar el término con el coeficiente <strong>menor</strong>. Así la x queda con coeficiente positivo y se evitan errores de signo.")}</div>
{B.om("p3", t("Practice: variables on both sides", "Practique: variables en ambos lados"))}'''),
     (t("check", "verificar"), t("Checking the solution", "Verificar la solución"),
      f'''      <p>{t("You check every solution by substituting it into the <strong>original equation</strong>. If both sides give the same value, the solution is right. One minute of checking catches almost every sign mistake.", "Toda solución se comprueba sustituyéndola en la <strong>ecuación original</strong>. Si los dos lados dan el mismo valor, la solución es correcta. Un minuto de verificación detecta casi todos los errores de signo.")}</p>
      <h3>{t("Practice: is it a solution?", "Practique: ¿es solución?")}</h3>
      <div class="practica" id="vf">
        <div class="enun" id="vf-enun"></div>
        <div class="campos">
          <div class="campo"><label for="vf-i">{t("Value of the left side", "Valor del lado izquierdo")}</label><input type="text" autocomplete="off" class="corto" id="vf-i"></div>
          <div class="campo"><label for="vf-d">{t("Value of the right side", "Valor del lado derecho")}</label><input type="text" autocomplete="off" class="corto" id="vf-d"></div>
          <div class="campo"><label for="vf-s">{t("Is it a solution?", "¿Es solución?")}</label>
            <select id="vf-s"><option value="">{t("Choose", "Elija")}</option><option value="si">{t("Yes, the sides match", "Sí, los lados coinciden")}</option><option value="no">{t("No, the sides do not match", "No, los lados no coinciden")}</option></select></div>
        </div>
        <div class="fila-btn">
          <button type="button" class="btn" id="vf-comprobar">Check</button>
          <button type="button" class="btn-sec" id="vf-nuevo">New exercise</button>
        </div>
        <div class="fb" id="vf-fb" role="status"></div>
        <p class="marcador" id="vf-marcador"></p>
      </div>''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Resolver ecuaciones lineales: propiedades de igualdad y variables en ambos lados")
