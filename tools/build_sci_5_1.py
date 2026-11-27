"""LearnGED · Ciencias · Lección 5.1 · El átomo, la tabla periódica y los enlaces químicos (EN/ES).
Fuente: clases_ciencias/leccion_5-1.html (diagramas en tools/svg/5-1_*.svg) y el interactivo ciencias/atomo (tabla_periodica).
Uso: python3 tools/build_sci_5_1.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "5-1"


def titulo():
    return t("The atom, the periodic table, and chemical bonds", "El átomo, la tabla periódica y los enlaces químicos")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


def svg_bohr():
    return C.svg_orig("5-1_0", {
        "3 p⁺": "3 p⁺", "4 n⁰": "4 n⁰", "−": "−", "Litio · 3 protones, 4 neutrones, 3 electrones": "Lithium · 3 protons, 4 neutrons, 3 electrons", "Núcleo": "Nucleus",
        "Protones (carga +) y neutrones (sin carga).": "Protons (+ charge) and neutrons (no charge).", "Concentra casi toda la masa del átomo.": "Almost all the atom’s mass is here.",
        "Primer nivel de energía": "First energy level", "Admite un máximo de 2 electrones.": "Holds at most 2 electrons.", "Segundo nivel de energía": "Second energy level",
        "Admite un máximo de 8 electrones.": "Holds at most 8 electrons.", "Aquí solo hay 1: es el electrón de valencia,": "There is only 1 here: the valence electron,",
        "y de él dependerá todo el enlace químico.": "and all chemical bonding depends on it."},
        "Bohr model of a lithium atom. In the center is a nucleus with three positively charged protons and four neutrons with no charge. Around the nucleus, two energy levels are drawn as circles: the first level, the closest, has two negatively charged electrons; the second level has one electron. In all there are three protons and three electrons, so the atom is electrically neutral. The only electron in the outer level is the valence electron.")


def svg_tabla():
    tr = {k: k for k in ("1", "2", "17", "18")}
    tr.update({"El número atómico aumenta en este sentido": "The atomic number increases this way", "Metales de transición": "Transition metals", "Aquí están los no metales": "The nonmetals are here",
               "METALES": "METALS", "Tienden a perder electrones": "Tend to lose electrons", "NO METALES": "NONMETALS", "Tienden a ganar electrones": "Tend to gain electrons",
               "Cada columna es un grupo · Cada fila es un periodo": "Each column is a group · Each row is a period",
               "Grupo 1 · Metales alcalinos: 1 electrón de valencia. Muy reactivos.": "Group 1 · Alkali metals: 1 valence electron. Very reactive.",
               "Grupo 2 · Metales alcalinotérreos: 2 electrones de valencia.": "Group 2 · Alkaline earth metals: 2 valence electrons.",
               "Grupo 17 · Halógenos: 7 electrones de valencia. Les falta uno para completar el nivel.": "Group 17 · Halogens: 7 valence electrons. One short of a full level.",
               "Grupo 18 · Gases nobles: el nivel exterior ya está completo. Casi no reaccionan.": "Group 18 · Noble gases: the outer level is already full. They hardly react."})
    return C.svg_orig("5-1_1", tr, "Simplified diagram of the periodic table. The columns are called groups and the rows, periods. From left to right: group 1, group 2, a wide block of transition metals, a block where the nonmetals are, group 17, and group 18 at the far right. An arrow at the top shows that the atomic number increases from left to right and from top to bottom. Metals are on the left of the table and nonmetals on the right. The key says that group 1 is the alkali metals with one valence electron, group 2 the alkaline earth metals with two, group 17 the halogens with seven, and group 18 the noble gases with a full outer level.")


def svg_enlaces():
    tr = {k: k for k in ("Na", "Cl", "−", "Na⁺", "Cl⁻", "↔", "O", "H")}
    tr.update({"Enlace iónico": "Ionic bond", "El electrón se transfiere": "The electron is transferred", "Metal · 1 e⁻ de valencia": "Metal · 1 valence e⁻", "No metal · le falta 1 e⁻": "Nonmetal · 1 e⁻ short",
               "Cargas opuestas que se atraen:": "Opposite charges attract:", "sal común (NaCl)": "table salt (NaCl)", "Enlace covalente": "Covalent bond", "Los electrones se comparten": "The electrons are shared",
               "Los dos electrones del centro": "The two electrons in the middle", "pertenecen a los dos átomos a la vez": "belong to both atoms at once", "Molécula de agua (H₂O)": "Water molecule (H₂O)",
               "Dos no metales unidos": "Two nonmetals joined"})
    return C.svg_orig("5-1_2", tr, "Comparison of an ionic bond and a covalent bond. In the left panel, the ionic bond: a sodium atom, a metal with one valence electron, transfers that electron to a chlorine atom, a nonmetal that is one electron short. The result is two ions with opposite charges, positive sodium and negative chloride, which attract each other. In the right panel, the covalent bond: two nonmetal atoms, here oxygen and hydrogen, share a pair of electrons that belongs to both at once, and form a molecule. Conclusion: metal plus nonmetal makes an ionic bond, and nonmetal plus nonmetal makes a covalent bond.")


# (Z, símbolo, nombre EN, nombre ES, número másico común, grupo, periodo, tipo: m/n/g)
ELEM = [(1, "H", "hydrogen", "hidrógeno", 1, 1, 1, "n"), (2, "He", "helium", "helio", 4, 18, 1, "g"), (3, "Li", "lithium", "litio", 7, 1, 2, "m"), (6, "C", "carbon", "carbono", 12, 14, 2, "n"),
        (7, "N", "nitrogen", "nitrógeno", 14, 15, 2, "n"), (8, "O", "oxygen", "oxígeno", 16, 16, 2, "n"), (9, "F", "fluorine", "flúor", 19, 17, 2, "n"), (10, "Ne", "neon", "neón", 20, 18, 2, "g"),
        (11, "Na", "sodium", "sodio", 23, 1, 3, "m"), (12, "Mg", "magnesium", "magnesio", 24, 2, 3, "m"), (13, "Al", "aluminum", "aluminio", 27, 13, 3, "m"), (14, "Si", "silicon", "silicio", 28, 14, 3, "n"),
        (15, "P", "phosphorus", "fósforo", 31, 15, 3, "n"), (16, "S", "sulfur", "azufre", 32, 16, 3, "n"), (17, "Cl", "chlorine", "cloro", 35, 17, 3, "n"), (18, "Ar", "argon", "argón", 40, 18, 3, "g"),
        (19, "K", "potassium", "potasio", 39, 1, 4, "m"), (20, "Ca", "calcium", "calcio", 40, 2, 4, "m"), (26, "Fe", "iron", "hierro", 56, 8, 4, "m"), (29, "Cu", "copper", "cobre", 64, 11, 4, "m"),
        (30, "Zn", "zinc", "cinc", 65, 12, 4, "m"), (35, "Br", "bromine", "bromo", 80, 17, 4, "n"), (47, "Ag", "silver", "plata", 108, 11, 5, "m"), (53, "I", "iodine", "yodo", 127, 17, 5, "n"),
        (79, "Au", "gold", "oro", 197, 11, 6, "m")]
IONES = [("Na", 1), ("K", 1), ("Li", 1), ("Mg", 2), ("Ca", 2), ("Al", 3), ("F", -1), ("Cl", -1), ("Br", -1), ("O", -2), ("S", -2), ("N", -3)]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("All matter is made of atoms, and every atom has the same design: a central <strong>nucleus</strong>, very small and very dense, and a much larger outer region where the <strong>electrons</strong> are. The differences between one element and another are not in the design, but in the number of particles.", "Toda la materia está formada por átomos, y todo átomo tiene la misma arquitectura: un <strong>núcleo</strong> central, muy pequeño y muy denso, y una región exterior mucho más amplia donde se encuentran los <strong>electrones</strong>. Las diferencias entre un elemento y otro no están en el diseño, sino en el número de partículas.")}</p>
{svg_bohr()}
{C.tabla(t("The three subatomic particles with their electric charge, where they are in the atom, and their relative mass", "Las tres partículas subatómicas con su carga eléctrica, su localización en el átomo y su masa relativa"),
 [t("Particle", "Partícula"), t("Charge", "Carga"), t("Where it is", "Dónde se encuentra"), t("Relative mass", "Masa relativa")],
 [[t("Proton", "Protón"), t("Positive (+)", "Positiva (+)"), t("In the nucleus", "En el núcleo"), t("1 unit", "1 unidad")],
  [t("Neutron", "Neutrón"), t("No charge (0)", "Sin carga (0)"), t("In the nucleus", "En el núcleo"), t("1 unit", "1 unidad")],
  [t("Electron", "Electrón"), t("Negative (−)", "Negativa (−)"), t("Outside the nucleus, in energy levels", "Fuera del núcleo, en niveles de energía"), t("About 1,800 times smaller", "Unas 1,800 veces menor")]])}
<p>{t("The test often uses something that follows from that table: since the electron has almost no mass, nearly all the atom’s mass is in the nucleus. Gaining or losing an electron does not change the mass noticeably; gaining or losing a neutron does.", "De esa tabla se desprende algo que el examen aprovecha con frecuencia: como el electrón tiene una masa casi despreciable, la masa del átomo está prácticamente toda en el núcleo. Ganar o perder un electrón no cambia la masa de manera apreciable; ganar o perder un neutrón sí.")}</p>
<h3>{t("The two numbers that describe an atom", "Los dos números que definen a un átomo")}</h3>
{C.tabla(t("Atomic number and mass number, what each counts, and how to find it", "Definición del número atómico y del número másico, con la operación que permite calcularlos"),
 [t("Number", "Número"), t("What it counts", "Qué cuenta"), t("How to find it", "Cómo se obtiene")],
 [[t("Atomic number (Z)", "Número atómico (Z)"), t("The protons in the nucleus", "Los protones del núcleo"), t("The periodic table gives it. It identifies the element.", "Lo indica la tabla periódica. Es el que identifica al elemento.")],
  [t("Mass number (A)", "Número másico (A)"), t("Protons plus neutrons", "Los protones más los neutrones"), t("A = protons + neutrons. So neutrons = A − Z.", "A = protones + neutrones. En consecuencia, neutrones = A − Z.")]])}
{C.caja("tip", t("The atomic number is the element’s identity", "El número atómico es la identidad del elemento"), "<p>" + t("No exceptions. An atom with 6 protons is carbon, whatever its neutrons or electrons. If the number of protons changes, it is no longer carbon. So for any question like “which element is it?”, the only number to look for is the protons.", "No admite excepciones. Un átomo con 6 protones es carbono, tenga los neutrones que tenga y los electrones que tenga. Si el número de protones cambia, deja de ser carbono. Por eso, ante cualquier pregunta del tipo «¿de qué elemento se trata?», la única cifra que hay que buscar es la de los protones.") + "</p>")}
{C.ejemplo(t("Example 1 · Protons, neutrons, and electrons", "Ejemplo 1 · Protones, neutrones y electrones"),
 [("", t("Aluminum has atomic number 13 and mass number 27. Find its protons, neutrons, and electrons, if the atom is neutral.", "El átomo de aluminio tiene número atómico 13 y número másico 27. Determine sus protones, neutrones y electrones, suponiendo que el átomo es neutro.")),
  ("1", t("<strong>Protons.</strong> The atomic number is the number of protons: <strong>13 protons</strong>.", "<strong>Protones.</strong> El número atómico es el número de protones: <strong>13 protones</strong>.")),
  ("2", t("<strong>Electrons.</strong> The atom is neutral, so positive and negative charges balance: as many electrons as protons, <strong>13 electrons</strong>.", "<strong>Electrones.</strong> El enunciado dice que el átomo es neutro, de modo que las cargas se compensan: hay tantos electrones como protones, <strong>13 electrones</strong>.")),
  ("3", t("<strong>Neutrons.</strong> Subtract: 27 − 13 = <strong>14 neutrons</strong>.", "<strong>Neutrones.</strong> Se restan: 27 − 13 = <strong>14 neutrones</strong>.")),
  ("4", t("<strong>Check.</strong> 13 protons + 14 neutrons = 27, exactly the mass number. Always check a subtraction with the opposite addition.", "<strong>Comprobación.</strong> 13 protones + 14 neutrones = 27, que es justamente el número másico. La resta se verifica siempre con la suma inversa."))])}
{C.caja("ojo", t("The atomic mass in the table is not the mass number", "La masa atómica de la tabla no es el número másico"), "<p>" + t("In the periodic table, under the element’s symbol, there is usually a number with decimals: chlorine’s is 35.45. That value is an average of all the element’s isotopes as they are found in nature, which is why it is not a whole number. The mass number is always a whole number and belongs to one specific atom. When an exercise asks for neutrons from the table’s atomic mass, round to the nearest whole number.", "En la tabla periódica, bajo el símbolo del elemento, suele aparecer un número con decimales: el del cloro es 35.45. Ese valor es un promedio de todos los isótopos del elemento tal como se encuentran en la naturaleza, y por eso no es entero. El número másico, en cambio, es siempre un número entero y corresponde a un átomo concreto. Cuando un ejercicio pide neutrones a partir de la masa atómica de la tabla, se redondea al entero más cercano.") + "</p>")}
{P(t("Try it 1 · Neutrons", "Pruebe 1 · Neutrones"), t("An atom has atomic number 19 and mass number 39. How many neutrons does it have?", "Un átomo tiene número atómico 19 y número másico 39. ¿Cuántos neutrones tiene?"), ["19", "20", "39"], 1,
   {0: t("19 is the protons.", "19 son los protones."), 2: t("39 is protons + neutrons.", "39 son protones + neutrones.")}, t("39 − 19 = 20.", "39 − 19 = 20."))}
{C.enlace(N, anc("count", "contar"), t("count the particles", "cuente las partículas"), t("New atoms and ions every time: protons, neutrons, and electrons.", "Átomos e iones nuevos cada vez: protones, neutrones y electrones."))}"""

    s2 = f"""<p>{t("An atom can differ from the basic description in two different ways, and the test often sets them side by side because they are easy to confuse. One question settles it: <strong>which particle changed?</strong>", "Un átomo puede apartarse de la descripción básica de dos maneras distintas, y el examen las contrapone con frecuencia porque se confunden con facilidad. La diferencia se resuelve con una sola pregunta: <strong>¿qué partícula cambió?</strong>")}</p>
{C.tabla(t("Isotope and ion compared: the particle that changes, the effect on mass and charge, and an example", "Comparación entre isótopo e ion según la partícula que cambia, el efecto sobre la masa, el efecto sobre la carga y un ejemplo de cada caso"),
 [t("Test", "Criterio"), t("Isotope", "Isótopo"), t("Ion", "Ion")],
 [[t("Particle that changes", "Partícula que cambia"), t("The number of neutrons", "El número de neutrones"), t("The number of electrons", "El número de electrones")],
  [t("Effect on mass", "Efecto sobre la masa"), t("The mass number changes", "Cambia el número másico"), t("Almost no change", "Prácticamente no cambia")],
  [t("Effect on charge", "Efecto sobre la carga"), t("None: still neutral", "Ninguno: sigue siendo neutro"), t("It gets a positive or negative charge", "Queda con carga positiva o negativa")],
  [t("Still the same element?", "¿Sigue siendo el mismo elemento?"), t("Yes, because the protons do not change", "Sí, porque los protones no cambian"), t("Yes, because the protons do not change", "Sí, porque los protones no cambian")],
  [t("Example", "Ejemplo"), t("Carbon-12 and carbon-14: both have 6 protons, with 6 and 8 neutrons", "Carbono-12 y carbono-14: 6 protones ambos, 6 y 8 neutrones"), t("Na⁺: sodium has lost one electron; Cl⁻: chlorine has gained one", "Na⁺: el sodio ha perdido un electrón; Cl⁻: el cloro ha ganado uno")]])}
<p>{t("Keep carbon-14 in mind, because it comes back in Topic 7. It is an unstable isotope, and that instability is what lets us date ancient remains: we know how fast it decays, so the share left in a sample tells how much time has passed. But chemically, carbon-14 behaves just like carbon-12, because electrons decide chemical behavior and both have six.", "El caso del carbono-14 conviene retenerlo porque reaparecerá en el Tema 7. Es un isótopo inestable, y esa inestabilidad es lo que permite datar restos antiguos: se conoce el ritmo al que se desintegra, de modo que la proporción que queda en una muestra informa del tiempo transcurrido. Pero, químicamente, el carbono-14 se comporta igual que el carbono-12, porque el comportamiento químico lo deciden los electrones y ambos tienen seis.")}</p>
<h3>{t("Cations and anions", "Cationes y aniones")}</h3>
<p>{t("When an atom loses electrons, it has more positive charges than negative ones, and the result is a <strong>cation</strong>, with a positive charge. When it gains electrons, there are extra negative charges, and the result is an <strong>anion</strong>. The logic is arithmetic: the charge of the ion is the difference between protons and electrons.", "Cuando un átomo pierde electrones, se queda con más cargas positivas que negativas y el resultado es un <strong>catión</strong>, de carga positiva. Cuando gana electrones, sobran cargas negativas y el resultado es un <strong>anión</strong>. La lógica es aritmética: la carga del ion es la diferencia entre protones y electrones.")}</p>
{C.ejemplo(t("Example 2 · Electrons in an ion", "Ejemplo 2 · Electrones de un ion"),
 [("", t("The magnesium ion is written Mg²⁺. Magnesium has atomic number 12. How many electrons does this ion have?", "El ion magnesio se representa Mg²⁺. El magnesio tiene número atómico 12. ¿Cuántos electrones tiene ese ion?")),
  ("1", t("<strong>Protons.</strong> The atomic number never changes: 12 protons, that is, 12 positive charges.", "<strong>Protones.</strong> El número atómico no cambia nunca: 12 protones, es decir, 12 cargas positivas.")),
  ("2", t("<strong>Read the sign.</strong> 2+ means there are two extra positive charges. That can only happen if two electrons are missing.", "<strong>Lectura del signo.</strong> El 2+ indica que hay dos cargas positivas en exceso. Eso solo puede ocurrir si faltan dos electrones.")),
  ("3", t("<strong>Calculate.</strong> 12 − 2 = <strong>10 electrons</strong>.", "<strong>Cálculo.</strong> 12 − 2 = <strong>10 electrones</strong>.")),
  ("4", t("<strong>Check.</strong> 12 positive charges minus 10 negative ones leave 2 positive, exactly what the symbol says.", "<strong>Comprobación.</strong> 12 cargas positivas menos 10 negativas dejan un saldo de 2 positivas, que es exactamente lo que dice el símbolo."))])}
{C.caja("ojo", t("The most common mistake here", "El error más frecuente del examen en este punto"), "<p>" + t("Thinking that the plus sign means the atom gained something. It is the other way around. A positive ion is positive because it <strong>lost</strong> electrons, which are the negative particles. Remember it in a phrase: <strong>lose negative, end up positive</strong>.", "Suponer que el signo positivo significa que el átomo ganó algo. Es al revés. Un ion positivo lo es porque <strong>perdió</strong> electrones, que son las partículas negativas. Conviene fijarlo con una frase: <strong>pierde negativo, queda positivo</strong>.") + "</p>")}
{P(t("Try it 2 · Same protons", "Pruebe 2 · Mismos protones"), t("Two atoms each have 8 protons, but one has 8 neutrons and the other 10. They are…", "Dos átomos tienen 8 protones cada uno, pero uno tiene 8 neutrones y el otro 10. Se trata de…"),
   [t("two different elements", "dos elementos distintos"), t("two ions of the same element", "dos iones del mismo elemento"), t("two isotopes of the same element", "dos isótopos del mismo elemento")], 2,
   {0: t("Same protons = same element.", "Mismos protones = mismo elemento."), 1: t("Ions differ in electrons, not neutrons.", "Los iones difieren en electrones, no en neutrones.")}, t("Neutrons changed: isotopes.", "Cambiaron los neutrones: isótopos."))}
{P(t("Try it 3 · Fluoride", "Pruebe 3 · El fluoruro"), t("The fluoride ion is written F⁻, and fluorine has atomic number 9. This ion has…", "El ion fluoruro se escribe F⁻ y el flúor tiene número atómico 9. Ese ion tiene…"),
   [t("9 protons and 10 electrons", "9 protones y 10 electrones"), t("10 protons and 9 electrons", "10 protones y 9 electrones"), t("9 protons and 8 electrons", "9 protones y 8 electrones")], 0,
   {1: t("Protons never change in an ion.", "Los protones nunca cambian en un ion."), 2: t("A minus sign means it gained an electron.", "El signo menos indica que ganó un electrón.")}, t("9 protons; one extra electron: 10.", "9 protones; un electrón de más: 10."))}
{C.enlace(N, anc("isotope-ion", "isotopo-ion"), t("isotope or ion?", "¿isótopo o ion?"), t("Which particle changed, and what happens to the mass and the charge?", "¿Qué partícula cambió, y qué pasa con la masa y la carga?"))}"""

    s3 = f"""<p>{t("The periodic table is not a list of names to memorize. It is an organized data table, and its organization is not arbitrary: an element’s place predicts how it will behave. If you can read it, you do not need to remember the properties of calcium, because you can work them out from where it is.", "La tabla periódica no es una lista de nombres que haya que aprender de memoria. Es una tabla de datos organizada, y su organización no es arbitraria: la posición de un elemento anticipa cómo se va a comportar. Quien sabe leerla no necesita recordar las propiedades del calcio, porque puede deducirlas de dónde está.")}</p>
{svg_tabla()}
<h3>{t("The two coordinates: group and period", "Las dos coordenadas: grupo y periodo")}</h3>
{C.tabla(t("What group and period mean in the periodic table and what each one predicts", "Significado del grupo y del periodo en la tabla periódica y consecuencia de cada uno sobre las propiedades del elemento"),
 [t("Coordinate", "Coordenada"), t("What it is", "Qué es"), t("What it predicts", "Qué permite predecir")],
 [[t("Group (column)", "Grupo (columna)"), t("Each of the 18 vertical columns", "Cada una de las 18 columnas verticales"), t("Elements in the same group have the same number of valence electrons, so they behave alike. Sodium and potassium react the same way because both are in group 1.", "Los elementos de un mismo grupo tienen el mismo número de electrones de valencia, y por eso se comportan de forma parecida. El sodio y el potasio reaccionan igual porque los dos están en el grupo 1.")],
  [t("Period (row)", "Periodo (fila)"), t("Each of the 7 horizontal rows", "Cada una de las 7 filas horizontales"), t("The period number tells how many energy levels the atom has. An element in period 3 has three levels in use.", "El número del periodo indica cuántos niveles de energía tiene el átomo. Un elemento del periodo 3 tiene tres niveles ocupados.")]])}
<p>{t("<strong>Valence electrons</strong> are the ones in the outermost level, and they are the only ones that take part in bonds. The lithium in the first diagram had only one in its outer level: that is what makes lithium a group 1 element. For groups 1, 2, and 13 to 18 there is a handy shortcut: groups 1 and 2 have one and two valence electrons; in groups 13 to 18, subtract 10 from the group number, so group 17 has seven and group 18 has eight.", "Los <strong>electrones de valencia</strong> son los del nivel más externo, y son los únicos que participan en los enlaces. En el litio del diagrama anterior había uno solo en el nivel exterior: eso es lo que hace del litio un elemento del grupo 1. Para los grupos 1, 2 y 13 a 18 existe un atajo cómodo: los grupos 1 y 2 tienen uno y dos electrones de valencia; en los grupos 13 a 18 se resta 10 al número del grupo, de manera que el grupo 17 tiene siete y el grupo 18, ocho.")}</p>
{C.caja("tip", t("The question the test really asks", "La pregunta que el examen hace realmente"), "<p>" + t("Items rarely ask just “how many valence electrons does sulfur have?” They usually give part of the table or the element’s data in the question and ask which element will behave like another. Always look for the answer in the same <strong>column</strong>, not the same row.", "Los ítems no suelen pedir «¿cuántos electrones de valencia tiene el azufre?» a secas. Suelen dar un fragmento de tabla o los datos del elemento dentro del propio enunciado y preguntar qué elemento se comportará de forma parecida a otro. La respuesta se busca siempre en la misma <strong>columna</strong>, no en la misma fila.") + "</p>")}
{C.ejemplo(t("Example 3 · An unknown element", "Ejemplo 3 · Un elemento desconocido"),
 [("", t("An unknown element is in group 2 and period 4. What can you say about it without knowing its name?", "Un elemento desconocido está en el grupo 2 y en el periodo 4. ¿Qué se puede afirmar de él sin conocer su nombre?")),
  ("1", t("<strong>From the group.</strong> Group 2 means two valence electrons. It is an alkaline earth metal and will tend to lose those two electrons, forming an ion with a 2+ charge.", "<strong>Por el grupo.</strong> Grupo 2 significa dos electrones de valencia. Es un metal alcalinotérreo y tenderá a perder esos dos electrones, formando un ion de carga 2+.")),
  ("2", t("<strong>From the period.</strong> Period 4 means four energy levels in use.", "<strong>Por el periodo.</strong> Periodo 4 significa cuatro niveles de energía ocupados.")),
  ("3", t("<strong>From its general position.</strong> It is on the left of the table, so it is a metal: it conducts electricity and reacts with nonmetals.", "<strong>Por la posición general.</strong> Está en la parte izquierda de la tabla, luego es un metal: conduce la electricidad y reacciona con los no metales.")),
  ("4", t("<strong>Predict.</strong> It will behave like magnesium and calcium, which are in its column. None of this needed you to know the element is calcium.", "<strong>Predicción de comportamiento.</strong> Se parecerá al magnesio y al calcio, que están en su misma columna. Nada de esto ha exigido saber que el elemento es el calcio."))])}
{P(t("Try it 4 · Same behavior", "Pruebe 4 · Mismo comportamiento"), t("Element X is in group 17. Which of these will behave most like X?", "El elemento X está en el grupo 17. ¿Cuál de estos elementos se comportará de manera más parecida a X?"),
   [t("One next to it, in group 16", "Uno situado a su lado, en el grupo 16"), t("Another one in group 17, in a different period", "Otro situado en el grupo 17, en un periodo distinto"), t("One in the same period, in group 2", "Uno situado en su mismo periodo, en el grupo 2")], 1,
   {0: t("Neighbors in a row are not alike.", "Los vecinos de fila no se parecen."), 2: t("Same row does not mean same behavior.", "Misma fila no significa mismo comportamiento.")}, t("Same column, same valence electrons.", "Misma columna, mismos electrones de valencia."))}
{C.enlace(N, anc("table", "tabla"), t("read the periodic table", "lea la tabla periódica"), t("Group, period, valence electrons, and who behaves alike.", "Grupo, periodo, electrones de valencia y quién se comporta igual."))}"""

    s4 = f"""<p>{t("The noble gases in group 18 hardly react with anything, and that is where the whole explanation of bonding starts. Their outer level is full, with eight electrons, and in that state an atom is stable and needs nothing. Other elements are not so lucky: their outer level is incomplete, and all their chemical behavior is about getting that full arrangement. That tendency is called the <strong>octet rule</strong>.", "Los gases nobles del grupo 18 casi no reaccionan con nada, y esa es la observación de la que arranca toda la explicación del enlace. Su nivel exterior está completo, con ocho electrones, y en ese estado un átomo es estable y no necesita nada. Los demás elementos no tienen esa suerte: su nivel exterior está incompleto, y todo su comportamiento químico consiste en conseguir esa configuración completa. Esa tendencia se conoce como <strong>regla del octeto</strong>.")}</p>
<p>{t("There are two ways to get it, and they give the two kinds of bond the test checks.", "Hay dos maneras de conseguirlo, y de ahí salen los dos tipos de enlace que evalúa el examen.")}</p>
{svg_enlaces()}
{C.tabla(t("The three kinds of chemical bond: what happens to the electrons, which elements form it, and the properties of the result", "Comparación de los tres tipos de enlace químico según lo que ocurre con los electrones, los elementos que lo forman y las propiedades resultantes"),
 [t("Kind of bond", "Tipo de enlace"), t("What happens to the electrons", "Qué ocurre con los electrones"), t("Between which elements", "Entre qué elementos"), t("Properties of the result", "Propiedades del resultado")],
 [[t("Ionic", "Iónico"), t("They move from one atom to the other", "Se transfieren de un átomo al otro"), t("Metal + nonmetal", "Metal + no metal"), t("Hard, brittle solids with high melting points. Dissolved in water, they conduct electricity.", "Sólidos duros y quebradizos, de punto de fusión alto. Disueltos en agua conducen la electricidad.")],
  [t("Covalent", "Covalente"), t("They are shared by the two atoms", "Se comparten entre los dos átomos"), t("Nonmetal + nonmetal", "No metal + no metal"), t("Lower melting points. Usually they do not conduct electricity.", "Puntos de fusión más bajos. En general no conducen la electricidad.")],
  [t("Metallic", "Metálico"), t("They move freely among all the atoms", "Se mueven libremente entre todos los átomos"), t("Metal + metal", "Metal + metal"), t("Conduct heat and electricity well. Malleable: they bend without breaking.", "Conducen bien el calor y la electricidad. Son maleables: se deforman sin romperse.")]])}
{C.caja("tip", t("The practical rule", "La regla práctica"), "<p>" + t("Predicting the kind of bond takes no calculation: just find both elements in the table. If one is on the left (metal) and the other on the right (nonmetal), the bond is ionic. If both are on the right, covalent. If both are on the left, metallic. Position decides.", "Predecir el tipo de enlace no exige cálculo alguno: basta con localizar los dos elementos en la tabla. Si uno está a la izquierda (metal) y el otro a la derecha (no metal), el enlace será iónico. Si los dos están a la derecha, será covalente. Si los dos están a la izquierda, metálico. La posición decide.") + "</p>")}
{C.caja("ojo", t("Sharing does not mean sharing equally", "Compartir no significa repartir a partes iguales"), "<p>" + t("In many covalent bonds one atom pulls the shared electrons harder than the other, and the molecule ends up with one side a little more negative and the other a little more positive. That happens in water, and it explains properties studied in Lesson 5.2: why water dissolves so many substances and why its boiling point is so high for such a small molecule. Here, just recognize the bond as covalent.", "En muchos enlaces covalentes uno de los dos átomos atrae los electrones compartidos con más fuerza que el otro, y la molécula queda con un lado algo más negativo y otro algo más positivo. Eso ocurre en el agua, y explica propiedades que se estudiarán en la Lección 5.2: por qué el agua disuelve tantas sustancias y por qué su punto de ebullición es tan alto para una molécula tan pequeña. Aquí basta con reconocer el enlace como covalente.") + "</p>")}
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>Atom</strong>: from the Greek <em>á-tomos</em>, “uncut,” because it was thought to be the piece of matter that could not be split. The root {R('tom-')}, cut, appears again in <em>anatomy</em> and <em>tomography</em>. <strong>Isotope</strong>: from {R('iso-')}, equal, and <em>tópos</em>, place: “in the same place,” because all the isotopes of an element share one box of the table. The root {R('iso-')} already appeared in <em>isotonic</em>. <strong>Ion</strong> comes from the Greek <em>ión</em>, “going,” for how it moves toward the electrodes; hence <em>cation</em>, going to the cathode, and <em>anion</em>, going to the anode. <strong>Valence</strong> comes from the Latin <em>valere</em>, to be strong or worth, and means an atom’s ability to combine. <strong>Periodic</strong> does not refer to time but to regular repetition: properties come back every so many elements.", f"<strong>Átomo</strong>: del griego <em>á-tomos</em>, «sin división», porque se creyó que era la porción de materia que ya no podía partirse. La raíz {R('tom-')}, cortar, reaparece en <em>anatomía</em> y en <em>tomografía</em>. <strong>Isótopo</strong>: de {R('iso-')}, igual, y <em>tópos</em>, lugar: literalmente, «en el mismo lugar», porque todos los isótopos de un elemento ocupan la misma casilla de la tabla. La raíz {R('iso-')} ya apareció en <em>isotónico</em>. <strong>Ion</strong> procede del griego <em>ión</em>, «el que va», por su desplazamiento hacia los electrodos; de ahí <em>catión</em>, el que va hacia el cátodo, y <em>anión</em>, el que va hacia el ánodo. <strong>Valencia</strong> viene del latín <em>valere</em>, tener fuerza o valor, y designa la capacidad de combinación de un átomo. <strong>Periódico</strong>, en tabla periódica, no alude al tiempo sino a la repetición regular: las propiedades vuelven a aparecer cada cierto número de elementos.")}</p>
{P(t("Try it 5 · Magnesium and oxygen", "Pruebe 5 · Magnesio y oxígeno"), t("Magnesium is a metal and oxygen a nonmetal. The bond between them will be…", "El magnesio es un metal y el oxígeno un no metal. El enlace que forman entre sí será…"),
   [t("ionic", "iónico"), t("covalent", "covalente"), t("metallic", "metálico")], 0,
   {1: t("Covalent is nonmetal + nonmetal.", "Covalente es no metal + no metal."), 2: t("Metallic is metal + metal.", "Metálico es metal + metal.")}, t("Metal + nonmetal: the metal gives electrons, the nonmetal takes them.", "Metal + no metal: el metal cede electrones y el no metal los toma."))}
{P(t("Try it 6 · Noble gases", "Pruebe 6 · Gases nobles"), t("The noble gases in group 18 hardly form compounds because…", "Los gases nobles del grupo 18 casi no forman compuestos porque…"),
   [t("they are too heavy", "son demasiado pesados"), t("they have no electrons", "no tienen electrones"), t("their outer level is already full, so they need to gain or lose nothing", "su nivel exterior ya está completo y no necesitan ganar ni perder electrones")], 2,
   {0: t("Helium is very light and still does not react.", "El helio es muy ligero y tampoco reacciona."), 1: t("Every atom has electrons.", "Todo átomo tiene electrones.")}, t("Full outer level: nothing to gain.", "Nivel exterior completo: nada que ganar."))}
{C.enlace(N, anc("bonds", "enlaces"), t("ionic, covalent, or metallic?", "¿iónico, covalente o metálico?"), t("Pairs of elements: find them in the table and predict the bond.", "Parejas de elementos: localícelas en la tabla y prediga el enlace."))}
{C.enlace(N, anc("words", "palabras"), t("words of chemistry", "palabras de la química"), t("Atom, isotope, ion, valence: what the roots say.", "Átomo, isótopo, ion, valencia: lo que dicen las raíces."))}"""

    s5 = f"""<p>{t("A short science text written for this level. Notice what made the table convince the scientific community.", "Texto científico breve adaptado al nivel. Observe qué permitió a la tabla convencer a la comunidad científica.")}</p>
{C.lectura(t("An empty box and an element that did not yet exist", "Una casilla vacía y un elemento que aún no existía"),
 [t("Around 1869, the Russian chemist Dmitri Mendeleev put the known elements in order of increasing atomic mass and noticed that certain properties came back at regular intervals. When he placed elements with similar properties in the same column, the arrangement left several boxes empty.", "Hacia 1869, el químico ruso Dmitri Mendeléyev ordenó los elementos conocidos según su masa atómica creciente y observó que ciertas propiedades reaparecían de forma regular. Al colocar los elementos de propiedades semejantes en una misma columna, la disposición dejó varias casillas sin ocupar."),
  t("Mendeleev argued that those gaps belonged to elements not yet discovered. He went further: from the position of each empty box, he predicted the approximate atomic mass, density, and chemical behavior of the element that should fill it. For one of them, below aluminum, he predicted a mass close to 68 and a density near 5.9 grams per cubic centimeter.", "Mendeléyev sostuvo que esos huecos correspondían a elementos todavía no descubiertos. Fue más lejos: a partir de la posición de cada casilla vacía, predijo la masa atómica aproximada, la densidad y el comportamiento químico del elemento que debía ocuparla. Para uno de ellos, situado debajo del aluminio, anunció una masa cercana a 68 y una densidad próxima a 5.9 gramos por centímetro cúbico."),
  t("In 1875, a French chemist isolated a new element and named it gallium. Its mass turned out to be 69.7. The density he measured at first, 4.7, did not match the prediction; after purifying the sample better, the measurement was corrected to 5.9. The match with what had been predicted six years earlier greatly strengthened acceptance of the table.", "En 1875, un químico francés aisló un elemento nuevo y lo llamó galio. Su masa resultó ser 69.7. El valor de densidad que midió al principio, 4.7, no coincidía con la predicción; tras purificar mejor la muestra, la medición se corrigió a 5.9. La coincidencia con lo anunciado seis años antes reforzó considerablemente la aceptación de la tabla."),
  t("Mendeleev’s system did have problems: in a few cases, the order by mass had to be changed so that properties fit the right column. The explanation came decades later, when Henry Moseley showed that the ordering rule was not atomic mass but the number of protons. With the atomic number as the rule, the problems disappeared. Note that the table was useful and predictive for almost half a century before anyone knew why it worked.", "El sistema de Mendeléyev, sin embargo, presentaba anomalías: en unos pocos casos hubo que alterar el orden de masas para que las propiedades encajaran en la columna correcta. La explicación llegó décadas después, cuando Henry Moseley mostró que el criterio de ordenación no era la masa atómica, sino el número de protones. Con el número atómico como criterio, las anomalías desaparecieron. Conviene notar que la tabla resultó útil y predictiva durante casi medio siglo antes de que se conociera la razón por la que funcionaba.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Mendeleev discovered gallium in 1869.", "Mendeléyev descubrió el galio en 1869."), t("The table did not just order what was known: it predicted properties of undiscovered elements, and that ability proved it.", "La tabla no solo ordenaba lo conocido: permitía predecir propiedades de elementos aún no descubiertos, y esa capacidad la validó."), t("All atomic masses measured in the 1800s were wrong.", "Las masas atómicas medidas en el siglo XIX eran todas incorrectas.")], 1,
   {0: t("A French chemist found it in 1875.", "Lo aisló un químico francés en 1875."), 2: t("The text does not say that.", "El texto no dice eso.")}, t("Prediction, then confirmation.", "Predicción y, después, confirmación."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("The first density measurement of gallium did not match the prediction. According to the text, this was settled because…", "La primera medición de la densidad del galio no coincidía con la predicción. Según el texto, la discrepancia se resolvió porque…"),
   [t("Mendeleev changed his prediction to fit the data", "Mendeléyev modificó su predicción para ajustarla al dato"), t("density was ignored as a property", "se decidió ignorar la densidad como propiedad"), t("the sample was purified better, and the new measurement gave a different value", "se purificó mejor la muestra y la nueva medición dio un valor distinto")], 2,
   {0: t("The prediction stayed the same; the measurement changed.", "La predicción no cambió; cambió la medición."), 1: t("The text says the measurement was corrected.", "El texto dice que la medición se corrigió.")}, t("A purer sample gave 5.9.", "Una muestra más pura dio 5.9."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("The problems with ordering by atomic mass disappeared when…", "Las anomalías del orden por masa atómica desaparecieron cuando…"),
   [t("the elements were ordered by their number of protons", "se pasó a ordenar los elementos por su número de protones"), t("the problem elements were removed from the table", "se retiraron de la tabla los elementos problemáticos"), t("the noble gases were discovered", "se descubrieron los gases nobles")], 0,
   {1: t("Nothing was removed.", "No se retiró nada."), 2: t("The text does not say that.", "El texto no dice eso.")}, t("Moseley: the atomic number is the rule.", "Moseley: el criterio es el número atómico."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Which conclusion does the text support without going beyond it?", "¿Cuál de estas conclusiones se apoya en el texto sin ir más allá de lo que afirma?"),
   [t("Every scientific prediction comes true if you wait long enough.", "Toda predicción científica acaba confirmándose si se espera lo suficiente."), t("Atomic mass is useless in chemistry.", "La masa atómica no sirve para nada en química."), t("A classification system can be useful and predictive before anyone knows why it works.", "Un sistema de clasificación puede resultar útil y predictivo antes de que se conozca la causa de que funcione.")], 2,
   {0: t("“Every” goes far beyond one case.", "«Toda» va mucho más allá de un caso."), 1: t("The text never says that.", "El texto nunca dice eso.")}, t("Last sentence of the text.", "Última oración del texto."))}"""

    G = lambda *a: C.ged_item(P, *a)
    frag = {"tipo": "tabla", "encabezados": [t("Element", "Elemento"), t("Symbol", "Símbolo"), t("Atomic number", "Número atómico"), t("Group", "Grupo"), t("Period", "Periodo")],
            "filas": [[t("Lithium", "Litio"), "Li", "3", "1", "2"], [t("Sodium", "Sodio"), "Na", "11", "1", "3"], [t("Magnesium", "Magnesio"), "Mg", "12", "2", "3"], [t("Chlorine", "Cloro"), "Cl", "17", "17", "3"], [t("Potassium", "Potasio"), "K", "19", "1", "4"]]}
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK).", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SP.6.b", "1–2", t("<em>An atom of iron has 26 protons and a mass number of 56.</em><br>How many neutrons does it have, and how many electrons if it is neutral?", "<em>Un átomo de hierro tiene 26 protones y número másico 56.</em><br>¿Cuántos neutrones tiene, y cuántos electrones si es neutro?"),
   [t("30 neutrons, 26 electrons", "30 neutrones, 26 electrones"), t("26 neutrons, 30 electrons", "26 neutrones, 30 electrones"), t("56 neutrons, 26 electrons", "56 neutrones, 26 electrones"), t("30 neutrons, 56 electrons", "30 neutrones, 56 electrones")], 0,
   {1: t("Neutral: electrons = protons.", "Neutro: electrones = protones."), 2: t("56 is protons + neutrons.", "56 son protones + neutrones."), 3: t("Electrons match protons, not the mass number.", "Los electrones igualan a los protones, no al número másico.")},
   t("56 − 26 = 30 neutrons; neutral, so 26 electrons.", "56 − 26 = 30 neutrones; neutro, así que 26 electrones."))}
{G(2, "SP.1.c", "2", t("<em>Part of the periodic table:</em>", "<em>Fragmento de la tabla periódica:</em>") + C.grafica(frag, t("Data table", "Tabla de datos")) + t("Which element will react most like sodium?", "¿Qué elemento reaccionará de manera más parecida al sodio?"),
   [t("Potassium", "El potasio"), t("Magnesium", "El magnesio"), t("Chlorine", "El cloro"), t("None of them", "Ninguno")], 0,
   {1: t("Magnesium is in the same period, but group 2.", "El magnesio está en el mismo periodo, pero en el grupo 2."), 2: t("Chlorine is in group 17: it behaves very differently.", "El cloro está en el grupo 17: se comporta de forma muy distinta."), 3: t("Look for the same group.", "Busque el mismo grupo.")},
   t("Potassium (and lithium) are in group 1 with sodium: one valence electron each.", "El potasio (y el litio) están en el grupo 1 con el sodio: un electrón de valencia cada uno."))}
{G(3, "SP.3.c", "2", t("<em>Calcium is in group 2. It tends to lose its valence electrons when it reacts.</em><br>What ion will calcium most likely form?", "<em>El calcio está en el grupo 2. Al reaccionar tiende a perder sus electrones de valencia.</em><br>¿Qué ion es más probable que forme el calcio?"),
   ["Ca²⁺", "Ca²⁻", "Ca⁺", "Ca⁶⁻"], 0,
   {1: t("Losing electrons gives a positive charge.", "Perder electrones da carga positiva."), 2: t("Group 2 has two valence electrons, not one.", "El grupo 2 tiene dos electrones de valencia, no uno."), 3: t("It loses electrons; it does not gain six.", "Pierde electrones; no gana seis.")},
   t("Two valence electrons lost: 2+. Lose negative, end up positive.", "Pierde dos electrones de valencia: 2+. Pierde negativo, queda positivo."))}
{G(4, "SP.7.a", "2–3", t("<em>Sodium chloride (table salt) has a melting point of 801 °C and conducts electricity when dissolved in water. Sugar melts at about 186 °C and does not conduct electricity in water.</em><br>Which explanation fits the bonding model?", "<em>El cloruro de sodio (sal común) funde a 801 °C y conduce la electricidad disuelto en agua. El azúcar funde a unos 186 °C y no conduce la electricidad en agua.</em><br>¿Qué explicación encaja con el modelo del enlace?"),
   [t("Salt has ionic bonds; sugar has covalent bonds.", "La sal tiene enlaces iónicos; el azúcar, enlaces covalentes."), t("Both have ionic bonds.", "Los dos tienen enlaces iónicos."), t("Salt has covalent bonds; sugar has ionic bonds.", "La sal tiene enlaces covalentes; el azúcar, iónicos."), t("Both have metallic bonds.", "Los dos tienen enlaces metálicos.")], 0,
   {1: t("Sugar does not conduct and melts low: not ionic.", "El azúcar no conduce y funde bajo: no es iónico."), 2: t("That is backward.", "Es al revés."), 3: t("Neither is a metal.", "Ninguno es un metal.")},
   t("High melting point + conducts in water = ionic. Lower melting point + no conduction = covalent.", "Punto de fusión alto + conduce en agua = iónico. Punto de fusión bajo + no conduce = covalente."))}
{G(5, "SP.4.a", "2–3", t("<em>Read “An empty box and an element that did not yet exist” in section 5.</em><br>Which piece of evidence most strongly supported Mendeleev’s table?", "<em>Lea «Una casilla vacía y un elemento que aún no existía» de la sección 5.</em><br>¿Qué evidencia apoyó con más fuerza la tabla de Mendeléyev?"),
   [t("Gallium was found with the mass and density he had predicted for an empty box.", "Se halló el galio con la masa y la densidad que él había predicho para una casilla vacía."), t("He ordered the elements by atomic mass.", "Ordenó los elementos por su masa atómica."), t("The first density measurement of gallium was 4.7.", "La primera medición de la densidad del galio fue 4.7."), t("Some elements had to be moved out of mass order.", "Algunos elementos tuvieron que salir del orden de masas.")], 0,
   {1: t("That is how he built it, not evidence for it.", "Así la construyó; no es evidencia a favor."), 2: t("That value did not match.", "Ese valor no coincidía."), 3: t("That was a problem for the table.", "Eso fue un problema para la tabla.")},
   t("A prediction made before the discovery, then confirmed: strong evidence.", "Una predicción hecha antes del descubrimiento y confirmada después: evidencia fuerte."))}"""

    secciones = [
        ("s1", t("The atom and its three particles", "El átomo y sus tres partículas"), s1),
        ("s2", t("Isotopes and ions: two different changes", "Isótopos e iones: dos cambios que no se parecen"), s2),
        ("s3", t("The periodic table as a tool for prediction", "La tabla periódica como documento predictivo"), s3),
        ("s4", t("Why atoms join: the chemical bond", "Por qué se unen los átomos: el enlace químico"), s4),
        ("s5", t("Science reading", "Lectura científica"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Ten atoms.", "Diez átomos."), t("Find protons, neutrons, and electrons for ten atoms from their atomic and mass numbers, including two ions.", "Calcule protones, neutrones y electrones de diez átomos a partir del número atómico y del número másico, incluidos dos iones.")),
        (t("Five pairs.", "Cinco parejas."), t("Predict the kind of bond for five pairs of elements, and justify each one with their positions in the table.", "Prediga el tipo de enlace de cinco parejas de elementos y justifique cada una con su posición en la tabla.")),
        (t("In your own words.", "Con sus palabras."), t("Write a short paragraph explaining the difference between an isotope and an ion.", "Escriba un párrafo breve que explique la diferencia entre un isótopo y un ion.")),
    ]
    Q = t
    quiz = [
        (Q("The positively charged particle in the nucleus is…", "La partícula con carga positiva que se encuentra en el núcleo es…"), [Q("the electron", "el electrón"), Q("the proton", "el protón"), Q("the neutron", "el neutrón"), Q("the ion", "el ion")], 1, {0: Q("Electrons are negative and outside.", "Los electrones son negativos y están fuera."), 2: Q("Neutrons have no charge.", "Los neutrones no tienen carga."), 3: Q("An ion is a whole atom.", "Un ion es un átomo completo.")}, Q("Proton: +, in the nucleus.", "Protón: +, en el núcleo.")),
        (Q("An atom has atomic number 16 and mass number 32. How many neutrons does it have?", "Un átomo tiene número atómico 16 y número másico 32. ¿Cuántos neutrones tiene?"), ["32", "48", "16", "8"], 2, {0: Q("That is the mass number.", "Ese es el número másico."), 1: Q("Subtract, do not add.", "Reste, no sume."), 3: Q("32 − 16 is not 8.", "32 − 16 no es 8.")}, Q("32 − 16 = 16.", "32 − 16 = 16.")),
        (Q("Almost all the mass of an atom is in…", "Casi toda la masa de un átomo se concentra en…"), [Q("the nucleus", "el núcleo"), Q("the first energy level", "el primer nivel de energía"), Q("the outer level", "el nivel exterior"), Q("the valence electrons", "los electrones de valencia")], 0, {1: Q("Levels hold electrons, which are very light.", "Los niveles tienen electrones, muy ligeros."), 2: Q("Electrons are very light.", "Los electrones son muy ligeros."), 3: Q("Electrons are very light.", "Los electrones son muy ligeros.")}, Q("Protons and neutrons are in the nucleus.", "Protones y neutrones están en el núcleo.")),
        (Q("A neutral nitrogen atom has atomic number 7. Its number of electrons is…", "Un átomo neutro de nitrógeno tiene número atómico 7. Su número de electrones es…"), ["14", "7", "0", Q("It depends on the mass number", "Depende del número másico")], 1, {0: Q("That is the mass number.", "Ese es el número másico."), 2: Q("Every atom has electrons.", "Todo átomo tiene electrones."), 3: Q("Neutral: electrons = protons.", "Neutro: electrones = protones.")}, Q("Neutral: 7 electrons for 7 protons.", "Neutro: 7 electrones para 7 protones.")),
        (Q("In the periodic table, the vertical columns are called…", "En la tabla periódica, las columnas verticales se llaman…"), [Q("periods", "periodos"), Q("levels", "niveles"), Q("groups", "grupos"), Q("series", "series")], 2, {0: Q("Periods are rows.", "Los periodos son filas."), 1: Q("Levels are in the atom.", "Los niveles están en el átomo."), 3: Q("Not the term used.", "No es el término.")}, Q("Columns = groups.", "Columnas = grupos.")),
        (Q("Two elements in the same group have the same…", "Dos elementos situados en el mismo grupo tienen en común…"), [Q("number of protons", "el mismo número de protones"), Q("mass number", "el mismo número másico"), Q("number of energy levels", "el mismo número de niveles de energía"), Q("number of valence electrons", "el mismo número de electrones de valencia")], 3, {0: Q("Then they would be the same element.", "Entonces serían el mismo elemento."), 1: Q("Masses differ down a column.", "Las masas cambian en la columna."), 2: Q("That is the period.", "Eso es el periodo.")}, Q("Same column, same valence electrons.", "Misma columna, mismos electrones de valencia.")),
        (Q("An element is in period 3. Its atoms have…", "Un elemento está en el periodo 3. Eso significa que sus átomos tienen…"), [Q("3 energy levels in use", "3 niveles de energía ocupados"), Q("3 protons", "3 protones"), Q("3 valence electrons", "3 electrones de valencia"), Q("3 neutrons", "3 neutrones")], 0, {1: Q("Protons are the atomic number.", "Los protones son el número atómico."), 2: Q("That is the group.", "Eso es el grupo."), 3: Q("Not from the period.", "No sale del periodo.")}, Q("Period = number of levels.", "Periodo = número de niveles.")),
        (Q("Elements in group 18 hardly react because…", "Los elementos del grupo 18 casi no reaccionan porque…"), [Q("they have no electrons", "no tienen electrones"), Q("their outer level is already full", "su nivel exterior ya está completo"), Q("they are the heaviest in the table", "son los más pesados de la tabla"), Q("they lose electrons very easily", "pierden electrones con mucha facilidad")], 1, {0: Q("They do.", "Sí tienen."), 2: Q("Helium is very light.", "El helio es muy ligero."), 3: Q("That would make them react.", "Eso los haría reaccionar.")}, Q("Octet complete.", "Octeto completo.")),
        (Q("Carbon-12 and carbon-14 are the same element because they have…", "El carbono-12 y el carbono-14 son el mismo elemento porque…"), [Q("the same number of neutrons", "tienen el mismo número de neutrones"), Q("the same mass", "tienen la misma masa"), Q("the same number of protons", "tienen el mismo número de protones"), Q("different columns in the table", "ocupan columnas distintas de la tabla")], 2, {0: Q("They differ in neutrons.", "Difieren en neutrones."), 1: Q("12 and 14 are different masses.", "12 y 14 son masas distintas."), 3: Q("Isotopes share one box.", "Los isótopos comparten casilla.")}, Q("6 protons both: carbon.", "6 protones los dos: carbono.")),
        (Q("The ion Ca²⁺ comes from a calcium atom with atomic number 20. This ion has…", "El ion Ca²⁺ procede de un átomo de calcio de número atómico 20. Ese ion tiene…"), [Q("20 protons and 18 electrons", "20 protones y 18 electrones"), Q("18 protons and 20 electrons", "18 protones y 20 electrones"), Q("22 protons and 20 electrons", "22 protones y 20 electrones"), Q("20 protons and 22 electrons", "20 protones y 22 electrones")], 0, {1: Q("Protons never change.", "Los protones no cambian."), 2: Q("Protons never change.", "Los protones no cambian."), 3: Q("2+ means it lost two electrons.", "2+ significa que perdió dos electrones.")}, Q("20 protons; 20 − 2 = 18 electrons.", "20 protones; 20 − 2 = 18 electrones.")),
        (Q("A metal and a nonmetal combine. The bond is…", "Un metal y un no metal se combinan entre sí. El enlace que se forma es…"), [Q("covalent", "covalente"), Q("metallic", "metálico"), Q("ionic", "iónico"), Q("no bond forms", "no se forma ningún enlace")], 2, {0: Q("Covalent is nonmetal + nonmetal.", "Covalente es no metal + no metal."), 1: Q("Metallic is metal + metal.", "Metálico es metal + metal."), 3: Q("They do combine.", "Sí se combinan.")}, Q("Metal + nonmetal: ionic.", "Metal + no metal: iónico.")),
        (Q("The key difference between ionic and covalent bonds is that…", "La diferencia esencial entre el enlace iónico y el covalente es que…"), [Q("in ionic bonds electrons are transferred, and in covalent bonds they are shared", "en el iónico los electrones se transfieren y en el covalente se comparten"), Q("ionic bonds involve neutrons and covalent bonds protons", "en el iónico intervienen neutrones y en el covalente protones"), Q("ionic bonds happen only between noble gases", "el iónico solo ocurre entre gases nobles"), Q("covalent bonds change the atomic number", "el covalente cambia el número atómico de los átomos")], 0, {1: Q("Bonds are about electrons.", "Los enlaces son cosa de electrones."), 2: Q("Noble gases hardly bond.", "Los gases nobles casi no forman enlaces."), 3: Q("Bonds never change protons.", "Los enlaces no cambian los protones.")}, Q("Transfer vs. share.", "Transferir frente a compartir.")),
    ]
    filas = [
        (t("Count protons, neutrons, and electrons", "Calcula protones, neutrones y electrones"), t("I do it for neutral atoms and for ions, changing only the electrons.", "Lo hago en átomos neutros y en iones, ajustando solo los electrones."), t("I get the protons but subtract the neutrons wrong.", "Obtengo los protones, pero me equivoco al restar los neutrones."), t("I mix up atomic number and mass number.", "Confundo el número atómico con el número másico.")),
        (t("Predict from the position in the table", "Deduce propiedades por la posición en la tabla"), t("I get valence electrons and levels from group and period, and say which elements behave alike.", "Deduzco electrones de valencia y niveles a partir de grupo y periodo, y digo qué elementos se comportan igual."), t("I find the element but do not link group and valence electrons.", "Localizo el elemento, pero no relaciono grupo y electrones de valencia."), t("I try to remember properties instead of using the table.", "Busco las propiedades de memoria, sin usar la tabla.")),
        (t("Tell isotope from ion", "Distingue isótopo de ion"), t("I explain which particle changes in each and why neither changes the element.", "Explico qué partícula cambia en cada uno y por qué ninguno cambia el elemento."), t("I know they differ but not which particle changes.", "Sé que son distintos, pero no qué partícula cambia."), t("I use the two words as if they meant the same.", "Uso los dos términos como equivalentes.")),
        (t("Predict the kind of bond", "Predice el tipo de enlace"), t("I predict it from the positions and link it to the properties of the compound.", "Lo predigo por la posición y lo relaciono con las propiedades del compuesto."), t("I get some right but cannot explain how.", "Acierto en algunos casos, pero no explico el criterio."), t("I guess.", "Adivino.")),
    ]
    cierre = "<p>" + t("This lesson worked on the single atom: its particles, its place in the table, and why it joins others. Lesson 5.2 goes one step up and looks at what happens when those atoms and molecules come together in large numbers: states of matter, density, and solutions.", "Esta lección ha trabajado en el nivel del átomo aislado: sus partículas, su posición en la tabla y la razón por la que se une a otros. La Lección 5.2 sube un escalón y observa lo que ocurre cuando esos átomos y esas moléculas se encuentran en cantidad: los estados de la materia, la densidad y las disoluciones.") + "</p><p>" + \
             t("The link between the two is direct. The covalent and uneven bond in water, only named here, will explain in 5.2 why water dissolves so many substances. And a warning: 5.2 asks you to rearrange a formula, the one for density, to find the mass or the volume. That is where Math Level 3 fully enters the science course.", "El enlace entre ambas lecciones es directo. El carácter covalente y desigual del enlace del agua, que aquí solo se ha nombrado, será en la 5.2 la explicación de por qué el agua disuelve tantas sustancias. Y conviene avisar de algo: la 5.2 exige despejar una fórmula, la de la densidad, para hallar la masa o el volumen. Es el punto donde el Nivel 3 de Matemáticas entra de lleno en el curso de Ciencias.") + "</p>"
    glosario = [
        (t("Proton / neutron / electron", "Protón / neutrón / electrón"), t("Positive particle in the nucleus / neutral particle in the nucleus / negative particle outside it.", "Partícula positiva del núcleo / neutra del núcleo / negativa fuera de él.")),
        (t("Atomic number (Z)", "Número atómico (Z)"), t("The number of protons; it identifies the element.", "Número de protones; identifica al elemento.")),
        (t("Mass number (A)", "Número másico (A)"), t("Protons plus neutrons.", "Protones más neutrones.")),
        (t("Isotope", "Isótopo"), t("An atom of the same element with a different number of neutrons.", "Átomo del mismo elemento con distinto número de neutrones.")),
        (t("Ion (cation / anion)", "Ion (catión / anión)"), t("An atom that has lost electrons (positive) or gained them (negative).", "Átomo que ha perdido electrones (positivo) o los ha ganado (negativo).")),
        (t("Group / period", "Grupo / periodo"), t("Column / row of the periodic table.", "Columna / fila de la tabla periódica.")),
        (t("Valence electrons", "Electrones de valencia"), t("The electrons in the outer level, which take part in bonds.", "Electrones del nivel exterior, que participan en los enlaces.")),
        (t("Octet rule", "Regla del octeto"), t("Atoms tend to reach eight electrons in their outer level.", "Los átomos tienden a completar ocho electrones en su nivel exterior.")),
        (t("Ionic / covalent / metallic bond", "Enlace iónico / covalente / metálico"), t("Electrons transferred / shared / moving freely among metal atoms.", "Electrones transferidos / compartidos / libres entre átomos metálicos.")),
    ]
    estd = C.estandares(["SP.6.b", "SP.1.c", "SP.3.c", "SP.7.a"], ["P.c"], base=["SP.4.a"])
    conexion = "<p>" + t("A new area starts. The four earlier topics covered life science. This one opens the second big area of the test, physical science, and it starts where it should: with the smallest unit that keeps the identity of a substance.", "Cambio de dominio. Los cuatro temas anteriores recorrieron las Ciencias de la vida. Este abre el segundo gran dominio del examen, el de las Ciencias físicas, y lo hace por donde corresponde: por la unidad más pequeña que conserva la identidad de una sustancia.") + "</p><p>" + \
               t("The content changes, but not the tools. You will still need the scientific notation of Lesson 2.1, the table reading of 2.2 (the periodic table is first of all a data table), and the habit from 4.3 of separating what a piece of data supports from what it does not.", "Cambia el contenido, pero no las herramientas. Seguirá haciendo falta la notación científica de la Lección 2.1, la lectura de tablas de la 2.2 —la tabla periódica es antes que nada una tabla de datos— y el hábito de la 4.3 de separar lo que un dato sostiene de lo que no.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> use the periodic table as a document to look things up in, not as a list to memorize. You do not need to learn symbols or atomic masses by heart: what you practice is getting information from a table that you will always have in front of you.", "<strong>Cómo estudiar esta lección:</strong> use la tabla periódica como un documento para consultar, no como una lista para memorizar. No hace falta aprender de memoria símbolos ni masas atómicas: lo que se practica es extraer información de una tabla que siempre tendrá a la vista.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Three particles, one table that predicts, and two ways for atoms to join.", "Tres partículas, una tabla que predice y dos maneras de unirse los átomos."),
        ["SP.6 · " + t("Expressing science information", "Expresar información científica"), "SP.1 · " + t("Understanding science texts", "Comprender textos científicos")],
        [t("<strong>Identify</strong> protons, neutrons, and electrons, with the charge and place of each.", "<strong>Identificar</strong> protones, neutrones y electrones, y describir la carga y la posición de cada uno."),
         t("<strong>Calculate</strong> the atomic number, the mass number, and the number of neutrons.", "<strong>Calcular</strong> el número atómico, el número másico y el número de neutrones de un átomo."),
         t("<strong>Tell</strong> an isotope from an ion and say which particle changes in each.", "<strong>Distinguir</strong> un isótopo de un ion y explicar qué partícula cambia en cada caso."),
         t("<strong>Find</strong> an element in the periodic table and predict its properties from its group and period.", "<strong>Localizar</strong> un elemento en la tabla periódica y deducir propiedades a partir de su grupo y su periodo."),
         t("<strong>Predict</strong> whether two elements will form an ionic or covalent bond, and justify it.", "<strong>Predecir</strong> si dos elementos formarán un enlace iónico o covalente, y justificar la predicción.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("5-2", t("States of matter, density, and solutions", "Estados de la materia, densidad y disoluciones")), glosario, P)


# ---------------------------------------------------------------- práctica
def js_contar():
    E = [[z, s, (n_en if C.L == "en" else n_es), a] for z, s, n_en, n_es, a, *_ in ELEM]
    if C.L == "en":
        tx = {"atomo": "An atom of <strong>{n}</strong> ({s}) has atomic number <strong>{z}</strong> and mass number <strong>{a}</strong>. It is neutral.",
              "ion": "The ion <strong>{ion}</strong> comes from {n}, atomic number <strong>{z}</strong>.",
              "q": {"p": "How many <strong>protons</strong>?", "n": "How many <strong>neutrons</strong>?", "e": "How many <strong>electrons</strong>?"},
              "sp": "Protons = atomic number = {z}.", "sn": "Neutrons = mass number − atomic number = {a} − {z} = {r}.", "se": "Neutral atom: electrons = protons = {z}.",
              "sie": "{z} protons; the charge {c} means it {gp} {k} {el}: {z} {op} {k} = {r}.", "lost": "lost", "gained": "gained",
              "g": "Protons = atomic number. Neutrons = mass number − atomic number. Electrons: same as protons if neutral; adjust by the charge if it is an ion."}
    else:
        tx = {"atomo": "Un átomo de <strong>{n}</strong> ({s}) tiene número atómico <strong>{z}</strong> y número másico <strong>{a}</strong>. Es neutro.",
              "ion": "El ion <strong>{ion}</strong> procede del {n}, de número atómico <strong>{z}</strong>.",
              "q": {"p": "¿Cuántos <strong>protones</strong> tiene?", "n": "¿Cuántos <strong>neutrones</strong> tiene?", "e": "¿Cuántos <strong>electrones</strong> tiene?"},
              "sp": "Protones = número atómico = {z}.", "sn": "Neutrones = número másico − número atómico = {a} − {z} = {r}.", "se": "Átomo neutro: electrones = protones = {z}.",
              "sie": "{z} protones; la carga {c} indica que {gp} {k} {el}: {z} {op} {k} = {r}.", "lost": "perdió", "gained": "ganó",
              "g": "Protones = número atómico. Neutrones = número másico − número atómico. Electrones: los mismos que protones si es neutro; ajuste por la carga si es un ion."}
    return f"""
var EL = {json.dumps(E, ensure_ascii=False)}, IO = {json.dumps(IONES)}, TC = {json.dumps(tx, ensure_ascii=False)};
var SUP = {{"1":"¹","2":"²","3":"³"}};
function fm(s, o){{ return s.replace(/\\{{(\\w+)\\}}/g, function(_, k){{ return o[k]; }}); }}
function gA(){{
  var r, enun, sol;
  if (aleatorio(1, 3) < 3){{
    var e = elige(EL), q = elige(["p", "n", "e"]), o = {{z: e[0], s: e[1], n: e[2], a: e[3]}};
    r = q === "p" ? e[0] : q === "n" ? e[3] - e[0] : e[0]; o.r = r;
    enun = "<p>" + fm(TC.atomo, o) + "</p><p>" + TC.q[q] + "</p>";
    sol = fm(q === "p" ? TC.sp : q === "n" ? TC.sn : TC.se, o);
  }} else {{
    var io = elige(IO), e = EL.filter(function(x){{ return x[1] === io[0]; }})[0], c = io[1], k = Math.abs(c);
    var sim = io[0] + (k > 1 ? SUP[k] : "") + (c > 0 ? "⁺" : "⁻");
    r = e[0] - c;
    var o = {{ion: sim, z: e[0], n: e[2], c: k + (c > 0 ? "+" : "−"), gp: c > 0 ? TC.lost : TC.gained, k: k, el: k > 1 ? {json.dumps(t("electrons", "electrones"))} : {json.dumps(t("electron", "electrón"))}, op: c > 0 ? "−" : "+", r: r}};
    enun = "<p>" + fm(TC.ion, o) + "</p><p>" + TC.q.e + "</p>";
    sol = fm(TC.sie, o);
  }}
  return {{enun: enun, solucion: sol, evalua: numN(r, [], TC.g)}};
}}
"""


def banco_isotopo_ion():
    O = [t("Isotopes of the same element", "Isótopos del mismo elemento"), t("An atom and its ion", "Un átomo y su ion"), t("Two different elements", "Dos elementos distintos")]
    d = [
        (t("Atom 1: 17 protons, 18 neutrons, 17 electrons. Atom 2: 17 protons, 20 neutrons, 17 electrons.", "Átomo 1: 17 protones, 18 neutrones, 17 electrones. Átomo 2: 17 protones, 20 neutrones, 17 electrones."), 0, t("Same protons, different neutrons.", "Mismos protones, distintos neutrones.")),
        (t("Atom 1: 11 protons, 12 neutrons, 11 electrons. Atom 2: 11 protons, 12 neutrons, 10 electrons.", "Átomo 1: 11 protones, 12 neutrones, 11 electrones. Átomo 2: 11 protones, 12 neutrones, 10 electrones."), 1, t("Only the electrons changed: Na⁺.", "Solo cambiaron los electrones: Na⁺.")),
        (t("Atom 1: 6 protons, 6 neutrons. Atom 2: 7 protons, 7 neutrons.", "Átomo 1: 6 protones, 6 neutrones. Átomo 2: 7 protones, 7 neutrones."), 2, t("Different protons: carbon and nitrogen.", "Distintos protones: carbono y nitrógeno.")),
        (t("Uranium-235 and uranium-238.", "El uranio-235 y el uranio-238."), 0, t("Same element, different mass numbers.", "Mismo elemento, distinto número másico.")),
        (t("O and O²⁻.", "O y O²⁻."), 1, t("Oxygen gained two electrons.", "El oxígeno ganó dos electrones.")),
        (t("Atom 1: 19 protons, 20 neutrons. Atom 2: 20 protons, 20 neutrons.", "Átomo 1: 19 protones, 20 neutrones. Átomo 2: 20 protones, 20 neutrones."), 2, t("Same neutrons does not matter: protons differ (potassium and calcium).", "Que tengan los mismos neutrones no importa: los protones difieren (potasio y calcio).")),
        (t("Hydrogen-1 and hydrogen-2 (deuterium).", "El hidrógeno-1 y el hidrógeno-2 (deuterio)."), 0, t("Deuterium has one extra neutron.", "El deuterio tiene un neutrón más.")),
    ]
    out = [{"enun": t("What are these two?", "¿Qué son estos dos?") + f"<br><strong>{x}</strong>", "ops": O, "ok": k, "enOrden": True, "pista": t("Compare protons first, then neutrons, then electrons.", "Compare primero los protones, después los neutrones y por último los electrones."), "exp": f"<strong>{O[k]}.</strong> {e}"} for x, k, e in d]
    extra = [
        (t("An atom loses one electron. Its mass…", "Un átomo pierde un electrón. Su masa…"), [t("barely changes", "casi no cambia"), t("drops by one unit", "baja una unidad"), t("doubles", "se duplica")], 0, t("Electrons are about 1,800 times lighter than a proton.", "El electrón es unas 1,800 veces más ligero que un protón.")),
        (t("An atom gains one neutron. Its charge…", "Un átomo gana un neutrón. Su carga…"), [t("does not change", "no cambia"), t("becomes positive", "se vuelve positiva"), t("becomes negative", "se vuelve negativa")], 0, t("Neutrons have no charge.", "Los neutrones no tienen carga.")),
        (t("A positive ion is positive because it…", "Un ion positivo es positivo porque…"), [t("lost electrons", "perdió electrones"), t("gained protons", "ganó protones"), t("gained electrons", "ganó electrones")], 0, t("Lose negative, end up positive.", "Pierde negativo, queda positivo.")),
    ]
    out += [{"enun": q, "ops": o, "ok": k, "pista": t("Which particle changed?", "¿Qué partícula cambió?"), "exp": e} for q, o, k, e in extra]
    return out


def banco_tabla():
    out = []
    val = lambda g: g if g <= 2 else g - 10
    nom = {s: t(ne, ns) for _, s, ne, ns, *_ in ELEM}
    for z, s, ne, ns, a, g, p, tipo in ELEM:
        if g in range(3, 13) or s == "He":
            continue
        n = t(ne, ns)
        v = val(g)
        ops = [str(v), str(p), str(g) if g != v else str(v + 1), str(8 - v) if 8 - v != v else str(v + 2)]
        if len(set(ops)) < 4:
            ops = [str(v)] + [str(x) for x in (v + 1, v + 2, v + 3)]
        out.append({"enun": t(f"<strong>{n.capitalize()}</strong> ({s}) is in group {g}, period {p}. How many <strong>valence electrons</strong> does it have?", f"El <strong>{n}</strong> ({s}) está en el grupo {g}, periodo {p}. ¿Cuántos <strong>electrones de valencia</strong> tiene?"),
                    "ops": ops, "ok": 0,
                    "pista": t("Groups 1 and 2: 1 and 2. Groups 13 to 18: subtract 10.", "Grupos 1 y 2: 1 y 2. Grupos 13 a 18: reste 10."),
                    "exp": t(f"Group {g} → {v} valence electrons. The period ({p}) is the number of levels.", f"Grupo {g} → {v} electrones de valencia. El periodo ({p}) es el número de niveles.")})
    fam = [("Li", ["Na", "Be", "C"]), ("F", ["Cl", "O", "Ne"]), ("Mg", ["Ca", "Na", "Al"]), ("O", ["S", "N", "F"]), ("Ne", ["Ar", "F", "Na"]), ("K", ["Na", "Ca", "Ar"])]
    for s, (ok, *otros) in fam:
        nm = lambda x: nom.get(x, {"Be": t("beryllium", "berilio")}.get(x, x))
        out.append({"enun": t(f"Which element behaves most like <strong>{nm(s)}</strong> ({s})?", f"¿Qué elemento se comporta de forma más parecida al <strong>{nm(s)}</strong> ({s})?"),
                    "ops": [f"{nm(x)} ({x})" for x in [ok] + otros], "ok": 0, "pista": t("Look in the same column, not the same row.", "Busque en la misma columna, no en la misma fila."),
                    "exp": t(f"{nm(ok).capitalize()} is in the same group.", f"El {nm(ok)} está en el mismo grupo.")})
    out += [
        {"enun": t("An element in group 1 will most likely form an ion with charge…", "Un elemento del grupo 1 formará probablemente un ion de carga…"), "ops": ["1+", "1−", "2+", "7−"], "ok": 0, "pista": t("Metals on the left lose their valence electrons.", "Los metales de la izquierda pierden sus electrones de valencia."), "exp": t("It loses its one valence electron: 1+.", "Pierde su único electrón de valencia: 1+.")},
        {"enun": t("An element in group 17 will most likely form an ion with charge…", "Un elemento del grupo 17 formará probablemente un ion de carga…"), "ops": ["1−", "7+", "1+", "17−"], "ok": 0, "pista": t("It is one electron short of eight.", "Le falta un electrón para ocho."), "exp": t("It gains one electron: 1−.", "Gana un electrón: 1−.")},
        {"enun": t("An element in group 16 will most likely form an ion with charge…", "Un elemento del grupo 16 formará probablemente un ion de carga…"), "ops": ["2−", "6+", "2+", "16−"], "ok": 0, "pista": t("6 valence electrons: how many short of eight?", "6 electrones de valencia: ¿cuántos le faltan para ocho?"), "exp": t("It gains two electrons: 2−.", "Gana dos electrones: 2−.")},
        {"enun": t("An element is in period 5. How many energy levels do its atoms use?", "Un elemento está en el periodo 5. ¿Cuántos niveles de energía usan sus átomos?"), "ops": ["5", "8", "2", "18"], "ok": 0, "pista": t("Period = levels.", "Periodo = niveles."), "exp": t("Period 5 → 5 levels.", "Periodo 5 → 5 niveles.")},
    ]
    return out


def clasif_enlaces():
    G = [t("Ionic (metal + nonmetal)", "Iónico (metal + no metal)"), t("Covalent (nonmetal + nonmetal)", "Covalente (no metal + no metal)"), t("Metallic (metal + metal)", "Metálico (metal + metal)")]
    P = [t("One on the left, one on the right of the table?", "¿Uno a la izquierda y otro a la derecha de la tabla?"), t("Both on the right?", "¿Los dos a la derecha?"), t("Both metals?", "¿Los dos metales?")]
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("Predict the kind of bond for each pair.", "Prediga el tipo de enlace de cada pareja."), "grupos": G, "etiqueta": t("Bond:", "Enlace:"),
                "piezas": [{"t": a, "v": v, "pista": P[v]} for a, v in piezas], "extra": t("Position decides: left = metals, right = nonmetals.", "La posición decide: izquierda = metales, derecha = no metales.")}
    return [
        item(t("Set 1", "Grupo 1"), [(t("Sodium (Na) and chlorine (Cl): table salt", "Sodio (Na) y cloro (Cl): sal común"), 0), (t("Hydrogen (H) and oxygen (O): water", "Hidrógeno (H) y oxígeno (O): agua"), 1), (t("Copper (Cu) and zinc (Zn): brass", "Cobre (Cu) y cinc (Zn): latón"), 2), (t("Carbon (C) and oxygen (O): carbon dioxide", "Carbono (C) y oxígeno (O): dióxido de carbono"), 1), (t("Magnesium (Mg) and oxygen (O)", "Magnesio (Mg) y oxígeno (O)"), 0)]),
        item(t("Set 2", "Grupo 2"), [(t("Calcium (Ca) and chlorine (Cl)", "Calcio (Ca) y cloro (Cl)"), 0), (t("Nitrogen (N) and hydrogen (H): ammonia", "Nitrógeno (N) e hidrógeno (H): amoníaco"), 1), (t("Iron (Fe) alone, in a nail", "Hierro (Fe) solo, en un clavo"), 2), (t("Potassium (K) and iodine (I)", "Potasio (K) y yodo (I)"), 0), (t("Carbon (C) and hydrogen (H): methane", "Carbono (C) e hidrógeno (H): metano"), 1)]),
    ]


def banco_palabras():
    d = [
        (t("<em>Atom</em> comes from <em>á-tomos</em>, which means…", "<em>Átomo</em> viene de <em>á-tomos</em>, que significa…"), [t("uncut, cannot be split", "sin división, que no se puede partir"), t("very small", "muy pequeño"), t("heavy", "pesado")], 0, t("The root tom-, cut, also appears in anatomy.", "La raíz tom-, cortar, aparece también en anatomía.")),
        (t("<em>Isotope</em>: iso- (equal) + tópos (place). Isotopes are “in the same place” because…", "<em>Isótopo</em>: iso- (igual) + tópos (lugar). Los isótopos están «en el mismo lugar» porque…"), [t("they share one box of the periodic table", "comparten una casilla de la tabla periódica"), t("they are in the same rock", "están en la misma roca"), t("they have the same mass", "tienen la misma masa")], 0, t("Same element, same box.", "Mismo elemento, misma casilla.")),
        (t("A <em>cation</em> moves toward the cathode, and an <em>anion</em> toward the anode. A cation is…", "Un <em>catión</em> va hacia el cátodo y un <em>anión</em> hacia el ánodo. Un catión es…"), [t("a positive ion", "un ion positivo"), t("a negative ion", "un ion negativo"), t("a neutral atom", "un átomo neutro")], 0, t("Cations are positive: they lost electrons.", "Los cationes son positivos: perdieron electrones.")),
        (t("<em>Valence</em> comes from <em>valere</em>, to be worth. Valence electrons are…", "<em>Valencia</em> viene de <em>valere</em>, valer. Los electrones de valencia son…"), [t("the outer electrons that decide how an atom combines", "los electrones exteriores que deciden cómo se combina el átomo"), t("all the electrons of the atom", "todos los electrones del átomo"), t("the electrons in the nucleus", "los electrones del núcleo")], 0, t("They give the atom its “combining power.”", "Dan al átomo su «capacidad de combinación».")),
        (t("In <em>periodic</em> table, “periodic” means…", "En tabla <em>periódica</em>, «periódica» significa…"), [t("properties repeat at regular intervals", "las propiedades se repiten a intervalos regulares"), t("it changes over time", "cambia con el tiempo"), t("it is printed in newspapers", "se publica en los periódicos")], 0, t("Regular repetition, like a period in music.", "Repetición regular, como un ciclo.")),
        (t("<em>Octet</em> rule: oct- means…", "Regla del <em>octeto</em>: oct- significa…"), ["8", "2", "10"], 0, t("Eight, as in octopus and October (once the 8th month).", "Ocho, como en octógono y en octubre (antes el 8.º mes).")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Break the word into its parts.", "Descomponga la palabra en sus partes."), "exp": e} for q, o, k, e in d]


def practica():
    A = {"en": ["count", "isotope-ion", "table", "bonds", "words"], "es": ["contar", "isotopo-ion", "tabla", "enlaces", "palabras"]}[C.L]
    libre = "      <p>" + t("Use the atomic number and the mass number. For an ion, adjust only the electrons.", "Use el número atómico y el número másico. En un ion, ajuste solo los electrones.") + "</p>\n" + f'''      <div class="practica" id="m1">
        <div class="enun" id="m1-enun"></div>
        <div class="campos"><div class="campo"><label for="m1-r">{t("Answer", "Respuesta")}</label><input type="text" inputmode="numeric" autocomplete="off" class="ancho" id="m1-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="m1-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="m1-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="m1-fb" role="status"></div>
        <p class="marcador" id="m1-marcador"></p>
      </div>'''
    mods = [
        (A[0], t("Count the particles", "Cuente las partículas"), libre),
        (A[1], t("Isotope or ion?", "¿Isótopo o ion?"), C.om("m2", t("Which particle changed?", "¿Qué partícula cambió?"))),
        (A[2], t("Read the periodic table", "Lea la tabla periódica"), C.om("m3", t("Group, period, valence electrons, and ions.", "Grupo, periodo, electrones de valencia e iones."))),
        (A[3], t("Ionic, covalent, or metallic?", "¿Iónico, covalente o metálico?"), C.clasifica("m4", t("Find both elements in the table.", "Localice los dos elementos en la tabla."))),
        (A[4], t("Words of chemistry", "Palabras de la química"), C.om("m5", t("Take the word apart before you answer.", "Descomponga la palabra antes de responder."))),
    ]
    js = (js_contar() + C.js_datos("ISO", banco_isotopo_ion()) + C.js_datos("TAB", banco_tabla()) + C.js_datos("ENL", clasif_enlaces()) + C.js_datos("PAL", banco_palabras()) +
          'creaPracticaLibre("m1", gA);\ncreaBanco("m2", ISO);\ncreaBanco("m3", TAB);\ncreaClasifica("m4", ENL);\ncreaBanco("m5", PAL);\n')
    return C.pagina_practica(N, titulo(), t("Five activities · new exercises every time · two tries in each one", "Cinco actividades · ejercicios nuevos cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
