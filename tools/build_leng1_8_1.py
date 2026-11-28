# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.1 · Fundamentos de la comunicación y escucha activa.
Fuente: clases_leng1/clase_8-1.html (GEDparaHispanos), adaptada al marco de LearnGED (sin práctica en gramatica: se escribió aquí).
Uso: python3 tools/build_leng1_8_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-1"
ESC = [("Mientras su hija le cuenta su día, Rosa mira el celular y dice «ajá» sin levantar la vista.", False, "Mira el celular: no presta atención."),
       ("El médico explica la receta. Pedro escucha y al final dice: «Entonces, tomo una pastilla cada ocho horas, ¿verdad?».", True, "Repite con sus palabras para confirmar: parafrasea."),
       ("En la reunión, Luis interrumpe a su compañera antes de que termine la idea.", False, "Interrumpir impide entender al otro."),
       ("Ana no entendió una palabra y pregunta: «¿Podría explicar qué significa “deducible”?».", True, "Pide aclaración en vez de fingir que entendió."),
       ("Carlos asiente con la cabeza y mira a su vecino mientras este le cuenta un problema.", True, "Contacto visual y asentir: buena escucha."),
       ("Mientras su compañero habla, Marta ya está pensando qué va a contestar y no oye el final.", False, "Pensar la respuesta mientras el otro habla impide escuchar."),
       ("La maestra pregunta algo y Jorge dice «sí, sí» aunque no entendió nada.", False, "Fingir que entendió produce malentendidos."),
       ("Lucía dice: «Si entendí bien, usted necesita el formulario firmado antes del viernes».", True, "Parafrasea para confirmar."),
       ("Raúl escucha a su hijo con los brazos cruzados y bostezando.", False, "La postura dice «no me interesa»."),
       ("Elena deja terminar a su esposo y luego dice: «Estoy de acuerdo, y quiero añadir que…».", True, "Espera su turno, muestra acuerdo y añade."),
       ("En la entrevista de trabajo, Pablo mira el reloj todo el tiempo.", False, "El gesto dice que tiene prisa o que no le interesa."),
       ("Sofía anota lo que dice la trabajadora social y pregunta lo que no le quedó claro.", True, "Anota y pide aclaración: escucha activa.")]
FUN = ["Mostrar acuerdo", "Añadir información", "Pedir aclaración", "Parafrasear"]
FRASES = [("Estoy de acuerdo con lo que dijo Ana.", 0), ("Tiene razón en que el horario es difícil.", 0), ("Comparto lo que usted piensa.", 0),
          ("Quiero añadir que también hay clases los sábados.", 1), ("A lo que dijo, agrego que la biblioteca tiene computadoras.", 1), ("También me parece importante el transporte.", 1),
          ("¿Puede explicar la última parte?", 2), ("No entendí bien lo del formulario.", 2), ("¿Podría repetir la fecha, por favor?", 2),
          ("Entonces, lo que usted dice es que no hay clase el lunes.", 3), ("Si entendí bien, usted prefiere estudiar de noche.", 3), ("O sea, que el examen es en marzo, ¿verdad?", 3)]
CANAL = ["Verbal", "No verbal", "Paraverbal"]
CAN = [("Las palabras «estoy de acuerdo».", 0), ("Cruzar los brazos.", 1), ("Hablar en voz muy baja.", 2), ("Asentir con la cabeza.", 1), ("Hablar muy rápido.", 2),
       ("Decir «no entendí».", 0), ("Mirar a los ojos.", 1), ("Subir el tono con enojo.", 2), ("Sonreír.", 1), ("Hacer una pausa antes de una idea importante.", 2), ("Escribir «gracias» en un mensaje.", 0)]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En los temas anteriores aprendió a leer y a escribir. Ahora completa el círculo con las dos destrezas que faltan: <strong>hablar y escuchar</strong>. Escuchar bien es tan importante como hablar bien: sin escuchar no se puede responder en una cita médica, una entrevista de trabajo o una reunión familiar.</p>
{C.tabla("El esquema de la comunicación", ["Papel", "Qué hace"], [["🗣️ Emisor", "Envía el mensaje."], ["👂 Receptor", "Recibe el mensaje."]])}
<p>En una conversación, los papeles se alternan todo el tiempo: cuando yo hablo soy emisor; cuando usted responde, el emisor es usted. Por eso la comunicación es <strong>de ida y vuelta</strong>.</p>
{C.caja("ojo", "Tres maneras de fallar", "<ul><li>Una persona habla todo el tiempo y no deja responder.</li><li>Quien escucha piensa en otra cosa.</li><li>Nadie pide aclaración cuando algo no se entiende, y sigue el malentendido.</li></ul>")}"""

    s2 = f"""{C.tabla("No es lo mismo oír que escuchar", ["Nivel", "Qué pasa", "Ejemplo"],
         [["👂 1 · Oír", "Los sonidos llegan, pero no se les presta atención.", "Oigo el tráfico de la calle."],
          ["🎧 2 · Escuchar", "Se presta atención a un sonido para entenderlo.", "Escucho la radio para enterarme de las noticias."],
          ["💡 3 · Escucha activa", "Se escucha para comprender de verdad: no se interrumpe, se pregunta lo que no se entiende y se demuestra que se entendió.", "Escucho al médico y repito con mis palabras lo que me dijo."]])}
{C.caja("tip", "La gran diferencia", "<p>En la escucha activa, el objetivo no es responder rápido, sino <strong>entender bien</strong>. Primero comprendo; después respondo.</p>")}
<h3>Frases de escucha activa</h3>
{C.tabla("Cuatro funciones", ["Para…", "Frases"],
         [["✅ Mostrar acuerdo", "«Estoy de acuerdo con…», «Comparto lo que dijo…», «Tiene razón en que…»"], ["➕ Añadir información", "«Quiero añadir que…», «También me parece importante…»"],
          ["❓ Pedir aclaración", "«¿Puede explicar…?», «No entendí bien la parte de…», «¿Podría repetir lo último?»"], ["🔁 Parafrasear", "«Entonces, lo que usted dice es…», «Si entendí bien, usted piensa que…»"]])}
<div class="texto-lectura"><p>🗣️ <strong>María:</strong> Mi meta este semestre es terminar el Nivel 1 y empezar el Nivel 2.</p>
<p>👂 <strong>Carlos:</strong> Estoy de acuerdo contigo; yo también quiero avanzar. ¿Puedes explicar por qué tienes prisa?</p>
<p>🗣️ <strong>María:</strong> Porque trabajo de día y solo tengo dos noches por semana para estudiar.</p>
<p>👂 <strong>Carlos:</strong> Entonces, lo que dices es que tu horario te limita. Quiero añadir que a mí me pasa igual con el segundo turno.</p></div>
<p>Carlos primero muestra que escuchó («estoy de acuerdo», «entonces, lo que dices es…») y después añade lo suyo. Eso es escucha activa.</p>
{P("Compruebe", "«Si entendí bien, usted prefiere estudiar de noche.» ¿Qué hace esta frase?", FUN, 3, {0: "No dice si está de acuerdo.", 1: "No añade nada nuevo.", 2: "No pregunta: repite con otras palabras."}, "<strong>Parafrasea</strong>: repite con sus palabras para confirmar.")}"""

    s3 = f"""{C.tabla("Tres canales", ["Canal", "Qué es"],
         [["🔤 Verbal", "Las palabras que decimos."], ["🙋 No verbal", "Los gestos, la postura, la mirada y la cara."], ["🎤 Paraverbal", "El tono, el volumen, la velocidad y las pausas de la voz."]])}
{C.tabla("Gestos que muestran escucha", ["Gesto", "Lo que dice"],
         [["👀 Mirar a los ojos", "«Le presto atención.»"], ["🙆 Asentir con la cabeza", "«Le sigo, entiendo.»"], ["🪑 Postura abierta", "«Estoy disponible.»"], ["😊 Cara amable", "«Lo que dice me interesa.»"]])}
{C.caja("tip", "Idea clave", "<p>Si las palabras dicen una cosa y el cuerpo otra, la gente suele creerle más al cuerpo. Brazos cruzados o mirada perdida dicen «no me interesa», aunque la boca diga «sí, le escucho».</p>")}
{C.tabla("La escucha en la vida diaria", ["Situación", "Clave"],
         [["🩺 Cita médica", "Lleve sus preguntas escritas. Al final, repita con sus palabras lo que entendió: «Entonces, tomo la medicina dos veces al día con comida, ¿verdad?»."],
          ["💼 Entrevista de trabajo", "Deje terminar la pregunta, piense un momento y responda. Si no entendió, pida que la repitan."],
          ["🏫 Reunión en la escuela", "Anote lo importante y pregunte lo que no quede claro antes de irse."], ["🏠 En casa", "Deje el celular, mire a quien le habla y no interrumpa."]])}
{P("Compruebe", "Mientras su hija le cuenta su día, Rosa mira el celular y dice «ajá». ¿Es buena escucha?", ["No: no presta atención", "Sí: está escuchando"], 0, {}, "<strong>No</strong>: mira el celular. El cuerpo dice «no me interesa».")}"""

    secciones = [("s1", "¿Qué es la comunicación?", s1), ("s2", "Escuchar de verdad", s2), ("s3", "El cuerpo también habla", s3)]
    tarea = [("Una conversación real.", "Esta semana, en una conversación con alguien de su casa o del trabajo, use al menos tres frases de escucha activa: una de acuerdo, una de aclaración y una para parafrasear."),
             ("Mi diario de escucha.", "Escriba en su cuaderno qué frases usó, cómo reaccionó la otra persona y qué gesto de escucha practicó."),
             ("Para la próxima cita.", "Prepare por escrito tres preguntas para su próxima cita médica o reunión en la escuela.")]
    quiz = [
        ("¿Por qué se dice que la comunicación es de ida y vuelta?", ["Porque los papeles de emisor y receptor se alternan", "Porque una persona habla y la otra calla"], 0, {}, "Los papeles <strong>se alternan</strong>."),
        ("¿Quién es el emisor?", ["Quien envía el mensaje", "Quien lo recibe"], 0, {}, "Quien <strong>envía</strong> el mensaje."),
        ("¿Cuál es el nivel más profundo de escucha?", ["La escucha activa", "Oír", "Escuchar"], 0, {1: "Oír es el más básico.", 2: "Falta participar."}, "La <strong>escucha activa</strong>."),
        ("«¿Podría repetir la fecha, por favor?» sirve para…", FUN, 2, {0: "No dice si está de acuerdo.", 1: "No añade.", 3: "No repite con otras palabras."}, "<strong>Pedir aclaración.</strong>"),
        ("«Quiero añadir que también hay clases los sábados» sirve para…", FUN, 1, {0: "No dice si está de acuerdo.", 2: "No pregunta.", 3: "No repite lo del otro."}, "<strong>Añadir información.</strong>"),
        ("El tono y el volumen de la voz son el canal…", CANAL, 2, {0: "Lo verbal son las palabras.", 1: "Lo no verbal son los gestos."}, "<strong>Paraverbal.</strong>"),
        ("Cruzar los brazos es comunicación…", CANAL, 1, {0: "No son palabras.", 2: "No es la voz."}, "<strong>No verbal.</strong>"),
        ("En la escucha activa, ¿qué va primero?", ["Entender bien", "Responder rápido"], 0, {}, "<strong>Entender</strong>; después responder."),
        ("¿Qué conviene hacer al final de una cita médica?", ["Repetir con sus palabras lo que entendió", "Irse sin preguntar"], 0, {}, "<strong>Parafrasear</strong> para confirmar."),
        ("Si alguien no entendió, ¿qué debe hacer?", ["Pedir aclaración", "Decir «sí, sí» y seguir"], 0, {}, "<strong>Pedir aclaración.</strong>"),
    ]
    filas = [
        ("Niveles de escucha", "Explico la diferencia entre oír, escuchar y escuchar activamente.", "Confundo escuchar con escucha activa.", "No veo la diferencia (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Frases de escucha activa", "Uso frases para mostrar acuerdo, añadir, pedir aclaración y parafrasear.", "Uso una o dos.", "No las uso (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Comunicación no verbal", "Cuido mis gestos y mi tono al escuchar.", "A veces mi cuerpo dice otra cosa.", "No me fijo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe escuchar de verdad. En la próxima lección va a usar esas frases para <strong>conversar sobre un texto</strong> con la técnica 1-2-4.</p>"
    glosario = [("Emisor", "Quien envía el mensaje."), ("Receptor", "Quien recibe el mensaje."), ("Escucha activa", "Escuchar para comprender: sin interrumpir, preguntando y demostrando que se entendió."),
                ("Parafrasear", "Repetir con sus palabras lo que dijo otra persona."), ("Comunicación no verbal", "Gestos, postura, mirada y cara."), ("Paraverbal", "Tono, volumen, velocidad y pausas de la voz.")]
    conexion = ("<p>Llegó al último tema del Nivel 1. Ya sabe leer y escribir párrafos de distintos tipos. Ahora va a trabajar las dos destrezas que faltan: hablar y escuchar.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y alguien con quien conversar (de su casa, del trabajo o de la clase).</p>")
    estd = LE.estandares([], base=["R.2.2"], fund=["SL.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Primero comprendo, después respondo.", ["Comunicación oral", "Escucha activa"],
                            ["<strong>Explicar</strong> la comunicación como un intercambio.", "<strong>Distinguir</strong> oír, escuchar y escuchar activamente.",
                             "<strong>Usar</strong> frases para mostrar acuerdo, añadir, pedir aclaración y parafrasear.", "<strong>Reconocer</strong> la comunicación verbal, no verbal y paraverbal."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-2", LE.titulo("8-2")), glosario, P)


def practica():
    esc = [{"enun": f"<div class=\"texto-lectura\"><p>{s}</p></div>¿Es buena escucha o mala escucha?", "ops": ["Buena escucha", "Mala escucha"], "ok": 0 if b else 1, "enOrden": True, "pista": "", "exp": e} for s, b, e in ESC]
    fra = [{"enun": f"<strong>«{f}»</strong><br>¿Para qué sirve esta frase?", "ops": FUN, "ok": k, "enOrden": True, "pista": "Acuerdo: estoy de acuerdo. Añadir: también, agrego. Aclaración: una pregunta. Parafrasear: entonces, si entendí bien.",
            "exp": f"Sirve para <strong>{FUN[k].lower()}</strong>."} for f, k in FRASES]
    can = [{"enun": f"<strong>{c}</strong><br>¿Qué canal de comunicación es?", "ops": CANAL, "ok": k, "enOrden": True, "pista": "Verbal: palabras. No verbal: gestos y cuerpo. Paraverbal: cómo suena la voz.",
            "exp": f"Es comunicación <strong>{CANAL[k].lower()}</strong>."} for c, k in CAN]
    mods = [("escucha", "¿Buena o mala escucha?", C.om("m1", "Lea la situación y decida.")),
            ("frases", "¿Para qué sirve la frase?", C.om("m2", "Elija la función de cada frase de escucha activa.")),
            ("canales", "¿Verbal, no verbal o paraverbal?", C.om("m3", "Decida por qué canal va el mensaje."))]
    js = C.js_datos("ESC", esc) + C.js_datos("FRA", fra) + C.js_datos("CAN", can) + 'creaBanco("m1", ESC);\ncreaBanco("m2", FRA);\ncreaBanco("m3", CAN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
