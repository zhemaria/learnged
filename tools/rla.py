# -*- coding: utf-8 -*-
"""Artes del Lenguaje (RLA) de LearnGED: estándares del GED® y CCR, para los dos caminos.

Este módulo reúne lo que comparten el camino en inglés (rla/level-N/) y el camino en español
(es/artes-del-lenguaje/nivel-N/):

  · RLA: los objetivos de evaluación del examen (R.2 a R.9, W.1 a W.3, L.1 y L.2) con su DOK y
    el estándar ancla CCR al que se alinean, en inglés y en español.
  · CCR: qué dice cada estándar ancla (Pimentel, 2013).
  · CONVENCIONES_EN / CONVENCIONES_ES: las trampas de edición de cada idioma. Los códigos L.1 y
    L.2 son los mismos en los dos exámenes, pero lo que se corrige es distinto: el examen en
    inglés pide inglés estándar y el examen en español, la norma del español.
  · estandares(cods, base, camino): el recuadro «Estándares de esta lección» de cada lección,
    con el mismo aspecto que en Ciencias y Estudios Sociales (clases std-* de /math/lesson.css).

La página de consulta con todo esto la construye tools/build_rla_estandares.py:
  rla/ged-standards.html y es/artes-del-lenguaje/estandares-ged.html.

Fuente de los objetivos, los DOK y la alineación: GED Testing Service, Assessment Guide for
Educators: Reasoning Through Language Arts (2016), capítulo 1. Los textos de los indicadores
están resumidos con palabras propias, en inglés y en español.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

L = "en"


def t(en, es):
    return en if L == "en" else es


# ---------------------------------------------------------------- objetivos de evaluación
# Cada objetivo: (título EN, título ES, anclas CCR, dominio). Dominio: lectura, argumento, escritura, lenguaje.
OBJETIVOS = {
    "R.2": ("Central ideas, themes, and summary", "Ideas centrales, temas y resumen", ["R.2"], "lectura"),
    "R.3": ("How events, characters, and ideas develop and interact", "Cómo se desarrollan y se relacionan hechos, personajes e ideas", ["R.3"], "lectura"),
    "R.4": ("Word meaning, tone, and figurative language", "Significado de las palabras, tono y lenguaje figurado", ["R.4", "L.4"], "lectura"),
    "R.5": ("Text structure and organization", "Estructura y organización del texto", ["R.5"], "lectura"),
    "R.6": ("Author's purpose and point of view", "Propósito y punto de vista del autor", ["R.6"], "lectura"),
    "R.7/R.9": ("Comparing texts and formats", "Comparar textos y formatos", ["R.7", "R.9"], "lectura"),
    "R.8": ("Evaluating arguments and evidence", "Evaluar argumentos y evidencia", ["R.8"], "argumento"),
    "W.1": ("Using evidence from the texts", "Usar la evidencia de los textos", ["R.1", "W.1"], "escritura"),
    "W.2": ("Writing the extended response", "Escribir la respuesta extendida", ["W.1", "W.2", "W.4"], "escritura"),
    "W.3": ("Clear writing and command of conventions", "Escritura clara y dominio de las normas", ["W.5", "L.1", "L.2", "L.3"], "escritura"),
    "L.1": ("Grammar and usage", "Gramática y uso", ["L.1"], "lenguaje"),
    "L.2": ("Capitalization and punctuation", "Mayúsculas y puntuación", ["L.2"], "lenguaje"),
}

# Indicadores: código -> (objetivo, DOK, texto EN, texto ES)
RLA = {
    "R.2.1": ("R.2", "1–2", "Understand explicit details and main ideas.", "Comprender los detalles explícitos y las ideas principales."),
    "R.2.2": ("R.2", "2", "Summarize details and ideas in a text.", "Resumir los detalles y las ideas de un texto."),
    "R.2.3": ("R.2", "2–3", "Make sentence-level inferences about details that support main ideas.", "Hacer inferencias, oración por oración, sobre los detalles que apoyan las ideas principales."),
    "R.2.4": ("R.2", "2–3", "Infer main ideas that are implied in paragraphs or whole texts.", "Inferir las ideas principales que no se dicen en un párrafo o en el texto completo."),
    "R.2.5": ("R.2", "1–3", "Decide which details support a main idea.", "Decidir qué detalles apoyan una idea principal."),
    "R.2.6": ("R.2", "1–3", "Identify a theme, or the elements that support it.", "Identificar un tema o los elementos que lo sostienen."),
    "R.2.7": ("R.2", "2–3", "Make evidence-based generalizations or hypotheses and apply them to new situations.", "Formular generalizaciones o hipótesis basadas en la evidencia y aplicarlas a situaciones nuevas."),
    "R.2.8": ("R.2", "2–3", "Draw conclusions that require putting several main ideas together.", "Sacar conclusiones que exigen reunir varias ideas principales."),
    "R.3.1": ("R.3", "1–2", "Put events in order.", "Ordenar una secuencia de hechos."),
    "R.3.2": ("R.3", "2", "Make inferences about plot, characters, setting, or ideas.", "Hacer inferencias sobre la trama, los personajes, el ambiente o las ideas."),
    "R.3.3": ("R.3", "2–3", "Analyze relationships within a text: how events shape the plot, how ideas connect, how context shapes meaning.", "Analizar las relaciones dentro de un texto: cómo los hechos mueven la trama, cómo se conectan las ideas, cómo el contexto da sentido."),
    "R.3.4": ("R.3", "2–3", "Infer unstated relationships: cause and effect, parallel ideas, contrast.", "Inferir relaciones que no se dicen: causa y efecto, ideas paralelas, contraste."),
    "R.3.5": ("R.3", "2–3", "Analyze the role that details play in a complex text.", "Analizar qué papel cumplen los detalles en un texto complejo."),
    "R.4.1": ("R.4", "1–3", "Determine the meaning of words and phrases in context, including connotative and figurative meanings.", "Determinar el significado de palabras y frases por el contexto, incluidos los sentidos connotativo y figurado."),
    "R.4.2": ("R.4", "2", "Analyze how replacing one word with another changes meaning or tone.", "Analizar cómo cambian el significado o el tono al cambiar una palabra por otra."),
    "R.4.3": ("R.4", "2–3", "Analyze the effect of specific words, phrases, or figures of speech on the author's purpose.", "Analizar el efecto de palabras, frases o figuras retóricas concretas en el propósito del autor."),
    "R.5.1": ("R.5", "2–3", "Analyze how a sentence, paragraph, or section fits into the whole text and develops its ideas.", "Analizar cómo una oración, un párrafo o una sección encajan en el texto completo y desarrollan sus ideas."),
    "R.5.2": ("R.5", "2–3", "Analyze how two sections next to each other relate (one develops, refines, or contrasts the other).", "Analizar la relación entre dos secciones seguidas (una desarrolla, precisa o contrasta la otra)."),
    "R.5.3": ("R.5", "2", "Analyze transition and signal words and what they do in the text.", "Analizar las palabras de transición y los conectores y qué función cumplen en el texto."),
    "R.5.4": ("R.5", "2–3", "Analyze how the structure of a text shapes meaning, stresses ideas, or supports the author's purpose.", "Analizar cómo la estructura del texto da sentido, destaca ideas o apoya el propósito del autor."),
    "R.6.1": ("R.6", "1–2", "Determine the author's point of view or purpose.", "Determinar el punto de vista o el propósito del autor."),
    "R.6.2": ("R.6", "2–3", "Analyze how the author sets his or her position apart from others or answers objections.", "Analizar cómo el autor distingue su postura de otras o responde a las objeciones."),
    "R.6.3": ("R.6", "2", "Infer the author's implicit and explicit purposes from details in the text.", "Inferir los propósitos implícitos y explícitos del autor a partir de los detalles del texto."),
    "R.6.4": ("R.6", "2–3", "Analyze the rhetorical techniques an author uses to support a position (analogy, enumeration, repetition and parallelism, contrast, qualifying statements).", "Analizar las técnicas retóricas con que el autor defiende una postura (analogía, enumeración, repetición y paralelismo, contraste, enunciados matizados)."),
    "R.9.1/R.7.1": ("R.7/R.9", "2–3", "Compare two texts on a similar topic, or a text with data in a table, graph, or timeline.", "Comparar dos textos sobre un tema parecido, o un texto con datos de una tabla, una gráfica o una línea del tiempo."),
    "R.9.2": ("R.7/R.9", "2–3", "Compare two passages of the same kind for point of view, tone, style, structure, or purpose.", "Comparar dos textos del mismo tipo en punto de vista, tono, estilo, estructura o propósito."),
    "R.9.3": ("R.7/R.9", "2–3", "Compare two opposing arguments and how each one uses evidence.", "Comparar dos argumentos opuestos y cómo usa la evidencia cada uno."),
    "R.7.2": ("R.7/R.9", "2–3", "Analyze how data or a graphic extends, clarifies, or contradicts a text.", "Analizar cómo unos datos o un gráfico amplían, aclaran o contradicen un texto."),
    "R.7.3": ("R.7/R.9", "2–3", "Compare passages in different formats or genres for scope, purpose, audience, or impact.", "Comparar textos de distinto formato o género en alcance, propósito, público o efecto."),
    "R.7.4": ("R.7/R.9", "2–3", "Put together details from several sources and formats to draw a conclusion or apply information.", "Reunir detalles de varias fuentes y formatos para sacar una conclusión o aplicar la información."),
    "R.8.1": ("R.8", "2–3", "Trace the steps of an argument and how its claims build on each other.", "Seguir los pasos de un argumento y cómo se apoyan unas afirmaciones en otras."),
    "R.8.2": ("R.8", "1–3", "Identify the evidence used to support a claim or conclusion.", "Identificar la evidencia que apoya una afirmación o una conclusión."),
    "R.8.3": ("R.8", "2–3", "Evaluate whether the evidence is relevant and enough.", "Evaluar si la evidencia es pertinente y suficiente."),
    "R.8.4": ("R.8", "2–3", "Tell supported claims from unsupported claims.", "Distinguir las afirmaciones sustentadas de las que no lo están."),
    "R.8.5": ("R.8", "2–3", "Judge whether the reasoning is valid; identify fallacies and their effect.", "Juzgar si el razonamiento es válido; identificar falacias y su efecto."),
    "R.8.6": ("R.8", "2–3", "Identify unstated premises or assumptions and evaluate their support.", "Identificar las premisas o los supuestos que no se dicen y evaluar su respaldo."),
    "W.1": ("W.1", "1–3", "Find explicit details and make logical inferences or valid claims that the text evidence supports.", "Encontrar los detalles explícitos y hacer inferencias lógicas o afirmaciones válidas que la evidencia del texto respalde."),
    "W.2": ("W.2", "2–3", "Write an analytic response with a clear claim, logical order, well-chosen evidence, and steady focus.", "Escribir una respuesta analítica con una tesis clara, un orden lógico, evidencia bien elegida y un enfoque constante."),
    "W.3": ("W.3", "1–2", "Write clearly and show enough command of the standard conventions of the language.", "Escribir con claridad y mostrar un dominio suficiente de las normas del idioma."),
    "L.1.1": ("L.1", "1–2", "Correct frequently confused words, homonyms, and contractions.", "Corregir palabras que se confunden con frecuencia y homónimos."),
    "L.1.2": ("L.1", "1–2", "Correct simple subject–verb agreement.", "Corregir la concordancia sencilla entre sujeto y verbo."),
    "L.1.3": ("L.1", "1–2", "Correct pronoun errors: agreement, unclear reference, and case.", "Corregir errores de pronombres: concordancia, referencia ambigua y forma (caso)."),
    "L.1.4": ("L.1", "1–2", "Replace nonstandard or informal usage.", "Sustituir el uso no normativo o demasiado informal."),
    "L.1.5": ("L.1", "1–2", "Fix dangling or misplaced modifiers and illogical word order.", "Corregir modificadores mal colocados y el orden ilógico de las palabras."),
    "L.1.6": ("L.1", "1–2", "Make series parallel and use subordination and coordination correctly.", "Lograr el paralelismo en las series y usar bien la subordinación y la coordinación."),
    "L.1.7": ("L.1", "1–2", "Correct agreement in harder cases: compound subjects, phrases between subject and verb, collective nouns.", "Corregir la concordancia en casos difíciles: sujetos compuestos, frases entre el sujeto y el verbo, sustantivos colectivos."),
    "L.1.8": ("L.1", "1–2", "Cut wordiness and awkward sentence construction.", "Eliminar las palabras de más y las construcciones torpes."),
    "L.1.9": ("L.1", "1–2", "Use transition words, conjunctive adverbs, and other words that support logic and clarity.", "Usar conectores, adverbios de enlace y otras palabras que apoyan la lógica y la claridad."),
    "L.2.1": ("L.2", "1–2", "Correct capitalization (proper nouns, titles, first word of a sentence).", "Corregir el uso de las mayúsculas (nombres propios, títulos, inicio de oración)."),
    "L.2.2": ("L.2", "1–2", "Eliminate run-on sentences, fused sentences, and fragments.", "Eliminar las oraciones fusionadas o mal unidas y los fragmentos."),
    "L.2.3": ("L.2", "1–2", "Correct apostrophes with possessive nouns.", "Corregir el apóstrofo en los posesivos (solo en inglés; en español, el posesivo se forma con «de»)."),
    "L.2.4": ("L.2", "1–2", "Correct punctuation: commas in a series, appositives, and other nonessential elements; end marks; punctuation between clauses.", "Corregir la puntuación: comas en las series, en las aposiciones y en otros elementos explicativos; signos de cierre; puntuación entre proposiciones."),
}

DOMINIOS = {
    "lectura": ("Reading for meaning", "Comprensión lectora"),
    "argumento": ("Arguments and evidence", "Argumentación y evidencia"),
    "escritura": ("Writing: the extended response", "Escritura: la respuesta extendida"),
    "lenguaje": ("Language conventions and editing", "Normas del idioma y corrección"),
}

# Categorías de informe del examen (nombres de la guía).
CATEGORIAS = [
    ("Analyzing and creating text features and technique", "Analizar y crear rasgos y técnicas del texto"),
    ("Using evidence to understand, analyze, and create arguments", "Usar la evidencia para comprender, analizar y crear argumentos"),
    ("Applying knowledge of the conventions and usage of the language", "Aplicar el conocimiento de las normas y el uso del idioma"),
]

# ---------------------------------------------------------------- estándares ancla CCR
CCR = {
    "R.1": ("Read closely to find what the text says explicitly and to make logical inferences; cite evidence.", "Leer con atención para saber qué dice el texto de forma explícita y hacer inferencias lógicas; citar la evidencia."),
    "R.2": ("Determine central ideas or themes and analyze their development; summarize key details.", "Determinar las ideas centrales o los temas y analizar su desarrollo; resumir los detalles clave."),
    "R.3": ("Analyze how individuals, events, and ideas develop and interact over a text.", "Analizar cómo se desarrollan y se relacionan las personas, los hechos y las ideas a lo largo de un texto."),
    "R.4": ("Interpret words and phrases, including technical, connotative, and figurative meanings; analyze how word choice shapes meaning or tone.", "Interpretar palabras y frases, también en sus sentidos técnico, connotativo y figurado; analizar cómo la elección de palabras da sentido o tono."),
    "R.5": ("Analyze the structure of texts and how their parts relate to each other and to the whole.", "Analizar la estructura de los textos y cómo se relacionan sus partes entre sí y con el todo."),
    "R.6": ("Assess how point of view or purpose shapes the content and style of a text.", "Valorar cómo el punto de vista o el propósito moldean el contenido y el estilo de un texto."),
    "R.7": ("Integrate and evaluate content presented in diverse formats and media.", "Integrar y evaluar contenido presentado en formatos y medios diversos."),
    "R.8": ("Trace and evaluate the argument and claims in a text, the reasoning, and the evidence.", "Seguir y evaluar el argumento y las afirmaciones de un texto, el razonamiento y la evidencia."),
    "R.9": ("Analyze how two or more texts address similar themes or topics.", "Analizar cómo tratan dos o más textos temas o asuntos parecidos."),
    "W.1": ("Write arguments to support claims, using valid reasoning and relevant, sufficient evidence.", "Escribir argumentos que sostengan una tesis con razonamiento válido y evidencia pertinente y suficiente."),
    "W.2": ("Write informative and explanatory texts that convey ideas clearly and accurately.", "Escribir textos informativos y explicativos que comuniquen ideas con claridad y precisión."),
    "W.4": ("Produce clear writing whose development, organization, and style fit the task, purpose, and audience.", "Producir una escritura clara cuyo desarrollo, organización y estilo se ajusten a la tarea, el propósito y el público."),
    "W.5": ("Develop and strengthen writing by planning, revising, editing, and rewriting.", "Desarrollar y mejorar la escritura planificando, revisando, corrigiendo y reescribiendo."),
    "L.1": ("Show command of the conventions of standard grammar and usage.", "Dominar las normas de la gramática y el uso del idioma estándar."),
    "L.2": ("Show command of the conventions of capitalization, punctuation, and spelling.", "Dominar las normas de las mayúsculas, la puntuación y la ortografía."),
    "L.3": ("Apply knowledge of language to understand how it works in different contexts and make effective choices.", "Aplicar el conocimiento del idioma para entender cómo funciona en distintos contextos y elegir con acierto."),
    "L.4": ("Determine or clarify the meaning of unknown words using context clues, word parts, and reference materials.", "Determinar o aclarar el significado de palabras desconocidas con pistas del contexto, partes de la palabra y obras de consulta."),
}

# ---------------------------------------------------------------- convenciones de cada examen
# (código, trampa, ejemplo incorrecto → correcto). El camino en inglés usa CONVENCIONES_EN;
# el camino en español, CONVENCIONES_ES. Las explicaciones de CONVENCIONES_EN van en los dos
# idiomas porque la página de consulta del camino en inglés también se lee en español.
CONVENCIONES_EN = [
    ("L.1.1", ("Confused words: there / their / they're; its / it's; your / you're; to / too / two; affect / effect; accept / except; whose / who's; past / passed",
               "Palabras que se confunden: there / their / they're; its / it's; your / you're; to / too / two; affect / effect; accept / except; whose / who's; past / passed"),
     "The company updated <s>it's</s> <b>its</b> policy because <b>it's</b> necessary."),
    ("L.1.2 · L.1.7", ("Agreement: the verb agrees with the real subject, not with the noun right before it; with either…or / neither…nor, with the closer subject; collective nouns (team, committee) usually take a singular verb",
                       "Concordancia: el verbo concuerda con el sujeto real, no con el sustantivo que tiene delante; con either…or / neither…nor, con el sujeto más cercano; los colectivos (team, committee) suelen llevar verbo en singular"),
     "The box of documents <s>have</s> <b>has</b> been misplaced."),
    ("L.1.3", ("Pronoun case and reference: subject form (I, he, they) vs. object form (me, him, them); every pronoun needs a clear antecedent",
               "Pronombres: forma de sujeto (I, he, they) frente a forma de objeto (me, him, them); todo pronombre necesita un antecedente claro"),
     "The director asked Marcus and <s>I</s> <b>me</b> to write the summary."),
    ("L.1.4", ("Informal usage: try and → try to; could of → could have; double negatives",
               "Uso informal: try and → try to; could of → could have; dobles negaciones"),
     "We will <s>try and</s> <b>try to</b> finish today."),
    ("L.1.5", ("Modifiers: an opening phrase must describe the subject that comes right after it",
               "Modificadores: la frase inicial debe describir al sujeto que viene justo después"),
     "Walking into the lab, <s>the experiment was observed</s> <b>the scientist observed the experiment</b>."),
    ("L.1.6", ("Parallelism: the items in a series have the same grammatical form",
               "Paralelismo: los elementos de una serie tienen la misma forma gramatical"),
     "…scheduling shifts, training workers, and <s>to prepare</s> <b>preparing</b> reports."),
    ("L.1.8", ("Wordiness: say it once and say it directly", "Palabras de más: dígalo una vez y de forma directa"),
     "<s>In my personal opinion I think that</s> <b>I think</b> the plan works."),
    ("L.1.9", ("Transitions: choose the word that shows the right logic (however = contrast, therefore = result)",
               "Conectores: elija la palabra que muestra la lógica correcta (however = contraste, therefore = consecuencia)"),
     "Sales fell; <s>therefore</s> <b>however</b>, profits rose."),
    ("L.2.1", ("Capital letters: proper nouns, official titles before a name, first word of a sentence; not seasons or common nouns",
               "Mayúsculas: nombres propios, cargos delante del nombre, primera palabra de la oración; no las estaciones ni los nombres comunes"),
     "We met <b>Mayor</b> Ruiz in the <s>Spring</s> <b>spring</b>."),
    ("L.2.2", ("Sentence boundaries: fragments, run-ons, and comma splices (two sentences joined only by a comma)",
               "Límites de la oración: fragmentos, oraciones fusionadas y comma splice (dos oraciones unidas solo con una coma)"),
     "The results were positive<s>, however,</s><b>; however,</b> more testing is needed."),
    ("L.2.3", ("Apostrophes: student's (one), students' (more than one), children's (irregular plural)",
               "Apóstrofo: student's (uno), students' (varios), children's (plural irregular)"),
     "the <s>students</s> <b>students'</b> assignments"),
    ("L.2.4", ("Commas: in a series, around nonessential information, between clauses joined by and/but/so",
               "Comas: en las series, alrededor de la información explicativa, entre proposiciones unidas por and/but/so"),
     "Dr. Adams<b>,</b> the lead researcher<b>,</b> presented the findings."),
]

CONVENCIONES_ES = [
    ("L.1.1", "Palabras que suenan igual y se escriben distinto: hay / ahí / ay; haber / a ver; hecho / echo; tuvo / tubo; valla / vaya / baya; sino / si no; porque / por qué / porqué / por que",
     "Quiero saber <s>porque</s> <b>por qué</b> llegó tarde."),
    ("L.1.1", "Tilde diacrítica: él / el, tú / tu, mí / mi, sé / se, más / mas, sí / si, té / te; qué, cómo, dónde en preguntas y exclamaciones, también indirectas",
     "<s>El</s> <b>Él</b> dijo que <s>tu</s> <b>tú</b> lo sabías."),
    ("L.1.2 · L.1.7", "Concordancia de sujeto y verbo, y de género y número: el verbo concuerda con el núcleo del sujeto aunque haya otra frase en medio; «la mayoría de…», «el grupo de…»",
     "El catálogo con las descripciones de los cursos <s>están</s> <b>está</b> en la oficina."),
    ("L.1.3", "Pronombres: le / les con su antecedente («les dije a ellos»), leísmo y laísmo, referencia ambigua",
     "<s>Le</s> <b>Les</b> expliqué a los empleados el nuevo horario."),
    ("L.1.4", "Uso no normativo: «haiga» → haya, «hubieron problemas» → hubo problemas, «habían muchas personas» → había, queísmo y dequeísmo («pienso de que» → pienso que)",
     "<s>Habían</s> <b>Había</b> muchas personas en la reunión."),
    ("L.1.5", "Modificadores y orden: el complemento va junto a lo que modifica; gerundio de posterioridad («chocó, muriendo…» → chocó y murió)",
     "<s>Se vende mesa para niño de madera</s> <b>Se vende mesa de madera para niño</b>."),
    ("L.1.6", "Paralelismo: los elementos de una serie con la misma forma (todos infinitivos, todos sustantivos…)",
     "Se encarga de organizar turnos, formar al personal y <s>la preparación de</s> <b>preparar</b> informes."),
    ("L.1.8", "Redundancias y palabras de más: «subir arriba», «volver a repetir», «en mi opinión personal creo que»",
     "<s>Volvió a repetir</s> <b>Repitió</b> las instrucciones."),
    ("L.1.9", "Conectores: sin embargo (contraste), por lo tanto (consecuencia), además (suma); van entre comas o tras punto y coma",
     "Las ventas bajaron; <s>por lo tanto</s> <b>sin embargo</b>, las ganancias subieron."),
    ("L.2.1", "Mayúsculas: nombres propios e inicio de oración; los días, los meses, los idiomas y los gentilicios van en minúscula; en los títulos de obras, solo la primera palabra",
     "La reunión es el <s>Lunes</s> <b>lunes</b> 3 de <s>Marzo</s> <b>marzo</b>."),
    ("L.2.2", "Límites de la oración: fragmentos y oraciones unidas solo con una coma",
     "El técnico revisó el equipo<s>,</s><b>;</b> todo funciona bien."),
    ("L.2.4", "Puntuación: signos de apertura ¿ ¡; nunca coma entre el sujeto y el verbo; comas en las series (sin coma antes de «y»), en las aposiciones y con los conectores; raya en el diálogo",
     "<b>¿</b>Cuándo empieza la clase? · Los estudiantes del turno de la noche<s>,</s> llegan a las seis."),
    ("L.2.4", "Acentuación general: agudas, llanas y esdrújulas; los hiatos (día, país, oír)",
     "La <s>reunion</s> <b>reunión</b> del <s>dia</s> <b>día</b> fue <s>rapida</s> <b>rápida</b>."),
]

# ---------------------------------------------------------------- formato del examen
FORMATO = {
    "en": [
        "<strong>150 minutes</strong> in three parts, with a <strong>10-minute break</strong> before the last one. The extended response has its own <strong>45 minutes</strong>.",
        "<strong>Texts:</strong> about 75% informational (science, social studies, the workplace) and 25% literature. Reading passages run 400 to 900 words; editing passages, 350 to 450.",
        "<strong>Question types:</strong> multiple choice, drop-down (choose the right word or phrase inside a passage; this is how grammar is tested), drag-and-drop, select an area, and fill in the blank.",
        "<strong>The extended response:</strong> two texts that argue about the same issue. You decide which argument is better supported and explain why, with evidence from both texts. It is scored on three traits, 0 to 2 points each (6 points); the score counts double in the RLA total.",
        "<strong>Score:</strong> 145 to pass; 165 to 174 is <em>GED College Ready</em>, and 175 to 200 is <em>College Ready + Credit</em>.",
    ],
    "es": [
        "<strong>150 minutos</strong> en tres partes, con un <strong>descanso de 10 minutos</strong> antes de la última. La respuesta extendida tiene sus propios <strong>45 minutos</strong>.",
        "<strong>Textos:</strong> alrededor de un 75 % informativos (ciencias, estudios sociales, el trabajo) y un 25 % literarios. Los textos de lectura tienen de 400 a 900 palabras; los de corrección, de 350 a 450.",
        "<strong>Tipos de pregunta:</strong> opción múltiple, menú desplegable (elegir la palabra o la frase correcta dentro de un texto; así se evalúa la gramática), arrastrar y soltar, seleccionar un área y completar el espacio en blanco.",
        "<strong>La respuesta extendida:</strong> dos textos que discuten sobre el mismo asunto. Usted decide qué argumento está mejor sustentado y explica por qué, con evidencia de los dos textos. Se califica en tres rasgos, de 0 a 2 puntos cada uno (6 puntos); la nota cuenta doble en el total de RLA.",
        "<strong>Puntuación:</strong> 145 para aprobar; de 165 a 174 es <em>GED College Ready</em>, y de 175 a 200, <em>College Ready + Credit</em>.",
    ],
}

RASGOS = [
    (("Trait 1 · Argument and use of evidence", "Rasgo 1 · Argumento y uso de la evidencia"),
     ("States which argument is better supported and backs the answer with relevant evidence from both texts; looks at the quality of the evidence and the reasoning, not at personal opinion.",
      "Dice qué argumento está mejor sustentado y lo respalda con evidencia pertinente de los dos textos; analiza la calidad de la evidencia y del razonamiento, no la opinión personal.")),
    (("Trait 2 · Development and organization", "Rasgo 2 · Desarrollo y organización"),
     ("Ideas in a logical order, developed with explanation; clear introduction, body, and conclusion; transitions; a formal register that fits the task.",
      "Ideas en un orden lógico y desarrolladas con explicación; introducción, desarrollo y conclusión claros; conectores; un registro formal adecuado a la tarea.")),
    (("Trait 3 · Clarity and conventions", "Rasgo 3 · Claridad y normas del idioma"),
     ("Varied, well-built sentences, precise words, and few errors of grammar, spelling, and punctuation; errors do not get in the way of understanding.",
      "Oraciones variadas y bien construidas, palabras precisas y pocos errores de gramática, ortografía y puntuación; los errores no impiden entender.")),
]


# ---------------------------------------------------------------- recuadro de la lección
def estandares(cods, base=(), camino="en"):
    """cods: indicadores que trabaja la lección; base: los que prepara.
    camino: 'en' (examen en inglés) o 'es' (examen en español): cambia la nota de las normas."""
    def li(cls, c):
        obj, dok, en, es = RLA[c]
        anclas = ", ".join(OBJETIVOS[obj][2])
        return (f'<li><span class="std-cod {cls}">{c}</span> {t(en, es)}<br><span class="std-meta">'
                f'{t("Target", "Objetivo")} {obj} · DOK {dok} · CCR {anclas}</span></li>')
    usados = []
    for c in list(cods) + list(base):
        for k in OBJETIVOS[RLA[c][0]][2]:
            if k not in usados:
                usados.append(k)
    s = [f'<details class="estandares" id="{t("ged-standards", "estandares-ged")}">',
         f'<summary><span aria-hidden="true">🎓</span> {t("Standards for this lesson (GED® and CCR)", "Estándares de esta lección (GED® y CCR)")}</summary>',
         '<div class="std-cuerpo">',
         f'<p class="std-tit">{t("GED® Reasoning Through Language Arts indicators that this lesson works on:", "Indicadores del examen GED® de Razonamiento a través de las Artes del Lenguaje que trabaja esta lección:")}</p><ul>' +
         "".join(li("std-dir", c) for c in cods) + "</ul>"]
    if base:
        s.append(f'<p class="std-tit">{t("It also builds the base for:", "También prepara la base para:")}</p><ul>' + "".join(li("std-base", c) for c in base) + "</ul>")
    if any(c.startswith("L.") for c in list(cods) + list(base)) and camino == "es":
        s.append('<p>' + t("On the GED test in Spanish, the L codes are the same, but what you correct follows the rules of Spanish.",
                           "En el examen GED en español, los códigos L son los mismos, pero lo que se corrige sigue la norma del español (tildes, concordancia, signos de apertura, mayúsculas…).") + '</p>')
    s.append(f'<p class="std-tit">{t("What the CCR anchor standards mean:", "Qué significan los estándares ancla CCR:")}</p><ul class="std-clave">' +
             "".join(f'<li><span class="std-cod std-ccr">{k}</span> {t(*CCR[k])}</li>' for k in usados) + "</ul>")
    pag = t("/rla/ged-standards.html", "/es/artes-del-lenguaje/estandares-ged.html")
    s.append('<p class="std-fuente">' + t(
        f'DOK (depth of knowledge): 1 = recall, 2 = use a skill or concept, 3 = reason with evidence. Source of the indicators, DOK ranges, and alignment: GED Testing Service, <cite>Assessment Guide for Educators: Reasoning Through Language Arts</cite> (2016). The CCR anchor standards are in Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>. <a href="{pag}">All the RLA standards</a>.',
        f'DOK (profundidad de conocimiento): 1 = recordar, 2 = aplicar una destreza o un concepto, 3 = razonar con evidencia. Fuente de los indicadores, los rangos de DOK y la alineación: GED Testing Service, <cite>Assessment Guide for Educators: Reasoning Through Language Arts</cite> (2016). Los estándares ancla CCR están en Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>. <a href="{pag}">Todos los estándares de RLA</a>.') + "</p>")
    s.append("</div>\n</details>")
    return "\n".join(s)
