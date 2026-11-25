"""Crea es/matematicas/nivel-1/practica-5-1.html a partir de math/level-1/practice-5-1.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-5-1.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 5.1 · Patrones numéricos y de figuras — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 5.1 · Number and shape patterns · LearnGED</title>", "<title>Práctica · Lección 5.1 · Patrones numéricos y de figuras · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 5 · Patterns and algebraic thinking</div>', '<div class="ruta">Nivel 1 · Tema 5 · Patrones y pensamiento algebraico</div>')
R("<h1>Lesson 5.1 · Number and shape patterns</h1>", "<h1>Lección 5.1 · Patrones numéricos y de figuras</h1>")
R("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otro intento.")
R('<li><a href="#number-patterns">Number patterns</a></li>', '<li><a href="#patrones-numericos">Patrones numéricos</a></li>')
R('<li><a href="#shape-patterns">Shape patterns</a></li>', '<li><a href="#patrones-figuras">Patrones de figuras</a></li>')
R('<li><a href="#input-output">Input-output tables</a></li>', '<li><a href="#entrada-salida">Tablas de entrada y salida</a></li>')
# 1
R('id="number-patterns" open>', 'id="patrones-numericos" open>'); R("<h2>Number patterns</h2>", "<h2>Patrones numéricos</h2>")
R("""<p>A <strong>pattern</strong> is a list of numbers that follows a <strong>rule</strong>. Each number is a <strong>term</strong>.
      To find the rule, look at what changes from one term to the next. If the numbers grow slowly and evenly, the rule is usually
      to add. If they grow very fast (they double or triple), the rule is usually to multiply.</p>""",
  """<p>Un <strong>patrón</strong> es una lista de números que sigue una <strong>regla</strong>. Cada número es un <strong>término</strong>.
      Para descubrir la regla, fíjese en qué cambia de un término al siguiente. Si los números crecen despacio y parejo, la regla casi siempre
      es sumar. Si crecen muy rápido (se duplican o se triplican), la regla casi siempre es multiplicar.</p>""")
R("<h3>Build your own pattern</h3>", "<h3>Forme su propio patrón</h3>")
R('<label for="pn-i">First term: ', '<label for="pn-i">Primer término: ')
R('<label for="pn-o">Rule</label><select id="pn-o"><option value="+">add</option><option value="-">subtract</option><option value="x">multiply by</option></select>', '<label for="pn-o">Regla</label><select id="pn-o"><option value="+">sumar</option><option value="-">restar</option><option value="x">multiplicar por</option></select>')
R('<label for="pn-k">Amount: ', '<label for="pn-k">Cantidad: ')
R('<p class="nota">Move the sliders and change the rule. Notice how adding makes the numbers grow evenly, and multiplying makes them grow very fast.</p>', '<p class="nota">Mueva los deslizadores y cambie la regla. Fíjese en que al sumar los números crecen parejo, y al multiplicar crecen muy rápido.</p>')
R("<h3>Practice: what comes next, or what is missing?</h3>", "<h3>Practique: ¿qué sigue o qué falta?</h3>")
# 2
R('id="shape-patterns">', 'id="patrones-figuras">'); R("<h2>Shape patterns</h2>", "<h2>Patrones de figuras</h2>")
R("""<p>Shapes can follow rules too. The trick: <strong>count something</strong> (squares, dots, sticks) and write the numbers.
      The shape pattern becomes a number pattern, and you already know how to find its rule.</p>""",
  """<p>Las figuras también pueden seguir reglas. El truco: <strong>cuente algo</strong> (cuadritos, puntos, palitos) y escriba los números.
      El patrón de figuras se vuelve un patrón numérico, y usted ya sabe descubrir su regla.</p>""")
R("<h3>Growing shapes</h3>", "<h3>Figuras que crecen</h3>")
R('<label for="pf-t">Pattern</label><select id="pf-t"><option value="0">Growing squares</option><option value="1">Rows of 3 dots</option><option value="2">L shapes</option><option value="3">Staircases</option></select>', '<label for="pf-t">Patrón</label><select id="pf-t"><option value="0">Cuadrados que crecen</option><option value="1">Filas de 3 puntos</option><option value="2">Figuras en L</option><option value="3">Escaleras</option></select>')
R("<h3>Practice: how many will it have?</h3>", "<h3>Practique: ¿cuántos tendrá?</h3>")
R('<label for="p2-r">How many</label>', '<label for="p2-r">Cuántos</label>')
# 3
R('id="input-output">', 'id="entrada-salida">'); R("<h2>Input-output tables</h2>", "<h2>Tablas de entrada y salida</h2>")
R("""<p>The <strong>input</strong> is the number you put into the "machine." The <strong>output</strong> is the number that comes out
      after the machine uses its rule. The rule connects <strong>each input with its own output</strong>: do not compare one row with
      the next one.</p>""",
  """<p>La <strong>entrada</strong> es el número que se mete en la «máquina». La <strong>salida</strong> es el número que sale
      después de que la máquina usa su regla. La regla une <strong>cada entrada con su propia salida</strong>: no compare una fila con
      la siguiente.</p>""")
R("<h3>The rule machine</h3>", "<h3>La máquina de reglas</h3>")
R("<p>The machine has a hidden rule. Type an input and see what comes out. Try several inputs, then guess the rule.</p>", "<p>La máquina tiene una regla escondida. Escriba una entrada y vea qué sale. Pruebe varias entradas y después adivine la regla.</p>")
R('<label for="mq-e" class="sr-only">Input</label>', '<label for="mq-e" class="sr-only">Entrada</label>')
R('<span class="caja" id="mq-caja">rule ?</span>', '<span class="caja" id="mq-caja">regla ?</span>')
R('id="mq-ok">Put it in the machine</button>', 'id="mq-ok">Meter en la máquina</button>')
R('id="mq-ver">Show the rule</button>', 'id="mq-ver">Mostrar la regla</button>')
R('id="mq-nueva">New machine</button>', 'id="mq-nueva">Otra máquina</button>')
R("<h3>Practice: what is the rule?</h3>", "<h3>Practique: ¿cuál es la regla?</h3>")
R("<h3>Practice: find the output</h3>", "<h3>Practique: halle la salida</h3>")
R('<label for="p4-r">Output</label>', '<label for="p4-r">Salida</label>')
R("<p><strong>Level 1 · Topic 5 · Patterns and algebraic thinking · LearnGED</strong><br>", "<p><strong>Nivel 1 · Tema 5 · Patrones y pensamiento algebraico · LearnGED</strong><br>")
# ---------- Script ----------
R("/* ============ Helpers ============ */", "/* ============ Utilidades ============ */")
R('function reglaTxt(o, k){ return (o === "x" ? "multiply by " : (o === "+" ? "add " : "subtract ")) + k; }', 'function reglaTxt(o, k){ return (o === "x" ? "multiplicar por " : (o === "+" ? "sumar " : "restar ")) + k; }')
R("/* sequence chain: terms t, jump label s, position of the missing term (or -1) */", "/* cadena de la sucesión: términos t, etiqueta del salto s, posición del término que falta (o -1) */")
R("/* ============ MODULE 1 · number patterns ============ */", "/* ============ MÓDULO 1 · patrones numéricos ============ */")
R("""'<span class="sr-only">Pattern: ' + t.join(", ") + '. Rule: ' + reglaTxt(o, k) + ' each time.</span>'""", """'<span class="sr-only">Patrón: ' + t.join(", ") + '. Regla: ' + reglaTxt(o, k) + ' cada vez.</span>'""")
R('agrega(base + k, "The numbers grow very fast, so the rule multiplies; it does not add. Divide one term by the one before it.");', 'agrega(base + k, "Los números crecen muy rápido, así que la regla multiplica; no suma. Divida un término entre el anterior.");')
R('agrega(aplica(o, k, cor), enMedio ? "That number is one jump too far. The missing term comes right after " + com(base) + "." : "That is two jumps after " + com(base) + ". You only need one.");',
  'agrega(aplica(o, k, cor), enMedio ? "Ese número está un salto más allá. El término que falta viene justo después de " + com(base) + "." : "Eso son dos saltos después de " + com(base) + ". Solo necesita uno.");')
R('agrega(base * (k + 1), "Check the rule: each term is " + k + " times the one before it.");', 'agrega(base * (k + 1), "Revise la regla: cada término es " + k + " veces el anterior.");')
R('agrega(cor + dir * k, enMedio ? "That number is one jump too far. The missing term comes right after " + com(base) + "." : "That is two jumps after " + com(base) + ". You only need one.");',
  'agrega(cor + dir * k, enMedio ? "Ese número está un salto más allá. El término que falta viene justo después de " + com(base) + "." : "Eso son dos saltos después de " + com(base) + ". Solo necesita uno.");')
R('agrega(cor + dir, "Check the size of the jump: it is " + k + " every time, not " + (k + 1) + " or " + (k - 1) + ".");', 'agrega(cor + dir, "Revise el tamaño del salto: es " + k + " cada vez, no " + (k + 1) + " ni " + (k - 1) + ".");')
R('agrega(base - dir * k, o === "+" ? "The numbers go up, so the rule adds. You subtracted." : "The numbers go down, so the rule subtracts. You added.");', 'agrega(base - dir * k, o === "+" ? "Los números suben, así que la regla suma. Usted restó." : "Los números bajan, así que la regla resta. Usted sumó.");')
R('"Find the jump first: compare two terms that are next to each other."); extra++; }', '"Busque primero el salto: compare dos términos que estén uno al lado del otro."); extra++; }')
R('enun: (pos === 4 ? "What number comes next in the pattern " : "What number is missing in the pattern ") + "<strong>" + txt + "</strong>?",', 'enun: (pos === 4 ? "¿Qué número sigue en el patrón " : "¿Qué número falta en el patrón ") + "<strong>" + txt + "</strong>?",')
R('pista: "Find the jump: compare two terms that are next to each other.",', 'pista: "Busque el salto: compare dos términos que estén uno al lado del otro.",')
R('bien: "The rule is " + regla + " each time: " + todos + ".",', 'bien: "La regla es " + regla + " cada vez: " + todos + ".",')
R('mal: "From one term to the next, you " + regla + ": "', 'mal: "De un término al siguiente, hay que " + regla + ": "')
R('". The whole pattern is " + todos + "."', '". El patrón completo es " + todos + "."')
R("/* ============ MODULE 2 · shape patterns ============ */", "/* ============ MÓDULO 2 · patrones de figuras ============ */")
R('{ nom: "squares", f: function(n){ return n * n; }, regla: "figure n is a square with n rows of n squares (n × n)"', '{ nom: "cuadritos", f: function(n){ return n * n; }, regla: "la figura n es un cuadrado con n filas de n cuadritos (n × n)"')
R('{ nom: "dots", f: function(n){ return 3 * n; }, regla: "each figure adds 3 dots (one more row of 3)"', '{ nom: "puntos", f: function(n){ return 3 * n; }, regla: "cada figura agrega 3 puntos (una fila más de 3)"')
R('{ nom: "squares", f: function(n){ return 2 * n + 1; }, regla: "each figure adds 2 squares (one on each arm of the L)"', '{ nom: "cuadritos", f: function(n){ return 2 * n + 1; }, regla: "cada figura agrega 2 cuadritos (uno en cada brazo de la L)"')
R('{ nom: "squares", f: function(n){ return n * (n + 1) / 2; }, regla: "each new step has one more square than the step before it (+2, +3, +4, …)"', '{ nom: "cuadritos", f: function(n){ return n * (n + 1) / 2; }, regla: "cada escalón nuevo tiene un cuadrito más que el anterior (+2, +3, +4, …)"')
R('punto = P.nom === "dots";', 'punto = P.nom === "puntos";')
R('var voz = "Figures " + n0 + " to " + n1 + " of the pattern, with "', 'var voz = "Figuras " + n0 + " a " + n1 + " del patrón, con "')
R('"Figure " + d.n, 17, "#222")', '"Figura " + d.n, 17, "#222")')
R("""$("pf-salida").innerHTML = '<div class="linea">Count the ' + P.nom + ': ' + vals.join(", ") + ', …</div><div class="linea">Rule: ' + P.regla + '.</div><div class="linea veredicto">Figure 5: ' + P.f(5) + ' · Figure 10: ' + P.f(10) + '</div>';""",
  """$("pf-salida").innerHTML = '<div class="linea">Cuente los ' + P.nom + ': ' + vals.join(", ") + ', …</div><div class="linea">Regla: ' + P.regla + '.</div><div class="linea veredicto">Figura 5: ' + P.f(5) + ' · Figura 10: ' + P.f(10) + '</div>';""")
R('msg: "Check whether the jump from one figure to the next is always the same. Write the next few numbers one by one." });', 'msg: "Revise si el salto de una figura a la siguiente es siempre el mismo. Escriba los números siguientes uno por uno." });')
R('msg: "That is figure 5. Keep going, one figure at a time, until figure " + n + "." });', 'msg: "Esa es la figura 5. Siga, figura por figura, hasta la figura " + n + "." });')
R('msg: "Doubling figure " + (n / 2) + " does not work here. Go figure by figure: find the rule and use it." });', 'msg: "Duplicar la figura " + (n / 2) + " no sirve aquí. Vaya figura por figura: descubra la regla y úsela." });')
R('enun: "A shape pattern has " + vals.join(", ") + " " + P.nom + " in figures 1 to 4. How many " + P.nom + " will <strong>figure " + n + "</strong> have?"', 'enun: "Un patrón de figuras tiene " + vals.join(", ") + " " + P.nom + " en las figuras 1 a 4. ¿Cuántos " + P.nom + " tendrá la <strong>figura " + n + "</strong>?"')
R('solucion: "Rule: " + P.regla + ". Figures 1 to " + n + ": " + serie.join(", ") + ". Answer: <strong>" + r + "</strong>.",', 'solucion: "Regla: " + P.regla + ". Figuras 1 a " + n + ": " + serie.join(", ") + ". Respuesta: <strong>" + r + "</strong>.",')
R('"Write the numbers figure by figure until you reach figure " + n + "."', '"Escriba los números figura por figura hasta llegar a la figura " + n + "."')
R("/* ============ MODULE 3 · input-output tables ============ */", "/* ============ MÓDULO 3 · tablas de entrada y salida ============ */")
R('$("mq-caja").textContent = "rule ?";', '$("mq-caja").textContent = "regla ?";')
R('$("mq-s").textContent = "Type a whole number from 0 to 999."; return; }', '$("mq-s").textContent = "Escriba un número entero del 0 al 999."; return; }')
R('$("mq-s").textContent = "Try a bigger number."; return; }', '$("mq-s").textContent = "Pruebe un número más grande."; return; }')
R('$("mq-s").textContent = "output: " + com(s);', '$("mq-s").textContent = "salida: " + com(s);')
R("""'<table class="comparar"><caption>What came out of the machine</caption><thead><tr><th scope="col">Input</th><th scope="col">Output</th></tr></thead><tbody>'""", """'<table class="comparar"><caption>Lo que salió de la máquina</caption><thead><tr><th scope="col">Entrada</th><th scope="col">Salida</th></tr></thead><tbody>'""")
R('$("mq-caja").textContent = "input " + sim(MQ.o) + " " + MQ.k;', '$("mq-caja").textContent = "entrada " + sim(MQ.o) + " " + MQ.k;')
R("""'<table class="comparar"><caption>Input-output table</caption><thead><tr><th scope="col">Input</th><th scope="col">Output</th></tr></thead><tbody>'""", """'<table class="comparar"><caption>Tabla de entrada y salida</caption><thead><tr><th scope="col">Entrada</th><th scope="col">Salida</th></tr></thead><tbody>'""")
R('function etiqueta(oo, kk){ return "output = input " + sim(oo) + " " + kk; }', 'function etiqueta(oo, kk){ return "salida = entrada " + sim(oo) + " " + kk; }')
R('prueba(["+", salto], "That compares one row with the next. The rule connects each input with its own output: "', 'prueba(["+", salto], "Eso compara una fila con la siguiente. La regla une cada entrada con su propia salida: "')
R('prueba(["+", s0 - ent[0]], "That works for the first row only. Check it with the second row: "', 'prueba(["+", s0 - ent[0]], "Eso sirve solo para la primera fila. Revíselo con la segunda: "')
R('prueba(["x", k], "Try it on the first row: " + ent[0] + " × " + k + " = " + ent[0] * k + ", not " + s0 + ".");', 'prueba(["x", k], "Pruébelo en la primera fila: " + ent[0] + " × " + k + " = " + ent[0] * k + ", no " + s0 + ".");')
R('prueba(["+", k], "Try it on the first row: " + ent[0] + " + " + k + " = " + (ent[0] + k) + ", not " + s0 + ".");', 'prueba(["+", k], "Pruébelo en la primera fila: " + ent[0] + " + " + k + " = " + (ent[0] + k) + ", no " + s0 + ".");')
R('prueba(["-", k], "The outputs are " + (s0 > ent[0] ? "greater" : "less") + " than the inputs, so check the operation.");', 'prueba(["-", k], "Las salidas son " + (s0 > ent[0] ? "mayores" : "menores") + " que las entradas, así que revise la operación.");')
R('enun: "What rule does this table follow?" + tablaES(o, k, ent),', 'enun: "¿Qué regla sigue esta tabla?" + tablaES(o, k, ent),')
R('pista: "Look across each row: what happens to the input to get its output? Check your rule on every row.",', 'pista: "Mire cada fila de izquierda a derecha: ¿qué le pasa a la entrada para dar su salida? Compruebe su regla en todas las filas.",')
R('bien: "Each input " + sim(o) + " " + k + " gives its output: "', 'bien: "Cada entrada " + sim(o) + " " + k + " da su salida: "')
R('mal: "Compare each input with its own output: " + ent[0] + " → " + s0 + ", " + ent[1] + " → " + aplica(o, k, ent[1]) + ". The rule is output = input " + sim(o) + " " + k + "."', 'mal: "Compare cada entrada con su propia salida: " + ent[0] + " → " + s0 + ", " + ent[1] + " → " + aplica(o, k, ent[1]) + ". La regla es salida = entrada " + sim(o) + " " + k + "."')
R('msg: "That is the output of the next row in the table, not the output for " + nueva + ". Use the rule on the input " + nueva + "." });', 'msg: "Esa es la salida de la fila siguiente de la tabla, no la salida para " + nueva + ". Use la regla con la entrada " + nueva + "." });')
R('enun: "Use the rule of this table. What is the output when the input is <strong>" + nueva + "</strong>?" + tablaES(o, k, ent),', 'enun: "Use la regla de esta tabla. ¿Cuál es la salida cuando la entrada es <strong>" + nueva + "</strong>?" + tablaES(o, k, ent),')
R('solucion: "The rule is output = input " + sim(o) + " " + k + ". So "', 'solucion: "La regla es salida = entrada " + sim(o) + " " + k + ". Así que "')
R('"First find the rule from the table, then use it on " + nueva + "."', '"Primero descubra la regla en la tabla, y después úsela con " + nueva + "."')
R("/* ---------- Start ---------- */", "/* ---------- Arranque ---------- */")
t.guarda("es/matematicas/nivel-1/practica-5-1.html")
