"""Level 3 · Lesson 7.1 · Volume of prisms and cylinders — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_7-1.html and algebra/n3-l7-1.html (GEDparaHispanos). US units: inches, feet, gallons.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n3
from build_n3_explora_6 import ESTILO as ESTILO_GEO

B.NIVEL = 3
N = "7-1"
TEMA = ("Volume and data analysis", "Volumen y análisis de datos")
TIT = ("Volume of prisms and cylinders", "Volumen de prismas y cilindros")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js", "/math/data3.js")
ESTILO = ESTILO_GEO + """
  .datos{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;}
  .dato{min-width:40px;text-align:center;padding:6px 8px;border:2px solid #90a4ae;border-radius:8px;background:#fff;font-weight:700;font-size:17px;}
  .dato.med{background:var(--tema);border-color:var(--tema-d);color:#fff;}
  .dato.baja{border-color:#1565c0;} .dato.alta{border-color:#2e7d32;}
  .dato.atip{background:#ffebee;border-color:#b71c1c;color:#b71c1c;}"""

def figuras():
    s = ('<polygon points="40,90 190,90 230,60 80,60" fill="#cfd8dc" stroke="#37474f" stroke-width="2"/>'
         '<polygon points="40,90 190,90 190,190 40,190" fill="#b0bec5" stroke="#37474f" stroke-width="2"/>'
         '<polygon points="190,90 230,60 230,160 190,190" fill="#90a4ae" stroke="#37474f" stroke-width="2"/>'
         f'<text x="115" y="212" font-size="16" font-weight="700" text-anchor="middle" fill="#0d47a1">{t("length", "largo")}</text>'
         f'<text x="24" y="145" font-size="16" font-weight="700" text-anchor="end" fill="#0d47a1">{t("height", "alto")}</text>'
         f'<text x="222" y="190" font-size="16" font-weight="700" text-anchor="start" fill="#0d47a1">{t("width", "ancho")}</text>'
         '<path d="M330 70 V180 A60 18 0 0 0 450 180 V70" fill="#b0bec5" stroke="#37474f" stroke-width="2"/>'
         '<ellipse cx="390" cy="70" rx="60" ry="18" fill="#cfd8dc" stroke="#37474f" stroke-width="2"/>'
         '<line x1="390" y1="70" x2="450" y2="70" stroke="#b71c1c" stroke-width="3"/><text x="420" y="60" font-size="18" font-weight="700" text-anchor="middle" fill="#b71c1c">r</text>'
         '<line x1="470" y1="70" x2="470" y2="180" stroke="#0d47a1" stroke-width="2"/><text x="480" y="130" font-size="18" font-weight="700" fill="#0d47a1">h</text>')
    return B.svg("0 0 520 230", t("A rectangular box with its length, width, and height labeled, and a cylinder with its radius r and height h labeled.", "Una caja rectangular con su largo, ancho y alto rotulados, y un cilindro con su radio r y su altura h rotulados."), s, 500)

def leccion():
    n = N
    pc3, pg3 = t("in³", "pulg³"), t("ft³", "pies³")
    s1 = f'''<p>{t("Topic 6 closed the geometry of flat figures (two dimensions). Topic 7 takes the step to three dimensions: volume measures how much space a solid takes up, or how much fits inside it. To find it, you use again the formulas and the solving of Topic 5, and the area of the base that you already worked with in earlier levels.", "El Tema 6 cerró la geometría de figuras planas (dos dimensiones). El Tema 7 da el salto a las tres dimensiones: el volumen mide cuánto espacio ocupa un cuerpo sólido o cuánto cabe dentro de él. Para calcularlo se usan de nuevo las fórmulas y el despeje aprendidos en el Tema 5, y el área de la base que ya se trabajó en niveles anteriores.")}</p>
<p>{t("<strong>Volume</strong> is the amount of space that a three-dimensional object takes up. For a prism or a cylinder, it is found with one powerful idea: the area of the base times the height.", "El <strong>volumen</strong> es la cantidad de espacio que ocupa un cuerpo de tres dimensiones. Para un prisma o un cilindro, se calcula con una idea única y poderosa: el área de la base multiplicada por la altura.")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">{t("V = area of the base × height", "V = área de la base × altura")}</p>
{figuras()}
{caja("tip", t("Cubic units", "Unidades cúbicas"), t("<p>Volume multiplies three lengths, so the answer is in <strong>cubic units</strong>: cubic inches (in³), cubic feet (ft³), and so on. Two useful facts: 1 cubic foot = 1,728 cubic inches (12 × 12 × 12), and 1 cubic foot holds about 7.48 gallons.</p>", "<p>Como el volumen multiplica tres medidas de longitud, el resultado se expresa en <strong>unidades cúbicas</strong>: pulgadas cúbicas (pulg³), pies cúbicos (pies³), etc. Dos datos útiles: 1 pie cúbico = 1,728 pulgadas cúbicas (12 × 12 × 12), y en 1 pie cúbico caben unos 7.48 galones.</p>"))}'''

    s2 = f'''<p>{t("In a rectangular prism (a box), the base is a rectangle, so V = length × width × height. In a triangular prism, the base is a triangle: first find the area of the triangle, then multiply it by the height (length) of the prism.", "En un prisma rectangular (una caja), la base es un rectángulo, así que V = largo × ancho × alto. En un prisma triangular, la base es un triángulo, así que primero se calcula el área del triángulo y luego se multiplica por la altura (el largo) del prisma.")}</p>
{ejemplo(t("Example 1: rectangular prism. A box is 5 inches long, 3 inches wide, and 4 inches high. What is its volume?", "Ejemplo 1 · Prisma rectangular. Una caja mide 5 pulgadas de largo, 3 de ancho y 4 de alto. ¿Cuál es su volumen?"),
  [("1", t("Multiply the three dimensions.", "Se multiplican las tres dimensiones."), "5 × 3 × 4 = 60."),
   ("✓", t("Answer.", "Respuesta."), f"V = <strong>60 {pc3}</strong>.")])}
{ejemplo(t("Example 2: triangular prism. A prism has a triangular base with an area of 6 square inches and a height of 10 inches. What is its volume?", "Ejemplo 2 · Prisma triangular. Un prisma tiene una base triangular de área 6 pulgadas cuadradas y una altura de 10 pulgadas. ¿Cuál es su volumen?"),
  [("1", t("Use V = area of the base × height.", "Se usa V = área de la base × altura."), "6 × 10 = 60."),
   ("✓", t("Answer.", "Respuesta."), f"V = <strong>60 {pc3}</strong>.")])}
{practica("p1", t("Practice 1 — A box", "Práctica 1 — Una caja"), t("A box measures 3 × 4 × 5. Its volume is…", "Una caja mide 3 × 4 × 5. Su volumen es…"), [("a", "60"), ("b", "12"), ("c", "20")])}
{practica("p2", t("Practice 2 — Base and height", "Práctica 2 — Base y altura"), t("A prism has a base with an area of 8 and a height of 6. Its volume is…", "Un prisma tiene una base de área 8 y una altura de 6. Su volumen es…"), [("a", "14"), ("b", "48"), ("c", "8")])}
{practica("p3", t("Practice 3 — A cube", "Práctica 3 — Un cubo"), t("A cube has sides of 3. Its volume is…", "Un cubo tiene lados de 3. Su volumen es…"), [("a", "9"), ("b", "18"), ("c", "27")])}
{enlace(n, t("prisms", "prismas"), t("volume of prisms", "volumen de prismas"), t("See the box layer by layer, find the area of the base, and multiply by the height.", "Vea la caja capa por capa, calcule el área de la base y multiplíquela por la altura."))}'''

    s3 = f'''<p>{t("In a cylinder, the base is a circle with radius r, and its area is πr². So the volume is that area times the height:", "En un cilindro, la base es un círculo de radio r, cuya área es πr². Por eso el volumen es esa área multiplicada por la altura:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">V = πr²h</p>
<p>{t("In the calculations, use π ≈ 3.14 (or the π key on the calculator). The formula is on the GED reference sheet; open it with the Reference sheet button.", "En los cálculos se usa π ≈ 3.14 (o la tecla π de la calculadora). La fórmula está en la hoja de referencia del GED; ábrala con el botón Hoja de referencia.")}</p>
{calc(t("About the calculator", "Sobre la calculadora"), t("<p>The GED test uses the TI-30XS MultiView calculator. The calculator on this page does the same operations, although some keys have other names or are in other places. If you have a TI-30XS, practice with it too so you learn where its keys are.</p>", "<p>En el examen GED se usa la calculadora TI-30XS MultiView. La calculadora de esta página hace las mismas operaciones, aunque algunas teclas tienen otro nombre o están en otro lugar. Si tiene una TI-30XS, practique también con ella para conocer la ubicación de sus teclas.</p>"))}
{ejemplo(t("Example 3: a cylinder has a radius of 2 inches and a height of 5 inches. What is its volume? (π ≈ 3.14)", "Ejemplo 3: un cilindro tiene un radio de 2 pulgadas y una altura de 5 pulgadas. ¿Cuál es su volumen? (π ≈ 3.14)"),
  [("1", t("Find the area of the base.", "Se calcula el área de la base."), "πr² = 3.14 × 2² = 3.14 × 4 = 12.56."),
   ("2", t("Multiply by the height.", "Se multiplica por la altura."), "12.56 × 5 = 62.8."),
   ("✓", t("Answer.", "Respuesta."), f"V ≈ <strong>62.8 {pc3}</strong>.")])}
{caja("ojo", t("Square only the radius", "Elevar al cuadrado solo el radio"), t("<p>In πr²h, the exponent applies only to the radius (r²), not to π or the height. A common mistake is to square the whole product. First r², then multiply by π and by h. And if the problem gives the <strong>diameter</strong>, divide it by 2 first to get the radius.</p>", "<p>En πr²h, el exponente afecta únicamente al radio (r²), no a π ni a la altura. Un error común es elevar al cuadrado todo el producto. Primero r², luego se multiplica por π y por h. Y si el problema da el <strong>diámetro</strong>, primero se divide entre 2 para obtener el radio.</p>"))}
{practica("p4", t("Practice 4 — Radius 2, height 10", "Práctica 4 — Radio 2, altura 10"), t("A cylinder has a radius of 2 and a height of 10 (π ≈ 3.14). Its volume is…", "Un cilindro tiene radio 2 y altura 10 (π ≈ 3.14). Su volumen es…"), [("a", "40"), ("b", "62.8"), ("c", "125.6")])}
{practica("p5", t("Practice 5 — Radius 5, height 2", "Práctica 5 — Radio 5, altura 2"), t("A cylinder has a radius of 5 and a height of 2 (π ≈ 3.14). Its volume is…", "Un cilindro tiene radio 5 y altura 2 (π ≈ 3.14). Su volumen es…"), [("a", "157"), ("b", "50"), ("c", "78.5")])}
{enlace(n, t("cylinders", "cilindros"), t("volume of cylinders", "volumen de cilindros"), t("Use V = πr²h with cylinders of different sizes.", "Aplique V = πr²h a cilindros de distintas medidas."))}'''

    s4 = f'''<p>{t("When you know the volume and one measure is missing, solve for it as in Topic 5. For the height of a prism, divide the volume by the area of the base.", "Cuando se conoce el volumen y falta una dimensión, se despeja como en el Tema 5. Para la altura de un prisma, se divide el volumen entre el área de la base.")}</p>
{ejemplo(t("Example 4: solving for the height. A prism has a volume of 60 cubic inches and a base with an area of 12 square inches. What is its height?", "Ejemplo 4 · Despejar la altura. Un prisma tiene un volumen de 60 pulgadas cúbicas y una base de área 12 pulgadas cuadradas. ¿Cuál es su altura?"),
  [("1", t("Start from V = area of the base × height.", "Se parte de V = área de la base × altura."), "60 = 12 × h."),
   ("2", t("Divide by 12.", "Se divide entre 12."), "h = 60 ÷ 12 = 5."),
   ("✓", t("Answer.", "Respuesta."), t("The height is <strong>5 inches</strong>.", "La altura es de <strong>5 pulgadas</strong>."))])}
{caja("tip", t("The radius of a cylinder", "El radio de un cilindro"), t("<p>To find the radius when you know the volume and the height, divide the volume by πh to get r², then take the square root: the same steps as the Pythagorean theorem in Lesson 6.2.</p>", "<p>Para hallar el radio conociendo el volumen y la altura, se divide el volumen entre πh para obtener r², y después se saca la raíz cuadrada: los mismos pasos del teorema de Pitágoras de la Lección 6.2.</p>"))}
{practica("p6", t("Practice 6 — The height", "Práctica 6 — La altura"), t("A prism has V = 100 and a base with an area of 20. The height is…", "Un prisma tiene V = 100 y una base de área 20. La altura es…"), [("a", "80"), ("b", "5"), ("c", "2000")])}
{enlace(n, t("solve", "despejar"), t("solving for the height or the radius", "despejar la altura o el radio"), t("Find the missing measure when you know the volume.", "Halle la medida que falta cuando se conoce el volumen."))}'''

    s5 = f'''<p>{t("Volume answers real questions about building and storage: how many gallons fit in a tank, how much concrete a column needs, how much fits in a box.", "El volumen responde preguntas reales de construcción y almacenamiento: cuántos galones caben en un tanque, cuánto concreto se necesita para una columna, cuánto material entra en una caja.")}</p>
{ejemplo(t("Example 5: a cylindrical tank has a radius of 2 feet and a height of 5 feet. How many cubic feet of water fit? About how many gallons is that? (π ≈ 3.14)", "Ejemplo 5 · Un tanque cilíndrico tiene un radio de 2 pies y una altura de 5 pies. ¿Cuántos pies cúbicos de agua caben? ¿Cuántos galones son, aproximadamente? (π ≈ 3.14)"),
  [("1", t("Area of the base.", "Área de la base."), "3.14 × 2² = 3.14 × 4 = 12.56."),
   ("2", t("Times the height.", "Por la altura."), f"12.56 × 5 = 62.8 {pg3}."),
   ("3", t("Convert to gallons.", "Se pasa a galones."), t("62.8 × 7.48 ≈ 470 gallons.", "62.8 × 7.48 ≈ 470 galones.")),
   ("✓", t("Answer.", "Respuesta."), t(f"About <strong>62.8 {pg3}</strong>, or about <strong>470 gallons</strong>.", f"Caben unos <strong>62.8 {pg3}</strong>, es decir, unos <strong>470 galones</strong>."))])}
{caja("ojo", t("Use the same unit for every measure", "Todas las medidas en la misma unidad"), t("<p>Before you calculate, make sure every measure is in the same unit (all in feet, or all in inches). If the radius is in inches and the height is in feet, convert first to a single unit.</p>", "<p>Antes de calcular, conviene que todas las medidas estén en la misma unidad (todo en pies, o todo en pulgadas). Si el radio está en pulgadas y la altura en pies, primero se convierten a una sola unidad.</p>"))}
{enlace(n, t("capacity", "capacidad"), t("capacity and storage", "capacidad y almacenamiento"), t("Solve problems about tanks, containers, and converting to gallons.", "Resuelva problemas de tanques, envases y conversión a galones."))}'''

    secciones = [("s-" + t("volume", "volumen"), t("What is volume?", "¿Qué es el volumen?"), s1),
                 ("s-" + t("prisms", "prismas"), t("Volume of prisms", "Volumen de prismas"), s2),
                 ("s-" + t("cylinders", "cilindros"), t("Volume of cylinders", "Volumen de cilindros"), s3),
                 ("s-" + t("solve", "despejar"), t("Solving for the height or the radius", "Despejar la altura o el radio"), s4),
                 ("s-" + t("capacity", "capacidad"), t("Uses: capacity and storage", "Aplicaciones: capacidad y almacenamiento"), s5)]

    lesson = {"next": t("Lesson 7.2", "Lección 7.2"), "review": t("sections 2 to 4", "las secciones 2 a 4"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("12 is 3 × 4, the area of the base. Multiply by 5 too.", "12 es 3 × 4, el área de la base. Falta multiplicar por 5."), "c": t("20 is 4 × 5. Multiply the three measures.", "20 es 4 × 5. Hay que multiplicar las tres medidas.")}, "right": "3 × 4 × 5 = 60.", "solution": "V = 3 × 4 × 5 = 60."},
      "p2": {"ok": "b", "hints": {"a": t("You added. Multiply the area of the base by the height.", "Sumó. Hay que multiplicar el área de la base por la altura."), "c": t("8 is only the area of the base. Multiply by the height.", "8 es solo el área de la base. Falta multiplicar por la altura.")}, "right": "8 × 6 = 48.", "solution": "V = 8 × 6 = 48."},
      "p3": {"ok": "c", "hints": {"a": t("9 is 3 × 3, the area of one face. Multiply by 3 once more.", "9 es 3 × 3, el área de una cara. Falta multiplicar otra vez por 3."), "b": t("The side is multiplied three times by itself, not by 6.", "El lado se multiplica tres veces por sí mismo, no por 6.")}, "right": "3 × 3 × 3 = 27.", "solution": "V = 3³ = 27."},
      "p4": {"ok": "c", "hints": {"a": t("40 is 2² × 10. Multiply by 3.14 too.", "40 es 2² × 10. Falta multiplicar por 3.14."), "b": t("62.8 is 3.14 × 2 × 10: the radius was not squared.", "62.8 es 3.14 × 2 × 10: no se elevó el radio al cuadrado.")}, "right": "3.14 × 4 × 10 = 125.6.", "solution": "V = 3.14 × 2² × 10 = 125.6."},
      "p5": {"ok": "a", "hints": {"b": t("50 is 5² × 2. Multiply by 3.14 too.", "50 es 5² × 2. Falta multiplicar por 3.14."), "c": t("78.5 is the area of the base. Multiply by the height, 2.", "78.5 es el área de la base. Falta multiplicar por la altura, 2.")}, "right": "3.14 × 25 × 2 = 157.", "solution": "V = 3.14 × 5² × 2 = 157."},
      "p6": {"ok": "b", "hints": {"a": t("You subtracted. Divide the volume by the area of the base.", "Restó. Hay que dividir el volumen entre el área de la base."), "c": t("You multiplied. To solve for the height, divide.", "Multiplicó. Para despejar la altura se divide.")}, "right": "100 ÷ 20 = 5.", "solution": "h = 100 ÷ 20 = 5."}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("You added the measures. Multiply them.", "Sumó las medidas. Hay que multiplicarlas."), "c": t("12 is 3 × 4. Multiply by 2 too.", "12 es 3 × 4. Falta multiplicar por 2."), "d": t("Check the multiplication: 2 × 3 × 4.", "Revise la multiplicación: 2 × 3 × 4.")}, "solution": "2 × 3 × 4 = 24."},
      "B": {"ok": "d", "hints": {"a": t("You added. Multiply the area of the base by the height.", "Sumó. Hay que multiplicar el área de la base por la altura."), "b": t("12 is only the area of the base.", "12 es solo el área de la base."), "c": t("5 is only the height.", "5 es solo la altura.")}, "solution": "12 × 5 = 60."},
      "C": {"ok": "a", "hints": {"b": t("You added. Multiply the area of the base by the height.", "Sumó. Hay que multiplicar el área de la base por la altura."), "c": t("6 is only the area of the base.", "6 es solo el área de la base."), "d": t("Check the multiplication: 6 × 10.", "Revise la multiplicación: 6 × 10.")}, "solution": "6 × 10 = 60."},
      "D": {"ok": "d", "hints": {"a": t("31.4 is 3.14 × 2 × 5: the radius was not squared.", "31.4 es 3.14 × 2 × 5: no se elevó el radio al cuadrado."), "b": t("20 is 2² × 5. Multiply by 3.14 too.", "20 es 2² × 5. Falta multiplicar por 3.14."), "c": t("Square only the radius, not the height.", "Solo el radio va al cuadrado, no la altura.")}, "solution": "3.14 × 4 × 5 = 62.8."},
      "E": {"ok": "b", "hints": {"a": t("94.2 is 3.14 × 3 × 10: the radius was not squared.", "94.2 es 3.14 × 3 × 10: no se elevó el radio al cuadrado."), "c": t("90 is 3² × 10. Multiply by 3.14 too.", "90 es 3² × 10. Falta multiplicar por 3.14."), "d": t("Use the radius, 3, not the diameter, 6.", "Use el radio, 3, no el diámetro, 6.")}, "solution": "3.14 × 9 × 10 = 282.6."},
      "F": {"ok": "c", "hints": {"a": t("2πr is the circumference of the base.", "2πr es la circunferencia de la base."), "b": t("πr² is only the area of the base.", "πr² es solo el área de la base."), "d": t("lwh is the volume of a box.", "lwh es el volumen de una caja.")}, "solution": "V = πr²h."},
      "G": {"ok": "d", "hints": {"a": t("You subtracted. Divide the volume by the area of the base.", "Restó. Hay que dividir el volumen entre el área de la base."), "b": t("You added. Divide.", "Sumó. Hay que dividir."), "c": t("You multiplied. To solve for the height, divide.", "Multiplicó. Para despejar la altura se divide.")}, "solution": "60 ÷ 12 = 5."},
      "H": {"ok": "b", "hints": {"a": t("The area of the base is 2 × 3 = 6. Divide 24 by 6.", "El área de la base es 2 × 3 = 6. Divida 24 entre 6."), "c": t("Divide by the whole base, 2 × 3 = 6, not only by 2.", "Se divide entre toda la base, 2 × 3 = 6, no solo entre 2."), "d": t("6 is the area of the base. Divide 24 by it.", "6 es el área de la base. Divida 24 entre ella.")}, "solution": "24 ÷ (2 × 3) = 4."}
     }}

    quiz = [
     ("A", t("A rectangular prism measures 2 × 3 × 4. Its volume is…", "Un prisma rectangular mide 2 × 3 × 4. Su volumen es…"), [("a", "9"), ("b", "24"), ("c", "12"), ("d", "48")]),
     ("B", t("A prism has a base with an area of 12 and a height of 5. Its volume is…", "Un prisma tiene una base de área 12 y una altura de 5. Su volumen es…"), [("a", "17"), ("b", "12"), ("c", "5"), ("d", "60")]),
     ("C", t("A triangular prism has a base with an area of 6 and a height of 10. Its volume is…", "Un prisma triangular tiene una base de área 6 y una altura de 10. Su volumen es…"), [("a", "60"), ("b", "16"), ("c", "6"), ("d", "600")]),
     ("D", t("A cylinder has a radius of 2 and a height of 5 (π ≈ 3.14). Its volume is…", "Un cilindro tiene radio 2 y altura 5 (π ≈ 3.14). Su volumen es…"), [("a", "31.4"), ("b", "20"), ("c", "125.6"), ("d", "62.8")]),
     ("E", t("A cylinder has a radius of 3 and a height of 10 (π ≈ 3.14). Its volume is…", "Un cilindro tiene radio 3 y altura 10 (π ≈ 3.14). Su volumen es…"), [("a", "94.2"), ("b", "282.6"), ("c", "90"), ("d", "1,130.4")]),
     ("F", t("What is the formula for the volume of a cylinder?", "¿Cuál es la fórmula del volumen de un cilindro?"), [("a", "V = 2πr"), ("b", "V = πr²"), ("c", "V = πr²h"), ("d", "V = lwh")]),
     ("G", t("A prism has V = 60 and a base with an area of 12. The height is…", "Un prisma tiene V = 60 y una base de área 12. La altura es…"), [("a", "48"), ("b", "72"), ("c", "720"), ("d", "5")]),
     ("H", t("A box has V = 24, a length of 2, and a width of 3. The height is…", "Una caja tiene V = 24, largo 2 y ancho 3. La altura es…"), [("a", "19"), ("b", "4"), ("c", "12"), ("d", "6")])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Find the volume of boxes, prisms, and cylinders with V = area of the base × height, solve for a missing measure, and solve real problems about capacity.", "Calcule el volumen de cajas, prismas y cilindros con V = área de la base × altura, despeje la medida que falta y resuelva problemas reales de capacidad."),
        ("🧮", t("Calculator and reference sheet", "Calculadora y hoja de referencia")),
        [t("<strong>Find</strong> the volume of rectangular and triangular prisms with V = area of the base × height.", "<strong>Calcular</strong> el volumen de prismas rectangulares y triangulares con V = área de la base × altura."),
         t("<strong>Find</strong> the volume of cylinders with V = πr²h.", "<strong>Calcular</strong> el volumen de cilindros con V = πr²h."),
         t("<strong>Identify</strong> the base and the height of each solid.", "<strong>Identificar</strong> correctamente la base y la altura de cada sólido."),
         t("<strong>Solve</strong> for the height or the radius when the volume is known.", "<strong>Despejar</strong> la altura o el radio cuando el volumen es conocido."),
         t("<strong>Give</strong> the answer in the right cubic units (in³, ft³) or in gallons.", "<strong>Expresar</strong> el resultado en las unidades cúbicas correctas (pulg³, pies³) o en galones.")],
        secciones,
        (t("Solve four exercises on the volume of prisms (rectangular and triangular), four on the volume of cylinders (with π ≈ 3.14), and two that solve for the height or the radius. Then check your answers with the calculator's π key: the difference shows how much you rounded.",
           "Resuelva cuatro ejercicios de volumen de prismas (rectangulares y triangulares), cuatro de volumen de cilindros (con π ≈ 3.14) y dos problemas inversos para despejar la altura o el radio. Después compare sus respuestas con la tecla π de la calculadora: la diferencia le dirá cuánto redondeó."),
         t("Find a box and a can at home. Measure the box in inches and find its volume. Measure the diameter and the height of the can, find its volume with V = πr²h, and divide by 231 to get gallons (1 gallon = 231 cubic inches). Compare it with the amount printed on the label.",
           "Busque en su casa una caja y una lata. Mida la caja en pulgadas y calcule su volumen. Mida el diámetro y la altura de la lata, calcule su volumen con V = πr²h y divídalo entre 231 para pasarlo a galones (1 galón = 231 pulgadas cúbicas). Compárelo con la cantidad impresa en la etiqueta.")),
        quiz,
        t("Self-check checklist for volume", "Lista de autoevaluación de volumen"),
        t("Self-check checklist: skills for the volume of prisms and cylinders", "Lista de autoevaluación: destrezas del volumen de prismas y cilindros"),
        [(t("Identifying the base and height", "Identificar base y altura"), t("I identify the base and the height of the solid, in prisms and cylinders in any position.", "Identifico la base y la altura del sólido, en prismas y cilindros en cualquier posición."), t("I identify the base or the height with mistakes.", "Identifico la base o la altura con errores."), t("I confuse the base with the height of the solid.", "Confundo la base con la altura del sólido.")),
         (t("Finding the area of the base", "Calcular el área de la base"), t("I find the area of the base without mistakes, even with πr².", "Calculo el área de la base sin errores, incluso con πr²."), t("I find the area with occasional mistakes.", "Calculo el área con errores ocasionales."), t("I do not find the area of the base.", "No calculo el área de la base.")),
         (t("Using V = area × height", "Aplicar V = área × altura"), t("I use the formula correctly and solve it for a missing measure when needed.", "Aplico la fórmula correctamente y la despejo cuando hace falta."), t("I use the formula with calculation mistakes.", "Aplico la fórmula con errores de cálculo."), t("I do not use the formula correctly.", "No aplico la fórmula correctamente.")),
         (t("Cubic units", "Unidades cúbicas"), t("I give the answer in cubic units and convert to gallons when the problem asks.", "Expreso el resultado en unidades cúbicas y lo paso a galones cuando el problema lo pide."), t("I use wrong or mixed units.", "Uso unidades incorrectas o inconsistentes."), t("I do not give the answer in cubic units.", "No expreso el resultado en unidades cúbicas."))],
        t("<p>In this lesson you found the volume of prisms and cylinders with the central idea V = area of the base × height (and V = πr²h for the cylinder), solved for the height or the radius when they were missing, and used volume in real capacity problems, giving the answer in cubic units.</p>\n<p>In <strong>Lesson 7.2 · Box plots</strong> the topic changes from space to data. You will learn to summarize a data set with five key values (minimum, Q1, median, Q3, and maximum) and to show them in a plot that shows spread and outliers at a glance.</p>",
          "<p>En esta lección se calculó el volumen de prismas y cilindros con la idea central V = área de la base × altura (y V = πr²h para el cilindro), se despejó la altura o el radio cuando faltaban, y se aplicó a problemas reales de capacidad, expresando el resultado en unidades cúbicas.</p>\n<p>En la <strong>Lección 7.2 · Diagramas de caja y bigotes</strong> el tema cambia del espacio a los datos. Se aprenderá a resumir un conjunto de datos con cinco valores clave (mínimo, Q1, mediana, Q3 y máximo) y a representarlos en un diagrama que muestra de un vistazo la dispersión y los valores atípicos.</p>"),
        ("7-2", ("", t("Lesson 7.2 · Box plots", "Lección 7.2 · Diagramas de caja y bigotes"))),
        [(t("volume", "volumen"), t("The amount of space a solid takes up. It is measured in cubic units.", "La cantidad de espacio que ocupa un cuerpo. Se mide en unidades cúbicas.")),
         (t("prism", "prisma"), t("A solid with two equal, parallel bases joined by flat faces, like a box.", "Un cuerpo con dos bases iguales y paralelas unidas por caras planas, como una caja.")),
         (t("cylinder", "cilindro"), t("A solid with two equal, parallel circular bases, like a can.", "Un cuerpo con dos bases circulares iguales y paralelas, como una lata.")),
         (t("radius", "radio"), t("The distance from the center of a circle to its edge: half the diameter.", "La distancia del centro de un círculo a su borde: la mitad del diámetro.")),
         (t("cubic unit", "unidad cúbica"), t("A cube that measures 1 unit on each side, like 1 in³ or 1 ft³.", "Un cubo que mide 1 unidad por lado, como 1 pulg³ o 1 pie³."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var UN = {in: T("inches", "pulgadas"), ft: T("feet", "pies"), in3: T("cubic inches", "pulgadas cúbicas"), ft3: T("cubic feet", "pies cúbicos"), gal: T("gallons", "galones")};
/* MODULE 1 · A box in layers, in perspective */
function pintaCaja(){
  var l = +$("cj-l").value, w = +$("cj-w").value, h = +$("cj-h").value, g = rad(+$("cj-g").value), phi = rad(28);
  ["l", "w", "h"].forEach(function(k){ $("cj-" + k + "v").textContent = $("cj-" + k).value; }); $("cj-gv").textContent = $("cj-g").value + "°";
  var cg = Math.cos(g), sg = Math.sin(g), cp = Math.cos(phi), sp = Math.sin(phi);
  function prj(p){ var x = p[0] - l / 2, y = p[1] - w / 2, z = p[2]; var xr = x * cg - y * sg, yr = x * sg + y * cg; return [xr, z * cp + yr * sp]; }
  var caras = [
    {n: [0, -1, 0], p: function(u, v){ return [u, 0, v]; }, U: l, V: h, col: "#b8c4ca"},
    {n: [0, 1, 0], p: function(u, v){ return [u, w, v]; }, U: l, V: h, col: "#b8c4ca"},
    {n: [-1, 0, 0], p: function(u, v){ return [0, u, v]; }, U: w, V: h, col: "#80deea"},
    {n: [1, 0, 0], p: function(u, v){ return [l, u, v]; }, U: w, V: h, col: "#80deea"},
    {n: [0, 0, 1], p: function(u, v){ return [u, v, h]; }, U: l, V: w, col: "#cfd8dc"},
    {n: [0, 0, -1], p: function(u, v){ return [u, v, 0]; }, U: l, V: w, col: "#cfd8dc"}];
  var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
  caras.forEach(function(c){ [[0, 0], [c.U, 0], [c.U, c.V], [0, c.V]].forEach(function(q){ var p = prj(c.p(q[0], q[1])); minX = Math.min(minX, p[0]); maxX = Math.max(maxX, p[0]); minY = Math.min(minY, p[1]); maxY = Math.max(maxY, p[1]); }); });
  var esc = Math.min(420 / (maxX - minX), 260 / (maxY - minY)), ox = 320 - (minX + maxX) / 2 * esc, oy = 150 + (minY + maxY) / 2 * esc;
  function V(p){ var q = prj(p); return [ox + q[0] * esc, oy - q[1] * esc]; }
  var s = '<svg class="geo-svg" viewBox="0 0 640 300" role="img" aria-label="' + T("A box " + l + " by " + w + " by " + h + " small cubes: " + (l * w * h) + " in all.", "Caja de " + l + " por " + w + " por " + h + " cubitos: " + (l * w * h) + " en total.") + '">';
  caras.forEach(function(c){
    var yr = c.n[0] * sg + c.n[1] * cg, d = yr * cp - c.n[2] * sp;
    if (!(d < 0)) return;
    var pts = [[0, 0], [c.U, 0], [c.U, c.V], [0, c.V]].map(function(q){ return V(c.p(q[0], q[1])); });
    s += '<polygon points="' + pts.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="' + c.col + '" stroke="#37474f" stroke-width="2.5"/>';
    for (var u = 1; u < c.U; u++) s += lineaG(V(c.p(u, 0)), V(c.p(u, c.V)), "#00838f", 1);
    for (var v = 1; v < c.V; v++) s += lineaG(V(c.p(0, v)), V(c.p(c.U, v)), "#00838f", 1);
  });
  $("cj-svg").innerHTML = s + "</svg>";
  $("cj-salida").innerHTML = '<div class="linea">' + T("One layer (the base) has " + l + " × " + w + " = " + (l * w) + " small cubes: that is the area of the base.", "Una capa (la base) tiene " + l + " × " + w + " = " + (l * w) + " cubitos: es el área de la base.") + "</div>" +
    '<div class="linea">' + T("There " + (h === 1 ? "is 1 layer" : "are " + h + " layers") + ": ", "Hay " + h + (h === 1 ? " capa" : " capas") + ": ") + (l * w) + " × " + h + " = <strong>" + (l * w * h) + "</strong>" + T(" small cubes.", " cubitos.") + "</div>" +
    '<div class="linea veredicto">V = ' + l + " × " + w + " × " + h + " = " + (l * w * h) + T(" cubic units", " unidades cúbicas") + "</div>";
}
function genPrisma(){
  var tp = aleatorio(1, 3), o, pc = {};
  if (tp === 1){ var l = aleatorio(2, 9), w = aleatorio(2, 8), h = aleatorio(2, 9), V = l * w * h;
    o = [opN(V), opN(l + w + h), opN(l * w), opN(2 * (l * w + l * h + w * h))]; pc["n" + (l + w + h)] = T("Multiply the measures; do not add them.", "Las medidas se multiplican, no se suman."); pc["n" + (l * w)] = T("That is the area of the base: multiply by the height too.", "Ese es el área de la base: falta multiplicar por la altura."); pc["n" + 2 * (l * w + l * h + w * h)] = T("That is the surface area, not the volume.", "Esa es el área de la superficie, no el volumen.");
    return {enun: T("A box is " + l + " inches long, " + w + " inches wide, and " + h + " inches high. What is its volume in cubic inches?", "Una caja mide " + l + " pulgadas de largo, " + w + " de ancho y " + h + " de alto. ¿Cuál es su volumen en pulgadas cúbicas?"), opciones: o, correcta: "n" + V, porClave: pc,
      pista: T("Volume of a box: length × width × height.", "Volumen de una caja: largo × ancho × alto."), bien: l + " × " + w + " × " + h + " = " + V + T(" in³.", " pulg³."), mal: "V = " + l + " × " + w + " × " + h + " = " + V + T(" in³.", " pulg³.")}; }
  if (tp === 2){ var a = aleatorio(2, 9), V2 = a * a * a;
    o = [opN(V2), opN(a * a), opN(3 * a), opN(6 * a * a)]; pc["n" + a * a] = T("That is the area of one face.", "Eso es el área de una cara."); pc["n" + 3 * a] = T("Multiply the side by itself three times; do not multiply by 3.", "Se multiplica el lado tres veces por sí mismo, no por 3."); pc["n" + 6 * a * a] = T("That is the surface area of the cube.", "Esa es el área de la superficie del cubo.");
    return {enun: T("What is the volume of a cube with sides of " + a + " inches?", "¿Cuál es el volumen de un cubo de " + a + " pulgadas de lado?"), opciones: o, correcta: "n" + V2, porClave: pc,
      pista: T("A cube is a box whose length, width, and height are equal.", "Un cubo es una caja con el largo, el ancho y el alto iguales."), bien: a + " × " + a + " × " + a + " = " + V2 + T(" in³.", " pulg³."), mal: "V = " + a + "³ = " + V2 + T(" in³.", " pulg³.")}; }
  var b = aleatorio(2, 8) * 2, ht = aleatorio(2, 7), L = aleatorio(3, 12), A = b * ht / 2, V3 = A * L;
  o = [opN(V3), opN(b * ht * L), opN(A), opN(b + ht + L)]; pc["n" + b * ht * L] = T("The area of the triangle is base × height ÷ 2: you forgot to divide by 2.", "El área del triángulo es base × altura ÷ 2: faltó dividir entre 2."); pc["n" + A] = T("That is the area of the base. Multiply by the length of the prism.", "Ese es el área de la base. Falta multiplicar por el largo del prisma.");
  return {enun: T("A prism has a triangular base with a base of " + b + " inches and a height of " + ht + " inches, and the prism is " + L + " inches long. What is its volume in cubic inches?", "Un prisma tiene como base un triángulo de base " + b + " pulgadas y altura " + ht + " pulgadas, y mide " + L + " pulgadas de largo. ¿Cuál es su volumen en pulgadas cúbicas?"), opciones: o, correcta: "n" + V3, porClave: pc,
    pista: T("First the area of the triangle (base × height ÷ 2), then times the length.", "Primero el área del triángulo (base × altura ÷ 2) y después por el largo."),
    bien: T("Area of the base: ", "Área de la base: ") + b + " × " + ht + " ÷ 2 = " + A + T(". Volume: ", ". Volumen: ") + A + " × " + L + " = " + V3 + T(" in³.", " pulg³."), mal: T("Area of the base: ", "Área de la base: ") + b + " × " + ht + " ÷ 2 = " + A + "; V = " + A + " × " + L + " = " + V3 + T(" in³.", " pulg³.")};
}

/* MODULE 2 · Cylinder */
function pintaCil(){
  var r = +$("ci-r").value, h = +$("ci-h").value;
  $("ci-rv").textContent = nm(r); $("ci-hv").textContent = nm(h);
  var esc = Math.min(160 / r, 220 / h, 40), R = r * esc, Hh = h * esc, cx = 300, yt = 150 - Hh / 2, yb = 150 + Hh / 2, ry = Math.max(R * 0.3, 6);
  var s = '<svg class="geo-svg" viewBox="0 0 640 310" role="img" aria-label="' + T("Cylinder with radius " + nm(r) + " and height " + nm(h) + ".", "Cilindro de radio " + nm(r) + " y altura " + nm(h) + ".") + '">';
  s += '<path d="M' + f1(cx - R) + " " + f1(yt) + " L" + f1(cx - R) + " " + f1(yb) + " A" + f1(R) + " " + f1(ry) + " 0 0 0 " + f1(cx + R) + " " + f1(yb) + " L" + f1(cx + R) + " " + f1(yt) + '" fill="#b8c4ca" stroke="#37474f" stroke-width="2.5"/>';
  s += '<path d="M' + f1(cx - R) + " " + f1(yb) + " A" + f1(R) + " " + f1(ry) + " 0 0 1 " + f1(cx + R) + " " + f1(yb) + '" fill="none" stroke="#37474f" stroke-width="1.5" stroke-dasharray="5 4"/>';
  s += '<ellipse cx="' + cx + '" cy="' + f1(yt) + '" rx="' + f1(R) + '" ry="' + f1(ry) + '" fill="#cfd8dc" stroke="#37474f" stroke-width="2.5"/>';
  s += lineaG([cx, yt], [cx + R, yt], "#b71c1c", 3) + textoA([cx + R / 2, yt - ry - 10], "r = " + nm(r), 18, "#b71c1c");
  s += lineaG([cx + R + 22, yt], [cx + R + 22, yb], "#0d47a1", 2) + textoA([cx + R + 30, (yt + yb) / 2], "h = " + nm(h), 18, "#0d47a1", 700, "start");
  $("ci-svg").innerHTML = s + "</svg>";
  var rr = r * r, base = PI * rr, V = base * h;
  $("ci-salida").innerHTML = '<div class="linea">' + T("First the radius squared: r² = ", "Primero el radio al cuadrado: r² = ") + nm(r) + "² = " + nm(rr) + ".</div>" +
    '<div class="linea">' + T("Area of the base: ", "Área de la base: ") + "π × " + nm(rr) + " ≈ 3.14 × " + nm(rr) + " = " + nm(r2(base)) + ".</div>" +
    '<div class="linea">' + T("Times the height: ", "Por la altura: ") + nm(r2(base)) + " × " + nm(h) + " ≈ <strong>" + nm(r2(V)) + "</strong>.</div>" +
    '<div class="linea veredicto">V = ' + nm(rr * h) + "π " + T("(exact)", "(exacto)") + " ≈ " + nm(r1(V)) + T(" cubic units", " unidades cúbicas") + "</div>";
}
function genCilindro(){
  var r = aleatorio(1, 9), h = aleatorio(2, 12), diam = Math.random() < 0.3, k = r * r * h;
  var enun = T("A cylinder has " + (diam ? "a diameter of " + (2 * r) : "a radius of " + r) + " inches and a height of " + h + " inches. What is its volume in cubic inches?", "Un cilindro tiene " + (diam ? "un diámetro de " + (2 * r) : "un radio de " + r) + " pulgadas y una altura de " + h + " pulgadas. ¿Cuál es su volumen en pulgadas cúbicas?");
  var pistas = [{v: 3.14 * r * h, msg: T("You forgot to square the radius.", "Faltó elevar el radio al cuadrado.")}, {v: 3.14 * 2 * r * h, msg: T("That looks like the lateral area (2πrh), not the volume.", "Eso se parece al área lateral (2πrh), no al volumen.")}, {v: r1(3.14 * r * r), msg: T("That is the area of the base: multiply by the height too.", "Ese es el área de la base: falta multiplicar por la altura.")}];
  if (diam) pistas.unshift({v: 3.14 * 4 * r * r * h, msg: T("You used the diameter as the radius: divide it by 2 first.", "Se usó el diámetro como radio: primero hay que dividirlo entre 2.")}, {v: 4 * r * r * h * Math.PI, msg: T("You used the diameter as the radius: divide it by 2 first.", "Se usó el diámetro como radio: primero hay que dividirlo entre 2.")});
  return {enun: enun, solucion: (diam ? T("The radius is ", "El radio es ") + (2 * r) + " ÷ 2 = " + r + ". " : "") + "V = π × " + r + "² × " + h + " = " + k + "π ≈ " + nm(r1(3.14 * k)) + T(" in³.", " pulg³."),
    evalua: function(v){ return evaluaPi(v, k, pistas); }};
}

/* MODULE 3 · Solving */
function problemaDespeje(tp){
  if (tp === undefined) tp = aleatorio(1, 4);
  if (tp === 1){ var A = aleatorio(4, 30), h = aleatorio(2, 12), V = A * h;
    return {txt: T("A prism has a volume of " + V + " cubic inches and a base with an area of " + A + " square inches. What is its height, in inches?", "Un prisma tiene un volumen de " + V + " pulgadas cúbicas y una base de área " + A + " pulgadas cuadradas. ¿Cuál es su altura, en pulgadas?"), res: h, mal: [{v: V * A, msg: T("You multiplied. To solve for the height, divide.", "Multiplicó. Para despejar la altura se divide.")}, {v: V - A, msg: T("You subtracted. Divide the volume by the area of the base.", "Restó. Hay que dividir el volumen entre el área de la base.")}],
      pasos: [T("Start from V = area of the base × height: ", "Se parte de V = área de la base × altura: ") + V + " = " + A + " × h.", T("Divide both sides by " + A + ": h = ", "Se divide entre " + A + " en ambos lados: h = ") + V + " ÷ " + A + ".", '<span class="veredicto">h = ' + h + " " + UN.in + "</span>"]}; }
  if (tp === 2){ var l = aleatorio(2, 10), w = aleatorio(2, 8), hh = aleatorio(2, 9), V2 = l * w * hh;
    return {txt: T("A box has a volume of " + V2 + " cubic inches, a length of " + l + " inches, and a width of " + w + " inches. What is its height, in inches?", "Una caja tiene un volumen de " + V2 + " pulgadas cúbicas, un largo de " + l + " pulgadas y un ancho de " + w + " pulgadas. ¿Cuál es su altura, en pulgadas?"), res: hh, mal: [{v: V2 / l, msg: T("Divide by the whole base, " + l + " × " + w + ", not only by the length.", "Se divide entre toda la base, " + l + " × " + w + ", no solo entre el largo.")}, {v: V2 / w, msg: T("Divide by the whole base, " + l + " × " + w + ", not only by the width.", "Se divide entre toda la base, " + l + " × " + w + ", no solo entre el ancho.")}],
      pasos: [T("The area of the base is ", "El área de la base es ") + l + " × " + w + " = " + (l * w) + T(" square inches.", " pulgadas cuadradas."), T("Divide the volume by the area of the base: h = ", "Se divide el volumen entre el área de la base: h = ") + V2 + " ÷ " + (l * w) + ".", '<span class="veredicto">h = ' + hh + " " + UN.in + "</span>"]}; }
  if (tp === 3){ var r = aleatorio(1, 6), hc = aleatorio(2, 10), V3 = r2(3.14 * r * r * hc);
    return {txt: T("A cylinder has a volume of " + nm(V3) + " cubic inches and a radius of " + r + " inches. What is its height, in inches? (π ≈ 3.14)", "Un cilindro tiene un volumen de " + nm(V3) + " pulgadas cúbicas y un radio de " + r + " pulgadas. ¿Cuál es su altura, en pulgadas? (π ≈ 3.14)"), res: hc, mal: [{v: V3 / (3.14 * r), msg: T("Square the radius before you divide: the base is π × r².", "Eleve el radio al cuadrado antes de dividir: la base es π × r².")}],
      pasos: [T("The area of the base is ", "El área de la base es ") + "3.14 × " + r + "² = 3.14 × " + (r * r) + " = " + nm(r2(3.14 * r * r)) + T(" square inches.", " pulgadas cuadradas."), T("Divide the volume by the area of the base: h = ", "Se divide el volumen entre el área de la base: h = ") + nm(V3) + " ÷ " + nm(r2(3.14 * r * r)) + ".", '<span class="veredicto">h = ' + hc + " " + UN.in + "</span>"]}; }
  var rr = aleatorio(2, 7), h4 = aleatorio(2, 10), V4 = r2(3.14 * rr * rr * h4);
  return {txt: T("A cylinder has a volume of " + nm(V4) + " cubic inches and a height of " + h4 + " inches. What is its radius, in inches? (π ≈ 3.14)", "Un cilindro tiene un volumen de " + nm(V4) + " pulgadas cúbicas y una altura de " + h4 + " pulgadas. ¿Cuál es su radio, en pulgadas? (π ≈ 3.14)"), res: rr, mal: [{v: rr * rr, msg: T("That is r². Take the square root.", "Ese es r². Falta sacar la raíz cuadrada.")}],
    pasos: [T("Divide the volume by πh: r² = ", "Se divide el volumen entre πh: r² = ") + nm(V4) + " ÷ (3.14 × " + h4 + ") = " + nm(V4) + " ÷ " + nm(r2(3.14 * h4)) + " = " + (rr * rr) + ".", T("Take the square root: r = ", "Se saca la raíz cuadrada: r = ") + "√" + (rr * rr) + ".", '<span class="veredicto">r = ' + rr + " " + UN.in + "</span>"]};
}
var DJ_COLA = [1, 3, 4];
function nuevoDJ(){ var q = problemaDespeje(DJ_COLA.length ? DJ_COLA.shift() : undefined); $("dj-enun").textContent = q.txt; DJS.carga(q.pasos); }
function genDespeje(){
  var q = problemaDespeje();
  return {enun: q.txt, solucion: q.pasos.map(function(p){ return p.replace(/<[^>]+>/g, ""); }).join(" "),
    evalua: function(v){ var r = evaluaDec(v, q.res, q.mal, 0.051); if (r.estado === "mal" && !q.mal.some(function(p){ return p.msg === r.msg; })) r.msg = T("Divide the volume by the area of the base.", "Divida el volumen entre el área de la base."); return r; }};
}

/* MODULE 4 · Capacity */
function genCapacidad(){
  var tp = aleatorio(1, 5), enun, res, sol, pistas = [];
  if (tp === 1){ var r = elige([1, 1.5, 2, 2.5, 3]), h = elige([2, 3, 4, 5, 6]), V = 3.14 * r * r * h; res = Math.round(V * 7.48);
    enun = T("A cylindrical tank has a radius of " + nm(r) + " feet and a height of " + h + " feet. About how many gallons of water fit? (π ≈ 3.14; 1 cubic foot ≈ 7.48 gallons)", "Un tanque cilíndrico tiene un radio de " + nm(r) + " pies y una altura de " + h + " pies. ¿Cuántos galones de agua caben, aproximadamente? (π ≈ 3.14; 1 pie cúbico ≈ 7.48 galones)");
    sol = "V = 3.14 × " + nm(r) + "² × " + h + " ≈ " + nm(r2(V)) + T(" cubic feet; × 7.48 ≈ " + res + " gallons.", " pies cúbicos; × 7.48 ≈ " + res + " galones."); pistas.push({v: V, tol: 0.6, msg: T("That is the volume in cubic feet. Now convert it to gallons.", "Ese es el volumen en pies cúbicos. Falta pasarlo a galones.")}); }
  else if (tp === 2){ var l = elige([20, 24, 30, 36]), w = elige([10, 12, 15]), hh = elige([12, 16, 18, 20]), Vi = l * w * hh; res = Math.round(Vi / 231);
    enun = T("A fish tank is " + l + " inches long, " + w + " inches wide, and " + hh + " inches high. About how many gallons fit? (1 gallon = 231 cubic inches)", "Una pecera mide " + l + " pulgadas de largo, " + w + " de ancho y " + hh + " de alto. ¿Cuántos galones caben, aproximadamente? (1 galón = 231 pulgadas cúbicas)");
    sol = "V = " + l + " × " + w + " × " + hh + " = " + com(Vi) + T(" cubic inches; ", " pulgadas cúbicas; ") + com(Vi) + " ÷ 231 ≈ " + res + T(" gallons.", " galones."); pistas.push({v: Vi, msg: T("That is the volume in cubic inches. Divide by 231 to get gallons.", "Ese es el volumen en pulgadas cúbicas. Divida entre 231 para pasarlo a galones.")}); }
  else if (tp === 3){ var L = elige([10, 12, 15, 20]), A = elige([5, 6, 8]), P = elige([1, 1.5, 2]), Vp = L * A * P; res = Math.round(Vp * 7.48);
    enun = T("A rectangular wading pool is " + L + " feet long, " + A + " feet wide, and " + nm(P) + " feet deep. About how many gallons fit? (1 cubic foot ≈ 7.48 gallons)", "Una piscina rectangular para niños mide " + L + " pies de largo, " + A + " de ancho y " + nm(P) + " de profundidad. ¿Cuántos galones caben, aproximadamente? (1 pie cúbico ≈ 7.48 galones)");
    sol = "V = " + L + " × " + A + " × " + nm(P) + " = " + nm(Vp) + T(" cubic feet; × 7.48 ≈ " + res + " gallons.", " pies cúbicos; × 7.48 ≈ " + res + " galones."); pistas.push({v: Vp, msg: T("That is the volume in cubic feet. Multiply by 7.48 to get gallons.", "Ese es el volumen en pies cúbicos. Multiplique por 7.48 para pasarlo a galones.")}); }
  else if (tp === 4){ var rc = elige([6, 9, 12]), hm = elige([8, 9, 10, 12]), Vc = 3.14 * (rc / 12) * (rc / 12) * hm; res = Math.round(Vc);
    enun = T("A cylindrical concrete column has a radius of " + rc + " inches and a height of " + hm + " feet. About how many cubic feet of concrete does it take? (π ≈ 3.14; change the radius to feet first)", "Una columna cilíndrica de concreto tiene un radio de " + rc + " pulgadas y una altura de " + hm + " pies. ¿Cuántos pies cúbicos de concreto lleva, aproximadamente? (π ≈ 3.14; primero pase el radio a pies)");
    sol = T("The radius is " + rc + " inches = " + nm(rc / 12) + " feet. ", "El radio es " + rc + " pulgadas = " + nm(rc / 12) + " pies. ") + "V = 3.14 × " + nm(rc / 12) + "² × " + hm + " ≈ " + nm(r2(Vc)) + T(" cubic feet, about " + res + ".", " pies cúbicos, unos " + res + "."); pistas.push({v: 3.14 * rc * rc * hm, tol: 1, msg: T("The radius is in inches and the height in feet. Change the radius to feet first: divide by 12.", "El radio está en pulgadas y la altura en pies. Primero pase el radio a pies: divida entre 12.")}); }
  else { var lc = elige([24, 36, 48]), wc = elige([12, 18, 24]), hc = elige([12, 18, 24]), Vl = lc * wc * hc; res = Math.round(Vl / 1728);
    enun = T("A storage box is " + lc + " inches long, " + wc + " inches wide, and " + hc + " inches high. About how many cubic feet does it hold? (1 cubic foot = 1,728 cubic inches)", "Una caja para guardar cosas mide " + lc + " pulgadas de largo, " + wc + " de ancho y " + hc + " de alto. ¿Cuántos pies cúbicos le caben, aproximadamente? (1 pie cúbico = 1,728 pulgadas cúbicas)");
    sol = "V = " + lc + " × " + wc + " × " + hc + " = " + com(Vl) + T(" cubic inches; ÷ 1,728 = ", " pulgadas cúbicas; ÷ 1,728 = ") + nm(r2(Vl / 1728)) + T(" cubic feet, about " + res + ".", " pies cúbicos, unos " + res + "."); pistas.push({v: Vl, msg: T("That is the volume in cubic inches. Divide by 1,728 to get cubic feet.", "Ese es el volumen en pulgadas cúbicas. Divida entre 1,728 para pasarlo a pies cúbicos.")}, {v: Vl / 12, tol: 1, msg: T("A cubic foot is 12 × 12 × 12 = 1,728 cubic inches, not 12.", "Un pie cúbico son 12 × 12 × 12 = 1,728 pulgadas cúbicas, no 12.")}); }
  var tol = Math.max(0.6, res * 0.01);
  return {enun: enun, solucion: sol, evalua: function(v){ var r = evaluaDec(v, res, pistas, tol); if (r.estado === "mal" && !pistas.some(function(p){ return p.msg === r.msg; })) r.msg = T("Find the volume first, then use the conversion in the problem.", "Calcule primero el volumen y después use la equivalencia del problema."); return r; }};
}

/* Start */
["cj-l", "cj-w", "cj-h", "cj-g"].forEach(function(id){ $(id).addEventListener("input", pintaCaja); }); pintaCaja();
OMR("p1", genPrisma);
["ci-r", "ci-h"].forEach(function(id){ $(id).addEventListener("input", pintaCil); }); pintaCil();
creaPracticaLibre("p2", genCilindro);
var DJS = pasoAPaso("dj", []);
$("dj-nuevo").addEventListener("click", nuevoDJ); nuevoDJ();
creaPracticaLibre("p3", genDespeje);
creaPracticaLibre("p4", genCapacidad);
'''

def practica_pagina():
    n = N
    def libre(pid, tit, et, nota):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota}</p>\n        <div class="fila-btn">', 1)
    def rango(i, et, v, mn, mx, st=1, mw=150):
        return f'<div class="campo" style="flex:1;min-width:{mw}px;"><label for="{i}">{et} <span id="{i}v"></span></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    mods = [
     (t("prisms", "prismas"), t("Volume of prisms", "Volumen de prismas"),
      f'''      <p>{t("Volume is the space an object takes up. For prisms and cylinders it is always found with the same idea: the area of the base times the height. The answer is in cubic units (in³, ft³).", "El volumen es el espacio que ocupa un cuerpo. Para prismas y cilindros se calcula siempre con la misma idea: el área de la base multiplicada por la altura. El resultado va en unidades cúbicas (pulg³, pies³).")}</p>
{n3.formula(t("V = area of the base × height", "V = área de la base × altura"))}
      <h3>{t("The box in layers", "La caja por capas")}</h3>
      <p>{t("Each small cube measures 1 unit on each side. The base has length × width small cubes, and you stack as many layers as the height says. Turn the box to see it from another side.", "Cada cubito mide 1 unidad por lado. La base tiene largo × ancho cubitos, y se apilan tantas capas como indica la altura. Gire la caja para verla desde otro lado.")}</p>
      <div class="panel"><div class="campos">
        {rango("cj-l", t("Length:", "Largo:"), 5, 1, 7)}
        {rango("cj-w", t("Width:", "Ancho:"), 3, 1, 6)}
        {rango("cj-h", t("Height:", "Alto:"), 4, 1, 6)}
        {rango("cj-g", t("Turn:", "Girar:"), 30, 10, 80)}</div></div>
      <div id="cj-svg"></div>
{n3.salida("cj-salida")}
      <div class="caja-tip">{t("<strong>Triangular prism:</strong> the base is a triangle. First find its area (base × height ÷ 2), then multiply by the length of the prism.", "<strong>Prisma triangular:</strong> la base es un triángulo. Primero se calcula su área (base × altura ÷ 2) y después se multiplica por el largo del prisma.")}</div>
{B.om("p1", t("Practice: volume of prisms", "Practique: volumen de prismas"))}'''),
     (t("cylinders", "cilindros"), t("Volume of cylinders", "Volumen de cilindros"),
      f'''      <p>{t("In a cylinder, the base is a circle with radius r, and its area is πr². So:", "En un cilindro la base es un círculo de radio r, cuya área es πr². Por eso:")}</p>
{n3.formula("V = πr²h")}
      <p>{t("Use π ≈ 3.14 or the π key on the calculator. You can also leave the answer <strong>exact</strong>, with π: for example, 20π.", "Se usa π ≈ 3.14 o la tecla π de la calculadora. También se puede dejar el resultado <strong>exacto</strong>, con π: por ejemplo, 20π.")}</p>
      <h3>{t("Cylinder calculator", "Calculadora del cilindro")}</h3>
      <div class="panel"><div class="campos">
        {rango("ci-r", t("Radius:", "Radio:"), 2, 0.5, 6, 0.5, 180)}
        {rango("ci-h", t("Height:", "Altura:"), 5, 1, 12, 0.5, 180)}</div></div>
      <div id="ci-svg"></div>
{n3.salida("ci-salida")}
{n3.atencion(t("Square only the radius:", "Solo el radio va al cuadrado:"), t("in πr²h the exponent applies only to r. And if the problem gives the <strong>diameter</strong>, divide it by 2 first to get the radius.", "en πr²h el exponente afecta únicamente a r. Y si el problema da el <strong>diámetro</strong>, primero se divide entre 2 para obtener el radio."))}
{libre("p2", t("Practice: volume of a cylinder", "Practique: volumen de un cilindro"), t("Volume", "Volumen"), t("Use π ≈ 3.14 and round to the nearest tenth, or type the exact answer with π, like 20π.", "Use π ≈ 3.14 y redondee a la décima, o escriba el resultado exacto con π, como 20π."))}'''),
     (t("solve", "despejar"), t("Solving for the height or the radius", "Despejar la altura o el radio"),
      f'''      <p>{t("If you know the volume and one measure is missing, solve for it as in Topic 5: the height is the volume divided by the area of the base. For the radius of a cylinder, divide by πh and then take the square root.", "Si se conoce el volumen y falta una medida, se despeja como en el Tema 5: la altura es el volumen dividido entre el área de la base. Para el radio de un cilindro, se divide entre πh y después se saca la raíz cuadrada.")}</p>
{n3.formula("h = " + '<span class="fracc"><span class="fa">V</span><span class="fb2">' + t("area of the base", "área de la base") + '</span></span>' + "&nbsp;&nbsp;&nbsp;&nbsp; r = √" + '<span class="fracc"><span class="fa">V</span><span class="fb2">πh</span></span>')}
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <p class="enun" id="dj-enun"></p>
        <div class="fila-btn"><button type="button" class="btn" id="dj-sig"></button><button type="button" class="btn-sec" id="dj-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="dj-nuevo">{t("Another example", "Otro ejemplo")}</button></div>
      </div>
      <div class="pasos" id="dj-pasos" aria-live="polite"></div>
{libre("p3", t("Practice: find the missing measure", "Practique: halle la medida que falta"), t("Measure", "Medida"), t("Type the number; if it is not exact, round to the nearest tenth.", "Escriba el número; si no es exacto, redondee a la décima."))}'''),
     (t("capacity", "capacidad"), t("Capacity and storage", "Capacidad y almacenamiento"),
      f'''      <p>{t("Volume answers real questions: how much water fits in a tank, or how much concrete a column takes. To go from volume to capacity, use these facts:", "El volumen responde preguntas reales: cuánta agua cabe en un tanque o cuánto concreto lleva una columna. Para pasar de volumen a capacidad se usan estas equivalencias:")}</p>
      <table class="reglas"><caption>{t("Volume and capacity facts", "Equivalencias entre volumen y capacidad")}</caption>
        <thead><tr><th scope="col">{t("Volume", "Volumen")}</th><th scope="col">{t("Equals", "Equivale a")}</th></tr></thead>
        <tbody><tr><td>{t("1 cubic foot", "1 pie cúbico")}</td><td>{t("1,728 cubic inches (12 × 12 × 12)", "1,728 pulgadas cúbicas (12 × 12 × 12)")}</td></tr>
        <tr><td>{t("1 cubic foot", "1 pie cúbico")}</td><td>{t("about 7.48 gallons", "unos 7.48 galones")}</td></tr>
        <tr><td>{t("231 cubic inches", "231 pulgadas cúbicas")}</td><td>{t("1 gallon", "1 galón")}</td></tr>
        <tr><td>{t("1 cubic yard", "1 yarda cúbica")}</td><td>{t("27 cubic feet (3 × 3 × 3)", "27 pies cúbicos (3 × 3 × 3)")}</td></tr></tbody></table>
      <div class="caja-tip">{t("<strong>Every measure in the same unit:</strong> if the radius is in inches and the height is in feet, convert everything to one unit first.", "<strong>Todas las medidas en la misma unidad:</strong> si el radio está en pulgadas y la altura en pies, primero se convierte todo a una sola unidad.")}</div>
{libre("p4", t("Practice: capacity problems", "Practique: problemas de capacidad"), t("Result", "Resultado"), t("Round to the nearest whole number.", "Redondee al número entero más cercano."))}''')]
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Volumen de prismas y cilindros")
