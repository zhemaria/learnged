# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 8.1 · Conversar con respeto: turnos, enlazar y aclarar.
Fuente: clases_leng2/clase_8-1.html (GEDparaHispanos) y gramatica/n2-l8-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_8_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "8-1"
TURNOS = [("🏫 Reunión de padres", "La directora explica el nuevo horario. Usted tiene una pregunta.", "", ["Esperar a que termine y decir: «Si me permite, tengo una pregunta».", "Levantar la voz para preguntar mientras ella sigue explicando el horario.", "Comentar la pregunta en voz baja con el padre que está sentado al lado."], "Espera y pide la palabra con cortesía."),
          ("💻 Clase por Zoom", "El profesor explica un ejercicio y usted quiere opinar.", "", ["Usar la mano virtual y esperar a que le den la palabra.", "Activar el micrófono y empezar a hablar enseguida.", "Escribir su opinión en el chat con letras mayúsculas."], "La mano virtual es la forma de pedir la palabra en línea."),
          ("👷 Reunión de trabajo", "Hace diez minutos que habla la misma persona y la reunión casi termina.", "", ["«Perdón que interrumpa; nos quedan cinco minutos. ¿Podemos decidir?»", "«Ya basta, llevas demasiado tiempo hablando tú solo y nadie te escucha.»", "Levantarse y salir de la reunión sin decir nada a nadie, para que se note."], "Interrumpe con disculpa y una razón."),
          ("🏫 Círculo de ideas", "Tres compañeros han hablado varias veces. Rosa no ha dicho nada.", "", ["«Rosa, no te hemos escuchado todavía. ¿Qué piensas?»", "Seguir hablando para que no haya silencios incómodos.", "«Rosa nunca dice nada; mejor sigamos sin ella.»"], "Da paso a quien no ha hablado."),
          ("🩺 Cita médica", "La doctora le está explicando un tratamiento. Le suena el teléfono.", "", ["Silenciar el teléfono y seguir escuchando a la doctora.", "Contestar la llamada mientras la doctora sigue hablando.", "Mirar los mensajes mientras ella termina de explicar."], "Escuchar con atención es parte del respeto."),
          ("🏢 Asamblea de vecinos", "Un vecino dice algo con lo que usted no está de acuerdo.", "", ["Esperar su turno y decir: «Entiendo su punto, pero yo pienso…».", "Decirle en voz alta, delante de todos, que está diciendo tonterías.", "Reírse de lo que dijo y comentarlo con el vecino que está al lado."], "Se critican las ideas, no a las personas."),
          ("💼 Entrevista de trabajo", "La entrevistadora todavía está formulando la pregunta.", "", ["Esperar a que termine la pregunta antes de responder.", "Empezar a responder antes de que termine de preguntar.", "Interrumpirla para hablar de su experiencia anterior."], "Escuchar la pregunta completa evita malentendidos."),
          ("🏫 Clase presencial", "Usted quiere añadir un ejemplo a lo que acaba de decir un compañero.", "", ["Levantar la mano y decir: «¿Puedo añadir un ejemplo?».", "Hablar al mismo tiempo que su compañero para no olvidarlo.", "Esperar al final de la clase y no decir nada nunca."], "Pide permiso y participa.")]
ENLAZA = [("🏫 Reunión de padres", "Están hablando de la seguridad a la salida de la escuela.", "Una madre: «Hace falta un guardia en el cruce de la esquina».", ["«Estoy de acuerdo, y añado que también faltan señales de alto».", "«¿Alguien sabe a qué hora es el partido del sábado?»", "«Yo prefiero hablar de la comida de la cafetería»."], "Retoma la idea y suma otra relacionada."),
          ("👷 Reunión de trabajo", "El grupo decide cuándo hacer la capacitación.", "Un compañero: «La capacitación debería ser el sábado».", ["«Entiendo tu punto, pero muchos tenemos a los niños el sábado».", "«No, el sábado no, y punto; eso no se discute más en esta reunión».", "«Hablando de otra cosa, ¿quién trajo el café que está en la mesa?»"], "Discrepa con respeto y da una razón."),
          ("🏫 Círculo de ideas", "Hablan sobre un texto de opinión acerca del reciclaje.", "Luis: «El autor da dos razones con datos».", ["«Como dijo Luis, hay dos razones; a mí me convenció la de la energía».", "«A mí, la verdad, no me gusta nada leer textos tan largos como este».", "«Perdón, ¿alguien sabe cuándo es el examen del GED este año?»"], "Nombra a Luis y continúa su idea."),
          ("🏢 Asamblea de vecinos", "Se habló de la basura, de las luces y del ruido. Ya casi termina.", "", ["«Para resumir: pediremos más contenedores, luces nuevas y horario de silencio».", "«Bueno, yo me tengo que ir ya, que es tarde y mañana trabajo temprano».", "«Lo del ruido de los sábados por la noche me molesta muchísimo, la verdad»."], "Resume lo que se dijo."),
          ("🏫 Clase", "La maestra preguntó qué es un texto informativo. Ana respondió primero.", "Ana: «Es un texto que explica un tema».", ["«Sí, y añado que no lleva opiniones, solo datos».", "«Yo creo que la clase de hoy fue muy larga».", "«¿Puedo ir al baño un momento?»"], "Completa la respuesta de Ana."),
          ("👪 Familia", "Deciden adónde ir el domingo.", "Su hijo: «Podemos ir al parque, porque va a hacer sol».", ["«Retomando lo del sol, podríamos llevar comida y hacer un pícnic».", "«El lunes tengo que madrugar mucho para ir a trabajar a la fábrica».", "«No sé, haz lo que quieras; a mí, la verdad, me da completamente igual»."], "Retoma la idea del sol y la desarrolla."),
          ("💻 Foro del curso", "Una compañera publicó su texto de opinión sobre el transporte.", "Su texto: «El autobús es más barato que el carro».", ["«Estoy de acuerdo contigo, y añado que tampoco hay que buscar estacionamiento».", "«Mi texto es mucho mejor que el tuyo, porque tiene más razones y datos».", "«No leí tu texto completo, pero seguramente está bien, como siempre»."], "Enlaza con su idea y suma un argumento.")]
ACLARA = [("🩺 Cita médica", "El médico le explica cómo tomar una medicina nueva. Quiere asegurarse de que entendió.", "Médico: «Tómela cada ocho horas durante diez días».", ["«Entonces, si entiendo bien, una pastilla cada ocho horas por diez días, ¿verdad?»", "Asentir con la cabeza y preguntarle después a un vecino o a un familiar.", "Decir que sí a todo para no hacerle perder tiempo al médico en la consulta."], "Repite lo que entendió para comprobarlo."),
          ("💊 Farmacia", "La farmacéutica habla muy rápido.", "", ["«Disculpe, ¿me lo puede repetir más despacio, por favor?»", "Irse sin preguntar y leer la etiqueta al llegar a casa.", "Pedirle que hable en inglés, aunque no lo entienda bien."], "Pedir que repita es su derecho."),
          ("🏫 Reunión de padres", "La maestra dice que su hijo necesita «refuerzo en lectura». No sabe qué significa.", "", ["«¿Podría explicarme qué quiere decir con refuerzo en lectura?»", "«Sí, claro, lo que usted diga, maestra; muchas gracias por todo».", "Quedarse con la duda y no volver a preguntar nada en la reunión."], "Pide que le explique el término."),
          ("💼 Entrevista de trabajo", "Le preguntan si tiene disponibilidad para un «turno rotativo».", "", ["«¿Quiere decir que el horario cambia cada semana?»", "«Sí, sí, no hay ningún problema con eso».", "«No entiendo, así que mejor no me interesa el puesto»."], "Comprueba lo que significa antes de responder."),
          ("👷 Trabajo", "Su supervisor dice: «Cambia el pedido». Hay dos pedidos abiertos.", "", ["«¿Se refiere al pedido de la mañana o al de la tarde?»", "Cambiar los dos pedidos para no equivocarse.", "No cambiar ninguno hasta que vuelva a pedirlo."], "Precisa a qué se refiere."),
          ("🏫 Círculo de ideas", "Usted dijo que el texto era «parcial» y nadie entendió.", "Compañero: «¿Qué quieres decir con parcial?»", ["«Lo que quiero decir es que solo muestra un punto de vista; por ejemplo…»", "«Parcial es parcial; si no lo sabes, búscalo tú mismo en el diccionario».", "«Olvídalo, no importa lo que dije antes; sigamos con otra cosa»."], "Aclara con otras palabras y un ejemplo."),
          ("🏦 Banco", "El empleado menciona un «cargo por mantenimiento». Usted no sabe cuánto es.", "", ["«¿Cuánto es ese cargo y cada cuánto se cobra?»", "Firmar todo para no hacer esperar a la fila.", "«Ah, sí, el cargo, claro, ya lo sabía»."], "Pregunta el dato concreto que necesita."),
          ("🏥 Hospital", "La enfermera le da instrucciones para el día de la operación.", "Enfermera: «Ayuno desde la medianoche».", ["«¿Quiere decir que no puedo comer ni beber nada después de las doce?»", "«Bueno, pero un café con leche en la mañana no hace ningún daño».", "Preguntarle a un amigo, al llegar a casa, qué significa «ayuno»."], "Comprueba lo que entendió con la misma persona.")]
DIALOGO = [("Marta", "inicia", "Buenas tardes a todos. Hoy queremos decidir si pedimos a la escuela que abra la biblioteca los sábados. ¿Quién quiere empezar?"),
           ("Jorge", "pide la palabra", "<mark>Si me permiten</mark>, yo creo que es buena idea. Muchos padres trabajamos entre semana y el sábado es el único día en que podemos ir con nuestros hijos."),
           ("Lucía", "enlaza y pregunta", "<mark>Estoy de acuerdo con Jorge, y añado que</mark> los niños podrían usar las computadoras para las tareas. Pero tengo una duda. <mark>¿Podrías explicar</mark> quién atendería la biblioteca ese día?"),
           ("Jorge", "aclara", "Buena pregunta. <mark>Lo que quiero decir es que</mark> podría haber voluntarios del comité, por turnos."),
           ("Samuel", "discrepa", "<mark>Entiendo tu punto, Jorge, pero</mark> me preocupa que no haya suficientes voluntarios. <mark>Retomando lo que dijo Lucía</mark> sobre las computadoras, quizás podríamos empezar solo dos sábados al mes."),
           ("Marta", "resume", "<mark>Entonces, para resumir:</mark> todos vemos la utilidad, la duda es quién atiende, y Samuel propone empezar con dos sábados al mes. ¿Les parece bien que lo propongamos así?")]


def escena(lugar, sit, dice):
    return f'<div class="texto-lectura escena-s"><p><strong>{lugar}</strong><br>{sit}</p>' + (f"<p><em>{dice}</em></p>" if dice else "") + "</div>"


def plano(t):
    import re
    return re.sub(r"<[^>]+>", "", t)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la clase, en una reunión de padres, en el trabajo o en la consulta del médico, conversamos con otras personas para resolver algo juntos. Una buena conversación no es la que gana quien habla más alto, sino aquella en la que todos se escuchan y las ideas de uno ayudan a las de otro. Hablar bien en grupo se aprende, igual que escribir bien. En este último tema del nivel practicará cómo pedir la palabra, cómo unir su idea a la de otra persona y qué decir cuando no entiende algo.</p>
{C.tabla("Las normas de una buena discusión", ["Norma", "Qué significa"],
         [["👂 Escuchar", "Hasta el final, sin interrumpir ni mirar el teléfono."], ["✋ Pedir la palabra", "Y esperar su turno."], ["🔗 Enlazar", "Conectar su idea con lo que ya se dijo."],
          ["❓ Preguntar", "Cuando algo no está claro."], ["🎯 Ser breve", "Hablar del tema, para que todos participen."], ["🤝 Respetar", "Criticar las ideas, no a las personas."]])}
{C.caja("tip", "¿Tú o usted?", "<p>Recuerde la Lección 3.3: con compañeros de clase, <em>tú</em>; en una cita médica, una entrevista o con alguien mayor que no conoce, <em>usted</em>. Las frases de esta lección sirven en las dos formas.</p>")}
<h3>Diálogo modelo: la reunión de padres</h3>
<p>Cuatro padres del comité de la escuela discuten si la escuela debería abrir la biblioteca los sábados. Lea el diálogo o escúchelo. Fíjese en las frases resaltadas.</p>
{LE.escuchar(" ".join(f"{n}: {plano(t)}" for n, _, t in DIALOGO), "Escuchar el diálogo")}
<div class="texto-lectura dialogo">{"".join(f'<p><strong>{n}</strong> <span class="rol">{r}</span><br>{t}</p>' for n, r, t in DIALOGO)}</div>
<p class="fuente">Texto escrito para esta lección.</p>
{C.caja("tip", "Fíjese", "<p>Samuel no está de acuerdo del todo, pero lo dice con respeto («Entiendo tu punto, pero…») y propone una solución. <strong>Discrepar no es pelear.</strong></p>")}
{P("Diálogo 1", "¿Qué frase usa Jorge para pedir la palabra?", ["«¿Quién quiere empezar?»", "«Si me permiten…»", "«Para resumir…»"], 1, {0: "Esa es de Marta, para iniciar.", 2: "Esa es para resumir."}, "Pide permiso antes de hablar.")}
{P("Diálogo 2", "¿Cómo muestra Samuel su desacuerdo?", ["Interrumpe a Jorge en voz alta", "Dice que la idea de Jorge es mala", "Reconoce la idea y propone otra opción"], 2, {0: "Espera su turno.", 1: "No ataca la idea."}, "«Entiendo tu punto, Jorge, pero…» y propone dos sábados al mes.")}
{P("Diálogo 3", "¿Qué hace Marta al final?", ["Resume lo dicho y pide acuerdo", "Da por terminada la reunión sin más", "Cambia de tema por completo"], 0, {1: "Pide acuerdo antes.", 2: "Sigue en el tema."}, "«Para resumir…».")}"""

    s2 = f"""{C.tabla("Frases para pedir la palabra", ["Situación", "Frases útiles"],
         [["Quiere hablar", "«Si me permiten…» · «¿Puedo añadir algo?» · «Quisiera decir algo sobre eso.»"], ["Alguien está hablando", "Espere a que termine. Si es en línea, use el botón de levantar la mano."],
          ["Tiene que interrumpir", "«Perdón que interrumpa, pero…» · «Disculpe, una pregunta rápida.»"], ["Quiere dar paso a otro", "«¿Qué opinas tú, Ana?» · «No hemos escuchado a Luis todavía.»"]])}
{C.caja("tip", "En una clase por Zoom", "<p>Active el micrófono solo cuando le toca, use la mano virtual para pedir la palabra y el chat para preguntas cortas.</p>")}
{P("¿Respetuoso? 1", "«Perdón que interrumpa, pero ¿podemos ver la hora?»", ["Respetuoso", "No respetuoso"], 0, {1: "Pide disculpas y es breve."}, "<strong>Respetuoso.</strong>")}
{P("¿Respetuoso? 2", "«¡Eso no es así! Déjame hablar a mí.»", ["Respetuoso", "No respetuoso"], 1, {0: "Corta al otro."}, "<strong>No respetuoso</strong>: corta al otro sin respeto.")}
<h3>Enlazar con lo que dijo otro</h3>
<p>Enlazar es empezar su comentario conectándolo con lo que dijo otra persona. Así la conversación avanza en lugar de saltar de un tema a otro.</p>
{C.tabla("Frases para enlazar", ["Para…", "Frases útiles"],
         [["Estar de acuerdo y sumar", "«Estoy de acuerdo con… y añado que…» · «Como dijo…, yo también…»"], ["No estar de acuerdo", "«Entiendo tu punto, pero…» · «Veo lo que dices; sin embargo…»"],
          ["Retomar una idea", "«Retomando lo que dijo…» · «Volviendo a la idea de…»"], ["Resumir", "«Para resumir…» · «Entonces, lo que hemos dicho es…»"]])}
{P("Enlazar", "Ana dijo: «El parque necesita más luces por la noche». ¿Qué respuesta enlaza mejor?", ["Como dijo Ana, falta luz, y añado que también faltan bancas.", "Yo quiero hablar de los precios del supermercado.", "Eso que dijo Ana no tiene ningún sentido para nadie."], 0, {1: "Cambia de tema.", 2: "No es respetuoso."}, "Retoma la idea de Ana y suma otra.")}"""

    s3 = f"""<p>No entender algo es normal. Lo que no conviene es quedarse callado. Pedir una aclaración es una forma de respeto: demuestra que está escuchando.</p>
{C.tabla("Frases para pedir y dar aclaraciones", ["Para…", "Frases útiles"],
         [["Pedir que expliquen", "«¿Podrías explicar…?» · «¿Me puede repetir…, por favor?» · «No entendí bien la parte de…»"], ["Comprobar que entendió", "«¿Quieres decir que…?» · «Entonces, si entiendo bien…»"],
          ["Aclarar lo que usted dijo", "«Lo que quiero decir es que…» · «Me explico mejor: …» · «Por ejemplo, …»"]])}
{C.caja("tip", "En la consulta del médico", "<p>Repita con sus palabras lo que le indicó: «Entonces, si entiendo bien, tomo una pastilla cada ocho horas durante una semana, ¿verdad?». Si algo está mal, el médico lo corregirá en ese momento.</p>")}
{P("Aclarar 1", "Un compañero dice: «Hay que cambiar el plan». Usted no sabe qué plan. ¿Qué dice?", ["¿Quieres decir el plan de estudio del grupo?", "Sí, claro, estoy totalmente de acuerdo.", "No me importa, haz lo que quieras."], 0, {1: "Se queda con la duda.", 2: "No es respetuoso."}, "Comprueba lo que entendió.")}
{P("Aclarar 2", "Le dicen que su idea no se entendió. ¿Qué hace?", ["Repetir la misma frase más alto", "Decir «Lo que quiero decir es que…» y dar un ejemplo", "Quedarse callado el resto de la reunión"], 1, {0: "Más alto no es más claro.", 2: "Se pierde su idea."}, "Aclara con otras palabras y un ejemplo.")}
<h3>El círculo de ideas</h3>
<p>En la clase en vivo trabajará en grupos de cuatro sobre un texto leído. Cada persona tiene un rol, y en la siguiente ronda los roles cambian:</p>
{C.tabla("Roles del círculo de ideas", ["Rol", "Qué hace"], [["🚀 Quien inicia", "Presenta el tema y la primera idea."], ["🔗 Quien enlaza", "Conecta su idea con la anterior."], ["❓ Quien pregunta", "Pide aclaraciones o ejemplos."], ["📝 Quien resume", "Recoge lo dicho al final."]])}
{C.tabla("Rúbrica de participación oral", ["Criterio", "3 · Logrado", "2 · En camino", "1 · Inicial"],
         [["Respeta los turnos", "Pide la palabra y espera siempre", "A veces interrumpe", "Interrumpe con frecuencia"], ["Enlaza su comentario", "Conecta con lo que dijo otro, usando frases para enlazar", "A veces conecta", "Habla sin relación con lo anterior"],
          ["Pide o da aclaraciones", "Pregunta y aclara cuando hace falta", "Lo hace solo si se le pide", "No pregunta ni aclara"], ["Escucha con atención", "Mira al hablante y retoma sus ideas", "Escucha, pero se distrae", "No presta atención"]])}
<p>Total: 12 puntos.</p>
<p>Si tiene con quién practicar, en la cena propongan un tema (¿adónde ir el domingo?) y repartan los cuatro roles. Al final, quien resume dice lo que se decidió.</p>"""

    secciones = [("s1", "Las normas y una reunión modelo", s1), ("s2", "Pedir la palabra y enlazar", s2), ("s3", "Aclarar y el círculo de ideas", s3)]
    tarea = [("Para el foro.", "Responda a dos compañeros usando una frase para enlazar distinta en cada respuesta: «Estoy de acuerdo con… y añado…», «Entiendo tu punto, pero…» o «¿Podrías explicar…?»."),
             ("Mi frase de rescate.", "Escriba tres frases que usaría en una cita médica o en una oficina para pedir que le repitan o le expliquen algo. Practíquelas en voz alta."),
             ("Observe una conversación.", "Mire un programa de debate o una reunión. Anote una frase respetuosa para discrepar y una interrupción que no fue respetuosa.")]
    quiz = [
        ("¿Cuál es la forma más respetuosa de pedir la palabra?", ["«Si me permiten, quisiera añadir algo.»", "«¡Ahora me toca a mí!»", "Empezar a hablar más alto que los demás."], 0, {1: "No pide permiso.", 2: "No respeta el turno."}, "Pide <strong>permiso</strong>."),
        ("En una clase por Zoom, para pedir la palabra conviene…", ["usar la mano virtual y esperar", "activar el micrófono y hablar enseguida", "escribir en mayúsculas en el chat"], 0, {1: "Interrumpe.", 2: "Las mayúsculas parecen gritos."}, "La <strong>mano virtual</strong>."),
        ("¿Qué frase <strong>enlaza</strong> con un comentario anterior?", ["«Estoy de acuerdo con Luis, y añado que…»", "«Yo quiero hablar de otra cosa.»", "«¿A qué hora termina la reunión?»"], 0, {1: "Cambia de tema.", 2: "Cambia de tema."}, "Nombra a Luis y <strong>suma</strong>."),
        ("¿Cómo muestra desacuerdo con respeto?", ["«Entiendo tu punto, pero creo que…»", "«Eso que dices es una tontería.»", "Quedarse callado, molesto, sin decir nada."], 0, {1: "Ataca a la persona.", 2: "No comunica nada."}, "Reconoce el punto y da el suyo."),
        ("«Retomando lo que dijo Carmen…» sirve para…", ["conectar con una idea dicha antes", "cambiar de tema por completo", "terminar la reunión"], 0, {1: "Es lo contrario.", 2: "Eso es resumir."}, "<strong>Conectar.</strong>"),
        ("¿Cuándo conviene pedir una aclaración?", ["Cuando no entiende algo importante", "Nunca, porque parece de mala educación", "Solo al final de la reunión, si sobra tiempo"], 0, {1: "Preguntar es respetuoso.", 2: "Mejor en el momento."}, "Cuando <strong>no entiende</strong>."),
        ("¿Qué frase sirve para <strong>comprobar</strong> que entendió?", ["«¿Quieres decir que…?»", "«Ya sé, ya sé, sigue.»", "«Bueno, como tú digas.»"], 0, {1: "No comprueba nada.", 2: "No comprueba nada."}, "<strong>¿Quieres decir que…?</strong>"),
        ("Para aclarar algo que <strong>usted</strong> dijo, puede decir…", ["«Lo que quiero decir es que…»", "«No me entiendes nunca.»", "«Olvídalo, no importa.»"], 0, {1: "Culpa al otro.", 2: "Se pierde la idea."}, "<strong>Lo que quiero decir es que…</strong>"),
        ("En el círculo de ideas, la persona que <strong>resume</strong>…", ["recoge al final lo que se dijo", "presenta el tema al principio", "hace todas las preguntas"], 0, {1: "Esa inicia.", 2: "Esa pregunta."}, "<strong>Recoge</strong> lo dicho."),
        ("En una discusión se critican…", ["las ideas, no a las personas", "las personas, no las ideas", "las ideas y también las personas"], 0, {1: "Es al revés.", 2: "A las personas, nunca."}, "Las <strong>ideas</strong>."),
    ]
    filas = [
        ("Turnos", "Pido la palabra, espero y doy paso a otros.", "A veces interrumpo.", "Interrumpo a menudo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Enlazar", "Conecto mi idea con la anterior y discrepo con respeto.", "A veces cambio de tema.", "Hablo sin relación con lo anterior (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Aclarar", "Pido que me expliquen y compruebo lo que entendí.", "Pregunto solo a veces.", "Me quedo con la duda (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya conversa con respeto y claridad. En la próxima lección practicará la <strong>comprensión auditiva</strong> y preparará una presentación oral.</p>"
    glosario = [("Pedir la palabra", "Solicitar el turno para hablar."), ("Enlazar", "Conectar su comentario con lo que dijo otra persona."),
                ("Discrepar", "No estar de acuerdo, y decirlo con respeto."), ("Aclarar", "Explicar mejor algo, o pedir que lo expliquen.")]
    conexion = ("<p>En el Nivel 1 practicó hablar y escuchar en conversaciones sencillas, y en la Lección 3.3 aprendió a elegir el registro. Hoy pondrá todo junto para participar en una discusión de grupo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, alguien con quien conversar.</p>")
    estd = LE.estandares([], base=["R.6.1"], fund=["SL.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Hablar en grupo: turnos, enlaces y aclaraciones.", ["Comunicación oral", "Conversación"],
                            ["<strong>Seguir</strong> las normas de una buena discusión.", "<strong>Pedir</strong> la palabra y dar paso a otros.",
                             "<strong>Enlazar</strong> su idea con la de otra persona, y discrepar con respeto.", "<strong>Pedir y dar</strong> aclaraciones."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-2", LE.titulo("8-2")), glosario, P)


def practica():
    def banco(d, q, pista):
        return [{"enun": escena(l, s, x) + f"<strong>{q}</strong>", "ops": ops, "ok": 0, "pista": pista, "exp": e} for l, s, x, ops, e in d]
    tu = banco(TURNOS, "¿Qué es lo más respetuoso?", "¿Esa forma respeta el turno y a las personas?")
    en = banco(ENLAZA, "¿Qué respuesta enlaza mejor con lo que se dijo?", "¿Esa respuesta se conecta con lo que acaban de decir?")
    ac = banco(ACLARA, "¿Qué diría usted?", "¿Esa respuesta le ayuda a entender mejor, o le deja con la duda?")
    mods = [("turnos", "Respetar los turnos", C.om("m1", "Elija lo más respetuoso en cada situación.")), ("enlazar", "Enlazar", C.om("m2", "Elija la respuesta que se conecta con lo que se dijo.")),
            ("aclarar", "Pedir y dar aclaraciones", C.om("m3", "Elija lo que diría para entender mejor o para explicarse."))]
    js = C.js_datos("TU", tu) + C.js_datos("EN", en) + C.js_datos("AC", ac) + 'creaBanco("m1", TU);\ncreaBanco("m2", EN);\ncreaBanco("m3", AC);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
