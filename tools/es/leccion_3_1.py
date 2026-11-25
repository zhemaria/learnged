"""Crea es/matematicas/nivel-1/leccion-3-1.html a partir de math/level-1/lesson-3-1.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-3-1.html"); t.leccion("")
R = t.r
t.cabecera("<!-- LearnGED · Lección 3.1 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 3.1 · Decimals: read, write, compare, and round · LearnGED</title>", "<title>Lección 3.1 · Decimales: leer, escribir, comparar y redondear · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 3 — Decimals</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 3 — Decimales</p>')
R("<h1>Lesson 3.1 · Decimals: read, write, compare, and round</h1>", "<h1>Lección 3.1 · Decimales: leer, escribir, comparar y redondear</h1>")
R('<p class="lema">The numbers of money and prices. The place value chart keeps going to the right of the decimal point.</p>', '<p class="lema">Los números del dinero y de los precios. La tabla de valor posicional sigue hacia la derecha del punto decimal.</p>')
R("Connection to money</span>", "Conexión con el dinero</span>")
R("<li><strong>Read and write</strong> decimals to the thousandths, with digits and with words.</li>", "<li><strong>Leer y escribir</strong> decimales hasta las milésimas, con cifras y con palabras.</li>")
R("<li><strong>Name</strong> the place value of a digit to the right of the decimal point.</li>", "<li><strong>Nombrar</strong> el valor posicional de un dígito a la derecha del punto decimal.</li>")
R("<li><strong>Compare and order</strong> decimals with the symbols &gt;, &lt;, and =.</li>", "<li><strong>Comparar y ordenar</strong> decimales con los símbolos &gt;, &lt; e =.</li>")
R("<li><strong>Round</strong> a decimal to the nearest tenth or the nearest hundredth.</li>", "<li><strong>Redondear</strong> un decimal a la décima o a la centésima más cercana.</li>")
R('<li><a href="#s-life">Decimals are already in your life</a></li>', '<li><a href="#s-vida">Los decimales ya están en su vida</a></li>')
R('<li><a href="#s-place">Place value after the decimal point</a></li>', '<li><a href="#s-valor">El valor posicional después del punto</a></li>')
R('<li><a href="#s-compare">Compare and order decimals</a></li>', '<li><a href="#s-comparar">Comparar y ordenar decimales</a></li>')
R('<li><a href="#s-round">Round decimals</a></li>', '<li><a href="#s-redondear">Redondear decimales</a></li>')
# 1
R('<h2 id="s-life"><span aria-hidden="true" class="num-seccion">1</span>Decimals are already in your life</h2>', '<h2 id="s-vida"><span aria-hidden="true" class="num-seccion">1</span>Los decimales ya están en su vida</h2>')
R("<p>You use decimals every day, even if you do not call them that. A product costs <strong>$3.99</strong>. Gas is <strong>$2.75</strong> a gallon. A recipe asks for <strong>1.5 pounds</strong> of meat. All of these are decimal numbers.</p>",
  "<p>Usted usa decimales todos los días, aunque no los llame así. Un producto cuesta <strong>$3.99</strong>. La gasolina está a <strong>$2.75</strong> el galón. Una receta pide <strong>1.5 libras</strong> de carne. Todos esos son números decimales.</p>")
R("<p>A <strong>decimal</strong> is a way to write <strong>parts of a whole</strong>. The <strong>decimal point</strong> separates the whole part (on the left) from the part that is less than one (on the right). In <strong>$3.99</strong>, the <strong>3</strong> is 3 whole dollars, and the <strong>.99</strong> is 99 cents: a part of a dollar.</p>",
  "<p>Un <strong>decimal</strong> es una forma de escribir <strong>partes de un entero</strong>. El <strong>punto decimal</strong> separa la parte entera (a la izquierda) de la parte que es menor que uno (a la derecha). En <strong>$3.99</strong>, el <strong>3</strong> son 3 dólares completos, y el <strong>.99</strong> son 99 centavos: una parte de un dólar.</p>")
R('<span class="etiqueta et-verde">Connection to Topic 1</span>', '<span class="etiqueta et-verde">Conexión con el Tema 1</span>')
R("<p>In Lesson 1.1 you learned the place value chart: ones, tens, hundreds… Decimals are <strong>the same chart, continued to the right</strong>. Each place to the right of the point is worth <strong>10 times less</strong> than the place before it.</p>",
  "<p>En la Lección 1.1 aprendió la tabla de valor posicional: unidades, decenas, centenas… Los decimales son <strong>la misma tabla, continuada hacia la derecha</strong>. Cada lugar a la derecha del punto vale <strong>10 veces menos</strong> que el lugar anterior.</p>")
# 2
R('<h2 id="s-place"><span aria-hidden="true" class="num-seccion">2</span>Place value after the decimal point</h2>', '<h2 id="s-valor"><span aria-hidden="true" class="num-seccion">2</span>El valor posicional después del punto</h2>')
R("<p>To the right of the decimal point, the places are called <strong>tenths</strong>, <strong>hundredths</strong>, and <strong>thousandths</strong>. Notice the <strong>-ths</strong> at the end: it tells you the place is a part of one. Here is the number <strong>4.625</strong> in the chart:</p>",
  "<p>A la derecha del punto decimal, los lugares se llaman <strong>décimas</strong>, <strong>centésimas</strong> y <strong>milésimas</strong>. Fíjese en la terminación <strong>-ésimas</strong>: le dice que el lugar es una parte de uno. Este es el número <strong>4.625</strong> en la tabla:</p>")
R('aria-label="Place value of 4.625 (tabla desplazable horizontalmente)"', 'aria-label="Valor posicional de 4.625 (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Place value of the number 4.625: 4 ones, 6 tenths, 2 hundredths, and 5 thousandths</caption>', '<caption class="cap-oculto">Valor posicional del número 4.625: 4 unidades, 6 décimas, 2 centésimas y 5 milésimas</caption>')
R('<tr><th scope="col">Ones</th><th scope="col">Decimal point</th><th scope="col">Tenths</th><th scope="col">Hundredths</th><th scope="col">Thousandths</th></tr>', '<tr><th scope="col">Unidades</th><th scope="col">Punto decimal</th><th scope="col">Décimas</th><th scope="col">Centésimas</th><th scope="col">Milésimas</th></tr>')
R('<td class="pie-grupo">Whole part</td>', '<td class="pie-grupo">Parte entera</td>')
R('<td class="pie-grupo" colspan="3">Decimal part</td>', '<td class="pie-grupo" colspan="3">Parte decimal</td>')
R('<span aria-hidden="true">📖</span> How to read 4.625</p>', '<span aria-hidden="true">📖</span> Cómo leer 4.625</p>')
R('<strong>Step 1.</strong> Read the whole part: "four."', '<strong>Paso 1.</strong> Lea la parte entera: «cuatro».')
R('<strong>Step 2.</strong> Read the decimal point as <strong>"and."</strong>', '<strong>Paso 2.</strong> Lea el punto decimal como <strong>«con»</strong>.')
R('<strong>Step 3.</strong> Read the decimal part as a whole number, <strong>625</strong>, and then say the name of the <strong>last place</strong>. The 5 is in the thousandths.', '<strong>Paso 3.</strong> Lea la parte decimal como un número entero, <strong>625</strong>, y después diga el nombre del <strong>último lugar</strong>. El 5 está en las milésimas.')
R('<strong>Result.</strong> "Four <strong>and</strong> six hundred twenty-five <strong>thousandths</strong>."', '<strong>Resultado.</strong> «Cuatro <strong>con</strong> seiscientas veinticinco <strong>milésimas</strong>».')
R('<span class="etiqueta et-verde">Good to know</span>', '<span class="etiqueta et-verde">Bueno saberlo</span>')
R("<p>In everyday talk, people also say \"four <strong>point</strong> six two five.\" Both ways are correct. With money, we say dollars and cents: $3.99 is \"three dollars <strong>and</strong> ninety-nine cents.\" Remember from Lesson 1.1: we do <strong>not</strong> use \"and\" when we read whole numbers. The word \"and\" is saved for the decimal point.</p>",
  "<p>En la conversación diaria también se dice «cuatro <strong>punto</strong> seis dos cinco». Las dos formas son correctas. Con el dinero decimos dólares y centavos: $3.99 es «tres dólares <strong>con</strong> noventa y nueve centavos». La palabra «con» se reserva para el punto decimal: al leer números enteros no se usa.</p>")
R("<p>The <strong>last place</strong> gives the name. <strong>0.7</strong> is \"seven <strong>tenths</strong>.\" <strong>0.07</strong> is \"seven <strong>hundredths</strong>.\" <strong>0.007</strong> is \"seven <strong>thousandths</strong>.\" It is the same digit 7, but its place changes its value, just like with whole numbers.</p>",
  "<p>El <strong>último lugar</strong> da el nombre. <strong>0.7</strong> es «siete <strong>décimas</strong>». <strong>0.07</strong> es «siete <strong>centésimas</strong>». <strong>0.007</strong> es «siete <strong>milésimas</strong>». Es el mismo dígito 7, pero su lugar cambia su valor, igual que en los números enteros.</p>")
R("<h3>Practice 1 — Place value after the point</h3>", "<h3>Práctica 1 — El valor posicional después del punto</h3>")
R("In the number <strong>8.<u>3</u>5</strong>, which place is the underlined digit <strong>3</strong> in?", "En el número <strong>8.<u>3</u>5</strong>, ¿en qué lugar está el dígito subrayado, el <strong>3</strong>?")
R('type="button">The ones</button>', 'type="button">En las unidades</button>')
R('type="button">The tenths</button>', 'type="button">En las décimas</button>')
R('type="button">The hundredths</button>', 'type="button">En las centésimas</button>')
R('type="button">The thousandths</button>', 'type="button">En las milésimas</button>')
R('href="practice-3-1.html#place-value"', 'href="practica-3-1.html#valor-posicional"')
R('práctica: place value after the point (se abre', 'práctica: el valor posicional después del punto (se abre')
R('<span class="ei-titulo">Practique más: place value after the point</span><span class="ei-sub">Put any decimal in the chart, find tenths, hundredths, and thousandths, and read decimals in words.</span>', '<span class="ei-titulo">Practique más: el valor posicional después del punto</span><span class="ei-sub">Ponga cualquier decimal en la tabla, encuentre décimas, centésimas y milésimas, y lea decimales con palabras.</span>')
# 3
R('<h2 id="s-compare"><span aria-hidden="true" class="num-seccion">3</span>Compare and order decimals</h2>', '<h2 id="s-comparar"><span aria-hidden="true" class="num-seccion">3</span>Comparar y ordenar decimales</h2>')
R("<p>Comparing decimals is a lot like comparing whole numbers, with one important rule: compare <strong>place by place, from left to right</strong>, starting with the whole part.</p>", "<p>Comparar decimales se parece mucho a comparar números enteros, con una regla importante: se compara <strong>lugar por lugar, de izquierda a derecha</strong>, empezando por la parte entera.</p>")
R("<h3>The trick: add zeros on the right</h3>", "<h3>El truco: agregar ceros a la derecha</h3>")
R("<p>When two decimals have a different number of digits after the point, you can <strong>add zeros on the right</strong> without changing the value. <strong>0.5</strong> is the same as <strong>0.50</strong> and <strong>0.500</strong>. Then both numbers have the same \"length,\" and they are easy to compare.</p>",
  "<p>Cuando dos decimales tienen distinta cantidad de dígitos después del punto, puede <strong>agregar ceros a la derecha</strong> sin cambiar el valor. <strong>0.5</strong> es lo mismo que <strong>0.50</strong> y que <strong>0.500</strong>. Así los dos números tienen la misma «longitud» y son fáciles de comparar.</p>")
R('<p class="titulo-ej">Example: compare 0.6 and 0.58</p>', '<p class="titulo-ej">Ejemplo: compare 0.6 y 0.58</p>')
R('<strong>Step 1.</strong> Make them the same length: write 0.6 as <strong>0.60</strong>.', '<strong>Paso 1.</strong> Iguale la longitud: escriba 0.6 como <strong>0.60</strong>.')
R('<strong>Step 2.</strong> Compare 0.60 and 0.58 place by place. Tenths: 6 and 5.', '<strong>Paso 2.</strong> Compare 0.60 y 0.58 lugar por lugar. Décimas: 6 y 5.')
R('<strong>Step 3.</strong> 6 is greater than 5. That decides it.', '<strong>Paso 3.</strong> 6 es mayor que 5. Eso lo decide.')
R('<strong>Result.</strong> <strong>0.6 &gt; 0.58</strong>.', '<strong>Resultado.</strong> <strong>0.6 &gt; 0.58</strong>.')
R("<p>Many people think 0.58 is greater than 0.6 \"because it has more digits.\" <strong>That is not true.</strong> With decimals, more digits do not mean a greater value. That is why it helps to add zeros and make the numbers the same length before you compare.</p>",
  "<p>Mucha gente piensa que 0.58 es mayor que 0.6 «porque tiene más dígitos». <strong>No es cierto.</strong> En los decimales, más dígitos no quiere decir más valor. Por eso ayuda agregar ceros e igualar la longitud antes de comparar.</p>")
R("<h3>Decimals on the number line</h3>", "<h3>Los decimales en la recta numérica</h3>")
R("<p>To order decimals, picture them on a number line. Between 0 and 1 there are endless decimals. The farther right a number is, the greater it is:</p>", "<p>Para ordenar decimales, imagínelos en la recta numérica. Entre 0 y 1 hay infinitos decimales. Cuanto más a la derecha está un número, mayor es:</p>")
R('aria-label="Number line from 0 to 1, marked at 0.25, 0.5, and 0.75. The point 0.3 is a little to the right of 0.25, and the point 0.8 is a little to the right of 0.75."', 'aria-label="Recta numérica de 0 a 1, con marcas en 0.25, 0.5 y 0.75. El punto 0.3 está un poco a la derecha de 0.25, y el punto 0.8 está un poco a la derecha de 0.75."')
R('href="infinite-decimals.html"', 'href="decimales-infinitos.html"')
R('aria-label="Open the activity: decimals never end (se abre en una pestaña nueva)"', 'aria-label="Abrir la actividad: los decimales no se acaban (se abre en una pestaña nueva)"')
R('<span class="ei-titulo">Explore: decimals never end</span><span class="ei-sub">Zoom in on the number line again and again, see why 0.1 = 0.10 = 0.100, and see what rounding really means.</span>', '<span class="ei-titulo">Explore: los decimales no se acaban</span><span class="ei-sub">Acérquese a la recta numérica una y otra vez, vea por qué 0.1 = 0.10 = 0.100 y qué quiere decir de verdad redondear.</span>')
R("<h3>Practice 2 — Compare decimals</h3>", "<h3>Práctica 2 — Comparar decimales</h3>")
R("Which symbol goes between <strong>2.07</strong> and <strong>2.7</strong>?", "¿Qué símbolo va entre <strong>2.07</strong> y <strong>2.7</strong>?")
R("<h3>Practice 3 — Order prices</h3>", "<h3>Práctica 3 — Ordenar precios</h3>")
R("Four products cost $1.50, $1.05, $1.55, and $1.15. Which one is the <strong>cheapest</strong>?", "Cuatro productos cuestan $1.50, $1.05, $1.55 y $1.15. ¿Cuál es el <strong>más barato</strong>?")
R('href="practice-3-1.html#compare"', 'href="practica-3-1.html#comparar"', 2)
R('práctica: compare and order decimals (se abre', 'práctica: comparar y ordenar decimales (se abre')
R('<span class="ei-titulo">Practique más: compare and order decimals</span><span class="ei-sub">Compare place by place and see both decimals on the number line.</span>', '<span class="ei-titulo">Practique más: comparar y ordenar decimales</span><span class="ei-sub">Compare lugar por lugar y vea los dos decimales en la recta numérica.</span>')
# 4
R('<h2 id="s-round"><span aria-hidden="true" class="num-seccion">4</span>Round decimals</h2>', '<h2 id="s-redondear"><span aria-hidden="true" class="num-seccion">4</span>Redondear decimales</h2>')
R("<p>To round decimals, use <strong>the same \"neighbor on the right\" rule</strong> you learned in Lesson 1.1. The difference is that now you work to the right of the point.</p>", "<p>Para redondear decimales, use <strong>la misma regla del «vecino de la derecha»</strong> que aprendió en la Lección 1.1. La diferencia es que ahora trabaja a la derecha del punto.</p>")
R("<li>Look at the digit <strong>to the right</strong> of the place you are rounding to.</li>", "<li>Mire el dígito <strong>a la derecha</strong> del lugar al que redondea.</li>")
R("<li>If it is <strong>0, 1, 2, 3, or 4</strong>, the digit stays the same.</li>", "<li>Si es <strong>0, 1, 2, 3 o 4</strong>, el dígito se queda igual.</li>")
R("<li>If it is <strong>5, 6, 7, 8, or 9</strong>, the digit goes up by one.</li>", "<li>Si es <strong>5, 6, 7, 8 o 9</strong>, el dígito sube uno.</li>")
R("<li>The digits to the right of that place are <strong>dropped</strong>. They do not turn into zeros like with whole numbers: they just go away.</li>", "<li>Los dígitos a la derecha de ese lugar <strong>se eliminan</strong>. No se vuelven ceros como en los números enteros: simplemente desaparecen.</li>")
R('<p class="titulo-ej">Example: round 5.348 to the nearest tenth</p>', '<p class="titulo-ej">Ejemplo: redondee 5.348 a la décima más cercana</p>')
R('<strong>Step 1.</strong> The place is the <strong>tenths</strong>: the digit 3.', '<strong>Paso 1.</strong> El lugar es el de las <strong>décimas</strong>: el dígito 3.')
R('<strong>Step 2.</strong> Look at its neighbor on the right (the hundredths): it is <strong>4</strong>.', '<strong>Paso 2.</strong> Mire su vecino de la derecha (las centésimas): es <strong>4</strong>.')
R('<strong>Step 3.</strong> 4 is less than 5, so the tenths digit stays 3. Drop the digits after it.', '<strong>Paso 3.</strong> 4 es menor que 5, así que el dígito de las décimas se queda en 3. Elimine los dígitos que siguen.')
R('<strong>Result.</strong> <strong>5.3</strong>.', '<strong>Resultado.</strong> <strong>5.3</strong>.')
R('<p class="titulo-ej">Example: round 5.348 to the nearest hundredth</p>', '<p class="titulo-ej">Ejemplo: redondee 5.348 a la centésima más cercana</p>')
R('<strong>Step 1.</strong> The place is the <strong>hundredths</strong>: the digit 4.', '<strong>Paso 1.</strong> El lugar es el de las <strong>centésimas</strong>: el dígito 4.')
R('<strong>Step 2.</strong> Look at its neighbor on the right (the thousandths): it is <strong>8</strong>.', '<strong>Paso 2.</strong> Mire su vecino de la derecha (las milésimas): es <strong>8</strong>.')
R('<strong>Step 3.</strong> 8 is 5 or more, so the hundredths digit goes up from 4 to 5.', '<strong>Paso 3.</strong> 8 es 5 o más, así que el dígito de las centésimas sube de 4 a 5.')
R('<strong>Result.</strong> <strong>5.35</strong>.', '<strong>Resultado.</strong> <strong>5.35</strong>.')
R('<span class="etiqueta et-verde">In real life: round to the cent</span>', '<span class="etiqueta et-verde">En la vida real: redondear al centavo</span>')
R("<p>Rounding to the hundredth is rounding \"to the cent.\" A cash register does this when a calculation gives $4.617: you pay <strong>$4.62</strong>.</p>", "<p>Redondear a la centésima es redondear «al centavo». La caja registradora lo hace cuando un cálculo da $4.617: usted paga <strong>$4.62</strong>.</p>")
R("<h3>Practice 4 — Round</h3>", "<h3>Práctica 4 — Redondear</h3>")
R("Round <strong>9.276</strong> to the nearest <strong>tenth</strong>.", "Redondee <strong>9.276</strong> a la <strong>décima</strong> más cercana.")
R('href="practice-3-1.html#round"', 'href="practica-3-1.html#redondear"')
R('práctica: round decimals (se abre', 'práctica: redondear decimales (se abre')
R('<span class="ei-titulo">Practique más: round decimals</span><span class="ei-sub">Use the neighbor-on-the-right rule and see the rounding on the number line.</span>', '<span class="ei-titulo">Practique más: redondear decimales</span><span class="ei-sub">Use la regla del vecino de la derecha y vea el redondeo en la recta numérica.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-3-1.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-3-1.html">página de práctica de esta lección</a> ')
R('<li><strong>The number line.</strong> Go back to the <a href="practica-3-1.html#comparar">number line in the practice activity</a> and place ten different decimals. Seeing the point on the line is what convinces you that 0.8 is greater than 0.75, even though 75 is greater than 8.</li>',
  '<li><strong>La recta numérica.</strong> Vuelva a la <a href="practica-3-1.html#comparar">recta numérica de la actividad de práctica</a> y ubique diez decimales distintos. Ver el punto en la recta es lo que lo convence de que 0.8 es mayor que 0.75, aunque 75 sea mayor que 8.</li>')
R("<li><strong>In your daily life.</strong> Look at three real prices from a store or a receipt. Write them in words, order them from least to greatest, and round each one to the nearest dollar.</li>",
  "<li><strong>En su vida diaria.</strong> Busque tres precios reales de una tienda o de un recibo. Escríbalos con palabras, ordénelos de menor a mayor y redondee cada uno al dólar más cercano.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> without a calculator and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> sin calculadora y pulse <strong>Revisar mis respuestas</strong>.")
R("In the number <strong>6.<u>4</u>9</strong>, which place is the underlined digit <strong>4</strong> in?", "En el número <strong>6.<u>4</u>9</strong>, ¿en qué lugar está el dígito subrayado, el <strong>4</strong>?")
R('type="button">Tenths</button><button class="opcion" data-k="b" type="button">Hundredths</button><button class="opcion" data-k="c" type="button">Thousandths</button><button class="opcion" data-k="d" type="button">Ones</button>',
  'type="button">Décimas</button><button class="opcion" data-k="b" type="button">Centésimas</button><button class="opcion" data-k="c" type="button">Milésimas</button><button class="opcion" data-k="d" type="button">Unidades</button>')
R("How do you write <strong>\"three and eight hundredths\"</strong> with digits?", "¿Cómo se escribe con cifras <strong>«tres con ocho centésimas»</strong>?")
R("Which number is <strong>equal</strong> to <strong>0.4</strong>?", "¿Qué número es <strong>igual</strong> a <strong>0.4</strong>?")
R("Which symbol makes this true: <strong>0.9 ___ 0.85</strong>?", "¿Qué símbolo hace verdadera esta comparación: <strong>0.9 ___ 0.85</strong>?")
R('type="button">&lt; (less than)</button><button class="opcion" data-k="b" type="button">= (equal to)</button><button class="opcion" data-k="c" type="button">&gt; (greater than)</button>', 'type="button">&lt; (menor que)</button><button class="opcion" data-k="b" type="button">= (igual a)</button><button class="opcion" data-k="c" type="button">&gt; (mayor que)</button>')
R("Which decimal is the <strong>greatest</strong>?", "¿Qué decimal es el <strong>mayor</strong>?")
R("Round <strong>3.471</strong> to the nearest <strong>tenth</strong>.", "Redondee <strong>3.471</strong> a la <strong>décima</strong> más cercana.")
R("Round <strong>$12.834</strong> to the nearest <strong>hundredth</strong> (to the cent).", "Redondee <strong>$12.834</strong> a la <strong>centésima</strong> más cercana (al centavo).")
R("Three runners had these times: 10.5 seconds, 10.45 seconds, and 10.6 seconds. Who was the <strong>fastest</strong> (the shortest time)?", "Tres corredores hicieron estos tiempos: 10.5 segundos, 10.45 segundos y 10.6 segundos. ¿Quién fue el <strong>más rápido</strong> (el menor tiempo)?")
R('type="button">The runner with 10.5 s</button><button class="opcion" data-k="b" type="button">The runner with 10.45 s</button><button class="opcion" data-k="c" type="button">The runner with 10.6 s</button><button class="opcion" data-k="d" type="button">They all tied</button>',
  'type="button">El de 10.5 s</button><button class="opcion" data-k="b" type="button">El de 10.45 s</button><button class="opcion" data-k="c" type="button">El de 10.6 s</button><button class="opcion" data-k="d" type="button">Empataron todos</button>')
# Lista
R('aria-label="Self-check checklist for decimals (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de decimales (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: decimal skills ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas con decimales ')
R('<tr><th scope="row">Read a decimal with three places</th><td>I read tenths, hundredths, and thousandths correctly.</td><td>I read tenths well, but I am not sure with thousandths.</td><td>I do not say the name of the decimal place.</td></tr>',
  '<tr><th scope="row">Leer un decimal de tres lugares</th><td>Leo bien las décimas, las centésimas y las milésimas.</td><td>Leo bien las décimas, pero dudo con las milésimas.</td><td>No digo el nombre del lugar decimal.</td></tr>')
R('<tr><th scope="row">Name the place of a decimal digit</th><td>I name the place of any digit with confidence.</td><td>I get tenths and hundredths right.</td><td>I mix up the places.</td></tr>',
  '<tr><th scope="row">Nombrar el lugar de un dígito decimal</th><td>Nombro con seguridad el lugar de cualquier dígito.</td><td>Acierto con las décimas y las centésimas.</td><td>Confundo los lugares.</td></tr>')
R('<tr><th scope="row">Compare two decimals</th><td>I use &gt;, &lt;, and = correctly, and I add zeros to make the numbers the same length.</td><td>I compare well, but sometimes I go by the number of digits.</td><td>I cannot decide which decimal is greater.</td></tr>',
  '<tr><th scope="row">Comparar dos decimales</th><td>Uso bien &gt;, &lt; e =, y agrego ceros para igualar la longitud de los números.</td><td>Comparo bien, pero a veces me guío por la cantidad de dígitos.</td><td>No logro decidir qué decimal es mayor.</td></tr>')
R('<tr><th scope="row">Round to a given place</th><td>I round to the tenth and to the hundredth correctly.</td><td>I use the rule, with a small mistake now and then.</td><td>I do not use the neighbor-on-the-right rule.</td></tr>',
  '<tr><th scope="row">Redondear al lugar pedido</th><td>Redondeo bien a la décima y a la centésima.</td><td>Uso la regla, con algún error pequeño de vez en cuando.</td><td>No uso la regla del vecino de la derecha.</td></tr>')
# Cierre
R("<p>You can now read, write, compare, and round decimals. Next, you will <strong>calculate</strong> with them. In <strong>Lesson 3.2 · Operations with decimals</strong> you will line up the decimal point to add and subtract, and you will learn where the point goes when you multiply and divide.</p>",
  "<p>Ya sabe leer, escribir, comparar y redondear decimales. Ahora va a <strong>calcular</strong> con ellos. En la <strong>Lección 3.2 · Operaciones con decimales</strong> alineará el punto decimal para sumar y restar, y aprenderá dónde va el punto al multiplicar y dividir.</p>")
R("<p>In the next lesson you will also start using a new tool: the <strong>TI-30XS</strong> calculator. You will use it to <strong>check</strong> your answers, never to replace your work on paper. Start a good habit now: <strong>clear the calculator's memory before you begin</strong>.</p>",
  "<p>En la próxima lección también empezará a usar una herramienta nueva: la calculadora <strong>TI-30XS</strong>. La usará para <strong>comprobar</strong> sus respuestas, nunca para reemplazar su trabajo en papel. Empiece ya un buen hábito: <strong>borre la memoria de la calculadora antes de empezar</strong>.</p>")
R('Next: <a href="lesson-3-2.html">Lesson 3.2 · Operations with decimals</a>', 'Siguiente: <a href="leccion-3-2.html">Lección 3.2 · Operaciones con decimales</a>')
R("""<dt>decimal</dt><dd>A number with a decimal point. It shows a whole part and a part that is less than one. Example: 3.99.</dd>
<dt>decimal point</dt><dd>The dot that separates the whole part (left) from the decimal part (right). We read it as "and."</dd>
<dt>tenth, hundredth, thousandth</dt><dd>The first three places to the right of the point. 0.1 is one tenth, 0.01 is one hundredth, 0.001 is one thousandth.</dd>
<dt>greater than (&gt;), less than (&lt;)</dt><dd>Symbols to compare two numbers. The open side faces the greater number: 0.6 &gt; 0.58.</dd>
<dt>round to the nearest…</dt><dd>To change a number to a simpler one close to it, keeping only up to a certain place. 5.348 rounded to the nearest tenth is 5.3.</dd>""",
"""<dt>decimal</dt><dd>Un número con punto decimal. Muestra una parte entera y una parte menor que uno. Ejemplo: 3.99.</dd>
<dt>punto decimal</dt><dd>El punto que separa la parte entera (a la izquierda) de la parte decimal (a la derecha). Se lee «con».</dd>
<dt>décima, centésima, milésima</dt><dd>Los tres primeros lugares a la derecha del punto. 0.1 es una décima, 0.01 es una centésima y 0.001 es una milésima.</dd>
<dt>mayor que (&gt;), menor que (&lt;)</dt><dd>Símbolos para comparar dos números. El lado abierto mira al número mayor: 0.6 &gt; 0.58.</dd>
<dt>redondear a la … más cercana</dt><dd>Cambiar un número por otro más sencillo y cercano, conservando solo hasta cierto lugar. 5.348 redondeado a la décima más cercana es 5.3.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 3 · Lesson 3.1</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 3 · Lección 3.1</p>")
t.js('''{
 next: "Lección 3.2",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "b",
   hints: { a: "Las unidades están a la izquierda del punto. El 3 está a la derecha.", c: "Cuente los lugares después del punto: el 3 está en el primero.", d: "Las milésimas son el tercer lugar después del punto. 8.35 tiene solo dos lugares." },
   right: "El primer lugar después del punto es el de las décimas.",
   solution: "En 8.35, el primer lugar a la derecha del punto es el de las décimas. Así que el 3 está en las décimas: vale 0.3." },
  p2: { ok: "b",
   hints: { a: "Más dígitos no quiere decir más valor. Escriba 2.7 como 2.70 y compare las décimas.", c: "El cero después del punto cambia el valor. Escriba 2.7 como 2.70 y compare." },
   right: "Escriba 2.7 como 2.70. En las décimas, 0 es menor que 7.",
   solution: "Iguale la longitud: 2.07 y 2.70. Las partes enteras son iguales (2). En las décimas, 0 es menor que 7. Así que 2.07 &lt; 2.7." },
  p3: { ok: "b",
   hints: { a: "Mire las décimas: 1.50 tiene un 5. ¿Hay algún precio con un dígito menor en las décimas?", c: "Ese es el más caro. La pregunta pide el más barato.", d: "Compare las décimas: 1.15 tiene un 1, y 1.05 tiene un 0." },
   right: "Todos los precios tienen $1. En las décimas, $1.05 tiene el dígito menor: 0.",
   solution: "Todos los precios empiezan con $1, así que compare las décimas: 5, 0, 5, 1. La menor es 0, en $1.05. En orden: $1.05 &lt; $1.15 &lt; $1.50 &lt; $1.55." },
  p4: { ok: "b",
   hints: { a: "Mire el vecino de la derecha de las décimas: es 7. Con 5 o más, el dígito sube.", c: "Eso es redondear a la centésima. La pregunta pide la décima: deje un solo dígito después del punto.", d: "Eso es redondear al entero. Redondee a la décima: un dígito después del punto." },
   right: "El vecino de las décimas (2) es 7: 5 o más, así que el 2 sube a 3.",
   solution: "El dígito de las décimas es 2. Su vecino de la derecha es 7. Como 7 es 5 o más, el 2 sube a 3, y se elimina lo demás: 9.3." }
 },
 quiz: {
  A: { ok: "a", hints: { b: "Las centésimas son el segundo lugar después del punto. ¿Dónde está el 4?", c: "Las milésimas son el tercer lugar después del punto. 6.49 tiene solo dos.", d: "Las unidades están a la izquierda del punto. El 4 está a la derecha." },
   solution: "El 4 es el primer dígito después del punto: el lugar de las décimas. Vale 0.4." },
  B: { ok: "d", hints: { a: "3.8 es tres con ocho décimas. Necesita centésimas: dos lugares después del punto.", b: "3.008 es tres con ocho milésimas: tres lugares después del punto.", c: "3.80 es lo mismo que 3.8: ocho décimas. El 8 tiene que ir en el segundo lugar." },
   solution: "«Centésimas» quiere decir dos lugares después del punto, y el 8 va en el último: 3.08." },
  C: { ok: "b", hints: { a: "0.04 son cuatro centésimas. Eso es menos que cuatro décimas.", c: "4.0 son cuatro unidades enteras, no cuatro décimas.", d: "0.004 son cuatro milésimas, mucho menos que cuatro décimas." },
   solution: "Un cero a la derecha no cambia el valor: 0.4 = 0.40. Los dos son cuatro décimas." },
  D: { ok: "c", hints: { a: "Escriba 0.9 como 0.90 y compare las décimas: 9 y 8.", b: "No son iguales. Escriba 0.9 como 0.90 y compare." },
   solution: "Escriba 0.9 como 0.90. En las décimas, 9 es mayor que 8. Así que 0.9 &gt; 0.85." },
  E: { ok: "d", hints: { a: "Escríbalos todos con tres lugares: 0.700, 0.680, 0.709, 0.720. ¿Cuál es el mayor?", b: "0.68 es el menor: tiene un 6 en las décimas.", c: "Más dígitos no quiere decir más valor. Compare 0.709 y 0.720 en las centésimas." },
   solution: "Con tres lugares: 0.700, 0.680, 0.709, 0.720. En las décimas, tres tienen un 7. En las centésimas, 0.720 tiene un 2, el mayor. Así que 0.72 es el mayor." },
  F: { ok: "a", hints: { b: "El vecino de la derecha de las décimas es 7. Con 5 o más, el dígito sube.", c: "Eso es redondear a la centésima. Deje un solo dígito después del punto.", d: "Eso es redondear al entero. Redondee a la décima." },
   solution: "El dígito de las décimas es 4. Su vecino de la derecha es 7, que es 5 o más, así que el 4 sube a 5: 3.5." },
  G: { ok: "c", hints: { a: "El vecino de la derecha de las centésimas es 4. Con 4 o menos, el dígito se queda igual.", b: "Eso es redondear a la décima. Al centavo quiere decir dos dígitos después del punto.", d: "Eso es redondear al dólar entero. Redondee al centavo." },
   solution: "El dígito de las centésimas es 3. Su vecino de la derecha es 4, que es menor que 5, así que el 3 se queda: $12.83." },
  H: { ok: "b", hints: { a: "Escriba todos los tiempos con dos lugares: 10.50, 10.45, 10.60. ¿Cuál es el menor?", c: "Ese es el tiempo más largo, así que es el corredor más lento.", d: "Los tiempos son distintos. Escríbalos con dos lugares y compare." },
   solution: "Con dos lugares: 10.50, 10.45, 10.60. El menor es 10.45 segundos. El menor tiempo es el del corredor más rápido." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-3-1.html")
