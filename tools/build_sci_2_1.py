"""LearnGED · Ciencias · Lección 2.1 · Notación científica, unidades y la calculadora TI-30XS (EN/ES).
Fuente: clases_ciencias/leccion_2-1.html y los interactivos ciencias/clinica_ti30xs y ciencias/escala_universo.
La práctica usa el motor de notación científica de Matemáticas (/math/scinot.js).
Uso: python3 tools/build_sci_2_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "2-1"
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def titulo():
    return t("Scientific notation, units, and the TI-30XS calculator", "Notación científica, unidades y la calculadora TI-30XS")


def anc(en, es):
    return en if C.L == "en" else es


def s(c, e):
    """c × 10^e, legible también para lectores de pantalla."""
    voz = t(f"{c} times 10 to the power of {e}".replace("-", "negative "), f"{c} por 10 elevado a {e}".replace("-", "menos "))
    return f'<span class="num-sci" aria-hidden="true">{c} × 10{str(e).translate(SUP)}</span><span class="sr-only">{voz}</span>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Scientific notation writes any number as the product of two pieces: a <strong>coefficient</strong> and a <strong>power of ten</strong>. One rule defines it, with no exceptions:", "La notación científica escribe cualquier cantidad como el producto de dos piezas: un <strong>coeficiente</strong> y una <strong>potencia de diez</strong>. La define una sola regla, sin excepciones:")}</p>
<div class="anatomia" role="img" aria-label="{t("3.6 times 10 to the 8th. The coefficient, 3.6, is at least 1 and less than 10. The exponent, 8, tells the scale of the number.", "3.6 por 10 elevado a 8. El coeficiente, 3.6, es mayor o igual que 1 y menor que 10. El exponente, 8, indica la escala del número.")}">
<span class="parte"><span class="coef">3.6</span><small>{t("coefficient: 1 ≤ a &lt; 10", "coeficiente: 1 ≤ a &lt; 10")}</small></span>
<span class="parte"><span>× 10<sup class="expo">8</sup></span><small>{t("power of ten: the exponent is the scale", "potencia de diez: el exponente es la escala")}</small></span>
</div>
{C.caja("ojo", t("The coefficient rule", "La regla del coeficiente"), "<p>" + t("The coefficient must be <strong>at least 1 and less than 10</strong>: exactly one nonzero digit in front of the decimal point. If the coefficient is 12.5 or 0.6, the number is not in scientific notation yet, even if its value is right.", "El coeficiente debe ser <strong>mayor o igual que 1 y menor que 10</strong>: exactamente una cifra distinta de cero delante del punto decimal. Si el coeficiente es 12.5 o 0.6, el número todavía no está en notación científica, aunque el valor sea correcto.") + "</p>")}
<p>{t(f"The exponent is not decoration: it is the scale of the number. Two numbers with the same coefficient and different exponents are nothing alike. Between {s('3.6', 8)} and {s('3.6', 11)} there is a factor of one thousand.", f"El exponente no es un adorno: es la escala del número. Dos cantidades con el mismo coeficiente y exponentes distintos no se parecen en nada. Entre {s('3.6', 8)} y {s('3.6', 11)} hay un factor de mil.")}</p>
{C.caja("tip", t("A bridge to Math", "Un puente con Matemáticas"), "<p>" + t('Math Level 3, Topic 2 teaches scientific notation step by step. If this section feels fast, open <a href="/math/level-3/lesson-2-1.html">Math Lesson 3 · 2.1</a> and come back.', 'El Tema 2 del Nivel 3 de Matemáticas enseña la notación científica paso a paso. Si esta sección le parece rápida, abra la <a href="/es/matematicas/nivel-3/leccion-2-1.html">Lección 2.1 del Nivel 3 de Matemáticas</a> y vuelva.') + "</p>")}"""

    s2 = f"""<p>{t("Converting is all about moving the decimal point and counting how many places it moved. The sign of the exponent tells you which way.", "Toda la conversión se reduce a mover el punto decimal y llevar la cuenta de cuántos lugares se movió. El signo del exponente indica en qué dirección.")}</p>
{C.tabla(t("How to convert between decimal and scientific notation, depending on the size of the number", "Reglas de conversión entre notación decimal y científica según el tamaño del número"),
 [t("Situation", "Situación"), t("What to do", "Qué se hace"), t("Example", "Ejemplo")],
 [[t("Large number to scientific notation", "Número grande a notación científica"), t("Move the point to the left until one digit is left in front. The exponent is positive and equals the number of places moved.", "Se mueve el punto hacia la izquierda hasta dejar una sola cifra delante. El exponente es positivo e igual al número de lugares."), f"149,600,000 = {s('1.496', 8)}"],
  [t("Small number to scientific notation", "Número pequeño a notación científica"), t("Move the point to the right until it passes the first nonzero digit. The exponent is negative.", "Se mueve el punto hacia la derecha hasta pasar la primera cifra distinta de cero. El exponente es negativo."), f"0.00047 = {s('4.7', -4)}"],
  [t("Positive exponent to decimal", "Exponente positivo a decimal"), t("Move the point to the right as many places as the exponent says, filling with zeros.", "Se mueve el punto hacia la derecha tantos lugares como indique el exponente, completando con ceros."), f"{s('2.5', 6)} = 2,500,000"],
  [t("Negative exponent to decimal", "Exponente negativo a decimal"), t("Move the point to the left as many places as the exponent says, filling with zeros.", "Se mueve el punto hacia la izquierda tantos lugares como indique el exponente, completando con ceros."), f"{s('5.2', -6)} = 0.0000052"]])}
{C.ejemplo(t("Example 1 · From decimal to scientific", "Ejemplo 1 · De decimal a científica"),
 [("", t("The average distance from Earth to the Sun is 149,600,000 km (about 93 million miles).", "La distancia media entre la Tierra y el Sol es de 149,600,000 km.")),
  ("1", t("Find where the decimal point is now: at the end, 149,600,000.", "Se localiza la posición actual del punto decimal: al final, 149,600,000.")),
  ("2", t("Move it to the left until one digit is left in front: 1.496.", "Se mueve hacia la izquierda hasta que quede una sola cifra delante: 1.496.")),
  ("3", t("Count the places: eight. The number was large, so the exponent is positive.", "Se cuentan los lugares: ocho. Como el número era grande, el exponente es positivo."))],
 t(f"<strong>Result:</strong> {s('1.496', 8)} km.", f"<strong>Resultado:</strong> {s('1.496', 8)} km."))}
{C.ejemplo(t("Example 2 · From scientific to decimal", "Ejemplo 2 · De científica a decimal"),
 [("", t(f"The charge of an electron is {s('1.6', -19)} coulombs.", f"La carga de un electrón es de {s('1.6', -19)} culombios.")),
  ("1", t("The exponent is negative, so the number is less than 1 and the point moves to the left.", "El exponente es negativo, así que el número es menor que 1 y el punto se mueve hacia la izquierda.")),
  ("2", t("Move it nineteen places, filling with zeros: 0.00000000000000000016.", "Se recorren diecinueve lugares, completando con ceros: 0.00000000000000000016."))],
 t("<strong>Note:</strong> this is exactly why scientific notation exists. Nobody counts eighteen zeros without a mistake, and the test does not ask you to: it asks you to understand the exponent.", "<strong>Observación:</strong> por esto existe la notación científica. Nadie cuenta dieciocho ceros sin equivocarse, y el examen no pide contarlos: pide interpretar el exponente."))}
{C.caja("ojo", t("The direction mistake", "El error de dirección"), "<p>" + t("Moving the point the wrong way flips the sign of the exponent and turns a tiny number into a giant one. A quick check always catches it: if the original number is less than 1, the exponent must be negative; if it is greater than 10, it must be positive. Check this before you write the answer.", "Confundir el sentido del movimiento invierte el signo del exponente y convierte un número diminuto en uno gigantesco. Un control rápido lo evita siempre: si el número original es menor que 1, el exponente tiene que ser negativo; si es mayor que 10, tiene que ser positivo. Compruébelo antes de escribir el resultado.") + "</p>")}
{P(t("Try it 1 · Small number", "Pruebe 1 · Número pequeño"), t("The number 0.00082 in scientific notation is…", "El número 0.00082 en notación científica es…"),
   [s("8.2", -3), s("8.2", -4), s("8.2", 4)], 1,
   {0: t("Count again: the point moves past 0, 0, 0, and 8. That is four places.", "Cuente otra vez: el punto pasa por 0, 0, 0 y 8. Son cuatro lugares."),
    2: t("The number is less than 1, so the exponent must be negative.", "El número es menor que 1, así que el exponente tiene que ser negativo.")},
   t(f"The point moves 4 places to the right: {s('8.2', -4)}. The number is small, so the exponent is negative.", f"El punto se mueve 4 lugares a la derecha: {s('8.2', -4)}. El número es pequeño, así que el exponente es negativo."))}
{P(t("Try it 2 · Back to decimal", "Pruebe 2 · De vuelta a decimal"), t(f"The number {s('4.5', 5)} as a decimal is…", f"El número {s('4.5', 5)} en notación decimal es…"),
   ["45,000", "0.000045", "450,000"], 2,
   {0: t("45,000 is 4.5 × 10⁴. Count five places to the right from 4.5.", "45,000 es 4.5 × 10⁴. Cuente cinco lugares a la derecha a partir de 4.5."),
    1: t("A positive exponent makes a large number. The point moves to the right.", "Un exponente positivo da un número grande. El punto se mueve hacia la derecha.")},
   t("Five places to the right from 4.5: 450,000.", "Cinco lugares a la derecha a partir de 4.5: 450,000."))}
{P(t("Try it 3 · Is it scientific notation?", "Pruebe 3 · ¿Está en notación científica?"), t(f"{s('0.6', 7)} is not in scientific notation because…", f"La expresión {s('0.6', 7)} no está en notación científica porque…"),
   [t("The coefficient is less than 1", "El coeficiente es menor que 1"), t("The exponent is too large", "El exponente es demasiado grande"), t("The base should be 2, not 10", "La base debería ser 2 en lugar de 10")], 0,
   {1: t("Any whole exponent is allowed. Look at the coefficient.", "Cualquier exponente entero es válido. Mire el coeficiente."),
    2: t("The base is always 10. Look at the coefficient.", "La base es siempre 10. Mire el coeficiente.")},
   t(f"0.6 is less than 1. Written correctly, it is {s('6', 6)}.", f"0.6 es menor que 1. Escrito correctamente es {s('6', 6)}."))}
{C.enlace(N, anc("write-sci", "escribir"), t("write real sizes in scientific notation", "escriba tamaños reales en notación científica"), t("From a proton to the Milky Way: write each size in scientific notation, and back.", "Del protón a la Vía Láctea: escriba cada tamaño en notación científica, y al revés."))}"""

    s3 = f"""<p>{t("Multiplying and dividing in scientific notation is easier than with the full numbers, because the two pieces are handled separately. Coefficients are multiplied or divided; exponents are added or subtracted.", "Operar en notación científica es más sencillo que operar con los números completos, porque las dos piezas se tratan por separado. Los coeficientes se multiplican o se dividen; los exponentes se suman o se restan.")}</p>
{C.tabla(t("How to multiply and divide in scientific notation", "Cómo multiplicar y dividir en notación científica"),
 [t("Operation", "Operación"), t("Coefficients", "Coeficientes"), t("Exponents", "Exponentes"), t("Example", "Ejemplo")],
 [[t("Multiply", "Multiplicar"), t("multiply them", "se multiplican"), t("add them", "se suman"), f"({s('4', 3)}) · ({s('2', 6)}) = {s('8', 9)}"],
  [t("Divide", "Dividir"), t("divide them", "se dividen"), t("subtract them", "se restan"), f"({s('9', 8)}) ÷ ({s('3', 2)}) = {s('3', 6)}"]])}
{C.ejemplo(t("Example 3 · When the coefficient goes out of range", "Ejemplo 3 · Cuando el coeficiente se sale del intervalo"),
 [("", t(f"Multiply ({s('5', 4)}) · ({s('4', 3)}).", f"Multiplicar ({s('5', 4)}) · ({s('4', 3)}).")),
  ("1", t(f"Coefficients: 5 × 4 = 20. Exponents: 4 + 3 = 7. The first result is {s('20', 7)}.", f"Coeficientes: 5 × 4 = 20. Exponentes: 4 + 3 = 7. El resultado provisional es {s('20', 7)}.")),
  ("2", t("The value is right, but 20 breaks the coefficient rule: it is not between 1 and 10.", "El valor es correcto, pero 20 no cumple la regla del coeficiente: no está entre 1 y 10.")),
  ("3", t(f"Rewrite 20 as {s('2', 1)} and add that power to the one you had: 1 + 7 = 8.", f"Se reescribe 20 como {s('2', 1)} y esa potencia se suma a la que ya había: 1 + 7 = 8."))],
 t(f"<strong>Result:</strong> {s('2', 8)}. This adjusting step costs the most points on the test, because the first result looks finished.", f"<strong>Resultado:</strong> {s('2', 8)}. Este paso de ajuste es el que más puntos cuesta en el examen, porque el resultado intermedio parece terminado."))}
{C.caja("tip", t("A ratio becomes a simple number", "El cociente que se vuelve un número sencillo"), "<p>" + t(f"To compare the sizes of two objects, divide. A red blood cell of {s('8', -6)} m against a bacterium of {s('2', -6)} m: the coefficients give 8 ÷ 2 = 4, and the exponents cancel, −6 − (−6) = 0. The blood cell is <strong>4 times</strong> larger. Without scientific notation, the same comparison means counting zeros.", f"Para comparar el tamaño de dos objetos, se divide. Un glóbulo rojo de {s('8', -6)} m frente a una bacteria de {s('2', -6)} m: los coeficientes dan 8 ÷ 2 = 4 y los exponentes se cancelan, −6 − (−6) = 0. El glóbulo es <strong>4 veces</strong> mayor. Sin notación científica, esa misma comparación exige contar ceros.") + "</p>")}
{P(t("Try it 4 · Multiply", "Pruebe 4 · Multiplicar"), t(f"({s('4', 3)}) · ({s('2', 6)}) equals…", f"El producto ({s('4', 3)}) · ({s('2', 6)}) es igual a…"),
   [s("6", 9), s("8", 9), s("8", 18)], 1,
   {0: t("The coefficients are multiplied, not added: 4 × 2.", "Los coeficientes se multiplican, no se suman: 4 × 2."),
    2: t("When you multiply, the exponents are added, not multiplied: 3 + 6.", "Al multiplicar, los exponentes se suman, no se multiplican: 3 + 6.")},
   t(f"4 × 2 = 8 and 3 + 6 = 9: {s('8', 9)}.", f"4 × 2 = 8 y 3 + 6 = 9: {s('8', 9)}."))}
{P(t("Try it 5 · Divide", "Pruebe 5 · Dividir"), t(f"({s('9', 8)}) ÷ ({s('3', 2)}) equals…", f"El cociente ({s('9', 8)}) ÷ ({s('3', 2)}) es igual a…"),
   [s("3", 6), s("3", 10), s("6", 6)], 0,
   {1: t("When you divide, the exponents are subtracted: 8 − 2.", "Al dividir, los exponentes se restan: 8 − 2."),
    2: t("The coefficients are divided, not subtracted: 9 ÷ 3.", "Los coeficientes se dividen, no se restan: 9 ÷ 3.")},
   t(f"9 ÷ 3 = 3 and 8 − 2 = 6: {s('3', 6)}.", f"9 ÷ 3 = 3 y 8 − 2 = 6: {s('3', 6)}."))}
{P(t("Try it 6 · Adjust the coefficient", "Pruebe 6 · Ajustar el coeficiente"), t(f"Multiplying ({s('6', 5)}) · ({s('5', 2)}) gives {s('30', 7)}. The final answer is…", f"Al multiplicar ({s('6', 5)}) · ({s('5', 2)}) se obtiene {s('30', 7)}. El resultado definitivo es…"),
   [t(f"{s('30', 7)}, already written correctly", f"{s('30', 7)}, que ya está bien escrito"), s("3", 7), s("3", 8)], 2,
   {0: t("30 is not between 1 and 10. It has to be adjusted.", "30 no está entre 1 y 10. Hay que ajustarlo."),
    1: t(f"30 = {s('3', 1)}, so the exponent must go up by 1.", f"30 = {s('3', 1)}, así que el exponente tiene que subir 1.")},
   t(f"30 = {s('3', 1)}, so 1 + 7 = 8: {s('3', 8)}.", f"30 = {s('3', 1)}, así que 1 + 7 = 8: {s('3', 8)}."))}
{C.enlace(N, anc("multiply", "operar"), t("multiply and divide", "multiplique y divida"), t("New exercises every time, including the ones where you must adjust the coefficient.", "Ejercicios nuevos cada vez, incluidos los que obligan a ajustar el coeficiente."))}"""

    escala = [("1.7", -15, t("proton", "protón")), ("1.0", -10, t("atom", "átomo")), ("1.0", -7, t("flu virus", "virus de la gripe")),
              ("1.7", 0, t("person", "persona")), ("1.3", 7, t("Earth", "la Tierra")), ("1.5", 11, t("Earth to Sun", "Tierra–Sol")), ("9.5", 20, t("Milky Way", "Vía Láctea"))]
    x0, x1, e0, e1 = 50, 690, -16, 22
    def X(e):
        return x0 + (e - e0) * (x1 - x0) / (e1 - e0)
    marcas = "".join(f'<line x1="{X(e):.0f}" y1="92" x2="{X(e):.0f}" y2="102" stroke="#5b6675"/><text x="{X(e):.0f}" y="120" text-anchor="middle" font-size="13" fill="#5b6675">10{str(e).translate(SUP)}</text>' for e in range(-15, 22, 6))
    puntos = "".join(f'<circle cx="{X(e + 0.2):.0f}" cy="97" r="6" fill="#2a7f86"/><text x="{X(e + 0.2):.0f}" y="{70 if i % 2 else 50}" text-anchor="middle" font-size="14" font-weight="700" fill="#1a2330">{n}</text><line x1="{X(e + 0.2):.0f}" y1="{74 if i % 2 else 54}" x2="{X(e + 0.2):.0f}" y2="90" stroke="#90a4ae"/>' for i, (c, e, n) in enumerate(escala))
    figura = (f'<svg viewBox="0 0 740 140" role="img" aria-label="{t("Number line of powers of ten, from 10 to the negative 15 to 10 to the 21 meters, with a proton, an atom, a flu virus, a person, Earth, the distance from Earth to the Sun, and the Milky Way. Equal steps on the line mean multiplying by the same number, not adding.", "Recta de potencias de diez, de 10 elevado a menos 15 a 10 elevado a 21 metros, con un protón, un átomo, un virus de la gripe, una persona, la Tierra, la distancia Tierra–Sol y la Vía Láctea. Pasos iguales en la recta significan multiplicar por el mismo número, no sumar.")}" style="width:100%;max-width:740px;height:auto;display:block;margin:12px auto;">'
              f'<line x1="{x0}" y1="97" x2="{x1}" y2="97" stroke="#1a2330" stroke-width="2"/>{marcas}{puntos}<text x="{x1}" y="136" text-anchor="end" font-size="12" fill="#5b6675">{t("meters", "metros")}</text></svg>')
    s4 = f"""<p>{t("The same value can be written with many units, but usually only one makes the number easy to read. The metric prefixes are powers of ten with a name. On the GED® Science test, as in all science, measurements are in the metric system (1 meter is about 3.3 feet; 1 kilogram is about 2.2 pounds).", "Un mismo valor puede escribirse con muchas unidades, pero solo una hace que el número resulte cómodo de leer. Los prefijos del sistema métrico son potencias de diez con nombre propio. En el examen de Ciencias del GED®, como en toda la ciencia, las medidas van en el sistema métrico.")}</p>
{C.tabla(t("Metric prefixes common on the test, the power of ten for each one, and a typical size", "Prefijos del sistema métrico frecuentes en el examen, la potencia de diez de cada uno y una magnitud típica"),
 [t("Prefix", "Prefijo"), t("Power of 10", "Potencia de 10"), t("Typical size", "Magnitud típica")],
 [[t("giga- (G)", "giga- (G)"), "10⁹", t("Distances between planets; computer memory.", "Distancias planetarias; capacidad de memoria.")],
  [t("mega- (M)", "mega- (M)"), "10⁶", t("Radius of Earth: about 6.4 megameters.", "Radio de la Tierra: unos 6.4 megámetros.")],
  [t("kilo- (k)", "kilo- (k)"), "10³", t("Distances on a map; body mass in kilograms.", "Distancias geográficas; masa corporal en kilogramos.")],
  [t("centi- (c)", "centi- (c)"), "10⁻²", t("Length of a sheet of paper in centimeters.", "Longitud de una hoja de papel en centímetros.")],
  [t("milli- (m)", "mili- (m)"), "10⁻³", t("Thickness of a coin; rainfall in millimeters.", "Grosor de una moneda; precipitación en milímetros.")],
  [t("micro- (µ)", "micro- (µ)"), "10⁻⁶", t("Size of a cell: 10 to 100 micrometers.", "Tamaño de una célula: entre 10 y 100 micrómetros.")],
  [t("nano- (n)", "nano- (n)"), "10⁻⁹", t("Wavelength of visible light: 400 to 700 nanometers.", "Longitud de onda de la luz visible: de 400 a 700 nanómetros.")]])}
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"The prefixes come from Greek and Latin, and their literal meaning helps you remember them. <span class='raiz'>Micro-</span> means “small” (microscope, microorganism). <span class='raiz'>Nano-</span> means “dwarf.” <span class='raiz'>Mega-</span> means “great.” <span class='raiz'>Kilo-</span> means “thousand.” <span class='raiz'>Giga-</span> comes from the Greek word for “giant.” If you know these five pieces, you can work out the size even if you forget the exact exponent.", "Los prefijos vienen del griego y del latín, y su significado literal ayuda a recordarlos. <span class='raiz'>Micro-</span> significa «pequeño» (microscopio, microorganismo). <span class='raiz'>Nano-</span> significa «enano». <span class='raiz'>Mega-</span> significa «grande». <span class='raiz'>Kilo-</span> significa «mil». <span class='raiz'>Giga-</span> viene de la palabra griega para «gigante». Quien reconoce estas cinco piezas deduce el orden de magnitud aunque no recuerde el exponente exacto.")}</p>
<h3>{t("The whole scale, from one end to the other", "La escala completa, de un extremo al otro")}</h3>
<p>{t("This line puts seven objects on the same line of powers of ten. Each step on the line means multiplying by the same amount, not adding: that is why a proton and a galaxy fit in the same picture.", "Esta recta sitúa siete objetos sobre una misma recta de potencias de diez. Cada paso de la recta equivale a multiplicar por la misma cantidad, no a sumar: por eso el protón y la galaxia caben en la misma imagen.")}</p>
{figura}
{C.caja("ojo", t("A line that fools your intuition", "Una recta que engaña a la intuición"), "<p>" + t("On this line, halfway between 1 meter and 10¹⁸ meters is not 500,000,000,000,000,000 meters, but 10⁹: one billion. Scales like this (logarithmic scales) appear on the test in graphs of earthquakes, acidity (pH), and sound, always for the same reason: the data cover so many powers of ten that no ordinary scale could show them together.", "En esta recta, la mitad del camino entre 1 metro y 10¹⁸ metros no está en 500,000,000,000,000,000 metros, sino en 10⁹: mil millones. Las escalas de este tipo (logarítmicas) aparecen en el examen en gráficas de terremotos, de acidez (pH) y de intensidad sonora, siempre por la misma razón: los datos abarcan tantas potencias de diez que ninguna escala corriente los mostraría juntos.") + "</p>")}
{P(t("Try it 7 · The right unit", "Pruebe 7 · La unidad adecuada"), t(f"A cell is {s('2', -5)} m long. The easiest unit to say that size is…", f"Una célula mide {s('2', -5)} m. La unidad más cómoda para expresar esa medida es…"),
   [t("the nanometer", "el nanómetro"), t("the micrometer", "el micrómetro"), t("the kilometer", "el kilómetro")], 1,
   {0: t(f"In nanometers it would be 20,000 nm: a big number. Which prefix is closest to {s('1', -5)}?", f"En nanómetros serían 20,000 nm: un número grande. ¿Qué prefijo se acerca más a {s('1', -5)}?"),
    2: t("A kilometer is huge. The cell is tiny.", "Un kilómetro es enorme. La célula es diminuta.")},
   t(f"{s('2', -5)} m = {s('20', -6)} m = 20 micrometers (20 µm), an easy number to read.", f"{s('2', -5)} m = {s('20', -6)} m = 20 micrómetros (20 µm), un número cómodo de leer."))}
{C.enlace(N, anc("units", "unidades"), t("choose the unit", "elija la unidad"), t("Real sizes, from atoms to stars: choose the unit that makes each number easy to read.", "Tamaños reales, de átomos a estrellas: elija la unidad que hace cómodo cada número."))}"""

    s5 = f"""<p>{t("The TI-30XS MultiView™ is the calculator used on the GED® test, on the screen and at the test center. In this lesson you use it only to <strong>check</strong> conversions and operations you already did by hand.", "La TI-30XS MultiView™ es la calculadora del examen GED®, en pantalla y en el centro de examen. En esta lección se usa solo para <strong>comprobar</strong> conversiones y operaciones que ya se resolvieron a mano.")}</p>
{C.tabla(t("TI-30XS MultiView keys for scientific notation, how to use them, and a warning for each one", "Funciones de la TI-30XS MultiView para notación científica, cómo se usan y la advertencia de cada una"),
 [t("Key or function", "Función"), t("How to use it", "Cómo se usa"), t("Warning", "Advertencia")],
 [[t("The ×10ⁿ key", "Tecla ×10ⁿ"), t(f"Enters the power of ten directly. For {s('3.6', 8)}, type the coefficient, then this key, then the exponent.", f"Introduce directamente la potencia de diez. Para {s('3.6', 8)} se teclea el coeficiente, después esta tecla y por último el exponente."), t("Do not type “× 10 ^ 8”: the result is the same, but it is longer and easy to get wrong with parentheses.", "No teclee «× 10 ^ 8»: el resultado sería el mismo, pero es más largo y se presta a errores de paréntesis.")],
  [t("The sign key (−)", "Tecla de signo (−)"), t(f"Enters negative exponents, as in {s('4.7', -4)}.", f"Introduce exponentes negativos, como en {s('4.7', -4)}."), t("It is not the subtraction key. Using subtraction gives an error or a wrong answer.", "Es distinta de la de restar. Usar la de restar da error o un resultado equivocado.")],
  [t("The mode menu", "Menú mode"), t("Lets you choose NORM, SCI, or ENG. In SCI, every answer is shown in scientific notation.", "Permite elegir NORM, SCI o ENG. En SCI todos los resultados se muestran en notación científica."), t("Go back to NORM when you finish, or later answers will look strange.", "Vuelva a NORM al terminar, o los resultados siguientes aparecerán en un formato inesperado.")],
  [t("Clear first", "Limpieza previa"), t("Before you start, clear the screen and any stored values from an earlier problem.", "Antes de empezar, borre la pantalla y los valores guardados de un ejercicio anterior."), t("A value left over from before is a common cause of strange answers.", "Un valor que quedó de antes es una causa frecuente de resultados incoherentes.")]])}
{C.ejemplo(t("Example 4 · First by hand, then the calculator", "Ejemplo 4 · Primero a mano, después la calculadora"),
 [("", t(f"How many hydrogen atoms, each {s('1', -10)} m wide, fit in a row along one millimeter?", f"¿Cuántos átomos de hidrógeno, de {s('1', -10)} m de diámetro, caben alineados en un milímetro?")),
  ("1", t(f"Write the millimeter in scientific notation: 1 mm = {s('1', -3)} m.", f"Se expresa el milímetro en notación científica: 1 mm = {s('1', -3)} m.")),
  ("2", t(f"Set up the division: ({s('1', -3)}) ÷ ({s('1', -10)}).", f"Se plantea la división: ({s('1', -3)}) ÷ ({s('1', -10)}).")),
  ("3", t("Coefficients: 1 ÷ 1 = 1. Exponents: −3 − (−10) = 7.", "Coeficientes: 1 ÷ 1 = 1. Exponentes: −3 − (−10) = 7.")),
  ("4", t(f"Estimate by hand: {s('1', 7)}, ten million atoms.", f"Estimación a mano: {s('1', 7)}, diez millones de átomos.")),
  ("5", t("Check on the calculator with the ×10ⁿ key and the sign key for the negative exponents. It should show 10,000,000.", "Verificación en la calculadora, con la tecla ×10ⁿ y la tecla de signo para los exponentes negativos. Debe aparecer 10,000,000."))],
 t("<strong>Why in that order:</strong> if you estimated first, you will notice right away if the screen shows nonsense. If you type without estimating, you will accept anything.", "<strong>Por qué en ese orden:</strong> quien estimó primero reconoce de inmediato si la pantalla muestra un disparate. Quien teclea sin estimar acepta cualquier cosa."))}
{C.calc(t("Try it on the calculator", "Pruébelo en la calculadora"), "<p>" + t("Open the calculator and check Example 4: type 1, ×10ⁿ, (−), 3, then ÷, then 1, ×10ⁿ, (−), 10, and enter. The screen should show 10000000.", "Abra la calculadora y compruebe el Ejemplo 4: teclee 1, ×10ⁿ, (−), 3, después ÷, luego 1, ×10ⁿ, (−), 10, y enter. La pantalla debe mostrar 10000000.") + "</p>")}
{C.caja("ojo", t("The calculator does not choose the size for you", "La calculadora no decide el orden de magnitud"), "<p>" + t("If you enter an exponent with the wrong sign, the calculator returns an answer that is perfectly calculated and completely wrong. No error message warns you. Your only protection is the estimate you made by hand first.", "Si el exponente se introduce con el signo cambiado, la máquina devolverá un resultado impecablemente calculado y completamente falso. Ningún mensaje de error avisa. La única defensa es la estimación previa hecha a mano.") + "</p>")}
{C.enlace(N, anc("clinic", "clinica"), t("the TI-30XS clinic", "la clínica de la TI-30XS"), t("Estimate by hand first, then check with the calculator. Plus five “broken screen” cases: find what went wrong.", "Primero estime a mano, después compruebe con la calculadora. Y cinco «averías»: descubra qué salió mal."))}"""

    s6 = f"""<p>{t("A short science text written for this level. Notice that every size is in scientific notation, as on the test.", "Texto científico breve adaptado al nivel. Todas las magnitudes aparecen en notación científica, como en el examen.")}</p>
{C.lectura(t("Why you cannot see a virus with a light microscope", "Por qué un virus no se ve con un microscopio de luz"),
 [t(f"A light microscope cannot tell apart two points that are too close together. The problem is not the quality of the lenses: it is light itself. Visible light has wavelengths between {s('4', -7)} m and {s('7', -7)} m, and no instrument that uses light can separate details much smaller than that. In practice, the limit is about {s('2', -7)} m.", f"Un microscopio óptico no puede distinguir dos puntos que estén demasiado próximos entre sí. El obstáculo no es la calidad de las lentes: es la propia luz. La luz visible tiene longitudes de onda entre {s('4', -7)} m y {s('7', -7)} m, y ningún instrumento que use luz puede separar detalles mucho más pequeños que ese tamaño. En la práctica, el límite se sitúa alrededor de {s('2', -7)} m."),
  t(f"A common bacterium is between {s('1', -6)} m and {s('5', -6)} m long, several times that limit. That is why bacteria are easy to see with a school microscope; they were first described in the 1600s with very simple instruments.", f"Una bacteria común mide entre {s('1', -6)} m y {s('5', -6)} m, es decir, varias veces ese límite. Por eso las bacterias se observan sin dificultad con un microscopio escolar, y fueron descritas por primera vez en el siglo XVII con instrumentos muy modestos."),
  t(f"A flu virus, in contrast, is about {s('1', -7)} m: half the limit. More magnification does not help. The image gets bigger, but no new detail appears, because the information was never formed. For decades, scientists knew viruses existed without anyone having seen one.", f"Un virus de la gripe mide, en cambio, alrededor de {s('1', -7)} m: la mitad del límite. Aumentar los aumentos no sirve de nada. La imagen se agranda, pero no aparece ningún detalle nuevo, porque la información nunca llegó a formarse. Durante décadas se supo que los virus existían sin que nadie hubiera visto uno."),
  t(f"The solution was to replace light with electrons, whose wavelength is around {s('1', -12)} m, millions of times smaller. The electron microscope, built in the 1930s, gave the first pictures of a virus at the end of that decade.", f"La solución fue sustituir la luz por electrones, cuya longitud de onda es del orden de {s('1', -12)} m, millones de veces menor. El microscopio electrónico, desarrollado en la década de 1930, permitió obtener las primeras imágenes de un virus a finales de esa misma década.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the central idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Bacteria were first described in the 1600s.", "Las bacterias fueron descritas por primera vez en el siglo XVII."), t("The limit of a light microscope depends not on magnification but on the wavelength of light.", "El límite de un microscopio óptico no depende del aumento, sino de la longitud de onda de la luz."), t("The electron microscope was built in the 1930s.", "El microscopio electrónico se desarrolló en la década de 1930.")], 1,
   {0: t("That is a detail of paragraph 2.", "Es un detalle del párrafo 2."), 2: t("That is a detail of the last paragraph. What do all four paragraphs explain?", "Es un detalle del último párrafo. ¿Qué explican los cuatro párrafos?")},
   t("All four paragraphs explain one idea: light sets the limit, so more magnification does not help.", "Los cuatro párrafos explican una idea: la luz pone el límite, y por eso más aumento no sirve."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t(f"How many times larger is a bacterium of {s('2', -6)} m than a virus of {s('1', -7)} m?", f"¿Cuántas veces mayor es una bacteria de {s('2', -6)} m que un virus de {s('1', -7)} m?"),
   [t("2 times", "2 veces"), t("200 times", "200 veces"), t("20 times", "20 veces")], 2,
   {0: t("Do not forget the exponents: −6 − (−7) = 1, so multiply 2 by 10.", "No olvide los exponentes: −6 − (−7) = 1, así que hay que multiplicar 2 por 10."), 1: t("Check the exponents: −6 − (−7) is 1, not 2.", "Revise los exponentes: −6 − (−7) es 1, no 2.")},
   t(f"Divide: 2 ÷ 1 = 2 and −6 − (−7) = 1, so {s('2', 1)} = 20 times.", f"Se divide: 2 ÷ 1 = 2 y −6 − (−7) = 1, es decir, {s('2', 1)} = 20 veces."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t(f"To say the limit, {s('2', -7)} m, with an easy prefix, you would say…", f"Para expresar el límite, {s('2', -7)} m, con un prefijo cómodo conviene decir…"),
   [t("200 nanometers", "200 nanómetros"), t("200 millimeters", "200 milímetros"), t("200 kilometers", "200 kilómetros")], 0,
   {1: t(f"200 mm is 20 cm: the size of a hand. The limit is far smaller.", "200 mm son 20 cm: el tamaño de una mano. El límite es muchísimo menor."), 2: t("Kilometers are for huge distances.", "Los kilómetros son para distancias enormes.")},
   t(f"{s('2', -7)} m = {s('200', -9)} m = 200 nm.", f"{s('2', -7)} m = {s('200', -9)} m = 200 nm."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("According to the text, why does more magnification not let you see a virus with a light microscope?", "Según el texto, ¿por qué aumentar los aumentos del microscopio óptico no permite ver un virus?"),
   [t("Because the virus moves too fast", "Porque el virus se mueve demasiado rápido"), t("Because school lenses are low quality", "Porque las lentes escolares son de baja calidad"), t("Because the detail was never formed in the image: light is the limit", "Porque el detalle nunca llegó a formarse en la imagen: la limitación está en la luz")], 2,
   {0: t("The text says nothing about movement.", "El texto no habla de movimiento."), 1: t("The text says the problem is not the lenses.", "El texto dice que el obstáculo no es la calidad de las lentes.")},
   t("Paragraph 3: the image gets bigger, but no new detail appears, because light cannot form it.", "Párrafo 3: la imagen se agranda, pero no aparece ningún detalle nuevo, porque la luz no puede formarlo."))}"""

    G = lambda *a: C.ged_item(P, *a)
    tabla_g = C.tabla(t("Approximate sizes of four objects", "Tamaño aproximado de cuatro objetos"), [t("Object", "Objeto"), t("Size (m)", "Tamaño (m)")],
        [[t("Flu virus", "Virus de la gripe"), s("1", -7)], [t("<em>E. coli</em> bacterium", "Bacteria <em>E. coli</em>"), s("2", -6)], [t("Red blood cell", "Glóbulo rojo"), s("8", -6)], [t("Human hair (thickness)", "Cabello humano (grosor)"), s("7", -5)]])
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text or a table, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK). You may use the calculator, but estimate first.", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve o una tabla, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora, pero estime primero.") + f"""</p>
{tabla_g}
{G(1, "SP.1.c", "2", t("Which object in the table is about 35 times thicker than a bacterium?", "¿Qué objeto de la tabla es unas 35 veces más grueso que la bacteria?"),
   [t("The flu virus", "El virus de la gripe"), t("The red blood cell", "El glóbulo rojo"), t("The human hair", "El cabello humano"), t("None of them", "Ninguno")], 2,
   {0: t("The virus is smaller than the bacterium, not larger.", "El virus es más pequeño que la bacteria, no más grande."), 1: t(f"Divide: {s('8', -6)} ÷ {s('2', -6)} = 4. That is 4 times, not 35.", f"Divida: {s('8', -6)} ÷ {s('2', -6)} = 4. Son 4 veces, no 35."), 3: t(f"Try the hair: {s('7', -5)} ÷ {s('2', -6)}.", f"Pruebe con el cabello: {s('7', -5)} ÷ {s('2', -6)}.")},
   t(f"{s('7', -5)} ÷ {s('2', -6)}: 7 ÷ 2 = 3.5 and −5 − (−6) = 1, so {s('3.5', 1)} = 35.", f"{s('7', -5)} ÷ {s('2', -6)}: 7 ÷ 2 = 3.5 y −5 − (−6) = 1, es decir, {s('3.5', 1)} = 35."))}
{G(2, "SP.1.b", "2", t("A student’s calculator shows <strong>1.5E11</strong> for the distance from Earth to the Sun in meters. How should the student write this answer?", "La calculadora de un estudiante muestra <strong>1.5E11</strong> para la distancia de la Tierra al Sol en metros. ¿Cómo debe escribir esa respuesta?"),
   [t("1.5E11 m, as the screen shows", "1.5E11 m, tal como aparece"), s("1.5", 11) + " m", s("15", 10) + " m", t("1.5 to the 11th power m", "1.5 elevado a 11 m")], 1,
   {0: t("The E is the calculator’s shortcut. It is not how you write scientific notation.", "La E es una abreviatura de la máquina. No es así como se escribe la notación científica."), 2: t("The value is the same, but 15 is not between 1 and 10.", "El valor es el mismo, pero 15 no está entre 1 y 10."), 3: t("The E does not mean “to the power of” on the 1.5. It means “times 10 to the power of.”", "La E no significa que 1.5 se eleve a una potencia. Significa «por 10 elevado a».")},
   t(f"E means “times 10 to the power of,” so 1.5E11 is {s('1.5', 11)} m.", f"E significa «por 10 elevado a», así que 1.5E11 es {s('1.5', 11)} m."))}
{G(3, "SP.7.b", "2", t(f"The formula sheet gives: <strong>speed = distance ÷ time</strong>. Light travels at {s('3', 8)} m/s, and the Sun is {s('1.5', 11)} m from Earth. About how long does sunlight take to reach Earth?", f"La hoja de fórmulas da: <strong>rapidez = distancia ÷ tiempo</strong>. La luz viaja a {s('3', 8)} m/s y el Sol está a {s('1.5', 11)} m de la Tierra. ¿Cuánto tarda, aproximadamente, la luz del Sol en llegar a la Tierra?"),
   [t("5 seconds", "5 segundos"), t("50 seconds", "50 segundos"), t("500 seconds (about 8 minutes)", "500 segundos (unos 8 minutos)"), t("4.5 × 10¹⁹ seconds", "4.5 × 10¹⁹ segundos")], 2,
   {0: t("Check the exponents: 11 − 8 = 3, not 0.", "Revise los exponentes: 11 − 8 = 3, no 0."), 1: t(f"1.5 ÷ 3 = 0.5, and 0.5 × 10³ is not 50.", f"1.5 ÷ 3 = 0.5, y 0.5 × 10³ no es 50."), 3: t("That is distance × speed. To find time, solve the formula for time: time = distance ÷ speed.", "Eso es distancia × rapidez. Para hallar el tiempo, despeje: tiempo = distancia ÷ rapidez.")},
   t(f"time = distance ÷ speed = ({s('1.5', 11)}) ÷ ({s('3', 8)}) = {s('0.5', 3)} = {s('5', 2)} s = 500 s, a little over 8 minutes.", f"tiempo = distancia ÷ rapidez = ({s('1.5', 11)}) ÷ ({s('3', 8)}) = {s('0.5', 3)} = {s('5', 2)} s = 500 s, algo más de 8 minutos."))}
{G(4, "SP.3.b", "2–3", t(f"Use the reading about microscopes. A certain virus is {s('3', -7)} m wide. What can you conclude?", f"Use la lectura sobre los microscopios. Un virus mide {s('3', -7)} m de ancho. ¿Qué se puede concluir?"),
   [t("It can never be seen with any microscope.", "No se puede ver con ningún microscopio."), t("It is just above the limit of about 2 × 10⁻⁷ m, so a light microscope may barely show it.", "Está justo por encima del límite de unos 2 × 10⁻⁷ m, así que un microscopio óptico podría mostrarlo apenas."), t("It is smaller than the flu virus, so it is easier to see.", "Es más pequeño que el virus de la gripe, así que es más fácil de ver."), t("It is the same size as a bacterium.", "Es del mismo tamaño que una bacteria.")], 1,
   {0: t("An electron microscope can see even smaller things.", "Un microscopio electrónico puede ver cosas aún más pequeñas."), 2: t(f"Compare: {s('3', -7)} is three times {s('1', -7)}. It is larger.", f"Compare: {s('3', -7)} es el triple de {s('1', -7)}. Es más grande."), 3: t(f"A bacterium is at least {s('1', -6)} m, more than 3 times larger.", f"Una bacteria mide al menos {s('1', -6)} m, más de 3 veces más.")},
   t(f"{s('3', -7)} m is 1.5 times the limit of {s('2', -7)} m: just above it, so it may barely be seen. The data support a careful conclusion, not a strong one.", f"{s('3', -7)} m es 1.5 veces el límite de {s('2', -7)} m: justo por encima, así que podría verse apenas. Los datos apoyan una conclusión prudente, no una tajante."))}
{G(5, "SP.6.b", "2", t("The mass of Earth is about 5,970,000,000,000,000,000,000,000 kg. Which is the same mass in scientific notation?", "La masa de la Tierra es de unos 5,970,000,000,000,000,000,000,000 kg. ¿Cuál es la misma masa en notación científica?"),
   [s("5.97", 21) + " kg", s("5.97", 24) + " kg", s("597", 22) + " kg", s("5.97", -24) + " kg"], 1,
   {0: t("Count the digits after the 5: there are 24 places, not 21. Count by groups of three.", "Cuente las cifras después del 5: son 24 lugares, no 21. Cuente de tres en tres."), 2: t("The value is right, but 597 is not between 1 and 10.", "El valor es correcto, pero 597 no está entre 1 y 10."), 3: t("The number is huge, so the exponent must be positive.", "El número es enorme, así que el exponente tiene que ser positivo.")},
   t(f"After the 5 there are 8 groups of three digits: 24 places. {s('5.97', 24)} kg.", f"Después del 5 hay 8 grupos de tres cifras: 24 lugares. {s('5.97', 24)} kg."))}"""

    secciones = [
        ("s1", t("What scientific notation is and how it is built", "Qué es la notación científica y cómo está construida"), s1),
        ("s2", t("Converting both ways", "Convertir en los dos sentidos"), s2),
        ("s3", t("Multiplying and dividing in scientific notation", "Multiplicar y dividir en notación científica"), s3),
        ("s4", t("Units, prefixes, and the scale of the universe", "Unidades, prefijos y la escala del universo"), s4),
        ("s5", t("The TI-30XS MultiView™ calculator", "La calculadora TI-30XS MultiView™"), s5),
        ("s6", t("Science reading", "Lectura científica"), s6),
        ("s7", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Ten real numbers.", "Diez números reales."), t("Find ten sizes in science (an atom, a cell, a mountain, a planet…) in a book or the news. Write each one in scientific notation and as a decimal.", "Busque diez magnitudes de la ciencia (un átomo, una célula, una montaña, un planeta…) en un libro o una noticia. Escriba cada una en notación científica y en notación decimal.")),
        (t("Choose the unit.", "Elija la unidad."), t("For five of them, choose the prefix that makes the number easiest to read, and explain your choice in one sentence.", "Para cinco de ellas, elija el prefijo que hace más cómodo el número y justifique la elección en una oración.")),
        (t("Estimate, then check.", "Estime y compruebe."), t("For three multiplications or divisions, write your estimate by hand first, then the calculator’s result. Did they agree? If not, find what was typed wrong.", "En tres multiplicaciones o divisiones, escriba primero su estimación a mano y después el resultado de la calculadora. ¿Coincidieron? Si no, encuentre qué se tecleó mal.")),
    ]
    Q = lambda p, o, k, h, x: (p, o, k, h, x)
    quiz = [
        Q(t("0.00047 in scientific notation is…", "El número 0.00047 en notación científica es…"), [s("4.7", -3), s("4.7", -4), s("47", -5), s("4.7", 4)], 1,
          {0: t("Count the places again: four.", "Cuente otra vez los lugares: cuatro."), 2: t("47 is not between 1 and 10.", "47 no está entre 1 y 10."), 3: t("The number is less than 1: negative exponent.", "El número es menor que 1: exponente negativo.")}, t("Four places to the right: 4.7 × 10⁻⁴.", "Cuatro lugares a la derecha: 4.7 × 10⁻⁴.")),
        Q(t("Which number is NOT written correctly in scientific notation?", "¿Cuál de estos números NO está bien escrito en notación científica?"), [s("3.0", 8), s("1.6", -19), s("12.5", 3), s("9.8", 0)], 2,
          {0: t("3.0 is between 1 and 10.", "3.0 está entre 1 y 10."), 1: t("A negative exponent is fine.", "Un exponente negativo es válido."), 3: t("10⁰ = 1, and 9.8 is between 1 and 10. It is valid.", "10⁰ = 1, y 9.8 está entre 1 y 10. Es válido.")}, t("12.5 is not less than 10. Correctly: 1.25 × 10⁴.", "12.5 no es menor que 10. Bien escrito: 1.25 × 10⁴.")),
        Q(t(f"{s('5.2', -6)} as a decimal is…", f"El número {s('5.2', -6)} en notación decimal es…"), ["0.000052", "0.0000052", "5,200,000", "0.00000052"], 1,
          {0: t("That is 5.2 × 10⁻⁵. Count six places.", "Eso es 5.2 × 10⁻⁵. Cuente seis lugares."), 2: t("A negative exponent makes a small number.", "Un exponente negativo da un número pequeño."), 3: t("That is 5.2 × 10⁻⁷. Count again.", "Eso es 5.2 × 10⁻⁷. Cuente otra vez.")}, t("Six places to the left: 0.0000052.", "Seis lugares a la izquierda: 0.0000052.")),
        Q(t("The average distance from Earth to the Sun is 149,600,000 km. In scientific notation it is…", "La distancia media de la Tierra al Sol es de 149,600,000 km. En notación científica es…"), [s("14.96", 7) + " km", s("1.496", 9) + " km", s("1.496", 8) + " km", s("1.496", -8) + " km"], 2,
          {0: t("14.96 is not between 1 and 10.", "14.96 no está entre 1 y 10."), 1: t("Count the places: eight.", "Cuente los lugares: ocho."), 3: t("A large number has a positive exponent.", "Un número grande tiene exponente positivo.")}, t("Eight places to the left: 1.496 × 10⁸ km.", "Ocho lugares a la izquierda: 1.496 × 10⁸ km.")),
        Q(t(f"A virus is {s('1', -7)} m wide. The best unit for this size is…", f"Un virus mide {s('1', -7)} m. La unidad más apropiada para expresarlo es…"), [t("the millimeter", "el milímetro"), t("the nanometer", "el nanómetro"), t("the meter", "el metro"), t("the kilometer", "el kilómetro")], 1,
          {0: t("In millimeters it would be 0.0001 mm: still a hard number.", "En milímetros serían 0.0001 mm: sigue siendo incómodo."), 2: t("In meters you need many zeros.", "En metros hacen falta muchos ceros."), 3: t("Kilometers are for huge distances.", "Los kilómetros son para distancias enormes.")}, t("1 × 10⁻⁷ m = 100 × 10⁻⁹ m = 100 nm.", "1 × 10⁻⁷ m = 100 × 10⁻⁹ m = 100 nm.")),
        Q(t("One kilometer, in meters, is…", "Un kilómetro equivale, en metros, a…"), [s("1", 3) + " m", s("1", 6) + " m", s("1", -3) + " m", s("1", 2) + " m"], 0,
          {1: t("10⁶ is mega-.", "10⁶ es mega-."), 2: t("10⁻³ is milli-.", "10⁻³ es mili-."), 3: t("10² is hecto-.", "10² es hecto-.")}, t("Kilo- means one thousand: 10³.", "Kilo- significa mil: 10³.")),
        Q(t("A sheet of paper is 0.0001 m thick. With the right prefix, that is…", "Una hoja de papel tiene 0.0001 m de grosor. Con el prefijo adecuado, ese grosor es de…"), [t("100 millimeters", "100 milímetros"), t("100 micrometers", "100 micrómetros"), t("100 nanometers", "100 nanómetros"), t("100 kilometers", "100 kilómetros")], 1,
          {0: t("100 mm is 10 cm. Much too thick.", "100 mm son 10 cm. Demasiado grueso."), 2: t("100 nm is far too thin: that is a virus.", "100 nm es demasiado delgado: es un virus."), 3: t("Kilometers are for huge distances.", "Los kilómetros son para distancias enormes.")}, t("0.0001 m = 1 × 10⁻⁴ m = 100 × 10⁻⁶ m = 100 µm.", "0.0001 m = 1 × 10⁻⁴ m = 100 × 10⁻⁶ m = 100 µm.")),
        Q(t(f"Light travels {s('3', 8)} m in one second. To write this distance with an easier number, use…", f"La luz recorre {s('3', 8)} m en un segundo. Para expresar esa distancia con un número más manejable conviene usar…"), [t("millimeters", "milímetros"), t("nanometers", "nanómetros"), t("centimeters", "centímetros"), t("kilometers", "kilómetros")], 3,
          {0: t("Smaller units make the number even bigger.", "Unidades más pequeñas hacen el número aún más grande."), 1: t("Smaller units make the number even bigger.", "Unidades más pequeñas hacen el número aún más grande."), 2: t("Smaller units make the number even bigger.", "Unidades más pequeñas hacen el número aún más grande.")}, t("3 × 10⁸ m = 3 × 10⁵ km = 300,000 km.", "3 × 10⁸ m = 3 × 10⁵ km = 300,000 km.")),
        Q(t(f"({s('3', 5)}) · ({s('2', 3)}) equals…", f"El producto ({s('3', 5)}) · ({s('2', 3)}) es igual a…"), [s("6", 8), s("6", 15), s("5", 8), s("6", 2)], 0,
          {1: t("Exponents are added, not multiplied.", "Los exponentes se suman, no se multiplican."), 2: t("Coefficients are multiplied, not added.", "Los coeficientes se multiplican, no se suman."), 3: t("When you multiply, add the exponents.", "Al multiplicar, se suman los exponentes.")}, t("3 × 2 = 6 and 5 + 3 = 8.", "3 × 2 = 6 y 5 + 3 = 8.")),
        Q(t(f"({s('8', 9)}) ÷ ({s('4', 4)}) equals…", f"El cociente ({s('8', 9)}) ÷ ({s('4', 4)}) es igual a…"), [s("2", 13), s("2", 5), s("4", 5), s("2", -5)], 1,
          {0: t("When you divide, subtract the exponents.", "Al dividir, se restan los exponentes."), 2: t("8 ÷ 4 = 2, not 4.", "8 ÷ 4 = 2, no 4."), 3: t("9 − 4 = 5, positive.", "9 − 4 = 5, positivo.")}, t("8 ÷ 4 = 2 and 9 − 4 = 5.", "8 ÷ 4 = 2 y 9 − 4 = 5.")),
        Q(t(f"({s('5', 4)}) · ({s('4', 3)}) gives {s('20', 7)}. Written correctly, the answer is…", f"Al multiplicar ({s('5', 4)}) · ({s('4', 3)}) se obtiene {s('20', 7)}. El resultado bien escrito es…"), [s("20", 7), s("2", 7), s("2", 8), s("9", 7)], 2,
          {0: t("20 is not between 1 and 10.", "20 no está entre 1 y 10."), 1: t("20 = 2 × 10¹: the exponent must go up by 1.", "20 = 2 × 10¹: el exponente tiene que subir 1."), 3: t("5 × 4 is 20, not 9.", "5 × 4 es 20, no 9.")}, t("20 × 10⁷ = 2 × 10⁸.", "20 × 10⁷ = 2 × 10⁸.")),
        Q(t(f"A red blood cell is {s('8', -6)} m and a bacterium is {s('2', -6)} m. The red blood cell is…", f"Un glóbulo rojo mide {s('8', -6)} m y una bacteria {s('2', -6)} m. El glóbulo rojo es…"), [t("4 times larger", "4 veces mayor"), t("4 times smaller", "4 veces menor"), t("16 times larger", "16 veces mayor"), t("4 × 10⁻¹² times larger", "4 × 10⁻¹² veces mayor")], 0,
          {1: t("8 is more than 2, so the blood cell is larger.", "8 es más que 2: el glóbulo es mayor."), 2: t("Divide, do not multiply: 8 ÷ 2.", "Divida, no multiplique: 8 ÷ 2."), 3: t("When you divide, subtract the exponents: −6 − (−6) = 0.", "Al dividir, se restan los exponentes: −6 − (−6) = 0.")}, t("8 ÷ 2 = 4 and the exponents cancel: 4 times larger.", "8 ÷ 2 = 4 y los exponentes se cancelan: 4 veces mayor.")),
    ]
    filas = [
        (t("Place the point and the exponent", "Coloca el punto y el exponente"), t("I convert both ways and check that the sign of the exponent matches the size of the number.", "Convierto en los dos sentidos y compruebo que el signo del exponente corresponde al tamaño del número."), t("I place the point, but I get the sign or the count wrong.", "Coloco el punto, pero me equivoco en el signo o en el conteo."), t("I move the point without a plan.", "Muevo el punto sin criterio.")),
        (t("Multiply and divide with no size errors", "Opera sin errores de magnitud"), t("I multiply and divide, adjust the coefficient, and predict the size before I calculate.", "Multiplico y divido, ajusto el coeficiente y anticipo el orden de magnitud."), t("I separate the pieces, but I forget to adjust the coefficient.", "Separo las piezas, pero no ajusto el coeficiente."), t("I mix coefficients and exponents.", "Mezclo coeficientes y exponentes.")),
        (t("Choose the right unit", "Elige la unidad adecuada"), t("I choose the prefix that makes the number easy and explain it with its power of ten.", "Elijo el prefijo que hace cómodo el número y lo justifico con su potencia de diez."), t("I change units, but the number is still awkward.", "Cambio de unidad, pero el número sigue siendo incómodo."), t("I always use the same unit.", "Uso siempre la misma unidad.")),
        (t("Use the calculator to check, not to think", "Usa la calculadora para verificar, no para pensar"), t("I estimate first, compare, and find the typing error when they disagree.", "Estimo primero, comparo y, si no coinciden, encuentro el error de tecleo."), t("I estimate sometimes, but I do not compare.", "Estimo a veces, pero no comparo."), t("I type without estimating and accept any answer.", "Tecleo sin estimar y acepto cualquier resultado.")),
    ]
    cierre = "<p>" + t("You now have the tool to handle any size on the test, however tiny or huge, and the habit of estimating before you type, which every content topic will ask of you.", "Esta lección deja la herramienta para manejar cualquier magnitud del examen, por diminuta o enorme que sea, y el hábito de estimar antes de teclear, que se exigirá en todos los temas de contenido.") + "</p><p>" + \
             t("Lesson 2.2 moves to graphs: real graphs of carbon dioxide, population growth, and solubility, and how to go from table to graph to paragraph. The numbers you learned to write here are the ones you will read on an axis.", "La Lección 2.2 pasa a las gráficas: gráficas reales de dióxido de carbono, de crecimiento de poblaciones y de solubilidad, y cómo pasar de la tabla a la gráfica y al párrafo. Los números que aquí aprendió a escribir serán los que lea en un eje.") + "</p>"
    glosario = [
        (t("Scientific notation", "Notación científica"), t("A number written as a coefficient (at least 1 and less than 10) times a power of ten.", "Un número escrito como un coeficiente (mayor o igual que 1 y menor que 10) por una potencia de diez.")),
        (t("Coefficient", "Coeficiente"), t("The first piece of a number in scientific notation.", "La primera pieza de un número en notación científica.")),
        (t("Exponent", "Exponente"), t("The small number on the 10. It tells how many places the point moves, and which way.", "El número pequeño sobre el 10. Indica cuántos lugares se mueve el punto, y hacia dónde.")),
        (t("Order of magnitude", "Orden de magnitud"), t("The size of a number given by its power of ten.", "El tamaño de un número dado por su potencia de diez.")),
        (t("Prefix", "Prefijo"), t("A word part that stands for a power of ten: kilo- (10³), milli- (10⁻³), micro- (10⁻⁶), nano- (10⁻⁹).", "Partícula que representa una potencia de diez: kilo- (10³), mili- (10⁻³), micro- (10⁻⁶), nano- (10⁻⁹).")),
        (t("Logarithmic scale", "Escala logarítmica"), t("A scale where each equal step means multiplying by the same number.", "Escala en la que cada paso igual significa multiplicar por el mismo número.")),
    ]
    estd = C.estandares(["SP.6.b", "SP.1.b", "SP.7.b", "SP.3.b"], [], base=["SP.1.c"])
    conexion = "<p>" + t("Topic 1 gave you three tools: rebuild an investigation, audit its design, and read a science text. Topic 2 builds the other support the test needs: numbers. Neither replaces the other: science is read, but it is also measured.", "El Tema 1 dejó tres herramientas: reconstruir una investigación, auditar su diseño y leer un texto científico. El Tema 2 construye el otro andamiaje que exige el examen: el numérico. Ninguno sustituye al otro: la ciencia se lee, pero también se mide.") + "</p><p>" + \
               t("The GED® Science test often shows sizes as small as an atom or as large as the distance between stars. Writing them with all their digits is awkward and leads to mistakes: one extra zero makes you wrong by a factor of ten. <strong>How to study this lesson:</strong> convert by hand first, and then check with the calculator, never the other way around.", "El examen de Ciencias del GED® presenta con frecuencia magnitudes tan pequeñas como un átomo o tan grandes como la distancia entre estrellas. Escribirlas con todas sus cifras es incómodo e induce a error: basta un cero de más para equivocarse por un factor de diez. <strong>Cómo estudiar esta lección:</strong> primero convierta a mano y después compruebe con la calculadora, nunca al revés.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("From the width of an atom to the distance between stars: write it, compare it, and check it.", "Del diámetro de un átomo a la distancia entre estrellas: escribirlo, compararlo y comprobarlo."),
        ["SP.6.b · " + t("Numbers and symbols", "Números y símbolos"), "SP.7.b · " + t("Formulas", "Fórmulas")],
        [t("<strong>Convert</strong> a number from decimal to scientific notation and back.", "<strong>Convertir</strong> un número de notación decimal a científica y al revés."),
         t("<strong>Spot</strong> a number written incorrectly in scientific notation and fix it.", "<strong>Reconocer</strong> un número mal escrito en notación científica y corregirlo."),
         t("<strong>Multiply and divide</strong> in scientific notation, adjusting the coefficient when it goes out of range.", "<strong>Multiplicar y dividir</strong> en notación científica, ajustando el coeficiente cuando se sale del intervalo."),
         t("<strong>Choose</strong> the right unit and prefix for sizes from atoms to stars.", "<strong>Seleccionar</strong> la unidad y el prefijo adecuados para magnitudes de átomos a estrellas."),
         t("<strong>Use</strong> the TI-30XS MultiView™ to check your reasoning, not to replace it.", "<strong>Usar</strong> la TI-30XS MultiView™ para verificar el razonamiento, no para sustituirlo.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("2-2", t("From the table to the graph, and from the graph to the text", "De la tabla a la gráfica y de la gráfica al texto")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- práctica
def objetos():
    return [
        ("1.7", -15, t("The width of a proton", "El diámetro de un protón")), ("1.0", -10, t("The width of a hydrogen atom", "El diámetro de un átomo de hidrógeno")),
        ("2.8", -10, t("The width of a water molecule", "El tamaño de una molécula de agua")), ("2.0", -9, t("The width of a DNA double helix", "El ancho de la doble hélice del ADN")),
        ("1.0", -7, t("The width of a flu virus", "El diámetro de un virus de la gripe")), ("5.5", -7, t("The wavelength of green light", "La longitud de onda de la luz verde")),
        ("2.0", -6, t("The length of an <em>E. coli</em> bacterium", "La longitud de una bacteria <em>E. coli</em>")), ("8.0", -6, t("The width of a red blood cell", "El diámetro de un glóbulo rojo")),
        ("7.0", -5, t("The thickness of a human hair", "El grosor de un cabello humano")), ("5.0", -4, t("The size of a grain of table salt", "El tamaño de un grano de sal")),
        ("4.42", 2, t("The height of the Willis Tower in Chicago", "La altura de la Torre Willis, en Chicago")), ("4.9", 5, t("The length of Lake Michigan", "La longitud del lago Míchigan")),
        ("1.27", 7, t("The diameter of Earth", "El diámetro de la Tierra")), ("1.39", 9, t("The diameter of the Sun", "El diámetro del Sol")),
        ("1.5", 11, t("The distance from Earth to the Sun", "La distancia de la Tierra al Sol")), ("9.0", 12, t("The diameter of Neptune’s orbit", "El diámetro de la órbita de Neptuno")),
        ("4.0", 16, t("The distance to Proxima Centauri, the nearest star", "La distancia a Próxima Centauri, la estrella más cercana")), ("9.5", 20, t("The diameter of the Milky Way", "El diámetro de la Vía Láctea")),
    ]


def banco_unidades():
    d = [
        (t("The width of a cell: 0.00002 m", "El ancho de una célula: 0.00002 m"), 1, t("0.00002 m = 20 × 10⁻⁶ m = 20 µm.", "0.00002 m = 20 × 10⁻⁶ m = 20 µm.")),
        (t("The wavelength of red light: 0.0000007 m", "La longitud de onda de la luz roja: 0.0000007 m"), 0, t("0.0000007 m = 700 × 10⁻⁹ m = 700 nm.", "0.0000007 m = 700 × 10⁻⁹ m = 700 nm.")),
        (t("The distance from Chicago to New York: 1,150,000 m", "La distancia de Chicago a Nueva York: 1,150,000 m"), 3, t("1,150,000 m = 1,150 × 10³ m = 1,150 km.", "1,150,000 m = 1,150 × 10³ m = 1,150 km.")),
        (t("The thickness of a coin: 0.0018 m", "El grosor de una moneda: 0.0018 m"), 2, t("0.0018 m = 1.8 × 10⁻³ m = 1.8 mm.", "0.0018 m = 1.8 × 10⁻³ m = 1.8 mm.")),
        (t("The width of a flu virus: 0.0000001 m", "El diámetro de un virus de la gripe: 0.0000001 m"), 0, t("0.0000001 m = 100 × 10⁻⁹ m = 100 nm.", "0.0000001 m = 100 × 10⁻⁹ m = 100 nm.")),
        (t("A dose of medicine: 0.0005 g", "Una dosis de medicamento: 0.0005 g"), 2, t("0.0005 g = 0.5 × 10⁻³ g = 0.5 mg (or 500 µg).", "0.0005 g = 0.5 × 10⁻³ g = 0.5 mg (o 500 µg).")),
        (t("The thickness of a human hair: 0.00007 m", "El grosor de un cabello: 0.00007 m"), 1, t("0.00007 m = 70 × 10⁻⁶ m = 70 µm.", "0.00007 m = 70 × 10⁻⁶ m = 70 µm.")),
        (t("The length of the Mississippi River: 3,730,000 m", "La longitud del río Misisipi: 3,730,000 m"), 3, t("3,730,000 m = 3,730 km.", "3,730,000 m = 3,730 km.")),
    ]
    ops = [t("nanometers (nm)", "nanómetros (nm)"), t("micrometers (µm)", "micrómetros (µm)"), t("millimeters (mm or mg)", "milímetros (mm o mg)"), t("kilometers (km)", "kilómetros (km)")]
    ops[2] = t("millimeters or milligrams (mm, mg)", "milímetros o miligramos (mm, mg)")
    P = {0: t("nano- is 10⁻⁹: for things smaller than a cell, like light waves and viruses.", "nano- es 10⁻⁹: para cosas más pequeñas que una célula, como las ondas de luz y los virus."),
         1: t("micro- is 10⁻⁶: for cells and hairs.", "micro- es 10⁻⁶: para células y cabellos."),
         2: t("milli- is 10⁻³: for coins, raindrops, and small doses.", "mili- es 10⁻³: para monedas, gotas y dosis pequeñas."),
         3: t("kilo- is 10³: for distances on a map.", "kilo- es 10³: para distancias de un mapa.")}
    return [{"enun": t("Which prefix makes this number easiest to read?", "¿Qué prefijo hace más cómodo este número?") + "<br><strong>" + x + "</strong>", "ops": ops, "ok": k, "enOrden": True,
             "pistas": {i: P[i] for i in range(4) if i != k}, "exp": e} for x, k, e in d]


def banco_clinica():
    return [
        {"t": t("How many hydrogen atoms, each 1 × 10⁻¹⁰ m wide, fit in a row along 1 mm (1 × 10⁻³ m)?", "¿Cuántos átomos de hidrógeno, de 1 × 10⁻¹⁰ m de diámetro, caben alineados en 1 mm (1 × 10⁻³ m)?"), "c": "1", "e": 7,
         "mano": t("Coefficients: 1 ÷ 1 = 1. Exponents: −3 − (−10) = 7. Subtracting a negative exponent adds it.", "Coeficientes: 1 ÷ 1 = 1. Exponentes: −3 − (−10) = 7. Restar un exponente negativo lo suma."),
         "teclas": t("Keys: 1, ×10ⁿ, (−), 3, ÷, 1, ×10ⁿ, (−), 10, enter.", "Teclas: 1, ×10ⁿ, (−), 3, ÷, 1, ×10ⁿ, (−), 10, enter.")},
        {"t": t("Light travels 3 × 10⁸ m every second. How far does it travel in one minute (60 s)?", "La luz recorre 3 × 10⁸ m cada segundo. ¿Qué distancia recorre en un minuto (60 s)?"), "c": "1.8", "e": 10,
         "mano": t("60 is 6 × 10¹. Coefficients: 3 × 6 = 18. Exponents: 8 + 1 = 9. 18 × 10⁹ must be adjusted to 1.8 × 10¹⁰.", "60 es 6 × 10¹. Coeficientes: 3 × 6 = 18. Exponentes: 8 + 1 = 9. 18 × 10⁹ se ajusta a 1.8 × 10¹⁰."),
         "teclas": t("Keys: 3, ×10ⁿ, 8, ×, 60, enter. The screen may show 1.8E10 or 18000000000: same number.", "Teclas: 3, ×10ⁿ, 8, ×, 60, enter. La pantalla puede mostrar 1.8E10 o 18000000000: es el mismo número.")},
        {"t": t("Proxima Centauri is 3.9 × 10¹⁶ m away. If light travels 3 × 10⁸ m each second, how many seconds does its light take to reach us?", "Próxima Centauri está a 3.9 × 10¹⁶ m. Si la luz recorre 3 × 10⁸ m cada segundo, ¿cuántos segundos tarda su luz en llegar?"), "c": "1.3", "e": 8,
         "mano": t("Coefficients: 3.9 ÷ 3 = 1.3. Exponents: 16 − 8 = 8. About 130 million seconds: a little over four years.", "Coeficientes: 3.9 ÷ 3 = 1.3. Exponentes: 16 − 8 = 8. Unos 130 millones de segundos: algo más de cuatro años."),
         "teclas": t("Keys: 3.9, ×10ⁿ, 16, ÷, 3, ×10ⁿ, 8, enter. If you get something near 10⁻⁸, you divided the wrong way.", "Teclas: 3.9, ×10ⁿ, 16, ÷, 3, ×10ⁿ, 8, enter. Si sale algo cerca de 10⁻⁸, dividió al revés.")},
        {"t": t("A red blood cell is 8 × 10⁻⁶ m wide. How many, in a row, would cover 1 cm (1 × 10⁻² m)?", "Un glóbulo rojo mide 8 × 10⁻⁶ m. ¿Cuántos harían falta, alineados, para cubrir 1 cm (1 × 10⁻² m)?"), "c": "1.25", "e": 3,
         "mano": t("Coefficients: 1 ÷ 8 = 0.125. Exponents: −2 − (−6) = 4. 0.125 × 10⁴ is below 1, so adjust: 1.25 × 10³.", "Coeficientes: 1 ÷ 8 = 0.125. Exponentes: −2 − (−6) = 4. 0.125 × 10⁴ queda por debajo de 1: se ajusta a 1.25 × 10³."),
         "teclas": t("Keys: 1, ×10ⁿ, (−), 2, ÷, 8, ×10ⁿ, (−), 6, enter. The screen shows 1250.", "Teclas: 1, ×10ⁿ, (−), 2, ÷, 8, ×10ⁿ, (−), 6, enter. La pantalla muestra 1250.")},
        {"t": t("A cube-shaped cell has edges of 2 × 10⁻⁵ m. What is its volume (edge³)?", "Una célula cúbica tiene 2 × 10⁻⁵ m de arista. ¿Cuál es su volumen (arista³)?"), "c": "8", "e": -15,
         "mano": t("Cube the coefficient: 2³ = 8. Multiply the exponent by 3: −5 × 3 = −15. The answer is in cubic meters.", "El coeficiente se eleva al cubo: 2³ = 8. El exponente se multiplica por 3: −5 × 3 = −15. El resultado va en metros cúbicos."),
         "teclas": t("Keys: 2, ×10ⁿ, (−), 5, ^, 3, enter.", "Teclas: 2, ×10ⁿ, (−), 5, ^, 3, enter.")},
    ]


def banco_averias():
    d = [
        (t("To find (5 × 10⁻⁴) × 2, a student types 5, the <strong>subtraction</strong> key, 4, × 2. What does the screen show, and why is it wrong?", "Para calcular (5 × 10⁻⁴) × 2, un estudiante teclea 5, la tecla de <strong>restar</strong>, 4, por 2. ¿Qué muestra la pantalla y por qué está mal?"),
         [t("−3, because it read “5 minus 4 times 2” and followed the order of operations", "−3, porque leyó «5 menos 4 por 2» y respetó la jerarquía de operaciones"), t("1 × 10⁻³, the right answer", "1 × 10⁻³, el resultado correcto"), t("A syntax error message", "Un mensaje de error de sintaxis"), t("0.001, because it fixes the mistake by itself", "0.001, porque corrige el error automáticamente")], 0,
         t("The subtraction key and the sign key are different. The calculator read “5 − 4 × 2,” did the multiplication first, and gave −3: perfectly calculated and unrelated to the problem. No error message appears, and that is the trap. If you estimated about 10⁻³ first, a negative answer tells you right away that something was typed wrong.", "La tecla de restar y la de signo son distintas. La calculadora leyó «5 − 4 × 2», resolvió primero la multiplicación y devolvió −3: impecable y sin relación con el problema. No aparece ningún error, y esa es la trampa. Quien estimó antes unos 10⁻³ ve enseguida que un resultado negativo delata un error de tecleo.")),
        (t("The screen shows 6.02E23. The test asks you to write the answer. What do you write?", "La pantalla muestra 6.02E23. El examen pide escribir la respuesta. ¿Qué se escribe?"),
         ["6.02E23", "6.02 × 10²³", "602 × 10²¹", t("6.02 to the 23rd power", "6.02 elevado a 23")], 1,
         t("The E is the calculator’s shortcut for “times ten to the power of.” It is screen notation, not written scientific notation. 602 × 10²¹ has the same value, but its coefficient is not between 1 and 10.", "La E es la abreviatura de la máquina para «por diez elevado a». Es notación de pantalla, no notación científica escrita. 602 × 10²¹ vale lo mismo, pero su coeficiente no está entre 1 y 10.")),
        (t("A student left the calculator in SCI mode. In the next lesson, 10 ÷ 4 gives 2.5E0 instead of 2.5. What happened?", "Un estudiante dejó la calculadora en modo SCI. En la lección siguiente, 10 ÷ 4 da 2.5E0 en lugar de 2.5. ¿Qué ocurrió?"),
         [t("The calculator is broken", "La calculadora se estropeó"), t("The answer is wrong and must be redone", "El resultado es incorrecto y hay que repetirlo"), t("It is the same number: SCI mode shows everything in scientific notation, and 2.5E0 is 2.5 × 10⁰", "Es el mismo número: el modo SCI lo muestra todo en notación científica, y 2.5E0 es 2.5 × 10⁰"), t("You need to press enter again", "Falta pulsar enter otra vez")], 2,
         t("10⁰ = 1, so 2.5 × 10⁰ is exactly 2.5. The answer was right; only the format is confusing. That is why you go back to NORM when you finish.", "10⁰ = 1, así que 2.5 × 10⁰ es exactamente 2.5. El resultado era correcto; lo que confunde es el formato. Por eso conviene volver a NORM al terminar.")),
        (t("For (4 × 10⁶) ÷ (2 × 10²), a student’s screen shows 2E8. She had estimated 2 × 10⁴ by hand. What should she do?", "Al calcular (4 × 10⁶) ÷ (2 × 10²), la pantalla de una estudiante muestra 2E8. Ella había estimado 2 × 10⁴. ¿Qué conviene hacer?"),
         [t("Trust the screen: the calculator never makes math mistakes", "Aceptar la pantalla: la calculadora no se equivoca"), t("Trust the estimate: 6 − 2 = 4, so she probably typed × instead of ÷", "Aceptar la estimación: 6 − 2 = 4, así que probablemente tecleó × en lugar de ÷"), t("Redo the estimate, because it must be wrong", "Repetir la estimación, porque seguro que está mal"), t("Switch to ENG mode and try again", "Cambiar a modo ENG e intentarlo de nuevo")], 1,
         t("The calculator only answers what was typed. An exponent of 8 instead of 4 is the sign of adding exponents, that is, of multiplying. The estimate caught the typing mistake: that is what it is for.", "La máquina solo responde a lo que se tecleó. Un exponente 8 en vez de 4 es la firma de una suma de exponentes, es decir, de una multiplicación. La estimación detectó el error: para eso sirve.")),
        (t("Which statement about the calculator on the GED® Science test is correct?", "¿Qué afirmación sobre la calculadora en el examen de Ciencias del GED® es correcta?"),
         [t("Type everything, because the calculator is never wrong", "Conviene teclearlo todo, porque la máquina no se equivoca"), t("The calculator warns you when your setup is wrong", "La calculadora avisa cuando el planteamiento es incorrecto"), t("The calculator checks reasoning you already did, but it does not replace it or catch setup errors", "La calculadora verifica un razonamiento ya hecho, pero no lo sustituye ni detecta errores de planteamiento"), t("No calculator is allowed on the Science test", "En el examen de Ciencias no se permite calculadora")], 2,
         t("The TI-30XS is allowed and calculates without error. What it cannot do is choose the operation or warn about a wrong sign. Always estimate first and check after.", "La TI-30XS está permitida y calcula sin error. Lo que no puede es decidir la operación ni avisar de un signo mal puesto. Siempre se estima primero y se comprueba después.")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Think about what the calculator actually received from the keys.", "Piense en qué recibió realmente la calculadora con esas teclas."), "exp": e} for q, o, k, e in d]


def js_practica():
    if C.L == "en":
        txt = """
function gA(){ var o = sacaA(), n = sci(o[0], o[1]), k = o[1];
  return {enun: "<p>" + o[2] + ": <strong>" + conComas(n) + " m</strong>.</p><p>Write this length in scientific notation.</p>", resp: n,
    explica: k > 0 ? "Large number: the point moves " + k + " places to the left, so the exponent is positive." : "Small number: the point moves " + (-k) + " places to the right, so the exponent is negative.",
    diagnostico: function(v, cc, kk){ return (igual(cc, leeNumero(aSci(n).c)) && kk === -k) ? "The coefficient is right, but the sign of the exponent is backward." : null; }}; }
function gB(){ var o = sacaB(), n = sci(o[0], o[1]);
  return {enun: "<p>" + o[2] + ": <strong>" + sciHTML(o[0], o[1]) + " m</strong>.</p><p>Write this length as a decimal number.</p>", resp: n,
    explica: "The answer is " + conComas(n) + " m. " + (o[1] > 0 ? "A positive exponent: the point moves " + o[1] + " places to the right." : "A negative exponent: the point moves " + (-o[1]) + " places to the left.")}; }
var PARES = [[8,2],[9,3],[6,2],[6,3],[8,4],[2,8],[3,6],[4,8],[3,4],[1.5,3],[7,2],[9,4.5]];
function gC(){
  var mulOp = Math.random() < 0.5, a, b, m = aleatorio(-9, 9), k = aleatorio(-9, 9);
  if (mulOp){ a = String(aleatorio(2, 9)); b = String(elige(["2", "3", "4", "5", "1.5", "2.5"])); }
  else { var p = elige(PARES); a = String(p[0]); b = String(p[1]); }
  var A = sci(a, m), B = sci(b, k), r = mulOp ? mul(A, B) : divide(A, B).n, s = aSci(r);
  var c0 = mulOp ? mul(leeNumero(a), leeNumero(b)) : divide(leeNumero(a), leeNumero(b)).n, e0 = mulOp ? m + k : m - k, aj = !esValida(plano(c0));
  return {enun: "<p>" + T("Find", "") + " (" + sciHTML(a, m) + ") " + (mulOp ? "×" : "÷") + " (" + sciHTML(b, k) + "). Write the answer in scientific notation.</p>", resp: r,
    explica: (mulOp ? "Multiply the coefficients (" + a + " × " + b + " = " + plano(c0) + ") and add the exponents (" + expTexto(m) + " + " + par(k) + " = " + expTexto(e0) + ")." : "Divide the coefficients (" + a + " ÷ " + b + " = " + plano(c0) + ") and subtract the exponents (" + expTexto(m) + " − " + par(k) + " = " + expTexto(e0) + ").") + (aj ? " Then adjust: " + plano(c0) + " is not between 1 and 10, so the answer is " + sciTexto(s.c, s.e) + "." : "")}; }
function gE(){ var o = sacaE(); return {enun: "<p>" + o.t + "</p><p><strong>Estimate by hand first.</strong> Then check with the calculator and write the answer in scientific notation.</p>", resp: sci(o.c, o.e), explica: o.mano + " " + o.teclas}; }
"""
    else:
        txt = """
function gA(){ var o = sacaA(), n = sci(o[0], o[1]), k = o[1];
  return {enun: "<p>" + o[2] + ": <strong>" + conComas(n) + " m</strong>.</p><p>Escriba esta longitud en notación científica.</p>", resp: n,
    explica: k > 0 ? "Número grande: el punto se mueve " + k + " lugares a la izquierda, así que el exponente es positivo." : "Número pequeño: el punto se mueve " + (-k) + " lugares a la derecha, así que el exponente es negativo.",
    diagnostico: function(v, cc, kk){ return (igual(cc, leeNumero(aSci(n).c)) && kk === -k) ? "El coeficiente está bien, pero el signo del exponente está al revés." : null; }}; }
function gB(){ var o = sacaB(), n = sci(o[0], o[1]);
  return {enun: "<p>" + o[2] + ": <strong>" + sciHTML(o[0], o[1]) + " m</strong>.</p><p>Escriba esta longitud como número decimal.</p>", resp: n,
    explica: "La respuesta es " + conComas(n) + " m. " + (o[1] > 0 ? "Exponente positivo: el punto se mueve " + o[1] + " lugares a la derecha." : "Exponente negativo: el punto se mueve " + (-o[1]) + " lugares a la izquierda.")}; }
var PARES = [[8,2],[9,3],[6,2],[6,3],[8,4],[2,8],[3,6],[4,8],[3,4],[1.5,3],[7,2],[9,4.5]];
function gC(){
  var mulOp = Math.random() < 0.5, a, b, m = aleatorio(-9, 9), k = aleatorio(-9, 9);
  if (mulOp){ a = String(aleatorio(2, 9)); b = String(elige(["2", "3", "4", "5", "1.5", "2.5"])); }
  else { var p = elige(PARES); a = String(p[0]); b = String(p[1]); }
  var A = sci(a, m), B = sci(b, k), r = mulOp ? mul(A, B) : divide(A, B).n, s = aSci(r);
  var c0 = mulOp ? mul(leeNumero(a), leeNumero(b)) : divide(leeNumero(a), leeNumero(b)).n, e0 = mulOp ? m + k : m - k, aj = !esValida(plano(c0));
  return {enun: "<p>Calcule (" + sciHTML(a, m) + ") " + (mulOp ? "×" : "÷") + " (" + sciHTML(b, k) + "). Escriba el resultado en notación científica.</p>", resp: r,
    explica: (mulOp ? "Se multiplican los coeficientes (" + a + " × " + b + " = " + plano(c0) + ") y se suman los exponentes (" + expTexto(m) + " + " + par(k) + " = " + expTexto(e0) + ")." : "Se dividen los coeficientes (" + a + " ÷ " + b + " = " + plano(c0) + ") y se restan los exponentes (" + expTexto(m) + " − " + par(k) + " = " + expTexto(e0) + ").") + (aj ? " Después se ajusta: " + plano(c0) + " no está entre 1 y 10, así que el resultado es " + sciTexto(s.c, s.e) + "." : "")}; }
function gE(){ var o = sacaE(); return {enun: "<p>" + o.t + "</p><p><strong>Estime primero a mano.</strong> Después compruebe con la calculadora y escriba el resultado en notación científica.</p>", resp: sci(o.c, o.e), explica: o.mano + " " + o.teclas}; }
"""
    txt = txt.replace('T("Find", "") + " (', '"Find (')
    return txt


def practica():
    A = {"en": ["write-sci", "to-decimal", "multiply", "units", "clinic", "broken"], "es": ["escribir", "a-decimal", "operar", "unidades", "clinica", "averias"]}[C.L]
    mods = [
        (A[0], t("Write real sizes in scientific notation", "Escriba tamaños reales en notación científica"),
         "      <p>" + t("From a proton to the Milky Way. Before you type, decide: is the number smaller than 1 (negative exponent) or larger than 10 (positive exponent)?", "Del protón a la Vía Láctea. Antes de escribir, decida: ¿el número es menor que 1 (exponente negativo) o mayor que 10 (exponente positivo)?") + "</p>\n" + C.sci_campos("m1")),
        (A[1], t("From scientific notation to decimal", "De notación científica a decimal"),
         "      <p>" + t("Move the point as many places as the exponent says. Use commas for thousands if you like: 1,270,000.", "Mueva el punto tantos lugares como indique el exponente. Puede separar los miles con comas: 1,270,000.") + "</p>\n" + C.dec_campo("m2", t("Number as a decimal", "Número en notación decimal"))),
        (A[2], t("Multiply and divide", "Multiplique y divida"),
         "      <p>" + t("Coefficients: multiply or divide. Exponents: add or subtract. Then check the coefficient rule (1 ≤ a &lt; 10) and adjust if needed.", "Coeficientes: se multiplican o se dividen. Exponentes: se suman o se restan. Después compruebe la regla del coeficiente (1 ≤ a &lt; 10) y ajuste si hace falta.") + "</p>\n" + C.sci_campos("m3")),
        (A[3], t("Choose the unit", "Elija la unidad"), C.om("m4", t("Choose the prefix that leaves a number that is easy to read.", "Elija el prefijo que deja un número cómodo de leer."))),
        (A[4], t("The TI-30XS clinic: estimate, then check", "La clínica de la TI-30XS: estime y compruebe"),
         "      <p>" + t("Work it out by hand first. Then open the calculator, type it, and compare. Write the answer in scientific notation.", "Resuélvalo primero a mano. Después abra la calculadora, tecléelo y compare. Escriba el resultado en notación científica.") + "</p>\n"
         + f'      <p><button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> {t("Open the calculator", "Abrir la calculadora")}</button></p>\n' + C.sci_campos("m5")),
        (A[5], t("Broken screens: what went wrong?", "Averías: ¿qué salió mal?"), C.om("m6", t("The calculator never makes math mistakes, but it calculates exactly what you typed.", "La calculadora nunca se equivoca en aritmética, pero calcula exactamente lo que se tecleó."))),
    ]
    obj = [[c, e, n] for c, e, n in objetos()]
    js = (C.js_datos("OBJ", obj) + C.js_datos("UNI", banco_unidades()) + C.js_datos("CLI", banco_clinica()) + C.js_datos("AVE", banco_averias()) +
          "var sacaA = mazo(OBJ), sacaB = mazo(OBJ), sacaE = mazo(CLI);\n" + js_practica() +
          'creaPracticaSci("m1", gA);\ncreaPracticaDec("m2", gB);\ncreaPracticaSci("m3", gC);\ncreaBanco("m4", UNI);\ncreaPracticaSci("m5", gE);\ncreaBanco("m6", AVE);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one · calculator included", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
