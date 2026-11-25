"""Crea es/matematicas/nivel-1/practica-5-3.html a partir de math/level-1/practice-5-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/practice-5-3.html"); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Nivel 1 · Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones — práctica (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Practice · Lesson 5.3 · One-step word problems with the four operations · LearnGED</title>", "<title>Práctica · Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones · LearnGED</title>")
R('<div class="ruta">Level 1 · Topic 5 · Patterns and algebraic thinking</div>', '<div class="ruta">Nivel 1 · Tema 5 · Patrones y pensamiento algebraico</div>')
R("<h1>Lesson 5.3 · One-step word problems with the four operations</h1>", "<h1>Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones</h1>")
R("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad.")
R('<li><a href="#operation">Choose the operation</a></li>', '<li><a href="#operacion">Elegir la operación</a></li>')
R('<li><a href="#equation">Write the equation</a></li>', '<li><a href="#ecuacion">Escribir la ecuación</a></li>')
R('<li><a href="#solve">Solve word problems step by step</a></li>', '<li><a href="#resolver">Resolver problemas verbales paso a paso</a></li>')
R('<li><a href="#makes-sense">Does the answer make sense?</a></li>', '<li><a href="#tiene-sentido">¿Tiene sentido la respuesta?</a></li>')
# 1
R('id="operation" open>', 'id="operacion" open>'); R("<h2>Choose the operation</h2>", "<h2>Elegir la operación</h2>")
R("<p>Before you calculate, <strong>picture what happens</strong> in the story. Then choose the operation that matches it.</p>", "<p>Antes de calcular, <strong>imagine lo que pasa</strong> en la historia. Después elija la operación que le corresponde.</p>")
R("<caption>Four situations, four operations</caption>", "<caption>Cuatro situaciones, cuatro operaciones</caption>")
R('<th scope="col">What happens in the story</th><th scope="col">Operation</th>', '<th scope="col">Lo que pasa en la historia</th><th scope="col">Operación</th>')
R("<tr><td>Amounts come together, or something increases</td><td>addition</td></tr>", "<tr><td>Se juntan cantidades, o algo aumenta</td><td>suma</td></tr>")
R("<tr><td>Something is taken away, or you compare two amounts</td><td>subtraction</td></tr>", "<tr><td>Se quita algo, o se comparan dos cantidades</td><td>resta</td></tr>")
R("<tr><td>Equal groups come together</td><td>multiplication</td></tr>", "<tr><td>Se juntan grupos iguales</td><td>multiplicación</td></tr>")
R("<tr><td>A total is split into equal groups</td><td>division</td></tr>", "<tr><td>Un total se reparte en grupos iguales</td><td>división</td></tr>")
R('<div class="caja-atencion"><strong>The story decides, not one word.</strong> "Pedro has $58. That is $15 more than Ana has." Ana has less than Pedro, so you subtract, even though the problem says "more."</div>',
  '<div class="caja-atencion"><strong>Decide la historia, no una palabra.</strong> «Pedro tiene $58. Eso es $15 más de lo que tiene Ana». Ana tiene menos que Pedro, así que se resta, aunque el problema diga «más».</div>')
R("<h3>Practice: which operation?</h3>", "<h3>Practique: ¿qué operación?</h3>")
# 2
R('id="equation">', 'id="ecuacion">'); R("<h2>Write the equation</h2>", "<h2>Escribir la ecuación</h2>")
R("<p>When the number you do not know is not the final result, call it <strong>x</strong> and write the story as an equation. Follow the story in order.</p>",
  "<p>Cuando el número que no conoce no es el resultado final, llámelo <strong>x</strong> y escriba la historia como una ecuación. Siga la historia en orden.</p>")
R("<caption>Stories and their equations</caption>", "<caption>Las historias y sus ecuaciones</caption>")
R('<th scope="col">In the story…</th><th scope="col">Equation</th>', '<th scope="col">En la historia…</th><th scope="col">Ecuación</th>')
R("<tr><td>something was added to the amount at first</td>", "<tr><td>se le agregó algo a la cantidad del principio</td>")
R("<tr><td>something was taken away from the amount at first</td>", "<tr><td>se le quitó algo a la cantidad del principio</td>")
R("<tr><td>there are equal groups of the unknown</td>", "<tr><td>hay grupos iguales de la incógnita</td>")
R("<tr><td>the unknown was split into equal parts</td>", "<tr><td>la incógnita se repartió en partes iguales</td>")
R("<h3>Practice: which equation?</h3>", "<h3>Practique: ¿qué ecuación?</h3>")
# 3
R('id="solve">', 'id="resolver">'); R("<h2>Solve word problems step by step</h2>", "<h2>Resolver problemas verbales paso a paso</h2>")
R("<p>The 4 steps with an unknown: <strong>1.</strong> Name the unknown. <strong>2.</strong> Write the equation. <strong>3.</strong> Solve it with the inverse operation. <strong>4.</strong> Check it in the story and answer with the unit. The bar model helps you see the parts and the whole.</p>",
  "<p>Los 4 pasos con una incógnita: <strong>1.</strong> Nombre la incógnita. <strong>2.</strong> Escriba la ecuación. <strong>3.</strong> Resuélvala con la operación inversa. <strong>4.</strong> Compruébela en la historia y responda con la unidad. El modelo de barras le ayuda a ver las partes y el todo.</p>")
R('id="ps-sig">Show the first step</button><button type="button" class="btn-sec" id="ps-todo">Show all the steps</button><button type="button" class="btn-sec" id="ps-nueva">New problem</button>',
  'id="ps-sig">Mostrar el primer paso</button><button type="button" class="btn-sec" id="ps-todo">Mostrar todos los pasos</button><button type="button" class="btn-sec" id="ps-nueva">Otro problema</button>')
R("<h3>Practice: solve the problem</h3>", "<h3>Practique: resolver el problema</h3>")
R('<label for="p3-r">Answer</label>', '<label for="p3-r">Respuesta</label>')
# 4
R('id="makes-sense">', 'id="tiene-sentido">'); R("<h2>Does the answer make sense?</h2>", "<h2>¿Tiene sentido la respuesta?</h2>")
R("<p>Before you give an answer, ask: <strong>Is the size right?</strong> (If a total is split, each part is smaller. If groups come together, the total is bigger.) <strong>Does it fit the story?</strong> <strong>Does it have its unit?</strong></p>",
  "<p>Antes de dar una respuesta, pregúntese: <strong>¿El tamaño es razonable?</strong> (Si se reparte un total, cada parte es menor. Si se juntan grupos, el total es mayor). <strong>¿Encaja en la historia?</strong> <strong>¿Lleva su unidad?</strong></p>")
R("<h3>Practice: which answer makes sense?</h3>", "<h3>Practique: ¿qué respuesta tiene sentido?</h3>")
R("<p><strong>Level 1 · Topic 5 · Patterns and algebraic thinking · LearnGED</strong>", "<p><strong>Nivel 1 · Tema 5 · Patrones y pensamiento algebraico · LearnGED</strong>")
# JS · todos los textos
ini = t.s.index("/* ============ TEXTS (all the words on this page) ============ */")
fin = t.s.index("/* ============ END OF TEXTS ============ */") + len("/* ============ END OF TEXTS ============ */")
R(t.s[ini:fin], r'''/* ============ TEXTOS (todas las palabras de esta página) ============ */
var SIT = [
  { op: "+", txt: "Una tienda tenía {a} bolsas de arroz. Un camión trajo {b} bolsas más. ¿Cuántas bolsas tiene la tienda ahora?", u: "bolsas", w: "algo aumenta", r: [120, 900, 20, 300] },
  { op: "+", txt: "Ana pagó ${a} de comida y ${b} de gasolina. ¿Cuánto pagó en total?", u: "$", w: "se juntan dos cantidades", r: [40, 250, 20, 90] },
  { op: "−", txt: "Un tanque tenía {a} galones de agua. Después se usaron {b} galones. ¿Cuántos galones quedan?", u: "galones", w: "se quita algo", r: [200, 900, 20, 190] },
  { op: "−", txt: "Luis gana ${a} a la semana. Marta gana ${b} a la semana. ¿Cuánto más gana Luis que Marta?", u: "$", w: "se comparan dos cantidades", r: [500, 900, 300, 490] },
  { op: "×", txt: "En una caja caben {a} latas. ¿Cuántas latas hay en {b} cajas?", u: "latas", w: "se juntan grupos iguales", r: [6, 24, 3, 15] },
  { op: "×", txt: "Una trabajadora gana ${a} por hora. ¿Cuánto gana en {b} horas?", u: "$", w: "se juntan grupos iguales", r: [12, 30, 4, 40] },
  { op: "÷", txt: "Se acomodan {p} sillas en {b} filas iguales. ¿Cuántas sillas hay en cada fila?", u: "sillas", w: "un total se reparte en grupos iguales", r: [6, 25, 3, 12], k: "b" },
  { op: "÷", txt: "Se empacan {p} huevos, {a} en cada cartón. ¿Cuántos cartones se necesitan?", u: "cartones", w: "un total se reparte en grupos del mismo tamaño", r: [6, 18, 3, 20], k: "a" }
];
var HIST = [
  { t: 0, txt: "Rosa tenía algo de dinero en su cuenta. Depositó ${a}, y ahora tiene ${b}. ¿Cuánto tenía al principio?", d: "el dinero que Rosa tenía al principio", u: "$", r: [50, 600, 20, 250] },
  { t: 0, txt: "Había algunas personas en un autobús. En una parada se subieron {a} personas más. Ahora hay {b} personas en el autobús. ¿Cuántas personas había antes de la parada?", d: "el número de personas que había en el autobús antes de la parada", u: "personas", r: [5, 40, 2, 20] },
  { t: 0, txt: "Un árbol creció {a} pulgadas este año. Ahora mide {b} pulgadas. ¿Cuánto medía hace un año?", d: "lo que medía el árbol hace un año", u: "pulgadas", r: [24, 120, 2, 15] },
  { t: 1, txt: "Carlos tenía algo de dinero. Gastó ${a} y le quedan ${b}. ¿Cuánto tenía al principio?", d: "el dinero que Carlos tenía al principio", u: "$", r: [40, 500, 10, 200] },
  { t: 1, txt: "Una panadera hizo algunos panes. Vendió {a} panes y le quedan {b}. ¿Cuántos panes hizo?", d: "el número de panes que hizo", u: "panes", r: [5, 40, 20, 90] },
  { t: 1, txt: "Un tanque tenía algo de agua. Después de usar {a} galones, quedan {b} galones. ¿Cuántos galones tenía el tanque?", d: "el número de galones que tenía el tanque al principio", u: "galones", r: [20, 200, 5, 80] },
  { t: 2, txt: "Marcos trabajó {a} horas y ganó ${b}. Gana lo mismo cada hora. ¿Cuánto gana por hora?", d: "el dinero que Marcos gana por hora", u: "$/h", r: [12, 30, 4, 10] },
  { t: 2, txt: "Una maestra compró {a} paquetes iguales de lápices, con {b} lápices en total. ¿Cuántos lápices hay en cada paquete?", d: "el número de lápices de cada paquete", u: "lápices", r: [6, 24, 3, 12] },
  { t: 2, txt: "Un camión recorrió {b} millas en {a} horas, a la misma velocidad cada hora. ¿Cuántas millas recorrió cada hora?", d: "el número de millas que el camión recorrió cada hora", u: "mi/h", r: [35, 65, 2, 9] },
  { t: 3, txt: "Una soga se cortó en {a} pedazos iguales. Cada pedazo mide {b} pies. ¿Cuánto medía la soga?", d: "lo que medía la soga", u: "pies", r: [4, 15, 3, 9] },
  { t: 3, txt: "Una caja de marcadores se repartió en partes iguales entre {a} mesas. A cada mesa le tocaron {b} marcadores. ¿Cuántos marcadores había en la caja?", d: "el número de marcadores que había en la caja", u: "marcadores", r: [4, 12, 3, 8] },
  { t: 3, txt: "El dinero de una rifa se repartió en partes iguales entre {a} familias. A cada familia le tocaron ${b}. ¿Cuánto dinero dejó la rifa?", d: "el dinero que dejó la rifa", u: "$", r: [20, 150, 3, 9] }
];
var TX5 = {
  cita: function(t){ return "«" + t + "»"; },
  conU: function(n, u){ return u === "$" ? "$" + n : (u === "$/h" ? "$" + n + " por hora" : (u === "mi/h" ? n + " millas por hora" : n + " " + u)); },
  opNom: { "+": "Sumar", "−": "Restar", "×": "Multiplicar", "÷": "Dividir" },
  opUso: { "+": "Se suma cuando se juntan cantidades", "−": "Se resta cuando se quita algo o se compara", "×": "Se multiplica cuando se juntan grupos iguales", "÷": "Se divide cuando un total se reparte en grupos iguales" },
  deOp: { "+": "sumar", "−": "restar", "×": "multiplicar", "÷": "dividir" },
  tam: { "+": "Cuando se juntan cantidades, la respuesta es mayor que cada cantidad, pero no enorme.", "−": "Cuando se quita algo o se compara, la respuesta es menor que la cantidad mayor.", "×": "Cuando se juntan grupos iguales, el total es mucho mayor que un grupo.", "÷": "Cuando se reparte un total, cada parte es mucho menor que el total." },
  pregOp: "¿Qué operación necesita?",
  pregTam: "¿Qué respuesta tiene sentido?",
  pregEc: function(d){ return "Si x es " + d + ", ¿qué ecuación muestra esta historia?"; },
  pistaOp: function(op, w){ return TX5.opUso[op] + ". En esta historia, " + w + "."; },
  bienOp: function(w, ex, r){ return "En esta historia, " + w + ": " + ex + " = " + r + "."; },
  pistaTam: function(op, opOk){ return "Esa respuesta sale de " + TX5.deOp[op] + ". " + TX5.tam[opOk]; },
  bienTam: function(w, ex, r, opOk){ return "En esta historia, " + w + ": " + ex + " = " + r + ". " + TX5.tam[opOk]; },
  pistaGen: "Primero imagine lo que pasa en la historia.",
  diez: "Esa respuesta es 10 veces demasiado grande: un cero de más lo cambia todo. Revise el tamaño.",
  porque: ["se le agregó algo a la cantidad del principio", "se le quitó algo a la cantidad del principio", "hay grupos iguales de la incógnita", "la incógnita se repartió en partes iguales"],
  forma: { suma: "x + un número quiere decir que a la incógnita se le agregó algo.", resta: "x − un número quiere decir que a la incógnita se le quitó algo.", por: "Un número pegado a la x quiere decir grupos iguales de la incógnita.", entre: "x ÷ un número quiere decir que la incógnita se repartió en partes iguales.", lugar: "Fíjese dónde van los números: el resultado de la historia va solo en un lado." },
  pistaEc: function(f, t){ return TX5.forma[f] + " En esta historia, " + TX5.porque[t] + "."; },
  bienEc: function(d, t, ec, x){ return "x es " + d + ". En esta historia, " + TX5.porque[t] + ": " + ec + ". Al resolverla: x = " + x + "."; },
  pistaEcGen: "Lea la historia en orden: ¿qué le pasó a la cantidad que no conoce?",
  inversa: function(t, a){ return ["restar " + a, "sumar " + a, "dividir entre " + a, "multiplicar por " + a][t]; },
  paso1: function(d){ return "<strong>Nombre la incógnita.</strong> x = " + d + "."; },
  paso2: function(t, ec){ return "<strong>Escriba la ecuación.</strong> En la historia, " + TX5.porque[t] + ": " + ec + "."; },
  paso3: function(t, a, op, x){ return "<strong>Resuelva.</strong> La operación inversa es " + TX5.inversa(t, a) + ": x = " + op + " = " + x + "."; },
  paso4: function(c, r){ return "<strong>Compruebe y responda.</strong> " + c + " ✓. La respuesta es " + r + "."; },
  respuesta: "La respuesta es ",
  mismaOp: function(t){ return "Usó la operación de la historia en vez de su inversa. Para deshacer " + ["la suma, reste", "la resta, sume", "la multiplicación, divida", "la división, multiplique"][t] + "."; },
  otraOp: function(t){ return "La incógnita está " + (t === 2 ? "en grupos iguales" : "repartida en partes iguales") + ", no sumada. Deshágalo con " + (t === 2 ? "una división" : "una multiplicación") + "."; },
  pistaRes: "Nombre la incógnita, escriba la ecuación y use la operación inversa.",
  cinta: function(t, a, b){ return ["Modelo de barras: un todo de " + b + " dividido en la incógnita x y " + a + ".", "Modelo de barras: la incógnita x es el todo, dividido en " + b + " que quedan y " + a + " que se quitaron.", "Modelo de barras: un todo de " + b + " dividido en " + a + " partes iguales, cada una x.", "Modelo de barras: la incógnita x es el todo, dividido en " + a + " partes iguales de " + b + " cada una."][t]; },
  btn: ["Mostrar el primer paso", "Mostrar el siguiente paso", "Ya se ven todos los pasos"]
};
/* ============ FIN DE LOS TEXTOS ============ */''')
for a, b in [("/* ---------- shared tools ---------- */", "/* ---------- herramientas comunes ---------- */"),
             ("/* ============ MODULE 1 · choose the operation ============ */", "/* ============ MÓDULO 1 · elegir la operación ============ */"),
             ("/* ============ MODULE 2 · write the equation ============ */", "/* ============ MÓDULO 2 · escribir la ecuación ============ */"),
             ("/* ============ MODULE 3 · solve step by step ============ */", "/* ============ MÓDULO 3 · resolver paso a paso ============ */"),
             ("/* ============ MODULE 4 · does it make sense? ============ */", "/* ============ MÓDULO 4 · ¿tiene sentido? ============ */"),
             ("/* ---------- Start ---------- */", "/* ---------- Inicio ---------- */")]:
    R(a, b)
t.guarda("es/matematicas/nivel-1/practica-5-3.html")
