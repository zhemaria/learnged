"""LearnGED · Ciencias · Lección 4.1 · ADN, ARN y expresión genética (EN/ES).
Fuente: clases_ciencias/leccion_4-1.html (diagramas en tools/svg/4-1_*.svg) y el interactivo ciencias/genetica.
Uso: python3 tools/build_sci_4_1.py
"""
import os, sys, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "4-1"


def titulo():
    return t("DNA, RNA, and gene expression", "ADN, ARN y expresión genética")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


LET = {k: k for k in "ATCGU"}


def svg_helice():
    tr = dict(LET)
    tr.update({"Hebra 1": "Strand 1", "Hebra 2": "Strand 2", "A con T · C con G · siempre": "A with T · C with G · always"})
    return C.svg_orig("4-1_0", tr, "Diagram of the two strands of DNA paired up. Strand one has the sequence adenine, thymine, cytosine, guanine, adenine, thymine. Strand two has the matching sequence: thymine, adenine, guanine, cytosine, thymine, adenine. Each adenine always pairs with a thymine, and each cytosine with a guanine.")


def svg_expresion():
    return C.svg_orig("4-1_1", {"transcripción": "transcription", "traducción": "translation", "ADN": "DNA", "ARN": "Messenger", "mensajero": "RNA", "Proteína": "Protein",
                                 "en el núcleo": "in the nucleus", "sale al citoplasma": "goes out to the cytoplasm", "en el ribosoma": "at the ribosome",
                                 "Tres letras del ARN mensajero, un aminoácido": "Three letters of messenger RNA, one amino acid"},
                       "Diagram of gene expression in two steps. From the DNA, in the nucleus, messenger RNA is made by transcription. From the messenger RNA, now at the ribosome, the protein is made by translation.")


def svg_mutacion():
    tr = {"Secuencia normal": "Normal sequence", "Con una sustitución": "With one substitution", "metionina": "methionine", "prolina": "proline", "ácido glutámico": "glutamic acid",
          "alto": "stop", "valina": "valine", "Una sola letra distinta, un aminoácido distinto": "One letter different, one amino acid different"}
    for c in ("AUG", "CCU", "GAG", "UAG", "GUG"):
        tr[c] = c
    return C.svg_orig("4-1_2", tr, "Comparison of a normal sequence and the same sequence with a substitution of one base. The normal sequence has the codons A U G, C C U, G A G, U A G, which are translated as methionine, proline, glutamic acid, and stop. In the mutated sequence, the third codon changes from G A G to G U G, and the amino acid changes from glutamic acid to valine. The other amino acids do not change.")


CODIGO = {"AUG": ("Methionine", "Metionina"), "CCU": ("Proline", "Prolina"), "GAG": ("Glutamic acid", "Ácido glutámico"), "GUG": ("Valine", "Valina"),
          "UUU": ("Phenylalanine", "Fenilalanina"), "UAG": ("Stop", "Alto"), "UAA": ("Stop", "Alto"), "UGA": ("Stop", "Alto")}
COMP_ADN = {"A": "T", "T": "A", "C": "G", "G": "C"}
COMP_ARN = {"A": "U", "T": "A", "C": "G", "G": "C"}


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("DNA is a ladder twisted around itself: that is the <strong>double helix</strong>. The two sides of the ladder are made of sugar and phosphate; each rung is two <strong>bases</strong> facing each other.", "El ADN es una escalera retorcida sobre sí misma: eso es la <strong>doble hélice</strong>. Los dos largueros están formados por azúcar y fosfato; cada peldaño lo forman dos <strong>bases nitrogenadas</strong> enfrentadas.")}</p>
<p>{t("There are only four bases (adenine, thymine, cytosine, and guanine), and they do not pair just any way. The rule has no exceptions:", "Hay solo cuatro bases —adenina, timina, citosina y guanina— y no se emparejan de cualquier manera. La regla no admite excepciones:")}</p>
{C.caja("tip", t("The base-pairing rule", "La regla de complementariedad"), "<p>" + t("Adenine always pairs with thymine, and cytosine always with guanine: <strong>A with T</strong> and <strong>C with G</strong>. That gives you something very useful: if you know one strand, the other one is completely set. You do not memorize it; you work it out.", "La adenina siempre se empareja con la timina, y la citosina siempre con la guanina: <strong>A con T</strong> y <strong>C con G</strong>. De ahí se sigue algo muy útil: conocida una hebra, la otra queda determinada por completo. No hay que memorizarla, se deduce.") + "</p>")}
{svg_helice()}
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>DNA</strong> stands for <strong>d</strong>eoxyribo<strong>n</strong>ucleic <strong>a</strong>cid. The three pieces say what it is: {R('nucleic')}, from the nucleus, where it was found; {R('ribo-')}, for ribose, the sugar in the sides of the ladder; and {R('deoxy-')}, from <em>de-</em>, without, plus oxygen, because that ribose is missing one oxygen. <strong>RNA</strong> is the same name <em>without</em> the deoxy-: ribonucleic acid, with the full ribose. The difference between the two names is one atom, and the name tells you which.", f"<strong>ADN</strong> son las siglas de ácido <strong>d</strong>esoxirribo<strong>n</strong>ucleico. Las tres piezas dicen qué es: {R('nucleico')}, del núcleo, donde se encontró; {R('ribo-')}, por la ribosa, el azúcar que forma los largueros; y {R('desoxi-')}, del griego <em>des-</em>, sin, más oxígeno, porque a esa ribosa le falta un oxígeno. El <strong>ARN</strong> es el mismo nombre <em>sin</em> el desoxi-: ácido ribonucleico, con la ribosa completa. La diferencia entre ambas siglas está en un solo átomo, y ese átomo está anunciado en el nombre.")}</p>
{P(t("Try it 1 · The other strand", "Pruebe 1 · La otra hebra"), t("If one DNA strand reads A T G C, the matching strand reads…", "Si una hebra de ADN dice A T G C, la hebra complementaria dice…"),
   ["A T G C", "T A C G", "G C A T"], 1,
   {0: t("That is the same strand. Pair each base.", "Esa es la misma hebra. Empareje cada base."), 2: t("That is the strand backward. Pair A with T and C with G.", "Esa es la hebra al revés. Empareje A con T y C con G.")},
   t("A→T, T→A, G→C, C→G.", "A→T, T→A, G→C, C→G."))}
{C.enlace(N, anc("pairing", "emparejar"), t("pair the bases", "empareje las bases"), t("New strands every time: write the matching strand.", "Hebras nuevas cada vez: escriba la hebra complementaria."))}"""

    s2 = f"""<p>{t("DNA stores the information and never leaves the nucleus. RNA is a working copy that does leave: it carries the message to the ribosome and then breaks down. Think of an office file: the original is kept locked up, and what goes around the office is a photocopy.", "El ADN guarda la información y no sale del núcleo. El ARN es una copia de trabajo que sí sale, lleva el mensaje al ribosoma y después se degrada. La comparación con un archivo lo explica: el original se conserva bajo llave y lo que circula por la oficina es una fotocopia.")}</p>
{C.tabla(t("DNA and RNA compared: strands, sugar, bases, location, and job", "Comparación entre el ADN y el ARN según número de hebras, azúcar, bases, ubicación y función"),
 [t("Feature", "Característica"), t("DNA", "ADN"), t("RNA", "ARN")],
 [[t("Number of strands", "Número de hebras"), t("Two, wound into a double helix.", "Dos, enrolladas en doble hélice."), t("One.", "Una sola.")],
  [t("Sugar", "Azúcar"), t("Deoxyribose.", "Desoxirribosa."), t("Ribose.", "Ribosa.")],
  [t("Bases", "Bases"), "A, T, C, G.", t("A, <strong>U</strong>, C, G. Uracil takes the place of thymine.", "A, <strong>U</strong>, C, G. El uracilo ocupa el lugar de la timina.")],
  [t("Where it is", "Ubicación"), t("In the nucleus, which it does not leave.", "En el núcleo, del que no sale."), t("Made in the nucleus; goes out to the cytoplasm.", "Se fabrica en el núcleo y sale al citoplasma.")],
  [t("Job", "Función"), t("Store the information permanently.", "Almacenar la información de forma permanente."), t("Carry the message to the ribosome to build the protein.", "Llevar el mensaje hasta el ribosoma para fabricar la proteína.")]])}
{C.caja("ojo", t("The only letter that changes", "La única letra que cambia"), "<p>" + t("Going from DNA to RNA, thymine is replaced by uracil. Where DNA says T, RNA says U. It is the most common mistake in transcription exercises: you copy the T out of habit, and everything after it is wrong. Always check the finished sequence for any T that slipped through.", "Al pasar de ADN a ARN, la timina se sustituye por uracilo. Donde el ADN dice T, el ARN dice U. Es el error más frecuente en los ejercicios de transcripción: se copia la T por costumbre y toda la secuencia posterior queda mal. Conviene revisar siempre la secuencia terminada buscando alguna T superviviente.") + "</p>")}
{P(t("Try it 2 · Never in RNA", "Pruebe 2 · Nunca en el ARN"), t("Which base never appears in RNA?", "En una molécula de ARN nunca aparece…"),
   [t("Uracil", "El uracilo"), t("Guanine", "La guanina"), t("Thymine", "La timina")], 2,
   {0: t("Uracil is the RNA base that replaces thymine.", "El uracilo es la base del ARN que sustituye a la timina."), 1: t("Guanine is in both.", "La guanina está en los dos.")},
   t("RNA uses U instead of T.", "El ARN usa U en lugar de T."))}
{P(t("Try it 3 · One atom", "Pruebe 3 · Un átomo"), t("The difference between the names DNA and RNA refers to…", "La diferencia entre las siglas ADN y ARN se refiere a…"),
   [t("one oxygen missing from the sugar of DNA", "un oxígeno de menos en el azúcar del ADN"), t("the number of different bases", "el número de bases distintas"), t("the size of the nucleus", "el tamaño del núcleo")], 0,
   {1: t("Both have four bases.", "Los dos tienen cuatro bases."), 2: t("The name says nothing about the nucleus size.", "El nombre no dice nada del tamaño del núcleo.")},
   t("Deoxy- = without one oxygen.", "Desoxi- = sin un oxígeno."))}
{C.enlace(N, anc("dna-rna", "adn-arn"), t("DNA, RNA, or both?", "¿ADN, ARN o los dos?"), t("Sort each feature into the right molecule.", "Coloque cada característica en la molécula que le corresponde."))}"""

    tabla_codigo = C.tabla(t("Simplified genetic code: the codons used in this lesson and the amino acid or order each one stands for", "Tabla simplificada del código genético con los codones que se emplean en esta lección y el aminoácido u orden que designa cada uno"),
        [t("RNA codon", "Codón del ARN"), t("Meaning", "Significado"), t("Note", "Observación")],
        [["AUG", t("Methionine", "Metionina"), t("It also marks where reading starts.", "Marca además el comienzo de la lectura.")],
         ["CCU", t("Proline", "Prolina"), "—"], ["GAG", t("Glutamic acid", "Ácido glutámico"), "—"],
         ["GUG", t("Valine", "Valina"), t("Differs from the one above by one letter.", "Se diferencia del anterior en una sola letra.")],
         ["UUU", t("Phenylalanine", "Fenilalanina"), "—"],
         ["UAG, UAA, UGA", t("Stop", "Alto"), t("They do not stand for any amino acid: they stop the reading.", "No designan aminoácido: detienen la lectura.")]])
    s3 = f"""<p>{t("The information in DNA is not used directly: it is copied and then translated. These are two steps with precise names and different places.", "La información del ADN no se usa directamente: se copia y se traduce. Son dos pasos con nombres precisos y con lugares distintos.")}</p>
{svg_expresion()}
<p>{t("Messenger RNA is read three letters at a time. Each group of three bases is called a <strong>codon</strong> and stands for one specific amino acid, or for the order to stop. The amino acids linked together make the protein.", "El ARN mensajero se lee de tres en tres. Cada grupo de tres bases se llama <strong>codón</strong> y designa un aminoácido concreto, o bien la orden de detenerse. Los aminoácidos encadenados forman la proteína.")}</p>
{tabla_codigo}
{C.ejemplo(t("Example 1 · From a DNA strand to a protein", "Ejemplo 1 · De una hebra de ADN a una proteína"),
 [("", t("Start with the DNA template strand: <strong>TAC · GGA · CTC · ATC</strong>", "Se parte de la hebra molde de ADN: <strong>TAC · GGA · CTC · ATC</strong>")),
  ("1", t("<strong>Transcription.</strong> Write the matching sequence, with uracil instead of thymine: A with U, T with A, C with G, G with C.", "<strong>Transcripción.</strong> Se escribe la secuencia complementaria, sustituyendo la timina por uracilo: A con U, T con A, C con G, G con C.")),
  ("2", t("The messenger RNA is: <strong>AUG · CCU · GAG · UAG</strong>", "El ARN mensajero resulta ser: <strong>AUG · CCU · GAG · UAG</strong>")),
  ("3", t("<strong>Translation.</strong> Look up each codon in the table: AUG is methionine, CCU is proline, GAG is glutamic acid, and UAG is the order to stop.", "<strong>Traducción.</strong> Se consulta cada codón en la tabla: AUG es metionina, CCU es prolina, GAG es ácido glutámico y UAG es la orden de alto."))],
 t("<strong>Result:</strong> a chain of three amino acids (methionine, proline, and glutamic acid), and the reading ends there. The stop codon adds no amino acid: it only says where to stop.", "<strong>Resultado:</strong> una cadena de tres aminoácidos —metionina, prolina y ácido glutámico— y ahí termina la lectura. El codón de alto no aporta ningún aminoácido: solo indica dónde parar."))}
{C.caja("ojo", t("Read in threes, without shifting", "Leer de tres en tres, sin desplazarse"), "<p>" + t("Codons are counted from the start and always in threes, without skipping or repeating any base. If a letter is lost while copying, every codon after it shifts and the protein comes out nothing like the right one. Separate the groups of three with a dot before translating, as in the example.", "Los codones se cuentan desde el principio y siempre de tres en tres, sin saltarse ni repetir ninguna base. Si al copiar la secuencia se pierde una letra, todos los codones siguientes se desplazan y la proteína resultante no se parece en nada a la correcta. Conviene separar los tríos con un punto antes de traducir, tal como se hace en el ejemplo.") + "</p>")}
{P(t("Try it 4 · Transcribe", "Pruebe 4 · Transcriba"), t("The DNA template T A C is transcribed as the RNA codon…", "La hebra molde de ADN T A C se transcribe como el codón de ARN…"),
   ["A U G", "A T G", "T A C"], 0,
   {1: t("RNA has no T: use U.", "El ARN no tiene T: use U."), 2: t("That is the same strand.", "Esa es la misma hebra.")},
   t("T→A, A→U, C→G: AUG, the start codon.", "T→A, A→U, C→G: AUG, el codón de inicio."))}
{P(t("Try it 5 · Where?", "Pruebe 5 · ¿Dónde?"), t("Translation happens in…", "La traducción ocurre en…"),
   [t("the nucleus", "el núcleo"), t("the ribosome", "el ribosoma"), t("the mitochondrion", "la mitocondria")], 1,
   {0: t("Transcription happens in the nucleus.", "La transcripción ocurre en el núcleo."), 2: t("The mitochondrion releases energy.", "La mitocondria libera energía.")},
   t("The ribosome is the assembly line for proteins (Lesson 3.1).", "El ribosoma es la línea de montaje de proteínas (Lección 3.1)."))}
{C.enlace(N, anc("transcribe", "transcribir"), t("transcribe DNA into RNA", "transcriba el ADN a ARN"), t("Write the messenger RNA. Watch out for T.", "Escriba el ARN mensajero. Cuidado con la T."))}
{C.enlace(N, anc("translate", "traducir"), t("from DNA to protein", "del ADN a la proteína"), t("Transcribe, split into codons, and translate with the table.", "Transcriba, separe en codones y traduzca con la tabla."))}"""

    s4 = f"""<p>{t("A <strong>point mutation</strong> is a change in a single base. It seems small, and sometimes it is, but it can change the protein completely.", "Una <strong>mutación puntual</strong> es el cambio de una sola base. Parece poca cosa y a veces lo es, pero puede alterar por completo la proteína resultante.")}</p>
{svg_mutacion()}
{C.tabla(t("Three possible effects of a point mutation on the protein", "Tres efectos posibles de una mutación puntual sobre la proteína resultante"),
 [t("Possible effect", "Efecto posible"), t("What happens", "Qué ocurre"), t("What it does to the protein", "Consecuencia sobre la proteína")],
 [[t("No effect", "Ningún efecto"), t("The codon changes, but the new one stands for the same amino acid. Several codons code for the same amino acid.", "El codón cambia, pero el nuevo designa el mismo aminoácido. Varios codones distintos codifican el mismo aminoácido."), t("The protein is identical. The mutation goes unnoticed.", "La proteína es idéntica. La mutación pasa inadvertida.")],
  [t("One amino acid changes", "Cambio de un aminoácido"), t("The new codon stands for a different amino acid, as when GAG becomes GUG.", "El nuevo codón designa un aminoácido distinto, como en el paso de GAG a GUG."), t("The protein is complete, but it may work worse, the same, or even better.", "La proteína se forma completa, pero puede funcionar peor, igual o incluso mejor.")],
  [t("Early stop", "Alto prematuro"), t("The new codon turns out to be a stop order where there was none.", "El nuevo codón resulta ser una orden de alto donde no la había."), t("The protein is cut short and almost always stops working.", "La proteína queda incompleta y casi siempre deja de funcionar.")]])}
{C.caja("ojo", t("A mutation is not “good” or “bad” by itself", "Una mutación no es «buena» ni «mala» por sí misma"), "<p>" + t("The test checks this idea often, and it goes against intuition. The effect of a mutation depends on the <strong>environment</strong> the living thing lives in. The same variant can be harmful in one place and helpful in another, as you will see in this lesson’s reading and, above all, in Lesson 4.3 with natural selection.", "Es una idea que el examen evalúa con frecuencia y que resulta contraintuitiva. El efecto de una mutación depende del <strong>ambiente</strong> en que vive el organismo. La misma variante puede ser perjudicial en un lugar y ventajosa en otro, como se verá en la lectura de esta lección y, sobre todo, en la Lección 4.3 al estudiar la selección natural.") + "</p>")}
{P(t("Try it 6 · An early stop", "Pruebe 6 · Un alto prematuro"), t("A mutation turns a normal codon into a stop codon. You can expect the protein to…", "Una mutación convierte un codón normal en un codón de alto. Cabe esperar que la proteína…"),
   [t("form the same as before", "se forme igual que antes"), t("be longer than usual", "sea más larga de lo habitual"), t("be cut short and probably not work", "quede incompleta y probablemente no funcione")], 2,
   {0: t("Reading stops at the new stop codon.", "La lectura se detiene en el nuevo codón de alto."), 1: t("A stop codon ends the chain sooner, not later.", "Un codón de alto termina la cadena antes, no después.")},
   t("Everything after the new stop is never built.", "Todo lo que va después del nuevo alto nunca se fabrica."))}
{P(t("Try it 7 · A lost letter", "Pruebe 7 · Una letra perdida"), t("One base is lost by mistake while copying a sequence. As a result…", "Al copiar una secuencia se pierde una base por descuido. La consecuencia es que…"),
   [t("every codon after it shifts, and the protein is different", "todos los codones siguientes se desplazan y la proteína resulta distinta"), t("only that codon changes", "solo cambia el codón afectado"), t("nothing happens", "no hay ninguna consecuencia")], 0,
   {1: t("Reading in threes moves every later group.", "Leer de tres en tres desplaza todos los grupos siguientes."), 2: t("Every later codon changes.", "Cambian todos los codones siguientes.")},
   t("A lost letter shifts the reading frame.", "Una letra perdida desplaza el marco de lectura."))}
{C.enlace(N, anc("mutations", "mutaciones"), t("what does the mutation do?", "¿qué hace la mutación?"), t("Compare the normal and changed codons and predict the effect on the protein.", "Compare el codón normal y el cambiado y prediga el efecto sobre la proteína."))}"""

    s5 = f"""<p>{t("A short science text written for this level. Notice that the final conclusion depends on the environment, not only on the molecule.", "Texto científico breve adaptado al nivel. Observe que la conclusión final depende del ambiente y no solo de la molécula.")}</p>
{C.lectura(t("One letter that changes a life", "Una letra que cambia una vida"),
 [t("Hemoglobin is the protein in red blood cells that carries oxygen. The gene for it has, in most people, a codon that stands for glutamic acid at one particular place in the chain.", "La hemoglobina es la proteína de los glóbulos rojos que transporta el oxígeno. El gen que la codifica tiene, en la mayoría de las personas, un codón que designa el ácido glutámico en una posición determinada de la cadena."),
  t("In some people that codon has one different base, and the amino acid built in is no longer glutamic acid but valine. The change affects one link in a chain of hundreds, but that is enough to change how the whole molecule behaves: when it gives up its oxygen, this hemoglobin tends to stick to itself and form stiff fibers.", "En algunas personas ese codón presenta una sola base distinta, y el aminoácido que se incorpora ya no es el ácido glutámico sino la valina. El cambio afecta a un solo eslabón de una cadena de cientos, pero basta para alterar el comportamiento de la molécula completa: cuando cede su oxígeno, esta hemoglobina tiende a unirse consigo misma formando fibras rígidas."),
  t("The red blood cells that contain it lose their round shape and become long and curved, like a sickle, which gives the disease its name: sickle cell anemia. These cells move through the body with difficulty, block the smallest vessels, and are destroyed too soon, which causes pain and anemia.", "Los glóbulos rojos que las contienen pierden su forma redondeada y adoptan una silueta alargada, semejante a una hoz, que da nombre a la enfermedad: anemia falciforme. Esas células circulan con dificultad, obstruyen los vasos más finos y se destruyen antes de tiempo, lo que produce dolor y anemia."),
  t("For years, the puzzling question was why such a harmful variant had not disappeared. The answer came from looking at where it is found: the variant is more common in regions where malaria is common. A person who inherits the allele from only one parent does not develop the disease and is also less likely to get sick from malaria. In those regions, carrying one copy is an advantage; in regions without malaria, that advantage disappears.", "La cuestión que durante años resultó desconcertante es por qué una variante tan perjudicial no había desaparecido. La respuesta llegó al observar su distribución geográfica: la variante es más frecuente en regiones donde la malaria es común. Quien hereda el alelo de un solo progenitor no desarrolla la enfermedad y además resulta menos vulnerable a la malaria. En esas regiones, portar una copia resulta ventajoso; en regiones sin malaria, esa ventaja desaparece.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Hemoglobin carries oxygen in red blood cells.", "La hemoglobina transporta oxígeno en los glóbulos rojos."), t("Sickle cell anemia is a painful disease.", "La anemia falciforme es una enfermedad dolorosa."), t("Changing one base changes the protein, and the effect of that change depends on the environment.", "El cambio de una sola base altera la proteína, y el efecto de esa alteración depende del ambiente.")], 2,
   {0: t("True, but it is the starting fact, not the main idea.", "Es cierto, pero es el dato de partida, no la idea central."), 1: t("True, but the text goes further.", "Es cierto, pero el texto va más allá.")},
   t("From one letter to the protein, and from the protein to the environment.", "De una letra a la proteína, y de la proteína al ambiente."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("According to the text, the amino acid that replaces glutamic acid is…", "Según el texto, el aminoácido que sustituye al ácido glutámico es…"),
   [t("valine", "la valina"), t("proline", "la prolina"), t("methionine", "la metionina")], 0,
   {1: t("Look at the second paragraph.", "Mire el segundo párrafo."), 2: t("Look at the second paragraph.", "Mire el segundo párrafo.")},
   t("Second paragraph: valine. It is the GAG → GUG change of the diagram.", "Segundo párrafo: la valina. Es el cambio GAG → GUG del diagrama."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("Why has the variant not disappeared in some regions?", "¿Por qué la variante no ha desaparecido en ciertas regiones?"),
   [t("Because it causes no symptoms", "Porque no produce ningún síntoma"), t("Because a person with one copy is less likely to get sick from malaria", "Porque quien hereda una sola copia resulta menos vulnerable a la malaria"), t("Because mutations never disappear", "Porque las mutaciones nunca desaparecen")], 1,
   {0: t("With two copies it causes serious disease.", "Con dos copias causa una enfermedad grave."), 2: t("The text does not say that.", "El texto no dice eso.")},
   t("Last paragraph: one copy protects against malaria.", "Último párrafo: una copia protege frente a la malaria."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("From the text you can conclude that a mutation…", "El texto permite concluir que una mutación…"),
   [t("is always harmful", "siempre es perjudicial para el organismo"), t("is always helpful in the long run", "siempre resulta beneficiosa a largo plazo"), t("can be harmful or helpful depending on the environment", "puede ser perjudicial o ventajosa según el ambiente en que viva el organismo")], 2,
   {0: t("In malaria regions, one copy helps.", "En regiones con malaria, una copia ayuda."), 1: t("Without malaria, there is no advantage.", "Sin malaria, no hay ventaja.")},
   t("Same variant, different environment, different effect.", "Misma variante, distinto ambiente, distinto efecto."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK).", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SP.6.b", "1–2", t("<em>A section of one DNA strand reads: C G A T T A.</em><br>Which sequence is the matching DNA strand?", "<em>Un fragmento de una hebra de ADN dice: C G A T T A.</em><br>¿Qué secuencia es la hebra complementaria de ADN?"),
   ["G C T A A T", "G C U A A U", "C G A T T A", "A T C G G C"], 0,
   {1: t("That would be RNA. DNA has T, not U.", "Eso sería ARN. El ADN tiene T, no U."), 2: t("That is the same strand.", "Esa es la misma hebra."), 3: t("Pair C with G and A with T.", "Empareje C con G y A con T.")},
   t("C→G, G→C, A→T, T→A, T→A, A→T.", "C→G, G→C, A→T, T→A, T→A, A→T."))}
{G(2, "SP.1.b", "2", t("<em>“The ribosome reads the messenger RNA one codon at a time, adding the amino acid each codon calls for.”</em><br>In this sentence, a <em>codon</em> is…", "<em>«El ribosoma lee el ARN mensajero codón a codón, añadiendo el aminoácido que pide cada codón.»</em><br>En esta oración, un <em>codón</em> es…"),
   [t("one base of the RNA", "una base del ARN"), t("a group of three RNA bases that stands for one amino acid", "un grupo de tres bases del ARN que designa un aminoácido"), t("a whole protein", "una proteína completa"), t("a part of the ribosome", "una parte del ribosoma")], 1,
   {0: t("Reading is in threes.", "La lectura es de tres en tres."), 2: t("A protein is many amino acids.", "Una proteína son muchos aminoácidos."), 3: t("The ribosome reads codons; they are not part of it.", "El ribosoma lee los codones; no forman parte de él.")},
   t("Three bases = one codon = one amino acid (or stop).", "Tres bases = un codón = un aminoácido (o alto)."))}
{G(3, "SP.3.c", "2–3", t("<em>A normal messenger RNA reads AUG · UUU · CCU · GAG · UAA. A mutation changes the second codon from UUU to UAA.</em><br>Use the code table in section 3. What will the protein be?", "<em>Un ARN mensajero normal dice AUG · UUU · CCU · GAG · UAA. Una mutación cambia el segundo codón de UUU a UAA.</em><br>Use la tabla del código de la sección 3. ¿Cómo será la proteína?"),
   [t("Methionine only: the chain stops after the first amino acid.", "Solo metionina: la cadena se detiene tras el primer aminoácido."), t("The same as before.", "Igual que antes."), t("Methionine, proline, glutamic acid.", "Metionina, prolina, ácido glutámico."), t("Longer than before.", "Más larga que antes.")], 0,
   {1: t("UAA is a stop codon, not phenylalanine.", "UAA es un codón de alto, no fenilalanina."), 2: t("Reading never gets past the second codon.", "La lectura no pasa del segundo codón."), 3: t("A stop codon makes it shorter.", "Un codón de alto la acorta.")},
   t("AUG = methionine, then UAA = stop: an early stop leaves a chain of one amino acid.", "AUG = metionina, después UAA = alto: un alto prematuro deja una cadena de un solo aminoácido."))}
{G(4, "SP.3.a", "2", t("<em>Read the text “One letter that changes a life” in section 5.</em><br>Which sentence from the text best supports the idea that a variant can be helpful in some places?", "<em>Lea el texto «Una letra que cambia una vida» de la sección 5.</em><br>¿Qué oración del texto apoya mejor la idea de que una variante puede ser ventajosa en algunos lugares?"),
   [t("“Hemoglobin is the protein in red blood cells that carries oxygen.”", "«La hemoglobina es la proteína de los glóbulos rojos que transporta el oxígeno.»"), t("“These cells … block the smallest vessels.”", "«Esas células … obstruyen los vasos más finos.»"), t("“In those regions, carrying one copy is an advantage.”", "«En esas regiones, portar una copia resulta ventajoso.»"), t("“The change affects one link in a chain of hundreds.”", "«El cambio afecta a un solo eslabón de una cadena de cientos.»")], 2,
   {0: t("That sentence only says what hemoglobin does.", "Esa oración solo dice qué hace la hemoglobina."), 1: t("That sentence describes harm, not advantage.", "Esa oración describe un daño, no una ventaja."), 3: t("That sentence is about the size of the change.", "Esa oración trata del tamaño del cambio.")},
   t("It says directly that in malaria regions one copy helps.", "Dice directamente que en las regiones con malaria una copia ayuda."))}
{G(5, "SP.7.a", "2", t("<em>Scientists describe the flow of genetic information as a model in three parts.</em><br>Which order is correct?", "<em>La ciencia describe el flujo de la información genética como un modelo en tres partes.</em><br>¿Qué orden es el correcto?"),
   [t("Protein → RNA → DNA", "Proteína → ARN → ADN"), t("DNA → RNA → protein", "ADN → ARN → proteína"), t("RNA → DNA → protein", "ARN → ADN → proteína"), t("DNA → protein → RNA", "ADN → proteína → ARN")], 1,
   {0: t("That is backward.", "Eso es al revés."), 2: t("RNA is copied from DNA, not the other way around.", "El ARN se copia del ADN, no al revés."), 3: t("The protein is the last step.", "La proteína es el último paso.")},
   t("DNA is transcribed into RNA, and RNA is translated into protein.", "El ADN se transcribe en ARN, y el ARN se traduce en proteína."))}"""

    secciones = [
        ("s1", t("The structure of DNA and base pairing", "La estructura del ADN y la complementariedad"), s1),
        ("s2", t("DNA and RNA: two similar molecules with different jobs", "ADN y ARN: dos moléculas parecidas con oficios distintos"), s2),
        ("s3", t("From gene to protein", "Del gen a la proteína"), s3),
        ("s4", t("Point mutations", "Mutaciones puntuales"), s4),
        ("s5", t("Science reading", "Lectura científica"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Pair with cards.", "Empareje con tarjetas."), t("Cut out eight cards with the bases (two each of A, T, C, and G) and pair them on the table. Check that only two pairs are possible.", "Recorte ocho tarjetas con las bases —dos de cada una: A, T, C y G— y emparéjelas sobre la mesa. Compruebe que solo hay dos parejas posibles.")),
        (t("Transcribe and check.", "Transcriba y revise."), t("Write three DNA strands of nine letters, transcribe each one into RNA, and then look over each RNA for any T that slipped through.", "Escriba tres hebras de ADN de nueve letras, transcriba cada una a ARN y después revise cada ARN en busca de alguna T superviviente.")),
        (t("Another genetic disease.", "Otra enfermedad genética."), t("Read about another genetic disease (for example, cystic fibrosis) and write which gene and which protein are involved.", "Lea sobre otra enfermedad genética (por ejemplo, la fibrosis quística) y escriba qué gen y qué proteína intervienen.")),
    ]
    Q = t
    quiz = [
        (Q("In DNA, adenine always pairs with…", "En el ADN, la adenina se empareja siempre con…"), [Q("guanine", "la guanina"), Q("cytosine", "la citosina"), Q("thymine", "la timina"), Q("uracil", "el uracilo")], 2,
         {0: Q("Guanine pairs with cytosine.", "La guanina va con la citosina."), 1: Q("Cytosine pairs with guanine.", "La citosina va con la guanina."), 3: Q("Uracil is in RNA, not DNA.", "El uracilo está en el ARN, no en el ADN.")}, Q("A with T.", "A con T.")),
        (Q("If one DNA strand reads G G A T C, the matching strand reads…", "Si una hebra de ADN dice G G A T C, la hebra complementaria dice…"), ["C C T A G", "G G A T C", "C C U A G", "A A T G C"], 0,
         {1: Q("That is the same strand.", "Esa es la misma hebra."), 2: Q("DNA has T, not U.", "El ADN tiene T, no U."), 3: Q("Pair G with C.", "Empareje G con C.")}, Q("G→C, G→C, A→T, T→A, C→G.", "G→C, G→C, A→T, T→A, C→G.")),
        (Q("The double helix of DNA is made of…", "La estructura de doble hélice del ADN está formada por…"), [Q("one folded strand", "una sola hebra plegada"), Q("two matching strands wound together", "dos hebras complementarias enrolladas"), Q("four parallel strands", "cuatro hebras paralelas"), Q("a chain of amino acids", "una cadena de aminoácidos")], 1,
         {0: Q("One strand is RNA.", "Una hebra es el ARN."), 2: Q("Double means two.", "Doble significa dos."), 3: Q("That is a protein.", "Eso es una proteína.")}, Q("A twisted ladder: two strands.", "Una escalera retorcida: dos hebras.")),
        (Q("The base found in RNA but not in DNA is…", "La base que aparece en el ARN y no en el ADN es…"), [Q("cytosine", "la citosina"), Q("thymine", "la timina"), Q("adenine", "la adenina"), Q("uracil", "el uracilo")], 3,
         {0: Q("Cytosine is in both.", "La citosina está en los dos."), 1: Q("Thymine is only in DNA.", "La timina solo está en el ADN."), 2: Q("Adenine is in both.", "La adenina está en los dos.")}, Q("U replaces T in RNA.", "La U sustituye a la T en el ARN.")),
        (Q("Unlike DNA, RNA…", "A diferencia del ADN, el ARN…"), [Q("has one strand and leaves the nucleus", "tiene una sola hebra y sale del núcleo"), Q("has two strands and stays in the nucleus", "tiene dos hebras y permanece en el núcleo"), Q("has no bases", "no contiene bases nitrogenadas"), Q("is found only in plants", "se encuentra solo en las plantas")], 0,
         {1: Q("That describes DNA.", "Eso describe al ADN."), 2: Q("RNA has A, U, C, G.", "El ARN tiene A, U, C, G."), 3: Q("It is in every cell.", "Está en todas las células.")}, Q("The working copy: one strand, goes out to the ribosome.", "La copia de trabajo: una hebra, sale al ribosoma.")),
        (Q("The main job of DNA is to…", "La función principal del ADN es…"), [Q("carry oxygen", "transportar oxígeno"), Q("store the genetic information permanently", "almacenar de forma permanente la información genética"), Q("build proteins directly in the cytoplasm", "fabricar directamente las proteínas en el citoplasma"), Q("produce energy", "producir energía")], 1,
         {0: Q("That is hemoglobin.", "Eso hace la hemoglobina."), 2: Q("DNA does not leave the nucleus; RNA carries the message.", "El ADN no sale del núcleo; el ARN lleva el mensaje."), 3: Q("That is the mitochondrion.", "Eso hace la mitocondria.")}, Q("The original, kept under lock and key.", "El original, bajo llave.")),
        (Q("The DNA template C T C is transcribed as the RNA codon…", "La hebra molde de ADN C T C se transcribe como el codón de ARN…"), ["C U C", "G A G", "G T G", "C T C"], 1,
         {0: Q("Pair each base; do not just replace T.", "Empareje cada base; no basta con cambiar la T."), 2: Q("RNA has no T.", "El ARN no tiene T."), 3: Q("That is the same strand.", "Esa es la misma hebra.")}, Q("C→G, T→A, C→G: GAG.", "C→G, T→A, C→G: GAG.")),
        (Q("A codon is made of…", "Un codón está formado por…"), [Q("two RNA bases", "dos bases del ARN"), Q("three RNA bases", "tres bases del ARN"), Q("four RNA bases", "cuatro bases del ARN"), Q("one amino acid", "un aminoácido")], 1,
         {0: Q("Reading is in threes.", "La lectura es de tres en tres."), 2: Q("Reading is in threes.", "La lectura es de tres en tres."), 3: Q("A codon stands for an amino acid; it is not one.", "Un codón designa un aminoácido; no lo es.")}, Q("Three bases.", "Tres bases.")),
        (Q("A mutation changes the codon GAG to GUG. Using the code table, the amino acid changes from…", "Una mutación cambia el codón GAG por GUG. Según la tabla del código, el aminoácido pasa de…"), [Q("proline to methionine", "prolina a metionina"), Q("valine to glutamic acid", "valina a ácido glutámico"), Q("glutamic acid to valine", "ácido glutámico a valina"), Q("methionine to stop", "metionina a alto")], 2,
         {0: Q("Look up GAG and GUG.", "Busque GAG y GUG."), 1: Q("That is backward.", "Eso es al revés."), 3: Q("Neither codon is AUG or a stop.", "Ninguno es AUG ni de alto.")}, Q("GAG = glutamic acid; GUG = valine.", "GAG = ácido glutámico; GUG = valina.")),
        (Q("A point mutation that turns a normal codon into a stop codon produces…", "Una mutación puntual que convierte un codón normal en un codón de alto produce…"), [Q("a protein cut short that probably does not work", "una proteína incompleta que probablemente no funcione"), Q("a protein identical to the original", "una proteína idéntica a la original"), Q("a longer protein", "una proteína más larga"), Q("no change in the cell", "ningún cambio en la célula")], 0,
         {1: Q("Reading stops early.", "La lectura se detiene antes."), 2: Q("Stop makes it shorter.", "El alto la acorta."), 3: Q("The protein changes.", "La proteína cambia.")}, Q("An early stop cuts the chain.", "Un alto prematuro corta la cadena.")),
    ]
    filas = [
        (t("Pair bases correctly", "Empareja bases correctamente"), t("I write the matching strand with no mistakes and check it for impossible pairs.", "Obtengo la hebra complementaria sin errores y la reviso en busca de parejas imposibles."), t("I use the rule but make mistakes in long sequences.", "Aplico la regla, pero me equivoco en secuencias largas."), t("I pair bases without a fixed rule.", "Emparejo las bases sin una regla fija.")),
        (t("Tell DNA from RNA", "Distingue ADN de ARN"), t("I tell them apart by strands, bases, location, and job, and explain why the information is copied.", "Los distingo por hebras, bases, ubicación y función, y explico por qué la información se copia."), t("I give some difference, but not the bases or the location.", "Señalo alguna diferencia, pero no la de las bases ni la de ubicación."), t("I mix up the two molecules.", "Confundo ambas moléculas.")),
        (t("Transcribe and translate without shifting", "Transcribe y traduce sin desplazarse"), t("I transcribe and translate a whole sequence and know where reading ends.", "Transcribo y traduzco una secuencia completa y reconozco dónde termina la lectura."), t("I split the codons but leave a T in the RNA.", "Separo los codones, pero conservo alguna T en el ARN."), t("I do not split the codons, or read them unevenly.", "No separo los codones o los leo de forma irregular.")),
        (t("Explain what a mutation does", "Explica el efecto de una mutación"), t("I tell the three possible effects apart and argue that the effect on the living thing depends on the environment.", "Distingo los tres efectos posibles y argumento que el efecto sobre el organismo depende del ambiente."), t("I know some mutations have no effect, but not why.", "Reconozco que hay mutaciones sin efecto, pero no sé por qué."), t("I think every mutation destroys the protein.", "Creo que toda mutación destruye la proteína.")),
    ]
    cierre = "<p>" + t("This lesson worked at the <strong>molecular</strong> level: what a gene is and how it becomes a protein. It also left an idea that Topic 4 develops all the way: the effect of a genetic variant <strong>depends on the environment</strong>, not only on the molecule.", "Esta lección trabajó el nivel <strong>molecular</strong>: qué es un gen y cómo se convierte en una proteína. Dejó además una idea que el Tema 4 va a desarrollar entera: que el efecto de una variante genética <strong>depende del ambiente</strong>, no solo de la molécula.") + "</p><p>" + \
             t("Lesson 4.2 moves up to the level of the <strong>individual</strong>. Before building the first Punnett square, it covers <strong>meiosis</strong>, which explains where sex cells come from and why each parent gives only one allele of each pair. And the tree diagram of Lesson 2.3 comes back, this time counting offspring instead of sex cells.", "La Lección 4.2 sube al nivel del <strong>individuo</strong>. Antes de construir el primer cuadro de Punnett se estudiará la <strong>meiosis</strong>, que explica de dónde salen los gametos y por qué cada progenitor aporta un solo alelo de cada par. Y reaparecerá el diagrama de árbol de la Lección 2.3, esta vez contando descendencia en lugar de gametos.") + "</p>"
    glosario = [
        (t("DNA", "ADN"), t("Deoxyribonucleic acid: the double-stranded molecule that stores genetic information.", "Ácido desoxirribonucleico: la molécula de doble hebra que guarda la información genética.")),
        (t("RNA", "ARN"), t("Ribonucleic acid: a single-stranded working copy that carries the message to the ribosome.", "Ácido ribonucleico: copia de trabajo de una hebra que lleva el mensaje al ribosoma.")),
        (t("Base", "Base nitrogenada"), t("One of the “letters” of DNA (A, T, C, G) or RNA (A, U, C, G).", "Cada una de las «letras» del ADN (A, T, C, G) o del ARN (A, U, C, G).")),
        (t("Complementary", "Complementaria"), t("Matching by the pairing rule: A with T (or U), C with G.", "Que se corresponde según la regla: A con T (o U), C con G.")),
        (t("Transcription", "Transcripción"), t("Copying DNA into messenger RNA, in the nucleus.", "Copia del ADN en ARN mensajero, en el núcleo.")),
        (t("Translation", "Traducción"), t("Reading messenger RNA to build a protein, at the ribosome.", "Lectura del ARN mensajero para fabricar una proteína, en el ribosoma.")),
        (t("Codon", "Codón"), t("Three RNA bases that stand for one amino acid or a stop.", "Tres bases del ARN que designan un aminoácido o una orden de alto.")),
        (t("Amino acid", "Aminoácido"), t("One of the building blocks that link up to make a protein.", "Cada una de las piezas que se encadenan para formar una proteína.")),
        (t("Point mutation", "Mutación puntual"), t("A change in a single base.", "Cambio de una sola base.")),
    ]
    estd = C.estandares(["SP.6.b", "SP.1.a", "SP.1.b", "SP.3.c"], ["L.e"], base=["SP.7.a"])
    conexion = "<p>" + t("The second half of life science starts here. Topic 3 answered what a cell is and how it gets energy. Topic 4 answers how information passes from one generation to the next, how populations change over time, and how living things are organized in an ecosystem.", "Comienza la segunda mitad del dominio. El Tema 3 respondió qué es una célula y cómo obtiene energía. El Tema 4 responde cómo se transmite la información de una generación a la siguiente, cómo cambian las poblaciones con el tiempo y cómo se organizan los seres vivos en un ecosistema.") + "</p><p>" + \
               t("This lesson starts at the smallest level, the molecule; 4.2 moves up to the individual, and 4.3 to the population. Keep that order in mind: <strong>molecule, individual, population</strong>. Each step explains the next one.", "Esta lección abre por el nivel más pequeño, la molécula, y la 4.2 subirá al individuo y la 4.3 a la población. Conviene tener presente ese orden: <strong>molécula, individuo, población</strong>. Cada escalón explica el siguiente.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> work with the model before the formal explanation. Pair the base cards and discover for yourself that only two pairs are possible; the rule will be obvious once you have checked it yourself.", "<strong>Cómo estudiar esta lección:</strong> manipule el modelo antes de detenerse en la explicación formal. Empareje las tarjetas y descubra por sí mismo que solo hay dos combinaciones posibles; la regla de complementariedad le resultará evidente cuando ya la haya comprobado.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Four letters, two pairs, and a code read in threes: how a gene becomes a protein, and what one changed letter can do.", "Cuatro letras, dos parejas y un código que se lee de tres en tres: cómo un gen se convierte en proteína y qué puede hacer una letra cambiada."),
        ["SP.6 · " + t("Expressing science information", "Expresar información científica"), "SP.1 · " + t("Understanding science texts", "Comprender textos científicos")],
        [t("<strong>Describe</strong> the double helix of DNA and apply the base-pairing rule.", "<strong>Describir</strong> la estructura de doble hélice del ADN y aplicar la regla de emparejamiento de bases complementarias."),
         t("<strong>Tell</strong> DNA from RNA by structure, location, and job.", "<strong>Distinguir</strong> el ADN del ARN por su estructura, su ubicación y su función."),
         t("<strong>Explain</strong> transcription and translation in general terms, and get the amino acids from a DNA strand.", "<strong>Explicar</strong> en términos generales la transcripción y la traducción, y obtener una secuencia de aminoácidos a partir de una hebra de ADN."),
         t("<strong>Link</strong> a point mutation with its possible effect on the protein.", "<strong>Relacionar</strong> una mutación puntual con su posible efecto sobre la proteína resultante."),
         t("<strong>Recognize</strong> that the same mutation can be harmful or helpful depending on the environment.", "<strong>Reconocer</strong> que una misma mutación puede resultar perjudicial o ventajosa según el ambiente.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("4-2", t("Meiosis, Punnett squares, and genetic probability", "Meiosis, cuadros de Punnett y probabilidad genética")), glosario, P)


# ---------------------------------------------------------------- práctica
def js_hebras():
    msg = {"en": {"vacio": "Type the letters, for example TACG.", "letras": "Use only the letters A, T, C, G (and U in RNA).",
                  "T": "RNA has no T: where DNA has A, RNA has U.", "U": "DNA has no U: A pairs with T.", "igual": "You copied the same strand. Pair each base: A with T, C with G.",
                  "largo": "The answer must have one letter for each letter of the strand.", "otra": "Check each pair: A with T (U in RNA), C with G."},
           "es": {"vacio": "Escriba las letras, por ejemplo TACG.", "letras": "Use solo las letras A, T, C, G (y U en el ARN).",
                  "T": "El ARN no tiene T: donde el ADN tiene A, el ARN tiene U.", "U": "El ADN no tiene U: la A se empareja con la T.", "igual": "Copió la misma hebra. Empareje cada base: A con T, C con G.",
                  "largo": "La respuesta debe tener una letra por cada letra de la hebra.", "otra": "Revise cada pareja: A con T (U en el ARN), C con G."}}[C.L]
    enun = {"en": ('"<p>DNA strand: <strong>" + sep(s) + "</strong></p><p>Write the <strong>" + (arn ? "messenger RNA" : "matching DNA strand") + "</strong>.</p>"', '"Pair each base: " + sep(s) + " → " + sep(r) + "."'),
            "es": ('"<p>Hebra de ADN: <strong>" + sep(s) + "</strong></p><p>Escriba " + (arn ? "el <strong>ARN mensajero</strong>" : "la <strong>hebra complementaria de ADN</strong>") + ".</p>"', '"Empareje cada base: " + sep(s) + " → " + sep(r) + "."')}[C.L]
    return f"""
var MH = {json.dumps(msg, ensure_ascii=False)};
function sep(x){{ return x.match(/.{{1,3}}/g).join(" · "); }}
function evaluaHebra(r, s, arn){{
  return function(v){{
    var x = (v || "").toUpperCase().replace(/[^A-Z]/g, "");
    if (!x) return {{estado: "invalido", msg: MH.vacio}};
    if (/[^ATCGU]/.test(x)) return {{estado: "invalido", msg: MH.letras}};
    if (x === r) return {{estado: "bien"}};
    if (x.length !== r.length) return {{estado: "mal", msg: MH.largo}};
    if (arn && x.indexOf("T") >= 0 && x.replace(/T/g, "U") === r) return {{estado: "mal", msg: MH.T}};
    if (!arn && x.indexOf("U") >= 0) return {{estado: "mal", msg: MH.U}};
    if (x === s) return {{estado: "mal", msg: MH.igual}};
    return {{estado: "mal", msg: MH.otra}};
  }};
}}
function hebra(n){{ var s = ""; for (var i = 0; i < n; i++) s += elige(["A", "T", "C", "G"]); return s; }}
function gH(arn){{
  return function(){{
    var s = hebra(elige([6, 9, 9, 12])), r = "", P = arn ? {{A: "U", T: "A", C: "G", G: "C"}} : {{A: "T", T: "A", C: "G", G: "C"}};
    for (var i = 0; i < s.length; i++) r += P[s[i]];
    return {{enun: {enun[0]}, solucion: {enun[1]}, evalua: evaluaHebra(r, s, arn)}};
  }};
}}
"""


def banco_traduccion():
    rnd = random.Random(41)
    cods = ["CCU", "GAG", "GUG", "UUU"]
    stops = ["UAG", "UAA", "UGA"]
    nom = lambda c: t(*CODIGO[c])
    out = []
    for _ in range(16):
        mid = [rnd.choice(cods) for _ in range(rnd.choice([2, 3]))]
        arn = ["AUG"] + mid + [rnd.choice(stops)]
        adn = "".join({"A": "T", "U": "A", "C": "G", "G": "C"}[b] for c in arn for b in c)
        trios = " · ".join(adn[i:i + 3] for i in range(0, len(adn), 3))
        cad = [nom(c) for c in arn[:-1]]
        J = lambda xs: ", ".join(x if i == 0 else x.lower() for i, x in enumerate(xs))
        ops = [J(cad)]
        alt = cad[:]; alt[-1] = nom(rnd.choice([c for c in cods if nom(c) != cad[-1]])); ops.append(J(alt))
        ops.append(J(cad + [t("stop", "alto")]))
        ops.append(J(cad[1:] or [nom("UUU")]))
        if len(set(ops)) < 4:
            continue
        exp = t("Transcription: ", "Transcripción: ") + " · ".join(arn) + ". " + t("Translation: ", "Traducción: ") + "; ".join(f"{c} = {nom(c).lower()}" for c in arn) + ". " + t("The stop codon adds nothing.", "El codón de alto no añade nada.")
        out.append({"enun": "<p>" + t("DNA template strand:", "Hebra molde de ADN:") + f" <strong>{trios}</strong></p><p><strong>" + t("Which chain of amino acids does it give? Use the code table.", "¿Qué cadena de aminoácidos produce? Use la tabla del código.") + "</strong></p>",
                    "ops": ops, "ok": 0, "pista": t("First write the RNA (A→U, T→A, C→G, G→C), then look up each codon.", "Primero escriba el ARN (A→U, T→A, C→G, G→C) y después busque cada codón."), "exp": exp})
    return out


def banco_mutaciones():
    E = [t("No effect: same amino acid", "Ningún efecto: mismo aminoácido"), t("One amino acid changes", "Cambia un aminoácido"), t("Early stop: the protein is cut short", "Alto prematuro: la proteína queda incompleta")]
    d = [
        (t("GAG changes to GUG.", "GAG cambia a GUG."), 1, t("Glutamic acid → valine: one amino acid changes (sickle cell).", "Ácido glutámico → valina: cambia un aminoácido (anemia falciforme).")),
        (t("UUU changes to UAA.", "UUU cambia a UAA."), 2, t("UAA is a stop codon: the chain ends early.", "UAA es un codón de alto: la cadena termina antes.")),
        (t("GAG changes to GAA. (GAA also stands for glutamic acid.)", "GAG cambia a GAA. (GAA también designa el ácido glutámico.)"), 0, t("Same amino acid: the protein does not change.", "Mismo aminoácido: la proteína no cambia.")),
        (t("CCU changes to CCC. (CCC also stands for proline.)", "CCU cambia a CCC. (CCC también designa la prolina.)"), 0, t("Several codons code for proline: no change.", "Varios codones codifican la prolina: sin cambio.")),
        (t("GUG changes to GAG.", "GUG cambia a GAG."), 1, t("Valine → glutamic acid.", "Valina → ácido glutámico.")),
        (t("GAG changes to UAG.", "GAG cambia a UAG."), 2, t("UAG is a stop codon.", "UAG es un codón de alto.")),
        (t("UUU changes to UUC. (UUC also stands for phenylalanine.)", "UUU cambia a UUC. (UUC también designa la fenilalanina.)"), 0, t("Same amino acid.", "Mismo aminoácido.")),
        (t("CCU changes to UCU. (UCU stands for serine.)", "CCU cambia a UCU. (UCU designa la serina.)"), 1, t("Proline → serine: one amino acid changes.", "Prolina → serina: cambia un aminoácido.")),
    ]
    out = [{"enun": t("A point mutation in a codon of messenger RNA:", "Una mutación puntual en un codón del ARN mensajero:") + f"<br><strong>{x}</strong><br>" + t("What is the effect on the protein? Use the code table.", "¿Qué efecto tiene sobre la proteína? Use la tabla del código."),
            "ops": E, "ok": k, "enOrden": True, "pista": t("Look up both codons: same amino acid, a different one, or a stop?", "Busque los dos codones: ¿mismo aminoácido, otro distinto o un alto?"), "exp": f"<strong>{E[k]}.</strong> {e}"} for x, k, e in d]
    out += [
        {"enun": t("One base is <strong>lost</strong> from the middle of a gene. What happens to the protein?", "Se <strong>pierde</strong> una base en mitad de un gen. ¿Qué le pasa a la proteína?"),
         "ops": [t("Every codon after it shifts, and the protein is very different", "Todos los codones siguientes se desplazan y la proteína cambia mucho"), t("Only one amino acid changes", "Solo cambia un aminoácido"), t("Nothing changes", "No cambia nada")], "ok": 0,
         "pista": t("Reading is in threes from the start.", "La lectura es de tres en tres desde el principio."), "exp": t("A lost base shifts the reading frame for the rest of the gene.", "Una base perdida desplaza el marco de lectura del resto del gen.")},
        {"enun": t("A mutation lets a plant survive in salty soil but makes it grow more slowly in normal soil. This mutation is…", "Una mutación permite a una planta sobrevivir en suelo salino, pero la hace crecer más despacio en suelo normal. Esta mutación es…"),
         "ops": [t("helpful or harmful depending on the environment", "ventajosa o perjudicial según el ambiente"), t("always harmful", "siempre perjudicial"), t("always helpful", "siempre ventajosa")], "ok": 0,
         "pista": t("Compare the two soils.", "Compare los dos suelos."), "exp": t("Like sickle cell and malaria: the environment decides.", "Como la anemia falciforme y la malaria: el ambiente decide.")},
    ]
    return out


def clasif_adn_arn():
    G = [t("DNA only", "Solo el ADN"), t("RNA only", "Solo el ARN"), t("Both", "Los dos")]
    PD = t("Double helix, T, stays in the nucleus?", "¿Doble hélice, T, se queda en el núcleo?")
    PR = t("One strand, U, goes to the ribosome?", "¿Una hebra, U, va al ribosoma?")
    PB = t("Is it true of both molecules?", "¿Es cierto de las dos moléculas?")
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("Decide whether each feature belongs to DNA, to RNA, or to both.", "Decida si cada característica es del ADN, del ARN o de los dos."), "grupos": G,
                "etiqueta": t("Molecule:", "Molécula:"), "piezas": [{"t": a, "v": v, "pista": [PD, PR, PB][v]} for a, v in piezas],
                "extra": t("The original stays locked in the nucleus; the photocopy goes out to work.", "El original se queda bajo llave en el núcleo; la fotocopia sale a trabajar.")}
    return [
        item(t("Set 1", "Grupo 1"), [(t("It has two strands.", "Tiene dos hebras."), 0), (t("It contains uracil (U).", "Contiene uracilo (U)."), 1), (t("It contains adenine, cytosine, and guanine.", "Contiene adenina, citosina y guanina."), 2),
                                    (t("It never leaves the nucleus.", "Nunca sale del núcleo."), 0), (t("It carries the message to the ribosome.", "Lleva el mensaje al ribosoma."), 1)]),
        item(t("Set 2", "Grupo 2"), [(t("Its sugar is deoxyribose.", "Su azúcar es la desoxirribosa."), 0), (t("Its sugar is ribose.", "Su azúcar es la ribosa."), 1), (t("It is a nucleic acid.", "Es un ácido nucleico."), 2),
                                    (t("It contains thymine (T).", "Contiene timina (T)."), 0), (t("It has a single strand.", "Tiene una sola hebra."), 1), (t("It is made of bases in a sequence.", "Está formado por una secuencia de bases."), 2)]),
    ]


def banco_vocab():
    d = [
        (t("<em>Deoxy</em>ribonucleic: <em>de-</em> means…", "<em>Desoxi</em>rribonucleico: <em>des-</em> significa…"), [t("without", "sin"), t("double", "doble"), t("inside", "dentro")], 0, t("Deoxy- = without one oxygen.", "Desoxi- = sin un oxígeno.")),
        (t("<em>Nucleic</em> acid got its name because it was first found…", "El ácido <em>nucleico</em> recibió ese nombre porque se encontró por primera vez…"), [t("in the nucleus", "en el núcleo"), t("in the blood", "en la sangre"), t("in plants", "en las plantas")], 0, t("Nucleic: from the nucleus.", "Nucleico: del núcleo.")),
        (t("<em>Transcription</em> (trans- + script, writing) means…", "<em>Transcripción</em> (trans- + escribir) significa…"), [t("copying in the same “language” of bases", "copiar en el mismo «idioma» de bases"), t("changing bases into amino acids", "cambiar bases por aminoácidos"), t("breaking DNA", "romper el ADN")], 0, t("Like copying a text by hand: DNA letters into RNA letters.", "Como copiar un texto a mano: letras de ADN a letras de ARN.")),
        (t("<em>Translation</em> means passing from…", "<em>Traducción</em> significa pasar de…"), [t("the language of bases to the language of amino acids", "el idioma de las bases al idioma de los aminoácidos"), t("DNA to RNA", "ADN a ARN"), t("one cell to another", "una célula a otra")], 0, t("As when you translate from Spanish to English: a different language.", "Como al traducir del español al inglés: otro idioma.")),
        (t("A <em>double helix</em> looks like…", "Una <em>doble hélice</em> se parece a…"), [t("a twisted ladder", "una escalera retorcida"), t("a ball of thread", "una bola de hilo"), t("a flat sheet", "una hoja plana")], 0, t("Two sides and rungs, twisted.", "Dos largueros y peldaños, retorcidos.")),
        (t("A <em>point</em> mutation affects…", "Una mutación <em>puntual</em> afecta a…"), [t("a single base", "una sola base"), t("a whole chromosome", "un cromosoma entero"), t("all the genes", "todos los genes")], 0, t("A point: one spot in the sequence.", "Un punto: un solo lugar de la secuencia.")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Break the word into its parts.", "Descomponga la palabra en sus partes."), "exp": e} for q, o, k, e in d]


def practica():
    A = {"en": ["pairing", "transcribe", "translate", "mutations", "dna-rna", "words"], "es": ["emparejar", "transcribir", "traducir", "mutaciones", "adn-arn", "palabras"]}[C.L]
    def libre(pid, intro):
        return "      <p>" + intro + "</p>\n" + f'''      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos"><div class="campo"><label for="{pid}-r">{t("Answer", "Respuesta")}</label><input type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" class="ancho" id="{pid}-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''
    tabla = C.tabla(t("Simplified genetic code", "Código genético simplificado"), [t("RNA codon", "Codón del ARN"), t("Meaning", "Significado")],
                    [[c, t(*CODIGO[c])] for c in ("AUG", "CCU", "GAG", "GUG", "UUU")] + [["UAG, UAA, UGA", t("Stop", "Alto")]])
    mods = [
        (A[0], t("Pair the bases", "Empareje las bases"), libre("m1", t("Write the matching DNA strand. You can type the letters with or without spaces.", "Escriba la hebra complementaria de ADN. Puede escribir las letras con espacios o sin ellos."))),
        (A[1], t("Transcribe DNA into RNA", "Transcriba el ADN a ARN"), libre("m2", t("Write the messenger RNA. Remember: in RNA, U takes the place of T.", "Escriba el ARN mensajero. Recuerde: en el ARN, la U ocupa el lugar de la T."))),
        (A[2], t("From DNA to protein", "Del ADN a la proteína"), "      " + tabla + "\n" + C.om("m3", t("Transcribe, split into codons, and translate.", "Transcriba, separe en codones y traduzca.")).lstrip()),
        (A[3], t("What does the mutation do?", "¿Qué hace la mutación?"), "      " + tabla + "\n" + C.om("m4", t("Compare the normal codon with the changed one.", "Compare el codón normal con el cambiado.")).lstrip()),
        (A[4], t("DNA, RNA, or both?", "¿ADN, ARN o los dos?"), C.clasifica("m5", t("Choose the molecule for each feature.", "Elija la molécula de cada característica."))),
        (A[5], t("Words of genetics", "Palabras de la genética"), C.om("m6", t("Take the word apart before you answer.", "Descomponga la palabra antes de responder."))),
    ]
    js = (js_hebras() + C.js_datos("TRA", banco_traduccion()) + C.js_datos("MUT", banco_mutaciones()) + C.js_datos("MOL", clasif_adn_arn()) + C.js_datos("VOC", banco_vocab()) +
          'creaPracticaLibre("m1", gH(false));\ncreaPracticaLibre("m2", gH(true));\ncreaBanco("m3", TRA);\ncreaBanco("m4", MUT);\ncreaClasifica("m5", MOL);\ncreaBanco("m6", VOC);\n')
    return C.pagina_practica(N, titulo(), t("Six activities · new exercises every time · two tries in each one", "Seis actividades · ejercicios nuevos cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
