"""Crea es/matematicas/nivel-1/leccion-2-3.html a partir de math/level-1/lesson-2-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-2-3.html"); t.leccion("")
R = t.r
t.cabecera("<!-- LearnGED · Lección 2.3 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 2.3 · Multiplication and division in word problems · LearnGED</title>", "<title>Lección 2.3 · Multiplicación y división en problemas verbales · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 2 — Multiplication and division</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 2 — Multiplicación y división</p>')
R("<h1>Lesson 2.3 · Multiplication and division in word problems</h1>", "<h1>Lección 2.3 · Multiplicación y división en problemas verbales</h1>")
R('<p class="lema">Decide when to multiply and when to divide in real problems, and use the properties to calculate quickly.</p>', '<p class="lema">Decida cuándo multiplicar y cuándo dividir en problemas reales, y use las propiedades para calcular rápido.</p>')
R("Keywords · Properties</span>", "Palabras clave · Propiedades</span>")
R("<li><strong>Decide</strong> whether a word problem needs multiplication or division.</li>", "<li><strong>Decidir</strong> si un problema verbal necesita una multiplicación o una división.</li>")
R("<li><strong>Set up and solve</strong> one-step word problems with any of the four operations.</li>", "<li><strong>Plantear y resolver</strong> problemas verbales de un paso con cualquiera de las cuatro operaciones.</li>")
R("<li><strong>Use</strong> the properties of operations to make calculations easier.</li>", "<li><strong>Usar</strong> las propiedades de las operaciones para facilitar los cálculos.</li>")
R("<li><strong>Check</strong> your answer and make sure it makes sense in the situation.</li>", "<li><strong>Comprobar</strong> su respuesta y asegurarse de que tiene sentido en la situación.</li>")
R('<li><a href="#s-together">Closing Topic 2: putting it all together</a></li>', '<li><a href="#s-juntos">Cierre del Tema 2: todo junto</a></li>')
R('<li><a href="#s-keywords">Keywords: multiply or divide?</a></li>', '<li><a href="#s-palabras-clave">Palabras clave: ¿multiplicar o dividir?</a></li>')
R('<li><a href="#s-four-steps">The 4 steps, again</a></li>', '<li><a href="#s-cuatro-pasos">Los 4 pasos, otra vez</a></li>')
R('<li><a href="#s-properties">Properties as shortcuts</a></li>', '<li><a href="#s-propiedades">Las propiedades como atajos</a></li>')
# 1
R('<h2 id="s-together"><span aria-hidden="true" class="num-seccion">1</span>Closing Topic 2: putting it all together</h2>', '<h2 id="s-juntos"><span aria-hidden="true" class="num-seccion">1</span>Cierre del Tema 2: todo junto</h2>')
R("<p>In Lesson 2.1 you learned to multiply, and in Lesson 2.2 you learned to divide. Just like in Topic 1 with addition and subtraction, the challenge now is not the calculation. The challenge is to <strong>decide what to calculate</strong> when the problem comes in words.</p>",
  "<p>En la Lección 2.1 aprendió a multiplicar, y en la Lección 2.2 aprendió a dividir. Igual que en el Tema 1 con la suma y la resta, el reto ahora no es el cálculo. El reto es <strong>decidir qué calcular</strong> cuando el problema viene en palabras.</p>")
R("<p>Today's key question is: <strong>\"Do I multiply or divide?\"</strong></p>", "<p>La pregunta clave de hoy es: <strong>«¿Multiplico o divido?»</strong></p>")
R("<p>We <strong>multiply</strong> when we have several <strong>equal groups</strong> and want the total. We <strong>divide</strong> when we have a <strong>total</strong> and want to split it into equal groups, or find how many groups fit.</p>",
  "<p><strong>Multiplicamos</strong> cuando tenemos varios <strong>grupos iguales</strong> y queremos el total. <strong>Dividimos</strong> cuando tenemos un <strong>total</strong> y queremos repartirlo en grupos iguales, o hallar cuántos grupos caben.</p>")
# 2
R('<h2 id="s-keywords"><span aria-hidden="true" class="num-seccion">2</span>Keywords: multiply or divide?</h2>', '<h2 id="s-palabras-clave"><span aria-hidden="true" class="num-seccion">2</span>Palabras clave: ¿multiplicar o dividir?</h2>')
R("<p>As in Topic 1, some words in a problem are clues. Here is your reference table for the two new operations:</p>", "<p>Como en el Tema 1, algunas palabras del problema son pistas. Esta es su tabla de referencia para las dos operaciones nuevas:</p>")
R('aria-label="Keywords for multiplication and division (tabla desplazable horizontalmente)"', 'aria-label="Palabras clave de la multiplicación y la división (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Words in a problem that point to multiplication or to division</caption>', '<caption class="cap-oculto">Palabras de un problema que indican multiplicación o división</caption>')
R('<span aria-hidden="true">✖️</span> Words that point to multiplying</th><th scope="col"><span aria-hidden="true">➗</span> Words that point to dividing</th>', '<span aria-hidden="true">✖️</span> Palabras que indican multiplicar</th><th scope="col"><span aria-hidden="true">➗</span> Palabras que indican dividir</th>')
R("<tr><td>each … how many in all?</td><td>split equally, share equally</td></tr>", "<tr><td>cada … ¿cuántos en total?</td><td>repartir en partes iguales, repartir entre</td></tr>")
R("<tr><td>the total of … equal groups</td><td>how much for each person? for each group?</td></tr>", "<tr><td>el total de … grupos iguales</td><td>¿cuánto le toca a cada persona? ¿a cada grupo?</td></tr>")
R("<tr><td>times, twice, double, triple</td><td>how many groups?</td></tr>", "<tr><td>veces, el doble, el triple</td><td>¿cuántos grupos?</td></tr>")
R("<tr><td>per (with the number of groups given): $15 per hour for 8 hours</td><td>half, one third, divided by</td></tr>", "<tr><td>por (cuando se da el número de grupos): $15 por hora durante 8 horas</td><td>la mitad, la tercera parte, dividido entre</td></tr>")
R("<p>The words <strong>\"each\"</strong> and <strong>\"per\"</strong> show up in both kinds of problems. Look at these two:</p>", "<p>Las palabras <strong>«cada»</strong> y <strong>«por»</strong> aparecen en los dos tipos de problema. Fíjese en estos dos:</p>")
R("<p><em>\"Each box has 12 soaps. How many soaps are in 15 boxes?\"</em> You know the groups and want the total: <strong>multiply</strong>. 12 × 15 = 180 soaps.</p>",
  "<p><em>«Cada caja tiene 12 jabones. ¿Cuántos jabones hay en 15 cajas?»</em> Conoce los grupos y quiere el total: <strong>multiplique</strong>. 12 × 15 = 180 jabones.</p>")
R("<p><em>\"180 soaps are packed 12 in each box. How many boxes are there?\"</em> You know the total and want the groups: <strong>divide</strong>. 180 ÷ 12 = 15 boxes.</p>",
  "<p><em>«Se empacan 180 jabones, 12 en cada caja. ¿Cuántas cajas hay?»</em> Conoce el total y quiere los grupos: <strong>divida</strong>. 180 ÷ 12 = 15 cajas.</p>")
R("<p>So the safest thing is to <strong>picture the situation</strong>: am I putting equal groups together (multiply), or am I splitting a total (divide)?</p>",
  "<p>Por eso, lo más seguro es <strong>imaginar la situación</strong>: ¿estoy juntando grupos iguales (multiplicar) o estoy repartiendo un total (dividir)?</p>")
R('href="practice-2-3.html#keywords"', 'href="practica-2-3.html#palabras-clave"')
R('práctica: multiply or divide (se abre', 'práctica: multiplicar o dividir (se abre')
R('<span class="ei-titulo">Practique más: multiply or divide?</span><span class="ei-sub">Read a situation and decide if it puts equal groups together or splits a total.</span>', '<span class="ei-titulo">Practique más: ¿multiplicar o dividir?</span><span class="ei-sub">Lea una situación y decida si junta grupos iguales o reparte un total.</span>')
# 3
R('<h2 id="s-four-steps"><span aria-hidden="true" class="num-seccion">3</span>The 4 steps, again</h2>', '<h2 id="s-cuatro-pasos"><span aria-hidden="true" class="num-seccion">3</span>Los 4 pasos, otra vez</h2>')
R("<p>The 4-step method you learned in Lesson 1.3 works for any word problem, including multiplication and division:</p>", "<p>El método de 4 pasos que aprendió en la Lección 1.3 sirve para cualquier problema verbal, también de multiplicación y división:</p>")
R('<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Read and underline</strong> the numbers and what the question asks.</p><p class="paso"><span aria-hidden="true" class="n">2</span><strong>Choose the operation:</strong> am I putting equal groups together, or splitting a total?</p><p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve</strong> with the standard method.</p><p class="paso"><span aria-hidden="true" class="n">4</span><strong>Does it make sense?</strong> Check your answer and its unit. If there is a remainder, decide what to do with it.</p>',
  '<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Lea y subraye</strong> los números y lo que pide la pregunta.</p><p class="paso"><span aria-hidden="true" class="n">2</span><strong>Elija la operación:</strong> ¿estoy juntando grupos iguales o repartiendo un total?</p><p class="paso"><span aria-hidden="true" class="n">3</span><strong>Resuelva</strong> con el método estándar.</p><p class="paso"><span aria-hidden="true" class="n">4</span><strong>¿Tiene sentido?</strong> Compruebe su respuesta y su unidad. Si hay residuo, decida qué hacer con él.</p>')
R('<p class="titulo-ej">Example: a multiplication problem</p>', '<p class="titulo-ej">Ejemplo: un problema de multiplicación</p>')
R("<p><em>\"A hall has 18 rows of chairs. Each row has 24 chairs. How many chairs are there in all?\"</em></p>", "<p><em>«Un salón tiene 18 filas de sillas. Cada fila tiene 24 sillas. ¿Cuántas sillas hay en total?»</em></p>")
R('<strong>Underline:</strong> 18 rows, 24 chairs in each row. The question asks for the total number of chairs.', '<strong>Subraye:</strong> 18 filas, 24 sillas en cada fila. La pregunta pide el total de sillas.')
R('<strong>Choose:</strong> every row has 24 chairs: equal groups that come together. It is a <strong>multiplication</strong>.', '<strong>Elija:</strong> cada fila tiene 24 sillas: grupos iguales que se juntan. Es una <strong>multiplicación</strong>.')
R('<strong>Solve:</strong> 18 × 24 = <strong>432</strong>.', '<strong>Resuelva:</strong> 18 × 24 = <strong>432</strong>.')
R('<strong>Does it make sense?</strong> 432 chairs in 18 rows is reasonable. The answer is <strong>432 chairs</strong>.', '<strong>¿Tiene sentido?</strong> 432 sillas en 18 filas es razonable. La respuesta es <strong>432 sillas</strong>.')
R('<p class="titulo-ej">Example: a division problem</p>', '<p class="titulo-ej">Ejemplo: un problema de división</p>')
R("<p><em>\"A company splits 384 boxes equally among 8 trucks. How many boxes does each truck carry?\"</em></p>", "<p><em>«Una compañía reparte 384 cajas en partes iguales entre 8 camiones. ¿Cuántas cajas lleva cada camión?»</em></p>")
R('<strong>Underline:</strong> 384 boxes, 8 trucks. The question asks for the boxes in each truck.', '<strong>Subraye:</strong> 384 cajas, 8 camiones. La pregunta pide las cajas de cada camión.')
R('<strong>Choose:</strong> "splits equally" and "each truck": you split a total. It is a <strong>division</strong>.', '<strong>Elija:</strong> «reparte en partes iguales» y «cada camión»: se reparte un total. Es una <strong>división</strong>.')
R('<strong>Solve:</strong> 384 ÷ 8 = <strong>48</strong>.', '<strong>Resuelva:</strong> 384 ÷ 8 = <strong>48</strong>.')
R('<strong>Does it make sense?</strong> Each truck carries part of the total, so 48 boxes is reasonable. Check: 48 × 8 = 384 ✓. The answer is <strong>48 boxes</strong>.', '<strong>¿Tiene sentido?</strong> Cada camión lleva una parte del total, así que 48 cajas es razonable. Comprobación: 48 × 8 = 384 ✓. La respuesta es <strong>48 cajas</strong>.')
R("<h3>Practice 1 — Multiply or divide?</h3>", "<h3>Práctica 1 — ¿Multiplicar o dividir?</h3>")
R("<em>\"A pack has 12 bars of soap. How many bars are in 15 packs?\"</em> Which operation do you need?", "<em>«Un paquete trae 12 barras de jabón. ¿Cuántas barras hay en 15 paquetes?»</em> ¿Qué operación necesita?")
R('type="button">Multiply: 12 × 15</button>', 'type="button">Multiplicar: 12 × 15</button>')
R('type="button">Divide: 15 ÷ 12</button>', 'type="button">Dividir: 15 ÷ 12</button>')
R('type="button">Add: 12 + 15</button>', 'type="button">Sumar: 12 + 15</button>')
R("<h3>Practice 2 — Solve the problem</h3>", "<h3>Práctica 2 — Resuelva el problema</h3>")
R("<em>\"525 students are split equally among 7 classrooms. How many students are in each classroom?\"</em>", "<em>«Se reparten 525 estudiantes en partes iguales entre 7 salones. ¿Cuántos estudiantes hay en cada salón?»</em>")
for n in ["532", "75", "85", "3,675"]:
    R('type="button">' + n + ' students</button>', 'type="button">' + n + ' estudiantes</button>')
R('href="practice-2-3.html#four-steps"', 'href="practica-2-3.html#cuatro-pasos"')
R('práctica: the 4 steps (se abre', 'práctica: los 4 pasos (se abre')
R('<span class="ei-titulo">Practique más: the 4 steps, again</span><span class="ei-sub">Solve word problems with the 4-step method, remainders included.</span>', '<span class="ei-titulo">Practique más: los 4 pasos, otra vez</span><span class="ei-sub">Resuelva problemas verbales con el método de 4 pasos, residuos incluidos.</span>')
# 4
R('<h2 id="s-properties"><span aria-hidden="true" class="num-seccion">4</span>Properties as shortcuts</h2>', '<h2 id="s-propiedades"><span aria-hidden="true" class="num-seccion">4</span>Las propiedades como atajos</h2>')
R("<p>The properties of operations are not just theory. They are <strong>shortcuts</strong> that help you calculate faster, sometimes even in your head.</p>", "<p>Las propiedades de las operaciones no son solo teoría. Son <strong>atajos</strong> que le ayudan a calcular más rápido, a veces hasta de memoria.</p>")
R('aria-label="Properties as shortcuts (tabla desplazable horizontalmente)"', 'aria-label="Las propiedades como atajos (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Properties of multiplication, what they say, and how they help</caption>', '<caption class="cap-oculto">Propiedades de la multiplicación, qué dicen y cómo ayudan</caption>')
R('<th scope="col">Property</th><th scope="col">What it says</th><th scope="col">How it helps</th>', '<th scope="col">Propiedad</th><th scope="col">Qué dice</th><th scope="col">Cómo ayuda</th>')
R("<tr><th scope=\"row\">Commutative</th><td>The order does not change the answer. 6 × 9 = 9 × 6</td><td>Put the factors in the order that is easiest for you.</td></tr>", "<tr><th scope=\"row\">Conmutativa</th><td>El orden no cambia el resultado. 6 × 9 = 9 × 6</td><td>Ponga los factores en el orden que le resulte más fácil.</td></tr>")
R("<tr><th scope=\"row\">Associative</th><td>You can group the factors in any way. (2 × 5) × 7 = 2 × (5 × 7)</td><td>Group first the numbers that give a round number (2 × 5 = 10).</td></tr>", "<tr><th scope=\"row\">Asociativa</th><td>Puede agrupar los factores de cualquier manera. (2 × 5) × 7 = 2 × (5 × 7)</td><td>Agrupe primero los números que dan un número redondo (2 × 5 = 10).</td></tr>")
R("<tr><th scope=\"row\">Distributive</th><td>You can split a factor into parts. 25 × 4 = (20 × 4) + (5 × 4)</td><td>Turn one hard multiplication into two easy ones.</td></tr>", "<tr><th scope=\"row\">Distributiva</th><td>Puede separar un factor en partes. 25 × 4 = (20 × 4) + (5 × 4)</td><td>Convierta una multiplicación difícil en dos fáciles.</td></tr>")
R("<tr><th scope=\"row\">Zero and one</th><td>n × 0 = 0 · n × 1 = n</td><td>The answer is immediate, with no calculation.</td></tr>", "<tr><th scope=\"row\">Cero y uno</th><td>n × 0 = 0 · n × 1 = n</td><td>El resultado es inmediato, sin cálculo.</td></tr>")
R('<p class="titulo-ej">Shortcut: 25 × 4 in your head</p>', '<p class="titulo-ej">Atajo: 25 × 4 de memoria</p>')
R("With the distributive property: 25 × 4 = (20 × 4) + (5 × 4).", "Con la propiedad distributiva: 25 × 4 = (20 × 4) + (5 × 4).")
R("20 × 4 = 80, and 5 × 4 = 20.", "20 × 4 = 80, y 5 × 4 = 20.")
R("80 + 20 = <strong>100</strong>. No paper needed.", "80 + 20 = <strong>100</strong>. Sin necesidad de papel.")
R("<h3>Practice 3 — Which property is it?</h3>", "<h3>Práctica 3 — ¿Qué propiedad es?</h3>")
R("<strong>(4 × 2) × 5 = 4 × (2 × 5)</strong> is an example of which property?", "<strong>(4 × 2) × 5 = 4 × (2 × 5)</strong> es un ejemplo de ¿qué propiedad?")
R('type="button">Commutative</button>', 'type="button">Conmutativa</button>', 2)
R('type="button">Associative</button>', 'type="button">Asociativa</button>', 2)
R('type="button">Distributive</button>', 'type="button">Distributiva</button>', 2)
R('type="button">Zero property</button>', 'type="button">Propiedad del cero</button>')
R('href="practice-2-3.html#properties"', 'href="practica-2-3.html#propiedades"')
R('práctica: properties as shortcuts (se abre', 'práctica: las propiedades como atajos (se abre')
R('<span class="ei-titulo">Practique más: properties as shortcuts</span><span class="ei-sub">Use the commutative, associative, and distributive properties to calculate faster.</span>', '<span class="ei-titulo">Practique más: las propiedades como atajos</span><span class="ei-sub">Use las propiedades conmutativa, asociativa y distributiva para calcular más rápido.</span>')
# Tarea
R("<p>This is independent practice. Plan for about one hour, with your notebook open. With it, you finish Topic 2.</p>", "<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto. Con ella termina el Tema 2.</p>")
R('<li><strong>The practice page.</strong> Open the <a href="practice-2-3.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-2-3.html">página de práctica de esta lección</a> ')
R("<li><strong>Write your own problems.</strong> Write two word problems with real numbers from your work, your kitchen, or a trip: one you solve by multiplying and one you solve by dividing. Solve them the next day. Did the words you wrote really point to the right operation?</li>",
  "<li><strong>Escriba sus propios problemas.</strong> Escriba dos problemas verbales con números reales de su trabajo, su cocina o un viaje: uno que se resuelva multiplicando y otro que se resuelva dividiendo. Resuélvalos al día siguiente. ¿Las palabras que escribió de verdad indicaban la operación correcta?</li>")
R("<li><strong>In your daily life.</strong> Find a cost that repeats with multiplication (for example, gas for a month) and a split with division (for example, a budget across the days of the week).</li>",
  "<li><strong>En su vida diaria.</strong> Busque un gasto que se repite, con multiplicación (por ejemplo, la gasolina de un mes), y un reparto, con división (por ejemplo, un presupuesto entre los días de la semana).</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> without a calculator and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> sin calculadora y pulse <strong>Revisar mis respuestas</strong>.")
R("<em>\"A store received 9 boxes, and each box has 48 items. How many items did it receive?\"</em> Which operation do you use?", "<em>«Una tienda recibió 9 cajas, y cada caja trae 48 artículos. ¿Cuántos artículos recibió?»</em> ¿Qué operación usa?")
R("<em>\"672 bottles are split equally into 6 boxes. How many bottles go in each box?\"</em> Which operation do you use?", "<em>«Se reparten 672 botellas en partes iguales en 6 cajas. ¿Cuántas botellas van en cada caja?»</em> ¿Qué operación usa?")
R('type="button">Multiplication</button><button class="opcion" data-k="b" type="button">Division</button>', 'type="button">Multiplicación</button><button class="opcion" data-k="b" type="button">División</button>', 2)
R("<em>\"A worker earns $128 a day. How much does the worker earn in 6 days?\"</em>", "<em>«Un trabajador gana $128 al día. ¿Cuánto gana en 6 días?»</em>")
R("<em>\"A box of 96 pencils is split equally among 8 students. How many pencils does each student get?\"</em>", "<em>«Una caja de 96 lápices se reparte en partes iguales entre 8 estudiantes. ¿Cuántos lápices recibe cada estudiante?»</em>")
for n in ["10", "14", "104", "12"]:
    R('type="button">' + n + ' pencils</button>', 'type="button">' + n + ' lápices</button>')
R("Which phrase points to <strong>division</strong>?", "¿Qué frase indica <strong>división</strong>?")
R('type="button">"for each box"</button><button class="opcion" data-k="b" type="button">"double"</button><button class="opcion" data-k="c" type="button">"split equally"</button><button class="opcion" data-k="d" type="button">"at a rate of"</button>',
  'type="button">«por cada caja»</button><button class="opcion" data-k="b" type="button">«el doble»</button><button class="opcion" data-k="c" type="button">«repartir en partes iguales»</button><button class="opcion" data-k="d" type="button">«a razón de»</button>')
R("<strong>7 × 5 = 5 × 7</strong> is an example of which property?", "<strong>7 × 5 = 5 × 7</strong> es un ejemplo de ¿qué propiedad?")
R('type="button">One property</button>', 'type="button">Propiedad del uno</button>')
R("<em>\"A bus carries 52 people. Each person paid $3. How much money was collected in all?\"</em>", "<em>«Un autobús lleva 52 personas. Cada persona pagó $3. ¿Cuánto dinero se recogió en total?»</em>")
R("<em>\"A family saves $150 each month. How much will it save in one year (12 months)?\"</em>", "<em>«Una familia ahorra $150 cada mes. ¿Cuánto ahorrará en un año (12 meses)?»</em>")
# Lista
R('aria-label="Self-check checklist for word problems with multiplication and division (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de problemas verbales con multiplicación y división (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: solving word problems ', '<caption class="cap-oculto">Lista de autoevaluación: resolver problemas verbales ')
R('<tr><th scope="row">Choose the operation</th><td>I tell multiplication and division apart with confidence, and I can say why.</td><td>I choose the right operation most of the time.</td><td>I depend only on keywords, or I guess.</td></tr>',
  '<tr><th scope="row">Elegir la operación</th><td>Distingo con seguridad la multiplicación de la división, y sé decir por qué.</td><td>Elijo la operación correcta la mayoría de las veces.</td><td>Dependo solo de las palabras clave, o adivino.</td></tr>')
R('<tr><th scope="row">Set up the operation</th><td>I write the operation with the numbers in the right order.</td><td>I set it up correctly most of the time.</td><td>I switch the numbers (for example, 8 ÷ 384 instead of 384 ÷ 8).</td></tr>',
  '<tr><th scope="row">Plantear la operación</th><td>Escribo la operación con los números en el orden correcto.</td><td>La planteo bien la mayoría de las veces.</td><td>Invierto los números (por ejemplo, 8 ÷ 384 en vez de 384 ÷ 8).</td></tr>')
R('<tr><th scope="row">Calculate</th><td>I calculate with no mistakes and use properties as shortcuts.</td><td>I calculate well, with a small mistake now and then.</td><td>I make mistakes in the steps.</td></tr>',
  '<tr><th scope="row">Calcular</th><td>Calculo sin errores y uso las propiedades como atajos.</td><td>Calculo bien, con algún error pequeño de vez en cuando.</td><td>Me equivoco en los pasos.</td></tr>')
R('<tr><th scope="row">Check and explain</th><td>I check with the opposite operation and give the answer with its unit.</td><td>I give the answer with its unit.</td><td>I give only a number, with no unit and no check.</td></tr>',
  '<tr><th scope="row">Comprobar y explicar</th><td>Compruebo con la operación contraria y doy la respuesta con su unidad.</td><td>Doy la respuesta con su unidad.</td><td>Doy solo un número, sin unidad y sin comprobar.</td></tr>')
# Cierre
R("<p>With this lesson you finish <strong>Topic 2 · Multiplication and division</strong>. You can now use all four operations with whole numbers and solve word problems with any of them.</p>",
  "<p>Con esta lección termina el <strong>Tema 2 · Multiplicación y división</strong>. Ya sabe usar las cuatro operaciones con números enteros y resolver problemas verbales con cualquiera de ellas.</p>")
R("<p>In <strong>Topic 3 · Decimals</strong> you will take a very useful step for daily life: working with the numbers you see in prices and money. <strong>Lesson 3.1</strong> teaches you to read, write, compare, and round decimals. From there, you will also start using the TI-30XS calculator to check your work.</p>",
  "<p>En el <strong>Tema 3 · Decimales</strong> dará un paso muy útil para la vida diaria: trabajar con los números que ve en los precios y el dinero. La <strong>Lección 3.1</strong> le enseña a leer, escribir, comparar y redondear decimales. A partir de ahí, también empezará a usar la calculadora TI-30XS para comprobar su trabajo.</p>")
R('Next: <a href="lesson-3-1.html">Lesson 3.1 · Decimals: read, write, compare, and round</a>', 'Siguiente: <a href="leccion-3-1.html">Lección 3.1 · Decimales: leer, escribir, comparar y redondear</a>')
R("""<dt>equal groups</dt><dd>Groups that all have the same number of things. 15 packs of 12 soaps are 15 equal groups.</dd>
<dt>split equally (share equally)</dt><dd>To divide a total so that every group gets the same amount.</dd>
<dt>per</dt><dd>For each. "$15 per hour" means $15 for each hour.</dd>
<dt>double, triple</dt><dd>Two times, three times a number. The triple of 35 is 3 × 35 = 105.</dd>
<dt>shortcut</dt><dd>A faster way to get the same answer, like using a property to calculate in your head.</dd>""",
"""<dt>grupos iguales</dt><dd>Grupos que tienen todos la misma cantidad de cosas. 15 paquetes de 12 jabones son 15 grupos iguales.</dd>
<dt>repartir en partes iguales</dt><dd>Dividir un total de modo que a cada grupo le toque la misma cantidad.</dd>
<dt>por</dt><dd>Por cada uno. «$15 por hora» quiere decir $15 por cada hora.</dd>
<dt>el doble, el triple</dt><dd>Dos veces, tres veces un número. El triple de 35 es 3 × 35 = 105.</dd>
<dt>atajo</dt><dd>Una forma más rápida de llegar al mismo resultado, como usar una propiedad para calcular de memoria.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 2 · Lesson 2.3</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 2 · Lección 2.3</p>")
t.js('''{
 next: "Lección 3.1",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "a",
   hints: { b: "No está repartiendo un total. Cada paquete suma 12 barras más.", c: "Sumar 12 + 15 mezcla barras y paquetes. Tiene 15 grupos iguales de 12." },
   right: "15 grupos iguales de 12: se multiplica. 12 × 15 = 180 barras.",
   solution: "Hay 15 paquetes, y cada uno trae 12 barras: 15 grupos iguales que se juntan. Se multiplica: 12 × 15 = 180 barras." },
  p2: { ok: "b",
   hints: { a: "«Repartir en partes iguales» quiere decir dividir, no sumar.", c: "Compruebe: 85 × 7 = 595, no 525.", d: "Está repartiendo un total, así que divida; no multiplique." },
   right: "Se reparte un total: 525 ÷ 7 = 75. Comprobación: 75 × 7 = 525 ✓",
   solution: "Se reparte un total en partes iguales: 525 ÷ 7. 52 ÷ 7 = 7, residuo 3. Baje el 5: 35 ÷ 7 = 5. Cada salón tiene 75 estudiantes. Comprobación: 75 × 7 = 525 ✓" },
  p3: { ok: "b",
   hints: { a: "El orden de los números es el mismo en los dos lados. ¿Qué cambió?", c: "Ningún factor se separó en partes. ¿Qué cambió?", d: "Aquí no hay ningún cero." },
   right: "Los números quedan en el mismo orden, pero cambia la agrupación. Agrupar primero 2 × 5 = 10 lo hace fácil: 4 × 10 = 40.",
   solution: "Fíjese en los paréntesis: cambió la agrupación, no el orden. Esa es la propiedad asociativa. Ayuda: 2 × 5 = 10, y 4 × 10 = 40." }
 },
 quiz: {
  A: { ok: "a", hints: { b: "Conoce el número de grupos y el tamaño de cada grupo, y quiere el total." },
   solution: "Se juntan 9 grupos iguales de 48 y quiere el total: se multiplica. 9 × 48 = 432 artículos." },
  B: { ok: "b", hints: { a: "Conoce el total y lo reparte en grupos iguales." },
   solution: "Se reparte un total en grupos iguales: se divide. 672 ÷ 6 = 112 botellas en cada caja." },
  C: { ok: "c", hints: { a: "6 días de $128 son grupos iguales. Multiplique; no sume.", b: "Unidades: 6 × 8 = 48, así que lleva 4. ¿Lo sumó en las decenas?", d: "Revise las decenas y las centenas. ¿Sumó todo lo que llevaba?" },
   solution: "6 grupos iguales de $128: 128 × 6. Unidades: 6 × 8 = 48, escriba 8 y lleve 4. Decenas: 6 × 2 = 12, más 4 = 16, escriba 6 y lleve 1. Centenas: 6 × 1 = 6, más 1 = 7. El trabajador gana $768." },
  D: { ok: "d", hints: { a: "Compruebe: 10 × 8 = 80, no 96.", b: "Compruebe: 14 × 8 = 112, que es más que 96.", c: "«Repartir en partes iguales» quiere decir dividir, no sumar." },
   solution: "Se reparte un total: 96 ÷ 8 = 12 lápices. Comprobación: 12 × 8 = 96 ✓" },
  E: { ok: "c", hints: { a: "«Por cada» puede ir con las dos operaciones. ¿Qué frase siempre quiere decir repartir un total?", b: "«El doble» quiere decir dos veces: multiplicar.", d: "«A razón de» casi siempre quiere decir que se repite una cantidad: multiplicar." },
   solution: "«Repartir en partes iguales» quiere decir que se divide un total en grupos iguales." },
  F: { ok: "b", hints: { a: "La propiedad asociativa trata de cómo se agrupan tres factores.", c: "La propiedad distributiva separa un factor en partes.", d: "Aquí no hay ningún 1." },
   solution: "Cambió el orden de los factores, y el producto no cambió. Esa es la propiedad conmutativa." },
  G: { ok: "d", hints: { a: "52 personas pagaron $3 cada una: grupos iguales. Multiplique; no sume.", b: "Compruebe: 3 × 2 = 6 y 3 × 50 = 150.", c: "No está repartiendo un total. Cada persona suma $3: multiplique." },
   solution: "52 grupos iguales de $3: 52 × 3 = 156. Atajo: (50 × 3) + (2 × 3) = 150 + 6. Recogieron $156." },
  H: { ok: "a", hints: { b: "12 meses de $150 son grupos iguales. Multiplique; no sume.", c: "Eso son 10 meses. Un año tiene 12 meses.", d: "Compruebe: (150 × 10) + (150 × 2)." },
   solution: "12 grupos iguales de $150: 150 × 12. Atajo: (150 × 10) + (150 × 2) = 1,500 + 300 = 1,800. La familia ahorrará $1,800." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-2-3.html")
