"""Lesson 7.3 · Area of rectangles and triangles — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "7-3"
AZ, AZC, GR, TXC = "#1565c0", "#e3f2fd", "#37474f", "#1a2330"

def txt(x, y, s, size=17, color=TXC):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="{size}" font-weight="700" fill="{color}">{s}</text>'

def cuadricula():
    k, x0, y0, l, w = 48, 160, 20, 5, 3
    s = [f'<rect x="{x0}" y="{y0}" width="{l * k}" height="{w * k}" fill="{AZC}" stroke="{GR}" stroke-width="3"/>']
    for i in range(1, l): s.append(f'<line x1="{x0 + i * k}" y1="{y0}" x2="{x0 + i * k}" y2="{y0 + w * k}" stroke="#90a4ae" stroke-width="1.5"/>')
    for j in range(1, w): s.append(f'<line x1="{x0}" y1="{y0 + j * k}" x2="{x0 + l * k}" y2="{y0 + j * k}" stroke="#90a4ae" stroke-width="1.5"/>')
    s.append(txt(x0 + l * k / 2, y0 + w * k + 28, t("5 units", "5 unidades")) + txt(x0 - 66, y0 + w * k / 2 + 6, t("3 units", "3 unidades")))
    return svg("0 0 560 200", t("A rectangle 5 units long and 3 units wide, divided into a grid of 15 equal squares: 3 rows of 5.",
                                "Un rectángulo de 5 unidades de largo y 3 unidades de ancho, dividido en una cuadrícula de 15 cuadritos iguales: 3 filas de 5."), "".join(s), ancho=480)

def triangulo_en_rect():
    x0, y0, W, H = 140, 20, 300, 160
    s = [f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="none" stroke="#90a4ae" stroke-width="2" stroke-dasharray="8 6"/>',
         f'<polygon points="{x0},{y0 + H} {x0 + W},{y0 + H} {x0 + 110},{y0}" fill="{AZC}" stroke="{GR}" stroke-width="3"/>',
         f'<line x1="{x0 + 110}" y1="{y0}" x2="{x0 + 110}" y2="{y0 + H}" stroke="{AZ}" stroke-width="3" stroke-dasharray="6 4"/><rect x="{x0 + 110}" y="{y0 + H - 14}" width="14" height="14" fill="none" stroke="{AZ}" stroke-width="2"/>',
         txt(x0 + W / 2, y0 + H + 28, t("base (b)", "base (b)")), txt(x0 + 160, y0 + H / 2 + 6, t("height (h)", "altura (h)"), 16, AZ)]
    return svg("0 0 580 215", t("A triangle drawn inside a rectangle with the same base and the same height. The dashed height goes straight up from the base to the top corner, making a right angle. The triangle fills exactly half of the rectangle.",
                                "Un triángulo dibujado dentro de un rectángulo con la misma base y la misma altura. La altura punteada sube recta desde la base hasta la esquina de arriba, formando un ángulo recto. El triángulo ocupa exactamente la mitad del rectángulo."), "".join(s), ancho=480)

def figura_L():
    k, x0, y0 = 26, 120, 20
    pts = [(0, 0), (8, 0), (8, 5), (4, 5), (4, 8), (0, 8)]
    P = " ".join(f"{x0 + x * k},{y0 + y * k}" for x, y in pts)
    s = [f'<polygon points="{P}" fill="{AZC}" stroke="{GR}" stroke-width="3"/>',
         f'<line x1="{x0}" y1="{y0 + 5 * k}" x2="{x0 + 4 * k}" y2="{y0 + 5 * k}" stroke="{AZ}" stroke-width="2.5" stroke-dasharray="7 5"/>',
         txt(x0 + 4 * k, y0 - 6, "8 ft" if B.L == "en" else "8 pies"), txt(x0 + 8 * k + 34, y0 + 2.5 * k + 6, "5 ft" if B.L == "en" else "5 pies"),
         txt(x0 - 36, y0 + 4 * k + 6, "8 ft" if B.L == "en" else "8 pies"), txt(x0 + 2 * k, y0 + 8 * k + 24, "4 ft" if B.L == "en" else "4 pies"),
         txt(x0 + 4 * k, y0 + 2.5 * k + 6, "A", 20, AZ), txt(x0 + 2 * k, y0 + 6.5 * k + 6, "B", 20, AZ)]
    return svg("0 0 480 260", t("An L-shaped floor. The top part, A, is a rectangle 8 feet by 5 feet. The bottom part, B, is a rectangle 4 feet wide and 3 feet tall. The whole left side measures 8 feet.",
                                "Un piso en forma de L. La parte de arriba, A, es un rectángulo de 8 pies por 5 pies. La parte de abajo, B, es un rectángulo de 4 pies de ancho y 3 pies de alto. Todo el lado izquierdo mide 8 pies."), "".join(s), ancho=420)

def leccion():
    n = N
    s1 = f'''<p>{t("The <strong>area</strong> is the amount of surface <strong>inside</strong> a shape. You need the area to buy carpet for a floor, paint for a wall, or grass for a yard. Perimeter goes around; area covers.",
"El <strong>área</strong> es la cantidad de superficie <strong>dentro</strong> de una figura. Se necesita el área para comprar alfombra para un piso, pintura para una pared o césped para un patio. El perímetro va alrededor; el área cubre.")}</p>
<p>{t("We measure area by counting <strong>square units</strong>: squares that are 1 unit on each side. Count the squares in this rectangle:", "El área se mide contando <strong>unidades cuadradas</strong>: cuadritos de 1 unidad por lado. Cuente los cuadritos de este rectángulo:")}</p>
{cuadricula()}
<p>{t("There are 3 rows of 5 squares: 3 × 5 = <strong>15 square units</strong>. That is why the area of a rectangle is found by <strong>multiplying</strong>.", "Hay 3 filas de 5 cuadritos: 3 × 5 = <strong>15 unidades cuadradas</strong>. Por eso el área de un rectángulo se halla <strong>multiplicando</strong>.")}</p>
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>Area is always in <strong>square units</strong>: square inches (sq in or in²), square feet (sq ft or ft²), square meters (m²). The little 2 means \"square,\" because we multiplied two lengths.</p>",
"<p>El área siempre va en <strong>unidades cuadradas</strong>: pulgadas cuadradas (in²), pies cuadrados (ft² o pies²), metros cuadrados (m²). El 2 pequeño quiere decir «cuadrado», porque multiplicamos dos longitudes.</p>"))}'''

    s2 = f'''{tabla(t("Area formulas for rectangles and squares", "Fórmulas del área de rectángulos y cuadrados"), t("Area of a rectangle and of a square", "El área de un rectángulo y de un cuadrado"),
       [t("Shape", "Figura"), t("Formula", "Fórmula"), t("In words", "En palabras")],
       [[t("rectangle", "rectángulo"), "A = l × w", t("length times width", "largo por ancho")],
        [t("square", "cuadrado"), "A = s × s = s²", t("side times side", "lado por lado")]], expr_cols=(1,))}
{ejemplo(t("Example: a bedroom is 12 ft long and 10 ft wide. What is its area?", "Ejemplo: un cuarto mide 12 pies de largo y 10 pies de ancho. ¿Cuál es su área?"),
  [("1", t("Use the formula.", "Use la fórmula."), "A = 12 × 10 = 120."),
   ("✓", t("Answer with square units.", "Responda con unidades cuadradas."), t("The area is <strong>120 square feet</strong> (120 ft²).", "El área es <strong>120 pies cuadrados</strong> (120 pies²)."))])}
{ejemplo(t("Example: a square tile is 9 inches on each side. What is its area?", "Ejemplo: una loseta cuadrada mide 9 pulgadas por lado. ¿Cuál es su área?"),
  [("1", t("Side times side.", "Lado por lado."), "A = 9 × 9 = 81."),
   ("✓", t("Answer.", "Respuesta."), t("The area is <strong>81 square inches</strong>.", "El área es <strong>81 pulgadas cuadradas</strong>."))])}
{caja("ojo", t("Watch out! Do not mix up area and perimeter", "¡Cuidado! No confunda el área con el perímetro"), t("<p>For the bedroom, the <strong>perimeter</strong> is 12 + 10 + 12 + 10 = 44 ft (the baseboard). The <strong>area</strong> is 12 × 10 = 120 ft² (the carpet). Add for perimeter; multiply for area.</p>",
"<p>En el cuarto, el <strong>perímetro</strong> es 12 + 10 + 12 + 10 = 44 pies (el zócalo). El <strong>área</strong> es 12 × 10 = 120 pies² (la alfombra). Para el perímetro se suma; para el área se multiplica.</p>"))}
{practica("p1", t("Practice 1 — Area of a rectangle", "Práctica 1 — El área de un rectángulo"), t("A rectangle is <strong>9 ft</strong> long and <strong>6 ft</strong> wide. What is its area?", "Un rectángulo mide <strong>9 pies</strong> de largo y <strong>6 pies</strong> de ancho. ¿Cuál es su área?"),
          [("a", t("30 sq ft", "30 pies²")), ("b", t("15 sq ft", "15 pies²")), ("c", t("54 sq ft", "54 pies²")), ("d", t("45 sq ft", "45 pies²"))])}
{enlace(n, t("count", "contar"), t("count the squares", "contar los cuadritos"), t("See why the area of a rectangle is length times width.", "Vea por qué el área de un rectángulo es largo por ancho."))}
{enlace(n, t("rectangles", "rectangulos"), t("area of rectangles and squares", "área de rectángulos y cuadrados"), t("Use A = l × w and A = s × s.", "Use A = l × w y A = s × s."))}'''

    s3 = f'''<p>{t("Every triangle is exactly <strong>half</strong> of a rectangle with the same base and the same height:", "Todo triángulo es exactamente la <strong>mitad</strong> de un rectángulo con la misma base y la misma altura:")}</p>
{triangulo_en_rect()}
<p>{t("So the area of a triangle is half of base times height:", "Así que el área de un triángulo es la mitad de la base por la altura:")} {E("A = ½ × b × h")}</p>
{caja("ojo", t("Watch out! The height goes straight up", "¡Cuidado! La altura sube recta"), t("<p>The <strong>height</strong> is the distance from the base to the opposite corner, measured <strong>straight up</strong> (perpendicular to the base, with a right angle). It is not the slanted side.</p>",
"<p>La <strong>altura</strong> es la distancia de la base a la esquina opuesta, medida <strong>en línea recta hacia arriba</strong> (perpendicular a la base, con un ángulo recto). No es el lado inclinado.</p>"))}
{ejemplo(t("Example: a triangle has a base of 10 ft and a height of 6 ft. What is its area?", "Ejemplo: un triángulo tiene una base de 10 pies y una altura de 6 pies. ¿Cuál es su área?"),
  [("1", t("Base times height.", "Base por altura."), t("10 × 6 = 60 (that is the whole rectangle).", "10 × 6 = 60 (ese es el rectángulo entero).")),
   ("2", t("Take half.", "Saque la mitad."), "60 ÷ 2 = 30."),
   ("✓", t("Answer.", "Respuesta."), t("The area is <strong>30 square feet</strong>.", "El área es <strong>30 pies cuadrados</strong>."))])}
{calc(t("Check it on the calculator", "Compruébelo en la calculadora"), t(f"""<p>Type {T("1")}{T("0")} {T("×")} {T("6")} {T("÷")} {T("2")} {T("enter")}. The screen shows 30.</p>""",
f"""<p>Escriba {T("1")}{T("0")} {T("×")} {T("6")} {T("÷")} {T("2")} {T("enter")}. La pantalla muestra 30.</p>"""))}
{practica("p2", t("Practice 2 — Area of a triangle", "Práctica 2 — El área de un triángulo"), t("A triangle has a base of <strong>8 cm</strong> and a height of <strong>5 cm</strong>. What is its area?", "Un triángulo tiene una base de <strong>8 cm</strong> y una altura de <strong>5 cm</strong>. ¿Cuál es su área?"),
          [("a", "40 cm²"), ("b", "20 cm²"), ("c", "13 cm²"), ("d", "26 cm²")])}
{enlace(n, t("triangles", "triangulos"), t("area of triangles", "área de triángulos"), t("Multiply base times height, then take half.", "Multiplique la base por la altura, y después saque la mitad."))}'''

    s4 = f'''<p>{t("Many real floors and yards are not simple rectangles. Split the shape into rectangles, find each area, and <strong>add</strong>.", "Muchos pisos y patios reales no son rectángulos simples. Divida la figura en rectángulos, halle cada área y <strong>sume</strong>.")}</p>
{figura_L()}
{ejemplo(t("Example: the area of the L-shaped floor", "Ejemplo: el área del piso en forma de L"),
  [("1", t("Part A.", "Parte A."), "8 × 5 = 40 " + t("ft².", "pies².")),
   ("2", t("Part B.", "Parte B."), t("It is 4 ft wide, and its height is 8 − 5 = 3 ft: 4 × 3 = 12 ft².", "Mide 4 pies de ancho, y su altura es 8 − 5 = 3 pies: 4 × 3 = 12 pies².")),
   ("✓", t("Add the parts.", "Sume las partes."), t("40 + 12 = <strong>52 square feet</strong>.", "40 + 12 = <strong>52 pies cuadrados</strong>."))])}
{ejemplo(t("Example: carpet costs $3 per square foot. How much does it cost to carpet a room 12 ft by 10 ft?", "Ejemplo: la alfombra cuesta $3 el pie cuadrado. ¿Cuánto cuesta alfombrar un cuarto de 12 pies por 10 pies?"),
  [("1", t("Area.", "Área."), "12 × 10 = 120 " + t("ft².", "pies².")),
   ("✓", t("Multiply by the price.", "Multiplique por el precio."), "120 × $3 = <strong>$360</strong>.")])}
{tabla(t("Area or perimeter", "¿Área o perímetro?"), t("Which everyday jobs need area and which need perimeter", "Qué trabajos de todos los días necesitan área y cuáles perímetro"),
       [t("Needs perimeter (around)", "Necesita perímetro (alrededor)"), t("Needs area (inside)", "Necesita área (adentro)")],
       [[t("fence, frame, baseboard, border", "cerca, marco, zócalo, borde"), t("carpet, paint, tiles, grass", "alfombra, pintura, losetas, césped")]])}
{practica("p3", t("Practice 3 — An L-shaped room", "Práctica 3 — Un cuarto en forma de L"), t("A room is made of two rectangles: one is <strong>8 m by 5 m</strong> and the other is <strong>4 m by 3 m</strong>. What is the total area?", "Un cuarto está formado por dos rectángulos: uno de <strong>8 m por 5 m</strong> y otro de <strong>4 m por 3 m</strong>. ¿Cuál es el área total?"),
          [("a", "52 m²"), ("b", "20 m²"), ("c", "480 m²"), ("d", "64 m²")])}
{practica("p4", t("Practice 4 — Area or perimeter?", "Práctica 4 — ¿Área o perímetro?"), t("You want to know how much paint to buy for a wall. What do you need to find?", "Usted quiere saber cuánta pintura comprar para una pared. ¿Qué necesita hallar?"),
          [("a", t("the perimeter", "el perímetro")), ("b", t("the volume", "el volumen")), ("c", t("an angle", "un ángulo")), ("d", t("the area", "el área"))])}
{enlace(n, t("real-life", "vida-real"), t("area in real life", "el área en la vida real"), t("L-shaped rooms, carpet, and tiles.", "Cuartos en forma de L, alfombras y losetas."))}'''

    secciones = [("s-" + t("what", "que-es"), t("What is area?", "¿Qué es el área?"), s1),
                 ("s-" + t("rectangles", "rectangulos"), t("Area of rectangles and squares", "Área de rectángulos y cuadrados"), s2),
                 ("s-" + t("triangles", "triangulos"), t("Area of triangles", "Área de triángulos"), s3),
                 ("s-" + t("real", "vida-real"), t("Area in real life", "El área en la vida real"), s4)]

    lesson = {"next": t("Lesson 8.1", "Lección 8.1"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("30 is 2 × 9 + 2 × 6, the perimeter. Area multiplies.", "30 es 2 × 9 + 2 × 6, el perímetro. El área multiplica."), "b": t("15 is 9 + 6. Multiply length times width.", "15 es 9 + 6. Multiplique el largo por el ancho."), "d": t("Check the multiplication: 9 × 6.", "Revise la multiplicación: 9 × 6.")},
             "right": t("9 × 6 = 54 square feet.", "9 × 6 = 54 pies cuadrados."), "solution": t("A = l × w = 9 × 6 = 54 square feet.", "A = l × w = 9 × 6 = 54 pies cuadrados.")},
      "p2": {"ok": "b", "hints": {"a": t("40 is 8 × 5, the whole rectangle. A triangle is half.", "40 es 8 × 5, el rectángulo entero. Un triángulo es la mitad."), "c": t("13 is 8 + 5. Multiply, then take half.", "13 es 8 + 5. Multiplique, y después saque la mitad."), "d": t("26 is 2 × (8 + 5), a perimeter idea. Use ½ × b × h.", "26 es 2 × (8 + 5), una idea de perímetro. Use ½ × b × h.")},
             "right": t("8 × 5 = 40, and half is 20 cm².", "8 × 5 = 40, y la mitad es 20 cm²."), "solution": t("A = ½ × 8 × 5 = 40 ÷ 2 = 20 cm².", "A = ½ × 8 × 5 = 40 ÷ 2 = 20 cm².")},
      "p3": {"ok": "a", "hints": {"b": t("20 is 8 + 5 + 4 + 3. Find each area and add the areas.", "20 es 8 + 5 + 4 + 3. Halle cada área y sume las áreas."), "c": t("480 multiplies the two areas. Add them.", "480 multiplica las dos áreas. Súmelas."), "d": t("Check the second rectangle: 4 × 3 = 12, not 24.", "Revise el segundo rectángulo: 4 × 3 = 12, no 24.")},
             "right": t("40 + 12 = 52 m².", "40 + 12 = 52 m²."), "solution": t("8 × 5 = 40 m² and 4 × 3 = 12 m². Total: 40 + 12 = 52 m².", "8 × 5 = 40 m² y 4 × 3 = 12 m². Total: 40 + 12 = 52 m².")},
      "p4": {"ok": "d", "hints": {"a": t("The perimeter is the border, like a frame. Paint covers the surface.", "El perímetro es el borde, como un marco. La pintura cubre la superficie."), "b": t("Volume is the space inside a box. A wall is flat.", "El volumen es el espacio dentro de una caja. Una pared es plana."), "c": t("An angle does not tell how much surface to cover.", "Un ángulo no dice cuánta superficie hay que cubrir.")},
             "right": t("Paint covers a surface: area.", "La pintura cubre una superficie: área."), "solution": t("Paint covers the surface inside the wall, so you need the area.", "La pintura cubre la superficie de la pared, así que necesita el área.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("Feet measure length, like a perimeter.", "Los pies miden longitud, como un perímetro."), "c": t("Degrees measure angles.", "Los grados miden ángulos."), "d": t("Cubic feet measure volume.", "Los pies cúbicos miden volumen.")}, "solution": t("Area is counted in squares: square feet, square inches, square meters.", "El área se cuenta en cuadritos: pies cuadrados, pulgadas cuadradas, metros cuadrados.")},
      "B": {"ok": "c", "hints": {"a": t("13 is 8 + 5. Multiply.", "13 es 8 + 5. Multiplique."), "b": t("26 is the perimeter. Area multiplies.", "26 es el perímetro. El área multiplica."), "d": t("80 doubles the area. A = l × w only.", "80 es el doble del área. A = l × w, nada más.")}, "solution": t("8 × 5 = 40 m².", "8 × 5 = 40 m².")},
      "C": {"ok": "a", "hints": {"b": t("28 is 4 × 7, the perimeter.", "28 es 4 × 7, el perímetro."), "c": t("14 is 7 + 7. Multiply side times side.", "14 es 7 + 7. Multiplique lado por lado."), "d": t("21 is 3 × 7. A square's area is side times side.", "21 es 3 × 7. El área de un cuadrado es lado por lado.")}, "solution": t("7 × 7 = 49 in².", "7 × 7 = 49 pulgadas cuadradas.")},
      "D": {"ok": "c", "hints": {"a": t("60 is 10 × 6, the whole rectangle. Take half.", "60 es 10 × 6, el rectángulo entero. Saque la mitad."), "b": t("16 is 10 + 6. Multiply, then take half.", "16 es 10 + 6. Multiplique, y después saque la mitad."), "d": t("32 is 2 × (10 + 6). Use ½ × b × h.", "32 es 2 × (10 + 6). Use ½ × b × h.")}, "solution": t("½ × 10 × 6 = 30 ft².", "½ × 10 × 6 = 30 pies².")},
      "E": {"ok": "d", "hints": {"a": t("A fence goes around: perimeter.", "Una cerca va alrededor: perímetro."), "b": t("A frame goes around: perimeter.", "Un marco va alrededor: perímetro."), "c": t("A baseboard goes around the room: perimeter.", "Un zócalo va alrededor del cuarto: perímetro.")}, "solution": t("Carpet covers the floor: you need the area.", "La alfombra cubre el piso: se necesita el área.")},
      "F": {"ok": "b", "hints": {"a": t("$132 is 44 × 3: you used the perimeter. Carpet covers the area.", "$132 es 44 × 3: usó el perímetro. La alfombra cubre el área."), "c": t("$66 is 22 × 3: you added 12 + 10. Multiply for area.", "$66 es 22 × 3: sumó 12 + 10. Para el área, multiplique."), "d": t("$44 is the perimeter in feet, not a cost.", "$44 es el perímetro en pies, no un costo.")}, "solution": t("Area: 12 × 10 = 120 ft². Cost: 120 × $3 = $360.", "Área: 12 × 10 = 120 pies². Costo: 120 × $3 = $360.")},
      "G": {"ok": "a", "hints": {"b": t("23 adds the sides. Find each area and add the areas.", "23 suma los lados. Halle cada área y sume las áreas."), "c": t("Check part B: 6 × 3 = 18.", "Revise la parte B: 6 × 3 = 18."), "d": t("240 multiplies 40 × 6. Add the two areas.", "240 multiplica 40 × 6. Sume las dos áreas.")}, "solution": t("10 × 4 = 40 and 6 × 3 = 18. Total: 58 ft².", "10 × 4 = 40 y 6 × 3 = 18. Total: 58 pies².")},
      "H": {"ok": "d", "hints": {"a": t("3 is 24 ÷ 8. Remember the ½: ½ × 8 × h = 4 × h.", "3 es 24 ÷ 8. Recuerde el ½: ½ × 8 × h = 4 × h."), "b": t("16 is 24 − 8. Use the formula: ½ × 8 × h = 24.", "16 es 24 − 8. Use la fórmula: ½ × 8 × h = 24."), "c": t("192 multiplies. Work backward: divide.", "192 multiplica. Trabaje al revés: divida.")}, "solution": t("½ × 8 × h = 24, so 4 × h = 24 and h = 6 in. Check: ½ × 8 × 6 = 24.", "½ × 8 × h = 24, así que 4 × h = 24 y h = 6 pulgadas. Comprobación: ½ × 8 × 6 = 24.")}
     }}

    quiz = [
     ("A", t("Area is measured in:", "El área se mide en:"), [("a", t("feet", "pies")), ("b", t("square feet", "pies cuadrados")), ("c", t("degrees", "grados")), ("d", t("cubic feet", "pies cúbicos"))]),
     ("B", t("A rectangle is <strong>8 m</strong> by <strong>5 m</strong>. What is its area?", "Un rectángulo mide <strong>8 m</strong> por <strong>5 m</strong>. ¿Cuál es su área?"), [("a", "13 m²"), ("b", "26 m²"), ("c", "40 m²"), ("d", "80 m²")]),
     ("C", t("A square has sides of <strong>7 in</strong>. What is its area?", "Un cuadrado tiene lados de <strong>7 pulgadas</strong>. ¿Cuál es su área?"), [("a", "49 in²"), ("b", "28 in²"), ("c", "14 in²"), ("d", "21 in²")]),
     ("D", t("A triangle has a base of <strong>10 ft</strong> and a height of <strong>6 ft</strong>. What is its area?", "Un triángulo tiene una base de <strong>10 pies</strong> y una altura de <strong>6 pies</strong>. ¿Cuál es su área?"), [("a", t("60 sq ft", "60 pies²")), ("b", t("16 sq ft", "16 pies²")), ("c", t("30 sq ft", "30 pies²")), ("d", t("32 sq ft", "32 pies²"))]),
     ("E", t("Which job needs the <strong>area</strong>?", "¿Qué trabajo necesita el <strong>área</strong>?"), [("a", t("a fence around a yard", "una cerca alrededor de un patio")), ("b", t("a frame for a picture", "un marco para un cuadro")), ("c", t("a baseboard for a room", "un zócalo para un cuarto")), ("d", t("carpet for a floor", "alfombra para un piso"))]),
     ("F", t("Carpet costs <strong>$3 per square foot</strong>. How much does it cost to carpet a room <strong>12 ft by 10 ft</strong>?", "La alfombra cuesta <strong>$3 el pie cuadrado</strong>. ¿Cuánto cuesta alfombrar un cuarto de <strong>12 pies por 10 pies</strong>?"), [("a", "$132"), ("b", "$360"), ("c", "$66"), ("d", "$44")]),
     ("G", t("A floor is made of two rectangles: <strong>10 ft by 4 ft</strong> and <strong>6 ft by 3 ft</strong>. What is the total area?", "Un piso está formado por dos rectángulos: <strong>10 pies por 4 pies</strong> y <strong>6 pies por 3 pies</strong>. ¿Cuál es el área total?"), [("a", t("58 sq ft", "58 pies²")), ("b", t("23 sq ft", "23 pies²")), ("c", t("46 sq ft", "46 pies²")), ("d", t("240 sq ft", "240 pies²"))]),
     ("H", t("A triangle has an area of <strong>24 in²</strong> and a base of <strong>8 in</strong>. What is its height?", "Un triángulo tiene un área de <strong>24 pulgadas cuadradas</strong> y una base de <strong>8 pulgadas</strong>. ¿Cuál es su altura?"), [("a", "3 in"), ("b", "16 in"), ("c", "192 in"), ("d", "6 in")])]

    return B.pagina_leccion(n, 7, t("Geometry", "Geometría"),
        t("Area of rectangles and triangles", "Área de rectángulos y triángulos"),
        t("Carpet, paint, and tiles: measure the surface inside a shape in square units.", "Alfombra, pintura y losetas: mida la superficie dentro de una figura en unidades cuadradas."),
        ("🟦", t("Count the squares", "Cuente los cuadritos")),
        [t("<strong>Explain</strong> what area is and why it uses square units.", "<strong>Explicar</strong> qué es el área y por qué usa unidades cuadradas."),
         t("<strong>Find</strong> the area of rectangles and squares.", "<strong>Hallar</strong> el área de rectángulos y cuadrados."),
         t("<strong>Find</strong> the area of triangles with ½ × base × height.", "<strong>Hallar</strong> el área de triángulos con ½ × base × altura."),
         t("<strong>Solve</strong> real problems with L-shaped rooms and prices, and decide between area and perimeter.", "<strong>Resolver</strong> problemas reales con cuartos en forma de L y precios, y decidir entre área y perímetro.")],
        secciones,
        (t("Draw a rectangle on graph paper and count its squares. Then check with length × width. Draw a triangle with the same base and height and show that it is half of the rectangle.",
           "Dibuje un rectángulo en papel cuadriculado y cuente sus cuadritos. Después compruebe con largo × ancho. Dibuje un triángulo con la misma base y la misma altura y muestre que es la mitad del rectángulo."),
         t("Measure a room in your home. Find its area, and find how much it would cost to cover it with carpet at $3 per square foot. Find its perimeter too, for the baseboard.",
           "Mida un cuarto de su casa. Halle su área y cuánto costaría cubrirlo con alfombra a $3 el pie cuadrado. Halle también su perímetro, para el zócalo.")),
        quiz,
        t("Self-check checklist for area", "Lista de autoevaluación del área"),
        t("Self-check checklist: skills for area", "Lista de autoevaluación: destrezas con el área"),
        [(t("Square units", "Unidades cuadradas"), t("I explain area as squares and always write square units.", "Explico el área como cuadritos y siempre escribo unidades cuadradas."), t("I find the area but sometimes forget the square units.", "Hallo el área, pero a veces olvido las unidades cuadradas."), t("I mix up area and perimeter.", "Confundo el área con el perímetro.")),
         (t("Rectangles and squares", "Rectángulos y cuadrados"), t("I use A = l × w and A = s × s with no mistakes.", "Uso A = l × w y A = s × s sin errores."), t("I use them with some help.", "Las uso con un poco de ayuda."), t("I add the sides instead of multiplying.", "Sumo los lados en vez de multiplicar.")),
         (t("Triangles", "Triángulos"), t("I use ½ × b × h and find the height straight up.", "Uso ½ × b × h y hallo la altura en línea recta."), t("I sometimes forget the ½.", "A veces olvido el ½."), t("I use the slanted side as the height.", "Uso el lado inclinado como altura.")),
         (t("Real problems", "Problemas reales"), t("I split shapes into rectangles and use prices per square foot.", "Divido figuras en rectángulos y uso precios por pie cuadrado."), t("I solve simple rectangles, but L-shapes are hard.", "Resuelvo rectángulos simples, pero las formas de L me cuestan."), t("I do not know when to use area or perimeter.", "No sé cuándo usar área o perímetro."))],
        t("<p>You have finished Topic 7. You can now classify shapes and find their perimeter and their area, the geometry skills that appear most on the GED® test.</p>\n<p>In <strong>Topic 8 · Tables, graphs, and final project</strong> you will read and make tables and graphs, and you will put all of Level 1 together in a final project.</p>",
          "<p>Terminó el Tema 7. Ya sabe clasificar figuras y hallar su perímetro y su área, las destrezas de geometría que más aparecen en el examen de GED®.</p>\n<p>En el <strong>Tema 8 · Tablas, gráficas y proyecto final</strong> leerá y hará tablas y gráficas, y juntará todo el Nivel 1 en un proyecto final.</p>"),
        ("8-1", (t("Topic 8 · ", "Tema 8 · "), t("Lesson 8.1 · Reading and understanding data tables", "Lección 8.1 · Leer e interpretar tablas de datos"))),
        [(t("area", "área"), t("The amount of surface inside a shape, measured in square units.", "La cantidad de superficie dentro de una figura, medida en unidades cuadradas.")),
         (t("square unit", "unidad cuadrada"), t("A square that is 1 unit on each side, like 1 ft² or 1 m².", "Un cuadrito de 1 unidad por lado, como 1 pie² o 1 m².")),
         (t("base", "base"), t("The side of a triangle (or rectangle) we measure along the bottom.", "El lado de un triángulo (o rectángulo) que se mide abajo.")),
         (t("height", "altura"), t("The distance from the base to the opposite corner, measured straight up, at a right angle.", "La distancia de la base a la esquina opuesta, medida en línea recta, con un ángulo recto.")),
         (t("composite shape", "figura compuesta"), t("A shape made of simpler shapes, like an L made of two rectangles.", "Una figura formada por figuras más simples, como una L formada por dos rectángulos."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "uu": {"in": "square inches", "ft": "square feet", "m": "square meters", "cm": "square centimeters", "yd": "square yards"},
  "ul": {"in": "inches", "ft": "feet", "m": "meters", "cm": "centimeters", "yd": "yards"},
  "ab": {"in": "in", "ft": "ft", "m": "m", "cm": "cm", "yd": "yd"},
  "pregContar": "Each small square is 1 square unit. What is the area of this rectangle?",
  "ariaContar": "A rectangle on a grid, {l} squares long and {w} squares tall.",
  "solContar": "There are {w} rows of {l} squares: {w} × {l} = <strong>{a}</strong> square units.",
  "perim": "That is the perimeter (around). Area counts the squares inside.",
  "suma": "You added. Area multiplies: rows × squares in each row.",
  "pistaContar": "Count the squares in one row, then multiply by the number of rows.",
  "pregRect": "A rectangle is <strong>{l} {u}</strong> long and <strong>{w} {u}</strong> wide. What is its area in {uu}?",
  "pregCuad": "A square has sides of <strong>{s} {u}</strong>. What is its area in {uu}?",
  "solRect": "A = l × w = {l} × {w} = <strong>{a}</strong> {uu}.",
  "solCuad": "A = s × s = {s} × {s} = <strong>{a}</strong> {uu}.",
  "cuatro": "That is 4 × the side, the perimeter. Area is side × side.",
  "pistaRect": "Area of a rectangle: length × width. Area of a square: side × side.",
  "pregTri": "A triangle has a base of <strong>{b} {u}</strong> and a height of <strong>{h} {u}</strong>. What is its area in {uu}?",
  "ariaTri": "A triangle with a base of {b} {u} and a height of {h} {u}.",
  "solTri": "A = ½ × b × h = ½ × {b} × {h} = {p} ÷ 2 = <strong>{a}</strong> {uu}.",
  "sinMitad": "That is base × height, the whole rectangle. A triangle is half: divide by 2.",
  "sumaTri": "Multiply base × height, then take half.",
  "pistaTri": "A = ½ × base × height.",
  "pregL": "A floor is made of two rectangles: <strong>{a1} {u} by {b1} {u}</strong> and <strong>{a2} {u} by {b2} {u}</strong>. What is the total area in {uu}?",
  "solL": "{a1} × {b1} = {A1} and {a2} × {b2} = {A2}. Total: {A1} + {A2} = <strong>{A}</strong> {uu}.",
  "pregCosto": "Carpet costs <strong>${c} per square foot</strong>. How many dollars does it cost to carpet a room <strong>{l} ft by {w} ft</strong>?",
  "solCosto": "Area: {l} × {w} = {A} square feet. Cost: {A} × ${c} = $<strong>{r}</strong>.",
  "pregLosetas": "A patio is <strong>{l} ft by {w} ft</strong>. Each tile covers <strong>1 square foot</strong>. Tiles come in boxes of <strong>{k}</strong>. How many boxes do you need?",
  "solLosetas": "Area: {l} × {w} = {A} tiles. Boxes: {A} ÷ {k} = {q}{resto}. You need <strong>{n}</strong> boxes.",
  "resto": ", remainder {r}, so you need one more box for the last {r} tiles",
  "masUna": "You need enough tiles: if there is a remainder, buy one more box.",
  "multAreas": "Find each area and add them; do not multiply the areas.",
  "perimR": "You used the perimeter. Carpet and tiles cover the area.",
  "pistaReal": "Find the area first, then do the extra step."
 },
 "es": {
  "uu": {"in": "pulgadas cuadradas", "ft": "pies cuadrados", "m": "metros cuadrados", "cm": "centímetros cuadrados", "yd": "yardas cuadradas"},
  "ul": {"in": "pulgadas", "ft": "pies", "m": "metros", "cm": "centímetros", "yd": "yardas"},
  "ab": {"in": "pulg", "ft": "pies", "m": "m", "cm": "cm", "yd": "yd"},
  "pregContar": "Cada cuadrito es 1 unidad cuadrada. ¿Cuál es el área de este rectángulo?",
  "ariaContar": "Un rectángulo sobre una cuadrícula, de {l} cuadritos de largo y {w} cuadritos de alto.",
  "solContar": "Hay {w} filas de {l} cuadritos: {w} × {l} = <strong>{a}</strong> unidades cuadradas.",
  "perim": "Eso es el perímetro (alrededor). El área cuenta los cuadritos de adentro.",
  "suma": "Sumó. El área multiplica: filas × cuadritos de cada fila.",
  "pistaContar": "Cuente los cuadritos de una fila, y después multiplique por la cantidad de filas.",
  "pregRect": "Un rectángulo mide <strong>{l} {u}</strong> de largo y <strong>{w} {u}</strong> de ancho. ¿Cuál es su área en {uu}?",
  "pregCuad": "Un cuadrado tiene lados de <strong>{s} {u}</strong>. ¿Cuál es su área en {uu}?",
  "solRect": "A = l × w = {l} × {w} = <strong>{a}</strong> {uu}.",
  "solCuad": "A = s × s = {s} × {s} = <strong>{a}</strong> {uu}.",
  "cuatro": "Eso es 4 × el lado, el perímetro. El área es lado × lado.",
  "pistaRect": "Área de un rectángulo: largo × ancho. Área de un cuadrado: lado × lado.",
  "pregTri": "Un triángulo tiene una base de <strong>{b} {u}</strong> y una altura de <strong>{h} {u}</strong>. ¿Cuál es su área en {uu}?",
  "ariaTri": "Un triángulo con una base de {b} {u} y una altura de {h} {u}.",
  "solTri": "A = ½ × b × h = ½ × {b} × {h} = {p} ÷ 2 = <strong>{a}</strong> {uu}.",
  "sinMitad": "Eso es base × altura, el rectángulo entero. El triángulo es la mitad: divida entre 2.",
  "sumaTri": "Multiplique la base por la altura, y después saque la mitad.",
  "pistaTri": "A = ½ × base × altura.",
  "pregL": "Un piso está formado por dos rectángulos: <strong>{a1} {u} por {b1} {u}</strong> y <strong>{a2} {u} por {b2} {u}</strong>. ¿Cuál es el área total en {uu}?",
  "solL": "{a1} × {b1} = {A1} y {a2} × {b2} = {A2}. Total: {A1} + {A2} = <strong>{A}</strong> {uu}.",
  "pregCosto": "La alfombra cuesta <strong>${c} el pie cuadrado</strong>. ¿Cuántos dólares cuesta alfombrar un cuarto de <strong>{l} pies por {w} pies</strong>?",
  "solCosto": "Área: {l} × {w} = {A} pies cuadrados. Costo: {A} × ${c} = $<strong>{r}</strong>.",
  "pregLosetas": "Un patio mide <strong>{l} pies por {w} pies</strong>. Cada loseta cubre <strong>1 pie cuadrado</strong>. Las losetas vienen en cajas de <strong>{k}</strong>. ¿Cuántas cajas necesita?",
  "solLosetas": "Área: {l} × {w} = {A} losetas. Cajas: {A} ÷ {k} = {q}{resto}. Necesita <strong>{n}</strong> cajas.",
  "resto": ", residuo {r}, así que necesita una caja más para las últimas {r} losetas",
  "masUna": "Necesita suficientes losetas: si hay residuo, compre una caja más.",
  "multAreas": "Halle cada área y súmelas; no multiplique las áreas.",
  "perimR": "Usó el perímetro. La alfombra y las losetas cubren el área.",
  "pistaReal": "Primero halle el área, y después haga el paso adicional."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
var UN = ["in", "ft", "m", "cm", "yd"];

/* ============ MODULE 1 · count the squares ============ */
function genContar(){
  var l = aleatorio(3, 9), w = aleatorio(2, 6), k = Math.min(36, 300 / l), s = "", x0 = 20, y0 = 20, a = l * w, tr = [];
  s += '<rect x="' + x0 + '" y="' + y0 + '" width="' + f1(l * k) + '" height="' + f1(w * k) + '" fill="#e3f2fd" stroke="#37474f" stroke-width="3"/>';
  for (var i = 1; i < l; i++) s += linea([x0 + i * k, y0], [x0 + i * k, y0 + w * k], "#90a4ae", 1.5);
  for (var j = 1; j < w; j++) s += linea([x0, y0 + j * k], [x0 + l * k, y0 + j * k], "#90a4ae", 1.5);
  if (2 * l + 2 * w !== a) tr.push({ v: 2 * l + 2 * w, msg: TXT.perim });
  if (l + w !== a) tr.push({ v: l + w, msg: TXT.suma });
  var svg = '<svg class="figura" viewBox="0 0 ' + f1(l * k + 40) + ' ' + f1(w * k + 40) + '" role="img" aria-label="' + F(TXT.ariaContar, { l: l, w: w }) + '">' + s + '</svg>';
  return { enun: TXT.pregContar + svg, solucion: F(TXT.solContar, { l: l, w: w, a: a }), evalua: numN(a, tr, TXT.pistaContar) };
}

/* ============ MODULE 2 · rectangles and squares ============ */
function genRect(){
  var u = elige(UN), tr = [];
  if (Math.random() < 0.65){
    var l = aleatorio(4, 25), w = aleatorio(2, l), a = l * w;
    if (2 * l + 2 * w !== a) tr.push({ v: 2 * l + 2 * w, msg: TXT.perim }); if (l + w !== a) tr.push({ v: l + w, msg: TXT.suma });
    return { enun: F(TXT.pregRect, { l: l, w: w, u: TXT.ul[u], uu: TXT.uu[u] }), solucion: F(TXT.solRect, { l: l, w: w, a: com(a), uu: TXT.uu[u] }), evalua: numN(a, tr, TXT.pistaRect) };
  }
  var s = aleatorio(3, 20), a2 = s * s;
  if (4 * s !== a2) tr.push({ v: 4 * s, msg: TXT.cuatro }); if (2 * s !== a2) tr.push({ v: 2 * s, msg: TXT.suma });
  return { enun: F(TXT.pregCuad, { s: s, u: TXT.ul[u], uu: TXT.uu[u] }), solucion: F(TXT.solCuad, { s: s, a: com(a2), uu: TXT.uu[u] }), evalua: numN(a2, tr, TXT.pistaRect) };
}

/* ============ MODULE 3 · triangles ============ */
function genTri(){
  var u = elige(UN), b = aleatorio(2, 20), h = aleatorio(2, 16), tr = [];
  if ((b * h) % 2) b += 1;
  var p = b * h, a = p / 2, cx = aleatorio(20, 80) / 100;
  if (p !== a) tr.push({ v: p, msg: TXT.sinMitad }); if (b + h !== a) tr.push({ v: b + h, msg: TXT.sumaTri });
  var k = Math.min(240 / b, 150 / h), W = b * k, H = h * k, x0 = 20, y0 = 20, xt = x0 + cx * W;
  var s = '<polygon points="' + x0 + ',' + f1(y0 + H) + ' ' + f1(x0 + W) + ',' + f1(y0 + H) + ' ' + f1(xt) + ',' + y0 + '" fill="#e3f2fd" stroke="#37474f" stroke-width="3"/>';
  s += '<line x1="' + f1(xt) + '" y1="' + y0 + '" x2="' + f1(xt) + '" y2="' + f1(y0 + H) + '" stroke="#1565c0" stroke-width="2.5" stroke-dasharray="6 4"/>';
  s += '<rect x="' + f1(xt) + '" y="' + f1(y0 + H - 12) + '" width="12" height="12" fill="none" stroke="#1565c0" stroke-width="2"/>';
  s += texto([x0 + W / 2, y0 + H + 22], b + " " + TXT.ab[u], 16, "#1a2330") + texto([xt + (cx < 0.5 ? 34 : -34), y0 + H / 2], h + " " + TXT.ab[u], 16, "#1565c0");
  var svg = '<svg class="figura" viewBox="0 0 ' + f1(W + 40) + ' ' + f1(H + 50) + '" role="img" aria-label="' + F(TXT.ariaTri, { b: b, h: h, u: TXT.ul[u] }) + '">' + s + '</svg>';
  return { enun: F(TXT.pregTri, { b: b, h: h, u: TXT.ul[u], uu: TXT.uu[u] }) + svg, solucion: F(TXT.solTri, { b: b, h: h, p: p, a: a, uu: TXT.uu[u] }), evalua: numN(a, tr, TXT.pistaTri) };
}

/* ============ MODULE 4 · real life ============ */
function genReal(){
  var r = Math.random(), tr = [];
  if (r < 0.34){
    var u = elige(UN), a1 = aleatorio(6, 15), b1 = aleatorio(3, 8), a2 = aleatorio(2, 6), b2 = aleatorio(2, 6), A1 = a1 * b1, A2 = a2 * b2, A = A1 + A2;
    tr.push({ v: A1 * A2, msg: TXT.multAreas }); tr.push({ v: a1 + b1 + a2 + b2, msg: TXT.suma });
    return { enun: F(TXT.pregL, { a1: a1, b1: b1, a2: a2, b2: b2, u: TXT.ul[u], uu: TXT.uu[u] }), solucion: F(TXT.solL, { a1: a1, b1: b1, a2: a2, b2: b2, A1: A1, A2: A2, A: A, uu: TXT.uu[u] }),
      evalua: numN(A, tr.filter(function(x){ return x.v !== A; }), TXT.pistaReal) };
  }
  if (r < 0.67){
    var l = aleatorio(8, 20), w = aleatorio(6, l), c = aleatorio(2, 9), Ar = l * w, res = Ar * c;
    tr.push({ v: (2 * l + 2 * w) * c, msg: TXT.perimR });
    return { enun: F(TXT.pregCosto, { c: c, l: l, w: w }), solucion: F(TXT.solCosto, { l: l, w: w, A: Ar, c: c, r: com(res) }), evalua: numN(res, tr.filter(function(x){ return x.v !== res; }), TXT.pistaReal) };
  }
  var L = aleatorio(6, 15), W = aleatorio(4, 12), k = elige([10, 12, 15, 20]), At = L * W, q = Math.floor(At / k), rr = At % k, nb = rr ? q + 1 : q;
  if (rr) tr.push({ v: q, msg: TXT.masUna });
  return { enun: F(TXT.pregLosetas, { l: L, w: W, k: k }), solucion: F(TXT.solLosetas, { l: L, w: W, A: At, k: k, q: q, resto: rr ? F(TXT.resto, { r: rr }) : "", n: nb }), evalua: numN(nb, tr, TXT.pistaReal) };
}

creaPracticaLibre("p1", genContar);
creaPracticaLibre("p2", genRect);
creaPracticaLibre("p3", genTri);
creaPracticaLibre("p4", genReal);
'''

def practica_pagina():
    n = N
    mods = [
     (t("count", "contar"), t("Count the squares", "Contar los cuadritos"),
      f'''      <p>{t("Area is the number of squares inside a shape. In a rectangle, the squares make rows: <strong>rows × squares in each row</strong>. That is why area = length × width.", "El área es la cantidad de cuadritos dentro de una figura. En un rectángulo, los cuadritos forman filas: <strong>filas × cuadritos de cada fila</strong>. Por eso el área = largo × ancho.")}</p>
{B.libre("p1", t("Practice: the area", "Practique: el área"), t("Area", "Área"))}'''),
     (t("rectangles", "rectangulos"), t("Area of rectangles and squares", "Área de rectángulos y cuadrados"),
      f'''      <table class="reglas">
        <caption>{t("Area formulas", "Fórmulas del área")}</caption>
        <tbody>
          <tr><td>{t("rectangle", "rectángulo")}</td><td>A = l × w</td></tr>
          <tr><td>{t("square", "cuadrado")}</td><td>A = s × s</td></tr>
        </tbody>
      </table>
{B.libre("p2", t("Practice: use the formula", "Practique: use la fórmula"), t("Area", "Área"))}'''),
     (t("triangles", "triangulos"), t("Area of triangles", "Área de triángulos"),
      f'''      <p>{t("A triangle is half of a rectangle: <strong>A = ½ × b × h</strong>. The height is measured straight up from the base (the dashed line).", "Un triángulo es la mitad de un rectángulo: <strong>A = ½ × b × h</strong>. La altura se mide en línea recta desde la base (la línea punteada).")}</p>
{B.libre("p3", t("Practice: area of a triangle", "Practique: el área de un triángulo"), t("Area", "Área"))}'''),
     (t("real-life", "vida-real"), t("Area in real life", "El área en la vida real"),
      f'''      <p>{t("Split L-shapes into rectangles and add the areas. For carpet, multiply the area by the price. For tiles, if there is a remainder, buy one more box.", "Divida las formas de L en rectángulos y sume las áreas. Para la alfombra, multiplique el área por el precio. Para las losetas, si hay residuo, compre una caja más.")}</p>
{B.libre("p4", t("Practice: real problems", "Practique: problemas reales"), t("Answer", "Respuesta"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t("Geometry", "Geometría"), t("Area of rectangles and triangles", "Área de rectángulos y triángulos"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun svg.figura{display:block;width:100%;max-width:340px;height:auto;margin:10px auto;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Área de rectángulos y triángulos")
