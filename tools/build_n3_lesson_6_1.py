"""Level 3 · Lesson 6.1 · Angles: relationships and parallel lines cut by a transversal — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_6-1.html and algebra/n3-l6-1.html (GEDparaHispanos). The explore page comes from build_n3_explora_6.py.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import math
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n3
from build_n3_explora_6 import ESTILO as ESTILO_GEO

B.NIVEL = 3
N = "6-1"
TEMA = ("Geometry: angles, the Pythagorean theorem, and similarity", "Geometría: ángulos, teorema de Pitágoras y semejanza")
TIT = ("Angles: relationships and parallel lines cut by a transversal", "Ángulos: relaciones y líneas paralelas cortadas por una transversal")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js")

def figura_transversal(alfa=60):
    """Static SVG for the lesson: same numbering as the practice page (1–4 at r, 5–8 at s)."""
    yA, yB = 95, 235
    dx = 70 / math.tan(math.radians(alfa))
    cA, cB = (320 + dx, yA), (320 - dx, yB)
    def p(c, r, g): return (c[0] + r * math.cos(math.radians(g)), c[1] - r * math.sin(math.radians(g)))
    a, b = p(cB, 95, alfa + 180), p(cA, 95, alfa)
    s = f'<line x1="30" y1="{yA}" x2="610" y2="{yA}" stroke="#424242" stroke-width="3"/><line x1="30" y1="{yB}" x2="610" y2="{yB}" stroke="#424242" stroke-width="3"/>'
    s += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#6a1b9a" stroke-width="3"/>'
    s += f'<text x="600" y="{yA - 14}" font-size="18" font-weight="700" fill="#555" text-anchor="middle">r</text><text x="600" y="{yB - 14}" font-size="18" font-weight="700" fill="#555" text-anchor="middle">s</text>'
    for i in range(1, 9):
        c = cA if i <= 4 else cB
        g = [(alfa + 180) / 2, alfa / 2, 180 + alfa / 2, (alfa + 540) / 2][(i - 1) % 4]
        q = p(c, 40, g)
        s += f'<text x="{q[0]:.1f}" y="{q[1] + 6:.1f}" font-size="18" font-weight="700" text-anchor="middle" fill="#222">{i}</text>'
    return B.svg("0 0 640 330", t("Two parallel lines r and s cut by a transversal. At line r, angles 1 (top left), 2 (top right), 3 (bottom left), and 4 (bottom right). At line s, angles 5, 6, 7, and 8 in the same positions.",
                                  "Dos rectas paralelas r y s cortadas por una transversal. En la recta r, los ángulos 1 (arriba a la izquierda), 2 (arriba a la derecha), 3 (abajo a la izquierda) y 4 (abajo a la derecha). En la recta s, los ángulos 5, 6, 7 y 8 en las mismas posiciones."), s, 600)

def leccion():
    n = N
    explora = t('<a href="explore-angles.html">Explore: angles, parallel lines, and a transversal</a>', '<a href="explorar-angulos.html">Explorar: ángulos, paralelas y una transversal</a>')
    s1 = f'''<p>{t("With Topic 5, the linear algebra of Level 3 is complete. Topic 6 turns to geometry, but algebra does not go away: many angle problems are solved by writing and solving a simple equation, exactly what you learned in Topics 4 and 5. This lesson studies how angles are related, especially the angles formed when a line called a transversal cuts two parallel lines.", "Con el Tema 5 quedó completa el álgebra lineal del Nivel 3. El Tema 6 da un giro hacia la geometría, pero el álgebra no se abandona: muchos problemas de ángulos se resuelven planteando y resolviendo una ecuación sencilla, justo lo aprendido en los Temas 4 y 5. Esta lección estudia cómo se relacionan los ángulos, en especial los que se forman cuando una recta transversal corta dos rectas paralelas.")}</p>
<p>{t("Three relationships come up again and again in geometry:", "Tres relaciones aparecen constantemente en geometría:")}</p>
{tabla(t("Basic angle relationships", "Relaciones básicas entre ángulos"), t("Basic angle relationships", "Relaciones básicas entre ángulos"), [t("Relationship", "Relación"), t("Property", "Propiedad"), t("Example", "Ejemplo")],
  [[t("Complementary", "Complementarios"), t("They add up to 90°", "Suman 90°"), t("30° and 60°", "30° y 60°")],
   [t("Supplementary", "Suplementarios"), t("They add up to 180°", "Suman 180°"), t("110° and 70°", "110° y 70°")],
   [t("Vertical angles", "Opuestos por el vértice"), t("They are equal", "Son iguales"), t("If one measures 50°, the opposite one does too", "Si uno mide 50°, el opuesto también")]])}
{ejemplo(t("Example 1: an angle measures 35°. What is the measure of its complement?", "Ejemplo 1: un ángulo mide 35°. ¿Cuánto mide su complemento?"),
  [("1", t("Complementary angles add up to 90°.", "Los complementarios suman 90°."), "90° − 35° = 55°."),
   ("✓", t("Answer.", "Respuesta."), t("The complement measures <strong>55°</strong>.", "El complemento mide <strong>55°</strong>."))])}
{caja("tip", t("Which is which?", "¿Cuál es cuál?"), t("<p>“Complementary” and “corner” (90°) both start with <strong>c</strong>; “supplementary” and “straight” (180°) both start with <strong>s</strong>. An angle of 90° or more has no complement.</p>", "<p>Para recordar cuál es cuál: «complementarios» y «esquina» (90°) van juntos; «suplementarios» y «recta» (180°) también. Un ángulo de 90° o más no tiene complemento.</p>"))}
{enlace(n, t("basics", "basicos"), t("basic angle relationships", "relaciones básicas entre ángulos"), t("Recognize complementary, supplementary, and vertical angles.", "Reconozca ángulos complementarios, suplementarios y opuestos por el vértice."))}'''

    s2 = f'''<p>{t("When a transversal cuts two parallel lines, eight angles are formed. There are only two measures: all the acute angles are equal, all the obtuse angles are equal, and an acute angle plus an obtuse angle add up to 180°.", "Cuando una recta transversal corta dos rectas paralelas, se forman ocho ángulos. Solo hay dos medidas: los ángulos agudos son todos iguales, los obtusos también, y un agudo más un obtuso suman 180°.")}</p>
{figura_transversal()}
{tabla(t("Angle pairs between two parallel lines cut by a transversal", "Parejas de ángulos entre dos paralelas cortadas por una transversal"), t("Angle pairs between two parallel lines", "Parejas de ángulos entre dos paralelas"), [t("Pair", "Tipo de pareja"), t("Example (in the diagram)", "Ejemplo (según el diagrama)"), t("Property", "Propiedad")],
  [[t("Corresponding", "Correspondientes"), t("1 and 5", "1 y 5"), t("They are equal", "Son iguales")],
   [t("Alternate interior", "Alternos internos"), t("4 and 5", "4 y 5"), t("They are equal", "Son iguales")],
   [t("Alternate exterior", "Alternos externos"), t("1 and 8", "1 y 8"), t("They are equal", "Son iguales")],
   [t("Same-side interior", "Internos del mismo lado"), t("3 and 5", "3 y 5"), t("They add up to 180°", "Suman 180°")],
   [t("Vertical angles", "Opuestos por el vértice"), t("1 and 4", "1 y 4"), t("They are equal", "Son iguales")]])}
{practica("p1", t("Practice 1 — Vertical angles", "Práctica 1 — Opuestos por el vértice"), t("Vertical angles are…", "Los ángulos opuestos por el vértice son…"), [("a", t("supplementary", "suplementarios")), ("b", t("equal", "iguales")), ("c", t("complementary", "complementarios"))])}
{practica("p2", t("Practice 2 — Corresponding angles", "Práctica 2 — Ángulos correspondientes"), t("Corresponding angles between parallel lines…", "Los ángulos correspondientes entre paralelas…"), [("a", t("add up to 180°", "suman 180°")), ("b", t("add up to 90°", "suman 90°")), ("c", t("are equal", "son iguales"))])}
{practica("p3", t("Practice 3 — Same-side interior angles", "Práctica 3 — Internos del mismo lado"), t("Same-side interior angles…", "Los ángulos internos del mismo lado…"), [("a", t("add up to 180°", "suman 180°")), ("b", t("add up to 90°", "suman 90°")), ("c", t("are equal", "son iguales"))])}
{caja("tip", t("Explore the eight angles", "Explore los ocho ángulos"), t(f"<p>In {explora}, tilt the transversal and choose any angle: the page shows which angles are equal to it and which ones add up to 180° with it, and then quizzes you on the relationships.</p>", f"<p>En {explora}, incline la transversal y elija cualquier ángulo: la página muestra cuáles son iguales a él y cuáles suman 180° con él, y después le hace preguntas sobre las relaciones.</p>"))}
{enlace(n, "transversal", t("parallel lines cut by a transversal", "paralelas cortadas por una transversal"), t("Identify the relationship between the eight angles of a transversal.", "Identifique la relación entre los ocho ángulos de una transversal."))}'''

    s3 = f'''<p>{t("If you know one of these relationships, you can find any unknown angle. Sometimes it helps to write an equation, like the ones in Topic 4: “they are equal” gives an equation with =, and “they add up to 180°” or “to 90°” gives a sum.", "Conociendo una de estas relaciones se calcula cualquier ángulo desconocido. A veces conviene plantear una ecuación, como las del Tema 4: «son iguales» da una ecuación con =, y «suman 180°» o «suman 90°» da una suma.")}</p>
{ejemplo(t("Example 2: with a transversal. In the diagram, angle 1 measures 70°. What are the measures of angle 5 and angle 3?", "Ejemplo 2 · Con una transversal. En el diagrama, el ángulo 1 mide 70°. ¿Cuánto miden el ángulo 5 y el ángulo 3?"),
  [("1", t("Angle 5 corresponds to angle 1.", "El ángulo 5 es correspondiente con el 1."), t("So it measures 70°.", "Así que mide 70°.")),
   ("2", t("Angle 3 and angle 1 form a straight line.", "El ángulo 3 y el 1 forman una recta."), t("They are supplementary: 180° − 70° = 110°.", "Son suplementarios: 180° − 70° = 110°.")),
   ("✓", t("Answer.", "Respuesta."), t("Angle 5 = <strong>70°</strong> and angle 3 = <strong>110°</strong>.", "Ángulo 5 = <strong>70°</strong> y ángulo 3 = <strong>110°</strong>."))])}
{ejemplo(t("Example 3: with an equation. Two supplementary angles measure x and 2x. What is the value of x?", "Ejemplo 3 · Con una ecuación. Dos ángulos suplementarios miden x y 2x. ¿Cuánto vale x?"),
  [("1", t("They add up to 180°.", "Suman 180°."), "x + 2x = 180."),
   ("2", t("Combine and divide by 3.", "Se combinan y se divide entre 3."), "3x = 180, x = 60."),
   ("✓", t("Answer.", "Respuesta."), t("x = 60: the angles measure <strong>60°</strong> and <strong>120°</strong>.", "x = 60: los ángulos miden <strong>60°</strong> y <strong>120°</strong>."))])}
{practica("p4", t("Practice 4 — Complement", "Práctica 4 — Complemento"), t("The complement of a 40° angle measures…", "El complemento de un ángulo de 40° mide…"), [("a", "140°"), ("b", "50°"), ("c", "60°")])}
{practica("p5", t("Practice 5 — Supplement", "Práctica 5 — Suplemento"), t("The supplement of a 125° angle measures…", "El suplemento de un ángulo de 125° mide…"), [("a", "65°"), ("b", "235°"), ("c", "55°")])}
{enlace(n, t("calculate", "calcular"), t("finding unknown angles", "calcular ángulos desconocidos"), t("Find an angle from another one with the right relationship, or with an equation.", "Halle un ángulo a partir de otro con la relación correcta, o con una ecuación."))}'''

    s4 = f'''<p>{t("A basic property: the three interior angles of any triangle add up to 180°. If you know two angles, you can always find the third one.", "Una propiedad fundamental: los tres ángulos interiores de cualquier triángulo suman 180°. Conociendo dos ángulos, siempre se puede hallar el tercero.")}</p>
<p class="formula" style="text-align:center;font-size:1.2rem;font-weight:700;">{t("angle A + angle B + angle C = 180°", "ángulo A + ángulo B + ángulo C = 180°")}</p>
{ejemplo(t("Example 4: a triangle has angles of 50° and 60°. What is the measure of the third angle?", "Ejemplo 4: un triángulo tiene ángulos de 50° y 60°. ¿Cuánto mide el tercero?"),
  [("1", t("The three angles add up to 180°.", "Los tres suman 180°."), "50° + 60° + C = 180°."),
   ("2", t("Add the known angles.", "Se suman los conocidos."), t("110° + C = 180°, so C = 70°.", "110° + C = 180°, así que C = 70°.")),
   ("✓", t("Answer.", "Respuesta."), t("The third angle measures <strong>70°</strong>.", "El tercer ángulo mide <strong>70°</strong>."))])}
{caja("ojo", t("The right triangle", "El triángulo rectángulo"), t("<p>If a triangle has a 90° angle, the other two angles must add up to 90° (because the total is 180°). So in a right triangle, the two angles that are not right angles are always complementary.</p>", "<p>Si un triángulo tiene un ángulo de 90°, los otros dos deben sumar 90° (porque el total es 180°). Por eso, en un triángulo rectángulo, los dos ángulos que no son rectos son siempre complementarios.</p>"))}
{practica("p6", t("Practice 6 — The third angle", "Práctica 6 — El tercer ángulo"), t("A triangle has angles of 90° and 45°. The third angle measures…", "Un triángulo tiene ángulos de 90° y 45°. El tercero mide…"), [("a", "45°"), ("b", "90°"), ("c", "55°")])}
{enlace(n, t("triangle", "triangulo"), t("the angles of a triangle", "la suma de los ángulos de un triángulo"), t("Use the fact that the three angles add up to 180° to find the missing one.", "Use que los tres ángulos suman 180° para hallar el que falta."))}'''

    secciones = [("s-" + t("basics", "basicos"), t("Basic angle relationships", "Relaciones básicas entre ángulos"), s1),
                 ("s-transversal", t("Parallel lines cut by a transversal", "Paralelas cortadas por una transversal"), s2),
                 ("s-" + t("calculate", "calcular"), t("Finding unknown angles", "Calcular ángulos desconocidos"), s3),
                 ("s-" + t("triangle", "triangulo"), t("The angles of a triangle", "La suma de los ángulos de un triángulo"), s4)]

    lesson = {"next": t("Lesson 6.2", "Lección 6.2"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("Supplementary angles add up to 180°. Vertical angles are across from each other.", "Los suplementarios suman 180°. Los opuestos por el vértice están enfrentados."), "c": t("Complementary angles add up to 90°.", "Los complementarios suman 90°.")}, "right": t("Vertical angles are across from each other at the same vertex, and they are always equal.", "Los opuestos por el vértice están enfrentados en el mismo vértice y siempre son iguales."), "solution": t("They are equal.", "Son iguales.")},
      "p2": {"ok": "c", "hints": {"a": t("Look at angles 1 and 5: they are in the same position.", "Mire los ángulos 1 y 5: están en la misma posición."), "b": t("No pair of angles here adds up to 90°.", "Ninguna pareja de aquí suma 90°.")}, "right": t("Corresponding angles are in the same position at each intersection, so they are equal.", "Los correspondientes están en la misma posición en cada intersección, así que son iguales."), "solution": t("They are equal.", "Son iguales.")},
      "p3": {"ok": "a", "hints": {"b": t("Look at angles 3 and 5: one is acute and the other is obtuse.", "Mire los ángulos 3 y 5: uno es agudo y el otro obtuso."), "c": t("One is acute and the other is obtuse, so they cannot be equal.", "Uno es agudo y el otro obtuso, así que no pueden ser iguales.")}, "right": t("One is acute and the other is obtuse: together they make 180°.", "Uno es agudo y el otro obtuso: juntos hacen 180°."), "solution": t("They add up to 180°.", "Suman 180°.")},
      "p4": {"ok": "b", "hints": {"a": t("140° is the supplement (180° − 40°).", "140° es el suplemento (180° − 40°)."), "c": t("Subtract from 90°: 90° − 40°.", "Reste de 90°: 90° − 40°.")}, "right": "90° − 40° = 50°.", "solution": "90° − 40° = 50°."},
      "p5": {"ok": "c", "hints": {"a": t("Check the subtraction: 180 − 125.", "Revise la resta: 180 − 125."), "b": t("Supplementary angles add up to 180°; subtract, do not add.", "Los suplementarios suman 180°: se resta, no se suma.")}, "right": "180° − 125° = 55°.", "solution": "180° − 125° = 55°."},
      "p6": {"ok": "a", "hints": {"b": t("The three angles add up to 180°: 90° + 45° + ? = 180°.", "Los tres suman 180°: 90° + 45° + ? = 180°."), "c": t("Check the subtraction: 180 − 90 − 45.", "Revise la resta: 180 − 90 − 45.")}, "right": "180° − 90° − 45° = 45°.", "solution": "180° − 90° − 45° = 45°."}
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("145° is the supplement: subtract from 90°.", "145° es el suplemento: reste de 90°."), "c": t("Check the subtraction: 90 − 35.", "Revise la resta: 90 − 35."), "d": t("The complement completes 90°.", "El complemento completa 90°.")}, "solution": "90° − 35° = 55°."},
      "B": {"ok": "c", "hints": {"a": t("Check the subtraction: 180 − 110.", "Revise la resta: 180 − 110."), "b": t("Subtract from 180°; do not add.", "Se resta de 180°, no se suma."), "d": t("That is the same angle; the supplement completes 180°.", "Es el mismo ángulo; el suplemento completa 180°.")}, "solution": "180° − 110° = 70°."},
      "C": {"ok": "b", "hints": {"a": t("They are in the same position, so they have the same measure.", "Están en la misma posición, así que miden lo mismo."), "c": t("No rule here involves 90°.", "Aquí ninguna regla tiene que ver con 90°."), "d": t("They can measure any amount, but always the same.", "Pueden medir cualquier cantidad, pero siempre lo mismo.")}, "solution": t("Corresponding angles are equal.", "Los correspondientes son iguales.")},
      "D": {"ok": "a", "hints": {"b": t("Supplementary is the rule for same-side interior angles.", "Suman 180° los internos del mismo lado, no estos."), "c": t("No rule here involves 90°.", "Aquí ninguna regla tiene que ver con 90°."), "d": t("Look at angles 4 and 5 in the diagram: they have the same measure.", "Mire los ángulos 4 y 5 del diagrama: miden lo mismo.")}, "solution": t("Alternate interior angles are equal.", "Los alternos internos son iguales.")},
      "E": {"ok": "c", "hints": {"a": t("Same-side interior: one acute and one obtuse.", "Internos del mismo lado: uno agudo y uno obtuso."), "b": t("They form half a turn, not a full turn.", "Forman media vuelta, no una vuelta completa."), "d": t("One is acute and the other is obtuse.", "Uno es agudo y el otro obtuso.")}, "solution": t("They add up to 180°.", "Suman 180°.")},
      "F": {"ok": "b", "hints": {"a": t("110° would be the supplement. Corresponding angles are equal.", "110° sería el suplemento. Los correspondientes son iguales."), "c": t("Corresponding angles are equal.", "Los correspondientes son iguales."), "d": t("Do not divide: corresponding angles are equal.", "No se divide: los correspondientes son iguales.")}, "solution": t("It also measures 70°.", "También mide 70°.")},
      "G": {"ok": "c", "hints": {"a": t("Check the subtraction: 180 − 50 − 60.", "Revise la resta: 180 − 50 − 60."), "b": t("That is 50 + 60; subtract that sum from 180°.", "Eso es 50 + 60; reste esa suma de 180°."), "d": t("The three angles add up to 180°.", "Los tres ángulos suman 180°.")}, "solution": "180° − 50° − 60° = 70°."},
      "H": {"ok": "a", "hints": {"b": t("The three angles add up to 180°: 90° + 30° + ? = 180°.", "Los tres suman 180°: 90° + 30° + ? = 180°."), "c": t("A triangle can have only one right angle.", "Un triángulo solo puede tener un ángulo recto."), "d": t("The three angles add up to 180°, and 90° + 30° + 120° is more.", "Los tres suman 180°, y 90° + 30° + 120° es más.")}, "solution": "180° − 90° − 30° = 60°."}
     }}

    quiz = [
     ("A", t("If an angle measures 35°, its complement measures…", "Si un ángulo mide 35°, su complemento mide…"), [("a", "55°"), ("b", "145°"), ("c", "65°"), ("d", "35°")]),
     ("B", t("If an angle measures 110°, its supplement measures…", "Si un ángulo mide 110°, su suplemento mide…"), [("a", "80°"), ("b", "250°"), ("c", "70°"), ("d", "110°")]),
     ("C", t("Corresponding angles between parallel lines are…", "Los ángulos correspondientes entre paralelas son…"), [("a", t("supplementary", "suplementarios")), ("b", t("equal", "iguales")), ("c", t("complementary", "complementarios")), ("d", t("always right angles", "siempre rectos"))]),
     ("D", t("Alternate interior angles are…", "Los ángulos alternos internos son…"), [("a", t("equal", "iguales")), ("b", t("supplementary", "suplementarios")), ("c", t("complementary", "complementarios")), ("d", t("always different", "siempre distintos"))]),
     ("E", t("Same-side interior angles add up to…", "Los ángulos internos del mismo lado suman…"), [("a", "90°"), ("b", "360°"), ("c", "180°"), ("d", t("they are equal", "son iguales"))]),
     ("F", t("If one of two corresponding angles measures 70°, the other one measures…", "Si un ángulo correspondiente mide 70°, el otro correspondiente mide…"), [("a", "110°"), ("b", "70°"), ("c", "20°"), ("d", "35°")]),
     ("G", t("A triangle has angles of 50° and 60°. The third angle measures…", "Un triángulo tiene ángulos de 50° y 60°. El tercero mide…"), [("a", "80°"), ("b", "110°"), ("c", "70°"), ("d", "90°")]),
     ("H", t("A right triangle has a 90° angle and a 30° angle. The third angle measures…", "Un triángulo rectángulo tiene un ángulo de 90° y otro de 30°. El tercero mide…"), [("a", "60°"), ("b", "30°"), ("c", "90°"), ("d", "120°")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Recognize how angles are related, use parallel lines and a transversal to find unknown angles, and use the 180° of a triangle.", "Reconozca cómo se relacionan los ángulos, use paralelas y una transversal para hallar ángulos desconocidos y aplique los 180° de un triángulo."),
        ("📐", t("Angles, parallel lines, and triangles", "Ángulos, paralelas y triángulos")),
        [t("<strong>Identify</strong> complementary angles (they add up to 90°), supplementary angles (they add up to 180°), and vertical angles (they are equal).", "<strong>Identificar</strong> ángulos complementarios (suman 90°), suplementarios (suman 180°) y opuestos por el vértice (son iguales)."),
         t("<strong>Recognize</strong> the angles formed by two parallel lines cut by a transversal: corresponding, alternate interior, alternate exterior, and same-side interior.", "<strong>Reconocer</strong> los ángulos que forman dos paralelas cortadas por una transversal: correspondientes, alternos internos, alternos externos e internos del mismo lado."),
         t("<strong>Use</strong> these relationships to find unknown angles.", "<strong>Aplicar</strong> estas relaciones para calcular ángulos desconocidos."),
         t("<strong>Use</strong> the fact that the angles of a triangle add up to 180°.", "<strong>Usar</strong> la propiedad de que los ángulos de un triángulo suman 180°."),
         t("<strong>Write</strong> simple equations to find an unknown angle.", "<strong>Plantear</strong> ecuaciones sencillas para hallar un ángulo desconocido.")],
        secciones,
        (t(f"Solve three exercises on complementary and supplementary angles, four on finding angles with a transversal and parallel lines, and three on finding the third angle of a triangle. Then practice in {explora} until you can tell at a glance whether two angles are corresponding, alternate interior, or same-side interior.",
           f"Resuelva tres ejercicios de ángulos complementarios y suplementarios, cuatro de calcular ángulos en una transversal con paralelas y tres de calcular el tercer ángulo de un triángulo. Después practique en {explora} hasta que reconozca de un vistazo si dos ángulos son correspondientes, alternos internos o internos del mismo lado."),
         t("Look for parallel lines cut by a transversal around you: a ladder with its rungs, the lines of a parking lot, railroad tracks crossing a street, or a window with a diagonal brace. Sketch one, number its eight angles, and mark which ones are equal and which ones add up to 180°.",
           "Busque paralelas cortadas por una transversal a su alrededor: una escalera de mano con sus peldaños, las líneas de un estacionamiento, una vía de tren que cruza una calle o una ventana con un refuerzo en diagonal. Dibuje una, numere sus ocho ángulos y marque cuáles son iguales y cuáles suman 180°.")),
        quiz,
        t("Self-check checklist for angle relationships", "Lista de autoevaluación de las relaciones entre ángulos"),
        t("Self-check checklist: skills for angle relationships, parallel lines, and triangles", "Lista de autoevaluación: destrezas de relaciones entre ángulos, paralelas y triángulos"),
        [(t("Identifying the relationship", "Identificar la relación"), t("I correctly identify the type of relationship between the angles, even with a transversal.", "Identifico correctamente el tipo de relación entre los ángulos, incluso en la transversal."), t("I identify some relationships, with mistakes.", "Identifico algunas relaciones, con errores."), t("I cannot tell the types of angle relationships apart.", "No distingo los tipos de relación entre ángulos.")),
         (t("Using the property", "Aplicar la propiedad"), t("I use the right property (equal, supplementary, adds up to 180°) and write an equation when needed.", "Aplico la propiedad correcta (iguales, suplementarios, suma 180°) y planteo una ecuación cuando hace falta."), t("I use the property with occasional mistakes.", "Aplico la propiedad con errores ocasionales."), t("I do not use the right property.", "No aplico la propiedad correcta.")),
         (t("Finding the angle", "Calcular el ángulo"), t("I find the unknown angle without mistakes and check that the result makes sense.", "Calculo el ángulo desconocido sin errores y verifico que el resultado tenga sentido."), t("I find the angle with some mistakes.", "Calculo el ángulo con algún error."), t("I make arithmetic mistakes when I calculate.", "Cometo errores aritméticos al calcular."))],
        t("<p>This lesson studied how angles are related: complementary, supplementary, and vertical angles, and the angles formed by two parallel lines cut by a transversal (corresponding, alternate interior, and same-side interior). You also used the fact that the angles of a triangle add up to 180°, writing equations when needed.</p>\n<p>In <strong>Lesson 6.2 · The Pythagorean theorem: proof, applications, and converse</strong> you will study the relationship between the sides of a right triangle: a² + b² = c². With it you will find unknown sides and solve real problems about building and distance.</p>",
          "<p>En esta lección se estudiaron las relaciones entre ángulos: complementarios, suplementarios y opuestos por el vértice, y las que forman dos paralelas cortadas por una transversal (correspondientes, alternos internos e internos del mismo lado). También se usó que los ángulos de un triángulo suman 180°, planteando ecuaciones cuando fue necesario.</p>\n<p>En la <strong>Lección 6.2 · Teorema de Pitágoras: demostración, aplicaciones y converso</strong> se estudiará la relación entre los lados de un triángulo rectángulo: a² + b² = c². Con ella se calcularán lados desconocidos y se resolverán problemas reales de construcción y distancia.</p>"),
        ("6-2", ("", t("Lesson 6.2 · The Pythagorean theorem: proof, applications, and converse", "Lección 6.2 · Teorema de Pitágoras: demostración, aplicaciones y converso"))),
        [(t("complementary angles", "ángulos complementarios"), t("Two angles that add up to 90°.", "Dos ángulos que suman 90°.")),
         (t("supplementary angles", "ángulos suplementarios"), t("Two angles that add up to 180°.", "Dos ángulos que suman 180°.")),
         (t("vertical angles", "ángulos opuestos por el vértice"), t("The angles across from each other where two lines cross. They are equal.", "Los ángulos enfrentados donde se cortan dos rectas. Son iguales.")),
         (t("transversal", "transversal"), t("A line that cuts two or more lines.", "Una recta que corta a dos o más rectas.")),
         (t("corresponding angles", "ángulos correspondientes"), t("Angles in the same position at each intersection with the transversal.", "Ángulos en la misma posición en cada intersección con la transversal.")),
         (t("alternate interior angles", "ángulos alternos internos"), t("Angles between the parallel lines, on opposite sides of the transversal.", "Ángulos entre las paralelas, a lados opuestos de la transversal."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* MODULE 1 · Two lines that cross */
function pintaBasicos(){
  var a = +$("bs-a").value, c = [320, 150], s = "";
  $("bs-val").textContent = a + "°"; $("bs-a").setAttribute("aria-valuetext", a + T(" degrees", " grados"));
  s += '<svg class="geo-svg" viewBox="0 0 640 300" role="img" aria-label="' + T("Two lines that cross. Angles: ", "Dos rectas que se cortan. Ángulos: ") + a + "°, " + (180 - a) + "°, " + a + "° " + T("and", "y") + " " + (180 - a) + '°.">';
  s += arco(c[0], c[1], 46, 0, a, COL_SEL, "#e3f2fd") + arco(c[0], c[1], 46, 180, 180 + a, COL_IG, "#e8f5e9") + arco(c[0], c[1], 38, a, 180, COL_SUP, "#ffebee");
  s += lineaG(punto(c[0], c[1], 280, 180), punto(c[0], c[1], 280, 0), "#424242", 3) + lineaG(punto(c[0], c[1], 150, a + 180), punto(c[0], c[1], 150, a), "#424242", 3);
  s += texto(punto(c[0], c[1], 80, a / 2), a + "°", 18, COL_SEL) + texto(punto(c[0], c[1], 80, 180 + a / 2), a + "°", 18, COL_IG) +
       texto(punto(c[0], c[1], 74, (a + 180) / 2), (180 - a) + "°", 18, COL_SUP) + texto(punto(c[0], c[1], 74, (a + 540) / 2), (180 - a) + "°", 18, "#424242");
  $("bs-svg").innerHTML = s + "</svg>";
  $("bs-salida").innerHTML = '<div class="linea">' + T("The vertical angle (across from it) also measures ", "El ángulo opuesto por el vértice también mide ") + "<strong>" + a + "°</strong>.</div>" +
    '<div class="linea">' + T("Its neighbor measures ", "Su vecino mide ") + "180° − " + a + "° = <strong>" + (180 - a) + "°</strong>" + T(": they are supplementary, because together they make a straight line.", ": son suplementarios, porque juntos forman una recta.") + "</div>" +
    '<div class="linea">' + (a < 90 ? T("Its complement would be ", "Su complemento sería ") + "90° − " + a + "° = <strong>" + (90 - a) + "°</strong>." : T("Since it measures " + a + "°, it has no complement: it already reaches or passes 90°.", "Como mide " + a + "°, no tiene complemento: ya llega o pasa de 90°.")) + "</div>";
}
function genBasicos(){
  var tp = aleatorio(1, 4), a, pc = {};
  if (tp === 1){ a = aleatorio(5, 85); pc["g" + (180 - a)] = T("That is the supplement (they add up to 180°). The complement completes 90°.", "Ese es el suplemento (suman 180°). El complemento completa 90°."); pc["g" + a] = T("That is the same angle. The complement completes 90°.", "Es el mismo ángulo. El complemento completa 90°.");
    return {enun: T("What is the measure of the complement of a " + a + "° angle?", "¿Cuánto mide el complemento de un ángulo de " + a + "°?"), opciones: [opG(90 - a), opG(180 - a), opG(a), opG(360 - a)], correcta: "g" + (90 - a), porClave: pc,
      pista: T("Complementary angles add up to 90°.", "Los complementarios suman 90°."), bien: "90° − " + a + "° = " + (90 - a) + "°.", mal: T("Complementary angles add up to 90°: ", "Los complementarios suman 90°: ") + "90° − " + a + "° = " + (90 - a) + "°."}; }
  if (tp === 2){ a = aleatorio(5, 175); if (a === 90) a = 91; pc["g" + Math.abs(90 - a)] = T("Supplementary angles add up to 180°, not 90°.", "Los suplementarios suman 180°, no 90°."); pc["g" + a] = T("That is the same angle. The supplement completes 180°.", "Es el mismo ángulo. El suplemento completa 180°.");
    return {enun: T("What is the measure of the supplement of a " + a + "° angle?", "¿Cuánto mide el suplemento de un ángulo de " + a + "°?"), opciones: [opG(180 - a), opG(Math.abs(90 - a)), opG(360 - a), opG(a)], correcta: "g" + (180 - a), porClave: pc,
      pista: T("Supplementary angles add up to 180°.", "Los suplementarios suman 180°."), bien: "180° − " + a + "° = " + (180 - a) + "°.", mal: T("Supplementary angles add up to 180°: ", "Los suplementarios suman 180°: ") + "180° − " + a + "° = " + (180 - a) + "°."}; }
  if (tp === 3){ a = aleatorio(20, 160); if (a === 90) a = 70; pc["g" + (180 - a)] = T("That is its neighbor, which forms a straight line with it. The vertical angle is across from it.", "Ese es su vecino, que forma una recta con él. El opuesto por el vértice está enfrentado.");
    return {enun: T("Two lines cross, and one of the angles measures " + a + "°. What is the measure of its vertical angle (the one across from it)?", "Dos rectas se cortan y uno de los ángulos mide " + a + "°. ¿Cuánto mide el ángulo opuesto por el vértice?"), opciones: [opG(a), opG(180 - a), opG(Math.abs(90 - a) || 45), opG(2 * a)], correcta: "g" + a, porClave: pc,
      pista: T("Vertical angles are across from each other.", "Los opuestos por el vértice están enfrentados."), bien: T("Vertical angles are equal.", "Los opuestos por el vértice son iguales."), mal: T("Vertical angles are equal: it measures " + a + "°. Its neighbor, on the other hand, measures " + (180 - a) + "°.", "Los opuestos por el vértice son iguales: mide " + a + "°. Su vecino, en cambio, mide " + (180 - a) + "°.")}; }
  a = aleatorio(95, 170); pc["g" + (a - 90)] = T("A complement must be positive, and 90° − " + a + "° is negative.", "Un complemento tiene que ser positivo, y 90° − " + a + "° es negativo."); pc["g" + (180 - a)] = T("That is the supplement. Can anything complete " + a + "° up to 90°?", "Ese es el suplemento. ¿Algo puede completar " + a + "° hasta 90°?");
  return {enun: T("What is the measure of the complement of a " + a + "° angle?", "¿Cuánto mide el complemento de un ángulo de " + a + "°?"), opciones: [{html: T("It has no complement", "No tiene complemento"), clave: "no"}, opG(180 - a), opG(a - 90), opG(360 - a)], correcta: "no", porClave: pc,
    pista: T("Complementary angles add up to 90°. Is " + a + "° less than 90°?", "Los complementarios suman 90°. ¿" + a + "° es menor que 90°?"), bien: T("Complementary angles add up to 90°, and " + a + "° is already more than 90°.", "Dos ángulos complementarios suman 90°, y " + a + "° ya pasa de 90°."), mal: T("It has none: " + a + "° is already more than 90°, so no positive angle completes it to 90°.", "No tiene: " + a + "° ya es mayor que 90°, así que ningún ángulo positivo lo completa hasta 90°.")};
}

/* MODULE 2 · Transversal */
var TV = {sel: 1};
function pintaTV(){
  var alfa = +$("tv-a").value, colores = {}, igual = [], sup = [], i;
  $("tv-val").textContent = alfa + "°"; $("tv-a").setAttribute("aria-valuetext", alfa + T(" degrees", " grados"));
  for (i = 1; i <= 8; i++){
    if (i === TV.sel) colores[i] = COL_SEL;
    else if (medida(i, alfa) === medida(TV.sel, alfa)){ colores[i] = COL_IG; igual.push(i); }
    else { colores[i] = COL_SUP; sup.push(i); }
  }
  if (alfa === 90){ igual = igual.concat(sup); sup = []; for (i = 1; i <= 8; i++) if (i !== TV.sel) colores[i] = COL_IG; }
  $("tv-svg").innerHTML = dibujaTransversal(alfa, {colores: colores, voz: T("Transversal tilted " + alfa + " degrees. Chosen angle: " + TV.sel + ".", "Transversal inclinada " + alfa + " grados. Ángulo elegido: " + TV.sel + ".")});
  Array.prototype.forEach.call($("tv-botones").children, function(b){ b.setAttribute("aria-pressed", +b.getAttribute("data-i") === TV.sel ? "true" : "false"); });
  var m = medida(TV.sel, alfa), nombre = function(j){ var r = relacion(TV.sel, j); return j + (r ? " (" + REL[r] + ")" : ""); };
  var h = '<div class="linea">' + T("Angle " + TV.sel + " measures ", "El ángulo " + TV.sel + " mide ") + "<strong>" + m + "°</strong>.</div>";
  h += '<div class="linea">' + T("Same measure (" + m + "°): ", "Miden lo mismo (" + m + "°): ") + igual.map(nombre).join(", ") + ".</div>";
  if (sup.length) h += '<div class="linea">' + T("They measure " + (180 - m) + "° and add up to 180° with it: ", "Miden " + (180 - m) + "° y suman 180° con él: ") + sup.map(nombre).join(", ") + ".</div>";
  $("tv-salida").innerHTML = h;
}
var PAREJAS = [[1, 5], [2, 6], [3, 7], [4, 8], [4, 5], [3, 6], [1, 8], [2, 7], [3, 5], [4, 6], [1, 4], [2, 3], [5, 8], [6, 7], [1, 7], [2, 8]];
var CLAVES = ["corr", "aint", "aext", "sint", "vert", "sext"];
function pistaRel(i, j){
  if (interDe(i) === interDe(j)) return T("Both angles are at the same intersection. Are they across from each other?", "Los dos ángulos están en la misma intersección. ¿Están enfrentados?");
  if (posDe(i) === posDe(j)) return T("Look at where each angle sits at its own intersection.", "Mire dónde está cada ángulo en su propia intersección.");
  return T("Are both angles between the parallel lines (interior) or outside them (exterior)? Are they on the same side of the transversal?", "¿Los dos ángulos están entre las paralelas (internos) o fuera de ellas (externos)? ¿Están del mismo lado de la transversal?");
}
function genRelacion(){
  var par = baraja(elige(PAREJAS)), r = relacion(par[0], par[1]), alfa = elige([50, 55, 60, 65, 70, 115, 120, 125]), col = {};
  col[par[0]] = COL_SEL; col[par[1]] = COL_SEL;
  var otros = baraja(CLAVES.filter(function(k){ return k !== r; })).slice(0, 3);
  var o = [{html: REL_OP[r], clave: r}].concat(otros.map(function(k){ return {html: REL_OP[k], clave: k}; }));
  var igual = medida(par[0], alfa) === medida(par[1], alfa), exp = T("They are " + REL[r] + ": ", "Son " + REL[r] + ": ") + (igual ? T("they have the same measure.", "miden lo mismo.") : T("they add up to 180°.", "suman 180°."));
  return {enun: T("What is the relationship between angles " + par[0] + " and " + par[1] + "?", "¿Qué relación tienen los ángulos " + par[0] + " y " + par[1] + "?") + dibujaTransversal(alfa, {colores: col, voz: T("Transversal with angles " + par[0] + " and " + par[1] + " highlighted.", "Transversal con los ángulos " + par[0] + " y " + par[1] + " resaltados.")}),
    opciones: o, correcta: r, porClave: {}, pista: pistaRel(par[0], par[1]), bien: exp, mal: exp};
}

/* MODULE 3 · Finding angles */
function genDiagrama(){
  var alfa = aleatorio(35, 145); if (alfa === 90) alfa = 72;
  var i = aleatorio(1, 8), j; do { j = aleatorio(1, 8); } while (j === i);
  var mi = medida(i, alfa), mj = medida(j, alfa), r = relacion(i, j), et = {}, col = {};
  et[i] = mi + "°"; et[j] = "?"; col[i] = COL_SEL; col[j] = COL_SUP;
  var porque = mi === mj ? (r ? T("They are " + REL[r] + ", so they have the same measure", "Son " + REL[r] + ", así que miden lo mismo") : T("Both are the same kind (both acute or both obtuse), so they have the same measure", "Los dos son del mismo tipo (agudos u obtusos), así que miden lo mismo"))
                         : (r ? T("They are " + REL[r] + ": they add up to 180°", "Son " + REL[r] + ": suman 180°") : T("One is acute and the other is obtuse: they add up to 180°", "Uno es agudo y el otro obtuso: suman 180°"));
  return {enun: T("Angle " + i + " measures " + mi + "°. What is the measure of angle " + j + "?", "El ángulo " + i + " mide " + mi + "°. ¿Cuánto mide el ángulo " + j + "?") +
      dibujaTransversal(alfa, {colores: col, etiquetas: et, voz: T("Transversal. Angle " + i + " measures " + mi + " degrees; the question asks about angle " + j + ".", "Transversal. El ángulo " + i + " mide " + mi + " grados; se pregunta por el ángulo " + j + ".")}),
    solucion: porque + (mi === mj ? "." : ": 180° − " + mi + "° = " + mj + "°."),
    evalua: function(v){ return evaluaGrados(v, mj, [{v: 180 - mj, msg: mi === mj ? T("Those two angles have the same measure; you do not subtract from 180°.", "Esos dos ángulos miden lo mismo; no hay que restar de 180°.") : T("Those two angles do not have the same measure: they add up to 180°.", "Esos dos ángulos no miden lo mismo: suman 180°.")}]); }};
}
function ex(a, b){ return auto(b ? P(tm(a, "x"), tm(b)) : P(tm(a, "x"))); }
function genEcuacion(){
  var tp = aleatorio(1, 5), x, a, b, c, d, enun, ec, pistas = [];
  if (tp === 1){ do { a = aleatorio(1, 3); c = aleatorio(2, 5); } while (180 % (a + c) || a === c); x = 180 / (a + c);
    enun = T("Two supplementary angles measure ", "Dos ángulos suplementarios miden ") + ex(a, 0) + T(" and ", " y ") + ex(c, 0) + T(". What is the value of x?", ". ¿Cuánto vale x?"); ec = ex(a, 0) + " + " + ex(c, 0) + " = 180"; pistas = [{v: fr(90, a + c), msg: T("Supplementary angles add up to 180°, not 90°.", "Los suplementarios suman 180°, no 90°.")}]; }
  else if (tp === 2){ x = aleatorio(10, 25); a = 1; c = 2; b = aleatorio(1, 10); d = 90 - (a * x + b) - c * x;
    enun = T("Two complementary angles measure ", "Dos ángulos complementarios miden ") + ex(a, b) + T(" and ", " y ") + ex(c, d) + T(". What is the value of x?", ". ¿Cuánto vale x?"); ec = "(" + ex(a, b) + ") + (" + ex(c, d) + ") = 90"; }
  else if (tp === 3){ x = aleatorio(10, 40); a = aleatorio(2, 4); c = a + aleatorio(1, 3); b = aleatorio(5, 30); d = a * x + b - c * x;
    enun = T("Two vertical angles measure ", "Dos ángulos opuestos por el vértice miden ") + ex(a, b) + T(" and ", " y ") + ex(c, d) + T(". What is the value of x?", ". ¿Cuánto vale x?"); ec = ex(a, b) + " = " + ex(c, d); }
  else if (tp === 4){ x = aleatorio(15, 35); a = aleatorio(3, 5); c = aleatorio(1, 2); b = -aleatorio(5, 20); d = a * x + b - c * x;
    enun = T("Between two parallel lines, two corresponding angles measure ", "Entre dos paralelas, dos ángulos correspondientes miden ") + ex(a, b) + T(" and ", " y ") + ex(c, d) + T(". What is the value of x?", ". ¿Cuánto vale x?"); ec = ex(a, b) + " = " + ex(c, d); }
  else { x = aleatorio(20, 45); a = 1; c = 2; b = aleatorio(5, 20); d = 180 - (x + b) - 2 * x;
    enun = T("Between two parallel lines, two same-side interior angles measure ", "Entre dos paralelas, dos ángulos internos del mismo lado miden ") + ex(a, b) + T(" and ", " y ") + ex(c, d) + T(". What is the value of x?", ". ¿Cuánto vale x?"); ec = "(" + ex(a, b) + ") + (" + ex(c, d) + ") = 180"; }
  var regla = tp === 3 || tp === 4 ? T("The angles are equal, so set the two expressions equal.", "Los ángulos son iguales, así que se igualan las dos expresiones.") : T("The angles add up to " + (tp === 2 ? 90 : 180) + "°, so add the two expressions.", "Los ángulos suman " + (tp === 2 ? 90 : 180) + "°, así que se suman las dos expresiones.");
  return {enun: enun, solucion: regla + " " + ec + ", x = " + x + ".",
    evalua: function(v){ var r = evaluaNumero(v, fr(x), pistas); if (r.estado === "mal" && !pistas.some(function(p){ return r.msg === p.msg; })) r.msg = regla; return r; }};
}

/* MODULE 4 · Triangle */
function pintaTR(){
  var A = +$("tr-a").value, B = +$("tr-b").value;
  if (A + B > 165){ B = 165 - A; $("tr-b").value = B; }
  var C = 180 - A - B, lenAC = Math.sin(rad(B)) / Math.sin(rad(C)), Cp = [lenAC * Math.cos(rad(A)), lenAC * Math.sin(rad(A))];
  var xs = [0, 1, Cp[0], 1.35], minX = Math.min.apply(null, xs), maxX = Math.max.apply(null, xs), maxY = Math.max(Cp[1], 0.01);
  var esc = Math.min(520 / (maxX - minX), 230 / maxY), ox = 60 - minX * esc, oy = 285;
  function V(p){ return [ox + p[0] * esc, oy - p[1] * esc]; }
  var pa = V([0, 0]), pb = V([1, 0]), pc = V(Cp), pe = V([1.35, 0]);
  $("tr-av").textContent = A + "°"; $("tr-bv").textContent = B + "°";
  $("tr-a").setAttribute("aria-valuetext", A + T(" degrees", " grados")); $("tr-b").setAttribute("aria-valuetext", B + T(" degrees", " grados"));
  var s = '<svg class="geo-svg" viewBox="0 0 640 320" role="img" aria-label="' + T("Triangle with angle A of " + A + ", B of " + B + ", and C of " + C + " degrees. Exterior angle at B: " + (A + C) + " degrees.", "Triángulo con ángulos A de " + A + ", B de " + B + " y C de " + C + " grados. Ángulo exterior en B: " + (A + C) + " grados.") + '">';
  s += '<polygon points="' + [pa, pb, pc].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#efebe9" stroke="#4e342e" stroke-width="3"/>';
  s += lineaG(pb, pe, "#9e9e9e", 2, ' stroke-dasharray="6 5"');
  var gBC = 180 - B, gCA = 180 + A, gCB = 360 - B;
  s += arco(pa[0], pa[1], 34, 0, A, COL_SEL, "#e3f2fd") + arco(pb[0], pb[1], 34, gBC, 180, COL_IG, "#e8f5e9") + arco(pc[0], pc[1], 30, gCA, gCB, COL_SUP, "#ffebee") + arco(pb[0], pb[1], 26, 0, gBC, "#6a1b9a", "#f3e5f5");
  s += texto(punto(pa[0], pa[1], 62, A / 2), A + "°", 20, COL_SEL) + texto(punto(pb[0], pb[1], 62, (gBC + 180) / 2), B + "°", 20, COL_IG);
  s += texto(punto(pc[0], pc[1], 56, (gCB + gCA) / 2), C + "°", 20, COL_SUP) + texto(punto(pb[0], pb[1], 66, gBC / 2), (A + C) + "°", 20, "#6a1b9a");
  s += texto([pa[0] - 16, pa[1] + 4], "A", 20, "#3e2723") + texto([pb[0] + 2, pb[1] + 22], "B", 20, "#3e2723") + texto([pc[0], pc[1] - 18], "C", 20, "#3e2723");
  $("tr-svg").innerHTML = s + "</svg>";
  $("tr-salida").innerHTML = '<div class="linea">' + A + "° + " + B + "° + " + C + "° = <strong>180°</strong>" + T(", whatever the shape.", ", sea cual sea la forma.") + "</div>" +
    '<div class="linea">' + T("The exterior angle at B (in purple) measures ", "El ángulo exterior en B (en morado) mide ") + "180° − " + B + "° = " + (A + C) + "°" + T(", which is exactly A + C = ", ", que es justo A + C = ") + A + "° + " + C + "°.</div>" +
    (A === 90 || B === 90 || C === 90 ? '<div class="linea">' + T("It is a right triangle: the other two angles add up to 90°.", "Es un triángulo rectángulo: los otros dos ángulos suman 90°.") + "</div>" : "");
}
function genTriangulo(){
  var tp = aleatorio(1, 4), A, B, C, enun, sol, res, pistas = [];
  if (tp === 1){ A = aleatorio(20, 100); B = aleatorio(20, 160 - A); res = 180 - A - B; enun = T("A triangle has angles of " + A + "° and " + B + "°. What is the measure of the third angle?", "Un triángulo tiene ángulos de " + A + "° y " + B + "°. ¿Cuánto mide el tercero?"); sol = "180° − " + A + "° − " + B + "° = " + res + "°.";
    pistas = [{v: A + B, msg: T("That is the sum of the two angles. Subtract it from 180°.", "Esa es la suma de los dos ángulos. Réstela de 180°.")}]; }
  else if (tp === 2){ A = aleatorio(15, 75); res = 90 - A; enun = T("In a right triangle, one of the acute angles measures " + A + "°. What is the measure of the other acute angle?", "En un triángulo rectángulo, uno de los ángulos agudos mide " + A + "°. ¿Cuánto mide el otro ángulo agudo?"); sol = T("The two acute angles add up to 90°: ", "Los dos agudos suman 90°: ") + "90° − " + A + "° = " + res + "°.";
    pistas = [{v: 180 - A, msg: T("Remember the right angle: 180° − 90° − " + A + "°.", "No olvide el ángulo recto: 180° − 90° − " + A + "°.")}]; }
  else if (tp === 3){ B = aleatorio(20, 80); res = 180 - 2 * B; enun = T("An isosceles triangle has two equal angles of " + B + "° each. What is the measure of the third angle?", "Un triángulo isósceles tiene dos ángulos iguales de " + B + "° cada uno. ¿Cuánto mide el tercer ángulo?"); sol = "180° − 2 · " + B + "° = " + res + "°.";
    pistas = [{v: 180 - B, msg: T("There are two angles of " + B + "°: subtract both.", "Hay dos ángulos de " + B + "°: reste los dos.")}]; }
  else { A = aleatorio(20, 80); C = aleatorio(20, 80); res = A + C; enun = T("Two interior angles of a triangle measure " + A + "° and " + C + "°. What is the measure of the exterior angle at the third vertex?", "Dos ángulos interiores de un triángulo miden " + A + "° y " + C + "°. ¿Cuánto mide el ángulo exterior que está junto al tercer vértice?"); sol = T("The exterior angle is the sum of the two interior angles that are not next to it: ", "El exterior es la suma de los dos interiores lejanos: ") + A + "° + " + C + "° = " + res + "°.";
    pistas = [{v: 180 - A - C, msg: T("That is the interior angle at the third vertex. The exterior angle forms a straight line with it.", "Ese es el ángulo interior del tercer vértice. El exterior forma una recta con él.")}]; }
  return {enun: enun, solucion: sol, evalua: function(v){ var r = evaluaGrados(v, res, pistas); if (r.estado === "mal" && !pistas.some(function(p){ return r.msg === p.msg; })) r.msg = T("The three angles of a triangle add up to 180°.", "Los tres ángulos de un triángulo suman 180°."); return r; }};
}

/* Start */
$("bs-a").addEventListener("input", pintaBasicos); pintaBasicos();
OMR("p1", genBasicos);
for (var ib = 1; ib <= 8; ib++){ (function(i){
  var b = document.createElement("button"); b.type = "button"; b.className = "eleccion"; b.textContent = T("Angle ", "Ángulo ") + i; b.setAttribute("data-i", i);
  b.addEventListener("click", function(){ TV.sel = i; pintaTV(); }); $("tv-botones").appendChild(b);
})(ib); }
$("tv-a").addEventListener("input", pintaTV); pintaTV();
OMR("p2", genRelacion);
creaPracticaLibre("p3", genDiagrama);
creaPracticaLibre("p4", genEcuacion);
$("tr-a").addEventListener("input", pintaTR); $("tr-b").addEventListener("input", pintaTR); pintaTR();
creaPracticaLibre("p5", genTriangulo);
'''

def practica_pagina():
    n = N
    explora = t('<a href="explore-angles.html">Explore: angles, parallel lines, and a transversal</a>', '<a href="explorar-angulos.html">Explorar: ángulos, paralelas y una transversal</a>')
    nota_g = t("Type only the number, without the ° symbol.", "Escriba solo el número, sin el símbolo °.")
    def grados(pid, tit, et=None):
        return B.libre(pid, tit, et or t("Measure in degrees", "Medida en grados"), nota=False).replace('<div class="fila-btn">', f'<p class="nota">{nota_g}</p>\n        <div class="fila-btn">', 1)
    mods = [
     (t("basics", "basicos"), t("Basic angle relationships", "Relaciones básicas entre ángulos"),
      f'''      <table class="reglas"><caption>{t("Basic angle relationships", "Relaciones básicas entre ángulos")}</caption>
        <thead><tr><th scope="col">{t("Relationship", "Relación")}</th><th scope="col">{t("Property", "Propiedad")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead>
        <tbody><tr><td>{t("Complementary", "Complementarios")}</td><td>{t("they add up to 90°", "suman 90°")}</td><td>{t("30° and 60°", "30° y 60°")}</td></tr>
        <tr><td>{t("Supplementary", "Suplementarios")}</td><td>{t("they add up to 180°", "suman 180°")}</td><td>{t("110° and 70°", "110° y 70°")}</td></tr>
        <tr><td>{t("Vertical angles", "Opuestos por el vértice")}</td><td>{t("they are equal", "son iguales")}</td><td>{t("50° and 50°", "50° y 50°")}</td></tr></tbody></table>
      <h3>{t("Two lines that cross", "Dos rectas que se cortan")}</h3>
      <p>{t("Move the slider. Vertical angles are always equal, and two neighboring angles always add up to 180°.", "Mueva el deslizador. Los ángulos opuestos por el vértice son siempre iguales, y dos ángulos vecinos siempre suman 180°.")}</p>
      <div class="panel"><div class="campo"><label for="bs-a">{t("Marked angle:", "Ángulo marcado:")} <span id="bs-val"></span></label><input type="range" id="bs-a" min="10" max="170" step="5" value="50"></div></div>
      <div id="bs-svg"></div>
{n3.salida("bs-salida")}
      <div class="caja-tip">{t("“Complementary” and “corner” (90°) both start with <strong>c</strong>; “supplementary” and “straight” (180°) both start with <strong>s</strong>. An angle of 90° or more has no complement.", "Para recordar cuál es cuál: «complementarios» y «esquina» (90°) van juntos; «suplementarios» y «recta» (180°) también. Un ángulo de 90° o más no tiene complemento.")}</div>
{B.om("p1", t("Practice: complement, supplement, and vertical angle", "Practique: complemento, suplemento y opuesto por el vértice"))}'''),
     ("transversal", t("Parallel lines cut by a transversal", "Paralelas cortadas por una transversal"),
      f'''      <p>{t("When a transversal cuts two parallel lines, eight angles are formed. There are only two measures: the acute angles are all equal, the obtuse angles are all equal, and an acute angle plus an obtuse angle add up to 180°.", "Cuando una recta transversal corta dos paralelas se forman ocho ángulos. Solo hay dos medidas: los ángulos agudos son todos iguales entre sí, los obtusos también, y un agudo más un obtuso suman 180°.")}</p>
      <table class="reglas"><caption>{t("Angle pairs between parallel lines", "Parejas de ángulos entre paralelas")}</caption>
        <thead><tr><th scope="col">{t("Pair", "Pareja")}</th><th scope="col">{t("Example in the diagram", "Ejemplo en el diagrama")}</th><th scope="col">{t("Property", "Propiedad")}</th></tr></thead>
        <tbody><tr><td>{t("Corresponding", "Correspondientes")}</td><td>{t("1 and 5", "1 y 5")}</td><td>{t("equal", "son iguales")}</td></tr>
        <tr><td>{t("Alternate interior", "Alternos internos")}</td><td>{t("4 and 5", "4 y 5")}</td><td>{t("equal", "son iguales")}</td></tr>
        <tr><td>{t("Alternate exterior", "Alternos externos")}</td><td>{t("1 and 8", "1 y 8")}</td><td>{t("equal", "son iguales")}</td></tr>
        <tr><td>{t("Same-side interior", "Internos del mismo lado")}</td><td>{t("3 and 5", "3 y 5")}</td><td>{t("add up to 180°", "suman 180°")}</td></tr>
        <tr><td>{t("Vertical angles", "Opuestos por el vértice")}</td><td>{t("1 and 4", "1 y 4")}</td><td>{t("equal", "son iguales")}</td></tr></tbody></table>
      <h3>{t("Explore the eight angles", "Explore los ocho ángulos")}</h3>
      <p>{t("Tilt the transversal and choose an angle: the angles with the same measure turn green, and the ones that complete it to 180° turn red.", "Incline la transversal y elija un ángulo: se marcan en verde los que miden lo mismo y en rojo los que lo completan hasta 180°.")}</p>
      <div class="panel"><div class="campo"><label for="tv-a">{t("Tilt of the transversal:", "Inclinación de la transversal:")} <span id="tv-val"></span></label><input type="range" id="tv-a" min="35" max="145" step="5" value="60"></div>
        <div class="elecciones" id="tv-botones" role="group" aria-label="{t("Choose an angle", "Elija un ángulo")}"></div></div>
      <div class="leyenda-geo" aria-hidden="true"><span><i style="background:#0d47a1"></i>{t("chosen", "elegido")}</span><span><i style="background:#1b5e20"></i>{t("same measure", "mide lo mismo")}</span><span><i style="background:#b71c1c"></i>{t("add up to 180°", "suman 180°")}</span></div>
      <div id="tv-svg"></div>
{n3.salida("tv-salida")}
      <div class="caja-tip">{t(f"More in {explora}: angles you can choose right on the drawing, and a quiz with hints.", f"Más en {explora}: ángulos que se eligen sobre el mismo dibujo y un cuestionario con pistas.")}</div>
{B.om("p2", t("Practice: what is the relationship?", "Practique: ¿qué relación tienen?"))}'''),
     (t("calculate", "calcular"), t("Finding unknown angles", "Calcular ángulos desconocidos"),
      f'''      <p>{t("If you know a relationship, you can find any angle. If the angles are given with expressions like 2x or 3x + 10, write an equation like the ones in Topic 4: “they are equal” gives an equation with =, and “they add up to 180°” or “to 90°” gives a sum.", "Conociendo una relación, se calcula cualquier ángulo. Si los ángulos vienen con expresiones como 2x o 3x + 10, se plantea una ecuación como las del Tema 4: «son iguales» da una ecuación con =, y «suman 180°» o «suman 90°» da una suma.")}</p>
{grados("p3", t("Practice: with the diagram", "Practique: con el diagrama"))}
{B.libre("p4", t("Practice: with an equation", "Practique: con una ecuación"), t("Value of x", "Valor de x"), nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("Type only the number.", "Escriba solo el número.") + '</p>\n        <div class="fila-btn">', 1)}'''),
     (t("triangle", "triangulo"), t("The angles of a triangle", "La suma de los ángulos de un triángulo"),
      f'''      <p>{t("The three interior angles of any triangle add up to 180°. Also, an exterior angle equals the sum of the two interior angles that are not next to it.", "Los tres ángulos interiores de cualquier triángulo suman 180°. Además, un ángulo exterior es igual a la suma de los dos interiores que no están junto a él.")}</p>
{n3.formula("A + B + C = 180°")}
      <h3>{t("Change the shape of the triangle", "Deforme el triángulo")}</h3>
      <div class="panel"><div class="campos">
        <div class="campo" style="flex:1;min-width:220px;"><label for="tr-a">{t("Angle A:", "Ángulo A:")} <span id="tr-av"></span></label><input type="range" id="tr-a" min="15" max="120" step="5" value="60"></div>
        <div class="campo" style="flex:1;min-width:220px;"><label for="tr-b">{t("Angle B:", "Ángulo B:")} <span id="tr-bv"></span></label><input type="range" id="tr-b" min="15" max="120" step="5" value="50"></div></div></div>
      <div id="tr-svg"></div>
{n3.salida("tr-salida")}
      <div class="caja-tip">{t("The right triangle: if one angle measures 90°, the other two add up to 90°. They are complementary.", "El triángulo rectángulo: si un ángulo mide 90°, los otros dos suman 90°: son complementarios.")}</div>
{grados("p5", t("Practice: find the missing angle", "Practique: halle el ángulo que falta"))}''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO_GEO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Ángulos: relaciones y líneas paralelas cortadas por una transversal")
