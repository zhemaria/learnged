"""Level 2 · Lesson 6.3 · Converting between U.S. customary and metric units — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg

B.NIVEL = 2
N = "6-3"
TEMA = ("Money math and unit conversions", "Matemáticas financieras y conversiones de medidas")
TIT = ("Converting between U.S. customary and metric units", "Conversiones entre el sistema inglés y el métrico")

def ej(titulo, enunciado, pasos):
    return ejemplo(titulo + f'<span style="display:block;font-weight:400;margin-top:6px">{enunciado}</span>', pasos)

def big(x):
    return f'<p style="text-align:center;font-size:1.4rem;font-weight:700;color:#0d47a1">{x}</p>'

def fr(arriba, abajo, voz):
    return (f'<span aria-hidden="true" style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.2;margin:0 4px">'
            f'<span style="display:block;border-bottom:2px solid currentColor;padding:0 4px">{arriba}</span><span style="display:block;padding:0 4px">{abajo}</span></span>'
            f'<span class="cap-oculto">{voz}</span>')

def leccion():
    n = N
    s1 = f'''<p>{t("In Topic 4 you worked with ratios and proportions; in Lessons 6.1 and 6.2, with amounts that change at a fixed rate. Converting units is one more kind of proportional reasoning: you multiply a measurement by a ratio of equal amounts, the <strong>conversion factor</strong>.", "En el Tema 4 se trabajó con razones y proporciones; en las Lecciones 6.1 y 6.2, con cantidades que cambian en una proporción fija. Convertir unidades es otra forma de razonamiento proporcional: una medida se multiplica por una razón de equivalencia, el <strong>factor de conversión</strong>.")}</p>
<p>{t("At the doctor's office, the nurse wrote down Mrs. Morales's weight: <strong>165 pounds</strong>. But the pharmacy form asks for the weight in <strong>kilograms</strong>. How do you convert it?", "En la consulta, el médico anotó el peso de la señora Morales: <strong>165 libras</strong>. Pero el formulario de la farmacia pide el peso en <strong>kilogramos</strong>. ¿Cómo se convierte?")}</p>
<p>{t("The United States uses the <strong>U.S. customary system</strong>: inches, feet, miles, pounds, gallons. Almost all the rest of the world, including Mexico and the rest of Latin America, uses the <strong>metric system</strong>: centimeters, meters, kilometers, grams, liters. Medicine, science, and many products use metric units even in the U.S., so you need to go from one system to the other.", "En Estados Unidos se usa el <strong>sistema inglés</strong> (llamado oficialmente <em>U.S. customary system</em>): pulgadas, pies, millas, libras, galones. En casi todo el resto del mundo, incluidos México y los demás países de América Latina, se usa el <strong>sistema métrico</strong>: centímetros, metros, kilómetros, gramos, litros. Quien vive entre los dos mundos necesita pasar de uno a otro.")}</p>
{ej(t("Example: the weight for the pharmacy", "Ejemplo: el peso para la farmacia"), t("Convert 165 lb to kilograms. Use 1 lb ≈ 454 g and 1 kg = 1,000 g.", "Convierta 165 lb a kilogramos, sabiendo que 1 lb ≈ 454 g y que 1 kg = 1,000 g."),
  [("1", t("Pounds to grams.", "De libras a gramos."), "165 × 454 = 74,910 g."),
   ("2", t("Grams to kilograms.", "De gramos a kilogramos."), "74,910 ÷ 1,000 = 74.91 kg."),
   ("3", t("Check with the rule of thumb.", "Compruebe con la regla práctica."), t("“1 kg is a little more than 2 lb”: 165 ÷ 2.2 = 75. ✓", "«1 kg es un poco más de 2 lb»: 165 ÷ 2.2 = 75. ✓")),
   ("✓", t("Answer.", "Respuesta."), t("Mrs. Morales weighs about <strong>74.9 kg</strong>.", "La señora Morales pesa unos <strong>74.9 kg</strong>."))])}
{practica("p1", t("Practice 1 — Weight", "Práctica 1 — El peso"), t("A patient weighs 150 lb. About how many kilograms is that? (1 lb ≈ 454 g)", "Un paciente pesa 150 lb. ¿Cuántos kilogramos son, aproximadamente? (1 lb ≈ 454 g)"),
          [("a", "330 kg"), ("b", "15 kg"), ("c", "68.1 kg"), ("d", "68,100 kg")])}
{enlace(n, t("doctors-office", "consultorio"), t("at the doctor's office and the pharmacy", "en el consultorio y en la farmacia"), t("Convert a weight from pounds to kilograms and check it with the rule of thumb.", "Convierta el peso de libras a kilogramos y compruebe con la regla práctica."))}'''

    s2 = f'''{tabla(t("Between the two systems", "Entre los dos sistemas"), t("Conversion factors between the U.S. customary and metric systems", "Factores de conversión entre el sistema inglés y el métrico"),
       [t("Quantity", "Magnitud"), t("Equivalence", "Equivalencia")],
       [[t("Length", "Longitud"), "1 in = 2.54 cm"], [t("Length", "Longitud"), "1 mi ≈ 1.609 km"], [t("Weight", "Peso"), "1 lb ≈ 454 g"], [t("Capacity", "Capacidad"), "1 gal ≈ 3.785 L"]])}
{tabla(t("Within each system", "Dentro de cada sistema"), t("Equivalences within each system", "Equivalencias dentro de cada sistema"),
       [t("U.S. customary", "Sistema inglés"), t("Metric", "Sistema métrico")],
       [["1 ft = 12 in", "1 m = 100 cm"], ["1 yd = 3 ft", "1 km = 1,000 m"], ["1 mi = 5,280 ft", "1 kg = 1,000 g"], ["1 lb = 16 oz · 1 gal = 4 qt", "1 L = 1,000 mL"]])}
{tabla(t("Unit names in both languages", "Las unidades en los dos idiomas"), t("Names of the units in English and in Spanish", "Nombres de las unidades en inglés y en español"),
       [t("English (abbreviation)", "Español (abreviatura)"), t("Spanish", "Inglés")],
       [[t("inch (in) · foot (ft) · yard (yd) · mile (mi)", "pulgada (in) · pie (ft) · yarda (yd) · milla (mi)"), t("pulgada · pie · yarda · milla", "inch · foot · yard · mile")],
        [t("pound (lb) · ounce (oz)", "libra (lb) · onza (oz)"), t("libra · onza", "pound · ounce")],
        [t("gallon (gal) · quart (qt)", "galón (gal) · cuarto (qt)"), t("galón · cuarto", "gallon · quart")],
        [t("conversion factor", "factor de conversión"), t("factor de conversión", "conversion factor")]])}
{caja("tip", t("Rules of thumb for estimating", "Reglas prácticas para estimar"), t("<p>A meter is a little more than a yard · a kilogram is a little more than 2 pounds · a liter is a little more than a quart · a kilometer is a little more than half a mile (about 0.6 mi). Use them to check whether a result makes sense.</p>", "<p>Un metro es un poco más que una yarda · un kilogramo es un poco más de 2 libras · un litro es un poco más que un cuarto de galón · un kilómetro es un poco más de media milla (unas 0.6 mi). Sirven para comprobar si un resultado tiene sentido.</p>"))}
{practica("p2", t("Practice 2 — Estimate", "Práctica 2 — Estime"), t("What is the most reasonable estimate for 10 kg?", "¿Cuál es la estimación más razonable para 10 kg?"),
          [("a", t("About 5 lb", "Unas 5 lb")), ("b", t("About 22 lb", "Unas 22 lb")), ("c", t("About 100 lb", "Unas 100 lb")), ("d", t("About 4.5 lb", "Unas 4.5 lb"))])}
{practica("p3", t("Practice 3 — A soda bottle", "Práctica 3 — Una botella de refresco"), t("A 2-liter soda bottle holds…", "Una botella de refresco de 2 L contiene…"),
          [("a", t("a little more than half a gallon.", "un poco más de medio galón.")), ("b", t("more than a gallon.", "más de un galón.")), ("c", t("one quart.", "un cuarto de galón.")), ("d", t("about 2 gallons.", "unos 2 galones."))])}
{enlace(n, t("factors", "factores"), t("the table of conversion factors", "la tabla de factores de conversión"), t("Practice the factors between the two systems and within each one, and decide whether a result makes sense.", "Practique los factores entre los dos sistemas y dentro de cada uno, y decida si un resultado tiene sentido."))}'''

    f1 = fr("2.54 cm", "1 in", t("2.54 centimeters over 1 inch", "2.54 centímetros sobre 1 pulgada"))
    f2 = fr("1 in", "2.54 cm", t("1 inch over 2.54 centimeters", "1 pulgada sobre 2.54 centímetros"))
    s3 = f'''<p>{t("Since 1 in and 2.54 cm are <strong>the same length</strong>, each of these fractions is exactly equal to 1:", "Como 1 in y 2.54 cm son <strong>la misma longitud</strong>, cada una de estas fracciones vale exactamente 1:")}</p>
<p style="text-align:center;font-size:1.25rem">{f1} {t("to go from inches to centimeters", "para pasar de pulgadas a centímetros")} &nbsp;&nbsp;·&nbsp;&nbsp; {f2} {t("to go from centimeters to inches", "para pasar de centímetros a pulgadas")}</p>
<p>{t("Multiplying by 1 does not change the amount, only the unit it is written in. The key is to choose the right fraction.", "Multiplicar por 1 no cambia la cantidad, solo la unidad en que se expresa. La clave está en elegir la fracción correcta.")}</p>
{caja("tip", t("Golden rule", "Regla de oro"), t("<p>The unit you want to get rid of goes on the <strong>bottom</strong> of the fraction. That way it cancels with the unit on top, and the unit you want is left.</p>", "<p>La unidad que se quiere eliminar va <strong>abajo</strong> en la fracción. Así se cancela con la unidad de arriba, y queda la unidad que se busca.</p>"))}
{ej(t("Example: inches to centimeters", "Ejemplo: de pulgadas a centímetros"), t("A school ruler is 12 in long. How many centimeters is that?", "Una regla escolar mide 12 in. ¿Cuántos centímetros son?"),
  [("1", t("Get rid of “in”: it goes on the bottom.", "Se quiere eliminar «in»: va abajo."), "12 in × (2.54 cm / 1 in)."),
   ("2", t("The inches cancel.", "Se cancelan las pulgadas."), "12 × 2.54 = 30.48 cm."),
   ("✓", t("Answer.", "Respuesta."), "<strong>30.48 cm</strong>")])}
{ej(t("Example: kilometers to miles", "Ejemplo: de kilómetros a millas"), t("How many miles long is a 10 km race?", "Una carrera de 10 km, ¿cuántas millas mide?"),
  [("1", t("Get rid of “km”: it goes on the bottom.", "Se quiere eliminar «km»: va abajo."), "10 km × (1 mi / 1.609 km)."),
   ("2", t("Divide.", "Divida."), "10 ÷ 1.609 ≈ 6.2 mi."),
   ("3", t("Check.", "Compruebe."), t("1 km ≈ 0.6 mi, so 10 km ≈ 6 mi. ✓", "1 km ≈ 0.6 mi, así que 10 km ≈ 6 mi. ✓")),
   ("✓", t("Answer.", "Respuesta."), t("About <strong>6.2 miles</strong>.", "Unas <strong>6.2 millas</strong>."))])}
{ej(t("Example: gallons to liters", "Ejemplo: de galones a litros"), t("How many liters does a 3-gallon water jug hold?", "Un garrafón de agua de 3 gal, ¿cuántos litros contiene?"),
  [("1", t("Get rid of “gal”.", "Se elimina «gal»."), "3 gal × (3.785 L / 1 gal) = 11.355 L."),
   ("✓", t("Answer.", "Respuesta."), t("About <strong>11.4 L</strong>.", "Unos <strong>11.4 L</strong>."))])}
<h3>{t("Conversions with several steps", "Conversiones de varios pasos")}</h3>
<p>{t("When there is no direct factor, chain fractions together. Each one cancels one unit, until you reach the unit you want.", "Cuando no hay un factor directo, se encadenan fracciones. Cada una cancela una unidad, hasta llegar a la que se busca.")}</p>
{ej(t("Example: feet to meters", "Ejemplo: de pies a metros"), t("A person is 6 ft tall. How many meters is that?", "Una persona mide 6 ft. ¿Cuántos metros son?"),
  [("1", t("Path.", "Camino."), t("feet → inches → centimeters → meters.", "pies → pulgadas → centímetros → metros.")),
   ("2", t("Chain.", "Cadena."), "6 ft × (12 in / 1 ft) × (2.54 cm / 1 in) × (1 m / 100 cm)."),
   ("3", t("Step by step.", "Paso a paso."), "6 × 12 = 72 in; 72 × 2.54 = 182.88 cm; 182.88 ÷ 100 = 1.8288 m."),
   ("✓", t("Answer.", "Respuesta."), t("About <strong>1.83 m</strong>.", "Unos <strong>1.83 m</strong>."))])}
{ej(t("Example: miles to meters", "Ejemplo: de millas a metros"), t("How many meters are in 2 miles?", "¿Cuántos metros hay en 2 millas?"),
  [("1", t("First step.", "Primer paso."), "2 mi × (1.609 km / 1 mi) = 3.218 km."),
   ("2", t("Second step.", "Segundo paso."), "3.218 km × (1,000 m / 1 km) = 3,218 m."),
   ("✓", t("Answer.", "Respuesta."), "<strong>3,218 m</strong>")])}
{caja("ojo", t("Common mistake", "Error frecuente"), t("<p>Using the fraction upside down. Changing 10 km to miles by multiplying by 1.609 gives 16.09 “miles”: a bigger number, even though miles are longer than kilometers. If the new unit is bigger, the number must come out smaller.</p>", "<p>Poner la fracción al revés. Convertir 10 km a millas multiplicando por 1.609 da 16.09 «millas», un número mayor, cuando las millas son más largas que los kilómetros. Si la unidad nueva es más grande, el número debe salir más pequeño.</p>"))}
{practica("p4", t("Practice 4 — Length", "Práctica 4 — Longitud"), "20 in = ? cm", [("a", "50.8 cm"), ("b", "7.87 cm"), ("c", "22.54 cm"), ("d", "508 cm")])}
{practica("p5", t("Practice 5 — Distance", "Práctica 5 — Distancia"), t("5 mi = ? km (round to the hundredth)", "5 mi = ? km (redondee a la centésima)"), [("a", "3.11 km"), ("b", "6.61 km"), ("c", "8,045 km"), ("d", "8.05 km")])}
{practica("p6", t("Practice 6 — Capacity", "Práctica 6 — Capacidad"), t("4 gal = ? L (round to the hundredth)", "4 gal = ? L (redondee a la centésima)"), [("a", "1.06 L"), ("b", "15.14 L"), ("c", "7.79 L"), ("d", "16 L")])}
{practica("p7", t("Practice 7 — Two steps", "Práctica 7 — Dos pasos"), t("10 ft = ? m (round to the hundredth)", "10 ft = ? m (redondee a la centésima)"), [("a", "25.4 m"), ("b", "3.94 m"), ("c", "3.05 m"), ("d", "304.8 m")])}
{practica("p8", t("Practice 8 — Choose the fraction", "Práctica 8 — Elija la fracción"), t("To change 50 km to miles, what fraction do you multiply by?", "Para convertir 50 km a millas, ¿por qué fracción se multiplica?"),
          [("a", fr("1.609 km", "1 mi", t("1.609 kilometers over 1 mile", "1.609 kilómetros sobre 1 milla"))), ("b", fr("1 km", "1.609 mi", t("1 kilometer over 1.609 miles", "1 kilómetro sobre 1.609 millas"))),
           ("c", fr("1.609 mi", "1 km", t("1.609 miles over 1 kilometer", "1.609 millas sobre 1 kilómetro"))), ("d", fr("1 mi", "1.609 km", t("1 mile over 1.609 kilometers", "1 milla sobre 1.609 kilómetros")))])}
{enlace(n, t("conversion-fraction", "fraccion-conversion"), t("the conversion-fraction method", "el método de la fracción de conversión"), t("Build the chain of fractions and cancel units, also in several steps.", "Arme la cadena de fracciones y cancele unidades, también en varios pasos."))}'''

    s4 = f'''<p>{t("Temperature is not converted with a single factor, because the two scales do not start at the same zero: water freezes at 0 °C, which is 32 °F. So first you subtract 32 (inside the parentheses, as in PEMDAS from Topic 3), and then you multiply.", "La temperatura no se convierte con un solo factor, porque los dos sistemas no empiezan en el mismo cero: el agua se congela a 0 °C, que equivalen a 32 °F. Por eso primero se resta 32 (dentro del paréntesis, como en PEMDAS del Tema 3) y después se multiplica.")}</p>
{big("°C = (°F − 32) × 5 ÷ 9")}
<p style="text-align:center">{t("From Fahrenheit to Celsius", "De Fahrenheit a Celsius")}</p>
{big("°F = °C × 9 ÷ 5 + 32")}
<p style="text-align:center">{t("From Celsius to Fahrenheit", "De Celsius a Fahrenheit")}</p>
{ej(t("Example: body temperature", "Ejemplo: la temperatura del cuerpo"), t("The thermometer reads 98.6 °F. How many degrees Celsius is that?", "El termómetro marca 98.6 °F. ¿Cuántos grados Celsius son?"),
  [("1", t("Parentheses.", "Paréntesis."), "98.6 − 32 = 66.6."),
   ("2", t("Multiply and divide.", "Multiplique y divida."), "66.6 × 5 ÷ 9 = 333 ÷ 9 = 37."),
   ("✓", t("Answer.", "Respuesta."), t("<strong>37 °C</strong>, normal body temperature.", "<strong>37 °C</strong>, la temperatura normal del cuerpo."))])}
{ej(t("Example: a pleasant day", "Ejemplo: un día agradable"), t("The forecast says 20 °C. How many degrees Fahrenheit is that?", "El pronóstico anuncia 20 °C. ¿Cuántos grados Fahrenheit son?"),
  [("1", t("Multiply and divide first.", "Primero multiplique y divida."), "20 × 9 ÷ 5 = 36."),
   ("2", t("Then add 32.", "Después sume 32."), "36 + 32 = 68."),
   ("✓", t("Answer.", "Respuesta."), "<strong>68 °F</strong>")])}
{calc(t("Temperature on the calculator", "La temperatura en la calculadora"), t(f"<p>For 98.6 °F: {T('(')} {T('98.6')} {T('−')} {T('32')} {T(')')} {T('×')} {T('5')} {T('÷')} {T('9')} {T('enter')} gives 37. Without the parentheses the calculator would multiply first and give a wrong result.</p>", f"<p>Para 98.6 °F: {T('(')} {T('98.6')} {T('−')} {T('32')} {T(')')} {T('×')} {T('5')} {T('÷')} {T('9')} {T('enter')} da 37. Sin los paréntesis, la calculadora multiplicaría primero y daría un resultado equivocado.</p>"))}
{practica("p9", t("Practice 9 — Temperature", "Práctica 9 — Temperatura"), t("86 °F = ? °C", "86 °F = ? °C"), [("a", "30 °C"), ("b", "15.8 °C"), ("c", "186.8 °C"), ("d", "54 °C")])}
{enlace(n, t("temperature", "temperatura"), t("temperature: a special case", "la temperatura: un caso especial"), t("Convert between Fahrenheit and Celsius, subtracting or adding 32 in the right order.", "Convierta entre Fahrenheit y Celsius restando o sumando 32 en el orden correcto."))}'''

    secciones = [("s-" + t("doctors-office", "consultorio"), t("At the doctor's office and the pharmacy", "En el consultorio y en la farmacia"), s1),
                 ("s-" + t("factors", "factores"), t("The table of conversion factors", "La tabla de factores de conversión"), s2),
                 ("s-" + t("conversion-fraction", "fraccion-conversion"), t("The conversion-fraction method", "El método de la fracción de conversión"), s3),
                 ("s-" + t("temperature", "temperatura"), t("Temperature: a special case", "La temperatura: un caso especial"), s4)]

    lesson = {"next": t("Topic 7", "Tema 7"), "review": t("sections 2 and 3", "las secciones 2 y 3"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("You multiplied by 2.2. The number of kilograms must be smaller than the number of pounds.", "Multiplicó por 2.2. El número de kilogramos debe ser menor que el de libras."), "b": t("Check the decimal point: 150 × 0.454.", "Revise el punto decimal: 150 × 0.454."), "d": t("That is the weight in grams. Divide by 1,000.", "Ese es el peso en gramos. Divida entre 1,000.")},
             "right": t("150 × 454 = 68,100 g = 68.1 kg.", "150 × 454 = 68,100 g = 68.1 kg."), "solution": t("150 × 454 = 68,100 g; 68,100 ÷ 1,000 = 68.1 kg. Check: 150 ÷ 2.2 ≈ 68.", "150 × 454 = 68,100 g; 68,100 ÷ 1,000 = 68.1 kg. Comprobación: 150 ÷ 2.2 ≈ 68.")},
      "p2": {"ok": "b", "hints": {"a": t("A kilogram is more than a pound, not less.", "Un kilogramo es más que una libra, no menos."), "c": t("1 kg is about 2.2 lb, not 10 lb.", "1 kg son unas 2.2 lb, no 10 lb."), "d": t("You divided. 1 kg is a little more than 2 lb: multiply.", "Dividió. 1 kg es un poco más de 2 lb: multiplique.")},
             "right": t("10 × 2.2 ≈ 22 lb.", "10 × 2.2 ≈ 22 lb."), "solution": t("1 kg is a little more than 2 lb, so 10 kg ≈ 22 lb.", "1 kg es un poco más de 2 lb, así que 10 kg ≈ 22 lb.")},
      "p3": {"ok": "a", "hints": {"b": t("A gallon is almost 4 liters.", "Un galón son casi 4 litros."), "c": t("A quart is a little less than 1 liter.", "Un cuarto es un poco menos de 1 litro."), "d": t("2 gallons would be almost 8 liters.", "2 galones serían casi 8 litros.")},
             "right": t("2 ÷ 3.785 ≈ 0.53 gal: a little more than half.", "2 ÷ 3.785 ≈ 0.53 gal: un poco más de la mitad."), "solution": t("1 gal ≈ 3.785 L, so 2 L ≈ 0.53 gal, a little more than half a gallon.", "1 gal ≈ 3.785 L, así que 2 L ≈ 0.53 gal, un poco más de medio galón.")},
      "p4": {"ok": "a", "hints": {"b": t("The fraction is upside down: centimeters are smaller, so the number must grow.", "La fracción está al revés: los centímetros son más pequeños, así que el número debe crecer."), "c": t("You added 2.54. Multiply.", "Sumó 2.54. Multiplique."), "d": t("Check the decimal point: 20 × 2.54.", "Revise el punto decimal: 20 × 2.54.")},
             "right": t("20 × 2.54 = 50.8 cm.", "20 × 2.54 = 50.8 cm."), "solution": t("20 in × (2.54 cm / 1 in) = 50.8 cm.", "20 in × (2.54 cm / 1 in) = 50.8 cm.")},
      "p5": {"ok": "d", "hints": {"a": t("The fraction is upside down: kilometers are shorter, so the number must grow.", "La fracción está al revés: los kilómetros son más cortos, así que el número debe crecer."), "b": t("You added 1.609. Multiply.", "Sumó 1.609. Multiplique."), "c": t("Check the decimal point: 5 × 1.609.", "Revise el punto decimal: 5 × 1.609.")},
             "right": t("5 × 1.609 = 8.045 ≈ 8.05 km.", "5 × 1.609 = 8.045 ≈ 8.05 km."), "solution": t("5 mi × (1.609 km / 1 mi) = 8.045 ≈ 8.05 km.", "5 mi × (1.609 km / 1 mi) = 8.045 ≈ 8.05 km.")},
      "p6": {"ok": "b", "hints": {"a": t("The fraction is upside down: liters are smaller, so the number must grow.", "La fracción está al revés: los litros son más pequeños, así que el número debe crecer."), "c": t("You added 3.785. Multiply.", "Sumó 3.785. Multiplique."), "d": t("You used 4 qt per gallon; here the answer is in liters.", "Usó 4 cuartos por galón; aquí la respuesta va en litros.")},
             "right": t("4 × 3.785 = 15.14 L.", "4 × 3.785 = 15.14 L."), "solution": t("4 gal × (3.785 L / 1 gal) = 15.14 L.", "4 gal × (3.785 L / 1 gal) = 15.14 L.")},
      "p7": {"ok": "c", "hints": {"a": t("10 × 2.54 skips a step: first change feet to inches.", "10 × 2.54 salta un paso: primero pase los pies a pulgadas."), "b": t("A fraction is upside down. A meter is longer than a foot, but only about 3 times longer.", "Hay una fracción al revés. Un metro es más largo que un pie, pero solo unas 3 veces."), "d": t("That is in centimeters. Divide by 100.", "Eso está en centímetros. Divida entre 100.")},
             "right": t("10 × 12 × 2.54 ÷ 100 = 3.048 ≈ 3.05 m.", "10 × 12 × 2.54 ÷ 100 = 3.048 ≈ 3.05 m."), "solution": t("10 ft × (12 in / 1 ft) × (2.54 cm / 1 in) × (1 m / 100 cm): 120 in; 304.8 cm; 3.048 m.", "10 ft × (12 in / 1 ft) × (2.54 cm / 1 in) × (1 m / 100 cm): 120 in; 304.8 cm; 3.048 m.")},
      "p8": {"ok": "d", "hints": {"a": t("With km on top, the kilometers do not cancel.", "Con km arriba, los kilómetros no se cancelan."), "b": t("1 km is not 1.609 mi; it is the other way around.", "1 km no son 1.609 mi; es al revés."), "c": t("1 km is not 1.609 mi; it is the other way around.", "1 km no son 1.609 mi; es al revés.")},
             "right": t("km goes on the bottom so it cancels: 50 ÷ 1.609 ≈ 31.1 mi.", "km va abajo para cancelarse: 50 ÷ 1.609 ≈ 31.1 mi."), "solution": t("The unit to get rid of (km) goes on the bottom: 1 mi / 1.609 km.", "La unidad que se elimina (km) va abajo: 1 mi / 1.609 km.")},
      "p9": {"ok": "a", "hints": {"b": t("Subtract 32 first, inside the parentheses.", "Primero reste 32, dentro del paréntesis."), "c": t("That is the formula for going to Fahrenheit.", "Esa es la fórmula para pasar a Fahrenheit."), "d": t("86 − 32 = 54; you still need × 5 ÷ 9.", "86 − 32 = 54; falta × 5 ÷ 9.")},
             "right": t("(86 − 32) × 5 ÷ 9 = 54 × 5 ÷ 9 = 30 °C.", "(86 − 32) × 5 ÷ 9 = 54 × 5 ÷ 9 = 30 °C."), "solution": t("(86 − 32) × 5 ÷ 9 = 54 × 5 ÷ 9 = 270 ÷ 9 = 30.", "(86 − 32) × 5 ÷ 9 = 54 × 5 ÷ 9 = 270 ÷ 9 = 30.")}
     },
     "quiz": {
      "A": {"ok": "b", "hints": {"a": t("The fraction is upside down.", "La fracción está al revés."), "c": t("You added 2.54.", "Sumó 2.54."), "d": t("Centimeters are smaller: the number must grow.", "Los centímetros son más pequeños: el número debe crecer.")}, "solution": t("12 × 2.54 = 30.48 cm.", "12 × 2.54 = 30.48 cm.")},
      "B": {"ok": "c", "hints": {"a": t("The fraction is upside down: miles are longer.", "La fracción está al revés: las millas son más largas."), "b": t("Check the decimal point: 10 ÷ 1.609.", "Revise el punto decimal: 10 ÷ 1.609."), "d": t("That is 1 mile in meters.", "Eso es 1 milla en metros.")}, "solution": t("10 ÷ 1.609 ≈ 6.2 mi.", "10 ÷ 1.609 ≈ 6.2 mi.")},
      "C": {"ok": "a", "hints": {"b": t("You multiplied by 2.2. Kilograms are heavier: the number must shrink.", "Multiplicó por 2.2. El kilogramo pesa más: el número debe bajar."), "c": t("That is in grams. Divide by 1,000.", "Eso está en gramos. Divida entre 1,000."), "d": t("You divided by 2. A kilogram is a little more than 2 lb.", "Dividió entre 2. Un kilogramo es un poco más de 2 lb.")}, "solution": t("165 × 454 = 74,910 g ≈ 74.9 kg.", "165 × 454 = 74,910 g ≈ 74.9 kg.")},
      "D": {"ok": "d", "hints": {"a": t("The fraction is upside down.", "La fracción está al revés."), "b": t("You added 3.785.", "Sumó 3.785."), "c": t("You used 4 qt per gallon.", "Usó 4 cuartos por galón.")}, "solution": t("3 × 3.785 = 11.355 ≈ 11.4 L.", "3 × 3.785 = 11.355 ≈ 11.4 L.")},
      "E": {"ok": "b", "hints": {"a": t("That is in inches.", "Eso está en pulgadas."), "c": t("You skipped changing feet to inches.", "Faltó pasar los pies a pulgadas."), "d": t("That is in centimeters.", "Eso está en centímetros.")}, "solution": t("6 × 12 × 2.54 ÷ 100 = 1.8288 ≈ 1.83 m.", "6 × 12 × 2.54 ÷ 100 = 1.8288 ≈ 1.83 m.")},
      "F": {"ok": "d", "hints": {"a": t("That is in kilometers. Multiply by 1,000.", "Eso está en kilómetros. Multiplique por 1,000."), "b": t("That is 2 miles in feet.", "Eso son 2 millas en pies."), "c": t("A fraction is upside down.", "Hay una fracción al revés.")}, "solution": t("2 × 1.609 = 3.218 km = 3,218 m.", "2 × 1.609 = 3.218 km = 3,218 m.")},
      "G": {"ok": "a", "hints": {"b": t("Subtract 32 first, inside the parentheses.", "Primero reste 32, dentro del paréntesis."), "c": t("That is the formula for going to Fahrenheit.", "Esa es la fórmula para pasar a Fahrenheit."), "d": t("98.6 − 32 = 66.6; you still need × 5 ÷ 9.", "98.6 − 32 = 66.6; falta × 5 ÷ 9.")}, "solution": t("(98.6 − 32) × 5 ÷ 9 = 37 °C.", "(98.6 − 32) × 5 ÷ 9 = 37 °C.")},
      "H": {"ok": "c", "hints": {"a": t("You still need to add 32.", "Falta sumar 32."), "b": t("Add 32 at the end, after multiplying.", "El 32 se suma al final, después de multiplicar."), "d": t("That is the formula for going to Celsius.", "Esa es la fórmula para pasar a Celsius.")}, "solution": t("20 × 9 ÷ 5 + 32 = 36 + 32 = 68 °F.", "20 × 9 ÷ 5 + 32 = 36 + 32 = 68 °F.")}
     }}

    quiz = [
     ("A", t("12 in = ? cm", "12 in = ? cm"), [("a", "4.72 cm"), ("b", "30.48 cm"), ("c", "14.54 cm"), ("d", "1.2 cm")]),
     ("B", t("How many miles is a 10 km race?", "¿Cuántas millas mide una carrera de 10 km?"), [("a", "16.09 mi"), ("b", "0.62 mi"), ("c", t("about 6.2 mi", "unas 6.2 mi")), ("d", "1,609 mi")]),
     ("C", t("165 lb is about how many kilograms?", "165 lb son aproximadamente ¿cuántos kilogramos?"), [("a", "74.9 kg"), ("b", "363 kg"), ("c", "74,910 kg"), ("d", "82.5 kg")]),
     ("D", t("How many liters are in 3 gallons?", "¿Cuántos litros hay en 3 galones?"), [("a", "0.79 L"), ("b", "6.785 L"), ("c", "12 L"), ("d", t("about 11.4 L", "unos 11.4 L"))]),
     ("E", t("A person is 6 ft tall. About how many meters is that?", "Una persona mide 6 ft. ¿Cuántos metros son, aproximadamente?"), [("a", "72 m"), ("b", "1.83 m"), ("c", "15.24 m"), ("d", "182.88 m")]),
     ("F", t("How many meters are in 2 miles?", "¿Cuántos metros hay en 2 millas?"), [("a", "3.218 m"), ("b", "10,560 m"), ("c", "1,243 m"), ("d", "3,218 m")]),
     ("G", t("98.6 °F = ? °C", "98.6 °F = ? °C"), [("a", "37 °C"), ("b", "22.8 °C"), ("c", "209.5 °C"), ("d", "66.6 °C")]),
     ("H", t("20 °C = ? °F", "20 °C = ? °F"), [("a", "36 °F"), ("b", "93.6 °F"), ("c", "68 °F"), ("d", "−6.7 °F")])]

    return B.pagina_leccion(n, 6, t(*TEMA), t(*TIT),
        t("From pounds to kilograms, from miles to kilometers, from Fahrenheit to Celsius: the conversion factor, the conversion-fraction method, and the special case of temperature.", "De libras a kilogramos, de millas a kilómetros, de Fahrenheit a Celsius: el factor de conversión, el método de la fracción de conversión y el caso especial de la temperatura."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Convert</strong> lengths, weights, and capacities between the U.S. customary and metric systems with the most common factors.", "<strong>Convertir</strong> longitudes, pesos y capacidades entre el sistema inglés y el métrico con los factores de conversión más usados."),
         t("<strong>Use</strong> the conversion-fraction method: multiply by 1 and cancel units.", "<strong>Aplicar</strong> el método de la fracción de conversión: multiplicar por 1 y cancelar unidades."),
         t("<strong>Solve</strong> conversions with several steps, for example, from feet to meters or from miles to meters.", "<strong>Resolver</strong> conversiones de varios pasos; por ejemplo, de pies a metros o de millas a metros."),
         t("<strong>Convert</strong> temperatures between degrees Fahrenheit and Celsius.", "<strong>Convertir</strong> temperaturas entre grados Fahrenheit y Celsius."),
         t("<strong>Apply</strong> conversions in health, work, and travel situations, with a reasonable estimate.", "<strong>Aplicar</strong> las conversiones en situaciones de salud, trabajo y viaje, con una aproximación razonable.")],
        secciones,
        (t("Do ten U.S. customary ↔ metric conversions of length, weight, and capacity; for each one, write the whole conversion fraction, not just the result. Do four conversions with several steps and four temperature conversions, two each way.",
           "Haga diez conversiones inglés ↔ métrico de longitud, peso y capacidad; en cada una, escriba la fracción de conversión completa, no solo el resultado. Haga cuatro conversiones de varios pasos y cuatro de temperatura, dos en cada sentido."),
         t("Look at labels at home or at the store: a soda bottle, a medicine box, a bag of food. Find a measurement in one system, convert it to the other, and check it against the label if it shows both.",
           "Revise etiquetas en casa o en la tienda: una botella de refresco, una caja de medicina, una bolsa de comida. Busque una medida en un sistema, conviértala al otro y compruébela con la etiqueta si trae las dos.")),
        quiz,
        t("Self-check checklist for conversions", "Lista de autoevaluación de conversiones"),
        t("Self-check checklist: skills for unit conversions", "Lista de autoevaluación: destrezas de conversión de unidades"),
        [(t("Choose the conversion factor", "Seleccionar el factor de conversión"), t("I choose the right factor every time, also in several steps, and I plan the chain before I calculate.", "Elijo el factor correcto en todos los casos, también en varios pasos, y planeo la cadena antes de calcular."), t("I choose the right factor with the table, but sometimes I use it upside down.", "Elijo el factor correcto con la tabla, pero a veces lo uso al revés."), t("I choose a factor for another quantity (for example, a length factor for a weight).", "Elijo un factor de otra magnitud (por ejemplo, de longitud para un peso).")),
         (t("Use the conversion-fraction method", "Aplicar el método de la fracción de conversión"), t("I write the fractions and cancel units at each step, also in temperature conversions.", "Escribo las fracciones y cancelo las unidades en cada paso, también en las conversiones de temperatura."), t("I write the fractions but make mistakes canceling units or calculating.", "Escribo las fracciones, pero me equivoco al cancelar unidades o al operar."), t("I multiply or divide without writing the units.", "Multiplico o divido sin escribir las unidades.")),
         (t("Give the result", "Expresar el resultado"), t("I give the result in the unit asked, rounded reasonably, and I check it with an estimate.", "Doy el resultado en la unidad pedida, con un redondeo razonable, y lo compruebo con una estimación."), t("I write the right unit but round in an odd way.", "Escribo la unidad correcta, pero redondeo de forma poco razonable."), t("I give a number with no unit or with the wrong unit.", "Doy un número sin unidad o con una unidad equivocada."))],
        t("<p>Converting units means multiplying by 1 written in a clever way: the <strong>conversion fraction</strong>. The golden rule, putting the unit you want to get rid of on the bottom, works the same at the pharmacy, in the shop, or on the road.</p>\n<p>That closes Topic 6: simple interest, depreciation, and conversions, three everyday uses of proportional reasoning. <strong>Topic 7</strong> moves into the geometry of composite figures and the circle, where units of measure take center stage again.</p>",
          "<p>Convertir unidades es multiplicar por 1 escrito de forma inteligente: la <strong>fracción de conversión</strong>. La regla de oro, poner abajo la unidad que se quiere eliminar, sirve igual para la farmacia, el taller o la carretera.</p>\n<p>Así se cierra el Tema 6: interés simple, depreciación y conversiones, tres aplicaciones del razonamiento proporcional a la vida diaria. El <strong>Tema 7</strong> entra en la geometría de las figuras compuestas y el círculo, donde las unidades de medida vuelven a ser protagonistas.</p>"),
        ("7-1", ("", t("Lesson 7.1 · Area of composite figures", "Lección 7.1 · Área de figuras compuestas"))),
        [(t("U.S. customary system", "sistema inglés"), t("The system of inches, feet, miles, pounds, and gallons used in the United States.", "El sistema de pulgadas, pies, millas, libras y galones que se usa en Estados Unidos.")),
         (t("metric system", "sistema métrico"), t("The system of meters, grams, and liters, based on powers of 10.", "El sistema de metros, gramos y litros, basado en potencias de 10.")),
         (t("conversion factor", "factor de conversión"), t("A ratio of two equal measurements, like 2.54 cm / 1 in; it is worth 1.", "Una razón entre dos medidas iguales, como 2.54 cm / 1 in; vale 1.")),
         (t("conversion fraction", "fracción de conversión"), t("The conversion factor written so that the unit to get rid of is on the bottom.", "El factor de conversión escrito de modo que la unidad que se elimina quede abajo."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "nom": {"in": "inches", "ft": "feet", "yd": "yards", "mi": "miles", "cm": "centimeters", "m": "meters", "km": "kilometers", "oz": "ounces", "lb": "pounds", "g": "grams", "kg": "kilograms", "qt": "quarts", "gal": "gallons", "mL": "milliliters", "L": "liters"},
  "por": " times ", "sobre": " over ",
  "cs1": "Pounds to grams: {lb} × 454 = {g} g. Grams to kilograms: {g} ÷ 1,000 = {kg} kg.", "cs2": "Check: {lb} ÷ 2.2 ≈ {e} kg. ✓",
  "cs1q": "A patient weighs {lb} pounds. How many kilograms is that? (1 lb ≈ 454 g; round to the tenth)", "cs1s": "{lb} × 454 = {g} g = {kg} kg ≈ {r} kg.", "cs1p": "You divided instead of multiplying: the number of kilograms must be smaller than the number of pounds.", "cs1g": "That is the weight in grams. You still need to divide by 1,000.",
  "cs2q": "A baby weighs {kg} kg. About how many pounds is that? (1 lb ≈ 454 g; round to the tenth)", "cs2s": "{kg} kg = {g} g; {g} ÷ 454 ≈ {r} lb.", "cs2p": "The fraction is upside down: from kilograms to pounds the number must grow.",
  "cs3q": "A prescription calls for {d} mg of a medicine for each kilogram of weight. The patient weighs {lb} lb. How many milligrams is the dose? (1 lb ≈ 454 g; round to the tenth)", "cs3s": "{lb} lb × 0.454 = {kg} kg; × {d} = {r} mg.", "cs3p": "First change the weight to kilograms.",
  "sq": "Which of these results makes sense for {x} {de} changed to {a}?", "sAlReves": "That is what you get with the fraction upside down.", "sGrande": "The new unit is bigger, so the number comes out smaller", "sChica": "The new unit is smaller, so the number comes out bigger",
  "fcAviso": "Type a positive amount.", "fcIgual": "The two units are the same: there is nothing to convert.", "fcCamino": "Path: {c}. Each fraction has on the bottom the unit that cancels (crossed out).",
  "fcQ": "Convert {x} {de} to {a}. (Round to the hundredth.)", "fcP": "It looks like a fraction ended up upside down: the unit you get rid of goes on the bottom.",
  "tmVoz": "{F} degrees Fahrenheit is {C} degrees Celsius.", "tmFC1": "Parentheses first: {F} − 32 = {r}. Then × 5 ÷ 9: {m} ÷ 9 ≈ {C}.", "tmCF1": "Multiplication and division first: {C} × 9 ÷ 5 = {m}. Then + 32 = {F}.",
  "tmQ1": "Convert {x} °F to degrees Celsius. (Round to the tenth if needed.)", "tmS1": "({x} − 32) × 5 ÷ 9 = {r} × 5 ÷ 9 ≈ {c} °C.", "tmP1": "First subtract 32 (inside the parentheses), then multiply by 5 ÷ 9.", "tmP2": "Subtract 32 before you multiply.",
  "tmQ2": "Convert {x} °C to degrees Fahrenheit. (Round to the tenth if needed.)", "tmS2": "{x} × 9 ÷ 5 + 32 = {m} + 32 = {c} °F.", "tmP3": "Add 32 at the end, after multiplying by 9 ÷ 5.", "tmP4": "That is the formula from °F to °C. To go to Fahrenheit: × 9 ÷ 5 + 32."
 },
 "es": {
  "nom": {"in": "pulgadas", "ft": "pies", "yd": "yardas", "mi": "millas", "cm": "centímetros", "m": "metros", "km": "kilómetros", "oz": "onzas", "lb": "libras", "g": "gramos", "kg": "kilogramos", "qt": "cuartos", "gal": "galones", "mL": "mililitros", "L": "litros"},
  "por": " por ", "sobre": " sobre ",
  "cs1": "De libras a gramos: {lb} × 454 = {g} g. De gramos a kilogramos: {g} ÷ 1,000 = {kg} kg.", "cs2": "Comprobación: {lb} ÷ 2.2 ≈ {e} kg. ✓",
  "cs1q": "Un paciente pesa {lb} libras. ¿Cuántos kilogramos son? (1 lb ≈ 454 g; redondee a la décima)", "cs1s": "{lb} × 454 = {g} g = {kg} kg ≈ {r} kg.", "cs1p": "Se dividió en vez de multiplicar: el número de kilogramos debe ser menor que el de libras.", "cs1g": "Ese es el peso en gramos. Falta dividir entre 1,000.",
  "cs2q": "Un bebé pesa {kg} kg. ¿Cuántas libras son, aproximadamente? (1 lb ≈ 454 g; redondee a la décima)", "cs2s": "{kg} kg = {g} g; {g} ÷ 454 ≈ {r} lb.", "cs2p": "La fracción está al revés: de kilogramos a libras el número debe crecer.",
  "cs3q": "Una receta médica indica {d} mg de un medicamento por cada kilogramo de peso. El paciente pesa {lb} lb. ¿Cuántos miligramos le corresponden? (1 lb ≈ 454 g; redondee a la décima)", "cs3s": "{lb} lb × 0.454 = {kg} kg; × {d} = {r} mg.", "cs3p": "Primero hay que pasar el peso a kilogramos.",
  "sq": "¿Cuál de estos resultados tiene sentido para {x} {de} convertidos a {a}?", "sAlReves": "Así sale con la fracción al revés.", "sGrande": "La unidad nueva es más grande, así que el número sale más pequeño", "sChica": "La unidad nueva es más pequeña, así que el número sale más grande",
  "fcAviso": "Escriba una cantidad positiva.", "fcIgual": "Las dos unidades son iguales: no hay nada que convertir.", "fcCamino": "Camino: {c}. Cada fracción tiene abajo la unidad que se cancela (tachada).",
  "fcQ": "Convierta {x} {de} a {a}. (Redondee a la centésima.)", "fcP": "Parece que alguna fracción quedó al revés: la unidad que se elimina va abajo.",
  "tmVoz": "{F} grados Fahrenheit son {C} grados Celsius.", "tmFC1": "Paréntesis primero: {F} − 32 = {r}. Después × 5 ÷ 9: {m} ÷ 9 ≈ {C}.", "tmCF1": "Multiplicación y división primero: {C} × 9 ÷ 5 = {m}. Después + 32 = {F}.",
  "tmQ1": "Convierta {x} °F a grados Celsius. (Redondee a la décima si hace falta.)", "tmS1": "({x} − 32) × 5 ÷ 9 = {r} × 5 ÷ 9 ≈ {c} °C.", "tmP1": "Primero se resta 32 (dentro del paréntesis) y después se multiplica por 5 ÷ 9.", "tmP2": "El 32 se resta antes de multiplicar.",
  "tmQ2": "Convierta {x} °C a grados Fahrenheit. (Redondee a la décima si hace falta.)", "tmS2": "{x} × 9 ÷ 5 + 32 = {m} + 32 = {c} °F.", "tmP3": "Se suma 32 al final, después de multiplicar por 9 ÷ 5.", "tmP4": "Esa es la fórmula de °F a °C. Para ir a Fahrenheit: × 9 ÷ 5 + 32."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function redon(v, d){ var p = Math.pow(10, d); return Math.round(v * p) / p; }

/* ---------- Conversion engine ---------- */
var UNI = { long: ["in", "ft", "yd", "mi", "cm", "m", "km"], peso: ["oz", "lb", "g", "kg"], cap: ["qt", "gal", "mL", "L"] };
var ARISTAS = [["in","cm",2.54],["mi","km",1.609],["lb","g",454],["gal","L",3.785],["ft","in",12],["yd","ft",3],["mi","ft",5280],["lb","oz",16],["gal","qt",4],["m","cm",100],["km","m",1000],["kg","g",1000],["L","mL",1000]];
function vecinos(u){ var v = []; ARISTAS.forEach(function(a){ if (a[0] === u) v.push(a[1]); else if (a[1] === u) v.push(a[0]); }); return v; }
function camino(de, a){
  var cola = [[de]], vistos = {}; vistos[de] = true;
  while (cola.length){ var r = cola.shift(), u = r[r.length - 1]; if (u === a) return r; vecinos(u).forEach(function(v){ if (!vistos[v]){ vistos[v] = true; cola.push(r.concat([v])); } }); }
  return null;
}
function arista(u, v){ for (var i = 0; i < ARISTAS.length; i++){ var e = ARISTAS[i]; if (e[0] === u && e[1] === v) return { arriba: [e[2], v], abajo: [1, u], f: e[2] }; if (e[1] === u && e[0] === v) return { arriba: [1, v], abajo: [e[2], u], f: 1 / e[2] }; } }
function convertir(x, de, a){ var c = camino(de, a), v = x, pasos = []; for (var i = 0; i < c.length - 1; i++){ var e = arista(c[i], c[i + 1]); v *= e.f; pasos.push(e); } return { v: v, pasos: pasos, camino: c }; }
function fracU(e){ return '<span class="fracc"><span class="fa">' + nd(e.arriba[0]) + ' ' + e.arriba[1] + '</span><span class="fb2">' + nd(e.abajo[0]) + ' <span class="tach">' + e.abajo[1] + '</span></span></span>'; }
function cadenaHTML(x, de, R){
  var h = nd(x) + ' <span class="tach">' + de + '</span>';
  R.pasos.forEach(function(e){ h += ' × ' + fracU(e); });
  var voz = nd(x) + " " + TXT.nom[de] + R.pasos.map(function(e){ return TXT.por + nd(e.arriba[0]) + " " + TXT.nom[e.arriba[1]] + TXT.sobre + nd(e.abajo[0]) + " " + TXT.nom[e.abajo[1]]; }).join("");
  return '<span aria-hidden="true">' + h + '</span><span class="sr-only">' + voz + '</span>';
}

/* ============ MODULE 1 · doctor's office ============ */
function pintaCS(){
  var lb = +$("cs-lb").value, g = lb * 454, kg = g / 1000;
  $("cs-lbv").textContent = lb;
  $("cs-salida").innerHTML = '<div class="linea cadena">' + cadenaHTML(lb, "lb", convertir(lb, "lb", "kg")) + ' = ' + nd(redon(kg, 2)) + ' kg</div>' +
    '<div class="linea">' + F(TXT.cs1, { lb: lb, g: nd(g), kg: nd(redon(kg, 2)) }) + '</div>' +
    '<div class="linea">' + F(TXT.cs2, { lb: lb, e: nd(redon(lb / 2.2, 1)) }) + '</div>';
}
function genCS(){
  var tp = aleatorio(1, 3), res, enun, sol, p = [];
  if (tp === 1){ var lb = aleatorio(20, 250); res = redon(lb * 0.454, 1); enun = F(TXT.cs1q, { lb: lb }); sol = F(TXT.cs1s, { lb: lb, g: nd(lb * 454), kg: nd(redon(lb * 0.454, 3)), r: nd(res) });
    p.push({ v: redon(lb / 0.454, 1), msg: TXT.cs1p }, { v: lb * 454, msg: TXT.cs1g }); }
  else if (tp === 2){ var kg = aleatorio(3, 40); res = redon(kg * 1000 / 454, 1); enun = F(TXT.cs2q, { kg: kg }); sol = F(TXT.cs2s, { kg: kg, g: nd(kg * 1000), r: nd(res) }); p.push({ v: redon(kg * 0.454, 1), msg: TXT.cs2p }); }
  else { var lb2 = 5 * aleatorio(4, 40), d = elige([2, 5, 10, 15]), kg2 = lb2 * 0.454; res = redon(d * kg2, 1); enun = F(TXT.cs3q, { d: d, lb: lb2 }); sol = F(TXT.cs3s, { lb: lb2, kg: nd(redon(kg2, 3)), d: d, r: nd(res) }); p.push({ v: d * lb2, msg: TXT.cs3p }); }
  return { enun: enun, correcta: nd(res), solucion: sol, evalua: numD(res, p.filter(function(x){ return Math.abs(x.v - res) > 0.06; }), null, 0.051) };
}

/* ============ MODULE 2 · does it make sense? ============ */
function genSentido(){
  var casos = [[10, "km", "mi"], [5, "kg", "lb"], [2, "L", "qt"], [12, "in", "cm"], [3, "gal", "L"], [100, "m", "yd"], [26.2, "mi", "km"], [150, "lb", "kg"]];
  var c = elige(casos), R = convertir(c[0], c[1], c[2]), bien = redon(R.v, 2), inv = redon(c[0] / R.v * c[0], 2);
  var o = [bien, inv, redon(c[0], 2), redon(bien * 10, 2)].filter(function(x, i, a){ return a.indexOf(x) === i; }).map(function(x){ return { html: nd(x) + " " + c[2], clave: "v" + x }; });
  var pc = {}; pc["v" + inv] = TXT.sAlReves;
  var ex = (R.v < c[0] ? TXT.sGrande : TXT.sChica) + ": " + nd(c[0]) + " " + c[1] + " ≈ " + nd(bien) + " " + c[2] + ".";
  return { enun: F(TXT.sq, { x: nd(c[0]), de: TXT.nom[c[1]], a: TXT.nom[c[2]] }), opciones: o, correcta: "v" + bien, pistas: pc, bien: ex, mal: ex };
}

/* ============ MODULE 3 · the conversion fraction ============ */
function llenaUnidades(){
  var m = $("fc-m").value, de = $("fc-de"), a = $("fc-a");
  de.innerHTML = UNI[m].map(function(u){ return '<option value="' + u + '">' + TXT.nom[u] + ' (' + u + ')</option>'; }).join(""); a.innerHTML = de.innerHTML;
  var def = { long: ["ft", "m"], peso: ["lb", "kg"], cap: ["gal", "L"] }[m]; de.value = def[0]; a.value = def[1];
}
function pintaFC(){
  var x = leeD($("fc-x").value), de = $("fc-de").value, a = $("fc-a").value, av = $("fc-aviso");
  if (x === null || x < 0){ av.className = "caja-aviso visible"; av.textContent = TXT.fcAviso; $("fc-x").classList.add("error"); $("fc-salida").innerHTML = ""; return; }
  av.className = "caja-aviso"; av.textContent = ""; $("fc-x").classList.remove("error");
  if (de === a){ $("fc-salida").innerHTML = '<div class="linea">' + TXT.fcIgual + '</div>'; return; }
  var R = convertir(x, de, a), parcial = x, h = '<div class="linea cadena">' + cadenaHTML(x, de, R) + ' = <strong>' + nd(redon(R.v, 4)) + ' ' + a + '</strong></div>';
  h += '<div class="linea">' + F(TXT.fcCamino, { c: R.camino.map(function(u){ return TXT.nom[u]; }).join(" → ") }) + '</div>';
  R.pasos.forEach(function(e){ var ant = parcial; parcial *= e.f; h += '<div class="linea">' + nd(redon(ant, 4)) + ' ' + e.abajo[1] + (e.f >= 1 ? ' × ' + nd(e.arriba[0]) : ' ÷ ' + nd(e.abajo[0])) + ' = ' + nd(redon(parcial, 4)) + ' ' + e.arriba[1] + '</div>'; });
  $("fc-salida").innerHTML = h;
}
var PARES = [[12, "in", "cm"], [10, "km", "mi"], [3, "gal", "L"], [6, "ft", "m"], [2, "mi", "m"], [5, "yd", "m"], [250, "cm", "in"], [8, "L", "gal"], [3, "lb", "kg"], [500, "g", "oz"], [2, "kg", "lb"], [20, "m", "ft"], [5, "qt", "L"], [1500, "mL", "qt"]];
function genFC(){
  var c = elige(PARES), x = c[0] * elige([1, 2, 3, 0.5, 1.5]), R = convertir(x, c[1], c[2]), res = redon(R.v, 2), inv = redon(x * x / R.v, 2), tol = Math.max(0.011, Math.abs(res) * 0.002);
  var p = Math.abs(inv - res) > tol * 2 ? [{ v: inv, msg: TXT.fcP }] : [];
  return { enun: F(TXT.fcQ, { x: nd(x), de: TXT.nom[c[1]], a: TXT.nom[c[2]] }), correcta: nd(res), solucion: cadenaHTML(x, c[1], R) + " ≈ " + nd(res) + " " + c[2] + ".", evalua: numD(res, p, null, tol) };
}

/* ============ MODULE 4 · temperature ============ */
function aC(f){ return (f - 32) * 5 / 9; }
function aF(c){ return c * 9 / 5 + 32; }
function termo(x, lo, hi, cx, et){
  var y0 = 220, y1 = 20, y = y0 - (x - lo) / (hi - lo) * (y0 - y1);
  return '<rect x="' + cx + '" y="' + y1 + '" width="22" height="' + (y0 - y1) + '" rx="11" fill="#fff" stroke="#004d40" stroke-width="2"/>' +
    '<rect x="' + (cx + 4) + '" y="' + f1(y) + '" width="14" height="' + f1(y0 - y + 8) + '" rx="7" fill="#c62828"/><circle cx="' + (cx + 11) + '" cy="' + (y0 + 12) + '" r="16" fill="#c62828"/>' +
    texto([cx + 11, 262], et, 16, "#004d40", 700) + '<text x="' + (cx + 34) + '" y="' + f1(y) + '" dominant-baseline="middle" font-size="16" font-weight="700" fill="#004d40">' + nd(redon(x, 1)) + ' ' + et + '</text>';
}
function pintaTM(){
  var dir = $("tm-dir").value, sl = $("tm-v");
  sl.min = -40; sl.max = dir === "fc" ? 220 : 105;
  var v = +sl.value; if (v > +sl.max){ v = +sl.max; sl.value = v; }
  var Fh = dir === "fc" ? v : aF(v), C = dir === "fc" ? aC(v) : v;
  $("tm-vv").textContent = nd(redon(v, 1)) + (dir === "fc" ? " °F" : " °C");
  $("tm-svg").innerHTML = '<svg class="figura" style="max-width:420px" viewBox="0 0 420 280" role="img" aria-label="' + F(TXT.tmVoz, { F: nd(redon(Fh, 1)), C: nd(redon(C, 1)) }) + '">' + termo(Fh, -40, 220, 80, "°F") + termo(C, -40, 105, 260, "°C") + '</svg>';
  $("tm-salida").innerHTML = dir === "fc"
    ? '<div class="linea">' + F(TXT.tmFC1, { F: nd(redon(Fh, 1)), r: nd(redon(Fh - 32, 2)), m: nd(redon((Fh - 32) * 5, 2)), C: nd(redon(C, 1)) }) + '</div><div class="linea veredicto">' + nd(redon(Fh, 1)) + ' °F ≈ ' + nd(redon(C, 1)) + ' °C</div>'
    : '<div class="linea">' + F(TXT.tmCF1, { C: nd(redon(C, 1)), m: nd(redon(C * 9 / 5, 2)), F: nd(redon(Fh, 1)) }) + '</div><div class="linea veredicto">' + nd(redon(C, 1)) + ' °C ≈ ' + nd(redon(Fh, 1)) + ' °F</div>';
}
function genTM(){
  var fc = Math.random() < 0.5, enun, res, sol, p = [];
  if (fc){ var Fv = elige([98.6, 32, 212, 50, 68, 77, 104, 14, -4, 86, 59, 23]); res = redon(aC(Fv), 1);
    enun = F(TXT.tmQ1, { x: nd(Fv) }); sol = F(TXT.tmS1, { x: nd(Fv), r: nd(redon(Fv - 32, 2)), c: nd(res) });
    p.push({ v: redon(Fv - 32 * 5 / 9, 1), msg: TXT.tmP1 }, { v: redon(Fv * 5 / 9 - 32, 1), msg: TXT.tmP2 }); }
  else { var Cv = elige([37, 20, 0, 100, 25, 30, -10, 15, 40, -5, 10]); res = redon(aF(Cv), 1);
    enun = F(TXT.tmQ2, { x: nd(Cv) }); sol = F(TXT.tmS2, { x: nd(Cv), m: nd(redon(Cv * 9 / 5, 2)), c: nd(res) });
    p.push({ v: redon((Cv + 32) * 9 / 5, 1), msg: TXT.tmP3 }, { v: redon(aC(Cv), 1), msg: TXT.tmP4 }); }
  return { enun: enun, correcta: nd(res), solucion: sol, evalua: numD(res, p.filter(function(x){ return Math.abs(x.v - res) > 0.06; }), null, 0.051) };
}

/* ============ Start ============ */
$("cs-lb").addEventListener("input", pintaCS); pintaCS();
creaPracticaLibre("p1", genCS);
creaPracticaOM("p2", genSentido);
$("fc-m").addEventListener("change", function(){ llenaUnidades(); pintaFC(); }); ["fc-de", "fc-a"].forEach(function(id){ $(id).addEventListener("change", pintaFC); }); $("fc-x").addEventListener("input", pintaFC);
llenaUnidades(); pintaFC();
creaPracticaLibre("p3", genFC);
$("tm-dir").addEventListener("change", function(){ $("tm-v").value = $("tm-dir").value === "fc" ? 98.6 : 20; pintaTM(); }); $("tm-v").addEventListener("input", pintaTM); pintaTM();
creaPracticaLibre("p4", genTM);
'''

def libre_x(pid, titulo, etiqueta, nota):
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), nota)

def practica_pagina():
    n = N
    mods = [
     (t("doctors-office", "consultorio"), t("At the doctor's office and the pharmacy", "En el consultorio y en la farmacia"),
      f'''      <p>{t("The United States uses the U.S. customary system (pounds, inches, gallons); almost all the rest of the world uses the metric system (kilograms, centimeters, liters). At the doctor's office weight is usually written in pounds, but many medicine doses are figured per kilogram.", "En Estados Unidos se usa el sistema inglés (libras, pulgadas, galones); en casi todo el resto del mundo, el métrico (kilogramos, centímetros, litros). En el consultorio el peso suele anotarse en libras, pero muchas dosis de medicamentos se calculan por kilogramo.")}</p>
      <h3>{t("From pounds to kilograms", "De libras a kilogramos")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:220px;"><label for="cs-lb">{t("Weight (pounds)", "Peso (libras)")}: <span id="cs-lbv"></span></label><input type="range" id="cs-lb" min="10" max="300" step="5" value="165"></div></div>
        <div class="salida" id="cs-salida" aria-live="polite"></div>
      </div>
      <div class="caja-tip"><strong>{t("To check:", "Para comprobar:")}</strong> {t("a kilogram is a little more than 2 pounds, so the weight in kilograms is a little less than half the weight in pounds (pounds ÷ 2.2).", "un kilogramo es un poco más de 2 libras, así que el peso en kilos es un poco menos de la mitad del peso en libras (libras ÷ 2.2).")}</div>
{libre_x("p1", t("Practice: at the doctor's office", "Practique: en el consultorio"), t("Answer", "Resultado"), t("Round to one decimal place, for example 74.9.", "Redondee a una cifra decimal, por ejemplo 74.9."))}'''),
     (t("factors", "factores"), t("The table of conversion factors", "La tabla de factores de conversión"),
      f'''      <table class="reglas">
        <caption>{t("Between the two systems", "Entre los dos sistemas")}</caption>
        <thead><tr><th scope="col">{t("Quantity", "Magnitud")}</th><th scope="col">{t("Equivalence", "Equivalencia")}</th></tr></thead>
        <tbody>
          <tr><td>{t("Length", "Longitud")}</td><td>1 in = 2.54 cm</td></tr>
          <tr><td>{t("Length", "Longitud")}</td><td>1 mi ≈ 1.609 km</td></tr>
          <tr><td>{t("Weight", "Peso")}</td><td>1 lb ≈ 454 g</td></tr>
          <tr><td>{t("Capacity", "Capacidad")}</td><td>1 gal ≈ 3.785 L</td></tr>
        </tbody>
      </table>
      <table class="reglas">
        <caption>{t("Within each system", "Dentro de cada sistema")}</caption>
        <thead><tr><th scope="col">{t("U.S. customary", "Inglés")}</th><th scope="col">{t("Metric", "Métrico")}</th></tr></thead>
        <tbody>
          <tr><td>1 ft = 12 in</td><td>1 m = 100 cm</td></tr>
          <tr><td>1 yd = 3 ft</td><td>1 km = 1,000 m</td></tr>
          <tr><td>1 mi = 5,280 ft</td><td>1 kg = 1,000 g</td></tr>
          <tr><td>1 lb = 16 oz · 1 gal = 4 qt</td><td>1 L = 1,000 mL</td></tr>
        </tbody>
      </table>
      <div class="caja-tip"><strong>{t("To estimate:", "Para estimar:")}</strong> {t("a meter is a little more than a yard; a kilogram, a little more than 2 pounds; a liter, a little more than a quart; a kilometer, about 0.6 miles.", "un metro es un poco más que una yarda; un kilogramo, un poco más de 2 libras; un litro, un poco más que un cuarto de galón; un kilómetro, unas 0.6 millas.")}</div>
{B.om("p2", t("Practice: does it make sense?", "Practique: ¿tiene sentido?"))}'''),
     (t("conversion-fraction", "fraccion-conversion"), t("The conversion-fraction method", "El método de la fracción de conversión"),
      f'''      <p>{t("Since 1 in and 2.54 cm are the same length, the fraction 2.54 cm / 1 in is worth 1: multiplying by it changes the unit, not the amount. <strong>Golden rule:</strong> the unit you want to get rid of goes on the bottom, so it cancels. If there is no direct factor, chain several fractions.", "Como 1 in y 2.54 cm son la misma longitud, la fracción 2.54 cm / 1 in vale 1: multiplicar por ella cambia la unidad, no la cantidad. <strong>Regla de oro:</strong> la unidad que se quiere eliminar va abajo, para que se cancele. Si no hay un factor directo, se encadenan varias fracciones.")}</p>
      <h3>{t("Build the chain", "Arme la cadena")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="fc-m">{t("Quantity", "Magnitud")}</label><select id="fc-m"><option value="long">{t("Length", "Longitud")}</option><option value="peso">{t("Weight", "Peso")}</option><option value="cap">{t("Capacity", "Capacidad")}</option></select></div>
          <div class="campo"><label for="fc-x">{t("Amount", "Cantidad")}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="fc-x" value="6"></div>
          <div class="campo"><label for="fc-de">{t("From", "De")}</label><select id="fc-de"></select></div>
          <div class="campo"><label for="fc-a">{t("To", "A")}</label><select id="fc-a"></select></div>
        </div>
        <div class="caja-aviso" id="fc-aviso" role="alert"></div>
        <div class="salida" id="fc-salida" aria-live="polite"></div>
      </div>
      <div class="caja-atencion"><strong>{t("Common mistake:", "Error frecuente:")}</strong> {t("using the fraction upside down. 10 km × 1.609 gives 16.09 “miles”, more than the kilometers, even though miles are longer. If the new unit is bigger, the number must come out smaller.", "poner la fracción al revés. 10 km × 1.609 da 16.09 «millas», más que los kilómetros, cuando las millas son más largas. Si la unidad nueva es más grande, el número tiene que salir más pequeño.")}</div>
{libre_x("p3", t("Practice: convert", "Practique: convierta"), t("Answer", "Resultado"), t("Round to two decimal places, for example 30.48.", "Redondee a dos cifras decimales, por ejemplo 30.48."))}'''),
     (t("temperature", "temperatura"), t("Temperature: a special case", "La temperatura: un caso especial"),
      f'''      <p>{t("Temperature is not converted with a single factor, because the two scales do not start at the same zero: water freezes at 0 °C, which is 32 °F. So you subtract or add 32, following the order of operations.", "La temperatura no se convierte con un solo factor, porque las dos escalas no empiezan en el mismo cero: el agua se congela a 0 °C, que son 32 °F. Por eso se resta o se suma 32, respetando el orden de operaciones.")}</p>
      <div class="formula">°C = (°F − 32) × 5 ÷ 9 &nbsp;&nbsp;&nbsp; °F = °C × 9 ÷ 5 + 32</div>
      <h3>{t("The two thermometers", "Los dos termómetros")}</h3>
      <div class="panel">
        <div class="campos">
          <div class="campo"><label for="tm-dir">{t("Convert", "Convertir")}</label><select id="tm-dir"><option value="fc">{t("from °F to °C", "de °F a °C")}</option><option value="cf">{t("from °C to °F", "de °C a °F")}</option></select></div>
          <div class="campo" style="flex:1;min-width:200px;"><label for="tm-v">{t("Temperature", "Temperatura")}: <span id="tm-vv"></span></label><input type="range" id="tm-v" min="-40" max="220" value="98.6" step="0.2"></div>
        </div>
        <div class="termo" id="tm-svg"></div>
        <div class="salida" id="tm-salida" aria-live="polite"></div>
      </div>
{libre_x("p4", t("Practice: temperature", "Practique: temperatura"), t("Degrees", "Grados"), t("Round to one decimal place if needed; use the minus sign for temperatures below zero.", "Redondee a una cifra decimal si hace falta; use el signo menos para temperaturas bajo cero."))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/rates.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Conversiones entre el sistema inglés y el métrico")
