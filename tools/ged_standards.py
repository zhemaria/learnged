"""GED® Mathematical Reasoning standards for LearnGED.

Source: GED Testing Service, Assessment Guide for Educators: Mathematical Reasoning (June 2016),
Chapter 1, Assessment Targets and Mathematical Practices.

What this script does (run it again after adding or changing a lesson):
  1. In every math lesson listed in LESSONS, writes a "GED® standards" box right after
     "What you will learn" (between the <!-- GED-STANDARDS --> markers).
  2. Builds math/ged-standards.html, the standards map for teachers.

Usage: python3 tools/ged_standards.py   (from the root of the learnged repository)
"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------- Official targets (indicator text as written in the guide; the long examples
# in A.5.e, A.7.a and A.7.d are left out) ----------
TARGETS = {
 "Q.1": "Apply number sense concepts, including ordering rational numbers, absolute value, multiples, factors, and exponents",
 "Q.1.a": "Order fractions and decimals, including on a number line.",
 "Q.1.b": "Apply number properties involving multiples and factors, such as using the least common multiple, greatest common factor, or distributive property to rewrite numeric expressions.",
 "Q.1.c": "Apply rules of exponents in numerical expressions with rational exponents to write equivalent expressions with rational exponents.",
 "Q.1.d": "Identify absolute value or a rational number as its distance from 0 on the number line and determine the distance between two rational numbers on the number line, including using the absolute value of their difference.",
 "Q.2": "Add, subtract, multiply, divide, and use exponents and roots of rational, fraction and decimal numbers",
 "Q.2.a": "Perform addition, subtraction, multiplication, and division on rational numbers.",
 "Q.2.b": "Perform computations and write numerical expressions with squares and square roots of positive, rational numbers.",
 "Q.2.c": "Perform computations and write numerical expressions with cubes and cube roots of rational numbers.",
 "Q.2.d": "Determine when a numerical expression is undefined.",
 "Q.2.e": "Solve one-step or multi-step arithmetic, real world problems involving the four operations with rational numbers, including those involving scientific notation.",
 "Q.3": "Calculate and use ratios, percents and scale factors",
 "Q.3.a": "Compute unit rates. Examples include but are not limited to: unit pricing, constant speed, persons per square mile, BTUs per cubic foot.",
 "Q.3.b": "Use scale factors to determine the magnitude of a size change. Convert between actual drawings and scale drawings.",
 "Q.3.c": "Solve multistep, arithmetic, real-world problems using ratios or proportions including those that require converting units of measure.",
 "Q.3.d": "Solve two-step, arithmetic, real world problems involving percents. Examples include but are not limited to: simple interest, tax, markups and markdowns, gratuities and commissions, percent increase and decrease.",
 "Q.4": "Calculate dimensions, perimeter, circumference, and area of two-dimensional figures",
 "Q.4.a": "Compute the area and perimeter of triangles and rectangles. Determine side lengths of triangles and rectangles when given area or perimeter.",
 "Q.4.b": "Compute the area and circumference of circles. Determine the radius or diameter when given area or circumference.",
 "Q.4.c": "Compute the perimeter of a polygon. Given a geometric formula, compute the area of a polygon. Determine side lengths of the figure when given the perimeter or area.",
 "Q.4.d": "Compute perimeter and area of 2-D composite geometric figures, which could include circles, given geometric formulas as needed.",
 "Q.4.e": "Use the Pythagorean theorem to determine unknown side lengths in a right triangle.",
 "Q.5": "Calculate dimensions, surface area, and volume of three-dimensional figures",
 "Q.5.a": "When given geometric formulas, compute volume and surface area of rectangular prisms. Solve for side lengths or height, when given volume or surface area.",
 "Q.5.b": "When given geometric formulas, compute volume and surface area of cylinders. Solve for height, radius, or diameter when given volume or surface area.",
 "Q.5.c": "When given geometric formulas, compute volume and surface area of right prisms. Solve for side lengths or height, when given volume or surface area.",
 "Q.5.d": "When given geometric formulas, compute volume and surface area of right pyramids and cones. Solve for side lengths, height, radius, or diameter when given volume or surface area.",
 "Q.5.e": "When given geometric formulas, compute volume and surface area of spheres. Solve for radius or diameter when given the surface area.",
 "Q.5.f": "Compute surface area and volume of composite 3-D geometric figures, given geometric formulas as needed.",
 "Q.6": "Interpret and create data displays",
 "Q.6.a": "Represent, display, and interpret categorical data in bar graphs or circle graphs.",
 "Q.6.b": "Represent, display, and interpret data involving one variable plots on the real number line including dot plots, histograms, and box plots.",
 "Q.6.c": "Represent, display, and interpret data involving two variables in tables and the coordinate plane including scatter plots and graphs.",
 "Q.7": "Calculate and use mean, median, mode and weighted average",
 "Q.7.a": "Calculate the mean, median, mode and range. Calculate a missing data value, given the average and all the missing data values but one, as well as calculating the average, given the frequency counts of all the data values, and calculating a weighted average.",
 "Q.8": "Utilize counting techniques and determine probabilities",
 "Q.8.a": "Use counting techniques to solve problems and determine combinations and permutations.",
 "Q.8.b": "Determine the probability of simple and compound events.",
 "A.1": "Write, evaluate, and compute with expressions and polynomials",
 "A.1.a": "Add, subtract, factor, multiply and expand linear expressions with rational coefficients.",
 "A.1.b": "Evaluate linear expressions by substituting integers for unknown quantities.",
 "A.1.c": "Write linear expressions as part of word-to-symbol translations or to represent common settings.",
 "A.1.d": "Add, subtract, multiply polynomials, including multiplying two binomials, or divide factorable polynomials.",
 "A.1.e": "Evaluate polynomial expressions by substituting integers for unknown quantities.",
 "A.1.f": "Factor polynomial expressions.",
 "A.1.g": "Write polynomial expressions as part of word-to-symbol translations or to represent common settings.",
 "A.1.h": "Add, subtract, multiply and divide rational expressions.",
 "A.1.i": "Evaluate rational expressions by substituting integers for unknown quantities.",
 "A.1.j": "Write rational expressions as part of word-to-symbol translations or to represent common settings.",
 "A.2": "Write, manipulate, and solve linear equations",
 "A.2.a": "Solve one-variable linear equations with rational number coefficients, including equations whose solutions require expanding expressions using the distributive property and collecting like terms or equations with coefficients represented by letters.",
 "A.2.b": "Solve real-world problems involving linear equations.",
 "A.2.c": "Write one-variable and multi-variable linear equations to represent context.",
 "A.2.d": "Solve a system of two simultaneous linear equations by graphing, substitution, or linear combination. Solve real-world problems leading to a system of linear equations.",
 "A.3": "Write, manipulate, solve, and graph linear inequalities",
 "A.3.a": "Solve linear inequalities in one variable with rational number coefficients.",
 "A.3.b": "Identify or graph the solution to a one variable linear inequality on a number line.",
 "A.3.c": "Solve real-world problems involving inequalities.",
 "A.3.d": "Write linear inequalities in one variable to represent context.",
 "A.4": "Write, manipulate, and solve quadratic equations",
 "A.4.a": "Solve quadratic equations in one variable with rational coefficients and real solutions, using appropriate methods (e.g., quadratic formula, completing the square, factoring, inspection).",
 "A.4.b": "Write one-variable quadratic equations to represent context.",
 "A.5": "Connect and interpret graphs and functions",
 "A.5.a": "Locate points in the coordinate plane.",
 "A.5.b": "Determine the slope of a line from a graph, equation, or table.",
 "A.5.c": "Interpret unit rate as the slope in a proportional relationship.",
 "A.5.d": "Graph two-variable linear equations.",
 "A.5.e": "For a function that models a linear or nonlinear relationship between two quantities, interpret key features of graphs and tables in terms of quantities, and sketch graphs showing key features given a verbal description of the relationship.",
 "A.6": "Connect coordinates, lines, and equations",
 "A.6.a": "Write the equation of a line with a given slope through a given point.",
 "A.6.b": "Write the equation of a line passing through two given distinct points.",
 "A.6.c": "Use slope to identify parallel and perpendicular lines and to solve geometric problems.",
 "A.7": "Compare, represent, and evaluate functions",
 "A.7.a": "Compare two different proportional relationships represented in different ways.",
 "A.7.b": "Represent or identify a function in a table or graph as having exactly one output (one element in the range) for each input (each element in the domain).",
 "A.7.c": "Evaluate linear and quadratic functions for values in their domain when represented using function notation.",
 "A.7.d": "Compare properties of two linear or quadratic functions each represented in a different way (algebraically, numerically in tables, graphically or by verbal descriptions).",
 "MP.1": "Building Solution Pathways and Lines of Reasoning",
 "MP.1.a": "Search for and recognize entry points for solving a problem.",
 "MP.1.b": "Plan a solution pathway or outline a line of reasoning.",
 "MP.1.c": "Select the best solution pathway, according to given criteria.",
 "MP.1.d": "Recognize and identify missing information that is required to solve a problem.",
 "MP.1.e": "Select the appropriate mathematical technique(s) to use in solving a problem or a line of reasoning.",
 "MP.2": "Abstracting Problems",
 "MP.2.a": "Represent real world problems algebraically.",
 "MP.2.b": "Represent real world problems visually.",
 "MP.2.c": "Recognize the important and salient attributes of a problem.",
 "MP.3": "Furthering Lines of Reasoning",
 "MP.3.a": "Build steps of a line of reasoning or solution pathway, based on previous step or givens.",
 "MP.3.b": "Complete the lines of reasoning of others.",
 "MP.3.c": "Improve or correct a flawed line of reasoning.",
 "MP.4": "Mathematical Fluency",
 "MP.4.a": "Manipulate and solve arithmetic expressions.",
 "MP.4.b": "Transform and solve algebraic expressions.",
 "MP.4.c": "Display data or algebraic expressions graphically.",
 "MP.5": "Evaluating Reasoning and Solution Pathways",
 "MP.5.a": "Recognize flaws in others' reasoning.",
 "MP.5.b": "Recognize and use counterexamples.",
 "MP.5.c": "Identify the information required to evaluate a line of reasoning.",
}


# ---------- College and Career Readiness (CCR) Standards for Adult Education (Pimentel, 2013) ----------
# Level letter, then the standard (examples left out). The codes are the Common Core codes the CCR uses.
CCR = {
 "3.OA.3": ("B", "Use multiplication and division within 100 to solve word problems in situations involving equal groups, arrays, and measurement quantities."),
 "3.OA.5": ("B", "Apply properties of operations as strategies to multiply and divide (commutative, associative, and distributive properties)."),
 "3.OA.7": ("B", "Fluently multiply and divide within 100. Know from memory all products of two one-digit numbers."),
 "3.OA.8": ("B", "Solve two-step word problems using the four operations. Assess the reasonableness of answers using mental computation and estimation strategies including rounding."),
 "4.NBT.1": ("C", "Recognize that in a multi-digit whole number, a digit in one place represents ten times what it represents in the place to its right."),
 "4.NBT.2": ("C", "Read and write multi-digit whole numbers using base-ten numerals, number names, and expanded form. Compare two multi-digit numbers using >, =, and < symbols."),
 "4.NBT.3": ("C", "Use place value understanding to round multi-digit whole numbers to any place."),
 "4.NBT.4": ("C", "Fluently add and subtract multi-digit whole numbers using the standard algorithm."),
 "4.NBT.5": ("C", "Multiply a whole number of up to four digits by a one-digit whole number, and multiply two two-digit numbers, using strategies based on place value and the properties of operations."),
 "4.NBT.6": ("C", "Find whole-number quotients and remainders with up to four-digit dividends and one-digit divisors."),
 "4.OA.3": ("C", "Solve multistep word problems posed with whole numbers and having whole-number answers using the four operations, including problems in which remainders must be interpreted. Assess the reasonableness of answers using mental computation and estimation strategies including rounding."),
 "5.NBT.1": ("C", "Recognize that in a multi-digit number, a digit in one place represents 10 times as much as it represents in the place to its right and 1/10 of what it represents in the place to its left."),
 "5.NBT.3": ("C", "Read, write, and compare decimals to thousandths."),
 "5.NBT.4": ("C", "Use place value understanding to round decimals to any place."),
 "5.NBT.5": ("C", "Fluently multiply multi-digit whole numbers using the standard algorithm."),
 "5.NBT.6": ("C", "Find whole-number quotients of whole numbers with up to four-digit dividends and two-digit divisors."),
 "5.NBT.7": ("C", "Add, subtract, multiply, and divide decimals to hundredths, using concrete models or drawings and strategies based on place value; relate the strategy to a written method and explain the reasoning used. (Applications involving financial literacy should be used.)"),
 "3.NF.1": ("B", "Understand a fraction 1/b as the quantity formed by 1 part when a whole is partitioned into b equal parts; understand a fraction a/b as the quantity formed by a parts of size 1/b."),
 "3.NF.3": ("B", "Explain equivalence of fractions in special cases, and compare fractions by reasoning about their size."),
 "4.NF.1": ("C", "Explain why a fraction a/b is equivalent to a fraction (n × a)/(n × b) by using visual fraction models. Use this principle to recognize and generate equivalent fractions."),
 "4.NF.2": ("C", "Compare two fractions with different numerators and different denominators, e.g., by creating common denominators or numerators, or by comparing to a benchmark fraction such as 1/2. Record the results of comparisons with symbols >, =, or <, and justify the conclusions."),
 "4.OA.4": ("C", "Find all factor pairs for a whole number in the range 1–100. Recognize that a whole number is a multiple of each of its factors. Determine whether a given whole number in the range 1–100 is prime or composite."),
 "6.NS.4": ("C", "Find the greatest common factor of two whole numbers less than or equal to 100 and the least common multiple of two whole numbers less than or equal to 12. Use the distributive property to express a sum of two whole numbers with a common factor as a multiple of a sum of two whole numbers with no common factor."),
 "4.NF.3": ("C", "Understand a fraction a/b with a > 1 as a sum of fractions 1/b: understand addition and subtraction of fractions as joining and separating parts referring to the same whole, and solve word problems involving addition and subtraction of fractions with like denominators."),
 "5.NF.1": ("C", "Add and subtract fractions with unlike denominators (including mixed numbers) by replacing given fractions with equivalent fractions in such a way as to produce an equivalent sum or difference of fractions with like denominators. For example, 2/3 + 5/4 = 8/12 + 15/12 = 23/12."),
 "5.NF.2": ("C", "Solve word problems involving addition and subtraction of fractions referring to the same whole, including cases of unlike denominators. Use benchmark fractions and number sense of fractions to estimate mentally and assess the reasonableness of answers. For example, recognize an incorrect result 2/5 + 1/2 = 3/7, by observing that 3/7 < 1/2."),
 "4.NF.6": ("C", "Use decimal notation for fractions with denominators 10 or 100. For example, rewrite 0.62 as 62/100."),
 "5.NF.3": ("C", "Interpret a fraction as division of the numerator by the denominator (a/b = a ÷ b)."),
 "7.NS.2d": ("D", "Convert a rational number to a decimal using long division; know that the decimal form of a rational number terminates in 0s or eventually repeats."),
 "6.NS.3": ("C", "Fluently add, subtract, multiply, and divide multi-digit decimals using the standard algorithm for each operation."),
}
CCR_FUENTE = "Pimentel, S. (2013). <cite>College and Career Readiness Standards for Adult Education</cite>. U.S. Department of Education, Office of Vocational and Adult Education"
CCR_ORDEN = list(CCR)

# ---------- Lessons and the targets they work on ----------
# "direct": the lesson works on the target as the GED test asks it.
# "builds": the lesson builds a skill the target needs (Level 1 works with whole numbers first).
# "mp":     Mathematical Practices the lesson practices.
LESSONS = [
 ("level-1/lesson-1-1.html", "1.1", "Place value and whole numbers",
  {"direct": [], "builds": ["Q.1.a"], "mp": ["MP.4.a"], "ccr": ["4.NBT.1", "4.NBT.2", "4.NBT.3"]}),
 ("level-1/lesson-1-2.html", "1.2", "Adding and subtracting whole numbers",
  {"direct": [], "builds": ["Q.2.a"], "mp": ["MP.4.a", "MP.3.a"], "ccr": ["4.NBT.4"]}),
 ("level-1/lesson-1-3.html", "1.3", "Adding and subtracting in word problems",
  {"direct": [], "builds": ["Q.2.e"], "mp": ["MP.1.a", "MP.1.b", "MP.2.c", "MP.4.a"], "ccr": ["3.OA.8", "4.OA.3"]}),
 ("level-1/lesson-2-1.html", "2.1", "Multiplying whole numbers",
  {"direct": [], "builds": ["Q.2.a", "Q.1.b"], "mp": ["MP.4.a"], "ccr": ["3.OA.5", "3.OA.7", "4.NBT.5", "5.NBT.5"]}),
 ("level-1/lesson-2-2.html", "2.2", "Dividing whole numbers",
  {"direct": [], "builds": ["Q.2.a", "Q.2.e"], "mp": ["MP.4.a", "MP.3.a"], "ccr": ["4.NBT.6", "5.NBT.6", "4.OA.3"]}),
 ("level-1/lesson-2-3.html", "2.3", "Multiplication and division in word problems",
  {"direct": [], "builds": ["Q.2.e", "Q.1.b"], "mp": ["MP.1.a", "MP.1.e", "MP.2.c", "MP.4.a"], "ccr": ["3.OA.3", "3.OA.5", "4.OA.3"]}),
 ("level-1/lesson-3-1.html", "3.1", "Decimals: read, write, compare, and round",
  {"direct": ["Q.1.a"], "builds": [], "mp": ["MP.4.a"], "ccr": ["5.NBT.1", "5.NBT.3", "5.NBT.4"]}),
 ("level-1/lesson-3-2.html", "3.2", "Operations with decimals",
  {"direct": ["Q.2.a", "Q.2.e"], "builds": [], "mp": ["MP.4.a", "MP.1.e", "MP.5.c"], "ccr": ["5.NBT.7", "6.NS.3"]}),
 ("level-1/lesson-3-3.html", "3.3", "Decimals in context and equivalent forms",
  {"direct": ["Q.2.e"], "builds": ["Q.1.a", "Q.2.a"], "mp": ["MP.1.a", "MP.1.b", "MP.2.c", "MP.4.a"], "ccr": ["5.NF.3", "4.NF.6", "7.NS.2d", "5.NBT.7"]}),
 ("level-1/lesson-4-1.html", "4.1", "Equivalent fractions: simplify and compare",
  {"direct": ["Q.1.a"], "builds": ["Q.1.b"], "mp": ["MP.2.b", "MP.3.a", "MP.4.a"], "ccr": ["3.NF.1", "3.NF.3", "4.NF.1", "4.NF.2"]}),
 ("level-1/lesson-4-1-gcf-lcm.html", "4.1 (complement)", "Complement: factors, multiples, GCF, and LCM",
  {"direct": ["Q.1.b"], "builds": [], "mp": ["MP.1.e", "MP.2.c", "MP.4.a"], "ccr": ["4.OA.4", "6.NS.4"]}),
 ("level-1/lesson-4-2.html", "4.2", "Adding and subtracting fractions",
  {"direct": ["Q.2.a", "Q.2.e"], "builds": ["Q.1.b"], "mp": ["MP.2.b", "MP.3.a", "MP.4.a", "MP.5.a"], "ccr": ["4.NF.3", "5.NF.1", "5.NF.2"]}),
]

SOURCE = "GED Testing Service, <cite>Assessment Guide for Educators: Mathematical Reasoning</cite> (2016)"
e = html.escape

def li(code, cls):
    return f'<li><span class="std-cod {cls}">{code}</span> {e(TARGETS[code])}</li>'

def box(m):
    parts = ['<!-- GED-STANDARDS -->', '<details class="estandares" id="ged-standards">',
             '<summary><span aria-hidden="true">🎓</span> Standards for this lesson (GED® and CCR)</summary>', '<div class="std-cuerpo">']
    if m["direct"]:
        parts.append('<p class="std-tit">This lesson works on these GED® Assessment Targets:</p><ul>' + "".join(li(c, "std-dir") for c in m["direct"]) + '</ul>')
    if m["builds"]:
        parts.append('<p class="std-tit">This lesson builds the foundation for these GED® Assessment Targets:</p><ul>' + "".join(li(c, "std-base") for c in m["builds"]) + '</ul>')
    if m["mp"]:
        parts.append('<p class="std-tit">Mathematical Practices you use:</p><ul>' + "".join(li(c, "std-mp") for c in m["mp"]) + '</ul>')
    if m.get("ccr"):
        parts.append('<p class="std-tit">College and Career Readiness (CCR) Standards for Adult Education:</p><ul>' + "".join(f'<li><span class="std-cod std-ccr">{c}</span> <span class="std-nivel">Level {CCR[c][0]}</span> {e(CCR[c][1])}</li>' for c in m["ccr"]) + '</ul>')
    parts.append(f'<p class="std-fuente">Sources: {SOURCE}; {CCR_FUENTE}. See the <a href="../ged-standards.html">standards map for all the lessons</a>.</p>')
    parts += ['</div>', '</details>', '<!-- /GED-STANDARDS -->']
    return "\n".join(parts)

def insert(path, m):
    full = os.path.join(ROOT, "math", path)
    s = open(full, encoding="utf-8").read()
    b = box(m)
    if "<!-- GED-STANDARDS -->" in s:
        s = re.sub(r"<!-- GED-STANDARDS -->.*?<!-- /GED-STANDARDS -->", lambda _: b, s, flags=re.S)
    else:
        # right after the "What you will learn" section
        i = s.index('<div class="caja caja-objetivo">')
        j = s.index("</section>", i)
        s = s[:j] + b + "\n" + s[j:]
    open(full, "w", encoding="utf-8").write(s)

def page():
    groups = [("Quantitative Problem Solving", "Q"), ("Algebraic Problem Solving", "A"), ("Mathematical Practices", "MP")]
    rows = []
    for title, pre in groups:
        rows.append(f'<h2 id="{pre.lower()}">{title}</h2>')
        heads = [c for c in TARGETS if c.startswith(pre + ".") and c.count(".") == 1]
        for h in heads:
            rows.append(f'<h3><span class="std-cod">{h}</span> {e(TARGETS[h])}</h3>')
            rows.append('<div class="tabla-scroll" role="region" tabindex="0" aria-label="' + h + ' (table you can scroll sideways)"><table class="std-tabla"><caption class="cap-oculto">' + h + ': indicators and the LearnGED lessons that teach them</caption><thead><tr><th scope="col">Code</th><th scope="col">Indicator</th><th scope="col">LearnGED lessons</th></tr></thead><tbody>')
            for c in [k for k in TARGETS if k.startswith(h + ".")]:
                links = []
                for path, num, name, m in LESSONS:
                    url = path
                    if c in m["direct"]: links.append(f'<a class="std-dir" href="{url}">Lesson {num}</a> <span class="std-tipo">works on it</span>')
                    elif c in m["builds"]: links.append(f'<a class="std-base" href="{url}">Lesson {num}</a> <span class="std-tipo">foundation</span>')
                    elif c in m["mp"]: links.append(f'<a class="std-mp" href="{url}">Lesson {num}</a>')
                cell = "<br>".join(links) if links else '<span class="std-pend">Coming in later lessons</span>'
                rows.append(f'<tr><th scope="row">{c}</th><td>{e(TARGETS[c])}</td><td>{cell}</td></tr>')
            rows.append('</tbody></table></div>')
    rows.append('<h2 id="ccr">College and Career Readiness (CCR) Standards for Adult Education</h2>')
    rows.append('<p>The GED® targets describe what the test asks. The CCR Standards describe the steps before it, by level (A to E). Level 1 lessons work mostly on Levels B and C. The list shows only the CCR standards that LearnGED lessons teach so far.</p>')
    rows.append('<div class="tabla-scroll" role="region" tabindex="0" aria-label="CCR Standards (table you can scroll sideways)"><table class="std-tabla"><caption class="cap-oculto">CCR Standards for Adult Education and the LearnGED lessons that teach them</caption><thead><tr><th scope="col">Code</th><th scope="col">Level</th><th scope="col">Standard</th><th scope="col">LearnGED lessons</th></tr></thead><tbody>')
    for c in CCR_ORDEN:
        links = [f'<a class="std-ccr" href="{p}">Lesson {n}</a>' for p, n, t, m in LESSONS if c in m.get("ccr", [])]
        rows.append(f'<tr><th scope="row">{c}</th><td>{CCR[c][0]}</td><td>{e(CCR[c][1])}</td><td>{"<br>".join(links)}</td></tr>')
    rows.append('</tbody></table></div>')
    lessons = "".join(f'<li><a href="{p}">Lesson {n} · {e(t)}</a>: ' + ", ".join(m["direct"] + m["builds"] + m["mp"]) + '</li>' for p, n, t, m in LESSONS)
    return f'''<!DOCTYPE html>
<!-- LearnGED · GED® Mathematical Reasoning standards map (built by tools/ged_standards.py; do not edit by hand) -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math standards map (GED® and CCR) · LearnGED</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lesson.css">
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="level-1/">Math · Level 1 lessons</a></nav>
<a class="saltar" href="#contenido">Skip to the standards</a>
<header class="principal"><div class="envoltura-header">
<p class="ruta">Math · For teachers</p>
<h1>Math standards map: GED® and CCR</h1>
<p class="lema">Which LearnGED lessons teach each GED® Assessment Target, Mathematical Practice, and College and Career Readiness Standard.</p>
</div></header>
<div class="envoltura" id="contenido">
<section>
<h2>How to read this map</h2>
<ul>
<li><span class="std-cod std-dir">works on it</span> The lesson teaches the target as the GED® test asks it.</li>
<li><span class="std-cod std-base">foundation</span> The lesson builds a skill the target needs. Level 1 starts with whole numbers; the test uses rational numbers (fractions, decimals, and negative numbers).</li>
<li>The Mathematical Practices are habits of reasoning. Many lessons practice them; the map lists the ones each lesson works on most.</li>
</ul>
<p>Jump to: <a href="#q">Quantitative Problem Solving</a> · <a href="#a">Algebraic Problem Solving</a> · <a href="#mp">Mathematical Practices</a> · <a href="#ccr">CCR Standards</a> · <a href="#by-lesson">By lesson</a></p>
<p class="std-fuente">Indicator text: {SOURCE}, Chapter 1. CCR Standards: {CCR_FUENTE}. GED® is a registered trademark of the American Council on Education (ACE), used under license by GED Testing Service LLC. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>
</section>
<section>
{chr(10).join(rows)}
</section>
<section>
<h2 id="by-lesson">By lesson</h2>
<ul>{lessons}</ul>
</section>
</div>
<footer><p>LearnGED · Math · GED® standards map</p><p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p></footer>
</body>
</html>
'''

if __name__ == "__main__":
    for path, num, name, m in LESSONS:
        for c in m["direct"] + m["builds"] + m["mp"]:
            assert c in TARGETS, c
        for c in m.get("ccr", []):
            assert c in CCR, c
        insert(path, m)
    open(os.path.join(ROOT, "math", "ged-standards.html"), "w", encoding="utf-8").write(page())
    print("ok:", len(LESSONS), "lessons")
