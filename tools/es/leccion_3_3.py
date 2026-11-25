"""Crea es/matematicas/nivel-1/leccion-3-3.html a partir de math/level-1/lesson-3-3.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-3-3.html"); t.leccion("")
R = t.r
t.cabecera("<!-- LearnGED · Lección 3.3 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 3.3 · Decimals in context and equivalent forms · LearnGED</title>", "<title>Lección 3.3 · Decimales en contexto y formas equivalentes · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 3 — Decimals</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 3 — Decimales</p>')
R("<h1>Lesson 3.3 · Decimals in context and equivalent forms</h1>", "<h1>Lección 3.3 · Decimales en contexto y formas equivalentes</h1>")
R('<p class="lema">Change fractions to decimals and decimals to fractions, and solve real problems about shopping, distances, and measurements.</p>', '<p class="lema">Convierta fracciones en decimales y decimales en fracciones, y resuelva problemas reales de compras, distancias y medidas.</p>')
R("Fraction ↔ decimal</span>", "Fracción ↔ decimal</span>")
R("<li><strong>Change</strong> a common fraction to a decimal by dividing the numerator by the denominator.</li>", "<li><strong>Convertir</strong> una fracción común en decimal dividiendo el numerador entre el denominador.</li>")
R("<li><strong>Change</strong> a decimal to a fraction and simplify it.</li>", "<li><strong>Convertir</strong> un decimal en fracción y simplificarla.</li>")
R("<li><strong>Recognize</strong> the most common fraction–decimal pairs.</li>", "<li><strong>Reconocer</strong> las parejas fracción–decimal más comunes.</li>")
R("<li><strong>Solve</strong> real problems with decimals: shopping, distances, measurements, and change.</li>", "<li><strong>Resolver</strong> problemas reales con decimales: compras, distancias, medidas y cambio.</li>")
R('<li><a href="#s-two-ways">Two ways to write the same thing</a></li>', '<li><a href="#s-dos-formas">Dos formas de escribir lo mismo</a></li>')
R('<li><a href="#s-fraction-to-decimal">From fraction to decimal: divide</a></li>', '<li><a href="#s-fraccion-a-decimal">De fracción a decimal: dividir</a></li>')
R('<li><a href="#s-decimal-to-fraction">From decimal to fraction: read and simplify</a></li>', '<li><a href="#s-decimal-a-fraccion">De decimal a fracción: leer y simplificar</a></li>')
R('<li><a href="#s-memorize">Pairs worth knowing by heart</a></li>', '<li><a href="#s-memoria">Parejas que conviene saber de memoria</a></li>')
R('<li><a href="#s-real-life">Decimals in real-life problems</a></li>', '<li><a href="#s-vida-real">Los decimales en problemas de la vida real</a></li>')
t.todas('<span aria-hidden="true">🧮</span> Open the calculator</button>', '<span aria-hidden="true">🧮</span> Abrir la calculadora</button>')
t.todas('<span class="et-calc"><span aria-hidden="true">🧮</span> Check it on the calculator</span>', '<span class="et-calc"><span aria-hidden="true">🧮</span> Compruébelo en la calculadora</span>')
t.todas("<strong>Step 1.</strong>", "<strong>Paso 1.</strong>"); t.todas("<strong>Step 2.</strong>", "<strong>Paso 2.</strong>"); t.todas("<strong>Result.</strong>", "<strong>Resultado.</strong>")
# 1
R('<h2 id="s-two-ways"><span aria-hidden="true" class="num-seccion">1</span>Two ways to write the same thing</h2>', '<h2 id="s-dos-formas"><span aria-hidden="true" class="num-seccion">1</span>Dos formas de escribir lo mismo</h2>')
R("<p>In Lesson 3.1 you saw that a decimal is a <strong>part of a whole</strong>. A fraction is a part of a whole too. In fact, they are <strong>two ways to write the same value</strong>.</p>",
  "<p>En la Lección 3.1 vio que un decimal es una <strong>parte de un entero</strong>. Una fracción también es una parte de un entero. De hecho, son <strong>dos formas de escribir el mismo valor</strong>.</p>")
R('<p>Think about money: half a dollar can be written as the fraction <span class="fracc" aria-hidden="true"><span class="fa">1</span><span class="fb2">2</span></span><span class="cap-oculto">1/2</span> of a dollar, or as the decimal <strong>$0.50</strong>. It is the same amount of money. Only the way you write it changes.</p>',
  '<p>Piense en el dinero: medio dólar se puede escribir como la fracción <span class="fracc" aria-hidden="true"><span class="fa">1</span><span class="fb2">2</span></span><span class="cap-oculto">1/2</span> de dólar, o como el decimal <strong>$0.50</strong>. Es la misma cantidad de dinero. Solo cambia la forma de escribirla.</p>')
R('<p>The bar in a fraction means <strong>"divided by."</strong> The fraction <span class="fracc" aria-hidden="true"><span class="fa">3</span><span class="fb2">4</span></span><span class="cap-oculto">3/4</span> means, exactly, <strong>3 ÷ 4</strong>. That is the key to changing any fraction to a decimal.</p>',
  '<p>La raya de una fracción quiere decir <strong>«dividido entre»</strong>. La fracción <span class="fracc" aria-hidden="true"><span class="fa">3</span><span class="fb2">4</span></span><span class="cap-oculto">3/4</span> quiere decir, exactamente, <strong>3 ÷ 4</strong>. Esa es la clave para convertir cualquier fracción en decimal.</p>')
# 2
R('<h2 id="s-fraction-to-decimal"><span aria-hidden="true" class="num-seccion">2</span>From fraction to decimal: divide</h2>', '<h2 id="s-fraccion-a-decimal"><span aria-hidden="true" class="num-seccion">2</span>De fracción a decimal: dividir</h2>')
R("<p>To change a fraction to a decimal, <strong>divide the numerator (top) by the denominator (bottom)</strong>. Use the division with decimals you learned in Lesson 3.2: if the numerator is smaller, write a point and zeros after it.</p>",
  "<p>Para convertir una fracción en decimal, <strong>divida el numerador (arriba) entre el denominador (abajo)</strong>. Use la división con decimales que aprendió en la Lección 3.2: si el numerador es menor, escriba un punto y ceros después.</p>")
R('<p class="titulo-ej">Example: change <span class="fracc"', '<p class="titulo-ej">Ejemplo: convierta <span class="fracc"')
R('<span class="cap-oculto">3/4</span> to a decimal</p>', '<span class="cap-oculto">3/4</span> en decimal</p>')
R("Set up the division: 3 ÷ 4. Since 3 is less than 4, write 3 as <strong>3.00</strong> and put the point in the answer.", "Plantee la división: 3 ÷ 4. Como 3 es menor que 4, escriba 3 como <strong>3.00</strong> y ponga el punto en el resultado.")
R("Divide: 30 ÷ 4 = 7, remainder 2. Bring down the next zero: 20 ÷ 4 = 5, with no remainder.", "Divida: 30 ÷ 4 = 7, residuo 2. Baje el cero siguiente: 20 ÷ 4 = 5, sin residuo.")
R("= <strong>0.75</strong>, just like 75 cents.", "= <strong>0.75</strong>, igual que 75 centavos.")
R('<p>Solve on paper first. Then clear the memory (<span class="tecla dos">2nd</span><span class="tecla">sto→</span> and <span class="tecla num">1</span>) and check in two ways:</p>', '<p>Resuelva primero en papel. Después borre la memoria (<span class="tecla dos">2nd</span><span class="tecla">sto→</span> y <span class="tecla num">1</span>) y compruebe de dos maneras:</p>')
R('<li><strong>As a division:</strong> type ', '<li><strong>Como división:</strong> escriba ')
R('. The screen shows <strong>0.75</strong>.</li>', '. La pantalla muestra <strong>0.75</strong>.</li>')
R('<li><strong>As a fraction:</strong> press <span class="tecla">n/d</span>, type <span class="tecla num">3</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">4</span>, leave with <span class="tecla">►</span>, and press <span class="tecla">enter</span>. The screen shows ',
  '<li><strong>Como fracción:</strong> pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">3</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">4</span>, salga con <span class="tecla">►</span> y pulse <span class="tecla">enter</span>. La pantalla muestra ')
R('. Now press <span class="tecla">⟷</span>: it changes to <strong>0.75</strong>.</li>', '. Ahora pulse <span class="tecla">⟷</span>: cambia a <strong>0.75</strong>.</li>')
R("<p>The calculator confirms; the paper teaches you.</p>", "<p>La calculadora confirma; el papel le enseña.</p>")
R("<h3>Practice 1 — Fraction to decimal</h3>", "<h3>Práctica 1 — De fracción a decimal</h3>")
R("Which decimal is equal to the fraction <span", "¿Qué decimal es igual a la fracción <span")
R('href="practice-3-3.html#fraction-to-decimal"', 'href="practica-3-3.html#fraccion-a-decimal"')
R('práctica: from fraction to decimal (se abre', 'práctica: de fracción a decimal (se abre')
R('<span class="ei-titulo">Practique más: from fraction to decimal</span><span class="ei-sub">Divide the numerator by the denominator and watch the decimal appear, step by step.</span>', '<span class="ei-titulo">Practique más: de fracción a decimal</span><span class="ei-sub">Divida el numerador entre el denominador y vea aparecer el decimal, paso a paso.</span>')
# 3
R('<h2 id="s-decimal-to-fraction"><span aria-hidden="true" class="num-seccion">3</span>From decimal to fraction: read and simplify</h2>', '<h2 id="s-decimal-a-fraccion"><span aria-hidden="true" class="num-seccion">3</span>De decimal a fracción: leer y simplificar</h2>')
R("<p>To change a decimal to a fraction, use what you learned in Lesson 3.1: <strong>the name of the last place gives you the denominator</strong>.</p>", "<p>Para convertir un decimal en fracción, use lo que aprendió en la Lección 3.1: <strong>el nombre del último lugar le da el denominador</strong>.</p>")
R("<li>If the decimal ends in the <strong>tenths</strong> → the denominator is <strong>10</strong>.</li>", "<li>Si el decimal termina en las <strong>décimas</strong> → el denominador es <strong>10</strong>.</li>")
R("<li>If it ends in the <strong>hundredths</strong> → the denominator is <strong>100</strong>.</li>", "<li>Si termina en las <strong>centésimas</strong> → el denominador es <strong>100</strong>.</li>")
R("<li>If it ends in the <strong>thousandths</strong> → the denominator is <strong>1,000</strong>.</li>", "<li>Si termina en las <strong>milésimas</strong> → el denominador es <strong>1,000</strong>.</li>")
R('<p class="titulo-ej">Example: change 0.6 to a fraction</p>', '<p class="titulo-ej">Ejemplo: convierta 0.6 en fracción</p>')
R('0.6 is "six tenths." The numerator is 6 and the denominator is 10: ', '0.6 es «seis décimas». El numerador es 6 y el denominador es 10: ')
R("Simplify: 6 and 10 can both be divided by 2. 6 ÷ 2 = 3, and 10 ÷ 2 = 5.", "Simplifique: 6 y 10 se pueden dividir los dos entre 2. 6 ÷ 2 = 3, y 10 ÷ 2 = 5.")
R("<p>A fraction is <strong>simplified</strong> when the numerator and the denominator cannot both be divided by the same number anymore. You will study simplifying in depth in Topic 4. For now, it is enough to simplify the easy ones.</p>",
  "<p>Una fracción está <strong>simplificada</strong> cuando el numerador y el denominador ya no se pueden dividir los dos entre el mismo número. Estudiará la simplificación a fondo en el Tema 4. Por ahora basta con simplificar las fáciles.</p>")
R('<p>The calculator can change a decimal to a fraction with the green function <strong>f◂▸d</strong> (above the <span class="tecla">table</span> key):</p>', '<p>La calculadora puede convertir un decimal en fracción con la función verde <strong>f◂▸d</strong> (encima de la tecla <span class="tecla">table</span>):</p>')
R('<li>Type <span class="tecla num">0</span><span class="tecla num">.</span><span class="tecla num">6</span>.</li>', '<li>Escriba <span class="tecla num">0</span><span class="tecla num">.</span><span class="tecla num">6</span>.</li>')
R('<li>Press <span class="tecla dos">2nd</span> and then <span class="tecla">table</span> (f◂▸d).</li>', '<li>Pulse <span class="tecla dos">2nd</span> y después <span class="tecla">table</span> (f◂▸d).</li>')
R('<li>Press <span class="tecla">enter</span>. The screen shows ', '<li>Pulse <span class="tecla">enter</span>. La pantalla muestra ')
R('<span class="cap-oculto">3/5</span>, already simplified.</li>', '<span class="cap-oculto">3/5</span>, ya simplificada.</li>')
R('href="practice-3-3.html#decimal-to-fraction"', 'href="practica-3-3.html#decimal-a-fraccion"')
R('práctica: from decimal to fraction (se abre', 'práctica: de decimal a fracción (se abre')
R('<span class="ei-titulo">Practique más: from decimal to fraction</span><span class="ei-sub">Read the last place, write the denominator, and simplify.</span>', '<span class="ei-titulo">Practique más: de decimal a fracción</span><span class="ei-sub">Lea el último lugar, escriba el denominador y simplifique.</span>')
# 4
R('<h2 id="s-memorize"><span aria-hidden="true" class="num-seccion">4</span>Pairs worth knowing by heart</h2>', '<h2 id="s-memoria"><span aria-hidden="true" class="num-seccion">4</span>Parejas que conviene saber de memoria</h2>')
R("<p>Some fraction–decimal pairs show up so often, in prices, recipes, and measurements, that it pays to <strong>know them by heart</strong>. Here is your reference table:</p>", "<p>Algunas parejas fracción–decimal aparecen tan a menudo, en precios, recetas y medidas, que vale la pena <strong>saberlas de memoria</strong>. Esta es su tabla de referencia:</p>")
R('aria-label="Common fraction and decimal pairs (tabla desplazable horizontalmente)"', 'aria-label="Parejas comunes de fracción y decimal (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Common fractions, their decimals, and where you see them</caption>', '<caption class="cap-oculto">Fracciones comunes, sus decimales y dónde se ven</caption>')
R('<th scope="col">Fraction</th><th scope="col">Decimal</th><th scope="col">Where you see it</th>', '<th scope="col">Fracción</th><th scope="col">Decimal</th><th scope="col">Dónde se ve</th>')
R("<td>half a dollar, half an hour</td>", "<td>medio dólar, media hora</td>")
R("<td>a quarter, 25 cents, a quarter of an hour</td>", "<td>una moneda de 25 centavos, un cuarto de hora</td>")
R("<td>three quarters, 75 cents</td>", "<td>tres cuartos, 75 centavos</td>")
R("<td>one fifth</td>", "<td>un quinto</td>")
R("<td>one tenth, a dime</td>", "<td>un décimo, una moneda de 10 centavos</td>")
R("<td>one third (a repeating decimal)</td>", "<td>un tercio (un decimal periódico)</td>")
R('<span class="etiqueta et-verde">A special case: 1/3</span>', '<span class="etiqueta et-verde">Un caso especial: 1/3</span>')
R("<p>When you divide 1 ÷ 3, the answer is 0.3333… and the 3s never end. This is a <strong>repeating decimal</strong>. In daily life we round it to 0.33. You will see repeating decimals in more detail in later levels.</p>",
  "<p>Cuando divide 1 ÷ 3, el resultado es 0.3333… y los 3 no se acaban nunca. Es un <strong>decimal periódico</strong>. En la vida diaria lo redondeamos a 0.33. Verá los decimales periódicos con más detalle en niveles más adelante.</p>")
R("<h3>Practice 2 — Decimal to fraction</h3>", "<h3>Práctica 2 — De decimal a fracción</h3>")
R("The decimal <strong>0.25</strong> is equal to which fraction?", "¿A qué fracción es igual el decimal <strong>0.25</strong>?")
R('href="practice-3-3.html#memorize"', 'href="practica-3-3.html#memoria"')
R('práctica: pairs worth knowing by heart (se abre', 'práctica: parejas que conviene saber de memoria (se abre')
R('<span class="ei-titulo">Practique más: pairs worth knowing by heart</span><span class="ei-sub">Practice with flash cards: the most common fractions and their decimals.</span>', '<span class="ei-titulo">Practique más: parejas que conviene saber de memoria</span><span class="ei-sub">Practique con tarjetas: las fracciones más comunes y sus decimales.</span>')
# 5
R('<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Decimals in real-life problems</h2>', '<h2 id="s-vida-real"><span aria-hidden="true" class="num-seccion">5</span>Los decimales en problemas de la vida real</h2>')
R("<p>Decimals are everywhere: shopping, distances, measurements, and change. Always use the 4-step method from Lesson 1.3: read and underline, choose the operation, solve, and check that the answer makes sense.</p>",
  "<p>Los decimales están en todas partes: compras, distancias, medidas y cambio. Use siempre el método de 4 pasos de la Lección 1.3: lea y subraye, elija la operación, resuelva y compruebe que el resultado tiene sentido.</p>")
R('<p class="titulo-ej">Example: a trip to the grocery store</p>', '<p class="titulo-ej">Ejemplo: una visita al supermercado</p>')
R('<p><em>"You buy bread for $2.50, milk for $3.75, and eggs for $4.20. If you pay with $20, how much change do you get?"</em></p>', '<p><em>«Compra pan por $2.50, leche por $3.75 y huevos por $4.20. Si paga con $20, ¿cuánto le dan de cambio?»</em></p>')
R("<strong>Underline:</strong> prices $2.50, $3.75, $4.20; you pay $20; the question asks for the change.", "<strong>Subraye:</strong> precios $2.50, $3.75, $4.20; paga con $20; la pregunta pide el cambio.")
R("<strong>Choose:</strong> first add the prices (put together), then subtract from what you paid (change). It takes two steps.", "<strong>Elija:</strong> primero sume los precios (juntar) y después réstelos de lo que pagó (cambio). Son dos pasos.")
R("<strong>Solve:</strong> 2.50 + 3.75 + 4.20 = 10.45. Then 20.00 − 10.45 = 9.55.", "<strong>Resuelva:</strong> 2.50 + 3.75 + 4.20 = 10.45. Después, 20.00 − 10.45 = 9.55.")
R("<strong>Does it make sense?</strong> The change ($9.55) is less than what you paid ($20). The answer is <strong>$9.55</strong>.", "<strong>¿Tiene sentido?</strong> El cambio ($9.55) es menos de lo que pagó ($20). La respuesta es <strong>$9.55</strong>.")
R("<p>Check each step: <span", "<p>Compruebe cada paso: <span")
R(" shows <strong>10.45</strong>. Then <span", " muestra <strong>10.45</strong>. Después <span")
R(" shows <strong>9.55</strong>.</p>", " muestra <strong>9.55</strong>.</p>")
R('<p>Tip: right after the first answer, you can press <span class="tecla">−</span> and the calculator writes <strong>ans</strong> (the last answer). For the change, though, you need 20 − 10.45, so type the whole subtraction.</p>',
  '<p>Consejo: justo después del primer resultado, puede pulsar <span class="tecla">−</span> y la calculadora escribe <strong>ans</strong> (el último resultado). Pero para el cambio necesita 20 − 10.45, así que escriba la resta completa.</p>')
R("<h3>Practice 3 — A problem in context</h3>", "<h3>Práctica 3 — Un problema en contexto</h3>")
R("A person walks <strong>1.8 miles</strong> in the morning and <strong>2.35 miles</strong> in the afternoon. How many miles did the person walk in all?", "Una persona camina <strong>1.8 millas</strong> en la mañana y <strong>2.35 millas</strong> en la tarde. ¿Cuántas millas caminó en total?")
for n in ["3.53", "4.15", "4.05", "2.53"]:
    R('type="button">' + n + ' miles</button>', 'type="button">' + n + ' millas</button>')
R("<h3>Practice 4 — A problem in context</h3>", "<h3>Práctica 4 — Un problema en contexto</h3>")
R("A gallon of gas costs <strong>$3.40</strong>. How much do <strong>6 gallons</strong> cost?", "Un galón de gasolina cuesta <strong>$3.40</strong>. ¿Cuánto cuestan <strong>6 galones</strong>?")
R('href="practice-3-3.html#real-life"', 'href="practica-3-3.html#vida-real"')
R('práctica: decimals in real life (se abre', 'práctica: los decimales en la vida real (se abre')
R('<span class="ei-titulo">Practique más: decimals in real life</span><span class="ei-sub">Solve shopping, change, and measurement problems with the 4 steps.</span>', '<span class="ei-titulo">Practique más: los decimales en la vida real</span><span class="ei-sub">Resuelva problemas de compras, cambio y medidas con los 4 pasos.</span>')
# Tarea
R("<p>This is independent practice. Plan for about one hour, with your notebook open. With it, you finish Topic 3.</p>", "<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto. Con ella termina el Tema 3.</p>")
R('<li><strong>The practice page.</strong> Open the <a href="practice-3-3.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-3-3.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Write the table of pairs from memory (1/2, 1/4, 3/4, 1/5, 1/10, 1/3). Then check each one by dividing, on paper and with the calculator. Do it again the next day without looking.</li>",
  "<li><strong>Papel y lápiz.</strong> Escriba de memoria la tabla de parejas (1/2, 1/4, 3/4, 1/5, 1/10, 1/3). Después compruebe cada una dividiendo, en papel y con la calculadora. Repítalo al día siguiente sin mirar.</li>")
R("<li><strong>In your daily life.</strong> Find a real price in an online store and write it as a fraction of a dollar. Then look at a recipe: write the measures that come as fractions (1/2 cup, 3/4 tablespoon) as decimals.</li>",
  "<li><strong>En su vida diaria.</strong> Busque un precio real en una tienda en línea y escríbalo como fracción de dólar. Después mire una receta: escriba como decimales las medidas que vienen en fracciones (1/2 taza, 3/4 de cucharada).</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. Work on paper.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>. Trabaje en papel.")
R("The bar in a fraction means:", "La raya de una fracción quiere decir:")
R('type="button">"times"</button><button class="opcion" data-k="b" type="button">"plus"</button><button class="opcion" data-k="c" type="button">"divided by"</button><button class="opcion" data-k="d" type="button">"minus"</button>',
  'type="button">«por»</button><button class="opcion" data-k="b" type="button">«más»</button><button class="opcion" data-k="c" type="button">«dividido entre»</button><button class="opcion" data-k="d" type="button">«menos»</button>')
R("Which decimal is equal to <span", "¿Qué decimal es igual a <span", 2)
R("The decimal <strong>0.7</strong> is equal to which fraction?", "¿A qué fracción es igual el decimal <strong>0.7</strong>?")
R("When you divide 1 ÷ 3, the answer 0.333… is called a ___ decimal.", "Cuando divide 1 ÷ 3, el resultado 0.333… se llama decimal ___.")
R('type="button">terminating (exact)</button><button class="opcion" data-k="b" type="button">whole</button><button class="opcion" data-k="c" type="button">repeating</button><button class="opcion" data-k="d" type="button">negative</button>',
  'type="button">exacto (finito)</button><button class="opcion" data-k="b" type="button">entero</button><button class="opcion" data-k="c" type="button">periódico</button><button class="opcion" data-k="d" type="button">negativo</button>')
R("A bag has 2.6 pounds of flour. You use 0.85 pounds for a recipe. How many pounds of flour are left?", "Una bolsa tiene 2.6 libras de harina. Usa 0.85 libras para una receta. ¿Cuántas libras de harina quedan?")
R("A pound of rice costs $1.25. How much do 4 pounds cost?", "Una libra de arroz cuesta $1.25. ¿Cuánto cuestan 4 libras?")
R("You buy items for $6.80 and $5.45, and you pay with $15. How much change do you get?", "Compra artículos de $6.80 y $5.45, y paga con $15. ¿Cuánto le dan de cambio?")
# Lista
R('aria-label="Self-check checklist for fractions, decimals, and problems (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de fracciones, decimales y problemas (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: changing between fractions and decimals and solving problems, ', '<caption class="cap-oculto">Lista de autoevaluación: convertir entre fracciones y decimales y resolver problemas, ')
R('<tr><th scope="row">Change a fraction to a decimal</th><td>I divide the numerator by the denominator with no mistakes.</td><td>I set up the division, but sometimes I make a mistake dividing.</td><td>I do not connect the fraction with a division.</td></tr>',
  '<tr><th scope="row">Convertir una fracción en decimal</th><td>Divido el numerador entre el denominador sin errores.</td><td>Planteo la división, pero a veces me equivoco al dividir.</td><td>No relaciono la fracción con una división.</td></tr>')
R('<tr><th scope="row">Change a decimal to a fraction</th><td>I find the denominator from the last place, and I simplify.</td><td>I write the right fraction, but I do not simplify it.</td><td>I mix up the denominators (10, 100, 1,000).</td></tr>',
  '<tr><th scope="row">Convertir un decimal en fracción</th><td>Hallo el denominador por el último lugar y simplifico.</td><td>Escribo la fracción correcta, pero no la simplifico.</td><td>Confundo los denominadores (10, 100, 1,000).</td></tr>')
R('<tr><th scope="row">Know the common pairs</th><td>I know 1/2, 1/4, 3/4, 1/5, and 1/10 by heart.</td><td>I know most of the pairs.</td><td>I know only 1/2 and 1/4, or none.</td></tr>',
  '<tr><th scope="row">Saber las parejas comunes</th><td>Sé de memoria 1/2, 1/4, 3/4, 1/5 y 1/10.</td><td>Sé la mayoría de las parejas.</td><td>Sé solo 1/2 y 1/4, o ninguna.</td></tr>')
R('<tr><th scope="row">Solve problems in context</th><td>I solve with the right answer, the unit, and a check.</td><td>I solve correctly and write the unit.</td><td>I set up the problem but make calculation mistakes, or I do not understand it.</td></tr>',
  '<tr><th scope="row">Resolver problemas en contexto</th><td>Resuelvo con el resultado correcto, la unidad y una comprobación.</td><td>Resuelvo bien y escribo la unidad.</td><td>Planteo el problema, pero me equivoco al calcular, o no lo entiendo.</td></tr>')
# Cierre
R("<p>With this lesson you finish <strong>Topic 3 · Decimals</strong>. You can now read, compare, round, and calculate with decimals, change them to fractions, and solve real problems with them.</p>",
  "<p>Con esta lección termina el <strong>Tema 3 · Decimales</strong>. Ya sabe leer, comparar, redondear y calcular con decimales, convertirlos en fracciones y resolver problemas reales con ellos.</p>")
R("<p>In <strong>Topic 4 · Fractions</strong> you will study the other way to write parts of a whole. <strong>Lesson 4.1 · Equivalent fractions: simplify and compare</strong> will show you how the same amount can be written with many different fractions, and how to find the simplest one. You already got a first look at that idea of \"simplifying\" in this lesson.</p>",
  "<p>En el <strong>Tema 4 · Fracciones</strong> estudiará la otra forma de escribir partes de un entero. La <strong>Lección 4.1 · Fracciones equivalentes: simplificar y comparar</strong> le mostrará cómo la misma cantidad se puede escribir con muchas fracciones distintas, y cómo hallar la más sencilla. En esta lección ya vio por primera vez esa idea de «simplificar».</p>")
R('Next: <a href="lesson-4-1.html">Topic 4 · Lesson 4.1 · Equivalent fractions: simplify and compare</a>', 'Siguiente: Tema 4 · <a href="leccion-4-1.html">Lección 4.1 · Fracciones equivalentes: simplificar y comparar</a>')
R("""<dt>numerator, denominator</dt><dd>The top and the bottom numbers of a fraction. In 3/4, the numerator is 3 and the denominator is 4.</dd>
<dt>equivalent</dt><dd>Equal in value, even if written in a different way. 1/2 and 0.5 are equivalent.</dd>
<dt>simplify a fraction</dt><dd>To divide the numerator and the denominator by the same number until you cannot do it anymore. 6/10 simplifies to 3/5.</dd>
<dt>terminating decimal</dt><dd>A decimal that ends, like 0.75.</dd>
<dt>repeating decimal</dt><dd>A decimal with digits that repeat forever, like 0.333… (1/3).</dd>
<dt>change (money)</dt><dd>The money you get back when you pay more than the price.</dd>""",
"""<dt>numerador, denominador</dt><dd>El número de arriba y el de abajo de una fracción. En 3/4, el numerador es 3 y el denominador es 4.</dd>
<dt>equivalente</dt><dd>Igual en valor, aunque se escriba de otra forma. 1/2 y 0.5 son equivalentes.</dd>
<dt>simplificar una fracción</dt><dd>Dividir el numerador y el denominador entre el mismo número hasta que ya no se pueda. 6/10 se simplifica a 3/5.</dd>
<dt>decimal exacto</dt><dd>Un decimal que se termina, como 0.75.</dd>
<dt>decimal periódico</dt><dd>Un decimal con dígitos que se repiten sin fin, como 0.333… (1/3).</dd>
<dt>cambio (dinero)</dt><dd>El dinero que le devuelven cuando paga más que el precio.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 3 · Lesson 3.3</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 3 · Lección 3.3</p>")
t.js('''{
 next: "Lección 4.1",
 review: "las secciones 2, 3, 4 y 5",
 practice: {
  p1: { ok: "b",
   hints: { a: "0.5 es un medio. Divida 1 ÷ 5: el resultado es menos de un medio.", c: "La fracción no se lee juntando los dígitos. Divida 1 ÷ 5.", d: "1.5 es más que 1, pero 1/5 es menos que 1. Divida 1 ÷ 5." },
   right: "1 ÷ 5 = 0.2. Comprobación: 0.2 × 5 = 1 ✓",
   solution: "La raya quiere decir dividido entre: 1 ÷ 5. Como 1 es menor que 5, escriba 1.0: 10 ÷ 5 = 2. Así que 1/5 = 0.2." },
  p2: { ok: "b",
   hints: { a: "1/2 es 0.5 (cincuenta centésimas), no 0.25.", c: "2/5 es 0.4. Lea 0.25 como veinticinco centésimas: 25/100.", d: "3/4 es 0.75. Lea 0.25 como veinticinco centésimas: 25/100." },
   right: "0.25 = 25/100, y 25/100 se simplifica a 1/4 (divida los dos entre 25).",
   solution: "0.25 son veinticinco centésimas: 25/100. Divida el numerador y el denominador entre 25: 1/4. Es como 25 centavos: un cuarto de dólar." },
  p3: { ok: "b",
   hints: { a: "Alinee los puntos: 1.80 + 2.35.", c: "Revise las décimas: 8 + 3 = 11, así que lleva 1 a las unidades.", d: "Eso se parece a una resta. La pregunta pide el total: sume." },
   right: "1.80 + 2.35 = 4.15 millas.",
   solution: "Total quiere decir sumar. Escriba 1.8 como 1.80 y alinee los puntos: 1.80 + 2.35 = 4.15. La persona caminó 4.15 millas." },
  p4: { ok: "b",
   hints: { a: "6 galones de $3.40 cada uno son grupos iguales: multiplique; no sume.", c: "Compruebe: 6 × 3 = 18 y 6 × 0.40 = 2.40.", d: "Cuente los lugares decimales: 3.40 tiene 2, así que 6 × 340 = 2040 se vuelve 20.40." },
   right: "3.40 × 6 = 20.40. Estimación: más o menos 3 × 6 = 18 ✓",
   solution: "6 grupos iguales de $3.40: se multiplica. 340 × 6 = 2,040. Con 2 lugares decimales: $20.40. Estimación: más o menos $3 × 6 = $18, cerca ✓" }
 },
 quiz: {
  A: { ok: "c", hints: { a: "Piense en 3/4 como repartir 3 entre 4.", b: "La raya no es una suma.", d: "La raya no es una resta." },
   solution: "La raya de la fracción quiere decir «dividido entre». 3/4 quiere decir 3 ÷ 4." },
  B: { ok: "a", hints: { b: "La fracción no se lee juntando los dígitos. Divida 3 ÷ 4.", c: "0.5 es 1/2. 3/4 es más que un medio.", d: "Divida 3 ÷ 4: 30 ÷ 4 = 7, residuo 2, y después 20 ÷ 4 = 5." },
   solution: "3 ÷ 4: escriba 3.00. 30 ÷ 4 = 7, residuo 2; 20 ÷ 4 = 5. Así que 3/4 = 0.75, como 75 centavos." },
  C: { ok: "b", hints: { a: "La fracción no se lee juntando los dígitos. Divida 1 ÷ 2.", c: "0.25 es 1/4. Un medio es más.", d: "1.2 es más que 1, pero 1/2 es menos que 1." },
   solution: "1 ÷ 2 = 0.5. Medio dólar es $0.50." },
  D: { ok: "d", hints: { a: "7/100 es 0.07. El 7 de 0.7 está en las décimas.", b: "1/7 es más o menos 0.14.", c: "7/1000 es 0.007, con tres lugares decimales." },
   solution: "0.7 son siete décimas. El último lugar es el de las décimas, así que el denominador es 10: 7/10." },
  E: { ok: "c", hints: { a: "Un decimal exacto se termina. 0.333… no se termina nunca.", b: "0.333… no es un número entero.", d: "0.333… es más que 0, así que no es negativo." },
   solution: "Los 3 se repiten y no se acaban nunca, así que 0.333… es un decimal periódico. En la vida diaria lo redondeamos: 1/3 ≈ 0.33." },
  F: { ok: "b", hints: { a: "Escriba 2.6 como 2.60 y reste: 2.60 − 0.85.", c: "Usó parte de la harina, así que queda menos: reste.", d: "Revise lo que pidió prestado: 2.60 − 0.85." },
   solution: "Usar quiere decir restar. 2.60 − 0.85 = 1.75. Quedan 1.75 libras de harina." },
  G: { ok: "d", hints: { a: "4 libras de $1.25 cada una son grupos iguales: multiplique; no sume.", b: "Compruebe: 4 × 1 = 4 y 4 × 0.25 = 1.", c: "No se olvide de los 25 centavos: 4 × 0.25 = 1." },
   solution: "1.25 × 4 = 5.00. Atajo: 4 × $1 = $4 y 4 × 25 centavos = $1, así que $5.00." },
  H: { ok: "a", hints: { b: "Revise primero el total: 6.80 + 5.45 = 12.25.", c: "Revise las centésimas: 15.00 − 12.25.", d: "Eso es el total que gastó. La pregunta pide el cambio." },
   solution: "Dos pasos. Primero el total: 6.80 + 5.45 = 12.25. Después el cambio: 15.00 − 12.25 = 2.75. Le dan $2.75 de cambio." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-3-3.html")
