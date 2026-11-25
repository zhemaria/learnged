"""Crea es/matematicas/nivel-1/leccion-4-2.html a partir de math/level-1/lesson-4-2.html."""
from traduce import Traductor, F
t = Traductor("math/level-1/lesson-4-2.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 4.2 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 4.2 · Adding and subtracting fractions · LearnGED</title>", "<title>Lección 4.2 · Suma y resta de fracciones · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 4 — Fractions</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 4 — Fracciones</p>')
R("<h1>Lesson 4.2 · Adding and subtracting fractions</h1>", "<h1>Lección 4.2 · Suma y resta de fracciones</h1>")
R('<p class="lema">Join and take away parts of a whole. The secret is simple: the parts must be the same size.</p>', '<p class="lema">Juntar y quitar partes de un entero. El secreto es sencillo: las partes tienen que ser del mismo tamaño.</p>')
R("Fraction bars</span>", "Barras de fracciones</span>")
R("<li><strong>Explain</strong> why only the numerators are added or subtracted.</li>", "<li><strong>Explicar</strong> por qué solo se suman o se restan los numeradores.</li>")
R("<li><strong>Add and subtract</strong> fractions with the same denominator.</li>", "<li><strong>Sumar y restar</strong> fracciones con el mismo denominador.</li>")
R("<li><strong>Find</strong> a common denominator for two fractions.</li>", "<li><strong>Hallar</strong> un denominador común para dos fracciones.</li>")
R("<li><strong>Add and subtract</strong> fractions with different denominators.</li>", "<li><strong>Sumar y restar</strong> fracciones con denominadores distintos.</li>")
R("<li><strong>Simplify</strong> the result, and write it as a mixed number when it is more than 1.</li>", "<li><strong>Simplificar</strong> el resultado y escribirlo como número mixto cuando es más que 1.</li>")
R('<li><a href="#s-why">Why the denominator matters</a></li>', '<li><a href="#s-por-que">Por qué importa el denominador</a></li>')
R('<li><a href="#s-same">The same denominator</a></li>', '<li><a href="#s-mismo">El mismo denominador</a></li>')
R('<li><a href="#s-different">Different denominators</a></li>', '<li><a href="#s-distintos">Denominadores distintos</a></li>')
R('<li><a href="#s-simplify">Simplify the result</a></li>', '<li><a href="#s-simplificar">Simplificar el resultado</a></li>')
# 1
R('<h2 id="s-why"><span aria-hidden="true" class="num-seccion">1</span>Why the denominator matters</h2>', '<h2 id="s-por-que"><span aria-hidden="true" class="num-seccion">1</span>Por qué importa el denominador</h2>')
R("<p>In Lesson 4.1 you learned that the <strong>denominator</strong> tells the <strong>size</strong> of the parts, and the <strong>numerator</strong> tells <strong>how many</strong> parts you have.</p>", "<p>En la Lección 4.1 aprendió que el <strong>denominador</strong> dice el <strong>tamaño</strong> de las partes, y el <strong>numerador</strong> dice <strong>cuántas</strong> partes tiene.</p>")
R("<p>Think about money. Two quarters plus one quarter are three quarters. You count the coins, and they are still <strong>quarters</strong>: putting them together does not change the size of each coin. Fractions work the same way:</p>",
  "<p>Piense en el dinero. Dos monedas de 25 centavos más una son tres monedas de 25 centavos: tres <strong>cuartos</strong> de dólar. Usted cuenta las monedas, y siguen siendo <strong>cuartos</strong>: juntarlas no cambia el tamaño de cada moneda. Las fracciones funcionan igual:</p>")
R("2 fourths + 1 fourth = 3 fourths, &nbsp; or &nbsp; ", "2 cuartos + 1 cuarto = 3 cuartos, &nbsp; o &nbsp; ")
R('<span class="etiqueta et-verde">The key idea</span>', '<span class="etiqueta et-verde">La idea clave</span>')
R("<p>To add or subtract fractions, the parts must be <strong>the same size</strong> (the same denominator). Then you add or subtract only the <strong>numerators</strong>. The denominator stays the same.</p>", "<p>Para sumar o restar fracciones, las partes tienen que ser <strong>del mismo tamaño</strong> (el mismo denominador). Entonces se suman o se restan solo los <strong>numeradores</strong>. El denominador se queda igual.</p>")
R("<p>But what if the parts are different sizes, like halves and thirds? You cannot count them together until you cut them into parts of the same size. You already know how: with <strong>equivalent fractions</strong>.</p>", "<p>¿Y si las partes son de tamaños distintos, como medios y tercios? No se pueden contar juntas hasta cortarlas en partes del mismo tamaño. Usted ya sabe cómo: con <strong>fracciones equivalentes</strong>.</p>")
# 2
R('<h2 id="s-same"><span aria-hidden="true" class="num-seccion">2</span>The same denominator</h2>', '<h2 id="s-mismo"><span aria-hidden="true" class="num-seccion">2</span>El mismo denominador</h2>')
R("<p>When the denominators are the same, add (or subtract) the numerators and keep the denominator.</p>", "<p>Cuando los denominadores son iguales, sume (o reste) los numeradores y deje el denominador.</p>")
t.todas('<p class="titulo-ej">Example: ', '<p class="titulo-ej">Ejemplo: ')
R("The denominators are the same (5): the parts are fifths.", "Los denominadores son iguales (5): las partes son quintos.")
R("Add the numerators: 2 + 1 = 3.", "Sume los numeradores: 2 + 1 = 3.")
R(". The parts are still fifths.</p>", ". Las partes siguen siendo quintos.</p>")
R('aria-label="A bar divided into 5 equal parts: 2 parts in dark purple and 1 part in light purple are shaded. Together they are 3 fifths."', 'aria-label="Una barra dividida en 5 partes iguales: 2 partes en morado oscuro y 1 parte en morado claro están sombreadas. Juntas son 3 quintos."')
R("<strong>2 fifths</strong> (dark) + <strong>1 fifth</strong> (light) = <strong>3 fifths</strong>", "<strong>2 quintos</strong> (oscuro) + <strong>1 quinto</strong> (claro) = <strong>3 quintos</strong>")
R(f"<p>Subtracting works the same way. A board is {F(5,8)} inch thick, and you sand off {F(2,8)} inch. Now it is 5 − 2 = 3 eighths: {F(3,8)} inch thick.</p>", f"<p>Restar funciona igual. Una tabla tiene {F(5,8)} de pulgada de grueso, y usted le lija {F(2,8)} de pulgada. Ahora tiene 5 − 2 = 3 octavos: {F(3,8)} de pulgada de grueso.</p>")
R(f"<p><strong>Never add the denominators.</strong> {F(2,5)} + {F(1,5)} is <strong>not</strong> {F(3,10)}. Here is a quick way to catch that mistake: {F(3,10)} is <strong>less</strong> than the {F(2,5)} you started with. If you add something to {F(2,5)}, the answer must be <strong>more</strong> than {F(2,5)}. Always ask yourself if your answer makes sense.</p>",
  f"<p><strong>Nunca sume los denominadores.</strong> {F(2,5)} + {F(1,5)} <strong>no</strong> es {F(3,10)}. Así se descubre rápido ese error: {F(3,10)} es <strong>menos</strong> que los {F(2,5)} del principio. Si le suma algo a {F(2,5)}, el resultado tiene que ser <strong>más</strong> que {F(2,5)}. Pregúntese siempre si su respuesta tiene sentido.</p>")
R("<h3>Practice 1 — Add with the same denominator</h3>", "<h3>Práctica 1 — Sumar con el mismo denominador</h3>")
R(f"What is {F(3,8)} + {F(2,8)}?", f"¿Cuánto es {F(3,8)} + {F(2,8)}?")
R("<h3>Practice 2 — Subtract with the same denominator</h3>", "<h3>Práctica 2 — Restar con el mismo denominador</h3>")
R(f"What is {F(7,9)} − {F(4,9)}?", f"¿Cuánto es {F(7,9)} − {F(4,9)}?")
R('href="practice-4-2.html#same-denominator"', 'href="practica-4-2.html#mismo-denominador"')
R('práctica: the same denominator (se abre', 'práctica: el mismo denominador (se abre')
R('<span class="ei-titulo">Practique más: the same denominator</span><span class="ei-sub">Join and take away parts with the bars, and add or subtract fractions with the same denominator.</span>', '<span class="ei-titulo">Practique más: el mismo denominador</span><span class="ei-sub">Junte y quite partes con las barras, y sume o reste fracciones con el mismo denominador.</span>')
# 3
R('<h2 id="s-different"><span aria-hidden="true" class="num-seccion">3</span>Different denominators</h2>', '<h2 id="s-distintos"><span aria-hidden="true" class="num-seccion">3</span>Denominadores distintos</h2>')
R("<p>When the denominators are different, the parts are different sizes. First, change the fractions to <strong>equivalent fractions with the same denominator</strong> (a <strong>common denominator</strong>). Then add or subtract the numerators.</p>", "<p>Cuando los denominadores son distintos, las partes son de tamaños distintos. Primero, convierta las fracciones en <strong>fracciones equivalentes con el mismo denominador</strong> (un <strong>denominador común</strong>). Después sume o reste los numeradores.</p>")
R("<h3>How to find a common denominator</h3>", "<h3>Cómo hallar un denominador común</h3>")
R("<p>Go through the <strong>multiples of the larger denominator</strong> (2 times, 3 times, …) until you find one that the smaller denominator also goes into. If you do not find one quickly, <strong>multiplying the two denominators always works</strong>. You may get bigger numbers, but you can simplify at the end.</p>",
  "<p>Recorra los <strong>múltiplos del denominador mayor</strong> (2 veces, 3 veces, …) hasta encontrar uno en el que también quepa el denominador menor. Si no lo encuentra rápido, <strong>multiplicar los dos denominadores siempre sirve</strong>. Puede que le salgan números más grandes, pero puede simplificar al final.</p>")
R("Find a common denominator. Multiples of 3: 3, 6, … The number 2 does not go into 3, but it does go into 6. The common denominator is <strong>6</strong>.", "Busque un denominador común. Múltiplos de 3: 3, 6, … El 2 no cabe exacto en 3, pero sí en 6. El denominador común es <strong>6</strong>.")
R("<strong>Paso 2.</strong> Change each fraction to sixths: ", "<strong>Paso 2.</strong> Convierta cada fracción en sextos: ")
R(f" (× 3), and {F(1,3)}", f" (× 3), y {F(1,3)}")
R("Now the parts are the same size. Add the numerators: 3 + 2 = 5.", "Ahora las partes son del mismo tamaño. Sume los numeradores: 3 + 2 = 5.")
R('aria-label="A bar divided into 2 equal parts with 1 part shaded: one half."', 'aria-label="Una barra dividida en 2 partes iguales con 1 parte sombreada: un medio."')
R('aria-label="A bar of the same size divided into 3 equal parts with 1 part shaded: one third."', 'aria-label="Una barra del mismo tamaño dividida en 3 partes iguales con 1 parte sombreada: un tercio."')
R('aria-label="A bar of the same size divided into 6 equal parts: 3 sixths in dark purple (the half) and 2 sixths in light purple (the third). Together they are 5 sixths."', 'aria-label="Una barra del mismo tamaño dividida en 6 partes iguales: 3 sextos en morado oscuro (el medio) y 2 sextos en morado claro (el tercio). Juntos son 5 sextos."')
R("Cut into sixths, the half is <strong>3 sixths</strong> and the third is <strong>2 sixths</strong>: together, <strong>5 sixths</strong>.", "Cortado en sextos, el medio es <strong>3 sextos</strong> y el tercio es <strong>2 sextos</strong>: juntos, <strong>5 sextos</strong>.")
R(" (inches on a ruler)</p>", " (pulgadas en una regla)</p>")
R("8 is a multiple of 4 (4 × 2 = 8). The common denominator is <strong>8</strong>.", "8 es múltiplo de 4 (4 × 2 = 8). El denominador común es <strong>8</strong>.")
R(f"<strong>Paso 2.</strong> Change {F(3,4)} to eighths: ", f"<strong>Paso 2.</strong> Convierta {F(3,4)} en octavos: ")
R(f". The {F(1,8)} stays as it is.", f". El {F(1,8)} se queda como está.")
R("Subtract the numerators: 6 − 1 = 5.", "Reste los numeradores: 6 − 1 = 5.")
R(f" = {F(5,8)} inch.</p>", f" = {F(5,8)} de pulgada.</p>")
R(f"<p>The calculator adds fractions and shows the answer in simplest form. To check {F(1,2)} + {F(1,3)}:</p>", f"<p>La calculadora suma fracciones y muestra el resultado en su forma más simple. Para comprobar {F(1,2)} + {F(1,3)}:</p>")
R('<li>Press <span class="tecla">n/d</span>, type <span class="tecla num">1</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">2</span>, and leave with <span class="tecla">►</span>.</li>', '<li>Pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">1</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">2</span> y salga con <span class="tecla">►</span>.</li>')
R('<li>Press <span class="tecla">+</span>.</li>', '<li>Pulse <span class="tecla">+</span>.</li>')
R('<li>Press <span class="tecla">n/d</span>, type <span class="tecla num">1</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">3</span>, and leave with <span class="tecla">►</span>.</li>', '<li>Pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">1</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">3</span> y salga con <span class="tecla">►</span>.</li>')
R('<li>Press <span class="tecla">enter</span>. The screen shows ', '<li>Pulse <span class="tecla">enter</span>. La pantalla muestra ')
R("<p>Work it out on paper first, then check. On the GED you will need to know the steps, not only the answer.</p>", "<p>Resuélvalo primero en papel y después compruebe. En el GED necesitará saber los pasos, no solo el resultado.</p>")
R("<h3>Practice 3 — Find a common denominator</h3>", "<h3>Práctica 3 — Hallar un denominador común</h3>")
R(f"To add {F(1,4)} + {F(1,6)}, what is the smallest common denominator?", f"Para sumar {F(1,4)} + {F(1,6)}, ¿cuál es el denominador común más pequeño?")
R('type="button">24 is the only one possible</button>', 'type="button">24 es el único posible</button>')
R("<h3>Practice 4 — Add with different denominators</h3>", "<h3>Práctica 4 — Sumar con denominadores distintos</h3>")
R(f"What is {F(1,2)} + {F(1,4)}?", f"¿Cuánto es {F(1,2)} + {F(1,4)}?")
R('href="practice-4-2.html#different-denominators"', 'href="practica-4-2.html#denominadores-distintos"')
R('práctica: different denominators (se abre', 'práctica: denominadores distintos (se abre')
R('<span class="ei-titulo">Practique más: different denominators</span><span class="ei-sub">See each step: the common denominator, the equivalent fractions, and the result with bars.</span>', '<span class="ei-titulo">Practique más: denominadores distintos</span><span class="ei-sub">Vea cada paso: el denominador común, las fracciones equivalentes y el resultado con barras.</span>')
R('href="lesson-4-1-gcf-lcm.html#s-lcm" aria-label="Open the complement: the least common multiple (LCM)"', 'href="leccion-4-1-mcd-mcm.html#s-mcm" aria-label="Abrir el complemento: el mínimo común múltiplo (MCM)"')
R('<span class="ei-titulo">The smallest common denominator is the LCM</span><span class="ei-sub">The least common multiple (LCM) of the two denominators is the smallest common denominator. Review how to find it in the complement to Lesson 4.1.</span><span class="ei-cta">Open the complement <span aria-hidden="true">›</span></span>',
  '<span class="ei-titulo">El denominador común más pequeño es el MCM</span><span class="ei-sub">El mínimo común múltiplo (MCM) de los dos denominadores es el denominador común más pequeño. Repase cómo hallarlo en el complemento de la Lección 4.1.</span><span class="ei-cta">Abrir el complemento <span aria-hidden="true">›</span></span>')
# 4
R('<h2 id="s-simplify"><span aria-hidden="true" class="num-seccion">4</span>Simplify the result</h2>', '<h2 id="s-simplificar"><span aria-hidden="true" class="num-seccion">4</span>Simplificar el resultado</h2>')
R("<p>After you add or subtract, look at the answer. If it can be simplified, simplify it, just as you learned in Lesson 4.1.</p>", "<p>Después de sumar o restar, mire el resultado. Si se puede simplificar, simplifíquelo, como aprendió en la Lección 4.1.</p>")
R("<strong>Paso 1.</strong> Same denominator: 1 + 1 = 2. So ", "<strong>Paso 1.</strong> Mismo denominador: 1 + 1 = 2. Así que ")
R("2 and 6 can both be divided by 2: ", "2 y 6 se pueden dividir los dos entre 2: ")
R("<h3>When the answer is more than 1</h3>", "<h3>Cuando el resultado es más que 1</h3>")
R(f"<p>Sometimes the numerator ends up greater than the denominator. For example, {F(3,4)} + {F(2,4)} = {F(5,4)}. A fraction like {F(5,4)} is called an <strong>improper fraction</strong>: it is more than one whole.</p>",
  f"<p>A veces el numerador queda mayor que el denominador. Por ejemplo, {F(3,4)} + {F(2,4)} = {F(5,4)}. Una fracción como {F(5,4)} se llama <strong>fracción impropia</strong>: es más que un entero.</p>")
R('aria-label="A bar divided into 4 equal parts, all 4 shaded: one whole."', 'aria-label="Una barra dividida en 4 partes iguales, las 4 sombreadas: un entero."')
R('aria-label="A second bar of the same size divided into 4 equal parts with 1 part shaded: one fourth more."', 'aria-label="Una segunda barra del mismo tamaño dividida en 4 partes iguales con 1 parte sombreada: un cuarto más."')
R(f"<p>Four fourths make <strong>one whole</strong>, and there is <strong>one fourth</strong> left over. So {F(5,4)} is the same as 1 and {F(1,4)}, written <strong>1&nbsp;{F(1,4)}</strong>. A number like this, with a whole number and a fraction, is called a <strong>mixed number</strong>. To find it, divide: 5 ÷ 4 = 1 with remainder 1.</p>",
  f"<p>Cuatro cuartos forman <strong>un entero</strong>, y sobra <strong>un cuarto</strong>. Así que {F(5,4)} es lo mismo que 1 y {F(1,4)}, que se escribe <strong>1&nbsp;{F(1,4)}</strong>. Un número así, con un número entero y una fracción, se llama <strong>número mixto</strong>. Para hallarlo, divida: 5 ÷ 4 = 1, residuo 1.</p>")
R('<span class="etiqueta et-verde">On the GED</span>', '<span class="etiqueta et-verde">En el GED</span>')
R(f"<p>The answer choices are almost always in <strong>simplest form</strong>. If your answer is {F(3,6)} and you do not see it among the choices, simplify it: look for {F(1,2)}.</p>", f"<p>Las opciones de respuesta casi siempre están en su <strong>forma más simple</strong>. Si su respuesta es {F(3,6)} y no la ve entre las opciones, simplifíquela: busque {F(1,2)}.</p>")
R('href="practice-4-2.html#simplify-result"', 'href="practica-4-2.html#simplificar-resultado"')
R('práctica: simplify the result (se abre', 'práctica: simplificar el resultado (se abre')
R('<span class="ei-titulo">Practique más: simplify the result</span><span class="ei-sub">Add or subtract, then simplify, and write the result as a mixed number when it is more than 1.</span>', '<span class="ei-titulo">Practique más: simplificar el resultado</span><span class="ei-sub">Sume o reste, después simplifique, y escriba el resultado como número mixto cuando es más que 1.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-4-2.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-4-2.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Write and solve ten operations: five with the same denominator and five with different denominators. Mix additions and subtractions. Simplify each answer, and write any improper fraction as a mixed number. Then check each one: does the answer make sense? A sum must be more than each fraction you added.</li>",
  "<li><strong>Papel y lápiz.</strong> Escriba y resuelva diez operaciones: cinco con el mismo denominador y cinco con denominadores distintos. Mezcle sumas y restas. Simplifique cada resultado, y escriba toda fracción impropia como número mixto. Después revise cada una: ¿el resultado tiene sentido? Una suma tiene que ser más que cada fracción que sumó.</li>")
R(f"<li><strong>In your day.</strong> You spend {F(1,4)} hour on the bus, {F(1,2)} hour cooking, and {F(1,3)} hour helping with homework. How many hours is that in all? Write the answer as a mixed number, and then in hours and minutes. (Hint: the common denominator is 12, and 1 hour = 60 minutes.)</li>",
  f"<li><strong>En su día.</strong> Pasa {F(1,4)} de hora en el autobús, {F(1,2)} hora cocinando y {F(1,3)} de hora ayudando con la tarea. ¿Cuántas horas son en total? Escriba el resultado como número mixto, y después en horas y minutos. (Pista: el denominador común es 12, y 1 hora = 60 minutos.)</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("When you add two fractions with the <strong>same denominator</strong>, what happens to the denominator?", "Cuando suma dos fracciones con el <strong>mismo denominador</strong>, ¿qué pasa con el denominador?")
R('type="button">It stays the same.</button><button class="opcion" data-k="b" type="button">The two denominators are added.</button><button class="opcion" data-k="c" type="button">The two denominators are multiplied.</button><button class="opcion" data-k="d" type="button">It becomes the sum of the numerators.</button>',
  'type="button">Se queda igual.</button><button class="opcion" data-k="b" type="button">Se suman los dos denominadores.</button><button class="opcion" data-k="c" type="button">Se multiplican los dos denominadores.</button><button class="opcion" data-k="d" type="button">Se vuelve la suma de los numeradores.</button>')
R(f"What is {F(2,7)} + {F(3,7)}?", f"¿Cuánto es {F(2,7)} + {F(3,7)}?")
R(f"What is {F(5,6)} − {F(2,6)}, in simplest form?", f"¿Cuánto es {F(5,6)} − {F(2,6)}, en su forma más simple?")
R(f"To add {F(1,3)} + {F(1,6)}, what is the smallest common denominator?", f"Para sumar {F(1,3)} + {F(1,6)}, ¿cuál es el denominador común más pequeño?")
R(f"What is {F(1,2)} + {F(1,3)}?", f"¿Cuánto es {F(1,2)} + {F(1,3)}?")
R(f"What is {F(3,4)} − {F(1,8)}?", f"¿Cuánto es {F(3,4)} − {F(1,8)}?")
R(f"What is the simplest form of {F(4,8)}?", f"¿Cuál es la forma más simple de {F(4,8)}?")
R(f"Rosa reads for {F(1,4)} hour and then studies for {F(1,2)} hour. How long is that in all?", f"Rosa lee {F(1,4)} de hora y después estudia {F(1,2)} hora. ¿Cuánto tiempo es en total?")
t.todas("</span> hour</button>", "</span> de hora</button>")
# Lista
R('aria-label="Self-check checklist for adding and subtracting fractions (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de suma y resta de fracciones (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for adding and subtracting fractions ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas para sumar y restar fracciones ')
R('<tr><th scope="row">Add and subtract with the same denominator</th><td>I add or subtract only the numerators, and I can explain why.</td><td>I get it right, but sometimes I am tempted to add the denominators.</td><td>I add or subtract the denominators too.</td></tr>',
  '<tr><th scope="row">Sumar y restar con el mismo denominador</th><td>Sumo o resto solo los numeradores, y sé explicar por qué.</td><td>Lo hago bien, pero a veces me tienta sumar los denominadores.</td><td>También sumo o resto los denominadores.</td></tr>')
R('<tr><th scope="row">Find a common denominator</th><td>I find the smallest one quickly.</td><td>I find one that works, but not always the smallest.</td><td>I add the denominators, or I do not know where to start.</td></tr>',
  '<tr><th scope="row">Hallar un denominador común</th><td>Hallo rápido el más pequeño.</td><td>Hallo uno que sirve, pero no siempre el más pequeño.</td><td>Sumo los denominadores, o no sé por dónde empezar.</td></tr>')
R('<tr><th scope="row">Add and subtract with different denominators</th><td>I change both fractions and operate with no mistakes.</td><td>I find the common denominator, but I make mistakes when I change the numerators.</td><td>I operate without making the denominators the same.</td></tr>',
  '<tr><th scope="row">Sumar y restar con denominadores distintos</th><td>Convierto las dos fracciones y opero sin errores.</td><td>Hallo el denominador común, pero me equivoco al cambiar los numeradores.</td><td>Opero sin igualar los denominadores.</td></tr>')
R('<tr><th scope="row">Simplify and check the result</th><td>I always simplify, write mixed numbers, and check that the answer makes sense.</td><td>I simplify most of the time.</td><td>I leave the answer without simplifying, and I do not check it.</td></tr>',
  '<tr><th scope="row">Simplificar y revisar el resultado</th><td>Siempre simplifico, escribo números mixtos y reviso que el resultado tenga sentido.</td><td>Simplifico la mayoría de las veces.</td><td>Dejo el resultado sin simplificar, y no lo reviso.</td></tr>')
# Cierre
R("<p>You can now add and subtract fractions, with the same or different denominators, and simplify the result. The hardest part of working with fractions is behind you.</p>", "<p>Ya sabe sumar y restar fracciones, con el mismo denominador o con denominadores distintos, y simplificar el resultado. Ya dejó atrás la parte más difícil de trabajar con fracciones.</p>")
R(f"<p>In <strong>Lesson 4.3 · Multiplying and dividing fractions</strong> you will see something that surprises many students: to multiply and divide fractions, you <strong>do not need</strong> a common denominator. Then, in Lesson 4.4, you will work with mixed numbers like the 1&nbsp;{F(1,4)} you met today.</p>",
  f"<p>En la <strong>Lección 4.3 · Multiplicación y división de fracciones</strong> verá algo que sorprende a muchos estudiantes: para multiplicar y dividir fracciones <strong>no hace falta</strong> un denominador común. Después, en la Lección 4.4, trabajará con números mixtos como el 1&nbsp;{F(1,4)} que conoció hoy.</p>")
R('Next: <a href="lesson-4-3.html">Lesson 4.3 · Multiplying and dividing fractions</a>', 'Siguiente: <a href="leccion-4-3.html">Lección 4.3 · Multiplicación y división de fracciones</a>')
R("""<dt>like denominators</dt><dd>Fractions with the same denominator, like 2/5 and 1/5. Their parts are the same size.</dd>
<dt>unlike denominators</dt><dd>Fractions with different denominators, like 1/2 and 1/3. Their parts are different sizes.</dd>
<dt>common denominator</dt><dd>A denominator that two fractions can share. It is a multiple of both denominators.</dd>
<dt>least common denominator</dt><dd>The smallest common denominator. It is the LCM of the denominators.</dd>
<dt>improper fraction</dt><dd>A fraction whose numerator is greater than or equal to its denominator, like 5/4. It is 1 or more.</dd>
<dt>mixed number</dt><dd>A whole number and a fraction together, like 1 1/4.</dd>
<dt>simplest form</dt><dd>A fraction whose top and bottom share no factor greater than 1, like 1/3.</dd>""",
"""<dt>denominadores iguales</dt><dd>Fracciones con el mismo denominador, como 2/5 y 1/5. Sus partes son del mismo tamaño.</dd>
<dt>denominadores distintos</dt><dd>Fracciones con denominadores diferentes, como 1/2 y 1/3. Sus partes son de tamaños distintos.</dd>
<dt>denominador común</dt><dd>Un denominador que pueden compartir dos fracciones. Es múltiplo de los dos denominadores.</dd>
<dt>mínimo común denominador</dt><dd>El denominador común más pequeño. Es el MCM de los denominadores.</dd>
<dt>fracción impropia</dt><dd>Una fracción cuyo numerador es mayor que su denominador o igual a él, como 5/4. Vale 1 o más.</dd>
<dt>número mixto</dt><dd>Un número entero y una fracción juntos, como 1 1/4.</dd>
<dt>forma más simple</dt><dd>Una fracción cuyo numerador y denominador no tienen ningún factor común mayor que 1, como 1/3.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.2</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 4 · Lección 4.2</p>")
t.js('''{
 next: "Lección 4.3",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "b",
   hints: { a: "También sumó los denominadores. Las partes son octavos antes y después: el denominador sigue siendo 8.", c: "Revise el de arriba: 3 + 2 = 5, no 6.", d: "1/8 es lo que da si resta. Este problema pide sumar." },
   right: "3 octavos más 2 octavos son 5 octavos. Las partes siguen siendo octavos, así que el denominador sigue siendo 8.",
   solution: "Mismo denominador: sume solo los numeradores, 3 + 2 = 5, y deje el 8. Así que 3/8 + 2/8 = 5/8." },
  p2: { ok: "a",
   hints: { b: "También restó los denominadores. Una fracción nunca puede tener 0 abajo. Deje el 9.", c: "11/9 es lo que da si suma. Este problema pide restar.", d: "Sumó los denominadores. Las partes son novenos antes y después: deje el 9." },
   right: "7 novenos menos 4 novenos son 3 novenos. En la sección 4 verá que 3/9 se puede simplificar a 1/3.",
   solution: "Mismo denominador: reste solo los numeradores, 7 − 4 = 3, y deje el 9. Así que 7/9 − 4/9 = 3/9 (que se simplifica a 1/3)." },
  p3: { ok: "b",
   hints: { a: "10 es 4 + 6. Sumar los denominadores no sirve: 10 no es múltiplo de 4.", c: "24 también sirve (4 × 6), pero no es el único. Busque un número más pequeño en el que quepan el 4 y el 6.", d: "2 es factor de 4 y de 6, no múltiplo. El denominador común tiene que ser múltiplo de los dos." },
   right: "Múltiplos de 6: 6, 12. El 12 es el primero en el que también cabe el 4.",
   solution: "Recorra los múltiplos del denominador mayor, 6: 6, 12, … El 4 no cabe exacto en 6, pero sí en 12. Así que 12 es el denominador común más pequeño." },
  p4: { ok: "b",
   hints: { a: "Sumó los de arriba y los de abajo. Primero iguale los denominadores: 1/2 = 2/4.", c: "2/4 es solo la primera fracción, convertida en cuartos. Ahora sume el 1/4.", d: "Revise: el resultado tiene que ser más que 1/2, porque le está sumando algo a 1/2." },
   right: "1/2 = 2/4, y 2/4 + 1/4 = 3/4.",
   solution: "4 es múltiplo de 2, así que el denominador común es 4. 1/2 = 2/4, y 2/4 + 1/4 = 3/4." }
 },
 quiz: {
  A: { ok: "a", hints: { b: "El denominador dice el tamaño de las partes. ¿Cambia el tamaño al juntarlas?", c: "El denominador dice el tamaño de las partes. ¿Cambia el tamaño al juntarlas?", d: "El denominador dice el tamaño de las partes. ¿Cambia el tamaño al juntarlas?" },
   solution: "El denominador se queda igual. Dice el tamaño de las partes, y juntar partes del mismo tamaño no cambia su tamaño. Solo se suman los numeradores." },
  B: { ok: "d", hints: { a: "Sumó los denominadores. Deje el 7.", b: "Revise el de arriba: 2 + 3 = 5.", c: "Aquí no multiplique los denominadores. Ya son iguales." },
   solution: "Mismo denominador: 2 + 3 = 5, y deje el 7. Así que 2/7 + 3/7 = 5/7." },
  C: { ok: "c", hints: { a: "Sumó los denominadores. Deje el 6, reste los de arriba y después simplifique.", b: "7/6 es lo que da si suma. Este problema pide restar.", d: "Una fracción nunca puede tener 0 abajo. Deje el 6." },
   solution: "5 − 2 = 3, así que 5/6 − 2/6 = 3/6. Después simplifique: divida el numerador y el denominador entre 3, y 3/6 = 1/2." },
  D: { ok: "b", hints: { a: "9 es 3 + 6. Sumar los denominadores no sirve.", c: "El 6 no cabe en 3. El denominador común tiene que ser múltiplo de los dos.", d: "5 no es múltiplo de 3 ni de 6." },
   solution: "6 ya es múltiplo de 3 (3 × 2 = 6). Así que 6 es el denominador común: 1/3 = 2/6." },
  E: { ok: "d", hints: { a: "Sumó los de arriba y los de abajo. 2/5 es menos que 1/2, ¡y usted le sumó algo a 1/2!", b: "Primero convierta las dos fracciones en sextos: 1/2 = 3/6 y 1/3 = 2/6.", c: "Primero convierta las dos fracciones en sextos, y sume los numeradores." },
   solution: "El denominador común es 6: 1/2 = 3/6 y 1/3 = 2/6. Después 3/6 + 2/6 = 5/6." },
  F: { ok: "a", hints: { b: "Restó los de arriba y los de abajo. Primero convierta 3/4 en octavos.", c: "Convierta 3/4 en octavos: 3/4 = 6/8. Después reste 1/8.", d: "7/8 es lo que da si suma. Este problema pide restar." },
   solution: "8 es múltiplo de 4, así que convierta 3/4 en octavos: 3/4 = 6/8. Después 6/8 − 1/8 = 5/8." },
  G: { ok: "b", hints: { a: "4/8 todavía se puede simplificar: 4 y 8 se pueden dividir los dos entre 4.", c: "Dividió solo el de arriba. Divida el numerador y el denominador entre el mismo número.", d: "8/4 son 2 enteros. Invirtió los números." },
   solution: "Divida el numerador y el denominador entre 4: 4 ÷ 4 = 1 y 8 ÷ 4 = 2. Así que 4/8 = 1/2." },
  H: { ok: "c", hints: { a: "Sumó los de arriba y los de abajo. Primero convierta 1/2 en cuartos.", b: "1/6 de hora son solo 10 minutos. El resultado tiene que ser más que 1/2 hora.", d: "2/4 es solo la 1/2 hora convertida en cuartos. Ahora sume el 1/4 de hora." },
   solution: "1/2 = 2/4, así que 1/4 + 2/4 = 3/4 de hora. Son 45 minutos." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-4-2.html")
