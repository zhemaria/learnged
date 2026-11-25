"""Crea es/matematicas/nivel-1/practica-3-2.html a partir de math/level-1/practice-3-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-3-2.html")
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 3.2 · Operaciones con decimales — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 3.2 · Operations with decimals · LearnGED</title>", "<title>Práctica · Lección 3.2 · Operaciones con decimales · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 3 · Decimals</div>', '<div class="ruta">Nivel 1 · Tema 3 · Decimales</div>')
R("<h1>Lesson 3.2 · Operations with decimals</h1>", "<h1>Lección 3.2 · Operaciones con decimales</h1>")
R("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. Solve on paper first; then check with the calculator (button at the top right).",
  "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento. Resuelva primero en papel; después compruebe con la calculadora (botón de la esquina superior derecha).")
R('<li><a href="#add-subtract">Add and subtract: line up the points</a></li>', '<li><a href="#sumar-restar">Sumar y restar: alinear los puntos</a></li>')
R('<li><a href="#multiply">Multiply: count the places</a></li>', '<li><a href="#multiplicar">Multiplicar: contar los lugares</a></li>')
R('<li><a href="#divide">Divide: move the point</a></li>', '<li><a href="#dividir">Dividir: mover el punto</a></li>')
t.todas('<span aria-hidden="true">🧮</span> Open the calculator</button>', '<span aria-hidden="true">🧮</span> Abrir la calculadora</button>')
t.todas('<span aria-hidden="true">🧮</span> Check it on the calculator</span>', '<span aria-hidden="true">🧮</span> Compruébelo en la calculadora</span>')
t.todas('">Answer</label>', '">Respuesta</label>')
t.todas("<h3>Step by step</h3>", "<h3>Paso a paso</h3>")
# 1
R('id="add-subtract" open>', 'id="sumar-restar" open>'); R("<h2>Add and subtract: line up the points</h2>", "<h2>Sumar y restar: alinear los puntos</h2>")
R("""<p>Line up the <strong>decimal points</strong> in one column. If the numbers have a different number of decimal places, add
      <strong>zeros on the right</strong>. Then work column by column, like with whole numbers. The point in the answer goes in the same column.</p>""",
  """<p>Alinee los <strong>puntos decimales</strong> en una columna. Si los números tienen distinta cantidad de lugares decimales, agregue
      <strong>ceros a la derecha</strong>. Después trabaje columna por columna, como con los números enteros. El punto del resultado va en la misma columna.</p>""")
R("<h3>Line up and calculate</h3>", "<h3>Alinee y calcule</h3>")
R('<label for="sr-a">First number</label>', '<label for="sr-a">Primer número</label>')
R('<label for="sr-o">Operation</label><select id="sr-o"><option value="+" selected>+ add</option><option value="-">− subtract</option></select>', '<label for="sr-o">Operación</label><select id="sr-o"><option value="+" selected>+ sumar</option><option value="-">− restar</option></select>')
R('<label for="sr-b">Second number</label>', '<label for="sr-b">Segundo número</label>')
R("<h3>Practice: add and subtract</h3>", "<h3>Practique: sume y reste</h3>")
R('<p class="nota">Type the number with a decimal point, for example 16.25. You can type $ for money.</p>', '<p class="nota">Escriba el número con punto decimal, por ejemplo 16.25. Puede escribir $ si es dinero.</p>')
R('<p>After you solve on paper, type the same operation on the calculator: the first number, <span class="tecla">+</span> or <span class="tecla">−</span>, the second number, and <span class="tecla">enter</span>. On the calculator you do not line up anything; that is your job on paper.</p>',
  '<p>Después de resolver en papel, escriba la misma operación en la calculadora: el primer número, <span class="tecla">+</span> o <span class="tecla">−</span>, el segundo número y <span class="tecla">enter</span>. En la calculadora no alinea nada; ese es su trabajo en papel.</p>')
# 2
R('id="multiply">', 'id="multiplicar">'); R("<h2>Multiply: count the places</h2>", "<h2>Multiplicar: contar los lugares</h2>")
R("""<p>Ignore the points and multiply like whole numbers. Then <strong>count the decimal places</strong> of both factors together:
      the answer has that many decimal places. Estimate to check that the point is in the right place.</p>""",
  """<p>Olvídese de los puntos y multiplique como con los números enteros. Después <strong>cuente los lugares decimales</strong> de los dos factores juntos:
      el resultado tiene esa cantidad de lugares decimales. Estime para comprobar que el punto está en su lugar.</p>""")
R('<label for="mu-a">First factor</label>', '<label for="mu-a">Primer factor</label>')
R('<label for="mu-b">Second factor</label>', '<label for="mu-b">Segundo factor</label>')
R("<h3>Practice: multiply</h3>", "<h3>Practique: multiplique</h3>")
R('<p class="nota">Type the number with a decimal point, for example 10.58.</p>', '<p class="nota">Escriba el número con punto decimal, por ejemplo 10.58.</p>')
R('<p>Type the first factor, <span class="tecla">×</span>, the second factor, and <span class="tecla">enter</span>. Compare three answers: your paper, your estimate, and the screen. When all three agree, you can trust your answer.</p>',
  '<p>Escriba el primer factor, <span class="tecla">×</span>, el segundo factor y <span class="tecla">enter</span>. Compare tres respuestas: su papel, su estimación y la pantalla. Cuando las tres coinciden, puede confiar en su respuesta.</p>')
# 3
R('id="divide">', 'id="dividir">'); R("<h2>Divide: move the point</h2>", "<h2>Dividir: mover el punto</h2>")
R("""<p>Move the point of the <strong>divisor</strong> until it is a whole number. Move the point of the <strong>dividend</strong> the same
      number of places, in the same direction. Then divide as always, and bring the point straight up into the answer.</p>""",
  """<p>Mueva el punto del <strong>divisor</strong> hasta que sea un número entero. Mueva el punto del <strong>dividendo</strong> la misma
      cantidad de lugares, en la misma dirección. Después divida como siempre y suba el punto derecho al resultado.</p>""")
R('<label for="di-a">Dividend</label>', '<label for="di-a">Dividendo</label>')
R("<h3>Practice: divide</h3>", "<h3>Practique: divida</h3>")
R('<p class="nota">Type the number with a decimal point, for example 18.9.</p>', '<p class="nota">Escriba el número con punto decimal, por ejemplo 18.9.</p>')
R('<p>Type the dividend, <span class="tecla">÷</span>, the divisor, and <span class="tecla">enter</span>. The calculator does not need you to move the point, so check that your paper agrees with the screen.</p>',
  '<p>Escriba el dividendo, <span class="tecla">÷</span>, el divisor y <span class="tecla">enter</span>. La calculadora no necesita que usted mueva el punto, así que compruebe que su papel coincide con la pantalla.</p>')
R("<p><strong>Level 1 · Topic 3 · Decimals · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 3 · Decimales · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Exact decimals (scaled whole numbers) ============ */", "/* ============ Decimales exactos (enteros escalados) ============ */")
R("/* Reads a typed decimal: allows $, commas, and spaces */", "/* Lee un decimal escrito: admite $, comas y espacios */")
R("/* Evaluator for a decimal answer, with common mistakes recognized */", "/* Evalúa una respuesta decimal y reconoce los errores comunes */")
R('msg: "Type a number with digits and a decimal point, for example 16.25." };', 'msg: "Escriba un número con cifras y punto decimal, por ejemplo 16.25." };')
R('msg: general || "Check your work one step at a time." };', 'msg: general || "Revise su trabajo paso a paso." };')
R("/* ============ MODULE 1 · add and subtract ============ */", "/* ============ MÓDULO 1 · sumar y restar ============ */")
R("/* Column table with the points lined up */", "/* Tabla en columnas con los puntos alineados */")
R('out.innerHTML = "Type two numbers with a decimal point, for example 12.4 and 3.85.";', 'out.innerHTML = "Escriba dos números con punto decimal, por ejemplo 12.4 y 3.85.";')
R('out.innerHTML = "At this level, put the greater number first when you subtract.";', 'out.innerHTML = "En este nivel, al restar ponga primero el número mayor.";')
R('pa + (o === "+" ? " plus " : " minus ") + pb + " in columns, with the points lined up. The answer is " + pr + "."', 'pa + (o === "+" ? " más " : " menos ") + pb + " en columnas, con los puntos alineados. El resultado es " + pr + "."')
R("""out.innerHTML = '<div class="linea">1. Add zeros so they match: ' + a + ' → <strong>' + pa + '</strong> and ' + b + ' → <strong>' + pb + '</strong>.</div>' +
    '<div class="linea">2. Line up the points and ' + (o === "+" ? "add" : "subtract") + ' column by column, like with whole numbers.</div>' +""",
  """out.innerHTML = '<div class="linea">1. Agregue ceros para igualarlos: ' + a + ' → <strong>' + pa + '</strong> y ' + b + ' → <strong>' + pb + '</strong>.</div>' +
    '<div class="linea">2. Alinee los puntos y ' + (o === "+" ? "sume" : "reste") + ' columna por columna, como con los números enteros.</div>' +""")
R('enun = "Find <strong>" + a + " + " + b + "</strong>."; }', 'enun = "Calcule <strong>" + a + " + " + b + "</strong>."; }')
R('enun = "Find <strong>" + a + " − " + b + "</strong>."; }', 'enun = "Calcule <strong>" + a + " − " + b + "</strong>."; }')
R('enun = "You pay a $" + b + " bill with a $" + a + " bill. <strong>How much change do you get?</strong>"; pre = "$"; }', 'enun = "Usted paga una cuenta de $" + b + " con un billete de $" + a + ". <strong>¿Cuánto le dan de cambio?</strong>"; pre = "$"; }')
R('enun = "A shirt costs $" + a + " and a pair of socks costs $" + b + ". <strong>How much do they cost together?</strong>"; pre = "$"; }', 'enun = "Una camisa cuesta $" + a + " y un par de medias cuesta $" + b + ". <strong>¿Cuánto cuestan juntos?</strong>"; pre = "$"; }')
R('msg: "Line up the decimal points, not the last digits. Add zeros so both numbers have the same decimal places." }];', 'msg: "Alinee los puntos decimales, no los últimos dígitos. Agregue ceros para que los dos números tengan los mismos lugares decimales." }];')
R('msg: "This one is a subtraction. Subtract the second number from the first." });', 'msg: "Esta es una resta. Reste el segundo número del primero." });')
R('solucion: "Add zeros and line up the points: "', 'solucion: "Agregue ceros y alinee los puntos: "')
R('"Line up the points, add zeros, and work column by column from the right."', '"Alinee los puntos, agregue ceros y trabaje columna por columna desde la derecha."')
R("/* ============ MODULE 2 · multiply ============ */", "/* ============ MÓDULO 2 · multiplicar ============ */")
R('out.innerHTML = "Type two numbers with a decimal point, for example 4.6 and 2.3.";', 'out.innerHTML = "Escriba dos números con punto decimal, por ejemplo 4.6 y 2.3.";')
R("""out.innerHTML = '<div class="linea">1. Ignore the points: ' + com(ia) + ' × ' + com(ib) + ' = ' + com(p) + '.</div>' +
    '<div class="linea">2. Count the decimal places: ' + a + ' has ' + da + ', and ' + b + ' has ' + db + '. In all: <strong>' + (da + db) + '</strong>.</div>' +
    '<div class="linea">3. Place the point so the answer has ' + (da + db) + (da + db === 1 ? ' decimal place' : ' decimal places') + ': ' + r + '.</div>' +
    '<div class="linea">Estimate: about ' + ea + ' × ' + eb + ' = ' + (ea * eb) + '.</div>' +""",
  """out.innerHTML = '<div class="linea">1. Olvídese de los puntos: ' + com(ia) + ' × ' + com(ib) + ' = ' + com(p) + '.</div>' +
    '<div class="linea">2. Cuente los lugares decimales: ' + a + ' tiene ' + da + ', y ' + b + ' tiene ' + db + '. En total: <strong>' + (da + db) + '</strong>.</div>' +
    '<div class="linea">3. Coloque el punto para que el resultado tenga ' + (da + db) + (da + db === 1 ? ' lugar decimal' : ' lugares decimales') + ': ' + r + '.</div>' +
    '<div class="linea">Estimación: más o menos ' + ea + ' × ' + eb + ' = ' + (ea * eb) + '.</div>' +""")
R('var enun = dinero ? "A pound of apples costs $" + a + ". <strong>How much do " + b + " pounds cost?</strong>" : "Find <strong>" + a + " × " + b + "</strong>.";', 'var enun = dinero ? "Una libra de manzanas cuesta $" + a + ". <strong>¿Cuánto cuestan " + b + " libras?</strong>" : "Calcule <strong>" + a + " × " + b + "</strong>.";')
R('msg: "Count again: " + a + " has " + nDec(a) + " and " + b + " has " + nDec(b) + " decimal places. The answer needs " + k + "." },', 'msg: "Cuente otra vez: " + a + " tiene " + nDec(a) + " y " + b + " tiene " + nDec(b) + " lugares decimales. El resultado necesita " + k + "." },')
R('msg: "The point is too far to the left. Count the decimal places again: the answer needs " + k + "." }];', 'msg: "El punto está demasiado a la izquierda. Cuente otra vez los lugares decimales: el resultado necesita " + k + "." }];')
R('msg: "That is an addition. Multiply the numbers." });', 'msg: "Eso es una suma. Multiplique los números." });')
R('". With " + k + (k === 1 ? " decimal place" : " decimal places") + ": <strong>"', '". Con " + k + (k === 1 ? " lugar decimal" : " lugares decimales") + ": <strong>"')
R('"Multiply without the points, then count the decimal places of both factors."', '"Multiplique sin los puntos y después cuente los lugares decimales de los dos factores."')
R("/* ============ MODULE 3 · divide ============ */", "/* ============ MÓDULO 3 · dividir ============ */")
R('out.innerHTML = "Type two numbers with a decimal point. The divisor cannot be 0.";', 'out.innerHTML = "Escriba dos números con punto decimal. El divisor no puede ser 0.";')
R("""(k ? '<div class="linea">1. The divisor is ' + b + '. Move its point ' + k + (k === 1 ? ' place' : ' places') + ' to the right: ' + b + ' → <strong>' + B2 + '</strong>.</div>' +
    '<div class="linea">2. Move the point of the dividend the same amount: ' + a + ' → <strong>' + limpia(A2) + '</strong>.</div>'
    : '<div class="linea">1. The divisor ' + b + ' is already a whole number. You do not move any point.</div>') +
    '<div class="linea">' + (k ? "3" : "2") + '. Divide ' + limpia(A2) + ' ÷ ' + B2 + ' with long division. The point goes straight up into the answer.</div>' +
    '<div class="linea veredicto">' + a + ' ÷ ' + b + ' = ' + (Math.abs(qr - q) > 1e-9 ? "about " : "") + limpia(String(qr)) + '</div>';""",
  """(k ? '<div class="linea">1. El divisor es ' + b + '. Mueva su punto ' + k + (k === 1 ? ' lugar' : ' lugares') + ' a la derecha: ' + b + ' → <strong>' + B2 + '</strong>.</div>' +
    '<div class="linea">2. Mueva el punto del dividendo lo mismo: ' + a + ' → <strong>' + limpia(A2) + '</strong>.</div>'
    : '<div class="linea">1. El divisor ' + b + ' ya es un número entero. No mueve ningún punto.</div>') +
    '<div class="linea">' + (k ? "3" : "2") + '. Divida ' + limpia(A2) + ' ÷ ' + B2 + ' con la división larga. El punto sube derecho al resultado.</div>' +
    '<div class="linea veredicto">' + a + ' ÷ ' + b + ' = ' + (Math.abs(qr - q) > 1e-9 ? "aproximadamente " : "") + limpia(String(qr)) + '</div>';""")
R('"$" + dvd + " is shared equally among " + d + " people. <strong>How much does each person get?</strong>" : "Find <strong>" + dvd + " ÷ " + d + "</strong>.";', '"$" + dvd + " se reparten en partes iguales entre " + d + " personas. <strong>¿Cuánto le toca a cada persona?</strong>" : "Calcule <strong>" + dvd + " ÷ " + d + "</strong>.";')
R('msg: "Bring the point straight up into the answer. Estimate to check." },', 'msg: "Suba el punto derecho al resultado. Estime para comprobar." },')
R('msg: "The answer is too small. Estimate: about how many times does " + d + " fit into " + dvd + "?" }];', 'msg: "El resultado es demasiado pequeño. Estime: ¿más o menos cuántas veces cabe " + d + " en " + dvd + "?" }];')
R('(kd ? "Move the point " + kd + (kd === 1 ? " place" : " places") + " in both numbers: " + movido + " ÷ " + base + ". " : "The divisor is whole, so no point moves. ") + "The answer is <strong>"',
  '(kd ? "Mueva el punto " + kd + (kd === 1 ? " lugar" : " lugares") + " en los dos números: " + movido + " ÷ " + base + ". " : "El divisor es entero, así que no se mueve ningún punto. ") + "El resultado es <strong>"')
R('"</strong>. Check: " + limpia(q) + " × " + d + " = " + dvd + ".",', '"</strong>. Comprobación: " + limpia(q) + " × " + d + " = " + dvd + ".",')
R('"Make the divisor whole, move the dividend\'s point the same amount, and divide."', '"Haga entero el divisor, mueva el punto del dividendo lo mismo y divida."')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-3-2.html")
