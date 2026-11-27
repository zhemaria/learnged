"""LearnGED · Estudios sociales · Lección 1.3 · Sesgo, punto de vista y lenguaje persuasivo (EN/ES).
Fuente: sociales/soc-1-3.html y las fichas del Archivo de fuentes (The Public y Street Railway Journal, 1905).
Uso: python3 tools/build_soc_1_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, documento, cita

N = "1-3"


def titulo():
    return t("Bias, point of view, and persuasive language", "Sesgo, punto de vista y lenguaje persuasivo")


def doc_a():
    ficha = [
        (t("Publication", "Publicación"), t("<cite>The Public</cite>, a weekly edited in Chicago by Louis F. Post, who openly supported city ownership of the streetcars", "<cite>The Public</cite>, semanario dirigido en Chicago por Louis F. Post, partidario declarado de que la ciudad fuera dueña de los tranvías")),
        (t("Date", "Fecha"), t("Saturday, September 23, 1905, pages 391–392", "Sábado 23 de septiembre de 1905, páginas 391 y 392")),
        (t("Kind of source", "Tipo de fuente"), t("Primary · news report in a political weekly", "Primaria · crónica en un semanario político")),
        (t("Legal status", "Situación legal"), t("Public domain in the United States (published in 1905)", "Dominio público en los Estados Unidos (publicado en 1905)")),
    ]
    partes = [
        (t("Fragment 1 · The headline and the first lines", "Fragmento 1 · El titular y las primeras líneas"),
         ["<strong>Progress of the Chicago traction movement.</strong>",
          "At the adjourned meeting of the local transportation committee of the City Council of Chicago on the 15th, held for the purpose of receiving proposals from the existing companies, no progress was made. All the traction interests were represented, and Col. E. R. Bliss acted as their spokesman. Col. Bliss stated that he had a proposition to make, but refused to submit it."],
         ["<strong>Avances del movimiento tranviario de Chicago.</strong>",
          "En la sesión aplazada del comité de transporte local del Concejo Municipal de Chicago, celebrada el día 15 con el propósito de recibir propuestas de las compañías existentes, no se produjo avance alguno. Todos los intereses tranviarios estaban representados, y el coronel E. R. Bliss actuó como su portavoz. El coronel Bliss declaró que tenía una propuesta que hacer, pero se negó a presentarla."]),
        (t("Fragment 2 · Alderman Finn’s questions", "Fragmento 2 · Las preguntas del concejal Finn"),
         ["Alderman Finn asked him: “Will you agree to sell at any time the city asks you to for the cost of construction, irrespective of franchise rights?”",
          "Col. Bliss replied: “We will not.”",
          "Alderman Finn again asked: “What is the earliest time you will sell to the city, irrespective of franchise rights?”",
          "To this Col. Bliss replied: “We cannot answer now, and will not say that we will sell at any time.”"],
         ["El concejal Finn le preguntó: «¿Accederán ustedes a vender en cualquier momento en que la ciudad se lo pida, por el costo de construcción, con independencia de los derechos de concesión?».",
          "El coronel Bliss respondió: «No accederemos».",
          "El concejal Finn preguntó de nuevo: «¿Cuál es la fecha más temprana en que venderán ustedes a la ciudad, con independencia de los derechos de concesión?».",
          "A esto respondió el coronel Bliss: «No podemos responder ahora, y no diremos que vayamos a vender en ningún momento»."]),
        (t("Fragment 3 · The end of the meeting", "Fragmento 3 · El final de la sesión"),
         ["Asked if he had a plan to offer, Col. Bliss replied that he had, but would not offer it then. Aldermen Finn and Dever tried to get the plan before the committee, but were voted down, seven to five, on Alderman Foreman’s motion to continue with the questions. The committee adjourned until the 26th."],
         ["Preguntado si tenía un plan que ofrecer, el coronel Bliss respondió que sí lo tenía, pero que no lo ofrecería entonces. Los concejales Finn y Dever intentaron llevar el plan ante el comité, pero fueron derrotados en votación, siete contra cinco, por la moción del concejal Foreman de continuar con las preguntas. El comité se aplazó hasta el día 26."]),
    ]
    return documento(t("Document A · <em>The Public</em>", "Documento A · <em>The Public</em>"), ficha, partes)


def doc_b():
    ficha = [
        (t("Publication", "Publicación"), t("<cite>Street Railway Journal</cite>, a trade magazine of the streetcar industry, published in New York. Its readers and its advertisers were the streetcar companies.", "<cite>Street Railway Journal</cite>, revista profesional del sector de los tranvías, publicada en Nueva York. Sus lectores y sus anunciantes eran las compañías de tranvías.")),
        (t("Date", "Fecha"), t("Saturday, September 23, 1905, page 467", "Sábado 23 de septiembre de 1905, página 467")),
        (t("Kind of source", "Tipo de fuente"), t("Primary · news report in a trade magazine", "Primaria · nota en una revista profesional")),
        (t("Legal status", "Situación legal"), t("Public domain in the United States (published in 1905)", "Dominio público en los Estados Unidos (publicado en 1905)")),
    ]
    partes = [
        (t("Fragment 1 · The headline and the first lines", "Fragmento 1 · El titular y las primeras líneas"),
         ["<strong>Chicago company to reply to questions propounded by the City Council.</strong>",
          "The meeting of the committee on local transportation of the Chicago City Council on Friday, Sept. 15, ended in the traction companies agreeing to answer on Sept. 26 several questions submitted by aldermen. The tangible results of the meeting were two offers, made by the Chicago City Company, as a part of what it would agree to do in order to secure an extension of franchise."],
         ["<strong>La compañía de Chicago responderá a las preguntas planteadas por el Concejo Municipal.</strong>",
          "La reunión del comité de transporte local del Concejo Municipal de Chicago, celebrada el viernes 15 de septiembre, terminó con el acuerdo de las compañías tranviarias de responder el 26 de septiembre a varias preguntas presentadas por los concejales. Los resultados tangibles de la reunión fueron dos ofrecimientos, hechos por la Chicago City Company como parte de lo que aceptaría hacer a cambio de obtener una prórroga de la concesión."]),
        (t("Fragment 2 · The other company", "Fragmento 2 · La otra compañía"),
         ["While the Union Traction representatives did not concur in these offers, they sat silent when the one involving them was made. They are understood to be bound by it."],
         ["Aunque los representantes de la Union Traction no se sumaron a esos ofrecimientos, guardaron silencio cuando se formuló el que les afectaba. Se entiende que quedan obligados por él."]),
        (t("Fragment 3 · What is still pending", "Fragmento 3 · Lo que queda pendiente"),
         ["The important questions which the company has agreed to answer at the next meeting of the committee are: In any settlement agreement which may be made will it be provided that at a determined period, or periods, during the life of the agreement the city may take over your lines? Will you agree to the city taking over the lines at any time during the life of the franchise, if one is granted?"],
         ["Las preguntas importantes que la compañía ha aceptado responder en la próxima reunión del comité son: En cualquier acuerdo que llegue a hacerse, ¿se dispondrá que en un período o unos períodos determinados, durante la vigencia del acuerdo, la ciudad pueda hacerse cargo de sus líneas? ¿Aceptarán ustedes que la ciudad se haga cargo de las líneas en cualquier momento durante la vigencia de la concesión, si se otorga una?"]),
    ]
    return documento(t("Document B · <em>Street Railway Journal</em>", "Documento B · <em>Street Railway Journal</em>"), ficha, partes)


def leccion():
    P = C.Practicas()
    FAL, SES, NIN = t("Falsehood", "Falsedad"), t("Bias", "Sesgo"), t("Neither", "Ninguna de las dos")

    s1 = f"""<p>{t("The word <strong>bias</strong> is almost always used as an accusation. Saying that a newspaper is biased sounds like saying it lies. It is worth separating the two ideas from the start, because the GED® Social Studies test does not ask whether a source lies: it asks <strong>where it is looking from</strong>.",
"La palabra <strong>sesgo</strong> se usa casi siempre como acusación. Decir que un periódico tiene sesgo suena a decir que engaña. Conviene separar las dos cosas desde el principio, porque el examen de Estudios Sociales del GED® no pregunta si una fuente miente: pregunta <strong>desde dónde mira</strong>.")}</p>
{C.tabla(t("False and biased are not the same", "Falso y sesgado no es lo mismo"),
         ["", t("A false source", "Una fuente falsa"), t("A biased source", "Una fuente sesgada")],
         [[t("What it does", "Qué hace"), t("States facts that did not happen.", "Afirma hechos que no ocurrieron."), t("States facts that did happen, but not all of them, and presents them with words that push toward a conclusion.", "Afirma hechos que sí ocurrieron, pero no todos, y los presenta con palabras que empujan hacia una conclusión.")],
          [t("How you answer it", "Cómo se responde"), t("By checking the facts: it is <strong>refuted</strong>.", "Comprobando los hechos: se <strong>refuta</strong>."), t("By reading another source: it is <strong>completed</strong>.", "Leyendo otra fuente: se <strong>completa</strong>.")],
          [t("Is it useful?", "¿Sirve?"), t("Only as evidence of who spread the lie and why.", "Solo como evidencia de quién difundió la mentira y por qué."), t("Yes, twice: for its facts, and as evidence of what mattered to the writer.", "Sí, dos veces: por sus hechos, y como evidencia de lo que le importaba a quien la escribió.")]])}
{C.caja("tip", t("The idea this lesson hangs on", "La idea de la que cuelga esta lección"), "<p>" + t("Bias is not usually in what a document says. It is in <strong>what it chooses to tell</strong>, in the order it puts things, and in the words it picks. That is why a biased source is still useful: its facts are good, and its choices show whom it serves.", "El sesgo no suele estar en lo que un documento dice. Está en <strong>lo que decide contar</strong>, en el orden en que lo pone y en las palabras que elige. Por eso una fuente sesgada sigue siendo útil: sus hechos valen, y su selección revela a quién sirve.") + "</p>")}
<p>{t("A beginner reader throws a one-sided source away. A skilled reader uses it twice: once for the facts it gives, and once as evidence of what mattered to the person who wrote it.",
"Ante una fuente parcial, el lector novato la descarta. El lector competente la usa dos veces: una por los hechos que aporta, y otra como prueba de lo que le importaba a quien la escribió.")}</p>
<h3>{t("Try it", "Inténtelo")}</h3>
{P(t("Practice 1 · False or biased?", "Práctica 1 · ¿Falso o sesgado?"), t("A newspaper writes that twenty aldermen attended the meeting, but the official minutes record twelve.", "Un periódico escribe que a la reunión asistieron veinte concejales, pero el acta oficial registra doce."), [FAL, SES, NIN], 0,
   {1: t("This is not about which facts were chosen: a number is wrong.", "No se trata de qué hechos se eligieron: una cifra es incorrecta."), 2: t("Something here can be checked, and it does not match.", "Aquí hay algo comprobable, y no coincide.")},
   t("<strong>Falsehood</strong> (or at least an error): a fact that can be checked against the minutes, and does not match.", "<strong>Falsedad</strong> (o por lo menos un error): un hecho que se puede comprobar con el acta, y no coincide."))}
{P(t("Practice 2 · False or biased?", "Práctica 2 · ¿Falso o sesgado?"), t("One newspaper writes that at the meeting “no progress was made.” Another writes that “the tangible results were two offers.”", "Un periódico escribe que en la reunión «no se produjo avance alguno». Otro escribe que «los resultados tangibles fueron dos ofrecimientos»."), [FAL, SES, t("One of them must be lying", "Uno de los dos miente por fuerza")], 1,
   {0: t("Could both statements be about real events at the same meeting?", "¿Podrían las dos afirmaciones hablar de hechos reales de la misma reunión?"), 2: t("“Progress” and “tangible” are judgments, not facts.", "«Avance» y «tangibles» son juicios, no hechos.")},
   t("<strong>Bias.</strong> Both can be true at once: offers were made, and the city got nothing it wanted. Each paper chose what to stress and which word to use.", "<strong>Sesgo.</strong> Las dos pueden ser ciertas a la vez: hubo ofrecimientos, y la ciudad no obtuvo nada de lo que quería. Cada periódico eligió qué destacar y qué palabra usar."))}"""

    s2 = f"""<p>{t("In 1905, Chicago had been arguing for years about who should own its streetcars (then called <em>traction</em> lines). The lines belonged to private companies that ran them with city permits called <strong>franchises</strong>. Mayor Edward F. Dunne had won the April election promising that the city would buy them.",
"En 1905, Chicago llevaba años discutiendo quién debía ser dueño de sus tranvías (en inglés se llamaban líneas de <em>tracción</em>). Las líneas eran de compañías privadas que operaban con permisos municipales llamados <strong>concesiones</strong>. El alcalde Edward F. Dunne había ganado las elecciones de abril prometiendo que la ciudad las compraría.")}</p>
<p>{t("On Friday, September 15, the City Council’s transportation committee met to hear proposals from the companies. The aldermen asked questions. Colonel E. R. Bliss answered for the companies. Eight days later, on the same Saturday, two publications told the story of that meeting. Both are primary sources. Neither one lies. And yet, if you read them one after the other, they seem to describe two different meetings.",
"El viernes 15 de septiembre, el comité de transporte del Concejo se reunió para escuchar propuestas de las compañías. Los concejales preguntaron. El coronel E. R. Bliss respondió en nombre de las compañías. Ocho días después, el mismo sábado, dos publicaciones contaron esa reunión. Las dos son fuentes primarias. Ninguna miente. Y sin embargo, si se leen seguidas, parecen dos reuniones distintas.")}</p>
{doc_a()}
{doc_b()}
{P(t("Question 1", "Pregunta 1"), t("How are the events in the two documents related?", "¿Qué relación hay entre los hechos que narran los dos documentos?"),
   [t("They tell about different meetings in different weeks", "Narran reuniones distintas de semanas distintas"), t("One tells about the meeting and the other comments on it from far away", "Uno narra la reunión y el otro la comenta desde lejos"), t("They tell about the same meeting on the same day", "Narran la misma reunión del mismo día")], 2,
   {0: t("Check the dates: both say the 15th.", "Compruebe las fechas: los dos dicen el día 15."), 1: t("Both report the meeting itself.", "Los dos informan de la reunión misma.")},
   t("Same committee, same Friday, same publication date. That is what makes the comparison so clear.", "Mismo comité, mismo viernes, misma fecha de publicación. Eso es lo que hace tan clara la comparación."))}
{P(t("Question 2", "Pregunta 2"), t("Document A says Bliss refused to submit his proposal. Document B says the company made two offers. How can both be true?", "El Documento A dice que Bliss se negó a presentar su propuesta. El B dice que la compañía hizo dos ofrecimientos. ¿Cómo pueden ser ciertas las dos cosas?"),
   [t("They are different things: a plan that was not submitted, and offers that were made", "Son cosas distintas: un plan que no se presentó y unos ofrecimientos que sí se hicieron"), t("One of them is inventing", "Uno de los dos inventa"), t("Document B is about another meeting", "El B se refiere a otra reunión")], 0,
   {1: t("Look for a reading where both statements are true.", "Busque una lectura en la que las dos afirmaciones sean ciertas."), 2: t("It names the same date and committee.", "Nombra la misma fecha y el mismo comité.")},
   t("Bliss kept his full plan to himself, and the company also made two smaller offers. Each paper told the part that fit its view.", "Bliss se guardó su plan completo, y la compañía también hizo dos ofrecimientos menores. Cada periódico contó la parte que encajaba con su mirada."))}"""

    filas_inv = [
        [t("The date and the committee", "La fecha y el comité"), t("Yes", "Sí"), t("Yes", "Sí")],
        [t("Bliss refused to submit his plan", "Bliss se negó a presentar su plan"), t("Yes", "Sí"), t("Not mentioned", "No lo menciona")],
        [t("Bliss’s “no” answers to Alderman Finn", "Las negativas de Bliss al concejal Finn"), t("Yes, quoted word for word", "Sí, citadas palabra por palabra"), t("Not mentioned", "No las menciona")],
        [t("The company’s two offers", "Los dos ofrecimientos de la compañía"), t("Not mentioned", "No los menciona"), t("Yes, the center of the story", "Sí, son el centro de la nota")],
        [t("The 7-to-5 vote against seeing the plan", "La votación de siete contra cinco para no ver el plan"), t("Yes", "Sí"), t("Not mentioned", "No la menciona")],
        [t("The meeting moved to the 26th", "El aplazamiento al día 26"), t("Yes", "Sí"), t("Yes", "Sí")],
        [t("Union Traction’s silence", "El silencio de la Union Traction"), t("Not mentioned", "No lo menciona"), t("Yes, and it interprets it", "Sí, y lo interpreta")],
    ]
    s3 = f"""<p>{t("Here is the main tool of the lesson. Put the two documents in columns and note, fact by fact, which one tells it. What appears in one column and not in the other is a <strong>decision</strong> made by the writer.",
"Aquí está la herramienta central de la lección. Ponga los dos documentos en columnas y anote, hecho por hecho, cuál de los dos lo cuenta. Lo que aparece en una columna y no en la otra es una <strong>decisión</strong> de quien escribió.")}</p>
{C.tabla(t("What each document tells about the same meeting", "Qué cuenta cada documento sobre la misma reunión"), [t("Fact from the meeting", "Hecho de la reunión"), "<em>The Public</em>", "<em>Street Railway Journal</em>"], filas_inv)}
{C.caja("tip", t("Look at the shape of the gap", "Fíjese en la forma del hueco"), "<p>" + t("It is not random. Everything <em>The Public</em> leaves out helps the companies, and everything the <em>Street Railway Journal</em> leaves out hurts them. <strong>When all of a source’s omissions point the same way, that direction is its point of view.</strong>", "No es aleatorio. Todo lo que <em>The Public</em> calla favorece a las compañías, y todo lo que calla el <em>Street Railway Journal</em> las perjudica. <strong>Cuando todas las omisiones de una fuente apuntan en la misma dirección, esa dirección es su punto de vista.</strong>") + "</p>")}
<p>{t("Notice one more thing. The two documents never contradict each other on a fact that can be checked. Both say the meeting was on the 15th and the next one on the 26th. When two one-sided sources agree on a detail, you can trust that detail more than if only one of them said it. Two opposite points of view, read together, give a picture that neither one gives alone.",
"Fíjese en algo más. Los dos documentos nunca se contradicen en un hecho comprobable. Los dos dicen que la reunión fue el 15 y la siguiente el 26. Cuando dos fuentes parciales coinciden en un detalle, ese detalle merece más confianza que si lo dijera solo una. Dos parcialidades opuestas, leídas juntas, dan una imagen que ninguna da por separado.")}</p>
{C.enlace(N, t("inventory", "inventario"), t("The inventory of what is missing", "El inventario de lo que falta"), t("Sort the facts of two reports: only in A, only in B, or in both.", "Clasifique los hechos de dos crónicas: solo en A, solo en B o en las dos."))}"""

    S = [t("A judging word in place of a fact", "Una palabra que juzga en lugar de un hecho"), t("Who is named and who is not", "A quién se nombra y a quién no"), t("A claim with no source", "Una atribución sin fuente"), t("The headline as a frame", "El titular como marco")]
    s4 = f"""<p>{t("Point of view is not announced. It leaks out through small choices in the writing. These four signals appear in almost any text, and the two documents of this lesson have all of them.",
"El punto de vista no se anuncia. Se filtra por decisiones pequeñas de redacción. Estas cuatro señales aparecen en casi cualquier texto, y los dos documentos de esta lección las traen todas.")}</p>
{C.tabla(t("Four signals of persuasive language", "Cuatro señales de lenguaje persuasivo"),
         [t("Signal", "Señal"), t("In the two documents", "En los dos documentos"), t("Why it persuades", "Por qué persuade")],
         [[f"1 · {S[0]}", t("A: “no progress was made.” B: “the tangible results were two offers.”", "A: «no se produjo avance alguno». B: «los resultados tangibles fueron dos ofrecimientos»."), t("Neither “progress” nor “tangible” is a fact: they are judgments about the facts, placed where the reader expects information.", "Ni «avance» ni «tangible» son hechos: son juicios sobre los hechos, colocados donde el lector espera información.")],
          [f"2 · {S[1]}", t("A names “Col. E. R. Bliss” again and again, with his rank, for each refusal. B never names him: it says “the company.”", "A nombra al «coronel E. R. Bliss» una y otra vez, con su grado, en cada negativa. B no lo nombra nunca: dice «la compañía»."), t("Putting a name on the refusals makes them personal; removing it dissolves them into an institution.", "Poner un nombre a las negativas las hace personales; quitarlo las disuelve en una institución.")],
          [f"3 · {S[2]}", t("B: “They are understood to be bound by it.” Understood by whom? It does not say.", "B: «Se entiende que quedan obligados por él». ¿Quién lo entiende así? No lo dice."), t("It presents an interpretation as if everyone already agreed with it.", "Presenta una interpretación como si todo el mundo ya estuviera de acuerdo.")],
          [f"4 · {S[3]}", t("A: “Progress of the Chicago traction movement,” over a story that says there was no progress. B: “Chicago company to reply,” about answers not yet given.", "A: «Avances del movimiento tranviario», sobre una crónica que cuenta que no hubo ninguno. B: «La compañía responderá», sobre respuestas que todavía no se han dado."), t("The headline tells the reader how to read the story before reading it.", "El titular le dice al lector cómo leer la nota antes de leerla.")]])}
{P(t("Practice 3 · Which signal?", "Práctica 3 · ¿Qué señal?"), t("“They are understood to be bound by it.”", "«Se entiende que quedan obligados por él»."), S, 2,
   {0: t("Is there a judging adjective here, or something else?", "¿Hay aquí un adjetivo que juzga, o es otra cosa?"), 1: t("No one is named or left unnamed here.", "Aquí no se nombra ni se deja de nombrar a nadie."), 3: t("This sentence is not a headline.", "Esta frase no es un titular.")},
   t("Who understands it? The sentence never says. The impersonal form disguises an interpretation as common knowledge.", "¿Quién lo entiende? La frase nunca lo dice. La forma impersonal disfraza una interpretación de conocimiento común."))}
{P(t("Practice 4 · Which signal?", "Práctica 4 · ¿Qué señal?"), t("One document writes “Col. Bliss” six times; the other writes “the company.”", "Un documento escribe «el coronel Bliss» seis veces; el otro, «la compañía»."), S, 1,
   {0: t("The difference is not a judging word.", "La diferencia no es una palabra que juzga."), 2: t("Both say who acted; they choose different names.", "Los dos dicen quién actuó; eligen nombres distintos."), 3: t("This is in the body of the story, not the headline.", "Esto está en el cuerpo de la nota, no en el titular.")},
   t("A face for the refusals in one; no face in the other.", "Un rostro para las negativas en uno; ningún rostro en el otro."))}
{C.caja("ojo", t("Fact, opinion, and reasoned judgment", "Hecho, opinión y juicio razonado"), "<p>" + t("The test also asks you to sort statements into three kinds. A <strong>fact</strong> can be checked: “The vote was seven to five.” An <strong>opinion</strong> is a preference that evidence cannot settle: “Bliss was a rude man.” A <strong>reasoned judgment</strong> is a conclusion built on evidence that someone could still dispute: “Since the company refused to name a date to sell, the meeting brought the city no closer to owning the lines.” Biased writing often presents an opinion or a judgment in the place where a fact should be.", "El examen también pide clasificar afirmaciones en tres clases. Un <strong>hecho</strong> se puede comprobar: «La votación fue siete contra cinco». Una <strong>opinión</strong> es una preferencia que la evidencia no puede decidir: «Bliss era un hombre grosero». Un <strong>juicio razonado</strong> es una conclusión construida con evidencia que alguien todavía podría discutir: «Como la compañía se negó a fijar una fecha de venta, la reunión no acercó a la ciudad a ser dueña de las líneas». La escritura sesgada suele colocar una opinión o un juicio en el lugar donde debería ir un hecho.") + "</p>")}
{C.enlace(N, t("signals", "senales"), t("Name the signal", "Identifique la señal"), t("Find the persuasive signal, then choose the neutral version.", "Encuentre la señal persuasiva y después elija la versión neutral."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK).",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SSP.5.b", "2", cita(t("“Loose lips might sink ships.”", "«Los labios sueltos pueden hundir barcos»."), t("Slogan on U.S. government posters during World War II", "Lema de carteles del gobierno de los Estados Unidos durante la Segunda Guerra Mundial")) +
   t("What was the main purpose of this slogan?", "¿Cuál era el propósito principal de este lema?"),
   [t("To persuade Americans not to talk about information that could help the enemy", "Persuadir a los estadounidenses de no hablar de información que pudiera ayudar al enemigo"), t("To report how many ships had been sunk", "Informar de cuántos barcos se habían hundido"), t("To recruit sailors for the navy", "Reclutar marineros para la marina"), t("To criticize the government’s war policy", "Criticar la política de guerra del gobierno")], 0,
   {1: t("It gives no numbers: it is a warning, not a report.", "No da cifras: es una advertencia, no un informe."), 2: t("It does not ask anyone to join.", "No pide a nadie que se aliste."), 3: t("The government made it.", "Lo hizo el propio gobierno.")},
   t("It is propaganda in the plain sense: a short, memorable message from the government to change behavior. Propaganda is not always false; what defines it is that it is made to persuade.", "Es propaganda en sentido estricto: un mensaje breve y fácil de recordar, del gobierno, para cambiar una conducta. La propaganda no siempre es falsa; lo que la define es que está hecha para persuadir."))}
{G(2, "SSP.7.a", "2", t("<em>Four statements about the streetcar meeting of September 15, 1905:</em><br>Which one is a <strong>fact</strong> that could be checked?", "<em>Cuatro afirmaciones sobre la reunión tranviaria del 15 de septiembre de 1905:</em><br>¿Cuál es un <strong>hecho</strong> que se podría comprobar?"),
   [t("The committee voted seven to five not to hear Bliss’s plan.", "El comité votó siete contra cinco no escuchar el plan de Bliss."), t("The meeting was a waste of everyone’s time.", "La reunión fue una pérdida de tiempo para todos."), t("The companies were greedy.", "Las compañías eran codiciosas."), t("The city should have bought the lines right away.", "La ciudad debió comprar las líneas de inmediato.")], 0,
   {1: t("“A waste of time” is a judgment.", "«Una pérdida de tiempo» es un juicio."), 2: t("“Greedy” is an opinion about motives.", "«Codiciosas» es una opinión sobre los motivos."), 3: t("“Should” signals an opinion about what is best.", "«Debió» indica una opinión sobre lo mejor.")},
   t("A vote count can be checked in the minutes. The other three are opinions or judgments.", "Un resultado de votación se puede comprobar en el acta. Las otras tres son opiniones o juicios."))}
{G(3, "SSP.8.a", "2–3", t("<em>Look at the table in section 3 of this lesson.</em><br>Which statement best describes how the two documents differ?", "<em>Observe la tabla de la sección 3 de esta lección.</em><br>¿Qué afirmación describe mejor en qué se diferencian los dos documentos?"),
   [t("They report different facts from the same meeting, and each leaves out the facts that hurt its side.", "Cuentan hechos distintos de la misma reunión, y cada uno omite los que perjudican a su lado."), t("They disagree about the date of the meeting.", "No coinciden en la fecha de la reunión."), t("One is a primary source and the other is secondary.", "Uno es fuente primaria y el otro secundaria."), t("One of them invented the vote.", "Uno de ellos inventó la votación.")], 0,
   {1: t("Both give the same dates.", "Los dos dan las mismas fechas."), 2: t("Both were written at the time: both are primary.", "Los dos se escribieron en su momento: los dos son primarios."), 3: t("Leaving out a fact is not inventing one.", "Omitir un hecho no es inventarlo.")},
   t("The difference is in selection, not in contradiction. That is the meaning of bias.", "La diferencia está en la selección, no en la contradicción. Eso es el sesgo."))}
{G(4, "SSP.5.a", "2", cita(t("“The tangible results of the meeting were two offers, made by the Chicago City Company.”", "«Los resultados tangibles de la reunión fueron dos ofrecimientos, hechos por la Chicago City Company»."), t("<cite>Street Railway Journal</cite>, a magazine read by streetcar companies, 1905", "<cite>Street Railway Journal</cite>, revista que leían las compañías de tranvías, 1905")) +
   t("Which word in this sentence best reveals the writer’s point of view?", "¿Qué palabra de esta frase revela mejor el punto de vista de quien escribe?"),
   [t("“tangible”", "«tangibles»"), t("“meeting”", "«reunión»"), t("“two”", "«dos»"), t("“Company”", "«Company»")], 0,
   {1: t("“Meeting” just names the event.", "«Reunión» solo nombra el suceso."), 2: t("“Two” is a number anyone can check.", "«Dos» es una cifra que cualquiera puede comprobar."), 3: t("It is part of a name.", "Es parte de un nombre.")},
   t("“Tangible” turns the offers into real achievements. A writer on the city’s side could have called them “two small offers” without saying anything false.", "«Tangibles» convierte los ofrecimientos en logros reales. Alguien del lado de la ciudad podría haberlos llamado «dos ofrecimientos menores» sin decir nada falso."))}"""

    secciones = [
        ("s1", t("Bias is not lying", "Sesgo no es mentira"), s1),
        ("s2", t("Two weeklies, one Friday", "Dos semanarios, un viernes"), s2),
        ("s3", t("The inventory of what is missing", "El inventario de lo que falta"), s3),
        ("s4", t("Four signals of persuasive language", "Cuatro señales de lenguaje persuasivo"), s4),
        ("s5", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("The inventory of omissions (25 minutes).", "El inventario de omisiones (25 minutos)."), t("Find two news stories from today about the same event, in two different media. Make a three-column table like the one in section 3: the fact, and one column for each medium. Write down ten facts. <em>Check:</em> if the omissions do not point in any direction, the two media may share the same point of view; look for another pair.",
                                                                                                      "Busque dos noticias de hoy sobre el mismo suceso, en dos medios distintos. Haga una tabla de tres columnas como la de la sección 3: el hecho y una columna por medio. Anote diez hechos. <em>Compruebe:</em> si las omisiones no apuntan en ninguna dirección, es probable que los dos medios compartan el punto de vista; busque otro par.")),
        (t("Rewrite without changing the facts (20 minutes).", "Reescribir sin cambiar los hechos (20 minutos)."), t("Take Fragment 1 of Document B and rewrite it from the opposite point of view, without adding, removing, or changing a single fact. You may only change words and order. <em>Check:</em> if you needed a new fact to get the effect, you went from bias to falsehood. Go back and do it with words only.",
                                                                                                              "Tome el Fragmento 1 del Documento B y reescríbalo desde el punto de vista contrario, sin añadir, quitar ni cambiar un solo hecho. Solo puede cambiar las palabras y el orden. <em>Compruebe:</em> si necesitó un dato nuevo para conseguir el efecto, pasó del sesgo a la falsedad. Vuelva atrás y hágalo solo con las palabras.")),
        (t("The two-source paragraph (30 minutes).", "El párrafo de las dos fuentes (30 minutos)."), t("Write a paragraph of 8 to 10 lines that answers: <em>What happened at the meeting of September 15, 1905?</em> Use both documents. Include at least one fact that appears only in each one, and point out one place where the language of a source seemed one-sided. <em>Check:</em> a supporter of the city and a supporter of the companies should both be able to read it without protesting.",
                                                                                                       "Escriba un párrafo de 8 a 10 líneas que responda: <em>¿Qué ocurrió en la reunión del 15 de septiembre de 1905?</em> Use los dos documentos. Incluya al menos un hecho que solo aparezca en cada uno, y señale un punto en el que el lenguaje de una fuente le pareció interesado. <em>Compruebe:</em> tanto un partidario de la ciudad como uno de las compañías deberían poder leerlo sin protestar.")),
    ]
    Q = t
    quiz = [
        (Q("A biased source is different from a false source because…", "Una fuente sesgada se distingue de una fuente falsa en que…"),
         [Q("the biased one states facts that did not happen", "la sesgada afirma hechos que no ocurrieron"), Q("the biased one states true facts, but not all of them, with words that push", "la sesgada afirma hechos ciertos, pero no todos, con palabras que empujan"), Q("there is no real difference", "no hay diferencia real"), Q("the biased one is always older", "la sesgada siempre es más antigua")], 1,
         {0: Q("That describes a false source.", "Eso describe una fuente falsa."), 2: Q("One is refuted, the other completed.", "Una se refuta; la otra se completa."), 3: Q("Age has nothing to do with it.", "La antigüedad no tiene nada que ver.")}, Q("Falsehood is refuted by checking; bias is completed by reading another source.", "La falsedad se refuta comprobando; el sesgo se completa leyendo otra fuente.")),
        (Q("Faced with a source that openly supports one side, the right move is to…", "Ante una fuente que defiende abiertamente una postura, lo correcto es…"),
         [Q("throw it away", "descartarla"), Q("use it for its facts and note its position as information about it", "usarla por sus hechos y anotar su postura como dato sobre ella"), Q("use it as if it were neutral", "usarla como si fuera neutral"), Q("use it only if there is nothing else", "usarla solo si no hay otra")], 1,
         {0: Q("Its facts may be good.", "Sus hechos pueden valer."), 2: Q("Its position matters.", "Su postura importa."), 3: Q("It is useful even when there are others.", "Es útil aunque haya otras.")}, Q("It is useful twice.", "Sirve dos veces.")),
        (Q("When all of a document’s omissions point the same way, that shows…", "Cuando todas las omisiones de un documento apuntan en la misma dirección, eso indica…"),
         [Q("that the writer was in a hurry", "que el autor tenía prisa"), Q("that the document is incomplete by accident", "que el documento está incompleto por accidente"), Q("its point of view", "su punto de vista"), Q("that it is false", "que es falso")], 2,
         {0: Q("Hurry would leave out things at random.", "La prisa dejaría fuera cosas al azar."), 1: Q("Accidents do not all favor one side.", "Los accidentes no favorecen todos a un lado."), 3: Q("Leaving out is not inventing.", "Omitir no es inventar.")}, Q("One omission can be chance; many in one direction are a decision.", "Una omisión puede ser casual; muchas en una dirección son una decisión.")),
        (Q("The two documents of this lesson were published…", "Los dos documentos de esta lección se publicaron…"),
         [Q("a year apart", "con un año de diferencia"), Q("on the same day, about the same meeting", "el mismo día, sobre la misma reunión"), Q("in the same newspaper", "en el mismo periódico"), Q("before the meeting took place", "antes de la reunión")], 1,
         {0: Q("Check the dates.", "Compruebe las fechas."), 2: Q("One was in Chicago, the other in New York.", "Uno era de Chicago y el otro de Nueva York."), 3: Q("Both report the meeting.", "Los dos informan de la reunión.")}, Q("Both are from September 23, 1905.", "Los dos son del 23 de septiembre de 1905.")),
        (Q("On which checkable fact do <em>The Public</em> and the <em>Street Railway Journal</em> contradict each other?", "¿En qué hecho comprobable se contradicen <em>The Public</em> y el <em>Street Railway Journal</em>?"),
         [Q("The date of the meeting", "La fecha de la reunión"), Q("The number of aldermen present", "El número de concejales presentes"), Q("None", "En ninguno"), Q("The name of the mayor", "El nombre del alcalde")], 2,
         {0: Q("Both say the 15th.", "Los dos dicen el 15."), 1: Q("Neither gives that number.", "Ninguno da esa cifra."), 3: Q("Only one of these fragments names the mayor.", "Solo uno de estos fragmentos nombra al alcalde.")}, Q("All the difference is in selection and language.", "Toda la diferencia está en la selección y el lenguaje.")),
        (Q("The <em>Street Railway Journal</em> does not mention the 7-to-5 vote or Bliss’s refusals. What can you conclude?", "El <em>Street Railway Journal</em> no menciona la votación de siete contra cinco ni las negativas de Bliss. ¿Qué se puede concluir?"),
         [Q("Its writer was not at the meeting", "Su redactor no asistió a la reunión"), Q("Those events did not happen", "Esos hechos no ocurrieron"), Q("It leaves out what hurt the companies, who were its readers", "Omite lo que perjudicaba a las compañías, que eran sus lectores"), Q("It did not cover Chicago", "No cubría Chicago")], 2,
         {0: Q("Nothing says that.", "Nada lo indica."), 1: Q("The other source records them.", "La otra fuente los registra."), 3: Q("This story is about Chicago.", "Esta nota es sobre Chicago.")}, Q("The omission fits the readers it served.", "La omisión encaja con el lector al que servía.")),
        (Q("Both documents say the committee met again on the 26th. Why does that matter?", "Los dos documentos dicen que el comité se volvió a reunir el 26. ¿Por qué importa?"),
         [Q("When two opposite sources agree on a detail, it deserves more trust", "Cuando dos fuentes opuestas coinciden en un detalle, ese detalle merece más confianza"), Q("It proves both are neutral", "Demuestra que los dos son neutrales"), Q("It proves both copied the minutes", "Demuestra que los dos copiaron el acta"), Q("It does not matter", "No importa")], 0,
         {1: Q("They agree on one fact; they are still one-sided.", "Coinciden en un hecho; siguen siendo parciales."), 2: Q("Nothing shows that.", "Nada lo demuestra."), 3: Q("It is the basis of corroboration.", "Es la base de la corroboración.")}, Q("Two opposite sources rarely agree by accident.", "Dos fuentes opuestas rara vez coinciden por casualidad.")),
        (Q("“The tangible results of the meeting were two offers.” The word “tangible”…", "«Los resultados tangibles de la reunión fueron dos ofrecimientos». La palabra «tangibles»…"),
         [Q("is a checkable fact", "es un hecho comprobable"), Q("is a judgment placed where the reader expects information", "es un juicio colocado donde el lector espera información"), Q("is a translation error", "es un error de traducción"), Q("does not change the meaning", "no cambia el sentido")], 1,
         {0: Q("Nobody can measure “tangible.”", "Nadie puede medir «tangible»."), 2: Q("It is in the original.", "Está en el original."), 3: Q("Try the sentence without it.", "Pruebe la frase sin ella.")}, Q("The adjective does the persuading.", "El adjetivo hace el trabajo de persuasión.")),
        (Q("One document names Col. Bliss in every refusal; the other only says “the company.” That contrast…", "Un documento nombra al coronel Bliss en cada negativa; el otro solo dice «la compañía». Ese contraste…"),
         [Q("does not matter to the reader", "es indiferente para el lector"), Q("makes the responsibility personal in one and dissolves it in the other", "personaliza la responsabilidad en uno y la disuelve en el otro"), Q("shows one writer did not know his name", "indica que uno no sabía su nombre"), Q("is just the style of the time", "es solo el estilo de la época")], 1,
         {0: Q("Names change how we judge.", "Los nombres cambian cómo juzgamos."), 2: Q("A trade magazine knew the industry’s spokesmen.", "Una revista del sector conocía a sus portavoces."), 3: Q("Both are from the same week.", "Los dos son de la misma semana.")}, Q("A face makes a refusal someone’s; no face makes it an institution’s.", "Un rostro hace de alguien la negativa; sin rostro, es de una institución.")),
        (Q("“They are understood to be bound by it.” The problem with this sentence is that it…", "«Se entiende que quedan obligados por él». El problema de esta frase es que…"),
         [Q("contains a false fact", "contiene un dato falso"), Q("presents an interpretation as common knowledge without saying who holds it", "presenta una interpretación como sabida, sin decir quién la sostiene"), Q("uses the wrong verb tense", "usa un tiempo verbal incorrecto"), Q("repeats earlier information", "repite información anterior")], 1,
         {0: Q("The silence did happen.", "El silencio sí ocurrió."), 2: Q("Grammar is not the issue.", "La gramática no es el problema."), 3: Q("It adds something new: an interpretation.", "Añade algo nuevo: una interpretación.")}, Q("The silence is the fact; “bound” is a reading of it.", "El silencio es el hecho; «obligados» es una lectura.")),
        (Q("Which statement is an <strong>opinion</strong>?", "¿Cuál de estas afirmaciones es una <strong>opinión</strong>?"),
         [Q("Mayor Dunne was elected in April 1905.", "El alcalde Dunne fue elegido en abril de 1905."), Q("Streetcars are the most beautiful way to travel.", "Los tranvías son la forma más bonita de viajar."), Q("The committee met on September 15.", "El comité se reunió el 15 de septiembre."), Q("The companies ran the lines with city franchises.", "Las compañías operaban las líneas con concesiones municipales.")], 1,
         {0: Q("An election date can be checked.", "La fecha de una elección se puede comprobar."), 2: Q("A meeting date can be checked.", "La fecha de una reunión se puede comprobar."), 3: Q("Franchises are on record.", "Las concesiones constan en registros.")}, Q("“Most beautiful” is a preference no evidence can settle.", "«La más bonita» es una preferencia que ninguna evidencia puede decidir.")),
        (Q("“Since the company would not name a date to sell, the meeting brought the city no closer to owning the lines.” This is…", "«Como la compañía no quiso fijar una fecha de venta, la reunión no acercó a la ciudad a ser dueña de las líneas». Esto es…"),
         [Q("a fact", "un hecho"), Q("an opinion with no evidence", "una opinión sin evidencia"), Q("a reasoned judgment: a conclusion built on evidence", "un juicio razonado: una conclusión construida con evidencia"), Q("a false statement", "una afirmación falsa")], 2,
         {0: Q("“No closer” is a conclusion, not something you can count.", "«No acercó» es una conclusión, no algo que se pueda contar."), 1: Q("It gives a reason based on what happened.", "Da una razón basada en lo que ocurrió."), 3: Q("The evidence fits it.", "La evidencia encaja.")}, Q("It starts from a fact (“would not name a date”) and reasons to a conclusion.", "Parte de un hecho («no quiso fijar una fecha») y razona hasta una conclusión.")),
    ]
    filas = [
        (t("Tell bias from falsehood", "Distingue el sesgo de la falsedad"), t("I separate the two, keep using the one-sided source for its facts, and say what would answer each: checking or completing.", "Separo las dos cosas, sigo usando la fuente parcial por sus hechos y digo qué respondería a cada una: comprobar o completar."), t("I know they differ, but I end up throwing the one-sided source away.", "Sé que no es lo mismo, pero acabo descartando la fuente parcial."), t("I treat every one-sided source as a lying source (<a href=\"#s1\">review section 1</a>).", "Trato toda fuente parcial como fuente que miente (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Find what a document leaves out", "Detecta lo que un documento calla"), t("I name specific omissions and show they all point the same way.", "Nombro omisiones concretas y muestro que todas apuntan en la misma dirección."), t("I notice something is missing but cannot say what.", "Noto que falta algo, pero no sé decir qué."), t("I only comment on what the document says (<a href=\"#s3\">review section 3</a>).", "Solo comento lo que el documento dice (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Spot persuasive language", "Identifica el lenguaje persuasivo"), t("I name the signal, quote the exact word, and can rewrite it in neutral words.", "Nombro la señal, cito la palabra exacta y sé reescribirla en palabras neutrales."), t("I spot judging adjectives but miss claims with no source and headlines.", "Reconozco los adjetivos que juzgan, pero no las atribuciones sin fuente ni los titulares."), t("I point to words that sound strong without saying why (<a href=\"#s4\">review section 4</a>).", "Señalo palabras que suenan fuertes sin explicar por qué (<a href=\"#s4\">repase la sección 4</a>).")),
        (t("Rebuild events from two sources", "Reconstruye los hechos con dos fuentes"), t("I take facts from both in my own neutral words, and say what is still unknown.", "Tomo hechos de las dos con mis propias palabras neutrales, y digo qué sigue sin saberse."), t("I use both but repeat the judging words of one.", "Uso las dos, pero repito las palabras que juzgan de una de ellas."), t("I pick one and drop the other (<a href=\"#s3\">review section 3</a>).", "Elijo una y desecho la otra (<a href=\"#s3\">repase la sección 3</a>).")),
    ]
    cierre = "<p>" + t("This lesson set up the third tool, and with it Topic 1 ends. The first lesson taught you to ask; the second, to question a document; this one, to read two at once.",
                         "Esta lección deja instalada la tercera herramienta, y con ella se cierra el Tema 1. La primera lección enseñó a preguntar; la segunda, a interrogar un documento; esta, a leer dos a la vez.") + "</p><p>" + \
             t("The main thing to take away: the two weeklies of 1905 did not contradict each other once. Each told true facts. The whole difference was in which facts to tell and with which words. That is why bias is not fought by throwing sources away, but by adding them up.",
               "Lo que hay que llevarse es esto: los dos semanarios de 1905 no se contradijeron ni una sola vez. Cada uno contó hechos verdaderos. La diferencia entera estuvo en cuáles contar y con qué palabras. Por eso el sesgo no se combate descartando fuentes, sino sumándolas.") + "</p><p>" + \
             t("Topic 2 changes the kind of source: instead of words, numbers. Graphs, tables, averages, and percents can also be one-sided, and the same questions (who made it, what for, what it leaves out) will work on them.",
               "El Tema 2 cambia el tipo de fuente: en lugar de palabras, números. Las gráficas, las tablas, los promedios y los porcentajes también pueden ser parciales, y las mismas preguntas (quién lo hizo, para qué, qué deja fuera) servirán con ellos.") + "</p>"
    glosario = [
        (t("Bias", "Sesgo"), t("A one-sided way of telling true facts: choosing some, leaving out others, and using words that push toward a conclusion.", "Forma parcial de contar hechos verdaderos: elegir unos, callar otros y usar palabras que empujan hacia una conclusión.")),
        (t("Point of view", "Punto de vista"), t("The position from which a source looks at events, shown by what it tells and how.", "Posición desde la que una fuente mira los hechos; se nota en lo que cuenta y en cómo lo cuenta.")),
        (t("Propaganda", "Propaganda"), t("A message made to persuade many people, often by a government or a movement.", "Mensaje hecho para persuadir a mucha gente, a menudo de un gobierno o de un movimiento.")),
        (t("Loaded language", "Lenguaje cargado"), t("Words that carry a judgment (“tangible,” “greedy,” “progress”) where a neutral word could be used.", "Palabras que llevan un juicio («tangible», «codicioso», «avance») donde podría ir una palabra neutral.")),
        (t("Fact, opinion, reasoned judgment", "Hecho, opinión, juicio razonado"), t("A fact can be checked; an opinion is a preference; a reasoned judgment is a conclusion built on evidence.", "Un hecho se puede comprobar; una opinión es una preferencia; un juicio razonado es una conclusión construida con evidencia.")),
        (t("Franchise", "Concesión"), t("Permission from a government for a private company to run a public service, like streetcars.", "Permiso de un gobierno para que una empresa privada preste un servicio público, como los tranvías.")),
        (t("Alderman", "Concejal"), t("A member of the Chicago City Council, elected by a ward.", "Miembro del Concejo Municipal de Chicago, elegido por un distrito.")),
    ]
    estd = C.estandares(["SSP.5.a", "SSP.5.b", "SSP.7.a", "SSP.8.a"], [], base=["SSP.4.a", "SSP.5.d"])
    conexion = "<p>" + t("Lesson 1.2 taught you to question a document on its own: origin, purpose, and context, and then decide what it supports. The two documents there did not contradict each other. They completed each other.",
                         "La Lección 1.2 enseñó a interrogar un documento a solas: origen, propósito y contexto, y después decidir qué sostiene. Los dos documentos de allí no se contradecían. Se completaban.") + "</p><p>" + \
               t("Here something else happens. Two weeklies came out on the same day, Saturday, September 23, 1905. Both tell about the same meeting, held on Friday the 15th in the Chicago City Council. Both are primary sources. Neither lies. And yet they seem to describe two different meetings. Finding out how that can happen is the whole lesson.",
                 "Aquí ocurre otra cosa. Dos semanarios salieron el mismo día, el sábado 23 de septiembre de 1905. Los dos cuentan la misma reunión, celebrada el viernes 15 en el Concejo Municipal de Chicago. Los dos son fuentes primarias. Ninguno miente. Y sin embargo parecen dos reuniones distintas. Averiguar cómo puede pasar eso es toda la lección.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("A source can be one-sided without telling a single lie. The bias is in what it chooses to tell, and in its words.", "Una fuente puede ser parcial sin decir una sola mentira. El sesgo está en lo que decide contar, y en sus palabras."),
        ["SSP.5 · " + t("Point of view and bias", "Punto de vista y sesgo"), "SSP.7 · " + t("Fact and opinion", "Hecho y opinión"), "SSP.8 · " + t("Comparing sources", "Comparar fuentes")],
        [t("<strong>Tell apart</strong> bias from falsehood, and recognize that a source can be one-sided without telling a single lie.", "<strong>Distinguir</strong> el sesgo de la falsedad, y reconocer que una fuente puede ser parcial sin decir una sola mentira."),
         t("<strong>Detect</strong> a document’s point of view through its words, whom it names, and to whom it attributes what it claims.", "<strong>Detectar</strong> el punto de vista de un documento por sus palabras, por a quién nombra y por a quién atribuye lo que afirma."),
         t("<strong>Find</strong> what a document leaves out by comparing it with another about the same events.", "<strong>Descubrir</strong> lo que un documento calla, comparándolo con otro sobre los mismos hechos."),
         t("<strong>Use</strong> two one-sided sources to rebuild what happened, and sort statements into fact, opinion, and reasoned judgment.", "<strong>Usar</strong> dos fuentes parciales para reconstruir lo ocurrido, y clasificar afirmaciones en hecho, opinión y juicio razonado.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        (None, t("Next: Topic 2 · Quantitative reasoning in social studies.", "Siguiente: Tema 2 · Razonamiento cuantitativo en estudios sociales.")), glosario, P)


# ---------------------------------------------------------------- la práctica
def banco_falso():
    FAL, SES, NIN = t("Falsehood", "Falsedad"), t("Bias", "Sesgo"), t("Neither: it is accurate and balanced", "Ninguna: es exacto y equilibrado")
    datos = [
        (t("A website says the Civil War ended in 1875.", "Un sitio web dice que la Guerra Civil terminó en 1875."), 0, t("It ended in 1865. A fact that can be checked, and it is wrong.", "Terminó en 1865. Un hecho comprobable, y es incorrecto.")),
        (t("A union newsletter reports a strike by quoting only the workers, and calls the company’s offer “an insult.”", "Un boletín sindical informa de una huelga citando solo a los trabajadores, y llama «un insulto» a la oferta de la empresa."), 1, t("The facts may be true, but only one side speaks and a loaded word judges the offer.", "Los hechos pueden ser ciertos, pero solo habla un lado y una palabra cargada juzga la oferta.")),
        (t("A company press release about the same strike quotes only managers and calls the workers’ demands “unrealistic.”", "Un comunicado de la empresa sobre la misma huelga cita solo a los directivos y llama «poco realistas» a las demandas de los trabajadores."), 1, t("The mirror image of the union newsletter: true facts, one side, loaded words.", "La imagen en espejo del boletín sindical: hechos ciertos, un solo lado, palabras cargadas.")),
        (t("A report says the city budget was $16 billion when the approved budget says $16.6 billion, and the report rounded.", "Un informe dice que el presupuesto municipal fue de 16 000 millones cuando el aprobado dice 16 600 millones, y el informe redondeó."), 2, t("Rounding with a clear number is not lying or bias, as long as it does not change the conclusion.", "Redondear con una cifra clara no es mentir ni sesgar, siempre que no cambie la conclusión.")),
        (t("A campaign ad says the opponent “voted against schools,” about a vote on a bill that cut school funds and also raised a tax.", "Un anuncio de campaña dice que el rival «votó contra las escuelas», sobre una votación de un proyecto que recortaba fondos escolares y además subía un impuesto."), 1, t("The vote happened, but the ad tells only the part that hurts the opponent.", "La votación ocurrió, pero el anuncio cuenta solo la parte que perjudica al rival.")),
        (t("A flyer says a candidate was born in another country, but her birth certificate says Chicago.", "Un volante dice que una candidata nació en otro país, pero su acta de nacimiento dice Chicago."), 0, t("A checkable fact, and the record shows it is false.", "Un hecho comprobable, y el registro muestra que es falso.")),
        (t("A news story gives the vote count, quotes one supporter and one opponent, and describes the law in plain words.", "Una noticia da el resultado de la votación, cita a un partidario y a un opositor, y describe la ley con palabras sencillas."), 2, t("Both sides speak and the words are neutral.", "Hablan los dos lados y las palabras son neutrales.")),
        (t("A magazine paid by car companies reports a new highway as “a victory for every driver” and does not mention the homes torn down to build it.", "Una revista pagada por fabricantes de autos presenta una nueva autopista como «una victoria para todos los conductores» y no menciona las casas derribadas para construirla."), 1, t("A loaded phrase and an omission that both favor its sponsors.", "Una frase cargada y una omisión que favorecen a quienes la pagan.")),
    ]
    ops = [FAL, SES, NIN]
    return [{"enun": t("Is the problem falsehood, bias, or neither?", "¿El problema es falsedad, sesgo o ninguna de las dos?") + "<br><strong>" + s + "</strong>",
             "ops": ops, "ok": k, "exp": f"<strong>{ops[k]}.</strong> " + e, "enOrden": True} for s, k, e in datos]


def casos_inventario():
    G = [t("Only in report A", "Solo en la crónica A"), t("Only in report B", "Solo en la crónica B"), t("In both reports", "En las dos crónicas")]
    PA = t("Read report A again: is it there? Now look for it in B.", "Vuelva a leer la crónica A: ¿está ahí? Ahora búsquelo en la B.")
    PB = t("Read report B again: is it there? Now look for it in A.", "Vuelva a leer la crónica B: ¿está ahí? Ahora búsquelo en la A.")
    PZ = t("Check both reports: some facts appear in each one, with different words.", "Revise las dos crónicas: algunos hechos aparecen en cada una, con palabras distintas.")
    def caso(tit, a, b, piezas, extra):
        return {"titulo": tit, "intro": f'<span style="display:block;margin:6px 0"><strong>A:</strong> {a}</span><span style="display:block;margin:6px 0"><strong>B:</strong> {b}</span>' + t("Where does each fact appear?", "¿Dónde aparece cada hecho?"),
                "grupos": G, "etiqueta": t("This fact appears…", "Este hecho aparece…"), "piezas": [{"t": x, "v": v, "pista": [PA, PB, PZ][v]} for x, v in piezas], "extra": extra}
    return [
        caso(t("Case 1 · The streetcar meeting, 1905", "Caso 1 · La reunión tranviaria, 1905"),
             t("<em>The Public</em> (pro-city weekly).", "<em>The Public</em> (semanario a favor de la ciudad)."), t("<em>Street Railway Journal</em> (streetcar-industry magazine).", "<em>Street Railway Journal</em> (revista del sector tranviario)."),
             [(t("The committee met on September 15.", "El comité se reunió el 15 de septiembre."), 2), (t("Bliss said “We will not.”", "Bliss dijo «No accederemos»."), 0),
              (t("The Chicago City Company made two offers.", "La Chicago City Company hizo dos ofrecimientos."), 1), (t("The vote was seven to five.", "La votación fue siete contra cinco."), 0),
              (t("The next meeting was set for the 26th.", "La siguiente reunión se fijó para el 26."), 2), (t("Union Traction sat silent.", "La Union Traction guardó silencio."), 1)],
             t(" A keeps what hurts the companies; B keeps what helps them. The shared facts are the ones you can trust most.", " A conserva lo que perjudica a las compañías; B, lo que las favorece. Los hechos compartidos son los que más confianza merecen.")),
        caso(t("Case 2 · A school board vote (practice example)", "Caso 2 · Una votación de la junta escolar (ejemplo de práctica)"),
             t("“Parents packed the board room Tuesday night as the board voted 4–3 to close Lincoln Elementary. Twenty-two parents spoke against the closing; none spoke in favor. Families will now travel up to two miles to the nearest school.”", "«Los padres llenaron la sala de la junta el martes por la noche cuando la junta votó 4 a 3 cerrar la escuela primaria Lincoln. Veintidós padres hablaron en contra del cierre; ninguno a favor. Las familias tendrán que viajar ahora hasta dos millas a la escuela más cercana»."),
             t("“On Tuesday the board voted 4–3 to close Lincoln Elementary, which was using only 40% of its seats. The closing will save $1.2 million a year, which the board says will pay for new reading teachers.”", "«El martes la junta votó 4 a 3 cerrar la escuela primaria Lincoln, que solo usaba el 40 % de sus plazas. El cierre ahorrará 1.2 millones de dólares al año, que según la junta pagarán nuevos maestros de lectura»."),
             [(t("The vote was 4–3.", "La votación fue 4 a 3."), 2), (t("Twenty-two parents spoke against the closing.", "Veintidós padres hablaron en contra del cierre."), 0),
              (t("The school was using only 40% of its seats.", "La escuela solo usaba el 40 % de sus plazas."), 1), (t("The closing will save $1.2 million a year.", "El cierre ahorrará 1.2 millones de dólares al año."), 1),
              (t("Some families will travel up to two miles.", "Algunas familias viajarán hasta dos millas."), 0), (t("The vote was on Tuesday.", "La votación fue el martes."), 2)],
             t(" Report A tells the cost to families; report B tells the cost to the budget. A careful reader needs both to answer the compelling question of Lesson 1.1: cost or access?", " La crónica A cuenta el costo para las familias; la B, el costo para el presupuesto. Un lector cuidadoso necesita las dos para responder la pregunta convincente de la Lección 1.1: ¿costo o acceso?")),
    ]


def banco_senal():
    S = [t("A judging word in place of a fact", "Una palabra que juzga en lugar de un hecho"), t("Who is named and who is not", "A quién se nombra y a quién no"), t("A claim with no source", "Una atribución sin fuente"), t("The headline as a frame", "El titular como marco")]
    pist = {0: t("Is there an adjective or noun that judges, where a neutral word could go?", "¿Hay un adjetivo o un sustantivo que juzga, donde podría ir una palabra neutral?"),
            1: t("Does the text give a face to one side and leave the other faceless?", "¿El texto pone rostro a un lado y deja sin rostro al otro?"),
            2: t("Does it say “it is believed” or “many say” without saying who?", "¿Dice «se cree» o «muchos dicen» sin decir quién?"),
            3: t("Is it the title, telling you how to read what follows?", "¿Es el título, que le dice cómo leer lo que sigue?")}
    datos = [
        (t("“Experts agree the plan will fail.” (No expert is named.)", "«Los expertos coinciden en que el plan fracasará». (No se nombra a ningún experto)."), 2),
        (t("Headline: “Mayor’s Reckless Spending Spree Continues,” over a story about the approved budget.", "Titular: «Continúa el derroche irresponsable del alcalde», sobre una nota acerca del presupuesto aprobado."), 3),
        (t("“The senator’s so-called reform bill passed on Monday.”", "«El llamado proyecto de reforma del senador se aprobó el lunes»."), 0),
        (t("“Officer Daniel Reyes stopped the car. The driver was released.” (The driver is never named.)", "«El agente Daniel Reyes detuvo el auto. El conductor fue liberado». (Al conductor nunca se le nombra)."), 1),
        (t("“It is widely believed that the new law hurts small farms.”", "«Se cree ampliamente que la nueva ley perjudica a las pequeñas granjas»."), 2),
        (t("“The council’s heroic decision saved the park.”", "«La heroica decisión del concejo salvó el parque»."), 0),
        (t("Headline: “Victory for Taxpayers,” over a story that says a tax was lowered by 0.1%.", "Titular: «Victoria para los contribuyentes», sobre una nota que dice que un impuesto bajó un 0.1 %."), 3),
        (t("A story about a factory closing quotes the CEO by name and refers to the workers only as “the employees.”", "Una nota sobre el cierre de una fábrica cita al director por su nombre y se refiere a los trabajadores solo como «los empleados»."), 1),
    ]
    return [{"enun": t("Which signal of persuasive language is this?", "¿Qué señal de lenguaje persuasivo es esta?") + "<br><strong>" + s + "</strong>",
             "ops": S, "ok": k, "pistas": {i: pist[k] for i in range(4) if i != k}, "exp": f"<strong>{S[k]}.</strong>", "enOrden": True} for s, k in datos]


def banco_neutral():
    datos = [
        (t("“The greedy landlord jacked up the rent again.”", "«El codicioso casero volvió a disparar el alquiler»."),
         [t("The landlord raised the rent by $150 a month, the second increase this year.", "El casero subió el alquiler 150 dólares al mes, la segunda subida de este año."), t("The landlord raised the rent, as greedy landlords always do.", "El casero subió el alquiler, como siempre hacen los caseros codiciosos."), t("The landlord generously kept the rent almost the same.", "El casero, generoso, dejó el alquiler casi igual.")],
         t("The neutral version replaces “greedy” and “jacked up” with checkable facts: the amount and how often.", "La versión neutral cambia «codicioso» y «disparar» por hechos comprobables: la cantidad y la frecuencia.")),
        (t("“The mob of protesters swarmed City Hall.”", "«La turba de manifestantes invadió el ayuntamiento»."),
         [t("About 300 protesters gathered outside City Hall.", "Unos 300 manifestantes se reunieron frente al ayuntamiento."), t("A crowd of brave citizens defended their rights at City Hall.", "Una multitud de ciudadanos valientes defendió sus derechos en el ayuntamiento."), t("Dangerous protesters attacked City Hall.", "Manifestantes peligrosos atacaron el ayuntamiento.")],
         t("“Mob” and “swarmed” judge; “brave” judges the other way. A number and a plain verb do not.", "«Turba» e «invadió» juzgan; «valientes» juzga hacia el otro lado. Una cifra y un verbo sencillo no.")),
        (t("“The company finally admitted its tiny wage increase.”", "«La empresa finalmente admitió su miserable aumento salarial»."),
         [t("The company announced a 2% wage increase.", "La empresa anunció un aumento salarial del 2 %."), t("The company proudly gave workers a big raise.", "La empresa, orgullosa, dio a los trabajadores un gran aumento."), t("The company was forced to admit a tiny raise.", "La empresa se vio obligada a admitir un aumento miserable.")],
         t("“Finally admitted” suggests guilt and “tiny” judges the amount; the neutral version gives the percent and lets the reader judge.", "«Finalmente admitió» sugiere culpa y «miserable» juzga la cantidad; la versión neutral da el porcentaje y deja que el lector juzgue.")),
        (t("“The mayor’s wasteful plan will cost taxpayers a fortune.”", "«El despilfarrador plan del alcalde costará una fortuna a los contribuyentes»."),
         [t("The mayor’s plan would cost an estimated $40 million over five years.", "El plan del alcalde costaría unos 40 millones de dólares en cinco años, según las estimaciones."), t("The mayor’s smart plan is a bargain at any price.", "El inteligente plan del alcalde es una ganga a cualquier precio."), t("Experts say the plan is wasteful.", "Los expertos dicen que el plan es un despilfarro.")],
         t("The third option hides the judgment behind “experts say” with no source. Only the first gives a checkable number.", "La tercera opción esconde el juicio tras «los expertos dicen», sin fuente. Solo la primera da una cifra comprobable.")),
        (t("“Hordes of migrants are flooding into the city.”", "«Hordas de migrantes están inundando la ciudad»."),
         [t("About 12,000 migrants arrived in the city between May and August.", "Unos 12 000 migrantes llegaron a la ciudad entre mayo y agosto."), t("Thousands of desperate migrants are pouring in.", "Miles de migrantes desesperados están llegando en masa."), t("The city is being invaded by migrants.", "La ciudad está siendo invadida por migrantes.")],
         t("“Hordes,” “flooding,” “pouring,” and “invaded” turn people into a disaster. A number and a period of time describe the same event without judging it.", "«Hordas», «inundando», «en masa» e «invadida» convierten a personas en un desastre. Una cifra y un período describen el mismo hecho sin juzgarlo.")),
    ]
    return [{"enun": t("This sentence uses loaded language:", "Esta frase usa lenguaje cargado:") + " <strong>" + s + "</strong><br>" + t("Which version is <strong>neutral</strong>?", "¿Qué versión es <strong>neutral</strong>?"),
             "ops": ops, "ok": 0, "pistas": {1: t("Look for words that judge: does this version still have some?", "Busque palabras que juzgan: ¿esta versión todavía tiene alguna?"), 2: t("Does this version still judge, or hide a judgment behind someone else?", "¿Esta versión sigue juzgando, o esconde un juicio detrás de otro?")}, "exp": e} for s, ops, e in datos]


def banco_hecho():
    H, O, J = t("Fact", "Hecho"), t("Opinion", "Opinión"), t("Reasoned judgment", "Juicio razonado")
    pist = {0: t("Could you check it in a record, a count, or a document?", "¿Se podría comprobar en un registro, un conteo o un documento?"),
            1: t("Is it a preference or a feeling that no evidence could settle?", "¿Es una preferencia o un sentimiento que ninguna evidencia podría decidir?"),
            2: t("Does it reach a conclusion and give evidence for it, even if someone could disagree?", "¿Llega a una conclusión y da evidencia para ella, aunque alguien pudiera discrepar?")}
    datos = [
        (t("The Nineteenth Amendment was ratified in 1920.", "La Decimonovena Enmienda se ratificó en 1920."), 0),
        (t("Chicago is the most exciting city in America.", "Chicago es la ciudad más emocionante de los Estados Unidos."), 1),
        (t("Because rents rose 30% while wages rose 10%, housing became harder to afford for many workers.", "Como los alquileres subieron un 30 % mientras los salarios subían un 10 %, la vivienda se volvió más difícil de pagar para muchos trabajadores."), 2),
        (t("The Senate has 100 members.", "El Senado tiene 100 miembros."), 0),
        (t("The 1905 meeting was boring.", "La reunión de 1905 fue aburrida."), 1),
        (t("Since the census shows the Black population of Chicago grew more than five times from 1910 to 1930, the Great Migration changed the city deeply.", "Como el censo muestra que la población negra de Chicago se multiplicó por más de cinco entre 1910 y 1930, la Gran Migración cambió profundamente la ciudad."), 2),
        (t("Hull-House opened in 1889.", "La Casa Hull abrió en 1889."), 0),
        (t("Jane Addams was the most admirable woman of her time.", "Jane Addams fue la mujer más admirable de su época."), 1),
        (t("Given that both opposite weeklies report the same date, the meeting almost certainly took place on September 15.", "Dado que los dos semanarios opuestos dan la misma fecha, la reunión casi con seguridad se celebró el 15 de septiembre."), 2),
    ]
    ops = [H, O, J]
    return [{"enun": t("Is this a fact, an opinion, or a reasoned judgment?", "¿Es un hecho, una opinión o un juicio razonado?") + "<br><strong>" + s + "</strong>",
             "ops": ops, "ok": k, "pistas": {i: pist[k] for i in range(3) if i != k}, "exp": f"<strong>{ops[k]}.</strong>", "enOrden": True} for s, k in datos]


def practica():
    A = {"en": ["false", "inventory", "signals", "neutral", "fact"], "es": ["falso", "inventario", "senales", "neutral", "hecho"]}[C.L]
    mods = [
        (A[0], t("False or biased?", "¿Falso o sesgado?"),
         C.om("m1", t("A false source states facts that did not happen. A biased source tells true facts, but not all of them, with words that push. Some sources are neither.", "Una fuente falsa afirma hechos que no ocurrieron. Una fuente sesgada cuenta hechos ciertos, pero no todos, con palabras que empujan. Algunas fuentes no son ni lo uno ni lo otro."))),
        (A[1], t("The inventory of what is missing", "El inventario de lo que falta"),
         C.clasifica("m2", t("Read the two reports. Then decide where each fact appears: only in A, only in B, or in both. If something is not right, the facts marked in yellow get a hint.", "Lea las dos crónicas. Después decida dónde aparece cada hecho: solo en A, solo en B o en las dos. Si algo no está bien, los hechos marcados en amarillo reciben una pista."))),
        (A[2], t("Name the signal", "Identifique la señal"),
         C.om("m3", t("The four signals: a judging word in place of a fact, who is named and who is not, a claim with no source, and the headline as a frame.", "Las cuatro señales: una palabra que juzga en lugar de un hecho, a quién se nombra y a quién no, una atribución sin fuente y el titular como marco."))),
        (A[3], t("Say it neutrally", "Dígalo de forma neutral"),
         C.om("m4", t("Each sentence uses loaded language. Choose the version that tells the same event without judging it.", "Cada frase usa lenguaje cargado. Elija la versión que cuenta el mismo hecho sin juzgarlo."))),
        (A[4], t("Fact, opinion, or reasoned judgment?", "¿Hecho, opinión o juicio razonado?"),
         C.om("m5", t("A fact can be checked. An opinion is a preference. A reasoned judgment is a conclusion with evidence behind it.", "Un hecho se puede comprobar. Una opinión es una preferencia. Un juicio razonado es una conclusión con evidencia detrás."))),
    ]
    js = (C.js_datos("FALSO", banco_falso()) + C.js_datos("INV", casos_inventario()) + C.js_datos("SEN", banco_senal()) +
          C.js_datos("NEU", banco_neutral()) + C.js_datos("HEC", banco_hecho()) +
          'creaBanco("m1", FALSO);\ncreaClasifica("m2", INV);\ncreaBanco("m3", SEN);\ncreaBanco("m4", NEU);\ncreaBanco("m5", HEC);\n')
    return C.pagina_practica(N, titulo(), t("Five activities · the order of the exercises changes every time · two tries in each one", "Cinco actividades · el orden de los ejercicios cambia cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
