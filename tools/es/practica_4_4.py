"""Crea es/matematicas/nivel-1/practica-4-4.html a partir de math/level-1/practice-4-4.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-4-4.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 4.4 · Operaciones con números mixtos — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 4.4 · Operations with mixed numbers · LearnGED</title>", "<title>Práctica · Lección 4.4 · Operaciones con números mixtos · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 4 · Fractions</div>', '<div class="ruta">Nivel 1 · Tema 4 · Fracciones</div>')
R("<h1>Lesson 4.4 · Operations with mixed numbers</h1>", "<h1>Lección 4.4 · Operaciones con números mixtos</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#convert">Mixed numbers and improper fractions</a></li>', '<li><a href="#convertir">Números mixtos y fracciones impropias</a></li>')
R('<li><a href="#multiply-divide">Multiply and divide mixed numbers</a></li>', '<li><a href="#multiplicar-dividir">Multiplicar y dividir números mixtos</a></li>')
R('<li><a href="#add-subtract">Add and subtract mixed numbers</a></li>', '<li><a href="#sumar-restar">Sumar y restar números mixtos</a></li>')
R('<li><a href="#real-life">Mixed numbers in real life</a></li>', '<li><a href="#vida-real">Los números mixtos en la vida real</a></li>')
t.todas('">Answer</label>', '">Respuesta</label>')
t.todas('<p class="nota">Type a mixed number with a space (2&nbsp;1/3), a fraction with a slash (7/3), or a whole number. Simplify the fraction part.', '<p class="nota">Escriba un número mixto con un espacio (2&nbsp;1/3), una fracción con una raya inclinada (7/3) o un número entero. Simplifique la parte de fracción.')
R(" Do not type the units.</p>", " No escriba las unidades.</p>")
# 1
R('id="convert" open>', 'id="convertir" open>'); R("<h2>Mixed numbers and improper fractions</h2>", "<h2>Números mixtos y fracciones impropias</h2>")
R("""<p>A <strong>mixed number</strong> is a whole number with a fraction: 2&nbsp;1/2 is "two and one half." The secret of the whole lesson is
      to change mixed numbers to improper fractions. <strong>Mixed to improper:</strong> whole number × denominator + numerator, over the same
      denominator. <strong>Improper to mixed:</strong> divide; the quotient is the whole number and the remainder is the numerator.</p>""",
  """<p>Un <strong>número mixto</strong> es un número entero con una fracción: 2&nbsp;1/2 es «dos y un medio». El secreto de toda la lección es
      convertir los números mixtos en fracciones impropias. <strong>De mixto a impropia:</strong> entero × denominador + numerador, sobre el mismo
      denominador. <strong>De impropia a mixto:</strong> divida; el cociente es el entero y el residuo es el numerador.</p>""")
R("<h3>Change it and see the bars</h3>", "<h3>Conviértalo y vea las barras</h3>")
R('<label for="cv-x">Type a mixed number (3 1/4) or an improper fraction (13/4)</label>', '<label for="cv-x">Escriba un número mixto (3 1/4) o una fracción impropia (13/4)</label>')
R("<h3>Practice: change it</h3>", "<h3>Practique: conviértalo</h3>")
R('<p class="nota">For a mixed number, type the whole number, a space, and the fraction: 3&nbsp;1/4. For an improper fraction, use a slash: 13/4.</p>', '<p class="nota">Para un número mixto, escriba el entero, un espacio y la fracción: 3&nbsp;1/4. Para una fracción impropia, use una raya inclinada: 13/4.</p>')
# 2
R('id="multiply-divide">', 'id="multiplicar-dividir">'); R("<h2>Multiply and divide mixed numbers</h2>", "<h2>Multiplicar y dividir números mixtos</h2>")
R("""<p>The rule has no exceptions: <strong>never</strong> multiply or divide the whole numbers on one side and the fractions on the other.
      Change everything to improper fractions, then multiply straight across, or keep, change, flip, as in Lesson 4.3.</p>""",
  """<p>La regla no tiene excepciones: <strong>nunca</strong> multiplique ni divida los enteros por un lado y las fracciones por otro.
      Convierta todo en fracciones impropias, y después multiplique en línea recta, o deje, cambie y voltee, como en la Lección 4.3.</p>""")
R('<div class="caja-tip"><strong>Example:</strong> ', '<div class="caja-tip"><strong>Ejemplo:</strong> ')
R("<h3>Practice: multiply or divide</h3>", "<h3>Practique: multiplique o divida</h3>")
# 3
R('id="add-subtract">', 'id="sumar-restar">'); R("<h2>Add and subtract mixed numbers</h2>", "<h2>Sumar y restar números mixtos</h2>")
R("""<p>The lesson's way: <strong>change to improper fractions</strong>, find a common denominator, add or subtract the numerators, and change
      back to a mixed number. Another way is to work <strong>wholes with wholes and fractions with fractions</strong>; when you subtract and the
      top fraction is too small, you <strong>borrow</strong> one whole (1 = 4/4, 1 = 8/8). The explorer shows both ways so you can compare them.</p>""",
  """<p>La forma de la lección: <strong>convierta en fracciones impropias</strong>, halle un denominador común, sume o reste los numeradores y vuelva
      a convertir en número mixto. Otra forma es trabajar <strong>enteros con enteros y fracciones con fracciones</strong>; cuando resta y la
      fracción de arriba es demasiado pequeña, <strong>pide prestado</strong> un entero (1 = 4/4, 1 = 8/8). La herramienta muestra las dos formas para que las compare.</p>""")
R("<h3>Step by step, two ways</h3>", "<h3>Paso a paso, de dos formas</h3>")
R('<label for="sr-a">First number</label>', '<label for="sr-a">Primer número</label>')
R('<label for="sr-o">Operation</label><select id="sr-o"><option value="-">− subtract</option><option value="+">+ add</option></select>', '<label for="sr-o">Operación</label><select id="sr-o"><option value="-">− restar</option><option value="+">+ sumar</option></select>')
R('<label for="sr-b">Second number</label>', '<label for="sr-b">Segundo número</label>')
R("<h3>Practice: add and subtract</h3>", "<h3>Practique: sume y reste</h3>")
# 4
R('id="real-life">', 'id="vida-real">'); R("<h2>Mixed numbers in real life</h2>", "<h2>Los números mixtos en la vida real</h2>")
R("""<p>Carpentry, recipes, and time: a board 5&nbsp;1/2 feet long, 1&nbsp;3/4 cups of flour, 2&nbsp;1/2 hours of work.
      Decide the operation first: "left" means subtract, "in all" means add, "times the recipe" means multiply, "how many pieces" means divide.</p>""",
  """<p>Carpintería, recetas y tiempo: una tabla de 5&nbsp;1/2 pies de largo, 1&nbsp;3/4 tazas de harina, 2&nbsp;1/2 horas de trabajo.
      Decida primero la operación: «queda» quiere decir restar, «en total» quiere decir sumar, «veces la receta» quiere decir multiplicar, «cuántos pedazos» quiere decir dividir.</p>""")
R("<h3>Practice: word problems with mixed numbers</h3>", "<h3>Practique: problemas verbales con números mixtos</h3>")
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
R("/* a random mixed number {e, n, d} with the fraction in simplest form */", "/* un número mixto al azar {e, n, d} con la fracción en su forma más simple */")
R("/* ============ MODULE 1 · convert ============ */", "/* ============ MÓDULO 1 · convertir ============ */")
R('e + " whole bars and " + n + " of " + d + " parts of another bar: " + N + "/" + d + "."', 'e + " barras enteras y " + n + " de " + d + " partes de otra barra: " + N + "/" + d + "."')
R("""o.innerHTML = '<div class="linea">1. Whole number × denominator: ' + e + ' × ' + d + ' = ' + (e * d) + ' (the parts in the ' + e + ' whole bar' + (e === 1 ? '' : 's') + ').</div><div class="linea">2. Add the numerator: ' + (e * d) + ' + ' + n + ' = ' + N + '.</div><div class="linea">3. The denominator stays: ' + d + '.</div>""",
  """o.innerHTML = '<div class="linea">1. Entero × denominador: ' + e + ' × ' + d + ' = ' + (e * d) + ' (las partes de ' + (e === 1 ? 'la barra entera' : 'las ' + e + ' barras enteras') + ').</div><div class="linea">2. Sume el numerador: ' + (e * d) + ' + ' + n + ' = ' + N + '.</div><div class="linea">3. El denominador se queda: ' + d + '.</div>""")
R('f.p + " parts of size 1/" + f.q + "."', 'f.p + " partes de tamaño 1/" + f.q + "."')
R("""o.innerHTML = '<div class="linea">1. Divide: ' + f.p + ' ÷ ' + f.q + ' = ' + q + ', remainder ' + r + '.</div><div class="linea">2. The quotient (' + q + ') is the whole number; the remainder (' + r + ') is the numerator; the denominator stays.</div>""",
  """o.innerHTML = '<div class="linea">1. Divida: ' + f.p + ' ÷ ' + f.q + ' = ' + q + ', residuo ' + r + '.</div><div class="linea">2. El cociente (' + q + ') es el entero; el residuo (' + r + ') es el numerador; el denominador se queda.</div>""")
R("""'<div class="linea">It is a proper fraction (less than 1): it has no whole part.</div>'""", """'<div class="linea">Es una fracción propia (menor que 1): no tiene parte entera.</div>'""")
R("""'<div class="linea">The fraction part can still be simplified: '""", """'<div class="linea">La parte de fracción todavía se puede simplificar: '""")
R('o.innerHTML = "Type a mixed number like 3 1/4 or an improper fraction like 13/4 (denominator up to 12).";', 'o.innerHTML = "Escriba un número mixto como 3 1/4 o una fracción impropia como 13/4 (denominador hasta 12).";')
R('if (Math.random() < 0.5) return { enun: "Change " + mixH(m.e, m.n, m.d) + " to an improper fraction.",', 'if (Math.random() < 0.5) return { enun: "Convierta " + mixH(m.e, m.n, m.d) + " en fracción impropia.",')
R('solucion: m.e + " × " + m.d + " + " + m.n + " = " + N + ", over " + m.d + ". Answer: <strong>"', 'solucion: m.e + " × " + m.d + " + " + m.n + " = " + N + ", sobre " + m.d + ". Respuesta: <strong>"')
R('return { estado: "mal", msg: "Write it as an improper fraction, with a slash." };', 'return { estado: "mal", msg: "Escríbalo como fracción impropia, con una raya inclinada." };')
R('{ estado: "mal", msg: "That is the same mixed number. Write it as an improper fraction, with a slash." } : { estado: "mal", msg: "Write it as an improper fraction, with a slash." };', '{ estado: "mal", msg: "Ese es el mismo número mixto. Escríbalo como fracción impropia, con una raya inclinada." } : { estado: "mal", msg: "Escríbalo como fracción impropia, con una raya inclinada." };')
R('msg: "Multiply the whole number by the denominator (not by the numerator), then add the numerator." }, { v: red(m.e + m.n, m.d), msg: "First multiply the whole number by the denominator: "', 'msg: "Multiplique el entero por el denominador (no por el numerador), y después sume el numerador." }, { v: red(m.e + m.n, m.d), msg: "Primero multiplique el entero por el denominador: "')
R('msg: "You forgot to add the numerator, " + m.n + "." }], false)(t); } };', 'msg: "Se olvidó de sumar el numerador, " + m.n + "." }], false)(t); } };')
R('return { enun: "Change " + fr(N, m.d) + " to a mixed number.",', 'return { enun: "Convierta " + fr(N, m.d) + " en número mixto.",')
R('solucion: N + " ÷ " + m.d + " = " + m.e + ", remainder " + m.n + ". Answer: <strong>"', 'solucion: N + " ÷ " + m.d + " = " + m.e + ", residuo " + m.n + ". Respuesta: <strong>"')
R('msg: "That is the same value, but write it as a mixed number: the whole number, a space, and the fraction." };', 'msg: "Ese es el mismo valor, pero escríbalo como número mixto: el entero, un espacio y la fracción." };')
R('msg: "Check the denominator: it stays " + m.d + "." }], true)(t); } };', 'msg: "Revise el denominador: se queda en " + m.d + "." }], true)(t); } };')
R("/* ============ MODULE 2 · multiply and divide ============ */", "/* ============ MÓDULO 2 · multiplicar y dividir ============ */")
R('var sol = mixS(a.e, a.n, a.d) + " = " + imp(a) + " and " + mixS(b.e, b.n, b.d) + " = " + imp(b) + ". " + (mult ? imp(a) + " × " + imp(b) : "Keep, change, flip: "', 'var sol = mixS(a.e, a.n, a.d) + " = " + imp(a) + " y " + mixS(b.e, b.n, b.d) + " = " + imp(b) + ". " + (mult ? imp(a) + " × " + imp(b) : "Dejar, cambiar, voltear: "')
R('" = " + R.n + "/" + R.d : "") + ". Answer: <strong>" + txtV(R) + "</strong>.";\n  return { enun: "Calculate " + mixH(a.e, a.n, a.d)', '" = " + R.n + "/" + R.d : "") + ". Respuesta: <strong>" + txtV(R) + "</strong>.";\n  return { enun: "Calcule " + mixH(a.e, a.n, a.d)')
R('msg: "Do not multiply the whole numbers and the fractions separately. Change both to improper fractions first." }] : [{ v: opV(A, B, "×"), msg: "You multiplied without flipping. To divide, flip the second number (as an improper fraction)." }, { v: opV(B, A, "÷"), msg: "You flipped the first number. Flip only the second one." }], true) };',
  'msg: "No multiplique los enteros y las fracciones por separado. Primero convierta los dos en fracciones impropias." }] : [{ v: opV(A, B, "×"), msg: "Multiplicó sin voltear. Para dividir, voltee el segundo número (como fracción impropia)." }, { v: opV(B, A, "÷"), msg: "Volteó el primer número. Voltee solo el segundo." }], true) };')
R("/* ============ MODULE 3 · add and subtract ============ */", "/* ============ MÓDULO 3 · sumar y restar ============ */")
R('h.push("Change to improper fractions: " + mixS(a.e, a.n, a.d) + " = " + A + "/" + a.d + " and "', 'h.push("Convierta en fracciones impropias: " + mixS(a.e, a.n, a.d) + " = " + A + "/" + a.d + " y "')
R('if (a.d !== b.d) h.push("Common denominator " + M + ": " + A2 + "/" + M + " and " + B2 + "/" + M + ".");', 'if (a.d !== b.d) h.push("Denominador común " + M + ": " + A2 + "/" + M + " y " + B2 + "/" + M + ".");')
R('h.push((o === "+" ? "Add" : "Subtract") + " the numerators: " + A2 + " " + (o === "+" ? "+" : "−") + " " + B2 + " = " + r + ", so "', 'h.push((o === "+" ? "Sume" : "Reste") + " los numeradores: " + A2 + " " + (o === "+" ? "+" : "−") + " " + B2 + " = " + r + ", así que "')
R('if (R.n >= R.d && R.d > 1) h.push("Change back: " + R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + ", remainder " + (R.n % R.d) + ", so "', 'if (R.n >= R.d && R.d > 1) h.push("Vuelva a convertir: " + R.n + " ÷ " + R.d + " = " + Math.floor(R.n / R.d) + ", residuo " + (R.n % R.d) + ", así que "')
R('h.push("Common denominator " + M + ": " + mixS(a.e, a.n, a.d) + " = " + mixS(a.e, an, M) + " and "', 'h.push("Denominador común " + M + ": " + mixS(a.e, a.n, a.d) + " = " + mixS(a.e, an, M) + " y "')
R('h.push("You must take away " + bn + "/" + M + " but " + (an ? "only have " + an + "/" + M : "have no fraction to take it from") + ". Borrow 1 whole = "', 'h.push("Tiene que quitar " + bn + "/" + M + ", pero " + (an ? "solo tiene " + an + "/" + M : "no tiene fracción de donde quitar") + ". Pida prestado 1 entero = "')
R('h.push((o === "+" ? "Add" : "Subtract") + " the wholes: " + (o === "+" ? a.e + " + " + b.e : ea + " − " + b.e) + " = " + e + ". Then the fractions: "', 'h.push((o === "+" ? "Sume" : "Reste") + " los enteros: " + (o === "+" ? a.e + " + " + b.e : ea + " − " + b.e) + " = " + e + ". Después las fracciones: "')
R('if (n >= M){ h.push(n + "/" + M + " is more than one whole: " + n + "/" + M + " = 1 and " + (n - M) + "/" + M + ", so add 1 to the " + e + "."); e += 1; n -= M; }', 'if (n >= M){ h.push(n + "/" + M + " es más que un entero: " + n + "/" + M + " = 1 y " + (n - M) + "/" + M + ", así que súmele 1 al " + e + "."); e += 1; n -= M; }')
R('if (n && sf.d !== M) h.push("Simplify the fraction: "', 'if (n && sf.d !== M) h.push("Simplifique la fracción: "')
R('s.innerHTML = "Type two mixed numbers with a space, for example 5 1/4 and 2 3/4 (or a whole number; denominators up to 12)."; return; }', 's.innerHTML = "Escriba dos números mixtos con un espacio, por ejemplo 5 1/4 y 2 3/4 (o un número entero; denominadores hasta 12)."; return; }')
R('s.innerHTML = "To subtract, the first number must be the greater one."; return; }', 's.innerHTML = "Para restar, el primer número tiene que ser el mayor."; return; }')
R("""s.innerHTML = '<div class="linea"><strong>The lesson\\'s way: improper fractions</strong></div>'""", """s.innerHTML = '<div class="linea"><strong>La forma de la lección: fracciones impropias</strong></div>'""")
R("""'<div class="linea" style="margin-top:10px"><strong>Another way: wholes and fractions</strong></div>'""", """'<div class="linea" style="margin-top:10px"><strong>Otra forma: enteros y fracciones</strong></div>'""")
R('return { enun: "Calculate " + mixH(a.e, a.n, a.d) + (suma ? " + " : " − ") + mixH(b.e, b.n, b.d) + ".", solucion: pasosImp(a, b, suma ? "+" : "-").pasos.join(" ") + " Answer: <strong>" + txtV(R) + "</strong>.",', 'return { enun: "Calcule " + mixH(a.e, a.n, a.d) + (suma ? " + " : " − ") + mixH(b.e, b.n, b.d) + ".", solucion: pasosImp(a, b, suma ? "+" : "-").pasos.join(" ") + " Respuesta: <strong>" + txtV(R) + "</strong>.",')
R('msg: "It looks like you subtracted the fractions the wrong way around. Use improper fractions, or borrow one whole when the top fraction is too small." }] : [], true) };', 'msg: "Parece que restó las fracciones al revés. Use fracciones impropias, o pida prestado un entero cuando la fracción de arriba es demasiado pequeña." }] : [], true) };')
R("/* ============ MODULE 4 · real life ============ */", "/* ============ MÓDULO 4 · vida real ============ */")
R('enun = "A board is " + mixH(tabla.e, tabla.n, tabla.d) + " feet long. You cut off " + mixH(corte.e, corte.n, corte.d) + " feet. How many feet are left?"; sol = "\\"Left\\" means subtract. "', 'enun = "Una tabla mide " + mixH(tabla.e, tabla.n, tabla.d) + " pies de largo. Usted corta " + mixH(corte.e, corte.n, corte.d) + " pies. ¿Cuántos pies quedan?"; sol = "«Quedan» quiere decir restar. "')
R('enun = "A recipe calls for " + mixH(h.e, h.n, h.d) + " cups of flour. How many cups do you need to make the recipe " + k + " times?"; sol = "\\"" + k + " times the recipe\\" means multiply: "', 'enun = "Una receta pide " + mixH(h.e, h.n, h.d) + " tazas de harina. ¿Cuántas tazas necesita para hacer la receta " + k + " veces?"; sol = "«" + k + " veces la receta» quiere decir multiplicar: "')
R('". Answer: <strong>" + txtV(R) + "</strong> cups.";', '". Respuesta: <strong>" + txtV(R) + "</strong> tazas.";')
R('msg: "You multiplied only the whole number. Change " + mixS(h.e, h.n, h.d) + " to " + imp(h) + " first." }); }', 'msg: "Multiplicó solo el entero. Primero convierta " + mixS(h.e, h.n, h.d) + " en " + imp(h) + "." }); }')
R('enun = "Ana worked " + mixH(a.e, a.n, a.d) + " hours on Monday and " + mixH(b.e, b.n, b.d) + " hours on Tuesday. How many hours did she work in all?"; sol = "\\"In all\\" means add. "', 'enun = "Ana trabajó " + mixH(a.e, a.n, a.d) + " horas el lunes y " + mixH(b.e, b.n, b.d) + " horas el martes. ¿Cuántas horas trabajó en total?"; sol = "«En total» quiere decir sumar. "')
R('enun = "How many pieces " + pz[0] + "/" + pz[1] + " yard long can you cut from a ribbon " + mixH(cinta.e, cinta.n, cinta.d) + " yards long?"; sol = "\\"How many pieces\\" means divide: "', 'enun = "¿Cuántos pedazos de " + pz[0] + "/" + pz[1] + " de yarda se pueden cortar de una cinta de " + mixH(cinta.e, cinta.n, cinta.d) + " yardas?"; sol = "«Cuántos pedazos» quiere decir dividir: "')
R('". Answer: <strong>" + R.n + "</strong> pieces."; }', '". Respuesta: <strong>" + R.n + "</strong> pedazos."; }')
R('enun = "A jug holds " + tot + " quarts of juice. You pour out " + mixH(us.e, us.n, us.d) + " quarts. How many quarts are left?"; sol = "\\"Left\\" means subtract. "', 'enun = "Una jarra tiene " + tot + " cuartos de galón de jugo. Usted sirve " + mixH(us.e, us.n, us.d) + " cuartos. ¿Cuántos cuartos de galón quedan?"; sol = "«Quedan» quiere decir restar. "')
R('if (sol.indexOf("Answer:") < 0) sol += " Answer: <strong>" + txtV(R) + "</strong>.";', 'if (sol.indexOf("Respuesta:") < 0) sol += " Respuesta: <strong>" + txtV(R) + "</strong>.";')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-4-4.html")
