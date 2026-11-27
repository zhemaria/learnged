"""LearnGED · Ciencias · Lección 8.3 · Simulacro cronometrado y tipos de pregunta (EN/ES).
Fuente: clases_ciencias/leccion_8-3.html y los interactivos ciencias/entrenador_formatos y examen/ciencias.
La práctica ensaya los cinco formatos del examen (opción múltiple, arrastrar y soltar, menú desplegable, completar espacios
y punto en una imagen, este con un motor propio en la página). El simulacro de 40 preguntas lo construye build_sci_simulacro.py.
Uso: python3 tools/build_sci_8_3.py
"""
import os, sys, random
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "8-3"


def titulo():
    return t("Timed practice test and item types", "Simulacro cronometrado y tipos de pregunta")


def anc(en, es):
    return en if C.L == "en" else es


def sim():
    return t("practice-test.html", "simulacro.html")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Knowing how the test is built lets you plan your effort before you start.", "Saber cómo está construida la prueba permite repartir el esfuerzo antes de empezar.")}</p>
{C.tabla(t("Content areas of the Science test, with their approximate weight and the course topics that cover them", "Dominios de contenido del examen de Ciencias, con su peso aproximado y los temas del curso que los cubren"),
 [t("Content area", "Dominio"), t("Approximate weight", "Peso aproximado"), t("Course topics", "Temas del curso")],
 [[t("Life science", "Ciencias de la vida"), "40 %", t("Topics 3 and 4", "Temas 3 y 4")], [t("Physical science", "Ciencias físicas"), "40 %", t("Topics 5 and 6", "Temas 5 y 6")], [t("Earth and space science", "Ciencias de la Tierra y el espacio"), "20 %", t("Topic 7", "Tema 7")]])}
{C.tabla(t("Basic facts about the GED Science test", "Datos básicos del examen de Ciencias del GED"),
 [t("Feature", "Característica"), t("What to expect", "Qué esperar")],
 [[t("Time", "Tiempo"), t("90 minutes, in one part, with no break", "90 minutos, en una sola parte, sin descanso")],
  [t("Number of questions", "Número de preguntas"), t("It is not fixed; practice with about 40 so the pace feels familiar", "No es fijo; practique con unas 40 para acostumbrarse al ritmo")],
  [t("Question types", "Tipos de pregunta"), t("Multiple choice, drag and drop, drop-down, fill in the blank, and hot spot (select an area). There is no written answer.", "Opción múltiple, arrastrar y soltar, menú desplegable, completar espacios y punto en una imagen. No hay respuesta escrita.")],
  [t("Tools", "Herramientas"), t("On-screen TI-30XS calculator and a formula sheet", "Calculadora TI-30XS en pantalla y hoja de fórmulas")],
  [t("Passing score", "Puntuación para aprobar"), t("145, on a scale from 100 to 200", "145, en una escala de 100 a 200")]])}
<p>{t("The <strong>science practices SP.1 to SP.8</strong> are not a separate block: they run through all three areas. A biology item can test reading a graph, and a physics item can test judging a conclusion. That is why Topics 1, 2, and 8 have no area of their own: they teach what applies to all of them.", "Las <strong>prácticas científicas SP.1 a SP.8</strong> no forman un bloque aparte: atraviesan los tres dominios. Un ítem de biología puede evaluar la lectura de una gráfica, y uno de física, la evaluación de una conclusión. Por eso los temas 1, 2 y 8 no tienen dominio propio: enseñan lo que se aplica en todos.")}</p>
{C.caja("tip", t("About how deep the questions go", "Sobre la profundidad de las preguntas"), "<p>" + t("Most items do not ask you to recall a fact, but to <strong>apply it or reason with it</strong> from a passage you just read. So memorizing definitions pays off little, and rereading the passage or graph carefully pays off a lot. Almost always, the information you need is in front of you.", "La mayoría de los ítems no piden recordar un dato, sino <strong>aplicarlo o razonar con él</strong> a partir de un estímulo que se acaba de leer. Eso significa que memorizar definiciones rinde poco, y que releer con atención el texto o la gráfica del enunciado rinde mucho. Casi siempre, la información necesaria está delante.") + "</p>")}
<p><small>{t("Test facts from GED Testing Service (ged.com). Rules can change: check ged.com before you register.", "Datos del examen tomados de GED Testing Service (ged.com). Las reglas pueden cambiar: compruébelas en ged.com antes de inscribirse.")}</small></p>"""

    def formato(n, nombre, que, como):
        return f'<h3>{t("Format", "Formato")} {n} · {nombre}</h3>\n<p>{que}</p>\n' + C.caja("tip", t("How to handle it", "Cómo abordarlo"), f"<p>{como}</p>")
    s2 = f"""<p>{t("These are the five kinds of question that appear on the screen. None is hard in itself; what costs points is meeting them for the first time on test day.", "Estos son los cinco tipos de pregunta que aparecen en pantalla. Ninguno es difícil en sí mismo; lo que cuesta puntos es descubrirlos por primera vez el día del examen.")}</p>
{formato(1, t("Multiple choice", "Opción múltiple"), t("The classic question: a prompt and four options, and you pick one.", "La pregunta clásica: un enunciado y cuatro opciones, de las que se elige una."), t("Read all four options before you decide. Often two are clearly out and the real choice is between the other two, which differ in a detail. Be wary of absolute words like “always,” “never,” and “the best,” as Lesson 7.3 warned.", "Leer las cuatro opciones antes de decidir. Con frecuencia dos son claramente descartables y la elección real está entre las otras dos, que se diferencian en un matiz. Desconfíe de los superlativos («siempre», «nunca», «la mejor»), que ya se señalaron en la Lección 7.3."))}
{formato(2, t("Drag and drop", "Arrastrar y soltar"), t("You take items from one area and place them in boxes, on a diagram, or in an order. It is the format used to balance chemical equations or sort organisms into feeding levels.", "Se toman elementos de una zona y se colocan en casillas, en un diagrama o en un orden determinado. Es el formato con el que se equilibran ecuaciones químicas y se clasifican niveles tróficos."), t("Place the items you are sure of first and leave the doubtful ones for last, when fewer boxes are left. You can move an item again: nothing is final until you submit. Check that no box is left empty.", "Colocar primero los elementos de los que se está seguro y dejar los dudosos para el final, cuando queden menos casillas libres. Si un elemento no encaja, se puede volver a mover: nada queda fijado hasta enviar la respuesta. Compruebe que no queda ninguna casilla vacía."))}
{formato(3, t("Drop-down menu", "Menú desplegable"), t("A sentence has one or more blanks, each with its own list of options. When you choose, the sentence is complete.", "Dentro de una frase aparecen uno o varios huecos, cada uno con su lista de opciones. Al elegir, la frase queda completa."), t("Read the whole sentence again <strong>after</strong> you choose, to check that it makes complete sense. When a sentence has two menus, the first choice usually affects the second.", "Leer la frase entera <strong>después</strong> de elegir, para comprobar que tiene sentido completo. Cuando hay dos menús en la misma frase, la elección del primero suele condicionar la del segundo."))}
{formato(4, t("Fill in the blank", "Completar espacios"), t("You type the answer, with no options to choose from. It is usually a number or a word.", "Se escribe la respuesta con el teclado, sin opciones donde elegir. Suele ser un número o una palabra."), t("Type only what is asked. If the question asks for a number, type the number, with no unit or extra text, unless the question says otherwise. Watch the decimals: use the format the question uses.", "Escribir solo lo que se pide. Si la pregunta pide un número, se escribe el número, sin unidad ni texto adicional, salvo que el enunciado indique otra cosa. Atención a los decimales: se usa el formato que el enunciado emplee."))}
{formato(5, t("Hot spot (select an area)", "Punto en una imagen"), t("You click on a specific place on a picture, diagram, or graph: the point where kinetic energy is greatest, the right layer of a diagram, the part of a graph where something happens.", "Se hace clic sobre un lugar concreto de una imagen, un diagrama o una gráfica: el punto donde la energía cinética es máxima, la capa correspondiente de un esquema, la zona de una gráfica donde ocurre algo."), t("Find the answer in your head first, and only then click. You can change the point by clicking somewhere else before you submit.", "Localizar primero mentalmente la respuesta y solo entonces hacer clic. El punto marcado puede cambiarse haciendo clic en otro lugar antes de enviar."))}
{C.caja("ojo", t("What these formats have in common", "Lo que estos formatos tienen en común"), "<p>" + t("None of them tests computer skills: they test science. But a student who sees a drag-and-drop screen for the first time spends a minute figuring it out, and that minute comes out of thinking time. Practicing them first removes a source of mistakes that <strong>has nothing to do with what you know</strong>.", "Ninguno evalúa destreza informática: evalúan ciencia. Pero un estudiante que se encuentra por primera vez con una pantalla de arrastrar y soltar gasta un minuto entendiéndola, y ese minuto sale del tiempo de pensar. Practicarlos antes elimina una fuente de error <strong>que nada tiene que ver con lo que se sabe</strong>.") + "</p>")}
{C.enlace(N, anc("multiple-choice", "opcion-multiple"), t("the five item types", "los cinco formatos"), t("Try each format with science content before the practice test.", "Ensaye cada formato con contenido de ciencias antes del simulacro."))}"""

    s3 = f"""<p>{t("Ninety minutes for about forty questions gives you a little over <strong>two minutes per question</strong>. That average does not mean spending two minutes on each one: it means the easy ones must leave room for the hard ones.", "Noventa minutos para unas cuarenta preguntas dan algo más de <strong>dos minutos por pregunta</strong>. Ese promedio no significa dedicar dos minutos a cada una: significa que las fáciles deben dejar margen para las difíciles.")}</p>
{C.tabla(t("Time plan for the practice test in three blocks, with the goal and the warning sign of each", "Estrategia de administración del tiempo durante el simulacro, dividida en tres bloques con su objetivo y la señal de alarma correspondiente"),
 [t("When", "Momento"), t("What to do", "Qué hacer"), t("Warning sign", "Señal de alarma")],
 [[t("First third · minutes 1 to 30", "Primer tercio · minutos 1 a 30"), t("Move on without getting stuck. Answer what you know and mark the rest for review.", "Avanzar sin atascarse. Responder lo que se sabe y marcar para revisar lo que no."), t("If at minute 30 you have not reached question 13, you are going too slowly.", "Si al minuto 30 no se ha llegado a la pregunta 13, se está yendo demasiado despacio.")],
  [t("Second third · minutes 31 to 60", "Segundo tercio · minutos 31 a 60"), t("Keep the pace. Long passages often show up here: reading them once carefully is faster than reading them three times.", "Mantener el ritmo. Los estímulos largos aparecen a menudo aquí: leerlos una vez con atención es más rápido que releerlos tres veces."), t("If at minute 60 you have not reached question 27, speed up and mark more questions.", "Si al minuto 60 no se ha llegado a la pregunta 27, conviene acelerar y dejar marcadas más preguntas.")],
  [t("Last third · minutes 61 to 90", "Último tercio · minutos 61 a 90"), t("Finish every question and go back to the marked ones with the time left.", "Terminar todas las preguntas y volver a las marcadas con el tiempo que quede."), t("If 10 minutes are left and some questions are still unopened, answer them all, even without being sure.", "Si faltan diez minutos y quedan preguntas sin abrir, responderlas todas aunque sea sin certeza.")]])}
{C.caja("ojo", t("Never leave a question blank", "Nunca se deja una pregunta en blanco"), "<p>" + t("There is no penalty for a wrong answer, so a guess has some chance of being right and a blank has none. Before you submit, the last check is always the same: nothing left unanswered.", "No hay penalización por error, de modo que una respuesta al azar tiene alguna probabilidad de acierto y una casilla vacía tiene cero. Antes de enviar, la última comprobación es siempre la misma: que no quede nada sin responder.") + "</p>")}
{C.caja("tip", t("The question that eats the time of three others", "El ítem que consume el tiempo de otros tres"), "<p>" + t("Getting stuck for eight minutes on a hard question costs much more than the point it is worth: it also costs the three questions at the end that you never get to read. If after a long minute you cannot see the way, mark it and move on. Coming back later, with a clear head, usually works better than insisting.", "Atascarse ocho minutos en una pregunta difícil cuesta mucho más que el punto que vale: cuesta también las tres preguntas del final que quedan sin leer. Si tras un minuto largo no se ve el camino, se marca y se sigue. Volver después, con la cabeza despejada, suele funcionar mejor que insistir.") + "</p>")}
{P(t("Try it 1 · Five minutes left", "Pruebe 1 · Quedan cinco minutos"), t("Five minutes are left and three questions have no answer. The right move is to…", "Faltan cinco minutos y quedan tres preguntas sin responder. Lo correcto es…"),
   [t("leave them blank so you do not risk a wrong answer", "dejarlas en blanco para no arriesgarse a fallar"), t("answer all of them, because there is no penalty for a wrong answer", "responderlas todas, porque no hay penalización por error"), t("answer only the one that looks easiest", "responder solo la que parezca más fácil")], 1,
   {0: t("A blank is always zero.", "En blanco siempre es cero."), 2: t("Why give up the other two chances?", "¿Por qué renunciar a las otras dos oportunidades?")}, t("No penalty: answer everything.", "Sin penalización: responda todo."))}
{P(t("Try it 2 · A stubborn question", "Pruebe 2 · Una pregunta que se resiste"), t("A question still has you stuck after a long minute. You should…", "Una pregunta se resiste después de un minuto largo. Conviene…"),
   [t("mark it, move on, and come back at the end", "marcarla, seguir adelante y volver al final"), t("keep at it until you solve it, whatever it takes", "insistir hasta resolverla, cueste lo que cueste"), t("skip the whole block", "abandonar el bloque completo")], 0,
   {1: t("That costs the questions at the end.", "Eso cuesta las preguntas del final."), 2: t("The rest of the block may be easy.", "El resto del bloque puede ser fácil.")}, t("Mark and move on.", "Marcar y seguir."))}
{P(t("Try it 3 · Fill in the blank", "Pruebe 3 · Completar espacios"), t("A fill-in-the-blank item asks for an object’s density. The expected answer is…", "Un ítem de completar espacios pide la densidad de un objeto. La respuesta esperada es…"),
   [t("a short explanation of the steps", "una explicación breve del procedimiento"), t("only the number, in the format the question shows", "solo el número, en el formato que indique el enunciado"), t("the number with all the work", "el número acompañado de todo el desarrollo")], 1,
   {0: t("It only takes what is asked.", "Solo admite lo que se pide."), 2: t("There is no room for work.", "No hay sitio para el desarrollo.")}, t("Only what is asked.", "Solo lo que se pide."))}"""

    s4 = f"""<p>{t("Finishing the practice test is not the end of the work, but the start of the most useful part. The overall score says little; what guides your review is knowing <strong>which science practice your mistakes are concentrated in</strong>. Two students with the same score can need opposite reviews: one misreads graphs but knows the content; the other reasons well but is missing concepts. The report of the practice test separates those two situations.", "Terminar el simulacro no es el final del trabajo, sino el principio de la parte más útil. La calificación global dice poco; lo que orienta el repaso es saber <strong>en qué práctica científica se concentran los fallos</strong>. Dos estudiantes con la misma puntuación pueden necesitar repasos opuestos: uno falla al leer gráficas y domina el contenido; el otro razona bien y le faltan conceptos. El informe del simulacro separa esas dos situaciones.")}</p>
{C.tabla(t("How to read the performance report: error pattern, what it means, and what to review", "Guía de interpretación del informe de desempeño: patrón de error, qué indica y qué conviene repasar"),
 [t("If your mistakes are mostly in…", "Si los fallos se concentran en…"), t("What it means", "Lo que indica"), t("What to review", "Qué conviene repasar")],
 [[t("SP.1 and SP.6 · understanding and expressing science information", "SP.1 y SP.6 · comprender y expresar información científica"), t("The problem is reading the passage, not the content", "La dificultad está en la lectura del estímulo, no en el contenido"), t("The science readings of each topic and the vocabulary with roots", "Las lecturas científicas de cada tema y el vocabulario técnico con sus raíces")],
  [t("SP.3 and SP.8 · reasoning with data, statistics, and probability", "SP.3 y SP.8 · razonar con datos, estadística y probabilidad"), t("The obstacle is working with numbers", "El obstáculo es cuantitativo"), t("All of Topic 2 and the rearranging problems in Lessons 5.2, 6.1, and 6.2", "El Tema 2 completo y los despejes de las lecciones 5.2, 6.1 y 6.2")],
  [t("SP.4 and SP.5 · judging conclusions and auditing sources", "SP.4 y SP.5 · evaluar conclusiones y auditar fuentes"), t("You know the content, but deciding what the data support is hard", "El contenido se domina, pero cuesta decidir qué sostienen los datos"), t("Lessons 8.1 and 7.3", "Las lecciones 8.1 y 7.3")],
  [t("SP.2 and SP.7 · the scientific method and using formulas", "SP.2 y SP.7 · método científico y aplicación de fórmulas"), t("The procedure is not smooth yet", "Falta soltura en el procedimiento"), t("Topic 1 and the formula sheet, until using it is automatic", "El Tema 1 y la hoja de fórmulas, hasta que su uso sea automático")],
  [t("One specific content area", "Un dominio de contenido concreto"), t("It is a gap in content, not in skill", "Es una laguna de contenido, no de destreza"), t("The topics of that area and their quizzes", "Los temas de ese dominio y sus quizzes")]])}
{C.caja("tip", t("How to review a mistake", "Cómo se revisa un error"), "<p>" + t("Looking at the right answer is not enough. The question that pays off is: <strong>why did the one I chose look right?</strong> There is almost always a reason, and that reason is the real mistake to fix. A mistake you understand does not happen again; a mistake you only correct does.", "No basta con mirar cuál era la respuesta correcta. La pregunta que rinde es: <strong>¿por qué me pareció bien la que elegí?</strong> Casi siempre hay una razón, y esa razón es el error real que conviene corregir. Un fallo entendido no se repite; un fallo solo corregido, sí.") + "</p>")}"""

    s5 = f"""<p>{t("The assessment for this lesson <strong>is not a practice quiz</strong>: it is a complete practice test in conditions like those of the official test.", "La evaluación de esta lección <strong>no es un quiz de práctica</strong>: es el simulacro completo en condiciones equivalentes a las del examen oficial.")}</p>
{C.tabla(t("Practice test conditions: number of questions, time, attempts, allowed materials, and mix of content", "Condiciones del simulacro: número de preguntas, duración, intentos, material autorizado y distribución de contenidos"),
 [t("Condition", "Condición"), t("Details", "Especificación")],
 [[t("Questions", "Preguntas"), "40"], [t("Time", "Duración"), t("90 minutes, no break; it is submitted by itself when time runs out", "90 minutos, sin descanso; se envía solo al acabarse el tiempo")], [t("Attempts", "Intentos"), t("One per sitting; each new attempt draws different questions", "Uno por sesión; cada intento nuevo saca preguntas distintas")],
  [t("Allowed", "Material permitido"), t("The on-screen calculator and the formula sheet", "La calculadora en pantalla y la hoja de fórmulas")], [t("Content mix", "Distribución de dominios"), t("16 life · 16 physical · 8 Earth and space", "16 de vida · 16 de físicas · 8 de la Tierra y el espacio")],
  [t("Result", "Resultado"), t("A report by content area and by science practice, with the lessons to review", "Un informe por dominio y por práctica científica, con las lecciones que conviene repasar")]])}
{C.caja("ojo", t("Do it in real conditions", "Hágalo en condiciones reales"), "<p>" + t("Ninety minutes in a row, with no break, no notes, and no interruptions. Choose a quiet time and place, and let people at home know not to interrupt you. A practice test with pauses does not measure what it needs to measure, which includes stamina and managing your time.", "Noventa minutos seguidos, sin descanso, sin consultas y sin interrupciones. Elija un momento y un lugar tranquilos, y avise en casa de que no lo interrumpan. Un simulacro con pausas no mide lo que hay que medir, que es también la resistencia y la administración del tiempo.") + "</p>")}
<p class="boton-centro"><a class="btn" href="{sim()}">{t("Open the timed practice test", "Abrir el simulacro cronometrado")}</a></p>
<p>{t("Before you register for the official test, also take <strong>GED Ready®</strong>, the official practice test from GED Testing Service, which tells you whether you are likely to pass.", "Antes de inscribirse en el examen oficial, conviene presentar también el <strong>GED Ready®</strong>, la prueba de práctica oficial de GED Testing Service, que indica si se está preparado para aprobar.")}</p>"""

    secciones = [
        ("s1", t("How the test is built", "La estructura del examen"), s1),
        ("s2", t("The five item types", "Los cinco formatos de pregunta"), s2),
        ("s3", t("Managing your time", "Administrar el tiempo"), s3),
        ("s4", t("After the practice test: reading your own mistakes", "Después del simulacro: leer los propios errores"), s4),
        ("s5", t("The final practice test", "El simulacro final"), s5),
    ]
    tarea = [
        (t("The five formats.", "Los cinco formatos."), t("Do every activity on the practice page until each format feels familiar.", "Haga todas las actividades de la página de práctica hasta que cada formato le resulte familiar.")),
        (t("The practice test.", "El simulacro."), t(f'Take the <a href="{sim()}">timed practice test</a> in real conditions, and print or save the report.', f'Presente el <a href="{sim()}">simulacro cronometrado</a> en condiciones reales e imprima o guarde el informe.')),
        (t("Your review plan.", "Su plan de repaso."), t("With the report in hand, write down your two weakest practices and the lessons you will review, and for three of your mistakes write why the wrong answer looked right.", "Con el informe en la mano, anote sus dos prácticas más débiles y las lecciones que repasará, y escriba en tres de sus errores por qué le pareció bien la respuesta equivocada.")),
    ]
    Q = t
    quiz = [
        (Q("How long is the GED Science test?", "¿Cuánto dura el examen de Ciencias del GED?"), [Q("90 minutes, no break", "90 minutos, sin descanso"), Q("60 minutes with a break", "60 minutos con descanso"), Q("2 hours", "2 horas"), Q("There is no time limit", "No tiene límite de tiempo")], 0, {}, Q("90 minutes in one part.", "90 minutos en una sola parte.")),
        (Q("Which content areas weigh the most on the test?", "¿Qué dominios pesan más en el examen?"), [Q("Earth and space science", "Ciencias de la Tierra y el espacio"), Q("Life science and physical science, about 40 % each", "Ciencias de la vida y ciencias físicas, cerca del 40 % cada una"), Q("They all weigh the same", "Todos pesan igual"), Q("Only the science practices", "Solo las prácticas científicas")], 1, {}, Q("40 · 40 · 20.", "40 · 40 · 20.")),
        (Q("With 10 minutes left, three questions are still unopened. You should…", "Faltan 10 minutos y quedan tres preguntas sin abrir. Conviene…"), [Q("leave them blank", "dejarlas en blanco"), Q("answer only one carefully", "responder solo una con calma"), Q("answer all of them, even without being sure", "responderlas todas aunque sea sin certeza"), Q("start the test over", "empezar el examen de nuevo")], 2, {}, Q("No penalty for guessing.", "No hay penalización por error.")),
        (Q("In a drag-and-drop item, the best strategy is to…", "En un ítem de arrastrar y soltar, la estrategia más eficaz es…"), [Q("place items in the order they appear", "colocar los elementos en el orden en que aparecen"), Q("start with the ones you doubt most", "empezar por los que generan más duda"), Q("check only the first box", "revisar solo la primera casilla"), Q("place the ones you are sure of first and leave the doubtful ones for last", "colocar primero los seguros y dejar los dudosos para el final")], 3, {}, Q("Sure ones first.", "Primero los seguros.")),
        (Q("In a drop-down item with two menus in one sentence, you should…", "En un ítem de menú desplegable con dos menús en una frase, conviene…"), [Q("reread the whole sentence after choosing, because the first choice often affects the second", "releer la frase entera después de elegir, porque la primera elección suele condicionar la segunda"), Q("choose each menu without reading the rest", "elegir cada menú sin leer el resto"), Q("always choose the first option", "elegir siempre la primera opción"), Q("leave the second menu empty", "dejar vacío el segundo menú")], 0, {}, Q("Read the full sentence.", "Leer la frase completa.")),
        (Q("A fill-in-the-blank item asks for a speed in m/s. You type…", "Un ítem de completar espacios pide una velocidad en m/s. Se escribe…"), [Q("“The speed is 12 m/s because…”", "«La velocidad es 12 m/s porque…»"), Q("only the number: 12", "solo el número: 12"), Q("12 m/s plus the work", "12 m/s más el desarrollo"), Q("nothing, if unsure", "nada, si no se está seguro")], 1, {}, Q("Only what is asked.", "Solo lo que se pide.")),
        (Q("In a hot-spot item, you…", "En un ítem de punto en una imagen…"), [Q("type a word", "se escribe una palabra"), Q("drag a label", "se arrastra una etiqueta"), Q("click on the right place in a picture, diagram, or graph", "se hace clic en el lugar correcto de una imagen, un diagrama o una gráfica"), Q("choose from a list", "se elige en una lista")], 2, {}, Q("Click the place.", "Clic en el lugar.")),
        (Q("At minute 30 you are on question 8 of about 40. That means…", "En el minuto 30 va por la pregunta 8 de unas 40. Eso significa que…"), [Q("you are on a good pace", "va a buen ritmo"), Q("you should slow down", "debe ir más despacio"), Q("nothing: pace does not matter", "nada: el ritmo no importa"), Q("you are going too slowly: speed up and mark the hard ones", "va demasiado despacio: acelere y marque las difíciles")], 3, {}, Q("Aim for question 13 by minute 30.", "Conviene ir por la 13 en el minuto 30.")),
        (Q("Two students got the same score. Their review plans…", "Dos estudiantes sacaron la misma puntuación. Sus planes de repaso…"), [Q("can be opposite, depending on which practices they missed", "pueden ser opuestos, según en qué prácticas fallaron"), Q("must be the same", "deben ser iguales"), Q("do not matter", "no importan"), Q("depend only on the total", "dependen solo del total")], 0, {}, Q("Read the report by practice.", "Leer el informe por práctica.")),
        (Q("Most of your mistakes are in SP.3 and SP.8. You should review…", "La mayoría de sus fallos están en SP.3 y SP.8. Conviene repasar…"), [Q("the vocabulary with roots", "el vocabulario con raíces"), Q("Topic 2 and the rearranging problems", "el Tema 2 y los despejes"), Q("only Lesson 8.1", "solo la Lección 8.1"), Q("nothing: those do not count", "nada: esas no cuentan")], 1, {}, Q("Numbers and data.", "Números y datos.")),
        (Q("The most useful question when reviewing a mistake is…", "La pregunta más útil al revisar un error es…"), [Q("“What was the right answer?”", "«¿Cuál era la respuesta correcta?»"), Q("“How many did I get wrong?”", "«¿Cuántas fallé?»"), Q("“Why did the answer I chose look right?”", "«¿Por qué me pareció bien la que elegí?»"), Q("“Was the question unfair?”", "«¿Era injusta la pregunta?»")], 2, {}, Q("Find the reason behind the mistake.", "Encontrar la razón del error.")),
        (Q("Before registering for the official test, it is a good idea to take…", "Antes de inscribirse en el examen oficial, conviene presentar…"), [Q("nothing else", "nada más"), Q("another course", "otro curso"), Q("the same practice test ten times", "el mismo simulacro diez veces"), Q("GED Ready®, the official practice test", "el GED Ready®, la prueba de práctica oficial")], 3, {}, Q("GED Ready®.", "GED Ready®.")),
    ]
    quiz = [(a, b, k, {i: t("Look again at the section of the lesson this question comes from.", "Vuelva a mirar la sección de la lección de la que sale esta pregunta.") for i in range(len(b)) if i != k}, e) for a, b, k, _, e in quiz]
    filas = [
        (t("Handle the five item types", "Maneja los cinco formatos de pregunta"), t("I answer each format without stopping to figure out the screen.", "Respondo cada formato sin detenerme a entender la pantalla."), t("I know some formats but hesitate with others.", "Conozco algunos formatos, pero dudo con otros."), t("I have not tried the formats yet.", "Todavía no he ensayado los formatos.")),
        (t("Manage my time", "Administra el tiempo"), t("I finish all the questions and come back to the marked ones.", "Termino todas las preguntas y vuelvo a las marcadas."), t("I finish, but rushing at the end.", "Termino, pero con prisas al final."), t("I run out of time with questions unopened.", "Se me acaba el tiempo con preguntas sin abrir.")),
        (t("Read my report", "Lee su informe"), t("I name my two weakest practices and the lessons to review.", "Identifico mis dos prácticas más débiles y las lecciones que repasaré."), t("I look at my score but not at the practices.", "Miro la puntuación, pero no las prácticas."), t("I do not look at the report.", "No miro el informe.")),
        (t("Learn from each mistake", "Aprende de cada error"), t("I explain why the wrong answer looked right.", "Explico por qué me pareció bien la respuesta equivocada."), t("I look up the right answer only.", "Solo busco la respuesta correcta."), t("I move on without reviewing.", "Sigo sin revisar.")),
    ]
    cierre = "<p>" + t("This is the end of the LearnGED Science course: twenty-four lessons, from the first hypothesis in Topic 1 to this practice test.", "Aquí termina el curso de Ciencias de LearnGED: veinticuatro lecciones, desde la primera hipótesis del Tema 1 hasta este simulacro.") + "</p><p>" + \
             t("It is worth looking back once. The course did not teach three separate sciences: it taught a few mechanisms that came back again and again. <strong>Convection</strong> boiled water, moved Earth’s mantle, and spreads the planet’s heat. <strong>Density</strong> explained what floats, which plate sinks, and why warm air rises. <strong>Conservation</strong> ruled the atoms of a chemical equation and the energy of a roller coaster. And evidence was always judged by the same rule, for evolution, for Wegener, and for the Big Bang: <strong>several independent lines that agree weigh more than one</strong>.", "Conviene mirar atrás una vez. El curso no enseñó tres ciencias separadas: enseñó unos pocos mecanismos que reaparecieron una y otra vez. La <strong>convección</strong> hervía agua, movía el manto terrestre y reparte hoy el calor del planeta. La <strong>densidad</strong> explicaba qué flota, qué placa se hunde y por qué el aire caliente sube. La <strong>conservación</strong> gobernaba los átomos de una ecuación química y la energía de una montaña rusa. Y la evidencia se evaluó siempre con el mismo criterio, en la evolución, en Wegener y en el Big Bang: <strong>varias líneas independientes que coinciden pesan más que una sola</strong>.") + "</p><p>" + \
             t("What matters most is left, and it is a habit more than a piece of content: <strong>asking what the data support and what they do not</strong>. It helps on the test, which is what comes first, and it keeps helping long after. Good luck on the test.", "Queda lo más importante, y es un hábito más que un contenido: <strong>preguntar qué sostienen los datos y qué no</strong>. Sirve para el examen, que es lo inmediato, y sigue sirviendo mucho después. Suerte en la prueba.") + "</p>"
    glosario = [
        (t("Item type", "Formato de pregunta"), t("The way a question is answered on screen: multiple choice, drag and drop, drop-down, fill in the blank, or hot spot.", "Manera de responder en pantalla: opción múltiple, arrastrar y soltar, menú desplegable, completar espacios o punto en una imagen.")),
        (t("Hot spot", "Punto en una imagen"), t("An item answered by clicking a place on a picture or graph.", "Pregunta que se responde haciendo clic en un lugar de una imagen o gráfica.")),
        (t("Pace", "Ritmo"), t("How fast you move through the test; check it at minutes 30 and 60.", "Velocidad con que se avanza en la prueba; se comprueba en los minutos 30 y 60.")),
        (t("Mark for review", "Marcar para revisar"), t("Flag a question to come back to it if time allows.", "Señalar una pregunta para volver a ella si queda tiempo.")),
        (t("Performance report", "Informe de desempeño"), t("Your results by content area and by science practice, with what to review.", "Resultados por dominio y por práctica científica, con lo que conviene repasar.")),
        (t("GED Ready®", "GED Ready®"), t("The official practice test from GED Testing Service.", "Prueba de práctica oficial de GED Testing Service.")),
    ]
    estd = C.estandares(["SP.1.a", "SP.3.b", "SP.4.a", "SP.7.a"], ["L.a", "P.a", "ES.b"], base=["SP.6.c"])
    conexion = "<p>" + t("<strong>The last lesson, and it does not teach science.</strong> All the content is done and the project is finished. What is left is what separates a student who knows from one who also <strong>performs</strong>: knowing the screen, sharing out the time, and knowing where you yourself tend to slip.", "<strong>Última lección, y no enseña ciencia.</strong> Todo el contenido está visto y el proyecto está terminado. Lo que queda es lo que separa a un estudiante que sabe de uno que además <strong>rinde</strong>: conocer la interfaz, repartir el tiempo y saber dónde falla uno mismo.") + "</p><p>" + \
               t("Here is why it matters. Points are lost on the test for three different reasons: not knowing the content, not knowing how to reason with data, and <strong>not knowing how to handle the screen or the clock</strong>. The first two were worked on for twenty-three lessons. The third is solved here, and it is the easiest to get rid of.", "Conviene decir por qué esto importa. En el examen se pierden puntos por tres motivos distintos: no saber el contenido, no saber razonar con los datos y <strong>no saber manejar la pantalla o el reloj</strong>. Los dos primeros se trabajaron durante veintitrés lecciones. El tercero se resuelve aquí, y es el más fácil de eliminar.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Know the screen, share out the clock, and read your own mistakes: the last step before the test.", "Conocer la pantalla, repartir el reloj y leer los propios errores: el último paso antes del examen."),
        [t("Final assessment", "Evaluación final"), "SP.1 – SP.8 · " + t("Performance report", "Informe de desempeño")],
        [t("<strong>Handle</strong> the five item types of the test with ease.", "<strong>Manejar</strong> con soltura los cinco formatos de pregunta del examen."),
         t("<strong>Manage</strong> your time in blocks during a timed test.", "<strong>Administrar</strong> el tiempo por bloques durante una prueba cronometrada."),
         t("<strong>Complete</strong> a full 90-minute practice test in conditions like the real test.", "<strong>Resolver</strong> un simulacro completo de noventa minutos en condiciones equivalentes a las del examen."),
         t("<strong>Analyze</strong> your own mistakes by science practice to find your personal pattern.", "<strong>Analizar</strong> los errores propios clasificados por práctica científica para identificar el patrón personal de dificultad.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        (None, t('<strong>End of the Science course.</strong> <a href="index.html">Back to the course plan</a>.', '<strong>Fin del curso de Ciencias.</strong> <a href="index.html">Volver al plan del curso</a>.')), glosario, P, calculadora=True)


# ---------------------------------------------------------------- práctica: los cinco formatos
def banco_om():
    d = [(t("Which absolute word in an answer choice should make you suspicious?", "¿Qué palabra absoluta en una opción debería hacerle desconfiar?"), [t("“always”", "«siempre»"), t("“according to the table”", "«según la tabla»"), t("“in this study”", "«en este estudio»"), t("“on average”", "«en promedio»")], 0, t("Absolute words are usually wrong.", "Las palabras absolutas suelen ser incorrectas.")),
         (t("A box of 10 kg has a net force of 30 N. Its acceleration is…", "Una caja de 10 kg recibe una fuerza neta de 30 N. Su aceleración es…"), ["3 m/s²", "300 m/s²", "0.3 m/s²", "40 m/s²"], 0, t("a = F ÷ m = 30 ÷ 10.", "a = F ÷ m = 30 ÷ 10.")),
         (t("Which organism is a producer?", "¿Qué organismo es un productor?"), [t("Grass", "La hierba"), t("A rabbit", "Un conejo"), t("A hawk", "Un halcón"), t("A mushroom", "Un hongo")], 0, t("Producers make their own food by photosynthesis.", "Los productores fabrican su alimento por fotosíntesis.")),
         (t("Rock that formed from cooled lava is…", "La roca formada por lava enfriada es…"), [t("igneous", "ígnea"), t("sedimentary", "sedimentaria"), t("metamorphic", "metamórfica"), t("fossil", "fósil")], 0, t("Ignis = fire.", "Ignis = fuego.")),
         (t("Five minutes are left and you have two questions unanswered. You should…", "Quedan cinco minutos y tiene dos preguntas sin responder. Conviene…"), [t("answer both", "responder las dos"), t("leave them blank", "dejarlas en blanco"), t("go back to question 1", "volver a la pregunta 1"), t("answer only one", "responder solo una")], 0, t("No penalty for guessing.", "No hay penalización por error."))]
    return [{"enun": f"<p>{q}</p>", "ops": o, "ok": k, "pista": t("Read all four options and rule out two first.", "Lea las cuatro opciones y descarte primero dos."), "exp": e} for q, o, k, e in d]


def clasif_troficos():
    G = [t("Producer", "Productor"), t("Primary consumer", "Consumidor primario"), t("Secondary consumer", "Consumidor secundario")]
    PI = [t("Does it make its own food from sunlight?", "¿Fabrica su alimento con la luz del sol?"), t("Does it eat plants?", "¿Come plantas?"), t("Does it eat animals that eat plants?", "¿Come animales que comen plantas?")]
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("On the test you would drag each organism into its box. Here, choose the box from the list.", "En el examen arrastraría cada organismo a su casilla. Aquí, elija la casilla en la lista."), "grupos": G, "etiqueta": t("Feeding level:", "Nivel trófico:"),
                "piezas": [{"t": a, "v": v, "pista": PI[v]} for a, v in piezas], "extra": t("Producers make food; primary consumers eat producers; secondary consumers eat primary consumers.", "Los productores fabrican alimento; los consumidores primarios comen productores; los secundarios comen consumidores primarios.")}
    return [item(t("A meadow food chain", "Cadena alimentaria de una pradera"), [(t("Clover", "Trébol"), 0), (t("Grasshopper", "Saltamontes"), 1), (t("Frog that eats grasshoppers", "Rana que come saltamontes"), 2), (t("Oak tree", "Roble"), 0), (t("Deer", "Ciervo"), 1)]),
            item(t("A pond food chain", "Cadena alimentaria de un estanque"), [(t("Algae", "Algas"), 0), (t("Tadpole that eats algae", "Renacuajo que come algas"), 1), (t("Fish that eats tadpoles", "Pez que come renacuajos"), 2), (t("Water lily", "Nenúfar"), 0), (t("Snail that eats plants", "Caracol que come plantas"), 1)])]


def ordenes():
    pasos = [t("Write the unbalanced equation: H₂ + O₂ → H₂O", "Escriba la ecuación sin equilibrar: H₂ + O₂ → H₂O"), t("Count the atoms on each side: O is 2 on the left and 1 on the right", "Cuente los átomos de cada lado: el O es 2 a la izquierda y 1 a la derecha"),
             t("Put a 2 in front of H₂O to balance oxygen", "Ponga un 2 delante de H₂O para equilibrar el oxígeno"), t("Now H is 2 on the left and 4 on the right: put a 2 in front of H₂", "Ahora el H es 2 a la izquierda y 4 a la derecha: ponga un 2 delante de H₂"),
             t("Check: 2 H₂ + O₂ → 2 H₂O has 4 H and 2 O on each side", "Compruebe: 2 H₂ + O₂ → 2 H₂O tiene 4 H y 2 O en cada lado")]
    cons = {"1>0": t("You count atoms in an equation that is already written.", "Se cuentan los átomos de una ecuación ya escrita."), "2>1": t("You fix oxygen after you see it is unbalanced.", "Se corrige el oxígeno después de ver que no está equilibrado."),
            "3>2": t("Hydrogen becomes unbalanced only after you add the 2 to H₂O.", "El hidrógeno se desequilibra solo después de poner el 2 en H₂O."), "4>3": t("You check at the end.", "Se comprueba al final.")}
    return [{"titulo": t("Balancing an equation · In order", "Equilibrar una ecuación · En orden"), "intro": t("On the test you would drag the steps into order. Here, use ▲ and ▼.", "En el examen arrastraría los pasos para ordenarlos. Aquí, use ▲ y ▼."),
             "pasos": pasos, "inicio": [2, 4, 0, 3, 1], "cons": cons, "general": t("Write, count, fix one element, recount, check.", "Escribir, contar, corregir un elemento, volver a contar, comprobar.")}]


def huecos():
    return [
        {"partes": [t("When a moving object speeds up, the net force on it is ", "Cuando un objeto en movimiento acelera, la fuerza neta sobre él es "), {"ops": [t("not zero", "distinta de cero"), t("zero", "cero")], "ok": 0}, t(", and it points ", ", y apunta "), {"ops": [t("in the direction of motion", "en el sentido del movimiento"), t("against the motion", "en contra del movimiento")], "ok": 0}, "."],
         "pista": t("Speeding up needs a net force forward.", "Acelerar exige una fuerza neta hacia delante."), "exp": t("Speeding up → net force in the direction of motion.", "Acelerar → fuerza neta en el sentido del movimiento.")},
        {"partes": [t("In photosynthesis, plants take in ", "En la fotosíntesis, las plantas toman "), {"ops": [t("carbon dioxide", "dióxido de carbono"), t("oxygen", "oxígeno")], "ok": 0}, t(" and give off ", " y liberan "), {"ops": [t("oxygen", "oxígeno"), t("carbon dioxide", "dióxido de carbono")], "ok": 0}, "."],
         "pista": t("Photosynthesis is the reverse of breathing out CO₂.", "La fotosíntesis es lo contrario de exhalar CO₂."), "exp": t("CO₂ in, O₂ out.", "Entra CO₂, sale O₂.")},
        {"partes": [t("If the wavelength gets shorter and the speed stays the same, the frequency ", "Si la longitud de onda disminuye y la velocidad no cambia, la frecuencia "), {"ops": [t("goes up", "aumenta"), t("goes down", "disminuye"), t("stays the same", "no cambia")], "ok": 0}, t(" and the energy ", " y la energía "), {"ops": [t("goes up", "aumenta"), t("goes down", "disminuye")], "ok": 0}, "."],
         "pista": t("v = λ × f, and shorter waves carry more energy.", "v = λ × f, y las ondas más cortas llevan más energía."), "exp": t("Shorter λ → higher f → more energy.", "Menor λ → mayor f → más energía.")},
        {"partes": [t("A statement about the usual pattern over thirty years describes ", "Una afirmación sobre el patrón habitual de treinta años describe "), {"ops": [t("climate", "el clima"), t("weather", "el tiempo meteorológico")], "ok": 0}, t(", while a forecast for tomorrow describes ", ", mientras que el pronóstico de mañana describe "), {"ops": [t("weather", "el tiempo meteorológico"), t("climate", "el clima")], "ok": 0}, "."],
         "pista": t("The time scale decides.", "Decide la escala temporal."), "exp": t("Decades → climate; days → weather.", "Décadas → clima; días → tiempo.")},
        {"partes": [t("In undisturbed rock layers, the layer at the bottom is the ", "En capas de roca no alteradas, la capa de abajo es la "), {"ops": [t("oldest", "más antigua"), t("youngest", "más reciente")], "ok": 0}, t(", and an intrusion that cuts a layer is ", ", y una intrusión que corta una capa es "), {"ops": [t("younger", "más joven"), t("older", "más antigua")], "ok": 0}, t(" than that layer.", " que esa capa.")],
         "pista": t("Superposition and the cutting rule.", "Superposición y regla del corte."), "exp": t("Bottom = oldest; what cuts is younger.", "Abajo = más antigua; lo que corta es más joven.")},
    ]


def completar():
    rnd = random.Random(83)
    out = []
    fmt = lambda x: format(D(x).normalize(), "f")
    for n in range(24):
        k = n % 4
        if k == 0:
            m = rnd.choice([20, 40, 50, 80, 100, 120, 150]); v = D(rnd.choice(["2", "2.5", "4", "5", "8", "10"]))
            r = D(m) / v; enun = t(f"An object has a mass of {m} g and a volume of {fmt(v)} cm³. What is its density, in <strong>g/cm³</strong>?", f"Un objeto tiene una masa de {m} g y un volumen de {fmt(v)} cm³. ¿Cuál es su densidad, en <strong>g/cm³</strong>?")
            exp = t(f"D = m ÷ V = {m} ÷ {fmt(v)} = {fmt(r)}.", f"D = m ÷ V = {m} ÷ {fmt(v)} = {fmt(r)}.")
        elif k == 1:
            m = rnd.choice([2, 5, 10, 20, 50]); a = rnd.choice([2, 3, 4, 5, 6])
            r = D(m * a); enun = t(f"A {m} kg cart speeds up at {a} m/s². What net force acts on it, in <strong>N</strong>?", f"Un carrito de {m} kg acelera a {a} m/s². ¿Qué fuerza neta actúa sobre él, en <strong>N</strong>?")
            exp = t(f"F = m × a = {m} × {a} = {r}.", f"F = m × a = {m} × {a} = {r}.")
        elif k == 2:
            W = rnd.choice([300, 600, 900, 1200, 1500]); s = rnd.choice([10, 20, 30, 60])
            r = D(W) / s; enun = t(f"A motor does {W:,} J of work in {s} s. What is its power, in <strong>W</strong>?", f"Un motor realiza {W:,} J de trabajo en {s} s. ¿Cuál es su potencia, en <strong>W</strong>?")
            exp = t(f"P = W ÷ t = {W:,} ÷ {s} = {fmt(r)}.", f"P = W ÷ t = {W:,} ÷ {s} = {fmt(r)}.")
        else:
            vals = [rnd.randint(10, 30) for _ in range(5)]
            r = D(sum(vals)) / 5; enun = t(f"Five plants measured {', '.join(map(str, vals))} cm. What is the mean height, in <strong>cm</strong>?", f"Cinco plantas midieron {', '.join(map(str, vals))} cm. ¿Cuál es la altura media, en <strong>cm</strong>?")
            exp = t(f"({' + '.join(map(str, vals))}) ÷ 5 = {sum(vals)} ÷ 5 = {fmt(r)}.", f"({' + '.join(map(str, vals))}) ÷ 5 = {sum(vals)} ÷ 5 = {fmt(r)}.")
        if r != r.quantize(D("0.01")):
            continue
        out.append({"enun": f"<p>{enun}</p>", "r": fmt(r), "exp": exp})
    return out


# ---- punto en una imagen: SVG con zonas que se pueden pulsar o elegir con el teclado
def svg_montana():
    pts = [("A", 70, 72), ("B", 190, 200), ("C", 272, 262), ("D", 404, 152), ("E", 470, 122)]
    z = "".join(f'<circle data-z="{l}" data-l="{t("Point", "Punto")} {l}" cx="{x}" cy="{y}" r="16" fill="#e8efff" stroke="#14265e" stroke-width="3"/><text x="{x}" y="{y + 5}" text-anchor="middle" font-size="14" font-weight="700" fill="#14265e" pointer-events="none">{l}</text>' for l, x, y in pts)
    return ('<svg viewBox="0 0 680 300" style="width:100%;max-width:640px;height:auto" role="group" aria-label="' + t("Roller coaster profile with five points, A to E, from left to right. A is the highest; C is the lowest; E is high but lower than A.", "Perfil de una montaña rusa con cinco puntos, de la A a la E, de izquierda a derecha. A es el más alto; C, el más bajo; E está alto, pero más bajo que A.") + '" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M 40 70 Q 130 74 175 170 Q 215 254 265 262 Q 330 270 385 176 Q 425 112 470 122 Q 520 132 560 210 Q 590 264 640 268" fill="none" stroke="#1e3a8a" stroke-width="5"/>' + z + '</svg>')


def svg_vt():
    return ('<svg viewBox="0 0 620 280" style="width:100%;max-width:600px;height:auto" role="group" aria-label="' + t("Velocity-time graph in three parts: part 1 rises, part 2 is flat above zero, part 3 falls to zero.", "Gráfica de velocidad frente a tiempo en tres tramos: el tramo 1 sube, el 2 es horizontal por encima del cero y el 3 baja hasta cero.") + '" xmlns="http://www.w3.org/2000/svg">'
            '<line x1="60" y1="230" x2="600" y2="230" stroke="#222" stroke-width="2"/><line x1="60" y1="230" x2="60" y2="30" stroke="#222" stroke-width="2"/>'
            f'<text x="330" y="266" text-anchor="middle" font-size="14" fill="#222">{t("Time", "Tiempo")}</text><text x="24" y="130" text-anchor="middle" font-size="14" fill="#222">v</text>'
            f'<line data-z="1" data-l="{t("Part 1", "Tramo 1")}" x1="60" y1="230" x2="230" y2="80" stroke="#5b8def" stroke-width="16" stroke-linecap="round"/>'
            f'<line data-z="2" data-l="{t("Part 2", "Tramo 2")}" x1="230" y1="80" x2="420" y2="80" stroke="#5b8def" stroke-width="16" stroke-linecap="round"/>'
            f'<line data-z="3" data-l="{t("Part 3", "Tramo 3")}" x1="420" y1="80" x2="580" y2="230" stroke="#5b8def" stroke-width="16" stroke-linecap="round"/>'
            '<text x="130" y="140" font-size="15" font-weight="700" fill="#14265e">1</text><text x="325" y="66" font-size="15" font-weight="700" fill="#14265e">2</text><text x="512" y="140" font-size="15" font-weight="700" fill="#14265e">3</text></svg>')


def svg_capas():
    let = "ABCDE"
    z = "".join(f'<rect data-z="{let[i]}" data-l="{t("Layer", "Capa")} {let[i]}" x="40" y="{30 + (4 - i) * 42}" width="300" height="42" fill="{["#b39ddb", "#c5b3e6", "#d6c9ef", "#e4dbf6", "#efe9fa"][i]}" stroke="#3c1478" stroke-width="2"/><text x="56" y="{30 + (4 - i) * 42 + 27}" font-size="15" font-weight="700" fill="#3c1478" pointer-events="none">{let[i]}</text>' for i in range(5))
    return ('<svg viewBox="0 0 380 270" style="width:100%;max-width:380px;height:auto" role="group" aria-label="' + t("Rock column with five layers. From top to bottom: E, D, C, B, A. An intrusion cuts layers A and B.", "Columna con cinco capas. De arriba abajo: E, D, C, B, A. Una intrusión corta las capas A y B.") + '" xmlns="http://www.w3.org/2000/svg">' + z +
            '<polygon points="240,240 262,240 255,156 247,156" fill="#5b21b6" pointer-events="none"/>' + f'<text x="251" y="258" text-anchor="middle" font-size="12" font-weight="700" fill="#3c1478">{t("Intrusion", "Intrusión")}</text></svg>')


def svg_tierra():
    capas = [("1", 130, "#a78bdb", t("outer ring", "anillo exterior")), ("2", 122, "#e6dcf9", t("second ring", "segundo anillo")), ("3", 76, "#d3c3f2", t("third ring", "tercer anillo")), ("4", 38, "#7c3aed", t("center", "centro"))]
    z = "".join(f'<circle data-z="{k}" data-l="{t("Zone", "Zona")} {k} ({d})" cx="150" cy="145" r="{r}" fill="{c}" stroke="#3c1478" stroke-width="2"/>' for k, r, c, d in capas)
    return ('<svg viewBox="0 0 300 290" style="width:100%;max-width:300px;height:auto" role="group" aria-label="' + t("Cutaway of Earth with four zones, from the thin outer ring to the center. No labels.", "Corte de la Tierra con cuatro zonas, del anillo exterior delgado al centro. Sin rótulos.") + '" xmlns="http://www.w3.org/2000/svg">' + z + '</svg>')


def banco_punto():
    M, V, K, T = svg_montana(), svg_vt(), svg_capas(), svg_tierra()
    d = [(M, t("Click the point where the car has the <strong>most kinetic energy</strong> (no friction).", "Haga clic en el punto donde el vagón tiene <strong>más energía cinética</strong> (sin fricción)."), "C", t("Lowest point → most kinetic energy.", "Punto más bajo → más energía cinética.")),
         (M, t("Click the point where the car has the <strong>most potential energy</strong>.", "Haga clic en el punto donde el vagón tiene <strong>más energía potencial</strong>."), "A", t("Highest point → most potential energy.", "Punto más alto → más energía potencial.")),
         (V, t("Click the part of the graph where the <strong>net force is zero</strong>.", "Haga clic en el tramo de la gráfica donde la <strong>fuerza neta es cero</strong>."), "2", t("Flat above zero: constant speed, net force zero.", "Horizontal sobre cero: velocidad constante, fuerza neta cero.")),
         (V, t("Click the part of the graph where the object is <strong>slowing down</strong>.", "Haga clic en el tramo de la gráfica donde el objeto <strong>frena</strong>."), "3", t("The line falls: speed decreases.", "La línea baja: la velocidad disminuye.")),
         (K, t("Click the <strong>oldest</strong> layer.", "Haga clic en la capa <strong>más antigua</strong>."), "A", t("Superposition: the bottom layer was laid down first.", "Superposición: la capa de abajo se depositó primero.")),
         (K, t("Click the <strong>oldest layer that the intrusion does not cut</strong>.", "Haga clic en la <strong>capa más antigua que la intrusión no corta</strong>."), "C", t("The intrusion cuts A and B; C covers it.", "La intrusión corta A y B; la C la cubre.")),
         (T, t("Click the <strong>mantle</strong>, where convection currents move the plates.", "Haga clic en el <strong>manto</strong>, donde las corrientes de convección mueven las placas."), "2", t("The thick second ring is the mantle.", "El grueso segundo anillo es el manto.")),
         (T, t("Click the <strong>outer core</strong>, made of liquid metal.", "Haga clic en el <strong>núcleo externo</strong>, de metal líquido."), "3", t("Third ring: liquid outer core.", "Tercer anillo: núcleo externo líquido."))]
    return [{"enun": f"<p>{q}</p>{s}", "ok": ok, "exp": e} for s, q, ok, e in d]


PUNTO_JS = r'''
function creaPunto(pre, banco){
  var saca = mazo(banco), est = {primero: 0, pista: 0, total: 0}, it, intentos, cerrado, fb = $(pre + "-fb"), zs = [];
  function pulsa(z){
    if (cerrado) return;
    zs.forEach(function(x){ x.classList.remove("z-sel"); x.setAttribute("aria-pressed", "false"); });
    z.classList.add("z-sel"); z.setAttribute("aria-pressed", "true");
    intentos++;
    if (z.dataset.z === it.ok){ cerrado = true; cuenta(est, intentos, true); z.classList.add("z-ok"); fb.className = "fb bien"; fb.innerHTML = TX.bien + it.exp + " <em>" + (intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>"; }
    else if (intentos === 1){ z.classList.add("z-mal"); fb.className = "fb pista"; fb.innerHTML = TX.todavia + (ES ? "Esa zona no es. Vuelva a leer la pregunta y localice la respuesta antes de hacer clic." : "That is not the spot. Reread the question and find the answer before you click.") + TX.otraVez; }
    else { cerrado = true; cuenta(est, intentos, false); z.classList.add("z-mal"); zs.forEach(function(x){ if (x.dataset.z === it.ok) x.classList.add("z-ok"); }); fb.className = "fb mal"; fb.innerHTML = TX.asi + it.exp + TX.nuevo; }
    marcador(pre, est);
  }
  function nuevo(){
    it = saca(); intentos = 0; cerrado = false; fb.className = "fb"; fb.innerHTML = "";
    $(pre + "-enun").innerHTML = it.enun;
    zs = [].slice.call($(pre + "-enun").querySelectorAll("[data-z]"));
    zs.forEach(function(z){
      z.setAttribute("tabindex", "0"); z.setAttribute("role", "button"); z.setAttribute("aria-pressed", "false"); z.setAttribute("aria-label", z.dataset.l); z.classList.add("zona");
      z.addEventListener("click", function(){ pulsa(z); });
      z.addEventListener("keydown", function(e){ if (e.key === "Enter" || e.key === " "){ e.preventDefault(); pulsa(z); } });
    });
  }
  $(pre + "-nuevo").addEventListener("click", nuevo);
  nuevo(); marcador(pre, est);
}
'''


def punto_html(pid):
    return f'''      <p>{t("On the test you click a place on the picture. Here you can also use the Tab key to move between the zones and Enter to choose.", "En el examen se hace clic en un lugar de la imagen. Aquí también puede usar la tecla Tab para pasar de una zona a otra y Enter para elegir.")}</p>
      <style>.zona{{cursor:pointer;}} .zona:focus{{outline:3px solid #1e3a8a;outline-offset:2px;}} .zona:hover{{opacity:.8;}} .z-sel{{stroke:#1e3a8a !important;stroke-width:4 !important;}} line.z-sel{{stroke:#1e3a8a !important;stroke-width:16 !important;}} .z-ok{{fill:#c8e6c9 !important;stroke:#2e7d32 !important;}} line.z-ok{{stroke:#43a047 !important;}} .z-mal{{fill:#ffcdd2 !important;stroke:#b71c1c !important;}} line.z-mal{{stroke:#e57373 !important;}}</style>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="fb" id="{pid}-fb" role="status" aria-live="polite"></div>
        <div class="fila-btn"><button type="button" class="btn-sec" id="{pid}-nuevo">{t("New exercise", "Otro ejercicio")}</button></div>
        <p class="marcador" id="{pid}-marcador" aria-live="polite"></p>
      </div>'''


def practica():
    A = {"en": ["multiple-choice", "drag-drop", "drop-down", "fill-in", "hot-spot"], "es": ["opcion-multiple", "arrastrar", "desplegable", "completar", "punto"]}[C.L]
    mods = [
        (A[0], t("Format 1 · Multiple choice", "Formato 1 · Opción múltiple"), C.om("m1", t("Read all four options before choosing.", "Lea las cuatro opciones antes de elegir."))),
        (A[1], t("Format 2 · Drag and drop", "Formato 2 · Arrastrar y soltar"), C.clasifica("m2") + "\n" + C.orden("m3")),
        (A[2], t("Format 3 · Drop-down menu", "Formato 3 · Menú desplegable"), C.huecos("m4", t("Choose in each menu, then reread the whole sentence.", "Elija en cada menú y después relea la frase entera."))),
        (A[3], t("Format 4 · Fill in the blank", "Formato 4 · Completar espacios"), "      <p>" + t("Type only the number: no unit, no words.", "Escriba solo el número: sin unidad ni palabras.") + "</p>\n" + C.dec_campo("m5", t("Answer", "Respuesta"))),
        (A[4], t("Format 5 · Hot spot", "Formato 5 · Punto en una imagen"), punto_html("m6")),
    ]
    pista = t("Use the formula, calculate, and type only the number.", "Aplique la fórmula, calcule y escriba solo el número.")
    js = (C.js_datos("OM", banco_om()) + C.js_datos("TRO", clasif_troficos()) + C.js_datos("ORD", ordenes()) + C.js_datos("HUE", huecos()) + C.js_datos("COM", completar()) + C.js_datos("PUN", banco_punto()) + PUNTO_JS +
          f"var sacaC = mazo(COM), PC = {C.json.dumps(pista, ensure_ascii=False)};\nfunction gC(){{ var q = sacaC(); return {{enun: q.enun, resp: leeNumero(q.r), explica: q.exp, pista: function(){{ return PC; }}}}; }}\n" +
          'creaBanco("m1", OM);\ncreaClasifica("m2", TRO);\ncreaOrden("m3", ORD);\ncreaHuecos("m4", HUE);\ncreaPracticaDec("m5", gC);\ncreaPunto("m6", PUN);\n')
    meta = t(f'Five activities, one for each item type · then take the <a href="{sim()}">timed practice test</a> · calculator included', f'Cinco actividades, una por cada formato · después, el <a href="{sim()}">simulacro cronometrado</a> · con calculadora')
    return C.pagina_practica(N, titulo(), meta, mods, js, scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
