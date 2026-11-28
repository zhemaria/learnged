# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 1.3 · Fluidez lectora.
Fuente: clases_leng1/clase_1-3.html (GEDparaHispanos). Ese archivo es hoy una copia de la Lección 1.3
del Nivel 2; aquí se adapta al Nivel 1 (principio del curso, textos y metas de este nivel).
Uso: python3 tools/build_leng1_1_3.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "1-3"

LLAMADA = [
    "El martes por la mañana sonó el teléfono en la casa de Marta. Era la secretaria de la escuela de adultos.",
    "—¿Hablo con la señora Marta Ruiz? —preguntó una voz amable.",
    "—Sí, soy yo. ¿Pasó algo?",
    "—No se preocupe, señora. La llamo porque su examen de lectura salió muy bien. Ya puede pasar al Nivel 2.",
    "Marta se quedó callada un momento. Después sonrió y dijo:",
    "—¡Qué alegría! Estudié todas las noches, después del trabajo, con mi cuaderno y mis libros.",
    "—Se nota —respondió la secretaria—. Las clases empiezan el lunes a las seis de la tarde. ¿Puede venir?",
    "—¡Claro que sí! Allí estaré.",
    "Cuando colgó, Marta llamó a su hija para contarle la noticia. Su hija gritó de alegría al otro lado de la línea. Esa noche, la familia cenó junta para celebrar, y Marta preparó su plato favorito: arroz con pollo.",
]
TEATRO = [{"q": "S", "t": "¿Hablo con la señora Marta Ruiz?"}, {"q": "M", "t": "Sí, soy yo. ¿Pasó algo?"},
          {"q": "S", "t": "No se preocupe, señora. La llamo porque su examen de lectura salió muy bien. Ya puede pasar al Nivel 2."},
          {"q": "M", "t": "¡Qué alegría! Estudié todas las noches, después del trabajo, con mi cuaderno y mis libros."},
          {"q": "S", "t": "Se nota. Las clases empiezan el lunes a las seis de la tarde. ¿Puede venir?"}, {"q": "M", "t": "¡Claro que sí! Allí estaré."}]
OTROS = [
    ("En la parada", ["Son las siete de la mañana. Rosa espera el autobús en la esquina. Hace frío, y ella lleva un café caliente en la mano.",
                      "—¿Ya pasó el autobús de las siete? —le pregunta a un señor.", "—No, todavía no. Siempre llega tarde los lunes.",
                      "Rosa sonríe. Saca su libro de la bolsa y empieza a leer. Cuando levanta la vista, ¡el autobús ya está ahí!"]),
    ("La receta de la abuela", ["Mi abuela hace el mejor arroz con leche del barrio. Primero lava el arroz y lo pone a hervir con agua, canela y un poco de sal.",
                                "Después agrega la leche, el azúcar y la cáscara de un limón. Lo mueve despacio, sin parar, durante media hora.",
                                "Al final, sirve el arroz en tazas pequeñas. ¡Qué rico huele la cocina!"]),
    ("Un mensaje de la escuela", ["Estimados padres: el viernes no habrá clases, porque los maestros tienen una reunión. Las clases siguen el lunes a la hora de siempre.",
                                  "Recuerden firmar la nota de la excursión. ¿Tienen preguntas? Llamen a la oficina de la escuela.", "Gracias por su apoyo."]),
]


def texto_lectura(tid, parrafos):
    return f'<div class="texto-lectura" id="{tid}">' + "".join(f"<p>{p}</p>" for p in parrafos) + "</div>"


def crono(cid, tid):
    return f'''<div class="crono" id="{cid}" data-texto="{tid}">
<p class="crono-reloj" id="{cid}-tiempo" aria-live="off">0:00</p>
<p><button type="button" class="btn" id="{cid}-empezar">Empezar</button> <button type="button" class="btn-sec" id="{cid}-terminar" disabled>Terminar</button></p>
<p class="fb" id="{cid}-res" role="status" aria-live="polite"></p>
{C.tabla("Resultados de mis pasadas", ["Pasada", "Tiempo", "Palabras por minuto"], [["—", "Todavía no hay pasadas.", ""]])}
<p>Los resultados se borran al cerrar la página. Anótelos en su cuaderno.</p>
</div>'''


def leccion():
    P = C.Practicas()
    demo = "Cada mañana, antes de ir al trabajo, preparo café y leo las noticias."
    s1 = f"""<p>Leer con <strong>fluidez</strong> no es leer lo más rápido posible. Es leer como si hablara: con naturalidad. Cuando la lectura fluye, la mente queda libre para entender lo que dice el texto, en lugar de gastar toda su energía en descifrar cada palabra. La fluidez tiene tres partes:</p>
{C.tabla("Las tres partes de la fluidez", ["Parte", "Qué significa", "Un error típico"],
         [["Precisión", "Leer cada palabra tal como está escrita.", "Saltarse palabras o cambiar <em>casa</em> por <em>cosa</em>."],
          ["Ritmo", "Leer a una velocidad cómoda: ni muy lenta ni atropellada.", "Leer palabra por palabra, como un robot, o tan rápido que no se entiende."],
          ["Expresión", "Hacer las pausas y dar a la voz el tono que pide el texto.", "Leer una pregunta como si fuera una afirmación."]])}
<h3>Escuche la diferencia</h3>
<p>Estas dos lecturas tienen las mismas palabras: <em>«{demo}»</em> ¿Cuál se entiende mejor?</p>
{LE.AVISO_VOZ}
<p><button type="button" class="btn-voz" data-hablar-palabras="{demo}"><span aria-hidden="true">🔊</span> Lectura palabra por palabra</button>
<button type="button" class="btn-voz" data-hablar="{demo}" data-vel="0.9"><span aria-hidden="true">🔊</span> Lectura fluida</button></p>
{C.caja("tip", "Al principio es normal ir despacio", "<p>Si usted lee todavía palabra por palabra, no se preocupe: así empezamos todos. La fluidez se gana leyendo el mismo texto varias veces, como verá en la sección 4. En el Tema 2 trabajará además los sonidos y las sílabas, que hacen más fácil leer las palabras largas.</p>")}
{P("Compruebe", "Leer con fluidez significa…", ["Leer lo más rápido que se pueda", "Leer como si hablara, con naturalidad", "Leer siempre en voz muy alta"], 1,
   {0: "Si se lee muy rápido, se pierden palabras y no se entiende.", 2: "El volumen no es lo importante."}, "Fluidez es leer <strong>con naturalidad</strong>: precisión, ritmo y expresión.")}"""

    s2 = f"""<p>Los signos de puntuación son las <strong>señales de tránsito</strong> de la lectura: dicen dónde detenerse y cuánto.</p>
{C.tabla("Signos de puntuación y la pausa que piden", ["Signo", "Qué hace la voz"],
         [["Coma ( , )", "Una pausa breve, como para tomar aire."], ["Punto ( . )", "Una pausa más larga. La voz baja al final de la oración."],
          ["Punto y aparte", "La pausa más larga: empieza un párrafo nuevo, una idea nueva."], ["Dos puntos ( : )", "Una pausa que anuncia lo que viene: una lista, una explicación o lo que alguien dice."],
          ["Puntos suspensivos ( … )", "La voz queda en el aire, como si faltara algo por decir."]])}
<h3>Una coma cambia el significado</h3>
{C.tabla("Oraciones que solo se distinguen por una coma", ["Se escribe", "Quiere decir", "Escuche"],
         [["No, quiero agua.", "Primero dice que no a otra cosa; luego pide agua.", LE.escuchar("No, quiero agua.", "Escuchar", 0.8)],
          ["No quiero agua.", "No quiere agua.", LE.escuchar("No quiero agua.", "Escuchar", 0.8)],
          ["Juan, mi vecino vino.", "Le hablo a Juan para contarle que vino mi vecino.", LE.escuchar("Juan, mi vecino vino.", "Escuchar", 0.8)],
          ["Juan, mi vecino, vino.", "Vino Juan, que es mi vecino.", LE.escuchar("Juan, mi vecino, vino.", "Escuchar", 0.8)]])}
{P("Compruebe", "«María, la doctora, llamó.» ¿Qué quiere decir?", ["Le hablo a María para contarle que llamó la doctora.", "Llamó María, que es la doctora."], 1, {},
   "Las dos comas encierran una explicación: <strong>María es la doctora</strong>. Con una sola coma («María, la doctora llamó.») le estaría hablando a María.")}"""

    s3 = f"""<p>La <strong>entonación</strong> es la música de la voz: sube, baja o se hace más fuerte. En español, los signos de pregunta y de exclamación se escriben <strong>al principio y al final</strong>, para que usted sepa desde dónde cambiar el tono.</p>
{C.tabla("Tipos de oración y su entonación", ["Tipo", "Qué hace la voz", "Ejemplo"],
         [["Afirmación", "Baja al final.", "El autobús llegó tarde. " + LE.escuchar("El autobús llegó tarde.", "", 0.85)],
          ["Pregunta de sí o no", "Sube al final.", "¿El autobús llegó tarde? " + LE.escuchar("¿El autobús llegó tarde?", "", 0.85)],
          ["Pregunta con qué, dónde, cuándo, quién, cómo", "Empieza alta en esa palabra y baja al final.", "¿Cuándo llegó el autobús? " + LE.escuchar("¿Cuándo llegó el autobús?", "", 0.85)],
          ["Exclamación", "Más fuerza y emoción.", "¡El autobús llegó tarde otra vez! " + LE.escuchar("¡El autobús llegó tarde otra vez!", "", 0.85)]])}
{C.caja("tip", "Mire antes de leer", "<p>Cuando vea <strong>¿</strong> o <strong>¡</strong>, prepare la voz desde esa palabra. Por eso en español el signo de apertura es obligatorio, aunque en inglés no exista.</p>")}
{P("Compruebe", "Usted quiere saber si su hijo ya terminó la tarea. ¿Qué escribe?", ["Terminaste la tarea.", "¿Terminaste la tarea?", "¡Terminaste la tarea!"], 1,
   {0: "Así lo cuenta, no lo pregunta. Usted no sabe la respuesta.", 2: "Eso expresa emoción o sorpresa, no una pregunta."}, "Es una pregunta de sí o no: <strong>¿Terminaste la tarea?</strong> La voz sube al final.")}"""

    s4 = f"""<p>La <strong>lectura repetida</strong> es la mejor manera de ganar fluidez: el mismo texto, varias veces, mejorando algo en cada pasada.</p>
<ol>
<li>Escuche el modelo mientras sigue el texto con la vista.</li>
<li>Primera pasada: pulse <strong>Empezar</strong>, lea en voz alta y pulse <strong>Terminar</strong> al llegar al final.</li>
<li>Repita dos veces más. En cada pasada intente mejorar una cosa: menos tropiezos, mejores pausas o más expresión.</li>
</ol>
<p><button type="button" class="btn-voz" data-hablar="{' '.join(LLAMADA).replace('—', ' ')}" data-vel="0.9"><span aria-hidden="true">🔊</span> Escuchar el modelo</button>
<button type="button" class="btn-voz" data-hablar="{' '.join(LLAMADA).replace('—', ' ')}" data-vel="0.7"><span aria-hidden="true">🔊</span> Más despacio</button>
<button type="button" class="btn-voz" data-callar><span aria-hidden="true">⏹</span> Detener</button></p>
<h3>La llamada</h3>
{texto_lectura("llamada", LLAMADA)}
{C.caja("tip", "La raya ( — )", "<p>En español, el diálogo se marca con raya. Cada raya al comienzo de una línea es una persona que habla; las rayas del medio encierran las palabras del narrador (<em>—preguntó una voz amable</em>). Al leer, cambie un poco la voz para cada personaje.</p>")}
<h3>Mis pasadas</h3>
{crono("c1", "llamada")}
{C.caja("ojo", "¿Cuánto es bueno?", "<p>Lo más importante es <strong>mejorar de una pasada a la siguiente sin perder precisión</strong>. Como orientación, al empezar este nivel es normal leer un texto como este a unas 40 o 60 palabras por minuto; al terminar el nivel, un buen objetivo es pasar de 60 con muy pocos tropiezos. Si lee más rápido pero se salta palabras, baje la velocidad.</p>")}
<h3>Evalúe su lectura</h3>
<p>Después de su tercera pasada, póngase un puntaje de 1 a 4 en cada fila y anótelo en su cuaderno. Si se grabó con el celular, escúchese antes de calificarse.</p>
{C.tabla("Rúbrica de fluidez", ["Criterio", "1 · Empezando", "2 · En camino", "3 · Bien", "4 · Muy bien"],
         [["Precisión", "Muchos tropiezos o cambios de palabras.", "Varios tropiezos.", "Uno o dos tropiezos.", "Lee todas las palabras como están."],
          ["Ritmo", "Palabra por palabra.", "Lento, con paradas largas.", "Casi siempre cómodo.", "Natural, como si hablara."],
          ["Pausas", "No respeta los signos.", "Respeta algunos puntos.", "Respeta puntos y comas.", "Respeta todos los signos."],
          ["Expresión", "Voz plana en todo el texto.", "Algo de entonación.", "Preguntas y exclamaciones bien marcadas.", "Distingue también a cada personaje."]])}"""

    s5 = f"""<p>Ahora usted es Marta. La computadora hace la voz de la secretaria. Cuando le toque, su línea se ilumina en naranja: léala en voz alta con la entonación que piden los signos y pulse <strong>Ya leí mi parte</strong>.</p>
<div class="teatro" id="t1" data-lineas='{json.dumps(TEATRO, ensure_ascii=False)}' data-yo="M" data-nombres='{json.dumps({"S": "Secretaria (la computadora)", "M": "Marta (usted)"}, ensure_ascii=False)}'>
<div class="teatro-lineas"></div>
<p><button type="button" class="btn" id="t1-empezar">Empezar</button> <button type="button" class="btn-sec" id="t1-sigue" disabled>Ya leí mi parte</button> <button type="button" class="btn-sec" id="t1-reiniciar">Volver al principio</button></p>
<p class="fb" id="t1-estado" role="status" aria-live="polite"></p>
</div>
{C.caja("tip", "Si tiene con quién practicar", "<p>Lean el diálogo entre dos personas, sin la computadora, y luego cambien los papeles.</p>")}"""

    secciones = [("s1", "¿Qué es leer con fluidez?", s1), ("s2", "Las pausas de la puntuación", s2), ("s3", "La entonación: preguntas y exclamaciones", s3),
                 ("s4", "Lectura repetida: «La llamada»", s4), ("s5", "Teatro leído", s5)]
    tarea = [("Mi grabación.", "Elija un párrafo de un periódico, una revista o un libro. Léalo tres veces y grábese con el celular en la tercera, unos 45 segundos. Escúchese y califíquese con la rúbrica de la sección 4."),
             ("Mis velocidades.", "Copie en su cuaderno las palabras por minuto de sus tres pasadas de «La llamada». ¿Cuánto mejoró de la primera a la tercera?"),
             ("Escribo con entonación.", "Escriba un diálogo corto (seis líneas) entre usted y alguien de su familia, con al menos una pregunta y una exclamación, y con raya en cada línea. Léalo en voz alta.")]
    rob = "Cuando llegué a casa, mi hija ya había preparado la cena."
    quiz = [
        ("¿Cuáles son las tres partes de la fluidez?", ["Velocidad, volumen y memoria", "Precisión, ritmo y expresión", "Letras, sílabas y palabras"], 1, {0: "La velocidad sola no es fluidez, y el volumen no cuenta.", 2: "Eso son partes de las palabras, no de la lectura."}, "<strong>Precisión, ritmo y expresión.</strong>"),
        ("La <strong>coma</strong> pide…", ["La pausa más larga", "Que la voz suba", "Una pausa breve"], 2, {0: "La pausa más larga es la del punto y aparte.", 1: "La voz sube en las preguntas de sí o no."}, "Una <strong>pausa breve</strong>, como para tomar aire."),
        ("«No, quiero agua.» Quien lo dice…", ["Sí quiere agua", "No quiere agua"], 0, {}, "La coma separa el «no» de lo que pide: <strong>sí quiere agua</strong>."),
        ("En una pregunta de sí o no, al final la voz…", ["Baja", "Sube", "Se queda igual"], 1, {0: "Baja en las afirmaciones.", 2: "La voz plana suena a robot."}, "<strong>Sube</strong> al final."),
        ("¿Para qué sirve el signo <strong>¿</strong> al principio de la pregunta?", ["Avisa desde dónde empieza la pregunta", "Indica que la voz debe bajar", "Separa dos palabras largas"], 0, {1: "La voz sube o cambia en la pregunta.", 2: "Para separar palabras hay espacios y comas."}, "Avisa <strong>desde dónde</strong> cambiar el tono."),
        (f"Escuche esta lectura. ¿Cómo es? {LE.escuchar(rob, 'Escuchar', 0.9)}", ["Fluida", "Entrecortada, palabra por palabra"], 0, {}, "Es <strong>fluida</strong>: suena como alguien que habla."),
        (f'Escuche esta lectura. ¿Cómo es? <button type="button" class="btn-voz" data-hablar-palabras="{rob}"><span aria-hidden="true">🔊</span> Escuchar</button>', ["Fluida", "Entrecortada, palabra por palabra"], 1, {}, "Es <strong>entrecortada</strong>: cada palabra suena sola, como un robot."),
        ("En un diálogo escrito en español, la <strong>raya</strong> ( — ) indica…", ["Una pausa muy larga", "Que la oración es una pregunta", "Que habla un personaje"], 2, {0: "Las pausas las marcan la coma y el punto.", 1: "Las preguntas llevan ¿ ?."}, "La raya indica que <strong>habla un personaje</strong>."),
        ("¿Qué es la <strong>lectura repetida</strong>?", ["Leer el mismo texto varias veces para mejorar", "Leer muchos textos distintos muy rápido", "Repetir dos veces cada palabra al leer"], 0, {1: "La idea es volver al mismo texto.", 2: "Eso rompería el ritmo."}, "Leer <strong>el mismo texto varias veces</strong>, mejorando algo en cada pasada."),
        ("Ve humo en la cocina y quiere avisar con fuerza. ¿Qué escribe?", ["¿Se quema la comida?", "Se quema la comida.", "¡Se quema la comida!"], 2, {0: "No es una pregunta: usted lo está viendo.", 1: "Falta la fuerza del aviso."}, "<strong>¡Se quema la comida!</strong> La exclamación da fuerza."),
        ("Si lee muy rápido y se salta palabras, ¿qué parte de la fluidez falla?", ["El volumen", "La precisión", "La memoria"], 1, {0: "El volumen no es parte de la fluidez.", 2: "No se trata de recordar, sino de leer lo que está escrito."}, "Falla la <strong>precisión</strong>."),
    ]
    filas = [
        ("Precisión", "Leo todas las palabras como están, sin saltarme ninguna.", "Tropiezo en algunas palabras largas.", "Me salto o cambio palabras seguido (<a href=\"#s4\">repita la lectura de la sección 4</a>)."),
        ("Pausas", "Hago la pausa que pide cada signo: coma, punto y punto y aparte.", "Respeto los puntos, pero no siempre las comas.", "Leo de corrido sin pausas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Entonación", "Marco bien las preguntas y las exclamaciones.", "A veces leo una pregunta como afirmación.", "Mi voz suena igual en todo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 1: ya conoce las letras, sabe cómo se arma una oración y cómo leer un texto en voz alta con precisión, pausas y entonación.</p>"
              "<p>En el Tema 2 bajará a lo más pequeño de las palabras: los sonidos y las sílabas. Saber oírlos y unirlos es lo que hace posible leer con soltura cualquier palabra nueva.</p>")
    glosario = [("Fluidez", "Leer con precisión, a un ritmo cómodo y con expresión, como si se hablara."), ("Precisión", "Leer cada palabra tal como está escrita."),
                ("Entonación", "La subida y bajada de la voz al hablar o leer."), ("Raya ( — )", "Signo que marca en español lo que dice cada personaje en un diálogo."),
                ("Lectura repetida", "Leer el mismo texto varias veces para ganar fluidez."), ("Palabras por minuto", "Cuántas palabras se leen en un minuto; sirve para ver el avance de una pasada a otra.")]
    conexion = ("<p>Ya conoce las letras y sabe cómo se arma una oración. Ahora damos el paso que une todo: leer un texto completo en voz alta, como lo haría un buen lector. Cuando la lectura fluye, la cabeza queda libre para entender.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno, el volumen activado y, si puede, el celular para grabarse.</p>")
    estd = LE.estandares([], base=["L.2.4"], fund=["RF.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Leer no es correr: es leer como se habla.",
                            ["Fundamentos de lectura", "Fluidez"],
                            ["<strong>Leer en voz alta</strong> un texto de este nivel sin saltarse ni cambiar palabras.",
                             "<strong>Hacer las pausas</strong> que marcan la coma, el punto y el punto y aparte.",
                             "<strong>Usar la entonación</strong> de las preguntas, las exclamaciones y los diálogos.",
                             "<strong>Medir</strong> su avance con la lectura repetida y una rúbrica de fluidez."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-1", LE.titulo("2-1")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_coma():
    d = [("No, quiero café.", ["Pide café", "No quiere café"], 0, "La coma separa el «no» de lo que pide: sí quiere café."),
         ("No quiero café.", ["Pide café", "No quiere café"], 1, "Sin coma, el «no» niega: no quiere café."),
         ("María, la doctora llamó.", ["Le hablo a María", "María es la doctora"], 0, "Le cuento a María que llamó la doctora."),
         ("María, la doctora, llamó.", ["Le hablo a María", "María es la doctora"], 1, "Las dos comas encierran una explicación: María es la doctora."),
         ("Pedro, come.", ["Le pido a Pedro que coma", "Cuento que Pedro come"], 0, "La coma separa el nombre de la persona a quien se le habla."),
         ("Pedro come.", ["Le pido a Pedro que coma", "Cuento que Pedro come"], 1, "Sin coma, es una afirmación sobre Pedro."),
         ("Ana, mi hermana viene mañana.", ["Le hablo a Ana", "Ana es mi hermana"], 0, "Le aviso a Ana que viene mi hermana."),
         ("Ana, mi hermana, viene mañana.", ["Le hablo a Ana", "Ana es mi hermana"], 1, "Las comas encierran la explicación: Ana es mi hermana."),
         ("Sí, señor, ya pagué.", ["Responde que ya pagó", "Pregunta si ya pagó"], 0, "Es una respuesta: no lleva signos de pregunta.")]
    return [{"enun": f"<strong>«{s}»</strong> {LE.escuchar(s, 'Escuchar', 0.8)}<br>¿Qué quiere decir?", "ops": o, "ok": k, "exp": e, "enOrden": True} for s, o, k, e in d]


def banco_situacion():
    d = [("Quiere saber si su hijo ya terminó la tarea.", ["Terminaste la tarea.", "¿Terminaste la tarea?", "¡Terminaste la tarea!"], 1, "Es una pregunta de sí o no: la voz sube al final."),
         ("Le alegra que su hijo por fin haya terminado.", ["Terminaste la tarea.", "¿Terminaste la tarea?", "¡Terminaste la tarea!"], 2, "Hay emoción: es una exclamación."),
         ("Le cuenta a la maestra lo que hizo su hijo, sin emoción especial.", ["Terminó la tarea.", "¿Terminó la tarea?", "¡Terminó la tarea!"], 0, "Es una afirmación: la voz baja al final."),
         ("Ve llegar el autobús y avisa a su amiga con prisa.", ["Llegó el autobús.", "¿Llegó el autobús?", "¡Llegó el autobús!"], 2, "El aviso urgente es una exclamación."),
         ("Acaba de salir de la tienda y no sabe si el autobús ya pasó.", ["Ya pasó el autobús.", "¿Ya pasó el autobús?", "¡Ya pasó el autobús!"], 1, "No lo sabe: pregunta."),
         ("Quiere saber a qué hora abre la clínica.", ["¿A qué hora abre la clínica?", "La clínica abre temprano.", "¡Qué temprano abre la clínica!"], 0, "Pregunta con <em>qué</em>: la voz empieza alta y baja al final."),
         ("Le sorprende lo caro que está el pan.", ["El pan está caro.", "¿Está caro el pan?", "¡Qué caro está el pan!"], 2, "La sorpresa se escribe con exclamación."),
         ("Le explica a un compañero dónde queda el baño.", ["El baño está al fondo.", "¿El baño está al fondo?", "¡El baño está al fondo!"], 0, "Es información: una afirmación."),
         ("No recuerda dónde dejó las llaves y le pregunta a su esposo.", ["Dónde dejé las llaves.", "¿Dónde dejé las llaves?", "¡Dónde dejé las llaves!"], 1, "Es una pregunta con <em>dónde</em>, con tilde y con signos de pregunta.")]
    return [{"enun": f"<em>{s}</em><br>¿Qué escribe?", "ops": o, "ok": k, "exp": e, "pista": "¿Usted afirma algo, pregunta algo que no sabe o expresa una emoción fuerte?"} for s, o, k, e in d]


def banco_signos():
    d = [("la coma ( , )", "Una pausa breve, como para tomar aire."), ("el punto ( . )", "Una pausa más larga; la voz baja al final."),
         ("el punto y aparte", "La pausa más larga: empieza una idea nueva."), ("los dos puntos ( : )", "Una pausa que anuncia lo que viene."),
         ("los puntos suspensivos ( … )", "La voz queda en el aire."), ("los signos ¿ ?", "La voz cambia porque es una pregunta."), ("los signos ¡ !", "La voz gana fuerza y emoción.")]
    b = []
    for i, (sig, que) in enumerate(d):
        otros = [d[(i + 2) % len(d)][1], d[(i + 4) % len(d)][1]]
        b.append({"enun": f"¿Qué hace la voz con <strong>{sig}</strong>?", "ops": [que] + otros, "ok": 0, "exp": f"Con {sig}: {que[0].lower() + que[1:]}",
                  "pista": "Piense en las señales de tránsito: ¿es una pausa corta, una pausa larga o un cambio de tono?"})
    return b


def practica():
    otros = "".join(f'<h3>{tit}</h3>\n<p><button type="button" class="btn-voz" data-hablar="{" ".join(ps).replace("—", " ")}" data-vel="0.85"><span aria-hidden="true">🔊</span> Escuchar el modelo</button></p>\n'
                    f'{texto_lectura("txt" + str(i), ps)}\n{crono("cr" + str(i), "txt" + str(i))}' for i, (tit, ps) in enumerate(OTROS, 1))
    mods = [
        ("pausas", "Las pausas cambian el sentido", C.om("m1", "Lea la oración (o escúchela) y elija qué quiere decir. Fíjese en las comas.")),
        ("entonacion", "Situación y entonación", C.om("m2", "Lea la situación y elija cómo se escribe lo que usted diría.")),
        ("signos", "Qué hace la voz con cada signo", C.om("m3", "Elija lo que hace la voz.")),
        ("lectura-repetida", "Lectura repetida con otros textos", f"      <p>Tres textos cortos para seguir practicando. Con cada uno: escuche el modelo, lea en voz alta tres veces con el cronómetro y compare sus palabras por minuto.</p>\n{LE.AVISO_VOZ}\n{otros}"),
    ]
    js = (C.js_datos("COMA", banco_coma()) + C.js_datos("SIT", banco_situacion()) + C.js_datos("SIG", banco_signos()) +
          'creaBanco("m1", COMA);\ncreaBanco("m2", SIT);\ncreaBanco("m3", SIG);\n')
    html = C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)
    return html


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
