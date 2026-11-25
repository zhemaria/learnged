"""Crea es/matematicas/nivel-1/practica-5-2.html a partir de math/level-1/practice-5-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-5-2.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 5.2 · Lenguaje algebraico e incógnitas simples — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 5.2 · Algebraic language and simple unknowns · LearnGED</title>", "<title>Práctica · Lección 5.2 · Lenguaje algebraico e incógnitas simples · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 5 · Patterns and algebraic thinking</div>', '<div class="ruta">Nivel 1 · Tema 5 · Patrones y pensamiento algebraico</div>')
R("<h1>Lesson 5.2 · Algebraic language and simple unknowns</h1>", "<h1>Lección 5.2 · Lenguaje algebraico e incógnitas simples</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad.")
R('<li><a href="#translate">Translate words into symbols</a></li>', '<li><a href="#traducir">Traducir palabras a símbolos</a></li>')
R('<li><a href="#balance">The equation as a scale</a></li>', '<li><a href="#balanza">La ecuación como balanza</a></li>')
R('<li><a href="#inverse-operation">Solve with the inverse operation</a></li>', '<li><a href="#operacion-inversa">Resolver con la operación inversa</a></li>')
R('<li><a href="#check">Check the solution</a></li>', '<li><a href="#comprobar">Comprobar la solución</a></li>')
# 1
R('id="translate" open>', 'id="traducir" open>'); R("<h2>Translate words into symbols</h2>", "<h2>Traducir palabras a símbolos</h2>")
R("""<p>An <strong>unknown</strong> is a number we do not know yet. We write it with a box □ or a letter like <strong>x</strong>.
      Algebra writes ideas with symbols: "a number plus five" is <strong>x + 5</strong>.</p>""",
  """<p>Una <strong>incógnita</strong> es un número que todavía no conocemos. La escribimos con un cuadrito □ o una letra como <strong>x</strong>.
      El álgebra escribe las ideas con símbolos: «un número más cinco» es <strong>x + 5</strong>.</p>""")
R("<caption>Translation table</caption>", "<caption>Tabla de traducción</caption>")
R('<th scope="col">In words</th><th scope="col">In algebra</th>', '<th scope="col">En palabras</th><th scope="col">En álgebra</th>')
R("<td>a number plus 7 · a number increased by 7 · 7 more than a number</td>", "<td>un número más 7 · un número aumentado en 7 · 7 más que un número</td>")
R("<td>a number minus 5 · a number decreased by 5 · 5 less than a number</td>", "<td>un número menos 5 · un número disminuido en 5 · 5 menos que un número</td>")
R("<td>twice a number</td>", "<td>el doble de un número</td>")
R("<td>three times a number</td>", "<td>el triple de un número</td>")
R("<td>a number divided by 4 · half of a number (divided by 2)</td>", "<td>un número dividido entre 4 · la mitad de un número (dividido entre 2)</td>")
R("<td>a number is equal to 12</td>", "<td>un número es igual a 12</td>")
R("""<div class="caja-atencion"><strong>Twice is written together:</strong> 2x, with no sign. A number written next to a letter means multiply.
      And "5 less than a number" is x − 5, not 5 − x: the number comes first.</div>""",
  """<div class="caja-atencion"><strong>El doble se escribe junto:</strong> 2x, sin ningún signo. Un número escrito al lado de una letra quiere decir multiplicar.
      Y «5 menos que un número» es x − 5, no 5 − x: el número va primero.</div>""")
R("<h3>Practice: translate</h3>", "<h3>Practique: traducir</h3>")
# 2
R('id="balance">', 'id="balanza">'); R("<h2>The equation as a scale</h2>", "<h2>La ecuación como balanza</h2>")
R("""<p>An <strong>equation</strong> says that what is on one side of the = sign has the same value as what is on the other side,
      like a balanced scale. <strong>To solve it</strong> is to find the number in the box that keeps the scale level.</p>""",
  """<p>Una <strong>ecuación</strong> dice que lo que está a un lado del signo = vale lo mismo que lo que está al otro lado,
      como una balanza en equilibrio. <strong>Resolverla</strong> es hallar el número del cuadrito que mantiene la balanza nivelada.</p>""")
R("<h3>Find the number in the box</h3>", "<h3>Halle el número del cuadrito</h3>")
R('<label for="bz-x">Try a number for the box: ', '<label for="bz-x">Pruebe un número para el cuadrito: ')
R('id="bz-nueva">New scale</button>', 'id="bz-nueva">Otra balanza</button>')
# 3
R('id="inverse-operation">', 'id="operacion-inversa">'); R("<h2>Solve with the inverse operation</h2>", "<h2>Resolver con la operación inversa</h2>")
R("""<p>The sure method: get the unknown alone with the <strong>inverse operation</strong> of what is with it. Subtraction undoes
      addition, and division undoes multiplication (and the other way around). And the rule of the scale: <strong>whatever you do to one
      side, do to the other side too</strong>.</p>""",
  """<p>El método seguro: deje sola la incógnita con la <strong>operación inversa</strong> de la que la acompaña. La resta deshace
      la suma, y la división deshace la multiplicación (y al revés). Y la regla de la balanza: <strong>lo que haga en un
      lado, hágalo también en el otro</strong>.</p>""")
R("<caption>The inverse operation for each case</caption>", "<caption>La operación inversa para cada caso</caption>")
R('<th scope="col">Equation</th><th scope="col">The x is…</th><th scope="col">Do this to both sides</th>', '<th scope="col">Ecuación</th><th scope="col">La x está…</th><th scope="col">Haga esto en los dos lados</th>')
R("<td>added to 3</td><td>subtract 3: x = 5</td>", "<td>sumada con 3</td><td>restar 3: x = 5</td>")
R("<td>minus 4</td><td>add 4: x = 14</td>", "<td>menos 4</td><td>sumar 4: x = 14</td>")
R("<td>multiplied by 4</td><td>divide by 4: x = 5</td>", "<td>multiplicada por 4</td><td>dividir entre 4: x = 5</td>")
R("<td>divided by 3</td><td>multiply by 3: x = 18</td>", "<td>dividida entre 3</td><td>multiplicar por 3: x = 18</td>")
R('id="oi-sig">Show the first step</button><button type="button" class="btn-sec" id="oi-todo">Show all the steps</button><button type="button" class="btn-sec" id="oi-nueva">New equation</button>',
  'id="oi-sig">Mostrar el primer paso</button><button type="button" class="btn-sec" id="oi-todo">Mostrar todos los pasos</button><button type="button" class="btn-sec" id="oi-nueva">Otra ecuación</button>')
R("<h3>Practice: solve</h3>", "<h3>Practique: resolver</h3>")
R('<label for="p2-r">Value of x</label>', '<label for="p2-r">Valor de x</label>')
# 4
R('id="check">', 'id="comprobar">'); R("<h2>Check the solution</h2>", "<h2>Comprobar la solución</h2>")
R("""<p>To know if an answer is right, <strong>substitute</strong>: put the number in place of x and calculate. If both sides are
      equal, the solution is right. In x + 6 = 15 with x = 9: 9 + 6 = 15 ✓.</p>""",
  """<p>Para saber si una respuesta está bien, <strong>sustituya</strong>: ponga el número en lugar de x y calcule. Si los dos lados son
      iguales, la solución está bien. En x + 6 = 15 con x = 9: 9 + 6 = 15 ✓.</p>""")
R("<h3>Practice: is it the solution?</h3>", "<h3>Practique: ¿es la solución?</h3>")
R("<p><strong>Level 1 · Topic 5 · Patterns and algebraic thinking · LearnGED</strong>", "<p><strong>Nivel 1 · Tema 5 · Patrones y pensamiento algebraico · LearnGED</strong>")
# JS · módulo 1
R(t.s[t.s.index("/* ============ MODULE 1 · translate ============ */"):t.s.index("/* ============ MODULE 2")],
r'''/* ============ MÓDULO 1 · traducir ============ */
var TR = [
  ["un número aumentado en {a}", "x + {a}", "«aumentado en» quiere decir sumar"],
  ["un número más {a}", "x + {a}", "«más» quiere decir sumar"],
  ["{a} más que un número", "x + {a}", "«más que» quiere decir sumar"],
  ["{a} menos que un número", "x − {a}", "«menos que» quiere decir restar, y el número va primero"],
  ["un número disminuido en {a}", "x − {a}", "«disminuido en» quiere decir restar"],
  ["un número menos {a}", "x − {a}", "«menos» quiere decir restar"],
  ["el doble de un número", "2x", "«el doble» quiere decir dos veces"],
  ["el triple de un número", "3x", "«el triple» quiere decir multiplicar por 3"],
  ["{a} veces un número", "{a}x", "«veces» quiere decir multiplicar"],
  ["un número dividido entre {a}", "x ÷ {a}", "«dividido entre» quiere decir dividir"],
  ["la mitad de un número", "x ÷ 2", "«la mitad de» quiere decir dividir entre 2"],
  ["un número es igual a {a}", "x = {a}", "«es igual a» es el signo igual"]
];
/* lo que dice una opción, en palabras */
function enPalabras(e){
  var m;
  if ((m = e.match(/^x \+ (\d+)$/))) return "un número más " + m[1];
  if ((m = e.match(/^x − (\d+)$/))) return "un número menos " + m[1];
  if ((m = e.match(/^(\d+) − x$/))) return m[1] + " menos un número";
  if ((m = e.match(/^(\d+)x$/))) return m[1] + " veces un número";
  if ((m = e.match(/^x ÷ (\d+)$/))) return "un número dividido entre " + m[1];
  if ((m = e.match(/^x = (\d+)$/))) return "un número es igual a " + m[1];
  return e;
}
function genTr(){
  var t = elige(TR), a = aleatorio(4, 12), f = t[0].replace("{a}", a), cor = t[1].replace("{a}", a);
  var pool = ["x + " + a, a + " − x", "x − " + a, a + "x", "x ÷ " + a, "2x", "3x", "x + 2", "x + 3", "x ÷ 2", "x = " + a].filter(function(x){ return x !== cor; });
  var o = [cor];
  if (cor === "x − " + a) o.push(a + " − x");
  baraja(pool).forEach(function(x){ if (o.length < 4 && o.indexOf(x) < 0) o.push(x); });
  var pistas = {};
  o.forEach(function(x){
    if (x === cor) return;
    pistas[x] = x === a + " − x" ? "Cuidado: «" + a + " menos que un número» le quita " + a + " al número, así que el número va primero."
      : x + " quiere decir «" + enPalabras(x) + "». Vuelva a mirar las palabras clave: " + t[2] + ".";
  });
  return {
    enun: "¿Cómo se escribe <strong>«" + f + "»</strong> en lenguaje algebraico?",
    opciones: o.map(function(x){ return { html: x, clave: x }; }), correcta: cor, pistas: pistas,
    pista: "Busque las palabras clave de la frase y la operación que indican.",
    bien: "«" + f + "» → " + cor + ". Recuerde: " + t[2] + ".",
    mal: "«" + f + "» se escribe " + cor + ", porque " + t[2] + "."
  };
}

''')
# JS · módulo 2
R("/* ============ MODULE 2 · the scale ============ */", "/* ============ MÓDULO 2 · la balanza ============ */")
R(""" role="img" aria-label="Scale: on the left, the box with ' + g + ' and a weight of ' + BZ.a + '; on the right, ' + BZ.b + '. ' + (izq === der ? "It is level." : (izq > der ? "The left side is heavier." : "The right side is heavier.")) + '">';""",
  """ role="img" aria-label="Balanza: a la izquierda, el cuadrito con ' + g + ' y una pesa de ' + BZ.a + '; a la derecha, ' + BZ.b + '. ' + (izq === der ? "Está nivelada." : (izq > der ? "El lado izquierdo pesa más." : "El lado derecho pesa más.")) + '">';""")
R("""'<div class="linea veredicto">Level! ' + g + ' + ' + BZ.a + ' = ' + BZ.b + '. The number in the box is ' + g + '.</div>'""",
  """'<div class="linea veredicto">¡Nivelada! ' + g + ' + ' + BZ.a + ' = ' + BZ.b + '. El número del cuadrito es ' + g + '.</div>'""")
R("""(izq > der ? ', more than ' + der + ': the box is too heavy. Try a smaller number.' : ', less than ' + der + ': the box needs more. Try a bigger number.')""",
  """(izq > der ? ', más que ' + der + ': el cuadrito pesa demasiado. Pruebe un número menor.' : ', menos que ' + der + ': al cuadrito le falta. Pruebe un número mayor.')""")
# JS · módulo 3
R("/* ============ MODULE 3 · inverse operation ============ */", "/* ============ MÓDULO 3 · operación inversa ============ */")
R('var inv = ["subtract " + e.a, "add " + e.a, "divide by " + e.a, "multiply by " + e.a][e.t];', 'var inv = ["restar " + e.a, "sumar " + e.a, "dividir entre " + e.a, "multiplicar por " + e.a][e.t];')
R('var con = ["added to " + e.a, "minus " + e.a, "multiplied by " + e.a, "divided by " + e.a][e.t];', 'var con = ["sumada con " + e.a, "menos " + e.a, "multiplicada por " + e.a, "dividida entre " + e.a][e.t];')
R('return ["The x is " + con + ". The inverse operation is <strong>" + inv + "</strong>.",', 'return ["La x está " + con + ". La operación inversa es <strong>" + inv + "</strong>.",')
R('"Do it to both sides, so the scale stays level: " + op + ".",', '"Hágalo en los dos lados, para que la balanza siga nivelada: " + op + ".",')
R('"On the left, the x is alone: x = " + e.x + ".",', '"A la izquierda, la x queda sola: x = " + e.x + ".",')
R("""'<span class="veredicto">Check: ' + izqTxt(e, e.x)""", """'<span class="veredicto">Comprobación: ' + izqTxt(e, e.x)""")
R("/* step-by-step panel */", "/* panel paso a paso */")
R('b.textContent = S.visto === 0 ? "Show the first step" : (fin ? "All the steps are showing" : "Show the next step");', 'b.textContent = S.visto === 0 ? "Mostrar el primer paso" : (fin ? "Ya se ven todos los pasos" : "Mostrar el siguiente paso");')
R('msg: "You used the same operation instead of the inverse one. To undo " + ["adding, subtract", "subtracting, add", "multiplying, divide", "dividing, multiply"][e.t] + "." });',
  'msg: "Usó la misma operación en vez de la inversa. Para deshacer " + ["la suma, reste", "la resta, sume", "la multiplicación, divida", "la división, multiplique"][e.t] + "." });')
R('msg: "The x is " + (e.t === 2 ? "multiplied" : "divided") + ", not added. Undo it with " + (e.t === 2 ? "division" : "multiplication") + "." });',
  'msg: "La x está " + (e.t === 2 ? "multiplicada" : "dividida") + ", no sumada. Deshágalo con " + (e.t === 2 ? "una división" : "una multiplicación") + "." });', 2)
R('enun: "Solve: <strong>" + ecTxt(e) + "</strong>",', 'enun: "Resuelva: <strong>" + ecTxt(e) + "</strong>",')
R('"Find the operation that is with the x, and use its inverse on both sides.")', '"Busque la operación que acompaña a la x, y use su inversa en los dos lados.")')
# JS · módulo 4
R("/* ============ MODULE 4 · check ============ */", "/* ============ MÓDULO 4 · comprobar ============ */")
R('var exp = "Substitute: " + izqTxt(e, prop) + " = " + izqS + (izqS === e.b ? ", and the right side is " + e.b + " ✓. It is the solution." : ", but the right side is " + e.b + " ✗. It is not the solution; the solution is x = " + e.x + ".");',
  'var exp = "Sustituya: " + izqTxt(e, prop) + " = " + izqS + (izqS === e.b ? ", y el lado derecho es " + e.b + " ✓. Es la solución." : ", pero el lado derecho es " + e.b + " ✗. No es la solución; la solución es x = " + e.x + ".");')
R('enun: "Is <strong>x = " + prop + "</strong> the solution of <strong>" + ecTxt(e) + "</strong>?",', 'enun: "¿<strong>x = " + prop + "</strong> es la solución de <strong>" + ecTxt(e) + "</strong>?",')
R('opciones: [{ html: "Yes", clave: "s" }, { html: "No", clave: "n" }]', 'opciones: [{ html: "Sí", clave: "s" }, { html: "No", clave: "n" }]')
R("/* ---------- Start ---------- */", "/* ---------- Inicio ---------- */")
t.guarda("es/matematicas/nivel-1/practica-5-2.html")
