# -*- coding: utf-8 -*-
"""Reviewer guides for Math Levels 3 and 4 (review/level-3.html, review/level-4.html).

The lesson titles are read from the lesson pages themselves, so the guides stay in step
with the site. Run after the lessons are built:  python3 tools/build_review.py
"""
import os, re, html

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = """<!DOCTYPE html>
<!-- LearnGED · reviewer guide — built by tools/build_review.py; do not edit by hand -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reviewer guide · Math Level {n} · LearnGED</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link href="/fonts/fonts.css" rel="stylesheet">
<link rel="stylesheet" href="../learnged.css">
<style>
  .doc section{{background:#fff;border:1px solid var(--line);border-left:6px solid var(--teal);border-radius:12px;padding:20px 24px;margin:0 0 18px;scroll-margin-top:12px}}
  .doc h1{{color:var(--navy);margin:28px 0 6px}}
  .doc h2{{color:var(--navy);margin:0 0 8px;font-size:1.3rem}}
  .doc h3{{color:var(--teal-d);font-size:1.05rem;margin:16px 0 6px}}
  .doc table{{border-collapse:collapse;width:100%;font-size:.95rem}}
  .doc th,.doc td{{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}}
  .doc th{{color:var(--muted)}}
  .doc tr.tema th{{background:#eef6f7;color:var(--navy);padding-top:10px}}
  .doc .toc{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 22px;margin:18px 0}}
  .doc .toc ol{{columns:2;margin:0;padding-left:2.4em}} .doc .toc li{{padding-left:.4em}}
  .doc .links a.btn{{margin:4px 8px 4px 0}}
  .doc .up{{display:inline-block;margin-top:8px;font-size:.85rem;color:var(--muted)}}
  .doc .scroll{{overflow-x:auto}}
  .guias{{display:flex;flex-wrap:wrap;gap:6px;margin:16px 0 0;padding:0;list-style:none;font-size:.9rem}}
  .guias a,.guias span{{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:3px 12px;background:#fff;color:var(--navy);text-decoration:none;font-weight:700}}
  .guias span{{background:var(--navy);color:#fff;border-color:var(--navy)}}
  @media (max-width:700px){{.doc .toc ol{{columns:1}}}}
  @media print{{.doc .up,.top .tools,.guias{{display:none}} .doc section{{break-inside:avoid}}}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="logo" href="/"><img src="../img/learnged-logo-horizontal.svg" alt="LearnGED home"></a>
  <div class="tools"><button type="button" onclick="window.print()">Print</button></div>
</div></header>
<main id="main" class="wrap doc">
"""

FOOT = """</main>
<footer><div class="wrap">
<p class="tm">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>
</div></footer>
</body>
</html>
"""

GUIAS = [("index.html", "Level 1"), ("level-2.html", "Level 2"), ("level-3.html", "Level 3"),
         ("level-4.html", "Level 4"), ("whats-next.html", "What comes next")]


def barra(actual):
    """Row of links to all reviewer guides; the current one is not a link."""
    s = ['<nav aria-label="Reviewer guides"><ul class="guias">']
    for f, t in GUIAS:
        if f == actual:
            s.append('<li><span aria-current="page">%s</span></li>' % t)
        else:
            s.append('<li><a href="%s">%s</a></li>' % (f, t))
    s.append('</ul></nav>')
    return "".join(s)


def titulo(nivel, tn):
    p = os.path.join(RAIZ, "math", "level-%d" % nivel, "lesson-%s.html" % tn)
    with open(p, encoding="utf-8") as f:
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", f.read(), re.S).group(1)
    h1 = re.sub(r"<[^>]+>", "", h1)
    return html.unescape(h1).split("·", 1)[1].strip()


def up():
    return '<a class="up" href="#top">↑ Back to top</a></section>\n'


def tabla_lecciones(n, temas):
    a = 'target="_blank" rel="noopener"'
    s = ['<div class="scroll"><table>',
         '<tr><th scope="col">#</th><th scope="col">Lesson</th><th scope="col">English</th><th scope="col">Spanish</th></tr>']
    for t, nombre in enumerate(temas, 1):
        s.append('<tr class="tema"><th colspan="4" scope="colgroup">Topic %d · %s</th></tr>' % (t, html.escape(nombre)))
        for k in (1, 2, 3):
            tn = "%d-%d" % (t, k)
            s.append(
                '<tr><td>%d.%d</td><td>%s</td>'
                '<td><a href="/math/level-%d/lesson-%s.html" %s>Lesson</a> · <a href="/math/level-%d/practice-%s.html" %s>Practice</a></td>'
                '<td><a href="/es/matematicas/nivel-%d/leccion-%s.html" %s lang="es">Lección</a> · '
                '<a href="/es/matematicas/nivel-%d/practica-%s.html" %s lang="es">Práctica</a></td></tr>'
                % (t, k, html.escape(titulo(n, tn)), n, tn, a, n, tn, a, n, tn, a, n, tn, a))
    s.append('</table></div>')
    return "\n".join(s)


def tabla(filas, cab):
    s = ['<div class="scroll"><table>', '<tr>' + "".join('<th scope="col">%s</th>' % c for c in cab) + '</tr>']
    for f in filas:
        s.append('<tr>' + "".join('<td>%s</td>' % c for c in f) + '</tr>')
    s.append('</table></div>')
    return "\n".join(s)


def guia(n, d):
    out = [HEAD.format(n=n), barra("level-%d.html" % n)]
    out.append('<h1 id="top">Reviewer guide · Math Level %d</h1>' % n)
    out.append(d["intro"])
    out.append("""<nav class="toc" aria-label="Contents"><ol>
<li><a href="#pages">What to review</a></li>
<li><a href="#plan">How to split the work</a></li>
<li><a href="#new">What is new in Level {n}</a></li>
<li><a href="#look">What to look for</a></li>
<li><a href="#feedback">How feedback works</a></li>
<li><a href="#math">Math conventions</a></li>
<li><a href="#glossary">Glossary (Spanish → English)</a></li>
<li><a href="#questions">Questions for you</a></li>
<li><a href="#signoff">Sign-off</a></li>
<li><a href="#send">How to send comments</a></li>
</ol></nav>
""".format(n=n))
    # 1
    out.append('<section id="pages"><h2>1. What to review</h2>')
    out.append('<p>Each lesson is the main page (about 4 hours of student work). Its practice page has 3 to 6 activities that make new exercises every time; the lesson links to each one. The Spanish column is there only if you want to compare: both versions are built from the same source, so they must teach exactly the same thing.</p>')
    out.append('<p class="links"><a class="btn" href="/math/level-%d/" target="_blank" rel="noopener">Math Level %d · index</a> '
               '<a class="btn" href="/math/ged-standards.html" target="_blank" rel="noopener">GED and CCR standards</a></p>' % (n, n))
    out.append(tabla_lecciones(n, d["temas"]))
    out.append(d["extras"])
    out.append(up())
    # 2
    out.append('<section id="plan"><h2>2. How to split the work</h2>')
    out.append('<p>Nobody needs to read all 48 pages. Two ways that work well:</p><ul>')
    out.append('<li><strong>By topic:</strong> each reviewer takes one or two topics (3 lessons each) and signs off on them in section 9.</li>')
    out.append('<li><strong>By sample:</strong> if you have only an hour, read one lesson and its practice page all the way through, and skim the rest of that topic. Good samples: %s.</li></ul>' % d["muestras"])
    out.append('<p>In each lesson, please try the 8-question quiz at the end, and in each practice page do at least two exercises per activity, including one with a wrong answer on purpose, to see the hint.</p>')
    out.append(up())
    # 3
    out.append('<section id="new"><h2>3. What is new in Level %d</h2><ul>' % n)
    out.extend('<li>%s</li>' % x for x in d["nuevo"])
    out.append('</ul>')
    out.append(up())
    # 4
    out.append("""<section id="look"><h2>4. What to look for</h2>
<ul>
<li><strong>Reading level.</strong> The algebra is harder here, but the sentences should not be. Mark any word or sentence that is too hard.</li>
<li><strong>Tone.</strong> Our students are adults. Does anything sound childish, or too academic?</li>
<li><strong>Math accuracy.</strong> Numbers, signs, rounding, units, and every step of the worked examples.</li>
<li><strong>US usage.</strong> Anything that sounds translated or “not how we say it here” (see the questions in section 8).</li>
<li><strong>Hints.</strong> Do the hints name the likely mistake without giving the answer away?</li>
<li><strong>Answer checking.</strong> If you type a correct answer in another reasonable form and the page rejects it, please tell us what you typed.</li>
<li><strong>Figures and graphs.</strong> Labels that overlap a line or a number on an axis, points in the wrong place, colors that are hard to tell apart.</li>
<li><strong>Accessibility.</strong> Try the pages on a phone and with the keyboard only (the interactive graphs work with the arrow keys too).</li>
</ul>
""")
    out.append(up())
    # 5
    out.append("""<section id="feedback"><h2>5. How feedback works</h2>
<p>The same idea as in Levels 1 and 2: <strong>a mistake is information, not a failure</strong>.</p>
<ol>
<li><strong>First wrong answer:</strong> a hint that points to the specific mistake (for example, “%s”). The student tries again.</li>
<li><strong>Second wrong answer:</strong> the solution, explained step by step.</li>
<li><strong>Questions with only two choices</strong> (for example, “%s”) show the explanation right away, because a second try would be a guess.</li>
<li>Praise is about the strategy, not about being smart.</li>
</ol>
""" % (d["pista"], d["dos"]))
    out.append(up())
    # 6
    out.append('<section id="math"><h2>6. Math conventions</h2>')
    out.append(tabla(d["convenciones"], ["Topic", "LearnGED"]))
    out.append(up())
    # 7
    out.append('<section id="glossary"><h2>7. Glossary (Spanish → English)</h2>')
    out.append('<p>These are the terms used in Level %d, added to the lists of the earlier levels.</p>' % n)
    out.append(tabla(d["glosario"], ["Spanish", "English", "Note"]))
    out.append(up())
    # 8
    out.append('<section id="questions"><h2>8. Questions for you</h2><ol>')
    out.extend('<li>%s</li>' % x for x in d["preguntas"])
    out.append('</ol>')
    out.append(up())
    # 9
    out.append('<section id="signoff"><h2>9. Sign-off</h2>')
    out.append('<p>When you finish a topic, mark it here (on paper or in your email). A topic needs at least one 🟢 to be marked ready on the site.</p>')
    filas = [["%d · %s" % (t, html.escape(x)), "", "", "☐ 🟢 Ready &nbsp; ☐ 🟡 Changes needed"] for t, x in enumerate(d["temas"], 1)]
    out.append(tabla(filas, ["Topic", "Reviewer", "Date", "Result"]))
    out.append(up())
    # 10
    out.append("""<section id="send"><h2>10. How to send comments</h2>
<p>Any format is fine: an email, a list, or a screenshot with notes. Please say <strong>which page</strong>, <strong>which section</strong> (sections and activities are numbered), and, for exercises, <strong>what you typed</strong>: the practice exercises change every time, so a screenshot helps a lot. Send your comments to José M. Fernández (Zhema).</p>
<p>If you also teach science, social studies, or reading and writing, the page <a href="whats-next.html">What comes next</a> shows the plan for those subjects, and your ideas are welcome there too.</p>
""")
    out.append(up())
    out.append(FOOT)
    return "\n".join(out)


A = 'target="_blank" rel="noopener"'

N3 = dict(
    temas=["Rules of exponents", "Scientific notation", "Radicals and the real numbers", "Linear algebra",
           "Inequalities and formulas", "Advanced geometry", "Volume and data analysis", "Counting and probability"],
    intro="""<p>Thank you for helping again. Math Level 3 of LearnGED is now complete: <strong>24 lessons and 24 practice pages</strong>, in English and in Spanish. Level 3 opens the route <strong>Prepare for the GED</strong>: the rules of exponents, scientific notation, radicals and the real numbers, linear equations and inequalities, formulas, angles, the Pythagorean theorem, similar figures, volume, box plots and histograms, and counting and probability.</p>
<p>A level is marked 🟢 <strong>ready</strong> only after a GED teacher who teaches in English has reviewed it. The <a href="./">Level 1 guide</a> explains the general style and the <a href="level-2.html">Level 2 guide</a> the conventions of the earlier levels; this guide focuses on what is new in Level 3.</p>""",
    extras="""<h3>Extra pages in Level 3</h3>
<ul>
<li><a href="/math/level-3/topic-1-check.html" %(a)s>Topic 1 check</a>: the five rules of exponents together, before moving on.</li>
<li><a href="/math/level-3/speed-irrationals.html" %(a)s>Speed practice: irrational numbers</a> (Lesson 3.3).</li>
<li>Explore pages, where the student moves the figure and watches the math: <a href="/math/level-3/explore-angles.html" %(a)s>angles and a transversal</a> (6.1), <a href="/math/level-3/explore-pythagoras.html" %(a)s>the Pythagorean theorem</a> (6.2), <a href="/math/level-3/explore-similar.html" %(a)s>similar triangles</a> (6.3), <a href="/math/level-3/explore-chance.html" %(a)s>dice, cards, and spinners</a> and <a href="/math/level-3/explore-tree.html" %(a)s>tree diagrams and two-way tables</a> (8.2).</li>
<li><a href="/math/level-3/project-level-3.html" %(a)s>Final project template</a> (saved in the browser, exported to PDF) and <a href="/math/level-3/final-check-level-3.html" %(a)s>final check</a>: 25 questions, passing score 18.</li>
<li>The practice page of Lesson 8.3 is a review of the whole level, with a searchable index of every practice activity.</li>
</ul>""" % {"a": A},
    muestras="<strong>1.2</strong> (zero and negative exponents), <strong>2.2</strong> (scientific notation with the calculator), <strong>3.1</strong> (simplifying radicals), <strong>4.2</strong> (variables on both sides), <strong>5.1</strong> (inequalities), <strong>6.2</strong> (Pythagorean theorem), <strong>7.2</strong> (box plots), and <strong>8.1</strong> (permutations and combinations)",
    nuevo=[
        "<strong>Algebra you can see.</strong> Exponents are shown as repeated factors that cancel, and equations are solved on a balance scale that shows how each move keeps both sides equal.",
        "<strong>Answers in more than one form.</strong> The practice pages accept equivalent forms where it makes sense (a fraction or a decimal, 36π or a decimal). Scientific notation is typed in two boxes: the number and the power of 10.",
        "<strong>The calculator in context.</strong> The TI-30XS simulator is used with the ×10ⁿ key (scientific notation), the square root, π, and nPr / nCr. Topic 8 insists on telling P from C: does the order matter?",
        "<strong>Figures drawn by the page.</strong> Angles with a transversal, right triangles, similar figures, solids, box plots, and histograms are drawn with their measurements, and each has a text description for screen readers.",
        "<strong>Explore pages</strong> for geometry and probability (see the list above), and a <strong>review of the whole level</strong> in the practice page of Lesson 8.3.",
        "<strong>Final project and final check.</strong> The project is a small investigation with the student's own data; the final check has 25 questions.",
    ],
    pista="When you multiply both sides by a negative number, the inequality sign flips.",
    dos="does the order matter: permutation or combination?",
    convenciones=[
        ["Exponents", "Final answers use positive exponents: x⁻³ is written 1/x³."],
        ["Scientific notation", "a × 10ⁿ with 1 ≤ a &lt; 10, typed in two boxes (3.2 and 5 for 3.2 × 10⁵). On the TI-30XS, the key is ×10ⁿ."],
        ["Radicals", "Simplest form: 3√2, not √18 (no perfect-square factor left under the root). The decimal from the calculator is used to check the answer."],
        ["Real numbers", "Natural, whole, integer, rational, and irrational, shown as nested sets and on the number line."],
        ["Equations", "Variables on both sides; special cases are named “no solution” and “all real numbers (infinitely many solutions)”."],
        ["Inequalities", "&lt;, &gt;, ≤, ≥. On the number line: open circle for &lt; and &gt;, closed circle for ≤ and ≥. The sign flips when both sides are multiplied or divided by a negative number."],
        ["Formulas", "“Solve the formula for…” (for example, solve d = rt for t). The letters are those of the GED formula sheet."],
        ["Angles", "Degrees. Pairs: complementary, supplementary, vertical, corresponding, alternate interior, alternate exterior."],
        ["Pythagorean theorem", "a² + b² = c², c is the hypotenuse; the converse tells whether a triangle is a right triangle."],
        ["Similar figures", "Scale factor and proportions; scale drawings use inches, feet, and miles."],
        ["Volume", "V = Bh for prisms and cylinders; π answers as 36π or as a decimal. US units: cubic inches, cubic feet, gallons."],
        ["Quartiles", "Method of halves: Q1 is the median of the lower half and Q3 the median of the upper half; with an odd number of data, the median goes into neither half. IQR = Q3 − Q1."],
        ["Histograms", "Equal intervals (bins); the left end is included and the right end is not, unless the page says otherwise."],
        ["Counting", "Counting principle, nPr = n!/(n − r)!, nCr = n!/(r!(n − r)!). Probability accepted as a fraction, a decimal, or a percent."],
    ],
    glosario=[
        ["exponente negativo · exponente cero", "negative exponent · zero exponent", ""],
        ["notación científica · orden de magnitud", "scientific notation · order of magnitude", ""],
        ["radical · radicando · forma simplificada", "radical · radicand · simplest form", ""],
        ["números racionales · irracionales · reales", "rational · irrational · real numbers", ""],
        ["término · coeficiente · términos semejantes", "term · coefficient · like terms", ""],
        ["ecuación lineal · despejar", "linear equation · solve for", "Spanish uses one verb, <em>despejar</em>, for “isolate” and “solve for”."],
        ["desigualdad · inecuación", "inequality", "Spanish uses both words; we use <em>desigualdad</em>."],
        ["fórmula literal", "literal equation · formula", "See question 6."],
        ["ángulos complementarios · suplementarios", "complementary · supplementary angles", ""],
        ["ángulos opuestos por el vértice", "vertical angles", ""],
        ["alternos internos · alternos externos · correspondientes", "alternate interior · alternate exterior · corresponding", ""],
        ["recta secante (transversal)", "transversal", ""],
        ["hipotenusa · catetos", "hypotenuse · legs", ""],
        ["figuras semejantes · factor de escala", "similar figures · scale factor", ""],
        ["teorema de Tales", "Thales' theorem", "See question 5."],
        ["prisma · cilindro · base · altura", "prism · cylinder · base · height", ""],
        ["diagrama de caja (y bigotes)", "box plot (box-and-whisker plot)", ""],
        ["cuartil · rango intercuartílico", "quartile · interquartile range (IQR)", ""],
        ["histograma · intervalo (clase)", "histogram · interval (bin)", ""],
        ["principio de conteo · permutación · combinación", "counting principle · permutation · combination", ""],
        ["con reemplazo · sin reemplazo", "with replacement · without replacement", ""],
        ["eventos independientes · dependientes", "independent · dependent events", ""],
    ],
    preguntas=[
        "<strong>Positive exponents.</strong> We ask for final answers with positive exponents only (1/x³, not x⁻³). Is that how you grade?",
        "<strong>Radicals.</strong> We ask for simplest form (3√2) and use the calculator decimal as a check. Do your students need simplest form for the GED, or is a decimal from the calculator enough?",
        "<strong>Scientific notation.</strong> Is “×10ⁿ key” the name your students use for that key on the TI-30XS?",
        "<strong>Quartiles.</strong> We use the method of halves (the median goes into neither half). Is that the method you teach?",
        "<strong>“Thales' theorem”</strong> (title of Lesson 6.3) is common in Latin America. Would you rather call it only “similar triangles and scale drawings”?",
        "<strong>“Literal equations” or “solving formulas”?</strong> Which one do your students hear more (Lesson 5.3)?",
        "<strong>Permutations and combinations.</strong> Many students confuse nPr and nCr. Is the question “does the order matter?” enough, or do you use another rule of thumb?",
        "<strong>Final check.</strong> 25 questions, passing score 18 (72%). Is that a fair bar before Level 4?",
    ],
)

N4 = dict(
    temas=["Analytic geometry", "3D volume and polynomials", "Multiplying and factoring", "Quadratic equations",
           "Rational expressions", "Systems of linear equations", "Systems of inequalities and functions",
           "Modeling with functions and a practice GED test"],
    intro="""<p>Thank you for helping again. Math Level 4 of LearnGED is now complete: <strong>24 lessons and 24 practice pages</strong>, in English and in Spanish. With it, the four Math levels are done. Level 4 is the last step before the GED math test: the coordinate plane and the equation of a line, volume of spheres, cones, and pyramids, polynomials and factoring, quadratic equations, rational expressions, systems of equations and inequalities, and functions (linear, quadratic, and exponential).</p>
<p>A level is marked 🟢 <strong>ready</strong> only after a GED teacher who teaches in English has reviewed it. The <a href="level-3.html">Level 3 guide</a> explains the conventions shared by Levels 3 and 4; this guide focuses on what is new in Level 4.</p>""",
    extras="""<h3>Extra pages in Level 4</h3>
<ul>
<li><a href="/math/level-4/project-level-4.html" %(a)s>Final project “My math model”</a>: the student picks a quadratic or exponential situation, makes the graph with its labels, and the page checks the analysis (saved in the browser, exported to PDF).</li>
<li><a href="/math/level-4/final-check-level-4.html" %(a)s>Final check</a>: 30 questions, passing score 21.</li>
<li>The practice page of Lesson 8.3 is a review of the whole level: mixed practice from the eight topics and a searchable index of every practice activity.</li>
</ul>""" % {"a": A},
    muestras="<strong>1.2</strong> (slope), <strong>1.3</strong> (equations of a line), <strong>3.3</strong> (factoring trinomials), <strong>4.3</strong> (quadratic formula), <strong>6.1</strong> (systems by substitution), <strong>7.1</strong> (graphing inequalities), <strong>7.2</strong> (functions), and <strong>8.1</strong> (the parabola)",
    nuevo=[
        "<strong>An interactive coordinate plane.</strong> The student marks points with the mouse, a finger, or the arrow keys, and drags points to see the slope and the line change.",
        "<strong>Graphs drawn by the page.</strong> Lines, systems, solution regions of inequalities, parabolas, and exponential curves are drawn in the browser, with labels placed away from the axes and from the other lines.",
        "<strong>Step by step.</strong> Most activities start with a “step by step” block that shows one move at a time before the student tries alone.",
        "<strong>Answer checking for algebra.</strong> The pages read polynomials (3x^2 − 2x + 5), factored forms (2(x + 5)(x − 5)), ordered pairs, and solutions such as x = −3 or x = 5. They check that a factorization is correct <em>and</em> complete.",
        "<strong>Feedback for systems.</strong> If a student's ordered pair is wrong, the page says whether it fits one equation but not the other.",
        "<strong>Final project and final check</strong> (see above), and a review of the whole level in Lesson 8.3.",
    ],
    pista="Your point fits the first equation but not the second: check the substitution.",
    dos="solid line or dashed line?",
    convenciones=[
        ["Ordered pairs", "(x, y), with the x-coordinate first."],
        ["Distance and midpoint", "d = √((x₂ − x₁)² + (y₂ − y₁)²) and M = ((x₁ + x₂)/2, (y₁ + y₂)/2). Negative coordinates go in parentheses when substituted."],
        ["Slope", "m = (y₂ − y₁)/(x₂ − x₁): “rise over run”. A horizontal line has slope 0; a vertical line has undefined slope."],
        ["Equation of a line", "Slope-intercept y = mx + b, point-slope y − y₁ = m(x − x₁), and standard form Ax + By = C. Parallel lines have the same slope; perpendicular slopes multiply to −1."],
        ["Volume and surface area", "The formulas of the GED formula sheet. π answers as 36π or as a decimal (with the calculator's π key or 3.14). US units: inches, feet, cubic feet, gallons."],
        ["Polynomials", "Standard form, highest degree first. Students type exponents with ^ (3x^2)."],
        ["Multiplying", "FOIL for two binomials, plus the special products (a + b)², (a − b)², and (a + b)(a − b)."],
        ["Factoring", "Always the greatest common factor first, then difference of squares or trinomials; the ac method when a ≠ 1. The answer must be factored completely."],
        ["Quadratic equations", "Solved by factoring, by completing the square, or with the quadratic formula. Solutions such as x = −3 or x = 5; rounded answers to the hundredth are accepted."],
        ["Rational expressions", "Factor, then cancel factors (never terms). Excluded values are stated: x ≠ 2."],
        ["Systems", "Solution as an ordered pair. Three kinds: one solution, no solution, infinitely many solutions."],
        ["Inequalities in two variables", "Solid line for ≤ and ≥, dashed line for &lt; and &gt;; a test point (usually (0, 0)) tells which side to shade. Only the solution region is shaded."],
        ["Functions", "f(x) notation, domain and range, the vertical line test, and average rate of change = (f(b) − f(a))/(b − a)."],
        ["Quadratic and exponential models", "Vertex at x = −b/(2a). Exponential y = a · bˣ (growth if b &gt; 1, decay if 0 &lt; b &lt; 1). Compound interest A = P(1 + r/n)^(nt), money rounded to the cent. Heights in feet, distances in miles."],
    ],
    glosario=[
        ["plano cartesiano · par ordenado · cuadrante", "coordinate plane · ordered pair · quadrant", ""],
        ["distancia · punto medio", "distance · midpoint", ""],
        ["pendiente · intercepto en y", "slope · y-intercept", "Also <em>ordenada al origen</em> in some countries."],
        ["forma pendiente-intercepto · punto-pendiente · forma estándar", "slope-intercept · point-slope · standard form", "See question 1."],
        ["esfera · cono · pirámide · área superficial", "sphere · cone · pyramid · surface area", ""],
        ["polinomio · monomio · binomio · trinomio · grado", "polynomial · monomial · binomial · trinomial · degree", ""],
        ["productos notables", "special products", ""],
        ["factor común · diferencia de cuadrados", "greatest common factor (GCF) · difference of squares", ""],
        ["trinomio cuadrado perfecto", "perfect square trinomial", ""],
        ["ecuación cuadrática · completar el cuadrado", "quadratic equation · completing the square", ""],
        ["fórmula cuadrática (general) · discriminante", "quadratic formula · discriminant", ""],
        ["expresión racional · valores excluidos", "rational expression · excluded values", ""],
        ["mínimo común denominador", "least common denominator (LCD)", ""],
        ["sistema de ecuaciones · sustitución · eliminación", "system of equations · substitution · elimination", ""],
        ["región solución (región factible)", "solution region (feasible region)", ""],
        ["línea continua · línea discontinua (punteada)", "solid line · dashed line", ""],
        ["función · dominio · rango", "function · domain · range", "Spanish also says <em>recorrido</em> for range."],
        ["prueba de la recta vertical", "vertical line test", ""],
        ["composición de funciones", "composition of functions", ""],
        ["tasa de cambio promedio", "average rate of change", ""],
        ["parábola · vértice · eje de simetría", "parabola · vertex · axis of symmetry", ""],
        ["crecimiento · decaimiento exponencial", "exponential growth · decay", ""],
        ["interés compuesto · logaritmo", "compound interest · logarithm", "See question 5."],
    ],
    preguntas=[
        "<strong>Standard form.</strong> We write Ax + By = C, with whole numbers and A positive. Is that the form your students know?",
        "<strong>FOIL.</strong> Do you teach FOIL, or do you prefer the distributive property or the box (area) method only?",
        "<strong>Factoring trinomials with a ≠ 1.</strong> We teach the ac method. Do your students know another method (trial and error, the box method)?",
        "<strong>Completing the square</strong> (Lesson 4.2) is rarely needed on the GED. Is it worth keeping as the bridge to the quadratic formula?",
        "<strong>Compound interest and logarithms</strong> (Lesson 8.2) are not on the GED formula sheet. Should we keep them as enrichment?",
        "<strong>Rational expressions</strong> (Topic 5): is the depth right for GED students, or too much?",
        "<strong>Graphs.</strong> Are the graphs easy to read on a phone? Is anything too small?",
        "<strong>Final check.</strong> 30 questions, passing score 21 (70%). Is that a fair signal that a student is ready for the GED math test?",
    ],
)


def main():
    for n, d in ((3, N3), (4, N4)):
        p = os.path.join(RAIZ, "review", "level-%d.html" % n)
        with open(p, "w", encoding="utf-8") as f:
            f.write(guia(n, d))
        print("ok", p)


if __name__ == "__main__":
    main()
