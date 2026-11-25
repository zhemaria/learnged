"""Crea es/matematicas/nivel-1/leccion-5-1.html a partir de math/level-1/lesson-5-1.html."""
from traduce import Traductor
t = Traductor("math/level-1/lesson-5-1.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Lección 5.1 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 5.1 · Number and shape patterns · LearnGED</title>", "<title>Lección 5.1 · Patrones numéricos y de figuras · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 5 — Patterns and algebraic thinking</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 5 — Patrones y pensamiento algebraico</p>')
R("<h1>Lesson 5.1 · Number and shape patterns</h1>", "<h1>Lección 5.1 · Patrones numéricos y de figuras</h1>")
R('<p class="lema">Find the hidden rule behind a list of numbers or shapes: your first step toward algebra.</p>', '<p class="lema">Descubra la regla escondida detrás de una lista de números o de figuras: su primer paso hacia el álgebra.</p>')
R("Find the rule</span>", "Descubrir la regla</span>")
R("<li><strong>Find the rule</strong> of a number pattern or a shape pattern.</li>", "<li><strong>Descubrir la regla</strong> de un patrón numérico o de figuras.</li>")
R("<li><strong>Continue</strong> a pattern for at least three more terms.</li>", "<li><strong>Continuar</strong> un patrón por lo menos tres términos más.</li>")
R("<li><strong>Find</strong> a missing term in the middle of a pattern.</li>", "<li><strong>Hallar</strong> un término que falta en medio de un patrón.</li>")
R("<li><strong>Explain the rule</strong> of a pattern in clear words.</li>", "<li><strong>Explicar la regla</strong> de un patrón con palabras claras.</li>")
R('<li><a href="#s-new-thinking">A new kind of thinking</a></li>', '<li><a href="#s-nueva-forma">Una nueva forma de pensar</a></li>')
R('<li><a href="#s-number-patterns">Number patterns</a></li>', '<li><a href="#s-patrones-numericos">Patrones numéricos</a></li>')
R('<li><a href="#s-shape-patterns">Shape patterns</a></li>', '<li><a href="#s-patrones-figuras">Patrones de figuras</a></li>')
R('<li><a href="#s-input-output">Input-output tables</a></li>', '<li><a href="#s-entrada-salida">Tablas de entrada y salida</a></li>')
# 1
R('<h2 id="s-new-thinking"><span aria-hidden="true" class="num-seccion">1</span>A new kind of thinking</h2>', '<h2 id="s-nueva-forma"><span aria-hidden="true" class="num-seccion">1</span>Una nueva forma de pensar</h2>')
R("<p>In Topics 1 to 4 you learned to <strong>calculate</strong>: to add, subtract, multiply, and divide whole numbers, decimals, and fractions. That is arithmetic.</p>", "<p>En los Temas 1 a 4 aprendió a <strong>calcular</strong>: a sumar, restar, multiplicar y dividir números enteros, decimales y fracciones. Eso es la aritmética.</p>")
R('<p>Topic 5 takes a new step. Now you will not only find an answer; you will <strong>discover the idea hidden</strong> behind the numbers. When you see 2, 4, 6, 8, … your mind notices something: "they go up by two." That is a <strong>pattern</strong>, and seeing it is the first step toward <strong>algebra</strong>.</p>',
  '<p>El Tema 5 da un paso nuevo. Ahora no solo va a hallar un resultado; va a <strong>descubrir la idea escondida</strong> detrás de los números. Cuando ve 2, 4, 6, 8, … su mente nota algo: «van subiendo de dos en dos». Eso es un <strong>patrón</strong>, y verlo es el primer paso hacia el <strong>álgebra</strong>.</p>')
R('<span class="etiqueta et-verde">The key idea of this lesson</span>', '<span class="etiqueta et-verde">La idea clave de esta lección</span>')
R("<p>A <strong>pattern</strong> (or sequence) is a list of numbers or shapes that follows a <strong>rule</strong>. If you discover the rule, you can predict what comes next, even if you have never seen it.</p>", "<p>Un <strong>patrón</strong> (o sucesión) es una lista de números o de figuras que sigue una <strong>regla</strong>. Si descubre la regla, puede predecir lo que viene después, aunque nunca lo haya visto.</p>")
# 2
R('<h2 id="s-number-patterns"><span aria-hidden="true" class="num-seccion">2</span>Number patterns</h2>', '<h2 id="s-patrones-numericos"><span aria-hidden="true" class="num-seccion">2</span>Patrones numéricos</h2>')
R("<p>In a number pattern, each number is called a <strong>term</strong>. The <strong>rule</strong> tells you how to go from one term to the next. To discover it, look at <strong>what changes from one term to the next</strong>.</p>", "<p>En un patrón numérico, cada número se llama <strong>término</strong>. La <strong>regla</strong> le dice cómo pasar de un término al siguiente. Para descubrirla, fíjese en <strong>qué cambia de un término al siguiente</strong>.</p>")
R("<h3>Patterns that add or subtract</h3>", "<h3>Patrones que suman o restan</h3>")
R("<p>Look at this pattern. What happens from one number to the next?</p>", "<p>Mire este patrón. ¿Qué pasa de un número al siguiente?</p>")
R('aria-label="Pattern: 3, plus 5, 8, plus 5, 13, plus 5, 18, plus 5, unknown term."', 'aria-label="Patrón: 3, más 5, 8, más 5, 13, más 5, 18, más 5, término desconocido."')
R('<p class="titulo-ej">Example: find the rule of 3, 8, 13, 18, …</p>', '<p class="titulo-ej">Ejemplo: descubra la regla de 3, 8, 13, 18, …</p>')
R("<strong>Find the jump.</strong> From 3 to 8 is + 5; from 8 to 13 is + 5; from 13 to 18 is + 5.", "<strong>Busque el salto.</strong> De 3 a 8 es + 5; de 8 a 13 es + 5; de 13 a 18 es + 5.")
R("<strong>Say the rule.</strong> Add 5 each time.", "<strong>Diga la regla.</strong> Sumar 5 cada vez.")
R("<strong>Use the rule.</strong> The next term is 18 + 5 = <strong>23</strong>.", "<strong>Use la regla.</strong> El término siguiente es 18 + 5 = <strong>23</strong>.")
R("<p>A pattern can also go down. In 40, 36, 32, 28, … the jump is − 4 each time, so the rule is <strong>subtract 4 each time</strong>, and the next term is 28 − 4 = 24.</p>", "<p>Un patrón también puede bajar. En 40, 36, 32, 28, … el salto es − 4 cada vez, así que la regla es <strong>restar 4 cada vez</strong>, y el término siguiente es 28 − 4 = 24.</p>")
R("<h3>Patterns that multiply</h3>", "<h3>Patrones que multiplican</h3>")
R("<p>Not every pattern adds. In this one, you get each term by <strong>multiplying</strong>:</p>", "<p>No todos los patrones suman. En este, cada término se obtiene <strong>multiplicando</strong>:</p>")
R('aria-label="Pattern: 2, times 2, 4, times 2, 8, times 2, 16, times 2, unknown term."', 'aria-label="Patrón: 2, por 2, 4, por 2, 8, por 2, 16, por 2, término desconocido."')
R("<p>Here the rule is <strong>multiply by 2 each time</strong>. The next term is 16 × 2 = <strong>32</strong>.</p>", "<p>Aquí la regla es <strong>multiplicar por 2 cada vez</strong>. El término siguiente es 16 × 2 = <strong>32</strong>.</p>")
R('<span class="etiqueta et-ambar">A tip to find the rule</span>', '<span class="etiqueta et-ambar">Un consejo para descubrir la regla</span>')
R("<p>First ask yourself: <strong>do the numbers grow slowly or very fast?</strong> If they grow slowly and evenly, the rule usually adds. If they grow very fast (they double or triple), the rule usually multiplies. Then check your rule on <strong>every</strong> pair of terms, not just the first two.</p>",
  "<p>Primero pregúntese: <strong>¿los números crecen despacio o muy rápido?</strong> Si crecen despacio y parejo, la regla casi siempre suma. Si crecen muy rápido (se duplican o se triplican), la regla casi siempre multiplica. Después compruebe su regla en <strong>cada</strong> pareja de términos, no solo en los dos primeros.</p>")
R('<p>The calculator can repeat a rule for you. If you press <span class="tecla">enter</span> on an empty line, it does the last calculation again with the new answer.</p>', '<p>La calculadora puede repetir una regla por usted. Si pulsa <span class="tecla">enter</span> en una línea vacía, vuelve a hacer el último cálculo con el resultado nuevo.</p>')
R('<li>Type the first term, <span class="tecla num">3</span>, and press <span class="tecla">enter</span>.</li>', '<li>Escriba el primer término, <span class="tecla num">3</span>, y pulse <span class="tecla">enter</span>.</li>')
R('<li>Press <span class="tecla">+</span> <span class="tecla num">5</span> <span class="tecla">enter</span>. The calculator writes ans+5 (the last answer plus 5) and shows 8.</li>', '<li>Pulse <span class="tecla">+</span> <span class="tecla num">5</span> <span class="tecla">enter</span>. La calculadora escribe ans+5 (el último resultado más 5) y muestra 8.</li>')
R('<li>Press <span class="tecla">enter</span> again and again. Each time it adds 5 one more time: 13, 18, 23, 28.</li>', '<li>Pulse <span class="tecla">enter</span> una y otra vez. Cada vez suma 5 una vez más: 13, 18, 23, 28.</li>')
R('<li>For a pattern that multiplies, do the same with <span class="tecla">×</span>: <span class="tecla num">2</span> <span class="tecla">enter</span>, then <span class="tecla">×</span> <span class="tecla num">2</span> <span class="tecla">enter</span>, then <span class="tecla">enter</span> <span class="tecla">enter</span>. You get 4, 8, 16, 32.</li>',
  '<li>Para un patrón que multiplica, haga lo mismo con <span class="tecla">×</span>: <span class="tecla num">2</span> <span class="tecla">enter</span>, después <span class="tecla">×</span> <span class="tecla num">2</span> <span class="tecla">enter</span>, y después <span class="tecla">enter</span> <span class="tecla">enter</span>. Obtiene 4, 8, 16, 32.</li>')
R("<h3>Practice 1 — Continue a pattern</h3>", "<h3>Práctica 1 — Continuar un patrón</h3>")
R("What number comes next in the pattern <strong>7, 11, 15, 19, ___</strong>?", "¿Qué número sigue en el patrón <strong>7, 11, 15, 19, ___</strong>?")
R("<h3>Practice 2 — The missing term in the middle</h3>", "<h3>Práctica 2 — El término que falta en medio</h3>")
R("In the pattern <strong>5, 10, ___, 20, 25</strong>, what number is missing?", "En el patrón <strong>5, 10, ___, 20, 25</strong>, ¿qué número falta?")
R('href="practice-5-1.html#number-patterns"', 'href="practica-5-1.html#patrones-numericos"')
R('práctica: number patterns (se abre', 'práctica: patrones numéricos (se abre')
R('<span class="ei-titulo">Practique más: number patterns</span><span class="ei-sub">Build your own patterns, find the rule, and find missing terms.</span>', '<span class="ei-titulo">Practique más: patrones numéricos</span><span class="ei-sub">Forme sus propios patrones, descubra la regla y halle los términos que faltan.</span>')
# 3
R('<h2 id="s-shape-patterns"><span aria-hidden="true" class="num-seccion">3</span>Shape patterns</h2>', '<h2 id="s-patrones-figuras"><span aria-hidden="true" class="num-seccion">3</span>Patrones de figuras</h2>')
R("<p>Patterns are not only made of numbers: <strong>shapes</strong> can follow a rule too. Look at how these squares grow:</p>", "<p>Los patrones no son solo de números: las <strong>figuras</strong> también pueden seguir una regla. Mire cómo crecen estos cuadrados:</p>")
R('aria-label="Three figures made of small squares. Figure 1 is 1 square. Figure 2 is a 2-by-2 square, 4 small squares. Figure 3 is a 3-by-3 square, 9 small squares."', 'aria-label="Tres figuras hechas de cuadritos. La figura 1 es 1 cuadrito. La figura 2 es un cuadrado de 2 por 2, 4 cuadritos. La figura 3 es un cuadrado de 3 por 3, 9 cuadritos."')
for k in ["1", "2", "3"]:
    R(f">Figure {k}</text>", f">Figura {k}</text>")
R(">1 square</text>", ">1 cuadrito</text>")
R(">4 squares</text>", ">4 cuadritos</text>")
R(">9 squares</text>", ">9 cuadritos</text>")
R("<p>The number of small squares makes a number pattern: <strong>1, 4, 9, …</strong> Each figure is a square with as many rows as its number: figure 4 will have 4 rows of 4, that is, 4 × 4 = <strong>16</strong> squares.</p>", "<p>La cantidad de cuadritos forma un patrón numérico: <strong>1, 4, 9, …</strong> Cada figura es un cuadrado con tantas filas como su número: la figura 4 tendrá 4 filas de 4, es decir, 4 × 4 = <strong>16</strong> cuadritos.</p>")
R('<span class="etiqueta et-verde">The trick</span>', '<span class="etiqueta et-verde">El truco</span>')
R("<p>You can turn any shape pattern into a number pattern by <strong>counting something</strong>: how many squares, how many dots, how many sides. Once you have the numbers, look for the rule just as you did in section 2.</p>", "<p>Puede convertir cualquier patrón de figuras en un patrón numérico <strong>contando algo</strong>: cuántos cuadritos, cuántos puntos, cuántos lados. Cuando ya tenga los números, busque la regla igual que en la sección 2.</p>")
R("<h3>Practice 3 — A shape pattern</h3>", "<h3>Práctica 3 — Un patrón de figuras</h3>")
R("A pattern of figures has 3, 6, 9, and 12 dots. How many dots will the next figure have?", "Un patrón de figuras tiene 3, 6, 9 y 12 puntos. ¿Cuántos puntos tendrá la figura siguiente?")
R('href="practice-5-1.html#shape-patterns"', 'href="practica-5-1.html#patrones-figuras"')
R('práctica: shape patterns (se abre', 'práctica: patrones de figuras (se abre')
R('<span class="ei-titulo">Practique más: shape patterns</span><span class="ei-sub">Count squares or dots and turn a shape pattern into a number pattern.</span>', '<span class="ei-titulo">Practique más: patrones de figuras</span><span class="ei-sub">Cuente cuadritos o puntos y convierta un patrón de figuras en un patrón numérico.</span>')
# 4
R('<h2 id="s-input-output"><span aria-hidden="true" class="num-seccion">4</span>Input-output tables</h2>', '<h2 id="s-entrada-salida"><span aria-hidden="true" class="num-seccion">4</span>Tablas de entrada y salida</h2>')
R("<p>A very useful way to show a rule is an <strong>input-output table</strong>. The <strong>input</strong> is the number you put in. The <strong>output</strong> is the number that comes out after you use the rule. You can think of a machine: a number goes in, the machine uses its rule, and a new number comes out.</p>",
  "<p>Una forma muy útil de mostrar una regla es una <strong>tabla de entrada y salida</strong>. La <strong>entrada</strong> es el número que se mete. La <strong>salida</strong> es el número que sale después de usar la regla. Puede pensar en una máquina: entra un número, la máquina usa su regla y sale un número nuevo.</p>")
R('aria-label="Input-output table (tabla desplazable horizontalmente)"', 'aria-label="Tabla de entrada y salida (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Input-output table: each input and its output</caption>', '<caption class="cap-oculto">Tabla de entrada y salida: cada entrada y su salida</caption>')
R('<th scope="col">Input</th><th scope="col">Output</th>', '<th scope="col">Entrada</th><th scope="col">Salida</th>')
R('<p class="titulo-ej">Example: find the rule of the table</p>', '<p class="titulo-ej">Ejemplo: descubra la regla de la tabla</p>')
R("<strong>Look across each row.</strong> 1 gives 4, 2 gives 5, 3 gives 6.", "<strong>Mire cada fila de izquierda a derecha.</strong> 1 da 4, 2 da 5, 3 da 6.")
R("<strong>Ask what happened to each input.</strong> 3 was added to each one: 1 + 3 = 4, 2 + 3 = 5, 3 + 3 = 6, 4 + 3 = 7.", "<strong>Pregúntese qué le pasó a cada entrada.</strong> A cada una se le sumó 3: 1 + 3 = 4, 2 + 3 = 5, 3 + 3 = 6, 4 + 3 = 7.")
R("<strong>Say the rule.</strong> The output is the input plus 3. If the input were 10, the output would be 13.", "<strong>Diga la regla.</strong> La salida es la entrada más 3. Si la entrada fuera 10, la salida sería 13.")
R("<p>In an input-output table, the rule connects <strong>each input with its own output</strong>. It does not compare one row with the next. Always read across the row: input → output.</p>", "<p>En una tabla de entrada y salida, la regla une <strong>cada entrada con su propia salida</strong>. No compara una fila con la siguiente. Lea siempre la fila de izquierda a derecha: entrada → salida.</p>")
R("<h3>Practice 4 — An input-output table</h3>", "<h3>Práctica 4 — Una tabla de entrada y salida</h3>")
R("In a table, the input 2 gives the output 6, the input 3 gives the output 9, and the input 4 gives the output 12. What is the rule?", "En una tabla, la entrada 2 da la salida 6, la entrada 3 da la salida 9 y la entrada 4 da la salida 12. ¿Cuál es la regla?")
t.todas('type="button">The output is the input times 3.</button>', 'type="button">La salida es la entrada por 3.</button>')
R('type="button">The output is the input plus 4.</button>', 'type="button">La salida es la entrada más 4.</button>', 2)
R('type="button">The output is the input plus 3.</button>', 'type="button">La salida es la entrada más 3.</button>')
R('type="button">The output is the input minus 3.</button>', 'type="button">La salida es la entrada menos 3.</button>')
R('href="practice-5-1.html#input-output"', 'href="practica-5-1.html#entrada-salida"')
R('práctica: input-output tables (se abre', 'práctica: tablas de entrada y salida (se abre')
R('<span class="ei-titulo">Practique más: input-output tables</span><span class="ei-sub">Find the rule of the machine and complete the outputs.</span>', '<span class="ei-titulo">Practique más: tablas de entrada y salida</span><span class="ei-sub">Descubra la regla de la máquina y complete las salidas.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-5-1.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-5-1.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Make three patterns of your own: one that adds, one that subtracts, and one that multiplies. Write five terms of each. For each one, write the rule in words <strong>before</strong> you write the next term: if you cannot say the rule, you have not found it yet. Then make an input-output table with five rows and write its rule.</li>",
  "<li><strong>Papel y lápiz.</strong> Invente tres patrones: uno que sume, uno que reste y uno que multiplique. Escriba cinco términos de cada uno. Para cada uno, escriba la regla con palabras <strong>antes</strong> de escribir el término siguiente: si no puede decir la regla, todavía no la ha encontrado. Después haga una tabla de entrada y salida de cinco filas y escriba su regla.</li>")
R("<li><strong>In your daily life.</strong> Look for a real pattern: the money you save each week, the times a bus stops at your corner, the house numbers on your street. Write the numbers as a list, describe the rule in words, and predict the next two terms.</li>",
  "<li><strong>En su vida diaria.</strong> Busque un patrón real: el dinero que ahorra cada semana, las horas en que el autobús para en su esquina, los números de las casas de su calle. Escriba los números como una lista, describa la regla con palabras y prediga los dos términos siguientes.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("What number comes next in the pattern <strong>4, 8, 12, 16, ___</strong>?", "¿Qué número sigue en el patrón <strong>4, 8, 12, 16, ___</strong>?")
R("What is the rule of the pattern <strong>50, 45, 40, 35, …</strong>?", "¿Cuál es la regla del patrón <strong>50, 45, 40, 35, …</strong>?")
R('type="button">Add 5 each time.</button><button class="opcion" data-k="b" type="button">Multiply by 5 each time.</button><button class="opcion" data-k="c" type="button">Divide by 5 each time.</button><button class="opcion" data-k="d" type="button">Subtract 5 each time.</button>',
  'type="button">Sumar 5 cada vez.</button><button class="opcion" data-k="b" type="button">Multiplicar por 5 cada vez.</button><button class="opcion" data-k="c" type="button">Dividir entre 5 cada vez.</button><button class="opcion" data-k="d" type="button">Restar 5 cada vez.</button>')
R("What number is missing in the pattern <strong>6, 12, ___, 24, 30</strong>?", "¿Qué número falta en el patrón <strong>6, 12, ___, 24, 30</strong>?")
R("What number comes next in the pattern <strong>3, 6, 12, 24, ___</strong>?", "¿Qué número sigue en el patrón <strong>3, 6, 12, 24, ___</strong>?")
R("A pattern of figures has 5, 10, 15, and 20 dots. How many dots will the next figure have?", "Un patrón de figuras tiene 5, 10, 15 y 20 puntos. ¿Cuántos puntos tendrá la figura siguiente?")
R("In a table, the input 1 gives the output 5, the input 2 gives the output 6, and the input 3 gives the output 7. What is the rule?", "En una tabla, la entrada 1 da la salida 5, la entrada 2 da la salida 6 y la entrada 3 da la salida 7. ¿Cuál es la regla?")
R('type="button">The output is the input times 5.</button>', 'type="button">La salida es la entrada por 5.</button>')
R('type="button">The output is the input plus 1.</button>', 'type="button">La salida es la entrada más 1.</button>')
R('type="button">The output is the input minus 4.</button>', 'type="button">La salida es la entrada menos 4.</button>')
R('The rule is "the output is the input times 4." If the input is <strong>5</strong>, what is the output?', 'La regla es «la salida es la entrada por 4». Si la entrada es <strong>5</strong>, ¿cuál es la salida?')
R("A person saves money like this: in week 1 she has $20, in week 2 she has $35, and in week 3 she has $50. If the pattern goes on, how much will she have in week 4?", "Una persona ahorra dinero así: en la semana 1 tiene $20, en la semana 2 tiene $35 y en la semana 3 tiene $50. Si el patrón sigue, ¿cuánto tendrá en la semana 4?")
# Lista
R('aria-label="Self-check checklist for patterns (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de patrones (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: skills for number and shape patterns ', '<caption class="cap-oculto">Lista de autoevaluación: destrezas con patrones numéricos y de figuras ')
R('<tr><th scope="row">Find the rule of a pattern</th><td>I find the rule in patterns that add, subtract, or multiply.</td><td>I find the rule when the pattern adds or subtracts.</td><td>I do not see what changes from one term to the next.</td></tr>',
  '<tr><th scope="row">Descubrir la regla de un patrón</th><td>Descubro la regla en patrones que suman, restan o multiplican.</td><td>Descubro la regla cuando el patrón suma o resta.</td><td>No veo qué cambia de un término al siguiente.</td></tr>')
R('<tr><th scope="row">Continue a pattern and find missing terms</th><td>I continue the pattern with no mistakes, and I find a missing term in the middle.</td><td>I continue the pattern forward, with an occasional slip.</td><td>I cannot continue the pattern yet.</td></tr>',
  '<tr><th scope="row">Continuar un patrón y hallar términos que faltan</th><td>Continúo el patrón sin errores, y hallo un término que falta en medio.</td><td>Continúo el patrón hacia adelante, con algún descuido de vez en cuando.</td><td>Todavía no puedo continuar el patrón.</td></tr>')
R('<tr><th scope="row">Work with input-output tables</th><td>I find the rule and complete the table with confidence.</td><td>I complete the table when I know the rule.</td><td>I compare one row with the next instead of each input with its output.</td></tr>',
  '<tr><th scope="row">Trabajar con tablas de entrada y salida</th><td>Descubro la regla y completo la tabla con seguridad.</td><td>Completo la tabla cuando sé la regla.</td><td>Comparo una fila con la siguiente en vez de cada entrada con su salida.</td></tr>')
R('<tr><th scope="row">Explain the rule in words</th><td>I explain the rule clearly and exactly ("add 5 each time").</td><td>I explain the rule, but my words are not always exact.</td><td>I cannot say the rule in words yet.</td></tr>',
  '<tr><th scope="row">Explicar la regla con palabras</th><td>Explico la regla con claridad y exactitud («sumar 5 cada vez»).</td><td>Explico la regla, pero mis palabras no siempre son exactas.</td><td>Todavía no puedo decir la regla con palabras.</td></tr>')
# Cierre
R("<p>You can now find the rule of a pattern and say it in words. That is exactly the bridge to algebra.</p>", "<p>Ya sabe descubrir la regla de un patrón y decirla con palabras. Ese es justo el puente hacia el álgebra.</p>")
R("<p>In <strong>Lesson 5.2 · Algebraic language and simple unknowns</strong> you will take the next step: you will write those rules with <strong>symbols</strong> instead of words, and use a letter or a box for a number you do not know yet, the <strong>unknown</strong>. This is the moment when math starts to use its own language.</p>",
  "<p>En la <strong>Lección 5.2 · Lenguaje algebraico e incógnitas simples</strong> dará el paso siguiente: escribirá esas reglas con <strong>símbolos</strong> en vez de palabras, y usará una letra o una cajita para un número que todavía no conoce, la <strong>incógnita</strong>. Es el momento en que las matemáticas empiezan a usar su propio lenguaje.</p>")
R('Next: <a href="lesson-5-2.html">Lesson 5.2 · Algebraic language and simple unknowns</a>', 'Siguiente: <a href="leccion-5-2.html">Lección 5.2 · Lenguaje algebraico e incógnitas simples</a>')
R("""<dt>pattern (sequence)</dt><dd>A list of numbers or shapes that follows a rule, like 3, 8, 13, 18, …</dd>
<dt>term</dt><dd>Each number in a pattern. In 3, 8, 13, the second term is 8.</dd>
<dt>rule</dt><dd>What you do to go from one term to the next, or from an input to its output, like "add 5 each time."</dd>
<dt>input</dt><dd>The number you put into a rule or a table.</dd>
<dt>output</dt><dd>The number you get after you use the rule on the input.</dd>
<dt>input-output table</dt><dd>A table that shows each input next to its output. The rule connects each input with its own output.</dd>""",
"""<dt>patrón (sucesión)</dt><dd>Una lista de números o de figuras que sigue una regla, como 3, 8, 13, 18, …</dd>
<dt>término</dt><dd>Cada número de un patrón. En 3, 8, 13, el segundo término es 8.</dd>
<dt>regla</dt><dd>Lo que se hace para pasar de un término al siguiente, o de una entrada a su salida, como «sumar 5 cada vez».</dd>
<dt>entrada</dt><dd>El número que se mete en una regla o en una tabla.</dd>
<dt>salida</dt><dd>El número que se obtiene después de usar la regla con la entrada.</dd>
<dt>tabla de entrada y salida</dt><dd>Una tabla que muestra cada entrada al lado de su salida. La regla une cada entrada con su propia salida.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.1</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 5 · Lección 5.1</p>")
t.js('''{
 next: "Lección 5.2",
 review: "las secciones 2, 3 y 4",
 practice: {
  p1: { ok: "c",
   hints: { a: "21 es 19 + 2. Mire otra vez el salto: de 7 a 11 es + 4.", b: "24 es 19 + 5. Revise el salto: 11 − 7 = 4, y 15 − 11 = 4.", d: "38 es 19 × 2. Estos números crecen despacio y parejo, así que la regla suma; no multiplica." },
   right: "La regla es sumar 4 cada vez: 19 + 4 = 23.",
   solution: "El salto es + 4 cada vez: 7, 11, 15, 19. Así que el término siguiente es 19 + 4 = 23." },
  p2: { ok: "b",
   hints: { a: "12 es 10 + 2. Busque primero el salto: de 5 a 10 es + 5.", c: "Revise el salto: de 5 a 10 es + 5, y de 20 a 25 también es + 5.", d: "18 está demasiado cerca de 20. El salto es + 5, así que el término que falta es 10 + 5." },
   right: "La regla es sumar 5 cada vez: 10 + 5 = 15, y 15 + 5 = 20.",
   solution: "El salto es + 5 (5 → 10 y 20 → 25). El término que falta va después de 10: 10 + 5 = 15. Comprobación: 15 + 5 = 20." },
  p3: { ok: "a",
   hints: { b: "13 es 12 + 1. Cuente el salto entre figuras: 3 → 6 es + 3.", c: "16 es 12 + 4. El salto entre figuras es + 3 cada vez.", d: "24 es 12 × 2. Los puntos crecen parejo de 3 en 3, así que sume; no multiplique." },
   right: "Cada figura tiene 3 puntos más: 12 + 3 = 15.",
   solution: "Escriba los números: 3, 6, 9, 12. El salto es + 3 cada vez, así que la figura siguiente tiene 12 + 3 = 15 puntos." },
  p4: { ok: "a",
   hints: { b: "Entrada + 4 sirve para la primera fila (2 + 4 = 6), pero revise la segunda: 3 + 4 = 7, no 9.", c: "Eso compara una salida con la siguiente (6 → 9 → 12). La regla une cada entrada con su propia salida: 2 → 6.", d: "Las salidas son mayores que las entradas, así que la regla no puede restar." },
   right: "2 × 3 = 6, 3 × 3 = 9 y 4 × 3 = 12. La regla sirve en todas las filas.",
   solution: "Mire cada fila de izquierda a derecha: 2 → 6, 3 → 9, 4 → 12. Cada salida es 3 veces su entrada. La regla es: la salida es la entrada por 3." }
 },
 quiz: {
  A: { ok: "a", hints: { b: "18 es 16 + 2. Revise el salto: de 4 a 8 es + 4.", c: "24 es 16 + 8, dos saltos de 4. Solo necesita un salto.", d: "32 es 16 × 2. Los números crecen parejo, así que la regla suma 4." },
   solution: "El salto es + 4 cada vez: 4, 8, 12, 16. El término siguiente es 16 + 4 = 20." },
  B: { ok: "d", hints: { a: "Los números bajan, así que la regla no puede sumar.", b: "Multiplicar por 5 hace los números mucho más grandes, pero estos se hacen más pequeños.", c: "50 ÷ 5 = 10, no 45. Halle cuánto baja cada término." },
   solution: "De un término al siguiente, los números bajan 5: 50 − 5 = 45, 45 − 5 = 40, 40 − 5 = 35. La regla es restar 5 cada vez." },
  C: { ok: "b", hints: { a: "16 es 12 + 4. El salto es + 6: 6 → 12.", c: "20 está demasiado cerca de 24. El salto es + 6, así que el término que falta es 12 + 6.", d: "15 no llega ni a la mitad del camino. El salto es + 6, así que el término que falta es 12 + 6." },
   solution: "El salto es + 6 (6 → 12 y 24 → 30). El término que falta es 12 + 6 = 18. Comprobación: 18 + 6 = 24." },
  D: { ok: "c", hints: { a: "36 es 24 + 12. Mire los saltos: + 3, + 6, + 12. No son iguales, así que la regla no suma.", b: "30 es 24 + 6. Los saltos no son iguales, así que la regla no suma.", d: "27 es 24 + 3. Los números crecen muy rápido: pruebe a multiplicar." },
   solution: "Cada término es el anterior por 2: 3 × 2 = 6, 6 × 2 = 12, 12 × 2 = 24. El término siguiente es 24 × 2 = 48." },
  E: { ok: "d", hints: { a: "22 es 20 + 2. El salto entre figuras es + 5.", b: "30 es 20 + 10, dos saltos de 5. Solo necesita uno.", c: "40 es 20 × 2. Los puntos crecen parejo de 5 en 5, así que sume; no multiplique." },
   solution: "Los números son 5, 10, 15, 20. El salto es + 5 cada vez, así que la figura siguiente tiene 20 + 5 = 25 puntos." },
  F: { ok: "a", hints: { b: "Entrada × 5 sirve para la primera fila (1 × 5 = 5), pero revise la segunda: 2 × 5 = 10, no 6.", c: "Eso compara una salida con la siguiente (5 → 6 → 7). Mire cada fila de izquierda a derecha: 1 → 5.", d: "Las salidas son mayores que las entradas, así que la regla no puede restar." },
   solution: "Mire cada fila de izquierda a derecha: 1 + 4 = 5, 2 + 4 = 6, 3 + 4 = 7. La regla es: la salida es la entrada más 4." },
  G: { ok: "b", hints: { a: "9 es 5 + 4. La regla dice multiplicar por 4, no sumar 4.", c: "45 es 5 × 9. Use el número de la regla: 5 × 4.", d: "1 es 5 − 4. La regla dice multiplicar por 4." },
   solution: "La regla es salida = entrada × 4. Con la entrada 5: 5 × 4 = 20." },
  H: { ok: "c", hints: { a: "$55 es $50 + $5. Busque el salto: de $20 a $35 es + $15.", b: "$70 es $50 + $20. El salto es de $15 cada semana: $35 − $20 = $15.", d: "$60 es $50 + $10. El salto es de $15 cada semana, no de $10." },
   solution: "Cada semana la cantidad sube $15: $20, $35, $50. En la semana 4 la persona tendrá $50 + $15 = $65." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-5-1.html")
