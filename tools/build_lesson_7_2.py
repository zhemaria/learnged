"""Lesson 7.2 · Perimeter of polygons — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json, math
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "7-2"
AZ, AZC, GR, TXC = "#1565c0", "#e3f2fd", "#37474f", "#1a2330"

def txt(x, y, s, size=17, color=TXC):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="{size}" font-weight="700" fill="{color}">{s}</text>'

def parque():
    """A five-sided park with a path around it."""
    P = [(80, 200), (60, 90), (220, 40), (420, 70), (460, 200)]
    lab = ["4 m", t("6 m", "6 m"), "9 m", "8 m", "12 m"]
    s = [f'<polygon points="{" ".join(f"{x},{y}" for x, y in P)}" fill="#e8f5e9" stroke="{AZ}" stroke-width="5" stroke-dasharray="14 8"/>']
    cx, cy = sum(p[0] for p in P) / 5, sum(p[1] for p in P) / 5
    for i in range(5):
        (x1, y1), (x2, y2) = P[i], P[(i + 1) % 5]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = mx - cx, my - cy; L = math.hypot(dx, dy)
        s.append(txt(mx + dx / L * 26, my + dy / L * 26 + 6, lab[i]))
    return svg("0 0 520 240", t("A park with five sides of 4, 6, 9, 8, and 12 meters. A dashed path goes all the way around it.",
                                "Un parque de cinco lados de 4, 6, 9, 8 y 12 metros. Un camino punteado le da toda la vuelta."), "".join(s), ancho=480)

def rect(l, w, ul, uw, aria):
    k = min(360 / l, 160 / w); W, H = l * k, w * k; x0, y0 = (480 - W) / 2, 30
    s = f'<rect x="{x0:.1f}" y="{y0}" width="{W:.1f}" height="{H:.1f}" fill="{AZC}" stroke="{GR}" stroke-width="3"/>'
    s += txt(x0 + W / 2, y0 + H + 26, ul) + txt(x0 - 34, y0 + H / 2 + 6, uw)
    return svg(f"0 0 480 {H + 72:.0f}", aria, s, ancho=420)

def leccion():
    n = N
    s1 = f'''<p>{t("The <strong>perimeter</strong> is the distance <strong>around</strong> a shape. If you walk all the way around a park, the distance you walk is the perimeter of the park. You need the perimeter to put a fence around a yard, a frame around a picture, or a border around a room.",
"El <strong>perímetro</strong> es la distancia <strong>alrededor</strong> de una figura. Si usted le da toda la vuelta a un parque caminando, la distancia que camina es el perímetro del parque. Se necesita el perímetro para poner una cerca alrededor de un patio, un marco alrededor de un cuadro o un borde alrededor de un cuarto.")}</p>
{parque()}
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>To find the perimeter of any polygon, <strong>add the lengths of all its sides</strong>. The perimeter is a length, so its unit is a unit of length: inches, feet, meters…</p>",
"<p>Para hallar el perímetro de cualquier polígono, <strong>sume las medidas de todos sus lados</strong>. El perímetro es una longitud, así que su unidad es de longitud: pulgadas, pies, metros…</p>"))}
{ejemplo(t("Example: the perimeter of the park", "Ejemplo: el perímetro del parque"),
  [("1", t("List all the sides.", "Anote todos los lados."), "4, 6, 9, 8, 12."),
   ("2", t("Add them.", "Súmelos."), "4 + 6 + 9 + 8 + 12 = 39."),
   ("✓", t("Answer with the unit.", "Responda con la unidad."), t("The perimeter is <strong>39 meters</strong>.", "El perímetro es <strong>39 metros</strong>."))])}
{caja("ojo", t("Watch out! Count every side", "¡Cuidado! Cuente todos los lados"), t("<p>The most common mistake is to forget a side. Put your finger on one corner and go around the shape, adding each side once, until you are back where you started.</p>",
"<p>El error más común es olvidar un lado. Ponga el dedo en una esquina y dé la vuelta a la figura, sumando cada lado una vez, hasta volver a donde empezó.</p>"))}
{enlace(n, t("add-sides", "sumar-lados"), t("add the sides", "sumar los lados"), t("Find the perimeter of shapes with 3 to 6 sides.", "Halle el perímetro de figuras de 3 a 6 lados."))}'''

    s2 = f'''<p>{t("Some shapes have equal sides, so we can multiply instead of adding one by one.", "Algunas figuras tienen lados iguales, así que se puede multiplicar en vez de sumar uno por uno.")}</p>
{rect(12, 8, t("12 ft", "12 pies"), t("8 ft", "8 pies"), t("A rectangle 12 feet long and 8 feet wide.", "Un rectángulo de 12 pies de largo y 8 pies de ancho."))}
{tabla(t("Perimeter shortcuts", "Atajos para el perímetro"), t("Perimeter formulas for rectangles, squares, and regular polygons", "Fórmulas del perímetro de rectángulos, cuadrados y polígonos regulares"),
       [t("Shape", "Figura"), t("Why", "Por qué"), t("Formula", "Fórmula")],
       [[t("rectangle", "rectángulo"), t("2 lengths and 2 widths", "2 largos y 2 anchos"), "P = 2l + 2w"],
        [t("square", "cuadrado"), t("4 equal sides", "4 lados iguales"), "P = 4s"],
        [t("regular polygon (all sides equal)", "polígono regular (todos los lados iguales)"), t("n equal sides", "n lados iguales"), "P = n × s"]], expr_cols=(2,))}
<p>{t("In the formulas, <strong>l</strong> is the length, <strong>w</strong> is the width, and <strong>s</strong> is the side. You will find formulas like these on the GED® formula sheet.",
"En las fórmulas, <strong>l</strong> es el largo (en inglés, <em>length</em>), <strong>w</strong> es el ancho (<em>width</em>) y <strong>s</strong> es el lado (<em>side</em>). Las letras vienen del inglés, como en la hoja de fórmulas del examen de GED®.")}</p>
{ejemplo(t("Example: the rectangle above, 12 ft by 8 ft", "Ejemplo: el rectángulo de arriba, de 12 pies por 8 pies"),
  [("1", t("Use the formula.", "Use la fórmula."), "P = 2 × 12 + 2 × 8."),
   ("2", t("Calculate.", "Calcule."), "24 + 16 = 40."),
   ("✓", t("Check by adding.", "Compruebe sumando."), t("12 + 8 + 12 + 8 = 40 ✓. The perimeter is <strong>40 feet</strong>.", "12 + 8 + 12 + 8 = 40 ✓. El perímetro es <strong>40 pies</strong>."))])}
{practica("p1", t("Practice 1 — A rectangle", "Práctica 1 — Un rectángulo"), t("A rectangle is <strong>15 m</strong> long and <strong>9 m</strong> wide. What is its perimeter?", "Un rectángulo mide <strong>15 m</strong> de largo y <strong>9 m</strong> de ancho. ¿Cuál es su perímetro?"),
          [("a", "24 m"), ("b", "48 m"), ("c", "135 m"), ("d", "33 m")])}
{practica("p2", t("Practice 2 — A regular hexagon", "Práctica 2 — Un hexágono regular"), t("A regular hexagon has sides of <strong>7 inches</strong>. What is its perimeter?", "Un hexágono regular tiene lados de <strong>7 pulgadas</strong>. ¿Cuál es su perímetro?"),
          [("a", t("42 inches", "42 pulgadas")), ("b", t("13 inches", "13 pulgadas")), ("c", t("49 inches", "49 pulgadas")), ("d", t("35 inches", "35 pulgadas"))])}
{enlace(n, t("rectangles", "rectangulos"), t("rectangles, squares, and regular polygons", "rectángulos, cuadrados y polígonos regulares"), t("Use the shortcuts to find the perimeter quickly.", "Use los atajos para hallar el perímetro rápido."))}'''

    s3 = f'''<p>{t("Sometimes you know the perimeter and need a side. Work backward: <strong>subtract</strong> the sides you know, or <strong>divide</strong> when the sides are equal.",
"A veces se conoce el perímetro y se necesita un lado. Trabaje al revés: <strong>reste</strong> los lados que conoce, o <strong>divida</strong> cuando los lados son iguales.")}</p>
{ejemplo(t("Example: a rectangle has a perimeter of 50 ft and a length of 15 ft. What is its width?", "Ejemplo: un rectángulo tiene un perímetro de 50 pies y un largo de 15 pies. ¿Cuánto mide de ancho?"),
  [("1", t("Half the perimeter.", "La mitad del perímetro."), t("One length and one width make half of the way around: 50 ÷ 2 = 25.", "Un largo y un ancho son la mitad de la vuelta: 50 ÷ 2 = 25.")),
   ("2", t("Take away the length.", "Quite el largo."), "25 − 15 = 10."),
   ("✓", t("Check.", "Compruebe."), t("2 × 15 + 2 × 10 = 30 + 20 = 50 ✓. The width is <strong>10 feet</strong>.", "2 × 15 + 2 × 10 = 30 + 20 = 50 ✓. El ancho es <strong>10 pies</strong>."))])}
{ejemplo(t("Example: a square has a perimeter of 36 cm. How long is each side?", "Ejemplo: un cuadrado tiene un perímetro de 36 cm. ¿Cuánto mide cada lado?"),
  [("1", t("4 equal sides.", "4 lados iguales."), "36 ÷ 4 = 9."),
   ("✓", t("Check.", "Compruebe."), t("4 × 9 = 36 ✓. Each side is <strong>9 cm</strong>.", "4 × 9 = 36 ✓. Cada lado mide <strong>9 cm</strong>."))])}
{practica("p3", t("Practice 3 — The missing side", "Práctica 3 — El lado que falta"), t("A rectangle has a perimeter of <strong>40 ft</strong> and a length of <strong>12 ft</strong>. What is its width?", "Un rectángulo tiene un perímetro de <strong>40 pies</strong> y un largo de <strong>12 pies</strong>. ¿Cuánto mide de ancho?"),
          [("a", t("28 ft", "28 pies")), ("b", t("16 ft", "16 pies")), ("c", t("8 ft", "8 pies")), ("d", t("4 ft", "4 pies"))])}
{enlace(n, t("missing-side", "lado-que-falta"), t("find the missing side", "hallar el lado que falta"), t("Work backward from the perimeter.", "Trabaje al revés a partir del perímetro."))}'''

    s4 = f'''<p>{t("Real perimeter problems often have one more step: a gate that does not need fence, a price for each foot, or laps around a field.",
"Los problemas reales de perímetro casi siempre tienen un paso más: una puerta que no lleva cerca, un precio por cada pie, o vueltas alrededor de una cancha.")}</p>
{ejemplo(t("Example: a yard is 30 ft by 20 ft. You will fence it, leaving a 4-ft gate. Fence costs $12 per foot. How much will the fence cost?", "Ejemplo: un patio mide 30 pies por 20 pies. Lo va a cercar, dejando una puerta de 4 pies. La cerca cuesta $12 el pie. ¿Cuánto costará la cerca?"),
  [("1", t("Perimeter.", "Perímetro."), "2 × 30 + 2 × 20 = 100 " + t("ft.", "pies.")),
   ("2", t("Take away the gate.", "Quite la puerta."), "100 − 4 = 96 " + t("ft of fence.", "pies de cerca.")),
   ("3", t("Multiply by the price.", "Multiplique por el precio."), "96 × $12 = $1,152."),
   ("✓", t("Answer.", "Respuesta."), t("The fence will cost <strong>$1,152</strong>.", "La cerca costará <strong>$1,152</strong>."))])}
{caja("ojo", t("Watch out! Perimeter is not area", "¡Cuidado! El perímetro no es el área"), t("<p>The perimeter measures the <strong>border</strong> (fence, frame, baseboard). The area measures the <strong>surface inside</strong> (carpet, paint, grass). You will learn area in Lesson 7.3. If the problem talks about going around, it is perimeter.</p>",
"<p>El perímetro mide el <strong>borde</strong> (cerca, marco, zócalo). El área mide la <strong>superficie de adentro</strong> (alfombra, pintura, césped). Aprenderá el área en la Lección 7.3. Si el problema habla de dar la vuelta, es perímetro.</p>"))}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>The fence: type {T("2")} {T("×")} {T("3")}{T("0")} {T("+")} {T("2")} {T("×")} {T("2")}{T("0")} {T("−")} {T("4")} {T("enter")}. The screen shows 96. Then type {T("×")} {T("1")}{T("2")} {T("enter")}: 1152.</p>""",
f"""<p>La cerca: escriba {T("2")} {T("×")} {T("3")}{T("0")} {T("+")} {T("2")} {T("×")} {T("2")}{T("0")} {T("−")} {T("4")} {T("enter")}. La pantalla muestra 96. Después escriba {T("×")} {T("1")}{T("2")} {T("enter")}: 1152.</p>"""))}
{practica("p4", t("Practice 4 — The cost of a fence", "Práctica 4 — El costo de una cerca"), t("A garden is <strong>20 ft</strong> by <strong>15 ft</strong>. Fence costs <strong>$9 per foot</strong>. How much does it cost to fence the whole garden?", "Un jardín mide <strong>20 pies</strong> por <strong>15 pies</strong>. La cerca cuesta <strong>$9 el pie</strong>. ¿Cuánto cuesta cercar todo el jardín?"),
          [("a", "$300"), ("b", "$2,700"), ("c", "$315"), ("d", "$630")])}
{enlace(n, t("real-life", "vida-real"), t("perimeter in real life", "el perímetro en la vida real"), t("Fences, gates, prices, and laps.", "Cercas, puertas, precios y vueltas."))}'''

    secciones = [("s-" + t("what", "que-es"), t("What is perimeter?", "¿Qué es el perímetro?"), s1),
                 ("s-" + t("shortcuts", "atajos"), t("Shortcuts: rectangles and squares", "Atajos: rectángulos y cuadrados"), s2),
                 ("s-" + t("missing", "falta"), t("Find a missing side", "Hallar un lado que falta"), s3),
                 ("s-" + t("real", "vida-real"), t("Perimeter in real life", "El perímetro en la vida real"), s4)]

    lesson = {"next": t("Lesson 7.3", "Lección 7.3"), "review": t("sections 1, 2, 3, and 4", "las secciones 1, 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("24 is 15 + 9: only two sides. A rectangle has 4 sides.", "24 es 15 + 9: solo dos lados. Un rectángulo tiene 4 lados."), "c": t("135 is 15 × 9. That is the area, not the perimeter.", "135 es 15 × 9. Eso es el área, no el perímetro."), "d": t("33 is 15 + 9 + 9. You forgot one length.", "33 es 15 + 9 + 9. Olvidó un largo.")},
             "right": t("2 × 15 + 2 × 9 = 30 + 18 = 48 m.", "2 × 15 + 2 × 9 = 30 + 18 = 48 m."), "solution": t("P = 2 × 15 + 2 × 9 = 48 m. Check: 15 + 9 + 15 + 9 = 48.", "P = 2 × 15 + 2 × 9 = 48 m. Comprobación: 15 + 9 + 15 + 9 = 48.")},
      "p2": {"ok": "a", "hints": {"b": t("13 is 7 + 6. A hexagon has 6 sides of 7: multiply.", "13 es 7 + 6. Un hexágono tiene 6 lados de 7: multiplique."), "c": t("49 is 7 × 7. A hexagon has 6 sides, not 7.", "49 es 7 × 7. Un hexágono tiene 6 lados, no 7."), "d": t("35 is 5 × 7, a pentagon. A hexagon has 6 sides.", "35 es 5 × 7, un pentágono. Un hexágono tiene 6 lados.")},
             "right": t("6 sides × 7 in = 42 in.", "6 lados × 7 pulgadas = 42 pulgadas."), "solution": t("A regular hexagon has 6 equal sides: 6 × 7 = 42 inches.", "Un hexágono regular tiene 6 lados iguales: 6 × 7 = 42 pulgadas.")},
      "p3": {"ok": "c", "hints": {"a": t("28 is 40 − 12. That still includes the other length and both widths.", "28 es 40 − 12. Eso todavía incluye el otro largo y los dos anchos."), "b": t("16 is 40 − 2 × 12: that is both widths together. Divide by 2.", "16 es 40 − 2 × 12: son los dos anchos juntos. Divida entre 2."), "d": t("Check: 2 × 12 + 2 × 4 = 32, not 40.", "Compruebe: 2 × 12 + 2 × 4 = 32, no 40.")},
             "right": t("40 ÷ 2 = 20, and 20 − 12 = 8 ft.", "40 ÷ 2 = 20, y 20 − 12 = 8 pies."), "solution": t("Half the perimeter is 20 (one length + one width). 20 − 12 = 8 ft. Check: 24 + 16 = 40.", "La mitad del perímetro es 20 (un largo + un ancho). 20 − 12 = 8 pies. Comprobación: 24 + 16 = 40.")},
      "p4": {"ok": "d", "hints": {"a": t("$300 is 20 × 15, the area. Fence goes around: use the perimeter.", "$300 es 20 × 15, el área. La cerca va alrededor: use el perímetro."), "b": t("$2,700 uses the area (300) times $9. Use the perimeter.", "$2,700 usa el área (300) por $9. Use el perímetro."), "c": t("$315 is (20 + 15) × 9, only half of the way around.", "$315 es (20 + 15) × 9, solo la mitad de la vuelta.")},
             "right": t("P = 70 ft, and 70 × $9 = $630.", "P = 70 pies, y 70 × $9 = $630."), "solution": t("Perimeter: 2 × 20 + 2 × 15 = 70 ft. Cost: 70 × $9 = $630.", "Perímetro: 2 × 20 + 2 × 15 = 70 pies. Costo: 70 × $9 = $630.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("12 is 5 + 7. Add all three sides.", "12 es 5 + 7. Sume los tres lados."), "b": t("315 multiplies. The perimeter adds the sides.", "315 multiplica. El perímetro suma los lados."), "d": t("16 is 7 + 9. Add all three sides.", "16 es 7 + 9. Sume los tres lados.")}, "solution": t("5 + 7 + 9 = 21 in.", "5 + 7 + 9 = 21 pulgadas.")},
      "B": {"ok": "d", "hints": {"a": t("14 is 10 + 4: only two sides.", "14 es 10 + 4: solo dos lados."), "b": t("40 is 10 × 4, the area.", "40 es 10 × 4, el área."), "c": t("24 is 10 + 10 + 4: one side is missing.", "24 es 10 + 10 + 4: falta un lado.")}, "solution": t("2 × 10 + 2 × 4 = 28 ft.", "2 × 10 + 2 × 4 = 28 pies.")},
      "C": {"ok": "a", "hints": {"b": t("36 is 6 × 6, the area.", "36 es 6 × 6, el área."), "c": t("12 is 2 × 6: only two sides.", "12 es 2 × 6: solo dos lados."), "d": t("10 is 6 + 4. Multiply the side by 4.", "10 es 6 + 4. Multiplique el lado por 4.")}, "solution": t("4 × 6 = 24 cm.", "4 × 6 = 24 cm.")},
      "D": {"ok": "b", "hints": {"a": t("13 is 8 + 5. Multiply: 5 sides of 8.", "13 es 8 + 5. Multiplique: 5 lados de 8."), "c": t("32 is 4 × 8. A pentagon has 5 sides.", "32 es 4 × 8. Un pentágono tiene 5 lados."), "d": t("48 is 6 × 8. A pentagon has 5 sides.", "48 es 6 × 8. Un pentágono tiene 5 lados.")}, "solution": t("5 × 8 = 40 m.", "5 × 8 = 40 m.")},
      "E": {"ok": "c", "hints": {"a": t("21 is 30 − 9. That still includes the other length and both widths.", "21 es 30 − 9. Eso todavía incluye el otro largo y los dos anchos."), "b": t("12 is 30 − 2 × 9: both widths together. Divide by 2.", "12 es 30 − 2 × 9: los dos anchos juntos. Divida entre 2."), "d": t("Check: 2 × 9 + 2 × 3 = 24, not 30.", "Compruebe: 2 × 9 + 2 × 3 = 24, no 30.")}, "solution": t("30 ÷ 2 = 15, and 15 − 9 = 6 ft.", "30 ÷ 2 = 15, y 15 − 9 = 6 pies.")},
      "F": {"ok": "a", "hints": {"b": t("24 is 48 ÷ 2. A square has 4 equal sides.", "24 es 48 ÷ 2. Un cuadrado tiene 4 lados iguales."), "c": t("192 is 48 × 4. Divide to find one side.", "192 es 48 × 4. Divida para hallar un lado."), "d": t("44 is 48 − 4. Divide by 4.", "44 es 48 − 4. Divida entre 4.")}, "solution": t("48 ÷ 4 = 12 in.", "48 ÷ 4 = 12 pulgadas.")},
      "G": {"ok": "d", "hints": {"a": t("38 ft is the whole perimeter. The gate does not need fence.", "38 pies es todo el perímetro. La puerta no lleva cerca."), "b": t("Take away the gate; do not add it.", "Quite la puerta; no la sume."), "c": t("84 is 12 × 7, the area.", "84 es 12 × 7, el área.")}, "solution": t("P = 2 × 12 + 2 × 7 = 38 ft. Without the gate: 38 − 3 = 35 ft.", "P = 2 × 12 + 2 × 7 = 38 pies. Sin la puerta: 38 − 3 = 35 pies.")},
      "H": {"ok": "b", "hints": {"a": t("Square feet measure area, the surface inside.", "Los pies cuadrados miden área, la superficie de adentro."), "c": t("Cubic feet measure volume, the space inside a box.", "Los pies cúbicos miden volumen, el espacio dentro de una caja."), "d": t("Degrees measure angles.", "Los grados miden ángulos.")}, "solution": t("The perimeter is a length, so it is measured in units of length, like feet.", "El perímetro es una longitud, así que se mide en unidades de longitud, como pies.")}
     }}

    quiz = [
     ("A", t("What is the perimeter of a triangle with sides of <strong>5, 7, and 9 inches</strong>?", "¿Cuál es el perímetro de un triángulo con lados de <strong>5, 7 y 9 pulgadas</strong>?"), [("a", "12 in"), ("b", "315 in"), ("c", "21 in"), ("d", "16 in")]),
     ("B", t("A rectangle is <strong>10 ft</strong> by <strong>4 ft</strong>. What is its perimeter?", "Un rectángulo mide <strong>10 pies</strong> por <strong>4 pies</strong>. ¿Cuál es su perímetro?"), [("a", t("14 ft", "14 pies")), ("b", t("40 ft", "40 pies")), ("c", t("24 ft", "24 pies")), ("d", t("28 ft", "28 pies"))]),
     ("C", t("A square has sides of <strong>6 cm</strong>. What is its perimeter?", "Un cuadrado tiene lados de <strong>6 cm</strong>. ¿Cuál es su perímetro?"), [("a", "24 cm"), ("b", "36 cm"), ("c", "12 cm"), ("d", "10 cm")]),
     ("D", t("A regular pentagon has sides of <strong>8 m</strong>. What is its perimeter?", "Un pentágono regular tiene lados de <strong>8 m</strong>. ¿Cuál es su perímetro?"), [("a", "13 m"), ("b", "40 m"), ("c", "32 m"), ("d", "48 m")]),
     ("E", t("A rectangle has a perimeter of <strong>30 ft</strong> and a length of <strong>9 ft</strong>. What is its width?", "Un rectángulo tiene un perímetro de <strong>30 pies</strong> y un largo de <strong>9 pies</strong>. ¿Cuánto mide de ancho?"), [("a", t("21 ft", "21 pies")), ("b", t("12 ft", "12 pies")), ("c", t("6 ft", "6 pies")), ("d", t("3 ft", "3 pies"))]),
     ("F", t("A square has a perimeter of <strong>48 in</strong>. How long is each side?", "Un cuadrado tiene un perímetro de <strong>48 pulgadas</strong>. ¿Cuánto mide cada lado?"), [("a", "12 in"), ("b", "24 in"), ("c", "192 in"), ("d", "44 in")]),
     ("G", t("A garden is <strong>12 ft</strong> by <strong>7 ft</strong>. You will fence it, leaving a <strong>3-ft</strong> gate. How many feet of fence do you need?", "Un jardín mide <strong>12 pies</strong> por <strong>7 pies</strong>. Lo va a cercar, dejando una puerta de <strong>3 pies</strong>. ¿Cuántos pies de cerca necesita?"), [("a", "38"), ("b", "41"), ("c", "84"), ("d", "35")]),
     ("H", t("Which unit can measure a perimeter?", "¿Qué unidad puede medir un perímetro?"), [("a", t("square feet", "pies cuadrados")), ("b", t("feet", "pies")), ("c", t("cubic feet", "pies cúbicos")), ("d", t("degrees", "grados"))])]

    return B.pagina_leccion(n, 7, t("Geometry", "Geometría"),
        t("Perimeter of polygons", "Perímetro de polígonos"),
        t("Fences, frames, and borders: find the distance around any shape.", "Cercas, marcos y bordes: halle la distancia alrededor de cualquier figura."),
        ("🧱", t("Go all the way around", "Dele toda la vuelta")),
        [t("<strong>Find</strong> the perimeter of a polygon by adding its sides.", "<strong>Hallar</strong> el perímetro de un polígono sumando sus lados."),
         t("<strong>Use</strong> the shortcuts for rectangles, squares, and regular polygons.", "<strong>Usar</strong> los atajos para rectángulos, cuadrados y polígonos regulares."),
         t("<strong>Find</strong> a missing side when you know the perimeter.", "<strong>Hallar</strong> un lado que falta cuando se conoce el perímetro."),
         t("<strong>Solve</strong> real problems with fences, gates, and prices.", "<strong>Resolver</strong> problemas reales con cercas, puertas y precios.")],
        secciones,
        (t("Draw a rectangle, a square, a triangle, and a regular hexagon. Choose and write the length of each side, and find each perimeter. Then draw a rectangle with a perimeter of 30 units and find its missing side.",
           "Dibuje un rectángulo, un cuadrado, un triángulo y un hexágono regular. Elija y escriba la medida de cada lado, y halle cada perímetro. Después dibuje un rectángulo con un perímetro de 30 unidades y halle su lado que falta."),
         t("Measure the perimeter of a table, a door, and a room in your home with a tape measure. Then figure out how many feet of baseboard the room would need, leaving out the door.",
           "Mida con una cinta métrica el perímetro de una mesa, una puerta y un cuarto de su casa. Después calcule cuántos pies de zócalo necesitaría el cuarto, sin contar la puerta.")),
        quiz,
        t("Self-check checklist for perimeter", "Lista de autoevaluación del perímetro"),
        t("Self-check checklist: skills for perimeter", "Lista de autoevaluación: destrezas con el perímetro"),
        [(t("Add the sides", "Sumar los lados"), t("I add every side once, with the right unit.", "Sumo cada lado una vez, con la unidad correcta."), t("I add the sides, but sometimes I miss one.", "Sumo los lados, pero a veces me falta uno."), t("I multiply the sides instead of adding them.", "Multiplico los lados en vez de sumarlos.")),
         (t("Use the shortcuts", "Usar los atajos"), t("I use P = 2l + 2w, P = 4s, and P = n × s correctly.", "Uso bien P = 2l + 2w, P = 4s y P = n × s."), t("I use them with some help.", "Los uso con un poco de ayuda."), t("I mix up perimeter and area.", "Confundo el perímetro con el área.")),
         (t("Find a missing side", "Hallar un lado que falta"), t("I work backward from the perimeter and check my answer.", "Trabajo al revés a partir del perímetro y compruebo mi respuesta."), t("I find it for squares, but rectangles are harder.", "Lo hallo en cuadrados, pero en rectángulos me cuesta."), t("I do not know where to start.", "No sé por dónde empezar.")),
         (t("Real problems", "Problemas reales"), t("I solve problems with gates, prices, and laps.", "Resuelvo problemas con puertas, precios y vueltas."), t("I find the perimeter but forget the extra step.", "Hallo el perímetro, pero olvido el paso adicional."), t("I am not sure when a problem asks for perimeter.", "No estoy seguro de cuándo un problema pide el perímetro."))],
        t("<p>You can now find the distance around any polygon and solve real perimeter problems.</p>\n<p>In <strong>Lesson 7.3 · Area of rectangles and triangles</strong> you will measure the surface inside a shape, which is what you need for carpet, paint, or tiles.</p>",
          "<p>Ya sabe hallar la distancia alrededor de cualquier polígono y resolver problemas reales de perímetro.</p>\n<p>En la <strong>Lección 7.3 · Área de rectángulos y triángulos</strong> medirá la superficie de adentro de una figura, que es lo que se necesita para una alfombra, la pintura o las losetas.</p>"),
        ("7-3", ("", t("Lesson 7.3 · Area of rectangles and triangles", "Lección 7.3 · Área de rectángulos y triángulos"))),
        [(t("perimeter", "perímetro"), t("The distance around a shape. For a polygon, the sum of its sides.", "La distancia alrededor de una figura. En un polígono, la suma de sus lados.")),
         (t("length and width", "largo y ancho"), t("The two different sides of a rectangle (l and w in the formulas).", "Los dos lados distintos de un rectángulo (l y w en las fórmulas).")),
         (t("regular polygon", "polígono regular"), t("A polygon with all its sides equal (and all its angles equal).", "Un polígono con todos sus lados iguales (y todos sus ángulos iguales).")),
         (t("formula", "fórmula"), t("A rule written with letters, like P = 4s.", "Una regla escrita con letras, como P = 4s."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "uu": {"in": "inches", "ft": "feet", "yd": "yards", "m": "meters", "cm": "centimeters"},
  "ab": {"in": "in", "ft": "ft", "yd": "yd", "m": "m", "cm": "cm"},
  "pregSuma": "What is the perimeter of this shape? The sides are in <strong>{u}</strong>.",
  "ariaPoli": "A shape with {n} sides of {lados} {u}. Not drawn to scale.",
  "y": "and",
  "solSuma": "Add all the sides: {suma} = <strong>{p}</strong> {u}.",
  "olvido": "You missed a side. Go all the way around and add each side once.",
  "pistaSuma": "Add the lengths of all the sides.",
  "escala": "Not drawn to scale.",
  "pregRect": "A rectangle is <strong>{l} {u}</strong> long and <strong>{w} {u}</strong> wide. What is its perimeter?",
  "pregCuad": "A square has sides of <strong>{s} {u}</strong>. What is its perimeter?",
  "pregReg": "A regular {nom} has sides of <strong>{s} {u}</strong>. What is its perimeter?",
  "polN": {"3": ["triangle", 3], "5": ["pentagon", 5], "6": ["hexagon", 6], "8": ["octagon", 8]},
  "solRect": "P = 2 × {l} + 2 × {w} = {a} + {b} = <strong>{p}</strong> {u}.",
  "solCuad": "P = 4 × {s} = <strong>{p}</strong> {u}.",
  "solReg": "A regular {nom} has {n} equal sides: {n} × {s} = <strong>{p}</strong> {u}.",
  "area": "That is the area (the surface inside), not the perimeter.",
  "dosLados": "You added only two sides. Go all the way around.",
  "sumaN": "Multiply the side by the number of sides; do not add them.",
  "pistaRect": "Use the shortcut: P = 2l + 2w, P = 4s, or P = n × s.",
  "pregFaltaR": "A rectangle has a perimeter of <strong>{P} {u}</strong> and a length of <strong>{l} {u}</strong>. What is its width?",
  "pregFaltaC": "A square has a perimeter of <strong>{P} {u}</strong>. How long is each side?",
  "pregFaltaT": "A triangle has a perimeter of <strong>{P} {u}</strong>. Two sides are <strong>{a} {u}</strong> and <strong>{b} {u}</strong>. How long is the third side?",
  "solFaltaR": "Half the perimeter is {P} ÷ 2 = {h} (one length + one width). {h} − {l} = <strong>{w}</strong> {u}.",
  "solFaltaC": "4 equal sides: {P} ÷ 4 = <strong>{s}</strong> {u}.",
  "solFaltaT": "Take away the sides you know: {P} − {a} − {b} = <strong>{c}</strong> {u}.",
  "dosAnchos": "That is both widths together. Divide by 2.",
  "unLargo": "You took away only one length. Half the perimeter is one length + one width.",
  "mitadC": "A square has 4 equal sides: divide by 4, not by 2.",
  "pistaFalta": "Work backward: subtract the sides you know, or divide when the sides are equal.",
  "pregCerca": "A yard is <strong>{l} ft</strong> by <strong>{w} ft</strong>. You will fence it, leaving a <strong>{g}-ft</strong> gate. How many feet of fence do you need?",
  "solCerca": "P = 2 × {l} + 2 × {w} = {P} ft. Without the gate: {P} − {g} = <strong>{r}</strong> ft.",
  "pregCosto": "A garden is <strong>{l} ft</strong> by <strong>{w} ft</strong>. Fence costs <strong>${c} per foot</strong>. How many dollars does it cost to fence the whole garden?",
  "solCosto": "P = 2 × {l} + 2 × {w} = {P} ft. Cost: {P} × ${c} = $<strong>{r}</strong>.",
  "pregVueltas": "A field is <strong>{l} m</strong> by <strong>{w} m</strong>. Pedro runs around it <strong>{k} times</strong>. How many meters does he run?",
  "solVueltas": "One lap: 2 × {l} + 2 × {w} = {P} m. {k} laps: {k} × {P} = <strong>{r}</strong> m.",
  "puerta": "The gate does not need fence: take it away.",
  "areaR": "You used the area. Fence goes around: use the perimeter.",
  "unaVuelta": "That is one lap. Multiply by the number of laps.",
  "pistaReal": "Find the perimeter first, then do the extra step."
 },
 "es": {
  "uu": {"in": "pulgadas", "ft": "pies", "yd": "yardas", "m": "metros", "cm": "centímetros"},
  "ab": {"in": "pulg", "ft": "pies", "yd": "yd", "m": "m", "cm": "cm"},
  "pregSuma": "¿Cuál es el perímetro de esta figura? Los lados están en <strong>{u}</strong>.",
  "ariaPoli": "Una figura de {n} lados de {lados} {u}. No está dibujada a escala.",
  "y": "y",
  "solSuma": "Sume todos los lados: {suma} = <strong>{p}</strong> {u}.",
  "olvido": "Le faltó un lado. Dé toda la vuelta y sume cada lado una vez.",
  "pistaSuma": "Sume las medidas de todos los lados.",
  "escala": "No está dibujada a escala.",
  "pregRect": "Un rectángulo mide <strong>{l} {u}</strong> de largo y <strong>{w} {u}</strong> de ancho. ¿Cuál es su perímetro?",
  "pregCuad": "Un cuadrado tiene lados de <strong>{s} {u}</strong>. ¿Cuál es su perímetro?",
  "pregReg": "Un {nom} regular tiene lados de <strong>{s} {u}</strong>. ¿Cuál es su perímetro?",
  "polN": {"3": ["triángulo", 3], "5": ["pentágono", 5], "6": ["hexágono", 6], "8": ["octágono", 8]},
  "solRect": "P = 2 × {l} + 2 × {w} = {a} + {b} = <strong>{p}</strong> {u}.",
  "solCuad": "P = 4 × {s} = <strong>{p}</strong> {u}.",
  "solReg": "Un {nom} regular tiene {n} lados iguales: {n} × {s} = <strong>{p}</strong> {u}.",
  "area": "Eso es el área (la superficie de adentro), no el perímetro.",
  "dosLados": "Sumó solo dos lados. Dé toda la vuelta.",
  "sumaN": "Multiplique el lado por la cantidad de lados; no los sume.",
  "pistaRect": "Use el atajo: P = 2l + 2w, P = 4s o P = n × s.",
  "pregFaltaR": "Un rectángulo tiene un perímetro de <strong>{P} {u}</strong> y un largo de <strong>{l} {u}</strong>. ¿Cuánto mide de ancho?",
  "pregFaltaC": "Un cuadrado tiene un perímetro de <strong>{P} {u}</strong>. ¿Cuánto mide cada lado?",
  "pregFaltaT": "Un triángulo tiene un perímetro de <strong>{P} {u}</strong>. Dos lados miden <strong>{a} {u}</strong> y <strong>{b} {u}</strong>. ¿Cuánto mide el tercer lado?",
  "solFaltaR": "La mitad del perímetro es {P} ÷ 2 = {h} (un largo + un ancho). {h} − {l} = <strong>{w}</strong> {u}.",
  "solFaltaC": "4 lados iguales: {P} ÷ 4 = <strong>{s}</strong> {u}.",
  "solFaltaT": "Quite los lados que conoce: {P} − {a} − {b} = <strong>{c}</strong> {u}.",
  "dosAnchos": "Esos son los dos anchos juntos. Divida entre 2.",
  "unLargo": "Quitó solo un largo. La mitad del perímetro es un largo + un ancho.",
  "mitadC": "Un cuadrado tiene 4 lados iguales: divida entre 4, no entre 2.",
  "pistaFalta": "Trabaje al revés: reste los lados que conoce, o divida cuando los lados son iguales.",
  "pregCerca": "Un patio mide <strong>{l} pies</strong> por <strong>{w} pies</strong>. Lo va a cercar, dejando una puerta de <strong>{g} pies</strong>. ¿Cuántos pies de cerca necesita?",
  "solCerca": "P = 2 × {l} + 2 × {w} = {P} pies. Sin la puerta: {P} − {g} = <strong>{r}</strong> pies.",
  "pregCosto": "Un jardín mide <strong>{l} pies</strong> por <strong>{w} pies</strong>. La cerca cuesta <strong>${c} el pie</strong>. ¿Cuántos dólares cuesta cercar todo el jardín?",
  "solCosto": "P = 2 × {l} + 2 × {w} = {P} pies. Costo: {P} × ${c} = $<strong>{r}</strong>.",
  "pregVueltas": "Una cancha mide <strong>{l} m</strong> por <strong>{w} m</strong>. Pedro le da <strong>{k} vueltas</strong> corriendo. ¿Cuántos metros corre?",
  "solVueltas": "Una vuelta: 2 × {l} + 2 × {w} = {P} m. {k} vueltas: {k} × {P} = <strong>{r}</strong> m.",
  "puerta": "La puerta no lleva cerca: quítela.",
  "areaR": "Usó el área. La cerca va alrededor: use el perímetro.",
  "unaVuelta": "Eso es una sola vuelta. Multiplique por la cantidad de vueltas.",
  "pistaReal": "Primero halle el perímetro, y después haga el paso adicional."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
var UN = ["in", "ft", "yd", "m", "cm"];

/* ============ MODULE 1 · add the sides ============ */
function genSuma(){
  var n = aleatorio(3, 6), u = elige(UN), L = [], cx = 150, cy = 115, R = 80, rot = Math.random() * Math.PI, P = [];
  for (var i = 0; i < n; i++){ L.push(aleatorio(3, 25)); var a = rot + 2 * Math.PI * i / n, r = R * (0.85 + Math.random() * 0.2); P.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]); }
  var s = '<polygon points="' + P.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#e3f2fd" stroke="#37474f" stroke-width="3"/>';
  for (i = 0; i < n; i++){ var q = P[i], w = P[(i + 1) % n], mx = (q[0] + w[0]) / 2, my = (q[1] + w[1]) / 2, dx = mx - cx, dy = my - cy, d = Math.sqrt(dx * dx + dy * dy) || 1;
    s += texto([mx + dx / d * 24, my + dy / d * 24], L[i] + " " + TXT.ab[u], 15, "#1a2330"); }
  var p = L.reduce(function(a, b){ return a + b; }, 0), tr = [];
  L.forEach(function(x){ if (p - x !== p) tr.push({ v: p - x, msg: TXT.olvido }); });
  var lados = L.slice(0, -1).join(", ") + " " + TXT.y + " " + L[n - 1];
  var svg = '<svg class="figura" viewBox="0 0 300 230" role="img" aria-label="' + F(TXT.ariaPoli, { n: n, lados: lados, u: TXT.uu[u] }) + '">' + s + '</svg>';
  return { enun: F(TXT.pregSuma, { u: TXT.uu[u] }) + svg + '<span class="nota">' + TXT.escala + '</span>',
    solucion: F(TXT.solSuma, { suma: L.join(" + "), p: p, u: TXT.uu[u] }), evalua: numN(p, tr, TXT.pistaSuma) };
}

/* ============ MODULE 2 · shortcuts ============ */
function genRect(){
  var u = elige(UN), r = Math.random(), tr = [];
  if (r < 0.5){
    var l = aleatorio(6, 30), w = aleatorio(3, l - 1), p = 2 * l + 2 * w;
    tr.push({ v: l * w, msg: TXT.area }); tr.push({ v: l + w, msg: TXT.dosLados }); tr.push({ v: 2 * l + w, msg: TXT.olvido }); tr.push({ v: l + 2 * w, msg: TXT.olvido });
    return { enun: F(TXT.pregRect, { l: l, w: w, u: TXT.uu[u] }), solucion: F(TXT.solRect, { l: l, w: w, a: 2 * l, b: 2 * w, p: p, u: TXT.uu[u] }), evalua: numN(p, tr.filter(function(x){ return x.v !== p; }), TXT.pistaRect) };
  }
  if (r < 0.75){
    var s = aleatorio(3, 25), p2 = 4 * s;
    if (s * s !== p2) tr.push({ v: s * s, msg: TXT.area }); if (2 * s !== p2) tr.push({ v: 2 * s, msg: TXT.dosLados }); if (s + 4 !== p2) tr.push({ v: s + 4, msg: TXT.sumaN });
    return { enun: F(TXT.pregCuad, { s: s, u: TXT.uu[u] }), solucion: F(TXT.solCuad, { s: s, p: p2, u: TXT.uu[u] }), evalua: numN(p2, tr, TXT.pistaRect) };
  }
  var k = elige(["3", "5", "6", "8"]), nm = TXT.polN[k], s3 = aleatorio(3, 20), p3 = nm[1] * s3;
  if (s3 + nm[1] !== p3) tr.push({ v: s3 + nm[1], msg: TXT.sumaN });
  return { enun: F(TXT.pregReg, { nom: nm[0], s: s3, u: TXT.uu[u] }), solucion: F(TXT.solReg, { nom: nm[0], n: nm[1], s: s3, p: p3, u: TXT.uu[u] }), evalua: numN(p3, tr, TXT.pistaRect) };
}

/* ============ MODULE 3 · missing side ============ */
function genFalta(){
  var u = elige(UN), r = Math.random(), tr = [];
  if (r < 0.5){
    var l = aleatorio(6, 30), w = aleatorio(2, l - 1), P = 2 * l + 2 * w;
    tr.push({ v: 2 * w, msg: TXT.dosAnchos }); tr.push({ v: P - l, msg: TXT.unLargo });
    return { enun: F(TXT.pregFaltaR, { P: P, l: l, u: TXT.uu[u] }), solucion: F(TXT.solFaltaR, { P: P, h: l + w, l: l, w: w, u: TXT.uu[u] }), evalua: numN(w, tr.filter(function(x){ return x.v !== w; }), TXT.pistaFalta) };
  }
  if (r < 0.75){
    var s = aleatorio(3, 25), P2 = 4 * s; tr.push({ v: 2 * s, msg: TXT.mitadC });
    return { enun: F(TXT.pregFaltaC, { P: P2, u: TXT.uu[u] }), solucion: F(TXT.solFaltaC, { P: P2, s: s, u: TXT.uu[u] }), evalua: numN(s, tr, TXT.pistaFalta) };
  }
  var a, b, c;
  do { a = aleatorio(4, 20); b = aleatorio(4, 20); c = aleatorio(4, 20); } while (a + b <= c || a + c <= b || b + c <= a);
  var P3 = a + b + c; if (a + b !== c) tr.push({ v: a + b, msg: TXT.pistaFalta });
  return { enun: F(TXT.pregFaltaT, { P: P3, a: a, b: b, u: TXT.uu[u] }), solucion: F(TXT.solFaltaT, { P: P3, a: a, b: b, c: c, u: TXT.uu[u] }), evalua: numN(c, tr, TXT.pistaFalta) };
}

/* ============ MODULE 4 · real life ============ */
function genReal(){
  var r = Math.random(), l = aleatorio(8, 40), w = aleatorio(5, l - 1), P = 2 * l + 2 * w, tr = [];
  if (r < 0.34){
    var g = aleatorio(3, 6), res = P - g; tr.push({ v: P, msg: TXT.puerta }); tr.push({ v: P + g, msg: TXT.puerta }); tr.push({ v: l * w, msg: TXT.areaR });
    return { enun: F(TXT.pregCerca, { l: l, w: w, g: g }), solucion: F(TXT.solCerca, { l: l, w: w, P: P, g: g, r: res }), evalua: numN(res, tr.filter(function(x){ return x.v !== res; }), TXT.pistaReal) };
  }
  if (r < 0.67){
    var c = aleatorio(5, 15), res2 = P * c; tr.push({ v: l * w * c, msg: TXT.areaR }); tr.push({ v: (l + w) * c, msg: TXT.dosLados });
    return { enun: F(TXT.pregCosto, { l: l, w: w, c: c }), solucion: F(TXT.solCosto, { l: l, w: w, P: P, c: c, r: com(res2) }), evalua: numN(res2, tr.filter(function(x){ return x.v !== res2; }), TXT.pistaReal) };
  }
  var L2 = aleatorio(4, 12) * 10, W2 = aleatorio(2, L2 / 10 - 1) * 10, P2 = 2 * L2 + 2 * W2, k = aleatorio(2, 8), res3 = P2 * k;
  tr.push({ v: P2, msg: TXT.unaVuelta }); tr.push({ v: (L2 + W2) * k, msg: TXT.dosLados });
  return { enun: F(TXT.pregVueltas, { l: L2, w: W2, k: k }), solucion: F(TXT.solVueltas, { l: L2, w: W2, P: P2, k: k, r: com(res3) }), evalua: numN(res3, tr.filter(function(x){ return x.v !== res3; }), TXT.pistaReal) };
}

creaPracticaLibre("p1", genSuma);
creaPracticaLibre("p2", genRect);
creaPracticaLibre("p3", genFalta);
creaPracticaLibre("p4", genReal);
'''

def practica_pagina():
    n = N
    mods = [
     (t("add-sides", "sumar-lados"), t("Add the sides", "Sumar los lados"),
      f'''      <p>{t("The perimeter is the distance around: add every side once. Put your finger on a corner and go all the way around.", "El perímetro es la distancia alrededor: sume cada lado una vez. Ponga el dedo en una esquina y dé toda la vuelta.")}</p>
{B.libre("p1", t("Practice: the perimeter", "Practique: el perímetro"), t("Perimeter", "Perímetro"))}'''),
     (t("rectangles", "rectangulos"), t("Rectangles, squares, and regular polygons", "Rectángulos, cuadrados y polígonos regulares"),
      f'''      <table class="reglas">
        <caption>{t("Perimeter shortcuts", "Atajos para el perímetro")}</caption>
        <tbody>
          <tr><td>{t("rectangle", "rectángulo")}</td><td>P = 2l + 2w</td></tr>
          <tr><td>{t("square", "cuadrado")}</td><td>P = 4s</td></tr>
          <tr><td>{t("regular polygon with n sides", "polígono regular de n lados")}</td><td>P = n × s</td></tr>
        </tbody>
      </table>
{B.libre("p2", t("Practice: use the shortcut", "Practique: use el atajo"), t("Perimeter", "Perímetro"))}'''),
     (t("missing-side", "lado-que-falta"), t("Find the missing side", "Hallar el lado que falta"),
      f'''      <p>{t("<strong>Rectangle:</strong> half the perimeter is one length + one width. <strong>Square:</strong> divide the perimeter by 4. <strong>Triangle:</strong> subtract the two sides you know.", "<strong>Rectángulo:</strong> la mitad del perímetro es un largo + un ancho. <strong>Cuadrado:</strong> divida el perímetro entre 4. <strong>Triángulo:</strong> reste los dos lados que conoce.")}</p>
{B.libre("p3", t("Practice: the missing side", "Practique: el lado que falta"), t("Side", "Lado"))}'''),
     (t("real-life", "vida-real"), t("Perimeter in real life", "El perímetro en la vida real"),
      f'''      <p>{t("Find the perimeter first. Then do the extra step: take away a gate, multiply by a price, or multiply by the number of laps.", "Primero halle el perímetro. Después haga el paso adicional: quite una puerta, multiplique por un precio, o multiplique por la cantidad de vueltas.")}</p>
{B.libre("p4", t("Practice: real problems", "Practique: problemas reales"), t("Answer", "Respuesta"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t("Geometry", "Geometría"), t("Perimeter of polygons", "Perímetro de polígonos"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun svg.figura{display:block;width:100%;max-width:320px;height:auto;margin:10px auto;}\n.enun .nota{display:block;text-align:center;font-weight:400;font-size:14px;color:#4a5462;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Perímetro de polígonos")
