"""Crea es/matematicas/nivel-1/practica-4-3.html a partir de math/level-1/practice-4-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-4-3.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 4.3 · Multiplicación y división de fracciones — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 4.3 · Multiplying and dividing fractions · LearnGED</title>", "<title>Práctica · Lección 4.3 · Multiplicación y división de fracciones · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 4 · Fractions</div>', '<div class="ruta">Nivel 1 · Tema 4 · Fracciones</div>')
R("<h1>Lesson 4.3 · Multiplying and dividing fractions</h1>", "<h1>Lección 4.3 · Multiplicación y división de fracciones</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#multiply">Multiply: straight across</a></li>', '<li><a href="#multiplicar">Multiplicar: en línea recta</a></li>')
R('<li><a href="#reciprocal">The reciprocal</a></li>', '<li><a href="#reciproco">El recíproco</a></li>')
R('<li><a href="#divide">Divide: keep, change, flip</a></li>', '<li><a href="#dividir">Dividir: dejar, cambiar, voltear</a></li>')
R('<li><a href="#real-life">Fractions in real life</a></li>', '<li><a href="#vida-real">Las fracciones en la vida real</a></li>')
t.todas('">First fraction</label>', '">Primera fracción</label>'); t.todas('">Second fraction</label>', '">Segunda fracción</label>')
# 1
R('id="multiply" open>', 'id="multiplicar" open>'); R("<h2>Multiply: straight across</h2>", "<h2>Multiplicar: en línea recta</h2>")
R("""<p>Good news: to multiply, you <strong>do not need a common denominator</strong>. Numerator times numerator on top, denominator
      times denominator on the bottom, and simplify at the end. The word <strong>"of"</strong> almost always means multiply: half of half a
      pizza is 1/2 × 1/2 = 1/4.</p>""",
  """<p>Buena noticia: para multiplicar <strong>no hace falta un denominador común</strong>. Numerador por numerador arriba, denominador
      por denominador abajo, y simplifique al final. La palabra <strong>«de»</strong> casi siempre quiere decir multiplicar: la mitad de media
      pizza es 1/2 × 1/2 = 1/4.</p>""")
R("<h3>The area model</h3>", "<h3>El modelo de área</h3>")
R("<h3>Practice: multiply</h3>", "<h3>Practique: multiplique</h3>")
R('<label for="p1-r">Product</label>', '<label for="p1-r">Producto</label>')
R('<p class="nota">Type the fraction with a slash, in simplest form, for example 2/5.</p>', '<p class="nota">Escriba la fracción con una raya inclinada, en su forma más simple, por ejemplo 2/5.</p>')
R('<p>Write the first fraction with <span class="tecla">n/d</span> (numerator, <span class="tecla">▼</span>, denominator, <span class="tecla">►</span>), press <span class="tecla">×</span>, write the second fraction the same way, and press <span class="tecla">enter</span>. The calculator shows the product in simplest form.</p>',
  '<p>Escriba la primera fracción con <span class="tecla">n/d</span> (numerador, <span class="tecla">▼</span>, denominador, <span class="tecla">►</span>), pulse <span class="tecla">×</span>, escriba la segunda fracción de la misma manera y pulse <span class="tecla">enter</span>. La calculadora muestra el producto en su forma más simple.</p>')
# 2
R('id="reciprocal">', 'id="reciproco">'); R("<h2>The reciprocal</h2>", "<h2>El recíproco</h2>")
R("""<p>The <strong>reciprocal</strong> of a fraction is the same fraction <strong>flipped upside down</strong>: the numerator goes to the
      bottom and the denominator to the top. The reciprocal of 3/4 is 4/3; the reciprocal of 1/8 is 8/1, which is 8; and the reciprocal of a
      whole number like 4 is 1/4 (every whole number is itself over 1). A number times its reciprocal is always 1.</p>""",
  """<p>El <strong>recíproco</strong> de una fracción es la misma fracción <strong>volteada</strong>: el numerador pasa
      abajo y el denominador arriba. El recíproco de 3/4 es 4/3; el recíproco de 1/8 es 8/1, que es 8; y el recíproco de un
      número entero como 4 es 1/4 (todo número entero es él mismo sobre 1). Un número por su recíproco siempre da 1.</p>""")
R("<h3>Practice: what is the reciprocal?</h3>", "<h3>Practique: ¿cuál es el recíproco?</h3>")
# 3
R('id="divide">', 'id="dividir">'); R("<h2>Divide: keep, change, flip</h2>", "<h2>Dividir: dejar, cambiar, voltear</h2>")
R("""<p>To divide: <strong>keep</strong> the first fraction as it is, <strong>change</strong> ÷ to ×, and <strong>flip</strong> the second
      fraction (use its reciprocal). Then multiply straight across.</p>""",
  """<p>Para dividir: <strong>deje</strong> la primera fracción como está, <strong>cambie</strong> ÷ por × y <strong>voltee</strong> la segunda
      fracción (use su recíproco). Después multiplique en línea recta.</p>""")
R('<div class="caja-atencion"><strong>Flip only the second fraction.</strong> If you flip the first one, or both, the answer comes out wrong.</div>', '<div class="caja-atencion"><strong>Voltee solo la segunda fracción.</strong> Si voltea la primera, o las dos, el resultado sale mal.</div>')
R("<h3>Practice: divide</h3>", "<h3>Practique: divida</h3>")
R('<label for="p3-r">Quotient</label>', '<label for="p3-r">Cociente</label>')
R('<p class="nota">Type the fraction with a slash, in simplest form. If it is more than 1, you can type a mixed number with a space, like 1&nbsp;1/2.</p>', '<p class="nota">Escriba la fracción con una raya inclinada, en su forma más simple. Si es más que 1, puede escribir un número mixto con un espacio, como 1&nbsp;1/2.</p>')
# 4
R('id="real-life">', 'id="vida-real">'); R("<h2>Fractions in real life</h2>", "<h2>Las fracciones en la vida real</h2>")
R('<p>"Half of," "a third of" ask you to <strong>multiply</strong>. "How many pieces of …?", "how many servings of …?" ask you to <strong>divide</strong>.</p>', '<p>«La mitad de», «un tercio de» piden <strong>multiplicar</strong>. «¿Cuántos pedazos de …?», «¿cuántas porciones de …?» piden <strong>dividir</strong>.</p>')
R('<div class="caja-tip"><strong>Example:</strong> how many 1/4-pound servings can you get from 3 pounds of meat? 3 ÷ 1/4 = 3 × 4 = 12 servings.</div>', '<div class="caja-tip"><strong>Ejemplo:</strong> ¿cuántas porciones de 1/4 de libra salen de 3 libras de carne? 3 ÷ 1/4 = 3 × 4 = 12 porciones.</div>')
R("<h3>Practice: word problems with fractions</h3>", "<h3>Practique: problemas verbales con fracciones</h3>")
R('<label for="p4-r">Answer</label>', '<label for="p4-r">Respuesta</label>')
R('<p class="nota">Type a fraction (3/8), a mixed number with a space (1&nbsp;1/2), or a whole number. Do not type the units.</p>', '<p class="nota">Escriba una fracción (3/8), un número mixto con un espacio (1&nbsp;1/2) o un número entero. No escriba las unidades.</p>')
R("<p><strong>Level 1 · Topic 4 · Fractions · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 4 · Fracciones · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Helpers ============ */", "/* ============ Utilidades ============ */")
R("/* value v = {n, d} in simplest form → HTML (whole, fraction, or mixed number) */", "/* valor v = {n, d} en su forma más simple → HTML (entero, fracción o número mixto) */")
R("""<span class="sr-only">' + e + ' and ' + r + '/' + v.d + '</span>'""", """<span class="sr-only">' + e + ' y ' + r + '/' + v.d + '</span>'""")
R('/* Reads "3/4", "7/4", "1 3/4", or "2". Returns { v: value, f: fraction part as typed, mixta, w } or null. */', '/* Lee "3/4", "7/4", "1 3/4" o "2". Devuelve { v: valor, f: la fracción tal como se escribió, mixta, w } o null. */')
R("/* Evaluator. obj = right value; pistas = [{v, msg}] for common mistakes; simple = the answer must be in simplest form */", "/* Evaluador. obj = valor correcto; pistas = [{v, msg}] para errores comunes; simple = la respuesta debe estar en su forma más simple */")
R('msg: "A fraction can never have 0 on the bottom. The parts keep their size: keep the denominator." };', 'msg: "Una fracción nunca puede tener 0 abajo. Las partes conservan su tamaño: deje el denominador." };')
R('msg: "Type a fraction with a slash (3/4), a mixed number with a space (1&nbsp;3/4), or a whole number." };', 'msg: "Escriba una fracción con una raya inclinada (3/4), un número mixto con un espacio (1&nbsp;3/4) o un número entero." };')
R('msg: "In a mixed number, the fraction part must be less than 1." };', 'msg: "En un número mixto, la parte de fracción tiene que ser menor que 1." };')
R('msg: "The value is right, but you can still simplify: " + r.f.p + " and " + r.f.q + " can both be divided by "', 'msg: "El valor está bien, pero todavía puede simplificar: " + r.f.p + " y " + r.f.q + " se pueden dividir los dos entre "')
R('msg: "That is not the right amount. Check each step." };', 'msg: "Esa no es la cantidad correcta. Revise cada paso." };')
R("/* Fraction bar: d equal parts, n of them filled (more than one bar if n > d) */", "/* Barra de fracción: d partes iguales, n sombreadas (más de una barra si n > d) */")
R("/* ============ MODULE 1 · multiply ============ */", "/* ============ MÓDULO 1 · multiplicar ============ */")
R("""aria-label="Area model: a square cut into ' + b + ' columns and ' + d + ' rows, ' + (b * d) + ' small parts in all. ' + a + ' columns are purple and ' + c + ' rows are blue. They overlap in ' + (a * c) + ' small parts, shown in dark purple.">'""",
  """aria-label="Modelo de área: un cuadrado cortado en ' + b + ' columnas y ' + d + ' filas, ' + (b * d) + ' partes pequeñas en total. ' + a + ' columnas son moradas y ' + c + ' filas son azules. Se cruzan en ' + (a * c) + ' partes pequeñas, en morado oscuro.">'""")
R('s.innerHTML = "Type two fractions with a slash, for example 2/3 and 4/5 (denominators up to 12).";', 's.innerHTML = "Escriba dos fracciones con una raya inclinada, por ejemplo 2/3 y 4/5 (denominadores hasta 12).";')
R("""s.innerHTML = '<div class="linea">Top: ' + A.p + ' × ' + B.p + ' = ' + n + '. Bottom: '""", """s.innerHTML = '<div class="linea">Arriba: ' + A.p + ' × ' + B.p + ' = ' + n + '. Abajo: '""")
R("""(dib ? '<div class="linea">In the picture: ' + d + ' small parts in all, and ' + n + ' in the dark purple area, where the two fractions overlap.</div>' : '<div class="linea">The picture works for fractions less than or equal to 1.</div>')""",
  """(dib ? '<div class="linea">En el dibujo: ' + d + ' partes pequeñas en total, y ' + n + ' en el área morado oscuro, donde se cruzan las dos fracciones.</div>' : '<div class="linea">El dibujo sirve para fracciones menores que 1 o iguales a 1.</div>')""")
R("/* a proper fraction n/d already in simplest form */", "/* una fracción propia n/d ya en su forma más simple */")
R('return { enun: de ? "What is " + fr(a, b) + " of " + fr(c, d) + "?" : "Calculate " + fr(a, b) + " × " + fr(c, d) + ".",', 'return { enun: de ? "¿Cuánto es " + fr(a, b) + " de " + fr(c, d) + "?" : "Calcule " + fr(a, b) + " × " + fr(c, d) + ".",')
R('solucion: "Top: " + a + " × " + c + " = " + (a * c) + ". Bottom: "', 'solucion: "Arriba: " + a + " × " + c + " = " + (a * c) + ". Abajo: "')
R('(R.d !== b * d ? " = " + txtV(R) : "") + ". Answer: <strong>" + txtV(R) + "</strong>.",', '(R.d !== b * d ? " = " + txtV(R) : "") + ". Respuesta: <strong>" + txtV(R) + "</strong>.",')
R('msg: "That is a division. To multiply, you do not flip anything." }, { v: suma, msg: "That is the sum. Multiply top by top and bottom by bottom." },', 'msg: "Eso es una división. Para multiplicar no se voltea nada." }, { v: suma, msg: "Esa es la suma. Multiplique arriba por arriba y abajo por abajo." },')
R('msg: "Multiply the denominators too: "', 'msg: "Multiplique también los denominadores: "')
R("/* ============ MODULE 2 · the reciprocal ============ */", "/* ============ MÓDULO 2 · el recíproco ============ */")
R('return { enun: "What is the reciprocal of " + a + "?",', 'return { enun: "¿Cuál es el recíproco de " + a + "?",')
R('pistas: { e: "That is the same number. Write it as a fraction first: " + a + " = " + a + "/1, and flip it.", m: "Write " + a + " as a fraction over 1, not over 2: " + a + "/1. Then flip it.", z: "No number times 0 equals 1. Write " + a + " as " + a + "/1 and flip it." },',
  'pistas: { e: "Ese es el mismo número. Escríbalo primero como fracción: " + a + " = " + a + "/1, y voltéelo.", m: "Escriba " + a + " como fracción sobre 1, no sobre 2: " + a + "/1. Después voltéelo.", z: "Ningún número por 0 da 1. Escriba " + a + " como " + a + "/1 y voltéelo." },')
R('bien: a + " = " + a + "/1. Flipped: 1/" + a + ". Check: " + a + " × 1/" + a + " = 1.", mal: "Every whole number is itself over 1: " + a + "/1. Flipped, it is 1/" + a + "." }; }',
  'bien: a + " = " + a + "/1. Volteado: 1/" + a + ". Comprobación: " + a + " × 1/" + a + " = 1.", mal: "Todo número entero es él mismo sobre 1: " + a + "/1. Volteado, es 1/" + a + "." }; }')
R('return { enun: "What is the reciprocal of " + fr(1, b) + "?",', 'return { enun: "¿Cuál es el recíproco de " + fr(1, b) + "?",')
R('pistas: { x: "That is the same fraction. Flip it upside down.", y: "Flip it: the 1 goes to the bottom and the " + b + " to the top: " + b + "/1.", u: "Flip the fraction: " + b + "/1. What whole number is that?" },',
  'pistas: { x: "Esa es la misma fracción. Voltéela.", y: "Voltéela: el 1 pasa abajo y el " + b + " arriba: " + b + "/1.", u: "Voltee la fracción: " + b + "/1. ¿Qué número entero es ese?" },')
R('bien: "Flipped, it is " + b + "/1, which is " + b + ".", mal: "Flipped, it is " + b + "/1, which is " + b + "." }; }', 'bien: "Volteada, es " + b + "/1, que es " + b + ".", mal: "Volteada, es " + b + "/1, que es " + b + "." }; }')
R('var pistas = {}; pistas[a + "/" + b] = "That is the same fraction. Flip it upside down."; pistas[b + "/" + b] = b + "/" + b + " is 1 whole. Flip the fraction: the " + a + " goes to the bottom."; pistas["1/" + b] = "Flip the whole fraction: the " + a + " goes to the bottom and the " + b + " to the top.";',
  'var pistas = {}; pistas[a + "/" + b] = "Esa es la misma fracción. Voltéela."; pistas[b + "/" + b] = b + "/" + b + " es 1 entero. Voltee la fracción: el " + a + " pasa abajo."; pistas["1/" + b] = "Voltee toda la fracción: el " + a + " pasa abajo y el " + b + " arriba.";')
R('return { enun: "What is the reciprocal of " + fr(a, b) + "?",', 'return { enun: "¿Cuál es el recíproco de " + fr(a, b) + "?",')
R('bien: "Flipped: " + b + "/" + a + ". Check: " + a + "/" + b + " × " + b + "/" + a + " = 1.", mal: "Flip it: the " + a + " goes to the bottom and the " + b + " to the top: " + b + "/" + a + "." };',
  'bien: "Volteada: " + b + "/" + a + ". Comprobación: " + a + "/" + b + " × " + b + "/" + a + " = 1.", mal: "Voltéela: el " + a + " pasa abajo y el " + b + " arriba: " + b + "/" + a + "." };')
R("/* ============ MODULE 3 · divide ============ */", "/* ============ MÓDULO 3 · dividir ============ */")
R('s.innerHTML = "Type two fractions with a slash, for example 3/4 and 1/2 (not 0, denominators up to 12)."; return; }', 's.innerHTML = "Escriba dos fracciones con una raya inclinada, por ejemplo 3/4 y 1/2 (no 0, denominadores hasta 12)."; return; }')
R("""s.innerHTML = '<div class="linea">1. Keep the first fraction: ' + fr(A.p, A.q) + '.</div><div class="linea">2. Change ÷ to ×.</div><div class="linea">3. Flip the second fraction: '""", """s.innerHTML = '<div class="linea">1. Deje la primera fracción: ' + fr(A.p, A.q) + '.</div><div class="linea">2. Cambie ÷ por ×.</div><div class="linea">3. Voltee la segunda fracción: '""")
R("""'<div class="linea">4. Multiply straight across: '""", """'<div class="linea">4. Multiplique en línea recta: '""")
R('return { enun: "Calculate " + fr(a, b) + " ÷ " + fr(c, d) + ".",', 'return { enun: "Calcule " + fr(a, b) + " ÷ " + fr(c, d) + ".",')
R('solucion: "Keep, change, flip: "', 'solucion: "Dejar, cambiar, voltear: "')
R('(R.n > R.d && R.d > 1 ? " = " + txtV(R) : "") + ". Answer: <strong>" + txtV(R) + "</strong>.",', '(R.n > R.d && R.d > 1 ? " = " + txtV(R) : "") + ". Respuesta: <strong>" + txtV(R) + "</strong>.",')
R('msg: "You multiplied without flipping. To divide, flip the second fraction." }, { v: red(b * c, a * d), msg: "You flipped the first fraction (or both). Flip only the second one." }], true) };',
  'msg: "Multiplicó sin voltear. Para dividir, voltee la segunda fracción." }, { v: red(b * c, a * d), msg: "Volteó la primera fracción (o las dos). Voltee solo la segunda." }], true) };')
R("/* ============ MODULE 4 · real life ============ */", "/* ============ MÓDULO 4 · vida real ============ */")
R('enun = "A recipe calls for " + frV(red(q[0], q[1])) + " cup" + (q[0] > q[1] ? "s" : "") + " of sugar. You are making half of the recipe. How many cups of sugar do you need?";',
  'enun = "Una receta pide " + frV(red(q[0], q[1])) + (q[0] > q[1] ? " tazas" : " de taza") + " de azúcar. Usted va a hacer la mitad de la receta. ¿Cuántas tazas de azúcar necesita?";')
R('sol = "\\"Half of\\" means multiply: 1/2 × "', 'sol = "«La mitad de» quiere decir multiplicar: 1/2 × "')
R('". Answer: <strong>" + txtV(R) + "</strong> cup.";', '". Respuesta: <strong>" + txtV(R) + "</strong> de taza.";')
R('msg: "That is double the sugar. Half the recipe needs less: multiply by 1/2." }); }', 'msg: "Eso es el doble del azúcar. La mitad de la receta necesita menos: multiplique por 1/2." }); }')
R('enun = "How many 1/" + f + "-pound servings can you get from " + n + " pounds of meat?";', 'enun = "¿Cuántas porciones de 1/" + f + " de libra salen de " + n + " libras de carne?";')
R('sol = "\\"How many servings\\" means divide: "', 'sol = "«Cuántas porciones» quiere decir dividir: "')
R('". Answer: <strong>" + (n * f) + "</strong> servings.";', '". Respuesta: <strong>" + (n * f) + "</strong> porciones.";')
R('msg: "You need to know how many servings fit: that is a division, "', 'msg: "Necesita saber cuántas porciones caben: eso es una división, "')
R('enun = "In a class of " + tot + " students, " + g[0] + "/" + g[1] + " of them have a job. How many students have a job?";', 'enun = "En una clase de " + tot + " estudiantes, " + g[0] + "/" + g[1] + " de ellos tienen trabajo. ¿Cuántos estudiantes tienen trabajo?";')
R('sol = g[0] + "/" + g[1] + " of " + tot + " means multiply: "', 'sol = g[0] + "/" + g[1] + " de " + tot + " quiere decir multiplicar: "')
R('". Answer: <strong>" + R.n + "</strong> students."; }', '". Respuesta: <strong>" + R.n + "</strong> estudiantes."; }')
R('enun = "A board is " + frV(red(tab[0], tab[1])) + " feet long. How many pieces " + pz[0] + "/" + pz[1] + " foot long can you cut from it?";', 'enun = "Una tabla mide " + frV(red(tab[0], tab[1])) + " pies de largo. ¿Cuántos pedazos de " + pz[0] + "/" + pz[1] + " de pie se pueden cortar de ella?";')
R('sol = "\\"How many pieces\\" means divide: "', 'sol = "«Cuántos pedazos» quiere decir dividir: "')
R('". Answer: <strong>" + R.n + "</strong> pieces."; }', '". Respuesta: <strong>" + R.n + "</strong> pedazos."; }')
R('enun = "You live " + d0[0] + "/" + d0[1] + " mile from the store. You have walked " + m[0] + "/" + m[1] + " of the way. How many miles have you walked?";', 'enun = "Usted vive a " + d0[0] + "/" + d0[1] + " de milla de la tienda. Ha caminado " + m[0] + "/" + m[1] + " del camino. ¿Cuántas millas ha caminado?";')
R('sol = m[0] + "/" + m[1] + " of " + d0[0] + "/" + d0[1] + " means multiply: "', 'sol = m[0] + "/" + m[1] + " de " + d0[0] + "/" + d0[1] + " quiere decir multiplicar: "')
R('". Answer: <strong>" + txtV(R) + "</strong> mile.";', '". Respuesta: <strong>" + txtV(R) + "</strong> de milla.";')
R('msg: "That is a division. \\"" + m[0] + "/" + m[1] + " of the way\\" means multiply." }); }', 'msg: "Eso es una división. «" + m[0] + "/" + m[1] + " del camino» quiere decir multiplicar." }); }')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-4-3.html")
