"""LearnGED · Estudios sociales · Lección 2.3 · Porcentajes, tasas, escalas de mapas y densidad (EN/ES).
Fuente: sociales/soc-2-3.html. El mapa inventado y las gráficas se dibujan aquí.
Uso: python3 tools/build_soc_2_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, cita

N = "2-3"
TER = [("A", 120000, 400), ("B", 90000, 150), ("C", 250000, 1250)]
F = 'font-family="Segoe UI, Arial, sans-serif"'


def titulo():
    return t("Percents, rates, map scales, and population density", "Porcentajes, tasas, escalas de mapas y densidad de población")


def svg_mapa():
    aria = t("Invented practice map of a small town, not a real place. A river crosses from top to bottom on the left. Two main streets cross in the center. The school is in the upper left and the clinic in the lower right; a dashed line joins them. In the corner, the scale: 1 : 50,000, and a scale bar divided into 0, 1, and 2 kilometers.",
             "Mapa inventado de un pueblo pequeño para practicar; no es un lugar real. Un río lo cruza de arriba abajo por la izquierda. Dos calles principales se cruzan en el centro. La escuela está arriba a la izquierda y la clínica abajo a la derecha; una línea de trazos las une. En una esquina, la escala: 1 : 50,000, y una barra de escala dividida en 0, 1 y 2 kilómetros.")
    s = [f'<svg class="diagrama" style="max-width:640px" viewBox="0 0 640 400" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">',
         '<rect x="1" y="1" width="638" height="398" rx="10" fill="#f6f3ea" stroke="#c9b3a2"/>',
         '<path d="M120 0 C 90 90, 160 150, 110 230 S 140 360, 100 400" fill="none" stroke="#8cc3d6" stroke-width="22"/>',
         '<line x1="0" y1="190" x2="640" y2="190" stroke="#fff" stroke-width="14"/><line x1="0" y1="190" x2="640" y2="190" stroke="#cfc6b6" stroke-width="2" stroke-dasharray="10 8"/>',
         '<line x1="360" y1="0" x2="360" y2="400" stroke="#fff" stroke-width="14"/><line x1="360" y1="0" x2="360" y2="400" stroke="#cfc6b6" stroke-width="2" stroke-dasharray="10 8"/>',
         '<rect x="420" y="40" width="70" height="40" fill="#dfe8d6"/><rect x="200" y="250" width="90" height="50" fill="#dfe8d6"/>',
         f'<text x="108" y="120" {F} font-size="13" fill="#2b6a80" transform="rotate(-70 108 120)">{t("River", "Río")}</text>',
         f'<text x="590" y="182" text-anchor="end" {F} font-size="12" fill="#5b6675">{t("Main St.", "Calle Mayor")}</text>',
         f'<text x="372" y="24" {F} font-size="12" fill="#5b6675">{t("Central Ave.", "Av. Central")}</text>',
         '<line x1="215" y1="95" x2="470" y2="290" stroke="#7a4a2e" stroke-width="2.5" stroke-dasharray="7 5"/>',
         '<rect x="200" y="80" width="30" height="30" rx="4" fill="#3949ab"/>', f'<text x="215" y="70" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330">{t("School", "Escuela")}</text>',
         '<rect x="455" y="275" width="30" height="30" rx="4" fill="#b8532c"/><path d="M470 281 v18 M461 290 h18" stroke="#fff" stroke-width="4"/>', f'<text x="446" y="296" text-anchor="end" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Clinic", "Clínica")}</text>',
         '<rect x="410" y="326" width="216" height="62" rx="8" fill="#fff" stroke="#c9b3a2"/>',
         f'<text x="422" y="345" {F} font-size="13" font-weight="700" fill="#1a2330">{t("Scale", "Escala")} 1 : 50,000</text>',
         f'<text x="430" y="362" text-anchor="middle" {F} font-size="12" fill="#1a2330">0</text><text x="510" y="362" text-anchor="middle" {F} font-size="12" fill="#1a2330">1</text><text x="590" y="362" text-anchor="middle" {F} font-size="12" fill="#1a2330">2 km</text>',
         '<rect x="430" y="368" width="80" height="8" fill="#1a2330"/><rect x="510" y="368" width="80" height="8" fill="#fff" stroke="#1a2330"/>',
         f'<text x="306" y="55" {F} font-size="22" font-weight="700" fill="#1a2330">N ↑</text>',
         "</svg>"]
    return "".join(s)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("There is only one formula, and it is worth writing the same way every time:", "La fórmula es una sola y conviene escribirla siempre igual:")}</p>
<p class="formula" style="font-size:1.2em;text-align:center"><strong>{t("percent change", "cambio porcentual")} = ( {t("new value", "valor nuevo")} − {t("old value", "valor viejo")} ) ÷ <mark>{t("old value", "valor viejo")}</mark> × 100</strong></p>
<p>{t("The highlighted part is the only thing people get wrong. You divide by the value you <strong>start from</strong>: not by the value you end at, not by the difference, and not by the sum of the two.", "Lo resaltado es lo único que se falla. Se divide entre el valor <strong>del que se parte</strong>: no entre el de llegada, ni entre la diferencia, ni entre la suma de los dos.")}</p>
{C.ejemplo(t("Why the base changes everything", "Por qué la base lo cambia todo"),
  [("1", t("An item costs $80. It goes up 25%: 80 × 1.25 = <strong>$100</strong>.", "Un artículo cuesta 80 dólares. Sube un 25 %: 80 × 1.25 = <strong>100 dólares</strong>.")),
   ("2", t("The next month it goes down 25%: 100 × 0.75 = <strong>$75</strong>.", "Al mes siguiente baja un 25 %: 100 × 0.75 = <strong>75 dólares</strong>.")),
   ("3", t("It does not go back to $80. The increase was figured on 80 and the decrease on 100: the same percent of different bases gives different amounts.", "No vuelve a 80. La subida se calculó sobre 80 y la bajada sobre 100: el mismo porcentaje de bases distintas da cantidades distintas."))],
  t("To go back from 100 to 80 you would need a 20% decrease, not 25%.", "Para volver de 100 a 80 haría falta bajar un 20 %, no un 25 %."))}
{C.caja("tip", t("The question that prevents the mistake", "La pregunta que evita el error"), "<p>" + t("Before you divide, ask out loud: <strong>a percent of what?</strong> The answer to that question is what you divide by.", "Antes de dividir, pregúntese en voz alta: <strong>¿un tanto por ciento de qué?</strong> La respuesta a esa pregunta es el denominador.") + "</p>")}
{P(t("Practice 1 · The right base", "Práctica 1 · La base correcta"), t("A rent goes up from $400 to $520. What is the percent change?", "Un alquiler sube de 400 a 520 dólares. ¿Cuál es el cambio porcentual?"),
   [t("12%, because it went up 120", "12 %, porque subió 120"), "30%", "23%"], 1,
   {0: t("120 is the amount, not the percent.", "120 es la cantidad, no el porcentaje."), 2: t("That divides by 520, the new value.", "Eso divide entre 520, el valor nuevo.")}, t("(520 − 400) ÷ 400 = 0.30 = 30%.", "(520 − 400) ÷ 400 = 0.30 = 30 %."))}
{C.enlace(N, t("percent", "porcentaje"), t("Percent change", "Cambio porcentual"), t("New numbers every time, with a hint if you divide by the wrong base.", "Números nuevos cada vez, con una pista si divide entre la base equivocada."))}"""

    s2 = f"""<p>{t("This difference appears on the test and in any economic news, and mixing it up changes how big the headline sounds. If unemployment goes from 4% to 6%:", "Esta distinción aparece en el examen y en cualquier noticia económica, y confundirla cambia el tamaño del titular. Si el desempleo pasa del 4 % al 6 %:")}</p>
{C.tabla(t("Two correct ways to say the same change", "Dos maneras correctas de decir el mismo cambio"), [t("You can say", "Se dice"), t("Calculation", "Cuenta"), t("Result", "Resultado")],
  [[t("It rose 2 percentage points", "Subió 2 puntos porcentuales"), "6 − 4", t("2 points", "2 puntos")], [t("It rose 50%", "Subió un 50 %"), "(6 − 4) ÷ 4 × 100", "50%"]])}
<p>{t("Both sentences describe exactly the same fact, and both are correct. But “it rose 2 points” sounds small, and “it rose 50%” sounds big.", "Las dos frases describen exactamente el mismo hecho y las dos son correctas. Pero «subió 2 puntos» suena a poco y «subió un 50 %» suena a mucho.")}</p>
{C.caja("ojo", t("And Lesson 1.3 comes back", "Y vuelve la Lección 1.3"), "<p>" + t("Someone who wants to make the problem look small will say two points. Someone who wants to alarm will say fifty percent. Neither one lies. They chose, just like the person who chooses between the mean and the median. The defense is the same: ask why that form and not the other.", "Quien quiera minimizar el problema dirá dos puntos. Quien quiera alarmar dirá cincuenta por ciento. Ninguno miente. Han elegido, igual que quien elige entre la media y la mediana. La defensa es la misma: preguntar por qué esa forma y no la otra.") + "</p>")}"""

    s3 = f"""<p>{t("This is the economic calculation the test asks most often, and the one most often missed, because the intuitive answer is wrong. Over ten years, a salary goes from $32,000 to $41,600 a year. In the same period, a price index (like the Consumer Price Index, which measures what the same basket of goods costs) goes from 100 to 128.", "Este es el cálculo económico que el examen plantea con más frecuencia, y el que más se falla, porque la respuesta intuitiva es incorrecta. Durante una década, un salario pasa de 32,000 a 41,600 dólares al año. En el mismo periodo, un índice de precios (como el Índice de Precios al Consumidor, que mide cuánto cuesta la misma canasta de productos) pasa de 100 a 128.")}</p>
{C.ejemplo(t("How much did it really go up?", "¿Cuánto subió de verdad?"),
  [("1", t("<strong>Salary:</strong> (41,600 − 32,000) ÷ 32,000 = 0.30 → <strong>30%</strong>.", "<strong>Salario:</strong> (41,600 − 32,000) ÷ 32,000 = 0.30 → <strong>30 %</strong>.")),
   ("2", t("<strong>Prices:</strong> (128 − 100) ÷ 100 = 0.28 → <strong>28%</strong>.", "<strong>Precios:</strong> (128 − 100) ÷ 100 = 0.28 → <strong>28 %</strong>.")),
   ("✗", t("<strong>The temptation:</strong> subtract, 30 − 28 = 2%. Wrong, even though it is close.", "<strong>La tentación:</strong> restar, 30 − 28 = 2 %. Es incorrecto, aunque quede cerca.")),
   ("3", t("<strong>Correct:</strong> bring the final salary back to starting-year dollars: 41,600 ÷ 1.28 = 32,500. Then (32,500 − 32,000) ÷ 32,000 = <strong>1.56%</strong>.", "<strong>Correcto:</strong> llevar el salario final a dólares del año de partida: 41,600 ÷ 1.28 = 32,500. Después (32,500 − 32,000) ÷ 32,000 = <strong>1.56 %</strong>."))],
  t("Buying power went up 1.56%, not 2%. The two percents were figured on different bases (one on a salary, the other on a price index), so they cannot be subtracted, just as you cannot subtract meters from pounds. Bring both amounts to the same unit: dollars of the starting year.", "El poder adquisitivo subió un 1.56 %, no un 2 %. Los dos porcentajes se calcularon sobre bases distintas (uno sobre un salario, el otro sobre un índice de precios), así que no se pueden restar, igual que no se restan metros y libras. Hay que llevar las dos cantidades a la misma unidad: dólares del año de partida."))}
{P(t("Practice 2 · Buying power", "Práctica 2 · Poder adquisitivo"), t("A salary goes from $25,000 to $30,000 while prices go from 100 to 120. How did buying power change?", "Un salario pasa de 25,000 a 30,000 dólares mientras los precios pasan de 100 a 120. ¿Cómo cambió el poder adquisitivo?"),
   [t("It did not change", "No cambió"), t("It went up 20%", "Subió un 20 %"), t("It went down 20%", "Bajó un 20 %")], 0,
   {1: t("That is the salary alone; prices rose too.", "Eso es solo el salario; los precios también subieron."), 2: t("Divide 30,000 by 1.20.", "Divida 30,000 entre 1.20.")}, t("30,000 ÷ 1.20 = 25,000 starting-year dollars: exactly the same buying power.", "30,000 ÷ 1.20 = 25,000 dólares del año de partida: exactamente el mismo poder adquisitivo."))}"""

    s4 = f"""<p>{t("A map scale of <strong>1 : 50,000</strong> means that one unit on the map stands for 50,000 of the same units on the ground. One inch on paper is 50,000 inches on the ground; one centimeter is 50,000 centimeters. The scale has no units because it works with any unit, as long as both sides use the same one.", "Una escala de <strong>1 : 50,000</strong> significa que una unidad del mapa equivale a 50,000 unidades iguales del terreno. Un centímetro en el papel son 50,000 centímetros en el terreno; una pulgada, 50,000 pulgadas. La escala no lleva unidades porque funciona con cualquiera, siempre que sea la misma en los dos lados.")}</p>
{svg_mapa()}
<p>{t("Two ways to give the same scale. The <strong>numeric</strong> scale (1 : 50,000) is a ratio. The <strong>graphic</strong> scale is the bar at the bottom, and it has an advantage: if the map is enlarged or shrunk when printed, the bar stretches with it and is still correct, while the ratio is not.", "Dos maneras de dar la misma escala. La <strong>numérica</strong> (1 : 50,000) es una razón. La <strong>gráfica</strong> es la barra de abajo, y tiene una ventaja: si el mapa se amplía o se reduce al imprimirlo, la barra se estira con él y sigue siendo válida, mientras que la razón numérica deja de serlo.")}</p>
{C.ejemplo(t("From centimeters on the map to kilometers on the ground", "De centímetros de mapa a kilómetros reales"),
  [("1", t("On the printed map, measure the distance from the school to the clinic with a ruler: <strong>8 cm</strong>.", "En el mapa impreso, mida con una regla la distancia de la escuela a la clínica: <strong>8 cm</strong>.")),
   ("2", t("Multiply by the scale: 8 × 50,000 = <strong>400,000 cm</strong> on the ground.", "Multiplique por la escala: 8 × 50,000 = <strong>400,000 cm</strong> en el terreno.")),
   ("3", t("Change to the unit the question asks for. 1 km = 100,000 cm, so 400,000 ÷ 100,000 = <strong>4 km</strong>.", "Convierta a la unidad que pide la pregunta. 1 km = 100,000 cm, así que 400,000 ÷ 100,000 = <strong>4 km</strong>."))],
  t("The mistake in this section is always about units, never about multiplying. Memorize one equivalence: 1 km = 100,000 cm. (In inches: 1 mile = 63,360 inches.)", "El error de esta sección es siempre de unidades, nunca de multiplicación. Memorice una sola equivalencia: 1 km = 100,000 cm. (En pulgadas: 1 milla = 63,360 pulgadas)."))}
{C.tabla(t("Three measurements solved, with different scales", "Tres medidas resueltas, con escalas distintas"), [t("On the map", "En el mapa"), t("Scale", "Escala"), t("Real distance", "Distancia real")],
  [["4 cm", "1 : 50,000", "200,000 cm = 2 km"], ["7.5 cm", "1 : 25,000", "187,500 cm = 1.875 km"], ["12 cm", "1 : 100,000", "1,200,000 cm = 12 km"]])}
<p>{t("Look at the second row. With a 1 : 25,000 scale the map is more zoomed in: it shows less land with more detail, so 7.5 cm is less than two kilometers. <strong>The bigger the number on the right, the more land fits on the paper, and the less detail there is.</strong>", "Fíjese en la segunda fila. Con una escala de 1 : 25,000 el mapa está más ampliado: muestra menos territorio con más detalle, y por eso 7.5 cm son menos de dos kilómetros. <strong>Cuanto mayor es el número de la derecha, más terreno cabe en el papel y menos detalle hay.</strong>")}</p>
{P(t("Practice 3 · Map scale", "Práctica 3 · Escala"), t("You measure 6 cm on a 1 : 25,000 map. What is the real distance?", "Mide 6 cm en un mapa 1 : 25,000. ¿Cuál es la distancia real?"), ["150 km", "1.5 km", "15 km"], 1,
   {0: t("6 × 25,000 = 150,000 cm. How many centimeters are in a kilometer?", "6 × 25,000 = 150,000 cm. ¿Cuántos centímetros tiene un kilómetro?"), 2: t("Check the conversion: 1 km = 100,000 cm.", "Revise la conversión: 1 km = 100,000 cm.")}, t("150,000 cm ÷ 100,000 = 1.5 km.", "150,000 cm ÷ 100,000 = 1.5 km."))}
{C.enlace(N, t("scale", "escala"), t("Map scale", "Escala de mapas"), t("A new measurement and scale every time.", "Una medida y una escala nuevas cada vez."))}"""

    pob = {"tipo": "barras", "xEtq": t("Area", "Territorio"), "yEtq": t("Population (thousands)", "Habitantes (miles)"), "barras": [{"etq": a, "valor": p // 1000} for a, p, s in TER]}
    den = {"tipo": "barras", "xEtq": t("Area", "Territorio"), "yEtq": t("People per km²", "Habitantes por km²"), "barras": [{"etq": a, "valor": p // s} for a, p, s in TER]}
    s5 = f"""<p>{t("Density is a division and nothing more:", "La densidad es una división y nada más:")}</p>
<p style="font-size:1.2em;text-align:center"><strong>{t("density = population ÷ area", "densidad = habitantes ÷ superficie")}</strong> → {t("people per km² (or per square mile)", "habitantes por km² (o por milla cuadrada)")}</p>
<p>{t("The interesting part is not the arithmetic. It is that <strong>the most populated area is almost never the densest</strong>. Illustrative data, chosen so that the order flips:", "Lo interesante no es la cuenta. Es que <strong>el territorio más poblado casi nunca es el más denso</strong>. Datos ilustrativos, elegidos para que el orden se invierta:")}</p>
<div class="dos-graficas"><div><h4>{t("Population", "Población")}</h4>{C.grafica(pob, C.describe(pob), ancho=400, alto=280, y1=300)}</div><div><h4>{t("Density", "Densidad")}</h4>{C.grafica(den, C.describe(den), ancho=400, alto=280, y1=700)}</div></div>
{C.tabla(t("Population, area, and density of the three areas", "Población, superficie y densidad de los tres territorios"), [t("Area", "Territorio"), t("Population", "Habitantes"), t("Area (km²)", "Superficie (km²)"), t("Division", "División"), t("Density", "Densidad")],
  [[a, f"{p:,}", f"{s:,}", f"{p:,} ÷ {s:,}", f"{p // s} " + t("per km²", "por km²")] for a, p, s in TER])}
<p>{t("Area C has almost three times as many people as B and is the least dense of the three. B has the fewest people and is the densest. Sorting by population and sorting by density give opposite lists.", "El territorio C tiene casi el triple de habitantes que el B y es el menos denso de los tres. El B es el menos poblado y el más denso. Ordenar por población y ordenar por densidad da listas opuestas.")}</p>
{C.caja("ojo", t("What a density does not say", "Qué no dice una densidad"), "<p>" + t("A density is a mean, and it has the same problem we saw in Lesson 2.2: it shares out equally what is not shared equally. An area with 200 people per km² could have everyone crowded into one city and the rest empty. The number cannot tell those two cases apart.", "La densidad es una media, y arrastra el mismo problema de la Lección 2.2: reparte por igual lo que no está repartido por igual. Un territorio de 200 habitantes por km² puede tener a toda su gente apiñada en una ciudad y el resto vacío. La cifra no distingue esos dos casos.") + "</p><p>" + t("Remember Agnes Holbrook’s maps from Lesson 1.2. She colored each lot whole, “whether occupied by one person or one hundred,” and warned in writing that her maps give no clue to density. A document that looks like it measures density, by an author who says it does not: the same skill of Lesson 1.2 (what a source supports and what it does not), now with a number.", "Recuerde los mapas de Agnes Holbrook de la Lección 1.2. Pintó cada solar entero, «lo habite una persona o cien», y advirtió por escrito que sus mapas no dan ninguna pista sobre la densidad. Un documento que parece medir densidad, de una autora que dice que no lo hace: la misma destreza de la Lección 1.2 (qué sostiene una fuente y qué no), ahora con un número.") + "</p>")}
{P(t("Practice 4 · Density", "Práctica 4 · Densidad"), t("A density of 200 people per km² means that…", "Una densidad de 200 habitantes por km² significa que…"),
   [t("on average there are 200 people per km², without knowing how they are spread out", "de media hay 200 habitantes por km², sin saber cómo están repartidos"), t("every km² has exactly 200 people", "cada km² tiene exactamente 200 habitantes"), t("the population is spread out evenly", "la población está repartida de forma uniforme")], 0,
   {1: t("It is an average.", "Es una media."), 2: t("The number cannot tell.", "La cifra no lo dice.")}, t("A density is a mean: it hides how people are actually spread.", "La densidad es una media: oculta cómo está repartida en realidad la gente."))}
{C.enlace(N, t("density", "densidad"), t("Population density", "Densidad de población"), t("Calculate the density of a new area every time.", "Calcule la densidad de un territorio nuevo cada vez."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK). You may use the calculator.",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SSP.10.a", "2", t("<em>A news report says: “The unemployment rate in the state rose from 4% to 6% last year.”</em><br>Which statement describes this change correctly?", "<em>Una noticia dice: «La tasa de desempleo del estado subió del 4 % al 6 % el año pasado»</em>.<br>¿Qué frase describe correctamente este cambio?"),
   [t("It rose 2 percentage points, which is a 50% increase in the rate.", "Subió 2 puntos porcentuales, que es un aumento del 50 % de la tasa."), t("It rose 2%, which is a small change.", "Subió un 2 %, que es un cambio pequeño."), t("It rose 6%.", "Subió un 6 %."), t("It rose 33%.", "Subió un 33 %.")], 0,
   {1: t("2 is points, not percent.", "2 son puntos, no por ciento."), 2: t("6% is the new rate, not the change.", "6 % es la tasa nueva, no el cambio."), 3: t("That divides by 6, the new value.", "Eso divide entre 6, el valor nuevo.")},
   t("6 − 4 = 2 points; 2 ÷ 4 = 0.5 = 50%.", "6 − 4 = 2 puntos; 2 ÷ 4 = 0.5 = 50 %."))}
{G(2, "SSP.6.c", "2", t("<em>On a map with a scale of 1 : 100,000, two towns are 3.5 cm apart.</em><br>How far apart are they on the ground?", "<em>En un mapa con escala 1 : 100,000, dos pueblos están a 3.5 cm de distancia.</em><br>¿A qué distancia están en el terreno?"),
   ["3.5 km", "35 km", "350 km", "0.35 km"], 0,
   {1: t("3.5 × 100,000 = 350,000 cm. Now convert.", "3.5 × 100,000 = 350,000 cm. Ahora convierta."), 2: t("Too many zeros: 1 km = 100,000 cm.", "Demasiados ceros: 1 km = 100,000 cm."), 3: t("Too few: check the conversion.", "Muy poco: revise la conversión.")},
   t("350,000 cm ÷ 100,000 = 3.5 km. With 1 : 100,000, each centimeter is exactly one kilometer.", "350,000 cm ÷ 100,000 = 3.5 km. Con 1 : 100,000, cada centímetro es exactamente un kilómetro."))}
{G(3, "SSP.10.a", "2", C.tabla(t("Two counties", "Dos condados"), [t("County", "Condado"), t("Population", "Habitantes"), t("Area (square miles)", "Superficie (millas cuadradas)")], [["North", "60,000", "300"], ["South", "45,000", "90"]]) +
   t("Which statement is supported by the table?", "¿Qué afirmación sostiene la tabla?"),
   [t("South County is more densely populated than North County.", "El condado Sur está más densamente poblado que el Norte."), t("North County is more densely populated because it has more people.", "El condado Norte está más densamente poblado porque tiene más habitantes."), t("The two counties have the same density.", "Los dos condados tienen la misma densidad."), t("People in South County live in apartments.", "La gente del condado Sur vive en apartamentos.")], 0,
   {1: t("More people is not more density: divide by the area.", "Más gente no es más densidad: divida entre la superficie."), 2: t("Do the two divisions.", "Haga las dos divisiones."), 3: t("The table says nothing about housing.", "La tabla no dice nada de la vivienda.")},
   t("North: 60,000 ÷ 300 = 200 per square mile. South: 45,000 ÷ 90 = 500 per square mile.", "Norte: 60,000 ÷ 300 = 200 por milla cuadrada. Sur: 45,000 ÷ 90 = 500 por milla cuadrada."))}
{G(4, "SSP.6.a", "3", t("<em>From 2010 to 2020, a worker’s hourly wage rose from $15.00 to $18.00. During the same years, prices rose 20%.</em><br>Which conclusion is best supported?", "<em>De 2010 a 2020, el salario por hora de un trabajador subió de 15.00 a 18.00 dólares. En los mismos años, los precios subieron un 20 %.</em><br>¿Qué conclusión está mejor sostenida?"),
   [t("The worker’s buying power stayed about the same.", "El poder adquisitivo del trabajador se mantuvo prácticamente igual."), t("The worker can buy 20% more than in 2010.", "El trabajador puede comprar un 20 % más que en 2010."), t("The worker can buy $3 more per hour of goods.", "El trabajador puede comprar 3 dólares más de productos por hora."), t("The worker’s buying power fell by 20%.", "El poder adquisitivo del trabajador bajó un 20 %.")], 0,
   {1: t("Prices rose too.", "Los precios también subieron."), 2: t("$3 more, but each dollar buys less.", "3 dólares más, pero cada dólar compra menos."), 3: t("The wage rose too.", "El salario también subió.")},
   t("The wage rose (18 − 15) ÷ 15 = 20%, the same as prices; $18.00 ÷ 1.20 = $15.00 in 2010 dollars.", "El salario subió (18 − 15) ÷ 15 = 20 %, lo mismo que los precios; 18.00 ÷ 1.20 = 15.00 dólares de 2010."))}"""

    secciones = [
        ("s1", t("Percent change and the base", "El cambio porcentual y la base"), s1),
        ("s2", t("Percentage points are not percents", "Puntos porcentuales no son por ciento"), s2),
        ("s3", t("How much did it really go up?", "¿Cuánto subió de verdad?"), s3),
        ("s4", t("The scale of a map", "La escala de un mapa"), s4),
        ("s5", t("Population density", "Densidad de población"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Ten percent changes (25 minutes).", "Diez cambios porcentuales (25 minutos)."), t("With the calculator, always grouping the subtraction in parentheses: from 40 to 52; from 80 to 60; from 12 to 15; from 250 to 200; from 1,200 to 1,500. Then, for each one, find the change needed to go back. <em>Check:</em> +30%, −25%, +25%, −20%, +25%; and to go back: −23.08%, +33.33%, −20%, +25%, −20%. They never match.", "Con la calculadora, agrupando siempre la resta entre paréntesis: de 40 a 52; de 80 a 60; de 12 a 15; de 250 a 200; de 1,200 a 1,500. Después, para cada uno, halle el cambio necesario para volver atrás. <em>Compruebe:</em> +30 %, −25 %, +25 %, −20 %, +25 %; y para volver: −23.08 %, +33.33 %, −20 %, +25 %, −20 %. Nunca coinciden.")),
        (t("How much did it really go up? (25 minutes)", "¿Cuánto subió de verdad? (25 minutos)"), t("A salary goes from $25,000 to $30,000 while prices go from 100 to 120. Calculate the change in the salary, in prices, and in buying power. Then write two lines explaining it to someone who thinks you can just subtract. <em>Check:</em> 20%, 20%, and 0%. Subtracting happens to work here, but try it with 32,000 → 41,600 and prices 100 → 128, and it fails.", "Un salario pasa de 25,000 a 30,000 dólares mientras los precios pasan de 100 a 120. Calcule el cambio del salario, el de los precios y el del poder adquisitivo. Después escriba dos líneas explicándoselo a alguien que cree que basta con restar. <em>Compruebe:</em> 20 %, 20 % y 0 %. Restar acierta aquí por casualidad, pero pruébelo con 32,000 → 41,600 y precios 100 → 128, y falla.")),
        (t("Your city to scale (30 minutes).", "Su ciudad a escala (30 minutos)."), t("Get a printed map with a scale. Measure three distances and convert them to real kilometers or miles. Then look up the population and area of your city or county and calculate its density. <em>Check:</em> if one distance comes out a thousand times too big or too small, the problem is the unit conversion.", "Consiga un mapa impreso con escala. Mida tres distancias y conviértalas a kilómetros o millas reales. Después busque la población y la superficie de su ciudad o condado y calcule su densidad. <em>Compruebe:</em> si una distancia le sale mil veces mayor o menor de lo razonable, el fallo está en la conversión de unidades.")),
    ]
    Q = t
    quiz = [
        (Q("A price goes from $40 to $52. The percent change is…", "Un precio pasa de 40 a 52 dólares. El cambio porcentual es…"), ["12%", "30%", "23%", "130%"], 1,
         {0: Q("12 is the amount.", "12 es la cantidad."), 2: Q("That divides by 52.", "Eso divide entre 52."), 3: Q("That is 52 ÷ 40 without subtracting 1.", "Eso es 52 ÷ 40 sin restar 1.")}, Q("12 ÷ 40 = 0.3.", "12 ÷ 40 = 0.3.")),
        (Q("A price goes from $250 to $200. The percent change is…", "Un precio pasa de 250 a 200 dólares. El cambio porcentual es…"), ["−20%", "−25%", "−50%", "+20%"], 0,
         {1: Q("That divides by 200.", "Eso divide entre 200."), 2: Q("Check the division.", "Revise la división."), 3: Q("The price went down.", "El precio bajó.")}, Q("−50 ÷ 250 = −0.2.", "−50 ÷ 250 = −0.2.")),
        (Q("$80 goes up 25%, then down 25%. It ends at…", "80 dólares suben un 25 % y después bajan un 25 %. Quedan en…"), ["$80", "$85", "$75", "$70"], 2,
         {0: Q("The two percents use different bases.", "Los dos porcentajes usan bases distintas."), 1: Q("Do it step by step.", "Hágalo paso a paso."), 3: Q("100 × 0.75 = ?", "100 × 0.75 = ?")}, Q("80 → 100 → 75.", "80 → 100 → 75.")),
        (Q("In the percent change formula, you divide the difference by…", "En la fórmula del cambio porcentual, la diferencia se divide entre…"), [Q("the old (starting) value", "el valor viejo (de partida)"), Q("the new value", "el valor nuevo"), Q("the sum of the two", "la suma de los dos"), Q("100", "100")], 0,
         {1: Q("Ask: a percent of what?", "Pregúntese: ¿un tanto por ciento de qué?"), 2: Q("That is not the formula.", "Esa no es la fórmula."), 3: Q("You multiply by 100 at the end.", "Se multiplica por 100 al final.")}, Q("The base is where you start.", "La base es de donde se parte.")),
        (Q("Unemployment goes from 4% to 6%. Which is correct?", "El desempleo pasa del 4 % al 6 %. ¿Qué es correcto?"), [Q("Only “it rose 2 points”", "Solo «subió 2 puntos»"), Q("Only “it rose 50%”", "Solo «subió un 50 %»"), Q("Both, since they describe the same fact", "Las dos, porque describen el mismo hecho"), Q("Neither", "Ninguna")], 2,
         {0: Q("The other is also correct.", "La otra también es correcta."), 1: Q("The other is also correct.", "La otra también es correcta."), 3: Q("Both are correct.", "Las dos son correctas.")}, Q("2 points = 50% of 4.", "2 puntos = 50 % de 4.")),
        (Q("A salary goes from $32,000 to $41,600 and prices from 100 to 128. Buying power rose…", "Un salario pasa de 32,000 a 41,600 dólares y los precios de 100 a 128. El poder adquisitivo subió…"), ["2%", "1.56%", "30%", "28%"], 1,
         {0: Q("You cannot subtract percents with different bases.", "No se restan porcentajes de bases distintas."), 2: Q("That is the salary only.", "Eso es solo el salario."), 3: Q("That is prices only.", "Eso es solo los precios.")}, Q("41,600 ÷ 1.28 = 32,500; +1.56%.", "41,600 ÷ 1.28 = 32,500; +1.56 %.")),
        (Q("A scale of 1 : 50,000 means that 1 cm on the map is…", "Una escala 1 : 50,000 significa que 1 cm del mapa equivale a…"), ["50,000 km", "0.5 km", "5 km", "50 km"], 1,
         {0: Q("50,000 cm, not km.", "50,000 cm, no km."), 2: Q("Divide by 100,000.", "Divida entre 100,000."), 3: Q("Check the zeros.", "Revise los ceros.")}, Q("50,000 cm = 0.5 km.", "50,000 cm = 0.5 km.")),
        (Q("8 cm on a 1 : 50,000 map is…", "8 cm en un mapa 1 : 50,000 son…"), ["400,000 km", "4 km", "40 km", "0.4 km"], 1,
         {0: Q("400,000 is in cm.", "400,000 son cm."), 2: Q("Too many: 1 km = 100,000 cm.", "Demasiado: 1 km = 100,000 cm."), 3: Q("Too few.", "Muy poco.")}, Q("400,000 cm = 4 km.", "400,000 cm = 4 km.")),
        (Q("Which map shows more detail?", "¿Qué mapa muestra más detalle?"), ["1 : 25,000", "1 : 100,000", Q("Both the same", "Los dos igual"), Q("It depends on the paper", "Depende del papel")], 0,
         {1: Q("A bigger number fits more land and less detail.", "Un número mayor muestra más terreno y menos detalle."), 2: Q("The scales are different.", "Las escalas son distintas."), 3: Q("The scale decides.", "La escala lo decide.")}, Q("Smaller number on the right = more zoomed in.", "Número menor a la derecha = más ampliado.")),
        (Q("Area B has 90,000 people on 150 km². Its density is…", "El territorio B tiene 90,000 habitantes en 150 km². Su densidad es…"), [Q("600 per km²", "600 por km²"), Q("6 per km²", "6 por km²"), Q("13,500,000 per km²", "13,500,000 por km²"), Q("1,667 per km²", "1,667 por km²")], 0,
         {1: Q("Check the zeros.", "Revise los ceros."), 2: Q("That multiplies.", "Eso multiplica."), 3: Q("Population ÷ area, not the reverse.", "Habitantes ÷ superficie, no al revés.")}, Q("90,000 ÷ 150 = 600.", "90,000 ÷ 150 = 600.")),
        (Q("Of areas A (120,000 on 400 km²), B (90,000 on 150 km²), and C (250,000 on 1,250 km²), the densest is…", "De los territorios A (120,000 en 400 km²), B (90,000 en 150 km²) y C (250,000 en 1,250 km²), el más denso es…"), ["A", "B", "C", Q("All the same", "Todos igual")], 1,
         {0: Q("A = 300 per km².", "A = 300 por km²."), 2: Q("C has the most people but 200 per km².", "C tiene más gente, pero 200 por km²."), 3: Q("Do the divisions.", "Haga las divisiones.")}, Q("B = 600 per km².", "B = 600 por km².")),
        (Q("A density of 200 people per km² allows you to say that…", "Una densidad de 200 habitantes por km² permite afirmar que…"), [Q("there are 200 per km² on average, without knowing how they are spread", "hay 200 por km² de media, sin saber cómo están repartidos"), Q("every km² has exactly 200", "cada km² tiene exactamente 200"), Q("the people are spread evenly", "la gente está repartida de forma uniforme"), Q("the area is a city", "el territorio es una ciudad")], 0,
         {1: Q("It is a mean.", "Es una media."), 2: Q("The number does not say.", "La cifra no lo dice."), 3: Q("Density does not say what kind of place it is.", "La densidad no dice qué tipo de lugar es.")}, Q("A density is a mean.", "La densidad es una media.")),
    ]
    filas = [
        (t("Use the right base", "Usa la base correcta"), t("I always divide by the starting value, group the subtraction in parentheses, and can explain why going up and down the same percent does not return to the start.", "Divido siempre entre el valor de partida, agrupo la resta entre paréntesis y sé explicar por qué subir y bajar el mismo porcentaje no devuelve al inicio."), t("I get increases right but fail with decreases or going back.", "Acierto en subidas, pero fallo en bajadas o al volver atrás."), t("I divide by the new value, or give the difference as the percent (<a href=\"#s1\">review section 1</a>).", "Divido entre el valor nuevo, o doy la diferencia como si fuera el porcentaje (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Tell points from percent", "Distingue puntos de por ciento"), t("I calculate both and notice when someone chose one to make a change look bigger or smaller.", "Calculo las dos cifras y noto cuándo alguien eligió una para agrandar o achicar un cambio."), t("I know they differ but miscalculate the percent.", "Sé que se diferencian, pero calculo mal el porcentaje."), t("I use them as if they were the same (<a href=\"#s2\">review section 2</a>).", "Las uso como si fueran lo mismo (<a href=\"#s2\">repase la sección 2</a>).")),
        (t("Apply a map scale", "Aplica la escala de un mapa"), t("I convert to the unit asked, check that the answer is reasonable, and explain why 1 : 25,000 shows more detail.", "Convierto a la unidad pedida, compruebo que el resultado es razonable y explico por qué 1 : 25,000 muestra más detalle."), t("I multiply right but answer in centimeters when kilometers are asked.", "Multiplico bien, pero respondo en centímetros cuando piden kilómetros."), t("I multiply at random or reverse the scale (<a href=\"#s4\">review section 4</a>).", "Multiplico al azar o invierto la escala (<a href=\"#s4\">repase la sección 4</a>).")),
        (t("Calculate and interpret density", "Calcula e interpreta la densidad"), t("I compare areas, explain why the most populated is not the densest, and say that density hides how people are spread.", "Comparo territorios, explico por qué el más poblado no es el más denso y digo que la densidad oculta cómo está repartida la gente."), t("I divide correctly but do not compare or interpret.", "Divido bien, pero no comparo ni interpreto."), t("I confuse population with density (<a href=\"#s5\">review section 5</a>).", "Confundo población con densidad (<a href=\"#s5\">repase la sección 5</a>).")),
    ]
    cierre = "<p>" + t("The three calculations of this lesson are simple divisions, and all three are missed for the same reason: dividing by the wrong number. The percent is divided by the starting value. The scale is converted, at the end, to the unit the question asks for. The density is divided by the area, and by nothing else.",
                         "Las tres cuentas de esta lección son divisiones sencillas, y las tres se fallan por lo mismo: por dividir entre el número equivocado. El porcentaje se divide entre el valor de partida. La escala se convierte, al final, a la unidad que pide la pregunta. La densidad se divide entre la superficie, y entre nada más.") + "</p><p>" + \
             t("This closes Topic 2. Lesson 2.1 taught you to read a graph by its structure before its content; 2.2, that a single number never describes a set of data; and this one, that a correct number can still be a chosen number: two percentage points and fifty percent are the same fact, and they do not sound the same. It is the idea Topic 1 ended with, now tested with numbers.",
               "Con esto se cierra el Tema 2. La 2.1 enseñó a leer una gráfica por su estructura antes que por su contenido; la 2.2, que un solo número nunca describe un conjunto; y esta, que una cifra correcta puede seguir siendo una cifra elegida: dos puntos porcentuales y un cincuenta por ciento son el mismo hecho, y no suenan igual. Es la idea con la que terminó el Tema 1, ahora comprobada con números.") + "</p><p>" + \
             t("Topic 3 changes ground: civics and the founding documents, from the social contract to the Declaration of Independence and the Constitution.", "El Tema 3 cambia de terreno: la educación cívica y los documentos fundacionales, del contrato social a la Declaración de Independencia y la Constitución.") + "</p>"
    glosario = [
        (t("Percent change", "Cambio porcentual"), t("(new − old) ÷ old × 100.", "(nuevo − viejo) ÷ viejo × 100.")),
        (t("Percentage points", "Puntos porcentuales"), t("The plain difference between two percents (6% − 4% = 2 points).", "La simple diferencia entre dos porcentajes (6 % − 4 % = 2 puntos).")),
        (t("Price index (CPI)", "Índice de precios (IPC)"), t("A number that tracks what the same basket of goods costs over time.", "Número que sigue cuánto cuesta la misma canasta de productos a lo largo del tiempo.")),
        (t("Buying power", "Poder adquisitivo"), t("What money can actually buy, once price changes are taken into account.", "Lo que el dinero puede comprar de verdad, una vez descontado el cambio de los precios.")),
        (t("Map scale", "Escala de un mapa"), t("The ratio between a distance on the map and the real distance (1 : 50,000).", "La razón entre una distancia del mapa y la real (1 : 50,000).")),
        (t("Population density", "Densidad de población"), t("Population ÷ area; people per km² or per square mile.", "Habitantes ÷ superficie; habitantes por km² o por milla cuadrada.")),
        (t("Rate", "Tasa"), t("An amount per unit of something else: per hour, per 100 people, per km².", "Una cantidad por cada unidad de otra cosa: por hora, por cada 100 personas, por km².")),
    ]
    estd = C.estandares(["SSP.10.a", "SSP.6.a", "SSP.6.c"], ["E.e", "E.f", "G.b"], base=["SSP.11.a", "SSP.5.b"])
    conexion = "<p>" + t("Lesson 2.2 taught you that a single number never describes a set of data, and that choosing between the mean and the median is already a one-sided decision. This lesson closes the topic with the three calculations that appear most on the Social Studies test: the percent, the scale, and the density. All three are simple divisions, and all three are missed for the same reason: dividing by the wrong number.",
                         "La Lección 2.2 enseñó que un solo número nunca describe un conjunto, y que elegir entre la media y la mediana ya es una decisión interesada. Esta cierra el tema con las tres cuentas que más aparecen en el examen de Estudios Sociales: el porcentaje, la escala y la densidad. Las tres son divisiones sencillas, y las tres se fallan por lo mismo: por dividir entre el número equivocado.") + "</p><p>" + \
               t("<strong>A note on map scales:</strong> the map work here is the same as similar figures and scale drawings in Math Level 3. If you already did that, you are not learning anything new: you are using it on a map.", "<strong>Una nota sobre las escalas:</strong> el trabajo con mapas de esta lección es el mismo de la semejanza y los dibujos a escala del Nivel 3 de Matemáticas. Si ya cursó aquello, no aprende nada nuevo: lo aplica a un mapa.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Three simple divisions that are missed for the same reason: dividing by the wrong number.", "Tres divisiones sencillas que se fallan por lo mismo: dividir entre el número equivocado."),
        ["SSP.10 · " + t("Rates and change", "Tasas y cambio"), "SSP.6 · " + t("Maps and numbers", "Mapas y números")],
        [t("<strong>Calculate</strong> and interpret percent changes in economic settings, always with the right base.", "<strong>Calcular</strong> e interpretar cambios porcentuales en contextos económicos, siempre con la base correcta."),
         t("<strong>Tell apart</strong> a change in percentage points from a percent change.", "<strong>Distinguir</strong> un cambio en puntos porcentuales de un cambio porcentual."),
         t("<strong>Use</strong> a map scale to find real distances without unit mistakes.", "<strong>Aplicar</strong> la escala de un mapa para hallar distancias reales sin errores de unidad."),
         t("<strong>Calculate</strong> population density and compare areas, knowing what that number says and what it does not.", "<strong>Calcular</strong> la densidad de población y comparar territorios, sabiendo qué afirma esa cifra y qué no.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        (None, t("Next: Topic 3 · Civics I: founding documents and constitutional principles.", "Siguiente: Tema 3 · Cívica I: documentos fundacionales y principios constitucionales.")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- la práctica
JS = r"""
function rd(x){ return Math.round(x * 100) / 100; }
function gPct(){
  var ctx = elige(TXS.ctx), p = elige([-50, -40, -25, -20, -10, -5, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100]), v, n, i;
  for (i = 0; i < 50; i++){ v = aleatorio(ctx[1], ctx[2]) * ctx[3]; n = v * (100 + p) / 100; if (n === Math.round(n)) break; }
  if (n !== Math.round(n)) return gPct();
  var r = p, exp = "( " + com(n) + " − " + com(v) + " ) ÷ " + com(v) + " = " + rd(p / 100) + " → " + p + "%.";
  return {enun: "<p>" + ctx[0].replace("{a}", ctx[4] + com(v)).replace("{b}", ctx[4] + com(n)) + "</p><p>" + TXS.pidePct + "</p>", resp: leeNumero(String(r)), explica: exp,
    pista: function(x){ var d = n - v; if (igual(x, leeNumero(String(d)))) return TXS.esDif; if (igual(x, leeNumero(String(rd(d / n * 100))))) return TXS.esNuevo; if (igual(x, leeNumero(String(-r)))) return TXS.signo; return TXS.formula; }};
}
function gEsc(){
  var esc = elige([10000, 20000, 25000, 50000, 100000, 200000, 250000]), cm = elige([2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 1.5, 2.5, 3.5, 4.5, 7.5]);
  var real = cm * esc, km = rd(real / 100000);
  if (Math.round(real / 100000 * 1000) / 1000 !== km) return gEsc();
  return {enun: "<p>" + TXS.esc.replace("{c}", cm).replace("{e}", com(esc)) + "</p>", resp: leeNumero(String(km)), explica: cm + " × " + com(esc) + " = " + com(real) + " cm; " + com(real) + " ÷ 100,000 = " + km + " km.",
    pista: function(x){ if (igual(x, leeNumero(String(real)))) return TXS.enCm; return TXS.escP; }};
}
function gDen(){
  var sup = elige([50, 80, 120, 150, 200, 250, 300, 400, 500, 600, 750, 800, 1000, 1250]), d = elige([25, 40, 50, 60, 75, 80, 120, 150, 200, 240, 300, 450, 600, 800, 1200]);
  var pob = sup * d, lugar = elige(TXS.lugares);
  return {enun: "<p>" + TXS.den.replace("{l}", lugar).replace("{p}", com(pob)).replace("{s}", com(sup)) + "</p>", resp: leeNumero(String(d)), explica: com(pob) + " ÷ " + com(sup) + " = " + d + TXS.porKm,
    pista: function(x){ if (igual(x, leeNumero(String(rd(sup / pob))))) return TXS.alReves; return TXS.denP; }};
}
"""


def tx():
    return {
        "ctx": [[t("The monthly rent of an apartment went from {a} to {b}.", "El alquiler mensual de un apartamento pasó de {a} a {b}."), 8, 30, 50, "$"],
                [t("The population of a town went from {a} to {b} people.", "La población de un pueblo pasó de {a} a {b} personas."), 20, 90, 100, ""],
                [t("A worker’s yearly salary went from {a} to {b}.", "El salario anual de un trabajador pasó de {a} a {b}."), 20, 60, 1000, "$"],
                [t("The number of voters in a ward went from {a} to {b}.", "El número de votantes de un distrito pasó de {a} a {b}."), 20, 80, 100, ""],
                [t("The price of a bus pass went from {a} to {b}.", "El precio de un pase de autobús pasó de {a} a {b}."), 20, 120, 1, "$"]],
        "pidePct": t("What is the <strong>percent change</strong>? Write only the number (use a minus sign if it went down).", "¿Cuál es el <strong>cambio porcentual</strong>? Escriba solo el número (con signo menos si bajó)."),
        "esDif": t("That is the change in amount, not in percent. Divide it by the starting value.", "Esa es la cantidad que cambió, no el porcentaje. Divídala entre el valor de partida."),
        "esNuevo": t("You divided by the new value. Divide by the starting value.", "Dividió entre el valor nuevo. Divida entre el valor de partida."),
        "signo": t("Check the sign: did it go up or down?", "Revise el signo: ¿subió o bajó?"),
        "formula": t("(new − old) ÷ old × 100.", "(nuevo − viejo) ÷ viejo × 100."),
        "esc": t("You measure <strong>{c} cm</strong> on a map with a scale of <strong>1 : {e}</strong>. What is the real distance in <strong>kilometers</strong>?", "Mide <strong>{c} cm</strong> en un mapa con escala <strong>1 : {e}</strong>. ¿Cuál es la distancia real en <strong>kilómetros</strong>?"),
        "enCm": t("That is in centimeters. Divide by 100,000 to get kilometers.", "Eso está en centímetros. Divida entre 100,000 para pasar a kilómetros."),
        "escP": t("Multiply the centimeters by the scale, then divide by 100,000.", "Multiplique los centímetros por la escala y después divida entre 100,000."),
        "lugares": [t("A county", "Un condado"), t("A town", "Un municipio"), t("A neighborhood", "Un barrio"), t("A small country", "Un país pequeño"), t("An island", "Una isla")],
        "den": t("{l} has <strong>{p}</strong> people on <strong>{s} km²</strong>. What is its population density, in people per km²?", "{l} tiene <strong>{p}</strong> habitantes en <strong>{s} km²</strong>. ¿Cuál es su densidad de población, en habitantes por km²?"),
        "porKm": t(" people per km².", " habitantes por km²."),
        "alReves": t("Upside down: population ÷ area.", "Al revés: habitantes ÷ superficie."),
        "denP": t("Divide the population by the area.", "Divida los habitantes entre la superficie."),
    }


def banco_puntos():
    datos = [
        (t("The poverty rate went from 10% to 12%.", "La tasa de pobreza pasó del 10 % al 12 %."), [t("2 points, a 20% increase", "2 puntos, un aumento del 20 %"), t("2 points, a 2% increase", "2 puntos, un aumento del 2 %"), t("12 points", "12 puntos"), t("20 points", "20 puntos")], t("12 − 10 = 2 points; 2 ÷ 10 = 20%.", "12 − 10 = 2 puntos; 2 ÷ 10 = 20 %.")),
        (t("Voter turnout went from 50% to 60%.", "La participación electoral pasó del 50 % al 60 %."), [t("10 points, a 20% increase", "10 puntos, un aumento del 20 %"), t("10 points, a 10% increase", "10 puntos, un aumento del 10 %"), t("20 points", "20 puntos"), t("60 points", "60 puntos")], t("60 − 50 = 10 points; 10 ÷ 50 = 20%.", "60 − 50 = 10 puntos; 10 ÷ 50 = 20 %.")),
        (t("The interest rate on a loan went from 2% to 3%.", "La tasa de interés de un préstamo pasó del 2 % al 3 %."), [t("1 point, a 50% increase", "1 punto, un aumento del 50 %"), t("1 point, a 1% increase", "1 punto, un aumento del 1 %"), t("3 points", "3 puntos"), t("50 points", "50 puntos")], t("3 − 2 = 1 point; 1 ÷ 2 = 50%: the interest you pay goes up by half.", "3 − 2 = 1 punto; 1 ÷ 2 = 50 %: el interés que paga sube a la mitad más.")),
        (t("The unemployment rate went from 8% to 6%.", "La tasa de desempleo pasó del 8 % al 6 %."), [t("down 2 points, a 25% decrease", "bajó 2 puntos, un descenso del 25 %"), t("down 2 points, a 2% decrease", "bajó 2 puntos, un descenso del 2 %"), t("down 33%", "bajó un 33 %"), t("down 6 points", "bajó 6 puntos")], t("8 − 6 = 2 points; 2 ÷ 8 = 25%.", "8 − 6 = 2 puntos; 2 ÷ 8 = 25 %.")),
    ]
    out = [{"enun": "<strong>" + s + "</strong><br>" + t("How should the change be described?", "¿Cómo se describe el cambio?"), "ops": ops, "ok": 0, "exp": e} for s, ops, e in datos]
    otros = [
        (t("A politician says crime went up “only 3 points,” from 6% to 9%. A rival says it went up 50%. Who is right?", "Un político dice que el delito subió «solo 3 puntos», del 6 % al 9 %. Un rival dice que subió un 50 %. ¿Quién tiene razón?"),
         [t("Both: each chose the form that fits their message", "Los dos: cada uno eligió la forma que encaja con su mensaje"), t("Only the politician", "Solo el político"), t("Only the rival", "Solo el rival"), t("Neither", "Ninguno")], t("3 points = 50% of 6. Same fact, two choices.", "3 puntos = 50 % de 6. El mismo hecho, dos elecciones.")),
        (t("A salary rose 10% and prices rose 10%. What happened to buying power?", "Un salario subió un 10 % y los precios un 10 %. ¿Qué pasó con el poder adquisitivo?"),
         [t("It stayed the same", "Se mantuvo igual"), t("It rose 10%", "Subió un 10 %"), t("It rose 20%", "Subió un 20 %"), t("It fell 10%", "Bajó un 10 %")], t("Salary × 1.10 ÷ 1.10 = the same.", "Salario × 1.10 ÷ 1.10 = lo mismo.")),
        (t("A salary rose 5% while prices rose 8%. What happened to buying power?", "Un salario subió un 5 % mientras los precios subían un 8 %. ¿Qué pasó con el poder adquisitivo?"),
         [t("It fell", "Bajó"), t("It rose 5%", "Subió un 5 %"), t("It rose 13%", "Subió un 13 %"), t("It stayed the same", "Se mantuvo igual")], t("Prices rose faster than the salary: each dollar of salary buys less. (1.05 ÷ 1.08 ≈ 0.972: about 2.8% less.)", "Los precios subieron más rápido que el salario: cada dólar compra menos. (1.05 ÷ 1.08 ≈ 0.972: un 2.8 % menos, aproximadamente).")),
        (t("A store raises a price 50% and then lowers it 50%. The final price is…", "Una tienda sube un precio un 50 % y después lo baja un 50 %. El precio final es…"),
         [t("lower than the original", "menor que el original"), t("the same as the original", "igual al original"), t("higher than the original", "mayor que el original"), t("impossible to know", "imposible de saber")], t("100 → 150 → 75: the decrease is figured on a bigger base.", "100 → 150 → 75: la bajada se calcula sobre una base mayor.")),
    ]
    out += [{"enun": "<strong>" + s + "</strong>", "ops": ops, "ok": 0, "exp": e} for s, ops, e in otros]
    return out


def practica():
    A = {"en": ["percent", "points", "scale", "density"], "es": ["porcentaje", "puntos", "escala", "densidad"]}[C.L]
    mods = [
        (A[0], t("Percent change", "Cambio porcentual"), "      <p>" + t("New numbers every time. Type with parentheses on the calculator: ( new − old ) ÷ old. Write the percent as a number (for example, 25 or −20).", "Números nuevos cada vez. En la calculadora, con paréntesis: ( nuevo − viejo ) ÷ viejo. Escriba el porcentaje como número (por ejemplo, 25 o −20).") + "</p>\n" + C.dec_campo("m1", t("Percent change", "Cambio porcentual"))),
        (A[1], t("Points, percents, and buying power", "Puntos, por ciento y poder adquisitivo"), C.om("m2", t("Points are a plain difference between two percents; the percent change divides that difference by the starting rate.", "Los puntos son la simple diferencia entre dos porcentajes; el cambio porcentual divide esa diferencia entre la tasa de partida."))),
        (A[2], t("Map scale", "Escala de mapas"), "      <p>" + t("Multiply by the scale, then change centimeters to kilometers: 1 km = 100,000 cm.", "Multiplique por la escala y después pase de centímetros a kilómetros: 1 km = 100,000 cm.") + "</p>\n" + C.dec_campo("m3", t("Kilometers", "Kilómetros"))),
        (A[3], t("Population density", "Densidad de población"), "      <p>" + t("Density = population ÷ area.", "Densidad = habitantes ÷ superficie.") + "</p>\n" + C.dec_campo("m4", t("People per km²", "Habitantes por km²"))),
    ]
    js = C.js_datos("TXS", tx()) + C.js_datos("PUN", banco_puntos()) + JS + 'creaPracticaDec("m1", gPct);\ncreaBanco("m2", PUN);\ncreaPracticaDec("m3", gEsc);\ncreaPracticaDec("m4", gDen);\n'
    return C.pagina_practica(N, titulo(), t("Four activities · new exercises every time · two tries in each one · calculator included", "Cuatro actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
