"""Level 3 · Lesson 2.3 · Adding, subtracting, and using scientific notation — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
import n3

B.NIVEL = 3
N = "2-3"
TEMA = ("Scientific notation", "Notación científica")
TIT = ("Adding, subtracting, and using scientific notation", "Suma, resta y aplicaciones en ciencia y tecnología")

def s(c, k):
    return f"{c} × 10<sup>{k}</sup>"

def big(x):
    return f'<p style="text-align:center;font-size:1.3rem;font-weight:700;color:#0d47a1">{x}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 2.2 you multiplied and divided by working the coefficients and the powers of 10 separately: the exponents were added or subtracted. Adding and subtracting work differently. Here the exponents do not change when you calculate; what matters is that they are <strong>equal before you start</strong>. Making the exponents equal is the step that organizes this whole lesson.",
"En la Lección 2.2 multiplicó y dividió operando los coeficientes y las potencias de 10 por separado: los exponentes se sumaban o se restaban. La suma y la resta funcionan de otro modo. Aquí los exponentes no cambian al operar; lo que se exige es que sean <strong>iguales antes de empezar</strong>. Igualar los exponentes es el paso que organiza toda esta lección.")}</p>
<p>{t("You can only add amounts directly when they have the same power of 10, just as you only add things of the same kind: 4 hundreds plus 5 hundreds are 9 hundreds. Add the coefficients and <strong>keep</strong> the power of 10.", "Solo se pueden sumar directamente cantidades con la misma potencia de 10, igual que solo se suman objetos del mismo tipo: 4 cientos más 5 cientos son 9 cientos. Se suman los coeficientes y la potencia de 10 <strong>se conserva</strong>.")}</p>
{big("(a × 10<sup>n</sup>) + (b × 10<sup>n</sup>) = (a + b) × 10<sup>n</sup>")}
{ejemplo(t(f"Example 1: find {s(3, 4)} + {s(2, 4)}", f"Ejemplo 1: calcule {s(3, 4)} + {s(2, 4)}"),
  [("1", t("Same exponent.", "Mismo exponente."), t("Both have 10<sup>4</sup>.", "Las dos tienen 10<sup>4</sup>.")),
   ("2", t("Add the coefficients.", "Se suman los coeficientes."), "3 + 2 = 5."),
   ("3", t("Keep the power.", "Se conserva la potencia."), "10<sup>4</sup>."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s(5, 4)}</strong>")])}
{caja("ojo", t("The power does not change", "La potencia no cambia"), t(f"<p>When you add, the exponents of 10 are not added. {s(3, 4)} + {s(2, 4)} is {s(5, 4)}, never {s(5, 8)}. And if the sum of the coefficients is 10 or more, adjust it as in the last lesson: {s(14, 5)} = {s('1.4', 6)}.</p>",
f"<p>Al sumar, los exponentes de 10 no se suman. {s(3, 4)} + {s(2, 4)} es {s(5, 4)}, nunca {s(5, 8)}. Y si la suma de coeficientes llega a 10 o más, se ajusta como en la lección anterior: {s(14, 5)} = {s('1.4', 6)}.</p>"))}
{practica("p1", t("Practice 1 — Same exponent", "Práctica 1 — Mismo exponente"), t(f"What is {s(4, 2)} + {s(5, 2)}?", f"¿Cuánto es {s(4, 2)} + {s(5, 2)}?"),
          [("a", s(9, 4)), ("b", s(9, 2)), ("c", s(20, 2)), ("d", s(9, 0))])}
{practica("p2", t("Practice 2 — Then adjust", "Práctica 2 — Después ajuste"), t(f"What is {s(7, 5)} + {s(7, 5)}?", f"¿Cuánto es {s(7, 5)} + {s(7, 5)}?"),
          [("a", s("1.4", 6)), ("b", s(14, 5)), ("c", s("1.4", 5)), ("d", s(14, 10))])}
{enlace(n, t("add", "sumar"), t("adding with equal exponents", "sumar con exponentes iguales"), t("Compare with the usual column addition and see why the power does not change.", "Compare con la suma en columnas de siempre y vea por qué la potencia no cambia."))}'''

    s2 = f'''<p>{t("If the powers of 10 do not match, first rewrite one of the amounts so both have the same exponent. It is best to match the <strong>larger</strong> one. Then add the coefficients.", "Si las potencias de 10 no coinciden, primero se reescribe una de las cantidades para que las dos tengan el mismo exponente. Conviene igualar al <strong>mayor</strong>. Después se suman los coeficientes.")}</p>
{ejemplo(t(f"Example 2: find {s(4, 5)} + {s(3, 4)}", f"Ejemplo 2: calcule {s(4, 5)} + {s(3, 4)}"),
  [("1", t("Match.", "Igualar."), t(f"The exponents are 5 and 4. Raise the smaller one: {s(3, 4)} = {s('0.3', 5)}.", f"Los exponentes son 5 y 4. Se sube el menor: {s(3, 4)} = {s('0.3', 5)}.")),
   ("2", t("Same power.", "Misma potencia."), f"{s(4, 5)} + {s('0.3', 5)}."),
   ("3", t("Add.", "Sumar."), "4 + 0.3 = 4.3."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s('4.3', 5)}</strong>")])}
{caja("tip", t("Why match the larger exponent", "Por qué igualar al mayor"), t("<p>When you raise the smaller exponent to the larger one, the term you rewrite gets a coefficient less than 1 (like 0.3), but the sum almost always lands right in valid form, with no extra adjustment.</p>", "<p>Al subir el exponente menor hasta el mayor, el término que se reescribe queda con un coeficiente menor que 1 (como 0.3), pero la suma casi siempre cae directamente en la forma válida, sin ajuste adicional.</p>"))}
{practica("p3", t("Practice 3 — Match, then add", "Práctica 3 — Iguale y sume"), t(f"What is {s(5, 4)} + {s(2, 3)}?", f"¿Cuánto es {s(5, 4)} + {s(2, 3)}?"),
          [("a", s(7, 7)), ("b", s("5.2", 3)), ("c", s("5.2", 4)), ("d", s(7, 4))])}
{enlace(n, t("match", "igualar"), t("making the exponents equal", "igualar los exponentes"), t("Try both ways of matching and write the rewritten coefficient yourself.", "Pruebe las dos maneras de igualar y escriba usted el coeficiente reescrito."))}'''

    s3 = f'''<p>{t("Subtraction follows exactly the same idea: if the exponents are equal, subtract the coefficients; if they are different, match them first.", "La resta sigue exactamente la misma idea: si los exponentes son iguales, se restan los coeficientes; si son distintos, se igualan primero.")}</p>
{big("(a × 10<sup>n</sup>) − (b × 10<sup>n</sup>) = (a − b) × 10<sup>n</sup>")}
{ejemplo(t(f"Example 3: find {s(9, 6)} − {s(4, 6)}", f"Ejemplo 3: calcule {s(9, 6)} − {s(4, 6)}"),
  [("1", t("Same exponent.", "Mismo exponente."), "10<sup>6</sup>."),
   ("2", t("Subtract the coefficients.", "Se restan los coeficientes."), "9 − 4 = 5."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s(5, 6)}</strong>")])}
{ejemplo(t(f"Example 4: find {s(7, 4)} − {s(2, 3)}", f"Ejemplo 4: calcule {s(7, 4)} − {s(2, 3)}"),
  [("1", t("Match.", "Igualar."), f"{s(2, 3)} = {s('0.2', 4)}."),
   ("2", t("Same power.", "Misma potencia."), f"{s(7, 4)} − {s('0.2', 4)}."),
   ("3", t("Subtract.", "Restar."), "7 − 0.2 = 6.8."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s('6.8', 4)}</strong>")])}
{caja("ojo", t("When the amounts are close", "Cuando las cantidades se parecen"), t(f"<p>If the two amounts are close, the difference can come out less than 1 and needs a new adjustment: {s('1.2', 5)} − {s(9, 4)} = {s('1.2', 5)} − {s('0.9', 5)} = {s('0.3', 5)} = {s(3, 4)}. And two equal amounts give 0.</p>",
f"<p>Si las dos cantidades se parecen, la diferencia puede quedar menor que 1 y obliga a reajustar: {s('1.2', 5)} − {s(9, 4)} = {s('1.2', 5)} − {s('0.9', 5)} = {s('0.3', 5)} = {s(3, 4)}. Y dos cantidades iguales dan 0.</p>"))}
{practica("p4", t("Practice 4 — Subtract", "Práctica 4 — Reste"), t(f"What is {s(6, 5)} − {s(4, 4)}?", f"¿Cuánto es {s(6, 5)} − {s(4, 4)}?"),
          [("a", s(2, 1)), ("b", s("5.6", 4)), ("c", s("5.6", 5)), ("d", s(2, 5))])}
{practica("p5", t("Practice 5 — Equal amounts", "Práctica 5 — Cantidades iguales"), t(f"What is {s(9, 6)} − {s(9, 6)}?", f"¿Cuánto es {s(9, 6)} − {s(9, 6)}?"),
          [("a", "0"), ("b", s(9, 6)), ("c", s(1, 6)), ("d", s(9, 0))])}
{enlace(n, t("subtract", "restar"), t("subtracting in scientific notation", "restar en notación científica"), t("Compare the usual column subtraction with subtraction in scientific notation.", "Compare la resta en columnas con la resta en notación científica."))}'''

    filas = [[t("“in all,” “are added,” “together”", "«en total», «se añaden», «juntos»"), t("an addition", "una suma")],
             [t("“is left,” “how much more,” “difference”", "«queda», «cuánto más», «diferencia»"), t("a subtraction", "una resta")],
             [t("“each hour for…,” “for each one, how many in…”", "«cada hora durante…», «por cada uno, cuántos en…»"), t("a multiplication", "una multiplicación")],
             [t("“how many fit,” “per,” “share”", "«cuántos caben», «por cada», «repartir»"), t("a division", "una división")]]
    s4 = f'''<p>{t("Scientific notation is the natural language of science. These examples use the four operations in real settings: space, cells, and technology.", "La notación científica es el lenguaje natural de la ciencia. Estos ejemplos usan las cuatro operaciones en contextos reales: el espacio, las células y la tecnología.")}</p>
{tabla(t("Hints for choosing the operation", "Pistas para elegir la operación"), t("Hints for choosing the operation from the words of the problem", "Pistas para elegir la operación según las palabras del problema"), [t("If the question says…", "Si la pregunta dice…"), t("It is usually", "Suele ser")], filas)}
{ejemplo(t(f"Example 5 · Space: a probe travels {s(4, 4)} km each hour. How far does it go in {s(6, 2)} hours?", f"Ejemplo 5 · Espacio: una sonda recorre {s(4, 4)} km cada hora. ¿Qué distancia recorre en {s(6, 2)} horas?"),
  [("1", t("Operation.", "Operación."), t(f"A multiplication: ({s(4, 4)})({s(6, 2)}).", f"Una multiplicación: ({s(4, 4)})({s(6, 2)}).")),
   ("2", t("Calculate.", "Calcular."), t(f"4 × 6 = 24; 4 + 2 = 6. Partial answer: {s(24, 6)}.", f"4 × 6 = 24; 4 + 2 = 6. Resultado parcial: {s(24, 6)}.")),
   ("3", t("Adjust.", "Ajustar."), f"{s(24, 6)} = {s('2.4', 7)}."),
   ("✓", t("Answer.", "Respuesta."), f"<strong>{s('2.4', 7)} km</strong>")])}
{ejemplo(t(f"Example 6 · Cells: a blood sample has {s(5, 6)} red blood cells, and {s(3, 5)} more are added. How many are there in all?", f"Ejemplo 6 · Células: una muestra tiene {s(5, 6)} glóbulos rojos y se le añaden {s(3, 5)} más. ¿Cuántos hay en total?"),
  [("1", t("Operation and match.", "Operación e igualar."), t(f"An addition with different exponents: {s(3, 5)} = {s('0.3', 6)}.", f"Una suma con exponentes distintos: {s(3, 5)} = {s('0.3', 6)}.")),
   ("2", t("Add.", "Sumar."), "5 + 0.3 = 5.3."),
   ("✓", t("Answer.", "Respuesta."), t(f"<strong>{s('5.3', 6)}</strong> red blood cells", f"<strong>{s('5.3', 6)}</strong> glóbulos rojos"))])}
{ejemplo(t(f"Example 7 · Technology: a drive holds {s(8, 12)} bytes, and each file takes up {s(2, 6)} bytes. How many files fit?", f"Ejemplo 7 · Tecnología: un disco guarda {s(8, 12)} bytes y cada archivo ocupa {s(2, 6)} bytes. ¿Cuántos archivos caben?"),
  [("1", t("Operation.", "Operación."), t(f"A division: ({s(8, 12)}) ÷ ({s(2, 6)}).", f"Una división: ({s(8, 12)}) ÷ ({s(2, 6)}).")),
   ("2", t("Calculate.", "Calcular."), "8 ÷ 2 = 4; 12 − 6 = 6."),
   ("✓", t("Answer.", "Respuesta."), t(f"<strong>{s(4, 6)}</strong> files", f"<strong>{s(4, 6)}</strong> archivos"))])}
{calc(t("Check on the calculator", "Compruebe en la calculadora"), t(f"<p>Type the amounts with the {T('×10<sup>n</sup>')} key and keep the order of operations: {T('5')} {T('×10<sup>n</sup>')} {T('6')} {T('+')} {T('3')} {T('×10<sup>n</sup>')} {T('5')} {T('enter')} shows 5300000, that is, {s('5.3', 6)}. The calculator matches the exponents on its own, but you still have to read the answer in valid scientific notation. Use {T('(−)')} for a negative exponent, not the subtraction key.</p>",
f"<p>Escriba las cantidades con la tecla {T('×10<sup>n</sup>')} y respete el orden de las operaciones: {T('5')} {T('×10<sup>n</sup>')} {T('6')} {T('+')} {T('3')} {T('×10<sup>n</sup>')} {T('5')} {T('enter')} muestra 5300000, es decir, {s('5.3', 6)}. La calculadora iguala los exponentes por su cuenta, pero el resultado hay que leerlo en notación científica válida. Use {T('(−)')} para un exponente negativo, no la tecla de resta.</p>"))}
{practica("p6", t("Practice 6 — Choose the operation", "Práctica 6 — Elija la operación"), t(f"A probe travels {s(3, 4)} km each hour for 5 hours. How far does it go in all?", f"Una sonda recorre {s(3, 4)} km cada hora durante 5 horas. ¿Qué distancia recorre en total?"),
          [("a", s("1.5", 5) + " km"), ("b", s("1.5", 4) + " km"), ("c", s("3.5", 5) + " km"), ("d", s(8, 4) + " km")])}
{enlace(n, t("applications", "aplicaciones"), t("science and technology applications", "aplicaciones en ciencia y tecnología"), t("Mixed problems with the four operations: choose the operation, then solve.", "Problemas mezclados con las cuatro operaciones: elija la operación y resuelva."))}'''

    secciones = [("s-" + t("add", "sumar"), t("Adding: match the exponents first", "Sumar: primero igualar los exponentes"), s1),
                 ("s-" + t("match", "igualar"), t("When the exponents are different", "Cuando los exponentes son distintos"), s2),
                 ("s-" + t("subtract", "restar"), t("Subtracting in scientific notation", "Restar en notación científica"), s3),
                 ("s-" + t("applications", "aplicaciones"), t("Science and technology applications", "Aplicaciones en ciencia y tecnología"), s4)]

    lesson = {"next": t("Topic 3", "el Tema 3"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("When you add, the exponents are not added: the power 10<sup>2</sup> stays.", "Al sumar, los exponentes no se suman: la potencia 10<sup>2</sup> se conserva."), "c": t("You multiplied the coefficients. Add them: 4 + 5.", "Multiplicó los coeficientes. Se suman: 4 + 5."), "d": t("The power of 10 does not disappear: it stays 10<sup>2</sup>.", "La potencia de 10 no desaparece: se conserva 10<sup>2</sup>.")},
             "right": t("4 + 5 = 9, and 10<sup>2</sup> stays.", "4 + 5 = 9, y 10<sup>2</sup> se conserva."), "solution": t(f"The exponents are equal: add 4 + 5 = 9 and keep 10<sup>2</sup>. So {s(9, 2)}.", f"Los exponentes son iguales: 4 + 5 = 9 y se conserva 10<sup>2</sup>. Así que {s(9, 2)}.")},
      "p2": {"ok": "a", "hints": {"b": t("The value is right, but 14 is not from 1 to 10: adjust it.", "El valor es correcto, pero 14 no está entre 1 y 10: ajústelo."), "c": t("When 14 becomes 1.4, the exponent must go up 1.", "Al pasar de 14 a 1.4, el exponente tiene que subir 1."), "d": t("The exponents are not added when you add.", "Al sumar, los exponentes no se suman.")},
             "right": t(f"7 + 7 = 14; {s(14, 5)} = {s('1.4', 6)}.", f"7 + 7 = 14; {s(14, 5)} = {s('1.4', 6)}."), "solution": t(f"7 + 7 = 14, so {s(14, 5)}. Adjust: 14 = {s('1.4', 1)}, so {s('1.4', 6)}.", f"7 + 7 = 14, así que {s(14, 5)}. Se ajusta: 14 = {s('1.4', 1)}, así que {s('1.4', 6)}.")},
      "p3": {"ok": "c", "hints": {"a": t("You added the exponents. Match them, then add the coefficients.", "Sumó los exponentes. Iguálelos y después sume los coeficientes."), "b": t("Match to the larger exponent, 4: the answer keeps 10<sup>4</sup>.", "Iguale al exponente mayor, 4: el resultado conserva 10<sup>4</sup>."), "d": t("You added 5 + 2 without matching. First, " + s(2, 3) + " = " + s("0.2", 4) + ".", "Sumó 5 + 2 sin igualar. Primero, " + s(2, 3) + " = " + s("0.2", 4) + ".")},
             "right": t(f"{s(2, 3)} = {s('0.2', 4)}; 5 + 0.2 = 5.2.", f"{s(2, 3)} = {s('0.2', 4)}; 5 + 0.2 = 5.2."), "solution": t(f"Match: {s(2, 3)} = {s('0.2', 4)}. Add: 5 + 0.2 = 5.2. So {s('5.2', 4)}.", f"Igualar: {s(2, 3)} = {s('0.2', 4)}. Sumar: 5 + 0.2 = 5.2. Así que {s('5.2', 4)}.")},
      "p4": {"ok": "c", "hints": {"a": t("You subtracted the exponents. Match them, then subtract the coefficients.", "Restó los exponentes. Iguálelos y después reste los coeficientes."), "b": t("Match to the larger exponent, 5: the answer keeps 10<sup>5</sup>.", "Iguale al exponente mayor, 5: el resultado conserva 10<sup>5</sup>."), "d": t("You subtracted 6 − 4 without matching. First, " + s(4, 4) + " = " + s("0.4", 5) + ".", "Restó 6 − 4 sin igualar. Primero, " + s(4, 4) + " = " + s("0.4", 5) + ".")},
             "right": t(f"{s(4, 4)} = {s('0.4', 5)}; 6 − 0.4 = 5.6.", f"{s(4, 4)} = {s('0.4', 5)}; 6 − 0.4 = 5.6."), "solution": t(f"Match: {s(4, 4)} = {s('0.4', 5)}. Subtract: 6 − 0.4 = 5.6. So {s('5.6', 5)}.", f"Igualar: {s(4, 4)} = {s('0.4', 5)}. Restar: 6 − 0.4 = 5.6. Así que {s('5.6', 5)}.")},
      "p5": {"ok": "a", "hints": {"b": t("Subtract the coefficients: 9 − 9.", "Reste los coeficientes: 9 − 9."), "c": t("9 − 9 is 0, not 1.", "9 − 9 es 0, no 1."), "d": t("A number minus itself is 0.", "Un número menos sí mismo da 0.")},
             "right": t("Two equal amounts give a difference of 0.", "Dos cantidades iguales dan diferencia 0."), "solution": t("9 − 9 = 0, so the difference is 0.", "9 − 9 = 0, así que la diferencia es 0.")},
      "p6": {"ok": "a", "hints": {"b": t("Check the exponent: 3 × 5 = 15, and 15 × 10<sup>4</sup> = 1.5 × 10<sup>5</sup>.", "Revise el exponente: 3 × 5 = 15, y 15 × 10<sup>4</sup> = 1.5 × 10<sup>5</sup>."), "c": t("You added 3 + 5. The same distance repeats each hour: multiply.", "Sumó 3 + 5. La misma distancia se repite cada hora: se multiplica."), "d": t("You added. The same distance repeats each hour: multiply.", "Sumó. La misma distancia se repite cada hora: se multiplica.")},
             "right": t(f"3 × 5 = 15; {s(15, 4)} = {s('1.5', 5)}.", f"3 × 5 = 15; {s(15, 4)} = {s('1.5', 5)}."), "solution": t(f"Multiply: ({s(3, 4)}) × 5 = {s(15, 4)} = {s('1.5', 5)} km.", f"Se multiplica: ({s(3, 4)}) × 5 = {s(15, 4)} = {s('1.5', 5)} km.")}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("When you add, the exponents are not added.", "Al sumar, los exponentes no se suman."), "c": t("You multiplied the coefficients. Add them.", "Multiplicó los coeficientes. Se suman."), "d": t("You multiplied the exponents. The power stays.", "Multiplicó los exponentes. La potencia se conserva.")}, "solution": t(f"5 + 3 = 8; keep 10<sup>3</sup>: {s(8, 3)}.", f"5 + 3 = 8; se conserva 10<sup>3</sup>: {s(8, 3)}.")},
      "B": {"ok": "d", "hints": {"a": t("The exponents are not added when you add.", "Al sumar, los exponentes no se suman."), "b": t("The exponents are not multiplied.", "Los exponentes no se multiplican."), "c": t("You multiplied the coefficients. Add them.", "Multiplicó los coeficientes. Se suman.")}, "solution": t(f"2.5 + 1.5 = 4; keep 10<sup>5</sup>: {s(4, 5)}.", f"2.5 + 1.5 = 4; se conserva 10<sup>5</sup>: {s(4, 5)}.")},
      "C": {"ok": "b", "hints": {"a": t("You added the exponents. Match them first.", "Sumó los exponentes. Primero iguálelos."), "c": t("Match to the larger exponent, 4.", "Iguale al exponente mayor, 4."), "d": t("You added 6 + 3 without matching.", "Sumó 6 + 3 sin igualar.")}, "solution": t(f"{s(3, 3)} = {s('0.3', 4)}; 6 + 0.3 = 6.3: {s('6.3', 4)}.", f"{s(3, 3)} = {s('0.3', 4)}; 6 + 0.3 = 6.3: {s('6.3', 4)}.")},
      "D": {"ok": "c", "hints": {"a": t("The power does not disappear: it stays 10<sup>6</sup>.", "La potencia no desaparece: se conserva 10<sup>6</sup>."), "b": t("You added. Subtract: 9 − 4.", "Sumó. Se resta: 9 − 4."), "d": t("You added the exponents. The power stays.", "Sumó los exponentes. La potencia se conserva.")}, "solution": t(f"9 − 4 = 5; keep 10<sup>6</sup>: {s(5, 6)}.", f"9 − 4 = 5; se conserva 10<sup>6</sup>: {s(5, 6)}.")},
      "E": {"ok": "c", "hints": {"a": t("You subtracted the exponents. Match them first.", "Restó los exponentes. Primero iguálelos."), "b": t("Match to the larger exponent, 4.", "Iguale al exponente mayor, 4."), "d": t("You subtracted 7 − 2 without matching.", "Restó 7 − 2 sin igualar.")}, "solution": t(f"{s(2, 3)} = {s('0.2', 4)}; 7 − 0.2 = 6.8: {s('6.8', 4)}.", f"{s(2, 3)} = {s('0.2', 4)}; 7 − 0.2 = 6.8: {s('6.8', 4)}.")},
      "F": {"ok": "d", "hints": {"a": t("You multiplied the exponent. The cells are in a row: multiply the length by 4.", "Multiplicó el exponente. Las células están en fila: se multiplica la longitud por 4."), "b": t("You added 2 + 4. Multiply: 2 × 4.", "Sumó 2 + 4. Se multiplica: 2 × 4."), "c": t("Multiplying by 4 does not change the exponent: 2 × 4 = 8, still 10<sup>−5</sup>.", "Multiplicar por 4 no cambia el exponente: 2 × 4 = 8, sigue 10<sup>−5</sup>.")}, "solution": t(f"({s(2, '−5')}) × 4 = {s(8, '−5')} m.", f"({s(2, '−5')}) × 4 = {s(8, '−5')} m.")},
      "G": {"ok": "a", "hints": {"b": t("0.8 is less than 1.", "0.8 es menor que 1."), "c": t("When you add, the exponents are not added.", "Al sumar, los exponentes no se suman."), "d": t("4 + 4 is 8, not 16.", "4 + 4 es 8, no 16.")}, "solution": t("8 is from 1 to 10, so it is already valid.", "8 está entre 1 y 10, así que ya es válida.")},
      "H": {"ok": "d", "hints": {"a": t("Exponents are added only when you multiply.", "Los exponentes se suman solo al multiplicar."), "b": t("The coefficients are added, not multiplied.", "Los coeficientes se suman, no se multiplican."), "c": t("You add, not subtract.", "Se suma, no se resta.")}, "solution": t("The exponents (6 and 4) are different: match them first.", "Los exponentes (6 y 4) son distintos: primero hay que igualarlos.")}
     }}

    quiz = [
     ("A", f"{s(5, 3)} + {s(3, 3)} =", [("a", s(8, 3)), ("b", s(8, 6)), ("c", s(15, 3)), ("d", s(8, 9))]),
     ("B", f"{s('2.5', 5)} + {s('1.5', 5)} =", [("a", s(4, 10)), ("b", s(4, 25)), ("c", s("3.75", 5)), ("d", s(4, 5))]),
     ("C", f"{s(6, 4)} + {s(3, 3)} =", [("a", s(9, 7)), ("b", s("6.3", 4)), ("c", s("6.3", 3)), ("d", s(9, 4))]),
     ("D", f"{s(9, 6)} − {s(4, 6)} =", [("a", s(5, 0)), ("b", s(13, 6)), ("c", s(5, 6)), ("d", s(5, 12))]),
     ("E", f"{s(7, 4)} − {s(2, 3)} =", [("a", s(5, 1)), ("b", s("6.8", 3)), ("c", s("6.8", 4)), ("d", s(5, 4))]),
     ("F", t(f"A cell is {s(2, '−5')} m long. How long are 4 cells in a row?", f"Una célula mide {s(2, '−5')} m. ¿Cuánto miden 4 células en fila?"), [("a", s(8, "−20") + " m"), ("b", s(6, "−5") + " m"), ("c", s(8, "−4") + " m"), ("d", s(8, "−5") + " m")]),
     ("G", t(f"Adding {s(4, 3)} + {s(4, 3)} gives {s(8, 3)}. Is it valid scientific notation?", f"Al sumar {s(4, 3)} + {s(4, 3)} se obtiene {s(8, 3)}. ¿Es notación científica válida?"), [("a", t("Yes, because 1 ≤ 8 &lt; 10", "Sí, porque 1 ≤ 8 &lt; 10")), ("b", t(f"No, it should be {s('0.8', 4)}", f"No, debe ser {s('0.8', 4)}")), ("c", t(f"No, it should be {s(8, 6)}", f"No, debe ser {s(8, 6)}")), ("d", t(f"No, it should be {s(16, 3)}", f"No, debe ser {s(16, 3)}"))]),
     ("H", t(f"What must you do first to add {s(3, 6)} + {s(5, 4)}?", f"¿Qué se debe hacer primero para sumar {s(3, 6)} + {s(5, 4)}?"), [("a", t("Add the exponents", "Sumar los exponentes")), ("b", t("Multiply the coefficients", "Multiplicar los coeficientes")), ("c", t("Subtract the coefficients", "Restar los coeficientes")), ("d", t("Make the exponents of 10 equal", "Igualar los exponentes de 10"))])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("To add or subtract, first make the powers of 10 equal. Then the four operations in science and technology.", "Para sumar o restar, primero se igualan las potencias de 10. Después, las cuatro operaciones en ciencia y tecnología."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Add and subtract</strong> numbers in scientific notation with the same exponent.", "<strong>Sumar y restar</strong> números en notación científica con el mismo exponente."),
         t("<strong>Make the exponents equal</strong> before adding or subtracting.", "<strong>Igualar los exponentes</strong> antes de sumar o restar."),
         t("<strong>Give</strong> every answer in valid scientific notation.", "<strong>Presentar</strong> cada resultado en notación científica válida."),
         t("<strong>Choose</strong> the operation in science and technology problems and solve them with units.", "<strong>Elegir</strong> la operación en problemas de ciencia y tecnología y resolverlos con unidades.")],
        secciones,
        (t("Do three additions and three subtractions in scientific notation (at least two of each with different exponents), and four mixed problems (space, cells, or technology) that use the four operations. Once the exponents are equal, adding in scientific notation is just adding decimals, and that is where careless points are lost.",
           "Haga tres sumas y tres restas en notación científica (al menos dos de cada una con exponentes distintos) y cuatro problemas mezclados (espacio, células o tecnología) que usen las cuatro operaciones. Una vez igualados los exponentes, sumar en notación científica es sumar decimales, y ahí es donde se pierden puntos por descuido."),
         t("Look up two large amounts of the same kind in the news (for example, the populations of two states) and write them in scientific notation. Find how many more people one has than the other, and the total, in scientific notation.",
           "Busque en las noticias dos cantidades grandes del mismo tipo (por ejemplo, la población de dos estados) y escríbalas en notación científica. Calcule cuántas personas más tiene uno que el otro, y el total, en notación científica.")),
        quiz,
        t("Self-check checklist for adding, subtracting, and using scientific notation", "Lista de autoevaluación de la suma, la resta y las aplicaciones de la notación científica"),
        t("Self-check checklist: skills for adding, subtracting, and using scientific notation", "Lista de autoevaluación: destrezas de la suma, la resta y las aplicaciones de la notación científica"),
        [(t("Making the exponents equal", "Igualar los exponentes"), t("I match the exponents before I calculate, usually to the larger one.", "Igualo los exponentes antes de operar, por lo general al mayor."), t("I match them, with a few mistakes.", "Los igualo, con algunos errores."), t("I add or subtract without matching first.", "Sumo o resto sin igualar primero.")),
         (t("Working with the coefficients", "Operar los coeficientes"), t("I add or subtract them correctly and keep the right power of 10.", "Los sumo o resto bien y conservo la potencia de 10 correcta."), t("I make some arithmetic mistakes.", "Cometo algunos errores de aritmética."), t("I also add or subtract the exponents.", "También sumo o resto los exponentes.")),
         (t("Valid scientific notation", "Notación científica válida"), t("My answer is always valid, and I check it on the calculator.", "Mi resultado siempre es válido, y lo compruebo en la calculadora."), t("I adjust the answer only sometimes.", "Ajusto el resultado solo a veces."), t("I leave the answer out of valid form.", "Dejo el resultado fuera de la forma válida.")),
         (t("Word problems", "Problemas de contexto"), t("I choose the operation, solve, and give the answer with units.", "Elijo la operación, resuelvo y doy el resultado con unidades."), t("I choose the operation, but make mistakes solving.", "Elijo la operación, pero me equivoco al resolver."), t("I do not know which operation the problem asks for.", "No sé qué operación pide el problema."))],
        t("<p>This lesson closes Topic 2. You can now do the four operations in scientific notation: to multiply and divide, work the coefficients and add or subtract the exponents; to add and subtract, first <strong>make the exponents equal</strong> and then work the coefficients. In every case, the answer is given in valid scientific notation and can be checked on the calculator.</p>\n<p>Topic 3 opens with <strong>Lesson 3.1 · Simplifying radicals with perfect-square factors</strong>. After powers and scientific notation, the natural next step is the reverse of squaring: roots and radicals. There you will complete the picture of the real number system.</p>",
          "<p>Con esta lección se cierra el Tema 2. Ya domina las cuatro operaciones en notación científica: para multiplicar y dividir se operan los coeficientes y se suman o restan los exponentes; para sumar y restar, primero hay que <strong>igualar los exponentes</strong> y luego operar los coeficientes. En todos los casos, el resultado se presenta en notación científica válida y se puede comprobar con la calculadora.</p>\n<p>El Tema 3 abre con la <strong>Lección 3.1 · Simplificar radicales: factorización en cuadrados perfectos</strong>. Tras las potencias y la notación científica, el paso natural es el camino inverso de elevar al cuadrado: las raíces y los radicales. Allí se completará el panorama del sistema de los números reales.</p>"),
        ("3-1", ("", t("Lesson 3.1 · Simplifying radicals with perfect-square factors", "Lección 3.1 · Simplificar radicales: factorización en cuadrados perfectos"))),
        [(t("make the exponents equal", "igualar los exponentes"), t("Rewrite one amount so both have the same power of 10 before you add or subtract.", "Reescribir una cantidad para que las dos tengan la misma potencia de 10 antes de sumar o restar.")),
         (t("common power", "potencia común"), t("The power of 10 that two amounts share. It stays the same in the answer when you add or subtract.", "La potencia de 10 que comparten dos cantidades. Se conserva en el resultado al sumar o restar.")),
         (t("difference", "diferencia"), t("The answer to a subtraction.", "El resultado de una resta.")),
         (t("unit", "unidad"), t("What an amount is measured in: kilometers, bytes, cells. It goes with the answer.", "En qué se mide una cantidad: kilómetros, bytes, células. Acompaña al resultado."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var NB = " ";
function columnasHTML(A, Bn, so, R){
  var f = [A, Bn, R].map(function(x){ return conComas(x); }), dec = f.map(function(x){ var p = x.indexOf("."); return p < 0 ? 0 : x.length - p - 1; }), md = Math.max.apply(null, dec);
  f = f.map(function(x, i){ return md === 0 ? x : x + (dec[i] === 0 ? NB : "") + NB.repeat(md - dec[i]); });
  return '<div class="centro"><div class="columnas" aria-hidden="true">' + NB + NB + f[0] + "<br>" + so + NB + f[1] + '<br><span class="raya" style="display:inline-block;min-width:100%;">' + f[2] + "</span></div></div>" +
    '<p class="sr-only">' + T("In columns: ", "En columnas: ") + conComas(A) + (so === "+" ? T(" plus ", " más ") : T(" minus ", " menos ")) + conComas(Bn) + T(" equals ", " es igual a ") + conComas(R) + ".</p>";
}
function leeCoef(id){ var x = $(id).value.trim(); return esValida(x) ? plano(leeNumero(x)) : null; }
function leeExp(id, min, max){ var x = $(id).value.trim().replace(/[−–]/g, "-"); if (!/^-?\d+$/.test(x)) return null; var k = parseInt(x, 10); return (k < min || k > max) ? null : k; }

/* ============ MODULE 1 · adding with equal exponents ============ */
function actualizaSE(){
  var a = leeCoef("se-a"), b = leeCoef("se-b"), n = leeExp("se-n", 0, 6), av = $("se-aviso");
  if (a === null || b === null || n === null){ av.className = "caja-aviso visible"; av.textContent = T("The coefficients must be from 1 to 10 (for example, 4 or 7.5) and the exponent must be a whole number from 0 to 6.", "Los coeficientes deben estar entre 1 y 10 (por ejemplo, 4 o 7.5) y el exponente debe ser un número entero de 0 a 6."); $("se-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var A = sci(a, n), Bn = sci(b, n), R = suma(A, Bn), sc = plano(suma(leeNumero(a), leeNumero(b)));
  var h = columnasHTML(A, Bn, "+", R);
  h += '<div class="linea">' + T("In scientific notation: ", "En notación científica: ") + sciHTML(a, n) + " + " + sciHTML(b, n) + " = " + sciHTML(sc, n) + (esValida(sc) ? "" : " = " + numSciHTML(R) + ' <span class="nota">' + T("(the coefficient " + sc + " was adjusted)", "(el coeficiente " + sc + " se ajustó)") + "</span>") + "</div>";
  h += '<div class="linea veredicto">✓ ' + conComas(R) + " = " + numSciHTML(R) + T(". The power 10<sup>" + n + "</sup> stayed the same.", ". La potencia 10<sup>" + n + "</sup> se conservó.") + "</div>";
  if (n === 0) h += '<div class="linea nota">' + T("With exponent 0 the mistake of adding exponents does not show, because 0 + 0 = 0. Try another exponent.", "Con exponente 0 el error de sumar exponentes no se nota, porque 0 + 0 = 0. Pruebe con otro exponente.") + "</div>";
  else h += '<div class="linea">' + T("If the exponents were added too: ", "Si se sumaran también los exponentes: ") + sciHTML(sc, 2 * n) + " = " + conComas(sci(sc, 2 * n)) + T(". It <strong>does not match</strong> the real sum, ", ". <strong>No coincide</strong> con la suma real, ") + conComas(R) + ".</div>";
  $("se-salida").innerHTML = h;
}
var SE_COLA = [["7", "7", 5], ["3", "2", 4]];
function azarSE(){ var e = SE_COLA.length ? SE_COLA.shift() : [coefAzar(aleatorio(1, 2)), coefAzar(aleatorio(1, 2)), aleatorio(1, 6)]; $("se-a").value = e[0]; $("se-b").value = e[1]; $("se-n").value = e[2]; actualizaSE(); }
function genSumar(){
  var a = coefAzar(aleatorio(1, 2)), b = coefAzar(aleatorio(1, 2)), n = aleatorio(-5, 9), sc = suma(leeNumero(a), leeNumero(b)), R = porPot(sc, n), rs = aSci(R), o = [opNum(R)], pc = {};
  var x1 = op(rs.c, 2 * n + (rs.e - n)); o.push(x1); pc[x1.clave] = T("When you add, the exponents are not added: the power of 10 stays.", "Al sumar, los exponentes no se suman: la potencia de 10 se conserva.");
  var x2 = opNum(porPot(mul(leeNumero(a), leeNumero(b)), n)); o.push(x2); pc[x2.clave] = T("The coefficients are added, not multiplied.", "Los coeficientes se suman, no se multiplican.");
  if (!esValida(plano(sc))){
    var x3 = op(plano(sc), n); o.push(x3); pc[x3.clave] = T("The value is right, but " + plano(sc) + " is not from 1 to 10: it still needs adjusting.", "El valor es correcto, pero " + plano(sc) + " no está entre 1 y 10: falta ajustar.");
    var x4 = op(rs.c, n); o.push(x4); pc[x4.clave] = T("When you adjust the coefficient, the exponent must go up 1.", "Al ajustar el coeficiente, el exponente tiene que subir 1.");
  }
  o.push(op(rs.c, rs.e + 1));
  var expl = T("Add the coefficients, ", "Se suman los coeficientes, ") + a + " + " + b + " = " + plano(sc) + T(", and keep the power.", ", y la potencia se conserva.") + (esValida(plano(sc)) ? "" : T(" Since " + plano(sc) + " is 10 or more, it is adjusted to ", " Como " + plano(sc) + " es 10 o más, se ajusta a ") + numSciHTML(R) + ".");
  return {enun: T("Find ", "Calcule ") + sciHTML(a, n) + " + " + sciHTML(b, n) + ".", opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc, bien: expl, mal: expl + " " + T("The answer is ", "La respuesta es ") + numSciHTML(R) + "."};
}

/* ============ MODULE 2 · making the exponents equal ============ */
var IG = {a: "", M: 0, b: "", n: 0, op: "+", cola: [["4", 5, "3", 4, "+"], ["7", 4, "2", 3, "−"]]};
function cargaIG(e){
  IG.a = e[0]; IG.M = e[1]; IG.b = e[2]; IG.n = e[3]; IG.op = e[4];
  $("ig-expr").innerHTML = '<span class="grande">' + sciHTML(IG.a, IG.M) + " " + IG.op + " " + sciHTML(IG.b, IG.n) + "</span><br>" + T("The exponents are different: " + expTexto(IG.M) + " and " + expTexto(IG.n) + ". Choose how to make them equal.", "Los exponentes son distintos: " + expTexto(IG.M) + " y " + expTexto(IG.n) + ". Elija cómo igualarlos.");
  $("ig-pasos").innerHTML = "";
}
function azarIG(){ var M = aleatorio(-4, 9), g = aleatorio(1, 2); return [coefAzar(aleatorio(1, 2)), M, coefAzar(aleatorio(1, 2)), M - g, Math.random() < 0.6 ? "+" : "−"]; }
function caminoIG(subir){
  var A = sci(IG.a, IG.M), Bn = sci(IG.b, IG.n), g = IG.M - IG.n, obj = subir ? IG.M : IG.n, R = IG.op === "+" ? suma(A, Bn) : resta(A, Bn);
  var ca = coefCon(A, obj), cb = coefCon(Bn, obj), rc = coefCon(R, obj), p = [];
  if (subir) p.push(T("Rewrite the term with the smaller exponent: ", "Se reescribe el término con el exponente menor: ") + sciHTML(IG.b, IG.n) + " = " + sciHTML(cb, obj) + T(". The exponent goes up " + g + ", so the point of the coefficient moves " + g + lugares(g) + " to the left.", ". El exponente sube " + g + ", así que el punto del coeficiente se mueve " + g + lugares(g) + " a la izquierda."));
  else p.push(T("Rewrite the term with the larger exponent: ", "Se reescribe el término con el exponente mayor: ") + sciHTML(IG.a, IG.M) + " = " + sciHTML(ca, obj) + T(". The exponent goes down " + g + ", so the point of the coefficient moves " + g + lugares(g) + " to the right.", ". El exponente baja " + g + ", así que el punto del coeficiente se mueve " + g + lugares(g) + " a la derecha."));
  p.push(T("Now both powers are 10<sup>" + expTexto(obj) + "</sup>: ", "Ahora las dos potencias son 10<sup>" + expTexto(obj) + "</sup>: ") + (IG.op === "+" ? T("add", "se suman") : T("subtract", "se restan")) + T(" the coefficients, ", " los coeficientes, ") + ca + " " + IG.op + " " + cb + " = " + rc + T(". Partial answer: ", ". Resultado parcial: ") + sciHTML(rc, obj) + ".");
  var nec = !esValida(rc);
  p.push(nec ? T("The coefficient " + rc + " is not from 1 to 10, so it needs adjusting: ", "El coeficiente " + rc + " no está entre 1 y 10, así que hay que ajustar: ") + sciHTML(rc, obj) + " = " + numSciHTML(R) + "." : T("The coefficient " + rc + " is already from 1 to 10: no adjustment needed.", "El coeficiente " + rc + " ya está entre 1 y 10: no hace falta ajustar."));
  var h = "<p><strong>" + T("Way chosen: ", "Camino elegido: ") + (subir ? T("raise the smaller exponent", "subir el exponente menor") : T("lower the larger exponent", "bajar el exponente mayor")) + ".</strong></p>";
  p.forEach(function(x, i){ h += '<div class="paso"><span class="n" aria-hidden="true">' + (i + 1) + "</span>" + x + "</div>"; });
  h += '<div class="paso"><span class="n" aria-hidden="true">✓</span><span class="veredicto">' + T("Answer: ", "Resultado: ") + numSciHTML(R) + ".</span> " + (nec ? T("This way needed an adjustment at the end.", "Este camino necesitó un ajuste al final.") : T("This way did not need a final adjustment.", "Este camino no necesitó ajuste final.")) + T(" Try the other way and compare.", " Pruebe el otro camino y compare.") + "</div>";
  $("ig-pasos").innerHTML = h;
}
function genIgualar(){
  var M = aleatorio(-4, 9), g = aleatorio(1, 2), a = coefAzar(aleatorio(1, 2)), b = coefAzar(aleatorio(1, 2)), n = M - g, A = sci(a, M), Bn = sci(b, n), R = suma(A, Bn), rr = coefCon(Bn, M), pg = Math.random() < 0.5;
  return {enun: T("Find ", "Calcule ") + (pg ? sciHTML(a, M) + " + " + sciHTML(b, n) : sciHTML(b, n) + " + " + sciHTML(a, M)) + ".", resp: R,
    alPintar: function(){ $("p2-rlab").textContent = T("Step 1: rewrite " + sciTexto(b, n) + " with the power 10" + supTexto(M) + ". Coefficient:", "Paso 1: reescriba " + sciTexto(b, n) + " con la potencia 10" + supTexto(M) + ". Coeficiente:"); $("p2-rpot").innerHTML = "× 10<sup>" + expTexto(M) + "</sup>"; },
    previo: function(){
      var v = leeNumero($("p2-r").value); $("p2-r").classList.toggle("error", !v || !igual(v, leeNumero(rr)));
      if (!v) return T("Finish step 1: the coefficient of " + sciTexto(b, n) + " rewritten with 10" + supTexto(M) + ".", "Complete el paso 1: el coeficiente de " + sciTexto(b, n) + " reescrito con 10" + supTexto(M) + ".");
      if (!igual(v, leeNumero(rr))) return T("Step 1 is not right: to raise the exponent from " + expTexto(n) + " to " + expTexto(M) + ", the point of the coefficient moves " + g + lugares(g) + " to the left.", "El paso 1 no es correcto: para subir el exponente de " + expTexto(n) + " a " + expTexto(M) + ", el punto del coeficiente se mueve " + g + lugares(g) + " a la izquierda.");
      return null; },
    explica: sciHTML(b, n) + " = " + sciHTML(rr, M) + T("; then ", "; después ") + a + " + " + rr + " = " + coefCon(R, M) + "." + (esValida(coefCon(R, M)) ? "" : T(" Since " + coefCon(R, M) + " is 10 or more, it is adjusted.", " Como " + coefCon(R, M) + " es 10 o más, se ajusta."))};
}

/* ============ MODULE 3 · subtracting ============ */
function actualizaSR(){
  var a = leeCoef("sr-a"), b = leeCoef("sr-b"), m = leeExp("sr-m", 0, 6), n = leeExp("sr-n", 0, 6), av = $("sr-aviso");
  if (a === null || b === null || m === null || n === null){ av.className = "caja-aviso visible"; av.textContent = T("The coefficients must be from 1 to 10 and the exponents must be whole numbers from 0 to 6.", "Los coeficientes deben estar entre 1 y 10 y los exponentes deben ser números enteros de 0 a 6."); $("sr-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var A = sci(a, m), Bn = sci(b, n), R = resta(A, Bn), M = Math.max(m, n), h = columnasHTML(A, Bn, "−", R), ca = coefCon(A, M), cb = coefCon(Bn, M), rc = coefCon(R, M);
  if (m !== n) h += '<div class="linea">' + T("Match the exponents to the larger one: ", "Se igualan los exponentes al mayor: ") + (m < n ? sciHTML(a, m) + " = " + sciHTML(ca, M) : sciHTML(b, n) + " = " + sciHTML(cb, M)) + ".</div>";
  h += '<div class="linea">' + T("Subtract the coefficients: ", "Se restan los coeficientes: ") + ca + " − " + cb + " = " + signo(rc) + T(", so the difference is ", ", así que la diferencia es ") + (esCero(R) ? "0." : sciHTML(rc, M) + (esValida(rc) ? "." : " = " + numSciHTML(R) + ' <span class="nota">' + T("(the coefficient was adjusted)", "(el coeficiente se ajustó)") + "</span>.")) + "</div>";
  h += '<div class="linea veredicto">✓ ' + (esCero(R) ? T("The two amounts are equal: the difference is 0.", "Las dos cantidades son iguales: la diferencia es 0.") : conComas(R) + " = " + numSciHTML(R) + ".") + "</div>";
  if (compara(R, N(0)) < 0) h += '<div class="linea nota">' + T("The answer is negative because the second amount is larger: the coefficient has a minus sign.", "El resultado es negativo porque la segunda cantidad es mayor: el coeficiente lleva el signo menos.") + "</div>";
  $("sr-salida").innerHTML = h;
}
var SR_COLA = [["1.2", 5, "9", 4], ["9", 6, "4", 6]];
function azarSR(){ var e = SR_COLA.length ? SR_COLA.shift() : null; if (!e){ var m = aleatorio(1, 6), n = Math.max(0, m - aleatorio(0, 1)); e = [coefAzar(aleatorio(1, 2)), m, coefAzar(aleatorio(1, 2)), n]; } $("sr-a").value = e[0]; $("sr-m").value = e[1]; $("sr-b").value = e[2]; $("sr-n").value = e[3]; actualizaSR(); }
function genRestar(){
  var t = aleatorio(1, 4), a, b, m, n;
  if (t === 1){ m = n = aleatorio(-5, 9); a = coefAzar(aleatorio(1, 2)); b = coefAzar(aleatorio(1, 2)); while (a === b) b = coefAzar(aleatorio(1, 2)); if (compara(leeNumero(a), leeNumero(b)) < 0){ var x = a; a = b; b = x; } }
  else if (t === 2){ m = aleatorio(-4, 9); n = m - aleatorio(1, 2); a = coefAzar(aleatorio(1, 2)); b = coefAzar(1); }
  else if (t === 3){ m = n = aleatorio(-4, 9); a = b = coefAzar(aleatorio(1, 2)); }
  else { var ai = aleatorio(11, 19); m = aleatorio(-3, 9); n = m - 1; a = plano(sci(String(ai), -1)); b = String(aleatorio(ai - 9, 9)); }
  var A = sci(a, m), Bn = sci(b, n), R = resta(A, Bn), o = [], pc = {}, enun = T("Find ", "Calcule ") + sciHTML(a, m) + " − " + sciHTML(b, n) + ".";
  if (esCero(R)){
    var z = op(a, m); pc[z.clave] = T("Subtract the coefficients: " + a + " − " + a + " = 0.", "Se restan los coeficientes: " + a + " − " + a + " = 0.");
    return {enun: enun, opciones: [{html: "0", clave: "0"}, z, op("1", m), op(a, 0)], correcta: "0", porClave: pc, bien: T("Two equal amounts have a difference of 0.", "Dos cantidades iguales dan diferencia 0."), mal: T("The two amounts are equal, so the difference is 0.", "Las dos cantidades son iguales, así que la diferencia es 0.")};
  }
  var rs = aSci(R), rc = coefCon(R, m); o.push(opNum(R));
  var x1 = op(plano(resta(leeNumero(a), leeNumero(b))).replace(/^-/, ""), m - n); o.push(x1); pc[x1.clave] = T("The exponents are not subtracted: the common power of 10 stays.", "Los exponentes no se restan: la potencia de 10 común se conserva.");
  if (m !== n){ var d = resta(leeNumero(a), leeNumero(b)), x2 = opNum(porPot(d, m)); if (!esCero(x2) && compara(d, N(0)) > 0){ o.push(x2); pc[x2.clave] = T("Make the exponents equal before you subtract.", "Antes de restar hay que igualar los exponentes."); } }
  if (!esValida(rc)){ var x3 = op(rc, m); o.push(x3); pc[x3.clave] = T("The value is right, but " + rc + " is less than 1: it still needs adjusting.", "El valor es correcto, pero " + rc + " es menor que 1: falta ajustar."); }
  o.push(op(rs.c, rs.e + 1)); o.push(op(rs.c, rs.e - 1));
  var expl = (m !== n ? sciHTML(b, n) + " = " + sciHTML(coefCon(Bn, m), m) + "; " : "") + a + " − " + coefCon(Bn, m) + " = " + rc + "." + (esValida(rc) ? "" : T(" Since " + rc + " is less than 1, it is adjusted to ", " Como " + rc + " es menor que 1, se ajusta a ") + numSciHTML(R) + ".");
  return {enun: enun, opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc, bien: expl, mal: expl + " " + T("The answer is ", "La respuesta es ") + numSciHTML(R) + "."};
}

/* ============ MODULE 4 · mixed problems ============ */
function genAplicacion(){
  var t = aleatorio(1, 8), A, Bn, M;
  if (t === 1){ var v = sci(coefAzar(1), 4), h = sci(coefAzar(1), 2);
    return {operacion: "×", resp: mul(v, h), porQueOp: T("the probe goes the same distance every hour: multiply.", "la sonda recorre la misma distancia cada hora: se multiplica."), explica: T("Distance = distance per hour × number of hours.", "Distancia = distancia por hora × número de horas."),
      enun: T("A space probe travels ", "Una sonda espacial recorre ") + numSciHTML(v) + T(" km each hour. How far does it go in ", " km cada hora. ¿Qué distancia recorre en ") + numSciHTML(h) + T(" hours?", " horas?")}; }
  if (t === 2){ M = aleatorio(5, 7); A = sci(coefAzar(1), M); Bn = sci(coefAzar(1), M - 1);
    return {operacion: "+", resp: suma(A, Bn), porQueOp: T("“are added” means putting the two amounts together: add.", "«se le añaden» indica juntar las dos cantidades: se suma."), explica: T("Make the exponents equal and add the coefficients.", "Se igualan los exponentes y se suman los coeficientes."),
      enun: T("A blood sample has ", "Una muestra de sangre tiene ") + numSciHTML(A) + T(" red blood cells, and ", " glóbulos rojos y se le añaden ") + numSciHTML(Bn) + T(" more are added. How many red blood cells are there in all?", " más. ¿Cuántos glóbulos rojos hay en total?")}; }
  if (t === 3){ var cn = sci(coefAzar(1), aleatorio(3, 7)), f = sci(coefAzar(1), aleatorio(4, 7)), D = mul(cn, f);
    return {operacion: "÷", resp: cn, porQueOp: T("“how many fit” shares the capacity over the size of each file: divide.", "«cuántos caben» reparte la capacidad entre el tamaño de cada archivo: se divide."), explica: T("Number of files = capacity ÷ size of each file.", "Cantidad de archivos = capacidad ÷ tamaño de cada archivo."),
      enun: T("A drive holds ", "Un disco guarda ") + numSciHTML(D) + T(" bytes, and each file takes up ", " bytes y cada archivo ocupa ") + numSciHTML(f) + T(" bytes. How many files fit?", " bytes. ¿Cuántos archivos caben?")}; }
  if (t === 4){ M = aleatorio(6, 9); A = sci(String(aleatorio(2, 9)), M); Bn = sci(coefAzar(1), M - 1);
    return {operacion: "−", resp: resta(A, Bn), porQueOp: T("“how much is left” after losing water: subtract.", "«cuánta le queda» después de perder agua: se resta."), explica: T("Make the exponents equal and subtract the coefficients.", "Se igualan los exponentes y se restan los coeficientes."),
      enun: T("A reservoir holds ", "Un embalse tiene ") + numSciHTML(A) + T(" gallons of water, and over the summer it loses ", " galones de agua y durante el verano pierde ") + numSciHTML(Bn) + T(" gallons. How much water is left?", " galones. ¿Cuánta agua le queda?")}; }
  if (t === 5){ var g = sci(elige(["6", "7", "5"]), -4), cg = sci(coefAzar(1), aleatorio(3, 6));
    return {operacion: "×", resp: mul(g, cg), porQueOp: T("all the grains have the same mass: multiply the mass of one by the number of grains.", "todos los granos tienen la misma masa: se multiplica la masa de uno por la cantidad."), explica: T("Total mass = mass of one grain × number of grains.", "Masa total = masa de un grano × número de granos."),
      enun: T("A grain of sand has a mass of about ", "Un grano de arena tiene una masa aproximada de ") + numSciHTML(g) + T(" grams. What is the mass of ", " gramos. ¿Cuál es la masa de ") + numSciHTML(cg) + T(" grains?", " granos?")}; }
  if (t === 6){ var cel = sci(coefAzar(1), -5), nn = sci(coefAzar(1), aleatorio(2, 4)), L = mul(cel, nn);
    return {operacion: "÷", resp: nn, porQueOp: T("“how many fit” in a length: divide the length by the width of one cell.", "«cuántas caben» en una longitud: se divide la longitud entre el ancho de una célula."), explica: T("Number = total length ÷ width of one cell.", "Cantidad = longitud total ÷ ancho de una célula."),
      enun: T("A cell is ", "Una célula mide ") + numSciHTML(cel) + T(" meters wide. How many cells, set in a row, cover ", " metros de ancho. ¿Cuántas células, puestas en fila, cubren ") + numSciHTML(L) + T(" meters?", " metros?")}; }
  if (t === 7){ A = sci(coefAzar(1), 13); Bn = sci(coefAzar(1), 12);
    return {operacion: "+", resp: suma(A, Bn), porQueOp: T("“farther than the first” is added to its distance: add.", "«más lejos que la primera» se añade a su distancia: se suma."), explica: T("Make the exponents equal and add the coefficients.", "Se igualan los exponentes y se suman los coeficientes."),
      enun: T("A star is ", "Una estrella está a ") + numSciHTML(A) + T(" km from the Earth. Another one is ", " km de la Tierra. Otra está ") + numSciHTML(Bn) + T(" km farther away than the first. How far from the Earth is the second star?", " km más lejos que la primera. ¿A qué distancia de la Tierra está la segunda?")}; }
  A = sci("5.97", 24); Bn = sci("7.35", 22);
  return {operacion: "−", resp: resta(A, Bn), porQueOp: T("“how much more mass” asks for the difference: subtract.", "«cuánta masa más» pide la diferencia: se resta."), explica: sciHTML("7.35", 22) + " = " + sciHTML("0.0735", 24) + T(", and 5.97 − 0.0735 = 5.8965.", ", y 5.97 − 0.0735 = 5.8965."),
    enun: T("The mass of the Earth is ", "La masa de la Tierra es ") + numSciHTML(A) + T(" kg and the mass of the Moon is ", " kg y la de la Luna es ") + numSciHTML(Bn) + T(" kg. How much more mass does the Earth have than the Moon?", " kg. ¿Cuánta masa más tiene la Tierra que la Luna?")};
}

/* ============ Start ============ */
["se-a", "se-b", "se-n"].forEach(function(id){ $(id).addEventListener("input", actualizaSE); });
$("se-azar").addEventListener("click", azarSE);
actualizaSE();
OMS("p1", genSumar);
$("ig-subir").addEventListener("click", function(){ caminoIG(true); });
$("ig-bajar").addEventListener("click", function(){ caminoIG(false); });
$("ig-nuevo").addEventListener("click", function(){ cargaIG(IG.cola.length ? IG.cola.shift() : azarIG()); });
cargaIG(IG.cola.shift());
creaPracticaSci("p2", genIgualar);
["sr-a", "sr-m", "sr-b", "sr-n"].forEach(function(id){ $(id).addEventListener("input", actualizaSR); });
$("sr-azar").addEventListener("click", azarSR);
actualizaSR();
OMS("p3", genRestar);
creaPracticaSci("p4", genAplicacion);
'''

def campo(i, et, v, corto=False):
    return f'<div class="campo"><label for="{i}">{et}</label><input type="text" inputmode="decimal" autocomplete="off" id="{i}" value="{v}"{" class=\"corto\"" if corto else ""}></div>'

def practica_pagina():
    n = N
    P = n3
    filas = [(t("“in all,” “are added,” “together”", "«en total», «se añaden», «juntos»"), t("an addition", "una suma")),
             (t("“is left,” “how much more,” “difference”", "«queda», «cuánto más», «diferencia»"), t("a subtraction", "una resta")),
             (t("“each hour for…,” “for each one, how many in…”", "«cada hora durante…», «por cada uno, cuántos en…»"), t("a multiplication", "una multiplicación")),
             (t("“how many fit,” “per,” “share”", "«cuántos caben», «por cada», «repartir»"), t("a division", "una división"))]
    paso1 = f'''
        <div class="campo" style="margin-bottom:6px;">
          <label for="p2-r" id="p2-rlab"></label>
          <div style="display:flex;align-items:center;gap:10px;"><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="p2-r"><span aria-hidden="true" style="font-size:20px;font-weight:700;white-space:nowrap;" id="p2-rpot"></span></div>
        </div>
        <p class="nota">{t("Step 2: write the final answer in valid scientific notation.", "Paso 2: escriba el resultado final en notación científica válida.")}</p>'''
    igualar = n3.sci_input("p2", t("Practice: match, then add", "Practique: iguale y sume")).replace('<div class="enun" id="p2-enun"></div>', '<div class="enun" id="p2-enun"></div>' + paso1)
    mods = [
     (t("add", "sumar"), t("Adding with equal exponents", "Sumar con exponentes iguales"),
      f'''      <p>{t("You can only add amounts directly when they have the <strong>same power of 10</strong>, just as you only add things of the same kind: 4 hundreds plus 5 hundreds are 9 hundreds. Add the coefficients and the power <strong>stays the same</strong>.", "Solo se suman directamente cantidades con la <strong>misma potencia de 10</strong>, igual que solo se suman objetos del mismo tipo: 4 cientos más 5 cientos son 9 cientos. Se suman los coeficientes y la potencia <strong>se conserva</strong>.")}</p>
{P.formula("(a × 10<sup>n</sup>) + (b × 10<sup>n</sup>) = (a + b) × 10<sup>n</sup>")}
      <h3>{t("Check it with ordinary addition", "Compruébelo con la suma de siempre")}</h3>
      <p>{t("Choose the coefficients and the exponent. The column addition shows that the power does not change, and the box below shows what the mistake of adding the exponents too would give.", "Elija los coeficientes y el exponente. La suma en columnas muestra que la potencia no cambia, y el recuadro de abajo muestra qué pasaría con el error de sumar también los exponentes.")}</p>
      <div class="panel"><div class="campos">{campo("se-a", t("First coefficient", "Primer coeficiente"), 4)}{campo("se-b", t("Second coefficient", "Segundo coeficiente"), 5)}{campo("se-n", t("Common exponent (0 to 6)", "Exponente común (de 0 a 6)"), 2, True)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="se-azar">{t("Another example", "Otro ejemplo")}</button></div></div>
{P.aviso("se-aviso")}
{P.salida("se-salida")}
{P.atencion(t("The power does not change:", "La potencia no cambia:"), t("3 × 10<sup>4</sup> + 2 × 10<sup>4</sup> is 5 × 10<sup>4</sup>, never 5 × 10<sup>8</sup>. And if the sum of the coefficients is 10 or more, adjust it as in the last lesson: 14 × 10<sup>5</sup> = 1.4 × 10<sup>6</sup>.", "3 × 10<sup>4</sup> + 2 × 10<sup>4</sup> es 5 × 10<sup>4</sup>, nunca 5 × 10<sup>8</sup>. Y si la suma de coeficientes llega a 10 o más, se ajusta igual que en la lección anterior: 14 × 10<sup>5</sup> = 1.4 × 10<sup>6</sup>."))}
{B.om("p1", t("Practice: adding with equal exponents", "Practique: sumar con exponentes iguales"))}'''),
     (t("match", "igualar"), t("Making the exponents equal", "Igualar los exponentes"),
      f'''      <p>{t("If the powers of 10 do not match, first <strong>rewrite one of the amounts</strong> so both have the same exponent. Then add or subtract the coefficients and, at the end, adjust if needed.", "Si las potencias de 10 no coinciden, primero se <strong>reescribe una de las cantidades</strong> para que las dos tengan el mismo exponente. Después se suman o se restan los coeficientes y, al final, se ajusta si hace falta.")}</p>
      <h3>{t("Two ways, the same answer", "Dos caminos, el mismo resultado")}</h3>
      <p>{t("Try both ways of matching. Both give the same answer; notice which one saves you the final adjustment.", "Pruebe las dos maneras de igualar. Las dos llegan al mismo resultado; fíjese en cuál le ahorra el ajuste final.")}</p>
      <div class="panel"><div class="estado" id="ig-expr"></div>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn" id="ig-subir">{t("Raise the smaller exponent", "Subir el exponente menor")}</button><button type="button" class="btn" id="ig-bajar">{t("Lower the larger exponent", "Bajar el exponente mayor")}</button><button type="button" class="btn-sec" id="ig-nuevo">{t("Another example", "Otro ejemplo")}</button></div></div>
      <div class="pasos" id="ig-pasos" aria-live="polite"></div>
      <div class="caja-tip"><strong>{t("Why match the larger exponent:", "Por qué conviene igualar al mayor:")}</strong> {t("the term you rewrite gets a coefficient less than 1 (like 0.3), but the sum almost always lands right in valid form, with no extra adjustment.", "el término que se reescribe queda con un coeficiente menor que 1 (como 0.3), pero la suma casi siempre cae directamente en la forma válida, sin ajuste adicional.")}</div>
{igualar}'''),
     (t("subtract", "restar"), t("Subtracting in scientific notation", "Restar en notación científica"),
      f'''      <p>{t("Subtraction follows the same idea: with equal exponents, subtract the coefficients; if they are different, match them first. Watch for one case: when the two amounts are close, the difference can be <strong>less than 1</strong> and needs a new adjustment.", "La resta sigue la misma idea: con exponentes iguales se restan los coeficientes; si son distintos, se igualan primero. Hay que estar atentos a un caso: cuando las dos cantidades son parecidas, la diferencia puede quedar <strong>menor que 1</strong> y obliga a reajustar el coeficiente.")}</p>
{P.formula("(a × 10<sup>n</sup>) − (b × 10<sup>n</sup>) = (a − b) × 10<sup>n</sup>")}
      <h3>{t("Subtraction in columns", "La resta en columnas")}</h3>
      <p>{t("Type two amounts, with the same exponent or different ones, and compare ordinary subtraction with subtraction in scientific notation.", "Escriba dos cantidades, con el mismo exponente o con exponentes distintos, y compare la resta de siempre con la resta en notación científica.")}</p>
      <div class="panel"><div class="campos">{campo("sr-a", t("First coefficient", "Primer coeficiente"), 7)}{campo("sr-m", t("First exponent (0 to 6)", "Primer exponente (0 a 6)"), 4, True)}{campo("sr-b", t("Second coefficient", "Segundo coeficiente"), 2)}{campo("sr-n", t("Second exponent (0 to 6)", "Segundo exponente (0 a 6)"), 3, True)}</div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="sr-azar">{t("Another example", "Otro ejemplo")}</button></div></div>
{P.aviso("sr-aviso")}
{P.salida("sr-salida")}
{B.om("p3", t("Practice: subtract", "Practique: restar"))}'''),
     (t("applications", "aplicaciones"), t("Science and technology applications", "Aplicaciones en ciencia y tecnología"),
      f'''      <p>{t("Here the four operations are mixed in real settings: space, cells, and technology. Before you calculate, decide what the problem asks for.", "Aquí se mezclan las cuatro operaciones en contextos reales: el espacio, las células y la tecnología. Antes de calcular, decida qué pide el problema.")}</p>
      <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("Hints (table you can scroll sideways)", "Pistas (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("Hints for choosing the operation", "Pistas para elegir la operación")}</caption>
      <thead><tr><th scope="col">{t("If the question says…", "Si la pregunta dice…")}</th><th scope="col">{t("It is usually", "Suele ser")}</th></tr></thead><tbody>{"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in filas)}</tbody></table></div>
{P.sci_input("p4", t("Practice: mixed problems", "Practique: problemas mezclados"), ops=[("+", t("Add", "Sumar")), ("−", t("Subtract", "Restar")), ("×", t("Multiply", "Multiplicar")), ("÷", t("Divide", "Dividir"))])}''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n3.ESTILO_SCI, scripts=("/math/scinot.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Suma, resta y aplicaciones en ciencia y tecnología")
