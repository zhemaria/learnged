# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 4.2 · Estructura de la historia y propósito del autor.
Fuente: clases_leng2/clase_4-2.html (GEDparaHispanos) y gramatica/n2-l4-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_4_2.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "4-2"
PARTES = ["Inicio", "Desarrollo", "Desenlace"]
PROP = ["Informar", "Entretener", "Persuadir"]
HIST = [("La fiesta sorpresa", ["Ana decidió organizar una fiesta sorpresa para su madre.", "Llamó en secreto a toda la familia.", "El sábado por la mañana compraron el pastel y los globos.", "Mientras su madre estaba en el mercado, decoraron la sala.", "Cuando ella abrió la puerta, todos gritaron: «¡Sorpresa!»."]),
        ("La llanta ponchada", ["Pedro salió temprano hacia el trabajo.", "A mitad del camino, oyó un ruido extraño en el carro.", "Se detuvo y vio que tenía una llanta ponchada.", "Llamó a su hermano, que llegó con una llanta de repuesto.", "Entre los dos la cambiaron y Pedro llegó solo media hora tarde."]),
        ("El huerto de la escuela", ["Los estudiantes querían un huerto en la escuela.", "Primero pidieron permiso a la directora.", "Después, los padres donaron tierra y semillas.", "Durante la primavera regaron las plantas todos los días.", "Al final del curso cosecharon tomates y los repartieron entre las familias."]),
        ("El examen de manejo", ["Rosa practicó con su tío todos los domingos.", "Una semana antes, estudió el manual de tránsito.", "El día del examen, estaba muy nerviosa.", "Respiró hondo y manejó con mucho cuidado.", "Al terminar, el examinador le dijo que había aprobado."]),
        ("El perro perdido", ["Una tarde de tormenta, el perro de la familia Gómez se escapó.", "Los niños lo buscaron por todo el barrio sin encontrarlo.", "Entonces pusieron carteles con su foto en las tiendas.", "Al día siguiente, una vecina llamó: lo tenía en su garaje.", "Los niños corrieron a buscarlo y desde entonces revisan bien la puerta."]),
        ("La receta de la abuela", ["Luis quería cocinar el mole de su abuela.", "Primero la llamó por teléfono para pedirle la receta.", "Luego fue al mercado a comprar los chiles y el chocolate.", "Pasó toda la tarde cocinando.", "Por la noche, la familia dijo que sabía igual que el de la abuela."])]
EN_PARTE = [("La fiesta sorpresa", "Ana vive con su madre, que pronto cumplirá cincuenta años.", 0, "Presenta a los personajes y la situación."),
            ("La fiesta sorpresa", "La madre llega a casa una hora antes de lo planeado.", 1, "Es una complicación: aparece el problema."),
            ("La fiesta sorpresa", "La madre llora de alegría al ver a toda la familia reunida.", 2, "Así termina la historia."),
            ("La llanta ponchada", "Pedro trabaja en una fábrica al otro lado de la ciudad.", 0, "Presenta al personaje y su situación."),
            ("La llanta ponchada", "En la autopista, el carro empieza a hacer un ruido extraño.", 1, "Empieza el problema."),
            ("La llanta ponchada", "Pedro llega al trabajo y su jefe le agradece por avisar.", 2, "El problema ya se resolvió."),
            ("El perro perdido", "La familia Gómez tiene un perro llamado Canela desde hace seis años.", 0, "Personajes y situación inicial."),
            ("El perro perdido", "Pasan dos días y nadie llama por los carteles.", 1, "La tensión sube: el problema sigue sin resolverse."),
            ("El perro perdido", "Canela vuelve a dormir en su rincón, junto a la estufa.", 2, "Todo vuelve a la normalidad: desenlace."),
            ("El examen de manejo", "Rosa quiere sacar su licencia para llevar a sus hijos a la escuela.", 0, "Presenta al personaje y lo que quiere."),
            ("El examen de manejo", "En el examen, un carro se le cruza y Rosa debe frenar de golpe.", 1, "El momento de mayor tensión."),
            ("El examen de manejo", "Esa tarde, Rosa lleva a sus hijos a tomar un helado en su propio carro.", 2, "El final feliz.")]
PROPOSITOS = [("La farmacia de la esquina abre todos los días de 8 a 10. Los domingos cierra a las 6.", 0, "Solo da datos: horarios."),
              ("¡Los mejores tacos de la ciudad están aquí! Ven hoy y el segundo taco es gratis.", 2, "«Los mejores», una orden y una oferta."),
              ("Cuando el gallo de don Chema empezó a cantar a medianoche, todo el pueblo se despertó asustado.", 1, "Un personaje y una situación divertida."),
              ("Para renovar la licencia, lleve su identificación, un comprobante de domicilio y el pago de la tarifa.", 0, "Explica qué hay que hacer."),
              ("Si quieres un barrio más seguro, ven a la reunión de vecinos del martes. ¡Tu voz cuenta!", 2, "Quiere que el lector actúe."),
              ("Esa noche, la luna era tan grande que Marta pensó que se iba a caer sobre la casa.", 1, "Narra con imaginación."),
              ("El lago Míchigan es uno de los cinco Grandes Lagos de América del Norte.", 0, "Un dato geográfico."),
              ("No pierdas más tiempo en el tráfico: compra tu bicicleta eléctrica y llega siempre a tiempo.", 2, "Una orden y un beneficio para convencer."),
              ("El abuelo se sentó, se acomodó el sombrero y dijo: —Les voy a contar cómo conocí a su abuela.", 1, "Un personaje que empieza a contar una historia."),
              ("Las vacunas contra la gripe se aplican cada año, preferiblemente en otoño.", 0, "Información sobre salud, sin opiniones."),
              ("Todos deberíamos reciclar: es fácil, es gratis y protege el planeta de nuestros hijos.", 2, "«Deberíamos» y razones para convencer."),
              ("Un ratón entró en la panadería y, al ver tanto pan, no supo por dónde empezar.", 1, "Una historia con un personaje.")]
MARISOL = ["Marisol llevaba tres meses buscando trabajo. Había enviado su solicitud a muchas tiendas del barrio, pero nadie la llamaba. Una mañana de lunes, por fin, sonó el teléfono: una clínica la citaba para una entrevista el jueves a las nueve.",
           "Marisol se preparó con cuidado. Planchó su mejor blusa, buscó información sobre la clínica y practicó sus respuestas frente al espejo. El jueves salió de casa una hora antes.",
           "Pero en la parada, el autobús no llegaba. Pasaron diez minutos, luego veinte. Marisol miraba el reloj con angustia: si seguía esperando, llegaría tarde. Entonces recordó que la clínica quedaba a solo quince cuadras. Respiró hondo y empezó a caminar rápido.",
           "Llegó a las nueve menos cinco, un poco cansada, pero a tiempo. La entrevistadora le preguntó por qué quería ese trabajo, y Marisol le habló de los años en que cuidó a su abuela enferma. Al final, la señora sonrió y le dijo:",
           "—Me gusta su actitud. Cuando hay un problema, usted busca una solución. ¿Puede empezar el lunes?",
           "Esa noche, Marisol celebró con su familia. El trabajo era nuevo, pero la lección ya la conocía: cuando el autobús no llega, hay que caminar."]
P1 = "«El jueves se inaugura la nueva biblioteca del barrio, en la calle 26. Tendrá 40 computadoras, una sala para niños y clases gratuitas de inglés. Abrirá de 9 a 8, de lunes a sábado.»"
P2 = "«¿Todavía no sabes nadar? ¡Nunca es tarde! En nuestra academia aprenderás en solo diez clases, con los mejores instructores. Inscríbete esta semana y la primera clase es gratis.»"


def pasaje(t):
    return f'<div class="texto-lectura"><p>{t}</p></div>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la Lección 4.1 aprendió a encontrar la idea principal. Pero no todos los textos se leen igual: una historia no se organiza como una noticia, y un anuncio no busca lo mismo que una receta. Hoy aprenderá dos herramientas: el <strong>mapa de la historia</strong>, para entender cualquier relato, y la pregunta del <strong>propósito</strong>: ¿para qué escribió esto el autor? En el GED, esa pregunta aparece una y otra vez.</p>
<p>Casi todas las historias, desde un cuento infantil hasta una película, tienen tres partes:</p>
{C.tabla("El mapa de la historia", ["Parte", "Qué contiene"],
         [["1 · Inicio", "<strong>Personajes</strong>: quiénes participan. <strong>Escenario</strong>: dónde y cuándo ocurre. <strong>Situación inicial</strong>: cómo están las cosas al empezar."],
          ["2 · Desarrollo", "<strong>Problema o conflicto</strong>: lo que se complica. <strong>Acciones</strong>: lo que hacen los personajes. <strong>Momento de mayor tensión</strong>: el punto en que todo se decide."],
          ["3 · Desenlace", "<strong>Solución</strong>: cómo termina el problema. A veces, una enseñanza o un cambio en el personaje."]])}
<p class="formula">La tensión <strong>sube</strong> durante el desarrollo, llega a su punto más alto y <strong>baja</strong> en el desenlace.</p>
{C.caja("tip", "La pregunta clave es el problema", "<p>Si encuentra el problema, encuentra la historia. Pregúntese: ¿qué quiere el personaje? ¿Qué se lo impide? Todo lo demás gira alrededor de eso.</p>")}
<p>Estos hechos son de una historia sobre una familia que se muda. ¿En qué parte va cada uno?</p>
{P("Compruebe", "«La familia Ortiz vive en un apartamento pequeño de Pilsen con sus tres hijos.»", PARTES, 0, {1: "Todavía no hay ningún problema.", 2: "No resuelve nada: presenta."}, "<strong>Inicio</strong>: presenta a los personajes y el escenario.")}
{P("Compruebe", "«El dueño les avisa que deben dejar el apartamento en un mes.»", PARTES, 1, {0: "Aquí aparece una complicación.", 2: "No se resuelve nada todavía."}, "<strong>Desarrollo</strong>: aparece el problema.")}
{P("Compruebe", "«Faltando dos días, una vecina les cuenta que su hermano alquila una casa.»", PARTES, 1, {0: "La historia ya empezó hace rato.", 2: "Todavía no se han mudado."}, "<strong>Desarrollo</strong>: es el momento de mayor tensión, cuando todo se decide.")}
{P("Compruebe", "«Se mudan a la casa nueva y los niños tienen, por fin, un patio.»", PARTES, 2, {0: "Es el final, no el comienzo.", 1: "El problema ya se resolvió."}, "<strong>Desenlace</strong>: el problema se resuelve.")}"""

    s2 = f"""<p>En una historia, los hechos están unidos por el <strong>tiempo</strong> y por la <strong>causa</strong>: uno pasa después del otro, y muchas veces por culpa del otro. Para seguir el orden, fíjese en las palabras que lo marcan:</p>
{C.tabla("Palabras que marcan el orden", ["Para…", "Palabras"],
         [["Empezar", "primero, al principio, una mañana, hace años"], ["Continuar", "después, luego, más tarde, al día siguiente, entonces"], ["Al mismo tiempo", "mientras, en ese momento, a la vez"],
          ["Terminar", "al final, finalmente, por fin, desde entonces"]])}
{C.caja("tip", "Causa y orden", "<p>Si un hecho causa otro, el que causa va primero. En «Como el autobús no llegó, Marisol caminó», primero el autobús no llega y después ella camina, aunque las palabras estén en otro orden.</p>")}
{P("Compruebe", "«Como llovía mucho, cancelaron el partido.» ¿Qué pasó primero?", ["Llovía mucho", "Cancelaron el partido", "Las dos cosas a la vez"], 0, {1: "Lo cancelaron porque llovía: la lluvia vino antes.", 2: "Una es la causa de la otra."}, "Primero <strong>llovía</strong>: es la causa.")}"""

    s3 = f"""<p>Todo texto se escribe para algo. Ese «para qué» es el <strong>propósito del autor</strong>. Los tres principales son:</p>
{C.tabla("Propósitos del autor y sus pistas", ["Propósito", "El autor quiere…", "Pistas en el texto", "Ejemplos"],
         [["Informar", "dar a conocer hechos o explicar cómo es o cómo se hace algo", "datos, fechas, números, pasos, tono neutral", "noticias, recetas, instrucciones, textos de ciencias"],
          ["Entretener", "contar una historia, divertir o emocionar", "personajes, diálogos, un problema, descripciones, humor", "cuentos, novelas, chistes, poemas"],
          ["Persuadir", "convencer al lector de pensar o hacer algo", "opiniones; palabras como <em>debe</em>, <em>el mejor</em>, <em>no se lo pierda</em>; razones para actuar; llamadas a la acción", "anuncios, cartas de opinión, discursos, campañas"]])}
{C.caja("tip", "Cómo justificarlo", "<p>No basta con decir «es para persuadir». En el GED se pide la evidencia: «El autor quiere persuadir, porque usa frases como <em>no espere más</em> y termina pidiendo al lector que llame».</p>")}
{C.caja("ojo", "Más de un propósito", "<p>Un texto puede tener varios, pero uno es el principal. Un anuncio puede ser divertido, pero su propósito principal es que usted compre.</p>")}
<h3>Un tema, tres propósitos</h3>
<p>Los tres textos hablan de bicicletas, pero cada uno tiene un propósito distinto. Lea cada uno y busque sus pistas.</p>
<p><strong>Texto A</strong></p>{pasaje("La ciudad inauguró ayer 12 nuevas estaciones de bicicletas compartidas en el lado oeste. Con ellas, la red suma 30 estaciones en la zona. El pase diario cuesta 15 dólares.")}
<p><strong>Texto B</strong></p>{pasaje("¿Cansado del tráfico? ¡Muévase en bici! Con nuestro pase mensual llega más rápido, ahorra dinero y cuida su salud. Inscríbase hoy y reciba la primera semana gratis.")}
<p><strong>Texto C</strong></p>{pasaje("Don Julio nunca había montado en bicicleta. A los sesenta años, su nieta le regaló una. El primer día se cayó tres veces, pero se levantó riendo. —Esta bici y yo vamos a ser amigos —dijo.")}
<p class="fuente">Los textos A, B y C son ejemplos escritos para esta lección; los números no son datos reales.</p>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary>
<ul><li><strong>A · Informar:</strong> datos (12 estaciones, 30 en total, 15 dólares), tono neutral, sin opiniones.</li><li><strong>B · Persuadir:</strong> una pregunta al lector, órdenes (<em>muévase, inscríbase</em>), beneficios y una oferta.</li>
<li><strong>C · Entretener:</strong> un personaje, un problema (no sabe montar), humor y un diálogo.</li></ul></details>
{P("Compruebe", "«Todos los vecinos deberían votar en la reunión del jueves: es nuestra oportunidad de mejorar el barrio.»", PROP, 2, {0: "No solo da datos: pide algo.", 1: "No cuenta una historia."}, "<strong>Persuadir</strong>: «deberían» y una razón para actuar.")}
{P("Compruebe", "«Para hacer una buena salsa, primero ase los tomates y los chiles; después licúelos con ajo y sal.»", PROP, 0, {1: "No hay personajes ni historia.", 2: "No intenta convencer: explica."}, "<strong>Informar</strong>: explica cómo se hace algo.")}"""

    s4 = f"""<p>Copie en su cuaderno el mapa de la historia (inicio, desarrollo, desenlace). Lea el cuento y complételo. Después responda las preguntas.</p>
{LE.escuchar(" ".join(MARISOL), "Escuchar el cuento")}
<div class="texto-lectura"><p><strong>La entrevista de Marisol</strong></p>{"".join(f"<p>{p}</p>" for p in MARISOL)}</div>
<details class="caja caja-tip"><summary><strong>Ver el mapa de la historia completo</strong></summary>
<ul><li><strong>Inicio:</strong> Marisol, una mujer que busca trabajo desde hace tres meses; su barrio; la llaman para una entrevista el jueves.</li>
<li><strong>Desarrollo:</strong> se prepara; el día de la entrevista el autobús no llega (problema); momento de mayor tensión: decide caminar quince cuadras.</li>
<li><strong>Desenlace:</strong> llega a tiempo, la entrevistadora valora su actitud y le da el trabajo; enseñanza: ante un problema, buscar una solución.</li></ul></details>
{P("Pregunta 1", "¿Cuál es el escenario de la historia?", ["Un barrio de la ciudad, durante una semana", "Una playa durante las vacaciones de verano", "Una escuela nocturna para adultos"], 0, {1: "No se habla de playa.", 2: "No se habla de una escuela."}, "El barrio, la parada y la clínica, de lunes a jueves.")}
{P("Pregunta 2", "¿Cuál es el problema principal el día de la entrevista?", ["La blusa de Marisol está arrugada", "El autobús no llega y puede llegar tarde", "La entrevistadora no la quiere recibir"], 1, {0: "La planchó con cuidado.", 2: "La recibe y le da el trabajo."}, "Es lo que pone en peligro lo que ella quiere: llegar a tiempo.")}
{P("Pregunta 3", "¿Cuál es el momento de mayor tensión?", ["Cuando suena el teléfono el lunes", "Cuando Marisol celebra con su familia", "Cuando decide caminar las quince cuadras"], 2, {0: "Eso es el inicio.", 1: "Eso es el desenlace."}, "Ahí se decide si llegará o no.")}
{P("Pregunta 4", "¿Por qué le dan el trabajo a Marisol?", ["Porque busca soluciones cuando hay un problema", "Porque vive muy cerca de la clínica", "Porque conoce a la entrevistadora"], 0, {1: "El texto no lo da como razón.", 2: "El texto no lo dice."}, "Lo dice la entrevistadora: «Cuando hay un problema, usted busca una solución».")}
{P("Pregunta 5", "¿Cuál es el propósito principal del autor?", ["Informar sobre los horarios de los autobuses", "Entretener con una historia que deja una enseñanza", "Persuadir al lector de trabajar en una clínica"], 1, {0: "No da datos de horarios.", 2: "No pide nada al lector."}, "Hay personajes, un problema y una solución: es un cuento.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · los textos de su día</span>
<p>Busque a su alrededor cinco textos distintos: un anuncio, una etiqueta de un alimento, un mensaje de la escuela, una noticia, una receta, un folleto, el chiste de un periódico… Para cada uno, escriba:</p>
<ul><li>Qué es y quién lo escribió.</li><li>Su propósito principal: informar, entretener o persuadir.</li><li>Dos pistas del texto que lo demuestran.</li></ul>
<p>Si tiene con quién practicar, miren juntos los anuncios de la televisión o del celular y descubran qué quieren que hagan: ¿comprar?, ¿votar?, ¿llamar? ¿Qué palabras usan para convencer?</p></div>"""

    secciones = [("s1", "Las partes de una historia", s1), ("s2", "El orden de los hechos", s2), ("s3", "El propósito del autor", s3), ("s4", "Lectura: «La entrevista de Marisol»", s4)]
    tarea = [("Mi película favorita.", "Haga el mapa de la historia de una película o una telenovela que conozca bien: personajes, escenario, problema, momento de mayor tensión y desenlace."),
             ("Tres propósitos.", "Escriba tres textos cortos (3 o 4 oraciones) sobre un mismo tema, por ejemplo su comida favorita: uno para informar, uno para persuadir y uno para entretener."),
             ("El final de Marisol.", "Escriba un final distinto para el cuento: ¿qué habría pasado si Marisol hubiera seguido esperando el autobús?")]
    quiz = [
        ("¿En qué parte de una historia aparece el problema o conflicto?", ["En el desarrollo", "En el desenlace", "En el título"], 0, {1: "En el desenlace se resuelve.", 2: "El título no cuenta la historia."}, "En el <strong>desarrollo</strong>."),
        ("El <strong>escenario</strong> de una historia es…", ["dónde y cuándo ocurre", "quién la escribió", "cómo termina el problema"], 0, {1: "Eso es el autor.", 2: "Eso es el desenlace."}, "<strong>Dónde y cuándo</strong> ocurre."),
        ("El <strong>desenlace</strong> es…", ["la parte en que se resuelve el problema", "el momento de mayor tensión", "la presentación de los personajes"], 0, {1: "Eso pertenece al desarrollo.", 2: "Eso es el inicio."}, "Se <strong>resuelve</strong> el problema."),
        ("¿Qué palabra suele indicar el final de una historia?", ["Finalmente", "Primero", "Mientras"], 0, {1: "Indica el comienzo.", 2: "Indica algo al mismo tiempo."}, "<strong>Finalmente.</strong>"),
        (pasaje(P1) + "¿Cuál es el propósito del texto?", PROP, 0, {1: "No hay personajes ni historia.", 2: "No pide nada al lector."}, "<strong>Informar</strong>: datos y horarios."),
        (pasaje(P2) + "¿Cuál es el propósito del texto?", PROP, 2, {0: "No solo da datos: pide algo.", 1: "No cuenta una historia."}, "<strong>Persuadir.</strong>"),
        (pasaje(P2) + "¿Qué pista muestra mejor ese propósito?", ["«Inscríbete esta semana y la primera clase es gratis.»", "El texto habla de aprender a nadar.", "El texto menciona que son diez clases."], 0, {1: "El tema no muestra el propósito.", 2: "Es un dato."}, "Una <strong>llamada a la acción</strong> con una oferta."),
        ("Un cuento con personajes, un problema y un final feliz tiene como propósito principal…", ["entretener", "informar", "persuadir"], 0, {1: "No da datos.", 2: "No pide nada."}, "<strong>Entretener.</strong>"),
        ("Unas instrucciones para armar un mueble tienen como propósito…", ["informar, explicando cómo se hace algo", "entretener con una historia divertida", "persuadir al lector de comprar más muebles"], 0, {1: "No hay historia.", 2: "No intentan convencer."}, "<strong>Informar.</strong>"),
        ("¿Qué se necesita para justificar el propósito del autor?", ["Señalar pistas del texto que lo demuestren", "Saber cómo se llama el autor del texto", "Leer solamente el título del texto"], 0, {1: "El nombre no dice el propósito.", 2: "El título no basta."}, "Las <strong>pistas del texto</strong>."),
    ]
    filas = [
        ("Mapa de la historia", "Encuentro los personajes, el escenario, el problema, el momento de mayor tensión y el desenlace.", "Encuentro el problema, pero dudo con el momento de mayor tensión.", "No distingo las partes (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Orden de los hechos", "Ordeno los hechos con las palabras de tiempo y las causas.", "Me confundo cuando la causa aparece después.", "No sigo el orden (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Propósito", "Digo si el texto informa, entretiene o persuade, y lo justifico con pistas.", "Lo digo, pero no doy pistas.", "No lo distingo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe trazar el mapa de una historia y reconocer para qué escribe un autor. En la próxima lección leerá con <strong>ilustraciones y características del texto</strong>: títulos, subtítulos, negritas y pies de foto.</p>"
    glosario = [("Escenario", "Dónde y cuándo ocurre una historia."), ("Conflicto", "El problema que mueve la historia."),
                ("Desenlace", "Parte final en la que se resuelve el problema."), ("Propósito del autor", "Para qué escribió el texto: informar, entretener o persuadir.")]
    conexion = ("<p>En el Nivel 1 conoció a los personajes, el escenario y las palabras de secuencia. Hoy los unirá en un mapa de la historia, y se preguntará para qué escribe cada autor.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.3.1", "R.6.1"], base=["R.3.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Cómo se arma una historia y para qué escribe el autor.", ["Lectura", "Estructura y propósito"],
                            ["<strong>Reconocer</strong> el inicio, el desarrollo y el desenlace de una historia.", "<strong>Ordenar</strong> los hechos con las palabras de tiempo y las causas.",
                             "<strong>Identificar</strong> el propósito del autor: informar, entretener o persuadir.", "<strong>Justificar</strong> el propósito con pistas del texto."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-3", LE.titulo("4-3")), glosario, P)


def practica():
    orden = []
    for ti, pasos in HIST:
        r = random.Random(ti); ini = list(range(len(pasos)))
        while ini == sorted(ini):
            r.shuffle(ini)
        orden.append({"titulo": f"«{ti}»", "intro": "Ordene los hechos con los botones ▲ y ▼. Las palabras de tiempo y las causas le ayudan.", "pasos": pasos, "inicio": ini, "cons": {},
                      "general": "Lea la historia en voz alta en este orden para fijarla."})
    pa = [{"enun": f"<p>Historia: <strong>«{h}»</strong></p>{pasaje(e)}<strong>¿En qué parte de la historia va?</strong>", "ops": PARTES, "ok": k, "enOrden": True,
           "pista": "¿Presenta algo, complica algo o lo resuelve?", "exp": f"<strong>{PARTES[k]}</strong>. {x}"} for h, e, k, x in EN_PARTE]
    pr = [{"enun": pasaje(f"«{t}»") + "<strong>¿Cuál es el propósito principal?</strong>", "ops": PROP, "ok": k, "enOrden": True,
           "pista": "Busque las pistas: ¿hay datos, hay personajes o hay frases para convencer?", "exp": f"<strong>{PROP[k]}</strong>. Pista: {x}"} for t, k, x in PROPOSITOS]
    mods = [("orden", "Ordene la historia", C.orden("m1", "Ponga los hechos en el orden en que ocurrieron.")),
            ("partes", "¿En qué parte va?", C.om("m2", "Diga si el hecho es del inicio, del desarrollo o del desenlace.")),
            ("proposito", "El propósito del autor", C.om("m3", "Lea el texto y elija su propósito principal."))]
    js = C.js_datos("OR", orden) + C.js_datos("PA", pa) + C.js_datos("PR", pr) + 'creaOrden("m1", OR);\ncreaBanco("m2", PA);\ncreaBanco("m3", PR);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
