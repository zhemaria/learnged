"""Crea es/matematicas/nivel-1/leccion-3-2.html a partir de math/level-1/lesson-3-2.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-3-2.html"); t.leccion("")
R = t.r
t.cabecera("<!-- LearnGED · Lección 3.2 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 3.2 · Operations with decimals · LearnGED</title>", "<title>Lección 3.2 · Operaciones con decimales · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 3 — Decimals</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 3 — Decimales</p>')
R("<h1>Lesson 3.2 · Operations with decimals</h1>", "<h1>Lección 3.2 · Operaciones con decimales</h1>")
R('<p class="lema">Add, subtract, multiply, and divide decimals. And meet the TI-30XS calculator, your tool to check your work.</p>', '<p class="lema">Sume, reste, multiplique y divida decimales. Y conozca la calculadora TI-30XS, su herramienta para comprobar su trabajo.</p>')
R("TI-30XS calculator</span>", "Calculadora TI-30XS</span>")
R("<li><strong>Add and subtract</strong> decimals by lining up the decimal points.</li>", "<li><strong>Sumar y restar</strong> decimales alineando los puntos decimales.</li>")
R("<li><strong>Multiply</strong> decimals by counting the decimal places in the answer.</li>", "<li><strong>Multiplicar</strong> decimales contando los lugares decimales del resultado.</li>")
R("<li><strong>Divide</strong> decimals by moving the point in the divisor and in the dividend.</li>", "<li><strong>Dividir</strong> decimales moviendo el punto en el divisor y en el dividendo.</li>")
R("<li><strong>Use</strong> the TI-30XS calculator to check your answers, without replacing your work on paper.</li>", "<li><strong>Usar</strong> la calculadora TI-30XS para comprobar sus respuestas, sin reemplazar su trabajo en papel.</li>")
R('<li><a href="#s-calculator">Your new tool: the TI-30XS calculator</a></li>', '<li><a href="#s-calculadora">Su herramienta nueva: la calculadora TI-30XS</a></li>')
R('<li><a href="#s-add">Add and subtract decimals: line up the points</a></li>', '<li><a href="#s-sumar">Sumar y restar decimales: alinear los puntos</a></li>')
R('<li><a href="#s-multiply">Multiply decimals: count the places</a></li>', '<li><a href="#s-multiplicar">Multiplicar decimales: contar los lugares</a></li>')
R('<li><a href="#s-divide">Divide decimals: move the point</a></li>', '<li><a href="#s-dividir">Dividir decimales: mover el punto</a></li>')
t.todas('<span aria-hidden="true">🧮</span> Open the calculator</button>', '<span aria-hidden="true">🧮</span> Abrir la calculadora</button>')
t.todas('<span class="et-calc"><span aria-hidden="true">🧮</span> Check it on the calculator</span>', '<span class="et-calc"><span aria-hidden="true">🧮</span> Compruébelo en la calculadora</span>')
t.todas("<strong>Step 1.</strong>", "<strong>Paso 1.</strong>"); t.todas("<strong>Step 2.</strong>", "<strong>Paso 2.</strong>"); t.todas("<strong>Step 3.</strong>", "<strong>Paso 3.</strong>"); t.todas("<strong>Result.</strong>", "<strong>Resultado.</strong>")
# 1
R('<h2 id="s-calculator"><span aria-hidden="true" class="num-seccion">1</span>Your new tool: the TI-30XS calculator</h2>', '<h2 id="s-calculadora"><span aria-hidden="true" class="num-seccion">1</span>Su herramienta nueva: la calculadora TI-30XS</h2>')
R("<p>Starting with this lesson, you will use the <strong>TI-30XS MultiView</strong> calculator. It is the calculator you can use on the GED test. It is a powerful tool, but you need to use it with good judgment.</p>",
  "<p>A partir de esta lección usará la calculadora <strong>TI-30XS MultiView</strong>. Es la calculadora que se puede usar en el examen GED. Es una herramienta poderosa, pero hay que usarla con buen criterio.</p>")
R('<span class="et-calc"><span aria-hidden="true">🧮</span> The calculator on this page</span>', '<span class="et-calc"><span aria-hidden="true">🧮</span> La calculadora de esta página</span>')
R("<p>This page has a calculator that works like the TI-30XS MultiView. Open it with the <strong>Calculator</strong> button at the top right of the screen, or with the button below. You can move it around the screen. The <strong>?</strong> button on the calculator explains every key, and the <strong>Reference sheet</strong> button shows the formulas you get on the test. If you have a real TI-30XS, practice with it too, so you learn where its keys are.</p>",
  "<p>Esta página tiene una calculadora que funciona como la TI-30XS MultiView. Ábrala con el botón <strong>Calculadora</strong> de la esquina superior derecha de la pantalla, o con el botón de abajo. Puede moverla por la pantalla. El botón <strong>?</strong> de la calculadora explica cada tecla, y el botón <strong>Hoja de referencia</strong> muestra las fórmulas que le dan en el examen. Si tiene una TI-30XS de verdad, practique también con ella, para aprender dónde están sus teclas.</p>")
R("<h3>Three golden rules before you start</h3>", "<h3>Tres reglas de oro antes de empezar</h3>")
R('<li><strong>Clear the memory before you calculate.</strong> Press <span class="tecla dos">2nd</span> and then <span class="tecla">sto→</span> (the green words above it say <em>clear var</em>), and choose <span class="tecla num">1</span> (Yes). This way no numbers from an earlier calculation get into yours. Make it a habit.</li>',
  '<li><strong>Borre la memoria antes de calcular.</strong> Pulse <span class="tecla dos">2nd</span> y después <span class="tecla">sto→</span> (las palabras verdes de arriba dicen <em>clear var</em>), y elija <span class="tecla num">1</span> (Yes, «sí»). Así ningún número de un cálculo anterior se mete en el suyo. Hágalo un hábito.</li>')
R("<li><strong>The calculator checks; it does not think.</strong> Solve on paper first. Use the calculator only to check. On the GED you need to understand the steps, not just press keys.</li>",
  "<li><strong>La calculadora comprueba; no piensa.</strong> Resuelva primero en papel. Use la calculadora solo para comprobar. En el GED necesita entender los pasos, no solo pulsar teclas.</li>")
R("<li><strong>Check what you typed.</strong> The calculator does exactly what you type. If you put a decimal point in the wrong place, the answer will be wrong, and the calculator will not warn you.</li>",
  "<li><strong>Revise lo que escribió.</strong> La calculadora hace exactamente lo que usted escribe. Si pone un punto decimal en el lugar equivocado, el resultado estará mal, y la calculadora no le avisará.</li>")
R('<span class="etiqueta et-verde">Why paper first?</span>', '<span class="etiqueta et-verde">¿Por qué primero en papel?</span>')
R("<p>When you know how to work with decimals by hand, you can <strong>notice</strong> when the calculator shows something that makes no sense. Without that skill, a typing mistake goes unnoticed. The calculator is your assistant, not your replacement.</p>",
  "<p>Cuando sabe trabajar con decimales a mano, puede <strong>darse cuenta</strong> de que la calculadora muestra algo que no tiene sentido. Sin esa destreza, un error al escribir pasa sin que lo note. La calculadora es su ayudante, no su reemplazo.</p>")
# 2
R('<h2 id="s-add"><span aria-hidden="true" class="num-seccion">2</span>Add and subtract decimals: line up the points</h2>', '<h2 id="s-sumar"><span aria-hidden="true" class="num-seccion">2</span>Sumar y restar decimales: alinear los puntos</h2>')
R("<p>Adding and subtracting decimals works just like it does with whole numbers (Lesson 1.2), with <strong>one new rule</strong>: <strong>line up the decimal points</strong>. The points go one under the other, in a straight column.</p>",
  "<p>Sumar y restar decimales funciona igual que con los números enteros (Lección 1.2), con <strong>una regla nueva</strong>: <strong>alinee los puntos decimales</strong>. Los puntos van uno debajo del otro, en una columna recta.</p>")
R("<p>If the numbers have a different number of decimal places, add zeros on the right so they match. Remember from Lesson 3.1: those zeros do not change the value.</p>",
  "<p>Si los números tienen distinta cantidad de lugares decimales, agregue ceros a la derecha para igualarlos. Recuerde la Lección 3.1: esos ceros no cambian el valor.</p>")
R('<p class="titulo-ej">Example: 12.4 + 3.85</p>', '<p class="titulo-ej">Ejemplo: 12.4 + 3.85</p>')
R("Write 12.4 as <strong>12.40</strong>, so it has as many decimal places as 3.85.", "Escriba 12.4 como <strong>12.40</strong>, para que tenga tantos lugares decimales como 3.85.")
R("Line up the points, one under the other, and add column by column, like with whole numbers.", "Alinee los puntos, uno debajo del otro, y sume columna por columna, como con los números enteros.")
R("The point in the answer goes in the same column as the other points.", "El punto del resultado va en la misma columna que los otros puntos.")
R('aria-label="12.40 plus 3.85 written in columns with the decimal points lined up. The answer is 16.25."', 'aria-label="12.40 más 3.85 escrito en columnas con los puntos decimales alineados. El resultado es 16.25."')
R("<p>The most common mistake is lining up the numbers on the right, as if they were whole numbers. With decimals, you line them up <strong>by the point</strong>. Always add 12.40 and 3.85, with the points in one column.</p>",
  "<p>El error más común es alinear los números por la derecha, como si fueran enteros. Con los decimales se alinean <strong>por el punto</strong>. Siempre sume 12.40 y 3.85, con los puntos en una columna.</p>")
R("<p>You already solved 12.4 + 3.85 on paper. Now check it:</p>", "<p>Ya resolvió 12.4 + 3.85 en papel. Ahora compruébelo:</p>")
t.todas("<li>Type <span", "<li>Escriba <span")
R('<li>Press <span class="tecla">+</span>, then type ', '<li>Pulse <span class="tecla">+</span> y después escriba ')
R('<li>Press <span class="tecla">enter</span>. The screen should show <strong>16.25</strong>, the same as your paper.</li>', '<li>Pulse <span class="tecla">enter</span>. La pantalla debe mostrar <strong>16.25</strong>, lo mismo que su papel.</li>')
R("<p>On the calculator you do not need to add zeros or line up anything. That is exactly why you need to know how it works on paper: to tell if the screen makes sense.</p>",
  "<p>En la calculadora no hace falta agregar ceros ni alinear nada. Justamente por eso necesita saber cómo funciona en papel: para saber si lo que muestra la pantalla tiene sentido.</p>")
R("<h3>Practice 1 — Add decimals</h3>", "<h3>Práctica 1 — Sumar decimales</h3>")
R("What is <strong>7.6 + 14.28</strong>?", "¿Cuánto es <strong>7.6 + 14.28</strong>?")
R("<h3>Practice 2 — Subtract decimals</h3>", "<h3>Práctica 2 — Restar decimales</h3>")
R("You pay a <strong>$13.75</strong> bill with a <strong>$20</strong> bill. How much change do you get?", "Usted paga una cuenta de <strong>$13.75</strong> con un billete de <strong>$20</strong>. ¿Cuánto le dan de cambio?")
R('href="practice-3-2.html#add-subtract"', 'href="practica-3-2.html#sumar-restar"')
R('práctica: add and subtract decimals (se abre', 'práctica: sumar y restar decimales (se abre')
R('<span class="ei-titulo">Practique más: add and subtract decimals</span><span class="ei-sub">Line up the points, add zeros, and work like with whole numbers.</span>', '<span class="ei-titulo">Practique más: sumar y restar decimales</span><span class="ei-sub">Alinee los puntos, agregue ceros y trabaje como con los números enteros.</span>')
# 3
R('<h2 id="s-multiply"><span aria-hidden="true" class="num-seccion">3</span>Multiply decimals: count the places</h2>', '<h2 id="s-multiplicar"><span aria-hidden="true" class="num-seccion">3</span>Multiplicar decimales: contar los lugares</h2>')
R("<p>Here is a nice surprise: to multiply decimals, you <strong>ignore the point at first</strong>. Multiply as if they were whole numbers (Lesson 2.1). At the end, place the point by counting.</p>",
  "<p>Aquí hay una buena sorpresa: para multiplicar decimales, <strong>al principio no se hace caso del punto</strong>. Multiplique como si fueran números enteros (Lección 2.1). Al final, coloque el punto contando.</p>")
R('<span class="etiqueta et-verde">The counting rule</span>', '<span class="etiqueta et-verde">La regla de contar</span>')
R("<p>Count how many decimal places the two factors have <strong>together</strong>. The answer has that same number of decimal places.</p>", "<p>Cuente cuántos lugares decimales tienen los dos factores <strong>juntos</strong>. El resultado tiene esa misma cantidad de lugares decimales.</p>")
R('<p class="titulo-ej">Example: 4.6 × 2.3</p>', '<p class="titulo-ej">Ejemplo: 4.6 × 2.3</p>')
R("Ignore the points and multiply: 46 × 23 = 1,058.", "Olvídese de los puntos y multiplique: 46 × 23 = 1,058.")
R("Count the decimal places: 4.6 has 1, and 2.3 has 1. That is <strong>2 decimal places</strong> in all.", "Cuente los lugares decimales: 4.6 tiene 1, y 2.3 tiene 1. Son <strong>2 lugares decimales</strong> en total.")
R("Place the point so the answer has 2 decimal places: 1058 → <strong>10.58</strong>.", "Coloque el punto para que el resultado tenga 2 lugares decimales: 1058 → <strong>10.58</strong>.")
R('<span class="etiqueta et-verde">Check with an estimate</span>', '<span class="etiqueta et-verde">Compruebe con una estimación</span>')
R("<p>4.6 is about 5, and 2.3 is about 2, so the answer should be close to 5 × 2 = 10. Since 10.58 is close to 10, the point is in the right place. If you got 105.8 or 1.058, you would know the point was wrong.</p>",
  "<p>4.6 es más o menos 5, y 2.3 es más o menos 2, así que el resultado debe estar cerca de 5 × 2 = 10. Como 10.58 está cerca de 10, el punto está en su lugar. Si le diera 105.8 o 1.058, sabría que el punto está mal.</p>")
R(', press <span class="tecla">×</span>, and type ', ', pulse <span class="tecla">×</span> y escriba ')
R('<li>Press <span class="tecla">enter</span>. The screen should show <strong>10.58</strong>.</li>', '<li>Pulse <span class="tecla">enter</span>. La pantalla debe mostrar <strong>10.58</strong>.</li>')
R("<p>Compare three answers: your paper, your estimate (about 10), and the calculator. When all three agree, you can trust your answer.</p>", "<p>Compare tres respuestas: su papel, su estimación (más o menos 10) y la calculadora. Cuando las tres coinciden, puede confiar en su respuesta.</p>")
R("<h3>Practice 3 — Multiply decimals</h3>", "<h3>Práctica 3 — Multiplicar decimales</h3>")
R("What is <strong>3.2 × 1.5</strong>?", "¿Cuánto es <strong>3.2 × 1.5</strong>?")
R('href="practice-3-2.html#multiply"', 'href="practica-3-2.html#multiplicar"')
R('práctica: multiply decimals (se abre', 'práctica: multiplicar decimales (se abre')
R('<span class="ei-titulo">Practique más: multiply decimals</span><span class="ei-sub">Multiply without the point, then count the decimal places at the end.</span>', '<span class="ei-titulo">Practique más: multiplicar decimales</span><span class="ei-sub">Multiplique sin el punto y cuente los lugares decimales al final.</span>')
# 4
R('<h2 id="s-divide"><span aria-hidden="true" class="num-seccion">4</span>Divide decimals: move the point</h2>', '<h2 id="s-dividir"><span aria-hidden="true" class="num-seccion">4</span>Dividir decimales: mover el punto</h2>')
R("<p>Dividing is easier when the <strong>divisor</strong> (the number you divide by) is a whole number. The trick: move the decimal point of the divisor until it is a whole number, and move the point of the dividend <strong>the same number of places</strong>.</p>",
  "<p>Dividir es más fácil cuando el <strong>divisor</strong> (el número entre el que se divide) es un número entero. El truco: mueva el punto decimal del divisor hasta que sea entero, y mueva el punto del dividendo <strong>la misma cantidad de lugares</strong>.</p>")
R('<p class="titulo-ej">Example: 9.45 ÷ 0.5</p>', '<p class="titulo-ej">Ejemplo: 9.45 ÷ 0.5</p>')
R("The divisor is 0.5. Move its point 1 place to the right: 0.5 → 5. Now it is a whole number.", "El divisor es 0.5. Mueva su punto 1 lugar a la derecha: 0.5 → 5. Ahora es un número entero.")
R("Move the point of the dividend the same amount, <strong>1 place</strong>: 9.45 → 94.5.", "Mueva el punto del dividendo lo mismo, <strong>1 lugar</strong>: 9.45 → 94.5.")
R("Now divide 94.5 ÷ 5 with long division. The point in the answer goes straight up from the dividend.", "Ahora divida 94.5 ÷ 5 con la división larga. El punto del resultado sube derecho desde el dividendo.")
R("<p>Both points move <strong>the same number of places</strong>, in <strong>the same direction</strong>. If you move one and forget the other, the answer will be off by 10 times or 100 times.</p>",
  "<p>Los dos puntos se mueven <strong>la misma cantidad de lugares</strong>, en <strong>la misma dirección</strong>. Si mueve uno y se olvida del otro, el resultado saldrá 10 o 100 veces equivocado.</p>")
R(', press <span class="tecla">÷</span>, and type ', ', pulse <span class="tecla">÷</span> y escriba ')
R('<li>Press <span class="tecla">enter</span>. The screen should show <strong>18.9</strong>.</li>', '<li>Pulse <span class="tecla">enter</span>. La pantalla debe mostrar <strong>18.9</strong>.</li>')
R("<p>Here you do not move any point: the calculator does it for you. One more reason to check on paper first.</p>", "<p>Aquí no mueve ningún punto: la calculadora lo hace por usted. Una razón más para comprobar primero en papel.</p>")
R("<h3>Practice 4 — Divide decimals</h3>", "<h3>Práctica 4 — Dividir decimales</h3>")
R("What is <strong>8.4 ÷ 4</strong>?", "¿Cuánto es <strong>8.4 ÷ 4</strong>?")
R('href="practice-3-2.html#divide"', 'href="practica-3-2.html#dividir"')
R('práctica: divide decimals (se abre', 'práctica: dividir decimales (se abre')
R('<span class="ei-titulo">Practique más: divide decimals</span><span class="ei-sub">Move the point in the divisor and in the dividend, then divide as always.</span>', '<span class="ei-titulo">Practique más: dividir decimales</span><span class="ei-sub">Mueva el punto en el divisor y en el dividendo, y después divida como siempre.</span>')
# Tarea
R("<p>This is independent practice. Plan for about one hour, with your notebook open. Golden rule: <strong>solve on paper first, and use the calculator only to check</strong>.</p>", "<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto. Regla de oro: <strong>resuelva primero en papel y use la calculadora solo para comprobar</strong>.</p>")
R('<li><strong>The practice page.</strong> Open the <a href="practice-3-2.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-3-2.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Solve twelve operations with decimals, three of each operation, and check each one with the calculator. When the answers do not match, find the mistake before you go on. It is almost always in the decimal point.</li>",
  "<li><strong>Papel y lápiz.</strong> Resuelva doce operaciones con decimales, tres de cada operación, y compruebe cada una con la calculadora. Cuando los resultados no coincidan, busque el error antes de seguir. Casi siempre está en el punto decimal.</li>")
R("<li><strong>In your daily life.</strong> Take a real receipt. Add two prices, subtract one, and check everything with the calculator. Remember to clear the memory before you start.</li>",
  "<li><strong>En su vida diaria.</strong> Tome un recibo real. Sume dos precios, reste uno y compruebe todo con la calculadora. Acuérdese de borrar la memoria antes de empezar.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. Work on paper, <strong>without the calculator</strong>: on the GED, the first part of the math test does not allow a calculator, and these questions check that you understand the steps.",
  "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>. Trabaje en papel, <strong>sin la calculadora</strong>: en el GED, la primera parte del examen de matemáticas no permite calculadora, y estas preguntas comprueban que usted entiende los pasos.")
R("To add or subtract decimals, what should you do first?", "Para sumar o restar decimales, ¿qué debe hacer primero?")
R('type="button">Line up the numbers on the right.</button><button class="opcion" data-k="b" type="button">Take out all the decimal points.</button><button class="opcion" data-k="c" type="button">Line up the decimal points.</button><button class="opcion" data-k="d" type="button">Multiply by 10 first.</button>',
  'type="button">Alinear los números por la derecha.</button><button class="opcion" data-k="b" type="button">Quitar todos los puntos decimales.</button><button class="opcion" data-k="c" type="button">Alinear los puntos decimales.</button><button class="opcion" data-k="d" type="button">Multiplicar primero por 10.</button>')
R("Add: <strong>5.7 + 2.65</strong>", "Sume: <strong>5.7 + 2.65</strong>")
R("Subtract: <strong>10 − 3.46</strong>", "Reste: <strong>10 − 3.46</strong>")
R("In <strong>2.4 × 3.6</strong>, how many decimal places will the answer have?", "En <strong>2.4 × 3.6</strong>, ¿cuántos lugares decimales tendrá el resultado?")
R('type="button">1 decimal place</button><button class="opcion" data-k="b" type="button">2 decimal places</button><button class="opcion" data-k="c" type="button">3 decimal places</button><button class="opcion" data-k="d" type="button">None</button>',
  'type="button">1 lugar decimal</button><button class="opcion" data-k="b" type="button">2 lugares decimales</button><button class="opcion" data-k="c" type="button">3 lugares decimales</button><button class="opcion" data-k="d" type="button">Ninguno</button>')
R("Multiply: <strong>0.7 × 0.4</strong>", "Multiplique: <strong>0.7 × 0.4</strong>")
R("Divide: <strong>6.5 ÷ 5</strong>", "Divida: <strong>6.5 ÷ 5</strong>")
R("Before you use the TI-30XS calculator to check your work, which habit should you always have?", "Antes de usar la calculadora TI-30XS para comprobar su trabajo, ¿qué hábito debe tener siempre?")
R('type="button">Turn it off and on three times.</button><button class="opcion" data-k="b" type="button">Never check what you type, because the calculator never fails.</button><button class="opcion" data-k="c" type="button">Clear the calculator\'s memory.</button><button class="opcion" data-k="d" type="button">Use it instead of solving on paper.</button>',
  'type="button">Apagarla y encenderla tres veces.</button><button class="opcion" data-k="b" type="button">No revisar nunca lo que escribe, porque la calculadora nunca falla.</button><button class="opcion" data-k="c" type="button">Borrar la memoria de la calculadora.</button><button class="opcion" data-k="d" type="button">Usarla en vez de resolver en papel.</button>')
R("At a store, three items cost $4.99, $2.50, and $7.25. What is the total?", "En una tienda, tres artículos cuestan $4.99, $2.50 y $7.25. ¿Cuál es el total?")
R("<p>After the quiz, you can check any question with the calculator to see that your paper and the screen agree.</p>", "<p>Después del quiz, puede comprobar cualquier pregunta con la calculadora para ver que su papel y la pantalla coinciden.</p>")
# Lista
R('aria-label="Self-check checklist for operations with decimals (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de operaciones con decimales (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: operations with decimals ', '<caption class="cap-oculto">Lista de autoevaluación: operaciones con decimales ')
R('<tr><th scope="row">Line up the point to add and subtract</th><td>I always line up the points and add zeros when I need them.</td><td>I line them up correctly most of the time.</td><td>I line up the numbers on the right, like whole numbers.</td></tr>',
  '<tr><th scope="row">Alinear el punto para sumar y restar</th><td>Siempre alineo los puntos y agrego ceros cuando hacen falta.</td><td>Los alineo bien la mayoría de las veces.</td><td>Alineo los números por la derecha, como los enteros.</td></tr>')
R('<tr><th scope="row">Place the point when I multiply</th><td>I count the places and place the point with no mistakes.</td><td>I multiply well, but sometimes the point ends up in the wrong place.</td><td>I do not use the counting rule.</td></tr>',
  '<tr><th scope="row">Colocar el punto al multiplicar</th><td>Cuento los lugares y coloco el punto sin errores.</td><td>Multiplico bien, pero a veces el punto queda en el lugar equivocado.</td><td>No uso la regla de contar.</td></tr>')
R('<tr><th scope="row">Move the point when I divide</th><td>I move both points the same number of places and divide correctly.</td><td>I move the points well, with a small mistake now and then.</td><td>I move one point and forget the other.</td></tr>',
  '<tr><th scope="row">Mover el punto al dividir</th><td>Muevo los dos puntos la misma cantidad de lugares y divido bien.</td><td>Muevo bien los puntos, con algún error pequeño de vez en cuando.</td><td>Muevo un punto y me olvido del otro.</td></tr>')
R('<tr><th scope="row">Use the calculator with good judgment</th><td>I solve on paper, clear the memory, and check with the calculator.</td><td>I use the calculator to check when I am asked to.</td><td>I use the calculator instead of solving on paper.</td></tr>',
  '<tr><th scope="row">Usar la calculadora con buen criterio</th><td>Resuelvo en papel, borro la memoria y compruebo con la calculadora.</td><td>Uso la calculadora para comprobar cuando me lo piden.</td><td>Uso la calculadora en vez de resolver en papel.</td></tr>')
# Cierre
R("<p>You can now do all four operations with decimals and check them with the <strong>TI-30XS</strong> calculator. In <strong>Lesson 3.3 · Decimals in context and equivalent forms</strong> you will change common fractions to decimals and back, and you will solve real problems about shopping, distances, and measurements with decimals.</p>",
  "<p>Ya sabe hacer las cuatro operaciones con decimales y comprobarlas con la calculadora <strong>TI-30XS</strong>. En la <strong>Lección 3.3 · Decimales en contexto y formas equivalentes</strong> convertirá fracciones comunes en decimales y al revés, y resolverá problemas reales de compras, distancias y medidas con decimales.</p>")
R("<p>That lesson is also a bridge to <strong>Topic 4</strong>, where you will study fractions in depth. You will see that decimals and fractions are two ways to write the same thing: <strong>parts of a whole</strong>.</p>",
  "<p>Esa lección es también un puente hacia el <strong>Tema 4</strong>, donde estudiará las fracciones a fondo. Verá que los decimales y las fracciones son dos formas de escribir lo mismo: <strong>partes de un entero</strong>.</p>")
R('Next: <a href="lesson-3-3.html">Lesson 3.3 · Decimals in context and equivalent forms</a>', 'Siguiente: <a href="leccion-3-3.html">Lección 3.3 · Decimales en contexto y formas equivalentes</a>')
R("""<dt>line up the decimal points</dt><dd>To write the numbers so their points are one under the other, in the same column.</dd>
<dt>decimal places</dt><dd>The digits to the right of the point. 4.62 has 2 decimal places.</dd>
<dt>factor</dt><dd>Each number you multiply. In 4.6 × 2.3, the factors are 4.6 and 2.3.</dd>
<dt>dividend, divisor, quotient</dt><dd>In 9.45 ÷ 0.5 = 18.9, the dividend is 9.45 (what you divide), the divisor is 0.5 (what you divide by), and the quotient is 18.9 (the answer).</dd>
<dt>estimate</dt><dd>A quick answer with rounded numbers, to see if the exact answer makes sense. 4.6 × 2.3 is about 5 × 2 = 10.</dd>
<dt>clear the memory</dt><dd>To erase the numbers stored in the calculator before you begin: 2nd, sto→ (clear var), 1 (Yes).</dd>""",
"""<dt>alinear los puntos decimales</dt><dd>Escribir los números de modo que sus puntos queden uno debajo del otro, en la misma columna.</dd>
<dt>lugares decimales</dt><dd>Los dígitos a la derecha del punto. 4.62 tiene 2 lugares decimales.</dd>
<dt>factor</dt><dd>Cada número que se multiplica. En 4.6 × 2.3, los factores son 4.6 y 2.3.</dd>
<dt>dividendo, divisor, cociente</dt><dd>En 9.45 ÷ 0.5 = 18.9, el dividendo es 9.45 (lo que se divide), el divisor es 0.5 (entre lo que se divide) y el cociente es 18.9 (el resultado).</dd>
<dt>estimación</dt><dd>Un resultado rápido con números redondeados, para ver si el resultado exacto tiene sentido. 4.6 × 2.3 es más o menos 5 × 2 = 10.</dd>
<dt>borrar la memoria</dt><dd>Borrar los números guardados en la calculadora antes de empezar: 2nd, sto→ (clear var), 1 (Yes).</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 3 · Lesson 3.2</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 3 · Lección 3.2</p>")
t.js('''{
 next: "Lección 3.3",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "b",
   hints: { a: "Revise las décimas: 6 + 2 = 8.", c: "Alinee los puntos decimales: 7.60 + 14.28. Los puntos van en una columna.", d: "¿Sumó las 6 décimas de 7.6? Escríbalo como 7.60." },
   right: "Con los puntos alineados: 7.60 + 14.28 = 21.88.",
   solution: "Escriba 7.6 como 7.60 y alinee los puntos: 7.60 + 14.28. Centésimas: 0 + 8 = 8. Décimas: 6 + 2 = 8. Unidades: 7 + 4 = 11, escriba 1 y lleve 1. Decenas: 1 + 1 = 2. El resultado es 21.88." },
  p2: { ok: "b",
   hints: { a: "Escriba $20 como $20.00 y revise las unidades después de pedir prestado.", c: "Escriba $20 como $20.00 y reste columna por columna, empezando por las centésimas.", d: "Escriba $20 como $20.00. ¿Pidió prestado a las unidades?" },
   right: "$20.00 − $13.75 = $6.25. Comprobación: $6.25 + $13.75 = $20.00 ✓",
   solution: "Escriba $20 como $20.00 y alinee los puntos: 20.00 − 13.75 = 6.25. Comprobación: 6.25 + 13.75 = 20.00 ✓. Su cambio es $6.25." },
  p3: { ok: "b",
   hints: { a: "Cuente los lugares decimales: 1 + 1 = 2. ¿Dónde va el punto?", c: "32 × 15 = 480. Con 2 lugares decimales, eso es 4.80.", d: "Eso es 3.2 + 1.5. Esto es una multiplicación." },
   right: "32 × 15 = 480, con 2 lugares decimales: 4.80 = 4.8. Estimación: 3 × 1.5 = 4.5 ✓",
   solution: "Olvídese de los puntos: 32 × 15 = 480. Cuente los lugares: 1 + 1 = 2. Coloque el punto: 4.80, que es 4.8. Estimación: más o menos 3 × 1.5 = 4.5, cerca de 4.8 ✓" },
  p4: { ok: "b",
   hints: { a: "El punto sube derecho al resultado. Estimación: 8 ÷ 4 = 2.", c: "Estimación: 8 ÷ 4 = 2. El resultado tiene que estar cerca de 2.", d: "Compruebe: 2.4 × 4 = 9.6, no 8.4." },
   right: "El divisor 4 ya es entero: 8.4 ÷ 4 = 2.1. Comprobación: 2.1 × 4 = 8.4 ✓",
   solution: "El divisor 4 es un número entero, así que no mueve ningún punto. Divida 8.4 ÷ 4 y suba el punto derecho: 2.1. Comprobación: 2.1 × 4 = 8.4 ✓" }
 },
 quiz: {
  A: { ok: "c", hints: { a: "Alinear por la derecha sirve para los números enteros, no para los decimales.", b: "Si quita los puntos, pierde el valor de cada dígito.", d: "No hace falta multiplicar primero." },
   solution: "Alinee los puntos decimales, uno debajo del otro. Después agregue ceros si hacen falta y trabaje columna por columna." },
  B: { ok: "b", hints: { a: "Alinee los puntos: 5.70 + 2.65.", c: "Eso parece una resta. Esta pregunta pide sumar.", d: "Revise las décimas: 7 + 6 = 13, así que lleva 1 a las unidades." },
   solution: "5.70 + 2.65: centésimas 0 + 5 = 5; décimas 7 + 6 = 13, escriba 3 y lleve 1; unidades 5 + 2 + 1 = 8. El resultado es 8.35." },
  C: { ok: "a", hints: { b: "Escriba 10 como 10.00 y reste cada columna, empezando por las centésimas.", c: "Revise las décimas y las centésimas: 10.00 − 3.46.", d: "Recuerde que pidió prestado a las unidades." },
   solution: "Escriba 10 como 10.00: 10.00 − 3.46 = 6.54. Comprobación: 6.54 + 3.46 = 10.00 ✓" },
  D: { ok: "b", hints: { a: "Cuente juntos los lugares decimales de los dos factores.", c: "Cada factor tiene solo un lugar decimal: 1 + 1.", d: "Los lugares decimales de los dos factores se suman." },
   solution: "2.4 tiene 1 lugar decimal y 3.6 tiene 1. Juntos: 2 lugares decimales. (2.4 × 3.6 = 8.64.)" },
  E: { ok: "d", hints: { a: "7 × 4 = 28, y el resultado necesita 2 lugares decimales, no 1.", b: "Eso es 0.7 + 0.4. Esto es una multiplicación.", c: "Coloque el punto decimal: 1 + 1 = 2 lugares decimales." },
   solution: "7 × 4 = 28. Cada factor tiene 1 lugar decimal, así que el resultado tiene 2: 0.28." },
  F: { ok: "a", hints: { b: "Suba el punto derecho al resultado.", c: "Estimación: 6.5 ÷ 5 es un poco más que 1.", d: "Compruebe: 1.5 × 5 = 7.5, no 6.5." },
   solution: "El divisor 5 es entero. Divida 6.5 ÷ 5 y suba el punto: 1.3. Comprobación: 1.3 × 5 = 6.5 ✓" },
  G: { ok: "c", hints: { a: "Apagarla y encenderla no hace más correcta su respuesta.", b: "Revise siempre lo que escribe. La calculadora hace exactamente lo que usted escribe.", d: "Resuelva primero en papel. La calculadora es para comprobar." },
   solution: "Borre la memoria antes de empezar (2nd, sto→, 1), para que ningún número de un cálculo anterior se meta en el suyo." },
  H: { ok: "d", hints: { a: "Revise lo que lleva a las unidades.", b: "Revise las centésimas y las décimas: primero alinee los puntos.", c: "Revise la columna de las unidades: 4 + 2 + 7, más lo que llevaba." },
   solution: "Alinee los puntos: 4.99 + 2.50 + 7.25. Centésimas: 9 + 0 + 5 = 14, escriba 4 y lleve 1. Décimas: 9 + 5 + 2 + 1 = 17, escriba 7 y lleve 1. Unidades: 4 + 2 + 7 + 1 = 14. El total es $14.74." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-3-2.html")
