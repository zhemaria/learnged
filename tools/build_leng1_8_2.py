# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.2 · Leer y conversar: la técnica 1-2-4.
Fuente: clases_leng1/clase_8-2.html (GEDparaHispanos), adaptada al marco de LearnGED (sin práctica en gramatica: se escribió aquí).
Uso: python3 tools/build_leng1_8_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-2"
PAPELES = ["Quien empieza", "Quien resume", "Quien pregunta", "Quien cierra"]
INTERV = [("Vamos a empezar. Leo el título: «Los abuelos como maestros de la familia». ¿Qué piensan al oírlo?", 0),
          ("Bueno, ya leímos el texto. ¿Quién quiere comenzar la conversación?", 0),
          ("El texto dice que los abuelos guardan la memoria de la familia, aunque vivan lejos.", 1),
          ("La idea principal es que, si no hablamos con los abuelos, su historia se pierde.", 1),
          ("En pocas palabras, el autor cuenta cómo los abuelos enseñan recetas y costumbres por teléfono.", 1),
          ("¿Por qué creen que las conversaciones con los abuelos son cada vez más cortas?", 2),
          ("¿Qué pasaría si nadie escribiera las historias de la familia?", 2),
          ("¿Cómo se relaciona este texto con lo que vive su familia?", 2),
          ("En conclusión, el grupo piensa que hay que guardar las historias de los abuelos.", 3),
          ("Lo que todos coincidimos es que una llamada a la semana puede hacer una gran diferencia.", 3),
          ("Para terminar: todos estamos de acuerdo en que los abuelos son un puente con nuestra cultura.", 3)]
ACUERDOS = ["Una voz a la vez", "Todos hablamos al menos una vez", "Pedimos la palabra con respeto", "Pedimos aclaración si no entendemos", "Criticamos ideas, no personas", "Cuidamos el tiempo"]
ROMPE = [("Mientras Ana habla, Luis empieza a hablar al mismo tiempo.", 0), ("Pedro no ha dicho nada en toda la reunión y nadie lo invita a participar.", 1),
         ("Rosa grita su idea sin esperar a que el otro termine la oración.", 2), ("Jorge no entendió una palabra, pero dice «sí, claro» para quedar bien.", 3),
         ("Marta le dice a su compañero: «Eso es una tontería, tú nunca sabes nada».", 4), ("Carlos habla veinte minutos seguidos y nadie más puede opinar.", 5),
         ("Dos personas hablan a la vez y nadie entiende a ninguna.", 0), ("Elena dice: «Lo que dijiste no tiene sentido porque eres muy joven».", 4)]
# Respuestas escritas: (mensaje, respuesta con escucha activa, dos que no)
RESP = [("Tía Carmen, en el grupo de la familia: «Estoy pensando en organizar la cena de Navidad en mi casa este año».",
         "¡Buena idea, tía! Si entendí bien, sería el 24. Yo puedo llevar el arroz. ¿A qué hora?", ["Ok. Ya veremos qué pasa con eso más adelante, cuando se acerque la fecha.", "Yo prefiero que sea en otro lado, como todos los años; tu casa queda muy lejos."]),
        ("Su jefe, por correo: «Mañana la reunión cambia a las 3:00. Traiga el informe de ventas».",
         "Entendido: la reunión es mañana a las 3:00 y llevo el informe de ventas. ¿Se hace en la misma sala?", ["Bueno. Hoy estoy muy ocupado con otras cosas y no puedo contestar más.", "¿Otra reunión? Ya tuvimos una la semana pasada y no sirvió para nada."]),
        ("Su vecino: «El lunes van a cortar el agua de 9 a 12 por una reparación».",
         "Gracias por avisar. Entonces, el lunes no habrá agua de 9 a 12. Voy a llenar unos baldes el domingo.", ["Siempre cortan el agua en este edificio; el dueño nunca arregla nada bien.", "👍 Ya lo había escuchado en el pasillo, pero se me había olvidado otra vez."]),
        ("Una compañera de clase: «No entendí la tarea de la Lección 8.1. ¿Qué hay que hacer?».",
         "Te entiendo, a mí también me costó. Hay que usar tres frases de escucha activa en una conversación y anotarlas. ¿Quieres que te muestre las mías?", ["Está fácil, solo tienes que leer bien la lección otra vez y la vas a entender.", "Pregúntale a la maestra, porque yo tampoco me acuerdo muy bien de lo que era."])]
ABUELOS = ["En muchas familias hispanas, los abuelos no son solo los miembros mayores: son los guardianes de la memoria. Cuando una familia emigra a otro país, los abuelos suelen quedarse en su pueblo mientras los hijos y los nietos viven lejos. Aun así, siguen siendo el puente con la cultura, la lengua y las costumbres de origen.",
           "Una llamada semanal, una visita en vacaciones o una receta enseñada por teléfono son maneras en que los abuelos transmiten lo que saben. Hay nietos que aprendieron a cocinar arroz con frijoles escuchando a su abuela paso a paso desde mil kilómetros de distancia. Hay otros que conocen la historia de su pueblo solo porque su abuelo se la contó.",
           "El problema es que, con el ritmo de vida de hoy, muchas familias sienten que esas conversaciones son cada vez más cortas. Y cuando los abuelos se van, se va con ellos un pedazo de la historia familiar que nadie escribió."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Hablar de lo que leyó con otra persona le obliga a ordenar su pensamiento, defender una idea y escuchar a quien piensa distinto. La <strong>técnica 1-2-4</strong> tiene tres fases. En un salón, el nombre viene del número de personas en cada fase: 1 (usted solo), 2 (en pareja) y 4 (en grupo). Si estudia por su cuenta, la idea es la misma.</p>
{C.tabla("La técnica 1-2-4", ["Fase", "Tiempo", "Qué hacer"],
         [["1 · Pensar solo", "3 minutos", "Responda la pregunta por escrito, sin consultar a nadie."],
          ["2 · Comparar", "5 minutos", "Comparta su respuesta con otra persona (de su casa, un amigo por teléfono) y escuche la suya. Si está solo, compárela con la respuesta modelo."],
          ["4 · Concluir", "5 minutos", "Escriba una conclusión que tome lo mejor de las dos respuestas."]])}
<ul><li><strong>Su idea va primero:</strong> si empieza escuchando a otros, es fácil repetir lo que oyó.</li><li><strong>Comparar enriquece:</strong> otra persona puede ver lo que usted no vio. No se trata de quién tiene razón, sino de mejorar la respuesta.</li>
<li><strong>Concluir ordena:</strong> al escribir, decide qué ideas se queda y por qué.</li></ul>
<h3>Lectura: «Los abuelos como maestros de la familia»</h3>
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in ABUELOS)}</div>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · técnica 1-2-4</span>
<p><strong>Pregunta:</strong> ¿cuál es la idea más importante que el autor quiere transmitir, y qué podría hacer su familia para fortalecer la conexión con los abuelos? Siga las tres fases.</p></div>
<details class="caja caja-tip"><summary><strong>Ya escribí mi respuesta: ver un modelo</strong></summary>
<p>«El autor quiere decir que los abuelos guardan la memoria de la familia y que, si no hablamos con ellos, esa historia se pierde. Mi familia podría hacer una videollamada cada domingo y pedirle a la abuela que nos cuente una historia o nos enseñe una receta. También podríamos escribir esas historias en un cuaderno.»</p></details>
{P("Compruebe", "¿Cuál es la idea principal del texto?", ["Los abuelos guardan la memoria de la familia, y si no hablamos con ellos se pierde", "Los abuelos cocinan muy bien", "Las familias emigran a otros países"], 0,
   {1: "Las recetas son un ejemplo, no la idea principal.", 2: "Es parte del contexto, no la idea principal."}, "Los abuelos son <strong>guardianes de la memoria</strong> familiar.")}"""

    s2 = f"""<p>Un <strong>círculo de lectura</strong> es una conversación ordenada sobre un texto en la que cada persona tiene un papel. Si estudia solo, haga los cuatro papeles usted mismo, uno tras otro, como si se pusiera cuatro sombreros.</p>
{C.tabla("Los cuatro papeles del lector", ["Papel", "Qué hace", "Frases"],
         [["🚀 Quien empieza", "Abre la conversación: lee el título o la primera oración e invita a hablar.", "«Vamos a empezar…», «¿Qué piensan?»"],
          ["📋 Quien resume", "Dice en dos o tres oraciones de qué trata el texto, sin opinar.", "«El texto dice que…», «La idea principal es…»"],
          ["❓ Quien pregunta", "Hace al menos dos preguntas que no se responden con sí o no.", "«¿Por qué creen que…?», «¿Qué pasaría si…?»"],
          ["🎯 Quien cierra", "Recoge lo dicho y formula la conclusión común.", "«En conclusión, el grupo piensa que…»"]])}
{P("Compruebe", "«¿Qué pasaría si nadie escribiera las historias de la familia?» ¿Qué papel cumple?", PAPELES, 2, {0: "No abre la conversación.", 1: "No resume: pregunta.", 3: "No concluye."}, "<strong>Quien pregunta</strong>.")}
<h3>Acuerdos para conversar</h3>
<ol>{"".join(f"<li><strong>{a}.</strong></li>" for a in ACUERDOS)}</ol>
{C.caja("tip", "¿Por qué ponerse de acuerdo antes?", "<p>Si todos conocen las reglas, es fácil volver al orden: si alguien interrumpe, nadie lo regaña; solo se le recuerda el acuerdo número uno.</p>")}"""

    s3 = f"""<p>Muchas conversaciones hoy son por escrito: el grupo de mensajes de la familia, un correo del trabajo, los comentarios de una noticia. Ahí también se nota quién escucha: responde a lo que el otro dijo, confirma lo importante y pregunta lo que falta.</p>
<div class="texto-lectura"><p><strong>Mensaje:</strong> «Mañana la reunión cambia a las 3:00. Traiga el informe de ventas».</p>
<p>❌ «Bueno.»</p><p>✅ «Entendido: la reunión es mañana a las 3:00 y llevo el informe de ventas. ¿Se hace en la misma sala?»</p></div>
<p>La buena respuesta <strong>parafrasea</strong> (repite la hora y lo que hay que llevar) y <strong>pide aclaración</strong> (la sala).</p>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Copie un mensaje real que haya recibido esta semana (sin datos privados) y escriba una respuesta con escucha activa: confirme lo importante y haga una pregunta.</p></div>"""

    secciones = [("s1", "La técnica 1-2-4", s1), ("s2", "Los cuatro papeles y los acuerdos", s2), ("s3", "Responder por escrito", s3)]
    tarea = [("Un círculo en casa.", "Lea con alguien de su casa una noticia corta o un cuento. Repártanse los cuatro papeles (o hágalos usted solo) y conversen diez minutos."),
             ("Mi conclusión.", "Escriba en su cuaderno la conclusión del círculo en dos o tres oraciones."),
             ("Los acuerdos.", "Escriba cuál de los seis acuerdos fue el más difícil de cumplir y por qué.")]
    quiz = [
        ("¿Qué se hace en la fase 1 de la técnica 1-2-4?", ["Pensar solo y escribir la respuesta", "Escuchar a todo el grupo", "Copiar la respuesta modelo"], 0, {1: "Eso va después.", 2: "Primero va su idea."}, "<strong>Pensar solo.</strong>"),
        ("¿Por qué su idea va primero?", ["Para no repetir lo que oyó de otros", "Para ganar la discusión"], 0, {}, "Para formar <strong>su propia opinión</strong>."),
        ("¿Qué se hace en la última fase?", ["Escribir una conclusión con lo mejor de las respuestas", "Decir quién ganó"], 0, {}, "<strong>Concluir.</strong>"),
        ("«El texto dice que los abuelos guardan la memoria de la familia.» ¿Qué papel es?", PAPELES, 1, {0: "No abre la conversación.", 2: "No pregunta.", 3: "No concluye la conversación del grupo."}, "<strong>Quien resume.</strong>"),
        ("¿Cómo deben ser las preguntas de «quien pregunta»?", ["Que no se respondan con sí o no", "Muy cortas, de sí o no"], 0, {}, "Preguntas <strong>abiertas</strong>."),
        ("Marta dice: «Eso es una tontería, tú nunca sabes nada». ¿Qué acuerdo rompe?", ["Criticamos ideas, no personas", "Cuidamos el tiempo", "Una voz a la vez"], 0, {1: "No es un problema de tiempo.", 2: "No habla a la vez que otro."}, "<strong>Criticamos ideas, no personas.</strong>"),
        ("Si no entiende algo en la conversación, ¿qué acuerdo le ayuda?", ["Pedimos aclaración si no entendemos", "Todos hablamos al menos una vez"], 0, {}, "<strong>Pedir aclaración.</strong>"),
        ("¿Cuál es la mejor respuesta a «La reunión cambia a las 3:00»?", ["Entendido: la reunión es a las 3:00. ¿En qué sala?", "Ok."], 0, {}, "La que <strong>confirma y pregunta</strong>."),
        ("¿Quién formula la conclusión común?", PAPELES, 3, {0: "Ese abre.", 1: "Ese resume el texto, no la conversación.", 2: "Ese pregunta."}, "<strong>Quien cierra.</strong>"),
        ("Si estudia solo, ¿puede usar los cuatro papeles?", ["Sí: los hace uno tras otro", "No: solo sirven en grupo"], 0, {}, "<strong>Sí</strong>, como cuatro sombreros."),
    ]
    filas = [
        ("Técnica 1-2-4", "Pienso solo, comparo y concluyo por escrito.", "Me salto la fase de pensar solo.", "No sigo las fases (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Papeles del lector", "Puedo hacer los cuatro papeles.", "Hago bien uno o dos.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Responder por escrito", "Respondo confirmando lo importante y preguntando lo que falta.", "Respondo, pero sin confirmar.", "Respondo «ok» (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe conversar sobre un texto. En la próxima lección va a trabajar con la tecnología: <strong>el vocabulario digital</strong> que necesita para el examen y para la vida.</p>"
    glosario = [("Técnica 1-2-4", "Pensar solo, comparar y concluir."), ("Círculo de lectura", "Conversación ordenada sobre un texto, con papeles."),
                ("Pregunta abierta", "Pregunta que no se responde con sí o no."), ("Conclusión común", "La idea que comparte el grupo al final.")]
    conexion = ("<p>En la Lección 8.1 aprendió la escucha activa y sus frases. Ahora va a usarlas para conversar sobre un texto: ordenar su pensamiento, defender una idea y escuchar a quien piensa distinto.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, alguien con quien leer.</p>")
    estd = LE.estandares(["R.2.1", "R.2.2"], fund=["SL.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Pensar solo, comparar y concluir.", ["Comunicación oral", "Comprensión"],
                            ["<strong>Aplicar</strong> la técnica 1-2-4 a un texto.", "<strong>Cumplir</strong> los cuatro papeles del lector.",
                             "<strong>Seguir</strong> los acuerdos para conversar.", "<strong>Responder</strong> por escrito con escucha activa."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-3", LE.titulo("8-3")), glosario, P)


def practica():
    pap = [{"enun": f"<strong>«{t}»</strong><br>¿Qué papel cumple esta intervención?", "ops": PAPELES, "ok": k, "enOrden": True, "pista": "Empieza: abre. Resume: dice de qué trata. Pregunta: hace preguntas abiertas. Cierra: concluye.",
            "exp": f"Es <strong>{PAPELES[k].lower()}</strong>."} for t, k in INTERV]
    rom = []
    for s, k in ROMPE:
        otros = [a for i, a in enumerate(ACUERDOS) if i != k]
        rom.append({"enun": f"<div class=\"texto-lectura\"><p>{s}</p></div>¿Qué acuerdo para conversar no se cumple?", "ops": [ACUERDOS[k]] + otros[:2] if k > 1 else [ACUERDOS[k]] + otros[-2:], "ok": 0,
                    "pista": "Piense qué regla le habría evitado el problema.", "exp": f"No se cumple «<strong>{ACUERDOS[k]}</strong>»."})
    res = [{"enun": f"<div class=\"texto-lectura\"><p>{m}</p></div>¿Qué respuesta muestra escucha activa?", "ops": [b] + m2, "ok": 0, "pista": "Busque la que confirma lo importante y pregunta o propone algo.",
            "exp": f"<strong>{b}</strong>"} for m, b, m2 in RESP]
    mods = [("papeles", "¿Qué papel es?", C.om("m1", "Decida qué papel cumple cada intervención.")),
            ("acuerdos", "¿Qué acuerdo no se cumple?", C.om("m2", "Lea la situación y elija el acuerdo que se rompe.")),
            ("responder", "Responder con escucha activa", C.om("m3", "Elija la mejor respuesta al mensaje."))]
    js = C.js_datos("PAP", pap) + C.js_datos("ROM", rom) + C.js_datos("RES", res) + 'creaBanco("m1", PAP);\ncreaBanco("m2", ROM);\ncreaBanco("m3", RES);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
