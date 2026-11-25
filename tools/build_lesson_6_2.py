"""Lesson 6.2 · Metric system, time, and temperature — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py, tools/build_indice_es.py and tools/indice_en.py."""
import json
import bilingue as B
from bilingue import t, E, T, practica, enlace, calc, caja, ejemplo, tabla, svg

N = "6-2"

def termometro():
    """A thermometer with both scales and the reference points."""
    x, top, bot = 320, 20, 300
    def yF(f): return bot - (f - 0) * (bot - top) / 220
    s = [f'<rect x="{x - 14}" y="{top - 6}" width="28" height="{bot - top + 12}" rx="14" fill="#fff" stroke="#37474f" stroke-width="2"/>',
         f'<rect x="{x - 7}" y="{yF(98.6):.1f}" width="14" height="{bot - yF(98.6) + 8:.1f}" fill="#e53935"/>',
         f'<circle cx="{x}" cy="{bot + 20}" r="22" fill="#e53935" stroke="#37474f" stroke-width="2"/>']
    for f, c, nombre in [(212, 100, t("water boils", "el agua hierve")), (98.6, 37, t("body temperature", "temperatura del cuerpo")),
                         (70, 21, t("a comfortable room", "un cuarto agradable")), (32, 0, t("water freezes", "el agua se congela"))]:
        y = yF(f)
        s.append(f'<line x1="{x - 24}" y1="{y:.1f}" x2="{x + 24}" y2="{y:.1f}" stroke="#37474f" stroke-width="2"/>')
        s.append(f'<text x="{x - 32}" y="{y + 6:.1f}" text-anchor="end" font-size="17" font-weight="700" fill="#b71c1c">{f:g} °F</text>')
        s.append(f'<text x="{x + 32}" y="{y + 6:.1f}" font-size="17" font-weight="700" fill="#0d47a1">{c} °C</text>')
        s.append(f'<text x="{x + 100}" y="{y + 6:.1f}" font-size="15" fill="#1a2330">{nombre}</text>')
    s.append(f'<text x="{x - 32}" y="{top - 2}" text-anchor="end" font-size="15" font-weight="700" fill="#b71c1c">Fahrenheit</text><text x="{x + 32}" y="{top - 2}" font-size="15" font-weight="700" fill="#0d47a1">Celsius</text>')
    return svg("0 0 640 350", t("A thermometer with two scales. Water boils at 212 degrees Fahrenheit, which is 100 degrees Celsius. Body temperature is 98.6 degrees Fahrenheit, 37 degrees Celsius. A comfortable room is about 70 degrees Fahrenheit, 21 degrees Celsius. Water freezes at 32 degrees Fahrenheit, 0 degrees Celsius.",
                                "Un termómetro con dos escalas. El agua hierve a 212 grados Fahrenheit, que son 100 grados Celsius. La temperatura del cuerpo es 98.6 grados Fahrenheit, 37 grados Celsius. Un cuarto agradable está a unos 70 grados Fahrenheit, 21 grados Celsius. El agua se congela a 32 grados Fahrenheit, 0 grados Celsius."), "".join(s))

def recta_tiempo():
    """Counting up from 9:45 to 1:20 on a number line."""
    x0, x1, y = 40, 600, 70
    def X(minutos): return x0 + (x1 - x0) * minutos / 215
    s = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#37474f" stroke-width="3"/>']
    for m, lab in [(0, "9:45"), (15, "10:00"), (195, "1:00"), (215, "1:20")]:
        s.append(f'<line x1="{X(m):.1f}" y1="{y - 10}" x2="{X(m):.1f}" y2="{y + 10}" stroke="#37474f" stroke-width="3"/><text x="{X(m):.1f}" y="{y + 34}" text-anchor="middle" font-size="17" font-weight="700" fill="#1a2330">{lab}</text>')
    for a, b2, lab in [(0, 15, "15 min"), (15, 195, "3 h"), (195, 215, "20 min")]:
        xm = (X(a) + X(b2)) / 2
        s.append(f'<path d="M{X(a):.1f},{y - 12} Q{xm:.1f},{y - 58} {X(b2):.1f},{y - 12}" fill="none" stroke="#1565c0" stroke-width="3"/>')
        s.append(f'<text x="{xm:.1f}" y="{y - 44}" text-anchor="middle" font-size="16" font-weight="700" fill="#0d47a1">{lab}</text>')
    return svg("0 0 640 120", t("A time line from 9:45 to 1:20. A jump of 15 minutes goes from 9:45 to 10:00, a jump of 3 hours goes from 10:00 to 1:00, and a jump of 20 minutes goes from 1:00 to 1:20.",
                                "Una recta del tiempo de 9:45 a 1:20. Un salto de 15 minutos va de 9:45 a 10:00, un salto de 3 horas va de 10:00 a 1:00, y un salto de 20 minutos va de 1:00 a 1:20."), "".join(s))

def leccion():
    n = N
    s1 = f'''<p>{t("Most countries, and all of science and medicine, use the <strong>metric system</strong>. You will see it on medicine labels (mg, mL), soda bottles (2 liters), and race distances (5 km).",
"La mayoría de los países, y toda la ciencia y la medicina, usan el <strong>sistema métrico</strong>. Usted lo ve en las etiquetas de las medicinas (mg, mL), en las botellas de refresco (2 litros) y en las carreras (5 km).")}</p>
<p>{t("The metric system has one base unit for each kind of measure, and it works with <strong>tens</strong>, like our place value:", "El sistema métrico tiene una unidad base para cada tipo de medida, y trabaja con <strong>dieces</strong>, como nuestro valor posicional:")}</p>
{tabla(t("Metric base units and prefixes", "Unidades base y prefijos del sistema métrico"), t("The base units of the metric system and what each prefix means", "Las unidades base del sistema métrico y lo que significa cada prefijo"),
       [t("Measure", "Medida"), t("Base unit", "Unidad base"), "kilo- (× 1,000)", t("centi- (÷ 100)", "centi- (÷ 100)"), t("milli- (÷ 1,000)", "mili- (÷ 1,000)")],
       [[t("Length", "Longitud"), t("meter (m)", "metro (m)"), t("kilometer (km)", "kilómetro (km)"), t("centimeter (cm)", "centímetro (cm)"), t("millimeter (mm)", "milímetro (mm)")],
        [t("Mass (weight)", "Masa (peso)"), t("gram (g)", "gramo (g)"), t("kilogram (kg)", "kilogramo (kg)"), "—", t("milligram (mg)", "miligramo (mg)")],
        [t("Capacity", "Capacidad"), t("liter (L)", "litro (L)"), "—", "—", t("milliliter (mL)", "mililitro (mL)")]])}
{caja("tip", t("The key idea of this lesson", "La idea clave de esta lección"), t("<p>The prefix tells you the size. <strong>Kilo</strong> always means 1,000, <strong>centi</strong> means one hundredth, and <strong>milli</strong> means one thousandth. So converting metric units is just multiplying or dividing by 10, 100, or 1,000: <strong>moving the decimal point</strong>, as you did in Topic 3.</p>",
"<p>El prefijo le dice el tamaño. <strong>Kilo</strong> siempre quiere decir 1,000, <strong>centi</strong> quiere decir una centésima, y <strong>mili</strong> quiere decir una milésima. Así que convertir unidades métricas es solo multiplicar o dividir entre 10, 100 o 1,000: <strong>mover el punto decimal</strong>, como hizo en el Tema 3.</p>"))}
<p>{t("To get a feel for the sizes: a <strong>meter</strong> is a little longer than a yard, a <strong>kilogram</strong> is a little more than 2 pounds, and a <strong>liter</strong> is a little more than a quart.",
"Para darse una idea de los tamaños: un <strong>metro</strong> es un poco más largo que una yarda, un <strong>kilogramo</strong> es un poco más de 2 libras, y un <strong>litro</strong> es un poco más que un cuarto de galón.")}</p>'''

    s2 = f'''{tabla(t("Metric equivalences", "Equivalencias del sistema métrico"), t("The metric equivalences you will use most", "Las equivalencias métricas que más va a usar"),
       [t("Length", "Longitud"), t("Mass", "Masa"), t("Capacity", "Capacidad")],
       [["1 km = 1,000 m", "1 kg = 1,000 g", "1 L = 1,000 mL"], ["1 m = 100 cm", "1 g = 1,000 mg", ""], ["1 cm = 10 mm", "", ""]])}
<p>{t("The rule is the same as in Lesson 6.1: to a <strong>smaller</strong> unit, multiply; to a <strong>bigger</strong> unit, divide. With powers of ten, that means moving the decimal point one place for each zero.",
"La regla es la misma de la Lección 6.1: a una unidad <strong>más pequeña</strong>, multiplique; a una unidad <strong>más grande</strong>, divida. Con potencias de diez, eso es mover el punto decimal un lugar por cada cero.")}</p>
{ejemplo(t("Example: 2.5 km = ___ m", "Ejemplo: 2.5 km = ___ m"),
  [("1", t("Smaller or bigger?", "¿Más pequeña o más grande?"), t("Meters are smaller than kilometers: multiply by 1,000.", "Los metros son más pequeños que los kilómetros: multiplique por 1,000.")),
   ("2", t("Move the point 3 places to the right", "Mueva el punto 3 lugares a la derecha"), t("(1,000 has 3 zeros): 2.5 → 2,500.", "(1,000 tiene 3 ceros): 2.5 → 2,500.")),
   ("✓", t("Answer.", "Respuesta."), t("2.5 km = <strong>2,500 m</strong>.", "2.5 km = <strong>2,500 m</strong>."))])}
{ejemplo(t("Example: 350 cm = ___ m", "Ejemplo: 350 cm = ___ m"),
  [("1", t("Smaller or bigger?", "¿Más pequeña o más grande?"), t("Meters are bigger than centimeters: divide by 100.", "Los metros son más grandes que los centímetros: divida entre 100.")),
   ("2", t("Move the point 2 places to the left", "Mueva el punto 2 lugares a la izquierda"), t("(100 has 2 zeros): 350. → 3.50.", "(100 tiene 2 ceros): 350. → 3.50.")),
   ("✓", t("Answer.", "Respuesta."), t("350 cm = <strong>3.5 m</strong>.", "350 cm = <strong>3.5 m</strong>."))])}
{caja("ojo", t("Watch out! Do not mix the two systems", "¡Cuidado! No mezcle los dos sistemas"), t("<p>Inside the metric system everything is tens. Between the metric system and the U.S. system it is not: 1 inch is 2.54 cm, not 10. If a GED® problem asks you to change between systems, it will give you the equivalence.</p>",
"<p>Dentro del sistema métrico todo es de diez en diez. Entre el sistema métrico y el sistema inglés, no: 1 pulgada son 2.54 cm, no 10. Si un problema del GED® le pide pasar de un sistema al otro, le dará la equivalencia.</p>"))}
{practica("p1", t("Practice 1 — From big to small", "Práctica 1 — De grande a pequeña"), t("<strong>3.2 kg</strong> = ___ g", "<strong>3.2 kg</strong> = ___ g"),
          [("a", "32 g"), ("b", "320 g"), ("c", "3,200 g"), ("d", "32,000 g")])}
{practica("p2", t("Practice 2 — From small to big", "Práctica 2 — De pequeña a grande"), t("<strong>450 cm</strong> = ___ m", "<strong>450 cm</strong> = ___ m"),
          [("a", "4.5 m"), ("b", "45 m"), ("c", "45,000 m"), ("d", "0.45 m")])}
{enlace(n, t("metric", "metrico"), t("convert metric units", "convertir unidades métricas"), t("Move the decimal point the right number of places.", "Mueva el punto decimal el número correcto de lugares."))}'''

    s3 = f'''{tabla(t("Units of time", "Unidades de tiempo"), t("Units of time and their equivalences", "Las unidades de tiempo y sus equivalencias"),
       [t("Unit", "Unidad"), t("Equivalence", "Equivalencia")],
       [[t("minute (min)", "minuto (min)"), t("1 min = 60 seconds", "1 min = 60 segundos")], [t("hour (h)", "hora (h)"), t("1 h = 60 min", "1 h = 60 min")],
        [t("day", "día"), t("1 day = 24 h", "1 día = 24 h")], [t("week", "semana"), t("1 week = 7 days", "1 semana = 7 días")],
        [t("year", "año"), t("1 year = 12 months = 52 weeks = 365 days", "1 año = 12 meses = 52 semanas = 365 días")]])}
{caja("ojo", t("Watch out! Time does not work with tens", "¡Cuidado! El tiempo no trabaja con dieces"), t("<p>An hour has <strong>60</strong> minutes, not 100. So 1.5 hours is 1 hour and <strong>30</strong> minutes (half of 60), not 1 hour and 50 minutes. And you cannot subtract times like decimals.</p>",
"<p>Una hora tiene <strong>60</strong> minutos, no 100. Así que 1.5 horas son 1 hora y <strong>30</strong> minutos (la mitad de 60), no 1 hora y 50 minutos. Y no se pueden restar horas como si fueran decimales.</p>"))}
<p>{t("<strong>Elapsed time</strong> is how much time passes between two moments. The safest way to find it is to <strong>count up</strong> in jumps: first to the next full hour, then by whole hours, then the minutes that are left.",
"El <strong>tiempo transcurrido</strong> es cuánto tiempo pasa entre dos momentos. La forma más segura de hallarlo es <strong>contar hacia adelante</strong> a saltos: primero hasta la siguiente hora en punto, después de hora en hora, y después los minutos que faltan.")}</p>
{recta_tiempo()}
{ejemplo(t("Example: a shift starts at 9:45 a.m. and ends at 1:20 p.m. How long is it?", "Ejemplo: un turno empieza a las 9:45 a.m. y termina a la 1:20 p.m. ¿Cuánto dura?"),
  [("1", t("To the next full hour:", "Hasta la siguiente hora en punto:"), t("9:45 → 10:00 is 15 minutes.", "9:45 → 10:00 son 15 minutos.")),
   ("2", t("Whole hours:", "Horas completas:"), t("10:00 → 1:00 is 3 hours.", "10:00 → 1:00 son 3 horas.")),
   ("3", t("The minutes left:", "Los minutos que faltan:"), t("1:00 → 1:20 is 20 minutes.", "1:00 → 1:20 son 20 minutos.")),
   ("✓", t("Add the jumps.", "Sume los saltos."), t("3 h + 15 min + 20 min = <strong>3 h 35 min</strong>.", "3 h + 15 min + 20 min = <strong>3 h 35 min</strong>."))])}
{practica("p3", t("Practice 3 — Elapsed time", "Práctica 3 — Tiempo transcurrido"), t("A shift goes from <strong>7:30 a.m.</strong> to <strong>3:15 p.m.</strong> How long is it?", "Un turno va de las <strong>7:30 a.m.</strong> a las <strong>3:15 p.m.</strong> ¿Cuánto dura?"),
          [("a", "8 h 45 min"), ("b", "7 h 45 min"), ("c", "7 h 85 min"), ("d", "4 h 15 min")])}
{enlace(n, t("elapsed-time", "tiempo-transcurrido"), t("elapsed time", "tiempo transcurrido"), t("Count up in jumps from the start time to the end time.", "Cuente hacia adelante a saltos, de la hora de inicio a la hora final."))}
{enlace(n, t("time-units", "unidades-tiempo"), t("units of time", "unidades de tiempo"), t("Convert hours, minutes, days, and weeks.", "Convierta horas, minutos, días y semanas."))}'''

    s4 = f'''<p>{t("In the United States, the weather and ovens use <strong>degrees Fahrenheit</strong> (°F). Science and most countries use <strong>degrees Celsius</strong> (°C). These reference points help you picture a temperature:",
"En los Estados Unidos, el tiempo y los hornos usan <strong>grados Fahrenheit</strong> (°F). La ciencia y la mayoría de los países usan <strong>grados Celsius</strong> (°C). Estos puntos de referencia le ayudan a imaginar una temperatura:")}</p>
{termometro()}
<p>{t("To find how much the temperature <strong>changed</strong>, subtract the smaller temperature from the bigger one, as with any difference.", "Para hallar cuánto <strong>cambió</strong> la temperatura, reste la temperatura menor de la mayor, como en cualquier diferencia.")}</p>
{ejemplo(t("Example: at 6 a.m. it was 38°F. At 3 p.m. it was 61°F. How much did the temperature rise?", "Ejemplo: a las 6 a.m. hacía 38 °F. A las 3 p.m. hacía 61 °F. ¿Cuánto subió la temperatura?"),
  [("1", t("Find the difference.", "Halle la diferencia."), "61 − 38 = 23."),
   ("✓", t("Answer with the unit.", "Responda con la unidad."), t("The temperature rose <strong>23 degrees</strong> (23°F).", "La temperatura subió <strong>23 grados</strong> (23 °F)."))])}
{caja("tip", t("Reading a thermometer", "Cómo leer un termómetro"), t("<p>Before you read a thermometer, find out <strong>how much each small mark is worth</strong>. If the numbers go 40, 50, 60 and there are 5 spaces between them, each mark is 10 ÷ 5 = 2 degrees.</p>",
"<p>Antes de leer un termómetro, averigüe <strong>cuánto vale cada rayita</strong>. Si los números van 40, 50, 60 y hay 5 espacios entre ellos, cada rayita vale 10 ÷ 5 = 2 grados.</p>"))}
{practica("p4", t("Practice 4 — Temperature change", "Práctica 4 — Cambio de temperatura"), t("In the morning it was <strong>45°F</strong>. In the afternoon it was <strong>72°F</strong>. How many degrees did it rise?", "En la mañana hacía <strong>45 °F</strong>. En la tarde hacía <strong>72 °F</strong>. ¿Cuántos grados subió?"),
          [("a", t("27 degrees", "27 grados")), ("b", t("117 degrees", "117 grados")), ("c", t("33 degrees", "33 grados")), ("d", t("37 degrees", "37 grados"))])}
{enlace(n, t("thermometer", "termometro"), t("read a thermometer", "leer un termómetro"), t("Find how much each mark is worth and read the temperature.", "Averigüe cuánto vale cada rayita y lea la temperatura."))}'''

    secciones = [("s-" + t("metric", "metrico"), t("The metric system: everything in tens", "El sistema métrico: todo de diez en diez"), s1),
                 ("s-" + t("metric-convert", "convertir-metrico"), t("Convert metric units", "Convertir unidades métricas"), s2),
                 ("s-" + t("time", "tiempo"), t("Time and elapsed time", "El tiempo y el tiempo transcurrido"), s3),
                 ("s-" + t("temperature", "temperatura"), t("Temperature", "La temperatura"), s4)]

    lesson = {"next": t("Lesson 6.3", "Lección 6.3"), "review": t("sections 2, 3, and 4", "las secciones 2, 3 y 4"),
     "practice": {
      "p1": {"ok": "c", "hints": {"a": t("32 is 3.2 × 10. A kilogram is 1,000 grams: move the point 3 places.", "32 es 3.2 × 10. Un kilogramo son 1,000 gramos: mueva el punto 3 lugares."),
                                   "b": t("320 is 3.2 × 100. A kilogram is 1,000 grams, not 100.", "320 es 3.2 × 100. Un kilogramo son 1,000 gramos, no 100."),
                                   "d": t("32,000 moves the point 4 places. 1,000 has only 3 zeros.", "32,000 mueve el punto 4 lugares. 1,000 tiene solo 3 ceros.")},
             "right": t("3.2 × 1,000 = 3,200 g.", "3.2 × 1,000 = 3,200 g."), "solution": t("Grams are smaller: multiply by 1,000 (move the point 3 places to the right). 3.2 kg = 3,200 g.", "Los gramos son más pequeños: multiplique por 1,000 (mueva el punto 3 lugares a la derecha). 3.2 kg = 3,200 g.")},
      "p2": {"ok": "a", "hints": {"b": t("45 divides by 10. A meter is 100 centimeters: move the point 2 places.", "45 divide entre 10. Un metro son 100 centímetros: mueva el punto 2 lugares."),
                                   "c": t("45,000 multiplies. Meters are bigger than centimeters, so divide.", "45,000 multiplica. Los metros son más grandes que los centímetros, así que divida."),
                                   "d": t("0.45 moves the point 3 places. 100 has 2 zeros.", "0.45 mueve el punto 3 lugares. 100 tiene 2 ceros.")},
             "right": t("450 ÷ 100 = 4.5 m.", "450 ÷ 100 = 4.5 m."), "solution": t("Meters are bigger: divide by 100 (move the point 2 places to the left). 450 cm = 4.5 m.", "Los metros son más grandes: divida entre 100 (mueva el punto 2 lugares a la izquierda). 450 cm = 4.5 m.")},
      "p3": {"ok": "b", "hints": {"a": t("Count the whole hours again: 8:00 a.m. to 3:00 p.m. is 7 hours.", "Cuente otra vez las horas completas: de 8:00 a.m. a 3:00 p.m. son 7 horas."),
                                   "c": t("85 minutes is more than an hour. You subtracted like decimals; count up in jumps instead.", "85 minutos es más de una hora. Restó como si fueran decimales; mejor cuente hacia adelante a saltos."),
                                   "d": t("4 h 15 min forgets that the shift goes past noon.", "4 h 15 min olvida que el turno pasa del mediodía.")},
             "right": t("7:30 → 8:00 is 30 min, 8:00 → 3:00 is 7 h, 3:00 → 3:15 is 15 min: 7 h 45 min.", "7:30 → 8:00 son 30 min, 8:00 → 3:00 son 7 h, 3:00 → 3:15 son 15 min: 7 h 45 min."),
             "solution": t("Count up: 30 min to 8:00, 7 hours to 3:00, and 15 min to 3:15. Total: 7 h 45 min.", "Cuente hacia adelante: 30 min hasta las 8:00, 7 horas hasta las 3:00, y 15 min hasta las 3:15. Total: 7 h 45 min.")},
      "p4": {"ok": "a", "hints": {"b": t("117 is 45 + 72. To find a change, subtract.", "117 es 45 + 72. Para hallar un cambio, reste."),
                                   "c": t("Check the subtraction: 72 − 45. Borrow from the tens.", "Revise la resta: 72 − 45. Pida prestado a las decenas."),
                                   "d": t("Check the subtraction: 72 − 45 = 27.", "Revise la resta: 72 − 45 = 27.")},
             "right": t("72 − 45 = 27 degrees.", "72 − 45 = 27 grados."), "solution": t("The change is the difference: 72 − 45 = 27 degrees.", "El cambio es la diferencia: 72 − 45 = 27 grados.")}
     },
     "quiz": {
      "A": {"ok": "c", "hints": {"a": t("100 is for centi-: 1 m = 100 cm.", "100 es para centi-: 1 m = 100 cm."), "b": t("Kilo- means 1,000.", "Kilo- quiere decir 1,000."), "d": t("12 is for feet and inches, not the metric system.", "12 es para pies y pulgadas, no para el sistema métrico.")},
            "solution": t("Kilo- means 1,000: 1 km = 1,000 m.", "Kilo- quiere decir 1,000: 1 km = 1,000 m.")},
      "B": {"ok": "b", "hints": {"a": t("35,000 multiplies. Meters are bigger, so divide.", "35,000 multiplica. Los metros son más grandes, así que divida."), "c": t("35 divides by 10. Divide by 100.", "35 divide entre 10. Divida entre 100."), "d": t("0.35 divides by 1,000. 1 m = 100 cm.", "0.35 divide entre 1,000. 1 m = 100 cm.")},
            "solution": t("350 ÷ 100 = 3.5 m.", "350 ÷ 100 = 3.5 m.")},
      "C": {"ok": "d", "hints": {"a": t("240 multiplies by 100. A kilogram is 1,000 grams.", "240 multiplica por 100. Un kilogramo son 1,000 gramos."), "b": t("24 multiplies by 10. Move the point 3 places.", "24 multiplica por 10. Mueva el punto 3 lugares."), "c": t("Grams are smaller, so the number gets bigger. Multiply.", "Los gramos son más pequeños, así que el número se hace más grande. Multiplique.")},
            "solution": t("2.4 × 1,000 = 2,400 g.", "2.4 × 1,000 = 2,400 g.")},
      "D": {"ok": "a", "hints": {"b": t("300 uses 100 minutes per hour. An hour has 60 minutes.", "300 usa 100 minutos por hora. Una hora tiene 60 minutos."), "c": t("63 adds. Each hour is 60 minutes: multiply.", "63 suma. Cada hora son 60 minutos: multiplique."), "d": t("30 is half an hour. 3 hours is much more.", "30 es media hora. 3 horas es mucho más.")},
            "solution": t("3 × 60 = 180 minutes.", "3 × 60 = 180 minutos.")},
      "E": {"ok": "b", "hints": {"a": t("Count up: 9:45 to 10:00 is only 15 minutes, then 3 whole hours to 1:00.", "Cuente hacia adelante: de 9:45 a 10:00 son solo 15 minutos, y después 3 horas completas hasta la 1:00."), "c": t("75 minutes is more than an hour. Count up in jumps.", "75 minutos es más de una hora. Cuente hacia adelante a saltos."), "d": t("10:00 to 1:00 is 3 hours, not 4.", "De 10:00 a 1:00 son 3 horas, no 4.")},
            "solution": t("15 min (to 10:00) + 3 h (to 1:00) + 20 min (to 1:20) = 3 h 35 min.", "15 min (hasta las 10:00) + 3 h (hasta la 1:00) + 20 min (hasta la 1:20) = 3 h 35 min.")},
      "F": {"ok": "d", "hints": {"a": t("Time is not base ten: half an hour is 30 minutes, not 50.", "El tiempo no es de base diez: media hora son 30 minutos, no 50."), "b": t("0.5 hour is half of 60 minutes.", "0.5 hora es la mitad de 60 minutos."), "c": t("1.5 hours is more than 1 hour.", "1.5 horas es más de 1 hora.")},
            "solution": t("0.5 hour = half of 60 minutes = 30 minutes. So 1.5 hours = 1 h 30 min.", "0.5 hora = la mitad de 60 minutos = 30 minutos. Así que 1.5 horas = 1 h 30 min.")},
      "G": {"ok": "c", "hints": {"a": t("0° is where water freezes on the Celsius scale, not Fahrenheit.", "0° es donde el agua se congela en la escala Celsius, no en la Fahrenheit."), "b": t("100° is where water boils on the Celsius scale.", "100° es donde el agua hierve en la escala Celsius."), "d": t("212°F is where water boils.", "212 °F es donde el agua hierve.")},
            "solution": t("Water freezes at 32°F, which is 0°C.", "El agua se congela a 32 °F, que son 0 °C.")},
      "H": {"ok": "a", "hints": {"b": t("123 is 48 + 75. A change is a difference: subtract.", "123 es 48 + 75. Un cambio es una diferencia: reste."), "c": t("Check the subtraction: 75 − 48. Borrow from the tens.", "Revise la resta: 75 − 48. Pida prestado a las decenas."), "d": t("Check the subtraction: 75 − 48 = 27.", "Revise la resta: 75 − 48 = 27.")},
            "solution": t("75 − 48 = 27 degrees.", "75 − 48 = 27 grados.")}
     }}

    quiz = [
     ("A", t("How many meters are in <strong>1 kilometer</strong>?", "¿Cuántos metros hay en <strong>1 kilómetro</strong>?"), [("a", "100"), ("b", "10"), ("c", "1,000"), ("d", "12")]),
     ("B", "<strong>350 cm</strong> = ___ m", [("a", "35,000"), ("b", "3.5"), ("c", "35"), ("d", "0.35")]),
     ("C", "<strong>2.4 kg</strong> = ___ g", [("a", "240"), ("b", "24"), ("c", "0.0024"), ("d", "2,400")]),
     ("D", t("<strong>3 hours</strong> = ___ minutes", "<strong>3 horas</strong> = ___ minutos"), [("a", "180"), ("b", "300"), ("c", "63"), ("d", "30")]),
     ("E", t("A shift starts at <strong>9:45 a.m.</strong> and ends at <strong>1:20 p.m.</strong> How long is it?", "Un turno empieza a las <strong>9:45 a.m.</strong> y termina a la <strong>1:20 p.m.</strong> ¿Cuánto dura?"), [("a", "4 h 25 min"), ("b", "3 h 35 min"), ("c", "3 h 75 min"), ("d", "4 h 35 min")]),
     ("F", t("<strong>1.5 hours</strong> is the same as:", "<strong>1.5 horas</strong> es lo mismo que:"), [("a", "1 h 50 min"), ("b", "1 h 5 min"), ("c", "15 min"), ("d", "1 h 30 min")]),
     ("G", t("Water freezes at:", "El agua se congela a:"), [("a", "0 °F"), ("b", "100 °F"), ("c", "32 °F"), ("d", "212 °F")]),
     ("H", t("In the morning it was <strong>48°F</strong>. In the afternoon it was <strong>75°F</strong>. How many degrees did it rise?", "En la mañana hacía <strong>48 °F</strong>. En la tarde hacía <strong>75 °F</strong>. ¿Cuántos grados subió?"),
      [("a", t("27 degrees", "27 grados")), ("b", t("123 degrees", "123 grados")), ("c", t("33 degrees", "33 grados")), ("d", t("37 degrees", "37 grados"))])]

    return B.pagina_leccion(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"),
        t("Metric system, time, and temperature", "Sistema métrico, tiempo y temperatura"),
        t("Meters, liters, and grams work with tens. Time works with sixties. Learn both, and how to read a thermometer.", "Metros, litros y gramos trabajan con dieces. El tiempo trabaja con sesentas. Aprenda los dos, y a leer un termómetro."),
        ("🌡️", t("Tens and sixties", "Dieces y sesentas")),
        [t("<strong>Use</strong> the metric units of length, mass, and capacity and their prefixes.", "<strong>Usar</strong> las unidades métricas de longitud, masa y capacidad y sus prefijos."),
         t("<strong>Convert</strong> metric units by moving the decimal point.", "<strong>Convertir</strong> unidades métricas moviendo el punto decimal."),
         t("<strong>Convert</strong> units of time and find elapsed time.", "<strong>Convertir</strong> unidades de tiempo y hallar el tiempo transcurrido."),
         t("<strong>Read</strong> a thermometer and find a change in temperature.", "<strong>Leer</strong> un termómetro y hallar un cambio de temperatura.")],
        secciones,
        (t("Find three metric measures at home (a soda bottle, a medicine, a food label). Convert each one to a smaller or a bigger metric unit. Then write down the start and end times of three activities in your day and find how long each one lasted.",
           "Busque tres medidas métricas en su casa (una botella de refresco, una medicina, una etiqueta de comida). Convierta cada una a una unidad métrica más pequeña o más grande. Después anote la hora de inicio y la hora final de tres actividades de su día y halle cuánto duró cada una."),
         t("Check the weather forecast for this week. Write the high and the low temperature for each day, and find how much the temperature changes each day.",
           "Mire el pronóstico del tiempo de esta semana. Anote la temperatura más alta y la más baja de cada día, y halle cuánto cambia la temperatura cada día.")),
        quiz,
        t("Self-check checklist for the metric system, time, and temperature", "Lista de autoevaluación del sistema métrico, el tiempo y la temperatura"),
        t("Self-check checklist: skills for the metric system, time, and temperature", "Lista de autoevaluación: destrezas con el sistema métrico, el tiempo y la temperatura"),
        [(t("Metric units and prefixes", "Unidades y prefijos métricos"), t("I know what kilo, centi, and milli mean and use the right unit.", "Sé lo que quieren decir kilo, centi y mili, y uso la unidad correcta."), t("I know some prefixes.", "Me sé algunos prefijos."), t("I mix up the prefixes.", "Confundo los prefijos.")),
         (t("Convert metric units", "Convertir unidades métricas"), t("I move the decimal point the right way and the right number of places.", "Muevo el punto decimal hacia el lado correcto y el número correcto de lugares."), t("I get the direction right, but sometimes not the number of places.", "Acierto la dirección, pero a veces no el número de lugares."), t("I am not sure whether to multiply or divide.", "No estoy seguro de si multiplicar o dividir.")),
         (t("Time and elapsed time", "Tiempo y tiempo transcurrido"), t("I convert units of time and find elapsed time by counting up.", "Convierto unidades de tiempo y hallo el tiempo transcurrido contando hacia adelante."), t("I find elapsed time when it does not pass noon.", "Hallo el tiempo transcurrido cuando no pasa del mediodía."), t("I subtract times like decimals.", "Resto las horas como si fueran decimales.")),
         (t("Temperature", "Temperatura"), t("I read a thermometer and find temperature changes.", "Leo un termómetro y hallo cambios de temperatura."), t("I read it when each mark is 1 degree.", "Lo leo cuando cada rayita vale 1 grado."), t("I do not check what each mark is worth.", "No reviso cuánto vale cada rayita."))],
        t("<p>You can now work with metric units, time, and temperature. Together with Lesson 6.1, you have all the units you need for the GED® test.</p>\n<p>In <strong>Lesson 6.3 · Applied measurement problems</strong> you will use all these units in real problems with several steps: recipes, trips, work schedules, and projects at home.</p>",
          "<p>Ya sabe trabajar con unidades métricas, con el tiempo y con la temperatura. Junto con la Lección 6.1, ya tiene todas las unidades que necesita para el examen de GED®.</p>\n<p>En la <strong>Lección 6.3 · Problemas aplicados de medición en contexto real</strong> usará todas estas unidades en problemas reales de varios pasos: recetas, viajes, horarios de trabajo y proyectos en la casa.</p>"),
        ("6-3", ("", t("Lesson 6.3 · Applied measurement problems", "Lección 6.3 · Problemas aplicados de medición en contexto real"))),
        [(t("metric system", "sistema métrico"), t("A system of units based on tens: meter, gram, liter.", "Un sistema de unidades basado en dieces: metro, gramo, litro.")),
         (t("prefix", "prefijo"), t("The first part of a unit's name that tells its size: kilo- (1,000), centi- (one hundredth), milli- (one thousandth).", "La primera parte del nombre de una unidad, que dice su tamaño: kilo- (1,000), centi- (una centésima), mili- (una milésima).")),
         (t("mass", "masa"), t("How much matter something has. In daily life we call it weight; we measure it in grams and kilograms.", "Cuánta materia tiene algo. En la vida diaria le decimos peso; se mide en gramos y kilogramos.")),
         (t("elapsed time", "tiempo transcurrido"), t("The time that passes between a start time and an end time.", "El tiempo que pasa entre una hora de inicio y una hora final.")),
         (t("degree", "grado"), t("The unit of temperature: °F (Fahrenheit) or °C (Celsius).", "La unidad de temperatura: °F (Fahrenheit) o °C (Celsius)."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "u": {"km": ["kilometer", "kilometers"], "m": ["meter", "meters"], "cm": ["centimeter", "centimeters"], "mm": ["millimeter", "millimeters"], "kg": ["kilogram", "kilograms"], "g": ["gram", "grams"], "mg": ["milligram", "milligrams"], "L": ["liter", "liters"], "mL": ["milliliter", "milliliters"],
        "s": ["second", "seconds"], "min": ["minute", "minutes"], "h": ["hour", "hours"], "d": ["day", "days"], "w": ["week", "weeks"], "mo": ["month", "months"], "y": ["year", "years"]},
  "cuantos": {}, "cuantosDef": "How many",
  "preg": "{c} <strong>{u2}</strong> are in <strong>{n} {u1}</strong>?",
  "solMult": "The {u2b} is a smaller unit than the {u1b}: multiply by {f}. {n} × {f} = <strong>{r}</strong> {u2}.",
  "solDiv": "The {u2b} is a bigger unit than the {u1b}: divide by {f}. {n} ÷ {f} = <strong>{r}</strong> {u2}.",
  "lugares": "You moved the decimal point the wrong number of places. {f} has {z} zeros: move it {z} places.",
  "alReves": "You went the wrong way. To a smaller unit, multiply; to a bigger unit, divide.",
  "cien": "An hour has 60 minutes, not 100.",
  "pistaMet": "Find the equivalence and decide: multiply or divide?",
  "invalido": "Type a number. You can use a decimal point, like 3.5.",
  "pregTrans": "How much time passes from <strong>{a}</strong> to <strong>{b}</strong>?",
  "la": "", "las": "", "durH": "{h} h",
  "dur": "{h} h {m} min",
  "salto1": "{a} → {c}: {m} min.", "saltoH": "{c} → {d}: {h} h.", "salto2": "{d} → {b}: {m} min.",
  "total": "Total: {r}.",
  "pistaDecimal": "Time does not work with tens: an hour has 60 minutes. Count up in jumps instead of subtracting.",
  "pistaHora": "Count the whole hours again.",
  "pistaMin": "Count the minutes again: first to the next full hour, then the minutes left at the end.",
  "pistaTrans": "Count up: to the next full hour, then whole hours, then the minutes left.",
  "am": "a.m.", "pm": "p.m.",
  "pregTerm": "What temperature does the thermometer show?",
  "ariaTerm": "A thermometer from {lo} to {hi} degrees {u}. The numbers go up by 10, and there are 5 small spaces between them. The liquid reaches {k} small marks above the {base} line.",
  "bienTerm": "The numbers go up by 10 with 5 spaces, so each mark is worth 2 degrees. The liquid is {k} marks above {base}: {base} + {k} × 2 = {v}{u}.",
  "bienTerm0": "The liquid is right on the {base} line: {v}{u}.",
  "pistaUno": "Each small mark is not 1 degree. There are 5 spaces between 10 degrees: 10 ÷ 5 = 2.",
  "pistaDiez": "Look at which numbered line is just below the liquid.",
  "pistaTerm": "First find how much each small mark is worth."
 },
 "es": {
  "u": {"km": ["kilómetro", "kilómetros"], "m": ["metro", "metros"], "cm": ["centímetro", "centímetros"], "mm": ["milímetro", "milímetros"], "kg": ["kilogramo", "kilogramos"], "g": ["gramo", "gramos"], "mg": ["miligramo", "miligramos"], "L": ["litro", "litros"], "mL": ["mililitro", "mililitros"],
        "s": ["segundo", "segundos"], "min": ["minuto", "minutos"], "h": ["hora", "horas"], "d": ["día", "días"], "w": ["semana", "semanas"], "mo": ["mes", "meses"], "y": ["año", "años"]},
  "cuantos": {"h": "Cuántas", "w": "Cuántas"}, "cuantosDef": "Cuántos",
  "preg": "¿{c} <strong>{u2}</strong> hay en <strong>{n} {u1}</strong>?",
  "solMult": "La unidad «{u2b}» es más pequeña que la unidad «{u1b}»: multiplique por {f}. {n} × {f} = <strong>{r}</strong> {u2}.",
  "solDiv": "La unidad «{u2b}» es más grande que la unidad «{u1b}»: divida entre {f}. {n} ÷ {f} = <strong>{r}</strong> {u2}.",
  "lugares": "Movió el punto decimal un número equivocado de lugares. {f} tiene {z} ceros: muévalo {z} lugares.",
  "alReves": "Fue hacia el lado equivocado. A una unidad más pequeña, multiplique; a una más grande, divida.",
  "cien": "Una hora tiene 60 minutos, no 100.",
  "pistaMet": "Busque la equivalencia y decida: ¿multiplicar o dividir?",
  "invalido": "Escriba un número. Puede usar el punto decimal, como en 3.5.",
  "pregTrans": "¿Cuánto tiempo pasa de {la1}<strong>{a}</strong> a {la2}<strong>{b}</strong>?",
  "la": "la ", "las": "las ", "durH": "{h} h",
  "dur": "{h} h {m} min",
  "salto1": "{a} → {c}: {m} min.", "saltoH": "{c} → {d}: {h} h.", "salto2": "{d} → {b}: {m} min.",
  "total": "Total: {r}.",
  "pistaDecimal": "El tiempo no trabaja con dieces: una hora tiene 60 minutos. Cuente hacia adelante a saltos en vez de restar.",
  "pistaHora": "Cuente otra vez las horas completas.",
  "pistaMin": "Cuente otra vez los minutos: primero hasta la siguiente hora en punto, y después los minutos que faltan al final.",
  "pistaTrans": "Cuente hacia adelante: hasta la siguiente hora en punto, después las horas completas, y después los minutos que faltan.",
  "am": "a.m.", "pm": "p.m.",
  "pregTerm": "¿Qué temperatura marca el termómetro?",
  "ariaTerm": "Un termómetro de {lo} a {hi} grados {u}. Los números suben de 10 en 10, y hay 5 espacios pequeños entre ellos. El líquido llega {k} rayitas arriba de la línea del {base}.",
  "bienTerm": "Los números suben de 10 en 10 con 5 espacios, así que cada rayita vale 2 grados. El líquido está {k} rayitas arriba del {base}: {base} + {k} × 2 = {v}{u}.",
  "bienTerm0": "El líquido está justo en la línea del {base}: {v}{u}.",
  "pistaUno": "Cada rayita no vale 1 grado. Hay 5 espacios entre 10 grados: 10 ÷ 5 = 2.",
  "pistaDiez": "Fíjese en qué línea con número queda justo debajo del líquido.",
  "pistaTerm": "Primero averigüe cuánto vale cada rayita."
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(m, k){ return o[k]; }); }
function cuantos(k){ return TXT.cuantos[k] || TXT.cuantosDef; }
function nd(x){ var r = Math.round(x * 1000) / 1000, p = String(r).split("."); return com(p[0]) + (p[1] ? "." + p[1] : ""); }
/* typed number that may have decimals */
function numD(res, pistas, general){
  return function(t){
    var s = String(t).replace(/[\s,]/g, "");
    if (!/^\d*\.?\d+$/.test(s)) return { estado: "invalido", msg: TXT.invalido };
    var v = parseFloat(s), cerca = function(a){ return Math.abs(v - a) < 1e-9; };
    if (cerca(res)) return { estado: "bien" };
    for (var i = 0; i < pistas.length; i++) if (cerca(pistas[i].v)) return { estado: "mal", msg: pistas[i].msg };
    return { estado: "mal", msg: general };
  };
}
function convierte(par, n, k){
  /* par = [big, small, factor]; k = how many big units (may have decimals); n = true: big → small */
  var big = par[0], small = par[1], f = par[2], z = String(f).length - 1, p = [];
  var o = { f: com(f), z: z };
  if (n){
    var r = k * f;
    p.push({ v: k / f, msg: TXT.alReves }); p.push({ v: r * 10, msg: F(TXT.lugares, o) }); p.push({ v: r / 10, msg: F(TXT.lugares, o) });
    if (f === 60) p.push({ v: k * 100, msg: TXT.cien });
    return { enun: F(TXT.preg, { c: cuantos(small), u2: TXT.u[small][1], n: nd(k), u1: TXT.u[big][k === 1 ? 0 : 1] }),
      solucion: F(TXT.solMult, { u2b: TXT.u[small][0], u1b: TXT.u[big][0], f: com(f), n: nd(k), r: nd(r), u2: TXT.u[small][1] }),
      evalua: numD(r, p.filter(function(x){ return Math.abs(x.v - r) > 1e-9; }), TXT.pistaMet) };
  }
  var s = k * f;
  p.push({ v: s * f, msg: TXT.alReves }); p.push({ v: k * 10, msg: F(TXT.lugares, o) }); p.push({ v: k / 10, msg: F(TXT.lugares, o) });
  if (f === 60) p.push({ v: s / 100, msg: TXT.cien });
  return { enun: F(TXT.preg, { c: cuantos(big), u2: TXT.u[big][1], n: nd(s), u1: TXT.u[small][s === 1 ? 0 : 1] }),
    solucion: F(TXT.solDiv, { u2b: TXT.u[big][0], u1b: TXT.u[small][0], f: com(f), n: nd(s), r: nd(k), u2: TXT.u[big][1] }),
    evalua: numD(k, p.filter(function(x){ return Math.abs(x.v - k) > 1e-9; }), TXT.pistaMet) };
}

/* ============ MODULE 1 · metric ============ */
var MET = [["km", "m", 1000], ["m", "cm", 100], ["cm", "mm", 10], ["m", "mm", 1000], ["kg", "g", 1000], ["g", "mg", 1000], ["L", "mL", 1000]];
function genMet(){
  var par = elige(MET), k = Math.random() < 0.5 ? aleatorio(2, 12) : aleatorio(11, 99) / 10;
  if (par[2] === 10 && k !== Math.round(k)) k = Math.round(k);
  return convierte(par, Math.random() < 0.5, k);
}

/* ============ MODULE 2 · elapsed time ============ */
function hora(m){ m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mi = m % 60, h12 = h % 12 === 0 ? 12 : h % 12;
  return h12 + ":" + (mi < 10 ? "0" : "") + mi + " " + (h < 12 ? TXT.am : TXT.pm); }
function hm(h, m){ return F(m === 0 ? TXT.durH : TXT.dur, { h: h, m: m }); }
function art(m){ return Math.floor((m % 720) / 60) === 1 ? TXT.la : TXT.las; }
function genTrans(){
  var ini = aleatorio(24, 40) * 15 + elige([0, 5, 10, 20, 25, 35, 40, 50]), dur = aleatorio(10, 60) * 5 + 60, fin = ini + dur;
  ini = ini % 1440; fin = ini + dur;
  var h = Math.floor(dur / 60), m = dur % 60, cor = hm(h, m), op = [{ html: cor, clave: "ok" }], pistas = {};
  function mete(hh, mm, msg){ if (hh < 0 || mm < 0) return; var x = hm(hh, mm); if (op.some(function(o){ return o.html === x; })) return; op.push({ html: x, clave: "k" + op.length }); pistas["k" + (op.length - 1)] = msg; }
  var a24 = Math.floor(ini / 60) * 100 + ini % 60, b24 = Math.floor((fin % 1440) / 60) * 100 + fin % 60, ing = b24 - a24;
  if (ing > 0 && ing % 100 !== m) mete(Math.floor(ing / 100), ing % 100, TXT.pistaDecimal);
  mete(h + 1, m, TXT.pistaHora); mete(h - 1, m, TXT.pistaHora);
  if (op.length < 4) mete(h, (m + 20) % 60, TXT.pistaMin);
  var c = Math.ceil(ini / 60) * 60, d = Math.floor(fin / 60) * 60, pasos = [];
  if (c > fin || d < c){ pasos.push(F(TXT.total, { r: cor })); }
  else {
    if (c > ini) pasos.push(F(TXT.salto1, { a: hora(ini), c: hora(c), m: c - ini }));
    if (d > c) pasos.push(F(TXT.saltoH, { c: hora(c), d: hora(d), h: (d - c) / 60 }));
    if (fin > d) pasos.push(F(TXT.salto2, { d: hora(d), b: hora(fin), m: fin - d }));
    pasos.push(F(TXT.total, { r: cor }));
  }
  var txt = pasos.join(" ");
  return { enun: F(TXT.pregTrans, { a: hora(ini), b: hora(fin), la1: art(ini), la2: art(fin) }), opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaTrans, bien: txt, mal: txt };
}

/* ============ MODULE 3 · units of time ============ */
var TIE = [["h", "min", 60, 12], ["min", "s", 60, 10], ["d", "h", 24, 7], ["w", "d", 7, 12], ["y", "mo", 12, 10], ["y", "w", 52, 5]];
function genTiempo(){ var par = elige(TIE); return convierte(par, Math.random() < 0.5, aleatorio(2, par[3])); }

/* ============ MODULE 4 · thermometer ============ */
function genTerm(){
  var base0 = elige([0, 10, 20, 30, 40, 50]), lo = base0, hi = base0 + 50, v = lo + 2 * aleatorio(2, 23), u = Math.random() < 0.7 ? " °F" : " °C";
  var base = Math.floor(v / 10) * 10, k = (v - base) / 2;
  var x = 300, top = 20, bot = 300, Y = function(g){ return bot - (g - lo) * (bot - top) / 50; }, s = "";
  s += '<rect x="' + (x - 14) + '" y="' + (top - 8) + '" width="28" height="' + (bot - top + 16) + '" rx="14" fill="#fff" stroke="#37474f" stroke-width="2"/>';
  s += '<rect x="' + (x - 7) + '" y="' + f1(Y(v)) + '" width="14" height="' + f1(bot - Y(v) + 10) + '" fill="#e53935"/><circle cx="' + x + '" cy="' + (bot + 22) + '" r="22" fill="#e53935" stroke="#37474f" stroke-width="2"/>';
  for (var g = lo; g <= hi; g += 2){ var y = Y(g), larga = g % 10 === 0;
    s += linea([x + 14, y], [x + (larga ? 44 : 30), y], "#37474f", larga ? 3 : 1.5);
    if (larga) s += texto([x + 70, y], g, 18, "#1a2330"); }
  var svg = '<svg class="figura" viewBox="220 0 170 350" role="img" aria-label="' + F(TXT.ariaTerm, { lo: lo, hi: hi, u: u.trim(), k: k, base: base }) + '">' + s + '</svg>';
  var op = [{ html: v + u, clave: "ok" }], pistas = {};
  function mete(w, msg){ if (w < lo || w > hi || w === v || op.some(function(o){ return o.html === w + u; })) return; op.push({ html: w + u, clave: "k" + op.length }); pistas["k" + (op.length - 1)] = msg; }
  mete(base + k, TXT.pistaUno); mete(v + 10, TXT.pistaDiez); mete(v - 10, TXT.pistaDiez); mete(v + 2, TXT.pistaTerm); mete(v - 2, TXT.pistaTerm);
  op = op.slice(0, 4);
  var txt = k === 0 ? F(TXT.bienTerm0, { base: base, v: v, u: u }) : F(TXT.bienTerm, { k: k, base: base, v: v, u: u });
  return { enun: TXT.pregTerm + svg, opciones: op, correcta: "ok", pistas: pistas, pista: TXT.pistaTerm, bien: txt, mal: txt };
}

creaPracticaLibre("p1", genMet);
creaPracticaOM("p2", genTrans);
creaPracticaLibre("p3", genTiempo);
creaPracticaOM("p4", genTerm);
'''

def practica_pagina():
    n = N
    mods = [
     (t("metric", "metrico"), t("Convert metric units", "Convertir unidades métricas"),
      f'''      <table class="reglas">
        <caption>{t("Metric equivalences", "Equivalencias métricas")}</caption>
        <thead><tr><th scope="col">{t("Length", "Longitud")}</th><th scope="col">{t("Mass", "Masa")}</th><th scope="col">{t("Capacity", "Capacidad")}</th></tr></thead>
        <tbody>
          <tr><td>1 km = 1,000 m</td><td>1 kg = 1,000 g</td><td>1 L = 1,000 mL</td></tr>
          <tr><td>1 m = 100 cm = 1,000 mm</td><td>1 g = 1,000 mg</td><td></td></tr>
          <tr><td>1 cm = 10 mm</td><td></td><td></td></tr>
        </tbody>
      </table>
      <div class="caja-atencion"><strong>{t("To a smaller unit: multiply (the point moves right). To a bigger unit: divide (the point moves left).", "A una unidad más pequeña: multiplique (el punto se mueve a la derecha). A una más grande: divida (el punto se mueve a la izquierda).")}</strong> {t("Move one place for each zero: 1,000 has 3 zeros.", "Mueva un lugar por cada cero: 1,000 tiene 3 ceros.")}</div>
{B.libre("p1", t("Practice: convert", "Practique: convertir"), t("Answer", "Respuesta"), nota=False)}
      <p class="nota">{t("Type only the number. You can use a decimal point, like 3.5.", "Escriba solo el número. Puede usar el punto decimal, como en 3.5.")}</p>'''),
     (t("elapsed-time", "tiempo-transcurrido"), t("Elapsed time", "Tiempo transcurrido"),
      f'''      <p>{t("Count up in jumps: from the start time to the next full hour, then whole hours, then the minutes left. Example: 9:45 → 10:00 (15 min) → 1:00 (3 h) → 1:20 (20 min). Total: 3 h 35 min.", "Cuente hacia adelante a saltos: de la hora de inicio a la siguiente hora en punto, después las horas completas, y después los minutos que faltan. Ejemplo: 9:45 → 10:00 (15 min) → 1:00 (3 h) → 1:20 (20 min). Total: 3 h 35 min.")}</p>
{B.om("p2", t("Practice: how much time passes?", "Practique: ¿cuánto tiempo pasa?"))}'''),
     (t("time-units", "unidades-tiempo"), t("Units of time", "Unidades de tiempo"),
      f'''      <table class="reglas">
        <caption>{t("Units of time", "Unidades de tiempo")}</caption>
        <tbody>
          <tr><td>{t("1 minute = 60 seconds", "1 minuto = 60 segundos")}</td><td>{t("1 hour = 60 minutes", "1 hora = 60 minutos")}</td></tr>
          <tr><td>{t("1 day = 24 hours", "1 día = 24 horas")}</td><td>{t("1 week = 7 days", "1 semana = 7 días")}</td></tr>
          <tr><td>{t("1 year = 12 months", "1 año = 12 meses")}</td><td>{t("1 year = 52 weeks", "1 año = 52 semanas")}</td></tr>
        </tbody>
      </table>
{B.libre("p3", t("Practice: convert units of time", "Practique: convertir unidades de tiempo"), t("Answer", "Respuesta"))}'''),
     (t("thermometer", "termometro"), t("Read a thermometer", "Leer un termómetro"),
      f'''      <p>{t("First find how much each small mark is worth. On these thermometers the numbers go up by 10, with 5 spaces between them: each mark is 10 ÷ 5 = <strong>2 degrees</strong>.", "Primero averigüe cuánto vale cada rayita. En estos termómetros los números suben de 10 en 10, con 5 espacios entre ellos: cada rayita vale 10 ÷ 5 = <strong>2 grados</strong>.")}</p>
{B.om("p4", t("Practice: read the temperature", "Practique: leer la temperatura"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 6, t("Measurement and time", "Sistemas de medidas y el tiempo"), t("Metric system, time, and temperature", "Sistema métrico, tiempo y temperatura"),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, estilo=".enun svg.figura{display:block;width:100%;max-width:220px;height:auto;margin:10px auto;}")

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Sistema métrico, tiempo y temperatura")
