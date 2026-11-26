"""Level 2 · Lesson 8.1 · Mean, median, mode, range, and weighted mean — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "8-1"
TEMA = ("Statistics and probability", "Estadística y probabilidad")
TIT = ("Mean, median, mode, range, and weighted mean", "Media, mediana, moda, rango y media ponderada")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.3rem;font-weight:700;color:#0d47a1">{x}</p>'

def fila(datos, marca=(), extra=""):
    """Data in a row; the positions in marca are highlighted."""
    s = ""
    for i, d in enumerate(datos):
        st = "background:#1565c0;color:#fff;border-color:#0d47a1" if i in marca else "background:#fff"
        s += f'<span style="display:inline-block;min-width:44px;text-align:center;padding:5px 8px;margin:2px;border:2px solid #90caf9;border-radius:8px;font-weight:700;{st}">{d}</span>'
    return f'<p style="text-align:center">{s}{extra}</p>'

def leccion():
    n = N
    s1 = f'''<p>{t("Welcome to Topic 8, the last topic of Level 2. Until now you worked with single numbers: an operation, a distance, a percent. Statistics is different: it works with <strong>sets of data</strong>. The typical question is no longer “how much is this?” but “how does this group of numbers behave?” To answer it, you sum up the group in one or two representative values.", "Bienvenida al Tema 8, el último del Nivel 2. Hasta ahora se trabajó con números concretos: una operación, una distancia, un porcentaje. La estadística es diferente: trata con <strong>conjuntos de datos</strong>. La pregunta típica deja de ser «¿cuánto vale esto?» y pasa a ser «¿cómo se comporta este grupo de números?». Para responderla, se resume el grupo en uno o dos valores representativos.")}</p>
<p>{t("Each of these four measures sums up a set of data in one number, but from a different point of view. Knowing when to use each one is as important as knowing how to find it.", "Cada una de estas cuatro medidas resume un conjunto de datos en un número, pero desde un punto de vista distinto. Saber cuándo usar cada una es tan importante como saber calcularla.")}</p>
{tabla(t("The four measures", "Las cuatro medidas"), t("Four ways to sum up a set of data", "Cuatro formas de resumir un conjunto de datos"),
       [t("Measure", "Medida"), t("What it tells you", "Qué dice"), t("How to find it", "Cómo se calcula")],
       [[t("Mean", "Media"), t("the average value", "el valor promedio"), t("sum ÷ number of values", "suma ÷ cantidad de datos")],
        [t("Median", "Mediana"), t("the middle value, once the data is in order", "el valor del centro, una vez ordenados los datos"), t("put the data in order and find the middle", "se ordenan y se busca el del medio")],
        [t("Mode", "Moda"), t("the most frequent value", "el valor más frecuente"), t("the value that repeats the most", "el que más se repite")],
        [t("Range", "Rango"), t("how spread out the data is", "qué tan dispersos están los datos"), t("greatest − least", "máximo − mínimo")]])}
{enlace(n, t("four-measures", "cuatro-medidas"), t("the four measures at a glance", "las cuatro medidas en una mirada"), t("Type your own data and the calculator gives the mean, median, mode, and range.", "Escriba sus propios datos y la calculadora le da la media, la mediana, la moda y el rango."))}'''

    s2 = f'''<p>{t("The <strong>mean</strong>, also called the <strong>average</strong>, is the best-known measure. Add all the values and divide by how many values there are.", "La <strong>media</strong>, llamada también <strong>promedio</strong>, es la medida más conocida. Se suman todos los datos y se divide entre la cantidad de datos.")}</p>
{big(t("mean = (sum of the values) ÷ (number of values)", "media = (suma de los datos) ÷ (cantidad de datos)"))}
{ej(t("Example: test scores", "Ejemplo: notas del semestre"), t("A student had these five scores: 78, 85, 90, 72, 95. What was the average?", "Un estudiante tuvo estas cinco notas: 78, 85, 90, 72, 95. ¿Cuál fue su promedio?"),
  [("1", t("Add.", "Sume."), "78 + 85 + 90 + 72 + 95 = 420."),
   ("2", t("Divide by how many.", "Divida entre la cantidad."), "420 ÷ 5 = 84."),
   ("✓", t("Answer.", "Respuesta."), t("The average is <strong>84</strong>.", "El promedio es <strong>84</strong>."))])}
{caja("tip", t("The idea behind it", "La idea intuitiva"), t("<p>The mean “shares out” all the values equally. If the 420 points were split evenly, each score would be exactly 84. That is why the mean is so useful to represent a group with a single number.</p>", "<p>La media «reparte en partes iguales» todos los datos. Si los 420 puntos del ejemplo se repartieran de forma pareja, cada nota sería exactamente 84. Por eso la media es tan útil para representar un grupo con un solo número.</p>"))}
{calc(t("The mean on the calculator", "La media en la calculadora"), t(f"<p>Type {T('(')} {T('78')} {T('+')} {T('85')} {T('+')} {T('90')} {T('+')} {T('72')} {T('+')} {T('95')} {T(')')} {T('÷')} {T('5')} {T('enter')}. The parentheses make the calculator add first. Without them it would divide only the 95 by 5.</p>", f"<p>Escriba {T('(')} {T('78')} {T('+')} {T('85')} {T('+')} {T('90')} {T('+')} {T('72')} {T('+')} {T('95')} {T(')')} {T('÷')} {T('5')} {T('enter')}. Los paréntesis hacen que la calculadora sume primero. Sin ellos, dividiría solo el 95 entre 5.</p>"))}
{practica("p1", t("Practice 1 — The mean", "Práctica 1 — La media"), t("Data: 5, 8, 8, 10, 14. What is the mean?", "Datos: 5, 8, 8, 10, 14. ¿Cuál es la media?"), [("a", "10"), ("b", "45"), ("c", "8"), ("d", "9")])}
{enlace(n, t("mean", "media"), t("the mean", "la media aritmética"), t("Level the towers to see the mean as equal shares, and practice.", "Empareje las torres para ver la media como un reparto en partes iguales, y practique."))}'''

    s3 = f'''<p>{t("The <strong>median</strong> is the value in the middle position when the data is in order from least to greatest. It splits the set into two equal halves: half the data is below it and half is above it.", "La <strong>mediana</strong> es el valor que ocupa la posición central cuando los datos están ordenados de menor a mayor. Divide el conjunto en dos mitades iguales: la mitad de los datos está debajo y la otra mitad, encima.")}</p>
<h3>{t("Case 1: an odd number of values", "Caso 1: cantidad impar de datos")}</h3>
<p>{t("The median is the value in the middle.", "La mediana es el dato del medio.")}</p>
{fila(["65", "72", "78", "85", "95"], (2,), t(" → median = 78", " → mediana = 78"))}
<h3>{t("Case 2: an even number of values", "Caso 2: cantidad par de datos")}</h3>
<p>{t("There are two values in the middle. The median is the mean of those two.", "Hay dos datos en el centro. La mediana es la media de esos dos.")}</p>
{fila(["60", "70", "75", "80", "90", "95"], (2, 3), t(" → median = (75 + 80) ÷ 2 = 77.5", " → mediana = (75 + 80) ÷ 2 = 77.5"))}
{caja("ojo", t("A step you must not skip", "Paso obligatorio"), t("<p>Put the data in order before you look for the median. Forgetting this is the most common mistake: the value in the middle of an unordered list is not the median.</p>", "<p>Antes de buscar la mediana, hay que ordenar los datos. Olvidarlo es el error más frecuente: el valor que queda en el centro de una lista desordenada no es la mediana.</p>"))}
{ej(t("Example: an unordered list", "Ejemplo: una lista desordenada"), t("Find the median of 12, 8, 15, 7, 10, 9, 14.", "Halle la mediana de 12, 8, 15, 7, 10, 9, 14."),
  [("1", t("Put them in order.", "Ordene."), "7, 8, 9, 10, 12, 14, 15."),
   ("2", t("Find the middle.", "Busque el centro."), t("There are 7 values (odd). The middle one is the 4th: 10.", "Hay 7 datos (cantidad impar). El del medio es el 4.º: 10.")),
   ("✓", t("Answer.", "Respuesta."), t("The median is <strong>10</strong>.", "La mediana es <strong>10</strong>."))])}
{practica("p2", t("Practice 2 — The median", "Práctica 2 — La mediana"), t("Data: 5, 8, 8, 10, 14. What is the median?", "Datos: 5, 8, 8, 10, 14. ¿Cuál es la mediana?"), [("a", "8"), ("b", "9"), ("c", "10"), ("d", "8.5")])}
{enlace(n, t("median", "mediana"), t("the median", "la mediana"), t("Put the data in order and find the middle, with an even and an odd number of values.", "Ordene los datos y encuentre el centro, con cantidad par e impar."))}'''

    s4 = f'''<h3>{t("The mode", "La moda")}</h3>
<p>{t("The <strong>mode</strong> is the value that appears most often. A set can have one mode, two modes (when two values tie for the most), or no mode (when every value appears the same number of times).", "La <strong>moda</strong> es el valor que aparece con más frecuencia. Un conjunto puede tener una moda, dos modas (cuando dos valores empatan en la frecuencia máxima) o ninguna (cuando todos aparecen el mismo número de veces).")}</p>
{fila(["4", "7", "9", "9", "9", "12", "15"], (2, 3, 4), t(" → mode = 9 (it appears three times)", " → moda = 9 (aparece tres veces)"))}
<h3>{t("The range", "El rango")}</h3>
<p>{t("The <strong>range</strong> measures how spread out the data is: the difference between the greatest and the least value.", "El <strong>rango</strong> mide qué tan dispersos están los datos: es la diferencia entre el valor mayor y el menor.")}</p>
{big(t("range = greatest − least", "rango = máximo − mínimo"))}
<p style="text-align:center">{t("In 4, 7, 9, 9, 9, 12, 15: range = 15 − 4 = 11.", "En 4, 7, 9, 9, 9, 12, 15: rango = 15 − 4 = 11.")}</p>
{caja("tip", t("When to use each one", "Cuándo usar cada una"), t("<p>The <strong>mean</strong> sums up numbers with no extreme values. The <strong>median</strong> is better when there are outliers (next section). The <strong>mode</strong> works even with data that is not numbers (favorite colors, best-selling sizes). The <strong>range</strong> gives a quick idea of the spread.</p>", "<p>La <strong>media</strong> resume datos numéricos sin valores extremos. La <strong>mediana</strong> es mejor cuando hay valores atípicos (siguiente sección). La <strong>moda</strong> sirve incluso con datos que no son números (colores favoritos, tallas más vendidas). El <strong>rango</strong> da una idea rápida de la dispersión.</p>"))}
{practica("p3", t("Practice 3 — The mode", "Práctica 3 — La moda"), t("Data: 5, 8, 8, 10, 14. What is the mode?", "Datos: 5, 8, 8, 10, 14. ¿Cuál es la moda?"), [("a", "9"), ("b", "14"), ("c", "8"), ("d", t("No mode", "No hay moda"))])}
{practica("p4", t("Practice 4 — The range", "Práctica 4 — El rango"), t("Data: 5, 8, 8, 10, 14. What is the range?", "Datos: 5, 8, 8, 10, 14. ¿Cuál es el rango?"), [("a", "19"), ("b", "9"), ("c", "14"), ("d", "5")])}
{enlace(n, t("mode-range", "moda-rango"), t("the mode and the range", "la moda y el rango"), t("Find the value that repeats the most and measure how spread out the data is.", "Encuentre el valor que más se repite y mida qué tan dispersos están los datos."))}'''

    s5 = f'''<p>{t("The mean has one important weakness: values that are very different from the rest, called <strong>outliers</strong>, pull it strongly. A single extreme value can drag the average far from what really represents the group.", "La media tiene un defecto importante: los valores muy distintos del resto, llamados <strong>valores atípicos</strong>, la arrastran con fuerza. Un solo dato extremo puede llevar el promedio lejos de lo que realmente representa al grupo.")}</p>
{ej(t("Example: the “average” salary", "Ejemplo: el salario «promedio»"), t("In a small company, five employees earn these monthly salaries: $3,000, $3,200, $3,100, $2,900, $3,300. A sixth employee, the director, earns $30,000. Compare the mean and the median.", "En una pequeña empresa, cinco empleados ganan estos salarios mensuales: $3,000, $3,200, $3,100, $2,900, $3,300. Un sexto empleado, el director, gana $30,000. Compare la media y la mediana."),
  [("1", t("Sum.", "Suma."), "3,000 + 3,200 + 3,100 + 2,900 + 3,300 + 30,000 = 45,500."),
   ("2", t("Mean.", "Media."), t("45,500 ÷ 6 ≈ 7,583. It sounds like an excellent salary for the company…", "45,500 ÷ 6 ≈ 7,583. Parece un salario excelente para la empresa…")),
   ("3", t("In order.", "Ordenados."), "2,900, 3,000, 3,100, 3,200, 3,300, 30,000."),
   ("4", t("Median.", "Mediana."), t("(3,100 + 3,200) ÷ 2 = 3,150. That is what most of them really earn.", "(3,100 + 3,200) ÷ 2 = 3,150. Eso es lo que gana en realidad la mayoría.")),
   ("✓", t("Conclusion.", "Conclusión."), t("The director's salary is an outlier that inflates the mean. The <strong>median</strong> represents the typical salary much better.", "El salario del director es un valor atípico que infla la media. La <strong>mediana</strong> representa mucho mejor el salario típico."))])}
{caja("tip", t("A lesson for the news", "Una lección para las noticias"), t("<p>When a headline says “the average salary went up X%”, ask whether it is the mean or the median. The difference between the two often tells the real story behind the data.</p>", "<p>Cuando un titular dice «el salario promedio subió un X%», conviene preguntar si se trata de la media o de la mediana. La diferencia entre las dos suele revelar la verdadera historia detrás de los datos.</p>"))}
{practica("p5", t("Practice 5 — Which measure?", "Práctica 5 — ¿Qué medida?"), t("In a company the owner earns 20 times more than everyone else. Which measure best represents the typical salary?", "En una empresa, el dueño gana 20 veces más que los demás. ¿Qué medida representa mejor el salario típico?"),
          [("a", t("The mean", "La media")), ("b", t("The mode", "La moda")), ("c", t("The range", "El rango")), ("d", t("The median", "La mediana"))])}
{enlace(n, t("outliers", "atipicos"), t("when the mean misleads", "cuando la media engaña"), t("Move the manager's salary and watch the mean shoot up while the median hardly changes.", "Mueva el salario del gerente y vea cómo se dispara la media mientras la mediana casi no cambia."))}'''

    s6 = f'''<p>{t("Sometimes not all the values are equally important. In grades, for example, the final exam counts more than a quiz. Then you find the <strong>weighted mean</strong>: multiply each value by its “weight” before you average.", "A veces no todos los datos tienen la misma importancia. En las calificaciones, por ejemplo, el examen final pesa más que un quiz. En esos casos se calcula la <strong>media ponderada</strong>: cada valor se multiplica por su «peso» antes de promediar.")}</p>
{big(t("weighted mean = Σ(value × weight) ÷ Σ(weights)", "media ponderada = Σ(valor × peso) ÷ Σ(pesos)"))}
<p>{t("The symbol Σ (sigma) means “sum”. Σ(value × weight) is the sum of all the products; Σ(weights) is the sum of the weights.", "El símbolo Σ (sigma) significa «suma». Σ(valor × peso) es la suma de todos los productos; Σ(pesos) es la suma de los pesos.")}</p>
{tabla(t("A grade report", "Un reporte de calificaciones"), t("Weighted mean of a grade report", "Media ponderada de un reporte de calificaciones"),
       [t("Assessment", "Evaluación"), t("Score", "Nota"), t("Weight", "Peso"), t("Score × weight", "Nota × peso")],
       [[t("Quiz", "Quiz"), "85", "20", "1,700"], [t("Midterm exam", "Examen parcial"), "78", "30", "2,340"], [t("Homework", "Tarea"), "92", "20", "1,840"], [t("Final exam", "Examen final"), "88", "30", "2,640"], [t("<strong>Totals</strong>", "<strong>Totales</strong>"), "—", "<strong>100</strong>", "<strong>8,520</strong>"]])}
{ej(t("Example: the final grade", "Ejemplo: la nota final"), t("A course counts the quiz 20%, the midterm 30%, homework 20%, and the final exam 30%. A student got 85, 78, 92, and 88. What is the final grade?", "Un curso evalúa el quiz con un 20%, el examen parcial con un 30%, la tarea con un 20% y el examen final con un 30%. Un estudiante obtuvo 85, 78, 92 y 88. ¿Cuál es su nota final?"),
  [("1", t("Sum of the products.", "Suma de productos."), "1,700 + 2,340 + 1,840 + 2,640 = 8,520."),
   ("2", t("Sum of the weights.", "Suma de pesos."), "20 + 30 + 20 + 30 = 100."),
   ("3", t("Divide.", "Divida."), "8,520 ÷ 100 = 85.2."),
   ("✓", t("Answer.", "Respuesta."), t("The final grade is <strong>85.2</strong>.", "La nota final es <strong>85.2</strong>."))])}
{caja("tip", t("A useful comparison", "Comparación útil"), t("<p>The simple mean of the four scores would be (85 + 78 + 92 + 88) ÷ 4 = 85.75. The weighted mean, 85.2, is a little lower because the midterm (78), the lowest score, weighs more than the homework (92), the highest. The weights change the result and make it fairer to the importance of each part.</p>", "<p>La media simple de las cuatro notas sería (85 + 78 + 92 + 88) ÷ 4 = 85.75. La media ponderada, 85.2, es un poco menor porque el examen parcial (78), la nota más baja, pesa más que la tarea (92), la más alta. Los pesos cambian el resultado y lo hacen más justo con la importancia de cada evaluación.</p>"))}
{practica("p6", t("Practice 6 — Two weights", "Práctica 6 — Dos pesos"), t("Quiz 70 (weight 25%) and exam 90 (weight 75%). What is the final grade?", "Quiz 70 (peso 25%) y examen 90 (peso 75%). ¿Cuál es la nota final?"), [("a", "80"), ("b", "85"), ("c", "160"), ("d", "82.5")])}
{practica("p7", t("Practice 7 — Another course", "Práctica 7 — Otro curso"), t("Homework 80 (weight 40%) and exam 60 (weight 60%). What is the final grade?", "Tarea 80 (peso 40%) y examen 60 (peso 60%). ¿Cuál es la nota final?"), [("a", "70"), ("b", "140"), ("c", "68"), ("d", "72")])}
{enlace(n, t("weighted-mean", "ponderada"), t("the weighted mean", "la media ponderada"), t("Find the final grade of a course when each part has a different weight.", "Calcule la nota final de un curso cuando cada parte tiene un peso distinto."))}'''

    secciones = [("s-" + t("four-measures", "cuatro-medidas"), t("The four measures at a glance", "Las cuatro medidas, en una mirada"), s1),
                 ("s-" + t("mean", "media"), t("The mean", "La media aritmética"), s2),
                 ("s-" + t("median", "mediana"), t("The median: the middle value", "La mediana: el valor del centro"), s3),
                 ("s-" + t("mode-range", "moda-rango"), t("The mode and the range", "La moda y el rango"), s4),
                 ("s-" + t("outliers", "atipicos"), t("When the mean misleads: outliers", "Cuando la media engaña: los valores atípicos"), s5),
                 ("s-" + t("weighted-mean", "ponderada"), t("The weighted mean", "La media ponderada"), s6)]

    lesson = {"next": t("Lesson 8.2", "Lección 8.2"), "review": t("sections 2, 3, and 6", "las secciones 2, 3 y 6"),
     "practice": {
      "p1": {"ok": "d", "hints": {"a": t("Check the sum: 5 + 8 + 8 + 10 + 14 = 45.", "Revise la suma: 5 + 8 + 8 + 10 + 14 = 45."), "b": t("That is the sum. Divide by how many values there are.", "Esa es la suma. Divida entre la cantidad de datos."), "c": t("8 is the mode and the median. The mean is sum ÷ number of values.", "8 es la moda y la mediana. La media es suma ÷ cantidad.")},
             "right": t("45 ÷ 5 = 9.", "45 ÷ 5 = 9."), "solution": t("Sum 45; 45 ÷ 5 = 9.", "Suma 45; 45 ÷ 5 = 9.")},
      "p2": {"ok": "a", "hints": {"b": t("9 is the mean. The median is the middle value.", "9 es la media. La mediana es el valor del centro."), "c": t("There are 5 values: the middle one is the 3rd.", "Hay 5 datos: el del medio es el 3.º."), "d": t("With 5 values there is only one in the middle.", "Con 5 datos hay solo uno en el centro.")},
             "right": t("5, 8, <strong>8</strong>, 10, 14: the median is 8.", "5, 8, <strong>8</strong>, 10, 14: la mediana es 8."), "solution": t("In order: 5, 8, 8, 10, 14. The 3rd value is 8.", "Ordenados: 5, 8, 8, 10, 14. El 3.º es 8.")},
      "p3": {"ok": "c", "hints": {"a": t("9 is the mean. The mode is the value that repeats.", "9 es la media. La moda es el valor que se repite."), "b": t("14 appears only once.", "14 aparece una sola vez."), "d": t("8 appears twice: there is a mode.", "8 aparece dos veces: sí hay moda.")},
             "right": t("8 appears twice.", "8 aparece dos veces."), "solution": t("8 is the only value that repeats.", "8 es el único valor que se repite.")},
      "p4": {"ok": "b", "hints": {"a": t("You added. The range is greatest − least.", "Sumó. El rango es máximo − mínimo."), "c": t("14 is the greatest value. Subtract the least.", "14 es el máximo. Reste el mínimo."), "d": t("5 is the least value. Subtract it from the greatest.", "5 es el mínimo. Réstelo del máximo.")},
             "right": t("14 − 5 = 9.", "14 − 5 = 9."), "solution": t("Range = 14 − 5 = 9.", "Rango = 14 − 5 = 9.")},
      "p5": {"ok": "d", "hints": {"a": t("The owner's salary drags the mean up.", "El salario del dueño arrastra la media hacia arriba."), "b": t("The mode is for the most frequent value; salaries may all be different.", "La moda es el valor más frecuente; los salarios pueden ser todos distintos."), "c": t("The range measures spread, not the typical value.", "El rango mide la dispersión, no el valor típico.")},
             "right": t("The median is not pulled by the outlier.", "A la mediana no la arrastra el valor atípico."), "solution": t("With an outlier, the median represents the typical value best.", "Con un valor atípico, la mediana representa mejor el valor típico.")},
      "p6": {"ok": "b", "hints": {"a": t("80 is the simple mean. Multiply by the weights.", "80 es la media simple. Multiplique por los pesos."), "c": t("You added the scores. Use 70 × 0.25 + 90 × 0.75.", "Sumó las notas. Use 70 × 0.25 + 90 × 0.75."), "d": t("Check: 70 × 0.25 = 17.5 and 90 × 0.75 = 67.5.", "Revise: 70 × 0.25 = 17.5 y 90 × 0.75 = 67.5.")},
             "right": t("17.5 + 67.5 = 85.", "17.5 + 67.5 = 85."), "solution": t("70 × 0.25 + 90 × 0.75 = 17.5 + 67.5 = 85.", "70 × 0.25 + 90 × 0.75 = 17.5 + 67.5 = 85.")},
      "p7": {"ok": "c", "hints": {"a": t("70 is the simple mean. Use the weights.", "70 es la media simple. Use los pesos."), "b": t("You added the scores.", "Sumó las notas."), "d": t("You switched the weights: the exam weighs 60%.", "Cambió los pesos: el examen pesa el 60%.")},
             "right": t("32 + 36 = 68.", "32 + 36 = 68."), "solution": t("80 × 0.40 + 60 × 0.60 = 32 + 36 = 68.", "80 × 0.40 + 60 × 0.60 = 32 + 36 = 68.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("That is the sum.", "Esa es la suma."), "b": t("Check: 420 ÷ 5.", "Revise: 420 ÷ 5."), "d": t("90 is the median.", "90 es la mediana.")}, "solution": t("420 ÷ 5 = 84.", "420 ÷ 5 = 84.")},
      "B": {"ok": "a", "hints": {"b": t("That is the middle of the unordered list. Put it in order first.", "Ese es el centro de la lista desordenada. Primero ordénela."), "c": t("In order: 7, 8, 9, 10, 12, 14, 15.", "Ordenados: 7, 8, 9, 10, 12, 14, 15."), "d": t("That is the mean.", "Esa es la media.")}, "solution": t("7, 8, 9, 10, 12, 14, 15 → 10.", "7, 8, 9, 10, 12, 14, 15 → 10.")},
      "C": {"ok": "d", "hints": {"a": t("With an even number of values, average the two in the middle.", "Con cantidad par, se promedian los dos del centro."), "b": t("Average 75 and 80.", "Promedie 75 y 80."), "c": t("That is the mean.", "Esa es la media.")}, "solution": t("(75 + 80) ÷ 2 = 77.5.", "(75 + 80) ÷ 2 = 77.5.")},
      "D": {"ok": "b", "hints": {"a": t("That is the mean.", "Esa es la media."), "c": t("That is the range.", "Ese es el rango."), "d": t("That is the greatest value.", "Ese es el máximo.")}, "solution": t("9 appears three times.", "9 aparece tres veces.")},
      "E": {"ok": "c", "hints": {"a": t("That is the greatest value.", "Ese es el máximo."), "b": t("That is the least value.", "Ese es el mínimo."), "d": t("You added. Subtract.", "Sumó. Reste.")}, "solution": t("15 − 4 = 11.", "15 − 4 = 11.")},
      "F": {"ok": "a", "hints": {"b": t("The mean is inflated by the director's salary.", "A la media la infla el salario del director."), "c": t("That is the range.", "Ese es el rango."), "d": t("That is the outlier itself.", "Ese es el propio valor atípico.")}, "solution": t("The median, $3,150, represents the typical salary.", "La mediana, $3,150, representa el salario típico.")},
      "G": {"ok": "d", "hints": {"a": t("That is the simple mean.", "Esa es la media simple."), "b": t("That is the sum of the scores.", "Esa es la suma de las notas."), "c": t("Check the products: 8,520 ÷ 100.", "Revise los productos: 8,520 ÷ 100.")}, "solution": t("8,520 ÷ 100 = 85.2.", "8,520 ÷ 100 = 85.2.")},
      "H": {"ok": "b", "hints": {"a": t("You cannot average colors.", "No se puede promediar colores."), "c": t("Colors cannot be put in number order.", "Los colores no se pueden ordenar como números."), "d": t("There is no greatest or least color.", "No hay color máximo ni mínimo.")}, "solution": t("With data that is not numbers, use the mode.", "Con datos que no son números se usa la moda.")}
     }}

    quiz = [
     ("A", t("A student's scores are 78, 85, 90, 72, and 95. What is the mean?", "Las notas de un estudiante son 78, 85, 90, 72 y 95. ¿Cuál es la media?"), [("a", "420"), ("b", "85"), ("c", "84"), ("d", "90")]),
     ("B", t("What is the median of 12, 8, 15, 7, 10, 9, 14?", "¿Cuál es la mediana de 12, 8, 15, 7, 10, 9, 14?"), [("a", "10"), ("b", "7"), ("c", "12"), ("d", "10.7")]),
     ("C", t("What is the median of 60, 70, 75, 80, 90, 95?", "¿Cuál es la mediana de 60, 70, 75, 80, 90, 95?"), [("a", "75"), ("b", "80"), ("c", "78.3"), ("d", "77.5")]),
     ("D", t("What is the mode of 4, 7, 9, 9, 9, 12, 15?", "¿Cuál es la moda de 4, 7, 9, 9, 9, 12, 15?"), [("a", "9.29"), ("b", "9"), ("c", "11"), ("d", "15")]),
     ("E", t("What is the range of 4, 7, 9, 9, 9, 12, 15?", "¿Cuál es el rango de 4, 7, 9, 9, 9, 12, 15?"), [("a", "15"), ("b", "4"), ("c", "11"), ("d", "19")]),
     ("F", t("Salaries: $2,900, $3,000, $3,100, $3,200, $3,300, and $30,000. Which number best represents the typical salary?", "Salarios: $2,900, $3,000, $3,100, $3,200, $3,300 y $30,000. ¿Qué número representa mejor el salario típico?"), [("a", t("$3,150 (the median)", "$3,150 (la mediana)")), ("b", t("$7,583 (the mean)", "$7,583 (la media)")), ("c", "$27,100"), ("d", "$30,000")]),
     ("G", t("Scores 85, 78, 92, and 88 with weights 20%, 30%, 20%, and 30%. What is the weighted mean?", "Notas 85, 78, 92 y 88 con pesos de 20%, 30%, 20% y 30%. ¿Cuál es la media ponderada?"), [("a", "85.75"), ("b", "343"), ("c", "84"), ("d", "85.2")]),
     ("H", t("To sum up the favorite color of the students in a class, you use the…", "Para resumir el color preferido de los estudiantes de un salón, se usa…"), [("a", t("mean", "la media")), ("b", t("mode", "la moda")), ("c", t("median", "la mediana")), ("d", t("range", "el rango"))])]

    return B.pagina_leccion(n, 8, t(*TEMA), t(*TIT),
        t("Summing up a set of data in one number: the mean, the median, the mode, and the range; why outliers mislead the mean; and the weighted mean of a grade report.", "Resumir un conjunto de datos en un número: la media, la mediana, la moda y el rango; por qué los valores atípicos engañan a la media; y la media ponderada de un reporte de calificaciones."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Find</strong> the mean as the sum of the values divided by how many there are.", "<strong>Calcular</strong> la media como la suma de los datos dividida entre la cantidad."),
         t("<strong>Find</strong> the median by putting the data in order and finding the middle value.", "<strong>Calcular</strong> la mediana ordenando los datos y buscando el valor central."),
         t("<strong>Name</strong> the mode as the most frequent value and the range as greatest − least.", "<strong>Identificar</strong> la moda como el valor que más se repite y el rango como máximo − mínimo."),
         t("<strong>Recognize</strong> when outliers make the mean misleading.", "<strong>Reconocer</strong> cuándo la media puede engañar por los valores atípicos."),
         t("<strong>Find</strong> the weighted mean when the values have different weights.", "<strong>Calcular</strong> la media ponderada cuando los datos tienen pesos distintos.")],
        secciones,
        (t("Find the mean of three sets of data. Find three medians (one with an odd number of values, one with an even number, one with an outlier). Find two modes and two ranges. Then solve four weighted-mean problems with different weights.",
           "Calcule la media de tres conjuntos de datos. Halle tres medianas (una con cantidad impar, otra con cantidad par y otra con un valor atípico). Halle dos modas y dos rangos. Después, resuelva cuatro problemas de media ponderada con pesos distintos."),
         t("Write down a real set of data from your week: your work hours each day, what you spend on groceries, or the temperature each morning. Find its mean, median, mode, and range. Which one sums it up best, and why?",
           "Anote un conjunto de datos real de su semana: las horas de trabajo de cada día, lo que gasta en el mercado o la temperatura de cada mañana. Halle la media, la mediana, la moda y el rango. ¿Cuál lo resume mejor y por qué?")),
        quiz,
        t("Self-check checklist for the measures of center", "Lista de autoevaluación de las medidas de tendencia central"),
        t("Self-check checklist: skills for the measures of center", "Lista de autoevaluación: destrezas de las medidas de tendencia central"),
        [(t("The mean and the median", "La media y la mediana"), t("I find both, put the data in order first, and explain why the median resists outliers.", "Calculo las dos, ordeno primero los datos y explico por qué la mediana resiste los valores atípicos."), t("I find them with some help.", "Las calculo con algo de apoyo."), t("I mix up the sum with the mean, or I do not put the data in order.", "Confundo la suma con la media, o no ordeno los datos.")),
         (t("The weighted mean", "La media ponderada"), t("I find it, compare it with the simple mean, and explain the effect of the weights.", "La calculo, la comparo con la media simple y explico el efecto de los pesos."), t("I find it by following the table.", "La calculo siguiendo la tabla."), t("I do not see how it differs from the simple mean.", "No reconozco la diferencia con la media simple.")),
         (t("Choose the measure", "Elegir la medida"), t("I choose the right measure for the situation and justify it with the data.", "Elijo la medida adecuada según la situación y lo justifico con los datos."), t("I choose with some help.", "Elijo con algo de apoyo."), t("I always use the mean.", "Uso la media en cualquier caso."))],
        t("<p>This first lesson of Topic 8 gave you the four basic measures to sum up a set of data: <strong>mean</strong>, <strong>median</strong>, <strong>mode</strong>, and <strong>range</strong>. The <strong>weighted mean</strong> added flexibility for cases where not all values count the same, like a semester's grades. And one key lesson: the mean can mislead when there are outliers; the median is often more representative.</p>\n<p>In <strong>Lesson 8.2 · Circle graphs: read, interpret, and make</strong> the percents of Topic 5 meet the circle of Topic 7 to show how a whole is divided. Each slice of the “pie” shows what part each category takes.</p>",
          "<p>En esta lección de apertura del Tema 8 quedaron claras las cuatro medidas básicas para resumir un conjunto de datos: <strong>media</strong>, <strong>mediana</strong>, <strong>moda</strong> y <strong>rango</strong>. La <strong>media ponderada</strong> añadió flexibilidad para los casos en que no todos los datos pesan igual, como las calificaciones del semestre. Y una lección crucial: la media puede engañar cuando hay valores atípicos; la mediana suele ser más representativa.</p>\n<p>En la <strong>Lección 8.2 · Gráficos circulares: leer, interpretar y construir</strong>, los porcentajes del Tema 5 se reencuentran con el círculo del Tema 7 para mostrar cómo se reparte un total. Cada sector del gráfico indica qué parte ocupa cada categoría.</p>"),
        ("8-2", ("", t("Lesson 8.2 · Circle graphs: read, interpret, and make", "Lección 8.2 · Gráficos circulares: leer, interpretar y construir"))),
        [(t("mean (average)", "media (promedio)"), t("The sum of the values divided by how many there are.", "La suma de los datos dividida entre la cantidad.")),
         (t("median", "mediana"), t("The middle value of the data in order.", "El valor del centro de los datos ordenados.")),
         (t("mode", "moda"), t("The value that appears most often.", "El valor que más se repite.")),
         (t("outlier", "valor atípico"), t("A value very different from the rest of the data.", "Un dato muy distinto del resto."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "md1": "Type at least two numbers separated by commas.", "ord": "In order:", "media": "Mean", "mediana": "Median", "moda": "Mode", "rango": "Range",
  "medio": "the middle value", "dosMedio": "average of the two in the middle", "bimodal": "bimodal",
  "mdNota": "In the data in order, the median is filled in color, the mode is yellow, and the least and greatest values have a blue border.",
  "meDatos": "Data: {d}.", "meVozR": "All the towers at height {m}.", "meVoz": "Towers with heights {d}.", "meMedia": "mean",
  "meS": "Sum: {s} = {t}. Number of values: {n}. Mean: {t} ÷ {n} = <strong>{m}</strong>.", "meRep": "Shared out equally, each tower gets {m} blocks: that is the mean.", "meLinea": "The red dashed line marks the mean. Press “Share equally” to level the towers.",
  "meBtn": "Share equally", "meBtn2": "Back to the data",
  "gm1": "A student's test scores: {d}. What is the mean? (Round to the hundredth if needed.)", "gm2": "Minutes of exercise on {n} days: {d}. What is the mean? (Round to the hundredth if needed.)",
  "gmS": "Sum: {s}; {s} ÷ {n} ≈ {m}.", "gmP1": "That is the sum. Divide by how many values there are.", "gmP2": "That is the median. The mean is sum ÷ number of values.",
  "gm3": "A student has {k} test scores: {d}. What score does she need on the next test so that the average of the {n} tests is {o}?", "gm3S": "The sum must be {o} × {n} = {T}. She already has {y}, so she needs {f}.", "gm3P": "Getting {o} is not enough if the other scores are lower: the total must be {T}.",
  "gmeQ": "Data: {d}. What is the median?", "gmeS1": "In order: {o}. There are {n} values: the middle one is number {k}, {m}.", "gmeS2": "In order: {o}. There are {n} values: the two in the middle are {a} and {b}; ({a} + {b}) ÷ 2 = {m}.",
  "gmeP": "Put the data in order first: the value in the middle of the unordered list is not the median.",
  "gmoQ": "Data: {d}. What is the mode?", "gmoP": "Two values tie for the most: the set is bimodal.", "gmo1": "{m} appears three times.", "gmo2": "{m} each appear twice: bimodal.", "gmo3": "No value repeats: there is no mode.",
  "gmoM1": "The mode is {m}, which appears three times.", "gmoM2": "There are two modes: {m}.", "gmoM3": "Every value appears once: there is no mode.",
  "graQ1": "Low temperatures (°F): {d}. What is the range?", "graQ2": "Data: {d}. What is the range?", "graS": "Greatest {M}, least {m}: {M} − {p} = {r}.",
  "graP1": "Subtracting a negative is adding its opposite: {M} − {p} = {M} + {q}.", "graP2": "Use the greatest and the least of all the values, not the first and the last in the list.",
  "atG": "The manager's salary pulls the mean up to {m}, more than any of the other five earn. The median, {me}, still represents the group well.", "atN": "With no extreme values, the mean and the median are very close.",
  "sit": [["The prices of the houses in a neighborhood, where there is one mansion.", "med", "A very high value drags the mean: the median is better."], ["The best-selling shoe size in a store.", "moda", "You want the most frequent value: the mode."], ["The scores on a test with no extreme values.", "media", "With no extreme values, the mean sums them up well."], ["The salaries in a company where the owner earns 20 times more than the others.", "med", "The owner's salary is an outlier: the median is better."], ["The favorite car color of the customers.", "moda", "With data that is not numbers, only the mode works."], ["The minutes a bus takes to arrive, all of them similar.", "media", "Similar data with no extremes: the mean."]],
  "sitQ": " Which measure best represents the group?", "opMedia": "The mean", "opMed": "The median", "opModa": "The mode",
  "po1": "{t} × 0.20 + {e} × 0.50 + {p} × 0.30 = {a} + {b} + {c}", "po2": "Final grade: {f}", "po3": "The simple average would be {s}. Since the exams weigh half, their score pulls the weighted mean more.",
  "pq1": "In a course, homework counts {a}%, exams {b}%, and the project {c}%. A student has {x} in homework, {y} in exams, and {z} in the project. What is the final grade?", "pq1P": "That is the simple average. Multiply each score by its weight.",
  "pq2": "A store sold {a} items at ${p}, {b} at ${q}, and {c} at ${r}. What was the average price per item, in dollars? (Round to the hundredth.)", "pq2P": "That is the average of the three prices, without counting how many were sold of each."
 },
 "es": {
  "md1": "Escriba por lo menos dos números separados por comas.", "ord": "Ordenados:", "media": "Media", "mediana": "Mediana", "moda": "Moda", "rango": "Rango",
  "medio": "el del medio", "dosMedio": "promedio de los dos del medio", "bimodal": "bimodal",
  "mdNota": "En los datos ordenados, la mediana va rellena de color, la moda en amarillo y el menor y el mayor con borde azul.",
  "meDatos": "Datos: {d}.", "meVozR": "Todas las torres a la altura {m}.", "meVoz": "Torres de alturas {d}.", "meMedia": "media",
  "meS": "Suma: {s} = {t}. Cantidad: {n}. Media: {t} ÷ {n} = <strong>{m}</strong>.", "meRep": "Repartidos en partes iguales, a cada torre le tocan {m} bloques: eso es la media.", "meLinea": "La línea roja punteada marca la media. Pulse «Repartir» para emparejar las torres.",
  "meBtn": "Repartir en partes iguales", "meBtn2": "Volver a los datos",
  "gm1": "Notas de un estudiante: {d}. ¿Cuál es la media? (Redondee a la centésima si hace falta.)", "gm2": "Minutos de ejercicio en {n} días: {d}. ¿Cuál es la media? (Redondee a la centésima si hace falta.)",
  "gmS": "Suma: {s}; {s} ÷ {n} ≈ {m}.", "gmP1": "Esa es la suma. Falta dividir entre la cantidad de datos.", "gmP2": "Esa es la mediana. La media es suma ÷ cantidad.",
  "gm3": "Una estudiante tiene {k} notas: {d}. ¿Qué nota necesita en el próximo examen para que el promedio de los {n} exámenes sea {o}?", "gm3S": "La suma tiene que ser {o} × {n} = {T}. Ya tiene {y}: le faltan {f}.", "gm3P": "Sacar {o} no basta si las otras notas son más bajas: la suma total tiene que ser {T}.",
  "gmeQ": "Datos: {d}. ¿Cuál es la mediana?", "gmeS1": "Ordenados: {o}. Hay {n} datos: el del medio es el {k}.º, {m}.", "gmeS2": "Ordenados: {o}. Hay {n} datos: los del medio son {a} y {b}; ({a} + {b}) ÷ 2 = {m}.",
  "gmeP": "Primero hay que ordenar los datos: el que queda en el centro de la lista desordenada no es la mediana.",
  "gmoQ": "Datos: {d}. ¿Cuál es la moda?", "gmoP": "Hay dos valores empatados en frecuencia: el conjunto es bimodal.", "gmo1": "{m} aparece tres veces.", "gmo2": "{m} aparecen dos veces cada uno: bimodal.", "gmo3": "Ningún valor se repite: no hay moda.",
  "gmoM1": "La moda es {m}, que aparece tres veces.", "gmoM2": "Hay dos modas: {m}.", "gmoM3": "Todos aparecen una sola vez: no hay moda.",
  "graQ1": "Temperaturas mínimas (°F): {d}. ¿Cuál es el rango?", "graQ2": "Datos: {d}. ¿Cuál es el rango?", "graS": "Máximo {M}, mínimo {m}: {M} − {p} = {r}.",
  "graP1": "Restar un negativo es sumar su opuesto: {M} − {p} = {M} + {q}.", "graP2": "Se usan el mayor y el menor de todos, no el primero y el último de la lista.",
  "atG": "El salario del gerente arrastra la media hasta {m}, más de lo que gana cualquiera de los otros cinco. La mediana, {me}, sigue representando bien al grupo.", "atN": "Sin valores extremos, la media y la mediana quedan muy cerca.",
  "sit": [["Los precios de las casas de un barrio, donde hay una mansión.", "med", "Un valor muy alto arrastra la media: conviene la mediana."], ["La talla de zapato más vendida en una tienda.", "moda", "Se busca lo más frecuente: la moda."], ["Las notas de un examen sin valores extremos.", "media", "Sin valores extremos, la media resume bien."], ["Los salarios de una empresa donde el dueño gana 20 veces más que los demás.", "med", "El salario del dueño es atípico: conviene la mediana."], ["El color de carro preferido por los clientes.", "moda", "Con datos que no son números, solo sirve la moda."], ["Los minutos que tarda en llegar un autobús, todos parecidos.", "media", "Datos parecidos y sin extremos: la media."]],
  "sitQ": " ¿Qué medida representa mejor al grupo?", "opMedia": "La media", "opMed": "La mediana", "opModa": "La moda",
  "po1": "{t} × 0.20 + {e} × 0.50 + {p} × 0.30 = {a} + {b} + {c}", "po2": "Nota final: {f}", "po3": "El promedio simple sería {s}. Como los exámenes pesan la mitad, su nota tira más de la media ponderada.",
  "pq1": "En un curso, las tareas valen {a}%, los exámenes {b}% y el proyecto {c}%. Un estudiante tiene {x} en tareas, {y} en exámenes y {z} en el proyecto. ¿Cuál es su nota final?", "pq1P": "Ese es el promedio simple. Cada nota tiene que multiplicarse por su peso.",
  "pq2": "Una tienda vendió {a} artículos a ${p}, {b} a ${q} y {c} a ${r}. ¿Cuál fue el precio promedio por artículo, en dólares? (Redondee a la centésima.)", "pq2P": "Ese es el promedio de los tres precios, sin tener en cuenta cuántos se vendieron de cada uno."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function par(n){ return n < 0 ? "(" + nd(n) + ")" : nd(n); }

/* ============ MODULE 1 · the four measures ============ */
function pintaMD(){
  var d = leeLista($("md-d").value), av = $("md-aviso");
  if (!d || d.length < 2){ av.className = "caja-aviso visible"; av.textContent = TXT.md1; $("md-d").classList.add("error"); $("md-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = ""; $("md-d").classList.remove("error");
  var o = ordenaN(d), n = o.length, m = Math.floor(n / 2), mo = modasDe(d), me = mediaDe(d);
  var cl = o.map(function(v, i){ return (n % 2 ? i === m : (i === m - 1 || i === m)) ? "med" : (mo.indexOf(v) >= 0 ? "moda" : ((i === 0 || i === n - 1) ? "ext" : "")); });
  $("md-salida").innerHTML = '<p>' + TXT.ord + '</p>' + chipsN(o, cl) +
    '<div class="medidas4"><div>' + TXT.media + '<strong>' + nd(Math.round(me * 100) / 100) + '</strong>' + nd(sumaDe(o)) + ' ÷ ' + n + '</div><div>' + TXT.mediana + '<strong>' + nd(medianaDe(d)) + '</strong>' + (n % 2 ? TXT.medio : TXT.dosMedio) + '</div><div>' + TXT.moda + '<strong>' + modaTxt(mo) + '</strong>' + (mo.length > 1 ? TXT.bimodal : "") + '</div><div>' + TXT.rango + '<strong>' + nd(o[n - 1] - o[0]) + '</strong>' + nd(o[n - 1]) + ' − ' + par(o[0]) + '</div></div>' +
    '<p class="nota">' + TXT.mdNota + '</p>';
}

/* ============ MODULE 2 · the mean ============ */
var ME = { d: [], rep: false };
function nuevoME(){
  var n = aleatorio(4, 6), prom = aleatorio(5, 12), d = [];
  for (var i = 0; i < n - 1; i++) d.push(Math.max(1, prom + aleatorio(-4, 4)));
  d.push(prom * n - sumaDe(d));
  if (d[n - 1] < 1 || d[n - 1] > 16) return nuevoME();
  ME.d = baraja(d); ME.rep = false; $("me-rep").textContent = TXT.meBtn; pintaME();
}
function pintaME(){
  var d = ME.d, n = d.length, s = sumaDe(d), m = s / n, u = 12, W = 640, x0 = 60, w = 60, g = (W - 2 * x0 - n * w) / (n - 1), yb = 240;
  $("me-datos").textContent = F(TXT.meDatos, { d: lista(d) });
  var sv = '<svg class="figura" viewBox="0 0 640 275" role="img" aria-label="' + (ME.rep ? F(TXT.meVozR, { m: nd(Math.round(m * 100) / 100) }) : F(TXT.meVoz, { d: lista(d) })) + '">';
  d.forEach(function(v, i){
    var h = ME.rep ? m : v, x = x0 + i * (w + g);
    for (var k = 0; k < Math.ceil(h); k++){ var hk = Math.min(1, h - k); sv += '<rect x="' + f1(x) + '" y="' + f1(yb - (k + hk) * u) + '" width="' + w + '" height="' + f1(hk * u - 1) + '" fill="' + (ME.rep ? "#64b5f6" : "#1565c0") + '"/>'; }
    sv += texto([x + w / 2, yb + 18], nd(ME.rep ? Math.round(m * 100) / 100 : v), 15, "#222");
  });
  sv += '<line x1="' + (x0 - 10) + '" y1="' + f1(yb - m * u) + '" x2="' + (W - x0 + 10) + '" y2="' + f1(yb - m * u) + '" stroke="#b71c1c" stroke-width="2" stroke-dasharray="7 5"/>';
  sv += '<text x="' + (W - x0 + 14) + '" y="' + f1(yb - m * u) + '" dominant-baseline="middle" font-size="13" font-weight="700" fill="#b71c1c">' + TXT.meMedia + '</text>';
  $("me-svg").innerHTML = sv + '</svg>';
  $("me-salida").innerHTML = '<div class="linea">' + F(TXT.meS, { s: d.join(" + "), t: s, n: n, m: nd(Math.round(m * 100) / 100) }) + '</div><div class="linea">' + (ME.rep ? F(TXT.meRep, { m: nd(Math.round(m * 100) / 100) }) : TXT.meLinea) + '</div>';
}
function genMedia(){
  var tp = aleatorio(1, 3);
  if (tp < 3){
    var n = aleatorio(4, 7), d = []; for (var i = 0; i < n; i++) d.push(aleatorio(60, 100));
    var m = Math.round(mediaDe(d) * 100) / 100, s = sumaDe(d), p = [{ v: s, msg: TXT.gmP1 }];
    if (Math.abs(medianaDe(d) - m) > 0.01) p.push({ v: medianaDe(d), msg: TXT.gmP2 });
    return { enun: F(tp === 1 ? TXT.gm1 : TXT.gm2, { d: lista(d), n: n }), correcta: nd(m), solucion: F(TXT.gmS, { s: s, n: n, m: nd(m) }), evalua: numD(m, p, null, 0.006) };
  }
  var k = aleatorio(3, 5), notas = [], obj = aleatorio(75, 90);
  for (var j = 0; j < k - 1; j++) notas.push(aleatorio(65, 95));
  var falta = obj * k - sumaDe(notas);
  if (falta < 50 || falta > 100 || falta === obj) return genMedia();
  return { enun: F(TXT.gm3, { k: k - 1, d: lista(notas), n: k, o: obj }), correcta: String(falta), solucion: F(TXT.gm3S, { o: obj, n: k, T: obj * k, y: obj * k - falta, f: falta }), evalua: numD(falta, [{ v: obj, msg: F(TXT.gm3P, { o: obj, T: obj * k }) }]) };
}

/* ============ MODULE 3 · the median ============ */
function genMediana(){
  var n = aleatorio(5, 10), d = [];
  while (d.length < n){ var x = aleatorio(5, 60); if (d.indexOf(x) < 0 || Math.random() < 0.15) d.push(x); }
  var o = ordenaN(d), me = medianaDe(d), m = Math.floor(n / 2), centro = n % 2 ? d[m] : (d[m - 1] + d[m]) / 2;
  var sol = n % 2 ? F(TXT.gmeS1, { o: lista(o), n: n, k: m + 1, m: nd(me) }) : F(TXT.gmeS2, { o: lista(o), n: n, a: o[m - 1], b: o[m], m: nd(me) });
  return { enun: F(TXT.gmeQ, { d: lista(d) }), correcta: nd(me), solucion: sol, evalua: numD(me, centro !== me ? [{ v: centro, msg: TXT.gmeP }] : [], null, 0.001) };
}

/* ============ MODULE 4 · the mode and the range ============ */
function genModa(){
  var tp = aleatorio(1, 3), d = [];
  if (tp === 1){ var mo = aleatorio(5, 20); d = [mo, mo, mo]; while (d.length < 7){ var x = aleatorio(3, 25); if (d.indexOf(x) < 0) d.push(x); } }
  else if (tp === 2){ var a = aleatorio(5, 12), b = aleatorio(13, 20); d = [a, a, b, b]; while (d.length < 7){ var y = aleatorio(3, 25); if (d.indexOf(y) < 0) d.push(y); } }
  else { while (d.length < 6){ var z = aleatorio(3, 30); if (d.indexOf(z) < 0) d.push(z); } }
  d = baraja(d);
  var m = modasDe(d), cor = modaTxt(m), o = [cor, TXS.sinModa, nd(medianaDe(d)), nd(Math.max.apply(null, d))], pc = {};
  if (tp === 2){ o.push(nd(m[0])); pc[nd(m[0])] = TXT.gmoP; }
  if (tp === 1) o.push(nd(ordenaN(d)[0]));
  o = o.filter(function(x, i, arr){ return arr.indexOf(x) === i; }).slice(0, 4);
  var mm = m.map(nd).join(TXS.y);
  return { enun: F(TXT.gmoQ, { d: lista(d) }), opciones: baraja(o).map(function(x){ return { html: x.charAt(0).toUpperCase() + x.slice(1), clave: x }; }), correcta: cor, pistas: pc,
    bien: F(tp === 3 ? TXT.gmo3 : (tp === 2 ? TXT.gmo2 : TXT.gmo1), { m: mm }), mal: F(tp === 3 ? TXT.gmoM3 : (tp === 2 ? TXT.gmoM2 : TXT.gmoM1), { m: mm }) };
}
function genRango(){
  var neg = Math.random() < 0.3, d = [], n = aleatorio(5, 9);
  for (var i = 0; i < n; i++) d.push(neg ? aleatorio(-15, 20) : aleatorio(2, 99));
  var mx = Math.max.apply(null, d), mn = Math.min.apply(null, d), r = mx - mn;
  if (neg && mn >= 0) return genRango();
  var p = mn < 0 ? [{ v: mx + mn, msg: F(TXT.graP1, { M: nd(mx), p: par(mn), q: nd(-mn) }) }] : [{ v: Math.abs(d[d.length - 1] - d[0]), msg: TXT.graP2 }];
  p = p.filter(function(x){ return x.v !== r; });
  return { enun: F(neg ? TXT.graQ1 : TXT.graQ2, { d: d.map(nd).join(", ") }), correcta: String(r), solucion: F(TXT.graS, { M: nd(mx), m: nd(mn), p: par(mn), r: r }), evalua: numD(r, p) };
}

/* ============ MODULE 5 · outliers ============ */
var SAL = [2900, 3000, 3100, 3200, 3300];
function pintaAT(){
  var g = +$("at-g").value, d = SAL.concat([g]), m = mediaDe(d), me = medianaDe(d), o = ordenaN(d);
  $("at-gv").textContent = dinero(g);
  $("at-salida").innerHTML = chipsN(o, o.map(function(v){ return v === g && g > 5000 ? "ext" : ""; }), o.map(dinero)) +
    '<div class="medidas4"><div>' + TXT.media + '<strong>' + dinero(Math.round(m)) + '</strong></div><div>' + TXT.mediana + '<strong>' + dinero(me) + '</strong></div></div>' +
    '<div class="salida"><div class="linea">' + (g > 5000 ? F(TXT.atG, { m: dinero(Math.round(m)), me: dinero(me) }) : TXT.atN) + '</div></div>';
}
function genSit(){
  var s = elige(TXT.sit);
  return { enun: s[0] + TXT.sitQ, opciones: [{ html: TXT.opMedia, clave: "media" }, { html: TXT.opMed, clave: "med" }, { html: TXT.opModa, clave: "moda" }], correcta: s[1], enOrden: true, bien: s[2], mal: s[2] };
}

/* ============ MODULE 6 · the weighted mean ============ */
function pintaPO(){
  var tt = +$("po-t").value, e = +$("po-e").value, p = +$("po-p").value, f = tt * 0.2 + e * 0.5 + p * 0.3, s = (tt + e + p) / 3;
  $("po-tv").textContent = tt; $("po-ev").textContent = e; $("po-pv").textContent = p;
  $("po-salida").innerHTML = '<div class="linea">' + F(TXT.po1, { t: tt, e: e, p: p, a: nd(r2(tt * 0.2)), b: nd(r2(e * 0.5)), c: nd(r2(p * 0.3)) }) + '</div><div class="linea veredicto">' + F(TXT.po2, { f: nd(r2(f)) }) + '</div><div class="linea">' + F(TXT.po3, { s: nd(r2(s)) }) + '</div>';
}
function r2(x){ return Math.round(x * 100) / 100; }
function genPond(){
  if (Math.random() < 0.5){
    var w = elige([[20, 50, 30], [25, 50, 25], [10, 60, 30], [30, 40, 30]]), n = [aleatorio(60, 100), aleatorio(55, 100), aleatorio(60, 100)], f = (n[0] * w[0] + n[1] * w[1] + n[2] * w[2]) / 100;
    var p = Math.abs(r2((n[0] + n[1] + n[2]) / 3) - f) > 0.01 ? [{ v: r2((n[0] + n[1] + n[2]) / 3), msg: TXT.pq1P }] : [];
    return { enun: F(TXT.pq1, { a: w[0], b: w[1], c: w[2], x: n[0], y: n[1], z: n[2] }), correcta: nd(r2(f)),
      solucion: n[0] + " × " + nd(w[0] / 100) + " + " + n[1] + " × " + nd(w[1] / 100) + " + " + n[2] + " × " + nd(w[2] / 100) + " = " + nd(r2(f)) + ".", evalua: numD(f, p, null, 0.006) };
  }
  var pr = [aleatorio(2, 5), aleatorio(6, 9), aleatorio(10, 15)], c = [aleatorio(10, 40), aleatorio(10, 40), aleatorio(5, 20)], tot = sumaDe(c), sp = pr[0] * c[0] + pr[1] * c[1] + pr[2] * c[2], mp = sp / tot;
  var p2 = Math.abs(r2(sumaDe(pr) / 3) - r2(mp)) > 0.01 ? [{ v: r2(sumaDe(pr) / 3), msg: TXT.pq2P }] : [];
  return { enun: F(TXT.pq2, { a: c[0], p: pr[0], b: c[1], q: pr[1], c: c[2], r: pr[2] }), correcta: nd(r2(mp)),
    solucion: "(" + pr[0] + " × " + c[0] + " + " + pr[1] + " × " + c[1] + " + " + pr[2] + " × " + c[2] + ") ÷ " + tot + " = " + nd(sp) + " ÷ " + tot + " ≈ " + nd(r2(mp)) + ".", evalua: numD(r2(mp), p2, null, 0.006) };
}

/* ============ Start ============ */
$("md-d").addEventListener("input", pintaMD); pintaMD();
$("me-rep").addEventListener("click", function(){ ME.rep = !ME.rep; $("me-rep").textContent = ME.rep ? TXT.meBtn2 : TXT.meBtn; pintaME(); }); $("me-nuevo").addEventListener("click", nuevoME); nuevoME();
creaPracticaLibre("p1", genMedia);
creaPracticaLibre("p2", genMediana);
creaPracticaOM("p3", genModa);
creaPracticaLibre("p4", genRango);
$("at-g").addEventListener("input", pintaAT); pintaAT();
creaPracticaOM("p5", genSit);
["po-t", "po-e", "po-p"].forEach(function(id){ $(id).addEventListener("input", pintaPO); }); pintaPO();
creaPracticaLibre("p6", genPond);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

NOTA = ("Type only the number. It may have decimals, like 84.25.", "Escriba solo el número. Puede llevar decimales, como 84.25.")

def practica_pagina():
    n = N
    def desl(i, et, vmin, vmax, val, paso=1):
        return f'<div class="campo" style="flex:1;min-width:150px;"><label for="{i}">{et}: <span id="{i}v"></span></label><input type="range" id="{i}" min="{vmin}" max="{vmax}" step="{paso}" value="{val}"></div>'
    mods = [
     (t("four-measures", "cuatro-medidas"), t("The four measures at a glance", "Las cuatro medidas en una mirada"),
      f'''      <table class="reglas">
        <caption>{t("Four ways to sum up a set of data", "Cuatro formas de resumir un conjunto de datos")}</caption>
        <thead><tr><th scope="col">{t("Measure", "Medida")}</th><th scope="col">{t("What it tells you", "Qué dice")}</th><th scope="col">{t("How to find it", "Cómo se calcula")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Mean", "Media")}</td><td>{t("the average", "el promedio")}</td><td>{t("sum ÷ number of values", "suma ÷ cantidad de datos")}</td></tr>
          <tr><td>{t("Median", "Mediana")}</td><td>{t("the middle value", "el valor del centro")}</td><td>{t("put the data in order and find the middle", "se ordenan y se busca el del medio")}</td></tr>
          <tr><td>{t("Mode", "Moda")}</td><td>{t("the most frequent value", "el valor más frecuente")}</td><td>{t("the one that repeats the most", "el que más se repite")}</td></tr>
          <tr><td>{t("Range", "Rango")}</td><td>{t("how spread out the data is", "qué tan dispersos están")}</td><td>{t("greatest − least", "máximo − mínimo")}</td></tr>
        </tbody>
      </table>
      <h3>{t("Calculator for the four measures", "Calculadora de las cuatro medidas")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;"><label for="md-d">{t("Type the data separated by commas", "Escriba los datos separados por comas")}</label><input type="text" class="ancho" id="md-d" autocomplete="off" value="78, 85, 90, 72, 95"></div></div>
        <div class="caja-aviso" id="md-aviso" role="alert"></div>
        <div id="md-salida" aria-live="polite"></div>
      </div>'''),
     (t("mean", "media"), t("The mean", "La media aritmética"),
      f'''      <p>{t("The mean, or average, is the sum of all the values divided by how many there are. It is what each one would get if everything were <strong>shared out equally</strong>.", "La media o promedio se obtiene sumando todos los datos y dividiendo entre cuántos son. Es lo que le tocaría a cada uno si todo se <strong>repartiera en partes iguales</strong>.")}</p>
      <h3>{t("Level the towers", "Empareje las torres")}</h3>
      <div class="panel">
        <p id="me-datos"></p>
        <div class="fila-btn"><button type="button" class="btn" id="me-rep">{t("Share equally", "Repartir en partes iguales")}</button><button type="button" class="btn-sec" id="me-nuevo">{t("Other data", "Otros datos")}</button></div>
        <div id="me-svg"></div>
        <div class="salida" id="me-salida" aria-live="polite"></div>
      </div>
{libre_x("p1", t("Practice: the mean", "Practique: la media"), t("Mean", "Media"), t(*NOTA))}'''),
     (t("median", "mediana"), t("The median", "La mediana"),
      f'''      <p>{t("First <strong>put the data in order</strong>. With an odd number of values, the median is the one in the middle; with an even number, it is the average of the two in the middle.", "Primero se <strong>ordenan los datos</strong>. Si la cantidad es impar, la mediana es el del medio; si es par, es el promedio de los dos del medio.")}</p>
      <div class="caja-atencion"><strong>{t("Common mistake:", "Error frecuente:")}</strong> {t("taking the middle value of the list without putting it in order first.", "tomar el valor del centro de la lista sin haberla ordenado.")}</div>
{libre_x("p2", t("Practice: the median", "Practique: la mediana"), t("Median", "Mediana"), t(*NOTA))}'''),
     (t("mode-range", "moda-rango"), t("The mode and the range", "La moda y el rango"),
      f'''      <p>{t("The <strong>mode</strong> is the value that repeats the most. There can be one, two (bimodal), or none. The <strong>range</strong> is greatest − least: it measures how spread out the data is.", "La <strong>moda</strong> es el valor que más se repite. Puede haber una, dos (bimodal) o ninguna. El <strong>rango</strong> es máximo − mínimo: mide qué tan dispersos están los datos.")}</p>
{B.om("p3", t("Practice: the mode", "Practique: la moda"))}
{libre_x("p4", t("Practice: the range", "Practique: el rango"), t("Range", "Rango"), t("Type only the number.", "Escriba solo el número."))}'''),
     (t("outliers", "atipicos"), t("When the mean misleads", "Cuando la media engaña"),
      f'''      <p>{t("Five employees earn between $2,900 and $3,300 a month. Move the sixth salary, the manager's, and watch the mean and the median.", "Cinco empleados ganan entre $2,900 y $3,300 al mes. Mueva el sexto salario, el del gerente, y observe la media y la mediana.")}</p>
      <div class="panel">
        <div class="campos">{desl("at-g", t("Manager's salary ($)", "Salario del gerente ($)"), 3500, 30000, 3500, 500)}</div>
        <div id="at-salida" aria-live="polite"></div>
      </div>
{B.om("p5", t("Practice: which measure?", "Practique: ¿qué medida?"))}'''),
     (t("weighted-mean", "ponderada"), t("The weighted mean", "La media ponderada"),
      f'''      <div class="formula">{t("weighted mean = Σ(value × weight) ÷ Σ(weights)", "media ponderada = Σ(valor × peso) ÷ Σ(pesos)")}</div>
      <p>{t("When the weights are percents that add to 100%, multiply each score by its percent as a decimal and add.", "Cuando los pesos son porcentajes que suman 100%, se multiplica cada nota por su porcentaje en decimal y se suma.")}</p>
      <h3>{t("A course grade", "La nota de un curso")}</h3>
      <div class="panel">
        <div class="campos">
          {desl("po-t", t("Homework (20%)", "Tareas (20%)"), 0, 100, 90)}
          {desl("po-e", t("Exams (50%)", "Exámenes (50%)"), 0, 100, 70)}
          {desl("po-p", t("Project (30%)", "Proyecto (30%)"), 0, 100, 85)}
        </div>
        <div class="salida" id="po-salida" aria-live="polite"></div>
      </div>
{libre_x("p6", t("Practice: the weighted mean", "Practique: la media ponderada"), t("Answer", "Resultado"), t(*NOTA))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 8, t(*TEMA), t(*TIT),
        t("Six practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Seis actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js", "/math/stats.js"))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Media, mediana, moda, rango y media ponderada")
