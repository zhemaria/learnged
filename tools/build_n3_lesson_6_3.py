"""Level 3 · Lesson 6.3 · Similar figures and scale drawings (Thales' theorem) — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_6-3.html and algebra/n3-l6-3.html (GEDparaHispanos). US units: inches, feet, miles.
The explore page comes from build_n3_explora_6.py. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n3
from build_n3_explora_6 import ESTILO as ESTILO_GEO

B.NIVEL = 3
N = "6-3"
TEMA = ("Geometry: angles, the Pythagorean theorem, and similarity", "Geometría: ángulos, teorema de Pitágoras y semejanza")
TIT = ("Similar figures and scale drawings (Thales' theorem)", "Semejanza de figuras y dibujos a escala (teorema de Tales)")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js")

def fx(a, b):
    return f'<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span>'

def figura_semejantes():
    s = ('<polygon points="40,230 120,230 40,170" fill="#e3f2fd" stroke="#0d47a1" stroke-width="3"/>'
         '<path d="M40 218 H52 V230" fill="none" stroke="#0d47a1" stroke-width="2"/>'
         '<text x="80" y="252" font-size="18" font-weight="700" fill="#0d47a1" text-anchor="middle">4</text>'
         '<text x="26" y="206" font-size="18" font-weight="700" fill="#0d47a1" text-anchor="middle">3</text>'
         '<text x="92" y="192" font-size="18" font-weight="700" fill="#0d47a1" text-anchor="middle">5</text>'
         '<polygon points="230,230 390,230 230,110" fill="#efebe9" stroke="#4e342e" stroke-width="3"/>'
         '<path d="M230 216 H244 V230" fill="none" stroke="#4e342e" stroke-width="2"/>'
         '<text x="310" y="254" font-size="18" font-weight="700" fill="#3e2723" text-anchor="middle">8</text>'
         '<text x="214" y="176" font-size="18" font-weight="700" fill="#3e2723" text-anchor="middle">6</text>'
         '<text x="324" y="160" font-size="18" font-weight="700" fill="#3e2723" text-anchor="middle">10</text>')
    return B.svg("0 0 430 270", t("Two similar right triangles. The small one has sides 3, 4, and 5. The large one has sides 6, 8, and 10: each side is twice the matching side of the small one.",
                                  "Dos triángulos rectángulos semejantes. El pequeño tiene lados 3, 4 y 5. El grande tiene lados 6, 8 y 10: cada lado es el doble del lado correspondiente del pequeño."), s, 430)

def figura_sombra():
    pies = t("ft", "pies")
    s = ('<line x1="10" y1="200" x2="470" y2="200" stroke="#6d4c41" stroke-width="3"/>'
         '<line x1="60" y1="200" x2="60" y2="160" stroke="#424242" stroke-width="6"/>'
         '<line x1="60" y1="202" x2="120" y2="202" stroke="#212121" stroke-width="6"/>'
         '<line x1="120" y1="200" x2="60" y2="160" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>'
         '<rect x="214" y="110" width="12" height="90" fill="#6d4c41"/><ellipse cx="220" cy="82" rx="32" ry="42" fill="#2e7d32"/>'
         '<line x1="220" y1="202" x2="460" y2="202" stroke="#212121" stroke-width="6"/>'
         '<line x1="460" y1="200" x2="220" y2="40" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>'
         '<path d="M175 40 H185 M180 40 V200 M175 200 H185" stroke="#1b5e20" stroke-width="2" fill="none"/>'
         f'<text x="50" y="186" font-size="16" font-weight="700" fill="#222" text-anchor="end">4 {pies}</text>'
         f'<text x="90" y="224" font-size="16" font-weight="700" fill="#222" text-anchor="middle">6 {pies}</text>'
         f'<text x="340" y="224" font-size="16" font-weight="700" fill="#222" text-anchor="middle">24 {pies}</text>'
         '<text x="168" y="126" font-size="18" font-weight="700" fill="#1b5e20" text-anchor="end">x</text>')
    return B.svg("0 0 480 236", t("A 4-foot post casts a 6-foot shadow. Next to it, a tree casts a 24-foot shadow. The height of the tree, x, is unknown. Dashed lines show the sun's rays at the same angle.",
                                  "Un poste de 4 pies proyecta una sombra de 6 pies. A su lado, un árbol proyecta una sombra de 24 pies. La altura del árbol, x, es desconocida. Las líneas punteadas son los rayos del sol, con el mismo ángulo."), s, 520)

def leccion():
    n = N
    explora = t('<a href="explore-similar.html">Explore: congruent and similar triangles</a>', '<a href="explorar-semejanza.html">Explorar: triángulos congruentes y semejantes</a>')
    pies, mi = t("feet", "pies"), t("miles", "millas")
    s1 = f'''<p>{t("Lesson 6.2 worked with a special kind of triangle. This lesson studies figures that have the same shape but a different size: <strong>similar figures</strong>. To work with them you use proportions, a Level 2 tool that here is applied to geometry, and the algebra of Topics 4 and 5 to solve for the unknown side.", "La Lección 6.2 trabajó con un tipo especial de triángulo. Esta lección estudia figuras que tienen la misma forma pero distinto tamaño: las <strong>figuras semejantes</strong>. Para resolverlas se usan proporciones, una herramienta del Nivel 2 que aquí se aplica a la geometría, y el álgebra de los Temas 4 y 5 para despejar el lado desconocido.")}</p>
<p>{t("Two figures are similar when they have the same shape: their corresponding angles are equal and their corresponding sides are proportional. The number that relates the sides is called the <strong>scale factor</strong>.", "Dos figuras son semejantes cuando tienen la misma forma: sus ángulos correspondientes son iguales y sus lados correspondientes son proporcionales. El número que relaciona los lados se llama <strong>factor de escala</strong>.")}</p>
{figura_semejantes()}
{caja("tip", t("The scale factor", "El factor de escala"), t("<p>To find it, divide a side of the large figure by the matching side of the small one. In the diagram, 8 ÷ 4 = 2: the large triangle is twice the small one. Every pair of sides has the same ratio (6 ÷ 3 = 2, 10 ÷ 5 = 2).</p>", "<p>Para encontrarlo, se divide un lado del grande entre su correspondiente del pequeño. En el diagrama, 8 ÷ 4 = 2: el triángulo grande es el doble del pequeño. Todos los lados cumplen la misma razón (6 ÷ 3 = 2, 10 ÷ 5 = 2).</p>"))}
{caja("tip", t("Congruent or similar?", "¿Congruentes o semejantes?"), t(f"<p>Congruent figures have the same shape <em>and</em> the same size (scale factor 1). In {explora}, drag the corners of a triangle and watch the angles stay the same while the sides grow by the scale factor.</p>", f"<p>Las figuras congruentes tienen la misma forma <em>y</em> el mismo tamaño (factor de escala 1). En {explora}, arrastre los vértices de un triángulo y observe cómo los ángulos se mantienen mientras los lados crecen según el factor de escala.</p>"))}
{enlace(n, t("similar", "semejantes"), t("similar figures", "figuras semejantes"), t("Check whether two figures are similar by the ratio of their sides.", "Compruebe si dos figuras son semejantes por la proporción de sus lados."))}'''

    s2 = f'''<p>{t("If two figures are similar, their corresponding sides form a proportion. To find an unknown side, write the proportion and solve it with cross multiplication.", "Si dos figuras son semejantes, sus lados correspondientes forman una proporción. Para hallar un lado desconocido, se plantea la proporción y se resuelve con la multiplicación cruzada.")}</p>
{ejemplo(t("Example 1: two triangles are similar. The sides of the small one are 3, 4, and 5. In the large one, the side that matches 3 measures 6. Find the side x that matches 5.", "Ejemplo 1: dos triángulos son semejantes. Los lados del pequeño son 3, 4 y 5; en el grande, el lado correspondiente al 3 mide 6 y se busca el lado x correspondiente al 5."),
  [("1", t("Write the proportion.", "Se plantea la proporción."), f"{fx(3, 6)} = {fx(5, 'x')}."),
   ("2", t("Cross multiply.", "Multiplicación cruzada."), t("3 · x = 6 · 5, that is, 3x = 30.", "3 · x = 6 · 5, es decir 3x = 30.")),
   ("3", t("Solve.", "Se despeja."), "x = 10."),
   ("✓", t("Answer.", "Respuesta."), t("The unknown side measures <strong>10</strong>.", "El lado desconocido mide <strong>10</strong>."))])}
{caja("ojo", t("Match the sides correctly", "Emparejar bien los lados"), t("<p>In the proportion, each side of the small figure goes with its matching side of the large one, always in the same order: small over large in both fractions, or large over small in both. Mixing the order gives a wrong answer.</p>", "<p>En la proporción, cada lado del pequeño debe ir con su correspondiente del grande, siempre en el mismo orden (pequeño sobre grande en las dos fracciones, o grande sobre pequeño en las dos). Mezclar el orden da un resultado incorrecto.</p>"))}
{practica("p1", t("Practice 1 — Scale factor", "Práctica 1 — Factor de escala"), t("What is the scale factor if a side of 5 matches a side of 15?", "¿Cuál es el factor de escala si un lado de 5 corresponde a uno de 15?"), [("a", "×2"), ("b", "×3"), ("c", "×10")])}
{practica("p2", t("Practice 2 — A matching side", "Práctica 2 — Un lado correspondiente"), t("With a scale factor of ×3, the side that matches 4 measures…", "Con un factor de escala ×3, el lado correspondiente al 4 mide…"), [("a", "12"), ("b", "7"), ("c", "1.33")])}
{practica("p3", t("Practice 3 — The missing side", "Práctica 3 — El lado que falta"), t("Triangles 3-4-5 and 6-8-x are similar. What is the value of x?", "Los triángulos 3-4-5 y 6-8-x son semejantes. ¿Cuánto vale x?"), [("a", "7"), ("b", "9"), ("c", "10")])}
{enlace(n, t("proportion", "proporcion"), t("finding a side with a proportion", "hallar un lado con una proporción"), t("Write and solve the proportion between corresponding sides.", "Plantee y resuelva la proporción entre lados correspondientes."))}'''

    s3 = f'''<p>{t("A map or a floor plan is a <strong>scale drawing</strong>: a similar, smaller version of something real. The scale tells how much of the real thing each unit of the drawing stands for.", "Un mapa o un plano es un <strong>dibujo a escala</strong>: una versión semejante, más pequeña, de algo real. La escala indica a cuánto de la realidad equivale cada unidad del dibujo.")}</p>
{ejemplo(t("Example 2: a map of Illinois. On a map, 1 inch stands for 5 miles. Two places are 4 inches apart on the map. What is the real distance?", "Ejemplo 2 · Mapa de Illinois. En un mapa, 1 pulgada representa 5 millas. Dos lugares están a 4 pulgadas en el mapa. ¿Cuál es la distancia real?"),
  [("1", t("Each inch is worth 5 miles.", "Cada pulgada vale 5 millas."), t("Multiply: 4 × 5 = 20.", "Se multiplica: 4 × 5 = 20.")),
   ("✓", t("Answer.", "Respuesta."), t("The real distance is <strong>20 miles</strong>.", "La distancia real es de <strong>20 millas</strong>."))])}
{ejemplo(t("Example 3: a floor plan at a scale of 1:100. A real wall measures 300 inches. How long is it on the plan?", "Ejemplo 3 · Plano a escala 1:100. Una pared real mide 300 pulgadas. ¿Cuánto mide en el plano?"),
  [("1", t("A scale of 1:100 means the plan is 100 times smaller.", "La escala 1:100 significa que el plano es 100 veces más pequeño."), t("Divide by 100.", "Se divide entre 100.")),
   ("2", t("Divide.", "Se divide."), "300 ÷ 100 = 3."),
   ("✓", t("Answer.", "Respuesta."), t("On the plan, the wall measures <strong>3 inches</strong>.", "En el plano, la pared mide <strong>3 pulgadas</strong>."))])}
{caja("tip", t("Multiply or divide?", "¿Multiplicar o dividir?"), t("<p>From the drawing to the real thing, the measure grows: multiply. From the real thing to the drawing, the measure shrinks: divide. A scale like 1:100 uses the same unit on both sides; a scale like 1 inch = 5 miles uses two different units.</p>", "<p>Del dibujo a la realidad, la medida crece: se multiplica. De la realidad al dibujo, la medida se achica: se divide. Una escala como 1:100 usa la misma unidad de los dos lados; una escala como 1 pulgada = 5 millas usa dos unidades distintas.</p>"))}
{enlace(n, t("scale", "escala"), t("scale drawings", "dibujos a escala"), t("Convert measures on maps and plans to real measures.", "Convierta medidas de mapas y planos a medidas reales."))}'''

    s4 = f'''<p>{t("Thales' theorem lets you find heights or distances that cannot be measured directly, using the proportion between an object and its shadow (or between a known reference and the unknown).", "El teorema de Tales permite hallar alturas o distancias que no se pueden medir directamente, usando la proporción entre una figura y su sombra (o entre una referencia conocida y la incógnita).")}</p>
{figura_sombra()}
{ejemplo(t("Example 4: the height of a tree. A 4-foot post casts a 6-foot shadow. At the same time, a tree casts a 24-foot shadow. How tall is the tree?", "Ejemplo 4 · La altura del árbol. Un poste de 4 pies proyecta una sombra de 6 pies. A la misma hora, un árbol proyecta una sombra de 24 pies. ¿Qué altura tiene el árbol?"),
  [("1", t("Write the proportion of height to shadow.", "Se plantea la proporción entre altura y sombra."), f"{fx(4, 6)} = {fx('x', 24)}."),
   ("2", t("Cross multiply.", "Multiplicación cruzada."), t("6 · x = 4 · 24, that is, 6x = 96.", "6 · x = 4 · 24, es decir 6x = 96.")),
   ("3", t("Solve.", "Se despeja."), "x = 16."),
   ("✓", t("Answer.", "Respuesta."), t("The tree is <strong>16 feet</strong> tall.", "El árbol mide <strong>16 pies</strong> de alto."))])}
{caja("ojo", t("Same time, same proportion", "La misma hora, la misma proporción"), t("<p>The shadow method works because, at the same time of day, the sun's rays hit everything at the same angle. So the object and its shadow form a triangle similar to the one formed by the reference and its shadow. Thales' theorem says it in general: parallel lines cut two transversals into proportional segments.</p>", "<p>El método de la sombra funciona porque, a la misma hora, los rayos del sol forman el mismo ángulo con todo. Así, el objeto y su sombra forman un triángulo semejante al de la referencia y su sombra. El teorema de Tales lo dice en general: rectas paralelas cortan dos transversales en segmentos proporcionales.</p>"))}
{practica("p4", t("Practice 4 — On a map", "Práctica 4 — En un mapa"), t("On a map, 1 inch = 2 miles. How many miles do 5 inches stand for?", "En un mapa, 1 pulgada = 2 millas. ¿A cuántas millas equivalen 5 pulgadas?"), [("a", f"7 {mi}"), ("b", f"10 {mi}"), ("c", f"2.5 {mi}")])}
{practica("p5", t("Practice 5 — A tree's shadow", "Práctica 5 — La sombra de un árbol"), t("A 6-foot post casts a 4-foot shadow; a tree casts a 16-foot shadow. The height of the tree is…", "Un poste de 6 pies da una sombra de 4 pies; un árbol da una sombra de 16 pies. La altura del árbol es…"), [("a", f"18 {pies}"), ("b", f"10.7 {pies}"), ("c", f"24 {pies}")])}
{practica("p6", t("Practice 6 — A floor plan", "Práctica 6 — Un plano"), t("Scale 1:50. A real wall 200 inches long appears on the plan as…", "Escala 1:50. Una pared real de 200 pulgadas aparece en el plano como…"), [("a", t("4 inches", "4 pulgadas")), ("b", t("40 inches", "40 pulgadas")), ("c", t("100 inches", "100 pulgadas"))])}
{enlace(n, t("thales", "tales"), t("Thales' theorem", "el teorema de Tales"), t("Find heights and distances indirectly.", "Calcule alturas y distancias de forma indirecta."))}'''

    secciones = [("s-" + t("similar", "semejantes"), t("Similar figures", "Figuras semejantes"), s1),
                 ("s-" + t("proportion", "proporcion"), t("Solving proportions to find a side", "Resolver proporciones para hallar un lado"), s2),
                 ("s-" + t("scale", "escala"), t("Scale drawings", "Dibujos a escala"), s3),
                 ("s-" + t("thales", "tales"), t("Thales' theorem: indirect measurement", "El teorema de Tales: medidas indirectas"), s4)]

    lesson = {"next": t("Lesson 7.1", "Lección 7.1"), "review": t("sections 2 and 4", "las secciones 2 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Divide, do not guess: 15 ÷ 5.", "Divida: 15 ÷ 5."), "c": t("The scale factor comes from dividing, not subtracting.", "El factor de escala se obtiene dividiendo, no restando.")}, "right": "15 ÷ 5 = 3.", "solution": "15 ÷ 5 = 3."},
      "p2": {"ok": "a", "hints": {"b": t("The factor multiplies; you do not add it.", "El factor multiplica; no se suma."), "c": t("The factor ×3 makes the side bigger: multiply.", "El factor ×3 agranda el lado: se multiplica.")}, "right": "4 × 3 = 12.", "solution": "4 × 3 = 12."},
      "p3": {"ok": "c", "hints": {"a": t("Sides do not grow by adding the same amount: they are multiplied by the same factor.", "Los lados no crecen sumando la misma cantidad: se multiplican por el mismo factor."), "b": t("Find the factor: 6 ÷ 3 = 2. Then 5 × 2.", "Halle el factor: 6 ÷ 3 = 2. Después 5 × 2.")}, "right": t("The factor is 2, so x = 5 × 2 = 10.", "El factor es 2, así que x = 5 × 2 = 10."), "solution": "x = 5 × 2 = 10."},
      "p4": {"ok": "b", "hints": {"a": t("Each inch is worth 2 miles: multiply, do not add.", "Cada pulgada vale 2 millas: se multiplica, no se suma."), "c": t("From the map to the real thing, the distance grows: multiply.", "Del mapa a la realidad la distancia crece: se multiplica.")}, "right": t("5 × 2 = 10 miles.", "5 × 2 = 10 millas."), "solution": t("5 × 2 = 10 miles.", "5 × 2 = 10 millas.")},
      "p5": {"ok": "c", "hints": {"a": t("Do not add: write the proportion 6/4 = x/16.", "No se suma: plantee la proporción 6/4 = x/16."), "b": t("Check the order: height over shadow in both fractions.", "Revise el orden: altura sobre sombra en las dos fracciones.")}, "right": t("6/4 = x/16, 4x = 96, x = 24 feet.", "6/4 = x/16, 4x = 96, x = 24 pies."), "solution": t("4x = 96, x = 24 feet.", "4x = 96, x = 24 pies.")},
      "p6": {"ok": "a", "hints": {"b": t("Check the division: 200 ÷ 50.", "Revise la división: 200 ÷ 50."), "c": t("The plan is 50 times smaller: divide by 50, not by 2.", "El plano es 50 veces más pequeño: se divide entre 50, no entre 2.")}, "right": "200 ÷ 50 = 4.", "solution": t("200 ÷ 50 = 4 inches.", "200 ÷ 50 = 4 pulgadas.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("Supplementary angles add up to 180°. Similar figures have the same shape.", "Los suplementarios suman 180°. Las figuras semejantes tienen la misma forma."), "b": t("The sides are proportional; the angles stay the same.", "Los lados son proporcionales; los ángulos se mantienen."), "d": t("If the angles changed, the shape would change.", "Si los ángulos cambiaran, cambiaría la forma.")}, "solution": t("They are equal.", "Son iguales.")},
      "B": {"ok": "a", "hints": {"b": t("Divide: 6 ÷ 3.", "Divida: 6 ÷ 3."), "c": t("Divide the large side by the small one: 6 ÷ 3.", "Divida el lado grande entre el pequeño: 6 ÷ 3."), "d": t("That is small ÷ large. Divide the large side by the small one.", "Eso es pequeño ÷ grande. Divida el grande entre el pequeño.")}, "solution": "6 ÷ 3 = 2."},
      "C": {"ok": "d", "hints": {"a": t("The factor multiplies; you do not add it.", "El factor multiplica; no se suma."), "b": t("×2 makes it bigger: multiply.", "×2 lo agranda: se multiplica."), "c": t("Multiply by 2, not by 5.", "Se multiplica por 2, no por 5.")}, "solution": "5 × 2 = 10."},
      "D": {"ok": "b", "hints": {"a": t("Multiply, do not add.", "Se multiplica, no se suma."), "c": t("From the map to the real thing, multiply.", "Del mapa a la realidad se multiplica."), "d": t("Multiply 4 × 5.", "Multiplique 4 × 5.")}, "solution": t("4 × 5 = 20 miles.", "4 × 5 = 20 millas.")},
      "E": {"ok": "b", "hints": {"a": t("Divide by 100, not by 10.", "Se divide entre 100, no entre 10."), "c": t("That is the real wall. On the plan it is 100 times smaller.", "Esa es la pared real. En el plano es 100 veces más pequeña."), "d": t("Check the division: 300 ÷ 100.", "Revise la división: 300 ÷ 100.")}, "solution": t("300 ÷ 100 = 3 inches.", "300 ÷ 100 = 3 pulgadas.")},
      "F": {"ok": "c", "hints": {"a": t("Check the order: height over shadow in both fractions, 4/6 = x/24.", "Revise el orden: altura sobre sombra en las dos fracciones, 4/6 = x/24."), "b": t("Write the proportion 4/6 = x/24 and cross multiply.", "Plantee 4/6 = x/24 y multiplique en cruz."), "d": t("Do not just multiply 4 × 24: divide by the post's shadow.", "No basta con 4 × 24: hay que dividir entre la sombra del poste.")}, "solution": t("6x = 96, x = 16 feet.", "6x = 96, x = 16 pies.")},
      "G": {"ok": "a", "hints": {"b": t("Check the order: height over shadow in both fractions.", "Revise el orden: altura sobre sombra en las dos fracciones."), "c": t("Do not add: write the proportion 6/4 = x/40.", "No se suma: plantee la proporción 6/4 = x/40."), "d": t("That is the building's shadow. The building is taller than its shadow, like the person.", "Esa es la sombra del edificio. El edificio es más alto que su sombra, igual que la persona.")}, "solution": t("4x = 240, x = 60 feet.", "4x = 240, x = 60 pies.")},
      "H": {"ok": "a", "hints": {"b": t("Check the order: 12/18 = 6/x.", "Revise el orden: 12/18 = 6/x."), "c": t("The pole is half the tower, so its shadow is half the tower's shadow.", "El poste es la mitad de la torre, así que su sombra es la mitad de la sombra de la torre."), "d": t("The pole is half as tall: its shadow is half of 18.", "El poste mide la mitad: su sombra es la mitad de 18.")}, "solution": t("12x = 108, x = 9 feet.", "12x = 108, x = 9 pies.")}
     }}

    quiz = [
     ("A", t("In similar figures, the corresponding angles are…", "En figuras semejantes, los ángulos correspondientes son…"), [("a", t("supplementary", "suplementarios")), ("b", t("proportional", "proporcionales")), ("c", t("equal", "iguales")), ("d", t("different", "distintos"))]),
     ("B", t("Similar triangles: a side of 3 matches a side of 6. What is the scale factor?", "Triángulos semejantes: un lado de 3 corresponde a uno de 6. ¿Factor de escala?"), [("a", "×2"), ("b", "×3"), ("c", "×1.5"), ("d", "×0.5")]),
     ("C", t("With a scale factor of ×2, the side that matches 5 measures…", "Con factor de escala ×2, el lado correspondiente al 5 mide…"), [("a", "7"), ("b", "2.5"), ("c", "25"), ("d", "10")]),
     ("D", t("On a map, 1 inch = 5 miles. Two cities are 4 inches apart on the map. The real distance is…", "En un mapa, 1 pulgada = 5 millas. Dos ciudades están a 4 pulgadas. La distancia real es…"), [("a", f"9 {mi}"), ("b", f"20 {mi}"), ("c", f"1.25 {mi}"), ("d", f"45 {mi}")]),
     ("E", t("Scale 1:100. A real wall 300 inches long appears on the plan as…", "Escala 1:100. Una pared real de 300 pulgadas aparece en el plano como…"), [("a", t("30 inches", "30 pulgadas")), ("b", t("3 inches", "3 pulgadas")), ("c", t("300 inches", "300 pulgadas")), ("d", t("0.3 inches", "0.3 pulgadas"))]),
     ("F", t("A 4-foot post casts a 6-foot shadow; a tree casts a 24-foot shadow. The height of the tree is…", "Un poste de 4 pies da una sombra de 6 pies; un árbol da una sombra de 24 pies. La altura del árbol es…"), [("a", f"36 {pies}"), ("b", f"12 {pies}"), ("c", f"16 {pies}"), ("d", f"96 {pies}")]),
     ("G", t("A 6-foot person casts a 4-foot shadow; a building casts a 40-foot shadow. The height of the building is…", "Una persona de 6 pies da una sombra de 4 pies; un edificio da una sombra de 40 pies. La altura del edificio es…"), [("a", f"60 {pies}"), ("b", f"26.7 {pies}"), ("c", f"46 {pies}"), ("d", f"40 {pies}")]),
     ("H", t("A 12-foot tower casts an 18-foot shadow. At the same time, what shadow does a 6-foot pole cast?", "Una torre de 12 pies da una sombra de 18 pies. ¿Qué sombra da un poste de 6 pies a la misma hora?"), [("a", f"9 {pies}"), ("b", f"4 {pies}"), ("c", f"36 {pies}"), ("d", f"12 {pies}")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Recognize similar figures, use proportions to find unknown sides, read map and plan scales, and measure heights you cannot reach.", "Reconozca figuras semejantes, use proporciones para hallar lados desconocidos, interprete escalas de mapas y planos y mida alturas inalcanzables."),
        ("📏", t("Proportions, scales, and shadows", "Proporciones, escalas y sombras")),
        [t("<strong>Recognize</strong> similar figures: equal angles and proportional sides.", "<strong>Reconocer</strong> figuras semejantes: ángulos iguales y lados proporcionales."),
         t("<strong>Find</strong> the scale factor between two similar figures.", "<strong>Hallar</strong> el factor de escala entre dos figuras semejantes."),
         t("<strong>Solve</strong> proportions to find an unknown side.", "<strong>Resolver</strong> proporciones para hallar un lado desconocido."),
         t("<strong>Read</strong> the scales of maps and floor plans.", "<strong>Interpretar</strong> escalas de mapas y planos."),
         t("<strong>Use</strong> Thales' theorem to measure heights and distances indirectly.", "<strong>Usar</strong> el teorema de Tales para medir alturas y distancias de forma indirecta.")],
        secciones,
        (t(f"Solve three exercises that find a side with a proportion, three on map and plan scales, and two that measure a height with shadows. Then try {explora} and the practice page.",
           f"Resuelva tres ejercicios de hallar un lado con una proporción, tres de escalas de mapas y planos y dos de medir una altura con sombras. Después pruebe {explora} y la página de práctica."),
         t("On a sunny day, measure your own shadow and the shadow of a tree, a pole, or a building at the same time. Use your height and the proportion of height to shadow to find how tall the object is. Then find the scale on a map of your city and work out the real distance between your home and a place you go often.",
           "En un día de sol, mida su propia sombra y la sombra de un árbol, un poste o un edificio a la misma hora. Use su estatura y la proporción entre altura y sombra para hallar cuánto mide el objeto. Después busque la escala en un mapa de su ciudad y calcule la distancia real entre su casa y un lugar al que va con frecuencia.")),
        quiz,
        t("Self-check checklist for similarity and scale", "Lista de autoevaluación de semejanza y escalas"),
        t("Self-check checklist: skills for similar figures, scale drawings, and Thales' theorem", "Lista de autoevaluación: destrezas de figuras semejantes, dibujos a escala y el teorema de Tales"),
        [(t("Writing the proportion", "Plantear la proporción"), t("I write the proportion with the corresponding sides matched in the same order.", "Planteo la proporción emparejando los lados correspondientes en el mismo orden."), t("I write it with the order mixed up at times.", "La planteo con el orden mezclado a veces."), t("I do not know how to write the proportion.", "No sé plantear la proporción.")),
         (t("Solving for the side", "Despejar el lado"), t("I cross multiply and solve without mistakes.", "Multiplico en cruz y despejo sin errores."), t("I solve with some mistakes.", "Despejo con algún error."), t("I do not solve the proportion.", "No resuelvo la proporción.")),
         (t("Using scales", "Usar escalas"), t("I decide correctly whether to multiply or divide with a scale.", "Decido bien si multiplicar o dividir con una escala."), t("I sometimes multiply when I should divide.", "A veces multiplico cuando debo dividir."), t("I do not understand what the scale means.", "No entiendo lo que significa la escala.")),
         (t("Indirect measurement", "Medidas indirectas"), t("I use the height-to-shadow proportion to find a height I cannot measure.", "Uso la proporción entre altura y sombra para hallar una altura que no puedo medir."), t("I mix up heights and shadows in the proportion.", "Mezclo alturas y sombras en la proporción."), t("I do not use the method.", "No uso el método."))],
        t("<p>This lesson closes Topic 6. You studied similar figures, their scale factor, and the proportions between their sides; you read the scales of maps and plans; and you measured heights you cannot reach with Thales' theorem. With angles, the Pythagorean theorem, and similarity, you now have the basic tools of geometry for the GED test.</p>\n<p>Topic 7 moves from flat figures to solids. It opens with <strong>Lesson 7.1 · Volume of prisms and cylinders</strong>.</p>",
          "<p>Con esta lección se cierra el Tema 6. Se estudiaron las figuras semejantes, su factor de escala y las proporciones entre sus lados; se interpretaron las escalas de mapas y planos; y se midieron alturas inalcanzables con el teorema de Tales. Con los ángulos, el teorema de Pitágoras y la semejanza, ya se tienen las herramientas básicas de geometría para el examen GED.</p>\n<p>El Tema 7 pasa de las figuras planas a los cuerpos sólidos. Abre con la <strong>Lección 7.1 · Volumen de prismas y cilindros</strong>.</p>"),
        ("7-1", ("", t("Lesson 7.1 · Volume of prisms and cylinders", "Lección 7.1 · Volumen de prismas y cilindros"))),
        [(t("similar figures", "figuras semejantes"), t("Figures with the same shape but possibly a different size: equal angles and proportional sides.", "Figuras con la misma forma, aunque pueden tener distinto tamaño: ángulos iguales y lados proporcionales.")),
         (t("congruent figures", "figuras congruentes"), t("Figures with the same shape and the same size.", "Figuras con la misma forma y el mismo tamaño.")),
         (t("scale factor", "factor de escala"), t("The number you multiply a side by to get the matching side of the similar figure.", "El número por el que se multiplica un lado para obtener el lado correspondiente de la figura semejante.")),
         (t("proportion", "proporción"), t("An equation that says two ratios are equal, like 3/6 = 5/10.", "Una igualdad entre dos razones, como 3/6 = 5/10.")),
         (t("scale drawing", "dibujo a escala"), t("A drawing similar to a real object, like a map or a floor plan.", "Un dibujo semejante a un objeto real, como un mapa o un plano."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var U = {in: T("inches", "pulgadas"), ft: T("feet", "pies"), mi: T("miles", "millas")};
/* MODULE 1 · Similar triangles */
function pintaSJ(){
  var l = $("sj-t").value.split(",").map(Number), k = +$("sj-k").value, a = l[0], b = l[1], c = l[2];
  $("sj-kv").textContent = "×" + nm(k); $("sj-k").setAttribute("aria-valuetext", T("times ", "por ") + nm(k));
  var v1 = verticesDe(a, b, c), v2 = verticesDe(a * k, b * k, c * k), esc = 500 / (c * (1 + k) * 1.1);
  var x0 = 40, y0 = 250, x1 = x0 + c * esc + 40;
  function V(v, ox){ return [ox + v[0] * esc, y0 - v[1] * esc]; }
  function tri(v, ox, fill, st){ return '<polygon points="' + v.map(function(p){ var q = V(p, ox); return f1(q[0]) + "," + f1(q[1]); }).join(" ") + '" fill="' + fill + '" stroke="' + st + '" stroke-width="3"/>'; }
  function rotulos(v, ox, lados, col){
    var s = "", pares = [[1, 2, 0], [2, 0, 1], [0, 1, 2]], cc = V([(v[0][0] + v[1][0] + v[2][0]) / 3, (v[0][1] + v[1][1] + v[2][1]) / 3], ox);
    pares.forEach(function(p){ var m = V([(v[p[0]][0] + v[p[1]][0]) / 2, (v[p[0]][1] + v[p[1]][1]) / 2], ox), d = [m[0] - cc[0], m[1] - cc[1]], n = Math.hypot(d[0], d[1]) || 1;
      s += texto([m[0] + d[0] / n * 16, m[1] + d[1] / n * 16], nm(lados[p[2]]), 16, col); });
    return s;
  }
  var top = y0 - Math.max(v1[2][1] * esc, v2[2][1] * esc) - 30, H = y0 + 26 - top;
  var s = '<svg class="geo-svg" viewBox="0 ' + f1(top) + " 640 " + f1(H) + '" role="img" aria-label="' + T("Original triangle with sides " + a + ", " + b + ", and " + c + ", and a similar triangle with sides " + nm(a * k) + ", " + nm(b * k) + ", and " + nm(c * k) + ".", "Triángulo original de lados " + a + ", " + b + " y " + c + ", y triángulo semejante de lados " + nm(a * k) + ", " + nm(b * k) + " y " + nm(c * k) + ".") + '">';
  s += tri(v1, x0, "#e3f2fd", "#0d47a1") + rotulos(v1, x0, [a, b, c], "#0d47a1");
  s += tri(v2, x1, "#efebe9", "#4e342e") + rotulos(v2, x1, [a * k, b * k, c * k], "#3e2723");
  $("sj-svg").innerHTML = s + "</svg>";
  var ang = angulosDe(a, b, c).map(function(g){ return aprox(g, 1) + "°"; });
  $("sj-tabla").innerHTML = '<table class="comparar"><caption>' + T("Corresponding sides and angles", "Lados y ángulos correspondientes") + '</caption><thead><tr><th scope="col">' + T("Original side", "Lado original") + '</th><th scope="col">' + T("New side", "Lado nuevo") + '</th><th scope="col">' + T("New ÷ original", "Nuevo ÷ original") + "</th></tr></thead><tbody>" +
    [a, b, c].map(function(x){ return "<tr><td>" + x + "</td><td>" + nm(x * k) + "</td><td>" + nm(k) + "</td></tr>"; }).join("") + "</tbody></table>" +
    '<p class="nota">' + T("The angles measure " + ang.join(", ") + " in both triangles: the scale factor does not change them.", "Los ángulos miden " + ang.join(", ") + " en los dos triángulos: no cambian con el factor de escala.") + "</p>";
}
function genFactor(){
  var tp = aleatorio(1, 3), a = aleatorio(2, 9), k = elige([2, 3, 4, 5, 0.5]), o, pc = {};
  if (tp === 1){ var b = a * k;
    o = [{html: "×" + nm(k), clave: "k" + k}, {html: "×" + nm(b - a), clave: "k" + (b - a)}, {html: "×" + nm(a / b), clave: "k" + (a / b)}, {html: "×" + nm(a * b), clave: "k" + (a * b)}];
    pc["k" + (b - a)] = T("You get the scale factor by dividing, not by subtracting.", "El factor de escala se obtiene dividiendo, no restando."); pc["k" + (a / b)] = T("Divide the new side by the original, not the other way around.", "Se divide el lado nuevo entre el original, no al revés."); pc["k" + (a * b)] = T("Divide the sides; do not multiply them.", "Los lados se dividen, no se multiplican.");
    return {enun: T("A side of " + a + " inches matches a side of " + nm(b) + " inches in a similar figure. What is the scale factor?", "Un lado de " + a + " pulgadas corresponde, en una figura semejante, a un lado de " + nm(b) + " pulgadas. ¿Cuál es el factor de escala?"), opciones: o, correcta: "k" + k, porClave: pc,
      pista: T("Divide the new side by the original side.", "Divida el lado nuevo entre el original."), bien: nm(b) + " ÷ " + a + " = " + nm(k) + ".", mal: T("Divide the new side by the original: ", "Se divide el lado nuevo entre el original: ") + nm(b) + " ÷ " + a + " = " + nm(k) + "."}; }
  if (tp === 2){ var r = a * k;
    o = [{html: nm(r), clave: "n" + r}, {html: nm(a + k), clave: "n" + (a + k)}, {html: nm(a / k), clave: "n" + (a / k)}, {html: nm(r + 1), clave: "n" + (r + 1)}];
    pc["n" + (a + k)] = T("The factor multiplies; you do not add it.", "El factor multiplica; no se suma."); pc["n" + (a / k)] = T("Multiply by the factor; do not divide.", "Se multiplica por el factor; no se divide.");
    return {enun: T("With a scale factor of ×" + nm(k) + ", how long is the side that matches a side of " + a + " inches?", "Con un factor de escala ×" + nm(k) + ", ¿cuánto mide el lado correspondiente a uno de " + a + " pulgadas?"), opciones: o, correcta: "n" + r, porClave: pc,
      pista: T("The scale factor is the number you multiply by.", "El factor de escala es el número por el que se multiplica."), bien: a + " × " + nm(k) + " = " + nm(r) + ".", mal: T("Multiply by the factor: ", "Se multiplica por el factor: ") + a + " × " + nm(k) + " = " + nm(r) + "."}; }
  var tr = elige([[3, 4, 5], [4, 5, 6], [5, 12, 13], [6, 8, 9]]), kk = elige([2, 3]), falt = tr[2] * kk, sumado = tr[2] + tr[0] * kk - tr[0];
  o = [{html: String(falt), clave: "n" + falt}, {html: String(sumado), clave: "n" + sumado}, {html: String(falt + 1), clave: "n" + (falt + 1)}, {html: String(tr[2] * kk * kk), clave: "n" + tr[2] * kk * kk}];
  pc["n" + sumado] = T("Sides of similar figures do not grow by adding the same amount: they are multiplied by the same factor.", "Entre figuras semejantes los lados no aumentan sumando la misma cantidad: se multiplican por el mismo factor.");
  return {enun: T("Two similar triangles have sides " + tr.join(", ") + " and " + (tr[0] * kk) + ", " + (tr[1] * kk) + ", x. What is the value of x?", "Dos triángulos semejantes tienen lados " + tr.join(", ") + " y " + (tr[0] * kk) + ", " + (tr[1] * kk) + ", x. ¿Cuánto vale x?"), opciones: o, correcta: "n" + falt, porClave: pc,
    pista: T("Find the scale factor first: " + (tr[0] * kk) + " ÷ " + tr[0] + ".", "Halle primero el factor de escala: " + (tr[0] * kk) + " ÷ " + tr[0] + "."),
    bien: T("The factor is ", "El factor es ") + (tr[0] * kk) + " ÷ " + tr[0] + " = " + kk + T(", so x = ", ", así que x = ") + tr[2] + " × " + kk + " = " + falt + ".", mal: T("The factor is " + kk + ": x = ", "El factor es " + kk + ": x = ") + tr[2] + " × " + kk + " = " + falt + "."};
}

/* MODULE 2 · Proportion */
function problemaProp(){
  var tr = elige([[3, 4, 5], [4, 6, 8], [5, 7, 9], [2, 5, 6], [6, 8, 10]]), k = elige([2, 3, 1.5, 2.5, 4]), i = aleatorio(0, 2), j; do { j = aleatorio(0, 2); } while (j === i);
  var gra = tr.map(function(x){ return x * k; }), deGrande = Math.random() < 0.5;
  return {peq: tr, gra: gra, i: i, j: j, deGrande: deGrande, x: deGrande ? gra[j] : tr[j]};
}
function textoProp(q){
  var nom = [T("first", "primer"), T("second", "segundo"), T("third", "tercer")];
  return T("Two triangles are similar. In the small one, the " + nom[q.i] + " side measures " + nm(q.peq[q.i]) + " and the " + nom[q.j] + " measures " + (q.deGrande ? nm(q.peq[q.j]) : "x") + ". In the large one, the corresponding sides measure " + nm(q.gra[q.i]) + " and " + (q.deGrande ? "x" : nm(q.gra[q.j])) + ". What is the value of x?",
           "Dos triángulos son semejantes. En el pequeño, el " + nom[q.i] + " lado mide " + nm(q.peq[q.i]) + " y el " + nom[q.j] + " mide " + (q.deGrande ? nm(q.peq[q.j]) : "x") + ". En el grande, los lados correspondientes miden " + nm(q.gra[q.i]) + " y " + (q.deGrande ? "x" : nm(q.gra[q.j])) + ". ¿Cuánto vale x?");
}
function pasosProp(q){
  var a = nm(q.peq[q.i]), A = nm(q.gra[q.i]), b = q.deGrande ? nm(q.peq[q.j]) : "x", B = q.deGrande ? "x" : nm(q.gra[q.j]);
  var cruz = q.deGrande ? a + " · x = " + A + " · " + b : A + " · x = " + a + " · " + B;
  var prod = q.deGrande ? q.gra[q.i] * q.peq[q.j] : q.peq[q.i] * q.gra[q.j], coef = q.deGrande ? q.peq[q.i] : q.gra[q.i];
  return [T("Write the proportion, small over large in both fractions: ", "Se plantea la proporción, pequeño sobre grande en las dos fracciones: ") + auto(Qf(a, A) + " = " + Qf(b, B)) + ".",
    T("Cross multiply: ", "Multiplicación cruzada: ") + auto(cruz) + T(", that is, ", ", es decir ") + auto(nm(coef) + "x = " + nm(prod)) + ".",
    T("Solve: x = ", "Se despeja: x = ") + nm(prod) + " ÷ " + nm(coef) + " = " + nm(q.x) + ".",
    '<span class="veredicto">x = ' + nm(q.x) + T(". Check: the scale factor is ", ". Comprobación: el factor de escala es ") + nm(q.gra[q.i] / q.peq[q.i]) + T(" in both pairs of sides.", " en los dos pares de lados.") + "</span>"];
}
var PP_COLA = [{peq: [3, 4, 5], gra: [6, 8, 10], i: 0, j: 2, deGrande: true, x: 10}];
function nuevoPP(){ var q = PP_COLA.length ? PP_COLA.shift() : problemaProp(); $("pp-enun").textContent = textoProp(q); PPS.carga(pasosProp(q)); }
function genProp(){
  var q = problemaProp(), malo = q.deGrande ? q.peq[q.j] * q.peq[q.i] / q.gra[q.i] : q.gra[q.j] * q.gra[q.i] / q.peq[q.i];
  return {enun: textoProp(q), solucion: pasosProp(q).slice(0, 3).join(" "),
    evalua: function(v){ return evaluaDec(v, q.x, [{v: malo, msg: T("It looks like the order in the proportion got mixed up: put small over large in both fractions.", "Parece que se mezcló el orden en la proporción: ponga pequeño sobre grande en las dos fracciones.")}]); }};
}

/* MODULE 3 · Scales */
function pintaES(){
  var tipo = $("es-tipo").value, dir = $("es-dir").value, k = leeDecimal($("es-k").value), m = leeDecimal($("es-m").value), av = $("es-aviso");
  $("es-klab").textContent = tipo === "mapa" ? T("Value of k (miles for each inch)", "Valor de k (millas por cada pulgada)") : T("Value of n", "Valor de n");
  $("es-mlab").textContent = dir === "real" ? (tipo === "mapa" ? T("Measure on the map (inches)", "Medida en el mapa (pulgadas)") : T("Measure on the plan (inches)", "Medida en el plano (pulgadas)")) : (tipo === "mapa" ? T("Real distance (miles)", "Distancia real (millas)") : T("Real measure (inches)", "Medida real (pulgadas)"));
  if (k === null || m === null || k <= 0 || m < 0){ av.className = "caja-aviso visible"; av.textContent = T("Type positive numbers.", "Escriba números positivos."); $("es-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = "";
  var r, h, dib = tipo === "mapa" ? T("map", "mapa") : T("plan", "plano");
  if (dir === "real"){ r = m * k; h = T("Each inch on the " + dib + " is worth " + nm(k) + (tipo === "mapa" ? " miles" : " real inches") + ": multiply. ", "Cada pulgada del " + dib + " vale " + nm(k) + (tipo === "mapa" ? " millas" : " pulgadas reales") + ": se multiplica. ") + nm(m) + " × " + nm(k) + " = <strong>" + nm(r) + " " + (tipo === "mapa" ? U.mi : U.in) + "</strong>" + T(" in real life.", " en la realidad."); }
  else { r = m / k; h = T("The real thing is bigger than the drawing: divide by ", "La realidad es más grande que el dibujo: se divide entre ") + nm(k) + ". " + nm(m) + " ÷ " + nm(k) + " = <strong>" + nm(r) + " " + U.in + "</strong>" + T(" on the " + dib + ".", " en el " + dib + "."); }
  if (tipo === "plano" && dir === "real" && r >= 24) h += T(" That is ", " Es decir, ") + nm(Math.round(r / 12 * 100) / 100) + " " + U.ft + ".";
  $("es-salida").innerHTML = '<div class="linea">' + h + "</div>";
}
function genEscala(){
  var tp = aleatorio(1, 4), k, m, r, enun, sol, pistas = [];
  if (tp === 1){ k = elige([2, 3, 5, 10, 20, 25]); m = elige([2, 3, 4, 5, 6, 7.5, 8]); r = m * k; enun = T("On a map, 1 inch stands for " + k + " miles. Two towns are " + nm(m) + " inches apart on the map. How many miles apart are they in real life?", "En un mapa, 1 pulgada representa " + k + " millas. Dos pueblos están a " + nm(m) + " pulgadas en el mapa. ¿A cuántas millas están en la realidad?"); sol = nm(m) + " × " + k + " = " + nm(r) + " " + U.mi + "."; pistas.push({v: m / k, msg: T("From the map to real life the distance grows: multiply.", "Del mapa a la realidad la distancia crece: se multiplica.")}); }
  else if (tp === 2){ k = elige([2, 4, 5, 10, 25]); r = elige([2, 3, 4, 6, 1.5, 2.5]); m = r * k; enun = T("On a map, 1 inch stands for " + k + " miles. Two cities are " + nm(m) + " miles apart in real life. How many inches apart are they on the map?", "En un mapa, 1 pulgada representa " + k + " millas. Dos ciudades están a " + nm(m) + " millas en la realidad. ¿A cuántas pulgadas están en el mapa?"); sol = nm(m) + " ÷ " + k + " = " + nm(r) + " " + U.in + "."; pistas.push({v: m * k, msg: T("From real life to the map the measure shrinks: divide.", "De la realidad al mapa la medida se achica: se divide.")}); }
  else if (tp === 3){ k = elige([24, 48, 50, 100]); r = elige([2, 3, 4, 5, 6, 8]); m = r * k; enun = T("A floor plan is drawn at a scale of 1:" + k + ". A real wall measures " + nm(m) + " inches. How many inches long is it on the plan?", "Un plano está a escala 1:" + k + ". Una pared real mide " + nm(m) + " pulgadas. ¿Cuántas pulgadas mide en el plano?"); sol = nm(m) + " ÷ " + k + " = " + nm(r) + " " + U.in + "."; pistas.push({v: m * k, msg: T("From real life to the plan, divide.", "De la realidad al plano se divide.")}); }
  else { k = elige([24, 48, 50, 100]); m = elige([1, 1.5, 2, 2.5, 3, 4]); r = m * k; enun = T("A floor plan is drawn at a scale of 1:" + k + ". A sofa measures " + nm(m) + " inches on the plan. How many inches long is it in real life?", "Un plano está a escala 1:" + k + ". Un sofá mide " + nm(m) + " pulgadas en el plano. ¿Cuántas pulgadas mide en la realidad?"); sol = nm(m) + " × " + k + " = " + nm(r) + " " + U.in + " (" + nm(Math.round(r / 12 * 100) / 100) + " " + U.ft + ")."; pistas.push({v: m / k, msg: T("From the plan to real life, multiply.", "Del plano a la realidad se multiplica.")}, {v: r / 12, msg: T("That is the answer in feet. The question asks for inches.", "Esa es la respuesta en pies. La pregunta pide pulgadas.")}); }
  return {enun: enun, solucion: sol, evalua: function(v){ var res = evaluaDec(v, r, pistas); if (res.estado === "mal" && !pistas.some(function(p){ return p.msg === res.msg; })) res.msg = T("From the drawing to real life, multiply; from real life to the drawing, divide.", "Del dibujo a la realidad se multiplica; de la realidad al dibujo se divide."); return res; }};
}

/* MODULE 4 · Shadows */
function pintaTH(){
  var h = +$("th-h").value, s = +$("th-s").value, S = +$("th-S").value, H = h * S / s;
  $("th-hv").textContent = nm(h); $("th-sv").textContent = nm(s); $("th-Sv").textContent = nm(S);
  var esc = Math.min(560 / (s + S + 3), 210 / Math.max(H, h)), y0 = 250, xp = 30, xa = xp + (s + 2) * esc, u = T(" ft", " pies");
  var svg = '<svg class="geo-svg" viewBox="0 0 640 290" role="img" aria-label="' + T("A " + nm(h) + "-foot post with a " + nm(s) + "-foot shadow; a tree with a " + nm(S) + "-foot shadow and a height of " + nm(H) + " feet.", "Poste de " + nm(h) + " pies con sombra de " + nm(s) + " pies; árbol con sombra de " + nm(S) + " pies y altura de " + nm(H) + " pies.") + '">';
  svg += lineaG([20, y0], [620, y0], "#6d4c41", 3);
  svg += lineaG([xp, y0], [xp, y0 - h * esc], "#424242", 6) + lineaG([xp + s * esc, y0], [xp, y0 - h * esc], "#f9a825", 2, ' stroke-dasharray="7 5"');
  svg += lineaG([xp, y0 + 2], [xp + s * esc, y0 + 2], "#212121", 6);
  svg += '<rect x="' + f1(xa - 6) + '" y="' + f1(y0 - H * esc * 0.45) + '" width="12" height="' + f1(H * esc * 0.45) + '" fill="#6d4c41"/>';
  svg += '<ellipse cx="' + f1(xa) + '" cy="' + f1(y0 - H * esc * 0.7) + '" rx="' + f1(Math.max(H * esc * 0.22, 14)) + '" ry="' + f1(H * esc * 0.3) + '" fill="#2e7d32"/>';
  svg += lineaG([xa + S * esc, y0], [xa, y0 - H * esc], "#f9a825", 2, ' stroke-dasharray="7 5"') + lineaG([xa, y0 + 2], [xa + S * esc, y0 + 2], "#212121", 6);
  svg += '<text x="' + f1(xp + 12) + '" y="' + f1(y0 - h * esc / 2) + '" font-size="18" font-weight="700" fill="#222" dominant-baseline="middle">' + nm(h) + u + "</text>";
  svg += texto([xp + s * esc / 2, y0 + 24], nm(s) + u, 18, "#222") + texto([xa + S * esc / 2, y0 + 24], nm(S) + u, 18, "#222");
  svg += '<text x="' + f1(xa + 14) + '" y="' + f1(Math.max(y0 - H * esc - 12, 16)) + '" font-size="18" font-weight="700" fill="#1b5e20">' + T("height = ", "altura = ") + nm(H) + u + "</text>";
  $("th-svg").innerHTML = svg + "</svg>";
  $("th-salida").innerHTML = '<div class="linea">' + T("Proportion: ", "Proporción: ") + auto(Qf(nm(h), nm(s)) + " = " + Qf("x", nm(S))) + T(". Cross multiply: ", ". Multiplicación cruzada: ") + auto(nm(s) + " · x = " + nm(h) + " · " + nm(S)) + ".</div>" +
    '<div class="linea veredicto">x = ' + nm(h * S) + " ÷ " + nm(s) + " = " + nm(H) + T(" feet tall.", " pies de altura.") + "</div>";
}
function genThales(){
  var tp = aleatorio(1, 3), h, s, S, H, enun, r, pistas = [], orden = T("Check the order: height over shadow in both fractions.", "Revise el orden: altura sobre sombra en las dos fracciones.");
  if (tp === 1){ h = elige([3, 4, 5, 6]); s = elige([2, 3, 4, 5, 6]); S = s * elige([2, 3, 4, 5, 6]); H = h * S / s; r = H;
    enun = T("A " + h + "-foot post casts a " + s + "-foot shadow. At the same time, a tree casts a " + S + "-foot shadow. How tall is the tree, in feet?", "Un poste de " + h + " pies proyecta una sombra de " + s + " pies. A la misma hora, un árbol proyecta una sombra de " + S + " pies. ¿Qué altura tiene el árbol, en pies?"); pistas.push({v: s * S / h, msg: orden}); }
  else if (tp === 2){ h = elige([5, 5.5, 6]); s = elige([2, 3, 4]); var k = elige([5, 6, 8, 10, 12]); H = h * k; S = s * k; r = S;
    enun = T("A " + nm(h) + "-foot person casts a " + s + "-foot shadow. At the same time, what shadow does a " + nm(H) + "-foot building cast, in feet?", "Una persona de " + nm(h) + " pies proyecta una sombra de " + s + " pies. A la misma hora, ¿qué sombra proyecta un edificio de " + nm(H) + " pies, en pies?"); pistas.push({v: H * h / s, msg: orden}); }
  else { h = elige([3, 4, 6]); s = elige([4, 5, 8, 9]); var k2 = elige([3, 4, 5, 6]); H = h * k2; S = s * k2; r = H;
    enun = T("A " + h + "-foot stick casts a " + s + "-foot shadow. The shadow of a tower measures " + S + " feet. How tall is the tower, in feet?", "Una vara de " + h + " pies da una sombra de " + s + " pies. La sombra de una torre mide " + S + " pies. ¿Cuánto mide la torre, en pies?"); pistas.push({v: s * S / h, msg: orden}); }
  return {enun: enun, solucion: T("Height-to-shadow proportion: ", "Proporción altura/sombra: ") + auto(Qf(nm(h), nm(s)) + " = " + Qf(nm(H), nm(S))) + T(". The answer is " + nm(r) + " feet.", ". El resultado es " + nm(r) + " pies."),
    evalua: function(v){ var res = evaluaDec(v, r, pistas); if (res.estado === "mal" && res.msg !== orden) res.msg = T("Write height over shadow for both objects, then cross multiply.", "Escriba altura sobre sombra para los dos objetos y multiplique en cruz."); return res; }};
}

/* Start */
$("sj-t").addEventListener("change", pintaSJ); $("sj-k").addEventListener("input", pintaSJ); pintaSJ();
OMR("p1", genFactor);
var PPS = pasoAPaso("pp", []);
$("pp-nuevo").addEventListener("click", nuevoPP); nuevoPP();
creaPracticaLibre("p2", genProp);
["es-tipo", "es-dir"].forEach(function(id){ $(id).addEventListener("change", pintaES); });
["es-k", "es-m"].forEach(function(id){ $(id).addEventListener("input", pintaES); });
pintaES();
creaPracticaLibre("p3", genEscala);
["th-h", "th-s", "th-S"].forEach(function(id){ $(id).addEventListener("input", pintaTH); }); pintaTH();
creaPracticaLibre("p4", genThales);
'''

def practica_pagina():
    n = N
    explora = t('<a href="explore-similar.html">Explore: congruent and similar triangles</a>', '<a href="explorar-semejanza.html">Explorar: triángulos congruentes y semejantes</a>')
    def dec(pid, tit, et, nota):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota}</p>\n        <div class="fila-btn">', 1)
    def rango(i, et, v, mn, mx, st):
        return f'<div class="campo" style="flex:1;min-width:180px;"><label for="{i}">{et} <span id="{i}v"></span></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    mods = [
     (t("similar", "semejantes"), t("Similar figures", "Figuras semejantes"),
      f'''      <p>{t("Two figures are similar when they have the same shape: their corresponding angles are equal and their corresponding sides are proportional. The number that relates them is the <strong>scale factor</strong>: divide a side of the new figure by the matching side of the original.", "Dos figuras son semejantes cuando tienen la misma forma: sus ángulos correspondientes son iguales y sus lados correspondientes son proporcionales. El número que los relaciona es el <strong>factor de escala</strong>: se obtiene dividiendo un lado de la figura nueva entre su correspondiente de la original.")}</p>
      <h3>{t("Make it bigger or smaller", "Agrande y achique")}</h3>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="sj-t">{t("Original triangle", "Triángulo original")}</label><select id="sj-t"><option value="3,4,5">{t("sides 3, 4, and 5", "lados 3, 4 y 5")}</option><option value="4,5,6">{t("sides 4, 5, and 6", "lados 4, 5 y 6")}</option><option value="3,5,7">{t("sides 3, 5, and 7", "lados 3, 5 y 7")}</option><option value="5,5,6">{t("sides 5, 5, and 6", "lados 5, 5 y 6")}</option></select></div>
        <div class="campo" style="flex:1;min-width:200px;"><label for="sj-k">{t("Scale factor:", "Factor de escala:")} <span id="sj-kv"></span></label><input type="range" id="sj-k" min="0.5" max="3" step="0.5" value="2"></div></div></div>
      <div id="sj-svg"></div>
      <div class="tabla-scroll" id="sj-tabla"></div>
      <div class="caja-tip">{t("If the factor is greater than 1, the figure grows; if it is between 0 and 1, it shrinks. The angles never change: that is why the shape stays the same.", "Si el factor es mayor que 1, la figura crece; si está entre 0 y 1, se achica. Los ángulos no cambian nunca: por eso la forma es la misma.")}</div>
      <div class="caja-tip">{t(f"Congruent or similar? Drag the corners of a triangle in {explora}.", f"¿Congruentes o semejantes? Arrastre los vértices de un triángulo en {explora}.")}</div>
{B.om("p1", t("Practice: scale factor and corresponding sides", "Practique: factor de escala y lados correspondientes"))}'''),
     (t("proportion", "proporcion"), t("Finding a side with a proportion", "Hallar un lado con una proporción"),
      f'''      <p>{t("The corresponding sides of two similar figures form a proportion. To find an unknown side, write the proportion and solve it with cross multiplication.", "Los lados correspondientes de dos figuras semejantes forman una proporción. Para hallar un lado desconocido se plantea la proporción y se resuelve con la multiplicación cruzada.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
      <div class="panel">
        <p class="enun" id="pp-enun"></p>
        <div class="fila-btn"><button type="button" class="btn" id="pp-sig"></button><button type="button" class="btn-sec" id="pp-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="pp-nuevo">{t("Another example", "Otro ejemplo")}</button></div>
      </div>
      <div class="pasos" id="pp-pasos" aria-live="polite"></div>
      <div class="caja-tip">{t("Match the sides correctly: in the proportion, each side of one figure goes with its matching side of the other, always in the same order (small over large in both fractions, or large over small in both).", "Empareje bien los lados: en la proporción, cada lado de una figura va con su correspondiente de la otra, y siempre en el mismo orden (pequeño sobre grande en las dos fracciones, o grande sobre pequeño en las dos).")}</div>
{dec("p2", t("Practice: find the unknown side", "Practique: halle el lado desconocido"), t("Length of the side", "Longitud del lado"), t("Type the number; it can be a decimal, like 7.5.", "Escriba el número; puede ser decimal, como 7.5."))}'''),
     (t("scale", "escala"), t("Scale drawings", "Dibujos a escala"),
      f'''      <p>{t("A map or a floor plan is a drawing similar to the real thing, but smaller. The scale tells how much of the real thing each unit of the drawing is worth. It is written in two ways:", "Un mapa o un plano es un dibujo semejante a la realidad, pero más pequeño. La escala indica cuánto de la realidad vale cada unidad del dibujo. Se escribe de dos maneras:")}</p>
      <table class="reglas"><caption>{t("The two ways to write a scale", "Las dos formas de escribir una escala")}</caption>
        <thead><tr><th scope="col">{t("Scale", "Escala")}</th><th scope="col">{t("Meaning", "Significa")}</th><th scope="col">{t("Drawing to real", "Del dibujo a la realidad")}</th><th scope="col">{t("Real to drawing", "De la realidad al dibujo")}</th></tr></thead>
        <tbody><tr><td>{t("1 inch = 5 miles", "1 pulgada = 5 millas")}</td><td>{t("each inch on the map is 5 miles", "cada pulgada del mapa son 5 millas")}</td><td>{t("multiply by 5", "se multiplica por 5")}</td><td>{t("divide by 5", "se divide entre 5")}</td></tr>
        <tr><td>1:100</td><td>{t("the real thing is 100 times bigger, in the same unit", "la realidad es 100 veces más grande, en la misma unidad")}</td><td>{t("multiply by 100", "se multiplica por 100")}</td><td>{t("divide by 100", "se divide entre 100")}</td></tr></tbody></table>
      <h3>{t("Scale converter", "Conversor de escalas")}</h3>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="es-tipo">{t("Kind of scale", "Tipo de escala")}</label><select id="es-tipo"><option value="mapa">{t("Map: 1 inch = k miles", "Mapa: 1 pulgada = k millas")}</option><option value="plano">{t("Plan: 1 : n", "Plano: 1 : n")}</option></select></div>
        <div class="campo"><label for="es-k" id="es-klab"></label><input type="text" inputmode="decimal" class="corto" id="es-k" value="5"></div>
        <div class="campo"><label for="es-dir">{t("Direction", "Dirección")}</label><select id="es-dir"><option value="real">{t("From the drawing to real life", "Del dibujo a la realidad")}</option><option value="dib">{t("From real life to the drawing", "De la realidad al dibujo")}</option></select></div>
        <div class="campo"><label for="es-m" id="es-mlab"></label><input type="text" inputmode="decimal" class="corto" id="es-m" value="4"></div></div>
        <p class="caja-aviso" id="es-aviso" role="alert"></p></div>
{n3.salida("es-salida")}
{dec("p3", t("Practice: maps and plans", "Practique: mapas y planos"), t("Result", "Resultado"), t("Type only the number, in the unit the question asks for.", "Escriba solo el número, en la unidad que pide la pregunta."))}'''),
     (t("thales", "tales"), t("Thales' theorem: indirect measurement", "El teorema de Tales: medidas indirectas"),
      f'''      <p>{t("At the same time of day, the sun's rays reach every object at the same angle. So an object and its shadow form a triangle similar to the one formed by another object and its shadow. With a known reference (a post, a person), you can find the height of something you cannot measure directly.", "A la misma hora, los rayos del sol llegan con el mismo ángulo a todos los objetos. Por eso un objeto y su sombra forman un triángulo semejante al de otro objeto y su sombra. Con una referencia conocida (un poste, una persona) se puede calcular la altura de algo que no se puede medir directamente.")}</p>
{n3.formula(t(fx("height of the post", "shadow of the post") + " = " + fx("height of the tree", "shadow of the tree"), fx("altura del poste", "sombra del poste") + " = " + fx("altura del árbol", "sombra del árbol")))}
      <h3>{t("The tree's shadow", "La sombra del árbol")}</h3>
      <div class="panel"><div class="campos">
        {rango("th-h", t("Height of the post (ft):", "Altura del poste (pies):"), 4, 2, 8, 1)}
        {rango("th-s", t("Shadow of the post (ft):", "Sombra del poste (pies):"), 6, 2, 10, 1)}
        {rango("th-S", t("Shadow of the tree (ft):", "Sombra del árbol (pies):"), 24, 10, 40, 2)}</div></div>
      <div id="th-svg"></div>
{n3.salida("th-salida")}
      <div class="caja-tip">{t("Same time, same proportion: if the shadows were measured at different times, the angle of the sun would change and the triangles would no longer be similar.", "La misma hora, la misma proporción: si se midieran las sombras a horas distintas, el ángulo del sol cambiaría y los triángulos ya no serían semejantes.")}</div>
{dec("p4", t("Practice: indirect measurement", "Practique: medidas indirectas"), t("Result", "Resultado"), t("Type the number; it can be a decimal.", "Escriba el número; puede ser decimal."))}''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO_GEO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Semejanza de figuras y dibujos a escala (teorema de Tales)")
