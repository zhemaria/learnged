"""Crea es/matematicas/nivel-1/leccion-4-1-mcd-mcm.html a partir de math/level-1/lesson-4-1-gcf-lcm.html."""
from traduce import Traductor, F
t = Traductor("math/level-1/lesson-4-1-gcf-lcm.html"); t.leccion(""); t.frecuentes()
R = t.r
t.cabecera("<!-- LearnGED · Complemento de la Lección 4.1 · Matemáticas Nivel 1 (español)\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
R("<title>Lesson 4.1 complement · Factors, multiples, GCF, and LCM · LearnGED</title>", "<title>Complemento de la Lección 4.1 · Factores, múltiplos, MCD y MCM · LearnGED</title>")
R('<p class="ruta">Math · Level 1 · Topic 4 — Fractions · Complement to Lesson 4.1</p>', '<p class="ruta">Matemáticas · Nivel 1 · Tema 4 — Fracciones · Complemento de la Lección 4.1</p>')
R("<h1>Lesson 4.1 complement · Factors, multiples, GCF, and LCM</h1>", "<h1>Complemento de la Lección 4.1 · Factores, múltiplos, MCD y MCM</h1>")
R('<p class="lema">Two small tools that make a big difference: the greatest common factor to simplify, and the least common multiple to add fractions.</p>', '<p class="lema">Dos herramientas pequeñas que hacen una gran diferencia: el máximo común divisor para simplificar, y el mínimo común múltiplo para sumar fracciones.</p>')
R("About 2 hours with practice and homework · take breaks</span>", "Unas 2 horas con la práctica y la tarea · tome descansos</span>")
R("Gets you ready for fractions</span>", "Lo prepara para las fracciones</span>")
R("<li><strong>Tell</strong> the factors of a number apart from its multiples.</li>", "<li><strong>Distinguir</strong> los factores de un número de sus múltiplos.</li>")
R("<li><strong>Recognize</strong> prime numbers and write a number as a product of primes.</li>", "<li><strong>Reconocer</strong> los números primos y escribir un número como producto de primos.</li>")
R("<li><strong>Find</strong> the greatest common factor (GCF) of two numbers in two ways.</li>", "<li><strong>Hallar</strong> el máximo común divisor (MCD) de dos números de dos maneras.</li>")
R("<li><strong>Find</strong> the least common multiple (LCM) of two numbers and use it as a common denominator.</li>", "<li><strong>Hallar</strong> el mínimo común múltiplo (MCM) de dos números y usarlo como denominador común.</li>")
R("<li><strong>Decide</strong> whether a word problem asks for the GCF or the LCM.</li>", "<li><strong>Decidir</strong> si un problema verbal pide el MCD o el MCM.</li>")
R('<li><a href="#s-factors">Factors and multiples</a></li>', '<li><a href="#s-factores">Factores y múltiplos</a></li>')
R('<li><a href="#s-primes">Prime numbers and prime factorization</a></li>', '<li><a href="#s-primos">Números primos y factorización prima</a></li>')
R('<li><a href="#s-gcf">The greatest common factor (GCF)</a></li>', '<li><a href="#s-mcd">El máximo común divisor (MCD)</a></li>')
R('<li><a href="#s-lcm">The least common multiple (LCM)</a></li>', '<li><a href="#s-mcm">El mínimo común múltiplo (MCM)</a></li>')
R('<li><a href="#s-which">GCF or LCM? How to decide in a problem</a></li>', '<li><a href="#s-cual">¿MCD o MCM? Cómo decidir en un problema</a></li>')
R('<span class="etiqueta et-verde">Why this lesson?</span>', '<span class="etiqueta et-verde">¿Por qué esta lección?</span>')
R('<p>In Lesson 4.1 you simplified fractions by looking for "a number that divides both." When that number is the greatest possible, it has a name: the <strong>greatest common factor</strong>. And in Lesson 4.2, to add fractions with different denominators, you need a <strong>common denominator</strong>: the easiest one is the <strong>least common multiple</strong>.</p>',
  '<p>En la Lección 4.1 simplificó fracciones buscando «un número que divida a los dos». Cuando ese número es el más grande posible, tiene nombre: el <strong>máximo común divisor</strong>. Y en la Lección 4.2, para sumar fracciones con denominadores distintos, necesita un <strong>denominador común</strong>: el más cómodo es el <strong>mínimo común múltiplo</strong>.</p>')
R('<p>This lesson explains both ideas from the beginning. The GED® test also asks about them directly ("What is the greatest common factor of 24 and 36?") and inside problems about sharing things and about schedules.</p>',
  '<p>Esta lección explica las dos ideas desde el principio. El examen GED® también pregunta por ellas directamente («¿Cuál es el máximo común divisor de 24 y 36?») y dentro de problemas de repartir cosas y de horarios.</p>')
# 1
R('<h2 id="s-factors"><span aria-hidden="true" class="num-seccion">1</span>Factors and multiples</h2>', '<h2 id="s-factores"><span aria-hidden="true" class="num-seccion">1</span>Factores y múltiplos</h2>')
R("<p>A <strong>factor</strong> (or divisor) of a number is a number that divides it <strong>evenly</strong>, with no remainder. 3 is a factor of 12 because 12 ÷ 3 = 4, with no remainder. 5 is not a factor of 12, because 12 ÷ 5 leaves a remainder of 2.</p>",
  "<p>Un <strong>factor</strong> (o divisor) de un número es un número que lo divide <strong>exactamente</strong>, sin residuo. 3 es factor de 12 porque 12 ÷ 3 = 4, sin residuo. 5 no es factor de 12, porque 12 ÷ 5 deja un residuo de 2.</p>")
R("<p>The best way to find factors is <strong>in pairs</strong>: look for the multiplications that give the number.</p>", "<p>La mejor forma de hallar factores es <strong>en parejas</strong>: busque las multiplicaciones que dan el número.</p>")
R('<p class="titulo-ej">Example: all the factors of 12</p>', '<p class="titulo-ej">Ejemplo: todos los factores de 12</p>')
R("Try the multiplications that give 12, starting with 1: 1 × 12, 2 × 6, 3 × 4.", "Pruebe las multiplicaciones que dan 12, empezando por 1: 1 × 12, 2 × 6, 3 × 4.")
R("The next number, 4, already showed up in the pair 3 × 4. When the pairs start to repeat, the list is complete.", "El número siguiente, 4, ya apareció en la pareja 3 × 4. Cuando las parejas empiezan a repetirse, la lista está completa.")
R("The factors of 12 are 1, 2, 3, 4, 6, and 12.", "Los factores de 12 son 1, 2, 3, 4, 6 y 12.")
R("<p>A <strong>multiple</strong> of a number is what you get when you multiply it by 1, 2, 3, 4… The multiples of 4 are 4, 8, 12, 16, 20, 24… and the list never ends.</p>", "<p>Un <strong>múltiplo</strong> de un número es lo que se obtiene al multiplicarlo por 1, 2, 3, 4… Los múltiplos de 4 son 4, 8, 12, 16, 20, 24… y la lista no se acaba nunca.</p>")
R('<span class="etiqueta et-ambar">Do not mix them up</span>', '<span class="etiqueta et-ambar">No los confunda</span>')
R("<p>A number has <strong>few</strong> factors, and they are never greater than the number (the factors of 12 end at 12). A number has <strong>endless</strong> multiples, and they are never smaller than the number (the multiples of 12 start at 12). Factors: you <strong>divide</strong>. Multiples: you <strong>multiply</strong>.</p>",
  "<p>Un número tiene <strong>pocos</strong> factores, y nunca son mayores que el número (los factores de 12 terminan en 12). Un número tiene <strong>infinitos</strong> múltiplos, y nunca son menores que el número (los múltiplos de 12 empiezan en 12). Factores: se <strong>divide</strong>. Múltiplos: se <strong>multiplica</strong>.</p>")
R("<p>These rules save you divisions when you look for factors:</p>", "<p>Estas reglas le ahorran divisiones cuando busca factores:</p>")
R('aria-label="Divisibility rules (tabla desplazable horizontalmente)"', 'aria-label="Reglas de divisibilidad (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Divisibility rules for 2, 3, 5, and 10</caption>', '<caption class="cap-oculto">Reglas de divisibilidad del 2, el 3, el 5 y el 10</caption>')
R('<th scope="col">A number can be divided by…</th><th scope="col">if…</th><th scope="col">Example</th>', '<th scope="col">Un número se puede dividir entre…</th><th scope="col">si…</th><th scope="col">Ejemplo</th>')
R("<td>it ends in 0, 2, 4, 6, or 8 (it is even).</td><td>38 yes; 27 no.</td>", "<td>termina en 0, 2, 4, 6 u 8 (es par).</td><td>38 sí; 27 no.</td>")
R("<td>the sum of its digits can be divided by 3.</td><td>51: 5 + 1 = 6, yes.</td>", "<td>la suma de sus dígitos se puede dividir entre 3.</td><td>51: 5 + 1 = 6, sí.</td>")
R("<td>it ends in 0 or 5.</td><td>45 yes; 52 no.</td>", "<td>termina en 0 o en 5.</td><td>45 sí; 52 no.</td>")
R("<td>it ends in 0.</td><td>70 yes; 75 no.</td>", "<td>termina en 0.</td><td>70 sí; 75 no.</td>")
R("<h3>Practice 1 — Factors</h3>", "<h3>Práctica 1 — Factores</h3>")
R("Which of these numbers is <strong>not</strong> a factor of 18?", "¿Cuál de estos números <strong>no</strong> es factor de 18?")
R('href="practice-4-1-gcf-lcm.html#factors"', 'href="practica-4-1-mcd-mcm.html#factores"')
R('práctica: factors and multiples (se abre', 'práctica: factores y múltiplos (se abre')
R('<span class="ei-titulo">Practique más: factors and multiples</span><span class="ei-sub">List all the factors of a number in pairs, and tell factors from multiples.</span>', '<span class="ei-titulo">Practique más: factores y múltiplos</span><span class="ei-sub">Haga la lista de todos los factores de un número en parejas, y distinga factores de múltiplos.</span>')
# 2
R('<h2 id="s-primes"><span aria-hidden="true" class="num-seccion">2</span>Prime numbers and prime factorization</h2>', '<h2 id="s-primos"><span aria-hidden="true" class="num-seccion">2</span>Números primos y factorización prima</h2>')
R("<p>A <strong>prime number</strong> has <strong>exactly two factors</strong>: 1 and itself. The first primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29. A number with more than two factors is called <strong>composite</strong> (12 is composite: it has six factors).</p>",
  "<p>Un <strong>número primo</strong> tiene <strong>exactamente dos factores</strong>: el 1 y él mismo. Los primeros primos son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29. Un número con más de dos factores se llama <strong>compuesto</strong> (12 es compuesto: tiene seis factores).</p>")
R('<span class="etiqueta et-verde">Two special cases</span>', '<span class="etiqueta et-verde">Dos casos especiales</span>')
R("<p><strong>1 is not prime</strong>: it has only one factor. And <strong>2 is the only even prime</strong>: every other even number can be divided by 2.</p>", "<p><strong>El 1 no es primo</strong>: tiene un solo factor. Y <strong>el 2 es el único primo par</strong>: todos los demás números pares se pueden dividir entre 2.</p>")
R("<p>Every composite number can be written as a multiplication of primes. This is called its <strong>prime factorization</strong>, and it is like the number's \"fingerprint\": each number has only one.</p>",
  "<p>Todo número compuesto se puede escribir como una multiplicación de primos. Eso se llama su <strong>factorización prima</strong>, y es como la «huella digital» del número: cada número tiene una sola.</p>")
R('<p class="titulo-ej">Example: the prime factorization of 60</p>', '<p class="titulo-ej">Ejemplo: la factorización prima de 60</p>')
R("Divide by the smallest prime that works: 60 ÷ 2 = 30.", "Divida entre el primo más pequeño que sirva: 60 ÷ 2 = 30.")
R("Keep going with the answer: 30 ÷ 2 = 15. 15 is not even, so try 3: 15 ÷ 3 = 5.", "Siga con el resultado: 30 ÷ 2 = 15. 15 no es par, así que pruebe el 3: 15 ÷ 3 = 5.")
R("5 is prime, so you are done.", "5 es primo, así que terminó.")
R("60 = 2 × 2 × 3 × 5, which you can also write as 2² × 3 × 5.", "60 = 2 × 2 × 3 × 5, que también se puede escribir 2² × 3 × 5.")
R('<span class="etiqueta et-verde">Always check</span>', '<span class="etiqueta et-verde">Compruebe siempre</span>')
R("<p>Multiply the primes you found: 2 × 2 × 3 × 5 = 60. If you do not get the number you started with, one of the divisions has a mistake.</p>", "<p>Multiplique los primos que encontró: 2 × 2 × 3 × 5 = 60. Si no le da el número del principio, alguna división tiene un error.</p>")
R("<h3>Practice 2 — Prime factorization</h3>", "<h3>Práctica 2 — Factorización prima</h3>")
R("What is the prime factorization of 36?", "¿Cuál es la factorización prima de 36?")
R('href="practice-4-1-gcf-lcm.html#primes"', 'href="practica-4-1-mcd-mcm.html#primos"')
R('práctica: prime numbers and prime factorization (se abre', 'práctica: números primos y factorización prima (se abre')
R('<span class="ei-titulo">Practique más: prime numbers and prime factorization</span><span class="ei-sub">Decide whether a number is prime or composite, and break numbers into primes with a factor tree.</span>', '<span class="ei-titulo">Practique más: números primos y factorización prima</span><span class="ei-sub">Decida si un número es primo o compuesto, y descomponga números en primos con un árbol de factores.</span>')
# 3
R('<h2 id="s-gcf"><span aria-hidden="true" class="num-seccion">3</span>The greatest common factor (GCF)</h2>', '<h2 id="s-mcd"><span aria-hidden="true" class="num-seccion">3</span>El máximo común divisor (MCD)</h2>')
R("<p>The <strong>greatest common factor (GCF)</strong> of two numbers is the <strong>greatest factor they share</strong>. You can find it in two ways.</p>", "<p>El <strong>máximo común divisor (MCD)</strong> de dos números es el <strong>factor más grande que tienen en común</strong>. Se puede hallar de dos maneras.</p>")
R("<h3>Method 1 · Compare the lists of factors</h3>", "<h3>Método 1 · Compare las listas de factores</h3>")
R('<p class="titulo-ej">Example: the GCF of 12 and 18</p>', '<p class="titulo-ej">Ejemplo: el MCD de 12 y 18</p>')
R("Factors of 12: 1, 2, 3, 4, 6, 12.", "Factores de 12: 1, 2, 3, 4, 6, 12.")
R("Factors of 18: 1, 2, 3, 6, 9, 18.</p>", "Factores de 18: 1, 2, 3, 6, 9, 18.</p>")
R("Factors in both lists: 1, 2, 3, and 6.", "Factores que están en las dos listas: 1, 2, 3 y 6.")
R("The greatest of them is 6. GCF(12, 18) = 6.", "El mayor de ellos es 6. MCD(12, 18) = 6.")
t.todas("<h3>Method 2 · Use the prime factorization</h3>", "<h3>Método 2 · Use la factorización prima</h3>")
R("<p>With big numbers, the lists get long. With the prime factorization, you take <strong>only the primes they share</strong>, each one with its <strong>smaller exponent</strong>.</p>", "<p>Con números grandes, las listas se hacen largas. Con la factorización prima, se toman <strong>solo los primos que tienen en común</strong>, cada uno con su <strong>exponente menor</strong>.</p>")
R('<p class="titulo-ej">Example: the GCF of 24 and 36</p>', '<p class="titulo-ej">Ejemplo: el MCD de 24 y 36</p>')
R("Shared primes: 2 (smaller exponent: 2²) and 3 (smaller exponent: 3¹).", "Primos comunes: 2 (exponente menor: 2²) y 3 (exponente menor: 3¹).")
R("GCF(24, 36) = 2² × 3 = 4 × 3 = 12.", "MCD(24, 36) = 2² × 3 = 4 × 3 = 12.")
R('<span class="etiqueta et-verde">What it is for: simplify in one step</span>', '<span class="etiqueta et-verde">Para qué sirve: simplificar en un solo paso</span>')
R(f"<p>If you divide the numerator and the denominator by their GCF, the fraction is in simplest form right away. To simplify {F(18,24)}: the GCF of 18 and 24 is 6. 18 ÷ 6 = 3 and 24 ÷ 6 = 4. The answer is {F(3,4)}.</p>",
  f"<p>Si divide el numerador y el denominador entre su MCD, la fracción queda en su forma más simple de una vez. Para simplificar {F(18,24)}: el MCD de 18 y 24 es 6. 18 ÷ 6 = 3 y 24 ÷ 6 = 4. El resultado es {F(3,4)}.</p>")
R("<h3>Practice 3 — Greatest common factor</h3>", "<h3>Práctica 3 — Máximo común divisor</h3>")
R("What is the greatest common factor of 20 and 30?", "¿Cuál es el máximo común divisor de 20 y 30?")
R('href="practice-4-1-gcf-lcm.html#gcf"', 'href="practica-4-1-mcd-mcm.html#mcd"')
R('práctica: the greatest common factor (se abre', 'práctica: el máximo común divisor (se abre')
R('<span class="ei-titulo">Practique más: the greatest common factor</span><span class="ei-sub">Find the GCF with lists and with primes, and use it to simplify in one step.</span>', '<span class="ei-titulo">Practique más: el máximo común divisor</span><span class="ei-sub">Halle el MCD con listas y con primos, y úselo para simplificar en un solo paso.</span>')
# 4
R('<h2 id="s-lcm"><span aria-hidden="true" class="num-seccion">4</span>The least common multiple (LCM)</h2>', '<h2 id="s-mcm"><span aria-hidden="true" class="num-seccion">4</span>El mínimo común múltiplo (MCM)</h2>')
R("<p>The <strong>least common multiple (LCM)</strong> of two numbers is the <strong>smallest multiple they share</strong> (not counting zero).</p>", "<p>El <strong>mínimo común múltiplo (MCM)</strong> de dos números es el <strong>múltiplo más pequeño que tienen en común</strong> (sin contar el cero).</p>")
R("<h3>Method 1 · Compare the lists of multiples</h3>", "<h3>Método 1 · Compare las listas de múltiplos</h3>")
R('<p class="titulo-ej">Example: the LCM of 4 and 6</p>', '<p class="titulo-ej">Ejemplo: el MCM de 4 y 6</p>')
R("Multiples of 4: 4, 8, <strong>12</strong>, 16, 20, 24…", "Múltiplos de 4: 4, 8, <strong>12</strong>, 16, 20, 24…")
R("Multiples of 6: 6, <strong>12</strong>, 18, 24…", "Múltiplos de 6: 6, <strong>12</strong>, 18, 24…")
R("The first number in both lists is 12. LCM(4, 6) = 12.", "El primer número que está en las dos listas es 12. MCM(4, 6) = 12.")
R("<p>Take <strong>every prime that shows up</strong>, shared or not, each one with its <strong>greater exponent</strong>.</p>", "<p>Tome <strong>todos los primos que aparecen</strong>, comunes o no, cada uno con su <strong>exponente mayor</strong>.</p>")
R('<p class="titulo-ej">Example: the LCM of 12 and 18</p>', '<p class="titulo-ej">Ejemplo: el MCM de 12 y 18</p>')
R("12 = 2² × 3 and 18 = 2 × 3².", "12 = 2² × 3 y 18 = 2 × 3².")
R("Primes that show up: 2 (greater exponent: 2²) and 3 (greater exponent: 3²).", "Primos que aparecen: 2 (exponente mayor: 2²) y 3 (exponente mayor: 3²).")
R("LCM(12, 18) = 2² × 3² = 4 × 9 = 36.", "MCM(12, 18) = 2² × 3² = 4 × 9 = 36.")
R('<span aria-hidden="true">🧮</span> A shortcut with the calculator</span>', '<span aria-hidden="true">🧮</span> Un atajo con la calculadora</span>')
R("<p>If you already know the GCF: LCM = (first number × second number) ÷ GCF. For 12 and 18, type ", "<p>Si ya sabe el MCD: MCM = (primer número × segundo número) ÷ MCD. Para 12 y 18, escriba ")
R(": the screen shows <strong>36</strong>.</p>", ": la pantalla muestra <strong>36</strong>.</p>")
R('<span class="etiqueta et-verde">What it is for: the common denominator</span>', '<span class="etiqueta et-verde">Para qué sirve: el denominador común</span>')
R(f"<p>To add {F(1,4)} + {F(1,6)}, the LCM of 4 and 6 is 12, the smallest common denominator: ", f"<p>Para sumar {F(1,4)} + {F(1,6)}, el MCM de 4 y 6 es 12, el denominador común más pequeño: ")
R(". A greater denominator (like 24) also works, but then you have to simplify at the end.</p>", ". Un denominador mayor (como 24) también sirve, pero entonces hay que simplificar al final.</p>")
R("<h3>Practice 4 — Least common multiple</h3>", "<h3>Práctica 4 — Mínimo común múltiplo</h3>")
R("What is the least common multiple of 6 and 8?", "¿Cuál es el mínimo común múltiplo de 6 y 8?")
R('href="practice-4-1-gcf-lcm.html#lcm"', 'href="practica-4-1-mcd-mcm.html#mcm"')
R('práctica: the least common multiple (se abre', 'práctica: el mínimo común múltiplo (se abre')
R('<span class="ei-titulo">Practique más: the least common multiple</span><span class="ei-sub">Find the LCM with lists and with primes.</span>', '<span class="ei-titulo">Practique más: el mínimo común múltiplo</span><span class="ei-sub">Halle el MCM con listas y con primos.</span>')
# 5
R('<h2 id="s-which"><span aria-hidden="true" class="num-seccion">5</span>GCF or LCM? How to decide in a problem</h2>', '<h2 id="s-cual"><span aria-hidden="true" class="num-seccion">5</span>¿MCD o MCM? Cómo decidir en un problema</h2>')
R('<p>In word problems, the question does not say "GCF" or "LCM." You have to recognize what it asks for:</p>', '<p>En los problemas verbales, la pregunta no dice «MCD» ni «MCM». Hay que reconocer lo que pide:</p>')
R('aria-label="How to tell if a problem asks for the GCF or the LCM (tabla desplazable horizontalmente)"', 'aria-label="Cómo saber si un problema pide el MCD o el MCM (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">How to tell whether a word problem asks for the GCF or the LCM</caption>', '<caption class="cap-oculto">Cómo saber si un problema verbal pide el MCD o el MCM</caption>')
R('<th scope="col">It asks for the…</th><th scope="col">when the problem is about…</th><th scope="col">Words that give it away</th>', '<th scope="col">Pide el…</th><th scope="col">cuando el problema trata de…</th><th scope="col">Palabras que lo delatan</th>')
R('<tr><th scope="row">GCF</th><td>sharing or cutting into equal groups, as large as possible, with nothing left over.</td><td>"the greatest number of equal groups," "the longest pieces," "with nothing left over."</td></tr>',
  '<tr><th scope="row">MCD</th><td>repartir o cortar en grupos iguales, lo más grandes posible, sin que sobre nada.</td><td>«el mayor número de grupos iguales», «los pedazos más largos», «sin que sobre nada».</td></tr>')
R('<tr><th scope="row">LCM</th><td>things that repeat, and when they happen together again.</td><td>"when will they happen together again?", "at the same time," "every so often."</td></tr>',
  '<tr><th scope="row">MCM</th><td>cosas que se repiten, y cuándo vuelven a coincidir.</td><td>«¿cuándo vuelven a coincidir?», «al mismo tiempo», «cada cierto tiempo».</td></tr>')
R('<p class="titulo-ej">Example: a sharing problem (GCF)</p>', '<p class="titulo-ej">Ejemplo: un problema de repartir (MCD)</p>')
R('<p><em>"A food pantry has 24 cans of beans and 36 cans of corn. It wants to make identical bags, with the same number of each kind of can and no cans left over. What is the greatest number of bags it can make?"</em></p>',
  '<p><em>«Un banco de comida tiene 24 latas de frijoles y 36 latas de maíz. Quiere hacer bolsas idénticas, con la misma cantidad de cada tipo de lata y sin que sobre ninguna. ¿Cuál es el mayor número de bolsas que puede hacer?»</em></p>')
R("You share into equal groups, as large as possible: the problem asks for the GCF.", "Se reparte en grupos iguales, lo más grandes posible: el problema pide el MCD.")
R("GCF(24, 36) = 12.", "MCD(24, 36) = 12.")
R("12 bags, each with 24 ÷ 12 = 2 cans of beans and 36 ÷ 12 = 3 cans of corn.", "12 bolsas, cada una con 24 ÷ 12 = 2 latas de frijoles y 36 ÷ 12 = 3 latas de maíz.")
R('<p class="titulo-ej">Example: a schedule problem (LCM)</p>', '<p class="titulo-ej">Ejemplo: un problema de horarios (MCM)</p>')
R('<p><em>"One bus stops at the corner every 15 minutes, and another every 20 minutes. At 8:00 they both stop together. When will they stop together again?"</em></p>',
  '<p><em>«Un autobús para en la esquina cada 15 minutos, y otro cada 20 minutos. A las 8:00 paran los dos juntos. ¿Cuándo volverán a parar juntos?»</em></p>')
R("Things repeat, and you want to know when they meet again: the problem asks for the LCM.", "Las cosas se repiten, y quiere saber cuándo vuelven a coincidir: el problema pide el MCM.")
R("Multiples of 15: 15, 30, 45, <strong>60</strong>. Multiples of 20: 20, 40, <strong>60</strong>. LCM(15, 20) = 60.", "Múltiplos de 15: 15, 30, 45, <strong>60</strong>. Múltiplos de 20: 20, 40, <strong>60</strong>. MCM(15, 20) = 60.")
R("They meet again 60 minutes later, at 9:00.", "Vuelven a coincidir 60 minutos después, a las 9:00.")
R("<h3>Practice 5 — GCF or LCM?</h3>", "<h3>Práctica 5 — ¿MCD o MCM?</h3>")
R("You have two ribbons, one 18 inches long and one 24 inches long. You want to cut them into pieces that are all the same length, as long as possible, with no ribbon left over. How long should each piece be?",
  "Tiene dos cintas, una de 18 pulgadas y otra de 24 pulgadas. Quiere cortarlas en pedazos todos del mismo largo, lo más largos posible, sin que sobre cinta. ¿Cuánto debe medir cada pedazo?")
for n in ["6", "72", "3", "12"]:
    R('type="button">' + n + ' inches</button>', 'type="button">' + n + ' pulgadas</button>')
R('href="practice-4-1-gcf-lcm.html#which"', 'href="practica-4-1-mcd-mcm.html#cual"')
R('práctica: GCF or LCM? (se abre', 'práctica: ¿MCD o MCM? (se abre')
R('<span class="ei-titulo">Practique más: GCF or LCM?</span><span class="ei-sub">Read real problems and decide whether they ask for the GCF or the LCM, then solve them.</span>', '<span class="ei-titulo">Practique más: ¿MCD o MCM?</span><span class="ei-sub">Lea problemas reales, decida si piden el MCD o el MCM, y resuélvalos.</span>')
# Tarea
R('<li><strong>The practice page.</strong> Open the <a href="practice-4-1-gcf-lcm.html">practice page for this lesson</a> ', '<li><strong>La página de práctica.</strong> Abra la <a href="practica-4-1-mcd-mcm.html">página de práctica de esta lección</a> ')
R("<li><strong>Paper and pencil.</strong> Write the prime factorization of 48, 72, 90, and 100, and check each one by multiplying. Then find the GCF and the LCM of 48 and 72, and of 90 and 100, with both methods. Both methods must give the same answer.</li>",
  "<li><strong>Papel y lápiz.</strong> Escriba la factorización prima de 48, 72, 90 y 100, y compruebe cada una multiplicando. Después halle el MCD y el MCM de 48 y 72, y de 90 y 100, con los dos métodos. Los dos métodos tienen que dar el mismo resultado.</li>")
R("<li><strong>Simplify in one step.</strong> Simplify 24/36, 45/60, and 56/84 by dividing by the GCF in one step.</li>", "<li><strong>Simplifique en un solo paso.</strong> Simplifique 24/36, 45/60 y 56/84 dividiendo entre el MCD de una vez.</li>")
R("<li><strong>In your daily life.</strong> Think of two things that repeat every so often (a medicine every 8 hours and a meal every 6 hours, two work shifts, two bus routes). Find how often they happen together, and write it in a sentence.</li>",
  "<li><strong>En su vida diaria.</strong> Piense en dos cosas que se repiten cada cierto tiempo (una medicina cada 8 horas y una comida cada 6 horas, dos turnos de trabajo, dos rutas de autobús). Halle cada cuánto coinciden, y escríbalo en una oración.</li>")
# Quiz
R("<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>.", "<p>Responda las <strong>8 preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>.")
R("What are all the factors of 15?", "¿Cuáles son todos los factores de 15?")
R('type="button">Only 1 and 15</button><button class="opcion" data-k="b" type="button">Only 3 and 5</button><button class="opcion" data-k="c" type="button">1, 3, 5, and 15</button><button class="opcion" data-k="d" type="button">15, 30, and 45</button>',
  'type="button">Solo 1 y 15</button><button class="opcion" data-k="b" type="button">Solo 3 y 5</button><button class="opcion" data-k="c" type="button">1, 3, 5 y 15</button><button class="opcion" data-k="d" type="button">15, 30 y 45</button>')
R("Which of these numbers is <strong>prime</strong>?", "¿Cuál de estos números es <strong>primo</strong>?")
R("What is the prime factorization of 40?", "¿Cuál es la factorización prima de 40?")
R("What is the greatest common factor of 16 and 24?", "¿Cuál es el máximo común divisor de 16 y 24?")
R("What is the least common multiple of 3 and 5?", "¿Cuál es el mínimo común múltiplo de 3 y 5?")
R("What is the least common multiple of 8 and 12?", "¿Cuál es el mínimo común múltiplo de 8 y 12?")
R(f"If you divide the numerator and the denominator of {F(15,45)} by their GCF, which fraction do you get?", f"Si divide el numerador y el denominador de {F(15,45)} entre su MCD, ¿qué fracción obtiene?")
R("Two lights blink together now. One blinks every 6 seconds and the other every 9 seconds. In how many seconds will they blink together again?", "Dos luces parpadean juntas ahora. Una parpadea cada 6 segundos y la otra cada 9 segundos. ¿En cuántos segundos volverán a parpadear juntas?")
for n in ["18", "54", "3", "15"]:
    R('type="button">' + n + ' seconds</button>', 'type="button">' + n + ' segundos</button>')
# Lista
R('aria-label="Self-check checklist for factors, GCF, and LCM (tabla desplazable horizontalmente)"', 'aria-label="Lista de autoevaluación de factores, MCD y MCM (tabla desplazable horizontalmente)"')
R('<caption class="cap-oculto">Self-check checklist: factors, primes, GCF, and LCM, ', '<caption class="cap-oculto">Lista de autoevaluación: factores, primos, MCD y MCM, ')
R('<tr><th scope="row">Tell factors from multiples</th><td>I list all the factors in pairs and explain how they differ from multiples.</td><td>I list the factors, but sometimes I miss one.</td><td>I mix up factors and multiples.</td></tr>',
  '<tr><th scope="row">Distinguir factores de múltiplos</th><td>Hago la lista de todos los factores en parejas y explico en qué se diferencian de los múltiplos.</td><td>Hago la lista de los factores, pero a veces se me escapa uno.</td><td>Confundo factores y múltiplos.</td></tr>')
R('<tr><th scope="row">Write the prime factorization</th><td>I find the prime factorization and check it by multiplying.</td><td>I find it, sometimes with extra steps.</td><td>I leave composite numbers in it (like 4 × 9).</td></tr>',
  '<tr><th scope="row">Escribir la factorización prima</th><td>Hallo la factorización prima y la compruebo multiplicando.</td><td>La hallo, a veces con pasos de más.</td><td>Dejo números compuestos en ella (como 4 × 9).</td></tr>')
R('<tr><th scope="row">Find the GCF and the LCM</th><td>I find them with both methods and use them to simplify and add fractions.</td><td>I find them correctly with one method.</td><td>I switch the GCF and the LCM.</td></tr>',
  '<tr><th scope="row">Hallar el MCD y el MCM</th><td>Los hallo con los dos métodos y los uso para simplificar y sumar fracciones.</td><td>Los hallo bien con un método.</td><td>Confundo el MCD con el MCM.</td></tr>')
R('<tr><th scope="row">Choose between GCF and LCM</th><td>I recognize what the problem asks for and explain my choice.</td><td>I choose well in problems like the examples.</td><td>I guess between the two.</td></tr>',
  '<tr><th scope="row">Elegir entre MCD y MCM</th><td>Reconozco lo que pide el problema y explico mi elección.</td><td>Elijo bien en problemas como los de los ejemplos.</td><td>Adivino entre los dos.</td></tr>')
# Cierre
R("<p>You can now find the factors and the multiples of a number, write its prime factorization, and find the <strong>GCF</strong> and the <strong>LCM</strong>. These are exactly the two tools fractions need.</p>",
  "<p>Ya sabe hallar los factores y los múltiplos de un número, escribir su factorización prima y hallar el <strong>MCD</strong> y el <strong>MCM</strong>. Son justo las dos herramientas que necesitan las fracciones.</p>")
R('<p>Go back to <a href="lesson-4-1.html#s-simplify">Lesson 4.1 · Simplify a fraction</a> and see that now you can simplify in one step. Then go on to <strong>Lesson 4.2 · Adding and subtracting fractions</strong>, where the LCM becomes the common denominator.</p>',
  '<p>Vuelva a la <a href="leccion-4-1.html#s-simplificar">Lección 4.1 · Simplificar una fracción</a> y vea que ahora puede simplificar en un solo paso. Después siga con la <strong>Lección 4.2 · Suma y resta de fracciones</strong>, donde el MCM se convierte en el denominador común.</p>')
R('Next: <a href="lesson-4-2.html">Lesson 4.2 · Adding and subtracting fractions</a>', 'Siguiente: <a href="leccion-4-2.html">Lección 4.2 · Suma y resta de fracciones</a>')
R("""<dt>factor (divisor)</dt><dd>A number that divides another number with no remainder. 3 is a factor of 12.</dd>
<dt>multiple</dt><dd>What you get when you multiply a number by 1, 2, 3… The multiples of 4 are 4, 8, 12…</dd>
<dt>prime number</dt><dd>A number with exactly two factors, 1 and itself: 2, 3, 5, 7, 11…</dd>
<dt>composite number</dt><dd>A number with more than two factors, like 12.</dd>
<dt>prime factorization</dt><dd>A number written as a multiplication of primes: 60 = 2² × 3 × 5.</dd>
<dt>greatest common factor (GCF)</dt><dd>The greatest factor two numbers share. GCF(12, 18) = 6.</dd>
<dt>least common multiple (LCM)</dt><dd>The smallest multiple two numbers share. LCM(4, 6) = 12.</dd>""",
"""<dt>factor (divisor)</dt><dd>Un número que divide a otro sin residuo. 3 es factor de 12.</dd>
<dt>múltiplo</dt><dd>Lo que se obtiene al multiplicar un número por 1, 2, 3… Los múltiplos de 4 son 4, 8, 12…</dd>
<dt>número primo</dt><dd>Un número con exactamente dos factores, el 1 y él mismo: 2, 3, 5, 7, 11…</dd>
<dt>número compuesto</dt><dd>Un número con más de dos factores, como 12.</dd>
<dt>factorización prima</dt><dd>Un número escrito como multiplicación de primos: 60 = 2² × 3 × 5.</dd>
<dt>máximo común divisor (MCD)</dt><dd>El factor más grande que tienen en común dos números. MCD(12, 18) = 6.</dd>
<dt>mínimo común múltiplo (MCM)</dt><dd>El múltiplo más pequeño que tienen en común dos números. MCM(4, 6) = 12.</dd>""")
R("<footer><p>LearnGED · Math · Level 1 · Topic 4 · Complement to Lesson 4.1</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Tema 4 · Complemento de la Lección 4.1</p>")
t.js('''{
 next: "Lección 4.2",
 review: "las secciones 1 a 5",
 practice: {
  p1: { ok: "c",
   hints: { a: "18 ÷ 3 = 6 sin residuo, así que 3 es factor.", b: "18 ÷ 6 = 3 sin residuo, así que 6 es factor.", d: "18 ÷ 9 = 2 sin residuo, así que 9 es factor." },
   right: "18 ÷ 4 = 4, residuo 2. Como hay residuo, 4 no es factor de 18.",
   solution: "Las parejas de factores de 18 son 1 × 18, 2 × 9 y 3 × 6. Así que los factores son 1, 2, 3, 6, 9 y 18. El 4 no está en la lista: 18 ÷ 4 deja un residuo de 2." },
  p2: { ok: "c",
   hints: { a: "4 y 9 no son primos. Siga descomponiéndolos: 4 = 2 × 2 y 9 = 3 × 3.", b: "6 no es primo: 6 = 2 × 3.", d: "6 no es primo. Descomponga cada 6 en 2 × 3." },
   right: "Solo números primos: 2 × 2 × 3 × 3 = 36 ✓",
   solution: "36 ÷ 2 = 18, 18 ÷ 2 = 9, 9 ÷ 3 = 3, y 3 es primo. Así que 36 = 2 × 2 × 3 × 3 = 2² × 3². Comprobación: 4 × 9 = 36 ✓" },
  p3: { ok: "b",
   hints: { a: "5 es un factor común, pero ¿hay uno mayor?", c: "60 es un múltiplo común, no un factor común. Los factores no son mayores que el número.", d: "2 es un factor común, pero ¿hay uno mayor?" },
   right: "Factores de 20: 1, 2, 4, 5, 10, 20. Factores de 30: 1, 2, 3, 5, 6, 10, 15, 30. El mayor común es 10.",
   solution: "Haga la lista de los factores. 20: 1, 2, 4, 5, 10, 20. 30: 1, 2, 3, 5, 6, 10, 15, 30. Comunes: 1, 2, 5, 10. El mayor es 10: MCD(20, 30) = 10." },
  p4: { ok: "b",
   hints: { a: "48 es un múltiplo común (6 × 8), pero ¿hay uno menor?", c: "2 es un factor común, no un múltiplo. Los múltiplos no son menores que el número.", d: "14 es 6 + 8. ¿Es 14 múltiplo de 6?" },
   right: "Múltiplos de 8: 8, 16, 24… 24 también es múltiplo de 6. MCM(6, 8) = 24.",
   solution: "Múltiplos de 6: 6, 12, 18, 24, 30… Múltiplos de 8: 8, 16, 24, 32… El primero que está en las dos listas es 24: MCM(6, 8) = 24." },
  p5: { ok: "a",
   hints: { b: "72 es el MCM. ¿Puede un pedazo ser más largo que las cintas? Este problema corta en pedazos iguales: MCD.", c: "3 pulgadas sirve, pero los pedazos deben ser lo más largos posible.", d: "12 no divide exactamente a 18: sobrarían 6 pulgadas de cinta." },
   right: "Pedazos iguales, lo más largos posible, sin que sobre nada: MCD(18, 24) = 6 pulgadas.",
   solution: "Cortar en pedazos iguales, lo más largos posible, sin que sobre nada, pide el MCD. Factores de 18: 1, 2, 3, 6, 9, 18. Factores de 24: 1, 2, 3, 4, 6, 8, 12, 24. MCD = 6 pulgadas: 3 pedazos de la primera cinta y 4 de la segunda." }
 },
 quiz: {
  A: { ok: "c", hints: { a: "15 ÷ 3 = 5 sin residuo, así que 3 también es factor.", b: "1 y 15 también son factores: 1 × 15 = 15.", d: "Esos son múltiplos de 15, no factores." },
   solution: "Parejas de factores de 15: 1 × 15 y 3 × 5. Los factores son 1, 3, 5 y 15." },
  B: { ok: "a", hints: { b: "21 = 3 × 7, así que tiene más de dos factores.", c: "27 = 3 × 9, así que tiene más de dos factores.", d: "33 = 3 × 11, así que tiene más de dos factores." },
   solution: "29 tiene exactamente dos factores, 1 y 29, así que es primo. 21, 27 y 33 se pueden dividir todos entre 3." },
  C: { ok: "d", hints: { a: "4 y 10 no son primos. Siga descomponiéndolos.", b: "20 no es primo. Siga descomponiéndolo.", c: "10 no es primo: 10 = 2 × 5." },
   solution: "40 ÷ 2 = 20, 20 ÷ 2 = 10, 10 ÷ 2 = 5. Así que 40 = 2 × 2 × 2 × 5 = 2³ × 5. Comprobación: 8 × 5 = 40 ✓" },
  D: { ok: "b", hints: { a: "4 es un factor común, pero 8 también divide a los dos.", c: "48 es un múltiplo común, no un factor.", d: "2 es un factor común, pero hay uno mayor." },
   solution: "Factores de 16: 1, 2, 4, 8, 16. Factores de 24: 1, 2, 3, 4, 6, 8, 12, 24. El máximo común divisor es 8." },
  E: { ok: "d", hints: { a: "8 es 3 + 5. ¿Es 8 múltiplo de 3?", b: "1 es factor de todos los números, no un múltiplo de 3 y de 5.", c: "30 es un múltiplo común, pero hay uno menor." },
   solution: "Múltiplos de 5: 5, 10, 15… 15 también es múltiplo de 3. MCM(3, 5) = 15." },
  F: { ok: "c", hints: { a: "48 es un múltiplo común, pero hay uno menor.", b: "4 es un factor común, no un múltiplo.", d: "96 es 8 × 12. Busque un múltiplo común menor." },
   solution: "Múltiplos de 12: 12, 24, 36… 24 también es múltiplo de 8. MCM(8, 12) = 24." },
  G: { ok: "b", hints: { a: "3/9 todavía se puede simplificar. El MCD de 15 y 45 es 15, no 5.", c: "5/15 todavía se puede simplificar. Use el MCD, 15.", d: "Compruebe: 45 ÷ 15 = 3, no 5." },
   solution: "MCD(15, 45) = 15. 15 ÷ 15 = 1 y 45 ÷ 15 = 3. Así que 15/45 = 1/3 en un solo paso." },
  H: { ok: "a", hints: { b: "54 es 6 × 9, un múltiplo común, pero hay uno menor.", c: "3 es un factor común. Las luces se repiten, así que busque un múltiplo común.", d: "15 es 6 + 9. ¿Es 15 múltiplo de 6?" },
   solution: "Cosas que se repiten y vuelven a coincidir: MCM. Múltiplos de 9: 9, 18… 18 también es múltiplo de 6. Vuelven a parpadear juntas en 18 segundos." }
 }
};''')
t.guarda("es/matematicas/nivel-1/leccion-4-1-mcd-mcm.html")
