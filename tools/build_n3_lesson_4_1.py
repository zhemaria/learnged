"""Level 3 · Lesson 4.1 · Variables, algebraic expressions, and translating — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "4-1"
TEMA = ("Linear algebra", "Álgebra lineal")
TIT = ("Variables, algebraic expressions, and translating", "Variables, expresiones algebraicas y traducción")
SCRIPTS = ("/math/radicals.js", "/math/linear.js")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("Algebra is not completely new: in Level 1 you already used simple unknowns to solve one-step problems. What changes here is the depth. After completing number sense in Topics 1 to 3 of this level (exponents, scientific notation, and the real numbers), Level 3 picks up that language again and makes it formal: you will translate fully between words and symbols, and you will learn to simplify expressions by distributing and combining like terms. That base will let you solve equations in the next lessons.",
"El lenguaje algebraico no es del todo nuevo: en el Nivel 1 ya se trabajó con incógnitas simples para resolver problemas de un paso. Lo que cambia aquí es la profundidad. Tras completar el sentido numérico en los Temas 1 al 3 de este nivel (exponentes, notación científica y números reales), el Nivel 3 retoma y formaliza ese lenguaje: se trabajará la traducción completa entre palabras y símbolos, y se aprenderá a simplificar expresiones distribuyendo y combinando términos semejantes. Esa base permitirá, en las próximas lecciones, resolver ecuaciones.")}</p>
<p>{t("A <strong>variable</strong> is a letter that stands for a number that is unknown or that can change. An <strong>algebraic expression</strong> combines variables, numbers, and operations. Its parts have precise names:", "Una <strong>variable</strong> es una letra que representa un número desconocido o que puede cambiar. Una <strong>expresión algebraica</strong> combina variables, números y operaciones. Sus partes tienen nombres precisos:")}</p>
{tabla(t("The parts of the expression 3x + 5", "Partes de la expresión 3x + 5"), t("Parts of the expression 3x plus 5: term, coefficient, variable, and constant", "Partes de la expresión 3x más 5: término, coeficiente, variable y constante"), [t("Part", "Parte"), t("In 3x + 5", "En 3x + 5"), t("Meaning", "Significado")],
  [[t("Term", "Término"), t("3x and 5", "3x y 5"), t("Each part separated by + or −.", "Cada parte separada por + o −.")],
   [t("Coefficient", "Coeficiente"), "3", t("The number that multiplies the variable.", "El número que multiplica a la variable.")],
   [t("Variable", "Variable"), "x", t("The letter that stands for the unknown value.", "La letra que representa el valor desconocido.")],
   [t("Constant", "Constante"), "5", t("The term that has no variable.", "El término que no tiene variable.")]])}
{caja("tip", t("The invisible coefficient", "Coeficiente invisible"), t("<p>When a variable appears alone, like x, its coefficient is 1 (x = 1x). In the same way, −x means −1x. Remembering this prevents mistakes when you combine terms.</p>", "<p>Cuando una variable aparece sola, como x, su coeficiente es 1 (x = 1x). De igual modo, −x significa −1x. Recordarlo evita errores al combinar términos.</p>"))}
{enlace(n, t("vocabulary", "vocabulario"), t("variables, terms, and coefficients", "variables, términos y coeficientes"), t("Identify the parts of an algebraic expression.", "Identifique las partes de una expresión algebraica."))}'''

    s2 = f'''<p>{t("Much of algebra is translating a sentence in words into the language of symbols. Certain words always point to the same operation.", "Gran parte del álgebra consiste en traducir un enunciado verbal al lenguaje de los símbolos. Ciertas palabras señalan siempre la misma operación.")}</p>
{tabla(t("From words to algebra", "Del lenguaje verbal al algebraico"), t("Translation table from words to algebra", "Tabla de traducción del lenguaje verbal al algebraico"), [t("Phrase in words", "Frase verbal"), t("Algebraic expression", "Expresión algebraica")],
  [[t("Twice a number x", "El doble de un número x"), "2x"], [t("Three more than a number x", "Tres más que un número x"), "x + 3"], [t("Half of a number x", "La mitad de un número x"), fx("x", 2)],
   [t("A number x decreased by 4", "Un número x disminuido en 4"), "x − 4"], [t("The square of a number x", "El cuadrado de un número x"), "x<sup>2</sup>"], [t("Five times a number, increased by 2", "Cinco veces un número, aumentado en 2"), "5x + 2"]])}
{caja("ojo", t("Order matters in subtraction", "El orden importa en la resta"), t("<p>“A number decreased by 4” is x − 4, but “4 decreased by a number” is 4 − x. And “4 less than a number” is x − 4: you take 4 away from the number. Subtraction is not commutative, so read carefully to see which comes first.</p>", "<p>«Un número disminuido en 4» es x − 4, pero «4 disminuido en un número» es 4 − x. Y «4 menos que un número» es x − 4: al número se le quitan 4. La resta no es conmutativa, así que conviene leer con cuidado quién va primero.</p>"))}
{practica("p1", t("Practice 1 — Times", "Práctica 1 — Veces"), t("“Five times a number x”", "«Cinco veces un número x»"), [("a", "5x"), ("b", "x + 5"), ("c", fx(5, "x"))])}
{practica("p2", t("Practice 2 — Increased by", "Práctica 2 — Aumentado en"), t("“A number x increased by 7”", "«Un número x aumentado en 7»"), [("a", "7x"), ("b", "x − 7"), ("c", "x + 7")])}
{practica("p3", t("Practice 3 — The square", "Práctica 3 — El cuadrado"), t("“The square of a number x”", "«El cuadrado de un número x»"), [("a", "2x"), ("b", "x<sup>2</sup>"), ("c", fx("x", 2))])}
{enlace(n, t("translate", "traducir"), t("translating between words and algebra", "traducir entre palabras y álgebra"), t("Turn phrases into expressions and expressions into phrases.", "Convierta frases en expresiones y expresiones en frases."))}'''

    s3 = f'''<p>{t("Two terms are <strong>like terms</strong> if they have the same variable raised to the same exponent. Only like terms can be combined, by adding or subtracting their coefficients.", "Dos términos son <strong>semejantes</strong> si tienen la misma variable elevada al mismo exponente. Solo los términos semejantes se pueden combinar, sumando o restando sus coeficientes.")}</p>
{ejemplo(t("Example 1: simplify 3x + 5x", "Ejemplo 1: simplifique 3x + 5x"),
  [("1", t("Like terms?", "¿Semejantes?"), t("Both terms have the variable x: they are like terms.", "Los dos términos tienen la variable x: son semejantes.")),
   ("2", t("Add the coefficients.", "Sumar los coeficientes."), "3 + 5 = 8."),
   ("✓", t("Answer.", "Respuesta."), "3x + 5x = <strong>8x</strong>")])}
{ejemplo(t("Example 2: simplify 7x − 2x + 4", "Ejemplo 2: simplifique 7x − 2x + 4"),
  [("1", t("The x terms.", "Los términos con x."), "7x − 2x = 5x."),
   ("2", t("The constant.", "La constante."), t("4 has no x: it stays apart.", "El 4 no tiene x: se deja aparte.")),
   ("✓", t("Answer.", "Respuesta."), "7x − 2x + 4 = <strong>5x + 4</strong>")])}
{caja("ojo", t("Different terms do not combine", "No se combinan términos distintos"), t("<p>4x + 2y cannot be simplified, because x and y are different variables. And 3x + 5 does not become 8x, because 5 has no x. Also, 3x<sup>2</sup> + 2x is not 5x<sup>2</sup>: the exponents are different.</p>", "<p>4x + 2y no se puede simplificar, porque x y y son variables diferentes. Tampoco 3x + 5 se reduce a 8x, porque el 5 no tiene la variable x. Y 3x<sup>2</sup> + 2x no es 5x<sup>2</sup>: los exponentes son distintos.</p>"))}
{enlace(n, t("like-terms", "semejantes"), t("combining like terms", "combinar términos semejantes"), t("Sort the terms into families and combine them.", "Clasifique los términos por familias y redúzcalos."))}'''

    s4 = f'''<p>{t("The distributive property lets you multiply a number by a sum by sharing it out to each term in the parentheses.", "La propiedad distributiva permite multiplicar un número por una suma, repartiéndolo a cada término del paréntesis.")}</p>
{big("a(b + c) = a · b + a · c")}
{ejemplo(t("Example 3: simplify 3(x + 4)", "Ejemplo 3: simplifique 3(x + 4)"),
  [("1", t("Share out the 3.", "Repartir el 3."), t("3 · x + 3 · 4.", "3 · x + 3 · 4.")),
   ("✓", t("Answer.", "Respuesta."), "3(x + 4) = <strong>3x + 12</strong>")])}
{ejemplo(t("Example 4: simplify 2(x + 3) + 4x", "Ejemplo 4: simplifique 2(x + 3) + 4x"),
  [("1", t("Distribute.", "Distribuir."), "2x + 6 + 4x."),
   ("2", t("Combine like terms.", "Combinar los semejantes."), "2x + 4x = 6x."),
   ("✓", t("Answer.", "Respuesta."), "2(x + 3) + 4x = <strong>6x + 6</strong>")])}
{caja("ojo", t("Signs are shared out too", "El signo también se reparte"), t("<p>−2(x − 5) = −2x + 10, because (−2)(−5) = +10. The most common mistake is to multiply only the first term: 3(x + 4) is not 3x + 4.</p>", "<p>−2(x − 5) = −2x + 10, porque (−2)(−5) = +10. El error más frecuente es multiplicar solo el primer término: 3(x + 4) no es 3x + 4.</p>"))}
{practica("p4", t("Practice 4 — Combine", "Práctica 4 — Combinar"), "4x + 6x =", [("a", "24x"), ("b", "10x"), ("c", "10x<sup>2</sup>")])}
{practica("p5", t("Practice 5 — Distribute", "Práctica 5 — Distribuir"), "5(x + 2) =", [("a", "5x + 10"), ("b", "5x + 2"), ("c", "x + 10")])}
{practica("p6", t("Practice 6 — With a constant", "Práctica 6 — Con constante"), "3x + 2 + x =", [("a", "5x"), ("b", "6x"), ("c", "4x + 2")])}
{enlace(n, t("distributive", "distributiva"), t("the distributive property", "la propiedad distributiva"), t("Distribute with the area model, paying attention to signs.", "Distribuya con el modelo de área y con atención a los signos."))}'''

    s5 = f'''<p>{t("To <strong>evaluate</strong> an expression means to replace the variable with a given value and work out the result, following the order of operations (PEMDAS).", "<strong>Evaluar</strong> una expresión significa sustituir la variable por un valor dado y calcular el resultado, respetando el orden de las operaciones (PEMDAS).")}</p>
{ejemplo(t("Example 5: evaluate 2x + 5 when x = 3", "Ejemplo 5: evalúe 2x + 5 cuando x = 3"),
  [("1", t("Substitute.", "Sustituir."), "2(3) + 5."),
   ("2", t("Multiply first.", "Multiplicar primero."), "6 + 5."),
   ("✓", t("Answer.", "Respuesta."), t("2x + 5 = <strong>11</strong> when x = 3.", "2x + 5 = <strong>11</strong> cuando x = 3."))])}
{ejemplo(t("Example 6: evaluate x<sup>2</sup> + 1 when x = 4", "Ejemplo 6: evalúe x<sup>2</sup> + 1 cuando x = 4"),
  [("1", t("Substitute.", "Sustituir."), "(4)<sup>2</sup> + 1."),
   ("2", t("The power first.", "La potencia primero."), "16 + 1."),
   ("✓", t("Answer.", "Respuesta."), t("x<sup>2</sup> + 1 = <strong>17</strong> when x = 4.", "x<sup>2</sup> + 1 = <strong>17</strong> cuando x = 4."))])}
{caja("tip", t("Use parentheses when you substitute", "Use paréntesis al sustituir"), t("<p>Writing 2(3) instead of 23 keeps you from confusing the multiplication with a two-digit number. With negative numbers it is essential: if x = −3, then x<sup>2</sup> = (−3)<sup>2</sup> = 9, but −x<sup>2</sup> = −(−3)<sup>2</sup> = −9.</p>", "<p>Escribir 2(3) en lugar de 23 evita confundir la multiplicación con un número de dos cifras. Con negativos es imprescindible: si x = −3, entonces x<sup>2</sup> = (−3)<sup>2</sup> = 9, pero −x<sup>2</sup> = −(−3)<sup>2</sup> = −9.</p>"))}
{enlace(n, t("evaluate", "evaluar"), t("evaluating expressions", "evaluar expresiones"), t("Substitute with parentheses and follow the order of operations.", "Sustituya con paréntesis y respete el orden de las operaciones."))}'''

    secciones = [("s-" + t("vocabulary", "vocabulario"), t("Variables, terms, and coefficients", "Variables, términos y coeficientes"), s1),
                 ("s-" + t("translate", "traducir"), t("Translating between words and algebra", "Traducir entre palabras y álgebra"), s2),
                 ("s-" + t("like-terms", "semejantes"), t("Combining like terms", "Combinar términos semejantes"), s3),
                 ("s-" + t("distributive", "distributiva"), t("The distributive property", "La propiedad distributiva"), s4),
                 ("s-" + t("evaluate", "evaluar"), t("Evaluating expressions", "Evaluar expresiones"), s5)]

    lesson = {"next": t("Lesson 4.2", "Lección 4.2"), "review": t("sections 2 to 5", "las secciones 2 a 5"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("“Times” means multiply, not add.", "«Veces» indica multiplicar, no sumar."), "c": t("That would be 5 divided by a number.", "Eso sería 5 dividido entre un número.")}, "right": t("“Five times” means 5 · x = 5x.", "«Cinco veces» es 5 · x = 5x."), "solution": t("Five times a number: 5 · x = 5x.", "Cinco veces un número: 5 · x = 5x.")},
      "p2": {"ok": "c", "hints": {"a": t("“Increased by” means add, not multiply.", "«Aumentado en» indica sumar, no multiplicar."), "b": t("“Increased” means it gets bigger: add.", "«Aumentado» quiere decir que crece: se suma.")}, "right": t("“Increased by 7” means + 7.", "«Aumentado en 7» es + 7."), "solution": t("A number increased by 7: x + 7.", "Un número aumentado en 7: x + 7.")},
      "p3": {"ok": "b", "hints": {"a": t("2x is twice the number: x + x.", "2x es el doble: x + x."), "c": t("That is half of the number.", "Eso es la mitad del número.")}, "right": t("The square is x · x = x².", "El cuadrado es x · x = x²."), "solution": t("The square of a number: x · x = x².", "El cuadrado de un número: x · x = x².")},
      "p4": {"ok": "b", "hints": {"a": t("Add the coefficients; do not multiply them.", "Se suman los coeficientes, no se multiplican."), "c": t("The exponent does not change when you add like terms.", "El exponente no cambia al sumar términos semejantes.")}, "right": "4 + 6 = 10: 10x.", "solution": "4x + 6x = (4 + 6)x = 10x."},
      "p5": {"ok": "a", "hints": {"b": t("The 5 also multiplies the 2.", "El 5 también multiplica al 2."), "c": t("The 5 also multiplies the x.", "El 5 también multiplica a la x.")}, "right": "5 · x + 5 · 2 = 5x + 10.", "solution": "5(x + 2) = 5x + 10."},
      "p6": {"ok": "c", "hints": {"a": t("The 2 has no x: it does not combine with the x terms.", "El 2 no tiene x: no se combina con los términos en x."), "b": t("The 2 has no x, and x counts as 1x.", "El 2 no tiene x, y x vale 1x.")}, "right": "3x + x = 4x; " + t("the 2 stays apart.", "el 2 queda aparte."), "solution": "3x + x + 2 = 4x + 2."}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("“Twice” means multiply by 2.", "«El doble» es multiplicar por 2."), "c": t("That is the square.", "Eso es el cuadrado."), "d": t("That is half.", "Eso es la mitad.")}, "solution": "2 · x = 2x."},
      "B": {"ok": "d", "hints": {"a": t("The number goes first: 5 is taken away from it.", "El número va primero: a él se le quitan 5."), "b": t("That is multiplying.", "Eso es multiplicar."), "c": t("“Decreased” means subtract.", "«Disminuido» es restar.")}, "solution": "x − 5."},
      "C": {"ok": "c", "hints": {"a": t("The 4 is a constant: it does not combine with x.", "El 4 es constante: no se combina con x."), "b": t("It is +4, not −4.", "Es +4, no −4."), "d": t("7x − 2x is a subtraction.", "7x − 2x es una resta.")}, "solution": "7x − 2x = 5x; 5x + 4."},
      "D": {"ok": "b", "hints": {"a": t("The 3 also multiplies the 4.", "El 3 también multiplica al 4."), "c": t("The 3 also multiplies the x.", "El 3 también multiplica a la x."), "d": t("3 · 4 = 12, not 7.", "3 · 4 = 12, no 7.")}, "solution": "3x + 12."},
      "E": {"ok": "d", "hints": {"a": t("2 · 3 = 6.", "2 · 3 = 6."), "b": t("You forgot the 4x.", "Faltó el 4x."), "c": t("2 · 3 = 6, not 9.", "2 · 3 = 6, no 9.")}, "solution": "2x + 6 + 4x = 6x + 6."},
      "F": {"ok": "a", "hints": {"b": t("2 · 3 = 6, then add 5.", "2 · 3 = 6 y después se suma 5."), "c": t("2(3) is a multiplication, not the number 23.", "2(3) es una multiplicación, no el número 23."), "d": t("Multiply before you add.", "Primero se multiplica, después se suma.")}, "solution": "2(3) + 5 = 6 + 5 = 11."},
      "G": {"ok": "c", "hints": {"a": t("4² = 16, not 8.", "4² = 16, no 8."), "b": t("Square the 4, then add 1.", "Eleve el 4 al cuadrado y después sume 1."), "d": t("Do not forget the + 1.", "No olvide el + 1.")}, "solution": "(4)² + 1 = 16 + 1 = 17."},
      "H": {"ok": "d", "hints": {"a": t("Different variables.", "Variables distintas."), "b": t("3 has no variable.", "El 3 no tiene variable."), "c": t("Different exponents.", "Exponentes distintos.")}, "solution": t("3x and 7x: same variable, same exponent.", "3x y 7x: misma variable y mismo exponente.")}
     }}

    quiz = [
     ("A", t("Translate: “twice a number x.”", "Traduzca: «el doble de un número x»."), [("a", "2x"), ("b", "x + 2"), ("c", "x<sup>2</sup>"), ("d", fx("x", 2))]),
     ("B", t("Translate: “a number x decreased by 5.”", "Traduzca: «un número x disminuido en 5»."), [("a", "5 − x"), ("b", "5x"), ("c", "x + 5"), ("d", "x − 5")]),
     ("C", t("Simplify: 7x − 2x + 4.", "Simplifique: 7x − 2x + 4."), [("a", "9x"), ("b", "5x − 4"), ("c", "5x + 4"), ("d", "9x + 4")]),
     ("D", t("Simplify: 3(x + 4).", "Simplifique: 3(x + 4)."), [("a", "3x + 4"), ("b", "3x + 12"), ("c", "x + 12"), ("d", "3x + 7")]),
     ("E", t("Simplify: 2(x + 3) + 4x.", "Simplifique: 2(x + 3) + 4x."), [("a", "6x + 3"), ("b", "2x + 6"), ("c", "6x + 9"), ("d", "6x + 6")]),
     ("F", t("Evaluate 2x + 5 when x = 3.", "Evalúe 2x + 5 cuando x = 3."), [("a", "11"), ("b", "13"), ("c", "25"), ("d", "8")]),
     ("G", t("Evaluate x<sup>2</sup> + 1 when x = 4.", "Evalúe x<sup>2</sup> + 1 cuando x = 4."), [("a", "9"), ("b", "81"), ("c", "17"), ("d", "16")]),
     ("H", t("Which are like terms?", "¿Cuáles son términos semejantes?"), [("a", t("3x and 3y", "3x y 3y")), ("b", t("3x and 3", "3x y 3")), ("c", t("x and x<sup>2</sup>", "x y x<sup>2</sup>")), ("d", t("3x and 7x", "3x y 7x"))])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("Write expressions with variables, translate between words and algebra, simplify, and evaluate.", "Escriba expresiones con variables, traduzca entre palabras y álgebra, simplifique y evalúe."),
        ("✏️", t("No calculator needed", "Sin calculadora")),
        [t("<strong>Use</strong> variables to stand for unknown amounts and write algebraic expressions.", "<strong>Usar</strong> variables para representar cantidades desconocidas y escribir expresiones algebraicas."),
         t("<strong>Translate</strong> phrases in words into algebra and back.", "<strong>Traducir</strong> enunciados verbales al lenguaje algebraico y viceversa."),
         t("<strong>Identify</strong> terms, coefficients, constants, and like terms.", "<strong>Identificar</strong> términos, coeficientes, constantes y términos semejantes."),
         t("<strong>Simplify</strong> expressions with the distributive property and by combining like terms.", "<strong>Simplificar</strong> expresiones aplicando la propiedad distributiva y combinando términos semejantes."),
         t("<strong>Evaluate</strong> expressions by substituting whole-number or fraction values.", "<strong>Evaluar</strong> expresiones sustituyendo valores enteros o fraccionarios.")],
        secciones,
        (t("Translate four phrases in words into algebraic expressions, simplify four expressions by combining like terms and using the distributive property, and evaluate four expressions with the given values (whole numbers or fractions).",
           "Traduzca cuatro frases verbales a expresiones algebraicas, simplifique cuatro expresiones combinando términos semejantes y usando la propiedad distributiva, y evalúe cuatro expresiones con los valores dados (enteros o fracciones)."),
         t("A plumber charges $45 for the visit plus $60 for each hour of work. Write an expression for the cost of h hours. Then evaluate it for 2 hours and for 3.5 hours. Look for another service you use (a phone plan, a taxi, a gym) that charges a fixed amount plus an amount per unit, and write its expression.",
           "Un plomero cobra $45 por la visita más $60 por cada hora de trabajo. Escriba una expresión para el costo de h horas. Después evalúela para 2 horas y para 3.5 horas. Busque otro servicio que usted use (un plan de teléfono, un taxi, un gimnasio) que cobre una cantidad fija más una cantidad por unidad, y escriba su expresión.")),
        quiz,
        t("Self-check checklist for algebraic expressions", "Lista de autoevaluación para las expresiones algebraicas"),
        t("Self-check checklist: skills for translating, simplifying, and evaluating expressions", "Lista de autoevaluación: destrezas para traducir, simplificar y evaluar expresiones"),
        [(t("Translating words ↔ algebra", "Traducir verbal ↔ algebraico"), t("I translate correctly both ways, including phrases with subtraction and squares.", "Traduzco correctamente en ambas direcciones, incluidas frases con resta y cuadrado."), t("I translate with some mistakes in the order or the operation.", "Traduzco con errores ocasionales de orden o de operación."), t("I mix up the operation or the order of the terms.", "Confundo la operación o el orden de los términos.")),
         (t("Simplifying expressions", "Simplificar expresiones"), t("I distribute and combine like terms correctly.", "Distribuyo y combino términos semejantes correctamente."), t("I distribute or I combine, but not both.", "Aplico la distributiva o combino, pero no ambas."), t("I combine terms that are not alike.", "Combino términos no semejantes.")),
         (t("Evaluating expressions", "Evaluar expresiones"), t("I substitute with parentheses and follow the order of operations, also with exponents and negative values.", "Sustituyo con paréntesis y respeto el orden de las operaciones, también con exponentes y valores negativos."), t("I substitute, but I make mistakes with PEMDAS.", "Sustituyo, pero cometo errores de PEMDAS."), t("I substitute incorrectly or ignore the order of operations.", "Sustituyo mal o ignoro el orden de las operaciones."))],
        t("<p>This lesson picked up and made formal the algebra language that began in Level 1: a variable stands for an unknown amount, and with it you write expressions that you translate from words, simplify by combining like terms and using the distributive property, and evaluate by substituting values.</p>\n<p>In <strong>Lesson 4.2 · Solving linear equations</strong> you take the next step: when one expression is set equal to another, you get an equation, and the goal is to find the value of the variable that makes it true. Simplifying and combining terms, as you learned here, will be the first step of every solution.</p>",
          "<p>En esta lección se retomó y formalizó el lenguaje algebraico iniciado en el Nivel 1: una variable representa una cantidad desconocida, y con ella se escriben expresiones que se traducen del lenguaje verbal, se simplifican combinando términos semejantes y aplicando la propiedad distributiva, y se evalúan sustituyendo valores.</p>\n<p>En la <strong>Lección 4.2 · Resolver ecuaciones lineales</strong> se dará el siguiente paso: cuando una expresión se iguala a otra, aparece una ecuación, y el objetivo será encontrar el valor de la variable que la hace verdadera. Simplificar y combinar términos, como se aprendió aquí, será el primer paso de toda resolución.</p>"),
        ("4-2", ("", t("Lesson 4.2 · Solving linear equations: properties of equality and variables on both sides", "Lección 4.2 · Resolver ecuaciones lineales: propiedades de igualdad y variables en ambos lados"))),
        [(t("variable", "variable"), t("A letter that stands for a number that is unknown or that can change, like x.", "Una letra que representa un número desconocido o que puede cambiar, como x.")),
         (t("coefficient", "coeficiente"), t("The number that multiplies the variable. In 3x, it is 3.", "El número que multiplica a la variable. En 3x, es 3.")),
         (t("like terms", "términos semejantes"), t("Terms with the same variable raised to the same exponent, like 3x and 7x.", "Términos con la misma variable elevada al mismo exponente, como 3x y 7x.")),
         (t("evaluate", "evaluar"), t("To replace the variable with a value and work out the result.", "Sustituir la variable por un valor y calcular el resultado."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* ============ MODULE 1 · the anatomy of an expression ============ */
function expresionAzar(){
  var p = [];
  if (Math.random() < 0.4) p.push(tm(elige([2, 3, 4, 5, -2, -3, 1, -1]), "x2"));
  p.push(tm(elige([2, 3, 4, 5, 6, 7, -2, -3, -4, -5, 1, -1]), "x"));
  if (Math.random() < 0.5) p.push(tm(elige([2, 3, 4, -2, -3, -6, 1, -1]), "y"));
  p.push(tm(nz(), ""));
  return baraja(p.slice(0, -1)).concat([p[p.length - 1]]);
}
function tipoTermino(tt){ return tt.v === "" ? T("Constant", "Constante") : T("Term with ", "Término con ") + (tt.v === "x2" ? "x²" : tt.v); }
function pintaAnatomia(){
  var p = expresionAzar();
  $("an-expr").innerHTML = polHTML(p);
  var h = "<caption>" + T("The parts of each term of the expression", "Partes de cada término de la expresión") + '</caption><thead><tr><th scope="col">' + T("Term", "Término") + '</th><th scope="col">' + T("Coefficient", "Coeficiente") + '</th><th scope="col">' + T("Variable part", "Parte con variable") + '</th><th scope="col">' + T("Type", "Tipo") + "</th></tr></thead><tbody>";
  p.forEach(function(tt){
    h += "<tr><td>" + auto(termVis(tt, true)) + "</td><td>" + (tt.v === "" ? "—" : menosV(tt.c) + (Math.abs(tt.c) === 1 ? T(" (invisible)", " (invisible)") : "")) + "</td><td>" +
         (tt.v === "" ? T("none", "ninguna") : auto(VAR_VIS[tt.v])) + "</td><td>" + tipoTermino(tt) + "</td></tr>";
  });
  $("an-tabla").innerHTML = h + "</tbody>";
}
function opNum(n){ return {html: menosV(n), clave: "n" + n}; }
function genPartes(){
  var p = expresionAzar(), tp = aleatorio(1, 4), vars = p.filter(function(x){ return x.v !== ""; }), pc = {}, o = [], usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  var enun0 = T("In the expression ", "En la expresión ") + polHTML(p) + ", ";
  if (tp <= 2){
    var obj = elige(vars), c = obj.c, nombre = obj.v === "x2" ? "x²" : obj.v, k = p[p.length - 1].c;
    mete(opNum(c));
    if (c < 0) mete(opNum(-c), T("The sign in front is part of the coefficient.", "El signo que va delante forma parte del coeficiente."));
    if (Math.abs(c) === 1) mete(opNum(0), T("When the variable is alone, the coefficient is 1 (or −1 with a minus sign), not 0.", "Cuando la variable aparece sola, el coeficiente es 1 (o −1 si lleva signo menos), no 0."));
    if (obj.v === "x2") mete(opNum(2), T("The 2 is the exponent, not the coefficient.", "El 2 es el exponente, no el coeficiente."));
    mete(opNum(k), T("That is the constant, not a coefficient.", "Esa es la constante, no un coeficiente."));
    vars.forEach(function(v){ if (v !== obj) mete(opNum(v.c), T("That is the coefficient of another term.", "Ese es el coeficiente de otro término.")); });
    mete(opNum(c + (c > 0 ? 1 : -1)));
    mete(opNum(c + (c > 0 ? 2 : -2)));
    return {enun: enun0 + T("what is the coefficient of ", "¿cuál es el coeficiente de ") + auto(VAR_VIS[obj.v]) + "?", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
      bien: T("The coefficient is the number that multiplies " + nombre + ", with its sign: " + menosV(c) + ".", "El coeficiente es el número que multiplica a " + nombre + ", con su signo: " + menosV(c) + "."), mal: T("The coefficient of " + nombre + " is " + menosV(c) + ".", "El coeficiente de " + nombre + " es " + menosV(c) + ".")};
  }
  if (tp === 3){
    var k2 = p[p.length - 1].c;
    mete(opNum(k2)); mete(opNum(-k2), T("The sign in front is part of the term.", "El signo que va delante forma parte del término."));
    vars.forEach(function(v){ mete(opNum(v.c), T("That is a coefficient: it multiplies a variable.", "Ese es un coeficiente: multiplica a una variable.")); });
    mete(opNum(p.length)); mete(opNum(k2 + 10));
    return {enun: enun0 + T("what is the constant?", "¿cuál es la constante?"), opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
      bien: T("The constant is the term with no variable, with its sign: " + menosV(k2) + ".", "La constante es el término sin variable, con su signo: " + menosV(k2) + "."), mal: T("The constant is " + menosV(k2) + ", the term that has no variable.", "La constante es " + menosV(k2) + ", el término que no tiene variable.")};
  }
  var n = p.length;
  return {enun: enun0 + T("how many terms does it have?", "¿cuántos términos tiene?"), opciones: [opNum(n - 1), opNum(n), opNum(n + 1), opNum(n + 2)], correcta: "n" + n, porClave: {}, enOrden: true,
    pista: T("Count the parts separated by + or −.", "Cuente las partes separadas por + o −."),
    bien: T("Each part separated by + or − is a term: there are " + n + ".", "Cada parte separada por + o − es un término: hay " + n + "."), mal: T("Count the parts separated by + or −: there are " + n + ".", "Cuente las partes separadas por + o −: hay " + n + ".")};
}

/* ============ MODULE 2 · translating ============ */
function fx(a, b){ return '<span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + "</span></span>"; }
function frases(n, m){
  return [
    {f: T("twice a number", "el doble de un número"), e: "2x"},
    {f: T("three times a number", "el triple de un número"), e: "3x"},
    {f: T(n + " more than a number", n + " más que un número"), e: "x + " + n},
    {f: T("a number increased by " + n, "un número aumentado en " + n), e: "x + " + n},
    {f: T("a number decreased by " + n, "un número disminuido en " + n), e: "x − " + n},
    {f: T(n + " decreased by a number", n + " disminuido en un número"), e: n + " − x"},
    {f: T(n + " less than a number", n + " menos que un número"), e: "x − " + n},
    {f: T("half of a number", "la mitad de un número"), e: fx("x", 2)},
    {f: T("a number divided by " + n, "un número dividido entre " + n), e: fx("x", n)},
    {f: T("the square of a number", "el cuadrado de un número"), e: "x<sup>2</sup>"},
    {f: T(n + " times a number, increased by " + m, n + " veces un número, aumentado en " + m), e: n + "x + " + m},
    {f: T("the product of " + n + " and a number, decreased by " + m, "el producto de " + n + " y un número, disminuido en " + m), e: n + "x − " + m},
    {f: T("three times the sum of a number and " + n, "el triple de la suma de un número y " + n), e: "3(x + " + n + ")"},
    {f: T("the difference of a number and " + n, "la diferencia entre un número y " + n), e: "x − " + n},
    {f: T(n + " times a number", n + " veces un número"), e: n + "x"}
  ];
}
function erroresDe(f, n, m){
  var e = f.e;
  if (e === "2x") return [["x + 2", T("“Twice” means multiply by 2, not add 2.", "«El doble» es multiplicar por 2, no sumar 2.")], ["x<sup>2</sup>", T("That is the square, x · x.", "Eso es el cuadrado, x · x.")], [fx("x", 2), T("That is half.", "Eso es la mitad.")]];
  if (e === "3x") return [["x + 3", T("“Three times” means multiply by 3.", "«El triple» es multiplicar por 3.")], ["x<sup>3</sup>", T("That is x · x · x.", "Eso es x · x · x.")], [fx("x", 3), T("That is a third.", "Eso es la tercera parte.")]];
  if (e === "x + " + n) return [[n + "x", T("That is multiplying.", "Eso es multiplicar.")], ["x − " + n, T("It is a sum, not a subtraction.", "Es una suma, no una resta.")], [n + " − x", T("It is a sum, not a subtraction.", "Es una suma, no una resta.")]];
  if (e === "x − " + n) return [[n + " − x", T("Order matters: " + n + " is taken away from the number, so the number goes first.", "El orden importa: al número se le quitan " + n + ", así que el número va primero.")], ["x + " + n, T("It is a subtraction.", "Es una resta.")], [fx("x", n), T("That is dividing.", "Eso es dividir.")]];
  if (e === n + " − x") return [["x − " + n, T("Order matters: here the number is taken away from " + n + ", so " + n + " goes first.", "El orden importa: aquí al " + n + " se le quita el número, así que el " + n + " va primero.")], [n + "x", T("That is multiplying.", "Eso es multiplicar.")], ["x + " + n, T("It is a subtraction.", "Es una resta.")]];
  if (e === fx("x", 2)) return [["2x", T("That is twice the number.", "Eso es el doble.")], ["x − 2", T("Half means dividing by 2.", "La mitad es dividir entre 2.")], ["x<sup>2</sup>", T("That is the square.", "Eso es el cuadrado.")]];
  if (e === fx("x", n)) return [[n + "x", T("That is multiplying.", "Eso es multiplicar.")], [fx(n, "x"), T("Order matters: the number is divided by " + n + ".", "El orden importa: el número se divide entre " + n + ".")], ["x − " + n, T("That is subtracting.", "Eso es restar.")]];
  if (e === "x<sup>2</sup>") return [["2x", T("That is twice the number.", "Eso es el doble.")], [fx("x", 2), T("That is half.", "Eso es la mitad.")], ["x + 2", T("The square is x · x.", "El cuadrado es x · x.")]];
  if (e === n + "x + " + m) return [[n + "(x + " + m + ")", T("Only the number is multiplied by " + n + "; then " + m + " is added.", "Solo el número se multiplica por " + n + "; después se suma " + m + ".")], [m + "x + " + n, T("The numbers are swapped.", "Los números están intercambiados.")], ["x + " + n + " + " + m, T("“Times” means multiply.", "«Veces» indica multiplicar.")]];
  if (e === n + "x − " + m) return [[m + " − " + n + "x", T("Order matters: " + m + " is taken away from the product.", "El orden importa: al producto se le quitan " + m + ".")], [n + "(x − " + m + ")", T("Only the number is multiplied by " + n + ".", "Solo el número se multiplica por " + n + ".")], [n + "x + " + m, T("“Decreased” means subtract.", "«Disminuido» es restar.")]];
  if (e === "3(x + " + n + ")") return [["3x + " + n, T("It is three times the whole sum: use parentheses.", "Es el triple de toda la suma: se usan paréntesis.")], ["x + 3 + " + n, T("“Three times” means multiply by 3.", "«El triple» es multiplicar por 3.")], ["3 + x + " + n, T("“Three times” means multiply by 3.", "«El triple» es multiplicar por 3.")]];
  if (e === n + "x") return [["x + " + n, T("“Times” means multiply.", "«Veces» indica multiplicar.")], ["x<sup>" + n + "</sup>", T("That is a power, not a product.", "Eso es una potencia, no un producto.")], [fx("x", n), T("That is dividing.", "Eso es dividir.")]];
  return [];
}
function mayus(s){ return s.charAt(0).toUpperCase() + s.slice(1); }
function genTraducir(){
  var n = aleatorio(3, 9), m = aleatorio(2, 9); while (m === n) m = aleatorio(2, 9);
  var f = elige(frases(n, m)), o = [{html: auto(f.e), clave: f.e}], pc = {};
  erroresDe(f, n, m).forEach(function(e){ o.push({html: auto(e[0]), clave: e[0]}); pc[e[0]] = e[1]; });
  return {enun: T("Translate into algebra: “" + mayus(f.f) + ".” Use x for the number.", "Traduzca a álgebra: «" + mayus(f.f) + "». Use x para el número."),
    opciones: [o[0]].concat(baraja(o.slice(1))), correcta: f.e, porClave: pc, bien: T("“" + f.f + "” is written ", "«" + f.f + "» se escribe ") + auto(f.e) + ".", mal: T("The translation is ", "La traducción es ") + auto(f.e) + "."};
}
function genAPalabras(){
  var n = aleatorio(3, 9), m = aleatorio(2, 9); while (m === n) m = aleatorio(2, 9);
  var fs = frases(n, m), f = elige(fs), otras = baraja(fs.filter(function(g){ return g.e !== f.e; }));
  var errores = erroresDe(f, n, m).map(function(x){ return x[0]; }), prefer = otras.filter(function(g){ return errores.indexOf(g.e) >= 0; }), resto = otras.filter(function(g){ return errores.indexOf(g.e) < 0; });
  var o = [{html: mayus(f.f), clave: "c"}], pc = {}, vistos = {};
  vistos[f.e] = 1;
  prefer.concat(resto).forEach(function(g){ if (o.length < 4 && !vistos[g.e]){ vistos[g.e] = 1; var k = "o" + o.length; o.push({html: mayus(g.f), clave: k}); pc[k] = T("That phrase is ", "Esa frase es ") + auto(g.e) + "."; } });
  return {enun: T("Which phrase matches ", "¿Qué frase corresponde a ") + auto(f.e) + "?", opciones: [o[0]].concat(baraja(o.slice(1))), correcta: "c", porClave: pc,
    bien: auto(f.e) + T(" is “" + f.f + ".”", " es «" + f.f + "»."), mal: auto(f.e) + T(" is “" + f.f + ".”", " es «" + f.f + "».")};
}

/* ============ MODULE 3 · families of like terms ============ */
var FAM_CLASE = {x2: "fam-x2", x: "fam-x", y: "fam-y", "": "fam-k"};
var FAM_NOMBRE = {x2: T("the x² family", "familia de x²"), x: T("the x family", "familia de x"), y: T("the y family", "familia de y"), "": T("constants", "constantes")};
function termFamVis(tt, primero){
  var a = Math.abs(tt.c), cuerpo = tt.v === "" ? String(a) : (a === 1 ? "" : a) + VAR_VIS[tt.v];
  return (tt.c < 0 ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + '<span class="' + FAM_CLASE[tt.v] + '">' + cuerpo + "</span>";
}
function polFamVis(p){ return p.map(function(tt, i){ return termFamVis(tt, i === 0); }).join(""); }
function polSemejantes(){
  var fams = baraja(["x", "y", ""]).slice(0, aleatorio(2, 3)); if (Math.random() < 0.3) fams.push("x2");
  var p = [];
  fams.forEach(function(v){ var k = aleatorio(1, 2); for (var i = 0; i < (k === 1 ? 2 : aleatorio(2, 3)); i++) p.push(tm(v === "" ? nz() : elige([1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5]), v)); });
  p = baraja(p);
  if (p.length > 6) p = p.slice(0, 6);
  return p;
}
var FA = {p: null, pasos: [], visto: 0};
function preparaFA(p){
  FA.p = p; FA.pasos = []; FA.visto = 0;
  var r = reducePol(p), fams = ORDEN_VAR.filter(function(v){ return p.some(function(tt){ return tt.v === v; }); });
  $("fa-expr").innerHTML = polHTML(p);
  FA.pasos.push(T("Find the family of each term: ", "Se identifica la familia de cada término: ") + envuelve(polFamVis(p), polVoz(p)) + ".");
  var grupos = fams.map(function(v){ return "(" + polVis(p.filter(function(tt){ return tt.v === v; })) + ")"; });
  FA.pasos.push(T("Group them by family: ", "Se agrupan por familias: ") + auto(grupos.join(" + ")) + ".");
  var lineas = fams.map(function(v){
    var g = p.filter(function(tt){ return tt.v === v; }), s = g.reduce(function(a, tt){ return a + tt.c; }, 0);
    return mayus(FAM_NOMBRE[v]) + ": " + g.map(function(tt){ return menosV(tt.c); }).join(" + ").replace(/\+ −/g, "− ") + " = " + menosV(s) + (s === 0 ? T(" (the family cancels out)", " (la familia se anula)") : "");
  });
  FA.pasos.push(T("Combine the coefficients in each family. ", "Se combinan los coeficientes de cada familia. ") + lineas.join(". ") + ".");
  FA.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + polHTML(p) + " = " + polHTML(r) + "</span>");
  pintaFA();
}
function pintaFA(){
  $("fa-pasos").innerHTML = FA.pasos.slice(0, FA.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === FA.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("fa-sig"); b.disabled = FA.visto >= FA.pasos.length; $("fa-todo").disabled = b.disabled;
  b.textContent = FA.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
var FA_COLA = [[tm(3, "x"), tm(5, "x")], [tm(7, "x"), tm(-2, "x"), tm(4)], [tm(3, "x"), tm(5), tm(-2, "y"), tm(1, "x"), tm(4, "y"), tm(-7)]];

/* Sorting terms into families: two tries */
var CF = {p: null, primero: 0, pista: 0, total: 0, resuelta: false, intentos: 0};
function pintaCF(){
  CF.p = polSemejantes(); CF.resuelta = false; CF.intentos = 0;
  $("cf-enun").innerHTML = T("Expression: ", "Expresión: ") + polHTML(CF.p) + T(". Choose the family of each term.", ". Elija la familia de cada término.");
  var h = "";
  CF.p.forEach(function(tt, i){
    h += '<div class="fila-term" id="cf-fila' + i + '"><span class="t">' + auto(termVis(tt, true)) + "</span>" +
         '<label class="sr-only" for="cf-s' + i + '">' + T("Family of the term ", "Familia del término ") + vozAuto(termVis(tt, true)) + "</label>" +
         '<select id="cf-s' + i + '"><option value="-">' + T("Choose the family", "Elija la familia") + '</option><option value="x2">' + T("x² family", "Familia de x²") + '</option><option value="x">' + T("x family", "Familia de x") + '</option><option value="y">' + T("y family", "Familia de y") + '</option><option value="k">' + T("Constants", "Constantes") + "</option></select></div>";
  });
  $("cf-filas").innerHTML = h;
  $("cf-comprobar").disabled = false;
  $("cf-fb").className = "fb"; $("cf-fb").innerHTML = "";
}
function compruebaCF(){
  if (CF.resuelta) return;
  var fb = $("cf-fb"), vacios = CF.p.filter(function(tt, i){ return $("cf-s" + i).value === "-"; }).length, bien = 0;
  if (vacios){ fb.className = "fb pista"; fb.innerHTML = T("Choose the family of every term before you check.", "Elija la familia de todos los términos antes de comprobar."); return; }
  CF.intentos++;
  CF.p.forEach(function(tt, i){ var ok = $("cf-s" + i).value === (tt.v === "" ? "k" : tt.v); $("cf-fila" + i).className = "fila-term " + (ok ? "bien" : "mal"); if (ok) bien++; });
  var final = T("Combining each family gives ", "Al combinar cada familia queda ") + polHTML(reducePol(CF.p)) + ".";
  if (bien < CF.p.length && CF.intentos < 2){
    fb.className = "fb pista";
    fb.innerHTML = TX.todavia + T(bien + " of " + CF.p.length + " are right. Change the ones marked in red: the family depends on the variable part and its exponent, not on the coefficient.", "Acertó " + bien + " de " + CF.p.length + ". Cambie los marcados en rojo: la familia la decide la parte con variable y su exponente, no el coeficiente.") + TX.unoMas;
    return;
  }
  CF.resuelta = true; CF.total++;
  CF.p.forEach(function(tt, i){ $("cf-s" + i).disabled = true; if ($("cf-s" + i).value !== (tt.v === "" ? "k" : tt.v)) $("cf-s" + i).value = tt.v === "" ? "k" : tt.v; });
  if (bien === CF.p.length){ if (CF.intentos === 1) CF.primero++; else CF.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + T("Every term is in its family. ", "Todos los términos están en su familia. ") + final; }
  else { fb.className = "fb mal"; fb.innerHTML = TX.asi + T("The lists now show the right family of each term. ", "Las listas muestran ahora la familia correcta de cada término. ") + final + TX.nuevo; }
  $("cf-comprobar").disabled = true;
  $("cf-marcador").textContent = TX.resueltos(CF.primero + CF.pista, CF.primero, CF.total);
}
function genSimplificar(){
  var p = polSemejantes(), r = reducePol(p), o = [], pc = {}, usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opPol(r));
  var todo = p.reduce(function(a, tt){ return a + tt.c; }, 0);
  mete(opPol(todo === 0 ? [] : [tm(todo, "x")]), T("Only terms in the same family combine.", "Solo se combinan términos de la misma familia."));
  var neg = p.filter(function(tt){ return tt.c < 0; });
  if (neg.length){ var cambia = neg[0]; mete(opPol(reducePol(p.map(function(tt){ return tt === cambia ? tm(-tt.c, tt.v) : tt; }))), T("Check the signs: the sign in front belongs to the term.", "Revise los signos: el signo que va delante pertenece al término.")); }
  if (p.some(function(tt){ return tt.v === "x2"; })) mete(opPol(reducePol(p.map(function(tt){ return tt.v === "x2" ? tm(tt.c, "x") : tt; }))), T("x² and x are not like terms: the exponents are different.", "x² y x no son semejantes: los exponentes son distintos."));
  if (p.some(function(tt){ return tt.v === ""; }) && p.some(function(tt){ return tt.v === "x"; })) mete(opPol(reducePol(p.map(function(tt){ return tt.v === "" ? tm(tt.c, "x") : tt; }))), T("Constants have no x: they do not combine with the x terms.", "Las constantes no tienen x: no se combinan con los términos en x."));
  if (r.length) mete(opPol(r.map(function(tt, i){ return i === 0 ? tm(tt.c + 1, tt.v) : tt; })), T("Check the coefficients again.", "Revise otra vez los coeficientes."));
  if (r.length) mete(opPol(r.map(function(tt, i){ return i === r.length - 1 ? tm(tt.c - 1 || -1, tt.v) : tt; })), T("Check the coefficients again.", "Revise otra vez los coeficientes."));
  return {enun: T("Simplify ", "Simplifique ") + polHTML(p) + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("Grouping by families: ", "Agrupando por familias: ") + envuelve(polFamVis(p), polVoz(p)) + " = " + polHTML(r) + ".", mal: T("The simplified form is ", "La forma simplificada es ") + polHTML(r) + "."};
}

/* ============ MODULE 4 · the distributive property ============ */
function pintaArea(){
  var at = $("ar-a").value.trim(), ct = $("ar-c").value.trim(), a = /^\d$/.test(at) ? +at : 0, c = /^\d$/.test(ct) ? +ct : 0;
  if (a < 1 || c < 1){ $("ar-svg").innerHTML = ""; $("ar-salida").innerHTML = T("Type whole numbers from 1 to 9.", "Escriba números enteros de 1 a 9."); return; }
  var H = 40 + a * 16, wx = 220, wc = c * 28, x0 = 60, y0 = 30;
  var s = '<svg class="balanza" viewBox="0 0 ' + (x0 + wx + wc + 30) + " " + (y0 + H + 50) + '" role="img" aria-label="' + T("Rectangle with height " + a + " and base x plus " + c + ", split in two: an area of " + a + " x and another of " + (a * c), "Rectángulo de altura " + a + " y base x más " + c + ", partido en dos: un área de " + a + " x y otra de " + (a * c)) + '">';
  s += '<rect x="' + x0 + '" y="' + y0 + '" width="' + wx + '" height="' + H + '" fill="#e3f2fd" stroke="#0d47a1" stroke-width="2"/>';
  s += '<rect x="' + (x0 + wx) + '" y="' + y0 + '" width="' + wc + '" height="' + H + '" fill="#fff8e1" stroke="#5c3900" stroke-width="2"/>';
  s += '<text x="' + (x0 + wx / 2) + '" y="' + (y0 + H / 2 + 7) + '" text-anchor="middle" font-size="22" font-weight="700" fill="#0d47a1">' + a + "x</text>";
  s += '<text x="' + (x0 + wx + wc / 2) + '" y="' + (y0 + H / 2 + 7) + '" text-anchor="middle" font-size="' + (wc < 60 ? 16 : 22) + '" font-weight="700" fill="#5c3900">' + (a * c) + "</text>";
  s += '<text x="' + (x0 + wx / 2) + '" y="' + (y0 + H + 28) + '" text-anchor="middle" font-size="20" fill="#222">x</text>';
  s += '<text x="' + (x0 + wx + wc / 2) + '" y="' + (y0 + H + 28) + '" text-anchor="middle" font-size="20" fill="#222">' + c + "</text>";
  s += '<text x="' + (x0 - 14) + '" y="' + (y0 + H / 2 + 7) + '" text-anchor="end" font-size="20" fill="#222">' + a + "</text></svg>";
  $("ar-svg").innerHTML = s;
  $("ar-salida").innerHTML = '<div class="linea">' + T("Area as one piece: height times base = ", "Área de una sola pieza: altura por base = ") + auto(a + "(x + " + c + ")") + ".</div>" +
    '<div class="linea">' + T("Area by parts: ", "Área por partes: ") + auto(a + " · x = " + a + "x") + T(" and ", " y ") + auto(a + " · " + c + " = " + (a * c)) + ".</div>" +
    '<div class="linea veredicto">' + T("It is the same area: ", "Son la misma área: ") + auto(a + "(x + " + c + ") = " + a + "x + " + (a * c)) + "</div>";
}
var P5 = {primero: 0, pista: 0, total: 0, resuelta: false, intentos: 0, a: 0, b: 0, c: 0};
function pintaP5(){
  P5.a = elige([2, 3, 4, 5, 6, 7, -2, -3, -4, -5]); P5.b = elige([1, 1, 2, 3, 4]); P5.c = nz(); P5.resuelta = false; P5.intentos = 0;
  $("p5-enun").innerHTML = T("Distribute: ", "Distribuya: ") + auto(menosV(P5.a) + "(" + polVis([tm(P5.b, "x"), tm(P5.c)]) + ")");
  ["p5-a", "p5-b"].forEach(function(id){ $(id).value = ""; $(id).disabled = false; $(id).classList.remove("error"); });
  $("p5-comprobar").disabled = false; $("p5-fb").className = "fb"; $("p5-fb").innerHTML = "";
}
function compruebaP5(){
  if (P5.resuelta) return;
  var A = leeEntero($("p5-a").value), Bb = leeEntero($("p5-b").value), fb = $("p5-fb");
  $("p5-a").classList.toggle("error", A === null); $("p5-b").classList.toggle("error", Bb === null);
  if (A === null || Bb === null){ fb.className = "fb pista"; fb.innerHTML = T("Type two whole numbers, with a minus sign if one is negative.", "Escriba dos números enteros, con su signo si es negativo."); return; }
  var ra = P5.a * P5.b, rb = P5.a * P5.c, res = polHTML([tm(ra, "x"), tm(rb)]);
  var explica = T("Multiply ", "Se multiplica ") + menosV(P5.a) + T(" by each term: ", " por cada término: ") + auto("(" + menosV(P5.a) + ")(" + polVis([tm(P5.b, "x")]) + ") = " + polVis([tm(ra, "x")])) + T(" and ", " y ") +
                auto("(" + menosV(P5.a) + ")(" + menosV(P5.c) + ") = " + menosV(rb)) + ".";
  P5.intentos++;
  if (A === ra && Bb === rb){
    P5.resuelta = true; P5.total++; if (P5.intentos === 1) P5.primero++; else P5.pista++;
    fb.className = "fb bien"; fb.innerHTML = TX.bien + res + ". " + explica + " <em>" + elige(P5.intentos === 1 ? ELOGIO : ELOGIO2) + "</em>";
  } else if (P5.intentos >= 2){
    P5.resuelta = true; P5.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + res + ". " + explica + TX.nuevo;
  } else {
    var msg = T("Multiply the number outside by each term inside.", "Multiplique el número de fuera por cada término de dentro.");
    if (A === ra && Bb === P5.c) msg = T("The first term is right, but " + menosV(P5.a) + " also multiplies the second term.", "El primer término está bien, pero el " + menosV(P5.a) + " también multiplica al segundo término.");
    else if (A === ra && Bb === -rb) msg = T("Check the sign of the second product: (" + menosV(P5.a) + ")(" + menosV(P5.c) + ").", "Revise el signo del segundo producto: (" + menosV(P5.a) + ")(" + menosV(P5.c) + ").");
    else if (A === -ra) msg = T("Check the sign of the first product.", "Revise el signo del primer producto.");
    else if (Bb === rb) msg = T("The constant is right; check the coefficient of x.", "La constante está bien; revise el coeficiente de x.");
    fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas;
  }
  if (P5.resuelta){ $("p5-a").disabled = true; $("p5-b").disabled = true; $("p5-comprobar").disabled = true; }
  $("p5-marcador").textContent = P5.total ? TX.resueltos(P5.primero + P5.pista, P5.primero, P5.total) : "";
}
function genDistCombina(){
  var a = aleatorio(2, 6), b = nz(), c = elige([1, 2, 3, 4, 5, -1, -2, -3]), d = Math.random() < 0.5 ? nz() : 0;
  var orig = auto(a + "(" + polVis([tm(1, "x"), tm(b)]) + ")" + termVis(tm(c, "x"), false) + (d ? termVis(tm(d), false) : ""));
  var r = reducePol([tm(a, "x"), tm(a * b), tm(c, "x"), tm(d)]), o = [], pc = {}, usadas = {};
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opPol(r));
  mete(opPol(reducePol([tm(a, "x"), tm(b), tm(c, "x"), tm(d)])), T("The " + a + " also multiplies the " + menosV(b) + " in the parentheses.", "El " + a + " multiplica también al " + menosV(b) + " del paréntesis."));
  mete(opPol(reducePol([tm(a + c + a * b + d, "x")])), T("Constants do not combine with the x terms.", "Las constantes no se combinan con los términos en x."));
  mete(opPol(reducePol([tm(a * c, "x"), tm(a * b), tm(d)])), T("Add the x terms after distributing; do not multiply them.", "Los términos en x se suman después de distribuir; no se multiplican."));
  mete(opPol(reducePol([tm(a, "x"), tm(-a * b), tm(c, "x"), tm(d)])), T("Check the sign of " + a + " · " + menosV(b) + ".", "Revise el signo de " + a + " · " + menosV(b) + "."));
  return {enun: T("Simplify ", "Simplifique ") + orig + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("First distribute: ", "Primero se distribuye: ") + polHTML([tm(a, "x"), tm(a * b), tm(c, "x")].concat(d ? [tm(d)] : [])) + T("; then combine like terms.", "; después se combinan los términos semejantes."),
    mal: T("Distribute and combine: the result is ", "Se distribuye y se combina: el resultado es ") + polHTML(r) + "."};
}

/* ============ MODULE 5 · evaluating expressions ============ */
function coefSust(c, primero, cuerpo){ var a = Math.abs(c), s = c < 0 ? (primero ? "−" : " − ") : (primero ? "" : " + "); return s + (a === 1 ? "" : a) + cuerpo; }
function evaluaPasos(A, Bc, C, v){
  var pv = "(" + menosV(v) + ")", pol = [], sust = "", primero = true, pasos = [];
  if (A){ pol.push(tm(A, "x2")); sust += coefSust(A, primero, pv + "<sup>2</sup>"); primero = false; }
  if (Bc){ pol.push(tm(Bc, "x")); sust += coefSust(Bc, primero, pv); primero = false; }
  if (C || primero){ pol.push(tm(C)); sust += (C < 0 ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + Math.abs(C); }
  pasos.push(T("Replace x with ", "Se sustituye x por ") + auto(pv) + ": " + auto(sust) + ".");
  var tA = A * v * v, tB = Bc * v, val = tA + tB + C;
  if (A) pasos.push(T("First the power: ", "Primero la potencia: ") + auto(pv + "<sup>2</sup> = " + menosV(v * v)) + (v < 0 ? T(" (a negative number squared is positive).", " (un negativo al cuadrado da positivo).") : ".") +
                    (A === -1 ? T(" The minus sign in front is not inside the parentheses, so it is applied afterward: ", " El signo menos de delante no está dentro del paréntesis, así que se aplica después: ") + auto("−" + menosV(v * v) + " = " + menosV(-v * v)) + "." : ""));
  var mults = [];
  if (A && Math.abs(A) !== 1) mults.push(auto(menosV(A) + " · " + menosV(v * v) + " = " + menosV(tA)));
  if (Bc && Math.abs(Bc) !== 1) mults.push(auto(menosV(Bc) + " · " + pv + " = " + menosV(tB)));
  if (mults.length) pasos.push(T("Then the multiplications: ", "Después las multiplicaciones: ") + mults.join(T(" and ", " y ")) + ".");
  var partes = [];
  if (A) partes.push(tA); if (Bc) partes.push(tB); if (C || !partes.length) partes.push(C);
  var sumaTxt = partes.map(function(x, i){ return i === 0 ? menosV(x) : (x < 0 ? " − " + Math.abs(x) : " + " + x); }).join("");
  if (partes.length > 1) pasos.push(T("Last, add and subtract from left to right: ", "Por último, sumas y restas de izquierda a derecha: ") + auto(sumaTxt + " = " + menosV(val)) + ".");
  pasos.push('<span class="veredicto">' + T("Answer: when x = " + menosV(v) + ", the expression equals " + menosV(val) + ".", "Resultado: cuando x = " + menosV(v) + ", la expresión vale " + menosV(val) + ".") + "</span>");
  return {pol: pol, pasos: pasos, val: val, tA: tA, tB: tB};
}
var EV = {pasos: [], visto: 0, cola: [[0, 2, 5, 3], [1, 0, 1, 4], [1, 0, 0, -3], [-1, 0, 0, -3], [3, -2, 1, -2]]};
function nuevoEV(){
  var e = EV.cola.length ? EV.cola.shift() : [elige([0, 1, -1, 2, 3]), elige([0, 2, 3, -4, 5, -1]), nz(), elige([-4, -3, -2, -1, 2, 3, 4, 5])];
  if (!e[0] && !e[1]) e[1] = 2;
  var R = evaluaPasos(e[0], e[1], e[2], e[3]);
  EV.pasos = R.pasos; EV.visto = 0;
  $("ev-expr").innerHTML = T("Evaluate ", "Evaluar ") + '<span class="grande">' + polHTML(R.pol) + "</span>" + T(" when x = ", " cuando x = ") + menosV(e[3]);
  pintaEV();
}
function pintaEV(){
  $("ev-pasos").innerHTML = EV.pasos.slice(0, EV.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === EV.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("ev-sig"); b.disabled = EV.visto >= EV.pasos.length; $("ev-todo").disabled = b.disabled;
  b.textContent = EV.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function genEvaluar(){
  var A = elige([0, 0, 1, -1, 2, 3]), Bc = elige([0, 2, 3, -2, -4, 5, 1, -1]), C = nz(), v = elige([-5, -4, -3, -2, -1, 2, 3, 4, 5, 6]);
  if (!A && !Bc) Bc = 3;
  var R = evaluaPasos(A, Bc, C, v), pistas = [];
  if (A && v < 0) pistas.push({v: fr(-R.tA + R.tB + C), msg: T("Check the power: a negative number squared is positive, (" + menosV(v) + ")² = " + (v * v) + ".", "Revise la potencia: un número negativo al cuadrado da positivo, (" + menosV(v) + ")² = " + (v * v) + ".")});
  if (A === -1) pistas.push({v: fr(v * v + R.tB + C), msg: T("The minus sign of −x² is applied after squaring: −(" + menosV(v) + ")² = " + menosV(-v * v) + ".", "El signo menos de −x² se aplica después de elevar al cuadrado: −(" + menosV(v) + ")² = " + menosV(-v * v) + ".")});
  if (Bc && v < 0) pistas.push({v: fr(R.tA - R.tB + C), msg: T("Check the sign when you multiply by a negative number.", "Revise el signo al multiplicar por un número negativo.")});
  if (A && Math.abs(A) > 1) pistas.push({v: fr(A * A * v * v + R.tB + C), msg: T("First square the value of x, then multiply by the coefficient.", "Primero se eleva al cuadrado el valor de x y después se multiplica por el coeficiente.")});
  return {enun: T("Evaluate ", "Evalúe ") + polHTML(R.pol) + T(" when x = ", " cuando x = ") + menosV(v) + ".",
    solucion: T("The value is ", "El valor es ") + menosV(R.val) + ". " + R.pasos.slice(0, -1).join(" "),
    evalua: function(txt){ return evaluaNumero(txt, fr(R.val), pistas); }};
}

/* ============ Start ============ */
$("an-nuevo").addEventListener("click", pintaAnatomia);
pintaAnatomia();
OMR("p1", genPartes);
OMR("p2", genTraducir);
OMR("p3", genAPalabras);
$("fa-sig").addEventListener("click", function(){ if (FA.visto < FA.pasos.length){ FA.visto++; pintaFA(); } });
$("fa-todo").addEventListener("click", function(){ FA.visto = FA.pasos.length; pintaFA(); });
$("fa-nuevo").addEventListener("click", function(){ preparaFA(FA_COLA.length ? FA_COLA.shift() : polSemejantes()); });
preparaFA(FA_COLA.shift());
$("cf-comprobar").addEventListener("click", compruebaCF);
$("cf-nuevo").addEventListener("click", pintaCF);
pintaCF();
OMR("p4", genSimplificar);
["ar-a", "ar-c"].forEach(function(id){ $(id).addEventListener("input", pintaArea); });
pintaArea();
$("p5-comprobar").addEventListener("click", compruebaP5);
$("p5-nuevo").addEventListener("click", pintaP5);
["p5-a", "p5-b"].forEach(function(id){ $(id).addEventListener("keydown", function(ev){ if (ev.key === "Enter") compruebaP5(); }); });
pintaP5();
OMR("p6", genDistCombina);
$("ev-sig").addEventListener("click", function(){ if (EV.visto < EV.pasos.length){ EV.visto++; pintaEV(); } });
$("ev-todo").addEventListener("click", function(){ EV.visto = EV.pasos.length; pintaEV(); });
$("ev-nuevo").addEventListener("click", nuevoEV);
nuevoEV();
creaPracticaLibre("p7", genEvaluar);
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}"

def campo(i, etiqueta, valor):
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="text" inputmode="numeric" class="corto" id="{i}" value="{valor}"></div>'

def pasos_panel(pre, extra_estado=""):
    return f'''      <div class="panel">
        <div class="estado"><span{extra_estado} id="{pre}-expr"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig"></button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="{pre}-nuevo">{t("Another example", "Otro ejemplo")}</button></div>
      </div>
      <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>'''

def practica_pagina():
    n = N
    P = n3
    mods = [
     (t("vocabulary", "vocabulario"), t("Variables, terms, and coefficients", "Variables, términos y coeficientes"),
      f'''      <p>{t("A <strong>variable</strong> is a letter that stands for an unknown number. An <strong>algebraic expression</strong> combines variables, numbers, and operations. Each part separated by + or − is a <strong>term</strong>; the number that multiplies the variable is its <strong>coefficient</strong>, and the term with no variable is the <strong>constant</strong>.", "Una <strong>variable</strong> es una letra que representa un número desconocido. Una <strong>expresión algebraica</strong> combina variables, números y operaciones. Cada parte separada por + o − es un <strong>término</strong>; el número que multiplica a la variable es su <strong>coeficiente</strong>, y el término sin variable es la <strong>constante</strong>.")}</p>
      <h3>{t("The anatomy of an expression", "Anatomía de una expresión")}</h3>
      <p>{t("Each term is taken apart into its pieces. Look at the signs: the sign in front belongs to the term.", "Cada término aparece desarmado en sus partes. Fíjese en los signos: el signo que va delante pertenece al término.")}</p>
      <div class="panel">
        <div class="estado"><span class="grande" id="an-expr"></span></div>
        <div class="tabla-scroll"><table class="comparar" id="an-tabla"></table></div>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn-sec" id="an-nuevo">{t("Another expression", "Otra expresión")}</button></div>
      </div>
      <div class="caja-tip"><strong>{t("The invisible coefficient:", "Coeficiente invisible:")}</strong> {t("when a variable appears alone, like x, its coefficient is 1 (x = 1x). In the same way, −x means −1x.", "cuando una variable aparece sola, como x, su coeficiente es 1 (x = 1x). De igual modo, −x significa −1x.")}</div>
{B.om("p1", t("Practice: identify the parts", "Practique: identifique las partes"))}'''),
     (t("translate", "traducir"), t("Translating between words and algebra", "Traducir entre palabras y álgebra"),
      f'''      <p>{t("Certain words always point to the same operation:", "Ciertas palabras señalan siempre la misma operación:")}</p>
      <table class="reglas">
        <caption>{t("Key words and their operation", "Palabras clave y su operación")}</caption>
        <thead><tr><th scope="col">{t("Operation", "Operación")}</th><th scope="col">{t("Words that signal it", "Palabras que la indican")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Addition", "Suma")}</td><td>{t("plus, increased by, the sum of, more than", "más, aumentado en, la suma de, más que")}</td></tr>
          <tr><td>{t("Subtraction", "Resta")}</td><td>{t("minus, decreased by, the difference of, less than", "menos, disminuido en, la diferencia entre, menos que")}</td></tr>
          <tr><td>{t("Multiplication", "Multiplicación")}</td><td>{t("times, twice, three times, the product of", "veces, el doble, el triple, el producto de")}</td></tr>
          <tr><td>{t("Division", "División")}</td><td>{t("half, a third, divided by, the quotient of", "la mitad, el tercio, dividido entre, el cociente de")}</td></tr>
        </tbody>
      </table>
{P.atencion(t("Order matters in subtraction:", "El orden importa en la resta:"), t("“a number decreased by 4” is x − 4, but “4 decreased by a number” is 4 − x. And “8 less than a number” is x − 8: you take 8 away from the number.", "«un número disminuido en 4» es x − 4, pero «4 disminuido en un número» es 4 − x. Y «8 menos que un número» es x − 8: al número se le quitan 8."))}
{B.om("p2", t("Practice: from words to algebra", "Practique: de palabras a álgebra"))}
{B.om("p3", t("Practice: from algebra to words", "Practique: de álgebra a palabras"))}'''),
     (t("like-terms", "semejantes"), t("Combining like terms", "Combinar términos semejantes"),
      f'''      <p>{t("Two terms are <strong>like terms</strong> if they have the same variable raised to the same exponent. Each kind of term forms a “family,” and only terms in the same family combine, by adding or subtracting their coefficients. Constants form their own family.", "Dos términos son <strong>semejantes</strong> si tienen la misma variable elevada al mismo exponente. Cada tipo de término forma una «familia», y solo se combinan los de la misma familia, sumando o restando sus coeficientes. Las constantes forman su propia familia.")}</p>
      <p><span class="fam-x2">x<sup>2</sup></span> &nbsp; <span class="fam-x">x</span> &nbsp; <span class="fam-y">y</span> &nbsp; <span class="fam-k">{t("constants", "constantes")}</span></p>
      <h3>{t("Step by step, by families", "Paso a paso por familias")}</h3>
{pasos_panel("fa", ' class="grande"')}
      <h3>{t("Practice: sort each term into its family", "Practique: clasifique cada término en su familia")}</h3>
      <div class="practica" id="cf">
        <div class="enun" id="cf-enun"></div>
        <div id="cf-filas"></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="cf-comprobar">Check</button>
          <button type="button" class="btn-sec" id="cf-nuevo">{t("Another expression", "Otra expresión")}</button>
        </div>
        <div class="fb" id="cf-fb" role="status"></div>
        <p class="marcador" id="cf-marcador"></p>
      </div>
{P.atencion(t("Different terms do not combine:", "No se combinan términos distintos:"), t("4x + 2y does not simplify, because x and y are different variables. And 3x + 5 is not 8x, because the 5 has no x. Also, 3x<sup>2</sup> + 2x is not 5x<sup>2</sup>: the exponents are different.", "4x + 2y no se simplifica, porque x y y son variables diferentes. Tampoco 3x + 5 da 8x, porque el 5 no tiene x. Y 3x<sup>2</sup> + 2x no es 5x<sup>2</sup>: los exponentes son distintos."))}
{B.om("p4", t("Practice: simplify the expression", "Practique: simplifique la expresión"))}'''),
     (t("distributive", "distributiva"), t("The distributive property", "La propiedad distributiva"),
      f'''      <p>{t("When a number multiplies a sum or a difference in parentheses, it multiplies <strong>each term</strong> inside, not just the first one.", "Cuando un número multiplica a una suma o a una resta entre paréntesis, multiplica a <strong>cada término</strong> de adentro, no solo al primero.")}</p>
{P.formula("a(b + c) = a · b + a · c")}
      <h3>{t("Why it works: the area model", "Por qué funciona: el modelo de área")}</h3>
      <p>{t("A rectangle with height a and base (x + c) can be split in two. The total area is the same however you work it out.", "Un rectángulo de altura a y base (x + c) se puede partir en dos. El área total es la misma, se calcule como se calcule.")}</p>
      <div class="panel"><div class="campos">
        {campo("ar-a", t("Height (1 to 9)", "Altura (de 1 a 9)"), 3)}
        {campo("ar-c", t("Number in the parentheses (1 to 9)", "Número dentro del paréntesis (de 1 a 9)"), 4)}
      </div></div>
      <div id="ar-svg"></div>
{P.salida("ar-salida")}
{P.atencion(t("With signs:", "Con signos:"), t("the sign of the factor is shared out too. −2(x − 5) = −2x + 10, because (−2)(−5) = +10. The most common mistake is to multiply only the first term: 3(x + 4) is not 3x + 4.", "el signo del factor también se reparte. −2(x − 5) = −2x + 10, porque (−2)(−5) = +10. El error más frecuente es multiplicar solo el primer término: 3(x + 4) no es 3x + 4."))}
      <h3>{t("Practice: distribute", "Practique: distribuya")}</h3>
      <div class="practica" id="p5">
        <div class="enun" id="p5-enun"></div>
        <div class="campos campos-sci">
          <div class="campo"><label for="p5-a">{t("Coefficient of x", "Coeficiente de x")}</label><input type="text" autocomplete="off" class="corto" id="p5-a"></div>
          <div class="campo" aria-hidden="true" style="font-size:20px;font-weight:700;padding-bottom:8px;">x +</div>
          <div class="campo"><label for="p5-b">{t("Constant", "Constante")}</label><input type="text" autocomplete="off" class="corto" id="p5-b"></div>
        </div>
        <p class="nota">{t("Type the numbers with their signs. For example, for −2x + 10 type −2 and 10; for 3x − 12 type 3 and −12.", "Escriba los números con su signo. Por ejemplo, para −2x + 10 escriba −2 y 10; para 3x − 12 escriba 3 y −12.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="p5-comprobar">Check</button>
          <button type="button" class="btn-sec" id="p5-nuevo">New exercise</button>
        </div>
        <div class="fb" id="p5-fb" role="status"></div>
        <p class="marcador" id="p5-marcador"></p>
      </div>
{B.om("p6", t("Practice: distribute and combine", "Practique: distribuya y combine"))}'''),
     (t("evaluate", "evaluar"), t("Evaluating expressions", "Evaluar expresiones"),
      f'''      <p>{t("To evaluate, replace the variable with a value and work it out, following the order of operations: parentheses, exponents, multiplication and division, addition and subtraction.", "Evaluar es sustituir la variable por un valor y calcular, respetando el orden de las operaciones: paréntesis, exponentes, multiplicación y división, suma y resta.")}</p>
      <h3>{t("Substitution, step by step", "Sustitución paso a paso")}</h3>
{pasos_panel("ev")}
      <div class="caja-tip"><strong>{t("Use parentheses when you substitute:", "Use paréntesis al sustituir:")}</strong> {t("writing 2(3) instead of 23 keeps you from confusing the multiplication with a two-digit number. With negative numbers it is essential: if x = −3, then x<sup>2</sup> = (−3)<sup>2</sup> = 9, but −x<sup>2</sup> = −(−3)<sup>2</sup> = −9.", "escribir 2(3) en lugar de 23 evita confundir la multiplicación con un número de dos cifras. Con negativos es imprescindible: si x = −3, entonces x<sup>2</sup> = (−3)<sup>2</sup> = 9, pero −x<sup>2</sup> = −(−3)<sup>2</sup> = −9.")}</div>
{B.libre("p7", t("Practice: evaluate the expression", "Practique: evalúe la expresión"), t("Result", "Resultado"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Type a whole number, with a minus sign if it is negative.", "Escriba un número entero, con signo menos si es negativo.") + '</p>\n        <div class="fila-btn">', 1)}''')]
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Variables, expresiones algebraicas y traducción")
