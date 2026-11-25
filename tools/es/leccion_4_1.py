"""Crea es/matematicas/nivel-1/leccion-4-1.html a partir de math/level-1/lesson-4-1.html."""
from traduce import Traductor, F
t = Traductor("math/level-1/lesson-4-1.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 4.1 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 4.1 · Equivalent fractions: simplify and compare · LearnGED</title>", "<title>Lección 4.1 · Fracciones equivalentes: simplificar y comparar · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 4 — Fractions</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 4 — Fracciones</p>')
R("<h1>Lesson 4.1 · Equivalent fractions: simplify and compare</h1>", "<h1>Lección 4.1 · Fracciones equivalentes: simplificar y comparar</h1>")
R('<p class="lema">The same amount can be written in many ways. Learn to recognize those ways, simplify them, and compare them.</p>', '<p class="lema">La misma cantidad se puede escribir de muchas maneras. Aprenda a reconocerlas, simplificarlas y compararlas.</p>')
R("Fraction bars</span>", "Barras de fracciones</span>")
R("<li><strong>Name</strong> the parts of a fraction: the numerator and the denominator.</li>", "<li><strong>Nombrar</strong> las partes de una fracción: el numerador y el denominador.</li>")
R("<li><strong>Recognize and make</strong> equivalent fractions (fractions with the same value).</li>", "<li><strong>Reconocer y formar</strong> fracciones equivalentes (fracciones con el mismo valor).</li>")
R("<li><strong>Simplify</strong> a fraction to its simplest form.</li>", "<li><strong>Simplificar</strong> una fracción a su forma más simple.</li>")
R("<li><strong>Compare</strong> two fractions to decide which one is greater.</li>", "<li><strong>Comparar</strong> dos fracciones para decidir cuál es mayor.</li>")
R('<li><a href="#s-what">What is a fraction?</a></li>', '<li><a href="#s-que-es">¿Qué es una fracción?</a></li>')
R('<li><a href="#s-equivalent">Equivalent fractions</a></li>', '<li><a href="#s-equivalentes">Fracciones equivalentes</a></li>')
R('<li><a href="#s-simplify">Simplify a fraction</a></li>', '<li><a href="#s-simplificar">Simplificar una fracción</a></li>')
R('<li><a href="#s-compare">Compare fractions</a></li>', '<li><a href="#s-comparar">Comparar fracciones</a></li>')
# 1
R('<h2 id="s-what"><span aria-hidden="true" class="num-seccion">1</span>What is a fraction?</h2>', '<h2 id="s-que-es"><span aria-hidden="true" class="num-seccion">1</span>¿Qué es una fracción?</h2>')
R('<p>In <strong>Topic 3</strong> you learned that a decimal is a part of a whole. A <strong>fraction</strong> is another way to write those parts, and many times it is the most natural one: "half an hour," "a quarter pound," "three quarters of a tank of gas."</p>',
  '<p>En el <strong>Tema 3</strong> aprendió que un decimal es una parte de un entero. Una <strong>fracción</strong> es otra forma de escribir esas partes, y muchas veces es la más natural: «media hora», «un cuarto de libra», «tres cuartos de tanque de gasolina».</p>')
R("<p>A fraction has two numbers separated by a bar:</p>", "<p>Una fracción tiene dos números separados por una raya:</p>")
R("<li>The <strong>numerator</strong> (top): how many parts we <strong>have</strong>.</li>", "<li>El <strong>numerador</strong> (arriba): cuántas partes <strong>tenemos</strong>.</li>")
R("<li>The <strong>denominator</strong> (bottom): how many <strong>equal parts</strong> the whole was divided into.</li>", "<li>El <strong>denominador</strong> (abajo): en cuántas <strong>partes iguales</strong> se dividió el entero.</li>")
R(f"<p>For example, {F(3,4)} means: the whole was divided into <strong>4</strong> equal parts, and we take <strong>3</strong> of them.</p>", f"<p>Por ejemplo, {F(3,4)} quiere decir: el entero se dividió en <strong>4</strong> partes iguales, y tomamos <strong>3</strong> de ellas.</p>")
R('aria-label="A bar divided into 4 equal parts, with 3 parts shaded: three fourths."', 'aria-label="Una barra dividida en 4 partes iguales, con 3 partes sombreadas: tres cuartos."')
R("<strong>Three fourths:</strong> 3 parts shaded out of 4 = ", "<strong>Tres cuartos:</strong> 3 partes sombreadas de 4 = ")
R('<span class="etiqueta et-verde">Connection to Topic 3</span>', '<span class="etiqueta et-verde">Conexión con el Tema 3</span>')
R(f'<p>Remember from Lesson 3.3: the fraction bar means "divided by." {F(3,4)} is the same as 3 ÷ 4 = 0.75. Fractions and decimals are two languages for the same idea.</p>',
  f'<p>Recuerde la Lección 3.3: la raya de la fracción quiere decir «dividido entre». {F(3,4)} es lo mismo que 3 ÷ 4 = 0.75. Las fracciones y los decimales son dos lenguajes para la misma idea.</p>')
R('href="practice-4-1.html#what"', 'href="practica-4-1.html#que-es"')
R('práctica: what is a fraction? (se abre', 'práctica: ¿qué es una fracción? (se abre')
R('<span class="ei-titulo">Practique más: what is a fraction?</span><span class="ei-sub">Build fractions with a bar and a number line, and name the numerator and the denominator.</span>', '<span class="ei-titulo">Practique más: ¿qué es una fracción?</span><span class="ei-sub">Forme fracciones con una barra y una recta numérica, y nombre el numerador y el denominador.</span>')
# 2
R('<h2 id="s-equivalent"><span aria-hidden="true" class="num-seccion">2</span>Equivalent fractions</h2>', '<h2 id="s-equivalentes"><span aria-hidden="true" class="num-seccion">2</span>Fracciones equivalentes</h2>')
R("<p>Two fractions are <strong>equivalent</strong> when they show <strong>the same amount</strong>, even though they are written with different numbers. Look at these two bars:</p>", "<p>Dos fracciones son <strong>equivalentes</strong> cuando muestran <strong>la misma cantidad</strong>, aunque se escriban con números distintos. Fíjese en estas dos barras:</p>")
R('aria-label="A bar divided into 2 equal parts, with 1 part shaded: one half."', 'aria-label="Una barra dividida en 2 partes iguales, con 1 parte sombreada: un medio."')
R(" — one half</p>", " — un medio</p>")
R('aria-label="A bar of the same size divided into 4 equal parts, with 2 parts shaded: two fourths, also one half."', 'aria-label="Una barra del mismo tamaño dividida en 4 partes iguales, con 2 partes sombreadas: dos cuartos, también un medio."')
R(" — also one half</p>", " — también un medio</p>")
R(f"<p>The shaded part is <strong>exactly the same size</strong>: {F(1,2)} and {F(2,4)} are equivalent fractions.</p>", f"<p>La parte sombreada es <strong>exactamente del mismo tamaño</strong>: {F(1,2)} y {F(2,4)} son fracciones equivalentes.</p>")
R('<span class="etiqueta et-verde">The golden rule</span>', '<span class="etiqueta et-verde">La regla de oro</span>')
R("<p>If you <strong>multiply</strong> (or <strong>divide</strong>) the numerator and the denominator by <strong>the same number</strong>, you get an equivalent fraction. Whatever you do to the top, you do to the bottom.</p>",
  "<p>Si <strong>multiplica</strong> (o <strong>divide</strong>) el numerador y el denominador por <strong>el mismo número</strong>, obtiene una fracción equivalente. Lo que le haga al de arriba, se lo hace al de abajo.</p>")
R('<p class="titulo-ej">Example: make fractions equivalent to ', '<p class="titulo-ej">Ejemplo: forme fracciones equivalentes a ')
R("Multiply the top and the bottom by 2: ", "Multiplique el numerador y el denominador por 2: ")
R("Multiply the top and the bottom by 3: ", "Multiplique el numerador y el denominador por 3: ")
R(". They all have the same value.</p>", ". Todas tienen el mismo valor.</p>")
R("<h3>Practice 1 — Equivalent fractions</h3>", "<h3>Práctica 1 — Fracciones equivalentes</h3>")
R(f"Which fraction is equivalent to {F(1,3)}?", f"¿Qué fracción es equivalente a {F(1,3)}?")
R('href="practice-4-1.html#equivalent"', 'href="practica-4-1.html#equivalentes"')
R('práctica: equivalent fractions (se abre', 'práctica: fracciones equivalentes (se abre')
R('<span class="ei-titulo">Practique más: equivalent fractions</span><span class="ei-sub">Multiply the top and the bottom by the same number and compare the bars.</span>', '<span class="ei-titulo">Practique más: fracciones equivalentes</span><span class="ei-sub">Multiplique el numerador y el denominador por el mismo número y compare las barras.</span>')
# 3
R('<h2 id="s-simplify"><span aria-hidden="true" class="num-seccion">3</span>Simplify a fraction</h2>', '<h2 id="s-simplificar"><span aria-hidden="true" class="num-seccion">3</span>Simplificar una fracción</h2>')
R("<p>To <strong>simplify</strong> (or reduce) a fraction means to write it with the smallest numbers possible, without changing its value. You do it by <strong>dividing</strong> the numerator and the denominator by the same number.</p>",
  "<p><strong>Simplificar</strong> (o reducir) una fracción es escribirla con los números más pequeños posibles, sin cambiar su valor. Se hace <strong>dividiendo</strong> el numerador y el denominador entre el mismo número.</p>")
R("<p>A fraction is in its <strong>simplest form</strong> when no number greater than 1 divides both the numerator and the denominator evenly.</p>", "<p>Una fracción está en su <strong>forma más simple</strong> cuando ningún número mayor que 1 divide exactamente al numerador y al denominador a la vez.</p>")
R('<p class="titulo-ej">Example: simplify ', '<p class="titulo-ej">Ejemplo: simplifique ')
R("Find a number that divides both 8 and 12. The number 4 works: 8 ÷ 4 = 2, and 12 ÷ 4 = 3.", "Busque un número que divida a 8 y a 12. El 4 sirve: 8 ÷ 4 = 2, y 12 ÷ 4 = 3.")
R(f"<strong>Paso 2.</strong> You get {F(2,3)}.", f"<strong>Paso 2.</strong> Obtiene {F(2,3)}.")
R("Can you keep going? 2 and 3 share no factor greater than 1. It is already in simplest form.", "¿Se puede seguir? 2 y 3 no tienen ningún factor común mayor que 1. Ya está en su forma más simple.")
R(f"<p>If you do not find the biggest number right away, that is fine. Divide by a small number (like 2) and repeat: ", "<p>Si no encuentra el número más grande enseguida, no importa. Divida entre un número pequeño (como 2) y repita: ")
R(". You get the same answer in more steps.</p>", ". Llega al mismo resultado en más pasos.</p>")
R("<p>The calculator always shows fractions in simplest form. Use it to check your work:</p>", "<p>La calculadora siempre muestra las fracciones en su forma más simple. Úsela para comprobar su trabajo:</p>")
R('<li>Press <span class="tecla">n/d</span>, type <span class="tecla num">8</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">1</span><span class="tecla num">2</span>, and leave with <span class="tecla">►</span>.</li>',
  '<li>Pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">8</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">1</span><span class="tecla num">2</span> y salga con <span class="tecla">►</span>.</li>')
R('<li>Press <span class="tecla">enter</span>. The screen shows ', '<li>Pulse <span class="tecla">enter</span>. La pantalla muestra ')
R("<p>Simplify on paper first. If your answer and the screen do not match, check whether you can still divide.</p>", "<p>Simplifique primero en papel. Si su respuesta y la pantalla no coinciden, revise si todavía puede dividir.</p>")
R("<h3>Practice 2 — Simplify</h3>", "<h3>Práctica 2 — Simplificar</h3>")
R(f"What is the simplest form of {F(6,10)}?", f"¿Cuál es la forma más simple de {F(6,10)}?")
R('href="practice-4-1.html#simplify"', 'href="practica-4-1.html#simplificar"')
R('práctica: simplify a fraction (se abre', 'práctica: simplificar una fracción (se abre')
R('<span class="ei-titulo">Practique más: simplify a fraction</span><span class="ei-sub">Divide by the same number until you reach the simplest form, step by step or all at once.</span>', '<span class="ei-titulo">Practique más: simplificar una fracción</span><span class="ei-sub">Divida entre el mismo número hasta llegar a la forma más simple, paso a paso o de una vez.</span>')
R('href="lesson-4-1-gcf-lcm.html" aria-label="Open the complement: factors, multiples, GCF, and LCM"', 'href="leccion-4-1-mcd-mcm.html" aria-label="Abrir el complemento: factores, múltiplos, MCD y MCM"')
R('<span class="ei-titulo">What is the greatest number that divides both?</span><span class="ei-sub">That number is the greatest common factor (GCF). This complement shows you how to find it, so you can simplify in one step. It also teaches the LCM, which you will need in Lesson 4.2.</span><span class="ei-cta">Open the complement <span aria-hidden="true">›</span></span>',
  '<span class="ei-titulo">¿Cuál es el número más grande que divide a los dos?</span><span class="ei-sub">Ese número es el máximo común divisor (MCD). Este complemento le enseña a hallarlo, para simplificar en un solo paso. También le enseña el MCM, que necesitará en la Lección 4.2.</span><span class="ei-cta">Abrir el complemento <span aria-hidden="true">›</span></span>')
# 4
R('<h2 id="s-compare"><span aria-hidden="true" class="num-seccion">4</span>Compare fractions</h2>', '<h2 id="s-comparar"><span aria-hidden="true" class="num-seccion">4</span>Comparar fracciones</h2>')
R("<p>To decide which of two fractions is greater, there are two cases.</p>", "<p>Para decidir cuál de dos fracciones es mayor, hay dos casos.</p>")
R("<h3>Case 1: the same denominator</h3>", "<h3>Caso 1: el mismo denominador</h3>")
R("<p>If the two fractions have <strong>the same denominator</strong>, it is easy: <strong>the greater one has the greater numerator</strong>. The parts are the same size, so more parts means more.</p>", "<p>Si las dos fracciones tienen <strong>el mismo denominador</strong>, es fácil: <strong>la mayor es la que tiene el numerador mayor</strong>. Las partes son del mismo tamaño, así que más partes es más.</p>")
R('<p class="titulo-ej">Example: compare ', '<p class="titulo-ej">Ejemplo: compare ', 2)
R(f"{F(3,8)} and {F(5,8)}</p>", f"{F(3,8)} y {F(5,8)}</p>")
R("Same denominator (8): the parts are the same size.", "Mismo denominador (8): las partes son del mismo tamaño.")
R(f"5 parts are more than 3 parts: {F(5,8)}", f"5 partes son más que 3 partes: {F(5,8)}")
R("<h3>Case 2: different denominators</h3>", "<h3>Caso 2: denominadores distintos</h3>")
R("<p>If the denominators are <strong>different</strong>, first make them the same: find <strong>equivalent fractions with the same denominator</strong>. Then compare the numerators.</p>", "<p>Si los denominadores son <strong>distintos</strong>, primero iguálelos: busque <strong>fracciones equivalentes con el mismo denominador</strong>. Después compare los numeradores.</p>")
R(f"{F(2,3)} and {F(3,4)}</p>", f"{F(2,3)} y {F(3,4)}</p>")
R("Find a common denominator. 12 works for both 3 and 4.", "Busque un denominador común. El 12 sirve para 3 y para 4.")
R("<strong>Paso 2.</strong> Change them: ", "<strong>Paso 2.</strong> Conviértalas: ")
R(f" (× 4), and {F(3,4)}", f" (× 4), y {F(3,4)}")
R("Compare the numerators: 9 is more than 8.", "Compare los numeradores: 9 es más que 8.")
R(f"<p>A <strong>greater</strong> denominator does not mean a greater fraction. {F(1,8)} is <strong>less</strong> than {F(1,2)}: the more parts you cut the whole into, the smaller each part is.</p>",
  f"<p>Un denominador <strong>mayor</strong> no quiere decir una fracción mayor. {F(1,8)} es <strong>menor</strong> que {F(1,2)}: cuantas más partes se corta el entero, más pequeña es cada parte.</p>")
R('aria-label="A bar divided into 2 equal parts with 1 shaded: one half."', 'aria-label="Una barra dividida en 2 partes iguales con 1 sombreada: un medio."')
R('aria-label="A bar of the same size divided into 8 equal parts with 1 shaded: one eighth, much smaller than one half."', 'aria-label="Una barra del mismo tamaño dividida en 8 partes iguales con 1 sombreada: un octavo, mucho menor que un medio."')
R('<span aria-hidden="true">🧮</span> Another way to check: change to decimals</span>', '<span aria-hidden="true">🧮</span> Otra forma de comprobar: convertir a decimales</span>')
R(f"<p>Fractions and decimals are two languages for the same idea. To compare {F(2,3)} and {F(3,4)}, you can change each one to a decimal with ", f"<p>Las fracciones y los decimales son dos lenguajes para la misma idea. Para comparar {F(2,3)} y {F(3,4)}, puede convertir cada una en decimal con ")
R("</span> shows <strong>0.666…</strong> and <span", "</span> muestra <strong>0.666…</strong> y <span")
R(f"</span> shows <strong>0.75</strong>. Since 0.75 is greater, {F(3,4)} is greater.</p>", f"</span> muestra <strong>0.75</strong>. Como 0.75 es mayor, {F(3,4)} es mayor.</p>")
R("<h3>Practice 3 — Compare (same denominator)</h3>", "<h3>Práctica 3 — Comparar (mismo denominador)</h3>")
R(f"Which fraction is greater: {F(7,10)} or {F(4,10)}?", f"¿Qué fracción es mayor: {F(7,10)} o {F(4,10)}?")
t.todas("</span> is greater</button>", "</span> es mayor</button>")
t.todas('type="button">They are equal</button>', 'type="button">Son iguales</button>')
R("<h3>Practice 4 — Compare (different denominators)</h3>", "<h3>Práctica 4 — Comparar (denominadores distintos)</h3>")
R(f"Which fraction is greater: {F(1,2)} or {F(2,5)}?", f"¿Qué fracción es mayor: {F(1,2)} o {F(2,5)}?")
R('href="practice-4-1.html#compare"', 'href="practica-4-1.html#comparar"')
R('práctica: compare fractions (se abre', 'práctica: comparar fracciones (se abre')
R('<span class="ei-titulo">Practique más: compare fractions</span><span class="ei-sub">Decide which is greater with the same denominator, the same numerator, or different denominators, and see the bars.</span>', '<span class="ei-titulo">Practique más: comparar fracciones</span><span class="ei-sub">Decida cuál es mayor con el mismo denominador, el mismo numerador o denominadores distintos, y vea las barras.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-4-1.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-4-1.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Draw two bars of the same length. Divide one into 4 parts and the other into 8. Shade 3/4 of the first one, and find how many eighths you need to shade to reach the same length. Do it again with 1/2 and sixths, and with 2/3 and twelfths. Seeing the bars side by side is what convinces you that two different fractions can be worth the same.</li>",
  "<li><strong>Papel y lápiz.</strong> Dibuje dos barras del mismo largo. Divida una en 4 partes y la otra en 8. Sombree 3/4 de la primera, y busque cuántos octavos tiene que sombrear para llegar al mismo largo. Repítalo con 1/2 y sextos, y con 2/3 y doceavos. Ver las barras una al lado de la otra es lo que lo convence de que dos fracciones distintas pueden valer lo mismo.</li>")
R("<li><strong>In your kitchen.</strong> Look at your measuring cups and spoons. How many 1/4 cups fill a 1/2 cup? How many teaspoons make a tablespoon? Write each answer as an equation with fractions, for example 2 × 1/4 cup = 1/2 cup.</li>",
  "<li><strong>En su cocina.</strong> Mire sus tazas y cucharas de medir. ¿Cuántas tazas de 1/4 llenan una taza de 1/2? ¿Cuántas cucharaditas forman una cucharada? Escriba cada respuesta como una igualdad con fracciones, por ejemplo 2 × 1/4 de taza = 1/2 taza.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R(f"In the fraction {F(5,8)}, which number is the <strong>denominator</strong>?", f"En la fracción {F(5,8)}, ¿qué número es el <strong>denominador</strong>?")
R(f"Which fraction is equivalent to {F(1,2)}?", f"¿Qué fracción es equivalente a {F(1,2)}?")
R("To get an equivalent fraction, you should:", "Para obtener una fracción equivalente, hay que:")
R('type="button">Add the same number to the top and the bottom.</button><button class="opcion" data-k="b" type="button">Change only the numerator.</button><button class="opcion" data-k="c" type="button">Subtract the same number from the top and the bottom.</button><button class="opcion" data-k="d" type="button">Multiply or divide the top and the bottom by the same number.</button>',
  'type="button">Sumar el mismo número al numerador y al denominador.</button><button class="opcion" data-k="b" type="button">Cambiar solo el numerador.</button><button class="opcion" data-k="c" type="button">Restar el mismo número al numerador y al denominador.</button><button class="opcion" data-k="d" type="button">Multiplicar o dividir el numerador y el denominador por el mismo número.</button>')
R(f"What is the simplest form of {F(4,8)}?", f"¿Cuál es la forma más simple de {F(4,8)}?")
R(f"What is the simplest form of {F(9,12)}?", f"¿Cuál es la forma más simple de {F(9,12)}?")
R(f"Which fraction is greater: {F(5,9)} or {F(2,9)}?", f"¿Qué fracción es mayor: {F(5,9)} o {F(2,9)}?")
R(f"Which fraction is <strong>less</strong>: {F(1,4)} or {F(1,6)}?", f"¿Qué fracción es <strong>menor</strong>: {F(1,4)} o {F(1,6)}?")
R(f"Two pizzas are the same size. {F(3,4)} of one pizza was eaten, and {F(5,8)} of the other. From which pizza was more eaten?", f"Dos pizzas son del mismo tamaño. De una se comieron {F(3,4)}, y de la otra {F(5,8)}. ¿De qué pizza se comió más?")
R(f'type="button">The one with {F(5,8)} eaten</button><button class="opcion" data-k="b" type="button">The same amount from both</button><button class="opcion" data-k="c" type="button">The one with {F(3,4)} eaten</button>',
  f'type="button">De la que se comieron {F(5,8)}</button><button class="opcion" data-k="b" type="button">Lo mismo de las dos</button><button class="opcion" data-k="c" type="button">De la que se comieron {F(3,4)}</button>')
# Lista
R('aria-label="Self-check checklist for equivalent fractions (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de fracciones equivalentes (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: fraction skills ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas con fracciones ')
R('<tr><th scope="row">Name the numerator and the denominator</th><td>I name them and explain what each one tells.</td><td>I name them correctly.</td><td>I mix up their roles, or I cannot tell them apart.</td></tr>',
  '<tr><th scope="row">Nombrar el numerador y el denominador</th><td>Los nombro y explico lo que dice cada uno.</td><td>Los nombro bien.</td><td>Confundo sus papeles, o no los distingo.</td></tr>')
R('<tr><th scope="row">Make equivalent fractions</th><td>I multiply or divide the top and the bottom with no mistakes.</td><td>I make equivalent fractions correctly most of the time.</td><td>I change only one number of the fraction.</td></tr>',
  '<tr><th scope="row">Formar fracciones equivalentes</th><td>Multiplico o divido el numerador y el denominador sin errores.</td><td>Formo bien fracciones equivalentes la mayoría de las veces.</td><td>Cambio solo un número de la fracción.</td></tr>')
R('<tr><th scope="row">Simplify fractions</th><td>I always reach the simplest form.</td><td>I simplify, sometimes in several steps, but I do not always finish.</td><td>I do not simplify.</td></tr>',
  '<tr><th scope="row">Simplificar fracciones</th><td>Siempre llego a la forma más simple.</td><td>Simplifico, a veces en varios pasos, pero no siempre termino.</td><td>No simplifico.</td></tr>')
R('<tr><th scope="row">Compare two fractions</th><td>I compare with the same and with different denominators, and I can explain why.</td><td>I compare well when the denominators are the same.</td><td>I go by the size of the numbers without making the denominators the same.</td></tr>',
  '<tr><th scope="row">Comparar dos fracciones</th><td>Comparo con el mismo denominador y con denominadores distintos, y sé explicar por qué.</td><td>Comparo bien cuando los denominadores son iguales.</td><td>Me guío por el tamaño de los números sin igualar los denominadores.</td></tr>')
# Cierre
R("<p>You now know what a fraction is, and you can make equivalent fractions, simplify, and compare. That is exactly the foundation you need to <strong>calculate</strong> with fractions.</p>", "<p>Ya sabe qué es una fracción, y sabe formar fracciones equivalentes, simplificar y comparar. Esa es justo la base que necesita para <strong>calcular</strong> con fracciones.</p>")
R("<p>In <strong>Lesson 4.2 · Adding and subtracting fractions</strong> you will add and subtract fractions, and you will see why you first need <strong>the same denominator</strong>. The equivalent fractions you practiced today will be your main tool.</p>",
  "<p>En la <strong>Lección 4.2 · Suma y resta de fracciones</strong> sumará y restará fracciones, y verá por qué primero necesita <strong>el mismo denominador</strong>. Las fracciones equivalentes que practicó hoy serán su herramienta principal.</p>")
R('Next: <a href="lesson-4-2.html">Lesson 4.2 · Adding and subtracting fractions</a>', 'Siguiente: <a href="leccion-4-2.html">Lección 4.2 · Suma y resta de fracciones</a>')
R("""<dt>fraction</dt><dd>A number that shows parts of a whole, like 3/4.</dd>
<dt>numerator</dt><dd>The top number of a fraction: how many parts you have.</dd>
<dt>denominator</dt><dd>The bottom number of a fraction: how many equal parts the whole was divided into.</dd>
<dt>equivalent fractions</dt><dd>Fractions with the same value, like 1/2, 2/4, and 5/10.</dd>
<dt>simplify (reduce)</dt><dd>To divide the top and the bottom by the same number to write the fraction with smaller numbers.</dd>
<dt>simplest form</dt><dd>A fraction whose top and bottom share no factor greater than 1, like 2/3.</dd>
<dt>common denominator</dt><dd>The same denominator for two or more fractions, so you can compare, add, or subtract them.</dd>""",
"""<dt>fracción</dt><dd>Un número que muestra partes de un entero, como 3/4.</dd>
<dt>numerador</dt><dd>El número de arriba de una fracción: cuántas partes tiene.</dd>
<dt>denominador</dt><dd>El número de abajo de una fracción: en cuántas partes iguales se dividió el entero.</dd>
<dt>fracciones equivalentes</dt><dd>Fracciones con el mismo valor, como 1/2, 2/4 y 5/10.</dd>
<dt>simplificar (reducir)</dt><dd>Dividir el numerador y el denominador entre el mismo número para escribir la fracción con números más pequeños.</dd>
<dt>forma más simple</dt><dd>Una fracción cuyo numerador y denominador no tienen ningún factor común mayor que 1, como 2/3.</dd>
<dt>denominador común</dt><dd>El mismo denominador para dos o más fracciones, para poder compararlas, sumarlas o restarlas.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.1</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 4 · Lección 4.1</p>")
t.js('''{
 next: "Lección 4.2",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "b",
   hints: { a: "2/3 es el doble de 1/3. Multiplique el numerador y el denominador por el mismo número.", c: "Solo cambió el de abajo. Lo que le haga al denominador, hágaselo también al numerador.", d: "3/6 es un medio, que es más que un tercio. Multiplique 1/3 por 3/3." },
   right: "1 × 3 = 3 y 3 × 3 = 9: multiplicó el numerador y el denominador por el mismo número.",
   solution: "Multiplique el numerador y el denominador de 1/3 por 3: (1 × 3)/(3 × 3) = 3/9. Las dos fracciones son la misma cantidad." },
  p2: { ok: "b",
   hints: { a: "Dividió solo el de arriba. Divida el numerador y el denominador entre el mismo número.", c: "Dividió solo el de abajo. Divida los dos entre 2.", d: "Compruebe: 6 ÷ 2 = 3, no 2." },
   right: "6 ÷ 2 = 3 y 10 ÷ 2 = 5. 3 y 5 no tienen ningún factor común mayor que 1, así que 3/5 es la forma más simple.",
   solution: "6 y 10 se pueden dividir los dos entre 2: 6 ÷ 2 = 3 y 10 ÷ 2 = 5. Así que 6/10 = 3/5, y 3/5 no se puede simplificar más." },
  p3: { ok: "a",
   right: "Mismo denominador: las partes son del mismo tamaño, y 7 partes son más que 4.",
   solution: "Los denominadores son iguales (10), así que las partes son del mismo tamaño. 7 partes son más que 4 partes: 7/10 > 4/10." },
  p4: { ok: "a",
   right: "1/2 = 5/10 y 2/5 = 4/10. 5 décimos son más que 4 décimos.",
   solution: "Use un denominador común, 10: 1/2 = 5/10 y 2/5 = 4/10. Como 5 > 4, 1/2 > 2/5. También puede pensar: 2/5 es menos que la mitad de 5." }
 },
 quiz: {
  A: { ok: "c", hints: { a: "El 5 está arriba: es el numerador.", b: "13 es 5 + 8. El denominador es uno de los dos números.", d: "3 es 8 − 5. El denominador es uno de los dos números." },
   solution: "El denominador es el número de abajo: 8. Dice en cuántas partes iguales se dividió el entero." },
  B: { ok: "b", hints: { a: "2/3 es más que un medio.", c: "1/4 es menos que un medio.", d: "3/8 es menos que un medio (4/8 es un medio)." },
   solution: "5/10: multiplique el numerador y el denominador de 1/2 por 5. Cinco décimos es un medio." },
  C: { ok: "d", hints: { a: "Sumar el mismo número cambia el valor: 1/2 no es igual a 2/3.", b: "Si cambia solo el numerador, la cantidad cambia.", c: "Restar el mismo número cambia el valor." },
   solution: "Multiplique o divida el numerador y el denominador por el mismo número. Así se conserva la misma cantidad." },
  D: { ok: "a", hints: { b: "Dividió solo el de arriba. Divida los dos.", c: "Compruebe: 8 ÷ 4 = 2, pero 4 ÷ 4 = 1.", d: "4/4 es un entero. 4/8 es la mitad." },
   solution: "Divida el numerador y el denominador entre 4: 4 ÷ 4 = 1 y 8 ÷ 4 = 2. Así que 4/8 = 1/2." },
  E: { ok: "b", hints: { a: "9/12 todavía se puede simplificar: 9 y 12 se pueden dividir los dos entre 3.", c: "Dividió solo el de arriba. Divida los dos entre 3.", d: "Compruebe: 9 ÷ 3 = 3, no 1." },
   solution: "9 y 12 se pueden dividir los dos entre 3: 9 ÷ 3 = 3 y 12 ÷ 3 = 4. Así que 9/12 = 3/4." },
  F: { ok: "c", hints: { a: "Mismo denominador: compare los numeradores. ¿Cuál es mayor, 5 o 2?", b: "Tienen el mismo denominador, pero numeradores distintos." },
   solution: "Mismo denominador (9), así que las partes son del mismo tamaño: 5 partes son más que 2. 5/9 > 2/9." },
  G: { ok: "a", hints: { b: "Mismo numerador: cuantas más partes tiene el entero, más pequeña es cada parte.", c: "Un entero cortado en 6 partes tiene partes más pequeñas que uno cortado en 4." },
   solution: "Las dos tienen 1 parte. Un entero cortado en 6 partes tiene partes más pequeñas que uno cortado en 4, así que 1/6 < 1/4." },
  H: { ok: "c", hints: { a: "Convierta 3/4 en octavos: 3/4 = 6/8. ¿Qué es más, 6/8 o 5/8?", b: "Convierta 3/4 en octavos y compare con 5/8." },
   solution: "3/4 = 6/8 (multiplique por 2). 6/8 es más que 5/8, así que se comió más de la pizza de la que se comieron 3/4." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-4-1.html")
