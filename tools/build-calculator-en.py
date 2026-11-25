"""Builds the English LearnGED version of the TI-30XS simulator (calculadora-gph.js).
Usage: python3 tools/build-calculator-en.py <algebra/calculadora-gph.js> js/calculator.js tools/calculator-guide-en.js
Every replacement must match exactly once (or the number given), so nothing is missed silently."""
import sys, re

src = open(sys.argv[1], encoding="utf-8").read()

def rep(old, new, count=1):
    global src
    n = src.count(old)
    if n != count:
        sys.exit(f"Expected {count} match(es), found {n}: {old[:80]!r}")
    src = src.replace(old, new)

def lit(old, new, count=1):
    rep("'" + old + "'", "'" + new + "'", count)

def litall(old, new):
    n = src.count("'" + old + "'")
    if n < 1:
        sys.exit(f"Not found: {old[:80]!r}")
    lit(old, new, n)

# ---------- Header ----------
rep(" * Calculadora GPH v2.3 — simulador de la TI-30XS MultiView™ — GEDparaHispanos",
    " * LearnGED calculator v2.3 (English) — TI-30XS MultiView™ simulator — LearnGED\n * English build of calculadora-gph.js (GEDparaHispanos).")
rep("https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es", "https://creativecommons.org/licenses/by-nc-sa/4.0/")
rep(" *   <script src=\"https://zhemaria.github.io/algebra/calculadora-gph.js\" defer></script>", " *   <script src=\"/js/calculator.js\" defer></script>   (LearnGED, English)")

# ---------- Error messages ----------
for es, en, c in [
    ("División entre cero", "Division by zero", 4),
    ("Raíz cuadrada de un número negativo", "Square root of a negative number", 2),
    ("Operación no válida", "Not a valid operation", 1),
    ("Número demasiado grande", "Number too large", 4),
    ("0 elevado a 0 no está definido", "0 to the power 0 is not defined", 2),
    ("Raíz par de un número negativo", "Even root of a negative number", 2),
    ("Base negativa con exponente decimal", "Negative base with a decimal exponent", 1),
    ("El índice de la raíz no puede ser 0", "The index of the root cannot be 0", 1),
    ("El factorial solo se aplica a enteros no negativos", "Factorial only works with whole numbers that are not negative", 1),
    ("nPr necesita números enteros no negativos", "nPr needs whole numbers that are not negative", 2),
    ("En nPr, el segundo número no puede ser mayor que el primero", "In nPr, the second number cannot be greater than the first", 1),
    ("nCr necesita números enteros no negativos", "nCr needs whole numbers that are not negative", 2),
    ("En nCr, el segundo número no puede ser mayor que el primero", "In nCr, the second number cannot be greater than the first", 1),
    ("El logaritmo solo existe para números positivos", "Logarithms exist only for positive numbers", 2),
    ("La tangente no existe para ese ángulo", "The tangent does not exist for that angle", 2),
    ("sin⁻¹ solo acepta valores entre −1 y 1", "sin⁻¹ accepts only values from −1 to 1", 1),
    ("cos⁻¹ solo acepta valores entre −1 y 1", "cos⁻¹ accepts only values from −1 to 1", 1),
    ("Error de sintaxis", "Syntax error", None),
    ("cosh⁻¹ solo acepta valores mayores o iguales que 1", "cosh⁻¹ accepts only values of 1 or more", 1),
    ("tanh⁻¹ solo acepta valores entre −1 y 1", "tanh⁻¹ accepts only values between −1 and 1", 1),
    ("randint( necesita dos números enteros", "randint( needs two whole numbers", 1),
    ("Las frecuencias deben ser números enteros no negativos", "Frequencies must be whole numbers that are not negative", 2),
    ("La lista de datos está vacía", "The data list is empty", 1),
    ("La lista de datos y la de frecuencias no tienen la misma cantidad de valores", "The data list and the frequency list do not have the same number of values", 1),
    ("No hay datos para calcular", "There is no data to calculate", 1),
    ("Una de las listas de datos está vacía", "One of the data lists is empty", 1),
    ("Las listas no tienen la misma cantidad de valores", "The lists do not have the same number of values", 1),
    ("Se necesitan al menos dos pares de datos", "You need at least two pairs of data", 1),
    ("Falta un número", "A number is missing", 1),
    ("Número mal escrito: tiene más de un punto decimal", "Number typed wrong: it has more than one decimal point", 1),
    ("Después de sto→ va una variable, al final del cálculo", "After sto→ comes a variable, at the end of the calculation", 1),
    ("La conversión debe ir al final del cálculo", "The conversion must go at the end of the calculation", 1),
    ("En un número mixto, la fracción no puede ser negativa", "In a mixed number, the fraction cannot be negative", 1),
    ("Número mixto incompleto: entero, u, numerador, / y denominador", "Mixed number not complete: whole number, u, numerator, /, and denominator", 1),
    ("Fracción incompleta: numerador / denominador", "Fraction not complete: numerator / denominator", 1),
    ("Notación científica incompleta: número E exponente", "Scientific notation not complete: number E exponent", 1),
    ("Escribe el número antes de °, \\' o \"", "Type the number before °, \\' or \"", 1),
    ("La tecla (−) es para números negativos. Para restar usa la tecla −", "The (−) key is for negative numbers. To subtract, use the − key", 1),
    ("Esta función necesita dos números separados por una coma (2nd .)", "This function needs two numbers separated by a comma (2nd .)", 1),
    ("La coma solo se usa dentro de funciones como randint(", "The comma is used only inside functions like randint(", 1),
    ("Sobra un paréntesis de cierre", "There is an extra closing parenthesis", 2),
    ("Para un número negativo usa la tecla (−), no la resta −", "For a negative number, use the (−) key, not the subtraction key −", 1),
    ("Falta el número antes de esta operación", "The number before this operation is missing", 1),
    ("Escribe primero el número n y después nPr o nCr", "Type the number n first, then nPr or nCr", 1),
    ("Falta el número antes de esta tecla", "The number before this key is missing", 1),
    ("Después de sto→ pulsa la tecla de variables para elegir dónde guardar", "After sto→, press the variable key to choose where to store", 1),
    ("Error de cálculo", "Calculation error", 2),
    ("No se pudo calcular", "Could not calculate", 1),
]:
    if c is None:
        lit(es, en, src.count("'" + es + "'"))
    else:
        lit(es, en, c)

# ---------- Spoken results (screen readers) ----------
lit(" por 10 a la ", " times 10 to the ", 2)
rep("' grados ' + m + ' minutos ' + quitarCeros(String(sg)) + ' segundos'", "' degrees ' + m + ' minutes ' + quitarCeros(String(sg)) + ' seconds'")
lit(" por ciento", " percent", 1)
lit("raíz de ", "square root of ", 1)
lit("menos ", "minus ", 2)
lit(" sobre ", " over ", 6)
lit(" y ", " and ", 2)
rep("anunciar('Resultado: '", "anunciar('Result: '")
rep("anunciar('Error: ' + e.message)", "anunciar('Error: ' + e.message)")

# ---------- Key descriptions [id, label, 2nd label, class, description, 2nd description] ----------
for es, en in [
    ("Tecla 2nd: activa la función verde de la siguiente tecla", "2nd key: turns on the green function of the next key"),
    ("mode: menú de modos", "mode: modes menu"), ("quit: salir del menú", "quit: leave the menu"),
    ("delete: borrar", "delete"), ("insert: insertar", "insert"),
    ("log: logaritmo base 10", "log: base-10 logarithm"), ("diez elevado a", "ten to the power"),
    ("prb: menú de probabilidad (nPr, nCr, factorial)", "prb: probability menu (nPr, nCr, factorial)"),
    ("angle: menú de ángulos", "angle: angles menu"), ("data: editor de datos", "data: data editor"), ("stat: estadística", "stat: statistics"),
    ("ln: logaritmo natural", "ln: natural logarithm"), ("e elevado a", "e to the power"),
    ("n/d: fracción", "n/d: fraction"), ("U n/d: número mixto", "U n/d: mixed number"),
    ("por diez elevado a: notación científica", "times ten to the power: scientific notation"),
    ("table: tabla de valores", "table: table of values"), ("f◂▸d: convertir entre fracción y decimal", "f◂▸d: change between fraction and decimal"),
    ("clear: borrar", "clear"), ("hyp: funciones hiperbólicas", "hyp: hyperbolic functions"),
    ("seno", "sine"), ("seno inverso", "inverse sine"), ("coseno", "cosine"), ("coseno inverso", "inverse cosine"),
    ("tangente", "tangent"), ("tangente inversa", "inverse tangent"),
    ("entre (división)", "divided by (division)"), ("K: constante", "K: constant"),
    ("elevar a una potencia", "raise to a power"), ("raíz con índice", "root with an index"),
    ("recíproco", "reciprocal"), ("n/d◂▸Un/d: convertir entre fracción y número mixto", "n/d◂▸Un/d: change between fraction and mixed number"),
    ("abrir paréntesis", "open parenthesis"), ("cerrar paréntesis", "close parenthesis"),
    ("expresar como por ciento", "show as a percent"), ("por (multiplicación)", "times (multiplication)"),
    ("al cuadrado", "squared"), ("raíz cuadrada", "square root"), ("menos (resta)", "minus (subtraction)"),
    ("recall: recuperar variable", "recall: get a variable"), ("más (suma)", "plus (addition)"),
    ("sto: guardar en variable", "sto: store in a variable"), ("clear var: borrar variables", "clear var: clear the variables"),
    ("tecla toggle: alternar el resultado entre fracción y decimal", "toggle key: switch the answer between fraction and decimal"),
    ("aproximar: resultado decimal", "approximate: decimal answer"),
    ("off: apagar y cerrar la calculadora", "off: turn off and close the calculator"),
    ("reset: restablecer la calculadora", "reset: reset the calculator"),
    ("punto decimal", "decimal point"), ("coma", "comma"), ("número negativo", "negative number"),
    ("ans: respuesta anterior", "ans: last answer"), ("enter: calcular", "enter: calculate"),
]:
    lit(es, en, src.count("'" + es + "'"))
lit("por ciento", "percent", 1)
lit("variables", "variables", src.count("'variables'"))

# ---------- Notices and menus ----------
for es, en in [
    ("La entrada ya está llena.", "The entry line is full."),
    ("La constante K debe empezar con una operación, por ejemplo + 3 o × 2", "The constant K must start with an operation, for example + 3 or × 2"),
    ("Constante K guardada: ahora escribe un número y pulsa enter para aplicarle la operación. 2nd K la desactiva.", "Constant K stored: now type a number and press enter to apply the operation. 2nd K turns it off."),
    ("Este resultado ya está convertido; pulsa enter con otro cálculo.", "This answer is already converted; press enter with another calculation."),
    ("Este resultado no tiene otra forma: solo se muestra como decimal o entero.", "This answer has no other form: it shows only as a decimal or a whole number."),
    ("Variables borradas: x, y, z, t, a, b y c valen 0.", "Variables cleared: x, y, z, t, a, b, and c are 0."),
    ("Las fórmulas en las listas estarán disponibles más adelante. Por ahora escribe los datos uno por uno.", "Formulas in lists will come later. For now, type the data one by one."),
    ("Menú de probabilidad: 1 nPr, 2 nCr, 3 factorial", "Probability menu: 1 nPr, 2 nCr, 3 factorial"),
    ("Menú de modos", "Modes menu"),
    ("Restablecer la calculadora: 1 No, 2 Sí", "Reset the calculator: 1 No, 2 Yes"),
    ("Menú de ángulos", "Angles menu"), ("Recuperar variable", "Recall a variable"),
    ("Borrar variables: 1 Sí, 2 No", "Clear variables: 1 Yes, 2 No"), ("Menú para borrar listas", "Menu to clear lists"),
    ("Menú de estadística: 1 una variable, 2 dos variables, 3 resultados", "Statistics menu: 1 one variable, 2 two variables, 3 results"),
    ("Menú", "Menu"),
    ("Modo CLASSIC: todo se escribe en una sola línea, por ejemplo 3 n/d 4 se ve 3/4 y el exponente se escribe después de ^ sin plantilla.", "CLASSIC mode: everything is typed on one line. For example, 3 n/d 4 shows as 3/4, and the exponent is typed after ^ with no template."),
    (" seleccionado", " selected"),
    ("Calculadora restablecida.", "Calculator reset."),
    ("Se borraron las tres listas.", "All three lists were cleared."),
    ("Se borró la lista L", "List L"),
    ("Resultados de ", "Results for "), ("una variable", "one variable"), ("dos variables", "two variables"),
    (" calculados. Usa las flechas para leerlos.", " are ready. Use the arrows to read them."),
    ("Todavía no hay resultados: primero calcula 1-Var Stats o 2-Var Stats.", "There are no results yet: first calculate 1-Var Stats or 2-Var Stats."),
    ("Falta el valor de ", "The value is missing for "),
    ("Escribe la función f(x) usando la tecla de variables para la x.", "Type the function f(x), using the variable key for x."),
    ("la coma", "the comma"),
    ("La calculadora siempre inserta lo que escribes donde está el cursor.", "The calculator always inserts what you type where the cursor is."),
    ("2nd activada", "2nd on"), ("2nd desactivada", "2nd off"),
    ("hyp activada: la próxima sin, cos o tan será hiperbólica", "hyp on: the next sin, cos, or tan will be hyperbolic"),
    ("hyp desactivada", "hyp off"),
    ("Constante K: escribe la operación que se repetirá (por ejemplo + 3 o × 2) y pulsa enter.", "Constant K: type the operation to repeat (for example + 3 or × 2) and press enter."),
]:
    lit(es, en, src.count("'" + es + "'"))
rep("'List L' + (i + 1) + '.'", "'List L' + (i + 1) + ' was cleared.'")

rep("avisar('Cada lista admite hasta ' + MAX_LISTA + ' datos.')", "avisar('Each list holds up to ' + MAX_LISTA + ' values.')")

# ---------- Hints shown under the screen ----------
for es, en in [
    ("<b>Numerador.</b> Pulsa ▼ para bajar al denominador.", "<b>Numerator.</b> Press ▼ to go down to the denominator."),
    ("<b>Denominador.</b> Pulsa ► para salir de la fracción.", "<b>Denominator.</b> Press ► to leave the fraction."),
    ("<b>Número entero.</b> Pulsa ► para pasar al numerador.", "<b>Whole number.</b> Press ► to move to the numerator."),
    ("<b>Denominador.</b> Pulsa ► para salir del número mixto.", "<b>Denominator.</b> Press ► to leave the mixed number."),
    ("<b>Exponente.</b> Pulsa ► para salir del exponente.", "<b>Exponent.</b> Press ► to leave the exponent."),
    ("<b>Exponente de 10.</b> Pulsa ► para salir.", "<b>Exponent of 10.</b> Press ► to leave it."),
    ("<b>Dentro de la raíz.</b> Pulsa ► para salir de la raíz.", "<b>Inside the root.</b> Press ► to leave the root."),
    ("<b>Índice de la raíz</b> (2, 3…). Pulsa ► para pasar al número.", "<b>Index of the root</b> (2, 3…). Press ► to move to the number."),
    ("<b>Dentro de la raíz.</b> Pulsa ► para salir.", "<b>Inside the root.</b> Press ► to leave it."),
    ("<b>Exponente de e.</b> Pulsa ► para salir.", "<b>Exponent of e.</b> Press ► to leave it."),
    (".</b> Pulsa clear para volver y corregirlo.", ".</b> Press clear to go back and fix it."),
    ("<b>2nd activa:</b> la próxima tecla hace la función escrita en verde encima de ella.", "<b>2nd is on:</b> the next key does the function written in green above it."),
    ("<b>hyp activa:</b> pulsa sin, cos o tan (o 2nd con ellas) para la función hiperbólica.", "<b>hyp is on:</b> press sin, cos, or tan (or 2nd with them) for the hyperbolic function."),
    ("Muévete con las flechas y pulsa <b>enter</b> para elegir. <b>clear</b> sale del menú.", "Move with the arrows and press <b>enter</b> to choose. <b>clear</b> leaves the menu."),
    ("Pulsa 1 para cancelar o 2 para restablecer.", "Press 1 to cancel or 2 to reset."),
    ("Pulsa 1 para poner todas las variables en 0, o 2 para cancelar.", "Press 1 to set all the variables to 0, or 2 to cancel."),
    ("Elige la variable cuyo valor quieres escribir en el cálculo.", "Choose the variable whose value you want to type in the calculation."),
    ("<b>1-Var Stats</b>: media, mediana, cuartiles… de una lista. <b>2-Var Stats</b>: dos listas (x e y) y la recta de regresión.", "<b>1-Var Stats</b>: mean, median, quartiles… of one list. <b>2-Var Stats</b>: two lists (x and y) and the regression line."),
    ("Elige con el número de la opción o con ▲ ▼ y enter.", "Choose with the option number, or with ▲ ▼ and enter."),
    (" ◄ ► cambian de pestaña.", " ◄ ► change tabs."),
    (" <b>clear</b> sale del menú.", " <b>clear</b> leaves the menu."),
    ("Escribe un dato y pulsa <b>enter</b> o ▼. ◄ ► cambian de lista. <b>data</b>: borrar listas · <b>2nd data</b>: estadística · <b>2nd mode</b> (quit): salir.", "Type a value and press <b>enter</b> or ▼. ◄ ► change lists. <b>data</b>: clear lists · <b>2nd data</b>: statistics · <b>2nd mode</b> (quit): leave."),
    ("▲ ▼ eligen la fila y ◄ ► la lista. Baja a <b>CALC</b> y pulsa <b>enter</b>.", "▲ ▼ choose the row and ◄ ► the list. Go down to <b>CALC</b> and press <b>enter</b>."),
    ("▲ ▼ recorren los resultados. <b>enter</b> (o el número) lleva el valor al cálculo. <b>clear</b>: salir.", "▲ ▼ move through the results. <b>enter</b> (or the number) puts the value in the calculation. <b>clear</b>: leave."),
    ("Escribe la función usando la tecla <b>x<sub>abc</sub><sup>yzt</sup></b> para la <i>x</i> y pulsa <b>enter</b>.", "Type the function using the <b>x<sub>abc</sub><sup>yzt</sup></b> key for <i>x</i>, and press <b>enter</b>."),
    ("<b>Start</b>: primer valor de <i>x</i>. <b>Step</b>: de cuánto en cuánto. <b>Auto</b> llena la tabla; <b>Ask-x</b> te deja escribir cada <i>x</i>. Baja a <b>OK</b> y pulsa <b>enter</b>.", "<b>Start</b>: first value of <i>x</i>. <b>Step</b>: how much it goes up each time. <b>Auto</b> fills the table; <b>Ask-x</b> lets you type each <i>x</i>. Go down to <b>OK</b> and press <b>enter</b>."),
    ("▲ ▼ recorren la tabla. <b>table</b>: cambiar la función · <b>2nd mode</b> (quit): salir.", "▲ ▼ move through the table. <b>table</b>: change the function · <b>2nd mode</b> (quit): leave."),
    ("Escribe un valor de <i>x</i> y pulsa <b>enter</b>. <b>2nd mode</b> (quit): salir.", "Type a value of <i>x</i> and press <b>enter</b>. <b>2nd mode</b> (quit): leave."),
    ("Escribe la operación de la constante (por ejemplo + 3) y pulsa <b>enter</b>.", "Type the operation for the constant (for example + 3) and press <b>enter</b>."),
    ("▲ ▼ recorren los cálculos anteriores. <b>enter</b> copia el seleccionado en la línea de entrada.", "▲ ▼ move through earlier calculations. <b>enter</b> copies the one selected to the entry line."),
    ("Ahora pulsa la tecla de variables (x<sub>abc</sub><sup>yzt</sup>) para elegir dónde guardar. Púlsala otra vez para cambiar de letra.", "Now press the variable key (x<sub>abc</sub><sup>yzt</sup>) to choose where to store. Press it again to change the letter."),
    ("Pulsa otra vez la tecla de variables para cambiar a y, z, t, a, b o c.", "Press the variable key again to change to y, z, t, a, b, or c."),
    ("<b>CLASSIC:</b> escribe el denominador.", "<b>CLASSIC:</b> type the denominator."),
    ("<b>CLASSIC:</b> escribe el numerador, pulsa <b>n/d</b> y escribe el denominador.", "<b>CLASSIC:</b> type the numerator, press <b>n/d</b>, and type the denominator."),
    ("<b>CLASSIC:</b> escribe el exponente; si tiene operaciones, ponlo entre paréntesis.", "<b>CLASSIC:</b> type the exponent; if it has operations, put it in parentheses."),
    ("Escribe el segundo número (r) y pulsa <b>enter</b>.", "Type the second number (r) and press <b>enter</b>."),
    ("Separa los dos números con la coma (<b>2nd</b> <b>.</b>) y pulsa <b>enter</b>.", "Separate the two numbers with the comma (<b>2nd</b> <b>.</b>) and press <b>enter</b>."),
    ("Pulsa <b>enter</b> para calcular.", "Press <b>enter</b> to calculate."),
    ("Constante K activa: escribe un número y pulsa <b>enter</b>. <b>2nd ÷</b> la desactiva.", "Constant K is on: type a number and press <b>enter</b>. <b>2nd ÷</b> turns it off."),
    ("<b>⟷</b> alterna fracción y decimal. Para verlo como número mixto: <b>2nd</b> <b>x⁻¹</b> (n/d◂▸Un/d) y <b>enter</b>.", "<b>⟷</b> switches between fraction and decimal. To see it as a mixed number: <b>2nd</b> <b>x⁻¹</b> (n/d◂▸Un/d) and <b>enter</b>."),
    ("<b>⟷</b> alterna entre la forma exacta y el decimal.", "<b>⟷</b> switches between the exact form and the decimal."),
]:
    litall(es, en)

# ---------- Formula sheet and guide: rewritten as whole blocks ----------
a = src.index("  var HTML_FORMULAS =")
b = src.index("  function htmlGuia() {")
src = src[:a] + open(sys.argv[3], encoding="utf-8").read() + "\n" + src[b:]
rep("'<p class=\"gti-nota\" style=\"margin-top:0\">Ir a:</p>", "'<p class=\"gti-nota\" style=\"margin-top:0\">Go to:</p>")

# ---------- Windows and toolbar ----------
for es, en, c in [
    ("Calculadora TI-30XS MultiView", "TI-30XS MultiView calculator", 1),
    ("Barra para mover la calculadora. Arrástrala o usa las flechas del teclado.", "Bar to move the calculator. Drag it or use the arrow keys.", 1),
    ("<span aria-hidden=\"true\">⠿</span><span class=\"gti-asa-t\">Calculadora</span>", "<span aria-hidden=\"true\">⠿</span><span class=\"gti-asa-t\">Calculator</span>", 1),
    ("Mostrar u ocultar las pistas", "Show or hide the hints", 1),
    ("Pistas", "Hints", 1), ("💡 Pistas", "💡 Hints", 1),
    ("Hoja de referencia", "Reference sheet", 2),
    ("Abrir la guía de uso de la calculadora", "Open the guide to using the calculator", 1),
    ("Cerrar", "Close", 2), ("Cerrar la calculadora", "Close the calculator", 1),
    ("Pistas activadas", "Hints on", 1), ("Pistas desactivadas", "Hints off", 1),
    ("Barra para mover la hoja de referencia. Arrástrala o usa las flechas del teclado.", "Bar to move the reference sheet. Drag it or use the arrow keys.", 1),
    ("<span aria-hidden=\"true\">⠿</span><span class=\"gti-asa-t\">Hoja de referencia</span>", "<span aria-hidden=\"true\">⠿</span><span class=\"gti-asa-t\">Reference sheet</span>", 1),
    ("Cerrar la hoja de referencia", "Close the reference sheet", 1),
    ("Secciones de la hoja", "Sections of the sheet", 1),
    ("Fórmulas", "Formulas", 1), ("Uso de la calculadora", "Using the calculator", 1),
    ("Herramientas de matemáticas", "Math tools", 1),
    ("<span aria-hidden=\"true\">🧮</span> Calculadora", "<span aria-hidden=\"true\">🧮</span> Calculator", 1),
    ("<span aria-hidden=\"true\">📐</span> Hoja de referencia", "<span aria-hidden=\"true\">📐</span> Reference sheet", 1),
    ("GEDparaHispanos · Zhema · recurso educativo", "LearnGED · Zhema · learning resource", 1),
]:
    lit(es, en, c)

lit("Constante K cancelada.", "Constant K canceled.")
lit("Constante K desactivada.", "Constant K is off.")
rep("<small>clear: volver · ◄ ►: corregir</small>", "<small>clear: go back · ◄ ►: fix it</small>")
rep("<span>Simulador GPH</span>", "<span>LearnGED simulator</span>")
rep("[['up', '▲', 'arriba'], ['left', '◄', 'izquierda'], ['right', '►', 'derecha'], ['down', '▼', 'abajo']]", "[['up', '▲', 'up'], ['left', '◄', 'left'], ['right', '►', 'right'], ['down', '▼', 'down']]")
rep("'aria-label': 'Flecha ' + a[2] }", "'aria-label': 'Arrow ' + a[2] }")
rep("b._d1 = 'Flecha ' + a[2];", "b._d1 = 'Arrow ' + a[2];")

# Separate saved window positions from the Spanish build (same browser, different site)
rep("'gti-pos-calc'", "'lg-pos-calc'", src.count("'gti-pos-calc'"))
rep("'gti-pos-hoja'", "'lg-pos-hoja'", src.count("'gti-pos-hoja'"))
# Options: accept "yes" as well as "si"
rep("abrir: attr('data-abrir') === 'si'", "abrir: attr('data-abrir') === 'si' || attr('data-abrir') === 'yes'")
rep("izquierda: attr('data-lado') === 'izquierda'", "izquierda: attr('data-lado') === 'izquierda' || attr('data-lado') === 'left'")

open(sys.argv[2], "w", encoding="utf-8").write(src)
print("ok")
