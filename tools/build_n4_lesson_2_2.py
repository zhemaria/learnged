"""Level 4 · Lesson 2.2 · Composite 3D figures and surface area — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_2-2.html, algebra/n4-l2-2.html (decomposing a figure, an idea of optimization)
and geometria/compuestas_3d and area_superficie (the composite-figure workshop and the solid with its net). All of them are
rebuilt here, inside LearnGED, with US units. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "2-2"
TEMA = ("3D volume and polynomials", "Volumen 3D y polinomios")
TIT = ("Composite 3D figures and surface area", "Figuras 3D compuestas y área de superficie")
SCRIPTS = n4.SCRIPTS + ("/math/solid4.js",)

def fig_silo():
    L = "#37474f"
    s = ('<path d="M120 100 L120 250 A70 18 0 0 0 260 250 L260 100" fill="#bbdefb" stroke="#37474f" stroke-width="2.5"/>'
         '<path d="M120 250 A70 18 0 0 1 260 250" fill="none" stroke="#90a4ae" stroke-width="2" stroke-dasharray="6 5"/>'
         '<path d="M120 100 L190 30 L260 100 A70 18 0 0 1 120 100 Z" fill="#ffe0b2" stroke="#37474f" stroke-width="2.5"/>'
         '<path d="M120 100 A70 18 0 0 0 260 100" fill="none" stroke="#37474f" stroke-width="2"/>'
         '<line x1="190" y1="100" x2="260" y2="100" stroke="#c62828" stroke-width="3"/><text x="225" y="92" font-size="15" font-weight="700" fill="#c62828" text-anchor="middle">r = 3</text>'
         '<line x1="285" y1="30" x2="285" y2="100" stroke="#e65100" stroke-width="2.5" stroke-dasharray="6 4"/><text x="292" y="70" font-size="15" font-weight="700" fill="#e65100">2</text>'
         '<line x1="285" y1="100" x2="285" y2="250" stroke="#1565c0" stroke-width="2.5" stroke-dasharray="6 4"/><text x="292" y="180" font-size="15" font-weight="700" fill="#1565c0">8</text>'
         f'<text x="380" y="80" font-size="15" font-weight="700" fill="#e65100">{t("cone", "cono")}</text><text x="380" y="180" font-size="15" font-weight="700" fill="#1565c0">{t("cylinder", "cilindro")}</text>'
         f'<text x="190" y="300" font-size="16" font-weight="700" fill="#10174f" text-anchor="middle">V = V({t("cylinder", "cilindro")}) + V({t("cone", "cono")})</text>')
    return B.svg("0 0 480 320", t("A silo: a cylinder with radius 3 and height 8, with a cone of height 2 on top. Its volume is the volume of the cylinder plus the volume of the cone.",
                                  "Un silo: un cilindro de radio 3 y altura 8 con un cono de altura 2 encima. Su volumen es el volumen del cilindro más el volumen del cono."), s, 440)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lesson 2.1.</strong> In Lesson 2.1 you found the volume of single solids (sphere, cone, pyramid). Many real objects, though, are not one single solid: a silo is a cylinder topped with a cone; a medicine capsule is a cylinder with two half-spheres. This lesson teaches you to <strong>break</strong> those figures into simple parts to find their volume, and to find how much material covers their surface.",
 "<strong>Conexión con la lección anterior.</strong> En la Lección 2.1 se calculó el volumen de sólidos sueltos (esfera, cono, pirámide). Muchos objetos reales, sin embargo, no son un solo sólido: un silo es un cilindro coronado por un cono; una cápsula de medicina es un cilindro con dos semiesferas. Esta lección enseña a <strong>descomponer</strong> esas figuras en partes simples para hallar su volumen, y a calcular cuánto material cubre su superficie.")}</p>
<p>{t("A <strong>composite figure</strong> is simple solids put together (or one taken out of another). The plan is always the same:", "Una <strong>figura compuesta</strong> es la unión (o la diferencia) de sólidos simples. La estrategia es siempre la misma:")}</p>
<ol><li>{t("Name the simple parts that make it up (cylinder, cone, half-sphere, prism…).", "Identificar las partes simples que la forman (cilindro, cono, semiesfera, prisma…).")}</li>
<li>{t("Find the volume of each part separately.", "Calcular el volumen de cada parte por separado.")}</li>
<li>{t("<strong>Add</strong> the volumes if the parts are joined, or <strong>subtract</strong> if there is a hole.", "<strong>Sumar</strong> los volúmenes si las partes se unen, o <strong>restar</strong> si hay un hueco.")}</li></ol>
{fig_silo()}
{enlace(n, t("decompose", "descomponer"), t("breaking a figure into parts", "cómo descomponer una figura"), t("Name the pieces of each figure and decide whether the volumes are added or subtracted.", "Identifique las piezas de cada figura y decida si los volúmenes se suman o se restan."))}'''

    s2 = f'''{ejemplo(t("Example 1: a cylinder with a half-sphere. A tank is a cylinder with radius 3 feet and height 10 feet, topped by a half-sphere with radius 3 feet. Find its total volume.", "Ejemplo 1 · Cilindro con semiesfera. Un tanque está formado por un cilindro de 3 pies de radio y 10 pies de altura, coronado por una semiesfera de 3 pies de radio. Hallar su volumen total."),
  [("1", t("Volume of the cylinder.", "Volumen del cilindro."), "V = πr²h = π · 9 · 10 = 90π."),
   ("2", t("Volume of the half-sphere: half of 4/3 πr³.", "Volumen de la semiesfera: la mitad de 4/3 πr³."), "1/2 · 4/3 · π · 27 = 1/2 · 36π = 18π."),
   ("3", t("Add.", "Se suman."), "90π + 18π = 108π."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>V = 108π ≈ 339.3 cubic feet</strong>.", "<strong>V = 108π ≈ 339.3 pies cúbicos</strong>."))])}
{ejemplo(t("Example 2: with a hole (subtract). A 10 × 10 × 5 inch block has a hole drilled through it: a cylinder with radius 2 inches and height 5 inches. Find the volume of what is left.", "Ejemplo 2 · Con un hueco (resta). A un bloque de 10 × 10 × 5 pulgadas se le perfora un cilindro de 2 pulgadas de radio y 5 pulgadas de altura. Hallar el volumen del sólido que queda."),
  [("1", t("Volume of the block (a prism).", "Volumen del bloque (un prisma)."), "10 · 10 · 5 = 500."),
   ("2", t("Volume of the hole.", "Volumen del hueco."), "π · 2² · 5 = 20π."),
   ("3", t("Subtract.", "Se resta."), "500 − 20π."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>V = 500 − 20π ≈ 437.2 cubic inches</strong>.", "<strong>V = 500 − 20π ≈ 437.2 pulgadas cúbicas</strong>."))])}
{caja("ojo", t("Add or subtract?", "¿Sumar o restar?"), t("<p>If the parts come together to make a bigger body, add. If a part is taken away (a hole, a hollow), subtract. Make a drawing and label each part before you calculate.</p>", "<p>Si las partes se juntan para formar un cuerpo más grande, se suman. Si una parte se quita (un agujero, un hueco), se resta. Conviene hacer un dibujo y rotular cada parte antes de calcular.</p>"))}
{practica("p1", t("Practice 1 — Cylinder and cone", "Práctica 1 — Cilindro y cono"), t("A cylinder with radius 2 and height 6 has a cone with radius 2 and height 3 on top. What is the total volume?", "Un cilindro de radio 2 y altura 6 tiene encima un cono de radio 2 y altura 3. ¿Cuál es el volumen total?"), [("a", "24π"), ("b", "28π"), ("c", "32π")])}
{practica("p2", t("Practice 2 — Cube and pyramid", "Práctica 2 — Cubo y pirámide"), t("A cube with side 5 has a pyramid with a 5 × 5 base and height 3 on top. What is the total volume?", "Un cubo de lado 5 tiene encima una pirámide de base 5 × 5 y altura 3. ¿Cuál es el volumen total?"), [("a", "150"), ("b", "175"), ("c", "125")])}
{practica("p3", t("Practice 3 — A half-sphere", "Práctica 3 — Una semiesfera"), t("What is the volume of a half-sphere with radius 6?", "¿Cuál es el volumen de una semiesfera de radio 6?"), [("a", "288π"), ("b", "72π"), ("c", "144π")])}
{enlace(n, t("volume", "volumen"), t("the volume of composite figures", "el volumen de figuras compuestas"), t("Build silos, tanks, capsules, towers, and drilled blocks, and see how the volumes of the parts add up.", "Arme silos, tanques, cápsulas, torres y bloques perforados, y observe cómo se suman los volúmenes de las partes."))}'''

    s3 = f'''<p>{t("The <strong>surface area</strong> is the sum of the areas of all the faces or surfaces of a solid. It answers questions like how much paint, paper, or material you need to cover it. These formulas are on the formula sheet too:", "El <strong>área de superficie</strong> es la suma de las áreas de todas las caras o superficies de un sólido. Responde preguntas como cuánta pintura, papel o material se necesita para cubrirlo. Estas fórmulas también están en la hoja de fórmulas:")}</p>
{tabla(t("Lateral and total surface area of the cylinder and the cone", "Área lateral y total del cilindro y del cono"), t("Lateral and total surface area formulas of the cylinder and the cone", "Fórmulas del área lateral y total del cilindro y del cono"),
  [t("Solid", "Sólido"), t("Lateral area", "Área lateral"), t("Total area", "Área total")],
  [[t("Cylinder", "Cilindro"), "2πrh", "2πrh + 2πr²"], [t("Cone", "Cono"), t("πrℓ (ℓ = slant height)", "πrℓ (ℓ = altura inclinada)"), "πrℓ + πr²"]])}
{ejemplo(t("Example 3: the lateral area of a cylinder. How much paint covers the side of a round tank with radius 4 feet and height 10 feet?", "Ejemplo 3 · Área lateral de un cilindro. ¿Cuánta pintura cubre la superficie lateral de un tanque cilíndrico de 4 pies de radio y 10 pies de altura?"),
  [("1", t("Use the lateral area.", "Se usa el área lateral."), "2πrh."),
   ("2", t("Substitute.", "Se sustituye."), "2 · π · 4 · 10 = 80π."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>80π ≈ 251.3 square feet</strong>.", "<strong>80π ≈ 251.3 pies cuadrados</strong>."))])}
{ejemplo(t("Example 4: the lateral area of a cone. A cone has radius 6 inches and slant height (ℓ) 10 inches. Find its lateral area.", "Ejemplo 4 · Área lateral de un cono. Un cono tiene 6 pulgadas de radio y 10 pulgadas de altura inclinada (ℓ). Hallar su área lateral."),
  [("1", t("Use the lateral area of the cone.", "Se usa el área lateral del cono."), "πrℓ."),
   ("2", t("Substitute.", "Se sustituye."), "π · 6 · 10 = 60π."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>60π ≈ 188.5 square inches</strong>.", "<strong>60π ≈ 188.5 pulgadas cuadradas</strong>."))])}
{caja("ojo", t("Slant height, not the straight-up height", "Altura inclinada, no altura vertical"), t("<p>The lateral area of a cone uses the slant height ℓ (the distance from the edge of the base to the point, along the surface), not the height h. If you only have h, find the slant height with Pythagoras: ℓ = √(r² + h²). And “lateral” means without the base and the top: the total area adds them.</p>", "<p>El área lateral del cono usa la altura inclinada ℓ (la distancia del borde de la base a la punta, por la superficie), no la altura vertical h. Si solo se da h, la inclinada se obtiene con Pitágoras: ℓ = √(r² + h²). Y «lateral» quiere decir sin la base ni la tapa: el área total las añade.</p>"))}
{practica("p4", t("Practice 4 — The side of a cylinder", "Práctica 4 — El lado de un cilindro"), t("What is the lateral area of a cylinder with radius 3 and height 7?", "¿Cuál es el área lateral de un cilindro de radio 3 y altura 7?"), [("a", "21π"), ("b", "42π"), ("c", "84π")])}
{practica("p5", t("Practice 5 — The side of a cone", "Práctica 5 — El lado de un cono"), t("What is the lateral area of a cone with radius 5 and slant height 12?", "¿Cuál es el área lateral de un cono de radio 5 y altura inclinada 12?"), [("a", "60π"), ("b", "30π"), ("c", "120π")])}
{practica("p6", t("Practice 6 — The whole cylinder", "Práctica 6 — El cilindro completo"), t("What is the total area of a cylinder with radius 2 and height 5?", "¿Cuál es el área total de un cilindro de radio 2 y altura 5?"), [("a", "20π"), ("b", "40π"), ("c", "28π")])}
{enlace(n, t("surface", "superficie"), t("the surface area", "el área de superficie"), t("See each solid closed and opened flat (its net), and build the area piece by piece.", "Vea cada sólido cerrado y abierto en el plano (su desarrollo), y construya el área pieza por pieza."))}'''

    s4 = f'''<p>{t("In design and engineering you want a given volume with the <strong>least material</strong> possible, that is, with the smallest surface area. For example, of two cans that hold the same volume, the one with less surface area costs less material.", "En diseño e ingeniería interesa lograr un volumen dado con la <strong>menor cantidad de material</strong> posible, es decir, con la menor área de superficie. Por ejemplo, entre dos latas que guardan el mismo volumen, la que tenga menor área de superficie cuesta menos material.")}</p>
{ejemplo(t("Example 5: comparing material. Two boxes hold 100 cubic inches. Box A is 10 × 10 × 1 and box B is 5 × 5 × 4. Which one uses less cardboard (less surface area)?", "Ejemplo 5 · Comparar material. Dos cajas guardan 100 pulgadas cúbicas. La caja A mide 10 × 10 × 1 y la caja B, 5 × 5 × 4. ¿Cuál usa menos cartón (menor área de superficie)?"),
  [("1", t("Area of A.", "Área de A."), "2(10·10 + 10·1 + 10·1) = 2(100 + 10 + 10) = 240."),
   ("2", t("Area of B.", "Área de B."), "2(5·5 + 5·4 + 5·4) = 2(25 + 20 + 20) = 130."),
   ("✓", t("Answer.", "Respuesta."), t("With the same volume, <strong>box B</strong> uses much less cardboard. Shapes closer to a cube tend to have less surface area.", "Con el mismo volumen, la <strong>caja B</strong> usa mucho menos cartón. Las formas más parecidas a un cubo tienden a tener menor área de superficie."))])}
{enlace(n, t("optimize", "optimizacion"), t("an idea of optimization", "la idea de optimización"), t("Compare boxes with the same volume and find the one that uses the least cardboard.", "Compare cajas del mismo volumen y encuentre la que usa menos cartón."))}'''

    secciones = [("s-" + t("decompose", "descomponer"), t("Breaking a composite figure into parts", "Descomponer una figura compuesta"), s1),
                 ("s-" + t("volume", "volumen"), t("The volume of composite figures", "Volumen de figuras compuestas"), s2),
                 ("s-" + t("surface", "superficie"), t("Surface area", "Área de superficie"), s3),
                 ("s-" + t("optimize", "optimizacion"), t("An idea of optimization", "Una idea de optimización"), s4)]

    lesson = {"next": t("Lesson 2.3", "Lección 2.3"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("That is only the cylinder: π · 4 · 6 = 24π. Add the cone.", "Ese es solo el cilindro: π · 4 · 6 = 24π. Falta sumar el cono."), "c": t("The cone has 1/3: 1/3 · π · 4 · 3 = 4π, not 8π.", "El cono lleva 1/3: 1/3 · π · 4 · 3 = 4π, no 8π.")}, "right": "24π + 4π = 28π.", "solution": "V = 24π + 4π = 28π."},
      "p2": {"ok": "a", "hints": {"b": t("The pyramid has 1/3: 1/3 · 25 · 3 = 25, not 50.", "La pirámide lleva 1/3: 1/3 · 25 · 3 = 25, no 50."), "c": t("That is only the cube. Add the pyramid.", "Ese es solo el cubo. Falta sumar la pirámide.")}, "right": "125 + 25 = 150.", "solution": "V = 125 + 25 = 150."},
      "p3": {"ok": "c", "hints": {"a": t("288π is the whole sphere. Take half.", "288π es la esfera entera. Tome la mitad."), "b": t("Check: 4/3 · 216 = 288, and half is 144.", "Revise: 4/3 · 216 = 288, y la mitad es 144.")}, "right": "1/2 · 4/3 · π · 216 = 144π.", "solution": "V = 144π."},
      "p4": {"ok": "b", "hints": {"a": t("You left out the 2: the formula is 2πrh.", "Olvidó el 2: la fórmula es 2πrh."), "c": t("2 · 3 · 7 = 42, not 84.", "2 · 3 · 7 = 42, no 84.")}, "right": "2 · π · 3 · 7 = 42π.", "solution": "42π."},
      "p5": {"ok": "a", "hints": {"b": t("π · 5 · 12 = 60π; there is no 1/2 here.", "π · 5 · 12 = 60π; aquí no hay 1/2."), "c": t("The lateral area of a cone is πrℓ, without a 2.", "El área lateral del cono es πrℓ, sin el 2.")}, "right": "π · 5 · 12 = 60π.", "solution": "60π."},
      "p6": {"ok": "c", "hints": {"a": t("That is only the side: 2π · 2 · 5 = 20π. Add the two circles: 2πr².", "Eso es solo el lado: 2π · 2 · 5 = 20π. Falta sumar los dos círculos: 2πr²."), "b": t("The two circles add 2π · 4 = 8π, not 20π.", "Los dos círculos suman 2π · 4 = 8π, no 20π.")}, "right": "20π + 8π = 28π.", "solution": "2πrh + 2πr² = 20π + 8π = 28π."},
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("That is only the cylinder. Add the half-sphere.", "Ese es solo el cilindro. Falta sumar la semiesfera."), "b": t("The half-sphere is 18π, not 36π: take half of the sphere.", "La semiesfera es 18π, no 36π: tome la mitad de la esfera."), "d": t("You subtracted. The parts are joined: add.", "Restó. Las partes se juntan: se suman.")}, "solution": "90π + 18π = 108π."},
      "B": {"ok": "d", "hints": {"a": t("The cone has 1/3: 1/3 · 4 · 3 = 4.", "El cono lleva 1/3: 1/3 · 4 · 3 = 4."), "b": t("That is only the cylinder. Add the cone.", "Ese es solo el cilindro. Falta sumar el cono."), "c": t("You subtracted. The parts are joined: add.", "Restó. Las partes se juntan: se suman.")}, "solution": "20π + 4π = 24π."},
      "C": {"ok": "b", "hints": {"a": t("The hole: π · 2² · 5 = 20π.", "El hueco: π · 2² · 5 = 20π."), "c": t("The hole takes material away: subtract.", "El hueco quita material: se resta."), "d": t("The block has no π: 10 · 10 · 5 = 500.", "El bloque no lleva π: 10 · 10 · 5 = 500.")}, "solution": "500 − 20π."},
      "D": {"ok": "a", "hints": {"b": t("The two half-spheres make a whole sphere: 36π, not 18π.", "Las dos semiesferas forman una esfera entera: 36π, no 18π."), "c": t("That is only the cylinder.", "Ese es solo el cilindro."), "d": t("The sphere is 4/3 · 27 = 36, so 36π.", "La esfera es 4/3 · 27 = 36, o sea 36π.")}, "solution": "90π + 36π = 126π."},
      "E": {"ok": "d", "hints": {"a": t("2 · 4 · 10 = 80, not 160.", "2 · 4 · 10 = 80, no 160."), "b": t("You left out the 2 or the radius.", "Olvidó el 2 o el radio."), "c": t("That uses r², which is for the circles, not the side.", "Eso usa r², que es para los círculos, no para el lado.")}, "solution": "2π · 4 · 10 = 80π."},
      "F": {"ok": "b", "hints": {"a": t("The cone has no 2: πrℓ.", "El cono no lleva 2: πrℓ."), "c": t("π · 6 · 10 = 60π.", "π · 6 · 10 = 60π."), "d": t("Do not square anything: πrℓ.", "No se eleva nada al cuadrado: πrℓ.")}, "solution": "π · 6 · 10 = 60π."},
      "G": {"ok": "a", "hints": {"b": t("You left out the 2: 2πrh.", "Olvidó el 2: 2πrh."), "c": t("2 · 5 · 4 = 40, not 80.", "2 · 5 · 4 = 40, no 80."), "d": t("That uses r²: the side is 2πrh.", "Eso usa r²: el lado es 2πrh.")}, "solution": "2π · 5 · 4 = 40π."},
      "H": {"ok": "c", "hints": {"a": t("You left out the 1/3.", "Olvidó el 1/3."), "b": t("Square the radius: 3² = 9.", "Eleve el radio al cuadrado: 3² = 9."), "d": t("Only the radius is squared, and divide by 3.", "Solo el radio va al cuadrado, y se divide entre 3.")}, "solution": "1/3 · 9 · 8 = 24: 24π."},
     }}

    quiz = [
     ("A", t("A cylinder with radius 3 and height 10 has a half-sphere with radius 3 on top. What is the total volume?", "Un cilindro de radio 3 y altura 10 tiene encima una semiesfera de radio 3. ¿Cuál es el volumen total?"), [("a", "90π"), ("b", "126π"), ("c", "108π"), ("d", "72π")]),
     ("B", t("A cylinder with radius 2 and height 5 has a cone with radius 2 and height 3 on top. What is the total volume?", "Un cilindro de radio 2 y altura 5 tiene encima un cono de radio 2 y altura 3. ¿Cuál es el volumen total?"), [("a", "28π"), ("b", "20π"), ("c", "16π"), ("d", "24π")]),
     ("C", t("A 10 × 10 × 5 block has a cylinder with radius 2 and height 5 drilled out. What volume is left?", "A un bloque de 10 × 10 × 5 se le perfora un cilindro de radio 2 y altura 5. ¿Qué volumen queda?"), [("a", "500 − 100π"), ("b", "500 − 20π"), ("c", "500 + 20π"), ("d", "480π")]),
     ("D", t("A capsule: a cylinder with radius 3 and height 10 with a half-sphere of radius 3 at each end. What is the total volume?", "Una cápsula: un cilindro de radio 3 y altura 10 con una semiesfera de radio 3 en cada extremo. ¿Cuál es el volumen total?"), [("a", "126π"), ("b", "108π"), ("c", "90π"), ("d", "162π")]),
     ("E", t("What is the lateral area of a cylinder with radius 4 and height 10?", "¿Cuál es el área lateral de un cilindro de radio 4 y altura 10?"), [("a", "160π"), ("b", "40π"), ("c", "100π"), ("d", "80π")]),
     ("F", t("What is the lateral area of a cone with radius 6 and slant height 10?", "¿Cuál es el área lateral de un cono de radio 6 y altura inclinada 10?"), [("a", "120π"), ("b", "60π"), ("c", "30π"), ("d", "360π")]),
     ("G", t("How much area does the paint cover on the side of a round tank with radius 5 and height 4?", "¿Cuánta superficie cubre la pintura en el lado de un tanque cilíndrico de radio 5 y altura 4?"), [("a", "40π"), ("b", "20π"), ("c", "80π"), ("d", "100π")]),
     ("H", t("What is the volume of an ice cream cone with radius 3 and height 8?", "¿Cuál es el volumen de un cono de helado de radio 3 y altura 8?"), [("a", "72π"), ("b", "8π"), ("c", "24π"), ("d", "216π")])]

    tarea = (t("For your own work, with a notebook, the formula sheet, and a calculator: (1) Three composite figures that you draw. Break each one into parts, write the volume of each part, and add them (or subtract, if there is a hole). (2) A silo made of a cylinder with radius 10 feet and height 30 feet, with a cone 8 feet tall on top. Find the volume of the cylinder and of the cone separately, then the total. (3) A medicine capsule: a cylinder with radius 0.2 inch and length 0.8 inch, with a half-sphere at each end. Find its volume and explain why the two half-spheres make a whole sphere. (4) Painting the silo: find the lateral area of the cylinder (2πrh) and decide whether to include the top and the bottom. If a gallon of paint covers 350 square feet, how many gallons do you need? (5) Four surface areas of different solids (prism, cylinder, cone, or sphere), using the formula sheet. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, la hoja de fórmulas y la calculadora: (1) Tres figuras compuestas dibujadas por usted. Descomponga cada una, anote el volumen de cada parte y súmelos (o réstelos, si hay un hueco). (2) Un silo formado por un cilindro de 10 pies de radio y 30 pies de altura con un cono de 8 pies de altura encima. Calcule por separado el volumen del cilindro y el del cono, y luego el total. (3) Una cápsula de medicina: un cilindro de 0.2 pulgadas de radio y 0.8 pulgadas de largo con una semiesfera en cada extremo. Calcule su volumen y explique por qué las dos semiesferas forman una esfera completa. (4) La pintura del silo: calcule el área lateral del cilindro (2πrh) y decida si debe incluir la tapa y la base. Si un galón de pintura cubre 350 pies cuadrados, ¿cuántos galones hacen falta? (5) Cuatro áreas de superficie de sólidos distintos (prisma, cilindro, cono o esfera), usando la hoja de fórmulas. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Take two boxes or cans from your kitchen that hold about the same amount (a cereal box and a shorter, wider box, for example). Measure them in inches, find the volume and the surface area of each one, and decide which design uses less cardboard or metal. Why do you think the company chose its shape?",
               "Tome de su cocina dos cajas o latas que guarden más o menos lo mismo (una caja de cereal y otra más baja y ancha, por ejemplo). Mídalas en pulgadas, calcule el volumen y el área de superficie de cada una y decida qué diseño usa menos cartón o metal. ¿Por qué cree que la compañía eligió esa forma?"))

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("Break 3D figures into simple solids to find their volume, find the surface area of cylinders and cones, and compare designs that hold the same volume.", "Descomponga figuras 3D en sólidos simples para hallar su volumen, calcule el área de superficie de cilindros y conos y compare diseños que guardan el mismo volumen."),
        ("📐", t("Formula sheet and calculator", "Hoja de fórmulas y calculadora")),
        [t("<strong>Break</strong> a composite 3D figure into simple solids.", "<strong>Descomponer</strong> una figura 3D compuesta en sólidos simples."),
         t("<strong>Find</strong> the volume of composite figures by adding or subtracting volumes.", "<strong>Calcular</strong> el volumen de figuras compuestas sumando o restando volúmenes."),
         t("<strong>Find</strong> the lateral and total surface area of cylinders, cones, and other solids.", "<strong>Calcular</strong> el área de superficie lateral y total de cilindros, conos y otros sólidos."),
         t("<strong>Compare</strong> designs with the same volume by how much material they use.", "<strong>Comparar</strong> diseños del mismo volumen según el material que usan.")],
        secciones, tarea, quiz,
        t("Self-check checklist for composite figures and surface area", "Lista de autoevaluación de figuras compuestas y área de superficie"),
        t("Self-check checklist: skills for composite figures and surface area", "Lista de autoevaluación: destrezas de figuras compuestas y área de superficie"),
        [(t("Breaking the figure apart", "Descomponer la figura"), t("I break the figure into its parts and choose to add or subtract.", "Descompongo la figura en sus partes y elijo sumar o restar."), t("I find some parts but leave one out or count one twice.", "Identifico algunas partes, pero omito o duplico alguna."), t("I do not find the simple parts.", "No identifico las partes simples.")),
         (t("Finding the total volume", "Calcular el volumen total"), t("I add or subtract the parts correctly and check that the total makes sense.", "Sumo o resto las partes correctamente y compruebo que el total tenga sentido."), t("I find the parts but add or subtract them wrong.", "Calculo las partes, pero las sumo o resto mal."), t("I find the volumes of the parts wrong.", "Calculo mal los volúmenes de las partes.")),
         (t("Surface area", "Área de superficie"), t("I use the right lateral or total formula and apply it to a material or cost problem.", "Uso la fórmula lateral o total correcta y la aplico a un problema de material o costo."), t("I use the formula but mix up the height and the slant height.", "Uso la fórmula, pero confundo la altura con la altura inclinada."), t("I do not find the right formula.", "No identifico la fórmula adecuada."))],
        t("<p>In this lesson you learned to <strong>break</strong> composite 3D figures into parts to find their volume by <strong>adding or subtracting</strong> simple parts, to find the <strong>surface area</strong> of cylinders, cones, and other solids, and to compare how much material different designs with the same volume use.</p>\n<p>This closes the geometry of space. <strong>Lesson 2.3 · Polynomials: types, adding, subtracting, and multiplying</strong> opens the door to higher algebra. You will see that combining like terms (such as 3x² + 5x²) is the same idea of “putting together what is alike” that you already use to simplify, and that polynomials let you write geometric measures in general form.</p>",
          "<p>En esta lección se aprendió a <strong>descomponer</strong> figuras 3D compuestas para hallar su volumen <strong>sumando o restando</strong> partes simples, a calcular el <strong>área de superficie</strong> de cilindros, conos y otros sólidos, y a comparar el material que usan distintos diseños del mismo volumen.</p>\n<p>Con esto se cierra la geometría del espacio. La <strong>Lección 2.3 · Polinomios: clasificación, suma, resta y multiplicación básica</strong> abre la puerta del álgebra superior. Se verá que combinar términos semejantes (como 3x² + 5x²) es la misma idea de «juntar lo parecido» que ya se usa al simplificar, y que los polinomios permiten expresar medidas geométricas de forma general.</p>"),
        ("2-3", ("", t("Lesson 2.3 · Polynomials: types, adding, subtracting, and multiplying", "Lección 2.3 · Polinomios: clasificación, suma, resta y multiplicación básica"))),
        [(t("composite figure", "figura compuesta"), t("A solid made of simple solids joined together or with one taken out.", "Un sólido formado por sólidos simples unidos o con uno quitado.")),
         (t("half-sphere (hemisphere)", "semiesfera"), t("Half of a sphere: its volume is 1/2 · 4/3 πr³ = 2/3 πr³.", "La mitad de una esfera: su volumen es 1/2 · 4/3 πr³ = 2/3 πr³.")),
         (t("surface area", "área de superficie"), t("The sum of the areas of all the surfaces of a solid.", "La suma de las áreas de todas las superficies de un sólido.")),
         (t("lateral area", "área lateral"), t("The surface area without the bases.", "El área de superficie sin las bases.")),
         (t("slant height (ℓ)", "altura inclinada (ℓ)"), t("In a cone or pyramid, the distance along the surface from the edge of the base to the point.", "En un cono o una pirámide, la distancia por la superficie del borde de la base a la punta."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function F(n, d){ return fr(n, d === undefined ? 1 : d); }
var COL = {cil: "#bbdefb", cono: "#ffe0b2", semi: "#c8e6c9", pri: "#d1c4e9", pir: "#ffe0b2", hueco: "#ffcdd2"};
var NOMP = {cil: T("Cylinder", "Cilindro"), cono: T("Cone", "Cono"), semi: T("Half-sphere", "Semiesfera"), esf: T("Whole sphere", "Esfera completa"), pri: T("Rectangular prism", "Prisma rectangular"), pir: T("Pyramid", "Pirámide")};
var FIG = {
  silo: {nom: T("Silo (cylinder + cone)", "Silo (cilindro + cono)"), partes: ["cil", "cono"], op: "+", dims: [["r", T("Radius r", "Radio r"), 1, 6, 3], ["h", T("Height of the cylinder h", "Altura del cilindro h"), 2, 12, 8], ["k", T("Height of the cone", "Altura del cono"), 1, 8, 3]]},
  tanque: {nom: T("Tank (cylinder + half-sphere)", "Tanque (cilindro + semiesfera)"), partes: ["cil", "semi"], op: "+", dims: [["r", T("Radius r", "Radio r"), 1, 6, 3], ["h", T("Height of the cylinder h", "Altura del cilindro h"), 2, 12, 10]]},
  capsula: {nom: T("Capsule (cylinder + 2 half-spheres)", "Cápsula (cilindro + 2 semiesferas)"), partes: ["cil", "semi"], op: "+", dos: true, dims: [["r", T("Radius r", "Radio r"), 1, 5, 2], ["h", T("Length of the cylinder h", "Largo del cilindro h"), 2, 12, 8]]},
  torre: {nom: T("Tower (prism + pyramid)", "Torre (prisma + pirámide)"), partes: ["pri", "pir"], op: "+", dims: [["a", T("Side of the base", "Lado de la base"), 1, 8, 4], ["h", T("Height of the prism", "Altura del prisma"), 2, 12, 8], ["k", T("Height of the pyramid", "Altura de la pirámide"), 1, 9, 3]]},
  bloque: {nom: T("Drilled block (prism − cylinder)", "Bloque perforado (prisma − cilindro)"), partes: ["pri", "cil"], op: "−", dims: [["a", T("Length", "Largo"), 4, 14, 10], ["b", T("Width", "Ancho"), 4, 14, 10], ["h", T("Height", "Alto"), 2, 10, 5], ["r", T("Radius of the hole", "Radio del hueco"), 1, 3, 2]]}};
/* Composite figure drawing; sep = draw the parts apart */
function figSVG(f, d, sep, colorear){
  var W = 420, H = 380, s = "", cx = 210, g = sep ? 44 : 0, c = function(k){ return colorear === false ? "#eceff1" : COL[k]; };
  function cil(cx0, base, R, h, col){ return '<path d="M' + f1(cx0 - R) + " " + f1(base - h) + " L" + f1(cx0 - R) + " " + f1(base) + " A" + f1(R) + " " + f1(R * .25) + " 0 0 0 " + f1(cx0 + R) + " " + f1(base) + " L" + f1(cx0 + R) + " " + f1(base - h) + '" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5"/>' + elip(cx0, base - h, R, R * .25, col) + elip(cx0, base, R, R * .25, "none", S4.oculto, "atras"); }
  function cono(cx0, base, R, h, col){ return '<path d="M' + f1(cx0 - R) + " " + f1(base) + " L" + f1(cx0) + " " + f1(base - h) + " L" + f1(cx0 + R) + " " + f1(base) + " A" + f1(R) + " " + f1(R * .25) + " 0 0 1 " + f1(cx0 - R) + " " + f1(base) + 'Z" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5"/>'; }
  function semi(cx0, base, R, arriba, col){ return '<path d="M' + f1(cx0 - R) + " " + f1(base) + " A" + f1(R) + " " + f1(R) + " 0 0 " + (arriba ? 1 : 0) + " " + f1(cx0 + R) + " " + f1(base) + " A" + f1(R) + " " + f1(R * .25) + " 0 0 " + (arriba ? 0 : 1) + " " + f1(cx0 - R) + " " + f1(base) + 'Z" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5"/>'; }
  function caja(x0, y0, w, dep, h, col){ var A = [x0, y0], B = [x0 + w, y0], C = [x0 + w + dep * .8, y0 - dep * .55], D = [x0 + dep * .8, y0 - dep * .55], up = function(p){ return [p[0], p[1] - h]; }, P = function(l){ return l.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" "); };
    return '<polygon points="' + P([A, B, up(B), up(A)]) + '" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5"/><polygon points="' + P([B, C, up(C), up(B)]) + '" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5" fill-opacity=".8"/><polygon points="' + P([up(A), up(B), up(C), up(D)]) + '" fill="' + col + '" stroke="' + S4.linea + '" stroke-width="2.5" fill-opacity=".6"/>'; }
  if (f === "silo" || f === "tanque" || f === "capsula"){
    var tot = (f === "silo" ? d.h + d.k : (f === "tanque" ? d.h + d.r : d.h + 2 * d.r)), esc = Math.min(28, 300 / tot, 130 / d.r), R = d.r * esc, h = d.h * esc, base = 345 - (f === "capsula" ? R : 0);
    if (f === "capsula") s += semi(cx, base + g, R, false, c("semi"));
    s += cil(cx, base, R, h, c("cil"));
    if (f === "silo") s += cono(cx, base - h - g, R, d.k * esc, c("cono"));
    else s += semi(cx, base - h - g, R, true, c("semi"));
    s += lin(cx, base - h / 2, cx + R, base - h / 2, S4.radio, 3) + '<circle cx="' + cx + '" cy="' + f1(base - h / 2) + '" r="3.5" fill="' + S4.radio + '"/>' + etq(cx + R / 2, base - h / 2 - 9, "r = " + d.r, S4.radio) + lin(cx + R + 18, base, cx + R + 18, base - h, S4.alto, 2.5, "6 4") + etq(cx + R + 24, base - h / 2, "h = " + d.h, S4.alto, "start");
    if (f === "silo") s += lin(cx + R + 18, base - h - g, cx + R + 18, base - h - g - d.k * esc, "#e65100", 2.5, "6 4") + etq(cx + R + 24, base - h - g - d.k * esc / 2 + 5, "h = " + d.k, "#e65100", "start");
  } else if (f === "torre"){
    var tot2 = d.h + d.k, e2 = Math.min(26, 290 / tot2, 200 / (d.a * 1.6)), w = d.a * e2, dep = d.a * e2 * .7, x0 = 210 - (w + dep * .8) / 2, y0 = 350, hh = d.h * e2, kk = d.k * e2;
    s += caja(x0, y0, w, dep, hh, c("pri"));
    var A = [x0, y0 - hh - g], B = [x0 + w, y0 - hh - g], C = [x0 + w + dep * .8, y0 - hh - g - dep * .55], cen = [x0 + (w + dep * .8) / 2, y0 - hh - g - dep * .275], V = [cen[0], cen[1] - kk];
    s += '<polygon points="' + [A, B, V].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="' + c("pir") + '" stroke="' + S4.linea + '" stroke-width="2.5"/><polygon points="' + [B, C, V].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="' + c("pir") + '" fill-opacity=".8" stroke="' + S4.linea + '" stroke-width="2.5"/>';
    s += etq(x0 + w / 2, y0 + 22, d.a, S4.base) + etq(x0 - 10, y0 - hh / 2, "h = " + d.h, S4.alto, "end") + etq(V[0] + 12, V[1] + kk / 2, T("pyramid h = ", "h de la pirámide = ") + d.k, "#e65100", "start");
  } else {
    var e3 = Math.min(22, 230 / (d.a + d.b * .8), 200 / d.h), w3 = d.a * e3, dp = d.b * e3, x3 = 210 - (w3 + dp * .8) / 2, y3 = 330, h3 = d.h * e3, R3 = d.r * e3, ccx = x3 + (w3 + dp * .8) / 2, ccy = y3 - h3 - dp * .275;
    s += caja(x3, y3, w3, dp, h3, c("pri"));
    s += elip(ccx, ccy, R3, R3 * .5, colorear === false ? "#fff" : COL.hueco) + lin(ccx, ccy, ccx + R3, ccy, S4.radio, 3) + etq(ccx + R3 / 2, ccy - 8, "r = " + d.r, S4.radio);
    if (sep) s += cil(370, 330, R3, h3, COL.hueco);
    s += etq(x3 + w3 / 2, y3 + 22, d.a, S4.base) + etq(x3 + w3 + dp * .4 + 14, y3 - dp * .3, d.b, S4.base, "start") + etq(x3 - 10, y3 - h3 / 2, d.h, S4.alto, "end");
  }
  return marco(W, H, FIG[f].nom + ". " + T("Measures: ", "Medidas: ") + Object.keys(d).map(function(k){ return k + " = " + d[k]; }).join(", ") + ".", s, 400);
}
/* Partial volumes: [{part, formula, sub, k (coef of π) or n (plain number)}] */
function partes(f, d){
  var l = [];
  if (f === "silo" || f === "tanque" || f === "capsula") l.push({p: "cil", form: "πr²h", sub: "π · " + d.r + "² · " + d.h, k: F(d.r * d.r * d.h), n: 0});
  if (f === "silo") l.push({p: "cono", form: "1/3 πr²h", sub: "1/3 · π · " + d.r + "² · " + d.k, k: F(d.r * d.r * d.k, 3), n: 0});
  if (f === "tanque") l.push({p: "semi", form: "1/2 · 4/3 πr³", sub: "2/3 · π · " + d.r + "³", k: F(2 * d.r * d.r * d.r, 3), n: 0});
  if (f === "capsula") l.push({p: "esf", form: "2 · (1/2 · 4/3 πr³)", sub: "4/3 · π · " + d.r + "³", k: F(4 * d.r * d.r * d.r, 3), n: 0});
  if (f === "torre"){ l.push({p: "pri", form: "Bh", sub: d.a + " · " + d.a + " · " + d.h, k: F(0), n: d.a * d.a * d.h}); l.push({p: "pir", form: "1/3 Bh", sub: "1/3 · " + d.a * d.a + " · " + d.k, k: F(0), n: d.a * d.a * d.k / 3}); }
  if (f === "bloque"){ l.push({p: "pri", form: "L · w · h", sub: d.a + " · " + d.b + " · " + d.h, k: F(0), n: d.a * d.b * d.h}); l.push({p: "cil", form: "πr²h", sub: "π · " + d.r + "² · " + d.h, k: F(-d.r * d.r * d.h), n: 0, resta: true}); }
  return l;
}
function totalTxt(l){
  var n = l.reduce(function(a, x){ return a + x.n; }, 0), k = l.reduce(function(a, x){ return fsum(a, x.k); }, F(0));
  var s = (n ? n1(n, 2) : "") + (k.n ? (n ? (k.n < 0 ? " − " : " + ") + piTxt(F(Math.abs(k.n), k.d)) : piTxt(k)) : "");
  return {txt: s, val: n + piVal(k)};
}
function parteTxt(x){ return x.n ? n1(x.n, 2) : piTxt(F(Math.abs(x.k.n), x.k.d)); }

/* ===== MODULE 1 · Decompose ===== */
function dcPinta(){
  var f = $("dc-fig").value, d = {}; FIG[f].dims.forEach(function(x){ d[x[0]] = x[4]; });
  $("dc-svg").innerHTML = figSVG(f, d, false, false); $("dc-fb").className = "fb"; $("dc-fb").innerHTML = "";
  document.querySelectorAll("#dc-piezas input").forEach(function(i){ i.checked = false; }); $("dc-mas").checked = false; $("dc-menos").checked = false;
}
$("dc-fig").addEventListener("change", dcPinta);
function dcRespuesta(f){ var p = FIG[f].partes.slice(); if (FIG[f].dos){ p = ["cil", "semi"]; } return p; }
$("dc-comprobar").addEventListener("click", function(){
  var f = $("dc-fig").value, sel = [].filter.call(document.querySelectorAll("#dc-piezas input"), function(i){ return i.checked; }).map(function(i){ return i.value; }), ok = dcRespuesta(f), op = $("dc-mas").checked ? "+" : ($("dc-menos").checked ? "−" : null), fb = $("dc-fb");
  var piezasOk = sel.length === ok.length && ok.every(function(p){ return sel.indexOf(p) >= 0; }) || (f === "capsula" && sel.length === 2 && sel.indexOf("cil") >= 0 && (sel.indexOf("semi") >= 0 || sel.indexOf("esf") >= 0));
  if (piezasOk && op === FIG[f].op){ fb.className = "fb bien"; fb.innerHTML = TX.bien + ok.map(function(p){ return NOMP[p]; }).join(FIG[f].op === "+" ? " + " : " − ") + (f === "capsula" ? T(" (the two half-spheres together make one whole sphere).", " (las dos semiesferas juntas forman una esfera completa).") : ".");
    var d = {}; FIG[f].dims.forEach(function(x){ d[x[0]] = x[4]; }); $("dc-svg").innerHTML = figSVG(f, d, true, true); return; }
  fb.className = "fb pista"; fb.innerHTML = TX.todavia + (!piezasOk ? T("Check the pieces: look for each simple solid (a round body, a point, a dome, a box).", "Revise las piezas: busque cada sólido simple (un cuerpo redondo, una punta, una cúpula, una caja).") : "") + (op !== FIG[f].op ? " " + T("Think again about the operation: is a part joined on, or taken out?", "Piense otra vez la operación: ¿una parte se añade o se quita?") : "");
});
$("dc-ver").addEventListener("click", function(){ var f = $("dc-fig").value, d = {}; FIG[f].dims.forEach(function(x){ d[x[0]] = x[4]; }); $("dc-svg").innerHTML = figSVG(f, d, true, true); $("dc-fb").className = "fb mal"; $("dc-fb").innerHTML = TX.asi + dcRespuesta(f).map(function(p){ return NOMP[p]; }).join(FIG[f].op === "+" ? " + " : " − ") + "."; });
$("dc-limpia").addEventListener("click", dcPinta);
dcPinta();
OMR("dq", function(){
  var f = elige(Object.keys(FIG)), ok = dcRespuesta(f).map(function(p){ return NOMP[p]; }).join(" " + FIG[f].op + " "), d = {}; FIG[f].dims.forEach(function(x){ d[x[0]] = x[4]; });
  var malos = [dcRespuesta(f).map(function(p){ return NOMP[p]; }).join(FIG[f].op === "+" ? " − " : " + "), NOMP.cil + " + " + NOMP.esf, NOMP.pri + " + " + NOMP.cil, NOMP.cil + " + " + NOMP.cono, NOMP.pri + " − " + NOMP.pir];
  var ops = [{clave: "ok", html: ok}], vistos = {}; vistos[ok] = 1;
  baraja(malos).forEach(function(m){ if (!vistos[m] && ops.length < 4){ vistos[m] = 1; ops.push({clave: m, html: m}); } });
  return {enun: T("Which simple solids make up this figure, and are their volumes added or subtracted?", "¿Qué sólidos simples forman esta figura y sus volúmenes se suman o se restan?") + figSVG(f, d, false, false).replace('max-width:400px', 'max-width:260px'),
    correcta: "ok", opciones: ops, pista: T("Name each part, then ask: is it joined on (add) or taken out (subtract)?", "Nombre cada parte y pregúntese: ¿se añade (suma) o se quita (resta)?"), bien: ok + "."};
});

/* ===== MODULE 2 · Composite volume workshop ===== */
var CV = {d: {}};
function cvCampos(){
  var f = $("cv-fig").value;
  $("cv-dims").innerHTML = FIG[f].dims.map(function(x){ return '<div class="campo" style="flex:1;min-width:180px;"><label for="cv-' + x[0] + '">' + x[1] + ' = <span id="cv-' + x[0] + 'v"></span></label><input type="range" id="cv-' + x[0] + '" min="' + x[2] + '" max="' + x[3] + '" step="1" value="' + x[4] + '"></div>'; }).join("");
  FIG[f].dims.forEach(function(x){ $("cv-" + x[0]).addEventListener("input", cvPinta); });
  cvPinta();
}
function cvPinta(){
  var f = $("cv-fig").value, d = {}, u = UNID[$("cv-u").value];
  FIG[f].dims.forEach(function(x){ d[x[0]] = +$("cv-" + x[0]).value; $("cv-" + x[0] + "v").textContent = d[x[0]]; });
  if (f === "bloque" && 2 * d.r >= Math.min(d.a, d.b)){ d.r = Math.max(1, Math.floor((Math.min(d.a, d.b) - 1) / 2)); $("cv-r").value = d.r; $("cv-rv").textContent = d.r; }
  $("cv-svg").innerHTML = figSVG(f, d, $("cv-sep").checked, true);
  var l = partes(f, d), tot = totalTxt(l);
  $("cv-tabla").innerHTML = '<caption class="sr-only">' + T("Volume of each part and total volume of the composite figure", "Volumen de cada parte y volumen total de la figura compuesta") + '</caption><thead><tr><th scope="col">' + T("Part", "Parte") + '</th><th scope="col">' + T("Formula", "Fórmula") + '</th><th scope="col">' + T("Substitution", "Sustitución") + '</th><th scope="col">' + T("Volume", "Volumen") + "</th></tr></thead><tbody>" +
    l.map(function(x){ return '<tr><td><span style="display:inline-block;width:14px;height:14px;border-radius:3px;background:' + (COL[x.p] || COL.semi) + ';border:1px solid #607d8b;margin-right:6px;vertical-align:middle"></span>' + NOMP[x.p] + (x.resta ? T(" (hole)", " (hueco)") : "") + "</td><td>" + x.form + "</td><td>" + x.sub + "</td><td>" + (x.resta ? "− " : "") + parteTxt(x) + "</td></tr>"; }).join("") +
    '<tr class="fila-activa"><td colspan="3"><strong>' + T("Total", "Total") + " (" + (FIG[f].op === "+" ? T("add", "se suman") : T("subtract", "se resta")) + ")</strong></td><td><strong>" + tot.txt + " ≈ " + n1(tot.val) + " " + u[2] + "</strong></td></tr></tbody>";
}
$("cv-fig").addEventListener("change", cvCampos); $("cv-u").addEventListener("change", cvPinta); $("cv-sep").addEventListener("change", cvPinta);
cvCampos();
creaPracticaLibre("cq", function(){
  var f = elige(Object.keys(FIG)), d = {}, u = UNID[elige(["in", "ft"])];
  FIG[f].dims.forEach(function(x){ d[x[0]] = aleatorio(x[2], Math.min(x[3], x[2] + 6)); });
  if (f === "silo" || f === "torre"){ d.k = 3 * aleatorio(1, 3); }
  if (f === "bloque"){ d.r = Math.min(d.r, Math.floor((Math.min(d.a, d.b) - 1) / 2)) || 1; }
  var l = partes(f, d), tot = totalTxt(l), conPi = l.some(function(x){ return x.k.n; }), soloPi = l.every(function(x){ return x.n === 0; });
  var desc = {silo: T("A silo: a cylinder with radius " + d.r + " and height " + d.h + ", with a cone of height " + d.k + " on top.", "Un silo: un cilindro de radio " + d.r + " y altura " + d.h + ", con un cono de altura " + d.k + " encima."),
    tanque: T("A tank: a cylinder with radius " + d.r + " and height " + d.h + ", with a half-sphere on top.", "Un tanque: un cilindro de radio " + d.r + " y altura " + d.h + ", con una semiesfera encima."),
    capsula: T("A capsule: a cylinder with radius " + d.r + " and length " + d.h + ", with a half-sphere at each end.", "Una cápsula: un cilindro de radio " + d.r + " y largo " + d.h + ", con una semiesfera en cada extremo."),
    torre: T("A tower: a prism with a square base " + d.a + " on each side and height " + d.h + ", with a pyramid of height " + d.k + " on top.", "Una torre: un prisma de base cuadrada de lado " + d.a + " y altura " + d.h + ", con una pirámide de altura " + d.k + " encima."),
    bloque: T("A block " + d.a + " × " + d.b + " × " + d.h + " with a hole of radius " + d.r + " drilled straight through its height.", "Un bloque de " + d.a + " × " + d.b + " × " + d.h + " con un agujero de radio " + d.r + " que lo atraviesa de arriba abajo.")}[f];
  $("cq-svg").innerHTML = figSVG(f, d, false, true).replace("max-width:400px", "max-width:300px");
  return {enun: desc + " " + T("Find the total volume (measures in ", "Calcule el volumen total (medidas en ") + u[1] + ")." + (soloPi ? T(" Give it with π or as a decimal.", " Escríbalo con π o en decimal.") : T(" Give it as a decimal, rounded to the tenth.", " Escríbalo en decimal, redondeado a la décima.")),
    evalua: function(txt){
      if (soloPi){ var k = l.reduce(function(a, x){ return fsum(a, x.k); }, F(0)), r = evaluaPi(txt, k, l.map(function(x){ return {k: fval(x.k), msg: T("That is only one part. Add the other one.", "Esa es solo una parte. Falta la otra.")}; }));
        if (f === "capsula" && r.estado === "mal"){ var x = leePi(txt); if (x && Math.abs((x.pi !== null ? x.pi : x.val / Math.PI) - (d.r * d.r * d.h + 2 * d.r * d.r * d.r / 3)) < .02 * d.r * d.r * d.h) r.msg = T("There are two half-spheres: together they make a whole sphere.", "Hay dos semiesferas: juntas forman una esfera completa."); }
        return r; }
      var m = String(txt).replace(/\s/g, "").replace(/[−–]/g, "-").match(/^(\d+(?:\.\d+)?)([-+])(\d+(?:\.\d+)?)π$/);
      if (m){ var v = +m[1] + (m[2] === "-" ? -1 : 1) * +m[3] * Math.PI; if (Math.abs(v - tot.val) < 0.01) return {estado: "bien"}; }
      var parc = l.map(function(x){ return {v: Math.abs(x.n + piVal(x.k)), msg: T("That is only one part. Combine it with the other.", "Esa es solo una parte. Combínela con la otra.")}; });
      if (f === "bloque") parc.push({v: l[0].n + Math.abs(piVal(l[1].k)), msg: T("The hole takes material away: subtract it.", "El hueco quita material: se resta.")});
      return evaluaNum(txt, tot.val, Math.max(0.051, tot.val * 0.002), parc.map(function(p){ return {v: p.v, msg: p.msg}; }).filter(function(p){ return Math.abs(p.v - tot.val) > 0.06; }).map(function(p){ return {v: Math.round(p.v * 10) / 10, msg: p.msg}; }));
    },
    solucion: l.map(function(x){ return NOMP[x.p] + ": " + x.sub + " = " + parteTxt(x); }).join("; ") + ". " + T("Total: ", "Total: ") + tot.txt + " ≈ " + n1(tot.val) + " " + u[2] + "."};
});

/* ===== MODULE 3 · Surface area and the net ===== */
var SUP = {s: "prisma", modo: "total", sel: null};
function piezasDe(s, d){
  if (s === "prisma") return [["base", T("Bottom", "Base"), d.a * d.b, d.a + " · " + d.b, 0], ["tapa", T("Top", "Tapa"), d.a * d.b, d.a + " · " + d.b, 0], ["f1", T("Front", "Frente"), d.a * d.c, d.a + " · " + d.c, 1], ["f2", T("Back", "Atrás"), d.a * d.c, d.a + " · " + d.c, 1], ["f3", T("Left side", "Lado izquierdo"), d.b * d.c, d.b + " · " + d.c, 1], ["f4", T("Right side", "Lado derecho"), d.b * d.c, d.b + " · " + d.c, 1]];
  if (s === "cilindro") return [["base", T("Bottom circle", "Círculo de la base"), F(d.r * d.r), "π · " + d.r + "²", 0], ["tapa", T("Top circle", "Círculo de la tapa"), F(d.r * d.r), "π · " + d.r + "²", 0], ["lat", T("Side (a rectangle when unrolled)", "Lado (un rectángulo al desenrollarlo)"), F(2 * d.r * d.c), "2π · " + d.r + " · " + d.c, 1]];
  if (s === "cono") return [["base", T("Base circle", "Círculo de la base"), F(d.r * d.r), "π · " + d.r + "²", 0], ["lat", T("Side (a fan shape when unrolled)", "Lado (un abanico al desenrollarlo)"), F(d.r * d.l), "π · " + d.r + " · " + d.l, 1]];
  if (s === "piramide") return [["base", T("Square base", "Base cuadrada"), d.a * d.a, d.a + " · " + d.a, 0]].concat([1, 2, 3, 4].map(function(i){ return ["t" + i, T("Triangle ", "Triángulo ") + i, d.a * d.l / 2, "1/2 · " + d.a + " · " + d.l, 1]; }));
  return [["esf", T("The whole surface", "Toda la superficie"), F(4 * d.r * d.r), "4π · " + d.r + "²", 1]];
}
var SDIM = {prisma: [["a", T("Length", "Largo"), 4], ["b", T("Width", "Ancho"), 3], ["c", T("Height", "Alto"), 2]], cilindro: [["r", T("Radius", "Radio"), 2], ["c", T("Height", "Altura"), 5]], cono: [["r", T("Radius", "Radio"), 3], ["l", T("Slant height ℓ", "Altura inclinada ℓ"), 5]], piramide: [["a", T("Side of the base", "Lado de la base"), 4], ["l", T("Slant height ℓ of a face", "Altura inclinada ℓ de una cara"), 5]], esfera: [["r", T("Radius", "Radio"), 3]]};
function areaTxt(v){ return typeof v === "object" ? piTxt(v) : n1(v, 2); }
function supCampos(){ var s = $("su-sol").value; SUP.s = s; SUP.sel = null;
  $("su-dims").innerHTML = SDIM[s].map(function(x){ return '<div class="campo"><label for="su-' + x[0] + '">' + x[1] + '</label><input type="number" class="corto" id="su-' + x[0] + '" min="1" max="12" value="' + x[2] + '"></div>'; }).join("");
  SDIM[s].forEach(function(x){ $("su-" + x[0]).addEventListener("input", supPinta); }); supPinta(); }
function redSVG(s, d, pz){
  var on = function(id, lat){ return (SUP.sel ? SUP.sel === id : (SUP.modo === "total" || lat)); }, col = function(id, lat){ return on(id, lat) ? (lat ? "#ffe0b2" : "#bbdefb") : "#f5f5f5"; }, st = function(id, lat){ return on(id, lat) ? S4.linea : "#cfd8dc"; }, r = "";
  var W = 460, H = 330, u;
  function rect(id, x, y, w, h, lat, txt){ return '<rect x="' + f1(x) + '" y="' + f1(y) + '" width="' + f1(w) + '" height="' + f1(h) + '" fill="' + col(id, lat) + '" stroke="' + st(id, lat) + '" stroke-width="2"/>' + (txt ? etq(x + w / 2, y + h / 2 + 5, txt, S4.linea, "middle", 13) : ""); }
  if (s === "prisma"){ u = Math.min(28, 440 / (2 * d.a + 2 * d.b), 300 / (d.b * 2 + d.c)); var a = d.a * u, b = d.b * u, c = d.c * u, x0 = (W - 2 * a - 2 * b) / 2, y0 = (H - c - 2 * b) / 2 + b;
    r += rect("f3", x0, y0, b, c, 1) + rect("f1", x0 + b, y0, a, c, 1, T("front", "frente")) + rect("f4", x0 + a + b, y0, b, c, 1) + rect("f2", x0 + a + 2 * b, y0, a, c, 1, T("back", "atrás")) + rect("tapa", x0 + b, y0 - b, a, b, 0, T("top", "tapa")) + rect("base", x0 + b, y0 + c, a, b, 0, T("bottom", "base")); }
  else if (s === "cilindro"){ u = Math.min(24, 420 / (2 * Math.PI * d.r), 300 / (d.c + 4 * d.r)); var R = d.r * u, Lr = 2 * Math.PI * R, hc = d.c * u, x1 = (W - Lr) / 2, y1 = (H - hc) / 2;
    r += rect("lat", x1, y1, Lr, hc, 1, "2πr × h") + '<circle cx="' + f1(W / 2) + '" cy="' + f1(y1 - R) + '" r="' + f1(R) + '" fill="' + col("tapa", 0) + '" stroke="' + st("tapa", 0) + '" stroke-width="2"/><circle cx="' + f1(W / 2) + '" cy="' + f1(y1 + hc + R) + '" r="' + f1(R) + '" fill="' + col("base", 0) + '" stroke="' + st("base", 0) + '" stroke-width="2"/>'; }
  else if (s === "cono"){ u = Math.min(30, 160 / d.l, 70 / d.r); var Lc = d.l * u, ang = 2 * Math.PI * d.r / d.l, cx = W / 2, cy = 40, a0 = Math.PI / 2 - ang / 2, a1 = Math.PI / 2 + ang / 2, big = ang > Math.PI ? 1 : 0;
    r += '<path d="M' + cx + " " + cy + " L" + f1(cx + Lc * Math.cos(a0)) + " " + f1(cy + Lc * Math.sin(a0)) + " A" + f1(Lc) + " " + f1(Lc) + " 0 " + big + " 1 " + f1(cx + Lc * Math.cos(a1)) + " " + f1(cy + Lc * Math.sin(a1)) + 'Z" fill="' + col("lat", 1) + '" stroke="' + st("lat", 1) + '" stroke-width="2"/>' + etq(cx, cy + Lc * .6, "ℓ = " + d.l, S4.linea, "middle", 13);
    r += '<circle cx="' + cx + '" cy="' + f1(Math.min(H - d.r * u - 6, cy + Lc + d.r * u + 4)) + '" r="' + f1(d.r * u) + '" fill="' + col("base", 0) + '" stroke="' + st("base", 0) + '" stroke-width="2"/>'; }
  else if (s === "piramide"){ u = Math.min(24, 300 / (d.a + 2 * d.l)); var A = d.a * u, Lp = d.l * u, x2 = (W - A) / 2, y2 = (H - A) / 2, P = function(l){ return l.map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" "); };
    r += rect("base", x2, y2, A, A, 0, "L × L");
    [["t1", [[x2, y2], [x2 + A, y2], [x2 + A / 2, y2 - Lp]]], ["t2", [[x2 + A, y2], [x2 + A, y2 + A], [x2 + A + Lp, y2 + A / 2]]], ["t3", [[x2, y2 + A], [x2 + A, y2 + A], [x2 + A / 2, y2 + A + Lp]]], ["t4", [[x2, y2], [x2, y2 + A], [x2 - Lp, y2 + A / 2]]]].forEach(function(q){ r += '<polygon points="' + P(q[1]) + '" fill="' + col(q[0], 1) + '" stroke="' + st(q[0], 1) + '" stroke-width="2"/>'; }); }
  else { r += '<circle cx="230" cy="165" r="120" fill="' + col("esf", 1) + '" stroke="' + S4.linea + '" stroke-width="2.5"/>' + elip(230, 165, 120, 30, "none", S4.linea, "frente") + etq(230, 175, T("A sphere cannot be laid flat: SA = 4πr²", "La esfera no se puede abrir en el plano: SA = 4πr²"), S4.linea, "middle", 13); }
  return marco(W, H, T("The net of the solid: its surfaces laid out flat. ", "El desarrollo del sólido: sus superficies extendidas en el plano. ") + pz.map(function(p){ return p[1]; }).join(", ") + ".", r, 440);
}
function supPinta(){
  var s = SUP.s, d = {}, u = UNID[$("su-u").value];
  SDIM[s].forEach(function(x){ var v = Math.max(1, Math.min(12, Math.round(+$("su-" + x[0]).value || 1))); d[x[0]] = v; });
  if (s === "cono" && d.l <= d.r){ d.l = d.r + 1; } if (s === "piramide" && d.l * 2 <= d.a){ d.l = Math.floor(d.a / 2) + 1; }
  var pz = piezasDe(s, d);
  var cerr = s === "prisma" ? prismaSVG({L: d.a, b: d.b, h: d.c, esc: 22, voz: T("A closed rectangular prism.", "Un prisma rectangular cerrado.")}) : s === "cilindro" ? cilindroSVG({r: d.r, h: d.c, esc: 22, voz: T("A closed cylinder.", "Un cilindro cerrado.")}) : s === "cono" ? conoSVG({r: d.r, h: Math.sqrt(d.l * d.l - d.r * d.r), esc: 22, voz: T("A closed cone.", "Un cono cerrado.")}).replace(/h = [\d.]+/, "") : s === "piramide" ? piramideSVG({L: d.a, b: d.a, h: Math.sqrt(d.l * d.l - d.a * d.a / 4), esc: 22, cuadrada: true, voz: T("A closed pyramid with a square base.", "Una pirámide cerrada de base cuadrada.")}).replace(/h = [\d.]+/, "") : esferaSVG({r: d.r, voz: T("A sphere.", "Una esfera.")});
  $("su-cerrado").innerHTML = cerr.replace(/max-width:\d+px/, "max-width:300px"); $("su-red").innerHTML = redSVG(s, d, pz);
  var lat = pz.filter(function(p){ return p[4]; }), mostrar = SUP.modo === "total" ? pz : lat;
  $("su-cards").innerHTML = pz.map(function(p){ var on = SUP.sel ? SUP.sel === p[0] : (SUP.modo === "total" || p[4]); return '<button type="button" class="tarjeta pieza" data-id="' + p[0] + '" aria-pressed="' + (SUP.sel === p[0]) + '" style="text-align:left;opacity:' + (on ? 1 : .45) + '"><strong>' + p[1] + (p[4] && SUP.s !== "esfera" ? T(" · lateral", " · lateral") : "") + "</strong>" + p[3] + " = " + areaTxt(p[2]) + "</button>"; }).join("");
  [].forEach.call(document.querySelectorAll("#su-cards .pieza"), function(b){ b.addEventListener("click", function(){ SUP.sel = SUP.sel === b.getAttribute("data-id") ? null : b.getAttribute("data-id"); supPinta(); }); });
  function suma(l){ var n = 0, k = F(0); l.forEach(function(p){ if (typeof p[2] === "object") k = fsum(k, p[2]); else n += p[2]; }); return (n ? n1(n, 2) : "") + (k.n ? (n ? " + " : "") + piTxt(k) : "") + (k.n ? " ≈ " + n1(n + piVal(k)) : ""); }
  $("su-res").innerHTML = '<div class="linea">' + T("Lateral area (without the bases): ", "Área lateral (sin las bases): ") + "<strong>" + suma(lat) + " " + u[3] + "</strong></div>" + '<div class="linea">' + T("Total area: ", "Área total: ") + "<strong>" + suma(pz) + " " + u[3] + "</strong></div>";
}
$("su-sol").addEventListener("change", supCampos); $("su-u").addEventListener("change", supPinta);
$("su-total").addEventListener("click", function(){ SUP.modo = "total"; SUP.sel = null; $("su-total").setAttribute("aria-pressed", "true"); $("su-lat").setAttribute("aria-pressed", "false"); supPinta(); });
$("su-lat").addEventListener("click", function(){ SUP.modo = "lat"; SUP.sel = null; $("su-lat").setAttribute("aria-pressed", "true"); $("su-total").setAttribute("aria-pressed", "false"); supPinta(); });
supCampos();
creaPracticaLibre("sq", function(){
  var tipo = elige(["cl", "ct", "kl", "kt", "pt", "es", "kh"]), u = UNID[elige(["in", "ft", "yd"])], r = aleatorio(1, 8), h = aleatorio(2, 12), l, k, enun, sol, pist = [];
  if (tipo === "cl"){ k = F(2 * r * h); enun = T("Find the lateral area of a cylinder with radius " + r + " and height " + h, "Calcule el área lateral de un cilindro de radio " + r + " y altura " + h); sol = "2π · " + r + " · " + h + " = " + piTxt(k); pist = [{k: r * h, msg: T("You left out the 2: 2πrh.", "Olvidó el 2: 2πrh.")}, {k: 2 * r * h + 2 * r * r, msg: T("Lateral means without the two circles.", "Lateral quiere decir sin los dos círculos.")}]; }
  else if (tipo === "ct"){ k = F(2 * r * h + 2 * r * r); enun = T("Find the total surface area of a cylinder with radius " + r + " and height " + h, "Calcule el área total de un cilindro de radio " + r + " y altura " + h); sol = "2π · " + r + " · " + h + " + 2π · " + r + "² = " + piTxt(F(2 * r * h)) + " + " + piTxt(F(2 * r * r)) + " = " + piTxt(k); pist = [{k: 2 * r * h, msg: T("That is only the side. Add the two circles, 2πr².", "Eso es solo el lado. Falta sumar los dos círculos, 2πr².")}, {k: 2 * r * h + r * r, msg: T("There are two circles: 2πr².", "Son dos círculos: 2πr².")}]; }
  else if (tipo === "kl" || tipo === "kt"){ l = r + aleatorio(1, 6); k = tipo === "kl" ? F(r * l) : F(r * l + r * r); enun = T("Find the " + (tipo === "kl" ? "lateral" : "total surface") + " area of a cone with radius " + r + " and slant height " + l, "Calcule el área " + (tipo === "kl" ? "lateral" : "total") + " de un cono de radio " + r + " y altura inclinada " + l); sol = "π · " + r + " · " + l + (tipo === "kt" ? " + π · " + r + "² = " + piTxt(F(r * l)) + " + " + piTxt(F(r * r)) : "") + " = " + piTxt(k);
    pist = [{k: 2 * r * l, msg: T("The cone has no 2: πrℓ.", "El cono no lleva 2: πrℓ.")}, tipo === "kt" ? {k: r * l, msg: T("That is only the side. Add the base, πr².", "Eso es solo el lado. Falta la base, πr².")} : {k: r * l + r * r, msg: T("Lateral means without the base.", "Lateral quiere decir sin la base.")}]; }
  else if (tipo === "kh"){ var tr = elige([[3, 4], [6, 8], [5, 12], [8, 6], [4, 3]]); r = tr[0]; h = tr[1]; l = Math.sqrt(r * r + h * h); k = F(r * l); enun = T("A cone has radius " + r + " and height " + h + " (straight up). Find its lateral area", "Un cono tiene radio " + r + " y altura (vertical) " + h + ". Calcule su área lateral"); sol = "ℓ = √(" + r + "² + " + h + "²) = " + l + "; π · " + r + " · " + l + " = " + piTxt(k); pist = [{k: r * h, msg: T("Use the slant height ℓ, not h: ℓ = √(r² + h²).", "Use la altura inclinada ℓ, no h: ℓ = √(r² + h²).")}]; }
  else if (tipo === "es"){ k = F(4 * r * r); enun = T("Find the surface area of a sphere with radius " + r, "Calcule el área de la superficie de una esfera de radio " + r); sol = "4π · " + r + "² = " + piTxt(k); pist = [{k: 4 * r * r * r / 3, msg: T("4/3 πr³ is the volume. The area is 4πr².", "4/3 πr³ es el volumen. El área es 4πr².")}, {k: r * r, msg: T("Multiply by 4: 4πr².", "Multiplique por 4: 4πr².")}]; }
  else { var a = aleatorio(2, 9), b = aleatorio(2, 9), c = aleatorio(2, 9), A = 2 * (a * b + a * c + b * c);
    return {enun: T("Find the total surface area of a box " + a + " × " + b + " × " + c + " (in " + u[1] + ").", "Calcule el área total de una caja de " + a + " × " + b + " × " + c + " (en " + u[1] + ")."),
      evalua: function(txt){ return evaluaNum(txt, A, 0.01, [{v: a * b * c, msg: T("That is the volume. The area adds the six faces.", "Ese es el volumen. El área suma las seis caras.")}, {v: a * b + a * c + b * c, msg: T("Each face has a twin: multiply by 2.", "Cada cara tiene una gemela: multiplique por 2.")}]); },
      solucion: "2(" + a + "·" + b + " + " + a + "·" + c + " + " + b + "·" + c + ") = 2(" + (a * b) + " + " + (a * c) + " + " + (b * c) + ") = " + A + " " + u[3] + "."}; }
  return {enun: enun + " (" + u[1] + "). " + T("Give it with π or as a decimal.", "Escríbalo con π o en decimal."), evalua: function(txt){ return evaluaPi(txt, k, pist); }, solucion: sol + " ≈ " + n1(piVal(k)) + " " + u[3] + "."};
});

/* ===== MODULE 4 · Optimization ===== */
function cajasDe(V){ var l = []; for (var a = 1; a <= V; a++) for (var b = a; b <= V; b++) if (V % (a * b) === 0){ var c = V / (a * b); if (c >= b) l.push([a, b, c, 2 * (a * b + a * c + b * c)]); } l.sort(function(x, y){ return y[3] - x[3]; }); return l; }
function opPinta(){
  var V = +$("op-v").value, l = cajasDe(V), i = Math.min(+$("op-i").value, l.length - 1), min = Math.min.apply(null, l.map(function(x){ return x[3]; })), q = l[i], u = UNID[$("op-u").value];
  $("op-i").max = l.length - 1; $("op-iv").textContent = q[0] + " × " + q[1] + " × " + q[2];
  $("op-svg").innerHTML = prismaSVG({L: q[2], b: q[1], h: q[0], esc: Math.min(26, 200 / q[2]), voz: T("A box " + q[0] + " × " + q[1] + " × " + q[2] + ".", "Una caja de " + q[0] + " × " + q[1] + " × " + q[2] + ".")});
  $("op-res").innerHTML = '<div class="linea">V = ' + q[0] + " · " + q[1] + " · " + q[2] + " = " + V + " " + u[2] + "</div>" + '<div class="linea veredicto">' + T("Area = ", "Área = ") + "2(" + q[0] * q[1] + " + " + q[0] * q[2] + " + " + q[1] * q[2] + ") = " + q[3] + " " + u[3] + (q[3] === min ? T(" · the least cardboard!", " · ¡el menor cartón!") : "") + "</div>";
  $("op-tabla").innerHTML = '<caption class="sr-only">' + T("All the boxes with whole-number sides that hold this volume, and their surface area", "Todas las cajas de lados enteros que guardan este volumen, con su área de superficie") + '</caption><thead><tr><th scope="col">' + T("Box", "Caja") + '</th><th scope="col">' + T("Surface area", "Área de superficie") + "</th></tr></thead><tbody>" +
    l.map(function(x, k){ return '<tr class="' + (x[3] === min ? "mejor" : "") + (k === i ? " fila-activa" : "") + '"><td>' + x[0] + " × " + x[1] + " × " + x[2] + "</td><td>" + x[3] + (x[3] === min ? " ✓" : "") + "</td></tr>"; }).join("") + "</tbody>";
}
$("op-v").addEventListener("change", function(){ $("op-i").value = 0; opPinta(); }); $("op-i").addEventListener("input", opPinta); $("op-u").addEventListener("change", opPinta); opPinta();
OMR("oq", function(){
  var V = elige([24, 36, 48, 60, 64, 72, 100]), l = baraja(cajasDe(V)).slice(0, 3);
  if (l.length < 3 || l[0][3] === l[1][3] || l[1][3] === l[2][3] || l[0][3] === l[2][3]) l = cajasDe(V).filter(function(x, i, a){ return i === 0 || i === a.length - 1 || i === Math.floor(a.length / 2); });
  var best = l.reduce(function(a, b){ return b[3] < a[3] ? b : a; }), key = function(x){ return x.slice(0, 3).join("x"); };
  return {enun: T("These boxes all hold " + V + " cubic inches. Which one uses the least cardboard?", "Todas estas cajas guardan " + V + " pulgadas cúbicas. ¿Cuál usa menos cartón?"), correcta: key(best),
    opciones: l.map(function(x){ return {clave: key(x), html: x[0] + " × " + x[1] + " × " + x[2]}; }),
    pista: T("Find the surface area of each box: 2(ab + ac + bc). The one closest to a cube usually wins.", "Calcule el área de cada caja: 2(ab + ac + bc). La más parecida a un cubo suele ganar."),
    bien: l.map(function(x){ return x[0] + "×" + x[1] + "×" + x[2] + ": " + x[3]; }).join("; ") + "."};
});
'''

def practica_pagina():
    n = N
    unidades = [("in", t("inches", "pulgadas")), ("ft", t("feet", "pies")), ("yd", t("yards", "yardas"))]
    figs = [("silo", t("Silo (cylinder + cone)", "Silo (cilindro + cono)")), ("tanque", t("Tank (cylinder + half-sphere)", "Tanque (cilindro + semiesfera)")), ("capsula", t("Capsule (cylinder + 2 half-spheres)", "Cápsula (cilindro + 2 semiesferas)")), ("torre", t("Tower (prism + pyramid)", "Torre (prisma + pirámide)")), ("bloque", t("Drilled block (prism − cylinder)", "Bloque perforado (prisma − cilindro)"))]
    piezas = [("cil", t("Cylinder", "Cilindro")), ("cono", t("Cone", "Cono")), ("semi", t("Half-sphere", "Semiesfera")), ("esf", t("Whole sphere", "Esfera completa")), ("pri", t("Rectangular prism", "Prisma rectangular")), ("pir", t("Pyramid", "Pirámide"))]
    mods = [
     (t("decompose", "descomponer"), t("Breaking a composite figure into parts", "Descomponer una figura compuesta"),
      f'''      <p>{t("Choose a figure. Check the simple solids it breaks into and decide whether their volumes are added or subtracted. Then check your answer: when it is right, the parts are drawn apart, each in its color.", "Elija una figura. Marque los sólidos simples en que se descompone y decida si sus volúmenes se suman o se restan. Después compruebe: cuando acierte, las partes se dibujan separadas, cada una con su color.")}</p>
      <div class="panel"><div class="campos">{n4.lista("dc-fig", t("Figure", "Figura"), figs)}</div></div>
      <div id="dc-svg"></div>
      <fieldset class="panel" id="dc-piezas"><legend><strong>{t("1. Which simple solids make it up?", "1. ¿En qué sólidos simples se descompone?")}</strong></legend>
        {"".join(f'<label style="display:inline-flex;gap:6px;margin:4px 14px 4px 0;"><input type="checkbox" value="{k}"> {v}</label>' for k, v in piezas)}</fieldset>
      <fieldset class="panel"><legend><strong>{t("2. Are the volumes added or subtracted?", "2. ¿Los volúmenes se suman o se restan?")}</strong></legend>
        <label style="margin-right:18px;"><input type="radio" name="dc-op" id="dc-mas"> {t("Added", "Se suman")}</label><label><input type="radio" name="dc-op" id="dc-menos"> {t("Subtracted", "Se restan")}</label></fieldset>
      <div class="fila-btn"><button type="button" class="btn" id="dc-comprobar">{t("Check my breakdown", "Comprobar mi descomposición")}</button><button type="button" class="btn-sec" id="dc-ver">{t("Show the answer", "Mostrar la respuesta")}</button><button type="button" class="btn-sec" id="dc-limpia">{t("Start over", "Reiniciar")}</button></div>
      <div class="fb" id="dc-fb" role="status"></div>
      <div class="caja-tip">{t("Add or subtract? If the parts come together to make a bigger body, add. If a part is taken away (a hole, a hollow), subtract.", "¿Sumar o restar? Si las partes se juntan para formar un cuerpo más grande, se suman. Si una parte se quita (un agujero, un hueco), se resta.")}</div>
{B.om("dq", t("Practice: the pieces and the operation", "Practique: las piezas y la operación"))}'''),
     (t("volume", "volumen"), t("The volume of composite figures", "Volumen de figuras compuestas"),
      f'''      <p>{t("Choose a figure and change its measures. The table finds the volume of each part with its formula and adds (or subtracts) them. Check “Separate the parts” to see each piece on its own.", "Elija una figura y cambie sus medidas. La tabla calcula el volumen de cada parte con su fórmula y los suma (o los resta). Marque «Separar las partes» para ver cada pieza por separado.")}</p>
      <div class="panel"><div class="campos">{n4.lista("cv-fig", t("Figure", "Figura"), figs)}{n4.lista("cv-u", t("Unit", "Unidad"), unidades)}</div>
        <div class="campos" id="cv-dims"></div>
        <div class="campo"><label><input type="checkbox" id="cv-sep"> {t("Separate the parts", "Separar las partes")}</label></div></div>
      <div id="cv-svg"></div>
      <div class="tabla-scroll"><table class="tabla-lados" id="cv-tabla"></table></div>
{B.libre("cq", t("Practice: the total volume", "Practique: el volumen total"), t("Volume", "Volumen"), nota=False).replace('<div class="enun" id="cq-enun"></div>', '<div class="enun" id="cq-enun"></div><div id="cq-svg"></div>')}'''),
     (t("surface", "superficie"), t("Surface area: the solid and its net", "Área de superficie: el sólido y su desarrollo"),
      f'''      <p>{t("Each solid is shown closed and opened flat (its net). Choose lateral or total area, or press a piece to light it up in the net. The area is built piece by piece.", "Cada sólido aparece cerrado y abierto en el plano (su desarrollo). Elija el área lateral o la total, o pulse una pieza para iluminarla en el desarrollo. El área se construye pieza por pieza.")}</p>
      <div class="panel"><div class="campos">{n4.lista("su-sol", t("Solid", "Sólido"), [("prisma", t("Rectangular prism", "Prisma rectangular")), ("cilindro", t("Cylinder", "Cilindro")), ("cono", t("Cone", "Cono")), ("piramide", t("Square pyramid", "Pirámide de base cuadrada")), ("esfera", t("Sphere", "Esfera"))])}{n4.lista("su-u", t("Unit", "Unidad"), unidades)}</div>
        <div class="campos" id="su-dims"></div>
        <div class="modos" role="group" aria-label="{t("Area to show", "Área que se muestra")}"><button type="button" class="btn-sec" id="su-total" aria-pressed="true">{t("Total area", "Área total")}</button><button type="button" class="btn-sec" id="su-lat" aria-pressed="false">{t("Lateral area only", "Solo el área lateral")}</button></div></div>
      <div class="tarjetas"><div style="flex:1;min-width:260px" id="su-cerrado"></div><div style="flex:1.4;min-width:300px" id="su-red"></div></div>
      <div class="tarjetas" id="su-cards"></div>
{n4.salida("su-res")}
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Lateral and total surface area of the solids on the formula sheet", "Área lateral y total de los sólidos de la hoja de fórmulas")}</caption>
        <thead><tr><th scope="col">{t("Solid", "Sólido")}</th><th scope="col">{t("Lateral area", "Área lateral")}</th><th scope="col">{t("Total area", "Área total")}</th></tr></thead><tbody>
        <tr><td>{t("Rectangular prism", "Prisma rectangular")}</td><td>{t("perimeter of the base × height", "perímetro de la base × altura")}</td><td>2ab + 2ac + 2bc</td></tr>
        <tr><td>{t("Cylinder", "Cilindro")}</td><td>2πrh</td><td>2πrh + 2πr²</td></tr>
        <tr><td>{t("Cone", "Cono")}</td><td>{t("πrℓ (ℓ = slant height)", "πrℓ (ℓ = altura inclinada)")}</td><td>πrℓ + πr²</td></tr>
        <tr><td>{t("Pyramid", "Pirámide")}</td><td>1/2 × {t("perimeter", "perímetro")} × ℓ</td><td>1/2 × {t("perimeter", "perímetro")} × ℓ + B</td></tr>
        <tr><td>{t("Sphere", "Esfera")}</td><td>—</td><td>4πr²</td></tr></tbody></table></div>
      <div class="caja-tip">{t("Lateral means “without the bases.” The lateral area counts only the surfaces around the body; the total area adds the bottom and, if there is one, the top. Read the problem carefully: an open tank has no top.", "Lateral quiere decir «sin las tapas». El área lateral cuenta solo las superficies que rodean el cuerpo; el área total añade la base y, si existe, la tapa. Lea bien el problema: un tanque abierto no tiene tapa.")}</div>
{B.libre("sq", t("Practice: surface area", "Practique: el área de superficie"), t("Area", "Área"), nota=False)}'''),
     (t("optimize", "optimizacion"), t("An idea of optimization", "Una idea de optimización"),
      f'''{n4.formula(t("Area of a box = 2(length·width + length·height + width·height)", "Área de la caja = 2(largo·ancho + largo·alto + ancho·alto)"))}
      <p>{t("Choose a volume and move the slider through all the boxes with whole-number sides that hold exactly that volume. The table marks in green the one that uses the least cardboard.", "Elija un volumen y mueva el deslizador para recorrer todas las cajas de medidas enteras que guardan exactamente ese volumen. La tabla marca en verde la que usa menos cartón.")}</p>
      <div class="panel"><div class="campos">{n4.lista("op-v", t("Volume the box must hold", "Volumen que debe guardar la caja"), [(v, str(v)) for v in (24, 36, 48, 64, 100)], 64)}
        <div class="campo" style="flex:1;min-width:220px;"><label for="op-i">{t("Box:", "Caja:")} <span id="op-iv"></span></label><input type="range" id="op-i" min="0" max="5" step="1" value="0"></div>{n4.lista("op-u", t("Unit", "Unidad"), unidades)}</div>
        <p class="nota">{t("The slider goes from the box that uses the most cardboard to the one that uses the least.", "El deslizador va de la caja que más cartón usa a la que menos usa.")}</p></div>
      <div id="op-svg"></div>
{n4.salida("op-res")}
      <div class="tabla-scroll"><table class="tabla-lados" id="op-tabla"></table></div>
      <div class="caja-tip">{t("The same volume does not mean the same material. The volume measures what fits inside; the surface area measures the material that wraps it. Shapes closer to a cube tend to have less surface area.", "Mismo volumen no significa mismo material. El volumen mide lo que cabe dentro; el área de superficie mide el material que lo envuelve. Las formas más parecidas a un cubo tienden a tener menor área de superficie.")}</div>
{B.om("oq", t("Practice: which design uses less material?", "Practique: ¿qué diseño usa menos material?"))}''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO + "\n  tr.fila-activa td{background:#fff8e1;font-weight:700;}\n  tr.mejor td{background:#e8f5e9;}\n  button.tarjeta{font:inherit;cursor:pointer;}\n  button.tarjeta[aria-pressed=\"true\"]{border-color:var(--tema);box-shadow:0 0 0 3px var(--tema-bg2);}", scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Figuras 3D compuestas y área de superficie")
