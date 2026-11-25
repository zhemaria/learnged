"""Builds math/level-1/lesson-4-2.html (English). Run tools/ged_standards.py afterwards
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
    href = href or f"practice-4-2.html#{ancla}"
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

LESSON = {
 "next": "Lesson 4.3", "review": "sections 2, 3, and 4",
 "practice": {
  "p1": {"ok": "b", "hints": {
      "a": "You added the denominators too. The parts are eighths before and after: the denominator stays 8.",
      "c": "Check the top: 3 + 2 = 5, not 6.",
      "d": "1/8 is what you get if you subtract. This problem asks you to add."},
   "right": "3 eighths plus 2 eighths are 5 eighths. The parts are still eighths, so the denominator stays 8.",
   "solution": "Same denominator: add only the numerators, 3 + 2 = 5, and keep the 8. So 3/8 + 2/8 = 5/8."},
  "p2": {"ok": "a", "hints": {
      "b": "You subtracted the denominators too. A fraction can never have 0 on the bottom. Keep the 9.",
      "c": "11/9 is what you get if you add. This problem asks you to subtract.",
      "d": "You added the denominators. The parts are ninths before and after: keep the 9."},
   "right": "7 ninths minus 4 ninths are 3 ninths. In section 4 you will see that 3/9 can be simplified to 1/3.",
   "solution": "Same denominator: subtract only the numerators, 7 − 4 = 3, and keep the 9. So 7/9 − 4/9 = 3/9 (which simplifies to 1/3)."},
  "p3": {"ok": "b", "hints": {
      "a": "10 is 4 + 6. Adding the denominators does not work: 10 is not a multiple of 4.",
      "c": "24 works too (4 × 6), but it is not the only one. Look for a smaller number that 4 and 6 both go into.",
      "d": "2 is a factor of 4 and 6, not a multiple. The common denominator must be a multiple of both."},
   "right": "Multiples of 6: 6, 12. Twelve is the first one that 4 also goes into.",
   "solution": "Go through the multiples of the larger denominator, 6: 6, 12, … 4 does not go into 6, but it does go into 12. So 12 is the smallest common denominator."},
  "p4": {"ok": "b", "hints": {
      "a": "You added the tops and the bottoms. First make the denominators the same: 1/2 = 2/4.",
      "c": "2/4 is only the first fraction, changed to fourths. Now add the 1/4.",
      "d": "Check: the answer should be more than 1/2, because you are adding to 1/2."},
   "right": "1/2 = 2/4, and 2/4 + 1/4 = 3/4.",
   "solution": "4 is a multiple of 2, so the common denominator is 4. 1/2 = 2/4, and 2/4 + 1/4 = 3/4."},
 },
 "quiz": {
  "A": {"ok": "a", "hints": {"b": "The denominator tells the size of the parts. Does the size change when you join them?", "c": "The denominator tells the size of the parts. Does the size change when you join them?", "d": "The denominator tells the size of the parts. Does the size change when you join them?"},
        "solution": "The denominator stays the same. It tells the size of the parts, and joining parts of the same size does not change their size. Only the numerators are added."},
  "B": {"ok": "d", "hints": {"a": "You added the denominators. Keep the 7.", "b": "Check the top: 2 + 3 = 5.", "c": "Do not multiply the denominators here. They are already the same."},
        "solution": "Same denominator: 2 + 3 = 5, and keep the 7. So 2/7 + 3/7 = 5/7."},
  "C": {"ok": "c", "hints": {"a": "You added the denominators. Keep the 6, subtract the tops, then simplify.", "b": "7/6 is what you get if you add. This problem asks you to subtract.", "d": "A fraction can never have 0 on the bottom. Keep the 6."},
        "solution": "5 − 2 = 3, so 5/6 − 2/6 = 3/6. Then simplify: divide the top and the bottom by 3, and 3/6 = 1/2."},
  "D": {"ok": "b", "hints": {"a": "9 is 3 + 6. Adding the denominators does not work.", "c": "6 does not go into 3. The common denominator must be a multiple of both.", "d": "5 is not a multiple of 3 or of 6."},
        "solution": "6 is already a multiple of 3 (3 × 2 = 6). So 6 is the common denominator: 1/3 = 2/6."},
  "E": {"ok": "d", "hints": {"a": "You added the tops and the bottoms. 2/5 is less than 1/2, but you added something to 1/2!", "b": "Change both fractions to sixths first: 1/2 = 3/6 and 1/3 = 2/6.", "c": "Change both fractions to sixths first, and add the numerators."},
        "solution": "The common denominator is 6: 1/2 = 3/6 and 1/3 = 2/6. Then 3/6 + 2/6 = 5/6."},
  "F": {"ok": "a", "hints": {"b": "You subtracted the tops and the bottoms. First change 3/4 to eighths.", "c": "Change 3/4 to eighths: 3/4 = 6/8. Then subtract 1/8.", "d": "7/8 is what you get if you add. This problem asks you to subtract."},
        "solution": "8 is a multiple of 4, so change 3/4 to eighths: 3/4 = 6/8. Then 6/8 − 1/8 = 5/8."},
  "G": {"ok": "b", "hints": {"a": "4/8 can still be simplified: 4 and 8 can both be divided by 4.", "c": "You divided only the top. Divide the top and the bottom by the same number.", "d": "8/4 is 2 wholes. You switched the numbers."},
        "solution": "Divide the top and the bottom by 4: 4 ÷ 4 = 1 and 8 ÷ 4 = 2. So 4/8 = 1/2."},
  "H": {"ok": "c", "hints": {"a": "You added the tops and the bottoms. Change 1/2 to fourths first.", "b": "1/6 hour is only 10 minutes. The answer must be more than 1/2 hour.", "d": "2/4 is only the 1/2 hour changed to fourths. Now add the 1/4 hour."},
        "solution": "1/2 = 2/4, so 1/4 + 2/4 = 3/4 hour. That is 45 minutes."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 4.2 · Math Level 1 (English) — built by tools/build_lesson_4_2.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 4.2 · Adding and subtracting fractions · LearnGED</title>
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
<h1>Lesson 4.2 · Adding and subtracting fractions</h1>
<p class="lema">Join and take away parts of a whole. The secret is simple: the parts must be the same size.</p>
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
<li><strong>Explain</strong> why only the numerators are added or subtracted.</li>
<li><strong>Add and subtract</strong> fractions with the same denominator.</li>
<li><strong>Find</strong> a common denominator for two fractions.</li>
<li><strong>Add and subtract</strong> fractions with different denominators.</li>
<li><strong>Simplify</strong> the result, and write it as a mixed number when it is more than 1.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-why">Why the denominator matters</a></li>
<li><a href="#s-same">The same denominator</a></li>
<li><a href="#s-different">Different denominators</a></li>
<li><a href="#s-simplify">Simplify the result</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-why"><span aria-hidden="true" class="num-seccion">1</span>Why the denominator matters</h2>
<p>In Lesson 4.1 you learned that the <strong>denominator</strong> tells the <strong>size</strong> of the parts, and the <strong>numerator</strong> tells <strong>how many</strong> parts you have.</p>
<p>Think about money. Two quarters plus one quarter are three quarters. You count the coins, and they are still <strong>quarters</strong>: putting them together does not change the size of each coin. Fractions work the same way:</p>
<p style="text-align:center">2 fourths + 1 fourth = 3 fourths, &nbsp; or &nbsp; {F(2, 4)} + {F(1, 4)} = {F(3, 4)}</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea</span>
<p>To add or subtract fractions, the parts must be <strong>the same size</strong> (the same denominator). Then you add or subtract only the <strong>numerators</strong>. The denominator stays the same.</p>
</div>
<p>But what if the parts are different sizes, like halves and thirds? You cannot count them together until you cut them into parts of the same size. You already know how: with <strong>equivalent fractions</strong>.</p>
</section>

<section>
<h2 id="s-same"><span aria-hidden="true" class="num-seccion">2</span>The same denominator</h2>
<p>When the denominators are the same, add (or subtract) the numerators and keep the denominator.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(2, 5)} + {F(1, 5)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> The denominators are the same (5): the parts are fifths.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Add the numerators: 2 + 1 = 3.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(2, 5)} + {F(1, 5)} = {F(3, 5)}. The parts are still fifths.</p>
</div>
{bar2(2, 1, 5, "A bar divided into 5 equal parts: 2 parts in dark purple and 1 part in light purple are shaded. Together they are 3 fifths.")}
<p style="text-align:center"><strong>2 fifths</strong> (dark) + <strong>1 fifth</strong> (light) = <strong>3 fifths</strong></p>
<p>Subtracting works the same way. A board is {F(5, 8)} inch thick, and you sand off {F(2, 8)} inch. Now it is 5 − 2 = 3 eighths: {F(3, 8)} inch thick.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out!</span>
<p><strong>Never add the denominators.</strong> {F(2, 5)} + {F(1, 5)} is <strong>not</strong> {F(3, 10)}. Here is a quick way to catch that mistake: {F(3, 10)} is <strong>less</strong> than the {F(2, 5)} you started with. If you add something to {F(2, 5)}, the answer must be <strong>more</strong> than {F(2, 5)}. Always ask yourself if your answer makes sense.</p>
</div>
{practica("p1", "Practice 1 — Add with the same denominator", f"What is {F(3, 8)} + {F(2, 8)}?", [("a", F(5, 16)), ("b", F(5, 8)), ("c", F(6, 8)), ("d", F(1, 8))])}
{practica("p2", "Practice 2 — Subtract with the same denominator", f"What is {F(7, 9)} − {F(4, 9)}?", [("a", F(3, 9)), ("b", F(3, 0)), ("c", F(11, 9)), ("d", F(3, 18))])}
{enlace("same-denominator", "the same denominator", "Join and take away parts with the bars, and add or subtract fractions with the same denominator.")}
</section>

<section>
<h2 id="s-different"><span aria-hidden="true" class="num-seccion">3</span>Different denominators</h2>
<p>When the denominators are different, the parts are different sizes. First, change the fractions to <strong>equivalent fractions with the same denominator</strong> (a <strong>common denominator</strong>). Then add or subtract the numerators.</p>
<h3>How to find a common denominator</h3>
<p>Go through the <strong>multiples of the larger denominator</strong> (2 times, 3 times, …) until you find one that the smaller denominator also goes into. If you do not find one quickly, <strong>multiplying the two denominators always works</strong>. You may get bigger numbers, but you can simplify at the end.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(1, 2)} + {F(1, 3)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Find a common denominator. Multiples of 3: 3, 6, … The number 2 does not go into 3, but it does go into 6. The common denominator is <strong>6</strong>.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Change each fraction to sixths: {F(1, 2)} = {F(3, 6)} (× 3), and {F(1, 3)} = {F(2, 6)} (× 2).</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> Now the parts are the same size. Add the numerators: 3 + 2 = 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(1, 2)} + {F(1, 3)} = {F(3, 6)} + {F(2, 6)} = {F(5, 6)}.</p>
</div>
{bar(1, 2, "A bar divided into 2 equal parts with 1 part shaded: one half.")}
{bar(1, 3, "A bar of the same size divided into 3 equal parts with 1 part shaded: one third.", "#ce93d8")}
{bar2(3, 2, 6, "A bar of the same size divided into 6 equal parts: 3 sixths in dark purple (the half) and 2 sixths in light purple (the third). Together they are 5 sixths.")}
<p style="text-align:center">Cut into sixths, the half is <strong>3 sixths</strong> and the third is <strong>2 sixths</strong>: together, <strong>5 sixths</strong>.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(3, 4)} − {F(1, 8)} (inches on a ruler)</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> 8 is a multiple of 4 (4 × 2 = 8). The common denominator is <strong>8</strong>.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> Change {F(3, 4)} to eighths: {F(3, 4)} = {F(6, 8)}. The {F(1, 8)} stays as it is.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Step 3.</strong> Subtract the numerators: 6 − 1 = 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(3, 4)} − {F(1, 8)} = {F(6, 8)} − {F(1, 8)} = {F(5, 8)} inch.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator adds fractions and shows the answer in simplest form. To check {F(1, 2)} + {F(1, 3)}:</p>
<ol>
<li>Press {T("n/d")}, type {T("1")}, go down with {T("▼")}, type {T("2")}, and leave with {T("►")}.</li>
<li>Press {T("+")}.</li>
<li>Press {T("n/d")}, type {T("1")}, go down with {T("▼")}, type {T("3")}, and leave with {T("►")}.</li>
<li>Press {T("enter")}. The screen shows {F(5, 6)}.</li>
</ol>
<p>Work it out on paper first, then check. On the GED you will need to know the steps, not only the answer.</p>""")}
{practica("p3", "Practice 3 — Find a common denominator", f"To add {F(1, 4)} + {F(1, 6)}, what is the smallest common denominator?", [("a", "10"), ("b", "12"), ("c", "24 is the only one possible"), ("d", "2")])}
{practica("p4", "Practice 4 — Add with different denominators", f"What is {F(1, 2)} + {F(1, 4)}?", [("a", F(2, 6)), ("b", F(3, 4)), ("c", F(2, 4)), ("d", F(1, 6))])}
{enlace("different-denominators", "different denominators", "See each step: the common denominator, the equivalent fractions, and the result with bars.")}
<a class="enlace-interactivo" href="lesson-4-1-gcf-lcm.html#s-lcm" aria-label="Open the complement: the least common multiple (LCM)">
<span class="ei-icono" aria-hidden="true">📘</span>
<span class="ei-cuerpo"><span class="ei-titulo">The smallest common denominator is the LCM</span><span class="ei-sub">The least common multiple (LCM) of the two denominators is the smallest common denominator. Review how to find it in the complement to Lesson 4.1.</span><span class="ei-cta">Open the complement <span aria-hidden="true">›</span></span></span>
</a>
</section>

<section>
<h2 id="s-simplify"><span aria-hidden="true" class="num-seccion">4</span>Simplify the result</h2>
<p>After you add or subtract, look at the answer. If it can be simplified, simplify it, just as you learned in Lesson 4.1.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: {F(1, 6)} + {F(1, 6)}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Step 1.</strong> Same denominator: 1 + 1 = 2. So {F(1, 6)} + {F(1, 6)} = {F(2, 6)}.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Step 2.</strong> 2 and 6 can both be divided by 2: {F(2, 6)} = {F(1, 3)}.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Result.</strong> {F(1, 6)} + {F(1, 6)} = {F(1, 3)}.</p>
</div>
<h3>When the answer is more than 1</h3>
<p>Sometimes the numerator ends up greater than the denominator. For example, {F(3, 4)} + {F(2, 4)} = {F(5, 4)}. A fraction like {F(5, 4)} is called an <strong>improper fraction</strong>: it is more than one whole.</p>
{bar(4, 4, "A bar divided into 4 equal parts, all 4 shaded: one whole.")}
{bar(1, 4, "A second bar of the same size divided into 4 equal parts with 1 part shaded: one fourth more.")}
<p>Four fourths make <strong>one whole</strong>, and there is <strong>one fourth</strong> left over. So {F(5, 4)} is the same as 1 and {F(1, 4)}, written <strong>1&nbsp;{F(1, 4)}</strong>. A number like this, with a whole number and a fraction, is called a <strong>mixed number</strong>. To find it, divide: 5 ÷ 4 = 1 with remainder 1.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">On the GED</span>
<p>The answer choices are almost always in <strong>simplest form</strong>. If your answer is {F(3, 6)} and you do not see it among the choices, simplify it: look for {F(1, 2)}.</p>
</div>
{enlace("simplify-result", "simplify the result", "Add or subtract, then simplify, and write the result as a mixed number when it is more than 1.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">5</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-4-2.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Write and solve ten operations: five with the same denominator and five with different denominators. Mix additions and subtractions. Simplify each answer, and write any improper fraction as a mixed number. Then check each one: does the answer make sense? A sum must be more than each fraction you added.</li>
<li><strong>In your day.</strong> You spend {F(1, 4)} hour on the bus, {F(1, 2)} hour cooking, and {F(1, 3)} hour helping with homework. How many hours is that in all? Write the answer as a mixed number, and then in hours and minutes. (Hint: the common denominator is 12, and 1 hour = 60 minutes.)</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">6</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. Questions with only two choices show the explanation right away. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "When you add two fractions with the <strong>same denominator</strong>, what happens to the denominator?", [("a", "It stays the same."), ("b", "The two denominators are added."), ("c", "The two denominators are multiplied."), ("d", "It becomes the sum of the numerators.")])}
{quiz("B", f"What is {F(2, 7)} + {F(3, 7)}?", [("a", F(5, 14)), ("b", F(6, 7)), ("c", F(5, 49)), ("d", F(5, 7))])}
{quiz("C", f"What is {F(5, 6)} − {F(2, 6)}, in simplest form?", [("a", F(3, 12)), ("b", F(7, 6)), ("c", F(1, 2)), ("d", F(3, 0))])}
{quiz("D", f"To add {F(1, 3)} + {F(1, 6)}, what is the smallest common denominator?", [("a", "9"), ("b", "6"), ("c", "3"), ("d", "5")])}
{quiz("E", f"What is {F(1, 2)} + {F(1, 3)}?", [("a", F(2, 5)), ("b", F(2, 6)), ("c", F(1, 6)), ("d", F(5, 6))])}
{quiz("F", f"What is {F(3, 4)} − {F(1, 8)}?", [("a", F(5, 8)), ("b", F(2, 4)), ("c", F(2, 8)), ("d", F(7, 8))])}
{quiz("G", f"What is the simplest form of {F(4, 8)}?", [("a", F(4, 8)), ("b", F(1, 2)), ("c", F(2, 8)), ("d", F(8, 4))])}
{quiz("H", f"Rosa reads for {F(1, 4)} hour and then studies for {F(1, 2)} hour. How long is that in all?", [("a", f"{F(2, 6)} hour"), ("b", f"{F(1, 6)} hour"), ("c", f"{F(3, 4)} hour"), ("d", f"{F(2, 4)} hour")])}
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
<div aria-label="Self-check checklist for adding and subtracting fractions (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for adding and subtracting fractions and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Add and subtract with the same denominator</th><td>I add or subtract only the numerators, and I can explain why.</td><td>I get it right, but sometimes I am tempted to add the denominators.</td><td>I add or subtract the denominators too.</td></tr>
<tr><th scope="row">Find a common denominator</th><td>I find the smallest one quickly.</td><td>I find one that works, but not always the smallest.</td><td>I add the denominators, or I do not know where to start.</td></tr>
<tr><th scope="row">Add and subtract with different denominators</th><td>I change both fractions and operate with no mistakes.</td><td>I find the common denominator, but I make mistakes when I change the numerators.</td><td>I operate without making the denominators the same.</td></tr>
<tr><th scope="row">Simplify and check the result</th><td>I always simplify, write mixed numbers, and check that the answer makes sense.</td><td>I simplify most of the time.</td><td>I leave the answer without simplifying, and I do not check it.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You can now add and subtract fractions, with the same or different denominators, and simplify the result. The hardest part of working with fractions is behind you.</p>
<p>In <strong>Lesson 4.3 · Multiplying and dividing fractions</strong> you will see something that surprises many students: to multiply and divide fractions, you <strong>do not need</strong> a common denominator. Then, in Lesson 4.4, you will work with mixed numbers like the 1&nbsp;{F(1, 4)} you met today.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: <a href="lesson-4-3.html">Lesson 4.3 · Multiplying and dividing fractions</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>like denominators</dt><dd>Fractions with the same denominator, like 2/5 and 1/5. Their parts are the same size.</dd>
<dt>unlike denominators</dt><dd>Fractions with different denominators, like 1/2 and 1/3. Their parts are different sizes.</dd>
<dt>common denominator</dt><dd>A denominator that two fractions can share. It is a multiple of both denominators.</dd>
<dt>least common denominator</dt><dd>The smallest common denominator. It is the LCM of the denominators.</dd>
<dt>improper fraction</dt><dd>A fraction whose numerator is greater than or equal to its denominator, like 5/4. It is 1 or more.</dd>
<dt>mixed number</dt><dd>A whole number and a fraction together, like 1 1/4.</dd>
<dt>simplest form</dt><dd>A fraction whose top and bottom share no factor greater than 1, like 1/3.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 4 · Lesson 4.2</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-4-2.html"), "w", encoding="utf-8").write(html)
print("ok")
