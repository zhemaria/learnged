"""Builds math/level-1/lesson-5-2.html (English). Run tools/ged_standards.py afterwards
to add the standards box."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def T(*keys):
    return "".join(f'<span class="{"tecla num" if k in list("0123456789.") else ("tecla dos" if k == "2nd" else "tecla")}">{k}</span>' for k in keys)

def opciones(pid, items):
    btn = "\n".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n{opciones(pid, items)}\n</div>'

def enlace(ancla, titulo, sub, href=None):
    href = href or f"practice-5-2.html#{ancla}"
    return f'''<a class="enlace-interactivo" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="Open the practice activity: {titulo} (opens in a new tab)">
<span class="ei-icono" aria-hidden="true">🔗</span>
<span class="ei-cuerpo"><span class="ei-titulo">Practice more: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">Open the activity <span aria-hidden="true">›</span></span></span>
</a>'''

def calc(titulo, cuerpo):
    return f'<div class="caja-calc">\n<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>\n{cuerpo}\n<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> Open the calculator</button>\n</div>'

def quiz(q, pregunta, items):
    btn = "".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">Question {q}</p>\n<p class="pregunta" id="t-q{q}">{pregunta}</p>\n<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>'

def E(t):
    """An expression or equation in algebra style."""
    return f'<span class="ec">{t}</span>'

def balanza(izq, der, label):
    """A balanced scale: left pan shows a box and + izq, right pan shows der."""
    cx, cy, L = 320, 60, 210
    s = [f'<polygon points="{cx - 34},236 {cx + 34},236 {cx},{cy + 8}" fill="#90a4ae"/>',
         f'<line x1="{cx - L}" y1="{cy}" x2="{cx + L}" y2="{cy}" stroke="#37474f" stroke-width="7" stroke-linecap="round"/>',
         f'<circle cx="{cx}" cy="{cy}" r="9" fill="#37474f"/>']
    for x in (cx - L, cx + L):
        s.append(f'<line x1="{x}" y1="{cy}" x2="{x - 70}" y2="{cy + 80}" stroke="#78909c" stroke-width="2"/><line x1="{x}" y1="{cy}" x2="{x + 70}" y2="{cy + 80}" stroke="#78909c" stroke-width="2"/>')
        s.append(f'<rect x="{x - 88}" y="{cy + 80}" width="176" height="11" rx="5" fill="#37474f"/>')
    xl, xr = cx - L, cx + L
    s.append(f'<rect x="{xl - 76}" y="{cy + 28}" width="56" height="50" rx="7" fill="#1565c0"/><text x="{xl - 48}" y="{cy + 61}" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">?</text>')
    s.append(f'<rect x="{xl + 4}" y="{cy + 28}" width="70" height="50" rx="7" fill="#cfd8dc"/><text x="{xl + 39}" y="{cy + 61}" text-anchor="middle" font-size="24" font-weight="700" fill="#1a2330">{izq}</text>')
    s.append(f'<rect x="{xr - 40}" y="{cy + 28}" width="80" height="50" rx="7" fill="#cfd8dc"/><text x="{xr}" y="{cy + 61}" text-anchor="middle" font-size="24" font-weight="700" fill="#1a2330">{der}</text>')
    s.append(f'<text x="{xl}" y="{cy + 124}" text-anchor="middle" font-size="22" font-weight="700" fill="#0d47a1">□ + {izq}</text><text x="{xr}" y="{cy + 124}" text-anchor="middle" font-size="22" font-weight="700" fill="#0d47a1">{der}</text>')
    return f'<svg viewBox="0 0 640 246" role="img" aria-label="{label}" style="width:100%;max-width:560px;height:auto;display:block;margin:12px auto;">{"".join(s)}</svg>'

LESSON = {
 "next": "Lesson 5.3", "review": "sections 2, 4, and 5",
 "practice": {
  "p1": {"ok": "d", "hints": {
      "a": "9 − x means 9 minus a number. \"Increased by\" means the number gets bigger: add 9.",
      "b": "9x means 9 times a number. \"Increased by 9\" means add 9, not multiply.",
      "c": "x ÷ 9 means a number divided by 9. \"Increased by\" means the number gets bigger: add 9."},
   "right": "\"Increased by\" means add: x + 9.",
   "solution": "\"A number\" is x, and \"increased by 9\" means add 9. So the expression is x + 9."},
  "p2": {"ok": "a", "hints": {
      "b": "x + 3 means a number plus 3. \"Three times\" means multiply by 3.",
      "c": "x ÷ 3 is a third of a number. \"Three times\" means multiply by 3.",
      "d": "x − 3 means a number minus 3. \"Three times\" means multiply by 3."},
   "right": "Three times x is written 3x: the 3 right next to the x means multiply.",
   "solution": "\"Three times a number\" means 3 × x. In algebra we write it 3x, with no sign between the 3 and the x."},
  "p3": {"ok": "d", "hints": {
      "a": "21 is 15 + 6. The x has + 6 with it, so undo it with the inverse: subtract 6.",
      "b": "6 is the number added to x, not the value of x. Subtract 6 from both sides.",
      "c": "90 is 15 × 6. The x has + 6 with it, so the inverse operation is subtract 6."},
   "right": "x + 6 − 6 = 15 − 6, so x = 9. Check: 9 + 6 = 15.",
   "solution": "The x has + 6 with it. The inverse of adding is subtracting, so subtract 6 from both sides: x = 15 − 6 = 9. Check: 9 + 6 = 15."},
  "p4": {"ok": "a", "hints": {
      "b": "21 is 18 + 3. 3x means 3 times x, so the inverse operation is divide by 3.",
      "c": "15 is 18 − 3. 3x means 3 times x, so the inverse operation is divide by 3.",
      "d": "54 is 18 × 3. You used the same operation. Undo the multiplication: divide by 3."},
   "right": "3x ÷ 3 = 18 ÷ 3, so x = 6. Check: 3 × 6 = 18.",
   "solution": "3x means 3 times x. The inverse of multiplying is dividing, so divide both sides by 3: x = 18 ÷ 3 = 6. Check: 3 × 6 = 18."},
 },
 "quiz": {
  "A": {"ok": "d", "hints": {"a": "The equal sign says that both sides have the same value. It is not the number we are looking for.", "b": "An unknown can be any number. We find its value by solving the equation.", "c": "The result of an addition is a sum. The unknown is the number we do not know yet."},
        "solution": "An unknown is a number we do not know yet. We write it with a symbol, like □ or x."},
  "B": {"ok": "c", "hints": {"a": "Careful with \"less than\": it takes 8 away from the number, so the number comes first: x − 8.", "b": "8x means 8 times a number. \"Less than\" means subtract.", "d": "x + 8 is 8 more than a number. \"Less than\" means subtract."},
        "solution": "\"8 less than a number\" means take 8 away from the number: x − 8. The order changes from the words: the number comes first."},
  "C": {"ok": "b", "hints": {"a": "2 plus x is written 2 + x, with a plus sign.", "c": "x minus 2 is written x − 2.", "d": "x divided by 2 is written x ÷ 2."},
        "solution": "When a number and a letter are written together, they are multiplied: 2x means 2 × x."},
  "D": {"ok": "a", "hints": {"b": "Adding 7 makes the left side x + 14. Undo the + 7 with its inverse: subtract 7.", "c": "The x is added to 7, not multiplied. Undo adding with subtracting.", "d": "10 is the other side, not what is with the x. Undo the + 7: subtract 7."},
        "solution": "The x has + 7 with it. The inverse of adding 7 is subtracting 7. Subtract 7 from both sides: x = 10 − 7 = 3."},
  "E": {"ok": "c", "hints": {"a": "16 is 12 + 4. Undo the + 4 with its inverse: subtract 4.", "b": "3 is 12 ÷ 4. The x is added to 4, not multiplied. Subtract 4.", "d": "48 is 12 × 4. The x has + 4 with it: subtract 4."},
        "solution": "Subtract 4 from both sides: x = 12 − 4 = 8. Check: 8 + 4 = 12."},
  "F": {"ok": "a", "hints": {"b": "40 is 35 + 5. 5x means 5 times x, so divide by 5.", "c": "30 is 35 − 5. 5x means 5 times x, so divide by 5.", "d": "175 is 35 × 5. Undo the multiplication with its inverse: divide by 5."},
        "solution": "5x means 5 times x. Divide both sides by 5: x = 35 ÷ 5 = 7. Check: 5 × 7 = 35."},
  "G": {"ok": "a", "hints": {"b": "Adding 8 and 12 does not test the equation. Put 8 in place of x.", "c": "8 − 4 is not in the equation. Put 8 in place of x and calculate x + 4.", "d": "You can always check: put the number in place of x and see if both sides are equal."},
        "solution": "To check, substitute: put 8 in place of x. 8 + 4 = 12, and the right side is 12. Both sides are equal, so x = 8 is right."},
  "H": {"ok": "b", "hints": {"a": "The worker earned $50, so the money went up: add 50, do not subtract.", "c": "50x means 50 times the money. The worker earned $50 more: add.", "d": "The $200 is what the worker has at the end, so it goes alone on one side: x + 50 = 200."},
        "solution": "The worker had x dollars, earned $50 more (+ 50), and now has $200: x + 50 = 200. Solving it: x = 200 − 50 = 150."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 5.2 · Math Level 1 (English) — built by tools/build_lesson_5_2.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 5.2 · Algebraic language and simple unknowns · LearnGED</title>
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
<p class="ruta">Math · Level 1 · Topic 5 — Patterns and algebraic thinking</p>
<h1>Lesson 5.2 · Algebraic language and simple unknowns</h1>
<p class="lema">Write with symbols what we used to say with words. Math starts to use its own language.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">⚖️</span> The balance model</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Translate</strong> phrases in words into algebraic language.</li>
<li><strong>Write</strong> one-step equations with an unknown (a box □ or a letter x).</li>
<li><strong>Solve</strong> one-step equations with the inverse operation.</li>
<li><strong>Check</strong> the solution by substituting the value you found.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-language">The language of algebra</a></li>
<li><a href="#s-translate">Translate words into symbols</a></li>
<li><a href="#s-balance">The equation: a balanced scale</a></li>
<li><a href="#s-inverse">Solve with the inverse operation</a></li>
<li><a href="#s-check">Check the solution</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-language"><span aria-hidden="true" class="num-seccion">1</span>The language of algebra</h2>
<p>In <strong>Lesson 5.1</strong> you found the rules of patterns and said them <strong>in words</strong>: "add 5 each time," "the output is the input times 3." That works, but it is long.</p>
<p>Algebra gives us a shorter and more exact way: <strong>write those ideas with symbols</strong>. Instead of saying "a number plus five," we write {E("x + 5")}. It means the same thing, but in the language of math.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The unknown</span>
<p>An <strong>unknown</strong> is a number we do not know yet. We show it with a symbol: a box <strong>□</strong> or a letter like <strong>x</strong> or <strong>n</strong>. The unknown is not an impossible mystery: it is simply "the number we want to find."</p>
</div>
</section>

<section>
<h2 id="s-translate"><span aria-hidden="true" class="num-seccion">2</span>Translate words into symbols</h2>
<p>To write in algebraic language, find the operation that each phrase points to. This is your translation table:</p>
<div aria-label="Phrases and their algebraic expressions (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">Translating phrases in words into algebraic language</caption>
<thead><tr><th scope="col">Phrase in words</th><th scope="col">In algebraic language</th></tr></thead>
<tbody>
<tr><td>A number <strong>plus</strong> 7 · a number <strong>increased by</strong> 7 · 7 <strong>more than</strong> a number</td><td class="expr">x + 7</td></tr>
<tr><td>A number <strong>minus</strong> 5 · a number <strong>decreased by</strong> 5 · 5 <strong>less than</strong> a number</td><td class="expr">x − 5</td></tr>
<tr><td><strong>Twice</strong> a number · <strong>two times</strong> a number</td><td class="expr">2x</td></tr>
<tr><td><strong>Three times</strong> a number</td><td class="expr">3x</td></tr>
<tr><td>A number <strong>divided by</strong> 4</td><td class="expr">x ÷ 4</td></tr>
<tr><td>A number <strong>is equal to</strong> 12 · a number <strong>is</strong> 12</td><td class="expr">x = 12</td></tr>
</tbody>
</table></div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out! Two traps</span>
<p><strong>Twice is written together.</strong> "Twice x" is written {E("2x")}, with no sign between the 2 and the x. In algebra, a number and a letter written <strong>together</strong> are multiplied: {E("2x")} means "2 times x."</p>
<p><strong>"Less than" changes the order.</strong> "5 less than a number" means take 5 away from the number, so the number comes first: {E("x − 5")}, not {E("5 − x")}.</p>
</div>
{practica("p1", "Practice 1 — Translate into symbols", 'How do you write "a number increased by 9" in algebraic language?', [("a", "9 − x"), ("b", "9x"), ("c", "x ÷ 9"), ("d", "x + 9")])}
{practica("p2", "Practice 2 — Translate into symbols", 'How do you write "three times a number"?', [("a", "3x"), ("b", "x + 3"), ("c", "x ÷ 3"), ("d", "x − 3")])}
{enlace("translate", "translate words into symbols", 'Turn phrases like "a number plus five" into expressions with x.')}
</section>

<section>
<h2 id="s-balance"><span aria-hidden="true" class="num-seccion">3</span>The equation: a balanced scale</h2>
<p>An <strong>equation</strong> says that two things are equal: what is on one side of the <strong>=</strong> sign has the same value as what is on the other side. The best way to picture it is a <strong>balanced scale</strong>.</p>
{balanza(3, 8, "A balanced scale. On the left pan there is a box with an unknown number and a weight of 3. On the right pan there is a weight of 8. The scale is level: box plus 3 equals 8.")}
<p style="text-align:center;font-size:14px;color:#4a5462">The scale is level: the left side weighs the same as the right side.</p>
<p>In the equation {E("□ + 3 = 8")}, the box hides a number. Because the scale is balanced, that number must make the left side worth 8. What number plus 3 gives 8? The number <strong>5</strong>.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea of this lesson</span>
<p><strong>To solve an equation</strong> is to find the value of the unknown that keeps the scale balanced: the number that makes the equation true.</p>
</div>
{enlace("balance", "the equation as a scale", "Try numbers in the box and see which one keeps the scale level.")}
</section>

<section>
<h2 id="s-inverse"><span aria-hidden="true" class="num-seccion">4</span>Solve with the inverse operation</h2>
<p>With easy equations you can guess, but there is a sure method that always works: use the <strong>inverse operation</strong>. Remember from Topics 1 and 2: subtraction undoes addition, and division undoes multiplication.</p>
<p>The idea is to <strong>get the unknown alone</strong>. To do that, use the inverse of the operation that is with it.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: solve {E("□ + 3 = 8")}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Look at the unknown.</strong> It is <em>added</em> to 3. The inverse of adding is <strong>subtracting</strong>.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Subtract 3 from both sides</strong>, so the scale stays balanced: □ + 3 − 3 = 8 − 3.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Simplify.</strong> On the left, + 3 − 3 cancel out, and the unknown is alone: □ = 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Solution.</strong> □ = <strong>5</strong>.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: solve {E("4x = 20")}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Look at the unknown.</strong> It is <em>multiplied</em> by 4. The inverse of multiplying is <strong>dividing</strong>.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Divide both sides by 4:</strong> 4x ÷ 4 = 20 ÷ 4.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Simplify.</strong> On the left, the x is alone: x = 5.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Solution.</strong> x = <strong>5</strong>.</p>
</div>
<p>The same idea works for the other two operations: addition undoes subtraction, and multiplication undoes division.</p>
<div aria-label="The inverse operation for each kind of equation (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">The inverse operation for each kind of one-step equation</caption>
<thead><tr><th scope="col">Equation</th><th scope="col">The x is…</th><th scope="col">Do this to both sides</th></tr></thead>
<tbody>
<tr><td class="expr">x + 3 = 8</td><td>added to 3</td><td>subtract 3: x = 8 − 3 = 5</td></tr>
<tr><td class="expr">x − 4 = 10</td><td>minus 4</td><td>add 4: x = 10 + 4 = 14</td></tr>
<tr><td class="expr">4x = 20</td><td>multiplied by 4</td><td>divide by 4: x = 20 ÷ 4 = 5</td></tr>
<tr><td class="expr">x ÷ 3 = 6</td><td>divided by 3</td><td>multiply by 3: x = 6 × 3 = 18</td></tr>
</tbody>
</table></div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">The rule of the scale</span>
<p>Whatever you do to one side of the equation, <strong>do it to the other side too</strong>. If you subtract 3 on the left, subtract 3 on the right. That way the scale never tips, and the equation stays true.</p>
</div>
{practica("p3", "Practice 3 — Solve an addition equation", f"Solve: {E('x + 6 = 15')}", [("a", "x = 21"), ("b", "x = 6"), ("c", "x = 90"), ("d", "x = 9")])}
{practica("p4", "Practice 4 — Solve a multiplication equation", f"Solve: {E('3x = 18')}", [("a", "x = 6"), ("b", "x = 21"), ("c", "x = 15"), ("d", "x = 54")])}
{enlace("inverse-operation", "solve with the inverse operation", "Get the unknown alone by undoing the operation that is with it, step by step.")}
</section>

<section>
<h2 id="s-check"><span aria-hidden="true" class="num-seccion">5</span>Check the solution</h2>
<p>After you solve, there is a simple way to know if you are right: <strong>substitute</strong>. That means you put the value you found in place of the unknown and see if the equation is true.</p>
<div class="ejemplo">
<p class="titulo-ej">Example: check that x = 9 solves {E("x + 6 = 15")}</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Substitute.</strong> Put 9 in place of x in the original equation: 9 + 6 = 15.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Calculate the left side.</strong> 9 + 6 = 15.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Compare.</strong> 15 = 15. Both sides are equal, so <strong>x = 9 is the right solution</strong>.</p>
</div>
<div class="caja caja-tip">
<span class="etiqueta et-verde">A good habit</span>
<p>Checking by substituting works like checking with the inverse operation in Topics 1 and 2: it tells you that your answer is right, with no one else checking it for you.</p>
</div>
{calc("Check it on the calculator", f"""<p>You can substitute with the calculator. Type the left side with your value in place of x, and compare the answer with the right side.</p>
<ol>
<li>Does x = 5 solve {E("4x = 20")}? Type {T("4")} {T("×")} {T("5")} {T("enter")}. The screen shows 20, the same as the right side: yes.</li>
<li>Does x = 18 solve {E("x ÷ 3 = 6")}? Type {T("1")}{T("8")} {T("÷")} {T("3")} {T("enter")}. The screen shows 6: yes.</li>
</ol>""")}
{enlace("check", "check the solution", "Put the value in place of x and see if both sides are equal.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">6</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-5-2.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Translate ten phrases into symbols: "twice a number," "5 less than a number," "a number divided by 3," and so on. Then go the other way: take {E("x + 12 = 40")} and write a real situation that this equation describes. Solve it and check it.</li>
<li><strong>In your daily life.</strong> Think of a situation of your own with a number you do not know: "I had some money, I spent $20, and I have $35 left. How much did I have?" Write it as an equation, solve it with the inverse operation, and check it by substituting.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">7</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "What is an unknown in an equation?", [("a", "The equal sign."), ("b", "A number that is always zero."), ("c", "The result of an addition."), ("d", "A number we do not know yet, shown with a symbol.")])}
{quiz("B", 'How do you write "8 less than a number" in algebraic language?', [("a", "8 − x"), ("b", "8x"), ("c", "x − 8"), ("d", "x + 8")])}
{quiz("C", f"The expression {E('2x')} means:", [("a", "2 plus x"), ("b", "2 times x"), ("c", "x minus 2"), ("d", "x divided by 2")])}
{quiz("D", f"To solve {E('x + 7 = 10')}, what do you do to both sides?", [("a", "Subtract 7."), ("b", "Add 7."), ("c", "Multiply by 7."), ("d", "Divide by 10.")])}
{quiz("E", f"Solve: {E('x + 4 = 12')}", [("a", "x = 16"), ("b", "x = 3"), ("c", "x = 8"), ("d", "x = 48")])}
{quiz("F", f"Solve: {E('5x = 35')}", [("a", "x = 7"), ("b", "x = 40"), ("c", "x = 30"), ("d", "x = 175")])}
{quiz("G", f"To check that x = 8 solves {E('x + 4 = 12')}, you should:", [("a", "Put 8 in place of x and see that 8 + 4 = 12."), ("b", "Add 8 + 12."), ("c", "Subtract 8 − 4."), ("d", "You cannot check it.")])}
{quiz("H", '"A worker had some money, earned $50, and now has $200." If x is the money the worker had, which equation shows this situation?', [("a", "x − 50 = 200"), ("b", "x + 50 = 200"), ("c", "50x = 200"), ("d", "x + 200 = 50")])}
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
<div aria-label="Self-check checklist for algebraic language and one-step equations (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for algebraic language and one-step equations and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Translate phrases into algebraic language</th><td>I translate addition, subtraction, multiplication, and division exactly, including "less than."</td><td>I translate most phrases correctly.</td><td>I only translate simple additions, or I mix up the order.</td></tr>
<tr><th scope="row">Write the right equation</th><td>I write the equation with the unknown in the right place.</td><td>I write the equation correctly most of the time.</td><td>I am not sure where the numbers and the unknown go.</td></tr>
<tr><th scope="row">Solve with the inverse operation</th><td>I use the inverse operation on both sides with no mistakes.</td><td>I solve correctly, with an occasional slip.</td><td>I use the same operation instead of the inverse one.</td></tr>
<tr><th scope="row">Check the solution</th><td>I substitute the value and check the equation on my own, every time.</td><td>I check when someone asks me to.</td><td>I do not check, or I substitute in the wrong place.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You can now translate phrases into algebraic language, write one-step equations, solve them with the inverse operation, and check the solution. You have taken your first steps in algebra.</p>
<p>In <strong>Lesson 5.3 · One-step word problems</strong> you will put together everything you learned in Level 1: you will read a problem in words, decide which of the four operations to use, write it as an equation with an unknown, and solve it. That lesson closes Topic 5.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: Lesson 5.3 · One-step word problems</p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>unknown (variable)</dt><dd>A number we do not know yet, shown with a box □ or a letter like x.</dd>
<dt>expression</dt><dd>Numbers, letters, and operation signs with no equal sign, like x + 5 or 3x.</dd>
<dt>equation</dt><dd>A statement that two things are equal, with an equal sign, like x + 3 = 8.</dd>
<dt>solve</dt><dd>To find the value of the unknown that makes the equation true.</dd>
<dt>inverse operation</dt><dd>The operation that undoes another one: subtraction undoes addition, and division undoes multiplication (and the other way around).</dd>
<dt>substitute</dt><dd>To put a number in place of the unknown, for example to check a solution.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.2</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-5-2.html"), "w", encoding="utf-8").write(html)
print("ok")
