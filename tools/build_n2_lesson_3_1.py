"""Level 2 · Lesson 3.1 · Order of operations: review and nested parentheses — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla
from n2 import pasos_panel

B.NIVEL = 2
N = "3-1"
TEMA = ("The full order of operations (PEMDAS)", "PEMDAS completo")
TIT = ("Order of operations: review and nested parentheses", "Orden de operaciones: repaso y paréntesis anidados")

C1, C2, C3 = "#0d47a1", "#1b5e20", "#6a1b9a"
def g(k, x):
    """Agrupador de color: ( ) azul, [ ] verde, { } violeta."""
    col, cierra = {"(": (C1, ")"), "[": (C2, "]"), "{": (C3, "}")}[k]
    return f'<strong style="color:{col}">{k}</strong>{x}<strong style="color:{col}">{cierra}</strong>'
def hl(x):
    return f'<mark style="background:#fff3e0;outline:2px solid #bf360c;border-radius:4px;padding:0 3px">{x}</mark>'
def linea(x):
    return f'<p style="text-align:center;font-size:1.15em;margin:4px 0">{x}</p>'

def leccion():
    n = N
    filas = [["1", "<strong>P</strong>", t("<strong>Parentheses</strong> and other grouping symbols. Whatever is inside goes first.", "<strong>Paréntesis</strong> y otros símbolos de agrupación. Lo que está dentro se resuelve primero.")],
             ["2", "<strong>E</strong>", t("<strong>Exponents</strong> and roots. Find any power or root before you use its value.", "<strong>Exponentes</strong> y raíces. Cualquier potencia o raíz se evalúa antes de operar con su valor.")],
             ["3", "<strong>MD</strong>", t("<strong>Multiplication and division</strong>, in the order they appear, <strong>from left to right</strong>. Neither one goes before the other.", "<strong>Multiplicación y división</strong>, en el orden en que aparecen, <strong>de izquierda a derecha</strong>. Ninguna tiene prioridad sobre la otra.")],
             ["4", "<strong>AS</strong>", t("<strong>Addition and subtraction</strong>, in the order they appear, <strong>from left to right</strong>. Neither one goes before the other.", "<strong>Adición (suma) y sustracción (resta)</strong>, en el orden en que aparecen, <strong>de izquierda a derecha</strong>. Tampoco tienen prioridad una sobre la otra.")]]
    s1 = f'''<p>{t("Welcome to Topic 3. In Topics 1 and 2 you built separate tools: integers, fractions with signs, powers, and square roots. In Topic 3 all those pieces come together under one set of rules: the <strong>order of operations</strong>. Without it, the same expression could give different answers depending on who works it. With it, everyone gets exactly the same answer.",
"Bienvenido al Tema 3. En los Temas 1 y 2 construyó herramientas por separado: enteros con signo, fracciones con signo, potencias y raíces cuadradas. En el Tema 3 todas esas piezas se unen bajo un mismo sistema de reglas: el <strong>orden de las operaciones</strong>. Sin él, una misma expresión podría dar resultados distintos según quién la calcule. Con él, todo el mundo llega exactamente al mismo resultado.")}</p>
<p>{t("The word <strong>PEMDAS</strong> sums up the order. Each letter is a stage, and the stages always go in the same order:", "La palabra <strong>PEMDAS</strong> resume el orden. Cada letra es una etapa, y las etapas se aplican siempre en el mismo orden:")}</p>
{tabla(t("The four levels of PEMDAS", "Los cuatro niveles de PEMDAS"), t("The four levels of the order of operations, from the first to the last", "Los cuatro niveles del orden de las operaciones, del primero al último"),
       [t("Level", "Nivel"), t("Letters", "Letras"), t("What you do", "Qué se hace")], filas)}
{caja("tip", t("Key idea", "Idea clave"), t("<p>PEMDAS has six letters, but there are only <strong>four levels</strong>. M and D share a level, and so do A and S. Mixing this up causes most mistakes. Some people remember the order with the sentence \"Please Excuse My Dear Aunt Sally.\"</p>",
"<p>PEMDAS tiene seis letras, pero hay solo <strong>cuatro niveles</strong>. La M y la D comparten nivel, y también la A y la S. Confundirlo es el origen de la mayoría de los errores.</p>"))}
{caja("ojo", t("The most common mistake", "El error más común"), t("<p>Thinking that multiplication always goes before division because \"M comes first.\" It does not: in 20 ÷ 4 × 5, divide first because it is farther left (20 ÷ 4 = 5; 5 × 5 = 25). Multiplying first would give 20 ÷ 20 = 1, which is wrong.</p>",
"<p>Creer que la multiplicación siempre va antes que la división porque «la M aparece primero». No es así: en 20 ÷ 4 × 5 se divide primero por estar más a la izquierda (20 ÷ 4 = 5; 5 × 5 = 25). Multiplicar primero daría 20 ÷ 20 = 1, que es incorrecto.</p>"))}
{practica("p1", t("Practice 1 — What goes first?", "Práctica 1 — ¿Qué va primero?"), t("In 5 + 2 × 7 − 3, which operation goes first?", "En 5 + 2 × 7 − 3, ¿qué operación va primero?"),
          [("a", t("the addition 5 + 2", "la suma 5 + 2")), ("b", t("the subtraction 7 − 3", "la resta 7 − 3")), ("c", t("the multiplication 2 × 7", "la multiplicación 2 × 7"))])}
{practica("p2", t("Practice 2 — Left to right", "Práctica 2 — De izquierda a derecha"), t("In 20 ÷ 5 × 2, which operation goes first?", "En 20 ÷ 5 × 2, ¿qué operación va primero?"),
          [("a", t("the multiplication 5 × 2", "la multiplicación 5 × 2")), ("b", t("the division 20 ÷ 5", "la división 20 ÷ 5")), ("c", t("The order does not matter.", "No importa el orden."))])}
{enlace(n, t("pyramid", "piramide"), t("the four levels of priority", "la pirámide de prioridades"), t("Decide which operation goes first using the four levels of PEMDAS.", "Identifique qué operación va primero según los cuatro niveles de PEMDAS."))}'''

    s2 = f'''<p>{t("The safest way is to <strong>copy the expression at every step</strong>, solving only the operation with the highest priority and leaving the rest as it is. That way you can clearly see the next move.", "La técnica más segura es <strong>copiar la expresión en cada paso</strong>, resolviendo solo la operación de mayor prioridad y dejando intacto el resto. Así se ve con claridad cuál es la jugada siguiente.")}</p>
{ejemplo(t("Example: 6 + 3 × 4 − 2", "Ejemplo: 6 + 3 × 4 − 2"),
  [("1", "MD.", t(f"No parentheses and no exponents. The multiplication goes first: 6 + {hl('3 × 4')} − 2 → 6 + 12 − 2.", f"No hay paréntesis ni exponentes. La multiplicación va primero: 6 + {hl('3 × 4')} − 2 → 6 + 12 − 2.")),
   ("2", "AS.", t(f"Add and subtract from left to right: {hl('6 + 12')} − 2 → 18 − 2.", f"Suma y resta de izquierda a derecha: {hl('6 + 12')} − 2 → 18 − 2.")),
   ("✓", t("Result.", "Resultado."), "18 − 2 = <strong>16</strong>")])}
{ejemplo(t("Example: (8 − 3)<sup>2</sup> + 12 ÷ 4", "Ejemplo: (8 − 3)<sup>2</sup> + 12 ÷ 4"),
  [("1", "P.", t(f"Inside the parentheses: {hl('8 − 3')} = 5 → 5<sup>2</sup> + 12 ÷ 4.", f"Dentro del paréntesis: {hl('8 − 3')} = 5 → 5<sup>2</sup> + 12 ÷ 4.")),
   ("2", "E.", t(f"The exponent: {hl('5<sup>2</sup>')} = 25 → 25 + 12 ÷ 4.", f"El exponente: {hl('5<sup>2</sup>')} = 25 → 25 + 12 ÷ 4.")),
   ("3", "MD.", t(f"The division: {hl('12 ÷ 4')} = 3 → 25 + 3.", f"La división: {hl('12 ÷ 4')} = 3 → 25 + 3.")),
   ("✓", "AS.", "25 + 3 = <strong>28</strong>")])}
{calc(t("The calculator follows PEMDAS", "La calculadora sigue PEMDAS"), t(f"""<p>The TI-30XS follows the order of operations by itself. For (8 − 3)<sup>2</sup> + 12 ÷ 4, press {T("(")} {T("8")} {T("−")} {T("3")} {T(")")} {T("x<sup>2</sup>")} {T("+")} {T("1")}{T("2")} {T("÷")} {T("4")} {T("enter")}. The screen shows 28. Work it on paper first: the GED asks you to know the steps.</p>""",
f"""<p>La TI-30XS sigue sola el orden de las operaciones. Para (8 − 3)<sup>2</sup> + 12 ÷ 4, pulse {T("(")} {T("8")} {T("−")} {T("3")} {T(")")} {T("x<sup>2</sup>")} {T("+")} {T("1")}{T("2")} {T("÷")} {T("4")} {T("enter")}. La pantalla muestra 28. Resuélvalo primero en papel: el GED pide conocer los pasos.</p>"""))}
{practica("p3", t("Practice 3 — Solve it", "Práctica 3 — Resuélvalo"), t("What is 7 + 6 × 2 − 4?", "¿Cuánto es 7 + 6 × 2 − 4?"),
          [("a", "22"), ("b", "15"), ("c", "9"), ("d", "11")])}
{enlace(n, t("step-by-step", "paso-a-paso"), t("step by step", "aplicación paso a paso"), t("Follow the expression line by line, solving one operation at each step.", "Siga la expresión línea por línea, resolviendo una sola operación en cada paso."))}'''

    s3 = f'''<p>{t("When an expression has grouping symbols <strong>inside</strong> other grouping symbols, always work <strong>from the innermost to the outermost</strong>.", "Cuando una expresión tiene agrupadores <strong>dentro</strong> de otros agrupadores, se resuelve siempre <strong>del más interior al más exterior</strong>.")}</p>
<p>{t("To tell them apart at a glance, we use three kinds of grouping symbols:", "Para distinguirlos a simple vista, se usan tres tipos de símbolos de agrupación:")}</p>
<ul>
<li>{t(f"Parentheses {g('(', '&nbsp;')}: the innermost level.", f"Paréntesis {g('(', '&nbsp;')}: el nivel más interior.")}</li>
<li>{t(f"Brackets {g('[', '&nbsp;')}: the middle level.", f"Corchetes {g('[', '&nbsp;')}: el nivel intermedio.")}</li>
<li>{t(f"Braces {g('{', '&nbsp;')}: the outermost level.", f"Llaves {g('{', '&nbsp;')}: el nivel más exterior.")}</li>
</ul>
<p>{t("They all work exactly like parentheses: only the shape changes, so it is easier to match each opening symbol with its closing one.", "Funcionan exactamente igual que los paréntesis: solo cambia la forma, para que sea más fácil emparejar cada símbolo de apertura con el de cierre.")}</p>
{ejemplo(t("Example: two levels", "Ejemplo: dos niveles") + " &nbsp; 2 × " + g("[", "3 + " + g("(", "4 × 2")),
  [("1", t("Step 1.", "Paso 1."), t(f"The inner parentheses: {hl('4 × 2')} = 8 → 2 × {g('[', '3 + 8')}.", f"El paréntesis interior: {hl('4 × 2')} = 8 → 2 × {g('[', '3 + 8')}.")),
   ("2", t("Step 2.", "Paso 2."), t(f"The brackets: {hl('3 + 8')} = 11 → 2 × 11.", f"El corchete: {hl('3 + 8')} = 11 → 2 × 11.")),
   ("✓", t("Result.", "Resultado."), "2 × 11 = <strong>22</strong>")])}
{ejemplo(t("Example: three levels", "Ejemplo: tres niveles") + " &nbsp; 50 − " + g("{", "4 + " + g("[", "3 × " + g("(", "6 − 2"))),
  [("1", t("Step 1.", "Paso 1."), t(f"Inner parentheses: {hl('6 − 2')} = 4.", f"Paréntesis interior: {hl('6 − 2')} = 4.")),
   ("2", t("Step 2.", "Paso 2."), t(f"Brackets: {hl('3 × 4')} = 12.", f"Corchete: {hl('3 × 4')} = 12.")),
   ("3", t("Step 3.", "Paso 3."), t(f"Braces: {hl('4 + 12')} = 16.", f"Llave: {hl('4 + 12')} = 16.")),
   ("✓", t("Result.", "Resultado."), "50 − 16 = <strong>34</strong>")])}
{caja("tip", t("A visual strategy", "Una estrategia visual"), t("<p>Before you start, count and match the pairs. Each ( needs a ), each [ needs a ], and each { needs a }. This check prevents the most frustrating mistakes.</p>",
"<p>Antes de operar, cuente y empareje los pares. Cada ( necesita un ), cada [ un ] y cada { un }. Esta revisión previa evita los errores más frustrantes.</p>"))}
{caja("ojo", t("On the calculator", "En la calculadora"), t("<p>The calculator has only round parentheses. Type brackets and braces as parentheses too: 2 × [3 + (4 × 2)] is 2 × ((3 + (4 × 2))).</p>",
"<p>La calculadora solo tiene paréntesis redondos. Los corchetes y las llaves también se escriben como paréntesis: 2 × [3 + (4 × 2)] es 2 × ((3 + (4 × 2))).</p>"))}
{practica("p4", t("Practice 4 — Nested", "Práctica 4 — Anidados"), t("What is 3 × [2 + (8 ÷ 4)]?", "¿Cuánto es 3 × [2 + (8 ÷ 4)]?"),
          [("a", "8"), ("b", "12"), ("c", "10"), ("d", "6")])}
{enlace(n, t("nested", "anidados"), t("nested grouping symbols", "paréntesis anidados"), t("Work from the inside out with parentheses, brackets, and braces in different colors.", "Resuelva de adentro hacia afuera con paréntesis, corchetes y llaves en colores distintos."))}'''

    s4 = f'''<p>{t("The plan for any expression is always the same: first the grouping symbols, <strong>from the inside out</strong>, and inside each one, use PEMDAS <strong>from the start</strong>. When all the grouping symbols are gone, use PEMDAS on what is left.", "La estrategia para cualquier expresión es siempre la misma: primero los agrupadores, <strong>del interior al exterior</strong>, y dentro de cada uno se aplica PEMDAS <strong>desde el principio</strong>. Cuando se han resuelto todos los agrupadores, se aplica PEMDAS al resto.")}</p>
{ejemplo(t("Example:", "Ejemplo:") + " &nbsp; " + g("[", "2<sup>2</sup> + " + g("(", "15 − 3 × 4")) + " × 5",
  [("1", t("Step 1.", "Paso 1."), t(f"Inside the parentheses, multiply before subtracting: {hl('3 × 4')} = 12 → (15 − 12).", f"Dentro del paréntesis, se multiplica antes de restar: {hl('3 × 4')} = 12 → (15 − 12).")),
   ("2", t("Step 2.", "Paso 2."), t(f"Finish the parentheses: {hl('15 − 12')} = 3 → [2<sup>2</sup> + 3] × 5.", f"Se termina el paréntesis: {hl('15 − 12')} = 3 → [2<sup>2</sup> + 3] × 5.")),
   ("3", t("Step 3.", "Paso 3."), t(f"Inside the brackets, the exponent before the addition: {hl('2<sup>2</sup>')} = 4 → [4 + 3] × 5.", f"Dentro del corchete, el exponente antes que la suma: {hl('2<sup>2</sup>')} = 4 → [4 + 3] × 5.")),
   ("4", t("Step 4.", "Paso 4."), t(f"Finish the brackets: {hl('4 + 3')} = 7 → 7 × 5.", f"Se termina el corchete: {hl('4 + 3')} = 7 → 7 × 5.")),
   ("✓", t("Result.", "Resultado."), "7 × 5 = <strong>35</strong>")])}
{caja("ojo", t("Watch out!", "¡Ojo!"), t("<p>With grouping symbols, you do not use PEMDAS \"across the whole expression\" at once. Each grouping symbol is a small expression that you finish completely before you move to the next one.</p>",
"<p>Cuando hay agrupadores, PEMDAS no se aplica «de un lado a otro de toda la expresión» a la vez. Cada agrupador es una pequeña expresión que se resuelve por completo antes de pasar a la siguiente.</p>"))}
{practica("p5", t("Practice 5 — Everything together", "Práctica 5 — Todo junto"), t("What is (10 − 4)<sup>2</sup> ÷ 9?", "¿Cuánto es (10 − 4)<sup>2</sup> ÷ 9?"),
          [("a", "4"), ("b", "12"), ("c", "6"), ("d", "36")])}
{enlace(n, t("combined", "combinado"), t("everything combined", "todo combinado"), t("Practice expressions that combine grouping symbols, powers, and the four operations.", "Practique expresiones que combinan agrupadores, potencias y las cuatro operaciones."))}
{enlace(n, t("emoji-challenges", "retos"), t("emoji challenges", "retos con emojis"), t("Find the value of each emoji from the clues, then solve the final expression in the right order.", "Halle el valor de cada emoji con las pistas y resuelva la expresión final en el orden correcto."))}'''

    secciones = [("s-" + t("pyramid", "piramide"), t("The four levels of PEMDAS", "La pirámide de prioridades de PEMDAS"), s1),
                 ("s-" + t("step-by-step", "paso-a-paso"), t("Step by step", "Aplicación paso a paso"), s2),
                 ("s-" + t("nested", "anidados"), t("Nested grouping symbols: from the inside out", "Paréntesis anidados: del interior hacia el exterior"), s3),
                 ("s-" + t("combined", "combinado"), t("Putting it all together", "Combinando todo: PEMDAS con anidamiento"), s4)]

    lesson = {"next": t("Lesson 3.2", "Lección 3.2"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Addition is on the last level. Is there a multiplication or division?", "La suma está en el último nivel. ¿Hay una multiplicación o una división?"), "b": t("7 − 3 is not even an operation here: the 7 is multiplied by 2 first.", "7 − 3 ni siquiera es una operación aquí: el 7 se multiplica primero por 2.")},
             "right": t("Multiplication comes before addition and subtraction.", "La multiplicación va antes que la suma y la resta."), "solution": t("No parentheses or exponents, so multiplication goes first: 2 × 7 = 14. Then 5 + 14 − 3 = 16.", "No hay paréntesis ni exponentes, así que primero va la multiplicación: 2 × 7 = 14. Después 5 + 14 − 3 = 16.")},
      "p2": {"ok": "b", "hints": {"a": t("Multiplication and division are on the same level. Which one is farther left?", "La multiplicación y la división están en el mismo nivel. ¿Cuál está más a la izquierda?"), "c": t("The order matters: 20 ÷ 5 × 2 = 8, but 20 ÷ 10 = 2.", "El orden importa: 20 ÷ 5 × 2 = 8, pero 20 ÷ 10 = 2.")},
             "right": t("Same level: from left to right. 20 ÷ 5 = 4, then 4 × 2 = 8.", "Mismo nivel: de izquierda a derecha. 20 ÷ 5 = 4, y después 4 × 2 = 8."), "solution": t("Multiplication and division share a level, so you go from left to right: first 20 ÷ 5 = 4, then 4 × 2 = 8.", "La multiplicación y la división comparten nivel: se va de izquierda a derecha. Primero 20 ÷ 5 = 4, después 4 × 2 = 8.")},
      "p3": {"ok": "b", "hints": {"a": t("You added 7 + 6 first. Multiplication goes before addition.", "Sumó primero 7 + 6. La multiplicación va antes que la suma."), "c": t("Check: 6 × 2 = 12, then 7 + 12 − 4.", "Revise: 6 × 2 = 12, después 7 + 12 − 4."), "d": t("You subtracted 2 − 4 first. Multiply 6 × 2 first.", "Restó 2 − 4 primero. Primero multiplique 6 × 2.")},
             "right": t("6 × 2 = 12; 7 + 12 = 19; 19 − 4 = 15.", "6 × 2 = 12; 7 + 12 = 19; 19 − 4 = 15."), "solution": t("Multiply first: 6 × 2 = 12. Then from left to right: 7 + 12 = 19, and 19 − 4 = 15.", "Primero se multiplica: 6 × 2 = 12. Después de izquierda a derecha: 7 + 12 = 19, y 19 − 4 = 15.")},
      "p4": {"ok": "b", "hints": {"a": t("You did 3 × 2 first. Start with the innermost parentheses: 8 ÷ 4.", "Hizo 3 × 2 primero. Empiece por el paréntesis interior: 8 ÷ 4."), "c": t("Check the brackets: 2 + 2 = 4, then 3 × 4.", "Revise el corchete: 2 + 2 = 4, después 3 × 4."), "d": t("Finish the brackets first: 2 + 2 = 4. Then multiply by 3.", "Termine primero el corchete: 2 + 2 = 4. Después multiplique por 3.")},
             "right": t("8 ÷ 4 = 2; 2 + 2 = 4; 3 × 4 = 12.", "8 ÷ 4 = 2; 2 + 2 = 4; 3 × 4 = 12."), "solution": t("Inner parentheses: 8 ÷ 4 = 2. Brackets: 2 + 2 = 4. Then 3 × 4 = 12.", "Paréntesis interior: 8 ÷ 4 = 2. Corchete: 2 + 2 = 4. Después 3 × 4 = 12.")},
      "p5": {"ok": "a", "hints": {"b": t("6 × 2 is not 6<sup>2</sup>. Square means 6 × 6.", "6 × 2 no es 6<sup>2</sup>. Al cuadrado es 6 × 6."), "c": t("You did not square: 6<sup>2</sup> = 36. Then 36 ÷ 9.", "No elevó al cuadrado: 6<sup>2</sup> = 36. Después 36 ÷ 9."), "d": t("36 is (10 − 4)<sup>2</sup>. You still need to divide by 9.", "36 es (10 − 4)<sup>2</sup>. Todavía falta dividir entre 9.")},
             "right": t("(10 − 4) = 6; 6<sup>2</sup> = 36; 36 ÷ 9 = 4.", "(10 − 4) = 6; 6<sup>2</sup> = 36; 36 ÷ 9 = 4."), "solution": t("P: 10 − 4 = 6. E: 6<sup>2</sup> = 36. D: 36 ÷ 9 = 4.", "P: 10 − 4 = 6. E: 6<sup>2</sup> = 36. D: 36 ÷ 9 = 4.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("You added 4 + 5 first. Multiply first.", "Sumó primero 4 + 5. Primero se multiplica."), "b": t("Check: 5 × 3 = 15, then 4 + 15.", "Revise: 5 × 3 = 15, después 4 + 15."), "d": t("That is 4 × 5 × 3. The 4 is added.", "Eso es 4 × 5 × 3. El 4 se suma.")}, "solution": t("5 × 3 = 15; 4 + 15 = 19.", "5 × 3 = 15; 4 + 15 = 19.")},
      "B": {"ok": "a", "hints": {"b": t("You multiplied 4 × 5 first. Division and multiplication: from left to right.", "Multiplicó 4 × 5 primero. División y multiplicación: de izquierda a derecha."), "c": t("Check: 20 ÷ 4 = 5, then 5 × 5.", "Revise: 20 ÷ 4 = 5, después 5 × 5."), "d": t("Check: 20 ÷ 4 = 5, then 5 × 5.", "Revise: 20 ÷ 4 = 5, después 5 × 5.")}, "solution": t("Left to right: 20 ÷ 4 = 5; 5 × 5 = 25.", "De izquierda a derecha: 20 ÷ 4 = 5; 5 × 5 = 25.")},
      "C": {"ok": "d", "hints": {"a": t("You subtracted 12 − 2 first. Divide first: 8 ÷ 2.", "Restó primero 12 − 2. Primero divida: 8 ÷ 2."), "b": t("Check the division: 8 ÷ 2 = 4.", "Revise la división: 8 ÷ 2 = 4."), "c": t("Check: 12 − 4 = 8, then 8 + 1.", "Revise: 12 − 4 = 8, después 8 + 1.")}, "solution": t("8 ÷ 2 = 4; 12 − 4 = 8; 8 + 1 = 9.", "8 ÷ 2 = 4; 12 − 4 = 8; 8 + 1 = 9.")},
      "D": {"ok": "b", "hints": {"a": t("The parentheses go first: 2 + 3 = 5.", "El paréntesis va primero: 2 + 3 = 5."), "c": t("5<sup>2</sup> = 25, not 10.", "5<sup>2</sup> = 25, no 10."), "d": t("You still need to subtract 1.", "Todavía falta restar 1.")}, "solution": t("(2 + 3) = 5; 5<sup>2</sup> = 25; 25 − 1 = 24.", "(2 + 3) = 5; 5<sup>2</sup> = 25; 25 − 1 = 24.")},
      "E": {"ok": "a", "hints": {"b": t("Start inside the parentheses: 1 + 2 = 3.", "Empiece dentro del paréntesis: 1 + 2 = 3."), "c": t("Check the brackets: 5 × 3 = 15, then 15 − 4.", "Revise el corchete: 5 × 3 = 15, después 15 − 4."), "d": t("Finish the brackets before you multiply by 2.", "Termine el corchete antes de multiplicar por 2.")}, "solution": t("(1 + 2) = 3; [5 × 3 − 4] = 15 − 4 = 11; 2 × 11 = 22.", "(1 + 2) = 3; [5 × 3 − 4] = 15 − 4 = 11; 2 × 11 = 22.")},
      "F": {"ok": "c", "hints": {"a": t("Start with the innermost: (9 − 5) = 4.", "Empiece por el más interior: (9 − 5) = 4."), "b": t("Check the brackets: 2 × 4 = 8.", "Revise el corchete: 2 × 4 = 8."), "d": t("Check the braces: 3 + 8 = 11, then 40 − 11.", "Revise la llave: 3 + 8 = 11, después 40 − 11.")}, "solution": t("(9 − 5) = 4; [2 × 4] = 8; {3 + 8} = 11; 40 − 11 = 29.", "(9 − 5) = 4; [2 × 4] = 8; {3 + 8} = 11; 40 − 11 = 29.")},
      "G": {"ok": "d", "hints": {"a": t("Multiplication and division share a level: neither always goes first.", "La multiplicación y la división comparten nivel: ninguna va siempre primero."), "b": t("Addition and subtraction come last.", "La suma y la resta van al final."), "c": t("Exponents come after grouping symbols, not before.", "Los exponentes van después de los agrupadores, no antes.")}, "solution": t("Grouping symbols first, then exponents and roots, then multiplication and division (left to right), then addition and subtraction (left to right).", "Primero los agrupadores, después exponentes y raíces, después multiplicación y división (de izquierda a derecha) y al final suma y resta (de izquierda a derecha).")},
      "H": {"ok": "b", "hints": {"a": t("You added 6 + 4 first. Inside the parentheses, multiply first: 4 × 3.", "Sumó 6 + 4 primero. Dentro del paréntesis, primero se multiplica: 4 × 3."), "c": t("Check: 6 + 12 = 18, then 18 ÷ 2.", "Revise: 6 + 12 = 18, después 18 ÷ 2."), "d": t("Finish the parentheses before dividing.", "Termine el paréntesis antes de dividir.")}, "solution": t("(6 + 4 × 3) = 6 + 12 = 18; 18 ÷ 2 = 9.", "(6 + 4 × 3) = 6 + 12 = 18; 18 ÷ 2 = 9.")}
     }}

    quiz = [
     ("A", t("What is 4 + 5 × 3?", "¿Cuánto es 4 + 5 × 3?"), [("a", "27"), ("b", "17"), ("c", "19"), ("d", "60")]),
     ("B", t("What is 20 ÷ 4 × 5?", "¿Cuánto es 20 ÷ 4 × 5?"), [("a", "25"), ("b", "1"), ("c", "10"), ("d", "100")]),
     ("C", t("What is 12 − 8 ÷ 2 + 1?", "¿Cuánto es 12 − 8 ÷ 2 + 1?"), [("a", "3"), ("b", "5"), ("c", "7"), ("d", "9")]),
     ("D", t("What is (2 + 3)<sup>2</sup> − 1?", "¿Cuánto es (2 + 3)<sup>2</sup> − 1?"), [("a", "12"), ("b", "24"), ("c", "9"), ("d", "25")]),
     ("E", t("What is 2 × [5 × (1 + 2) − 4]?", "¿Cuánto es 2 × [5 × (1 + 2) − 4]?"), [("a", "22"), ("b", "18"), ("c", "26"), ("d", "15")]),
     ("F", t("What is 40 − {3 + [2 × (9 − 5)]}?", "¿Cuánto es 40 − {3 + [2 × (9 − 5)]}?"), [("a", "23"), ("b", "33"), ("c", "29"), ("d", "11")]),
     ("G", t("Which order is right?", "¿Qué orden es el correcto?"), [("a", t("Multiplication always before division", "La multiplicación siempre antes que la división")), ("b", t("Addition before multiplication", "La suma antes que la multiplicación")), ("c", t("Exponents before grouping symbols", "Los exponentes antes que los agrupadores")), ("d", t("Grouping, exponents, multiplication and division, addition and subtraction", "Agrupadores, exponentes, multiplicación y división, suma y resta"))]),
     ("H", t("What is (6 + 4 × 3) ÷ 2?", "¿Cuánto es (6 + 4 × 3) ÷ 2?"), [("a", "15"), ("b", "9"), ("c", "12"), ("d", "8")])]

    return B.pagina_leccion(n, 3, t(*TEMA), t(*TIT),
        t("One set of rules so that everyone gets the same answer: the four levels of PEMDAS, step by step, and nested grouping symbols.", "Un solo sistema de reglas para que todos lleguen al mismo resultado: los cuatro niveles de PEMDAS, paso a paso, y los agrupadores anidados."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Name</strong> the four levels of the order of operations (PEMDAS).", "<strong>Nombrar</strong> los cuatro niveles del orden de las operaciones (PEMDAS)."),
         t("<strong>Work</strong> multiplication and division, and addition and subtraction, from left to right.", "<strong>Resolver</strong> la multiplicación y la división, y la suma y la resta, de izquierda a derecha."),
         t("<strong>Solve</strong> an expression step by step, one operation at a time.", "<strong>Resolver</strong> una expresión paso a paso, una operación a la vez."),
         t("<strong>Work</strong> nested parentheses, brackets, and braces from the inside out.", "<strong>Resolver</strong> paréntesis, corchetes y llaves anidados de adentro hacia afuera.")],
        secciones,
        (t("Write and solve five expressions with the four operations (no parentheses), five with parentheses and an exponent, and five with nested grouping symbols. Write one line for each step, and underline the operation you do in that step.",
           "Escriba y resuelva cinco expresiones con las cuatro operaciones (sin paréntesis), cinco con paréntesis y un exponente, y cinco con agrupadores anidados. Escriba una línea por paso y subraye la operación que hace en ese paso."),
         t("Look at a receipt or a bill: 3 items at $4 plus a $5 fee. Write it as one expression, like 3 × 4 + 5, and solve it in the right order. Then check that the bill says the same.",
           "Mire un recibo o una factura: 3 artículos de $4 más un cargo de $5. Escríbalo como una sola expresión, como 3 × 4 + 5, y resuélvala en el orden correcto. Después compruebe que la factura dice lo mismo.")),
        quiz,
        t("Self-check checklist for the order of operations", "Lista de autoevaluación del orden de las operaciones"),
        t("Self-check checklist: skills for the order of operations", "Lista de autoevaluación: destrezas del orden de las operaciones"),
        [(t("The four levels", "Los cuatro niveles"), t("I know them and I know that M and D (and A and S) share a level.", "Los conozco y sé que la M y la D (y la A y la S) comparten nivel."), t("I know the order, but I put M before D.", "Conozco el orden, pero pongo la M antes que la D."), t("I work from left to right without looking at the operations.", "Resuelvo de izquierda a derecha sin mirar las operaciones.")),
         (t("Step by step", "Paso a paso"), t("I copy the expression at each step and make no mistakes.", "Copio la expresión en cada paso y no me equivoco."), t("I get it right, but I skip steps and sometimes slip.", "Acierto, pero me salto pasos y a veces me equivoco."), t("I try to do everything at once.", "Intento hacerlo todo a la vez.")),
         (t("Nested grouping symbols", "Agrupadores anidados"), t("I work from the inside out with three levels.", "Resuelvo de adentro hacia afuera con tres niveles."), t("I can do two levels, but three confuse me.", "Puedo con dos niveles, pero tres me confunden."), t("I do not know where to start.", "No sé por dónde empezar.")),
         (t("Everything together", "Todo junto"), t("I use PEMDAS inside each grouping symbol and finish it before moving on.", "Aplico PEMDAS dentro de cada agrupador y lo termino antes de seguir."), t("I sometimes jump out of a grouping symbol too soon.", "A veces salgo de un agrupador antes de tiempo."), t("I mix up the levels.", "Mezclo los niveles."))],
        t("<p>You now have the system that puts everything in order: the four levels of PEMDAS, step by step, and grouping symbols from the inside out.</p>\n<p>In <strong>Lesson 3.2 · PEMDAS with powers, roots, fractions, and signs</strong> you will add the rest of the tools of Level 2: square roots and fraction bars that work like hidden parentheses, and negative numbers with exponents.</p>",
          "<p>Ya tiene el sistema que pone todo en orden: los cuatro niveles de PEMDAS, paso a paso, y los agrupadores de adentro hacia afuera.</p>\n<p>En la <strong>Lección 3.2 · PEMDAS con potencias, raíces, fracciones y signos</strong> sumará el resto de las herramientas del Nivel 2: las raíces y las barras de fracción, que funcionan como paréntesis escondidos, y los números negativos con exponentes.</p>"),
        ("3-2", ("", t("Lesson 3.2 · PEMDAS with powers, roots, fractions, and signs", "Lección 3.2 · PEMDAS con potencias, raíces, fracciones y signos"))),
        [(t("order of operations", "orden de las operaciones"), t("The rules that say which operation to do first, so everyone gets the same answer.", "Las reglas que dicen qué operación se hace primero, para que todos lleguen al mismo resultado.")),
         ("PEMDAS", t("Parentheses, Exponents, Multiplication and Division, Addition and Subtraction.", "Paréntesis, Exponentes, Multiplicación y División, Adición y Sustracción.")),
         (t("grouping symbols", "agrupadores"), t("Parentheses ( ), brackets [ ], and braces { }. What is inside goes first.", "Paréntesis ( ), corchetes [ ] y llaves { }. Lo que está dentro va primero.")),
         (t("nested", "anidado"), t("One grouping symbol inside another. Work from the inside out.", "Un agrupador dentro de otro. Se resuelve de adentro hacia afuera.")),
         (t("left to right", "de izquierda a derecha"), t("The way to work two operations on the same level.", "La forma de resolver dos operaciones del mismo nivel."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "primeroQ": "In {e}, what do you solve first?", "primeroVa": "First comes {x}. ",
  "pistaPrimero": "Look for grouping symbols first, then exponents, then multiplication and division from left to right.",
  "pistaIzq": "It looks like you worked from left to right without the order: multiplication and division come before addition and subtraction.",
  "emojiIntro": "Find the value of each emoji from the clues. Then solve the last line in the right order.",
  "pista1a": "{e} + {e} + {e} = {r}, so 3 × {e} = {r} and {e} = {r} ÷ 3 = {v}.", "pista1b": "{e} × 3 = {r}, so {e} = {r} ÷ 3 = {v}.",
  "pista2a": "{e} + {k} + {e} = {r}. Since {k} = {kv}, 2 × {e} = {r} − {kv} = {d}, and {e} = {v}.",
  "pista2b": "{e} × 2 + {k} = {r}. Since {k} = {kv}, {e} × 2 = {r} − {kv} = {d}, and {e} = {v}.",
  "pista2c": "({e} + {k}) × 2 = {r}. So {e} + {k} = {h}; since {k} = {kv}, {e} = {v}.",
  "pista3a": "{e} + {e} + {k} = {r}. Since {k} = {kv}, 2 × {e} = {d}, and {e} = {v}.",
  "pista3b": "{e} × {k} = {r}. Since {k} = {kv}, {e} = {r} ÷ {kv} = {v}.",
  "pista3c": "{e} × 3 − {k} = {r}. Since {k} = {kv}, {e} × 3 = {d}, and {e} = {v}.",
  "valores": "The values: {l}.", "final": "The last line: {e} = {s}. ",
  "pistaEmoji": "First find each emoji from its clue. Then, in the last line, use PEMDAS: multiply and divide before you add and subtract."
 },
 "es": {
  "primeroQ": "En {e}, ¿qué se resuelve primero?", "primeroVa": "Primero va {x}. ",
  "pistaPrimero": "Busque primero los agrupadores, después los exponentes y luego la multiplicación y la división de izquierda a derecha.",
  "pistaIzq": "Parece que resolvió de izquierda a derecha sin respetar el orden: la multiplicación y la división van antes que la suma y la resta.",
  "emojiIntro": "Halle el valor de cada emoji con las pistas. Después resuelva la última línea en el orden correcto.",
  "pista1a": "{e} + {e} + {e} = {r}, así que 3 × {e} = {r} y {e} = {r} ÷ 3 = {v}.", "pista1b": "{e} × 3 = {r}, así que {e} = {r} ÷ 3 = {v}.",
  "pista2a": "{e} + {k} + {e} = {r}. Como {k} = {kv}, 2 × {e} = {r} − {kv} = {d}, y {e} = {v}.",
  "pista2b": "{e} × 2 + {k} = {r}. Como {k} = {kv}, {e} × 2 = {r} − {kv} = {d}, y {e} = {v}.",
  "pista2c": "({e} + {k}) × 2 = {r}. Entonces {e} + {k} = {h}; como {k} = {kv}, {e} = {v}.",
  "pista3a": "{e} + {e} + {k} = {r}. Como {k} = {kv}, 2 × {e} = {d}, y {e} = {v}.",
  "pista3b": "{e} × {k} = {r}. Como {k} = {kv}, {e} = {r} ÷ {kv} = {v}.",
  "pista3c": "{e} × 3 − {k} = {r}. Como {k} = {kv}, {e} × 3 = {d}, y {e} = {v}.",
  "valores": "Los valores: {l}.", "final": "La última línea: {e} = {s}. ",
  "pistaEmoji": "Primero halle cada emoji con su pista. Después, en la última línea, aplique PEMDAS: multiplique y divida antes de sumar y restar."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
var OPS = ["+", "−", "×", "÷"];
function n(a, b){ return nA(a, b); }
function op(l){ return elige(l || OPS); }
/* Expressions with no nesting */
function fabSimple(){
  var tipo = aleatorio(1, 5);
  if (tipo === 1) return [n(), op(["+", "−"]), n(), op(["×", "÷"]), n(), op(["+", "−"]), n()];
  if (tipo === 2) return [n(2, 40), "÷", n(2, 9), "×", n()];
  if (tipo === 3) return [G("(", [n(), op(["+", "−"]), n()]), "×", n(), op(["+", "−"]), n()];
  if (tipo === 4) return [Pw(G("(", [n(2, 9), op(["+", "−"]), n(1, 6)]), 2), op(["+", "−"]), n(2, 40), "÷", n(2, 9)];
  return [n(), op(["+", "−"]), n(), "×", G("(", [n(), op(["+", "−"]), n()])];
}
/* Two or three levels of grouping symbols */
function fabAnidada(){
  var tipo = aleatorio(1, 5);
  if (tipo === 1) return [n(2, 9), "×", G("[", [n(), "+", G("(", [n(), op(), n()])])];
  if (tipo === 2) return [n(30, 90), "−", G("{", [n(), "+", G("[", [n(2, 6), "×", G("(", [n(), "−", n()])])])];
  if (tipo === 3) return [G("[", [G("(", [n(), "+", n()]), "×", n(2, 6), "−", n()]), "÷", n(2, 9)];
  if (tipo === 4) return [G("{", [n(), "+", G("[", [n(2, 6), "×", G("(", [n(), "−", n()]), "−", n()])]), "÷", n(2, 6)];
  return [n(), "+", G("[", [n(10, 60), "÷", G("(", [n(), "−", n()]), "+", n()]), "×", n(2, 5)];
}
function fabCombinada(){
  var tipo = aleatorio(1, 4);
  if (tipo === 1) return [Pw(G("(", [n(2, 9), "−", n(1, 5)]), 2), "÷", n(2, 9), "+", G("[", [n(), "×", G("(", [n(), "−", n()])])];
  if (tipo === 2) return [n(20, 99), "−", n(2, 6), "×", G("[", [n(), "+", G("(", [n(10, 40), "÷", n(2, 9)])])];
  if (tipo === 3) return [G("{", [n(2, 5), "×", G("[", [Pw(n(2, 5), 2), "−", G("(", [n(), "+", n()])])]), "+", n()];
  return [n(), "×", n(), "−", G("[", [n(10, 50), "÷", G("(", [n(2, 9), "−", n(1, 6)]), "×", n(2, 4)])];
}
/* Level 2 Topic 3 starts with whole numbers: no negative numbers on the way */
function sinNeg(R){ return R.res >= 0 && R.pasos.length >= 2 && R.pasos.every(function(p){ return !hayNeg(p.despues); }); }

/* ============ MODULE 1 · what goes first? ============ */
function genPrimero(){
  for (var k = 0; k < 200; k++){
    var e = norm(generaExacta(Math.random() < 0.5 ? fabSimple : fabAnidada, 400, sinNeg).e), ok = primerSitio(e), s = sitios(e);
    var extras = []; e.forEach(function(x, i){ if (i % 2 === 0 && (x.t === "p" || x.t === "g")) extras.push(rTerm(x, i > 0)); });
    s = s.concat(extras).filter(function(x, i, a){ return a.indexOf(x) === i && x !== ok; });
    if (!ok || s.length < 2) continue;
    var o = [{ html: ok, clave: "ok" }].concat(baraja(s).slice(0, 3).map(function(x, i){ return { html: x, clave: "m" + i }; }));
    var R = resolver(e);
    return { enun: F(TXT.primeroQ, { e: exprHTML(e) }), opciones: o, correcta: "ok", pista: TXT.pistaPrimero, bien: R.pasos[0].desc, mal: F(TXT.primeroVa, { x: ok }) + R.pasos[0].desc };
  }
}

/* ============ MODULE 5 · emoji challenges ============ */
var EMOJIS = ["🍎", "🍌", "🍊", "🍇", "🍓", "🥝", "🍒", "🍍", "🐱", "🐶", "🐰", "🦊", "🐻", "🐼", "🐸", "🌻", "🌷", "⭐", "🌙", "🌈", "🔥", "💎", "🎈", "🎁", "🏆", "🎯"];
function emo(x){ return '<span class="emo">' + x + '</span>'; }
function genEmoji(){
  var em = baraja(EMOJIS).slice(0, 3), A = emo(em[0]), Bm = emo(em[1]), C = emo(em[2]);
  var a = aleatorio(2, 12), b = aleatorio(2, 10), c = aleatorio(2, 9), pistas = [], expl = [];
  var t1 = aleatorio(1, 2);
  if (t1 === 1){ pistas.push(A + " + " + A + " + " + A + " = " + 3 * a); expl.push(F(TXT.pista1a, { e: A, r: 3 * a, v: a })); }
  else { pistas.push(A + " × 3 = " + 3 * a); expl.push(F(TXT.pista1b, { e: A, r: 3 * a, v: a })); }
  var t2 = aleatorio(1, 3);
  if (t2 === 1){ pistas.push(Bm + " + " + A + " + " + Bm + " = " + (2 * b + a)); expl.push(F(TXT.pista2a, { e: Bm, k: A, r: 2 * b + a, kv: a, d: 2 * b, v: b })); }
  else if (t2 === 2){ pistas.push(Bm + " × 2 + " + A + " = " + (2 * b + a)); expl.push(F(TXT.pista2b, { e: Bm, k: A, r: 2 * b + a, kv: a, d: 2 * b, v: b })); }
  else { pistas.push("(" + Bm + " + " + A + ") × 2 = " + 2 * (a + b)); expl.push(F(TXT.pista2c, { e: Bm, k: A, r: 2 * (a + b), h: a + b, kv: a, v: b })); }
  var t3 = aleatorio(1, 3);
  if (t3 === 1){ pistas.push(C + " + " + C + " + " + Bm + " = " + (2 * c + b)); expl.push(F(TXT.pista3a, { e: C, k: Bm, r: 2 * c + b, kv: b, d: 2 * c, v: c })); }
  else if (t3 === 2){ pistas.push(C + " × " + Bm + " = " + c * b); expl.push(F(TXT.pista3b, { e: C, k: Bm, r: c * b, kv: b, v: c })); }
  else { pistas.push(C + " × 3 − " + Bm + " = " + (3 * c - b)); expl.push(F(TXT.pista3c, { e: C, k: Bm, r: 3 * c - b, kv: b, d: 3 * c, v: c })); }
  /* the last line: always needs the order of operations */
  var formas = [
    [[N(a), "+", N(b), "×", N(c)], A + " + " + Bm + " × " + C],
    [[N(a), "×", N(b), "−", N(c)], A + " × " + Bm + " − " + C],
    [[N(a * c), "÷", N(c), "+", N(b)], null],
    [[N(b), "+", N(a), "×", N(c), "−", N(b)], Bm + " + " + A + " × " + C + " − " + Bm],
    [[G("(", [N(a), "+", N(b)]), "×", N(c)], "(" + A + " + " + Bm + ") × " + C]];
  var f = elige(formas.filter(function(x){ return x[1]; }));
  var R = resolver(f[0]), pist = pistasErrores(f[0], R.res, ["izqder"]);
  var enun = '<p class="nota" style="margin-top:0">' + TXT.emojiIntro + '</p><div class="retos">' + pistas.map(function(x){ return '<div class="reto-linea">' + x + '</div>'; }).join("") + '<div class="reto-linea reto-final">' + f[1] + ' = ❓</div></div>';
  var sol = expl.join(" ") + " " + F(TXT.valores, { l: em[0] + " = " + a + ", " + em[1] + " = " + b + ", " + em[2] + " = " + c }) + " " + F(TXT.final, { e: f[1], s: rLista(f[0]) }) + R.pasos.map(function(p){ return p.desc; }).join(" ");
  return { enun: enun, correcta: String(R.res), solucion: sol, evalua: numE(R.res, pist, TXT.pistaEmoji) };
}

/* ============ Start ============ */
creaPracticaOM("p1", genPrimero);
stepper("pp", fabSimple, [[N(6), "+", N(3), "×", N(4), "−", N(2)], [Pw(G("(", [N(8), "−", N(3)]), 2), "+", N(12), "÷", N(4)]], sinNeg);
creaPracticaLibre("p2", practicaDe(fabSimple, sinNeg, ["izqder", "potmul"]));
stepper("an", fabAnidada, [[N(2), "×", G("[", [N(3), "+", G("(", [N(4), "×", N(2)])])], [N(50), "−", G("{", [N(4), "+", G("[", [N(3), "×", G("(", [N(6), "−", N(2)])])])]], sinNeg);
creaPracticaLibre("p3", practicaDe(fabAnidada, sinNeg, ["izqder"]));
creaPracticaLibre("p4", practicaDe(fabCombinada, sinNeg, ["izqder", "potmul"]));
creaPracticaLibre("p5", genEmoji);
'''

def practica_pagina():
    n = N
    nota_n = t("Type only the number.", "Escriba solo el número.")
    def libre_n(pid, titulo):
        return B.libre_e(pid, titulo).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota_n)
    mods = [
     (t("pyramid", "piramide"), t("The four levels of priority", "La pirámide de prioridades"),
      f'''      <table class="reglas">
        <caption>{t("The four levels of PEMDAS", "Los cuatro niveles de PEMDAS")}</caption>
        <thead><tr><th scope="col">{t("Level", "Nivel")}</th><th scope="col">{t("What you do", "Qué se hace")}</th></tr></thead>
        <tbody>
          <tr><td>1 · P</td><td>{t("grouping symbols: ( ), [ ], { }, from the inside out", "agrupadores: ( ), [ ], { }, de adentro hacia afuera")}</td></tr>
          <tr><td>2 · E</td><td>{t("exponents and roots", "exponentes y raíces")}</td></tr>
          <tr><td>3 · MD</td><td>{t("multiplication and division, from left to right", "multiplicación y división, de izquierda a derecha")}</td></tr>
          <tr><td>4 · AS</td><td>{t("addition and subtraction, from left to right", "suma y resta, de izquierda a derecha")}</td></tr>
        </tbody>
      </table>
      <div class="caja-atencion"><strong>{t("Six letters, four levels.", "Seis letras, cuatro niveles.")}</strong> {t("M and D share a level, and so do A and S. In 20 ÷ 4 × 5, divide first because it is farther left.", "La M y la D comparten nivel, y también la A y la S. En 20 ÷ 4 × 5 se divide primero por estar más a la izquierda.")}</div>
{B.om("p1", t("Practice: what goes first?", "Practique: ¿qué va primero?"))}'''),
     (t("step-by-step", "paso-a-paso"), t("Step by step", "Aplicación paso a paso"),
      f'''      <p>{t("Copy the expression at every step and solve only the operation with the highest priority. The operation you are working on is marked.", "Copie la expresión en cada paso y resuelva solo la operación de mayor prioridad. La operación que se resuelve aparece marcada.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos_panel("pp", t("Another expression", "Otra expresión"))}
{libre_n("p2", t("Practice: solve", "Practique: resolver"))}'''),
     (t("nested", "anidados"), t("Nested grouping symbols", "Paréntesis anidados"),
      f'''      <p>{t("Work from the <strong>innermost</strong> grouping symbol to the outermost. Each kind has its own color: <span class=\"n1\">( )</span> parentheses, <span class=\"n2\">[ ]</span> brackets, <span class=\"n3\">{ }</span> braces.", "Se resuelve del agrupador <strong>más interior</strong> al más exterior. Cada tipo tiene su color: <span class=\"n1\">( )</span> paréntesis, <span class=\"n2\">[ ]</span> corchetes, <span class=\"n3\">{ }</span> llaves.")}</p>
      <h3>{t("From the inside out", "Del interior hacia el exterior")}</h3>
{pasos_panel("an", t("Another expression", "Otra expresión"))}
{libre_n("p3", t("Practice: nested grouping symbols", "Practique: agrupadores anidados"))}'''),
     (t("combined", "combinado"), t("Everything combined", "Todo combinado"),
      f'''      <p>{t("Grouping symbols first, from the inside out; inside each one, use PEMDAS from the start. Finish each grouping symbol before you move on.", "Primero los agrupadores, de adentro hacia afuera; dentro de cada uno, PEMDAS desde el principio. Termine cada agrupador antes de seguir.")}</p>
{libre_n("p4", t("Practice: combined expressions", "Practique: expresiones combinadas"))}'''),
     (t("emoji-challenges", "retos"), t("Emoji challenges", "Retos con emojis"),
      f'''      <p>{t("Each emoji stands for a whole number. Use the first three lines to find each one, and then solve the last line. The last line always needs the order of operations.", "Cada emoji representa un número entero. Use las tres primeras líneas para hallar cada uno y después resuelva la última. La última línea siempre necesita el orden de las operaciones.")}</p>
{libre_n("p5", t("Practice: emoji challenge", "Practique: reto con emojis"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    estilo = ".retos{margin:8px 0;}\n.reto-linea{font-size:24px;line-height:1.6;margin:4px 0;}\n.reto-final{border-top:2px dashed var(--tema-bg2);padding-top:6px;margin-top:8px;}\n.emo{font-size:28px;}"
    return B.pagina_practica(n, 3, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=estilo, scripts=("/math/integers.js", "/math/pemdas.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Orden de operaciones: repaso y paréntesis anidados")
