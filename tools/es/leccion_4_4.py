"""Crea es/matematicas/nivel-1/leccion-4-4.html a partir de math/level-1/lesson-4-4.html."""
from traduce import Traductor, F
t = Traductor("math/level-1/lesson-4-4.html"); t.leccion(""); t.frecuentes()
R = t.r
def M(e, a, b): return f'<span style="white-space:nowrap">{e}&nbsp;{F(a, b)}</span>'
t.cabecera("<!-- LearnGED · Lección 4.4 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 4.4 · Operations with mixed numbers · LearnGED</title>", "<title>Lección 4.4 · Operaciones con números mixtos · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 4 — Fractions</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 4 — Fracciones</p>')
R("<h1>Lesson 4.4 · Operations with mixed numbers</h1>", "<h1>Lección 4.4 · Operaciones con números mixtos</h1>")
R('<p class="lema">Mixed numbers look hard, but there is a trick that always works: change them to improper fractions and use everything you already learned in this topic.</p>', '<p class="lema">Los números mixtos parecen difíciles, pero hay un truco que siempre funciona: convertirlos en fracciones impropias y usar todo lo que ya aprendió en este tema.</p>')
R("Add, subtract, multiply, and divide</span>", "Sumar, restar, multiplicar y dividir</span>")
R("<li><strong>Change</strong> mixed numbers to improper fractions, and back, with confidence.</li>", "<li><strong>Convertir</strong> números mixtos en fracciones impropias, y al revés, con seguridad.</li>")
R("<li><strong>Multiply and divide</strong> mixed numbers by changing them to improper fractions first.</li>", "<li><strong>Multiplicar y dividir</strong> números mixtos convirtiéndolos primero en fracciones impropias.</li>")
R("<li><strong>Add and subtract</strong> mixed numbers, including cases where you take away more than the fraction you have.</li>", "<li><strong>Sumar y restar</strong> números mixtos, también cuando se quita más que la fracción que se tiene.</li>")
R("<li><strong>Solve</strong> real-life problems with mixed numbers, and simplify the answer.</li>", "<li><strong>Resolver</strong> problemas de la vida real con números mixtos, y simplificar el resultado.</li>")
R('<li><a href="#s-old-friend">An old friend</a></li>', '<li><a href="#s-viejo-amigo">Un viejo conocido</a></li>')
R('<li><a href="#s-convert">Quick review: mixed numbers and improper fractions</a></li>', '<li><a href="#s-convertir">Repaso rápido: números mixtos y fracciones impropias</a></li>')
R('<li><a href="#s-multiply-divide">Multiply and divide mixed numbers</a></li>', '<li><a href="#s-multiplicar-dividir">Multiplicar y dividir números mixtos</a></li>')
R('<li><a href="#s-add-subtract">Add and subtract mixed numbers</a></li>', '<li><a href="#s-sumar-restar">Sumar y restar números mixtos</a></li>')
R('<li><a href="#s-real-life">Mixed numbers in real-life problems</a></li>', '<li><a href="#s-vida-real">Los números mixtos en problemas de la vida real</a></li>')
R('<li><a href="#s-next">The end of Topic 4</a></li>', '<li><a href="#s-siguiente">El final del Tema 4</a></li>')
t.todas('<p class="titulo-ej">Example', '<p class="titulo-ej">Ejemplo')
t.todas("<strong>Change.</strong>", "<strong>Convertir.</strong>"); t.todas("<strong>Simplify.</strong>", "<strong>Simplificar.</strong>"); t.todas("<strong>Change back.</strong>", "<strong>Volver a convertir.</strong>")
t.todas('<span class="etiqueta et-verde">The rule</span>', '<span class="etiqueta et-verde">La regla</span>')
# 1
R('<h2 id="s-old-friend"><span aria-hidden="true" class="num-seccion">1</span>An old friend</h2>', '<h2 id="s-viejo-amigo"><span aria-hidden="true" class="num-seccion">1</span>Un viejo conocido</h2>')
R(f"<p>You have already met mixed numbers in this topic. In Lesson 4.2, the answer 5/4 became {M(1,1,4)}. In Lesson 4.3, the answer 3/2 became {M(1,1,2)}. Today, mixed numbers get a lesson of their own.</p>",
  f"<p>Ya conoció los números mixtos en este tema. En la Lección 4.2, el resultado 5/4 se volvió {M(1,1,4)}. En la Lección 4.3, el resultado 3/2 se volvió {M(1,1,2)}. Hoy los números mixtos tienen una lección propia.</p>")
R(f'<p>A <strong>mixed number</strong> is a whole number together with a fraction. For example, {M(2,1,2)} means "two wholes and one half." We use them every day: a recipe calls for {M(1,3,4)} cups of flour; a board is {M(5,1,2)} feet long; a movie lasts {M(2,1,4)} hours.</p>',
  f'<p>Un <strong>número mixto</strong> es un número entero junto con una fracción. Por ejemplo, {M(2,1,2)} quiere decir «dos enteros y un medio». Los usamos todos los días: una receta pide {M(1,3,4)} tazas de harina; una tabla mide {M(5,1,2)} pies de largo; una película dura {M(2,1,4)} horas.</p>')
R('<span class="etiqueta et-verde">The key idea of this lesson</span>', '<span class="etiqueta et-verde">La idea clave de esta lección</span>')
R("<p>There are no new rules to memorize. The secret to working with mixed numbers is just one: <strong>change them to improper fractions</strong>, then do exactly what you already know how to do with fractions. At the end, write the answer as a mixed number again.</p>",
  "<p>No hay reglas nuevas que memorizar. El secreto para trabajar con números mixtos es uno solo: <strong>convertirlos en fracciones impropias</strong>, y después hacer exactamente lo que ya sabe hacer con fracciones. Al final, vuelva a escribir el resultado como número mixto.</p>")
# 2
R('<h2 id="s-convert"><span aria-hidden="true" class="num-seccion">2</span>Quick review: mixed numbers and improper fractions</h2>', '<h2 id="s-convertir"><span aria-hidden="true" class="num-seccion">2</span>Repaso rápido: números mixtos y fracciones impropias</h2>')
R("<p>The whole lesson rests on this skill, so let us review it carefully before we go on.</p>", "<p>Toda la lección se apoya en esta destreza, así que repasémosla con cuidado antes de seguir.</p>")
R("<h3>From a mixed number to an improper fraction</h3>", "<h3>De número mixto a fracción impropia</h3>")
R("<p><strong>Whole number × denominator + numerator</strong> goes on top. The denominator does not change.</p>", "<p><strong>Entero × denominador + numerador</strong> va arriba. El denominador no cambia.</p>")
R(f": change {M(3,1,4)} to an improper fraction</p>", f": convierta {M(3,1,4)} en fracción impropia</p>")
R("Multiply the whole number by the denominator: 3 × 4 = 12. (Each whole has 4 fourths, so 3 wholes have 12 fourths.)", "Multiplique el entero por el denominador: 3 × 4 = 12. (Cada entero tiene 4 cuartos, así que 3 enteros tienen 12 cuartos.)")
R("Add the numerator: 12 + 1 = 13. That is the new numerator.", "Sume el numerador: 12 + 1 = 13. Ese es el nuevo numerador.")
R("The denominator stays the same: 4.", "El denominador se queda igual: 4.")
R('aria-label="Four bars, each divided into 4 equal parts. The first three bars are fully shaded, and the fourth bar has 1 part shaded: 3 wholes and 1 fourth, which is 13 fourths in all."', 'aria-label="Cuatro barras, cada una dividida en 4 partes iguales. Las tres primeras barras están sombreadas por completo, y la cuarta tiene 1 parte sombreada: 3 enteros y 1 cuarto, que son 13 cuartos en total."')
R("3 whole bars and 1 more fourth: <strong>13 fourths</strong> in all.", "3 barras enteras y 1 cuarto más: <strong>13 cuartos</strong> en total.")
R("<h3>From an improper fraction to a mixed number</h3>", "<h3>De fracción impropia a número mixto</h3>")
R("<p><strong>Numerator ÷ denominator.</strong> The quotient is the whole number, the remainder is the new numerator, and the denominator does not change.</p>", "<p><strong>Numerador ÷ denominador.</strong> El cociente es el entero, el residuo es el nuevo numerador, y el denominador no cambia.</p>")
R(f": change {F(17,5)} to a mixed number</p>", f": convierta {F(17,5)} en número mixto</p>")
R("Divide: 17 ÷ 5 = 3, with 2 left over (remainder 2).", "Divida: 17 ÷ 5 = 3, y sobran 2 (residuo 2).")
R("The quotient (3) is the whole number. The remainder (2) is the numerator.", "El cociente (3) es el entero. El residuo (2) es el numerador.")
R("The denominator stays the same: 5.", "El denominador se queda igual: 5.")
R("<h3>Practice 1 — Change to an improper fraction</h3>", "<h3>Práctica 1 — Convertir en fracción impropia</h3>")
R(f"Change {M(2,1,3)} to an improper fraction.", f"Convierta {M(2,1,3)} en fracción impropia.")
R('href="practice-4-4.html#convert"', 'href="practica-4-4.html#convertir"')
R('práctica: mixed numbers and improper fractions (se abre', 'práctica: números mixtos y fracciones impropias (se abre')
R('<span class="ei-titulo">Practique más: mixed numbers and improper fractions</span><span class="ei-sub">Change mixed numbers to improper fractions and back, and see them with bars.</span>', '<span class="ei-titulo">Practique más: números mixtos y fracciones impropias</span><span class="ei-sub">Convierta números mixtos en fracciones impropias y al revés, y véalos con barras.</span>')
# 3
R('<h2 id="s-multiply-divide"><span aria-hidden="true" class="num-seccion">3</span>Multiply and divide mixed numbers</h2>', '<h2 id="s-multiplicar-dividir"><span aria-hidden="true" class="num-seccion">3</span>Multiplicar y dividir números mixtos</h2>')
R("<p>Here the rule is firm, with no exceptions: <strong>never</strong> multiply or divide the whole numbers on one side and the fractions on the other. Change everything to improper fractions first.</p>", "<p>Aquí la regla es firme, sin excepciones: <strong>nunca</strong> multiplique ni divida los enteros por un lado y las fracciones por otro. Convierta todo primero en fracciones impropias.</p>")
R('<span class="etiqueta et-verde">To multiply or divide mixed numbers</span>', '<span class="etiqueta et-verde">Para multiplicar o dividir números mixtos</span>')
R("<p>1) Change to improper fractions · 2) multiply or divide as in Lesson 4.3 · 3) simplify and change back to a mixed number.</p>", "<p>1) Convierta en fracciones impropias · 2) multiplique o divida como en la Lección 4.3 · 3) simplifique y vuelva a convertir en número mixto.</p>")
R(" (multiply): ", " (multiplicar): "); R(" (divide): ", " (dividir): ")
R(f" and {M(1,1,3)} = {F(4,3)}.", f" y {M(1,1,3)} = {F(4,3)}.")
R(f"<strong>Multiply.</strong> Numerators: 5 × 4 = 20. Denominators: 2 × 3 = 6. You get {F(20,6)}.", f"<strong>Multiplicar.</strong> Numeradores: 5 × 4 = 20. Denominadores: 2 × 3 = 6. Obtiene {F(20,6)}.")
R(" Divide the top and the bottom by 2: ", " Divida el numerador y el denominador entre 2: ")
R("10 ÷ 3 = 3, remainder 1.", "10 ÷ 3 = 3, residuo 1.")
R(f'<p>It is tempting to multiply "2 × 1" and "{F(1,2)} × {F(1,3)}" separately. That gives {M(2,1,6)}, which is wrong: the right answer is {M(3,1,3)}. Always change to improper fractions before you multiply or divide.</p>',
  f'<p>Es tentador multiplicar «2 × 1» y «{F(1,2)} × {F(1,3)}» por separado. Eso da {M(2,1,6)}, que está mal: el resultado correcto es {M(3,1,3)}. Convierta siempre en fracciones impropias antes de multiplicar o dividir.</p>')
R(f" and {M(1,1,2)} = {F(3,2)}.", f" y {M(1,1,2)} = {F(3,2)}.")
R("<strong>Keep, change, flip.</strong> ", "<strong>Dejar, cambiar, voltear.</strong> ")
R(" Divide the top and the bottom by 6: ", " Divida el numerador y el denominador entre 6: ")
R("5 ÷ 2 = 2, remainder 1: ", "5 ÷ 2 = 2, residuo 1: ")
R('<p>The calculator has a template for mixed numbers, U n/d, the second function of <span class="tecla">n/d</span>.</p>', '<p>La calculadora tiene una plantilla para números mixtos, U n/d, la segunda función de <span class="tecla">n/d</span>.</p>')
R(f'<li>For {M(2,1,2)}: type <span class="tecla num">2</span>, press <span class="tecla dos">2nd</span> <span class="tecla">n/d</span>, type <span class="tecla num">1</span>, go down with <span class="tecla">▼</span>, type <span class="tecla num">2</span>, and leave with <span class="tecla">►</span>.</li>',
  f'<li>Para {M(2,1,2)}: escriba <span class="tecla num">2</span>, pulse <span class="tecla dos">2nd</span> <span class="tecla">n/d</span>, escriba <span class="tecla num">1</span>, baje con <span class="tecla">▼</span>, escriba <span class="tecla num">2</span> y salga con <span class="tecla">►</span>.</li>')
R(f'<li>Press <span class="tecla">×</span>, and write {M(1,1,3)} the same way.</li>', f'<li>Pulse <span class="tecla">×</span> y escriba {M(1,1,3)} de la misma manera.</li>')
R(f'<li>Press <span class="tecla">enter</span>. The screen shows the improper fraction {F(10,3)}.</li>', f'<li>Pulse <span class="tecla">enter</span>. La pantalla muestra la fracción impropia {F(10,3)}.</li>')
R(f'<li>To see it as a mixed number, press <span class="tecla dos">2nd</span> <span class="tecla">x⁻¹</span> (n/d◂▸Un/d) and <span class="tecla">enter</span>. The screen shows {M(3,1,3)}.</li>', f'<li>Para verla como número mixto, pulse <span class="tecla dos">2nd</span> <span class="tecla">x⁻¹</span> (n/d◂▸Un/d) y <span class="tecla">enter</span>. La pantalla muestra {M(3,1,3)}.</li>')
R("<h3>Practice 2 — Multiply mixed numbers</h3>", "<h3>Práctica 2 — Multiplicar números mixtos</h3>")
R(f"What is {M(1,1,2)} × 2?", f"¿Cuánto es {M(1,1,2)} × 2?")
R("<h3>Practice 3 — Divide mixed numbers</h3>", "<h3>Práctica 3 — Dividir números mixtos</h3>")
R(f"What is {M(2,1,2)} ÷ {M(1,1,4)}?", f"¿Cuánto es {M(2,1,2)} ÷ {M(1,1,4)}?")
R('href="practice-4-4.html#multiply-divide"', 'href="practica-4-4.html#multiplicar-dividir"')
R('práctica: multiply and divide mixed numbers (se abre', 'práctica: multiplicar y dividir números mixtos (se abre')
R('<span class="ei-titulo">Practique más: multiply and divide mixed numbers</span><span class="ei-sub">Change everything to improper fractions and use the rules from Lesson 4.3.</span>', '<span class="ei-titulo">Practique más: multiplicar y dividir números mixtos</span><span class="ei-sub">Convierta todo en fracciones impropias y use las reglas de la Lección 4.3.</span>')
# 4
R('<h2 id="s-add-subtract"><span aria-hidden="true" class="num-seccion">4</span>Add and subtract mixed numbers</h2>', '<h2 id="s-sumar-restar"><span aria-hidden="true" class="num-seccion">4</span>Sumar y restar números mixtos</h2>')
R("<p>To add and subtract, use the same plan: change to improper fractions, find a common denominator (as in Lesson 4.2), add or subtract, and change back to a mixed number. This one method works for every case.</p>", "<p>Para sumar y restar, use el mismo plan: convierta en fracciones impropias, halle un denominador común (como en la Lección 4.2), sume o reste, y vuelva a convertir en número mixto. Este único método sirve para todos los casos.</p>")
R('<span class="etiqueta et-verde">To add or subtract mixed numbers</span>', '<span class="etiqueta et-verde">Para sumar o restar números mixtos</span>')
R("<p>Change to improper fractions · find a common denominator · add or subtract the numerators · change back to a mixed number.</p>", "<p>Convierta en fracciones impropias · halle un denominador común · sume o reste los numeradores · vuelva a convertir en número mixto.</p>")
R(" (add): ", " (sumar): "); R(" (subtract): ", " (restar): ")
R(f" and {M(2,1,2)} = {F(5,2)}.", f" y {M(2,1,2)} = {F(5,2)}.")
R("<strong>Common denominator (4).</strong> ", "<strong>Denominador común (4).</strong> ")
R("<strong>Add the numerators.</strong> ", "<strong>Sumar los numeradores.</strong> ")
R("17 ÷ 4 = 4, remainder 1: ", "17 ÷ 4 = 4, residuo 1: ")
R("<h3>Subtracting from a whole number</h3>", "<h3>Restar de un número entero</h3>")
R(f'<p>Problems like 4 − {M(1,2,3)} often scare students, because "there is no fraction to take from." With improper fractions, that problem disappears.</p>', f'<p>Problemas como 4 − {M(1,2,3)} suelen asustar, porque «no hay fracción de donde quitar». Con fracciones impropias, ese problema desaparece.</p>')
R(f"<strong>Write the whole number as a fraction.</strong> 4 = {F(4,1)} = {F(12,3)} (common denominator 3).", f"<strong>Escribir el entero como fracción.</strong> 4 = {F(4,1)} = {F(12,3)} (denominador común 3).")
R("<strong>Change the mixed number.</strong> ", "<strong>Convertir el número mixto.</strong> ")
R("<strong>Subtract the numerators.</strong> ", "<strong>Restar los numeradores.</strong> ")
R("7 ÷ 3 = 2, remainder 1: ", "7 ÷ 3 = 2, residuo 1: ")
R('<span class="etiqueta et-verde">Why one method?</span>', '<span class="etiqueta et-verde">¿Por qué un solo método?</span>')
R(f"<p>There is another way to add mixed numbers: wholes with wholes and fractions with fractions. It works, but when you subtract and the top fraction is too small, you must <strong>borrow</strong> a whole (for example, 1 = {F(3,3)}). Changing to improper fractions always works the same way, with no special tricks. Learn this one well, and you can solve all four operations with the same recipe. The practice page shows both ways, so you can compare them.</p>",
  f"<p>Hay otra forma de sumar números mixtos: enteros con enteros y fracciones con fracciones. Funciona, pero cuando resta y la fracción de arriba es demasiado pequeña, tiene que <strong>pedir prestado</strong> un entero (por ejemplo, 1 = {F(3,3)}). Convertir en fracciones impropias funciona siempre de la misma manera, sin trucos especiales. Aprenda bien este método y podrá resolver las cuatro operaciones con la misma receta. La página de práctica muestra las dos formas, para que las compare.</p>")
R("<h3>Practice 4 — Add mixed numbers</h3>", "<h3>Práctica 4 — Sumar números mixtos</h3>")
R(f"What is {M(1,3,4)} + {M(2,1,2)}?", f"¿Cuánto es {M(1,3,4)} + {M(2,1,2)}?")
R('href="practice-4-4.html#add-subtract"', 'href="practica-4-4.html#sumar-restar"')
R('práctica: add and subtract mixed numbers (se abre', 'práctica: sumar y restar números mixtos (se abre')
R('<span class="ei-titulo">Practique más: add and subtract mixed numbers</span><span class="ei-sub">See the steps with improper fractions, and compare them with the wholes-and-fractions way.</span>', '<span class="ei-titulo">Practique más: sumar y restar números mixtos</span><span class="ei-sub">Vea los pasos con fracciones impropias y compárelos con la forma de enteros y fracciones.</span>')
# 5
R('<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Mixed numbers in real-life problems</h2>', '<h2 id="s-vida-real"><span aria-hidden="true" class="num-seccion">5</span>Los números mixtos en problemas de la vida real</h2>')
R("<p>Always use the 4-step method from Lesson 1.3: read and underline, choose the operation, solve, and check if the answer makes sense. Mixed numbers show up most in cooking, carpentry, and measurements.</p>", "<p>Use siempre el método de 4 pasos de la Lección 1.3: lea y subraye, elija la operación, resuelva y compruebe si el resultado tiene sentido. Los números mixtos aparecen sobre todo en la cocina, la carpintería y las medidas.</p>")
R(f'<p class="titulo-ej">📋 "A carpenter has a board 8 feet long and cuts off {M(3,1,2)} feet. How much of the board is left?"</p>', f'<p class="titulo-ej">📋 «Un carpintero tiene una tabla de 8 pies de largo y corta {M(3,1,2)} pies. ¿Cuánto queda de la tabla?»</p>')
R(f"<strong>Read and underline.</strong> A board 8 feet long; cuts off {M(3,1,2)} feet; how much is left.", f"<strong>Lea y subraye.</strong> Una tabla de 8 pies de largo; corta {M(3,1,2)} pies; cuánto queda.")
R(f'<strong>Choose the operation.</strong> "Left" means subtract: 8 − {M(3,1,2)}.', f'<strong>Elija la operación.</strong> «Queda» quiere decir restar: 8 − {M(3,1,2)}.')
R(f"<strong>Solve.</strong> 8 = {F(16,2)} and {M(3,1,2)}", f"<strong>Resuelva.</strong> 8 = {F(16,2)} y {M(3,1,2)}")
R(f"<strong>Does it make sense?</strong> {M(4,1,2)} feet are left, less than the 8 feet at the start. That makes sense, because a piece was cut off.", f"<strong>¿Tiene sentido?</strong> Quedan {M(4,1,2)} pies, menos que los 8 pies del principio. Tiene sentido, porque se cortó un pedazo.")
R("<h3>Practice 5 — A word problem</h3>", "<h3>Práctica 5 — Un problema verbal</h3>")
R(f"A board is {M(5,1,2)} feet long. If you cut off {M(1,3,4)} feet, how much is left?", f"Una tabla mide {M(5,1,2)} pies de largo. Si corta {M(1,3,4)} pies, ¿cuánto queda?")
t.todas("</span></span> feet</button>", "</span></span> pies</button>")
R('href="practice-4-4.html#real-life"', 'href="practica-4-4.html#vida-real"')
R('práctica: mixed numbers in real life (se abre', 'práctica: los números mixtos en la vida real (se abre')
R('<span class="ei-titulo">Practique más: mixed numbers in real life</span><span class="ei-sub">Solve problems about carpentry, recipes, and time with mixed numbers.</span>', '<span class="ei-titulo">Practique más: los números mixtos en la vida real</span><span class="ei-sub">Resuelva problemas de carpintería, recetas y tiempo con números mixtos.</span>')
# Tarea
R("<p>This is independent practice. Plan for about one hour, with your notebook open. With it, you finish Topic 4.</p>", "<p>Esta es práctica independiente. Calcule alrededor de una hora, con su cuaderno abierto. Con ella termina el Tema 4.</p>")
R('<li><strong>The practice page.</strong> Open the <a href="practice-4-4.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-4-4.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Write six mixed numbers, change them to improper fractions, and then change them back to mixed numbers. If you do not get the same number back, the mistake is on the way there or on the way back: find it now. Then solve eight operations, two of each of the four.</li>",
  "<li><strong>Papel y lápiz.</strong> Escriba seis números mixtos, conviértalos en fracciones impropias y después vuelva a convertirlos en números mixtos. Si no le vuelve el mismo número, el error está en la ida o en la vuelta: búsquelo ahora. Después resuelva ocho operaciones, dos de cada una de las cuatro.</li>")
R(f"<li><strong>In your kitchen.</strong> Take a recipe with mixed numbers ({M(1,1,2)} cups, {M(2,3,4)} tablespoons). Find how much you would need to make double the recipe, and write it as a mixed number, not as an improper fraction: it is easier to read when you cook.</li>",
  f"<li><strong>En su cocina.</strong> Tome una receta con números mixtos ({M(1,1,2)} tazas, {M(2,3,4)} cucharadas). Halle cuánto necesitaría para hacer el doble de la receta, y escríbalo como número mixto, no como fracción impropia: es más fácil de leer cuando cocina.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("To multiply or divide mixed numbers, the first thing you do is:", "Para multiplicar o dividir números mixtos, lo primero que se hace es:")
R('type="button">Multiply the whole numbers together and the fractions together.</button><button class="opcion" data-k="b" type="button">Find a common denominator.</button><button class="opcion" data-k="c" type="button">Change each mixed number to an improper fraction.</button><button class="opcion" data-k="d" type="button">Flip both mixed numbers.</button>',
  'type="button">Multiplicar los enteros entre sí y las fracciones entre sí.</button><button class="opcion" data-k="b" type="button">Hallar un denominador común.</button><button class="opcion" data-k="c" type="button">Convertir cada número mixto en fracción impropia.</button><button class="opcion" data-k="d" type="button">Voltear los dos números mixtos.</button>')
R(f"Change {M(3,2,5)} to an improper fraction.", f"Convierta {M(3,2,5)} en fracción impropia.")
R(f"What is {M(2,1,3)} × {M(1,1,2)}?", f"¿Cuánto es {M(2,1,3)} × {M(1,1,2)}?")
R(f"What is {M(4,1,2)} ÷ {M(1,1,2)}?", f"¿Cuánto es {M(4,1,2)} ÷ {M(1,1,2)}?")
R(f"What is {M(2,1,4)} + {M(1,1,2)}?", f"¿Cuánto es {M(2,1,4)} + {M(1,1,2)}?")
R(f"What is 5 − {M(2,3,5)}?", f"¿Cuánto es 5 − {M(2,3,5)}?")
R(f"A recipe uses {M(1,1,2)} cups of sugar. To make double the recipe, how much sugar do you need?", f"Una receta lleva {M(1,1,2)} tazas de azúcar. Para hacer el doble de la receta, ¿cuánta azúcar necesita?")
R('type="button">3 cups</button>', 'type="button">3 tazas</button>')
t.todas("</span></span> cups</button>", "</span></span> tazas</button>")
R(f"A pitcher has {M(3,1,4)} quarts of water, and you use {M(1,3,4)} quarts. How much water is left?", f"Una jarra tiene {M(3,1,4)} cuartos de galón de agua, y usted usa {M(1,3,4)} cuartos. ¿Cuánta agua queda?")
R('type="button">2 quarts</button>', 'type="button">2 cuartos de galón</button>')
t.todas("</span></span> quarts</button>", "</span></span> cuartos de galón</button>")
# Lista
R('aria-label="Self-check checklist for operations with mixed numbers (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de operaciones con números mixtos (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for operations with mixed numbers ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas para operar con números mixtos ')
R('<tr><th scope="row">Change between mixed numbers and improper fractions</th><td>I change both ways quickly and with no mistakes.</td><td>I change correctly most of the time.</td><td>I forget to add the numerator, or I change the denominator.</td></tr>',
  '<tr><th scope="row">Convertir entre números mixtos y fracciones impropias</th><td>Convierto en las dos direcciones, rápido y sin errores.</td><td>Convierto bien la mayoría de las veces.</td><td>Olvido sumar el numerador, o cambio el denominador.</td></tr>')
R('<tr><th scope="row">Multiply and divide mixed numbers</th><td>I change to improper fractions before I operate, and I simplify.</td><td>I operate correctly, with an occasional slip.</td><td>I try to work with the whole numbers and the fractions separately.</td></tr>',
  '<tr><th scope="row">Multiplicar y dividir números mixtos</th><td>Convierto en fracciones impropias antes de operar, y simplifico.</td><td>Opero bien, con algún descuido de vez en cuando.</td><td>Intento trabajar los enteros y las fracciones por separado.</td></tr>')
R('<tr><th scope="row">Add and subtract mixed numbers</th><td>I find the common denominator and solve, even when I subtract from a whole number.</td><td>I add and subtract well in simple cases.</td><td>I get stuck when the fraction I take away is bigger than the one I have.</td></tr>',
  '<tr><th scope="row">Sumar y restar números mixtos</th><td>Hallo el denominador común y resuelvo, aun cuando resto de un número entero.</td><td>Sumo y resto bien en los casos sencillos.</td><td>Me trabo cuando la fracción que quito es mayor que la que tengo.</td></tr>')
R('<tr><th scope="row">Solve problems and simplify</th><td>I choose the right operation, solve, simplify, and write the units.</td><td>I set up the problem correctly, but I do not always change back to a mixed number.</td><td>I am not sure which operation the problem needs.</td></tr>',
  '<tr><th scope="row">Resolver problemas y simplificar</th><td>Elijo la operación correcta, resuelvo, simplifico y escribo las unidades.</td><td>Planteo bien el problema, pero no siempre vuelvo a convertir en número mixto.</td><td>No estoy seguro de qué operación necesita el problema.</td></tr>')
# Cierre
R('<h2 id="s-next"><span aria-hidden="true" class="num-seccion">🏁</span>The end of Topic 4 and the first half of Level 1</h2>', '<h2 id="s-siguiente"><span aria-hidden="true" class="num-seccion">🏁</span>El final del Tema 4 y de la primera mitad del Nivel 1</h2>')
R("<p>With this lesson you finish <strong>Topic 4 · Fractions</strong>. You now know fractions from start to finish: equivalent fractions, simplifying, the four operations, and now mixed numbers too.</p>", "<p>Con esta lección termina el <strong>Tema 4 · Fracciones</strong>. Ya conoce las fracciones de principio a fin: fracciones equivalentes, simplificación, las cuatro operaciones y, ahora, también los números mixtos.</p>")
R('<span class="etiqueta et-verde">An important milestone</span>', '<span class="etiqueta et-verde">Un logro importante</span>')
R("<p>With Topics 1 to 4 complete, you can do the four operations with whole numbers, decimals, fractions, and mixed numbers: all of basic arithmetic. That is the foundation for the rest of the course.</p>", "<p>Con los Temas 1 a 4 completos, ya sabe hacer las cuatro operaciones con números enteros, decimales, fracciones y números mixtos: toda la aritmética básica. Esa es la base del resto del curso.</p>")
R("<p>In <strong>Topic 5 · Patterns and algebraic thinking</strong> you will take a new and exciting step: from numbers to ideas. <strong>Lesson 5.1 · Number and shape patterns</strong> will teach you to discover the hidden rule behind a sequence: your first step toward algebra.</p>",
  "<p>En el <strong>Tema 5 · Patrones y pensamiento algebraico</strong> dará un paso nuevo y emocionante: de los números a las ideas. La <strong>Lección 5.1 · Patrones numéricos y de figuras</strong> le enseñará a descubrir la regla escondida detrás de una sucesión: su primer paso hacia el álgebra.</p>")
R('Next: Topic 5 · <a href="lesson-5-1.html">Lesson 5.1 · Number and shape patterns</a>', 'Siguiente: Tema 5 · Lección 5.1 · Patrones numéricos y de figuras')
R("""<dt>mixed number</dt><dd>A whole number together with a fraction, like 2 1/2 ("two and one half").</dd>
<dt>improper fraction</dt><dd>A fraction whose numerator is greater than or equal to its denominator, like 5/2. It is 1 or more.</dd>
<dt>quotient</dt><dd>The answer to a division. In 17 ÷ 5, the quotient is 3.</dd>
<dt>remainder</dt><dd>What is left over in a division. In 17 ÷ 5, the remainder is 2.</dd>
<dt>borrow</dt><dd>In the wholes-and-fractions way of subtracting, to break one whole into a fraction (like 1 = 3/3) when the top fraction is too small.</dd>""",
"""<dt>número mixto</dt><dd>Un número entero junto con una fracción, como 2 1/2 («dos y un medio»).</dd>
<dt>fracción impropia</dt><dd>Una fracción cuyo numerador es mayor que su denominador o igual a él, como 5/2. Vale 1 o más.</dd>
<dt>cociente</dt><dd>El resultado de una división. En 17 ÷ 5, el cociente es 3.</dd>
<dt>residuo</dt><dd>Lo que sobra en una división. En 17 ÷ 5, el residuo es 2.</dd>
<dt>pedir prestado</dt><dd>En la forma de restar con enteros y fracciones, romper un entero en fracción (como 1 = 3/3) cuando la fracción de arriba es demasiado pequeña.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.4</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 4 · Lección 4.4</p>")
t.js('''{
 next: "Lección 5.1",
 review: "las secciones 2, 3, 4 y 5",
 practice: {
  p1: { ok: "a",
   hints: { b: "6 es 2 × 3, el entero por el denominador. Ahora sume el numerador: 6 + 1.", c: "5 es 2 + 3. Multiplique el entero por el denominador: 2 × 3 = 6. Después sume el numerador.", d: "2/3 es solo la parte de fracción. No se olvide de los 2 enteros: 2 × 3 = 6 tercios." },
   right: "2 × 3 = 6, y 6 + 1 = 7. El denominador sigue siendo 3: 7/3.",
   solution: "Entero × denominador: 2 × 3 = 6. Sume el numerador: 6 + 1 = 7. El denominador sigue siendo 3. Así que 2 1/3 = 7/3." },
  p2: { ok: "b",
   hints: { a: "Multiplicó solo el entero (1 × 2 = 2) y dejó el 1/2. Primero convierta 1 1/2 en 3/2.", c: "Primero convierta 1 1/2 en fracción impropia: 3/2. Después 3/2 × 2/1.", d: "Primero convierta 1 1/2 en fracción impropia: 3/2. Después 3/2 × 2/1." },
   right: "1 1/2 = 3/2, y 3/2 × 2/1 = 6/2 = 3. Dos veces uno y medio es tres.",
   solution: "1 1/2 = 3/2, y 2 = 2/1. Multiplique: 3/2 × 2/1 = 6/2 = 3." },
  p3: { ok: "b",
   hints: { a: "Primero convierta los dos en fracciones impropias: 2 1/2 = 5/2 y 1 1/4 = 5/4. Después deje, cambie y voltee.", c: "Multiplicó en vez de dividir. Voltee la segunda fracción: 5/4 se vuelve 4/5.", d: "Volteó el primer número. Deje 5/2 y voltee solo el segundo: 4/5." },
   right: "5/2 × 4/5 = 20/10 = 2. ¿Cuántas veces cabe 1 1/4 en 2 1/2? Exactamente dos.",
   solution: "2 1/2 = 5/2 y 1 1/4 = 5/4. Dejar, cambiar, voltear: 5/2 × 4/5 = 20/10 = 2." },
  p4: { ok: "b",
   hints: { a: "Convierta en fracciones impropias: 7/4 + 5/2 = 7/4 + 10/4. Cuente otra vez los enteros.", c: "3 3/4 es solo 1 + 2 enteros con los 3/4. Todavía falta sumar el 1/2: 3/4 + 2/4 es más que 1.", d: "Sumó 1/2 + 3/4 como si diera 1/2. Use un denominador común: 3/4 + 2/4 = 5/4." },
   right: "7/4 + 10/4 = 17/4 = 4 1/4.",
   solution: "1 3/4 = 7/4 y 2 1/2 = 5/2 = 10/4. Sume: 7/4 + 10/4 = 17/4. Y 17 ÷ 4 = 4, residuo 1, así que 4 1/4." },
  p5: { ok: "b",
   hints: { a: "Restó las fracciones al revés (3/4 − 1/2). Convierta las dos en cuartos: 22/4 − 7/4.", c: "Revise la resta: 22/4 − 7/4 = 15/4. ¿Cuánto es 15 ÷ 4?", d: "Revise los enteros: 5 1/2 − 1 3/4 es menos que 4. Convierta las dos en cuartos: 22/4 − 7/4." },
   right: "22/4 − 7/4 = 15/4 = 3 3/4 pies.",
   solution: "5 1/2 = 11/2 = 22/4 y 1 3/4 = 7/4. Reste: 22/4 − 7/4 = 15/4. Y 15 ÷ 4 = 3, residuo 3, así que quedan 3 3/4 pies." }
 },
 quiz: {
  A: { ok: "c", hints: { a: "Trabajar los enteros y las fracciones por separado da un resultado equivocado al multiplicar o dividir.", b: "El denominador común es para sumar y restar.", d: "Voltear es para dividir, y solo el segundo número, después de convertirlo en fracción impropia." },
   solution: "Primero convierta cada número mixto en fracción impropia. Después multiplique o divida como en la Lección 4.3." },
  B: { ok: "d", hints: { a: "15 es 3 × 5. Ahora sume el numerador: 15 + 2.", b: "Multiplique el entero por el denominador, no por el numerador: 3 × 5 = 15.", c: "8 es 3 + 5. Multiplique el entero por el denominador: 3 × 5 = 15. Después sume 2." },
   solution: "3 × 5 = 15, y 15 + 2 = 17. El denominador sigue siendo 5: 3 2/5 = 17/5." },
  C: { ok: "a", hints: { b: "Ese es el primer número. Convierta los dos en fracciones impropias y multiplique: 7/3 × 3/2.", c: "No multiplique los enteros y las fracciones por separado. Convierta en fracciones impropias: 7/3 × 3/2.", d: "Convierta en fracciones impropias: 7/3 × 3/2 = 21/6. Simplifique y vuelva a convertir en número mixto." },
   solution: "2 1/3 = 7/3 y 1 1/2 = 3/2. Multiplique: 7/3 × 3/2 = 21/6 = 7/2 = 3 1/2." },
  D: { ok: "b", hints: { a: "Multiplicó en vez de dividir. Voltee el segundo número: 3/2 se vuelve 2/3.", c: "Primero convierta en fracciones impropias: 9/2 ÷ 3/2. Después deje, cambie y voltee.", d: "Primero convierta en fracciones impropias: 9/2 ÷ 3/2. Después deje, cambie y voltee." },
   solution: "4 1/2 = 9/2 y 1 1/2 = 3/2. Dejar, cambiar, voltear: 9/2 × 2/3 = 18/6 = 3. Comprobación: tres veces 1 1/2 es 4 1/2." },
  E: { ok: "c", hints: { a: "Use un denominador común: 1/4 + 2/4 = 3/4, no 1/4.", b: "Sume otra vez los enteros: 2 + 1 = 3, no 4.", d: "1/2 = 2/4, así que 1/4 + 2/4 = 3/4." },
   solution: "2 1/4 = 9/4 y 1 1/2 = 6/4. Sume: 9/4 + 6/4 = 15/4 = 3 3/4." },
  F: { ok: "d", hints: { a: "El resultado tiene que ser menos que 3, porque quita más que 2.", b: "Dejó los 3/5 en vez de quitarlos. Convierta 5 en quintos: 25/5 − 13/5.", c: "El resultado tiene que ser menos que 3, porque quita más que 2. Convierta 5 en quintos: 25/5 − 13/5." },
   solution: "5 = 25/5 y 2 3/5 = 13/5. Reste: 25/5 − 13/5 = 12/5 = 2 2/5." },
  G: { ok: "a", hints: { b: "Duplicó solo el entero. Duplique también el 1/2: 1/2 + 1/2 = 1.", c: "Compruebe: 3/2 × 2 = 6/2. ¿Cuánto es 6 ÷ 2?", d: "El doble quiere decir multiplicar por 2. El resultado tiene que ser más que 1 1/2." },
   solution: "1 1/2 = 3/2, y 3/2 × 2 = 6/2 = 3 tazas." },
  H: { ok: "b", hints: { a: "Revise las fracciones: no se puede quitar 3/4 de 1/4 sin romper un entero. Use fracciones impropias: 13/4 − 7/4.", c: "Convierta las dos en cuartos: 13/4 − 7/4 = 6/4. Simplifíquelo.", d: "Restó 1/4 − 3/4 al revés. Use fracciones impropias: 13/4 − 7/4." },
   solution: "3 1/4 = 13/4 y 1 3/4 = 7/4. Reste: 13/4 − 7/4 = 6/4 = 3/2 = 1 1/2 cuartos de galón." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-4-4.html")
