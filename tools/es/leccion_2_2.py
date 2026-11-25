"""Crea es/matematicas/nivel-1/leccion-2-2.html a partir de math/level-1/lesson-2-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-2-2.html"); t.leccion("")
R = t.r
t.cabecera("<!-- LearnGED · Lección 2.2 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 2.2 · Dividing whole numbers · LearnGED</title>", "<title>Lección 2.2 · División de números enteros · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 2 — Multiplication and division</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 2 — Multiplicación y división</p>')
R("<h1>Lesson 2.2 · Dividing whole numbers</h1>", "<h1>Lección 2.2 · División de números enteros</h1>")
R('<p class="lema">Long division step by step and, most important, what to do with the remainder in a real problem.</p>', '<p class="lema">La división larga paso a paso y, lo más importante, qué hacer con el residuo en un problema real.</p>')
R("Divide · Multiply · Subtract · Bring down</span>", "Dividir · Multiplicar · Restar · Bajar</span>")
R("<li><strong>Divide</strong> whole numbers by one-digit and two-digit numbers with long division.</li>", "<li><strong>Dividir</strong> números enteros entre números de uno y de dos dígitos con la división larga.</li>")
R("<li><strong>Find</strong> the remainder of a division.</li>", "<li><strong>Hallar</strong> el residuo de una división.</li>")
R("<li><strong>Decide</strong> what the remainder means in a problem: give it as the answer, round the quotient up, or drop it.</li>", "<li><strong>Decidir</strong> qué significa el residuo en un problema: darlo como respuesta, redondear el cociente hacia arriba o descartarlo.</li>")
R("<li><strong>Check</strong> a division with multiplication.</li>", "<li><strong>Comprobar</strong> una división con la multiplicación.</li>")
R('<li><a href="#s-meaning">What does dividing mean?</a></li>', '<li><a href="#s-significado">¿Qué significa dividir?</a></li>')
R('<li><a href="#s-long-division">Long division, step by step</a></li>', '<li><a href="#s-division-larga">La división larga, paso a paso</a></li>')
R('<li><a href="#s-remainder">When it does not divide evenly: the remainder</a></li>', '<li><a href="#s-residuo">Cuando no da exacto: el residuo</a></li>')
R('<li><a href="#s-what-to-do">The most important part: what do I do with the remainder?</a></li>', '<li><a href="#s-que-hacer">Lo más importante: ¿qué hago con el residuo?</a></li>')
# 1
R('<h2 id="s-meaning"><span aria-hidden="true" class="num-seccion">1</span>What does dividing mean?</h2>', '<h2 id="s-significado"><span aria-hidden="true" class="num-seccion">1</span>¿Qué significa dividir?</h2>')
R("<p>In Lesson 2.1 you learned to multiply. Division is its <strong>opposite operation</strong>. Multiplying puts equal groups together. Dividing <strong>splits a total into equal groups</strong>, or finds <strong>how many groups fit</strong>.</p>",
  "<p>En la Lección 2.1 aprendió a multiplicar. La división es su <strong>operación contraria</strong>. Multiplicar junta grupos iguales. Dividir <strong>reparte un total en grupos iguales</strong>, o halla <strong>cuántos grupos caben</strong>.</p>")
R("<p>Imagine you have <strong>24 chairs</strong> and you want to set them up in <strong>rows of 6</strong>. The question \"How many rows can you make?\" is a division: <strong>24 ÷ 6 = 4</strong> rows.</p>",
  "<p>Imagine que tiene <strong>24 sillas</strong> y quiere acomodarlas en <strong>filas de 6</strong>. La pregunta «¿Cuántas filas puede formar?» es una división: <strong>24 ÷ 6 = 4</strong> filas.</p>")
R('aria-label="24 squares split into 4 groups of 6."', 'aria-label="24 cuadritos repartidos en 4 grupos de 6."')
R("<p>In <strong>24 ÷ 6 = 4</strong>: 24 is the <strong>dividend</strong> (the total you split), 6 is the <strong>divisor</strong> (the size of each group, or how many groups), and 4 is the <strong>quotient</strong> (the answer). If something is left over, that is the <strong>remainder</strong>.</p>",
  "<p>En <strong>24 ÷ 6 = 4</strong>: 24 es el <strong>dividendo</strong> (el total que se reparte), 6 es el <strong>divisor</strong> (el tamaño de cada grupo, o cuántos grupos hay) y 4 es el <strong>cociente</strong> (el resultado). Si sobra algo, eso es el <strong>residuo</strong>.</p>")
R('href="practice-2-2.html#meaning"', 'href="practica-2-2.html#significado"')
R('what dividing means (se abre', 'qué significa dividir (se abre')
R('<span class="ei-titulo">Practique más: what dividing means</span><span class="ei-sub">Split a total into equal groups and name the dividend, divisor, and quotient.</span>', '<span class="ei-titulo">Practique más: qué significa dividir</span><span class="ei-sub">Reparta un total en grupos iguales y nombre el dividendo, el divisor y el cociente.</span>')
# 2
R('<h2 id="s-long-division"><span aria-hidden="true" class="num-seccion">2</span>Long division, step by step</h2>', '<h2 id="s-division-larga"><span aria-hidden="true" class="num-seccion">2</span>La división larga, paso a paso</h2>')
R("<p>To divide big numbers we use <strong>long division</strong>. You repeat the same cycle of four steps until there are no more digits:</p>", "<p>Para dividir números grandes usamos la <strong>división larga</strong>. Se repite el mismo ciclo de cuatro pasos hasta que no quedan dígitos:</p>")
R('<p class="titulo-ej">The cycle</p>', '<p class="titulo-ej">El ciclo</p>')
R('<p class="paso"><span aria-hidden="true" class="n">D</span><strong>Divide.</strong> How many times does the divisor fit? Write that number in the quotient.</p><p class="paso"><span aria-hidden="true" class="n">M</span><strong>Multiply.</strong> Multiply the divisor by that number.</p><p class="paso"><span aria-hidden="true" class="n">S</span><strong>Subtract.</strong> Subtract that product to see what is left.</p><p class="paso"><span aria-hidden="true" class="n">B</span><strong>Bring down.</strong> Bring down the next digit and start the cycle again.</p>',
  '<p class="paso"><span aria-hidden="true" class="n">D</span><strong>Dividir.</strong> ¿Cuántas veces cabe el divisor? Escriba ese número en el cociente.</p><p class="paso"><span aria-hidden="true" class="n">M</span><strong>Multiplicar.</strong> Multiplique el divisor por ese número.</p><p class="paso"><span aria-hidden="true" class="n">R</span><strong>Restar.</strong> Reste ese producto para ver cuánto queda.</p><p class="paso"><span aria-hidden="true" class="n">B</span><strong>Bajar.</strong> Baje el dígito siguiente y empiece otra vez el ciclo.</p>')
R('<p class="titulo-ej">Example: 738 ÷ 6</p>', '<p class="titulo-ej">Ejemplo: 738 ÷ 6</p>')
R("<p>Work from left to right.</p>", "<p>Trabaje de izquierda a derecha.</p>")
R('<strong>Divide:</strong> how many times does 6 fit in 7? <strong>1</strong> time. Write 1 in the quotient.', '<strong>Dividir:</strong> ¿cuántas veces cabe 6 en 7? <strong>1</strong> vez. Escriba 1 en el cociente.')
R('<strong>Multiply and subtract:</strong> 1 × 6 = 6. Then 7 − 6 = 1.', '<strong>Multiplicar y restar:</strong> 1 × 6 = 6. Después, 7 − 6 = 1.')
R('<strong>Bring down</strong> the 3. Now you have 13.', '<strong>Bajar</strong> el 3. Ahora tiene 13.')
R('<strong>Divide:</strong> how many times does 6 fit in 13? <strong>2</strong> times. 2 × 6 = 12, and 13 − 12 = 1.', '<strong>Dividir:</strong> ¿cuántas veces cabe 6 en 13? <strong>2</strong> veces. 2 × 6 = 12, y 13 − 12 = 1.')
R('<strong>Bring down</strong> the 8. Now you have 18.', '<strong>Bajar</strong> el 8. Ahora tiene 18.')
R('<strong>Divide:</strong> how many times does 6 fit in 18? Exactly <strong>3</strong> times. 3 × 6 = 18, and 18 − 18 = 0.', '<strong>Dividir:</strong> ¿cuántas veces cabe 6 en 18? Exactamente <strong>3</strong> veces. 3 × 6 = 18, y 18 − 18 = 0.')
R('<strong>Result:</strong> the quotient is <strong>123</strong>, and the remainder is 0.', '<strong>Resultado:</strong> el cociente es <strong>123</strong> y el residuo es 0.')
R('aria-label="738 divided by 6 in long division. The quotient is 123 and the remainder is 0."', 'aria-label="738 entre 6 en división larga. El cociente es 123 y el residuo es 0."')
R("<p>The remainder must always be <strong>smaller than the divisor</strong>. If you subtract and get a number that is equal to or bigger than the divisor, the digit in the quotient is too small. Make it bigger.</p>",
  "<p>El residuo siempre tiene que ser <strong>menor que el divisor</strong>. Si al restar le da un número igual o mayor que el divisor, el dígito del cociente es demasiado pequeño. Auméntelo.</p>")
R('<span class="etiqueta et-ambar">Watch out for zeros in the quotient</span>', '<span class="etiqueta et-ambar">Cuidado con los ceros en el cociente</span>')
R("<p>If the divisor does not fit, write <strong>0</strong> in the quotient before you bring down the next digit. Example: <strong>624 ÷ 6</strong>. 6 fits in 6 one time. Bring down the 2: 6 does not fit in 2, so write <strong>0</strong>. Bring down the 4: 24 ÷ 6 = 4. The answer is <strong>104</strong>, not 14.</p>",
  "<p>Si el divisor no cabe, escriba <strong>0</strong> en el cociente antes de bajar el dígito siguiente. Ejemplo: <strong>624 ÷ 6</strong>. 6 cabe en 6 una vez. Baje el 2: 6 no cabe en 2, así que escriba <strong>0</strong>. Baje el 4: 24 ÷ 6 = 4. El resultado es <strong>104</strong>, no 14.</p>")
R('aria-label="624 divided by 6 in long division. The quotient is 104: there is a 0 in the tens place."', 'aria-label="624 entre 6 en división larga. El cociente es 104: hay un 0 en el lugar de las decenas."')
R('href="practice-2-2.html#long-division"', 'href="practica-2-2.html#division-larga"')
R('long division (se abre', 'la división larga (se abre')
R('<span class="ei-titulo">Practique más: long division</span><span class="ei-sub">Go through divide, multiply, subtract, and bring down until you finish.</span>', '<span class="ei-titulo">Practique más: la división larga</span><span class="ei-sub">Recorra dividir, multiplicar, restar y bajar hasta terminar.</span>')
# 3
R('<h2 id="s-remainder"><span aria-hidden="true" class="num-seccion">3</span>When it does not divide evenly: the remainder</h2>', '<h2 id="s-residuo"><span aria-hidden="true" class="num-seccion">3</span>Cuando no da exacto: el residuo</h2>')
R("<p>Not every division comes out even. When something is left over, that amount is the <strong>remainder</strong>.</p>", "<p>No todas las divisiones dan exacto. Cuando sobra algo, esa cantidad es el <strong>residuo</strong>.</p>")
R('<p class="titulo-ej">Example: 50 ÷ 7</p>', '<p class="titulo-ej">Ejemplo: 50 ÷ 7</p>')
R('How many times does 7 fit in 50? <strong>7</strong> times, because 7 × 7 = 49. (8 × 7 = 56 is too much.)', '¿Cuántas veces cabe 7 en 50? <strong>7</strong> veces, porque 7 × 7 = 49. (8 × 7 = 56 es demasiado.)')
R('Subtract: 50 − 49 = <strong>1</strong>. That 1 is the remainder, and it is smaller than 7 ✓.', 'Reste: 50 − 49 = <strong>1</strong>. Ese 1 es el residuo, y es menor que 7 ✓.')
R('<strong>Result:</strong> 50 ÷ 7 = 7, remainder 1. Many books write this as <strong>7 R1</strong>.', '<strong>Resultado:</strong> 50 ÷ 7 = 7, residuo 1. Muchos libros lo escriben <strong>7 R1</strong>.')
R('<span class="etiqueta et-verde">Check a division with multiplication</span>', '<span class="etiqueta et-verde">Comprobar una división con la multiplicación</span>')
R("<p>(quotient × divisor) + remainder must equal the dividend.<br>50 ÷ 7 = 7, remainder 1 → (7 × 7) + 1 = 49 + 1 = 50 ✓</p>", "<p>(cociente × divisor) + residuo tiene que dar el dividendo.<br>50 ÷ 7 = 7, residuo 1 → (7 × 7) + 1 = 49 + 1 = 50 ✓</p>")
R("<h3>Practice 1 — Division with a remainder</h3>", "<h3>Práctica 1 — División con residuo</h3>")
R("What is <strong>85 ÷ 4</strong>?", "¿Cuánto es <strong>85 ÷ 4</strong>?")
for a, b in [("20, remainder 5", "20, residuo 5"), ("21, remainder 1", "21, residuo 1"), ("21, remainder 0", "21, residuo 0"), ("22, remainder 3", "22, residuo 3")]:
    R('type="button">' + a + "</button>", 'type="button">' + b + "</button>")
R('href="practice-2-2.html#remainder"', 'href="practica-2-2.html#residuo"')
R('práctica: the remainder (se abre', 'práctica: el residuo (se abre')
R('<span class="ei-titulo">Practique más: the remainder</span><span class="ei-sub">Find what is left over and check it with quotient × divisor + remainder.</span>', '<span class="ei-titulo">Practique más: el residuo</span><span class="ei-sub">Halle lo que sobra y compruébelo con cociente × divisor + residuo.</span>')
# 4
R('<h2 id="s-what-to-do"><span aria-hidden="true" class="num-seccion">4</span>The most important part: what do I do with the remainder?</h2>', '<h2 id="s-que-hacer"><span aria-hidden="true" class="num-seccion">4</span>Lo más importante: ¿qué hago con el residuo?</h2>')
R("<p>Finding the remainder is only half of the work. The other half, and the more important one, is deciding <strong>what the remainder means</strong> in the real situation. There are three possibilities, and the problem tells you which one to use.</p>",
  "<p>Hallar el residuo es solo la mitad del trabajo. La otra mitad, la más importante, es decidir <strong>qué significa el residuo</strong> en la situación real. Hay tres posibilidades, y el problema le dice cuál usar.</p>")
R("<p>Three problems, the same calculation: <strong>26 ÷ 4 = 6, remainder 2</strong>.</p>", "<p>Tres problemas, el mismo cálculo: <strong>26 ÷ 4 = 6, residuo 2</strong>.</p>")
R('<strong>Give the remainder.</strong> <em>"There are 26 rolls of bread to pack in 4 equal boxes. How many rolls are left over?"</em> The answer is the remainder: <strong>2 rolls</strong> are left over.',
  '<strong>Dar el residuo.</strong> <em>«Hay 26 panes para empacar en 4 cajas iguales. ¿Cuántos panes sobran?»</em> La respuesta es el residuo: sobran <strong>2 panes</strong>.')
R('<strong>Round the quotient up.</strong> <em>"26 people are traveling in cars that hold 4 people each. How many cars do they need?"</em> 6 cars are not enough: 2 people would stay behind. They need one more car: <strong>7 cars</strong>.',
  '<strong>Redondear el cociente hacia arriba.</strong> <em>«26 personas viajan en carros donde caben 4 personas en cada uno. ¿Cuántos carros necesitan?»</em> 6 carros no alcanzan: 2 personas se quedarían. Necesitan un carro más: <strong>7 carros</strong>.')
R('<strong>Drop the remainder.</strong> <em>"I have $26, and each ticket costs $4. How many tickets can I buy?"</em> Only whole tickets count: <strong>6 tickets</strong>. The $2 left over is not enough for another one.',
  '<strong>Descartar el residuo.</strong> <em>«Tengo $26 y cada boleto cuesta $4. ¿Cuántos boletos puedo comprar?»</em> Solo cuentan los boletos completos: <strong>6 boletos</strong>. Los $2 que sobran no alcanzan para otro.')
R('<span class="etiqueta et-verde">The question that decides it all</span>', '<span class="etiqueta et-verde">La pregunta que lo decide todo</span>')
R("<p>Ask yourself: does the problem ask for <strong>what is left over</strong>, for <strong>full groups</strong>, or for <strong>enough room for everyone</strong>? The answer tells you whether to give the remainder, drop it, or round up.</p>",
  "<p>Pregúntese: ¿el problema pide <strong>lo que sobra</strong>, los <strong>grupos completos</strong> o que haya <strong>lugar para todos</strong>? La respuesta le dice si dar el residuo, descartarlo o redondear hacia arriba.</p>")
R("<h3>Practice 2 — What the remainder means</h3>", "<h3>Práctica 2 — Qué significa el residuo</h3>")
R("<h3>Practice 3 — What the remainder means</h3>", "<h3>Práctica 3 — Qué significa el residuo</h3>")
R('<em>"A school is taking 50 students on a trip in buses with 12 seats. How many buses do they need?"</em> (50 ÷ 12 = 4, remainder 2)', '<em>«Una escuela lleva a 50 estudiantes de excursión en autobuses de 12 asientos. ¿Cuántos autobuses necesita?»</em> (50 ÷ 12 = 4, residuo 2)')
R('type="button">4 buses</button>', 'type="button">4 autobuses</button>')
R('type="button">5 buses</button>', 'type="button">5 autobuses</button>')
R('type="button">2 buses</button>', 'type="button">2 autobuses</button>')
R('type="button">4 buses, and 2 students are left over</button>', 'type="button">4 autobuses, y sobran 2 estudiantes</button>')
R('<em>"I have $74, and I want to buy T-shirts that cost $9 each. How many whole T-shirts can I buy?"</em> (74 ÷ 9 = 8, remainder 2)', '<em>«Tengo $74 y quiero comprar camisetas de $9 cada una. ¿Cuántas camisetas completas puedo comprar?»</em> (74 ÷ 9 = 8, residuo 2)')
R('type="button">9 T-shirts</button>', 'type="button">9 camisetas</button>')
R('type="button">8 T-shirts</button>', 'type="button">8 camisetas</button>')
R('type="button">8 T-shirts and $2 toward another one</button>', 'type="button">8 camisetas y $2 para otra</button>')
R('type="button">2 T-shirts</button>', 'type="button">2 camisetas</button>')
R('href="practice-2-2.html#what-to-do"', 'href="practica-2-2.html#que-hacer"')
R('what to do with the remainder (se abre', 'qué hacer con el residuo (se abre')
R('<span class="ei-titulo">Practique más: what to do with the remainder</span><span class="ei-sub">Decide if you give the remainder, drop it, or round up.</span>', '<span class="ei-titulo">Practique más: qué hacer con el residuo</span><span class="ei-sub">Decida si da el residuo, lo descarta o redondea hacia arriba.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-2-2.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-2-2.html">página de práctica de esta lección</a> ')
R('<li><strong>With paper and pencil.</strong> Do eight long divisions and say the four steps out loud: "Divide… Multiply… Subtract… Bring down." Check each one with multiplication: (quotient × divisor) + remainder.</li>',
  '<li><strong>Con papel y lápiz.</strong> Haga ocho divisiones largas y diga en voz alta los cuatro pasos: «Dividir… Multiplicar… Restar… Bajar». Compruebe cada una con la multiplicación: (cociente × divisor) + residuo.</li>')
R('<li><strong>In your daily life.</strong> Think about something you share or split: hours in a week, money across days, food among people. Write the division, solve it, and decide what the remainder means in that case.</li>',
  '<li><strong>En su vida diaria.</strong> Piense en algo que usted comparte o reparte: horas en una semana, dinero entre varios días, comida entre personas. Escriba la división, resuélvala y decida qué significa el residuo en ese caso.</li>')
# Quiz
R("<p>Answer the <strong>8 questions</strong> without a calculator and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> sin calculadora y pulse <strong>Revisar mis respuestas</strong>.")
R("In <strong>96 ÷ 8</strong>, which number is the <strong>divisor</strong>?", "En <strong>96 ÷ 8</strong>, ¿qué número es el <strong>divisor</strong>?")
R("Divide: <strong>852 ÷ 4</strong>", "Divida: <strong>852 ÷ 4</strong>")
R("Divide: <strong>67 ÷ 5</strong>", "Divida: <strong>67 ÷ 5</strong>")
for a, b in [("13, remainder 2", "13, residuo 2"), ("12, remainder 7", "12, residuo 7"), ("13, remainder 0", "13, residuo 0"), ("14, remainder 3", "14, residuo 3")]:
    R('type="button">' + a + "</button>", 'type="button">' + b + "</button>")
R("How do you check that <strong>67 ÷ 5 = 13, remainder 2</strong> is right?", "¿Cómo se comprueba que <strong>67 ÷ 5 = 13, residuo 2</strong> está bien?")
R('type="button">13 + 5 + 2 should equal 67</button>', 'type="button">13 + 5 + 2 debe dar 67</button>')
R('type="button">67 × 5 should equal 13</button>', 'type="button">67 × 5 debe dar 13</button>')
R('type="button">13 − 5 − 2 should equal 67</button>', 'type="button">13 − 5 − 2 debe dar 67</button>')
R('type="button">(13 × 5) + 2 should equal 67</button>', 'type="button">(13 × 5) + 2 debe dar 67</button>')
R("You divide by <strong>6</strong> and get a remainder of <strong>9</strong>. What does that mean?", "Divide entre <strong>6</strong> y le da un residuo de <strong>9</strong>. ¿Qué significa eso?")
R('type="button">The quotient is too small. The remainder cannot be bigger than the divisor.</button>', 'type="button">El cociente es demasiado pequeño. El residuo no puede ser mayor que el divisor.</button>')
R('type="button">It is fine. The remainder can be any number.</button>', 'type="button">Está bien. El residuo puede ser cualquier número.</button>')
R('type="button">Add 6 to the remainder.</button>', 'type="button">Hay que sumarle 6 al residuo.</button>')
R('type="button">The division cannot be done.</button>', 'type="button">La división no se puede hacer.</button>')
R('<em>"45 children are going to a park in cars that hold 4 children each. How many cars do they need so everyone can go?"</em> (45 ÷ 4 = 11, remainder 1)', '<em>«45 niños van a un parque en carros donde caben 4 niños en cada uno. ¿Cuántos carros necesitan para que vayan todos?»</em> (45 ÷ 4 = 11, residuo 1)')
R('type="button">11 cars</button>', 'type="button">11 carros</button>')
R('type="button">12 cars</button>', 'type="button">12 carros</button>')
R('type="button">1 car</button>', 'type="button">1 carro</button>')
R('type="button">11 cars, and 1 child stays behind</button>', 'type="button">11 carros, y 1 niño se queda</button>')
R('<em>"A bakery makes 100 rolls and packs them in bags of 6. How many rolls are left over, not enough to fill a bag?"</em> (100 ÷ 6 = 16, remainder 4)', '<em>«Una panadería hace 100 panes y los empaca en bolsas de 6. ¿Cuántos panes sobran, sin llegar a llenar una bolsa?»</em> (100 ÷ 6 = 16, residuo 4)')
for a, b in [("4 rolls", "4 panes"), ("16 rolls", "16 panes"), ("17 rolls", "17 panes"), ("6 rolls", "6 panes")]:
    R('type="button">' + a + "</button>", 'type="button">' + b + "</button>")
R('<em>"A company splits $980 equally among 7 workers. How much does each worker get?"</em>', '<em>«Una compañía reparte $980 en partes iguales entre 7 trabajadores. ¿Cuánto recibe cada trabajador?»</em>')
# Lista
R('aria-label="Self-check checklist for division (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de división (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: division skills ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas de división ')
R('<tr><th scope="row">Long division</th><td>I divide, multiply, subtract, and bring down with no mistakes, with one-digit and two-digit divisors.</td><td>I do it correctly with one-digit divisors.</td><td>I skip a step or bring down the wrong digit.</td></tr>',
  '<tr><th scope="row">División larga</th><td>Divido, multiplico, resto y bajo sin errores, con divisores de uno y de dos dígitos.</td><td>Lo hago bien con divisores de un dígito.</td><td>Me salto un paso o bajo el dígito equivocado.</td></tr>')
R('<tr><th scope="row">The remainder</th><td>I find the remainder and check that it is smaller than the divisor.</td><td>I find the remainder correctly.</td><td>I get a remainder bigger than the divisor and do not notice.</td></tr>',
  '<tr><th scope="row">El residuo</th><td>Hallo el residuo y compruebo que sea menor que el divisor.</td><td>Hallo bien el residuo.</td><td>Me da un residuo mayor que el divisor y no me doy cuenta.</td></tr>')
R('<tr><th scope="row">What the remainder means</th><td>I always decide whether to give, drop, or round up, and I can explain why.</td><td>I decide correctly most of the time.</td><td>I calculate correctly but do not know what to do with the remainder.</td></tr>',
  '<tr><th scope="row">Qué significa el residuo</th><td>Siempre decido si darlo, descartarlo o redondear hacia arriba, y sé explicar por qué.</td><td>Decido bien la mayoría de las veces.</td><td>Calculo bien, pero no sé qué hacer con el residuo.</td></tr>')
R('<tr><th scope="row">Check with multiplication</th><td>I check with (quotient × divisor) + remainder on my own.</td><td>I check when someone asks me to.</td><td>I forget to add the remainder when I check, or I do not check.</td></tr>',
  '<tr><th scope="row">Comprobar con la multiplicación</th><td>Compruebo por mi cuenta con (cociente × divisor) + residuo.</td><td>Compruebo cuando alguien me lo pide.</td><td>Olvido sumar el residuo al comprobar, o no compruebo.</td></tr>')
# Cierre
R("<p>Now you can use all four operations with whole numbers: add, subtract, multiply, and divide. You also know what a remainder means in a real problem. In <strong>Lesson 2.3 · Multiplication and division in word problems</strong>, you will put it all together: you will decide whether a word problem needs multiplication or division, and you will use the properties to solve it quickly. That lesson closes Topic 2.</p>",
  "<p>Ya sabe usar las cuatro operaciones con números enteros: sumar, restar, multiplicar y dividir. También sabe qué significa el residuo en un problema real. En la <strong>Lección 2.3 · Multiplicación y división en problemas verbales</strong> lo juntará todo: decidirá si un problema verbal necesita una multiplicación o una división, y usará las propiedades para resolverlo rápido. Esa lección cierra el Tema 2.</p>")
R('Next: <a href="lesson-2-3.html">Lesson 2.3 · Multiplication and division in word problems</a>', 'Siguiente: <a href="leccion-2-3.html">Lección 2.3 · Multiplicación y división en problemas verbales</a>')
R("""<dt>dividend</dt><dd>The total you divide. In 24 ÷ 6 = 4, the dividend is 24.</dd>
<dt>divisor</dt><dd>The number you divide by. In 24 ÷ 6 = 4, the divisor is 6.</dd>
<dt>quotient</dt><dd>The answer to a division. In 24 ÷ 6 = 4, the quotient is 4.</dd>
<dt>remainder</dt><dd>What is left over when a division does not come out even. It is always smaller than the divisor. 50 ÷ 7 = 7, remainder 1 (7 R1).</dd>
<dt>long division</dt><dd>A way to divide big numbers step by step: divide, multiply, subtract, bring down, and repeat.</dd>
<dt>round up</dt><dd>Here: use the next whole number for the quotient, so that everyone or everything fits.</dd>""",
"""<dt>dividendo</dt><dd>El total que se divide. En 24 ÷ 6 = 4, el dividendo es 24.</dd>
<dt>divisor</dt><dd>El número entre el que se divide. En 24 ÷ 6 = 4, el divisor es 6.</dd>
<dt>cociente</dt><dd>El resultado de una división. En 24 ÷ 6 = 4, el cociente es 4.</dd>
<dt>residuo</dt><dd>Lo que sobra cuando una división no da exacto. Siempre es menor que el divisor. 50 ÷ 7 = 7, residuo 1 (7 R1).</dd>
<dt>división larga</dt><dd>Una forma de dividir números grandes paso a paso: dividir, multiplicar, restar, bajar y repetir.</dd>
<dt>redondear hacia arriba</dt><dd>Aquí: usar el número entero siguiente para el cociente, de modo que quepan todos o todo.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 2 · Lesson 2.2</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 2 · Lección 2.2</p>")
t.js('''{
 next: "Lección 2.3",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "b",
   hints: { a: "Un residuo de 5 es mayor que el divisor, 4. El cociente es demasiado pequeño.", c: "21 × 4 = 84, no 85. Sobra algo.", d: "22 × 4 = 88, que es más que 85." },
   right: "8 ÷ 4 = 2. Baje el 5: 5 ÷ 4 = 1, residuo 1. Comprobación: (21 × 4) + 1 = 85 ✓",
   solution: "8 ÷ 4 = 2. Baje el 5: 5 ÷ 4 = 1, residuo 1. La respuesta es 21, residuo 1. Comprobación: (21 × 4) + 1 = 84 + 1 = 85 ✓" },
  p2: { ok: "b",
   hints: { a: "Con 4 autobuses, 2 estudiantes se quedan sin asiento. Tienen que ir todos.", c: "2 es el residuo: los estudiantes sin asiento.", d: "¿Pueden quedarse 2 estudiantes en casa? Todos tienen que ir a la excursión." },
   right: "Tienen que ir todos, así que se redondea hacia arriba: 4 autobuses llevan 48 estudiantes, y los otros 2 necesitan un autobús más. 5 autobuses.",
   solution: "Todos tienen que ir a la excursión. 4 autobuses llevan 48 estudiantes, y 2 estudiantes se quedarían sin asiento, así que necesitan un autobús más: 5 autobuses." },
  p3: { ok: "b",
   hints: { a: "9 camisetas cuestan 9 × $9 = $81. Eso es más que $74.", c: "$2 no alcanzan para otra camiseta. Solo cuentan las camisetas completas.", d: "2 es el dinero que sobra, no la cantidad de camisetas." },
   right: "Solo cuentan las camisetas completas, así que se descarta el residuo: 8 camisetas. Los $2 que sobran no alcanzan para otra.",
   solution: "8 camisetas cuestan 8 × $9 = $72, y sobran $2. Eso no alcanza para otra camiseta, así que se descarta el residuo: 8 camisetas." }
 },
 quiz: {
  A: { ok: "c", hints: { a: "96 es el total que se divide: el dividendo.", b: "12 es el resultado: el cociente.", d: "Aquí no hay residuo. ¿Entre qué número se divide?" },
   solution: "El divisor es el número entre el que se divide: 8. (96 es el dividendo y 12 es el cociente.)" },
  B: { ok: "b", hints: { a: "Después de 8 ÷ 4 = 2, baje el 5. 4 cabe en 5 una vez, así que el dígito de las decenas es 1, no 0.", c: "Revise el orden de los dígitos del cociente. Trabaje de izquierda a derecha.", d: "Revise el último paso: baje el 2 para formar 12. 12 ÷ 4 = 3." },
   solution: "8 ÷ 4 = 2. Baje el 5: 5 ÷ 4 = 1, residuo 1. Baje el 2: 12 ÷ 4 = 3. El cociente es 213. Comprobación: 213 × 4 = 852 ✓" },
  C: { ok: "a", hints: { b: "Un residuo de 7 es mayor que el divisor, 5. El cociente es demasiado pequeño.", c: "13 × 5 = 65, no 67. Sobra algo.", d: "14 × 5 = 70, que es más que 67." },
   solution: "6 ÷ 5 = 1, residuo 1. Baje el 7: 17 ÷ 5 = 3, residuo 2. La respuesta es 13, residuo 2. Comprobación: (13 × 5) + 2 = 67 ✓" },
  D: { ok: "d", hints: { a: "La división se deshace con la multiplicación, no con la suma.", b: "Empiece con el cociente, no con el dividendo.", c: "La división se deshace con la multiplicación." },
   solution: "La multiplicación deshace la división: (cociente × divisor) + residuo = dividendo. (13 × 5) + 2 = 65 + 2 = 67 ✓" },
  E: { ok: "a", hints: { b: "Si sobran 9, ¿podría caber el 6 una vez más?", c: "Si sobran 9, ¿podría caber el 6 una vez más?", d: "La división sí se puede hacer. Mire otra vez el residuo." },
   solution: "Si sobran 9, el 6 cabe por lo menos una vez más. El residuo siempre tiene que ser menor que el divisor, así que el cociente es demasiado pequeño. Auméntelo." },
  F: { ok: "b", hints: { a: "Con 11 carros, 1 niño se queda sin asiento. Tienen que ir todos.", c: "1 es el residuo: el niño sin asiento.", d: "El problema dice que tienen que ir todos. Nadie puede quedarse." },
   solution: "Tienen que ir todos, así que se redondea el cociente hacia arriba. 11 carros llevan 44 niños, y 1 niño todavía necesita asiento: 12 carros." },
  G: { ok: "a", hints: { b: "16 es la cantidad de bolsas llenas. La pregunta es por los panes que sobran.", c: "La pregunta es por los panes que sobran, no por la cantidad de bolsas.", d: "6 es el tamaño de una bolsa." },
   solution: "La pregunta pide lo que sobra, así que la respuesta es el residuo: 4 panes." },
  H: { ok: "c", hints: { a: "Compruebe: 130 × 7 = 910, no 980.", b: "Después de 98 ÷ 7 = 14, todavía queda un 0 por bajar. 0 ÷ 7 = 0, así que escriba 0 en el cociente.", d: "Repartir quiere decir dividir, no sumar." },
   solution: "9 ÷ 7 = 1, residuo 2. Baje el 8: 28 ÷ 7 = 4. Baje el 0: 0 ÷ 7 = 0. Cada trabajador recibe $140. Comprobación: 140 × 7 = 980 ✓" }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-2-2.html")
