"""Builds math/level-1/lesson-3-3.html (English). Fractions are written with F(n, d):
stacked on screen, read as "n/d" by screen readers."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def F(n, d):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{n}</span><span class="fb2">{d}</span></span><span class="cap-oculto">{n}/{d}</span>'

def T(*keys):
    out = []
    for k in keys:
        cls = "tecla num" if k in list("0123456789.") else ("tecla dos" if k == "2nd" else "tecla")
        out.append(f'<span class="{cls}">{k}</span>')
    return "".join(out)

def opciones(pid, items, quiz=False):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    if quiz:
        return btn
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'''<div class="practica">
<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>
<p class="pregunta-int" id="t-{pid}">{pregunta}</p>
{opciones(pid, items)}
</div>'''

def enlace(ancla, titulo, sub):
    return f'''<a class="enlace-interactivo" href="practice-3-3.html#{ancla}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo.lower()} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def calc(titulo, cuerpo):
    return f'''<div class="caja-calc">
<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>
{cuerpo}
<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>
</div>'''

def quiz(q, pregunta, items):
    return f'''<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>
<p class="pregunta" id="t-q{q}">{pregunta}</p>
<div aria-labelledby="t-q{q}" class="opciones" role="group">
{opciones(None, items, True)}
</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'''

LESSON = {
 "next": "Lesson 4.1",
 "review": "sections 2, 3, 4, and 5",
 "practice": {
  "p1": {"ok": "b", "hints": {
      "a": "0.5 is one half. Divide 1 ÷ 5: the answer is less than one half.",
      "c": "The fraction is not read by putting the digits together. Divide 1 ÷ 5.",
      "d": "1.5 is more than 1, but 1/5 is less than 1. Divide 1 ÷ 5."},
   "right": "1 ÷ 5 = 0.2. Check: 0.2 × 5 = 1 ✓",
   "solution": "The bar means divided by: 1 ÷ 5. Since 1 is less than 5, write 1.0: 10 ÷ 5 = 2. So 1/5 = 0.2."},
  "p2": {"ok": "b", "hints": {
      "a": "1/2 is 0.5 (fifty hundredths), not 0.25.",
      "c": "2/5 is 0.4. Read 0.25 as twenty-five hundredths: 25/100.",
      "d": "3/4 is 0.75. Read 0.25 as twenty-five hundredths: 25/100."},
   "right": "0.25 = 25/100, and 25/100 simplifies to 1/4 (divide both by 25).",
   "solution": "0.25 is twenty-five hundredths: 25/100. Divide the top and the bottom by 25: 1/4. It is like 25 cents: one quarter of a dollar."},
  "p3": {"ok": "b", "hints": {
      "a": "Line up the points: 1.80 + 2.35.",
      "c": "Check the tenths: 8 + 3 = 11, so you carry 1 to the ones.",
      "d": "That is close to a subtraction. The question asks for the total: add."},
   "right": "1.80 + 2.35 = 4.15 miles.",
   "solution": "Total means add. Write 1.8 as 1.80 and line up the points: 1.80 + 2.35 = 4.15. The person walked 4.15 miles."},
  "p4": {"ok": "b", "hints": {
      "a": "6 gallons at $3.40 each are equal groups: multiply, do not add.",
      "c": "Check: 6 × 3 = 18 and 6 × 0.40 = 2.40.",
      "d": "Count the decimal places: 3.40 has 2, so 6 × 340 = 2040 becomes 20.40."},
   "right": "3.40 × 6 = 20.40. Estimate: about 3 × 6 = 18 ✓",
   "solution": "6 equal groups of $3.40: multiply. 340 × 6 = 2,040. With 2 decimal places: $20.40. Estimate: about $3 × 6 = $18, close ✓"},
 },
 "quiz": {
  "A": {"ok": "c", "hints": {"a": "Think of 3/4 as sharing 3 among 4.", "b": "The bar is not addition.", "d": "The bar is not subtraction."},
        "solution": "The fraction bar means \"divided by.\" 3/4 means 3 ÷ 4."},
  "B": {"ok": "a", "hints": {"b": "The fraction is not read by putting the digits together. Divide 3 ÷ 4.", "c": "0.5 is 1/2. 3/4 is more than one half.", "d": "Divide 3 ÷ 4: 30 ÷ 4 = 7, remainder 2, then 20 ÷ 4 = 5."},
        "solution": "3 ÷ 4: write 3.00. 30 ÷ 4 = 7, remainder 2; 20 ÷ 4 = 5. So 3/4 = 0.75, like 75 cents."},
  "C": {"ok": "b", "hints": {"a": "The fraction is not read by putting the digits together. Divide 1 ÷ 2.", "c": "0.25 is 1/4. One half is more.", "d": "1.2 is more than 1, but 1/2 is less than 1."},
        "solution": "1 ÷ 2 = 0.5. Half a dollar is $0.50."},
  "D": {"ok": "d", "hints": {"a": "7/100 is 0.07. The 7 in 0.7 is in the tenths.", "b": "1/7 is about 0.14.", "c": "7/1000 is 0.007, with three decimal places."},
        "solution": "0.7 is seven tenths. The last place is the tenths, so the denominator is 10: 7/10."},
  "E": {"ok": "c", "hints": {"a": "An exact (terminating) decimal ends. 0.333… never ends.", "b": "0.333… is not a whole number.", "d": "0.333… is more than 0, so it is not negative."},
        "solution": "The 3s repeat and never end, so 0.333… is a repeating decimal. In daily life we round it: 1/3 ≈ 0.33."},
  "F": {"ok": "b", "hints": {"a": "Write 2.6 as 2.60 and subtract: 2.60 − 0.85.", "c": "You used some of the flour, so there is less left: subtract.", "d": "Check the borrowing: 2.60 − 0.85."},
        "solution": "Used means subtract. 2.60 − 0.85 = 1.75. There are 1.75 pounds of flour left."},
  "G": {"ok": "d", "hints": {"a": "4 kilos at $1.25 each are equal groups: multiply, do not add.", "b": "Check: 4 × 1 = 4 and 4 × 0.25 = 1.", "c": "Do not forget the 25 cents: 4 × 0.25 = 1."},
        "solution": "1.25 × 4 = 5.00. Shortcut: 4 × $1 = $4 and 4 × 25 cents = $1, so $5.00."},
  "H": {"ok": "a", "hints": {"b": "Check the total first: 6.80 + 5.45 = 12.25.", "c": "Check the hundredths: 15.00 − 12.25.", "d": "That is the total you spent. The question asks for the change."},
        "solution": "Two steps. First the total: 6.80 + 5.45 = 12.25. Then the change: 15.00 − 12.25 = 2.75. Your change is $2.75."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 3.3 · Math Level 1 (English) — built by tools/build_lesson_3_3.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 3.3 · Decimals in context and equivalent forms · LearnGED</title>
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
<p class="ruta">Math · Level 1 · Topic 3 — Decimals</p>
<h1>Lesson 3.3 · Decimals in context and equivalent forms</h1>
<p class="lema">Change fractions to decimals and decimals to fractions, and solve real problems about shopping, distances, and measurements.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🔄</span> Fraction ↔ decimal</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Change</strong> a common fraction to a decimal by dividing the numerator by the denominator.</li>
<li><strong>Change</strong> a decimal to a fraction and simplify it.</li>
<li><strong>Recognize</strong> the most common fraction–decimal pairs.</li>
<li><strong>Solve</strong> real problems with decimals: shopping, distances, measurements, and change.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-two-ways">Two ways to write the same thing</a></li>
<li><a href="#s-fraction-to-decimal">From fraction to decimal: divide</a></li>
<li><a href="#s-decimal-to-fraction">From decimal to fraction: read and simplify</a></li>
<li><a href="#s-memorize">Pairs worth knowing by heart</a></li>
<li><a href="#s-real-life">Decimals in real-life problems</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-two-ways"><span aria-hidden="true" class="num-seccion">1</span>Two ways to write the same thing</h2>
<p>In Lesson 3.1 you saw that a decimal is a <strong>part of a whole</strong>. A fraction is a part of a whole too. In fact, they are <strong>two ways to write the same value</strong>.</p>
<p>Think about money: half a dollar can be written as the fraction {F(1, 2)} of a dollar, or as the decimal <strong>$0.50</strong>. It is the same amount of money. Only the way you write it changes.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Key idea</span>
<p>The bar in a fraction means <strong>"divided by."</strong> The fraction {F(3, 4)} means, exactly, <strong>3 ÷ 4</strong>. That is the key to changing any fraction to a decimal.</p>
</div>
</section>

<section>
<h2 id="s-fraction-to-decimal"><span aria-hidden="true" class="num-seccion">2</span>From fraction to decimal: divide</h2>
<p>To change a fraction to a decimal, <strong>divide the numerator (top) by the denominator (bottom)</strong>. Use the division with decimals you learned in Lesson 3.2: if the numerator is smaller, write a point and zeros after it.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: change {F(3, 4)} to a decimal</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Set up the division: 3 ÷ 4. Since 3 is less than 4, write 3 as <strong>3.00</strong> and put the point in the answer.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Divide: 30 ÷ 4 = 7, remainder 2. Bring down the next zero: 20 ÷ 4 = 5, with no remainder.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(3, 4)} = <strong>0.75</strong>, just like 75 cents.</p>
</div>
{calc("Check it on the calculator", f"""<p>Solve on paper first. Then clear the memory ({T("2nd", "sto→")} and {T("1")}) and check in two ways:</p>
<ol>
<li><strong>As a division:</strong> type {T("3", "÷", "4", "enter")}. The screen shows <strong>0.75</strong>.</li>
<li><strong>As a fraction:</strong> press {T("n/d")}, type {T("3")}, go down with {T("▼")}, type {T("4")}, leave with {T("►")}, and press {T("enter")}. The screen shows {F(3, 4)}. Now press {T("⟷")}: it changes to <strong>0.75</strong>.</li>
</ol>
<p>The calculator confirms; the paper teaches you.</p>""")}
{practica("p1", "Practice 1 — Fraction to decimal", f"Which decimal is equal to the fraction {F(1, 5)}?", [("a", "0.5"), ("b", "0.2"), ("c", "0.15"), ("d", "1.5")])}
{enlace("fraction-to-decimal", "from fraction to decimal", "Divide the numerator by the denominator and watch the decimal appear, step by step.")}
</section>

<section>
<h2 id="s-decimal-to-fraction"><span aria-hidden="true" class="num-seccion">3</span>From decimal to fraction: read and simplify</h2>
<p>To change a decimal to a fraction, use what you learned in Lesson 3.1: <strong>the name of the last place gives you the denominator</strong>.</p>
<ul>
<li>If the decimal ends in the <strong>tenths</strong> → the denominator is <strong>10</strong>.</li>
<li>If it ends in the <strong>hundredths</strong> → the denominator is <strong>100</strong>.</li>
<li>If it ends in the <strong>thousandths</strong> → the denominator is <strong>1,000</strong>.</li>
</ul>
<div class="ejemplo">
<p class="titulo-ej">Example: change 0.6 to a fraction</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> 0.6 is "six tenths." The numerator is 6 and the denominator is 10: {F(6, 10)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Simplify: 6 and 10 can both be divided by 2. 6 ÷ 2 = 3, and 10 ÷ 2 = 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> 0.6 = {F(3, 5)}.</p>
</div>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out!</span>
<p>A fraction is <strong>simplified</strong> when the numerator and the denominator cannot both be divided by the same number anymore. You will study simplifying in depth in Topic 4. For now, it is enough to simplify the easy ones.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator can change a decimal to a fraction with the green function <strong>f◂▸d</strong> (above the {T("table")} key):</p>
<ol>
<li>Type {T("0", ".", "6")}.</li>
<li>Press {T("2nd")} and then {T("table")} (f◂▸d).</li>
<li>Press {T("enter")}. The screen shows {F(3, 5)}, already simplified.</li>
</ol>""")}
{enlace("decimal-to-fraction", "from decimal to fraction", "Read the last place, write the denominator, and simplify.")}
</section>

<section>
<h2 id="s-memorize"><span aria-hidden="true" class="num-seccion">4</span>Pairs worth knowing by heart</h2>
<p>Some fraction–decimal pairs show up so often, in prices, recipes, and measurements, that it pays to <strong>know them by heart</strong>. Here is your reference table:</p>
<div aria-label="Common fraction and decimal pairs (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Common fractions, their decimals, and where you see them</caption>
<thead><tr><th scope="col">Fraction</th><th scope="col">Decimal</th><th scope="col">Where you see it</th></tr></thead>
<tbody>
<tr><th scope="row">1/2</th><td>0.5</td><td>half a dollar, half an hour</td></tr>
<tr><th scope="row">1/4</th><td>0.25</td><td>a quarter, 25 cents, a quarter of an hour</td></tr>
<tr><th scope="row">3/4</th><td>0.75</td><td>three quarters, 75 cents</td></tr>
<tr><th scope="row">1/5</th><td>0.2</td><td>one fifth</td></tr>
<tr><th scope="row">1/10</th><td>0.1</td><td>one tenth, a dime</td></tr>
<tr><th scope="row">1/3</th><td>≈ 0.33</td><td>one third (a repeating decimal)</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">A special case: 1/3</span>
<p>When you divide 1 ÷ 3, the answer is 0.3333… and the 3s never end. This is a <strong>repeating decimal</strong>. In daily life we round it to 0.33. You will see repeating decimals in more detail in later levels.</p>
</div>
{practica("p2", "Practice 2 — Decimal to fraction", "The decimal <strong>0.25</strong> is equal to which fraction?", [("a", F(1, 2)), ("b", F(1, 4)), ("c", F(2, 5)), ("d", F(3, 4))])}
{enlace("memorize", "pairs worth knowing by heart", "Practice with flash cards: the most common fractions and their decimals.")}
</section>

<section>
<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Decimals in real-life problems</h2>
<p>Decimals are everywhere: shopping, distances, measurements, and change. Always use the 4-step method from Lesson 1.3: read and underline, choose the operation, solve, and check that the answer makes sense.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: a trip to the grocery store</p>
<p><em>"You buy bread for $2.50, milk for $3.75, and eggs for $4.20. If you pay with $20, how much change do you get?"</em></p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Underline:</strong> prices $2.50, $3.75, $4.20; you pay $20; the question asks for the change.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Choose:</strong> first add the prices (put together), then subtract from what you paid (change). It takes two steps.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve:</strong> 2.50 + 3.75 + 4.20 = 10.45. Then 20.00 − 10.45 = 9.55.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Does it make sense?</strong> The change ($9.55) is less than what you paid ($20). The answer is <strong>$9.55</strong>.</p>
</div>
{calc("Check it on the calculator", f"""<p>Check each step: {T("2", ".", "5", "+", "3", ".", "7", "5", "+", "4", ".", "2", "enter")} shows <strong>10.45</strong>. Then {T("2", "0", "−", "1", "0", ".", "4", "5", "enter")} shows <strong>9.55</strong>.</p>
<p>Tip: right after the first answer, you can press {T("−")} and the calculator writes <strong>ans</strong> (the last answer). For the change, though, you need 20 − 10.45, so type the whole subtraction.</p>""")}
{practica("p3", "Practice 3 — A problem in context", "A person walks <strong>1.8 miles</strong> in the morning and <strong>2.35 miles</strong> in the afternoon. How many miles did the person walk in all?", [("a", "3.53 miles"), ("b", "4.15 miles"), ("c", "4.05 miles"), ("d", "2.53 miles")])}
{practica("p4", "Practice 4 — A problem in context", "A gallon of gas costs <strong>$3.40</strong>. How much do <strong>6 gallons</strong> cost?", [("a", "$9.40"), ("b", "$20.40"), ("c", "$18.40"), ("d", "$2.04")])}
{enlace("real-life", "decimals in real life", "Solve shopping, change, and measurement problems with the 4 steps.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">6</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open. With it, you finish Topic 3.</p>
<ul class="lista-tarea">
<li><strong>ThatQuiz.</strong> Go to <a href="https://www.thatquiz.org/" rel="noopener noreferrer" target="_blank">ThatQuiz</a> and practice changing fractions to decimals and decimals to fractions. You will use this skill a lot later, with percents.</li>
<li><strong>Paper and pencil.</strong> Write the table of pairs from memory (1/2, 1/4, 3/4, 1/5, 1/10, 1/3). Then check each one by dividing, on paper and with the calculator. Do it again the next day without looking.</li>
<li><strong>In your daily life.</strong> Find a real price in an online store and write it as a fraction of a dollar. Then look at a recipe: write the measures that come as fractions (1/2 cup, 3/4 tablespoon) as decimals.</li>
</ul>
<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">7</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. Work on paper. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "The bar in a fraction means:", [("a", '"times"'), ("b", '"plus"'), ("c", '"divided by"'), ("d", '"minus"')])}
{quiz("B", f"Which decimal is equal to {F(3, 4)}?", [("a", "0.75"), ("b", "0.34"), ("c", "0.5"), ("d", "0.7")])}
{quiz("C", f"Which decimal is equal to {F(1, 2)}?", [("a", "0.12"), ("b", "0.5"), ("c", "0.25"), ("d", "1.2")])}
{quiz("D", "The decimal <strong>0.7</strong> is equal to which fraction?", [("a", F(7, 100)), ("b", F(1, 7)), ("c", F(7, 1000)), ("d", F(7, 10))])}
{quiz("E", "When you divide 1 ÷ 3, the answer 0.333… is called a ___ decimal.", [("a", "terminating (exact)"), ("b", "whole"), ("c", "repeating"), ("d", "negative")])}
{quiz("F", "A bag has 2.6 pounds of flour. You use 0.85 pounds for a recipe. How many pounds of flour are left?", [("a", "1.85 lb"), ("b", "1.75 lb"), ("c", "3.45 lb"), ("d", "2.25 lb")])}
{quiz("G", "A pound of rice costs $1.25. How much do 4 pounds cost?", [("a", "$4.25"), ("b", "$5.25"), ("c", "$4.00"), ("d", "$5.00")])}
{quiz("H", "You buy items for $6.80 and $5.45, and you pay with $15. How much change do you get?", [("a", "$2.75"), ("b", "$3.75"), ("c", "$2.65"), ("d", "$12.25")])}
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
<div aria-label="Self-check checklist for fractions, decimals, and problems (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: changing between fractions and decimals and solving problems, and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Change a fraction to a decimal</th><td>I divide the numerator by the denominator with no mistakes.</td><td>I set up the division, but sometimes I make a mistake dividing.</td><td>I do not connect the fraction with a division.</td></tr>
<tr><th scope="row">Change a decimal to a fraction</th><td>I find the denominator from the last place, and I simplify.</td><td>I write the right fraction, but I do not simplify it.</td><td>I mix up the denominators (10, 100, 1,000).</td></tr>
<tr><th scope="row">Know the common pairs</th><td>I know 1/2, 1/4, 3/4, 1/5, and 1/10 by heart.</td><td>I know most of the pairs.</td><td>I know only 1/2 and 1/4, or none.</td></tr>
<tr><th scope="row">Solve problems in context</th><td>I solve with the right answer, the unit, and a check.</td><td>I solve correctly and write the unit.</td><td>I set up the problem but make calculation mistakes, or I do not understand it.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>With this lesson you finish <strong>Topic 3 · Decimals</strong>. You can now read, compare, round, and calculate with decimals, change them to fractions, and solve real problems with them.</p>
<p>In <strong>Topic 4 · Fractions</strong> you will study the other way to write parts of a whole. <strong>Lesson 4.1 · Equivalent fractions: simplify and compare</strong> will show you how the same amount can be written with many different fractions, and how to find the simplest one. You already got a first look at that idea of "simplifying" in this lesson.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: <a href="lesson-4-1.html">Topic 4 · Lesson 4.1 · Equivalent fractions: simplify and compare</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>numerator, denominator</dt><dd>The top and the bottom numbers of a fraction. In 3/4, the numerator is 3 and the denominator is 4.</dd>
<dt>equivalent</dt><dd>Equal in value, even if written in a different way. 1/2 and 0.5 are equivalent.</dd>
<dt>simplify a fraction</dt><dd>To divide the numerator and the denominator by the same number until you cannot do it anymore. 6/10 simplifies to 3/5.</dd>
<dt>terminating decimal</dt><dd>A decimal that ends, like 0.75.</dd>
<dt>repeating decimal</dt><dd>A decimal with digits that repeat forever, like 0.333… (1/3).</dd>
<dt>change (money)</dt><dd>The money you get back when you pay more than the price.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 3 · Lesson 3.3</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-3-3.html"), "w", encoding="utf-8").write(html)
print("ok")
