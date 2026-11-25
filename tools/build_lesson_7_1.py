"""Lesson 7.1 · Classifying 2D shapes — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json, math
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "7-1"
AZ, AZC, GR, TX_ = "#1565c0", "#e3f2fd", "#37474f", "#1a2330"

def txt(x, y, s, size=16, color=TX_, anchor="middle", peso=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{peso}" fill="{color}">{s}</text>'

def vocabulario():
    s = []
    # segment
    s.append(f'<line x1="30" y1="70" x2="180" y2="70" stroke="{AZ}" stroke-width="4"/><circle cx="30" cy="70" r="6" fill="{GR}"/><circle cx="180" cy="70" r="6" fill="{GR}"/>')
    s.append(txt(30, 50, "A") + txt(180, 50, "B") + txt(105, 120, t("line segment AB", "segmento AB"), 15))
    # parallel
    s.append(f'<line x1="230" y1="45" x2="400" y2="45" stroke="{AZ}" stroke-width="4"/><line x1="230" y1="90" x2="400" y2="90" stroke="{AZ}" stroke-width="4"/>')
    s.append(txt(315, 120, t("parallel lines", "rectas paralelas"), 15))
    # perpendicular
    s.append(f'<line x1="450" y1="95" x2="610" y2="95" stroke="{AZ}" stroke-width="4"/><line x1="530" y1="25" x2="530" y2="95" stroke="{AZ}" stroke-width="4"/><rect x="530" y="79" width="16" height="16" fill="none" stroke="{GR}" stroke-width="2"/>')
    s.append(txt(530, 120, t("perpendicular lines", "rectas perpendiculares"), 15))
    return svg("0 0 640 135", t("Three drawings. A line segment between point A and point B. Two parallel lines, side by side, that never meet. Two perpendicular lines that meet in a square corner, marked with a small square.",
                                "Tres dibujos. Un segmento entre el punto A y el punto B. Dos rectas paralelas, una al lado de la otra, que nunca se juntan. Dos rectas perpendiculares que se juntan en una esquina cuadrada, marcada con un cuadrito."), "".join(s))

def angulo(cx, cy, grados, etiqueta, nombre):
    L = 70
    a = math.radians(grados)
    x2, y2 = cx + L * math.cos(a), cy - L * math.sin(a)
    s = [f'<line x1="{cx}" y1="{cy}" x2="{cx + L}" y2="{cy}" stroke="{GR}" stroke-width="4"/><line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GR}" stroke-width="4"/>']
    if grados == 90:
        s.append(f'<rect x="{cx}" y="{cy - 16}" width="16" height="16" fill="none" stroke="{AZ}" stroke-width="2.5"/>')
    else:
        r = 26
        large = 1 if grados > 180 else 0
        s.append(f'<path d="M{cx + r},{cy} A{r},{r} 0 {large} 0 {cx + r * math.cos(a):.1f},{cy - r * math.sin(a):.1f}" fill="none" stroke="{AZ}" stroke-width="2.5"/>')
    s.append(txt(cx + 20, cy + 30, etiqueta, 15, AZ) + txt(cx + 20, cy + 50, nombre, 15))
    return "".join(s)

def angulos():
    s = angulo(40, 100, 45, "45°", t("acute", "agudo")) + angulo(200, 100, 90, "90°", t("right", "recto")) + angulo(370, 100, 135, "135°", t("obtuse", "obtuso")) + angulo(520, 100, 180, "180°", t("straight", "llano"))
    return svg("0 0 640 160", t("Four angles. An acute angle of 45 degrees. A right angle of 90 degrees, marked with a small square. An obtuse angle of 135 degrees. A straight angle of 180 degrees, which looks like a straight line.",
                                "Cuatro ángulos. Un ángulo agudo de 45 grados. Un ángulo recto de 90 grados, marcado con un cuadrito. Un ángulo obtuso de 135 grados. Un ángulo llano de 180 grados, que parece una línea recta."), s)

def marca(x1, y1, x2, y2, k):
    """k little tick marks at the middle of a side (equal sides have the same marks)."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L; nx, ny = -uy, ux
    s = ""
    for i in range(k):
        o = (i - (k - 1) / 2) * 7
        cx, cy = mx + ux * o, my + uy * o
        s += f'<line x1="{cx - nx * 8:.1f}" y1="{cy - ny * 8:.1f}" x2="{cx + nx * 8:.1f}" y2="{cy + ny * 8:.1f}" stroke="{AZ}" stroke-width="2.5"/>'
    return s

def poli(pts, fill=AZC):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" stroke="{GR}" stroke-width="3"/>'

def triangulos():
    s = []
    # by sides
    A = [(40, 150), (160, 150), (100, 46)]
    s.append(poli(A) + marca(*A[0], *A[1], 1) + marca(*A[1], *A[2], 1) + marca(*A[2], *A[0], 1) + txt(100, 180, t("equilateral", "equilátero"), 15))
    Bp = [(230, 150), (330, 150), (280, 40)]
    s.append(poli(Bp) + marca(*Bp[1], *Bp[2], 2) + marca(*Bp[2], *Bp[0], 2) + txt(280, 180, t("isosceles", "isósceles"), 15))
    C = [(400, 150), (600, 150), (450, 70)]
    s.append(poli(C) + txt(500, 180, t("scalene", "escaleno"), 15))
    return svg("0 0 640 195", t("Three triangles. An equilateral triangle with three equal sides, each marked with one tick. An isosceles triangle with two equal sides, marked with two ticks. A scalene triangle with three different sides, with no marks.",
                                "Tres triángulos. Un triángulo equilátero con tres lados iguales, cada uno marcado con una rayita. Un triángulo isósceles con dos lados iguales, marcados con dos rayitas. Un triángulo escaleno con tres lados distintos, sin marcas."), "".join(s))

def cuadrilateros():
    s = []
    figs = [([(20, 40), (110, 40), (110, 130), (20, 130)], t("square", "cuadrado")),
            ([(140, 55), (270, 55), (270, 125), (140, 125)], t("rectangle", "rectángulo")),
            ([(345, 30), (395, 85), (345, 140), (295, 85)], t("rhombus", "rombo")),
            ([(430, 125), (460, 50), (560, 50), (530, 125)], t("parallelogram", "paralelogramo")),
            ([(575, 125), (595, 55), (620, 55), (638, 125)], "")]
    for pts, nom in figs[:4]:
        s.append(poli(pts))
        cx = sum(p[0] for p in pts) / 4
        s.append(txt(cx, 165, nom, 14))
    return svg("0 0 590 180", t("Four quadrilaterals: a square, a rectangle, a rhombus that looks like a tilted square, and a parallelogram that looks like a leaning rectangle.",
                                "Cuatro cuadriláteros: un cuadrado, un rectángulo, un rombo que parece un cuadrado inclinado, y un paralelogramo que parece un rectángulo inclinado."), "".join(s), ancho=600)

def trapecio():
    s = poli([(60, 120), (110, 40), (230, 40), (300, 120)]) + txt(180, 150, t("trapezoid", "trapecio"), 15)
    return svg("0 0 360 160", t("A trapezoid: a quadrilateral with only one pair of parallel sides, the top and the bottom.", "Un trapecio: un cuadrilátero con un solo par de lados paralelos, el de arriba y el de abajo."), s, ancho=320)

def leccion():
    n = N
    s1 = f'''<p>{t("Geometry is the part of math that studies <strong>shapes</strong>. To talk about shapes clearly, we need a few words. These words appear in every geometry problem on the GED® test.",
"La geometría es la parte de las matemáticas que estudia las <strong>figuras</strong>. Para hablar de las figuras con claridad, necesitamos algunas palabras. Estas palabras aparecen en todos los problemas de geometría del examen de GED®.")}</p>
{vocabulario()}
{tabla(t("Basic geometry words", "Palabras básicas de geometría"), t("The basic words of geometry and what they mean", "Las palabras básicas de la geometría y lo que significan"),
       [t("Word", "Palabra"), t("What it means", "Qué quiere decir")],
       [[t("<strong>line segment</strong>", "<strong>segmento</strong>"), t("A straight piece of a line, with two endpoints.", "Un pedazo recto de una línea, con dos extremos.")],
        [t("<strong>side</strong>", "<strong>lado</strong>"), t("Each line segment that forms a shape.", "Cada segmento que forma una figura.")],
        [t("<strong>vertex</strong> (plural: vertices)", "<strong>vértice</strong>"), t("A corner, where two sides meet.", "Una esquina, donde se juntan dos lados.")],
        [t("<strong>parallel</strong>", "<strong>paralelas</strong>"), t("Lines that never meet and are always the same distance apart, like the rails of a train track.", "Rectas que nunca se juntan y siempre están a la misma distancia, como los rieles del tren.")],
        [t("<strong>perpendicular</strong>", "<strong>perpendiculares</strong>"), t("Lines that meet in a square corner, like the corner of a sheet of paper.", "Rectas que se juntan en una esquina cuadrada, como la esquina de una hoja de papel.")],
        [t("<strong>polygon</strong>", "<strong>polígono</strong>"), t("A closed shape made only of straight sides.", "Una figura cerrada hecha solo de lados rectos.")]])}
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>We <strong>classify</strong> shapes by their <strong>attributes</strong>: how many sides they have, whether the sides are equal, whether they are parallel, and what kind of angles they have. The name of a shape is a short way to say all that.</p>",
"<p><strong>Clasificamos</strong> las figuras por sus <strong>atributos</strong>: cuántos lados tienen, si los lados son iguales, si son paralelos y qué tipo de ángulos tienen. El nombre de una figura es una forma corta de decir todo eso.</p>"))}'''

    s2 = f'''<p>{t("An <strong>angle</strong> is the opening between two sides that meet at a vertex. We measure it in <strong>degrees</strong> (°). The key angle is the <strong>right angle</strong>: a square corner, exactly 90°. We compare every other angle with it.",
"Un <strong>ángulo</strong> es la abertura entre dos lados que se juntan en un vértice. Se mide en <strong>grados</strong> (°). El ángulo clave es el <strong>ángulo recto</strong>: una esquina cuadrada, exactamente de 90°. Todos los demás ángulos se comparan con él.")}</p>
{angulos()}
{tabla(t("Kinds of angles", "Tipos de ángulos"), t("The four kinds of angles and their measures", "Los cuatro tipos de ángulos y sus medidas"),
       [t("Angle", "Ángulo"), t("Measure", "Medida"), t("How it looks", "Cómo se ve")],
       [[t("<strong>acute</strong>", "<strong>agudo</strong>"), t("less than 90°", "menos de 90°"), t("smaller than a square corner", "más cerrado que una esquina cuadrada")],
        [t("<strong>right</strong>", "<strong>recto</strong>"), t("exactly 90°", "exactamente 90°"), t("a square corner (marked with a small square)", "una esquina cuadrada (se marca con un cuadrito)")],
        [t("<strong>obtuse</strong>", "<strong>obtuso</strong>"), t("more than 90° and less than 180°", "más de 90° y menos de 180°"), t("more open than a square corner", "más abierto que una esquina cuadrada")],
        [t("<strong>straight</strong>", "<strong>llano</strong>"), t("exactly 180°", "exactamente 180°"), t("a straight line", "una línea recta")]])}
{caja("tip", t("A trick with a sheet of paper", "Un truco con una hoja de papel"), t("<p>The corner of a sheet of paper is a right angle. Put it on an angle: if the angle fits inside the corner, it is <strong>acute</strong>; if it opens wider, it is <strong>obtuse</strong>.</p>",
"<p>La esquina de una hoja de papel es un ángulo recto. Póngala sobre un ángulo: si el ángulo cabe dentro de la esquina, es <strong>agudo</strong>; si se abre más, es <strong>obtuso</strong>.</p>"))}
{practica("p1", t("Practice 1 — Kinds of angles", "Práctica 1 — Tipos de ángulos"), t("An angle measures <strong>45°</strong>. What kind of angle is it?", "Un ángulo mide <strong>45°</strong>. ¿Qué tipo de ángulo es?"),
          [("a", t("right", "recto")), ("b", t("obtuse", "obtuso")), ("c", t("acute", "agudo")), ("d", t("straight", "llano"))])}
{enlace(n, t("angles", "angulos"), t("classify angles", "clasificar ángulos"), t("Look at an angle and its measure, and name it.", "Mire un ángulo y su medida, y nómbrelo."))}'''

    s3 = f'''<p>{t("A <strong>triangle</strong> is a polygon with 3 sides and 3 angles. We can classify it in two ways: by its <strong>sides</strong> or by its <strong>angles</strong>. Equal sides are shown with the same little marks.",
"Un <strong>triángulo</strong> es un polígono de 3 lados y 3 ángulos. Se puede clasificar de dos maneras: por sus <strong>lados</strong> o por sus <strong>ángulos</strong>. Los lados iguales se muestran con las mismas rayitas.")}</p>
{triangulos()}
{tabla(t("Kinds of triangles", "Tipos de triángulos"), t("Triangles classified by their sides and by their angles", "Los triángulos clasificados por sus lados y por sus ángulos"),
       [t("By its sides", "Por sus lados"), t("By its angles", "Por sus ángulos")],
       [[t("<strong>equilateral</strong>: 3 equal sides", "<strong>equilátero</strong>: 3 lados iguales"), t("<strong>acute</strong>: 3 acute angles", "<strong>acutángulo</strong>: 3 ángulos agudos")],
        [t("<strong>isosceles</strong>: 2 equal sides", "<strong>isósceles</strong>: 2 lados iguales"), t("<strong>right</strong>: 1 right angle", "<strong>rectángulo</strong>: 1 ángulo recto")],
        [t("<strong>scalene</strong>: no equal sides", "<strong>escaleno</strong>: ningún lado igual"), t("<strong>obtuse</strong>: 1 obtuse angle", "<strong>obtusángulo</strong>: 1 ángulo obtuso")]])}
{caja("ojo", t("Watch out! The three angles add up to 180°", "¡Cuidado! Los tres ángulos suman 180°"), t("<p>In every triangle, the three angles add up to <strong>180°</strong>. That is why a triangle can have only one right angle or one obtuse angle: two of them would already add up to 180° or more.</p>",
"<p>En todo triángulo, los tres ángulos suman <strong>180°</strong>. Por eso un triángulo solo puede tener un ángulo recto o un ángulo obtuso: dos de ellos ya sumarían 180° o más.</p>"))}
{practica("p2", t("Practice 2 — Triangles by their sides", "Práctica 2 — Triángulos por sus lados"), t("A triangle has two sides of <strong>8 inches</strong> and one side of <strong>5 inches</strong>. By its sides, it is:", "Un triángulo tiene dos lados de <strong>8 pulgadas</strong> y un lado de <strong>5 pulgadas</strong>. Por sus lados, es:"),
          [("a", t("equilateral", "equilátero")), ("b", t("isosceles", "isósceles")), ("c", t("scalene", "escaleno")), ("d", t("right", "rectángulo"))])}
{enlace(n, t("triangles", "triangulos"), t("classify triangles", "clasificar triángulos"), t("Classify triangles by their sides and by their angles.", "Clasifique triángulos por sus lados y por sus ángulos."))}'''

    s4 = f'''<p>{t("Polygons are named by their number of sides:", "Los polígonos se nombran por su cantidad de lados:")}</p>
{tabla(t("Names of polygons", "Nombres de los polígonos"), t("Polygons and their number of sides", "Los polígonos y su cantidad de lados"),
       [t("Sides", "Lados"), t("Name", "Nombre"), t("An example", "Un ejemplo")],
       [["3", t("triangle", "triángulo"), t("a yield sign", "una señal de ceda el paso")], ["4", t("quadrilateral", "cuadrilátero"), t("a window", "una ventana")],
        ["5", t("pentagon", "pentágono"), t("the Pentagon building", "el edificio del Pentágono")], ["6", t("hexagon", "hexágono"), t("a cell in a honeycomb", "una celda de un panal")],
        ["8", t("octagon", "octágono"), t("a stop sign", "una señal de alto")]])}
<p>{t("<strong>Quadrilaterals</strong> (4 sides) have their own names, depending on their sides and angles:", "Los <strong>cuadriláteros</strong> (4 lados) tienen sus propios nombres, según sus lados y sus ángulos:")}</p>
{cuadrilateros()}
{tabla(t("Kinds of quadrilaterals", "Tipos de cuadriláteros"), t("The kinds of quadrilaterals and their attributes", "Los tipos de cuadriláteros y sus atributos"),
       [t("Name", "Nombre"), t("Attributes", "Atributos")],
       [[t("<strong>parallelogram</strong>", "<strong>paralelogramo</strong>"), t("2 pairs of parallel sides", "2 pares de lados paralelos")],
        [t("<strong>rectangle</strong>", "<strong>rectángulo</strong>"), t("a parallelogram with 4 right angles", "un paralelogramo con 4 ángulos rectos")],
        [t("<strong>rhombus</strong>", "<strong>rombo</strong>"), t("a parallelogram with 4 equal sides", "un paralelogramo con 4 lados iguales")],
        [t("<strong>square</strong>", "<strong>cuadrado</strong>"), t("4 equal sides and 4 right angles", "4 lados iguales y 4 ángulos rectos")],
        [t("<strong>trapezoid</strong>", "<strong>trapecio</strong>"), t("only 1 pair of parallel sides", "un solo par de lados paralelos")]])}
{trapecio()}
{caja("tip", t("A family of shapes", "Una familia de figuras"), t("<p>A <strong>square</strong> has all the attributes of a rectangle (4 right angles) and all the attributes of a rhombus (4 equal sides). So every square is also a rectangle and a rhombus. But not every rectangle is a square.</p>",
"<p>Un <strong>cuadrado</strong> tiene todos los atributos de un rectángulo (4 ángulos rectos) y todos los de un rombo (4 lados iguales). Así que todo cuadrado es también un rectángulo y un rombo. Pero no todo rectángulo es un cuadrado.</p>"))}
{practica("p3", t("Practice 3 — Names of polygons", "Práctica 3 — Nombres de polígonos"), t("How many sides does an <strong>octagon</strong> have?", "¿Cuántos lados tiene un <strong>octágono</strong>?"),
          [("a", "8"), ("b", "6"), ("c", "10"), ("d", "5")])}
{practica("p4", t("Practice 4 — Quadrilaterals", "Práctica 4 — Cuadriláteros"), t("Which quadrilateral has <strong>only one pair</strong> of parallel sides?", "¿Qué cuadrilátero tiene <strong>un solo par</strong> de lados paralelos?"),
          [("a", t("square", "cuadrado")), ("b", t("rectangle", "rectángulo")), ("c", t("parallelogram", "paralelogramo")), ("d", t("trapezoid", "trapecio"))])}
{enlace(n, t("polygons", "poligonos"), t("name polygons", "nombrar polígonos"), t("Count the sides and name the polygon.", "Cuente los lados y nombre el polígono."))}
{enlace(n, t("quadrilaterals", "cuadrilateros"), t("quadrilaterals", "cuadriláteros"), t("Read the attributes and choose the best name.", "Lea los atributos y elija el mejor nombre."))}'''

    secciones = [("s-" + t("words", "palabras"), t("The words of geometry", "Las palabras de la geometría"), s1),
                 ("s-" + t("angles", "angulos"), t("Angles", "Los ángulos"), s2),
                 ("s-" + t("triangles", "triangulos"), t("Triangles", "Los triángulos"), s3),
                 ("s-" + t("polygons", "poligonos"), t("Polygons and quadrilaterals", "Polígonos y cuadriláteros"), s4)]

    lesson = {"next": t("Lesson 7.2", "Lección 7.2"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("A right angle is exactly 90°. 45° is smaller.", "Un ángulo recto mide exactamente 90°. 45° es menos."), "b": t("An obtuse angle is more than 90°. 45° is less.", "Un ángulo obtuso mide más de 90°. 45° es menos."), "d": t("A straight angle is 180°, a straight line.", "Un ángulo llano mide 180°, una línea recta.")},
             "right": t("45° is less than 90°: an acute angle.", "45° es menos de 90°: un ángulo agudo."), "solution": t("An angle of less than 90° is acute. 45° is half of a right angle.", "Un ángulo de menos de 90° es agudo. 45° es la mitad de un ángulo recto.")},
      "p2": {"ok": "b", "hints": {"a": t("Equilateral needs 3 equal sides. Here only 2 are equal.", "Equilátero necesita 3 lados iguales. Aquí solo 2 son iguales."), "c": t("Scalene means no equal sides. Here 2 sides are equal.", "Escaleno quiere decir ningún lado igual. Aquí 2 lados son iguales."), "d": t("Right is a name by angles, not by sides. The question asks about the sides.", "Rectángulo es un nombre por los ángulos, no por los lados. La pregunta es sobre los lados.")},
             "right": t("2 equal sides: isosceles.", "2 lados iguales: isósceles."), "solution": t("Two sides of 8 inches are equal, and the third is different. A triangle with exactly 2 equal sides is isosceles.", "Los dos lados de 8 pulgadas son iguales, y el tercero es distinto. Un triángulo con 2 lados iguales es isósceles.")},
      "p3": {"ok": "a", "hints": {"b": t("6 sides is a hexagon.", "6 lados es un hexágono."), "c": t("10 sides is a decagon.", "10 lados es un decágono."), "d": t("5 sides is a pentagon.", "5 lados es un pentágono.")},
             "right": t("Octo- means 8, like an octopus with 8 arms.", "Octo- quiere decir 8: un octágono tiene 8 lados, como una señal de alto."), "solution": t("An octagon has 8 sides, like a stop sign.", "Un octágono tiene 8 lados, como una señal de alto.")},
      "p4": {"ok": "d", "hints": {"a": t("A square has 2 pairs of parallel sides.", "Un cuadrado tiene 2 pares de lados paralelos."), "b": t("A rectangle has 2 pairs of parallel sides.", "Un rectángulo tiene 2 pares de lados paralelos."), "c": t("Parallelo- tells you: it has 2 pairs of parallel sides.", "Paralelo- se lo dice: tiene 2 pares de lados paralelos.")},
             "right": t("A trapezoid has only one pair of parallel sides.", "Un trapecio tiene un solo par de lados paralelos."), "solution": t("Squares, rectangles, and parallelograms have 2 pairs of parallel sides. A trapezoid has only 1 pair.", "Los cuadrados, los rectángulos y los paralelogramos tienen 2 pares de lados paralelos. El trapecio tiene solo 1 par.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Acute is less than 90°.", "Agudo es menos de 90°."), "c": t("Obtuse is more than 90°.", "Obtuso es más de 90°."), "d": t("Straight is 180°.", "Llano es 180°.")}, "solution": t("An angle of exactly 90° is a right angle: a square corner.", "Un ángulo de exactamente 90° es un ángulo recto: una esquina cuadrada.")},
      "B": {"ok": "d", "hints": {"a": t("Acute is less than 90°. 135° is more.", "Agudo es menos de 90°. 135° es más."), "b": t("Right is exactly 90°.", "Recto es exactamente 90°."), "c": t("Straight is exactly 180°. 135° is less.", "Llano es exactamente 180°. 135° es menos.")}, "solution": t("135° is more than 90° and less than 180°: obtuse.", "135° es más de 90° y menos de 180°: obtuso.")},
      "C": {"ok": "a", "hints": {"b": t("Isosceles has exactly 2 equal sides. Here all 3 are equal.", "Isósceles tiene 2 lados iguales. Aquí los 3 son iguales."), "c": t("Scalene has no equal sides.", "Escaleno no tiene lados iguales."), "d": t("Right is a name by angles. The question gives the sides.", "Rectángulo es un nombre por los ángulos. La pregunta da los lados.")}, "solution": t("3 equal sides: equilateral.", "3 lados iguales: equilátero.")},
      "D": {"ok": "c", "hints": {"a": t("Equilateral needs 3 equal sides.", "Equilátero necesita 3 lados iguales."), "b": t("Isosceles needs 2 equal sides. 5, 7, and 9 are all different.", "Isósceles necesita 2 lados iguales. 5, 7 y 9 son todos distintos."), "d": t("Obtuse is a name by angles. The question gives the sides.", "Obtusángulo es un nombre por los ángulos. La pregunta da los lados.")}, "solution": t("5, 7, and 9 are all different: scalene.", "5, 7 y 9 son todos distintos: escaleno.")},
      "E": {"ok": "b", "hints": {"a": t("A pentagon has 5 sides.", "Un pentágono tiene 5 lados."), "c": t("An octagon has 8 sides.", "Un octágono tiene 8 lados."), "d": t("A quadrilateral has 4 sides.", "Un cuadrilátero tiene 4 lados.")}, "solution": t("6 sides: hexagon, like a cell in a honeycomb.", "6 lados: hexágono, como una celda de un panal.")},
      "F": {"ok": "c", "hints": {"a": t("Perpendicular lines meet in a square corner.", "Las rectas perpendiculares se juntan en una esquina cuadrada."), "b": t("Intersecting lines cross each other.", "Las rectas que se cortan se cruzan."), "d": t("A diagonal joins two corners that are not next to each other.", "Una diagonal une dos esquinas que no están una al lado de la otra.")}, "solution": t("Lines that never meet and stay the same distance apart are parallel, like train rails.", "Las rectas que nunca se juntan y siempre están a la misma distancia son paralelas, como los rieles del tren.")},
      "G": {"ok": "d", "hints": {"a": t("A trapezoid has only one pair of parallel sides.", "Un trapecio tiene un solo par de lados paralelos."), "b": t("A rhombus has 4 equal sides, but its angles do not have to be right angles.", "Un rombo tiene 4 lados iguales, pero sus ángulos no tienen que ser rectos."), "c": t("A rectangle has 4 right angles, but its sides do not have to be equal.", "Un rectángulo tiene 4 ángulos rectos, pero sus lados no tienen que ser iguales.")}, "solution": t("4 equal sides and 4 right angles: a square. It is the most exact name.", "4 lados iguales y 4 ángulos rectos: un cuadrado. Es el nombre más exacto.")},
      "H": {"ok": "a", "hints": {"b": t("A rectangle can be long and narrow, with sides that are not equal.", "Un rectángulo puede ser largo y angosto, con lados que no son iguales."), "c": t("A trapezoid has only one pair of parallel sides.", "Un trapecio tiene un solo par de lados paralelos."), "d": t("Two right angles already add up to 180°, and the three angles of a triangle add up to 180°.", "Dos ángulos rectos ya suman 180°, y los tres ángulos de un triángulo suman 180°.")}, "solution": t("A square has 4 right angles, so it has everything a rectangle needs. Every square is a rectangle.", "Un cuadrado tiene 4 ángulos rectos, así que tiene todo lo que necesita un rectángulo. Todo cuadrado es un rectángulo.")}
     }}

    quiz = [
     ("A", t("An angle that measures <strong>90°</strong> is called:", "Un ángulo que mide <strong>90°</strong> se llama:"), [("a", t("acute", "agudo")), ("b", t("right", "recto")), ("c", t("obtuse", "obtuso")), ("d", t("straight", "llano"))]),
     ("B", t("An angle that measures <strong>135°</strong> is:", "Un ángulo que mide <strong>135°</strong> es:"), [("a", t("acute", "agudo")), ("b", t("right", "recto")), ("c", t("straight", "llano")), ("d", t("obtuse", "obtuso"))]),
     ("C", t("A triangle has sides of <strong>6 cm, 6 cm, and 6 cm</strong>. By its sides, it is:", "Un triángulo tiene lados de <strong>6 cm, 6 cm y 6 cm</strong>. Por sus lados, es:"), [("a", t("equilateral", "equilátero")), ("b", t("isosceles", "isósceles")), ("c", t("scalene", "escaleno")), ("d", t("right", "rectángulo"))]),
     ("D", t("A triangle has sides of <strong>5 in, 7 in, and 9 in</strong>. By its sides, it is:", "Un triángulo tiene lados de <strong>5, 7 y 9 pulgadas</strong>. Por sus lados, es:"), [("a", t("equilateral", "equilátero")), ("b", t("isosceles", "isósceles")), ("c", t("scalene", "escaleno")), ("d", t("obtuse", "obtusángulo"))]),
     ("E", t("A polygon with <strong>6 sides</strong> is a:", "Un polígono de <strong>6 lados</strong> es un:"), [("a", t("pentagon", "pentágono")), ("b", t("hexagon", "hexágono")), ("c", t("octagon", "octágono")), ("d", t("quadrilateral", "cuadrilátero"))]),
     ("F", t("Lines that never meet and are always the same distance apart are:", "Las rectas que nunca se juntan y siempre están a la misma distancia son:"), [("a", t("perpendicular", "perpendiculares")), ("b", t("intersecting", "secantes (se cortan)")), ("c", t("parallel", "paralelas")), ("d", t("diagonal", "diagonales"))]),
     ("G", t("What is the best name for a quadrilateral with <strong>4 equal sides and 4 right angles</strong>?", "¿Cuál es el mejor nombre para un cuadrilátero con <strong>4 lados iguales y 4 ángulos rectos</strong>?"), [("a", t("trapezoid", "trapecio")), ("b", t("rhombus", "rombo")), ("c", t("rectangle", "rectángulo")), ("d", t("square", "cuadrado"))]),
     ("H", t("Which statement is true?", "¿Qué afirmación es verdadera?"), [("a", t("Every square is a rectangle.", "Todo cuadrado es un rectángulo.")), ("b", t("Every rectangle is a square.", "Todo rectángulo es un cuadrado.")), ("c", t("A trapezoid has two pairs of parallel sides.", "Un trapecio tiene dos pares de lados paralelos.")), ("d", t("A triangle can have two right angles.", "Un triángulo puede tener dos ángulos rectos."))])]

    return B.pagina_leccion(n, 7, t("Geometry", "Geometría"),
        t("Classifying 2D shapes: attributes and vocabulary", "Clasificación de figuras 2D: atributos y vocabulario"),
        t("Sides, angles, and parallel lines: learn the words of geometry and name every shape by its attributes.", "Lados, ángulos y rectas paralelas: aprenda las palabras de la geometría y nombre cada figura por sus atributos."),
        ("📐", t("The right angle as a guide", "El ángulo recto como guía")),
        [t("<strong>Use</strong> the basic words of geometry: side, vertex, parallel, perpendicular.", "<strong>Usar</strong> las palabras básicas de la geometría: lado, vértice, paralelas, perpendiculares."),
         t("<strong>Classify</strong> angles as acute, right, obtuse, or straight.", "<strong>Clasificar</strong> ángulos en agudos, rectos, obtusos o llanos."),
         t("<strong>Classify</strong> triangles by their sides and by their angles.", "<strong>Clasificar</strong> triángulos por sus lados y por sus ángulos."),
         t("<strong>Name</strong> polygons and quadrilaterals by their attributes.", "<strong>Nombrar</strong> polígonos y cuadriláteros por sus atributos.")],
        secciones,
        (t("Draw one example of each: an acute, a right, and an obtuse angle; an equilateral, an isosceles, and a scalene triangle; a square, a rectangle, a rhombus, and a trapezoid. Mark equal sides and right angles.",
           "Dibuje un ejemplo de cada uno: un ángulo agudo, uno recto y uno obtuso; un triángulo equilátero, uno isósceles y uno escaleno; un cuadrado, un rectángulo, un rombo y un trapecio. Marque los lados iguales y los ángulos rectos."),
         t("Go for a walk or look around your home and find 10 shapes: windows, signs, tiles, roofs. Write the name of each shape and one of its attributes.",
           "Salga a caminar o mire su casa y encuentre 10 figuras: ventanas, señales, losetas, techos. Escriba el nombre de cada figura y uno de sus atributos.")),
        quiz,
        t("Self-check checklist for classifying shapes", "Lista de autoevaluación de clasificación de figuras"),
        t("Self-check checklist: skills for classifying shapes", "Lista de autoevaluación: destrezas para clasificar figuras"),
        [(t("The words of geometry", "Las palabras de la geometría"), t("I use side, vertex, parallel, and perpendicular correctly.", "Uso bien lado, vértice, paralelas y perpendiculares."), t("I know most of the words.", "Me sé la mayoría de las palabras."), t("I mix up parallel and perpendicular.", "Confundo paralelas y perpendiculares.")),
         (t("Kinds of angles", "Tipos de ángulos"), t("I classify any angle by comparing it with 90°.", "Clasifico cualquier ángulo comparándolo con 90°."), t("I recognize right angles, but I mix up acute and obtuse.", "Reconozco los ángulos rectos, pero confundo agudos y obtusos."), t("I do not know how to classify angles yet.", "Todavía no sé clasificar ángulos.")),
         (t("Kinds of triangles", "Tipos de triángulos"), t("I classify triangles by their sides and by their angles.", "Clasifico triángulos por sus lados y por sus ángulos."), t("I classify them by their sides only.", "Los clasifico solo por sus lados."), t("I mix up the names.", "Confundo los nombres.")),
         (t("Polygons and quadrilaterals", "Polígonos y cuadriláteros"), t("I name polygons and quadrilaterals and explain why a square is also a rectangle.", "Nombro polígonos y cuadriláteros y explico por qué un cuadrado también es un rectángulo."), t("I name the common shapes.", "Nombro las figuras comunes."), t("I only know the square and the triangle.", "Solo conozco el cuadrado y el triángulo."))],
        t("<p>You can now name shapes by their attributes: their sides, their angles, and their parallel lines.</p>\n<p>In <strong>Lesson 7.2 · Perimeter of polygons</strong> you will measure the distance around a shape, using what you learned about sides and units.</p>",
          "<p>Ya sabe nombrar las figuras por sus atributos: sus lados, sus ángulos y sus rectas paralelas.</p>\n<p>En la <strong>Lección 7.2 · Perímetro de polígonos</strong> medirá la distancia alrededor de una figura, usando lo que aprendió de los lados y de las unidades.</p>"),
        ("7-2", ("", t("Lesson 7.2 · Perimeter of polygons", "Lección 7.2 · Perímetro de polígonos"))),
        [(t("vertex", "vértice"), t("A corner of a shape, where two sides meet.", "Una esquina de una figura, donde se juntan dos lados.")),
         (t("angle", "ángulo"), t("The opening between two sides that meet at a vertex, measured in degrees (°).", "La abertura entre dos lados que se juntan en un vértice; se mide en grados (°).")),
         (t("right angle", "ángulo recto"), t("An angle of exactly 90°, a square corner.", "Un ángulo de exactamente 90°, una esquina cuadrada.")),
         (t("parallel", "paralelas"), t("Lines that never meet and are always the same distance apart.", "Rectas que nunca se juntan y siempre están a la misma distancia.")),
         (t("perpendicular", "perpendiculares"), t("Lines that meet in a right angle.", "Rectas que se juntan formando un ángulo recto.")),
         (t("polygon", "polígono"), t("A closed shape made only of straight sides.", "Una figura cerrada hecha solo de lados rectos.")),
         (t("quadrilateral", "cuadrilátero"), t("A polygon with 4 sides.", "Un polígono de 4 lados."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "ang": {"ag": "acute", "re": "right", "ob": "obtuse", "ll": "straight"},
  "pregAng": "This angle measures <strong>{g}°</strong>. What kind of angle is it?",
  "ariaAng": "An angle that measures {g} degrees.",
  "porAng": {"ag": "less than 90°", "re": "exactly 90°", "ob": "more than 90° and less than 180°", "ll": "exactly 180°"},
  "bienAng": "{g}° is {por}: <strong>{nom}</strong>.",
  "angA": {"ag": "an acute angle", "re": "a right angle", "ob": "an obtuse angle", "ll": "a straight angle"},
  "pistaAng": "Compare the angle with 90°, a square corner.",
  "lados": {"eqi": "equilateral", "iso": "isosceles", "esc": "scalene"},
  "angT": {"ac": "acute", "rt": "right", "ob": "obtuse"},
  "pregLados": "A triangle has sides of <strong>{a}, {b}, and {c} {u}</strong>. By its sides, it is:",
  "pregAngT": "A triangle has angles of <strong>{a}°, {b}°, and {c}°</strong>. By its angles, it is:",
  "u": "inches",
  "ariaTri": "A triangle with sides of {a}, {b}, and {c} {u}.",
  "ariaTriA": "A triangle with angles of {a}, {b}, and {c} degrees.",
  "bienLados": {"eqi": "All 3 sides are equal: <strong>equilateral</strong>.", "iso": "Exactly 2 sides are equal: <strong>isosceles</strong>.", "esc": "No two sides are equal: <strong>scalene</strong>."},
  "bienAngT": {"ac": "All 3 angles are less than 90°: <strong>acute</strong>.", "rt": "One angle is exactly 90°: <strong>right</strong>.", "ob": "One angle is more than 90°: <strong>obtuse</strong>."},
  "pistaLados": "Count how many sides are equal.",
  "pistaAngT": "Look for an angle of 90° or more.",
  "poli": {"3": "triangle", "4": "quadrilateral", "5": "pentagon", "6": "hexagon", "7": "heptagon", "8": "octagon"},
  "pregPoli": "What is the name of this polygon?",
  "ariaPoli": "A polygon with {n} straight sides.",
  "bienPoli": "It has {n} sides. Its name is <strong>{nom}</strong>.",
  "pistaPoli": "Count the sides one by one. Put your finger on a corner and go around.",
  "cuad": {"sq": "square", "rect": "rectangle", "rh": "rhombus", "par": "parallelogram", "tr": "trapezoid"},
  "desc": {"sq": "4 equal sides and 4 right angles", "rect": "4 right angles, and its sides are not all equal", "rh": "4 equal sides, and its angles are not right angles", "par": "2 pairs of parallel sides, no right angles, and its sides are not all equal", "tr": "only 1 pair of parallel sides"},
  "pregCuad": "A quadrilateral has <strong>{d}</strong>. What is its best name?",
  "bienCuad": "A quadrilateral with {d} is a <strong>{nom}</strong>.",
  "pistaCuad": {"sq": "A square needs 4 equal sides and 4 right angles.", "rect": "A rectangle needs 4 right angles.", "rh": "A rhombus needs 4 equal sides.", "par": "A parallelogram needs 2 pairs of parallel sides.", "tr": "A trapezoid has only 1 pair of parallel sides."}
 },
 "es": {
  "ang": {"ag": "agudo", "re": "recto", "ob": "obtuso", "ll": "llano"},
  "pregAng": "Este ángulo mide <strong>{g}°</strong>. ¿Qué tipo de ángulo es?",
  "ariaAng": "Un ángulo que mide {g} grados.",
  "porAng": {"ag": "menos de 90°", "re": "exactamente 90°", "ob": "más de 90° y menos de 180°", "ll": "exactamente 180°"},
  "bienAng": "{g}° es {por}: <strong>{nom}</strong>.",
  "angA": {"ag": "un ángulo agudo", "re": "un ángulo recto", "ob": "un ángulo obtuso", "ll": "un ángulo llano"},
  "pistaAng": "Compare el ángulo con 90°, una esquina cuadrada.",
  "lados": {"eqi": "equilátero", "iso": "isósceles", "esc": "escaleno"},
  "angT": {"ac": "acutángulo", "rt": "rectángulo", "ob": "obtusángulo"},
  "pregLados": "Un triángulo tiene lados de <strong>{a}, {b} y {c} {u}</strong>. Por sus lados, es:",
  "pregAngT": "Un triángulo tiene ángulos de <strong>{a}°, {b}° y {c}°</strong>. Por sus ángulos, es:",
  "u": "pulgadas",
  "ariaTri": "Un triángulo con lados de {a}, {b} y {c} {u}.",
  "ariaTriA": "Un triángulo con ángulos de {a}, {b} y {c} grados.",
  "bienLados": {"eqi": "Los 3 lados son iguales: <strong>equilátero</strong>.", "iso": "Exactamente 2 lados son iguales: <strong>isósceles</strong>.", "esc": "No hay dos lados iguales: <strong>escaleno</strong>."},
  "bienAngT": {"ac": "Los 3 ángulos miden menos de 90°: <strong>acutángulo</strong>.", "rt": "Un ángulo mide exactamente 90°: <strong>rectángulo</strong>.", "ob": "Un ángulo mide más de 90°: <strong>obtusángulo</strong>."},
  "pistaLados": "Cuente cuántos lados son iguales.",
  "pistaAngT": "Busque un ángulo de 90° o más.",
  "poli": {"3": "triángulo", "4": "cuadrilátero", "5": "pentágono", "6": "hexágono", "7": "heptágono", "8": "octágono"},
  "pregPoli": "¿Cómo se llama este polígono?",
  "ariaPoli": "Un polígono de {n} lados rectos.",
  "bienPoli": "Tiene {n} lados. Se llama <strong>{nom}</strong>.",
  "pistaPoli": "Cuente los lados uno por uno. Ponga el dedo en una esquina y dé la vuelta.",
  "cuad": {"sq": "cuadrado", "rect": "rectángulo", "rh": "rombo", "par": "paralelogramo", "tr": "trapecio"},
  "desc": {"sq": "4 lados iguales y 4 ángulos rectos", "rect": "4 ángulos rectos, y sus lados no son todos iguales", "rh": "4 lados iguales, y sus ángulos no son rectos", "par": "2 pares de lados paralelos, ningún ángulo recto, y sus lados no son todos iguales", "tr": "un solo par de lados paralelos"},
  "pregCuad": "Un cuadrilátero tiene <strong>{d}</strong>. ¿Cuál es su mejor nombre?",
  "bienCuad": "Un cuadrilátero con {d} es un <strong>{nom}</strong>.",
  "pistaCuad": {"sq": "Un cuadrado necesita 4 lados iguales y 4 ángulos rectos.", "rect": "Un rectángulo necesita 4 ángulos rectos.", "rh": "Un rombo necesita 4 lados iguales.", "par": "Un paralelogramo necesita 2 pares de lados paralelos.", "tr": "Un trapecio tiene un solo par de lados paralelos."}
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function fig(vb, aria, cuerpo){ return '<svg class="figura" viewBox="' + vb + '" role="img" aria-label="' + aria + '">' + cuerpo + '</svg>'; }

/* ============ MODULE 1 · angles ============ */
function genAng(){
  var tipo = elige(["ag", "ag", "re", "ob", "ob", "ll"]), g = tipo === "re" ? 90 : (tipo === "ll" ? 180 : (tipo === "ag" ? aleatorio(3, 17) * 5 : aleatorio(19, 34) * 5));
  var rot = aleatorio(0, 40), cx = 150, cy = 150, L = 110, a1 = rot * Math.PI / 180, a2 = (rot + g) * Math.PI / 180;
  var p1 = [cx + L * Math.cos(a1), cy - L * Math.sin(a1)], p2 = [cx + L * Math.cos(a2), cy - L * Math.sin(a2)], s = "";
  s += linea([cx, cy], p1, "#37474f", 5) + linea([cx, cy], p2, "#37474f", 5);
  if (g === 90){ var u = 22, q1 = [cx + u * Math.cos(a1), cy - u * Math.sin(a1)], q2 = [cx + u * Math.cos(a2), cy - u * Math.sin(a2)], q3 = [q1[0] + q2[0] - cx, q1[1] + q2[1] - cy];
    s += '<polyline points="' + f1(q1[0]) + ',' + f1(q1[1]) + ' ' + f1(q3[0]) + ',' + f1(q3[1]) + ' ' + f1(q2[0]) + ',' + f1(q2[1]) + '" fill="none" stroke="#1565c0" stroke-width="3"/>'; }
  else { var r = 34; s += '<path d="M' + f1(cx + r * Math.cos(a1)) + ',' + f1(cy - r * Math.sin(a1)) + ' A' + r + ',' + r + ' 0 0 0 ' + f1(cx + r * Math.cos(a2)) + ',' + f1(cy - r * Math.sin(a2)) + '" fill="none" stroke="#1565c0" stroke-width="3"/>'; }
  s += '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#37474f"/>';
  var ops = ["ag", "re", "ob", "ll"], pistas = {};
  ops.forEach(function(k){ if (k !== tipo) pistas[k] = TXT.pistaAng; });
  var txt = F(TXT.bienAng, { g: g, por: TXT.porAng[tipo], nom: TXT.angA[tipo] });
  var xs = [cx, p1[0], p2[0]], ys = [cy, p1[1], p2[1]], x0 = Math.min.apply(null, xs) - 20, y0 = Math.min.apply(null, ys) - 20, w = Math.max.apply(null, xs) + 20 - x0, hh = Math.max.apply(null, ys) + 20 - y0;
  if (hh < 90){ y0 -= (90 - hh) / 2; hh = 90; }
  return { enOrden: true, enun: F(TXT.pregAng, { g: g }) + fig(f1(x0) + " " + f1(y0) + " " + f1(w) + " " + f1(hh), F(TXT.ariaAng, { g: g }), s),
    opciones: ops.map(function(k){ return { html: TXT.ang[k], clave: k }; }), correcta: tipo, pistas: pistas, pista: TXT.pistaAng, bien: txt, mal: txt };
}

/* ============ MODULE 2 · triangles ============ */
function dibujaTri(a, b, c){
  /* sides a = BC, b = CA, c = AB; A at the origin, B on the x axis */
  var x = (b * b + c * c - a * a) / (2 * c), y = Math.sqrt(Math.max(0, b * b - x * x));
  var xs = [0, c, x], ys = [0, 0, y], mnx = Math.min.apply(null, xs), mxx = Math.max.apply(null, xs), k = Math.min(240 / (mxx - mnx), 150 / Math.max(y, 1));
  var P = xs.map(function(xx, i){ return [30 + (xx - mnx) * k, 180 - ys[i] * k]; });
  return '<polygon points="' + P.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#e3f2fd" stroke="#37474f" stroke-width="3"/>';
}
function genTri(){
  var pistas = {}, s;
  if (Math.random() < 0.5){
    var tipo = elige(["eqi", "iso", "iso", "esc"]), a, b, c;
    if (tipo === "eqi"){ a = b = c = aleatorio(3, 12); }
    else if (tipo === "iso"){ a = b = aleatorio(5, 12); c = aleatorio(3, 2 * a - 2); if (c === a) c = a - 2; }
    else { do { a = aleatorio(4, 12); b = aleatorio(4, 12); c = aleatorio(4, 12); } while (a === b || b === c || a === c || a + b <= c || a + c <= b || b + c <= a); }
    var L = baraja([a, b, c]);
    ["eqi", "iso", "esc"].forEach(function(k){ if (k !== tipo) pistas[k] = TXT.pistaLados; });
    s = fig("0 0 300 200", F(TXT.ariaTri, { a: L[0], b: L[1], c: L[2], u: TXT.u }), dibujaTri(L[0], L[1], L[2]));
    return { enOrden: true, enun: F(TXT.pregLados, { a: L[0], b: L[1], c: L[2], u: TXT.u }) + s, opciones: ["eqi", "iso", "esc"].map(function(k){ return { html: TXT.lados[k], clave: k }; }),
      correcta: tipo, pistas: pistas, pista: TXT.pistaLados, bien: TXT.bienLados[tipo], mal: TXT.bienLados[tipo] };
  }
  var t2 = elige(["ac", "rt", "ob"]), A, Bb, C;
  if (t2 === "rt"){ A = 90; Bb = aleatorio(4, 14) * 5; }
  else if (t2 === "ob"){ A = aleatorio(19, 28) * 5; Bb = aleatorio(3, (175 - A) / 5 - 2) * 5; }
  else { do { A = aleatorio(10, 17) * 5; Bb = aleatorio(9, 17) * 5; } while (180 - A - Bb >= 90 || 180 - A - Bb <= 0); }
  C = 180 - A - Bb;
  var G = baraja([A, Bb, C]);
  ["ac", "rt", "ob"].forEach(function(k){ if (k !== t2) pistas[k] = TXT.pistaAngT; });
  return { enOrden: true, enun: F(TXT.pregAngT, { a: G[0], b: G[1], c: G[2] }), opciones: ["ac", "rt", "ob"].map(function(k){ return { html: TXT.angT[k], clave: k }; }),
    correcta: t2, pistas: pistas, pista: TXT.pistaAngT, bien: TXT.bienAngT[t2], mal: TXT.bienAngT[t2] };
}

/* ============ MODULE 3 · polygons ============ */
function genPoli(){
  var n = aleatorio(3, 8), cx = 150, cy = 110, R = 85, rot = Math.random() * Math.PI, P = [];
  for (var i = 0; i < n; i++){ var a = rot + 2 * Math.PI * i / n, r = R * (0.8 + Math.random() * 0.25); P.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]); }
  var s = '<polygon points="' + P.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#e3f2fd" stroke="#37474f" stroke-width="3"/>';
  P.forEach(function(p){ s += '<circle cx="' + f1(p[0]) + '" cy="' + f1(p[1]) + '" r="4" fill="#37474f"/>'; });
  var keys = ["3", "4", "5", "6", "7", "8"], pistas = {}, op = baraja(keys.filter(function(k){ return k !== String(n); })).slice(0, 3).concat([String(n)]);
  op.sort(); op.forEach(function(k){ if (k !== String(n)) pistas[k] = TXT.pistaPoli; });
  var txt = F(TXT.bienPoli, { n: n, nom: TXT.poli[String(n)] });
  return { enOrden: true, enun: TXT.pregPoli + fig("40 10 220 200", F(TXT.ariaPoli, { n: n }), s), opciones: op.map(function(k){ return { html: TXT.poli[k], clave: k }; }),
    correcta: String(n), pistas: pistas, pista: TXT.pistaPoli, bien: txt, mal: txt };
}

/* ============ MODULE 4 · quadrilaterals ============ */
function genCuad(){
  var ks = ["sq", "rect", "rh", "par", "tr"], k = elige(ks), pistas = {};
  ks.forEach(function(x){ if (x !== k) pistas[x] = TXT.pistaCuad[x]; });
  var txt = F(TXT.bienCuad, { d: TXT.desc[k], nom: TXT.cuad[k] });
  return { enOrden: true, enun: F(TXT.pregCuad, { d: TXT.desc[k] }), opciones: ks.map(function(x){ return { html: TXT.cuad[x], clave: x }; }),
    correcta: k, pistas: pistas, pista: TXT.pistaCuad[k], bien: txt, mal: txt };
}

creaPracticaOM("p1", genAng);
creaPracticaOM("p2", genTri);
creaPracticaOM("p3", genPoli);
creaPracticaOM("p4", genCuad);
'''

def practica_pagina():
    n = N
    mods = [
     (t("angles", "angulos"), t("Classify angles", "Clasificar ángulos"),
      f'''      <table class="reglas">
        <caption>{t("Kinds of angles", "Tipos de ángulos")}</caption>
        <tbody>
          <tr><td>{t("acute", "agudo")}</td><td>{t("less than 90°", "menos de 90°")}</td></tr>
          <tr><td>{t("right", "recto")}</td><td>{t("exactly 90° (a square corner)", "exactamente 90° (una esquina cuadrada)")}</td></tr>
          <tr><td>{t("obtuse", "obtuso")}</td><td>{t("more than 90° and less than 180°", "más de 90° y menos de 180°")}</td></tr>
          <tr><td>{t("straight", "llano")}</td><td>{t("exactly 180° (a straight line)", "exactamente 180° (una línea recta)")}</td></tr>
        </tbody>
      </table>
{B.om("p1", t("Practice: what kind of angle?", "Practique: ¿qué tipo de ángulo?"))}'''),
     (t("triangles", "triangulos"), t("Classify triangles", "Clasificar triángulos"),
      f'''      <p>{t("<strong>By its sides:</strong> equilateral (3 equal), isosceles (2 equal), scalene (none equal). <strong>By its angles:</strong> acute (all less than 90°), right (one of 90°), obtuse (one of more than 90°).", "<strong>Por sus lados:</strong> equilátero (3 iguales), isósceles (2 iguales), escaleno (ninguno igual). <strong>Por sus ángulos:</strong> acutángulo (todos de menos de 90°), rectángulo (uno de 90°), obtusángulo (uno de más de 90°).")}</p>
{B.om("p2", t("Practice: what kind of triangle?", "Practique: ¿qué tipo de triángulo?"))}'''),
     (t("polygons", "poligonos"), t("Name polygons", "Nombrar polígonos"),
      f'''      <p>{t("3 sides: triangle · 4: quadrilateral · 5: pentagon · 6: hexagon · 7: heptagon · 8: octagon.", "3 lados: triángulo · 4: cuadrilátero · 5: pentágono · 6: hexágono · 7: heptágono · 8: octágono.")}</p>
{B.om("p3", t("Practice: count the sides", "Practique: cuente los lados"))}'''),
     (t("quadrilaterals", "cuadrilateros"), t("Quadrilaterals", "Cuadriláteros"),
      f'''      <table class="reglas">
        <caption>{t("Kinds of quadrilaterals", "Tipos de cuadriláteros")}</caption>
        <tbody>
          <tr><td>{t("square", "cuadrado")}</td><td>{t("4 equal sides and 4 right angles", "4 lados iguales y 4 ángulos rectos")}</td></tr>
          <tr><td>{t("rectangle", "rectángulo")}</td><td>{t("4 right angles", "4 ángulos rectos")}</td></tr>
          <tr><td>{t("rhombus", "rombo")}</td><td>{t("4 equal sides", "4 lados iguales")}</td></tr>
          <tr><td>{t("parallelogram", "paralelogramo")}</td><td>{t("2 pairs of parallel sides", "2 pares de lados paralelos")}</td></tr>
          <tr><td>{t("trapezoid", "trapecio")}</td><td>{t("only 1 pair of parallel sides", "un solo par de lados paralelos")}</td></tr>
        </tbody>
      </table>
{B.om("p4", t("Practice: the best name", "Practique: el mejor nombre"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t("Geometry", "Geometría"), t("Classifying 2D shapes: attributes and vocabulary", "Clasificación de figuras 2D: atributos y vocabulario"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun svg.figura{display:block;width:100%;max-width:280px;height:auto;margin:10px auto;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Clasificación de figuras 2D: atributos y vocabulario")
