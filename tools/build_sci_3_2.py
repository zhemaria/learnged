"""LearnGED · Ciencias · Lección 3.2 · Fotosíntesis y respiración celular: el flujo de la energía (EN/ES).
Fuente: clases_ciencias/leccion_3-2.html (diagramas en tools/svg/3-2_*.svg) y los interactivos
ciencias/flujo_energia, ciencias/ciclo_carbono y ciencias/simulador_ecosistemico.
Uso: python3 tools/build_sci_3_2.py
"""
import os, sys, random, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "3-2"


def titulo():
    return t("Photosynthesis and cellular respiration: how energy flows", "Fotosíntesis y respiración celular: el flujo de la energía")


def anc(en, es):
    return en if C.L == "en" else es


FOTO = "6 CO₂ + 6 H₂O + " + "{luz}" + " → C₆H₁₂O₆ + 6 O₂"
RESP = "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + " + "{energia}"


def ec_foto():
    return FOTO.format(luz=t("light", "luz"))


def ec_resp():
    return RESP.format(energia=t("energy", "energía"))


def svg_ecuaciones():
    return C.svg_orig("3-2_0", {
        "FOTOSÍNTESIS · en el cloroplasto": "PHOTOSYNTHESIS · in the chloroplast", "6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂": "6 CO₂ + 6 H₂O + light → C₆H₁₂O₆ + 6 O₂",
        "RESPIRACIÓN CELULAR · en la mitocondria": "CELLULAR RESPIRATION · in the mitochondrion", "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + energía": "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + energy",
        "glucosa": "glucose", "y O₂": "and O₂", "CO₂": "CO₂", "y H₂O": "and H₂O", "Lo que produce una es lo que consume la otra": "What one makes is what the other uses",
        "La fotosíntesis almacena energía en la glucosa; la respiración la libera": "Photosynthesis stores energy in glucose; respiration releases it"},
        "Diagram of how photosynthesis and cellular respiration are related. Photosynthesis happens in the chloroplast: six molecules of carbon dioxide plus six of water plus light make one molecule of glucose and six of oxygen. Cellular respiration happens in the mitochondrion: one molecule of glucose plus six of oxygen make six of carbon dioxide, six of water, and energy. The products of each process are the reactants of the other: glucose and oxygen go from photosynthesis to respiration, and carbon dioxide and water go back from respiration to photosynthesis.")


def svg_carbono():
    return C.svg_orig("3-2_1", {
        "Atmósfera": "Atmosphere", "CO₂": "CO₂", "Planta": "Plant", "glucosa": "glucose", "Herbívoro": "Plant eater", "tejidos": "tissues",
        "Descomponedores": "Decomposers", "hongos, bacterias": "fungi, bacteria", "fotosíntesis": "photosynthesis", "alimentación": "eating",
        "muerte": "death", "descomposición": "decomposition"},
        "The carbon cycle in four stages. From the atmosphere, carbon dioxide passes into the plant through photosynthesis. From the plant it passes to the plant eater through eating. From the plant eater it passes to the decomposers after death. And from the decomposers it goes back to the atmosphere through decomposition and respiration. The cycle closes on itself.")


LUZ = [[0, 0], [2, 18], [4, 34], [6, 45], [8, 50], [10, 51], [12, 51]]


def graf_luz():
    sp = {"tipo": "linea", "xEtq": t("Light intensity (arbitrary units)", "Intensidad luminosa (unidades arbitrarias)"), "yEtq": t("Rate (units/min)", "Tasa (unid./min)"), "px": 2, "py": 10,
          "series": [{"nombre": "", "puntos": LUZ}]}
    aria = t("Line graph of the rate of photosynthesis against light intensity. The horizontal axis is light intensity, from 0 to 12 units. The vertical axis is the rate, from 0 to 60. The curve rises fast at first: at 2 units of light the rate is 18, at 4 it is 34, and at 6 it is 45. From 8 units on, the curve levels off near 50 (51 at 10 and at 12) and does not rise again even as the light keeps increasing. That leveling off is the saturation point.",
             "Gráfica de líneas de la tasa fotosintética frente a la intensidad luminosa. El eje horizontal es la intensidad luminosa, de 0 a 12 unidades. El eje vertical es la tasa, de 0 a 60. La curva sube con rapidez al principio: con 2 unidades de luz la tasa es 18, con 4 es 34 y con 6 es 45. A partir de 8 unidades la curva se aplana en torno a 50 (51 con 10 y con 12) y no vuelve a subir aunque la luz siga aumentando. Ese aplanamiento es el punto de saturación.")
    return C.grafica(sp, aria, y0=0, y1=60)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("A chemical equation is read from left to right. To the left of the arrow are the <strong>reactants</strong>, what is used up; to the right, the <strong>products</strong>, what you get. The large numbers in front of each formula tell how many molecules take part.", "Una ecuación química se lee de izquierda a derecha. A la izquierda de la flecha están los <strong>reactivos</strong>, lo que se consume; a la derecha, los <strong>productos</strong>, lo que se obtiene. Los números grandes que preceden a cada fórmula indican cuántas moléculas intervienen.")}</p>
{svg_ecuaciones()}
{C.tabla(t("Photosynthesis and cellular respiration compared: reactants, products, where they happen, and the role of energy", "Comparación entre la fotosíntesis y la respiración celular según reactivos, productos, lugar donde ocurre y papel de la energía"),
 [t("Feature", "Aspecto"), t("Photosynthesis", "Fotosíntesis"), t("Cellular respiration", "Respiración celular")],
 [[t("Reactants", "Reactivos"), t("Carbon dioxide, water, and light.", "Dióxido de carbono, agua y luz."), t("Glucose and oxygen.", "Glucosa y oxígeno.")],
  [t("Products", "Productos"), t("Glucose and oxygen.", "Glucosa y oxígeno."), t("Carbon dioxide, water, and usable energy (ATP).", "Dióxido de carbono, agua y energía utilizable (ATP).")],
  [t("Where it happens", "Dónde ocurre"), t("In the chloroplast. Only in plants, algae, and some bacteria.", "En el cloroplasto. Solo en plantas, algas y algunas bacterias."), t("In the mitochondrion. In plants and in animals, every one of them.", "En la mitocondria. En plantas y en animales, sin excepción.")],
  [t("Energy", "Energía"), t("Takes it in and stores it in the bonds of glucose.", "La absorbe y la almacena en los enlaces de la glucosa."), t("Releases it so the cell can use it.", "La libera para que la célula pueda usarla.")],
  [t("When it happens", "Cuándo ocurre"), t("Only when there is light.", "Solo con luz disponible."), t("All the time, day and night.", "De forma continua, de día y de noche.")]])}
{C.caja("ojo", t("The most common mistake on the test", "El error más frecuente del examen"), "<p>" + t("Believing that plants “do photosynthesis” and animals “breathe,” as if they were two alternatives. They are not. Plants do both: they make glucose in the chloroplast during the day and burn it in the mitochondrion at all hours, just like any animal. Photosynthesis is what plants do <em>in addition</em>, not <em>instead</em>.", "Creer que las plantas «hacen fotosíntesis» y los animales «respiran», como si fueran procesos alternativos. No lo son. Las plantas hacen las dos cosas: fabrican glucosa en el cloroplasto durante el día y la queman en la mitocondria a todas horas, igual que cualquier animal. La fotosíntesis es lo que las plantas hacen <em>además</em>, no <em>en lugar de</em>.") + "</p>")}
{C.caja("tip", t("A check that saves memorizing", "Una comprobación que evita memorizar"), "<p>" + t("The two equations are the same one read in opposite directions. If you remember one, you get the other by swapping reactants and products. One more clue: photosynthesis needs light, so light goes on the left; respiration gives energy, so energy goes on the right.", "Las dos ecuaciones son la misma leída en direcciones opuestas. Si se recuerda una, la otra se obtiene invirtiendo reactivos y productos. Y hay una pista adicional: la fotosíntesis necesita luz, así que la luz va del lado izquierdo; la respiración produce energía, así que la energía va del derecho.") + "</p>")}
{P(t("Try it 1 · Reactants", "Pruebe 1 · Reactivos"), t("The reactants of photosynthesis are…", "Los reactivos de la fotosíntesis son…"),
   [t("glucose and oxygen", "glucosa y oxígeno"), t("carbon dioxide, water, and light", "dióxido de carbono, agua y luz"), t("water and energy", "agua y energía")], 1,
   {0: t("Those are its products, on the right of the arrow.", "Esos son sus productos, a la derecha de la flecha."), 2: t("Energy is a product of respiration.", "La energía es un producto de la respiración.")},
   t("Left of the arrow: 6 CO₂ + 6 H₂O + light.", "A la izquierda de la flecha: 6 CO₂ + 6 H₂O + luz."))}
{P(t("Try it 2 · Where?", "Pruebe 2 · ¿Dónde?"), t("Cellular respiration happens in…", "La respiración celular ocurre en…"),
   [t("the chloroplast, only in plants", "el cloroplasto, solo en plantas"), t("the nucleus of every cell", "el núcleo de todas las células"), t("the mitochondrion, in plants and in animals", "la mitocondria, tanto en plantas como en animales")], 2,
   {0: t("The chloroplast does photosynthesis.", "El cloroplasto hace la fotosíntesis."), 1: t("The nucleus holds the DNA.", "El núcleo guarda el ADN.")},
   t("The mitochondrion is the power plant of every eukaryotic cell.", "La mitocondria es la central eléctrica de toda célula eucariota."))}
{P(t("Try it 3 · At night", "Pruebe 3 · De noche"), t("At night, a plant…", "Durante la noche, una planta…"),
   [t("keeps carrying out cellular respiration, but not photosynthesis", "continúa realizando la respiración celular, pero no la fotosíntesis"), t("stops all activity", "detiene por completo toda actividad"), t("carries out photosynthesis faster", "realiza la fotosíntesis a mayor velocidad")], 0,
   {1: t("A living plant always needs energy.", "Una planta viva siempre necesita energía."), 2: t("Photosynthesis needs light.", "La fotosíntesis necesita luz.")},
   t("No light, no photosynthesis; respiration goes on day and night.", "Sin luz no hay fotosíntesis; la respiración sigue día y noche."))}
{C.enlace(N, anc("equations", "ecuaciones"), t("complete the equations", "complete las ecuaciones"), t("Fill in the missing parts and count the atoms on each side.", "Complete las partes que faltan y cuente los átomos de cada lado."))}
{C.enlace(N, anc("which-process", "que-proceso"), t("photosynthesis, respiration, or both?", "¿fotosíntesis, respiración o las dos?"), t("Sort each feature into the right process.", "Coloque cada característica en el proceso que le corresponde."))}"""

    s2 = f"""<p>{t("A carbon atom is neither made nor destroyed: it travels. The same atom that today is part of the carbon dioxide in the air may tomorrow be part of a leaf, then of a muscle, and later go back to the air. That trip is the <strong>carbon cycle</strong>, and the test checks it by asking about one specific stage.", "Un átomo de carbono no se crea ni se destruye: circula. El mismo átomo que hoy forma parte del dióxido de carbono atmosférico puede formar mañana parte de una hoja, después de un músculo y más tarde volver a la atmósfera. Ese recorrido es el <strong>ciclo del carbono</strong>, y el examen lo evalúa preguntando por una etapa concreta.")}</p>
{svg_carbono()}
{C.ejemplo(t("Example 1 · The trip of one atom", "Ejemplo 1 · El recorrido de un átomo"),
 [("", t("Follow a carbon atom from a CO₂ molecule in the air until it goes back to the air.", "Se sigue un átomo de carbono desde una molécula de CO₂ del aire hasta su regreso a la atmósfera.")),
  ("1", t("The leaf takes in the CO₂ and, through photosynthesis, builds that carbon into a glucose molecule.", "La hoja capta el CO₂ y, mediante la fotosíntesis, incorpora ese carbono a una molécula de glucosa.")),
  ("2", t("A plant eater eats the leaf. The carbon becomes part of its body, or is released right away if the animal burns that glucose.", "Un herbívoro come la hoja. El carbono pasa a formar parte de sus tejidos, o bien se libera de inmediato si el animal quema esa glucosa.")),
  ("3", t("When the animal dies, decomposers use its remains as food.", "Al morir el animal, los descomponedores utilizan sus restos como alimento.")),
  ("4", t("As they respire, the decomposers give the carbon back to the air as CO₂, and the cycle starts again.", "Al respirar, los descomponedores devuelven el carbono a la atmósfera en forma de CO₂, y el ciclo vuelve a empezar."))],
 t("<strong>There are shortcuts, too:</strong> carbon does not always make the full trip. The plant itself respires, so part of the carbon it just took in goes back to the air without passing through any animal. And another part can be locked away for millions of years if remains turn into coal or oil. Burning those fuels puts back, all at once, carbon that had been out of the cycle since before humans existed.", "<strong>Un atajo que también existe:</strong> el carbono no siempre recorre el ciclo completo. La propia planta respira, de modo que parte del carbono que acaba de fijar vuelve a la atmósfera sin pasar por ningún animal. Y otra parte puede quedar retenida durante millones de años si los restos se transforman en carbón o petróleo. Quemar esos combustibles reincorpora de golpe un carbono que llevaba fuera del ciclo desde antes de que existieran los seres humanos."))}
{P(t("Try it 4 · Out of the air", "Pruebe 4 · Fuera del aire"), t("In the carbon cycle, the process that takes CO₂ out of the air is…", "En el ciclo del carbono, el proceso que retira CO₂ de la atmósfera es…"),
   [t("the respiration of decomposers", "la respiración de los descomponedores"), t("photosynthesis", "la fotosíntesis"), t("the plant eater’s eating", "la alimentación del herbívoro")], 1,
   {0: t("Respiration gives CO₂ back to the air.", "La respiración devuelve CO₂ al aire."), 2: t("Eating moves carbon from plant to animal; the air is not involved.", "Comer pasa el carbono de la planta al animal; el aire no interviene.")},
   t("CO₂ is a reactant of photosynthesis: it is taken from the air.", "El CO₂ es un reactivo de la fotosíntesis: se toma del aire."))}
{P(t("Try it 5 · Fossil fuels", "Pruebe 5 · Combustibles fósiles"), t("Burning coal or oil affects the carbon cycle because it…", "Quemar carbón o petróleo afecta al ciclo del carbono porque…"),
   [t("removes carbon from the planet", "elimina carbono del planeta"), t("puts back in the air carbon that had been out of the cycle for millions of years", "devuelve a la atmósfera un carbono que llevaba millones de años fuera del ciclo"), t("stops plants from doing photosynthesis", "impide la fotosíntesis de las plantas")], 1,
   {0: t("Carbon is neither made nor destroyed.", "El carbono no se crea ni se destruye."), 2: t("Plants keep doing photosynthesis.", "Las plantas siguen haciendo la fotosíntesis.")},
   t("The carbon locked in fossil fuels goes back to the air all at once.", "El carbono retenido en los combustibles vuelve de golpe al aire."))}
{C.enlace(N, anc("carbon", "carbono"), t("follow the carbon", "siga al carbono"), t("Put the stages of the carbon trip in order.", "Ordene las etapas del recorrido del carbono."))}"""

    s3 = f"""<p>{t("If light is a reactant, you would expect more light to give more photosynthesis. That is what happens, but only up to a point. The graph below is one of the most common on the test, and you read it with the same five steps of Lesson 2.2.", "Si la luz es un reactivo, cabe esperar que a más luz haya más fotosíntesis. Y así ocurre, pero solo hasta cierto punto. La gráfica siguiente es de las que aparecen con más frecuencia en el examen, y se lee con los mismos cinco pasos de la Lección 2.2.")}</p>
<p><strong>{t("Rate of photosynthesis against light intensity", "Tasa fotosintética frente a intensidad luminosa")}</strong></p>
{graf_luz()}
{C.ejemplo(t("Example 2 · An extrapolation question", "Ejemplo 2 · Una pregunta de extrapolación"),
 [("", t("If, starting at 8 units of light, the intensity were doubled to 16, what would happen to the rate of photosynthesis?", "Si a partir de 8 unidades de luz se duplicara la intensidad hasta 16, ¿qué ocurriría con la tasa fotosintética?")),
  ("1", t("Look at the shape of the curve after 8: it has leveled off. Between 8 and 12 the rate barely changes.", "Se observa la forma de la curva más allá de 8: se ha aplanado. Entre 8 y 12 la tasa apenas varía.")),
  ("2", t("Light is no longer what limits the process. Another reactant (the CO₂ available) or the temperature is now the bottleneck.", "La luz ha dejado de ser el factor que limita el proceso. Otro reactivo —el CO₂ disponible— o la temperatura pasan a ser el cuello de botella.")),
  ("3", t("So you can expect the rate to stay about the same, not to double.", "Por tanto, cabe esperar que la tasa se mantenga aproximadamente igual, no que se duplique."))],
 t("<strong>How to word the answer:</strong> “If the trend shown continues, the rate will stay near 50.” Keep the condition, as in Lesson 2.2, because there are no measurements past 12.", "<strong>Cómo se formula la respuesta:</strong> «Si la tendencia observada se mantiene, la tasa permanecerá cerca de 50». Se conserva la condición, tal como se estableció en la Lección 2.2, porque más allá de 12 no hay ninguna medición."))}
{C.caja("tip", t("The limiting factor", "El factor limitante"), "<p>" + t("When a process depends on several reactants, its speed is always set by the one in shortest supply. Adding more of the others does nothing. It is the same logic as a factory with plenty of materials but only one worker: hiring more suppliers does not raise production.", "Cuando un proceso depende de varios reactivos, la velocidad la marca siempre el que está más escaso. Aumentar los demás no sirve de nada. Es la misma lógica de una fábrica que tiene material de sobra pero un solo operario: contratar más proveedores no aumenta la producción.") + "</p>")}
{P(t("Try it 6 · Reading the curve", "Pruebe 6 · Leer la curva"), t("If the light goes from 2 to 6 units, the rate of photosynthesis…", "Si en la gráfica la luz aumenta de 2 a 6 unidades, la tasa fotosintética…"),
   [t("rises from about 18 to about 45", "sube de 18 a 45 aproximadamente"), t("stays the same", "permanece constante"), t("goes down", "disminuye")], 0,
   {1: t("Between 2 and 6 the curve is still rising steeply.", "Entre 2 y 6 la curva todavía sube con fuerza."), 2: t("The curve never goes down.", "La curva nunca baja.")},
   t("Read the curve at 2 (18) and at 6 (45).", "Lea la curva en 2 (18) y en 6 (45)."))}
{P(t("Try it 7 · Past saturation", "Pruebe 7 · Más allá de la saturación"), t("Past the saturation point, more light does not raise the rate because…", "Más allá del punto de saturación, aumentar la luz no aumenta la tasa porque…"),
   [t("the plant no longer needs light", "la planta deja de necesitar luz"), t("the chloroplast is destroyed", "el cloroplasto se destruye"), t("light is no longer the limiting factor; another reactant is", "la luz ha dejado de ser el factor limitante y lo es ahora otro reactivo")], 2,
   {0: t("Light is still a reactant.", "La luz sigue siendo un reactivo."), 1: t("Nothing in the graph shows damage: the rate stays high.", "Nada en la gráfica indica daño: la tasa sigue alta.")},
   t("Now something else is in shortest supply: CO₂ or temperature.", "Ahora lo más escaso es otra cosa: el CO₂ o la temperatura."))}
{C.enlace(N, anc("limiting", "limitante"), t("rate graphs and limiting factors", "gráficas de tasa y factor limitante"), t("New curves every time: read values, find where they level off, and predict.", "Curvas nuevas cada vez: lea valores, localice dónde se aplanan y prediga."))}
{C.enlace(N, anc("day-night", "dia-noche"), t("gases by day and by night", "los gases de día y de noche"), t("Plants, animals, and closed jars: which gas goes in and which goes out?", "Plantas, animales y frascos cerrados: ¿qué gas entra y cuál sale?"))}"""

    s4 = f"""<p>{t("A short science text written for this level. It has numbers: read it with the checklist from Lesson 2.2.", "Texto científico breve adaptado al nivel. Contiene datos numéricos: conviene leerlo con la lista de verificación de la Lección 2.2.")}</p>
{C.lectura(t("A greenhouse test", "Un ensayo en invernadero"),
 [t("A farm research team wanted to find out what limited the growth of its tomato plants in winter. It set up four identical greenhouses and changed only one condition in each, keeping everything else the same.", "Un equipo agronómico quiso determinar qué factor limitaba el crecimiento de sus plantas de tomate en invierno. Preparó cuatro invernaderos idénticos y modificó en cada uno una sola condición, manteniendo constantes todas las demás."),
  t("In the first greenhouse, the control, the plants grew with natural winter light and the normal CO₂ level of the air. In the second, the light was doubled with lamps. In the third, the light stayed natural but the CO₂ level was raised. In the fourth, both were raised at once.", "En el primer invernadero, que sirvió de control, las plantas crecieron con la luz natural de invierno y la concentración de CO₂ del aire. En el segundo se duplicó la iluminación mediante lámparas. En el tercero se mantuvo la luz natural pero se elevó la concentración de CO₂. En el cuarto se aumentaron ambas cosas a la vez."),
  t("After six weeks, the dry mass of the plants was measured. The control group reached 42 grams per plant. The greenhouse with extra light reached 61 grams. The one with extra CO₂, 46. And the one with both, 78 grams.", "Al cabo de seis semanas se midió la masa seca de las plantas. El grupo de control alcanzó 42 gramos por planta. El invernadero con luz adicional llegó a 61 gramos. El de CO₂ adicional, a 46. Y el que recibió ambas mejoras alcanzó 78 gramos."),
  t("The team concluded that in winter the main limiting factor was light, since raising it alone gave a large improvement, while raising only the CO₂ barely changed the result. It warned, however, that the conclusion applies only to the winter conditions tested, and that the experiment cannot predict what would happen in summer.", "El equipo concluyó que en invierno el factor limitante principal era la luz, ya que aumentarla por sí sola produjo una mejora considerable, mientras que aumentar solo el CO₂ apenas modificó el resultado. Advirtió, sin embargo, que la conclusión se refiere únicamente a las condiciones invernales ensayadas y que el experimento no permite anticipar qué ocurriría en verano.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Carbon dioxide has no effect on plant growth.", "El dióxido de carbono no influye en el crecimiento de las plantas."), t("Tomato plants grow better in a greenhouse than outdoors.", "Las plantas de tomate crecen mejor en invernadero que al aire libre."), t("In the winter conditions tested, light was what limited growth.", "En las condiciones invernales ensayadas, la luz era el factor que limitaba el crecimiento.")], 2,
   {0: t("CO₂ did help a little (46 against 42), and a lot together with light.", "El CO₂ sí ayudó algo (46 frente a 42), y mucho junto con la luz."), 1: t("There was no outdoor group to compare with.", "No hubo grupo al aire libre para comparar.")},
   t("That is the team’s conclusion, with its limit: winter.", "Es la conclusión del equipo, con su límite: el invierno."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("How much more dry mass did the greenhouse with extra light have than the control?", "¿Cuál fue el aumento de masa seca del invernadero con luz adicional respecto del control?"),
   [t("19 grams per plant", "19 gramos por planta"), t("61 grams per plant", "61 gramos por planta"), t("4 grams per plant", "4 gramos por planta")], 0,
   {1: t("61 g is the total, not the increase.", "61 g es el total, no el aumento."), 2: t("4 g is the increase with extra CO₂.", "4 g es el aumento con CO₂ adicional.")},
   t("61 − 42 = 19 grams.", "61 − 42 = 19 gramos."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("Why did the team change only one condition in each greenhouse?", "¿Por qué el equipo modificó una sola condición en cada invernadero?"),
   [t("To save money", "Para ahorrar recursos"), t("To be able to link any difference to that one variable", "Para poder atribuir cualquier diferencia observada a esa única variable"), t("Because plants cannot stand two changes at once", "Porque las plantas no toleran dos cambios simultáneos")], 1,
   {0: t("The text gives a scientific reason, not a money reason.", "El texto da una razón científica, no económica."), 2: t("The fourth greenhouse had two changes and grew best.", "El cuarto invernadero tuvo dos cambios y fue el que más creció.")},
   t("Isolating the variable, as in Topic 1.", "Aislar la variable, como en el Tema 1."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Why do the authors not extend their conclusion to summer?", "¿Por qué los autores no extienden su conclusión al verano?"),
   [t("Because tomatoes are not grown in summer", "Porque en verano no se cultivan tomates"), t("Because CO₂ disappears in summer", "Porque el CO₂ desaparece en verano"), t("Because they did not measure in those conditions, and with more natural light the limiting factor could be something else", "Porque no midieron en esas condiciones y con más luz natural el factor limitante podría ser otro")], 2,
   {0: t("The text does not say that.", "El texto no dice eso."), 1: t("CO₂ is always in the air.", "El CO₂ está siempre en el aire.")},
   t("No data, no conclusion: in summer, with plenty of light, CO₂ might become the limit.", "Sin datos no hay conclusión: en verano, con luz de sobra, el límite podría ser el CO₂."))}"""

    G = lambda *a: C.ged_item(P, *a)
    burb = {"tipo": "tabla", "encabezados": [t("Distance from the lamp (cm)", "Distancia a la lámpara (cm)"), "10", "20", "30", "40", "50"],
            "filas": [[t("Bubbles of oxygen per minute", "Burbujas de oxígeno por minuto"), "48", "30", "17", "9", "5"]]}
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK).", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SP.6.b", "2", t(f"<em>Photosynthesis: {ec_foto()}</em><br>How many oxygen atoms are on the left side of the equation?", f"<em>Fotosíntesis: {ec_foto()}</em><br>¿Cuántos átomos de oxígeno hay en el lado izquierdo de la ecuación?"),
   ["8", "12", "18", "24"], 2,
   {0: t("Multiply each formula by the number in front: 6 CO₂ has 6 × 2 oxygen atoms.", "Multiplique cada fórmula por el número de delante: 6 CO₂ tiene 6 × 2 átomos de oxígeno."), 1: t("12 is only the oxygen in 6 CO₂. Add the oxygen in 6 H₂O.", "12 es solo el oxígeno de 6 CO₂. Sume el de 6 H₂O."), 3: t("Each H₂O has only one oxygen atom.", "Cada H₂O tiene un solo átomo de oxígeno.")},
   t("6 CO₂ → 6 × 2 = 12; 6 H₂O → 6 × 1 = 6; total 18. The right side also has 18 (6 in glucose + 12 in 6 O₂): atoms are neither made nor destroyed.", "6 CO₂ → 6 × 2 = 12; 6 H₂O → 6 × 1 = 6; total 18. El lado derecho también tiene 18 (6 en la glucosa + 12 en 6 O₂): los átomos no se crean ni se destruyen."))}
{G(2, "SP.3.b", "2", t("<em>A water plant was placed at different distances from a lamp, and the oxygen bubbles it gave off were counted.</em>", "<em>Se colocó una planta acuática a distintas distancias de una lámpara y se contaron las burbujas de oxígeno que desprendía.</em>") + C.grafica(burb, t("Data table", "Tabla de datos")) + t("Which conclusion do the data support?", "¿Qué conclusión apoyan los datos?"),
   [t("The closer the lamp, the faster the plant does photosynthesis.", "Cuanto más cerca la lámpara, más rápida es la fotosíntesis."), t("The plant does not need light.", "La planta no necesita luz."), t("The lamp heats the water, and heat makes the bubbles.", "La lámpara calienta el agua, y el calor produce las burbujas."), t("At 60 cm there would be no photosynthesis at all.", "A 60 cm no habría ninguna fotosíntesis.")], 0,
   {1: t("The bubbles change a lot with the light.", "Las burbujas cambian mucho con la luz."), 2: t("The data do not measure temperature: that would go beyond them.", "Los datos no miden la temperatura: sería ir más allá de ellos."), 3: t("The numbers go down but there is no reason to think they reach zero at 60 cm.", "Los números bajan, pero nada indica que lleguen a cero a 60 cm.")},
   t("More light (closer lamp) → more oxygen → more photosynthesis. That is all the data show.", "Más luz (lámpara más cerca) → más oxígeno → más fotosíntesis. Es lo que muestran los datos."))}
{G(3, "SP.3.c", "2–3", t("<em>Use the graph of the rate of photosynthesis against light intensity in section 3 (it levels off near 50 from 8 units on).</em><br>A grower raises the light from 10 to 14 units without changing anything else. What will most likely happen?", "<em>Use la gráfica de tasa fotosintética frente a intensidad luminosa de la sección 3 (se aplana en torno a 50 a partir de 8 unidades).</em><br>Un agricultor sube la luz de 10 a 14 unidades sin cambiar nada más. ¿Qué es lo más probable?"),
   [t("The rate rises to about 70.", "La tasa sube a unos 70."), t("The rate stays near 50.", "La tasa se mantiene cerca de 50."), t("The rate drops to 0.", "La tasa baja a 0."), t("The rate doubles.", "La tasa se duplica.")], 1,
   {0: t("The curve stopped rising at 8.", "La curva dejó de subir en 8."), 2: t("There is more light, not less.", "Hay más luz, no menos."), 3: t("Doubling would need light to still be the limiting factor.", "Duplicarse exigiría que la luz siguiera siendo el factor limitante.")},
   t("Past saturation, light is not the limit: if the trend continues, the rate stays near 50.", "Pasada la saturación, la luz no es el límite: si la tendencia sigue, la tasa se mantiene cerca de 50."))}
{G(4, "SP.7.a", "2–3", t("<em>In 1771, Joseph Priestley found that a mouse in a sealed jar soon fainted, but a mouse in a sealed jar with a mint plant, in the light, stayed active much longer.</em><br>Which explanation fits the model of photosynthesis and respiration?", "<em>En 1771, Joseph Priestley observó que un ratón en un frasco cerrado pronto se desmayaba, pero un ratón en un frasco cerrado con una planta de menta, a la luz, seguía activo mucho más tiempo.</em><br>¿Qué explicación encaja con el modelo de la fotosíntesis y la respiración?"),
   [t("The plant gave off oxygen that the mouse used in respiration.", "La planta liberó oxígeno, que el ratón usó en la respiración."), t("The plant gave off carbon dioxide that the mouse needed.", "La planta liberó dióxido de carbono, que el ratón necesitaba."), t("The plant took in the mouse’s oxygen.", "La planta absorbió el oxígeno del ratón."), t("The mint smell kept the mouse awake.", "El olor de la menta mantuvo despierto al ratón.")], 0,
   {1: t("Animals give off CO₂; they do not need it.", "Los animales liberan CO₂; no lo necesitan."), 2: t("That would make things worse for the mouse.", "Eso empeoraría la situación del ratón."), 3: t("That is not a scientific explanation.", "Esa no es una explicación científica.")},
   t("In the light, the plant’s photosynthesis gave off O₂ and used the mouse’s CO₂: what one makes, the other uses.", "A la luz, la fotosíntesis de la planta liberó O₂ y usó el CO₂ del ratón: lo que uno produce, el otro lo consume."))}
{G(5, "SP.1.c", "2", t("<em>Look at the carbon cycle diagram in section 2.</em><br>Which process moves carbon from the plant eater to the decomposers?", "<em>Observe el diagrama del ciclo del carbono de la sección 2.</em><br>¿Qué proceso lleva el carbono del herbívoro a los descomponedores?"),
   [t("Photosynthesis", "La fotosíntesis"), t("Eating", "La alimentación"), t("Death", "La muerte"), t("Decomposition", "La descomposición")], 2,
   {0: t("Photosynthesis goes from the air to the plant.", "La fotosíntesis va del aire a la planta."), 1: t("Eating goes from the plant to the plant eater.", "La alimentación va de la planta al herbívoro."), 3: t("Decomposition goes from the decomposers to the air.", "La descomposición va de los descomponedores al aire.")},
   t("The arrow from the plant eater to the decomposers is labeled “death.”", "La flecha del herbívoro a los descomponedores dice «muerte»."))}"""

    secciones = [
        ("s1", t("The two overall equations", "Las dos ecuaciones globales"), s1),
        ("s2", t("Follow the carbon", "Siga al carbono"), s2),
        ("s3", t("The rate of photosynthesis and its limit", "La tasa fotosintética y su límite"), s3),
        ("s4", t("Science reading", "Lectura científica"), s4),
        ("s5", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Build the equations.", "Arme las ecuaciones."), t("Write each part of the two equations on a separate card (reactants, arrow, products) and put them together without looking. Then check with the lesson.", "Escriba cada parte de las dos ecuaciones en una tarjeta separada (reactivos, flecha, productos) y ármelas sin mirar. Después compruébelas con la lección.")),
        (t("Trace the carbon.", "Trace el carbono."), t("Write the trip of a carbon atom in five stages, naming the process that causes each step.", "Escriba el recorrido de un átomo de carbono en cinco etapas, nombrando el proceso responsable de cada paso.")),
        (t("Read another curve.", "Lea otra curva."), t("Find a graph of how a living thing’s activity changes with temperature (for example, how fast yeast makes gas). Describe where it rises, where it levels off, and what you predict past the last point.", "Busque una gráfica de cómo cambia la actividad de un ser vivo con la temperatura (por ejemplo, la producción de gas de la levadura). Describa dónde sube, dónde se aplana y qué predice más allá del último punto.")),
    ]
    Q = t
    quiz = [
        (Q("The products of photosynthesis are…", "Los productos de la fotosíntesis son…"), [Q("carbon dioxide and water", "dióxido de carbono y agua"), Q("glucose and oxygen", "glucosa y oxígeno"), Q("water and light", "agua y luz"), Q("glucose and carbon dioxide", "glucosa y dióxido de carbono")], 1,
         {0: Q("Those are its reactants.", "Esos son sus reactivos."), 2: Q("Those are reactants.", "Esos son reactivos."), 3: Q("CO₂ is used, not made.", "El CO₂ se consume, no se produce.")}, Q("Right of the arrow: C₆H₁₂O₆ + 6 O₂.", "A la derecha de la flecha: C₆H₁₂O₆ + 6 O₂.")),
        (Q("The reactants of cellular respiration are…", "Los reactivos de la respiración celular son…"), [Q("glucose and oxygen", "glucosa y oxígeno"), Q("carbon dioxide and water", "dióxido de carbono y agua"), Q("light and water", "luz y agua"), Q("only glucose", "solo glucosa")], 0,
         {1: Q("Those are its products.", "Esos son sus productos."), 2: Q("Light belongs to photosynthesis.", "La luz es de la fotosíntesis."), 3: Q("It also needs oxygen.", "También necesita oxígeno.")}, Q("C₆H₁₂O₆ + 6 O₂ on the left.", "C₆H₁₂O₆ + 6 O₂ a la izquierda.")),
        (Q("In 6 CO₂ + 6 H₂O + light → C₆H₁₂O₆ + 6 O₂, the 6 in front of CO₂ means…", "En la ecuación 6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂, el número 6 delante del CO₂ indica…"), [Q("that the reaction repeats six times", "que la reacción se repite seis veces"), Q("how many carbon atoms each molecule has", "cuántos átomos de carbono tiene cada molécula"), Q("how many molecules of carbon dioxide take part", "cuántas moléculas de dióxido de carbono intervienen"), Q("the temperature of the process", "la temperatura del proceso")], 2,
         {0: Q("It counts molecules, not repetitions.", "Cuenta moléculas, no repeticiones."), 1: Q("Each CO₂ has one carbon atom; the small number tells atoms.", "Cada CO₂ tiene un átomo de carbono; el número pequeño cuenta átomos."), 3: Q("Equations do not show temperature that way.", "Las ecuaciones no indican así la temperatura.")}, Q("The large number in front counts molecules.", "El número grande de delante cuenta moléculas.")),
        (Q("The energy released by cellular respiration is available to the cell as…", "La energía liberada por la respiración celular queda disponible para la célula en forma de…"), [Q("glucose", "glucosa"), Q("oxygen", "oxígeno"), Q("water", "agua"), Q("ATP", "ATP")], 3,
         {0: Q("Glucose is what gets burned.", "La glucosa es lo que se quema."), 1: Q("Oxygen is a reactant.", "El oxígeno es un reactivo."), 2: Q("Water is a product, but it carries no energy.", "El agua es un producto, pero no transporta energía.")}, Q("The cell’s usable energy is ATP.", "La energía utilizable de la célula es el ATP.")),
        (Q("Which statement is correct?", "¿Cuál de estas afirmaciones es correcta?"), [Q("Only animals carry out cellular respiration", "Solo los animales realizan la respiración celular"), Q("Plants carry out both photosynthesis and cellular respiration", "Las plantas realizan tanto la fotosíntesis como la respiración celular"), Q("Plants only carry out photosynthesis", "Las plantas solo realizan la fotosíntesis"), Q("Cellular respiration happens in the chloroplast", "La respiración celular ocurre en el cloroplasto")], 1,
         {0: Q("Plants respire too.", "Las plantas también respiran."), 2: Q("They also have mitochondria.", "También tienen mitocondrias."), 3: Q("It happens in the mitochondrion.", "Ocurre en la mitocondria.")}, Q("Photosynthesis is what plants do in addition, not instead.", "La fotosíntesis es lo que las plantas hacen además, no en lugar de.")),
        (Q("Photosynthesis and cellular respiration go together because…", "La fotosíntesis y la respiración celular son procesos complementarios porque…"), [Q("they happen in the same organelle", "ocurren en el mismo organelo"), Q("both need light", "ambos requieren luz"), Q("the products of each are the reactants of the other", "los productos de cada uno son los reactivos del otro"), Q("both release energy", "ambos liberan energía")], 2,
         {0: Q("Chloroplast and mitochondrion are different.", "Cloroplasto y mitocondria son distintos."), 1: Q("Only photosynthesis needs light.", "Solo la fotosíntesis necesita luz."), 3: Q("Photosynthesis stores energy.", "La fotosíntesis almacena energía.")}, Q("What one makes, the other uses.", "Lo que uno produce, el otro lo consume.")),
        (Q("At night a plant does no photosynthesis but does respire. So at night the plant…", "Durante la noche una planta no realiza la fotosíntesis, pero sí la respiración. Por tanto, de noche la planta…"), [Q("uses oxygen and gives off carbon dioxide", "consume oxígeno y libera dióxido de carbono"), Q("gives off oxygen and uses carbon dioxide", "libera oxígeno y consume dióxido de carbono"), Q("exchanges no gases", "no intercambia gases"), Q("no longer needs energy", "deja de necesitar energía")], 0,
         {1: Q("That is photosynthesis, which needs light.", "Eso es la fotosíntesis, que necesita luz."), 2: Q("Respiration exchanges gases.", "La respiración intercambia gases."), 3: Q("A living plant always needs energy.", "Una planta viva siempre necesita energía.")}, Q("Respiration only: O₂ in, CO₂ out.", "Solo respiración: entra O₂ y sale CO₂.")),
        (Q("In the lesson’s graph, at 4 units of light the rate of photosynthesis is about…", "Según la gráfica de la lección, cuando la intensidad luminosa vale 4 unidades la tasa fotosintética es de aproximadamente…"), ["18", "34", "45", "50"], 1,
         {0: Q("18 is at 2 units.", "18 corresponde a 2 unidades."), 2: Q("45 is at 6 units.", "45 corresponde a 6 unidades."), 3: Q("50 is the level after 8 units.", "50 es el nivel a partir de 8.")}, Q("Go up from 4 to the curve and across: 34.", "Suba desde 4 hasta la curva y lea: 34.")),
        (Q("The part of the graph where the curve levels off is…", "La zona de la gráfica en la que la curva se aplana corresponde a…"), [Q("a measuring error", "un error de medición"), Q("the death of the plant", "la muerte de la planta"), Q("the light saturation point", "el punto de saturación lumínica"), Q("the start of respiration", "el inicio de la respiración")], 2,
         {0: Q("The values are steady, not wrong.", "Los valores son estables, no erróneos."), 1: Q("The rate stays high.", "La tasa sigue alta."), 3: Q("Respiration goes on all the time.", "La respiración ocurre siempre.")}, Q("More light no longer helps: saturation.", "Más luz ya no ayuda: saturación.")),
        (Q("If the light went from 10 to 20 units, you could expect the rate to…", "Si la intensidad luminosa pasara de 10 a 20 unidades, cabría esperar que la tasa fotosintética…"), [Q("double", "se duplicara"), Q("stay about the same, if the trend shown continues", "se mantuviera aproximadamente igual, si la tendencia observada continúa"), Q("drop to zero", "descendiera a cero"), Q("grow without end", "creciera de forma indefinida")], 1,
         {0: Q("The curve is already flat.", "La curva ya es plana."), 2: Q("More light does not stop the process.", "Más luz no detiene el proceso."), 3: Q("The curve has leveled off.", "La curva se aplanó.")}, Q("Keep the condition: if the trend continues, about 50.", "Conserve la condición: si la tendencia continúa, unos 50.")),
        (Q("A limiting factor is one that…", "Un factor limitante es aquel que…"), [Q("is present in the largest amount", "aparece en mayor cantidad en la reacción"), Q("sets the speed of the process because it is in shortest supply", "marca la velocidad del proceso por estar más escaso"), Q("acts only at night", "solo actúa de noche"), Q("stops every chemical reaction", "impide toda reacción química")], 1,
         {0: Q("It is the opposite: the scarcest.", "Es lo contrario: el más escaso."), 2: Q("It has nothing to do with night.", "No tiene que ver con la noche."), 3: Q("It slows the process; it does not stop everything.", "Frena el proceso; no lo detiene todo.")}, Q("The scarcest reactant sets the pace.", "El reactivo más escaso marca el ritmo.")),
        (Q("In the greenhouse test, raising only the CO₂ barely helped. The reasonable conclusion is that…", "En el experimento del invernadero, aumentar solo el CO₂ apenas mejoró el resultado. La conclusión razonable es que…"), [Q("CO₂ plays no part in photosynthesis", "el CO₂ no interviene en la fotosíntesis"), Q("the experiment was badly designed", "el experimento estuvo mal diseñado"), Q("plants do not take in CO₂ in winter", "las plantas no absorben CO₂ en invierno"), Q("in those conditions, CO₂ was not the limiting factor", "en esas condiciones el CO₂ no era el factor limitante")], 3,
         {0: Q("CO₂ is a reactant.", "El CO₂ es un reactivo."), 1: Q("It isolated each variable well.", "Aisló bien cada variable."), 2: Q("With light and CO₂ together, the plants grew most.", "Con luz y CO₂ juntos, las plantas crecieron más.")}, Q("Light was scarcer than CO₂ in winter.", "En invierno, la luz era más escasa que el CO₂.")),
    ]
    filas = [
        (t("Name reactants and products", "Identifica reactivos y productos"), t("I name them for both processes and say in which organelle each happens.", "Los identifico en los dos procesos y señalo en qué organelo ocurre cada uno."), t("I know them for one process, but not the other.", "Los identifico en uno de los procesos, pero no en el otro."), t("I mix up reactants and products, or the two processes.", "Confundo reactivos con productos o mezclo los procesos.")),
        (t("Explain how the two processes are linked", "Explica la relación entre ambos procesos"), t("I explain that the products of each are the reactants of the other, and that plants do both.", "Explico que los productos de cada uno son los reactivos del otro, y que las plantas hacen los dos."), t("I say they are related, but not how.", "Digo que están relacionados, pero no en qué."), t("I present them as separate or as alternatives.", "Los presento como independientes o alternativos.")),
        (t("Trace carbon through the cycle", "Rastrea el carbono en el ciclo"), t("I trace the full trip, naming each process, and know the shortcuts (the plant’s own respiration, fossil fuels).", "Trazo el recorrido completo nombrando cada proceso y reconozco los atajos (la respiración de la planta, los combustibles fósiles)."), t("I order the stages but do not name the processes.", "Ordeno las etapas, pero no nombro los procesos."), t("I cannot put the stages in order.", "No logro ordenar las etapas.")),
        (t("Read and extend a rate graph", "Interpreta y extrapola una gráfica de tasa"), t("I find the saturation point, extrapolate keeping the condition, and explain it with the limiting factor.", "Localizo la saturación, extrapolo conservando la condición y lo explico con el factor limitante."), t("I read values correctly but extend the line without noticing it levels off.", "Leo valores correctamente, pero extrapolo sin advertir la saturación."), t("I read wrong values or do not see where the curve is flat.", "Leo valores incorrectos o no distingo la meseta.")),
    ]
    cierre = "<p>" + t("This lesson closed the energy circuit of the cell and left two ideas that come back in several topics: <strong>matter cycles while energy changes form</strong>, and every process with several reactants has a <strong>limiting factor</strong> that sets its pace.", "Esta lección cerró el circuito de la energía en la célula y dejó dos ideas que reaparecerán en varios temas: que <strong>la materia circula mientras la energía se transforma</strong>, y que en todo proceso con varios reactivos existe un <strong>factor limitante</strong> que marca el ritmo.") + "</p><p>" + \
             t("Lesson 3.3 closes Topic 3 by moving up in scale, from the cell to the whole body: the five main body systems and how they work together, the negative feedback that keeps temperature and glucose steady (the same mechanism as the body-temperature text in Lesson 1.3), and how to read real public health data.", "La Lección 3.3 cierra el Tema 3 subiendo de escala: de la célula al organismo completo. Se estudiarán los cinco sistemas principales y sus interacciones, la retroalimentación negativa que mantiene estables la temperatura y la glucosa —el mismo mecanismo del texto sobre termorregulación de la Lección 1.3— y la lectura de datos reales de salud pública.") + "</p>"
    glosario = [
        (t("Reactant / product", "Reactivo / producto"), t("What a reaction uses up / what it makes.", "Lo que una reacción consume / lo que produce.")),
        (t("Photosynthesis", "Fotosíntesis"), t("Making glucose and oxygen from carbon dioxide, water, and light, in the chloroplast.", "Fabricación de glucosa y oxígeno a partir de dióxido de carbono, agua y luz, en el cloroplasto.")),
        (t("Cellular respiration", "Respiración celular"), t("Burning glucose with oxygen to release usable energy (ATP), in the mitochondrion.", "Combustión de la glucosa con oxígeno para liberar energía utilizable (ATP), en la mitocondria.")),
        (t("ATP", "ATP"), t("The molecule that carries usable energy inside the cell.", "Molécula que transporta la energía utilizable dentro de la célula.")),
        (t("Carbon cycle", "Ciclo del carbono"), t("The path carbon follows between the air, living things, the soil, and the oceans.", "Recorrido del carbono entre la atmósfera, los seres vivos, el suelo y los océanos.")),
        (t("Decomposer", "Descomponedor"), t("A living thing, such as a fungus or bacterium, that feeds on dead remains.", "Ser vivo, como un hongo o una bacteria, que se alimenta de restos muertos.")),
        (t("Saturation point", "Punto de saturación"), t("Where more of a factor no longer raises the rate.", "Punto a partir del cual aumentar un factor ya no aumenta la tasa.")),
        (t("Limiting factor", "Factor limitante"), t("The factor in shortest supply, which sets the speed of a process.", "El factor más escaso, que marca la velocidad de un proceso.")),
    ]
    estd = C.estandares(["SP.6.b", "SP.3.b", "SP.3.c", "SP.7.a"], ["L.b", "L.c"], base=["SP.1.c"])
    conexion = "<p>" + t("Lesson 3.1 introduced the chloroplast and the mitochondrion as two names on a list of organelles. This lesson puts them to work: they are the two rooms where energy enters life and where it is released.", "La Lección 3.1 presentó el cloroplasto y la mitocondria como dos nombres de una lista de organelos. Esta lección los pone a funcionar: son las dos cámaras donde la energía entra en la vida y donde se libera.") + "</p><p>" + \
               t("There is a reason the equations appear here and not in a chemistry topic. A chemical equation is, as practice SP.6 says, a way of expressing a process with numbers and symbols: the same skill that in Topic 2 took you from a table to a graph now takes you from a biological process to an expression with numbers. You do not memorize it: you read it.", "Y hay una razón para que las ecuaciones aparezcan aquí y no en un tema de química. Una ecuación química es, como dice la práctica SP.6, una manera de expresar un fenómeno con números y símbolos: la misma destreza que en el Tema 2 permitía pasar de una tabla a una gráfica permite ahora pasar de un proceso biológico a una expresión con números. No se memoriza: se lee.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> build the equations with cards before writing them. Moving the pieces to one side of the arrow or the other fixes the difference between reactant and product much better than copying the finished equation.", "<strong>Cómo estudiar esta lección:</strong> arme las ecuaciones con tarjetas antes de escribirlas. Manipular las piezas y colocarlas a un lado u otro de la flecha fija la distinción entre reactivo y producto mucho mejor que copiar la ecuación ya hecha.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("The chloroplast stores energy and the mitochondrion releases it: two equations, one cycle, and a limit.", "El cloroplasto almacena la energía y la mitocondria la libera: dos ecuaciones, un ciclo y un límite."),
        ["SP.6 · " + t("Expressing science information", "Expresar información científica"), "SP.3 · " + t("Reasoning from data", "Razonar a partir de datos")],
        [t("<strong>Write and read</strong> the overall equations of photosynthesis and cellular respiration.", "<strong>Escribir e interpretar</strong> las ecuaciones globales de la fotosíntesis y de la respiración celular."),
         t("<strong>Name</strong> the reactants and products of each process and where each one happens.", "<strong>Identificar</strong> los reactivos y los productos de cada proceso y señalar dónde ocurre cada uno."),
         t("<strong>Explain</strong> how the two processes depend on each other and why neither would be enough alone.", "<strong>Explicar</strong> la relación complementaria entre ambos procesos y por qué ninguno bastaría por sí solo."),
         t("<strong>Trace</strong> a carbon atom around the cycle, from the air back to the air.", "<strong>Rastrear</strong> el recorrido de un átomo de carbono a lo largo del ciclo, de la atmósfera a la atmósfera."),
         t("<strong>Read</strong> a graph of the rate of photosynthesis against light and extend it past the saturation point.", "<strong>Interpretar</strong> una gráfica de tasa fotosintética frente a intensidad luminosa y extrapolar más allá del punto de saturación.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("3-3", t("Human body systems, homeostasis, and health", "Sistemas del cuerpo humano, homeostasis y salud")), glosario, P)


# ---------------------------------------------------------------- práctica
def huecos_ecuaciones():
    CO2, H2O, GLU, O2 = "CO₂", "H₂O", "C₆H₁₂O₆", "O₂"
    L, E = t("light", "luz"), t("energy", "energía")
    S = [CO2, H2O, GLU, O2]
    return [
        {"partes": [t("Photosynthesis: 6 ", "Fotosíntesis: 6 "), {"ops": S, "ok": 0}, " + 6 ", {"ops": S, "ok": 1}, f" + {L} → ", {"ops": S, "ok": 2}, " + 6 ", {"ops": S, "ok": 3}],
         "pista": t("What does the plant take in from the air and the soil? What does it make?", "¿Qué toma la planta del aire y del suelo? ¿Qué fabrica?"),
         "exp": t("6 CO₂ + 6 H₂O + light → C₆H₁₂O₆ + 6 O₂. The plant takes in carbon dioxide and water and makes glucose and oxygen.", "6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂. La planta toma dióxido de carbono y agua, y fabrica glucosa y oxígeno.")},
        {"partes": [t("Cellular respiration: ", "Respiración celular: "), {"ops": S, "ok": 2}, " + 6 ", {"ops": S, "ok": 3}, " → 6 ", {"ops": S, "ok": 0}, " + 6 ", {"ops": S, "ok": 1}, f" + {E}"],
         "pista": t("It is the photosynthesis equation read backward.", "Es la ecuación de la fotosíntesis leída al revés."),
         "exp": t("C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + energy: glucose is burned with oxygen.", "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + energía: la glucosa se quema con oxígeno.")},
        {"partes": [t("Light goes on the ", "La luz va del lado "), {"ops": [t("left", "izquierdo"), t("right", "derecho")], "ok": 0}, t(" of the photosynthesis equation, because it is ", " de la ecuación de la fotosíntesis, porque es "), {"ops": [t("a reactant", "un reactivo"), t("a product", "un producto")], "ok": 0},
                    t("; energy goes on the ", "; la energía va del lado "), {"ops": [t("left", "izquierdo"), t("right", "derecho")], "ok": 1}, t(" of the respiration equation, because it is ", " de la ecuación de la respiración, porque es "), {"ops": [t("a reactant", "un reactivo"), t("a product", "un producto")], "ok": 1}, "."],
         "pista": t("Photosynthesis needs light; respiration gives energy.", "La fotosíntesis necesita luz; la respiración produce energía."),
         "exp": t("What a process needs goes on the left; what it gives, on the right.", "Lo que un proceso necesita va a la izquierda; lo que da, a la derecha.")},
        {"partes": [t("Photosynthesis happens in the ", "La fotosíntesis ocurre en el "), {"ops": [t("chloroplast", "cloroplasto"), t("mitochondrion", "mitocondria"), t("nucleus", "núcleo")], "ok": 0},
                    t(" and stores energy; respiration happens in the ", " y almacena energía; la respiración ocurre en la "), {"ops": [t("chloroplast", "cloroplasto"), t("mitochondrion", "mitocondria"), t("nucleus", "núcleo")], "ok": 1},
                    t(" and ", " y "), {"ops": [t("releases", "libera"), t("stores", "almacena")], "ok": 0}, t(" it.", " esa energía.")],
         "pista": t("The solar panel and the power plant of the cell.", "El panel solar y la central eléctrica de la célula."),
         "exp": t("Chloroplast: stores energy in glucose. Mitochondrion: releases it as ATP.", "Cloroplasto: almacena la energía en la glucosa. Mitocondria: la libera como ATP.")},
    ]


def atomos():
    """Preguntas de conteo de átomos (respuesta escrita)."""
    F, R = t("photosynthesis", "la fotosíntesis"), t("respiration", "la respiración")
    d = [
        (t("How many carbon atoms are in one glucose molecule, C₆H₁₂O₆?", "¿Cuántos átomos de carbono tiene una molécula de glucosa, C₆H₁₂O₆?"), 6, t("The small 6 after C: 6 carbon atoms.", "El 6 pequeño después de C: 6 átomos de carbono.")),
        (t("How many hydrogen atoms are in one glucose molecule, C₆H₁₂O₆?", "¿Cuántos átomos de hidrógeno tiene una molécula de glucosa, C₆H₁₂O₆?"), 12, t("H₁₂: 12 hydrogen atoms.", "H₁₂: 12 átomos de hidrógeno.")),
        (t("How many atoms in all are in one glucose molecule, C₆H₁₂O₆?", "¿Cuántos átomos en total tiene una molécula de glucosa, C₆H₁₂O₆?"), 24, t("6 + 12 + 6 = 24.", "6 + 12 + 6 = 24.")),
        (t("In 6 CO₂, how many oxygen atoms are there?", "En 6 CO₂, ¿cuántos átomos de oxígeno hay?"), 12, t("6 molecules × 2 oxygen atoms = 12.", "6 moléculas × 2 átomos de oxígeno = 12.")),
        (t("In 6 H₂O, how many hydrogen atoms are there?", "En 6 H₂O, ¿cuántos átomos de hidrógeno hay?"), 12, t("6 molecules × 2 hydrogen atoms = 12.", "6 moléculas × 2 átomos de hidrógeno = 12.")),
        (t(f"In {F} (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂), how many oxygen atoms are on the left side?", f"En {F} (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂), ¿cuántos átomos de oxígeno hay en el lado izquierdo?"), 18, t("6 × 2 + 6 × 1 = 12 + 6 = 18.", "6 × 2 + 6 × 1 = 12 + 6 = 18.")),
        (t(f"In {F} (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂), how many oxygen atoms are on the right side?", f"En {F} (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂), ¿cuántos átomos de oxígeno hay en el lado derecho?"), 18, t("6 in glucose + 6 × 2 in O₂ = 18. The same as on the left.", "6 en la glucosa + 6 × 2 en O₂ = 18. Igual que a la izquierda.")),
        (t(f"In {F}, how many carbon atoms are on each side?", f"En {F}, ¿cuántos átomos de carbono hay en cada lado?"), 6, t("Left: 6 CO₂ → 6. Right: C₆ → 6.", "Izquierda: 6 CO₂ → 6. Derecha: C₆ → 6.")),
        (t(f"In {R} (C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O), how many hydrogen atoms are on the right side?", f"En {R} (C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O), ¿cuántos átomos de hidrógeno hay en el lado derecho?"), 12, t("6 H₂O → 6 × 2 = 12, the same 12 as in the glucose.", "6 H₂O → 6 × 2 = 12, los mismos 12 de la glucosa.")),
        (t("How many O₂ molecules does a cell need to burn one glucose molecule?", "¿Cuántas moléculas de O₂ necesita una célula para quemar una molécula de glucosa?"), 6, t("C₆H₁₂O₆ + 6 O₂: six.", "C₆H₁₂O₆ + 6 O₂: seis.")),
        (t("A plant makes 3 glucose molecules. How many CO₂ molecules did it take in?", "Una planta fabrica 3 moléculas de glucosa. ¿Cuántas moléculas de CO₂ tomó?"), 18, t("6 CO₂ per glucose: 3 × 6 = 18.", "6 CO₂ por cada glucosa: 3 × 6 = 18.")),
        (t("A cell burns 2 glucose molecules. How many CO₂ molecules does it give off?", "Una célula quema 2 moléculas de glucosa. ¿Cuántas moléculas de CO₂ libera?"), 12, t("6 CO₂ per glucose: 2 × 6 = 12.", "6 CO₂ por cada glucosa: 2 × 6 = 12.")),
        (t("A plant makes 4 glucose molecules. How many O₂ molecules does it give off?", "Una planta fabrica 4 moléculas de glucosa. ¿Cuántas moléculas de O₂ libera?"), 24, t("6 O₂ per glucose: 4 × 6 = 24.", "6 O₂ por cada glucosa: 4 × 6 = 24.")),
    ]
    return [{"enun": f"<p>{q}</p>", "r": r, "exp": e} for q, r, e in d]


def clasif_procesos():
    G = [t("Photosynthesis only", "Solo la fotosíntesis"), t("Cellular respiration only", "Solo la respiración celular"), t("Both processes", "Los dos procesos")]
    PF = t("Does it need light or make glucose?", "¿Necesita luz o fabrica glucosa?")
    PR = t("Does it burn glucose or give off CO₂?", "¿Quema glucosa o libera CO₂?")
    PA = t("Is it true of both?", "¿Es cierto de los dos?")
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("Decide whether each statement is true of photosynthesis, of cellular respiration, or of both.", "Decida si cada afirmación es cierta de la fotosíntesis, de la respiración celular o de las dos."),
                "grupos": G, "etiqueta": t("Process:", "Proceso:"), "piezas": [{"t": a, "v": v, "pista": [PF, PR, PA][v]} for a, v in piezas],
                "extra": t("Plants do both; animals only respire.", "Las plantas hacen los dos; los animales solo respiran.")}
    return [
        item(t("Set 1", "Grupo 1"), [(t("It needs light.", "Necesita luz."), 0), (t("It happens in the mitochondrion.", "Ocurre en la mitocondria."), 1), (t("It happens in plant cells.", "Ocurre en las células vegetales."), 2),
                                    (t("It gives off oxygen.", "Libera oxígeno."), 0), (t("It gives off carbon dioxide.", "Libera dióxido de carbono."), 1)]),
        item(t("Set 2", "Grupo 2"), [(t("It goes on day and night.", "Ocurre de día y de noche."), 1), (t("It stores energy in glucose.", "Almacena energía en la glucosa."), 0), (t("It involves water.", "Interviene el agua."), 2),
                                    (t("It happens in animal cells.", "Ocurre en las células animales."), 1), (t("It uses carbon dioxide.", "Consume dióxido de carbono."), 0)]),
        item(t("Set 3", "Grupo 3"), [(t("It makes ATP the cell can use.", "Produce ATP que la célula puede usar."), 1), (t("It happens in the chloroplast.", "Ocurre en el cloroplasto."), 0), (t("Its equation includes glucose.", "Su ecuación incluye la glucosa."), 2),
                                    (t("It uses oxygen.", "Consume oxígeno."), 1), (t("It is part of the carbon cycle.", "Forma parte del ciclo del carbono."), 2)]),
    ]


def ordenes_carbono():
    return [
        {"titulo": t("The carbon trip · Through a food chain", "El viaje del carbono · Por una cadena alimentaria"),
         "intro": t("Follow a carbon atom from the air back to the air. Put the five steps in order with ▲ and ▼.", "Siga un átomo de carbono desde el aire hasta su regreso al aire. Ordene los cinco pasos con ▲ y ▼."),
         "pasos": [t("A CO₂ molecule is in the air.", "Una molécula de CO₂ está en el aire."), t("A leaf takes in the CO₂ and builds the carbon into glucose (photosynthesis).", "Una hoja capta el CO₂ e incorpora el carbono a la glucosa (fotosíntesis)."),
                   t("A rabbit eats the leaf, and the carbon becomes part of its body (eating).", "Un conejo come la hoja y el carbono pasa a sus tejidos (alimentación)."), t("The rabbit dies, and fungi and bacteria feed on its remains (death).", "El conejo muere y los hongos y las bacterias se alimentan de sus restos (muerte)."),
                   t("As they respire, the decomposers give off the carbon as CO₂ (decomposition).", "Al respirar, los descomponedores liberan el carbono como CO₂ (descomposición).")],
         "inicio": [4, 2, 0, 3, 1],
         "cons": {"2>1": t("The rabbit cannot eat carbon that is not yet in the leaf: photosynthesis comes first.", "El conejo no puede comer un carbono que aún no está en la hoja: primero va la fotosíntesis."),
                  "3>2": t("Decomposers feed on remains: the rabbit must eat and live before it dies.", "Los descomponedores se alimentan de restos: el conejo tiene que comer y vivir antes de morir."),
                  "4>3": t("The decomposers need remains to feed on before they can give off that carbon.", "Los descomponedores necesitan restos de los que alimentarse antes de liberar ese carbono.")},
         "general": t("Air → plant → plant eater → decomposers → air.", "Aire → planta → herbívoro → descomponedores → aire.")},
        {"titulo": t("The carbon trip · The long way", "El viaje del carbono · El camino largo"),
         "intro": t("Some carbon stays out of the cycle for millions of years. Put the steps in order.", "Parte del carbono queda fuera del ciclo durante millones de años. Ordene los pasos."),
         "pasos": [t("Ancient plants take in CO₂ from the air through photosynthesis.", "Plantas antiguas captan CO₂ del aire mediante la fotosíntesis."), t("The plants die and are buried under mud before they rot.", "Las plantas mueren y quedan enterradas bajo el lodo antes de pudrirse."),
                   t("Over millions of years, heat and pressure turn the remains into coal.", "Durante millones de años, el calor y la presión transforman los restos en carbón."), t("People dig up the coal and burn it in a power plant.", "Se extrae el carbón y se quema en una central eléctrica."),
                   t("The carbon goes back into the air as CO₂, all at once.", "El carbono vuelve de golpe al aire como CO₂.")],
         "inicio": [3, 0, 4, 1, 2],
         "cons": {"2>1": t("Coal forms from buried remains: the plants must die and be buried first.", "El carbón se forma a partir de restos enterrados: primero las plantas deben morir y quedar sepultadas."),
                  "3>2": t("You cannot burn coal that has not formed yet.", "No se puede quemar un carbón que aún no se ha formado."),
                  "4>3": t("The CO₂ is released when the coal is burned.", "El CO₂ se libera al quemar el carbón.")},
         "general": t("Burial takes carbon out of the cycle; burning fossil fuels puts it back all at once.", "El enterramiento saca el carbono del ciclo; quemar combustibles fósiles lo devuelve de golpe.")},
    ]


def banco_limitante():
    rnd = random.Random(32)
    out = []
    contextos = [
        (t("Rate of photosynthesis against light intensity", "Tasa fotosintética frente a intensidad luminosa"), t("Light (units)", "Luz (unidades)"), t("Rate (units/min)", "Tasa (unid./min)"), t("light", "la luz"), t("Another factor, such as CO₂ or temperature, now limits the rate.", "Otro factor, como el CO₂ o la temperatura, limita ahora la tasa.")),
        (t("Rate of photosynthesis against CO₂ level", "Tasa fotosintética frente a concentración de CO₂"), t("CO₂ (units)", "CO₂ (unidades)"), t("Rate (units/min)", "Tasa (unid./min)"), t("CO₂", "el CO₂"), t("Another factor, such as light or temperature, now limits the rate.", "Otro factor, como la luz o la temperatura, limita ahora la tasa.")),
        (t("Oxygen given off by algae against light intensity", "Oxígeno liberado por algas frente a intensidad luminosa"), t("Light (units)", "Luz (unidades)"), t("Oxygen (mL/h)", "Oxígeno (mL/h)"), t("light", "la luz"), t("Another factor, such as CO₂ or temperature, now limits the rate.", "Otro factor, como el CO₂ o la temperatura, limita ahora la tasa.")),
    ]
    for n in range(18):
        tit, xe, ye, fac, otro = contextos[n % 3]
        M = rnd.choice([40, 50, 60, 70, 80])
        s = rnd.choice([1.6, 2.0, 2.4])
        pts = [[x, round(M * (1 - math.exp(-x / s)))] for x in range(0, 13, 2)]
        sat = next(x for x, y in pts if y >= pts[-1][1] - 2)
        sp = {"tipo": "linea", "xEtq": xe, "yEtq": ye, "px": 2, "series": [{"nombre": "", "puntos": pts}]}
        g = f"<p><strong>{tit}</strong></p>" + C.grafica(sp, C.describe(sp), ancho=520, alto=290)
        q = n % 4
        if q == 0:
            x = rnd.choice([2, 4, 6]); y = dict(pts)[x]
            ops = [str(y)] + [str(v) for v in rnd.sample([v for _, v in pts if abs(v - y) > 3], 3)]
            out.append({"enun": g + "<p><strong>" + t(f"What is the rate at {x} units?", f"¿Cuál es la tasa con {x} unidades?") + "</strong></p>", "ops": ops, "ok": 0,
                        "pista": t("Go up from the value on the horizontal axis to the line, then across to the vertical axis.", "Suba desde el valor del eje horizontal hasta la línea y lea en el eje vertical."), "exp": t(f"At {x} units the line is at {y}.", f"Con {x} unidades la línea está en {y}.")})
        elif q == 1:
            cands = sorted({sat, max(sat - 4, 2), min(sat + 4, 12), 0} if sat > 2 else {2, 6, 10, 0})
            ops = [str(sat)] + [str(c) for c in cands if c != sat][:3]
            out.append({"enun": g + "<p><strong>" + t("From about what value on the horizontal axis does the curve level off?", "¿A partir de qué valor del eje horizontal, aproximadamente, se aplana la curva?") + "</strong></p>", "ops": ops, "ok": 0,
                        "pista": t("Find where the line stops rising and becomes nearly flat.", "Busque dónde la línea deja de subir y se vuelve casi plana."),
                        "exp": t(f"From about {sat} on, the values barely change (they stay near {pts[-1][1]}).", f"A partir de unas {sat} unidades, los valores apenas cambian (se mantienen cerca de {pts[-1][1]}).")})
        elif q == 2:
            top = pts[-1][1]
            ops = [t(f"It would stay near {top}.", f"Se mantendría cerca de {top}."), t(f"It would rise to about {top * 2}.", f"Subiría a unos {top * 2}."), t("It would drop to zero.", "Bajaría a cero."), t(f"It would rise to about {top + 20}.", f"Subiría a unos {top + 20}.")]
            out.append({"enun": g + "<p><strong>" + t("If the value on the horizontal axis went to 20, what would most likely happen to the rate, if the trend continues?", "Si el valor del eje horizontal llegara a 20, ¿qué es lo más probable que le pasara a la tasa, si la tendencia continúa?") + "</strong></p>", "ops": ops, "ok": 0,
                        "pista": t("Look at the last part of the curve: is it still rising?", "Observe el último tramo de la curva: ¿sigue subiendo?"),
                        "exp": t(f"The curve has leveled off; if the trend continues, the rate stays near {top}.", f"La curva ya se aplanó; si la tendencia continúa, la tasa se mantiene cerca de {top}.")})
        else:
            ops = [otro, t(f"The plant no longer needs {fac}.", f"La planta ya no necesita {fac}."), t("The plant has died.", "La planta ha muerto."), t("The measurements are wrong.", "Las mediciones están mal.")]
            out.append({"enun": g + "<p><strong>" + t("Why does the curve stop rising on the right?", "¿Por qué la curva deja de subir a la derecha?") + "</strong></p>", "ops": ops, "ok": 0,
                        "pista": t("Think about the limiting factor.", "Piense en el factor limitante."),
                        "exp": t(f"Past saturation, {fac} is no longer the limiting factor. ", f"Pasada la saturación, {fac} ya no es el factor limitante. ") + otro})
    return out


def banco_dia_noche():
    d = [
        (t("A potted plant is in bright sunlight. Overall, which gas does it give off?", "Una planta en maceta está a pleno sol. En conjunto, ¿qué gas libera?"),
         [t("Oxygen", "Oxígeno"), t("Carbon dioxide", "Dióxido de carbono"), t("Neither", "Ninguno")], 0,
         t("In bright light, photosynthesis is faster than respiration, so overall the plant gives off oxygen.", "Con mucha luz, la fotosíntesis supera a la respiración, así que en conjunto la planta libera oxígeno.")),
        (t("The same plant is in a dark closet. Which gas does it give off?", "La misma planta está en un armario oscuro. ¿Qué gas libera?"),
         [t("Oxygen", "Oxígeno"), t("Carbon dioxide", "Dióxido de carbono"), t("Neither", "Ninguno")], 1,
         t("In the dark there is only respiration: it uses O₂ and gives off CO₂.", "A oscuras solo hay respiración: consume O₂ y libera CO₂.")),
        (t("A goldfish is in a bowl, day or night. Which gas does it give off into the water?", "Un pez está en una pecera, de día o de noche. ¿Qué gas libera al agua?"),
         [t("Oxygen", "Oxígeno"), t("Carbon dioxide", "Dióxido de carbono"), t("Both, depending on the light", "Los dos, según la luz")], 1,
         t("Animals only respire: they always give off CO₂.", "Los animales solo respiran: siempre liberan CO₂.")),
        (t("A sealed jar holds a plant and a snail, in the light. Why can both stay alive for a long time?", "Un frasco cerrado contiene una planta y un caracol, a la luz. ¿Por qué pueden vivir los dos mucho tiempo?"),
         [t("The plant’s photosynthesis gives the snail oxygen and uses its CO₂.", "La fotosíntesis de la planta le da oxígeno al caracol y usa su CO₂."), t("The snail gives the plant oxygen.", "El caracol le da oxígeno a la planta."), t("Neither one needs gases.", "Ninguno necesita gases.")], 0,
         t("What one makes, the other uses.", "Lo que uno produce, el otro lo consume.")),
        (t("The same sealed jar (plant and snail) is kept in the dark. What happens?", "El mismo frasco cerrado (planta y caracol) se mantiene a oscuras. ¿Qué ocurre?"),
         [t("Oxygen runs out, because both only respire.", "El oxígeno se agota, porque los dos solo respiran."), t("Oxygen builds up.", "El oxígeno se acumula."), t("Nothing changes.", "No cambia nada.")], 0,
         t("With no light, no photosynthesis: plant and snail both use O₂ and give off CO₂.", "Sin luz no hay fotosíntesis: planta y caracol consumen O₂ y liberan CO₂.")),
        (t("Water with a plant turns yellow when CO₂ builds up and blue when CO₂ goes down. In the light, the water turns blue. Why?", "Un agua con una planta se vuelve amarilla cuando aumenta el CO₂ y azul cuando disminuye. A la luz, el agua se vuelve azul. ¿Por qué?"),
         [t("The plant is using more CO₂ in photosynthesis than it gives off in respiration.", "La planta consume más CO₂ en la fotosíntesis del que libera en la respiración."), t("The plant stopped respiring.", "La planta dejó de respirar."), t("Light destroys CO₂.", "La luz destruye el CO₂.")], 0,
         t("The plant still respires, but in the light photosynthesis uses more CO₂ than respiration gives off.", "La planta sigue respirando, pero a la luz la fotosíntesis consume más CO₂ del que libera la respiración.")),
        (t("Same water and plant, now kept in the dark. What color will the water turn?", "La misma agua con la planta, ahora a oscuras. ¿De qué color se volverá?"),
         [t("Yellow, because CO₂ builds up", "Amarilla, porque aumenta el CO₂"), t("Blue, because CO₂ goes down", "Azul, porque disminuye el CO₂"), t("It stays the same", "No cambia")], 0,
         t("In the dark only respiration: CO₂ builds up.", "A oscuras solo hay respiración: el CO₂ aumenta.")),
        (t("Why do people say a forest is “the lungs of the planet”?", "¿Por qué se dice que un bosque es «el pulmón del planeta»?"),
         [t("Because overall it takes in CO₂ and gives off oxygen", "Porque en conjunto absorbe CO₂ y libera oxígeno"), t("Because trees do not respire", "Porque los árboles no respiran"), t("Because it breathes like a person", "Porque respira como una persona")], 0,
         t("Trees respire too, but during the day their photosynthesis takes in more CO₂ than they give off. (Real lungs do the opposite: they take in oxygen.)", "Los árboles también respiran, pero de día su fotosíntesis absorbe más CO₂ del que liberan. (Los pulmones de verdad hacen lo contrario: toman oxígeno.)")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Light → photosynthesis and respiration. Dark → only respiration. Animals → only respiration.", "Luz → fotosíntesis y respiración. Oscuridad → solo respiración. Animales → solo respiración."), "exp": e} for q, o, k, e in d]


def practica():
    A = {"en": ["equations", "atoms", "which-process", "carbon", "limiting", "day-night"], "es": ["ecuaciones", "atomos", "que-proceso", "carbono", "limitante", "dia-noche"]}[C.L]
    pista_atomos = t("Multiply the small number by the large number in front of the formula, and add.", "Multiplique el número pequeño por el número grande de delante de la fórmula, y sume.")
    mods = [
        (A[0], t("Complete the equations", "Complete las ecuaciones"), C.huecos("m1", t("Choose the missing pieces of each sentence.", "Elija las piezas que faltan en cada oración."))),
        (A[1], t("Count the atoms", "Cuente los átomos"),
         "      <p>" + t("The small number after a letter counts atoms; the large number in front counts molecules.", "El número pequeño después de una letra cuenta átomos; el número grande de delante cuenta moléculas.") + "</p>\n"
         + f'''      <div class="practica" id="m2">
        <div class="enun" id="m2-enun"></div>
        <div class="campos"><div class="campo"><label for="m2-r">{t("Answer", "Respuesta")}</label><input type="text" inputmode="numeric" autocomplete="off" class="ancho" id="m2-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="m2-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="m2-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="m2-fb" role="status"></div>
        <p class="marcador" id="m2-marcador"></p>
      </div>'''),
        (A[2], t("Photosynthesis, respiration, or both?", "¿Fotosíntesis, respiración o las dos?"), C.clasifica("m3", t("Choose the process for each statement.", "Elija el proceso de cada afirmación."))),
        (A[3], t("Follow the carbon", "Siga al carbono"), C.orden("m4", t("Two trips: through a food chain and the long way.", "Dos viajes: por una cadena alimentaria y por el camino largo."))),
        (A[4], t("Rate graphs and limiting factors", "Gráficas de tasa y factor limitante"), C.om("m5", t("Eighteen curves: read, find the saturation point, and predict.", "Dieciocho curvas: lea, localice la saturación y prediga."))),
        (A[5], t("Gases by day and by night", "Los gases de día y de noche"), C.om("m6", t("Which gas goes in, which goes out, and why?", "¿Qué gas entra, cuál sale y por qué?"))),
    ]
    js = (C.js_datos("HUE", huecos_ecuaciones()) + C.js_datos("ATO", atomos()) + C.js_datos("PRO", clasif_procesos()) + C.js_datos("CAR", ordenes_carbono()) +
          C.js_datos("LIM", banco_limitante()) + C.js_datos("DIA", banco_dia_noche()) +
          f"var sacaA = mazo(ATO);\nfunction gA(){{ var q = sacaA(); return {{enun: q.enun, solucion: q.exp, evalua: numN(q.r, [], {C.json.dumps(pista_atomos, ensure_ascii=False)})}}; }}\n" +
          'creaHuecos("m1", HUE);\ncreaPracticaLibre("m2", gA);\ncreaClasifica("m3", PRO);\ncreaOrden("m4", CAR);\ncreaBanco("m5", LIM);\ncreaBanco("m6", DIA);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
