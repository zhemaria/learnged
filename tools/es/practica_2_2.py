"""Crea es/matematicas/nivel-1/practica-2-2.html a partir de math/level-1/practice-2-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-2-2.html")
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 2.2 · División de números enteros — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 2.2 · Dividing whole numbers · LearnGED</title>", "<title>Práctica · Lección 2.2 · División de números enteros · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 2 · Multiplication and division</div>', '<div class="ruta">Nivel 1 · Tema 2 · Multiplicación y división</div>')
R("<h1>Lesson 2.2 · Dividing whole numbers</h1>", "<h1>Lección 2.2 · División de números enteros</h1>")
R("Four practice activities on one page. The exercises change every time, so you can practice as many times as you want. If you make a mistake, you get a hint and another try.",
  "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez, así que puede practicar todas las veces que quiera. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#meaning">What does dividing mean?</a></li>', '<li><a href="#significado">¿Qué significa dividir?</a></li>')
R('<li><a href="#long-division">Long division, step by step</a></li>', '<li><a href="#division-larga">La división larga, paso a paso</a></li>')
R('<li><a href="#remainder">The remainder</a></li>', '<li><a href="#residuo">El residuo</a></li>')
R('<li><a href="#what-to-do">What do I do with the remainder?</a></li>', '<li><a href="#que-hacer">¿Qué hago con el residuo?</a></li>')
R('id="meaning" open>', 'id="significado" open>'); R("<h2>What does dividing mean?</h2>", "<h2>¿Qué significa dividir?</h2>")
R("""<p>Division is the opposite of multiplication: it <strong>splits a total into equal groups</strong>, or finds <strong>how many groups fit</strong>.
      In 24 ÷ 6 = 4, 24 is the <strong>dividend</strong> (the total), 6 is the <strong>divisor</strong>, 4 is the <strong>quotient</strong> (the answer),
      and anything left over is the <strong>remainder</strong>.</p>""",
  """<p>La división es la contraria de la multiplicación: <strong>reparte un total en grupos iguales</strong>, o halla <strong>cuántos grupos caben</strong>.
      En 24 ÷ 6 = 4, 24 es el <strong>dividendo</strong> (el total), 6 es el <strong>divisor</strong>, 4 es el <strong>cociente</strong> (el resultado),
      y lo que sobra es el <strong>residuo</strong>.</p>""")
R("<h3>Make equal groups</h3>", "<h3>Forme grupos iguales</h3>")
R('<label for="rp-t">Total: <span id="rp-tv"></span></label>', '<label for="rp-t">Total: <span id="rp-tv"></span></label>')
R('<label for="rp-d">Size of each group: <span id="rp-dv"></span></label>', '<label for="rp-d">Tamaño de cada grupo: <span id="rp-dv"></span></label>')
R("<h3>Practice: the words</h3>", "<h3>Practique: las palabras</h3>")
R('id="long-division">', 'id="division-larga">'); R("<h2>Long division, step by step</h2>", "<h2>La división larga, paso a paso</h2>")
R("<caption>Repeat the cycle until there are no more digits to bring down</caption>", "<caption>Repita el ciclo hasta que no queden dígitos por bajar</caption>")
R('<th scope="col">Step</th><th scope="col">What you do</th>', '<th scope="col">Paso</th><th scope="col">Qué hace</th>')
R("<tr><td>Divide</td><td>How many times does the divisor fit? Write that number in the quotient.</td></tr>", "<tr><td>Dividir</td><td>¿Cuántas veces cabe el divisor? Escriba ese número en el cociente.</td></tr>")
R("<tr><td>Multiply</td><td>Multiply the divisor by that number.</td></tr>", "<tr><td>Multiplicar</td><td>Multiplique el divisor por ese número.</td></tr>")
R("<tr><td>Subtract</td><td>Subtract to see what is left.</td></tr>", "<tr><td>Restar</td><td>Reste para ver cuánto queda.</td></tr>")
R("<tr><td>Bring down</td><td>Bring down the next digit and start again.</td></tr>", "<tr><td>Bajar</td><td>Baje el dígito siguiente y empiece otra vez.</td></tr>")
R("<h3>Step by step</h3>", "<h3>Paso a paso</h3>")
R('<label for="dl-a">Dividend</label>', '<label for="dl-a">Dividendo</label>')
R('<label for="dl-b">Divisor (one digit)</label>', '<label for="dl-b">Divisor (un dígito)</label>')
R("""<strong>The remainder is always smaller than the divisor.</strong> If you subtract and get a number equal to or bigger than the divisor,
        the digit in the quotient is too small: make it bigger. And if the divisor does not fit, write <strong>0</strong> in the quotient.""",
  """<strong>El residuo siempre es menor que el divisor.</strong> Si al restar le da un número igual o mayor que el divisor,
        el dígito del cociente es demasiado pequeño: auméntelo. Y si el divisor no cabe, escriba <strong>0</strong> en el cociente.""")
R("<h3>Practice: divide (no remainder)</h3>", "<h3>Practique: divida (sin residuo)</h3>")
R('<label for="p2-r">Quotient</label>', '<label for="p2-r">Cociente</label>')
R('id="remainder">', 'id="residuo">'); R("<h2>The remainder</h2>", "<h2>El residuo</h2>")
R("<p>When a division does not come out even, what is left over is the <strong>remainder</strong>. Check it like this:</p>", "<p>Cuando una división no da exacto, lo que sobra es el <strong>residuo</strong>. Compruébelo así:</p>")
R('<div class="formula">(quotient × divisor) + remainder = dividend</div>', '<div class="formula">(cociente × divisor) + residuo = dividendo</div>')
R('<div class="caja-tip"><strong>Example:</strong> 50 ÷ 7 = 7, remainder 1, because (7 × 7) + 1 = 49 + 1 = 50 ✓.</div>', '<div class="caja-tip"><strong>Ejemplo:</strong> 50 ÷ 7 = 7, residuo 1, porque (7 × 7) + 1 = 49 + 1 = 50 ✓.</div>')
R("<h3>Practice: quotient and remainder</h3>", "<h3>Practique: cociente y residuo</h3>")
R('id="what-to-do">', 'id="que-hacer">'); R("<h2>What do I do with the remainder?</h2>", "<h2>¿Qué hago con el residuo?</h2>")
R("""<p>Finding the remainder is half of the work. The other half is deciding what it means in the real situation. The same calculation,
      26 ÷ 4 = 6, remainder 2, has three different answers:</p>""",
  """<p>Hallar el residuo es la mitad del trabajo. La otra mitad es decidir qué significa en la situación real. El mismo cálculo,
      26 ÷ 4 = 6, residuo 2, tiene tres respuestas distintas:</p>""")
R("<caption>The three possibilities</caption>", "<caption>Las tres posibilidades</caption>")
R('<th scope="col">What the problem asks for</th><th scope="col">What you do</th><th scope="col">Example</th>', '<th scope="col">Lo que pide el problema</th><th scope="col">Qué hace</th><th scope="col">Ejemplo</th>')
R("<tr><td>what is left over</td><td>give the remainder</td><td>26 rolls in 4 equal boxes: <strong>2</strong> are left over</td></tr>", "<tr><td>lo que sobra</td><td>dar el residuo</td><td>26 panes en 4 cajas iguales: sobran <strong>2</strong></td></tr>")
R("<tr><td>enough room for everyone</td><td>round the quotient up</td><td>26 people in cars for 4: they need <strong>7</strong> cars</td></tr>", "<tr><td>que haya lugar para todos</td><td>redondear el cociente hacia arriba</td><td>26 personas en carros de 4: necesitan <strong>7</strong> carros</td></tr>")
R("<tr><td>full groups only</td><td>drop the remainder</td><td>$26 and $4 tickets: you can buy <strong>6</strong> tickets</td></tr>", "<tr><td>solo grupos completos</td><td>descartar el residuo</td><td>$26 y boletos de $4: puede comprar <strong>6</strong> boletos</td></tr>")
R("<h3>Practice: what does the remainder mean?</h3>", "<h3>Practique: ¿qué significa el residuo?</h3>")
R("<p><strong>Level 1 · Topic 2 · Multiplication and division · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 2 · Multiplicación y división · LearnGED</strong><br>")
# Script
R("""'<div class="linea">With ' + t + ' objects you can make <strong>' + q + (q === 1 ? ' group' : ' groups') + '</strong> of ' + d + (r ? ', and <strong>' + r + '</strong> ' + (r === 1 ? 'is' : 'are') + ' left over (in red).' : ', with nothing left over.') + '</div><div class="linea veredicto">' + t + ' ÷ ' + d + ' = ' + q + (r ? ', remainder ' + r : '') + '</div><div class="linea">Dividend ' + t + ' · divisor ' + d + ' · quotient ' + q + ' · remainder ' + r + '</div>'""",
  """'<div class="linea">Con ' + t + ' objetos puede formar <strong>' + q + (q === 1 ? ' grupo' : ' grupos') + '</strong> de ' + d + (r ? ', y ' + (r === 1 ? 'sobra' : 'sobran') + ' <strong>' + r + '</strong> (en rojo).' : ', sin que sobre nada.') + '</div><div class="linea veredicto">' + t + ' ÷ ' + d + ' = ' + q + (r ? ', residuo ' + r : '') + '</div><div class="linea">Dividendo ' + t + ' · divisor ' + d + ' · cociente ' + q + ' · residuo ' + r + '</div>'""")
R('var nombres = ["the dividend", "the divisor", "the quotient", "the remainder"]', 'var nombres = ["el dividendo", "el divisor", "el cociente", "el residuo"]')
R('var pistas = { v0: n + " is the total you divide: the dividend.", v1: d + " is the number you divide by: the divisor.", v2: q + " is the answer: the quotient.", v3: r + " is what is left over: the remainder." };',
  'var pistas = { v0: n + " es el total que se divide: el dividendo.", v1: d + " es el número entre el que se divide: el divisor.", v2: q + " es el resultado: el cociente.", v3: r + " es lo que sobra: el residuo." };')
R('enun: "In <strong>" + n + " ÷ " + d + " = " + q + ", remainder " + r + "</strong>, which number is " + nombres[k] + "?"', 'enun: "En <strong>" + n + " ÷ " + d + " = " + q + ", residuo " + r + "</strong>, ¿qué número es " + nombres[k] + "?"')
R('bien: "Dividend " + n + ", divisor " + d + ", quotient " + q + ", remainder " + r + ".",', 'bien: "Dividendo " + n + ", divisor " + d + ", cociente " + q + ", residuo " + r + ".",')
R('mal: "The dividend is the total (" + n + "), the divisor is what you divide by (" + d + "), the quotient is the answer (" + q + "), and the remainder is what is left over (" + r + ")." };',
  'mal: "El dividendo es el total (" + n + "), el divisor es entre lo que se divide (" + d + "), el cociente es el resultado (" + q + ") y el residuo es lo que sobra (" + r + ")." };')
R("""aria-label="Long division: ' + com(n) + ' divided by ' + d + '\"""", """aria-label="División larga: ' + com(n) + ' entre ' + d + '\"""")
R('var txt = "<strong>Divide:</strong> how many times does " + d + " fit in " + parcial + "? " + (q === 0 ? "It does not fit: write 0 in the quotient." : q + (q === 1 ? " time." : " times.")) + " <strong>Multiply:</strong> " + q + " × " + d + " = " + m + ". <strong>Subtract:</strong> " + parcial + " − " + m + " = " + r + ".";',
  'var txt = "<strong>Dividir:</strong> ¿cuántas veces cabe " + d + " en " + parcial + "? " + (q === 0 ? "No cabe: escriba 0 en el cociente." : q + (q === 1 ? " vez." : " veces.")) + " <strong>Multiplicar:</strong> " + q + " × " + d + " = " + m + ". <strong>Restar:</strong> " + parcial + " − " + m + " = " + r + ".";')
R('txt += " <strong>Bring down</strong> the " + s[i + 1] + ": now you have " + (r*10 + (+s[i + 1])) + ".";', 'txt += " <strong>Bajar</strong> el " + s[i + 1] + ": ahora tiene " + (r*10 + (+s[i + 1])) + ".";')
R('txt += r ? " There are no more digits to bring down: the remainder is " + r + "." : " There are no more digits to bring down, and the remainder is 0.";', 'txt += r ? " No quedan dígitos por bajar: el residuo es " + r + "." : " No quedan dígitos por bajar, y el residuo es 0.";')
R('"Type a dividend with up to 7 digits and a one-digit divisor (1 to 9)."', '"Escriba un dividendo de hasta 7 dígitos y un divisor de un dígito (del 1 al 9)."')
R("(DL.n % DL.d ? ', remainder ' + DL.n % DL.d : '')", "(DL.n % DL.d ? ', residuo ' + DL.n % DL.d : '')")
R("'<div class=\"linea\">Start on the left. If the divisor does not fit in the first digit, use the first two digits.</div>'", "'<div class=\"linea\">Empiece por la izquierda. Si el divisor no cabe en el primer dígito, use los dos primeros dígitos.</div>'")
R('com(n) + " boxes are split equally among " + d + " trucks. How many boxes does each truck carry? "', 'com(n) + " cajas se reparten en partes iguales entre " + d + " camiones. ¿Cuántas cajas lleva cada camión? "')
R('msg: "This is a division, not a multiplication." }];', 'msg: "Esto es una división, no una multiplicación." }];')
R('msg: "A zero is missing in the quotient. When the divisor does not fit, write 0 before you bring down the next digit." });', 'msg: "Falta un cero en el cociente. Cuando el divisor no cabe, escriba 0 antes de bajar el dígito siguiente." });')
R('return { enun: ctx + "Find <strong>" + com(n) + " ÷ " + d + "</strong>."', 'return { enun: ctx + "Calcule <strong>" + com(n) + " ÷ " + d + "</strong>."')
R('" The quotient is " + com(q) + ". Check: " + com(q) + " × " + d + " = " + com(n) + ".",', '" El cociente es " + com(q) + ". Comprobación: " + com(q) + " × " + d + " = " + com(n) + ".",')
R('"Divide, multiply, subtract, bring down. Check your answer: quotient × " + d + " should give " + com(n) + "."', '"Divida, multiplique, reste y baje. Compruebe su respuesta: cociente × " + d + " debe dar " + com(n) + "."')
R('return { html: x[0] + ", remainder " + x[1], clave: x[0] + "-" + x[1] };', 'return { html: x[0] + ", residuo " + x[1], clave: x[0] + "-" + x[1] };')
R('pistas[(q - 1) + "-" + (r + d)] = "A remainder of " + (r + d) + " is bigger than the divisor, " + d + ". The quotient is too small.";', 'pistas[(q - 1) + "-" + (r + d)] = "Un residuo de " + (r + d) + " es mayor que el divisor, " + d + ". El cociente es demasiado pequeño.";')
R('pistas[(q + 1) + "-0"] = (q + 1) + " × " + d + " = " + (q + 1)*d + ", which is more than " + n + ".";', 'pistas[(q + 1) + "-0"] = (q + 1) + " × " + d + " = " + (q + 1)*d + ", que es más que " + n + ".";')
R('pistas[q + "-0"] = q + " × " + d + " = " + q*d + ", not " + n + ". Something is left over.";', 'pistas[q + "-0"] = q + " × " + d + " = " + q*d + ", no " + n + ". Sobra algo.";')
R('return { enun: "What is <strong>" + n + " ÷ " + d + "</strong>?"', 'return { enun: "¿Cuánto es <strong>" + n + " ÷ " + d + "</strong>?"')
R('bien: "Check: (" + q + " × " + d + ") + " + r + " = " + q*d + " + " + r + " = " + n + " ✓.",', 'bien: "Comprobación: (" + q + " × " + d + ") + " + r + " = " + q*d + " + " + r + " = " + n + " ✓.",')
R('mal: n + " ÷ " + d + " = " + q + ", remainder " + r + ". Check: (" + q + " × " + d + ") + " + r + " = " + n + "." };', 'mal: n + " ÷ " + d + " = " + q + ", residuo " + r + ". Comprobación: (" + q + " × " + d + ") + " + r + " = " + n + "." };')
R('enun = "A school is taking " + n + " students on a trip in buses with " + d + " seats. How many buses do they need?"; cor = q + 1; exp = "Everyone has to go: " + q + " buses are not enough (" + r + " student" + (r === 1 ? "" : "s") + " would have no seat). Round up: " + (q + 1) + " buses.";',
  'enun = "Una escuela lleva a " + n + " estudiantes de excursión en autobuses de " + d + " asientos. ¿Cuántos autobuses necesita?"; cor = q + 1; exp = "Tienen que ir todos: " + q + " autobuses no alcanzan (" + r + (r === 1 ? " estudiante se quedaría" : " estudiantes se quedarían") + " sin asiento). Se redondea hacia arriba: " + (q + 1) + " autobuses.";')
R('enun = "You have $" + n + " to buy T-shirts that cost $" + d + " each. How many whole T-shirts can you buy?"; cor = q; exp = "Only whole T-shirts count: " + q + ". The $" + r + " left over is not enough for another one, so drop the remainder.";',
  'enun = "Tiene $" + n + " para comprar camisetas de $" + d + " cada una. ¿Cuántas camisetas completas puede comprar?"; cor = q; exp = "Solo cuentan las camisetas completas: " + q + ". Los $" + r + " que sobran no alcanzan para otra, así que se descarta el residuo.";')
R('enun = n + " rolls are packed into " + d + " boxes, with the same number in each box. How many rolls are left over?"; cor = r; exp = "The question asks for what is left over: the remainder, " + r + " roll" + (r === 1 ? "" : "s") + ".";',
  'enun = n + " panes se empacan en " + d + " cajas, con la misma cantidad en cada caja. ¿Cuántos panes sobran?"; cor = r; exp = "La pregunta pide lo que sobra: el residuo, " + r + (r === 1 ? " pan" : " panes") + ".";')
R('enun += " <em>(" + n + " ÷ " + d + " = " + q + ", remainder " + r + ")</em>";', 'enun += " <em>(" + n + " ÷ " + d + " = " + q + ", residuo " + r + ")</em>";')
R('pistas["n" + q] = "Does the problem ask for full groups only? Read the question again."; pistas["n" + (q + 1)] = "Does everyone or everything need to fit? Read the question again."; pistas["n" + r] = "Does the problem ask for what is left over? Read the question again.";',
  'pistas["n" + q] = "¿El problema pide solo grupos completos? Lea otra vez la pregunta."; pistas["n" + (q + 1)] = "¿Tienen que caber todos, o todo? Lea otra vez la pregunta."; pistas["n" + r] = "¿El problema pide lo que sobra? Lea otra vez la pregunta.";')
R("/* ============ MODULE", "/* ============ MÓDULO", 4)
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-2-2.html")
