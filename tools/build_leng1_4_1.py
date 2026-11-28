# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.1 · Predecir y preguntar antes de leer.
Fuente: clases_leng1/clase_4-1.html (GEDparaHispanos), adaptada al marco de LearnGED.
Uso: python3 tools/build_leng1_4_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "4-1"
CAJA1 = ["Un domingo, Lucía ayudaba a su abuela a ordenar el armario. En el fondo encontró una caja de madera vieja, con una cerradura pequeña. Junto a la caja había una llave dorada.",
         "—¿Puedo abrirla? —preguntó Lucía.", "—Sí, pero con cuidado: la madera está frágil y se puede romper —contestó la abuela."]
CAJA2 = ["Adentro había cartas, fotos en blanco y negro y un pañuelo bordado con flores azules. Las cartas eran del abuelo, que había trabajado muchos años lejos de casa. En cada carta, él le contaba a la abuela cómo era su vida en otro país y cuánto la extrañaba. Lucía y su abuela leyeron las cartas toda la tarde, entre risas y lágrimas. Esa noche, las dos decidieron guardar la caja como el tesoro de la familia."]
MOMENTOS = [("Miro el título y las imágenes.", 0), ("Me pregunto: «¿de qué tratará?»", 0), ("Pienso qué sé ya del tema.", 0), ("Escribo una predicción.", 0),
            ("Releo una oración que me confundió.", 1), ("Busco pistas para entender una palabra.", 1), ("Compruebo si mi predicción va bien.", 1), ("Me detengo en una parada para pensar.", 1),
            ("Cuento con mis palabras de qué se trató.", 2), ("Reviso si se respondió mi pregunta.", 2), ("Escribo un resumen corto.", 2), ("Decido si confirmé, ajusté o rechacé mi predicción.", 2)]
PREDICCIONES = [
    ("«Cómo ahorrar en el supermercado»", "🛒", ["Va a dar consejos para gastar menos al hacer las compras.", "Va a contar la historia de un supermercado famoso.", "Va a explicar cómo se siembran las verduras."], 0),
    ("«El día que se fue la luz en el barrio»", "🕯️", ["Va a explicar cómo funciona la electricidad en las plantas.", "Va a contar qué pasó en un barrio cuando no hubo electricidad.", "Va a dar recetas de cocina."], 1),
    ("«Diez frutas que ayudan al corazón»", "🍎❤️", ["Va a hablar de enfermedades de los pulmones.", "Va a contar la vida de un médico.", "Va a nombrar frutas buenas para la salud del corazón."], 2),
    ("«Cómo preparar una entrevista de trabajo»", "👔", ["Va a dar pasos para prepararse antes de una entrevista.", "Va a contar cómo se fabrica la ropa formal.", "Va a explicar las leyes de inmigración."], 0),
    ("«Los huracanes del Caribe: cuando la naturaleza ruge»", "🌀", ["Va a hablar de los leones del zoológico.", "Va a explicar el daño que causan los huracanes en las islas.", "Va a dar consejos para viajar en avión."], 1),
    ("«Mi primer día en Chicago»", "🏙️", ["Va a explicar la historia de los rascacielos.", "Va a contar lo que vivió alguien al llegar a Chicago.", "Va a dar el pronóstico del tiempo."], 1),
    ("«Cinco errores al manejar en la nieve»", "🚗❄️", ["Va a advertir sobre lo que no se debe hacer al manejar con nieve.", "Va a enseñar a esquiar.", "Va a contar cómo se forma la nieve en las nubes."], 0),
    ("«La receta secreta de mi abuela»", "🍲", ["Va a explicar cómo se guarda un secreto.", "Va a hablar de los abuelos en general.", "Va a contar cómo se prepara un plato familiar."], 2),
]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>La comprensión no empieza con la primera palabra del texto: empieza <strong>antes</strong>. El buen lector trabaja en tres momentos, y cada uno tiene su estrategia:</p>
{C.tabla("Los tres momentos del buen lector", ["Momento", "Qué hace", "Qué se pregunta"],
         [["🔍 Antes", "Predice y pregunta", "¿De qué tratará?"], ["📖 Durante", "Aclara dudas", "¿Qué significa esto?"], ["✍️ Después", "Resume", "¿De qué se trató?"]])}
<p>Esta lección trabaja el primero. La próxima, los otros dos.</p>
{C.caja("tip", "Predecir no es adivinar", "<p>Una <strong>predicción</strong> es una anticipación lógica basada en pistas reales que el texto da antes de empezar: el título, las imágenes, las palabras destacadas. Cuando predice, su cabeza se prepara para entender.</p>")}
<p>Predecir ayuda porque lo mantiene atento (querrá saber si acertó), le da un objetivo a la lectura, despierta lo que ya sabe del tema y convierte la lectura en una conversación con el texto.</p>
{P("Compruebe", "¿Qué es una <strong>predicción</strong>?", ["Una adivinanza al azar", "Una anticipación basada en pistas del texto", "El resumen del final"], 1,
   {0: "Adivinar es decir cualquier cosa sin pistas.", 2: "El resumen se hace después de leer."}, "Es una <strong>anticipación lógica</strong> con pistas del título, las imágenes o las palabras destacadas.")}"""

    s2 = f"""<p>Antes de leer la primera oración, el lector detective ya tiene tres fuentes de pistas:</p>
{C.tabla("Dónde buscar las pistas", ["Pista", "Qué observar", "Qué le dice"],
         [["🏷️ El título", "Las palabras del título y del subtítulo", "El tema general"], ["🖼️ Las imágenes", "Fotos, dibujos, gráficas, mapas", "El contexto y la emoción del texto"],
          ["🔤 Las palabras destacadas", "Palabras en negrita, en cursiva o en subtítulos", "Los conceptos clave"]])}
{C.ejemplo("Pensar en voz alta: una lectora predice", [
    ("1", "Lee el título: <em>«Los huracanes del Caribe: cuando la naturaleza ruge»</em>. Ve una imagen: una palmera doblada por el viento y el cielo gris."),
    ("2", "Piensa: «Veo <em>huracanes</em> y <em>Caribe</em>. Sé que en el Caribe hay temporada de huracanes de junio a noviembre. <em>Cuando la naturaleza ruge</em> suena fuerte, peligroso»."),
    ("3", "<strong>Predicción:</strong> «Este texto va a hablar del daño que causan los huracanes en las islas del Caribe»."),
    ("4", "<strong>Pregunta:</strong> «¿Cuál ha sido el huracán más fuerte del Caribe?»")],
    "Usó dos pistas (el título y la imagen) y lo que ya sabía.")}
{C.tabla("Frases para empezar una predicción", ["Frase", "Ejemplo"],
         [["El título me sugiere que…", "…se tratará de cómo ahorrar dinero."], ["La palabra ___ me hace pensar en…", "La palabra <em>receta</em> me hace pensar en ingredientes y pasos."],
          ["Creo que el texto va a explicar…", "…por qué dormir es importante."], ["Después de leer espero saber…", "…cómo se prepara una sopa de pollo."]])}
{C.caja("ojo", "La regla del detective", "<p>Toda predicción se justifica con al menos una pista. Si no puede decir «pienso esto porque vi…», no es una predicción: es una adivinanza.</p>")}
{P("Compruebe", f"<span class=\"emoji-grande\" aria-hidden=\"true\">🛒</span>Título: <em>«Cómo ahorrar en el supermercado»</em>. ¿Cuál es la mejor predicción?",
   ["Va a contar la historia de un supermercado famoso.", "Va a dar consejos para gastar menos al hacer las compras.", "Va a explicar cómo se siembran las verduras."], 1,
   {0: "El título dice «cómo ahorrar», no «la historia de».", 2: "El título no habla de sembrar."}, "Las pistas <em>cómo</em> y <em>ahorrar</em> anuncian <strong>consejos para gastar menos</strong>.")}"""

    s3 = f"""<p>Ahora con un cuento de verdad. Tiene dos paradas: en cada una, deténgase y escriba en su cuaderno antes de seguir.</p>
<h3>«La caja de la abuela»</h3>
<p class="emoji-grande" aria-hidden="true">📦🗝️</p>
<p class="nota-fina">Imagen: una caja de madera vieja sobre una mesa, con una llave pequeña y dorada al lado.</p>
<div class="caja caja-ojo"><span class="etiqueta et-ambar">🛑 Parada 1 · Antes de leer</span>
<p>Mire solo el título y la imagen. Escriba en su cuaderno:</p>
<ul><li>Una predicción: «Creo que el cuento va a tratar de…»</li><li>Una pregunta que espera que el cuento responda: «¿Qué habrá…?», «¿Por qué…?»</li><li>La pista que usó: el título, la imagen o las dos.</li></ul></div>
<details class="caja caja-tip"><summary><strong>Ya escribí mi predicción: leer la primera parte</strong></summary>
<div class="texto-lectura">{"".join(f"<p>{x}</p>" for x in CAJA1)}</div>
<p>{LE.escuchar(" ".join(CAJA1).replace("—", " "), "Escuchar", 0.85)}</p>
<div class="caja caja-ojo"><span class="etiqueta et-ambar">🛑 Parada 2 · Durante la lectura</span>
<ul><li>¿Su predicción va bien? ¿La confirma, la ajusta o la rechaza?</li><li>Escriba una predicción nueva: ¿qué cree que hay dentro de la caja?</li></ul></div>
<details class="caja caja-tip"><summary><strong>Leer la segunda parte</strong></summary>
<div class="texto-lectura">{"".join(f"<p>{x}</p>" for x in CAJA2)}</div>
<p>{LE.escuchar(" ".join(CAJA2), "Escuchar", 0.85)}</p>
<div class="caja caja-ojo"><span class="etiqueta et-ambar">🛑 Al terminar</span>
<ul><li>¿Se respondió su pregunta de la Parada 1?</li><li>¿En qué acertó y qué le sorprendió?</li></ul></div>
</details></details>
<h3>Confirmar, ajustar o rechazar</h3>
<p>Una predicción no es una respuesta final: es una hipótesis. Mientras lee, compárela con lo que el texto dice. Hay tres resultados, y los tres son buenos:</p>
<ul><li>✅ <strong>Confirmar:</strong> el texto coincide con lo que pensaba.</li><li>🔄 <strong>Ajustar:</strong> el texto cambia un poco lo que pensaba.</li><li>❌ <strong>Rechazar:</strong> el texto va por otro camino.</li></ul>
{C.caja("tip", "No se frustre si falla", "<p>Lo importante no es acertar, sino seguir pensando mientras lee. Una predicción rechazada significa que aprendió algo nuevo.</p>")}
<p>En la Lección 4.2 volverá a este cuento para aclarar sus palabras difíciles y resumirlo.</p>"""

    secciones = [("s1", "El ciclo de la lectura activa", s1), ("s2", "Las pistas del lector detective", s2), ("s3", "Lectura guiada: «La caja de la abuela»", s3)]
    tarea = [("Mis tres preguntas.", "Copie en limpio lo que escribió en las paradas del cuento: su predicción, su pregunta y la pista que usó. Lo completará en la Lección 4.2."),
             ("Un texto de su vida.", "Busque un texto corto de verdad (una noticia, un aviso, un folleto). Antes de leerlo, mire el título y las imágenes y escriba una predicción y una pregunta. Después léalo y anote si confirmó, ajustó o rechazó su predicción."),
             ("Frases modelo.", "Escriba predicciones para estos títulos con las frases de la sección 2: <em>«Cómo preparar una entrevista de trabajo»</em>, <em>«El día que se fue la luz en el barrio»</em> y <em>«Diez frutas que ayudan al corazón»</em>.")]
    quiz = [
        ("¿Cuáles son los tres momentos del buen lector?", ["Antes, durante y después de leer", "Mañana, tarde y noche", "Leer, copiar y memorizar"], 0, {1: "No se trata de la hora del día.", 2: "Copiar y memorizar no son estrategias de comprensión."}, "<strong>Antes, durante y después</strong>."),
        ("¿Qué se hace <strong>antes</strong> de leer?", ["Resumir", "Predecir y preguntar", "Aclarar palabras"], 1, {0: "Se resume después.", 2: "Se aclara durante la lectura."}, "<strong>Predecir y preguntar</strong>."),
        ("¿Cuáles son las tres pistas del lector detective?", ["El título, las imágenes y las palabras destacadas", "El precio, el autor y el número de páginas", "Las comas, los puntos y las mayúsculas"], 0, {1: "Eso no dice de qué trata el texto.", 2: "Eso es puntuación."}, "<strong>Título, imágenes y palabras destacadas.</strong>"),
        ("¿En qué se diferencia una predicción de una adivinanza?", ["La predicción se apoya en pistas", "No hay diferencia"], 0, {}, "La predicción se <strong>apoya en pistas</strong>."),
        ("Título: <em>«Cinco errores al manejar en la nieve»</em>. ¿Mejor predicción?", ["Va a enseñar a esquiar.", "Va a advertir lo que no se debe hacer al manejar con nieve.", "Va a explicar cómo se forma la nieve."], 1, {0: "El título habla de manejar, no de esquiar.", 2: "El título habla de errores al manejar."}, "Las pistas <em>errores</em> y <em>manejar</em> lo dicen."),
        ("Si su predicción no se confirma, ¿qué significa?", ["Que leyó mal", "Que aprendió algo nuevo: la ajusta o la rechaza"], 1, {}, "Es normal: <strong>se ajusta o se rechaza</strong>, y se aprende."),
        ("¿Cuál es una buena pregunta antes de leer?", ["¿Qué habrá dentro de la caja?", "¿Cuántas letras tiene el título?"], 0, {}, "Una pregunta sobre el <strong>contenido</strong>, que la lectura puede responder."),
        ("¿Qué frase sirve para empezar una predicción?", ["El título me sugiere que…", "Había una vez…", "En conclusión…"], 0, {1: "Así empiezan los cuentos.", 2: "Así se cierra un texto."}, "<strong>El título me sugiere que…</strong>"),
        ("¿Por qué ayuda predecir?", ["Porque prepara la cabeza para entender y da un objetivo a la lectura", "Porque así se lee más rápido sin entender"], 0, {}, "Prepara para entender y <strong>da un objetivo</strong>: confirmar o no."),
        ("En «La caja de la abuela», ¿qué había dentro de la caja?", ["Dinero y joyas", "Cartas, fotos y un pañuelo bordado", "Herramientas viejas"], 1, {0: "Lea otra vez la segunda parte.", 2: "Lea otra vez la segunda parte."}, "<strong>Cartas del abuelo, fotos y un pañuelo bordado.</strong>"),
    ]
    filas = [
        ("Predecir con pistas", "Hago predicciones y digo qué pista usé.", "Predigo, pero no siempre sé decir la pista.", "Adivino sin mirar las pistas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Preguntar antes de leer", "Escribo preguntas abiertas que el texto puede responder.", "Mis preguntas se responden con sí o no.", "No sé qué preguntar (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Confirmar, ajustar o rechazar", "Comparo mi predicción con el texto mientras leo.", "Lo hago solo al final.", "Me olvido de mi predicción (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe qué hacer antes de leer. En la próxima lección completará el ciclo: qué hacer <strong>durante</strong> la lectura cuando algo no se entiende, y cómo <strong>resumir</strong> al terminar.</p>"
    glosario = [("Predicción", "Anticipación lógica de lo que dirá un texto, basada en pistas."), ("Pista", "Algo del texto que ayuda a anticipar: el título, una imagen, una palabra destacada."),
                ("Conocimiento previo", "Lo que usted ya sabe de un tema antes de leer."), ("Hipótesis", "Idea que se comprueba después: se confirma, se ajusta o se rechaza.")]
    conexion = ("<p>Empieza el Tema 4: la <strong>comprensión</strong>, entender de verdad lo que lee. Ya sabe leer las palabras; ahora va a aprender a pensar con ellas. Todo empieza antes de leer, mirando el título y las imágenes.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un texto corto de su vida diaria (una noticia, un aviso, un folleto).</p>")
    estd = LE.estandares(["R.2.1"], base=["R.2.7", "R.5.1"])
    return C.pagina_leccion(N, LE.titulo(N), "La comprensión empieza antes de la primera palabra.", ["R.2 · Ideas centrales", "Comprensión"],
                            ["<strong>Usar</strong> el título, las imágenes y las palabras destacadas para predecir de qué tratará un texto.", "<strong>Formular</strong> preguntas que guíen la lectura.",
                             "<strong>Distinguir</strong> una predicción razonable de una adivinanza.", "<strong>Confirmar, ajustar o rechazar</strong> una predicción mientras lee."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-2", LE.titulo("4-2")), glosario, P)


def practica():
    M = ["Antes de leer", "Durante la lectura", "Después de leer"]
    mom = [{"enun": f"<strong>{a}</strong><br>¿En qué momento lo hace el buen lector?", "ops": M, "ok": k, "enOrden": True,
            "pista": "Antes: predice y pregunta. Durante: aclara y comprueba. Después: resume y revisa.", "exp": f"<strong>{M[k]}</strong>."} for a, k in MOMENTOS]
    pre = [{"enun": f"<span class=\"emoji-grande\" aria-hidden=\"true\">{e}</span>Título: <em>{t}</em><br>¿Cuál es la predicción más razonable?", "ops": o, "ok": k,
            "pista": "Busque en el título las palabras que dicen de qué trata. La buena predicción se apoya en ellas.", "exp": f"<strong>{o[k]}</strong> Se apoya en las palabras del título."} for t, e, o, k in PREDICCIONES]
    preg = [("«La caja de la abuela»", ["¿Qué habrá dentro de la caja?", "¿De qué color es la página?", "¿Cuántas palabras tiene el título?"], 0),
            ("«Cómo ahorrar en el supermercado»", ["¿Qué trucos sirven para gastar menos?", "¿El supermercado está abierto?", "¿Quién escribió el título?"], 0),
            ("«El día que se fue la luz en el barrio»", ["¿Cuántas letras tiene barrio?", "¿Qué hicieron los vecinos sin electricidad?", "¿Es de día?"], 1),
            ("«Diez frutas que ayudan al corazón»", ["¿Me gustan las frutas?", "¿Qué frutas son y cómo ayudan?", "¿Son diez?"], 1)]
    pq = [{"enun": f"Título: <em>{t}</em><br>¿Cuál es la mejor pregunta para guiar la lectura?", "ops": o, "ok": k,
           "pista": "La mejor pregunta es abierta (qué, por qué, cómo) y el texto la puede responder.", "exp": f"<strong>{o[k]}</strong>"} for t, o, k in preg]
    mods = [("momentos", "¿Antes, durante o después?", C.om("m1", "Ubique cada acción del buen lector en su momento.")),
            ("predicciones", "La predicción más razonable", C.om("m2", "Elija la predicción que se apoya en las pistas del título y la imagen.")),
            ("preguntas", "La mejor pregunta", C.om("m3", "Elija la pregunta que mejor guía la lectura."))]
    js = (C.js_datos("MOM", mom) + C.js_datos("PRE", pre) + C.js_datos("PRG", pq) + 'creaBanco("m1", MOM);\ncreaBanco("m2", PRE);\ncreaBanco("m3", PRG);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
