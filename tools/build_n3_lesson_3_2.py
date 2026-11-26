"""Level 3 · Lesson 3.2 · Adding, subtracting, and multiplying radicals — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "3-2"
TEMA = ("Radicals and the real numbers", "Radicales y números reales")
TIT = ("Adding, subtracting, and multiplying radicals", "Operaciones con radicales: suma, resta y multiplicación")

def r(k, n=None):
    """k√n, or √k when n is None."""
    if n is None:
        return f'<span class="rad">√<span class="rc">{k}</span></span>'
    return f'{k}<span class="rad">√<span class="rc">{n}</span></span>'

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 3.1 you learned to simplify radicals by taking out the largest perfect square. That step is now essential: to add or subtract radicals you look at their irrational part, and two radicals that do not look alike often turn out to be like radicals once they are simplified.",
"En la Lección 3.1 aprendió a simplificar radicales extrayendo el mayor cuadrado perfecto. Ese paso es ahora imprescindible: para sumar o restar radicales hay que mirar su parte irracional, y muchas veces dos radicales que no parecen semejantes lo son una vez simplificados.")}</p>
<p>{t(f"Radicals combine just like like terms in algebra. Just as 3x + 5x = 8x, also {r(3, 2)} + {r(5, 2)} = {r(8, 2)}: you add the coefficients and the irrational part <strong>stays the same</strong>.", f"Los radicales se combinan igual que los términos semejantes del álgebra. Así como 3x + 5x = 8x, también {r(3, 2)} + {r(5, 2)} = {r(8, 2)}: se suman los coeficientes y la parte irracional <strong>se conserva</strong>.")}</p>
{big(f'{r(3, 2)} + {r(5, 2)} = {r(8, 2)} &nbsp; ' + t("(like 3x + 5x = 8x)", "(igual que 3x + 5x = 8x)"))}
{ejemplo(t(f"Example 1: add {r(4, 5)} + {r(6, 5)}", f"Ejemplo 1: sume {r(4, 5)} + {r(6, 5)}"),
  [("1", t("Same irrational part.", "Misma parte irracional."), t(f"Both terms have {r(5)}.", f"Los dos términos tienen {r(5)}.")),
   ("2", t("Add the coefficients.", "Sumar los coeficientes."), "4 + 6 = 10."),
   ("✓", t("Answer.", "Respuesta."), f"{r(4, 5)} + {r(6, 5)} = <strong>{r(10, 5)}</strong>")])}
{ejemplo(t(f"Example 2: subtract {r(7, 3)} − {r(2, 3)}", f"Ejemplo 2: reste {r(7, 3)} − {r(2, 3)}"),
  [("1", t("Same irrational part.", "Misma parte irracional."), f"{r(3)}."),
   ("2", t("Subtract the coefficients.", "Restar los coeficientes."), "7 − 2 = 5."),
   ("✓", t("Answer.", "Respuesta."), f"{r(7, 3)} − {r(2, 3)} = <strong>{r(5, 3)}</strong>")])}
{caja("ojo", t("Different parts do not combine", "No se combinan partes distintas"), t(f"<p>{r(2)} + {r(3)} is not {r(5)}, and it is not {r(2, 5)}. They have different irrational parts, so they are not like radicals and the sum is left as it is: {r(2)} + {r(3)}.</p>", f"<p>{r(2)} + {r(3)} no es {r(5)} ni {r(2, 5)}. Como tienen distinta parte irracional, no son semejantes y la suma se deja indicada: {r(2)} + {r(3)}.</p>"))}
{enlace(n, t("like", "semejantes"), t("adding and subtracting like radicals", "sumar y restar radicales semejantes"), t("Build two terms and see whether they combine.", "Arme dos términos y observe si se combinan."))}'''

    s2 = f'''<p>{t("Sometimes two radicals do not look alike, but once you simplify them they are. So before you decide, simplify each radical.", "A veces dos radicales no parecen semejantes, pero al simplificarlos resulta que sí lo son. Por eso, antes de decidir, conviene simplificar cada radical.")}</p>
{ejemplo(t(f"Example 3: add {r(8)} + {r(2)}", f"Ejemplo 3: sume {r(8)} + {r(2)}"),
  [("1", t("Simplify.", "Simplificar."), f"{r(8)} = √(4 · 2) = {r(2, 2)}."),
   ("2", t("Now they are alike.", "Ahora son semejantes."), t(f"Both have {r(2)}: {r(2, 2)} + {r(2)}.", f"Los dos tienen {r(2)}: {r(2, 2)} + {r(2)}.")),
   ("3", t("Add the coefficients.", "Sumar los coeficientes."), t(f"{r(2)} = 1{r(2)}, so 2 + 1 = 3.", f"{r(2)} = 1{r(2)}, así que 2 + 1 = 3.")),
   ("✓", t("Answer.", "Respuesta."), f"{r(8)} + {r(2)} = <strong>{r(3, 2)}</strong>")])}
{tabla(t("Can they be combined?", "¿Se pueden combinar?"), t("Combining radicals: three cases, whether they combine, and the result", "Combinar radicales: tres casos, si se combinan y el resultado"), [t("Case", "Situación"), t("Can they be combined?", "¿Se pueden combinar?"), t("Result", "Resultado")],
  [[f"{r(3, 2)} + {r(5, 2)}", t("Yes, same irrational part", "Sí, misma parte irracional"), r(8, 2)],
   [f"{r(2)} + {r(3)}", t("No, different irrational parts", "No, distinta parte irracional"), t("Left as it is", "Se deja indicado")],
   [f"{r(8)} + {r(2)}", t(f"Yes, after simplifying {r(8)} = {r(2, 2)}", f"Sí, tras simplificar {r(8)} = {r(2, 2)}"), r(3, 2)]])}
{practica("p1", t("Practice 1 — Combine directly?", "Práctica 1 — ¿Se combinan directamente?"), t(f"Can you combine {r(2)} + {r(3)} directly?", f"¿Se pueden combinar directamente {r(2)} + {r(3)}?"),
          [("a", t(f"Yes, it gives {r(5)}", f"Sí, da {r(5)}")), ("b", t("No, the irrational parts are different", "No, distinta parte irracional")), ("c", t(f"Yes, it gives {r(2, 5)}", f"Sí, da {r(2, 5)}"))])}
{practica("p2", t("Practice 2 — Add", "Práctica 2 — Sumar"), f"{r(4, 3)} + {r(2, 3)} =",
          [("a", r(6, 3)), ("b", r(6, 6)), ("c", r(8, 3))])}
{practica("p3", t("Practice 3 — Simplify first", "Práctica 3 — Simplificar primero"), t(f"{r(12)} + {r(3)} = (simplify {r(12)} first)", f"{r(12)} + {r(3)} = (simplifique {r(12)} primero)"),
          [("a", r(15)), ("b", r(2, 15)), ("c", r(3, 3))])}
{enlace(n, t("simplify-first", "simplificar-primero"), t("alike or not? Simplify first", "¿semejantes o no? Simplificar primero"), t("Simplify first to find out which radicals can be combined.", "Simplifique primero para descubrir qué radicales se pueden combinar."))}'''

    s3 = f'''<p>{t("To multiply, use the product property again, now in the joining direction: the product of the roots is the root of the product. Simplify the result at the end.", "Para multiplicar se usa de nuevo la propiedad del producto, ahora en dirección de unir: el producto de las raíces es la raíz del producto. Conviene simplificar el resultado al final.")}</p>
{big(f'{r("a")} · {r("b")} = √(a · b)')}
{ejemplo(t(f"Example 4: multiply {r(3)} · {r(5)}", f"Ejemplo 4: multiplique {r(3)} · {r(5)}"),
  [("1", t("Join them under one radical.", "Unir bajo un solo radical."), f"√(3 · 5) = {r(15)}."),
   ("2", t("Simplify?", "¿Simplificar?"), t("15 has no perfect squares: it is already simple.", "15 no tiene cuadrados perfectos: ya está simple.")),
   ("✓", t("Answer.", "Respuesta."), f"{r(3)} · {r(5)} = <strong>{r(15)}</strong>")])}
{ejemplo(t(f"Example 5: multiply {r(6)} · {r(2)}", f"Ejemplo 5: multiplique {r(6)} · {r(2)}"),
  [("1", t("Join them.", "Unir."), f"√(6 · 2) = {r(12)}."),
   ("2", t("Simplify.", "Simplificar."), f"{r(12)} = √(4 · 3) = {r(2, 3)}."),
   ("✓", t("Answer.", "Respuesta."), f"{r(6)} · {r(2)} = <strong>{r(2, 3)}</strong>")])}
{ejemplo(t(f"Example 6: multiply {r(2)} · ({r(2)} + 5)", f"Ejemplo 6: multiplique {r(2)} · ({r(2)} + 5)"),
  [("1", t("Distribute.", "Distribuir."), f"{r(2)} · {r(2)} + {r(2)} · 5."),
   ("2", t("Each product.", "Cada producto."), t(f"{r(2)} · {r(2)} = {r(4)} = 2, and {r(2)} · 5 = {r(5, 2)}.", f"{r(2)} · {r(2)} = {r(4)} = 2, y {r(2)} · 5 = {r(5, 2)}.")),
   ("✓", t("Answer.", "Respuesta."), f"{r(2)} · ({r(2)} + 5) = <strong>2 + {r(5, 2)}</strong>")])}
{caja("tip", t("A root times itself", "Una raíz por sí misma"), t(f"<p>{r('a')} · {r('a')} = √(a · a) = a. For example, {r(7)} · {r(7)} = 7. This is the idea that defines the square root, and it comes up often when you distribute.</p>", f"<p>{r('a')} · {r('a')} = √(a · a) = a. Por ejemplo, {r(7)} · {r(7)} = 7. Esta es la idea que define la raíz cuadrada y aparece con frecuencia al distribuir.</p>"))}
{practica("p4", t("Practice 4 — Multiply", "Práctica 4 — Multiplicar"), f"{r(5)} · {r(2)} =",
          [("a", r(10)), ("b", r(7)), ("c", "10")])}
{practica("p5", t("Practice 5 — A root times itself", "Práctica 5 — Una raíz por sí misma"), f"{r(3)} · {r(3)} =",
          [("a", r(3)), ("b", "3"), ("c", "9")])}
{practica("p6", t("Practice 6 — Multiply and simplify", "Práctica 6 — Multiplicar y simplificar"), f"{r(8)} · {r(2)} =",
          [("a", r(10)), ("b", r(2, 8)), ("c", "4")])}
{enlace(n, t("multiply", "multiplicar"), t("multiplying radicals", "multiplicar radicales"), t("Join the roots under one radical and simplify the product.", "Una las raíces bajo un solo radical y simplifique el producto."))}'''

    s4 = f'''<p>{t("An irrational radical has no exact decimal value, but you can approximate it. First trap it between two whole numbers using perfect squares; then use the calculator. This helps you estimate results and check your work.", "Un radical irracional no tiene un valor decimal exacto, pero se puede aproximar. Primero se acorrala entre dos enteros con los cuadrados perfectos; después se usa la calculadora. Esto ayuda a estimar resultados y a verificar operaciones.")}</p>
{ejemplo(t(f"Example 7: between which whole numbers is {r(20)}?", f"Ejemplo 7: ¿entre qué enteros está {r(20)}?"),
  [("1", t("Perfect squares around it.", "Cuadrados perfectos alrededor."), "16 &lt; 20 &lt; 25."),
   ("2", t("Take the roots.", "Sacar las raíces."), "4 &lt; " + r(20) + " &lt; 5."),
   ("✓", t("Answer.", "Respuesta."), t(f"{r(20)} is between 4 and 5. The calculator gives 4.472…, so {r(20)} ≈ <strong>4.5</strong> to the nearest tenth.", f"{r(20)} está entre 4 y 5. La calculadora da 4.472…, así que {r(20)} ≈ <strong>4.5</strong> a la décima."))])}
{ejemplo(t(f"Example 8: approximate {r(3, 2)} to two decimal places", f"Ejemplo 8: aproxime {r(3, 2)} a dos decimales"),
  [("1", t("On the calculator.", "En la calculadora."), f"{r(2)} ≈ 1.41421."),
   ("2", t("Multiply by the coefficient.", "Multiplicar por el coeficiente."), "3 × 1.41421 = 4.24264."),
   ("✓", t("Answer.", "Respuesta."), f"{r(3, 2)} ≈ <strong>4.24</strong>")])}
{calc(t("Approximating on the calculator", "Aproximar con la calculadora"), t(f"<p>For {r(3, 2)}: {T('3')} {T('×')} {T('2nd')} {T('x<sup>2</sup>')} {T('2')} {T('enter')} shows 4.242640687. Round at the end, not before: if you round {r(2)} to 1.41 first, you get 4.23, which is off in the last digit.</p>",
f"<p>Para {r(3, 2)}: {T('3')} {T('×')} {T('2nd')} {T('x<sup>2</sup>')} {T('2')} {T('enter')} muestra 4.242640687. Redondee al final, no antes: si redondea primero {r(2)} a 1.41, obtiene 4.23, que falla en la última cifra.</p>"))}
{caja("tip", t("Estimate to check", "Estimar para verificar"), t(f"<p>If a sum of radicals gives, for example, {r(3, 3)}, check that {r(3, 3)} ≈ 5.20 and compare it with the decimal value of the original expression. If the decimals match, the operation is right.</p>", f"<p>Si una suma de radicales da, por ejemplo, {r(3, 3)}, se puede comprobar que {r(3, 3)} ≈ 5.20 y compararlo con el decimal de la expresión original. Si los decimales coinciden, la operación es correcta.</p>"))}
{enlace(n, t("approximate", "aproximar"), t("approximating radicals", "aproximar radicales"), t("Trap the root between two whole numbers, then between two tenths.", "Acorrale la raíz entre dos enteros y luego entre dos décimas."))}'''

    secciones = [("s-" + t("like", "semejantes"), t("Adding and subtracting like radicals", "Sumar y restar radicales semejantes"), s1),
                 ("s-" + t("simplify-first", "simplificar-primero"), t("Alike or not? Simplify first", "¿Semejantes o no? Simplificar primero"), s2),
                 ("s-" + t("multiply", "multiplicar"), t("Multiplying radicals", "Multiplicar radicales"), s3),
                 ("s-" + t("approximate", "aproximar"), t("Approximating radicals", "Aproximar radicales"), s4)]

    lesson = {"next": t("Lesson 3.3", "Lección 3.3"), "review": t("sections 1 to 3", "las secciones 1 a 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("The radicands are not added. Check: 1.414 + 1.732 is not √5 ≈ 2.236.", "Los radicandos no se suman. Compruebe: 1.414 + 1.732 no es √5 ≈ 2.236."), "c": t("Only like radicals combine, and these have different irrational parts.", "Solo se combinan los semejantes, y estos tienen distinta parte irracional.")}, "right": t(f"{r(2)} and {r(3)} have different irrational parts: the sum is left as it is.", f"{r(2)} y {r(3)} tienen distinta parte irracional: la suma se deja indicada."), "solution": t(f"They are not like radicals, so {r(2)} + {r(3)} stays as it is. Check: 1.414 + 1.732 = 3.146, but {r(5)} ≈ 2.236.", f"No son semejantes, así que {r(2)} + {r(3)} se deja indicado. Compruebe: 1.414 + 1.732 = 3.146, pero {r(5)} ≈ 2.236.")},
      "p2": {"ok": "a", "hints": {"b": t("The irrational part stays the same: do not add the radicands.", "La parte irracional se conserva: no se suman los radicandos."), "c": t("The coefficients are added, not multiplied.", "Los coeficientes se suman, no se multiplican.")},
             "right": t(f"4 + 2 = 6, and {r(3)} stays the same.", f"4 + 2 = 6, y {r(3)} se conserva."), "solution": f"{r(4, 3)} + {r(2, 3)} = (4 + 2){r(3)} = {r(6, 3)}."},
      "p3": {"ok": "c", "hints": {"a": t(f"Radicands are not added. Simplify {r(12)} first.", f"Los radicandos no se suman. Simplifique primero {r(12)}."), "b": t(f"Radicands are not added. {r(12)} = {r(2, 3)}.", f"Los radicandos no se suman. {r(12)} = {r(2, 3)}.")},
             "right": t(f"{r(12)} = {r(2, 3)}, and {r(2, 3)} + {r(3)} = {r(3, 3)}.", f"{r(12)} = {r(2, 3)}, y {r(2, 3)} + {r(3)} = {r(3, 3)}."), "solution": f"{r(12)} + {r(3)} = {r(2, 3)} + {r(3)} = {r(3, 3)}."},
      "p4": {"ok": "a", "hints": {"b": t("The radicands are multiplied, not added.", "Los radicandos se multiplican, no se suman."), "c": t("The product stays inside the radical.", "El producto sigue dentro del radical.")},
             "right": f"√(5 · 2) = {r(10)}.", "solution": f"{r(5)} · {r(2)} = √(5 · 2) = {r(10)}."},
      "p5": {"ok": "b", "hints": {"a": t("A root times itself loses the radical.", "Una raíz por sí misma pierde el radical."), "c": t(f"{r(3)} · {r(3)} = {r(9)} = 3, not 9.", f"{r(3)} · {r(3)} = {r(9)} = 3, no 9.")},
             "right": f"{r(3)} · {r(3)} = {r(9)} = 3.", "solution": f"{r(3)} · {r(3)} = {r(9)} = 3."},
      "p6": {"ok": "c", "hints": {"a": t("The radicands are multiplied, not added.", "Los radicandos se multiplican, no se suman."), "b": t("That would be adding the radicals, not multiplying them.", "Eso sería sumar los radicales, no multiplicarlos.")},
             "right": f"√(8 · 2) = {r(16)} = 4.", "solution": f"{r(8)} · {r(2)} = {r(16)} = 4."}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("Different irrational parts.", "Distinta parte irracional."), "b": t("Different irrational parts.", "Distinta parte irracional."), "d": t("Different irrational parts, even with the same coefficient.", "Distinta parte irracional, aunque el coeficiente sea igual.")}, "solution": t(f"Only {r(4, 7)} and {r(2, 7)} share the irrational part {r(7)}.", f"Solo {r(4, 7)} y {r(2, 7)} comparten la parte irracional {r(7)}.")},
      "B": {"ok": "b", "hints": {"a": t("The radicand stays the same: do not add it.", "El radicando se conserva: no se suma."), "c": t("The coefficients are added, not multiplied.", "Los coeficientes se suman, no se multiplican."), "d": t("The radical does not disappear.", "El radical no desaparece.")}, "solution": f"3 + 5 = 8: {r(8, 2)}."},
      "C": {"ok": "d", "hints": {"a": t("The radical does not disappear.", "El radical no desaparece."), "b": t("It is a subtraction.", "Es una resta."), "c": t("The radicand stays the same.", "El radicando se conserva.")}, "solution": f"7 − 2 = 5: {r(5, 5)}."},
      "D": {"ok": "c", "hints": {"a": t("Radicands are not added.", "Los radicandos no se suman."), "b": t("Radicands are not added.", "Los radicandos no se suman."), "d": t(f"Simplify {r(8)} = {r(2, 2)} first.", f"Simplifique primero {r(8)} = {r(2, 2)}.")}, "solution": f"{r(2, 2)} + {r(2)} = {r(3, 2)}."},
      "E": {"ok": "b", "hints": {"a": t("The radicands are multiplied.", "Los radicandos se multiplican."), "c": t("The product stays inside the radical.", "El producto queda dentro del radical."), "d": t("3 · 5 = 15.", "3 · 5 = 15.")}, "solution": f"√(3 · 5) = {r(15)}."},
      "F": {"ok": "a", "hints": {"b": t("The radicands are multiplied.", "Los radicandos se multiplican."), "c": t("√12 = 2√3.", "√12 = 2√3."), "d": t("The product stays inside the radical.", "El producto queda dentro del radical.")}, "solution": f"{r(12)} = {r(2, 3)}."},
      "G": {"ok": "b", "hints": {"a": t("Distribute to both terms.", "Distribuya a los dos términos."), "c": t("2 and 5√2 are not like terms.", "2 y 5√2 no son semejantes."), "d": t("√2 · 5 = 5√2: the radical stays.", "√2 · 5 = 5√2: el radical se conserva.")}, "solution": f"{r(2)} · {r(2)} + {r(2)} · 5 = 2 + {r(5, 2)}."},
      "H": {"ok": "c", "hints": {"a": t("That is 3 + 3.", "Eso es 3 + 3."), "b": t("That is √3.", "Eso es √3."), "d": t("That is 3 · 3.", "Eso es 3 · 3.")}, "solution": "3 × 1.41421 ≈ 4.24."}
     }}

    quiz = [
     ("A", t("Which pair can be combined directly?", "¿Cuáles se pueden combinar directamente?"), [("a", f"{r(2)} " + t("and", "y") + f" {r(3)}"), ("b", f"{r(5)} " + t("and", "y") + f" {r(6)}"), ("c", f"{r(4, 7)} " + t("and", "y") + f" {r(2, 7)}"), ("d", f"{r(3, 2)} " + t("and", "y") + f" {r(3, 5)}")]),
     ("B", f"{r(3, 2)} + {r(5, 2)} =", [("a", r(8, 4)), ("b", r(8, 2)), ("c", r(15, 2)), ("d", "8")]),
     ("C", f"{r(7, 5)} − {r(2, 5)} =", [("a", "5"), ("b", r(9, 5)), ("c", r(5, 10)), ("d", r(5, 5))]),
     ("D", t(f"{r(8)} + {r(2)} = (simplify first)", f"{r(8)} + {r(2)} = (simplifique primero)"), [("a", r(10)), ("b", r(2, 10)), ("c", r(3, 2)), ("d", r(16))]),
     ("E", f"{r(3)} · {r(5)} =", [("a", r(8)), ("b", r(15)), ("c", "15"), ("d", r(35))]),
     ("F", t(f"{r(6)} · {r(2)} = (simplify)", f"{r(6)} · {r(2)} = (simplifique)"), [("a", r(2, 3)), ("b", r(8)), ("c", r(2, 6)), ("d", "12")]),
     ("G", f"{r(2)} · ({r(2)} + 5) =", [("a", f"{r(2)} + 5"), ("b", f"2 + {r(5, 2)}"), ("c", r(7, 2)), ("d", "2 + 5")]),
     ("H", t(f"Approximate {r(3, 2)} to two decimal places.", f"Aproxime {r(3, 2)} a dos decimales."), [("a", "6.00"), ("b", "1.73"), ("c", "4.24"), ("d", "9.00")])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("Add and subtract like radicals, simplifying first, and multiply radicals with the product property.", "Sume y reste radicales semejantes, simplificando primero, y multiplique radicales con la propiedad del producto."),
        ("🧮", t("Calculator to approximate", "Calculadora para aproximar")),
        [t("<strong>Add and subtract</strong> like radicals (with the same irrational part).", "<strong>Sumar y restar</strong> radicales semejantes (con la misma parte irracional)."),
         t("<strong>Simplify first</strong> radicals that do not look alike, to find out whether they are.", "<strong>Simplificar primero</strong> los radicales que no parecen semejantes, para revelar si lo son."),
         t("<strong>Multiply</strong> radicals with √a · √b = √(a · b), including a product with a binomial.", "<strong>Multiplicar</strong> radicales con √a · √b = √(a · b), incluido un producto con un binomio."),
         t("<strong>Approximate</strong> an irrational radical to two decimal places with the calculator.", "<strong>Aproximar</strong> un radical irracional a dos decimales con la calculadora.")],
        secciones,
        (t("Decide for three pairs of radicals whether they are alike (simplify first). Then do four additions and subtractions of radicals, four multiplications with the result simplified, and approximate one radical to two decimal places. For the approximation, always compare your estimate on paper with the calculator before you go on.",
           "Decida para tres parejas de radicales si son semejantes (simplificando primero). Después haga cuatro sumas y restas de radicales, cuatro multiplicaciones con el resultado simplificado y aproxime un radical a dos decimales. En la aproximación, compare siempre su estimación en papel con la calculadora antes de seguir."),
         t("A square garden has an area of 50 square feet and a square shed next to it has an area of 8 square feet. Their sides are √50 and √8 feet. Find the total length if you place them side by side (simplify first), and approximate it to two decimal places.",
           "Un jardín cuadrado tiene un área de 50 pies cuadrados y un cobertizo cuadrado a su lado tiene 8 pies cuadrados. Sus lados miden √50 y √8 pies. Halle el largo total si se colocan uno junto al otro (simplificando primero) y aproxímelo a dos decimales.")),
        quiz,
        t("Self-check checklist for operations with radicals", "Lista de autoevaluación para las operaciones con radicales"),
        t("Self-check checklist: skills for adding, subtracting, and multiplying radicals", "Lista de autoevaluación: destrezas para sumar, restar y multiplicar radicales"),
        [(t("Simplifying before combining", "Simplificar antes de combinar"), t("I simplify each radical before I decide whether they are alike.", "Simplifico cada radical antes de decidir si son semejantes."), t("I simplify only some radicals before I operate.", "Simplifico solo algunos radicales antes de operar."), t("I try to combine without simplifying first.", "Intento combinar sin simplificar primero.")),
         (t("Combining like radicals", "Combinar radicales semejantes"), t("I combine only radicals with the same irrational part and leave the rest as it is.", "Combino solo radicales con la misma parte irracional y dejo indicado lo demás."), t("I combine like radicals, with mistakes in the coefficients.", "Combino los semejantes con errores de coeficiente."), t("I combine radicals with different irrational parts.", "Combino radicales de distinta parte irracional.")),
         (t("Multiplying and simplifying", "Multiplicar y simplificar"), t("I multiply, simplify the product, and distribute over a binomial.", "Multiplico, simplifico el producto y distribuyo sobre un binomio."), t("I multiply, but I do not simplify the result.", "Multiplico, pero no simplifico el resultado."), t("I do not use √a · √b = √(a · b).", "No aplico √a · √b = √(a · b)."))],
        t("<p>You worked with radicals: you add and subtract only those with the same irrational part, like like terms, simplifying first to find out which ones they are; and you multiply with √a · √b = √(a · b), simplifying the result. You also approximated a radical with the calculator.</p>\n<p>In <strong>Lesson 3.3 · The real number system</strong> you will see where these radicals fit among all the numbers: you will sort numbers into rational and irrational, place irrational numbers on the number line, and close Topic 3 with a full view of the real numbers.</p>",
          "<p>Operó con radicales: se suman y restan solo los que tienen la misma parte irracional —como términos semejantes—, simplificando primero para descubrir cuáles lo son, y se multiplican con √a · √b = √(a · b), simplificando el resultado. También aproximó un radical con la calculadora.</p>\n<p>En la <strong>Lección 3.3 · El sistema de números reales</strong> verá el lugar de estos radicales entre todos los números: clasificará números en racionales e irracionales, ubicará irracionales en la recta numérica y cerrará el Tema 3 con una mirada completa a los números reales.</p>"),
        ("3-3", ("", t("Lesson 3.3 · The real number system: rational, irrational, and the number line", "Lección 3.3 · El sistema de números reales: racionales, irracionales y la recta numérica"))),
        [(t("like radicals", "radicales semejantes"), t("Radicals with the same irrational part, like 3√2 and 5√2. Only like radicals can be added or subtracted.", "Radicales con la misma parte irracional, como 3√2 y 5√2. Solo los semejantes se pueden sumar o restar.")),
         (t("coefficient", "coeficiente"), t("The number in front of the radical. In 5√2, the coefficient is 5.", "El número que va delante del radical. En 5√2, el coeficiente es 5.")),
         (t("irrational part", "parte irracional"), t("The radical that is left after simplifying. In 5√2, it is √2.", "El radical que queda después de simplificar. En 5√2, es √2.")),
         (t("approximate", "aproximar"), t("To give a decimal value that is close to the exact value, like √2 ≈ 1.41.", "Dar un valor decimal cercano al valor exacto, como √2 ≈ 1.41."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function entero(id, min, max){ var s = $(id).value.trim(); if (!/^\d+$/.test(s)) return null; var n = parseInt(s, 10); return (n < min || n > max) ? null : n; }
function libreCuadrados(n){ return simplRad(n).k === 1; }
function signo(c){ return String(c).replace("-", "−"); }

/* ============ MODULE 1 · can they be combined? ============ */
function pintaSM(){
  var a = entero("sm-a", 1, 20), r1 = entero("sm-r1", 2, 200), b = entero("sm-b", 1, 20), r2 = entero("sm-r2", 2, 200), op = $("sm-op").value, av = $("sm-aviso");
  if (a === null || r1 === null || b === null || r2 === null){
    av.className = "caja-aviso visible"; av.textContent = T("Use whole-number coefficients from 1 to 20 and whole-number radicands from 2 to 200.", "Use coeficientes enteros de 1 a 20 y radicandos enteros de 2 a 200.");
    $("sm-salida").innerHTML = ""; return;
  }
  av.className = "caja-aviso"; av.textContent = "";
  var sg = op === "+" ? 1 : -1, orig = [TM(a, r1), TM(sg * b, r2)], h = '<div class="linea grande">' + exprHTML(orig) + "</div>";
  if (r1 === r2){
    var c = a + sg * b, res = c === 0 ? [] : [TM(c, r1)];
    h += '<div class="linea">' + T("They have the same irrational part, " + radHTML(1, r1) + ", so you " + (op === "+" ? "add" : "subtract") + " the coefficients: " + a + " " + op + " " + b + " = " + signo(c) + ".", "Tienen la misma parte irracional, " + radHTML(1, r1) + ": se " + (op === "+" ? "suman" : "restan") + " los coeficientes, " + a + " " + op + " " + b + " = " + signo(c) + ".") + "</div>";
    h += '<div class="linea">' + T("It is like ", "Es como ") + a + "x " + op + " " + b + "x = " + (c === 0 ? "0" : signo(c) + "x") + ".</div>";
    h += '<div class="linea veredicto">✓ ' + exprHTML(orig) + " = " + exprHTML(res) + "</div>";
    h += '<div class="linea nota">' + T("Check: " + aprox(valor(orig), 3) + " and " + aprox(valor(res), 3) + " match.", "Comprobación: " + aprox(valor(orig), 3) + " y " + aprox(valor(res), 3) + " coinciden.") + "</div>";
  } else {
    var s1 = simplRad(r1), s2 = simplRad(r2);
    h += '<div class="linea veredicto">' + T("The irrational parts are different (" + radHTML(1, r1) + " and " + radHTML(1, r2) + "): they are not like radicals, and the expression is left as it is.", "La parte irracional es distinta (" + radHTML(1, r1) + " y " + radHTML(1, r2) + "): no son semejantes y se deja indicado.") + "</div>";
    if (op === "+"){
      var trampa = [TM(a + b, r1 + r2)];
      h += '<div class="linea">' + T("The “add everything” mistake would give ", "El error de «sumar todo» daría ") + exprHTML(trampa) + " ≈ " + aprox(valor(trampa), 3) + T(", but ", ", pero ") + exprHTML(orig) + " ≈ " + aprox(valor(orig), 3) + T(". They do not match.", ". No coinciden.") + "</div>";
    } else h += '<div class="linea">' + T("Approximate value: ", "Valor aproximado: ") + exprHTML(orig) + " ≈ " + aprox(valor(orig), 3) + ".</div>";
    if (s1.r === s2.r) h += '<div class="linea"><strong>' + T("But careful:", "Pero ojo:") + "</strong> " + T("if you simplify, ", "si se simplifica, ") + radHTML(1, r1) + " = " + radHTML(s1.k, s1.r) + T(" and ", " y ") + radHTML(1, r2) + " = " + radHTML(s2.k, s2.r) +
      T(". They are like radicals after all! That is what module 2 is about: ", ". ¡Sí son semejantes! Eso es lo que se trabaja en el módulo 2: ") + '<a href="#' + T("simplify-first", "simplificar-primero") + '">' + T("simplify first", "simplificar primero") + "</a>.</div>";
  }
  $("sm-salida").innerHTML = h;
}
var BASES = [2, 3, 5, 6, 7, 10, 11];
function genSemej(){
  var tp = aleatorio(1, 4), r = elige(BASES), a = aleatorio(1, 9), b = aleatorio(1, 9), o, pc = {};
  if (tp === 1 || tp === 4){
    if (tp === 4) a = 1;
    var res = [TM(a + b, r)]; o = [opExpr(res)];
    var d1 = opExpr([TM(a + b, 2 * r)]); o.push(d1); pc[d1.clave] = T("The irrational part stays the same: radicands are not added.", "La parte irracional se conserva: no se suman los radicandos.");
    var d2 = opExpr([TM(a * b, r)]); if (d2.clave !== o[0].clave){ o.push(d2); pc[d2.clave] = T("The coefficients are added, not multiplied.", "Los coeficientes se suman, no se multiplican."); }
    var d3 = {html: String(a + b), clave: "n" + (a + b)}; o.push(d3); pc[d3.clave] = T("The radical does not disappear when you add: ", "El radical no desaparece al sumar: se conserva ") + radHTML(1, r) + T(" stays.", ".");
    if (tp === 4){ var d4 = opExpr([TM(b, r)]); o.push(d4); pc[d4.clave] = radHTML(1, r) + T(" counts as 1", " vale como 1") + radHTML(1, r) + T(": its coefficient is 1, not 0.", ": su coeficiente es 1, no 0."); }
    return {enun: T("Work out ", "Calcule ") + exprHTML([TM(a, r), TM(b, r)]) + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
      bien: T("Add the coefficients, " + a + " + " + b + " = " + (a + b) + ", and keep ", "Se suman los coeficientes, " + a + " + " + b + " = " + (a + b) + ", y se conserva ") + radHTML(1, r) + ".", mal: T("The answer is ", "La respuesta es ") + exprHTML(res) + "."};
  }
  if (tp === 2){
    if (a === b) a = b + aleatorio(1, 4);
    if (a < b){ var x = a; a = b; b = x; }
    var res2 = [TM(a - b, r)]; o = [opExpr(res2)];
    var e1 = {html: String(a - b), clave: "n" + (a - b)}; o.push(e1); pc[e1.clave] = T("The radical does not disappear when you subtract: ", "El radical no desaparece al restar: se conserva ") + radHTML(1, r) + T(" stays.", ".");
    var e2 = opExpr([TM(a + b, r)]); o.push(e2); pc[e2.clave] = T("It is a subtraction: the coefficients are subtracted.", "Es una resta: los coeficientes se restan.");
    o.push({html: T("They cannot be subtracted", "No se pueden restar"), clave: "ind"}); pc.ind = T("Yes, they can: they have the same irrational part.", "Sí se pueden: tienen la misma parte irracional.");
    return {enun: T("Work out ", "Calcule ") + exprHTML([TM(a, r), TM(-b, r)]) + ".", opciones: o, correcta: o[0].clave, porClave: pc,
      bien: T("Subtract the coefficients, " + a + " − " + b + " = " + (a - b) + ", and keep ", "Se restan los coeficientes, " + a + " − " + b + " = " + (a - b) + ", y se conserva ") + radHTML(1, r) + ".", mal: T("The answer is ", "La respuesta es ") + exprHTML(res2) + "."};
  }
  var r2 = elige(BASES.filter(function(z){ return z !== r; })); a = elige([1, 1, 2, 3]); b = elige([1, 1, 2, 4]);
  var orig = [TM(a, r), TM(b, r2)];
  o = [{html: T("Left as it is: ", "Se deja indicado: ") + exprHTML(orig), clave: "ind"}];
  var f1 = opExpr([TM(a + b, r + r2)]); o.push(f1); pc[f1.clave] = T("Different radicands cannot be added.", "No se pueden sumar radicandos distintos.");
  var f2 = opExpr([TM(a + b, r)]); o.push(f2); pc[f2.clave] = T("Only terms with the same irrational part combine.", "Solo se combinan términos con la misma parte irracional.");
  var f3 = opExpr([TM(a * b, r * r2)]); o.push(f3); pc[f3.clave] = T("That would be a multiplication, not a sum.", "Eso sería una multiplicación, no una suma.");
  return {enun: T("Work out ", "Calcule ") + exprHTML(orig) + ".", opciones: o, correcta: "ind", porClave: pc,
    bien: T("The irrational parts are different, so they are not like radicals. Check: " + aprox(valor(orig), 3) + " is not equal to " + aprox(valor([TM(a + b, r + r2)]), 3) + ".", "La parte irracional es distinta, así que no son semejantes. Compruébelo: " + aprox(valor(orig), 3) + " no es igual a " + aprox(valor([TM(a + b, r + r2)]), 3) + "."),
    mal: T("Since ", "Como ") + radHTML(1, r) + T(" and ", " y ") + radHTML(1, r2) + T(" are different, the sum is left as it is.", " son distintos, la suma se deja indicada.")};
}

/* ============ MODULE 2 · simplify first ============ */
var SP = {lista: [[1, 8, 1, 1, 2], [1, 12, 1, 1, 27], [1, 50, -1, 1, 18], [1, 20, 1, 1, 45], [1, 8, 1, 1, 3], [1, 75, -1, 1, 12], [3, 8, 1, 1, 32], [1, 12, 1, 1, 3]], pasos: [], visto: 0};
function exprOriginal(e){ return [TM(e[0], e[1]), TM(e[2] * e[3], e[4])]; }
function llenaSP(){
  var sel = $("sp-sel"); sel.innerHTML = "";
  SP.lista.forEach(function(e, i){ var o = document.createElement("option"); o.value = i; o.textContent = exprVis(exprOriginal(e)).replace(/<[^>]+>/g, ""); sel.appendChild(o); });
}
function resuelveSP(e){ var orig = exprOriginal(e), simp = orig.map(simplTermino), res = combina(simp); return {orig: orig, simp: simp, res: res, semej: simp[0].r === simp[1].r}; }
function preparaSP(){
  var e = SP.lista[parseInt($("sp-sel").value, 10)], R = resuelveSP(e);
  SP.pasos = []; SP.visto = 0;
  $("sp-expr").innerHTML = '<span class="grande">' + exprHTML(R.orig) + "</span>";
  R.orig.forEach(function(x, i){
    var s = simplRad(x.r), k = Math.abs(x.k), txt = (i === 0 ? T("First term: ", "Primer término: ") : T("Second term: ", "Segundo término: "));
    if (s.k === 1) txt += radHTML(k, x.r) + T(" is already simple.", " ya está simple.");
    else if (k === 1) txt += radHTML(1, x.r) + " = √(" + (s.k * s.k) + " · " + s.r + ") = " + radHTML(s.k, s.r) + ".";
    else txt += radHTML(k, x.r) + " = " + k + " · " + radHTML(s.k, s.r) + " = " + radHTML(k * s.k, s.r) + ".";
    SP.pasos.push(txt);
  });
  if (R.semej) SP.pasos.push(T("Now both terms have ", "Ahora los dos términos tienen ") + radHTML(1, R.simp[0].r) + T(": they are like radicals. Combine the coefficients: ", ": son semejantes. Se combinan los coeficientes: ") + exprHTML(R.simp) + " = " + exprHTML(R.res) + ".");
  else SP.pasos.push(T("After simplifying, the irrational parts are still different (", "Después de simplificar, la parte irracional sigue siendo distinta (") + radHTML(1, R.simp[0].r) + T(" and ", " y ") + radHTML(1, R.simp[1].r) + T("): they are not like radicals.", "): no son semejantes."));
  SP.pasos.push('<span class="veredicto">' + T("Answer: ", "Resultado: ") + exprHTML(R.orig) + " = " + exprHTML(R.semej ? R.res : R.simp) + "</span>" + (R.semej ? "" : T(" (left as it is)", " (se deja indicado)")));
  pintaSP();
}
function pintaSP(){
  $("sp-pasos").innerHTML = SP.pasos.slice(0, SP.visto).map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i === SP.pasos.length - 1 ? "✓" : i + 1) + "</span>" + p + "</div>"; }).join("");
  var b = $("sp-sig"); b.disabled = SP.visto >= SP.pasos.length; $("sp-todo").disabled = b.disabled;
  b.textContent = SP.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
}
function exprAzar(semejantes){
  var b = elige([2, 3, 5, 6, 7]), s1 = aleatorio(1, 5), s2 = aleatorio(1, 5), k1 = elige([1, 1, 1, 2, 3]), k2 = elige([1, 1, 1, 2]);
  if (s1 === 1 && s2 === 1) s1 = aleatorio(2, 5);
  var b2 = semejantes ? b : elige([2, 3, 5, 6, 7].filter(function(z){ return z !== b; }));
  var sg = Math.random() < 0.6 ? 1 : -1;
  if (sg < 0 && k1 * s1 < k2 * s2){ var x = s1; s1 = s2; s2 = x; var u = k1; k1 = k2; k2 = u; }
  return [k1, s1 * s1 * b, sg, k2, s2 * s2 * b2];
}
function azarSP(){ SP.lista.push(exprAzar(Math.random() < 0.8)); llenaSP(); $("sp-sel").value = SP.lista.length - 1; preparaSP(); }
function genSimplCombina(){
  var e, R, o, pc = {}, usadas = {};
  do { e = exprAzar(Math.random() < 0.75); R = resuelveSP(e); } while (R.semej && (!R.res.length || e[0] + e[2] * e[3] === 0));
  var enun = T("Work out ", "Calcule ") + exprHTML(R.orig) + T(". Simplify each radical first.", ". Simplifique primero cada radical.");
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  if (R.semej){
    o = []; mete(opExpr(R.res));
    if (e[2] > 0 && e[0] === 1 && e[3] === 1) mete(opRad(1, e[1] + e[4]), T("Radicands are not added: simplify each radical first.", "Los radicandos no se suman: primero se simplifica cada radical."));
    mete({html: T("They cannot be combined", "No se pueden combinar"), clave: "ind"}, T("Yes, they can: after simplifying, both have ", "Sí se pueden: después de simplificar, los dos tienen ") + radHTML(1, R.simp[0].r) + ".");
    if (R.res.length) mete(opExpr([TM(R.res[0].k + (R.res[0].k > 0 ? 1 : -1), R.res[0].r)]), T("Check the coefficients after simplifying.", "Revise los coeficientes después de simplificar."));
    mete(opExpr([TM(e[0] + e[2] * e[3], R.simp[0].r)]), T("You forgot the coefficients that come out when you simplify.", "Faltó usar los coeficientes que salen al simplificar."));
    return {enun: enun, opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
      bien: exprHTML(R.orig) + " = " + exprHTML(R.simp) + " = " + exprHTML(R.res) + ".", mal: T("Simplify: ", "Se simplifica: ") + exprHTML(R.simp) + " = " + exprHTML(R.res) + "."};
  }
  o = []; mete({html: T("Left as it is: ", "Se deja indicado: ") + exprHTML(R.simp), clave: "ind"});
  mete(opExpr([TM(Math.abs(R.simp[0].k) + Math.abs(R.simp[1].k), R.simp[0].r)]), T("After simplifying, the irrational parts are still different: they do not combine.", "Después de simplificar, la parte irracional sigue siendo distinta: no se combinan."));
  mete(opExpr([TM(Math.abs(R.simp[0].k) + Math.abs(R.simp[1].k), R.simp[0].r + R.simp[1].r)]), T("Different radicands are not added.", "No se suman radicandos distintos."));
  mete({html: T("Left as it is: ", "Se deja indicado: ") + exprHTML(R.orig), clave: "orig"}, T("It is left as it is, yes, but first simplify each radical.", "Se deja indicado, sí, pero primero hay que simplificar cada radical."));
  return {enun: enun, opciones: o, correcta: "ind", porClave: pc,
    bien: T("Simplified, it is ", "Simplificado queda ") + exprHTML(R.simp) + T(", and since the irrational parts are different, it is left as it is.", ", y como la parte irracional es distinta, se deja indicado."),
    mal: T("It simplifies to ", "Se simplifica a ") + exprHTML(R.simp) + T(", which cannot be combined.", ", que no se puede combinar.")};
}
function genEscribeSP(){
  var e, R;
  do { e = exprAzar(true); R = resuelveSP(e); } while (!R.res.length || R.res[0].k <= 0);
  return {enun: T("Work out ", "Calcule ") + exprHTML(R.orig) + T(" and write the result as a single term.", " y escriba el resultado como un solo término."), k: R.res[0].k, r: R.res[0].r,
    explica: exprHTML(R.orig) + " = " + exprHTML(R.simp) + " = " + exprHTML(R.res) + "."};
}

/* ============ MODULE 3 · multiplying ============ */
var MU_COLA = [[1, 3, 1, 5], [1, 2, 1, 2], [2, 3, 4, 6], [1, 8, 1, 2]];
function pintaMU(){
  var k1 = entero("mu-k1", 1, 20), a = entero("mu-a", 1, 200), k2 = entero("mu-k2", 1, 20), b = entero("mu-b", 1, 200), av = $("mu-aviso");
  if (k1 === null || a === null || k2 === null || b === null){
    av.className = "caja-aviso visible"; av.textContent = T("Use whole-number coefficients from 1 to 20 and whole-number radicands from 1 to 200.", "Use coeficientes enteros de 1 a 20 y radicandos enteros de 1 a 200.");
    $("mu-salida").innerHTML = ""; return;
  }
  av.className = "caja-aviso"; av.textContent = "";
  var s = simplRad(a * b), kf = k1 * k2 * s.k, h = '<div class="linea grande">(' + radHTML(k1, a) + ")(" + radHTML(k2, b) + ") = " + radHTML(kf, s.r) + "</div>";
  h += '<div class="linea">' + T("Coefficients: ", "Coeficientes: ") + k1 + " · " + k2 + " = " + (k1 * k2) + T(". Radicands: ", ". Radicandos: ") + radHTML(1, a) + " · " + radHTML(1, b) + " = " + radHTML(1, a * b) + ".</div>";
  if (a === b) h += '<div class="linea">' + T("It is a root times itself: ", "Es una raíz por sí misma: ") + radHTML(1, a) + " · " + radHTML(1, a) + " = " + a + ".</div>";
  else if (s.k > 1) h += '<div class="linea">' + T("Simplify: ", "Se simplifica: ") + radHTML(1, a * b) + " = " + radHTML(s.k, s.r) + T(", and ", ", y ") + (k1 * k2) + " · " + radHTML(s.k, s.r) + " = " + radHTML(kf, s.r) + ".</div>";
  else h += '<div class="linea">' + T((a * b) + " has no perfect squares: ", (a * b) + " no tiene cuadrados perfectos: ") + radHTML(1, a * b) + T(" is already simple.", " ya está simple.") + "</div>";
  h += '<div class="linea nota">' + T("Check: ", "Comprobación: ") + aprox(k1 * Math.sqrt(a) * k2 * Math.sqrt(b), 3) + T(" and ", " y ") + aprox(kf * Math.sqrt(s.r), 3) + ".</div>";
  $("mu-salida").innerHTML = h;
}
function azarMU(){
  var e = MU_COLA.length ? MU_COLA.shift() : [elige([1, 1, 2, 3]), aleatorio(2, 15), elige([1, 1, 2, 5]), aleatorio(2, 15)];
  $("mu-k1").value = e[0]; $("mu-a").value = e[1]; $("mu-k2").value = e[2]; $("mu-b").value = e[3]; pintaMU();
}
function genMultiplicar(){
  var tp = aleatorio(1, 5), o, pc = {}, a, b, res;
  if (tp === 1){
    a = aleatorio(2, 15); while (esCuadrado(a)) a++;
    o = [{html: String(a), clave: "n" + a}];
    var d1 = opRad(1, a); o.push(d1); pc[d1.clave] = T("√a · √a is not √a: the radical disappears.", "√a · √a no es √a: el radical desaparece.");
    var d2 = {html: String(a * a), clave: "n" + a * a}; o.push(d2); pc[d2.clave] = T("√a · √a = √(a²) = a, not a².", "√a · √a = √(a²) = a, no a².");
    var d3 = opRad(2, a); o.push(d3); pc[d3.clave] = T("That would be √a + √a. Here you multiply.", "Eso sería √a + √a. Aquí se multiplica.");
    return {enun: T("Work out ", "Calcule ") + radHTML(1, a) + " · " + radHTML(1, a) + ".", opciones: o, correcta: o[0].clave, porClave: pc,
      bien: radHTML(1, a) + " · " + radHTML(1, a) + " = " + radHTML(1, a * a) + " = " + a + ".", mal: T("The answer is " + a + ": a root times itself gives the radicand.", "La respuesta es " + a + ": una raíz por sí misma da el radicando.")};
  }
  if (tp === 5){
    a = elige([2, 3, 5, 6, 7]); var c = aleatorio(2, 9);
    res = [TM(a, 1), TM(c, a)]; o = [opExpr(res)];
    var f1 = opExpr([TM(a, 1), TM(c, 1)]); o.push(f1); pc[f1.clave] = radHTML(1, a) + " · " + c + T(" is ", " es ") + radHTML(c, a) + T(": the radical stays.", ": el radical se conserva.");
    var f2 = opExpr([TM(a + c, a)]); o.push(f2); pc[f2.clave] = a + T(" and ", " y ") + radHTML(c, a) + T(" are not like terms: they do not combine.", " no son semejantes: no se combinan.");
    var f3 = opExpr([TM(2 * a, 1), TM(c, a)]); o.push(f3); pc[f3.clave] = radHTML(1, a) + " · " + radHTML(1, a) + " = " + a + T(", not ", ", no ") + (2 * a) + ".";
    return {enun: T("Work out ", "Calcule ") + radHTML(1, a) + " · (" + radHTML(1, a) + " + " + c + ").", opciones: o, correcta: o[0].clave, porClave: pc,
      bien: T("Distribute: ", "Se distribuye: ") + radHTML(1, a) + " · " + radHTML(1, a) + " = " + a + T(" and ", " y ") + radHTML(1, a) + " · " + c + " = " + radHTML(c, a) + ".",
      mal: T("The answer is ", "La respuesta es ") + exprHTML(res) + "."};
  }
  var k1 = tp === 4 ? aleatorio(2, 5) : 1, k2 = tp === 4 ? aleatorio(2, 5) : 1;
  do { a = aleatorio(2, 12); b = aleatorio(2, 12); } while (a === b || esCuadrado(a) || esCuadrado(b) || (tp === 2 && !libreCuadrados(a * b)) || (tp === 3 && libreCuadrados(a * b)));
  var s = simplRad(a * b), kf = k1 * k2 * s.k, usadas = {};
  o = [];
  function mete(op, msg){ if (usadas[op.clave]) return; usadas[op.clave] = 1; o.push(op); if (msg) pc[op.clave] = msg; }
  mete(opRad(kf, s.r));
  mete(opRad(k1 * k2, a + b), T("The radicands are multiplied, not added.", "Los radicandos se multiplican, no se suman."));
  mete({html: String(k1 * k2 * a * b), clave: "n" + k1 * k2 * a * b}, T("The product stays inside the radical: ", "El producto sigue dentro del radical: ") + radHTML(1, a * b) + ".");
  if (s.k > 1) mete(opRad(k1 * k2, a * b), T("The value is right, but ", "El valor es correcto, pero ") + radHTML(1, a * b) + T(" can still be simplified.", " todavía se puede simplificar."));
  if (tp === 4) mete(opRad((k1 + k2) * s.k, s.r), T("The coefficients outside are multiplied, not added.", "Los coeficientes de fuera se multiplican, no se suman."));
  mete(opRad(kf + 1, s.r));
  return {enun: T("Work out ", "Calcule ") + (tp === 4 ? "(" + radHTML(k1, a) + ")(" + radHTML(k2, b) + ")" : radHTML(1, a) + " · " + radHTML(1, b)) + T(". Simplify the result.", ". Simplifique el resultado."),
    opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
    bien: T("Join them under one radical: ", "Se unen bajo un radical: ") + radHTML(k1 * k2, a * b) + (s.k > 1 ? T(", which simplifies to ", ", y se simplifica a ") + radHTML(kf, s.r) : "") + ".",
    mal: T("The answer is ", "La respuesta es ") + radHTML(kf, s.r) + "."};
}

/* ============ MODULE 4 · approximating ============ */
function pintaAP(){
  var n = entero("ap-n", 2, 200), av = $("ap-aviso");
  if (n === null){ av.className = "caja-aviso visible"; av.textContent = T("Type a whole number from 2 to 200.", "Escriba un número entero de 2 a 200."); $("ap-salida").innerHTML = ""; $("ap-recta").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var raiz = Math.sqrt(n), a = Math.floor(raiz + 1e-12), h;
  if (esCuadrado(n)){
    $("ap-recta").innerHTML = rectaSVG(Math.max(0, a - 1), a + 1, 0.1, [{v: a, txt: "√" + n}], T("Number line: the square root of " + n + " lands exactly on " + a, "Recta numérica: la raíz de " + n + " cae exactamente en " + a));
    $("ap-salida").innerHTML = '<div class="linea veredicto">' + T(n + " is a perfect square: ", n + " es un cuadrado perfecto: ") + radHTML(1, n) + " = " + a + T(" exactly. Try a number that is not.", " exactamente. Pruebe con un número que no lo sea.") + "</div>";
    return;
  }
  var d = Math.floor(raiz * 10 + 1e-9), t0 = d / 10, t1 = (d + 1) / 10;
  h = '<div class="linea"><strong>' + T("Between which whole numbers:", "Entre qué enteros:") + "</strong> " + (a * a) + " &lt; " + n + " &lt; " + ((a + 1) * (a + 1)) + T(", so ", ", así que ") + radHTML(1, n) + T(" is between " + a + " and " + (a + 1) + ".", " está entre " + a + " y " + (a + 1) + ".") + "</div>";
  h += '<div class="linea"><strong>' + T("Between which tenths:", "Entre qué décimas:") + "</strong> " + t0.toFixed(1) + "² = " + (d * d / 100).toFixed(2) + T(" and ", " y ") + t1.toFixed(1) + "² = " + ((d + 1) * (d + 1) / 100).toFixed(2) +
       T(". Since " + n + " is in between, ", ". Como " + n + " queda en medio, ") + radHTML(1, n) + T(" is between " + t0.toFixed(1) + " and " + t1.toFixed(1) + ".", " está entre " + t0.toFixed(1) + " y " + t1.toFixed(1) + ".") + "</div>";
  h += '<div class="linea veredicto">' + T("With the calculator: ", "Con la calculadora: ") + radHTML(1, n) + " ≈ " + aprox(raiz, 3) + T(", which rounds to " + aprox(raiz, 1) + " to the nearest tenth.", ", que redondeado a la décima es " + aprox(raiz, 1) + ".") + "</div>";
  $("ap-recta").innerHTML = rectaSVG(a, a + 1, 0.1, [{v: raiz, txt: "√" + n}], T("Number line from " + a + " to " + (a + 1) + " with the square root of " + n + " near " + aprox(raiz, 1), "Recta numérica de " + a + " a " + (a + 1) + " con la raíz de " + n + " cerca de " + aprox(raiz, 1)));
  $("ap-salida").innerHTML = h;
}
function azarAP(){ var n; do { n = aleatorio(2, 200); } while (esCuadrado(n)); $("ap-n").value = n; pintaAP(); }
function genEstimar(){
  if (Math.random() < 0.55){
    var n; do { n = aleatorio(2, 150); } while (esCuadrado(n));
    var a = Math.floor(Math.sqrt(n)), o = [], pc = {};
    [a - 1, a, a + 1, a + 2].forEach(function(i){ if (i >= 0){ o.push({html: T("Between " + i + " and " + (i + 1), "Entre " + i + " y " + (i + 1)), clave: "e" + i}); pc["e" + i] = T((i * i) + " and " + ((i + 1) * (i + 1)) + " do not surround " + n + ".", (i * i) + " y " + ((i + 1) * (i + 1)) + " no rodean a " + n + "."); } });
    var ok = "e" + a;
    return {enun: T("Between which two consecutive whole numbers is ", "¿Entre qué dos enteros consecutivos está ") + radHTML(1, n) + "?", opciones: o, correcta: ok, porClave: pc, enOrden: true,
      pista: T("Look for the perfect squares just below and just above " + n + ".", "Busque los cuadrados perfectos justo por debajo y justo por encima de " + n + "."),
      bien: (a * a) + " &lt; " + n + " &lt; " + ((a + 1) * (a + 1)) + T(", so ", ", así que ") + radHTML(1, n) + T(" is between " + a + " and " + (a + 1) + ".", " está entre " + a + " y " + (a + 1) + "."),
      mal: T("The perfect squares around " + n + " are " + (a * a) + " and " + ((a + 1) * (a + 1)) + ", so it is between " + a + " and " + (a + 1) + ".", "Los cuadrados perfectos que rodean a " + n + " son " + (a * a) + " y " + ((a + 1) * (a + 1)) + ", así que está entre " + a + " y " + (a + 1) + ".")};
  }
  var k = aleatorio(2, 6), r = elige([2, 3, 5, 6, 7]), v = k * Math.sqrt(r), op2 = [], pc2 = {}, usadas = {};
  function mete(x, msg){ var c = "a" + x; if (usadas[c]) return; usadas[c] = 1; op2.push({html: "≈ " + x, clave: c}); if (msg) pc2[c] = msg; }
  mete(aprox(v, 2));
  mete(aprox(Math.sqrt(k * r), 2), T("That is ", "Eso es ") + radHTML(1, k * r) + T(": the coefficient stays outside and multiplies the root.", ": el coeficiente queda fuera y multiplica a la raíz."));
  mete(aprox(k + Math.sqrt(r), 2), T("The coefficient multiplies the root; it is not added to it.", "El coeficiente multiplica a la raíz, no se le suma."));
  mete(aprox(k * r, 2), T("You still need the root: ", "Falta sacar la raíz: ") + radHTML(1, r) + T(" is not ", " no es ") + r + ".");
  return {enun: T("What is the approximate value of ", "¿Cuál es el valor aproximado de ") + radHTML(k, r) + "?", opciones: [op2[0]].concat(baraja(op2.slice(1))), correcta: op2[0].clave, porClave: pc2,
    bien: radHTML(1, r) + " ≈ " + aprox(Math.sqrt(r), 3) + T(", and ", ", y ") + k + " × " + aprox(Math.sqrt(r), 3) + " ≈ " + aprox(v, 2) + ".",
    mal: T("Multiply the coefficient by the root: ", "Se multiplica el coeficiente por la raíz: ") + k + " × " + aprox(Math.sqrt(r), 3) + " ≈ " + aprox(v, 2) + "."};
}
function genDecima(){
  var n; do { n = aleatorio(2, 150); } while (esCuadrado(n));
  var raiz = Math.sqrt(n), bueno = aprox(raiz, 1), a = Math.floor(raiz);
  return {enun: T("Approximate ", "Aproxime ") + radHTML(1, n) + T(" to the nearest tenth.", " a la décima."),
    solucion: radHTML(1, n) + " ≈ " + aprox(raiz, 3) + T(", which rounds to " + bueno + ".", ", que redondeado a la décima es " + bueno + "."),
    evalua: function(txt){
      var v = leeDecimal(txt);
      if (v === null) return {estado: "invalido", msg: T("Type a decimal number, for example " + (a + 0.5).toFixed(1) + ".", "Escriba un número decimal, por ejemplo " + (a + 0.5).toFixed(1) + ".")};
      if (Math.abs(v - parseFloat(bueno)) < 1e-9) return {estado: "bien", msg: ""};
      if (Math.abs(v - raiz) <= 0.1) return {estado: "mal", msg: T("Close: you are within a tenth, but that is not the correct rounding.", "Casi: está a menos de una décima, pero no es el redondeo correcto.")};
      if (v >= a && v <= a + 1) return {estado: "mal", msg: T("The whole number (" + a + ") is right; fine-tune the tenth by squaring your estimate.", "El entero (" + a + ") está bien; afine la décima elevando al cuadrado su estimación.")};
      return {estado: "mal", msg: T("Trap it first: " + (a * a) + " < " + n + " < " + ((a + 1) * (a + 1)) + ", so the root is between " + a + " and " + (a + 1) + ".", "Primero acorrale: " + (a * a) + " < " + n + " < " + ((a + 1) * (a + 1)) + ", así que la raíz está entre " + a + " y " + (a + 1) + ".")};
    }};
}

/* ============ Start ============ */
["sm-a", "sm-r1", "sm-b", "sm-r2"].forEach(function(id){ $(id).addEventListener("input", pintaSM); });
$("sm-op").addEventListener("change", pintaSM);
pintaSM();
OMR("p1", genSemej);
llenaSP();
$("sp-sel").addEventListener("change", preparaSP);
$("sp-sig").addEventListener("click", function(){ if (SP.visto < SP.pasos.length){ SP.visto++; pintaSP(); } });
$("sp-todo").addEventListener("click", function(){ SP.visto = SP.pasos.length; pintaSP(); });
$("sp-azar").addEventListener("click", azarSP);
preparaSP();
OMR("p2", genSimplCombina);
creaPracticaRad("p3", genEscribeSP);
["mu-k1", "mu-a", "mu-k2", "mu-b"].forEach(function(id){ $(id).addEventListener("input", pintaMU); });
$("mu-azar").addEventListener("click", azarMU);
pintaMU();
OMR("p4", genMultiplicar);
$("ap-n").addEventListener("input", pintaAP);
$("ap-azar").addEventListener("click", azarAP);
pintaAP();
OMR("p5", genEstimar);
creaPracticaLibre("p6", genDecima);
'''

def campo(i, etiqueta, valor):
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="text" inputmode="numeric" class="corto" id="{i}" value="{valor}"></div>'

def practica_pagina():
    from build_n3_lesson_3_1 import rad_input
    n = N
    P = n3
    mods = [
     (t("like", "semejantes"), t("Adding and subtracting like radicals", "Sumar y restar radicales semejantes"),
      f'''      <p>{t("Radicals combine just like like terms in algebra. Just as 3x + 5x = 8x, also 3√2 + 5√2 = 8√2: you add the coefficients and the irrational part <strong>stays the same</strong>.", "Los radicales se combinan igual que los términos semejantes del álgebra. Así como 3x + 5x = 8x, también 3√2 + 5√2 = 8√2: se suman los coeficientes y la parte irracional <strong>se conserva</strong>.")}</p>
{P.formula("3√2 + 5√2 = 8√2 &nbsp; " + t("(like 3x + 5x = 8x)", "(igual que 3x + 5x = 8x)"))}
      <h3>{t("Can they be combined?", "¿Se pueden combinar?")}</h3>
      <p>{t("Build two terms and see whether they combine. The line of decimals checks the result.", "Arme dos términos y observe si se combinan. La línea de decimales comprueba el resultado.")}</p>
      <div class="panel">
        <div class="campos">
          {campo("sm-a", t("First coefficient", "Primer coeficiente"), 3)}
          {campo("sm-r1", t("First radicand", "Primer radicando"), 2)}
          <div class="campo"><label for="sm-op">{t("Operation", "Operación")}</label><select id="sm-op"><option value="+">{t("+ add", "+ sumar")}</option><option value="−">{t("− subtract", "− restar")}</option></select></div>
          {campo("sm-b", t("Second coefficient", "Segundo coeficiente"), 5)}
          {campo("sm-r2", t("Second radicand", "Segundo radicando"), 2)}
        </div>
        <p class="nota">{t("Then try different radicands, for example 2 and 3, or 8 and 2.", "Pruebe después con radicandos distintos, por ejemplo 2 y 3, o 8 y 2.")}</p>
      </div>
{P.aviso("sm-aviso")}
{P.salida("sm-salida")}
{P.atencion(t("Different parts do not combine:", "No se combinan partes distintas:"), t("√2 + √3 is not √5, and it is not 2√5. They have different irrational parts, so they are not like radicals and the sum is left as it is: √2 + √3.", "√2 + √3 no es √5 ni 2√5. Como tienen distinta parte irracional, no son semejantes y la suma se deja indicada: √2 + √3."))}
{B.om("p1", t("Practice: add and subtract", "Practique: sumar y restar"))}'''),
     (t("simplify-first", "simplificar-primero"), t("Alike or not? Simplify first", "¿Semejantes o no? Simplificar primero"),
      f'''      <p>{t("Sometimes two radicals do not look alike, but once you simplify them they are. So before you decide, simplify each radical. Remember that √2 is the same as 1√2.", "A veces dos radicales no parecen semejantes, pero al simplificarlos resulta que sí lo son. Por eso, antes de decidir, conviene simplificar cada radical. Recuerde que √2 es lo mismo que 1√2.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="sp-sel">{t("Expression", "Expresión")}</label><select id="sp-sel"></select></div></div>
        <div class="fila-btn"><button type="button" class="btn" id="sp-sig"></button><button type="button" class="btn-sec" id="sp-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="sp-azar">{t("Another one at random", "Otra al azar")}</button></div>
      </div>
      <div class="fraccion-grande" id="sp-expr"></div>
      <div class="pasos" id="sp-pasos" aria-live="polite"></div>
{B.om("p2", t("Practice: simplify and combine", "Practique: simplifique y combine"))}
{rad_input("p3", t("Write it yourself: the result as a single term", "Escríbalo usted: el resultado en un solo término"))}'''),
     (t("multiply", "multiplicar"), t("Multiplying radicals", "Multiplicar radicales"),
      f'''      <p>{t("To multiply, use the product property in the other direction: the product of the roots is the root of the product. The coefficients outside are multiplied together, and you simplify at the end.", "Para multiplicar se usa la propiedad del producto en la otra dirección: el producto de las raíces es la raíz del producto. Los coeficientes de fuera se multiplican entre sí y al final se simplifica.")}</p>
{P.formula("√a · √b = √(a · b)")}
      <h3>{t("Join and simplify", "Unir y simplificar")}</h3>
      <div class="panel">
        <div class="campos">
          {campo("mu-k1", t("First coefficient", "Coeficiente del primero"), 1)}
          {campo("mu-a", t("First radicand", "Radicando del primero"), 6)}
          {campo("mu-k2", t("Second coefficient", "Coeficiente del segundo"), 1)}
          {campo("mu-b", t("Second radicand", "Radicando del segundo"), 2)}
        </div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="mu-azar">{t("Another example", "Otro ejemplo")}</button></div>
      </div>
{P.aviso("mu-aviso")}
{P.salida("mu-salida")}
      <div class="caja-tip"><strong>{t("A root times itself:", "Una raíz por sí misma:")}</strong> {t("√a · √a = √(a · a) = a. For example, √7 · √7 = 7. This idea comes up often when you distribute: √2 · (√2 + 5) = 2 + 5√2.", "√a · √a = √(a · a) = a. Por ejemplo, √7 · √7 = 7. Esta idea aparece a menudo al distribuir: √2 · (√2 + 5) = 2 + 5√2.")}</div>
{B.om("p4", t("Practice: multiply", "Practique: multiplicar"))}'''),
     (t("approximate", "aproximar"), t("Approximating radicals", "Aproximar radicales"),
      f'''      <p>{t("A radical that is not exact has no decimal that ends, but you can <strong>trap</strong> it between two numbers using perfect squares: since 16 &lt; 20 &lt; 25, √20 is between 4 and 5. Then you narrow it down to the tenth.", "Un radical que no es exacto no tiene un decimal que termine, pero se puede <strong>acorralar</strong> entre dos números usando cuadrados perfectos: como 16 &lt; 20 &lt; 25, √20 está entre 4 y 5. Después se afina a la décima.")}</p>
      <h3>{t("Trap the root", "Acorralar la raíz")}</h3>
      <div class="panel">
        <div class="campos">{campo("ap-n", t("Radicand (2 to 200)", "Radicando (de 2 a 200)"), 20)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="ap-azar">{t("Another number", "Otro número")}</button></div>
      </div>
{P.aviso("ap-aviso")}
      <div id="ap-recta"></div>
{P.salida("ap-salida")}
{B.om("p5", t("Practice: estimate", "Practique: estimar"))}
{B.libre("p6", t("Write it yourself: approximate to the nearest tenth", "Escríbalo usted: aproxime a la décima"), t("Approximation to the nearest tenth", "Aproximación a la décima"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Type a decimal with one digit after the point, for example 4.5. You can use the calculator to check.", "Escriba un decimal con una cifra después del punto, por ejemplo 4.5. Puede usar la calculadora para comprobar.") + '</p>\n        <div class="fila-btn">', 1)}
      <div class="caja-tip"><strong>{t("Estimate to check:", "Estimar para verificar:")}</strong> {t("if a sum of radicals gives 3√3, you can check that 3√3 ≈ 5.20 and compare it with the decimal of the original expression. If they match, the operation is right.", "si una suma de radicales da 3√3, puede comprobar que 3√3 ≈ 5.20 y compararlo con el decimal de la expresión original. Si coinciden, la operación es correcta.")}</div>''')]
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_RAD, scripts=("/math/radicals.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Operaciones con radicales: suma, resta y multiplicación")
