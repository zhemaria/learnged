"""Level 4 · Lesson 6.3 · Graphing systems and modeling — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_6-3.html and algebra/n4-l6-3.html (move the lines and watch the crossing point, from
standard form to the kind of system, translating word problems, and the break-even point). They are rebuilt here, inside LearnGED,
with math/sys4.js. Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4
from build_n4_lesson_6_1 import ESTILO_SIS

B.NIVEL = 4
N = "6-3"
TEMA = ("Systems of linear equations", "Sistemas de ecuaciones lineales")
TIT = ("Graphing systems and modeling", "El método gráfico y el modelado")
SCRIPTS = n4.SCRIPTS + ("/math/sys4.js",)
ESTILO = n4.ESTILO + ESTILO_SIS

def fig_cruce():
    p = n4.Plano(-2, 6, -2, 7, 34, paso=1)
    p.seg((-2, -1), (6, 7), "#1565c0", 3.5).seg((-2, 7), (6, -1), "#c62828", 3.5)
    p.texto((4.4, 4.4), "y = x + 1", "#1565c0", 14, "start", 14, 0).texto((4.3, 1.2), "y = −x + 5", "#c62828", 14, "start", 14, 0)
    p.punto((2, 3), "#2e7d32").texto((2, 3), "(2, 3)", "#2e7d32", 15, "end", -14, 0)
    return p.svg(t("Graph of the lines y = x + 1 and y = negative x + 5, which cross at the point 2, 3.", "Gráfica de las rectas y = x + 1 e y = −x + 5, que se cruzan en el punto 2, 3."), 340)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with Lessons 6.1 and 6.2.</strong> In Lessons 6.1 and 6.2 you solved systems with algebra (substitution and elimination). Now you add a third view: the graph. Seeing both lines on the plane helps you understand why a system has one, no, or infinitely many solutions.", "<strong>Conexión con la lección anterior.</strong> En las Lecciones 6.1 y 6.2 se resolvieron sistemas con álgebra (sustitución y eliminación). Ahora se añade una tercera mirada: el método gráfico. Ver las dos rectas en el plano ayuda a entender por qué un sistema tiene una, ninguna o infinitas soluciones.")}</p>
<p>{t("To solve a system by graphing, graph both lines on the same plane. The point where they cross is the solution of the system: its pair (x, y) works in both equations.", "Para resolver un sistema gráficamente se grafican las dos rectas en el mismo plano. El punto donde se cruzan es la solución del sistema: su par (x, y) cumple las dos ecuaciones.")}</p>
{fig_cruce()}
<p>{t("On the graph, the lines y = x + 1 and y = −x + 5 cross at (2, 3). That is exactly the result substitution or elimination would give.", "En la gráfica, las rectas y = x + 1 e y = −x + 5 se cruzan en (2, 3). Ese es justamente el resultado que daría resolver el sistema por sustitución o eliminación.")}</p>
{practica("p1", t("Practice 1 — Read the crossing", "Práctica 1 — Leer el cruce"), t("Two lines cross at (3, 2). What is the solution of the system?", "Dos rectas se cruzan en (3, 2). ¿Cuál es la solución del sistema?"), [("a", "(2, 3)"), ("b", "(0, 0)"), ("c", "(3, 2)")])}
{practica("p2", t("Practice 2 — Parallel lines", "Práctica 2 — Rectas paralelas"), t("If the two lines are parallel, the system has:", "Si las dos rectas son paralelas, el sistema tiene:"), [("a", t("one solution", "una solución")), ("b", t("no solution", "ninguna solución")), ("c", t("infinitely many solutions", "infinitas soluciones"))])}
{practica("p3", t("Practice 3 — The same line", "Práctica 3 — La misma recta"), t("If both equations graph the same line, there are:", "Si las dos ecuaciones grafican la misma recta, hay:"), [("a", t("no solutions", "ninguna solución")), ("b", t("one solution", "una solución")), ("c", t("infinitely many solutions", "infinitas soluciones"))])}
{enlace(n, t("graph", "grafico"), t("the graphing method", "el método gráfico"), t("Sliders for the slope and the intercept move the two lines and the crossing point, plus new graphs to read the solution.", "Deslizadores de pendiente e intercepto para mover las dos rectas y ver desplazarse el punto de cruce, más gráficas nuevas para leer la solución."))}'''

    s2 = f'''<p>{t("The graph and the algebra tell the same story. The three kinds of system look like this on the plane:", "La gráfica y el álgebra cuentan la misma historia. Los tres tipos de sistema del tema se ven así en el plano:")}</p>
{tabla(t("Graph and kind of system", "Gráfica y tipo de sistema"), t("How the graph matches the kind of system", "Correspondencia entre el aspecto gráfico y el tipo de sistema"), [t("On the graph", "En la gráfica"), t("Kind of system", "Tipo de sistema"), t("Solutions", "Soluciones"), t("Slopes and intercepts", "Pendientes e interceptos")],
  [[t("The lines cross at one point", "Las rectas se cruzan en un punto"), t("Independent", "Independiente"), t("One", "Una"), t("different slopes", "pendientes distintas")], [t("The lines are parallel", "Las rectas son paralelas"), t("Inconsistent", "Inconsistente"), t("None", "Ninguna"), t("same slope, different intercept", "misma pendiente, distinto intercepto")], [t("The lines are the same", "Las rectas coinciden"), t("Dependent", "Dependiente"), t("Infinitely many", "Infinitas"), t("same slope and same intercept", "misma pendiente y mismo intercepto")]])}
{caja("tip", t("Graph to see, solve to be exact", "Graficar para visualizar, resolver para precisar"), t("<p>The graph shows at a glance how many solutions there are; the algebra gives the exact point, especially when it is not a pair of whole numbers. To know the kind without graphing, write each equation as y = mx + b and compare the slopes and the intercepts.</p>", "<p>La gráfica muestra de un vistazo cuántas soluciones hay; el álgebra da el valor exacto del punto, sobre todo cuando no es un par de enteros. Para saber el tipo sin graficar, se escribe cada ecuación como y = mx + b y se comparan las pendientes y los interceptos.</p>"))}
{enlace(n, t("connect", "conectar"), t("the connection between graph and algebra", "la conexión entre gráfica y álgebra"), t("Systems taken from standard form to y = mx + b, comparing slopes and intercepts to know the kind before graphing.", "Sistemas pasados de la forma estándar a y = mx + b, comparando pendientes e interceptos para saber el tipo antes de graficar."))}'''

    s3 = f'''<p>{t("The most important step in a word problem is to define the variables and write two equations from the text.", "El paso más importante en un problema verbal es definir las variables y escribir dos ecuaciones a partir del texto.")}</p>
{tabla(t("Common phrases", "Frases frecuentes"), t("Common phrases and how they are written in algebra", "Frases frecuentes y cómo se escriben en álgebra"), [t("Phrase", "Frase"), t("In algebra", "En álgebra")],
  [[t("the sum of x and y is 10", "la suma de x e y es 10"), "x + y = 10"], [t("their difference is 4", "su diferencia es 4"), "x − y = 4"], [t("a costs $3 more than n", "a cuesta $3 más que n"), "a = n + 3"], [t("a is twice n", "a es el doble de n"), "a = 2n"], [t("two coffees and one tea cost $8", "dos cafés y un té cuestan $8"), "2c + t = 8"]])}
{ejemplo(t("Example 1: an adult ticket costs $3 more than a child ticket. Two adults and three children pay $26. How much is each ticket?", "Ejemplo 1 · Un boleto de adulto cuesta $3 más que uno de niño. Dos adultos y tres niños pagan $26. ¿Cuánto cuesta cada boleto?"),
  [("1", t("Let a be the adult price and c the child price:", "Sea a el precio del adulto y n el del niño:"), t("a = c + 3 and 2a + 3c = 26.", "a = n + 3 y 2a + 3n = 26.")), ("2", t("Substitute:", "Se sustituye:"), t("2(c + 3) + 3c = 26.", "2(n + 3) + 3n = 26.")), ("3", t("Solve:", "Se resuelve:"), t("5c + 6 = 26, c = 4. Then a = 7.", "5n + 6 = 26, n = 4. Entonces a = 7.")),
   ("✓", t("Answer.", "Respuesta."), t("<strong>The child ticket costs $4 and the adult ticket, $7.</strong>", "<strong>El boleto de niño cuesta $4 y el de adulto, $7.</strong>"))])}
{practica("p4", t("Practice 4 — The system", "Práctica 4 — El sistema"), t("“x plus y equals 10; x minus y equals 2.” The system is:", "«x más y es igual a 10; x menos y es igual a 2.» El sistema es:"), [("a", "x + y = 2 ; x − y = 10"), ("b", "x + y = 10 ; x − y = 2"), ("c", "x · y = 10 ; x − y = 2")])}
{practica("p5", t("Practice 5 — $2 more", "Práctica 5 — $2 más"), t("“The adult ticket (a) costs $2 more than the child ticket (c).” The equation is:", "«El boleto de adulto (a) cuesta $2 más que el de niño (n).» La ecuación es:"), [("a", t("a = c + 2", "a = n + 2")), ("b", t("c = a + 2", "n = a + 2")), ("c", t("a + c = 2", "a + n = 2"))])}
{enlace(n, t("translate", "traducir"), t("translating word problems", "la traducción de problemas verbales"), t("The most common phrases on the test with their translation, problems set up step by step, and setting-up exercises.", "Las frases más frecuentes del examen con su traducción, problemas armados paso a paso y ejercicios de planteamiento."))}'''

    s4 = f'''<p>{t("A business has costs (fixed plus variable) and revenue (from sales). The <strong>break-even point</strong> is where costs and revenue are equal: the business neither gains nor loses. It is the solution of the system formed by the cost line and the revenue line.", "Una empresa tiene costos (fijos más variables) e ingresos (por las ventas). El <strong>punto de equilibrio</strong> es donde costos e ingresos se igualan: ni gana ni pierde. Es la solución del sistema formado por la recta de costos y la de ingresos.")}</p>
{ejemplo(t("Example 2: costs are C = 100 + 5x and revenue is R = 10x (x = units sold). What is the break-even point?", "Ejemplo 2 · Los costos son C = 100 + 5x y los ingresos I = 10x (x = unidades vendidas). ¿Cuál es el punto de equilibrio?"),
  [("1", t("Set costs equal to revenue:", "Se igualan costos e ingresos:"), "100 + 5x = 10x."), ("2", t("Solve:", "Se resuelve:"), "100 = 5x, x = 20."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>The break-even point is 20 units.</strong> Below 20 there is a loss; above 20, a profit.", "<strong>El punto de equilibrio es 20 unidades.</strong> Por debajo de 20 hay pérdida; por encima, ganancia."))])}
{caja("ojo", t("Read the break-even point", "Interprete el punto de equilibrio"), t("<p>To the left of the point, costs are greater than revenue (loss); to the right, revenue is greater than costs (profit).</p>", "<p>A la izquierda del punto, los costos superan a los ingresos (pérdida); a la derecha, los ingresos superan a los costos (ganancia).</p>"))}
{practica("p6", t("Practice 6 — The break-even point", "Práctica 6 — El punto de equilibrio"), t("Costs C = 50 + 2x; revenue R = 7x. What is the break-even point (units)?", "Costos C = 50 + 2x ; ingresos I = 7x. ¿Punto de equilibrio (unidades)?"), [("a", "10"), ("b", "5"), ("c", "50")])}
{practica("p7", t("Practice 7 — Selling more", "Práctica 7 — Vender más"), t("If the business sells MORE than the break-even point, it:", "Si vende MÁS que el punto de equilibrio, la empresa:"), [("a", t("loses money", "pierde dinero")), ("b", t("makes money", "gana dinero")), ("c", t("stays the same", "queda igual"))])}
{enlace(n, t("break-even", "equilibrio"), t("the break-even point", "el punto de equilibrio"), t("A simulator with the fixed costs, the cost per unit, and the selling price, with the loss and profit zones marked on the graph.", "Simulador con costos fijos, costo por unidad y precio de venta, con las zonas de pérdida y ganancia marcadas en la gráfica."))}'''

    secciones = [("s-" + t("graph", "grafico"), t("The graphing method", "El método gráfico"), s1),
                 ("s-" + t("connect", "conectar"), t("Connecting the graph and the algebra", "Conectar lo gráfico con lo algebraico"), s2),
                 ("s-" + t("translate", "traducir"), t("Translating a word problem into a system", "Traducir un problema verbal a un sistema"), s3),
                 ("s-" + t("break-even", "equilibrio"), t("Modeling: the break-even point", "Modelado: el punto de equilibrio"), s4)]

    lesson = {"next": t("Lesson 7.1", "Lección 7.1"), "review": t("sections 1 and 3", "las secciones 1 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("The order matters: x first, then y.", "El orden importa: primero x y después y."), "b": t("The lines cross at (3, 2), not at the origin.", "Las rectas se cruzan en (3, 2), no en el origen.")}, "right": t("The crossing point is the solution.", "El punto de cruce es la solución."), "solution": "(3, 2)."},
      "p2": {"ok": "b", "hints": {"a": t("Parallel lines never cross.", "Las rectas paralelas nunca se cruzan."), "c": t("Infinitely many is when the lines are the same.", "Infinitas es cuando las rectas son la misma.")}, "right": t("They never cross: inconsistent.", "Nunca se cruzan: inconsistente."), "solution": t("No solution.", "Ninguna solución.")},
      "p3": {"ok": "c", "hints": {"a": t("The same line has all its points in common.", "La misma recta tiene todos sus puntos en común."), "b": t("They do not cross at just one point: they are on top of each other.", "No se cruzan en un solo punto: están superpuestas.")}, "right": t("Every point of the line works in both.", "Todos los puntos de la recta cumplen las dos."), "solution": t("Infinitely many.", "Infinitas.")},
      "p4": {"ok": "b", "hints": {"a": t("The sum is 10 and the difference is 2.", "La suma es 10 y la diferencia es 2."), "c": t("“Plus” means +, not times.", "«Más» es +, no por.")}, "right": t("x + y = 10 and x − y = 2.", "x + y = 10 y x − y = 2."), "solution": "x + y = 10 ; x − y = 2."},
      "p5": {"ok": "a", "hints": {"b": t("The adult ticket is the more expensive one.", "El de adulto es el más caro."), "c": t("$2 is a difference, not a total.", "$2 es una diferencia, no un total.")}, "right": t("The adult price is the child price plus 2.", "El precio de adulto es el de niño más 2."), "solution": t("a = c + 2.", "a = n + 2.")},
      "p6": {"ok": "a", "hints": {"b": t("50 + 2x = 7x gives 50 = 5x.", "50 + 2x = 7x da 50 = 5x."), "c": t("50 is the fixed cost.", "50 es el costo fijo.")}, "right": t("50 = 5x, x = 10.", "50 = 5x, x = 10."), "solution": "10."},
      "p7": {"ok": "b", "hints": {"a": t("It loses money below the break-even point.", "Pierde dinero por debajo del punto de equilibrio."), "c": t("It stays even only at the break-even point.", "Queda igual solo en el punto de equilibrio.")}, "right": t("To the right, revenue is above costs.", "A la derecha, los ingresos superan a los costos."), "solution": t("It makes money.", "Gana dinero.")},
     },
     "quiz": {
      "A": {"ok": "a", "hints": {"b": t("The order matters: x first.", "El orden importa: primero x."), "c": t("The lines cross at (4, 1).", "Las rectas se cruzan en (4, 1)."), "d": t("They cross, so there is a solution.", "Se cruzan, así que hay solución.")}, "solution": "(4, 1)."},
      "B": {"ok": "c", "hints": {"a": t("Parallel lines never cross.", "Las rectas paralelas nunca se cruzan."), "b": t("Infinitely many is the same line.", "Infinitas es la misma recta."), "d": t("Two lines cross at most once.", "Dos rectas se cruzan a lo sumo una vez.")}, "solution": t("None.", "Ninguna.")},
      "C": {"ok": "a", "hints": {"b": t("They do not cross at only one point.", "No se cruzan en un solo punto."), "c": t("The same line has every point in common.", "La misma recta tiene todos los puntos en común."), "d": t("Two different lines cross at most once.", "Dos rectas distintas se cruzan a lo sumo una vez.")}, "solution": t("Infinitely many.", "Infinitas.")},
      "D": {"ok": "c", "hints": {"a": t("The sum is 12 and the difference is 4.", "La suma es 12 y la diferencia es 4."), "b": t("“Sum” means +.", "«Suma» es +."), "d": t("“Difference” means −.", "«Diferencia» es −.")}, "solution": "x + y = 12 ; x − y = 4."},
      "E": {"ok": "b", "hints": {"a": t("The adult ticket is the bigger one: a = 2c.", "El de adulto es el mayor: a = 2n."), "c": t("“Twice” means multiply by 2.", "«El doble» es multiplicar por 2."), "d": t("2a = c would make the child ticket the bigger one.", "2a = n haría mayor el de niño.")}, "solution": t("a = 2c.", "a = 2n.")},
      "F": {"ok": "d", "hints": {"a": t("Three pencils: 3 goes with p for pencils.", "Tres lápices: el 3 va con l."), "b": t("They cost $7, not 0.", "Cuestan $7, no 0."), "c": t("There are three pencils and two pens.", "Son tres lápices y dos plumas.")}, "solution": t("3p + 2n = 7.", "3l + 2p = 7.")},
      "G": {"ok": "b", "hints": {"a": t("80 + 4x = 12x gives 80 = 8x.", "80 + 4x = 12x da 80 = 8x."), "c": t("80 is the fixed cost.", "80 es el costo fijo."), "d": t("80 = 8x, x = 10.", "80 = 8x, x = 10.")}, "solution": t("10 units.", "10 unidades.")},
      "H": {"ok": "d", "hints": {"a": t("$7 is the adult ticket.", "$7 es el boleto de adulto."), "b": t("$3 is the difference between the tickets.", "$3 es la diferencia entre los boletos."), "c": t("Check: 2(8) + 3(5) = 31, not 26.", "Compruebe: 2(8) + 3(5) = 31, no 26.")}, "solution": "$4."},
     }}

    quiz = [
     ("A", t("Two lines cross at the point (4, 1). The solution of the system is:", "Dos rectas se cruzan en el punto (4, 1). La solución del sistema es:"), [("a", "(4, 1)"), ("b", "(1, 4)"), ("c", "(0, 0)"), ("d", t("no solution", "no hay solución"))]),
     ("B", t("Two parallel lines. How many solutions does the system have?", "Dos rectas paralelas. ¿Cuántas soluciones tiene el sistema?"), [("a", t("one", "una")), ("b", t("infinitely many", "infinitas")), ("c", t("none", "ninguna")), ("d", t("two", "dos"))]),
     ("C", t("Both equations graph the same line. How many solutions?", "Las dos ecuaciones grafican la misma recta. ¿Cuántas soluciones?"), [("a", t("infinitely many", "infinitas")), ("b", t("one", "una")), ("c", t("none", "ninguna")), ("d", t("two", "dos"))]),
     ("D", t("“The sum of two numbers is 12 and their difference is 4.” The system is:", "«La suma de dos números es 12 y su diferencia es 4.» El sistema es:"), [("a", "x + y = 4 ; x − y = 12"), ("b", "x · y = 12 ; x − y = 4"), ("c", "x + y = 12 ; x − y = 4"), ("d", "x + y = 12 ; x · y = 4")]),
     ("E", t("“An adult ticket (a) costs twice as much as a child ticket (c).” The equation is:", "«Un boleto de adulto (a) cuesta el doble que uno de niño (n).» La ecuación es:"), [("a", t("c = 2a", "n = 2a")), ("b", t("a = 2c", "a = 2n")), ("c", t("a + c = 2", "a + n = 2")), ("d", t("2a = c", "2a = n"))]),
     ("F", t("“Three pencils (p) and two pens (n) cost $7.” The equation is:", "«Tres lápices (l) y dos plumas (p) cuestan $7.» La ecuación es:"), [("a", t("2p + 3n = 7", "2l + 3p = 7")), ("b", t("3p + 2n = 0", "3l + 2p = 0")), ("c", t("p + n = 7", "l + p = 7")), ("d", t("3p + 2n = 7", "3l + 2p = 7"))]),
     ("G", t("Costs C = 80 + 4x; revenue R = 12x. What is the break-even point?", "Costos C = 80 + 4x ; ingresos I = 12x. ¿Punto de equilibrio?"), [("a", t("8 units", "8 unidades")), ("b", t("10 units", "10 unidades")), ("c", t("80 units", "80 unidades")), ("d", t("20 units", "20 unidades"))]),
     ("H", t("Two adults and three children pay $26; an adult ticket costs $3 more than a child ticket. How much is the child ticket?", "Dos adultos y tres niños pagan $26; un adulto cuesta $3 más que un niño. ¿Cuánto cuesta el boleto de niño?"), [("a", "$7"), ("b", "$3"), ("c", "$5"), ("d", "$4")])]

    tarea = (t("For your own work, with your notebook, graph paper, and the calculator: (1) The break-even point: a workshop has costs C = 200 + 8x and revenue R = 12x, where x is the number of units sold. Graph both lines, find the break-even point, and shade the loss zone and the profit zone. Do it again with C = 150 + 3x and R = 8x. (2) From the text to the system: define the variables, write the two equations, solve with the method you prefer, and interpret the answer. (a) The sum of two numbers is 30 and their difference is 6. (b) A concert sold 100 tickets, at $12 for adults and $5 for children, and took in $920. (3) Three views, one solution: solve the system y = 2x − 1 and x + y = 5 by graphing, by substitution, and by elimination. Check that all three give the same point and write which one was fastest for you and why. Then do several exercises of each activity on the practice page. About 70 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno, papel cuadriculado y la calculadora: (1) El punto de equilibrio: un taller tiene costos C = 200 + 8x e ingresos I = 12x, donde x es el número de unidades vendidas. Grafique las dos rectas, halle el punto de equilibrio y sombree la zona de pérdida y la de ganancia. Repita con C = 150 + 3x e I = 8x. (2) Del texto al sistema: defina las variables, escriba las dos ecuaciones, resuelva por el método que prefiera e interprete la respuesta. (a) La suma de dos números es 30 y su diferencia es 6. (b) Un concierto vendió 100 entradas, a $12 las de adulto y a $5 las de niño, y recaudó $920. (3) Tres miradas, una solución: resuelva el sistema y = 2x − 1 y x + y = 5 por el método gráfico, por sustitución y por eliminación. Compruebe que los tres dan el mismo punto y escriba cuál le resultó más rápido y por qué. Después haga varios ejercicios de cada actividad de la página de práctica. Unos 70 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("Think of a small business you know (a food stand, a lawn service). Estimate its fixed costs per month, its cost per sale, and its price, and find how many sales it needs to break even.",
               "Piense en un pequeño negocio que conozca (un puesto de comida, un servicio de jardinería). Estime sus costos fijos al mes, su costo por venta y su precio, y halle cuántas ventas necesita para llegar al punto de equilibrio."))

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("Solve systems by graphing, connect the graph with the algebra, translate word problems into systems, and find the break-even point.", "Resuelva sistemas gráficamente, conecte la gráfica con el álgebra, traduzca problemas verbales a sistemas y halle el punto de equilibrio."),
        ("🧮", t("Calculator allowed", "Se permite calculadora")),
        [t("<strong>Solve</strong> a system by graphing and read the crossing point.", "<strong>Resolver</strong> un sistema gráficamente y leer el punto de cruce."),
         t("<strong>Connect</strong> the graph (crossing, parallel, the same line) with the kind of system.", "<strong>Conectar</strong> la gráfica (cruce, paralelas, la misma recta) con el tipo de sistema."),
         t("<strong>Translate</strong> a word problem into a system of two equations.", "<strong>Traducir</strong> un problema verbal a un sistema de dos ecuaciones."),
         t("<strong>Find</strong> and interpret the break-even point of a business.", "<strong>Hallar</strong> e interpretar el punto de equilibrio de un negocio.")],
        secciones, tarea, quiz,
        t("Self-check checklist for graphing and modeling", "Lista de autoevaluación del método gráfico y el modelado"),
        t("Self-check checklist: skills for graphing systems and modeling", "Lista de autoevaluación: destrezas del método gráfico y el modelado"),
        [(t("Graphing and reading the crossing", "Graficar y leer la intersección"), t("I graph both lines accurately and read the crossing point, in the right order.", "Grafico las dos rectas con precisión y leo el punto de cruce en el orden correcto."), t("I graph them, but I read the point with the coordinates swapped.", "Las grafico, pero leo el punto con las coordenadas al revés."), t("I do not graph the lines.", "No grafico las rectas.")),
         (t("Translating the text", "Traducir el texto"), t("I define the variables and write both equations from the text.", "Defino las variables y escribo las dos ecuaciones a partir del texto."), t("I write one of the two equations correctly.", "Escribo bien una de las dos ecuaciones."), t("I do not set up the system.", "No planteo el sistema.")),
         (t("The break-even point", "El punto de equilibrio"), t("I find it and explain the loss and profit zones.", "Lo hallo y explico las zonas de pérdida y ganancia."), t("I find it, but I do not interpret it.", "Lo hallo, pero no lo interpreto."), t("I do not set costs equal to revenue.", "No igualo costos e ingresos."))],
        t("<p>This lesson closes Topic 6 · Systems of linear equations. You solved systems by substitution, elimination, and graphing, classified them, translated word problems into systems, and found the break-even point.</p>\n<p>Topic 7 · Systems of inequalities and functions begins with <strong>Lesson 7.1 · Systems of linear inequalities: graphing the solution region</strong>. Instead of a single crossing point, the solution will be a whole shaded region of the plane.</p>",
          "<p>Con esta lección se cierra el Tema 6 · Sistemas de ecuaciones lineales. Se resolvieron sistemas por sustitución, eliminación y el método gráfico, se clasificaron, se tradujeron problemas verbales a sistemas y se halló el punto de equilibrio.</p>\n<p>El Tema 7 · Sistemas de desigualdades y funciones comienza con la <strong>Lección 7.1 · Sistemas de desigualdades lineales: graficar la región solución</strong>. En lugar de un solo punto de cruce, la solución será toda una región sombreada del plano.</p>"),
        ("7-1", ("", t("Lesson 7.1 · Systems of linear inequalities: graphing the solution region", "Lección 7.1 · Sistemas de desigualdades lineales: graficar la región solución"))),
        [(t("graphing method", "método gráfico"), t("Graphing both lines and reading the point where they cross.", "Graficar las dos rectas y leer el punto donde se cruzan.")),
         (t("slope-intercept form", "forma pendiente-intercepto"), t("y = mx + b: m is the slope and b the y-intercept.", "y = mx + b: m es la pendiente y b el intercepto con el eje y.")),
         (t("break-even point", "punto de equilibrio"), t("Where costs equal revenue: no gain and no loss.", "Donde los costos igualan a los ingresos: ni ganancia ni pérdida.")),
         (t("fixed cost", "costo fijo"), t("A cost that does not change with the number of units (rent, equipment).", "Un costo que no cambia con el número de unidades (renta, equipo)."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
function nz(a, b){ var v; do { v = aleatorio(a, b); } while (!v); return v; }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }
function yMB(m, b){ return "y = " + (m ? terminoXY(m, "x", true) : "") + (b ? (m ? (b < 0 ? " − " + -b : " + " + b) : sg(b)) : (m ? "" : "0")); }
function lineaMB(m, b){ return L3(-m, 1, b, yMB(m, b)); }
function r2(x){ return Math.round(x * 100) / 100; }

/* ===== MODULE 1 · The graphing method ===== */
function grDibuja(){
  var m1 = +$("gr-m1").value, b1 = +$("gr-b1").value, m2 = +$("gr-m2").value, b2 = +$("gr-b2").value;
  $("gr-m1v").textContent = sg(m1); $("gr-b1v").textContent = sg(b1); $("gr-m2v").textContent = sg(m2); $("gr-b2v").textContent = sg(b2);
  var L1 = lineaMB(m1, b1), L2 = lineaMB(m2, b2), r = resuelveSis(L1, L2);
  $("gr-graf").innerHTML = grafSis(L1, L2, {sinPunto: r.tipo === "uno" && (r.x !== Math.round(r.x) || r.y !== Math.round(r.y))});
  $("gr-txt").innerHTML = '<div class="linea">' + (r.tipo === "uno" ? T("The lines cross at ", "Las rectas se cruzan en ") + "<strong>(" + sg(r2(r.x)) + ", " + sg(r2(r.y)) + ")</strong>" + (r.x !== Math.round(r.x) || r.y !== Math.round(r.y) ? T(" (rounded): on the graph it is hard to read exactly; the algebra gives the exact value.", " (redondeado): en la gráfica es difícil de leer con exactitud; el álgebra da el valor exacto.") : T(": one solution (independent).", ": una solución (independiente).")) : r.tipo === "ninguna" ? T("Same slope, different intercept: the lines are parallel. No solution (inconsistent).", "Misma pendiente, distinto intercepto: las rectas son paralelas. Ninguna solución (inconsistente).") : T("Same slope and same intercept: it is the same line. Infinitely many solutions (dependent).", "Misma pendiente y mismo intercepto: es la misma recta. Infinitas soluciones (dependiente).")) + "</div>";
}
["gr-m1", "gr-b1", "gr-m2", "gr-b2"].forEach(function(id){ $(id).addEventListener("input", grDibuja); }); grDibuja();
creaPracticaPar("gq", function(){ var x0 = aleatorio(-5, 5), y0 = aleatorio(-5, 5), m1, m2; do { m1 = elige([-3, -2, -1, 1, 2, 3]); m2 = elige([-2, -1, 0, 1, 2]); } while (m1 === m2);
  var b1 = y0 - m1 * x0, b2 = y0 - m2 * x0, L1 = lineaMB(m1, b1), L2 = lineaMB(m2, b2);
  return {enun: T("Read the solution on the graph: where do the lines cross?", "Lea la solución en la gráfica: ¿dónde se cruzan las rectas?") + grafSis(L1, L2, {sinPunto: true}), x: x0, y: y0, diag: diagSis(L1, L2, {x: x0, y: y0}),
    solucion: T("The lines cross at ", "Las rectas se cruzan en ") + par(x0, y0) + ". " + T("Check: ", "Comprobación: ") + y0 + " = " + m1 + "(" + x0 + ") " + (b1 < 0 ? "− " + -b1 : "+ " + b1) + " ✓."};
});

/* ===== MODULE 2 · From standard form to the kind of system ===== */
function frTxt(n, d){ d = d || 1; if (d < 0){ n = -n; d = -d; } var g = mcd(Math.abs(n), d) || 1; n /= g; d /= g; return d === 1 ? sg(n) : (n < 0 ? "−" : "") + Math.abs(n) + "/" + d; }
function aMB(L){ /* ax + by = c → y = mx + b */ var s = "", mt = frTxt(-L.a, L.b), kt;
  if (L.a) s = (mt === "1" ? "" : mt === "−1" ? "−" : mt.indexOf("/") > 0 ? (mt.charAt(0) === "−" ? "−(" + mt.slice(1) + ")" : "(" + mt + ")") : mt) + "x";
  if (L.c){ kt = frTxt(L.c, L.b); s += s ? (kt.charAt(0) === "−" ? " − " + kt.slice(1) : " + " + kt) : kt; }
  return "y = " + (s || "0"); }
function sisConectar(cl){
  var a = nz(-4, 4), b = elige([1, 2, -1, -2, 3]), x0 = aleatorio(-4, 4), y0 = aleatorio(-4, 4), k = elige([2, 3, -1, -2]), L1, L2;
  if (cl === "ind"){ var S = sisCon(x0, y0, {lim: 4}); return S; }
  if (a < 0 && b < 0){ a = -a; b = -b; }
  var c = a * x0 + b * y0, g = mcd(mcd(Math.abs(a), Math.abs(b)), Math.abs(c)) || 1; L1 = L3(a / g, b / g, c / g); k = elige([2, 3]);
  if (cl === "dep") L2 = L3(k * L1.a, k * L1.b, k * L1.c); else L2 = L3(k * L1.a, k * L1.b, k * (L1.c + nz(-5, 5)));
  if (Math.random() < .5){ var tmp = L1; L1 = L2; L2 = tmp; }
  return [L1, L2];
}
function pasosConectar(S){ var L1 = S[0], L2 = S[1], m1 = -L1.a / L1.b, m2 = -L2.a / L2.b, b1 = L1.c / L1.b, b2 = L2.c / L2.b, cl = Math.abs(m1 - m2) > 1e-9 ? "ind" : Math.abs(b1 - b2) > 1e-9 ? "inc" : "dep";
  return [T("First equation: ", "Primera ecuación: ") + ecTxt(L1) + " → " + aMB(L1) + ". " + T("Slope ", "Pendiente ") + frTxt(-L1.a, L1.b) + T(", intercept ", ", intercepto ") + frTxt(L1.c, L1.b) + ".",
    T("Second equation: ", "Segunda ecuación: ") + ecTxt(L2) + " → " + aMB(L2) + ". " + T("Slope ", "Pendiente ") + frTxt(-L2.a, L2.b) + T(", intercept ", ", intercepto ") + frTxt(L2.c, L2.b) + ".",
    cl === "ind" ? T("The slopes are different: the lines cross at one point.", "Las pendientes son distintas: las rectas se cruzan en un punto.") : cl === "inc" ? T("Same slope, different intercept: parallel lines.", "Misma pendiente, distinto intercepto: rectas paralelas.") : T("Same slope and same intercept: the same line.", "Misma pendiente y mismo intercepto: la misma recta."),
    "<strong>" + {ind: T("Independent: one solution.", "Independiente: una solución."), inc: T("Inconsistent: no solution.", "Inconsistente: ninguna solución."), dep: T("Dependent: infinitely many solutions.", "Dependiente: infinitas soluciones.")}[cl] + "</strong>"]; }
var CN = null;
pasoAPaso4("cn", function(){ CN = sisConectar(elige(["ind", "inc", "dep"])); return {enun: T("What kind of system is ", "¿Qué tipo de sistema es ") + sisHTML(CN[0], CN[1]) + "?", pasos: pasosConectar(CN), inicio: function(){ $("cn-graf").innerHTML = ""; }, fin: function(){ $("cn-graf").innerHTML = grafSis(CN[0], CN[1]); }}; });
var NOMK = {ind: T("Independent: one solution", "Independiente: una solución"), inc: T("Inconsistent: no solution", "Inconsistente: ninguna solución"), dep: T("Dependent: infinitely many solutions", "Dependiente: infinitas soluciones")};
OMR("kq", function(){ var cl = elige(["ind", "inc", "dep"]), S = sisConectar(cl), r = resuelveSis(S[0], S[1]), real = r.tipo === "uno" ? "ind" : r.tipo === "ninguna" ? "inc" : "dep";
  return {enun: T("Without graphing, what kind of system is ", "Sin graficar, ¿qué tipo de sistema es ") + sisHTML(S[0], S[1]) + "?", correcta: real, enOrden: true, opciones: ["ind", "inc", "dep"].map(function(x){ return {clave: x, html: NOMK[x]}; }),
    pista: T("Write each equation as y = mx + b and compare the slopes and the intercepts.", "Escriba cada ecuación como y = mx + b y compare las pendientes y los interceptos."), bien: pasosConectar(S).slice(0, 3).join(" ")};
});

/* ===== MODULE 3 · Translating ===== */
function tradCaso(){
  var tipo = aleatorio(0, 4), s, d, k, a, b, tot;
  if (tipo === 0){ s = aleatorio(8, 30); d = aleatorio(2, 6); return {enun: T("“The sum of two numbers is " + s + " and their difference is " + d + ".” The system is:", "«La suma de dos números es " + s + " y su diferencia es " + d + ".» El sistema es:"), ok: "x + y = " + s + " ; x − y = " + d, mal: ["x + y = " + d + " ; x − y = " + s, "x · y = " + s + " ; x − y = " + d, "x + y = " + s + " ; x · y = " + d], porque: T("“Sum” is + and “difference” is −.", "«Suma» es + y «diferencia» es −.")}; }
  if (tipo === 1){ k = aleatorio(2, 6); return {enun: T("“An adult ticket (a) costs $" + k + " more than a child ticket (c).” The equation is:", "«Un boleto de adulto (a) cuesta $" + k + " más que uno de niño (n).» La ecuación es:"), ok: T("a = c + " + k, "a = n + " + k), mal: [T("c = a + " + k, "n = a + " + k), T("a + c = " + k, "a + n = " + k), T("a = " + k + "c", "a = " + k + "n")], porque: T("The adult ticket is the child ticket plus " + k + ".", "El de adulto es el de niño más " + k + ".")}; }
  if (tipo === 2){ k = elige([2, 3, 4]); var veces = {2: T("twice", "el doble de"), 3: T("three times", "el triple de"), 4: T("four times", "el cuádruple de")}[k]; return {enun: T("“A father's age (f) is " + veces + " his son's age (s).” The equation is:", "«La edad del padre (p) es " + veces + " la edad del hijo (h).» La ecuación es:"), ok: T("f = " + k + "s", "p = " + k + "h"), mal: [T("s = " + k + "f", "h = " + k + "p"), T("f = s + " + k, "p = h + " + k), T("f + s = " + k, "p + h = " + k)], porque: T("The father is the older one: multiply the son's age by " + k + ".", "El padre es el mayor: se multiplica la edad del hijo por " + k + ".")}; }
  if (tipo === 3){ a = aleatorio(2, 5); do { b = aleatorio(1, 4); } while (b === a); tot = aleatorio(10, 40); return {enun: T("“" + a + " notebooks (n) and " + b + " pens (p) cost $" + tot + ".” The equation is:", "«" + a + " cuadernos (c) y " + b + " plumas (p) cuestan $" + tot + ".» La ecuación es:"), ok: T(a + "n + " + (b === 1 ? "" : b) + "p = " + tot, a + "c + " + (b === 1 ? "" : b) + "p = " + tot), mal: [T((b === 1 ? "" : b) + "n + " + a + "p = " + tot, (b === 1 ? "" : b) + "c + " + a + "p = " + tot), T("n + p = " + tot, "c + p = " + tot), T(a + "n + " + (b === 1 ? "" : b) + "p = 0", a + "c + " + (b === 1 ? "" : b) + "p = 0")], porque: T("Each number goes with its own item: " + a + " notebooks, " + b + " pens.", "Cada número va con su artículo: " + a + " cuadernos, " + b + " plumas.")}; }
  tot = aleatorio(10, 40); k = aleatorio(2, 8); return {enun: T("“There are " + tot + " coins in all, and there are " + k + " more dimes (d) than nickels (n).” The system is:", "«Hay " + tot + " monedas en total, y hay " + k + " monedas de 10¢ (d) más que de 5¢ (n).» El sistema es:"), ok: "n + d = " + tot + " ; d = n + " + k, mal: ["n + d = " + tot + " ; n = d + " + k, "n + d = " + k + " ; d = n + " + tot, "5n + 10d = " + tot + " ; d = n + " + k], porque: T("“In all” is the sum; “more dimes than nickels” means d = n + " + k + ".", "«En total» es la suma; «más de 10¢ que de 5¢» significa d = n + " + k + ".")};
}
OMR("tq", function(){ var c = tradCaso(); return {enun: c.enun, correcta: "ok", opciones: [{clave: "ok", html: c.ok}].concat(c.mal.map(function(m, i){ return {clave: "m" + i, html: m}; })), pista: T("Translate one phrase at a time.", "Traduzca una frase a la vez."), bien: c.porque}; });

/* ===== MODULE 4 · The break-even point ===== */
function eqDibuja(){
  var F = +$("pe-f").value, v = +$("pe-v").value, p = +$("pe-p").value;
  $("pe-fv").textContent = F; $("pe-vv").textContent = v; $("pe-pv").textContent = p;
  var W = 470, H = 300, m = 50, out = $("pe-txt");
  if (p <= v){ $("pe-graf").innerHTML = ""; out.innerHTML = '<div class="linea"><strong style="color:#c62828">' + T("The price is not higher than the cost per unit: the business never breaks even. Every sale adds to the loss.", "El precio no supera el costo por unidad: el negocio nunca llega al equilibrio. Cada venta aumenta la pérdida.") + "</strong></div>"; return; }
  var xe = F / (p - v), xmax = Math.max(10, Math.ceil(xe * 2 / 10) * 10), ymax = p * xmax * 1.05, X = function(x){ return m + x / xmax * (W - m - 20); }, Y = function(y){ return H - 40 - y / ymax * (H - 70); };
  var s = '<polygon points="' + X(0) + "," + Y(F) + " " + X(xe) + "," + Y(F + v * xe) + " " + X(0) + "," + Y(0) + '" fill="rgba(198,40,40,.13)"/>' +
    '<polygon points="' + X(xe) + "," + Y(p * xe) + " " + X(xmax) + "," + Y(p * xmax) + " " + X(xmax) + "," + Y(F + v * xmax) + '" fill="rgba(46,125,50,.15)"/>';
  s += '<line x1="' + m + '" y1="' + Y(0) + '" x2="' + (W - 12) + '" y2="' + Y(0) + '" stroke="#263238" stroke-width="2"/><line x1="' + m + '" y1="' + Y(0) + '" x2="' + m + '" y2="16" stroke="#263238" stroke-width="2"/>';
  var pt = xmax / 5, i; for (i = 0; i <= xmax + 1e-9; i += pt) s += '<text x="' + X(i).toFixed(1) + '" y="' + (Y(0) + 16) + '" font-size="11" text-anchor="middle" fill="#455a64">' + Math.round(i) + "</text>";
  var py = Math.pow(10, Math.floor(Math.log10(ymax / 4))); var pp = Math.ceil(ymax / 5 / py) * py; for (i = pp; i < ymax; i += pp) s += '<text x="' + (m - 6) + '" y="' + (Y(i) + 4).toFixed(1) + '" font-size="11" text-anchor="end" fill="#455a64">$' + Math.round(i).toLocaleString("en-US") + "</text>";
  s += '<text x="' + (W - 12) + '" y="' + (Y(0) + 32) + '" font-size="12" text-anchor="end" fill="#263238">' + T("units sold (x)", "unidades vendidas (x)") + "</text>";
  s += '<line x1="' + X(0) + '" y1="' + Y(F) + '" x2="' + X(xmax) + '" y2="' + Y(F + v * xmax) + '" stroke="#c62828" stroke-width="3"/><line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(xmax) + '" y2="' + Y(p * xmax) + '" stroke="#1565c0" stroke-width="3"/>';
  var xw = 160 / (W - m - 20) * xmax; s += '<text x="' + (X(0) + 6) + '" y="' + (Y(F + v * xw) - 9).toFixed(1) + '" font-size="13" font-weight="700" text-anchor="start" fill="#c62828" paint-order="stroke" stroke="#fff" stroke-width="4">' + T("costs", "costos") + " C = " + F + " + " + (v === 1 ? "" : v) + 'x</text><text x="' + (X(xmax) - 4) + '" y="' + (Y(p * xmax) - 8) + '" font-size="13" font-weight="700" text-anchor="end" fill="#1565c0" paint-order="stroke" stroke="#fff" stroke-width="4">' + T("revenue R = ", "ingresos I = ") + p + "x</text>";
  var xl = xe * .3, gl = Y(p * xl) - Y(F + v * xl), ll = gl >= 22 ? [X(xl), (Y(F + v * xl) + Y(p * xl)) / 2 + 5, "middle"] : [X(xe * .6) + 6, Y(p * xe * .6) + 18, "start"], xg = xe + .7 * (xmax - xe), gap = Y(F + v * xg) - Y(p * xg), lg = gap >= 20 ? [X(xg), (Y(F + v * xg) + Y(p * xg)) / 2 + 5, "middle"] : [X((xe + xmax) / 2) - 6, Y(p * (xe + xmax) / 2) - 8, "end"];
  s += '<text x="' + ll[0].toFixed(1) + '" y="' + ll[1].toFixed(1) + '" font-size="13" font-weight="700" fill="#c62828" text-anchor="' + ll[2] + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + T("loss", "pérdida") + '</text><text x="' + lg[0].toFixed(1) + '" y="' + lg[1].toFixed(1) + '" font-size="13" font-weight="700" fill="#2e7d32" text-anchor="' + lg[2] + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + T("profit", "ganancia") + "</text>";
  s += '<circle cx="' + X(xe).toFixed(1) + '" cy="' + Y(p * xe).toFixed(1) + '" r="7" fill="#2e7d32" stroke="#fff" stroke-width="2"/><text x="' + (X(xe) + 10).toFixed(1) + '" y="' + (Y(p * xe) + 24).toFixed(1) + '" font-size="13" font-weight="700" text-anchor="start" fill="#2e7d32" paint-order="stroke" stroke="#fff" stroke-width="4">' + T("break-even", "equilibrio") + " (" + r2(xe) + ", $" + r2(p * xe).toLocaleString("en-US") + ")</text>";
  $("pe-graf").innerHTML = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + T("Costs and revenue: they meet at " + r2(xe) + " units. Before that, a loss; after it, a profit.", "Costos e ingresos: se igualan en " + r2(xe) + " unidades. Antes, pérdida; después, ganancia.") + '" style="display:block;margin:auto;max-width:' + W + 'px;width:100%">' + s + "</svg>";
  out.innerHTML = '<div class="linea">' + F + " + " + (v === 1 ? "" : v) + "x = " + p + "x → " + F + " = " + (p - v === 1 ? "" : p - v) + "x → x = " + r2(xe) + (xe !== Math.round(xe) ? T(" (round up: " + Math.ceil(xe) + " units are needed to stop losing)", " (se redondea hacia arriba: hacen falta " + Math.ceil(xe) + " unidades para dejar de perder)") : "") + ".</div>" +
    '<div class="linea">' + T("Below " + r2(xe) + " units, costs are above revenue: <strong>loss</strong>. Above it: <strong>profit</strong>.", "Por debajo de " + r2(xe) + " unidades, los costos superan a los ingresos: <strong>pérdida</strong>. Por encima: <strong>ganancia</strong>.") + "</div>";
}
["pe-f", "pe-v", "pe-p"].forEach(function(id){ $(id).addEventListener("input", eqDibuja); }); eqDibuja();
OMR("bq", function(){ var v = aleatorio(2, 9), d = aleatorio(2, 8), p = v + d, xe = d * aleatorio(2, 6) * elige([1, 5]), F = d * xe, tipo = aleatorio(0, 2);
  if (tipo === 0) return {enun: T("Costs C = " + F + " + " + v + "x; revenue R = " + p + "x. What is the break-even point (units)?", "Costos C = " + F + " + " + v + "x ; ingresos I = " + p + "x. ¿Punto de equilibrio (unidades)?"), correcta: "ok",
    opciones: [{clave: "ok", html: String(xe)}, {clave: "f", html: String(Math.round(F / p))}, {clave: "c", html: String(F)}, {clave: "s", html: String(Math.round(F / (p + v)))}].filter(function(o, i, l){ return l.map(function(z){ return z.html; }).indexOf(o.html) === i; }),
    pista: T("Set C equal to R and solve for x.", "Iguale C con I y despeje x."), bien: F + " + " + v + "x = " + p + "x → " + F + " = " + d + "x → x = " + xe + "."};
  var k = tipo === 1 ? xe + aleatorio(1, 10) : Math.max(1, xe - aleatorio(1, xe - 1));
  return {enun: T("Costs C = " + F + " + " + v + "x; revenue R = " + p + "x. The break-even point is " + xe + " units. If it sells " + k + " units, the business:", "Costos C = " + F + " + " + v + "x ; ingresos I = " + p + "x. El punto de equilibrio es " + xe + " unidades. Si vende " + k + " unidades, la empresa:"), correcta: tipo === 1 ? "g" : "p", enOrden: true,
    opciones: [{clave: "g", html: T("makes money", "gana dinero")}, {clave: "p", html: T("loses money", "pierde dinero")}, {clave: "i", html: T("stays even", "queda igual")}], pista: T("Is " + k + " above or below " + xe + "?", "¿" + k + " está por encima o por debajo de " + xe + "?"),
    bien: "C = " + F + " + " + v + "(" + k + ") = " + (F + v * k) + "; I = " + p + "(" + k + ") = " + p * k + ". " + (p * k > F + v * k ? T("Revenue is greater: profit of $" + (p * k - F - v * k) + ".", "Los ingresos son mayores: ganancia de $" + (p * k - F - v * k) + ".") : T("Costs are greater: loss of $" + (F + v * k - p * k) + ".", "Los costos son mayores: pérdida de $" + (F + v * k - p * k) + "."))};
});
'''

def practica_pagina():
    n = N
    rango = lambda i, et, mn, mx, st, v, suf="": f'<div class="campo"><label for="{i}">{et}{"" if et.endswith("$") else " "}<output id="{i}v"></output>{suf}</label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"></div>'
    frases = [(t("the sum of x and y is 10", "la suma de x e y es 10"), "x + y = 10"), (t("their difference is 4", "su diferencia es 4"), "x − y = 4"), (t("a costs $3 more than n", "a cuesta $3 más que n"), "a = n + 3"), (t("a is $3 less than n", "a cuesta $3 menos que n"), "a = n − 3"), (t("a is twice n", "a es el doble de n"), "a = 2n"), (t("a is half of n", "a es la mitad de n"), "a = n/2"), (t("two coffees and one tea cost $8", "dos cafés y un té cuestan $8"), "2c + t = 8"), (t("there are 20 coins in all", "hay 20 monedas en total"), "n + d = 20")]
    tabla_fr = (f'<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Common phrases and how they are written in algebra", "Frases frecuentes y cómo se escriben en álgebra")}</caption><thead><tr><th scope="col">{t("Phrase", "Frase")}</th><th scope="col">{t("In algebra", "En álgebra")}</th></tr></thead><tbody>'
                + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in frases) + "</tbody></table></div>")
    mods = [
     (t("graph", "grafico"), t("The graphing method", "El método gráfico"),
      f'''      <p>{t("Move the slope (m) and the y-intercept (b) of each line y = mx + b and watch the crossing point move. When the slopes are equal, the lines are parallel or the same.", "Mueva la pendiente (m) y el intercepto (b) de cada recta y = mx + b y observe cómo se desplaza el punto de cruce. Cuando las pendientes son iguales, las rectas son paralelas o la misma.")}</p>
      <div class="panel"><div class="campos">{rango("gr-m1", t("Blue line: m =", "Recta azul: m ="), -3, 3, 0.5, 1)}{rango("gr-b1", "b =", -6, 6, 1, 1)}{rango("gr-m2", t("Red line: m =", "Recta roja: m ="), -3, 3, 0.5, -1)}{rango("gr-b2", "b =", -6, 6, 1, 5)}</div></div>
      <div id="gr-graf"></div>
{n4.salida("gr-txt")}
{n4.par_libre("gq", t("Practice: read the solution on the graph", "Practique: lea la solución en la gráfica"))}'''),
     (t("connect", "conectar"), t("Connecting the graph and the algebra", "Conectar lo gráfico con lo algebraico"),
      f'''      <p>{t("To know the kind of system before graphing, write each equation as y = mx + b. Different slopes: the lines cross. Same slope and different intercept: parallel. Same slope and same intercept: the same line.", "Para saber el tipo de sistema antes de graficar, se escribe cada ecuación como y = mx + b. Pendientes distintas: las rectas se cruzan. Misma pendiente y distinto intercepto: paralelas. Misma pendiente y mismo intercepto: la misma recta.")}</p>
{n4.pasos("cn", t("Another system", "Otro sistema"))}
      <div id="cn-graf"></div>
{B.om("kq", t("Practice: what kind of system is it?", "Practique: ¿qué tipo de sistema es?"))}'''),
     (t("translate", "traducir"), t("Translating word problems", "Traducir problemas verbales"),
      f'''      <p>{t("The key step is to define the variables and turn each sentence of the text into an equation. These are the phrases that appear most often:", "El paso clave es definir las variables y convertir cada frase del texto en una ecuación. Estas son las frases que más aparecen:")}</p>
{tabla_fr}
      <div class="caja-tip">{t("Watch out for “more than”: “a costs $3 more than n” is a = n + 3, with the 3 added to the smaller one, not 3 + a = n.", "Cuidado con «más que»: «a cuesta $3 más que n» es a = n + 3, sumando el 3 al menor, y no 3 + a = n.")}</div>
{B.om("tq", t("Practice: choose the setup", "Practique: elija el planteamiento"))}'''),
     (t("break-even", "equilibrio"), t("The break-even point", "El punto de equilibrio"),
      f'''      <p>{t("Costs: C = fixed costs + cost per unit · x. Revenue: R = price · x. The break-even point is where C = R.", "Costos: C = costos fijos + costo por unidad · x. Ingresos: I = precio · x. El punto de equilibrio es donde C = I.")}</p>
      <div class="panel"><div class="campos">{rango("pe-f", t("Fixed costs: $", "Costos fijos: $"), 50, 500, 10, 100)}{rango("pe-v", t("Cost per unit: $", "Costo por unidad: $"), 1, 20, 1, 5)}{rango("pe-p", t("Selling price: $", "Precio de venta: $"), 2, 30, 1, 10)}</div></div>
      <div id="pe-graf"></div>
{n4.salida("pe-txt")}
{B.om("bq", t("Practice: find and interpret the break-even point", "Practique: halle e interprete el punto de equilibrio"))}''')]
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try. You may use the calculator.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad. Puede usar la calculadora."),
        mods, LOGICA, estilo=ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "El método gráfico y el modelado")
