"""LearnGED · Ciencias · Lección 4.2 · Meiosis, cuadros de Punnett y probabilidad genética (EN/ES).
Fuente: clases_ciencias/leccion_4-2.html (diagramas en tools/svg/4-2_*.svg) y los interactivos
ciencias/meiosis, ciencias/punnett_interactivo y ciencias/arbol_probabilidad.
Uso: python3 tools/build_sci_4_2.py
"""
import os, sys, random
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "4-2"


def titulo():
    return t("Meiosis, Punnett squares, and genetic probability", "Meiosis, cuadros de Punnett y probabilidad genética")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


def svg_meiosis():
    return C.svg_orig("4-2_0", {"Mitosis": "Mitosis", "Meiosis": "Meiosis", "2 células · mismo número de cromosomas": "2 cells · same number of chromosomes", "para crecer y reparar": "for growth and repair",
                                 "4 células · la mitad de los cromosomas": "4 cells · half the chromosomes", "son los gametos": "they are the sex cells"},
                       "Comparison of mitosis and meiosis. In mitosis, a cell with two chromosomes divides once and makes two daughter cells, each with two chromosomes, identical to the original. In meiosis, the same cell divides twice and makes four cells, each with only one chromosome, that is, with half. The cells from mitosis are for growth and repair; the cells from meiosis are the sex cells.")


def svg_arbol():
    tr = {k: k for k in ("I", "II", "III", "I-1", "I-2", "II-1", "II-2", "II-3", "III-1")}
    tr.update({"varón": "male", "mujer": "female", "manifiesta el rasgo": "shows the trait", "no lo manifiesta": "does not show it"})
    return C.svg_orig("4-2_1", tr, "Family tree (pedigree) of three generations. In the first generation, a man who does not show the trait has children with a woman who does not show it. They have two children: a son who shows the trait and a daughter who does not. That daughter has a child with a man who does not show the trait, and they have a son who shows the trait. Since the trait comes back in the third generation through people who do not show it, the woman in the second generation must be a carrier.")


def punnett(cab, filas, desc, nota=None):
    """cab: gametos de las columnas; filas: [(gameto, [casillas])]."""
    th = "".join(f'<th scope="col">{c}</th>' for c in cab)
    tr = "".join(f'<tr><th scope="row">{g}</th>' + "".join(f"<td>{x}</td>" for x in xs) + "</tr>" for g, xs in filas)
    return (f'<table class="cuaderno" style="max-width:{140 + 110 * len(cab)}px;margin:10px auto;text-align:center"><caption class="cap-oculto">{desc}</caption>'
            f'<thead><tr><th scope="col">{t("Sex cells", "Gametos")}</th>{th}</tr></thead><tbody>{tr}</tbody></table>' + (f'<p style="text-align:center">{nota}</p>' if nota else ""))


def cruza(p1, p2):
    g1, g2 = [p1[0], p1[1]], [p2[0], p2[1]]
    return g1, g2, [["".join(sorted(a + b, key=lambda c: (c.lower(), c.islower()))) for a in g1] for b in g2]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Start with a math problem. A human cell has 46 chromosomes. If the egg and the sperm each carried all 46, together they would have 92. The children of that generation would make sex cells with 92, and their grandchildren would have 184. In a few generations the number would be absurd.", "Empecemos por un problema aritmético. Una célula humana tiene 46 cromosomas. Si el óvulo y el espermatozoide llevaran cada uno los 46, al unirse resultarían 92. Los hijos de esa generación producirían gametos de 92 y sus nietos tendrían 184. En pocas generaciones el número sería absurdo.")}</p>
<p>{t("The solution is <strong>meiosis</strong>: a division that makes cells with half the chromosomes. Human sex cells have 23. When two of them join, fertilization brings the number back to 46, and it stays the same generation after generation.", "La solución es la <strong>meiosis</strong>: una división que produce células con la mitad de los cromosomas. Los gametos humanos tienen 23. Al unirse dos de ellos, la fecundación restaura los 46 y el número se mantiene constante generación tras generación.")}</p>
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>Meiosis</strong> comes from the Greek <em>meíosis</em>, making smaller: the name tells you the result, a division that reduces. <strong>Mitosis</strong> comes from <em>mitos</em>, thread, for how the chromosomes look as they divide, and says nothing about the number, because it does not change it. <strong>Gamete</strong> (sex cell) comes from the Greek for “husband or wife”: the cell meant to join another. And <strong>diploid</strong> and <strong>haploid</strong> share the root {R('-ploid')}, fold or set: {R('di-')} is two sets of chromosomes, 46 in humans; {R('haplo-')} is one set, 23.", f"<strong>Meiosis</strong> viene del griego <em>meíosis</em>, disminución, de la misma familia que <em>menos</em>. El nombre anuncia el resultado: una división que reduce. Frente a ella, <strong>mitosis</strong> viene de <em>mitos</em>, hilo, por el aspecto de los cromosomas al dividirse, y no dice nada sobre el número, porque no lo cambia. <strong>Gameto</strong> procede del griego para «esposo o esposa»: la célula destinada a unirse con otra. Y <strong>diploide</strong> y <strong>haploide</strong> comparten la raíz {R('-ploide')}, pliegue o juego: {R('di-')} es dos juegos de cromosomas, 46 en el ser humano; {R('haplo-')} es uno solo, 23.")}</p>
{svg_meiosis()}
{C.tabla(t("Mitosis and meiosis compared: divisions, cells made, chromosomes, genetic likeness, and purpose", "Comparación entre mitosis y meiosis según divisiones, células resultantes, cromosomas, semejanza genética y finalidad"),
 [t("Feature", "Aspecto"), "Mitosis", "Meiosis"],
 [[t("Divisions", "Divisiones"), t("One.", "Una."), t("Two in a row.", "Dos seguidas.")],
  [t("Cells made", "Células resultantes"), t("Two.", "Dos."), t("Four.", "Cuatro.")],
  [t("Chromosomes in each", "Cromosomas de cada una"), t("The same as the original: 46 in humans.", "Los mismos que la original: 46 en el ser humano."), t("Half: 23 in humans.", "La mitad: 23 en el ser humano.")],
  [t("Genetic likeness", "Semejanza genética"), t("Identical to each other and to the original.", "Idénticas entre sí y a la original."), t("Different from each other: each gets a different mix.", "Distintas entre sí: cada una recibe una combinación diferente.")],
  [t("What it is for", "Para qué sirve"), t("Growing, repairing, and replacing tissue.", "Crecer, reparar y reemplazar tejidos."), t("Making eggs and sperm.", "Formar óvulos y espermatozoides.")]])}
{C.caja("tip", t("The key to everything that follows", "La clave de todo lo que sigue"), "<p>" + t("Since each sex cell carries one set of chromosomes, it also carries <strong>one allele of each gene</strong>. That is why, in the Punnett square below, each parent gives one letter per box and not the two it has. The square is not an arbitrary convention: it is the sharing done by meiosis, drawn.", "Como cada gameto lleva un solo juego de cromosomas, lleva también <strong>un solo alelo de cada gen</strong>. Por eso, en el cuadro de Punnett que se construirá a continuación, cada progenitor aporta una sola letra por casilla y no las dos que posee. El cuadro no es una convención arbitraria: es el reparto que hace la meiosis, dibujado.") + "</p>")}
{P(t("Try it 1 · An egg cell", "Pruebe 1 · Un óvulo"), t("A human egg cell has…", "Un óvulo humano contiene…"), [t("46 chromosomes", "46 cromosomas"), t("23 chromosomes", "23 cromosomas"), t("92 chromosomes", "92 cromosomas")], 1,
   {0: t("46 is a body cell. Sex cells have half.", "46 es una célula del cuerpo. Los gametos tienen la mitad."), 2: t("92 is the problem meiosis avoids.", "92 es justo el problema que evita la meiosis.")},
   t("Meiosis halves the number: 23.", "La meiosis reduce a la mitad: 23."))}
{P(t("Try it 2 · One letter per box", "Pruebe 2 · Una letra por casilla"), t("In a Punnett square, each parent gives one allele per box because…", "En un cuadro de Punnett cada progenitor aporta un solo alelo por casilla porque…"),
   [t("it is a writing convention", "es una convención de escritura"), t("the other allele is lost", "el otro alelo se pierde"), t("meiosis puts one allele of each gene in each sex cell", "la meiosis reparte un solo alelo de cada gen a cada gameto")], 2,
   {0: t("It is not just a convention: it is what meiosis does.", "No es solo una convención: es lo que hace la meiosis."), 1: t("It is not lost; it goes to another sex cell.", "No se pierde; va a otro gameto.")},
   t("One set of chromosomes per sex cell = one allele per gene.", "Un juego de cromosomas por gameto = un alelo por gen."))}
{C.enlace(N, anc("mitosis-meiosis", "mitosis-meiosis"), t("mitosis or meiosis?", "¿mitosis o meiosis?"), t("Sort each feature into the right kind of division.", "Coloque cada característica en el tipo de división que le corresponde."))}"""

    s2 = f"""<p>{t("Each gene can come in different versions called <strong>alleles</strong>. A person has two alleles of each gene: one from the father and one from the mother. They are written with letters: a capital letter for the dominant allele and a small letter for the recessive one.", "Cada gen puede presentarse en versiones distintas llamadas <strong>alelos</strong>. Una persona tiene dos alelos de cada gen: uno del padre y otro de la madre. Se representan con letras, mayúscula para el dominante y minúscula para el recesivo.")}</p>
{C.tabla(t("Basic genetics terms, what they mean, and an example with flower color", "Términos básicos de la genética con su definición y un ejemplo aplicado al color de la flor"),
 [t("Term", "Término"), t("What it means", "Qué significa"), t("Example", "Ejemplo")],
 [[t("Genotype", "Genotipo"), t("The two alleles the individual has.", "Los dos alelos que el individuo posee."), t("AA, Aa, or aa.", "AA, Aa o aa.")],
  [t("Phenotype", "Fenotipo"), t("The trait that shows and can be observed.", "La característica que se manifiesta y puede observarse."), t("Purple flower or white flower.", "Flor morada o flor blanca.")],
  [t("Dominant allele", "Alelo dominante"), t("Shows with just one copy. Written as a capital letter.", "Se manifiesta con una sola copia. Se escribe en mayúscula."), t("A, the purple-flower allele.", "A, el alelo de flor morada.")],
  [t("Recessive allele", "Alelo recesivo"), t("Shows only if both copies are present. Small letter.", "Solo se manifiesta si están presentes las dos copias. Minúscula."), t("a, the white-flower allele.", "a, el alelo de flor blanca.")],
  [t("Homozygous", "Homocigoto"), t("The two alleles are the same.", "Los dos alelos son iguales."), t("AA or aa.", "AA o aa.")],
  [t("Heterozygous", "Heterocigoto"), t("The two alleles are different. Also called a carrier.", "Los dos alelos son distintos. También se le llama portador."), t("Aa: purple flower, but it carries the white allele.", "Aa: flor morada, pero lleva el alelo blanco.")]])}
{C.caja("ojo", t("Different genotypes, same phenotype", "Genotipos distintos, mismo fenotipo"), "<p>" + t("A flower with genotype AA and one with Aa are both purple. Looking at them, you cannot tell them apart, and yet they pass different things to their offspring. The test uses this all the time: it asks for the genotype when the phenotype is not enough to work it out, and that is where the family tree comes in.", "Una flor con genotipo AA y otra con genotipo Aa son las dos moradas. Mirándolas no hay manera de distinguirlas, y sin embargo transmiten cosas distintas a su descendencia. El examen aprovecha esa asimetría constantemente: pregunta por el genotipo cuando el fenotipo no basta para deducirlo, y ahí es donde entra el árbol genealógico.") + "</p>")}
{P(t("Try it 3 · Genotype or phenotype?", "Pruebe 3 · ¿Genotipo o fenotipo?"), t("“White flower” describes the plant’s…", "«Flor blanca» describe el… de la planta."),
   [t("phenotype", "fenotipo"), t("genotype", "genotipo"), t("allele", "alelo")], 0,
   {1: t("The genotype is the letters, such as aa.", "El genotipo son las letras, como aa."), 2: t("An allele is one version of the gene, written as a letter.", "Un alelo es una versión del gen, escrita como letra.")},
   t("What you can see is the phenotype.", "Lo que se ve es el fenotipo."))}"""

    _, _, c = cruza("Aa", "Aa")
    s3 = f"""<p>{t("A Punnett square crosses the possible sex cells of one parent with those of the other. Each box is one possible combination in the offspring, and all the boxes are equally likely.", "Un cuadro de Punnett cruza los gametos posibles de un progenitor con los del otro. Cada casilla es una combinación posible en la descendencia, y todas tienen la misma probabilidad.")}</p>
{C.ejemplo(t("Example 1 · Crossing two heterozygous plants", "Ejemplo 1 · Cruce de dos heterocigotos"),
 [("", t("Two purple-flowered heterozygous plants are crossed: Aa × Aa. By meiosis, each one makes sex cells with A and sex cells with a.", "Se cruzan dos plantas de flor morada heterocigotas: Aa × Aa. Cada una produce, por meiosis, gametos con A y gametos con a."))])}
{punnett(["A", "a"], [("A", c[0]), ("a", c[1])], t("Punnett square for Aa × Aa. The sex cells of one parent head the columns and those of the other, the rows. The four results are AA, Aa, Aa, and aa.", "Cuadro de Punnett del cruce Aa × Aa. Los gametos de un progenitor encabezan las columnas y los del otro, las filas. Los cuatro resultados son AA, Aa, Aa y aa."))}
{C.ejemplo(t("Example 2 · Reading the square on two levels", "Ejemplo 2 · Leer el cuadro en dos niveles"),
 [("1", t("<strong>Genotype ratio:</strong> one AA box, two Aa boxes, and one aa box. That is <strong>1 : 2 : 1</strong>.", "<strong>Proporción de genotipos:</strong> una casilla AA, dos casillas Aa y una casilla aa. Es decir, <strong>1 : 2 : 1</strong>.")),
  ("2", t("<strong>Phenotype ratio:</strong> AA and Aa look the same: both are purple. Only aa is white. So <strong>3 purple : 1 white</strong>.", "<strong>Proporción de fenotipos:</strong> AA y Aa se ven igual, las dos son moradas. Solo aa es blanca. Por tanto, <strong>3 moradas : 1 blanca</strong>.")),
  ("3", t("The probability of a white flower is 1 box out of 4.", "La probabilidad de flor blanca es de 1 casilla entre 4."))])}
{C.caja("ojo", t("The most missed distinction", "La distinción que más se falla"), "<p>" + t("The genotype and phenotype ratios of the same square are different: 1:2:1 against 3:1. Before answering, read whether the question says “genotype” or “phenotype,” or names a trait you can see, such as color.", "Las proporciones de genotipo y de fenotipo del mismo cuadro son distintas, 1:2:1 frente a 3:1. Antes de responder hay que leer si la pregunta dice «genotipo» o «fenotipo», o bien si nombra una característica visible, como el color.") + "</p>")}
{P(t("Try it 4 · Phenotypes", "Pruebe 4 · Fenotipos"), t("From the cross Aa × Aa, the expected phenotype ratio is…", "Del cruce Aa × Aa, la proporción de fenotipos esperada es…"),
   [t("3 dominant : 1 recessive", "3 dominantes : 1 recesivo"), "1 : 2 : 1", t("all dominant", "todos dominantes")], 0,
   {1: t("1 : 2 : 1 is the genotype ratio.", "1 : 2 : 1 es la proporción de genotipos."), 2: t("aa is recessive and shows up in one box.", "aa es recesivo y aparece en una casilla.")},
   t("AA + Aa + Aa look dominant; aa looks recessive.", "AA + Aa + Aa se ven dominantes; aa, recesivo."))}
{C.enlace(N, anc("punnett", "punnett"), t("one-gene crosses", "cruces de un gen"), t("New crosses every time: build the square in your head or on paper and answer.", "Cruces nuevos cada vez: arme el cuadro de cabeza o en papel y responda."))}"""

    s4 = f"""<p>{t("The test can ask for the same result in four different ways. They are not four answers: they are four ways of writing the same one, and you should be able to go from one to another without stopping.", "El examen puede pedir el mismo resultado de cuatro maneras distintas. No son cuatro respuestas: son cuatro escrituras de la misma, y conviene saber pasar de una a otra sin detenerse.")}</p>
{C.tabla(t("The four ways to write an offspring result, applied to the three most common results", "Los cuatro formatos en que puede expresarse una proporción de descendencia, aplicados a las tres proporciones más frecuentes"),
 [t("Result", "Resultado"), t("Fraction", "Fracción"), t("Decimal", "Decimal"), t("Percent", "Porcentaje"), t("Ratio", "Razón")],
 [[t("Purple flower (3 of 4)", "Flor morada (3 de 4)"), "3/4", "0.75", "75%" if C.L == "en" else "75 %", t("3 : 1 to white", "3 : 1 frente a la blanca")],
  [t("White flower (1 of 4)", "Flor blanca (1 de 4)"), "1/4", "0.25", "25%" if C.L == "en" else "25 %", t("1 : 3 to purple", "1 : 3 frente a la morada")],
  [t("Genotype Aa (2 of 4)", "Genotipo Aa (2 de 4)"), "2/4 = 1/2", "0.5", "50%" if C.L == "en" else "50 %", t("1 : 1 to the rest", "1 : 1 frente al resto")]])}
{C.caja("ojo", t("A ratio is not a fraction", "La razón no es la fracción"), "<p>" + t("It is the most common mistake in this part. A fraction compares one part with the <strong>whole</strong>: 3/4 means three out of every four. A ratio compares one part with <strong>another part</strong>: 3:1 means three purple for every white. Same data, two different comparisons. Writing “3/4” where the ratio was asked for, or “3:1” where the fraction was asked for, counts as wrong just like a math error.", "Es el error más frecuente de este bloque. La fracción compara una parte con el <strong>total</strong>: 3/4 significa tres de cada cuatro. La razón compara una parte con <strong>otra parte</strong>: 3:1 significa tres moradas por cada blanca. Los mismos datos, dos comparaciones distintas. Escribir «3/4» donde se pedía la razón, o «3:1» donde se pedía la fracción, se penaliza igual que un error de cálculo.") + "</p>")}
{C.caja("tip", t("Probability is not certainty", "Probabilidad no es certeza"), "<p>" + t("A probability of 1/4 for a white flower does not mean that exactly one out of every four seeds will be white. There may be none, or three. The ratio holds approximately when there are many offspring, exactly as with tossing a coin. Remember what Lesson 2.3 said about spread: real results cluster around the expected value; they do not match it exactly.", "Que la probabilidad de flor blanca sea de 1/4 no significa que de cada cuatro semillas vaya a salir exactamente una blanca. Puede no salir ninguna, o salir tres. La proporción se cumple de forma aproximada cuando la descendencia es numerosa, exactamente igual que ocurre al lanzar una moneda. Conviene recordar aquí lo trabajado en la Lección 2.3 sobre dispersión: los resultados reales se agrupan alrededor del valor esperado, no coinciden con él.") + "</p>")}
{P(t("Try it 5 · One in four", "Pruebe 5 · Uno de cuatro"), t("A probability of 1/4, written as a percent and as a ratio, is…", "Una probabilidad de 1/4 expresada como porcentaje y como razón es…"),
   [t("25% and 1 : 4", "25 % y 1 : 4"), t("25% and 1 : 3", "25 % y 1 : 3"), t("40% and 1 : 3", "40 % y 1 : 3")], 1,
   {0: t("1 : 4 is the fraction in disguise. Compare part with part: 1 against the other 3.", "1 : 4 es la fracción disfrazada. Compare parte con parte: 1 frente a los otros 3."), 2: t("1/4 = 0.25 = 25%.", "1/4 = 0.25 = 25 %.")},
   t("1 ÷ 4 = 0.25 = 25%; ratio: 1 for every 3 others.", "1 ÷ 4 = 0.25 = 25 %; razón: 1 por cada 3 restantes."))}
{C.enlace(N, anc("formats", "formatos"), t("fraction, decimal, percent, and ratio", "fracción, decimal, porcentaje y razón"), t("Convert each result to the format asked for.", "Convierta cada resultado al formato que se pide."))}"""

    gam = ["AB", "Ab", "aB", "ab"]
    def comb(x, y):
        a = "".join(sorted(x[0] + y[0], key=lambda c: c.islower())); b = "".join(sorted(x[1] + y[1], key=lambda c: c.islower()))
        return a + b
    filas16 = [(g, [comb(g2, g) for g2 in gam]) for g in gam]
    s5 = f"""<p>{t("When you follow two genes at once, each parent can make four kinds of sex cell. You do not have to memorize that number: it is the counting principle of Lesson 2.3. Two choices for the first gene times two for the second give 2 × 2 = 4 sex cells, and the square grows to 4 × 4 = 16 boxes.", "Cuando se siguen dos genes a la vez, cada progenitor puede producir cuatro tipos de gameto. Y ese número no hay que memorizarlo: es el principio del conteo de la Lección 2.3. Dos posibilidades para el primer gen por dos para el segundo dan 2 × 2 = 4 gametos, y el cuadro pasa a tener 4 × 4 = 16 casillas.")}</p>
<p>{t("Two individuals AaBb × AaBb are crossed. The possible sex cells of each are AB, Ab, aB, and ab.", "Se cruzan dos individuos AaBb × AaBb. Los gametos posibles de cada uno son AB, Ab, aB y ab.")}</p>
{punnett(gam, filas16, t("Two-gene Punnett square for AaBb × AaBb, with sixteen boxes. The four kinds of sex cell head the columns and the rows.", "Cuadro de Punnett dihíbrido del cruce AaBb × AaBb, con dieciséis casillas. Los cuatro tipos de gameto encabezan las columnas y las filas."))}
{C.ejemplo(t("Example 3 · Counting phenotypes in the two-gene square", "Ejemplo 3 · Contar fenotipos en el cuadro dihíbrido"),
 [("", t("To count phenotypes, ask in each box whether there is at least one capital letter for each gene.", "Para contar fenotipos basta con preguntarse, en cada casilla, si hay al menos una mayúscula de cada gen.")),
  ("1", t("Boxes with A and B together, both traits dominant: <strong>9</strong>.", "Casillas con A y con B a la vez, ambos rasgos dominantes: <strong>9</strong>.")),
  ("2", t("Boxes with A but bb, first trait dominant and second recessive: <strong>3</strong>.", "Casillas con A pero con bb, primer rasgo dominante y segundo recesivo: <strong>3</strong>.")),
  ("3", t("Boxes with aa but B, first trait recessive and second dominant: <strong>3</strong>.", "Casillas con aa pero con B, primer rasgo recesivo y segundo dominante: <strong>3</strong>.")),
  ("4", t("Boxes aabb, both recessive: <strong>1</strong>.", "Casillas aabb, ambos recesivos: <strong>1</strong>."))],
 t("<strong>Result:</strong> the ratio <strong>9 : 3 : 3 : 1</strong>, the best-known ratio of classical genetics. Always check that the boxes add up to 16: if they do not, a box was miscounted.", "<strong>Resultado:</strong> la proporción <strong>9 : 3 : 3 : 1</strong>, la más característica de la genética clásica. Las 16 casillas suman, y esa comprobación conviene hacerla siempre: si la suma no da 16, hay una casilla mal contada."))}
{P(t("Try it 6 · Kinds of sex cell", "Pruebe 6 · Tipos de gameto"), t("An individual AaBb can make…", "Un individuo AaBb puede producir…"),
   [t("4 kinds of sex cell, by the counting principle", "4 tipos de gameto, por el principio del conteo"), t("2 kinds of sex cell", "2 tipos de gameto"), t("16 kinds of sex cell", "16 tipos de gameto")], 0,
   {1: t("That would be true for one gene.", "Eso sería con un solo gen."), 2: t("16 is the number of boxes, not of sex cells.", "16 es el número de casillas, no de gametos.")},
   t("2 × 2 = 4: AB, Ab, aB, ab.", "2 × 2 = 4: AB, Ab, aB, ab."))}
{C.enlace(N, anc("two-genes", "dos-genes"), t("two-gene crosses", "cruces de dos genes"), t("Sex cells, boxes, and the 9 : 3 : 3 : 1 ratio.", "Gametos, casillas y la proporción 9 : 3 : 3 : 1."))}"""

    XA, Xa = "X<sup>A</sup>", "X<sup>a</sup>"
    s6 = f"""<p>{t("The crosses above assumed that both parents have the same possibilities. With certain genes that is no longer true, and the reason is one particular pair of chromosomes.", "Los cruces anteriores suponían que los dos progenitores tienen las mismas posibilidades. Con ciertos genes eso deja de ser cierto, y el motivo está en un par de cromosomas concreto.")}</p>
<p>{t("Of the 23 human pairs, one decides sex. Women have two X chromosomes; men have one X and one Y. And here is the key detail: the Y chromosome is much smaller and does not carry a copy of most of the genes on the X.", "De los 23 pares humanos, uno determina el sexo. Las mujeres tienen dos cromosomas X; los varones, un X y un Y. Y ahí está el detalle decisivo: el cromosoma Y es mucho más pequeño y no lleva copia de la mayoría de los genes del X.")}</p>
{C.caja("tip", t("The consequence, in one sentence", "La consecuencia, en una frase"), "<p>" + t("For a gene on the X chromosome, a woman has two alleles and a man has only one. A man with a single recessive allele shows the trait, because there is no second allele to cover it up. A woman would need both. That is why recessive X-linked traits, such as color blindness or hemophilia, are much more common in men.", "Para un gen situado en el cromosoma X, la mujer tiene dos alelos y el varón tiene uno solo. Un varón con un único alelo recesivo lo manifiesta, porque no hay un segundo alelo que pueda enmascararlo. Una mujer necesitaría los dos. Por eso los rasgos recesivos ligados al X —como el daltonismo o la hemofilia— aparecen con mucha más frecuencia en varones.") + "</p>")}
<p>{t(f"In the notation, the allele is written above the X. A woman who carries color blindness is {XA}{Xa}: she has the allele, but sees colors normally. A color-blind man is {Xa}Y.", f"La notación añade el alelo como índice sobre la X. Una mujer portadora de daltonismo es {XA}{Xa}: tiene el alelo, pero ve los colores con normalidad. Un varón daltónico es {Xa}Y.")}</p>
{C.ejemplo(t("Example 4 · Carrier mother, father not color-blind", "Ejemplo 4 · Madre portadora, padre no daltónico"),
 [("", t(f"A carrier woman, {XA}{Xa}, has children with a man who sees colors normally, {XA}Y.", f"Se cruza una mujer portadora, {XA}{Xa}, con un varón que ve los colores con normalidad, {XA}Y."))])}
{punnett([XA + t(" (father)", " (del padre)"), "Y" + t(" (father)", " (del padre)")],
         [(XA + t(" (mother)", " (de la madre)"), [XA + XA + t(" · daughter, not a carrier", " · hija, no portadora"), XA + "Y" + t(" · son, not color-blind", " · hijo, no daltónico")]),
          (Xa + t(" (mother)", " (de la madre)"), [XA + Xa + t(" · carrier daughter", " · hija portadora"), Xa + "Y" + t(" · color-blind son", " · hijo daltónico")])],
         t("Punnett square for a carrier mother and a father who is not color-blind. The mother’s sex cells head the rows and the father’s, the columns. Results: a daughter who is not a carrier, a son who is not color-blind, a carrier daughter, and a color-blind son.", "Cuadro de Punnett del cruce entre una mujer portadora de daltonismo y un varón no daltónico. Los gametos de la madre encabezan las filas y los del padre, las columnas. Resultados: hija no portadora, hijo no daltónico, hija portadora e hijo daltónico."))}
<p>{t("Read the result separately for each sex, and that is the difference from everything before. Among the daughters, none is color-blind and half are carriers. Among the sons, half are color-blind. One cross, two different results depending on sex.", "El resultado se lee por separado para cada sexo, y ahí está la diferencia con todo lo anterior. Entre las hijas, ninguna es daltónica y la mitad son portadoras. Entre los hijos, la mitad es daltónica. Un mismo cruce con dos resultados distintos según el sexo.")}</p>
{C.caja("ojo", t("The mistake the test is looking for", "El error que el examen busca"), "<p>" + t("Answering “25% of the children will be color-blind” and stopping there. It is true of all the children, but the question almost always says “of the sons” or “of the daughters,” and then the right answer is 50% or 0%. In a sex-linked cross, read carefully which group the question is about.", "Responder «el 25 % de la descendencia será daltónica» y quedarse ahí. Es cierto sobre el total, pero la pregunta casi siempre dice «de los hijos varones» o «de las hijas», y entonces la respuesta correcta es 50 % o 0 %. Ante un cruce ligado al sexo hay que leer con cuidado sobre qué grupo se pide la proporción.") + "</p>")}
{P(t("Try it 7 · Why men?", "Pruebe 7 · ¿Por qué los varones?"), t("A man shows a recessive X-linked trait with a single allele because…", "Un varón manifiesta un rasgo recesivo ligado al cromosoma X con un solo alelo porque…"),
   [t("men have more X chromosomes", "los varones tienen más cromosomas X"), t("the allele becomes dominant in men", "el alelo se vuelve dominante en los varones"), t("the Y chromosome has no copy of that gene, so there is no second allele to cover it", "el cromosoma Y no lleva copia de ese gen, así que no hay un segundo alelo que lo enmascare")], 2,
   {0: t("Men have one X; women have two.", "Los varones tienen un X; las mujeres, dos."), 1: t("Dominance does not change with sex.", "La dominancia no cambia con el sexo.")},
   t("One allele, nothing to cover it.", "Un solo alelo, nada que lo enmascare."))}
{P(t("Try it 8 · The sons", "Pruebe 8 · Los hijos varones"), t(f"From a carrier mother {XA}{Xa} and a father {XA}Y, what share of the <strong>sons</strong> are color-blind?", f"Del cruce entre una madre portadora {XA}{Xa} y un padre {XA}Y, ¿qué proporción de los <strong>hijos varones</strong> es daltónica?"),
   [t("Half", "La mitad"), t("None", "Ninguno"), t("One quarter", "La cuarta parte")], 0,
   {1: t("None is the answer for the daughters.", "Ninguna es la respuesta para las hijas."), 2: t("1/4 is of all the children. The question asks only about sons.", "1/4 es del total. La pregunta es solo sobre los hijos varones.")},
   t(f"Two son boxes: {XA}Y and {Xa}Y. One of two is color-blind.", f"Dos casillas de hijo: {XA}Y y {Xa}Y. Uno de dos es daltónico."))}
{C.enlace(N, anc("sex-linked", "ligada-al-sexo"), t("sex-linked crosses", "cruces ligados al sexo"), t("Read the result for the sons and for the daughters separately.", "Lea el resultado de los hijos y el de las hijas por separado."))}"""

    s7 = f"""<p>{t("A family tree, or <strong>pedigree</strong>, follows a trait through several generations. It is used to work out genotypes that cannot be seen: who is a carrier even though nothing shows.", "Un árbol genealógico muestra un rasgo a lo largo de varias generaciones. Su utilidad es deducir genotipos que no se ven: quién es portador aunque no manifieste nada.")}</p>
{svg_arbol()}
{C.ejemplo(t("Example 5 · Working out a genotype you cannot see", "Ejemplo 5 · Deducir un genotipo que no se ve"),
 [("", t("The trait in the tree is recessive. What can you say about II-2, the woman in the second generation, who does not show it?", "El rasgo del árbol es recesivo. ¿Qué puede afirmarse sobre II-2, la mujer de la segunda generación, que no lo manifiesta?")),
  ("1", t("Her son III-1 shows the trait, so he is homozygous recessive: he has two recessive alleles.", "Su hijo III-1 sí manifiesta el rasgo, de modo que es homocigoto recesivo: tiene dos alelos recesivos.")),
  ("2", t("One of those two alleles must come from her, because each parent gives one.", "Uno de esos dos alelos procede necesariamente de ella, porque cada progenitor aporta uno.")),
  ("3", t("Since she does not show the trait, she cannot be homozygous recessive. So she has one dominant and one recessive allele.", "Como ella no manifiesta el rasgo, no puede ser homocigota recesiva. Tiene entonces un alelo dominante y uno recesivo."))],
 t("<strong>Conclusion:</strong> II-2 is a carrier, even though nothing about her shows it. That is exactly the kind of reasoning the test asks for: a trait that skips a generation means that someone in between carried it without showing it.", "<strong>Conclusión:</strong> II-2 es portadora, aunque nada en su aspecto lo revele. Ese es exactamente el tipo de deducción que pide el examen: un rasgo que salta una generación obliga a que alguien en el medio lo haya llevado sin manifestarlo."))}
{P(t("Try it 9 · Where to start", "Pruebe 9 · Por dónde empezar"), t("When reading a family tree for a recessive trait, it is best to start with…", "Al leer un árbol genealógico de un rasgo recesivo, conviene empezar la deducción por…"),
   [t("a person who shows the trait, because their genotype is certain", "el individuo afectado, porque su genotipo se conoce con certeza"), t("the oldest person", "el individuo de mayor edad"), t("any person who does not show it", "cualquier individuo no afectado")], 0,
   {1: t("Age gives no genetic information.", "La edad no da información genética."), 2: t("Someone who does not show it could be AA or Aa: uncertain.", "Quien no lo manifiesta puede ser AA o Aa: incierto.")},
   t("Shows a recessive trait = aa for sure. From there, work outward.", "Manifiesta un rasgo recesivo = aa con certeza. Desde ahí se deduce hacia fuera."))}
{C.enlace(N, anc("family-trees", "arboles"), t("reason with family trees", "razone con árboles genealógicos"), t("Who must be a carrier, and why?", "¿Quién tiene que ser portador, y por qué?"))}"""

    s8 = f"""<p>{t("A short science text written for this level. Notice how the author tells the expected ratio apart from the observed result.", "Texto científico breve adaptado al nivel. Observe cómo el autor distingue la proporción esperada del resultado observado.")}</p>
{C.lectura(t("The peas of a monastery", "Los guisantes de un monasterio"),
 [t("In the mid-1800s, a monk named Gregor Mendel grew peas in his monastery garden and kept careful records of his crosses. He chose seven traits that came in two clearly different versions, among them seed color, yellow or green, and seed shape, smooth or wrinkled.", "A mediados del siglo XIX, un monje llamado Gregor Mendel cultivó guisantes en el huerto de su monasterio y llevó un registro minucioso de sus cruces. Eligió siete características que aparecían en dos versiones bien diferenciadas, entre ellas el color de la semilla, amarilla o verde, y la forma, lisa o rugosa."),
  t("When he crossed yellow-seed plants with green-seed plants, all the offspring were yellow. Green seemed to have disappeared. But when he crossed those yellow plants with each other, green came back in part of the next generation. Of 8,023 seeds counted in one of his experiments, 6,022 were yellow and 2,001 green.", "Al cruzar plantas de semilla amarilla con plantas de semilla verde, toda la descendencia resultó amarilla. El verde parecía haber desaparecido. Pero al cruzar entre sí esas plantas amarillas, el verde reapareció en una parte de la generación siguiente. De 8,023 semillas contadas en uno de sus experimentos, 6,022 fueron amarillas y 2,001 verdes."),
  t("Mendel worked out the ratio between the two numbers and got about three to one. The same ratio came up in all seven traits he studied. From that he concluded that each plant must carry two factors for each trait, that one could hide the other, and that the two factors separate when the reproductive cells form.", "Mendel calculó la razón entre ambas cifras y obtuvo aproximadamente tres a uno. La misma proporción se repitió en las siete características estudiadas. De ahí dedujo que cada planta debía llevar dos factores para cada característica, que uno podía enmascarar al otro y que al formarse las células reproductoras los dos factores se separaban."),
  t("It is remarkable that he reached that conclusion without knowing about chromosomes, which would be described decades later, or DNA. What he did was count a great deal and trust the ratio. He also noticed that his numbers were not exact: 6,022 is not exactly three times 2,001, and he argued that the difference was what you would expect in any count where chance plays a part.", "Es notable que llegara a esa conclusión sin conocer los cromosomas, que se describirían décadas más tarde, ni el ADN. Lo que hizo fue contar muchísimo y confiar en la proporción. También advirtió que sus cifras no eran exactas: 6,022 no es tres veces 2,001 con precisión matemática, y sostuvo que la desviación era la esperable en cualquier conteo con azar de por medio.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Mendel was a monk who grew peas.", "Mendel era monje y cultivaba guisantes."), t("By counting large numbers of offspring, Mendel worked out the rules of heredity without knowing about chromosomes or DNA.", "Contando grandes cantidades de descendencia, Mendel dedujo las reglas de la herencia sin conocer los cromosomas ni el ADN."), t("Yellow seeds are more common than green ones.", "Las semillas amarillas son más frecuentes que las verdes.")], 1,
   {0: t("A detail, not the main idea.", "Un detalle, no la idea central."), 2: t("Only in that cross; it is a result, not the main idea.", "Solo en ese cruce; es un resultado, no la idea central.")},
   t("Counting and trusting the ratio: that is the point of the text.", "Contar y confiar en la proporción: esa es la tesis del texto."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("The ratio of yellow to green seeds that Mendel got was about…", "La razón entre semillas amarillas y verdes que obtuvo Mendel fue aproximadamente…"),
   ["1 : 1", "9 : 3 : 3 : 1", "3 : 1"], 2,
   {0: t("6,022 is much more than 2,001.", "6,022 es mucho más que 2,001."), 1: t("That ratio needs two genes.", "Esa proporción requiere dos genes.")},
   t("6,022 ÷ 2,001 ≈ 3.01: about 3 to 1.", "6,022 ÷ 2,001 ≈ 3.01: aproximadamente 3 a 1."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("That all the first offspring were yellow shows that the yellow allele is…", "Que toda la primera descendencia fuera amarilla indica que el alelo amarillo es…"),
   [t("dominant over green", "dominante sobre el verde"), t("recessive to green", "recesivo frente al verde"), t("sex-linked", "ligado al sexo")], 0,
   {1: t("A recessive allele would be hidden, not shown.", "Un alelo recesivo quedaría oculto, no se vería."), 2: t("Nothing in the text is about sex.", "Nada en el texto trata del sexo.")},
   t("Yellow hid green: yellow is dominant.", "El amarillo ocultó al verde: el amarillo es dominante."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Why do 6,022 and 2,001 not give exactly 3 to 1?", "¿Por qué las cifras 6,022 y 2,001 no dan exactamente 3 a 1?"),
   [t("Because Mendel counted wrong", "Porque Mendel se equivocó al contar"), t("Because the real ratio was different", "Porque la proporción real era otra"), t("Because an expected ratio holds approximately, not exactly, when chance is involved", "Porque una proporción esperada se cumple de forma aproximada, no exacta, cuando interviene el azar")], 2,
   {0: t("The text says he counted carefully.", "El texto dice que contó con cuidado."), 1: t("It was the same in all seven traits: 3 to 1.", "Se repitió en las siete características: 3 a 1.")},
   t("Probability, not certainty, as in Lesson 2.3.", "Probabilidad, no certeza, como en la Lección 2.3."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK). You may use the calculator.", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SP.8.c", "2", t("<em>In guinea pigs, black fur (B) is dominant over white fur (b). A black guinea pig Bb is crossed with a white one bb.</em><br>What is the probability that a baby will have white fur?", "<em>En los cobayos, el pelo negro (B) es dominante sobre el blanco (b). Se cruza un cobayo negro Bb con uno blanco bb.</em><br>¿Qué probabilidad hay de que una cría tenga el pelo blanco?"),
   ["0%", "25%", "50%", "100%"] if C.L == "en" else ["0 %", "25 %", "50 %", "100 %"], 2,
   {0: t("The black parent carries b.", "El progenitor negro lleva b."), 1: t("25% is for Bb × Bb.", "25 % es para Bb × Bb."), 3: t("The black parent can also give B.", "El progenitor negro también puede dar B.")},
   t("Boxes: Bb, Bb, bb, bb. Two of four are white: 50%.", "Casillas: Bb, Bb, bb, bb. Dos de cuatro son blancas: 50 %."))}
{G(2, "SP.8.b", "2", t("<em>A pea plant is AaBbCc for three genes.</em><br>How many different kinds of sex cell can it make?", "<em>Una planta de guisante es AaBbCc para tres genes.</em><br>¿Cuántos tipos distintos de gameto puede producir?"),
   ["3", "6", "8", "16"], 2,
   {0: t("Each gene gives 2 choices; multiply.", "Cada gen da 2 opciones; multiplique."), 1: t("2 + 2 + 2 adds; the counting principle multiplies.", "2 + 2 + 2 suma; el principio del conteo multiplica."), 3: t("16 is for four genes.", "16 es para cuatro genes.")},
   t("2 × 2 × 2 = 8, as in the tree diagram of Lesson 2.3.", "2 × 2 × 2 = 8, como en el diagrama de árbol de la Lección 2.3."))}
{G(3, "SP.3.b", "2–3", t("<em>Two tall plants are crossed. Of their 400 offspring, 302 are tall and 98 are short.</em><br>What are the most likely genotypes of the parents?", "<em>Se cruzan dos plantas altas. De sus 400 descendientes, 302 son altos y 98 bajos.</em><br>¿Cuáles son los genotipos más probables de los progenitores?"),
   ["TT × TT", "TT × Tt", "Tt × Tt", "tt × tt"], 2,
   {0: t("TT × TT gives only tall plants.", "TT × TT da solo plantas altas."), 1: t("TT × Tt gives only tall plants too.", "TT × Tt también da solo plantas altas."), 3: t("tt plants are short, not tall.", "Las plantas tt son bajas, no altas.")},
   t("302 : 98 ≈ 3 : 1, the ratio of Tt × Tt. Short plants (tt) need a t from each parent.", "302 : 98 ≈ 3 : 1, la proporción de Tt × Tt. Las bajas (tt) necesitan una t de cada progenitor."))}
{G(4, "SP.3.c", "2", t(f"<em>Hemophilia is a recessive X-linked trait. A woman who does not carry it, {XA}{XA}, has children with a man who has hemophilia, {Xa}Y.</em><br>What do you predict for their children?", f"<em>La hemofilia es un rasgo recesivo ligado al X. Una mujer no portadora, {XA}{XA}, tiene hijos con un varón con hemofilia, {Xa}Y.</em><br>¿Qué se predice para sus hijos?"),
   [t("All daughters are carriers; no son has hemophilia.", "Todas las hijas son portadoras; ningún hijo tiene hemofilia."), t("All sons have hemophilia.", "Todos los hijos tienen hemofilia."), t("Half the daughters have hemophilia.", "La mitad de las hijas tiene hemofilia."), t("No child carries the allele.", "Ningún hijo o hija lleva el alelo.")], 0,
   {1: t("Sons get their X from the mother, who has none.", "Los hijos reciben el X de la madre, que no lo tiene."), 2: t("Daughters get one normal X from the mother.", "Las hijas reciben un X normal de la madre."), 3: t("Every daughter gets the father’s X.", "Toda hija recibe el X del padre.")},
   t(f"Daughters: {XA}{Xa} (carriers). Sons: {XA}Y (no hemophilia).", f"Hijas: {XA}{Xa} (portadoras). Hijos: {XA}Y (sin hemofilia)."))}
{G(5, "SP.1.c", "2–3", t("<em>Look at the family tree in section 7. The trait is recessive.</em><br>What can you say for sure about I-1 and I-2, the first generation?", "<em>Observe el árbol genealógico de la sección 7. El rasgo es recesivo.</em><br>¿Qué puede afirmarse con seguridad sobre I-1 e I-2, la primera generación?"),
   [t("Both are carriers.", "Los dos son portadores."), t("Both show the trait.", "Los dos manifiestan el rasgo."), t("Neither carries the allele.", "Ninguno lleva el alelo."), t("Only one of them is a carrier.", "Solo uno de ellos es portador.")], 0,
   {1: t("Neither is shaded in the tree.", "Ninguno aparece marcado en el árbol."), 2: t("Then their son II-1 could not show it.", "Entonces su hijo II-1 no podría manifestarlo."), 3: t("II-1 needs one recessive allele from each parent.", "II-1 necesita un alelo recesivo de cada progenitor.")},
   t("Their son II-1 shows the trait (aa): each parent gave one a, but neither shows it, so both are Aa.", "Su hijo II-1 manifiesta el rasgo (aa): cada progenitor aportó una a, pero ninguno lo manifiesta, así que los dos son Aa."))}"""

    secciones = [
        ("s1", t("Meiosis: where sex cells come from", "La meiosis: de dónde salen los gametos"), s1),
        ("s2", t("Genotype, phenotype, and alleles", "Genotipo, fenotipo y alelos"), s2),
        ("s3", t("The one-gene Punnett square", "El cuadro de Punnett monohíbrido"), s3),
        ("s4", t("Four ways to write the same result", "Los cuatro formatos de una misma proporción"), s4),
        ("s5", t("The two-gene square", "El cuadro dihíbrido"), s5),
        ("s6", t("Sex-linked inheritance", "Herencia ligada al sexo"), s6),
        ("s7", t("Reading a family tree", "Leer un árbol genealógico"), s7),
        ("s8", t("Science reading", "Lectura científica"), s8),
        ("s9", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Ten crosses.", "Diez cruces."), t("Do seven one-gene crosses and three two-gene crosses on paper, giving each answer in the format asked for (fraction, decimal, percent, or ratio).", "Resuelva en papel siete cruces monohíbridos y tres dihíbridos, con la respuesta en el formato que se pida en cada caso (fracción, decimal, porcentaje o razón).")),
        (t("Sons and daughters.", "Hijos e hijas."), t("Do two sex-linked crosses and give the expected result for the daughters and for the sons separately.", "Resuelva dos cruces ligados al sexo e indique por separado el resultado esperado entre las hijas y entre los hijos varones.")),
        (t("A family tree.", "Un árbol genealógico."), t("Draw a three-generation family tree for a recessive trait with two people left unmarked, and write how you work out each of their genotypes.", "Dibuje un árbol genealógico de tres generaciones para un rasgo recesivo con dos personas sin marcar, y escriba cómo deduce el genotipo de cada una.")),
    ]
    Q = t
    pc = lambda x: x if C.L == "en" else x.replace("%", " %")
    quiz = [
        (Q("Meiosis is different from mitosis because it makes…", "La meiosis se diferencia de la mitosis en que produce…"), [Q("two identical cells with the same number of chromosomes", "dos células idénticas con el mismo número de cromosomas"), Q("four cells with half the chromosomes", "cuatro células con la mitad de los cromosomas"), Q("one larger cell", "una sola célula de mayor tamaño"), Q("two cells with twice the chromosomes", "dos células con el doble de cromosomas")], 1,
         {0: Q("That is mitosis.", "Eso es la mitosis."), 2: Q("Meiosis divides twice.", "La meiosis divide dos veces."), 3: Q("It halves, not doubles.", "Reduce a la mitad, no duplica.")}, Q("Two divisions, four cells, half the chromosomes.", "Dos divisiones, cuatro células, la mitad de los cromosomas.")),
        (Q("If human sex cells had 46 chromosomes instead of 23…", "Si los gametos humanos tuvieran 46 cromosomas en lugar de 23, la consecuencia sería que…"), [Q("the number of chromosomes would double each generation", "el número de cromosomas se duplicaría en cada generación"), Q("no sex cells would form", "no se formarían gametos"), Q("children would be identical to their parents", "los hijos serían idénticos a los padres"), Q("nothing would happen", "no habría ninguna consecuencia")], 0,
         {1: Q("They would form, with the wrong number.", "Se formarían, con el número equivocado."), 2: Q("Each child still mixes two parents.", "Cada hijo sigue mezclando a dos progenitores."), 3: Q("46 + 46 = 92.", "46 + 46 = 92.")}, Q("46 + 46 = 92, then 184…", "46 + 46 = 92, luego 184…")),
        (Q("In the cross Aa × Aa, the expected genotype ratio is…", "En el cruce Aa × Aa, la proporción de genotipos esperada es…"), ["3 : 1", "1 : 1", "1 : 2 : 1", "9 : 3 : 3 : 1"], 2,
         {0: Q("3 : 1 is the phenotype ratio.", "3 : 1 es la de fenotipos."), 1: Q("That is Aa × aa.", "Esa es la de Aa × aa."), 3: Q("That needs two genes.", "Esa requiere dos genes.")}, Q("AA : Aa : aa = 1 : 2 : 1.", "AA : Aa : aa = 1 : 2 : 1.")),
        (Q("In the cross Aa × aa, the share of offspring with the recessive phenotype is…", "En el cruce Aa × aa, la proporción de descendientes con fenotipo recesivo es…"), [Q("none", "ninguno"), Q("half", "la mitad"), Q("one quarter", "la cuarta parte"), Q("three out of four", "tres de cada cuatro")], 1,
         {0: Q("aa appears in two boxes.", "aa aparece en dos casillas."), 2: Q("One quarter is for Aa × Aa.", "La cuarta parte es para Aa × Aa."), 3: Q("Count the aa boxes.", "Cuente las casillas aa.")}, Q("Aa, Aa, aa, aa: half.", "Aa, Aa, aa, aa: la mitad.")),
        (Q("AA crossed with aa gives offspring that are…", "Un individuo AA cruzado con uno aa produce descendencia…"), [Q("all Aa, with the dominant phenotype", "toda Aa, con fenotipo dominante"), Q("half AA and half aa", "mitad AA y mitad aa"), Q("all aa", "toda aa"), Q("in a 3 : 1 ratio", "en proporción 3 : 1")], 0,
         {1: Q("Each child gets A from one and a from the other.", "Cada hijo recibe A de uno y a del otro."), 2: Q("Every child gets an A.", "Todo hijo recibe una A."), 3: Q("3 : 1 is Aa × Aa.", "3 : 1 es Aa × Aa.")}, Q("Every box is Aa.", "Todas las casillas son Aa.")),
        (Q("Two purple-flowered plants have a white-flowered offspring. Both parents are…", "Dos plantas de flor morada tienen una descendiente de flor blanca. El genotipo de ambos progenitores es…"), ["AA × AA", "AA × Aa", "Aa × Aa", "aa × aa"], 2,
         {0: Q("They could not give an a.", "No podrían aportar una a."), 1: Q("The AA parent cannot give an a.", "El progenitor AA no puede aportar una a."), 3: Q("aa plants are white.", "Las plantas aa son blancas.")}, Q("White = aa: each parent gave an a, and both are purple, so both are Aa.", "Blanca = aa: cada progenitor aportó una a, y los dos son morados, así que son Aa.")),
        (Q("An individual AaBb can make how many kinds of sex cell?", "Un individuo de genotipo AaBb puede producir cuántos tipos distintos de gameto…"), ["2", "4", "8", "16"], 1,
         {0: Q("That would be one gene.", "Eso sería con un gen."), 2: Q("8 is for three genes.", "8 es para tres genes."), 3: Q("16 is the number of boxes.", "16 es el número de casillas.")}, Q("2 × 2 = 4.", "2 × 2 = 4.")),
        (Q("The Punnett square for AaBb × AaBb has…", "El cuadro de Punnett del cruce AaBb × AaBb tiene…"), [Q("4 boxes", "4 casillas"), Q("8 boxes", "8 casillas"), Q("16 boxes", "16 casillas"), Q("9 boxes", "9 casillas")], 2,
         {0: Q("Each parent makes 4 kinds of sex cell.", "Cada progenitor produce 4 tipos de gameto."), 1: Q("4 × 4, not 4 + 4.", "4 × 4, no 4 + 4."), 3: Q("9 is one part of the ratio.", "9 es una parte de la proporción.")}, Q("4 × 4 = 16.", "4 × 4 = 16.")),
        (Q("The typical phenotype ratio of the cross AaBb × AaBb is…", "La proporción de fenotipos característica del cruce dihíbrido AaBb × AaBb es…"), ["3 : 1", "1 : 2 : 1", "1 : 1 : 1 : 1", "9 : 3 : 3 : 1"], 3,
         {0: Q("That is one gene.", "Esa es de un gen."), 1: Q("That is one gene’s genotypes.", "Esa es de genotipos de un gen."), 2: Q("That is AaBb × aabb.", "Esa es AaBb × aabb.")}, Q("9 : 3 : 3 : 1, adding to 16.", "9 : 3 : 3 : 1, que suma 16.")),
        (Q("A probability of 3/4 as a decimal and a percent is…", "Una probabilidad de 3/4 expresada como decimal y porcentaje es…"), [pc("0.75 and 75%") if C.L == "en" else "0.75 y 75 %", pc("0.34 and 34%") if C.L == "en" else "0.34 y 34 %", pc("0.25 and 25%") if C.L == "en" else "0.25 y 25 %", pc("3.4 and 340%") if C.L == "en" else "3.4 y 340 %"], 0,
         {1: Q("3/4 is not “3 point 4.” Divide 3 by 4.", "3/4 no es «3 coma 4». Divida 3 entre 4."), 2: Q("0.25 is 1/4.", "0.25 es 1/4."), 3: Q("A probability cannot be more than 1.", "Una probabilidad no puede pasar de 1.")}, Q("3 ÷ 4 = 0.75 = 75%.", "3 ÷ 4 = 0.75 = 75 %.")),
        (Q("If three purple and one white are expected out of every four, the RATIO of purple to white is…", "Si de cada cuatro descendientes se esperan tres morados y uno blanco, la RAZÓN entre morados y blancos es…"), ["3/4", "1 : 4", "3 : 1", "25%" if C.L == "en" else "25 %"], 2,
         {0: Q("3/4 is the fraction of purple.", "3/4 es la fracción de morados."), 1: Q("Compare part with part.", "Compare parte con parte."), 3: Q("25% is the share of white.", "25 % es la proporción de blancos.")}, Q("3 purple for every 1 white.", "3 morados por cada blanco.")),
        (Q("The difference between the fraction 1/4 and the ratio 1 : 3 is that…", "La diferencia entre la fracción 1/4 y la razón 1 : 3 es que…"), [Q("they are different amounts", "son cantidades distintas"), Q("the fraction compares a part with the whole, and the ratio compares a part with another part", "la fracción compara una parte con el total y la razón compara una parte con otra parte"), Q("the ratio is always larger", "la razón siempre es mayor"), Q("the fraction is used only in math", "la fracción solo se usa en matemáticas")], 1,
         {0: Q("They describe the same result.", "Describen el mismo resultado."), 2: Q("It is not about size.", "No es cuestión de tamaño."), 3: Q("Both are used in genetics.", "Las dos se usan en genética.")}, Q("Part/whole against part:part.", "Parte/total frente a parte:parte.")),
        (Q("Recessive X-linked traits are more common in men because…", "Los rasgos recesivos ligados al cromosoma X aparecen con más frecuencia en varones porque…"), [Q("men inherit more recessive alleles", "los varones heredan más alelos recesivos"), Q("the Y chromosome has no copy of those genes, so one allele is enough to show the trait", "el cromosoma Y no lleva copia de esos genes, así que un solo alelo basta para manifestarlos"), Q("women cannot carry those alleles", "las mujeres no pueden portar esos alelos"), Q("the allele switches from dominant to recessive by sex", "el alelo cambia de dominante a recesivo según el sexo")], 1,
         {0: Q("They inherit the same way.", "Heredan igual."), 2: Q("Women can be carriers.", "Las mujeres pueden ser portadoras."), 3: Q("Dominance does not change.", "La dominancia no cambia.")}, Q("One X, nothing to cover the allele.", "Un solo X, nada que enmascare el alelo.")),
        (Q("From a carrier mother and a father who is not color-blind, the expected share of DAUGHTERS who are color-blind is…", "Del cruce entre una madre portadora de daltonismo y un padre no daltónico, la proporción esperada de HIJAS daltónicas es…"), [Q("none", "ninguna"), Q("half", "la mitad"), Q("one quarter", "la cuarta parte"), Q("all", "todas")], 0,
         {1: Q("Half of the daughters are carriers, not color-blind.", "La mitad de las hijas son portadoras, no daltónicas."), 2: Q("One quarter is of all the children, and it is the sons.", "La cuarta parte es del total, y son hijos varones."), 3: Q("Every daughter gets a normal X from the father.", "Toda hija recibe un X normal del padre.")}, Q("Every daughter gets the father’s normal X.", "Toda hija recibe el X normal del padre.")),
        (Q("In a family tree, a recessive trait shows up again in a grandchild whose parents do not show it. You can conclude that…", "En un árbol genealógico, un rasgo recesivo reaparece en un nieto cuyos padres no lo manifiestan. Puede deducirse que…"), [Q("the trait is dominant", "el rasgo es dominante"), Q("there was a new mutation", "hubo una mutación nueva"), Q("the tree is wrong", "el árbol está mal construido"), Q("both parents are carriers", "ambos padres son portadores")], 3,
         {0: Q("A dominant trait cannot skip a generation this way.", "Un rasgo dominante no salta así una generación."), 1: Q("The simplest explanation is inheritance.", "La explicación más sencilla es la herencia."), 2: Q("This is a normal pattern.", "Es un patrón normal.")}, Q("The child is aa: one a from each parent.", "El hijo es aa: una a de cada progenitor.")),
        (Q("When reading a family tree, it is best to start with…", "Al leer un árbol genealógico, conviene empezar la deducción por…"), [Q("a person who shows the trait, because their genotype is certain", "el individuo afectado, porque su genotipo se conoce con certeza"), Q("the oldest person", "el individuo de mayor edad"), Q("any person who does not show the trait", "cualquier individuo no afectado"), Q("always the oldest generation", "la generación más antigua siempre")], 0,
         {1: Q("Age says nothing about genes.", "La edad no dice nada de los genes."), 2: Q("They could be AA or Aa.", "Podrían ser AA o Aa."), 3: Q("Start where you are certain.", "Empiece por lo que es seguro.")}, Q("Recessive trait shown = aa for sure.", "Rasgo recesivo manifiesto = aa seguro.")),
    ]
    filas = [
        (t("Build the square with the right sex cells", "Construye el cuadro con los gametos correctos"), t("I get the right sex cells in one- and two-gene crosses and explain their number with meiosis and the counting principle.", "Obtengo los gametos correctos en cruces de uno y dos genes y justifico su número con la meiosis y el principio del conteo."), t("I get them for one gene, but not for two.", "Los obtengo en el monohíbrido, pero no en el dihíbrido."), t("I put the whole genotype in the margins instead of the sex cells.", "Coloco en los márgenes el genotipo completo en lugar de los gametos.")),
        (t("Tell genotype from phenotype when counting", "Distingue genotipo de fenotipo al contar"), t("I count both ratios and can tell which one is asked for, even without those words.", "Cuento las dos proporciones y sé cuál se pide, aunque la pregunta no use esas palabras."), t("I know the difference but miscount one of them.", "Conozco la diferencia, pero me equivoco al contar una."), t("I count one ratio without knowing which.", "Cuento una sola proporción sin saber cuál.")),
        (t("Write the result in the format asked for", "Expresa la proporción en el formato pedido"), t("I convert among the four formats and explain what each one compares.", "Convierto entre los cuatro formatos y explico qué compara cada uno."), t("I convert, but mix up fraction and ratio.", "Convierto, pero confundo fracción y razón."), t("I always answer in the same format.", "Respondo siempre en el mismo formato.")),
        (t("Read the result as probability, not certainty", "Interpreta el resultado como probabilidad"), t("I treat the ratio as an expected value and link the spread to the number of offspring.", "Trato la proporción como valor esperado y relaciono la desviación con el tamaño de la descendencia."), t("I say it is a probability but reason as if it were exact.", "Digo que es probabilidad, pero razono como si fuera exacta."), t("I think exactly one in four will be recessive.", "Creo que de cada cuatro saldrá exactamente uno recesivo.")),
    ]
    cierre = "<p>" + t("This lesson worked at the level of the <strong>individual</strong>: what an offspring inherits and how likely it is. It also paid back the debt from Topic 3 with meiosis, which turns the Punnett square into a model of something real, not a recipe.", "Esta lección trabajó el nivel del <strong>individuo</strong>: qué hereda un descendiente y con qué probabilidad. Saldó además la deuda del Tema 3 con la meiosis, que es lo que convierte el cuadro de Punnett en un modelo de algo real y no en una receta.") + "</p><p>" + \
             t("Lesson 4.3 moves up to the last level, the <strong>population</strong>. There, the variation counted case by case here becomes raw material: differences between individuals, combined with pressure from the environment, explain how a whole species changes. And sickle cell from Lesson 4.1 comes back, as an example of why a harmful variant can stay around.", "La Lección 4.3 sube al último nivel, el de la <strong>población</strong>. Allí la variación que aquí se contaba caso por caso pasa a ser materia prima: las diferencias entre individuos, combinadas con una presión del ambiente, explican cómo cambia una especie entera. Y volverá la anemia falciforme de la Lección 4.1, ahora como ejemplo de por qué una variante perjudicial puede mantenerse.") + "</p>"
    glosario = [
        (t("Meiosis", "Meiosis"), t("Division that makes four sex cells with half the chromosomes.", "División que produce cuatro gametos con la mitad de los cromosomas.")),
        (t("Gamete (sex cell)", "Gameto"), t("An egg or sperm cell, with one set of chromosomes.", "Óvulo o espermatozoide, con un solo juego de cromosomas.")),
        (t("Allele", "Alelo"), t("One version of a gene.", "Cada versión de un gen.")),
        (t("Genotype / phenotype", "Genotipo / fenotipo"), t("The two alleles an individual has / the trait that shows.", "Los dos alelos que posee el individuo / la característica que se manifiesta.")),
        (t("Dominant / recessive", "Dominante / recesivo"), t("Shows with one copy / shows only with two copies.", "Se manifiesta con una copia / solo se manifiesta con dos copias.")),
        (t("Homozygous / heterozygous", "Homocigoto / heterocigoto"), t("Two equal alleles / two different alleles (a carrier).", "Dos alelos iguales / dos alelos distintos (portador).")),
        (t("Punnett square", "Cuadro de Punnett"), t("A table that crosses the sex cells of two parents to show the possible offspring.", "Tabla que cruza los gametos de dos progenitores para mostrar la descendencia posible.")),
        (t("Ratio", "Razón"), t("A comparison of one part with another part, such as 3 : 1.", "Comparación de una parte con otra parte, como 3 : 1.")),
        (t("Sex-linked trait", "Rasgo ligado al sexo"), t("A trait whose gene is on the X chromosome.", "Rasgo cuyo gen está en el cromosoma X.")),
        (t("Family tree (pedigree)", "Árbol genealógico"), t("A chart that follows a trait through several generations.", "Diagrama que sigue un rasgo a lo largo de varias generaciones.")),
    ]
    estd = C.estandares(["SP.8.b", "SP.8.c", "SP.7.a", "SP.3.b", "SP.1.c"], ["L.e"], base=["SP.3.c"])
    conexion = "<p>" + t("Lesson 4.1 worked at the molecular level: a gene is transcribed and translated into a protein. This one moves up to the individual and asks a different question: if each person has two copies of each gene, one from each parent, which one shows, and how likely is it to be passed on?", "La Lección 4.1 trabajó el nivel molecular: un gen se transcribe y se traduce en una proteína. Esta sube al nivel del individuo y responde a una pregunta distinta: si cada persona tiene dos copias de cada gen, una de cada progenitor, ¿cuál de las dos se manifiesta y con qué probabilidad se transmite?") + "</p><p>" + \
               t("And there is a debt from Topic 3. Lesson 3.1 explained mitosis and said that there was a second kind of cell division. That debt is paid here, and not as a curiosity: without meiosis, you can fill in a Punnett square from memory, but you will not understand it.", "Y hay una deuda pendiente del Tema 3. La Lección 3.1 explicó la mitosis y anunció que existía una segunda forma de división celular. Esa deuda se salda aquí, y no como curiosidad: sin la meiosis, un cuadro de Punnett se rellena de memoria pero no se entiende.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> it builds on percents from Math (Level 2) and on the counting principle of Lesson 2.3. If they are not fresh, review them first: the sex cells of a two-gene cross are exactly the 2 × 2 of that tree diagram.", "<strong>Cómo estudiar esta lección:</strong> se apoya en los porcentajes de Matemáticas (Nivel 2) y en el principio del conteo de la Lección 2.3. Si esos temas no están frescos, repáselos antes: los gametos de un cruce dihíbrido son exactamente el 2 × 2 de aquel diagrama de árbol.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Why each parent gives one letter, how to fill in the square, and how to read the result as a probability.", "Por qué cada progenitor aporta una sola letra, cómo se rellena el cuadro y cómo se lee el resultado como probabilidad."),
        ["SP.8 · " + t("Probability and counting", "Probabilidad y conteo"), "SP.7 · " + t("Scientific models", "Modelos científicos")],
        [t("<strong>Explain</strong> how meiosis makes sex cells with half the chromosomes, and why each parent gives one allele.", "<strong>Explicar</strong> cómo la meiosis produce gametos con la mitad de los cromosomas y por qué cada progenitor aporta un solo alelo."),
         t("<strong>Use</strong> genotype, phenotype, dominant, recessive, homozygous, and heterozygous correctly.", "<strong>Usar</strong> correctamente genotipo, fenotipo, dominante, recesivo, homocigoto y heterocigoto."),
         t("<strong>Build</strong> one- and two-gene Punnett squares and read the genotype and phenotype ratios.", "<strong>Construir</strong> cuadros de Punnett monohíbridos y dihíbridos y leer las proporciones de genotipo y de fenotipo."),
         t("<strong>Write</strong> a result as a fraction, decimal, percent, and ratio.", "<strong>Expresar</strong> un resultado como fracción, decimal, porcentaje y razón."),
         t("<strong>Solve</strong> sex-linked crosses, reading sons and daughters separately.", "<strong>Resolver</strong> cruces ligados al sexo, leyendo por separado a hijos e hijas."),
         t("<strong>Work out</strong> hidden genotypes from a family tree.", "<strong>Deducir</strong> genotipos ocultos a partir de un árbol genealógico.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("4-3", t("Natural selection, evidence for evolution, and ecosystems", "Selección natural, evidencia evolutiva y ecosistemas")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- práctica
RASGOS = [  # (dominante, recesivo, letra, organismo)
    (("purple flowers", "flor morada"), ("white flowers", "flor blanca"), "A", ("pea plants", "plantas de guisante")),
    (("black fur", "pelo negro"), ("white fur", "pelo blanco"), "B", ("guinea pigs", "cobayos")),
    (("tall stems", "tallo alto"), ("short stems", "tallo bajo"), "T", ("pea plants", "plantas de guisante")),
    (("yellow seeds", "semilla amarilla"), ("green seeds", "semilla verde"), "Y", ("pea plants", "plantas de guisante")),
    (("round seeds", "semilla lisa"), ("wrinkled seeds", "semilla rugosa"), "R", ("pea plants", "plantas de guisante")),
]


def pct(f):
    v = float(f) * 100
    s = (str(int(v)) if v == int(v) else str(v))
    return s + ("%" if C.L == "en" else " %")


def frac(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


def banco_monohibrido():
    rnd = random.Random(42)
    out = []
    pares = [("Aa", "Aa"), ("Aa", "aa"), ("AA", "aa"), ("AA", "Aa"), ("Aa", "Aa"), ("Aa", "aa")]
    for n in range(24):
        dom, rec, L, org = RASGOS[n % len(RASGOS)]
        p1, p2 = pares[n % len(pares)]
        p1, p2 = p1.replace("A", L).replace("a", L.lower()), p2.replace("A", L).replace("a", L.lower())
        g1, g2, c = cruza(p1, p2)
        cas = [x for f in c for x in f]
        nrec = sum(1 for x in cas if x == L.lower() * 2)
        nhom = sum(1 for x in cas if x == L * 2)
        nhet = 4 - nrec - nhom
        cuadro = punnett(g1, [(g2[i], c[i]) for i in range(2)], t("Punnett square", "Cuadro de Punnett"))
        ctx = t(f"In {org[0]}, {dom[0]} ({L}) is dominant over {rec[0]} ({L.lower()}). The cross is <strong>{p1} × {p2}</strong>.",
                f"En {org[1]}, {dom[1]} ({L}) es dominante sobre {rec[1]} ({L.lower()}). El cruce es <strong>{p1} × {p2}</strong>.")
        q = n % 3
        if q == 0:
            f = F(nrec, 4)
            pre = t(f"What is the probability of offspring with {rec[0]}?", f"¿Qué probabilidad hay de descendencia con {rec[1]}?")
            ok = pct(f)
            otros = [pct(F(k, 4)) for k in range(5) if F(k, 4) != f]
            ops = [ok] + rnd.sample(otros, 3)
            exp = t(f"{nrec} of the 4 boxes are {L.lower() * 2}: {frac(f)} = {pct(f)}.", f"{nrec} de las 4 casillas son {L.lower() * 2}: {frac(f)} = {pct(f)}.")
        elif q == 1:
            ok = f"{nhom} : {nhet} : {nrec}"
            cands = ["1 : 2 : 1", "0 : 2 : 2", "0 : 4 : 0", "2 : 2 : 0", "3 : 1 : 0", "1 : 1 : 2"]
            ops = [ok] + rnd.sample([x for x in cands if x != ok], 3)
            pre = t(f"Of the 4 boxes, how many are {L}{L} : {L}{L.lower()} : {L.lower()}{L.lower()}?", f"De las 4 casillas, ¿cuántas son {L}{L} : {L}{L.lower()} : {L.lower()}{L.lower()}?")
            exp = t(f"Count the boxes: {nhom} {L}{L}, {nhet} {L}{L.lower()}, {nrec} {L.lower()}{L.lower()}.", f"Cuente las casillas: {nhom} {L}{L}, {nhet} {L}{L.lower()}, {nrec} {L.lower()}{L.lower()}.")
        else:
            nd = 4 - nrec
            frases = [t(f"3 {dom[0]} : 1 {rec[0]}", f"3 {dom[1]} : 1 {rec[1]}"), t(f"1 {dom[0]} : 1 {rec[0]}", f"1 {dom[1]} : 1 {rec[1]}"),
                      t(f"all {dom[0]}", f"todas con {dom[1]}"), t(f"1 {dom[0]} : 3 {rec[0]}", f"1 {dom[1]} : 3 {rec[1]}")]
            k = {(3, 1): 0, (2, 2): 1, (4, 0): 2}[(nd, nrec)]
            ops = [frases[k]] + [f for i, f in enumerate(frases) if i != k]
            pre = t("What is the phenotype ratio?", "¿Cuál es la proporción de fenotipos?")
            exp = t(f"{nd} boxes have at least one {L} ({dom[0]}); {nrec} are {L.lower() * 2} ({rec[0]}).", f"{nd} casillas tienen al menos una {L} ({dom[1]}); {nrec} son {L.lower() * 2} ({rec[1]}).")
        if len(set(ops)) != len(ops):
            continue
        out.append({"enun": f"<p>{ctx}</p><p><strong>{pre}</strong></p>", "ops": ops, "ok": 0,
                    "pista": t("Draw the square: one parent’s two letters across the top, the other’s down the side.", "Dibuje el cuadro: las dos letras de un progenitor arriba y las del otro a la izquierda."),
                    "exp": exp + cuadro})
    return out


def banco_formatos():
    rnd = random.Random(43)
    out = []
    casos = [(F(1, 4), 1, 3), (F(3, 4), 3, 1), (F(1, 2), 1, 1), (F(9, 16), 9, 7), (F(1, 16), 1, 15), (F(3, 16), 3, 13), (F(1, 8), 1, 7), (F(5, 8), 5, 3)]
    for f, a, b in casos:
        dec = str(float(f)).rstrip("0").rstrip(".")
        for k in range(3):
            if k == 0:
                pre = t(f"Write {frac(f)} as a percent.", f"Escriba {frac(f)} como porcentaje.")
                ok = pct(f); ops = [ok, pct(F(f.denominator - f.numerator, f.denominator)), (str(f.numerator) + str(f.denominator)) + ("%" if C.L == "en" else " %"), pct(f / 2)]
                exp = t(f"{f.numerator} ÷ {f.denominator} = {dec} = {pct(f)}.", f"{f.numerator} ÷ {f.denominator} = {dec} = {pct(f)}.")
            elif k == 1:
                pre = t(f"{frac(f)} of the offspring show a trait. What is the <strong>ratio</strong> of offspring with the trait to offspring without it?", f"{frac(f)} de la descendencia manifiesta un rasgo. ¿Cuál es la <strong>razón</strong> entre descendientes con el rasgo y sin él?")
                ok = f"{a} : {b}"; ops = [ok, f"{f.numerator} : {f.denominator}", f"{b} : {a}", f"1 : {f.denominator}" if f.numerator != 1 else f"{a + 1} : {b}"]
                exp = t(f"Out of {f.denominator}, {a} have it and {b} do not: {a} : {b}. ({f.numerator} : {f.denominator} would compare a part with the whole.)", f"De cada {f.denominator}, {a} lo tienen y {b} no: {a} : {b}. ({f.numerator} : {f.denominator} compararía una parte con el total.)")
            else:
                pre = t(f"Write {frac(f)} as a decimal.", f"Escriba {frac(f)} como decimal.")
                ok = dec; ops = [ok, f"{f.numerator}.{f.denominator}", str(float(F(f.denominator - f.numerator, f.denominator))).rstrip("0").rstrip("."), str(float(f) * 10).rstrip("0").rstrip(".")]
                exp = t(f"Divide: {f.numerator} ÷ {f.denominator} = {dec}.", f"Divida: {f.numerator} ÷ {f.denominator} = {dec}.")
            if len(set(ops)) != len(ops):
                continue
            out.append({"enun": f"<p><strong>{pre}</strong></p>", "ops": ops, "ok": 0, "pista": t("Fraction = part ÷ whole. Ratio = part : other part.", "Fracción = parte ÷ total. Razón = parte : otra parte."), "exp": exp})
    rnd.shuffle(out)
    return out


def banco_dihibrido():
    d = [
        (t("How many kinds of sex cell can an individual <strong>AaBb</strong> make?", "¿Cuántos tipos de gameto puede producir un individuo <strong>AaBb</strong>?"), ["4", "2", "8", "16"], t("2 × 2 = 4: AB, Ab, aB, ab.", "2 × 2 = 4: AB, Ab, aB, ab.")),
        (t("How many kinds of sex cell can an individual <strong>AABb</strong> make?", "¿Cuántos tipos de gameto puede producir un individuo <strong>AABb</strong>?"), ["2", "4", "1", "3"], t("1 × 2 = 2: AB and Ab. AA can give only A.", "1 × 2 = 2: AB y Ab. AA solo puede dar A.")),
        (t("How many kinds of sex cell can an individual <strong>aabb</strong> make?", "¿Cuántos tipos de gameto puede producir un individuo <strong>aabb</strong>?"), ["1", "2", "4", "0"], t("1 × 1 = 1: only ab.", "1 × 1 = 1: solo ab.")),
        (t("How many boxes does the square for <strong>AaBb × AaBb</strong> have?", "¿Cuántas casillas tiene el cuadro de <strong>AaBb × AaBb</strong>?"), ["16", "8", "4", "9"], t("4 kinds of sex cell × 4 = 16.", "4 tipos de gameto × 4 = 16.")),
        (t("In <strong>AaBb × AaBb</strong>, what fraction of offspring show both dominant traits?", "En <strong>AaBb × AaBb</strong>, ¿qué fracción de la descendencia manifiesta los dos rasgos dominantes?"), ["9/16", "3/16", "1/16", "3/4"], t("9 of the 16 boxes have A and B.", "9 de las 16 casillas tienen A y B.")),
        (t("In <strong>AaBb × AaBb</strong>, what fraction of offspring are <strong>aabb</strong>?", "En <strong>AaBb × AaBb</strong>, ¿qué fracción de la descendencia es <strong>aabb</strong>?"), ["1/16", "1/4", "9/16", "3/16"], t("Only 1 box of 16: 1/4 × 1/4 = 1/16.", "Solo 1 casilla de 16: 1/4 × 1/4 = 1/16.")),
        (t("In <strong>AaBb × AaBb</strong>, what fraction show the first trait dominant and the second recessive?", "En <strong>AaBb × AaBb</strong>, ¿qué fracción manifiesta el primer rasgo dominante y el segundo recesivo?"), ["3/16", "9/16", "1/16", "1/4"], t("A with bb: 3 of 16 (3/4 × 1/4).", "A con bb: 3 de 16 (3/4 × 1/4).")),
        (t("The phenotype ratio of <strong>AaBb × AaBb</strong> is…", "La proporción de fenotipos de <strong>AaBb × AaBb</strong> es…"), ["9 : 3 : 3 : 1", "3 : 1", "1 : 2 : 1", "1 : 1 : 1 : 1"], t("9 + 3 + 3 + 1 = 16.", "9 + 3 + 3 + 1 = 16.")),
        (t("Out of 320 offspring of <strong>AaBb × AaBb</strong>, about how many are expected to be aabb?", "De 320 descendientes de <strong>AaBb × AaBb</strong>, ¿cuántos se espera, aproximadamente, que sean aabb?"), ["20", "60", "180", "80"], t("320 × 1/16 = 20. Expected, not exact.", "320 × 1/16 = 20. Esperado, no exacto.")),
        (t("Out of 320 offspring of <strong>AaBb × AaBb</strong>, about how many are expected to show both dominant traits?", "De 320 descendientes de <strong>AaBb × AaBb</strong>, ¿cuántos se espera que manifiesten los dos rasgos dominantes?"), ["180", "160", "240", "90"], t("320 × 9/16 = 180.", "320 × 9/16 = 180.")),
    ]
    return [{"enun": f"<p>{q}</p>", "ops": o, "ok": 0, "pista": t("Count the sex cells of each gene and multiply (Lesson 2.3).", "Cuente los gametos de cada gen y multiplique (Lección 2.3)."), "exp": e} for q, o, e in d]


def banco_ligado():
    XA, Xa = "X<sup>A</sup>", "X<sup>a</sup>"
    cr = [  # (madre, padre, hijas daltónicas, hijas portadoras, hijos daltónicos)
        (XA + Xa, XA + "Y", 0, 1, 1), (XA + Xa, Xa + "Y", 1, 1, 1), (XA + XA, Xa + "Y", 0, 2, 0), (Xa + Xa, XA + "Y", 0, 2, 2), (XA + XA, XA + "Y", 0, 0, 0)]
    def p(k):
        return [t("none", "ninguna"), t("half", "la mitad"), t("all", "todas")][k]
    def pm(k):
        return [t("none", "ninguno"), t("half", "la mitad"), t("all", "todos")][k]
    out = []
    for m, pa, hd, hp, vd in cr:
        ctx = t(f"Color blindness is a recessive X-linked trait. Mother: <strong>{m}</strong>. Father: <strong>{pa}</strong>.", f"El daltonismo es un rasgo recesivo ligado al X. Madre: <strong>{m}</strong>. Padre: <strong>{pa}</strong>.")
        out.append({"enun": f"<p>{ctx}</p><p><strong>" + t("What share of the <em>sons</em> are expected to be color-blind?", "¿Qué proporción de los <em>hijos varones</em> se espera que sea daltónica?") + "</strong></p>",
                    "ops": [pm(0), pm(1), pm(2)], "ok": vd, "enOrden": True, "pista": t("Sons get their X from the mother and Y from the father.", "Los hijos reciben el X de la madre y el Y del padre."),
                    "exp": t("Each son gets one of the mother’s X chromosomes; the father gives Y.", "Cada hijo recibe uno de los X de la madre; el padre aporta el Y.")})
        out.append({"enun": f"<p>{ctx}</p><p><strong>" + t("What share of the <em>daughters</em> are expected to be color-blind?", "¿Qué proporción de las <em>hijas</em> se espera que sea daltónica?") + "</strong></p>",
                    "ops": [p(0), p(1), p(2)], "ok": hd, "enOrden": True, "pista": t("Daughters get one X from each parent. They need two recessive alleles.", "Las hijas reciben un X de cada progenitor. Necesitan dos alelos recesivos."),
                    "exp": t(f"Every daughter gets the father’s X ({pa[:-1]}) plus one of the mother’s.", f"Toda hija recibe el X del padre ({pa[:-1]}) más uno de los de la madre.")})
    return out


def banco_arboles():
    d = [
        (t("A trait is recessive. A man and a woman who do not show it have a daughter who does. What are the parents?", "Un rasgo es recesivo. Un hombre y una mujer que no lo manifiestan tienen una hija que sí. ¿Qué son los padres?"),
         [t("Both carriers (Aa)", "Los dos portadores (Aa)"), t("Both AA", "Los dos AA"), t("One aa and one AA", "Uno aa y otro AA")], 0, t("The daughter is aa: one a from each parent; neither shows it, so both are Aa.", "La hija es aa: una a de cada progenitor; ninguno lo manifiesta, así que los dos son Aa.")),
        (t("A trait is recessive. A woman who shows it (aa) has children with a man who is AA. Can any child show the trait?", "Un rasgo es recesivo. Una mujer que lo manifiesta (aa) tiene hijos con un hombre AA. ¿Puede algún hijo manifestar el rasgo?"),
         [t("No: all children are Aa", "No: todos los hijos son Aa"), t("Yes, half of them", "Sí, la mitad"), t("Yes, all of them", "Sí, todos")], 0, t("Every child gets an A from the father.", "Todo hijo recibe una A del padre.")),
        (t("A trait shows up in every generation, and every person who shows it has at least one parent who shows it. The trait is most likely…", "Un rasgo aparece en todas las generaciones, y toda persona que lo manifiesta tiene al menos un progenitor que también. Lo más probable es que el rasgo sea…"),
         [t("dominant", "dominante"), t("recessive", "recesivo"), t("not inherited", "no heredado")], 0, t("A dominant trait does not skip generations: one copy is enough to show it.", "Un rasgo dominante no salta generaciones: basta una copia para manifestarlo.")),
        (t("A trait skips a generation: grandparent shows it, parent does not, grandchild does. The trait is most likely…", "Un rasgo salta una generación: el abuelo lo manifiesta, el padre no, el nieto sí. Lo más probable es que el rasgo sea…"),
         [t("recessive", "recesivo"), t("dominant", "dominante"), t("caused by the environment", "causado por el ambiente")], 0, t("Someone in between carried it without showing it: recessive.", "Alguien en medio lo llevó sin manifestarlo: recesivo.")),
        (t("A man who does not show a recessive trait has a mother who shows it (aa). What is the man?", "Un hombre que no manifiesta un rasgo recesivo tiene una madre que sí (aa). ¿Qué es el hombre?"),
         [t("A carrier (Aa)", "Portador (Aa)"), t("AA", "AA"), t("aa", "aa")], 0, t("His mother could only give him a; he does not show it, so he is Aa.", "Su madre solo pudo darle a; él no lo manifiesta, así que es Aa.")),
        (t("Two parents who both show a recessive trait (aa × aa) have four children. How many are expected to show it?", "Dos padres que manifiestan un rasgo recesivo (aa × aa) tienen cuatro hijos. ¿Cuántos se espera que lo manifiesten?"),
         [t("All four", "Los cuatro"), t("Two", "Dos"), t("One", "Uno")], 0, t("They can only give a: every child is aa.", "Solo pueden dar a: todo hijo es aa.")),
    ]
    return [{"enun": f"<p>{q}</p>", "ops": o, "ok": k, "pista": t("Start with the person whose genotype is certain: whoever shows a recessive trait is aa.", "Empiece por quien tiene el genotipo seguro: quien manifiesta un rasgo recesivo es aa."), "exp": e} for q, o, k, e in d]


def clasif_division():
    G = ["Mitosis", "Meiosis", t("Both", "Las dos")]
    PM = t("Growth and repair, identical cells?", "¿Crecer y reparar, células idénticas?")
    PE = t("Sex cells, half the chromosomes?", "¿Gametos, la mitad de los cromosomas?")
    PB = t("Is it true of both divisions?", "¿Es cierto de las dos divisiones?")
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("Decide whether each feature belongs to mitosis, meiosis, or both.", "Decida si cada característica es de la mitosis, de la meiosis o de las dos."), "grupos": G,
                "etiqueta": t("Division:", "División:"), "piezas": [{"t": a, "v": v, "pista": [PM, PE, PB][v]} for a, v in piezas],
                "extra": t("Mitosis makes more of the same; meiosis makes sex cells with half.", "La mitosis produce más de lo mismo; la meiosis, gametos con la mitad.")}
    return [
        item(t("Set 1", "Grupo 1"), [(t("It makes two cells.", "Produce dos células."), 0), (t("It makes four cells.", "Produce cuatro células."), 1), (t("The DNA is copied first.", "El ADN se duplica antes."), 2),
                                    (t("It makes egg and sperm cells.", "Forma óvulos y espermatozoides."), 1), (t("It repairs a cut on the skin.", "Repara una herida de la piel."), 0)]),
        item(t("Set 2", "Grupo 2"), [(t("Each new cell has 46 chromosomes (in humans).", "Cada célula nueva tiene 46 cromosomas (en el ser humano)."), 0), (t("Each new cell has 23 chromosomes (in humans).", "Cada célula nueva tiene 23 cromosomas (en el ser humano)."), 1),
                                    (t("The new cells are all different from each other.", "Las células nuevas son todas distintas entre sí."), 1), (t("It is a kind of cell division.", "Es un tipo de división celular."), 2), (t("It has only one division.", "Tiene una sola división."), 0)]),
    ]


def practica():
    A = {"en": ["mitosis-meiosis", "punnett", "formats", "two-genes", "sex-linked", "family-trees"], "es": ["mitosis-meiosis", "punnett", "formatos", "dos-genes", "ligada-al-sexo", "arboles"]}[C.L]
    mods = [
        (A[0], t("Mitosis or meiosis?", "¿Mitosis o meiosis?"), C.clasifica("m1", t("Choose the division for each feature.", "Elija la división de cada característica."))),
        (A[1], t("One-gene crosses", "Cruces de un gen"), C.om("m2", t("Draw the square on paper. The solution shows it.", "Dibuje el cuadro en papel. La solución lo muestra."))),
        (A[2], t("Fraction, decimal, percent, and ratio", "Fracción, decimal, porcentaje y razón"), C.om("m3", t("Fraction = part of the whole. Ratio = part to part.", "Fracción = parte del total. Razón = parte frente a parte."))),
        (A[3], t("Two-gene crosses", "Cruces de dos genes"), C.om("m4", t("Sex cells, boxes, and the 9 : 3 : 3 : 1 ratio.", "Gametos, casillas y la proporción 9 : 3 : 3 : 1."))),
        (A[4], t("Sex-linked crosses", "Cruces ligados al sexo"), C.om("m5", t("Sons and daughters, read separately.", "Hijos e hijas, por separado."))),
        (A[5], t("Reason with family trees", "Razone con árboles genealógicos"), C.om("m6", t("Start with whoever has a certain genotype.", "Empiece por quien tiene el genotipo seguro."))),
    ]
    js = (C.js_datos("DIV", clasif_division()) + C.js_datos("MON", banco_monohibrido()) + C.js_datos("FOR", banco_formatos()) + C.js_datos("DIH", banco_dihibrido()) +
          C.js_datos("LIG", banco_ligado()) + C.js_datos("ARB", banco_arboles()) +
          'creaClasifica("m1", DIV);\ncreaBanco("m2", MON);\ncreaBanco("m3", FOR);\ncreaBanco("m4", DIH);\ncreaBanco("m5", LIG);\ncreaBanco("m6", ARB);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one · calculator included", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"), mods, js, calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
