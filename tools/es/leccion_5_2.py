"""Crea es/matematicas/nivel-1/leccion-5-2.html a partir de math/level-1/lesson-5-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-5-2.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 5.2 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 5.2 · Algebraic language and simple unknowns · LearnGED</title>", "<title>Lección 5.2 · Lenguaje algebraico e incógnitas simples · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 5 — Patterns and algebraic thinking</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 5 — Patrones y pensamiento algebraico</p>')
R("<h1>Lesson 5.2 · Algebraic language and simple unknowns</h1>", "<h1>Lección 5.2 · Lenguaje algebraico e incógnitas simples</h1>")
R('<p class="lema">Write with symbols what we used to say with words. Math starts to use its own language.</p>', '<p class="lema">Escriba con símbolos lo que antes decíamos con palabras. Las matemáticas empiezan a usar su propio idioma.</p>')
R("The balance model</span>", "El modelo de la balanza</span>")
R("<li><strong>Translate</strong> phrases in words into algebraic language.</li>", "<li><strong>Traducir</strong> frases en palabras al lenguaje algebraico.</li>")
R("<li><strong>Write</strong> one-step equations with an unknown (a box □ or a letter x).</li>", "<li><strong>Escribir</strong> ecuaciones de un paso con una incógnita (un cuadrito □ o una letra x).</li>")
R("<li><strong>Solve</strong> one-step equations with the inverse operation.</li>", "<li><strong>Resolver</strong> ecuaciones de un paso con la operación inversa.</li>")
R("<li><strong>Check</strong> the solution by substituting the value you found.</li>", "<li><strong>Comprobar</strong> la solución sustituyendo el valor que halló.</li>")
R('<li><a href="#s-language">The language of algebra</a></li>', '<li><a href="#s-lenguaje">El lenguaje del álgebra</a></li>')
R('<li><a href="#s-translate">Translate words into symbols</a></li>', '<li><a href="#s-traducir">Traducir palabras a símbolos</a></li>')
R('<li><a href="#s-balance">The equation: a balanced scale</a></li>', '<li><a href="#s-balanza">La ecuación: una balanza en equilibrio</a></li>')
R('<li><a href="#s-inverse">Solve with the inverse operation</a></li>', '<li><a href="#s-inversa">Resolver con la operación inversa</a></li>')
R('<li><a href="#s-check">Check the solution</a></li>', '<li><a href="#s-comprobar">Comprobar la solución</a></li>')
# 1
R('<h2 id="s-language"><span aria-hidden="true" class="num-seccion">1</span>The language of algebra</h2>', '<h2 id="s-lenguaje"><span aria-hidden="true" class="num-seccion">1</span>El lenguaje del álgebra</h2>')
R('<p>In <strong>Lesson 5.1</strong> you found the rules of patterns and said them <strong>in words</strong>: "add 5 each time," "the output is the input times 3." That works, but it is long.</p>',
  '<p>En la <strong>Lección 5.1</strong> descubrió las reglas de los patrones y las dijo <strong>con palabras</strong>: «sumar 5 cada vez», «la salida es la entrada por 3». Eso funciona, pero es largo.</p>')
R('<p>Algebra gives us a shorter and more exact way: <strong>write those ideas with symbols</strong>. Instead of saying "a number plus five," we write <span class="ec">x + 5</span>. It means the same thing, but in the language of math.</p>',
  '<p>El álgebra nos da una forma más corta y más exacta: <strong>escribir esas ideas con símbolos</strong>. En vez de decir «un número más cinco», escribimos <span class="ec">x + 5</span>. Quiere decir lo mismo, pero en el idioma de las matemáticas.</p>')
R('<span class="etiqueta et-verde">The unknown</span>', '<span class="etiqueta et-verde">La incógnita</span>')
R('<p>An <strong>unknown</strong> is a number we do not know yet. We show it with a symbol: a box <strong>□</strong> or a letter like <strong>x</strong> or <strong>n</strong>. The unknown is not an impossible mystery: it is simply "the number we want to find."</p>',
  '<p>Una <strong>incógnita</strong> es un número que todavía no conocemos. La mostramos con un símbolo: un cuadrito <strong>□</strong> o una letra como <strong>x</strong> o <strong>n</strong>. La incógnita no es un misterio imposible: es sencillamente «el número que queremos hallar».</p>')
# 2
R('<h2 id="s-translate"><span aria-hidden="true" class="num-seccion">2</span>Translate words into symbols</h2>', '<h2 id="s-traducir"><span aria-hidden="true" class="num-seccion">2</span>Traducir palabras a símbolos</h2>')
R("<p>To write in algebraic language, find the operation that each phrase points to. This is your translation table:</p>", "<p>Para escribir en lenguaje algebraico, busque la operación que indica cada frase. Esta es su tabla de traducción:</p>")
R('aria-label="Phrases and their algebraic expressions (tabla desplazable horizontalmente)"', 'aria-label="Frases y sus expresiones algebraicas (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Translating phrases in words into algebraic language</caption>', '<caption class="cap-oculto">Traducción de frases en palabras al lenguaje algebraico</caption>')
R('<th scope="col">Phrase in words</th><th scope="col">In algebraic language</th>', '<th scope="col">Frase en palabras</th><th scope="col">En lenguaje algebraico</th>')
R("<td>A number <strong>plus</strong> 7 · a number <strong>increased by</strong> 7 · 7 <strong>more than</strong> a number</td>", "<td>Un número <strong>más</strong> 7 · un número <strong>aumentado en</strong> 7 · 7 <strong>más que</strong> un número</td>")
R("<td>A number <strong>minus</strong> 5 · a number <strong>decreased by</strong> 5 · 5 <strong>less than</strong> a number</td>", "<td>Un número <strong>menos</strong> 5 · un número <strong>disminuido en</strong> 5 · 5 <strong>menos que</strong> un número</td>")
R("<td><strong>Twice</strong> a number · <strong>two times</strong> a number</td>", "<td><strong>El doble de</strong> un número · <strong>dos veces</strong> un número</td>")
R("<td><strong>Three times</strong> a number</td>", "<td><strong>El triple de</strong> un número · <strong>tres veces</strong> un número</td>")
R("<td>A number <strong>divided by</strong> 4</td>", "<td>Un número <strong>dividido entre</strong> 4</td>")
R("<td>A number <strong>is equal to</strong> 12 · a number <strong>is</strong> 12</td>", "<td>Un número <strong>es igual a</strong> 12 · un número <strong>es</strong> 12</td>")
R('<span class="etiqueta et-ambar">Watch out! Two traps</span>', '<span class="etiqueta et-ambar">¡Cuidado! Dos trampas</span>')
R('<p><strong>Twice is written together.</strong> "Twice x" is written <span class="ec">2x</span>, with no sign between the 2 and the x. In algebra, a number and a letter written <strong>together</strong> are multiplied: <span class="ec">2x</span> means "2 times x."</p>',
  '<p><strong>El doble se escribe junto.</strong> «El doble de x» se escribe <span class="ec">2x</span>, sin ningún signo entre el 2 y la x. En álgebra, un número y una letra escritos <strong>juntos</strong> se multiplican: <span class="ec">2x</span> quiere decir «2 por x».</p>')
R('<p><strong>"Less than" changes the order.</strong> "5 less than a number" means take 5 away from the number, so the number comes first: <span class="ec">x − 5</span>, not <span class="ec">5 − x</span>.</p>',
  '<p><strong>«Menos que» cambia el orden.</strong> «5 menos que un número» quiere decir quitarle 5 al número, así que el número va primero: <span class="ec">x − 5</span>, no <span class="ec">5 − x</span>.</p>')
R("<h3>Practice 1 — Translate into symbols</h3>", "<h3>Práctica 1 — Traducir a símbolos</h3>")
R("<h3>Practice 2 — Translate into symbols</h3>", "<h3>Práctica 2 — Traducir a símbolos</h3>")
R('How do you write "a number increased by 9" in algebraic language?', '¿Cómo se escribe «un número aumentado en 9» en lenguaje algebraico?')
R('How do you write "three times a number"?', '¿Cómo se escribe «el triple de un número»?')
R('href="practice-5-2.html#translate"', 'href="practica-5-2.html#traducir"')
R('práctica: translate words into symbols (se abre', 'práctica: traducir palabras a símbolos (se abre')
R('<span class="ei-titulo">Practique más: translate words into symbols</span><span class="ei-sub">Turn phrases like "a number plus five" into expressions with x.</span>',
  '<span class="ei-titulo">Practique más: traducir palabras a símbolos</span><span class="ei-sub">Convierta frases como «un número más cinco» en expresiones con x.</span>')
# 3
R('<h2 id="s-balance"><span aria-hidden="true" class="num-seccion">3</span>The equation: a balanced scale</h2>', '<h2 id="s-balanza"><span aria-hidden="true" class="num-seccion">3</span>La ecuación: una balanza en equilibrio</h2>')
R("<p>An <strong>equation</strong> says that two things are equal: what is on one side of the <strong>=</strong> sign has the same value as what is on the other side. The best way to picture it is a <strong>balanced scale</strong>.</p>",
  "<p>Una <strong>ecuación</strong> dice que dos cosas son iguales: lo que está a un lado del signo <strong>=</strong> vale lo mismo que lo que está al otro lado. La mejor manera de imaginarla es una <strong>balanza en equilibrio</strong>.</p>")
R('aria-label="A balanced scale. On the left pan there is a box with an unknown number and a weight of 3. On the right pan there is a weight of 8. The scale is level: box plus 3 equals 8."',
  'aria-label="Una balanza en equilibrio. En el platillo izquierdo hay un cuadrito con un número desconocido y una pesa de 3. En el platillo derecho hay una pesa de 8. La balanza está nivelada: cuadrito más 3 es igual a 8."')
R(">The scale is level: the left side weighs the same as the right side.</p>", ">La balanza está nivelada: el lado izquierdo pesa lo mismo que el lado derecho.</p>")
R('<p>In the equation <span class="ec">□ + 3 = 8</span>, the box hides a number. Because the scale is balanced, that number must make the left side worth 8. What number plus 3 gives 8? The number <strong>5</strong>.</p>',
  '<p>En la ecuación <span class="ec">□ + 3 = 8</span>, el cuadrito esconde un número. Como la balanza está en equilibrio, ese número tiene que hacer que el lado izquierdo valga 8. ¿Qué número más 3 da 8? El número <strong>5</strong>.</p>')
R('<span class="etiqueta et-verde">The key idea of this lesson</span>', '<span class="etiqueta et-verde">La idea clave de esta lección</span>')
R("<p><strong>To solve an equation</strong> is to find the value of the unknown that keeps the scale balanced: the number that makes the equation true.</p>",
  "<p><strong>Resolver una ecuación</strong> es hallar el valor de la incógnita que mantiene la balanza en equilibrio: el número que hace verdadera la ecuación.</p>")
R('href="practice-5-2.html#balance"', 'href="practica-5-2.html#balanza"')
R('práctica: the equation as a scale (se abre', 'práctica: la ecuación como balanza (se abre')
R('<span class="ei-titulo">Practique más: the equation as a scale</span><span class="ei-sub">Try numbers in the box and see which one keeps the scale level.</span>',
  '<span class="ei-titulo">Practique más: la ecuación como balanza</span><span class="ei-sub">Pruebe números en el cuadrito y vea cuál mantiene la balanza nivelada.</span>')
# 4
R('<h2 id="s-inverse"><span aria-hidden="true" class="num-seccion">4</span>Solve with the inverse operation</h2>', '<h2 id="s-inversa"><span aria-hidden="true" class="num-seccion">4</span>Resolver con la operación inversa</h2>')
R("<p>With easy equations you can guess, but there is a sure method that always works: use the <strong>inverse operation</strong>. Remember from Topics 1 and 2: subtraction undoes addition, and division undoes multiplication.</p>",
  "<p>Con ecuaciones fáciles puede adivinar, pero hay un método seguro que siempre funciona: usar la <strong>operación inversa</strong>. Recuerde de los Temas 1 y 2: la resta deshace la suma, y la división deshace la multiplicación.</p>")
R("<p>The idea is to <strong>get the unknown alone</strong>. To do that, use the inverse of the operation that is with it.</p>",
  "<p>La idea es <strong>dejar sola la incógnita</strong>. Para eso, use la operación inversa de la que la acompaña.</p>")
R('<p class="titulo-ej">Example: solve <span class="ec">□ + 3 = 8</span></p>', '<p class="titulo-ej">Ejemplo: resuelva <span class="ec">□ + 3 = 8</span></p>')
R('<p class="titulo-ej">Example: solve <span class="ec">4x = 20</span></p>', '<p class="titulo-ej">Ejemplo: resuelva <span class="ec">4x = 20</span></p>')
R("<strong>Look at the unknown.</strong> It is <em>added</em> to 3. The inverse of adding is <strong>subtracting</strong>.", "<strong>Mire la incógnita.</strong> Está <em>sumada</em> con 3. La inversa de sumar es <strong>restar</strong>.")
R("<strong>Subtract 3 from both sides</strong>, so the scale stays balanced: □ + 3 − 3 = 8 − 3.", "<strong>Reste 3 en los dos lados</strong>, para que la balanza siga en equilibrio: □ + 3 − 3 = 8 − 3.")
R("<strong>Simplify.</strong> On the left, + 3 − 3 cancel out, and the unknown is alone: □ = 5.", "<strong>Simplifique.</strong> A la izquierda, + 3 − 3 se anulan, y la incógnita queda sola: □ = 5.")
R("<strong>Look at the unknown.</strong> It is <em>multiplied</em> by 4. The inverse of multiplying is <strong>dividing</strong>.", "<strong>Mire la incógnita.</strong> Está <em>multiplicada</em> por 4. La inversa de multiplicar es <strong>dividir</strong>.")
R("<strong>Divide both sides by 4:</strong> 4x ÷ 4 = 20 ÷ 4.", "<strong>Divida los dos lados entre 4:</strong> 4x ÷ 4 = 20 ÷ 4.")
R("<strong>Simplify.</strong> On the left, the x is alone: x = 5.", "<strong>Simplifique.</strong> A la izquierda, la x queda sola: x = 5.")
R("<strong>Solution.</strong> □ = <strong>5</strong>.", "<strong>Solución.</strong> □ = <strong>5</strong>.")
R("<strong>Solution.</strong> x = <strong>5</strong>.", "<strong>Solución.</strong> x = <strong>5</strong>.")
R("<p>The same idea works for the other two operations: addition undoes subtraction, and multiplication undoes division.</p>", "<p>La misma idea sirve para las otras dos operaciones: la suma deshace la resta, y la multiplicación deshace la división.</p>")
R('aria-label="The inverse operation for each kind of equation (tabla desplazable horizontalmente)"', 'aria-label="La operación inversa para cada tipo de ecuación (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">The inverse operation for each kind of one-step equation</caption>', '<caption class="cap-oculto">La operación inversa para cada tipo de ecuación de un paso</caption>')
R('<th scope="col">Equation</th><th scope="col">The x is…</th><th scope="col">Do this to both sides</th>', '<th scope="col">Ecuación</th><th scope="col">La x está…</th><th scope="col">Haga esto en los dos lados</th>')
R("<td>added to 3</td><td>subtract 3: x = 8 − 3 = 5</td>", "<td>sumada con 3</td><td>restar 3: x = 8 − 3 = 5</td>")
R("<td>minus 4</td><td>add 4: x = 10 + 4 = 14</td>", "<td>menos 4</td><td>sumar 4: x = 10 + 4 = 14</td>")
R("<td>multiplied by 4</td><td>divide by 4: x = 20 ÷ 4 = 5</td>", "<td>multiplicada por 4</td><td>dividir entre 4: x = 20 ÷ 4 = 5</td>")
R("<td>divided by 3</td><td>multiply by 3: x = 6 × 3 = 18</td>", "<td>dividida entre 3</td><td>multiplicar por 3: x = 6 × 3 = 18</td>")
R('<span class="etiqueta et-ambar">The rule of the scale</span>', '<span class="etiqueta et-ambar">La regla de la balanza</span>')
R("<p>Whatever you do to one side of the equation, <strong>do it to the other side too</strong>. If you subtract 3 on the left, subtract 3 on the right. That way the scale never tips, and the equation stays true.</p>",
  "<p>Lo que haga en un lado de la ecuación, <strong>hágalo también en el otro lado</strong>. Si resta 3 a la izquierda, reste 3 a la derecha. Así la balanza nunca se inclina, y la ecuación sigue siendo verdadera.</p>")
R("<h3>Practice 3 — Solve an addition equation</h3>", "<h3>Práctica 3 — Resolver una ecuación de suma</h3>")
R("<h3>Practice 4 — Solve a multiplication equation</h3>", "<h3>Práctica 4 — Resolver una ecuación de multiplicación</h3>")
R('id="t-p3">Solve: ', 'id="t-p3">Resuelva: ')
R('id="t-p4">Solve: ', 'id="t-p4">Resuelva: ')
R('href="practice-5-2.html#inverse-operation"', 'href="practica-5-2.html#operacion-inversa"')
R('práctica: solve with the inverse operation (se abre', 'práctica: resolver con la operación inversa (se abre')
R('<span class="ei-titulo">Practique más: solve with the inverse operation</span><span class="ei-sub">Get the unknown alone by undoing the operation that is with it, step by step.</span>',
  '<span class="ei-titulo">Practique más: resolver con la operación inversa</span><span class="ei-sub">Deje sola la incógnita deshaciendo, paso a paso, la operación que la acompaña.</span>')
# 5
R('<h2 id="s-check"><span aria-hidden="true" class="num-seccion">5</span>Check the solution</h2>', '<h2 id="s-comprobar"><span aria-hidden="true" class="num-seccion">5</span>Comprobar la solución</h2>')
R("<p>After you solve, there is a simple way to know if you are right: <strong>substitute</strong>. That means you put the value you found in place of the unknown and see if the equation is true.</p>",
  "<p>Después de resolver, hay una forma sencilla de saber si acertó: <strong>sustituir</strong>. Es decir, poner el valor que halló en lugar de la incógnita y ver si la ecuación es verdadera.</p>")
R('<p class="titulo-ej">Example: check that x = 9 solves <span class="ec">x + 6 = 15</span></p>', '<p class="titulo-ej">Ejemplo: compruebe que x = 9 resuelve <span class="ec">x + 6 = 15</span></p>')
R("<strong>Substitute.</strong> Put 9 in place of x in the original equation: 9 + 6 = 15.", "<strong>Sustituya.</strong> Ponga 9 en lugar de x en la ecuación original: 9 + 6 = 15.")
R("<strong>Calculate the left side.</strong> 9 + 6 = 15.", "<strong>Calcule el lado izquierdo.</strong> 9 + 6 = 15.")
R("<strong>Compare.</strong> 15 = 15. Both sides are equal, so <strong>x = 9 is the right solution</strong>.", "<strong>Compare.</strong> 15 = 15. Los dos lados son iguales, así que <strong>x = 9 es la solución correcta</strong>.")
R('<span class="etiqueta et-verde">A good habit</span>', '<span class="etiqueta et-verde">Un buen hábito</span>')
R("<p>Checking by substituting works like checking with the inverse operation in Topics 1 and 2: it tells you that your answer is right, with no one else checking it for you.</p>",
  "<p>Comprobar sustituyendo funciona como la comprobación con la operación inversa de los Temas 1 y 2: le dice que su respuesta está bien, sin que nadie más se la tenga que revisar.</p>")
R("<p>You can substitute with the calculator. Type the left side with your value in place of x, and compare the answer with the right side.</p>",
  "<p>Puede sustituir con la calculadora. Escriba el lado izquierdo con su valor en lugar de x, y compare el resultado con el lado derecho.</p>")
R('<li>Does x = 5 solve <span class="ec">4x = 20</span>? Type <span class="tecla num">4</span> <span class="tecla">×</span> <span class="tecla num">5</span> <span class="tecla">enter</span>. The screen shows 20, the same as the right side: yes.</li>',
  '<li>¿x = 5 resuelve <span class="ec">4x = 20</span>? Escriba <span class="tecla num">4</span> <span class="tecla">×</span> <span class="tecla num">5</span> <span class="tecla">enter</span>. La pantalla muestra 20, igual que el lado derecho: sí.</li>')
R('<li>Does x = 18 solve <span class="ec">x ÷ 3 = 6</span>? Type <span class="tecla num">1</span><span class="tecla num">8</span> <span class="tecla">÷</span> <span class="tecla num">3</span> <span class="tecla">enter</span>. The screen shows 6: yes.</li>',
  '<li>¿x = 18 resuelve <span class="ec">x ÷ 3 = 6</span>? Escriba <span class="tecla num">1</span><span class="tecla num">8</span> <span class="tecla">÷</span> <span class="tecla num">3</span> <span class="tecla">enter</span>. La pantalla muestra 6: sí.</li>')
R('href="practice-5-2.html#check"', 'href="practica-5-2.html#comprobar"')
R('práctica: check the solution (se abre', 'práctica: comprobar la solución (se abre')
R('<span class="ei-titulo">Practique más: check the solution</span><span class="ei-sub">Put the value in place of x and see if both sides are equal.</span>',
  '<span class="ei-titulo">Practique más: comprobar la solución</span><span class="ei-sub">Ponga el valor en lugar de x y vea si los dos lados son iguales.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-5-2.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-5-2.html">página de práctica de esta lección</a> ')
R('<li><strong>Paper and pencil.</strong> Translate ten phrases into symbols: "twice a number," "5 less than a number," "a number divided by 3," and so on. Then go the other way: take <span class="ec">x + 12 = 40</span> and write a real situation that this equation describes. Solve it and check it.</li>',
  '<li><strong>Papel y lápiz.</strong> Traduzca diez frases a símbolos: «el doble de un número», «5 menos que un número», «un número dividido entre 3», etc. Después vaya al revés: tome <span class="ec">x + 12 = 40</span> y escriba una situación real que esa ecuación describa. Resuélvala y compruébela.</li>')
R('<li><strong>In your daily life.</strong> Think of a situation of your own with a number you do not know: "I had some money, I spent $20, and I have $35 left. How much did I have?" Write it as an equation, solve it with the inverse operation, and check it by substituting.</li>',
  '<li><strong>En su vida diaria.</strong> Piense en una situación suya con un número que no conoce: «Tenía algo de dinero, gasté $20 y me quedan $35. ¿Cuánto tenía?». Escríbala como ecuación, resuélvala con la operación inversa y compruébela sustituyendo.</li>')
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("What is an unknown in an equation?", "¿Qué es una incógnita en una ecuación?")
R('type="button">The equal sign.</button><button class="opcion" data-k="b" type="button">A number that is always zero.</button><button class="opcion" data-k="c" type="button">The result of an addition.</button><button class="opcion" data-k="d" type="button">A number we do not know yet, shown with a symbol.</button>',
  'type="button">El signo igual.</button><button class="opcion" data-k="b" type="button">Un número que siempre es cero.</button><button class="opcion" data-k="c" type="button">El resultado de una suma.</button><button class="opcion" data-k="d" type="button">Un número que todavía no conocemos, mostrado con un símbolo.</button>')
R('How do you write "8 less than a number" in algebraic language?', '¿Cómo se escribe «8 menos que un número» en lenguaje algebraico?')
R('The expression <span class="ec">2x</span> means:', 'La expresión <span class="ec">2x</span> quiere decir:')
R('type="button">2 plus x</button><button class="opcion" data-k="b" type="button">2 times x</button><button class="opcion" data-k="c" type="button">x minus 2</button><button class="opcion" data-k="d" type="button">x divided by 2</button>',
  'type="button">2 más x</button><button class="opcion" data-k="b" type="button">2 por x</button><button class="opcion" data-k="c" type="button">x menos 2</button><button class="opcion" data-k="d" type="button">x dividido entre 2</button>')
R('To solve <span class="ec">x + 7 = 10</span>, what do you do to both sides?', 'Para resolver <span class="ec">x + 7 = 10</span>, ¿qué se hace en los dos lados?')
R('type="button">Subtract 7.</button><button class="opcion" data-k="b" type="button">Add 7.</button><button class="opcion" data-k="c" type="button">Multiply by 7.</button><button class="opcion" data-k="d" type="button">Divide by 10.</button>',
  'type="button">Restar 7.</button><button class="opcion" data-k="b" type="button">Sumar 7.</button><button class="opcion" data-k="c" type="button">Multiplicar por 7.</button><button class="opcion" data-k="d" type="button">Dividir entre 10.</button>')
R('id="t-qE">Solve: ', 'id="t-qE">Resuelva: ')
R('id="t-qF">Solve: ', 'id="t-qF">Resuelva: ')
R('To check that x = 8 solves <span class="ec">x + 4 = 12</span>, you should:', 'Para comprobar que x = 8 resuelve <span class="ec">x + 4 = 12</span>, usted debe:')
R('type="button">Put 8 in place of x and see that 8 + 4 = 12.</button><button class="opcion" data-k="b" type="button">Add 8 + 12.</button><button class="opcion" data-k="c" type="button">Subtract 8 − 4.</button><button class="opcion" data-k="d" type="button">You cannot check it.</button>',
  'type="button">Poner 8 en lugar de x y ver que 8 + 4 = 12.</button><button class="opcion" data-k="b" type="button">Sumar 8 + 12.</button><button class="opcion" data-k="c" type="button">Restar 8 − 4.</button><button class="opcion" data-k="d" type="button">No se puede comprobar.</button>')
R('"A worker had some money, earned $50, and now has $200." If x is the money the worker had, which equation shows this situation?',
  '«Un trabajador tenía algo de dinero, ganó $50 y ahora tiene $200». Si x es el dinero que tenía el trabajador, ¿qué ecuación muestra esta situación?')
# Lista
R('aria-label="Self-check checklist for algebraic language and one-step equations (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de lenguaje algebraico y ecuaciones de un paso (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for algebraic language and one-step equations ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas de lenguaje algebraico y ecuaciones de un paso ')
R('<tr><th scope="row">Translate phrases into algebraic language</th><td>I translate addition, subtraction, multiplication, and division exactly, including "less than."</td><td>I translate most phrases correctly.</td><td>I only translate simple additions, or I mix up the order.</td></tr>',
  '<tr><th scope="row">Traducir frases al lenguaje algebraico</th><td>Traduzco con exactitud sumas, restas, multiplicaciones y divisiones, incluso «menos que».</td><td>Traduzco bien la mayoría de las frases.</td><td>Solo traduzco sumas sencillas, o confundo el orden.</td></tr>')
R('<tr><th scope="row">Write the right equation</th><td>I write the equation with the unknown in the right place.</td><td>I write the equation correctly most of the time.</td><td>I am not sure where the numbers and the unknown go.</td></tr>',
  '<tr><th scope="row">Escribir la ecuación correcta</th><td>Escribo la ecuación con la incógnita en el lugar correcto.</td><td>Escribo bien la ecuación la mayoría de las veces.</td><td>No estoy seguro de dónde van los números y la incógnita.</td></tr>')
R('<tr><th scope="row">Solve with the inverse operation</th><td>I use the inverse operation on both sides with no mistakes.</td><td>I solve correctly, with an occasional slip.</td><td>I use the same operation instead of the inverse one.</td></tr>',
  '<tr><th scope="row">Resolver con la operación inversa</th><td>Uso la operación inversa en los dos lados sin errores.</td><td>Resuelvo bien, con algún descuido de vez en cuando.</td><td>Uso la misma operación en vez de la inversa.</td></tr>')
R('<tr><th scope="row">Check the solution</th><td>I substitute the value and check the equation on my own, every time.</td><td>I check when someone asks me to.</td><td>I do not check, or I substitute in the wrong place.</td></tr>',
  '<tr><th scope="row">Comprobar la solución</th><td>Sustituyo el valor y compruebo la ecuación por mi cuenta, siempre.</td><td>Compruebo cuando alguien me lo pide.</td><td>No compruebo, o sustituyo en el lugar equivocado.</td></tr>')
# Cierre
R("<p>You can now translate phrases into algebraic language, write one-step equations, solve them with the inverse operation, and check the solution. You have taken your first steps in algebra.</p>",
  "<p>Ya sabe traducir frases al lenguaje algebraico, escribir ecuaciones de un paso, resolverlas con la operación inversa y comprobar la solución. Ha dado sus primeros pasos en el álgebra.</p>")
R("<p>In <strong>Lesson 5.3 · One-step word problems</strong> you will put together everything you learned in Level 1: you will read a problem in words, decide which of the four operations to use, write it as an equation with an unknown, and solve it. That lesson closes Topic 5.</p>",
  "<p>En la <strong>Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones</strong> juntará todo lo que aprendió en el Nivel 1: leerá un problema en palabras, decidirá cuál de las cuatro operaciones usar, lo escribirá como una ecuación con una incógnita y lo resolverá. Esa lección cierra el Tema 5.</p>")
R("Next: Lesson 5.3 · One-step word problems</p>", "Siguiente: Lección 5.3 · Problemas verbales de un paso con las cuatro operaciones</p>")
R("""<dt>unknown (variable)</dt><dd>A number we do not know yet, shown with a box □ or a letter like x.</dd>
<dt>expression</dt><dd>Numbers, letters, and operation signs with no equal sign, like x + 5 or 3x.</dd>
<dt>equation</dt><dd>A statement that two things are equal, with an equal sign, like x + 3 = 8.</dd>
<dt>solve</dt><dd>To find the value of the unknown that makes the equation true.</dd>
<dt>inverse operation</dt><dd>The operation that undoes another one: subtraction undoes addition, and division undoes multiplication (and the other way around).</dd>
<dt>substitute</dt><dd>To put a number in place of the unknown, for example to check a solution.</dd>""",
"""<dt>incógnita (variable)</dt><dd>Un número que todavía no conocemos, mostrado con un cuadrito □ o una letra como x.</dd>
<dt>expresión</dt><dd>Números, letras y signos de operación sin signo igual, como x + 5 o 3x.</dd>
<dt>ecuación</dt><dd>Una afirmación de que dos cosas son iguales, con signo igual, como x + 3 = 8.</dd>
<dt>resolver</dt><dd>Hallar el valor de la incógnita que hace verdadera la ecuación.</dd>
<dt>operación inversa</dt><dd>La operación que deshace otra: la resta deshace la suma, y la división deshace la multiplicación (y al revés).</dd>
<dt>sustituir</dt><dd>Poner un número en lugar de la incógnita, por ejemplo para comprobar una solución.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.2</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 5 · Lección 5.2</p>")
t.js('''{
 next: "Lección 5.3",
 review: "las secciones 2, 4 y 5",
 practice: {
  p1: { ok: "d",
   hints: { a: "9 − x quiere decir 9 menos un número. «Aumentado en» quiere decir que el número se hace más grande: sume 9.", b: "9x quiere decir 9 por un número. «Aumentado en 9» quiere decir sumar 9, no multiplicar.", c: "x ÷ 9 quiere decir un número dividido entre 9. «Aumentado en» quiere decir que el número se hace más grande: sume 9." },
   right: "«Aumentado en» quiere decir sumar: x + 9.",
   solution: "«Un número» es x, y «aumentado en 9» quiere decir sumar 9. Así que la expresión es x + 9." },
  p2: { ok: "a",
   hints: { b: "x + 3 quiere decir un número más 3. «El triple» quiere decir multiplicar por 3.", c: "x ÷ 3 es la tercera parte de un número. «El triple» quiere decir multiplicar por 3.", d: "x − 3 quiere decir un número menos 3. «El triple» quiere decir multiplicar por 3." },
   right: "El triple de x se escribe 3x: el 3 pegado a la x quiere decir multiplicar.",
   solution: "«El triple de un número» quiere decir 3 × x. En álgebra se escribe 3x, sin ningún signo entre el 3 y la x." },
  p3: { ok: "d",
   hints: { a: "21 es 15 + 6. La x tiene + 6, así que deshágalo con la inversa: reste 6.", b: "6 es el número que se le suma a x, no el valor de x. Reste 6 en los dos lados.", c: "90 es 15 × 6. La x tiene + 6, así que la operación inversa es restar 6." },
   right: "x + 6 − 6 = 15 − 6, así que x = 9. Comprobación: 9 + 6 = 15.",
   solution: "La x tiene + 6. La inversa de sumar es restar, así que reste 6 en los dos lados: x = 15 − 6 = 9. Comprobación: 9 + 6 = 15." },
  p4: { ok: "a",
   hints: { b: "21 es 18 + 3. 3x quiere decir 3 por x, así que la operación inversa es dividir entre 3.", c: "15 es 18 − 3. 3x quiere decir 3 por x, así que la operación inversa es dividir entre 3.", d: "54 es 18 × 3. Usó la misma operación. Deshaga la multiplicación: divida entre 3." },
   right: "3x ÷ 3 = 18 ÷ 3, así que x = 6. Comprobación: 3 × 6 = 18.",
   solution: "3x quiere decir 3 por x. La inversa de multiplicar es dividir, así que divida los dos lados entre 3: x = 18 ÷ 3 = 6. Comprobación: 3 × 6 = 18." }
 },
 quiz: {
  A: { ok: "d", hints: { a: "El signo igual dice que los dos lados valen lo mismo. No es el número que buscamos.", b: "Una incógnita puede ser cualquier número. Su valor se halla resolviendo la ecuación.", c: "El resultado de una suma es un total. La incógnita es el número que todavía no conocemos." },
   solution: "Una incógnita es un número que todavía no conocemos. La escribimos con un símbolo, como □ o x." },
  B: { ok: "c", hints: { a: "Cuidado con «menos que»: le quita 8 al número, así que el número va primero: x − 8.", b: "8x quiere decir 8 por un número. «Menos que» quiere decir restar.", d: "x + 8 es 8 más que un número. «Menos que» quiere decir restar." },
   solution: "«8 menos que un número» quiere decir quitarle 8 al número: x − 8. El orden cambia respecto a las palabras: el número va primero." },
  C: { ok: "b", hints: { a: "2 más x se escribe 2 + x, con signo más.", c: "x menos 2 se escribe x − 2.", d: "x dividido entre 2 se escribe x ÷ 2." },
   solution: "Cuando un número y una letra se escriben juntos, se multiplican: 2x quiere decir 2 × x." },
  D: { ok: "a", hints: { b: "Sumar 7 deja el lado izquierdo como x + 14. Deshaga el + 7 con su inversa: reste 7.", c: "La x está sumada con 7, no multiplicada. Deshaga la suma con una resta.", d: "10 es el otro lado, no lo que acompaña a la x. Deshaga el + 7: reste 7." },
   solution: "La x tiene + 7. La inversa de sumar 7 es restar 7. Reste 7 en los dos lados: x = 10 − 7 = 3." },
  E: { ok: "c", hints: { a: "16 es 12 + 4. Deshaga el + 4 con su inversa: reste 4.", b: "3 es 12 ÷ 4. La x está sumada con 4, no multiplicada. Reste 4.", d: "48 es 12 × 4. La x tiene + 4: reste 4." },
   solution: "Reste 4 en los dos lados: x = 12 − 4 = 8. Comprobación: 8 + 4 = 12." },
  F: { ok: "a", hints: { b: "40 es 35 + 5. 5x quiere decir 5 por x, así que divida entre 5.", c: "30 es 35 − 5. 5x quiere decir 5 por x, así que divida entre 5.", d: "175 es 35 × 5. Deshaga la multiplicación con su inversa: divida entre 5." },
   solution: "5x quiere decir 5 por x. Divida los dos lados entre 5: x = 35 ÷ 5 = 7. Comprobación: 5 × 7 = 35." },
  G: { ok: "a", hints: { b: "Sumar 8 y 12 no pone a prueba la ecuación. Ponga 8 en lugar de x.", c: "8 − 4 no está en la ecuación. Ponga 8 en lugar de x y calcule x + 4.", d: "Siempre se puede comprobar: ponga el número en lugar de x y vea si los dos lados son iguales." },
   solution: "Para comprobar, sustituya: ponga 8 en lugar de x. 8 + 4 = 12, y el lado derecho es 12. Los dos lados son iguales, así que x = 8 está bien." },
  H: { ok: "b", hints: { a: "El trabajador ganó $50, así que el dinero subió: sume 50, no reste.", c: "50x quiere decir 50 veces el dinero. El trabajador ganó $50 más: sume.", d: "Los $200 son lo que el trabajador tiene al final, así que van solos en un lado: x + 50 = 200." },
   solution: "El trabajador tenía x dólares, ganó $50 más (+ 50) y ahora tiene $200: x + 50 = 200. Al resolverla: x = 200 − 50 = 150." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-5-2.html")
