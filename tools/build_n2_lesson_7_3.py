"""Level 2 · Lesson 7.3 · Area of a circle and figures with semicircles — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json, math
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "7-3"
TEMA = ("Geometry: circles and composite figures", "Geometría transicional")
TIT = ("Area of a circle and figures with semicircles", "Área del círculo y figuras compuestas con semicírculos")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def tx(x, y, s, col="#222", tam=17, anc="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" dominant-baseline="middle" font-size="{tam}" font-weight="700" fill="{col}">{s}</text>'

def porciones(n=12):
    """Circle cut into n sectors, then the sectors laid out alternately: almost a parallelogram of base πr and height r."""
    R, cx, cy = 70, 80, 110
    ang = 2 * math.pi / n
    s = ""
    for i in range(n):
        a1, a2 = i * ang, (i + 1) * ang
        col = "#90a4ae" if i % 2 else "#cfd8dc"
        s += f'<path d="M{cx} {cy} L{cx + R * math.cos(a1):.1f} {cy - R * math.sin(a1):.1f} A{R} {R} 0 0 0 {cx + R * math.cos(a2):.1f} {cy - R * math.sin(a2):.1f} Z" fill="{col}" stroke="#37474f" stroke-width="1.5"/>'
    w = 2 * R * math.sin(ang / 2)
    h = R * math.cos(ang / 2)
    xs, yb = 270, 160
    for j in range(n):
        x = xs + j * w / 2
        if j % 2 == 0:   # apex up, arc at the bottom
            s += f'<path d="M{x + w / 2:.1f} {yb - R} L{x:.1f} {yb} Q{x + w / 2:.1f} {yb + (R - h) * 2:.1f} {x + w:.1f} {yb} Z" fill="#cfd8dc" stroke="#37474f" stroke-width="1.5"/>'
        else:            # apex down, arc at the top
            s += f'<path d="M{x + w / 2:.1f} {yb} L{x:.1f} {yb - R} Q{x + w / 2:.1f} {yb - R - (R - h) * 2:.1f} {x + w:.1f} {yb - R} Z" fill="#90a4ae" stroke="#37474f" stroke-width="1.5"/>'
    L = n / 2 * w
    s += f'<line x1="{xs}" y1="{yb + 22}" x2="{xs + L + w / 2:.1f}" y2="{yb + 22}" stroke="#0d47a1" stroke-width="2"/>' + tx(xs + (L + w / 2) / 2, yb + 40, t("base ≈ half the circumference = π × r", "base ≈ media circunferencia = π × r"), "#0d47a1", 15)
    s += f'<line x1="{xs - 10}" y1="{yb - R}" x2="{xs - 10}" y2="{yb}" stroke="#b71c1c" stroke-width="2"/>' + tx(xs - 16, yb - R / 2, t("height ≈ r", "altura ≈ r"), "#b71c1c", 15, "end")
    s += tx(cx, cy + R + 22, t("circle of radius r", "círculo de radio r"), "#37474f", 15)
    return svg("0 0 640 220", t("On the left, a circle cut into 12 equal slices. On the right, the same slices laid side by side, alternately pointing up and down: they form almost a parallelogram whose base is half the circumference, π times r, and whose height is the radius r. Its area is π r times r, that is, π r squared.",
                                "A la izquierda, un círculo cortado en 12 porciones iguales. A la derecha, las mismas porciones puestas una junto a otra, alternando hacia arriba y hacia abajo: forman casi un paralelogramo cuya base es la mitad de la circunferencia, π por r, y cuya altura es el radio r. Su área es π r por r, es decir, π r al cuadrado."), s, 640)

def pista():
    h, w = 100, 60
    esc = 3.2
    x0, y0, R = 320 - h * esc / 2, 40, w / 2 * esc
    s = f'<path d="M{x0:.1f} {y0} L{x0 + h * esc:.1f} {y0} A{R:.1f} {R:.1f} 0 0 1 {x0 + h * esc:.1f} {y0 + 2 * R:.1f} L{x0:.1f} {y0 + 2 * R:.1f} A{R:.1f} {R:.1f} 0 0 1 {x0:.1f} {y0} Z" fill="#c8e6c9" stroke="#37474f" stroke-width="3"/>'
    s += f'<rect x="{x0:.1f}" y="{y0}" width="{h * esc:.1f}" height="{2 * R:.1f}" fill="none" stroke="#37474f" stroke-width="2" stroke-dasharray="6 4"/>'
    s += tx(320, y0 + 2 * R + 22, "100 ft", "#222", 18)
    s += f'<line x1="{x0 + h * esc + 0:.1f}" y1="{y0}" x2="{x0 + h * esc:.1f}" y2="{y0 + 2 * R:.1f}" stroke="#b71c1c" stroke-width="2" stroke-dasharray="5 4"/>'
    s += tx(x0 + h * esc - 8, y0 + R, "60 ft", "#b71c1c", 18, "end")
    return svg("0 0 640 270", t("A track shape: a 100 by 60 foot rectangle, outlined with dashes, with a half circle on each short end. Each half circle has a diameter of 60 feet.",
                                "Una pista: un rectángulo de 100 por 60 pies, marcado con línea punteada, con un semicírculo en cada extremo corto. Cada semicírculo tiene un diámetro de 60 pies."), s, 640)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 7.2 you measured the edge of a circle: its circumference. This lesson finishes the study of the circle by measuring its <strong>inside surface</strong>: how much area fits inside it. You will also combine circles with simple figures to make real designs, like a running track or an arched window.", "En la Lección 7.2 se midió el borde del círculo: su circunferencia. Esta lección completa el estudio del círculo midiendo su <strong>superficie interior</strong>: cuánta área cabe dentro de él. También se aprende a combinar el círculo con figuras simples para formar diseños reales, como una pista de atletismo o una ventana en arco.")}</p>
{big("A = π × r²")}
<p style="text-align:center">{t("The area is π times <strong>the square of the radius</strong>. The square applies only to the radius, not to π.", "El área es π por <strong>el cuadrado del radio</strong>. El cuadrado afecta solo al radio, no a π.")}</p>
<h3>{t("Where the formula comes from", "De dónde viene la fórmula")}</h3>
<p>{t("Cut a circle into many thin slices and lay them side by side, alternately up and down. They form a shape that looks like a <strong>parallelogram</strong>. Its base is half the circumference (π × r) and its height is the radius (r). Base times height: π × r × r = π × r².", "Si se divide el círculo en muchas porciones delgadas y se acomodan alternando arriba y abajo, se forma una figura parecida a un <strong>paralelogramo</strong>. Su base es la mitad de la circunferencia (π × r) y su altura es el radio (r). Base por altura: π × r × r = π × r².")}</p>
<div style="text-align:center">{porciones()}</div>
{caja("ojo", t("Order of operations", "Orden de operaciones"), t("<p>In A = πr², the square applies only to the radius. First find r², then multiply by π: exponents come before multiplication (PEMDAS). For example, if r = 5, then r² = 25 and A = π × 25.</p>", "<p>En A = πr², el cuadrado se aplica solo al radio. Primero se calcula r² y luego se multiplica por π: el exponente va antes que la multiplicación (PEMDAS). Por ejemplo, si r = 5, entonces r² = 25 y A = π × 25.</p>"))}
{ej(t("Example: area from the radius", "Ejemplo: área a partir del radio"), t("Find the area of a circle with a radius of 6 in. Use π ≈ 3.14.", "Calcule el área de un círculo de radio 6 in. Use π ≈ 3.14."),
  [("1", t("Formula.", "Fórmula."), "A = π × r² ≈ 3.14 × 6²."),
   ("2", t("Square first.", "Primero el cuadrado."), "6² = 36."),
   ("3", t("Multiply.", "Multiplique."), "3.14 × 36 = 113.04."),
   ("✓", t("Answer.", "Respuesta."), t("The area is about <strong>113.04 in²</strong>.", "El área es de aproximadamente <strong>113.04 in²</strong>."))])}
{ej(t("Example: you only know the diameter", "Ejemplo: solo se conoce el diámetro"), t("Find the area of a circle with a diameter of 10 ft.", "Calcule el área de un círculo de diámetro 10 ft."),
  [("1", t("First the radius.", "Primero el radio."), "r = d ÷ 2 = 10 ÷ 2 = 5 ft."),
   ("2", t("Square the radius.", "Eleve el radio al cuadrado."), "5² = 25."),
   ("3", t("Formula.", "Fórmula."), "A ≈ 3.14 × 25 = 78.5."),
   ("✓", t("Answer.", "Respuesta."), t("The area is about <strong>78.5 ft²</strong>.", "El área es de aproximadamente <strong>78.5 ft²</strong>."))])}
{calc(t("Area on the calculator", "El área en la calculadora"), t(f"<p>For r = 6: {T('π')} {T('×')} {T('6')} {T('x²')} {T('enter')} gives 113.097… The calculator squares the 6 before it multiplies, as PEMDAS says. With 3.14 you get 113.04; both are close enough.</p>", f"<p>Para r = 6: {T('π')} {T('×')} {T('6')} {T('x²')} {T('enter')} da 113.097… La calculadora eleva el 6 al cuadrado antes de multiplicar, como manda PEMDAS. Con 3.14 sale 113.04; los dos bastan.</p>"))}
{practica("p1", t("Practice 1 — Area from the radius", "Práctica 1 — Área con el radio"), t("r = 4 in. What is the area of the circle? (π ≈ 3.14)", "r = 4 in. ¿Cuál es el área del círculo? (π ≈ 3.14)"),
          [("a", "25.12 in²"), ("b", "50.24 in²"), ("c", "157.75 in²"), ("d", "12.56 in²")])}
{practica("p2", t("Practice 2 — Area from the diameter", "Práctica 2 — Área con el diámetro"), t("d = 12 ft. What is the area of the circle? (π ≈ 3.14)", "d = 12 ft. ¿Cuál es el área del círculo? (π ≈ 3.14)"),
          [("a", "452.16 ft²"), ("b", "37.68 ft²"), ("c", "18.84 ft²"), ("d", "113.04 ft²")])}
{enlace(n, t("area-formula", "formula-area"), t("the area formula", "la fórmula del área del círculo"), t("See where A = πr² comes from and practice squaring the radius first.", "Vea de dónde sale A = πr² y practique elevando primero el radio al cuadrado."))}'''

    s2 = f'''<p>{t("The circle has two different “measures” in this topic, each with its own formula. Mixing them up is one of the most common mistakes. The rule is simple: it depends on what you want to measure, <strong>the edge or the surface</strong>.", "El círculo tiene dos «medidas» distintas en este tema, cada una con su fórmula. Confundirlas es uno de los errores más comunes. La regla es sencilla: depende de qué se quiera medir, <strong>el borde o la superficie</strong>.")}</p>
{tabla(t("Circumference or area?", "¿Circunferencia o área?"), t("Circumference and area of a circle, side by side", "Circunferencia y área del círculo, lado a lado"),
       ["", t("Circumference (edge) ⭕", "Circunferencia (borde) ⭕"), t("Area (surface) 🟣", "Área (superficie) 🟣")],
       [[t("When", "Cuándo"), t("you measure the outline: fencing around a garden, trim around a table, how far a wheel rolls in one turn", "se mide el contorno: la cerca que rodea un jardín, el ribete de una mesa, lo que avanza una rueda en una vuelta"), t("you measure the inside: grass that covers a garden, how much pizza there is, the bottom of a round pool", "se mide la superficie interior: el césped que cubre un jardín, cuánta pizza hay, el fondo de una piscina redonda")],
        [t("Formula", "Fórmula"), "C = π × d &nbsp;o&nbsp; C = 2 × π × r" if B.L == "es" else "C = π × d &nbsp;or&nbsp; C = 2 × π × r", "A = π × r²"],
        [t("Units", "Unidades"), t("linear: in, ft, yd", "lineales: in, ft, yd"), t("square: in², ft², yd²", "cuadradas: in², ft², yd²")]])}
{caja("tip", t("Word clues", "Pistas en las palabras"), t("<p>Words like “around”, “fence”, “edge”, “border”, “trim” ask for the <strong>circumference</strong>. Words like “cover”, “paint”, “plant”, “carpet”, “fill the surface” ask for the <strong>area</strong>. And the units never lie: if the answer is in feet, it is the circumference; in square feet, it is the area.</p>", "<p>Palabras como «rodear», «cerca», «borde», «contorno» piden la <strong>circunferencia</strong>. Palabras como «cubrir», «pintar», «sembrar», «alfombrar», «llenar la superficie» piden el <strong>área</strong>. Y las unidades nunca mienten: si la respuesta va en pies, es circunferencia; en pies cuadrados, es área.</p>"))}
{practica("p3", t("Practice 3 — A fence", "Práctica 3 — Una cerca"), t("How much fencing do you need to go around a round garden?", "¿Cuánta cerca hace falta para rodear un jardín redondo?"),
          [("a", t("Circumference (π × d)", "Circunferencia (π × d)")), ("b", t("Area (π × r²)", "Área (π × r²)"))])}
{practica("p4", t("Practice 4 — The grass", "Práctica 4 — El césped"), t("How much sod covers the same round garden?", "¿Cuánto césped cubre el mismo jardín redondo?"),
          [("a", t("Circumference (π × d)", "Circunferencia (π × d)")), ("b", t("Area (π × r²)", "Área (π × r²)"))])}
{enlace(n, t("which-one", "cual-usar"), t("circumference or area?", "¿circunferencia o área?"), t("Decide from the key words whether the situation asks for the edge or the surface.", "Decida a partir de las palabras clave si la situación pide el borde o la superficie."))}'''

    s3 = f'''<p>{t("When you know the area and want the radius, solve the formula. Since the radius is squared, you need a <strong>square root</strong> at the end.", "Cuando se conoce el área y se quiere el radio, hay que despejar la fórmula. Como el radio está al cuadrado, hace falta una <strong>raíz cuadrada</strong> al final.")}</p>
{big("r² = A ÷ π &nbsp;&nbsp;&nbsp; r = √(A ÷ π)")}
{ej(t("Example: from area to radius", "Ejemplo: del área al radio"), t("A round garden has an area of 78.5 ft². What is its radius?", "Un jardín redondo tiene un área de 78.5 ft². ¿Cuál es su radio?"),
  [("1", t("Divide by π.", "Divida entre π."), "r² ≈ 78.5 ÷ 3.14 = 25."),
   ("2", t("Square root.", "Raíz cuadrada."), "r = √25 = 5."),
   ("✓", t("Answer.", "Respuesta."), t("The radius of the garden is <strong>5 ft</strong>.", "El radio del jardín es de <strong>5 ft</strong>."))])}
{caja("tip", t("Connection with Topic 2", "Conexión con el Tema 2"), t("<p>Here you use what you learned in Lesson 2.3 about square roots of perfect squares. When A ÷ π is a perfect square (25, 36, 49, 100…), the radius comes out whole and the work is quick.</p>", "<p>Aquí se aprovecha lo aprendido en la Lección 2.3 sobre las raíces de cuadrados perfectos. Cuando A ÷ π da un cuadrado perfecto (25, 36, 49, 100…), el radio sale entero y el cálculo es inmediato.</p>"))}
{practica("p5", t("Practice 5 — Find the radius", "Práctica 5 — Halle el radio"), t("A circle has an area of 314 in². What is its radius? (π ≈ 3.14)", "Un círculo tiene un área de 314 in². ¿Cuál es su radio? (π ≈ 3.14)"),
          [("a", "100 in"), ("b", "50 in"), ("c", "10 in"), ("d", "20 in")])}
{enlace(n, t("radius-from-area", "radio-desde-area"), t("finding the radius from the area", "hallar el radio a partir del área"), t("Divide by π and take the square root to get back the radius.", "Divida entre π y saque la raíz cuadrada para recuperar el radio."))}'''

    s4 = f'''<p>{t("A <strong>semicircle</strong> is half of a circle. Its area is half the area of the whole circle:", "Un <strong>semicírculo</strong> es la mitad de un círculo. Su área es la mitad del área del círculo completo:")}</p>
{big(t("A<sub>semicircle</sub> = (π × r²) ÷ 2", "A<sub>semicírculo</sub> = (π × r²) ÷ 2"))}
<p>{t("Semicircles show up in many real figures together with rectangles: a running track, an arched window, a stage with a curved front.", "Los semicírculos aparecen en muchas figuras reales combinados con rectángulos: la pista de atletismo, la ventana en arco, el escenario con frente curvo.")}</p>
<div style="text-align:center">{pista()}</div>
{ej(t("Example: the track", "Ejemplo: la pista"), t("A track is made of a 100 ft × 60 ft rectangle and two semicircles, one on each short end, each with a diameter of 60 ft. What is the total area?", "Una pista está formada por un rectángulo de 100 ft × 60 ft y dos semicírculos, uno en cada extremo corto, cada uno con un diámetro de 60 ft. ¿Cuál es el área total?"),
  [("1", t("Rectangle.", "Rectángulo."), "100 × 60 = 6,000 ft²."),
   ("2", t("Two semicircles = one whole circle.", "Dos semicírculos = un círculo completo."), t("Radius: 60 ÷ 2 = 30 ft.", "Radio: 60 ÷ 2 = 30 ft.")),
   ("3", t("Area of that circle.", "Área de ese círculo."), "3.14 × 30² = 3.14 × 900 = 2,826 ft²."),
   ("4", t("Total.", "Total."), "6,000 + 2,826 = 8,826 ft²."),
   ("✓", t("Answer.", "Respuesta."), t("The track has a total area of <strong>8,826 ft²</strong>.", "La pista tiene un área total de <strong>8,826 ft²</strong>."))])}
{caja("tip", t("Handy shortcut", "Atajo útil"), t("<p>When a figure has two semicircles of the same size, put them together in your mind to make one whole circle. That saves dividing by 2 twice and lowers the chance of a mistake.</p>", "<p>Cuando una figura tiene dos semicírculos del mismo tamaño, conviene unirlos mentalmente para formar un círculo completo. Eso evita dividir entre 2 dos veces y reduce las posibilidades de error.</p>"))}
{practica("p6", t("Practice 6 — A semicircle", "Práctica 6 — Un semicírculo"), t("r = 8 in. What is the area of the semicircle? (π ≈ 3.14)", "r = 8 in. ¿Cuál es el área del semicírculo? (π ≈ 3.14)"),
          [("a", "200.96 in²"), ("b", "25.12 in²"), ("c", "100.48 in²"), ("d", "50.24 in²")])}
{enlace(n, t("semicircles", "semicirculos"), t("figures with semicircles", "figuras con semicírculos"), t("Build an arched window or a track and find its total area.", "Arme una ventana con arco o una pista de atletismo y calcule su área total."))}'''

    s5 = f'''<p>{t("The area of a circle comes up every day: planting grass, painting a round wall, covering the bottom of a pool, sharing a pizza.", "El área del círculo aparece en situaciones cotidianas: sembrar césped, pintar una pared redonda, cubrir el fondo de una piscina, repartir una pizza.")}</p>
{ej(t("Example: planting grass", "Ejemplo: sembrar césped"), t("A round flower bed has a radius of 4 ft. Sod costs $2 per square foot. How much does it cost to cover it all?", "Un parterre redondo tiene 4 ft de radio. El césped en rollo cuesta $2 por pie cuadrado. ¿Cuánto cuesta cubrirlo todo?"),
  [("1", t("Area.", "Área."), "A ≈ 3.14 × 4² = 3.14 × 16 = 50.24 ft²."),
   ("2", t("Cost.", "Costo."), "50.24 × $2 = $100.48."),
   ("✓", t("Answer.", "Respuesta."), t("Covering the flower bed costs about <strong>$100.48</strong>.", "Cubrir el parterre cuesta aproximadamente <strong>$100.48</strong>."))])}
{ej(t("Example: a table with round ends", "Ejemplo: una mesa con extremos redondos"), t("A dining table is a 6 ft × 3 ft rectangle with a semicircle on each short end (diameter 3 ft). What is its total area?", "Una mesa de comedor es un rectángulo de 6 ft × 3 ft con un semicírculo en cada extremo corto (diámetro 3 ft). ¿Cuál es su área total?"),
  [("1", t("Rectangle.", "Rectángulo."), "6 × 3 = 18 ft²."),
   ("2", t("Two semicircles = one circle.", "Dos semicírculos = un círculo."), t("Radius: 3 ÷ 2 = 1.5 ft. Area ≈ 3.14 × 1.5² = 3.14 × 2.25 = 7.065 ft².", "Radio: 3 ÷ 2 = 1.5 ft. Área ≈ 3.14 × 1.5² = 3.14 × 2.25 = 7.065 ft².")),
   ("3", t("Total.", "Total."), "18 + 7.065 = 25.065 ft²."),
   ("✓", t("Answer.", "Respuesta."), t("The table has an area of about <strong>25.07 ft²</strong>.", "La mesa tiene un área de aproximadamente <strong>25.07 ft²</strong>."))])}
{practica("p7", t("Practice 7 — Sod for a flower bed", "Práctica 7 — Césped para un parterre"), t("A round flower bed has a radius of 5 ft. Sod costs $2 per square foot. What does it cost? (π ≈ 3.14)", "Un parterre redondo tiene 5 ft de radio. El césped cuesta $2 por pie cuadrado. ¿Cuánto cuesta? (π ≈ 3.14)"),
          [("a", "$31.40"), ("b", "$62.80"), ("c", "$78.50"), ("d", "$157")])}
{enlace(n, t("applications", "aplicaciones"), t("uses of the area of a circle", "aplicaciones del área del círculo"), t("Solve problems about pizzas, gardens, and sprinklers, and compare prices per square inch.", "Resuelva problemas de pizzas, jardines y aspersores, y compare precios por pulgada cuadrada."))}'''

    secciones = [("s-" + t("area-formula", "formula-area"), t("The area formula", "La fórmula del área del círculo"), s1),
                 ("s-" + t("which-one", "cual-usar"), t("Circumference or area: which one?", "Circunferencia o área: ¿cuál usar?"), s2),
                 ("s-" + t("radius-from-area", "radio-desde-area"), t("The reverse problem: the radius from the area", "El problema inverso: el radio a partir del área"), s3),
                 ("s-" + t("semicircles", "semicirculos"), t("Composite figures with semicircles", "Figuras compuestas con semicírculos"), s4),
                 ("s-" + t("applications", "aplicaciones"), t("Real uses", "Aplicaciones reales"), s5)]

    lesson = {"next": t("Topic 8", "Tema 8"), "review": t("sections 1, 2, and 4", "las secciones 1, 2 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("That is the circumference (2 × π × r). The area is π × r².", "Esa es la circunferencia (2 × π × r). El área es π × r²."), "c": t("You squared 3.14 × 4. The square applies only to the radius.", "Elevó al cuadrado 3.14 × 4. El cuadrado se aplica solo al radio."), "d": t("You multiplied by 4 instead of 4². Square the radius: 4 × 4 = 16.", "Multiplicó por 4 en vez de 4². Eleve el radio al cuadrado: 4 × 4 = 16.")},
             "right": t("3.14 × 16 = 50.24 in².", "3.14 × 16 = 50.24 in²."), "solution": t("A = π × r² ≈ 3.14 × 4² = 3.14 × 16 = 50.24 in².", "A = π × r² ≈ 3.14 × 4² = 3.14 × 16 = 50.24 in².")},
      "p2": {"ok": "d", "hints": {"a": t("You used the diameter as the radius. First divide by 2: r = 6.", "Usó el diámetro como radio. Primero divida entre 2: r = 6."), "b": t("That is the circumference.", "Esa es la circunferencia."), "c": t("That is π × 6. Square the radius: 6² = 36.", "Eso es π × 6. Eleve el radio al cuadrado: 6² = 36.")},
             "right": t("r = 6; 3.14 × 36 = 113.04 ft².", "r = 6; 3.14 × 36 = 113.04 ft²."), "solution": t("r = 12 ÷ 2 = 6; A ≈ 3.14 × 6² = 3.14 × 36 = 113.04 ft².", "r = 12 ÷ 2 = 6; A ≈ 3.14 × 6² = 3.14 × 36 = 113.04 ft².")},
      "p3": {"ok": "a", "hints": {"b": t("“Go around” asks for the edge: the circumference.", "«Rodear» pide el borde: la circunferencia.")},
             "right": t("The fence is the edge: circumference, in feet.", "La cerca es el borde: circunferencia, en pies."), "solution": t("Going around = the edge = the circumference.", "Rodear = el borde = la circunferencia.")},
      "p4": {"ok": "b", "hints": {"a": t("“Cover” asks for the surface: the area.", "«Cubrir» pide la superficie: el área.")},
             "right": t("The sod covers the surface: area, in square feet.", "El césped cubre la superficie: área, en pies cuadrados."), "solution": t("Covering = the surface = the area.", "Cubrir = la superficie = el área.")},
      "p5": {"ok": "c", "hints": {"a": t("That is r². Take the square root.", "Ese es r². Saque la raíz cuadrada."), "b": t("You divided by 2π (that is for the circumference). With the area, divide by π and take the square root.", "Dividió entre 2π (eso es para la circunferencia). Con el área se divide entre π y se saca la raíz."), "d": t("That is the diameter. The radius is half.", "Ese es el diámetro. El radio es la mitad.")},
             "right": t("314 ÷ 3.14 = 100; √100 = 10 in.", "314 ÷ 3.14 = 100; √100 = 10 in."), "solution": t("r² ≈ 314 ÷ 3.14 = 100; r = √100 = 10 in.", "r² ≈ 314 ÷ 3.14 = 100; r = √100 = 10 in.")},
      "p6": {"ok": "c", "hints": {"a": t("That is the whole circle. A semicircle is half.", "Ese es el círculo completo. El semicírculo es la mitad."), "b": t("That is half the circumference. Use the area: π × r² ÷ 2.", "Eso es media circunferencia. Use el área: π × r² ÷ 2."), "d": t("That is the circumference. Use π × r² ÷ 2.", "Esa es la circunferencia. Use π × r² ÷ 2.")},
             "right": t("3.14 × 64 ÷ 2 = 100.48 in².", "3.14 × 64 ÷ 2 = 100.48 in²."), "solution": t("(3.14 × 8²) ÷ 2 = (3.14 × 64) ÷ 2 = 200.96 ÷ 2 = 100.48 in².", "(3.14 × 8²) ÷ 2 = (3.14 × 64) ÷ 2 = 200.96 ÷ 2 = 100.48 in².")},
      "p7": {"ok": "d", "hints": {"a": t("That is the circumference in feet, not money.", "Esa es la circunferencia en pies, no dinero."), "b": t("You used the circumference. Covering asks for the area.", "Usó la circunferencia. Cubrir pide el área."), "c": t("$78.50 would be at $1 per square foot. Multiply by $2.", "$78.50 sería a $1 por pie cuadrado. Multiplique por $2.")},
             "right": t("78.5 × 2 = $157.", "78.5 × 2 = $157."), "solution": t("A ≈ 3.14 × 5² = 78.5 ft²; 78.5 × $2 = $157.", "A ≈ 3.14 × 5² = 78.5 ft²; 78.5 × $2 = $157.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("That is the circumference.", "Esa es la circunferencia."), "c": t("The square applies only to the radius.", "El cuadrado se aplica solo al radio."), "d": t("That is 6², without π.", "Eso es 6², sin π.")}, "solution": t("3.14 × 36 = 113.04 in².", "3.14 × 36 = 113.04 in².")},
      "B": {"ok": "d", "hints": {"a": t("That is the circumference.", "Esa es la circunferencia."), "b": t("You used the diameter as the radius.", "Usó el diámetro como radio."), "c": t("That is half the circumference.", "Eso es media circunferencia.")}, "solution": t("r = 5; 3.14 × 25 = 78.5 ft².", "r = 5; 3.14 × 25 = 78.5 ft².")},
      "C": {"ok": "a", "hints": {"b": t("A fence goes around: it is the edge.", "La cerca rodea: es el borde."), "c": t("The radius alone is not the length of the fence.", "El radio solo no es la longitud de la cerca."), "d": t("The diameter alone is not the length of the fence.", "El diámetro solo no es la longitud de la cerca.")}, "solution": t("Around = circumference.", "Rodear = circunferencia.")},
      "D": {"ok": "c", "hints": {"a": t("Grass covers the surface.", "El césped cubre la superficie."), "b": t("The diameter is a length, not a surface.", "El diámetro es una longitud, no una superficie."), "d": t("The radius is a length, not a surface.", "El radio es una longitud, no una superficie.")}, "solution": t("Cover = area.", "Cubrir = área.")},
      "E": {"ok": "b", "hints": {"a": t("That is r². Take the square root.", "Ese es r². Saque la raíz cuadrada."), "c": t("Divide by π, not by 2π.", "Divida entre π, no entre 2π."), "d": t("Check: √25.", "Revise: √25.")}, "solution": t("78.5 ÷ 3.14 = 25; √25 = 5 ft.", "78.5 ÷ 3.14 = 25; √25 = 5 ft.")},
      "F": {"ok": "d", "hints": {"a": t("That is the circumference.", "Esa es la circunferencia."), "b": t("That is the whole circle.", "Ese es el círculo completo."), "c": t("That is half the circumference.", "Eso es media circunferencia.")}, "solution": t("3.14 × 64 ÷ 2 = 100.48 in².", "3.14 × 64 ÷ 2 = 100.48 in².")},
      "G": {"ok": "a", "hints": {"b": t("Two semicircles make one circle, not two.", "Dos semicírculos forman un círculo, no dos."), "c": t("There is a semicircle on each end.", "Hay un semicírculo en cada extremo."), "d": t("You added a length to an area.", "Sumó una longitud a un área.")}, "solution": t("6,000 + 2,826 = 8,826 ft².", "6,000 + 2,826 = 8,826 ft².")},
      "H": {"ok": "c", "hints": {"a": t("That is the circumference, not the area.", "Esa es la circunferencia, no el área."), "b": t("That is the area; multiply by $2.", "Esa es el área; multiplique por $2."), "d": t("You doubled twice. 50.24 × 2.", "Duplicó dos veces. 50.24 × 2.")}, "solution": t("3.14 × 16 = 50.24; × $2 = $100.48.", "3.14 × 16 = 50.24; × $2 = $100.48.")}
     }}

    quiz = [
     ("A", t("What is the area of a circle with a radius of 6 in? (π ≈ 3.14)", "¿Cuál es el área de un círculo de radio 6 in? (π ≈ 3.14)"), [("a", "37.68 in²"), ("b", "113.04 in²"), ("c", "354.95 in²"), ("d", "36 in²")]),
     ("B", t("What is the area of a circle with a diameter of 10 ft? (π ≈ 3.14)", "¿Cuál es el área de un círculo de diámetro 10 ft? (π ≈ 3.14)"), [("a", "31.4 ft²"), ("b", "314 ft²"), ("c", "15.7 ft²"), ("d", "78.5 ft²")]),
     ("C", t("To find how much fencing goes around a round garden, you calculate the…", "Para saber cuánta cerca rodea un jardín redondo, se calcula…"), [("a", t("circumference", "la circunferencia")), ("b", t("area", "el área")), ("c", t("radius", "el radio")), ("d", t("diameter", "el diámetro"))]),
     ("D", t("To find how much sod covers a round garden, you calculate the…", "Para saber cuánto césped cubre un jardín redondo, se calcula…"), [("a", t("circumference", "la circunferencia")), ("b", t("diameter", "el diámetro")), ("c", t("area", "el área")), ("d", t("radius", "el radio"))]),
     ("E", t("A round garden has an area of 78.5 ft². What is its radius? (π ≈ 3.14)", "Un jardín redondo tiene un área de 78.5 ft². ¿Cuál es su radio? (π ≈ 3.14)"), [("a", "25 ft"), ("b", "5 ft"), ("c", "12.5 ft"), ("d", "2.5 ft")]),
     ("F", t("What is the area of a semicircle with a radius of 8 in? (π ≈ 3.14)", "¿Cuál es el área de un semicírculo de radio 8 in? (π ≈ 3.14)"), [("a", "50.24 in²"), ("b", "200.96 in²"), ("c", "25.12 in²"), ("d", "100.48 in²")]),
     ("G", t("A track is a 100 ft × 60 ft rectangle with a semicircle (diameter 60 ft) on each end. What is its area? (π ≈ 3.14)", "Una pista es un rectángulo de 100 ft × 60 ft con un semicírculo (diámetro 60 ft) en cada extremo. ¿Cuál es su área? (π ≈ 3.14)"), [("a", "8,826 ft²"), ("b", "11,652 ft²"), ("c", "7,413 ft²"), ("d", "6,188.4 ft²")]),
     ("H", t("A round flower bed has a radius of 4 ft. Sod costs $2 per square foot. What does it cost? (π ≈ 3.14)", "Un parterre redondo tiene 4 ft de radio. El césped cuesta $2 por pie cuadrado. ¿Cuánto cuesta? (π ≈ 3.14)"), [("a", "$25.12"), ("b", "$50.24"), ("c", "$100.48"), ("d", "$200.96")])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("The inside of the circle: A = πr², when to use circumference and when to use area, the radius from the area, and figures that combine rectangles with semicircles.", "El interior del círculo: A = πr², cuándo usar la circunferencia y cuándo el área, el radio a partir del área y figuras que combinan rectángulos con semicírculos."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Find</strong> the area of a circle with A = π × r².", "<strong>Calcular</strong> el área de un círculo con la fórmula A = π × r²."),
         t("<strong>Decide</strong> when to use the circumference (edge) and when to use the area (surface).", "<strong>Distinguir</strong> cuándo usar la circunferencia (borde) y cuándo el área (superficie)."),
         t("<strong>Solve</strong> for the radius when you know the area.", "<strong>Despejar</strong> el radio cuando se conoce el área del círculo."),
         t("<strong>Find</strong> the area of composite figures that combine rectangles and semicircles.", "<strong>Calcular</strong> el área de figuras compuestas que combinan rectángulos con semicírculos."),
         t("<strong>Use</strong> the area of a circle for real surfaces: gardens, pools, tracks.", "<strong>Aplicar</strong> el área del círculo a superficies reales: jardines, piscinas, pistas.")],
        secciones,
        (t("Find the area in five problems given the radius and three given the diameter. Find the radius in three problems given the area. Solve four composite figures with rectangles and semicircles, and three “circumference or area?” problems.",
           "Calcule el área en cinco ejercicios dado el radio y en tres dado el diámetro. Halle el radio en tres ejercicios dada el área. Resuelva cuatro figuras compuestas con rectángulos y semicírculos, y tres problemas de «¿circunferencia o área?»."),
         t("Compare two pizza sizes from a menu you know. Find the area of each in square inches and the price per square inch. Which one is the better deal?",
           "Compare dos tamaños de pizza de un menú que conozca. Calcule el área de cada una en pulgadas cuadradas y el precio por pulgada cuadrada. ¿Cuál conviene más?")),
        quiz,
        t("Self-check checklist for the area of a circle", "Lista de autoevaluación del área del círculo"),
        t("Self-check checklist: skills for the area of a circle", "Lista de autoevaluación: destrezas del área del círculo"),
        [(t("Use A = πr²", "Aplicar A = πr²"), t("I use the formula with the radius or the diameter, check, and explain the order of operations.", "Aplico la fórmula con el radio o con el diámetro, compruebo y explico el orden de operaciones."), t("I use the formula with help.", "Aplico la fórmula con apoyo."), t("I mix up r² with 2r.", "Confundo r² con 2r.")),
         (t("Circumference or area", "Circunferencia o área"), t("I tell them apart, justify it with the units, and use both in mixed problems.", "Las distingo, lo justifico con las unidades y aplico las dos en problemas mixtos."), t("I choose with help from the key words.", "Elijo con apoyo de las palabras clave."), t("I use one formula for the other.", "Uso una fórmula por la otra.")),
         (t("Semicircles and the reverse problem", "Semicírculos y problema inverso"), t("I join two semicircles into one circle, solve for the radius, and check by working backward.", "Uno dos semicírculos en un círculo, despejo el radio y compruebo calculando hacia atrás."), t("I solve simple cases with help.", "Resuelvo casos sencillos con apoyo."), t("I do not see the semicircle as half a circle.", "No reconozco el semicírculo como mitad de un círculo."))],
        t("<p>This lesson closes <strong>Topic 7</strong>. You can now find the area of composite figures, the circumference and the area of a circle, and the area of designs that combine rectangles with semicircles. The number <strong>π</strong>, discovered in Lesson 7.2, has become a familiar tool.</p>\n<p><strong>Topic 8 · Statistics and probability</strong> changes the setting one last time in Level 2. Lesson 8.1 opens it with the basic measures that sum up a set of data in a single number, and what you learned here about the circle comes back in Lesson 8.2, with circle graphs.</p>",
          "<p>Con esta lección se cierra el <strong>Tema 7</strong>. Quedaron dominadas el área de figuras compuestas, la circunferencia y el área del círculo, y la combinación de rectángulos con semicírculos en diseños reales. El número <strong>π</strong>, descubierto en la Lección 7.2, se volvió una herramienta familiar.</p>\n<p>El <strong>Tema 8 · Estadística y probabilidad</strong> cambia el terreno por última vez en el Nivel 2. La Lección 8.1 lo abre con las medidas básicas para resumir un conjunto de datos en un único número representativo, y lo aprendido aquí sobre el círculo volverá en la Lección 8.2, con los gráficos circulares.</p>"),
        ("8-1", ("", t("Lesson 8.1 · Mean, median, mode, range, and weighted mean", "Lección 8.1 · Media, mediana, moda, rango y media ponderada"))),
        [(t("area of a circle", "área del círculo"), t("The surface inside a circle: A = π × r².", "La superficie interior de un círculo: A = π × r².")),
         (t("semicircle", "semicírculo"), t("Half a circle; its area is (π × r²) ÷ 2.", "La mitad de un círculo; su área es (π × r²) ÷ 2.")),
         (t("square root", "raíz cuadrada"), t("The number that, squared, gives the original: √25 = 5.", "El número que, elevado al cuadrado, da el original: √25 = 5.")),
         (t("in terms of π", "en términos de π"), t("An exact answer that keeps the π symbol, like 36π.", "Un resultado exacto que conserva el símbolo π, como 36π."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "scVoz": "A circle cut into {n} slices arranged like a parallelogram with base π times r and height r.", "base": "base ≈ π × r", "scCasi": "is almost a rectangle", "scOnda": "still has wavy edges",
  "scSal": "With {n} slices the shape {x}. Area ≈ base × height = (π × r) × r = <strong>π × r²</strong>.",
  "ctx": ["a circle", "a pizza", "a round garden", "a round table", "a round rug"], "aQ": "Find the area of {c} with a {t} of {v} in.", "diam": "diameter", "radio": "radius",
  "aS1": "r = {d} ÷ 2 = {r}. ", "aS": "A ≈ 3.14 × {r}² = 3.14 × {k} ≈ {x} (or {k}π).",
  "aP1": "That is the circumference (2 × π × r). The area is π × r².", "aP2": "You used the diameter as the radius: divide by 2 first.", "aP3": "The square applies only to the radius, not to π × r.",
  "cu": [["How much fencing do you need to go around a round garden?", "c"], ["How much sod covers a round garden?", "a"], ["How much pizza is there in a 14-inch pizza?", "a"], ["How far does a wheel roll in one turn?", "c"], ["How much paint do you need for the bottom of a round pool?", "a"], ["How much ribbon do you need for the edge of a round cake?", "c"], ["How much fabric do you need for a round tablecloth?", "a"], ["How long is one lap of a circular track?", "c"], ["What area does a sprinkler that reaches 5 ft water?", "a"], ["How long is the frame of a round mirror?", "c"]],
  "cuC": "Circumference (edge): π × d", "cuA": "Area (surface): π × r²", "cuBC": "It measures the edge: circumference, in linear units.", "cuBA": "It measures the surface: area, in square units.", "cuMC": "It asks for the edge: circumference.", "cuMA": "It asks for the surface: area.",
  "ivCtx": ["A round garden has an area of", "A pizza has an area of", "A round rug covers", "A sprinkler waters a circle of"], "ivQ": "{c} {A} square feet. How long is its {t}? (π ≈ 3.14)",
  "ivS": "r² = {A} ÷ 3.14 = {k}; r = √{k} = {r}", "ivSd": "; d = 2 × {r} = {d}", "ivP1": "That is r². Take the square root.", "ivP2": "That would be with the circumference. With the area, divide by π and take the square root.", "ivP3": "That is the radius. The diameter is twice as long.",
  "smV": "Window: a rectangle {w} by {h} with a semicircle of diameter {w} on top.", "smP": "Track: a rectangle {h} by {w} with a semicircle on each end.",
  "smR": "Rectangle: {w} × {h} = {A} ft².", "smS1": "Semicircle with radius {r}: 3.14 × {r}² ÷ 2 = {x} ft².", "smS2": "Two semicircles with radius {r} make one circle: 3.14 × {r}² = {x} ft².", "smT": "Total area ≈ {x} ft²",
  "seQ1": "A window is a rectangle {w} ft wide and {h} ft tall, with a semicircle on top. What is its area, in ft²?", "seQ2": "A field is a rectangle {h} ft long and {w} ft wide, with a semicircle on each end. What is its area, in ft²?",
  "seS": "Rectangle: {R}; {x}; total ≈ {T} ft².", "seS1": "semicircle: 3.14 × {r}² ÷ 2 = {s}", "seS2": "whole circle: 3.14 × {r}² = {s}",
  "seP1": "On top there is half a circle: its area is divided by 2.", "seP2": "The radius is half the width.", "seP3": "Two semicircles make one circle, not two.", "seP4": "There are two semicircles, one on each end.",
  "pz": "A {d1}-inch pizza costs {p1} and a {d2}-inch pizza costs {p2}. How many inches across is the one that costs less per square inch?",
  "pzP": "Compare the price per square inch: price ÷ area. The bigger pizza is not always the better deal.", "pzS": "Areas: {a1} and {a2} in². Price per in²: {u1} and {u2}. The {m}-inch pizza is the better deal.",
  "ce": "You will plant sod in a round garden with a radius of {r} ft. Sod costs {p} per square foot. What does it cost, in dollars? (π ≈ 3.14)", "ceS": "A = 3.14 × {r}² = {A} ft²; × {p} ≈ {x}.", "ceP": "You used the circumference. Planting asks for the area.",
  "as": "A sprinkler waters in a circle up to {r} ft away. What area does it water, in ft²? (π ≈ 3.14)", "asS": "The reach is the radius: 3.14 × {r}² ≈ {x} ft².", "asP": "The sprinkler's reach is the radius, not the diameter.",
  "bo": "You want to put a decorative border around a round fountain with a radius of {r} ft. How many feet of border do you need? (π ≈ 3.14)", "boS": "It is the edge: C = 2 × 3.14 × {r} ≈ {x} ft.", "boP": "You found the area. “Around” asks for the circumference."
 },
 "es": {
  "scVoz": "Círculo cortado en {n} porciones acomodadas como un paralelogramo de base pi por r y altura r.", "base": "base ≈ π × r", "scCasi": "ya casi es un rectángulo", "scOnda": "todavía tiene los bordes ondulados",
  "scSal": "Con {n} porciones la figura {x}. Área ≈ base × altura = (π × r) × r = <strong>π × r²</strong>.",
  "ctx": ["un círculo", "una pizza", "un jardín redondo", "una mesa redonda", "una alfombra redonda"], "aQ": "Calcule el área de {c} con un {t} de {v} in.", "diam": "diámetro", "radio": "radio",
  "aS1": "r = {d} ÷ 2 = {r}. ", "aS": "A ≈ 3.14 × {r}² = 3.14 × {k} ≈ {x} (o {k}π).",
  "aP1": "Esa es la circunferencia (2 × π × r). El área es π × r².", "aP2": "Se usó el diámetro como radio: primero se divide entre 2.", "aP3": "El cuadrado se aplica solo al radio, no a π × r.",
  "cu": [["¿Cuánta cerca hace falta para rodear un jardín redondo?", "c"], ["¿Cuánto césped cubre un jardín redondo?", "a"], ["¿Cuánta pizza hay en una pizza de 14 pulgadas?", "a"], ["¿Qué distancia avanza una rueda en una vuelta?", "c"], ["¿Cuánta pintura hace falta para el fondo de una piscina redonda?", "a"], ["¿Cuánto listón hace falta para el borde de un pastel redondo?", "c"], ["¿Cuánta tela hace falta para un mantel redondo?", "a"], ["¿Cuánto mide una vuelta a una pista circular?", "c"], ["¿Qué superficie riega un aspersor que alcanza 5 ft?", "a"], ["¿Cuánto mide el marco de un espejo redondo?", "c"]],
  "cuC": "Circunferencia (borde): π × d", "cuA": "Área (superficie): π × r²", "cuBC": "Se mide el borde: circunferencia, en unidades lineales.", "cuBA": "Se mide la superficie: área, en unidades cuadradas.", "cuMC": "Se pide el borde: circunferencia.", "cuMA": "Se pide la superficie: área.",
  "ivCtx": ["Un jardín redondo tiene un área de", "Una pizza tiene un área de", "Una alfombra redonda cubre", "Un aspersor riega un círculo de"], "ivQ": "{c} {A} pies cuadrados. ¿Cuánto mide su {t}? (π ≈ 3.14)",
  "ivS": "r² = {A} ÷ 3.14 = {k}; r = √{k} = {r}", "ivSd": "; d = 2 × {r} = {d}", "ivP1": "Ese es r². Falta sacar la raíz cuadrada.", "ivP2": "Eso sería con la circunferencia. Con el área se divide entre π y se saca la raíz.", "ivP3": "Ese es el radio. El diámetro es el doble.",
  "smV": "Ventana: rectángulo de {w} por {h} con un semicírculo de diámetro {w} encima.", "smP": "Pista: rectángulo de {h} por {w} con un semicírculo en cada extremo.",
  "smR": "Rectángulo: {w} × {h} = {A} ft².", "smS1": "Semicírculo de radio {r}: 3.14 × {r}² ÷ 2 = {x} ft².", "smS2": "Dos semicírculos de radio {r} forman un círculo: 3.14 × {r}² = {x} ft².", "smT": "Área total ≈ {x} ft²",
  "seQ1": "Una ventana es un rectángulo de {w} ft de ancho y {h} ft de alto, con un semicírculo encima. ¿Cuál es su área, en ft²?", "seQ2": "Un campo es un rectángulo de {h} ft de largo y {w} ft de ancho, con un semicírculo en cada extremo. ¿Cuál es su área, en ft²?",
  "seS": "Rectángulo: {R}; {x}; total ≈ {T} ft².", "seS1": "semicírculo: 3.14 × {r}² ÷ 2 = {s}", "seS2": "círculo completo: 3.14 × {r}² = {s}",
  "seP1": "Arriba hay medio círculo: su área se divide entre 2.", "seP2": "El radio es la mitad del ancho.", "seP3": "Dos semicírculos forman un solo círculo, no dos.", "seP4": "Hay dos semicírculos, uno en cada extremo.",
  "pz": "Una pizza de {d1} pulgadas cuesta {p1} y una de {d2} pulgadas cuesta {p2}. ¿De cuántas pulgadas de diámetro es la que sale más barata por pulgada cuadrada?",
  "pzP": "Compare el precio por pulgada cuadrada: precio ÷ área. La pizza más grande no siempre conviene más.", "pzS": "Áreas: {a1} y {a2} in². Precio por in²: {u1} y {u2}. Conviene la de {m} pulgadas.",
  "ce": "Se va a sembrar césped en un jardín redondo de {r} ft de radio. El césped cuesta {p} por pie cuadrado. ¿Cuánto cuesta, en dólares? (π ≈ 3.14)", "ceS": "A = 3.14 × {r}² = {A} ft²; × {p} ≈ {x}.", "ceP": "Se calculó con la circunferencia. Sembrar pide el área.",
  "as": "Un aspersor riega en círculo hasta {r} ft de distancia. ¿Qué área riega, en ft²? (π ≈ 3.14)", "asS": "El alcance es el radio: 3.14 × {r}² ≈ {x} ft².", "asP": "El alcance del aspersor es el radio, no el diámetro.",
  "bo": "Se quiere poner un borde decorativo alrededor de una fuente redonda de {r} ft de radio. ¿Cuántos pies de borde hacen falta? (π ≈ 3.14)", "boS": "Es el borde: C = 2 × 3.14 × {r} ≈ {x} ft.", "boP": "Se calculó el área. «Alrededor» pide la circunferencia."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }

/* ============ MODULE 1 · the slices ============ */
function pintaSC(){
  var n = +$("sc-n").value, R = 70, ang = 2 * Math.PI / n, cx = 100, cy = 110, yb = 160, xs = 230;
  var s = '<svg class="figura" viewBox="0 0 640 230" role="img" aria-label="' + F(TXT.scVoz, { n: n }) + '">';
  for (var i = 0; i < n; i++){ var a1 = i * ang, a2 = (i + 1) * ang; s += '<path d="M' + cx + ' ' + cy + ' L' + f1(cx + R * Math.cos(a1)) + ' ' + f1(cy - R * Math.sin(a1)) + ' A' + R + ' ' + R + ' 0 0 0 ' + f1(cx + R * Math.cos(a2)) + ' ' + f1(cy - R * Math.sin(a2)) + ' Z" fill="' + (i % 2 ? "#90a4ae" : "#cfd8dc") + '" stroke="#37474f" stroke-width="1.5"/>'; }
  var w = 2 * R * Math.sin(ang / 2), h = R * Math.cos(ang / 2);
  for (var j = 0; j < n; j++){
    var x = xs + j * w / 2;
    if (j % 2 === 0) s += '<path d="M' + f1(x + w / 2) + ' ' + f1(yb - R) + ' L' + f1(x) + ' ' + yb + ' Q' + f1(x + w / 2) + ' ' + f1(yb + (R - h) * 2) + ' ' + f1(x + w) + ' ' + yb + ' Z" fill="#cfd8dc" stroke="#37474f" stroke-width="1.5"/>';
    else s += '<path d="M' + f1(x + w / 2) + ' ' + yb + ' L' + f1(x) + ' ' + f1(yb - R) + ' Q' + f1(x + w / 2) + ' ' + f1(yb - R - (R - h) * 2) + ' ' + f1(x + w) + ' ' + f1(yb - R) + ' Z" fill="#90a4ae" stroke="#37474f" stroke-width="1.5"/>';
  }
  var L = n / 2 * w + w / 2;
  s += textoA([xs + L / 2, yb + 30], TXT.base, 16, "#0d47a1") + textoA([xs - 14, yb - R / 2], "r", 18, "#b71c1c", 700, "end");
  $("sc-svg").innerHTML = s + '</svg>';
  $("sc-nv").textContent = n;
  $("sc-salida").innerHTML = '<div class="linea">' + F(TXT.scSal, { n: n, x: n >= 20 ? TXT.scCasi : TXT.scOnda }) + '</div>';
}
function genA(){
  var conD = Math.random() < 0.35, r = aleatorio(2, 20), k = r * r;
  var p = [{ k: 2 * r, msg: TXT.aP1 }];
  if (conD) p.push({ k: 4 * r * r, msg: TXT.aP2 });
  var base = evaluaPiK(k, p.filter(function(x){ return x.k !== k; })), mal = r2(Math.pow(3.14 * r, 2));
  return { enun: F(TXT.aQ, { c: elige(TXT.ctx), t: conD ? TXT.diam : TXT.radio, v: conD ? 2 * r : r }), correcta: nd(r2(3.14 * k)),
    solucion: (conD ? F(TXT.aS1, { d: 2 * r, r: r }) : "") + F(TXT.aS, { r: r, k: k, x: nd(r2(3.14 * k)) }),
    evalua: function(t){ var v = leeD(String(t)); if (v !== null && Math.abs(v - mal) < 0.02) return { estado: "mal", msg: TXT.aP3 }; return base(t); } };
}

/* ============ MODULE 2 · circumference or area ============ */
function genCual(){
  var e = elige(TXT.cu), c = e[1] === "c";
  return { enun: e[0], opciones: [{ html: TXT.cuC, clave: "c" }, { html: TXT.cuA, clave: "a" }], correcta: e[1], enOrden: true, bien: c ? TXT.cuBC : TXT.cuBA, mal: c ? TXT.cuMC : TXT.cuMA };
}

/* ============ MODULE 3 · the radius from the area ============ */
function genInvA(){
  var r = aleatorio(2, 15), A = r2(3.14 * r * r), pideD = Math.random() < 0.3, res = pideD ? 2 * r : r;
  var o = { c: elige(TXT.ivCtx), A: nd(A), t: pideD ? TXT.diam : TXT.radio, k: r * r, r: r, d: 2 * r };
  var p = [{ v: r * r, msg: TXT.ivP1 }, { v: r2(A / 6.28), msg: TXT.ivP2 }];
  if (pideD) p.push({ v: r, msg: TXT.ivP3 });
  return { enun: F(TXT.ivQ, o), correcta: String(res), solucion: F(TXT.ivS, o) + (pideD ? F(TXT.ivSd, o) : "") + ".",
    evalua: evaluaInvPi(res, pideD ? 2 * Math.sqrt(A / Math.PI) : Math.sqrt(A / Math.PI), p.filter(function(x){ return Math.abs(x.v - res) > 0.02; })) };
}

/* ============ MODULE 4 · semicircles ============ */
function semiSVG(tp, w, h){
  var u = " ft";
  if (tp === 1) return figuraSVG([{ pts: [[0,0],[w,0],[w,h],[0,h]] }], [[[0,0],[w,0], w + u, 1], [[w,0],[w,h], h + u, 1]], F(TXT.smV, { w: w, h: h }), [{ arco: true, c: [w / 2, h], r: w / 2, pts: [[0,h + w / 2]] }], 300);
  var r = w / 2, esc = Math.min(440 / (h + w), 200 / w), x0 = 320 - h * esc / 2, y0 = 140 - r * esc, R = r * esc;
  var s = '<svg class="figura" viewBox="0 0 640 300" role="img" aria-label="' + F(TXT.smP, { h: h, w: w }) + '">';
  s += '<path d="M' + f1(x0) + ' ' + f1(y0) + ' L' + f1(x0 + h * esc) + ' ' + f1(y0) + ' A' + f1(R) + ' ' + f1(R) + ' 0 0 1 ' + f1(x0 + h * esc) + ' ' + f1(y0 + 2 * R) + ' L' + f1(x0) + ' ' + f1(y0 + 2 * R) + ' A' + f1(R) + ' ' + f1(R) + ' 0 0 1 ' + f1(x0) + ' ' + f1(y0) + ' Z" fill="#cfd8dc" stroke="#37474f" stroke-width="3"/>';
  s += '<rect x="' + f1(x0) + '" y="' + f1(y0) + '" width="' + f1(h * esc) + '" height="' + f1(2 * R) + '" fill="#eceff1" stroke="#37474f" stroke-width="2" stroke-dasharray="6 4"/>';
  s += textoA([x0 + h * esc / 2, y0 + 2 * R + 24], h + u, 18, "#222") + lineaD([x0 + h * esc / 2, y0], [x0 + h * esc / 2, y0 + 2 * R]) + textoA([x0 + h * esc / 2 + 8, y0 + R], w + u, 18, "#b71c1c", 700, "start");
  return s + '</svg>';
}
function pintaSM(){
  var tp = +$("sm-t").value, w = +$("sm-w").value, h = +$("sm-h").value, r = w / 2, Ar = w * h, As = tp === 1 ? 3.14 * r * r / 2 : 3.14 * r * r;
  $("sm-wv").textContent = w; $("sm-hv").textContent = h;
  $("sm-svg").innerHTML = semiSVG(tp, w, h);
  $("sm-salida").innerHTML = '<div class="linea">' + F(TXT.smR, { w: w, h: h, A: nd(Ar) }) + '</div><div class="linea">' + F(tp === 1 ? TXT.smS1 : TXT.smS2, { r: nd(r), x: nd(r2(As)) }) + '</div><div class="linea veredicto">' + F(TXT.smT, { x: nd(r2(Ar + As)) }) + '</div>';
}
function genSemi(){
  var tp = aleatorio(1, 2), w = 2 * aleatorio(1, 8), h = aleatorio(3, 20), r = w / 2, S = tp === 1 ? 3.14 * r * r / 2 : 3.14 * r * r, A = w * h + S, Api = w * h + (tp === 1 ? Math.PI * r * r / 2 : Math.PI * r * r);
  var p = tp === 1 ? [{ v: r2(w * h + 3.14 * r * r), msg: TXT.seP1 }, { v: r2(w * h + 3.14 * w * w / 2), msg: TXT.seP2 }] : [{ v: r2(w * h + 2 * 3.14 * r * r), msg: TXT.seP3 }, { v: r2(w * h + 3.14 * r * r / 2), msg: TXT.seP4 }];
  var x = F(tp === 1 ? TXT.seS1 : TXT.seS2, { r: nd(r), s: nd(r2(S)) });
  return { enun: F(tp === 1 ? TXT.seQ1 : TXT.seQ2, { w: w, h: h }) + semiSVG(tp, w, h), correcta: nd(r2(A)), solucion: F(TXT.seS, { R: nd(w * h), x: x, T: nd(r2(A)) }),
    evalua: evaluaInvPi(r2(A), Api, p.filter(function(q){ return Math.abs(q.v - r2(A)) > 0.05; })) };
}

/* ============ MODULE 5 · real uses ============ */
function genApl(){
  var tp = aleatorio(1, 4), res, resPi, enun, sol, p = [];
  if (tp === 1){ var d1 = elige([10, 12]), d2 = elige([14, 16, 18]), p1 = elige([8, 9, 10]), p2 = elige([13, 15, 17]), a1 = 3.14 * d1 * d1 / 4, a2 = 3.14 * d2 * d2 / 4, u1 = p1 / a1, u2 = p2 / a2, m = u1 < u2 ? d1 : d2;
    if (Math.abs(u1 - u2) < 0.004) return genApl();
    res = m; resPi = m; enun = F(TXT.pz, { d1: d1, d2: d2, p1: dinero(p1), p2: dinero(p2) });
    sol = F(TXT.pzS, { a1: nd(r2(a1)), a2: nd(r2(a2)), u1: "$" + u1.toFixed(3), u2: "$" + u2.toFixed(3), m: m }); p.push({ v: m === d1 ? d2 : d1, msg: TXT.pzP }); }
  else if (tp === 2){ var r = aleatorio(3, 12), pc = elige([1, 1.5, 2, 2.5]); res = r2(3.14 * r * r * pc); resPi = Math.PI * r * r * pc;
    enun = F(TXT.ce, { r: r, p: dinero2(pc) }); sol = F(TXT.ceS, { r: r, A: nd(r2(3.14 * r * r)), p: dinero2(pc), x: dinero2(res) }); p.push({ v: r2(2 * 3.14 * r * pc), msg: TXT.ceP }); }
  else if (tp === 3){ var ra = aleatorio(4, 20); res = r2(3.14 * ra * ra); resPi = Math.PI * ra * ra; enun = F(TXT.as, { r: ra }); sol = F(TXT.asS, { r: ra, x: nd(res) }); p.push({ v: r2(3.14 * ra * ra / 4), msg: TXT.asP }); }
  else { var rr = aleatorio(2, 10); res = r2(2 * 3.14 * rr); resPi = 2 * Math.PI * rr; enun = F(TXT.bo, { r: rr }); sol = F(TXT.boS, { r: rr, x: nd(res) }); p.push({ v: r2(3.14 * rr * rr), msg: TXT.boP }); }
  return { enun: enun, correcta: tp === 2 ? dinero2(res) : nd(res), solucion: sol, evalua: evaluaInvPi(res, resPi, p.filter(function(q){ return Math.abs(q.v - res) > 0.05; })) };
}

/* ============ Start ============ */
$("sc-n").addEventListener("input", pintaSC); pintaSC();
creaPracticaLibre("p1", genA);
creaPracticaOM("p2", genCual);
creaPracticaLibre("p3", genInvA);
$("sm-t").addEventListener("change", pintaSM); ["sm-w", "sm-h"].forEach(function(id){ $(id).addEventListener("input", pintaSM); }); pintaSM();
creaPracticaLibre("p4", genSemi);
creaPracticaLibre("p5", genApl);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA_PI = ("Use π ≈ 3.14 and round to two decimal places, or write the answer in terms of π, like 36π.", "Use π ≈ 3.14 y redondee a dos decimales, o escriba el resultado en términos de π, como 36π.")
NOTA_2 = ("Use π ≈ 3.14 and round to two decimal places if needed.", "Use π ≈ 3.14 y redondee a dos decimales si hace falta.")

def practica_pagina():
    n = N
    mods = [
     (t("area-formula", "formula-area"), t("The area formula", "La fórmula del área del círculo"),
      f'''      <div class="formula">A = π × r²</div>
      <p>{t("Cut the circle into slices and lay them alternately up and down: they form almost a parallelogram whose base is half the circumference (π × r) and whose height is the radius (r). The more slices, the closer it gets to a rectangle.", "Si se corta el círculo en porciones y se acomodan alternando arriba y abajo, forman casi un paralelogramo cuya base es la mitad de la circunferencia (π × r) y cuya altura es el radio (r). Cuantas más porciones, más se parece a un rectángulo.")}</p>
      <h3>{t("Cut the circle", "Corte el círculo")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="sc-n">{t("Number of slices", "Número de porciones")}: <span id="sc-nv"></span></label><input type="range" id="sc-n" min="4" max="32" step="2" value="8"></div></div>
        <div id="sc-svg"></div>
        <div class="salida" id="sc-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Order of operations:", "Orden de operaciones:")}</strong> {t("square the radius first, then multiply by π. If r = 5, then r² = 25 and A = π × 25.", "primero se eleva el radio al cuadrado y después se multiplica por π. Si r = 5, entonces r² = 25 y A = π × 25.")}</div>
{libre_x("p1", t("Practice: find the area", "Practique: calcule el área"), t("Area", "Área"), t(*NOTA_PI))}'''),
     (t("which-one", "cual-usar"), t("Circumference or area?", "¿Circunferencia o área?"),
      f'''      <table class="reglas">
        <caption>{t("Two measures of the circle", "Dos medidas del círculo")}</caption>
        <thead><tr><th scope="col"></th><th scope="col">{t("Circumference (edge)", "Circunferencia (borde)")}</th><th scope="col">{t("Area (surface)", "Área (superficie)")}</th></tr></thead>
        <tbody>
          <tr><th scope="row">{t("Key words", "Palabras clave")}</th><td>{t("around, fence, edge, border, one lap", "rodear, cerca, borde, contorno, una vuelta")}</td><td>{t("cover, paint, plant, carpet, how much fits", "cubrir, pintar, sembrar, alfombrar, cuánto cabe")}</td></tr>
          <tr><th scope="row">{t("Formula", "Fórmula")}</th><td>C = π × d</td><td>A = π × r²</td></tr>
          <tr><th scope="row">{t("Units", "Unidades")}</th><td>{t("linear: in, ft, yd", "lineales: in, ft, yd")}</td><td>{t("square: in², ft², yd²", "cuadradas: in², ft², yd²")}</td></tr>
        </tbody>
      </table>
{B.om("p2", t("Practice: circumference or area?", "Practique: ¿circunferencia o área?"))}'''),
     (t("radius-from-area", "radio-desde-area"), t("The radius from the area", "El radio a partir del área"),
      f'''      <p>{t("Since the radius is squared, you need a square root at the end: first divide by π, then take the square root.", "Como el radio está al cuadrado, al final hace falta una raíz cuadrada: primero se divide entre π y después se saca la raíz.")}</p>
      <div class="formula">r² = A ÷ π &nbsp;&nbsp;&nbsp; r = √(A ÷ π)</div>
      <div class="caja-tip"><strong>{t("Example:", "Ejemplo:")}</strong> {t("a garden has an area of 78.5 ft². 78.5 ÷ 3.14 = 25, and √25 = 5 ft.", "un jardín tiene un área de 78.5 ft². 78.5 ÷ 3.14 = 25, y √25 = 5 ft.")}</div>
{libre_x("p3", t("Practice: from the area to the radius", "Practique: del área al radio"), t("Answer", "Resultado"), t("Type only the number, for example 5.", "Escriba solo el número, por ejemplo 5."))}'''),
     (t("semicircles", "semicirculos"), t("Figures with semicircles", "Figuras con semicírculos"),
      f'''      <p>{t("A semicircle is half a circle: its area is (π × r²) ÷ 2. When there are two equal semicircles, put them together into one whole circle.", "Un semicírculo es medio círculo: su área es (π × r²) ÷ 2. Cuando hay dos semicírculos iguales, conviene unirlos en un círculo completo.")}</p>
      <h3>{t("Build the figure", "Arme la figura")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="sm-t">{t("Figure", "Figura")}</label><select id="sm-t"><option value="1">{t("Window: rectangle with a semicircle on top", "Ventana: rectángulo con un semicírculo arriba")}</option><option value="2">{t("Track: rectangle with two semicircles", "Pista: rectángulo con dos semicírculos")}</option></select></div>
          <div class="campo" style="flex:1;min-width:150px;"><label for="sm-w">{t("Rectangle width (ft)", "Ancho del rectángulo (ft)")}: <span id="sm-wv"></span></label><input type="range" id="sm-w" min="2" max="20" step="2" value="6"></div>
          <div class="campo" style="flex:1;min-width:150px;"><label for="sm-h">{t("Rectangle length (ft)", "Largo del rectángulo (ft)")}: <span id="sm-hv"></span></label><input type="range" id="sm-h" min="2" max="30" value="8"></div>
        </div>
        <div id="sm-svg"></div>
        <div class="salida" id="sm-salida" aria-live="polite"></div>
      </div>
{libre_x("p4", t("Practice: rectangles and semicircles", "Practique: rectángulos y semicírculos"), t("Area (ft²)", "Área (ft²)"), t(*NOTA_2))}'''),
     (t("applications", "aplicaciones"), t("Real uses", "Aplicaciones reales"),
      f'''      <p>{t("Pizzas, gardens, sprinklers, and fountains. Before you calculate, decide whether the problem asks for the edge or the surface.", "Pizzas, jardines, aspersores y fuentes. Antes de calcular, decida si el problema pide el borde o la superficie.")}</p>
{libre_x("p5", t("Practice: problems with circles", "Practique: problemas con círculos"), t("Answer", "Resultado"), t(*NOTA_2))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/geometry.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Área del círculo y figuras compuestas con semicírculos")
