"""LearnGED · Ciencias · Lección 1.3 · Leer ciencia: vocabulario técnico y procedimientos de pasos múltiples (EN/ES).
Fuente: clases_ciencias/leccion_1-3.html y el interactivo ciencias/protocolo_desordenado.
Uso: python3 tools/build_sci_1_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "1-3"


def titulo():
    return t("Reading science: technical vocabulary and multistep procedures", "Leer ciencia: vocabulario técnico y procedimientos de pasos múltiples")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


def cebolla():
    return [t("Cut a small piece of onion and peel off a thin, clear layer from the inside.", "Cortar un trozo pequeño de cebolla y separar una capa fina y transparente de la cara interna."),
            t("Lay the layer flat on the glass slide, with no folds.", "Colocar la capa extendida sobre el portaobjetos, sin dobleces."),
            t("Add a drop of stain on the sample.", "Añadir una gota de colorante sobre la muestra."),
            t("Wait one minute so the stain soaks in.", "Esperar un minuto para que el colorante penetre."),
            t("Cover it with the cover slip, lowering it slowly at an angle to avoid air bubbles.", "Cubrir con el cubreobjetos inclinándolo poco a poco, para evitar burbujas de aire."),
            t("Remove the extra stain with paper towel at the edge.", "Retirar el exceso de colorante con papel absorbente por el borde."),
            t("Look first with the lowest-power lens and focus.", "Observar primero con el objetivo de menor aumento y enfocar."),
            t("Switch to the highest-power lens and adjust only the fine focus.", "Cambiar al objetivo de mayor aumento y ajustar solamente el enfoque fino.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Most science words are not new words: they are old pieces put together. If you know thirty pieces, you can get close to the meaning of hundreds of words you have never seen.", "La mayoría de los términos científicos no son palabras nuevas: son piezas antiguas ensambladas. Quien conoce treinta piezas puede aproximarse al significado de cientos de términos que nunca ha visto.")}</p>
{C.tabla(t("Common science roots and prefixes, what they mean, and words made with each one", "Raíces y afijos científicos de alta frecuencia, su significado y ejemplos de términos formados con cada uno"),
 [t("Root or prefix", "Raíz o afijo"), t("Meaning", "Significado"), t("Examples", "Ejemplos")],
 [[R("bio-"), t("life", "vida"), t("Biology, biodiversity, biomass, antibiotic.", "Biología, biodiversidad, biomasa, antibiótico.")],
  [R(t("photo-", "foto-")), t("light", "luz"), t("Photosynthesis, photoreceptor, photon.", "Fotosíntesis, fotorreceptor, fotón.")],
  [R(t("hydro-", "hidro-")), t("water", "agua"), t("Hydrosphere, hydrolysis, dehydration.", "Hidrosfera, hidrólisis, deshidratación.")],
  [R("termo-" if C.L == "es" else "thermo-"), t("heat, temperature", "calor, temperatura"), t("Thermometer, thermodynamics, exothermic.", "Termómetro, termodinámica, exotérmico.")],
  [R("endo-"), t("inside, inward", "dentro, hacia adentro"), t("Endothermic (takes in heat), endoskeleton.", "Endotérmico (absorbe calor), endoesqueleto.")],
  [R("exo-"), t("outside, outward", "fuera, hacia afuera"), t("Exothermic (gives off heat), exoskeleton.", "Exotérmico (libera calor), exoesqueleto.")],
  [R("-sis"), t("process, action", "proceso, acción"), t("Photosynthesis, osmosis, mitosis, hydrolysis.", "Fotosíntesis, ósmosis, mitosis, hidrólisis.")],
  [R(t("-logy", "-logía")), t("study of", "estudio o tratado de"), t("Biology, geology, ecology, meteorology.", "Biología, geología, ecología, meteorología.")]])}
{C.ejemplo(t("Example 1 · A word you have never seen", "Ejemplo 1 · Un término nunca visto"),
 [("", t("A text talks about the <strong>hydrolysis</strong> of a large molecule. You do not know the word.", "Un texto menciona la <strong>hidrólisis</strong> de una molécula grande. El estudiante no conoce la palabra.")),
  ("1", t(f"Separate the pieces you know: {R('hydro-')} and {R('-lysis')}.", f"Se separan las piezas conocidas: {R('hidro-')} y {R('-lisis')}.")),
  ("2", t(f"{R('Hydro-')} means water. The ending {R('-lysis')} appears in <em>analysis</em> and <em>paralysis</em>: it has to do with breaking apart or loosening.", f"{R('Hidro-')} es agua. El sufijo {R('-lisis')} aparece en <em>análisis</em> y en <em>parálisis</em>: tiene que ver con separar o deshacer.")),
  ("3", t("Guess a meaning before you look it up: breaking something apart with water.", "Se propone un significado antes de consultar: separar algo mediante agua."))],
 t("<strong>Result:</strong> the guess is right. Hydrolysis is breaking a molecule apart with water. You did not need to memorize it.", "<strong>Resultado:</strong> la aproximación es correcta. La hidrólisis es la ruptura de una molécula por acción del agua. No hizo falta memorizarla."))}
{C.caja("tip", t("Endo- and exo- are worth points", "Endo- y exo- valen puntos"), "<p>" + t("This pair shows up on the test very often in Topic 5, with chemical reactions. An <strong>exo</strong>thermic reaction gives off heat to the <strong>outside</strong>; an <strong>endo</strong>thermic one takes heat <strong>in</strong>. If you remember the two pieces, you do not need to memorize the two definitions.", "Este par aparece en el examen con mucha frecuencia en el Tema 5, con las reacciones químicas. Una reacción <strong>exo</strong>térmica libera calor hacia <strong>fuera</strong>; una <strong>endo</strong>térmica lo absorbe hacia <strong>dentro</strong>. Quien retiene las dos partículas no necesita memorizar las dos definiciones.") + "</p>")}
{P(t("Try it 1 · Exothermic", "Pruebe 1 · Exotérmica"),
   t("An <strong>exothermic</strong> reaction is one that…", "Una reacción <strong>exotérmica</strong> es aquella que…"),
   [t("Only happens inside a living thing", "Ocurre solamente dentro de un ser vivo"), t("Takes in heat from around it", "Absorbe calor del ambiente"), t("Gives off heat to the outside", "Libera calor hacia el exterior")], 2,
   {0: t("Nothing in the word talks about living things. Look at the two pieces: exo- and thermo-.", "Nada en la palabra habla de seres vivos. Mire las dos piezas: exo- y termo-."),
    1: t("Taking heat in is “inward”: that would be endo-. What does exo- mean?", "Absorber calor es «hacia adentro»: eso sería endo-. ¿Qué significa exo-?")},
   t("Exo- (outward) + thermo- (heat): it gives off heat to the outside.", "Exo- (hacia fuera) + termo- (calor): libera calor hacia el exterior."))}
{P(t("Try it 2 · Photosynthesis", "Pruebe 2 · Fotosíntesis"),
   t("If photo- means light and -sis means process, then <strong>photosynthesis</strong> must be…", "Sabiendo que foto- es luz y -sis es proceso, la <strong>fotosíntesis</strong> debe ser…"),
   [t("A process that uses light", "Un proceso que utiliza la luz"), t("The study of light", "El estudio de la luz"), t("An instrument that measures light", "Un instrumento que mide la luz")], 0,
   {1: t("“The study of” would be -logy. The word ends in -sis.", "«El estudio de» sería -logía. La palabra termina en -sis."),
    2: t("An instrument that measures would end in -meter.", "Un instrumento que mide terminaría en -metro.")},
   t("Photo- (light) + -sis (process): a process that uses light. Plants use it to make their food.", "Foto- (luz) + -sis (proceso): un proceso que utiliza la luz. Las plantas lo usan para fabricar su alimento."))}
{P(t("Try it 3 · Hydrosphere", "Pruebe 3 · Hidrosfera"),
   t("The <strong>hydrosphere</strong> is, most likely…", "La <strong>hidrosfera</strong> es, con toda probabilidad…"),
   [t("The study of the oceans", "El estudio de los océanos"), t("All the water on the planet", "El conjunto del agua del planeta"), t("A device that measures humidity", "Un aparato para medir la humedad")], 1,
   {0: t("A “study of” word would end in -logy.", "Un término de «estudio» terminaría en -logía."),
    2: t("A measuring device would end in -meter.", "Un aparato de medida terminaría en -metro.")},
   t("Hydro- (water) + sphere (ball, the planet): all the water of the Earth, like the atmosphere is all its air.", "Hidro- (agua) + esfera (el planeta): el conjunto del agua de la Tierra, igual que la atmósfera es todo su aire."))}
{C.enlace(N, anc("roots", "raices"), t("break the word apart", "descomponga el término"), t("Twelve science words you may not know. Use the roots to work out what they mean.", "Doce términos científicos que quizá no conozca. Use las raíces para deducir su significado."))}"""

    s2 = f"""<p>{t("Not every word can be broken apart. When it cannot, the author of a science text almost always leaves a clue near the word, because the author wants to be understood. Knowing the kind of clue speeds up your reading a lot.", "No todo término se deja descomponer. En esos casos, el autor de un texto científico casi siempre deja una pista cerca de la palabra, porque le interesa que se le entienda. Reconocer el tipo de pista acelera muchísimo la lectura.")}</p>
{C.tabla(t("Four kinds of context clues, the signal words that give them away, and an example of each", "Cuatro tipos de pista de contexto, las señales que las delatan y un ejemplo de cada una"),
 [t("Kind of clue", "Tipo de pista"), t("Signal words", "Señales que la delatan"), t("Example", "Ejemplo")],
 [[t("Definition", "Definición directa"), t("<em>that is, in other words, is defined as</em>, commas or parentheses that explain", "<em>es decir, o sea, se define como</em>, comas o paréntesis explicativos"), t("<strong>Homeostasis</strong>, that is, keeping the inside of the body steady, takes energy.", "La <strong>homeostasis</strong>, es decir, el mantenimiento de condiciones internas estables, exige energía.")],
  [t("Example", "Ejemplo"), t("<em>for example, such as, like, including</em>", "<em>por ejemplo, como, tales como, entre ellos</em>"), t("<strong>Arthropods</strong>, such as insects, crabs, and spiders, have an exoskeleton.", "Los <strong>artrópodos</strong>, como los insectos, los cangrejos y las arañas, tienen exoesqueleto.")],
  [t("Contrast", "Contraste"), t("<em>in contrast, unlike, whereas, but, however</em>", "<em>en cambio, a diferencia de, mientras que, pero, sin embargo</em>"), t("<strong>Autotrophs</strong> make their own food; heterotrophs, in contrast, must get it from outside.", "Las especies <strong>autótrofas</strong> fabrican su alimento; las heterótrofas, en cambio, deben obtenerlo.")],
  [t("Synonym", "Sinónimo cercano"), t("<em>also called, known as, or simply</em>", "<em>también llamado, conocido como, o simplemente</em>"), t("<strong>Precipitation</strong>, also called rain when it falls as a liquid, brings water back to the ground.", "La <strong>precipitación</strong>, también llamada lluvia cuando cae en forma líquida, devuelve el agua al suelo.")]])}
{C.caja("ojo", t("A contrast can trick you if you read fast", "El contraste engaña si se lee rápido"), "<p>" + t("In “autotrophs make their own food; heterotrophs, in contrast, must get it from outside,” the word defined by the second half is <em>heterotroph</em>. <em>In contrast</em> tells you that what follows is the <strong>opposite</strong> of what came before. If you read only half the sentence, you get the definition backward.", "En «las autótrofas fabrican su alimento; las heterótrofas, en cambio, deben obtenerlo», la segunda mitad define la palabra <em>heterótrofa</em>. <em>En cambio</em> avisa de que lo que sigue es lo <strong>contrario</strong> de lo anterior. Leer solo la mitad de la oración conduce a la definición invertida.") + "</p>")}"""

    pasos = cebolla()
    s3 = f"""<p>{t("A lab procedure is not a list of suggestions: it is a <strong>sequence</strong>. Each step sets up what the next step needs. Switching two steps or skipping one does not just slow the experiment down: it ruins it.", "Un protocolo de laboratorio no es una lista de sugerencias: es una <strong>secuencia</strong>. Cada paso prepara la condición que el siguiente necesita. Invertir dos pasos o saltarse uno no retrasa el experimento: lo invalida.")}</p>
<div class="ejemplo"><p class="titulo-ej">{t("Example 2 · An eight-step procedure", "Ejemplo 2 · Protocolo de ocho pasos")}</p>
<p>{t("Preparing a sample of onion skin to see its cells under the microscope:", "Preparación de una muestra de epidermis de cebolla para observar sus células al microscopio:")}</p>
{"".join(f'<p class="paso"><span aria-hidden="true" class="n">{i}</span>{x}</p>' for i, x in enumerate(pasos, 1))}
</div>
{C.caja("ojo", t("What happens if the order changes", "Qué ocurre si se altera el orden"), "<p>" + t("Staining after covering keeps the stain from reaching the cells. Starting with the highest power leaves the sample out of view and you have to start over. Covering all at once, without tilting, traps bubbles that can look like parts of a cell.", "Colorear después de cubrir impide que el colorante llegue a las células. Empezar por el mayor aumento deja la muestra fuera de campo y obliga a comenzar de nuevo. Cubrir de golpe, sin inclinar, atrapa burbujas que se confunden con estructuras celulares.") + "</p>")}
{C.caja("tip", t("Words that mark the order", "Palabras que marcan la secuencia"), "<p>" + t("<em>First, next, then, once, before, after that, last, finally.</em> When you read a procedure, underline them: they are the skeleton of the order, and the answer to a test question is often right in one of them.", "<em>Primero, a continuación, después, una vez que, antes de, seguidamente, por último, finalmente.</em> Al leer un procedimiento conviene subrayarlas: son el esqueleto del orden y, con frecuencia, la respuesta a la pregunta del examen está justo en una de ellas.") + "</p>")}
{C.caja("tip", t("Three ways to check the order", "Tres maneras de comprobar el orden"), "<ul><li>" + t("<strong>Look for what a step needs.</strong> If step 4 talks about “the stained sample,” it cannot come before the step that stains it. The clue is usually in a noun, not in the verb.", "<strong>Busque lo que el paso necesita.</strong> Si el paso 4 habla de «la muestra ya coloreada», no puede ir antes del paso que la colorea. La pista suele estar en un sustantivo, no en el verbo.") +
 "</li><li>" + t("<strong>Try switching them in your head.</strong> If you switch two steps and the answer is “nothing happens,” they can go in either order. If the answer is “it can’t be done” or “it would be ruined,” you have found the order.", "<strong>Pruebe a invertirlos mentalmente.</strong> Si al intercambiar dos pasos la respuesta es «no pasa nada», el orden da igual. Si es «no se podría hacer» o «se estropearía», ya tiene el orden.") +
 "</li><li>" + t("<strong>Some steps really can be switched,</strong> and the test will not ask you about those, because there would be no single right answer.", "<strong>Algunos pasos sí son intercambiables,</strong> y el examen no preguntará por ellos, porque no tendría una única respuesta correcta.") + "</li></ul>")}
{C.enlace(N, anc("order", "orden"), t("the mixed-up procedure", "el protocolo desordenado"), t("Three lab procedures with their steps mixed up. Put them in order and see what would happen in the lab if two were switched.", "Tres protocolos de laboratorio con los pasos revueltos. Póngalos en orden y vea qué pasaría en el laboratorio si dos quedaran invertidos."))}"""

    s4 = f"""<p>{t("The <strong>central idea</strong> is what the whole text says. The <strong>supporting details</strong> are the facts, examples, and numbers that back it up. Taking an eye-catching detail for the central idea is the most common mistake, and the test always offers that option among the wrong answers.", "La <strong>idea central</strong> es aquello que el texto sostiene en su conjunto. Los <strong>detalles de apoyo</strong> son los datos, ejemplos y cifras que la sostienen. Confundir un detalle llamativo con la idea central es el error más común, y el examen ofrece siempre esa opción entre los distractores.")}</p>
<p>{t("The <strong>structure</strong> is the way the author organized that idea. In science texts, three structures cover almost every case.", "La <strong>estructura</strong> es la forma en que el autor organizó esa idea. En textos científicos, tres estructuras cubren casi todos los casos.")}</p>
{C.tabla(t("Three structures of science texts, the signal words that identify them, and the question each one answers", "Tres estructuras de texto científico, las señales que las identifican y la pregunta que responde cada una"),
 [t("Structure", "Estructura"), t("Signal words", "Señales"), t("Question the text answers", "Pregunta que responde el texto")],
 [[t("Sequence", "Secuencia"), t("<em>first, then, next, while, last, finally</em>", "<em>primero, después, a continuación, mientras, por último, finalmente</em>"), t("In what order does it happen?", "¿En qué orden ocurre?")],
  [t("Cause and effect", "Causa y efecto"), t("<em>because, due to, causes, leads to, therefore, as a result</em>", "<em>porque, debido a, provoca, produce, por lo tanto, como resultado, en consecuencia</em>"), t("Why does it happen, and what are the results?", "¿Por qué ocurre y qué consecuencias tiene?")],
  [t("Compare and contrast", "Comparación"), t("<em>in contrast, unlike, whereas, both, like, however</em>", "<em>en cambio, a diferencia de, mientras que, ambos, al igual que, sin embargo</em>"), t("How are they alike, and how are they different?", "¿En qué se parecen y en qué se diferencian?")]])}
{C.caja("tip", t("Central idea or detail?", "¿Idea central o detalle?"), "<p>" + t("If a statement covers only one paragraph, it is a detail. The central idea has to cover the whole text. A good check: does the statement leave out an important part of what you read? If it does, it is not the central idea.", "Si una afirmación solo cubre un párrafo del texto, es un detalle. La idea central tiene que abarcar el texto completo. Un buen control: ¿la afirmación deja fuera alguna parte importante de lo leído? Si la deja, no es la idea central.") + "</p>")}
{C.caja("tip", t("Read with a pencil: four marks", "Lea con lápiz: cuatro marcas"), "<p>" + t("Mark the text as you read: <strong>?</strong> next to a word you do not know, <strong>★</strong> next to the central idea, <strong>✓</strong> next to a supporting fact, and a <strong>circle</strong> around each order word. The first time, read slowly and out loud, as if you were explaining it to someone.", "Marque el texto mientras lee: <strong>?</strong> junto a un término desconocido, <strong>★</strong> junto a la idea central, <strong>✓</strong> junto a un dato de apoyo y un <strong>círculo</strong> alrededor de cada palabra de secuencia. La primera vez, lea despacio y en voz alta, como si le explicara el texto a otra persona.") + "</p>")}"""

    s5 = f"""<p>{t("A short science text written for this level. Read it using the four marks, then answer the questions.", "Texto científico breve adaptado al nivel. Léalo con las cuatro marcas y responda las preguntas.")}</p>
{C.lectura(t("How the body keeps its temperature", "Cómo mantiene el cuerpo su temperatura"),
 [t("The human body works well only within a narrow range of temperature, around 37 °C (98.6 °F). Keeping that value steady, even when the surroundings change, is called <strong>thermoregulation</strong>. It is one case of <strong>homeostasis</strong>, that is, keeping conditions inside the body constant.", "El cuerpo humano funciona correctamente dentro de un margen estrecho de temperatura, alrededor de los 37 °C. Mantener ese valor estable, a pesar de que el ambiente cambie, se denomina <strong>termorregulación</strong>, y es un caso particular de <strong>homeostasis</strong>, es decir, del mantenimiento de condiciones internas constantes."),
  t("When the outside temperature goes up, the blood vessels in the skin get wider, and more blood comes to the surface, so heat is lost to the air more easily. Also, the sweat glands release sweat: as the water evaporates, it takes heat from the body and cools it.", "Cuando la temperatura externa sube, los vasos sanguíneos de la piel se dilatan y llega más sangre a la superficie, de modo que el calor se pierde con mayor facilidad hacia el aire. Además, las glándulas sudoríparas liberan sudor: al evaporarse, el agua absorbe calor del cuerpo y lo enfría."),
  t("When the outside temperature goes down, the opposite happens. The blood vessels in the skin get narrower and lose less heat, while the muscles make fast, automatic contractions (shivering) that produce extra heat.", "Cuando la temperatura externa baja, ocurre lo contrario. Los vasos de la piel se estrechan y reducen la pérdida de calor, mientras que los músculos producen contracciones rápidas e involuntarias —los escalofríos— que generan calor adicional."),
  t("These responses have a limit. If the surroundings are extreme, or the effort lasts too long, the inside temperature moves out of the safe range, and heat stroke or hypothermia can happen. That is why thermoregulation is not a luxury for the body: the body needs it to work.", "Estos mecanismos tienen un límite. Si el ambiente es extremo o el esfuerzo demasiado prolongado, la temperatura interna se desplaza fuera del margen seguro y aparecen el golpe de calor o la hipotermia. Por eso la termorregulación no es un lujo del organismo, sino una condición para su funcionamiento.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"),
   t("What is the central idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Sweat evaporates and takes heat from the body.", "El sudor se evapora y absorbe calor del cuerpo."), t("Shivering is a set of automatic muscle contractions.", "Los escalofríos son contracciones musculares involuntarias."), t("The body has ways to keep its temperature steady, but they have a limit.", "El cuerpo dispone de mecanismos para mantener estable su temperatura, aunque tienen un límite.")], 2,
   {0: t("That is true, but it only covers part of paragraph 2. Does it cover the cold and the limits?", "Es cierto, pero solo cubre parte del párrafo 2. ¿Abarca el frío y los límites?"),
    1: t("That is a detail of paragraph 3. Look for the statement that covers all four paragraphs.", "Es un detalle del párrafo 3. Busque la afirmación que abarca los cuatro párrafos.")},
   t("Only the third statement covers the whole text: the mechanisms for heat and for cold, and their limit.", "Solo la tercera abarca el texto completo: los mecanismos para el calor y para el frío, y su límite."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"),
   t("Using the clues in the text, <strong>homeostasis</strong> means…", "Según las pistas del propio texto, <strong>homeostasis</strong> significa…"),
   [t("Keeping conditions inside the body constant", "El mantenimiento de condiciones internas constantes"), t("Losing heat by evaporation", "La pérdida de calor por evaporación"), t("The study of body temperature", "El estudio de la temperatura corporal")], 0,
   {1: t("That is how sweat works. Look right after the word “homeostasis.”", "Así funciona el sudor. Mire justo después de la palabra «homeostasis»."),
    2: t("“The study of” would need -logy. The text defines the word for you.", "«El estudio de» necesitaría -logía. El texto define la palabra.")},
   t("The text says it right after the word: “that is, keeping conditions inside the body constant.”", "El texto lo dice justo después: «es decir, del mantenimiento de condiciones internas constantes»."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"),
   t("What kind of context clue does the text give for <strong>homeostasis</strong>?", "¿Qué tipo de pista de contexto ofrece el texto para <strong>homeostasis</strong>?"),
   [t("An example", "Un ejemplo"), t("A definition, signaled by “that is”", "Una definición directa, introducida por «es decir»"), t("A contrast", "Un contraste")], 1,
   {0: t("An example would use “such as” or “for example.” Which signal word comes after “homeostasis”?", "Un ejemplo usaría «como» o «por ejemplo». ¿Qué señal aparece después de «homeostasis»?"),
    2: t("A contrast would use “in contrast” or “unlike.”", "Un contraste usaría «en cambio» o «a diferencia de».")},
   t("“That is” introduces a definition.", "«Es decir» introduce una definición directa."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"),
   t("Paragraphs 2 and 3 are organized mainly as…", "Los párrafos segundo y tercero están organizados sobre todo como…"),
   [t("A sequence of lab steps", "Una secuencia de pasos de laboratorio"), t("A list of definitions", "Una lista de definiciones"), t("A comparison of what happens in heat and what happens in cold", "Una comparación entre lo que ocurre con calor y lo que ocurre con frío")], 2,
   {0: t("There are no lab steps here. What do the two paragraphs put side by side?", "Aquí no hay pasos de laboratorio. ¿Qué ponen lado a lado los dos párrafos?"),
    1: t("They describe what the body does, not what words mean. Look at “the opposite happens.”", "Describen lo que hace el cuerpo, no qué significan palabras. Fíjese en «ocurre lo contrario».")},
   t("Paragraph 2 is about heat, paragraph 3 about cold, and “the opposite happens” joins them: it is a comparison.", "El párrafo 2 trata del calor, el 3 del frío, y «ocurre lo contrario» los une: es una comparación."))}
{P(t("Try it 4 · The onion procedure", "Pruebe 4 · El protocolo de la cebolla"),
   t("In the onion procedure, what happens if you put on the cover slip before adding the stain?", "En el protocolo de la cebolla, ¿qué ocurre si se cubre con el cubreobjetos antes de añadir el colorante?"),
   [t("Nothing: the order of these two steps does not matter", "Nada: el orden de esos dos pasos es indiferente"), t("The stain does not reach the cells, and you cannot see them", "El colorante no llega a las células y la muestra no se ve"), t("The sample dries out right away", "La muestra se seca de inmediato")], 1,
   {0: t("Switch them in your head: can the stain get under a cover slip that is already on?", "Inviértalos mentalmente: ¿puede el colorante entrar bajo un cubreobjetos ya puesto?"),
    2: t("Drying is not the problem. Think about where the stain has to go.", "Secarse no es el problema. Piense adónde tiene que llegar el colorante.")},
   t("The cover slip seals the sample, so the stain cannot reach the cells and they stay clear.", "El cubreobjetos sella la muestra: el colorante no llega a las células y estas quedan transparentes."))}
{P(t("Try it 5 · Which structure?", "Pruebe 5 · ¿Qué estructura?"),
   t("“More carbon dioxide <strong>causes</strong> the average temperature to rise; <strong>therefore</strong>, glaciers shrink.” The structure is…", "«El aumento de dióxido de carbono <strong>provoca</strong> una subida de la temperatura media, <strong>por lo tanto</strong> los glaciares retroceden». La estructura es…"),
   [t("Cause and effect", "Causa y efecto"), t("Compare and contrast", "Comparación"), t("Sequence", "Secuencia")], 0,
   {1: t("Nothing is being compared. Look at the bold words.", "No se compara nada. Fíjese en las palabras en negrita."),
    2: t("It is not a list of steps in time. What do “causes” and “therefore” signal?", "No es una lista de pasos en el tiempo. ¿Qué señalan «provoca» y «por lo tanto»?")},
   t("“Causes” and “therefore” are cause-and-effect signal words.", "«Provoca» y «por lo tanto» son señales de causa y efecto."))}
{P(t("Try it 6 · Which structure?", "Pruebe 6 · ¿Qué estructura?"),
   t("“Amphibians also breathe through their skin; reptiles, <strong>in contrast</strong>, use only their lungs.” The structure is…", "«Los anfibios respiran también por la piel; los reptiles, <strong>en cambio</strong>, dependen solo de sus pulmones». La estructura es…"),
   [t("Sequence", "Secuencia"), t("Cause and effect", "Causa y efecto"), t("Compare and contrast", "Comparación")], 2,
   {0: t("Nothing happens in order here.", "Aquí nada ocurre en orden."),
    1: t("Neither one causes the other. What does “in contrast” do?", "Ninguno causa al otro. ¿Qué hace «en cambio»?")},
   t("“In contrast” shows a difference between two groups: compare and contrast.", "«En cambio» marca una diferencia entre dos grupos: es una comparación."))}
{P(t("Try it 7 · Central idea or detail?", "Pruebe 7 · ¿Idea central o detalle?"),
   t("A text describes the color of sweat in an experiment in great detail. That information is…", "Un texto describe con detalle el color del sudor en un experimento. Esa información es…"),
   [t("The central idea of the text", "La idea central del texto"), t("A supporting detail", "Un detalle de apoyo"), t("The structure of the text", "La estructura del texto")], 1,
   {0: t("Could the color of sweat cover a whole text about an experiment? Probably not.", "¿Podría el color del sudor abarcar todo un texto sobre un experimento? Probablemente no."),
    2: t("The structure is how the text is organized, not one piece of information.", "La estructura es cómo se organiza el texto, no un dato.")},
   t("A precise, eye-catching fact is usually a supporting detail, not the central idea.", "Un dato preciso y llamativo suele ser un detalle de apoyo, no la idea central."))}"""

    G = lambda *a: C.ged_item(P, *a)
    intro_g = "<p>" + t("These questions work like the ones on the GED® Science test: first a short text, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK). Use the four marks while you read.",
                        "Estas preguntas funcionan como las del examen de Ciencias del GED®: primero un texto breve, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK). Use las cuatro marcas mientras lee.") + "</p>"
    sG = intro_g + f"""
{G(1, "SP.1.b", "2",
   t("<em>In a study of a new blood pressure medicine, the drop in pressure was statistically <strong>significant</strong>, meaning that it is very unlikely to be due to chance alone.</em><br>In this text, <strong>significant</strong> means…", "<em>En un estudio de un nuevo medicamento para la presión, el descenso de la presión fue estadísticamente <strong>significativo</strong>, es decir, es muy poco probable que se deba solo al azar.</em><br>En este texto, <strong>significativo</strong> quiere decir…"),
   [t("very large", "muy grande"), t("very important for patients", "muy importante para los pacientes"), t("unlikely to be due to chance", "poco probable que se deba al azar"), t("full of meaning", "lleno de significado")], 2,
   {0: t("In everyday language, yes. But the text gives its own meaning: look after “meaning that.”", "En el habla diaria, sí. Pero el texto da su propio significado: mire después de «es decir»."), 1: t("That is another everyday meaning. In science the word has a technical sense, and the text defines it.", "Ese es otro significado cotidiano. En ciencia la palabra tiene un sentido técnico, y el texto lo define."), 3: t("That is the meaning of the word in general. What does this text say it means?", "Ese es el significado general de la palabra. ¿Qué dice este texto que significa?")},
   t("The text defines it right away: “meaning that it is very unlikely to be due to chance alone.” A significant result can even be a small one.", "El texto lo define enseguida: «es decir, es muy poco probable que se deba solo al azar». Un resultado significativo puede ser incluso pequeño."))}
{G(2, "SP.1.b", "2",
   t("<em>The bacteria were grown on a <strong>medium</strong> of agar, a jelly made from seaweed that contains the nutrients they need.</em><br>In this text, <strong>medium</strong> means…", "<em>Las bacterias se cultivaron en un <strong>medio</strong> de agar, una gelatina hecha de algas que contiene los nutrientes que necesitan.</em><br>En este texto, <strong>medio</strong> quiere decir…"),
   [t("something of middle size", "la mitad de algo"), t("the material in which something grows", "el material en el que algo crece"), t("the average of a set of numbers", "el promedio de un conjunto de números"), t("a way of communicating, like TV", "un medio de comunicación, como la televisión")], 1,
   {0: t("Nothing in the sentence is about size. What do the bacteria need from the agar?", "Nada en la oración habla de mitades. ¿Qué necesitan las bacterias del agar?"), 2: t("That is a math meaning. Here the word is about growing bacteria.", "Ese es un significado matemático. Aquí la palabra trata del cultivo de bacterias."), 3: t("That meaning does not fit a jelly with nutrients.", "Ese significado no encaja con una gelatina con nutrientes.")},
   t("The context explains it: the agar is a jelly with the nutrients the bacteria need to grow. A word can have several meanings; the context chooses one.", "El contexto lo explica: el agar es una gelatina con los nutrientes que las bacterias necesitan para crecer. Una palabra puede tener varios significados; el contexto elige uno."))}
{G(3, "SP.3.a", "2",
   t("Go back to the reading “How the body keeps its temperature.” Which sentence <strong>best supports</strong> the idea that thermoregulation has limits?", "Vuelva a la lectura «Cómo mantiene el cuerpo su temperatura». ¿Qué oración <strong>apoya mejor</strong> la idea de que la termorregulación tiene límites?"),
   [t("“The human body works well only within a narrow range of temperature.”", "«El cuerpo humano funciona correctamente dentro de un margen estrecho de temperatura»."), t("“As the water evaporates, it takes heat from the body and cools it.”", "«Al evaporarse, el agua absorbe calor del cuerpo y lo enfría»."), t("“If the surroundings are extreme, or the effort lasts too long, the inside temperature moves out of the safe range.”", "«Si el ambiente es extremo o el esfuerzo demasiado prolongado, la temperatura interna se desplaza fuera del margen seguro»."), t("“The muscles make fast, automatic contractions that produce extra heat.”", "«Los músculos producen contracciones rápidas e involuntarias que generan calor adicional».")], 2,
   {0: t("That sentence says the body needs a narrow range, not that its responses can fail.", "Esa oración dice que el cuerpo necesita un margen estrecho, no que sus mecanismos puedan fallar."), 1: t("That explains how sweating works, not when it stops working.", "Eso explica cómo funciona el sudor, no cuándo deja de funcionar."), 3: t("That describes a response to cold. Look for when the responses are not enough.", "Eso describe una respuesta al frío. Busque cuándo los mecanismos no bastan.")},
   t("Only this sentence describes what happens when the responses are not enough: the temperature leaves the safe range (heat stroke, hypothermia).", "Solo esta oración describe qué ocurre cuando los mecanismos no bastan: la temperatura sale del margen seguro (golpe de calor, hipotermia)."))}
{G(4, "SP.2.d", "2–3",
   t("<em>Procedure for testing pond water: 1. Rinse the tube with pond water. 2. Fill the tube to the 10 mL line. 3. Add 5 drops of reagent and cap the tube. 4. Shake for 30 seconds. 5. Wait 5 minutes and compare the color with the chart. <strong>Note: if the water is cloudy, filter it through a coffee filter before step 2.</strong></em><br>A student’s sample is cloudy. What should the student do right after rinsing the tube?", "<em>Procedimiento para analizar agua de estanque: 1. Enjuagar el tubo con agua del estanque. 2. Llenar el tubo hasta la marca de 10 mL. 3. Añadir 5 gotas de reactivo y tapar el tubo. 4. Agitar durante 30 segundos. 5. Esperar 5 minutos y comparar el color con la tabla. <strong>Nota: si el agua está turbia, filtrarla con un filtro de café antes del paso 2.</strong></em><br>La muestra de un estudiante está turbia. ¿Qué debe hacer justo después de enjuagar el tubo?"),
   [t("Fill the tube to the 10 mL line", "Llenar el tubo hasta la marca de 10 mL"), t("Filter the water through a coffee filter", "Filtrar el agua con un filtro de café"), t("Add 5 drops of reagent", "Añadir 5 gotas de reactivo"), t("Compare the color with the chart", "Comparar el color con la tabla")], 1,
   {0: t("That is step 2 for clear water. Read the note at the end.", "Ese es el paso 2 para agua clara. Lea la nota del final."), 2: t("The reagent goes in after the tube is filled. Something comes before that for cloudy water.", "El reactivo va después de llenar el tubo. Con agua turbia, algo va antes."), 3: t("Comparing the color is the last step.", "Comparar el color es el último paso.")},
   t("The note is a special case: cloudy water must be filtered <em>before step 2</em>, so it goes between rinsing (step 1) and filling (step 2). Procedures on the test often hide an exception like this.", "La nota es un caso especial: el agua turbia se filtra <em>antes del paso 2</em>, es decir, entre enjuagar (paso 1) y llenar (paso 2). Los procedimientos del examen suelen esconder una excepción así."))}
{G(5, "SP.1.a", "2–3",
   t("<em>Coral reefs cover less than 1% of the ocean floor, but about a quarter of all ocean species live on or near them. Reefs also protect coasts by slowing down large waves. When the water gets too warm, corals push out the tiny algae that live inside them and give them food and color. The corals turn white, a change called bleaching, and many die if the water stays warm for weeks.</em><br>Which statement best summarizes the text?", "<em>Los arrecifes de coral cubren menos del 1 % del fondo del océano, pero cerca de una cuarta parte de todas las especies marinas vive en ellos o cerca de ellos. Los arrecifes también protegen las costas, porque frenan las olas grandes. Cuando el agua se calienta demasiado, los corales expulsan las diminutas algas que viven en su interior y les dan alimento y color. Los corales se vuelven blancos, un cambio llamado blanqueamiento, y muchos mueren si el agua sigue caliente durante semanas.</em><br>¿Qué afirmación resume mejor el texto?"),
   [t("Coral reefs cover less than 1% of the ocean floor.", "Los arrecifes de coral cubren menos del 1 % del fondo del océano."), t("Coral reefs are small but very valuable, and warm water can bleach and kill the corals.", "Los arrecifes de coral son pequeños pero muy valiosos, y el agua caliente puede blanquear y matar los corales."), t("Algae give corals their color.", "Las algas dan su color a los corales."), t("People should stop building on the coast.", "La gente debería dejar de construir en la costa.")], 1,
   {0: t("That is one number from the first sentence: a supporting detail.", "Ese es un dato de la primera oración: un detalle de apoyo."), 2: t("True, but it covers only part of the text. Does it say anything about why reefs matter?", "Es cierto, pero solo cubre una parte del texto. ¿Dice algo de por qué importan los arrecifes?"), 3: t("The text gives no advice. A summary says only what the text says.", "El texto no da consejos. Un resumen dice solo lo que dice el texto.")},
   t("A good summary covers the whole text: why reefs matter (many species, protection of coasts) and the danger of warm water (bleaching).", "Un buen resumen abarca todo el texto: por qué importan los arrecifes (muchas especies, protección de las costas) y el peligro del agua caliente (blanqueamiento)."))}"""

    secciones = [
        ("s1", t("Break the word apart: prefix, root, and suffix", "Descomponer el término: prefijo, raíz y sufijo"), s1),
        ("s2", t("When the root is not enough: context clues", "Cuando la raíz no basta: las pistas del contexto"), s2),
        ("s3", t("Multistep procedures", "Procedimientos de pasos múltiples"), s3),
        ("s4", t("Central idea and text structure", "Idea central y estructura del texto"), s4),
        ("s5", t("Science reading", "Lectura científica"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Break it apart before you look it up.", "Descomponer antes de consultar."), t("Find six science words you do not know in a text (a news story, medicine instructions, or a product label). Break each one into its roots and write a meaning <em>before</em> you look it up. Then compare and write down which piece gave you the key clue.", "Busque seis términos científicos desconocidos en un texto (una noticia, las indicaciones de un medicamento, la etiqueta de un producto). Descomponga cada uno en sus raíces y escriba un significado <em>antes</em> de consultar. Después compare y anote qué pieza le dio la pista decisiva.")),
        (t("Narrate a procedure.", "Narrar un procedimiento."), t("Put the steps of a procedure in order on the practice page. Then tell the procedure out loud, step by step, and write one sentence about what would go wrong if two of the steps were switched.", "Ordene los pasos de un protocolo en la página de práctica. Después cuente el procedimiento en voz alta, paso a paso, y escriba una oración sobre qué fallaría si se invirtieran dos de ellos.")),
        (t("Four marks.", "Cuatro marcas."), t("Take the texts of this lesson and use the four marks: ? for a word you do not know, ★ for the central idea, ✓ for a supporting fact, and a circle for each order word. Write the central idea of each text in one sentence, and name its structure with the words that gave it away.", "Tome los textos de esta lección y aplique las cuatro marcas: ? para un término desconocido, ★ para la idea central, ✓ para un dato de apoyo y un círculo para cada palabra de secuencia. Escriba la idea central de cada texto en una oración y nombre su estructura con las palabras que la delatan.")),
    ]
    quiz = [
        (t("If hydro- means water, then the <em>dehydration</em> of a living thing is…", "Sabiendo que hidro- significa agua, la <em>deshidratación</em> de un organismo consiste en…"),
         [t("Taking in too much water", "La entrada excesiva de agua"), t("The loss of water from the body", "La pérdida de agua del cuerpo"), t("The study of the water in the body", "El estudio del agua corporal"), t("Measuring the water you drink", "La medición del agua ingerida")], 1,
         {0: t("The prefix de- means “removing,” not “adding.”", "El prefijo des- significa «quitar», no «añadir»."), 2: t("“Study of” would be -logy.", "«Estudio» sería -logía."), 3: t("Measuring would be -meter.", "Medir sería -metro.")},
         t("De- (removing) + hydr- (water): losing water.", "Des- (quitar) + hidr- (agua): perder agua.")),
        (t("Using endo- and thermo-, an <em>endothermic</em> reaction is one that…", "Por el significado de endo- y termo-, una reacción <em>endotérmica</em> es la que…"),
         [t("Takes heat in", "Absorbe calor hacia adentro"), t("Gives off heat to the outside", "Libera calor hacia afuera"), t("Has no heat changes", "No implica cambios de calor"), t("Only happens in water", "Ocurre solo dentro del agua")], 0,
         {1: t("Outward would be exo-.", "Hacia afuera sería exo-."), 2: t("Thermo- tells you heat is involved.", "Termo- indica que interviene el calor."), 3: t("Water would be hydro-.", "El agua sería hidro-.")},
         t("Endo- (inward) + thermo- (heat): it takes heat in.", "Endo- (hacia adentro) + termo- (calor): absorbe calor.")),
        (t("“Arthropods, such as insects, crabs, and spiders, have an exoskeleton.” The context clue is…", "«Los artrópodos, como los insectos, los cangrejos y las arañas, tienen exoesqueleto». La pista de contexto es…"),
         [t("A contrast", "Un contraste"), t("A synonym", "Un sinónimo cercano"), t("An example", "Un ejemplo"), t("A definition", "Una definición directa")], 2,
         {0: t("Nothing is set against anything else.", "No se opone nada a nada."), 1: t("There is no “also called.”", "No hay «también llamado»."), 3: t("A definition would use “that is.” What signal word is there?", "Una definición usaría «es decir». ¿Qué señal aparece?")},
         t("“Such as” introduces examples (insects, crabs, spiders).", "«Como» introduce ejemplos (insectos, cangrejos, arañas).")),
        (t("“Autotrophs make their own food; heterotrophs, in contrast, must get it from outside.” According to the text, <em>heterotroph</em> means…", "«Las especies autótrofas fabrican su alimento; las heterótrofas, en cambio, deben obtenerlo». Según el texto, <em>heterótrofo</em> significa…"),
         [t("That it makes its own food", "Que fabrica su propio alimento"), t("That it lives in water", "Que vive dentro del agua"), t("That it studies feeding", "Que estudia la alimentación"), t("That it must get its food from outside", "Que debe obtener su alimento del exterior")], 3,
         {0: t("That is autotroph. “In contrast” means the opposite.", "Eso es autótrofo. «En cambio» indica lo contrario."), 1: t("Water is not mentioned.", "El agua no se menciona."), 2: t("Nothing in the sentence is about studying.", "Nada en la oración habla de estudiar.")},
         t("“In contrast” signals the opposite of “makes its own food”: it must get food from outside.", "«En cambio» señala lo contrario de «fabrica su alimento»: debe obtenerlo del exterior.")),
        (t("In the onion procedure, the stain must be added…", "En el protocolo de la cebolla, el colorante debe añadirse…"),
         [t("After putting on the cover slip", "Después de colocar el cubreobjetos"), t("Before putting on the cover slip", "Antes de colocar el cubreobjetos"), t("Only after you finish looking", "Solo al terminar la observación"), t("Only on the microscope lens", "Únicamente sobre el objetivo del microscopio")], 1,
         {0: t("The cover slip would seal the sample.", "El cubreobjetos sellaría la muestra."), 2: t("Then there would be nothing stained to look at.", "Entonces no habría nada teñido que observar."), 3: t("The stain goes on the sample, not on the lens.", "El colorante va sobre la muestra, no sobre el objetivo.")},
         t("Stain first, so it can soak into the cells; then cover.", "Primero se colorea, para que penetre en las células; después se cubre.")),
        (t("Why do you look first with the lowest-power lens?", "¿Por qué se observa primero con el objetivo de menor aumento?"),
         [t("Because it lets you find and focus the sample before you zoom in", "Porque permite localizar y enfocar la muestra antes de ampliarla"), t("Because the highest power damages the slide", "Porque el mayor aumento daña el portaobjetos"), t("Because the stain works faster that way", "Porque el colorante actúa más rápido así"), t("Because it keeps air bubbles from forming", "Porque evita que se formen burbujas de aire")], 0,
         {1: t("The lens does not damage the slide.", "El objetivo no daña el portaobjetos."), 2: t("The lens has nothing to do with the stain.", "El objetivo no tiene que ver con el colorante."), 3: t("Bubbles are avoided by tilting the cover slip.", "Las burbujas se evitan inclinando el cubreobjetos.")},
         t("The low power shows a wide area, so you can find the sample; the high power shows a tiny area.", "El menor aumento muestra un campo amplio para encontrar la muestra; el mayor, un campo diminuto.")),
        (t("Which of these words shows order in a procedure?", "¿Cuál de estas palabras señala el orden dentro de un procedimiento?"),
         [t("Due to", "Debido a"), t("In contrast", "En cambio"), t("Next", "A continuación"), t("For example", "Por ejemplo")], 2,
         {0: t("“Due to” signals a cause.", "«Debido a» señala una causa."), 1: t("“In contrast” signals a comparison.", "«En cambio» señala una comparación."), 3: t("“For example” introduces an example.", "«Por ejemplo» introduce un ejemplo.")},
         t("“Next” tells you what comes after: it is an order word.", "«A continuación» indica lo que viene después: es una palabra de secuencia.")),
        (t("A text explains the water cycle paragraph by paragraph: evaporation, condensation, precipitation, and soaking into the ground. Its structure is…", "Un texto explica el ciclo del agua párrafo a párrafo: evaporación, condensación, precipitación e infiltración. Su estructura es…"),
         [t("Compare and contrast", "Comparación"), t("Cause and effect", "Causa y efecto"), t("Problem and solution", "Problema y solución"), t("Sequence", "Secuencia")], 3,
         {0: t("Nothing is compared: each paragraph is the next stage.", "No se compara nada: cada párrafo es la etapa siguiente."), 1: t("Some stages lead to others, but the text is organized by order.", "Unas etapas llevan a otras, pero el texto se organiza por orden."), 2: t("No problem is presented.", "No se presenta ningún problema.")},
         t("Stages one after another, in order: sequence.", "Etapas una tras otra, en orden: secuencia.")),
        (t("“Cutting down trees reduces how much water the soil holds, and, as a result, floods increase.” The structure is…", "«La tala de árboles reduce la retención de agua en el suelo y, como resultado, aumentan las inundaciones». La estructura es…"),
         [t("Cause and effect", "Causa y efecto"), t("A sequence of steps", "Secuencia de pasos"), t("Compare and contrast", "Comparación"), t("Definition", "Definición")], 0,
         {1: t("It is not a set of steps to follow.", "No es un conjunto de pasos que seguir."), 2: t("Two things are not being compared.", "No se comparan dos cosas."), 3: t("No word is being defined.", "No se define ninguna palabra.")},
         t("“As a result” signals the effect of cutting down trees.", "«Como resultado» señala el efecto de la tala.")),
        (t("What is the best test to decide whether a statement is the central idea?", "¿Cuál es la mejor prueba para decidir si una afirmación es la idea central?"),
         [t("It is in the first sentence of the text", "Que aparezca en la primera oración del texto"), t("It covers the whole text, not just one paragraph", "Que abarque el texto completo y no solo un párrafo"), t("It has a number in it", "Que contenga un dato numérico"), t("It is the longest statement in the text", "Que sea la afirmación más larga del texto")], 1,
         {0: t("The central idea is not always at the start.", "La idea central no siempre está al principio."), 2: t("A number is usually a supporting detail.", "Un dato numérico suele ser un detalle de apoyo."), 3: t("Length does not decide it.", "La longitud no lo decide.")},
         t("The central idea must cover the whole text; if it leaves out an important part, it is a detail.", "La idea central tiene que abarcar todo el texto; si deja fuera una parte importante, es un detalle.")),
    ]
    filas = [
        (t("Work out a word from its root or context", "Deduce el significado por la raíz o el contexto"), t("I work it out and can say which piece or clue let me do it.", "Lo deduzco y digo qué pieza o qué señal me lo permitió."), t("I guess a meaning, but not from the root or the context.", "Propongo un significado, pero sin apoyarme en la raíz ni en el contexto."), t("I stop at the word and do not guess.", "Me detengo ante el término y no propongo significado.")),
        (t("Follow a procedure without skipping steps", "Sigue un procedimiento sin omitir pasos"), t("I follow every step in order and can say what would fail if the order changed.", "Ejecuto todos los pasos en orden y anticipo qué fallaría si se alterara."), t("I follow it with one step skipped or switched.", "Lo sigo con alguna omisión o inversión puntual."), t("I skip or switch several steps.", "Omito o invierto varios pasos.")),
        (t("Find the central idea, not a detail", "Identifica la idea central sin confundirla con un detalle"), t("I write it in my own sentence and point out the details that support it.", "La formulo con mis palabras y distingo los detalles que la sostienen."), t("I get close, but my central idea leaves out part of the text.", "Me acerco, pero mi idea central deja fuera parte del texto."), t("I pick an eye-catching detail.", "Señalo un detalle llamativo.")),
        (t("Recognize the structure of a text", "Reconoce la estructura del texto"), t("I name it, point to the signal words, and explain how it helps me understand.", "La nombro, cito las señales y explico cómo ayuda a entender."), t("I name it, but I cannot say why.", "La nombro, pero no sé en qué me baso."), t("I do not recognize the structure.", "No reconozco la estructura.")),
    ]
    cierre = "<p>" + t("This lesson closes Topic 1. You now have the three tools you will use in the whole course: the <strong>anatomy of an investigation</strong>, <strong>experimental design</strong> with its variables and sources of error, and <strong>reading science texts</strong> by roots, context, procedures, and structure. None of them belongs to one subject: you will use all three in biology, chemistry, physics, and Earth science.",
                         "Con esta lección se cierra el Tema 1. Quedan instaladas las tres herramientas del curso: la <strong>anatomía de una investigación</strong>, el <strong>diseño experimental</strong> con sus variables y fuentes de error, y la <strong>lectura de textos científicos</strong> por raíces, contexto, procedimientos y estructura. Ninguna pertenece a un contenido concreto: las tres se aplicarán a biología, química, física y ciencias de la Tierra por igual.") + "</p><p>" + \
             t("Topic 2 builds the other support the test needs: numbers. It opens with Lesson 2.1, where you will work with sizes that go from the width of an atom to the distance between stars.",
               "El Tema 2 construye el otro andamiaje que exige el examen: el numérico. Abre con la Lección 2.1, donde se trabajará con magnitudes que van del diámetro de un átomo a la distancia entre estrellas.") + "</p>"
    glosario = [
        (t("Prefix, root, suffix", "Prefijo, raíz, sufijo"), t("The pieces of a word: at the start, in the middle (the main meaning), and at the end.", "Las piezas de una palabra: al principio, en el centro (el significado principal) y al final.")),
        (t("Context clue", "Pista de contexto"), t("Words near an unknown word that help you work out its meaning: a definition, an example, a contrast, or a synonym.", "Palabras cercanas a un término desconocido que ayudan a deducir su significado: definición, ejemplo, contraste o sinónimo.")),
        (t("Procedure (protocol)", "Procedimiento (protocolo)"), t("A sequence of steps where each one prepares what the next one needs.", "Secuencia de pasos en la que cada uno prepara lo que el siguiente necesita.")),
        (t("Central idea", "Idea central"), t("What the whole text says.", "Lo que el texto sostiene en su conjunto.")),
        (t("Supporting detail", "Detalle de apoyo"), t("A fact, example, or number that backs up the central idea.", "Dato, ejemplo o cifra que sostiene la idea central.")),
        (t("Text structure", "Estructura del texto"), t("How the author organized the text: sequence, cause and effect, or compare and contrast.", "Cómo organizó el autor el texto: secuencia, causa y efecto o comparación.")),
    ]
    estd = C.estandares(["SP.1.a", "SP.1.b", "SP.2.d", "SP.3.a"], [], base=["SP.6.c"])
    conexion = "<p>" + t("Lessons 1.1 and 1.2 taught you to rebuild an investigation and to audit its design. Both need something we took for granted until now: <strong>understanding the text</strong>. This lesson closes Topic 1 with the skill that holds up the other two.",
                         "Las lecciones 1.1 y 1.2 enseñaron a reconstruir una investigación y a auditar su diseño. Ambas cosas exigen algo que hasta ahora se dio por supuesto: <strong>entender el texto</strong>. Esta lección cierra el Tema 1 con la destreza que sostiene a las otras dos.") + "</p><p>" + \
               t("Let’s say it clearly: the GED® Science test is, in large part, a reading test. Nobody has to know ahead of time what <em>thermoregulation</em> means. What the test checks is whether you can work it out with what the text puts in front of you.",
                 "Conviene decirlo con claridad: el examen de Ciencias del GED® es, en buena medida, un examen de lectura. Nadie tiene que saber de antemano qué significa <em>termorregulación</em>. Lo que sí se evalúa es si usted puede averiguarlo con lo que el propio texto le pone delante.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("The GED® Science test is, in large part, a reading test. Here you learn to read science.", "El examen de Ciencias del GED® es, en buena medida, un examen de lectura. Aquí se aprende a leer ciencia."),
        ["SP.1 · " + t("Reading science", "Comprender textos científicos"), "SP.2.d · " + t("Steps of an investigation", "Pasos de una investigación")],
        [t("<strong>Work out</strong> the meaning of a technical word by breaking it into its Greek and Latin roots.", "<strong>Determinar</strong> el significado de un término técnico descomponiéndolo en sus raíces griegas y latinas."),
         t("<strong>Work out</strong> the meaning of an unknown word from the clues around it.", "<strong>Deducir</strong> el significado de una palabra desconocida a partir de las pistas del contexto."),
         t("<strong>Follow</strong> a multistep procedure without skipping or switching any step.", "<strong>Seguir</strong> un procedimiento técnico de pasos múltiples sin omitir ni invertir ninguno."),
         t("<strong>Find</strong> the central idea of a science text without mixing it up with a supporting detail.", "<strong>Identificar</strong> la idea central de un texto científico sin confundirla con un detalle de apoyo."),
         t("<strong>Recognize</strong> how the author organized the text: sequence, cause and effect, or compare and contrast.", "<strong>Reconocer</strong> la estructura del texto: secuencia, causa y efecto, o comparación.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        (None, t("Next: Topic 2 · Quantitative reasoning in science (being written).", "Siguiente: Tema 2 · Razonamiento cuantitativo en ciencias (en preparación).")), glosario, P)


# ---------------------------------------------------------------- práctica
def protocolos():
    return [
        {"titulo": t("Procedure 1 · Onion skin under the microscope", "Protocolo 1 · Epidermis de cebolla al microscopio"),
         "intro": t("Preparing a sample of onion skin to see its cells under the microscope. Put the eight steps in order with the ▲ and ▼ buttons.", "Preparación de una muestra de epidermis de cebolla para observar sus células al microscopio. Ordene los ocho pasos con los botones ▲ y ▼."),
         "pasos": cebolla(), "inicio": [7, 2, 0, 4, 1, 6, 5, 3],
         "cons": {"4>2": t("You covered before staining. The cover slip seals the sample, so the stain no longer reaches the cells and they stay clear: under the microscope you cannot see the nucleus or the wall.", "Cubrió antes de colorear. El cubreobjetos sella la muestra, así que el colorante ya no llega a las células y quedan transparentes: al microscopio no se distingue el núcleo ni la pared."),
                  "7>6": t("You started with the highest-power lens. It shows a tiny area, so the sample is out of view and you have to go back to the low power to find it.", "Empezó por el objetivo de mayor aumento. Ese objetivo abarca un campo diminuto: la muestra queda fuera de vista y hay que volver al menor aumento para encontrarla."),
                  "2>1": t("You added the stain before placing the sample on the slide. The stain spills and the onion layer is not stained.", "Añadió el colorante antes de colocar la muestra en el portaobjetos. El colorante se derrama y la capa de cebolla queda sin teñir."),
                  "3>2": t("You waited for stain to soak in before adding any. The wait only makes sense after staining.", "Esperó a que penetrara un colorante que todavía no había añadido. La espera solo tiene sentido después de colorear."),
                  "5>4": t("You removed the extra stain before putting on the cover slip. Without the cover slip, the paper pulls the sample itself away.", "Retiró el exceso de colorante antes de poner el cubreobjetos. Sin él, el papel arrastra la propia muestra."),
                  "1>0": t("You placed on the slide a layer you had not yet peeled from the onion.", "Colocó sobre el portaobjetos una capa que aún no había separado de la cebolla.")},
         "general": t("This procedure has three steps that rule over all the others: place before staining, stain before covering, and focus with the low power before switching to the high power.", "Este protocolo tiene tres dependencias que mandan sobre todas las demás: colocar antes de colorear, colorear antes de cubrir y enfocar con el menor aumento antes de pasar al mayor.")},
        {"titulo": t("Procedure 2 · The density of an irregular solid", "Protocolo 2 · La densidad de un sólido irregular"),
         "intro": t("Finding the density of a small stone with the water displacement method. Put the seven steps in order.", "Determinación de la densidad de una piedra pequeña por el método de desplazamiento de agua. Ordene los siete pasos."),
         "pasos": [t("Set the scale to zero with the empty container on it.", "Poner la balanza a cero con el recipiente vacío encima."),
                   t("Measure the mass of the dry stone and write it down in grams.", "Medir la masa de la piedra seca y anotarla en gramos."),
                   t("Fill the graduated cylinder with water to a known mark and write down that volume.", "Llenar la probeta con agua hasta una marca conocida y anotar ese volumen."),
                   t("Put the stone into the cylinder carefully, without splashing.", "Introducir la piedra en la probeta con cuidado, sin salpicar."),
                   t("Write down the new volume the water shows with the stone inside.", "Anotar el nuevo volumen que marca el agua con la piedra dentro."),
                   t("Subtract the first volume from the final volume to get the volume of the stone.", "Restar el volumen inicial del volumen final para obtener el volumen de la piedra."),
                   t("Divide the mass by the volume to get the density.", "Dividir la masa entre el volumen para obtener la densidad.")],
         "inicio": [4, 0, 6, 2, 5, 3, 1], "libres": [[1, 2]],
         "cons": {"3>2": t("You put the stone in before writing down the first water volume. Without that number there is nothing to subtract, and you have to start over: it is the most common mistake in this lab.", "Metió la piedra antes de anotar el volumen inicial del agua. Sin ese dato no hay resta posible y hay que empezar de nuevo: es el error más frecuente de esta práctica."),
                  "1>0": t("You measured the mass without setting the scale to zero. The reading includes the container, so the density will come out too high.", "Midió la masa sin poner la balanza a cero. La lectura incluye el recipiente, así que la densidad saldrá mayor de la real."),
                  "5>4": t("You subtracted before writing down the final volume. There are not two numbers to subtract yet.", "Restó antes de anotar el volumen final. Todavía no hay dos números que restar."),
                  "6>5": t("You divided before finding the volume of the stone. The number you would use as volume would be the water’s, not the stone’s.", "Dividió antes de calcular el volumen desplazado. Usaría como volumen el del agua, no el de la piedra."),
                  "4>3": t("You wrote down the final volume before putting the stone in, so you wrote the same number twice and the stone’s volume would come out zero.", "Anotó el volumen final sin haber introducido la piedra: anotó dos veces el mismo número y el volumen de la piedra saldría cero.")},
         "general": t("Here the order is set by the data: each calculation needs numbers that exist only if they were written down before. One pair can go either way: measuring the mass and filling the cylinder, because neither one needs anything from the other.", "Aquí el orden lo impone una dependencia de datos: cada cálculo necesita números que solo existen si se anotaron antes. Un par sí es intercambiable: medir la masa y llenar la probeta, porque ninguno de los dos necesita nada del otro.")},
        {"titulo": t("Procedure 3 · Growing bacteria on a plate", "Protocolo 3 · Cultivo bacteriano en placa"),
         "intro": t("Spreading a sample on a plate with growing medium. Put the seven steps in order.", "Siembra de una muestra en una placa con medio de cultivo. Ordene los siete pasos."),
         "pasos": [t("Label the plate with the date and the sample number before touching anything else.", "Rotular la placa con la fecha y el número de muestra antes de tocar nada más."),
                   t("Sterilize the loop in the flame and let it cool for a few seconds.", "Esterilizar el asa de siembra a la llama y dejarla enfriar unos segundos."),
                   t("Pick up the sample with the cooled loop.", "Tomar la muestra con el asa ya fría."),
                   t("Spread the sample on the growing medium with gentle strokes.", "Extender la muestra sobre el medio de cultivo con trazos suaves."),
                   t("Close the plate and seal it around the edge.", "Cerrar la placa y sellarla por el borde."),
                   t("Keep the plate upside down at 37 °C for 24 hours.", "Incubar la placa boca abajo a 37 °C durante 24 horas."),
                   t("Count the colonies you can see and write down the result.", "Contar las colonias visibles y anotar el resultado.")],
         "inicio": [1, 5, 3, 0, 6, 2, 4],
         "cons": {"2>1": t("You picked up the sample with a loop that was not sterilized. Whatever grows could come from the loop and not from the sample, so the result means nothing.", "Tomó la muestra con el asa sin esterilizar. Lo que crezca puede venir del asa y no de la muestra, así que el resultado no significa nada."),
                  "1>0": t("You sterilized before labeling. It seems not to matter, but it does: labeling at the end means handling a plate that already has bacteria, and mixing up two plates ruins the whole test. Labeling first is a lab rule, not a preference.", "Esterilizó antes de rotular. Parece indiferente y no lo es: rotular al final obliga a manipular una placa ya sembrada, y basta con confundir dos placas para invalidar el ensayo. Rotular primero es una regla de laboratorio, no una preferencia."),
                  "5>4": t("You put the plate in the incubator without sealing it. Air gets in freely and contaminates the culture.", "Incubó la placa sin sellarla. El aire de la estufa entra libremente y contamina el cultivo."),
                  "6>5": t("You counted colonies before incubating. At zero hours there is nothing to count: colonies take a day to become visible.", "Contó las colonias antes de incubar. A las cero horas no hay nada que contar: las colonias tardan un día en verse."),
                  "3>2": t("You spread a loop that had not picked up the sample yet.", "Extendió sobre el medio un asa que aún no había tomado la muestra.")},
         "general": t("This procedure teaches something new: sometimes the order is set not by physics but by safety and record-keeping. Labeling first and sterilizing before touching the sample are that kind of step.", "Este protocolo enseña algo nuevo: hay pasos cuyo orden no lo impone la física sino la seguridad y la trazabilidad. Rotular primero y esterilizar antes de tocar la muestra son de ese tipo.")},
    ]


def frases():
    if C.L == "en":
        return [
            {"partes": ["The stain is added and, ", {"ops": ["once", "before", "even though"], "ok": 0}, " it has soaked in, the sample is covered with the cover slip."],
             "pista": "Does the stain have to finish soaking in before the next step?",
             "exp": "“Once” means the first step must be finished before you go on. “Before” would say the opposite: covering while the stain has not soaked in, which is exactly the mistake that ruins the sample."},
            {"partes": ["Write down the first water volume ", {"ops": ["after", "before", "while"], "ok": 1}, " putting the stone in the cylinder, and ", {"ops": ["then", "earlier", "on the contrary"], "ok": 0}, " write down the final volume."],
             "pista": "Which number is lost if the stone goes in first?",
             "exp": "The first blank sets the key step: the first volume must be written down before the stone goes in, or the number is lost. The second blank just links the next action, and “then” does that."},
            {"partes": ["The plate is labeled ", {"ops": ["first", "last", "at the same time"], "ok": 0}, ", and only ", {"ops": ["after that", "before that"], "ok": 0}, " is the sample spread."],
             "pista": "When should a plate be labeled: before or after it has bacteria on it?",
             "exp": "“Only after that” shows it is not a suggestion but a condition. In technical texts, “only” in front of an order word almost always marks a required step."},
            {"partes": ["Look with the lowest-power lens and, ", {"ops": ["finally", "beforehand", "at the same time"], "ok": 0}, ", switch to the highest power, adjusting only the fine focus."],
             "pista": "Which lens comes last?",
             "exp": "“Finally” closes the sequence. “Beforehand” would switch the order, and the sample would be lost from view."},
        ]
    return [
        {"partes": ["Se añade el colorante y, ", {"ops": ["una vez que", "antes de que", "aunque"], "ok": 0}, " haya penetrado, se cubre la muestra con el cubreobjetos."],
         "pista": "¿El colorante tiene que terminar de penetrar antes del paso siguiente?",
         "exp": "«Una vez que» marca que lo primero tiene que estar terminado para seguir. Con «antes de que» la frase diría lo contrario: cubrir mientras el colorante aún no ha penetrado, que es justo el error que arruina la preparación."},
        {"partes": ["Se anota el volumen inicial del agua ", {"ops": ["después de", "antes de", "mientras"], "ok": 1}, " introducir la piedra en la probeta, y ", {"ops": ["seguidamente", "previamente", "por el contrario"], "ok": 0}, " se anota el volumen final."],
         "pista": "¿Qué dato se pierde si la piedra entra primero?",
         "exp": "El primer hueco fija la dependencia crítica: el volumen inicial debe anotarse antes de meter la piedra, o el dato se pierde. El segundo solo encadena la acción siguiente, y para eso sirve «seguidamente»."},
        {"partes": ["La placa se rotula ", {"ops": ["en primer lugar", "por último", "al mismo tiempo"], "ok": 0}, ", y solo ", {"ops": ["después", "antes"], "ok": 0}, " se procede a la siembra."],
         "pista": "¿Cuándo se rotula una placa: antes o después de sembrarla?",
         "exp": "«Solo después» refuerza que no es una recomendación sino una condición. En los textos técnicos, «solo» delante de una palabra de secuencia casi siempre señala un paso obligatorio."},
        {"partes": ["Se observa con el objetivo de menor aumento y, ", {"ops": ["por último", "previamente", "simultáneamente"], "ok": 0}, ", se pasa al de mayor aumento ajustando solo el enfoque fino."],
         "pista": "¿Qué objetivo va al final?",
         "exp": "«Por último» cierra la secuencia. Si dijera «previamente», el orden quedaría invertido y la muestra se perdería de vista."},
    ]


def banco_dependencias():
    d = [
        (t("In the microscope procedure, why must the one-minute wait come after adding the stain, and not before?", "En el protocolo del microscopio, ¿por qué el paso de esperar un minuto tiene que ir después de añadir el colorante y no antes?"),
         [t("Because the stain takes a minute to prepare", "Porque el colorante tarda un minuto en prepararse"), t("Because waiting only makes sense if there is already stain to soak into the sample", "Porque la espera solo tiene sentido si ya hay colorante que penetre en la muestra"), t("Because the microscope needs to warm up", "Porque el microscopio necesita calentarse"), t("Because the lab safety rules say so", "Porque así lo indica la norma de seguridad del laboratorio")], 1,
         t("The clue is in the noun: the step talks about “the stain” soaking in, so it needs stain that was already added. When a step mentions the result of another, that other step comes first.", "La dependencia está en el sustantivo: el paso habla de que «el colorante» penetre, así que necesita un colorante ya añadido. Cuando un paso menciona el resultado de otro, ese otro va antes por fuerza.")),
        (t("In the density lab, what happens if you put the stone in before writing down the first water volume?", "En la medición de densidad, ¿qué ocurre si se introduce la piedra antes de anotar el volumen inicial del agua?"),
         [t("Nothing: the volume can be found anyway", "No ocurre nada: el volumen se puede calcular igual"), t("The stone gets wet and changes its mass", "La piedra se moja y falsea la masa"), t("The first volume is lost and the subtraction cannot be done", "Se pierde el dato del volumen inicial y la resta ya no puede hacerse"), t("Water spills and the cylinder must be dried", "El agua se derrama y hay que secar la probeta")], 2,
         t("The stone’s volume comes from subtracting the first volume from the final one. Without the first one there is no subtraction, and you must empty the cylinder and start over. It is a data dependency: the later step needs a number that only exists if someone wrote it down before.", "El volumen de la piedra se obtiene restando el inicial del final. Sin el inicial no hay resta posible, y hay que vaciar la probeta y empezar otra vez. Es una dependencia de datos: el paso posterior necesita un número que solo existe si alguien lo anotó antes.")),
        (t("In the bacteria procedure, why must you sterilize the loop before picking up the sample?", "En el cultivo bacteriano, ¿por qué hay que esterilizar el asa antes de tomar la muestra?"),
         [t("So the loop is hot and the sample sticks better", "Para que el asa esté caliente y la muestra se adhiera mejor"), t("Because a dirty loop would add other microbes, and what grows would not come from the sample", "Porque el asa sucia introduciría microorganismos ajenos y lo que creciera no vendría de la muestra"), t("Because the flame activates the growing medium", "Porque la llama activa el medio de cultivo"), t("So the loop does not rust", "Para que el asa no se oxide durante la siembra")], 1,
         t("If the loop adds its own microbes, the result says nothing about the sample. It is the same problem as an uncontrolled variable from Lesson 1.2, now in lab technique.", "Si el asa aporta sus propios microorganismos, el resultado no dice nada sobre la muestra: es el mismo problema de la variable no controlada de la Lección 1.2, aplicado a la técnica de laboratorio.")),
        (t("A procedure says: “Remove the extra stain with paper towel at the edge.” Which step must have been done before?", "Un procedimiento dice: «Retirar el exceso de colorante con papel absorbente por el borde». ¿Qué paso tiene que haberse hecho antes, obligatoriamente?"),
         [t("Switching to the highest-power lens", "Cambiar al objetivo de mayor aumento"), t("Covering the sample with the cover slip", "Cubrir la muestra con el cubreobjetos"), t("Setting the scale to zero", "Poner la balanza a cero"), t("Labeling the slide", "Rotular el portaobjetos")], 1,
         t("The paper soaks up stain at the edge of the cover slip, so the cover slip must already be on. Without it, the paper would pull the sample away. The clue is “at the edge”: there is an edge only once the sample is covered.", "El papel absorbe por el borde del cubreobjetos, así que el cubreobjetos tiene que estar puesto. Sin él, el papel arrastraría la muestra. La pista es «por el borde», que presupone un borde que solo existe una vez cubierta la preparación.")),
        (t("Two steps of a procedure are “measure the mass of the stone” and “fill the cylinder with water.” What can you say about their order?", "Dos pasos de un protocolo son «medir la masa de la piedra» y «llenar la probeta con agua». ¿Qué se puede afirmar sobre su orden?"),
         [t("The mass must always be measured first", "La masa tiene que medirse siempre primero"), t("The cylinder must always be filled first", "La probeta tiene que llenarse siempre primero"), t("They can go in either order: neither needs anything from the other", "Son intercambiables: ninguno necesita nada del otro"), t("They must be done at exactly the same time", "Deben hacerse exactamente a la vez")], 2,
         t("Neither step needs the other, so the order does not matter. Recognizing steps that can be switched is part of the skill: if you are unsure between two steps that do not depend on each other, the test question is about something else.", "No hay dependencia entre ellos, así que el orden da igual. Reconocer los pasos intercambiables también es parte de la destreza: si duda entre dos que no dependen uno del otro, la pregunta del examen va por otro lado.")),
    ]
    return [{"enun": q, "ops": o, "ok": k, "pista": t("Ask yourself what the later step needs. If a step uses the result of another, that other step comes first.", "Pregúntese qué necesita el paso posterior. Si un paso usa el resultado de otro, ese otro va antes."), "exp": e} for q, o, k, e in d]


def banco_raices():
    d = [
        (t("<strong>Biodegradable</strong> (bio- = life)", "<strong>Biodegradable</strong> (bio- = vida)"), [t("Can be broken down by living things", "Que los seres vivos pueden descomponer"), t("Made only of plastic", "Hecho solo de plástico"), t("That measures life", "Que mide la vida")], 0, t("Bio- (life): living things, like bacteria and fungi, can break it down.", "Bio- (vida): los seres vivos, como bacterias y hongos, pueden descomponerlo.")),
        (t("<strong>Thermostat</strong> (thermo- = heat; -stat = keeps still)", "<strong>Termostato</strong> (termo- = calor; -stato = que mantiene fijo)"), [t("A device that keeps the temperature steady", "Un aparato que mantiene fija la temperatura"), t("The study of heat", "El estudio del calor"), t("A reaction that gives off heat", "Una reacción que libera calor")], 0, t("Thermo- (heat) + -stat (keeps steady): it keeps the temperature steady.", "Termo- (calor) + -stato (mantiene fijo): mantiene estable la temperatura.")),
        (t("<strong>Exoskeleton</strong> (exo- = outside)", "<strong>Exoesqueleto</strong> (exo- = fuera)"), [t("A skeleton on the outside of the body", "Un esqueleto por fuera del cuerpo"), t("A skeleton inside the body", "Un esqueleto por dentro del cuerpo"), t("An animal with no skeleton", "Un animal sin esqueleto")], 0, t("Exo- (outside): the hard shell of insects and crabs.", "Exo- (fuera): el caparazón duro de insectos y cangrejos.")),
        (t("<strong>Endoskeleton</strong> (endo- = inside)", "<strong>Endoesqueleto</strong> (endo- = dentro)"), [t("A skeleton on the outside of the body", "Un esqueleto por fuera del cuerpo"), t("A skeleton inside the body", "Un esqueleto por dentro del cuerpo"), t("The study of bones", "El estudio de los huesos")], 1, t("Endo- (inside): like our own skeleton.", "Endo- (dentro): como nuestro propio esqueleto.")),
        (t("<strong>Hydroelectric</strong> (hydro- = water)", "<strong>Hidroeléctrica</strong> (hidro- = agua)"), [t("Electricity made from moving water", "Electricidad producida con agua en movimiento"), t("Electricity made from sunlight", "Electricidad producida con luz solar"), t("A device that measures electricity", "Un aparato que mide la electricidad")], 0, t("Hydro- (water) + electric: electricity from water, as in a dam.", "Hidro- (agua) + eléctrica: electricidad a partir del agua, como en una presa.")),
        (t("<strong>Ecology</strong> (eco- = home, environment; -logy = study of)", "<strong>Ecología</strong> (eco- = casa, entorno; -logía = estudio de)"), [t("The study of living things and their environment", "El estudio de los seres vivos y su entorno"), t("A machine that cleans the air", "Una máquina que limpia el aire"), t("The process of recycling", "El proceso de reciclar")], 0, t("Eco- (home, environment) + -logy (study of).", "Eco- (casa, entorno) + -logía (estudio de).")),
        (t("<strong>Photometer</strong> (photo- = light; -meter = measure)", "<strong>Fotómetro</strong> (foto- = luz; -metro = medida)"), [t("A device that measures light", "Un aparato que mide la luz"), t("A process that uses light", "Un proceso que usa la luz"), t("The study of light", "El estudio de la luz")], 0, t("Photo- (light) + -meter (measure): it measures light.", "Foto- (luz) + -metro (medida): mide la luz.")),
        (t("<strong>Hypothermia</strong> (hypo- = below; thermo- = heat)", "<strong>Hipotermia</strong> (hipo- = debajo; termo- = calor)"), [t("Body temperature below normal", "Temperatura del cuerpo por debajo de lo normal"), t("Body temperature above normal", "Temperatura del cuerpo por encima de lo normal"), t("A device that heats the body", "Un aparato que calienta el cuerpo")], 0, t("Hypo- (below) + thermo- (heat): a temperature that is too low.", "Hipo- (debajo) + termo- (calor): una temperatura demasiado baja.")),
        (t("<strong>Hyperthermia</strong> (hyper- = above, too much)", "<strong>Hipertermia</strong> (hiper- = encima, en exceso)"), [t("Body temperature below normal", "Temperatura del cuerpo por debajo de lo normal"), t("Body temperature above normal", "Temperatura del cuerpo por encima de lo normal"), t("The study of fever", "El estudio de la fiebre")], 1, t("Hyper- (too much) + thermo- (heat): a temperature that is too high.", "Hiper- (exceso) + termo- (calor): una temperatura demasiado alta.")),
        (t("<strong>Microorganism</strong> (micro- = very small)", "<strong>Microorganismo</strong> (micro- = muy pequeño)"), [t("A living thing too small to see without a microscope", "Un ser vivo demasiado pequeño para verse sin microscopio"), t("A very large animal", "Un animal muy grande"), t("A part of a plant", "Una parte de una planta")], 0, t("Micro- (very small) + organism (living thing).", "Micro- (muy pequeño) + organismo (ser vivo).")),
        (t("<strong>Geothermal</strong> (geo- = earth; thermo- = heat)", "<strong>Geotérmica</strong> (geo- = tierra; termo- = calor)"), [t("Heat that comes from inside the Earth", "Calor que procede del interior de la Tierra"), t("The study of rocks", "El estudio de las rocas"), t("Light that comes from the Sun", "Luz que procede del Sol")], 0, t("Geo- (earth) + thermo- (heat): heat from inside the Earth.", "Geo- (tierra) + termo- (calor): el calor del interior de la Tierra.")),
        (t("<strong>Osmosis</strong> (-sis = process)", "<strong>Ósmosis</strong> (-sis = proceso)"), [t("A process", "Un proceso"), t("A device", "Un aparato"), t("A science", "Una ciencia")], 0, t("The ending -sis tells you it is a process: in osmosis, water moves through a membrane.", "La terminación -sis indica que es un proceso: en la ósmosis, el agua pasa a través de una membrana.")),
    ]
    return [{"enun": t("Use the roots to work out the meaning:", "Use las raíces para deducir el significado:") + "<br>" + w, "ops": o, "ok": k,
             "pista": t("Translate each piece, then put them together.", "Traduzca cada pieza y después únalas."), "exp": e} for w, o, k, e in d]


def banco_estructura():
    S = [t("Sequence", "Secuencia"), t("Cause and effect", "Causa y efecto"), t("Compare and contrast", "Comparación")]
    P = {0: t("Sequence uses order words: first, then, next, finally.", "La secuencia usa palabras de orden: primero, después, a continuación, por último."),
         1: t("Cause and effect uses because, causes, therefore, as a result.", "La causa y efecto usa porque, provoca, por lo tanto, como resultado."),
         2: t("Compare and contrast uses in contrast, unlike, whereas, both, like.", "La comparación usa en cambio, a diferencia de, mientras que, ambos, al igual que.")}
    d = [
        (t("First, the water evaporates. Then the vapor cools and forms clouds. Finally, the water falls as rain.", "Primero, el agua se evapora. Después, el vapor se enfría y forma nubes. Por último, el agua cae como lluvia."), 0),
        (t("Because the soil had no plants to hold it, the heavy rain washed it into the river.", "Como el suelo no tenía plantas que lo sujetaran, la lluvia intensa lo arrastró hasta el río."), 1),
        (t("Plant cells have a cell wall; animal cells, in contrast, have only a membrane.", "Las células vegetales tienen pared celular; las animales, en cambio, solo tienen membrana."), 2),
        (t("Smoking damages the lungs; as a result, smokers get short of breath more easily.", "Fumar daña los pulmones; como resultado, los fumadores se quedan sin aire con más facilidad."), 1),
        (t("Both Earth and Mars have seasons, but a year on Mars is almost twice as long.", "Tanto la Tierra como Marte tienen estaciones, pero el año marciano dura casi el doble."), 2),
        (t("To make a cell slide, cut the sample, then stain it, and finally cover it.", "Para preparar una muestra, se corta, a continuación se tiñe y por último se cubre."), 0),
        (t("Whereas renewable energy comes back naturally, fossil fuels take millions of years to form.", "Mientras que la energía renovable se repone de forma natural, los combustibles fósiles tardan millones de años en formarse."), 2),
        (t("High fever causes the body to lose water; therefore, a person with fever needs to drink more.", "La fiebre alta provoca pérdida de agua; por lo tanto, una persona con fiebre necesita beber más."), 1),
    ]
    out = [{"enun": t("What is the structure of this passage?", "¿Qué estructura tiene este fragmento?") + "<br><strong>" + x + "</strong>", "ops": S, "ok": k, "enOrden": True,
            "pistas": {i: P[i] for i in range(3) if i != k}, "exp": f"<strong>{S[k]}.</strong> " + P[k]} for x, k in d]
    C_ = [t("Definition", "Definición directa"), t("Example", "Ejemplo"), t("Contrast", "Contraste"), t("Synonym", "Sinónimo cercano")]
    PC = {0: t("A definition uses “that is,” “in other words,” or “is defined as.”", "Una definición usa «es decir», «o sea» o «se define como»."),
          1: t("An example uses “such as,” “for example,” or “including.”", "Un ejemplo usa «como», «por ejemplo» o «entre ellos»."),
          2: t("A contrast uses “in contrast,” “unlike,” or “whereas.”", "Un contraste usa «en cambio», «a diferencia de» o «mientras que»."),
          3: t("A synonym uses “also called,” “known as,” or “or simply.”", "Un sinónimo usa «también llamado», «conocido como» u «o simplemente».")}
    d2 = [
        (t("<strong>Mitosis</strong>, that is, the division of one cell into two identical cells, lets the body grow.", "La <strong>mitosis</strong>, es decir, la división de una célula en dos células idénticas, permite crecer al cuerpo."), 0),
        (t("<strong>Invertebrates</strong>, such as worms, snails, and jellyfish, have no backbone.", "Los <strong>invertebrados</strong>, como los gusanos, los caracoles y las medusas, no tienen columna vertebral."), 1),
        (t("<strong>Herbivores</strong> eat only plants; carnivores, in contrast, eat other animals.", "Los <strong>herbívoros</strong> comen solo plantas; los carnívoros, en cambio, comen otros animales."), 2),
        (t("The <strong>epidermis</strong>, also called the outer layer of the skin, protects the body.", "La <strong>epidermis</strong>, también llamada capa externa de la piel, protege el cuerpo."), 3),
    ]
    out += [{"enun": t("What kind of context clue helps you with the word in bold?", "¿Qué tipo de pista de contexto ayuda con la palabra en negrita?") + "<br>" + x, "ops": C_, "ok": k, "enOrden": True,
             "pistas": {i: PC[i] for i in range(4) if i != k}, "exp": f"<strong>{C_[k]}.</strong> " + PC[k]} for x, k in d2]
    return out


def practica():
    A = {"en": ["order", "order-words", "depends", "roots", "structure"], "es": ["orden", "palabras-secuencia", "dependencias", "raices", "estructura"]}[C.L]
    mods = [
        (A[0], t("The mixed-up procedure", "El protocolo desordenado"),
         C.orden("m1", t("Use ▲ and ▼ to move each step. When you think the order is right, press <strong>Check the order</strong>. If something is wrong, you will see what would happen in the lab, and you get a second try. You can use the keyboard: Tab to move to a button, Enter to press it.", "Use ▲ y ▼ para mover cada paso. Cuando crea que el orden es correcto, pulse <strong>Comprobar el orden</strong>. Si algo no está bien, verá qué pasaría en el laboratorio y tendrá un segundo intento. Puede usar el teclado: Tab para ir a un botón y Enter para pulsarlo."))),
        (A[1], t("Words that mark the order", "Las palabras que marcan la secuencia"),
         C.huecos("m2", t("Choose the order word that makes each sentence correct.", "Elija la palabra de secuencia que hace correcta cada oración."))),
        (A[2], t("Which step depends on which?", "¿Qué paso depende de cuál?"),
         C.om("m3", t("A step depends on another when it needs something the other one makes. The clue is usually in a noun.", "Un paso depende de otro cuando necesita algo que el anterior produce. La pista suele estar en un sustantivo."))),
        (A[3], t("Break the word apart", "Descomponga el término"),
         C.om("m4", t("Each word comes with the meaning of its pieces. Put the pieces together.", "Cada término viene con el significado de sus piezas. Únalas."))),
        (A[4], t("Context clues and text structure", "Pistas de contexto y estructura del texto"),
         C.om("m5", t("Find the signal words: they tell you the kind of clue or the structure.", "Busque las palabras señal: indican el tipo de pista o la estructura."))),
    ]
    js = (C.js_datos("PROT", protocolos()) + C.js_datos("FRASES", frases()) + C.js_datos("DEP", banco_dependencias()) +
          C.js_datos("RAI", banco_raices()) + C.js_datos("EST", banco_estructura()) +
          'creaOrden("m1", PROT);\ncreaHuecos("m2", FRASES);\ncreaBanco("m3", DEP);\ncreaBanco("m4", RAI);\ncreaBanco("m5", EST);\n')
    return C.pagina_practica(N, titulo(), t("Five activities · the order of the exercises changes every time · two tries in each one", "Cinco actividades · el orden de los ejercicios cambia cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
