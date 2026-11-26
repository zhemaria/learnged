"""Level 4 · Lesson 2.3 · Polynomials: types, adding, subtracting, and multiplying — builds the lesson and its practice page in English and in Spanish.
Sources (GEDparaHispanos): clase_mate4/leccion_2-3.html, algebra/n4-l2-3.html (what a polynomial is) and the interactives
algebra/polinomios_suma_resta, polinomios_monomio_por_polinomio, and polinomios_evaluar. They are rebuilt here, inside LearnGED.
The answers are typed as polynomials (math/poly4.js reads them). Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import bilingue as B
from bilingue import t, practica, enlace, caja, ejemplo, tabla
import n4

B.NIVEL = 4
N = "2-3"
TEMA = ("3D volume and polynomials", "Volumen 3D y polinomios")
TIT = ("Polynomials: types, adding, subtracting, and multiplying", "Polinomios: clasificación, suma, resta y multiplicación básica")
SCRIPTS = n4.SCRIPTS + ("/math/poly4.js",)

def leccion():
    n = N
    s1 = f'''<p>{t("<strong>A link with the first part of Topic 2.</strong> You measured volumes and surfaces with numbers. Now the same measures are written in general form with letters: the perimeter of a lot whose sides are (2x + 1) and (3x − 2) is a <strong>polynomial</strong>. And combining like terms such as 3x² + 5x² is the same idea of “putting together what is alike” that you used to add 3x + 5x in Level 3.",
 "<strong>Conexión con la primera parte del Tema 2.</strong> Se midieron volúmenes y superficies con números. Ahora esas mismas medidas se escriben de forma general con letras: el perímetro de un terreno cuyos lados son (2x + 1) y (3x − 2) es un <strong>polinomio</strong>. Y combinar términos semejantes como 3x² + 5x² es la misma idea de «juntar lo parecido» que ya se usó al sumar 3x + 5x en el Nivel 3.")}</p>
<p>{t("A <strong>polynomial</strong> is an expression made of terms added or subtracted. Each <strong>term</strong> has a coefficient (the number) and a variable part with whole-number exponents that are not negative (like x, x², x³).", "Un <strong>polinomio</strong> es una expresión formada por términos sumados o restados. Cada <strong>término</strong> tiene un coeficiente (el número) y una parte literal con exponentes enteros no negativos (como x, x², x³).")}</p>
<ul><li>{t("The <strong>degree of a term</strong> is the exponent of its variable (in 5x³ the degree is 3; a number alone has degree 0).", "El <strong>grado de un término</strong> es el exponente de su variable (en 5x³ el grado es 3; un número solo tiene grado 0).")}</li>
<li>{t("The <strong>degree of the polynomial</strong> is the largest degree among its terms.", "El <strong>grado del polinomio</strong> es el mayor grado entre sus términos.")}</li>
<li>{t("The <strong>leading coefficient</strong> is the number in the term of highest degree.", "El <strong>coeficiente principal</strong> es el número del término de mayor grado.")}</li>
<li>{t("A polynomial is in <strong>standard form</strong> when its terms go from the highest degree to the lowest.", "Un polinomio está en <strong>forma estándar</strong> cuando sus términos van del mayor grado al menor.")}</li></ul>
{tabla(t("Types of polynomials by number of terms", "Clasificación de los polinomios por número de términos"), t("Name of a polynomial by its number of terms, with an example", "Nombre del polinomio según su número de términos, con un ejemplo"),
  [t("Name", "Nombre"), t("Number of terms", "Número de términos"), t("Example", "Ejemplo")],
  [[t("Monomial", "Monomio"), t("1 term", "1 término"), "5x²"], [t("Binomial", "Binomio"), t("2 terms", "2 términos"), "3x − 7"], [t("Trinomial", "Trinomio"), t("3 terms", "3 términos"), "x² + 4x − 6"]])}
{ejemplo(t("Example 1: name it and find its degree. Look at the polynomial 4x³ − 2x + 7.", "Ejemplo 1 · Clasificar y hallar el grado. Analizar el polinomio 4x³ − 2x + 7."),
  [("1", t("It has 3 terms.", "Tiene 3 términos."), t("It is a <strong>trinomial</strong>.", "Es un <strong>trinomio</strong>.")),
   ("2", t("The largest exponent is 3.", "El mayor exponente es 3."), t("It has <strong>degree 3</strong>.", "Es de <strong>grado 3</strong>.")),
   ("3", t("The number in the degree-3 term is 4.", "El coeficiente del término de grado 3 es 4."), t("The <strong>leading coefficient</strong> is 4.", "El <strong>coeficiente principal</strong> es 4.")),
   ("✓", t("Answer.", "Respuesta."), t("A trinomial of degree 3 with leading coefficient 4.", "Un trinomio de grado 3 con coeficiente principal 4."))])}
{caja("ojo", t("The sign goes with the term", "El signo va con el término"), t("<p>Each sign belongs to the term after it: in 3x − 5 the second term is −5, not 5. And when you see no number in front of x, the coefficient is 1: in x² it is 1 and in −x³ it is −1. Expressions with a negative exponent, a fractional exponent, or x in a denominator (like 5/x) are <strong>not</strong> polynomials.</p>", "<p>Cada signo pertenece al término que le sigue: en 3x − 5 el segundo término es −5, no 5. Y cuando no se ve ningún número delante de la x, el coeficiente es 1: en x² es 1 y en −x³ es −1. Las expresiones con un exponente negativo, con un exponente fraccionario o con la x en un denominador (como 5/x) <strong>no</strong> son polinomios.</p>"))}
{enlace(n, t("what-is", "que-es"), t("what a polynomial is", "qué es un polinomio"), t("Terms, coefficients, degree, standard form, and types.", "Términos, coeficientes, grado, forma estándar y clasificación."))}'''

    s2 = f'''<p>{t("To add or subtract polynomials, combine the <strong>like terms</strong>: the ones with the same variable and the same exponent. Only the coefficients are added or subtracted; the variable part stays the same.", "Para sumar o restar polinomios se combinan los <strong>términos semejantes</strong>: los que tienen la misma variable con el mismo exponente. Solo se suman o restan los coeficientes; la parte literal no cambia.")}</p>
{ejemplo(t("Example 2: adding. Add (3x² + 2x − 5) + (x² − 4x + 1).", "Ejemplo 2 · Suma. Sumar (3x² + 2x − 5) + (x² − 4x + 1)."),
  [("1", t("The x² terms.", "Términos en x²."), "3x² + x² = 4x²."),
   ("2", t("The x terms.", "Términos en x."), "2x + (−4x) = −2x."),
   ("3", t("The numbers.", "Términos constantes."), "−5 + 1 = −4."),
   ("✓", t("Answer.", "Respuesta."), "<strong>4x² − 2x − 4</strong>.")])}
{ejemplo(t("Example 3: subtracting. Subtract (5x² + 3x − 2) − (2x² − x + 4).", "Ejemplo 3 · Resta. Restar (5x² + 3x − 2) − (2x² − x + 4)."),
  [("1", t("The minus sign changes <strong>every</strong> sign of the second polynomial.", "El signo menos cambia <strong>todos</strong> los signos del segundo polinomio."), "5x² + 3x − 2 − 2x² + x − 4."),
   ("2", t("The x² terms.", "Términos en x²."), "5x² − 2x² = 3x²."),
   ("3", t("The x terms and the numbers.", "Términos en x y constantes."), "3x + x = 4x; −2 − 4 = −6."),
   ("✓", t("Answer.", "Respuesta."), "<strong>3x² + 4x − 6</strong>.")])}
{caja("ojo", t("The most common mistake in subtraction", "El error más común en la resta"), t("<p>Forgetting to change the sign of <strong>every</strong> term of the second polynomial. The minus sign reaches each term inside the parentheses, not only the first one. And when you add or subtract, the exponent is copied: 3x² + 5x² = 8x², not 8x⁴.</p>", "<p>Olvidar cambiar el signo de <strong>todos</strong> los términos del segundo polinomio. El signo menos afecta a cada término dentro del paréntesis, no solo al primero. Y al sumar o restar, el exponente se copia: 3x² + 5x² = 8x², no 8x⁴.</p>"))}
{practica("p1", t("Practice 1 — Adding", "Práctica 1 — Suma"), "(x² + 2x) + (3x² + x) = …", [("a", "4x² + 2x"), ("b", "3x² + 3x"), ("c", "4x² + 3x")])}
{practica("p2", t("Practice 2 — Subtracting", "Práctica 2 — Resta"), "(6x − 4) − (2x + 3) = …", [("a", "4x − 7"), ("b", "4x − 1"), ("c", "8x − 7")])}
{practica("p3", t("Practice 3 — Terms that cancel", "Práctica 3 — Términos que se anulan"), "(2x² − 3x + 1) + (x² + 3x − 1) = …", [("a", "3x² − 6x"), ("b", "3x²"), ("c", "3x² + 6x")])}
{enlace(n, t("add-subtract", "suma-resta"), t("adding and subtracting polynomials", "la suma y resta de polinomios"), t("A guided workshop in three steps and typed practice that names the trap when you fall into one.", "Un taller guiado en tres pasos y práctica escrita que nombra la trampa cuando se cae en una."))}'''

    s3 = f'''<p>{t("To multiply a monomial by a polynomial, use the <strong>distributive property</strong>: the monomial multiplies every term of the polynomial. When you multiply the variables, <strong>add the exponents</strong> (the product rule from Level 3): x · x² = x³.", "Para multiplicar un monomio por un polinomio se aplica la <strong>propiedad distributiva</strong>: el monomio multiplica a cada término del polinomio. Al multiplicar las variables se <strong>suman los exponentes</strong> (la regla del producto del Nivel 3): x · x² = x³.")}</p>
<p class="formula" style="text-align:center;font-size:1.3rem;font-weight:700;">a(b + c + d) = ab + ac + ad</p>
{ejemplo(t("Example 4: a monomial times a trinomial. Multiply 3x(2x² − 4x + 5).", "Ejemplo 4 · Monomio por trinomio. Multiplicar 3x(2x² − 4x + 5)."),
  [("1", "3x · 2x² = 6x³", t("(numbers: 3 · 2 = 6; exponents: 1 + 2 = 3).", "(coeficientes: 3 · 2 = 6; exponentes: 1 + 2 = 3).")),
   ("2", "3x · (−4x) = −12x².", ""),
   ("3", "3x · 5 = 15x.", ""),
   ("✓", t("Answer.", "Respuesta."), "<strong>6x³ − 12x² + 15x</strong>.")])}
{ejemplo(t("Example 5: with a negative sign. Multiply −2x²(x³ − 3x).", "Ejemplo 5 · Con signo negativo. Multiplicar −2x²(x³ − 3x)."),
  [("1", "−2x² · x³ = −2x⁵.", ""),
   ("2", "−2x² · (−3x) = 6x³", t("(negative times negative is positive).", "(negativo por negativo da positivo).")),
   ("✓", t("Answer.", "Respuesta."), "<strong>−2x⁵ + 6x³</strong>.")])}
{caja("ojo", t("Two rules at once", "Dos reglas a la vez"), t("<p>When you distribute, watch the sign (negative times negative is positive) and add the exponents of the same variable. Multiplying the numbers and adding the exponents are two separate steps: do not mix them. And the monomial visits <strong>every</strong> term: 5(x + 2) = 5x + 10, not 5x + 2.</p>", "<p>Al distribuir, cuide el signo (negativo por negativo da positivo) y sume los exponentes de las variables iguales. Multiplicar los coeficientes y sumar los exponentes son pasos distintos: no se mezclan. Y el monomio visita a <strong>cada</strong> término: 5(x + 2) = 5x + 10, no 5x + 2.</p>"))}
{practica("p4", t("Practice 4 — A number times a binomial", "Práctica 4 — Un número por un binomio"), "5(x + 2) = …", [("a", "5x + 2"), ("b", "x + 10"), ("c", "5x + 10")])}
{practica("p5", t("Practice 5 — 2x times a binomial", "Práctica 5 — 2x por un binomio"), "2x(x − 3) = …", [("a", "2x² − 6x"), ("b", "2x² − 3"), ("c", "2x − 6x")])}
{practica("p6", t("Practice 6 — x² times a binomial", "Práctica 6 — x² por un binomio"), "x²(x + 4) = …", [("a", "x² + 4x²"), ("b", "x³ + 4x²"), ("c", "x³ + 4x")])}
{enlace(n, t("multiply", "multiplicar"), t("a monomial times a polynomial", "el producto de un monomio por un polinomio"), t("Follow the arrows of the distributive property and practice with typed answers.", "Siga las flechas de la propiedad distributiva y practique con respuestas escritas."))}'''

    s4 = f'''<p>{t("To <strong>evaluate</strong> a polynomial means to put a number in place of the variable and calculate the result. It is useful, for example, to find the actual value of a perimeter written with x once you know x.", "<strong>Evaluar</strong> un polinomio significa sustituir la variable por un valor numérico y calcular el resultado. Es útil, por ejemplo, para hallar el valor concreto de un perímetro algebraico cuando se conoce x.")}</p>
{ejemplo(t("Example 6: evaluate P = 2x² − 3x + 1 when x = 4.", "Ejemplo 6 · Evaluar P = 2x² − 3x + 1 cuando x = 4."),
  [("1", t("Put 4 in place of x.", "Se sustituye x por 4."), "2(4)² − 3(4) + 1."),
   ("2", t("Powers, then products.", "Potencias y productos."), "2(16) − 12 + 1 = 32 − 12 + 1."),
   ("3", t("Add and subtract from left to right.", "Se opera de izquierda a derecha."), "21."),
   ("✓", t("Answer.", "Respuesta."), "<strong>P = 21</strong>.")])}
{caja("ojo", t("Watch the order of operations", "Cuidado con el orden de operaciones"), t("<p>First the exponents, then the multiplications, and last the additions and subtractions. When you put in a negative value, write it in parentheses: (−3)² = 9, not −9.</p>", "<p>Primero los exponentes, luego las multiplicaciones y, por último, las sumas y restas. Al sustituir un valor negativo, conviene escribirlo entre paréntesis: (−3)² = 9, no −9.</p>"))}
{enlace(n, t("evaluate", "evaluar"), t("evaluating a polynomial", "la evaluación de un polinomio"), t("Put a number in place of x step by step, negative numbers included.", "Sustituya la x por un número paso a paso, también por números negativos."))}'''

    secciones = [("s-" + t("what-is", "que-es"), t("What is a polynomial?", "¿Qué es un polinomio?"), s1),
                 ("s-" + t("add-subtract", "suma-resta"), t("Adding and subtracting polynomials", "Suma y resta de polinomios"), s2),
                 ("s-" + t("multiply", "multiplicar"), t("A monomial times a polynomial", "Multiplicación de un monomio por un polinomio"), s3),
                 ("s-" + t("evaluate", "evaluar"), t("Evaluating a polynomial", "Evaluar un polinomio"), s4)]

    lesson = {"next": t("Lesson 3.1", "Lección 3.1"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("Add the x terms too: 2x + x = 3x.", "Sume también los términos en x: 2x + x = 3x."), "b": t("x² + 3x² = 4x² (the x² has an invisible 1).", "x² + 3x² = 4x² (la x² lleva un 1 invisible).")}, "right": "x² + 3x² = 4x², 2x + x = 3x.", "solution": "4x² + 3x."},
      "p2": {"ok": "a", "hints": {"b": t("The minus changes the sign of +3 too: −4 − 3 = −7.", "El menos cambia también el signo de +3: −4 − 3 = −7."), "c": t("It is a subtraction: 6x − 2x = 4x.", "Es una resta: 6x − 2x = 4x.")}, "right": "6x − 2x = 4x, −4 − 3 = −7.", "solution": "4x − 7."},
      "p3": {"ok": "b", "hints": {"a": t("−3x + 3x = 0: the x terms cancel.", "−3x + 3x = 0: los términos en x se anulan."), "c": t("−3x + 3x = 0, not 6x.", "−3x + 3x = 0, no 6x.")}, "right": t("The x terms and the numbers cancel: 3x².", "Los términos en x y los números se anulan: 3x²."), "solution": "3x²."},
      "p4": {"ok": "c", "hints": {"a": t("The 5 must multiply the 2 too.", "El 5 también debe multiplicar al 2."), "b": t("The 5 must multiply the x too.", "El 5 también debe multiplicar a la x.")}, "right": "5 · x + 5 · 2 = 5x + 10.", "solution": "5x + 10."},
      "p5": {"ok": "a", "hints": {"b": t("2x must multiply the −3 too: 2x · (−3) = −6x.", "2x también debe multiplicar al −3: 2x · (−3) = −6x."), "c": t("x · x = x², so 2x · x = 2x².", "x · x = x², así que 2x · x = 2x².")}, "right": "2x · x = 2x², 2x · (−3) = −6x.", "solution": "2x² − 6x."},
      "p6": {"ok": "b", "hints": {"a": t("x² · x = x³ (add the exponents: 2 + 1).", "x² · x = x³ (se suman los exponentes: 2 + 1)."), "c": t("x² · 4 = 4x², not 4x.", "x² · 4 = 4x², no 4x.")}, "right": "x² · x = x³, x² · 4 = 4x².", "solution": "x³ + 4x²."},
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("It has two terms: 7x and −3.", "Tiene dos términos: 7x y −3."), "b": t("A trinomial has three terms.", "Un trinomio tiene tres términos."), "c": t("The largest exponent is 1.", "El mayor exponente es 1.")}, "solution": t("Two terms: a binomial.", "Dos términos: binomio.")},
      "B": {"ok": "b", "hints": {"a": t("The degree is the largest exponent.", "El grado es el mayor exponente."), "c": t("You counted the terms. The degree is the largest exponent.", "Contó los términos. El grado es el mayor exponente."), "d": t("Do not add the exponents: take the largest.", "No se suman los exponentes: se toma el mayor.")}, "solution": t("Degree 4.", "Grado 4.")},
      "C": {"ok": "a", "hints": {"b": t("3x − 5x = −2x.", "3x − 5x = −2x."), "c": t("2x² + x² = 3x².", "2x² + x² = 3x²."), "d": t("The x is kept: 3x − 5x = −2x.", "La x se conserva: 3x − 5x = −2x.")}, "solution": "3x² − 2x."},
      "D": {"ok": "c", "hints": {"a": t("−1 + 6 = 5, not 7.", "6 + (−1) = 5, no 7."), "b": t("4x² + 2x² = 6x².", "4x² + 2x² = 6x²."), "d": t("−x + 3x = +2x.", "−x + 3x = +2x.")}, "solution": "6x² + 2x + 5."},
      "E": {"ok": "b", "hints": {"a": t("The minus changes every sign: +2x becomes −2x.", "El menos cambia todos los signos: +2x pasa a −2x."), "c": t("−3 − (−7) = −3 + 7 = 4.", "−3 − (−7) = −3 + 7 = 4."), "d": t("It is a subtraction: 5x² − x² = 4x².", "Es una resta: 5x² − x² = 4x².")}, "solution": "4x² + 0x + 4 = 4x² + 4."},
      "F": {"ok": "c", "hints": {"a": t("3x must multiply the 4 too.", "3x también debe multiplicar al 4."), "b": t("Multiply the coefficients: 3 · 1 = 3.", "Multiplique los coeficientes: 3 · 1 = 3."), "d": t("3x · x = 3x².", "3x · x = 3x².")}, "solution": "3x² + 12x."},
      "G": {"ok": "a", "hints": {"b": t("x² · x = x³: add the exponents.", "x² · x = x³: se suman los exponentes."), "c": t("2x² · (−5) = −10x².", "2x² · (−5) = −10x²."), "d": t("Multiply: 2 · 3 = 6.", "Multiplique: 2 · 3 = 6.")}, "solution": "6x³ − 10x²."},
      "H": {"ok": "d", "hints": {"a": t("−4x · (−x) = +4x².", "−4x · (−x) = +4x²."), "b": t("−4x · 2x² is negative: −8x³.", "−4x · 2x² es negativo: −8x³."), "c": t("−4x · 3 = −12x.", "−4x · 3 = −12x.")}, "solution": "−8x³ + 4x² − 12x."},
     }}

    quiz = [
     ("A", t("What kind of expression is 7x − 3?", "¿Cómo se clasifica la expresión 7x − 3?"), [("a", t("Monomial", "Monomio")), ("b", t("Trinomial", "Trinomio")), ("c", t("Polynomial of degree 2", "Polinomio de grado 2")), ("d", t("Binomial", "Binomio"))]),
     ("B", t("What is the degree of 5x⁴ − 2x² + x?", "¿Cuál es el grado de 5x⁴ − 2x² + x?"), [("a", "2"), ("b", "4"), ("c", "3"), ("d", "7")]),
     ("C", "(2x² + 3x) + (x² − 5x) = …", [("a", "3x² − 2x"), ("b", "3x² + 8x"), ("c", "2x² − 2x"), ("d", "3x² − 2")]),
     ("D", "(4x² − x + 6) + (2x² + 3x − 1) = …", [("a", "6x² + 2x + 7"), ("b", "2x² + 2x + 5"), ("c", "6x² + 2x + 5"), ("d", "6x² − 2x + 5")]),
     ("E", "(5x² + 2x − 3) − (x² + 2x − 7) = …", [("a", "4x² + 4x − 10"), ("b", "4x² + 4"), ("c", "4x² − 4"), ("d", "6x² + 4x + 4")]),
     ("F", "3x(x + 4) = …", [("a", "3x² + 4"), ("b", "4x² + 12x"), ("c", "3x² + 12x"), ("d", "3x + 12x")]),
     ("G", "2x²(3x − 5) = …", [("a", "6x³ − 10x²"), ("b", "6x² − 10x²"), ("c", "6x³ − 5x²"), ("d", "5x³ − 10x²")]),
     ("H", "−4x(2x² − x + 3) = …", [("a", "−8x³ − 4x² + 12x"), ("b", "8x³ + 4x² − 12x"), ("c", "−8x³ + 4x² + 12x"), ("d", "−8x³ + 4x² − 12x")])]

    tarea = (t("For your own work, with your notebook open: (1) Six polynomials named by their number of terms (monomial, binomial, trinomial) and by their degree. (2) Six additions and subtractions of polynomials. In the subtractions, share the minus sign with every term before you combine the like terms. (3) A triangle whose sides measure (2x + 1), (3x − 2), and (x + 4) feet. Write its perimeter as a simplified polynomial, then evaluate it for x = 4. (4) Six products: three of a monomial times a binomial and three of a monomial times a trinomial. Check the coefficient, the sign, and the sum of the exponents in each term. (5) Four polynomials evaluated at values of x that you choose, at least one of them negative. About 60 minutes; check your work with the checklist of this lesson.",
              "Para hacer por su cuenta, con el cuaderno abierto: (1) Seis polinomios clasificados por su número de términos (monomio, binomio, trinomio) y por su grado. (2) Seis sumas y restas de polinomios. En las restas, reparta el signo menos a todos los términos antes de combinar los semejantes. (3) Un triángulo cuyos lados miden (2x + 1), (3x − 2) y (x + 4) pies. Escriba su perímetro como un polinomio simplificado y después evalúelo para x = 4. (4) Seis productos: tres de monomio por binomio y tres de monomio por trinomio. Revise en cada término el coeficiente, el signo y la suma de los exponentes. (5) Cuatro polinomios evaluados para valores de x que usted elija, al menos uno negativo. Unos 60 minutos; revise su trabajo con la lista de autoevaluación de esta lección."),
             t("A garden is x feet wide and (x + 6) feet long. Write its perimeter and its area as polynomials. Then measure (or imagine) a real garden or room and choose x: evaluate both polynomials and check them against your measures.",
               "Un huerto mide x pies de ancho y (x + 6) pies de largo. Escriba su perímetro y su área como polinomios. Después mida (o imagine) un huerto o una habitación real y elija x: evalúe los dos polinomios y compárelos con sus medidas."))

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("Name polynomials by their terms and degree, add and subtract them, multiply a monomial by a polynomial, and evaluate a polynomial.", "Clasifique polinomios por sus términos y su grado, súmelos y réstelos, multiplique un monomio por un polinomio y evalúe un polinomio."),
        ("✏️", t("Notebook", "Cuaderno")),
        [t("<strong>Name</strong> a polynomial by its number of terms and its degree, and find its leading coefficient.", "<strong>Clasificar</strong> un polinomio por su número de términos y su grado, e identificar su coeficiente principal."),
         t("<strong>Add and subtract</strong> polynomials by combining like terms.", "<strong>Sumar y restar</strong> polinomios combinando términos semejantes."),
         t("<strong>Multiply</strong> a monomial by a polynomial with the distributive property.", "<strong>Multiplicar</strong> un monomio por un polinomio con la propiedad distributiva."),
         t("<strong>Evaluate</strong> a polynomial for a given value of the variable.", "<strong>Evaluar</strong> un polinomio para un valor dado de la variable.")],
        secciones, tarea, quiz,
        t("Self-check checklist for polynomials", "Lista de autoevaluación de polinomios"),
        t("Self-check checklist: skills for naming, adding, subtracting, and multiplying polynomials", "Lista de autoevaluación: destrezas para clasificar, sumar, restar y multiplicar polinomios"),
        [(t("Naming and finding the degree", "Clasificar y hallar el grado"), t("I name the polynomial and its degree and find the leading coefficient.", "Clasifico el polinomio por nombre y grado e identifico el coeficiente principal."), t("I name it by its terms but mix up the degree.", "Lo clasifico por sus términos, pero confundo el grado."), t("I cannot tell a monomial, a binomial, and a trinomial apart.", "No distingo monomio, binomio y trinomio.")),
         (t("Adding and subtracting", "Sumar y restar"), t("I combine like terms correctly in additions and subtractions.", "Combino correctamente los términos semejantes en sumas y restas."), t("I combine like terms but miss a sign in subtraction.", "Combino semejantes, pero fallo un signo en la resta."), t("I combine terms that are not alike.", "Combino términos que no son semejantes.")),
         (t("A monomial times a polynomial", "Monomio por polinomio"), t("I distribute with no sign or exponent mistakes, and I can evaluate the result.", "Distribuyo sin errores de signo ni de exponente y puedo evaluar el resultado."), t("I distribute with sign or exponent mistakes.", "Distribuyo con errores de signo o de exponente."), t("I do not multiply every term.", "No multiplico todos los términos."))],
        t("<p>This lesson closes <strong>Topic 2</strong>. You learned to <strong>name</strong> polynomials (by their number of terms and their degree), to <strong>add and subtract</strong> them by combining like terms, to <strong>multiply</strong> a monomial by a polynomial with the distributive property, and to <strong>evaluate</strong> a polynomial by putting in a value.</p>\n<p><strong>Topic 3 · Multiplying and factoring</strong> starts with <strong>Lesson 3.1 · Multiplying binomials: FOIL and special products</strong>. You will multiply two binomials with the <strong>FOIL</strong> method and use shortcuts like (a + b)² = a² + 2ab + b² and (a + b)(a − b) = a² − b².</p>",
          "<p>Con esta lección se cierra el <strong>Tema 2</strong>. Se aprendió a <strong>clasificar</strong> polinomios (por número de términos y por grado), a <strong>sumarlos y restarlos</strong> combinando términos semejantes, a <strong>multiplicar</strong> un monomio por un polinomio con la propiedad distributiva y a <strong>evaluar</strong> un polinomio sustituyendo un valor.</p>\n<p>El <strong>Tema 3 · Multiplicación y factorización</strong> comienza con la <strong>Lección 3.1 · Multiplicación de binomios: FOIL e identidades notables</strong>. Se multiplicarán dos binomios con el método <strong>FOIL</strong> y se usarán atajos como (a + b)² = a² + 2ab + b² y (a + b)(a − b) = a² − b².</p>"),
        ("3-1", ("", t("Lesson 3.1 · Multiplying binomials: FOIL and special products", "Lección 3.1 · Multiplicación de binomios: FOIL e identidades notables"))),
        [(t("polynomial", "polinomio"), t("Terms added or subtracted, with whole-number exponents that are not negative.", "Términos sumados o restados, con exponentes enteros no negativos.")),
         (t("term", "término"), t("A number, a variable, or a product of them, like 5x³.", "Un número, una variable o un producto de ellos, como 5x³.")),
         (t("like terms", "términos semejantes"), t("Terms with the same variable and the same exponent, like 3x² and −x².", "Términos con la misma variable y el mismo exponente, como 3x² y −x².")),
         (t("degree", "grado"), t("The largest exponent of the variable in the polynomial.", "El mayor exponente de la variable en el polinomio.")),
         (t("leading coefficient", "coeficiente principal"), t("The number in the term of highest degree.", "El número del término de mayor grado."))],
        lesson)

# ---------------- practice page ----------------
LOGICA = r'''
var NOMBRE = {1: T("monomial", "monomio"), 2: T("binomial", "binomio"), 3: T("trinomial", "trinomio")};
function nomP(p){ var k = pTerminos(p); return k <= 3 ? NOMBRE[k] : T("polynomial with " + k + " terms", "polinomio de " + k + " términos"); }
function mon(c, g){ return pMono(c, g); }
function pn(v){ return v < 0 ? "(" + sg(v) + ")" : sg(v); }

/* ===== MODULE 1 · What is a polynomial ===== */
var QE = {orden: null, p: null, modo: "term"};
function qeNuevo(ejemplo){
  if (ejemplo){ QE.p = pDe({3: 4, 1: -2, 0: 7}); QE.orden = [[4, 3], [-2, 1], [7, 0]]; }
  else { QE.p = azarP(aleatorio(1, 4), aleatorio(1, 3) + (Math.random() < .3 ? 1 : 0), 9); QE.orden = baraja(listaTerm(QE.p)); }
  qePinta();
}
function qePinta(){
  var p = QE.p, l = QE.orden, g = pGrado(p), modo = QE.modo;
  var html = l.map(function(t, i){
    var vis = tVis(t[0], t[1], i === 0), est = "";
    if (modo === "term") est = "background:" + ["#e3f2fd", "#fff8e1", "#e8f5e9", "#f3e5f5"][i % 4] + ";border-radius:8px;padding:2px 4px;";
    if (modo === "grado" && t[1] === g) est = "background:#ffe0b2;border-radius:8px;padding:2px 4px;";
    return '<span style="' + est + '">' + vis + "</span>" + (modo === "coef" ? '<sub style="font-size:13px;color:#c62828;font-weight:700;margin-left:2px">' + sg(t[0]) + "</sub>" : "") + (modo === "grado" ? '<sub style="font-size:13px;color:#1565c0;font-weight:700;margin-left:2px">' + t[1] + "</sub>" : "");
  }).join("");
  $("qe-pol").innerHTML = '<span aria-hidden="true">' + html + '</span><span class="sr-only">' + pVoz(p, l) + "</span>";
  var lead = p[g], std = l.every(function(t, i){ return i === 0 || t[1] < l[i - 1][1]; });
  $("qe-info").innerHTML = '<div class="linea">' + T("Terms: ", "Términos: ") + l.length + " → <strong>" + nomP(p) + "</strong></div>" +
    '<div class="linea">' + T("Degree: ", "Grado: ") + "<strong>" + g + "</strong> · " + T("leading coefficient: ", "coeficiente principal: ") + "<strong>" + sg(lead) + "</strong></div>" +
    '<div class="linea">' + (std ? T("It is in standard form (highest degree first).", "Está en forma estándar (el mayor grado primero).") : T("It is not in standard form yet: press “Put in standard form.”", "Todavía no está en forma estándar: pulse «Ordenar en forma estándar».")) + "</div>";
  ["term", "coef", "grado"].forEach(function(k){ $("qe-" + k).setAttribute("aria-pressed", k === modo ? "true" : "false"); });
}
["term", "coef", "grado"].forEach(function(k){ $("qe-" + k).addEventListener("click", function(){ QE.modo = k; qePinta(); }); });
$("qe-otro").addEventListener("click", function(){ qeNuevo(false); });
$("qe-ordena").addEventListener("click", function(){ QE.orden = listaTerm(QE.p); qePinta(); });
$("qe-ej").addEventListener("click", function(){ qeNuevo(true); });
qeNuevo(true);
OMR("qq", function(){
  var tipo = elige(["nombre", "grado", "lider", "espol"]);
  if (tipo === "espol"){
    var c = elige([["x²/2 + 0.5x − 3", true], ["−8", true], ["4x<sup>−2</sup> + 1", false], ["6x<sup>1/2</sup> − x", false], ["5/x + 2", false], ["x³ − x + 1", true], ["3/x²", false], ["0.25x² + x", true]]);
    return {enun: T("Is ", "¿Es ") + c[0] + T(" a polynomial?", " un polinomio?"), correcta: c[1] ? "si" : "no", enOrden: true, opciones: [{clave: "si", html: T("Yes", "Sí")}, {clave: "no", html: "No"}],
      pista: T("The exponents of x must be whole numbers that are not negative; x cannot be in a denominator. The coefficients may be fractions or decimals.", "Los exponentes de la x deben ser enteros no negativos; la x no puede estar en un denominador. Los coeficientes sí pueden ser fracciones o decimales."), bien: c[1] ? T("Yes: every exponent is a whole number, 0 or more.", "Sí: todos los exponentes son enteros, 0 o más.") : T("No: there is a negative or fractional exponent, or x in a denominator.", "No: hay un exponente negativo o fraccionario, o la x en un denominador.")};
  }
  var p = azarP(aleatorio(1, 5), aleatorio(1, 3), 9), orden = baraja(listaTerm(p)), g = pGrado(p), lead = p[g], vis = pHTML(p, orden);
  if (tipo === "nombre"){ var k = pTerminos(p), ok = NOMBRE[k] + T(" of degree ", " de grado ") + g;
    var ops = [ok, NOMBRE[k] + T(" of degree ", " de grado ") + (g + 1), NOMBRE[k === 3 ? 2 : k + 1] + T(" of degree ", " de grado ") + g, NOMBRE[k === 1 ? 3 : k - 1] + T(" of degree ", " de grado ") + Math.max(1, g - 1)];
    return {enun: T("Name the polynomial ", "Clasifique el polinomio ") + vis + T(" by its terms and its degree.", " por sus términos y su grado."), correcta: ok, opciones: ops.map(function(o){ return {clave: o, html: o}; }),
      pista: T("Count the terms first; then look for the largest exponent.", "Primero cuente los términos; después busque el mayor exponente."), bien: ok + "."}; }
  if (tipo === "grado") return {enun: T("What is the degree of ", "¿Cuál es el grado de ") + vis + "?", correcta: String(g), opciones: [g, g + 1, Math.max(0, g - 1), pTerminos(p) === g ? g + 2 : pTerminos(p)].map(function(x){ return {clave: String(x), html: String(x)}; }),
    pista: T("The degree is the largest exponent, wherever that term is written.", "El grado es el mayor exponente, esté donde esté escrito ese término."), bien: T("The largest exponent is ", "El mayor exponente es ") + g + "."};
  var otros = orden.filter(function(t){ return t[1] !== g; }).map(function(t){ return t[0]; });
  return {enun: T("What is the leading coefficient of ", "¿Cuál es el coeficiente principal de ") + vis + "?", correcta: String(lead), opciones: [lead, -lead, orden[0][0], otros.length ? otros[0] : lead + 1, g].map(function(x){ return {clave: String(x), html: sg(x)}; }),
    pista: T("Find the term with the largest exponent; its number (with its sign) is the leading coefficient. It is not always the first one written.", "Busque el término con el mayor exponente; su número (con su signo) es el coeficiente principal. No siempre es el primero que aparece escrito."), bien: T("The term of degree ", "El término de grado ") + g + T(" has the number ", " lleva el número ") + sg(lead) + "."};
});

/* ===== MODULE 2 · Adding and subtracting ===== */
function casoSR(){
  var resta = Math.random() < .5, g = elige([1, 2, 2]), a = azarP(g, g + 1, 9), b = azarP(g, aleatorio(2, g + 1), 9);
  var r = resta ? pResta(a, b) : pSuma(a, b), quitado = resta ? pEsc(b, -1) : b;
  var enun = "(" + pVis(a) + ") " + (resta ? "−" : "+") + " (" + pVis(b) + ")", voz = "(" + pVoz(a) + ") " + (resta ? T(" minus ", " menos ") : T(" plus ", " más ")) + " (" + pVoz(b) + ")";
  var fam = []; for (var k = Math.max(a.length, b.length) - 1; k >= 0; k--){ var x = a[k] || 0, y = quitado[k] || 0; if (x || y) fam.push([k, x, y]); }
  var COLF = ["#e3f2fd", "#fff8e1", "#e8f5e9"];
  var pasos = [(resta ? T("Remove the parentheses. The minus sign changes <strong>every</strong> sign of the second polynomial: ", "Se quitan los paréntesis. El signo menos cambia <strong>todos</strong> los signos del segundo polinomio: ") : T("Remove the parentheses (with a plus sign, nothing changes): ", "Se quitan los paréntesis (con un signo más, nada cambia): ")) + pVis(a) + pVis(quitado).replace(/^(?!−)/, " + ").replace(/^−/, " − ") + ".",
    T("Group each family of like terms: ", "Se agrupa cada familia de términos semejantes: ") + fam.map(function(f, i){ return '<span style="background:' + COLF[i % 3] + ';border-radius:6px;padding:1px 4px">' + [f[1] ? tVis(f[1], f[0], true) : "", f[2] ? tVis(f[2], f[0], !f[1]) : ""].join("") + "</span>"; }).join("  ") + ".",
    T("Combine each family (only the numbers; the x part is copied): ", "Se combina cada familia (solo los números; la parte con x se copia): ") + "<strong>" + pVis(r) + "</strong>."];
  return {a: a, b: b, r: r, resta: resta, enun: '<span aria-hidden="true">' + enun + '</span><span class="sr-only">' + voz + "</span>", pasos: pasos};
}
pasoAPaso4("sr", function(){ var c = casoSR(); return {enun: T("Simplify: ", "Simplifique: ") + c.enun, pasos: c.pasos}; });
creaPracticaLibre("sq", function(){
  var c = casoSR(), trampas = [];
  if (c.resta){ var gb = pGrado(c.b), lead = pMono(c.b[gb], gb), soloPrimero = pSuma(pResta(c.a, lead), pResta(c.b, lead)); trampas.push({p: soloPrimero, msg: T("Trap 3: the minus sign changes the sign of every term of the second polynomial, not only the first one.", "Trampa 3: el signo menos cambia el signo de todos los términos del segundo polinomio, no solo el del primero.")}); trampas.push({p: pSuma(c.a, c.b), msg: T("It is a subtraction: change the signs of the second polynomial.", "Es una resta: cambie los signos del segundo polinomio.")}); }
  var dobles = []; c.r.forEach(function(x, i){ if (x) dobles[2 * i] = x; }); for (var i = 0; i < dobles.length; i++) dobles[i] = dobles[i] || 0;
  trampas.push({p: dobles, msg: T("Trap 1: when you add or subtract, the exponent is copied. Exponents are added only when you multiply.", "Trampa 1: al sumar o restar, el exponente se copia. Los exponentes solo se suman al multiplicar.")});
  return {enun: T("Simplify ", "Simplifique ") + c.enun + T(". Use ^ for exponents: x^2.", ". Use ^ para los exponentes: x^2."), evalua: function(txt){ return evaluaP(txt, c.r, trampas, function(p){ return pTerminos(p) < pTerminos(c.r) ? T("A term is missing: each family of like terms gives one term.", "Falta un término: cada familia de términos semejantes da un término.") : null; }); },
    solucion: c.pasos.join(" ")};
});

/* ===== MODULE 3 · A monomial times a polynomial ===== */
function casoMP(){
  var c = elige([-5, -4, -3, -2, -1, 2, 3, 4, 5, 6]), g = aleatorio(0, 3), q = azarP(aleatorio(1, 3), aleatorio(2, 3), 7), m = pMono(c, g), r = pMul(m, q);
  var mVis = tVis(c, g, true), lista = listaTerm(q);
  var pasos = lista.map(function(t){ var cc = c * t[0], gg = g + t[1]; return mVis + " · " + (t[0] < 0 ? "(" + tVis(t[0], t[1], true) + ")" : tVis(t[0], t[1], true)) + " = " + tVis(cc, gg, true) + ' <span class="nota">(' + T("numbers: ", "números: ") + pn(c) + " · " + pn(t[0]) + " = " + sg(cc) + "; " + T("exponents: ", "exponentes: ") + g + " + " + t[1] + " = " + gg + ")</span>"; });
  pasos.push(T("Put the pieces together: ", "Se juntan los resultados: ") + "<strong>" + pVis(r) + "</strong>.");
  return {c: c, g: g, q: q, m: m, r: r, enun: '<span aria-hidden="true">' + mVis + "(" + pVis(q) + ')</span><span class="sr-only">' + pVoz(m) + T(" times ", " por ") + "(" + pVoz(q) + ")</span>", pasos: pasos};
}
pasoAPaso4("mp", function(){ var c = casoMP(); return {enun: T("Multiply: ", "Multiplique: ") + c.enun, pasos: c.pasos}; });
creaPracticaLibre("mq", function(){
  var k = casoMP(), lst = listaTerm(k.q), trampas = [];
  trampas.push({p: pSuma(pMul(k.m, pMono(lst[0][0], lst[0][1])), pResta(k.q, pMono(lst[0][0], lst[0][1]))), msg: T("Trap 1: the monomial must multiply every term, not only the first.", "Trampa 1: el monomio debe multiplicar a todos los términos, no solo al primero.")});
  var expMal = {}; lst.forEach(function(t){ var gg = k.g * t[1]; expMal[gg] = (expMal[gg] || 0) + k.c * t[0]; }); if (k.g > 1) trampas.push({p: pDe(expMal), msg: T("Trap 3: when you multiply powers of x, the exponents are added, not multiplied.", "Trampa 3: al multiplicar potencias de x, los exponentes se suman, no se multiplican.")});
  var coefMal = {}; lst.forEach(function(t){ coefMal[k.g + t[1]] = (coefMal[k.g + t[1]] || 0) + (t[1] && k.g ? k.c + t[0] : k.c * t[0]); }); trampas.push({p: pDe(coefMal), msg: T("Trap 4: the numbers are multiplied, not added.", "Trampa 4: los números se multiplican, no se suman.")});
  var signoMal = {}; lst.forEach(function(t){ signoMal[k.g + t[1]] = Math.abs(k.c * t[0]) * (k.c < 0 && t[0] < 0 ? -1 : (k.c * t[0] < 0 ? -1 : 1)); }); if (k.c < 0) trampas.push({p: pDe(signoMal), msg: T("Trap 2: negative times negative is positive.", "Trampa 2: negativo por negativo da positivo.")});
  return {enun: T("Multiply ", "Multiplique ") + k.enun + T(". Use ^ for exponents: x^3.", ". Use ^ para los exponentes: x^3."), evalua: function(txt){ return evaluaP(txt, k.r, trampas.filter(function(t){ return !pIgual(t.p, k.r); })); }, solucion: k.pasos.join(" ").replace(/<span class="nota">|<\/span>/g, "")};
});

/* ===== MODULE 4 · Evaluating ===== */
function casoEv(){
  var p = azarP(aleatorio(1, 3), aleatorio(2, 3), 6), x = elige([-3, -2, -1, 1, 2, 3, 4, 5]), l = listaTerm(p);
  var sust = l.map(function(t, i){ var a = Math.abs(t[0]), s = t[0] < 0 ? (i ? " − " : "−") : (i ? " + " : ""); return s + (t[1] === 0 ? a : (a === 1 ? "" : a) + "(" + sg(x) + ")" + (t[1] > 1 ? "<sup>" + t[1] + "</sup>" : "")); }).join("");
  var pots = l.map(function(t, i){ var a = Math.abs(t[0]), s = t[0] < 0 ? (i ? " − " : "−") : (i ? " + " : ""); return s + (t[1] === 0 ? a : (a === 1 ? "" : a) + "(" + sg(Math.pow(x, t[1])) + ")"); }).join("");
  var prods = l.map(function(t, i){ var v = t[0] * Math.pow(x, t[1]); return i ? (v < 0 ? " − " + Math.abs(v) : " + " + v) : sg(v); }).join("");
  var val = pEval(p, x);
  return {p: p, x: x, val: val, pasos: [T("Put ", "Se sustituye la x por ") + pn(x) + T(" in place of x (in parentheses): ", " (entre paréntesis): ") + sust + "."].concat(pGrado(p) > 1 ? [T("Powers first: ", "Primero las potencias: ") + pots + "."] : []).concat([T("Then the multiplications: ", "Después las multiplicaciones: ") + prods + ".", T("Add and subtract from left to right: ", "Se suma y se resta de izquierda a derecha: ") + "<strong>" + sg(val) + "</strong>."]),
    malo: l.reduce(function(s, t){ return s + t[0] * (t[1] % 2 === 0 && x < 0 ? -Math.pow(-x, t[1]) : Math.pow(x, t[1])); }, 0)};
}
pasoAPaso4("ev", function(){ var c = casoEv(); return {enun: T("Evaluate ", "Evalúe ") + pHTML(c.p) + T(" when x = ", " cuando x = ") + sg(c.x) + ".", pasos: c.pasos}; });
creaPracticaLibre("eq", function(){
  var c = casoEv();
  return {enun: T("Evaluate ", "Evalúe ") + pHTML(c.p) + T(" when x = ", " cuando x = ") + sg(c.x) + ".",
    evalua: function(txt){ var v = leeEntero(txt); if (v === null) return {estado: "invalido", msg: T("Type a whole number, like −7 or 12.", "Escriba un número entero, como −7 o 12.")};
      if (v === c.val) return {estado: "bien"}; if (c.malo !== c.val && v === c.malo) return {estado: "mal", msg: T("Write the negative value in parentheses: (−3)² = 9, not −9.", "Escriba el valor negativo entre paréntesis: (−3)² = 9, no −9.")};
      return {estado: "mal", msg: T("Follow the order: powers, then multiplications, then additions and subtractions.", "Siga el orden: potencias, después multiplicaciones y, al final, sumas y restas.")}; },
    solucion: c.pasos.join(" ")};
});
'''

def practica_pagina():
    n = N
    libre = lambda pid, tit, et, nota=None: B.libre(pid, tit, et, nota=False).replace('inputmode="decimal" ', "") + (f'\n      <p class="nota">{nota}</p>' if nota else "")
    tabla_trampas = lambda filas: '<div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">' + t("The most common traps", "Las trampas más frecuentes") + '</caption><thead><tr><th scope="col">#</th><th scope="col">' + t("Wrong", "Incorrecto") + '</th><th scope="col">' + t("Right", "Correcto") + '</th><th scope="col">' + t("Why", "Por qué") + '</th></tr></thead><tbody>' + "".join(f"<tr><td>{i + 1}</td><td>✗ {a}</td><td>✓ {b}</td><td>{c}</td></tr>" for i, (a, b, c) in enumerate(filas)) + '</tbody></table></div>'
    mods = [
     (t("what-is", "que-es"), t("What is a polynomial?", "¿Qué es un polinomio?"),
      f'''      <p>{t("A polynomial is made of terms added or subtracted. Each term has a coefficient (the number) and a power of x with a whole-number exponent, 0 or more. Choose what to highlight, ask for another polynomial, or put it in standard form.", "Un polinomio está formado por términos sumados o restados. Cada término tiene un coeficiente (el número) y una potencia de x con exponente entero, 0 o más. Elija qué resaltar, pida otro polinomio o póngalo en forma estándar.")}</p>
      <div class="modos" role="group" aria-label="{t("Highlight", "Resaltar")}"><button type="button" class="btn-sec" id="qe-term">{t("Terms", "Términos")}</button><button type="button" class="btn-sec" id="qe-coef">{t("Coefficients", "Coeficientes")}</button><button type="button" class="btn-sec" id="qe-grado">{t("Degree", "Grado")}</button></div>
      <p id="qe-pol" style="font-size:30px;text-align:center;margin:18px 0;" aria-live="polite"></p>
{n4.salida("qe-info")}
      <div class="fila-btn"><button type="button" class="btn-sec" id="qe-otro">{t("Another polynomial", "Otro polinomio")}</button><button type="button" class="btn-sec" id="qe-ordena">{t("Put in standard form", "Ordenar en forma estándar")}</button><button type="button" class="btn-sec" id="qe-ej">{t("The lesson example", "Ver el ejemplo de la lección")}</button></div>
      <div class="caja-tip">{t("Each sign goes with the term after it: in 3x − 5 the second term is −5. When no number is written in front of x, the coefficient is 1: in x² it is 1 and in −x³ it is −1.", "Cada signo va con el término que le sigue: en 3x − 5 el segundo término es −5. Cuando no se ve ningún número delante de la x, el coeficiente es 1: en x² es 1 y en −x³ es −1.")}</div>
      <h3>{t("When is an expression not a polynomial?", "¿Cuándo una expresión no es un polinomio?")}</h3>
      <div class="tabla-scroll"><table class="tabla-lados"><caption class="sr-only">{t("Expressions that are and are not polynomials", "Expresiones que son y que no son polinomios")}</caption><thead><tr><th scope="col">{t("Expression", "Expresión")}</th><th scope="col">{t("Polynomial?", "¿Es polinomio?")}</th><th scope="col">{t("Reason", "Razón")}</th></tr></thead><tbody>
        <tr><td>x²/2 + 0.5x − 3</td><td>{t("Yes", "Sí")}</td><td>{t("The coefficients are fractions or decimals, but the exponents (2, 1, and 0) are whole numbers.", "Los coeficientes son fracciones o decimales, pero los exponentes (2, 1 y 0) son enteros.")}</td></tr>
        <tr><td>−8</td><td>{t("Yes", "Sí")}</td><td>{t("A monomial of degree 0.", "Un monomio de grado 0.")}</td></tr>
        <tr><td>4x<sup>−2</sup> + 1</td><td>No</td><td>{t("The exponent −2 is negative.", "El exponente −2 es negativo.")}</td></tr>
        <tr><td>6x<sup>1/2</sup> − x</td><td>No</td><td>{t("The exponent 1/2 is a fraction.", "El exponente 1/2 es fraccionario.")}</td></tr>
        <tr><td>5/x + 2</td><td>No</td><td>{t("x is in a denominator (5/x is 5x⁻¹).", "La x está en un denominador (5/x es 5x⁻¹).")}</td></tr></tbody></table></div>
{B.om("qq", t("Practice: terms, degree, and type", "Practique: términos, grado y clasificación"))}'''),
     (t("add-subtract", "suma-resta"), t("Adding and subtracting polynomials", "Suma y resta de polinomios"),
      f'''      <p>{t("Golden rule: only like terms go together, the ones with the same power of x. It is like sorting laundry: shirts with shirts, pants with pants. Only the numbers are added or subtracted; the x part is copied.", "La regla de oro: solo se juntan los términos semejantes, los que tienen la misma potencia de x. Es como ordenar ropa: las camisas con las camisas, los pantalones con los pantalones. Solo se suman o restan los números; la parte con x se copia.")}</p>
{tabla_trampas([("3x² + 5x² = 8x⁴", "3x² + 5x² = 8x²", t("When you add, the exponent is copied.", "Al sumar, el exponente se copia.")), ("3x² + 2x = 5x³", t("3x² + 2x (already simplified)", "3x² + 2x (ya está simplificado)"), t("x² and x are different families.", "x² y x son familias distintas.")), ("−(2x² − x + 4) = −2x² − x + 4", "−(2x² − x + 4) = −2x² + x − 4", t("The minus changes every sign.", "El menos cambia todos los signos.")), ("7 − 3x + 5x = 7 + 8x", "7 − 3x + 5x = 7 + 2x", t("Each term keeps the sign on its left.", "Cada término se lleva el signo de su izquierda.")), ("x² + 4x² = 4x²", "x² + 4x² = 5x²", t("x² has an invisible 1.", "x² lleva un 1 invisible."))])}
      <h3>{t("Guided workshop", "Taller guiado")}</h3>
{n4.pasos("sr", t("Another exercise", "Otro ejercicio"))}
{libre("sq", t("Practice: add or subtract", "Practique: sume o reste"), t("Result", "Resultado"))}'''),
     (t("multiply", "multiplicar"), t("A monomial times a polynomial", "Producto de un monomio por un polinomio"),
      f'''{n4.formula("a(b + c + d) = ab + ac + ad")}
      <p>{t("The monomial visits every term of the parentheses, one by one. In each product there are two separate jobs: the numbers are multiplied (with the sign rule), and the exponents of x are added. A lone x has exponent 1, and a number alone has no x.", "El monomio visita a cada término del paréntesis, uno por uno. En cada producto hay dos trabajos distintos: los números se multiplican (con la regla de los signos) y los exponentes de x se suman. Una x sola tiene exponente 1, y un número solo no tiene x.")}</p>
{tabla_trampas([("5(x + 2) = 5x + 2", "5(x + 2) = 5x + 10", t("The monomial multiplies every term.", "El monomio multiplica a todos los términos.")), ("−3x(x − 4) = −3x² − 12x", "−3x(x − 4) = −3x² + 12x", t("Same signs give positive.", "Signos iguales dan positivo.")), ("x² · x³ = x⁶", "x² · x³ = x⁵", t("The exponents are added.", "Los exponentes se suman.")), ("4x · 3x = 7x²", "4x · 3x = 12x²", t("The numbers are multiplied.", "Los números se multiplican.")), ("3x · 5 = 15", "3x · 5 = 15x", t("The x does not disappear.", "La x no desaparece."))])}
      <h3>{t("The arrows, step by step", "Las flechas, paso a paso")}</h3>
{n4.pasos("mp", t("Another product", "Otro producto"))}
{libre("mq", t("Practice: multiply", "Practique: multiplique"), t("Product", "Producto"))}'''),
     (t("evaluate", "evaluar"), t("Evaluating a polynomial", "Evaluar un polinomio"),
      f'''      <p>{t("To evaluate, put the number in place of x, always in parentheses, and follow the order of operations: powers, then multiplications, then additions and subtractions.", "Para evaluar, se pone el número en lugar de la x, siempre entre paréntesis, y se sigue el orden de operaciones: potencias, después multiplicaciones y, al final, sumas y restas.")}</p>
{n4.pasos("ev", t("Another polynomial", "Otro polinomio"))}
      <div class="caja-atencion"><strong>{t("Parentheses for negative numbers.", "Paréntesis para los negativos.")}</strong> {t("(−3)² = 9, but −3² = −9. When you put a negative number in place of x, write it in parentheses so the exponent reaches the sign too.", "(−3)² = 9, pero −3² = −9. Al poner un número negativo en lugar de la x, escríbalo entre paréntesis para que el exponente alcance también al signo.")}</div>
{libre("eq", t("Practice: evaluate", "Practique: evalúe"), t("Value", "Valor"))}''')]
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, LOGICA, estilo=n4.ESTILO, scripts=SCRIPTS)

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Polinomios: clasificación, suma, resta y multiplicación básica")
