"""LearnGED · Ciencias · Lección 3.1 · Teoría celular, organelos y membrana plasmática (EN/ES).
Fuente: clases_ciencias/leccion_3-1.html (sus diagramas están en tools/svg/3-1_*.svg) y los interactivos
ciencias/celula, ciencias/mitosis y ciencias/osmosis.
Uso: python3 tools/build_sci_3_1.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "3-1"


def titulo():
    return t("Cell theory, organelles, and the cell membrane", "Teoría celular, organelos y membrana plasmática")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


# ---------------------------------------------------------------- diagramas
def svg_mitosis():
    return C.svg_orig("3-1_0", {
        "1 · Una célula": "1 · One cell", "2 · El ADN se duplica": "2 · The DNA is copied", "3 · Las copias se separan": "3 · The copies separate",
        "4 · Dos células hijas": "4 · Two daughter cells", "2 cromosomas": "2 chromosomes", "cada uno, por duplicado": "each one, copied",
        "una copia a cada lado": "one copy to each side", "2 cromosomas cada una": "2 chromosomes each"},
        "Diagram of mitosis in four stages. In the first, a cell has two chromosomes, drawn as a blue bar and a brown bar. In the second, the DNA has been copied and each chromosome appears twice. In the third, the copies line up in the center and move apart to opposite sides. In the fourth, two daughter cells have formed, each with one blue bar and one brown bar: the same number of chromosomes as the original cell and the same information.")


def svg_celulas():
    return C.svg_orig("3-1_1", {
        "Célula animal": "Animal cell", "Célula vegetal": "Plant cell", "Núcleo": "Nucleus", "Mitocondria": "Mitochondrion", "Cloroplasto": "Chloroplast",
        "Ribosomas": "Ribosomes", "Vacuola central": "Central vacuole", "Pared celular": "Cell wall", "Membrana plasmática": "Cell membrane"},
        "Comparison of an animal cell and a plant cell. The animal cell is rounded, with no outer wall, and has the nucleus with its nucleolus and several mitochondria. The plant cell is rectangular, surrounded by a thick cell wall as well as the membrane, and has a central vacuole that fills much of the inside, the nucleus pushed to one side, several mitochondria, and several chloroplasts. The cell wall, the central vacuole, and the chloroplasts are found only in the plant cell.")


def svg_transporte():
    return C.svg_orig("3-1_2", {
        "Transporte pasivo": "Passive transport", "Transporte activo": "Active transport", "A favor del gradiente · no requiere energía": "With the gradient · no energy needed",
        "ATP": "ATP", "En contra del gradiente · requiere energía": "Against the gradient · needs energy"},
        "Comparison of passive and active transport. In passive transport the particles move from the area of high concentration to the area of low concentration, that is, with the gradient, and no energy is needed. In active transport the particles move from low concentration to high concentration, against the gradient, and energy is needed in the form of A T P.")


def svg_osmosis():
    return C.svg_orig("3-1_3", {
        "Hipotónica": "Hypotonic", "Isotónica": "Isotonic", "Hipertónica": "Hypertonic", "Menos soluto fuera": "Less solute outside", "El agua entra": "Water goes in",
        "La célula se hincha": "The cell swells", "Igual dentro y fuera": "Same inside and outside", "Entra tanta como sale": "As much goes in as out",
        "La célula no cambia": "The cell does not change", "Más soluto fuera": "More solute outside", "El agua sale": "Water goes out", "La célula se arruga": "The cell shrinks"},
        "Three cases of osmosis. In a hypotonic solution there is little solute outside the cell, water goes in, and the cell swells. In an isotonic solution the concentration is the same inside and outside, as much water goes in as goes out, and the cell does not change. In a hypertonic solution there is a lot of solute outside, water goes out, and the cell shrinks.")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Cell theory is one of the clearest examples of what the test means by a <strong>scientific theory</strong>: not a guess, but an explanation built on two centuries of observations and supported today by all of them.", "La teoría celular es uno de los ejemplos más claros de lo que el examen entiende por <strong>teoría científica</strong>: no una conjetura, sino una explicación construida sobre dos siglos de observaciones acumuladas y sostenida hoy por todas ellas.")}</p>
{C.tabla(t("The three statements of cell theory, the observations behind each one, and what follows from it", "Los tres postulados de la teoría celular, la observación que sostiene cada uno y su consecuencia"),
 [t("Statement", "Postulado"), t("What observation supports it", "Qué observación lo sostiene"), t("What follows", "Consecuencia")],
 [[t("All living things are made of cells.", "Todos los seres vivos están formados por células."), t("As microscopes got better in the 1800s, every tissue that was examined, from plants or animals, turned out to be made of cells.", "Al mejorar los microscopios en el siglo XIX, cada tejido examinado —vegetal o animal— resultó estar compuesto de células."), t("The cell is the building block shared by all life.", "La célula es la unidad estructural común a toda la vida.")],
  [t("The cell is the basic unit of structure and function.", "La célula es la unidad básica de estructura y función."), t("Each cell carries out the functions of life by itself: it gets energy, responds to its surroundings, and reproduces.", "Cada célula realiza por sí misma las funciones vitales: obtiene energía, responde al medio y se reproduce."), t("To explain a living thing, you first have to explain its cells.", "Explicar un organismo exige explicar primero sus células.")],
  [t("Every cell comes from another cell that already existed.", "Toda célula procede de otra célula preexistente."), t("No controlled experiment has ever produced cells from nonliving matter.", "Ningún experimento controlado logró jamás obtener células a partir de materia no viva."), t("Life does not appear out of nothing (no “spontaneous generation”). Life is continuous.", "Queda descartada la generación espontánea. La vida tiene continuidad.")]])}
{C.caja("ojo", t("Why this is a theory and not a hypothesis", "Por qué esto es una teoría y no una hipótesis"), "<p>" + t("The test keeps the two words apart. A <strong>hypothesis</strong> is a proposed explanation that still has to be tested; a <strong>theory</strong> is an explanation that has already passed repeated tests and ties together a whole body of observations. In everyday speech, “theory” suggests doubt; in science it means just the opposite.", "El examen distingue con claridad ambos términos. Una <strong>hipótesis</strong> es una explicación propuesta que aún debe someterse a prueba; una <strong>teoría</strong> es una explicación que ya superó pruebas repetidas y que organiza un cuerpo entero de observaciones. En el lenguaje corriente «teoría» sugiere duda; en ciencia significa justo lo contrario.") + "</p>")}
{P(t("Try it 1 · Theory or hypothesis?", "Pruebe 1 · ¿Teoría o hipótesis?"), t("Cell theory is called a <em>theory</em> because…", "La teoría celular recibe el nombre de <em>teoría</em> porque…"),
   [t("it has not been proved yet", "todavía no se ha demostrado"), t("it explains many observations and has passed repeated tests", "explica muchas observaciones y ha superado pruebas repetidas"), t("one scientist proposed it", "la propuso un solo científico")], 1,
   {0: t("That is the everyday meaning. In science, a theory is the strongest kind of explanation.", "Ese es el sentido corriente. En ciencia, una teoría es el tipo de explicación más sólido."), 2: t("Many researchers over two centuries built it.", "La construyeron muchos investigadores durante dos siglos.")},
   t("A theory ties together a whole body of observations and has survived repeated tests.", "Una teoría organiza un cuerpo entero de observaciones y ha superado pruebas repetidas."))}"""

    s2 = f"""<p>{t("The third statement says that every cell comes from another cell, but it does not say how. The answer is <strong>cell division</strong>. Without it, cell theory would be incomplete: a claim about where cells come from, with no mechanism behind it.", "El tercer postulado afirma que toda célula procede de otra célula preexistente, pero no dice de qué manera. La respuesta es la <strong>división celular</strong>, y sin ella la teoría celular quedaría incompleta: una afirmación sobre el origen de las células sin ningún mecanismo que la sostenga.")}</p>
<p>{t("Cells divide for three reasons: so the body can grow, to repair damaged tissue, and to replace cells that wear out. Skin and blood are renewed all through life.", "Las células se dividen por tres motivos: para que el organismo crezca, para reparar un tejido dañado y para reemplazar células que se desgastan. La piel y la sangre se renuevan de forma continua a lo largo de toda la vida.")}</p>
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>Chromosome</strong>: from {R('chromo-')}, color, and {R('-some')}, body. The name comes from the fact that these structures soaked up the dyes of the 1800s and so became visible under the microscope. A chromosome is DNA packed tightly so it can be shared out without tangling. The same root {R('-some')} appears in <em>ribosome</em>, and {R('chromo-')} in <em>chromatic</em> and <em>monochrome</em>. A human cell has 46 chromosomes, in 23 pairs.", f"<strong>Cromosoma</strong>: de {R('cromo-')}, color, y {R('-soma')}, cuerpo. El nombre viene de que estas estructuras se teñían intensamente con los colorantes del siglo XIX y por eso se hicieron visibles al microscopio. Un cromosoma es el ADN empaquetado y compactado para poder repartirse sin enredarse. La misma raíz {R('-soma')} ya apareció en <em>ribosoma</em>, y {R('cromo-')} reaparece en <em>cromático</em> y <em>monocromo</em>. La célula humana tiene 46 cromosomas, organizados en 23 pares.")}</p>
<p>{t("Before it divides, the cell <strong>copies all of its DNA</strong>. That step makes sure each new cell gets a full set of instructions and not half of them. Only then is the copy shared out.", "Antes de dividirse, la célula <strong>duplica todo su ADN</strong>. Ese paso es el que garantiza que cada célula hija reciba una copia completa y no la mitad de las instrucciones. Solo después se reparte lo duplicado.")}</p>
{svg_mitosis()}
{C.tabla(t("The stages of cell division by mitosis, what happens in each one, and why it is needed", "Etapas de la división celular por mitosis, con lo que ocurre en cada una y por qué es necesaria"),
 [t("Stage", "Etapa"), t("What happens", "Qué ocurre"), t("Why it is needed", "Por qué es necesaria")],
 [[t("Interphase", "Interfase"), t("The cell grows, does its jobs, and copies all of its DNA.", "La célula crece, cumple sus funciones y duplica todo su ADN."), t("Without the copy, there would not be two full sets to share.", "Sin la duplicación previa, no habría dos juegos completos que repartir.")],
  [t("Prophase", "Profase"), t("The copied DNA packs tightly and the chromosomes become visible. The covering of the nucleus breaks down.", "El ADN duplicado se compacta y los cromosomas se hacen visibles. La envoltura del núcleo se desorganiza."), t("A long, loose thread would tangle when shared; packed tight, it can be moved.", "Un hilo largo y suelto se enredaría al repartirse; compactado, se puede mover.")],
  [t("Metaphase", "Metafase"), t("The copied chromosomes line up across the middle of the cell.", "Los cromosomas duplicados se alinean en el plano central de la célula."), t("Lining up makes sure the sharing is exact and not random.", "La alineación asegura que el reparto sea exacto y no al azar.")],
  [t("Anaphase", "Anafase"), t("The copies of each chromosome pull apart and move to opposite ends.", "Las copias de cada cromosoma se separan y viajan hacia polos opuestos."), t("This is the sharing itself: one full set goes to each side.", "Es el reparto propiamente dicho: un juego completo hacia cada lado.")],
  [t("Telophase and cytokinesis", "Telofase y citocinesis"), t("Two nuclei form again and the cytoplasm splits into two cells.", "Se reconstruyen los dos núcleos y el citoplasma se divide en dos células."), t("It ends the process: one cell has become two separate cells.", "Cierra el proceso: de una célula resultan dos, ya independientes.")]])}
{C.ejemplo(t("Example 1 · Counting chromosomes before and after", "Ejemplo 1 · Contar cromosomas antes y después"),
 [("", t("A human skin cell, with 46 chromosomes, divides by mitosis. How many chromosomes will each daughter cell have?", "Una célula humana de la piel, con 46 cromosomas, se divide por mitosis. ¿Cuántos cromosomas tendrá cada célula hija?")),
  ("1", t("During interphase, the 46 chromosomes are copied. The cell now has two copies of each one.", "Durante la interfase, los 46 cromosomas se duplican. La célula pasa a tener dos copias de cada uno.")),
  ("2", t("In anaphase, one copy of each chromosome goes to each end.", "En la anafase, una copia de cada cromosoma va a cada polo.")),
  ("3", t("Each daughter cell gets a full set: <strong>46 chromosomes</strong>, the same as the original cell.", "Cada célula hija recibe un juego completo: <strong>46 cromosomas</strong>, los mismos que tenía la célula original."))],
 t("<strong>What to remember:</strong> mitosis makes two cells that are genetically identical to the original, with the same number of chromosomes. No information is lost or gained. That is why it works for growth and repair, where what you need is more of the same.", "<strong>La conclusión que hay que retener:</strong> la mitosis produce dos células genéticamente idénticas a la original y con el mismo número de cromosomas. No se pierde ni se gana información. Por eso sirve para crecer y reparar, donde lo que hace falta es más de lo mismo."))}
{C.caja("ojo", t("The copy comes first, not after", "La duplicación va antes, no después"), "<p>" + t("The most common mistake is to picture the cell splitting in two and then each half filling in what it is missing. That is not what happens. First all the DNA is copied, and only then is it shared out. If the order were reversed, each daughter cell would get half the instructions and could not work.", "El error más frecuente es imaginar que la célula se parte en dos y luego cada mitad completa lo que le falta. No ocurre así. Primero se duplica todo el ADN y solo entonces se reparte. Si el orden se invirtiera, cada célula hija se quedaría con la mitad de las instrucciones y no podría funcionar.") + "</p>")}
{C.caja("tip", t("A second way to divide comes in Topic 4", "Hay una segunda forma de dividirse, y llega en el Tema 4"), "<p>" + t("Egg and sperm cells cannot form by mitosis: if each carried 46 chromosomes, together they would give 92, and in the next generation 184. <strong>Meiosis</strong> solves that problem by making cells with half, 23 chromosomes. That is also why, in a Punnett square, each parent gives only one allele of each pair.", "Los óvulos y los espermatozoides no pueden formarse por mitosis: si cada uno llevara 46 cromosomas, al unirse resultarían 92, y en la generación siguiente 184. La <strong>meiosis</strong> resuelve ese problema produciendo células con la mitad, 23 cromosomas. Esa es también la razón por la que en un cuadro de Punnett cada progenitor aporta un solo alelo de cada par.") + "</p>")}
{P(t("Try it 2 · Chromosomes after mitosis", "Pruebe 2 · Cromosomas después de la mitosis"), t("A dog cell has 78 chromosomes. After mitosis, each daughter cell has…", "Una célula de perro tiene 78 cromosomas. Después de la mitosis, cada célula hija tiene…"),
   ["39", "78", "156"], 1,
   {0: t("Half is what meiosis gives. Mitosis keeps the number.", "La mitad es lo que da la meiosis. La mitosis conserva el número."), 2: t("156 is the copied DNA before sharing. Each cell gets one full set.", "156 es el ADN duplicado antes del reparto. Cada célula recibe un juego completo.")},
   t("Mitosis gives two cells identical to the original: 78 chromosomes each.", "La mitosis da dos células idénticas a la original: 78 cromosomas cada una."))}
{P(t("Try it 3 · If the order changed", "Pruebe 3 · Si cambiara el orden"), t("If a cell split in two <em>before</em> copying its DNA, each daughter cell would…", "Si una célula se partiera en dos <em>antes</em> de duplicar su ADN, cada célula hija…"),
   [t("get only part of the instructions", "recibiría solo una parte de las instrucciones"), t("be twice as large", "sería el doble de grande"), t("be exactly the same as normal", "sería exactamente igual que siempre")], 0,
   {1: t("Size is not the problem. Think about the DNA.", "El tamaño no es el problema. Piense en el ADN."), 2: t("Without the copy, there is only one set to share between two cells.", "Sin la copia, hay un solo juego para repartir entre dos células.")},
   t("The copy guarantees a full set for each cell; without it, each gets part.", "La duplicación garantiza un juego completo para cada célula; sin ella, cada una recibe una parte."))}
{C.enlace(N, anc("mitosis", "mitosis"), t("put mitosis in order", "ordene la mitosis"), t("Arrange the stages of cell division, first by what happens and then by name.", "Ordene las etapas de la división celular, primero por lo que ocurre y después por su nombre."))}"""

    s3 = f"""<p>{t("An <strong>organelle</strong> is a structure inside the cell that does one special job. The word itself says it: a small organ. Comparing the cell to a factory helps you remember the jobs, as long as you remember it is only a comparison, not a description.", "Un <strong>organelo</strong> es una estructura interna especializada en una tarea. La palabra misma lo dice: órgano pequeño. La analogía de la fábrica ayuda a fijar las funciones, siempre que se recuerde que es una analogía y no una descripción.")}</p>
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"Almost every name can be taken apart. <strong>Mitochondrion</strong>: from {R('mito-')}, thread, and {R('-chondrion')}, grain, for how it looks under the microscope. <strong>Chloroplast</strong>: from {R('chloro-')}, green, and {R('-plast')}, formed body: the green body. <strong>Endoplasmic reticulum</strong>: <em>reticulum</em> is a small net, {R('endo-')} is inside, and <em>plasm</em> is the content of the cell: a net inside the cytoplasm. <strong>Ribosome</strong>: {R('ribo-')}, for the ribonucleic acid (RNA) it is made of, and {R('-some')}, body. <strong>Cytoplasm</strong>: {R('cyto-')} is cell. Five roots solve five names.", f"Casi todos los nombres se dejan descomponer. <strong>Mitocondria</strong>: de {R('mito-')}, hilo, y {R('-condria')}, gránulo, por su aspecto al microscopio. <strong>Cloroplasto</strong>: de {R('cloro-')}, verde, y {R('-plasto')}, formación u orgánulo; es decir, el orgánulo verde. <strong>Retículo endoplasmático</strong>: <em>retículo</em> es red pequeña, {R('endo-')} es dentro y <em>plasma</em> es el contenido celular: una red dentro del citoplasma. <strong>Ribosoma</strong>: de {R('ribo-')}, por el ácido ribonucleico que lo forma, y {R('-soma')}, cuerpo. <strong>Citoplasma</strong>: {R('cito-')} es célula. Cinco raíces resuelven cinco nombres.")}</p>
{C.tabla(t("The main organelles, their job in the cell, and the matching part of a factory", "Los organelos principales, su función celular y la analogía de fábrica que le corresponde a cada uno"),
 [t("Organelle", "Organelo"), t("Job", "Función"), t("Factory comparison", "Analogía de fábrica")],
 [[t(*o[0]), t(*o[1]), t(*o[2])] for o in ORGANELOS])}
{P(t("Try it 4 · The power plant", "Pruebe 4 · La central eléctrica"), t("The structure that carries out cellular respiration is…", "La estructura responsable de la respiración celular es…"),
   [t("the ribosome", "el ribosoma"), t("the nucleus", "el núcleo"), t("the mitochondrion", "la mitocondria")], 2,
   {0: t("The ribosome builds proteins.", "El ribosoma fabrica proteínas."), 1: t("The nucleus holds the DNA.", "El núcleo guarda el ADN.")},
   t("The mitochondrion releases the energy of glucose: the power plant.", "La mitocondria libera la energía de la glucosa: la central eléctrica."))}
{C.enlace(N, anc("organelles", "organelos"), t("organelles and their jobs", "organelos y funciones"), t("Name the organelle from its job, its factory role, or its roots.", "Nombre el organelo por su función, su papel en la fábrica o sus raíces."))}"""

    s4 = f"""<p>{t("The differences are not decoration: each one fits a different way of living. A plant cell makes its own food and does not move, and that explains its three special structures.", "Las diferencias no son decorativas: cada una responde a una forma distinta de vivir. La célula vegetal fabrica su propio alimento y no se desplaza, y sus tres estructuras exclusivas se explican por ahí.")}</p>
{svg_celulas()}
{C.tabla(t("Prokaryotic and eukaryotic cells compared on five features", "Comparación entre célula procariota y célula eucariota según cinco características"),
 [t("Feature", "Característica"), t("Prokaryote", "Procariota"), t("Eukaryote", "Eucariota")],
 [[t("Nucleus", "Núcleo"), t("None. The DNA floats free in the cytoplasm.", "No lo tiene. El ADN flota libre en el citoplasma."), t("Yes, with its own covering that keeps the DNA apart from the rest.", "Sí, con envoltura propia que separa el ADN del resto.")],
  [t("Organelles with a membrane", "Organelos con membrana"), t("None.", "No los tiene."), t("Mitochondria, reticulum, and chloroplasts in plant cells.", "Mitocondrias, retículo, cloroplastos en las vegetales.")],
  [t("Size", "Tamaño"), t("Small: about 1 × 10⁻⁶ m.", "Pequeña: del orden de 1 × 10⁻⁶ m."), t("Larger: between 1 × 10⁻⁵ and 1 × 10⁻⁴ m.", "Mayor: entre 1 × 10⁻⁵ y 1 × 10⁻⁴ m.")],
  [t("Examples", "Ejemplos"), t("Bacteria and archaea.", "Bacterias y arqueas."), t("Animals, plants, fungi, and protists.", "Animales, plantas, hongos y protistas.")],
  [t("Organization", "Organización"), t("Almost always one-celled.", "Casi siempre unicelular."), t("One-celled or many-celled.", "Unicelular o pluricelular.")]])}
{C.caja("tip", t("The root solves the pair", "La raíz resuelve la pareja"), "<p>" + t(f"{R('-karyote')} comes from the Greek word for kernel, the nucleus. {R('Pro-')} means before: a <em>prokaryote</em> is “before the nucleus,” a cell that does not have one yet. {R('Eu-')} means true: a <em>eukaryote</em> has a “true nucleus.” If you know the pair pro- / eu-, you will not mix them up again.", f"{R('-cariota')} viene de la palabra griega para núcleo. {R('Pro-')} significa antes: <em>procariota</em> es «antes del núcleo», la célula que aún no lo tiene. {R('Eu-')} significa verdadero: <em>eucariota</em> es «con núcleo verdadero». Quien reconoce el par pro- / eu- no vuelve a confundir cuál es cuál.") + "</p>")}
{P(t("Try it 5 · Only in plants", "Pruebe 5 · Solo en plantas"), t("The three structures found only in plant cells (not in animal cells) are…", "Las tres estructuras exclusivas de la célula vegetal son…"),
   [t("cell wall, chloroplast, and central vacuole", "pared celular, cloroplasto y vacuola central"), t("nucleus, mitochondrion, and ribosome", "núcleo, mitocondria y ribosoma"), t("cell membrane, nucleus, and cytoplasm", "membrana plasmática, núcleo y citoplasma")], 0,
   {1: t("Animal cells have all three of those.", "La célula animal tiene las tres."), 2: t("Every eukaryotic cell has those.", "Toda célula eucariota las tiene.")},
   t("A plant makes its own food (chloroplasts), stands without a skeleton (wall), and stores water (vacuole).", "La planta fabrica su alimento (cloroplastos), se sostiene sin esqueleto (pared) y almacena agua (vacuola)."))}
{P(t("Try it 6 · Bacteria", "Pruebe 6 · Las bacterias"), t("A bacterium is a prokaryotic cell because…", "Una bacteria es una célula procariota porque…"),
   [t("it is smaller than other cells", "es de menor tamaño que las demás células"), t("its DNA is not inside a nucleus with its own covering", "su ADN no está encerrado en un núcleo con envoltura propia"), t("it has no DNA", "no contiene ADN")], 1,
   {0: t("Size goes with it, but it is not what defines it.", "El tamaño la acompaña, pero no la define."), 2: t("Every cell has DNA.", "Toda célula tiene ADN.")},
   t("Pro-karyote: no true nucleus. The DNA floats in the cytoplasm.", "Pro-cariota: sin núcleo verdadero. El ADN flota en el citoplasma."))}
{C.enlace(N, anc("cell-types", "tipos-de-celula"), t("animal, plant, or bacterium?", "¿animal, vegetal o bacteria?"), t("Read the description of each cell and decide what kind it is.", "Lea la descripción de cada célula y decida de qué tipo es."))}"""

    s5 = f"""<p>{t("The cell membrane is <strong>semipermeable</strong>: it lets some substances through and not others. Because of that, the cell can keep its inside different from the outside, which, in the end, is what being alive means.", "La membrana plasmática es <strong>semipermeable</strong>: deja pasar unas sustancias y otras no. De esa selectividad depende que la célula conserve un interior distinto del exterior, que es, en el fondo, lo que significa estar viva.")}</p>
<p>{t("The key word of this section is <strong>gradient</strong>: the difference in concentration between two areas. Substances tend to move on their own from where there is a lot to where there is little, until both sides are even. That movement costs no energy; moving the other way does.", "La palabra clave de toda esta sección es <strong>gradiente</strong>: la diferencia de concentración entre dos zonas. Las sustancias tienden espontáneamente a moverse de donde hay mucho a donde hay poco, hasta igualar ambos lados. Ese movimiento espontáneo no cuesta energía; el movimiento contrario, sí.")}</p>
{svg_transporte()}
{C.tabla(t("The three ways substances cross the membrane, what moves and in which direction, and whether energy is needed", "Los tres mecanismos de transporte a través de la membrana, qué mueve cada uno y si requiere energía"),
 [t("Mechanism", "Mecanismo"), t("What moves and where", "Qué se mueve y hacia dónde"), t("Does it need energy?", "¿Requiere energía?")],
 [[t("Diffusion", "Difusión"), t("Any dissolved substance, from where it is more concentrated to where it is less.", "Cualquier sustancia disuelta, desde donde está más concentrada hacia donde lo está menos."), t("No. It happens on its own.", "No. Es un movimiento espontáneo.")],
  [t("Osmosis", "Ósmosis"), t("Only water, across the membrane, toward the side with more solute.", "Únicamente agua, a través de la membrana, hacia el lado donde hay más soluto."), t("No. It is the diffusion of water.", "No. Es difusión de agua.")],
  [t("Active transport", "Transporte activo"), t("Substances the cell needs to collect, from where there is little to where there is already a lot.", "Sustancias que la célula necesita acumular, desde donde hay poco hacia donde ya hay mucho."), t("Yes. The cell spends ATP.", "Sí. La célula gasta ATP.")]])}
{C.caja("ojo", t("Water follows the salt", "El agua sigue a la sal"), "<p>" + t("Osmosis is often remembered backward. Water does not move toward where there is less water “looking for balance”; it moves toward the side with <strong>more solute</strong>. Both statements say the same thing (more solute means less water), but the test words its questions in terms of solute concentration. Always reason that way: water follows the salt.", "La ósmosis se explica al revés de como suele recordarse: el agua no va hacia donde hay menos agua «buscando equilibrio», sino hacia el lado donde hay <strong>más soluto</strong>. Ambas formulaciones son equivalentes —más soluto significa menos agua—, pero el examen redacta sus preguntas en términos de concentración de soluto. Conviene razonar siempre en esos términos: el agua sigue a la sal.") + "</p>")}
{P(t("Try it 7 · Against the gradient", "Pruebe 7 · En contra del gradiente"), t("Moving a substance from where there is little of it to where there is already a lot is…", "El movimiento de una sustancia desde donde hay poca concentración hacia donde ya hay mucha corresponde a…"),
   [t("simple diffusion", "difusión simple"), t("active transport, which uses ATP", "transporte activo, con gasto de ATP"), t("osmosis", "ósmosis")], 1,
   {0: t("Diffusion goes from more to less.", "La difusión va de más a menos."), 2: t("Osmosis moves only water, and it needs no energy.", "La ósmosis mueve solo agua, y sin gasto de energía.")},
   t("Going against the gradient costs energy: active transport.", "Ir en contra del gradiente cuesta energía: transporte activo."))}
{P(t("Try it 8 · What crosses?", "Pruebe 8 · ¿Qué atraviesa?"), t("In osmosis, which substance crosses the membrane?", "En la ósmosis, ¿qué sustancia atraviesa la membrana?"),
   [t("Salt", "La sal"), t("Glucose", "La glucosa"), t("Water", "El agua")], 2,
   {0: t("Salt is the solute; it stays where it is.", "La sal es el soluto; se queda donde está."), 1: t("Glucose is a solute too.", "La glucosa también es un soluto.")},
   t("Osmosis is the diffusion of water.", "La ósmosis es la difusión del agua."))}
{C.enlace(N, anc("transport", "transporte"), t("diffusion, osmosis, or active transport?", "¿difusión, ósmosis o transporte activo?"), t("Real situations: decide which mechanism is at work.", "Situaciones reales: decida qué mecanismo actúa."))}"""

    s6 = f"""<p>{t("This is the level the test checks: not recognizing a definition, but <strong>predicting</strong> a result. The three possible cases come from comparing the solute concentration outside the cell with the one inside.", "Este es el nivel que evalúa el examen: no reconocer una definición, sino <strong>anticipar</strong> un resultado. Los tres casos posibles dependen de comparar la concentración de soluto de fuera con la de dentro de la célula.")}</p>
{svg_osmosis()}
{C.ejemplo(t("Example 2 · A prediction, step by step", "Ejemplo 2 · Una predicción paso a paso"),
 [("", t("Red blood cells are placed in distilled water, which has no salt at all. What will happen?", "Se colocan glóbulos rojos en agua destilada, que no contiene sal alguna. ¿Qué ocurrirá?")),
  ("1", t("Compare the solute: inside the blood cell there are salts; outside, none. The outside is <strong>hypotonic</strong>.", "Se compara la concentración de soluto: dentro del glóbulo hay sales; fuera, ninguna. El exterior es <strong>hipotónico</strong>.")),
  ("2", t("Water follows the salt, so it will go <strong>into</strong> the blood cell.", "El agua sigue a la sal, de modo que <strong>entrará</strong> en el glóbulo.")),
  ("3", t("The blood cell will swell. Since it has no cell wall to hold it, it can burst.", "El glóbulo se hinchará. Como carece de pared celular que lo contenga, puede llegar a romperse."))],
 t("<strong>The comparison that completes the idea:</strong> a plant cell in the same distilled water also takes in water, but its cell wall holds against the pressure, and the cell becomes firm instead of bursting. That is exactly what keeps a well-watered plant standing, and what is lost when it wilts.", "<strong>Y la comparación que cierra la idea:</strong> una célula vegetal en la misma agua destilada también absorbe agua, pero su pared celular resiste la presión y la célula queda firme en lugar de reventar. Eso es exactamente lo que mantiene erguida una planta bien regada, y lo que se pierde cuando se marchita."))}
{C.caja("tip", t("The prefixes give the answer before the reasoning", "Los prefijos dan la respuesta antes que el razonamiento"), "<p>" + t(f"{R('hypo-')} means below, {R('hyper-')} above, and {R('iso-')} equal. A <strong>hypotonic</strong> solution has less solute than the cell; a <strong>hypertonic</strong> one, more. Once you know where the solute is, water moves toward it. The same prefixes appear in <em>hypothermia</em>, <em>hypertension</em>, and <em>isothermal</em>.", f"{R('hipo-')} significa por debajo, {R('hiper-')} por encima e {R('iso-')} igual. La disolución <strong>hipotónica</strong> tiene menos soluto que la célula; la <strong>hipertónica</strong>, más. Y una vez situado el soluto, el agua se mueve hacia él. Los mismos prefijos reaparecen en <em>hipotermia</em>, <em>hipertensión</em> e <em>isotérmico</em>.") + "</p>")}
{P(t("Try it 9 · Sugar syrup", "Pruebe 9 · Almíbar"), t("A plant cell is placed in a very concentrated sugar solution. You can expect it to…", "Una célula vegetal se coloca en una disolución muy concentrada de azúcar. Cabe esperar que…"),
   [t("lose water, and its contents pull away from the wall", "pierda agua y su contenido se separe de la pared"), t("take in water until it bursts", "absorba agua hasta reventar"), t("not change at all", "no experimente ningún cambio")], 0,
   {1: t("Where is there more solute: inside or outside?", "¿Dónde hay más soluto: dentro o fuera?"), 2: t("The outside has much more solute, so water moves.", "Fuera hay mucho más soluto, así que el agua se mueve.")},
   t("Hypertonic outside: water goes out. The wall keeps its shape, but the inside shrinks away from it.", "Exterior hipertónico: el agua sale. La pared conserva la forma, pero el interior se separa de ella."))}
{P(t("Try it 10 · No change", "Pruebe 10 · Sin cambios"), t("A red blood cell stays the same in a solution. That solution is…", "Un glóbulo rojo permanece sin cambios en una disolución. Esa disolución es…"),
   [t("isotonic compared with the inside of the cell", "isotónica respecto del interior del glóbulo"), t("hypotonic compared with the inside of the cell", "hipotónica respecto del interior del glóbulo"), t("distilled water", "agua destilada")], 0,
   {1: t("In a hypotonic solution, water goes in and the cell swells.", "En una hipotónica, el agua entra y el glóbulo se hincha."), 2: t("Distilled water is the most hypotonic of all.", "El agua destilada es la más hipotónica de todas.")},
   t("Iso- = equal: as much water goes in as out.", "Iso- = igual: entra tanta agua como sale."))}
{C.enlace(N, anc("predict", "predecir"), t("predict what the cell does", "prediga qué le pasa a la célula"), t("New cases every time: compare the solute, decide where the water goes, and predict the result.", "Casos nuevos cada vez: compare el soluto, decida hacia dónde va el agua y prediga el resultado."))}"""

    s7 = f"""<p>{t("A short science text written for this level. Notice how it explains an everyday practice with a cell mechanism.", "Texto científico breve adaptado al nivel. Observe que explica una práctica cotidiana mediante un mecanismo celular.")}</p>
{C.lectura(t("Why salt keeps food from spoiling", "Por qué la sal conserva los alimentos"),
 [t("Salting meat or fish to keep it is thousands of years old, much older than any knowledge of cells. Even so, why it works is fully explained by osmosis.", "Salar la carne o el pescado para conservarlos es una técnica de miles de años, muy anterior a cualquier conocimiento sobre las células. Sin embargo, su eficacia se explica por completo mediante la ósmosis."),
  t("The microorganisms that spoil food, bacteria and fungi, are cells surrounded by a semipermeable membrane. When the food is covered with salt, the liquid around those cells has a much higher solute concentration than their inside: it becomes hypertonic.", "Los microorganismos que descomponen un alimento —bacterias y hongos— son células rodeadas de una membrana semipermeable. Cuando el alimento se cubre de sal, el medio que rodea a esas células pasa a tener una concentración de soluto mucho mayor que la de su interior: se vuelve hipertónico."),
  t("Under those conditions, water leaves the microbe cells. As they lose water, their inside becomes more concentrated, the reactions that keep them alive stop, and the microorganism stops multiplying. You do not need to destroy it: taking away the water it needs to work is enough.", "En esas condiciones el agua sale de las células microbianas hacia el exterior. Al perder agua, el interior se concentra, las reacciones que sostienen la vida se detienen y el microorganismo deja de multiplicarse. No es necesario destruirlo: basta con retirarle el agua que necesita para funcionar."),
  t("The same idea explains why sugar keeps jam from spoiling, why a salad gives off liquid when you salt it, and why seawater does not quench thirst: drinking it puts more salt into the body than the body can get rid of, and as a result the cells give up water instead of getting it.", "El mismo principio explica que el azúcar conserve las mermeladas, que una ensalada suelte líquido al salarla y que el agua de mar no sirva para calmar la sed: al beberla se introduce en el cuerpo más sal de la que este puede eliminar, y el resultado es que las células ceden agua en lugar de recibirla.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Salting is a very old way to keep food.", "La salazón es una técnica de conservación muy antigua."), t("Salt keeps food because it makes a hypertonic environment that pulls water out of microorganisms.", "La sal conserva los alimentos porque crea un medio hipertónico que extrae el agua de los microorganismos."), t("Bacteria and fungi have a semipermeable membrane.", "Las bacterias y los hongos tienen membrana semipermeable.")], 1,
   {0: t("True, but it is a detail of the first paragraph.", "Es cierto, pero es un detalle del primer párrafo."), 2: t("True, but it is one step of the explanation, not the main idea.", "Es cierto, pero es un paso de la explicación, no la idea central.")},
   t("The whole text explains how salt works through osmosis.", "Todo el texto explica cómo actúa la sal mediante la ósmosis."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("For the microbe cells, salted food is a solution that is…", "Respecto de las células microbianas, el alimento salado constituye un medio…"),
   [t("isotonic", "isotónico"), t("hypotonic", "hipotónico"), t("hypertonic", "hipertónico")], 2,
   {0: t("Iso- is equal. Is there the same amount of solute?", "Iso- es igual. ¿Hay el mismo soluto?"), 1: t("Hypo- is less. Is there less solute outside?", "Hipo- es menos. ¿Hay menos soluto fuera?")},
   t("Much more solute outside than inside: hypertonic.", "Mucho más soluto fuera que dentro: hipertónico."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("According to the text, salt stops microorganisms because it…", "Según el texto, la sal detiene a los microorganismos porque…"),
   [t("takes away the water they need to work", "les retira el agua que necesitan para funcionar"), t("destroys their membrane directly", "destruye directamente su membrana"), t("raises the temperature of the food", "eleva la temperatura del alimento")], 0,
   {1: t("The text says you do not need to destroy it.", "El texto dice que no es necesario destruirlo."), 2: t("The text does not talk about temperature.", "El texto no habla de temperatura.")},
   t("Third paragraph: taking away its water is enough.", "Tercer párrafo: basta con retirarle el agua."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Why does seawater not quench thirst?", "¿Por qué el agua de mar no calma la sed?"),
   [t("Because it has microorganisms", "Porque contiene microorganismos"), t("Because the body cannot take in salty water", "Porque el cuerpo no puede absorber el agua salada"), t("Because it adds more salt than the body can remove, so the cells give up water", "Porque aporta más sal de la que el cuerpo elimina, y entonces las células ceden agua")], 2,
   {0: t("The text does not say that.", "El texto no dice eso."), 1: t("It is absorbed; the problem is the salt it brings.", "Se absorbe; el problema es la sal que trae.")},
   t("Last paragraph: the cells give up water instead of getting it.", "Último párrafo: las células ceden agua en lugar de recibirla."))}"""

    G = lambda *a: C.ged_item(P, *a)
    papa = {"tipo": "tabla", "encabezados": [t("Salt in the water (%)", "Sal en el agua (%)"), "0", "2", "4", "8"],
            "filas": [[t("Change in mass of the potato (%)", "Cambio de masa de la papa (%)"), "+12", "+3", "−6", "−14"]]}
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK).", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SP.7.a", "2", t("<em>For centuries, people believed that flies came out of rotting meat. In 1668, Francesco Redi covered some jars of meat with fine cloth and left others open. Maggots appeared only in the open jars.</em><br>Which statement of cell theory does this experiment support?", "<em>Durante siglos se creyó que las moscas nacían de la carne podrida. En 1668, Francesco Redi cubrió con una tela fina algunos frascos con carne y dejó otros abiertos. Solo aparecieron larvas en los frascos abiertos.</em><br>¿Qué postulado de la teoría celular apoya este experimento?"),
   [t("All living things are made of cells.", "Todos los seres vivos están formados por células."), t("The cell is the basic unit of function.", "La célula es la unidad básica de función."), t("Living things come only from other living things.", "Los seres vivos proceden solo de otros seres vivos."), t("Cells contain DNA.", "Las células contienen ADN.")], 2,
   {0: t("Redi did not look at cells at all.", "Redi no observó células."), 1: t("The experiment is about where living things come from.", "El experimento trata de dónde vienen los seres vivos."), 3: t("DNA was unknown in 1668 and is not a statement of the theory.", "El ADN era desconocido en 1668 y no es un postulado.")},
   t("No flies reached the covered meat, so no maggots appeared: life came from life, not from the meat.", "Las moscas no llegaron a la carne cubierta y no hubo larvas: la vida vino de vida, no de la carne."))}
{G(2, "SP.3.c", "2–3", t("<em>A class put equal pieces of potato in water with different amounts of salt for one hour and measured the change in mass.</em>", "<em>Una clase colocó trozos iguales de papa en agua con distintas cantidades de sal durante una hora y midió el cambio de masa.</em>") + C.grafica(papa, t("Data table", "Tabla de datos")) + t("At about what salt concentration would the potato’s mass <strong>not change</strong>?", "¿Con qué concentración de sal, aproximadamente, la masa de la papa <strong>no cambiaría</strong>?"),
   [t("0%", "0 %"), t("Between 2% and 4%", "Entre 2 % y 4 %"), t("Between 4% and 8%", "Entre 4 % y 8 %"), t("Above 8%", "Más de 8 %")], 1,
   {0: t("At 0% the potato gained 12%: water went in.", "Con 0 % la papa ganó un 12 %: entró agua."), 2: t("At 4% it already lost mass. Where does the change go from + to −?", "Con 4 % ya perdió masa. ¿Dónde pasa el cambio de + a −?"), 3: t("Above 8% it loses even more.", "Por encima de 8 % pierde aún más.")},
   t("The change goes from +3 at 2% to −6 at 4%: zero is in between. There the water outside is isotonic with the potato cells.", "El cambio pasa de +3 con 2 % a −6 con 4 %: el cero está entre ambos. Ahí el agua es isotónica respecto de las células de la papa."))}
{G(3, "SP.3.c", "2", t("<em>In hospitals, a salt solution of 0.9% is given into the veins because it has the same solute concentration as blood cells.</em><br>What would happen to red blood cells if they received a 5% salt solution by mistake?", "<em>En los hospitales se administra en la vena una solución salina al 0.9 %, porque tiene la misma concentración de soluto que los glóbulos rojos.</em><br>¿Qué les pasaría a los glóbulos rojos si recibieran por error una solución al 5 %?"),
   [t("They would take in water and burst.", "Absorberían agua y reventarían."), t("They would lose water and shrink.", "Perderían agua y se arrugarían."), t("They would not change.", "No cambiarían."), t("They would grow a cell wall.", "Formarían una pared celular.")], 1,
   {0: t("That would happen in a hypotonic solution, like pure water.", "Eso pasaría en una hipotónica, como el agua pura."), 2: t("5% is much more than 0.9%: the solution is not isotonic.", "5 % es mucho más que 0.9 %: no es isotónica."), 3: t("Animal cells cannot make a cell wall.", "Las células animales no pueden fabricar pared celular.")},
   t("5% is hypertonic compared with the cells: water follows the salt out, and the cells shrink.", "5 % es hipertónica respecto de los glóbulos: el agua sigue a la sal hacia fuera y se arrugan."))}
{G(4, "SP.1.b", "2", t("<em>“The cell membrane is semipermeable: it lets water and some small molecules through, but stops most large molecules.”</em><br>In this sentence, <em>semipermeable</em> means that the membrane…", "<em>«La membrana plasmática es semipermeable: deja pasar el agua y algunas moléculas pequeñas, pero detiene la mayoría de las moléculas grandes.»</em><br>En esta oración, <em>semipermeable</em> significa que la membrana…"),
   [t("lets everything through", "deja pasar todo"), t("lets nothing through", "no deja pasar nada"), t("lets only some substances through", "deja pasar solo algunas sustancias"), t("is only half as thick as the wall", "tiene la mitad de grosor que la pared")], 2,
   {0: t("The sentence says it stops large molecules.", "La oración dice que detiene las moléculas grandes."), 1: t("It lets water through.", "Deja pasar el agua."), 3: t("Semi- means partly; here it describes what passes, not thickness.", "Semi- significa en parte; aquí describe lo que pasa, no el grosor.")},
   t("Semi- (partly) + permeable (lets through): it lets through only some substances.", "Semi- (en parte) + permeable (que deja pasar): solo deja pasar algunas sustancias."))}
{G(5, "SP.4.a", "2–3", t("<em>A student claims: “Plant cells do not need mitochondria, because chloroplasts give them all the energy they need.” In an experiment, a plant kept in total darkness for two days used oxygen and gave off carbon dioxide the whole time.</em><br>How does the evidence relate to the claim?", "<em>Un estudiante afirma: «Las células vegetales no necesitan mitocondrias, porque los cloroplastos les dan toda la energía que necesitan». En un experimento, una planta mantenida dos días en total oscuridad consumió oxígeno y liberó dióxido de carbono todo el tiempo.</em><br>¿Qué relación tiene la evidencia con la afirmación?"),
   [t("It supports the claim, because the plant stayed alive.", "La apoya, porque la planta siguió viva."), t("It challenges the claim: with no light, the plant still carried out cellular respiration, which happens in the mitochondria.", "La contradice: sin luz, la planta siguió haciendo la respiración celular, que ocurre en las mitocondrias."), t("It has nothing to do with the claim.", "No tiene relación con la afirmación."), t("It supports the claim, because chloroplasts make oxygen.", "La apoya, porque los cloroplastos producen oxígeno.")], 1,
   {0: t("Staying alive in the dark is the problem for the claim: what gave it energy?", "Seguir viva a oscuras es justo el problema: ¿qué le dio energía?"), 2: t("Using oxygen and giving off CO₂ is exactly what respiration does.", "Consumir oxígeno y liberar CO₂ es exactamente lo que hace la respiración."), 3: t("In the dark, it used oxygen; it did not make it.", "A oscuras consumió oxígeno; no lo produjo.")},
   t("Using O₂ and giving off CO₂ is respiration, done by mitochondria. Plant cells have them and use them day and night.", "Consumir O₂ y liberar CO₂ es la respiración, que hacen las mitocondrias. Las células vegetales las tienen y las usan día y noche."))}"""

    secciones = [
        ("s1", t("Cell theory and the evidence behind it", "La teoría celular y la evidencia que la sostiene"), s1),
        ("s2", t("Cell division: how the third statement comes true", "La división celular: cómo se cumple el tercer postulado"), s2),
        ("s3", t("Organelles and their jobs", "Los organelos y sus funciones"), s3),
        ("s4", t("Animal, plant, and prokaryotic cells", "Célula animal, célula vegetal y célula procariota"), s4),
        ("s5", t("The membrane and the concentration gradient", "La membrana y el gradiente de concentración"), s5),
        ("s6", t("Predicting what a solution does to a cell", "Predecir el efecto de una disolución"), s6),
        ("s7", t("Science reading", "Lectura científica"), s7),
        ("s8", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Label from memory.", "Rotule de memoria."), t("Copy the animal and plant cell diagrams without labels on a sheet of paper and label them from memory. Then check with the lesson.", "Copie sin rótulos los diagramas de célula animal y vegetal en una hoja y rotúlelos de memoria. Después compruébelos con la lección.")),
        (t("Predict and explain.", "Prediga y explique."), t("What happens to a cell placed in a hypertonic solution? Explain your reasoning in two sentences, not just the result.", "¿Qué le ocurre a una célula colocada en una disolución hipertónica? Explique su razonamiento en dos oraciones, no solo el resultado.")),
        (t("Order and imagine.", "Ordene e imagine."), t("Put the stages of mitosis in order and explain in one sentence what would happen if the DNA were copied after the sharing instead of before.", "Ordene las etapas de la mitosis y explique en una oración qué ocurriría si la duplicación del ADN sucediera después del reparto y no antes.")),
        (t("Take words apart.", "Descomponga palabras."), t("Break six terms from the lesson into roots and write the meaning you think they have before checking the glossary.", "Descomponga en raíces seis términos de la lección y escriba el significado que propone antes de consultar el glosario.")),
    ]
    Q = lambda en, es: t(en, es)
    quiz = [
        (Q("The organelle that holds the DNA and directs the cell’s activity is…", "El organelo que contiene el ADN y dirige la actividad de la célula es…"), [Q("the mitochondrion", "la mitocondria"), Q("the nucleus", "el núcleo"), Q("the ribosome", "el ribosoma"), Q("the vacuole", "la vacuola")], 1,
         {0: Q("The mitochondrion releases energy.", "La mitocondria libera energía."), 2: Q("The ribosome builds proteins.", "El ribosoma fabrica proteínas."), 3: Q("The vacuole stores water.", "La vacuola almacena agua.")}, Q("The nucleus is the office where the plans are kept.", "El núcleo es la oficina donde se guardan los planos.")),
        (Q("Ribosomes…", "Los ribosomas se encargan de…"), [Q("build proteins", "fabricar proteínas"), Q("store water", "almacenar agua"), Q("carry out photosynthesis", "realizar la fotosíntesis"), Q("make the cell stiff", "dar rigidez a la célula")], 0,
         {1: Q("That is the vacuole.", "Esa es la vacuola."), 2: Q("That is the chloroplast.", "Ese es el cloroplasto."), 3: Q("That is the cell wall.", "Esa es la pared celular.")}, Q("The ribosome is the assembly line for proteins.", "El ribosoma es la línea de montaje de las proteínas.")),
        (Q("If chloro- means green and -plast means formed body, the chloroplast must be…", "Sabiendo que cloro- significa verde y -plasto significa orgánulo, el cloroplasto debe ser…"), [Q("the organelle that stores chlorine", "el orgánulo que almacena clorato"), Q("the green organelle where photosynthesis happens", "el orgánulo verde donde ocurre la fotosíntesis"), Q("an inside transport network", "una red interna de transporte"), Q("the outer covering of the cell", "la envoltura externa de la célula")], 1,
         {0: Q("Chloro- here means green, not the chemical.", "Cloro- aquí significa verde, no el elemento químico."), 2: Q("That is the endoplasmic reticulum.", "Ese es el retículo endoplasmático."), 3: Q("That is the membrane or wall.", "Esa es la membrana o la pared.")}, Q("Green body: the chloroplast, where photosynthesis happens.", "Orgánulo verde: el cloroplasto, donde ocurre la fotosíntesis.")),
        (Q("The structure that controls what enters and leaves the cell is…", "La estructura que regula qué sustancias entran y salen de la célula es…"), [Q("the endoplasmic reticulum", "el retículo endoplasmático"), Q("the cell wall", "la pared celular"), Q("the cell membrane", "la membrana plasmática"), Q("the nucleolus", "el nucléolo")], 2,
         {0: Q("The reticulum moves things inside the cell.", "El retículo transporta por dentro."), 1: Q("The wall gives shape; it does not choose what passes.", "La pared da forma; no selecciona lo que pasa."), 3: Q("The nucleolus is inside the nucleus.", "El nucléolo está dentro del núcleo.")}, Q("The membrane is the door with access control.", "La membrana es la puerta con control de acceso.")),
        (Q("Before dividing by mitosis, the cell copies its DNA. If it did not…", "Antes de dividirse por mitosis, la célula duplica su ADN. Si no lo hiciera…"), [Q("each daughter cell would get half the instructions", "cada célula hija recibiría la mitad de las instrucciones"), Q("division would be faster", "la división sería más rápida"), Q("the daughter cells would be larger", "las células hijas serían más grandes"), Q("there would be no difference", "no habría ninguna diferencia")], 0,
         {1: Q("Speed is not the point.", "La velocidad no es lo importante."), 2: Q("Size is not the point.", "El tamaño no es lo importante."), 3: Q("Without the copy there is only one set.", "Sin la copia hay un solo juego.")}, Q("The copy guarantees a full set for each cell.", "La duplicación garantiza un juego completo para cada célula.")),
        (Q("A human cell with 46 chromosomes divides by mitosis. Each daughter cell will have…", "Una célula humana con 46 cromosomas se divide por mitosis. Cada célula hija tendrá…"), [Q("23 chromosomes", "23 cromosomas"), Q("92 chromosomes", "92 cromosomas"), Q("46 chromosomes", "46 cromosomas"), Q("a varying number", "un número variable")], 2,
         {0: Q("Half is meiosis.", "La mitad es la meiosis."), 1: Q("92 is the copied DNA before sharing.", "92 es el ADN duplicado antes del reparto."), 3: Q("Mitosis is exact.", "La mitosis es exacta.")}, Q("Mitosis keeps the number: 46.", "La mitosis conserva el número: 46.")),
        (Q("A cell has a cell wall, chloroplasts, and a large central vacuole. It is…", "Una célula posee pared celular, cloroplastos y una vacuola central grande. Se trata de una célula…"), [Q("an animal cell", "animal"), Q("a prokaryote", "procariota"), Q("a plant cell", "vegetal"), Q("a cell with no nucleus", "sin núcleo")], 2,
         {0: Q("Animal cells have none of those three.", "La célula animal no tiene ninguna de las tres."), 1: Q("Prokaryotes have no chloroplasts.", "Las procariotas no tienen cloroplastos."), 3: Q("Nothing says it has no nucleus.", "Nada indica que no tenga núcleo.")}, Q("Wall, chloroplasts, and central vacuole: a plant cell.", "Pared, cloroplastos y vacuola central: célula vegetal.")),
        (Q("The key difference between a prokaryotic and a eukaryotic cell is that the prokaryote…", "La diferencia esencial entre una célula procariota y una eucariota es que la procariota…"), [Q("has no DNA", "no tiene ADN"), Q("has no cell membrane", "no tiene membrana plasmática"), Q("is always many-celled", "es siempre pluricelular"), Q("does not keep its DNA inside a nucleus with its own covering", "no tiene su ADN encerrado en un núcleo con envoltura propia")], 3,
         {0: Q("Every cell has DNA.", "Toda célula tiene ADN."), 1: Q("Every cell has a membrane.", "Toda célula tiene membrana."), 2: Q("Prokaryotes are almost always one-celled.", "Las procariotas son casi siempre unicelulares.")}, Q("Pro-karyote: before the nucleus.", "Pro-cariota: antes del núcleo.")),
        (Q("Which structure do animal, plant, and bacterial cells share?", "¿Qué estructura comparten la célula animal, la vegetal y la bacteriana?"), [Q("The cell membrane", "La membrana plasmática"), Q("The chloroplast", "El cloroplasto"), Q("The central vacuole", "La vacuola central"), Q("The nucleus", "El núcleo")], 0,
         {1: Q("Animals and bacteria have none.", "Animales y bacterias no los tienen."), 2: Q("Only plants have one.", "Solo las plantas la tienen."), 3: Q("Bacteria have no nucleus.", "Las bacterias no tienen núcleo.")}, Q("Every cell has a membrane: it is what separates inside from outside.", "Toda célula tiene membrana: es lo que separa el dentro del fuera.")),
        (Q("In osmosis, water moves toward the side with…", "En la ósmosis, el agua se desplaza hacia el lado donde hay…"), [Q("less solute", "menos soluto"), Q("more solute", "más soluto"), Q("higher temperature", "mayor temperatura"), Q("less pressure", "menos presión")], 1,
         {0: Q("It is the other way: water follows the salt.", "Es al revés: el agua sigue a la sal."), 2: Q("Temperature is not what decides it.", "La temperatura no es lo que decide."), 3: Q("Think about the solute.", "Piense en el soluto.")}, Q("Water follows the salt: toward more solute.", "El agua sigue a la sal: hacia más soluto.")),
        (Q("Active transport differs from diffusion because it…", "El transporte activo se distingue de la difusión en que…"), [Q("moves only water", "solo mueve agua"), Q("happens only in plant cells", "ocurre únicamente en células vegetales"), Q("goes against the gradient and uses ATP", "va en contra del gradiente y consume ATP"), Q("is faster", "es más rápido")], 2,
         {0: Q("That is osmosis.", "Esa es la ósmosis."), 1: Q("It happens in all cells.", "Ocurre en todas las células."), 3: Q("Speed is not the difference.", "La velocidad no es la diferencia.")}, Q("Against the gradient, with energy (ATP).", "En contra del gradiente, con gasto de energía (ATP).")),
        (Q("A red blood cell is put in distilled water. You can predict that it will…", "Un glóbulo rojo se coloca en agua destilada. Cabe predecir que…"), [Q("lose water and shrink", "perderá agua y se arrugará"), Q("take in water, swell, and may burst", "absorberá agua, se hinchará y podrá romperse"), Q("not change", "no experimentará ningún cambio"), Q("make a cell wall", "fabricará una pared celular")], 1,
         {0: Q("That happens in a hypertonic solution.", "Eso ocurre en una hipertónica."), 2: Q("Distilled water has no salt: it is not isotonic.", "El agua destilada no tiene sal: no es isotónica."), 3: Q("Animal cells cannot.", "Las células animales no pueden.")}, Q("Hypotonic outside: water goes in, and with no wall the cell can burst.", "Exterior hipotónico: el agua entra y, sin pared, el glóbulo puede romperse.")),
        (Q("A plant cell in a very salty solution loses water. Unlike an animal cell, the plant cell…", "Una célula vegetal colocada en una disolución muy salada perderá agua. A diferencia de una célula animal, la vegetal…"), [Q("keeps its outer shape thanks to the cell wall", "conserva su forma exterior gracias a la pared celular"), Q("absorbs the salt to make up for it", "absorbe la sal para compensar"), Q("is not affected by osmosis", "no es afectada por la ósmosis"), Q("bursts right away", "se rompe de inmediato")], 0,
         {1: Q("Water moves, not salt.", "Se mueve el agua, no la sal."), 2: Q("It does lose water.", "Sí pierde agua."), 3: Q("Losing water does not make a cell burst.", "Perder agua no hace reventar.")}, Q("The wall keeps the shape; the inside shrinks away from it.", "La pared conserva la forma; el interior se separa de ella.")),
        (Q("An isotonic solution, compared with a cell, is one in which…", "Un medio isotónico respecto de una célula es aquel en el que…"), [Q("water only goes in", "el agua solo entra"), Q("water only goes out", "el agua solo sale"), Q("there is no solute at all", "no hay soluto alguno"), Q("as much water goes in as goes out, and the volume does not change", "entra tanta agua como sale y el volumen no cambia")], 3,
         {0: Q("That is hypotonic.", "Eso es hipotónico."), 1: Q("That is hypertonic.", "Eso es hipertónico."), 2: Q("That is distilled water, which is hypotonic.", "Eso es agua destilada, que es hipotónica.")}, Q("Iso- = equal.", "Iso- = igual.")),
    ]
    filas = [
        (t("Find organelles in a diagram", "Localiza organelos en un diagrama"), t("I find the main organelles and can tell right away whether the diagram is an animal or a plant cell.", "Localizo los organelos principales y reconozco de inmediato si el diagrama es de una célula animal o vegetal."), t("I find the largest ones, but I mix up the smaller ones.", "Localizo los más grandes, pero confundo los menores entre sí."), t("I cannot identify them on a diagram without labels.", "No los identifico sobre el diagrama sin rótulos.")),
        (t("Match structure with job", "Asocia estructura con función"), t("I match each organelle with its job and can explain why its structure fits the job.", "Asocio cada organelo con su función y explico por qué su estructura se ajusta a ella."), t("I match the best-known ones.", "Asocio los más conocidos."), t("I list names without jobs.", "Enumero nombres sin relacionarlos con ninguna función.")),
        (t("Explain transport with the gradient", "Explica el transporte con el gradiente"), t("I explain diffusion, osmosis, and active transport with the gradient and energy, and I state osmosis in terms of solute.", "Explico difusión, ósmosis y transporte activo con el gradiente y la energía, y formulo la ósmosis en términos de soluto."), t("I mention the gradient but do not tell passive from active transport.", "Menciono el gradiente, pero no distingo el transporte pasivo del activo."), t("I describe movement without mentioning concentration.", "Describo el movimiento sin mencionar la concentración.")),
        (t("Predict the effect of a solution", "Predice el efecto de una disolución"), t("I predict all three cases, explain them, and tell a cell with a wall from one without.", "Predigo los tres casos, los justifico y distingo la célula con pared de la que no la tiene."), t("I predict the hypertonic case, but not the other two.", "Predigo el caso hipertónico, pero no los otros dos."), t("I cannot predict the result, or I reverse it.", "No anticipo el resultado o lo invierto.")),
    ]
    cierre = "<p>" + t("This lesson left two things in place. One, an inventory of the cell: what is inside and what it is for. The other, the skill the test rewards above memory: <strong>predicting a result from a principle</strong>, here the concentration gradient.", "Esta lección dejó dos cosas instaladas. Una, el inventario de la célula: qué hay dentro y para qué sirve. Otra, la destreza que el examen premia por encima del recuerdo: <strong>predecir un resultado a partir de un principio</strong>, en este caso el gradiente de concentración.") + "</p><p>" + \
             t("Lesson 3.2 puts two of those organelles to work. The chloroplast and the mitochondrion stop being names on a list and become the two rooms where energy flows, with their overall equations and their matching relationship: what one makes is exactly what the other uses.", "La Lección 3.2 pone a trabajar dos de esos organelos. El cloroplasto y la mitocondria dejan de ser nombres de una lista para convertirse en las dos cámaras donde ocurre el flujo de la energía, con sus ecuaciones globales y su relación complementaria: lo que una produce es exactamente lo que la otra consume.") + "</p>"
    glosario = [
        (t("Cell theory", "Teoría celular"), t("All living things are made of cells; the cell is the basic unit of life; every cell comes from another cell.", "Todos los seres vivos están formados por células; la célula es la unidad básica de la vida; toda célula procede de otra.")),
        (t("Organelle", "Organelo"), t("A structure inside the cell with a special job.", "Estructura interna de la célula especializada en una tarea.")),
        (t("Chromosome", "Cromosoma"), t("DNA packed tightly so it can be shared when the cell divides.", "ADN empaquetado para poder repartirse cuando la célula se divide.")),
        (t("Mitosis", "Mitosis"), t("Cell division that makes two cells identical to the original.", "División celular que produce dos células idénticas a la original.")),
        (t("Prokaryote / eukaryote", "Procariota / eucariota"), t("A cell without a true nucleus / with a true nucleus.", "Célula sin núcleo verdadero / con núcleo verdadero.")),
        (t("Semipermeable", "Semipermeable"), t("Letting only some substances through.", "Que deja pasar solo algunas sustancias.")),
        (t("Gradient", "Gradiente"), t("A difference in concentration between two areas.", "Diferencia de concentración entre dos zonas.")),
        (t("Osmosis", "Ósmosis"), t("The movement of water across a membrane toward the side with more solute.", "Movimiento del agua a través de una membrana hacia el lado con más soluto.")),
        (t("Active transport", "Transporte activo"), t("Moving a substance against its gradient, using ATP.", "Movimiento de una sustancia en contra del gradiente, con gasto de ATP.")),
        (t("Hypotonic / isotonic / hypertonic", "Hipotónica / isotónica / hipertónica"), t("A solution with less / the same / more solute than the cell.", "Disolución con menos / el mismo / más soluto que la célula.")),
    ]
    estd = C.estandares(["SP.7.a", "SP.1.a", "SP.1.b", "SP.3.c"], ["L.d", "L.b"], base=["SP.4.a"])
    conexion = "<p>" + t("The content starts here. The first two topics gave you tools: how science is investigated, how it is read, and how data are handled. None of them belonged to one subject. From here on, the subject begins, and it starts with the area that weighs the most on the test: <strong>life science, about 40% of the questions</strong>.", "Comienza el contenido. Los dos primeros temas instalaron herramientas: cómo se investiga, cómo se lee ciencia y cómo se manejan los datos. Ninguna pertenecía a un contenido concreto. A partir de aquí empieza la materia, y lo hace por el dominio de mayor peso del examen: <strong>Ciencias de la vida, cerca del 40 % de las preguntas</strong>.") + "</p><p>" + \
               t("Everything you learned is still in use. In particular, this lesson’s vocabulary is built with the roots from Lesson 1.3: mito-, chloro-, -plast, endo-, and reticulum. If you kept them, you will hardly need to memorize any organelle name.", "Todo lo anterior sigue en uso. En particular, el vocabulario de esta lección se construye con las raíces trabajadas en la Lección 1.3: mito-, cloro-, -plasto, endo- y retículo. Quien las retuvo no tendrá que memorizar casi ningún nombre de organelo.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> build the vocabulary from the roots, not from a list. With each new organelle, first take the word apart, and only then check its job in the diagram.", "<strong>Cómo estudiar esta lección:</strong> el vocabulario se construye desde las raíces, no desde la lista. Ante cada organelo nuevo, descomponga primero el término y solo después confirme la función con el diagrama.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Every living thing is made of cells: what is inside one, how it divides, and what its membrane lets through.", "Todo ser vivo está hecho de células: qué hay dentro de una, cómo se divide y qué deja pasar su membrana."),
        ["SP.7 · " + t("Scientific theories", "Teorías científicas"), "SP.1 · " + t("Understanding science texts", "Comprender textos científicos")],
        [t("<strong>State</strong> the three statements of cell theory and the evidence behind each one.", "<strong>Enunciar</strong> los tres postulados de la teoría celular y la evidencia que condujo a cada uno."),
         t("<strong>Explain</strong> how mitosis makes the third statement come true, and why the DNA is copied before it is shared.", "<strong>Explicar</strong> cómo la mitosis da cumplimiento al tercer postulado y por qué el ADN se duplica antes del reparto."),
         t("<strong>Find</strong> the main organelles in a diagram and match each one with its job.", "<strong>Localizar</strong> los organelos principales en un diagrama y asociar cada uno con su función."),
         t("<strong>Tell apart</strong> animal and plant cells, and prokaryotic and eukaryotic cells.", "<strong>Distinguir</strong> la célula animal de la vegetal y la célula procariota de la eucariota."),
         t("<strong>Explain</strong> diffusion, osmosis, and active transport in terms of the concentration gradient.", "<strong>Explicar</strong> la difusión, la ósmosis y el transporte activo en términos de gradiente de concentración."),
         t("<strong>Predict</strong> what happens to a cell placed in a hypotonic, isotonic, or hypertonic solution.", "<strong>Predecir</strong> qué le ocurre a una célula colocada en una disolución hipotónica, isotónica o hipertónica.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("3-2", t("Photosynthesis and cellular respiration: how energy flows", "Fotosíntesis y respiración celular: el flujo de la energía")), glosario, P)


ORGANELOS = [
    (("Nucleus", "Núcleo"), ("Holds the DNA and directs the cell’s activity.", "Contiene el ADN y dirige la actividad de la célula."), ("The main office, where the plans are kept.", "La oficina de dirección, donde se guardan los planos.")),
    (("Mitochondrion", "Mitocondria"), ("Carries out cellular respiration and releases the energy in glucose.", "Realiza la respiración celular y libera la energía de la glucosa."), ("The power plant.", "La central eléctrica.")),
    (("Ribosome", "Ribosoma"), ("Builds proteins following the instructions in the DNA.", "Fabrica las proteínas siguiendo las instrucciones del ADN."), ("The assembly line.", "La línea de montaje.")),
    (("Endoplasmic reticulum", "Retículo endoplasmático"), ("Carries the substances the cell makes.", "Transporta las sustancias fabricadas por la célula."), ("The hallways and conveyor belts.", "Los pasillos y las cintas transportadoras.")),
    (("Chloroplast", "Cloroplasto"), ("Carries out photosynthesis. Only in plant cells and algae.", "Realiza la fotosíntesis. Solo en células vegetales y algas."), ("The solar panel that powers the factory.", "El panel solar que alimenta la fábrica.")),
    (("Cell membrane", "Membrana plasmática"), ("Controls what enters and leaves the cell.", "Regula qué entra y qué sale de la célula."), ("The door with access control.", "La puerta con control de acceso.")),
    (("Cell wall", "Pared celular"), ("Gives the cell stiffness and shape. Only in plants, fungi, and many bacteria.", "Da rigidez y forma. Solo en células vegetales, hongos y muchas bacterias."), ("The outer wall of the building.", "El muro exterior del edificio.")),
    (("Central vacuole", "Vacuola central"), ("Stores water and other substances, and keeps the pressure that holds the plant up.", "Almacena agua y sustancias, y mantiene la presión que sostiene la planta."), ("The water tank.", "El depósito de agua.")),
]


# ---------------------------------------------------------------- práctica
def banco_organelos():
    nombres = [t(*o[0]) for o in ORGANELOS]
    raices = {
        1: t("<em>mito-</em> (thread) + <em>-chondrion</em> (grain)", "<em>mito-</em> (hilo) + <em>-condria</em> (gránulo)"),
        2: t("<em>ribo-</em> (from RNA) + <em>-some</em> (body)", "<em>ribo-</em> (del ARN) + <em>-soma</em> (cuerpo)"),
        3: t("<em>reticulum</em> (small net) + <em>endo-</em> (inside) + <em>plasm</em>", "<em>retículo</em> (red pequeña) + <em>endo-</em> (dentro) + <em>plasma</em>"),
        4: t("<em>chloro-</em> (green) + <em>-plast</em> (formed body)", "<em>cloro-</em> (verde) + <em>-plasto</em> (orgánulo)"),
    }
    out = []
    rnd = random.Random(31)
    for i, o in enumerate(ORGANELOS):
        otros = [j for j in range(len(ORGANELOS)) if j != i]
        def item(enun, k_ok, exp):
            ds = rnd.sample(otros, 3)
            ops = [nombres[k_ok]] + [nombres[d] for d in ds]
            return {"enun": enun, "ops": ops, "ok": 0, "pista": t("Think of the factory: what does each part do?", "Piense en la fábrica: ¿qué hace cada parte?"), "exp": exp}
        out.append(item(t("Which organelle does this job?", "¿Qué organelo realiza esta función?") + "<br><strong>" + t(*o[1]) + "</strong>", i, f"<strong>{nombres[i]}.</strong> {t(*o[2])}"))
        out.append(item(t("In the cell-as-a-factory comparison, which organelle is…", "En la analogía de la fábrica, ¿qué organelo es…") + "<br><strong>" + t(*o[2]) + "</strong>", i, f"<strong>{nombres[i]}:</strong> {t(*o[1])}"))
        if i in raices:
            out.append(item(t("Which organelle’s name is built from these roots?", "¿Qué organelo tiene un nombre formado con estas raíces?") + "<br><strong>" + raices[i] + "</strong>", i, f"<strong>{nombres[i]}:</strong> {t(*o[1])}"))
    return out


def ordenes_mitosis():
    return [
        {"titulo": t("Cell division · What happens", "División celular · Lo que ocurre"),
         "intro": t("Put what happens during cell division in order, from the start to two new cells. Use the ▲ and ▼ buttons.", "Ordene lo que ocurre durante la división celular, desde el principio hasta las dos células nuevas. Use los botones ▲ y ▼."),
         "pasos": [t("The cell grows and copies all of its DNA.", "La célula crece y duplica todo su ADN."),
                   t("The copied DNA packs tightly and the chromosomes become visible.", "El ADN duplicado se compacta y los cromosomas se hacen visibles."),
                   t("The chromosomes line up across the middle of the cell.", "Los cromosomas se alinean en el plano central de la célula."),
                   t("The copies of each chromosome pull apart to opposite ends.", "Las copias de cada cromosoma se separan hacia polos opuestos."),
                   t("Two nuclei form and the cytoplasm splits into two cells.", "Se forman dos núcleos y el citoplasma se divide en dos células.")],
         "inicio": [3, 0, 4, 2, 1],
         "cons": {"1>0": t("You packed the DNA before copying it. Only DNA that has been copied can be shared so each cell gets a full set.", "Compactó el ADN antes de duplicarlo. Solo el ADN ya duplicado puede repartirse de modo que cada célula reciba un juego completo."),
                  "3>2": t("You separated the copies before lining them up. Lining up first is what makes the sharing exact.", "Separó las copias antes de alinearlas. La alineación previa es la que hace que el reparto sea exacto."),
                  "4>3": t("You split the cell before the copies had moved apart: one cell could end up with both copies of a chromosome.", "Dividió la célula antes de que se separaran las copias: una célula podría quedarse con las dos copias de un cromosoma."),
                  "3>0": t("You shared the chromosomes before copying them: each cell would get half the instructions.", "Repartió los cromosomas antes de duplicarlos: cada célula recibiría la mitad de las instrucciones.")},
         "general": t("Copy, pack, line up, separate, split: each step needs the one before.", "Duplicar, compactar, alinear, separar y dividir: cada paso necesita el anterior.")},
        {"titulo": t("Cell division · The names", "División celular · Los nombres"),
         "intro": t("Now put the names of the stages in order.", "Ahora ordene los nombres de las etapas."),
         "pasos": [t("Interphase: the DNA is copied", "Interfase: se duplica el ADN"), t("Prophase: the chromosomes become visible", "Profase: los cromosomas se hacen visibles"),
                   t("Metaphase: they line up in the middle", "Metafase: se alinean en el centro"), t("Anaphase: the copies separate", "Anafase: las copias se separan"),
                   t("Telophase and cytokinesis: two cells", "Telofase y citocinesis: dos células")],
         "inicio": [2, 4, 0, 3, 1],
         "cons": {"2>1": t("Metaphase comes after prophase: the chromosomes must be visible and packed before they can line up.", "La metafase va después de la profase: los cromosomas tienen que estar compactados antes de alinearse."),
                  "3>2": t("Anaphase comes after metaphase: first line up, then separate. The initials P-M-A-T help you remember the order.", "La anafase va después de la metafase: primero alinear, después separar. Las iniciales P-M-A-T ayudan a recordar el orden."),
                  "1>0": t("Interphase comes first: the DNA has to be copied before anything else.", "La interfase va primero: el ADN tiene que duplicarse antes de todo.")},
         "general": t("Interphase, then P-M-A-T: prophase, metaphase, anaphase, telophase.", "Interfase y después P-M-A-T: profase, metafase, anafase y telofase.")},
    ]


def clasif_celulas():
    G = [t("Animal cell", "Célula animal"), t("Plant cell", "Célula vegetal"), t("Bacterium (prokaryote)", "Bacteria (procariota)")]
    PA = t("Nucleus, but no wall and no chloroplasts?", "¿Núcleo, pero sin pared ni cloroplastos?")
    PV = t("Look for chloroplasts or a large central vacuole.", "Busque cloroplastos o una vacuola central grande.")
    PB = t("No nucleus: the DNA floats in the cytoplasm.", "Sin núcleo: el ADN flota en el citoplasma.")
    def item(tit, piezas, extra):
        return {"titulo": tit, "intro": t("Read each description and decide what kind of cell it is.", "Lea cada descripción y decida de qué tipo de célula se trata."), "grupos": G,
                "etiqueta": t("Kind of cell:", "Tipo de célula:"), "piezas": [{"t": a, "v": v, "pista": [PA, PV, PB][v]} for a, v in piezas], "extra": extra}
    return [
        item(t("Set 1", "Grupo 1"), [
            (t("A cell from the leaf of a bean plant, with green chloroplasts.", "Una célula de la hoja de una planta de frijol, con cloroplastos verdes."), 1),
            (t("A muscle cell with many mitochondria and a nucleus, but no wall.", "Una célula muscular con muchas mitocondrias y un núcleo, pero sin pared."), 0),
            (t("A tiny cell from yogurt, with its DNA loose in the cytoplasm.", "Una célula diminuta del yogur, con su ADN suelto en el citoplasma."), 2),
            (t("A cell with a nucleus, a stiff wall, and a large central vacuole full of water.", "Una célula con núcleo, una pared rígida y una vacuola central grande llena de agua."), 1),
            (t("A white blood cell that changes shape to surround germs.", "Un glóbulo blanco que cambia de forma para rodear a los microbios."), 0)],
         t("A flexible shape points to an animal cell; a fixed shape with a wall and vacuole, to a plant cell.", "Una forma flexible apunta a célula animal; una forma fija con pared y vacuola, a célula vegetal.")),
        item(t("Set 2", "Grupo 2"), [
            (t("A cell about 1 × 10⁻⁶ m long, with no organelles surrounded by a membrane.", "Una célula de unos 1 × 10⁻⁶ m, sin organelos rodeados de membrana."), 2),
            (t("A nerve cell with a long extension and a nucleus.", "Una neurona con una prolongación larga y un núcleo."), 0),
            (t("A cell from the green stem of a plant, rectangular, with chloroplasts.", "Una célula del tallo verde de una planta, rectangular, con cloroplastos."), 1),
            (t("A cell that causes strep throat, with no nucleus.", "Una célula que causa una infección de garganta, sin núcleo."), 2),
            (t("A skin cell with a nucleus and mitochondria, and no chloroplasts or wall.", "Una célula de la piel con núcleo y mitocondrias, sin cloroplastos ni pared."), 0)],
         t("Size and the lack of a nucleus give away the bacteria.", "El tamaño y la falta de núcleo delatan a las bacterias.")),
    ]


def banco_transporte():
    O = [t("Diffusion", "Difusión"), t("Osmosis", "Ósmosis"), t("Active transport", "Transporte activo")]
    P = {0: t("Diffusion: a dissolved substance spreads from more to less, with no energy.", "Difusión: una sustancia disuelta se reparte de más a menos, sin energía."),
         1: t("Osmosis: only water moves, toward more solute.", "Ósmosis: solo se mueve el agua, hacia más soluto."),
         2: t("Active transport: from less to more, spending ATP.", "Transporte activo: de menos a más, con gasto de ATP.")}
    d = [
        (t("Oxygen passes from the air in the lungs, where there is a lot, into the blood, where there is less.", "El oxígeno pasa del aire de los pulmones, donde hay mucho, a la sangre, donde hay menos."), 0, t("From more to less, no energy: diffusion.", "De más a menos y sin energía: difusión.")),
        (t("A wilted lettuce leaf gets crisp again after an hour in fresh water.", "Una hoja de lechuga marchita recupera su firmeza tras una hora en agua dulce."), 1, t("Water went into the cells, where there is more solute: osmosis.", "El agua entró en las células, donde hay más soluto: ósmosis.")),
        (t("Root cells take in minerals from the soil even though there are already more minerals inside the root than in the soil.", "Las células de la raíz absorben minerales del suelo aunque ya hay más minerales dentro de la raíz que en el suelo."), 2, t("Against the gradient: it costs ATP.", "En contra del gradiente: cuesta ATP.")),
        (t("A drop of food coloring spreads through a glass of still water.", "Una gota de colorante se reparte por un vaso de agua quieta."), 0, t("The coloring spreads from more to less on its own.", "El colorante se reparte de más a menos por sí solo.")),
        (t("Slices of cucumber in salty water give off water and go soft.", "Rodajas de pepino en agua salada sueltan agua y se ablandan."), 1, t("Water left the cells toward the salt: osmosis.", "El agua salió de las células hacia la sal: ósmosis.")),
        (t("Nerve cells pump sodium out, even though there is already much more sodium outside than inside.", "Las neuronas expulsan sodio aunque fuera ya hay mucho más sodio que dentro."), 2, t("Pumping against the gradient needs energy.", "Bombear en contra del gradiente requiere energía.")),
        (t("Carbon dioxide made in a cell passes into the blood, where there is less of it.", "El dióxido de carbono producido en una célula pasa a la sangre, donde hay menos."), 0, t("From more to less, on its own.", "De más a menos, por sí solo.")),
        (t("Raisins left in water swell up.", "Unas pasas dejadas en agua se hinchan."), 1, t("Water went into the raisins, which are full of sugar.", "El agua entró en las pasas, que están llenas de azúcar.")),
    ]
    return [{"enun": t("Which mechanism is at work?", "¿Qué mecanismo actúa?") + "<br><strong>" + x + "</strong>", "ops": O, "ok": k, "enOrden": True,
             "pistas": {i: P[i] for i in range(3) if i != k}, "exp": f"<strong>{O[k]}.</strong> {e}"} for x, k, e in d]


def banco_prediccion():
    """Casos de ósmosis generados: tipo de célula × relación de concentraciones × pregunta."""
    rnd = random.Random(7)
    CEL = [(t("a red blood cell", "un glóbulo rojo"), "a"), (t("a cell from an onion", "una célula de cebolla"), "v"), (t("a cheek cell", "una célula de la mejilla"), "a"), (t("a cell from a lettuce leaf", "una célula de hoja de lechuga"), "v")]
    TIPOS = [t("Hypotonic", "Hipotónica"), t("Isotonic", "Isotónica"), t("Hypertonic", "Hipertónica")]
    AGUA = [t("More water goes in than goes out.", "Entra más agua de la que sale."), t("As much water goes in as goes out.", "Entra tanta agua como sale."), t("More water goes out than goes in.", "Sale más agua de la que entra.")]
    RES = {"a": [t("It swells and may burst.", "Se hincha y puede reventar."), t("It does not change.", "No cambia."), t("It loses water and shrinks.", "Pierde agua y se arruga."), t("It becomes firm, held by its wall.", "Queda firme, sostenida por su pared.")],
           "v": [t("It becomes firm, held by its wall.", "Queda firme, sostenida por su pared."), t("It does not change.", "No cambia."), t("It loses water and its contents pull away from the wall.", "Pierde agua y su contenido se separa de la pared."), t("It swells and bursts.", "Se hincha y revienta.")]}
    out = []
    for cel, k in CEL:
        for rel in range(3):
            for q in range(3):
                dentro = rnd.choice([0.9, 1, 1.5, 2])
                fuera = {0: rnd.choice([0, round(dentro / 3, 1), 0.1]), 1: dentro, 2: rnd.choice([3, 5, 8, 10])}[rel]
                fmt = lambda x: (str(x).rstrip("0").rstrip(".") if isinstance(x, float) else str(x))
                esc = t(f"The inside of {cel} has <strong>{fmt(dentro)}%</strong> dissolved substances. It is placed in a solution with <strong>{fmt(fuera)}%</strong>.",
                        f"El interior de {cel} tiene <strong>{fmt(dentro)} %</strong> de sustancias disueltas. Se coloca en una disolución con <strong>{fmt(fuera)} %</strong>.")
                comp = [t("less solute outside than inside", "menos soluto fuera que dentro"), t("the same solute inside and outside", "el mismo soluto dentro y fuera"), t("more solute outside than inside", "más soluto fuera que dentro")][rel]
                if q == 0:
                    pre, ops, ok = t("Compared with the cell, the solution is…", "Respecto de la célula, la disolución es…"), TIPOS, rel
                    exp = t(f"There is {comp}: {TIPOS[rel].lower()}.", f"Hay {comp}: {TIPOS[rel].lower()}.")
                elif q == 1:
                    pre, ops, ok = t("Which way does the water move?", "¿Hacia dónde se mueve el agua?"), AGUA, rel
                    exp = t(f"There is {comp}, and water follows the solute. {AGUA[rel]}", f"Hay {comp}, y el agua sigue al soluto. {AGUA[rel]}")
                else:
                    pre, ops, ok = t("What happens to the cell?", "¿Qué le pasa a la célula?"), RES[k], rel
                    pared = t(" A plant cell has a wall that holds against the pressure." if k == "v" else " An animal cell has no wall to hold it.", " La célula vegetal tiene una pared que resiste la presión." if k == "v" else " La célula animal no tiene pared que la contenga.")
                    exp = t(f"There is {comp}. {AGUA[rel]}", f"Hay {comp}. {AGUA[rel]}") + pared
                out.append({"enun": f"<p>{esc}</p><p><strong>{pre}</strong></p>", "ops": ops, "ok": ok, "enOrden": True,
                            "pista": t("Compare the two percentages first: where is there more solute? Water moves toward it.", "Compare primero los dos porcentajes: ¿dónde hay más soluto? El agua se mueve hacia allí."), "exp": f"<strong>{ops[ok]}</strong> {exp}"})
    return out


def banco_raices():
    d = [
        (t("<em>Chromosome</em>: chromo- (color) + -some (body). Why that name?", "<em>Cromosoma</em>: cromo- (color) + -soma (cuerpo). ¿Por qué ese nombre?"),
         [t("They soaked up dyes and showed up as colored bodies under the microscope.", "Se teñían con los colorantes y se veían como cuerpos coloreados al microscopio."), t("They give the cell its color.", "Dan color a la célula."), t("They are only in colored cells.", "Solo están en células de color.")], 0,
         t("The name comes from how they were first seen: bodies that took the color of the dye.", "El nombre viene de cómo se vieron por primera vez: cuerpos que tomaban el color del tinte.")),
        (t("<em>Eukaryote</em>: eu- (true) + -karyote (nucleus). A eukaryotic cell…", "<em>Eucariota</em>: eu- (verdadero) + -cariota (núcleo). Una célula eucariota…"),
         [t("has a true nucleus", "tiene núcleo verdadero"), t("has no nucleus", "no tiene núcleo"), t("has two nuclei", "tiene dos núcleos")], 0, t("Eu- = true: a cell with a true nucleus.", "Eu- = verdadero: célula con núcleo verdadero.")),
        (t("<em>Prokaryote</em>: pro- (before) + -karyote (nucleus). A prokaryotic cell…", "<em>Procariota</em>: pro- (antes) + -cariota (núcleo). Una célula procariota…"),
         [t("has a very large nucleus", "tiene un núcleo muy grande"), t("does not have a true nucleus", "no tiene núcleo verdadero"), t("is older than the nucleus of a plant", "es más antigua que el núcleo de una planta")], 1, t("“Before the nucleus”: a cell that does not have one.", "«Antes del núcleo»: una célula que no lo tiene.")),
        (t("<em>Hypertonic</em>: hyper- means…", "<em>Hipertónica</em>: hiper- significa…"),
         [t("below", "por debajo"), t("equal", "igual"), t("above", "por encima")], 2, t("Hyper- = above: more solute than the cell, as in <em>hypertension</em>.", "Hiper- = por encima: más soluto que la célula, como en <em>hipertensión</em>.")),
        (t("<em>Hypotonic</em>: hypo- means…", "<em>Hipotónica</em>: hipo- significa…"),
         [t("below", "por debajo"), t("equal", "igual"), t("above", "por encima")], 0, t("Hypo- = below: less solute than the cell, as in <em>hypothermia</em>.", "Hipo- = por debajo: menos soluto que la célula, como en <em>hipotermia</em>.")),
        (t("<em>Cytoplasm</em>: cyto- means…", "<em>Citoplasma</em>: cito- significa…"),
         [t("cell", "célula"), t("water", "agua"), t("green", "verde")], 0, t("Cyto- = cell: the content of the cell. It also appears in <em>cytokinesis</em>, the splitting of the cell.", "Cito- = célula: el contenido de la célula. También aparece en <em>citocinesis</em>, la división de la célula.")),
        (t("<em>Endoplasmic</em>: endo- means…", "<em>Endoplasmático</em>: endo- significa…"),
         [t("outside", "fuera"), t("inside", "dentro"), t("around", "alrededor")], 1, t("Endo- = inside: a network inside the cytoplasm.", "Endo- = dentro: una red dentro del citoplasma.")),
        (t("<em>Semipermeable</em>: semi- means…", "<em>Semipermeable</em>: semi- significa…"),
         [t("completely", "completamente"), t("partly", "en parte"), t("never", "nunca")], 1, t("Semi- = partly: it lets only some substances through.", "Semi- = en parte: deja pasar solo algunas sustancias.")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Break the word into its parts.", "Descomponga la palabra en sus partes."), "exp": e} for q, o, k, e in d]


def practica():
    A = {"en": ["organelles", "mitosis", "cell-types", "transport", "predict", "roots"], "es": ["organelos", "mitosis", "tipos-de-celula", "transporte", "predecir", "raices"]}[C.L]
    mods = [
        (A[0], t("Organelles and their jobs", "Organelos y funciones"), C.om("m1", t("From the job, the factory role, or the roots, name the organelle.", "Por la función, el papel en la fábrica o las raíces, nombre el organelo."))),
        (A[1], t("Put mitosis in order", "Ordene la mitosis"), C.orden("m2", t("First what happens, then the names of the stages.", "Primero lo que ocurre, después los nombres de las etapas."))),
        (A[2], t("Animal, plant, or bacterium?", "¿Animal, vegetal o bacteria?"), C.clasifica("m3", t("Choose the kind of cell for each description.", "Elija el tipo de célula de cada descripción."))),
        (A[3], t("Diffusion, osmosis, or active transport?", "¿Difusión, ósmosis o transporte activo?"), C.om("m4", t("Ask two things: what moves, and does it go with the gradient or against it?", "Pregúntese dos cosas: qué se mueve, y si va a favor o en contra del gradiente."))),
        (A[4], t("Predict what the cell does", "Prediga qué le pasa a la célula"), C.om("m5", t("Thirty-six cases. Compare the solute inside and outside first.", "Treinta y seis casos. Compare primero el soluto de dentro y de fuera."))),
        (A[5], t("Roots of cell words", "Raíces de las palabras de la célula"), C.om("m6", t("Take the word apart before you answer.", "Descomponga la palabra antes de responder."))),
    ]
    js = (C.js_datos("ORG", banco_organelos()) + C.js_datos("MIT", ordenes_mitosis()) + C.js_datos("CEL", clasif_celulas()) +
          C.js_datos("TRA", banco_transporte()) + C.js_datos("PRE", banco_prediccion()) + C.js_datos("RAI", banco_raices()) +
          'creaBanco("m1", ORG);\ncreaOrden("m2", MIT);\ncreaClasifica("m3", CEL);\ncreaBanco("m4", TRA);\ncreaBanco("m5", PRE);\ncreaBanco("m6", RAI);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
