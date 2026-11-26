"""Level 2 · Lesson 7.1 · Area of composite figures — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg
from geo import figura

B.NIVEL = 2
N = "7-1"
TEMA = ("Geometry: circles and composite figures", "Geometría transicional")
TIT = ("Area of composite figures", "Área de figuras compuestas")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

L_PTS = [(0, 0), (12, 0), (12, 10), (18, 10), (18, 20), (0, 20)]

def fig_tres():
    a = [(0, 0), (6, 0), (6, 4), (10, 4), (10, 9), (0, 9)]
    b = [(14, 0), (24, 0), (24, 6), (21, 9), (14, 9)]
    c = [(28, 0), (36, 0), (36, 6), (28, 6)]
    techo = [(28, 6), (36, 6), (32, 10)]
    ex = [dict(txt=t("L shape", "En forma de L"), p=(5, -2)), dict(txt=t("Cut corner", "Esquina recortada"), p=(19, -2)), dict(txt=t("House", "Casa"), p=(32, -2))]
    return figura([dict(pts=a), dict(pts=b), dict(pts=c), dict(pts=techo, fill="#cfd8dc")], [],
                  t("Three composite figures: an L shape made of two rectangles, a rectangle with one corner cut off, and a house made of a rectangle with a triangle on top.",
                    "Tres figuras compuestas: una L formada por dos rectángulos, un rectángulo con una esquina recortada y una casa formada por un rectángulo con un triángulo encima."), ex, 260)

def fig_l_suma():
    cot = [((0, 0), (12, 0), "12 ft"), ((18, 20), (0, 20), "18 ft"), ((0, 20), (0, 0), "20 ft"), ((18, 10), (18, 20), "10 ft"), ((12, 10), (18, 10), "6 ft"), ((12, 0), (12, 10), "10 ft")]
    ex = [dict(linea=((0, 10), (12, 10))), dict(txt="R1", p=(9, 15)), dict(txt="R2", p=(6, 5))]
    return figura([dict(pts=L_PTS)], cot, t("L-shaped floor plan: 18 feet across the top, 20 feet on the left side, 12 feet across the bottom. A dashed line 10 feet down from the top splits it into R1, 18 by 10 on top, and R2, 12 by 10 below.",
                                         "Plano en forma de L: 18 pies arriba, 20 pies del lado izquierdo y 12 pies abajo. Una línea punteada a 10 pies del borde superior lo divide en R1, de 18 por 10, arriba, y R2, de 12 por 10, abajo."), ex, 330)

def fig_l_resta():
    cot = [((18, 20), (0, 20), "18 ft"), ((0, 20), (0, 0), "20 ft"), ((12, 0), (18, 0), "6 ft"), ((18, 0), (18, 10), "10 ft")]
    falta = dict(pts=[(12, 0), (18, 0), (18, 10), (12, 10)], fill="#ffebee", stroke="#b71c1c", dash=True, sw=2)
    return figura([dict(pts=L_PTS), falta], cot, t("The same L shape completed to an 18 by 20 rectangle; the missing 6 by 10 corner is shown with a red dashed outline.",
                                                 "La misma L completada hasta un rectángulo de 18 por 20; la esquina que falta, de 6 por 10, aparece con borde rojo punteado."),
                  [dict(txt=t("missing", "falta"), p=(15, 5), col="#b71c1c")], 330)

def fig_terreno():
    P = [(0, 0), (25, 0), (25, 12), (17, 12), (17, 18), (0, 18)]
    falta = dict(pts=[(17, 12), (25, 12), (25, 18), (17, 18)], fill="#ffebee", stroke="#b71c1c", dash=True, sw=2)
    cot = [((0, 0), (25, 0), "25 ft"), ((0, 18), (0, 0), "18 ft"), ((25, 18), (17, 18), "8 ft"), ((25, 12), (25, 18), "6 ft")]
    return figura([dict(pts=P, fill="#c8e6c9"), falta], cot, t("A 25 by 18 foot yard with an 8 by 6 foot corner cut off at the top right, shown with a red dashed outline.",
                                                          "Un patio de 25 por 18 pies al que le falta una esquina de 8 por 6 pies arriba a la derecha, marcada con borde rojo punteado."),
                  [dict(txt=t("missing", "falta"), p=(21, 15), col="#b71c1c")], 300)

def fig_fachada():
    cot = [((0, 0), (30, 0), "30 ft"), ((30, 0), (30, 20), "20 ft")]
    ex = [dict(linea=((15, 20), (15, 32))), dict(txt="12 ft", p=(18.6, 25))]
    return figura([dict(pts=[(0, 0), (30, 0), (30, 20), (0, 20)]), dict(pts=[(0, 20), (30, 20), (15, 32)], fill="#cfd8dc")], cot,
                  t("House front: a rectangle 30 feet wide and 20 feet tall with a triangle on top whose height is 12 feet.", "Fachada: un rectángulo de 30 pies de ancho y 20 de alto con un triángulo encima de 12 pies de altura."), ex, 300)

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Topic 7. So far Level 2 has worked with numbers and comparisons: integers, fractions, PEMDAS, ratios, percents, and money math. Now the setting changes: you start <strong>measuring space</strong>. This first lesson opens the topic with a key skill: finding the area of figures that are not simple rectangles or triangles, but combinations of several basic shapes.", "Bienvenida al Tema 7. Hasta ahora el Nivel 2 ha trabajado con números y comparaciones: enteros con signo, fracciones, PEMDAS, razones, porcentajes y matemáticas financieras. Ahora el terreno cambia: se pasa a la <strong>medición del espacio</strong>. Esta primera lección abre el tema con una técnica esencial: cómo medir el área de figuras que no son simples rectángulos o triángulos, sino combinaciones de varias formas básicas.")}</p>
<p>{t("Area is always measured in <strong>square units</strong>: square inches (in²), square feet (ft²), square yards (yd²).", "El área se mide siempre en <strong>unidades cuadradas</strong>: pulgadas cuadradas (in²), pies cuadrados (ft²), yardas cuadradas (yd²).")}</p>
{tabla(t("Basic area formulas", "Fórmulas básicas de área"), t("Area formulas for the basic figures", "Fórmulas de área de las figuras básicas"),
       [t("Figure", "Figura"), t("Formula", "Fórmula"), t("In words", "En palabras")],
       [[t("Rectangle", "Rectángulo"), "A = b × h", t("base times height", "base por altura")],
        [t("Square", "Cuadrado"), "A = s²", t("side squared", "lado al cuadrado")],
        [t("Parallelogram", "Paralelogramo"), "A = b × h", t("base times height (the height, not the slanted side)", "base por altura (la altura, no el lado inclinado)")],
        [t("Triangle", "Triángulo"), "A = (b × h) ÷ 2", t("base times height, divided by two", "base por altura, entre dos")],
        [t("Trapezoid", "Trapecio"), "A = ((B + b) × h) ÷ 2", t("sum of the bases times the height, divided by two", "suma de las bases por la altura, entre dos")]])}
{caja("tip", t("One idea behind all of them", "Una idea que las une"), t("<p>All these formulas share one structure: <strong>base times height</strong>, adjusted by a factor (1 for the rectangle, ½ for the triangle, the average of the bases for the trapezoid). Thinking this way helps you remember them without memorizing.</p>", "<p>Todas estas fórmulas comparten una estructura: <strong>base por altura</strong>, ajustada por un factor (1 en el rectángulo, ½ en el triángulo, el promedio de las bases en el trapecio). Pensar así ayuda a recordarlas sin memorizarlas a la fuerza.</p>"))}
{enlace(n, t("basic-formulas", "formulas-basicas"), t("the basic area formulas", "las fórmulas básicas de área"), t("Explore the rectangle, square, parallelogram, triangle, and trapezoid, and review what each formula measures.", "Explore el rectángulo, el cuadrado, el paralelogramo, el triángulo y el trapecio, y repase qué mide cada fórmula."))}'''

    s2 = f'''<p>{t("A <strong>composite figure</strong> is made by putting together two or more simple figures. They are everywhere: an L-shaped apartment, a yard with one corner cut off, the front of a house (a rectangle with a triangle on top).", "Una <strong>figura compuesta</strong> se forma al combinar dos o más figuras simples. Aparecen en todas partes: un apartamento en forma de L, un patio con una esquina recortada, la fachada de una casa (un rectángulo con un triángulo encima).")}</p>
<div style="text-align:center">{fig_tres()}</div>
<p>{t("Any of these can be measured with one simple idea: <strong>divide and conquer</strong>. Draw one or more helper lines that split the figure into simple pieces whose area you know how to find; then add them, or in some cases subtract.", "Cualquiera de ellas se mide con una idea sencilla: <strong>dividir para conquistar</strong>. Se trazan una o varias líneas auxiliares que descomponen la figura en piezas simples cuya área se sabe calcular; luego se suman o, en algunos casos, se restan.")}</p>
{tabla(t("The two strategies", "Las dos estrategias"), t("Addition and subtraction strategies", "Estrategias de adición y de sustracción"),
       [t("Strategy", "Estrategia"), t("What you do", "Qué se hace"), t("Best when…", "Conviene cuando…")],
       [[t("Addition", "Adición"), t("split the figure into pieces and add their areas", "se parte la figura en piezas y se suman sus áreas"), t("the figure splits easily into pieces", "la figura se divide fácilmente en piezas")],
        [t("Subtraction", "Sustracción"), t("find the area of the whole figure and subtract what is missing", "se calcula la figura completa y se resta lo que falta"), t("the figure is a big one with a piece taken out", "la figura es una grande a la que le quitaron un trozo")]])}
{enlace(n, t("strategy", "estrategia"), t("what a composite figure is", "qué es una figura compuesta"), t("Recognize figures made of simple pieces and decide how to split them.", "Reconozca figuras formadas por piezas simples y decida cómo dividirlas."))}'''

    s3 = f'''<p>{t("With the <strong>addition strategy</strong>, draw a helper line that splits the figure into two (or more) simple pieces. Find each area on its own and add the results.", "En la <strong>estrategia de adición</strong>, se traza una línea auxiliar que parte la figura en dos (o más) piezas simples. Se calcula el área de cada pieza por separado y se suman los resultados.")}</p>
<div style="text-align:center">{fig_l_suma()}</div>
{ej(t("Example: an L shape", "Ejemplo: forma de L"), t("An L-shaped room has the measurements shown in the plan. What is its total area?", "Un cuarto en forma de L tiene las medidas que muestra el plano. ¿Cuál es su área total?"),
  [("1", t("Helper line.", "Línea auxiliar."), t("Draw a horizontal line 10 ft below the top edge. The figure splits into two rectangles.", "Trace una línea horizontal a 10 ft del borde superior. La figura queda dividida en dos rectángulos.")),
   ("2", t("R1 (top).", "R1 (arriba)."), "18 × 10 = 180 ft²."),
   ("3", t("R2 (bottom).", "R2 (abajo)."), "12 × 10 = 120 ft²."),
   ("4", t("Add.", "Sume."), "180 + 120 = 300 ft²."),
   ("✓", t("Answer.", "Respuesta."), t("The room has an area of <strong>300 square feet</strong>.", "El cuarto tiene un área de <strong>300 pies cuadrados</strong>."))])}
{caja("tip", t("Visual strategy", "Estrategia visual"), t("<p>Label each piece with a letter or a different color (R1, R2, T1…) and write its area next to it. At the end, adding them up is a mechanical step.</p>", "<p>Conviene marcar cada pieza con una letra o un color distinto (R1, R2, T1…) y anotar su área al lado. Al final, sumar todas las áreas se vuelve un paso mecánico.</p>"))}
{practica("p1", t("Practice 1 — Two rectangles", "Práctica 1 — Dos rectángulos"), t("A figure is made of two rectangles joined together: one is 20 ft × 5 ft and the other is 12 ft × 5 ft. What is the total area?", "Una figura está formada por dos rectángulos unidos: uno de 20 ft × 5 ft y otro de 12 ft × 5 ft. ¿Cuál es el área total?"),
          [("a", "100 ft²"), ("b", "160 ft²"), ("c", "42 ft²"), ("d", "6,000 ft²")])}
{enlace(n, t("addition", "adicion"), t("the addition strategy", "la estrategia de adición"), t("Change the measurements of the L-shaped room, figure out the missing side, and add the pieces.", "Mueva las medidas del cuarto en L, deduzca el lado que falta y sume las piezas."))}'''

    s4 = f'''<p>{t("Sometimes a composite figure looks more like <strong>a big rectangle with a piece missing</strong>. The <strong>subtraction strategy</strong>: find the area of the whole rectangle, then subtract the area of the missing piece.", "A veces una figura compuesta se ve mejor como <strong>un rectángulo grande al que le falta un trozo</strong>. La <strong>estrategia de sustracción</strong> consiste en calcular el área del rectángulo completo y luego restar el área del trozo faltante.")}</p>
<div style="text-align:center">{fig_terreno()}</div>
{ej(t("Example: a yard with a corner cut off", "Ejemplo: un patio con una esquina recortada"), t("A 25 ft × 18 ft rectangular yard has one corner cut off (a rectangle 8 ft × 6 ft). What is the usable area?", "Un patio rectangular de 25 ft × 18 ft tiene una esquina recortada (un rectángulo de 8 ft × 6 ft). ¿Cuál es el área aprovechable?"),
  [("1", t("The whole rectangle.", "El rectángulo completo."), "25 × 18 = 450 ft²."),
   ("2", t("The missing piece.", "El trozo que falta."), "8 × 6 = 48 ft²."),
   ("3", t("Subtract.", "Reste."), "450 − 48 = 402 ft²."),
   ("✓", t("Answer.", "Respuesta."), t("The usable area is <strong>402 square feet</strong>.", "El área aprovechable es de <strong>402 pies cuadrados</strong>."))])}
{caja("ojo", t("Watch out", "Atención"), t("<p>Choosing addition or subtraction is a matter of convenience. The same figure can be solved both ways, and the result must be the same. If one way is clumsy, try the other.</p>", "<p>Elegir entre adición y sustracción es cuestión de comodidad. Una misma figura puede resolverse de las dos maneras, y el resultado debe ser idéntico. Si un camino resulta engorroso, conviene probar el otro.</p>"))}
{practica("p2", t("Practice 2 — Which strategy?", "Práctica 2 — ¿Qué estrategia?"), t("A rectangular field had a triangle removed from one corner. Which strategy is easier?", "A un campo rectangular se le quitó un triángulo en una esquina. ¿Qué estrategia es más cómoda?"),
          [("a", t("Subtraction: whole rectangle minus the triangle", "Sustracción: el rectángulo completo menos el triángulo")), ("b", t("Addition: split it into pieces and add", "Adición: partirlo en piezas y sumar"))])}
{practica("p3", t("Practice 3 — Subtract what is missing", "Práctica 3 — Reste lo que falta"), t("An L shape is a 15 ft × 8 ft rectangle with a 6 ft × 4 ft corner cut out. What is its area?", "Una L es un rectángulo de 15 ft × 8 ft al que le falta una esquina de 6 ft × 4 ft. ¿Cuál es su área?"),
          [("a", "120 ft²"), ("b", "24 ft²"), ("c", "96 ft²"), ("d", "144 ft²")])}
{enlace(n, t("subtraction", "sustraccion"), t("the subtraction strategy", "la estrategia de sustracción"), t("Complete the rectangle, subtract the missing piece, and check that it matches the addition result.", "Complete el rectángulo, reste el trozo que falta y compruebe que da lo mismo que por adición."))}'''

    s5 = f'''<p>{t("For many figures both strategies work and give the same result. It is worth seeing this in an example.", "En muchas figuras las dos estrategias funcionan y conducen al mismo resultado. Vale la pena verlo en un ejemplo concreto.")}</p>
{tabla(t("Addition and subtraction", "Adición y sustracción"), t("The two strategies side by side", "Las dos estrategias, lado a lado"),
       ["", t("Addition ➕", "Adición ➕"), t("Subtraction ➖", "Sustracción ➖")],
       [[t("What you do", "Qué se hace"), t("Split the figure into simple pieces and add their areas.", "Se divide la figura en piezas simples y se suman sus áreas."), t("Complete the figure to a big rectangle and subtract the extra piece.", "Se completa la figura hasta formar un rectángulo grande y se le resta el trozo que sobra.")],
        [t("Formula", "Fórmula"), "A = A₁ + A₂ + …", t("A = A<sub>whole</sub> − A<sub>missing</sub>", "A = A<sub>completo</sub> − A<sub>falta</sub>")],
        [t("Useful when", "Útil cuando"), t("the cuts are easy to draw", "las divisiones son fáciles de trazar"), t("what is missing is easy to see", "lo que falta se identifica claramente")]])}
<div style="text-align:center">{fig_l_resta()}</div>
{ej(t("Example: one figure, two ways", "Ejemplo: una misma figura por dos caminos"), t("Check that the L shape from the addition example (300 ft²) also comes out by subtraction.", "Compruebe que la L del ejemplo de adición (300 ft²) también se obtiene por sustracción."),
  [("1", t("The whole rectangle.", "El rectángulo completo."), t("18 × 20 = 360 ft² (the outside measurements).", "18 × 20 = 360 ft² (las medidas exteriores).")),
   ("2", t("The missing corner.", "La esquina que falta."), "6 × 10 = 60 ft²."),
   ("3", t("Subtract.", "Reste."), "360 − 60 = 300 ft²."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>300 ft²</strong>, the same as with addition. ✓", "<strong>300 ft²</strong>, igual que por adición. ✓"))])}'''

    s6 = f'''<p>{t("Once you have the area, you often multiply it by a <strong>unit price</strong> to find the total cost of a material: paint per square foot, carpet per square foot, tile per square foot.", "Una vez calculada el área, es muy común multiplicarla por un <strong>precio por unidad</strong> para conocer el costo total de un material: pintura, alfombra o losetas por pie cuadrado.")}</p>
{ej(t("Example: carpeting the L", "Ejemplo: alfombrar la L"), t("The L-shaped room (300 ft²) will be carpeted at $4 per square foot. What will it cost?", "El cuarto en forma de L (300 ft²) se va a alfombrar a $4 por pie cuadrado. ¿Cuánto costará?"),
  [("1", t("Area.", "Área."), "300 ft²."),
   ("2", t("Cost.", "Costo."), "300 × $4 = $1,200."),
   ("✓", t("Answer.", "Respuesta."), t("Carpeting the room costs <strong>$1,200</strong>.", "Alfombrar el cuarto cuesta <strong>$1,200</strong>."))])}
<div style="text-align:center">{fig_fachada()}</div>
{ej(t("Example: painting the front of a house", "Ejemplo: pintar una fachada"), t("The front of a house is a 30 ft × 20 ft rectangle with a triangle on top (base 30 ft, height 12 ft). One gallon of paint covers 350 ft². How many gallons do you need?", "La fachada de una casa es un rectángulo de 30 ft × 20 ft con un triángulo encima (base 30 ft, altura 12 ft). Un galón de pintura cubre 350 ft². ¿Cuántos galones se necesitan?"),
  [("1", t("Rectangle.", "Rectángulo."), "30 × 20 = 600 ft²."),
   ("2", t("Triangle.", "Triángulo."), "(30 × 12) ÷ 2 = 180 ft²."),
   ("3", t("Total.", "Total."), "600 + 180 = 780 ft²."),
   ("4", t("Gallons.", "Galones."), t("780 ÷ 350 ≈ 2.23. You cannot buy part of a gallon, so round <strong>up</strong>: 3 gallons.", "780 ÷ 350 ≈ 2.23. No se compran fracciones de galón, así que se redondea <strong>hacia arriba</strong>: 3 galones.")),
   ("✓", t("Answer.", "Respuesta."), t("You need <strong>3 gallons</strong> of paint.", "Hacen falta <strong>3 galones</strong> de pintura."))])}
{calc(t("Area and cost on the calculator", "El área y el costo en la calculadora"), t(f"<p>For the front of the house: {T('30')} {T('×')} {T('20')} {T('+')} {T('30')} {T('×')} {T('12')} {T('÷')} {T('2')} {T('enter')} gives 780. The calculator follows PEMDAS, so you do not need parentheses. Then {T('÷')} {T('350')} {T('enter')} gives 2.228…</p>", f"<p>Para la fachada: {T('30')} {T('×')} {T('20')} {T('+')} {T('30')} {T('×')} {T('12')} {T('÷')} {T('2')} {T('enter')} da 780. La calculadora respeta PEMDAS, así que no hacen falta paréntesis. Después, {T('÷')} {T('350')} {T('enter')} da 2.228…</p>"))}
{practica("p4", t("Practice 4 — A house", "Práctica 4 — Una casa"), t("A figure is a 10 ft × 6 ft rectangle with a triangle on top (base 10 ft, height 4 ft). What is its area?", "Una figura es un rectángulo de 10 ft × 6 ft con un triángulo encima (base 10 ft, altura 4 ft). ¿Cuál es su área?"),
          [("a", "100 ft²"), ("b", "64 ft²"), ("c", "80 ft²"), ("d", "120 ft²")])}
{practica("p5", t("Practice 5 — Tile", "Práctica 5 — Losetas"), t("A 48 ft² floor is covered with tile at $15 per square foot. What is the total cost?", "Un piso de 48 ft² se cubre con losetas a $15 por pie cuadrado. ¿Cuál es el costo total?"),
          [("a", "$63"), ("b", "$720"), ("c", "$320"), ("d", "$3.20")])}
{practica("p6", t("Practice 6 — Gallons of paint", "Práctica 6 — Galones de pintura"), t("A fence has 820 ft² to paint. One gallon covers 350 ft². How many gallons must you buy?", "Una cerca tiene 820 ft² por pintar. Un galón cubre 350 ft². ¿Cuántos galones hay que comprar?"),
          [("a", t("2 gallons", "2 galones")), ("b", t("2.34 gallons", "2.34 galones")), ("c", t("4 gallons", "4 galones")), ("d", t("3 gallons", "3 galones"))])}
{enlace(n, t("cost", "costo"), t("the cost of materials", "el costo de los materiales"), t("Go from the area to the budget, and round up the gallons or rolls.", "Pase del área al presupuesto y redondee hacia arriba los galones o los rollos."))}'''

    secciones = [("s-" + t("review", "repaso"), t("Review of the basic area formulas", "Repaso de las fórmulas básicas de área"), s1),
                 ("s-" + t("composite", "compuesta"), t("What a composite figure is", "Qué es una figura compuesta"), s2),
                 ("s-" + t("addition", "adicion"), t("The addition strategy", "La estrategia de adición"), s3),
                 ("s-" + t("subtraction", "sustraccion"), t("The subtraction strategy", "La estrategia de sustracción"), s4),
                 ("s-" + t("compare", "comparacion"), t("Comparing the two strategies", "Comparación de las dos estrategias"), s5),
                 ("s-" + t("cost", "costo"), t("Real uses: the cost of materials", "Aplicaciones reales: el costo de los materiales"), s6)]

    lesson = {"next": t("Lesson 7.2", "Lección 7.2"), "review": t("sections 3, 4, and 6", "las secciones 3, 4 y 6"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("That is only the first rectangle. Add the second one.", "Ese es solo el primer rectángulo. Sume el segundo."), "c": t("You added the sides. Area is base times height.", "Sumó los lados. El área es base por altura."), "d": t("You multiplied the two areas. Add them.", "Multiplicó las dos áreas. Súmelas.")},
             "right": t("100 + 60 = 160 ft².", "100 + 60 = 160 ft²."), "solution": t("20 × 5 = 100 and 12 × 5 = 60; 100 + 60 = 160 ft².", "20 × 5 = 100 y 12 × 5 = 60; 100 + 60 = 160 ft².")},
      "p2": {"ok": "a", "hints": {"b": t("The field is a whole rectangle with a piece missing: it is easier to subtract.", "El campo es un rectángulo completo al que le falta un trozo: es más cómodo restar.")},
             "right": t("Whole rectangle minus the missing triangle.", "Rectángulo completo menos el triángulo que falta."), "solution": t("Subtraction: find the area of the whole rectangle and subtract the triangle.", "Sustracción: se calcula el rectángulo completo y se resta el triángulo.")},
      "p3": {"ok": "c", "hints": {"a": t("That is the whole rectangle. Subtract the missing corner.", "Ese es el rectángulo completo. Reste la esquina que falta."), "b": t("That is the missing corner.", "Esa es la esquina que falta."), "d": t("You added the corner. Subtract it.", "Sumó la esquina. Réstela.")},
             "right": t("120 − 24 = 96 ft².", "120 − 24 = 96 ft²."), "solution": t("15 × 8 = 120; 6 × 4 = 24; 120 − 24 = 96 ft².", "15 × 8 = 120; 6 × 4 = 24; 120 − 24 = 96 ft².")},
      "p4": {"ok": "c", "hints": {"a": t("The triangle's area is divided by 2.", "El área del triángulo se divide entre 2."), "b": t("You added the sides of the triangle. Use (b × h) ÷ 2.", "Sumó los lados del triángulo. Use (b × h) ÷ 2."), "d": t("Check the rectangle: 10 × 6.", "Revise el rectángulo: 10 × 6.")},
             "right": t("60 + 20 = 80 ft².", "60 + 20 = 80 ft²."), "solution": t("Rectangle 10 × 6 = 60; triangle (10 × 4) ÷ 2 = 20; total 80 ft².", "Rectángulo 10 × 6 = 60; triángulo (10 × 4) ÷ 2 = 20; total 80 ft².")},
      "p5": {"ok": "b", "hints": {"a": t("You added. Multiply the area by the price.", "Sumó. Multiplique el área por el precio."), "c": t("Check: 48 × 15.", "Revise: 48 × 15."), "d": t("You divided. Multiply.", "Dividió. Multiplique.")},
             "right": t("48 × 15 = $720.", "48 × 15 = $720."), "solution": t("Cost = area × price = 48 × $15 = $720.", "Costo = área × precio = 48 × $15 = $720.")},
      "p6": {"ok": "d", "hints": {"a": t("2 gallons cover only 700 ft². The paint would run out.", "2 galones cubren solo 700 ft². La pintura no alcanza."), "b": t("The store does not sell part of a gallon. Round up.", "En la tienda no se vende parte de un galón. Redondee hacia arriba."), "c": t("3 gallons already cover 1,050 ft².", "3 galones ya cubren 1,050 ft².")},
             "right": t("820 ÷ 350 ≈ 2.34 → 3 gallons.", "820 ÷ 350 ≈ 2.34 → 3 galones."), "solution": t("820 ÷ 350 ≈ 2.34; round up: 3 gallons.", "820 ÷ 350 ≈ 2.34; se redondea hacia arriba: 3 galones.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("The triangle's area is divided by 2.", "El área del triángulo se divide entre 2."), "b": t("You added. Multiply base by height.", "Sumó. Multiplique base por altura."), "d": t("That is the perimeter idea, not the area.", "Esa es la idea del perímetro, no del área.")}, "solution": t("(10 × 6) ÷ 2 = 30 ft².", "(10 × 6) ÷ 2 = 30 ft².")},
      "B": {"ok": "a", "hints": {"b": t("You still need to divide by 2.", "Falta dividir entre 2."), "c": t("Add both bases before you multiply.", "Sume las dos bases antes de multiplicar."), "d": t("Use ((B + b) × h) ÷ 2.", "Use ((B + b) × h) ÷ 2.")}, "solution": t("((8 + 4) × 5) ÷ 2 = 30 ft².", "((8 + 4) × 5) ÷ 2 = 30 ft².")},
      "C": {"ok": "d", "hints": {"a": t("That is only the first rectangle.", "Ese es solo el primer rectángulo."), "b": t("That is only the second rectangle.", "Ese es solo el segundo rectángulo."), "c": t("You added the sides.", "Sumó los lados.")}, "solution": t("100 + 60 = 160 ft².", "100 + 60 = 160 ft².")},
      "D": {"ok": "b", "hints": {"a": t("Subtract the missing corner; do not add it.", "La esquina que falta se resta, no se suma."), "c": t("That is the whole rectangle.", "Ese es el rectángulo completo."), "d": t("That is the missing corner.", "Esa es la esquina que falta.")}, "solution": t("450 − 48 = 402 ft².", "450 − 48 = 402 ft².")},
      "E": {"ok": "c", "hints": {"a": t("The window is not painted: it is subtracted.", "La ventana no se pinta: se resta."), "b": t("Areas are not multiplied by each other.", "Las áreas no se multiplican entre sí."), "d": t("You paint the wall, not the window.", "Se pinta la pared, no la ventana.")}, "solution": t("Subtraction: whole wall minus the window.", "Sustracción: toda la pared menos la ventana.")},
      "F": {"ok": "a", "hints": {"b": t("The triangle's area is divided by 2.", "El área del triángulo se divide entre 2."), "c": t("Check the triangle: (10 × 4) ÷ 2.", "Revise el triángulo: (10 × 4) ÷ 2."), "d": t("Check both pieces again.", "Revise las dos piezas otra vez.")}, "solution": t("60 + 20 = 80 ft².", "60 + 20 = 80 ft².")},
      "G": {"ok": "d", "hints": {"a": t("You added. Multiply the area by the price.", "Sumó. Multiplique el área por el precio."), "b": t("You divided. Multiply.", "Dividió. Multiplique."), "c": t("Check: 300 × 4.", "Revise: 300 × 4.")}, "solution": t("300 × $4 = $1,200.", "300 × $4 = $1,200.")},
      "H": {"ok": "b", "hints": {"a": t("2 gallons cover only 700 ft².", "2 galones cubren solo 700 ft²."), "c": t("You cannot buy part of a gallon.", "No se compra parte de un galón."), "d": t("3 gallons are already enough.", "3 galones ya alcanzan.")}, "solution": t("780 ÷ 350 ≈ 2.23 → 3 gallons.", "780 ÷ 350 ≈ 2.23 → 3 galones.")}
     }}

    quiz = [
     ("A", t("A triangle has a base of 10 ft and a height of 6 ft. What is its area?", "Un triángulo tiene base de 10 ft y altura de 6 ft. ¿Cuál es su área?"), [("a", "60 ft²"), ("b", "16 ft²"), ("c", "30 ft²"), ("d", "32 ft²")]),
     ("B", t("A trapezoid has bases of 8 ft and 4 ft and a height of 5 ft. What is its area?", "Un trapecio tiene bases de 8 ft y 4 ft y altura de 5 ft. ¿Cuál es su área?"), [("a", "30 ft²"), ("b", "60 ft²"), ("c", "40 ft²"), ("d", "17 ft²")]),
     ("C", t("A figure is made of two rectangles: 20 ft × 5 ft and 12 ft × 5 ft. What is its total area?", "Una figura está formada por dos rectángulos: 20 ft × 5 ft y 12 ft × 5 ft. ¿Cuál es su área total?"), [("a", "100 ft²"), ("b", "60 ft²"), ("c", "37 ft²"), ("d", "160 ft²")]),
     ("D", t("A 25 ft × 18 ft yard has an 8 ft × 6 ft corner cut off. What is the usable area?", "Un patio de 25 ft × 18 ft tiene una esquina recortada de 8 ft × 6 ft. ¿Cuál es el área aprovechable?"), [("a", "498 ft²"), ("b", "402 ft²"), ("c", "450 ft²"), ("d", "48 ft²")]),
     ("E", t("You want the area of a wall with a window, to paint it. What do you do?", "Se quiere el área de una pared con una ventana, para pintarla. ¿Qué se hace?"), [("a", t("Add the wall and the window", "Sumar la pared y la ventana")), ("b", t("Multiply the wall by the window", "Multiplicar la pared por la ventana")), ("c", t("Subtract the window from the wall", "Restar la ventana de la pared")), ("d", t("Find only the window", "Calcular solo la ventana"))]),
     ("F", t("A house shape is a 10 ft × 6 ft rectangle with a triangle on top (base 10 ft, height 4 ft). What is its area?", "Una casa es un rectángulo de 10 ft × 6 ft con un triángulo encima (base 10 ft, altura 4 ft). ¿Cuál es su área?"), [("a", "80 ft²"), ("b", "100 ft²"), ("c", "64 ft²"), ("d", "120 ft²")]),
     ("G", t("A 300 ft² room is carpeted at $4 per square foot. What does it cost?", "Un cuarto de 300 ft² se alfombra a $4 por pie cuadrado. ¿Cuánto cuesta?"), [("a", "$304"), ("b", "$75"), ("c", "$1,300"), ("d", "$1,200")]),
     ("H", t("You must paint 780 ft². One gallon covers 350 ft². How many gallons do you buy?", "Hay que pintar 780 ft². Un galón cubre 350 ft². ¿Cuántos galones se compran?"), [("a", t("2 gallons", "2 galones")), ("b", t("3 gallons", "3 galones")), ("c", t("2.23 gallons", "2.23 galones")), ("d", t("4 gallons", "4 galones"))])]

    return B.pagina_leccion(n, 7, t(*TEMA), t(*TIT),
        t("Divide and conquer: the area of L shapes, cut corners, and house fronts by adding or subtracting simple pieces, and the cost of materials.", "Dividir para conquistar: el área de figuras en L, esquinas recortadas y fachadas sumando o restando piezas simples, y el costo de los materiales."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Recall</strong> the area formulas for rectangles, triangles, and trapezoids.", "<strong>Recordar</strong> las fórmulas de área de rectángulos, triángulos y trapecios."),
         t("<strong>Split</strong> a composite figure into simple figures with helper lines.", "<strong>Descomponer</strong> una figura compuesta en figuras simples mediante líneas auxiliares."),
         t("<strong>Use</strong> the addition strategy: add the areas of the pieces.", "<strong>Aplicar</strong> la estrategia de adición: sumar las áreas de las piezas."),
         t("<strong>Use</strong> the subtraction strategy: subtract a missing piece from a bigger rectangle.", "<strong>Aplicar</strong> la estrategia de sustracción: restar el trozo que falta de un rectángulo mayor."),
         t("<strong>Find</strong> the cost of a material (paint, carpet) from the area and a unit price.", "<strong>Calcular</strong> el costo de un material (pintura, alfombra) a partir del área y de un precio por unidad.")],
        secciones,
        (t("Solve four L- or T-shaped figures by addition and three figures with cut corners by subtraction. Then solve three cost problems (paint, carpet, or tile) and two reverse problems: given the total area and one side, find the other side.",
           "Resuelva cuatro figuras en forma de L o de T por adición y tres figuras con esquinas recortadas por sustracción. Después, resuelva tres problemas de costo (pintura, alfombra o losetas) y dos problemas inversos: dada el área total y un lado, halle el otro."),
         t("Measure a room in your home (or use a floor plan). Sketch it, split it into rectangles, find its area in square feet, and estimate what it would cost to carpet it at $4 per square foot.",
           "Mida un cuarto de su casa (o use un plano). Dibújelo, divídalo en rectángulos, calcule su área en pies cuadrados y estime cuánto costaría alfombrarlo a $4 por pie cuadrado.")),
        quiz,
        t("Self-check checklist for composite figures", "Lista de autoevaluación de figuras compuestas"),
        t("Self-check checklist: skills for the area of composite figures", "Lista de autoevaluación: destrezas del área de figuras compuestas"),
        [(t("Split the figure", "Descomponer la figura"), t("I draw the right helper lines on my own and choose the easier strategy.", "Trazo las líneas auxiliares correctas sin ayuda y elijo la estrategia más cómoda."), t("I split the figure with some help.", "Descompongo la figura con algo de apoyo."), t("I do not see how to split the figure.", "No identifico cómo dividir la figura.")),
         (t("Use the formulas", "Aplicar las fórmulas"), t("I use the right formula for each piece and check the result the other way.", "Aplico la fórmula correcta a cada pieza y compruebo el resultado por el otro camino."), t("I use the formulas with help.", "Aplico las fórmulas con apoyo."), t("I mix up the area formulas.", "Confundo las fórmulas de área.")),
         (t("Use it in real life", "Aplicarlo a la vida real"), t("I find the cost of materials and round gallons or rolls up.", "Calculo el costo de los materiales y redondeo hacia arriba los galones o rollos."), t("I find the cost with guidance.", "Calculo el costo con guía."), t("I do not connect the area with the cost.", "No relaciono el área con el costo."))],
        t("<p>This first lesson of Topic 7 added a key geometry skill: splitting a composite figure into simple figures to find its area, by <strong>addition</strong> or by <strong>subtraction</strong>. And it connects right away to real life: floor plans, remodeling budgets, the cost of materials.</p>\n<p>In <strong>Lesson 7.2 · Circumference of a circle</strong> a new figure comes in, different from all the others: the <strong>circle</strong>. You will meet the number <strong>π</strong> (pi), a universal constant that relates the circumference to the diameter, and you will discover it by measuring real objects.</p>",
          "<p>En esta lección de apertura del Tema 7 se incorporó una técnica esencial de la geometría: descomponer una figura compuesta en figuras simples para calcular su área, por <strong>adición</strong> o por <strong>sustracción</strong>. Y se conecta de inmediato con la vida real: planos de viviendas, presupuestos de remodelación, costos de materiales.</p>\n<p>En la <strong>Lección 7.2 · Circunferencia del círculo</strong> entra en juego una figura nueva, distinta de todas las anteriores: el <strong>círculo</strong>. Aparecerá el número <strong>π</strong> (pi), una constante universal que relaciona la circunferencia con el diámetro, y se descubrirá midiendo objetos reales.</p>"),
        ("7-2", ("", t("Lesson 7.2 · Circumference of a circle", "Lección 7.2 · Circunferencia del círculo"))),
        [(t("composite figure", "figura compuesta"), t("A figure made of two or more simple figures.", "Figura formada por dos o más figuras simples.")),
         (t("helper line", "línea auxiliar"), t("A line you draw to split a figure into simple pieces.", "Línea que se traza para dividir una figura en piezas simples.")),
         (t("square unit", "unidad cuadrada"), t("The unit of area: in², ft², yd².", "La unidad del área: in², ft², yd².")),
         (t("unit price", "precio por unidad"), t("The price of each square unit of a material.", "El precio de cada unidad cuadrada de un material."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "u": "ft", "u2": "ft²",
  "ladoL": "Side: ", "baseMay": "Longer base: ", "baseL": "Base: ", "lado": "side",
  "unid": " square units", "alturaNota": "The height (red dashed line) is perpendicular to the base: it is not the slanted side.",
  "figVoz": "Figure with its measurements; area {A}.",
  "nom": {"rect": "rectangle", "cuad": "square", "par": "parallelogram", "tri": "triangle", "trap": "trapezoid"},
  "baQ": "What is the area of this {f}?",
  "baTri": "For the triangle you still need to divide by 2.", "baTrap1": "For the trapezoid you still need to divide by 2.", "baTrap2": "For the trapezoid, add the two bases before you multiply.",
  "baCuad1": "Side squared is side × side, not side × 2.", "baCuad2": "That is the perimeter. The area is side × side.", "baRect": "That is the perimeter. The area is base times height.",
  "estr": [["An L-shaped room that splits easily into two rectangles.", "a", "Split it into two rectangles and add."], ["A rectangular field with a triangle removed from one corner.", "s", "Find the whole rectangle and subtract the triangle."], ["A house drawn as a rectangle with a triangle on top (the roof).", "a", "Rectangle plus triangle: add."], ["A picture frame: a rectangle with a rectangular hole in the middle.", "s", "The big rectangle minus the hole."], ["A rectangular yard with a rectangular pool in the middle; you want the area of the grass.", "s", "The whole yard minus the pool."], ["A T shape made of two rectangles.", "a", "Split it into two rectangles and add."], ["A wall with a window; you want the area to paint.", "s", "The whole wall minus the window."], ["A lot made of a square with a triangle attached to one side.", "a", "Square plus triangle."]],
  "estrQ": " Which strategy is easier?", "estrA": "Addition: split and add", "estrS": "Subtraction: complete and subtract",
  "lVoz": "L shape, {W} by {H}, with a {a} by {b} corner cut out.", "lSubVoz": "The L shape completed with the missing rectangle, in red dashed outline.", "falta": "missing",
  "lf1": "R1 (top): {a1} × {b} = {A1} ft². R2 (bottom): {W} × {hb} = {A2} ft².", "lf2": "Total area: {A1} + {A2} = {T} ft²",
  "ls1": "Whole rectangle: {W} × {H} = {WH} ft². Missing piece: {a} × {b} = {ab} ft².", "ls2": "Area: {WH} − {ab} = {T} ft², the same as by addition.",
  "suQ": "What is the area of this figure, in ft²?", "suS": "Split it into two rectangles: {a1} × {b} = {A1} and {W} × {hb} = {A2}; total {T} ft².", "suP": "That would be the whole rectangle: this figure is missing a corner.",
  "su2Q": "The front of a house is a rectangle {b} ft wide and {h} ft tall, with a triangular roof {ht} ft tall on top. What is its area, in ft²?", "su2Voz": "House: a rectangle with a triangle on top.",
  "su2S": "Rectangle: {b} × {h} = {R}; triangle: ({b} × {ht}) ÷ 2 = {Tr}; total {T} ft².", "su2P": "The triangle's area is divided by 2.",
  "re1Q": "A {W} ft × {H} ft yard has a {a} ft × {b} ft rectangular pool in the middle. How many square feet of grass are there?", "re1S": "{W} × {H} = {WH}; minus {a} × {b} = {ab}: {T} ft².", "re1Voz": "Yard with a pool in the middle.", "re1P": "Subtract the pool; do not add it.",
  "re2Q": "A {W} ft × {H} ft rectangular lot had a triangular corner cut off, with legs of {a} ft and {b} ft. What area is left, in ft²?", "re2S": "{WH} − ({a} × {b}) ÷ 2 = {WH} − {tr} = {T} ft².", "re2Voz": "Lot with a triangular corner cut off.", "re2P": "The missing piece is a triangle: its area is divided by 2.",
  "re3Q": "An L-shaped lot is a {W} ft × {H} ft rectangle missing a {a} ft × {b} ft corner. What is its area, in ft²?", "re3S": "{WH} − {ab} = {T} ft².", "re3Voz": "L-shaped lot.",
  "co1Q": "An L-shaped room measures {W} ft × {H} ft, but it is missing a {a} ft × {b} ft corner. Flooring costs {p} per square foot. How much does it cost to cover the room, in dollars?", "co1S": "Area: {WH} − {ab} = {A} ft²; {A} × {p} = {x}.", "co1P": "You still need to subtract the corner that is not there.",
  "co2Q": "A wall is {L} ft × {H} ft and has {v} {vent} 3 ft × 4 ft. One gallon of paint covers 350 ft². How many gallons must you buy?", "vent1": "window", "vent2": "windows",
  "co2S": "Area to paint: {LH} − {vv} = {A} ft²; {A} ÷ 350 ≈ {q}, round up: {g} gallons.", "co2P1": "If you round down, the paint runs out. Round up.", "co2P2": "The windows are not painted: subtract them.",
  "co3Q": "A triangular garden has a base of {b} ft and a height of {h} ft. Sod costs {p} per square foot. How much does the sod cost, in dollars?", "co3S": "Area: ({b} × {h}) ÷ 2 = {A} ft²; × {p} = {x}.", "co3P": "The triangle's area is divided by 2."
 },
 "es": {
  "u": "ft", "u2": "ft²",
  "ladoL": "Lado: ", "baseMay": "Base mayor: ", "baseL": "Base: ", "lado": "lado",
  "unid": " unidades cuadradas", "alturaNota": "La altura (línea roja punteada) es perpendicular a la base: no es el lado inclinado.",
  "figVoz": "Figura con sus medidas; área {A}.",
  "nom": {"rect": "rectángulo", "cuad": "cuadrado", "par": "paralelogramo", "tri": "triángulo", "trap": "trapecio"},
  "baQ": "¿Cuál es el área de este {f}?",
  "baTri": "En el triángulo falta dividir entre 2.", "baTrap1": "En el trapecio falta dividir entre 2.", "baTrap2": "En el trapecio se suman las dos bases antes de multiplicar.",
  "baCuad1": "Lado al cuadrado es lado × lado, no lado × 2.", "baCuad2": "Ese es el perímetro. El área es lado × lado.", "baRect": "Ese es el perímetro. El área es base por altura.",
  "estr": [["Una habitación en forma de L que se parte fácilmente en dos rectángulos.", "a", "Se parte en dos rectángulos y se suman."], ["Un campo rectangular al que se le quitó un triángulo en una esquina.", "s", "Se calcula el rectángulo completo y se resta el triángulo."], ["Una casa dibujada como un rectángulo con un triángulo encima (el techo).", "a", "Rectángulo más triángulo: se suman."], ["Un marco de fotos: un rectángulo con un hueco rectangular en el centro.", "s", "Rectángulo grande menos el hueco."], ["Un patio rectangular con una piscina rectangular en medio; se quiere el área del césped.", "s", "Todo el patio menos la piscina."], ["Una figura en forma de T formada por dos rectángulos.", "a", "Se parte en dos rectángulos y se suman."], ["Una pared con una ventana; se quiere el área que hay que pintar.", "s", "Toda la pared menos la ventana."], ["Un terreno formado por un cuadrado y un triángulo pegados a un lado.", "a", "Cuadrado más triángulo."]],
  "estrQ": " ¿Qué estrategia es más cómoda?", "estrA": "Adición: partir y sumar", "estrS": "Sustracción: completar y restar",
  "lVoz": "Figura en L de {W} por {H}, con una esquina recortada de {a} por {b}.", "lSubVoz": "La figura en L completada con el rectángulo que falta, con borde rojo punteado.", "falta": "falta",
  "lf1": "R1 (arriba): {a1} × {b} = {A1} ft². R2 (abajo): {W} × {hb} = {A2} ft².", "lf2": "Área total: {A1} + {A2} = {T} ft²",
  "ls1": "Rectángulo completo: {W} × {H} = {WH} ft². Lo que falta: {a} × {b} = {ab} ft².", "ls2": "Área: {WH} − {ab} = {T} ft², lo mismo que por adición.",
  "suQ": "¿Cuál es el área de esta figura, en ft²?", "suS": "Se parte en dos rectángulos: {a1} × {b} = {A1} y {W} × {hb} = {A2}; total {T} ft².", "suP": "Ese sería el rectángulo completo: a esta figura le falta una esquina.",
  "su2Q": "Una fachada es un rectángulo de {b} ft de ancho y {h} ft de alto, con un techo triangular de {ht} ft de altura encima. ¿Cuál es su área, en ft²?", "su2Voz": "Casa: rectángulo con un triángulo encima.",
  "su2S": "Rectángulo: {b} × {h} = {R}; triángulo: ({b} × {ht}) ÷ 2 = {Tr}; total {T} ft².", "su2P": "El área del triángulo se divide entre 2.",
  "re1Q": "Un patio de {W} ft × {H} ft tiene una piscina rectangular de {a} ft × {b} ft en medio. ¿Cuántos pies cuadrados de césped hay?", "re1S": "{W} × {H} = {WH}; menos {a} × {b} = {ab}: {T} ft².", "re1Voz": "Patio con una piscina en medio.", "re1P": "La piscina se resta, no se suma.",
  "re2Q": "A un terreno rectangular de {W} ft × {H} ft se le quitó una esquina triangular con catetos de {a} ft y {b} ft. ¿Cuál es el área que queda, en ft²?", "re2S": "{WH} − ({a} × {b}) ÷ 2 = {WH} − {tr} = {T} ft².", "re2Voz": "Terreno con una esquina triangular recortada.", "re2P": "El trozo que falta es un triángulo: su área se divide entre 2.",
  "re3Q": "Un terreno en forma de L es un rectángulo de {W} ft × {H} ft al que le falta una esquina de {a} ft × {b} ft. ¿Cuál es su área, en ft²?", "re3S": "{WH} − {ab} = {T} ft².", "re3Voz": "Terreno en L.",
  "co1Q": "Un cuarto en forma de L mide {W} ft × {H} ft, pero le falta una esquina de {a} ft × {b} ft. El piso cuesta {p} por pie cuadrado. ¿Cuánto cuesta cubrir el cuarto, en dólares?", "co1S": "Área: {WH} − {ab} = {A} ft²; {A} × {p} = {x}.", "co1P": "Falta restar la esquina que no existe.",
  "co2Q": "Una pared mide {L} ft × {H} ft y tiene {v} {vent} de 3 ft × 4 ft. Un galón de pintura cubre 350 ft². ¿Cuántos galones hay que comprar?", "vent1": "ventana", "vent2": "ventanas",
  "co2S": "Área a pintar: {LH} − {vv} = {A} ft²; {A} ÷ 350 ≈ {q}; se redondea hacia arriba: {g} galones.", "co2P1": "Si se redondea hacia abajo, la pintura no alcanza. Se redondea hacia arriba.", "co2P2": "Las ventanas no se pintan: se restan.",
  "co3Q": "Un jardín triangular tiene una base de {b} ft y una altura de {h} ft. El césped en rollo cuesta {p} por pie cuadrado. ¿Cuánto cuesta el césped, en dólares?", "co3S": "Área: ({b} × {h}) ÷ 2 = {A} ft²; × {p} = {x}.", "co3P": "El área del triángulo se divide entre 2."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }

/* ============ MODULE 1 · basic formulas ============ */
function forma(f, b, h, bm){
  var P, cot = [], ex = [], A, txt;
  if (f === "rect"){ P = [[0,0],[b,0],[b,h],[0,h]]; cot = [[[0,0],[b,0],"b = " + b, 1], [[b,0],[b,h],"h = " + h, 1]]; A = b * h; txt = b + " × " + h + " = " + A; }
  else if (f === "cuad"){ P = [[0,0],[b,0],[b,b],[0,b]]; cot = [[[0,0],[b,0],TXT.lado + " = " + b, 1]]; A = b * b; txt = b + "² = " + b + " × " + b + " = " + A; }
  else if (f === "par"){ var d = Math.max(1, b * 0.3); P = [[0,0],[b,0],[b + d,h],[d,h]]; cot = [[[0,0],[b,0],"b = " + b, 1]]; ex = [{ linea: true, pts: [[d,0],[d,h]] }, { txt: "h = " + h, p: [d + 0.8 + b * 0.08, h / 2] }]; A = b * h; txt = b + " × " + h + " = " + A; }
  else if (f === "tri"){ var c = b * 0.35; P = [[0,0],[b,0],[c,h]]; cot = [[[0,0],[b,0],"b = " + b, 1]]; ex = [{ linea: true, pts: [[c,0],[c,h]] }, { txt: "h = " + h, p: [c + 0.8 + b * 0.08, h / 2.5] }]; A = b * h / 2; txt = "(" + b + " × " + h + ") ÷ 2 = " + nd(A); }
  else { var bb = Math.min(bm, b - 1), o = (b - bb) / 2; P = [[0,0],[b,0],[o + bb,h],[o,h]]; cot = [[[0,0],[b,0],"B = " + b, 1], [[o + bb,h],[o,h],"b = " + bb, 1]]; ex = [{ linea: true, pts: [[o,0],[o,h]] }, { txt: "h = " + h, p: [o + 0.8 + b * 0.08, h / 2] }]; A = (b + bb) * h / 2; txt = "((" + b + " + " + bb + ") × " + h + ") ÷ 2 = " + nd(A); }
  return { svg: figuraSVG([{ pts: P }], cot, F(TXT.figVoz, { A: nd(A) }), ex, 280), A: A, txt: txt };
}
function pintaBA(){
  var f = $("ba-f").value, b = +$("ba-b").value, h = +$("ba-h").value, bm = +$("ba-B").value;
  $("ba-bl").textContent = (f === "cuad" ? TXT.ladoL : (f === "trap" ? TXT.baseMay : TXT.baseL)) + b; $("ba-hv").textContent = h; $("ba-Bv").textContent = Math.min(bm, b - 1);
  $("ba-hc").style.display = f === "cuad" ? "none" : ""; $("ba-Bc").style.display = f === "trap" ? "" : "none";
  var Fm = forma(f, b, h, bm);
  $("ba-svg").innerHTML = Fm.svg;
  $("ba-salida").innerHTML = '<div class="linea veredicto">A = ' + Fm.txt + TXT.unid + '</div>' + (f === "par" || f === "tri" || f === "trap" ? '<div class="linea">' + TXT.alturaNota + '</div>' : "");
}
function genBasica(){
  var f = elige(["rect", "cuad", "par", "tri", "trap"]), b = aleatorio(4, 16), h = aleatorio(3, 12), bm = aleatorio(2, b - 2), Fm = forma(f, b, h, bm), p = [];
  if (f === "tri") p.push({ v: b * h, msg: TXT.baTri });
  if (f === "trap") p.push({ v: (b + Math.min(bm, b - 1)) * h, msg: TXT.baTrap1 }, { v: b * h, msg: TXT.baTrap2 });
  if (f === "cuad") p.push({ v: 2 * b, msg: TXT.baCuad1 }, { v: 4 * b, msg: TXT.baCuad2 });
  if (f === "rect") p.push({ v: 2 * (b + h), msg: TXT.baRect });
  p = p.filter(function(x){ return Math.abs(x.v - Fm.A) > 0.01; });
  return { enun: F(TXT.baQ, { f: TXT.nom[f] }) + Fm.svg, correcta: nd(Fm.A), solucion: "A = " + Fm.txt + ".", evalua: numD(Fm.A, p) };
}

/* ============ MODULE 2 · addition or subtraction ============ */
function genEstrategia(){
  var e = elige(TXT.estr);
  return { enun: e[0] + TXT.estrQ, opciones: [{ html: TXT.estrA, clave: "a" }, { html: TXT.estrS, clave: "s" }], correcta: e[1], enOrden: true, bien: e[2], mal: e[2] };
}

/* ============ MODULES 3 and 4 · the L shape ============ */
function figL(W, H, a, b, modo){
  var u = " " + TXT.u, P = [[0,0],[W,0],[W,H - b],[W - a,H - b],[W - a,H],[0,H]];
  if (modo === "sub") return figuraSVG([{ pts: P }, { pts: [[W - a,H - b],[W,H - b],[W,H],[W - a,H]], fill: "#ffebee", stroke: "#b71c1c", dash: true, sw: 2 }],
    [[[0,0],[W,0],W + u, 1], [[0,H],[0,0],H + u, 1], [[W,H],[W - a,H],a + u, 1], [[W,H - b],[W,H],b + u, 1]], TXT.lSubVoz, [{ txt: TXT.falta, p: [W - a / 2, H - b / 2], col: "#b71c1c" }], 320);
  var cot = [[[0,0],[W,0],W + u, 1], [[0,H],[0,0],H + u, 1], [[W - a,H],[0,H],(W - a) + u, 1], [[W,0],[W,H - b],(H - b) + u, 1], [[W,H - b],[W - a,H - b],a + u, 1], [[W - a,H - b],[W - a,H],b + u, 1]];
  var ex = modo === "add" ? [{ linea: true, pts: [[0,H - b],[W - a,H - b]] }, { txt: "R1", p: [(W - a) / 2, H - b / 2] }, { txt: "R2", p: [W / 2, (H - b) / 2] }] : [];
  return figuraSVG([{ pts: P }], cot, F(TXT.lVoz, { W: W, H: H, a: a, b: b }), ex, 320);
}
function pintaLF(){
  var W = +$("lf-W").value, H = +$("lf-H").value, a = Math.min(+$("lf-a").value, W - 1), b = Math.min(+$("lf-b").value, H - 1);
  $("lf-Wv").textContent = W; $("lf-Hv").textContent = H; $("lf-av").textContent = a; $("lf-bv").textContent = b;
  var A1 = (W - a) * b, A2 = W * (H - b), Tt = A1 + A2;
  $("lf-svg").innerHTML = figL(W, H, a, b, "add");
  $("lf-salida").innerHTML = '<div class="linea">' + F(TXT.lf1, { a1: W - a, b: b, A1: nd(A1), W: W, hb: H - b, A2: nd(A2) }) + '</div><div class="linea veredicto">' + F(TXT.lf2, { A1: nd(A1), A2: nd(A2), T: nd(Tt) }) + '</div>';
  $("ls-svg").innerHTML = figL(W, H, a, b, "sub");
  $("ls-salida").innerHTML = '<div class="linea">' + F(TXT.ls1, { W: W, H: H, WH: nd(W * H), a: a, b: b, ab: nd(a * b) }) + '</div><div class="linea veredicto">' + F(TXT.ls2, { WH: nd(W * H), ab: nd(a * b), T: nd(W * H - a * b) }) + '</div>';
}
function genSuma(){
  var u = " " + TXT.u;
  if (Math.random() < 0.6){
    var W = aleatorio(8, 24), H = aleatorio(8, 24), a = aleatorio(2, W - 3), b = aleatorio(2, H - 3), Tt = W * H - a * b;
    var P = [[0,0],[W,0],[W,H - b],[W - a,H - b],[W - a,H],[0,H]], cot = [[[0,0],[W,0],W + u, 1], [[0,H],[0,0],H + u, 1], [[W - a,H],[0,H],(W - a) + u, 1], [[W,0],[W,H - b],(H - b) + u, 1]];
    return { enun: TXT.suQ + figuraSVG([{ pts: P }], cot, F(TXT.lVoz, { W: W, H: H, a: a, b: b }), [], 300), correcta: nd(Tt),
      solucion: F(TXT.suS, { a1: W - a, b: b, A1: nd((W - a) * b), W: W, hb: H - b, A2: nd(W * (H - b)), T: nd(Tt) }), evalua: numD(Tt, [{ v: W * H, msg: TXT.suP }]) };
  }
  var b2 = 2 * aleatorio(3, 10), h = aleatorio(4, 12), ht = aleatorio(2, 8), T2 = b2 * h + b2 * ht / 2;
  var svgC = figuraSVG([{ pts: [[0,0],[b2,0],[b2,h],[0,h]] }, { pts: [[0,h],[b2,h],[b2 / 2,h + ht]], fill: "#cfd8dc" }], [[[0,0],[b2,0],b2 + u, 1], [[b2,0],[b2,h],h + u, 1]], TXT.su2Voz,
    [{ linea: true, pts: [[b2 / 2,h],[b2 / 2,h + ht]] }, { txt: ht + u, p: [b2 / 2 + b2 * 0.1 + 0.6, h + ht / 2.5] }], 300);
  return { enun: F(TXT.su2Q, { b: b2, h: h, ht: ht }) + svgC, correcta: nd(T2), solucion: F(TXT.su2S, { b: b2, h: h, ht: ht, R: nd(b2 * h), Tr: nd(b2 * ht / 2), T: nd(T2) }), evalua: numD(T2, [{ v: b2 * h + b2 * ht, msg: TXT.su2P }]) };
}
function genResta(){
  var u = " " + TXT.u, tp = aleatorio(1, 3), W = aleatorio(10, 30), H = aleatorio(8, 24), a, b, Tt, enun, sol, svgC, p = [];
  if (tp === 1){ a = aleatorio(2, Math.floor(W / 2)); b = aleatorio(2, Math.floor(H / 2)); Tt = W * H - a * b;
    var o = { W: W, H: H, a: a, b: b, WH: nd(W * H), ab: nd(a * b), T: nd(Tt) }; enun = F(TXT.re1Q, o); sol = F(TXT.re1S, o);
    svgC = figuraSVG([{ pts: [[0,0],[W,0],[W,H],[0,H]], fill: "#c8e6c9" }, { pts: [[W / 2 - a / 2,H / 2 - b / 2],[W / 2 + a / 2,H / 2 - b / 2],[W / 2 + a / 2,H / 2 + b / 2],[W / 2 - a / 2,H / 2 + b / 2]], fill: "#bbdefb", stroke: "#0d47a1" }], [[[0,0],[W,0],W + u, 1], [[W,0],[W,H],H + u, 1]], TXT.re1Voz, [{ txt: a + " × " + b, p: [W / 2, H / 2], col: "#0d47a1" }], 280);
    p.push({ v: W * H + a * b, msg: TXT.re1P }); }
  else if (tp === 2){ a = aleatorio(2, W - 4); b = aleatorio(2, H - 4); Tt = W * H - a * b / 2;
    var o2 = { W: W, H: H, a: a, b: b, WH: nd(W * H), tr: nd(a * b / 2), T: nd(Tt) }; enun = F(TXT.re2Q, o2); sol = F(TXT.re2S, o2);
    svgC = figuraSVG([{ pts: [[0,0],[W,0],[W,H - b],[W - a,H],[0,H]] }, { pts: [[W,H - b],[W,H],[W - a,H]], fill: "#ffebee", stroke: "#b71c1c", dash: true, sw: 2 }], [[[0,0],[W,0],W + u, 1], [[0,H],[0,0],H + u, 1], [[W - a,H],[W,H],a + u, -1], [[W,H],[W,H - b],b + u, -1]], TXT.re2Voz, [], 300);
    p.push({ v: W * H - a * b, msg: TXT.re2P }); }
  else { a = aleatorio(2, W - 3); b = aleatorio(2, H - 3); Tt = W * H - a * b;
    var o3 = { W: W, H: H, a: a, b: b, WH: nd(W * H), ab: nd(a * b), T: nd(Tt) }; enun = F(TXT.re3Q, o3); sol = F(TXT.re3S, o3);
    svgC = figuraSVG([{ pts: [[0,0],[W,0],[W,H - b],[W - a,H - b],[W - a,H],[0,H]] }], [[[0,0],[W,0],W + u, 1], [[0,H],[0,0],H + u, 1], [[W,H - b],[W - a,H - b],a + u, 1], [[W - a,H - b],[W - a,H],b + u, 1]], TXT.re3Voz, [], 300); }
  return { enun: enun + svgC, correcta: nd(Tt), solucion: sol, evalua: numD(Tt, p) };
}

/* ============ MODULE 5 · cost of materials ============ */
function genCosto(){
  var tp = aleatorio(1, 3), res, enun, sol, p = [];
  if (tp === 1){ var W = aleatorio(10, 24), H = aleatorio(10, 20), a = aleatorio(3, W - 4), b = aleatorio(3, H - 4), A = W * H - a * b, pr = elige([2, 3, 3.5, 4, 5.25]); res = A * pr;
    var o = { W: W, H: H, a: a, b: b, p: dinero2(pr), WH: nd(W * H), ab: nd(a * b), A: nd(A), x: dinero(res) }; enun = F(TXT.co1Q, o); sol = F(TXT.co1S, o); p.push({ v: W * H * pr, msg: TXT.co1P }); }
  else if (tp === 2){ var L = aleatorio(10, 40), Hh = aleatorio(8, 12), v = aleatorio(1, 3), Ap = L * Hh - v * 12, g = Math.ceil(Ap / 350); res = g;
    if (Ap % 350 === 0) return genCosto();
    var o2 = { L: L, H: Hh, v: v, vent: v === 1 ? TXT.vent1 : TXT.vent2, LH: nd(L * Hh), vv: v * 12, A: nd(Ap), q: nd(Math.round(Ap / 350 * 100) / 100), g: g }; enun = F(TXT.co2Q, o2); sol = F(TXT.co2S, o2);
    p.push({ v: Math.floor(Ap / 350), msg: TXT.co2P1 }); if (Math.ceil(L * Hh / 350) !== g) p.push({ v: Math.ceil(L * Hh / 350), msg: TXT.co2P2 }); }
  else { var b2 = aleatorio(6, 30), h2 = aleatorio(4, 20), At = b2 * h2 / 2, pc = elige([0.5, 0.75, 1, 1.25]); res = At * pc;
    var o3 = { b: b2, h: h2, A: nd(At), p: dinero2(pc), x: dinero2(res) }; enun = F(TXT.co3Q, o3); sol = F(TXT.co3S, o3); p.push({ v: b2 * h2 * pc, msg: TXT.co3P }); }
  res = Math.round(res * 100) / 100;
  return { enun: enun, correcta: tp === 2 ? String(res) : dinero(res), solucion: sol, evalua: numD(res, p.filter(function(x){ return Math.abs(x.v - res) > 0.01; })) };
}

/* ============ Start ============ */
$("ba-f").addEventListener("change", pintaBA); ["ba-b", "ba-h", "ba-B"].forEach(function(id){ $(id).addEventListener("input", pintaBA); }); pintaBA();
creaPracticaLibre("p1", genBasica);
creaPracticaOM("p2", genEstrategia);
["lf-W", "lf-H", "lf-a", "lf-b"].forEach(function(id){ $(id).addEventListener("input", pintaLF); }); pintaLF();
creaPracticaLibre("p3", genSuma);
creaPracticaLibre("p4", genResta);
creaPracticaLibre("p5", genCosto);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA = ("Type only the number, without units.", "Escriba solo el número, sin unidades.")

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1, idc=None, lab_id=None):
        c = f' id="{idc}"' if idc else ""
        if lab_id:
            return f'<div class="campo" style="flex:1;min-width:150px;"{c}><label for="{i}" id="{lab_id}">{et}</label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
        return f'<div class="campo" style="flex:1;min-width:130px;"{c}><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    mods = [
     (t("basic-formulas", "formulas-basicas"), t("Basic area formulas", "Fórmulas básicas de área"),
      f'''      <table class="reglas">
        <caption>{t("Area formulas (area is always in square units)", "Fórmulas de área (el área va siempre en unidades cuadradas)")}</caption>
        <thead><tr><th scope="col">{t("Figure", "Figura")}</th><th scope="col">{t("Formula", "Fórmula")}</th><th scope="col">{t("In words", "En palabras")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Rectangle", "Rectángulo")}</td><td>A = b × h</td><td>{t("base times height", "base por altura")}</td></tr>
          <tr><td>{t("Square", "Cuadrado")}</td><td>A = s²</td><td>{t("side squared", "lado al cuadrado")}</td></tr>
          <tr><td>{t("Parallelogram", "Paralelogramo")}</td><td>A = b × h</td><td>{t("base times height (the height, not the slanted side)", "base por altura (la altura, no el lado inclinado)")}</td></tr>
          <tr><td>{t("Triangle", "Triángulo")}</td><td>A = (b × h) ÷ 2</td><td>{t("base times height, divided by two", "base por altura, entre dos")}</td></tr>
          <tr><td>{t("Trapezoid", "Trapecio")}</td><td>A = ((B + b) × h) ÷ 2</td><td>{t("sum of the bases times the height, divided by two", "suma de las bases por la altura, entre dos")}</td></tr>
        </tbody>
      </table>
      <h3>{t("Explore each figure", "Explore cada figura")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="ba-f">{t("Figure", "Figura")}</label><select id="ba-f"><option value="rect">{t("Rectangle", "Rectángulo")}</option><option value="cuad">{t("Square", "Cuadrado")}</option><option value="par">{t("Parallelogram", "Paralelogramo")}</option><option value="tri">{t("Triangle", "Triángulo")}</option><option value="trap">{t("Trapezoid", "Trapecio")}</option></select></div>
          {desl("ba-b", t("Base", "Base"), 2, 20, 10, lab_id="ba-bl")}
          {desl("ba-h", t("Height", "Altura"), 2, 15, 6, idc="ba-hc")}
          {desl("ba-B", t("Shorter base", "Base menor"), 1, 19, 5, idc="ba-Bc")}
        </div>
        <div id="ba-svg"></div>
        <div class="salida" id="ba-salida" aria-live="polite"></div>
      </div>
{libre_x("p1", t("Practice: area of basic figures", "Practique: área de figuras básicas"), t("Area", "Área"), t(*NOTA))}'''),
     (t("strategy", "estrategia"), t("What a composite figure is", "Qué es una figura compuesta"),
      f'''      <p>{t("A composite figure is made of two or more simple figures: an L-shaped apartment, a yard with a corner cut off, a house with its roof. You measure it with one simple idea: <strong>divide and conquer</strong>. There are two ways:", "Una figura compuesta está formada por dos o más figuras simples: el plano de un apartamento en L, un patio con una esquina recortada, una casa con su techo. Se mide con una idea sencilla: <strong>dividir para conquistar</strong>. Hay dos caminos:")}</p>
      <table class="reglas">
        <caption>{t("The two strategies", "Las dos estrategias")}</caption>
        <thead><tr><th scope="col">{t("Strategy", "Estrategia")}</th><th scope="col">{t("What you do", "Qué se hace")}</th><th scope="col">{t("Best when…", "Conviene cuando…")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Addition", "Adición")}</td><td>{t("split it into pieces and add their areas", "se parte en piezas y se suman sus áreas")}</td><td>{t("the figure splits easily into pieces", "la figura se divide fácilmente en piezas")}</td></tr>
          <tr><td>{t("Subtraction", "Sustracción")}</td><td>{t("find the whole figure and subtract what is missing", "se calcula la figura completa y se resta lo que falta")}</td><td>{t("the figure is a big one with a piece taken out", "la figura es una grande a la que le quitaron un trozo")}</td></tr>
        </tbody>
      </table>
{B.om("p2", t("Practice: addition or subtraction?", "Practique: ¿adición o sustracción?"))}'''),
     (t("addition", "adicion"), t("The addition strategy", "La estrategia de adición"),
      f'''      <p>{t("Draw a helper line that splits the figure into simple pieces; find each area and add them. If a measurement is missing, figure it out from the others: in an L shape, the missing side is the difference of two sides you know.", "Se traza una línea auxiliar que parte la figura en piezas simples; se calcula cada área y se suman. Si falta alguna medida, se deduce de las otras: en una L, el lado que falta es la diferencia de dos que sí se conocen.")}</p>
      <h3>{t("The L-shaped room", "El cuarto en L")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("lf-W", t("Total width (ft)", "Ancho total (ft)"), 8, 30, 18)}
          {desl("lf-H", t("Total height (ft)", "Alto total (ft)"), 8, 30, 20)}
          {desl("lf-a", t("Cut-out width (ft)", "Recorte, ancho (ft)"), 1, 25, 6)}
          {desl("lf-b", t("Cut-out height (ft)", "Recorte, alto (ft)"), 1, 25, 10)}
        </div>
        <div id="lf-svg"></div>
        <div class="salida" id="lf-salida" aria-live="polite"></div>
      </div>
{libre_x("p3", t("Practice: add the pieces", "Practique: sume las piezas"), t("Area (ft²)", "Área (ft²)"), t(*NOTA))}'''),
     (t("subtraction", "sustraccion"), t("The subtraction strategy", "La estrategia de sustracción"),
      f'''      <p>{t("Imagine the whole figure (almost always a rectangle), find its area, and subtract the missing piece. Here is the same L shape from the module above, done this way:", "Se imagina la figura completa (casi siempre un rectángulo), se calcula su área y se le resta el trozo que falta. La misma L del módulo anterior, por este camino:")}</p>
      <div class="panel">
        <div id="ls-svg"></div>
        <div class="salida" id="ls-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip">{t("Both ways give the same result. If one is clumsy, try the other; and if you have time, use the second one to check the first.", "Los dos caminos dan lo mismo. Si uno resulta engorroso, pruebe el otro; y si tiene tiempo, use el segundo para comprobar el primero.")}</div>
{libre_x("p4", t("Practice: subtract what is missing", "Practique: reste lo que falta"), t("Area (ft²)", "Área (ft²)"), t(*NOTA))}'''),
     (t("cost", "costo"), t("The cost of materials", "El costo de los materiales"),
      f'''      <p>{t("From area to budget: find the area and multiply by the price of each square unit. If the material comes in cans or rolls that cover a fixed amount, divide and <strong>round up</strong>: the store does not sell half a gallon of paint.", "Del área al presupuesto: se calcula el área y se multiplica por el precio de cada unidad cuadrada. Si el material se vende en envases o rollos que cubren una cantidad fija, se divide y se <strong>redondea hacia arriba</strong>: en la tienda no se vende medio galón de pintura.")}</p>
{libre_x("p5", t("Practice: how much does it cost?", "Practique: ¿cuánto cuesta?"), t("Answer", "Resultado"), t("Type only the number; it may have cents.", "Escriba solo el número; puede llevar centavos."))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 7, t(*TEMA), t(*TIT),
        t("Five practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cinco actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/geometry.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Área de figuras compuestas")
