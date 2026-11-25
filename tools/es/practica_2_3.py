"""Crea es/matematicas/nivel-1/practica-2-3.html a partir de math/level-1/practice-2-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-2-3.html")
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 2.3 · Problemas verbales — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 2.3 · Multiplication and division in word problems · LearnGED</title>", "<title>Práctica · Lección 2.3 · Multiplicación y división en problemas verbales · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 2 · Multiplication and division</div>', '<div class="ruta">Nivel 1 · Tema 2 · Multiplicación y división</div>')
R("<h1>Lesson 2.3 · Multiplication and division in word problems</h1>", "<h1>Lección 2.3 · Multiplicación y división en problemas verbales</h1>")
R("Three practice activities on one page. The exercises change every time, so you can practice as many times as you want. If you make a mistake, you get a hint and another try.",
  "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez, así que puede practicar todas las veces que quiera. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#keywords">Keywords: multiply or divide?</a></li>', '<li><a href="#palabras-clave">Palabras clave: ¿multiplicar o dividir?</a></li>')
R('<li><a href="#four-steps">The 4 steps, again</a></li>', '<li><a href="#cuatro-pasos">Los 4 pasos, otra vez</a></li>')
R('<li><a href="#properties">Properties as shortcuts</a></li>', '<li><a href="#propiedades">Las propiedades como atajos</a></li>')
# 1
R('id="keywords" open>', 'id="palabras-clave" open>'); R("<h2>Keywords: multiply or divide?</h2>", "<h2>Palabras clave: ¿multiplicar o dividir?</h2>")
R("""<p>We <strong>multiply</strong> when there are several equal groups and we want the total. We <strong>divide</strong> when there is a total
      and we want to split it into equal groups, or find how many groups fit.</p>""",
  """<p><strong>Multiplicamos</strong> cuando hay varios grupos iguales y queremos el total. <strong>Dividimos</strong> cuando hay un total
      y queremos repartirlo en grupos iguales, o hallar cuántos grupos caben.</p>""")
R("<caption>Words that point to multiplying or dividing</caption>", "<caption>Palabras que indican multiplicar o dividir</caption>")
R('<th scope="col">✖️ Point to multiplying</th><th scope="col">➗ Point to dividing</th>', '<th scope="col">✖️ Indican multiplicar</th><th scope="col">➗ Indican dividir</th>')
R("<tr><td>each … how many in all?</td><td>split equally, share equally</td></tr>", "<tr><td>cada … ¿cuántos en total?</td><td>repartir en partes iguales, repartir entre</td></tr>")
R("<tr><td>the total of … equal groups</td><td>how much for each person? for each group?</td></tr>", "<tr><td>el total de … grupos iguales</td><td>¿cuánto le toca a cada persona? ¿a cada grupo?</td></tr>")
R("<tr><td>times, twice, double, triple</td><td>how many groups?</td></tr>", "<tr><td>veces, el doble, el triple</td><td>¿cuántos grupos?</td></tr>")
R("<tr><td>per (with the number of groups given)</td><td>half, one third, divided by</td></tr>", "<tr><td>por (cuando se da el número de grupos)</td><td>la mitad, la tercera parte, dividido entre</td></tr>")
R('<strong>"Each" and "per" show up in both kinds of problems.</strong> Picture the situation: are equal groups coming together (multiply), or is a total being split (divide)?',
  '<strong>«Cada» y «por» aparecen en los dos tipos de problema.</strong> Imagine la situación: ¿se juntan grupos iguales (multiplicar) o se reparte un total (dividir)?')
R("<h3>Practice: multiply or divide?</h3>", "<h3>Practique: ¿multiplicar o dividir?</h3>")
# 2
R('id="four-steps">', 'id="cuatro-pasos">'); R("<h2>The 4 steps, again</h2>", "<h2>Los 4 pasos, otra vez</h2>")
R("<p>The method from Lesson 1.3 works here too. In step 4, if there is a remainder, decide what to do with it.</p>", "<p>El método de la Lección 1.3 también sirve aquí. En el paso 4, si hay residuo, decida qué hacer con él.</p>")
R("<h3>Solve with the 4 steps</h3>", "<h3>Resuelva con los 4 pasos</h3>")
R('id="cp-nuevo">New problem</button>', 'id="cp-nuevo">Otro problema</button>')
R("<h3>Practice: solve the problem</h3>", "<h3>Practique: resuelva el problema</h3>")
R('<label for="p2-r">Answer</label>', '<label for="p2-r">Respuesta</label>')
R('<p class="nota">Type the number only, without units or $.</p>', '<p class="nota">Escriba solo el número, sin unidades ni $.</p>')
# 3
R('id="properties">', 'id="propiedades">'); R("<h2>Properties as shortcuts</h2>", "<h2>Las propiedades como atajos</h2>")
R("<caption>How each property helps</caption>", "<caption>Cómo ayuda cada propiedad</caption>")
R('<th scope="col">Property</th><th scope="col">What it says</th><th scope="col">How it helps</th>', '<th scope="col">Propiedad</th><th scope="col">Qué dice</th><th scope="col">Cómo ayuda</th>')
R("<tr><td>Commutative</td><td>6 × 9 = 9 × 6</td><td>put the factors in the easiest order</td></tr>", "<tr><td>Conmutativa</td><td>6 × 9 = 9 × 6</td><td>poner los factores en el orden más fácil</td></tr>")
R("<tr><td>Associative</td><td>(2 × 5) × 7 = 2 × (5 × 7)</td><td>group first what gives a round number (2 × 5 = 10)</td></tr>", "<tr><td>Asociativa</td><td>(2 × 5) × 7 = 2 × (5 × 7)</td><td>agrupar primero lo que da un número redondo (2 × 5 = 10)</td></tr>")
R("<tr><td>Distributive</td><td>25 × 4 = (20 × 4) + (5 × 4)</td><td>turn one hard multiplication into two easy ones</td></tr>", "<tr><td>Distributiva</td><td>25 × 4 = (20 × 4) + (5 × 4)</td><td>convertir una multiplicación difícil en dos fáciles</td></tr>")
R("<tr><td>Zero and one</td><td>n × 0 = 0 · n × 1 = n</td><td>immediate answer, no calculation</td></tr>", "<tr><td>Cero y uno</td><td>n × 0 = 0 · n × 1 = n</td><td>resultado inmediato, sin cálculo</td></tr>")
R("<h3>Practice: which property is it?</h3>", "<h3>Practique: ¿qué propiedad es?</h3>")
R("<h3>Practice: calculate in your head with a shortcut</h3>", "<h3>Practique: calcule de memoria con un atajo</h3>")
R('<label for="p4-r">Answer</label>', '<label for="p4-r">Respuesta</label>')
R("<p><strong>Level 1 · Topic 2 · Multiplication and division · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 2 · Multiplicación y división · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ MODULE 1 · keywords ============ */", "/* ============ MÓDULO 1 · palabras clave ============ */")
R('''var FR = [["A pack has 12 bars of soap. How many bars are in 15 packs?", "m"], ["384 boxes are split equally among 8 trucks. How many boxes does each truck get?", "d"], ["Each ticket costs $9. How much do 6 tickets cost?", "m"], ["How many teams of 5 can you make with 45 people?", "d"], ["A hall has 18 rows with 24 chairs in each row. How many chairs?", "m"], ["4 friends share $96 equally. How much does each one get?", "d"], ["She earns $15 per hour and works 8 hours. How much does she earn?", "m"], ["Half of the 150 students take the bus. How many take the bus?", "d"], ["What is triple 35?", "m"], ["How many bags of 6 oranges can you fill with 72 oranges?", "d"], ["A car goes 30 miles per gallon. How far does it go on 12 gallons?", "m"], ["A pizza has 8 slices for 4 people. How many slices does each person get?", "d"], ["180 bars of soap are packed 12 in each box. How many boxes?", "d"], ["Each box has 12 bars of soap. How many bars are in 15 boxes?", "m"]];''',
  '''var FR = [["Un paquete trae 12 barras de jabón. ¿Cuántas barras hay en 15 paquetes?", "m"], ["Se reparten 384 cajas en partes iguales entre 8 camiones. ¿Cuántas cajas le tocan a cada camión?", "d"], ["Cada boleto cuesta $9. ¿Cuánto cuestan 6 boletos?", "m"], ["¿Cuántos equipos de 5 se pueden formar con 45 personas?", "d"], ["Un salón tiene 18 filas con 24 sillas en cada fila. ¿Cuántas sillas hay?", "m"], ["4 amigos se reparten $96 en partes iguales. ¿Cuánto le toca a cada uno?", "d"], ["Ella gana $15 por hora y trabaja 8 horas. ¿Cuánto gana?", "m"], ["La mitad de los 150 estudiantes va en autobús. ¿Cuántos van en autobús?", "d"], ["¿Cuánto es el triple de 35?", "m"], ["¿Cuántas bolsas de 6 naranjas se pueden llenar con 72 naranjas?", "d"], ["Un carro recorre 30 millas por galón. ¿Cuánto recorre con 12 galones?", "m"], ["Una pizza tiene 8 pedazos para 4 personas. ¿Cuántos pedazos le tocan a cada persona?", "d"], ["Se empacan 180 barras de jabón, 12 en cada caja. ¿Cuántas cajas hay?", "d"], ["Cada caja trae 12 barras de jabón. ¿Cuántas barras hay en 15 cajas?", "m"]];''')
R('''enun: "<em>“" + f[0] + "”</em> Which operation do you need?", opciones: [ { html: "✖️ Multiply", clave: "m" }, { html: "➗ Divide", clave: "d" } ]''', '''enun: "<em>«" + f[0] + "»</em> ¿Qué operación necesita?", opciones: [ { html: "✖️ Multiplicar", clave: "m" }, { html: "➗ Dividir", clave: "d" } ]''')
R('''bien: f[1] === "m" ? "Equal groups come together, and you want the total: multiply." : "A total is split into equal groups, or you find how many groups fit: divide.",''',
  '''bien: f[1] === "m" ? "Se juntan grupos iguales y quiere el total: se multiplica." : "Se reparte un total en grupos iguales, o se halla cuántos grupos caben: se divide.",''')
R('''mal: f[1] === "m" ? "Here you know the groups and want the total, so you multiply." : "Here you know the total and split it into equal groups, so you divide." }; }''',
  '''mal: f[1] === "m" ? "Aquí conoce los grupos y quiere el total, así que se multiplica." : "Aquí conoce el total y lo reparte en grupos iguales, así que se divide." }; }''')
R("/* Word problems */", "/* Problemas verbales */")
R('txt = "A hall has " + a + " rows of chairs. Each row has " + b + " chairs."; preg = "How many chairs are there in all?"; uni = "chairs"; r = a*b; sentido = com(r) + " chairs in " + a + " rows is reasonable"; }',
  'txt = "Un salón tiene " + a + " filas de sillas. Cada fila tiene " + b + " sillas."; preg = "¿Cuántas sillas hay en total?"; uni = "sillas"; r = a*b; sentido = com(r) + " sillas en " + a + " filas es razonable"; }')
R('txt = "A company splits " + com(a) + " boxes equally among " + b + " trucks."; preg = "How many boxes does each truck carry?"; uni = "boxes"; r = q; sentido = "each truck carries part of the total. Check: " + q + " " + X + " " + b + " = " + com(a); }',
  'txt = "Una compañía reparte " + com(a) + " cajas en partes iguales entre " + b + " camiones."; preg = "¿Cuántas cajas lleva cada camión?"; uni = "cajas"; r = q; sentido = "cada camión lleva una parte del total. Comprobación: " + q + " " + X + " " + b + " = " + com(a); }')
R('txt = "A pack has " + per + " bars of soap."; preg = "How many bars are in " + packs + " packs?"; uni = "bars"; r = per*packs; a = packs; b = per; sentido = "many packs hold more bars than one pack"; }',
  'txt = "Un paquete trae " + per + " barras de jabón."; preg = "¿Cuántas barras hay en " + packs + " paquetes?"; uni = "barras"; r = per*packs; a = packs; b = per; sentido = "muchos paquetes traen más barras que un solo paquete"; }')
R('txt = com(a) + " students are split equally among " + b + " classrooms."; preg = "How many students are in each classroom?"; uni = "students"; r = q; sentido = "each classroom has part of the total. Check: " + q + " " + X + " " + b + " = " + com(a); }',
  'txt = "Se reparten " + com(a) + " estudiantes en partes iguales entre " + b + " salones."; preg = "¿Cuántos estudiantes hay en cada salón?"; uni = "estudiantes"; r = q; sentido = "cada salón tiene una parte del total. Comprobación: " + q + " " + X + " " + b + " = " + com(a); }')
R('txt = "A person earns $" + a + " per hour and works " + b + " hours a week."; preg = "How much does the person earn in a week?"; r = a*b; sentido = "a week of work pays more than one hour"; }',
  'txt = "Una persona gana $" + a + " por hora y trabaja " + b + " horas a la semana."; preg = "¿Cuánto gana en una semana?"; r = a*b; sentido = "una semana de trabajo paga más que una hora"; }')
R('txt = a + " people are going on a trip in vans with " + b + " seats."; preg = "How many vans do they need?"; uni = "vans"; r = q + 1; extra = a + " " + D + " " + b + " = " + q + ", remainder " + rr + ". Everyone has to go, so round up."; sentido = q + " vans leave " + rr + " " + (rr === 1 ? "person" : "people") + " without a seat"; }',
  'txt = a + " personas van de excursión en camionetas de " + b + " asientos."; preg = "¿Cuántas camionetas necesitan?"; uni = "camionetas"; r = q + 1; extra = a + " " + D + " " + b + " = " + q + ", residuo " + rr + ". Tienen que ir todos, así que se redondea hacia arriba."; sentido = "con " + q + " camionetas, " + rr + " " + (rr === 1 ? "persona se queda" : "personas se quedan") + " sin asiento"; }')
R('txt = "You have $" + a + " to buy books that cost $" + b + " each."; preg = "How many whole books can you buy?"; uni = "books"; r = q; extra = a + " " + D + " " + b + " = " + q + ", remainder " + r4 + ". The $" + r4 + " left over is not enough for another book, so drop the remainder."; sentido = "only whole books count"; }',
  'txt = "Tiene $" + a + " para comprar libros de $" + b + " cada uno."; preg = "¿Cuántos libros completos puede comprar?"; uni = "libros"; r = q; extra = a + " " + D + " " + b + " = " + q + ", residuo " + r4 + ". Los $" + r4 + " que sobran no alcanzan para otro libro, así que se descarta el residuo."; sentido = "solo cuentan los libros completos"; }')
R('txt = "A car goes " + a + " miles per gallon of gas."; preg = "How many miles does it go on " + b + " gallons?"; uni = "miles"; r = a*b; sentido = "more gallons take you more miles"; }',
  'txt = "Un carro recorre " + a + " millas por galón de gasolina."; preg = "¿Cuántas millas recorre con " + b + " galones?"; uni = "millas"; r = a*b; sentido = "con más galones se recorren más millas"; }')
R("/* ============ MODULE 2 · four steps (guided) ============ */", "/* ============ MÓDULO 2 · cuatro pasos (guiado) ============ */")
R('"Problems solved: " + CP.total + " (" + CP.primero + " on the first try)"', '"Problemas resueltos: " + CP.total + " (" + CP.primero + " al primer intento)"')
R("<strong>Read and underline.</strong> Numbers: <strong>", "<strong>Lea y subraye.</strong> Números: <strong>")
R("'</strong> and <strong>' + com(q.b)", "'</strong> y <strong>' + com(q.b)")
R('<strong>Choose the operation:</strong> <span class="signos" role="group" aria-label="Operation"><button type="button" id="cp-x" aria-label="Multiply" aria-pressed="false">', '<strong>Elija la operación:</strong> <span class="signos" role="group" aria-label="Operación"><button type="button" id="cp-x" aria-label="Multiplicar" aria-pressed="false">')
R('<button type="button" id="cp-d" aria-label="Divide" aria-pressed="false">', '<button type="button" id="cp-d" aria-label="Dividir" aria-pressed="false">')
R('porque = q.op === X ? "there are equal groups and you want the total" : "you split a total or find how many groups fit";', 'porque = q.op === X ? "hay grupos iguales y quiere el total" : "se reparte un total o se halla cuántos grupos caben";')
R('fb.innerHTML = "<strong>Not this time.</strong> It is " + (q.op === X ? "a multiplication" : "a division") + ": " + porque + ". Let’s go on with step 3."; }',
  'fb.innerHTML = "<strong>Esta vez no.</strong> Es " + (q.op === X ? "una multiplicación" : "una división") + ": " + porque + ". Sigamos con el paso 3."; }')
R('fb.innerHTML = "✓ Correct: it is " + (q.op === X ? "a multiplication" : "a division") + ", because " + porque + "."; }', 'fb.innerHTML = "✓ Correcto: es " + (q.op === X ? "una multiplicación" : "una división") + ", porque " + porque + "."; }')
R("<strong>Solve:</strong> ' + com(q.a)", "<strong>Resuelva:</strong> ' + com(q.a)")
R("(q.extra ? ' (and decide what to do with the remainder)' : '') + '. Answer:</label>", "(q.extra ? ' (y decida qué hacer con el residuo)' : '') + '. Respuesta:</label>")
R('fb.innerHTML = "Type the answer using digits only."; return; }', 'fb.innerHTML = "Escriba la respuesta solo con dígitos."; return; }')
R('fb.innerHTML = "<strong>Not yet.</strong> " + (q.extra && v === otro ? "Think about the remainder: " + q.sentido + "." : "Check your work one step at a time.") + " <strong>You have one more try.</strong>";',
  'fb.innerHTML = "<strong>Todavía no.</strong> " + (q.extra && v === otro ? "Piense en el residuo: " + q.sentido + "." : "Revise su trabajo paso a paso.") + " <strong>Le queda un intento más.</strong>";')
R('fb.innerHTML = "✓ Correct. <em>"', 'fb.innerHTML = "✓ Correcto. <em>"')
R('fb.innerHTML = "<strong>Here is the answer.</strong> "', 'fb.innerHTML = "<strong>Esta es la respuesta.</strong> "')
R("<strong>Does it make sense?</strong> ' + (q.extra ? q.extra + \" \" : \"\") + 'Yes: ' + q.sentido + '. <strong>Answer: ' + q.fmt(q.r) + '.</strong></div>'",
  "<strong>¿Tiene sentido?</strong> ' + (q.extra ? q.extra + \" \" : \"\") + 'Sí: ' + q.sentido + '. <strong>Respuesta: ' + q.fmt(q.r) + '.</strong></div>'")
R('msg: "Think about the remainder: " + q.sentido + "." }); }', 'msg: "Piense en el residuo: " + q.sentido + "." }); }')
R('msg: "Equal groups come together: multiply, do not add." });', 'msg: "Se juntan grupos iguales: multiplique; no sume." });')
R('msg: "You split a total: divide, do not multiply." });', 'msg: "Se reparte un total: divida; no multiplique." });')
R('solucion: q.extra ? q.extra + " Answer: " + q.fmt(q.r) + "." : com(q.a) + " " + q.op + " " + com(q.b) + " = " + com(q.r) + ". Answer: " + q.fmt(q.r) + ".",',
  'solucion: q.extra ? q.extra + " Respuesta: " + q.fmt(q.r) + "." : com(q.a) + " " + q.op + " " + com(q.b) + " = " + com(q.r) + ". Respuesta: " + q.fmt(q.r) + ".",')
R('"Decide first: equal groups (multiply) or splitting a total (divide)? Then calculate step by step."', '"Decida primero: ¿grupos iguales (multiplicar) o repartir un total (dividir)? Después calcule paso a paso."')
R("/* ============ MODULE 3 · properties ============ */", "/* ============ MÓDULO 3 · propiedades ============ */")
R('var nom = { c: "Commutative", a: "Associative", d: "Distributive", z: "Zero property", u: "One property" };', 'var nom = { c: "Conmutativa", a: "Asociativa", d: "Distributiva", z: "Propiedad del cero", u: "Propiedad del uno" };\n  var nomLargo = { c: "la propiedad conmutativa", a: "la propiedad asociativa", d: "la propiedad distributiva", z: "la propiedad del cero", u: "la propiedad del uno" };')
R('var exp = { c: "The order of the factors changed.", a: "The grouping changed (look at the parentheses).", d: "A factor was split into two parts.", z: "Any number times 0 is 0.", u: "Any number times 1 stays the same." };',
  'var exp = { c: "Cambió el orden de los factores.", a: "Cambió la agrupación (fíjese en los paréntesis).", d: "Un factor se separó en dos partes.", z: "Cualquier número por 0 da 0.", u: "Cualquier número por 1 queda igual." };')
R('var pistas = { c: "Did the order of the factors change?", a: "Look at the parentheses. Did the grouping change?", d: "Was a factor split into parts?", z: "Is there a zero?", u: "Is there a 1?" };',
  'var pistas = { c: "¿Cambió el orden de los factores?", a: "Fíjese en los paréntesis. ¿Cambió la agrupación?", d: "¿Se separó un factor en partes?", z: "¿Hay un cero?", u: "¿Hay un 1?" };')
R('''"</strong> is an example of which property?", opciones: o, correcta: cor, pistas: pistas, bien: exp[cor], mal: "It is the " + nom[cor].toLowerCase().replace(" property", "") + " property: " + exp[cor].charAt(0).toLowerCase() + exp[cor].slice(1) };''',
  '''"</strong> es un ejemplo de ¿qué propiedad?", opciones: o, correcta: cor, pistas: pistas, bien: exp[cor], mal: "Es " + nomLargo[cor] + ": " + exp[cor].charAt(0).toLowerCase() + exp[cor].slice(1) };''')
R('enun = "Find <strong>" + n + " " + X + " " + m + "</strong> in your head with the distributive property.";', 'enun = "Calcule <strong>" + n + " " + X + " " + m + "</strong> de memoria con la propiedad distributiva.";')
R('p.push({ v: dec*m + (n - dec), msg: "Multiply both parts by " + m + ": the " + (n - dec) + " too." }); }', 'p.push({ v: dec*m + (n - dec), msg: "Multiplique las dos partes por " + m + ": el " + (n - dec) + " también." }); }')
R('enun = "Find <strong>2 " + X + " " + x + " " + X + " 5</strong> in your head. (Hint: group the 2 with the 5.)";', 'enun = "Calcule <strong>2 " + X + " " + x + " " + X + " 5</strong> de memoria. (Pista: agrupe el 2 con el 5.)";')
R('enun = "Find <strong>4 " + X + " " + y + " " + X + " 25</strong> in your head. (Hint: 4 " + X + " 25 = 100.)";', 'enun = "Calcule <strong>4 " + X + " " + y + " " + X + " 25</strong> de memoria. (Pista: 4 " + X + " 25 = 100.)";')
R('"Use the hint: make a round number first, then multiply."', '"Use la pista: forme primero un número redondo y después multiplique."')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-2-3.html")
