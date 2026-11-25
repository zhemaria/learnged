"""Builds math/level-1/lesson-4-1-gcf-lcm.html (English): the complement of Lesson 4.1
on factors, multiples, primes, the GCF, and the LCM. Run tools/ged_standards.py afterwards."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def F(n, d):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{n}</span><span class="fb2">{d}</span></span><span class="cap-oculto">{n}/{d}</span>'

def T(*keys):
    return "".join(f'<span class="{"tecla num" if k in list("0123456789.") else "tecla"}">{k}</span>' for k in keys)

def opciones(pid, items):
    btn = "\n".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n{opciones(pid, items)}\n</div>'

def enlace(ancla, titulo, sub):
    return f'''<a class="enlace-interactivo" href="practice-4-1-gcf-lcm.html#{ancla}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def ejemplo(titulo, pasos, resultado):
    p = "".join(f'<p class="paso"><span aria-hidden="true" class="n">{i}</span><strong>Step {i}.</strong> {t}</p>' for i, t in enumerate(pasos, 1))
    return f'<div class="ejemplo">\n<p class="titulo-ej">{titulo}</p>\n{p}\n<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {resultado}</p>\n</div>'

def quiz(q, pregunta, items):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>\n<p class="pregunta" id="t-q{q}">{pregunta}</p>\n<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'

LESSON = {
 "next": "Lesson 4.2", "review": "sections 1 to 5",
 "practice": {
  "p1": {"ok": "c", "hints": {"a": "18 ÷ 3 = 6 with no remainder, so 3 is a factor.", "b": "18 ÷ 6 = 3 with no remainder, so 6 is a factor.", "d": "18 ÷ 9 = 2 with no remainder, so 9 is a factor."},
         "right": "18 ÷ 4 = 4, remainder 2. Since there is a remainder, 4 is not a factor of 18.",
         "solution": "The factor pairs of 18 are 1 × 18, 2 × 9, and 3 × 6. So the factors are 1, 2, 3, 6, 9, and 18. 4 is not on the list: 18 ÷ 4 leaves a remainder of 2."},
  "p2": {"ok": "c", "hints": {"a": "4 and 9 are not prime. Keep breaking them down: 4 = 2 × 2 and 9 = 3 × 3.", "b": "6 is not prime: 6 = 2 × 3.", "d": "6 is not prime. Break each 6 into 2 × 3."},
         "right": "Only prime numbers: 2 × 2 × 3 × 3 = 36 ✓",
         "solution": "36 ÷ 2 = 18, 18 ÷ 2 = 9, 9 ÷ 3 = 3, and 3 is prime. So 36 = 2 × 2 × 3 × 3 = 2² × 3². Check: 4 × 9 = 36 ✓"},
  "p3": {"ok": "b", "hints": {"a": "5 is a common factor, but is there a greater one?", "c": "60 is a common multiple, not a common factor. Factors are not greater than the number.", "d": "2 is a common factor, but is there a greater one?"},
         "right": "Factors of 20: 1, 2, 4, 5, 10, 20. Factors of 30: 1, 2, 3, 5, 6, 10, 15, 30. The greatest common one is 10.",
         "solution": "List the factors. 20: 1, 2, 4, 5, 10, 20. 30: 1, 2, 3, 5, 6, 10, 15, 30. Common: 1, 2, 5, 10. The greatest is 10: GCF(20, 30) = 10."},
  "p4": {"ok": "b", "hints": {"a": "48 is a common multiple (6 × 8), but is there a smaller one?", "c": "2 is a common factor, not a multiple. Multiples are not smaller than the number.", "d": "14 is 6 + 8. Is 14 a multiple of 6?"},
         "right": "Multiples of 8: 8, 16, 24… 24 is also a multiple of 6. LCM(6, 8) = 24.",
         "solution": "Multiples of 6: 6, 12, 18, 24, 30… Multiples of 8: 8, 16, 24, 32… The first one in both lists is 24: LCM(6, 8) = 24."},
  "p5": {"ok": "a", "hints": {"b": "72 is the LCM. Can a piece be longer than the ribbons? This problem cuts into equal pieces: GCF.", "c": "3 inches works, but the pieces should be as long as possible.", "d": "12 does not divide 18 evenly: 6 inches of ribbon would be left over."},
         "right": "Equal pieces, as long as possible, nothing left over: GCF(18, 24) = 6 inches.",
         "solution": "Cutting into equal pieces, as long as possible, with nothing left over, asks for the GCF. Factors of 18: 1, 2, 3, 6, 9, 18. Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. GCF = 6 inches: 3 pieces from the first ribbon and 4 from the second."},
 },
 "quiz": {
  "A": {"ok": "c", "hints": {"a": "15 ÷ 3 = 5 with no remainder, so 3 is also a factor.", "b": "1 and 15 are factors too: 1 × 15 = 15.", "d": "Those are multiples of 15, not factors."},
        "solution": "Factor pairs of 15: 1 × 15 and 3 × 5. The factors are 1, 3, 5, and 15."},
  "B": {"ok": "a", "hints": {"b": "21 = 3 × 7, so it has more than two factors.", "c": "27 = 3 × 9, so it has more than two factors.", "d": "33 = 3 × 11, so it has more than two factors."},
        "solution": "29 has exactly two factors, 1 and 29, so it is prime. 21, 27, and 33 can all be divided by 3."},
  "C": {"ok": "d", "hints": {"a": "4 and 10 are not prime. Keep breaking them down.", "b": "20 is not prime. Keep breaking it down.", "c": "10 is not prime: 10 = 2 × 5."},
        "solution": "40 ÷ 2 = 20, 20 ÷ 2 = 10, 10 ÷ 2 = 5. So 40 = 2 × 2 × 2 × 5 = 2³ × 5. Check: 8 × 5 = 40 ✓"},
  "D": {"ok": "b", "hints": {"a": "4 is a common factor, but 8 also divides both.", "c": "48 is a common multiple, not a factor.", "d": "2 is a common factor, but there is a greater one."},
        "solution": "Factors of 16: 1, 2, 4, 8, 16. Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. The greatest common factor is 8."},
  "E": {"ok": "d", "hints": {"a": "8 is 3 + 5. Is 8 a multiple of 3?", "b": "1 is a factor of every number, not a multiple of 3 and 5.", "c": "30 is a common multiple, but there is a smaller one."},
        "solution": "Multiples of 5: 5, 10, 15… 15 is also a multiple of 3. LCM(3, 5) = 15."},
  "F": {"ok": "c", "hints": {"a": "48 is a common multiple, but there is a smaller one.", "b": "4 is a common factor, not a multiple.", "d": "96 is 8 × 12. Look for a smaller common multiple."},
        "solution": "Multiples of 12: 12, 24, 36… 24 is also a multiple of 8. LCM(8, 12) = 24."},
  "G": {"ok": "b", "hints": {"a": "3/9 can still be simplified. The GCF of 15 and 45 is 15, not 5.", "c": "5/15 can still be simplified. Use the GCF, 15.", "d": "Check: 45 ÷ 15 = 3, not 5."},
        "solution": "GCF(15, 45) = 15. 15 ÷ 15 = 1 and 45 ÷ 15 = 3. So 15/45 = 1/3 in one step."},
  "H": {"ok": "a", "hints": {"b": "54 is 6 × 9, a common multiple, but there is a smaller one.", "c": "3 is a common factor. The lights repeat, so look for a common multiple.", "d": "15 is 6 + 9. Is 15 a multiple of 6?"},
        "solution": "Things that repeat and meet again: LCM. Multiples of 9: 9, 18… 18 is also a multiple of 6. They blink together again in 18 seconds."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 4.1 complement · Factors, multiples, GCF, and LCM (English) — built by tools/build_lesson_4_1_gcf.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 4.1 complement · Factors, multiples, GCF, and LCM · LearnGED</title>
<meta name="robots" content="noindex"/>
<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="../lesson.css">
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="./">Math · Level 1 lessons</a></nav>
<a class="saltar" href="#indice">Skip to the lesson contents</a>
<header class="principal">
<div class="envoltura-header">
<p class="ruta">Math · Level 1 · Topic 4 — Fractions · Complement to Lesson 4.1</p>
<h1>Lesson 4.1 complement · Factors, multiples, GCF, and LCM</h1>
<p class="lema">Two small tools that make a big difference: the greatest common factor to simplify, and the least common multiple to add fractions.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 2 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🧩</span> Gets you ready for fractions</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Tell</strong> the factors of a number apart from its multiples.</li>
<li><strong>Recognize</strong> prime numbers and write a number as a product of primes.</li>
<li><strong>Find</strong> the greatest common factor (GCF) of two numbers in two ways.</li>
<li><strong>Find</strong> the least common multiple (LCM) of two numbers and use it as a common denominator.</li>
<li><strong>Decide</strong> whether a word problem asks for the GCF or the LCM.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-factors">Factors and multiples</a></li>
<li><a href="#s-primes">Prime numbers and prime factorization</a></li>
<li><a href="#s-gcf">The greatest common factor (GCF)</a></li>
<li><a href="#s-lcm">The least common multiple (LCM)</a></li>
<li><a href="#s-which">GCF or LCM? How to decide in a problem</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Why this lesson?</span>
<p>In Lesson 4.1 you simplified fractions by looking for "a number that divides both." When that number is the greatest possible, it has a name: the <strong>greatest common factor</strong>. And in Lesson 4.2, to add fractions with different denominators, you need a <strong>common denominator</strong>: the easiest one is the <strong>least common multiple</strong>.</p>
<p>This lesson explains both ideas from the beginning. The GED® test also asks about them directly ("What is the greatest common factor of 24 and 36?") and inside problems about sharing things and about schedules.</p>
</div>

<section>
<h2 id="s-factors"><span aria-hidden="true" class="num-seccion">1</span>Factors and multiples</h2>
<p>A <strong>factor</strong> (or divisor) of a number is a number that divides it <strong>evenly</strong>, with no remainder. 3 is a factor of 12 because 12 ÷ 3 = 4, with no remainder. 5 is not a factor of 12, because 12 ÷ 5 leaves a remainder of 2.</p>
<p>The best way to find factors is <strong>in pairs</strong>: look for the multiplications that give the number.</p>
{ejemplo("Example: all the factors of 12", ["Try the multiplications that give 12, starting with 1: 1 × 12, 2 × 6, 3 × 4.", "The next number, 4, already showed up in the pair 3 × 4. When the pairs start to repeat, the list is complete."], "The factors of 12 are 1, 2, 3, 4, 6, and 12.")}
<p>A <strong>multiple</strong> of a number is what you get when you multiply it by 1, 2, 3, 4… The multiples of 4 are 4, 8, 12, 16, 20, 24… and the list never ends.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Do not mix them up</span>
<p>A number has <strong>few</strong> factors, and they are never greater than the number (the factors of 12 end at 12). A number has <strong>endless</strong> multiples, and they are never smaller than the number (the multiples of 12 start at 12). Factors: you <strong>divide</strong>. Multiples: you <strong>multiply</strong>.</p>
</div>
<p>These rules save you divisions when you look for factors:</p>
<div aria-label="Divisibility rules (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Divisibility rules for 2, 3, 5, and 10</caption>
<thead><tr><th scope="col">A number can be divided by…</th><th scope="col">if…</th><th scope="col">Example</th></tr></thead>
<tbody>
<tr><th scope="row">2</th><td>it ends in 0, 2, 4, 6, or 8 (it is even).</td><td>38 yes; 27 no.</td></tr>
<tr><th scope="row">3</th><td>the sum of its digits can be divided by 3.</td><td>51: 5 + 1 = 6, yes.</td></tr>
<tr><th scope="row">5</th><td>it ends in 0 or 5.</td><td>45 yes; 52 no.</td></tr>
<tr><th scope="row">10</th><td>it ends in 0.</td><td>70 yes; 75 no.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
{practica("p1", "Practice 1 — Factors", "Which of these numbers is <strong>not</strong> a factor of 18?", [("a", "3"), ("b", "6"), ("c", "4"), ("d", "9")])}
{enlace("factors", "factors and multiples", "List all the factors of a number in pairs, and tell factors from multiples.")}
</section>

<section>
<h2 id="s-primes"><span aria-hidden="true" class="num-seccion">2</span>Prime numbers and prime factorization</h2>
<p>A <strong>prime number</strong> has <strong>exactly two factors</strong>: 1 and itself. The first primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29. A number with more than two factors is called <strong>composite</strong> (12 is composite: it has six factors).</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Two special cases</span>
<p><strong>1 is not prime</strong>: it has only one factor. And <strong>2 is the only even prime</strong>: every other even number can be divided by 2.</p>
</div>
<p>Every composite number can be written as a multiplication of primes. This is called its <strong>prime factorization</strong>, and it is like the number's "fingerprint": each number has only one.</p>
{ejemplo("Example: the prime factorization of 60", ["Divide by the smallest prime that works: 60 ÷ 2 = 30.", "Keep going with the answer: 30 ÷ 2 = 15. 15 is not even, so try 3: 15 ÷ 3 = 5.", "5 is prime, so you are done."], "60 = 2 × 2 × 3 × 5, which you can also write as 2² × 3 × 5.")}
<div class="caja caja-tip">
<span class="etiqueta et-verde">Always check</span>
<p>Multiply the primes you found: 2 × 2 × 3 × 5 = 60. If you do not get the number you started with, one of the divisions has a mistake.</p>
</div>
{practica("p2", "Practice 2 — Prime factorization", "What is the prime factorization of 36?", [("a", "4 × 9"), ("b", "2 × 3 × 6"), ("c", "2 × 2 × 3 × 3"), ("d", "6 × 6")])}
{enlace("primes", "prime numbers and prime factorization", "Decide whether a number is prime or composite, and break numbers into primes with a factor tree.")}
</section>

<section>
<h2 id="s-gcf"><span aria-hidden="true" class="num-seccion">3</span>The greatest common factor (GCF)</h2>
<p>The <strong>greatest common factor (GCF)</strong> of two numbers is the <strong>greatest factor they share</strong>. You can find it in two ways.</p>
<h3>Method 1 · Compare the lists of factors</h3>
{ejemplo("Example: the GCF of 12 and 18", ["Factors of 12: 1, 2, 3, 4, 6, 12.", "Factors of 18: 1, 2, 3, 6, 9, 18.", "Factors in both lists: 1, 2, 3, and 6."], "The greatest of them is 6. GCF(12, 18) = 6.")}
<h3>Method 2 · Use the prime factorization</h3>
<p>With big numbers, the lists get long. With the prime factorization, you take <strong>only the primes they share</strong>, each one with its <strong>smaller exponent</strong>.</p>
{ejemplo("Example: the GCF of 24 and 36", ["24 = 2 × 2 × 2 × 3 = 2³ × 3.", "36 = 2 × 2 × 3 × 3 = 2² × 3².", "Shared primes: 2 (smaller exponent: 2²) and 3 (smaller exponent: 3¹)."], "GCF(24, 36) = 2² × 3 = 4 × 3 = 12.")}
<div class="caja caja-tip">
<span class="etiqueta et-verde">What it is for: simplify in one step</span>
<p>If you divide the numerator and the denominator by their GCF, the fraction is in simplest form right away. To simplify {F(18, 24)}: the GCF of 18 and 24 is 6. 18 ÷ 6 = 3 and 24 ÷ 6 = 4. The answer is {F(3, 4)}.</p>
</div>
{practica("p3", "Practice 3 — Greatest common factor", "What is the greatest common factor of 20 and 30?", [("a", "5"), ("b", "10"), ("c", "60"), ("d", "2")])}
{enlace("gcf", "the greatest common factor", "Find the GCF with lists and with primes, and use it to simplify in one step.")}
</section>

<section>
<h2 id="s-lcm"><span aria-hidden="true" class="num-seccion">4</span>The least common multiple (LCM)</h2>
<p>The <strong>least common multiple (LCM)</strong> of two numbers is the <strong>smallest multiple they share</strong> (not counting zero).</p>
<h3>Method 1 · Compare the lists of multiples</h3>
{ejemplo("Example: the LCM of 4 and 6", ["Multiples of 4: 4, 8, <strong>12</strong>, 16, 20, 24…", "Multiples of 6: 6, <strong>12</strong>, 18, 24…"], "The first number in both lists is 12. LCM(4, 6) = 12.")}
<h3>Method 2 · Use the prime factorization</h3>
<p>Take <strong>every prime that shows up</strong>, shared or not, each one with its <strong>greater exponent</strong>.</p>
{ejemplo("Example: the LCM of 12 and 18", ["12 = 2² × 3 and 18 = 2 × 3².", "Primes that show up: 2 (greater exponent: 2²) and 3 (greater exponent: 3²)."], "LCM(12, 18) = 2² × 3² = 4 × 9 = 36.")}
<div class="caja-calc">
<span class="et-calc"><span aria-hidden="true">🧮</span> A shortcut with the calculator</span>
<p>If you already know the GCF: LCM = (first number × second number) ÷ GCF. For 12 and 18, type {T("(", "1", "2", "×", "1", "8", ")", "÷", "6", "enter")}: the screen shows <strong>36</strong>.</p>
<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>
</div>
<div class="caja caja-tip">
<span class="etiqueta et-verde">What it is for: the common denominator</span>
<p>To add {F(1, 4)} + {F(1, 6)}, the LCM of 4 and 6 is 12, the smallest common denominator: {F(3, 12)} + {F(2, 12)} = {F(5, 12)}. A greater denominator (like 24) also works, but then you have to simplify at the end.</p>
</div>
{practica("p4", "Practice 4 — Least common multiple", "What is the least common multiple of 6 and 8?", [("a", "48"), ("b", "24"), ("c", "2"), ("d", "14")])}
{enlace("lcm", "the least common multiple", "Find the LCM with lists and with primes.")}
</section>

<section>
<h2 id="s-which"><span aria-hidden="true" class="num-seccion">5</span>GCF or LCM? How to decide in a problem</h2>
<p>In word problems, the question does not say "GCF" or "LCM." You have to recognize what it asks for:</p>
<div aria-label="How to tell if a problem asks for the GCF or the LCM (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">How to tell whether a word problem asks for the GCF or the LCM</caption>
<thead><tr><th scope="col">It asks for the…</th><th scope="col">when the problem is about…</th><th scope="col">Words that give it away</th></tr></thead>
<tbody>
<tr><th scope="row">GCF</th><td>sharing or cutting into equal groups, as large as possible, with nothing left over.</td><td>"the greatest number of equal groups," "the longest pieces," "with nothing left over."</td></tr>
<tr><th scope="row">LCM</th><td>things that repeat, and when they happen together again.</td><td>"when will they happen together again?", "at the same time," "every so often."</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: a sharing problem (GCF)</p>
<p><em>"A food pantry has 24 cans of beans and 36 cans of corn. It wants to make identical bags, with the same number of each kind of can and no cans left over. What is the greatest number of bags it can make?"</em></p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> You share into equal groups, as large as possible: the problem asks for the GCF.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> GCF(24, 36) = 12.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> 12 bags, each with 24 ÷ 12 = 2 cans of beans and 36 ÷ 12 = 3 cans of corn.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: a schedule problem (LCM)</p>
<p><em>"One bus stops at the corner every 15 minutes, and another every 20 minutes. At 8:00 they both stop together. When will they stop together again?"</em></p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Things repeat, and you want to know when they meet again: the problem asks for the LCM.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Multiples of 15: 15, 30, 45, <strong>60</strong>. Multiples of 20: 20, 40, <strong>60</strong>. LCM(15, 20) = 60.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> They meet again 60 minutes later, at 9:00.</p>
</div>
{practica("p5", "Practice 5 — GCF or LCM?", "You have two ribbons, one 18 inches long and one 24 inches long. You want to cut them into pieces that are all the same length, as long as possible, with no ribbon left over. How long should each piece be?", [("a", "6 inches"), ("b", "72 inches"), ("c", "3 inches"), ("d", "12 inches")])}
{enlace("which", "GCF or LCM?", "Read real problems and decide whether they ask for the GCF or the LCM, then solve them.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">6</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-4-1-gcf-lcm.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Write the prime factorization of 48, 72, 90, and 100, and check each one by multiplying. Then find the GCF and the LCM of 48 and 72, and of 90 and 100, with both methods. Both methods must give the same answer.</li>
<li><strong>Simplify in one step.</strong> Simplify 24/36, 45/60, and 56/84 by dividing by the GCF in one step.</li>
<li><strong>In your daily life.</strong> Think of two things that repeat every so often (a medicine every 8 hours and a meal every 6 hours, two work shifts, two bus routes). Find how often they happen together, and write it in a sentence.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">7</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "What are all the factors of 15?", [("a", "Only 1 and 15"), ("b", "Only 3 and 5"), ("c", "1, 3, 5, and 15"), ("d", "15, 30, and 45")])}
{quiz("B", "Which of these numbers is <strong>prime</strong>?", [("a", "29"), ("b", "21"), ("c", "27"), ("d", "33")])}
{quiz("C", "What is the prime factorization of 40?", [("a", "4 × 10"), ("b", "2 × 20"), ("c", "2² × 10"), ("d", "2³ × 5")])}
{quiz("D", "What is the greatest common factor of 16 and 24?", [("a", "4"), ("b", "8"), ("c", "48"), ("d", "2")])}
{quiz("E", "What is the least common multiple of 3 and 5?", [("a", "8"), ("b", "1"), ("c", "30"), ("d", "15")])}
{quiz("F", "What is the least common multiple of 8 and 12?", [("a", "48"), ("b", "4"), ("c", "24"), ("d", "96")])}
{quiz("G", f"If you divide the numerator and the denominator of {F(15, 45)} by their GCF, which fraction do you get?", [("a", F(3, 9)), ("b", F(1, 3)), ("c", F(5, 15)), ("d", F(1, 5))])}
{quiz("H", "Two lights blink together now. One blinks every 6 seconds and the other every 9 seconds. In how many seconds will they blink together again?", [("a", "18 seconds"), ("b", "54 seconds"), ("c", "3 seconds"), ("d", "15 seconds")])}
</div>
<p style="text-align:center;margin-top:18px;">
<button class="btn" id="btn-calificar" type="button">Check my answers</button>
<button class="btn btn-sec" id="btn-reintentar" style="display:none;" type="button">Start the quiz again</button>
</p>
<div aria-live="polite" class="marcador" id="marcador" role="status">
<div aria-hidden="true" class="barra-prog"><span id="barra"></span></div>
<p class="puntaje" id="puntaje"></p>
<p class="mensaje" id="mensaje"></p>
</div>
</section>

<section>
<h2 id="s-checklist"><span aria-hidden="true" class="num-seccion">8</span>Self-check checklist</h2>
<p>Use this checklist to see how you are doing. For each skill, choose <strong>Got it</strong>, <strong>Getting there</strong>, or <strong>Needs more practice</strong>. Read it <strong>before</strong> you start the homework. Use it <strong>after</strong> to check your own work honestly.</p>
<div aria-label="Self-check checklist for factors, GCF, and LCM (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: factors, primes, GCF, and LCM, and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Tell factors from multiples</th><td>I list all the factors in pairs and explain how they differ from multiples.</td><td>I list the factors, but sometimes I miss one.</td><td>I mix up factors and multiples.</td></tr>
<tr><th scope="row">Write the prime factorization</th><td>I find the prime factorization and check it by multiplying.</td><td>I find it, sometimes with extra steps.</td><td>I leave composite numbers in it (like 4 × 9).</td></tr>
<tr><th scope="row">Find the GCF and the LCM</th><td>I find them with both methods and use them to simplify and add fractions.</td><td>I find them correctly with one method.</td><td>I switch the GCF and the LCM.</td></tr>
<tr><th scope="row">Choose between GCF and LCM</th><td>I recognize what the problem asks for and explain my choice.</td><td>I choose well in problems like the examples.</td><td>I guess between the two.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You can now find the factors and the multiples of a number, write its prime factorization, and find the <strong>GCF</strong> and the <strong>LCM</strong>. These are exactly the two tools fractions need.</p>
<p>Go back to <a href="lesson-4-1.html#s-simplify">Lesson 4.1 · Simplify a fraction</a> and see that now you can simplify in one step. Then go on to <strong>Lesson 4.2 · Adding and subtracting fractions</strong>, where the LCM becomes the common denominator.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: <a href="lesson-4-2.html">Lesson 4.2 · Adding and subtracting fractions</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>factor (divisor)</dt><dd>A number that divides another number with no remainder. 3 is a factor of 12.</dd>
<dt>multiple</dt><dd>What you get when you multiply a number by 1, 2, 3… The multiples of 4 are 4, 8, 12…</dd>
<dt>prime number</dt><dd>A number with exactly two factors, 1 and itself: 2, 3, 5, 7, 11…</dd>
<dt>composite number</dt><dd>A number with more than two factors, like 12.</dd>
<dt>prime factorization</dt><dd>A number written as a multiplication of primes: 60 = 2² × 3 × 5.</dd>
<dt>greatest common factor (GCF)</dt><dd>The greatest factor two numbers share. GCF(12, 18) = 6.</dd>
<dt>least common multiple (LCM)</dt><dd>The smallest multiple two numbers share. LCM(4, 6) = 12.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 4 · Complement to Lesson 4.1</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-4-1-gcf-lcm.html"), "w", encoding="utf-8").write(html)
print("ok")
