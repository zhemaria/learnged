# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.1 · Los personajes y sus conflictos.
Fuente: clases_leng1/clase_5-1.html (GEDparaHispanos) y gramatica/n1-l5-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_5_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-1"
ROLES = ["Protagonista", "Antagonista", "Mentor o mentora"]
# (historia, [(personaje, rol)])
HISTORIAS = [
    ("Lucía quiere abrir su propia panadería. Su tía, que fue panadera muchos años, le enseña a hacer la masa. Pero el dueño del local se niega a alquilárselo y le pone mil obstáculos.", [("Lucía", 0), ("la tía", 2), ("el dueño del local", 1)]),
    ("Tomás es el nuevo en el equipo de fútbol. El entrenador lo aconseja y le enseña a no rendirse. Pero Raúl, el capitán, no quiere que Tomás juegue y lo deja fuera de las jugadas.", [("Tomás", 0), ("el entrenador", 2), ("Raúl", 1)]),
    ("Una familia de pescadores sale al mar para salvar su barco. Una tormenta enorme los atrapa durante dos días. El abuelo, que conoce el mar como nadie, les dice cómo mantener el barco a flote.", [("la familia de pescadores", 0), ("la tormenta", 1), ("el abuelo", 2)]),
    ("Ana estudia para el GED por las noches. Su vecina, una maestra jubilada, le presta libros y le explica las dudas. Pero el cansancio intenta vencerla cada noche.", [("Ana", 0), ("la vecina", 2), ("el cansancio", 1)]),
    ("El joven Pedro quiere ser músico. Su padre se opone y le esconde la guitarra. Don Julio, un viejo guitarrista del barrio, le da clases a escondidas.", [("Pedro", 0), ("el padre", 1), ("don Julio", 2)]),
    ("Marisol defiende a los vecinos de su edificio. Una empresa quiere sacarlos para construir oficinas. Una abogada del centro comunitario le explica sus derechos.", [("Marisol", 0), ("la empresa", 1), ("la abogada", 2)]),
]
RTIPOS = ["Físico", "De personalidad", "De su forma de hablar"]
RASGOS = [("Tiene el cabello largo y rizado.", 0), ("Es muy alta y delgada.", 0), ("Tiene una cicatriz en la mano izquierda.", 0), ("Usa anteojos redondos.", 0), ("Tiene unos sesenta años y la piel morena.", 0),
          ("Siempre ayuda a sus vecinos sin pedir nada a cambio.", 1), ("Es muy desconfiado: no cree en nadie.", 1), ("Nunca se rinde, aunque las cosas salgan mal.", 1), ("Es tímida y se pone roja cuando le hablan.", 1),
          ("Es honesto: devolvió la cartera que encontró.", 1), ("Habla muy despacio y en voz baja.", 2), ("Siempre grita cuando está nervioso.", 2), ("Usa palabras muy técnicas que nadie entiende.", 2),
          ("Habla con mucha cortesía: «Con su permiso, señora».", 2), ("Repite «¿me explico?» al final de cada frase.", 2)]
# (situación, 0 interno / 1 externo)
CONFLICTOS = [("Daniel quiere decirle a su jefe que está enfermo, pero tiene miedo de perder el trabajo.", 0), ("Un incendio obliga a la familia Ramos a salir de su casa en plena noche.", 1),
              ("Sara no sabe si perdonar a su hermana o seguir enojada con ella.", 0), ("El banco le niega el préstamo a Jorge para su negocio.", 1),
              ("Rosa siente vergüenza de su acento y no se atreve a hablar en las reuniones.", 0), ("Una sequía seca el pozo del que bebe todo el pueblo.", 1),
              ("Luis se siente culpable porque no visitó a su abuelo antes de que muriera.", 0), ("Dos vecinos discuten porque el árbol de uno tapa la luz del otro.", 1),
              ("Carmen duda de si es demasiado mayor para volver a estudiar.", 0), ("El dueño del edificio quiere subir la renta al doble.", 1),
              ("Mario quiere dejar el cigarro, pero cuando está nervioso le gana la tentación.", 0), ("Una nueva ley obliga a los vendedores de la calle a pagar un permiso muy caro.", 1),
              ("Elena no se decide entre aceptar un trabajo lejos o quedarse cerca de su familia.", 0), ("Un perro bravo no deja pasar a Pablo por la única calle que lleva a su casa.", 1),
              ("Teresa piensa que no es lo bastante inteligente para aprobar el examen.", 0), ("La nieve bloquea la carretera y la ambulancia no puede llegar.", 1),
              ("Los compañeros de trabajo de Inés le esconden las herramientas para molestarla.", 1), ("Felipe sabe que su amigo robó dinero y no sabe si decírselo a alguien.", 0),
              ("El río crece y amenaza con inundar las siembras de la familia.", 1), ("Carlos quiere invitar a María a salir, pero le tiembla la voz y no se atreve a llamarla.", 0)]
MARTA = ["Marta vivía en un barrio de Chicago donde casi todos hablaban español. Tenía cuarenta años y trabajaba limpiando casas. Era una mujer callada, trabajadora y muy educada con sus clientes, pero cuando llegaba a casa se sentía triste: quería estudiar inglés, pero el miedo a equivocarse le cerraba la boca.",
         "Su vecina, doña Elena, era maestra jubilada. Cada semana le repetía: «Marta, tú puedes. No tienes que hablar perfecto: solo tienes que empezar».",
         "Un martes por la mañana, Marta caminó hasta el centro comunitario y se inscribió en la clase de inglés. Se sentó en la última fila, con el cuaderno temblando entre las manos. Cuando la maestra le pidió que se presentara, Marta respiró profundo y dijo: «My name is Marta». Tres palabras. Pero por primera vez en años, sonrió desde adentro."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Los <strong>personajes</strong> son las personas, los animales o los seres imaginarios a quienes les pasan las cosas en una historia. Analizar a un personaje es mirar tres cosas: el <strong>papel</strong> (rol) que cumple, sus <strong>rasgos</strong> (cómo es) y el <strong>conflicto</strong> que enfrenta.</p>
{C.caja("tip", "Idea central", "<p>Toda historia se sostiene en una pregunta sencilla: <strong>¿qué le pasa al personaje y cómo responde?</strong></p>")}
<h3>Tres papeles frecuentes</h3>
{C.tabla("Los papeles de los personajes", ["Papel", "Qué hace", "Ejemplo"],
         [["👤 Protagonista", "Es el personaje principal. Enfrenta el conflicto y, casi siempre, cambia o aprende algo.", "Caperucita, en <em>Caperucita Roja</em>."],
          ["⚔️ Antagonista", "Se opone al protagonista. No siempre es «malo»: puede ser un rival, una autoridad, la naturaleza o una fuerza como el cansancio.", "El lobo, en <em>Caperucita Roja</em>."],
          ["🦉 Mentor o mentora", "Guía, aconseja o ayuda al protagonista.", "El hada madrina, en <em>Cenicienta</em>."]])}
{P("Compruebe", "<em>Lucía quiere abrir su panadería. Su tía le enseña a hacer la masa. El dueño del local no quiere alquilárselo.</em> ¿Qué papel cumple <strong>la tía</strong>?", ROLES, 2,
   {0: "La historia gira alrededor de Lucía, no de la tía.", 1: "La tía no se opone: ayuda."}, "Es la <strong>mentora</strong>: enseña y ayuda a Lucía.")}"""

    s2 = f"""<h3>Los rasgos: cómo es el personaje</h3>
{C.tabla("Tres clases de rasgos", ["Clase", "Pregunta", "Ejemplo"],
         [["Físicos", "¿Cómo se ve? ¿Qué edad tiene?", "Alto, delgado, de pelo canoso, con anteojos."],
          ["De personalidad", "¿Cómo es por dentro? ¿Cómo actúa?", "Honesto, tímido, valiente, generoso."],
          ["Forma de hablar", "¿Qué dice y cómo lo dice?", "Habla con cortesía, usa palabras técnicas, grita siempre."]])}
{C.caja("ojo", "Los rasgos se demuestran", "<p>Muchas veces el texto no dice «era honesto»: lo muestra con una acción, como <em>devolvió la cartera que encontró</em>. Usted tiene que deducir el rasgo a partir de lo que el personaje hace o dice. El GED pregunta mucho de esta manera.</p>")}
<h3>El conflicto: el motor de la historia</h3>
<p>El <strong>conflicto</strong> es el problema que enfrenta el protagonista. Sin conflicto, nada cambia y no hay historia. Hay dos grandes clases:</p>
{C.tabla("Conflicto interno y externo", ["Clase", "Dónde ocurre", "Ejemplo"],
         [["🧠 Interno", "Dentro del personaje: miedo, duda, culpa, indecisión.", "Ana tiene miedo de hablar en público, pero debe dar un discurso."],
          ["🌪️ Externo", "Fuera del personaje: contra otra persona, la naturaleza, la sociedad o una circunstancia.", "Pedro pierde el trabajo y tiene que conseguir dinero para la renta."]])}
{C.caja("ojo", "Pueden ir juntos", "<p>Una misma historia puede tener los dos: un personaje lucha contra una tormenta (externo) y, al mismo tiempo, contra su propio miedo (interno).</p>")}
{P("Compruebe", "<em>Rosa no sabe si aceptar un trabajo nuevo o quedarse donde está.</em> ¿Qué conflicto es?", ["Interno", "Externo"], 0, {}, "<strong>Interno</strong>: la duda ocurre dentro de Rosa.")}
{P("Compruebe", "<em>Siempre ayuda a sus vecinos sin pedir nada a cambio.</em> ¿Qué clase de rasgo es?", RTIPOS, 1,
   {0: "No dice cómo se ve.", 2: "No dice cómo habla."}, "Es un rasgo <strong>de personalidad</strong>: generoso, servicial.")}"""

    cuento = "".join(f"<p>{p}</p>" for p in MARTA)
    s3 = f"""<h3>Lectura: «El día que Marta se atrevió»</h3>
<div class="texto-lectura">{cuento}</div>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Haga el <strong>mapa de personaje</strong> de Marta: divida una hoja en cuatro cuadros y escriba, con sus palabras, (1) rasgos físicos y datos, (2) rasgos de personalidad, (3) el conflicto que enfrenta y (4) el cambio o la resolución.</p></div>
<details class="caja caja-tip"><summary><strong>Ya hice mi mapa: ver un modelo</strong></summary>
<ul><li><strong>Datos:</strong> tiene cuarenta años, limpia casas y vive en un barrio de Chicago. El cuento no describe su cara ni su cuerpo.</li>
<li><strong>Personalidad:</strong> callada, trabajadora, educada; quiere aprender, pero es insegura.</li>
<li><strong>Conflicto:</strong> sobre todo interno, el miedo a equivocarse.</li>
<li><strong>Cambio:</strong> se inscribe en la clase y se presenta en voz alta. Vence su miedo, aunque sea con tres palabras.</li></ul>
<p>Sus palabras pueden ser otras. Lo importante es que cada idea se pueda comprobar en el cuento. ¿Se fijó en doña Elena? Es la mentora de Marta.</p></details>
{P("Compruebe", "En el cuento, ¿qué papel cumple <strong>doña Elena</strong>?", ROLES, 2, {0: "La historia gira alrededor de Marta.", 1: "Doña Elena no se opone: la anima."}, "Es la <strong>mentora</strong>: anima a Marta a empezar.")}
{P("Compruebe", "¿Qué frase del cuento muestra que Marta es <strong>insegura</strong>?", ["«el cuaderno temblando entre las manos»", "«trabajaba limpiando casas»", "«Tenía cuarenta años»"], 0,
   {1: "Es un dato de su trabajo, no de cómo se siente.", 2: "Es un dato de su edad."}, "<strong>«el cuaderno temblando entre las manos»</strong>: el nerviosismo muestra la inseguridad.")}"""

    secciones = [("s1", "Los personajes y sus papeles", s1), ("s2", "Rasgos y conflictos", s2), ("s3", "Práctica: el mapa de personaje", s3)]
    tarea = [("El mapa de un personaje que conoce.", "Piense en una película, una serie, una telenovela o un cuento que le guste. Haga en su cuaderno el mapa de su protagonista, con los cuatro cuadros de la sección 3."),
             ("Rasgos con pruebas.", "Escriba al menos tres rasgos de personalidad y, junto a cada uno, una acción del personaje que lo demuestre."),
             ("El que se opone.", "Escriba una oración que diga quién es el antagonista o qué fuerza se opone al protagonista, y si el conflicto es interno, externo o los dos."),
             ("Compártalo.", "Si alguien de su casa conoce la misma historia, cuéntele su mapa y pregúntele si está de acuerdo.")]
    quiz = [
        ("¿Qué tres cosas se miran al analizar a un personaje?", ["Su papel, sus rasgos y su conflicto", "Su nombre, su edad y su ciudad", "El título, el autor y el final"], 0, {1: "Son datos, no un análisis.", 2: "Eso es del libro, no del personaje."}, "<strong>Papel, rasgos y conflicto.</strong>"),
        ("¿Quién es el <strong>protagonista</strong>?", ["El personaje principal, que enfrenta el conflicto", "El que se opone al principal", "El que da consejos"], 0, {1: "Ese es el antagonista.", 2: "Ese es el mentor."}, "El <strong>personaje principal</strong>."),
        ("¿El antagonista tiene que ser una persona mala?", ["No: puede ser un rival, una autoridad o la naturaleza", "Sí, siempre es malvado", "Sí, y siempre es un animal"], 0, {1: "Puede ser una tormenta o el cansancio.", 2: "No."}, "<strong>No</strong>: es lo que se opone, sea lo que sea."),
        ("¿Quién es el <strong>mentor</strong>?", ["El que guía y aconseja al protagonista", "El personaje más joven", "El enemigo del protagonista"], 0, {1: "La edad no importa.", 2: "Ese es el antagonista."}, "El que <strong>guía y aconseja</strong>."),
        ("«Honesto, tímido y generoso» son rasgos…", ["de personalidad", "físicos", "de la forma de hablar"], 0, {1: "No dicen cómo se ve.", 2: "No dicen cómo habla."}, "<strong>De personalidad.</strong>"),
        ("«Alto, de pelo canoso y con anteojos» son rasgos…", ["físicos", "de personalidad", "de la forma de hablar"], 0, {1: "Dicen cómo se ve, no cómo es por dentro.", 2: "No dicen cómo habla."}, "<strong>Físicos.</strong>"),
        ("Un conflicto <strong>interno</strong> ocurre…", ["dentro del personaje: miedo, duda, culpa", "entre dos países", "siempre contra la naturaleza"], 0, {1: "Eso es externo.", 2: "Eso es externo."}, "<strong>Dentro</strong> del personaje."),
        ("«Un huracán destruye la casa de la familia Pérez.» ¿Qué conflicto es?", ["Interno", "Externo"], 1, {}, "<strong>Externo</strong>: contra la naturaleza."),
        ("En el cuento de Marta, ¿cuál es su conflicto principal?", ["El miedo a equivocarse", "Una tormenta", "Un jefe injusto"], 0, {1: "No hay tormenta en el cuento.", 2: "El cuento no habla de un jefe."}, "<strong>El miedo a equivocarse</strong>: un conflicto interno."),
        ("¿Por qué importa el conflicto en una historia?", ["Pone en marcha la historia y hace cambiar al personaje", "Hace la historia más corta", "Presenta a todos los personajes"], 0, {1: "No tiene que ver con el largo.", 2: "Eso no es el conflicto."}, "Es el <strong>motor</strong> de la historia."),
    ]
    filas = [
        ("Papeles", "Distingo protagonista, antagonista y mentor en cualquier historia.", "Confundo a veces el antagonista cuando no es una persona.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Rasgos", "Deduzco rasgos de lo que el personaje hace y dice.", "Solo veo los rasgos que el texto dice directamente.", "No sé qué es un rasgo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Conflicto", "Digo si es interno o externo y por qué.", "Lo encuentro, pero no sé clasificarlo.", "No lo encuentro (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe mirar a los personajes como lo pide el GED: qué papel cumplen, cómo son y qué problema enfrentan. En la próxima lección verá dónde y cuándo pasa la historia: <strong>el escenario</strong>.</p>"
    glosario = [("Personaje", "Persona, animal o ser a quien le pasan las cosas en una historia."), ("Protagonista", "Personaje principal."), ("Antagonista", "Personaje o fuerza que se opone al protagonista."),
                ("Mentor", "Personaje que guía o ayuda al protagonista."), ("Rasgo", "Característica física, de personalidad o de la forma de hablar."),
                ("Conflicto", "Problema que enfrenta el protagonista: interno (dentro) o externo (fuera).")]
    conexion = ("<p>En el Tema 4 aprendió estrategias para entender lo que lee. Ahora va a usarlas para leer historias. Toda historia empieza con alguien a quien le pasa algo: los personajes.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una película, serie o cuento que conozca bien.</p>")
    estd = LE.estandares(["R.3.2"], base=["R.3.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Sin conflicto, el personaje no cambia y no hay historia.", ["R.3.2 · Personajes", "Texto narrativo"],
                            ["<strong>Distinguir</strong> el protagonista, el antagonista y el mentor.", "<strong>Describir</strong> los rasgos de un personaje con pruebas del texto.",
                             "<strong>Diferenciar</strong> el conflicto interno del externo.", "<strong>Hacer</strong> el mapa de un personaje."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-2", LE.titulo("5-2")), glosario, P)


def practica():
    rol = [{"enun": f"<div class=\"texto-lectura\"><p>{h}</p></div>¿Qué papel cumple <strong>{w}</strong>?", "ops": ROLES, "ok": k, "enOrden": True,
            "pista": "Protagonista: a quien le pasa la historia. Antagonista: lo que se le opone. Mentor: quien lo ayuda o aconseja.",
            "exp": f"<strong>{w[0].upper() + w[1:]}</strong>: {['es el centro de la historia', 'se opone al protagonista', 'guía o ayuda al protagonista'][k]}."} for h, ps in HISTORIAS for w, k in ps]
    ras = [{"enun": f"<strong>{r}</strong><br>¿Qué clase de rasgo es?", "ops": RTIPOS, "ok": k, "enOrden": True, "pista": "Físico: cómo se ve. Personalidad: cómo es o cómo actúa. Forma de hablar: qué dice y cómo.",
            "exp": f"Es un rasgo <strong>{RTIPOS[k].lower()}</strong>."} for r, k in RASGOS]
    con = [{"enun": f"<strong>{c}</strong><br>¿El conflicto es interno o externo?", "ops": ["Interno", "Externo"], "ok": k, "enOrden": True, "pista": "¿La lucha ocurre dentro del personaje o contra algo de afuera?",
            "exp": ["La lucha ocurre <strong>dentro</strong> del personaje.", "La lucha es contra algo de <strong>afuera</strong>."][k]} for c, k in CONFLICTOS]
    mods = [("papeles", "¿Qué papel cumple?", C.om("m1", "Lea la historia y decida el papel de cada personaje.")),
            ("rasgos", "¿Qué clase de rasgo es?", C.om("m2", "Físico, de personalidad o de la forma de hablar.")),
            ("conflictos", "¿Interno o externo?", C.om("m3", "¿La lucha ocurre dentro del personaje o contra algo de afuera?"))]
    js = C.js_datos("ROL", rol) + C.js_datos("RAS", ras) + C.js_datos("CON", con) + 'creaBanco("m1", ROL);\ncreaBanco("m2", RAS);\ncreaBanco("m3", CON);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
