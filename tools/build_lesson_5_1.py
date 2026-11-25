"""Builds math/level-1/lesson-5-1.html (English). Run tools/ged_standards.py afterwards
to add the standards box."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def T(*keys):
    return "".join(f'<span class="{"tecla num" if k in list("0123456789.") else ("tecla dos" if k == "2nd" else "tecla")}">{k}</span>' for k in keys)

def seq(terms, jump, word):
    """Sequence chain: terms with the jump between them; None is the unknown term."""
    parts, spoken = [], []
    for i, t in enumerate(terms):
        if i:
            parts.append(f'<div class="salto" aria-hidden="true">{jump}</div>')
        parts.append(f'<div class="term incog" aria-hidden="true">?</div>' if t is None else f'<div class="term" aria-hidden="true">{t}</div>')
        spoken.append("unknown term" if t is None else str(t))
    label = f"Pattern: {f', {word}, '.join(spoken)}."
    return f'<div class="secuencia" role="img" aria-label="{label}">\n' + "\n".join(parts) + '\n</div>'

def squares(label):
    """Figures 1, 2, 3 of the growing-squares pattern (1, 4, 9 squares)."""
    u, gap, out, x = 26, 64, [], 20
    alto = 3 * u
    for n in (1, 2, 3):
        for i in range(n):
            for j in range(n):
                out.append(f'<rect x="{x + i * u}" y="{10 + alto - (j + 1) * u}" width="{u - 3}" height="{u - 3}" rx="3" fill="#1565c0"/>')
        out.append(f'<text x="{x + n * u / 2 - 1.5:.1f}" y="{alto + 36}" text-anchor="middle" font-size="15" fill="#1a2330">Figure {n}</text>')
        out.append(f'<text x="{x + n * u / 2 - 1.5:.1f}" y="{alto + 56}" text-anchor="middle" font-size="15" font-weight="700" fill="#0d47a1">{n * n} square{"s" if n > 1 else ""}</text>')
        x += n * u + gap
    W = x - gap + 20
    return f'<svg viewBox="0 0 {W} {alto + 66}" role="img" aria-label="{label}" style="width:100%;max-width:{W * 1.25:.0f}px;height:auto;display:block;margin:10px auto;">{"".join(out)}</svg>'

def opciones(pid, items):
    btn = "\n".join(f'<button class="opcion" data-k="{k}" type="button">{t}</button>' for k, t in items)
    return f'<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>'

def practica(pid, titulo, pregunta, items):
    return f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n{opciones(pid, items)}\n</div>'

def enlace(ancla, titulo, sub, href=None):
    href = href or f"practice-5-1.html#{ancla}"
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
 "next": "Lesson 5.2", "review": "sections 2, 3, and 4",
 "practice": {
  "p1": {"ok": "c", "hints": {
      "a": "21 is 19 + 2. Look at the jump again: from 7 to 11 is + 4.",
      "b": "24 is 19 + 5. Check the jump: 11 − 7 = 4, and 15 − 11 = 4.",
      "d": "38 is 19 × 2. These numbers grow slowly and evenly, so the rule adds; it does not multiply."},
   "right": "The rule is add 4 each time: 19 + 4 = 23.",
   "solution": "The jump is + 4 every time: 7, 11, 15, 19. So the next term is 19 + 4 = 23."},
  "p2": {"ok": "b", "hints": {
      "a": "12 is 10 + 2. Find the jump first: from 5 to 10 is + 5.",
      "c": "Check the jump: from 5 to 10 is + 5, and from 20 to 25 is + 5 too.",
      "d": "18 is too close to 20. The jump is + 5, so the missing term is 10 + 5."},
   "right": "The rule is add 5 each time: 10 + 5 = 15, and 15 + 5 = 20.",
   "solution": "The jump is + 5 (5 → 10 and 20 → 25). The missing term comes after 10: 10 + 5 = 15. Check: 15 + 5 = 20."},
  "p3": {"ok": "a", "hints": {
      "b": "13 is 12 + 1. Count the jump between figures: 3 → 6 is + 3.",
      "c": "16 is 12 + 4. The jump between figures is + 3 every time.",
      "d": "24 is 12 × 2. The dots grow evenly by 3, so add; do not multiply."},
   "right": "Each figure has 3 more dots: 12 + 3 = 15.",
   "solution": "Write the numbers: 3, 6, 9, 12. The jump is + 3 every time, so the next figure has 12 + 3 = 15 dots."},
  "p4": {"ok": "a", "hints": {
      "b": "Input + 4 works for the first row (2 + 4 = 6), but check the second row: 3 + 4 = 7, not 9.",
      "c": "That compares one output with the next one (6 → 9 → 12). The rule connects each input with its own output: 2 → 6.",
      "d": "The outputs are greater than the inputs, so the rule cannot subtract."},
   "right": "2 × 3 = 6, 3 × 3 = 9, and 4 × 3 = 12. The rule works on every row.",
   "solution": "Look across each row: 2 → 6, 3 → 9, 4 → 12. Each output is 3 times its input. The rule is: the output is the input times 3."},
 },
 "quiz": {
  "A": {"ok": "a", "hints": {"b": "18 is 16 + 2. Check the jump: from 4 to 8 is + 4.", "c": "24 is 16 + 8, two jumps of 4. You only need one jump.", "d": "32 is 16 × 2. The numbers grow evenly, so the rule adds 4."},
        "solution": "The jump is + 4 every time: 4, 8, 12, 16. The next term is 16 + 4 = 20."},
  "B": {"ok": "d", "hints": {"a": "The numbers go down, so the rule cannot add.", "b": "Multiplying by 5 makes numbers much bigger, but these get smaller.", "c": "50 ÷ 5 = 10, not 45. Find how much each term goes down."},
        "solution": "From one term to the next, the numbers go down by 5: 50 − 5 = 45, 45 − 5 = 40, 40 − 5 = 35. The rule is subtract 5 each time."},
  "C": {"ok": "b", "hints": {"a": "16 is 12 + 4. The jump is + 6: 6 → 12.", "c": "20 is too close to 24. The jump is + 6, so the missing term is 12 + 6.", "d": "15 is less than halfway. The jump is + 6, so the missing term is 12 + 6."},
        "solution": "The jump is + 6 (6 → 12 and 24 → 30). The missing term is 12 + 6 = 18. Check: 18 + 6 = 24."},
  "D": {"ok": "c", "hints": {"a": "36 is 24 + 12. Look at the jumps: + 3, + 6, + 12. They are not the same, so the rule does not add.", "b": "30 is 24 + 6. The jumps are not equal, so the rule does not add.", "d": "27 is 24 + 3. The numbers grow very fast: try multiplying."},
        "solution": "Each term is the one before it times 2: 3 × 2 = 6, 6 × 2 = 12, 12 × 2 = 24. The next term is 24 × 2 = 48."},
  "E": {"ok": "d", "hints": {"a": "22 is 20 + 2. The jump between figures is + 5.", "b": "30 is 20 + 10, two jumps of 5. You only need one.", "c": "40 is 20 × 2. The dots grow evenly by 5, so add; do not multiply."},
        "solution": "The numbers are 5, 10, 15, 20. The jump is + 5 every time, so the next figure has 20 + 5 = 25 dots."},
  "F": {"ok": "a", "hints": {"b": "Input × 5 works for the first row (1 × 5 = 5), but check the second row: 2 × 5 = 10, not 6.", "c": "That compares one output with the next one (5 → 6 → 7). Look across each row instead: 1 → 5.", "d": "The outputs are greater than the inputs, so the rule cannot subtract."},
        "solution": "Look across each row: 1 + 4 = 5, 2 + 4 = 6, 3 + 4 = 7. The rule is: the output is the input plus 4."},
  "G": {"ok": "b", "hints": {"a": "9 is 5 + 4. The rule says multiply by 4, not add 4.", "c": "45 is 5 × 9. Use the number in the rule: 5 × 4.", "d": "1 is 5 − 4. The rule says multiply by 4."},
        "solution": "The rule is output = input × 4. With the input 5: 5 × 4 = 20."},
  "H": {"ok": "c", "hints": {"a": "$55 is $50 + $5. Find the jump: from $20 to $35 is + $15.", "b": "$70 is $50 + $20. The jump is $15 each week: $35 − $20 = $15.", "d": "$60 is $50 + $10. The jump is $15 each week, not $10."},
        "solution": "Each week the amount goes up by $15: $20, $35, $50. In week 4 the person will have $50 + $15 = $65."},
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 5.1 · Math Level 1 (English) — built by tools/build_lesson_5_1.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 5.1 · Number and shape patterns · LearnGED</title>
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
<h1>Lesson 5.1 · Number and shape patterns</h1>
<p class="lema">Find the hidden rule behind a list of numbers or shapes: your first step toward algebra.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🔍</span> Find the rule</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Find the rule</strong> of a number pattern or a shape pattern.</li>
<li><strong>Continue</strong> a pattern for at least three more terms.</li>
<li><strong>Find</strong> a missing term in the middle of a pattern.</li>
<li><strong>Explain the rule</strong> of a pattern in clear words.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-new-thinking">A new kind of thinking</a></li>
<li><a href="#s-number-patterns">Number patterns</a></li>
<li><a href="#s-shape-patterns">Shape patterns</a></li>
<li><a href="#s-input-output">Input-output tables</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-new-thinking"><span aria-hidden="true" class="num-seccion">1</span>A new kind of thinking</h2>
<p>In Topics 1 to 4 you learned to <strong>calculate</strong>: to add, subtract, multiply, and divide whole numbers, decimals, and fractions. That is arithmetic.</p>
<p>Topic 5 takes a new step. Now you will not only find an answer; you will <strong>discover the idea hidden</strong> behind the numbers. When you see 2, 4, 6, 8, … your mind notices something: "they go up by two." That is a <strong>pattern</strong>, and seeing it is the first step toward <strong>algebra</strong>.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea of this lesson</span>
<p>A <strong>pattern</strong> (or sequence) is a list of numbers or shapes that follows a <strong>rule</strong>. If you discover the rule, you can predict what comes next, even if you have never seen it.</p>
</div>
</section>

<section>
<h2 id="s-number-patterns"><span aria-hidden="true" class="num-seccion">2</span>Number patterns</h2>
<p>In a number pattern, each number is called a <strong>term</strong>. The <strong>rule</strong> tells you how to go from one term to the next. To discover it, look at <strong>what changes from one term to the next</strong>.</p>
<h3>Patterns that add or subtract</h3>
<p>Look at this pattern. What happens from one number to the next?</p>
{seq([3, 8, 13, 18, None], "+5", "plus 5")}
<div class="ejemplo">
<p class="titulo-ej">Example: find the rule of 3, 8, 13, 18, …</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Find the jump.</strong> From 3 to 8 is + 5; from 8 to 13 is + 5; from 13 to 18 is + 5.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Say the rule.</strong> Add 5 each time.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Use the rule.</strong> The next term is 18 + 5 = <strong>23</strong>.</p>
</div>
<p>A pattern can also go down. In 40, 36, 32, 28, … the jump is − 4 each time, so the rule is <strong>subtract 4 each time</strong>, and the next term is 28 − 4 = 24.</p>
<h3>Patterns that multiply</h3>
<p>Not every pattern adds. In this one, you get each term by <strong>multiplying</strong>:</p>
{seq([2, 4, 8, 16, None], "×2", "times 2")}
<p>Here the rule is <strong>multiply by 2 each time</strong>. The next term is 16 × 2 = <strong>32</strong>.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">A tip to find the rule</span>
<p>First ask yourself: <strong>do the numbers grow slowly or very fast?</strong> If they grow slowly and evenly, the rule usually adds. If they grow very fast (they double or triple), the rule usually multiplies. Then check your rule on <strong>every</strong> pair of terms, not just the first two.</p>
</div>
{calc("Check it on the calculator", f"""<p>The calculator can repeat a rule for you. If you press {T("enter")} on an empty line, it does the last calculation again with the new answer.</p>
<ol>
<li>Type the first term, {T("3")}, and press {T("enter")}.</li>
<li>Press {T("+")} {T("5")} {T("enter")}. The calculator writes ans+5 (the last answer plus 5) and shows 8.</li>
<li>Press {T("enter")} again and again. Each time it adds 5 one more time: 13, 18, 23, 28.</li>
<li>For a pattern that multiplies, do the same with {T("×")}: {T("2")} {T("enter")}, then {T("×")} {T("2")} {T("enter")}, then {T("enter")} {T("enter")}. You get 4, 8, 16, 32.</li>
</ol>""")}
{practica("p1", "Practice 1 — Continue a pattern", "What number comes next in the pattern <strong>7, 11, 15, 19, ___</strong>?", [("a", "21"), ("b", "24"), ("c", "23"), ("d", "38")])}
{practica("p2", "Practice 2 — The missing term in the middle", "In the pattern <strong>5, 10, ___, 20, 25</strong>, what number is missing?", [("a", "12"), ("b", "15"), ("c", "14"), ("d", "18")])}
{enlace("number-patterns", "number patterns", "Build your own patterns, find the rule, and find missing terms.")}
</section>

<section>
<h2 id="s-shape-patterns"><span aria-hidden="true" class="num-seccion">3</span>Shape patterns</h2>
<p>Patterns are not only made of numbers: <strong>shapes</strong> can follow a rule too. Look at how these squares grow:</p>
{squares("Three figures made of small squares. Figure 1 is 1 square. Figure 2 is a 2-by-2 square, 4 small squares. Figure 3 is a 3-by-3 square, 9 small squares.")}
<p>The number of small squares makes a number pattern: <strong>1, 4, 9, …</strong> Each figure is a square with as many rows as its number: figure 4 will have 4 rows of 4, that is, 4 × 4 = <strong>16</strong> squares.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The trick</span>
<p>You can turn any shape pattern into a number pattern by <strong>counting something</strong>: how many squares, how many dots, how many sides. Once you have the numbers, look for the rule just as you did in section 2.</p>
</div>
{practica("p3", "Practice 3 — A shape pattern", "A pattern of figures has 3, 6, 9, and 12 dots. How many dots will the next figure have?", [("a", "15"), ("b", "13"), ("c", "16"), ("d", "24")])}
{enlace("shape-patterns", "shape patterns", "Count squares or dots and turn a shape pattern into a number pattern.")}
</section>

<section>
<h2 id="s-input-output"><span aria-hidden="true" class="num-seccion">4</span>Input-output tables</h2>
<p>A very useful way to show a rule is an <strong>input-output table</strong>. The <strong>input</strong> is the number you put in. The <strong>output</strong> is the number that comes out after you use the rule. You can think of a machine: a number goes in, the machine uses its rule, and a new number comes out.</p>
<div aria-label="Input-output table (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-es"><caption class="cap-oculto">Input-output table: each input and its output</caption>
<thead><tr><th scope="col">Input</th><th scope="col">Output</th></tr></thead>
<tbody>
<tr><td class="col-e">1</td><td class="col-s">4</td></tr>
<tr><td class="col-e">2</td><td class="col-s">5</td></tr>
<tr><td class="col-e">3</td><td class="col-s">6</td></tr>
<tr><td class="col-e">4</td><td class="col-s">7</td></tr>
</tbody>
</table></div>
<div class="ejemplo">
<p class="titulo-ej">Example: find the rule of the table</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Look across each row.</strong> 1 gives 4, 2 gives 5, 3 gives 6.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Ask what happened to each input.</strong> 3 was added to each one: 1 + 3 = 4, 2 + 3 = 5, 3 + 3 = 6, 4 + 3 = 7.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Say the rule.</strong> The output is the input plus 3. If the input were 10, the output would be 13.</p>
</div>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out!</span>
<p>In an input-output table, the rule connects <strong>each input with its own output</strong>. It does not compare one row with the next. Always read across the row: input → output.</p>
</div>
{practica("p4", "Practice 4 — An input-output table", "In a table, the input 2 gives the output 6, the input 3 gives the output 9, and the input 4 gives the output 12. What is the rule?", [("a", "The output is the input times 3."), ("b", "The output is the input plus 4."), ("c", "The output is the input plus 3."), ("d", "The output is the input minus 3.")])}
{enlace("input-output", "input-output tables", "Find the rule of the machine and complete the outputs.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">5</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-5-1.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Make three patterns of your own: one that adds, one that subtracts, and one that multiplies. Write five terms of each. For each one, write the rule in words <strong>before</strong> you write the next term: if you cannot say the rule, you have not found it yet. Then make an input-output table with five rows and write its rule.</li>
<li><strong>In your daily life.</strong> Look for a real pattern: the money you save each week, the times a bus stops at your corner, the house numbers on your street. Write the numbers as a list, describe the rule in words, and predict the next two terms.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">6</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", "What number comes next in the pattern <strong>4, 8, 12, 16, ___</strong>?", [("a", "20"), ("b", "18"), ("c", "24"), ("d", "32")])}
{quiz("B", "What is the rule of the pattern <strong>50, 45, 40, 35, …</strong>?", [("a", "Add 5 each time."), ("b", "Multiply by 5 each time."), ("c", "Divide by 5 each time."), ("d", "Subtract 5 each time.")])}
{quiz("C", "What number is missing in the pattern <strong>6, 12, ___, 24, 30</strong>?", [("a", "16"), ("b", "18"), ("c", "20"), ("d", "15")])}
{quiz("D", "What number comes next in the pattern <strong>3, 6, 12, 24, ___</strong>?", [("a", "36"), ("b", "30"), ("c", "48"), ("d", "27")])}
{quiz("E", "A pattern of figures has 5, 10, 15, and 20 dots. How many dots will the next figure have?", [("a", "22"), ("b", "30"), ("c", "40"), ("d", "25")])}
{quiz("F", "In a table, the input 1 gives the output 5, the input 2 gives the output 6, and the input 3 gives the output 7. What is the rule?", [("a", "The output is the input plus 4."), ("b", "The output is the input times 5."), ("c", "The output is the input plus 1."), ("d", "The output is the input minus 4.")])}
{quiz("G", 'The rule is "the output is the input times 4." If the input is <strong>5</strong>, what is the output?', [("a", "9"), ("b", "20"), ("c", "45"), ("d", "1")])}
{quiz("H", "A person saves money like this: in week 1 she has $20, in week 2 she has $35, and in week 3 she has $50. If the pattern goes on, how much will she have in week 4?", [("a", "$55"), ("b", "$70"), ("c", "$65"), ("d", "$60")])}
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
<div aria-label="Self-check checklist for patterns (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for number and shape patterns and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Find the rule of a pattern</th><td>I find the rule in patterns that add, subtract, or multiply.</td><td>I find the rule when the pattern adds or subtracts.</td><td>I do not see what changes from one term to the next.</td></tr>
<tr><th scope="row">Continue a pattern and find missing terms</th><td>I continue the pattern with no mistakes, and I find a missing term in the middle.</td><td>I continue the pattern forward, with an occasional slip.</td><td>I cannot continue the pattern yet.</td></tr>
<tr><th scope="row">Work with input-output tables</th><td>I find the rule and complete the table with confidence.</td><td>I complete the table when I know the rule.</td><td>I compare one row with the next instead of each input with its output.</td></tr>
<tr><th scope="row">Explain the rule in words</th><td>I explain the rule clearly and exactly ("add 5 each time").</td><td>I explain the rule, but my words are not always exact.</td><td>I cannot say the rule in words yet.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You can now find the rule of a pattern and say it in words. That is exactly the bridge to algebra.</p>
<p>In <strong>Lesson 5.2 · Algebraic language and simple unknowns</strong> you will take the next step: you will write those rules with <strong>symbols</strong> instead of words, and use a letter or a box for a number you do not know yet, the <strong>unknown</strong>. This is the moment when math starts to use its own language.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: <a href="lesson-5-2.html">Lesson 5.2 · Algebraic language and simple unknowns</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>pattern (sequence)</dt><dd>A list of numbers or shapes that follows a rule, like 3, 8, 13, 18, …</dd>
<dt>term</dt><dd>Each number in a pattern. In 3, 8, 13, the second term is 8.</dd>
<dt>rule</dt><dd>What you do to go from one term to the next, or from an input to its output, like "add 5 each time."</dd>
<dt>input</dt><dd>The number you put into a rule or a table.</dd>
<dt>output</dt><dd>The number you get after you use the rule on the input.</dd>
<dt>input-output table</dt><dd>A table that shows each input next to its output. The rule connects each input with its own output.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.1</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-5-1.html"), "w", encoding="utf-8").write(html)
print("ok")
