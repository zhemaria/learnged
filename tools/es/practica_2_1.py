"""Crea es/matematicas/nivel-1/practica-2-1.html a partir de math/level-1/practice-2-1.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-2-1.html")
R = t.r
R("<!-- LearnGED · Level 1 · Lesson 2.1", "<!-- LearnGED · Nivel 1 · Lección 2.1")
t.s = t.s.replace(t.s[t.s.index("<!-- LearnGED"):t.s.index("-->") + 3], "<!-- LearnGED · Nivel 1 · Lección 2.1 · Multiplicación de números enteros — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->", 1)
R("<title>Practice · Lesson 2.1 · Multiplying whole numbers · LearnGED</title>", "<title>Práctica · Lección 2.1 · Multiplicación de números enteros · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 2 · Multiplication and division</div>', '<div class="ruta">Nivel 1 · Tema 2 · Multiplicación y división</div>')
R("<h1>Lesson 2.1 · Multiplying whole numbers</h1>", "<h1>Lección 2.1 · Multiplicación de números enteros</h1>")
R("Five practice activities and a review game on one page. The exercises change every time, so you can practice as many times as you want. If you make a mistake, you get a hint and another try.",
  "Cinco actividades de práctica y un juego de repaso en una sola página. Los ejercicios cambian cada vez, así que puede practicar todas las veces que quiera. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#meaning">What does multiplying mean?</a></li>', '<li><a href="#significado">¿Qué significa multiplicar?</a></li>')
R('<li><a href="#tables-properties">Times tables and properties</a></li>', '<li><a href="#tablas-propiedades">Tablas de multiplicar y propiedades</a></li>')
R('<li><a href="#one-digit">Multiplying by one digit</a></li>', '<li><a href="#un-digito">Multiplicar por un dígito</a></li>')
R('<li><a href="#two-digit">Multiplying by two digits</a></li>', '<li><a href="#dos-digitos">Multiplicar por dos dígitos</a></li>')
R('<li><a href="#estimate">Checking with an estimate</a></li>', '<li><a href="#estimar">Comprobar con una estimación</a></li>')
R('<li><a href="#bingo">Multiplication bingo</a></li>', '<li><a href="#bingo">Bingo de multiplicación</a></li>')
# Módulo 1
R('id="meaning" open>', 'id="significado" open>')
R("<h2>What does multiplying mean?</h2>", "<h2>¿Qué significa multiplicar?</h2>")
R("""<p><strong>Multiplying is adding the same number several times</strong>, in a shorter way. Four packs of 6 bottles are
      6 + 6 + 6 + 6 = 24, so 4 × 6 = 24. The numbers you multiply are the <strong>factors</strong>, and the answer is the <strong>product</strong>.</p>""",
  """<p><strong>Multiplicar es sumar el mismo número varias veces</strong>, de forma más corta. Cuatro paquetes de 6 botellas son
      6 + 6 + 6 + 6 = 24, así que 4 × 6 = 24. Los números que se multiplican son los <strong>factores</strong>, y el resultado es el <strong>producto</strong>.</p>""")
R("<h3>Rows and columns (an array)</h3>", "<h3>Filas y columnas (un arreglo)</h3>")
R('<label for="ar-f">Rows: <span id="ar-fv"></span></label>', '<label for="ar-f">Filas: <span id="ar-fv"></span></label>')
R('<label for="ar-c">In each row: <span id="ar-cv"></span></label>', '<label for="ar-c">En cada fila: <span id="ar-cv"></span></label>')
R("<h3>Practice: which multiplication is it?</h3>", "<h3>Practique: ¿qué multiplicación es?</h3>")
# Módulo 2
R('id="tables-properties">', 'id="tablas-propiedades">')
R("<h2>Times tables and properties</h2>", "<h2>Tablas de multiplicar y propiedades</h2>")
R("""<p>It helps to know the tables up to 12 × 12, like a carpenter knows the measurements. Press a square: its row and its column
      light up, and the "twin" square, with the factors switched, turns yellow. It has the same product.</p>""",
  """<p>Ayuda saber las tablas hasta 12 × 12, como el carpintero conoce sus medidas. Pulse una casilla: se iluminan su fila y su columna,
      y la casilla «gemela», con los factores cambiados de lugar, se pone amarilla. Tiene el mismo producto.</p>""")
R("<caption>Properties that make life easier</caption>", "<caption>Propiedades que facilitan la vida</caption>")
R('<th scope="col">Property</th><th scope="col">What it says</th><th scope="col">Example</th>', '<th scope="col">Propiedad</th><th scope="col">Qué dice</th><th scope="col">Ejemplo</th>')
R("<tr><td>Commutative</td><td>the order of the factors does not change the product</td>", "<tr><td>Conmutativa</td><td>el orden de los factores no cambia el producto</td>")
R("<tr><td>Associative</td><td>with three factors, you can group them in any way</td>", "<tr><td>Asociativa</td><td>con tres factores, se pueden agrupar de cualquier forma</td>")
R("<tr><td>Distributive</td><td>you can split a factor into easier parts</td>", "<tr><td>Distributiva</td><td>se puede separar un factor en partes más fáciles</td>")
R("<tr><td>Zero and one</td><td>times 0 is 0; times 1 stays the same</td>", "<tr><td>El cero y el uno</td><td>por 0 da 0; por 1 se queda igual</td>")
R("<h3>Practice: use the distributive property</h3>", "<h3>Practique: use la propiedad distributiva</h3>")
R('<label for="p2-r">Product</label>', '<label for="p2-r">Producto</label>')
# Módulo 3
R('id="one-digit">', 'id="un-digito">')
R("<h2>Multiplying by one digit</h2>", "<h2>Multiplicar por un dígito</h2>")
R("""<p>Multiply each digit, from right to left, and <strong>carry</strong> the same way you do when you add. Add the number you carried
      <strong>after</strong> you multiply the next column.</p>""",
  """<p>Multiplique cada dígito, de derecha a izquierda, y <strong>lleve</strong> igual que al sumar. Sume lo que llevaba
      <strong>después</strong> de multiplicar la columna siguiente.</p>""")
R("<h3>One column at a time</h3>", "<h3>Una columna a la vez</h3>")
R('<label for="m1-a">Number</label>', '<label for="m1-a">Número</label>')
R('<label for="m1-b">Times (one digit)</label>', '<label for="m1-b">Por (un dígito)</label>')
R("<h3>Practice: multiply by one digit</h3>", "<h3>Practique: multiplique por un dígito</h3>")
R('<label for="p3-r">Product</label>', '<label for="p3-r">Producto</label>')
# Módulo 4
R('id="two-digit">', 'id="dos-digitos">')
R("<h2>Multiplying by two digits</h2>", "<h2>Multiplicar por dos dígitos</h2>")
R("""<p>With two digits, find <strong>two partial products</strong> and add them. The second partial product, for the tens, moves
      <strong>one place to the left</strong>. That is why many people write a 0 that "holds the place."</p>""",
  """<p>Con dos dígitos, halle <strong>dos productos parciales</strong> y súmelos. El segundo producto parcial, el de las decenas, se corre
      <strong>un lugar a la izquierda</strong>. Por eso muchas personas escriben un 0 que «guarda el lugar».</p>""")
R("<h3>The two partial products</h3>", "<h3>Los dos productos parciales</h3>")
R('<label for="m2-a">Number</label>', '<label for="m2-a">Número</label>')
R('<label for="m2-b">Times (two digits)</label>', '<label for="m2-b">Por (dos dígitos)</label>')
R("<h3>Practice: multiply by two digits</h3>", "<h3>Practique: multiplique por dos dígitos</h3>")
R('<label for="p4-r">Product</label>', '<label for="p4-r">Producto</label>')
# Módulo 5
R('id="estimate">', 'id="estimar">')
R("<h2>Checking with an estimate</h2>", "<h2>Comprobar con una estimación</h2>")
R("""<p>To see if a product is reasonable, <strong>round the factors</strong> and multiply the round numbers, which is easy. An estimate
      does not give the exact answer, but it is the alarm that catches a missing zero or a partial product in the wrong place.</p>""",
  """<p>Para ver si un producto es razonable, <strong>redondee los factores</strong> y multiplique los números redondos, que es fácil. La estimación
      no da el resultado exacto, pero es la alarma que atrapa un cero que falta o un producto parcial fuera de su lugar.</p>""")
R("<h3>Estimate and compare</h3>", "<h3>Estime y compare</h3>")
R('<label for="es-a">First factor</label>', '<label for="es-a">Primer factor</label>')
R('<label for="es-b">Second factor</label>', '<label for="es-b">Segundo factor</label>')
R("<h3>Practice: is it reasonable?</h3>", "<h3>Practique: ¿es razonable?</h3>")
# Módulo 6
R("<h2>Multiplication bingo</h2>", "<h2>Bingo de multiplicación</h2>")
R("<p>Review the times tables with a game. It opens in a new tab.</p>", "<p>Repase las tablas de multiplicar con un juego. Se abre en una pestaña nueva.</p>")
R("""<a class="tarjeta-ext" href="../games/multiplication-bingo.html" target="_blank" rel="noopener noreferrer"><strong>Multiplication bingo</strong>The tables from 1 to 12, as a game.<span class="ir">Open in a new tab ›</span></a>""",
  """<a class="tarjeta-ext" href="../juegos/bingo-multiplicacion.html" target="_blank" rel="noopener noreferrer"><strong>Bingo de multiplicación</strong>Las tablas del 1 al 12, en forma de juego.<span class="ir">Abrir en una pestaña nueva ›</span></a>""")
R("<p><strong>Level 1 · Topic 2 · Multiplication and division · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 2 · Multiplicación y división · LearnGED</strong><br>")
# ---- Script ----
R("Repeated addition: ' + (f <= 8 ? Array(f).fill(c).join(\" + \") : c + \" + \" + c + \" + … (\" + f + \" times)\")",
  "Suma repetida: ' + (f <= 8 ? Array(f).fill(c).join(\" + \") : c + \" + \" + c + \" + … (\" + f + \" veces)\")")
R("'</div><div class=\"linea\">Factors: ' + f + ' and ' + c + '. Product: ' + f*c + '.</div>'", "'</div><div class=\"linea\">Factores: ' + f + ' y ' + c + '. Producto: ' + f*c + '.</div>'")
R('enun: "Which multiplication does this array show?" + \'<div role="img" aria-label="An array of \' + f + \' rows with \' + c + \' dots in each row.">\'',
  'enun: "¿Qué multiplicación muestra este arreglo?" + \'<div role="img" aria-label="Un arreglo de \' + f + \' filas con \' + c + \' puntos en cada fila.">\'')
R('pistas: { o1: "Do not add the rows and the columns. There are " + f + " equal rows of " + c + ".", o2: "Count the dots in one row again." },',
  'pistas: { o1: "No sume las filas y las columnas. Hay " + f + " filas iguales de " + c + ".", o2: "Cuente otra vez los puntos de una fila." },')
R('bien: f + " rows of " + c + ": " + f + " × " + c + " = " + f*c + ".", mal: "There are " + f + " rows with " + c + " in each row: " + f + " × " + c + " = " + f*c + "." };',
  'bien: f + " filas de " + c + ": " + f + " × " + c + " = " + f*c + ".", mal: "Hay " + f + " filas con " + c + " en cada fila: " + f + " × " + c + " = " + f*c + "." };')
R('enun: "Which multiplication is the same as " + Array(f).fill(c).join(" + ") + "?"', 'enun: "¿Qué multiplicación es lo mismo que " + Array(f).fill(c).join(" + ") + "?"')
R('pistas: { o1: "Count how many times the " + c + " is added.", o2: "Which number is added again and again?", o3: "Count how many times the " + c + " is added." },',
  'pistas: { o1: "Cuente cuántas veces se suma el " + c + ".", o2: "¿Qué número se suma una y otra vez?", o3: "Cuente cuántas veces se suma el " + c + "." },')
R('bien: "The " + c + " is added " + f + " times: " + f + " × " + c + " = " + f*c + ".", mal: "It is the " + c + " added " + f + " times: " + f + " × " + c + " = " + f*c + "." };',
  'bien: "El " + c + " se suma " + f + " veces: " + f + " × " + c + " = " + f*c + ".", mal: "Es el " + c + " sumado " + f + " veces: " + f + " × " + c + " = " + f*c + "." };')
R('<caption class="cap-oculto">Times table from 1 to 12</caption>', '<caption class="cap-oculto">Tabla de multiplicar del 1 al 12</caption>')
R("aria-label=\"' + f + ' times ' + c + '\"", "aria-label=\"' + f + ' por ' + c + '\"")
R('(a === b2 ? "This is a square number: the two factors are the same." : "Its twin, " + b2 + " × " + a + " = " + a*b2 + ", gives the same product: the commutative property.")',
  '(a === b2 ? "Es un número cuadrado: los dos factores son iguales." : "Su gemela, " + b2 + " × " + a + " = " + a*b2 + ", da el mismo producto: la propiedad conmutativa.")')
R('enun: "Use the distributive property to find <strong>" + d + " × " + m + "</strong>. (Hint: " + d + " = " + dec + " + " + u + ")",',
  'enun: "Use la propiedad distributiva para hallar <strong>" + d + " × " + m + "</strong>. (Pista: " + d + " = " + dec + " + " + u + ")",')
R('msg: "Multiply both parts by " + m + ": the " + u + " too." }, { v: d + m, msg: "This is a multiplication, not an addition." }], "Multiply each part by " + m + ", then add the two answers.") };',
  'msg: "Multiplique las dos partes por " + m + ": el " + u + " también." }, { v: d + m, msg: "Esto es una multiplicación, no una suma." }], "Multiplique cada parte por " + m + " y después sume los dos resultados.") };')
R('txt = cap1(PLACE[k]) + ": " + m + " × " + x + " = " + x*m + (c ? ", plus the " + c + " you carried = " + p : "") + ".";',
  'txt = cap1(LUGARES_PL[k]) + ": " + m + " × " + x + " = " + x*m + (c ? ", más el " + c + " que llevaba = " + p : "") + ".";')
R('txt += " This is the last column: write " + p + ".";', 'txt += " Es la última columna: escriba " + p + ".";')
R('txt += c ? " Write " + (p % 10) + " and carry " + c + "." : " Write " + p + ".";', 'txt += c ? " Escriba " + (p % 10) + " y lleve " + c + "." : " Escriba " + p + ".";')
R('"Multiplication in columns, " + PLACE[k]', '"Multiplicación en columnas, " + LUGARES_PL[k]')
R('"Type a number with up to 6 digits and a one-digit factor (0 to 9)."', '"Escriba un número de hasta 6 dígitos y un factor de un dígito (del 0 al 9)."')
R('"Multiplication: " + com(S.a) + " times " + S.m', '"Multiplicación: " + com(S.a) + " por " + S.m')
R("'<div class=\"linea\">Start with the ones. What you carry appears in red at the top.</div>'", "'<div class=\"linea\">Empiece por las unidades. Lo que se lleva aparece en rojo arriba.</div>'")
R('enun: "Find <strong>" + com(a) + " × " + m + "</strong>.", solucion: pasosM1(a, m).pasos.map(function(p){ return p.txt; }).join(" ") + " The product is " + com(r) + ".",',
  'enun: "Calcule <strong>" + com(a) + " × " + m + "</strong>.", solucion: pasosM1(a, m).pasos.map(function(p){ return p.txt; }).join(" ") + " El producto es " + com(r) + ".",')
R('msg: "It looks like the carried numbers were not added. After you multiply each column, add what you carried." }] : [], "Multiply one column at a time, from right to left, and add what you carry.") };',
  'msg: "Parece que no se sumó lo que se llevaba. Después de multiplicar cada columna, sume lo que llevó." }] : [], "Multiplique una columna a la vez, de derecha a izquierda, y sume lo que lleva.") };')
R('txt: "First partial product, by the ones (" + u + "): " + com(a) + " × " + u + " = " + com(p1) + ".", tabla: tab(base, P1, "First partial product: " + com(p1)) });',
  'txt: "Primer producto parcial, por las unidades (" + u + "): " + com(a) + " × " + u + " = " + com(p1) + ".", tabla: tab(base, P1, "Primer producto parcial: " + com(p1)) });')
R('txt: "Second partial product, by the tens (" + d + "): " + com(a) + " × " + d + " = " + com(p2) + ". This " + d + " is worth " + d*10 + ", so move it one place to the left: " + com(p2*10) + " (the gray 0 holds the place).", tabla: tab(base.concat([{ dig: P1 }]), P2v, "Second partial product: " + com(p2*10)) });',
  'txt: "Segundo producto parcial, por las decenas (" + d + "): " + com(a) + " × " + d + " = " + com(p2) + ". Este " + d + " vale " + d*10 + ", así que se corre un lugar a la izquierda: " + com(p2*10) + " (el 0 gris guarda el lugar).", tabla: tab(base.concat([{ dig: P1 }]), P2v, "Segundo producto parcial: " + com(p2*10)) });')
R('txt: "Add the partial products: " + com(p1) + " + " + com(p2*10) + " = " + com(tot) + ".", tabla: tab(base.concat([{ dig: P1 }, { signo: "+", dig: P2v }]), digitos(tot, W), "Sum of the partial products: " + com(tot)) });',
  'txt: "Sume los productos parciales: " + com(p1) + " + " + com(p2*10) + " = " + com(tot) + ".", tabla: tab(base.concat([{ dig: P1 }, { signo: "+", dig: P2v }]), digitos(tot, W), "Suma de los productos parciales: " + com(tot)) });')
R('"Type a number with up to 5 digits and a two-digit factor (10 to 99)."', '"Escriba un número de hasta 5 dígitos y un factor de dos dígitos (del 10 al 99)."')
R('"Multiplication: " + com(S.a) + " times " + S.b', '"Multiplicación: " + com(S.a) + " por " + S.b')
R("'<div class=\"linea\">First multiply by the ones digit of the second factor, then by the tens digit.</div>'", "'<div class=\"linea\">Primero multiplique por el dígito de las unidades del segundo factor y después por el de las decenas.</div>'")
R('enun: "Find <strong>" + com(a) + " × " + b + "</strong>.", solucion: P.pasos', 'enun: "Calcule <strong>" + com(a) + " × " + b + "</strong>.", solucion: P.pasos')
R('msg: "It looks like the second partial product was not moved one place to the left. Write a 0 to hold the place." }, { v: a*(b % 10), msg: "That is only the first partial product. Multiply by the tens too, then add." }], "Find the two partial products, move the second one place to the left, and add.") };',
  'msg: "Parece que el segundo producto parcial no se corrió un lugar a la izquierda. Escriba un 0 que guarde el lugar." }, { v: a*(b % 10), msg: "Ese es solo el primer producto parcial. Multiplique también por las decenas y después sume." }], "Halle los dos productos parciales, corra el segundo un lugar a la izquierda y sume.") };')
R('s.innerHTML = "Type two whole numbers.";', 's.innerHTML = "Escriba dos números enteros.";')
R("""'<div class="linea">Round: ' + com(a) + ' is about ' + com(ra) + ', and ' + com(b) + ' is about ' + com(rb) + '.</div><div class="linea">Estimate: ' + com(ra) + ' × ' + com(rb) + ' = <strong>' + com(ra*rb) + '</strong> (about).</div><div class="linea veredicto">Exact: ' + com(a*b) + ', close to the estimate</div><div class="linea nota">If you got ' + com(Math.round(a*b/10)) + ' or ' + com(a*b*10) + ', the estimate would warn you about a mistake.</div>'""",
  """'<div class="linea">Redondee: ' + com(a) + ' es unos ' + com(ra) + ', y ' + com(b) + ' es unos ' + com(rb) + '.</div><div class="linea">Estimación: ' + com(ra) + ' × ' + com(rb) + ' = <strong>' + com(ra*rb) + '</strong> (aproximadamente).</div><div class="linea veredicto">Exacto: ' + com(a*b) + ', cerca de la estimación</div><div class="linea nota">Si le hubiera dado ' + com(Math.round(a*b/10)) + ' o ' + com(a*b*10) + ', la estimación le avisaría del error.</div>'""")
R('var exp = "Estimate: " + com(ra) + " × " + com(rb) + " = " + com(est) + ". " + (ok ? com(dado) + " is close to it, so it is reasonable." : com(dado) + " is far from " + com(est) + ", so there is a mistake. The correct product is " + com(r) + ".");',
  'var exp = "Estimación: " + com(ra) + " × " + com(rb) + " = " + com(est) + ". " + (ok ? com(dado) + " está cerca, así que es razonable." : com(dado) + " está lejos de " + com(est) + ", así que hay un error. El producto correcto es " + com(r) + ".");')
R('enun: "Someone found <strong>" + com(a) + " × " + b + " = " + com(dado) + "</strong>. Use an estimate: is it reasonable?", opciones: [ { html: "Yes, it is reasonable", clave: "s" }, { html: "No, it is too far off", clave: "n" } ]',
  'enun: "Alguien calculó <strong>" + com(a) + " × " + b + " = " + com(dado) + "</strong>. Use una estimación: ¿es razonable?", opciones: [ { html: "Sí, es razonable", clave: "s" }, { html: "No, está demasiado lejos", clave: "n" } ]')
R("/* ============ MODULE", "/* ============ MÓDULO", 5)
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-2-1.html")
