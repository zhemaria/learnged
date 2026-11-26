"""Level 4 · Lesson 2.1 · Volume of spheres, cones, and pyramids — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_2-1.html, algebra/n4-l2-1.html (the formula sheet and the three solids, the sphere)
and geometria/vol_esfera, vol_cono, vol_piramide (the three workshops with their challenge). All of them are rebuilt here, inside LearnGED,
with US units. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n4

B.NIVEL = 4
N = "2-1"
TEMA = ("3D volume and polynomials", "Volumen 3D y polinomios")
TIT = ("Volume of spheres, cones, and pyramids", "Volumen de esferas, conos y pirámides")
SCRIPTS = n4.SCRIPTS + ("/math/solid4.js",)

def fig_solidos():
    L, R, A = "#37474f", "#c62828", "#1565c0"
    s = []
    # sphere
    s.append(f'<circle cx="100" cy="110" r="70" fill="#e3f2fd" stroke="{L}" stroke-width="2.5"/><path d="M30 110 A70 17 0 0 0 170 110" fill="none" stroke="{L}" stroke-width="2"/><path d="M30 110 A70 17 0 0 1 170 110" fill="none" stroke="#90a4ae" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(f'<line x1="100" y1="110" x2="170" y2="110" stroke="{R}" stroke-width="3"/><text x="178" y="116" font-size="16" font-weight="700" fill="{R}">r</text>')
    s.append('<text x="100" y="215" font-size="16" font-weight="700" fill="#10174f" text-anchor="middle">V = 4/3 πr³</text>')
    # cone
    s.append(f'<path d="M230 170 L300 40 L370 170 A70 16 0 0 1 230 170 Z" fill="#e3f2fd" stroke="{L}" stroke-width="2.5"/><path d="M230 170 A70 16 0 0 1 370 170" fill="none" stroke="#90a4ae" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(f'<line x1="300" y1="40" x2="300" y2="170" stroke="{A}" stroke-width="3" stroke-dasharray="7 5"/><line x1="300" y1="170" x2="370" y2="170" stroke="{R}" stroke-width="3"/><text x="290" y="110" font-size="16" font-weight="700" fill="{A}" text-anchor="end">h</text><text x="335" y="195" font-size="16" font-weight="700" fill="{R}" text-anchor="middle">r</text>')
    s.append('<text x="300" y="215" font-size="16" font-weight="700" fill="#10174f" text-anchor="middle">V = 1/3 πr²h</text>')
    # pyramid
    s.append('<polygon points="430,175 540,175 500,40" fill="#e3f2fd" stroke="#37474f" stroke-width="2.5"/><polygon points="540,175 575,150 500,40" fill="#bbdefb" stroke="#37474f" stroke-width="2.5"/>')
    s.append('<line x1="430" y1="175" x2="465" y2="150" stroke="#90a4ae" stroke-width="2" stroke-dasharray="6 5"/><line x1="465" y1="150" x2="575" y2="150" stroke="#90a4ae" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(f'<line x1="500" y1="40" x2="502" y2="162" stroke="{A}" stroke-width="3" stroke-dasharray="7 5"/><text x="492" y="110" font-size="16" font-weight="700" fill="{A}" text-anchor="end">h</text>')
    s.append('<text x="505" y="215" font-size="16" font-weight="700" fill="#10174f" text-anchor="middle">V = 1/3 Bh</text>')
    return B.svg("0 0 600 230", t("Three solids. A sphere with its radius r: V = 4/3 πr³. A cone with its radius r and height h: V = 1/3 πr²h. A pyramid with its height h: V = 1/3 Bh, where B is the area of the base.",
                                  "Tres sólidos. Una esfera con su radio r: V = 4/3 πr³. Un cono con su radio r y su altura h: V = 1/3 πr²h. Una pirámide con su altura h: V = 1/3 Bh, donde B es el área de la base."), "".join(s), 600)

def leccion():
    n = N
    hoja = t("<strong>Reference sheet</strong> button at the top of every lesson", "botón <strong>Hoja de referencia</strong>, arriba en cada lección")
    s1 = f'''<p>{t("<strong>A link with Topic 1.</strong> In Topic 1 you measured distances and figures on the plane (two dimensions). Now you move to <strong>space</strong> (three dimensions). You already know the volume of prisms and cylinders from Level 3; this lesson adds three new solids: the sphere, the cone, and the pyramid. From this topic on, always work with the <strong>formula sheet</strong>, the same kind you get on test day.",
 "<strong>Conexión con el tema anterior.</strong> En el Tema 1 se midieron distancias y figuras en el plano (dos dimensiones). Ahora se pasa al <strong>espacio</strong> (tres dimensiones). Los volúmenes de prismas y cilindros ya se conocen del Nivel 3; esta lección añade tres sólidos nuevos: la esfera, el cono y la pirámide. A partir de este tema se trabaja siempre con la <strong>hoja de fórmulas</strong>, la misma que se recibe el día del examen.")}</p>
<p>{t(f"On the GED test you do not memorize the volume formulas: you get them on a formula sheet. The skill that is tested is <strong>finding the right formula</strong>, substituting the measures correctly, and calculating. On this site, the formula sheet opens with the {hoja}.",
     f"En el examen GED las fórmulas de volumen no se memorizan: se entregan en una hoja de fórmulas. La destreza que se evalúa es <strong>localizar la fórmula correcta</strong>, sustituir bien las medidas y calcular. En este sitio, la hoja de fórmulas se abre con el {hoja}.")}</p>
{fig_solidos()}
{tabla(t("Volume formulas for the sphere, the cone, and the pyramid", "Fórmulas de volumen de la esfera, el cono y la pirámide"), t("Volume formula of each solid and the measures it needs", "Fórmula del volumen de cada sólido y las medidas que necesita"),
  [t("Solid", "Sólido"), t("Volume formula", "Fórmula del volumen"), t("Measures you need", "Datos que se necesitan")],
  [[t("Sphere", "Esfera"), "V = 4/3 πr³", t("the radius r", "el radio r")], [t("Cone", "Cono"), "V = 1/3 πr²h", t("the radius r of the base and the height h", "el radio r de la base y la altura h")],
   [t("Pyramid", "Pirámide"), "V = 1/3 Bh", t("the area of the base B and the height h", "el área de la base B y la altura h")]])}
{caja("tip", t("The factor 1/3", "El factor 1/3"), t("<p>The cone and the pyramid both have 1/3. A cone fits three times into a cylinder with the same base and height, and a pyramid fits three times into a prism with the same base and height.</p>", "<p>Tanto el cono como la pirámide llevan 1/3. Un cono cabe tres veces dentro de un cilindro de la misma base y altura, y una pirámide cabe tres veces dentro de un prisma de la misma base y altura.</p>"))}
{enlace(n, t("formulas", "formulas"), t("the formula sheet and the three solids", "la hoja de fórmulas y los tres sólidos"), t("Recognize each solid, choose its formula, and tell the radius from the diameter.", "Reconozca cada sólido, elija su fórmula y distinga el radio del diámetro."))}'''

    s2 = f'''<p>{t("A sphere is fixed by its <strong>radius</strong> alone. Its volume is:", "Una esfera queda definida solo por su <strong>radio</strong>. Su volumen es:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">V = 4/3 πr³</p>
<p>{t("The radius is cubed (it is a measure in three dimensions), then multiplied by π and by 4/3.", "El radio se eleva al cubo (es una medida en tres dimensiones) y se multiplica por π y por 4/3.")}</p>
{ejemplo(t("Example 1: find the volume of a sphere with a radius of 3 inches.", "Ejemplo 1 · Hallar el volumen de una esfera de 3 pulgadas de radio."),
  [("1", t("Cube the radius.", "Se eleva el radio al cubo."), "3³ = 27."),
   ("2", t("Substitute.", "Se sustituye."), "V = 4/3 · π · 27."),
   ("3", t("Simplify.", "Se simplifica."), t("4/3 · 27 = 36, so V = 36π.", "4/3 · 27 = 36, así que V = 36π.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>V = 36π ≈ 113.1 cubic inches</strong> (with the π key; with π ≈ 3.14 it is 113.0).", "<strong>V = 36π ≈ 113.1 pulgadas cúbicas</strong> (con la tecla π; con π ≈ 3.14 da 113.0)."))])}
{caja("ojo", t("The radius, not the diameter", "El radio, no el diámetro"), t("<p>If the problem gives the diameter, divide it by 2 first to get the radius. Putting the diameter straight into the formula is a common mistake.</p>", "<p>Si el problema da el diámetro, primero se divide entre 2 para obtener el radio. Un error común es usar el diámetro directamente en la fórmula.</p>"))}
{calc(t("Exact or approximate", "Exacto o aproximado"), t("<p>The exact answer keeps π (for example, 36π). For the approximate value, use what the problem says: π ≈ 3.14 or the π key. The two can differ a little in the last digits; if nothing is said, the π key is more exact.</p>", "<p>La respuesta exacta deja π (por ejemplo, 36π). Para el valor aproximado, use lo que indique el problema: π ≈ 3.14 o la tecla π de la calculadora. Las dos formas pueden diferir un poco en las últimas cifras; si no se indica nada, la tecla π es más exacta.</p>"))}
{practica("p1", t("Practice 1 — A radius of 1", "Práctica 1 — Radio 1"), t("What is the volume of a sphere with radius 1?", "¿Cuál es el volumen de una esfera de radio 1?"), [("a", "4/3 π"), ("b", "4π"), ("c", "3/4 π")])}
{practica("p2", t("Practice 2 — A radius of 6", "Práctica 2 — Radio 6"), t("What is the volume of a sphere with radius 6?", "¿Cuál es el volumen de una esfera de radio 6?"), [("a", "144π"), ("b", "72π"), ("c", "288π")])}
{practica("p3", t("Practice 3 — The formula", "Práctica 3 — La fórmula"), t("Which is the volume formula of a sphere?", "¿Cuál es la fórmula del volumen de una esfera?"), [("a", "πr²h"), ("b", "4/3 πr³"), ("c", "1/3 πr²h")])}
{enlace(n, t("sphere", "esfera"), t("the volume of the sphere", "el volumen de la esfera"), t("Change the radius, follow V = 4/3 πr³ step by step, and see why doubling the radius makes the volume 8 times bigger.", "Cambie el radio, siga el cálculo de V = 4/3 πr³ paso a paso y vea por qué al duplicar el radio el volumen se multiplica por 8."))}'''

    s3 = f'''<p>{t("The <strong>cone</strong> has a round base and a point. Its volume is one third of the volume of a cylinder with the same base and height:", "El <strong>cono</strong> tiene una base circular y una punta. Su volumen es un tercio del de un cilindro con la misma base y altura:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">V = 1/3 πr²h</p>
{ejemplo(t("Example 2: a cone. Find the volume of a cone with a radius of 3 inches and a height of 10 inches.", "Ejemplo 2 · Cono. Hallar el volumen de un cono de 3 pulgadas de radio y 10 pulgadas de altura."),
  [("1", t("Square the radius.", "Se eleva el radio al cuadrado."), "3² = 9."),
   ("2", t("Substitute.", "Se sustituye."), "V = 1/3 · π · 9 · 10 = 1/3 · π · 90."),
   ("3", t("Simplify.", "Se simplifica."), t("1/3 · 90 = 30, so V = 30π.", "1/3 · 90 = 30, así que V = 30π.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>V = 30π ≈ 94.2 cubic inches</strong>.", "<strong>V = 30π ≈ 94.2 pulgadas cúbicas</strong>."))])}
<p>{t("The <strong>pyramid</strong> has a base that is a polygon (often a square or a rectangle). Its volume is one third of the area of the base times the height:", "La <strong>pirámide</strong> tiene una base poligonal (con frecuencia un cuadrado o un rectángulo). Su volumen es un tercio del área de la base por la altura:")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">V = 1/3 Bh</p>
{ejemplo(t("Example 3: a pyramid. Find the volume of a pyramid with a square base 6 feet on each side and a height of 10 feet.", "Ejemplo 3 · Pirámide. Hallar el volumen de una pirámide de base cuadrada de 6 pies de lado y 10 pies de altura."),
  [("1", t("Area of the base.", "Área de la base."), t("B = 6 × 6 = 36 square feet.", "B = 6 × 6 = 36 pies cuadrados.")),
   ("2", t("Substitute.", "Se sustituye."), "V = 1/3 · 36 · 10 = 1/3 · 360."),
   ("3", t("Simplify.", "Se simplifica."), "V = 120."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>V = 120 cubic feet</strong>.", "<strong>V = 120 pies cúbicos</strong>."))])}
{caja("ojo", t("Two careful steps", "Dos cuidados"), t("<p>In the cone, only the radius is squared; the height is multiplied as it is. In the pyramid, find the area of the base first (side × side for a square, length × width for a rectangle), and only then use 1/3 × B × h. The h is the straight-up height, not the slanted height of a face.</p>", "<p>En el cono, solo el radio se eleva al cuadrado; la altura se multiplica tal como está. En la pirámide, primero se calcula el área de la base (lado × lado si es cuadrada, largo × ancho si es rectangular) y solo después se aplica 1/3 × B × h. La h es la altura vertical, no la altura inclinada de una cara.</p>"))}
{practica("p4", t("Practice 4 — A cone", "Práctica 4 — Un cono"), t("What is the volume of a cone with radius 5 and height 6?", "¿Cuál es el volumen de un cono de radio 5 y altura 6?"), [("a", "50π"), ("b", "150π"), ("c", "30π")])}
{practica("p5", t("Practice 5 — A pyramid", "Práctica 5 — Una pirámide"), t("What is the volume of a pyramid with a square base 4 on each side and height 9?", "¿Cuál es el volumen de una pirámide de base cuadrada de lado 4 y altura 9?"), [("a", "144"), ("b", "48"), ("c", "24")])}
{practica("p6", t("Practice 6 — Cone and cylinder", "Práctica 6 — Cono y cilindro"), t("The volume of a cone is ___ of the volume of a cylinder with the same base and height.", "El volumen de un cono es ___ del de un cilindro con la misma base y altura."), [("a", t("one half", "la mitad")), ("b", t("double", "el doble")), ("c", t("one third", "un tercio"))])}
{enlace(n, t("cone", "cono"), t("the volume of the cone", "el volumen del cono"), t("Change the radius and the height, compare the cone with its cylinder, and see why the radius counts more than the height.", "Cambie el radio y la altura, compare el cono con su cilindro y vea por qué el radio pesa más que la altura."))}
{enlace(n, t("pyramid", "piramide"), t("the volume of the pyramid", "el volumen de la pirámide"), t("Change the base and the height and compare the pyramid with its prism.", "Cambie la base y la altura y compare la pirámide con su prisma."))}'''

    s4 = f'''<p>{t("Sometimes you know the volume and need the radius or the height. Substitute what you know and solve for the unknown, as in any equation.", "A veces se conoce el volumen y se busca el radio o la altura. Se sustituyen los datos conocidos y se despeja la incógnita como en cualquier ecuación.")}</p>
{ejemplo(t("Example 4: the height of a cone. A cone has a volume of 30π cubic inches and a radius of 3 inches. What is its height?", "Ejemplo 4 · La altura de un cono. Un cono tiene un volumen de 30π pulgadas cúbicas y un radio de 3 pulgadas. ¿Cuál es su altura?"),
  [("1", t("Substitute in V = 1/3 πr²h.", "Se sustituye en V = 1/3 πr²h."), "30π = 1/3 · π · 9 · h."),
   ("2", t("Simplify the right side.", "Se simplifica el lado derecho."), t("1/3 · 9 = 3, so 30π = 3πh.", "1/3 · 9 = 3, queda 30π = 3πh.")),
   ("3", t("Divide both sides by 3π.", "Se dividen los dos lados entre 3π."), "h = 30π ÷ 3π = 10."),
   ("✓", t("Answer.", "Respuesta."), t("The height is <strong>10 inches</strong>.", "La altura es de <strong>10 pulgadas</strong>."))])}
{caja("tip", t("Canceling π makes it easier", "Cancelar π facilita el cálculo"), t("<p>When π is on both sides of the equation, it cancels. Then solving only takes simple numbers.</p>", "<p>Cuando π aparece en los dos lados de la ecuación, se cancela. Así el despeje se reduce a operaciones con números sencillos.</p>"))}
{enlace(n, t("solve", "despejar"), t("finding a missing measure", "despejar una medida desconocida"), t("Cases step by step: the height of a cone or a pyramid and the radius of a sphere from the volume.", "Casos paso a paso: la altura de un cono o de una pirámide y el radio de una esfera a partir del volumen."))}'''

    secciones = [("s-" + t("formulas", "formulas"), t("The formula sheet and the three solids", "La hoja de fórmulas y los tres sólidos"), s1),
                 ("s-" + t("sphere", "esfera"), t("The volume of a sphere", "Volumen de la esfera"), s2),
                 ("s-" + t("cone", "cono"), t("The volume of a cone and of a pyramid", "Volumen del cono y de la pirámide"), s3),
                 ("s-" + t("solve", "despejar"), t("Finding a missing measure", "Despejar una medida desconocida"), s4)]

    lesson = {"next": t("Lesson 2.2", "Lección 2.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("Do not forget the 4/3: 4/3 · π · 1³.", "No olvide el 4/3: 4/3 · π · 1³."), "c": t("The fraction is 4/3, not 3/4.", "La fracción es 4/3, no 3/4.")}, "right": "4/3 · π · 1³ = 4/3 π.", "solution": "V = 4/3 π."},
      "p2": {"ok": "c", "hints": {"a": t("You squared the radius (36). Cube it: 6³ = 216.", "Elevó el radio al cuadrado (36). Hay que elevarlo al cubo: 6³ = 216."), "b": t("6³ = 216 and 4/3 · 216 = 288.", "6³ = 216 y 4/3 · 216 = 288.")}, "right": "6³ = 216, 4/3 · 216 = 288: 288π.", "solution": "V = 288π."},
      "p3": {"ok": "b", "hints": {"a": t("πr²h is the cylinder.", "πr²h es el cilindro."), "c": t("1/3 πr²h is the cone.", "1/3 πr²h es el cono.")}, "right": t("The sphere only needs the radius: 4/3 πr³.", "La esfera solo necesita el radio: 4/3 πr³."), "solution": "V = 4/3 πr³."},
      "p4": {"ok": "a", "hints": {"b": t("You left out the 1/3: 25 · 6 = 150, then divide by 3.", "Olvidó el 1/3: 25 · 6 = 150, después se divide entre 3."), "c": t("Square the radius: 5² = 25, not 5.", "Eleve el radio al cuadrado: 5² = 25, no 5.")}, "right": "1/3 · π · 25 · 6 = 50π.", "solution": "V = 50π."},
      "p5": {"ok": "b", "hints": {"a": t("You left out the 1/3: 16 · 9 = 144, then divide by 3.", "Olvidó el 1/3: 16 · 9 = 144, después se divide entre 3."), "c": t("The base is 4 × 4 = 16, not 8.", "La base es 4 × 4 = 16, no 8.")}, "right": "B = 16, V = 1/3 · 16 · 9 = 48.", "solution": "V = 48."},
      "p6": {"ok": "c", "hints": {"a": t("Look at the formula: V = 1/3 πr²h.", "Mire la fórmula: V = 1/3 πr²h."), "b": t("The cone is smaller than its cylinder.", "El cono es más pequeño que su cilindro.")}, "right": t("Three cones fill the cylinder.", "Tres conos llenan el cilindro."), "solution": t("One third.", "Un tercio.")},
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("You used 4 · 3 instead of 3³.", "Usó 4 · 3 en lugar de 3³."), "b": t("27 is r³. Multiply it by 4/3.", "27 es r³. Multiplíquelo por 4/3."), "c": t("4 · 27 = 108; you still need to divide by 3.", "4 · 27 = 108; falta dividir entre 3.")}, "solution": "4/3 · 27 = 36: 36π."},
      "B": {"ok": "b", "hints": {"a": t("πr²h is the cylinder.", "πr²h es el cilindro."), "c": t("1/3 πr²h is the cone.", "1/3 πr²h es el cono."), "d": t("4πr² is the surface area of the sphere, not its volume.", "4πr² es el área de la superficie de la esfera, no su volumen.")}, "solution": "V = 4/3 πr³."},
      "C": {"ok": "c", "hints": {"a": t("You left out the 1/3.", "Olvidó el 1/3."), "b": t("Square the radius: 3² = 9.", "Eleve el radio al cuadrado: 3² = 9."), "d": t("Only the radius is squared, and do not forget the 1/3.", "Solo el radio va al cuadrado, y no olvide el 1/3.")}, "solution": "1/3 · 9 · 10 = 30: 30π."},
      "D": {"ok": "d", "hints": {"a": t("You left out the 1/3: 4 · 9 = 36, then divide by 3.", "Olvidó el 1/3: 4 · 9 = 36, después se divide entre 3."), "b": t("Square the radius: 2² = 4, not 2.", "Eleve el radio al cuadrado: 2² = 4, no 2."), "c": t("Square the radius: 2² = 4.", "Eleve el radio al cuadrado: 2² = 4.")}, "solution": "1/3 · 4 · 9 = 12: 12π."},
      "E": {"ok": "b", "hints": {"a": t("You left out the 1/3.", "Olvidó el 1/3."), "c": t("The base is 6 × 6 = 36, not 6 + 6.", "La base es 6 × 6 = 36, no 6 + 6."), "d": t("Find the base first: 6 × 6 = 36.", "Primero la base: 6 × 6 = 36.")}, "solution": "1/3 · 36 · 10 = 120."},
      "F": {"ok": "a", "hints": {"b": t("You left out the 1/3.", "Olvidó el 1/3."), "c": t("The base is 4 × 3 = 12. Then 1/3 · 12 · 5.", "La base es 4 × 3 = 12. Después 1/3 · 12 · 5."), "d": t("1/3 · 12 · 5 = 20.", "1/3 · 12 · 5 = 20.")}, "solution": "B = 12, V = 1/3 · 12 · 5 = 20."},
      "G": {"ok": "d", "hints": {"a": t("You left out the 1/3: 144 · 5 = 720, then divide by 3.", "Olvidó el 1/3: 144 · 5 = 720, después se divide entre 3."), "b": t("The base is 12 × 12 = 144, not 12 · 5 · 2.", "La base es 12 × 12 = 144."), "c": t("1/3 · 144 · 5 = 240.", "1/3 · 144 · 5 = 240.")}, "solution": "1/3 · 144 · 5 = 240."},
      "H": {"ok": "b", "hints": {"a": t("30 is the number in front of π in the volume. Solve 30π = 3πh.", "30 es el número que acompaña a π en el volumen. Despeje 30π = 3πh."), "c": t("3 is the radius.", "3 es el radio."), "d": t("You multiplied instead of dividing.", "Multiplicó en lugar de dividir.")}, "solution": "30π = 1/3 · π · 9 · h = 3πh → h = 10."},
     }}

    quiz = [
     ("A", t("What is the volume of a sphere with radius 3?", "¿Cuál es el volumen de una esfera de radio 3?"), [("a", "12π"), ("b", "27π"), ("c", "108π"), ("d", "36π")]),
     ("B", t("Which formula gives the volume of a sphere?", "¿Qué fórmula da el volumen de una esfera?"), [("a", "πr²h"), ("b", "4/3 πr³"), ("c", "1/3 πr²h"), ("d", "4πr²")]),
     ("C", t("What is the volume of a cone with radius 3 and height 10?", "¿Cuál es el volumen de un cono de radio 3 y altura 10?"), [("a", "90π"), ("b", "10π"), ("c", "30π"), ("d", "270π")]),
     ("D", t("What is the volume of a cone with radius 2 and height 9?", "¿Cuál es el volumen de un cono de radio 2 y altura 9?"), [("a", "36π"), ("b", "18π"), ("c", "6π"), ("d", "12π")]),
     ("E", t("What is the volume of a pyramid with a square base 6 on each side and height 10?", "¿Cuál es el volumen de una pirámide de base cuadrada de lado 6 y altura 10?"), [("a", "360"), ("b", "120"), ("c", "60"), ("d", "40")]),
     ("F", t("What is the volume of a pyramid with a 4 × 3 rectangular base and height 5?", "¿Cuál es el volumen de una pirámide de base rectangular de 4 × 3 y altura 5?"), [("a", "20"), ("b", "60"), ("c", "30"), ("d", "40")]),
     ("G", t("What is the volume of a pyramid with a square base 12 on each side and height 5?", "¿Cuál es el volumen de una pirámide de base cuadrada de lado 12 y altura 5?"), [("a", "720"), ("b", "120"), ("c", "480"), ("d", "240")]),
     ("H", t("A cone has a volume of 30π and a radius of 3. What is its height?", "Un cono tiene un volumen de 30π y un radio de 3. ¿Cuál es su altura?"), [("a", "30"), ("b", "10"), ("c", "3"), ("d", "90")])]

    tarea = (t("For your own work, with a notebook, the formula sheet, and a calculator: (1) Four sphere volumes, two from the radius and two from the diameter. Copy the formula from the sheet and write the substitution before you calculate. (2) A round water tank with a radius of 4 feet: how many cubic feet of water does it hold? Also give the answer in gallons (1 cubic foot ≈ 7.48 gallons). (3) Three cones, one of them an ice cream cone with a radius of 1.5 inches and a height of 4 inches. In each one, underline that only the radius is squared, and do not forget the 1/3. (4) Three pyramids, one of them with a square base 755 feet on each side and a height of 481 feet (the Great Pyramid of Giza). Find the area of the base first, and say whether the size of the answer seems reasonable. (5) Two missing-measure problems: from the volume, find the radius or the height. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, la hoja de fórmulas y la calculadora: (1) Cuatro volúmenes de esferas, dos a partir del radio y dos a partir del diámetro. Copie la fórmula de la hoja y escriba la sustitución antes de calcular. (2) Un tanque de agua esférico de 4 pies de radio: ¿cuántos pies cúbicos de agua caben? Exprese también el resultado en galones (1 pie cúbico ≈ 7.48 galones). (3) Tres conos, entre ellos uno de helado de 1.5 pulgadas de radio y 4 pulgadas de altura. En cada uno, subraye que solo el radio se eleva al cuadrado y no olvide el factor 1/3. (4) Tres pirámides, entre ellas una de base cuadrada de 755 pies de lado y 481 pies de altura (la Gran Pirámide de Guiza). Calcule primero el área de la base y comente si el tamaño del resultado le parece razonable. (5) Dos problemas de medida desconocida: conocido el volumen, despeje el radio o la altura. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Find a ball, a party hat or a paper cup shaped like a cone, and a box-shaped container at home. Measure them in inches and find their volumes. Which holds more? Fill the cone with rice or water and pour it into a cylinder-shaped glass with the same base and height: how many cones does it take?",
               "Busque en casa una pelota, un gorro de fiesta o un vaso de papel en forma de cono, y un recipiente en forma de caja. Mídalos en pulgadas y calcule sus volúmenes. ¿Cuál tiene más capacidad? Llene el cono de arroz o de agua y viértalo en un vaso cilíndrico de la misma base y altura: ¿cuántos conos hacen falta?"))

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("Use the formula sheet to find the volume of spheres, cones, and pyramids, and find a missing measure from the volume.", "Use la hoja de fórmulas para hallar el volumen de esferas, conos y pirámides, y despeje una medida desconocida a partir del volumen."),
        ("📐", t("Formula sheet and calculator", "Hoja de fórmulas y calculadora")),
        [t("<strong>Find</strong> the right formula on the formula sheet for each solid.", "<strong>Localizar</strong> en la hoja de fórmulas la fórmula adecuada para cada sólido."),
         t("<strong>Find</strong> the volume of a sphere, a cone, and a pyramid.", "<strong>Calcular</strong> el volumen de una esfera, un cono y una pirámide."),
         t("<strong>Write</strong> the answer exactly (with π) and approximately, with cubic units.", "<strong>Expresar</strong> el resultado en forma exacta (con π) y aproximada, con unidades cúbicas."),
         t("<strong>Solve</strong> for a missing measure (radius or height) when you know the volume.", "<strong>Despejar</strong> una medida desconocida (radio o altura) a partir del volumen.")],
        secciones, tarea, quiz,
        t("Self-check checklist for the volume of solids", "Lista de autoevaluación del volumen de sólidos"),
        t("Self-check checklist: skills for the volume of spheres, cones, and pyramids", "Lista de autoevaluación: destrezas del volumen de esferas, conos y pirámides"),
        [(t("Finding and using the formula", "Localizar y aplicar la fórmula"), t("I choose and use the right formula from the sheet quickly and surely.", "Selecciono y aplico la fórmula correcta de la hoja con seguridad y rapidez."), t("I find a formula but use it for the wrong solid.", "Localizo una fórmula, pero la aplico al sólido equivocado."), t("I cannot find the right formula on the sheet.", "No localizo la fórmula correcta en la hoja.")),
         (t("Substituting and calculating", "Sustituir y calcular"), t("I substitute correctly, calculate with π, and check that the answer is reasonable.", "Sustituyo correctamente, calculo con π y compruebo que el resultado sea razonable."), t("I make occasional mistakes with the exponents or the 1/3.", "Cometo errores ocasionales en los exponentes o en el 1/3."), t("I use the diameter, or I forget the exponent.", "Uso el diámetro u olvido el exponente.")),
         (t("Writing the answer", "Expresar el resultado"), t("I give the answer in cubic units and can find a missing measure when needed.", "Doy el resultado en unidades cúbicas y despejo una medida cuando hace falta."), t("I give units, but not cubic ones, or I round too much.", "Pongo unidades, pero no cúbicas, o redondeo demasiado."), t("I leave out the units.", "Omito las unidades."))],
        t("<p>In this lesson you found the volume of <strong>spheres</strong> (4/3 πr³), <strong>cones</strong> (1/3 πr²h), and <strong>pyramids</strong> (1/3 Bh), always with the <strong>formula sheet</strong>, and you learned to <strong>solve for</strong> a measure from the volume.</p>\n<p>In <strong>Lesson 2.2 · Composite 3D figures and surface area</strong> you will combine these solids: a silo is a cylinder topped with a cone, a capsule is a cylinder with two half-spheres. You will find the volume by <strong>adding or subtracting</strong> parts, and you will meet the <strong>surface area</strong>, to answer questions like how much paint or material you need.</p>",
          "<p>En esta lección se calculó el volumen de <strong>esferas</strong> (4/3 πr³), <strong>conos</strong> (1/3 πr²h) y <strong>pirámides</strong> (1/3 Bh), siempre con la <strong>hoja de fórmulas</strong>, y se aprendió a <strong>despejar</strong> una medida a partir del volumen.</p>\n<p>En la <strong>Lección 2.2 · Figuras 3D compuestas y área de superficie</strong> se combinarán estos sólidos: un silo es un cilindro coronado por un cono, una cápsula es un cilindro con dos semiesferas. Se calculará el volumen <strong>sumando o restando</strong> partes y se introducirá el <strong>área de superficie</strong>, para responder preguntas como cuánta pintura o material se necesita.</p>"),
        ("2-2", ("", t("Lesson 2.2 · Composite 3D figures and surface area", "Lección 2.2 · Figuras 3D compuestas y área de superficie"))),
        [(t("sphere", "esfera"), t("A solid where every point is the same distance (the radius) from the center.", "Un sólido en el que todos los puntos están a la misma distancia (el radio) del centro.")),
         (t("cone", "cono"), t("A solid with a round base and a point.", "Un sólido con una base circular y una punta.")),
         (t("pyramid", "pirámide"), t("A solid with a polygon for a base and triangular faces that meet at a point.", "Un sólido con un polígono de base y caras triangulares que se juntan en una punta.")),
         (t("height (h)", "altura (h)"), t("The straight-up distance from the base to the point, not the slanted one.", "La distancia vertical de la base a la punta, no la inclinada.")),
         (t("cubic units", "unidades cúbicas"), t("The units of volume: cubic inches, cubic feet, cubic yards.", "Las unidades del volumen: pulgadas cúbicas, pies cúbicos, yardas cúbicas."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function F(n, d){ return fr(n, d === undefined ? 1 : d); }
function U(){ return UNID[$("es-u") ? $("es-u").value : "in"]; }
function vPi(k){ return piTxt(k) + " ≈ " + n1(piVal(k)); }

/* ===== MODULE 1 · The formula sheet ===== */
var FO = {s: "esfera"};
function foPinta(){
  var dia = $("fo-d").checked, s = FO.s, svg, txt;
  ["esfera", "cono", "piramide"].forEach(function(k){ $("fo-" + k).setAttribute("aria-pressed", k === s ? "true" : "false"); });
  if (s === "esfera"){ svg = esferaSVG({r: "r", diam: dia, voz: T("A sphere with its radius r marked from the center to the surface", "Una esfera con su radio r marcado del centro a la superficie") + (dia ? T(" and its diameter d below.", " y su diámetro d debajo.") : ".")});
    txt = T("<strong>V = 4/3 πr³.</strong> The only measure is the radius r, from the center to the surface. ", "<strong>V = 4/3 πr³.</strong> La única medida es el radio r, del centro a la superficie. ") + (dia ? T("The diameter d goes all the way across: d = 2r, so r = d ÷ 2.", "El diámetro d cruza de lado a lado: d = 2r, así que r = d ÷ 2.") : ""); }
  else if (s === "cono"){ svg = conoSVG({r: 5, h: 8, esc: 22, voz: T("A cone with the radius r of its base and its height h, from the center of the base to the point.", "Un cono con el radio r de su base y su altura h, del centro de la base a la punta.")}).replace("r = 5", "r").replace("h = 8", "h");
    txt = T("<strong>V = 1/3 πr²h.</strong> It needs the radius r of the round base and the height h, measured straight up from the center of the base to the point.", "<strong>V = 1/3 πr²h.</strong> Necesita el radio r de la base circular y la altura h, medida en vertical del centro de la base a la punta.") + (dia ? " " + T("If you are given the diameter of the base, halve it.", "Si se da el diámetro de la base, se divide entre 2.") : ""); }
  else { svg = piramideSVG({L: 6, b: 6, h: 8, esc: 24, cuadrada: true, voz: T("A pyramid with a square base of side L and its height h, from the center of the base to the point.", "Una pirámide de base cuadrada de lado L y su altura h, del centro de la base a la punta.")}).replace(/L = 6/g, "L").replace("h = 8", "h");
    txt = T("<strong>V = 1/3 Bh.</strong> B is the area of the base (here L × L) and h is the straight-up height, not the slanted height of a face.", "<strong>V = 1/3 Bh.</strong> B es el área de la base (aquí L × L) y h es la altura vertical, no la altura inclinada de una cara."); }
  $("fo-svg").innerHTML = svg; $("fo-txt").innerHTML = '<div class="linea">' + txt + "</div>";
}
["esfera", "cono", "piramide"].forEach(function(k){ $("fo-" + k).addEventListener("click", function(){ FO.s = k; foPinta(); }); });
$("fo-d").addEventListener("change", foPinta); foPinta();
OMR("fq", function(){
  var tipo = elige(["formula", "formula", "radio", "dato"]);
  var FORM = {esfera: "V = 4/3 πr³", cono: "V = 1/3 πr²h", piramide: "V = 1/3 Bh", cilindro: "V = πr²h", prisma: "V = Bh", area: "SA = 4πr²"};
  var NOM = {esfera: T("a sphere", "una esfera"), cono: T("a cone", "un cono"), piramide: T("a pyramid", "una pirámide"), cilindro: T("a cylinder", "un cilindro"), prisma: T("a prism", "un prisma")};
  if (tipo === "formula"){
    var s = elige(["esfera", "cono", "piramide", "cilindro"]);
    return {enun: T("Which formula gives the volume of ", "¿Qué fórmula da el volumen de ") + NOM[s] + "?", correcta: s,
      opciones: ["esfera", "cono", "piramide", "cilindro", "area"].map(function(k){ return {clave: k, html: FORM[k]}; }).filter(function(o, i, a){ return o.clave === s || i < 5; }).slice(0, 5),
      porClave: {area: T("SA = 4πr² is the surface area of a sphere, not a volume.", "SA = 4πr² es el área de la superficie de la esfera, no un volumen."), cilindro: T("πr²h is the cylinder.", "πr²h es el cilindro."), cono: T("1/3 πr²h is the cone.", "1/3 πr²h es el cono."), piramide: T("1/3 Bh is the pyramid.", "1/3 Bh es la pirámide."), esfera: T("4/3 πr³ is the sphere.", "4/3 πr³ es la esfera.")},
      pista: T("Look at the reference sheet: which measures does this solid have?", "Mire la hoja de referencia: ¿qué medidas tiene este sólido?"), bien: FORM[s] + "."};
  }
  if (tipo === "radio"){
    var d = 2 * aleatorio(2, 12), u = elige(["in", "ft"]), obj = elige(["esfera", "cono"]);
    return {enun: T("The problem gives ", "El problema da ") + NOM[obj] + T(" with a diameter of ", " con un diámetro de ") + d + " " + UNID[u][1] + T(". What number goes in place of r in the formula?", ". ¿Qué número va en lugar de r en la fórmula?"), correcta: "r",
      opciones: [{clave: "r", html: String(d / 2)}, {clave: "d", html: String(d)}, {clave: "2d", html: String(2 * d)}, {clave: "dd", html: String(d * d)}],
      porClave: {d: T("That is the diameter. The radius is half of it.", "Ese es el diámetro. El radio es la mitad."), "2d": T("The radius is smaller than the diameter: divide by 2.", "El radio es más pequeño que el diámetro: se divide entre 2.")},
      pista: T("r = d ÷ 2.", "r = d ÷ 2."), bien: "r = " + d + " ÷ 2 = " + d / 2 + "."};
  }
  var q = elige([["piramide", T("the area of the base and the height", "el área de la base y la altura")], ["esfera", T("only the radius", "solo el radio")], ["cono", T("the radius of the base and the height", "el radio de la base y la altura")]]);
  return {enun: T("Which measures do you need to find the volume of ", "¿Qué medidas se necesitan para el volumen de ") + NOM[q[0]] + "?", correcta: q[0], enOrden: true,
    opciones: [{clave: "esfera", html: T("Only the radius", "Solo el radio")}, {clave: "cono", html: T("The radius of the base and the height", "El radio de la base y la altura")}, {clave: "piramide", html: T("The area of the base and the height", "El área de la base y la altura")}, {clave: "x", html: T("The radius and the diameter", "El radio y el diámetro")}],
    pista: T("Read the formula: each letter is a measure you need.", "Lea la fórmula: cada letra es una medida que se necesita."), bien: q[1] + "."};
});

/* ===== MODULE 2 · Sphere workshop ===== */
function esPinta(){
  var dado = $("es-dado").value, v = +$("es-r").value, r = dado === "d" ? v / 2 : v, u = U(), k = fmul(F(4, 3), F(Math.round(r * r * r * 8), 8));
  $("es-rv").textContent = v; $("es-rl").textContent = dado === "d" ? T("Diameter d", "Diámetro d") : T("Radius r", "Radio r");
  $("es-svg").innerHTML = esferaSVG({r: nd(r), diam: dado === "d", cil: $("es-cil").checked, voz: T("A sphere with a radius of ", "Una esfera de radio ") + nd(r) + " " + u[1] + ($("es-cil").checked ? T(", inside the cylinder that holds it exactly.", ", dentro del cilindro que la contiene exactamente.") : ".")});
  var pasos = '<div class="linea">' + T("Formula: ", "Fórmula: ") + "V = 4/3 πr³</div>";
  if (dado === "d") pasos += '<div class="linea">' + T("First the radius: r = d ÷ 2 = ", "Primero el radio: r = d ÷ 2 = ") + v + " ÷ 2 = " + nd(r) + "</div>";
  pasos += '<div class="linea">' + T("Substitute: ", "Sustitución: ") + "V = 4/3 · π · " + nd(r) + "³</div>" +
    '<div class="linea">' + T("Cube the radius: ", "Se eleva al cubo: ") + nd(r) + "³ = " + nd(r * r * r) + "</div>" +
    '<div class="linea veredicto">V = 4/3 · ' + nd(r * r * r) + " · π = " + piTxt(k) + " ≈ " + n1(piVal(k)) + " " + u[2] + "</div>" +
    '<div class="linea">' + T("With π ≈ 3.14: ", "Con π ≈ 3.14: ") + n1(fval(k) * 3.14) + " " + u[2] + "</div>";
  if ($("es-cil").checked) pasos += '<div class="linea">' + T("The cylinder that holds it has V = πr² · 2r = 2πr³ = ", "El cilindro que la contiene tiene V = πr² · 2r = 2πr³ = ") + piTxt(fmul(F(2), F(Math.round(r * r * r * 8), 8))) + T(": the sphere fills exactly 2/3 of it.", ": la esfera ocupa exactamente 2/3 de él.") + "</div>";
  $("es-pasos").innerHTML = pasos;
  $("es-tabla").innerHTML = '<caption class="sr-only">' + T("Volume of the sphere for the current radius and its multiples", "Volumen de la esfera para el radio actual y sus múltiplos") + '</caption><thead><tr><th scope="col">' + T("Radius", "Radio") + '</th><th scope="col">' + T("Volume (about)", "Volumen aproximado") + '</th><th scope="col">' + T("Compared with now", "Comparado con el actual") + "</th></tr></thead><tbody>" +
    [1, 2, 3].map(function(m){ return "<tr><td>" + nd(r * m) + " " + u[4] + "</td><td>" + n1(4 / 3 * Math.PI * Math.pow(r * m, 3)) + " " + u[2] + "</td><td>× " + m * m * m + (m > 1 ? " (" + m + "³)" : "") + "</td></tr>"; }).join("") + "</tbody>";
  esReto();
}
var RET = {v: null};
function esRetoNuevo(){ var r = aleatorio(2, 12); RET.v = 4 / 3 * Math.PI * r * r * r; RET.bien = false; $("er-meta").textContent = "V ≈ " + n1(RET.v) + " " + U()[2]; esReto(); }
function esReto(){
  if (RET.v === null) return;
  var dado = $("es-dado").value, v = +$("es-r").value, r = dado === "d" ? v / 2 : v, V = 4 / 3 * Math.PI * r * r * r, dif = (V - RET.v) / RET.v, fb = $("er-fb");
  if (Math.abs(dif) <= 0.02){ fb.className = "fb bien"; fb.innerHTML = TX.bien + T("With r = ", "Con r = ") + nd(r) + T(" the volume is ", " el volumen es ") + n1(V) + "."; }
  else { fb.className = "fb pista"; fb.innerHTML = T("Now V ≈ ", "Ahora V ≈ ") + n1(V) + ": " + (dif < 0 ? T("too small, make the radius bigger.", "se queda corto: aumente el radio.") : T("too big, make the radius smaller.", "se pasa: reduzca el radio.")); }
}
["es-r", "es-dado", "es-u", "es-cil"].forEach(function(i){ $(i).addEventListener("input", esPinta); $(i).addEventListener("change", esPinta); });
$("es-x2").addEventListener("click", function(){ $("es-r").value = Math.min(12, +$("es-r").value * 2); esPinta(); $("es-nota").textContent = T("The radius doubled; the volume became 2³ = 8 times bigger.", "El radio se duplicó; el volumen se multiplicó por 2³ = 8."); });
$("es-m2").addEventListener("click", function(){ $("es-r").value = Math.max(1, Math.round(+$("es-r").value / 2)); esPinta(); $("es-nota").textContent = T("Half the radius gives 1/8 of the volume.", "La mitad del radio da 1/8 del volumen."); });
$("er-otro").addEventListener("click", esRetoNuevo);
esPinta(); esRetoNuevo();
function pistaPi(r){ return [{k: 4 * r * r * r, msg: T("Do not forget to divide by 3: the fraction is 4/3.", "No olvide dividir entre 3: la fracción es 4/3.")}, {k: 4 / 3 * r * r, msg: T("You squared the radius. For a sphere, cube it: r³.", "Elevó el radio al cuadrado. En la esfera se eleva al cubo: r³.")},
  {k: 4 / 3 * 8 * r * r * r, msg: T("It looks like you used the diameter. Use the radius: half of the diameter.", "Parece que usó el diámetro. Use el radio: la mitad del diámetro.")}, {k: r * r * r, msg: T("Multiply r³ by 4/3.", "Multiplique r³ por 4/3.")}]; }
creaPracticaLibre("pe", function(){
  var r = aleatorio(1, 9), d = Math.random() < 0.35, u = UNID[elige(["in", "ft", "yd"])], k = fmul(F(4, 3), F(r * r * r));
  return {enun: T("Find the volume of a sphere with a ", "Calcule el volumen de una esfera de ") + (d ? T("diameter of ", "diámetro ") + 2 * r : T("radius of ", "radio ") + r) + " " + u[1] + ". " + T("Give it with π (like 36π) or as a decimal.", "Escríbalo con π (como 36π) o en decimal."),
    evalua: function(txt){ return evaluaPi(txt, k, pistaPi(r)); },
    solucion: (d ? "r = " + 2 * r + " ÷ 2 = " + r + "; " : "") + "V = 4/3 · π · " + r + "³ = 4/3 · " + r * r * r + " · π = " + vPi(k) + " " + u[2] + "."};
});

/* ===== MODULE 3 · Cone workshop ===== */
function coPinta(){
  var r = +$("co-r").value, h = +$("co-h").value, u = UNID[$("co-u").value], k = F(r * r * h, 3), kc = F(r * r * h);
  $("co-rv").textContent = r; $("co-hv").textContent = h;
  $("co-svg").innerHTML = conoSVG({r: r, h: h, esc: 16, cil: $("co-cil").checked, voz: T("A cone with radius ", "Un cono de radio ") + r + T(" and height ", " y altura ") + h + " " + u[1] + ($("co-cil").checked ? T(", inside the cylinder with the same base and height.", ", dentro del cilindro de igual base y altura.") : ".")});
  $("co-pasos").innerHTML = '<div class="linea">' + T("Formula: ", "Fórmula: ") + "V = 1/3 πr²h</div>" + '<div class="linea">' + T("Substitute: ", "Sustitución: ") + "V = 1/3 · π · " + r + "² · " + h + "</div>" +
    '<div class="linea">' + T("Square only the radius: ", "Se eleva solo el radio al cuadrado: ") + r + "² = " + r * r + "</div>" + '<div class="linea veredicto">V = 1/3 · ' + r * r + " · " + h + " · π = " + vPi(k) + " " + u[2] + "</div>";
  $("co-cards").innerHTML = '<div class="tarjeta"><strong>' + T("Cone", "Cono") + '</strong><span class="grande">' + piTxt(k) + "</span><br>≈ " + n1(piVal(k)) + " " + u[2] + '</div><div class="tarjeta"><strong>' + T("Cylinder with the same base and height", "Cilindro de igual base y altura") + '</strong><span class="grande">' + piTxt(kc) + "</span><br>≈ " + n1(piVal(kc)) + " " + u[2] + "</div>";
}
["co-r", "co-h", "co-u", "co-cil"].forEach(function(i){ $(i).addEventListener("input", coPinta); $(i).addEventListener("change", coPinta); });
$("co-x2r").addEventListener("click", function(){ if (+$("co-r").value * 2 > 10){ $("co-nota").textContent = T("Make the radius 5 or less first.", "Primero deje el radio en 5 o menos."); return; } $("co-r").value = +$("co-r").value * 2; coPinta(); $("co-nota").textContent = T("Doubling the radius makes the volume 2² = 4 times bigger: the radius is squared.", "Al duplicar el radio, el volumen se multiplica por 2² = 4: el radio está al cuadrado."); });
$("co-x2h").addEventListener("click", function(){ if (+$("co-h").value * 2 > 16){ $("co-nota").textContent = T("Make the height 8 or less first.", "Primero deje la altura en 8 o menos."); return; } $("co-h").value = +$("co-h").value * 2; coPinta(); $("co-nota").textContent = T("Doubling the height only doubles the volume.", "Al duplicar la altura, el volumen solo se duplica."); });
coPinta();
creaPracticaLibre("pc", function(){
  var r = aleatorio(1, 8), h = 3 * aleatorio(1, 5) + (Math.random() < 0.3 ? 1 : 0), d = Math.random() < 0.25, u = UNID[elige(["in", "ft"])], k = F(r * r * h, 3);
  return {enun: T("Find the volume of a cone with a ", "Calcule el volumen de un cono de ") + (d ? T("diameter of ", "diámetro ") + 2 * r : T("radius of ", "radio ") + r) + T(" and a height of ", " y altura ") + h + " " + u[1] + ". " + T("Give it with π or as a decimal.", "Escríbalo con π o en decimal."),
    evalua: function(txt){ return evaluaPi(txt, k, [{k: r * r * h, msg: T("You left out the 1/3: divide by 3.", "Olvidó el 1/3: divida entre 3.")}, {k: r * h / 3, msg: T("Square the radius: r².", "Eleve el radio al cuadrado: r².")}, {k: r * r * h * h / 3, msg: T("Only the radius is squared, not the height.", "Solo el radio va al cuadrado, no la altura.")}, {k: 4 * r * r * h / 3, msg: T("It looks like you used the diameter. Use the radius.", "Parece que usó el diámetro. Use el radio.")}]); },
    solucion: (d ? "r = " + 2 * r + " ÷ 2 = " + r + "; " : "") + "V = 1/3 · π · " + r + "² · " + h + " = 1/3 · " + r * r * h + " · π = " + vPi(k) + " " + u[2] + "."};
});

/* ===== MODULE 4 · Pyramid workshop ===== */
function piPinta(){
  var cuad = $("pi-forma").value === "c", L = +$("pi-L").value, w = cuad ? L : +$("pi-w").value, h = +$("pi-h").value, u = UNID[$("pi-u").value], Bv = L * w, V = Bv * h / 3;
  $("pi-wc").hidden = cuad; $("pi-Lv").textContent = L; $("pi-wv").textContent = w; $("pi-hv").textContent = h;
  $("pi-svg").innerHTML = piramideSVG({L: L, b: w, h: h, esc: 18, cuadrada: cuad, prisma: $("pi-pri").checked, voz: T("A pyramid with a ", "Una pirámide de base ") + (cuad ? T("square base " + L + " on each side", "cuadrada de lado " + L) : T(L + " by " + w + " rectangular base", "rectangular de " + L + " por " + w)) + T(" and a height of ", " y altura ") + h + " " + u[1] + "."});
  $("pi-pasos").innerHTML = '<div class="linea">' + T("Step 1 · area of the base: ", "Paso 1 · área de la base: ") + "B = " + L + " × " + w + " = " + Bv + " " + u[3] + "</div>" +
    '<div class="linea">' + T("Step 2 · substitute: ", "Paso 2 · sustitución: ") + "V = 1/3 · " + Bv + " · " + h + " = 1/3 · " + Bv * h + "</div>" + '<div class="linea veredicto">V = ' + n1(V, 2) + " " + u[2] + "</div>";
  $("pi-cards").innerHTML = '<div class="tarjeta"><strong>' + T("Pyramid", "Pirámide") + '</strong><span class="grande">' + n1(V, 2) + "</span> " + u[2] + '</div><div class="tarjeta"><strong>' + T("Prism with the same base and height", "Prisma de igual base y altura") + '</strong><span class="grande">' + Bv * h + "</span> " + u[2] + "</div>";
}
["pi-forma", "pi-L", "pi-w", "pi-h", "pi-u", "pi-pri"].forEach(function(i){ $(i).addEventListener("input", piPinta); $(i).addEventListener("change", piPinta); });
piPinta();
creaPracticaLibre("pp", function(){
  var cuad = Math.random() < 0.6, L = aleatorio(2, 12), w = cuad ? L : aleatorio(2, 10), h = 3 * aleatorio(1, 6), u = UNID[elige(["in", "ft", "yd"])], V = L * w * h / 3;
  return {enun: T("Find the volume of a pyramid with a ", "Calcule el volumen de una pirámide de base ") + (cuad ? T("square base " + L + " " + u[1] + " on each side", "cuadrada de " + L + " " + u[1] + " de lado") : T(L + " × " + w + " rectangular base (in " + u[1] + ")", "rectangular de " + L + " × " + w + " (en " + u[1] + ")")) + T(" and a height of ", " y altura de ") + h + " " + u[1] + ".",
    evalua: function(txt){ return evaluaNum(txt, V, 0.01, [{v: L * w * h, msg: T("You left out the 1/3: divide by 3.", "Olvidó el 1/3: divida entre 3.")}, {v: (L + w) * h / 3, msg: T("The base is an area: multiply, do not add.", "La base es un área: se multiplica, no se suma.")}, {v: L * h / 3, msg: T("Find the whole area of the base first: L × " + (cuad ? "L" : "w") + ".", "Primero el área completa de la base: L × " + (cuad ? "L" : "a") + ".")}]); },
    solucion: "B = " + L + " × " + w + " = " + L * w + "; V = 1/3 · " + L * w + " · " + h + " = " + V + " " + u[2] + "."};
});

/* ===== MODULE 5 · A missing measure ===== */
function casoDespeje(){
  var tipo = elige(["hc", "hp", "re", "hc"]), u = UNID[elige(["in", "ft"])], r, h, L, k;
  if (tipo === "hc"){ r = aleatorio(2, 6); h = aleatorio(2, 12); k = F(r * r * h, 3);
    return {enun: T("A cone has a volume of ", "Un cono tiene un volumen de ") + piTxt(k) + " " + u[2] + T(" and a radius of ", " y un radio de ") + r + " " + u[1] + T(". What is its height?", ". ¿Cuál es su altura?"), res: h, u: u,
      pasos: [T("Substitute in V = 1/3 πr²h: ", "Se sustituye en V = 1/3 πr²h: ") + piTxt(k) + " = 1/3 · π · " + r * r + " · h.", T("Simplify the right side: ", "Se simplifica el lado derecho: ") + piTxt(k) + " = " + piTxt(F(r * r, 3)) + " · h.", T("Divide both sides by ", "Se dividen los dos lados entre ") + piTxt(F(r * r, 3)) + ": h = " + fTxt(k) + " ÷ " + fTxt(F(r * r, 3)) + " = " + h + ".", T("The height is ", "La altura es de ") + "<strong>" + h + " " + u[1] + "</strong>."],
      malos: [{v: fval(k), msg: T("That is the number in front of π in the volume. Solve for h.", "Ese es el número que acompaña a π en el volumen. Despeje h.")}, {v: fval(k) / (r * r), msg: T("Remember the 1/3: (1/3) · r² = " + nd(r * r / 3) + ".", "Recuerde el 1/3: (1/3) · r² = " + nd(r * r / 3) + ".")}]}; }
  if (tipo === "hp"){ L = aleatorio(2, 10); h = aleatorio(2, 12); var V = L * L * h / 3;
    return {enun: T("A pyramid with a square base " + L + " " + u[1] + " on each side has a volume of " + nd(V) + " " + u[2] + ". What is its height?", "Una pirámide de base cuadrada de " + L + " " + u[1] + " de lado tiene un volumen de " + nd(V) + " " + u[2] + ". ¿Cuál es su altura?"), res: h, u: u,
      pasos: [T("Area of the base: ", "Área de la base: ") + "B = " + L + " × " + L + " = " + L * L + ".", T("Substitute in V = 1/3 Bh: ", "Se sustituye en V = 1/3 Bh: ") + nd(V) + " = 1/3 · " + L * L + " · h.", T("Multiply both sides by 3: ", "Se multiplican los dos lados por 3: ") + nd(3 * V) + " = " + L * L + " · h.", T("Divide by ", "Se divide entre ") + L * L + ": h = <strong>" + h + " " + u[1] + "</strong>."],
      malos: [{v: V / (L * L), msg: T("Remember the 1/3: multiply the volume by 3 first.", "Recuerde el 1/3: primero multiplique el volumen por 3.")}, {v: 3 * V / L, msg: T("The base is L × L, not L.", "La base es L × L, no L.")}]}; }
  r = aleatorio(1, 6); k = F(4 * r * r * r, 3);
  return {enun: T("A sphere has a volume of ", "Una esfera tiene un volumen de ") + piTxt(k) + " " + u[2] + T(". What is its radius?", ". ¿Cuál es su radio?"), res: r, u: u,
    pasos: [T("Substitute in V = 4/3 πr³: ", "Se sustituye en V = 4/3 πr³: ") + piTxt(k) + " = 4/3 · π · r³.", T("Cancel π and multiply both sides by 3/4: ", "Se cancela π y se multiplican los dos lados por 3/4: ") + "r³ = " + fTxt(k) + " · 3/4 = " + r * r * r + ".", T("Take the cube root: ", "Se saca la raíz cúbica: ") + "r = ∛" + r * r * r + " = " + r + ".", T("The radius is ", "El radio es de ") + "<strong>" + r + " " + u[1] + "</strong>."],
    malos: [{v: r * r * r, msg: T("That is r³. Take the cube root.", "Ese es r³. Saque la raíz cúbica.")}, {v: 2 * r, msg: T("That is the diameter. The radius is half.", "Ese es el diámetro. El radio es la mitad.")}]};
}
pasoAPaso4("dz", function(){ var c = casoDespeje(); return {enun: c.enun, pasos: c.pasos}; });
creaPracticaLibre("pd", function(){
  var c = casoDespeje();
  return {enun: c.enun, evalua: function(txt){ return evaluaNum(txt, c.res, 0.01, c.malos); }, solucion: c.pasos.join(" ").replace(/<\/?strong>/g, "")};
});
'''

def practica_pagina():
    n = N
    def deslizador(i, et, mn, mx, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:190px;"><label for="{i}">{et} = <span id="{i}v"></span></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{paso}" value="{val}"></div>'
    unidades = [("in", t("inches", "pulgadas")), ("ft", t("feet", "pies")), ("yd", t("yards", "yardas"))]
    libre = lambda pid, tit, et: B.libre(pid, tit, et, nota=False)
    mods = [
     (t("formulas", "formulas"), t("The formula sheet and the three solids", "La hoja de fórmulas y los tres sólidos"),
      f'''      <p>{t("On the GED test you do not memorize the volume formulas: they are on the formula sheet (here, the <strong>Reference sheet</strong> button at the top of the page). The skill is finding the right formula, putting in the right measures, and calculating. Choose a solid: the drawing marks the measures its formula asks for.", "En el examen GED las fórmulas de volumen no se memorizan: están en la hoja de fórmulas (aquí, el botón <strong>Hoja de referencia</strong>, arriba en la página). La destreza es localizar la fórmula correcta, poner las medidas correctas y calcular. Elija un sólido: el dibujo marca las medidas que pide su fórmula.")}</p>
      <div class="modos" role="group" aria-label="{t("Solid", "Sólido")}"><button type="button" class="btn-sec" id="fo-esfera">{t("Sphere", "Esfera")}</button><button type="button" class="btn-sec" id="fo-cono">{t("Cone", "Cono")}</button><button type="button" class="btn-sec" id="fo-piramide">{t("Pyramid", "Pirámide")}</button></div>
      <div class="campo"><label><input type="checkbox" id="fo-d"> {t("Also show the diameter", "Mostrar también el diámetro")}</label></div>
      <div id="fo-svg"></div>
{n4.salida("fo-txt")}
      <div class="caja-tip">{t("The factor 1/3: a cone fits three times into a cylinder with the same base and height, and a pyramid fits three times into a prism with the same base and height.", "El factor 1/3: un cono cabe tres veces dentro de un cilindro de la misma base y altura, y una pirámide cabe tres veces dentro de un prisma de la misma base y altura.")}</div>
{B.om("fq", t("Practice: the right formula and the right measures", "Practique: la fórmula y los datos correctos"))}'''),
     (t("sphere", "esfera"), t("The volume of a sphere", "Volumen de la esfera"),
      f'''{n4.formula("V = 4/3 πr³")}
      <p>{t("Move the slider and follow the steps. Then use the buttons to see what happens to the volume when the radius doubles or is cut in half.", "Mueva el deslizador y siga los pasos. Después use los botones para ver qué pasa con el volumen cuando el radio se duplica o se reduce a la mitad.")}</p>
      <div class="panel"><div class="campos">{n4.lista("es-dado", t("The problem gives", "El problema da"), [("r", t("the radius", "el radio")), ("d", t("the diameter", "el diámetro"))])}
        <div class="campo" style="flex:1;min-width:190px;"><label for="es-r"><span id="es-rl"></span> = <span id="es-rv"></span></label><input type="range" id="es-r" min="1" max="12" step="1" value="3"></div>
        {n4.lista("es-u", t("Unit", "Unidad"), unidades)}</div>
        <div class="campo"><label><input type="checkbox" id="es-cil"> {t("Show the cylinder that holds it", "Mostrar el cilindro que la contiene")}</label></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="es-x2">{t("Double the radius", "Duplicar el radio")}</button><button type="button" class="btn-sec" id="es-m2">{t("Halve the radius", "Reducir el radio a la mitad")}</button></div></div>
      <div id="es-svg"></div>
{n4.salida("es-pasos")}
      <p class="nota" id="es-nota" aria-live="polite"></p>
      <div class="tabla-scroll"><table class="tabla-lados" id="es-tabla"></table></div>
      <div class="caja-tip">{t("The rule of the cube: if the radius is multiplied by 2, the volume is multiplied by 2³ = 8; if it is multiplied by 3, the volume is multiplied by 3³ = 27. It comes straight from the exponent 3 in the formula.", "La regla del cubo: si el radio se multiplica por 2, el volumen se multiplica por 2³ = 8; si se multiplica por 3, el volumen se multiplica por 3³ = 27. Es la consecuencia directa del exponente 3 de la fórmula.")}</div>
      <h3>{t("Challenge: reach the volume", "Reto: alcance el volumen")}</h3>
      <div class="practica"><p class="enun">{t("Move the slider until the volume is close to (within 2 %):", "Mueva el deslizador hasta que el volumen se acerque (con un margen del 2 %) a:")} <strong id="er-meta"></strong></p>
        <div class="fb" id="er-fb" role="status"></div><div class="fila-btn"><button type="button" class="btn-sec" id="er-otro">{t("New challenge", "Nuevo reto")}</button></div></div>
{libre("pe", t("Practice: the volume of a sphere", "Practique: el volumen de la esfera"), t("Volume", "Volumen"))}'''),
     (t("cone", "cono"), t("The volume of a cone", "Volumen del cono"),
      f'''{n4.formula("V = 1/3 πr²h")}
      <div class="panel"><div class="campos">{deslizador("co-r", t("Radius r", "Radio r"), 1, 10, 3)}{deslizador("co-h", t("Height h", "Altura h"), 1, 16, 10)}{n4.lista("co-u", t("Unit", "Unidad"), unidades)}</div>
        <div class="campo"><label><input type="checkbox" id="co-cil"> {t("Show the cylinder with the same base and height", "Mostrar el cilindro de igual base y altura")}</label></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="co-x2r">{t("Double the radius", "Duplicar el radio")}</button><button type="button" class="btn-sec" id="co-x2h">{t("Double the height", "Duplicar la altura")}</button></div></div>
      <div id="co-svg"></div>
{n4.salida("co-pasos")}
      <div class="tarjetas" id="co-cards" aria-live="polite"></div>
      <p class="nota" id="co-nota" aria-live="polite"></p>
      <div class="caja-atencion"><strong>{t("Only the radius is squared.", "Solo el radio se eleva al cuadrado.")}</strong> {t("In 1/3 πr²h the exponent belongs to r alone; the height is multiplied as it is. That is also why the radius counts more than the height: doubling r makes the volume 4 times bigger, doubling h only doubles it.", "En 1/3 πr²h el exponente afecta únicamente a r; la altura se multiplica tal como está. Por eso también el radio pesa más que la altura: duplicar r multiplica el volumen por 4; duplicar h solo lo duplica.")}</div>
{libre("pc", t("Practice: the volume of a cone", "Practique: el volumen del cono"), t("Volume", "Volumen"))}'''),
     (t("pyramid", "piramide"), t("The volume of a pyramid", "Volumen de la pirámide"),
      f'''{n4.formula("V = 1/3 Bh")}
      <div class="panel"><div class="campos">{n4.lista("pi-forma", t("Shape of the base", "Forma de la base"), [("c", t("Square", "Cuadrada")), ("r", t("Rectangular", "Rectangular"))])}
        {deslizador("pi-L", t("Length L", "Largo L"), 1, 12, 6)}<div id="pi-wc" style="flex:1;min-width:190px;">{deslizador("pi-w", t("Width w", "Ancho a"), 1, 12, 4)}</div>{deslizador("pi-h", t("Height h", "Altura h"), 1, 15, 10)}{n4.lista("pi-u", t("Unit", "Unidad"), unidades)}</div>
        <div class="campo"><label><input type="checkbox" id="pi-pri"> {t("Show the prism with the same base and height", "Mostrar el prisma de igual base y altura")}</label></div></div>
      <div id="pi-svg"></div>
{n4.salida("pi-pasos")}
      <div class="tarjetas" id="pi-cards" aria-live="polite"></div>
      <div class="caja-atencion"><strong>{t("The height of the pyramid, not of a face.", "La altura de la pirámide, no la de una cara.")}</strong> {t("The h in the formula is the straight-up height, from the center of the base to the point (the dashed blue line). It is not the slanted height of a triangular face.", "La h de la fórmula es la altura vertical, del centro de la base a la punta (la línea azul discontinua). No es la altura inclinada de una cara triangular.")}</div>
{libre("pp", t("Practice: the volume of a pyramid", "Practique: el volumen de la pirámide"), t("Volume", "Volumen"))}'''),
     (t("solve", "despejar"), t("Finding a missing measure", "Despejar una medida desconocida"),
      f'''      <p>{t("When you know the volume, substitute everything you know and solve for the missing measure. If π is on both sides, it cancels.", "Cuando se conoce el volumen, se sustituye todo lo conocido y se despeja la medida que falta. Si π aparece en los dos lados, se cancela.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{n4.pasos("dz", t("Another case", "Otro caso"))}
{libre("pd", t("Practice: find the missing measure", "Practique: halle la medida que falta"), t("Measure", "Medida"))}''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Volumen de esferas, conos y pirámides")
