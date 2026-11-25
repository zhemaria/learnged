"""Crea es/matematicas/nivel-1/practica-4-2.html a partir de math/level-1/practice-4-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-4-2.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 4.2 · Suma y resta de fracciones — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 4.2 · Adding and subtracting fractions · LearnGED</title>", "<title>Práctica · Lección 4.2 · Suma y resta de fracciones · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 4 · Fractions</div>', '<div class="ruta">Nivel 1 · Tema 4 · Fracciones</div>')
R("<h1>Lesson 4.2 · Adding and subtracting fractions</h1>", "<h1>Lección 4.2 · Suma y resta de fracciones</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#same-denominator">The same denominator</a></li>', '<li><a href="#mismo-denominador">El mismo denominador</a></li>')
R('<li><a href="#different-denominators">Different denominators</a></li>', '<li><a href="#denominadores-distintos">Denominadores distintos</a></li>')
R('<li><a href="#simplify-result">Simplify the result</a></li>', '<li><a href="#simplificar-resultado">Simplificar el resultado</a></li>')
t.todas('">Answer</label>', '">Respuesta</label>')
t.todas('<option value="+">+ add</option><option value="-">− subtract</option>', '<option value="+">+ sumar</option><option value="-">− restar</option>')
t.todas('">Operation</label>', '">Operación</label>')
# 1
R('id="same-denominator" open>', 'id="mismo-denominador" open>'); R("<h2>The same denominator</h2>", "<h2>El mismo denominador</h2>")
R("""<p>The denominator tells the <strong>size</strong> of the parts; the numerator tells <strong>how many</strong> there are. If the parts are
      the same size, <strong>add (or subtract) the numerators and keep the denominator</strong>: 2 fourths of a pizza plus 1 fourth are 3 fourths.</p>""",
  """<p>El denominador dice el <strong>tamaño</strong> de las partes; el numerador dice <strong>cuántas</strong> hay. Si las partes son
      del mismo tamaño, <strong>sume (o reste) los numeradores y deje el denominador</strong>: 2 cuartos de pizza más 1 cuarto son 3 cuartos.</p>""")
R("<h3>Join the pieces</h3>", "<h3>Junte los pedazos</h3>")
R('<label for="md-d">Denominator: ', '<label for="md-d">Denominador: ')
R('<label for="md-a">First numerator: ', '<label for="md-a">Primer numerador: ')
R('<label for="md-b">Second numerator: ', '<label for="md-b">Segundo numerador: ')
R("""<strong>The most common mistake:</strong> adding the denominators too. 2/5 + 1/5 is not 3/10: the size of the parts does not change when you join them.
        Besides, 3/10 is less than 2/5, and adding should give you more.""",
  """<strong>El error más común:</strong> sumar también los denominadores. 2/5 + 1/5 no es 3/10: el tamaño de las partes no cambia al juntarlas.
        Además, 3/10 es menos que 2/5, y al sumar debería obtener más.""")
R("<h3>Practice: the same denominator</h3>", "<h3>Practique: el mismo denominador</h3>")
R('<p class="nota">Type the fraction with a slash, for example 3/5.</p>', '<p class="nota">Escriba la fracción con una raya inclinada, por ejemplo 3/5.</p>')
# 2
R('id="different-denominators">', 'id="denominadores-distintos">'); R("<h2>Different denominators</h2>", "<h2>Denominadores distintos</h2>")
R("""<p>If the parts are different sizes, first <strong>make the denominators the same</strong>. Go through the multiples of the larger
      denominator until you find one that the smaller one also goes into. If you do not find one, multiplying the two denominators always
      works. Then change each fraction to an equivalent fraction, and add or subtract the numerators.</p>""",
  """<p>Si las partes son de tamaños distintos, primero <strong>iguale los denominadores</strong>. Recorra los múltiplos del denominador
      mayor hasta encontrar uno en el que también quepa el menor. Si no lo encuentra, multiplicar los dos denominadores siempre
      sirve. Después convierta cada fracción en una equivalente, y sume o reste los numeradores.</p>""")
R('<label for="dd-a">First fraction</label>', '<label for="dd-a">Primera fracción</label>')
R('<label for="dd-b">Second fraction</label>', '<label for="dd-b">Segunda fracción</label>')
R("<h3>Practice: which common denominator?</h3>", "<h3>Practique: ¿qué denominador común?</h3>")
R("<h3>Practice: different denominators</h3>", "<h3>Practique: denominadores distintos</h3>")
R('<p class="nota">Type the fraction with a slash, in simplest form. If it is more than 1, you can type a mixed number with a space, like 1&nbsp;1/4.</p>', '<p class="nota">Escriba la fracción con una raya inclinada, en su forma más simple. Si es más que 1, puede escribir un número mixto con un espacio, como 1&nbsp;1/4.</p>')
R("""<p>Write the first fraction with <span class="tecla">n/d</span> (numerator, <span class="tecla">▼</span>, denominator, <span class="tecla">►</span>),
        press <span class="tecla">+</span> or <span class="tecla">−</span>, write the second fraction the same way, and press <span class="tecla">enter</span>.
        The calculator shows the answer in simplest form. Solve on paper first, then check.</p>""",
  """<p>Escriba la primera fracción con <span class="tecla">n/d</span> (numerador, <span class="tecla">▼</span>, denominador, <span class="tecla">►</span>),
        pulse <span class="tecla">+</span> o <span class="tecla">−</span>, escriba la segunda fracción de la misma manera y pulse <span class="tecla">enter</span>.
        La calculadora muestra el resultado en su forma más simple. Resuelva primero en papel y después compruebe.</p>""")
# 3
R('id="simplify-result">', 'id="simplificar-resultado">'); R("<h2>Simplify the result</h2>", "<h2>Simplificar el resultado</h2>")
R("""<p>Leave the answer in <strong>simplest form</strong>: 3/6 simplifies to 1/2. And if the result is more than 1, like 7/4, you can
      also write it as a <strong>mixed number</strong>: 7 ÷ 4 = 1 with remainder 3, so 7/4 = 1&nbsp;3/4.</p>""",
  """<p>Deje el resultado en su <strong>forma más simple</strong>: 3/6 se simplifica a 1/2. Y si el resultado es más que 1, como 7/4, también
      puede escribirlo como <strong>número mixto</strong>: 7 ÷ 4 = 1, residuo 3, así que 7/4 = 1&nbsp;3/4.</p>""")
R("<h3>Practice: calculate and simplify</h3>", "<h3>Practique: calcule y simplifique</h3>")
R('<p class="nota">Type a fraction in simplest form (3/4), a mixed number with a space (1&nbsp;3/4), or a whole number.</p>', '<p class="nota">Escriba una fracción en su forma más simple (3/4), un número mixto con un espacio (1&nbsp;3/4) o un número entero.</p>')
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
R('msg: "That is not the right amount. Check each step: the same denominator first, then the numerators." };', 'msg: "Esa no es la cantidad correcta. Revise cada paso: primero el mismo denominador y después los numeradores." };')
R("/* Fraction bar: d equal parts, n of them filled (more than one bar if n > d) */", "/* Barra de fracción: d partes iguales, n sombreadas (más de una barra si n > d) */")
R("/* ============ MODULE 1 · the same denominator ============ */", "/* ============ MÓDULO 1 · el mismo denominador ============ */")
R('$("md-salida").innerHTML = "To subtract, the first numerator must be the greater one.";', '$("md-salida").innerHTML = "Para restar, el primer numerador tiene que ser el mayor.";')
R('a + "/" + d + " shaded."', 'a + "/" + d + " sombreado."'); R('b + "/" + d + " shaded."', 'b + "/" + d + " sombreado."')
R('"Result: " + r + "/" + d + " shaded."', '"Resultado: " + r + "/" + d + " sombreado."')
R("""var h = '<div class="linea">The parts are the same size (' + d + ' equal parts in each whole). ' + (o === "+" ? "Add" : "Subtract") + ' only the numerators: '""", """var h = '<div class="linea">Las partes son del mismo tamaño (' + d + ' partes iguales en cada entero). ' + (o === "+" ? "Sume" : "Reste") + ' solo los numeradores: '""")
R("""h += '<div class="linea">The result is more than 1 whole: ' + d + '/' + d + ' fill one bar, and ' + (r - d) + '/' + d + ' are left over.</div>';""", """h += '<div class="linea">El resultado es más que 1 entero: ' + d + '/' + d + ' llenan una barra, y sobran ' + (r - d) + '/' + d + '.</div>';""")
R('msg: "Do not add the denominators. The parts keep their size, so the denominator stays " + d + "." }];', 'msg: "No sume los denominadores. Las partes conservan su tamaño, así que el denominador sigue siendo " + d + "." }];')
R('msg: "That is what you get if you subtract. This problem asks you to add." });', 'msg: "Eso es lo que da si resta. Este problema pide sumar." });')
R('msg: "That is what you get if you add. This problem asks you to subtract." });', 'msg: "Eso es lo que da si suma. Este problema pide restar." });')
R('return { enun: "Calculate " + fr(a, d)', 'return { enun: "Calcule " + fr(a, d)')
R('" = " + r + ", and the denominator stays " + d + ": <strong>" + r + "/" + d + "</strong>" + (R.d !== d ? ", which simplifies to " + txtV(R) : "") + ".",', '" = " + r + ", y el denominador sigue siendo " + d + ": <strong>" + r + "/" + d + "</strong>" + (R.d !== d ? ", que se simplifica a " + txtV(R) : "") + ".",')
R("/* ============ MODULE 2 · different denominators ============ */", "/* ============ MÓDULO 2 · denominadores distintos ============ */")
R('s.innerHTML = "Type two fractions with a slash, for example 1/2 and 1/3 (denominators up to 20).";', 's.innerHTML = "Escriba dos fracciones con una raya inclinada, por ejemplo 1/2 y 1/3 (denominadores hasta 20).";')
R('s.innerHTML = "To subtract, the first fraction must be the greater one.";', 's.innerHTML = "Para restar, la primera fracción tiene que ser la mayor.";')
R("""'<div class="linea">1. The denominators are already the same.</div>'""", """'<div class="linea">1. Los denominadores ya son iguales.</div>'""")
R("""'<div class="linea">1. Multiples of ' + mayor + ': ' + mult.join(", ") + '. ' + (mult.length === 1 ? 'The number ' + menor + ' already goes into ' + M + '.' : 'The first one that ' + menor + ' also goes into is ' + M + '.') + '</div>';""",
  """'<div class="linea">1. Múltiplos de ' + mayor + ': ' + mult.join(", ") + '. ' + (mult.length === 1 ? 'El ' + menor + ' ya cabe exacto en ' + M + '.' : 'El primero en el que también cabe el ' + menor + ' es ' + M + '.') + '</div>';""")
R("""h += '<div class="linea">2. Change each fraction: '""", """h += '<div class="linea">2. Convierta cada fracción: '""")
R("""' (× ' + M / A.q + ') and '""", """' (× ' + M / A.q + ') y '""")
R("""h += '<div class="linea">3. Same denominator now: '""", """h += '<div class="linea">3. Ahora con el mismo denominador: '""")
R('A.p + "/" + A.q + " changed to " + a2 + "/" + M + "."', 'A.p + "/" + A.q + " convertido en " + a2 + "/" + M + "."')
R('B.p + "/" + B.q + " changed to " + b2 + "/" + M + "."', 'B.p + "/" + B.q + " convertido en " + b2 + "/" + M + "."')
R('"Result: " + r + "/" + M + "."', '"Resultado: " + r + "/" + M + "."')
R('pistas["c" + x] = "That is " + p[0] + " + " + p[1] + ". Adding the denominators does not work" + (vale(x) ? ": " + x + " is a common denominator, but not the smallest." : ": " + x + " is not a multiple of both.");',
  'pistas["c" + x] = "Eso es " + p[0] + " + " + p[1] + ". Sumar los denominadores no sirve" + (vale(x) ? ": " + x + " es un denominador común, pero no el más pequeño." : ": " + x + " no es múltiplo de los dos.");')
R('pistas["c" + x] = x + " works too, but it is not the smallest. Look for a smaller multiple of " + Math.max(p[0], p[1]) + ".";', 'pistas["c" + x] = x + " también sirve, pero no es el más pequeño. Busque un múltiplo más pequeño de " + Math.max(p[0], p[1]) + ".";')
R('pistas["c" + x] = x + " is not a multiple of both " + p[0] + " and " + p[1] + ".";', 'pistas["c" + x] = x + " no es múltiplo de " + p[0] + " y de " + p[1] + " a la vez.";')
R('return { enun: "To calculate " + fr(1, p[0]) + " + " + fr(1, p[1]) + ", what is the smallest common denominator?",', 'return { enun: "Para calcular " + fr(1, p[0]) + " + " + fr(1, p[1]) + ", ¿cuál es el denominador común más pequeño?",')
R('pista: "Go through the multiples of " + mayor + " until you find one that " + menor + " also goes into.",', 'pista: "Recorra los múltiplos de " + mayor + " hasta encontrar uno en el que también quepa el " + menor + ".",')
R('bien: "Multiples of " + mayor + ": " + mult.join(", ") + ". " + M + " is the first one that " + menor + " also goes into.",', 'bien: "Múltiplos de " + mayor + ": " + mult.join(", ") + ". " + M + " es el primero en el que también cabe el " + menor + ".",')
R('mal: "Multiples of " + mayor + ": " + mult.join(", ") + ". The first one that " + menor + " also goes into is " + M + "." };', 'mal: "Múltiplos de " + mayor + ": " + mult.join(", ") + ". El primero en el que también cabe el " + menor + " es " + M + "." };')
R('return { enun: "Calculate " + fr(p[0], p[1])', 'return { enun: "Calcule " + fr(p[0], p[1])')
R('solucion: "Common denominator " + M + ": " + fr(p[0], p[1]) + " = " + fr(a2, M) + " and " + fr(p[2], p[3]) + " = " + fr(b2, M) + ". Then "', 'solucion: "Denominador común " + M + ": " + fr(p[0], p[1]) + " = " + fr(a2, M) + " y " + fr(p[2], p[3]) + " = " + fr(b2, M) + ". Después "')
R('". Answer: <strong>" + txtV(R) + "</strong>.",', '". Respuesta: <strong>" + txtV(R) + "</strong>.",')
R('msg: "Do not " + (suma ? "add" : "subtract") + " the tops and the bottoms. First make the denominators the same." }], true) };', 'msg: "No " + (suma ? "sume" : "reste") + " los de arriba y los de abajo. Primero iguale los denominadores." }], true) };')
R("/* ============ MODULE 3 · simplify the result ============ */", "/* ============ MÓDULO 3 · simplificar el resultado ============ */")
t.todas(' and write the answer in simplest form.";', ' y escriba el resultado en su forma más simple.";')
R('enun = "Calculate " + fr(a, d)', 'enun = "Calcule " + fr(a, d)')
R('enun = "Calculate " + fr(p[0], p[1])', 'enun = "Calcule " + fr(p[0], p[1])')
R('", so the sum is " + r + "/" + d + ". "', '", así que la suma es " + r + "/" + d + ". "')
R('(R.d !== d ? "Divide the top and the bottom by " + mcd(r, d)', '(R.d !== d ? "Divida el numerador y el denominador entre " + mcd(r, d)')
R('(R.n > R.d ? R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + " with remainder " + (R.n % R.d) + "." : ""));', '(R.n > R.d ? R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + ", residuo " + (R.n % R.d) + "." : ""));')
R('sol = "Common denominator " + M + ": "', 'sol = "Denominador común " + M + ": "')
R('(R.d !== M ? "Divide the top and the bottom by " + mcd(num, M)', '(R.d !== M ? "Divida el numerador y el denominador entre " + mcd(num, M)')
R('(R.n > R.d && R.d !== 1 ? R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + " with remainder " + (R.n % R.d) + "." : "");', '(R.n > R.d && R.d !== 1 ? R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + ", residuo " + (R.n % R.d) + "." : "");')
R('return { enun: enun, solucion: sol + " Answer: <strong>" + txtV(R) + "</strong>" + (R.n > R.d && R.d !== 1 ? " (or " + R.n + "/" + R.d + ")" : "") + ".", evalua: evFr(R, [], true) };', 'return { enun: enun, solucion: sol + " Respuesta: <strong>" + txtV(R) + "</strong>" + (R.n > R.d && R.d !== 1 ? " (o " + R.n + "/" + R.d + ")" : "") + ".", evalua: evFr(R, [], true) };')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-4-2.html")
