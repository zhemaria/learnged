"""Builds math/level-1/lesson-5-3.html (English). Run tools/ged_standards.py afterwards
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
    href = href or f"practice-5-3.html#{ancla}"
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


def cinta(partes, total, label):
    """A bar model: partes = list of (width, text, fill); total written above with a bracket."""
    x0, y0, W, H = 40, 70, 560, 56
    s = [f'<line x1="{x0}" y1="38" x2="{x0 + W}" y2="38" stroke="#0d47a1" stroke-width="2"/>',
         f'<line x1="{x0}" y1="30" x2="{x0}" y2="46" stroke="#0d47a1" stroke-width="2"/><line x1="{x0 + W}" y1="30" x2="{x0 + W}" y2="46" stroke="#0d47a1" stroke-width="2"/>',
         f'<rect x="{x0 + W / 2 - 46}" y="20" width="92" height="34" rx="6" fill="#fff"/><text x="{x0 + W / 2}" y="44" text-anchor="middle" font-size="22" font-weight="700" fill="#0d47a1">{total}</text>']
    tot = sum(p[0] for p in partes); x = x0
    for w, t, c in partes:
        ww = W * w / tot
        s.append(f'<rect x="{x:.1f}" y="{y0}" width="{ww:.1f}" height="{H}" fill="{c}" stroke="#37474f" stroke-width="2"/>')
        s.append(f'<text x="{x + ww / 2:.1f}" y="{y0 + 36}" text-anchor="middle" font-size="22" font-weight="700" fill="{"#fff" if c == "#1565c0" else "#1a2330"}">{t}</text>')
        x += ww
    return f'<svg viewBox="0 0 640 150" role="img" aria-label="{label}" style="width:100%;max-width:560px;height:auto;display:block;margin:12px auto;">{"".join(s)}</svg>'

AZ, GR = "#1565c0", "#cfd8dc"

LESSON = {
 "next": "Lesson 6.1", "review": "sections 2, 3, and 4",
 "practice": {
  "p1": {"ok": "c", "hints": {
      "a": "Adding 12 + 24 puts two different things together. Here there are 12 equal groups of 24 bottles.",
      "b": "Nothing is taken away in this story. Every box has the same number of bottles: equal groups.",
      "d": "Nothing is split. The boxes come together, each with 24 bottles: equal groups."},
   "right": "12 equal groups of 24 bottles: 12 × 24 = 288 bottles.",
   "solution": "Each box has the same number of bottles, and the boxes come together: equal groups. Multiply: 12 × 24 = 288 bottles."},
  "p2": {"ok": "b", "hints": {
      "a": "48 is 41 + 7. The word \"older\" can fool you: Rita is older, so her brother is younger.",
      "c": "287 is 41 × 7. Nothing is repeated in equal groups. Compare the two ages.",
      "d": "7 is the difference between the ages, not the brother's age. Take 7 away from Rita's age."},
   "right": "Her brother is 7 years younger: 41 − 7 = 34 years.",
   "solution": "Rita is older, so her brother is younger. Take the difference away: 41 − 7 = 34 years."},
  "p3": {"ok": "a", "hints": {
      "b": "x − 14 means 14 people got off. In the story, 14 people got on: add.",
      "c": "14x means 14 equal groups. In the story, 14 people were added to the bus.",
      "d": "The 50 people are on the bus at the end, so 50 goes alone on one side: x + 14 = 50."},
   "right": "There were x people, 14 more got on, and now there are 50: x + 14 = 50. So x = 36.",
   "solution": "There were x people at first, 14 more got on (+ 14), and now there are 50: x + 14 = 50. Solving it: x = 50 − 14 = 36 people."},
  "p4": {"ok": "d", "hints": {
      "a": "13 is 8 + 5. The box was split into 5 equal parts, so the box had 5 times 8 markers.",
      "b": "3 is 8 − 5. The box was split into 5 equal parts of 8 markers each.",
      "c": "8 markers is what one table got, not the whole box. There are 5 tables."},
   "right": "x ÷ 5 = 8, so x = 8 × 5 = 40 markers. Check: 40 ÷ 5 = 8.",
   "solution": "The box (x) was split among 5 tables, and each got 8: x ÷ 5 = 8. The inverse of dividing is multiplying: x = 8 × 5 = 40 markers."}
 },
 "quiz": {
  "A": {"ok": "d", "hints": {
      "a": "Nothing comes together here. A total of 96 is being split.",
      "b": "Subtracting 8 once does not split the tortillas into equal bags.",
      "c": "Multiplying makes a bigger total. Here the total of 96 is split into equal bags."},
   "solution": "A total (96 tortillas) is split equally into 8 bags: divide. 96 ÷ 8 = 12 tortillas in each bag."},
  "B": {"ok": "b", "hints": {
      "a": "43 is 34 + 9. \"Older\" can fool you: Lucía is older, so her brother is younger.",
      "c": "306 is 34 × 9. Nothing is repeated in equal groups. Compare the ages.",
      "d": "9 is the difference between the ages, not the brother's age."},
   "solution": "Lucía is 9 years older, so her brother is 9 years younger: 34 − 9 = 25 years."},
  "C": {"ok": "c", "hints": {
      "a": "x + 65 means he got $65 more. He spent $65: take it away.",
      "b": "65x means 65 times the money. He spent $65: subtract.",
      "d": "Nothing was split into equal parts. He spent $65: subtract."},
   "solution": "He had x dollars, spent $65 (− 65), and has $120 left: x − 65 = 120. Solving it: x = 120 + 65 = $185."},
  "D": {"ok": "a", "hints": {
      "b": "x + 15 adds $15 once. Each ticket costs $15: that is x equal groups of $15.",
      "c": "Nothing is taken away. Each ticket costs the same: equal groups.",
      "d": "The numbers are in the wrong places. x tickets of $15 each cost $180: 15x = 180."},
   "solution": "x tickets at $15 each cost 15 × x dollars, and the group paid $180: 15x = 180. Solving it: x = 180 ÷ 15 = 12 tickets."},
  "E": {"ok": "c", "hints": {
      "a": "15 is 9 + 6. The rope was cut into 6 equal pieces of 9 feet, so it is 6 times 9.",
      "b": "3 is 9 − 6. Each of the 6 pieces is 9 feet long, so the rope is longer than 9 feet.",
      "d": "9 feet is one piece. The whole rope has 6 pieces like that."},
   "solution": "The rope (x) was cut into 6 equal pieces of 9 feet: x ÷ 6 = 9. So x = 9 × 6 = 54 feet."},
  "F": {"ok": "b", "hints": {
      "a": "$100 is less than one month of rent. Twelve months must cost much more than $1,200.",
      "c": "$1,212 is $1,200 + 12. They pay $1,200 each month for 12 months: equal groups.",
      "d": "$1,188 is less than one month of rent, so it cannot be the cost of 12 months."},
   "solution": "12 months of $1,200 each: 12 × $1,200 = $14,400. It makes sense: it is much more than one month."},
  "G": {"ok": "a", "hints": {
      "b": "$996 also counts the 38 pants. The question asks only about the shirts.",
      "c": "$57 is 45 + 12. Each of the 45 shirts costs $12: equal groups.",
      "d": "$456 uses the 38 pants. The question asks about the 45 shirts."},
   "solution": "Only the shirts matter: 45 shirts at $12 each. 45 × $12 = $540. The 38 pants are extra information."},
  "H": {"ok": "d", "hints": {
      "a": "The number is right, but the unit is not. The question asks how many miles per gallon.",
      "b": "1,920 is 240 × 8. The miles are split among the gallons: divide.",
      "c": "248 is 240 + 8. The miles are split among the 8 gallons: divide."},
   "solution": "240 miles split among 8 gallons: 240 ÷ 8 = 30. The answer needs its unit: 30 miles per gallon."}
 }
}

html = f'''<!DOCTYPE html>
<!-- LearnGED · Lesson 5.3 · Math Level 1 (English) — built by tools/build_lesson_5_3.py
     José M. Fernández · CC BY-NC-SA 4.0 -->

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lesson 5.3 · One-step word problems with the four operations · LearnGED</title>
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
<h1>Lesson 5.3 · One-step word problems with the four operations</h1>
<p class="lema">Read the story, find the unknown, write the equation, and solve it. Everything from Level 1 comes together here.</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> About 4 hours with practice and homework · take breaks</span>
<span class="chip"><span aria-hidden="true">🧩</span> From the story to the equation</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>What you will learn</h2>
<p>When you finish this lesson, you will be able to:</p>
<ul>
<li><strong>Picture</strong> the situation in a story and choose which of the four operations it needs.</li>
<li><strong>Name</strong> the unknown and write the problem as a one-step equation.</li>
<li><strong>Solve</strong> the equation with the inverse operation.</li>
<li><strong>Check</strong> that the answer makes sense and has the right unit.</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">Lesson contents</h2><ol>
<li><a href="#s-together">Everything comes together</a></li>
<li><a href="#s-situations">Four situations, four operations</a></li>
<li><a href="#s-equation">From the story to the equation</a></li>
<li><a href="#s-sense">Does the answer make sense?</a></li>
<li><a href="#s-homework">Homework</a></li>
<li><a href="#s-quiz">Practice quiz</a></li>
<li><a href="#s-checklist">Self-check checklist</a></li>
<li><a href="#s-next">Coming next</a></li>
<li><a href="#s-words">Key words</a></li>
</ol></nav>

<section>
<h2 id="s-together"><span aria-hidden="true" class="num-seccion">1</span>Everything comes together</h2>
<p>This lesson closes Topic 5 and puts together everything you learned in Level 1. In <strong>Topics 1 and 2</strong> you learned when to add, subtract, multiply, and divide in a word problem. In <strong>Lesson 5.2</strong> you learned to write and solve equations with an unknown.</p>
<p>Now you will join both ideas: you will read a problem in words, find the number you do not know, write it as an equation, and solve it.</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The key idea of this lesson</span>
<p>A word problem is a <strong>story with an unknown</strong>. Your job is to translate the story into an equation, solve the equation, and answer the question with the right unit.</p>
</div>
</section>

<section>
<h2 id="s-situations"><span aria-hidden="true" class="num-seccion">2</span>Four situations, four operations</h2>
<p>Before you choose an operation, <strong>picture what happens</strong> in the story. Each operation matches one kind of situation:</p>
<div aria-label="Situations and their operations (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">Each kind of situation and the operation it needs</caption>
<thead><tr><th scope="col">Situation</th><th scope="col">What happens</th><th scope="col">Operation</th><th scope="col">Example</th></tr></thead>
<tbody>
<tr><td><strong>Put together · add on</strong></td><td>Amounts come together, or something increases.</td><td>Addition</td><td class="expr">245 + 130</td></tr>
<tr><td><strong>Take away · compare</strong></td><td>Something is taken away, or you find the difference between two amounts.</td><td>Subtraction</td><td class="expr">500 − 175</td></tr>
<tr><td><strong>Equal groups</strong></td><td>Several groups of the same size come together.</td><td>Multiplication</td><td class="expr">9 × 24</td></tr>
<tr><td><strong>Split equally</strong></td><td>A total is split into equal parts, or into groups of a given size.</td><td>Division</td><td class="expr">96 ÷ 8</td></tr>
</tbody>
</table></div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out! The words can fool you</span>
<p>Key words help, but <strong>the story decides</strong>. Look at this problem: "Pedro has $58. That is $15 more than Ana has. How much does Ana have?" It says "more," but Ana has <strong>less</strong> than Pedro. So we subtract: 58 − 15 = <strong>$43</strong>.</p>
</div>
{practica("p1", "Practice 1 — Choose the operation", '"A store receives 12 boxes. Each box has 24 bottles. How many bottles are there in all?" Which operation do you need?', [("a", "Add: 12 + 24"), ("b", "Subtract: 24 − 12"), ("c", "Multiply: 12 × 24"), ("d", "Divide: 24 ÷ 12")])}
{practica("p2", "Practice 2 — When the words fool you", '"Rita is 41 years old. She is 7 years older than her brother. How old is her brother?"', [("a", "48 years"), ("b", "34 years"), ("c", "287 years"), ("d", "7 years")])}
{enlace("operation", "choose the operation", "Read a situation, picture what happens, and choose the operation.")}
</section>

<section>
<h2 id="s-equation"><span aria-hidden="true" class="num-seccion">3</span>From the story to the equation</h2>
<p>When the number you do not know is not the final result, an equation helps a lot. Use the 4 steps from Lesson 1.3, now with an unknown:</p>
<div class="caja caja-tip">
<span class="etiqueta et-verde">The 4 steps with an unknown</span>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Read and name the unknown.</strong> Underline the numbers and the question. Call the number you do not know x.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Write the equation.</strong> Follow the story in order, with x in its place.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve</strong> with the inverse operation, as in Lesson 5.2.</p>
<p class="paso"><span aria-hidden="true" class="n">4</span><strong>Check and answer.</strong> Put the value back into the story, and write the answer with its unit.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: "Rosa had some money in her account. She deposited $85, and now she has $310. How much did she have at first?"</p>
{cinta([(225, "x", AZ), (85, "85", GR)], "310", "A bar model. A whole bar of 310 is split into two parts: the unknown x and 85.")}
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Name the unknown.</strong> x = the money Rosa had at first.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Write the equation.</strong> She had x, and $85 was added: {E("x + 85 = 310")}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve.</strong> Subtract 85 from both sides: x = 310 − 85 = 225.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Check and answer.</strong> $225 + $85 = $310 ✓. Rosa had <strong>$225</strong> at first.</p>
</div>
<div class="ejemplo">
<p class="titulo-ej">Example: "Marcos worked 8 hours and earned $136. He earns the same amount each hour. How much does he earn per hour?"</p>
{cinta([(1, "x", AZ)] * 8, "136", "A bar model. A whole bar of 136 is split into 8 equal parts, each one marked x.")}
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Name the unknown.</strong> x = the money Marcos earns per hour.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Write the equation.</strong> 8 equal hours of x dollars each: {E("8x = 136")}.</p>
<p class="paso"><span aria-hidden="true" class="n">3</span><strong>Solve.</strong> Divide both sides by 8: x = 136 ÷ 8 = 17.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Check and answer.</strong> 8 × $17 = $136 ✓. Marcos earns <strong>$17 per hour</strong>.</p>
</div>
<p>Every one-step story fits one of these four equations:</p>
<div aria-label="Kinds of stories and their equations (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">The four kinds of one-step stories and their equations</caption>
<thead><tr><th scope="col">Story</th><th scope="col">Equation</th><th scope="col">Solution</th></tr></thead>
<tbody>
<tr><td>I had some money, I got $25 more, and now I have $60.</td><td class="expr">x + 25 = 60</td><td style="white-space:nowrap">x = 60 − 25 = 35</td></tr>
<tr><td>I had some money, I spent $15, and I have $40 left.</td><td class="expr">x − 15 = 40</td><td style="white-space:nowrap">x = 40 + 15 = 55</td></tr>
<tr><td>6 equal boxes hold 72 cans in all.</td><td class="expr">6x = 72</td><td style="white-space:nowrap">x = 72 ÷ 6 = 12</td></tr>
<tr><td>Some markers were split equally among 4 tables, and each table got 9.</td><td class="expr">x ÷ 4 = 9</td><td style="white-space:nowrap">x = 9 × 4 = 36</td></tr>
</tbody>
</table></div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
{practica("p3", "Practice 3 — Write the equation", '"Some people were on a bus. At a stop, 14 more people got on. Now there are 50 people on the bus." If x is the number of people at first, which equation shows this story?', [("a", "x + 14 = 50"), ("b", "x − 14 = 50"), ("c", "14x = 50"), ("d", "x + 50 = 14")])}
{practica("p4", "Practice 4 — Solve the problem", '"A teacher split a box of markers equally among 5 tables. Each table got 8 markers. How many markers were in the box?"', [("a", "13 markers"), ("b", "3 markers"), ("c", "8 markers"), ("d", "40 markers")])}
{enlace("equation", "write the equation", "Read a story and choose the equation that shows it.")}
{enlace("solve", "solve word problems step by step", "Follow the 4 steps with an unknown, then solve problems on your own.")}
</section>

<section>
<h2 id="s-sense"><span aria-hidden="true" class="num-seccion">4</span>Does the answer make sense?</h2>
<p>The last step is the one people skip most, and it catches many mistakes. Ask yourself three questions:</p>
<ul>
<li><strong>Is the size right?</strong> If something was added, the total must be bigger. If a total was split, each part must be smaller.</li>
<li><strong>Does it fit the story?</strong> Put the answer back into the story, not only into the equation.</li>
<li><strong>Does it have its unit?</strong> Dollars, miles, hours, people… A number alone does not answer the question.</li>
</ul>
<div class="ejemplo">
<p class="titulo-ej">Example: "A school bought 7 equal boxes of paper with 3,500 sheets in all. How many sheets are in each box?"</p>
<p class="paso"><span aria-hidden="true" class="n">1</span><strong>Solve.</strong> {E("7x = 3,500")}, so x = 3,500 ÷ 7 = 500.</p>
<p class="paso"><span aria-hidden="true" class="n">2</span><strong>Check the size.</strong> Each box holds part of the total, so the answer must be smaller than 3,500. 500 is smaller ✓.</p>
<p class="paso"><span aria-hidden="true" class="n">✓</span><strong>Check the story and the unit.</strong> 7 boxes × 500 sheets = 3,500 sheets ✓. Each box has <strong>500 sheets</strong>.</p>
</div>
<div class="caja caja-ojo">
<span class="etiqueta et-ambar">Watch out! Extra information</span>
<p>Some problems give you numbers you do not need. "A store sold 45 shirts and 38 pants. Each shirt costs $12. How much money did the shirts bring in?" The 38 pants do not matter for this question: 45 × $12 = <strong>$540</strong>.</p>
</div>
{calc("Solve it and check it on the calculator", f"""<p>The calculator can do the inverse operation for you, and then check the answer against the story.</p>
<ol>
<li>Solve {E("7x = 3,500")}: type {T("3")}{T("5")}{T("0")}{T("0")} {T("÷")} {T("7")} {T("enter")}. The screen shows 500.</li>
<li>Check it: type {T("5")}{T("0")}{T("0")} {T("×")} {T("7")} {T("enter")}. The screen shows 3500, the total in the story: ✓.</li>
</ol>""")}
{enlace("makes-sense", "does the answer make sense?", "Choose the answer that fits the story, with the right size and the right unit.")}
</section>

<section>
<h2 id="s-homework"><span aria-hidden="true" class="num-seccion">5</span>Homework</h2>
<p>This is independent practice. Plan for about one hour, with your notebook open.</p>
<ul class="lista-tarea">
<li><strong>The practice page.</strong> Open the <a href="practice-5-3.html">practice page for this lesson</a> and do each activity. The exercises change every time. Do at least 10 in each activity, and keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.</li>
<li><strong>Paper and pencil.</strong> Write four short stories of your own, one for each operation. For each one, name the unknown, write the equation, solve it, and check it. Then trade stories with a classmate or a family member and solve theirs.</li>
<li><strong>In your daily life.</strong> Look for a real one-step problem this week: a bill split among roommates, the hours you need to work to earn a certain amount, the miles left on a trip. Solve it with the 4 steps and write the answer with its unit.</li>
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">6</span>Practice quiz</h2>
<p>Answer the <strong>8 questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.</p>
<div id="quiz">
{quiz("A", '"A cook splits 96 tortillas equally into 8 bags. How many tortillas go in each bag?" Which operation do you need?', [("a", "Add."), ("b", "Subtract."), ("c", "Multiply."), ("d", "Divide.")])}
{quiz("B", '"Lucía is 34 years old. She is 9 years older than her brother. How old is her brother?"', [("a", "43 years"), ("b", "25 years"), ("c", "306 years"), ("d", "9 years")])}
{quiz("C", '"A worker had some money. He spent $65 and has $120 left." If x is the money he had, which equation shows this story?', [("a", "x + 65 = 120"), ("b", "65x = 120"), ("c", "x − 65 = 120"), ("d", "x ÷ 65 = 120")])}
{quiz("D", '"Each ticket costs $15. A group paid $180 in all." If x is the number of tickets, which equation shows this story?', [("a", "15x = 180"), ("b", "x + 15 = 180"), ("c", "x − 15 = 180"), ("d", "180x = 15")])}
{quiz("E", '"A rope was cut into 6 equal pieces. Each piece is 9 feet long. How long was the rope?"', [("a", "15 feet"), ("b", "3 feet"), ("c", "54 feet"), ("d", "9 feet")])}
{quiz("F", '"A family pays $1,200 in rent each month. How much do they pay in 12 months?" Which answer makes sense?', [("a", "$100"), ("b", "$14,400"), ("c", "$1,212"), ("d", "$1,188")])}
{quiz("G", '"A store sold 45 shirts and 38 pants. Each shirt costs $12. How much money did the shirts bring in?"', [("a", "$540"), ("b", "$996"), ("c", "$57"), ("d", "$456")])}
{quiz("H", '"A car travels 240 miles on 8 gallons of gas. How many miles does it travel per gallon?"', [("a", "30 gallons"), ("b", "1,920 miles"), ("c", "248 miles"), ("d", "30 miles per gallon")])}
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
<div aria-label="Self-check checklist for one-step word problems (table you can scroll sideways)" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">Self-check checklist: skills for one-step word problems and what Got it, Getting there, and Needs more practice look like</caption>
<thead><tr><th scope="col">Skill</th><th class="nivel-cab" scope="col">Got it</th><th class="nivel-cab" scope="col">Getting there</th><th class="nivel-cab" scope="col">Needs more practice</th></tr></thead>
<tbody>
<tr><th scope="row">Picture the situation</th><td>I picture what happens and choose the operation, even when the words try to fool me.</td><td>I choose the right operation in most problems.</td><td>I only look for key words, and sometimes I choose the wrong operation.</td></tr>
<tr><th scope="row">Name the unknown and write the equation</th><td>I name the unknown and write an equation that follows the story.</td><td>I write the equation, but sometimes I put a number in the wrong place.</td><td>I am not sure what the unknown is or how to write the equation.</td></tr>
<tr><th scope="row">Solve the equation</th><td>I solve with the inverse operation, with no mistakes.</td><td>I solve correctly, with an occasional slip.</td><td>I use the same operation instead of the inverse one.</td></tr>
<tr><th scope="row">Check that the answer makes sense</th><td>I check the size, the story, and the unit every time.</td><td>I check when I remember.</td><td>I give a number without checking it or writing its unit.</td></tr>
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> Slide the table sideways to see all the columns.</p>
</section>

<section class="cierre">
<h2 id="s-next"><span aria-hidden="true" class="num-seccion">➡️</span>Coming next</h2>
<p>You can now solve one-step word problems with the four operations: picture the situation, write the equation, solve it, and check that the answer makes sense. With this lesson, you finish Topic 5.</p>
<p>In <strong>Topic 6 · Measurement and time</strong> you will use these skills with real measures: inches and feet, pounds and ounces, cups and gallons, and also the metric system, time, and temperature.</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> Next: Topic 6 · <a href="lesson-6-1.html">Lesson 6.1 · U.S. customary units: length, weight, and capacity</a></p>
</section>

<section>
<h2 id="s-words"><span aria-hidden="true" class="num-seccion">📘</span>Key words</h2>
<dl class="glosario">
<dt>word problem</dt><dd>A math problem told as a story in words, with a question to answer.</dd>
<dt>unknown</dt><dd>The number we do not know yet. In an equation we call it x.</dd>
<dt>equation</dt><dd>A statement that two things are equal, like x + 85 = 310.</dd>
<dt>bar model</dt><dd>A drawing with bars that shows the parts and the whole of a problem.</dd>
<dt>reasonable</dt><dd>Said of an answer that makes sense in the story: it has the right size and the right unit.</dd>
<dt>unit</dt><dd>What a number counts or measures: dollars, miles, hours, people.</dd>
</dl>
</section>
</div>
<footer><p>LearnGED · Math · Level 1 · Topic 5 · Lesson 5.3</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service. TI-30XS MultiView is a trademark of Texas Instruments; the calculator on this page is an independent learning simulator.</p></footer>
<script>
window.LESSON = {json.dumps(LESSON, ensure_ascii=False, indent=1)};
</script>
<script src="../lesson.js"></script>
<script src="/js/calculator.js" data-color="#0d47a1" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "math", "level-1", "lesson-5-3.html"), "w", encoding="utf-8").write(html)
print("ok")
