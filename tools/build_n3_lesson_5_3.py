"""Level 3 · Lesson 5.3 · Solving literal formulas, and a general strategy — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "5-3"
TEMA = ("Inequalities and formulas", "Inecuaciones y fórmulas")
TIT = ("Solving literal formulas, and a general strategy", "Despeje de fórmulas literales y estrategia general de resolución")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def leccion():
    n = N
    pasos4 = [t("Identify the variable you want to solve for.", "Identificar qué variable se quiere despejar."),
              t("Isolate it with the properties of equality (inverse operations), treating the other letters as numbers.", "Aislarla con las propiedades de igualdad (operaciones inversas), tratando las demás letras como números."),
              t("Simplify the result, with a fraction if needed.", "Simplificar el resultado, con fracción si es necesario."),
              t("Check that the variable you want is alone on one side.", "Verificar que la variable buscada quedó sola de un lado.")]
    s1 = f'''<p>{t("Throughout Topic 4 and the first part of Topic 5 you solved equations and inequalities to find the value of x. Solving a formula is exactly the same, with one difference: the variable you want is surrounded by other letters instead of numbers. As the key idea says, “solving a formula is solving an equation where the variable is a symbol, not a number.”",
"A lo largo del Tema 4 y la primera parte del Tema 5 se resolvieron ecuaciones e inecuaciones para encontrar el valor de x. Despejar una fórmula es exactamente lo mismo, con una diferencia: la variable que se busca está rodeada de otras letras en lugar de números. Como dice la idea clave, «despejar es resolver una ecuación donde la variable es un símbolo, no un número».")}</p>
<p>{t("A <strong>literal formula</strong> relates several amounts with letters, like d = rt (distance = rate × time). <strong>Solving for</strong> one of them means rewriting the formula so that this variable is alone on one side. You treat the other letters as if they were known numbers.", "Una <strong>fórmula literal</strong> relaciona varias cantidades con letras, como d = rt (distancia = rapidez × tiempo). <strong>Despejar</strong> una de ellas significa reescribir la fórmula para que esa variable quede sola de un lado. Las demás letras se tratan como si fueran números conocidos.")}</p>
{ejemplo(t("Example 1: in d = rt, solve for t", "Ejemplo 1: en d = rt, despeje t"),
  [("1", t("t is multiplied by r.", "La t está multiplicada por r."), t("To isolate it, divide both sides by r.", "Para aislarla, se divide entre r en ambos lados.")),
   ("2", t("Divide.", "Dividir."), f"{fx('d', 'r')} = t."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>t = {fx('d', 'r')}</strong>")])}
{caja("tip", t("The other letters are “numbers”", "Las otras letras son «números»"), t("<p>When you solve d = rt for t, you treat r just like a number. Dividing by r is like dividing by 5 or any other number: an inverse operation to isolate the variable you want.</p>", "<p>Al despejar t en d = rt, la r se trata igual que un número. Dividir entre r es como dividir entre 5 o entre cualquier número: una operación inversa para aislar la variable buscada.</p>"))}'''

    s2 = f'''<p>{t("To solve for any variable, you always follow the same sequence.", "Para despejar cualquier variable se sigue siempre la misma secuencia.")}</p>
<ol>{"".join(f"<li>{p}</li>" for p in pasos4)}</ol>
{enlace(n, t("solve-for", "despejar"), t("the four-step strategy", "la estrategia de cuatro pasos"), t("Solve for the variable you are asked for, as if it were an equation with letters.", "Despeje la variable pedida como si fuera una ecuación con letras."))}'''

    filas = [[t("Area of a rectangle", "Área de un rectángulo"), "A = bh"], [t("Perimeter of a rectangle", "Perímetro de un rectángulo"), "P = 2l + 2w"], [t("Volume of a box", "Volumen de una caja"), "V = lwh"],
             [t("Simple interest", "Interés simple"), "I = Prt"], [t("Distance", "Distancia"), "d = rt"], [t("Temperature (°F from °C)", "Temperatura (°F a partir de °C)"), f"F = {fx(9, 5)}C + 32"]]
    s3 = f'''<p>{t("These are some of the formulas that come up most on the GED test. In each one you can solve for any of its variables.", "Estas son algunas de las fórmulas que más aparecen en el examen GED. En cada una se puede despejar cualquiera de sus variables.")}</p>
{tabla(t("Common GED formulas", "Fórmulas de uso frecuente en el GED"), t("Formulas that appear often on the GED test", "Fórmulas de uso frecuente en el GED"), [t("Situation", "Contexto"), t("Formula", "Fórmula")], filas)}
{ejemplo(t("Example 2: in A = bh, solve for h", "Ejemplo 2: en A = bh, despeje h"),
  [("1", t("h is multiplied by b.", "La h está multiplicada por b."), t("Divide both sides by b.", "Se divide entre b en ambos lados.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>h = {fx('A', 'b')}</strong>")])}
{ejemplo(t("Example 3: in I = Prt, solve for P", "Ejemplo 3: en I = Prt, despeje P"),
  [("1", t("P is multiplied by r and by t.", "La P está multiplicada por r y por t."), t("Divide by the product rt.", "Se divide entre el producto rt.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>P = {fx('I', 'rt')}</strong>")])}
{practica("p1", t("Practice 1 — Distance", "Práctica 1 — Distancia"), t("In d = rt, solve for r.", "En d = rt, despeje r."), [("a", "r = dt"), ("b", f"r = {fx('t', 'd')}"), ("c", f"r = {fx('d', 't')}")])}
{practica("p2", t("Practice 2 — Area", "Práctica 2 — Área"), t("In A = lw, solve for l.", "En A = lw, despeje l."), [("a", "l = Aw"), ("b", f"l = {fx('A', 'w')}"), ("c", f"l = {fx('w', 'A')}")])}
{practica("p3", t("Practice 3 — A sum", "Práctica 3 — Una suma"), t("In P = a + b + c, solve for c.", "En P = a + b + c, despeje c."), [("a", "c = P − a − b"), ("b", "c = P + a + b"), ("c", f"c = {fx('P', 'ab')}")])}
{enlace(n, t("common", "comunes"), t("common formulas", "fórmulas comunes"), t("Solve for variables in geometry, money, and science formulas.", "Despeje variables en fórmulas de geometría, finanzas y física."))}'''

    s4 = f'''<p>{t("Some formulas need more than one operation to solve, just like multi-step equations. Undo the operations in reverse order.", "Algunas fórmulas requieren más de una operación para despejar, igual que las ecuaciones de varios pasos. Se deshacen las operaciones en orden inverso.")}</p>
{ejemplo(t("Example 4: temperature. In F = (9/5)C + 32, solve for C", "Ejemplo 4: temperatura. En F = (9/5)C + 32, despeje C"),
  [("1", t("Subtract 32 from both sides.", "Restar 32 en ambos lados."), f"F − 32 = {fx(9, 5)}C."),
   ("2", t("Multiply both sides by 5/9.", "Multiplicar por 5/9 en ambos lados."), t(f"That undoes the {fx(9, 5)}: {fx(5, 9)}(F − 32) = C.", f"Eso deshace el {fx(9, 5)}: {fx(5, 9)}(F − 32) = C.")),
   ("✓", t("Answer.", "Respuesta."), f"<strong>C = {fx(5, 9)}(F − 32)</strong>")])}
{ejemplo(t("Example 5: a line. In y = mx + b, solve for b", "Ejemplo 5: recta. En y = mx + b, despeje b"),
  [("1", t("Subtract mx from both sides.", "Restar mx en ambos lados."), "y − mx = b."),
   ("✓", t("Answer.", "Respuesta."), "<strong>b = y − mx</strong>")])}
{caja("ojo", t("Reverse order, and the parentheses matter", "Orden inverso, y el paréntesis importa"), t(f"<p>In F = (9/5)C + 32, first remove the “+ 32” (subtract), then the “× 9/5” (multiply by the reciprocal). It is the same reverse order as two-step equations. And {fx(5, 9)}(F − 32) is not the same as {fx(5, 9)}F − 32: first subtract 32 from the whole F, then multiply the whole result.</p>", f"<p>En F = (9/5)C + 32, primero se quita el «+ 32» (resta) y luego el «× 9/5» (multiplicación por el recíproco). Es el mismo orden inverso de las ecuaciones de dos pasos. Y {fx(5, 9)}(F − 32) no es lo mismo que {fx(5, 9)}F − 32: primero se resta 32 a toda la F y después se multiplica el resultado completo.</p>"))}
{enlace(n, t("two-step", "dos-pasos"), t("two-step formulas", "fórmulas de dos pasos"), t("Solve formulas that require undoing two operations.", "Despeje en fórmulas que requieren deshacer dos operaciones."))}'''

    s5 = f'''<p>{t("Once it is solved, the formula lets you work out the variable you want by substituting the known values.", "Una vez despejada, la fórmula sirve para calcular la variable buscada sustituyendo los valores conocidos.")}</p>
{ejemplo(t("Example 6: a car traveled d = 120 miles at a rate of r = 40 miles per hour. How long did it take?", "Ejemplo 6: un auto recorrió d = 120 millas a una rapidez de r = 40 millas por hora. ¿Cuánto tiempo tardó?"),
  [("1", t("Use the solved formula.", "Usar la fórmula despejada."), f"t = {fx('d', 'r')}."),
   ("2", t("Substitute.", "Sustituir."), f"t = {fx(120, 40)} = 3."),
   ("✓", t("Answer.", "Respuesta."), t("The car took <strong>3 hours</strong>.", "El auto tardó <strong>3 horas</strong>."))])}
{caja("tip", t("A link to science", "Conexión con las ciencias"), t("<p>The same idea works with F = ma (force = mass × acceleration). To find the acceleration a, solve for a = F/m. Solving formulas is a general tool that appears in geometry, money, and science.</p>", "<p>La misma idea aplica a F = ma (fuerza = masa × aceleración). Para hallar la aceleración a, se despeja a = F/m. Despejar es una herramienta general que aparece en geometría, finanzas y ciencias.</p>"))}
{enlace(n, t("apply", "aplicar"), t("using the solved formula", "aplicar la fórmula despejada"), t("Use the solved formula to solve a problem.", "Use la fórmula ya despejada para resolver un problema."))}'''

    secciones = [("s-" + t("what-is", "que-es"), t("What does it mean to solve a formula?", "¿Qué es despejar una fórmula?"), s1),
                 ("s-" + t("four-steps", "cuatro-pasos"), t("The four-step strategy", "La estrategia de cuatro pasos"), s2),
                 ("s-" + t("common", "comunes"), t("Solving common formulas", "Despejar en fórmulas comunes"), s3),
                 ("s-" + t("two-step", "dos-pasos"), t("Two-step formulas", "Fórmulas de dos pasos"), s4),
                 ("s-" + t("apply", "aplicar"), t("Using the solved formula", "Aplicar la fórmula despejada"), s5)]

    lesson = {"next": t("Lesson 6.1", "Lección 6.1"), "review": t("sections 3 to 5", "las secciones 3 a 5"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("r is multiplied by t: divide; do not multiply.", "La r está multiplicada por t: se divide, no se multiplica."), "b": t("The fraction is upside down: d goes on top.", "La fracción quedó al revés: la d va arriba.")}, "right": t("Divide both sides by t.", "Se divide entre t en ambos lados."), "solution": "r = d/t."},
      "p2": {"ok": "b", "hints": {"a": t("l is multiplied by w: divide; do not multiply.", "La l está multiplicada por w: se divide, no se multiplica."), "c": t("The fraction is upside down: A goes on top.", "La fracción quedó al revés: la A va arriba.")}, "right": t("Divide both sides by w.", "Se divide entre w en ambos lados."), "solution": "l = A/w."},
      "p3": {"ok": "a", "hints": {"b": t("a and b are added to c: subtract them.", "A la c se le suman a y b: se restan."), "c": t("It is a sum, not a product.", "Es una suma, no un producto.")}, "right": t("Subtract a and b from both sides.", "Se restan a y b en ambos lados."), "solution": "c = P − a − b."}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("t is multiplied: divide.", "La t está multiplicada: se divide."), "c": t("The fraction is upside down.", "La fracción está al revés."), "d": t("It is a product, not a sum.", "Es un producto, no una suma.")}, "solution": "t = d/r."},
      "B": {"ok": "d", "hints": {"a": t("Divide by rt; do not multiply.", "Se divide entre rt, no se multiplica."), "b": t("The fraction is upside down.", "La fracción está al revés."), "c": t("It is a product, not a sum.", "Es un producto, no una suma.")}, "solution": "P = I/(rt)."},
      "C": {"ok": "c", "hints": {"a": t("w is also multiplied by 2.", "La w también está multiplicada por 2."), "b": t("Subtract 2l from P, not from 2P.", "Se resta 2l a P, no a 2P."), "d": t("Subtract 2l; do not add it.", "Se resta 2l, no se suma.")}, "solution": "2w = P − 2l, w = (P − 2l)/2."},
      "D": {"ok": "b", "hints": {"a": t("b is added: subtract mx.", "La b está sumada: se resta mx."), "c": t("Order: y − mx.", "El orden es y − mx."), "d": t("b is added, not multiplied.", "La b está sumada, no multiplicada.")}, "solution": "b = y − mx."},
      "E": {"ok": "d", "hints": {"a": t("Divide by lw.", "Se divide entre lw."), "b": t("The fraction is upside down.", "La fracción está al revés."), "c": t("It is a product, not a sum.", "Es un producto, no una suma.")}, "solution": "h = V/(lw)."},
      "F": {"ok": "c", "hints": {"a": t("That is 120 − 40.", "Eso es 120 − 40."), "b": t("That is 120 + 40.", "Eso es 120 + 40."), "d": t("That is 120 × 40.", "Eso es 120 × 40.")}, "solution": "t = 120/40 = 3."},
      "G": {"ok": "d", "hints": {"a": t("rt = 0.05 · 2 = 0.1.", "rt = 0.05 · 2 = 0.1."), "b": t("100 is the interest, not P.", "100 es el interés, no P."), "c": t("Divide 100 by 0.1, not by 0.2.", "Divida 100 entre 0.1, no entre 0.2.")}, "solution": "P = 100/(0.05 · 2) = 1000."},
      "H": {"ok": "b", "hints": {"a": t("212 − 32 = 180, then multiply by 5/9.", "212 − 32 = 180 y después se multiplica por 5/9."), "c": t("Subtract 32 first, then multiply by 5/9.", "Primero se resta 32 y después se multiplica por 5/9."), "d": t("Substitute F = 212 into the formula.", "Sustituya F = 212 en la fórmula.")}, "solution": "(212 − 32) · 5/9 = 180 · 5/9 = 100."}
     }}

    quiz = [
     ("A", t("In d = rt, solve for t.", "En d = rt, despeje t."), [("a", "t = dr"), ("b", f"t = {fx('d', 'r')}"), ("c", f"t = {fx('r', 'd')}"), ("d", "t = d − r")]),
     ("B", t("In I = Prt, solve for P.", "En I = Prt, despeje P."), [("a", "P = Irt"), ("b", f"P = {fx('rt', 'I')}"), ("c", "P = I − rt"), ("d", f"P = {fx('I', 'rt')}")]),
     ("C", t("In P = 2l + 2w, solve for w.", "En P = 2l + 2w, despeje w."), [("a", "w = P − 2l"), ("b", "w = 2P − 2l"), ("c", f"w = {fx('P − 2l', 2)}"), ("d", f"w = {fx('P + 2l', 2)}")]),
     ("D", t("In y = mx + b, solve for b.", "En y = mx + b, despeje b."), [("a", "b = y + mx"), ("b", "b = y − mx"), ("c", "b = mx − y"), ("d", f"b = {fx('y', 'mx')}")]),
     ("E", t("In V = lwh, solve for h.", "En V = lwh, despeje h."), [("a", "h = Vlw"), ("b", f"h = {fx('lw', 'V')}"), ("c", "h = V − lw"), ("d", f"h = {fx('V', 'lw')}")]),
     ("F", t("In d = rt, if d = 120 and r = 40, find t.", "En d = rt, si d = 120 y r = 40, halle t."), [("a", "t = 80"), ("b", "t = 160"), ("c", "t = 3"), ("d", "t = 4800")]),
     ("G", t("In I = Prt, if I = 100, r = 0.05, and t = 2, find P.", "En I = Prt, si I = 100, r = 0.05 y t = 2, halle P."), [("a", "P = 10"), ("b", "P = 100"), ("c", "P = 500"), ("d", "P = 1000")]),
     ("H", t("In C = (F − 32) · 5/9, if F = 212, find C.", "En C = (F − 32) · 5/9, si F = 212, halle C."), [("a", "C = 180"), ("b", "C = 100"), ("c", "C = 32"), ("d", "C = 212")])]

    return B.pagina_leccion(n, 5, t(*TEMA), t(*TIT),
        t("Solve a formula for any of its letters, treating the other letters as numbers, and use it to solve problems.", "Despeje una fórmula para cualquiera de sus letras, tratando las demás como números, y úsela para resolver problemas."),
        ("🧮", t("Calculator to apply formulas", "Calculadora para aplicar fórmulas")),
        [t("<strong>Solve</strong> a literal formula for a specific variable with the properties of equality.", "<strong>Despejar</strong> una variable específica en una fórmula literal usando las propiedades de igualdad."),
         t("<strong>Treat</strong> the other letters of the formula as if they were constants.", "<strong>Tratar</strong> las demás letras de la fórmula como si fueran constantes."),
         t("<strong>Use</strong> a general four-step strategy to solve for a variable.", "<strong>Aplicar</strong> una estrategia general de cuatro pasos para despejar."),
         t("<strong>Use</strong> the solved formula to solve a problem in context.", "<strong>Usar</strong> la fórmula despejada para resolver un problema de contexto."),
         t("<strong>Recognize</strong> the formulas that are used often on the GED test.", "<strong>Reconocer</strong> las fórmulas de uso frecuente en el GED.")],
        secciones,
        (t("Solve a given formula for a variable six times, and use a solved formula four times in a problem with numbers. Write each answer with its units.",
           "Despeje una variable en una fórmula dada en seis ejercicios, y aplique una fórmula despejada en cuatro problemas de contexto con valores numéricos. Escriba cada respuesta con sus unidades."),
         t("Plan a trip: choose a city you would like to drive to, look up the distance in miles, and decide on an average speed. Solve d = rt for t and find how many hours the trip would take. Then check the weather forecast there in °F and convert it to °C with C = (5/9)(F − 32).",
           "Planifique un viaje: elija una ciudad a la que le gustaría ir en auto, busque la distancia en millas y decida una rapidez promedio. Despeje t en d = rt y halle cuántas horas tomaría el viaje. Después busque el pronóstico del tiempo allí en °F y conviértalo a °C con C = (5/9)(F − 32).")),
        quiz,
        t("Self-check checklist for solving formulas", "Lista de autoevaluación para despejar fórmulas"),
        t("Self-check checklist: skills for solving literal formulas and using them", "Lista de autoevaluación: destrezas para despejar fórmulas literales y aplicarlas"),
        [(t("Isolating the variable", "Aislar la variable buscada"), t("I isolate the variable, treating the other letters as constants.", "Aíslo la variable buscada tratando las demás letras como constantes."), t("I isolate it with some mistakes.", "La aíslo con errores ocasionales."), t("I do not use the properties of equality to solve for it.", "No aplico las propiedades de igualdad para despejar.")),
         (t("Simplifying the result", "Simplificar el resultado"), t("I write the result in its clearest form, with a fraction if needed.", "Presento el resultado en su forma más clara, con fracción si hace falta."), t("I simplify with a mistake in the fraction.", "Simplifico con algún error en la fracción."), t("I leave the result unfinished or written wrong.", "Dejo el despeje incompleto o mal escrito.")),
         (t("Using the solved formula", "Aplicar la fórmula despejada"), t("I use the solved formula, get the right value, and give it with units.", "Aplico la fórmula despejada, obtengo el valor correcto y lo doy con unidades."), t("I substitute the values with mistakes.", "Sustituyo los valores con errores."), t("I do not use the solved formula to calculate.", "No uso la fórmula despejada para calcular."))],
        t("<p>This lesson closes Topic 5. You can now solve inequalities of every kind and solve literal formulas: identify the variable you want, isolate it by treating the other letters as numbers, simplify, and use the solved formula in real problems. With that, the linear algebra of Level 3 is complete.</p>\n<p>Topic 6 turns to geometry. It opens with <strong>Lesson 6.1 · Angles: relationships and parallel lines cut by a transversal</strong>. The algebra you just mastered will be a constant tool: many geometry problems are solved by writing and solving an equation, exactly what you learned in these two topics.</p>",
          "<p>Con esta lección se cierra el Tema 5. Ya se resuelven inecuaciones de todo tipo y se despejan fórmulas literales: identificar la variable buscada, aislarla tratando las demás letras como números, simplificar y aplicar la fórmula despejada en problemas reales. Con ello queda completa el álgebra lineal del Nivel 3.</p>\n<p>El Tema 6 dará un giro hacia la geometría. Abrirá con la <strong>Lección 6.1 · Ángulos: relaciones y líneas paralelas cortadas por una transversal</strong>. El álgebra recién dominada será una herramienta constante: muchos problemas de geometría se resuelven planteando y resolviendo una ecuación, justo lo aprendido en estos dos temas.</p>"),
        ("6-1", ("", t("Lesson 6.1 · Angles: relationships and parallel lines cut by a transversal", "Lección 6.1 · Ángulos: relaciones y líneas paralelas cortadas por una transversal"))),
        [(t("literal formula", "fórmula literal"), t("A formula that relates several amounts with letters, like d = rt.", "Una fórmula que relaciona varias cantidades con letras, como d = rt.")),
         (t("solve for", "despejar"), t("To rewrite a formula so that one variable is alone on one side.", "Reescribir una fórmula para que una variable quede sola de un lado.")),
         (t("reciprocal", "recíproco"), t("The fraction turned upside down: the reciprocal of 9/5 is 5/9. Multiplying by it undoes the 9/5.", "La fracción dada vuelta: el recíproco de 9/5 es 5/9. Multiplicar por él deshace el 9/5.")),
         (t("simple interest", "interés simple"), t("I = Prt: the principal P times the rate r times the time t in years.", "I = Prt: el capital P por la tasa r por el tiempo t en años."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function Q(a, b){ return '<span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + "</span></span>"; }
var R59 = Q(5, 9), R95 = Q(9, 5), MEDIO = Q(1, 2);
function divide(x, y){ return T(x + " is multiplied by " + y + ": divide both sides by " + y + ".", "La " + x + " está multiplicada por " + y + ": se divide entre " + y + " en ambos lados."); }
function dividePor(x, y, prod){ return T(x + " is multiplied by " + y + ": divide by the product " + prod + ".", "La " + x + " está multiplicada por " + y + ": se divide entre el producto " + prod + "."); }

/* ============ One-operation formulas ============ */
var UNA = [
  {f: "d = rt", v: "t", res: "t = " + Q("d", "r"), op: divide("t", "r"),
   num: ["120 = 40t", T("divide by 40", "se divide entre 40"), "t = " + Q(120, 40) + " = 3"], mal: ["t = dr", "t = " + Q("r", "d"), "t = d − r"], hallar: T("the time t, when you know the distance and the rate", "el tiempo t, conocidas la distancia y la rapidez")},
  {f: "d = rt", v: "r", res: "r = " + Q("d", "t"), op: divide("r", "t"),
   num: ["150 = 3r", T("divide by 3", "se divide entre 3"), "r = " + Q(150, 3) + " = 50"], mal: ["r = dt", "r = " + Q("t", "d"), "r = d − t"], hallar: T("the rate r, when you know the distance and the time", "la rapidez r, conocidos la distancia y el tiempo")},
  {f: "A = bh", v: "h", res: "h = " + Q("A", "b"), op: divide("h", "b"),
   num: ["24 = 6h", T("divide by 6", "se divide entre 6"), "h = " + Q(24, 6) + " = 4"], mal: ["h = Ab", "h = " + Q("b", "A"), "h = A − b"], hallar: T("the height h of a rectangle, when you know the area and the base", "la altura h de un rectángulo, conocidos el área y la base")},
  {f: "V = lwh", v: "h", res: "h = " + Q("V", "lw"), op: dividePor("h", T("l and by w", "l y por w"), "lw"),
   num: ["60 = 5 · 3 · h", T("divide by 15", "se divide entre 15"), "h = " + Q(60, 15) + " = 4"], mal: ["h = Vlw", "h = " + Q("lw", "V"), "h = " + Q("V", "l") + " − w"], hallar: T("the height h of a box, when you know the volume, the length, and the width", "la altura h de una caja, conocidos el volumen, el largo y el ancho")},
  {f: "I = Prt", v: "P", res: "P = " + Q("I", "rt"), op: dividePor("P", T("r and by t", "r y por t"), "rt"),
   num: ["90 = P · 0.05 · 3", T("divide by 0.15", "se divide entre 0.15"), "P = " + Q(90, "0.15") + " = 600"], mal: ["P = Irt", "P = " + Q("rt", "I"), "P = I − rt"], hallar: T("the principal P, when you know the interest, the rate, and the time", "el capital P, conocidos el interés, la tasa y el tiempo")},
  {f: "I = Prt", v: "r", res: "r = " + Q("I", "Pt"), op: dividePor("r", T("P and by t", "P y por t"), "Pt"),
   num: ["90 = 600 · r · 3", T("divide by 1800", "se divide entre 1800"), "r = " + Q(90, 1800) + " = 0.05"], mal: ["r = IPt", "r = " + Q("Pt", "I"), "r = " + Q("I", "P") + " − t"], hallar: T("the interest rate r, when you know the interest, the principal, and the time", "la tasa de interés r, conocidos el interés, el capital y el tiempo")},
  {f: "I = Prt", v: "t", res: "t = " + Q("I", "Pr"), op: dividePor("t", T("P and by r", "P y por r"), "Pr"),
   num: ["90 = 600 · 0.05 · t", T("divide by 30", "se divide entre 30"), "t = " + Q(90, 30) + " = 3"], mal: ["t = IPr", "t = " + Q("Pr", "I"), "t = I − Pr"], hallar: T("the time t of an investment, when you know the interest, the principal, and the rate", "el tiempo t de una inversión, conocidos el interés, el capital y la tasa")},
  {f: "P = a + b + c", v: "c", res: "c = P − a − b", op: T("a and b are added to c: subtract a and b from both sides.", "A la c se le suman a y b: se restan a y b en ambos lados."),
   num: ["20 = 6 + 5 + c", T("subtract 6 and 5", "se restan 6 y 5"), "c = 20 − 6 − 5 = 9"], mal: ["c = P + a + b", "c = " + Q("P", "ab"), "c = P − a + b"], hallar: T("the third side c of a triangle, when you know the perimeter and the other two sides", "el tercer lado c de un triángulo, conocidos el perímetro y los otros dos lados")},
  {f: "F = ma", v: "a", res: "a = " + Q("F", "m"), op: divide("a", "m"),
   num: ["50 = 10a", T("divide by 10", "se divide entre 10"), "a = " + Q(50, 10) + " = 5"], mal: ["a = Fm", "a = " + Q("m", "F"), "a = F − m"], hallar: T("the acceleration a, when you know the force and the mass", "la aceleración a, conocidas la fuerza y la masa")}
];
function etiqueta(d){ return T("In " + d.f + ", solve for " + d.v, "En " + d.f + ", despejar " + d.v); }

/* MODULE 1 · numbers and letters side by side */
var PL = {visto: 0, total: 4};
function llenaPL(){ var sel = $("pl-sel"); UNA.forEach(function(d, i){ var o = document.createElement("option"); o.value = i; o.textContent = etiqueta(d); sel.appendChild(o); }); }
function pintaPL(){
  var d = UNA[+$("pl-sel").value], filas = [
    [T("Identify", "Identificar"), T("You want " + d.v + " alone in ", "Se quiere dejar sola la " + d.v + " en ") + auto(d.num[0]) + ".", T("You want " + d.v + " alone in ", "Se quiere dejar sola la " + d.v + " en ") + auto(d.f) + "."],
    [T("Isolate", "Aislar"), T("Inverse operation: ", "Operación inversa: ") + d.num[1] + T(" on both sides.", " en ambos lados."), d.op],
    [T("Simplify", "Simplificar"), auto(d.num[2]) + ".", auto(d.res) + "."],
    [T("Check", "Verificar"), T(d.v + " is alone, and the other side has only numbers.", "La " + d.v + " quedó sola y del otro lado solo hay números."), T(d.v + " is alone, and no " + d.v + " appears on the other side.", "La " + d.v + " quedó sola y del otro lado no aparece ninguna " + d.v + ".")]
  ], h = "";
  for (var i = 0; i < PL.visto; i++){
    h += "<p><strong>" + T("Step ", "Paso ") + (i + 1) + " · " + filas[i][0] + '</strong></p><div class="lado-a-lado"><div><p class="nota">' + T("With numbers", "Con números") + "</p>" + filas[i][1] +
         '</div><div><p class="nota">' + T("With letters", "Con letras") + "</p>" + filas[i][2] + "</div></div>";
  }
  $("pl-pasos").innerHTML = h;
  var b = $("pl-sig"); b.disabled = PL.visto >= PL.total; $("pl-todo").disabled = b.disabled;
  b.textContent = PL.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function pistasMal(d){
  var izq = d.f.split(" = ")[0], suma = d.f.indexOf("+") >= 0;
  return {m0: suma ? T("To undo an addition, subtract.", "Para deshacer una suma, se resta.") : T("If the letter is multiplied, you divide; you do not multiply.", "Si la letra está multiplicada, se divide; no se multiplica."),
          m1: suma ? T("It is a sum, not a product.", "Es una suma, no un producto.") : T("The fraction is upside down: " + izq + ", which was alone, goes on top.", "La fracción quedó al revés: lo que estaba solo (" + izq + ") va arriba."),
          m2: suma ? T("Check the signs: subtract both a and b.", "Revise los signos: se restan a y b.") : T("The letters are multiplied, not added: you divide.", "Las letras están multiplicadas, no sumadas: se divide.")};
}
function genDespejar(){
  var d = elige(UNA), o = [{html: auto(d.res), clave: "b"}].concat(d.mal.map(function(m, i){ return {html: auto(m), clave: "m" + i}; }));
  return {enun: T("In ", "En ") + auto(d.f) + T(", solve for ", ", despeje ") + d.v + ".", opciones: o, correcta: "b", porClave: pistasMal(d), bien: d.op, mal: d.op + T(" You get ", " Queda ") + auto(d.res) + "."};
}
function genNecesitas(){
  var d = elige(UNA), otras = baraja(UNA.filter(function(x){ return x !== d && x.res !== d.res; })).slice(0, 2);
  var o = [{html: auto(d.res), clave: "b"}, {html: auto(d.mal[1]), clave: "inv"}].concat(otras.map(function(x, i){ return {html: auto(x.res), clave: "o" + i}; }));
  var pc = {inv: T("The fraction is upside down.", "La fracción está al revés."), o0: T("That formula finds a different amount.", "Esa fórmula halla otra cantidad."), o1: T("That formula finds a different amount.", "Esa fórmula halla otra cantidad.")};
  return {enun: T("Which solved formula finds " + d.hallar + "? (The original formula is ", "¿Qué fórmula despejada sirve para hallar " + d.hallar + "? (La fórmula original es ") + auto(d.f) + ".)", opciones: o, correcta: "b", porClave: pc,
    bien: T("Solve " + auto(d.f) + " for " + d.v + ": ", "Se despeja " + d.v + " en " + auto(d.f) + ": ") + auto(d.res) + ".", mal: T("Solve " + auto(d.f) + " for " + d.v + ": ", "Se despeja " + d.v + " en " + auto(d.f) + ": ") + auto(d.res) + "."};
}

/* ============ MODULE 3 · two-step formulas ============ */
var DOS = [
  {f: "F = " + R95 + "C + 32", v: "C", res: "C = " + R59 + "(F − 32)",
   pasos: [T("First remove what is added: subtract 32 from both sides. You get ", "Se quita primero lo que está sumado: se resta 32 en ambos lados. Queda ") + auto("F − 32 = " + R95 + "C") + ".",
           T("To undo the multiplication by " + R95 + ", multiply both sides by its reciprocal, " + R59 + ". You get ", "Para deshacer la multiplicación por " + R95 + " se multiplica por su recíproco, " + R59 + ", en ambos lados. Queda ") + auto(R59 + "(F − 32) = C") + "."],
   mal: ["C = " + R59 + "F − 32", "C = " + R95 + "(F − 32)", "C = " + R59 + "(F + 32)"],
   pc: [T("Order matters: subtract 32 from the whole F first, then multiply everything by 5/9.", "El orden importa: primero se resta 32 a toda la F y después se multiplica todo por 5/9."), T("Multiply by the reciprocal, 5/9, not by 9/5 again.", "Se multiplica por el recíproco, 5/9, no otra vez por 9/5."), T("To undo + 32, subtract 32.", "Para deshacer + 32 se resta 32.")]},
  {f: "y = mx + b", v: "b", res: "b = y − mx",
   pasos: [T("b is added: subtract mx from both sides. You get ", "La b está sumada: se resta mx en ambos lados. Queda ") + auto("y − mx = b") + "."],
   mal: ["b = y + mx", "b = " + Q("y", "mx"), "b = mx − y"],
   pc: [T("To undo + mx, subtract mx.", "Para deshacer + mx se resta mx."), T("b is added, not multiplied.", "La b está sumada, no multiplicada."), T("The order is y − mx.", "El orden es y − mx.")]},
  {f: "y = mx + b", v: "x", res: "x = " + Q("y − b", "m"),
   pasos: [T("First remove what is added: subtract b from both sides. You get ", "Se quita primero lo que está sumado: se resta b en ambos lados. Queda ") + auto("y − b = mx") + ".",
           T("x is multiplied by m: divide both sides by m. You get ", "La x está multiplicada por m: se divide entre m en ambos lados. Queda ") + auto(Q("y − b", "m") + " = x") + "."],
   mal: ["x = " + Q("y", "m") + " − b", "x = " + Q("y + b", "m"), "x = m(y − b)"],
   pc: [T("Order matters: subtract b first, then divide the whole result by m.", "El orden importa: primero se resta b y después se divide todo entre m."), T("To undo + b, subtract b.", "Para deshacer + b se resta b."), T("x is multiplied by m: divide by m.", "La x está multiplicada por m: se divide entre m.")]},
  {f: "P = 2l + 2w", v: "l", res: "l = " + Q("P − 2w", 2),
   pasos: [T("First remove what is added: subtract 2w from both sides. You get ", "Se quita primero lo que está sumado: se resta 2w en ambos lados. Queda ") + auto("P − 2w = 2l") + ".",
           T("l is multiplied by 2: divide both sides by 2. You get ", "La l está multiplicada por 2: se divide entre 2 en ambos lados. Queda ") + auto(Q("P − 2w", 2) + " = l") + "."],
   mal: ["l = " + Q("P", 2) + " − 2w", "l = " + Q("P + 2w", 2), "l = P − w"],
   pc: [T("Order matters: subtract 2w first, then divide the whole result by 2.", "El orden importa: primero se resta 2w y después se divide todo entre 2."), T("To undo + 2w, subtract 2w.", "Para deshacer + 2w se resta 2w."), T("Divide the whole P − 2w by 2.", "Se divide todo P − 2w entre 2.")]},
  {f: "A = " + MEDIO + "bh", v: "h", res: "h = " + Q("2A", "b"),
   pasos: [T("To undo the " + MEDIO + ", multiply both sides by 2. You get ", "Para deshacer el " + MEDIO + " se multiplica por 2 en ambos lados. Queda ") + auto("2A = bh") + ".",
           T("h is multiplied by b: divide by b. You get ", "La h está multiplicada por b: se divide entre b. Queda ") + auto(Q("2A", "b") + " = h") + "."],
   mal: ["h = " + Q("A", "2b"), "h = " + Q("A", "b"), "h = 2Ab"],
   pc: [T("To undo the 1/2, multiply by 2; do not divide.", "Para deshacer el 1/2 se multiplica por 2; no se divide."), T("You forgot to undo the 1/2.", "Faltó deshacer el 1/2."), T("h is multiplied by b: divide by b.", "La h está multiplicada por b: se divide entre b.")]}
];
var DP = {pasos: [], visto: 0};
function llenaDP(){ var sel = $("dp-sel"); DOS.forEach(function(d, i){ var o = document.createElement("option"); o.value = i; o.textContent = etiqueta(d).replace(/<span class="fracc"><span class="fa">(.*?)<\/span><span class="fb2">(.*?)<\/span><\/span>/g, "($1/$2)"); sel.appendChild(o); }); }
function preparaDP(){
  var d = DOS[+$("dp-sel").value];
  DP.pasos = [T("You want " + d.v + " alone.", "Se quiere dejar sola la " + d.v + ".")].concat(d.pasos).concat(['<span class="veredicto">' + T("Answer: ", "Resultado: ") + auto(d.res) + "</span>"]); DP.visto = 0;
  $("dp-expr").innerHTML = '<span class="grande">' + auto(d.f) + "</span>";
  pintaDP();
}
function pintaDP(){
  $("dp-pasos").innerHTML = DP.pasos.slice(0, DP.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === DP.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("dp-sig"); b.disabled = DP.visto >= DP.pasos.length; $("dp-todo").disabled = b.disabled;
  b.textContent = DP.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function genDosPasos(){
  var d = elige(DOS), o = [{html: auto(d.res), clave: "b"}].concat(d.mal.map(function(m, i){ return {html: auto(m), clave: "m" + i}; })), pc = {};
  d.pc.forEach(function(p, i){ pc["m" + i] = p; });
  return {enun: T("In ", "En ") + auto(d.f) + T(", solve for ", ", despeje ") + d.v + ".", opciones: o, correcta: "b", porClave: pc, bien: d.pasos.join(" "), mal: d.pasos.join(" ")};
}

/* ============ MODULE 4 · using the formula: two paths ============ */
function problemaFormula(){
  var tp = aleatorio(1, 6);
  if (tp === 1){ var r = elige([40, 45, 50, 55, 60, 65]), tt = aleatorio(2, 6), d = r * tt;
    return {txt: T("A car traveled " + d + " miles at " + r + " miles per hour. How many hours did it take?", "Un auto recorrió " + d + " millas a " + r + " millas por hora. ¿Cuántas horas tardó?"), f: "d = rt", des: "t = " + Q("d", "r"),
      sust: d + " = " + r + "t", res: fr(tt), unidad: T("hours", "horas"), cuenta: "t = " + Q(d, r) + " = " + tt, resuelve: T("divide both sides by " + r, "se divide entre " + r + " en ambos lados")}; }
  if (tp === 2){ var Pc = elige([500, 800, 1000, 1200, 2000]), rr = elige([2, 3, 4, 5, 6]), ti = aleatorio(2, 5), I = Pc * rr * ti / 100;
    return {txt: T("An investment of $" + Pc + " earned $" + I + " in simple interest in " + ti + " years. What was the yearly interest rate? Give the answer as a decimal (for example, 0.04).", "Una inversión de $" + Pc + " produjo $" + I + " de interés simple en " + ti + " años. ¿Cuál fue la tasa de interés anual? Dé la respuesta en decimal (por ejemplo, 0.04)."), f: "I = Prt", des: "r = " + Q("I", "Pt"),
      sust: I + " = " + Pc + " · r · " + ti, res: fr(rr, 100), unidad: T("(that is, " + rr + "%)", "(es decir, " + rr + " %)"), cuenta: "r = " + Q(I, Pc * ti) + " = " + (rr / 100), resuelve: T("multiply " + Pc + " · " + ti + " = " + (Pc * ti) + " and divide both sides by " + (Pc * ti), "se multiplica " + Pc + " · " + ti + " = " + (Pc * ti) + " y se divide entre " + (Pc * ti) + " en ambos lados")}; }
  if (tp === 3){ var C = elige([-10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 100]), F = 9 * C / 5 + 32;
    return {txt: T("The thermometer reads " + F + " °F. How many degrees Celsius is that?", "El termómetro marca " + F + " °F. ¿Cuántos grados Celsius son?"), f: "F = " + R95 + "C + 32", des: "C = " + R59 + "(F − 32)",
      sust: F + " = " + R95 + "C + 32", res: fr(C), unidad: "°C", cuenta: "C = " + R59 + "(" + F + " − 32) = " + R59 + " · " + (F - 32) + " = " + C, resuelve: T("subtract 32 from both sides and multiply by ", "se resta 32 en ambos lados y se multiplica por ") + R59}; }
  if (tp === 4){ var w = aleatorio(3, 12), l = w + aleatorio(2, 10), Pp = 2 * l + 2 * w;
    return {txt: T("A rectangle has a perimeter of " + Pp + " feet and a width of " + w + " feet. How long is it?", "Un rectángulo tiene un perímetro de " + Pp + " pies y un ancho de " + w + " pies. ¿Cuánto mide el largo?"), f: "P = 2l + 2w", des: "l = " + Q("P − 2w", 2),
      sust: Pp + " = 2l + " + (2 * w), res: fr(l), unidad: T("feet", "pies"), cuenta: "l = " + Q(Pp + " − " + (2 * w), 2) + " = " + Q(Pp - 2 * w, 2) + " = " + l, resuelve: T("subtract " + (2 * w) + " from both sides and divide by 2", "se resta " + (2 * w) + " en ambos lados y se divide entre 2")}; }
  if (tp === 5){ var lv = aleatorio(3, 10), wv = aleatorio(2, 8), hv = aleatorio(2, 9), V = lv * wv * hv;
    return {txt: T("A box has a volume of " + V + " cubic inches, a length of " + lv + " inches, and a width of " + wv + " inches. How tall is it?", "Una caja tiene un volumen de " + V + " pulgadas cúbicas, un largo de " + lv + " pulgadas y un ancho de " + wv + " pulgadas. ¿Cuánto mide la altura?"), f: "V = lwh", des: "h = " + Q("V", "lw"),
      sust: V + " = " + lv + " · " + wv + " · h", res: fr(hv), unidad: T("inches", "pulgadas"), cuenta: "h = " + Q(V, lv * wv) + " = " + hv, resuelve: T("multiply " + lv + " · " + wv + " = " + (lv * wv) + " and divide both sides by " + (lv * wv), "se multiplica " + lv + " · " + wv + " = " + (lv * wv) + " y se divide entre " + (lv * wv) + " en ambos lados")}; }
  var m = elige([2, 3, 4, 5, -2]), b = nz(), x = aleatorio(-4, 8), y = m * x + b;
  return {txt: T("On the line y = " + P(tm(m, "x"), tm(b)).replace(/<[^>]+>/g, "") + ", what is x when y = " + menosV(y) + "?", "En la recta y = " + P(tm(m, "x"), tm(b)).replace(/<[^>]+>/g, "") + ", ¿cuánto vale x cuando y = " + menosV(y) + "?"), f: "y = mx + b", des: "x = " + Q("y − b", "m"),
    sust: menosV(y) + " = " + P(tm(m, "x"), tm(b)), res: fr(x), unidad: "", cuenta: "x = " + Q("(" + menosV(y) + ") − (" + menosV(b) + ")", menosV(m)) + " = " + Q(menosV(y - b), menosV(m)) + " = " + menosV(x), resuelve: (b > 0 ? T("subtract " + b, "se resta " + b) : T("add " + (-b), "se suma " + (-b))) + T(" on both sides and divide by ", " en ambos lados y se divide entre ") + menosV(m)};
}
function nuevoCA(){
  var q = problemaFormula();
  $("ca-enun").textContent = q.txt;
  $("ca-caminos").innerHTML =
    "<div><p><strong>" + T("Solve first", "Despejar primero") + "</strong></p><p>" + T("Formula: ", "Fórmula: ") + auto(q.f) + ".</p><p>" + T("Solve: ", "Se despeja: ") + auto(q.des) + ".</p><p>" + T("Substitute: ", "Se sustituye: ") + auto(q.cuenta) + ".</p></div>" +
    "<div><p><strong>" + T("Substitute first", "Sustituir primero") + "</strong></p><p>" + T("Formula: ", "Fórmula: ") + auto(q.f) + ".</p><p>" + T("Substitute: ", "Se sustituye: ") + auto(q.sust) + ".</p><p>" + T("Solve the equation: ", "Se resuelve la ecuación: ") + auto(q.resuelve) + T(". The result is ", ". El resultado es ") + numHTML(q.res, "dec") + ".</p></div>";
}
function genAplicar(){
  var q = problemaFormula();
  return {enun: q.txt, solucion: T("With ", "Con ") + auto(q.des) + ": " + auto(q.cuenta) + " " + q.unidad + ".", evalua: function(tx){ return evaluaNumero(tx, q.res, []); }};
}

/* ============ Start ============ */
llenaPL();
$("pl-sel").addEventListener("change", function(){ PL.visto = 0; pintaPL(); });
$("pl-sig").addEventListener("click", function(){ if (PL.visto < PL.total){ PL.visto++; pintaPL(); } });
$("pl-todo").addEventListener("click", function(){ PL.visto = PL.total; pintaPL(); });
pintaPL();
OMR("p1", genDespejar);
OMR("p2", genNecesitas);
llenaDP();
$("dp-sel").addEventListener("change", preparaDP);
$("dp-sig").addEventListener("click", function(){ if (DP.visto < DP.pasos.length){ DP.visto++; pintaDP(); } });
$("dp-todo").addEventListener("click", function(){ DP.visto = DP.pasos.length; pintaDP(); });
preparaDP();
OMR("p3", genDosPasos);
$("ca-nuevo").addEventListener("click", nuevoCA);
nuevoCA();
creaPracticaLibre("p4", genAplicar);
'''

ESTILO = n3.ESTILO_RAD + "\n  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}\n  .estado .grande{font-size:1.8rem;font-weight:700;color:var(--acento);}"

def practica_pagina():
    n = N
    P = n3
    pasos4 = [t("Identify the variable you want to solve for.", "Identificar qué variable se quiere despejar."),
              t("Isolate it with inverse operations, treating the other letters as numbers.", "Aislarla con operaciones inversas, tratando las demás letras como números."),
              t("Simplify the result, with a fraction if needed.", "Simplificar el resultado, con fracción si hace falta."),
              t("Check that the variable you want is alone on one side.", "Verificar que la variable buscada quedó sola de un lado.")]
    lista4 = "\n".join(f'        <div class="paso"><span class="n" aria-hidden="true">{i + 1}</span>{p}</div>' for i, p in enumerate(pasos4))
    filas = [(t("Distance", "Distancia"), "d = rt", t("d: distance, r: rate (speed), t: time", "d: distancia, r: rapidez, t: tiempo")),
             (t("Area of a rectangle", "Área de un rectángulo"), "A = bh", t("b: base, h: height", "b: base, h: altura")),
             (t("Volume of a box", "Volumen de una caja"), "V = lwh", t("l: length, w: width, h: height", "l: largo, w: ancho, h: altura")),
             (t("Simple interest", "Interés simple"), "I = Prt", t("P: principal, r: rate, t: time in years", "P: capital, r: tasa, t: tiempo en años")),
             (t("Perimeter of a triangle", "Perímetro de un triángulo"), "P = a + b + c", t("a, b, c: the three sides", "a, b, c: los tres lados")),
             (t("Force", "Fuerza"), "F = ma", t("m: mass, a: acceleration", "m: masa, a: aceleración"))]
    tabla_f = "\n".join(f"          <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in filas)
    mods = [
     (t("solve-for", "despejar"), t("The four-step strategy", "La estrategia de cuatro pasos"),
      f'''      <p>{t("To <strong>solve for</strong> a variable is to rewrite the formula so that this letter is alone on one side. The key: treat the other letters <strong>as if they were numbers</strong>. That is why solving a formula is the same as solving an equation you already know how to solve.", "<strong>Despejar</strong> una variable es reescribir la fórmula para que esa letra quede sola de un lado. La clave: las demás letras se tratan <strong>como si fueran números</strong>. Por eso despejar una fórmula es lo mismo que resolver una ecuación que ya sabe resolver.")}</p>
      <div class="pasos">
{lista4}
      </div>
      <h3>{t("Numbers and letters, side by side", "Con números y con letras, en paralelo")}</h3>
      <p>{t("On the left, an equation with numbers; on the right, the formula. The steps are the same.", "A la izquierda, una ecuación con números; a la derecha, la fórmula. Los pasos son los mismos.")}</p>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:240px;"><label for="pl-sel">{t("Formula and variable", "Fórmula y variable")}</label><select id="pl-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="pl-sig"></button><button type="button" class="btn-sec" id="pl-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button></div>
      </div>
      <div id="pl-pasos" aria-live="polite"></div>
{B.om("p1", t("Practice: solve for the variable", "Practique: despeje la variable"))}'''),
     (t("common", "comunes"), t("Common formulas", "Fórmulas comunes"),
      f'''      <p>{t("These formulas come up often on the test. In each one you can solve for any of its letters.", "Estas fórmulas aparecen mucho en el examen. En cada una se puede despejar cualquiera de sus letras.")}</p>
      <table class="reglas">
        <caption>{t("Formulas used often", "Fórmulas de uso frecuente")}</caption>
        <thead><tr><th scope="col">{t("Situation", "Contexto")}</th><th scope="col">{t("Formula", "Fórmula")}</th><th scope="col">{t("What the letters mean", "Significado de las letras")}</th></tr></thead>
        <tbody>
{tabla_f}
        </tbody>
      </table>
      <div class="caja-tip"><strong>{t("If the letter is multiplied", "Si la letra está multiplicada")}</strong> {t("by others, divide by all of them: in I = Prt, P = I/(rt).", "por otras, se divide entre todas ellas: en I = Prt, P = I/(rt).")} <strong>{t("If it is added,", "Si está sumada,")}</strong> {t("subtract the others: in P = a + b + c, c = P − a − b.", "se restan las demás: en P = a + b + c, c = P − a − b.")}</div>
{B.om("p2", t("Practice: which formula do you need?", "Practique: ¿qué fórmula necesita?"))}'''),
     (t("two-step", "dos-pasos"), t("Two-step formulas", "Fórmulas de dos pasos"),
      f'''      <p>{t("Some formulas need more than one operation. Undo them in <strong>reverse order</strong>, just like two-step equations: first remove what is added or subtracted, and last what multiplies.", "Algunas fórmulas necesitan más de una operación. Se deshacen en <strong>orden inverso</strong>, igual que las ecuaciones de dos pasos: primero se quita lo que está sumado o restado, y al final lo que multiplica.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:240px;"><label for="dp-sel">{t("Formula and variable", "Fórmula y variable")}</label><select id="dp-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="dp-sig"></button><button type="button" class="btn-sec" id="dp-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button></div>
      </div>
      <div class="fraccion-grande" id="dp-expr"></div>
      <div class="pasos" id="dp-pasos" aria-live="polite"></div>
{P.atencion(t("The parentheses matter:", "El paréntesis importa:"), t("C = (5/9)(F − 32) is not the same as C = (5/9)F − 32. First subtract 32 from the whole F, then multiply the whole result.", "C = (5/9)(F − 32) no es lo mismo que C = (5/9)F − 32. Primero se resta 32 a toda la F y después se multiplica el resultado completo."))}
{B.om("p3", t("Practice: solve in two steps", "Practique: despeje en dos pasos"))}'''),
     (t("apply", "aplicar"), t("Using the solved formula", "Aplicar la fórmula despejada"),
      f'''      <p>{t("There are two ways to find a letter: <strong>solve first</strong> and substitute afterward, or <strong>substitute first</strong> and solve the equation that is left. Both give the same result. Solving first is better when you have to calculate many times, because the solved formula works for every case.", "Hay dos caminos para calcular una letra: <strong>despejar primero</strong> y sustituir después, o <strong>sustituir primero</strong> y resolver la ecuación que queda. Los dos dan el mismo resultado. Despejar primero conviene cuando hay que calcular muchas veces, porque la fórmula despejada sirve para todos los casos.")}</p>
      <h3>{t("Two paths, the same result", "Dos caminos, el mismo resultado")}</h3>
      <div class="panel">
        <p class="enun" id="ca-enun"></p>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn-sec" id="ca-nuevo">{t("Another problem", "Otro problema")}</button></div>
        <div class="lado-a-lado" id="ca-caminos" aria-live="polite"></div>
      </div>
{B.libre("p4", t("Practice: calculate with the formula", "Practique: calcule con la fórmula"), t("Result", "Resultado"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Type only the number, without units. It can be a decimal or a fraction.", "Escriba solo el número, sin unidades. Puede ser decimal o fracción.") + '</p>\n        <div class="fila-btn">', 1)}''')]
    return B.pagina_practica(n, 5, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Despeje de fórmulas literales y estrategia general de resolución")
