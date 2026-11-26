"""Level 2 · Lesson 4.3 · Inverse proportions and mixed applications — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg
from n2 import fr

B.NIVEL = 2
N = "4-3"
TEMA = ("Ratios, rates, and proportions", "Razones, proporciones y porcentajes")
TIT = ("Inverse proportions and mixed applications", "Proporciones inversas y aplicaciones mixtas")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def graficas():
    """Directa: recta desde el origen. Inversa: curva que baja (x·y = 24)."""
    def ejes(x0):
        return (f'<line x1="{x0}" y1="190" x2="{x0 + 230}" y2="190" stroke="#424242" stroke-width="2"/>'
                f'<line x1="{x0}" y1="190" x2="{x0}" y2="20" stroke="#424242" stroke-width="2"/>')
    d = ejes(40) + '<line x1="40" y1="190" x2="250" y2="40" stroke="#1565c0" stroke-width="4"/>'
    d += f'<text x="145" y="215" text-anchor="middle" font-size="15" font-weight="700" fill="#1565c0">{t("Direct: a straight line from 0", "Directa: recta que sale del 0")}</text>'
    pts = " ".join(f"{330 + x * 9:.1f},{190 - (24 / x) * 6:.1f}" for x in [1 + i * 0.25 for i in range(0, 93)])
    d += ejes(330) + f'<polyline points="{pts}" fill="none" stroke="#bf360c" stroke-width="4"/>'
    d += f'<text x="445" y="215" text-anchor="middle" font-size="15" font-weight="700" fill="#bf360c">{t("Inverse: a curve that goes down", "Inversa: curva que baja")}</text>'
    return svg("0 0 600 225", t("Two graphs. Direct proportion: a straight line that starts at zero and goes up. Inverse proportion: a curve that starts high and goes down, getting closer to the horizontal axis.",
                               "Dos gráficas. Proporción directa: una recta que sale del cero y sube. Proporción inversa: una curva que empieza alta y baja, acercándose al eje horizontal."), d, 600)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 4.2 you worked with direct proportions: if one quantity grows, the other grows in the same ratio. But not every situation works that way. If you hire more painters, the building gets painted in fewer days. This lesson presents <strong>inverse proportions</strong> and teaches you to decide, before you calculate, which kind each problem is.",
"En la Lección 4.2 trabajó con la proporcionalidad directa: si una cantidad crece, la otra crece en la misma razón. Pero no todas las situaciones funcionan así. Si se contratan más pintores, el edificio se pinta en menos días. Esta lección presenta la <strong>proporcionalidad inversa</strong> y enseña a decidir, antes de calcular, cuál de los dos tipos corresponde a cada problema.")}</p>
<p>{t("Before you set up any proportion, ask one question: <strong>if one quantity doubles, what happens to the other?</strong>", "Antes de plantear cualquier proporción, hágase una sola pregunta: <strong>si una cantidad se duplica, ¿qué le pasa a la otra?</strong>")}</p>
{tabla(t("Direct and inverse proportion", "Proporción directa e inversa"), t("The two kinds of proportion compared", "Comparación de los dos tipos de proporcionalidad"),
       ["", t("Direct", "Directa"), t("Inverse", "Inversa")],
       [[t("If X doubles…", "Si X se duplica…"), t("Y doubles", "Y se duplica"), t("Y is cut in half", "Y se reduce a la mitad")],
        [t("What stays the same", "Lo que no cambia"), t("the quotient: Y ÷ X = k", "el cociente: Y ÷ X = k"), t("the product: X × Y = k", "el producto: X × Y = k")],
        [t("Example", "Ejemplo"), t("twice the pounds of apples cost twice the money", "el doble de libras de manzanas cuesta el doble"), t("twice the workers finish in half the time", "el doble de obreros termina en la mitad del tiempo")]])}
{caja("ojo", t("Going down is not enough", "No basta con que baje"), t("<p>For a proportion to be inverse, when one quantity doubles the other must become exactly half; when one triples, the other must become one third. If you spend money and your balance goes down, that is not an inverse proportion: it is a subtraction.</p>", "<p>Para que sea inversa, al duplicar una cantidad la otra debe quedar exactamente a la mitad; al triplicarla, en la tercera parte. Si una persona gasta dinero y su saldo baja, eso no es proporcionalidad inversa: es una resta.</p>"))}
{practica("p1", t("Practice 1 — Hours and pay", "Práctica 1 — Horas y sueldo"), t("The more hours you work, the more pay you get (paid by the hour).", "A más horas trabajadas, más sueldo (pago por hora)."),
          [("a", t("Inverse", "Inversa")), ("b", t("Direct", "Directa"))])}
{practica("p2", t("Practice 2 — Sharing a pizza", "Práctica 2 — Repartir una pizza"), t("A pizza of a fixed size is shared by more people: each one gets less.", "Una pizza de tamaño fijo se reparte entre más personas: a cada una le toca menos."),
          [("a", t("Inverse", "Inversa")), ("b", t("Direct", "Directa"))])}
{practica("p3", t("Practice 3 — Speed and time", "Práctica 3 — Velocidad y tiempo"), t("The faster you drive, the less time it takes to go the same distance.", "A mayor velocidad, menos tiempo para recorrer la misma distancia."),
          [("a", t("Direct", "Directa")), ("b", t("Inverse", "Inversa"))])}
{enlace(n, t("direct-or-inverse", "directa-inversa"), t("direct or inverse", "directa frente a inversa"), t("See what grows and what shrinks, and ask: if X doubles, what happens to Y?", "Observe qué crece y qué disminuye, y pregúntese: si duplico X, ¿qué le pasa a Y?"))}'''

    s2 = f'''<p>{t("In an inverse proportion, the product of the two quantities is always the same number. That number is the <strong>constant</strong> k, and it usually stands for the “total work.”", "En una proporción inversa, el producto de las dos cantidades es siempre el mismo número. Ese número es la <strong>constante</strong> k y suele representar el «trabajo total».")}</p>
{tabla(t("Workers and days to finish the same job", "Obreros y días para terminar la misma obra"), t("Workers, days, and workers times days", "Obreros, días y obreros por días"),
       [t("Workers", "Obreros"), "2", "4", "6", "12"], [[t("Days", "Días"), "24", "12", "8", "4"], [t("Workers × days", "Obreros × días"), "48", "48", "48", "48"]])}
<p>{t("The product is always 48: the job takes 48 “worker-days” of work, however you split them.", "El producto es siempre 48: la obra requiere 48 «días-obrero» de trabajo, se repartan como se repartan.")}</p>
{graficas()}
{caja("tip", t("The idea that ties it together", "La idea que lo une todo"), t("<p>In a direct proportion the <strong>division</strong> (Y ÷ X) stays the same; in an inverse proportion the <strong>multiplication</strong> (X × Y) stays the same. Knowing what stays the same is the key to all of Topic 4.</p>", "<p>En la directa se mantiene constante la <strong>división</strong> (Y ÷ X); en la inversa se mantiene constante la <strong>multiplicación</strong> (X × Y). Saber qué permanece constante es la clave de todo el Tema 4.</p>"))}
{practica("p4", t("Practice 4 — Faucets", "Práctica 4 — Llaves de agua"), t("Several identical faucets fill a tank: with more faucets open, it takes less time. What kind of proportion is it?", "Varias llaves iguales llenan un tanque: con más llaves abiertas, menos tiempo. ¿Qué tipo de proporción es?"),
          [("a", t("Direct", "Directa")), ("b", t("Inverse", "Inversa"))])}'''

    s3 = f'''<p>{t("There are two ways to solve an inverse proportion, and they give the same answer. The first uses the constant: find k with the complete data and divide it by the new value. The second is the <strong>inverse rule of three</strong>: multiply straight across (not crosswise) and divide by the remaining value.", "Hay dos formas equivalentes de resolver una proporción inversa. La primera usa la constante: se calcula k con los datos completos y se divide entre el dato nuevo. La segunda es la <strong>regla de tres inversa</strong>: se multiplica en línea recta (no en cruz) y se divide entre el dato restante.")}</p>
{ej(t("Example: workers and time", "Ejemplo: obreros y tiempo"), t("Four workers take 9 days to finish a job. How many days would 6 workers take, working at the same pace?", "Cuatro obreros tardan 9 días en terminar una obra. ¿Cuántos días tardarían 6 obreros, trabajando al mismo ritmo?"),
  [("1", t("Ask the question.", "Hágase la pregunta."), t("More workers, fewer days: it is inverse.", "Más obreros, menos días: es inversa.")),
   ("2", t("The constant.", "La constante."), t("k = 4 × 9 = 36 worker-days.", "k = 4 × 9 = 36 días-obrero.")),
   ("3", t("With 6 workers.", "Con 6 obreros."), "6 × x = 36 → x = 36 ÷ 6 = 6."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>6 days</strong>", "<strong>6 días</strong>"))])}
{ej(t("Example: speed and time", "Ejemplo: velocidad y tiempo"), t("A bus covers a route at 60 mph in 5 hours. How long would it take at 75 mph?", "Un autobús cubre una ruta a 60 mph en 5 horas. ¿Cuánto tardaría a 75 mph?"),
  [("1", t("Inverse.", "Inversa."), t("Faster, less time. The constant is the distance: 60 × 5 = 300 miles.", "Más velocidad, menos tiempo. La constante es la distancia: 60 × 5 = 300 millas.")),
   ("2", t("At 75 mph.", "A 75 mph."), "75 × x = 300 → x = 300 ÷ 75 = 4."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>4 hours</strong>", "<strong>4 horas</strong>"))])}
{ej(t("Example: supplies", "Ejemplo: provisiones"), t("The supplies at a camp last 12 people for 10 days. If 3 more people arrive, how many days will the supplies last?", "Las provisiones de un campamento alcanzan para 12 personas durante 10 días. Si llegan 3 personas más, ¿para cuántos días alcanzan?"),
  [("1", t("Inverse.", "Inversa."), t("More people, fewer days. k = 12 × 10 = 120 rations.", "Más personas, menos días. k = 12 × 10 = 120 raciones.")),
   ("2", t("Now 15 people.", "Ahora son 15 personas."), "x = 120 ÷ 15 = 8."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>8 days</strong>", "<strong>8 días</strong>"))])}
{ej(t("Example from science: pressure and volume", "Ejemplo de ciencias: presión y volumen"), t("At a constant temperature, a gas takes up 6 liters at a pressure of 2 atmospheres. What volume does it take up at 3 atmospheres?", "A temperatura constante, un gas ocupa 6 litros a una presión de 2 atmósferas. ¿Qué volumen ocupa a 3 atmósferas?"),
  [("1", t("Inverse.", "Inversa."), t("More pressure squeezes the gas. k = 2 × 6 = 12.", "Al aumentar la presión, el gas se comprime. k = 2 × 6 = 12.")),
   ("2", t("At 3 atmospheres.", "A 3 atmósferas."), "x = 12 ÷ 3 = 4."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>4 liters</strong>. In science this is called Boyle's law.", "<strong>4 litros</strong>. En ciencias esta relación se conoce como la ley de Boyle."))])}
{caja("ojo", t("The typical mistake", "El error típico"), t("<p>Using the cross products of a direct proportion on an inverse problem. In the workers example it would give 4/9 = 6/x, so x = 13.5 days. That answer says that more workers take <em>longer</em>, which makes no sense. Common sense is the best check.</p>", "<p>Usar el producto cruzado de la proporción directa en un problema inverso. En el ejemplo de los obreros daría 4/9 = 6/x, es decir, x = 13.5 días. Ese resultado dice que con más obreros se tarda <em>más</em>, lo cual no tiene sentido. El sentido común es la mejor verificación.</p>"))}
{practica("p5", t("Practice 5 — Workers", "Práctica 5 — Obreros"), t("Three workers take 12 days. How many days do 9 workers take?", "Tres obreros tardan 12 días. ¿Cuántos días tardan 9 obreros?"),
          [("a", t("36 days", "36 días")), ("b", t("4 days", "4 días")), ("c", t("6 days", "6 días")), ("d", t("18 days", "18 días"))])}
{practica("p6", t("Practice 6 — A trip", "Práctica 6 — Un viaje"), t("At 40 mph a trip takes 6 hours. How many hours does it take at 60 mph?", "A 40 mph un viaje toma 6 horas. ¿Cuántas horas toma a 60 mph?"),
          [("a", t("9 hours", "9 horas")), ("b", t("3 hours", "3 horas")), ("c", t("4 hours", "4 horas")), ("d", t("5 hours", "5 horas"))])}
{enlace(n, t("inverse", "inversas"), t("solving inverse proportions", "resolver proporciones inversas"), t("Find the constant product and divide it by the new quantity.", "Calcule el producto constante y divídalo entre la cantidad nueva."))}'''

    s4 = f'''<p>{t("On the GED, problems do not tell you what kind they are. For any proportion problem: (1) ask the question “if X doubles, what happens to Y?”; (2) choose the method (constant ratio or constant product); (3) solve; (4) check that the answer makes sense.", "En el GED los problemas no anuncian de qué tipo son. Para cualquier problema de proporciones: (1) hágase la pregunta «si duplico X, ¿qué le pasa a Y?»; (2) elija el método (razón constante o producto constante); (3) resuelva; (4) compruebe que el resultado tiene sentido.")}</p>
{ej(t("Example: one context, two questions", "Ejemplo: un mismo contexto, dos preguntas"), t("In a factory, 5 identical machines make 400 parts in 8 hours.", "En una fábrica, 5 máquinas iguales producen 400 piezas en 8 horas."),
  [("a", t("Same 5 machines, 12 hours?", "¿Las mismas 5 máquinas en 12 horas?"), t(f"More hours, more parts: <strong>direct</strong>. {fr(400, 8)} = {fr('x', 12)} → x = 400 × 12 ÷ 8 = <strong>600 parts</strong>.", f"Más horas, más piezas: <strong>directa</strong>. {fr(400, 8)} = {fr('x', 12)} → x = 400 × 12 ÷ 8 = <strong>600 piezas</strong>.")),
   ("b", t("8 machines, the same 400 parts?", "¿8 máquinas para las mismas 400 piezas?"), t("More machines, less time: <strong>inverse</strong>. k = 5 × 8 = 40 machine-hours → x = 40 ÷ 8 = <strong>5 hours</strong>.", "Más máquinas, menos tiempo: <strong>inversa</strong>. k = 5 × 8 = 40 horas-máquina → x = 40 ÷ 8 = <strong>5 horas</strong>.")),
   ("✓", t("Moral.", "Moraleja."), t("The context does not decide the type; the pair of quantities you compare does.", "El contexto no decide el tipo; lo decide qué par de cantidades se compara."))])}
{calc(t("Inverse proportions on the calculator", "Proporciones inversas en la calculadora"), t(f"<p>For 4 workers and 9 days, with 6 workers: type {T('4')} {T('×')} {T('9')} {T('÷')} {T('6')} {T('enter')}. The screen shows 6.</p>", f"<p>Para 4 obreros y 9 días, con 6 obreros: escriba {T('4')} {T('×')} {T('9')} {T('÷')} {T('6')} {T('enter')}. La pantalla muestra 6.</p>"))}
{practica("p7", t("Practice 7 — Meat", "Práctica 7 — Carne"), t("Three pounds of meat cost $13.50. How much do 5 pounds cost?", "Tres libras de carne cuestan $13.50. ¿Cuánto cuestan 5 libras?"),
          [("a", "$8.10"), ("b", "$22.50"), ("c", "$18.50"), ("d", "$4.50")])}
{practica("p8", t("Practice 8 — Two faucets", "Práctica 8 — Dos llaves"), t("One faucet fills a tank in 6 hours. How long do 2 identical faucets take?", "Una llave llena un tanque en 6 horas. ¿Cuánto tardan 2 llaves iguales?"),
          [("a", t("12 hours", "12 horas")), ("b", t("4 hours", "4 horas")), ("c", t("2 hours", "2 horas")), ("d", t("3 hours", "3 horas"))])}
{enlace(n, t("mixed", "mixtas"), t("mixed applications", "aplicaciones mixtas"), t("Decide first whether each problem is direct or inverse, then solve it.", "Decida primero si cada problema es directo o inverso y después resuélvalo."))}'''

    secciones = [("s-" + t("question", "pregunta"), t("The key question: “If X doubles, what happens to Y?”", "La pregunta diagnóstica: «si duplico X, ¿qué le pasa a Y?»"), s1),
                 ("s-" + t("constant", "constante"), t("The constant k = x × y", "La constante k = x × y"), s2),
                 ("s-" + t("inverse", "inversas"), t("Solving inverse proportions", "Resolver proporciones inversas"), s3),
                 ("s-" + t("mixed", "mixtas"), t("Mixed applications", "Aplicaciones mixtas"), s4)]

    lesson = {"next": t("Topic 5", "el Tema 5"), "review": t("sections 1, 3, and 4", "las secciones 1, 3 y 4"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("If you work twice the hours, what happens to your pay?", "Si trabaja el doble de horas, ¿qué le pasa al sueldo?")}, "right": t("Twice the hours, twice the pay: direct.", "El doble de horas, el doble de sueldo: directa."), "solution": t("If the hours double, the pay doubles too. It is direct.", "Si las horas se duplican, el sueldo también. Es directa.")},
      "p2": {"ok": "a", "hints": {"b": t("If twice as many people share it, each one gets…?", "Si la comparten el doble de personas, a cada una le toca…")}, "right": t("Twice the people, half the pizza each: inverse.", "El doble de personas, la mitad para cada una: inversa."), "solution": t("If the number of people doubles, each share is cut in half. It is inverse.", "Si el número de personas se duplica, cada porción se reduce a la mitad. Es inversa.")},
      "p3": {"ok": "b", "hints": {"a": t("If you drive twice as fast, what happens to the time?", "Si va al doble de velocidad, ¿qué le pasa al tiempo?")}, "right": t("Twice the speed, half the time: inverse.", "El doble de velocidad, la mitad del tiempo: inversa."), "solution": t("If the speed doubles, the time is cut in half. Speed × time = distance stays the same. It is inverse.", "Si la velocidad se duplica, el tiempo se reduce a la mitad. Velocidad × tiempo = distancia no cambia. Es inversa.")},
      "p4": {"ok": "b", "hints": {"a": t("With twice as many faucets, does it take twice as long?", "Con el doble de llaves, ¿tarda el doble?")}, "right": t("Twice the faucets, half the time: inverse.", "El doble de llaves, la mitad del tiempo: inversa."), "solution": t("Faucets × time stays the same (the size of the tank). It is inverse.", "Llaves × tiempo no cambia (el tamaño del tanque). Es inversa.")},
      "p5": {"ok": "b", "hints": {"a": t("That would be direct. More workers take fewer days.", "Eso sería directa. Más obreros tardan menos días."), "c": t("Check: k = 3 × 12 = 36, and 36 ÷ 9.", "Revise: k = 3 × 12 = 36, y 36 ÷ 9."), "d": t("You subtracted. Use k = 3 × 12.", "Restó. Use k = 3 × 12.")},
             "right": t("k = 3 × 12 = 36; 36 ÷ 9 = 4 days.", "k = 3 × 12 = 36; 36 ÷ 9 = 4 días."), "solution": t("Inverse: k = 3 × 12 = 36 worker-days. With 9 workers: 36 ÷ 9 = 4 days.", "Inversa: k = 3 × 12 = 36 días-obrero. Con 9 obreros: 36 ÷ 9 = 4 días.")},
      "p6": {"ok": "c", "hints": {"a": t("That would be direct. Faster takes less time.", "Eso sería directa. Más rápido tarda menos."), "b": t("Check: 40 × 6 = 240 miles, and 240 ÷ 60.", "Revise: 40 × 6 = 240 millas, y 240 ÷ 60."), "d": t("Check: 240 ÷ 60.", "Revise: 240 ÷ 60.")},
             "right": t("40 × 6 = 240 miles; 240 ÷ 60 = 4 hours.", "40 × 6 = 240 millas; 240 ÷ 60 = 4 horas."), "solution": t("Inverse: the distance stays the same, 40 × 6 = 240 miles. At 60 mph: 240 ÷ 60 = 4 hours.", "Inversa: la distancia no cambia, 40 × 6 = 240 millas. A 60 mph: 240 ÷ 60 = 4 horas.")},
      "p7": {"ok": "b", "hints": {"a": t("You used the inverse method. More pounds cost more: it is direct.", "Usó el método inverso. Más libras cuestan más: es directa."), "c": t("You added. Use the price per pound: $13.50 ÷ 3.", "Sumó. Use el precio por libra: $13.50 ÷ 3."), "d": t("$4.50 is the price of 1 pound. Multiply by 5.", "$4.50 es el precio de 1 libra. Multiplique por 5.")},
             "right": t("$13.50 ÷ 3 = $4.50; × 5 = $22.50.", "$13.50 ÷ 3 = $4.50; × 5 = $22.50."), "solution": t("Direct: 1 pound costs $13.50 ÷ 3 = $4.50, so 5 pounds cost $22.50.", "Directa: 1 libra cuesta $13.50 ÷ 3 = $4.50, así que 5 libras cuestan $22.50.")},
      "p8": {"ok": "d", "hints": {"a": t("That would be direct. Two faucets fill it faster.", "Eso sería directa. Dos llaves la llenan más rápido."), "b": t("Check: k = 1 × 6 = 6, and 6 ÷ 2.", "Revise: k = 1 × 6 = 6, y 6 ÷ 2."), "c": t("Check: 6 ÷ 2.", "Revise: 6 ÷ 2.")},
             "right": t("1 × 6 = 6; 6 ÷ 2 = 3 hours.", "1 × 6 = 6; 6 ÷ 2 = 3 horas."), "solution": t("Inverse: k = 1 × 6 = 6 faucet-hours. With 2 faucets: 6 ÷ 2 = 3 hours.", "Inversa: k = 1 × 6 = 6 horas-llave. Con 2 llaves: 6 ÷ 2 = 3 horas.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("Going down is not enough: is there a product that stays the same?", "No basta con que baje: ¿hay un producto que no cambie?"), "b": t("If you buy twice the gallons, you pay twice: that is direct.", "Si compra el doble de galones, paga el doble: eso es directa."), "d": t("More hours, more pay: direct.", "Más horas, más sueldo: directa.")}, "solution": t("Twice the workers finish in half the time: inverse.", "El doble de obreros termina en la mitad del tiempo: inversa.")},
      "B": {"ok": "a", "hints": {"b": t("That is the direct proportion.", "Esa es la directa."), "c": t("A sum does not stay the same here.", "Aquí la suma no se mantiene."), "d": t("A difference does not stay the same here.", "Aquí la diferencia no se mantiene.")}, "solution": t("In an inverse proportion, x × y stays the same.", "En una proporción inversa, x × y no cambia.")},
      "C": {"ok": "d", "hints": {"a": t("That would be direct. More workers take fewer days.", "Eso sería directa. Más obreros tardan menos días."), "b": t("You subtracted. Use k = 4 × 9 = 36.", "Restó. Use k = 4 × 9 = 36."), "c": t("Check: 36 ÷ 6.", "Revise: 36 ÷ 6.")}, "solution": t("k = 4 × 9 = 36; 36 ÷ 6 = 6 days.", "k = 4 × 9 = 36; 36 ÷ 6 = 6 días.")},
      "D": {"ok": "b", "hints": {"a": t("That would be direct. Faster takes less time.", "Eso sería directa. Más rápido tarda menos."), "c": t("Check: 60 × 5 = 300, and 300 ÷ 75.", "Revise: 60 × 5 = 300, y 300 ÷ 75."), "d": t("You subtracted 75 − 60. Use the distance: 60 × 5 = 300.", "Restó 75 − 60. Use la distancia: 60 × 5 = 300.")}, "solution": t("60 × 5 = 300 miles; 300 ÷ 75 = 4 hours.", "60 × 5 = 300 millas; 300 ÷ 75 = 4 horas.")},
      "E": {"ok": "c", "hints": {"a": t("That would be direct. More people use up the supplies faster.", "Eso sería directa. Más personas gastan las provisiones más rápido."), "b": t("You subtracted 3. Use k = 12 × 10.", "Restó 3. Use k = 12 × 10."), "d": t("Check: 120 ÷ 15.", "Revise: 120 ÷ 15.")}, "solution": t("k = 12 × 10 = 120; 120 ÷ 15 = 8 days.", "k = 12 × 10 = 120; 120 ÷ 15 = 8 días.")},
      "F": {"ok": "a", "hints": {"b": t("Gas and miles grow together: direct. Use the rate: 90 ÷ 3 = 30 miles per gallon.", "Gasolina y millas crecen juntas: directa. Use la tasa: 90 ÷ 3 = 30 millas por galón."), "c": t("Check: 240 ÷ 30.", "Revise: 240 ÷ 30."), "d": t("You used the inverse method. It is direct.", "Usó el método inverso. Es directa.")}, "solution": t("Direct: 3/90 = x/240, so x = 3 × 240 ÷ 90 = 8 gallons.", "Directa: 3/90 = x/240, así que x = 3 × 240 ÷ 90 = 8 galones.")},
      "G": {"ok": "b", "hints": {"a": t("That would be direct. More painters take less time.", "Eso sería directa. Más pintores tardan menos."), "c": t("Check: k = 4 × 6 = 24, and 24 ÷ 8.", "Revise: k = 4 × 6 = 24, y 24 ÷ 8."), "d": t("You subtracted. Use k = 4 × 6.", "Restó. Use k = 4 × 6.")}, "solution": t("k = 4 × 6 = 24; 24 ÷ 8 = 3 days.", "k = 4 × 6 = 24; 24 ÷ 8 = 3 días.")},
      "H": {"ok": "d", "hints": {"a": t("More hours, more parts: direct, not inverse.", "Más horas, más piezas: directa, no inversa."), "b": t("Check: 400 × 12 ÷ 8.", "Revise: 400 × 12 ÷ 8."), "c": t("You added 4. Use the ratio: 400 ÷ 8 = 50 parts per hour.", "Sumó 4. Use la razón: 400 ÷ 8 = 50 piezas por hora.")}, "solution": t("Direct: 400 ÷ 8 = 50 parts per hour; 50 × 12 = 600 parts.", "Directa: 400 ÷ 8 = 50 piezas por hora; 50 × 12 = 600 piezas.")}
     }}

    quiz = [
     ("A", t("Which situation is an inverse proportion?", "¿Cuál situación es una proporción inversa?"),
      [("a", t("Spending money from a $100 balance", "Gastar dinero de un saldo de $100")), ("b", t("Gallons of gas bought and money paid", "Galones de gasolina comprados y dinero pagado")), ("c", t("Number of workers and days to finish the same job", "Número de obreros y días para terminar la misma obra")), ("d", t("Hours worked and pay, at $15 an hour", "Horas trabajadas y sueldo, a $15 la hora"))]),
     ("B", t("In an inverse proportion, what stays the same?", "En una proporción inversa, ¿qué se mantiene constante?"),
      [("a", t("The product x × y", "El producto x × y")), ("b", t("The quotient y ÷ x", "El cociente y ÷ x")), ("c", t("The sum x + y", "La suma x + y")), ("d", t("The difference y − x", "La diferencia y − x"))]),
     ("C", t("4 workers take 9 days. How many days do 6 workers take?", "4 obreros tardan 9 días. ¿Cuántos días tardan 6 obreros?"), [("a", "13.5"), ("b", "7"), ("c", "5"), ("d", "6")]),
     ("D", t("A bus takes 5 hours at 60 mph. How long does it take at 75 mph?", "Un autobús tarda 5 horas a 60 mph. ¿Cuánto tarda a 75 mph?"), [("a", t("6.25 hours", "6.25 horas")), ("b", t("4 hours", "4 horas")), ("c", t("3 hours", "3 horas")), ("d", t("15 hours", "15 horas"))]),
     ("E", t("Supplies last 12 people for 10 days. How many days do they last 15 people?", "Las provisiones alcanzan para 12 personas durante 10 días. ¿Para cuántos días alcanzan a 15 personas?"), [("a", "12.5"), ("b", "7"), ("c", "8"), ("d", "9")]),
     ("F", t("A car uses 3 gallons every 90 miles. How many gallons does it need for 240 miles?", "Un auto gasta 3 galones cada 90 millas. ¿Cuántos galones necesita para 240 millas?"), [("a", "8"), ("b", "30"), ("c", "7"), ("d", "1.125")]),
     ("G", t("4 painters take 6 days to paint a building. How long do 8 painters take?", "4 pintores tardan 6 días en pintar un edificio. ¿Cuánto tardan 8 pintores?"), [("a", t("12 days", "12 días")), ("b", t("3 days", "3 días")), ("c", t("4 days", "4 días")), ("d", t("2 days", "2 días"))]),
     ("H", t("5 machines make 400 parts in 8 hours. How many parts do the same 5 machines make in 12 hours?", "5 máquinas producen 400 piezas en 8 horas. ¿Cuántas piezas producen las mismas 5 máquinas en 12 horas?"), [("a", "266.7"), ("b", "500"), ("c", "404"), ("d", "600")])]

    return B.pagina_leccion(n, 4, t(*TEMA), t(*TIT),
        t("When one quantity grows and the other shrinks: inverse proportions, the constant product, and deciding which method to use.", "Cuando una cantidad crece y la otra disminuye: la proporción inversa, el producto constante y cómo decidir qué método usar."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Tell</strong> direct from inverse proportion with the question “if X doubles, what happens to Y?”", "<strong>Distinguir</strong> la proporción directa de la inversa con la pregunta «si duplico X, ¿qué le pasa a Y?»."),
         t("<strong>Find</strong> the constant k = x × y of an inverse proportion.", "<strong>Calcular</strong> la constante k = x × y de una proporción inversa."),
         t("<strong>Solve</strong> inverse-proportion problems: workers and days, speed and time, supplies.", "<strong>Resolver</strong> problemas de proporción inversa: obreros y días, velocidad y tiempo, provisiones."),
         t("<strong>Choose</strong> the right method in mixed problems and check that the answer makes sense.", "<strong>Elegir</strong> el método correcto en problemas mixtos y comprobar que el resultado tiene sentido.")],
        secciones,
        (t("Classify eight situations from your daily life as direct or inverse, and justify each one with the question “if X doubles, what happens to Y?” Solve six inverse and mixed problems: workers and days, speed and time, supplies and people.",
           "Clasifique ocho situaciones de su vida diaria como directas o inversas y justifique cada una con la pregunta «si duplico X, ¿qué le pasa a Y?». Resuelva seis problemas de proporción inversa y mixta: obreros y días, velocidad y tiempo, provisiones y personas."),
         t("Choose one situation from your work or your home. Set it up, say whether it is direct or inverse, solve it, and explain out loud why the method you chose is the right one.",
           "Elija una situación de su trabajo o de su casa. Plantéela, diga si es directa o inversa, resuélvala y explique en voz alta por qué el método elegido es el correcto.")),
        quiz,
        t("Self-check checklist for inverse proportions", "Lista de autoevaluación de proporciones inversas"),
        t("Self-check checklist: skills for inverse proportions and mixed applications", "Lista de autoevaluación: destrezas de proporciones inversas y aplicaciones mixtas"),
        [(t("Tell direct from inverse", "Distinguir directa de inversa"), t("I classify any situation and justify it with the key question.", "Clasifico cualquier situación y la justifico con la pregunta diagnóstica."), t("I classify simple cases with help.", "Clasifico casos sencillos con ayuda."), t("I cannot tell the two kinds apart.", "No distingo los dos tipos.")),
         (t("Solve with k = x × y", "Resolver con k = x × y"), t("I find k and the missing value with no mistakes.", "Calculo k y el valor que falta sin errores."), t("I find k with help.", "Calculo k con ayuda."), t("I do not know what k is.", "No identifico la constante.")),
         (t("Use it in real life", "Aplicar en la vida real"), t("I choose the right method and explain why the other would give a silly answer.", "Elijo el método correcto y explico por qué el otro daría un resultado absurdo."), t("I choose the right type with help.", "Elijo el tipo correcto con ayuda."), t("I use the wrong kind of proportion.", "Aplico el tipo de proporción equivocado."))],
        t("<p>With this lesson you finish <strong>Topic 4</strong>. You now know the key difference between <strong>direct</strong> proportion (constant ratio) and <strong>inverse</strong> proportion (constant product), and the habit of asking the key question before you calculate.</p>\n<p><strong>Topic 5 · Percents</strong> opens with Lesson 5.1 · Percent: conversions and the three basic cases. There you will use direct proportions for a very common case: ratios out of 100.</p>",
          "<p>Con esta lección termina el <strong>Tema 4</strong>. Ya conoce la diferencia esencial entre la proporcionalidad <strong>directa</strong> (razón constante) y la <strong>inversa</strong> (producto constante), y tiene el hábito de hacer la pregunta diagnóstica antes de calcular.</p>\n<p>El <strong>Tema 5 · Porcentajes</strong> abre con la Lección 5.1 · El porcentaje: conversiones y los tres casos fundamentales. Allí aplicará las proporciones directas a un caso muy común: las razones expresadas por cada 100.</p>"),
        ("5-1", ("", t("Lesson 5.1 · Percent: conversions and the three basic cases", "Lección 5.1 · El porcentaje: conversiones y los tres casos fundamentales"))),
        [(t("inverse proportion", "proporción inversa"), t("When one quantity doubles, the other is cut in half; the product x × y stays the same.", "Cuando una cantidad se duplica, la otra se reduce a la mitad; el producto x × y no cambia.")),
         (t("constant k", "constante k"), t("In an inverse proportion, the fixed product x × y (the “total work”).", "En una proporción inversa, el producto fijo x × y (el «trabajo total»).")),
         (t("inverse rule of three", "regla de tres inversa"), t("Multiply straight across and divide by the remaining value.", "Se multiplica en línea recta y se divide entre el dato restante.")),
         (t("worker-days", "días-obrero"), t("A unit of total work: workers × days.", "Unidad de trabajo total: obreros × días."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "casas": "Cement: <strong>{s} bags</strong>", "cteCasas": "What stays the same is the quotient: {s} ÷ {c} = <strong>20 bags per house</strong>.",
  "dias": "Days of work: <strong>{d}</strong>", "cteObreros": "What stays the same is the product: {o} × {d} = <strong>60 worker-days</strong>.",
  "vozCasas": "{c} houses", "vozObreros": "{o} workers",
  "sit": [["Pounds of apples and the money you pay for them.", "d", "More pounds, more money: direct."],
          ["Number of workers and days to finish a job.", "i", "More workers, fewer days: inverse."],
          ["The speed of a car and the time to travel the same distance.", "i", "More speed, less time: inverse."],
          ["Gallons of gas and the miles you can drive.", "d", "More gas, more miles: direct."],
          ["Hours worked and pay earned (paid by the hour).", "d", "More hours, more pay: direct."],
          ["Number of faucets open and the time to fill a tank.", "i", "More faucets, less time: inverse."],
          ["Guests at a party and the size of the piece of one cake each one gets.", "i", "More guests, smaller pieces: inverse."],
          ["Cups of flour and the number of cookies in a recipe.", "d", "More cookies, more flour: direct."],
          ["Number of people who share a fixed rent and what each one pays.", "i", "More people, each pays less: inverse."],
          ["Inches on a map and real miles.", "d", "More inches on the map, more miles: direct."]],
  "queTipo": " What kind of proportion is it?", "dir": "Direct: both grow together", "inv": "Inverse: one grows and the other shrinks",
  "pistaTipo": "Ask yourself: if one quantity doubles, does the other double or get cut in half?",
  "i1": "{a} workers take {b} days to finish a job. How many days would {c} workers take at the same pace?", "i1s": "{a} × {b} = {k}; {k} ÷ {c} = {r} days.",
  "i2": "A bus covers a route at {a} mph in {b} hours. How many hours would it take at {c} mph?", "i2s": "{a} × {b} = {k} miles; {k} ÷ {c} = {r} hours.",
  "i3": "With {a} faucets open, a tank fills in {b} minutes. How many minutes does it take with {c} {f}?", "i3s": "{a} × {b} = {k}; {k} ÷ {c} = {r} minutes.", "llave": ["faucet", "faucets"],
  "i4": "If {a} people share the rent, each one pays {b}. How much would each one pay if there were {c} people, in dollars?", "i4s": "{a} × {b} = {k}; {k} ÷ {c} = {r}.",
  "esInv": "It is inverse: the product stays the same. ", "comoDir": "That is what you would get if it were direct. Here, as one quantity grows, the other shrinks: the product stays the same.",
  "m": [
   ["{a} pounds of meat cost {b}. How much do {c} pounds cost?", "d", "$"],
   ["{a} workers paint a house in {b} days. How many days do {c} workers take?", "i", " days"],
   ["A car uses {a} gallons every {b} miles. How many gallons does it need for {c} miles?", "d", " gallons"],
   ["At {a} mph a trip takes {b} hours. How many hours does it take at {c} mph?", "i", " hours"],
   ["A recipe for {a} servings uses {b} cups of rice. How many cups are needed for {c} servings?", "d", " cups"],
   ["The food in a shelter lasts {a} people for {b} days. How many days does it last {c} people?", "i", " days"]],
  "solD": "Direct: {b} ÷ {a} = {u} per unit; {u} × {c} = {r}.", "solI": "Inverse: k = {a} × {b} = {k}; {k} ÷ {c} = {r}.",
  "pDir": "You used the inverse method, but this one is direct: both quantities grow together.", "pInv": "You used cross products, but this one is inverse: one quantity grows and the other shrinks.",
  "pSuma": "Proportions are not solved by adding or subtracting the difference.", "pistaMix": "First decide: is it direct or inverse?"
 },
 "es": {
  "casas": "Cemento: <strong>{s} sacos</strong>", "cteCasas": "Lo constante es el cociente: {s} ÷ {c} = <strong>20 sacos por casa</strong>.",
  "dias": "Días de obra: <strong>{d}</strong>", "cteObreros": "Lo constante es el producto: {o} × {d} = <strong>60 días-obrero</strong>.",
  "vozCasas": "{c} casas", "vozObreros": "{o} obreros",
  "sit": [["Libras de manzanas y lo que se paga por ellas.", "d", "Más libras, más dinero: directa."],
          ["Número de obreros y días para terminar una obra.", "i", "Más obreros, menos días: inversa."],
          ["Velocidad de un auto y tiempo para recorrer la misma distancia.", "i", "Más velocidad, menos tiempo: inversa."],
          ["Galones de gasolina y millas que se pueden recorrer.", "d", "Más gasolina, más millas: directa."],
          ["Horas trabajadas y sueldo ganado (pago por hora).", "d", "Más horas, más sueldo: directa."],
          ["Número de llaves abiertas y tiempo para llenar un tanque.", "i", "Más llaves, menos tiempo: inversa."],
          ["Invitados a una fiesta y el tamaño del pedazo de un pastel que le toca a cada uno.", "i", "Más invitados, pedazos más pequeños: inversa."],
          ["Tazas de harina y número de galletas de una receta.", "d", "Más galletas, más harina: directa."],
          ["Número de personas que comparten una renta fija y lo que paga cada una.", "i", "Más personas, menos paga cada una: inversa."],
          ["Pulgadas en un mapa y millas reales.", "d", "Más pulgadas en el mapa, más millas: directa."]],
  "queTipo": " ¿Qué tipo de proporción es?", "dir": "Directa: las dos crecen juntas", "inv": "Inversa: una crece y la otra disminuye",
  "pistaTipo": "Pregúntese: si una cantidad se duplica, ¿la otra se duplica o se reduce a la mitad?",
  "i1": "{a} obreros tardan {b} días en terminar una obra. ¿Cuántos días tardarían {c} obreros al mismo ritmo?", "i1s": "{a} × {b} = {k}; {k} ÷ {c} = {r} días.",
  "i2": "Un autobús cubre una ruta a {a} mph en {b} horas. ¿Cuántas horas tardaría a {c} mph?", "i2s": "{a} × {b} = {k} millas; {k} ÷ {c} = {r} horas.",
  "i3": "Con {a} llaves abiertas, un tanque se llena en {b} minutos. ¿Cuántos minutos tarda con {c} {f}?", "i3s": "{a} × {b} = {k}; {k} ÷ {c} = {r} minutos.", "llave": ["llave", "llaves"],
  "i4": "Si {a} personas comparten la renta, cada una paga {b}. ¿Cuánto pagaría cada una si fueran {c} personas, en dólares?", "i4s": "{a} × {b} = {k}; {k} ÷ {c} = {r}.",
  "esInv": "Es inversa: el producto se mantiene. ", "comoDir": "Así sería si fuera directa. Aquí, si una cantidad crece, la otra disminuye: se mantiene el producto.",
  "m": [
   ["{a} libras de carne cuestan {b}. ¿Cuánto cuestan {c} libras?", "d", "$"],
   ["{a} obreros pintan una casa en {b} días. ¿Cuántos días tardan {c} obreros?", "i", " días"],
   ["Un auto gasta {a} galones cada {b} millas. ¿Cuántos galones necesita para {c} millas?", "d", " galones"],
   ["A {a} mph un viaje toma {b} horas. ¿Cuántas horas toma a {c} mph?", "i", " horas"],
   ["Una receta para {a} porciones lleva {b} tazas de arroz. ¿Cuántas tazas se necesitan para {c} porciones?", "d", " tazas"],
   ["La comida de un albergue alcanza para {a} personas durante {b} días. ¿Para cuántos días alcanza a {c} personas?", "i", " días"]],
  "solD": "Directa: {b} ÷ {a} = {u} por unidad; {u} × {c} = {r}.", "solI": "Inversa: k = {a} × {b} = {k}; {k} ÷ {c} = {r}.",
  "pDir": "Usó el método inverso, pero esta es directa: las dos cantidades crecen juntas.", "pInv": "Usó el producto cruzado, pero esta es inversa: una cantidad crece y la otra disminuye.",
  "pSuma": "Las proporciones no se resuelven sumando o restando la diferencia.", "pistaMix": "Primero decida: ¿es directa o inversa?"
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }

/* ============ MODULE 1 · direct or inverse ============ */
function pintaDI(){
  var c = +$("di-c").value, o = +$("di-o").value, sacos = 20 * c, dias = Math.round(60 / o * 100) / 100;
  $("di-cv").textContent = c; $("di-ov").textContent = o;
  $("di-sd").innerHTML = '<div class="linea"><span aria-hidden="true">' + '🏠'.repeat(c) + '</span><span class="sr-only">' + F(TXT.vozCasas, { c: c }) + '</span></div><div class="linea">' + F(TXT.casas, { s: sacos }) + '</div><div class="barra-v" style="width:' + (sacos / 2) + '%" aria-hidden="true"></div>' +
    '<div class="linea">' + F(TXT.cteCasas, { s: sacos, c: c }) + '</div>';
  $("di-si").innerHTML = '<div class="linea"><span aria-hidden="true">' + '👷'.repeat(o) + '</span><span class="sr-only">' + F(TXT.vozObreros, { o: o }) + '</span></div><div class="linea">' + F(TXT.dias, { d: nd(dias) }) + '</div><div class="barra-v" style="width:' + (dias / 60 * 100) + '%" aria-hidden="true"></div>' +
    '<div class="linea">' + F(TXT.cteObreros, { o: o, d: nd(dias) }) + '</div>';
}
function genTipo(){
  var s = elige(TXT.sit);
  return { enun: s[0] + TXT.queTipo, opciones: [{ html: TXT.dir, clave: "d" }, { html: TXT.inv, clave: "i" }], correcta: s[1], enOrden: true, pista: TXT.pistaTipo, bien: s[2], mal: s[2] };
}

/* ============ MODULE 2 · inverse proportions ============ */
function genInversa(){
  for (var z = 0; z < 100; z++){
    var tp = aleatorio(1, 4), a, b, c, k, res, enun, sol, din = false, ds, x;
    if (tp === 1){ a = aleatorio(2, 8); b = aleatorio(3, 12); k = a * b; ds = []; for (x = 2; x <= 24; x++) if (k % x === 0 && x !== a) ds.push(x); if (!ds.length) continue; c = elige(ds); res = k / c;
      enun = F(TXT.i1, { a: a, b: b, c: c }); sol = F(TXT.i1s, { a: a, b: b, c: c, k: k, r: nd(res) }); }
    else if (tp === 2){ a = 5 * aleatorio(8, 14); b = aleatorio(2, 6); k = a * b; var vs = [45, 50, 55, 60, 65, 70, 75, 80].filter(function(v){ return v !== a && (k / v) * 4 === Math.round((k / v) * 4); }); if (!vs.length) continue; c = elige(vs); res = k / c;
      enun = F(TXT.i2, { a: a, b: b, c: c }); sol = F(TXT.i2s, { a: a, b: b, c: c, k: k, r: nd(res) }); }
    else if (tp === 3){ a = aleatorio(2, 4); b = aleatorio(6, 12) * 2; k = a * b; var ls = [1, 2, 3, 4, 6, 8].filter(function(v){ return v !== a && k % v === 0; }); c = elige(ls); res = k / c;
      enun = F(TXT.i3, { a: a, b: b, c: c, f: c === 1 ? TXT.llave[0] : TXT.llave[1] }); sol = F(TXT.i3s, { a: a, b: b, c: c, k: k, r: nd(res) }); }
    else { a = aleatorio(3, 6); b = a * 60 * aleatorio(1, 3); k = a * b; var ps = [2, 3, 4, 5, 6, 8, 10, 12].filter(function(v){ return v !== a && k % v === 0; }); c = elige(ps); res = k / c; din = true;
      enun = F(TXT.i4, { a: a, b: dinero(b), c: c }); sol = F(TXT.i4s, { a: a, b: dinero(b), c: c, k: dinero(k), r: dinero(res) }); }
    var directa = b * c / a;
    return { enun: enun, correcta: din ? dinero(res) : nd(res), solucion: TXT.esInv + sol, evalua: numD(res, Math.abs(directa - res) > 0.01 ? [{ v: directa, msg: TXT.comoDir }] : []) };
  }
}

/* ============ MODULE 3 · mixed applications ============ */
function genMixta(){
  for (var z = 0; z < 200; z++){
    var i = aleatorio(0, 5), m = TXT.m[i], tipo = m[1], a, b, c, res, din = i === 0;
    if (i === 0){ a = aleatorio(2, 5); var pu = elige([2.5, 3.5, 4.5, 5.25, 6]); b = a * pu; c = aleatorio(2, 9); }
    else if (i === 1 || i === 5){ a = aleatorio(2, 12); b = aleatorio(3, 15); c = aleatorio(2, 16); }
    else if (i === 2){ a = aleatorio(2, 5); b = a * elige([25, 30, 35]); c = b / a * aleatorio(2, 12); }
    else if (i === 3){ a = 5 * aleatorio(6, 14); b = aleatorio(2, 8); c = 5 * aleatorio(6, 16); }
    else { a = aleatorio(2, 6); b = aleatorio(1, 4); c = aleatorio(2, 12); }
    if (c === a) continue;
    var d = b * c / a, inv = a * b / c;
    res = tipo === "d" ? d : inv;
    var otro = tipo === "d" ? inv : d, suma = b + (c - a);
    if (Math.abs(res * 100 - Math.round(res * 100)) > 1e-6 || Math.abs(otro * 100 - Math.round(otro * 100)) > 1e-6 || res <= 0) continue;
    var f = function(v){ return din ? dinero(v) : nd(v) + m[2]; };
    var bt = din ? dinero(b) : nd(b), ops = [{ html: f(res), clave: "ok" }], pc = {};
    ops.push({ html: f(otro), clave: "otro" }); pc.otro = tipo === "d" ? TXT.pDir : TXT.pInv;
    if (suma > 0 && Math.abs(suma - res) > 0.01 && Math.abs(suma - otro) > 0.01){ ops.push({ html: f(suma), clave: "suma" }); pc.suma = TXT.pSuma; }
    if (Math.abs(res - otro) < 0.01) continue;
    var u = Math.round(b / a * 1000) / 1000, kk = a * b;
    var sol = tipo === "d" ? F(TXT.solD, { a: a, b: bt, c: c, u: din ? dinero(u) : nd(u), r: f(res) }) : F(TXT.solI, { a: a, b: nd(b), c: c, k: nd(kk), r: f(res) });
    return { enun: F(m[0], { a: a, b: bt, c: c }), opciones: ops, correcta: "ok", pistas: pc, pista: TXT.pistaMix, bien: sol, mal: sol };
  }
}

/* ============ Start ============ */
["di-c", "di-o"].forEach(function(id){ $(id).addEventListener("input", pintaDI); }); pintaDI();
creaPracticaOM("p1", genTipo);
creaPracticaLibre("p2", genInversa);
creaPracticaOM("p3", genMixta);
'''

def libre_d(pid, titulo, etiqueta):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."),
        t("Type only the number. It may have decimals, like 1.25; for money you may use the $ sign.", "Escriba solo el número. Puede llevar decimales, como 1.25; si es dinero, puede usar el signo $."))

def practica_pagina():
    n = N
    mods = [
     (t("direct-or-inverse", "directa-inversa"), t("Direct or inverse", "Directa frente a inversa"),
      f'''      <p>{t("Let's build houses. Move the sliders and watch what grows and what shrinks.", "Vamos a construir casas. Mueva los controles y observe qué crece y qué disminuye.")}</p>
      <div class="tableros">
        <div class="tablero">
          <h4>{t("Houses and cement: they go up together ↑↑", "Casas y cemento: suben juntos ↑↑")}</h4>
          <div class="campo"><label for="di-c">{t("Number of houses", "Número de casas")}: <span id="di-cv"></span></label><input type="range" id="di-c" min="1" max="10" value="2"></div>
          <div class="salida" id="di-sd" aria-live="polite"></div>
        </div>
        <div class="tablero">
          <h4>{t("Workers and days: one goes up, the other goes down ↑↓", "Obreros y días: uno sube, el otro baja ↑↓")}</h4>
          <div class="campo"><label for="di-o">{t("Number of workers", "Número de obreros")}: <span id="di-ov"></span></label><input type="range" id="di-o" min="1" max="12" value="2"></div>
          <div class="salida" id="di-si" aria-live="polite"></div>
        </div>
      </div>
      <table class="reglas">
        <caption>{t("The two kinds of proportion", "Las dos clases de proporcionalidad")}</caption>
        <thead><tr><th scope="col"></th><th scope="col">{t("Direct", "Directa")}</th><th scope="col">{t("Inverse", "Inversa")}</th></tr></thead>
        <tbody>
          <tr><td>{t("If one quantity grows…", "Si una cantidad crece…")}</td><td>{t("the other grows", "la otra crece")}</td><td>{t("the other shrinks", "la otra disminuye")}</td></tr>
          <tr><td>{t("If one doubles…", "Si una se duplica…")}</td><td>{t("the other doubles", "la otra se duplica")}</td><td>{t("the other is cut in half", "la otra se reduce a la mitad")}</td></tr>
          <tr><td>{t("What stays the same", "Lo que no cambia")}</td><td>{t("the quotient (the ratio)", "el cociente (la razón)")}</td><td>{t("the product", "el producto")}</td></tr>
        </tbody>
      </table>
      <div class="caja-tip"><strong>{t("The test question:", "La pregunta de prueba:")}</strong> {t("“If one quantity grows, what does the other do?” If it grows too, it is direct; if it shrinks, it is inverse.", "«si una cantidad crece, ¿qué hace la otra?». Si crece con ella, es directa; si disminuye, es inversa.")}</div>
{B.om("p1", t("Practice: direct or inverse?", "Practique: ¿directa o inversa?"))}'''),
     (t("inverse", "inversas"), t("Solving inverse proportions", "Resolver proporciones inversas"),
      f'''      <p>{t("In an inverse proportion, what stays the same is the <strong>product</strong>. Multiply the known values, then divide by the new quantity.", "En una proporción inversa lo que se mantiene es el <strong>producto</strong>. Se calcula el producto con los datos conocidos y se divide entre la cantidad nueva.")}</p>
      <div class="formula">{t("4 workers × 9 days = 36 &nbsp;→&nbsp; 6 workers × x days = 36 &nbsp;→&nbsp; x = 6", "4 obreros × 9 días = 36 &nbsp;→&nbsp; 6 obreros × x días = 36 &nbsp;→&nbsp; x = 6")}</div>
{libre_d("p2", t("Practice: inverse proportions", "Practique: proporciones inversas"), t("Answer", "Resultado"))}'''),
     (t("mixed", "mixtas"), t("Mixed applications", "Aplicaciones mixtas"),
      f'''      <p>{t("Problems do not say what kind they are. First ask the key question, then choose the method: constant ratio (direct) or constant product (inverse). Last, check that the answer makes sense.", "Los problemas no dicen de qué tipo son. Primero hágase la pregunta diagnóstica y después elija el método: razón constante (directa) o producto constante (inversa). Al final, compruebe que el resultado tiene sentido.")}</p>
{B.om("p3", t("Practice: decide and solve", "Practique: decida y resuelva"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 4, t(*TEMA), t(*TIT),
        t("Three practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Tres actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Proporciones inversas y aplicaciones mixtas")
