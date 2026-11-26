"""Level 2 · Lesson 7.2 · Circumference of a circle — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json, math
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "7-2"
TEMA = ("Geometry: circles and composite figures", "Geometría transicional")
TIT = ("Circumference of a circle", "Circunferencia del círculo")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def tx(x, y, s, col="#222", tam=17, anc="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" dominant-baseline="middle" font-size="{tam}" font-weight="700" fill="{col}">{s}</text>'

def anatomia():
    cx, cy, R = 220, 150, 115
    a = math.radians(50); px, py = cx + R * math.cos(a), cy - R * math.sin(a)
    s = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#eceff1" stroke="#37474f" stroke-width="5"/>'
    s += f'<line x1="{cx - R}" y1="{cy}" x2="{cx + R}" y2="{cy}" stroke="#0d47a1" stroke-width="4"/>'
    s += f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="#b71c1c" stroke-width="4"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#222"/>' + tx(cx - 14, cy - 16, "O")
    s += tx((cx + px) / 2 - 22, (cy + py) / 2 - 10, t("radius r", "radio r"), "#b71c1c", 16, "end")
    s += tx(cx, cy + 22, t("diameter d", "diámetro d"), "#0d47a1", 16)
    s += f'<line x1="{cx + R * 0.74:.1f}" y1="{cy + R * 0.74:.1f}" x2="{cx + R * 0.74 + 40:.1f}" y2="{cy + R * 0.74 + 26:.1f}" stroke="#37474f" stroke-width="2"/>'
    s += tx(cx + R * 0.74 + 46, cy + R * 0.74 + 30, t("circumference C (the edge)", "circunferencia C (el borde)"), "#37474f", 16, "start")
    return svg("0 0 640 300", t("A circle with center O. A red segment from the center to the edge is the radius r. A blue segment through the center from edge to edge is the diameter d. The edge of the circle is the circumference C.",
                                "Un círculo con centro O. Un segmento rojo del centro al borde es el radio r. Un segmento azul que atraviesa el círculo por el centro es el diámetro d. El borde del círculo es la circunferencia C."), s, 640)

def desenrolla():
    d, u = 2, 60
    C = math.pi * d
    R, cx, cy = d * u / 2, 40 + d * u / 2, 70
    y = cy + R + 40
    s = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#eceff1" stroke="#37474f" stroke-width="4"/><line x1="{cx - R}" y1="{cy}" x2="{cx + R}" y2="{cy}" stroke="#0d47a1" stroke-width="3"/>'
    s += f'<line x1="40" y1="{y}" x2="{40 + C * u:.1f}" y2="{y}" stroke="#37474f" stroke-width="6"/>'
    for k in range(3):
        s += f'<rect x="{40 + k * d * u}" y="{y + 10}" width="{d * u}" height="14" fill="{"#90caf9" if k % 2 else "#0d47a1"}"/>' + tx(40 + (k + .5) * d * u, y + 40, "d", "#0d47a1", 16)
    s += f'<rect x="{40 + 3 * d * u}" y="{y + 10}" width="{0.14159 * d * u:.1f}" height="14" fill="#f9a825"/>' + tx(40 + C * u + 8, y, "C", "#37474f", 17, "start")
    return svg(f"0 0 460 {y + 64:.0f}", t("The edge of a circle stretched into a straight line C. Three diameters fit along it, plus a small extra piece of about 0.14 diameter, shown in yellow.",
                                         "El borde de un círculo estirado en una línea recta C. A lo largo de ella caben tres diámetros, más un pedacito de unas 0.14 veces el diámetro, en amarillo."), s, 460)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 7.1 you worked with rectangles, triangles, and trapezoids: figures with straight sides. This lesson brings in a completely different figure: the <strong>circle</strong>, a closed curve whose points are all the same distance from a center point. The old formulas are not enough to measure it; a famous constant appears: <strong>π</strong> (pi).", "En la Lección 7.1 se trabajó con rectángulos, triángulos y trapecios: figuras de lados rectos. Esta lección introduce una figura completamente distinta: el <strong>círculo</strong>, una curva cerrada cuyos puntos están todos a la misma distancia de un punto central. Para medirlo no bastan las fórmulas anteriores; aparece una constante célebre: <strong>π</strong> (pi).")}</p>
<div style="text-align:center">{anatomia()}</div>
{tabla(t("Parts of a circle", "Partes del círculo"), t("The parts of a circle", "Las partes del círculo"),
       [t("Part", "Parte"), t("What it is", "Qué es")],
       [[t("Center (O)", "Centro (O)"), t("the point that is the same distance from every point on the circle", "el punto que está a la misma distancia de todos los puntos del círculo")],
        [t("Radius (r)", "Radio (r)"), t("the distance from the center to any point on the circle", "la distancia del centro a cualquier punto del círculo")],
        [t("Diameter (d)", "Diámetro (d)"), t("the segment across the circle through the center; it is <strong>twice the radius</strong>", "el segmento que atraviesa el círculo pasando por el centro; es <strong>el doble del radio</strong>")],
        [t("Circumference (C)", "Circunferencia (C)"), t("the length of the edge of the circle: its “perimeter”", "la longitud del borde del círculo: su «perímetro»")]])}
{big("d = 2 × r &nbsp;&nbsp;&nbsp; r = d ÷ 2")}
{caja("ojo", t("Careful with the words", "Cuidado con las palabras"), t("<p>The <strong>circle</strong> is the whole region, including the inside; the <strong>circumference</strong> is only the edge. People sometimes use the words loosely, but when you measure, be clear about which one you are measuring.</p>", "<p>El <strong>círculo</strong> es la región completa, incluido el interior; la <strong>circunferencia</strong> es solo el borde. A veces se usan como sinónimos, pero al medir hay que tener claro qué se está midiendo.</p>"))}
{practica("p1", t("Practice 1 — Radius and diameter", "Práctica 1 — Radio y diámetro"), t("A circle has a radius of 12 in. How long is its diameter?", "Un círculo tiene un radio de 12 in. ¿Cuánto mide su diámetro?"),
          [("a", "6 in"), ("b", "24 in"), ("c", "12 in"), ("d", "37.68 in")])}
{enlace(n, t("anatomy", "anatomia"), t("the parts of a circle", "las partes del círculo"), t("Move the radius and watch the diameter and the circumference change.", "Mueva el radio y vea cómo cambian el diámetro y la circunferencia."))}'''

    s2 = f'''<p>{t("Measure the edge (the circumference, C) of several round objects with a string, and measure their diameter (d) with a ruler. Something amazing happens: the ratio C ÷ d <strong>always gives the same number</strong>, whatever the size of the object.", "Si se mide con una cuerda el contorno (la circunferencia, C) de varios objetos redondos y se mide también su diámetro (d) con una regla, se descubre algo asombroso: la razón C ÷ d <strong>siempre da el mismo número</strong>, sin importar el tamaño del objeto.")}</p>
{tabla(t("C ÷ d in real objects", "C ÷ d en objetos reales"), t("The ratio C ÷ d in real objects", "La razón C ÷ d en objetos reales"),
       [t("Object", "Objeto"), t("Diameter d (in)", "Diámetro d (in)"), t("Circumference C (in)", "Circunferencia C (in)"), "C ÷ d"],
       [[t("Quarter (coin)", "Moneda de 25 centavos"), "0.955", "3.00", "≈ 3.14"], [t("Dinner plate", "Plato"), "10", "31.42", "≈ 3.14"], [t("Soda can", "Lata de refresco"), "2.6", "8.17", "≈ 3.14"], [t("Car tire", "Llanta de carro"), "26", "81.68", "≈ 3.14"]])}
<div style="text-align:center">{desenrolla()}</div>
<p>{t("That constant number has its own name: <strong>π</strong>, the Greek letter “pi”. Its exact value has infinitely many decimal places with no repeating pattern, but for calculations an approximation is enough:", "Ese número constante tiene nombre propio: <strong>π</strong>, la letra griega «pi». Su valor exacto tiene infinitas cifras decimales sin patrón que se repita, pero para los cálculos basta con aproximarlo:")}</p>
{big("π ≈ 3.14159")}
<p>{t("The usual approximation is <strong>π ≈ 3.14</strong>. Another useful one, as a fraction, is <strong>π ≈ 22/7</strong>. The calculator also has a π key, which gives a slightly more exact answer.", "La aproximación habitual es <strong>π ≈ 3.14</strong>. Otra útil, en fracción, es <strong>π ≈ 22/7</strong>. La calculadora tiene además una tecla π, que da un resultado un poco más exacto.")}</p>
{caja("tip", t("A key idea", "Idea fundamental"), t("<p>Nobody invented π. It is a constant of nature: every circle, of any size, has a circumference about 3.14159 times its diameter. That is why π shows up so often in mathematics.</p>", "<p>π no es una invención humana. Es una constante de la naturaleza: cualquier círculo, sin importar su tamaño, tiene una circunferencia de aproximadamente 3.14159 veces su diámetro. Por eso aparece tantas veces en las matemáticas.</p>"))}
{practica("p2", t("Practice 2 — The ratio", "Práctica 2 — La razón"), t("For any circle, the ratio circumference ÷ diameter is…", "En cualquier círculo, la razón circunferencia ÷ diámetro es…"),
          [("a", t("different for each circle", "distinta para cada círculo")), ("b", t("always 2", "siempre 2")), ("c", t("always the same: π", "siempre la misma: π")), ("d", t("larger for larger circles", "mayor en los círculos grandes"))])}
{enlace(n, t("pi", "pi"), t("the discovery of π", "el descubrimiento de π"), t("Unroll the edge of a wheel and see that it is always a little more than three diameters: π.", "Desenrolle el borde de una rueda y vea que siempre mide un poco más de tres diámetros: π."))}'''

    s3 = f'''<p>{t("The definition of π gives the circumference formula right away. If C ÷ d = π, then:", "La definición de π da de inmediato la fórmula de la circunferencia. Si C ÷ d = π, entonces:")}</p>
{big("C = π × d")}
<p style="text-align:center">{t("when you know the <strong>diameter</strong>", "cuando se conoce el <strong>diámetro</strong>")}</p>
{big("C = 2 × π × r")}
<p style="text-align:center">{t("when you know the <strong>radius</strong> (because d = 2r)", "cuando se conoce el <strong>radio</strong> (porque d = 2r)")}</p>
<p>{t("The two formulas are the same; choose based on the data you have. Both are on the GED formula sheet.", "Las dos fórmulas son equivalentes; se elige según el dato que se tenga. Las dos aparecen en la hoja de fórmulas del GED.")}</p>
{ej(t("Example: with the diameter", "Ejemplo: con el diámetro"), t("A pizza has a diameter of 14 inches. What is its circumference?", "Una pizza tiene un diámetro de 14 pulgadas. ¿Cuál es su circunferencia?"),
  [("1", t("Data.", "Datos."), t("d = 14 in. Use C = π × d.", "d = 14 in. Se usa C = π × d.")),
   ("2", t("Substitute.", "Sustituya."), "C ≈ 3.14 × 14 = 43.96 in."),
   ("✓", t("Answer.", "Respuesta."), t("The circumference of the pizza is about <strong>44 inches</strong>.", "La circunferencia de la pizza mide aproximadamente <strong>44 pulgadas</strong>."))])}
{ej(t("Example: with the radius", "Ejemplo: con el radio"), t("A circular walking path has a radius of 40 feet. How long is one full lap?", "Un sendero circular tiene un radio de 40 pies. ¿Cuánto mide una vuelta completa?"),
  [("1", t("Data.", "Datos."), t("r = 40 ft. Use C = 2 × π × r.", "r = 40 ft. Se usa C = 2 × π × r.")),
   ("2", t("Substitute.", "Sustituya."), "C ≈ 2 × 3.14 × 40 = 251.2 ft."),
   ("✓", t("Answer.", "Respuesta."), t("One lap is about <strong>251.2 feet</strong>.", "Una vuelta completa mide aproximadamente <strong>251.2 pies</strong>."))])}
{caja("ojo", t("Watch out", "Atención"), t("<p>Any result found with π ≈ 3.14 is approximate, not exact. That is why we write “≈” (approximately equal). If an exact answer is asked for, leave it <strong>in terms of π</strong>: C = 14π inches.</p>", "<p>El resultado de un cálculo con π ≈ 3.14 es aproximado, no exacto. Por eso se escribe «≈» (aproximadamente igual). Si se pide un resultado exacto, se deja <strong>en términos de π</strong>: C = 14π pulgadas.</p>"))}
{calc(t("π on the calculator", "π en la calculadora"), t(f"<p>For the walking path: {T('2')} {T('×')} {T('π')} {T('×')} {T('40')} {T('enter')} gives 251.327… With the π key the answer is a little more exact than with 3.14 (251.2). On the GED, both are usually close enough; read the answer choices.</p>", f"<p>Para el sendero: {T('2')} {T('×')} {T('π')} {T('×')} {T('40')} {T('enter')} da 251.327… Con la tecla π el resultado es un poco más exacto que con 3.14 (251.2). En el GED, los dos suelen bastar; fíjese en las opciones de respuesta.</p>"))}
{practica("p3", t("Practice 3 — With the diameter", "Práctica 3 — Con el diámetro"), t("d = 10 in. What is C? (π ≈ 3.14)", "d = 10 in. ¿Cuánto mide C? (π ≈ 3.14)"), [("a", "15.7 in"), ("b", "62.8 in"), ("c", "13.14 in"), ("d", "31.4 in")])}
{practica("p4", t("Practice 4 — With the radius", "Práctica 4 — Con el radio"), t("r = 6 ft. What is C? (π ≈ 3.14)", "r = 6 ft. ¿Cuánto mide C? (π ≈ 3.14)"), [("a", "37.68 ft"), ("b", "18.84 ft"), ("c", "113.04 ft"), ("d", "12 ft")])}
{enlace(n, t("formulas", "formulas"), t("the two circumference formulas", "las dos fórmulas de la circunferencia"), t("Use the calculator with the diameter or the radius and practice C = πd and C = 2πr.", "Use la calculadora con el diámetro o con el radio y practique C = πd y C = 2πr."))}'''

    s4 = f'''<p>{t("Sometimes you know the circumference and need the radius or the diameter. Just solve the formula:", "A veces se conoce la circunferencia y se busca el radio o el diámetro. Basta con despejar la fórmula:")}</p>
{big("d = C ÷ π &nbsp;&nbsp;&nbsp; r = C ÷ (2π)")}
{ej(t("Example: find the radius", "Ejemplo: hallar el radio"), t("The edge of a round table is 188.4 in long. What is its radius?", "El borde de una mesa redonda mide 188.4 in. ¿Cuál es su radio?"),
  [("1", t("Data.", "Datos."), t("C = 188.4 in. You want r.", "C = 188.4 in. Se busca r.")),
   ("2", t("Solve.", "Despeje."), "r = C ÷ (2π) ≈ 188.4 ÷ (2 × 3.14) = 188.4 ÷ 6.28."),
   ("3", t("Divide.", "Divida."), "188.4 ÷ 6.28 = 30."),
   ("✓", t("Answer.", "Respuesta."), t("The radius of the table is <strong>30 in</strong>.", "El radio de la mesa es de <strong>30 in</strong>."))])}
{caja("tip", t("Check", "Comprobación"), t("<p>Check by working backward. If r = 30 in, then C = 2 × 3.14 × 30 = 188.4 in. ✓ It matches. This quick check catches arithmetic mistakes.</p>", "<p>Conviene comprobar calculando hacia atrás. Si r = 30 in, entonces C = 2 × 3.14 × 30 = 188.4 in. ✓ Coincide. Esta comprobación rápida atrapa los errores de cálculo.</p>"))}
{practica("p5", t("Practice 5 — Find the radius", "Práctica 5 — Halle el radio"), t("A circular track has a circumference of 314 ft. What is its radius? (π ≈ 3.14)", "Una pista circular tiene una circunferencia de 314 ft. ¿Cuál es su radio? (π ≈ 3.14)"),
          [("a", "100 ft"), ("b", "25 ft"), ("c", "50 ft"), ("d", "157 ft")])}
{enlace(n, t("solve-for-radius", "hallar-radio"), t("finding the radius or the diameter", "hallar el radio o el diámetro"), t("Start from the circumference and solve for the diameter or the radius.", "Parta de la circunferencia y despeje el diámetro o el radio."))}'''

    s5 = f'''<p>{t("The circumference shows up in very concrete situations: how much fencing goes around a round garden, how much trim covers the edge of a table, how far a tire rolls in one turn.", "La circunferencia aparece en situaciones muy concretas: cuánta cerca rodea un jardín redondo, cuánto ribete cubre el borde de una mesa, qué distancia recorre una llanta en una vuelta.")}</p>
{ej(t("Example: fencing a garden", "Ejemplo: cercar un jardín"), t("A round garden has a radius of 7 ft. How many feet of fencing go around it? Use π ≈ 22/7.", "Un jardín redondo tiene un radio de 7 ft. ¿Cuántos pies de cerca hacen falta para rodearlo? Use π ≈ 22/7."),
  [("1", t("Formula.", "Fórmula."), "C = 2 × π × r ≈ 2 × (22/7) × 7."),
   ("2", t("Simplify.", "Simplifique."), t("The 7 in the denominator cancels with the radius: 2 × 22 = 44.", "El 7 del denominador se cancela con el radio: 2 × 22 = 44.")),
   ("✓", t("Answer.", "Respuesta."), t("About <strong>44 ft</strong> of fencing. (22/7 is handy when the radius is a multiple of 7.)", "Unos <strong>44 ft</strong> de cerca. (La fracción 22/7 es cómoda cuando el radio es múltiplo de 7.)"))])}
{ej(t("Example: a rolling tire", "Ejemplo: una llanta en movimiento"), t("A car tire has a diameter of 24 in. How far does the car move in one full turn of the tire?", "Una llanta de carro tiene un diámetro de 24 in. ¿Qué distancia recorre el carro en una vuelta completa de la llanta?"),
  [("1", t("One turn = the circumference.", "Una vuelta = la circunferencia."), "C ≈ 3.14 × 24 = 75.36 in."),
   ("2", t("In feet.", "En pies."), "75.36 ÷ 12 = 6.28 ft."),
   ("✓", t("Answer.", "Respuesta."), t("With each turn the car moves about <strong>75.36 in</strong>, a little more than 6 feet.", "En cada vuelta el carro avanza unas <strong>75.36 in</strong>, un poco más de 6 pies."))])}
{practica("p6", t("Practice 6 — A fountain", "Práctica 6 — Una fuente"), t("A round fountain has a radius of 4 ft. How long is its edge? (π ≈ 3.14)", "Una fuente redonda tiene un radio de 4 ft. ¿Cuánto mide su borde? (π ≈ 3.14)"),
          [("a", "12.56 ft"), ("b", "25.12 ft"), ("c", "50.24 ft"), ("d", "8 ft")])}
{enlace(n, t("applications", "aplicaciones"), t("uses of the circumference", "aplicaciones de la circunferencia"), t("Solve problems about wheels, fences, and round tracks.", "Resuelva problemas de ruedas, cercas y pistas circulares."))}'''

    secciones = [("s-" + t("anatomy", "anatomia"), t("The parts of a circle", "Las partes del círculo"), s1),
                 ("s-" + t("pi", "pi"), t("The discovery of π", "El descubrimiento de π"), s2),
                 ("s-" + t("formulas", "formulas"), t("The two circumference formulas", "Las dos fórmulas de la circunferencia"), s3),
                 ("s-" + t("solve-for-radius", "hallar-radio"), t("The reverse problem: finding the radius", "El problema inverso: hallar el radio"), s4),
                 ("s-" + t("applications", "aplicaciones"), t("Real uses", "Aplicaciones reales"), s5)]

    lesson = {"next": t("Lesson 7.3", "Lección 7.3"), "review": t("sections 3 and 4", "las secciones 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("It is the other way: the diameter is twice the radius.", "Es al revés: el diámetro es el doble del radio."), "c": t("That is the radius.", "Ese es el radio."), "d": t("That is the circumference idea. The diameter is just 2 × r.", "Esa es la idea de la circunferencia. El diámetro es solo 2 × r.")},
             "right": t("d = 2 × 12 = 24 in.", "d = 2 × 12 = 24 in."), "solution": t("d = 2 × r = 2 × 12 = 24 in.", "d = 2 × r = 2 × 12 = 24 in.")},
      "p2": {"ok": "c", "hints": {"a": t("Look at the table: big or small, the ratio is about 3.14.", "Mire la tabla: grande o pequeño, la razón es unos 3.14."), "b": t("2 is the ratio of the diameter to the radius.", "2 es la razón entre el diámetro y el radio."), "d": t("Look at the table: the tire and the coin give the same ratio.", "Mire la tabla: la llanta y la moneda dan la misma razón.")},
             "right": t("C ÷ d = π for every circle.", "C ÷ d = π en todos los círculos."), "solution": t("C ÷ d is always π ≈ 3.14, whatever the size.", "C ÷ d es siempre π ≈ 3.14, sea cual sea el tamaño.")},
      "p3": {"ok": "d", "hints": {"a": t("With the diameter, C = π × d: do not divide by 2.", "Con el diámetro, C = π × d: no se divide entre 2."), "b": t("That would be with the 10 as the radius.", "Eso sería si 10 fuera el radio."), "c": t("You added 3.14. Multiply.", "Sumó 3.14. Multiplique.")},
             "right": t("3.14 × 10 = 31.4 in.", "3.14 × 10 = 31.4 in."), "solution": t("C = π × d ≈ 3.14 × 10 = 31.4 in.", "C = π × d ≈ 3.14 × 10 = 31.4 in.")},
      "p4": {"ok": "a", "hints": {"b": t("With the radius, C = 2 × π × r: multiply by 2 too.", "Con el radio, C = 2 × π × r: falta multiplicar por 2."), "c": t("That is π × r², the area. The circumference is 2 × π × r.", "Eso es π × r², el área. La circunferencia es 2 × π × r."), "d": t("That is the diameter. Multiply by π.", "Ese es el diámetro. Multiplique por π.")},
             "right": t("2 × 3.14 × 6 = 37.68 ft.", "2 × 3.14 × 6 = 37.68 ft."), "solution": t("C = 2 × π × r ≈ 2 × 3.14 × 6 = 37.68 ft.", "C = 2 × π × r ≈ 2 × 3.14 × 6 = 37.68 ft.")},
      "p5": {"ok": "c", "hints": {"a": t("That is the diameter (314 ÷ 3.14). The radius is half.", "Ese es el diámetro (314 ÷ 3.14). El radio es la mitad."), "b": t("Check: 314 ÷ 6.28.", "Revise: 314 ÷ 6.28."), "d": t("You divided by 2 only. Divide by 2π.", "Dividió solo entre 2. Divida entre 2π.")},
             "right": t("314 ÷ 6.28 = 50 ft.", "314 ÷ 6.28 = 50 ft."), "solution": t("r = C ÷ (2π) ≈ 314 ÷ 6.28 = 50 ft.", "r = C ÷ (2π) ≈ 314 ÷ 6.28 = 50 ft.")},
      "p6": {"ok": "b", "hints": {"a": t("With the radius you also multiply by 2.", "Con el radio también se multiplica por 2."), "c": t("That is the area (π × r²). The edge is the circumference.", "Esa es el área (π × r²). El borde es la circunferencia."), "d": t("That is the diameter.", "Ese es el diámetro.")},
             "right": t("2 × 3.14 × 4 = 25.12 ft.", "2 × 3.14 × 4 = 25.12 ft."), "solution": t("C = 2 × π × r ≈ 2 × 3.14 × 4 = 25.12 ft.", "C = 2 × π × r ≈ 2 × 3.14 × 4 = 25.12 ft.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The diameter goes all the way across.", "El diámetro atraviesa todo el círculo."), "b": t("The circumference is the edge.", "La circunferencia es el borde."), "d": t("The center is a point.", "El centro es un punto.")}, "solution": t("The distance from the center to the edge is the radius.", "La distancia del centro al borde es el radio.")},
      "B": {"ok": "a", "hints": {"b": t("It is the other way: the diameter is twice the radius.", "Es al revés: el diámetro es el doble del radio."), "c": t("That is the radius.", "Ese es el radio."), "d": t("You do not need π to find the diameter.", "Para el diámetro no hace falta π.")}, "solution": t("d = 2 × 12 = 24 in.", "d = 2 × 12 = 24 in.")},
      "C": {"ok": "d", "hints": {"a": t("The digits are switched.", "Las cifras están cambiadas."), "b": t("π is a little more than 3.", "π es un poco más de 3."), "c": t("The fraction is 22/7, not 22.7.", "La fracción es 22/7, no 22.7.")}, "solution": t("π ≈ 3.14.", "π ≈ 3.14.")},
      "D": {"ok": "b", "hints": {"a": t("It is the same for every circle.", "Es la misma para todos los círculos."), "c": t("Size does not change it.", "El tamaño no la cambia."), "d": t("2 is diameter ÷ radius.", "2 es diámetro ÷ radio.")}, "solution": t("C ÷ d = π always.", "C ÷ d = π siempre.")},
      "E": {"ok": "a", "hints": {"b": t("With the diameter, do not divide by 2.", "Con el diámetro no se divide entre 2."), "c": t("That is the area.", "Esa es el área."), "d": t("That is the radius.", "Ese es el radio.")}, "solution": t("3.14 × 9 = 28.26 in.", "3.14 × 9 = 28.26 in.")},
      "F": {"ok": "c", "hints": {"a": t("Multiply by 2 too.", "Multiplique también por 2."), "b": t("That is the area.", "Esa es el área."), "d": t("That is the diameter.", "Ese es el diámetro.")}, "solution": t("2 × 3.14 × 4 = 25.12 ft.", "2 × 3.14 × 4 = 25.12 ft.")},
      "G": {"ok": "b", "hints": {"a": t("That is the diameter.", "Ese es el diámetro."), "c": t("Check: 314 ÷ 6.28.", "Revise: 314 ÷ 6.28."), "d": t("Divide by 2π, not by 2.", "Divida entre 2π, no entre 2.")}, "solution": t("314 ÷ 6.28 = 50 ft.", "314 ÷ 6.28 = 50 ft.")},
      "H": {"ok": "d", "hints": {"a": t("That is 22/7 × 7 only; multiply by 2 too.", "Eso es solo 22/7 × 7; falta multiplicar por 2."), "b": t("That is the area (π × r²).", "Esa es el área (π × r²)."), "c": t("You used 14 as the radius.", "Usó 14 como radio.")}, "solution": t("2 × (22/7) × 7 = 44 ft.", "2 × (22/7) × 7 = 44 ft.")}
     }}

    quiz = [
     ("A", t("The distance from the center of a circle to its edge is called the…", "La distancia del centro de un círculo a su borde se llama…"), [("a", t("diameter", "diámetro")), ("b", t("circumference", "circunferencia")), ("c", t("radius", "radio")), ("d", t("center", "centro"))]),
     ("B", t("A circle has a radius of 12 in. Its diameter is…", "Un círculo tiene un radio de 12 in. Su diámetro mide…"), [("a", "24 in"), ("b", "6 in"), ("c", "12 in"), ("d", "37.68 in")]),
     ("C", t("π is approximately…", "π es aproximadamente…"), [("a", "3.41"), ("b", "2.14"), ("c", "22.7"), ("d", "3.14")]),
     ("D", t("For any circle, circumference ÷ diameter is…", "En cualquier círculo, circunferencia ÷ diámetro es…"), [("a", t("different for each circle", "distinta para cada círculo")), ("b", t("always π", "siempre π")), ("c", t("larger for larger circles", "mayor en los círculos grandes")), ("d", t("always 2", "siempre 2"))]),
     ("E", t("A plate has a diameter of 9 in. Its circumference is… (π ≈ 3.14)", "Un plato tiene un diámetro de 9 in. Su circunferencia mide… (π ≈ 3.14)"), [("a", "28.26 in"), ("b", "14.13 in"), ("c", "63.59 in"), ("d", "4.5 in")]),
     ("F", t("A round fountain has a radius of 4 ft. How long is its edge? (π ≈ 3.14)", "Una fuente redonda tiene un radio de 4 ft. ¿Cuánto mide su borde? (π ≈ 3.14)"), [("a", "12.56 ft"), ("b", "50.24 ft"), ("c", "25.12 ft"), ("d", "8 ft")]),
     ("G", t("A track has a circumference of 314 ft. Its radius is… (π ≈ 3.14)", "Una pista tiene una circunferencia de 314 ft. Su radio mide… (π ≈ 3.14)"), [("a", "100 ft"), ("b", "50 ft"), ("c", "25 ft"), ("d", "157 ft")]),
     ("H", t("A round garden has a radius of 7 ft. How much fencing goes around it? (π ≈ 22/7)", "Un jardín redondo tiene un radio de 7 ft. ¿Cuánta cerca lo rodea? (π ≈ 22/7)"), [("a", "22 ft"), ("b", "154 ft"), ("c", "88 ft"), ("d", "44 ft")])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("A new figure: the circle. Its parts, the discovery of π, the formulas C = πd and C = 2πr, and how to find the radius from the circumference.", "Una figura nueva: el círculo. Sus partes, el descubrimiento de π, las fórmulas C = πd y C = 2πr, y cómo hallar el radio a partir de la circunferencia."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Name</strong> the parts of a circle: center, radius, diameter, and circumference.", "<strong>Distinguir</strong> las partes de un círculo: centro, radio, diámetro y circunferencia."),
         t("<strong>Use</strong> the relationship d = 2r between diameter and radius.", "<strong>Reconocer</strong> la relación d = 2r entre el diámetro y el radio."),
         t("<strong>Discover</strong> π as the constant ratio of the circumference to the diameter.", "<strong>Descubrir</strong> π como la razón constante entre la circunferencia y el diámetro."),
         t("<strong>Find</strong> the circumference with C = πd or C = 2πr.", "<strong>Calcular</strong> la circunferencia con C = πd o C = 2πr."),
         t("<strong>Solve</strong> reverse problems: find the radius or the diameter from the circumference.", "<strong>Resolver</strong> problemas inversos: hallar el radio o el diámetro a partir de la circunferencia.")],
        secciones,
        (t("Find the circumference in four problems given the radius and four given the diameter. Find the radius or the diameter in three problems given the circumference. Solve three real problems (a round garden, a tire, a plate).",
           "Calcule la circunferencia en cuatro ejercicios dado el radio y en cuatro dado el diámetro. Halle el radio o el diámetro en tres ejercicios dada la circunferencia. Resuelva tres aplicaciones reales (un jardín redondo, una llanta, un plato)."),
         t("Find three round objects at home (a plate, a can, a lid). Measure the edge with a string and the diameter with a ruler, in inches. Divide C ÷ d for each one. How close do you get to 3.14?",
           "Busque tres objetos redondos en casa (un plato, una lata, una tapa). Mida el borde con una cuerda y el diámetro con una regla, en pulgadas. Divida C ÷ d en cada uno. ¿Qué tan cerca queda de 3.14?")),
        quiz,
        t("Self-check checklist for the circumference", "Lista de autoevaluación de la circunferencia"),
        t("Self-check checklist: skills for the circumference of a circle", "Lista de autoevaluación: destrezas de la circunferencia del círculo"),
        [(t("Parts of the circle", "Partes del círculo"), t("I name the center, radius, diameter, and circumference and explain d = 2r on my own.", "Identifico el centro, el radio, el diámetro y la circunferencia, y explico d = 2r sin ayuda."), t("I tell the terms apart with some help.", "Distingo los términos con algo de apoyo."), t("I mix up the radius and the diameter.", "Confundo el radio con el diámetro.")),
         (t("Use the formulas", "Aplicar las fórmulas"), t("I use C = πd or C = 2πr depending on the data and choose the easier one.", "Aplico C = πd o C = 2πr según el dato y elijo la más cómoda."), t("I use one formula with help.", "Aplico una fórmula con apoyo."), t("I do not know which formula to use.", "No reconozco qué fórmula usar.")),
         (t("Reverse problems and real uses", "Problemas inversos y aplicaciones"), t("I solve for the radius, check by working backward, and explain the result.", "Despejo el radio, compruebo calculando hacia atrás y explico el resultado."), t("I solve for the radius with help.", "Despejo el radio con apoyo."), t("I cannot find the radius from the circumference.", "No despejo el radio a partir de la circunferencia."))],
        t("<p>This lesson added a new figure: the <strong>circle</strong>. You learned its parts (center, radius, diameter, circumference), the relationship d = 2r, and, above all, you discovered π as a universal constant: the circumference ÷ diameter of any circle. With C = πd or C = 2πr you can already find the edge of gardens, fountains, and tracks.</p>\n<p>In <strong>Lesson 7.3 · Area of a circle and figures with semicircles</strong> you will measure not the edge of the circle but its <strong>inside surface</strong>. A new formula appears, A = πr², and circles combine with rectangles in real composite figures, like a running track.</p>",
          "<p>En esta lección se incorporó una figura nueva: el <strong>círculo</strong>. Quedaron claras sus partes (centro, radio, diámetro, circunferencia), la relación d = 2r y, sobre todo, se descubrió π como una constante universal: la razón circunferencia ÷ diámetro de cualquier círculo. Con C = πd o C = 2πr ya se calcula el borde de jardines, fuentes y pistas.</p>\n<p>En la <strong>Lección 7.3 · Área del círculo y figuras compuestas con semicírculos</strong> se medirá no el borde del círculo, sino su <strong>superficie interior</strong>. Aparecerá una nueva fórmula, A = πr², y se combinarán círculos con rectángulos en figuras compuestas reales, como una pista de atletismo.</p>"),
        ("7-3", ("", t("Lesson 7.3 · Area of a circle and figures with semicircles", "Lección 7.3 · Área del círculo y figuras compuestas con semicírculos"))),
        [(t("radius (r)", "radio (r)"), t("The distance from the center to the edge of a circle.", "La distancia del centro al borde del círculo.")),
         (t("diameter (d)", "diámetro (d)"), t("The segment across the circle through the center: d = 2r.", "El segmento que atraviesa el círculo por el centro: d = 2r.")),
         (t("circumference (C)", "circunferencia (C)"), t("The length of the edge of a circle: C = πd.", "La longitud del borde del círculo: C = πd.")),
         ("π (pi)", t("The ratio C ÷ d of any circle, about 3.14.", "La razón C ÷ d de cualquier círculo, unos 3.14."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "anVoz": "Circle with radius {r} and diameter {d}.", "anSal": "Radius (red): {r}. Diameter (blue): 2 × {r} = {d}. The edge is the circumference: C ≈ 3.14 × {d} = {C}.",
  "an1Q": "A circle has a radius of {v}. How long is its diameter?", "an1P": "It is the other way: the diameter is twice the radius.", "an1S": "d = 2 × {v} = {d}.", "an1M": "The diameter is twice the radius: {d}.",
  "an2Q": "A circle has a diameter of {d}. How long is its radius?", "an2P": "It is the other way: the radius is half the diameter.", "an2S": "r = {d} ÷ 2 = {v}.", "an2M": "The radius is half the diameter: {v}.",
  "an3": [["the distance from the center to any point on the edge", "r"], ["the segment across the circle through the center", "d"], ["the length of the edge of the circle", "c"], ["the point that is the same distance from the whole edge", "o"]],
  "an3Q": "What is the name of {x}?", "nomP": {"r": "The radius", "d": "The diameter", "c": "The circumference", "o": "The center"}, "an3M": "It is {x}.",
  "piVoz": "The edge of the wheel, stretched out, is about 3.14 times its diameter.", "piSal": "C ÷ d = {C} ÷ {d} ≈ 3.14. Three whole diameters fit, plus a small piece (yellow) of 0.14 diameter.",
  "foD": "With the diameter: C = π × d ≈ 3.14 × {v}", "foR": "With the radius: C = 2 × π × r ≈ 2 × 3.14 × {v}",
  "ctx": ["a circle", "a pizza", "a round table", "a wall clock", "a round pool"], "cQ": "Find the circumference of {c} with a {t} of {v} in.", "diam": "diameter", "radio": "radius",
  "cS": "{f} ≈ {x} in (or {k}π).", "cP1": "With the diameter, C = π × d: do not divide by 2.", "cP2": "With the radius use C = 2 × π × r: multiply by 2 too.", "cP3": "That is π × r², the area. The circumference is 2 × π × r.",
  "ivCtx": ["The edge of a round table is", "The fence around a round garden is", "One lap of a circular track is", "The edge of a plate is"], "ivQ": "{c} {C} in long. How long is its {t}? (π ≈ 3.14)",
  "ivSd": "d = {C} ÷ 3.14 = {x}.", "ivSr": "r = {C} ÷ (2 × 3.14) = {C} ÷ 6.28 = {x}.", "ivPd": "That is the radius. The diameter is C ÷ π.", "ivPr": "That is the diameter. For the radius, divide by 2π.", "ivPm": "You multiplied instead of dividing.",
  "ap1": "A bicycle wheel has a diameter of {d} inches. How many inches does it roll in {n} turns? (π ≈ 3.14)", "ap1S": "One turn: 3.14 × {d} = {u}; in {n} turns: × {n} ≈ {x} in.",
  "ap2": "You want to fence a round garden with a radius of {r} ft. How many feet of fencing do you need? (π ≈ 3.14)", "ap2S": "C = 2 × 3.14 × {r} ≈ {x} ft.",
  "ap3": "A circular track has a radius of {r} ft. If a runner does {v} laps, how many feet does she run? (π ≈ 3.14)", "ap3S": "One lap: 2 × 3.14 × {r} = {u} ft; × {v} ≈ {x} ft.",
  "ap4": "You want to put ribbon around the edge of a round cake {d} inches across. How many inches of ribbon do you need? (π ≈ 3.14)", "ap4S": "C = 3.14 × {d} ≈ {x} in.",
  "apP": "Check whether the data is the radius or the diameter."
 },
 "es": {
  "anVoz": "Círculo de radio {r} y diámetro {d}.", "anSal": "Radio (rojo): {r}. Diámetro (azul): 2 × {r} = {d}. El borde es la circunferencia: C ≈ 3.14 × {d} = {C}.",
  "an1Q": "Un círculo tiene un radio de {v}. ¿Cuánto mide su diámetro?", "an1P": "Es al revés: el diámetro es el doble del radio.", "an1S": "d = 2 × {v} = {d}.", "an1M": "El diámetro es el doble del radio: {d}.",
  "an2Q": "Un círculo tiene un diámetro de {d}. ¿Cuánto mide su radio?", "an2P": "Es al revés: el radio es la mitad del diámetro.", "an2S": "r = {d} ÷ 2 = {v}.", "an2M": "El radio es la mitad del diámetro: {v}.",
  "an3": [["la distancia del centro a cualquier punto del borde", "r"], ["el segmento que atraviesa el círculo pasando por el centro", "d"], ["la longitud del borde del círculo", "c"], ["el punto que está a la misma distancia de todo el borde", "o"]],
  "an3Q": "¿Cómo se llama {x}?", "nomP": {"r": "El radio", "d": "El diámetro", "c": "La circunferencia", "o": "El centro"}, "an3M": "Es {x}.",
  "piVoz": "El borde de la rueda, estirado, mide unas 3.14 veces su diámetro.", "piSal": "C ÷ d = {C} ÷ {d} ≈ 3.14. Caben 3 diámetros completos y un pedacito (en amarillo) de 0.14 diámetros.",
  "foD": "Con el diámetro: C = π × d ≈ 3.14 × {v}", "foR": "Con el radio: C = 2 × π × r ≈ 2 × 3.14 × {v}",
  "ctx": ["un círculo", "una pizza", "una mesa redonda", "un reloj de pared", "una piscina redonda"], "cQ": "Calcule la circunferencia de {c} con un {t} de {v} in.", "diam": "diámetro", "radio": "radio",
  "cS": "{f} ≈ {x} in (o {k}π).", "cP1": "Con el diámetro, C = π × d: no se divide entre 2.", "cP2": "Con el radio se usa C = 2 × π × r: falta multiplicar por 2.", "cP3": "Eso es π × r², el área. La circunferencia es 2 × π × r.",
  "ivCtx": ["El borde de una mesa redonda mide", "La cerca que rodea un jardín redondo mide", "Una vuelta a una pista circular mide", "El contorno de un plato mide"], "ivQ": "{c} {C} in. ¿Cuánto mide su {t}? (π ≈ 3.14)",
  "ivSd": "d = {C} ÷ 3.14 = {x}.", "ivSr": "r = {C} ÷ (2 × 3.14) = {C} ÷ 6.28 = {x}.", "ivPd": "Ese es el radio. El diámetro es C ÷ π.", "ivPr": "Ese es el diámetro. Para el radio se divide entre 2π.", "ivPm": "Se multiplicó en vez de dividir.",
  "ap1": "Una rueda de bicicleta tiene un diámetro de {d} pulgadas. ¿Cuántas pulgadas avanza en {n} vueltas? (π ≈ 3.14)", "ap1S": "Una vuelta: 3.14 × {d} = {u}; en {n} vueltas: × {n} ≈ {x} in.",
  "ap2": "Se quiere cercar un jardín redondo de {r} ft de radio. ¿Cuántos pies de cerca hacen falta? (π ≈ 3.14)", "ap2S": "C = 2 × 3.14 × {r} ≈ {x} ft.",
  "ap3": "Una pista circular tiene {r} ft de radio. Si una corredora da {v} vueltas, ¿cuántos pies recorre? (π ≈ 3.14)", "ap3S": "Una vuelta: 2 × 3.14 × {r} = {u} ft; × {v} ≈ {x} ft.",
  "ap4": "Se quiere poner un listón alrededor del borde de un pastel redondo de {d} pulgadas de diámetro. ¿Cuántas pulgadas de listón hacen falta? (π ≈ 3.14)", "ap4S": "C = 3.14 × {d} ≈ {x} in.",
  "apP": "Revise si el dato es el radio o el diámetro."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }

/* ============ MODULE 1 · parts of the circle ============ */
function circSVG(r){
  var R = Math.min(120, 24 * r), cx = 320, cy = 150, a = rad(55), px = cx + R * Math.cos(a), py = cy - R * Math.sin(a);
  var s = '<svg class="figura" viewBox="0 0 640 300" role="img" aria-label="' + F(TXT.anVoz, { r: r, d: 2 * r }) + '">';
  s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="#eceff1" stroke="#37474f" stroke-width="4"/>';
  s += linea([cx - R, cy], [cx + R, cy], "#0d47a1", 3) + '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#222"/>' + textoA([cx - 12, cy - 14], "O", 16, "#222");
  s += linea([cx, cy], [px, py], "#b71c1c", 3) + textoA([(cx + px) / 2 - 10, (cy + py) / 2 - 10], "r = " + r, 16, "#b71c1c", 700, "end");
  s += textoA([cx, cy + 22], "d = " + (2 * r), 16, "#0d47a1") + textoA([cx + R * 0.72 + 14, cy + R * 0.72 + 14], "C", 18, "#37474f", 700, "start");
  return s + '</svg>';
}
function pintaAN(){ var r = +$("an-r").value; $("an-rv").textContent = r; $("an-svg").innerHTML = circSVG(r); $("an-salida").innerHTML = '<div class="linea">' + F(TXT.anSal, { r: r, d: 2 * r, C: nd(r2(3.14 * 2 * r)) }) + '</div>'; }
function genAnat(){
  var tp = aleatorio(1, 3), v = aleatorio(2, 40), pc = {};
  if (tp === 1){ var o = baraja([2 * v, v / 2, v, r2(v * 3.14)]).map(function(x){ return { html: nd(x), clave: "n" + x }; }); pc["n" + v / 2] = TXT.an1P;
    return { enun: F(TXT.an1Q, { v: v }), opciones: o, correcta: "n" + 2 * v, pistas: pc, bien: F(TXT.an1S, { v: v, d: 2 * v }), mal: F(TXT.an1M, { d: 2 * v }) }; }
  if (tp === 2){ var d = 2 * v, o2 = baraja([v, 2 * d, d, d / 4]).map(function(x){ return { html: nd(x), clave: "n" + x }; }); pc["n" + 2 * d] = TXT.an2P;
    return { enun: F(TXT.an2Q, { d: d }), opciones: o2, correcta: "n" + v, pistas: pc, bien: F(TXT.an2S, { d: d, v: v }), mal: F(TXT.an2M, { v: v }) }; }
  var q = elige(TXT.an3);
  return { enun: F(TXT.an3Q, { x: q[0] }), opciones: ["r", "d", "c", "o"].map(function(k){ return { html: TXT.nomP[k], clave: k }; }), correcta: q[1], enOrden: true, bien: TXT.nomP[q[1]] + ".", mal: F(TXT.an3M, { x: TXT.nomP[q[1]].toLowerCase() }) };
}

/* ============ MODULE 2 · the discovery of π ============ */
function pintaPI(){
  var d = +$("pi-d").value, u = 44, C = Math.PI * d, R = d * u / 2, cx = 30 + R, cy = 40 + R, y = cy + R + 30;
  $("pi-dv").textContent = nd(d);
  var s = '<svg class="figura" viewBox="0 0 ' + f1(Math.max(640, 80 + C * u)) + ' ' + f1(y + 60) + '" role="img" aria-label="' + TXT.piVoz + '">';
  s += '<circle cx="' + f1(cx) + '" cy="' + f1(cy) + '" r="' + f1(R) + '" fill="#eceff1" stroke="#37474f" stroke-width="4"/>' + linea([cx - R, cy], [cx + R, cy], "#0d47a1", 3);
  s += linea([30, y], [30 + C * u, y], "#37474f", 6);
  for (var k = 0; k < 3; k++) s += '<rect x="' + f1(30 + k * d * u) + '" y="' + (y + 10) + '" width="' + f1(d * u) + '" height="14" fill="' + (k % 2 ? "#90caf9" : "#0d47a1") + '"/>' + textoA([30 + (k + 0.5) * d * u, y + 40], "d", 15, "#0d47a1");
  s += '<rect x="' + f1(30 + 3 * d * u) + '" y="' + (y + 10) + '" width="' + f1(0.14159 * d * u) + '" height="14" fill="#f9a825"/>' + textoA([30 + C * u + 8, y], "C", 16, "#37474f", 700, "start");
  $("pi-svg").innerHTML = s + '</svg>';
  $("pi-salida").innerHTML = '<div class="linea">' + F(TXT.piSal, { C: nd(r2(C)), d: nd(d) }) + '</div>';
}

/* ============ MODULE 3 · the two formulas ============ */
function pintaFO(){
  var tp = $("fo-t").value, v = +$("fo-v").value, d = tp === "d" ? v : 2 * v;
  $("fo-vv").textContent = v;
  $("fo-salida").innerHTML = '<div class="linea">' + F(tp === "d" ? TXT.foD : TXT.foR, { v: v }) + ' ≈ <strong>' + nd(r2(3.14 * d)) + '</strong></div><div class="linea veredicto">C = ' + d + 'π ≈ ' + nd(r2(3.14 * d)) + '</div>';
}
function genC(){
  var conD = Math.random() < 0.5, v = aleatorio(2, 40), d = conD ? v : 2 * v;
  var f = conD ? "C = 3.14 × " + v : "C = 2 × 3.14 × " + v;
  return { enun: F(TXT.cQ, { c: elige(TXT.ctx), t: conD ? TXT.diam : TXT.radio, v: v }), correcta: nd(r2(3.14 * d)), solucion: F(TXT.cS, { f: f, x: nd(r2(3.14 * d)), k: d }),
    evalua: evaluaPiK(d, conD ? [{ k: d / 2, msg: TXT.cP1 }] : [{ k: v, msg: TXT.cP2 }, { k: v * v, msg: TXT.cP3 }].filter(function(x){ return x.k !== d; })) };
}

/* ============ MODULE 4 · from the circumference to the radius ============ */
function genInv(){
  var r = aleatorio(3, 40), C = r2(2 * 3.14 * r), pideD = Math.random() < 0.4, res = pideD ? 2 * r : r, o = { c: elige(TXT.ivCtx), C: nd(C), t: pideD ? TXT.diam : TXT.radio, x: res };
  var p = pideD ? [{ v: r, msg: TXT.ivPd }] : [{ v: 2 * r, msg: TXT.ivPr }, { v: r2(C * 3.14), msg: TXT.ivPm }];
  return { enun: F(TXT.ivQ, o), correcta: String(res), solucion: F(pideD ? TXT.ivSd : TXT.ivSr, o), evalua: evaluaInvPi(res, pideD ? C / Math.PI : C / (2 * Math.PI), p) };
}

/* ============ MODULE 5 · real uses ============ */
function genApl(){
  var tp = aleatorio(1, 4), enun, sol, k;
  if (tp === 1){ var d = elige([20, 24, 26, 28]), n = aleatorio(10, 100); k = d * n; enun = F(TXT.ap1, { d: d, n: n }); sol = F(TXT.ap1S, { d: d, n: n, u: nd(r2(3.14 * d)), x: nd(r2(3.14 * k)) }); }
  else if (tp === 2){ var r = aleatorio(3, 20); k = 2 * r; enun = F(TXT.ap2, { r: r }); sol = F(TXT.ap2S, { r: r, x: nd(r2(3.14 * k)) }); }
  else if (tp === 3){ var rp = 10 * aleatorio(5, 20), v = aleatorio(2, 6); k = 2 * rp * v; enun = F(TXT.ap3, { r: rp, v: v }); sol = F(TXT.ap3S, { r: rp, v: v, u: nd(r2(6.28 * rp)), x: nd(r2(3.14 * k)) }); }
  else { var dm = aleatorio(6, 18); k = dm; enun = F(TXT.ap4, { d: dm }); sol = F(TXT.ap4S, { d: dm, x: nd(r2(3.14 * dm)) }); }
  return { enun: enun, correcta: nd(r2(3.14 * k)), solucion: sol, evalua: evaluaPiK(k, [{ k: k / 2, msg: TXT.apP }, { k: k * 2, msg: TXT.apP }]) };
}

/* ============ Start ============ */
$("an-r").addEventListener("input", pintaAN); pintaAN();
creaPracticaOM("p1", genAnat);
$("pi-d").addEventListener("input", pintaPI); pintaPI();
$("fo-t").addEventListener("change", pintaFO); $("fo-v").addEventListener("input", pintaFO); pintaFO();
creaPracticaLibre("p2", genC);
creaPracticaLibre("p3", genInv);
creaPracticaLibre("p4", genApl);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA_PI = ("Use π ≈ 3.14 and round to two decimal places, or write the answer in terms of π, like 14π.", "Use π ≈ 3.14 y redondee a dos decimales, o escriba el resultado en términos de π, como 14π.")
NOTA_2 = ("Use π ≈ 3.14 and round to two decimal places if needed.", "Use π ≈ 3.14 y redondee a dos decimales si hace falta.")

def practica_pagina():
    n = N
    mods = [
     (t("anatomy", "anatomia"), t("The parts of a circle", "Las partes del círculo"),
      f'''      <p>{t("The center is the same distance from every point on the edge. That distance is the <strong>radius</strong> (r). The <strong>diameter</strong> (d) goes across the circle through the center: it is twice the radius. The <strong>circumference</strong> (C) is the length of the edge, the “perimeter” of the circle.", "El centro está a la misma distancia de todos los puntos del borde. Esa distancia es el <strong>radio</strong> (r). El <strong>diámetro</strong> (d) atraviesa el círculo pasando por el centro: es el doble del radio. La <strong>circunferencia</strong> (C) es la longitud del borde, el «perímetro» del círculo.")}</p>
      <div class="formula">d = 2 × r &nbsp;&nbsp;&nbsp; r = d ÷ 2</div>
      <h3>{t("Move the radius", "Mueva el radio")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="an-r">{t("Radius", "Radio")}: <span id="an-rv"></span></label><input type="range" id="an-r" min="1" max="12" value="5"></div></div>
        <div id="an-svg"></div>
        <div class="salida" id="an-salida" aria-live="polite"></div>
      </div>
{B.om("p1", t("Practice: parts of the circle", "Practique: partes del círculo"))}'''),
     (t("pi", "pi"), t("The discovery of π", "El descubrimiento de π"),
      f'''      <p>{t("If you measure the edge of any round object and divide it by its diameter, you always get <strong>the same number</strong>, a little more than 3. That number is <strong>π</strong> (pi): π ≈ 3.14159. In calculations we use π ≈ 3.14.", "Si se mide el borde de cualquier objeto redondo y se divide entre su diámetro, siempre sale <strong>el mismo número</strong>, un poco más de 3. Ese número es <strong>π</strong> (pi): π ≈ 3.14159. En los cálculos se usa π ≈ 3.14.")}</p>
      <table class="reglas">
        <caption>{t("The ratio C ÷ d in real objects", "La razón C ÷ d en objetos reales")}</caption>
        <thead><tr><th scope="col">{t("Object", "Objeto")}</th><th scope="col">{t("Diameter (in)", "Diámetro (in)")}</th><th scope="col">{t("Circumference (in)", "Circunferencia (in)")}</th><th scope="col">C ÷ d</th></tr></thead>
        <tbody>
          <tr><td>{t("Quarter (coin)", "Moneda de 25 centavos")}</td><td>0.955</td><td>3.00</td><td>≈ 3.14</td></tr>
          <tr><td>{t("Dinner plate", "Plato")}</td><td>10</td><td>31.42</td><td>≈ 3.14</td></tr>
          <tr><td>{t("Soda can", "Lata de refresco")}</td><td>2.6</td><td>8.17</td><td>≈ 3.14</td></tr>
          <tr><td>{t("Car tire", "Llanta de carro")}</td><td>26</td><td>81.68</td><td>≈ 3.14</td></tr>
        </tbody>
      </table>
      <h3>{t("Unroll the edge", "Desenrolle el borde")}</h3>
      <p>{t("The edge of the wheel, stretched into a straight line, is <strong>a little more than three diameters</strong>.", "El borde de la rueda, estirado en línea recta, mide <strong>un poco más de tres diámetros</strong>.")}</p>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="pi-d">{t("Diameter", "Diámetro")}: <span id="pi-dv"></span></label><input type="range" id="pi-d" min="2" max="8" step="0.5" value="4"></div></div>
        <div id="pi-svg"></div>
        <div class="salida" id="pi-salida" aria-live="polite"></div>
      </div>'''),
     (t("formulas", "formulas"), t("The two circumference formulas", "Las dos fórmulas de la circunferencia"),
      f'''      <div class="formula">C = π × d &nbsp;&nbsp;&nbsp; C = 2 × π × r</div>
      <p>{t("They are the same formula; choose based on the data you have. The result with π ≈ 3.14 is approximate (≈). If an exact answer is asked for, leave it “in terms of π”: C = 14π.", "Las dos son la misma fórmula; se elige según el dato que se tenga. El resultado con π ≈ 3.14 es aproximado (≈). Si se pide exacto, se deja «en términos de π»: C = 14π.")}</p>
      <h3>{t("Calculator", "Calculadora")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="fo-t">{t("Known value", "Dato conocido")}</label><select id="fo-t"><option value="d">{t("the diameter", "el diámetro")}</option><option value="r">{t("the radius", "el radio")}</option></select></div>
          <div class="campo" style="flex:1;min-width:180px;"><label for="fo-v">{t("Value", "Valor")}: <span id="fo-vv"></span></label><input type="range" id="fo-v" min="1" max="60" value="14"></div>
        </div>
        <div class="salida" id="fo-salida" aria-live="polite"></div>
      </div>
{libre_x("p2", t("Practice: find the circumference", "Practique: calcule la circunferencia"), t("Circumference", "Circunferencia"), t(*NOTA_PI))}'''),
     (t("solve-for-radius", "hallar-radio"), t("Finding the radius or the diameter", "Hallar el radio o el diámetro"),
      f'''      <p>{t("If you know the circumference, solve the formula: the diameter is C ÷ π, and the radius is C ÷ (2π).", "Si se conoce la circunferencia, se despeja: el diámetro es C ÷ π, y el radio es C ÷ (2π).")}</p>
      <div class="formula">d = C ÷ π &nbsp;&nbsp;&nbsp; r = C ÷ (2π)</div>
      <div class="caja-tip"><strong>{t("Example:", "Ejemplo:")}</strong> {t("the edge of a round table is 188.4 in. r = 188.4 ÷ (2 × 3.14) = 188.4 ÷ 6.28 = 30 in.", "el borde de una mesa redonda mide 188.4 in. r = 188.4 ÷ (2 × 3.14) = 188.4 ÷ 6.28 = 30 in.")}</div>
{libre_x("p3", t("Practice: from the circumference to the radius", "Practique: de la circunferencia al radio"), t("Answer", "Resultado"), t(*NOTA_2))}'''),
     (t("applications", "aplicaciones"), t("Real uses", "Aplicaciones reales"),
      f'''      <p>{t("A wheel rolls its circumference in each turn. A fence around a round garden measures its circumference. One lap around a circular track is its circumference.", "Una rueda avanza su circunferencia en cada vuelta. Una cerca que rodea un jardín redondo mide su circunferencia. Una vuelta a una pista circular es su circunferencia.")}</p>
{libre_x("p4", t("Practice: circumference problems", "Practique: problemas con circunferencia"), t("Answer", "Resultado"), t(*NOTA_2))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/geometry.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Circunferencia del círculo")
