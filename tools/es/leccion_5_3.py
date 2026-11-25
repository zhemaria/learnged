"""Crea es/matematicas/nivel-1/leccion-5-3.html a partir de math/level-1/lesson-5-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-5-3.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 5.3 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 5.3 · One-step word problems with the four operations · LearnGED</title>", "<title>Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 5 — Patterns and algebraic thinking</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 5 — Patrones y pensamiento algebraico</p>')
R("<h1>Lesson 5.3 · One-step word problems with the four operations</h1>", "<h1>Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones</h1>")
R('<p class="lema">Read the story, find the unknown, write the equation, and solve it. Everything from Level 1 comes together here.</p>', '<p class="lema">Lea la historia, halle la incógnita, escriba la ecuación y resuélvala. Aquí se junta todo el Nivel 1.</p>')
R("From the story to the equation</span>", "De la historia a la ecuación</span>")
R("<li><strong>Picture</strong> the situation in a story and choose which of the four operations it needs.</li>", "<li><strong>Imaginar</strong> la situación de una historia y elegir cuál de las cuatro operaciones necesita.</li>")
R("<li><strong>Name</strong> the unknown and write the problem as a one-step equation.</li>", "<li><strong>Nombrar</strong> la incógnita y escribir el problema como una ecuación de un paso.</li>")
R("<li><strong>Solve</strong> the equation with the inverse operation.</li>", "<li><strong>Resolver</strong> la ecuación con la operación inversa.</li>")
R("<li><strong>Check</strong> that the answer makes sense and has the right unit.</li>", "<li><strong>Comprobar</strong> que la respuesta tiene sentido y lleva la unidad correcta.</li>")
R('<li><a href="#s-together">Everything comes together</a></li>', '<li><a href="#s-todo-junto">Todo se junta</a></li>')
R('<li><a href="#s-situations">Four situations, four operations</a></li>', '<li><a href="#s-situaciones">Cuatro situaciones, cuatro operaciones</a></li>')
R('<li><a href="#s-equation">From the story to the equation</a></li>', '<li><a href="#s-ecuacion">De la historia a la ecuación</a></li>')
R('<li><a href="#s-sense">Does the answer make sense?</a></li>', '<li><a href="#s-sentido">¿Tiene sentido la respuesta?</a></li>')
# 1
R('<h2 id="s-together"><span aria-hidden="true" class="num-seccion">1</span>Everything comes together</h2>', '<h2 id="s-todo-junto"><span aria-hidden="true" class="num-seccion">1</span>Todo se junta</h2>')
R("<p>This lesson closes Topic 5 and puts together everything you learned in Level 1. In <strong>Topics 1 and 2</strong> you learned when to add, subtract, multiply, and divide in a word problem. In <strong>Lesson 5.2</strong> you learned to write and solve equations with an unknown.</p>",
  "<p>Esta lección cierra el Tema 5 y junta todo lo que aprendió en el Nivel 1. En los <strong>Temas 1 y 2</strong> aprendió cuándo sumar, restar, multiplicar y dividir en un problema verbal. En la <strong>Lección 5.2</strong> aprendió a escribir y resolver ecuaciones con una incógnita.</p>")
R("<p>Now you will join both ideas: you will read a problem in words, find the number you do not know, write it as an equation, and solve it.</p>",
  "<p>Ahora va a unir las dos ideas: leerá un problema en palabras, hallará el número que no conoce, lo escribirá como una ecuación y la resolverá.</p>")
R('<span class="etiqueta et-verde">The key idea of this lesson</span>', '<span class="etiqueta et-verde">La idea clave de esta lección</span>')
R("<p>A word problem is a <strong>story with an unknown</strong>. Your job is to translate the story into an equation, solve the equation, and answer the question with the right unit.</p>",
  "<p>Un problema verbal es una <strong>historia con una incógnita</strong>. Su trabajo es traducir la historia a una ecuación, resolver la ecuación y responder la pregunta con la unidad correcta.</p>")
# 2
R('<h2 id="s-situations"><span aria-hidden="true" class="num-seccion">2</span>Four situations, four operations</h2>', '<h2 id="s-situaciones"><span aria-hidden="true" class="num-seccion">2</span>Cuatro situaciones, cuatro operaciones</h2>')
R("<p>Before you choose an operation, <strong>picture what happens</strong> in the story. Each operation matches one kind of situation:</p>", "<p>Antes de elegir una operación, <strong>imagine lo que pasa</strong> en la historia. Cada operación corresponde a un tipo de situación:</p>")
R('aria-label="Situations and their operations (tabla desplazable horizontalmente)"', 'aria-label="Las situaciones y sus operaciones (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Each kind of situation and the operation it needs</caption>', '<caption class="cap-oculto">Cada tipo de situación y la operación que necesita</caption>')
R('<th scope="col">Situation</th><th scope="col">What happens</th><th scope="col">Operation</th><th scope="col">Example</th>', '<th scope="col">Situación</th><th scope="col">Qué pasa</th><th scope="col">Operación</th><th scope="col">Ejemplo</th>')
R("<td><strong>Put together · add on</strong></td><td>Amounts come together, or something increases.</td><td>Addition</td>", "<td><strong>Juntar · agregar</strong></td><td>Se juntan cantidades, o algo aumenta.</td><td>Suma</td>")
R("<td><strong>Take away · compare</strong></td><td>Something is taken away, or you find the difference between two amounts.</td><td>Subtraction</td>", "<td><strong>Quitar · comparar</strong></td><td>Se quita algo, o se halla la diferencia entre dos cantidades.</td><td>Resta</td>")
R("<td><strong>Equal groups</strong></td><td>Several groups of the same size come together.</td><td>Multiplication</td>", "<td><strong>Grupos iguales</strong></td><td>Se juntan varios grupos del mismo tamaño.</td><td>Multiplicación</td>")
R("<td><strong>Split equally</strong></td><td>A total is split into equal parts, or into groups of a given size.</td><td>Division</td>", "<td><strong>Repartir en partes iguales</strong></td><td>Un total se reparte en partes iguales, o en grupos de un tamaño dado.</td><td>División</td>")
R('<span class="etiqueta et-ambar">Watch out! The words can fool you</span>', '<span class="etiqueta et-ambar">¡Cuidado! Las palabras pueden engañarle</span>')
R('<p>Key words help, but <strong>the story decides</strong>. Look at this problem: "Pedro has $58. That is $15 more than Ana has. How much does Ana have?" It says "more," but Ana has <strong>less</strong> than Pedro. So we subtract: 58 − 15 = <strong>$43</strong>.</p>',
  '<p>Las palabras clave ayudan, pero <strong>la historia decide</strong>. Mire este problema: «Pedro tiene $58. Eso es $15 más de lo que tiene Ana. ¿Cuánto tiene Ana?». Dice «más», pero Ana tiene <strong>menos</strong> que Pedro. Así que restamos: 58 − 15 = <strong>$43</strong>.</p>')
R("<h3>Practice 1 — Choose the operation</h3>", "<h3>Práctica 1 — Elegir la operación</h3>")
R('"A store receives 12 boxes. Each box has 24 bottles. How many bottles are there in all?" Which operation do you need?', '«Una tienda recibe 12 cajas. Cada caja tiene 24 botellas. ¿Cuántas botellas hay en total?». ¿Qué operación necesita?')
R('type="button">Add: 12 + 24</button>', 'type="button">Sumar: 12 + 24</button>')
R('type="button">Subtract: 24 − 12</button>', 'type="button">Restar: 24 − 12</button>')
R('type="button">Multiply: 12 × 24</button>', 'type="button">Multiplicar: 12 × 24</button>')
R('type="button">Divide: 24 ÷ 12</button>', 'type="button">Dividir: 24 ÷ 12</button>')
R("<h3>Practice 2 — When the words fool you</h3>", "<h3>Práctica 2 — Cuando las palabras engañan</h3>")
R('"Rita is 41 years old. She is 7 years older than her brother. How old is her brother?"', '«Rita tiene 41 años. Tiene 7 años más que su hermano. ¿Cuántos años tiene su hermano?»')
for n in ["48", "34", "287", "7"]:
    R(f'type="button">{n} years</button>', f'type="button">{n} años</button>')
R('href="practice-5-3.html#operation"', 'href="practica-5-3.html#operacion"')
R('práctica: choose the operation (se abre', 'práctica: elegir la operación (se abre')
R('<span class="ei-titulo">Practique más: choose the operation</span><span class="ei-sub">Read a situation, picture what happens, and choose the operation.</span>',
  '<span class="ei-titulo">Practique más: elegir la operación</span><span class="ei-sub">Lea una situación, imagine lo que pasa y elija la operación.</span>')
# 3
R('<h2 id="s-equation"><span aria-hidden="true" class="num-seccion">3</span>From the story to the equation</h2>', '<h2 id="s-ecuacion"><span aria-hidden="true" class="num-seccion">3</span>De la historia a la ecuación</h2>')
R("<p>When the number you do not know is not the final result, an equation helps a lot. Use the 4 steps from Lesson 1.3, now with an unknown:</p>",
  "<p>Cuando el número que no conoce no es el resultado final, una ecuación ayuda mucho. Use los 4 pasos de la Lección 1.3, ahora con una incógnita:</p>")
R('<span class="etiqueta et-verde">The 4 steps with an unknown</span>', '<span class="etiqueta et-verde">Los 4 pasos con una incógnita</span>')
R("<strong>Read and name the unknown.</strong> Underline the numbers and the question. Call the number you do not know x.", "<strong>Lea y nombre la incógnita.</strong> Subraye los números y la pregunta. Llame x al número que no conoce.")
R("<strong>Write the equation.</strong> Follow the story in order, with x in its place.", "<strong>Escriba la ecuación.</strong> Siga la historia en orden, con la x en su lugar.")
R("<strong>Solve</strong> with the inverse operation, as in Lesson 5.2.", "<strong>Resuelva</strong> con la operación inversa, como en la Lección 5.2.")
R("<strong>Check and answer.</strong> Put the value back into the story, and write the answer with its unit.", "<strong>Compruebe y responda.</strong> Vuelva a poner el valor en la historia, y escriba la respuesta con su unidad.")
R('<p class="titulo-ej">Example: "Rosa had some money in her account. She deposited $85, and now she has $310. How much did she have at first?"</p>',
  '<p class="titulo-ej">Ejemplo: «Rosa tenía algo de dinero en su cuenta. Depositó $85, y ahora tiene $310. ¿Cuánto tenía al principio?»</p>')
R('aria-label="A bar model. A whole bar of 310 is split into two parts: the unknown x and 85."', 'aria-label="Un modelo de barras. Una barra entera de 310 está dividida en dos partes: la incógnita x y 85."')
R("<strong>Name the unknown.</strong> x = the money Rosa had at first.", "<strong>Nombre la incógnita.</strong> x = el dinero que Rosa tenía al principio.")
R('<strong>Write the equation.</strong> She had x, and $85 was added: ', '<strong>Escriba la ecuación.</strong> Tenía x, y se le agregaron $85: ')
R("<strong>Solve.</strong> Subtract 85 from both sides: x = 310 − 85 = 225.", "<strong>Resuelva.</strong> Reste 85 en los dos lados: x = 310 − 85 = 225.")
R("<strong>Check and answer.</strong> $225 + $85 = $310 ✓. Rosa had <strong>$225</strong> at first.", "<strong>Compruebe y responda.</strong> $225 + $85 = $310 ✓. Rosa tenía <strong>$225</strong> al principio.")
R('<p class="titulo-ej">Example: "Marcos worked 8 hours and earned $136. He earns the same amount each hour. How much does he earn per hour?"</p>',
  '<p class="titulo-ej">Ejemplo: «Marcos trabajó 8 horas y ganó $136. Gana lo mismo cada hora. ¿Cuánto gana por hora?»</p>')
R('aria-label="A bar model. A whole bar of 136 is split into 8 equal parts, each one marked x."', 'aria-label="Un modelo de barras. Una barra entera de 136 está dividida en 8 partes iguales, cada una marcada con x."')
R("<strong>Name the unknown.</strong> x = the money Marcos earns per hour.", "<strong>Nombre la incógnita.</strong> x = el dinero que Marcos gana por hora.")
R("<strong>Write the equation.</strong> 8 equal hours of x dollars each: ", "<strong>Escriba la ecuación.</strong> 8 horas iguales de x dólares cada una: ")
R("<strong>Solve.</strong> Divide both sides by 8: x = 136 ÷ 8 = 17.", "<strong>Resuelva.</strong> Divida los dos lados entre 8: x = 136 ÷ 8 = 17.")
R("<strong>Check and answer.</strong> 8 × $17 = $136 ✓. Marcos earns <strong>$17 per hour</strong>.", "<strong>Compruebe y responda.</strong> 8 × $17 = $136 ✓. Marcos gana <strong>$17 por hora</strong>.")
R("<p>Every one-step story fits one of these four equations:</p>", "<p>Toda historia de un paso cabe en una de estas cuatro ecuaciones:</p>")
R('aria-label="Kinds of stories and their equations (tabla desplazable horizontalmente)"', 'aria-label="Tipos de historias y sus ecuaciones (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">The four kinds of one-step stories and their equations</caption>', '<caption class="cap-oculto">Los cuatro tipos de historias de un paso y sus ecuaciones</caption>')
R('<th scope="col">Story</th><th scope="col">Equation</th><th scope="col">Solution</th>', '<th scope="col">Historia</th><th scope="col">Ecuación</th><th scope="col">Solución</th>')
R("<td>I had some money, I got $25 more, and now I have $60.</td>", "<td>Tenía algo de dinero, recibí $25 más, y ahora tengo $60.</td>")
R("<td>I had some money, I spent $15, and I have $40 left.</td>", "<td>Tenía algo de dinero, gasté $15, y me quedan $40.</td>")
R("<td>6 equal boxes hold 72 cans in all.</td>", "<td>En 6 cajas iguales caben 72 latas en total.</td>")
R("<td>Some markers were split equally among 4 tables, and each table got 9.</td>", "<td>Unos marcadores se repartieron en partes iguales entre 4 mesas, y a cada mesa le tocaron 9.</td>")
R("<h3>Practice 3 — Write the equation</h3>", "<h3>Práctica 3 — Escribir la ecuación</h3>")
R('"Some people were on a bus. At a stop, 14 more people got on. Now there are 50 people on the bus." If x is the number of people at first, which equation shows this story?',
  '«Había algunas personas en un autobús. En una parada se subieron 14 personas más. Ahora hay 50 personas en el autobús». Si x es el número de personas que había al principio, ¿qué ecuación muestra esta historia?')
R("<h3>Practice 4 — Solve the problem</h3>", "<h3>Práctica 4 — Resolver el problema</h3>")
R('"A teacher split a box of markers equally among 5 tables. Each table got 8 markers. How many markers were in the box?"', '«Una maestra repartió una caja de marcadores en partes iguales entre 5 mesas. A cada mesa le tocaron 8 marcadores. ¿Cuántos marcadores había en la caja?»')
for n in ["13", "3", "8", "40"]:
    R(f'type="button">{n} markers</button>', f'type="button">{n} marcadores</button>')
R('href="practice-5-3.html#equation"', 'href="practica-5-3.html#ecuacion"')
R('práctica: write the equation (se abre', 'práctica: escribir la ecuación (se abre')
R('<span class="ei-titulo">Practique más: write the equation</span><span class="ei-sub">Read a story and choose the equation that shows it.</span>',
  '<span class="ei-titulo">Practique más: escribir la ecuación</span><span class="ei-sub">Lea una historia y elija la ecuación que la muestra.</span>')
R('href="practice-5-3.html#solve"', 'href="practica-5-3.html#resolver"')
R('práctica: solve word problems step by step (se abre', 'práctica: resolver problemas verbales paso a paso (se abre')
R('<span class="ei-titulo">Practique más: solve word problems step by step</span><span class="ei-sub">Follow the 4 steps with an unknown, then solve problems on your own.</span>',
  '<span class="ei-titulo">Practique más: resolver problemas verbales paso a paso</span><span class="ei-sub">Siga los 4 pasos con una incógnita, y después resuelva problemas por su cuenta.</span>')
# 4
R('<h2 id="s-sense"><span aria-hidden="true" class="num-seccion">4</span>Does the answer make sense?</h2>', '<h2 id="s-sentido"><span aria-hidden="true" class="num-seccion">4</span>¿Tiene sentido la respuesta?</h2>')
R("<p>The last step is the one people skip most, and it catches many mistakes. Ask yourself three questions:</p>", "<p>El último paso es el que más se salta la gente, y atrapa muchos errores. Hágase tres preguntas:</p>")
R("<li><strong>Is the size right?</strong> If something was added, the total must be bigger. If a total was split, each part must be smaller.</li>", "<li><strong>¿El tamaño es razonable?</strong> Si se agregó algo, el total tiene que ser mayor. Si se repartió un total, cada parte tiene que ser menor.</li>")
R("<li><strong>Does it fit the story?</strong> Put the answer back into the story, not only into the equation.</li>", "<li><strong>¿Encaja en la historia?</strong> Vuelva a poner la respuesta en la historia, no solo en la ecuación.</li>")
R("<li><strong>Does it have its unit?</strong> Dollars, miles, hours, people… A number alone does not answer the question.</li>", "<li><strong>¿Lleva su unidad?</strong> Dólares, millas, horas, personas… Un número solo no responde la pregunta.</li>")
R('<p class="titulo-ej">Example: "A school bought 7 equal boxes of paper with 3,500 sheets in all. How many sheets are in each box?"</p>',
  '<p class="titulo-ej">Ejemplo: «Una escuela compró 7 cajas iguales de papel con 3,500 hojas en total. ¿Cuántas hojas hay en cada caja?»</p>')
R("<strong>Solve.</strong> ", "<strong>Resuelva.</strong> ")
R(", so x = 3,500 ÷ 7 = 500.", ", así que x = 3,500 ÷ 7 = 500.")
R("<strong>Check the size.</strong> Each box holds part of the total, so the answer must be smaller than 3,500. 500 is smaller ✓.", "<strong>Revise el tamaño.</strong> Cada caja tiene una parte del total, así que la respuesta tiene que ser menor que 3,500. 500 es menor ✓.")
R("<strong>Check the story and the unit.</strong> 7 boxes × 500 sheets = 3,500 sheets ✓. Each box has <strong>500 sheets</strong>.", "<strong>Revise la historia y la unidad.</strong> 7 cajas × 500 hojas = 3,500 hojas ✓. Cada caja tiene <strong>500 hojas</strong>.")
R('<span class="etiqueta et-ambar">Watch out! Extra information</span>', '<span class="etiqueta et-ambar">¡Cuidado! Información de sobra</span>')
R('<p>Some problems give you numbers you do not need. "A store sold 45 shirts and 38 pants. Each shirt costs $12. How much money did the shirts bring in?" The 38 pants do not matter for this question: 45 × $12 = <strong>$540</strong>.</p>',
  '<p>Algunos problemas le dan números que no necesita. «Una tienda vendió 45 camisas y 38 pantalones. Cada camisa cuesta $12. ¿Cuánto dinero dejaron las camisas?». Los 38 pantalones no importan para esta pregunta: 45 × $12 = <strong>$540</strong>.</p>')
R("Solve it and check it on the calculator</span>", "Resuélvalo y compruébelo en la calculadora</span>")
R("<p>The calculator can do the inverse operation for you, and then check the answer against the story.</p>", "<p>La calculadora puede hacer la operación inversa por usted, y después comprobar la respuesta con la historia.</p>")
R("<li>Solve ", "<li>Resuelva ")
R(": type ", ": escriba ", 2)
R(". The screen shows 500.</li>", ". La pantalla muestra 500.</li>")
R("<li>Check it: escriba ", "<li>Compruébelo: escriba ")
R(". The screen shows 3500, the total in the story: ✓.</li>", ". La pantalla muestra 3500, el total de la historia: ✓.</li>")
R('href="practice-5-3.html#makes-sense"', 'href="practica-5-3.html#tiene-sentido"')
R('práctica: does the answer make sense? (se abre', 'práctica: ¿tiene sentido la respuesta? (se abre')
R('<span class="ei-titulo">Practique más: does the answer make sense?</span><span class="ei-sub">Choose the answer that fits the story, with the right size and the right unit.</span>',
  '<span class="ei-titulo">Practique más: ¿tiene sentido la respuesta?</span><span class="ei-sub">Elija la respuesta que encaja en la historia, con el tamaño y la unidad correctos.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-5-3.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-5-3.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Write four short stories of your own, one for each operation. For each one, name the unknown, write the equation, solve it, and check it. Then trade stories with a classmate or a family member and solve theirs.</li>",
  "<li><strong>Papel y lápiz.</strong> Invente cuatro historias cortas, una para cada operación. En cada una, nombre la incógnita, escriba la ecuación, resuélvala y compruébela. Después intercambie historias con un compañero de clase o con alguien de su familia y resuelva las de esa persona.</li>")
R("<li><strong>In your daily life.</strong> Look for a real one-step problem this week: a bill split among roommates, the hours you need to work to earn a certain amount, the miles left on a trip. Solve it with the 4 steps and write the answer with its unit.</li>",
  "<li><strong>En su vida diaria.</strong> Busque esta semana un problema real de un paso: una cuenta repartida entre compañeros de casa, las horas que necesita trabajar para ganar cierta cantidad, las millas que faltan en un viaje. Resuélvalo con los 4 pasos y escriba la respuesta con su unidad.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R('"A cook splits 96 tortillas equally into 8 bags. How many tortillas go in each bag?" Which operation do you need?', '«Un cocinero reparte 96 tortillas en partes iguales en 8 bolsas. ¿Cuántas tortillas van en cada bolsa?». ¿Qué operación necesita?')
R('type="button">Add.</button><button class="opcion" data-k="b" type="button">Subtract.</button><button class="opcion" data-k="c" type="button">Multiply.</button><button class="opcion" data-k="d" type="button">Divide.</button>',
  'type="button">Sumar.</button><button class="opcion" data-k="b" type="button">Restar.</button><button class="opcion" data-k="c" type="button">Multiplicar.</button><button class="opcion" data-k="d" type="button">Dividir.</button>')
R('"Lucía is 34 years old. She is 9 years older than her brother. How old is her brother?"', '«Lucía tiene 34 años. Tiene 9 años más que su hermano. ¿Cuántos años tiene su hermano?»')
R('type="button">43 years</button><button class="opcion" data-k="b" type="button">25 years</button><button class="opcion" data-k="c" type="button">306 years</button><button class="opcion" data-k="d" type="button">9 years</button>',
  'type="button">43 años</button><button class="opcion" data-k="b" type="button">25 años</button><button class="opcion" data-k="c" type="button">306 años</button><button class="opcion" data-k="d" type="button">9 años</button>')
R('"A worker had some money. He spent $65 and has $120 left." If x is the money he had, which equation shows this story?', '«Un trabajador tenía algo de dinero. Gastó $65 y le quedan $120». Si x es el dinero que tenía, ¿qué ecuación muestra esta historia?')
R('"Each ticket costs $15. A group paid $180 in all." If x is the number of tickets, which equation shows this story?', '«Cada boleto cuesta $15. Un grupo pagó $180 en total». Si x es el número de boletos, ¿qué ecuación muestra esta historia?')
R('"A rope was cut into 6 equal pieces. Each piece is 9 feet long. How long was the rope?"', '«Una soga se cortó en 6 pedazos iguales. Cada pedazo mide 9 pies. ¿Cuánto medía la soga?»')
R('type="button">15 feet</button><button class="opcion" data-k="b" type="button">3 feet</button><button class="opcion" data-k="c" type="button">54 feet</button><button class="opcion" data-k="d" type="button">9 feet</button>',
  'type="button">15 pies</button><button class="opcion" data-k="b" type="button">3 pies</button><button class="opcion" data-k="c" type="button">54 pies</button><button class="opcion" data-k="d" type="button">9 pies</button>')
R('"A family pays $1,200 in rent each month. How much do they pay in 12 months?" Which answer makes sense?', '«Una familia paga $1,200 de renta cada mes. ¿Cuánto paga en 12 meses?». ¿Qué respuesta tiene sentido?')
R('"A store sold 45 shirts and 38 pants. Each shirt costs $12. How much money did the shirts bring in?"', '«Una tienda vendió 45 camisas y 38 pantalones. Cada camisa cuesta $12. ¿Cuánto dinero dejaron las camisas?»')
R('"A car travels 240 miles on 8 gallons of gas. How many miles does it travel per gallon?"', '«Un carro recorre 240 millas con 8 galones de gasolina. ¿Cuántas millas recorre por galón?»')
R('type="button">30 gallons</button><button class="opcion" data-k="b" type="button">1,920 miles</button><button class="opcion" data-k="c" type="button">248 miles</button><button class="opcion" data-k="d" type="button">30 miles per gallon</button>',
  'type="button">30 galones</button><button class="opcion" data-k="b" type="button">1,920 millas</button><button class="opcion" data-k="c" type="button">248 millas</button><button class="opcion" data-k="d" type="button">30 millas por galón</button>')
# Lista
R('aria-label="Self-check checklist for one-step word problems (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de problemas verbales de un paso (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for one-step word problems ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas para problemas verbales de un paso ')
R('<tr><th scope="row">Picture the situation</th><td>I picture what happens and choose the operation, even when the words try to fool me.</td><td>I choose the right operation in most problems.</td><td>I only look for key words, and sometimes I choose the wrong operation.</td></tr>',
  '<tr><th scope="row">Imaginar la situación</th><td>Imagino lo que pasa y elijo la operación, aunque las palabras traten de engañarme.</td><td>Elijo la operación correcta en la mayoría de los problemas.</td><td>Solo busco palabras clave, y a veces elijo la operación equivocada.</td></tr>')
R('<tr><th scope="row">Name the unknown and write the equation</th><td>I name the unknown and write an equation that follows the story.</td><td>I write the equation, but sometimes I put a number in the wrong place.</td><td>I am not sure what the unknown is or how to write the equation.</td></tr>',
  '<tr><th scope="row">Nombrar la incógnita y escribir la ecuación</th><td>Nombro la incógnita y escribo una ecuación que sigue la historia.</td><td>Escribo la ecuación, pero a veces pongo un número en el lugar equivocado.</td><td>No estoy seguro de cuál es la incógnita ni de cómo escribir la ecuación.</td></tr>')
R('<tr><th scope="row">Solve the equation</th><td>I solve with the inverse operation, with no mistakes.</td><td>I solve correctly, with an occasional slip.</td><td>I use the same operation instead of the inverse one.</td></tr>',
  '<tr><th scope="row">Resolver la ecuación</th><td>Resuelvo con la operación inversa, sin errores.</td><td>Resuelvo bien, con algún descuido de vez en cuando.</td><td>Uso la misma operación en vez de la inversa.</td></tr>')
R('<tr><th scope="row">Check that the answer makes sense</th><td>I check the size, the story, and the unit every time.</td><td>I check when I remember.</td><td>I give a number without checking it or writing its unit.</td></tr>',
  '<tr><th scope="row">Comprobar que la respuesta tiene sentido</th><td>Reviso el tamaño, la historia y la unidad, siempre.</td><td>Reviso cuando me acuerdo.</td><td>Doy un número sin revisarlo ni escribir su unidad.</td></tr>')
# Cierre
R("<p>You can now solve one-step word problems with the four operations: picture the situation, write the equation, solve it, and check that the answer makes sense. With this lesson, you finish Topic 5.</p>",
  "<p>Ya sabe resolver problemas verbales de un paso con las cuatro operaciones: imaginar la situación, escribir la ecuación, resolverla y comprobar que la respuesta tiene sentido. Con esta lección termina el Tema 5.</p>")
R("<p>In <strong>Topic 6 · Measurement and time</strong> you will use these skills with real measures: inches and feet, pounds and ounces, cups and gallons, and also the metric system, time, and temperature.</p>",
  "<p>En el <strong>Tema 6 · Sistemas de medidas y el tiempo</strong> usará estas destrezas con medidas reales: pulgadas y pies, libras y onzas, tazas y galones, y también el sistema métrico, el tiempo y la temperatura.</p>")
R('Next: Topic 6 · <a href="lesson-6-1.html">Lesson 6.1 · U.S. customary units: length, weight, and capacity</a></p>', 'Siguiente: Tema 6 · <a href="leccion-6-1.html">Lección 6.1 · Sistema inglés: longitud, peso y capacidad</a></p>')
R("""<dt>word problem</dt><dd>A math problem told as a story in words, with a question to answer.</dd>
<dt>unknown</dt><dd>The number we do not know yet. In an equation we call it x.</dd>
<dt>equation</dt><dd>A statement that two things are equal, like x + 85 = 310.</dd>
<dt>bar model</dt><dd>A drawing with bars that shows the parts and the whole of a problem.</dd>
<dt>reasonable</dt><dd>Said of an answer that makes sense in the story: it has the right size and the right unit.</dd>
<dt>unit</dt><dd>What a number counts or measures: dollars, miles, hours, people.</dd>""",
"""<dt>problema verbal</dt><dd>Un problema de matemáticas contado como una historia en palabras, con una pregunta que responder.</dd>
<dt>incógnita</dt><dd>El número que todavía no conocemos. En una ecuación lo llamamos x.</dd>
<dt>ecuación</dt><dd>Una afirmación de que dos cosas son iguales, como x + 85 = 310.</dd>
<dt>modelo de barras</dt><dd>Un dibujo con barras que muestra las partes y el todo de un problema.</dd>
<dt>razonable</dt><dd>Se dice de una respuesta que tiene sentido en la historia: tiene el tamaño correcto y la unidad correcta.</dd>
<dt>unidad</dt><dd>Lo que un número cuenta o mide: dólares, millas, horas, personas.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.3</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 5 · Lección 5.3</p>")
t.js('''{
 next: "Lección 6.1",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "c",
   hints: { a: "Sumar 12 + 24 junta dos cosas distintas. Aquí hay 12 grupos iguales de 24 botellas.", b: "En esta historia no se quita nada. Cada caja tiene la misma cantidad de botellas: grupos iguales.", d: "No se reparte nada. Las cajas se juntan, cada una con 24 botellas: grupos iguales." },
   right: "12 grupos iguales de 24 botellas: 12 × 24 = 288 botellas.",
   solution: "Cada caja tiene la misma cantidad de botellas, y las cajas se juntan: grupos iguales. Multiplique: 12 × 24 = 288 botellas." },
  p2: { ok: "b",
   hints: { a: "48 es 41 + 7. La palabra «más» puede engañarle: Rita es mayor, así que su hermano es menor.", c: "287 es 41 × 7. No hay grupos iguales que se repitan. Compare las dos edades.", d: "7 es la diferencia entre las edades, no la edad del hermano. Réstele 7 a la edad de Rita." },
   right: "Su hermano tiene 7 años menos: 41 − 7 = 34 años.",
   solution: "Rita es mayor, así que su hermano es menor. Reste la diferencia: 41 − 7 = 34 años." },
  p3: { ok: "a",
   hints: { b: "x − 14 quiere decir que se bajaron 14 personas. En la historia se subieron 14 personas: sume.", c: "14x quiere decir 14 grupos iguales. En la historia se agregaron 14 personas al autobús.", d: "Las 50 personas están en el autobús al final, así que el 50 va solo en un lado: x + 14 = 50." },
   right: "Había x personas, se subieron 14 más, y ahora hay 50: x + 14 = 50. Así que x = 36.",
   solution: "Al principio había x personas, se subieron 14 más (+ 14), y ahora hay 50: x + 14 = 50. Al resolverla: x = 50 − 14 = 36 personas." },
  p4: { ok: "d",
   hints: { a: "13 es 8 + 5. La caja se repartió en 5 partes iguales, así que tenía 5 veces 8 marcadores.", b: "3 es 8 − 5. La caja se repartió en 5 partes iguales de 8 marcadores cada una.", c: "8 marcadores es lo que le tocó a una mesa, no la caja entera. Hay 5 mesas." },
   right: "x ÷ 5 = 8, así que x = 8 × 5 = 40 marcadores. Comprobación: 40 ÷ 5 = 8.",
   solution: "La caja (x) se repartió entre 5 mesas, y a cada una le tocaron 8: x ÷ 5 = 8. La inversa de dividir es multiplicar: x = 8 × 5 = 40 marcadores." }
 },
 quiz: {
  A: { ok: "d", hints: { a: "Aquí no se junta nada. Se reparte un total de 96.", b: "Restar 8 una vez no reparte las tortillas en bolsas iguales.", c: "Multiplicar da un total mayor. Aquí el total de 96 se reparte en bolsas iguales." },
   solution: "Un total (96 tortillas) se reparte en partes iguales en 8 bolsas: divida. 96 ÷ 8 = 12 tortillas en cada bolsa." },
  B: { ok: "b", hints: { a: "43 es 34 + 9. La palabra «más» puede engañarle: Lucía es mayor, así que su hermano es menor.", c: "306 es 34 × 9. No hay grupos iguales que se repitan. Compare las edades.", d: "9 es la diferencia entre las edades, no la edad del hermano." },
   solution: "Lucía tiene 9 años más, así que su hermano tiene 9 años menos: 34 − 9 = 25 años." },
  C: { ok: "c", hints: { a: "x + 65 quiere decir que recibió $65 más. Él gastó $65: quítelos.", b: "65x quiere decir 65 veces el dinero. Él gastó $65: reste.", d: "No se repartió nada en partes iguales. Él gastó $65: reste." },
   solution: "Tenía x dólares, gastó $65 (− 65), y le quedan $120: x − 65 = 120. Al resolverla: x = 120 + 65 = $185." },
  D: { ok: "a", hints: { b: "x + 15 suma $15 una sola vez. Cada boleto cuesta $15: son x grupos iguales de $15.", c: "No se quita nada. Cada boleto cuesta lo mismo: grupos iguales.", d: "Los números están en lugares equivocados. x boletos de $15 cada uno cuestan $180: 15x = 180." },
   solution: "x boletos a $15 cada uno cuestan 15 × x dólares, y el grupo pagó $180: 15x = 180. Al resolverla: x = 180 ÷ 15 = 12 boletos." },
  E: { ok: "c", hints: { a: "15 es 9 + 6. La soga se cortó en 6 pedazos iguales de 9 pies, así que mide 6 veces 9.", b: "3 es 9 − 6. Cada uno de los 6 pedazos mide 9 pies, así que la soga mide más de 9 pies.", d: "9 pies es un solo pedazo. La soga entera tiene 6 pedazos así." },
   solution: "La soga (x) se cortó en 6 pedazos iguales de 9 pies: x ÷ 6 = 9. Así que x = 9 × 6 = 54 pies." },
  F: { ok: "b", hints: { a: "$100 es menos que un mes de renta. Doce meses tienen que costar mucho más de $1,200.", c: "$1,212 es $1,200 + 12. Pagan $1,200 cada mes durante 12 meses: grupos iguales.", d: "$1,188 es menos que un mes de renta, así que no puede ser el costo de 12 meses." },
   solution: "12 meses de $1,200 cada uno: 12 × $1,200 = $14,400. Tiene sentido: es mucho más que un mes." },
  G: { ok: "a", hints: { b: "$996 también cuenta los 38 pantalones. La pregunta es solo sobre las camisas.", c: "$57 es 45 + 12. Cada una de las 45 camisas cuesta $12: grupos iguales.", d: "$456 usa los 38 pantalones. La pregunta es sobre las 45 camisas." },
   solution: "Solo importan las camisas: 45 camisas a $12 cada una. 45 × $12 = $540. Los 38 pantalones son información de sobra." },
  H: { ok: "d", hints: { a: "El número está bien, pero la unidad no. La pregunta es cuántas millas por galón.", b: "1,920 es 240 × 8. Las millas se reparten entre los galones: divida.", c: "248 es 240 + 8. Las millas se reparten entre los 8 galones: divida." },
   solution: "240 millas repartidas entre 8 galones: 240 ÷ 8 = 30. La respuesta necesita su unidad: 30 millas por galón." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-5-3.html")
