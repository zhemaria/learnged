"""Crea es/matematicas/nivel-1/leccion-4-3.html a partir de math/level-1/lesson-4-3.html."""
from traduce import Traductor, F
t = Traductor("math/level-1/lesson-4-3.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 4.3 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 4.3 · Multiplying and dividing fractions · LearnGED</title>", "<title>Lección 4.3 · Multiplicación y división de fracciones · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 4 — Fractions</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 4 — Fracciones</p>')
R("<h1>Lesson 4.3 · Multiplying and dividing fractions</h1>", "<h1>Lección 4.3 · Multiplicación y división de fracciones</h1>")
R('<p class="lema">The good news: multiplying and dividing fractions is simpler than adding them. With this lesson, you complete the four operations with fractions.</p>', '<p class="lema">La buena noticia: multiplicar y dividir fracciones es más sencillo que sumarlas. Con esta lección completa las cuatro operaciones con fracciones.</p>')
R("Multiply and divide</span>", "Multiplicar y dividir</span>")
R("<li><strong>Multiply</strong> fractions: numerator times numerator and denominator times denominator.</li>", "<li><strong>Multiplicar</strong> fracciones: numerador por numerador y denominador por denominador.</li>")
R("<li><strong>Find</strong> the reciprocal of a fraction (the fraction flipped upside down).</li>", "<li><strong>Hallar</strong> el recíproco de una fracción (la fracción volteada).</li>")
R("<li><strong>Divide</strong> fractions by multiplying by the reciprocal of the second one.</li>", "<li><strong>Dividir</strong> fracciones multiplicando por el recíproco de la segunda.</li>")
R("<li><strong>Solve</strong> real-life problems with fractions, and simplify the answer.</li>", "<li><strong>Resolver</strong> problemas de la vida real con fracciones, y simplificar el resultado.</li>")
R('<li><a href="#s-surprise">A pleasant surprise</a></li>', '<li><a href="#s-sorpresa">Una sorpresa agradable</a></li>')
R('<li><a href="#s-multiply">Multiply fractions: straight across</a></li>', '<li><a href="#s-multiplicar">Multiplicar fracciones: en línea recta</a></li>')
R('<li><a href="#s-reciprocal">The reciprocal: the flipped fraction</a></li>', '<li><a href="#s-reciproco">El recíproco: la fracción volteada</a></li>')
R('<li><a href="#s-divide">Divide fractions: keep, change, flip</a></li>', '<li><a href="#s-dividir">Dividir fracciones: dejar, cambiar, voltear</a></li>')
R('<li><a href="#s-real-life">Fractions in real-life problems</a></li>', '<li><a href="#s-vida-real">Las fracciones en problemas de la vida real</a></li>')
t.todas('<p class="titulo-ej">Example: ', '<p class="titulo-ej">Ejemplo: ')
# 1
R('<h2 id="s-surprise"><span aria-hidden="true" class="num-seccion">1</span>A pleasant surprise</h2>', '<h2 id="s-sorpresa"><span aria-hidden="true" class="num-seccion">1</span>Una sorpresa agradable</h2>')
R("<p>In Lesson 4.2, adding and subtracting fractions took some work: you had to find a common denominator first. Today there is good news.</p>", "<p>En la Lección 4.2, sumar y restar fracciones costó trabajo: primero había que hallar un denominador común. Hoy hay buenas noticias.</p>")
R("<p><strong>Multiplying and dividing fractions is easier than adding them.</strong> You do <strong>not</strong> need a common denominator. The rules are short and direct. You only need to learn them well and use them carefully.</p>", "<p><strong>Multiplicar y dividir fracciones es más fácil que sumarlas.</strong> <strong>No</strong> necesita un denominador común. Las reglas son cortas y directas. Solo tiene que aprenderlas bien y usarlas con cuidado.</p>")
R('<span class="etiqueta et-verde">The key idea</span>', '<span class="etiqueta et-verde">La idea clave</span>')
R(f'<p>Multiplying a fraction by a fraction answers the question "<strong>how much is a part of a part?</strong>" For example, half of half a pizza is a quarter of the pizza: {F(1,2)} of {F(1,2)} = {F(1,4)}. The word <strong>"of"</strong> almost always means <strong>multiply</strong>.</p>',
  f'<p>Multiplicar una fracción por otra responde la pregunta «<strong>¿cuánto es una parte de una parte?</strong>». Por ejemplo, la mitad de media pizza es un cuarto de la pizza: {F(1,2)} de {F(1,2)} = {F(1,4)}. La palabra <strong>«de»</strong> casi siempre quiere decir <strong>multiplicar</strong>.</p>')
R('aria-label="A square cut in half from top to bottom and in half from side to side. The half on the left is light purple, the top half is light blue, and the part where they overlap, one of the four parts, is dark purple: one fourth."', 'aria-label="Un cuadrado cortado por la mitad de arriba abajo y por la mitad de lado a lado. La mitad de la izquierda es morado claro, la mitad de arriba es azul claro, y la parte donde se cruzan, una de las cuatro partes, es morado oscuro: un cuarto."')
R(f"Half (purple) of a half (blue): the dark part is <strong>1 of 4</strong> equal parts, {F(1,4)} of the whole.", f"La mitad (morado) de una mitad (azul): la parte oscura es <strong>1 de 4</strong> partes iguales, {F(1,4)} del entero.")
# 2
R('<h2 id="s-multiply"><span aria-hidden="true" class="num-seccion">2</span>Multiply fractions: straight across</h2>', '<h2 id="s-multiplicar"><span aria-hidden="true" class="num-seccion">2</span>Multiplicar fracciones: en línea recta</h2>')
R("<p>Multiplying fractions is the most direct operation of all.</p>", "<p>Multiplicar fracciones es la operación más directa de todas.</p>")
R('<span class="etiqueta et-verde">To multiply fractions</span>', '<span class="etiqueta et-verde">Para multiplicar fracciones</span>')
R("<p><strong>Numerator × numerator</strong> on top, and <strong>denominator × denominator</strong> on the bottom. Then simplify if you can.</p>", "<p><strong>Numerador × numerador</strong> arriba, y <strong>denominador × denominador</strong> abajo. Después simplifique si puede.</p>")
R("Multiply the numerators: 2 × 4 = 8.", "Multiplique los numeradores: 2 × 4 = 8.")
R("Multiply the denominators: 3 × 5 = 15.", "Multiplique los denominadores: 3 × 5 = 15.")
R("Check if you can simplify: 8 and 15 share no factor greater than 1. It is already in simplest form.", "Revise si puede simplificar: 8 y 15 no tienen ningún factor común mayor que 1. Ya está en su forma más simple.")
R('aria-label="A square cut into 3 columns and 5 rows, 15 small parts in all. 2 columns are light purple (two thirds) and 4 rows are light blue (four fifths). The 8 small parts where they overlap are dark purple: eight fifteenths."', 'aria-label="Un cuadrado cortado en 3 columnas y 5 filas, 15 partes pequeñas en total. 2 columnas son morado claro (dos tercios) y 4 filas son azul claro (cuatro quintos). Las 8 partes pequeñas donde se cruzan son morado oscuro: ocho quinceavos."')
R(f"2 of the 3 columns and 4 of the 5 rows: they overlap in <strong>8</strong> of the <strong>15</strong> small parts, {F(8,15)}.", f"2 de las 3 columnas y 4 de las 5 filas: se cruzan en <strong>8</strong> de las <strong>15</strong> partes pequeñas, {F(8,15)}.")
R("<p>When you multiply fractions, you do <strong>not</strong> look for a common denominator. That was for adding and subtracting. Here you multiply straight across. And always check at the end if the answer can be simplified.</p>", "<p>Al multiplicar fracciones, <strong>no</strong> se busca un denominador común. Eso era para sumar y restar. Aquí se multiplica en línea recta. Y revise siempre al final si el resultado se puede simplificar.</p>")
R(f"<p>To check {F(2,3)} × {F(4,5)}:</p>", f"<p>Para comprobar {F(2,3)} × {F(4,5)}:</p>")
R('<li>Press <span class="tecla">n/d</span>, type <span class="tecla num">2</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">3</span>, and leave with <span class="tecla">►</span>.</li>', '<li>Pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">2</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">3</span> y salga con <span class="tecla">►</span>.</li>')
R('<li>Press <span class="tecla">×</span>.</li>', '<li>Pulse <span class="tecla">×</span>.</li>')
R('<li>Press <span class="tecla">n/d</span>, type <span class="tecla num">4</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">5</span>, and leave with <span class="tecla">►</span>.</li>', '<li>Pulse <span class="tecla">n/d</span>, escriba <span class="tecla num">4</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">5</span> y salga con <span class="tecla">►</span>.</li>')
R('<li>Press <span class="tecla">enter</span>. The screen shows ', '<li>Pulse <span class="tecla">enter</span>. La pantalla muestra ')
R("<h3>Practice 1 — Multiply fractions</h3>", "<h3>Práctica 1 — Multiplicar fracciones</h3>")
R(f"What is {F(1,2)} × {F(3,4)}?", f"¿Cuánto es {F(1,2)} × {F(3,4)}?")
R("<h3>Practice 2 — The word “of”</h3>", "<h3>Práctica 2 — La palabra «de»</h3>")
R(f"What is {F(1,3)} of {F(1,2)}?", f"¿Cuánto es {F(1,3)} de {F(1,2)}?")
R('href="practice-4-3.html#multiply"', 'href="practica-4-3.html#multiplicar"')
R('práctica: multiply fractions (se abre', 'práctica: multiplicar fracciones (se abre')
R('<span class="ei-titulo">Practique más: multiply fractions</span><span class="ei-sub">Multiply straight across, numerator by numerator and denominator by denominator, and see the area model.</span>', '<span class="ei-titulo">Practique más: multiplicar fracciones</span><span class="ei-sub">Multiplique en línea recta, numerador por numerador y denominador por denominador, y vea el modelo de área.</span>')
# 3
R('<h2 id="s-reciprocal"><span aria-hidden="true" class="num-seccion">3</span>The reciprocal: the flipped fraction</h2>', '<h2 id="s-reciproco"><span aria-hidden="true" class="num-seccion">3</span>El recíproco: la fracción volteada</h2>')
R("<p>Before you divide fractions, you need one simple idea: the <strong>reciprocal</strong>.</p>", "<p>Antes de dividir fracciones, necesita una idea sencilla: el <strong>recíproco</strong>.</p>")
R("<p>The <strong>reciprocal</strong> of a fraction is the same fraction <strong>flipped upside down</strong>: the numerator goes to the bottom, and the denominator goes to the top.</p>", "<p>El <strong>recíproco</strong> de una fracción es la misma fracción <strong>volteada</strong>: el numerador pasa abajo, y el denominador pasa arriba.</p>")
R(f"The reciprocal of {F(3,4)} is {F(4,3)}.</p>", f"El recíproco de {F(3,4)} es {F(4,3)}.</p>")
R('<p class="titulo-ej">Examples of reciprocals</p>', '<p class="titulo-ej">Ejemplos de recíprocos</p>')
R(f"The reciprocal of {F(2,5)} is {F(5,2)}.", f"El recíproco de {F(2,5)} es {F(5,2)}.")
R(f"The reciprocal of {F(1,8)} is {F(8,1)}, which is the same as 8.", f"El recíproco de {F(1,8)} es {F(8,1)}, que es lo mismo que 8.")
R(f"The reciprocal of a whole number like 4 is {F(1,4)}. Every whole number is itself over 1: 4 = {F(4,1)}.", f"El recíproco de un número entero como 4 es {F(1,4)}. Todo número entero es él mismo sobre 1: 4 = {F(4,1)}.")
R('<span class="etiqueta et-verde">A way to check</span>', '<span class="etiqueta et-verde">Una forma de comprobar</span>')
R(f"<p>A number times its reciprocal always equals 1. For example, {F(3,4)} × {F(4,3)} = {F(12,12)} = 1.</p>", f"<p>Un número por su recíproco siempre da 1. Por ejemplo, {F(3,4)} × {F(4,3)} = {F(12,12)} = 1.</p>")
R("<h3>Practice 3 — The reciprocal</h3>", "<h3>Práctica 3 — El recíproco</h3>")
R(f"What is the reciprocal of {F(5,7)}?", f"¿Cuál es el recíproco de {F(5,7)}?")
R('href="practice-4-3.html#reciprocal"', 'href="practica-4-3.html#reciproco"')
R('práctica: the reciprocal (se abre', 'práctica: el recíproco (se abre')
R('<span class="ei-titulo">Practique más: the reciprocal</span><span class="ei-sub">Flip the fraction, and practice with whole numbers and with fractions that have 1 on top.</span>', '<span class="ei-titulo">Practique más: el recíproco</span><span class="ei-sub">Voltee la fracción, y practique con números enteros y con fracciones que tienen 1 arriba.</span>')
# 4
R('<h2 id="s-divide"><span aria-hidden="true" class="num-seccion">4</span>Divide fractions: keep, change, flip</h2>', '<h2 id="s-dividir"><span aria-hidden="true" class="num-seccion">4</span>Dividir fracciones: dejar, cambiar, voltear</h2>')
R("<p>Here is the most useful trick in Topic 4. To divide fractions, you do not really divide: you change the division into a <strong>multiplication</strong>.</p>", "<p>Este es el truco más útil del Tema 4. Para dividir fracciones, en realidad no se divide: se convierte la división en una <strong>multiplicación</strong>.</p>")
R('<span class="etiqueta et-verde">To divide fractions: keep, change, flip</span>', '<span class="etiqueta et-verde">Para dividir fracciones: dejar, cambiar, voltear</span>')
R("<p><strong>Keep</strong> the first fraction as it is · <strong>change</strong> ÷ to × · <strong>flip</strong> the second fraction (use its reciprocal). Then multiply.</p>", "<p><strong>Deje</strong> la primera fracción como está · <strong>cambie</strong> ÷ por × · <strong>voltee</strong> la segunda fracción (use su recíproco). Después multiplique.</p>")
R(f"<strong>Keep.</strong> The first fraction stays the same: {F(3,4)}.", f"<strong>Dejar.</strong> La primera fracción se queda igual: {F(3,4)}.")
R("<strong>Change.</strong> The ÷ becomes ×.", "<strong>Cambiar.</strong> El ÷ se vuelve ×.")
R(f"<strong>Flip.</strong> {F(1,2)} becomes its reciprocal, {F(2,1)}.", f"<strong>Voltear.</strong> {F(1,2)} se vuelve su recíproco, {F(2,1)}.")
R("<strong>Multiply.</strong> ", "<strong>Multiplicar.</strong> ")
R("<strong>Simplify.</strong> Divide the top and the bottom by 2: ", "<strong>Simplificar.</strong> Divida el numerador y el denominador entre 2: ")
R(f" = {F(3,2)}, or 1&nbsp;{F(1,2)}.</p>", f" = {F(3,2)}, o 1&nbsp;{F(1,2)}.</p>")
R(f'<p><strong>Does it make sense?</strong> Dividing by {F(1,2)} asks "how many halves fit in {F(3,4)}?" One half fits, and then half of another half: one and a half. That is why dividing by a fraction less than 1 gives a <strong>bigger</strong> answer.</p>',
  f'<p><strong>¿Tiene sentido?</strong> Dividir entre {F(1,2)} pregunta «¿cuántos medios caben en {F(3,4)}?». Cabe un medio, y después la mitad de otro medio: uno y medio. Por eso dividir entre una fracción menor que 1 da un resultado <strong>mayor</strong>.</p>')
R("<p>Flip <strong>only the second fraction</strong>, the one after the ÷ sign. The first one stays exactly the same. And never forget to change the ÷ to ×.</p>", "<p>Voltee <strong>solo la segunda fracción</strong>, la que va después del signo ÷. La primera se queda exactamente igual. Y no se olvide nunca de cambiar el ÷ por ×.</p>")
R(f'<p>The calculator divides fractions too. For {F(3,4)} ÷ {F(1,2)}, write {F(3,4)} with <span class="tecla">n/d</span>, press <span class="tecla">÷</span>, write {F(1,2)}, and press <span class="tecla">enter</span>. The screen shows {F(3,2)}.</p>',
  f'<p>La calculadora también divide fracciones. Para {F(3,4)} ÷ {F(1,2)}, escriba {F(3,4)} con <span class="tecla">n/d</span>, pulse <span class="tecla">÷</span>, escriba {F(1,2)} y pulse <span class="tecla">enter</span>. La pantalla muestra {F(3,2)}.</p>')
R("<h3>Practice 4 — Divide fractions</h3>", "<h3>Práctica 4 — Dividir fracciones</h3>")
R(f"What is {F(1,2)} ÷ {F(1,4)}?", f"¿Cuánto es {F(1,2)} ÷ {F(1,4)}?")
R('href="practice-4-3.html#divide"', 'href="practica-4-3.html#dividir"')
R('práctica: divide fractions (se abre', 'práctica: dividir fracciones (se abre')
R('<span class="ei-titulo">Practique más: divide fractions</span><span class="ei-sub">Keep the first fraction, change to multiplication, and flip the second, step by step.</span>', '<span class="ei-titulo">Practique más: dividir fracciones</span><span class="ei-sub">Deje la primera fracción, cambie a multiplicación y voltee la segunda, paso a paso.</span>')
# 5
R('<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Fractions in real-life problems</h2>', '<h2 id="s-vida-real"><span aria-hidden="true" class="num-seccion">5</span>Las fracciones en problemas de la vida real</h2>')
R('<p>Always use the 4-step method from Lesson 1.3. Remember the key clue: the word <strong>"of"</strong> usually means <strong>multiply</strong>. Cutting or sharing something into pieces of a fractional size ("how many pieces of …?", "how many servings of …?") usually means <strong>divide</strong>.</p>',
  '<p>Use siempre el método de 4 pasos de la Lección 1.3. Recuerde la pista clave: la palabra <strong>«de»</strong> casi siempre quiere decir <strong>multiplicar</strong>. Cortar o repartir algo en pedazos de un tamaño fraccionario («¿cuántos pedazos de …?», «¿cuántas porciones de …?») casi siempre quiere decir <strong>dividir</strong>.</p>')
R(f'<p class="titulo-ej">📋 "A recipe calls for {F(3,4)} cup of sugar. You are making only half of the recipe. How much sugar do you need?"</p>', f'<p class="titulo-ej">📋 «Una receta pide {F(3,4)} de taza de azúcar. Usted va a hacer solo la mitad de la receta. ¿Cuánta azúcar necesita?»</p>')
R(f"<strong>Read and underline.</strong> {F(3,4)} cup of sugar; you want half ({F(1,2)}) of the recipe.", f"<strong>Lea y subraye.</strong> {F(3,4)} de taza de azúcar; quiere la mitad ({F(1,2)}) de la receta.")
R(f'<strong>Choose the operation.</strong> "Half of {F(3,4)}": the word "of" means multiply. It is {F(1,2)} × {F(3,4)}.', f'<strong>Elija la operación.</strong> «La mitad de {F(3,4)}»: la palabra «de» quiere decir multiplicar. Es {F(1,2)} × {F(3,4)}.')
R("<strong>Solve.</strong> ", "<strong>Resuelva.</strong> ")
R(f"<strong>Does it make sense?</strong> {F(3,8)} cup is less than {F(3,4)} cup. That makes sense, because you are making half the recipe. You need {F(3,8)} cup of sugar.", f"<strong>¿Tiene sentido?</strong> {F(3,8)} de taza es menos que {F(3,4)} de taza. Tiene sentido, porque hace la mitad de la receta. Necesita {F(3,8)} de taza de azúcar.")
R("<h3>Practice 5 — A word problem</h3>", "<h3>Práctica 5 — Un problema verbal</h3>")
R(f"A board 6 feet long is cut into pieces that are {F(1,2)} foot each. How many pieces do you get? (6 ÷ {F(1,2)})", f"Una tabla de 6 pies de largo se corta en pedazos de {F(1,2)} pie cada uno. ¿Cuántos pedazos salen? (6 ÷ {F(1,2)})")
for n in ["3", "12", "6"]:
    R('type="button">' + n + ' pieces</button>', 'type="button">' + n + ' pedazos</button>')
R("</span> of a piece</button>", "</span> de pedazo</button>")
R('href="practice-4-3.html#real-life"', 'href="practica-4-3.html#vida-real"')
R('práctica: fractions in real life (se abre', 'práctica: las fracciones en la vida real (se abre')
R('<span class="ei-titulo">Practique más: fractions in real life</span><span class="ei-sub">Decide if the problem asks you to multiply or to divide, and solve it.</span>', '<span class="ei-titulo">Practique más: las fracciones en la vida real</span><span class="ei-sub">Decida si el problema pide multiplicar o dividir, y resuélvalo.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-4-3.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-4-3.html">página de práctica de esta lección</a> ')
R("and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you. In the last activity, multiplying and dividing are mixed: the hard part is not the math, it is deciding which one the problem needs.</li>", "y haga cada actividad. Los ejercicios cambian cada vez. Haga por lo menos 10 en cada actividad y siga hasta acertar 8 de 10 al primer intento. El marcador de cada actividad lleva la cuenta por usted. En la última actividad se mezclan la multiplicación y la división: lo difícil no son las cuentas, sino decidir cuál necesita el problema.</li>")
R(f"<li><strong>With a sheet of paper.</strong> Fold a sheet in half and shade that half. Fold it in half again the other way, and shade half of the shaded part with another color. Open it and count the parts: there it is, in your hands, why {F(1,2)} × {F(1,2)} = {F(1,4)}. Repeat with thirds: fold in three, then in half. The area model on the practice page shows the same idea.</li>",
  f"<li><strong>Con una hoja de papel.</strong> Doble una hoja por la mitad y sombree esa mitad. Dóblela otra vez por la mitad en el otro sentido, y sombree con otro color la mitad de la parte sombreada. Ábrala y cuente las partes: ahí tiene, en sus manos, por qué {F(1,2)} × {F(1,2)} = {F(1,4)}. Repítalo con tercios: doble en tres y después por la mitad. El modelo de área de la página de práctica muestra la misma idea.</li>")
R(f"<li><strong>In your kitchen.</strong> Take a recipe. Find how much of each ingredient you would need for half the recipe (multiply by {F(1,2)}) and for double the recipe (multiply by 2). Write the two columns next to the original amounts.</li>",
  f"<li><strong>En su cocina.</strong> Tome una receta. Halle cuánto necesitaría de cada ingrediente para la mitad de la receta (multiplique por {F(1,2)}) y para el doble (multiplique por 2). Escriba las dos columnas al lado de las cantidades originales.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("To multiply two fractions, you should:", "Para multiplicar dos fracciones, hay que:")
R('type="button">Find a common denominator first.</button><button class="opcion" data-k="b" type="button">Flip both fractions.</button><button class="opcion" data-k="c" type="button">Multiply numerator by numerator and denominator by denominator.</button><button class="opcion" data-k="d" type="button">Add the numerators.</button>',
  'type="button">Hallar primero un denominador común.</button><button class="opcion" data-k="b" type="button">Voltear las dos fracciones.</button><button class="opcion" data-k="c" type="button">Multiplicar numerador por numerador y denominador por denominador.</button><button class="opcion" data-k="d" type="button">Sumar los numeradores.</button>')
R(f"What is {F(2,3)} × {F(1,4)}?", f"¿Cuánto es {F(2,3)} × {F(1,4)}?")
R(f"What is {F(1,2)} of {F(1,3)}?", f"¿Cuánto es {F(1,2)} de {F(1,3)}?")
R(f"What is the reciprocal of {F(2,9)}?", f"¿Cuál es el recíproco de {F(2,9)}?")
R("To divide fractions, after you keep the first fraction the same, you should:", "Para dividir fracciones, después de dejar igual la primera fracción, hay que:")
R('type="button">Flip the first fraction and add.</button><button class="opcion" data-k="b" type="button">Flip both fractions.</button><button class="opcion" data-k="c" type="button">Find a common denominator.</button><button class="opcion" data-k="d" type="button">Change ÷ to ×, flip the second fraction, and multiply.</button>',
  'type="button">Voltear la primera fracción y sumar.</button><button class="opcion" data-k="b" type="button">Voltear las dos fracciones.</button><button class="opcion" data-k="c" type="button">Hallar un denominador común.</button><button class="opcion" data-k="d" type="button">Cambiar ÷ por ×, voltear la segunda fracción y multiplicar.</button>')
R(f"What is {F(3,5)} ÷ {F(1,2)}?", f"¿Cuánto es {F(3,5)} ÷ {F(1,2)}?")
R(f"A recipe calls for {F(2,3)} cup of oil. To make half of the recipe, how much oil do you need?", f"Una receta pide {F(2,3)} de taza de aceite. Para hacer la mitad de la receta, ¿cuánto aceite necesita?")
t.todas("</span> cup</button>", "</span> de taza</button>")
R("</span> cups</button>", "</span> de taza</button>")
R(f"A ribbon 4 yards long is cut into pieces that are {F(1,4)} yard each. How many pieces do you get?", f"Una cinta de 4 yardas de largo se corta en pedazos de {F(1,4)} de yarda cada uno. ¿Cuántos pedazos salen?")
R('type="button">16 pieces</button><button class="opcion" data-k="b" type="button">1 piece</button><button class="opcion" data-k="c" type="button">4 pieces</button><button class="opcion" data-k="d" type="button">8 pieces</button>',
  'type="button">16 pedazos</button><button class="opcion" data-k="b" type="button">1 pedazo</button><button class="opcion" data-k="c" type="button">4 pedazos</button><button class="opcion" data-k="d" type="button">8 pedazos</button>')
# Lista
R('aria-label="Self-check checklist for multiplying and dividing fractions (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de multiplicación y división de fracciones (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for multiplying and dividing fractions ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas para multiplicar y dividir fracciones ')
R('<tr><th scope="row">Multiply fractions</th><td>I multiply straight across with no mistakes, and I simplify.</td><td>I multiply correctly most of the time.</td><td>I look for a common denominator when I do not need one, or I mix up the steps.</td></tr>',
  '<tr><th scope="row">Multiplicar fracciones</th><td>Multiplico en línea recta sin errores, y simplifico.</td><td>Multiplico bien la mayoría de las veces.</td><td>Busco un denominador común cuando no hace falta, o confundo los pasos.</td></tr>')
R('<tr><th scope="row">Find the reciprocal</th><td>I find the reciprocal of any fraction or whole number.</td><td>I find the reciprocal of a fraction, but whole numbers confuse me.</td><td>I mix up the reciprocal with the original fraction.</td></tr>',
  '<tr><th scope="row">Hallar el recíproco</th><td>Hallo el recíproco de cualquier fracción o número entero.</td><td>Hallo el recíproco de una fracción, pero los números enteros me confunden.</td><td>Confundo el recíproco con la fracción original.</td></tr>')
R('<tr><th scope="row">Divide fractions</th><td>I use "keep, change, flip" with no mistakes.</td><td>I divide correctly, with an occasional slip.</td><td>I flip the wrong fraction, or I forget to change ÷ to ×.</td></tr>',
  '<tr><th scope="row">Dividir fracciones</th><td>Uso «dejar, cambiar, voltear» sin errores.</td><td>Divido bien, con algún descuido de vez en cuando.</td><td>Volteo la fracción equivocada, u olvido cambiar ÷ por ×.</td></tr>')
R('<tr><th scope="row">Solve problems and simplify</th><td>I choose the right operation, solve, simplify, and check that the answer makes sense.</td><td>I set up the problem correctly, but I do not always simplify.</td><td>I am not sure whether the problem asks me to multiply or to divide.</td></tr>',
  '<tr><th scope="row">Resolver problemas y simplificar</th><td>Elijo la operación correcta, resuelvo, simplifico y reviso que el resultado tenga sentido.</td><td>Planteo bien el problema, pero no siempre simplifico.</td><td>No estoy seguro de si el problema pide multiplicar o dividir.</td></tr>')
# Cierre
R("<p>In this lesson you completed the four operations with fractions: add, subtract, multiply, and divide. You can now work with proper and improper fractions.</p>", "<p>En esta lección completó las cuatro operaciones con fracciones: sumar, restar, multiplicar y dividir. Ya sabe trabajar con fracciones propias e impropias.</p>")
R(f"<p>One piece of Topic 4 is still missing. So far you have worked with fractions on their own. In <strong>Lesson 4.4 · Operations with mixed numbers</strong> you will see what happens when a whole number comes with a fraction, like 2&nbsp;{F(1,2)} cups, and how to calculate with them using everything you already know.</p>",
  f"<p>Todavía falta una pieza del Tema 4. Hasta ahora trabajó con fracciones solas. En la <strong>Lección 4.4 · Operaciones con números mixtos</strong> verá qué pasa cuando un número entero viene con una fracción, como 2&nbsp;{F(1,2)} tazas, y cómo calcular con ellos usando todo lo que ya sabe.</p>")
R('Next: <a href="lesson-4-4.html">Lesson 4.4 · Operations with mixed numbers</a>', 'Siguiente: <a href="leccion-4-4.html">Lección 4.4 · Operaciones con números mixtos</a>')
R("""<dt>product</dt><dd>The answer to a multiplication. The product of 1/2 and 3/4 is 3/8.</dd>
<dt>quotient</dt><dd>The answer to a division. The quotient of 3/4 ÷ 1/2 is 3/2.</dd>
<dt>reciprocal</dt><dd>A fraction flipped upside down. The reciprocal of 3/4 is 4/3. A number times its reciprocal equals 1.</dd>
<dt>keep, change, flip</dt><dd>The steps to divide fractions: keep the first fraction, change ÷ to ×, and flip the second fraction.</dd>
<dt>"of"</dt><dd>In a problem with fractions, "of" usually means multiply: half of 3/4 is 1/2 × 3/4.</dd>
<dt>area model</dt><dd>A rectangle cut into rows and columns that shows the product of two fractions as the part where they overlap.</dd>""",
"""<dt>producto</dt><dd>El resultado de una multiplicación. El producto de 1/2 y 3/4 es 3/8.</dd>
<dt>cociente</dt><dd>El resultado de una división. El cociente de 3/4 ÷ 1/2 es 3/2.</dd>
<dt>recíproco</dt><dd>Una fracción volteada. El recíproco de 3/4 es 4/3. Un número por su recíproco da 1.</dd>
<dt>dejar, cambiar, voltear</dt><dd>Los pasos para dividir fracciones: dejar la primera fracción, cambiar ÷ por × y voltear la segunda fracción.</dd>
<dt>«de»</dt><dd>En un problema con fracciones, «de» casi siempre quiere decir multiplicar: la mitad de 3/4 es 1/2 × 3/4.</dd>
<dt>modelo de área</dt><dd>Un rectángulo cortado en filas y columnas que muestra el producto de dos fracciones como la parte donde se cruzan.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.3</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 4 · Lección 4.3</p>")
t.js('''{
 next: "Lección 4.4",
 review: "las secciones 2, 3, 4 y 5",
 practice: {
  p1: { ok: "b",
   hints: { a: "Volteó la primera fracción. Para multiplicar no se voltea nada: arriba × arriba, abajo × abajo.", c: "3/4 es solo la segunda fracción. Multiplique también los de abajo: 2 × 4 = 8.", d: "Sumó los de arriba y los de abajo. Este problema pide multiplicar." },
   right: "1 × 3 = 3 arriba y 2 × 4 = 8 abajo. La mitad de 3/4 es 3/8.",
   solution: "Multiplique en línea recta: 1 × 3 = 3 arriba, 2 × 4 = 8 abajo. Así que 1/2 × 3/4 = 3/8." },
  p2: { ok: "a",
   hints: { b: "Sumó los de arriba y los de abajo. La palabra «de» quiere decir multiplicar.", c: "5/6 es 1/3 + 1/2. La palabra «de» quiere decir multiplicar, no sumar.", d: "Un tercio de un medio tiene que ser menos que un medio. Multiplique: 1 × 1 arriba, 3 × 2 abajo." },
   right: "1/3 de 1/2 quiere decir 1/3 × 1/2 = 1/6. Un tercio de un medio es un pedazo pequeño.",
   solution: "«De» quiere decir multiplicar: 1/3 × 1/2 = (1 × 1)/(3 × 2) = 1/6." },
  p3: { ok: "b",
   hints: { a: "Esa es la misma fracción. El recíproco es la fracción volteada.", c: "7/7 es 1 entero. Voltee la fracción: el 5 pasa abajo y el 7 pasa arriba.", d: "Voltee la fracción: el 5 pasa abajo y el 7 pasa arriba." },
   right: "Volteada: el 7 va arriba y el 5 abajo. Y 5/7 × 7/5 = 35/35 = 1.",
   solution: "Voltee la fracción: el numerador 5 pasa abajo y el denominador 7 pasa arriba. El recíproco de 5/7 es 7/5." },
  p4: { ok: "b",
   hints: { a: "Multiplicó sin voltear. Para dividir, voltee la segunda fracción: 1/4 se vuelve 4/1.", c: "Deje la primera fracción, cambie ÷ por × y voltee la segunda: 1/2 × 4/1.", d: "Sumó. Deje la primera fracción, cambie ÷ por × y voltee la segunda." },
   right: "1/2 × 4/1 = 4/2 = 2. En un medio caben dos cuartos.",
   solution: "Deje 1/2, cambie ÷ por × y voltee 1/4 a 4/1: 1/2 × 4/1 = 4/2 = 2. Comprobación: dos cuartos forman un medio." },
  p5: { ok: "b",
   hints: { a: "3 es la mitad de 6. Pero no está tomando la mitad de la tabla: está contando cuántos pedazos de medio pie caben en ella.", c: "Cada pedazo mide solo medio pie, así que salen más pedazos que pies.", d: "La pregunta es cuántos pedazos. El resultado tiene que ser un número entero de pedazos." },
   right: "6 ÷ 1/2 = 6 × 2 = 12. Cada pie da 2 pedazos, y hay 6 pies.",
   solution: "«Cuántos pedazos caben» quiere decir dividir: 6 ÷ 1/2 = 6 × 2/1 = 12 pedazos. Cada pie da 2 pedazos de medio pie, y 6 × 2 = 12." }
 },
 quiz: {
  A: { ok: "c", hints: { a: "El denominador común es para sumar y restar, no para multiplicar.", b: "Voltear es para dividir, y solo la segunda fracción.", d: "Sumar los numeradores es para sumar fracciones con el mismo denominador." },
   solution: "Multiplique en línea recta: numerador × numerador arriba, y denominador × denominador abajo. Después simplifique." },
  B: { ok: "a", hints: { b: "Sumó los de arriba y los de abajo. Multiplíquelos, en cambio.", c: "Volteó la segunda fracción. Eso es para dividir.", d: "Multiplique los de abajo: 3 × 4 = 12." },
   solution: "2 × 1 = 2 arriba y 3 × 4 = 12 abajo: 2/12, que se simplifica a 1/6." },
  C: { ok: "d", hints: { a: "La mitad de un tercio tiene que ser menos que un tercio. «De» quiere decir multiplicar.", b: "5/6 es 1/2 + 1/3. «De» quiere decir multiplicar, no sumar.", c: "3/2 es más que 1. La mitad de un tercio es un pedazo pequeño." },
   solution: "«De» quiere decir multiplicar: 1/2 × 1/3 = (1 × 1)/(2 × 3) = 1/6." },
  D: { ok: "b", hints: { a: "Esa es la misma fracción. Voltéela.", c: "Voltee toda la fracción: el 2 pasa abajo y el 9 arriba.", d: "9/9 es 1. Voltee la fracción: el 2 pasa abajo y el 9 arriba." },
   solution: "Voltee la fracción: el recíproco de 2/9 es 9/2." },
  E: { ok: "d", hints: { a: "La primera fracción se queda igual, y se multiplica, no se suma.", b: "Solo se voltea la segunda fracción.", c: "El denominador común es para sumar y restar." },
   solution: "Deje la primera fracción, cambie ÷ por × y voltee la segunda fracción. Después multiplique." },
  F: { ok: "b", hints: { a: "Multiplicó sin voltear. Voltee la segunda fracción: 1/2 se vuelve 2/1.", c: "Deje 3/5, cambie ÷ por × y voltee 1/2 a 2/1.", d: "Volteó la primera fracción. Solo se voltea la segunda." },
   solution: "3/5 × 2/1 = 6/5 (que es 1 1/5). ¿Cuántos medios caben en 3/5? Un poco más de uno." },
  G: { ok: "c", hints: { a: "Esa es la receta completa. La mitad de la receta necesita menos aceite.", b: "4/3 es el doble del aceite. La mitad de la receta necesita menos.", d: "1/6 es la mitad de 1/3. Halle la mitad de 2/3: 1/2 × 2/3." },
   solution: "La mitad de 2/3 de taza: 1/2 × 2/3 = 2/6 = 1/3 de taza." },
  H: { ok: "a", hints: { b: "Cada pedazo mide solo 1/4 de yarda, así que salen muchos pedazos.", c: "Cada yarda da 4 pedazos, y hay 4 yardas.", d: "Cada yarda da 4 pedazos. ¿Cuántos pedazos hay en 4 yardas?" },
   solution: "4 ÷ 1/4 = 4 × 4 = 16 pedazos. Cada yarda da 4 pedazos, y 4 × 4 = 16." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-4-3.html")
