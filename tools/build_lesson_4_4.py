"""Builds math/level-1/lesson-4-4.html (English). Run tools/ged_standards.py afterwards
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
    href = href or f"practice-4-4.html#{ancla}"
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

def M(w, n, d):
    """Mixed number: whole number and a stacked fraction, kept on one line."""
    return f'<span style="white-space:nowrap">{w}&nbsp;{F(n, d)}</span>'

def bars(N, d, label, color="#7b1fa2", width=360):
    """N parts of size 1/d, drawn as as many whole bars as needed."""
    k = -(-N // d); h, w = 34, width / d; out = []
    for b in range(k):
        for i in range(d):
            idx = b * d + i
            out.append(f'<rect x="{10 + i * w:.1f}" y="{6 + b * (h + 10)}" width="{w:.1f}" height="{h}" fill="{color if idx < N else "#fff"}" stroke="#37474f" stroke-width="2"/>')
    return f'<svg viewBox="0 0 {width + 20} {k * (h + 10) + 6}" role="img" aria-label="{label}" style="width:100%;max-width:{width + 20}px;height:auto;display:block;margin:6px auto;">{"".join(out)}</svg>'

LESSON = {
 "next": "Lesson 5.1", "review": "sections 2, 3, 4, and 5",
 "practice": {
  "p1": {"ok": "a", "hints": {
      "b": "6 is 2 × 3, the whole number times the denominator. Now add the numerator: 6 + 1.",
      "c": "5 is 2 + 3. Multiply the whole number by the denominator: 2 × 3 = 6. Then add the numerator.",
      "d": "2/3 is only the fraction part. Do not forget the 2 wholes: 2 × 3 = 6 thirds."},
   "right": "2 × 3 = 6, and 6 + 1 = 7. The denominator stays 3: 7/3.",
   "solution": "Whole number × denominator: 2 × 3 = 6. Add the numerator: 6 + 1 = 7. The denominator stays 3. So 2 1/3 = 7/3."},
  "p2": {"ok": "b", "hints": {
      "a": "You multiplied only the whole number (1 × 2 = 2) and kept the 1/2. Change 1 1/2 to 3/2 first.",
      "c": "Change 1 1/2 to an improper fraction first: 3/2. Then 3/2 × 2/1.",
      "d": "Change 1 1/2 to an improper fraction first: 3/2. Then 3/2 × 2/1."},
   "right": "1 1/2 = 3/2, and 3/2 × 2/1 = 6/2 = 3. Two times one and a half is three.",
   "solution": "1 1/2 = 3/2, and 2 = 2/1. Multiply: 3/2 × 2/1 = 6/2 = 3."},
  "p3": {"ok": "b", "hints": {
      "a": "Change both to improper fractions first: 2 1/2 = 5/2 and 1 1/4 = 5/4. Then keep, change, flip.",
      "c": "You multiplied instead of dividing. Flip the second fraction: 5/4 becomes 4/5.",
      "d": "You flipped the first number. Keep 5/2, and flip only the second: 4/5."},
   "right": "5/2 × 4/5 = 20/10 = 2. How many 1 1/4 fit in 2 1/2? Exactly two.",
   "solution": "2 1/2 = 5/2 and 1 1/4 = 5/4. Keep, change, flip: 5/2 × 4/5 = 20/10 = 2."},
  "p4": {"ok": "b", "hints": {
      "a": "Change to improper fractions: 7/4 + 5/2 = 7/4 + 10/4. Count the wholes again.",
      "c": "3 3/4 is only 1 + 2 wholes with the 3/4. You still have the 1/2 to add: 3/4 + 2/4 is more than 1.",
      "d": "You added 1/2 + 3/4 as if it were 1/2. Use a common denominator: 3/4 + 2/4 = 5/4."},
   "right": "7/4 + 10/4 = 17/4 = 4 1/4.",
   "solution": "1 3/4 = 7/4 and 2 1/2 = 5/2 = 10/4. Add: 7/4 + 10/4 = 17/4. And 17 ÷ 4 = 4 remainder 1, so 4 1/4."},
  "p5": {"ok": "b", "hints": {
      "a": "You subtracted the fractions the wrong way (3/4 − 1/2). Change both to fourths: 22/4 − 7/4.",
      "c": "Check the subtraction: 22/4 − 7/4 = 15/4. What is 15 ÷ 4?",
      "d": "Check the wholes: 5 1/2 − 1 3/4 is less than 4. Change both to fourths: 22/4 − 7/4."},
   "right": "22/4 − 7/4 = 15/4 = 3 3/4 feet.",
   "solution": "5 1/2 = 11/2 = 22/4 and 1 3/4 = 7/4. Subtract: 22/4 − 7/4 = 15/4. And 15 ÷ 4 = 3 remainder 3, so 3 3/4 feet are left."},
 },
 "quiz": {
  "A": {"ok": "c", "hints": {"a": "Working with the whole numbers and the fractions separately gives a wrong answer when you multiply or divide.", "b": "A common denominator is for adding and subtracting.", "d": "Flipping is for dividing, and only the second number, after you change it to an improper fraction."},
        "solution": "First change each mixed number to an improper fraction. Then multiply or divide as in Lesson 4.3."},
  "B": {"ok": "d", "hints": {"a": "15 is 3 × 5. Now add the numerator: 15 + 2.", "b": "Multiply the whole number by the denominator, not by the numerator: 3 × 5 = 15.", "c": "8 is 3 + 5. Multiply the whole number by the denominator: 3 × 5 = 15. Then add 2."},
        "solution": "3 × 5 = 15, and 15 + 2 = 17. The denominator stays 5: 3 2/5 = 17/5."},
  "C": {"ok": "a", "hints": {"b": "That is the first number. Change both to improper fractions and multiply: 7/3 × 3/2.", "c": "Do not multiply the wholes and the fractions separately. Change to improper fractions: 7/3 × 3/2.", "d": "Change to improper fractions: 7/3 × 3/2 = 21/6. Simplify and change back to a mixed number."},
        "solution": "2 1/3 = 7/3 and 1 1/2 = 3/2. Multiply: 7/3 × 3/2 = 21/6 = 7/2 = 3 1/2."},
  "D": {"ok": "b", "hints": {"a": "You multiplied instead of dividing. Flip the second number: 3/2 becomes 2/3.", "c": "Change to improper fractions first: 9/2 ÷ 3/2. Then keep, change, flip.", "d": "Change to improper fractions first: 9/2 ÷ 3/2. Then keep, change, flip."},
        "solution": "4 1/2 = 9/2 and 1 1/2 = 3/2. Keep, change, flip: 9/2 × 2/3 = 18/6 = 3. Check: three times 1 1/2 is 4 1/2."},
  "E": {"ok": "c", "hints": {"a": "Use a common denominator: 1/4 + 2/4 = 3/4, not 1/4.", "b": "Add the wholes again: 2 + 1 = 3, not 4.", "d": "1/2 = 2/4, so 1/4 + 2/4 = 3/4."},
        "solution": "2 1/4 = 9/4 and 1 1/2 = 6/4. Add: 9/4 + 6/4 = 15/4 = 3 3/4."},
  "F": {"ok": "d", "hints": {"a": "The answer must be less than 3, because you take away more than 2.", "b": "You kept the 3/5 instead of taking it away. Change 5 to fifths: 25/5 − 13/5.", "c": "The answer must be less than 3, because you take away more than 2. Change 5 to fifths: 25/5 − 13/5."},
        "solution": "5 = 25/5 and 2 3/5 = 13/5. Subtract: 25/5 − 13/5 = 12/5 = 2 2/5."},
  "G": {"ok": "a", "hints": {"b": "You doubled only the whole number. Double the 1/2 too: 1/2 + 1/2 = 1.", "c": "Check: 3/2 × 2 = 6/2. What is 6 ÷ 2?", "d": "Doubling means multiply by 2. The answer must be more than 1 1/2."},
        "solution": "1 1/2 = 3/2, and 3/2 × 2 = 6/2 = 3 cups."},
  "H": {"ok": "b", "hints": {"a": "Check the fractions: you cannot take 3/4 from 1/4 without breaking a whole. Use improper fractions: 13/4 − 7/4.", "c": "Change both to fourths: 13/4 − 7/4 = 6/4. Simplify it.", "d": "You subtracted 1/4 − 3/4 the wrong way. Use improper fractions: 13/4 − 7/4."},
        "solution": "3 1/4 = 13/4 and 1 3/4 = 7/4. Subtract: 13/4 − 7/4 = 6/4 = 3/2 = 1 1/2 quarts."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 4.4 · Math Level 1 (English) — built by tools/build_lesson_4_4.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 4.4 · Operations with mixed numbers · LearnGED</title>
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
<h1>Lesson 4.4 · Operations with mixed numbers</h1>
<p class="lema">Mixed numbers look hard, but there is a trick that always works: change them to improper fractions and use everything you already learned in this topic.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🔢</span> Add, subtract, multiply, and divide</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Change</strong> mixed numbers to improper fractions, and back, with confidence.</li>
<li><strong>Multiply and divide</strong> mixed numbers by changing them to improper fractions first.</li>
<li><strong>Add and subtract</strong> mixed numbers, including cases where you take away more than the fraction you have.</li>
<li><strong>Solve</strong> real-life problems with mixed numbers, and simplify the answer.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-old-friend">An old friend</a></li>
<li><a href="#s-convert">Quick review: mixed numbers and improper fractions</a></li>
<li><a href="#s-multiply-divide">Multiply and divide mixed numbers</a></li>
<li><a href="#s-add-subtract">Add and subtract mixed numbers</a></li>
<li><a href="#s-real-life">Mixed numbers in real-life problems</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">The end of Topic 4</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-old-friend"><span aria-hidden="true" class="num-seccion">1</span>An old friend</h2>
<p>You have already met mixed numbers in this topic. In Lesson 4.2, the answer 5/4 became {M(1, 1, 4)}. In Lesson 4.3, the answer 3/2 became {M(1, 1, 2)}. Today, mixed numbers get a lesson of their own.</p>
<p>A <strong>mixed number</strong> is a whole number together with a fraction. For example, {M(2, 1, 2)} means "two wholes and one half." We use them every day: a recipe calls for {M(1, 3, 4)} cups of flour; a board is {M(5, 1, 2)} feet long; a movie lasts {M(2, 1, 4)} hours.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea of this lesson</span>
<p>There are no new rules to memorize. The secret to working with mixed numbers is just one: <strong>change them to improper fractions</strong>, then do exactly what you already know how to do with fractions. At the end, write the answer as a mixed number again.</p>
</div>
</section>

<section>
<h2 id="s-convert"><span aria-hidden="true" class="num-seccion">2</span>Quick review: mixed numbers and improper fractions</h2>
<p>The whole lesson rests on this skill, so let us review it carefully before we go on.</p>
<h3>From a mixed number to an improper fraction</h3>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The rule</span>
<p><strong>Whole number × denominator + numerator</strong> goes on top. The denominator does not change.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: change {M(3, 1, 4)} to an improper fraction</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Multiply the whole number by the denominator: 3 × 4 = 12. (Each whole has 4 fourths, so 3 wholes have 12 fourths.)</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Add the numerator: 12 + 1 = 13. That is the new numerator.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> The denominator stays the same: 4.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {M(3, 1, 4)} = {F(13, 4)}.</p>
</div>
{bars(13, 4, "Four bars, each divided into 4 equal parts. The first three bars are fully shaded, and the fourth bar has 1 part shaded: 3 wholes and 1 fourth, which is 13 fourths in all.")}
<p style="text-align:center">3 whole bars and 1 more fourth: <strong>13 fourths</strong> in all.</p>
<h3>From an improper fraction to a mixed number</h3>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The rule</span>
<p><strong>Numerator ÷ denominator.</strong> The quotient is the whole number, the remainder is the new numerator, and the denominator does not change.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: change {F(17, 5)} to a mixed number</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Divide: 17 ÷ 5 = 3, with 2 left over (remainder 2).</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> The quotient (3) is the whole number. The remainder (2) is the numerator.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> The denominator stays the same: 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(17, 5)} = {M(3, 2, 5)}.</p>
</div>
{practica("p1", "Practice 1 — Change to an improper fraction", f"Change {M(2, 1, 3)} to an improper fraction.", [("a", F(7, 3)), ("b", F(6, 3)), ("c", F(5, 3)), ("d", F(2, 3))])}
{enlace("convert", "mixed numbers and improper fractions", "Change mixed numbers to improper fractions and back, and see them with bars.")}
</section>

<section>
<h2 id="s-multiply-divide"><span aria-hidden="true" class="num-seccion">3</span>Multiply and divide mixed numbers</h2>
<p>Here the rule is firm, with no exceptions: <strong>never</strong> multiply or divide the whole numbers on one side and the fractions on the other. Change everything to improper fractions first.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">To multiply or divide mixed numbers</span>
<p>1) Change to improper fractions · 2) multiply or divide as in Lesson 4.3 · 3) simplify and change back to a mixed number.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example (multiply): {M(2, 1, 2)} × {M(1, 1, 3)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Change.</strong> {M(2, 1, 2)} = {F(5, 2)} and {M(1, 1, 3)} = {F(4, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Multiply.</strong> Numerators: 5 × 4 = 20. Denominators: 2 × 3 = 6. You get {F(20, 6)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Simplify.</strong> Divide the top and the bottom by 2: {F(20, 6)} = {F(10, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">4</span><strong>Change back.</strong> 10 ÷ 3 = 3, remainder 1.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {M(2, 1, 2)} × {M(1, 1, 3)} = {M(3, 1, 3)}.</p>
</div>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out! The most common mistake</span>
<p>It is tempting to multiply "2 × 1" and "{F(1, 2)} × {F(1, 3)}" separately. That gives {M(2, 1, 6)}, which is wrong: the right answer is {M(3, 1, 3)}. Always change to improper fractions before you multiply or divide.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example (divide): {M(3, 3, 4)} ÷ {M(1, 1, 2)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Change.</strong> {M(3, 3, 4)} = {F(15, 4)} and {M(1, 1, 2)} = {F(3, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Keep, change, flip.</strong> {F(15, 4)} × {F(2, 3)} = {F(30, 12)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Simplify.</strong> Divide the top and the bottom by 6: {F(30, 12)} = {F(5, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Change back.</strong> 5 ÷ 2 = 2, remainder 1: {M(2, 1, 2)}.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator has a template for mixed numbers, U n/d, the second function of {T("n/d")}.</p>
<ol>
<li>For {M(2, 1, 2)}: type {T("2")}, press {T("2nd")} {T("n/d")}, type {T("1")}, go down with {T("▼")}, type {T("2")}, and leave with {T("►")}.</li>
<li>Press {T("×")}, and write {M(1, 1, 3)} the same way.</li>
<li>Press {T("enter")}. The screen shows the improper fraction {F(10, 3)}.</li>
<li>To see it as a mixed number, press {T("2nd")} {T("x⁻¹")} (n/d◂▸Un/d) and {T("enter")}. The screen shows {M(3, 1, 3)}.</li>
</ol>""")}
{practica("p2", "Practice 2 — Multiply mixed numbers", f"What is {M(1, 1, 2)} × 2?", [("a", M(2, 1, 2)), ("b", "3"), ("c", M(3, 1, 2)), ("d", "4")])}
{practica("p3", "Practice 3 — Divide mixed numbers", f"What is {M(2, 1, 2)} ÷ {M(1, 1, 4)}?", [("a", M(1, 1, 4)), ("b", "2"), ("c", M(3, 1, 8)), ("d", F(1, 2))])}
{enlace("multiply-divide", "multiply and divide mixed numbers", "Change everything to improper fractions and use the rules from Lesson 4.3.")}
</section>

<section>
<h2 id="s-add-subtract"><span aria-hidden="true" class="num-seccion">4</span>Add and subtract mixed numbers</h2>
<p>To add and subtract, use the same plan: change to improper fractions, find a common denominator (as in Lesson 4.2), add or subtract, and change back to a mixed number. This one method works for every case.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">To add or subtract mixed numbers</span>
<p>Change to improper fractions · find a common denominator · add or subtract the numerators · change back to a mixed number.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example (add): {M(1, 3, 4)} + {M(2, 1, 2)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Change.</strong> {M(1, 3, 4)} = {F(7, 4)} and {M(2, 1, 2)} = {F(5, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Common denominator (4).</strong> {F(5, 2)} = {F(10, 4)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Add the numerators.</strong> {F(7, 4)} + {F(10, 4)} = {F(17, 4)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Change back.</strong> 17 ÷ 4 = 4, remainder 1: {M(4, 1, 4)}.</p>
</div>
<h3>Subtracting from a whole number</h3>
<p>Problems like 4 − {M(1, 2, 3)} often scare students, because "there is no fraction to take from." With improper fractions, that problem disappears.</p>
<div class="ejemplo">
<p class="titulo-ej">Example (subtract): 4 − {M(1, 2, 3)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Write the whole number as a fraction.</strong> 4 = {F(4, 1)} = {F(12, 3)} (common denominator 3).</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Change the mixed number.</strong> {M(1, 2, 3)} = {F(5, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Subtract the numerators.</strong> {F(12, 3)} − {F(5, 3)} = {F(7, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Change back.</strong> 7 ÷ 3 = 2, remainder 1: {M(2, 1, 3)}.</p>
</div>
<div class="caja caja-tip">
<span class="etiqueta et-verde">Why one method?</span>
<p>There is another way to add mixed numbers: wholes with wholes and fractions with fractions. It works, but when you subtract and the top fraction is too small, you must <strong>borrow</strong> a whole (for example, 1 = {F(3, 3)}). Changing to improper fractions always works the same way, with no special tricks. Learn this one well, and you can solve all four operations with the same recipe. The practice page shows both ways, so you can compare them.</p>
</div>
{practica("p4", "Practice 4 — Add mixed numbers", f"What is {M(1, 3, 4)} + {M(2, 1, 2)}?", [("a", M(3, 1, 4)), ("b", M(4, 1, 4)), ("c", M(3, 3, 4)), ("d", M(4, 1, 2))])}
{enlace("add-subtract", "add and subtract mixed numbers", "See the steps with improper fractions, and compare them with the wholes-and-fractions way.")}
</section>

<section>
<h2 id="s-real-life"><span aria-hidden="true" class="num-seccion">5</span>Mixed numbers in real-life problems</h2>
<p>Always use the 4-step method from Lesson 1.3: read and underline, choose the operation, solve, and check if the answer makes sense. Mixed numbers show up most in cooking, carpentry, and measurements.</p>
<div class="ejemplo">
<p class="titulo-ej">📋 "A carpenter has a board 8 feet long and cuts off {M(3, 1, 2)} feet. How much of the board is left?"</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Read and underline.</strong> A board 8 feet long; cuts off {M(3, 1, 2)} feet; how much is left.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Choose the operation.</strong> "Left" means subtract: 8 − {M(3, 1, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve.</strong> 8 = {F(16, 2)} and {M(3, 1, 2)} = {F(7, 2)}. {F(16, 2)} − {F(7, 2)} = {F(9, 2)} = {M(4, 1, 2)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Does it make sense?</strong> {M(4, 1, 2)} feet are left, less than the 8 feet at the start. That makes sense, because a piece was cut off.</p>
</div>
{practica("p5", "Practice 5 — A word problem", f"A board is {M(5, 1, 2)} feet long. If you cut off {M(1, 3, 4)} feet, how much is left?", [("a", f"{M(4, 1, 4)} feet"), ("b", f"{M(3, 3, 4)} feet"), ("c", f"{M(3, 1, 4)} feet"), ("d", f"{M(4, 3, 4)} feet")])}
{enlace("real-life", "mixed numbers in real life", "Solve problems about carpentry, recipes, and time with mixed numbers.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">6</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open. With it, you finish Topic 4.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-4-4.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Write six mixed numbers, change them to improper fractions, and then change them back to mixed numbers. If you do not get the same number back, the mistake is on the way there or on the way back: find it now. Then solve eight operations, two of each of the four.</li>
<li><strong>In your kitchen.</strong> Take a recipe with mixed numbers ({M(1, 1, 2)} cups, {M(2, 3, 4)} tablespoons). Find how much you would need to make double the recipe, and write it as a mixed number, not as an improper fraction: it is easier to read when you cook.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">7</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. Questions with only two choices show the explanation right away. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "To multiply or divide mixed numbers, the first thing you do is:", [("a", "Multiply the whole numbers together and the fractions together."), ("b", "Find a common denominator."), ("c", "Change each mixed number to an improper fraction."), ("d", "Flip both mixed numbers.")])}
{quiz("B", f"Change {M(3, 2, 5)} to an improper fraction.", [("a", F(15, 5)), ("b", F(11, 5)), ("c", F(8, 5)), ("d", F(17, 5))])}
{quiz("C", f"What is {M(2, 1, 3)} × {M(1, 1, 2)}?", [("a", M(3, 1, 2)), ("b", M(2, 1, 3)), ("c", M(2, 1, 6)), ("d", "4")])}
{quiz("D", f"What is {M(4, 1, 2)} ÷ {M(1, 1, 2)}?", [("a", "6"), ("b", "3"), ("c", M(2, 1, 4)), ("d", M(3, 1, 2))])}
{quiz("E", f"What is {M(2, 1, 4)} + {M(1, 1, 2)}?", [("a", M(3, 1, 4)), ("b", M(4, 1, 4)), ("c", M(3, 3, 4)), ("d", M(3, 1, 2))])}
{quiz("F", f"What is 5 − {M(2, 3, 5)}?", [("a", M(3, 3, 5)), ("b", M(2, 3, 5)), ("c", M(3, 2, 5)), ("d", M(2, 2, 5))])}
{quiz("G", f"A recipe uses {M(1, 1, 2)} cups of sugar. To make double the recipe, how much sugar do you need?", [("a", "3 cups"), ("b", f"{M(2, 1, 2)} cups"), ("c", f"{M(3, 1, 2)} cups"), ("d", f"{M(1, 3, 4)} cups")])}
{quiz("H", f"A pitcher has {M(3, 1, 4)} quarts of water, and you use {M(1, 3, 4)} quarts. How much water is left?", [("a", "2 quarts"), ("b", f"{M(1, 1, 2)} quarts"), ("c", f"{M(1, 1, 4)} quarts"), ("d", f"{M(2, 1, 2)} quarts")])}
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
<div aria-label="Self-check checklist for operations with mixed numbers (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for operations with mixed numbers and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Change between mixed numbers and improper fractions</th><td>I change both ways quickly and with no mistakes.</td><td>I change correctly most of the time.</td><td>I forget to add the numerator, or I change the denominator.</td></tr>
<tr><th scope="row">Multiply and divide mixed numbers</th><td>I change to improper fractions before I operate, and I simplify.</td><td>I operate correctly, with an occasional slip.</td><td>I try to work with the whole numbers and the fractions separately.</td></tr>
<tr><th scope="row">Add and subtract mixed numbers</th><td>I find the common denominator and solve, even when I subtract from a whole number.</td><td>I add and subtract well in simple cases.</td><td>I get stuck when the fraction I take away is bigger than the one I have.</td></tr>
<tr><th scope="row">Solve problems and simplify</th><td>I choose the right operation, solve, simplify, and write the units.</td><td>I set up the problem correctly, but I do not always change back to a mixed number.</td><td>I am not sure which operation the problem needs.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">🏁</span>The end of Topic 4 and the first half of Level 1</h2>
<p>With this lesson you finish <strong>Topic 4 · Fractions</strong>. You now know fractions from start to finish: equivalent fractions, simplifying, the four operations, and now mixed numbers too.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">An important milestone</span>
<p>With Topics 1 to 4 complete, you can do the four operations with whole numbers, decimals, fractions, and mixed numbers: all of basic arithmetic. That is the foundation for the rest of the course.</p>
</div>
<p>In <strong>Topic 5 · Patterns and algebraic thinking</strong> you will take a new and exciting step: from numbers to ideas. <strong>Lesson 5.1 · Number and shape patterns</strong> will teach you to discover the hidden rule behind a sequence: your first step toward algebra.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: Topic 5 · <a href="lesson-5-1.html">Lesson 5.1 · Number and shape patterns</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>mixed number</dt><dd>A whole number together with a fraction, like 2 1/2 ("two and one half").</dd>
<dt>improper fraction</dt><dd>A fraction whose numerator is greater than or equal to its denominator, like 5/2. It is 1 or more.</dd>
<dt>quotient</dt><dd>The answer to a division. In 17 ÷ 5, the quotient is 3.</dd>
<dt>remainder</dt><dd>What is left over in a division. In 17 ÷ 5, the remainder is 2.</dd>
<dt>borrow</dt><dd>In the wholes-and-fractions way of subtracting, to break one whole into a fraction (like 1 = 3/3) when the top fraction is too small.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.4</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-4-4.html"), "w", encoding="utf-8").write(html)
print("ok")
