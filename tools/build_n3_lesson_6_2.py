"""Level 3 · Lesson 6.2 · The Pythagorean theorem: proof, applications, and converse — builds the lesson and its practice page in English and in Spanish.
Sources: clase_mate3/leccion_6-2.html and algebra/n3-l6-2.html (GEDparaHispanos). The explore page comes from build_n3_explora_6.py.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla, calc
import n3
from build_n3_explora_6 import ESTILO as ESTILO_GEO

B.NIVEL = 3
N = "6-2"
TEMA = ("Geometry: angles, the Pythagorean theorem, and similarity", "Geometría: ángulos, teorema de Pitágoras y semejanza")
TIT = ("The Pythagorean theorem: proof, applications, and converse", "Teorema de Pitágoras: demostración, aplicaciones y converso")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js")

def figura_triangulo():
    s = ('<polygon points="120,250 420,250 120,60" fill="#efebe9" stroke="#4e342e" stroke-width="3"/>'
         '<path d="M120 232 H138 V250" fill="none" stroke="#4e342e" stroke-width="2"/>'
         '<text x="100" y="160" font-size="24" font-weight="700" fill="#0d47a1" text-anchor="middle">a</text>'
         '<text x="270" y="282" font-size="24" font-weight="700" fill="#1b5e20" text-anchor="middle">b</text>'
         '<text x="290" y="140" font-size="24" font-weight="700" fill="#b71c1c" text-anchor="middle">c</text>'
         f'<text x="300" y="166" font-size="15" fill="#b71c1c" text-anchor="middle">{t("hypotenuse", "hipotenusa")}</text>')
    return B.svg("0 0 540 300", t("A right triangle. The legs a and b form the right angle, marked with a small square. The hypotenuse c is across from the right angle.",
                                  "Un triángulo rectángulo. Los catetos a y b forman el ángulo recto, marcado con un cuadradito. La hipotenusa c está enfrente del ángulo recto."), s, 460)

def leccion():
    n = N
    explora = t('<a href="explore-pythagoras.html">Explore: the Pythagorean theorem in real life</a>', '<a href="explorar-pitagoras.html">Explorar: el teorema de Pitágoras en la vida real</a>')
    s1 = f'''<p>{t("In Lesson 6.1 you worked with the angles of triangles, including the right triangle (the one with a 90° angle). This lesson studies the relationship between its sides: the Pythagorean theorem. To solve for the unknown side you will use exactly the algebra of Topics 4 and 5, and you will take a square root as in Topic 3.", "En la Lección 6.1 se trabajó con los ángulos de los triángulos, incluyendo el triángulo rectángulo (el que tiene un ángulo de 90°). Esta lección estudia la relación entre sus lados: el teorema de Pitágoras. Para despejar el lado desconocido se usará exactamente lo aprendido en el álgebra de los Temas 4 y 5, y se sacará la raíz cuadrada como en el Tema 3.")}</p>
<p>{t("In a right triangle, the two sides that form the 90° angle are called the <strong>legs</strong> (a and b). The side across from the right angle, which is the longest one, is called the <strong>hypotenuse</strong> (c). The Pythagorean theorem relates the three:", "En un triángulo rectángulo, los dos lados que forman el ángulo de 90° se llaman <strong>catetos</strong> (a y b). El lado opuesto al ángulo recto, que es el más largo, se llama <strong>hipotenusa</strong> (c). El teorema de Pitágoras relaciona los tres:")}</p>
<p class="formula" style="text-align:center;font-size:1.4rem;font-weight:700;">a² + b² = c²</p>
{figura_triangulo()}
{caja("ojo", t("The hypotenuse is always c", "La hipotenusa siempre es c"), t("<p>It is the longest side, and it is across from the right angle. Finding it correctly is the first step, because in the formula a² + b² = c², c always takes the place of the hypotenuse.</p>", "<p>Es el lado más largo y está enfrente del ángulo recto. Identificarla bien es el primer paso, porque en la fórmula a² + b² = c², la c siempre ocupa el lugar de la hipotenusa.</p>"))}
{enlace(n, t("theorem", "teorema"), t("the right triangle and the theorem", "el triángulo rectángulo y el teorema"), t("See the proof with squares, and find the hypotenuse and the legs before you write a² + b² = c².", "Vea la demostración con cuadrados e identifique la hipotenusa y los catetos antes de plantear a² + b² = c²."))}'''

    s2 = f'''<p>{t("When you know the two legs, substitute them into the formula and take the square root to find the hypotenuse.", "Cuando se conocen los dos catetos, se sustituyen en la fórmula y se saca la raíz cuadrada para hallar la hipotenusa.")}</p>
{ejemplo(t("Example 1: the 3-4-5 triangle. The legs measure 3 and 4. What is the length of the hypotenuse?", "Ejemplo 1 · El triángulo 3-4-5. Los catetos miden 3 y 4. ¿Cuánto mide la hipotenusa?"),
  [("1", t("Substitute.", "Se sustituye."), t("3² + 4² = c², that is, 9 + 16 = c².", "3² + 4² = c², es decir 9 + 16 = c².")),
   ("2", t("Add.", "Se suma."), "25 = c²."),
   ("3", t("Take the square root.", "Se saca la raíz."), "c = √25 = 5."),
   ("✓", t("Answer.", "Respuesta."), t("The hypotenuse measures <strong>5</strong>.", "La hipotenusa mide <strong>5</strong>."))])}
{ejemplo(t("Example 2: the legs measure 6 and 8. What is the length of the hypotenuse?", "Ejemplo 2: los catetos miden 6 y 8. ¿Cuánto mide la hipotenusa?"),
  [("1", t("Substitute.", "Se sustituye."), "6² + 8² = 36 + 64 = 100 = c²."),
   ("2", t("Take the square root.", "Se saca la raíz."), "c = √100 = 10."),
   ("✓", t("Answer.", "Respuesta."), t("The hypotenuse measures <strong>10</strong>.", "La hipotenusa mide <strong>10</strong>."))])}
{calc(t("With the calculator", "Con la calculadora"), t("<p>When the sum of the squares is not a perfect square, use the calculator: for legs 5 and 7, c² = 25 + 49 = 74, and √74 ≈ 8.6. Round to the tenth unless the problem says otherwise.</p>", "<p>Cuando la suma de los cuadrados no es un cuadrado perfecto, use la calculadora: con catetos 5 y 7, c² = 25 + 49 = 74, y √74 ≈ 8.6. Redondee a la décima, salvo que el problema diga otra cosa.</p>"))}
{practica("p1", t("Practice 1 — Legs 8 and 15", "Práctica 1 — Catetos 8 y 15"), t("The legs measure 8 and 15. The hypotenuse measures…", "Los catetos miden 8 y 15. La hipotenusa mide…"), [("a", "17"), ("b", "23"), ("c", "64")])}
{practica("p2", t("Practice 2 — Legs 9 and 12", "Práctica 2 — Catetos 9 y 12"), t("The legs measure 9 and 12. The hypotenuse measures…", "Los catetos miden 9 y 12. La hipotenusa mide…"), [("a", "21"), ("b", "15"), ("c", "225")])}
{enlace(n, t("hypotenuse", "hipotenusa"), t("finding the hypotenuse", "calcular la hipotenusa"), t("Add the squares of the legs and take the square root.", "Sume los cuadrados de los catetos y saque la raíz."))}'''

    s3 = f'''<p>{t("If you know the hypotenuse and one leg, solve for the other leg: subtract the square of the known leg and take the square root.", "Si se conocen la hipotenusa y un cateto, se despeja el otro cateto: se resta el cuadrado del cateto conocido y se saca la raíz.")}</p>
{ejemplo(t("Example 3: the hypotenuse measures 13 and one leg measures 5. What is the length of the other leg?", "Ejemplo 3: la hipotenusa mide 13 y un cateto mide 5. ¿Cuánto mide el otro cateto?"),
  [("1", t("Write the equation.", "Se plantea."), t("5² + b² = 13², that is, 25 + b² = 169.", "5² + b² = 13², es decir 25 + b² = 169.")),
   ("2", t("Solve for b².", "Se despeja."), "b² = 169 − 25 = 144."),
   ("3", t("Take the square root.", "Se saca la raíz."), "b = √144 = 12."),
   ("✓", t("Answer.", "Respuesta."), t("The other leg measures <strong>12</strong>.", "El otro cateto mide <strong>12</strong>."))])}
{caja("ojo", t("For a leg, subtract", "Para un cateto, se resta"), t("<p>When you look for a leg, the square of the hypotenuse is alone on one side, and you subtract the square of the known leg from it. A common mistake is to add instead of subtract. Check your answer: a leg is always shorter than the hypotenuse.</p>", "<p>Al buscar un cateto, el cuadrado de la hipotenusa va solo de un lado y se le resta el cuadrado del cateto conocido. Un error común es sumar en lugar de restar. Compruebe su respuesta: un cateto siempre es más corto que la hipotenusa.</p>"))}
{practica("p3", t("Practice 3 — The missing leg", "Práctica 3 — El cateto que falta"), t("The hypotenuse measures 13 and one leg measures 12. The other leg measures…", "La hipotenusa mide 13 y un cateto mide 12. El otro cateto mide…"), [("a", "7"), ("b", "5"), ("c", "25")])}
{caja("tip", t("Real-life problems", "Problemas de la vida real"), t(f"<p>Ladders, ramps, roofs, guy wires, and TV screens all hide a right triangle. Practice with them in {explora}, where you can show the triangle on the drawing and see the solution step by step.</p>", f"<p>Escaleras, rampas, techos, cables tensores y pantallas de televisor esconden un triángulo rectángulo. Practique con ellos en {explora}, donde puede ver el triángulo sobre el dibujo y la solución paso a paso.</p>"))}
{enlace(n, t("leg", "cateto"), t("finding a leg", "calcular un cateto"), t("Subtract the squares and take the square root to find the missing leg.", "Reste los cuadrados y saque la raíz para hallar el cateto que falta."))}'''

    s4 = f'''<p>{t("Some right triangles have sides that are whole numbers. Recognizing them saves calculations on the test.", "Algunos triángulos rectángulos tienen lados que son números enteros. Reconocerlos ahorra cálculos en el examen.")}</p>
{tabla(t("Common Pythagorean triples", "Triples pitagóricos comunes"), t("Common Pythagorean triples (whole legs and hypotenuse)", "Triples pitagóricos comunes (catetos e hipotenusa enteros)"), [t("Leg a", "Cateto a"), t("Leg b", "Cateto b"), t("Hypotenuse c", "Hipotenusa c")],
  [["3", "4", "5"], ["5", "12", "13"], ["8", "15", "17"], ["7", "24", "25"]])}
{caja("tip", t("Multiples work too", "Los múltiplos también funcionan"), t("<p>If 3-4-5 is a triple, so are 6-8-10 (everything times 2) and 9-12-15 (everything times 3). Recognizing a multiple of 3-4-5 lets you find the answer almost right away.</p>", "<p>Si 3-4-5 es un triple, también lo son 6-8-10 (todo por 2) o 9-12-15 (todo por 3). Reconocer un múltiplo del 3-4-5 permite hallar la respuesta casi de inmediato.</p>"))}
{enlace(n, t("triples", "triples"), t("Pythagorean triples", "triples pitagóricos"), t("Recognize the most common triples and their multiples.", "Reconozca los triples más comunes y sus múltiplos."))}'''

    s5 = f'''<p>{t("The <strong>converse</strong> goes the other way: if the three sides of a triangle make a² + b² = c² true, then the triangle is a right triangle. It is a way to check whether a corner is a right angle.", "El <strong>converso</strong> permite ir en sentido contrario: si los tres lados de un triángulo cumplen a² + b² = c², entonces el triángulo es rectángulo. Sirve para verificar si una esquina forma un ángulo recto.")}</p>
{ejemplo(t("Example 4: checking with the converse. Is a triangle with sides 30, 40, and 50 a right triangle?", "Ejemplo 4 · Verificar con el converso. ¿Es rectángulo un triángulo con lados 30, 40 y 50?"),
  [("1", t("The longest side (50) would be the hypotenuse.", "El lado más largo (50) sería la hipotenusa."), t("Check: 30² + 40² = 900 + 1,600 = 2,500.", "Se comprueba: 30² + 40² = 900 + 1,600 = 2,500.")),
   ("2", t("Compare.", "Se compara."), t("50² = 2,500. They match, so a² + b² = c² is true.", "Y 50² = 2,500. Como coinciden, se cumple a² + b² = c².")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>Yes</strong>, the triangle is a right triangle.", "<strong>Sí</strong>, el triángulo es rectángulo."))])}
{caja("tip", t("On the job", "En la obra"), t("<p>Carpenters mark 3 feet on one wall and 4 feet on the other. If the diagonal between the marks measures 5 feet, the corner is square. That is the converse of the theorem.</p>", "<p>Los carpinteros marcan 3 pies en una pared y 4 en la otra. Si la diagonal entre las marcas mide 5 pies, la esquina está a escuadra. Es el converso del teorema.</p>"))}
{practica("p4", t("Practice 4 — 5, 12, and 13", "Práctica 4 — 5, 12 y 13"), t("Is a triangle with sides 5, 12, and 13 a right triangle?", "¿Es rectángulo un triángulo de lados 5, 12 y 13?"), [("a", t("Yes, because 25 + 144 = 169", "Sí, porque 25 + 144 = 169")), ("b", "No"), ("c", t("Only if it is isosceles", "Solo si es isósceles"))])}
{practica("p5", t("Practice 5 — 4, 5, and 6", "Práctica 5 — 4, 5 y 6"), t("Is a triangle with sides 4, 5, and 6 a right triangle?", "¿Es rectángulo un triángulo de lados 4, 5 y 6?"), [("a", t("Yes", "Sí")), ("b", t("Always", "Siempre lo es")), ("c", t("No, because 16 + 25 ≠ 36", "No, porque 16 + 25 ≠ 36"))])}
{enlace(n, t("converse", "converso"), t("the converse of the theorem", "el converso del teorema"), t("Decide whether a triangle is a right triangle from its sides.", "Decida si un triángulo es rectángulo a partir de sus lados."))}'''

    secciones = [("s-" + t("theorem", "teorema"), t("The right triangle and the theorem", "El triángulo rectángulo y el teorema"), s1),
                 ("s-" + t("hypotenuse", "hipotenusa"), t("Finding the hypotenuse", "Calcular la hipotenusa"), s2),
                 ("s-" + t("leg", "cateto"), t("Finding a leg", "Calcular un cateto"), s3),
                 ("s-triples", t("Pythagorean triples", "Triples pitagóricos"), s4),
                 ("s-" + t("converse", "converso"), t("The converse of the theorem", "El converso del teorema"), s5)]

    lesson = {"next": t("Lesson 6.3", "Lección 6.3"), "review": t("sections 2, 3, and 5", "las secciones 2, 3 y 5"),
     "practice": {
      "p1": {"ok": "a", "hints": {"b": t("You added the legs. Add their squares: 64 + 225.", "Sumó los catetos. Hay que sumar sus cuadrados: 64 + 225."), "c": t("64 is 8². Add 8² + 15² and take the square root.", "64 es 8². Sume 8² + 15² y saque la raíz.")}, "right": "8² + 15² = 64 + 225 = 289, √289 = 17.", "solution": "8² + 15² = 289, c = √289 = 17."},
      "p2": {"ok": "b", "hints": {"a": t("You added the legs. Add their squares: 81 + 144.", "Sumó los catetos. Hay que sumar sus cuadrados: 81 + 144."), "c": t("225 is c². You still need the square root.", "225 es c². Falta sacar la raíz.")}, "right": "9² + 12² = 81 + 144 = 225, √225 = 15.", "solution": "9² + 12² = 225, c = √225 = 15."},
      "p3": {"ok": "b", "hints": {"a": t("Do not subtract the sides; subtract their squares: 169 − 144.", "No se restan los lados; se restan sus cuadrados: 169 − 144."), "c": t("25 is b². You still need the square root.", "25 es b². Falta sacar la raíz.")}, "right": "13² − 12² = 169 − 144 = 25, √25 = 5.", "solution": "b² = 169 − 144 = 25, b = 5."},
      "p4": {"ok": "a", "hints": {"b": t("Check: 5² + 12² = 25 + 144 = 169, and 13² = 169.", "Compruebe: 5² + 12² = 25 + 144 = 169, y 13² = 169."), "c": t("The converse only needs a² + b² = c². Check it.", "El converso solo pide que se cumpla a² + b² = c². Compruébelo.")}, "right": t("25 + 144 = 169 = 13², so it is a right triangle.", "25 + 144 = 169 = 13², así que es rectángulo."), "solution": t("Yes: 25 + 144 = 169.", "Sí: 25 + 144 = 169.")},
      "p5": {"ok": "c", "hints": {"a": t("Check: 4² + 5² = 16 + 25 = 41, and 6² = 36.", "Compruebe: 4² + 5² = 16 + 25 = 41, y 6² = 36."), "b": t("Not every triangle is a right triangle. Check a² + b² = c².", "No todo triángulo es rectángulo. Compruebe a² + b² = c².")}, "right": t("16 + 25 = 41, which is not 36, so it is not a right triangle.", "16 + 25 = 41, que no es 36, así que no es rectángulo."), "solution": t("No: 16 + 25 = 41 ≠ 36.", "No: 16 + 25 = 41 ≠ 36.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("You added the legs. Add their squares.", "Sumó los catetos. Hay que sumar sus cuadrados."), "b": t("100 is c². Take the square root.", "100 es c². Saque la raíz."), "c": t("You multiplied the legs. Add their squares.", "Multiplicó los catetos. Hay que sumar sus cuadrados.")}, "solution": "36 + 64 = 100, c = 10."},
      "B": {"ok": "c", "hints": {"a": t("You added the legs. Add their squares.", "Sumó los catetos. Hay que sumar sus cuadrados."), "b": t("169 is c². Take the square root.", "169 es c². Saque la raíz."), "d": t("You multiplied the legs. Add their squares.", "Multiplicó los catetos. Hay que sumar sus cuadrados.")}, "solution": "25 + 144 = 169, c = 13."},
      "C": {"ok": "a", "hints": {"b": t("Do not subtract the sides; subtract their squares.", "No se restan los lados; se restan sus cuadrados."), "c": t("You added the sides. For a leg, subtract the squares.", "Sumó los lados. Para un cateto se restan los cuadrados."), "d": t("144 is b². Take the square root.", "144 es b². Saque la raíz.")}, "solution": "169 − 25 = 144, b = 12."},
      "D": {"ok": "b", "hints": {"a": t("Subtract the squares: 625 − 49.", "Reste los cuadrados: 625 − 49."), "c": t("You added the sides. For a leg, subtract the squares.", "Sumó los lados. Para un cateto se restan los cuadrados."), "d": t("625 is 25². Subtract 7² and take the square root.", "625 es 25². Reste 7² y saque la raíz.")}, "solution": "625 − 49 = 576, b = 24."},
      "E": {"ok": "a", "hints": {"b": t("Check: 9 + 16 = 25 = 5².", "Compruebe: 9 + 16 = 25 = 5²."), "c": t("The converse only needs a² + b² = c².", "El converso solo pide que se cumpla a² + b² = c²."), "d": t("The three sides are enough to decide.", "Con los tres lados basta para decidir.")}, "solution": t("Yes: 9 + 16 = 25.", "Sí: 9 + 16 = 25.")},
      "F": {"ok": "a", "hints": {"b": t("Check: 36 + 64 = 100, and 11² = 121.", "Compruebe: 36 + 64 = 100, y 11² = 121."), "c": t("Not every triangle is a right triangle.", "No todo triángulo es rectángulo."), "d": t("The three sides are enough to decide.", "Con los tres lados basta para decidir.")}, "solution": t("No: 100 ≠ 121.", "No: 100 ≠ 121.")},
      "G": {"ok": "c", "hints": {"a": t("You added the legs. Add their squares: 144 + 25.", "Sumó los catetos. Hay que sumar sus cuadrados: 144 + 25."), "b": t("You subtracted the legs. The ramp is the hypotenuse: add the squares.", "Restó los catetos. La rampa es la hipotenusa: se suman los cuadrados."), "d": t("You multiplied. Add the squares and take the square root.", "Multiplicó. Sume los cuadrados y saque la raíz.")}, "solution": t("144 + 25 = 169, √169 = 13 feet.", "144 + 25 = 169, √169 = 13 pies.")},
      "H": {"ok": "d", "hints": {"a": t("You subtracted the sides. Subtract their squares: 100 − 36.", "Restó los lados. Hay que restar sus cuadrados: 100 − 36."), "b": t("The ladder is the hypotenuse, so the height is a leg: subtract.", "La escalera es la hipotenusa, así que la altura es un cateto: se resta."), "c": t("You multiplied. Subtract the squares and take the square root.", "Multiplicó. Reste los cuadrados y saque la raíz.")}, "solution": t("100 − 36 = 64, √64 = 8 feet.", "100 − 36 = 64, √64 = 8 pies.")}
     }}

    pies = t("feet", "pies")
    quiz = [
     ("A", t("The legs measure 6 and 8. The hypotenuse measures…", "Catetos 6 y 8. La hipotenusa mide…"), [("a", "14"), ("b", "100"), ("c", "48"), ("d", "10")]),
     ("B", t("The legs measure 5 and 12. The hypotenuse measures…", "Catetos 5 y 12. La hipotenusa mide…"), [("a", "17"), ("b", "169"), ("c", "13"), ("d", "60")]),
     ("C", t("The hypotenuse measures 13 and one leg measures 5. The other leg measures…", "Hipotenusa 13, un cateto 5. El otro cateto mide…"), [("a", "12"), ("b", "8"), ("c", "18"), ("d", "144")]),
     ("D", t("The hypotenuse measures 25 and one leg measures 7. The other leg measures…", "Hipotenusa 25, un cateto 7. El otro cateto mide…"), [("a", "18"), ("b", "24"), ("c", "32"), ("d", "625")]),
     ("E", t("Is a triangle with sides 3, 4, and 5 a right triangle?", "¿Es rectángulo un triángulo de lados 3, 4 y 5?"), [("a", t("Yes, because 9 + 16 = 25", "Sí, porque 9 + 16 = 25")), ("b", "No"), ("c", t("Only if it is isosceles", "Solo si es isósceles")), ("d", t("There is not enough information", "Falta información"))]),
     ("F", t("Is a triangle with sides 6, 8, and 11 a right triangle?", "¿Es rectángulo un triángulo de lados 6, 8 y 11?"), [("a", t("No, because 36 + 64 ≠ 121", "No, porque 36 + 64 ≠ 121")), ("b", t("Yes", "Sí")), ("c", t("Yes, always", "Sí, siempre")), ("d", t("There is no way to know", "No se puede saber"))]),
     ("G", t("A ramp covers a horizontal distance of 12 feet and rises 5 feet. How long is the ramp (the hypotenuse)?", "Una rampa cubre una distancia horizontal de 12 pies y sube 5 pies. ¿Cuánto mide la rampa (la hipotenusa)?"), [("a", f"17 {pies}"), ("b", f"7 {pies}"), ("c", f"13 {pies}"), ("d", f"60 {pies}")]),
     ("H", t("A 10-foot ladder leans against a wall with its foot 6 feet from the wall. How high up the wall does it reach?", "Una escalera de 10 pies se apoya en una pared, con el pie a 6 pies de la pared. ¿A qué altura llega?"), [("a", f"4 {pies}"), ("b", f"16 {pies}"), ("c", f"60 {pies}"), ("d", f"8 {pies}")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Use a² + b² = c² to find a missing side of a right triangle, recognize Pythagorean triples, and use the converse to check for a right angle.", "Use a² + b² = c² para hallar el lado que falta de un triángulo rectángulo, reconozca los triples pitagóricos y use el converso para comprobar un ángulo recto."),
        ("📐", t("Calculator for square roots", "Calculadora para las raíces")),
        [t("<strong>Identify</strong> the hypotenuse and the legs of a right triangle.", "<strong>Identificar</strong> la hipotenusa y los catetos de un triángulo rectángulo."),
         t("<strong>Use</strong> a² + b² = c² to find the hypotenuse.", "<strong>Aplicar</strong> a² + b² = c² para hallar la hipotenusa."),
         t("<strong>Solve</strong> for a leg when you know the hypotenuse and the other leg.", "<strong>Despejar</strong> un cateto conociendo la hipotenusa y el otro cateto."),
         t("<strong>Recognize</strong> common Pythagorean triples and their multiples.", "<strong>Reconocer</strong> los triples pitagóricos comunes y sus múltiplos."),
         t("<strong>Use</strong> the converse to decide whether a triangle is a right triangle, and solve real problems about building and distance.", "<strong>Usar</strong> el converso para decidir si un triángulo es rectángulo, y resolver problemas reales de construcción y distancia.")],
        secciones,
        (t(f"Solve four exercises that find the hypotenuse or a leg, four word problems about building or distance, and two exercises that use the converse to check whether a triangle is a right triangle. Then practice in {explora}: once the square root comes easily, all that is left is to decide which side is missing.",
           f"Resuelva cuatro ejercicios de calcular la hipotenusa o un cateto, cuatro problemas aplicados de construcción o distancia y dos ejercicios de verificar, con el converso, si un triángulo es rectángulo. Después practique en {explora}: cuando la raíz le salga sola, solo queda identificar cuál de los tres lados falta."),
         t("Check a corner at home with the 3-4-5 rule: measure 3 feet along one wall and 4 feet along the other from the corner, and mark both points. Measure the distance between the marks. If it is 5 feet, the corner is square. Then measure the width and height of a TV or computer screen and use the theorem to find its diagonal; compare it with the size on the box.",
           "Compruebe una esquina de su casa con la regla 3-4-5: mida 3 pies a lo largo de una pared y 4 pies a lo largo de la otra desde la esquina, y marque los dos puntos. Mida la distancia entre las marcas. Si es de 5 pies, la esquina está a escuadra. Después mida el ancho y el alto de la pantalla de un televisor o computadora y use el teorema para hallar su diagonal; compárela con la medida de la caja.")),
        quiz,
        t("Self-check checklist for the Pythagorean theorem", "Lista de autoevaluación del teorema de Pitágoras"),
        t("Self-check checklist: skills for the Pythagorean theorem and its converse", "Lista de autoevaluación: destrezas del teorema de Pitágoras y su converso"),
        [(t("Identifying the hypotenuse and legs", "Identificar hipotenusa y catetos"), t("I identify the hypotenuse and the legs correctly, even in triangles in different positions.", "Identifico correctamente la hipotenusa y los catetos, incluso en triángulos en distintas posiciones."), t("I identify the sides with occasional mistakes.", "Identifico los lados con errores ocasionales."), t("I confuse the hypotenuse with a leg.", "Confundo la hipotenusa con un cateto.")),
         (t("Writing a² + b² = c²", "Plantear a² + b² = c²"), t("I write a² + b² = c² correctly and recognize Pythagorean triples.", "Planteo a² + b² = c² correctamente y reconozco los triples pitagóricos."), t("I write the equation with the sides in the wrong places.", "Planteo la ecuación con los lados mal ubicados."), t("I do not write the equation correctly.", "No planteo la ecuación correctamente.")),
         (t("Finding the side", "Calcular el lado"), t("I find the hypotenuse and the legs correctly.", "Calculo correctamente la hipotenusa y los catetos."), t("I make mistakes solving or taking the square root.", "Calculo con errores al despejar o al sacar la raíz."), t("I do not solve or take the square root.", "No despejo ni saco la raíz.")),
         (t("Using the converse", "Aplicar el converso"), t("I use the converse to decide whether the triangle is a right triangle, choosing the longest side as c.", "Uso el converso para decidir si el triángulo es rectángulo, tomando el lado más largo como c."), t("I use the converse with mistakes.", "Aplico el converso con errores."), t("I do not use the converse to classify.", "No uso el converso para clasificar."))],
        t("<p>In this lesson you learned the Pythagorean theorem (a² + b² = c²) to find the hypotenuse and the legs of a right triangle, recognized Pythagorean triples, and used the converse to check whether a triangle is a right triangle, solving real problems about building and distance.</p>\n<p>In <strong>Lesson 6.3 · Similar figures and scale drawings (Thales' theorem)</strong> you will study figures that have the same shape but a different size. You will solve proportions to find unknown sides, read the scales of maps and plans, and measure heights you cannot reach with Thales' theorem.</p>",
          "<p>En esta lección se aprendió el teorema de Pitágoras (a² + b² = c²) para calcular la hipotenusa y los catetos de un triángulo rectángulo, se reconocieron los triples pitagóricos y se usó el converso para verificar si un triángulo es rectángulo, resolviendo problemas reales de construcción y distancia.</p>\n<p>En la <strong>Lección 6.3 · Semejanza de figuras y dibujos a escala (teorema de Tales)</strong> se estudiarán las figuras que tienen la misma forma pero distinto tamaño. Se resolverán proporciones para hallar lados desconocidos, se interpretarán escalas de mapas y planos, y se medirán alturas inaccesibles con el teorema de Tales.</p>"),
        ("6-3", ("", t("Lesson 6.3 · Similar figures and scale drawings (Thales' theorem)", "Lección 6.3 · Semejanza de figuras y dibujos a escala (teorema de Tales)"))),
        [(t("right triangle", "triángulo rectángulo"), t("A triangle with a 90° angle.", "Un triángulo con un ángulo de 90°.")),
         (t("legs", "catetos"), t("The two sides that form the right angle.", "Los dos lados que forman el ángulo recto.")),
         (t("hypotenuse", "hipotenusa"), t("The side across from the right angle. It is always the longest side.", "El lado opuesto al ángulo recto. Siempre es el lado más largo.")),
         (t("Pythagorean triple", "triple pitagórico"), t("Three whole numbers that make a² + b² = c² true, like 3, 4, 5.", "Tres números enteros que cumplen a² + b² = c², como 3, 4, 5.")),
         (t("converse", "converso"), t("The theorem turned around: if a² + b² = c², the triangle is a right triangle.", "El teorema al revés: si se cumple a² + b² = c², el triángulo es rectángulo."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
/* MODULE 1 · Squares on the sides */
function pintaCuadrados(){
  var a = +$("pc-a").value, b = +$("pc-b").value, c2 = a * a + b * b;
  $("pc-av").textContent = a; $("pc-bv").textContent = b;
  var minX = -a, maxX = b + a, minY = -b, maxY = a + b, esc = Math.min(560 / (maxX - minX), 440 / (maxY - minY)), ox = 320 - (minX + maxX) / 2 * esc, oy = 20 + maxY * esc;
  function V(p){ return [ox + p[0] * esc, oy - p[1] * esc]; }
  function poli(l, fill, st){ return '<polygon points="' + l.map(function(p){ var q = V(p); return f1(q[0]) + "," + f1(q[1]); }).join(" ") + '" fill="' + fill + '" stroke="' + st + '" stroke-width="2"/>'; }
  var s = '<svg class="geo-svg" viewBox="0 0 640 ' + f1(oy + b * esc + 20) + '" role="img" aria-label="' + T("Right triangle with legs " + a + " and " + b + " and a square on each side. Areas: " + (a * a) + ", " + (b * b) + ", and " + c2 + ".", "Triángulo rectángulo de catetos " + a + " y " + b + " con un cuadrado sobre cada lado. Áreas: " + (a * a) + ", " + (b * b) + " y " + c2 + ".") + '">';
  s += poli([[0, 0], [0, a], [-a, a], [-a, 0]], "#e3f2fd", "#0d47a1") + poli([[0, 0], [b, 0], [b, -b], [0, -b]], "#e8f5e9", "#1b5e20") + poli([[b, 0], [0, a], [a, a + b], [b + a, b]], "#fff8e1", "#5c3900");
  var i;
  for (i = 1; i < a; i++) s += lineaG(V([-a, i]), V([0, i]), "#90caf9", 1) + lineaG(V([-i, 0]), V([-i, a]), "#90caf9", 1);
  for (i = 1; i < b; i++) s += lineaG(V([i, 0]), V([i, -b]), "#a5d6a7", 1) + lineaG(V([0, -i]), V([b, -i]), "#a5d6a7", 1);
  s += poli([[0, 0], [b, 0], [0, a]], "#efebe9", "#4e342e") + marcaRecta(V([0, 0]), 0, 12, "#4e342e");
  s += texto(V([-a / 2, a / 2]), a > 1 ? "a² = " + (a * a) : "1", a > 2 ? 18 : 14, "#0d47a1") + texto(V([b / 2, -b / 2]), b > 1 ? "b² = " + (b * b) : "1", b > 2 ? 18 : 14, "#1b5e20");
  s += texto(V([(b + a) / 2, (a + b) / 2]), "c² = " + c2, 20, "#5c3900");
  $("pc-svg").innerHTML = s + "</svg>";
  $("pc-salida").innerHTML = '<div class="linea">' + (a * a) + " + " + (b * b) + " = <strong>" + c2 + "</strong>" + T(": the area of the square on the hypotenuse.", ": el área del cuadrado de la hipotenusa.") + "</div>" +
    '<div class="linea veredicto">' + T("The hypotenuse measures c = ", "La hipotenusa mide c = ") + "√" + c2 + (esCuadrado(c2) ? " = " + Math.sqrt(c2) + T(". It is a Pythagorean triple!", ". ¡Es un triple pitagórico!") : " ≈ " + aprox(Math.sqrt(c2), 2) + ".") + "</div>";
}
function genHipotenusa(){
  var tr = elige([[3, 4, 5], [5, 12, 13], [8, 15, 17], [6, 8, 10]]), rot = aleatorio(0, 359), letras = baraja(["p", "q", "r"]);
  var sc = 230 / tr[2], c = Math.cos(rad(rot)), sn = Math.sin(rad(rot));
  function G(p){ var x = p[0] * sc, y = p[1] * sc; return [x * c - y * sn, -(x * sn + y * c)]; }
  var pa = G([0, 0]), pb = G([tr[1], 0]), pc = G([0, tr[0]]), cx = (pa[0] + pb[0] + pc[0]) / 3, cy = (pa[1] + pb[1] + pc[1]) / 3;
  pa = [pa[0] - cx + 320, pa[1] - cy + 160]; pb = [pb[0] - cx + 320, pb[1] - cy + 160]; pc = [pc[0] - cx + 320, pc[1] - cy + 160];
  function medio(p, q){ var m = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2], v = [m[0] - 320, m[1] - 160], nn = Math.hypot(v[0], v[1]) || 1; return [m[0] + v[0] / nn * 22, m[1] + v[1] / nn * 22]; }
  var s = '<svg class="geo-svg" viewBox="0 0 640 320" role="img" aria-label="' + T("A turned right triangle with sides ", "Triángulo rectángulo girado con lados ") + letras.join(", ") + T(". The right angle is marked with a small square between sides " + letras[0] + " and " + letras[1] + ".", ". El ángulo recto está marcado con un cuadradito entre los lados " + letras[0] + " y " + letras[1] + ".") + '">';
  s += '<polygon points="' + [pa, pb, pc].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#efebe9" stroke="#4e342e" stroke-width="3"/>';
  var gAB = Math.atan2(-(pb[1] - pa[1]), pb[0] - pa[0]) * 180 / Math.PI, gAC = Math.atan2(-(pc[1] - pa[1]), pc[0] - pa[0]) * 180 / Math.PI;
  s += marcaRecta(pa, ((gAC - gAB + 360) % 360) < 180 ? gAB : gAC, 14, "#4e342e");
  s += texto(medio(pa, pc), letras[0], 22, "#0d47a1") + texto(medio(pa, pb), letras[1], 22, "#0d47a1") + texto(medio(pb, pc), letras[2], 22, "#0d47a1") + "</svg>";
  var pc2 = {}; pc2[letras[0]] = pc2[letras[1]] = T("That side touches the right angle: it is a leg.", "Ese lado toca el ángulo recto: es un cateto."); pc2.x = T("Only one side is the hypotenuse.", "Solo un lado es la hipotenusa.");
  return {enun: T("In this right triangle, which side is the hypotenuse?", "En este triángulo rectángulo, ¿cuál lado es la hipotenusa?") + s,
    opciones: letras.map(function(l){ return {html: T("Side ", "El lado ") + l, clave: l}; }).concat([{html: T("Any of the three", "Cualquiera de los tres"), clave: "x"}]), correcta: letras[2], porClave: pc2,
    pista: T("Find the small square: it marks the right angle.", "Busque el cuadradito: marca el ángulo recto."), bien: T("The hypotenuse is the side across from the right angle (the small square).", "La hipotenusa es el lado de enfrente del ángulo recto (el cuadradito)."), mal: T("The hypotenuse is " + letras[2] + ": the side that does not touch the right angle.", "La hipotenusa es " + letras[2] + ": el lado que no toca el ángulo recto.")};
}

/* MODULES 2 and 3 · Hypotenuse and leg, step by step */
function pasosHip(a, b){
  var c2 = a * a + b * b;
  return [T("Substitute the legs: ", "Se sustituyen los catetos: ") + auto(a + "<sup>2</sup> + " + b + "<sup>2</sup> = c<sup>2</sup>") + ".",
    T("Square and add: ", "Se calculan y se suman los cuadrados: ") + (a * a) + " + " + (b * b) + " = " + c2 + T(", so c² = ", ", así que c² = ") + c2 + ".",
    T("Take the square root: c = ", "Se saca la raíz cuadrada: c = ") + raizTxt(c2) + ".",
    '<span class="veredicto">' + T("The hypotenuse measures ", "La hipotenusa mide ") + (esCuadrado(c2) ? Math.sqrt(c2) : "≈ " + aprox(Math.sqrt(c2), 1)) + ".</span>"];
}
function pasosCat(c, a){
  var b2 = c * c - a * a;
  return [T("Write it with the hypotenuse alone: ", "Se plantea con la hipotenusa sola: ") + auto(a + "<sup>2</sup> + b<sup>2</sup> = " + c + "<sup>2</sup>") + T(", that is, ", ", es decir ") + (a * a) + " + b² = " + (c * c) + ".",
    T("Solve by subtracting: b² = ", "Se despeja restando: b² = ") + (c * c) + " − " + (a * a) + " = " + b2 + ".",
    T("Take the square root: b = ", "Se saca la raíz cuadrada: b = ") + raizTxt(b2) + ".",
    '<span class="veredicto">' + T("The other leg measures ", "El otro cateto mide ") + (esCuadrado(b2) ? Math.sqrt(b2) : "≈ " + aprox(Math.sqrt(b2), 1)) + T(". It is shorter than the hypotenuse, as it should be.", ". Es menor que la hipotenusa, como debe ser.") + "</span>"];
}
var HP_COLA = [[3, 4], [6, 8], [5, 7]], CT_COLA = [[13, 5], [10, 6], [9, 4]];
function nuevoHP(){
  var e = HP_COLA.length ? HP_COLA.shift() : (Math.random() < 0.7 ? tripleAzar(40).slice(0, 2) : [aleatorio(2, 9), aleatorio(2, 9)]);
  $("hp-enun").innerHTML = T("The legs measure " + e[0] + " and " + e[1] + ". What is the length of the hypotenuse?", "Los catetos miden " + e[0] + " y " + e[1] + ". ¿Cuánto mide la hipotenusa?"); HPS.carga(pasosHip(e[0], e[1]));
}
function nuevoCT(){
  var e; if (CT_COLA.length) e = CT_COLA.shift(); else if (Math.random() < 0.7){ var tr = tripleAzar(40); e = [tr[2], tr[aleatorio(0, 1)]]; } else { var c = aleatorio(6, 15); e = [c, aleatorio(2, c - 1)]; }
  $("ct-enun").innerHTML = T("The hypotenuse measures " + e[0] + " and one leg measures " + e[1] + ". What is the length of the other leg?", "La hipotenusa mide " + e[0] + " y un cateto mide " + e[1] + ". ¿Cuánto mide el otro cateto?"); CTS.carga(pasosCat(e[0], e[1]));
}
function genPracHip(){
  var e = Math.random() < 0.7 ? tripleAzar(50).slice(0, 2) : [aleatorio(2, 12), aleatorio(2, 12)], a = e[0], b = e[1], c2 = a * a + b * b;
  return {enun: T("The legs of a right triangle measure " + a + " and " + b + ". What is the length of the hypotenuse?", "Los catetos de un triángulo rectángulo miden " + a + " y " + b + ". ¿Cuánto mide la hipotenusa?"),
    solucion: a + "² + " + b + "² = " + (a * a) + " + " + (b * b) + " = " + c2 + T(", and c = ", ", y c = ") + raizTxt(c2) + ".",
    evalua: function(v){ return evaluaRaiz(v, c2, [{v: a + b, msg: T("You do not add the sides themselves: add their squares, then take the square root.", "Los lados no se suman directamente: se suman sus cuadrados y después se saca la raíz.")}, {v: c2, msg: T("That is c². You still need to take the square root.", "Ese es c². Falta sacar la raíz cuadrada.")}]); }};
}
function genPracCat(){
  var c, a; if (Math.random() < 0.7){ var tr = tripleAzar(50); c = tr[2]; a = tr[aleatorio(0, 1)]; } else { c = aleatorio(6, 16); a = aleatorio(2, c - 1); }
  var b2 = c * c - a * a;
  return {enun: T("The hypotenuse of a right triangle measures " + c + " and one leg measures " + a + ". What is the length of the other leg?", "La hipotenusa de un triángulo rectángulo mide " + c + " y un cateto mide " + a + ". ¿Cuánto mide el otro cateto?"),
    solucion: c + "² − " + a + "² = " + (c * c) + " − " + (a * a) + " = " + b2 + T(", and b = ", ", y b = ") + raizTxt(b2) + ".",
    evalua: function(v){ return evaluaRaiz(v, b2, [{v: Math.sqrt(c * c + a * a), msg: T("You added the squares. For a leg, subtract the square of the known leg from the square of the hypotenuse.", "Se sumaron los cuadrados. Para un cateto, al cuadrado de la hipotenusa se le resta el del cateto conocido.")},
      {v: c - a, msg: T("You do not subtract the sides themselves: subtract their squares, then take the square root.", "Los lados no se restan directamente: se restan sus cuadrados y después se saca la raíz.")}, {v: b2, msg: T("That is b². You still need to take the square root.", "Ese es b². Falta sacar la raíz cuadrada.")}]); }};
}

/* MODULE 4 · Triples */
function pintaTP(){
  var tr = $("tp-base").value.split(",").map(Number), k = +$("tp-k").value, a = tr[0] * k, b = tr[1] * k, c = tr[2] * k;
  $("tp-kv").textContent = k;
  $("tp-salida").innerHTML = '<div class="linea grande">' + a + " – " + b + " – " + c + "</div>" +
    '<div class="linea">' + T("Check: ", "Comprobación: ") + a + "² + " + b + "² = " + com(a * a) + " + " + com(b * b) + " = " + com(a * a + b * b) + T(", and ", ", y ") + c + "² = " + com(c * c) + ". ✓</div>" +
    (k > 1 ? '<div class="linea">' + T("It is the triple " + tr.join("-") + " multiplied by " + k + ": each side times " + k + ".", "Es el triple " + tr.join("-") + " multiplicado por " + k + ": cada lado por " + k + ".") + "</div>" : "");
}
function genTriple(){
  if (Math.random() < 0.55){
    var tr = tripleAzar(60), falta = aleatorio(0, 2), vis = tr.map(function(x, i){ return i === falta ? "?" : x; }).join(", ");
    var ok = tr[falta], o = [{html: String(ok), clave: "n" + ok}], pc = {};
    var otros = tr.filter(function(x, i){ return i !== falta; });
    var suma = falta === 2 ? otros[0] + otros[1] : otros[1] - otros[0]; o.push({html: String(suma), clave: "n" + suma}); pc["n" + suma] = T("You do not add or subtract the sides themselves: work with their squares.", "Los lados no se suman ni se restan directamente: se trabaja con los cuadrados.");
    [ok + 1, ok - 1, ok + 2].forEach(function(v){ o.push({html: String(v), clave: "n" + v}); });
    return {enun: T("Complete the Pythagorean triple: " + vis + " (the last number is the hypotenuse).", "Complete el triple pitagórico: " + vis + " (el último número es la hipotenusa)."), opciones: [o[0]].concat(baraja(o.slice(1)).slice(0, 3)), correcta: o[0].clave, porClave: pc,
      pista: T("Is it a multiple of 3-4-5, 5-12-13, 8-15-17, or 7-24-25?", "¿Es un múltiplo de 3-4-5, 5-12-13, 8-15-17 o 7-24-25?"),
      bien: tr.join("-") + T(" makes ", " cumple ") + tr[0] + "² + " + tr[1] + "² = " + tr[2] + T("² true.", "²."), mal: T("It is ", "Es ") + tr.join("-") + ": " + com(tr[0] * tr[0]) + " + " + com(tr[1] * tr[1]) + " = " + com(tr[2] * tr[2]) + "."};
  }
  var b = tripleAzar(60), malos = [];
  while (malos.length < 3){ var m = tripleAzar(60).slice(); m[2] += elige([1, -1, 2]); if (m[0] * m[0] + m[1] * m[1] !== m[2] * m[2] && malos.indexOf(m.join("-")) < 0 && m.join("-") !== b.join("-")) malos.push(m.join("-")); }
  var o2 = [{html: b.join(" – "), clave: "b"}].concat(malos.map(function(m, i){ return {html: m.split("-").join(" – "), clave: "m" + i}; }));
  return {enun: T("Which of these is a Pythagorean triple?", "¿Cuál de estos es un triple pitagórico?"), opciones: o2, correcta: "b", porClave: {},
    pista: T("Check a² + b² = c² for each one, or look for a multiple of a known triple.", "Compruebe a² + b² = c² en cada uno, o busque un múltiplo de un triple conocido."),
    bien: b[0] + "² + " + b[1] + "² = " + com(b[0] * b[0] + b[1] * b[1]) + " = " + b[2] + "².", mal: T("Only " + b.join("-") + " makes a² + b² = c² true: ", "Solo " + b.join("-") + " cumple a² + b² = c²: ") + com(b[0] * b[0]) + " + " + com(b[1] * b[1]) + " = " + com(b[2] * b[2]) + "."};
}

/* MODULE 5 · Converse */
function genConverso(){
  var lados, si = Math.random() < 0.5;
  if (si) lados = tripleAzar(60);
  else { lados = tripleAzar(60).slice(); lados[aleatorio(0, 2)] += elige([1, -1, 2]); if (lados[0] * lados[0] + lados[1] * lados[1] === lados[2] * lados[2]) lados[2]++; }
  var ord = lados.slice().sort(function(x, y){ return x - y; }), a = ord[0], b = ord[1], c = ord[2], s = a * a + b * b;
  var ok = s === c * c, vis = baraja(lados).join(", ");
  var exp = T("The longest side is " + c + ". ", "El lado más largo es " + c + ". ") + a + "² + " + b + "² = " + com(a * a) + " + " + com(b * b) + " = " + com(s) + T(" and ", " y ") + c + "² = " + com(c * c) + ": " + (ok ? T("they match, so it is a right triangle.", "coinciden, así que es rectángulo.") : T("they do not match, so it is not a right triangle.", "no coinciden, así que no es rectángulo."));
  return {enun: T("Is a triangle with sides " + vis + " a right triangle?", "¿Es rectángulo un triángulo cuyos lados miden " + vis + "?"),
    opciones: [{html: T("Yes, it is a right triangle", "Sí, es rectángulo"), clave: "si"}, {html: T("No, it is not a right triangle", "No, no es rectángulo"), clave: "no"}, {html: T("There is no way to know without measuring the angles", "No se puede saber sin medir los ángulos"), clave: "x"}],
    correcta: ok ? "si" : "no", porClave: {x: T("Yes, you can: the converse of the theorem lets you decide with the sides alone.", "Sí se puede: el converso del teorema permite decidirlo solo con los lados.")},
    pista: T("Use the longest side as c, and check whether a² + b² = c².", "Tome el lado más largo como c y compruebe si a² + b² = c²."), bien: exp, mal: exp};
}

/* Start */
["pc-a", "pc-b"].forEach(function(id){ $(id).addEventListener("input", pintaCuadrados); });
pintaCuadrados();
OMR("p1", genHipotenusa);
var HPS = pasoAPaso("hp", []), CTS = pasoAPaso("ct", []);
$("hp-nuevo").addEventListener("click", nuevoHP); nuevoHP();
creaPracticaLibre("p2", genPracHip);
$("ct-nuevo").addEventListener("click", nuevoCT); nuevoCT();
creaPracticaLibre("p3", genPracCat);
$("tp-base").addEventListener("change", pintaTP); $("tp-k").addEventListener("input", pintaTP); pintaTP();
OMR("p4", genTriple);
OMR("p5", genConverso);
'''

def practica_pagina():
    n = N
    explora = t('<a href="explore-pythagoras.html">Explore: the Pythagorean theorem in real life</a>', '<a href="explorar-pitagoras.html">Explorar: el teorema de Pitágoras en la vida real</a>')
    def pasos(pre, nuevo):
        return f'''      <div class="panel">
        <p class="enun" id="{pre}-enun"></p>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig"></button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all the steps", "Mostrar todos los pasos")}</button><button type="button" class="btn-sec" id="{pre}-nuevo">{nuevo}</button></div>
      </div>
      <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>'''
    def raiz(pid, tit, et):
        return B.libre(pid, tit, et, nota=False).replace('<div class="fila-btn">', '<p class="nota">' + t("If the result is not exact, round to the nearest tenth (for example, 7.8).", "Si el resultado no es exacto, redondee a la décima (por ejemplo, 7.8).") + '</p>\n        <div class="fila-btn">', 1)
    otro = t("Another example", "Otro ejemplo")
    mods = [
     (t("theorem", "teorema"), t("The right triangle and the theorem", "El triángulo rectángulo y el teorema"),
      f'''      <p>{t("In a right triangle, the two sides that form the 90° angle are the <strong>legs</strong> (a and b). The side across from the right angle, the longest one, is the <strong>hypotenuse</strong> (c).", "En un triángulo rectángulo, los dos lados que forman el ángulo de 90° son los <strong>catetos</strong> (a y b). El lado de enfrente del ángulo recto, el más largo, es la <strong>hipotenusa</strong> (c).")}</p>
{n3.formula("a² + b² = c²")}
      <h3>{t("The proof with squares", "La demostración con cuadrados")}</h3>
      <p>{t("Draw a square on each side. The theorem says that the areas of the two small squares together are exactly the area of the big square. Change the legs and check it.", "Sobre cada lado se dibuja un cuadrado. El teorema dice que las áreas de los dos cuadrados pequeños juntas son exactamente el área del cuadrado grande. Cambie los catetos y compruébelo.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo" style="flex:1;min-width:200px;"><label for="pc-a">{t("Leg a:", "Cateto a:")} <span id="pc-av"></span></label><input type="range" id="pc-a" min="1" max="12" step="1" value="3"></div>
        <div class="campo" style="flex:1;min-width:200px;"><label for="pc-b">{t("Leg b:", "Cateto b:")} <span id="pc-bv"></span></label><input type="range" id="pc-b" min="1" max="12" step="1" value="4"></div></div></div>
      <div id="pc-svg"></div>
{n3.salida("pc-salida")}
      <div class="caja-tip">{t("The hypotenuse is always c: it is the longest side, and it is across from the right angle. Finding it is the first step, because in the formula it always takes the place that is alone.", "La hipotenusa siempre es c: es el lado más largo y está enfrente del ángulo recto. Identificarla bien es el primer paso, porque en la fórmula ocupa siempre el lugar que va solo.")}</div>
{B.om("p1", t("Practice: which side is the hypotenuse?", "Practique: ¿cuál es la hipotenusa?"))}'''),
     (t("hypotenuse", "hipotenusa"), t("Finding the hypotenuse", "Calcular la hipotenusa"),
      f'''      <p>{t("With the two legs, substitute into the formula, add the squares, and take the square root.", "Con los dos catetos se sustituye en la fórmula, se suman los cuadrados y se saca la raíz cuadrada.")}</p>
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos("hp", otro)}
{raiz("p2", t("Practice: find the hypotenuse", "Practique: calcule la hipotenusa"), t("Hypotenuse", "Hipotenusa"))}'''),
     (t("leg", "cateto"), t("Finding a leg", "Calcular un cateto"),
      f'''      <p>{t("If you know the hypotenuse and one leg, solve for the other: subtract the square of the known leg from the square of the hypotenuse, and take the square root.", "Si se conocen la hipotenusa y un cateto, se despeja el otro: al cuadrado de la hipotenusa se le resta el cuadrado del cateto conocido, y se saca la raíz.")}</p>
{n3.formula("b² = c² − a²")}
      <h3>{t("Step by step", "Paso a paso")}</h3>
{pasos("ct", otro)}
      <div class="caja-tip">{t("For a leg, subtract: the most common mistake is to add the two squares. If your answer is longer than the hypotenuse, something is wrong: no leg can be longer than the hypotenuse.", "La hipotenusa se resta, no se suma: el error más común al buscar un cateto es sumar los dos cuadrados. Si el resultado sale más largo que la hipotenusa, algo está mal: ningún cateto puede ser más largo que ella.")}</div>
{raiz("p3", t("Practice: find the missing leg", "Practique: calcule el cateto que falta"), t("Leg", "Cateto"))}
      <div class="caja-tip">{t(f"Word problems with ladders, ramps, roofs, and screens: {explora}.", f"Problemas con escaleras, rampas, techos y pantallas: {explora}.")}</div>'''),
     ("triples", t("Pythagorean triples", "Triples pitagóricos"),
      f'''      <p>{t("Some right triangles have three whole-number sides. Recognizing them saves calculations on the test, and their multiples work too: if 3-4-5 is a triple, so are 6-8-10 and 9-12-15.", "Algunos triángulos rectángulos tienen los tres lados enteros. Reconocerlos ahorra cálculos en el examen, y sus múltiplos también funcionan: si 3-4-5 es un triple, también lo son 6-8-10 y 9-12-15.")}</p>
      <h3>{t("Triple maker", "Generador de triples")}</h3>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="tp-base">{t("Basic triple", "Triple básico")}</label><select id="tp-base"><option value="3,4,5">3-4-5</option><option value="5,12,13">5-12-13</option><option value="8,15,17">8-15-17</option><option value="7,24,25">7-24-25</option></select></div>
        <div class="campo" style="flex:1;min-width:200px;"><label for="tp-k">{t("Multiply by:", "Multiplicar por:")} <span id="tp-kv"></span></label><input type="range" id="tp-k" min="1" max="10" step="1" value="1"></div></div></div>
{n3.salida("tp-salida")}
{B.om("p4", t("Practice: recognize the triple", "Practique: reconozca el triple"))}'''),
     (t("converse", "converso"), t("The converse of the theorem", "El converso del teorema"),
      f'''      <p>{t("The converse goes the other way: if the three sides make a² + b² = c² true, the triangle is a right triangle. It is a way to check whether a corner is a right angle. The longest side always plays the part of c, even if it is not listed last.", "El converso va en sentido contrario: si los tres lados cumplen a² + b² = c², el triángulo es rectángulo. Sirve para comprobar si una esquina forma un ángulo recto. El lado más largo hace siempre de c, aunque no aparezca al final.")}</p>
{B.om("p5", t("Practice: is it a right triangle?", "Practique: ¿es rectángulo?"))}
      <div class="caja-tip">{t("On the job: carpenters mark 3 feet on one wall and 4 on the other. If the diagonal measures 5, the corner is square. That is the converse of the theorem.", "En la obra: los carpinteros marcan 3 pies en una pared y 4 en la otra; si la diagonal mide 5, la esquina está a escuadra. Es el converso del teorema.")}</div>''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=ESTILO_GEO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Teorema de Pitágoras: demostración, aplicaciones y converso")
