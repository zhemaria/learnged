"""Crea es/matematicas/nivel-1/practica-3-1.html a partir de math/level-1/practice-3-1.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-3-1.html")
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 3.1 · Decimales — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 3.1 · Decimals: read, write, compare, and round · LearnGED</title>", "<title>Práctica · Lección 3.1 · Decimales: leer, escribir, comparar y redondear · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 3 · Decimals</div>', '<div class="ruta">Nivel 1 · Tema 3 · Decimales</div>')
R("<h1>Lesson 3.1 · Decimals: read, write, compare, and round</h1>", "<h1>Lección 3.1 · Decimales: leer, escribir, comparar y redondear</h1>")
R("Three practice activities on one page. The exercises change every time, so you can practice as many times as you want. If you make a mistake, you get a hint and another try.",
  "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez, así que puede practicar todas las veces que quiera. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#place-value">Place value after the decimal point</a></li>', '<li><a href="#valor-posicional">El valor posicional después del punto</a></li>')
R('<li><a href="#compare">Compare and order decimals</a></li>', '<li><a href="#comparar">Comparar y ordenar decimales</a></li>')
R('<li><a href="#round">Round decimals</a></li>', '<li><a href="#redondear">Redondear decimales</a></li>')
# 1
R('id="place-value" open>', 'id="valor-posicional" open>'); R("<h2>Place value after the decimal point</h2>", "<h2>El valor posicional después del punto</h2>")
R("""<p>Decimals are the place value chart <strong>continued to the right</strong>. The point separates the whole part from the parts:
      in $3.99 there are 3 whole dollars and 99 cents. To the right of the point are the <strong>tenths</strong>, the
      <strong>hundredths</strong>, and the <strong>thousandths</strong>. Each place is worth 10 times less than the place before it.</p>""",
  """<p>Los decimales son la tabla de valor posicional <strong>continuada hacia la derecha</strong>. El punto separa la parte entera de las partes:
      en $3.99 hay 3 dólares completos y 99 centavos. A la derecha del punto están las <strong>décimas</strong>, las
      <strong>centésimas</strong> y las <strong>milésimas</strong>. Cada lugar vale 10 veces menos que el lugar anterior.</p>""")
R("<h3>Put a decimal in the chart</h3>", "<h3>Ponga un decimal en la tabla</h3>")
R('<label for="vd-n">Type a decimal (up to 3 digits after the point)</label>', '<label for="vd-n">Escriba un decimal (hasta 3 dígitos después del punto)</label>')
R('<p class="nota">Press a digit in the chart to see what it is worth.</p>', '<p class="nota">Pulse un dígito de la tabla para ver cuánto vale.</p>')
R("<strong>The last place gives the name:</strong> 0.7 is seven <em>tenths</em>; 0.07 is seven <em>hundredths</em>; 0.007 is seven <em>thousandths</em>.", "<strong>El último lugar da el nombre:</strong> 0.7 es siete <em>décimas</em>; 0.07 es siete <em>centésimas</em>; 0.007 es siete <em>milésimas</em>.")
R("<h3>Practice: which place is it in?</h3>", "<h3>Practique: ¿en qué lugar está?</h3>")
R("<h3>Practice: how do you read it?</h3>", "<h3>Practique: ¿cómo se lee?</h3>")
# 2
R('id="compare">', 'id="comparar">'); R("<h2>Compare and order decimals</h2>", "<h2>Comparar y ordenar decimales</h2>")
R("""<p>Compare <strong>place by place, from left to right</strong>. If the numbers have a different number of digits, add
      <strong>zeros on the right</strong>. They do not change the value: 0.6 = 0.60 = 0.600.</p>""",
  """<p>Compare <strong>lugar por lugar, de izquierda a derecha</strong>. Si los números tienen distinta cantidad de dígitos, agregue
      <strong>ceros a la derecha</strong>. No cambian el valor: 0.6 = 0.60 = 0.600.</p>""")
R("<h3>Compare on the number line</h3>", "<h3>Compare en la recta numérica</h3>")
R('<label for="cd-a">First decimal</label>', '<label for="cd-a">Primer decimal</label>')
R('<label for="cd-b">Second decimal</label>', '<label for="cd-b">Segundo decimal</label>')
R("""<strong>The most common mistake:</strong> thinking that 0.58 is greater than 0.6 "because it has more digits." With decimals,
        more digits do not mean more value.""",
  """<strong>El error más común:</strong> pensar que 0.58 es mayor que 0.6 «porque tiene más dígitos». En los decimales,
        más dígitos no quiere decir más valor.""")
R("<h3>Practice: which symbol goes there?</h3>", "<h3>Practique: ¿qué símbolo va?</h3>")
R("<h3>Practice: the cheapest or the most expensive?</h3>", "<h3>Practique: ¿el más barato o el más caro?</h3>")
# 3
R('id="round">', 'id="redondear">'); R("<h2>Round decimals</h2>", "<h2>Redondear decimales</h2>")
R("""<p>It is the same neighbor-on-the-right rule from Lesson 1.1: if the neighbor is 0 to 4, the digit stays the same; if it is
      5 to 9, the digit goes up by one. The difference: the digits on the right <strong>are dropped</strong>. They do not turn into zeros.</p>""",
  """<p>Es la misma regla del vecino de la derecha de la Lección 1.1: si el vecino es de 0 a 4, el dígito se queda igual; si es
      de 5 a 9, el dígito sube uno. La diferencia: los dígitos de la derecha <strong>se eliminan</strong>. No se vuelven ceros.</p>""")
R("<h3>Round on the number line</h3>", "<h3>Redondee en la recta numérica</h3>")
R('<label for="rd-n">Decimal</label>', '<label for="rd-n">Decimal</label>')
R('<label for="rd-l">Round to</label><select id="rd-l"><option value="0">the nearest whole number</option><option value="1" selected>the nearest tenth</option><option value="2">the nearest hundredth (the cent)</option></select>',
  '<label for="rd-l">Redondear</label><select id="rd-l"><option value="0">al entero más cercano</option><option value="1" selected>a la décima más cercana</option><option value="2">a la centésima más cercana (al centavo)</option></select>')
R("<h3>Practice: round</h3>", "<h3>Practique: redondee</h3>")
R('<label for="p5-r">Rounded number</label>', '<label for="p5-r">Número redondeado</label>')
R('<p class="nota">Type the number with a decimal point, for example 5.3.</p>', '<p class="nota">Escriba el número con punto decimal, por ejemplo 5.3.</p>')
R("<p><strong>Level 1 · Topic 3 · Decimals · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 3 · Decimales · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Exact decimals (scaled whole numbers, no floating-point surprises) ============ */", "/* ============ Decimales exactos (enteros escalados, sin sorpresas de coma flotante) ============ */")
R('var LUG = ["", "tenths", "hundredths", "thousandths"], LUG1 = ["", "tenth", "hundredth", "thousandth"];', 'var LUG = ["", "décimas", "centésimas", "milésimas"], LUG1 = ["", "décima", "centésima", "milésima"];')
R('''/* Read a decimal in words, US style: the point is read "and" */
function decWords(s){
  s = String(s); var p = s.split("."), e = +p[0], d = p[1] || "";
  if (!d) return words(e);
  var n = +d, k = d.length, dec = (n === 0 ? "zero" : words(n)) + " " + (n === 1 ? LUG1[k] : LUG[k]);
  return (e ? words(e) + " and " : "") + dec;
}''',
  '''/* Número en femenino, para décimas, centésimas y milésimas: «seiscientas veinticinco» */
function fem(s){ return s.replace(/ientos/g, "ientas").replace(/veintiuno$/, "veintiuna").replace(/ uno$/, " una").replace(/^uno$/, "una"); }
/* Leer un decimal con palabras: el punto se lee «con» */
function decWords(s){
  s = String(s); var p = s.split("."), e = +p[0], d = p[1] || "";
  if (!d) return enLetras(e);
  var n = +d, k = d.length, dec = (n === 0 ? "cero" : fem(enLetras(n))) + " " + (n === 1 ? LUG1[k] : LUG[k]);
  return (e ? enLetras(e) + " con " : "") + dec;
}''')
R("/* ============ MODULE 1 · place value ============ */", "/* ============ MÓDULO 1 · valor posicional ============ */")
R('var COLS = [["Hundreds", 2], ["Tens", 1], ["Ones", 0], ["Point", null], ["Tenths", -1], ["Hundredths", -2], ["Thousandths", -3]];', 'var COLS = [["Centenas", 2], ["Decenas", 1], ["Unidades", 0], ["Punto", null], ["Décimas", -1], ["Centésimas", -2], ["Milésimas", -3]];')
R('av.textContent = "Type a decimal with a point, for example 4.625 (up to 3 digits before and after the point)."; return;', 'av.textContent = "Escriba un decimal con punto, por ejemplo 4.625 (hasta 3 dígitos antes y después del punto)."; return;')
R("""'<table class="vp"><caption class="sr-only">Place value chart for ' + s + '</caption><tr class="fila-grupo"><td colspan="3">Whole part</td><td></td><td colspan="3">Decimal part</td></tr><tr>'""",
  """'<table class="vp"><caption class="sr-only">Tabla de valor posicional de ' + s + '</caption><tr class="fila-grupo"><td colspan="3">Parte entera</td><td></td><td colspan="3">Parte decimal</td></tr><tr>'""")
R("""aria-label="Digit ' + x + ', ' + COLS[i][0].toLowerCase() + ' place">'""", """aria-label="Dígito ' + x + ', lugar de las ' + COLS[i][0].toLowerCase() + '">'""")
R("""var out = '<div class="linea">Read it: <strong>' + decWords(s) + '</strong>.</div><div class="linea">Whole part: ' + (e || "0") + '. Decimal part: ' + (d ? d + " (" + LUG[d.length] + ")" : "none") + '.</div>';""",
  """var out = '<div class="linea">Se lee: <strong>' + decWords(s) + '</strong>.</div><div class="linea">Parte entera: ' + (e || "0") + '. Parte decimal: ' + (d ? d + " (" + LUG[d.length] + ")" : "ninguna") + '.</div>';""")
R("""out += '<div class="linea veredicto">The ' + x + ' is in the ' + c[0].toLowerCase() + ' place. It is worth ' +
      (c[1] >= 0 ? com(x * Math.pow(10, c[1])) : limpia(deEsc(x, -c[1])) + " (" + words(x) + " " + (x === 1 ? LUG1[-c[1]] : LUG[-c[1]]) + ")") + '.</div>';""",
  """out += '<div class="linea veredicto">El ' + x + ' está en las ' + c[0].toLowerCase() + '. Vale ' +
      (c[1] >= 0 ? com(x * Math.pow(10, c[1])) : limpia(deEsc(x, -c[1])) + " (" + fem(enLetras(x)) + " " + (x === 1 ? LUG1[-c[1]] : LUG[-c[1]]) + ")") + '.</div>';""")
R('var nom = ["The ones", "The tenths", "The hundredths", "The thousandths"];', 'var nom = ["En las unidades", "En las décimas", "En las centésimas", "En las milésimas"];')
R('var pistas = { l0: "The ones are to the left of the point. This digit is to the right." };', 'var pistas = { l0: "Las unidades están a la izquierda del punto. Este dígito está a la derecha." };')
R('pistas["l" + j] = "Count the places after the point: tenths (1st), hundredths (2nd), thousandths (3rd).";', 'pistas["l" + j] = "Cuente los lugares después del punto: décimas (1.º), centésimas (2.º), milésimas (3.º).";')
R('enun: "In the number <strong>" + marcado + "</strong>, which place is the underlined digit <strong>" + dig + "</strong> in?",', 'enun: "En el número <strong>" + marcado + "</strong>, ¿en qué lugar está el dígito subrayado, el <strong>" + dig + "</strong>?",')
R('bien: "It is place number " + (k + 1) + " after the point: the " + LUG[k + 1] + ".",', 'bien: "Es el lugar número " + (k + 1) + " después del punto: las " + LUG[k + 1] + ".",')
R('mal: "After the point come the tenths, the hundredths, and the thousandths. The " + dig + " is in the " + LUG[k + 1] + "." };', 'mal: "Después del punto vienen las décimas, las centésimas y las milésimas. El " + dig + " está en las " + LUG[k + 1] + "." };')
R('return { enun: "How do you read <strong>" + s + "</strong>?",', 'return { enun: "¿Cómo se lee <strong>" + s + "</strong>?",')
R('pista: "Count the digits after the point. The last digit\'s place gives the name.",', 'pista: "Cuente los dígitos después del punto. El lugar del último dígito da el nombre.",')
R('bien: "The last place, the " + LUG[k] + ", gives the name.",', 'bien: "El último lugar, el de las " + LUG[k] + ", da el nombre.",')
R('mal: "You read it \\"" + decWords(s) + ".\\" The last digit is in the " + LUG[k] + "." };', 'mal: "Se lee «" + decWords(s) + "». El último dígito está en las " + LUG[k] + "." };')
R("/* ============ MODULE 2 · compare ============ */", "/* ============ MÓDULO 2 · comparar ============ */")
R('out.innerHTML = "Type two decimals with a point, for example 0.6 and 0.58.";', 'out.innerHTML = "Escriba dos decimales con punto, por ejemplo 0.6 y 0.58.";')
R("""(nDec(a) !== nDec(b) ? 'Add zeros so they are the same length: ' : 'They are already the same length: ') + '<strong>' + pa + '</strong> and <strong>' + pb + '</strong>.</div>';""",
  """(nDec(a) !== nDec(b) ? 'Agregue ceros para igualar la longitud: ' : 'Ya tienen la misma longitud: ') + '<strong>' + pa + '</strong> y <strong>' + pb + '</strong>.</div>';""")
R("""h += '<div class="linea">The whole parts are different: ' + pa.split(".")[0] + ' and ' + pb.split(".")[0] + '. That decides it.</div>';""", """h += '<div class="linea">Las partes enteras son distintas: ' + pa.split(".")[0] + ' y ' + pb.split(".")[0] + '. Eso lo decide.</div>';""")
R("""h += '<div class="linea">Place by place, from left to right, the first different digits are ' + pa[i] + ' and ' + pb[i] + '. That decides it.</div>';""", """h += '<div class="linea">Lugar por lugar, de izquierda a derecha, los primeros dígitos distintos son ' + pa[i] + ' y ' + pb[i] + '. Eso lo decide.</div>';""")
R('"Number line with " + a + " and " + b + ". The one farther to the right is greater."', '"Recta numérica con " + a + " y " + b + ". El que está más a la derecha es mayor."')
R("""'<p class="nota">These numbers are too far apart to show on one number line.</p>'""", """'<p class="nota">Estos números están demasiado lejos para mostrarlos en una sola recta numérica.</p>'""")
R('var igual = "Add zeros so they are the same length: " + deEsc(A, k) + " and " + deEsc(B, k) + ". Then compare place by place.";', 'var igual = "Agregue ceros para igualar la longitud: " + deEsc(A, k) + " y " + deEsc(B, k) + ". Después compare lugar por lugar.";')
R('return { enOrden: true, enun: "Which symbol goes between <strong>" + a + "</strong> and <strong>" + b + "</strong>?",', 'return { enOrden: true, enun: "¿Qué símbolo va entre <strong>" + a + "</strong> y <strong>" + b + "</strong>?",')
R('bien: "With zeros: " + deEsc(A, k) + " and " + deEsc(B, k) + ".",', 'bien: "Con ceros: " + deEsc(A, k) + " y " + deEsc(B, k) + ".",')
R('mal: "Make them the same length: " + deEsc(A, k) + " and " + deEsc(B, k) + ". Now you can see that " + a + " " + gt(r) + " " + b + "." };', 'mal: "Iguale la longitud: " + deEsc(A, k) + " y " + deEsc(B, k) + ". Ahora se ve que " + a + " " + gt(r) + " " + b + "." };')
R('return { enun: "Four products cost " + ps.map(function(x){ return "$" + x; }).join(", ") + ". Which one is the <strong>" + (caro ? "most expensive" : "cheapest") + "</strong>?",',
  'var lp = ps.map(function(x){ return "$" + x; });\n  return { enun: "Cuatro productos cuestan " + lp.slice(0, 3).join(", ") + " y " + lp[3] + ". ¿Cuál es el <strong>" + (caro ? "más caro" : "más barato") + "</strong>?",')
R('pista: "All the prices have the same dollars ($" + e + "). Compare the tenths first, then the hundredths.",', 'pista: "Todos los precios tienen los mismos dólares ($" + e + "). Compare primero las décimas y después las centésimas.",')
R('bien: "In order: " + lista + ".", mal: "All the prices start with $" + e + ", so compare the tenths, then the hundredths. In order: " + lista + "." };', 'bien: "En orden: " + lista + ".", mal: "Todos los precios empiezan con $" + e + ", así que compare las décimas y después las centésimas. En orden: " + lista + "." };')
R("/* ============ MODULE 3 · round ============ */", "/* ============ MÓDULO 3 · redondear ============ */")
R('var LUGR = ["the nearest whole number", "the nearest tenth", "the nearest hundredth"];', 'var LUGR = ["al entero más cercano", "a la décima más cercana", "a la centésima más cercana"];')
R('out.innerHTML = "Type a decimal with a point, for example 5.348.";', 'out.innerHTML = "Escriba un decimal con punto, por ejemplo 5.348.";')
R("""out.innerHTML = '<div class="linea">' + s + ' has no digits after that place, so there is nothing to round.</div>';""", """out.innerHTML = '<div class="linea">' + s + ' no tiene dígitos después de ese lugar, así que no hay nada que redondear.</div>';""")
R("""aria-label="' + s + ' is between ' + loS + ' and ' + hiS + '. It rounds to ' + r + '.">'""", """aria-label="' + s + ' está entre ' + loS + ' y ' + hiS + '. Se redondea a ' + r + '.">'""")
R('"halfway", 15, "#757575", 400)', '"la mitad", 15, "#757575", 400)')
R("""out.innerHTML = '<div class="linea">The neighbor on the right is <strong>' + vec + '</strong>: ' + (+vec >= 5 ? "5 or more, so the digit goes up by one." : "4 or less, so the digit stays the same.") +
    ' The digits on the right are dropped.</div><div class="linea veredicto">' + s + ' rounded to ' + LUGR[k] + ' ≈ ' + r + '</div>';""",
  """out.innerHTML = '<div class="linea">El vecino de la derecha es <strong>' + vec + '</strong>: ' + (+vec >= 5 ? "5 o más, así que el dígito sube uno." : "4 o menos, así que el dígito se queda igual.") +
    ' Los dígitos de la derecha se eliminan.</div><div class="linea veredicto">' + s + ' redondeado ' + LUGR[k] + ' ≈ ' + r + '</div>';""")
R('var enun = (dinero ? "A calculator shows a price of <strong>$" + s + "</strong>. Round it to the cent (the nearest hundredth)." : "Round <strong>" + s + "</strong> to " + LUGR[k] + ".");',
  'var enun = (dinero ? "Una calculadora muestra un precio de <strong>$" + s + "</strong>. Redondéelo al centavo (a la centésima más cercana)." : "Redondee <strong>" + s + "</strong> " + LUGR[k] + ".");')
R('solucion: "The neighbor on the right is " + vec + (+vec >= 5 ? " (5 or more), so the digit goes up" : " (4 or less), so the digit stays the same") + ", and the rest is dropped: <strong>" + (dinero ? "$" : "") + r + "</strong>.",',
  'solucion: "El vecino de la derecha es " + vec + (+vec >= 5 ? " (5 o más), así que el dígito sube" : " (4 o menos), así que el dígito se queda igual") + ", y lo demás se elimina: <strong>" + (dinero ? "$" : "") + r + "</strong>.",')
R('return { estado: "invalido", msg: "Type the number with digits and a decimal point, for example 5.3." };', 'return { estado: "invalido", msg: "Escriba el número con cifras y punto decimal, por ejemplo 5.3." };')
R('msg: "The value is right, but you kept too many digits. When you round to " + LUGR[k] + ", keep " + (k === 0 ? "no digits" : k === 1 ? "one digit" : "two digits") + " after the point." };',
  'msg: "El valor está bien, pero dejó demasiados dígitos. Al redondear " + LUGR[k] + ", " + (k === 0 ? "no deje ningún dígito" : k === 1 ? "deje un dígito" : "deje dos dígitos") + " después del punto." };')
R('msg: "Check the neighbor on the right: with 5 or more the digit goes up; with 4 or less it stays the same." };', 'msg: "Revise el vecino de la derecha: con 5 o más el dígito sube; con 4 o menos se queda igual." };')
R('msg: "Round to " + LUGR[k] + ": keep " + (k === 0 ? "no digits" : k === 1 ? "one digit" : "two digits") + " after the point." };', 'msg: "Redondee " + LUGR[k] + ": " + (k === 0 ? "no deje ningún dígito" : k === 1 ? "deje un dígito" : "deje dos dígitos") + " después del punto." };')
R('msg: "Find the place you are rounding to, then look only at its neighbor on the right." };', 'msg: "Busque el lugar al que redondea y mire solo su vecino de la derecha." };')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-3-1.html")
