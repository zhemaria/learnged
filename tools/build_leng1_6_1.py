# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.1 · El poder de las ilustraciones para comprender.
Fuente: clases_leng1/clase_6-1.html (GEDparaHispanos), adaptada al marco de LearnGED.
Las escenas para «leer la imagen» se arman con emojis grandes y una descripción para lectores de pantalla.
Uso: python3 tools/build_leng1_6_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-1"
# (emojis, descripción, tema correcto, dos distractores)
ESCENAS = [("🏥 👩‍⚕️ 💉", "Un hospital, una enfermera y una jeringa.", "La salud y la atención médica", ["Un partido de fútbol", "La cosecha del maíz"]),
           ("🌱 👨‍🌾 🚜 🌽", "Plantas que brotan, un agricultor, un tractor y una mazorca.", "La agricultura y el campo", ["La vida en una gran ciudad", "Una erupción volcánica"]),
           ("🌋 🔥 🌑", "Un volcán con fuego, de noche.", "Los volcanes y sus erupciones", ["Una fiesta de cumpleaños", "Cómo cuidar el jardín"]),
           ("🏙️ 🚕 🚇 🚦", "Edificios altos, un taxi, el metro y un semáforo.", "La vida y el transporte en la ciudad", ["La pesca en el mar", "Los animales de la granja"]),
           ("🌀 🌊 🏠 ⛈️", "Un huracán, olas grandes, una casa y una tormenta.", "Los huracanes y sus daños", ["Las vacaciones en la playa", "La construcción de casas"]),
           ("🗳️ 🏛️ 📜", "Una urna de votación, un edificio de gobierno y un documento.", "Las elecciones y el gobierno", ["La historia de los museos", "El correo postal"]),
           ("🦷 🪥 🍬", "Un diente, un cepillo de dientes y un dulce.", "El cuidado de los dientes", ["La fábrica de dulces", "Los deportes de invierno"]),
           ("☀️ ➡️ 🔋 ➡️ 💡 🏠", "El sol carga una batería que enciende la luz de una casa.", "La energía solar en el hogar", ["El pronóstico del tiempo", "La venta de casas"]),
           ("🐝 🌸 🍎", "Una abeja, una flor y una manzana.", "Las abejas y las frutas que comemos", ["Los peligros de las picaduras", "La decoración con flores"]),
           ("🧓 👵 💊 📋", "Dos personas mayores, medicinas y una lista.", "La salud de las personas mayores", ["La escuela primaria", "Un viaje en avión"]),
           ("🚰 💧 🧪", "Una llave de agua, una gota y un tubo de laboratorio.", "La calidad del agua potable", ["Los deportes acuáticos", "La cocina de la abuela"]),
           ("💼 📝 🤝", "Un maletín, un formulario y dos manos que se saludan.", "Buscar trabajo y la entrevista de empleo", ["Las vacaciones de verano", "La siembra de árboles"])]
# (emojis, descripción, oración que la describe, dos distractores)
DESCRIBE = [("🌧️ ☂️ 🚶", "Lluvia, un paraguas y una persona caminando.", "Una persona camina bajo la lluvia con paraguas.", ["Una persona toma el sol en la playa.", "Una persona duerme en su cama."]),
            ("🎂 🎈 👨‍👩‍👧", "Un pastel, globos y una familia.", "Una familia celebra un cumpleaños.", ["Una familia va al médico.", "Una familia limpia la casa."]),
            ("🚌 ⏰ 🏃", "Un autobús, un reloj y una persona corriendo.", "Una persona corre para no perder el autobús.", ["Una persona maneja un camión.", "Una persona espera sentada en casa."]),
            ("❄️ ⛄ 🧤", "Nieve, un muñeco de nieve y guantes.", "Es invierno y hace mucho frío.", ["Es verano y hace calor.", "Es un día de lluvia en primavera."]),
            ("📚 ✏️ 👩‍🏫", "Libros, un lápiz y una maestra.", "Una maestra da una clase.", ["Una cocinera prepara la cena.", "Una doctora atiende a un paciente."]),
            ("🛒 🍎 🥖 💵", "Un carrito, una manzana, un pan y dinero.", "Alguien hace las compras de comida.", ["Alguien cocina en un restaurante.", "Alguien siembra en el huerto."]),
            ("🔥 🚒 👨‍🚒", "Fuego, un camión de bomberos y un bombero.", "Los bomberos apagan un incendio.", ["Los bomberos hacen una fiesta.", "Un chef enciende la estufa."]),
            ("🏖️ ☀️ 🐚", "Una playa, el sol y una concha.", "Un día de sol en la playa.", ["Una tormenta en la montaña.", "Una noche de nieve en la ciudad."])]
PASOS = ["Mirar la imagen con calma, sin leer el texto.", "Predecir de qué va a tratar el texto.", "Leer el texto escrito.", "Comprobar si la predicción fue correcta."]


def escena(emo, desc, grande=True):
    return f'<span class="escena" role="img" aria-label="{desc}">{emo}</span>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En el GED, sobre todo en Ciencias y en Estudios Sociales, muchas preguntas vienen con fotos, ilustraciones, mapas, tablas o gráficas. Saber leerlas se llama <strong>alfabetización visual</strong>, y es tan importante como leer letras.</p>
<p>Cuando leemos, el cerebro hace dos trabajos a la vez: <strong>descifrar</strong> las palabras y <strong>entender</strong> lo que quieren decir. Si las palabras son difíciles, casi toda la energía se va en descifrar. Una buena imagen ayuda con el segundo trabajo: muestra de qué se habla.</p>
{C.tabla("El mismo texto, sin imagen y con imagen", ["Sin imagen", "Con imagen"],
         [["«La célula procariota no tiene un núcleo definido; su material genético está suelto en el citoplasma, a diferencia de la célula eucariota.»<br>⚠️ Cuesta más entenderlo.",
           f"{escena('🦠 ⟷ 🔵', 'Dos células: una sin núcleo y otra con un núcleo en el centro.')}<br><strong>Procariota:</strong> sin núcleo · <strong>Eucariota:</strong> con núcleo.<br>✅ Cuesta menos entenderlo."]])}
{C.caja("tip", "Idea central", "<p>La ilustración no es un adorno. Dirige la atención a lo importante y le da al cerebro un apoyo para comprender. No lee por usted, pero le ayuda a entender lo que lee.</p>")}"""

    s2 = f"""<h3>La técnica de las dos lecturas</h3>
{C.tabla("Las dos lecturas", ["Paso", "Qué hacer"],
         [["1 · Leer la imagen", "Antes de leer una palabra, mire la foto o el dibujo. ¿Qué veo? ¿Qué personas, lugares u objetos? ¿Qué está pasando?"],
          ["2 · Predecir", "Con lo que vio, diga de qué va a tratar el texto (como en la Lección 4.1)."],
          ["3 · Leer el texto", "Ahora sí, lea. Lo entenderá con más facilidad."],
          ["4 · Comprobar", "¿Se cumplió su predicción? Ajústela si hace falta."]])}
{C.caja("tip", "¿Por qué funciona?", "<p>Porque despierta lo que usted ya sabe. Al ver un volcán, el cerebro recuerda lava, calor y erupciones antes de leer: las palabras difíciles del texto ya tienen dónde acomodarse.</p>")}
<h3>Lea las imágenes</h3>
{P("Mire la imagen", f"{escena(*ESCENAS[0][:2])}<br>¿De qué va a tratar el texto?", [ESCENAS[0][2]] + ESCENAS[0][3], 0, {1: "No hay nada de deportes en la imagen.", 2: "No hay campo ni maíz."}, f"<strong>{ESCENAS[0][2]}</strong>: hospital, enfermera, jeringa.")}
{P("Mire la imagen", f"{escena(*ESCENAS[2][:2])}<br>¿De qué va a tratar el texto?", [ESCENAS[2][2]] + ESCENAS[2][3], 0, {1: "No hay pastel ni globos.", 2: "No hay plantas."}, f"<strong>{ESCENAS[2][2]}</strong>.")}
{P("Mire la imagen", f"{escena(*ESCENAS[3][:2])}<br>¿De qué va a tratar el texto?", [ESCENAS[3][2]] + ESCENAS[3][3], 0, {1: "No hay mar ni peces.", 2: "No hay animales."}, f"<strong>{ESCENAS[3][2]}</strong>.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · con una imagen de verdad</span>
<p>Busque un artículo con una foto en un periódico, una revista, un folleto de la clínica o una página de noticias. Tape el texto y mire solo la imagen. En su cuaderno escriba tres cosas que ve y una predicción: «Creo que el texto va a hablar de…». Después lea el texto y termine: «Mi predicción fue correcta / casi correcta / no fue correcta porque…».</p></div>
<details class="caja caja-tip"><summary><strong>Ver un ejemplo</strong></summary>
<p><strong>Imagen:</strong> una calle con agua hasta las rodillas, un carro detenido y personas con botas de goma.</p>
<ul><li><strong>Veo:</strong> agua en toda la calle, un carro parado y gente con botas.</li><li><strong>Predicción:</strong> «Creo que el texto va a hablar de una inundación después de una tormenta».</li>
<li><strong>Después de leer:</strong> «Fue casi correcta: el texto habla de una tubería rota, no de una tormenta. Pero sí era sobre agua en la calle».</li></ul>
<p>Una predicción que no se cumple también sirve: lo preparó para leer con atención.</p></details>"""

    secciones = [("s1", "Las imágenes ayudan a comprender", s1), ("s2", "Leer la imagen primero", s2), ("s3", "Práctica: antes de leer, la foto", s3)]
    tarea = [("Mis imágenes con historia.", "Elija dos fotos: una de su familia o su barrio (que se pueda mostrar) y una que acompañe un artículo."),
             ("Lo que se ve.", "Para cada una, escriba qué se ve (personas, lugar, objetos, lo que pasa) y un párrafo de dos o tres oraciones que cuente la historia de la foto."),
             ("La predicción.", "Con la foto del artículo, escriba su predicción antes de leer y si se cumplió después."),
             ("Compártalo.", "Muestre la foto familiar a alguien de su casa y pregúntele qué historia ve. ¿Coincide con la suya?")]
    quiz = [
        ("¿Qué es la alfabetización visual?", ["Saber leer imágenes, mapas, tablas y gráficas", "Saber dibujar", "Leer en voz alta"], 0, {1: "No se trata de dibujar.", 2: "No."}, "Saber <strong>leer imágenes</strong>."),
        ("¿Qué dos trabajos hace el cerebro al leer?", ["Descifrar las palabras y entender lo que dicen", "Mirar y dibujar", "Contar y sumar"], 0, {1: "No.", 2: "No."}, "<strong>Descifrar y entender.</strong>"),
        ("¿Cómo ayuda una imagen?", ["Muestra de qué se habla y apoya la comprensión", "Lee por usted", "Solo adorna"], 0, {1: "No lee por usted.", 2: "No es solo un adorno."}, "<strong>Apoya la comprensión.</strong>"),
        ("En la técnica de las dos lecturas, ¿qué se hace primero?", ["Mirar la imagen", "Leer el texto", "Responder las preguntas"], 0, {1: "El texto va después.", 2: "Eso va al final."}, "<strong>Mirar la imagen.</strong>"),
        ("¿Qué se hace después de mirar la imagen?", ["Predecir de qué tratará el texto", "Cerrar el libro", "Saltar el texto"], 0, {1: "No.", 2: "No."}, "<strong>Predecir.</strong>"),
        ("¿Por qué funciona la técnica?", ["Despierta lo que ya sabemos del tema", "Hace el texto más corto"], 0, {}, "Despierta el <strong>conocimiento previo</strong>."),
        (f"{escena(*ESCENAS[4][:2])}<br>¿De qué tratará el texto?", [ESCENAS[4][2]] + ESCENAS[4][3], 0, {1: "Hay tormenta y olas peligrosas, no vacaciones.", 2: "No se ve a nadie construyendo."}, f"<strong>{ESCENAS[4][2]}</strong>."),
        ("Si su predicción no se cumple, ¿qué pasa?", ["También sirvió: lo preparó para leer con atención", "Leyó mal y debe empezar de nuevo"], 0, {}, "<strong>También sirvió.</strong>"),
        ("¿En qué materias del GED hay más imágenes?", ["Ciencias y Estudios Sociales", "Ninguna"], 0, {}, "<strong>Ciencias y Estudios Sociales</strong>, aunque aparecen en todas."),
        ("¿Cuál es el último paso de las dos lecturas?", ["Comprobar la predicción", "Mirar la imagen", "Predecir"], 0, {1: "Ese es el primero.", 2: "Ese es el segundo."}, "<strong>Comprobar.</strong>"),
    ]
    filas = [
        ("Leer la imagen", "Describo personas, lugar, objetos y lo que pasa.", "Veo algo, pero me quedo corto.", "No sé qué mirar (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Predecir", "Predigo el tema del texto a partir de la imagen.", "A veces mi predicción no se apoya en la imagen.", "No predigo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Comprobar", "Reviso mi predicción después de leer.", "A veces se me olvida.", "No comparo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe usar las imágenes para entender mejor. En la próxima lección verá las demás señales que el autor pone en un artículo: <strong>título, subtítulos, rótulos y pies de foto</strong>.</p>"
    glosario = [("Alfabetización visual", "Saber leer imágenes, mapas, tablas y gráficas."), ("Ilustración", "Dibujo o foto que acompaña a un texto."),
                ("Conocimiento previo", "Lo que usted ya sabe de un tema antes de leer."), ("Predicción", "Lo que uno cree que va a pasar o que va a decir el texto.")]
    conexion = ("<p>Hasta ahora trabajó con el texto escrito. Ahora va a dar un paso que le abre las puertas de los exámenes de Ciencias y de Estudios Sociales: leer las imágenes.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un periódico, una revista o una página de noticias con fotos.</p>")
    estd = LE.estandares(["R.7.4"], base=["R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Una imagen no es un adorno: es una herramienta para comprender.", ["R.7 · Información visual", "Alfabetización visual"],
                            ["<strong>Explicar</strong> cómo una imagen ayuda a comprender un texto.", "<strong>Leer</strong> una imagen: personas, lugar, objetos y acción.",
                             "<strong>Predecir</strong> el tema de un texto a partir de su imagen.", "<strong>Aplicar</strong> la técnica de las dos lecturas."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-2", LE.titulo("6-2")), glosario, P)


def practica():
    pre = [{"enun": f"{escena(e, d)}<br>Mire la imagen. ¿De qué va a tratar el texto?", "ops": [ok] + dis, "ok": 0, "pista": "Nombre lo que ve, uno por uno. ¿Qué tienen en común?",
            "exp": f"<strong>{ok}</strong>: la imagen muestra {d[0].lower() + d[1:]}"} for e, d, ok, dis in ESCENAS]
    des = [{"enun": f"{escena(e, d)}<br>¿Qué oración describe mejor la imagen?", "ops": [ok] + dis, "ok": 0, "pista": "Fíjese en cada parte de la imagen: ¿qué oración las incluye todas?",
            "exp": f"<strong>{ok}</strong>"} for e, d, ok, dis in DESCRIBE]
    orden = [{"titulo": "La técnica de las dos lecturas", "intro": "Ordene los pasos con los botones ▲ y ▼.", "pasos": PASOS, "inicio": ini, "cons": {},
              "general": "Primero la imagen, después la predicción, luego el texto y al final la comprobación."} for ini in ([2, 0, 3, 1], [3, 1, 0, 2], [1, 3, 2, 0])]
    mods = [("predecir", "¿De qué va a tratar?", C.om("m1", "Mire la imagen y prediga el tema del texto.")),
            ("describir", "¿Qué muestra la imagen?", C.om("m2", "Elija la oración que describe la imagen.")),
            ("pasos", "Los pasos de las dos lecturas", C.orden("m3"))]
    js = C.js_datos("PRE", pre) + C.js_datos("DES", des) + C.js_datos("ORD", orden) + 'creaBanco("m1", PRE);\ncreaBanco("m2", DES);\ncreaOrden("m3", ORD);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
