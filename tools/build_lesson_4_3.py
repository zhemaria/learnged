"""Builds math/level-1/lesson-4-3.html (English). Run tools/ged_standards.py afterwards
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
    href = href or f"practice-4-3.html#{ancla}"
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def calc(titulo, cuerpo):
    return f'<div class="caja-calc">\n<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>\n{cuerpo}\n<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>\n</div>'

def quiz(q, pregunta, items):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>\n<p class="pregunta" id="t-q{q}">{pregunta}</p>\n<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'

def bar2(a, b, d, label, ca="#7b1fa2", cb="#ce93d8", width=480):
    """Fraction bar with two shaded groups: a parts in one color, then b parts in another."""
    h, w = 44, width / d
    def col(i):
        return ca if i < a else (cb if i < a + b else "#fff")
    rects = "".join(f'<rect x="{10 + i * w:.1f}" y="8" width="{w:.1f}" height="{h}" fill="{col(i)}" stroke="#37474f" stroke-width="2"/>' for i in range(d))
    return f'<svg viewBox="0 0 {width + 20} {h + 16}" role="img" aria-label="{label}" style="width:100%;max-width:{width + 20}px;height:auto;display:block;margin:6px auto;">{rects}</svg>'

def area(a, b, c, d, label, size=300):
    """Area model for a/b × c/d: b vertical strips (a shaded), d horizontal strips (c shaded); overlap darker."""
    W = H = size; cw, rh = W / b, H / d; out = []
    for i in range(b):
        for j in range(d):
            col_in, row_in = i < a, j < c
            fill = "#4a148c" if col_in and row_in else ("#ce93d8" if col_in else ("#90caf9" if row_in else "#fff"))
            out.append(f'<rect x="{10 + i * cw:.1f}" y="{10 + j * rh:.1f}" width="{cw:.1f}" height="{rh:.1f}" fill="{fill}" stroke="#ffffff" stroke-width="1.5"/>')
    out.append(f'<rect x="10" y="10" width="{W}" height="{H}" fill="none" stroke="#37474f" stroke-width="3"/>')
    return f'<svg viewBox="0 0 {W + 20} {H + 20}" role="img" aria-label="{label}" style="width:100%;max-width:{W + 20}px;height:auto;display:block;margin:6px auto;">{"".join(out)}</svg>'

LESSON = {
 "next": "Lesson 4.4", "review": "sections 2, 3, 4, and 5",
 "practice": {
  "p1": {"ok": "b", "hints": {
      "a": "You flipped the first fraction. To multiply, you do not flip anything: top × top, bottom × bottom.",
      "c": "3/4 is only the second fraction. Multiply the bottoms too: 2 × 4 = 8.",
      "d": "You added the tops and the bottoms. This problem asks you to multiply."},
   "right": "1 × 3 = 3 on top and 2 × 4 = 8 on the bottom. Half of 3/4 is 3/8.",
   "solution": "Multiply straight across: 1 × 3 = 3 on top, 2 × 4 = 8 on the bottom. So 1/2 × 3/4 = 3/8."},
  "p2": {"ok": "a", "hints": {
      "b": "You added the tops and the bottoms. The word \"of\" means multiply.",
      "c": "5/6 is 1/3 + 1/2. The word \"of\" means multiply, not add.",
      "d": "One third of a half must be less than a half. Multiply: 1 × 1 on top, 3 × 2 on the bottom."},
   "right": "1/3 of 1/2 means 1/3 × 1/2 = 1/6. A third of a half is a small piece.",
   "solution": "\"Of\" means multiply: 1/3 × 1/2 = (1 × 1)/(3 × 2) = 1/6."},
  "p3": {"ok": "b", "hints": {
      "a": "That is the same fraction. The reciprocal is the fraction flipped upside down.",
      "c": "7/7 is 1 whole. Flip the fraction: the 5 goes to the bottom and the 7 goes to the top.",
      "d": "Flip the fraction: the 5 goes to the bottom and the 7 goes to the top."},
   "right": "Flipped: the 7 goes on top and the 5 on the bottom. And 5/7 × 7/5 = 35/35 = 1.",
   "solution": "Flip the fraction: the numerator 5 goes to the bottom and the denominator 7 goes to the top. The reciprocal of 5/7 is 7/5."},
  "p4": {"ok": "b", "hints": {
      "a": "You multiplied without flipping. To divide, flip the second fraction: 1/4 becomes 4/1.",
      "c": "Keep the first fraction, change ÷ to ×, and flip the second: 1/2 × 4/1.",
      "d": "You added. Keep the first fraction, change ÷ to ×, and flip the second."},
   "right": "1/2 × 4/1 = 4/2 = 2. Two quarters fit in a half.",
   "solution": "Keep 1/2, change ÷ to ×, and flip 1/4 to 4/1: 1/2 × 4/1 = 4/2 = 2. Check: two quarters make a half."},
  "p5": {"ok": "b", "hints": {
      "a": "3 is half of 6. But you are not taking half of the board: you are counting how many half-foot pieces fit in it.",
      "c": "Each piece is only half a foot, so you get more pieces than feet.",
      "d": "The question asks how many pieces. The answer must be a whole number of pieces."},
   "right": "6 ÷ 1/2 = 6 × 2 = 12. Each foot gives 2 pieces, and there are 6 feet.",
   "solution": "\"How many pieces fit\" means divide: 6 ÷ 1/2 = 6 × 2/1 = 12 pieces. Each foot gives 2 half-foot pieces, and 6 × 2 = 12."},
 },
 "quiz": {
  "A": {"ok": "c", "hints": {"a": "A common denominator is for adding and subtracting, not for multiplying.", "b": "Flipping is for dividing, and only the second fraction.", "d": "Adding numerators is for adding fractions with the same denominator."},
        "solution": "Multiply straight across: numerator × numerator on top, and denominator × denominator on the bottom. Then simplify."},
  "B": {"ok": "a", "hints": {"b": "You added the tops and the bottoms. Multiply them instead.", "c": "You flipped the second fraction. That is for dividing.", "d": "Multiply the bottoms: 3 × 4 = 12."},
        "solution": "2 × 1 = 2 on top and 3 × 4 = 12 on the bottom: 2/12, which simplifies to 1/6."},
  "C": {"ok": "d", "hints": {"a": "Half of a third must be less than a third. \"Of\" means multiply.", "b": "5/6 is 1/2 + 1/3. \"Of\" means multiply, not add.", "c": "3/2 is more than 1. Half of a third is a small piece."},
        "solution": "\"Of\" means multiply: 1/2 × 1/3 = (1 × 1)/(2 × 3) = 1/6."},
  "D": {"ok": "b", "hints": {"a": "That is the same fraction. Flip it.", "c": "Flip the whole fraction: the 2 goes to the bottom and the 9 to the top.", "d": "9/9 is 1. Flip the fraction: the 2 goes to the bottom and the 9 to the top."},
        "solution": "Flip the fraction: the reciprocal of 2/9 is 9/2."},
  "E": {"ok": "d", "hints": {"a": "The first fraction stays the same, and you multiply, not add.", "b": "Only the second fraction is flipped.", "c": "A common denominator is for adding and subtracting."},
        "solution": "Keep the first fraction, change ÷ to ×, and flip the second fraction. Then multiply."},
  "F": {"ok": "b", "hints": {"a": "You multiplied without flipping. Flip the second fraction: 1/2 becomes 2/1.", "c": "Keep 3/5, change ÷ to ×, and flip 1/2 to 2/1.", "d": "You flipped the first fraction. Only the second one is flipped."},
        "solution": "3/5 × 2/1 = 6/5 (which is 1 1/5). How many halves fit in 3/5? A little more than one."},
  "G": {"ok": "c", "hints": {"a": "That is the full recipe. Half the recipe needs less oil.", "b": "4/3 is double the oil. Half the recipe needs less.", "d": "1/6 is half of 1/3. Find half of 2/3: 1/2 × 2/3."},
        "solution": "Half of 2/3 cup: 1/2 × 2/3 = 2/6 = 1/3 cup."},
  "H": {"ok": "a", "hints": {"b": "Each piece is only 1/4 yard, so you get many pieces.", "c": "Each yard gives 4 pieces, and there are 4 yards.", "d": "Each yard gives 4 pieces. How many pieces in 4 yards?"},
        "solution": "4 ÷ 1/4 = 4 × 4 = 16 pieces. Each yard gives 4 pieces, and 4 × 4 = 16."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 4.3 · Math Level 1 (English) — built by tools/build_lesson_4_3.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 4.3 · Multiplying and dividing fractions · LearnGED</title>
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
<h1>Lesson 4.3 · Multiplying and dividing fractions</h1>
<p class="lema">The good news: multiplying and dividing fractions is simpler than adding them. With this lesson, you complete the four operations with fractions.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🔄</span> Multiply and divide</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Multiply</strong> fractions: numerator times numerator and denominator times denominator.</li>
<li><strong>Find</strong> the reciprocal of a fraction (the fraction flipped upside down).</li>
<li><strong>Divide</strong> fractions by multiplying by the reciprocal of the second one.</li>
<li><strong>Solve</strong> real-life problems with fractions, and simplify the answer.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-surprise">A pleasant surprise</a></li>
<li><a href="#s-multiply">Multiply fractions: straight across</a></li>
<li><a href="#s-reciprocal">The reciprocal: the flipped fraction</a></li>
<li><a href="#s-divide">Divide fractions: keep, change, flip</a></li>
<li><a href="#s-real-life">Fractions in real-life problems</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-surprise"><span aria-hidden="true" class="num-seccion">1</span>A pleasant surprise</h2>
<p>In Lesson 4.2, adding and subtracting fractions took some work: you had to find a common denominator first. Today there is good news.</p>
<p><strong>Multiplying and dividing fractions is easier than adding them.</strong> You do <strong>not</strong> need a common denominator. The rules are short and direct. You only need to learn them well and use them carefully.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea</span>
<p>Multiplying a fraction by a fraction answers the question "<strong>how much is a part of a part?</strong>" For example, half of half a pizza is a quarter of the pizza: {F(1, 2)} of {F(1, 2)} = {F(1, 4)}. The word <strong>"of"</strong> almost always means <strong>multiply</strong>.</p>
</div>
{area(1, 2, 1, 2, "A square cut in half from top to bottom and in half from side to side. The half on the left is light purple, the top half is light blue, and the part where they overlap, one of the four parts, is dark purple: one fourth.")}
<p style="text-align:center">Half (purple) of a half (blue): the dark part is <strong>1 of 4</strong> equal parts, {F(1, 4)} of the whole.</p>
</section>

<section>
<h2 id="s-multiply"><span aria-hidden="true" class="num-seccion">2</span>Multiply fractions: straight across</h2>
<p>Multiplying fractions is the most direct operation of all.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">To multiply fractions</span>
<p><strong>Numerator × numerator</strong> on top, and <strong>denominator × denominator</strong> on the bottom. Then simplify if you can.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(2, 3)} × {F(4, 5)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Multiply the numerators: 2 × 4 = 8.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Multiply the denominators: 3 × 5 = 15.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> Check if you can simplify: 8 and 15 share no factor greater than 1. It is already in simplest form.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(2, 3)} × {F(4, 5)} = {F(8, 15)}.</p>
</div>
{area(2, 3, 4, 5, "A square cut into 3 columns and 5 rows, 15 small parts in all. 2 columns are light purple (two thirds) and 4 rows are light blue (four fifths). The 8 small parts where they overlap are dark purple: eight fifteenths.")}
<p style="text-align:center">2 of the 3 columns and 4 of the 5 rows: they overlap in <strong>8</strong> of the <strong>15</strong> small parts, {F(8, 15)}.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out!</span>
<p>When you multiply fractions, you do <strong>not</strong> look for a common denominator. That was for adding and subtracting. Here you multiply straight across. And always check at the end if the answer can be simplified.</p>
</div>
{calc("Check it on the calculator", f"""<p>To check {F(2, 3)} × {F(4, 5)}:</p>
<ol>
<li>Press {T("n/d")}, type {T("2")}, go down with {T("▼")}, type {T("3")}, and leave with {T("►")}.</li>
<li>Press {T("×")}.</li>
<li>Press {T("n/d")}, type {T("4")}, go down with {T("▼")}, type {T("5")}, and leave with {T("►")}.</li>
<li>Press {T("enter")}. The screen shows {F(8, 15)}.</li>
</ol>""")}
{practica("p1", "Practice 1 — Multiply fractions", f"What is {F(1, 2)} × {F(3, 4)}?", [("a", F(4, 6)), ("b", F(3, 8)), ("c", F(3, 4)), ("d", F(2, 7))])}
{practica("p2", "Practice 2 — The word “of”", f"What is {F(1, 3)} of {F(1, 2)}?", [("a", F(1, 6)), ("b", F(2, 5)), ("c", F(5, 6)), ("d", F(2, 3))])}
{enlace("multiply", "multiply fractions", "Multiply straight across, numerator by numerator and denominator by denominator, and see the area model.")}
</section>

<section>
<h2 id="s-reciprocal"><span aria-hidden="true" class="num-seccion">3</span>The reciprocal: the flipped fraction</h2>
<p>Before you divide fractions, you need one simple idea: the <strong>reciprocal</strong>.</p>
<p>The <strong>reciprocal</strong> of a fraction is the same fraction <strong>flipped upside down</strong>: the numerator goes to the bottom, and the denominator goes to the top.</p>
<p style="text-align:center;font-size:1.15em">The reciprocal of {F(3, 4)} is {F(4, 3)}.</p>
<div class="ejemplo">
<p class="titulo-ej">Examples of reciprocals</p>
<p class="paso"><span aria-hidden="true" class="n">1</span>The reciprocal of {F(2, 5)} is {F(5, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span>The reciprocal of {F(1, 8)} is {F(8, 1)}, which is the same as 8.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span>The reciprocal of a whole number like 4 is {F(1, 4)}. Every whole number is itself over 1: 4 = {F(4, 1)}.</p>
</div>
<div class="caja caja-tip">
<span class="etiqueta et-verde">A way to check</span>
<p>A number times its reciprocal always equals 1. For example, {F(3, 4)} × {F(4, 3)} = {F(12, 12)} = 1.</p>
</div>
{practica("p3", "Practice 3 — The reciprocal", f"What is the reciprocal of {F(5, 7)}?", [("a", F(5, 7)), ("b", F(7, 5)), ("c", F(7, 7)), ("d", F(1, 5))])}
{enlace("reciprocal", "the reciprocal", "Flip the fraction, and practice with whole numbers and with fractions that have 1 on top.")}
</section>

<section>
<h2 id="s-divide"><span aria-hidden="true" class="num-seccion">4</span>Divide fractions: keep, change, flip</h2>
<p>Here is the most useful trick in Topic 4. To divide fractions, you do not really divide: you change the division into a <strong>multiplication</strong>.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">To divide fractions: keep, change, flip</span>
<p><strong>Keep</strong> the first fraction as it is · <strong>change</strong> ÷ to × · <strong>flip</strong> the second fraction (use its reciprocal). Then multiply.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(3, 4)} ÷ {F(1, 2)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Keep.</strong> The first fraction stays the same: {F(3, 4)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Change.</strong> The ÷ becomes ×.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Flip.</strong> {F(1, 2)} becomes its reciprocal, {F(2, 1)}.</p>
<p class="paso"><span aria-hidden="true" class="n">4</span><strong>Multiply.</strong> {F(3, 4)} × {F(2, 1)} = {F(6, 4)}.</p>
<p class="paso"><span aria-hidden="true" class="n">5</span><strong>Simplify.</strong> Divide the top and the bottom by 2: {F(6, 4)} = {F(3, 2)} = 1&nbsp;{F(1, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(3, 4)} ÷ {F(1, 2)} = {F(3, 2)}, or 1&nbsp;{F(1, 2)}.</p>
</div>
<p><strong>Does it make sense?</strong> Dividing by {F(1, 2)} asks "how many halves fit in {F(3, 4)}?" One half fits, and then half of another half: one and a half. That is why dividing by a fraction less than 1 gives a <strong>bigger</strong> answer.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out! The most common mistake</span>
<p>Flip <strong>only the second fraction</strong>, the one after the ÷ sign. The first one stays exactly the same. And never forget to change the ÷ to ×.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator divides fractions too. For {F(3, 4)} ÷ {F(1, 2)}, write {F(3, 4)} with {T("n/d")}, press {T("÷")}, write {F(1, 2)}, and press {T("enter")}. The screen shows {F(3, 2)}.</p>""")}
{practica("p4", "Practice 4 — Divide fractions", f"What is {F(1, 2)} ÷ {F(1, 4)}?", [("a", F(1, 8)), ("b", "2"), ("c", F(1, 2)), ("d", F(2, 6))])}
{enlace("divide", "divide fractions", "Keep the first fraction, change to multiplication, and flip the second, step by step.")}
</section>

<section>
<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Fractions in real-life problems</h2>
<p>Always use the 4-step method from Lesson 1.3. Remember the key clue: the word <strong>"of"</strong> usually means <strong>multiply</strong>. Cutting or sharing something into pieces of a fractional size ("how many pieces of …?", "how many servings of …?") usually means <strong>divide</strong>.</p>
<div class="ejemplo">
<p class="titulo-ej">📋 "A recipe calls for {F(3, 4)} cup of sugar. You are making only half of the recipe. How much sugar do you need?"</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Read and underline.</strong> {F(3, 4)} cup of sugar; you want half ({F(1, 2)}) of the recipe.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Choose the operation.</strong> "Half of {F(3, 4)}": the word "of" means multiply. It is {F(1, 2)} × {F(3, 4)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve.</strong> {F(1, 2)} × {F(3, 4)} = {F(3, 8)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Does it make sense?</strong> {F(3, 8)} cup is less than {F(3, 4)} cup. That makes sense, because you are making half the recipe. You need {F(3, 8)} cup of sugar.</p>
</div>
{practica("p5", "Practice 5 — A word problem", f"A board 6 feet long is cut into pieces that are {F(1, 2)} foot each. How many pieces do you get? (6 ÷ {F(1, 2)})", [("a", "3 pieces"), ("b", "12 pieces"), ("c", "6 pieces"), ("d", f"{F(1, 12)} of a piece")])}
{enlace("real-life", "fractions in real life", "Decide if the problem asks you to multiply or to divide, and solve it.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">6</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-4-3.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you. In the last activity, multiplying and dividing are mixed: the hard part is not the math, it is deciding which one the problem needs.</li>
<li><strong>With a sheet of paper.</strong> Fold a sheet in half and shade that half. Fold it in half again the other way, and shade half of the shaded part with another color. Open it and count the parts: there it is, in your hands, why {F(1, 2)} × {F(1, 2)} = {F(1, 4)}. Repeat with thirds: fold in three, then in half. The area model on the practice page shows the same idea.</li>
<li><strong>In your kitchen.</strong> Take a recipe. Find how much of each ingredient you would need for half the recipe (multiply by {F(1, 2)}) and for double the recipe (multiply by 2). Write the two columns next to the original amounts.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">7</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. Questions with only two choices show the explanation right away. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "To multiply two fractions, you should:", [("a", "Find a common denominator first."), ("b", "Flip both fractions."), ("c", "Multiply numerator by numerator and denominator by denominator."), ("d", "Add the numerators.")])}
{quiz("B", f"What is {F(2, 3)} × {F(1, 4)}?", [("a", f"{F(2, 12)} = {F(1, 6)}"), ("b", F(3, 7)), ("c", F(8, 3)), ("d", F(2, 7))])}
{quiz("C", f"What is {F(1, 2)} of {F(1, 3)}?", [("a", F(2, 3)), ("b", F(5, 6)), ("c", F(3, 2)), ("d", F(1, 6))])}
{quiz("D", f"What is the reciprocal of {F(2, 9)}?", [("a", F(2, 9)), ("b", F(9, 2)), ("c", F(1, 2)), ("d", F(9, 9))])}
{quiz("E", "To divide fractions, after you keep the first fraction the same, you should:", [("a", "Flip the first fraction and add."), ("b", "Flip both fractions."), ("c", "Find a common denominator."), ("d", "Change ÷ to ×, flip the second fraction, and multiply.")])}
{quiz("F", f"What is {F(3, 5)} ÷ {F(1, 2)}?", [("a", F(3, 10)), ("b", F(6, 5)), ("c", F(3, 7)), ("d", F(5, 6))])}
{quiz("G", f"A recipe calls for {F(2, 3)} cup of oil. To make half of the recipe, how much oil do you need?", [("a", f"{F(2, 3)} cup"), ("b", f"{F(4, 3)} cups"), ("c", f"{F(1, 3)} cup"), ("d", f"{F(1, 6)} cup")])}
{quiz("H", f"A ribbon 4 yards long is cut into pieces that are {F(1, 4)} yard each. How many pieces do you get?", [("a", "16 pieces"), ("b", "1 piece"), ("c", "4 pieces"), ("d", "8 pieces")])}
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
<div aria-label="Self-check checklist for multiplying and dividing fractions (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for multiplying and dividing fractions and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Multiply fractions</th><td>I multiply straight across with no mistakes, and I simplify.</td><td>I multiply correctly most of the time.</td><td>I look for a common denominator when I do not need one, or I mix up the steps.</td></tr>
<tr><th scope="row">Find the reciprocal</th><td>I find the reciprocal of any fraction or whole number.</td><td>I find the reciprocal of a fraction, but whole numbers confuse me.</td><td>I mix up the reciprocal with the original fraction.</td></tr>
<tr><th scope="row">Divide fractions</th><td>I use "keep, change, flip" with no mistakes.</td><td>I divide correctly, with an occasional slip.</td><td>I flip the wrong fraction, or I forget to change ÷ to ×.</td></tr>
<tr><th scope="row">Solve problems and simplify</th><td>I choose the right operation, solve, simplify, and check that the answer makes sense.</td><td>I set up the problem correctly, but I do not always simplify.</td><td>I am not sure whether the problem asks me to multiply or to divide.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>In this lesson you completed the four operations with fractions: add, subtract, multiply, and divide. You can now work with proper and improper fractions.</p>
<p>One piece of Topic 4 is still missing. So far you have worked with fractions on their own. In <strong>Lesson 4.4 · Operations with mixed numbers</strong> you will see what happens when a whole number comes with a fraction, like 2&nbsp;{F(1, 2)} cups, and how to calculate with them using everything you already know.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: <a href="lesson-4-4.html">Lesson 4.4 · Operations with mixed numbers</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>product</dt><dd>The answer to a multiplication. The product of 1/2 and 3/4 is 3/8.</dd>
<dt>quotient</dt><dd>The answer to a division. The quotient of 3/4 ÷ 1/2 is 3/2.</dd>
<dt>reciprocal</dt><dd>A fraction flipped upside down. The reciprocal of 3/4 is 4/3. A number times its reciprocal equals 1.</dd>
<dt>keep, change, flip</dt><dd>The steps to divide fractions: keep the first fraction, change ÷ to ×, and flip the second fraction.</dd>
<dt>"of"</dt><dd>In a problem with fractions, "of" usually means multiply: half of 3/4 is 1/2 × 3/4.</dd>
<dt>area model</dt><dd>A rectangle cut into rows and columns that shows the product of two fractions as the part where they overlap.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.3</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-4-3.html"), "w", encoding="utf-8").write(html)
print("ok")
