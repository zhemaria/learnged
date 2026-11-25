"""Crea es/matematicas/nivel-1/practica-4-1-mcd-mcm.html a partir de math/level-1/practice-4-1-gcf-lcm.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-4-1-gcf-lcm.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Complemento de la Lección 4.1 · MCD y MCM — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
import re
t.s = re.sub(r"<title>[^<]*</title>", "<title>Práctica · Complemento de la Lección 4.1 · Factores, múltiplos, MCD y MCM · LearnGED</title>", t.s, count=1)
R('<div class="ruta">Level 1 · Topic 4 · Fractions · Complement to Lesson 4.1</div>', '<div class="ruta">Nivel 1 · Tema 4 · Fracciones · Complemento de la Lección 4.1</div>')
R("<h1>Factors, multiples, GCF, and LCM</h1>", "<h1>Factores, múltiplos, MCD y MCM</h1>")
R("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#factors">Factors and multiples</a></li>', '<li><a href="#factores">Factores y múltiplos</a></li>')
R('<li><a href="#primes">Prime numbers and prime factorization</a></li>', '<li><a href="#primos">Números primos y factorización prima</a></li>')
R('<li><a href="#gcf">The greatest common factor (GCF)</a></li>', '<li><a href="#mcd">El máximo común divisor (MCD)</a></li>')
R('<li><a href="#lcm">The least common multiple (LCM)</a></li>', '<li><a href="#mcm">El mínimo común múltiplo (MCM)</a></li>')
R('<li><a href="#which">GCF or LCM?</a></li>', '<li><a href="#cual">¿MCD o MCM?</a></li>')
# 1
R('id="factors" open>', 'id="factores" open>'); R("<h2>Factors and multiples</h2>", "<h2>Factores y múltiplos</h2>")
R("<p>Factors <strong>divide</strong> the number evenly; find them <strong>in pairs</strong>. Multiples come from <strong>multiplying</strong> the number by 1, 2, 3…</p>", "<p>Los factores <strong>dividen</strong> el número exactamente; hállelos <strong>en parejas</strong>. Los múltiplos salen de <strong>multiplicar</strong> el número por 1, 2, 3…</p>")
R("<h3>Find the factors and the multiples</h3>", "<h3>Halle los factores y los múltiplos</h3>")
R('<label for="fm-n">Number (2 to 200)</label>', '<label for="fm-n">Número (del 2 al 200)</label>')
R("<h3>Practice: which one is not a factor?</h3>", "<h3>Practique: ¿cuál no es factor?</h3>")
# 2
R('id="primes">', 'id="primos">'); R("<h2>Prime numbers and prime factorization</h2>", "<h2>Números primos y factorización prima</h2>")
R("""<p>A <strong>prime</strong> has exactly two factors: 1 and itself. To write the <strong>prime factorization</strong>, divide by the smallest prime that
      works, again and again, until you reach 1. Then check by multiplying.</p>""", """<p>Un <strong>primo</strong> tiene exactamente dos factores: el 1 y él mismo. Para escribir la <strong>factorización prima</strong>, divida entre el primo más pequeño que
      sirva, una y otra vez, hasta llegar a 1. Después compruebe multiplicando.</p>""")
R("<h3>Break a number into primes</h3>", "<h3>Descomponga un número en primos</h3>")
R('<label for="pf-n">Number (2 to 1,000)</label>', '<label for="pf-n">Número (del 2 al 1,000)</label>')
R("<h3>Practice: prime or composite?</h3>", "<h3>Practique: ¿primo o compuesto?</h3>")
R("<h3>Practice: which is the prime factorization?</h3>", "<h3>Practique: ¿cuál es la factorización prima?</h3>")
# 3
R('id="gcf">', 'id="mcd">'); R("<h2>The greatest common factor (GCF)</h2>", "<h2>El máximo común divisor (MCD)</h2>")
R("<p>List the factors of both numbers and take the <strong>greatest one they share</strong>. Or use primes: take the primes they share, each with its smaller exponent.</p>", "<p>Haga la lista de los factores de los dos números y tome el <strong>mayor que tienen en común</strong>. O use primos: tome los primos comunes, cada uno con su exponente menor.</p>")
R("<h3>GCF and LCM, step by step</h3>", "<h3>MCD y MCM, paso a paso</h3>")
R('<label for="gl-a">First number</label>', '<label for="gl-a">Primer número</label>')
R('<label for="gl-b">Second number</label>', '<label for="gl-b">Segundo número</label>')
R("<h3>Practice: find the GCF</h3>", "<h3>Practique: halle el MCD</h3>")
R('<label for="p4-r">GCF</label>', '<label for="p4-r">MCD</label>')
# 4
R('id="lcm">', 'id="mcm">'); R("<h2>The least common multiple (LCM)</h2>", "<h2>El mínimo común múltiplo (MCM)</h2>")
R("""<p>List the multiples of both numbers and take the <strong>first one they share</strong>. Or use primes: take every prime that shows up, each with its greater exponent.
      Shortcut: LCM = (first × second) ÷ GCF. The step-by-step tool is in <a href="#gcf">section 3</a>.</p>""",
  """<p>Haga la lista de los múltiplos de los dos números y tome el <strong>primero que tienen en común</strong>. O use primos: tome todos los primos que aparecen, cada uno con su exponente mayor.
      Atajo: MCM = (primero × segundo) ÷ MCD. La herramienta paso a paso está en la <a href="#mcd">sección 3</a>.</p>""")
R("<h3>Practice: find the LCM</h3>", "<h3>Practique: halle el MCM</h3>")
R('<label for="p5-r">LCM</label>', '<label for="p5-r">MCM</label>')
R('<p>Use the shortcut: type <span class="tecla">(</span> first number <span class="tecla">×</span> second number <span class="tecla">)</span> <span class="tecla">÷</span> GCF <span class="tecla">enter</span>.</p>',
  '<p>Use el atajo: escriba <span class="tecla">(</span> primer número <span class="tecla">×</span> segundo número <span class="tecla">)</span> <span class="tecla">÷</span> MCD <span class="tecla">enter</span>.</p>')
# 5
R('id="which">', 'id="cual">'); R("<h2>GCF or LCM?</h2>", "<h2>¿MCD o MCM?</h2>")
R("<p><strong>GCF:</strong> sharing or cutting into equal groups, as large as possible, with nothing left over. <strong>LCM:</strong> things that repeat, and when they happen together again.</p>", "<p><strong>MCD:</strong> repartir o cortar en grupos iguales, lo más grandes posible, sin que sobre nada. <strong>MCM:</strong> cosas que se repiten, y cuándo vuelven a coincidir.</p>")
R("<h3>Practice: solve the problem</h3>", "<h3>Practique: resuelva el problema</h3>")
R("<p><strong>Level 1 · Topic 4 · Fractions · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 4 · Fracciones · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Number helpers ============ */", "/* ============ Utilidades de números ============ */")
R("/* ============ MODULE 1 · factors and multiples ============ */", "/* ============ MÓDULO 1 · factores y múltiplos ============ */")
R('out.innerHTML = "Type a whole number from 2 to 200."; return; }', 'out.innerHTML = "Escriba un número entero del 2 al 200."; return; }')
R("""'<div class="linea">Factor pairs: '""", """'<div class="linea">Parejas de factores: '""")
R("""'<div class="linea veredicto">Factors of ' + n + ': '""", """'<div class="linea veredicto">Factores de ' + n + ': '""")
R("""(esPrimo(n) ? n + ' has exactly two factors: it is <strong>prime</strong>.' : n + ' has ' + factores(n).length + ' factors: it is <strong>composite</strong>.')""", """(esPrimo(n) ? n + ' tiene exactamente dos factores: es <strong>primo</strong>.' : n + ' tiene ' + factores(n).length + ' factores: es <strong>compuesto</strong>.')""")
R("""'<div class="linea">Multiples of ' + n + ': ' + mult.map(com).join(", ") + '… (they never end)</div>'""", """'<div class="linea">Múltiplos de ' + n + ': ' + mult.map(com).join(", ") + '… (no se acaban nunca)</div>'""")
R('pistas["k" + x] = n + " ÷ " + x + " = " + (n / x) + " with no remainder, so " + x + " is a factor.";', 'pistas["k" + x] = n + " ÷ " + x + " = " + (n / x) + " sin residuo, así que " + x + " es factor.";')
R('return { enun: "Which of these numbers is <strong>not</strong> a factor of " + n + "?",', 'return { enun: "¿Cuál de estos números <strong>no</strong> es factor de " + n + "?",')
R('bien: n + " ÷ " + malo + " leaves a remainder of " + (n % malo) + ". The factors of " + n + " are " + factores(n).join(", ") + ".",', 'bien: n + " ÷ " + malo + " deja un residuo de " + (n % malo) + ". Los factores de " + n + " son " + factores(n).join(", ") + ".",')
R('mal: "The factors of " + n + " are " + factores(n).join(", ") + ". " + malo + " is not on the list: " + n + " ÷ " + malo + " leaves a remainder of " + (n % malo) + "." };', 'mal: "Los factores de " + n + " son " + factores(n).join(", ") + ". " + malo + " no está en la lista: " + n + " ÷ " + malo + " deja un residuo de " + (n % malo) + "." };')
R("/* ============ MODULE 2 · primes ============ */", "/* ============ MÓDULO 2 · primos ============ */")
R('out.innerHTML = "Type a whole number from 2 to 1,000."; return; }', 'out.innerHTML = "Escriba un número entero del 2 al 1,000."; return; }')
R("""' is prime: its only factors are 1 and ' + n + '.</div>'""", """' es primo: sus únicos factores son 1 y ' + n + '.</div>'""")
R("""'<div class="linea">Divide by the smallest prime that works, again and again:</div>'""", """'<div class="linea">Divida entre el primo más pequeño que sirva, una y otra vez:</div>'""")
R("""'</div><div class="linea">Check: ' + p.join(" × ")""", """'</div><div class="linea">Comprobación: ' + p.join(" × ")""")
R('var por = p ? n + " has exactly two factors, 1 and " + n + ": it is prime." : n + " has more than two factors (" + f.join(", ") + "): it is composite.";', 'var por = p ? n + " tiene exactamente dos factores, 1 y " + n + ": es primo." : n + " tiene más de dos factores (" + f.join(", ") + "): es compuesto.";')
R('enun: "Is <strong>" + n + "</strong> prime or composite?", opciones: [{ html: "Prime", clave: "p" }, { html: "Composite", clave: "c" }],', 'enun: "¿<strong>" + n + "</strong> es primo o compuesto?", opciones: [{ html: "Primo", clave: "p" }, { html: "Compuesto", clave: "c" }],')
R('pistas[o] = prod !== n ? "Multiply to check: " + o + " = " + prod + ", not " + n + "." : "Not every number in it is prime: " + nums.filter(function(v){ return !esPrimo(v); }).join(", ") + " can still be broken down."; } });',
  'pistas[o] = prod !== n ? "Multiplique para comprobar: " + o + " = " + prod + ", no " + n + "." : "No todos los números son primos: " + nums.filter(function(v){ return !esPrimo(v); }).join(", ") + " todavía se puede descomponer."; } });')
R('return { enun: "What is the prime factorization of <strong>" + n + "</strong>?",', 'return { enun: "¿Cuál es la factorización prima de <strong>" + n + "</strong>?",')
R('bien: "Only primes, and " + ok + " = " + n + ".", mal: n + " = " + ok + (p.length > 2 ? " = " + conExp(p) : "") + ". Every number in it is prime." };', 'bien: "Solo primos, y " + ok + " = " + n + ".", mal: n + " = " + ok + (p.length > 2 ? " = " + conExp(p) : "") + ". Todos sus números son primos." };')
R("/* ============ MODULE 3 and 4 · GCF and LCM ============ */", "/* ============ MÓDULOS 3 y 4 · MCD y MCM ============ */")
R('out.innerHTML = "Type two whole numbers from 2 to 500."; return; }', 'out.innerHTML = "Escriba dos números enteros del 2 al 500."; return; }')
R("""out.innerHTML = '<div class="linea"><strong>GCF · Method 1:</strong> factors of ' + a + ': ' + fa.join(", ") + '. Factors of ' + b + ': ' + fb.join(", ") + '. Common: ' + com_.join(", ") + '.</div>' +
    '<div class="linea"><strong>GCF · Method 2:</strong> ' + a + ' = ' + (primos(a).length > 1 ? conExp(primos(a)) : a) + ' and ' + b + ' = ' + (primos(b).length > 1 ? conExp(primos(b)) : b) + '. Shared primes, smaller exponent: ' + gp + '.</div>' +
    '<div class="linea veredicto">GCF(' + a + ', ' + b + ') = ' + g + '</div>' +
    '<div class="linea"><strong>LCM · Method 1:</strong> multiples of ' + a + ': ' + ma.map(com).join(", ") + '… Multiples of ' + b + ': ' + mb.map(com).join(", ") + '…</div>' +
    '<div class="linea"><strong>LCM · Method 2:</strong> every prime, greater exponent: ' + lp + '. <strong>Shortcut:</strong> (' + a + ' × ' + b + ') ÷ ' + g + ' = ' + com(l) + '.</div>' +
    '<div class="linea veredicto">LCM(' + a + ', ' + b + ') = ' + com(l) + '</div>';""",
  """out.innerHTML = '<div class="linea"><strong>MCD · Método 1:</strong> factores de ' + a + ': ' + fa.join(", ") + '. Factores de ' + b + ': ' + fb.join(", ") + '. Comunes: ' + com_.join(", ") + '.</div>' +
    '<div class="linea"><strong>MCD · Método 2:</strong> ' + a + ' = ' + (primos(a).length > 1 ? conExp(primos(a)) : a) + ' y ' + b + ' = ' + (primos(b).length > 1 ? conExp(primos(b)) : b) + '. Primos comunes, exponente menor: ' + gp + '.</div>' +
    '<div class="linea veredicto">MCD(' + a + ', ' + b + ') = ' + g + '</div>' +
    '<div class="linea"><strong>MCM · Método 1:</strong> múltiplos de ' + a + ': ' + ma.map(com).join(", ") + '… Múltiplos de ' + b + ': ' + mb.map(com).join(", ") + '…</div>' +
    '<div class="linea"><strong>MCM · Método 2:</strong> todos los primos, exponente mayor: ' + lp + '. <strong>Atajo:</strong> (' + a + ' × ' + b + ') ÷ ' + g + ' = ' + com(l) + '.</div>' +
    '<div class="linea veredicto">MCM(' + a + ', ' + b + ') = ' + com(l) + '</div>';""")
R('var pistas = [{ v: l, msg: "That is a common multiple. The GCF is a common factor: it cannot be greater than the numbers." }];', 'var pistas = [{ v: l, msg: "Ese es un múltiplo común. El MCD es un factor común: no puede ser mayor que los números." }];')
R('return { enun: "Find the greatest common factor of <strong>" + a + "</strong> and <strong>" + b + "</strong>.",', 'return { enun: "Halle el máximo común divisor de <strong>" + a + "</strong> y <strong>" + b + "</strong>.",')
R('solucion: "Factors of " + a + ": " + factores(a).join(", ") + ". Factors of " + b + ": " + factores(b).join(", ") + ". The greatest common factor is <strong>" + g + "</strong>.",', 'solucion: "Factores de " + a + ": " + factores(a).join(", ") + ". Factores de " + b + ": " + factores(b).join(", ") + ". El máximo común divisor es <strong>" + g + "</strong>.",')
R('var v = leeNum(t); if (v === null) return { estado: "invalido", msg: "Type a whole number." };', 'var v = leeNum(t); if (v === null) return { estado: "invalido", msg: "Escriba un número entero." };', 2)
R('if (a % v === 0 && b % v === 0) return { estado: "mal", msg: v + " is a common factor, but there is a greater one." };', 'if (a % v === 0 && b % v === 0) return { estado: "mal", msg: v + " es un factor común, pero hay uno mayor." };')
R('return { estado: "mal", msg: v + " does not divide both numbers. List the factors of each and look for the greatest one they share." };', 'return { estado: "mal", msg: v + " no divide a los dos números. Haga la lista de los factores de cada uno y busque el mayor que tienen en común." };')
R('return { enun: "Find the least common multiple of <strong>" + a + "</strong> and <strong>" + b + "</strong>.",', 'return { enun: "Halle el mínimo común múltiplo de <strong>" + a + "</strong> y <strong>" + b + "</strong>.",')
R('solucion: "Multiples of " + Math.max(a, b) + ": "', 'solucion: "Múltiplos de " + Math.max(a, b) + ": "')
R('"… The first one that is also a multiple of " + Math.min(a, b) + " is <strong>" + l + "</strong>. Shortcut: ("', '"… El primero que también es múltiplo de " + Math.min(a, b) + " es <strong>" + l + "</strong>. Atajo: ("')
R('msg: "That is the GCF, a common factor. The LCM is a common multiple: it cannot be smaller than the numbers." };', 'msg: "Ese es el MCD, un factor común. El MCM es un múltiplo común: no puede ser menor que los números." };')
R('msg: v + " is a common multiple, but there is a smaller one." };', 'msg: v + " es un múltiplo común, pero hay uno menor." };')
R('msg: v + " is not a multiple of both numbers. List the multiples of the greater number until one is also a multiple of the smaller." };', 'msg: v + " no es múltiplo de los dos números. Haga la lista de los múltiplos del número mayor hasta que uno sea también múltiplo del menor." };')
R("/* ============ MODULE 5 · GCF or LCM? ============ */", "/* ============ MÓDULO 5 · ¿MCD o MCM? ============ */")
R('enun = "A food pantry has " + a + " cans of beans and " + b + " cans of corn. It wants identical bags with no cans left over. <strong>What is the greatest number of bags it can make?</strong>"; gcf = true; }',
  'enun = "Un banco de comida tiene " + a + " latas de frijoles y " + b + " latas de maíz. Quiere bolsas idénticas sin que sobre ninguna lata. <strong>¿Cuál es el mayor número de bolsas que puede hacer?</strong>"; gcf = true; }')
R('enun = "You have two ribbons, " + a + " inches and " + b + " inches long. You cut them into equal pieces, as long as possible, with nothing left over. <strong>How long is each piece, in inches?</strong>"; gcf = true; }',
  'enun = "Tiene dos cintas, de " + a + " pulgadas y de " + b + " pulgadas. Las corta en pedazos iguales, lo más largos posible, sin que sobre nada. <strong>¿Cuántas pulgadas mide cada pedazo?</strong>"; gcf = true; }')
R('enun = "One bus stops every " + a + " minutes and another every " + b + " minutes. They stop together at 8:00. <strong>In how many minutes will they stop together again?</strong>"; gcf = false; }',
  'enun = "Un autobús para cada " + a + " minutos y otro cada " + b + " minutos. Paran juntos a las 8:00. <strong>¿En cuántos minutos volverán a parar juntos?</strong>"; gcf = false; }')
R('enun = "One light blinks every " + a + " seconds and another every " + b + " seconds. They blink together now. <strong>In how many seconds will they blink together again?</strong>"; gcf = false; }',
  'enun = "Una luz parpadea cada " + a + " segundos y otra cada " + b + " segundos. Ahora parpadean juntas. <strong>¿En cuántos segundos volverán a parpadear juntas?</strong>"; gcf = false; }')
R('pistas["k" + otro] = gcf ? "This problem shares into equal groups with nothing left over: it asks for the GCF, not the LCM." : "Things repeat and meet again: this problem asks for the LCM, not the GCF.";', 'pistas["k" + otro] = gcf ? "Este problema reparte en grupos iguales sin que sobre nada: pide el MCD, no el MCM." : "Las cosas se repiten y vuelven a coincidir: este problema pide el MCM, no el MCD.";')
R('pistas["k" + (a * b)] = gcf ? "Multiplying the numbers gives a common multiple. Is this a sharing problem or a repeating problem?" : "The product is a common multiple, but is it the least one?";', 'pistas["k" + (a * b)] = gcf ? "Multiplicar los números da un múltiplo común. ¿Es un problema de repartir o de cosas que se repiten?" : "El producto es un múltiplo común, pero ¿es el menor?";')
R('pistas["k" + (a + b)] = "Adding the numbers does not answer this kind of problem. Decide first: GCF or LCM?";', 'pistas["k" + (a + b)] = "Sumar los números no responde este tipo de problema. Decida primero: ¿MCD o MCM?";')
R('pista: "Decide first: is this sharing into equal groups (GCF) or things that repeat (LCM)?",', 'pista: "Decida primero: ¿es repartir en grupos iguales (MCD) o cosas que se repiten (MCM)?",')
R('bien: (gcf ? "Sharing into equal groups: GCF(" : "Repeating and meeting again: LCM(")', 'bien: (gcf ? "Repartir en grupos iguales: MCD(" : "Repetirse y volver a coincidir: MCM(")')
R('mal: (gcf ? "Sharing into equal groups, as large as possible, asks for the GCF. GCF(" : "Things that repeat and meet again ask for the LCM. LCM(")', 'mal: (gcf ? "Repartir en grupos iguales, lo más grandes posible, pide el MCD. MCD(" : "Las cosas que se repiten y vuelven a coincidir piden el MCM. MCM(")')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-4-1-mcd-mcm.html")
