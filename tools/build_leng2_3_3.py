# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 3.3 · Registro formal e informal: habla frente a escritura.
Fuente: clases_leng2/clase_3-3.html (GEDparaHispanos) y gramatica/n2-l3-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_3_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "3-3"
REG = ["Formal", "Informal"]
CLAS = [("Buenos días. Quisiera confirmar mi cita del jueves a las diez.", 0, "Saludo de cortesía y oración completa."),
        ("¿Qué onda? ¿Vamos al cine el sábado?", 1, "<em>¿Qué onda?</em> es un saludo de confianza."),
        ("Le informamos que su pedido llegará el lunes.", 0, "<em>usted</em> e <em>informar</em>."),
        ("Ya llegué, mamá, no te preocupes 😘", 1, "Trato de <em>tú</em> y emoji."),
        ("Estimado cliente: le recordamos que su factura vence el día 15.", 0, "Saludo formal con dos puntos."),
        ("Oye, tmb trae hielo xfa", 1, "Abreviaturas: <em>tmb, xfa</em>."),
        ("¿Podría indicarme dónde está la oficina de admisiones?", 0, "<em>¿Podría…?</em> es una petición cortés con <em>usted</em>."),
        ("Esa película está bien chida, ¡tienes que verla!", 1, "<em>chida</em> es una palabra coloquial."),
        ("Le agradezco de antemano su atención.", 0, "Fórmula de cortesía."),
        ("Nos vemos al rato, cuídate", 1, "Despedida de confianza."),
        ("Adjunto le envío mi currículum para el puesto de recepcionista.", 0, "Vocabulario de trabajo y <em>usted</em>."),
        ("Me quedé sin pega, ando buscando algo", 1, "<em>pega</em> (trabajo, en Chile) y tono de conversación."),
        ("Señora Martínez, ¿tendría unos minutos para hablar sobre mi hijo?", 0, "Trato de <em>usted</em> y pregunta cortés."),
        ("Jaja no manches, qué risa 😂", 1, "Expresión coloquial y emoji.")]
DEST = [("Le escribe a la maestra de su hija. ¿Cómo empieza?", ["Estimada maestra López:", "¡Hola, profe! ¿Cómo andas?", "Oye, maestra López, ¿qué tal?"]),
        ("Le escribe a su mejor amiga. ¿Cómo empieza?", ["¡Hola, Caro! ¿Cómo estás?", "Estimada Carolina:", "Muy señora mía:"]),
        ("Llama a una clínica para pedir una cita.", ["Buenos días, quisiera pedir una cita con el doctor Ruiz.", "¿Qué tal? Oye, ¿me das una cita con el doctor Ruiz?", "Hola, ¿qué onda? Necesito al doctor Ruiz pa' mañana."]),
        ("Termina un correo a una oficina del gobierno.", ["Atentamente,", "Chao, gracias!!", "Un besote,"]),
        ("Le pide a su hijo que saque la basura.", ["Mijo, ¿sacas la basura, por favor?", "Le solicito que retire los residuos.", "Estimado hijo: saque la basura."]),
        ("Le pide a su supervisor que le cambie el turno.", ["¿Sería posible cambiar mi turno del martes por el jueves?", "Oye, cámbiame el turno del martes por el jueves, ¿va?", "Cambia mi turno del martes, porfa, que el jueves me va mejor."]),
        ("Responde un mensaje de su hermano, que la invita a comer.", ["¡Claro! Allí estaré a las dos.", "Le confirmo mi asistencia a la comida.", "Acepto cordialmente su invitación."]),
        ("Escribe una queja a la compañía de cable.", ["Les escribo porque el servicio lleva tres días sin funcionar.", "Oigan, el cable no sirve desde el lunes, ¿qué pasó? 😡", "El cable anda bien mal, ya van tres días, arréglenlo ya."]),
        ("Agradece una entrevista de trabajo.", ["Muchas gracias por recibirme ayer y por su tiempo.", "Gracias x la entrevista de ayer!! Estuvo súper 👍", "Ey, gracias por la entrevista, estuvo bien chida."]),
        ("Le pregunta a un desconocido por una calle.", ["Disculpe, ¿sabe dónde queda la calle Pulaski?", "Oye, ¿tú sabes dónde queda la calle Pulaski?", "Tú, ¿dónde queda Pulaski? Ando perdido."]),
        ("Le escribe a su compañera de clase para quedar a estudiar.", ["¿Estudiamos juntas el jueves en la biblioteca?", "Le propongo una sesión de estudio el jueves.", "Estimada compañera: solicito su presencia el jueves."]),
        ("Responde en el GED una pregunta de respuesta extendida.", ["El autor presenta tres argumentos a favor de su postura.", "Pues el autor dice como tres cosas, o sea, que tiene razón.", "El autor tiene razón y ya, eso es todo lo que hay que decir."])]
TRANS = [("oye q onda, mi hijo no va a ir mañana xq tiene gripa, ok?", ["Les informo que mi hijo no asistirá mañana porque tiene gripe.", "Oye, mi hijo no va a ir mañana porque tiene gripa, ¿ok?", "Les informo q mi hijo no va a ir mañana xq tiene gripa."]),
         ("la llave del baño está rota otra vez, la arreglas ya porfa?", ["Le informo que la llave del baño está rota de nuevo. ¿Podría repararla pronto?", "La llave del baño ta rota otra vez. ¿Me la arreglas ya, porfa?", "Le informo que la llave del baño está rota otra vez. Arréglala ya, porfa."]),
         ("vi lo de la chamba de cocinero, cuánto pagan?", ["Vi su anuncio para el puesto de cocinero. ¿Podría indicarme el salario?", "Vi lo de la chamba de cocinero en su anuncio. ¿Cuánto pagan?", "Vi su anuncio de la chamba de cocinero. ¿Cuánto me van a pagar?"]),
         ("no puedo ir a la junta, se me complicó, perdón", ["Lamento informarle que no podré asistir a la reunión por un imprevisto.", "No voy a poder ir a la junta de mañana, se me complicó, perdón.", "Lamento que no puedo ir a la junta, es que se me complicó todo."]),
         ("me mandas el papel de la renta xfa", ["¿Podría enviarme el recibo del alquiler, por favor?", "Mándame el papel de la renta cuando puedas, por favor.", "¿Me envía el papel de la renta xfa? Lo necesito."]),
         ("gracias x todo, nos vemos", ["Le agradezco mucho su ayuda. Saludos cordiales.", "Muchas gracias por todo, nos vemos al rato.", "Muchas gracias x su ayuda, nos vemos pronto."]),
         ("tengo q faltar el lunes, voy al doc", ["Necesito faltar el lunes porque tengo una cita médica.", "Tengo que faltar el lunes porque voy al doc, ¿va?", "Necesito faltar el lunes xq tengo que ir al doctor."]),
         ("está bien caro el curso, no hay descuento o algo?", ["¿El curso ofrece algún descuento? El precio es alto para mí.", "Está bien caro el curso. ¿No hay un descuento o algo así?", "¿No hay un descuentito o algo? El curso está bien caro."]),
         ("ya te pagué, checa tu cuenta", ["Le informo que ya realicé el pago. Puede verificarlo en su cuenta.", "Ya le pagué todo, así que chequee su cuenta cuando pueda.", "Ya te hice el pago completo, revisa tu cuenta del banco."]),
         ("ando buscando info de las clases de compu", ["Quisiera información sobre las clases de computación.", "Ando buscando información de las clases de compu.", "Quisiera info sobre las clases de computación, porfa."])]
HABLADO = "Oye, este, ¿sabes qué? Que mañana no voy a poder ir, o sea, por lo del niño, que está malito, ¿sabes? Pues eso."
ESCRITO = "Mañana no podré ir porque mi hijo está enfermo."


def leccion():
    P = C.Practicas()
    s1 = f"""<p>No hablamos igual con nuestra mejor amiga que con el médico, ni le escribimos igual a un hermano que a la oficina del Seguro Social. Sin pensarlo, cambiamos las palabras, el trato y hasta la forma de las oraciones. Esa manera de usar la lengua según la situación se llama <strong>registro</strong>. Saber elegirlo es tan importante como la ortografía: un correo de trabajo escrito como un chat da una mala impresión, aunque no tenga ni un error.</p>
{C.tabla("Registro formal e informal", ["Registro", "Cuándo se usa", "Ejemplo"],
         [["Informal", "Con familia, amigos y personas de confianza, en situaciones relajadas.", "¡Hola, Pati! ¿Vienes el sábado a la carne asada?"],
          ["Formal", "Con personas que no conocemos o que tienen un cargo; en el trabajo, en oficinas, en la escuela, en exámenes.", "Buenos días, señora Rivas. Le escribo para confirmar la reunión del sábado."]])}
{C.caja("tip", "Ninguno es «mejor»", "<p>El registro informal no es incorrecto: es el adecuado para otra situación. Lo que no funciona es usar uno donde corresponde el otro, como tratar de «mi amor» al cajero del banco, o escribirle a un hijo «Estimado hijo: le informo que la cena está servida».</p>")}
{C.caja("ojo", "En el GED", "<p>La respuesta extendida del examen de Artes del Lenguaje se escribe en <strong>registro formal</strong>. Es una de las cosas que se califican.</p>")}
{P("Compruebe", "Un correo a la maestra de su hijo va en registro…", REG, 0, {1: "La maestra es una persona con un cargo, en un contexto escolar."}, "<strong>Formal.</strong>")}"""

    s2 = f"""{C.tabla("Marcas del registro informal y del formal", ["Aspecto", "Informal", "Formal"],
         [["Trato", "tú (o vos en varios países): ¿Cómo estás?", "usted: ¿Cómo está usted?"], ["Saludo", "Hola · ¿Qué tal? · Oye", "Buenos días · Estimado señor:"],
          ["Despedida", "Chao · Nos vemos · Un abrazo", "Atentamente · Saludos cordiales · Quedo a sus órdenes"],
          ["Vocabulario", "Palabras de todos los días y de cada país: chamba, pega, chido, bacán", "Palabras generales y precisas: trabajo, empleo, excelente"],
          ["Verbos", "pedir, decir, arreglar, mandar", "solicitar, informar, resolver, enviar"], ["Escritura", "Abreviaturas y emojis: q, xq, tmb, 👍", "Palabras completas, sin emojis: que, porque, también"],
          ["Oraciones", "Cortas, a veces incompletas: ¿Mañana? Ok.", "Completas y bien puntuadas: De acuerdo, nos vemos mañana."]])}
{C.caja("tip", "Las palabras de cada país", "<p><em>chamba</em> (México), <em>pega</em> (Chile), <em>curro</em> (España) o <em>camello</em> (Colombia) quieren decir lo mismo: <strong>trabajo</strong>. Son parte de la riqueza del español, pero en un texto formal conviene la palabra que se entiende en todos los países.</p>")}
{P("Compruebe", "«Oye, tmb trae hielo xfa» está en registro…", REG, 1, {0: "Tiene abreviaturas y trato de tú."}, "<strong>Informal</strong>: abreviaturas y tú.")}
<h3>Hablar no es lo mismo que escribir</h3>
<p>Cuando hablamos, tenemos la voz, los gestos y a la otra persona delante, que puede preguntarnos si no entiende. Cuando escribimos, el texto tiene que entenderse solo.</p>
{C.tabla("Diferencias entre la lengua hablada y la escrita", ["Al hablar", "Al escribir"],
         [["Repetimos y nos corregimos sobre la marcha: «Fui al, este, al mercado…»", "Revisamos antes de enviar: Fui al mercado."],
          ["Usamos muletillas: este, o sea, pues, tipo, ¿sabes?", "Las quitamos: no aportan nada en el papel."],
          ["Acortamos palabras: pa'l trabajo, 'tá bien, ¿pa' qué?", "Las escribimos completas: para el trabajo, está bien, ¿para qué?"],
          ["Señalamos: «Ponlo ahí, al lado de eso»", "Nombramos: Póngalo en la mesa, junto al teléfono."]])}
<p><strong>Escuche la diferencia.</strong> La primera versión es como se diría hablando; la segunda, como se escribiría en una nota.</p>
<div class="texto-lectura"><p>{LE.escuchar(HABLADO, "Hablando")} «{HABLADO}»</p><p>{LE.escuchar(ESCRITO, "Escrito")} «{ESCRITO}»</p></div>"""

    s3 = f"""<p>Antes de escribir, hágase dos preguntas: <strong>¿a quién le escribo?</strong> y <strong>¿para qué?</strong> Con esas respuestas elige el registro.</p>
{C.tabla("Situaciones y registro adecuado", ["Situación", "Registro"],
         [["Un mensaje a su hermana para quedar el domingo", "Informal"], ["Un correo a la maestra de su hijo", "Formal"], ["Una solicitud de empleo", "Formal"],
          ["Una nota a su compañero de cuarto sobre la compra", "Informal"], ["Una queja a la compañía de luz", "Formal"],
          ["Un mensaje a un compañero de trabajo de confianza", "Informal, pero más cuidado si el tema es de trabajo"]])}
<h3>Lectura: el mismo mensaje, dos tonos</h3>
<p>Daniela necesita el viernes libre para acompañar a su madre al médico. Lea los dos mensajes. En su cuaderno, haga una tabla de dos columnas y anote cinco diferencias: el trato, el saludo, el vocabulario, la escritura y la despedida.</p>
<h4>A su amiga Karla</h4>
<div class="chat" role="group" aria-label="Mensajes de texto de Daniela a Karla"><p class="burbuja">Hola Karla!! 😊 oye el viernes no puedo ir al gym xq tengo q llevar a mi mamá al doctor 😕 lo dejamos pa la otra semana?<span class="hora">8:15 p. m.</span></p>
<p class="burbuja">Bueno, me avisas. Besos!!<span class="hora">8:16 p. m.</span></p></div>
<h4>A su supervisora</h4>
<div class="texto-lectura carta"><p><strong>Asunto:</strong> Solicitud de día libre el viernes 16 de octubre</p><p>Estimada señora Ortega:</p>
<p>Le escribo para solicitarle el viernes 16 de octubre como día libre. Ese día debo acompañar a mi madre a una cita médica que no se puede cambiar. Si es necesario, puedo recuperar las horas el sábado o la semana siguiente.</p>
<p>Quedo atenta a su respuesta. Muchas gracias por su comprensión.</p><p>Atentamente,<br>Daniela Castro</p></div>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary>
{C.tabla("Diferencias entre los dos mensajes", ["Aspecto", "A Karla", "A la supervisora"],
         [["Trato", "tú: me avisas", "usted: Le escribo, su respuesta"], ["Saludo", "Hola Karla!!", "Estimada señora Ortega:"], ["Vocabulario", "gym, doctor, pa la otra semana", "solicitar, cita médica, la semana siguiente"],
          ["Escritura", "xq, q, emojis, sin signos de apertura", "Palabras completas, signos y puntuación correctos"], ["Despedida", "Besos!!", "Atentamente, Daniela Castro"]])}
<p>Fíjese además en que el correo explica el motivo, propone una solución (recuperar las horas) y lleva un asunto claro. En un mensaje formal, ser amable y concreto ayuda a obtener lo que se pide.</p></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · de informal a formal</span>
<p>Reescriba cada mensaje en registro formal, sin cambiar lo que se quiere decir.</p>
<ol><li>A la oficina de la escuela: «oye q onda, mi hijo no va a ir mañana xq tiene gripa, ok?»</li><li>Al dueño del apartamento: «la llave del baño está rota otra vez, la puedes arreglar ya porfa?»</li>
<li>A una empresa donde quiere trabajar: «hola, vi lo de la chamba de cocinero, me interesa, cuánto pagan?»</li></ol>
<details><summary><strong>Ver versiones posibles</strong></summary>
<p>«Buenos días. Les informo que mi hijo, [nombre], no asistirá a clases mañana porque tiene gripe. Gracias por su atención. Atentamente, [firma]».</p>
<p>«Estimado señor [apellido]: Le escribo para informarle que la llave del baño está rota de nuevo. ¿Podría enviar a alguien a repararla lo antes posible? Muchas gracias. Saludos cordiales, [firma]».</p>
<p>«Estimados señores: Vi su anuncio para el puesto de cocinero y me interesa mucho. ¿Podrían indicarme cuál es el salario y cómo puedo enviar mi solicitud? Quedo a sus órdenes. Atentamente, [firma]».</p></details>
<p>Si tiene con quién practicar, representen una llamada formal (pedir una cita en una clínica) y luego una informal (invitar a un amigo a comer). Fíjense en qué cambia en sus voces y sus palabras.</p></div>"""

    secciones = [("s1", "¿Qué es el registro?", s1), ("s2", "Las marcas de cada registro", s2), ("s3", "¿A quién le escribe?", s3)]
    tarea = [("Un mensaje, dos versiones.", "Elija una situación real (pedir un permiso, cambiar una cita, hacer una queja). Escriba la versión informal, para alguien de confianza, y la formal, por correo, con asunto, saludo, dos párrafos, despedida y firma."),
             ("Mis muletillas.", "Grábese dos minutos contando qué hizo ayer. Escúchese y anote las muletillas que repite (este, o sea, pues…). Luego escriba el mismo relato sin ellas."),
             ("Revisión final.", "Revise su correo formal con lo aprendido en el tema: mayúsculas, comas, dos puntos del saludo, tildes y ortografía.")]
    quiz = [
        ("¿Qué es el registro?", ["La manera de usar la lengua según la situación", "Las reglas de la tilde", "Una lista de palabras difíciles"], 0, {1: "Eso es ortografía.", 2: "Eso es vocabulario."}, "La manera de usar la lengua <strong>según la situación</strong>."),
        ("¿El registro informal es incorrecto?", ["No: es el adecuado para otras situaciones", "Sí: siempre hay que evitarlo"], 0, {1: "Con la familia y los amigos es el adecuado."}, "<strong>No</strong>: depende de la situación."),
        ("¿En qué registro se escribe la respuesta extendida del GED?", ["Formal", "Informal"], 0, {1: "Es un examen: el registro formal se califica."}, "<strong>Formal.</strong>"),
        ("¿Qué trato es propio del registro formal?", ["usted", "tú", "vos"], 0, {1: "Es de confianza.", 2: "Es de confianza en varios países."}, "<strong>usted.</strong>"),
        ("¿Cuál es una despedida formal?", ["Saludos cordiales,", "Nos vemos,", "Un besote,"], 0, {1: "Es de confianza.", 2: "Es de confianza."}, "<strong>Saludos cordiales,</strong>"),
        ("¿Qué palabra conviene en un texto formal?", ["trabajo", "chamba", "pega"], 0, {1: "Es una palabra de México, coloquial.", 2: "Es una palabra de Chile, coloquial."}, "<strong>trabajo</strong>: se entiende en todos los países."),
        ("¿Cuál es una muletilla?", ["o sea", "porque", "además"], 0, {1: "Es un conector con sentido.", 2: "Es un conector con sentido."}, "<strong>o sea</strong>: no aporta nada en el papel."),
        ("En un texto formal, <em>xq</em> se escribe…", ["porque", "x q", "pq"], 0, {1: "Las abreviaturas de chat no van.", 2: "Las abreviaturas de chat no van."}, "<strong>porque</strong>, completo."),
        ("Le pide a su supervisor un cambio de turno:", ["¿Sería posible cambiar mi turno del martes?", "Oye, cámbiame el turno del martes, ¿va?"], 0, {1: "Con el supervisor, mejor usted y una petición cortés."}, "Petición cortés: <strong>¿Sería posible…?</strong>"),
        ("Al escribir, en lugar de señalar («ponlo ahí») conviene…", ["nombrar el lugar", "repetir la palabra ahí", "añadir un emoji"], 0, {1: "El lector no ve hacia dónde señala.", 2: "No da la información."}, "<strong>Nombrar</strong>: en la mesa, junto al teléfono."),
    ]
    filas = [
        ("Registro", "Elijo el registro según a quién le escribo y para qué.", "Lo elijo bien, pero se me cuela alguna palabra informal.", "Escribo igual en todas partes (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Marcas", "Reconozco el trato, el vocabulario y la escritura de cada registro.", "Reconozco algunas marcas.", "No distingo las marcas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Transformar", "Paso un mensaje de informal a formal sin cambiar lo que dice.", "Lo paso, pero quedan abreviaturas o muletillas.", "No sé cómo hacerlo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 3. Ya escribe con buena ortografía y elige el registro adecuado. En el Tema 4 volverá a la <strong>lectura</strong>: la idea principal de textos de varios párrafos.</p>"
    glosario = [("Registro", "Manera de usar la lengua según la situación: formal o informal."), ("Muletilla", "Palabra que se repite al hablar sin aportar nada: este, o sea, pues."),
                ("Abreviatura de chat", "Palabra acortada en mensajes: q, xq, tmb."), ("Regionalismo", "Palabra propia de un país o una región: chamba, pega, curro.")]
    conexion = ("<p>En las lecciones 3.1 y 3.2 cuidó la forma de las palabras y los signos. Ahora dará un paso más: elegir las palabras y el tono según a quién le escribe.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si quiere, un mensaje o un correo suyo para revisar.</p>")
    estd = LE.estandares(["L.1.4", "W.3"], base=["L.1.8"], fund=["SL.6"])
    return C.pagina_leccion(N, LE.titulo(N), "Cada situación pide su manera de escribir.", ["Escritura", "Registro"],
                            ["<strong>Distinguir</strong> el registro formal del informal.", "<strong>Reconocer</strong> las diferencias entre la lengua hablada y la escrita.",
                             "<strong>Elegir</strong> el registro según el destinatario y el propósito.", "<strong>Transformar</strong> un mensaje informal en uno formal."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-1", LE.titulo("4-1")), glosario, P)


def practica():
    cl = [{"enun": f"<span class=\"grande\">«{t}»</span><br>¿En qué registro está?", "ops": REG, "ok": k, "enOrden": True,
           "pista": "¿Usa tú o usted? ¿Tiene abreviaturas, emojis o palabras de un solo país?", "exp": f"<strong>{REG[k]}</strong>. {e}"} for t, k, e in CLAS]
    de = [{"enun": f"<strong>{s}</strong>", "ops": ops, "ok": 0, "pista": "Piense en quién recibe el mensaje: ¿es alguien de confianza o una persona con la que debe ser formal?",
           "exp": f"«{ops[0]}»"} for s, ops in DEST]
    tr = [{"enun": f"<span class=\"grande\">«{m}»</span><br>¿Cuál es la mejor versión formal?", "ops": ops, "ok": 0,
           "pista": "Esa versión conserva palabras informales o abreviaturas, o no usa usted.", "exp": f"«{ops[0]}»"} for m, ops in TRANS]
    mods = [("registro", "¿Formal o informal?", C.om("m1", "Lea el mensaje y diga en qué registro está.")),
            ("destinatario", "El destinatario decide", C.om("m2", "Para cada situación, elija cómo empezar, pedir o despedirse.")),
            ("transformar", "Transforme el mensaje", C.om("m3", "Elija la mejor versión formal de un mensaje escrito como un chat."))]
    js = C.js_datos("CL", cl) + C.js_datos("DE", de) + C.js_datos("TR", tr) + 'creaBanco("m1", CL);\ncreaBanco("m2", DE);\ncreaBanco("m3", TR);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
