"""LearnGED · Ciencias · Lección 6.2 · Trabajo, energía y conservación (EN/ES).
Fuente: clases_ciencias/leccion_6-2.html (diagramas en tools/svg/6-2_*.svg) y los interactivos fisica/trabajo_potencia_energia, fisica/mont_rusa y fisica/pendulo.
Uso: python3 tools/build_sci_6_2.py
"""
import os, sys, random
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "6-2"


def titulo():
    return t("Work, energy, and conservation", "Trabajo, energía y conservación")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


def fmt(x):
    s = format(D(x).normalize(), "f")
    return s


def miles(x):
    """Separador de miles con coma en ambos idiomas."""
    s = fmt(x)
    ent, _, dec = s.partition(".")
    ent = f"{int(ent):,}"
    return ent + ("." + dec if dec else "")


def svg_trabajo():
    tr = {"Sí hay trabajo": "Work is done", "F = 50 N": "F = 50 N", "d = 3 m": "d = 3 m", "W = 50 × 3 = 150 J": "W = 50 × 3 = 150 J",
          "No hay trabajo": "No work is done", "F hacia arriba": "F upward", "d = 0 · la maleta no se mueve": "d = 0 · the suitcase does not move", "W = 50 × 0 = 0 J": "W = 50 × 0 = 0 J"}
    return C.svg_orig("6-2_0", tr, "Two situations compared to decide whether mechanical work is done. In the first, a person pushes a box with a force of fifty newtons and the box moves three meters in the direction of the force: work is done, and it equals one hundred fifty joules. In the second, a person holds a heavy suitcase without moving: there is an upward force, but no movement, so the mechanical work is zero, even though the person gets tired.")


def svg_montana():
    tr = {k: k for k in "ABCDE"}
    tr.update({"E queda por debajo de A:": "E is lower than A:", "la fricción transformó esa energía en calor": "friction turned that energy into heat",
               "A: Ep máxima, Ec casi nula": "A: PE highest, KE almost zero", "C: Ec máxima, Ep mínima, mayor velocidad": "C: KE highest, PE lowest, top speed", "E: Ep alta otra vez": "E: PE high again"})
    return C.svg_orig("6-2_1", tr, "Profile of a roller coaster with five labeled points. Point A is at the very top, where the car is almost stopped: potential energy is highest and kinetic energy almost zero. Point B is halfway down: potential energy has gone down and kinetic energy has gone up. Point C is at the bottom, the lowest point: potential energy is lowest, kinetic energy is highest, and the speed is the greatest of the whole ride. Point D is on the next climb, halfway up: kinetic energy turns back into potential energy. Point E is the top of the second hill, lower than the first, because friction has turned part of the mechanical energy into heat. The sum of kinetic and potential energy stays the same if nothing is lost to friction.")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("In physics, <strong>work</strong> does not mean effort. It means something very specific: a force that manages to <strong>move</strong> an object in the direction of that force. If nothing moves, no work is done, no matter how much you sweat.", "En física, <strong>trabajo</strong> no significa esfuerzo. Significa algo muy concreto: una fuerza que consigue <strong>desplazar</strong> un objeto en la dirección de esa fuerza. Si no hay desplazamiento, no hay trabajo, por mucho que se sude.")}</p>
{C.caja("tip", t("The formula", "La fórmula"), "<p>" + t("<strong>W = F × d</strong>, where F is the force in newtons and d the distance moved in meters. The result is in <strong>joules (J)</strong>. One joule is the work of a one-newton force over one meter: <strong>1 J = 1 N · m</strong>.", "<strong>W = F × d</strong>, donde F es la fuerza en newtons y d la distancia recorrida en metros. El resultado se expresa en <strong>julios (J)</strong>. Un julio es el trabajo de una fuerza de un newton a lo largo de un metro: <strong>1 J = 1 N · m</strong>.") + "</p>")}
{svg_trabajo()}
{C.ejemplo(t("Example 1 · Work", "Ejemplo 1 · Trabajo"),
 [("", t("A person pushes a cart with a force of 25 N for 4 meters. How much work is done?", "Una persona empuja un carrito con una fuerza de 25 N a lo largo de 4 metros. ¿Qué trabajo realiza?")),
  ("1", t("<strong>What is missing.</strong> Force and distance are given; work is asked: W = F × d.", "<strong>Qué falta.</strong> Se dan fuerza y distancia y se pide trabajo: W = F × d.")),
  ("2", t("<strong>Substitute and calculate.</strong> W = 25 N × 4 m = <strong>100 J</strong>.", "<strong>Sustitución y cálculo.</strong> W = 25 N × 4 m = <strong>100 J</strong>.")),
  ("3", t("<strong>Unit.</strong> Newtons times meters are joules, by definition. An answer in newtons or in meters would be wrong.", "<strong>Unidad.</strong> Newtons por metros son julios, por definición. Un resultado en newtons o en metros sería incorrecto."))])}
{C.caja("ojo", t("Zero work does not mean zero effort", "Trabajo cero no significa esfuerzo cero"), "<p>" + t("Holding a heavy suitcase for ten minutes without moving is very tiring, and yet the mechanical work is zero, because the distance moved in the direction of the force is zero. The same happens when you push a wall that does not budge. The test asks about this often, and the right answer usually seems to go against common sense.", "Sostener una maleta pesada durante diez minutos sin moverse cansa muchísimo y, sin embargo, el trabajo mecánico es cero, porque la distancia recorrida en la dirección de la fuerza es cero. Lo mismo ocurre al empujar una pared que no cede. El examen plantea esta situación con frecuencia, y la respuesta correcta suele parecer contraria al sentido común.") + "</p>")}
{P(t("Try it 1 · Holding a box", "Pruebe 1 · Sostener una caja"), t("A person holds a heavy box without moving for two minutes. The mechanical work done is…", "Una persona sostiene una caja pesada sin moverse durante dos minutos. El trabajo mecánico que realiza es…"),
   [t("very large, because the box is heavy", "muy grande, porque la caja pesa mucho"), t("equal to the weight of the box", "igual al peso de la caja"), t("zero, because nothing moves", "cero, porque no hay desplazamiento")], 2,
   {0: t("Heavy is not the same as work.", "Pesado no es lo mismo que trabajo."), 1: t("Weight is a force, not work.", "El peso es una fuerza, no un trabajo.")}, t("d = 0, so W = F × 0 = 0 J.", "d = 0, así que W = F × 0 = 0 J."))}
{C.enlace(N, anc("work", "trabajo"), t("work problems", "problemas de trabajo"), t("New problems every time, some with zero work.", "Problemas nuevos cada vez, algunos con trabajo cero."))}"""

    s2 = f"""<p>{t("Two people lift the same box to the same height, one in five seconds and the other in twenty. They did the same work, because force and distance are the same. What sets them apart is how fast they did it, and that is <strong>power</strong>.", "Dos personas suben la misma caja a la misma altura, una en cinco segundos y la otra en veinte. Han realizado el mismo trabajo, porque la fuerza y la distancia son idénticas. Lo que las distingue es la rapidez con que lo hicieron, y eso es la <strong>potencia</strong>.")}</p>
{C.caja("tip", t("The formula", "La fórmula"), "<p>" + t("<strong>P = W ÷ t</strong>, where W is the work in joules and t the time in seconds. The result is in <strong>watts (W)</strong>: one watt is one joule per second.", "<strong>P = W ÷ t</strong>, donde W es el trabajo en julios y t el tiempo en segundos. El resultado se expresa en <strong>vatios (W)</strong>: un vatio es un julio por segundo.") + "</p>")}
{C.caja("ojo", t("Two meanings of W", "Una colisión de símbolos que conviene tener clara"), "<p>" + t("The letter W is used for two different things: as a quantity it means <strong>work</strong>, and as a unit it means <strong>watt</strong>. Tell them apart by where they are: before the equals sign or inside a formula, it is work; next to a number as the unit of the result, it is watts. A 12 W light bulb uses twelve joules every second.", "La letra W se usa para dos cosas distintas: como magnitud significa <strong>trabajo</strong> (del inglés <em>work</em>) y como unidad significa <strong>vatio</strong>. Se distinguen por el sitio: si aparece antes del signo igual o dentro de una fórmula, es trabajo; si acompaña a un número como unidad del resultado, es vatio. Una bombilla de 12 W consume doce julios cada segundo.") + "</p>")}
{C.ejemplo(t("Example 2 · Power", "Ejemplo 2 · Potencia"),
 [("", t("A motor does 600 J of work in 30 seconds. What is its power?", "Un motor realiza un trabajo de 600 J en 30 segundos. ¿Cuál es su potencia?")),
  ("1", t("<strong>What is missing.</strong> Work and time are given; power is asked: P = W ÷ t.", "<strong>Qué falta.</strong> Se dan trabajo y tiempo y se pide potencia: P = W ÷ t.")),
  ("2", t("<strong>Substitute and calculate.</strong> P = 600 J ÷ 30 s = <strong>20 W</strong>.", "<strong>Sustitución y cálculo.</strong> P = 600 J ÷ 30 s = <strong>20 W</strong>.")),
  ("3", t("<strong>Meaning.</strong> The motor delivers twenty joules every second. If it did the same work in half the time, its power would double, even though the work would not change.", "<strong>Interpretación.</strong> El motor entrega veinte julios cada segundo. Si hiciera el mismo trabajo en la mitad de tiempo, su potencia sería el doble, aunque el trabajo no habría cambiado."))])}
{P(t("Try it 2 · Two workers", "Pruebe 2 · Dos obreros"), t("Two workers lift identical loads to the same height, one in 10 s and the other in 40 s. You can say that…", "Dos obreros suben cargas idénticas a la misma altura, uno en 10 s y otro en 40 s. Se puede afirmar que…"),
   [t("they did the same work, but the first one had more power", "realizaron el mismo trabajo, pero el primero desarrolló más potencia"), t("the first one did more work", "el primero realizó más trabajo"), t("the second one had more power", "el segundo desarrolló más potencia")], 0,
   {1: t("Same force, same height: same work.", "Misma fuerza, misma altura: mismo trabajo."), 2: t("Taking longer means less power.", "Tardar más significa menos potencia.")}, t("Same work, less time → more power.", "Mismo trabajo, menos tiempo → más potencia."))}
{C.enlace(N, anc("power", "potencia"), t("power problems", "problemas de potencia"), t("Find the power, the work, or the time.", "Halle la potencia, el trabajo o el tiempo."))}"""

    s3 = f"""<p>{t("<strong>Energy</strong> is the ability to do work, and it is measured in the same unit: joules. This lesson focuses on two forms and their sum.", "La <strong>energía</strong> es la capacidad de realizar trabajo, y se mide en las mismas unidades: julios. En esta lección interesan dos formas y su suma.")}</p>
{C.tabla(t("The three energy quantities in this lesson, with their formula, what each depends on, and an example", "Las tres magnitudes energéticas de la lección con su fórmula, de qué depende cada una y un ejemplo"),
 [t("Type", "Tipo"), t("Formula", "Fórmula"), t("Depends on", "De qué depende"), t("Example", "Ejemplo")],
 [[t("Kinetic energy (KE)", "Energía cinética (Ec)"), t("KE = ½ · m · v²", "Ec = ½ · m · v²"), t("Mass and, above all, speed, which is squared", "La masa y, sobre todo, la velocidad, que va elevada al cuadrado"), t("A moving car", "Un automóvil en marcha")],
  [t("Gravitational potential energy (PE)", "Energía potencial gravitatoria (Ep)"), t("PE = m · g · h", "Ep = m · g · h"), t("Mass and height above a reference level", "La masa y la altura respecto a un nivel de referencia"), t("A car stopped at the top of a roller coaster", "Un vagón detenido en lo alto de una montaña rusa")],
  [t("Mechanical energy", "Energía mecánica"), t("ME = KE + PE", "Em = Ec + Ep"), t("The sum of the two above", "La suma de las dos anteriores"), t("The system’s total at any point of the ride", "El total del sistema en cualquier punto del recorrido")]])}
<p>{t("In the potential energy formula, <strong>g</strong> is the acceleration due to gravity, which on Earth is <strong>9.8 m/s²</strong>. It is on the GED formula sheet, so you do not have to memorize it; some problems round it to 10 to keep things simple, and when they do, the question says so.", "En la fórmula de la energía potencial, <strong>g</strong> es la aceleración de la gravedad, cuyo valor en la Tierra es de <strong>9.8 m/s²</strong>. Aparece en la hoja de fórmulas del GED, de modo que no hay que recordarlo; algunos problemas lo redondean a 10 para simplificar, y en ese caso el enunciado lo indica.")}</p>
{C.ejemplo(t("Example 3 · Potential energy", "Ejemplo 3 · Energía potencial"),
 [("", t("A 50 kg car sits at the top of a slope, 10 meters high (about 33 feet). What is its potential energy?", "Un vagón de 50 kg se encuentra en lo alto de una pendiente, a 10 metros de altura. ¿Cuál es su energía potencial?")),
  ("1", t("<strong>Formula.</strong> PE = m · g · h.", "<strong>Fórmula.</strong> Ep = m · g · h.")),
  ("2", t("<strong>Substitute.</strong> PE = 50 kg × 9.8 m/s² × 10 m.", "<strong>Sustitución.</strong> Ep = 50 kg × 9.8 m/s² × 10 m.")),
  ("3", t("<strong>Calculate.</strong> PE = <strong>4,900 J</strong>.", "<strong>Cálculo.</strong> Ep = <strong>4,900 J</strong>."))])}
{C.ejemplo(t("Example 4 · Kinetic energy and the effect of the square", "Ejemplo 4 · Energía cinética y el efecto del cuadrado"),
 [("", t("A 2 kg object moves at 6 m/s. Find its kinetic energy. Then do it again for 12 m/s.", "Un cuerpo de 2 kg se mueve a 6 m/s. Calcule su energía cinética. Después repita el cálculo para 12 m/s.")),
  ("1", t("<strong>First case.</strong> KE = ½ × 2 kg × (6 m/s)² = ½ × 2 × 36 = <strong>36 J</strong>.", "<strong>Primer caso.</strong> Ec = ½ × 2 kg × (6 m/s)² = ½ × 2 × 36 = <strong>36 J</strong>.")),
  ("2", t("<strong>Second case.</strong> KE = ½ × 2 kg × (12 m/s)² = ½ × 2 × 144 = <strong>144 J</strong>.", "<strong>Segundo caso.</strong> Ec = ½ × 2 kg × (12 m/s)² = ½ × 2 × 144 = <strong>144 J</strong>.")),
  ("3", t("<strong>What to notice.</strong> The speed doubled, but the energy was multiplied by four. That comes straight from the speed being squared.", "<strong>Lo que hay que observar.</strong> La velocidad se ha duplicado, pero la energía se ha multiplicado por cuatro. Es la consecuencia directa de que la velocidad vaya elevada al cuadrado."))])}
{C.caja("ojo", t("That four explains the reading in Lesson 6.1", "Ese cuatro explica la lectura de la Lección 6.1"), "<p>" + t("Braking distance does not grow in step with speed, but much faster: a car going twice as fast carries four times as much kinetic energy, and the friction of the brakes has to take all of it away. That is why road safety campaigns focus on speed and not only on reaction time. It is also the most common gut mistake with this formula on the test: thinking that doubling the speed doubles the energy.", "La distancia de frenado no crece en proporción a la velocidad, sino mucho más deprisa: un automóvil que circula al doble de velocidad lleva cuatro veces más energía cinética, y toda esa energía tiene que ser retirada por la fricción de los frenos. Por eso las campañas de seguridad vial insisten en la velocidad y no solo en el tiempo de reacción. Es también el error de intuición más frecuente del examen en esta fórmula: suponer que al doblar la velocidad se dobla la energía.") + "</p>")}
{P(t("Try it 3 · Double the speed", "Pruebe 3 · Doble velocidad"), t("If an object’s speed doubles, its kinetic energy…", "Si la velocidad de un cuerpo se duplica, su energía cinética…"),
   [t("doubles", "se duplica"), t("is multiplied by four", "se multiplica por cuatro"), t("does not change", "no cambia")], 1,
   {0: t("Speed is squared.", "La velocidad va al cuadrado."), 2: t("KE depends on speed.", "La Ec depende de la velocidad.")}, t("2² = 4.", "2² = 4."))}
{C.enlace(N, anc("energy", "energia"), t("kinetic and potential energy problems", "problemas de energía cinética y potencial"), t("Use KE = ½ m v² and PE = m g h with new numbers every time.", "Use Ec = ½ m v² y Ep = m g h con números nuevos cada vez."))}"""

    s4 = f"""<p>{t("The principle is short and very powerful: <strong>energy is neither created nor destroyed; it only changes from one form to another</strong>. It is the same idea that ran Topic 5 with matter, now applied to energy.", "El principio es breve y muy poderoso: <strong>la energía no se crea ni se destruye, solo se transforma de una forma en otra</strong>. Es la misma idea que gobernaba el Tema 5 con la materia, aplicada ahora a la energía.")}</p>
<p>{t("On a ride like a roller coaster, that means the potential energy the car had at the top does not vanish on the way down: it becomes kinetic energy. And on the way up again, the kinetic energy turns back into potential energy. The sum of both, the mechanical energy, stays the same if nothing is lost.", "En un recorrido como el de una montaña rusa, eso significa que la energía potencial que el vagón tenía arriba no desaparece al bajar: se convierte en energía cinética. Y al subir de nuevo, la cinética vuelve a convertirse en potencial. La suma de ambas, la energía mecánica, se mantiene constante si no hay pérdidas.")}</p>
{svg_montana()}
{C.tabla(t("Potential energy, kinetic energy, and speed at each of the five points of the roller coaster", "Energía potencial, energía cinética y velocidad en cada uno de los cinco puntos del recorrido de la montaña rusa"),
 [t("Point", "Punto"), t("Potential energy", "Energía potencial"), t("Kinetic energy", "Energía cinética"), t("Speed", "Velocidad")],
 [[t("A · first top", "A · cima inicial"), t("Highest", "Máxima"), t("Almost zero", "Casi nula"), t("Almost zero", "Casi nula")],
  [t("B · halfway down", "B · media bajada"), t("Has gone down", "Ha disminuido"), t("Has gone up", "Ha aumentado"), t("Medium", "Media")],
  [t("C · lowest point", "C · punto más bajo"), t("Lowest", "Mínima"), t("Highest", "Máxima"), t("The greatest of the ride", "La mayor del recorrido")],
  [t("D · halfway up", "D · media subida"), t("Goes up again", "Vuelve a aumentar"), t("Goes down again", "Vuelve a disminuir"), t("Medium", "Media")],
  [t("E · second top", "E · segunda cima"), t("High, but less than at A", "Alta, pero menor que en A"), t("Low", "Baja"), t("Low", "Baja")]])}
<p>{t("You can fill in that table without a single calculation, and that is the skill the test rewards. One reading rule is enough: <strong>where the track is higher, potential energy is greater; where it is lower, kinetic energy and speed are greater</strong>.", "Esa tabla se puede completar sin hacer un solo cálculo, y ahí está la destreza que el examen premia. Basta con una regla de lectura: <strong>donde el recorrido está más alto, la potencial es mayor; donde está más bajo, la cinética y la velocidad son mayores</strong>.")}</p>
<h3>{t("Why the second hill is always lower", "Por qué la segunda colina siempre es más baja")}</h3>
<p>{t("If energy is conserved, you might expect the car to climb back to exactly its starting height. It never does, and the reason ties straight back to the last lesson: friction with the rails and the air turns part of the mechanical energy into heat. That energy has not disappeared (the conservation principle still holds), but it is no longer available to move the car.", "Si la energía se conserva, cabría esperar que el vagón volviera a subir exactamente a la altura de partida. No lo hace nunca, y el motivo enlaza directamente con la lección anterior: la fricción con los raíles y con el aire transforma parte de la energía mecánica en calor. Esa energía no ha desaparecido (el principio de conservación sigue cumpliéndose), pero ya no está disponible para mover el vagón.")}</p>
<p>{t("That is why no roller coaster has a second top as high as the first, and why a pendulum left alone swings less and less until it stops. In both cases the energy still exists: it is spread out as heat in the air, the rails, and the object itself.", "Por eso ninguna montaña rusa tiene una segunda cima tan alta como la primera, y por eso un péndulo abandonado a su suerte va reduciendo su oscilación hasta detenerse. En ambos casos la energía sigue existiendo: está repartida como calor entre el aire, los raíles y el propio cuerpo.")}</p>
{C.caja("ojo", t("The exact wording matters on the test", "La formulación exacta importa en el examen"), "<p>" + t("Saying that “energy is lost” is imprecise and is usually the wrong option. What happens is that energy <strong>turns into heat</strong> and can no longer be used for motion. The right answer almost always mentions the change of form, not disappearance.", "Decir que «se pierde energía» es impreciso y suele ser la opción incorrecta del ítem. Lo que ocurre es que la energía <strong>se transforma en calor</strong> y deja de ser aprovechable para el movimiento. La respuesta correcta casi siempre menciona la transformación, no la desaparición.") + "</p>")}
<h3>{t("Energy changes in everyday devices", "Transformaciones de energía en aparatos cotidianos")}</h3>
{C.tabla(t("Everyday devices with the energy that goes in, the useful energy that comes out, and the energy that turns into heat", "Aparatos cotidianos con la energía que entra, la energía útil que sale y la que se transforma en calor"),
 [t("Device", "Aparato"), t("Energy in", "Energía que entra"), t("Useful energy out", "Energía útil que sale"), t("Also produces", "También produce")],
 [[t("Light bulb", "Bombilla"), t("Electrical", "Eléctrica"), t("Light", "Luminosa"), t("Heat (a lot in incandescent bulbs, little in LEDs)", "Calor (mucho en las incandescentes, poco en las LED)")],
  [t("Electric fan", "Ventilador"), t("Electrical", "Eléctrica"), t("Kinetic (moving blades)", "Cinética (aspas en movimiento)"), t("Heat and sound", "Calor y sonido")],
  [t("Car engine", "Motor de automóvil"), t("Chemical (fuel)", "Química (combustible)"), t("Kinetic", "Cinética"), t("A lot of heat", "Mucho calor")],
  [t("Battery-powered flashlight", "Linterna de pilas"), t("Chemical (battery)", "Química (pila)"), t("Light", "Luminosa"), t("Heat", "Calor")],
  [t("Solar panel", "Panel solar"), t("Light", "Luminosa"), t("Electrical", "Eléctrica"), t("Heat", "Calor")],
  [t("Hydroelectric dam", "Presa hidroeléctrica"), t("Potential (water held high)", "Potencial (agua en altura)"), t("Electrical", "Eléctrica"), t("Heat and sound", "Calor y sonido")]])}
{P(t("Try it 4 · Fastest point", "Pruebe 4 · El punto más rápido"), t("On the roller coaster, the car is fastest at…", "En el recorrido de la montaña rusa, la velocidad del vagón es mayor en…"),
   [t("point A, the first top", "el punto A, la cima inicial"), t("point C, the lowest point", "el punto C, el más bajo del recorrido"), t("point E, the second top", "el punto E, la segunda cima")], 1,
   {0: t("At the top the car is almost stopped.", "Arriba el vagón casi está detenido."), 2: t("E is high: little kinetic energy.", "E está alto: poca energía cinética.")}, t("Lowest point → most kinetic energy → most speed.", "Punto más bajo → más energía cinética → más velocidad."))}
{P(t("Try it 5 · The second top", "Pruebe 5 · La segunda cima"), t("The second top never reaches the height of the first because…", "La segunda cima nunca alcanza la altura de la primera porque…"),
   [t("gravity gets weaker during the ride", "la gravedad disminuye durante el recorrido"), t("part of the energy is destroyed", "parte de la energía se destruye"), t("friction turns part of the mechanical energy into heat", "la fricción transforma parte de la energía mecánica en calor")], 2,
   {0: t("Gravity does not change.", "La gravedad no cambia."), 1: t("Energy is never destroyed.", "La energía nunca se destruye.")}, t("Transformation, not disappearance.", "Transformación, no desaparición."))}
{C.enlace(N, anc("roller-coaster", "montana-rusa"), t("predict on the roller coaster", "prediga en la montaña rusa"), t("Where is each energy highest? Answer without calculating.", "¿Dónde es máxima cada energía? Responda sin calcular."))}
{C.enlace(N, anc("changes", "transformaciones"), t("energy changes", "transformaciones de energía"), t("What goes in, what comes out, and where the heat comes from.", "Qué entra, qué sale y de dónde sale el calor."))}
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>Energy</strong> comes from the Greek <em>enérgeia</em>, made of {R('en-')}, in, and {R('ergon')}, work: literally, the ability to do work that is inside. The same root {R('erg')} is in <em>ergonomics</em>. <strong>Kinetic</strong> comes from {R('kinesis')}, motion, the root of <em>cinema</em>, which first meant moving pictures. <strong>Potential</strong> comes from the Latin <em>potentia</em>, power or ability: it is the energy that is not acting yet but could, because of where the object is. <strong>Power</strong>, on the other hand, measures speed of work, not ability, so do not mix them up despite how alike they sound. <strong>Joule</strong> and <strong>watt</strong> are named after James Joule and James Watt: the unit name is written in lowercase and its symbol in uppercase, J and W, just like the newton in Lesson 6.1.", f"<strong>Energía</strong> procede del griego <em>enérgeia</em>, formada por {R('en-')}, dentro, y {R('érgon')}, obra o trabajo: literalmente, la capacidad de obrar que está dentro. La misma raíz {R('érgon')} aparece en <em>ergonomía</em>. <strong>Cinética</strong> viene de {R('kínesis')}, movimiento, la raíz de <em>cine</em>, que en su origen designaba imágenes en movimiento. <strong>Potencial</strong> procede del latín <em>potentia</em>, poder o capacidad: es la energía que todavía no actúa pero puede hacerlo, por la posición que ocupa el cuerpo. <strong>Potencia</strong>, en cambio, mide rapidez, no capacidad, y conviene no confundirlas pese al parecido. <strong>Julio</strong> y <strong>vatio</strong> son epónimos, de James Joule y James Watt: el nombre de la unidad se escribe en minúscula y su símbolo en mayúscula, J y W, igual que ocurría con el newton en la Lección 6.1.")}</p>"""

    s5 = f"""<p>{t("A short science text written for this level. Notice how much of the energy reaches its goal and what happens to the rest.", "Texto científico breve adaptado al nivel. Observe qué proporción de la energía llega a su destino y qué ocurre con el resto.")}</p>
{C.lectura(t("Where a car’s energy goes", "Adónde va la energía de un automóvil"),
 [t("When fuel burns in a car’s engine, it releases a certain amount of energy. Only part of it ends up moving the car; the rest turns into other forms that do not help it move.", "Cuando se quema combustible en el motor de un automóvil, se libera una cantidad determinada de energía. Solo una parte de ella acaba moviendo el vehículo; el resto se transforma en otras formas que no contribuyen al desplazamiento."),
  t("Several efficiency studies agree that, in a regular gasoline engine, about three quarters of the energy released is given off as heat, through the exhaust, the cooling system, and the rubbing of moving parts. Another share goes to running the car’s own accessories.", "Diversos análisis de eficiencia coinciden en que, en un motor de gasolina convencional, alrededor de las tres cuartas partes de la energía liberada se disipa en forma de calor, tanto por los gases de escape como por el sistema de refrigeración y por el rozamiento entre las piezas móviles. Una fracción adicional se emplea en mover los accesorios del propio vehículo."),
  t("Of the energy that does reach the wheels, part is used up pushing through the air, which gets much harder as speed goes up, and part in the rolling resistance of the tires. When braking, the kinetic energy the car has built up turns almost completely into heat in the brakes and goes off into the air.", "De la energía que sí llega a las ruedas, una parte se consume en vencer la resistencia del aire, que aumenta rápidamente con la velocidad, y otra en la resistencia de rodadura de los neumáticos. Al frenar, la energía cinética acumulada se transforma casi por completo en calor en los frenos y se disipa en el aire."),
  t("Some vehicles have regenerative braking, which recovers part of that energy and stores it in a battery instead of giving it off as heat. The studies reviewed point out that the savings depend a lot on the kind of trip, and that they are much larger on trips with frequent braking than on the open highway.", "Algunos vehículos incorporan sistemas de frenado regenerativo, que recuperan una fracción de esa energía y la almacenan en una batería en lugar de disiparla. Los estudios consultados señalan que el ahorro obtenido depende mucho del tipo de recorrido, y que en trayectos con frenadas frecuentes resulta considerablemente mayor que en carretera abierta.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Cars do not need energy to move.", "Los automóviles no necesitan energía para moverse."), t("The fuel’s energy is destroyed during the trip.", "La energía del combustible se destruye durante el trayecto."), t("Only part of the fuel’s energy moves the car; the rest turns mostly into heat.", "Solo una parte de la energía del combustible mueve el vehículo; el resto se transforma sobre todo en calor.")], 2,
   {0: t("The text says the opposite.", "El texto dice lo contrario."), 1: t("Energy is not destroyed; it changes form.", "La energía no se destruye; cambia de forma.")}, t("Part moves the car; most becomes heat.", "Una parte mueve el auto; la mayoría se vuelve calor."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("When braking, the car’s kinetic energy…", "Al frenar, la energía cinética del vehículo…"),
   [t("turns almost completely into heat in the brakes", "se transforma casi por completo en calor en los frenos"), t("disappears without a trace", "desaparece sin dejar rastro"), t("becomes extra mass", "se convierte en masa adicional")], 0,
   {1: t("Energy does not disappear.", "La energía no desaparece."), 2: t("Not in everyday physics.", "No en la física cotidiana.")}, t("Friction in the brakes → heat.", "Fricción en los frenos → calor."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("According to the text, regenerative braking pays off most…", "Según el texto, el frenado regenerativo resulta más provechoso…"),
   [t("on the open highway at steady speed", "en carretera abierta y a velocidad constante"), t("on trips with frequent braking", "en recorridos con frenadas frecuentes"), t("only in gasoline cars", "solo en vehículos de gasolina")], 1,
   {0: t("Little braking, little to recover.", "Poco frenado, poco que recuperar."), 2: t("The text does not say that.", "El texto no dice eso.")}, t("More braking, more energy to recover.", "Más frenadas, más energía que recuperar."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Does this text contradict the conservation of energy?", "¿Contradice este texto el principio de conservación de la energía?"),
   [t("Yes, because it describes energy being lost", "Sí, porque describe energía que se pierde"), t("Yes, because the engine creates new energy", "Sí, porque el motor crea energía nueva"), t("No: the energy does not disappear; it turns into heat and can no longer be used for motion", "No: la energía no desaparece, se transforma en calor y deja de ser aprovechable para el movimiento")], 2,
   {0: t("It changes form, it is not lost.", "Cambia de forma, no se pierde."), 1: t("The engine changes chemical energy; it does not create it.", "El motor transforma energía química; no la crea.")}, t("Conservation holds.", "La conservación se cumple."))}"""

    G = lambda *a: C.ged_item(P, *a)
    ec = {"tipo": "barras", "xEtq": t("Point on the ride", "Punto del recorrido"), "yEtq": t("Kinetic energy (kJ)", "Energía cinética (kJ)"), "py": 5,
          "barras": [{"etq": "P", "valor": 2}, {"etq": "Q", "valor": 14}, {"etq": "R", "valor": 25}, {"etq": "S", "valor": 9}, {"etq": "T", "valor": 4}]}
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK). You may use the calculator and the formula sheet.", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora y la hoja de fórmulas.") + f"""</p>
{G(1, "SP.7.b", "2", t("<em>A mover pushes a 40 kg dresser across the floor with a force of 120 N for 5 meters, then holds it still for 30 seconds.</em><br>How much work does the mover do in total?", "<em>Un empleado de mudanzas empuja una cómoda de 40 kg por el suelo con una fuerza de 120 N a lo largo de 5 metros y después la sostiene quieta durante 30 segundos.</em><br>¿Cuánto trabajo realiza en total?"),
   ["600 J", "3,600 J", "200 J", "24 J"], 0,
   {1: t("Holding still adds no work: there is no distance.", "Sostenerla quieta no suma trabajo: no hay distancia."), 2: t("The mass is not part of W = F × d here.", "La masa no entra en W = F × d aquí."), 3: t("That divides instead of multiplying.", "Eso divide en lugar de multiplicar.")},
   t("W = 120 × 5 = 600 J; holding still adds 0 J.", "W = 120 × 5 = 600 J; sostenerla quieta suma 0 J."))}
{G(2, "SP.7.b", "2", t("<em>Motor X lifts a load using 1,800 J in 60 s. Motor Y does the same job in 20 s.</em><br>Which statement is correct?", "<em>El motor X sube una carga empleando 1,800 J en 60 s. El motor Y hace el mismo trabajo en 20 s.</em><br>¿Qué afirmación es correcta?"),
   [t("Motor Y has a power of 90 W, three times that of motor X.", "El motor Y tiene una potencia de 90 W, el triple que el motor X."), t("Both motors have the same power because the work is the same.", "Los dos motores tienen la misma potencia porque el trabajo es el mismo."), t("Motor X has more power because it works longer.", "El motor X tiene más potencia porque trabaja más tiempo."), t("Motor Y does three times as much work.", "El motor Y realiza el triple de trabajo.")], 0,
   {1: t("Power also depends on time.", "La potencia también depende del tiempo."), 2: t("Longer time means less power.", "Más tiempo significa menos potencia."), 3: t("Same job, same work.", "Mismo trabajo, mismos julios.")},
   t("X: 1,800 ÷ 60 = 30 W. Y: 1,800 ÷ 20 = 90 W.", "X: 1,800 ÷ 60 = 30 W. Y: 1,800 ÷ 20 = 90 W."))}
{G(3, "SP.6.c", "2", t("<em>A car’s speed goes from 15 m/s to 30 m/s.</em><br>How does its kinetic energy change?", "<em>La velocidad de un automóvil pasa de 15 m/s a 30 m/s.</em><br>¿Cómo cambia su energía cinética?"),
   [t("It becomes four times as large.", "Se hace cuatro veces mayor."), t("It becomes twice as large.", "Se hace el doble."), t("It stays the same.", "No cambia."), t("It increases by 15 J.", "Aumenta 15 J.")], 0,
   {1: t("Speed is squared in KE = ½ m v².", "La velocidad va al cuadrado en Ec = ½ m v²."), 2: t("KE depends on speed.", "La Ec depende de la velocidad."), 3: t("Speed and energy have different units.", "Velocidad y energía tienen unidades distintas.")},
   t("Double the speed → 2² = 4 times the energy.", "Doble velocidad → 2² = 4 veces la energía."))}
{G(4, "SP.1.c", "2", t("<em>Kinetic energy of a roller-coaster car at five points of a ride, with no friction:</em>", "<em>Energía cinética de un vagón de montaña rusa en cinco puntos de un recorrido, sin fricción:</em>") + C.grafica(ec, C.describe(ec), ancho=520, alto=290, y0=0) + t("At which point is the car <strong>highest</strong> above the ground?", "¿En qué punto está el vagón <strong>más alto</strong> sobre el suelo?"),
   ["P", "R", "Q", "S"], 0,
   {1: t("R has the most kinetic energy: it is the lowest point.", "R tiene la mayor energía cinética: es el punto más bajo."), 2: t("Q has a lot of kinetic energy.", "Q tiene mucha energía cinética."), 3: t("S has more kinetic energy than P.", "S tiene más energía cinética que P.")},
   t("Least kinetic energy → most potential energy → highest point.", "Menor energía cinética → mayor energía potencial → punto más alto."))}
{G(5, "SP.3.b", "2–3", t("<em>Read “Where a car’s energy goes” in section 5. A student writes: “Most of a gasoline car’s fuel energy is wasted, so the car breaks the law of conservation of energy.”</em><br>What is wrong with the student’s reasoning?", "<em>Lea «Adónde va la energía de un automóvil» de la sección 5. Un estudiante escribe: «La mayor parte de la energía del combustible se desperdicia, así que el automóvil no cumple la ley de conservación de la energía».</em><br>¿Qué falla en su razonamiento?"),
   [t("The “wasted” energy is not destroyed: it turns into heat, so the total is still conserved.", "La energía «desperdiciada» no se destruye: se transforma en calor, así que el total se conserva."), t("Nothing: the text shows energy disappearing.", "Nada: el texto muestra que la energía desaparece."), t("Gasoline cars do not lose any energy to heat.", "Los autos de gasolina no transforman energía en calor."), t("Conservation only applies to roller coasters.", "La conservación solo se aplica a las montañas rusas.")], 0,
   {1: t("The text describes transformation, not disappearance.", "El texto describe transformación, no desaparición."), 2: t("The text says about three quarters become heat.", "El texto dice que unas tres cuartas partes se vuelven calor."), 3: t("It applies everywhere.", "Se aplica en todas partes.")},
   t("Useful energy is lost to heat, but total energy is conserved.", "La energía útil se va en calor, pero la energía total se conserva."))}"""

    secciones = [
        ("s1", t("Mechanical work", "El trabajo mecánico"), s1),
        ("s2", t("Power: work and time", "La potencia: el trabajo y el tiempo"), s2),
        ("s3", t("The forms of mechanical energy", "Las formas de la energía mecánica"), s3),
        ("s4", t("Conservation of energy", "La conservación de la energía"), s4),
        ("s5", t("Science reading", "Lectura científica"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Ten problems.", "Diez problemas."), t("Do ten work, power, and energy problems, with the right unit in each answer.", "Resuelva diez problemas de trabajo, potencia y transformación de energía, con la unidad exigida en cada respuesta.")),
        (t("Four predictions.", "Cuatro predicciones."), t("Draw a ride with ups and downs, label four points, and say without calculating where speed and each energy are highest.", "Dibuje un recorrido con desniveles, rotule cuatro puntos y diga, sin calcular, dónde son mayores la velocidad y cada energía.")),
        (t("In your own words.", "Con sus palabras."), t("Write a short paragraph explaining why doubling a car’s speed multiplies its kinetic energy by four, and what that means when braking.", "Escriba un párrafo breve que explique por qué duplicar la velocidad de un vehículo multiplica por cuatro su energía cinética, y qué consecuencia tiene eso al frenar.")),
    ]
    Q = t
    quiz = [
        (Q("The energy an object has because it is moving is called…", "La energía que posee un cuerpo por el hecho de estar en movimiento se denomina…"), [Q("kinetic energy", "energía cinética"), Q("potential energy", "energía potencial"), Q("power", "potencia"), Q("work", "trabajo")], 0, {1: Q("That depends on height.", "Esa depende de la altura."), 2: Q("Power is a rate.", "La potencia es una rapidez."), 3: Q("Work is force times distance.", "El trabajo es fuerza por distancia.")}, Q("Kinesis = motion.", "Kínesis = movimiento.")),
        (Q("A car stopped at the top of a slope has mostly…", "Un vagón detenido en lo alto de una pendiente posee sobre todo…"), [Q("kinetic energy", "energía cinética"), Q("gravitational potential energy", "energía potencial gravitatoria"), Q("power", "potencia"), Q("no energy", "ninguna energía")], 1, {0: Q("It is stopped.", "Está detenido."), 2: Q("Power is not stored.", "La potencia no se almacena."), 3: Q("Height gives it energy.", "La altura le da energía.")}, Q("Height → potential energy.", "Altura → energía potencial.")),
        (Q("The mechanical energy of a system is…", "La energía mecánica de un sistema es…"), [Q("only the kinetic energy", "solo la energía cinética"), Q("only the potential energy", "solo la energía potencial"), Q("the sum of kinetic and potential energy", "la suma de la cinética y la potencial"), Q("energy divided by time", "la energía dividida entre el tiempo")], 2, {0: Q("Half of it.", "Es solo una parte."), 1: Q("Half of it.", "Es solo una parte."), 3: Q("That is power.", "Eso es potencia.")}, Q("ME = KE + PE.", "Em = Ec + Ep.")),
        (Q("The quantity that measures how fast work is done is…", "La magnitud que mide la rapidez con que se realiza un trabajo es…"), [Q("force", "la fuerza"), Q("kinetic energy", "la energía cinética"), Q("potential energy", "la energía potencial"), Q("power", "la potencia")], 3, {0: Q("Force is a push.", "La fuerza es un empuje."), 1: Q("That is energy of motion.", "Es energía del movimiento."), 2: Q("That is energy of position.", "Es energía de posición.")}, Q("P = W ÷ t.", "P = W ÷ t.")),
        (Q("At the lowest point of a roller coaster, the car has…", "En el punto más bajo de una montaña rusa, el vagón tiene…"), [Q("highest kinetic and lowest potential energy", "energía cinética máxima y potencial mínima"), Q("highest potential and lowest kinetic energy", "energía potencial máxima y cinética mínima"), Q("both energies at their highest", "ambas energías máximas"), Q("no energy at all", "ambas energías nulas")], 0, {1: Q("That is the top.", "Eso es la cima."), 2: Q("One goes up as the other goes down.", "Una sube cuando la otra baja."), 3: Q("It is moving fast.", "Se mueve rápido.")}, Q("Low → fast.", "Abajo → rápido.")),
        (Q("A pendulum left alone swings less and less because…", "Un péndulo abandonado a su suerte reduce poco a poco su oscilación porque…"), [Q("gravity gets weaker", "la gravedad disminuye"), Q("friction turns part of the mechanical energy into heat", "la fricción transforma parte de la energía mecánica en calor"), Q("energy is destroyed", "la energía se destruye"), Q("its mass goes down", "su masa disminuye")], 1, {0: Q("Gravity does not change.", "La gravedad no cambia."), 2: Q("Energy is never destroyed.", "La energía nunca se destruye."), 3: Q("Its mass stays the same.", "Su masa no cambia.")}, Q("Friction → heat.", "Fricción → calor.")),
        (Q("If an object’s speed doubles, its kinetic energy…", "Si la velocidad de un cuerpo se duplica, su energía cinética…"), [Q("does not change", "no cambia"), Q("doubles", "se duplica"), Q("is multiplied by four", "se multiplica por cuatro"), Q("is cut in half", "se reduce a la mitad")], 2, {0: Q("It depends on speed.", "Depende de la velocidad."), 1: Q("Speed is squared.", "La velocidad va al cuadrado."), 3: Q("More speed, more energy.", "Más velocidad, más energía.")}, Q("2² = 4.", "2² = 4.")),
        (Q("A car climbs the second hill and does not reach the height of the first. This means that…", "Un vagón sube por la segunda colina y no alcanza la altura de la primera. Eso significa que…"), [Q("conservation of energy does not hold", "el principio de conservación de la energía no se cumple"), Q("potential energy turned into mass", "la energía potencial se convirtió en masa"), Q("the car lost weight on the ride", "el vagón perdió peso durante el recorrido"), Q("friction turned part of the mechanical energy into heat", "parte de la energía mecánica se transformó en calor por la fricción")], 3, {0: Q("It always holds.", "Siempre se cumple."), 1: Q("Not in everyday physics.", "No en la física cotidiana."), 2: Q("Its weight is the same.", "Su peso es el mismo.")}, Q("Transformation into heat.", "Transformación en calor.")),
        (Q("A 20 N force moves an object 5 meters in the same direction. The work done is…", "Una fuerza de 20 N desplaza un objeto 5 metros en su misma dirección. El trabajo realizado es…"), ["100 J", "25 J", "4 J", "100 W"], 0, {1: Q("That is adding.", "Eso es sumar."), 2: Q("That is dividing.", "Eso es dividir."), 3: Q("Watts are for power.", "Los vatios son de potencia.")}, Q("20 × 5 = 100 J.", "20 × 5 = 100 J.")),
        (Q("A person holds a box still for one minute. The mechanical work done is…", "Una persona sostiene una caja inmóvil durante un minuto. El trabajo mecánico realizado es…"), ["60 J", Q("0 J, because nothing moves", "0 J, porque no hay desplazamiento"), Q("equal to the weight of the box", "igual al peso de la caja"), Q("impossible to know", "imposible de determinar")], 1, {0: Q("Time is not distance.", "El tiempo no es distancia."), 2: Q("Weight is a force.", "El peso es una fuerza."), 3: Q("d = 0 tells you.", "d = 0 lo dice.")}, Q("d = 0 → W = 0.", "d = 0 → W = 0.")),
        (Q("A motor does 900 J of work in 45 seconds. Its power is…", "Un motor realiza 900 J de trabajo en 45 segundos. Su potencia es…"), ["40,500 W", "945 W", "20 W", "0.05 W"], 2, {0: Q("That is multiplying.", "Eso es multiplicar."), 1: Q("That is adding.", "Eso es sumar."), 3: Q("Upside down.", "Al revés.")}, Q("900 ÷ 45 = 20 W.", "900 ÷ 45 = 20 W.")),
        (Q("A 4 kg object moves at 5 m/s. Its kinetic energy is…", "Un cuerpo de 4 kg se mueve a 5 m/s. Su energía cinética es…"), ["20 J", "100 J", "10 J", "50 J"], 3, {0: Q("Square the speed first.", "Eleve primero la velocidad al cuadrado."), 1: Q("Do not forget the ½.", "No olvide el ½."), 2: Q("Square the speed, not the mass.", "Eleve al cuadrado la velocidad.")}, Q("½ × 4 × 25 = 50 J.", "½ × 4 × 25 = 50 J.")),
    ]
    filas = [
        (t("Tell the energy types apart in a system", "Distingue los tipos de energía en un sistema"), t("I identify kinetic, potential, and mechanical energy at each point and explain that mechanical energy is their sum.", "Identifico cinética, potencial y mecánica en cada punto y explico que la mecánica es la suma."), t("I name kinetic and potential energy but place them wrong on the ride.", "Nombro la cinética y la potencial, pero las asigno mal en el recorrido."), t("I use “energy” as one single word.", "Empleo «energía» como término único.")),
        (t("Use conservation to predict without calculating", "Aplica la conservación para predecir sin calcular"), t("I predict where speed and each energy are highest, reasoning with height.", "Predigo dónde son máximas la velocidad y cada energía, razonando con la altura."), t("I predict some cases but do not use conservation to explain.", "Predigo algún caso, pero no justifico con la conservación."), t("I need to calculate to answer anything.", "Necesito calcular para responder cualquier pregunta.")),
        (t("Calculate with the right formula", "Calcula con la fórmula adecuada"), t("I use W = F · d, P = W ÷ t, KE = ½ m v², and PE = m g h with joules and watts.", "Aplico W = F · d, P = W ÷ t, Ec = ½ m v² y Ep = m g h con julios y vatios."), t("I choose the formula well but forget to square the speed.", "Elijo bien la fórmula, pero olvido elevar la velocidad al cuadrado."), t("I pick formulas at random.", "Elijo la fórmula al azar.")),
        (t("Explain the result in context", "Interpreta el resultado en su contexto"), t("I explain the result as energy changing form, with friction turning it into heat.", "Explico el resultado como transformación de energía, con la fricción convirtiéndola en calor."), t("I explain it but say the energy is lost.", "Lo interpreto, pero afirmo que la energía se pierde."), t("I give the number with no meaning.", "Entrego el número sin relacionarlo con la situación.")),
    ]
    cierre = "<p>" + t("This lesson ended with heat: that is where the energy friction takes from motion ends up, on the roller coaster, in the pendulum, and in a car’s brakes. Lesson 6.3 picks up that thread and studies heat in its own right: what sets it apart from temperature and how it travels.", "Esta lección ha terminado en el calor: es ahí donde va a parar la energía que la fricción retira del movimiento, tanto en la montaña rusa como en el péndulo y en los frenos de un automóvil. La Lección 6.3 recoge ese hilo y estudia el calor por derecho propio: qué lo distingue de la temperatura y por qué caminos se transmite.") + "</p><p>" + \
             t("The second half of that lesson opens something new, waves, with their properties and the electromagnetic spectrum. Scientific notation from Lesson 2.1 comes back there, because wavelengths are handled in powers of ten.", "La segunda mitad de esa lección abre un asunto nuevo, las ondas, con sus propiedades y el espectro electromagnético. Allí volverá la notación científica de la Lección 2.1, porque las longitudes de onda se manejan en potencias de diez.") + "</p>"
    glosario = [
        (t("Work (W)", "Trabajo (W)"), t("Force times the distance moved in the direction of the force: W = F × d, in joules.", "Fuerza por la distancia recorrida en su dirección: W = F × d, en julios.")),
        (t("Joule (J)", "Julio (J)"), t("The unit of work and energy: 1 J = 1 N · m.", "Unidad de trabajo y de energía: 1 J = 1 N · m.")),
        (t("Power (P)", "Potencia (P)"), t("How fast work is done: P = W ÷ t, in watts.", "Rapidez con que se realiza un trabajo: P = W ÷ t, en vatios.")),
        (t("Watt (W)", "Vatio (W)"), t("The unit of power: one joule per second.", "Unidad de potencia: un julio por segundo.")),
        (t("Kinetic energy", "Energía cinética"), t("Energy of motion: KE = ½ m v².", "Energía del movimiento: Ec = ½ m v².")),
        (t("Potential energy", "Energía potencial"), t("Energy of position (height): PE = m g h, with g = 9.8 m/s².", "Energía de posición (altura): Ep = m g h, con g = 9.8 m/s².")),
        (t("Conservation of energy", "Conservación de la energía"), t("Energy is neither created nor destroyed; it only changes form.", "La energía no se crea ni se destruye; solo cambia de forma.")),
    ]
    estd = C.estandares(["SP.7.b", "SP.6.c", "SP.1.c", "SP.3.b"], ["P.c"], base=["SP.4.a"])
    conexion = "<p>" + t("A change of question. Lesson 6.1 asked what makes motion change, and the answer was the net force. This lesson asks something else: what it costs to move something and what happens to that cost afterward. The answer is <strong>energy</strong>, and its most useful property is that it is not lost: it changes form.", "Cambio de pregunta. La 6.1 preguntaba qué hace que el movimiento cambie, y la respuesta era la fuerza neta. Esta lección pregunta otra cosa: cuánto cuesta mover algo y qué ocurre con ese coste después. La respuesta es la <strong>energía</strong>, y su propiedad más útil es que no se pierde: cambia de forma.") + "</p><p>" + \
               t("Rearranging formulas is already familiar from 5.2 and 6.1, so the work here is choosing the right formula and giving the result in the right unit. This lesson brings two new units, the joule and the watt, and both are easy to mix up. All the formulas (W = F · d, KE = ½ m v², PE = m · g · h) are on the GED formula sheet.", "El despeje ya se domina desde la 5.2 y la 6.1, de modo que lo que se trabaja aquí es elegir la fórmula correcta y expresar el resultado en la unidad correcta. Esta lección introduce dos unidades nuevas, el julio y el vatio, y ambas se confunden con facilidad. Todas las fórmulas (W = F · d, Ec = ½ m v², Ep = m · g · h) están en la hoja de fórmulas del GED.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> predict before you calculate, then compare your prediction with the number. Whoever reasons with conservation of energy first solves many test items without any math, because the test often asks “where is it greatest” and not “how much is it.”", "<strong>Cómo estudiar esta lección:</strong> prediga antes de calcular y después contraste la predicción con el resultado numérico. Quien razona primero con la conservación de la energía resuelve muchos ítems del examen sin operar, porque el examen pregunta con frecuencia «dónde es mayor» y no «cuánto vale».") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("What it costs to move something and where that energy goes: work, power, kinetic and potential energy, and the principle that energy only changes form.", "Cuánto cuesta mover algo y adónde va esa energía: trabajo, potencia, energía cinética y potencial, y el principio de que la energía solo cambia de forma."),
        ["SP.7 · " + t("Using formulas", "Aplicar fórmulas"), "SP.6 · " + t("Reading graphs and giving results", "Leer gráficas y expresar resultados")],
        [t("<strong>Calculate</strong> mechanical work and recognize when a force does no work.", "<strong>Calcular</strong> el trabajo mecánico y reconocer los casos en que una fuerza no realiza trabajo."),
         t("<strong>Calculate</strong> power and tell it apart from work.", "<strong>Calcular</strong> la potencia y distinguirla del trabajo."),
         t("<strong>Tell apart</strong> kinetic, potential, and mechanical energy in a system.", "<strong>Distinguir</strong> energía cinética, potencial y mecánica en un sistema."),
         t("<strong>Use</strong> conservation of energy to predict speed or height at a point, before calculating.", "<strong>Aplicar</strong> la conservación de la energía para predecir la velocidad o la altura en un punto, antes de calcular."),
         t("<strong>Explain</strong> a numerical result in its physical context, including energy turned into heat by friction.", "<strong>Interpretar</strong> el resultado numérico en su contexto físico, incluida la energía que la fricción transforma en calor.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("6-3", t("Heat and waves", "El calor y las ondas")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- práctica
def prob_trabajo():
    rnd = random.Random(64)
    ctx = [(("pushes a cart", "empuja un carrito"), ("pushes", "empuja")), (("pulls a sled", "arrastra un trineo"), ("pulls", "arrastra")), (("pushes a lawn mower", "empuja una cortadora de césped"), ("pushes", "empuja")),
           (("drags a box", "arrastra una caja"), ("drags", "arrastra")), (("lifts a bag of cement", "sube un saco de cemento"), ("lifts", "sube"))]
    out = []
    for n in range(30):
        (q, _) = ctx[n % len(ctx)]
        F = rnd.choice([10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
        d = D(rnd.choice(["2", "3", "4", "5", "6", "8", "10", "12", "1.5", "2.5"]))
        k = n % 5
        if k == 3:
            enun = t(f"A person holds a {F} N box still at chest height for 3 minutes. How much mechanical work is done, in <strong>J</strong>?", f"Una persona sostiene una caja de {F} N quieta a la altura del pecho durante 3 minutos. ¿Cuánto trabajo mecánico realiza, en <strong>J</strong>?")
            r, exp = "0", t("Nothing moves: d = 0, so W = 0 J, however tiring it is.", "No hay desplazamiento: d = 0, así que W = 0 J, por mucho que canse.")
        elif k == 4:
            W = F * d
            enun = t(f"A worker does {miles(W)} J of work pushing a cart with a force of {F} N. How far does the cart move, in <strong>m</strong>?", f"Un trabajador realiza {miles(W)} J de trabajo empujando un carro con una fuerza de {F} N. ¿Qué distancia recorre el carro, en <strong>m</strong>?")
            r, exp = fmt(d), t(f"d = W ÷ F = {miles(W)} ÷ {F} = {fmt(d)} m.", f"d = W ÷ F = {miles(W)} ÷ {F} = {fmt(d)} m.")
        else:
            W = F * d
            enun = t(f"A person {q[0]} with a force of {F} N for {fmt(d)} m. How much work is done, in <strong>J</strong>?", f"Una persona {q[1]} con una fuerza de {F} N a lo largo de {fmt(d)} m. ¿Qué trabajo realiza, en <strong>J</strong>?")
            r, exp = fmt(W), t(f"W = F × d = {F} × {fmt(d)} = {miles(W)} J.", f"W = F × d = {F} × {fmt(d)} = {miles(W)} J.")
        out.append({"enun": f"<p>{enun}</p>", "r": r, "exp": exp})
    return out


def prob_potencia():
    rnd = random.Random(65)
    out = []
    dev = [("motor", "motor"), ("crane", "grúa"), ("elevator", "ascensor"), ("pump", "bomba de agua"), ("person climbing stairs", "persona que sube escaleras")]
    for n in range(30):
        en, es = dev[n % len(dev)]
        art = "un" if es in ("motor", "ascensor") else "una"
        P_ = rnd.choice([20, 25, 40, 50, 60, 75, 100, 120, 150, 200, 250, 300, 500])
        tt = rnd.choice([2, 4, 5, 6, 8, 10, 12, 15, 20, 30, 40, 60])
        W = P_ * tt
        k = n % 3
        if k == 0:
            enun = t(f"A {en} does {W:,} J of work in {tt} s. What is its power, in <strong>W</strong>?", f"{art.capitalize()} {es} realiza {W:,} J de trabajo en {tt} s. ¿Cuál es su potencia, en <strong>W</strong>?")
            r, exp = str(P_), t(f"P = W ÷ t = {W:,} ÷ {tt} = {P_} W.", f"P = W ÷ t = {W:,} ÷ {tt} = {P_} W.")
        elif k == 1:
            enun = t(f"A {P_} W {en} runs for {tt} s. How much work does it do, in <strong>J</strong>?", f"{art.capitalize()} {es} de {P_} W funciona durante {tt} s. ¿Cuánto trabajo realiza, en <strong>J</strong>?")
            r, exp = str(W), t(f"W = P × t = {P_} × {tt} = {W:,} J.", f"W = P × t = {P_} × {tt} = {W:,} J.")
        else:
            enun = t(f"A {P_} W {en} has to do {W:,} J of work. How long does it take, in <strong>s</strong>?", f"{art.capitalize()} {es} de {P_} W tiene que realizar {W:,} J de trabajo. ¿Cuánto tarda, en <strong>s</strong>?")
            r, exp = str(tt), t(f"t = W ÷ P = {W:,} ÷ {P_} = {tt} s.", f"t = W ÷ P = {W:,} ÷ {P_} = {tt} s.")
        out.append({"enun": f"<p>{enun}</p>", "r": r, "exp": exp})
    return out


def prob_energia():
    rnd = random.Random(66)
    out = []
    for n in range(30):
        k = n % 3
        if k == 0:
            m = rnd.choice([2, 4, 6, 8, 10, 20, 50, 60, 80, 100]); v = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20])
            E = D(m) * v * v / 2
            enun = t(f"An object with a mass of {m} kg moves at {v} m/s. What is its kinetic energy, in <strong>J</strong>?", f"Un cuerpo de {m} kg se mueve a {v} m/s. ¿Cuál es su energía cinética, en <strong>J</strong>?")
            r, exp = fmt(E), t(f"KE = ½ × {m} × {v}² = ½ × {m} × {v * v} = {miles(E)} J.", f"Ec = ½ × {m} × {v}² = ½ × {m} × {v * v} = {miles(E)} J.")
        elif k == 1:
            m = rnd.choice([1, 2, 5, 10, 20, 25, 50, 60, 70, 100]); h = rnd.choice([1, 2, 3, 4, 5, 10, 12, 15, 20, 30])
            E = D(m) * D("9.8") * h
            enun = t(f"A {m} kg object is {h} m above the ground. What is its potential energy, in <strong>J</strong>? (Use g = 9.8 m/s².)", f"Un cuerpo de {m} kg está a {h} m sobre el suelo. ¿Cuál es su energía potencial, en <strong>J</strong>? (Use g = 9.8 m/s².)")
            r, exp = fmt(E), t(f"PE = m × g × h = {m} × 9.8 × {h} = {miles(E)} J.", f"Ep = m × g × h = {m} × 9.8 × {h} = {miles(E)} J.")
        else:
            m = rnd.choice([10, 20, 40, 50, 80, 100, 200, 500]); h = rnd.choice([2, 5, 8, 10, 20, 25, 40])
            E = m * 10 * h
            enun = t(f"A {m} kg roller-coaster car starts at rest {h} m high. With no friction, how much kinetic energy does it have at ground level, in <strong>J</strong>? (Use g = 10 m/s².)", f"Un vagón de {m} kg parte del reposo a {h} m de altura. Sin fricción, ¿cuánta energía cinética tiene al nivel del suelo, en <strong>J</strong>? (Use g = 10 m/s².)")
            r, exp = str(E), t(f"All its potential energy turns into kinetic: PE = {m} × 10 × {h} = {E:,} J, so KE = {E:,} J at the bottom.", f"Toda su energía potencial se transforma en cinética: Ep = {m} × 10 × {h} = {E:,} J, así que Ec = {E:,} J abajo.")
        out.append({"enun": f"<p>{enun}</p>", "r": r, "exp": exp})
    return out


def banco_montana():
    rnd = random.Random(67)
    letras = "ABCDE"
    out = []
    for n in range(14):
        alt = rnd.sample([5, 12, 18, 25, 32, 40, 48], 5)
        alt[0] = max(alt) + 6
        sp = {"tipo": "barras", "xEtq": t("Point on the ride", "Punto del recorrido"), "yEtq": t("Height (m)", "Altura (m)"), "py": 10, "barras": [{"etq": l, "valor": a} for l, a in zip(letras, alt)]}
        tipo = n % 4
        mx, mn = letras[alt.index(max(alt))], letras[alt.index(min(alt))]
        orden = sorted(range(5), key=lambda i: alt[i])
        if tipo == 0:
            q, r, e = t("At which point is the car <strong>fastest</strong>?", "¿En qué punto va más <strong>rápido</strong> el vagón?"), mn, t(f"Lowest point ({mn}) → least potential energy → most kinetic energy and speed.", f"Punto más bajo ({mn}) → menor energía potencial → mayor energía cinética y velocidad.")
        elif tipo == 1:
            q, r, e = t("At which point is the <strong>potential energy</strong> highest?", "¿En qué punto es máxima la <strong>energía potencial</strong>?"), mx, t(f"Highest point ({mx}) → most potential energy.", f"Punto más alto ({mx}) → mayor energía potencial.")
        elif tipo == 2:
            q, r, e = t("At which point is the car <strong>slowest</strong>?", "¿En qué punto va más <strong>despacio</strong> el vagón?"), mx, t(f"Highest point ({mx}) → least kinetic energy → slowest.", f"Punto más alto ({mx}) → menor energía cinética → más lento.")
        else:
            seg = letras[orden[1]]
            q, r, e = t("Which point has the <strong>second-highest</strong> kinetic energy?", "¿Qué punto tiene la <strong>segunda</strong> mayor energía cinética?"), seg, t(f"Second-lowest point ({seg}) → second-highest kinetic energy.", f"Segundo punto más bajo ({seg}) → segunda mayor energía cinética.")
        enun = "<p>" + t("Heights of a roller-coaster car at five points of a ride (the car starts at A, almost at rest; ignore friction):", "Alturas de un vagón de montaña rusa en cinco puntos de un recorrido (parte de A casi en reposo; sin fricción):") + "</p>" + C.grafica(sp, C.describe(sp), ancho=480, alto=270, y0=0) + f"<p><strong>{q}</strong></p>"
        out.append({"enun": enun, "ops": list(letras), "ok": letras.index(r), "enOrden": True,
                    "pista": t("Higher → more potential energy, less speed. Lower → more kinetic energy, more speed.", "Más alto → más energía potencial, menos velocidad. Más bajo → más energía cinética, más velocidad."), "exp": e})
    return out


def banco_transf():
    E = {"q": t("Chemical", "Química"), "e": t("Electrical", "Eléctrica"), "l": t("Light", "Luminosa"), "k": t("Kinetic (motion)", "Cinética (movimiento)"), "p": t("Potential (height)", "Potencial (altura)"), "s": t("Sound", "Sonora"), "c": t("Heat", "Calor")}
    d = [(t("A battery-powered flashlight", "Una linterna de pilas"), "q", "l"), (t("An electric fan", "Un ventilador eléctrico"), "e", "k"), (t("A solar panel", "Un panel solar"), "l", "e"),
         (t("A car engine", "El motor de un automóvil"), "q", "k"), (t("A water heater", "Un calentador de agua"), "e", "c"), (t("A hydroelectric dam", "Una presa hidroeléctrica"), "p", "e"),
         (t("A speaker", "Un altavoz"), "e", "s"), (t("A person climbing stairs (food energy)", "Una persona que sube escaleras (energía de los alimentos)"), "q", "p"),
         (t("A blender", "Una licuadora"), "e", "k"), (t("A wind turbine", "Un aerogenerador"), "k", "e"), (t("A campfire", "Una fogata"), "q", "c"), (t("A light bulb", "Una bombilla"), "e", "l")]
    out = []
    claves = list(E)
    rnd = random.Random(68)
    for disp, a, b in d:
        ok = f"{E[a]} → {E[b]}"
        dist = {f"{E[b]} → {E[a]}"}
        while len(dist) < 3:
            x, y = rnd.sample(claves, 2)
            if (x, y) != (a, b) and (x, y) != (b, a):
                dist.add(f"{E[x]} → {E[y]}")
        ops = [ok] + sorted(dist)
        rnd.shuffle(ops)
        out.append({"enun": f"<p><strong>{disp}</strong></p><p>" + t("What is the main energy change (energy in → useful energy out)?", "¿Cuál es la transformación principal (energía que entra → energía útil que sale)?") + "</p>", "ops": ops, "ok": ops.index(ok),
                    "pista": t("Ask what the device runs on and what it is for.", "Pregúntese de qué se alimenta el aparato y para qué sirve."), "exp": t(f"{ok}. Some energy also turns into heat, as in every device.", f"{ok}. Algo de energía también se transforma en calor, como en todo aparato.")})
    extra = [(t("In every device on this list, part of the energy also becomes…", "En todos los aparatos de esta lista, parte de la energía también se transforma en…"), [t("heat", "calor"), t("mass", "masa"), t("nothing: it disappears", "nada: desaparece")], 0, t("Heat is the usual “by-product.”", "El calor es el «subproducto» habitual.")),
             (t("An LED bulb and an incandescent bulb give the same light. The LED uses less electricity because…", "Una bombilla LED y una incandescente dan la misma luz. La LED consume menos electricidad porque…"), [t("it turns less of the energy into heat", "transforma menos energía en calor"), t("it destroys less energy", "destruye menos energía"), t("it creates light from nothing", "crea luz de la nada")], 0, t("Less heat, more of the energy becomes light.", "Menos calor: más energía se convierte en luz.")),
             (t("Saying “the car lost energy when braking” is imprecise. It is better to say that…", "Decir «el auto perdió energía al frenar» es impreciso. Es mejor decir que…"), [t("its kinetic energy turned into heat in the brakes", "su energía cinética se transformó en calor en los frenos"), t("its energy was destroyed", "su energía se destruyó"), t("its energy became mass", "su energía se convirtió en masa")], 0, t("Transformation, not disappearance.", "Transformación, no desaparición."))]
    for q, o, k, e in extra:
        out.append({"enun": f"<p>{q}</p>", "ops": o, "ok": k, "pista": t("Energy is never created or destroyed.", "La energía nunca se crea ni se destruye."), "exp": e})
    return out


def practica():
    A = {"en": ["work", "power", "energy", "roller-coaster", "changes"], "es": ["trabajo", "potencia", "energia", "montana-rusa", "transformaciones"]}[C.L]
    instr = "      <p>" + t("Choose the formula, calculate, and write only the number (the unit is in the question). You can use the calculator.", "Elija la fórmula, calcule y escriba solo el número (la unidad está en la pregunta). Puede usar la calculadora.") + "</p>\n"
    mods = [
        (A[0], t("Work problems", "Problemas de trabajo"), instr + C.dec_campo("m1", t("Answer", "Respuesta"))),
        (A[1], t("Power problems", "Problemas de potencia"), instr + C.dec_campo("m2", t("Answer", "Respuesta"))),
        (A[2], t("Kinetic and potential energy", "Energía cinética y potencial"), instr + C.dec_campo("m3", t("Answer", "Respuesta"))),
        (A[3], t("Predict on the roller coaster", "Prediga en la montaña rusa"), C.om("m4", t("Read the heights and answer without calculating.", "Lea las alturas y responda sin calcular."))),
        (A[4], t("Energy changes", "Transformaciones de energía"), C.om("m5", t("What goes in and what useful energy comes out?", "¿Qué energía entra y cuál sale útil?"))),
    ]
    pT = t("W = F × d · d = W ÷ F. If nothing moves, W = 0.", "W = F × d · d = W ÷ F. Si no hay desplazamiento, W = 0.")
    pP = t("P = W ÷ t · W = P × t · t = W ÷ P.", "P = W ÷ t · W = P × t · t = W ÷ P.")
    pE = t("KE = ½ × m × v² (square the speed first) · PE = m × g × h.", "Ec = ½ × m × v² (eleve primero la velocidad al cuadrado) · Ep = m × g × h.")
    js = (C.js_datos("TRA", prob_trabajo()) + C.js_datos("POT", prob_potencia()) + C.js_datos("ENE", prob_energia()) + C.js_datos("MON", banco_montana()) + C.js_datos("TRF", banco_transf()) +
          f"function gen(B, p){{ var s = mazo(B); return function(){{ var q = s(); return {{enun: q.enun, resp: leeNumero(q.r), explica: q.exp, pista: function(){{ return p; }}}}; }}; }}\n" +
          f'creaPracticaDec("m1", gen(TRA, {C.json.dumps(pT, ensure_ascii=False)}));\ncreaPracticaDec("m2", gen(POT, {C.json.dumps(pP, ensure_ascii=False)}));\ncreaPracticaDec("m3", gen(ENE, {C.json.dumps(pE, ensure_ascii=False)}));\n' +
          'creaBanco("m4", MON);\ncreaBanco("m5", TRF);\n')
    return C.pagina_practica(N, titulo(), t("Five activities · new exercises every time · two tries in each one · calculator included", "Cinco actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"),
                             mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
