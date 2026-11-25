"""Crea es/matematicas/nivel-1/practica-3-3.html a partir de math/level-1/practice-3-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-3-3.html")
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 3.3 · Decimales en contexto — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 3.3 · Decimals in context and equivalent forms · LearnGED</title>", "<title>Práctica · Lección 3.3 · Decimales en contexto y formas equivalentes · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 3 · Decimals</div>', '<div class="ruta">Nivel 1 · Tema 3 · Decimales</div>')
R("<h1>Lesson 3.3 · Decimals in context and equivalent forms</h1>", "<h1>Lección 3.3 · Decimales en contexto y formas equivalentes</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. Solve on paper first; then check with the calculator (button at the top right).",
  "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento. Resuelva primero en papel; después compruebe con la calculadora (botón de la esquina superior derecha).")
R('<li><a href="#fraction-to-decimal">From fraction to decimal</a></li>', '<li><a href="#fraccion-a-decimal">De fracción a decimal</a></li>')
R('<li><a href="#decimal-to-fraction">From decimal to fraction</a></li>', '<li><a href="#decimal-a-fraccion">De decimal a fracción</a></li>')
R('<li><a href="#memorize">Pairs worth knowing by heart</a></li>', '<li><a href="#memoria">Parejas que conviene saber de memoria</a></li>')
R('<li><a href="#real-life">Decimals in real life</a></li>', '<li><a href="#vida-real">Los decimales en la vida real</a></li>')
t.todas('<span aria-hidden="true">🧮</span> Open the calculator</button>', '<span aria-hidden="true">🧮</span> Abrir la calculadora</button>')
t.todas('<span aria-hidden="true">🧮</span> Check it on the calculator</span>', '<span aria-hidden="true">🧮</span> Compruébelo en la calculadora</span>')
# 1
R('id="fraction-to-decimal" open>', 'id="fraccion-a-decimal" open>'); R("<h2>From fraction to decimal</h2>", "<h2>De fracción a decimal</h2>")
R("""<p>The fraction bar means <strong>"divided by"</strong>. Divide the numerator by the denominator. If the numerator is smaller,
      write a point and zeros after it, and keep dividing.</p>""",
  """<p>La raya de la fracción quiere decir <strong>«dividido entre»</strong>. Divida el numerador entre el denominador. Si el numerador es menor,
      escriba un punto y ceros después, y siga dividiendo.</p>""")
R("<h3>Divide the fraction</h3>", "<h3>Divida la fracción</h3>")
R('<label for="fd-n">Numerator (top)</label>', '<label for="fd-n">Numerador (arriba)</label>')
R('<label for="fd-d">Denominator (bottom)</label>', '<label for="fd-d">Denominador (abajo)</label>')
R("<h3>Practice: which decimal is it?</h3>", "<h3>Practique: ¿qué decimal es?</h3>")
R('<p>Type the numerator, <span class="tecla">÷</span>, the denominator, and <span class="tecla">enter</span>. Or write the fraction with <span class="tecla">n/d</span> and press <span class="tecla">⟷</span> to see it as a decimal.</p>',
  '<p>Escriba el numerador, <span class="tecla">÷</span>, el denominador y <span class="tecla">enter</span>. O escriba la fracción con <span class="tecla">n/d</span> y pulse <span class="tecla">⟷</span> para verla como decimal.</p>')
# 2
R('id="decimal-to-fraction">', 'id="decimal-a-fraccion">'); R("<h2>From decimal to fraction</h2>", "<h2>De decimal a fracción</h2>")
R("""<p>Read the decimal. The <strong>last place</strong> gives the denominator: tenths → 10, hundredths → 100, thousandths → 1,000.
      Then simplify: divide the top and the bottom by the same number.</p>""",
  """<p>Lea el decimal. El <strong>último lugar</strong> da el denominador: décimas → 10, centésimas → 100, milésimas → 1,000.
      Después simplifique: divida el numerador y el denominador entre el mismo número.</p>""")
R("<h3>From the decimal to the fraction</h3>", "<h3>Del decimal a la fracción</h3>")
R("<h3>Practice: write it as a simplified fraction</h3>", "<h3>Practique: escríbalo como fracción simplificada</h3>")
R('<label for="p2-r">Fraction</label>', '<label for="p2-r">Fracción</label>')
R('<p class="nota">Type the fraction with a slash, for example 3/5.</p>', '<p class="nota">Escriba la fracción con una raya inclinada, por ejemplo 3/5.</p>')
R('<p>Type the decimal, press <span class="tecla dos">2nd</span> and <span class="tecla">table</span> (the green words say <em>f◂▸d</em>), and press <span class="tecla">enter</span>. The calculator shows the simplified fraction.</p>',
  '<p>Escriba el decimal, pulse <span class="tecla dos">2nd</span> y <span class="tecla">table</span> (las palabras verdes dicen <em>f◂▸d</em>) y pulse <span class="tecla">enter</span>. La calculadora muestra la fracción simplificada.</p>')
# 3
R('id="memorize">', 'id="memoria">'); R("<h2>Pairs worth knowing by heart</h2>", "<h2>Parejas que conviene saber de memoria</h2>")
R("<p>Press a card to see its decimal. Try to say the decimal out loud <strong>before</strong> you turn the card.</p>", "<p>Pulse una tarjeta para ver su decimal. Intente decir el decimal en voz alta <strong>antes</strong> de voltear la tarjeta.</p>")
R('aria-label="Flash cards: fractions and decimals"', 'aria-label="Tarjetas: fracciones y decimales"')
R('id="eq-todas">Mostrar todo</button>', 'id="eq-todas">Mostrar todas</button>')
R('id="eq-ninguna">Hide all</button>', 'id="eq-ninguna">Ocultar todas</button>')
R("<h3>Practice: find the pair</h3>", "<h3>Practique: encuentre la pareja</h3>")
# 4
R('id="real-life">', 'id="vida-real">'); R("<h2>Decimals in real life</h2>", "<h2>Los decimales en la vida real</h2>")
R("<p>Use the 4 steps: read and underline, choose the operation, solve, and check that the answer makes sense.</p>", "<p>Use los 4 pasos: lea y subraye, elija la operación, resuelva y compruebe que el resultado tiene sentido.</p>")
R("<h3>Practice: problems with decimals</h3>", "<h3>Practique: problemas con decimales</h3>")
R('<label for="p4-r">Answer</label>', '<label for="p4-r">Respuesta</label>')
R('<p class="nota">Type the number only. You can type $ for money; do not type the unit (miles, pounds).</p>', '<p class="nota">Escriba solo el número. Puede escribir $ si es dinero; no escriba la unidad (millas, libras).</p>')
R("<p>After you solve on paper, check each step on the calculator. In two-step problems, check both steps.</p>", "<p>Después de resolver en papel, compruebe cada paso en la calculadora. En los problemas de dos pasos, compruebe los dos.</p>")
R("<p><strong>Level 1 · Topic 3 · Decimals · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 3 · Decimales · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Helpers ============ */", "/* ============ Utilidades ============ */")
R("/* Stacked fraction: visual + text for screen readers */", "/* Fracción apilada: visual + texto para lectores de pantalla */")
R('var LUG = ["", "tenths", "hundredths", "thousandths"];', 'var LUG = ["", "décimas", "centésimas", "milésimas"];')
R("/* ============ MODULE 1 · fraction to decimal ============ */", "/* ============ MÓDULO 1 · de fracción a decimal ============ */")
R('pasos.push(t + " ÷ " + d + " = " + q + ", remainder " + (t - q * d));', 'pasos.push(t + " ÷ " + d + " = " + q + ", residuo " + (t - q * d));')
R('out.innerHTML = "Type a numerator and a denominator (the denominator cannot be 0)."; return; }', 'out.innerHTML = "Escriba un numerador y un denominador (el denominador no puede ser 0)."; return; }')
R('(n % d ? ", remainder " + (n % d) + "." : ", with no remainder.")', '(n % d ? ", residuo " + (n % d) + "." : ", sin residuo.")')
R("""(R.ent ? "Put a point in the answer and keep bringing down zeros:" : "Since " + n + " is less than " + d + ", write " + n + ".000… and put the point in the answer:")""",
  """(R.ent ? "Ponga un punto en el resultado y siga bajando ceros:" : "Como " + n + " es menor que " + d + ", escriba " + n + ".000… y ponga el punto en el resultado:")""")
R("""'<div class="linea">The digits ' + R.cifras.slice(R.per) + ' repeat forever: this is a repeating decimal. Rounded to the hundredth: '""", """'<div class="linea">Los dígitos ' + R.cifras.slice(R.per) + ' se repiten sin fin: es un decimal periódico. Redondeado a la centésima: '""")
R('pistas[pegado] = "A fraction is not read by putting the digits together with a point. Divide " + f[0] + " ÷ " + f[1] + ".";', 'pistas[pegado] = "Una fracción no se lee juntando los dígitos con un punto. Divida " + f[0] + " ÷ " + f[1] + ".";')
R('pistas[inv] = "You divided the bottom by the top. Divide the numerator (top) by the denominator (bottom).";', 'pistas[inv] = "Dividió el de abajo entre el de arriba. Divida el numerador (arriba) entre el denominador (abajo).";')
R('pistas[x10] = "Check where the point goes. " + fr(f[0], f[1]) + " is less than 1.";', 'pistas[x10] = "Revise dónde va el punto. " + fr(f[0], f[1]) + " es menor que 1.";')
R('return { enun: "Which decimal is equal to " + fr(f[0], f[1]) + "?",', 'return { enun: "¿Qué decimal es igual a " + fr(f[0], f[1]) + "?",')
R('mal: "Divide the numerator by the denominator: " + f[0] + " ÷ " + f[1] + " = " + s + "." };', 'mal: "Divida el numerador entre el denominador: " + f[0] + " ÷ " + f[1] + " = " + s + "." };')
R("/* ============ MODULE 2 · decimal to fraction ============ */", "/* ============ MÓDULO 2 · de decimal a fracción ============ */")
R('out.innerHTML = "Type a decimal with a point, for example 0.6 or 1.25 (up to 3 digits after the point)."; return; }', 'out.innerHTML = "Escriba un decimal con punto, por ejemplo 0.6 o 1.25 (hasta 3 dígitos después del punto)."; return; }')
R('out.innerHTML = "0 as a fraction is 0."; return; }', 'out.innerHTML = "0 como fracción es 0."; return; }')
R("""out.innerHTML = '<div class="linea">' + t + ' ends in the <strong>' + LUG[k] + '</strong>, so the denominator is ' + com(den) + ': ' + t + ' = ' + fr(num, den) + '</div>' +
    (g > 1 ? '<div class="linea">Simplify: divide the top and the bottom by ' + g + '. ' + num + ' ÷ ' + g + ' = ' + (num / g) + ', and ' + com(den) + ' ÷ ' + g + ' = ' + (den / g) + '.</div>'
           : '<div class="linea">' + num + ' and ' + den + ' cannot both be divided by the same number: the fraction is already simplified.</div>') +""",
  """out.innerHTML = '<div class="linea">' + t + ' termina en las <strong>' + LUG[k] + '</strong>, así que el denominador es ' + com(den) + ': ' + t + ' = ' + fr(num, den) + '</div>' +
    (g > 1 ? '<div class="linea">Simplifique: divida el numerador y el denominador entre ' + g + '. ' + num + ' ÷ ' + g + ' = ' + (num / g) + ', y ' + com(den) + ' ÷ ' + g + ' = ' + (den / g) + '.</div>'
           : '<div class="linea">' + num + ' y ' + den + ' no se pueden dividir los dos entre el mismo número: la fracción ya está simplificada.</div>') +""")
R('return { enun: "Write <strong>" + v + "</strong> as a simplified fraction.",', 'return { enun: "Escriba <strong>" + v + "</strong> como fracción simplificada.",')
R('solucion: v + " ends in the " + LUG[k] + ": " + num + "/" + den + ". Simplified: <strong>" + f[0] + "/" + f[1] + "</strong>.",', 'solucion: v + " termina en las " + LUG[k] + ": " + num + "/" + den + ". Simplificada: <strong>" + f[0] + "/" + f[1] + "</strong>.",')
R('return { estado: "invalido", msg: "Type a fraction with a slash, for example 3/5." };', 'return { estado: "invalido", msg: "Escriba una fracción con una raya inclinada, por ejemplo 3/5." };')
R('msg: "The value is right, but the fraction can be simplified more. Divide the top and the bottom by the same number." };', 'msg: "El valor está bien, pero la fracción se puede simplificar más. Divida el numerador y el denominador entre el mismo número." };')
R('msg: "Check the denominator: " + v + " ends in the " + LUG[k] + ", so the denominator is " + den + "." };', 'msg: "Revise el denominador: " + v + " termina en las " + LUG[k] + ", así que el denominador es " + den + "." };')
R('msg: "Read the decimal: the last place gives the denominator. Then simplify." };', 'msg: "Lea el decimal: el último lugar da el denominador. Después simplifique." };')
R("/* ============ MODULE 3 · pairs to know by heart ============ */", "/* ============ MÓDULO 3 · parejas de memoria ============ */")
R('if (dir) return { enun: "Which decimal goes with " + fr(e[0], e[1]) + "?",', 'if (dir) return { enun: "¿Qué decimal va con " + fr(e[0], e[1]) + "?",')
R('pista: "Divide " + e[0] + " ÷ " + e[1] + ", or think of money: a quarter is $0.25.",', 'pista: "Divida " + e[0] + " ÷ " + e[1] + ", o piense en el dinero: una moneda de 25 centavos es $0.25.",')
R('mal: e[0] + "/" + e[1] + " = " + e[2] + ", because " + e[0] + " ÷ " + e[1] + " = "', 'mal: e[0] + "/" + e[1] + " = " + e[2] + ", porque " + e[0] + " ÷ " + e[1] + " = "')
R('return { enun: "Which fraction goes with <strong>" + e[2] + "</strong>?",', 'return { enun: "¿Qué fracción va con <strong>" + e[2] + "</strong>?",')
R('pista: "Divide the top by the bottom of each fraction, or think of money.",', 'pista: "Divida el numerador entre el denominador de cada fracción, o piense en el dinero.",')
R("/* ============ MODULE 4 · real life ============ */", "/* ============ MÓDULO 4 · vida real ============ */")
R('enun = "At the grocery store: bread $" + c2(a) + ", milk $" + c2(b) + ", and eggs $" + c2(c) + ". You pay with $" + pago + ". <strong>How much change do you get?</strong>";',
  'enun = "En el supermercado: pan $" + c2(a) + ", leche $" + c2(b) + " y huevos $" + c2(c) + ". Paga con $" + pago + ". <strong>¿Cuánto le dan de cambio?</strong>";')
R('sol = "Step 1: " + c2(a) + " + " + c2(b) + " + " + c2(c) + " = " + c2(tot) + ". Step 2: "', 'sol = "Paso 1: " + c2(a) + " + " + c2(b) + " + " + c2(c) + " = " + c2(tot) + ". Paso 2: "')
R('msg: "That is the total you spent. The question asks for the change: subtract it from what you paid." });', 'msg: "Eso es el total que gastó. La pregunta pide el cambio: réstelo de lo que pagó." });')
R('enun = "A person walks " + (m / 10) + " miles in the morning and " + c2(n) + " miles in the afternoon. <strong>How many miles did the person walk in all?</strong>";',
  'enun = "Una persona camina " + (m / 10) + " millas en la mañana y " + c2(n) + " millas en la tarde. <strong>¿Cuántas millas caminó en total?</strong>";')
R('" = <strong>" + limpia(res) + " miles</strong>.";', '" = <strong>" + limpia(res) + " millas</strong>.";')
R('msg: "Line up the decimal points before you add: "', 'msg: "Alinee los puntos decimales antes de sumar: "')
R('enun = "Gas costs $" + c2(pg) + " a gallon. <strong>How much do " + g + " gallons cost?</strong>";', 'enun = "La gasolina cuesta $" + c2(pg) + " el galón. <strong>¿Cuánto cuestan " + g + " galones?</strong>";')
R('"</strong>. Estimate: about $" + Math.round(pg / 100)', '"</strong>. Estimación: más o menos $" + Math.round(pg / 100)')
R('msg: "Equal groups: multiply, do not add." });', 'msg: "Grupos iguales: multiplique; no sume." });')
R('enun = "A $" + c2(tot2) + " bill is split equally among " + per + " people. <strong>How much does each person pay?</strong>";', 'enun = "Una cuenta de $" + c2(tot2) + " se reparte en partes iguales entre " + per + " personas. <strong>¿Cuánto paga cada persona?</strong>";')
R('"</strong>. Check: " + res + " × " + per + " = " + c2(tot2) + ".";', '"</strong>. Comprobación: " + res + " × " + per + " = " + c2(tot2) + ".";')
R('msg: "Split equally means divide, not multiply." });', 'msg: "Repartir en partes iguales quiere decir dividir, no multiplicar." });')
R('enun = "A bag of apples weighs " + c2(al) + " pounds and a bag of oranges weighs " + c2(al2) + " pounds. <strong>How many pounds heavier is the bag of apples?</strong>";',
  'enun = "Una bolsa de manzanas pesa " + c2(al) + " libras y una bolsa de naranjas pesa " + c2(al2) + " libras. <strong>¿Cuántas libras más pesa la bolsa de manzanas?</strong>";')
R('" = <strong>" + limpia(res) + " pounds</strong>.";', '" = <strong>" + limpia(res) + " libras</strong>.";')
R('msg: "\\"How many pounds heavier\\" compares two weights: subtract." });', 'msg: "«¿Cuántas libras más pesa?» compara dos pesos: reste." });')
R('return { estado: "invalido", msg: "Type a number with a decimal point, for example 9.55." };', 'return { estado: "invalido", msg: "Escriba un número con punto decimal, por ejemplo 9.55." };')
R('msg: "Use the 4 steps: underline, choose the operation, solve, and check that it makes sense." };', 'msg: "Use los 4 pasos: subraye, elija la operación, resuelva y compruebe que tiene sentido." };')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-3-3.html")
