"""Builds math/level-1/lesson-4-1.html (English). Run tools/ged_standards.py afterwards
to add the standards box."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def F(n, d):
    return f'<span class="fracc" aria-hidden="true"><span class="fa">{n}</span><span class="fb2">{d}</span></span><span class="cap-oculto">{n}/{d}</span>'

def T(*keys):
    return "".join(f'<span class="{"tecla num" if k in list("0123456789.") else ("tecla dos" if k == "2nd" else "tecla")}">{k}</span>' for k in keys)

def bar(n, d, label, color="#7b1fa2", width=480):
    """Fraction bar: d equal parts, n of them filled."""
    h, w = 44, width / d
    rects = "".join(f'<rect x="{10 + i * w:.1f}" y="8" width="{w:.1f}" height="{h}" fill="{color if i < n else "#fff"}" stroke="#37474f" stroke-width="2"/>' for i in range(d))
    return f'<svg viewBox="0 0 {width + 20} {h + 16}" role="img" aria-label="{label}" style="width:100%;max-width:{width + 20}px;height:auto;display:block;margin:6px auto;">{rects}</svg>'

def opciones(pid, items):
    btn = "\n".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n{opciones(pid, items)}\n</div>'

def enlace(ancla, titulo, sub, href=None):
    href = href or f"practice-4-1.html#{ancla}"
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def calc(titulo, cuerpo):
    return f'<div class="caja-calc">\n<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>\n{cuerpo}\n<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>\n</div>'

def quiz(q, pregunta, items):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>\n<p class="pregunta" id="t-q{q}">{pregunta}</p>\n<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'

LESSON = {
 "next": "Lesson 4.2", "review": "sections 2, 3, and 4",
 "practice": {
  "p1": {"ok": "b", "hints": {
      "a": "2/3 is twice as much as 1/3. Multiply the top and the bottom by the same number.",
      "c": "Only the bottom changed. Whatever you do to the bottom, do to the top too.",
      "d": "3/6 is one half, which is more than one third. Multiply 1/3 by 3/3."},
   "right": "1 × 3 = 3 and 3 × 3 = 9: you multiplied the top and the bottom by the same number.",
   "solution": "Multiply the top and the bottom of 1/3 by 3: (1 × 3)/(3 × 3) = 3/9. Both fractions are the same amount."},
  "p2": {"ok": "b", "hints": {
      "a": "You divided only the top. Divide the top and the bottom by the same number.",
      "c": "You divided only the bottom. Divide both by 2.",
      "d": "Check: 6 ÷ 2 = 3, not 2."},
   "right": "6 ÷ 2 = 3 and 10 ÷ 2 = 5. 3 and 5 share no factor greater than 1, so 3/5 is the simplest form.",
   "solution": "6 and 10 can both be divided by 2: 6 ÷ 2 = 3 and 10 ÷ 2 = 5. So 6/10 = 3/5, and 3/5 cannot be simplified more."},
  "p3": {"ok": "a",
   "right": "Same denominator: the parts are the same size, and 7 parts are more than 4.",
   "solution": "The denominators are the same (10), so the parts are the same size. 7 parts are more than 4 parts: 7/10 > 4/10."},
  "p4": {"ok": "a",
   "right": "1/2 = 5/10 and 2/5 = 4/10. 5 tenths are more than 4 tenths.",
   "solution": "Use a common denominator, 10: 1/2 = 5/10 and 2/5 = 4/10. Since 5 > 4, 1/2 > 2/5. You can also think: 2/5 is less than half of 5."},
 },
 "quiz": {
  "A": {"ok": "c", "hints": {"a": "5 is on top: that is the numerator.", "b": "13 is 5 + 8. The denominator is one of the two numbers.", "d": "3 is 8 − 5. The denominator is one of the two numbers."},
        "solution": "The denominator is the bottom number: 8. It tells how many equal parts the whole was divided into."},
  "B": {"ok": "b", "hints": {"a": "2/3 is more than one half.", "c": "1/4 is less than one half.", "d": "3/8 is less than one half (4/8 is one half)."},
        "solution": "5/10: multiply 1/2 by 5 on the top and the bottom. Five tenths is one half."},
  "C": {"ok": "d", "hints": {"a": "Adding the same number changes the value: 1/2 is not equal to 2/3.", "b": "If you change only the numerator, the amount changes.", "c": "Subtracting the same number changes the value."},
        "solution": "Multiply or divide the top and the bottom by the same number. That keeps the same amount."},
  "D": {"ok": "a", "hints": {"b": "You divided only the top. Divide both.", "c": "Check: 8 ÷ 4 = 2, but 4 ÷ 4 = 1.", "d": "4/4 is one whole. 4/8 is half."},
        "solution": "Divide the top and the bottom by 4: 4 ÷ 4 = 1 and 8 ÷ 4 = 2. So 4/8 = 1/2."},
  "E": {"ok": "b", "hints": {"a": "9/12 can still be simplified: 9 and 12 can both be divided by 3.", "c": "You divided only the top. Divide both by 3.", "d": "Check: 9 ÷ 3 = 3, not 1."},
        "solution": "9 and 12 can both be divided by 3: 9 ÷ 3 = 3 and 12 ÷ 3 = 4. So 9/12 = 3/4."},
  "F": {"ok": "c", "hints": {"a": "Same denominator: compare the numerators. Which is greater, 5 or 2?", "b": "They have the same denominator but different numerators."},
        "solution": "Same denominator (9), so the parts are the same size: 5 parts are more than 2. 5/9 > 2/9."},
  "G": {"ok": "a", "hints": {"b": "Same numerator: the more parts the whole is divided into, the smaller each part.", "c": "A whole cut into 6 parts has smaller parts than a whole cut into 4."},
        "solution": "Both have 1 part. A whole cut into 6 parts has smaller parts than a whole cut into 4, so 1/6 < 1/4."},
  "H": {"ok": "c", "hints": {"a": "Change 3/4 to eighths: 3/4 = 6/8. Which is more, 6/8 or 5/8?", "b": "Change 3/4 to eighths and compare with 5/8."},
        "solution": "3/4 = 6/8 (multiply by 2). 6/8 is more than 5/8, so more was eaten from the pizza with 3/4 eaten."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 4.1 · Math Level 1 (English) — built by tools/build_lesson_4_1.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 4.1 · Equivalent fractions: simplify and compare · LearnGED</title>
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
<p class="ruta">Math · Level 1 · Topic 4 — Fractions</p>
<h1>Lesson 4.1 · Equivalent fractions: simplify and compare</h1>
<p class="lema">The same amount can be written in many ways. Learn to recognize those ways, simplify them, and compare them.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🍕</span> Fraction bars</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Name</strong> the parts of a fraction: the numerator and the denominator.</li>
<li><strong>Recognize and make</strong> equivalent fractions (fractions with the same value).</li>
<li><strong>Simplify</strong> a fraction to its simplest form.</li>
<li><strong>Compare</strong> two fractions to decide which one is greater.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-what">What is a fraction?</a></li>
<li><a href="#s-equivalent">Equivalent fractions</a></li>
<li><a href="#s-simplify">Simplify a fraction</a></li>
<li><a href="#s-compare">Compare fractions</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-what"><span aria-hidden="true" class="num-seccion">1</span>What is a fraction?</h2>
<p>In <strong>Topic 3</strong> you learned that a decimal is a part of a whole. A <strong>fraction</strong> is another way to write those parts, and many times it is the most natural one: "half an hour," "a quarter pound," "three quarters of a tank of gas."</p>
<p>A fraction has two numbers separated by a bar:</p>
<ul>
<li>The <strong>numerator</strong> (top): how many parts we <strong>have</strong>.</li>
<li>The <strong>denominator</strong> (bottom): how many <strong>equal parts</strong> the whole was divided into.</li>
</ul>
<p>For example, {F(3, 4)} means: the whole was divided into <strong>4</strong> equal parts, and we take <strong>3</strong> of them.</p>
{bar(3, 4, "A bar divided into 4 equal parts, with 3 parts shaded: three fourths.")}
<p style="text-align:center"><strong>Three fourths:</strong> 3 parts shaded out of 4 = {F(3, 4)}</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Connection to Topic 3</span>
<p>Remember from Lesson 3.3: the fraction bar means "divided by." {F(3, 4)} is the same as 3 ÷ 4 = 0.75. Fractions and decimals are two languages for the same idea.</p>
</div>
{enlace("what", "what is a fraction?", "Build fractions with a bar and a number line, and name the numerator and the denominator.")}
</section>

<section>
<h2 id="s-equivalent"><span aria-hidden="true" class="num-seccion">2</span>Equivalent fractions</h2>
<p>Two fractions are <strong>equivalent</strong> when they show <strong>the same amount</strong>, even though they are written with different numbers. Look at these two bars:</p>
{bar(1, 2, "A bar divided into 2 equal parts, with 1 part shaded: one half.")}
<p style="text-align:center">{F(1, 2)} — one half</p>
{bar(2, 4, "A bar of the same size divided into 4 equal parts, with 2 parts shaded: two fourths, also one half.", "#ba68c8")}
<p style="text-align:center">{F(2, 4)} — also one half</p>
<p>The shaded part is <strong>exactly the same size</strong>: {F(1, 2)} and {F(2, 4)} are equivalent fractions.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The golden rule</span>
<p>If you <strong>multiply</strong> (or <strong>divide</strong>) the numerator and the denominator by <strong>the same number</strong>, you get an equivalent fraction. Whatever you do to the top, you do to the bottom.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: make fractions equivalent to {F(2, 3)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Multiply the top and the bottom by 2: {F("2 × 2", "3 × 2")} = {F(4, 6)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Multiply the top and the bottom by 3: {F("2 × 3", "3 × 3")} = {F(6, 9)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(2, 3)} = {F(4, 6)} = {F(6, 9)}. They all have the same value.</p>
</div>
{practica("p1", "Practice 1 — Equivalent fractions", f"Which fraction is equivalent to {F(1, 3)}?", [("a", F(2, 3)), ("b", F(3, 9)), ("c", F(1, 6)), ("d", F(3, 6))])}
{enlace("equivalent", "equivalent fractions", "Multiply the top and the bottom by the same number and compare the bars.")}
</section>

<section>
<h2 id="s-simplify"><span aria-hidden="true" class="num-seccion">3</span>Simplify a fraction</h2>
<p>To <strong>simplify</strong> (or reduce) a fraction means to write it with the smallest numbers possible, without changing its value. You do it by <strong>dividing</strong> the numerator and the denominator by the same number.</p>
<p>A fraction is in its <strong>simplest form</strong> when no number greater than 1 divides both the numerator and the denominator evenly.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: simplify {F(8, 12)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Find a number that divides both 8 and 12. The number 4 works: 8 ÷ 4 = 2, and 12 ÷ 4 = 3.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> You get {F(2, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> Can you keep going? 2 and 3 share no factor greater than 1. It is already in simplest form.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(8, 12)} = {F(2, 3)}.</p>
</div>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Tip</span>
<p>If you do not find the biggest number right away, that is fine. Divide by a small number (like 2) and repeat: {F(8, 12)} → ÷ 2 → {F(4, 6)} → ÷ 2 → {F(2, 3)}. You get the same answer in more steps.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator always shows fractions in simplest form. Use it to check your work:</p>
<ol>
<li>Press {T("n/d")}, type {T("8")}, go down with {T("▼")}, type {T("1", "2")}, and leave with {T("►")}.</li>
<li>Press {T("enter")}. The screen shows {F(2, 3)}.</li>
</ol>
<p>Simplify on paper first. If your answer and the screen do not match, check whether you can still divide.</p>""")}
{practica("p2", "Practice 2 — Simplify", f"What is the simplest form of {F(6, 10)}?", [("a", F(3, 10)), ("b", F(3, 5)), ("c", F(6, 5)), ("d", F(2, 5))])}
{enlace("simplify", "simplify a fraction", "Divide by the same number until you reach the simplest form, step by step or all at once.")}
<a class="enlace-interactivo" href="lesson-4-1-gcf-lcm.html" aria-label="Open the complement: factors, multiples, GCF, and LCM">
<span class="ei-icono" aria-hidden="true">📘</span>
<span class="ei-cuerpo"><span class="ei-titulo">What is the greatest number that divides both?</span><span class="ei-sub">That number is the greatest common factor (GCF). This complement shows you how to find it, so you can simplify in one step. It also teaches the LCM, which you will need in Lesson 4.2.</span><span class="ei-cta">Open the complement <span aria-hidden="true">›</span></span></span>
</a>
</section>

<section>
<h2 id="s-compare"><span aria-hidden="true" class="num-seccion">4</span>Compare fractions</h2>
<p>To decide which of two fractions is greater, there are two cases.</p>
<h3>Case 1: the same denominator</h3>
<p>If the two fractions have <strong>the same denominator</strong>, it is easy: <strong>the greater one has the greater numerator</strong>. The parts are the same size, so more parts means more.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: compare {F(3, 8)} and {F(5, 8)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Same denominator (8): the parts are the same size.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> 5 parts are more than 3 parts: {F(5, 8)} &gt; {F(3, 8)}.</p>
</div>
<h3>Case 2: different denominators</h3>
<p>If the denominators are <strong>different</strong>, first make them the same: find <strong>equivalent fractions with the same denominator</strong>. Then compare the numerators.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: compare {F(2, 3)} and {F(3, 4)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Find a common denominator. 12 works for both 3 and 4.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Change them: {F(2, 3)} = {F(8, 12)} (× 4), and {F(3, 4)} = {F(9, 12)} (× 3).</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> Compare the numerators: 9 is more than 8.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(3, 4)} &gt; {F(2, 3)}.</p>
</div>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out!</span>
<p>A <strong>greater</strong> denominator does not mean a greater fraction. {F(1, 8)} is <strong>less</strong> than {F(1, 2)}: the more parts you cut the whole into, the smaller each part is.</p>
</div>
{bar(1, 2, "A bar divided into 2 equal parts with 1 shaded: one half.", "#1565c0")}
{bar(1, 8, "A bar of the same size divided into 8 equal parts with 1 shaded: one eighth, much smaller than one half.", "#7b1fa2")}
{calc("Another way to check: change to decimals", f"""<p>Fractions and decimals are two languages for the same idea. To compare {F(2, 3)} and {F(3, 4)}, you can change each one to a decimal with {T("÷")}: {T("2", "÷", "3", "enter")} shows <strong>0.666…</strong> and {T("3", "÷", "4", "enter")} shows <strong>0.75</strong>. Since 0.75 is greater, {F(3, 4)} is greater.</p>""")}
{practica("p3", "Practice 3 — Compare (same denominator)", f"Which fraction is greater: {F(7, 10)} or {F(4, 10)}?", [("a", f"{F(7, 10)} is greater"), ("b", f"{F(4, 10)} is greater"), ("c", "They are equal")])}
{practica("p4", "Practice 4 — Compare (different denominators)", f"Which fraction is greater: {F(1, 2)} or {F(2, 5)}?", [("a", f"{F(1, 2)} is greater"), ("b", f"{F(2, 5)} is greater"), ("c", "They are equal")])}
{enlace("compare", "compare fractions", "Decide which is greater with the same denominator, the same numerator, or different denominators, and see the bars.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">5</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-4-1.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Draw two bars of the same length. Divide one into 4 parts and the other into 8. Shade 3/4 of the first one, and find how many eighths you need to shade to reach the same length. Do it again with 1/2 and sixths, and with 2/3 and twelfths. Seeing the bars side by side is what convinces you that two different fractions can be worth the same.</li>
<li><strong>In your kitchen.</strong> Look at your measuring cups and spoons. How many 1/4 cups fill a 1/2 cup? How many teaspoons make a tablespoon? Write each answer as an equation with fractions, for example 2 × 1/4 cup = 1/2 cup.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">6</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. Questions with only two choices show the explanation right away. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", f"In the fraction {F(5, 8)}, which number is the <strong>denominator</strong>?", [("a", "5"), ("b", "13"), ("c", "8"), ("d", "3")])}
{quiz("B", f"Which fraction is equivalent to {F(1, 2)}?", [("a", F(2, 3)), ("b", F(5, 10)), ("c", F(1, 4)), ("d", F(3, 8))])}
{quiz("C", "To get an equivalent fraction, you should:", [("a", "Add the same number to the top and the bottom."), ("b", "Change only the numerator."), ("c", "Subtract the same number from the top and the bottom."), ("d", "Multiply or divide the top and the bottom by the same number.")])}
{quiz("D", f"What is the simplest form of {F(4, 8)}?", [("a", F(1, 2)), ("b", F(2, 8)), ("c", F(2, 3)), ("d", F(4, 4))])}
{quiz("E", f"What is the simplest form of {F(9, 12)}?", [("a", F(9, 12)), ("b", F(3, 4)), ("c", F(3, 12)), ("d", F(1, 3))])}
{quiz("F", f"Which fraction is greater: {F(5, 9)} or {F(2, 9)}?", [("a", F(2, 9)), ("b", "They are equal"), ("c", F(5, 9))])}
{quiz("G", f"Which fraction is <strong>less</strong>: {F(1, 4)} or {F(1, 6)}?", [("a", F(1, 6)), ("b", F(1, 4)), ("c", "They are equal")])}
{quiz("H", f"Two pizzas are the same size. {F(3, 4)} of one pizza was eaten, and {F(5, 8)} of the other. From which pizza was more eaten?", [("a", f"The one with {F(5, 8)} eaten"), ("b", "The same amount from both"), ("c", f"The one with {F(3, 4)} eaten")])}
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
<h2 id="s-checklist"><span aria-hidden="true" class="num-seccion">7</span>Self-check checklist</h2>
<p>Use this checklist to see how you are doing. For each skill, choose <strong>Got it</strong>, <strong>Getting there</strong>, or <strong>Needs more practice</strong>. Read it <strong>before</strong> you start the homework. Use it <strong>after</strong> to check your own work honestly.</p>
<div aria-label="Self-check checklist for equivalent fractions (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: fraction skills and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Name the numerator and the denominator</th><td>I name them and explain what each one tells.</td><td>I name them correctly.</td><td>I mix up their roles, or I cannot tell them apart.</td></tr>
<tr><th scope="row">Make equivalent fractions</th><td>I multiply or divide the top and the bottom with no mistakes.</td><td>I make equivalent fractions correctly most of the time.</td><td>I change only one number of the fraction.</td></tr>
<tr><th scope="row">Simplify fractions</th><td>I always reach the simplest form.</td><td>I simplify, sometimes in several steps, but I do not always finish.</td><td>I do not simplify.</td></tr>
<tr><th scope="row">Compare two fractions</th><td>I compare with the same and with different denominators, and I can explain why.</td><td>I compare well when the denominators are the same.</td><td>I go by the size of the numbers without making the denominators the same.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You now know what a fraction is, and you can make equivalent fractions, simplify, and compare. That is exactly the foundation you need to <strong>calculate</strong> with fractions.</p>
<p>In <strong>Lesson 4.2 · Adding and subtracting fractions</strong> you will add and subtract fractions, and you will see why you first need <strong>the same denominator</strong>. The equivalent fractions you practiced today will be your main tool.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: Lesson 4.2 · Adding and subtracting fractions</p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>fraction</dt><dd>A number that shows parts of a whole, like 3/4.</dd>
<dt>numerator</dt><dd>The top number of a fraction: how many parts you have.</dd>
<dt>denominator</dt><dd>The bottom number of a fraction: how many equal parts the whole was divided into.</dd>
<dt>equivalent fractions</dt><dd>Fractions with the same value, like 1/2, 2/4, and 5/10.</dd>
<dt>simplify (reduce)</dt><dd>To divide the top and the bottom by the same number to write the fraction with smaller numbers.</dd>
<dt>simplest form</dt><dd>A fraction whose top and bottom share no factor greater than 1, like 2/3.</dd>
<dt>common denominator</dt><dd>The same denominator for two or more fractions, so you can compare, add, or subtract them.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.1</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-4-1.html"), "w", encoding="utf-8").write(html)
print("ok")
