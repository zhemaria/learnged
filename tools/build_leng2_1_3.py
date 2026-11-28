# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 1.3 · Fluidez lectora: precisión, ritmo y expresión.
Fuente: clases_leng2/clase_1-3.html (GEDparaHispanos) y gramatica/n2-l1-3.html, adaptadas al marco de LearnGED.
La Lección 1.3 del Nivel 1 ya trabaja la fluidez básica con «La llamada»; esta lección sube el nivel: comas que cambian el
sentido (vocativo y aposición), entonación por tipo de oración, el diálogo con raya y textos más largos, con meta de unas
100 palabras por minuto.
Uso: python3 tools/build_leng2_1_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "1-3"
PAUSAS = [("No, quiero café.", ["Pide café", "No quiere café"], 0, "La coma separa el «no»: dice que no a otra cosa y pide café."),
          ("No quiero café.", ["Pide café", "No quiere café"], 1, "Sin coma, el «no» niega el café."),
          ("María, la doctora llamó.", ["Le hablo a María", "María es la doctora"], 0, "Le cuento a María que llamó la doctora."),
          ("María, la doctora, llamó.", ["Le hablo a María", "María es la doctora"], 1, "Las dos comas encierran una explicación: «la doctora» es María."),
          ("Pedro, come.", ["Le pido a Pedro que coma", "Cuento que Pedro come"], 0, "La coma separa el nombre de la persona a quien se le habla."),
          ("Pedro come.", ["Le pido a Pedro que coma", "Cuento que Pedro come"], 1, "Sin coma, es una afirmación sobre Pedro."),
          ("Ana, mi prima viene mañana.", ["Le hablo a Ana", "Ana es mi prima"], 0, "Le aviso a Ana que viene mi prima."),
          ("Ana, mi prima, viene mañana.", ["Le hablo a Ana", "Ana es mi prima"], 1, "«Mi prima» explica quién es Ana."),
          ("Luis, vamos a comer.", ["Invito a Luis a comer", "Cuento que Luis va a comer"], 0, "Le hablo a Luis: la coma lo separa."),
          ("Luis va a comer.", ["Invito a Luis a comer", "Cuento que Luis va a comer"], 1, "Es una afirmación sobre lo que hará Luis.")]
ENTON = [("Quiere saber si su hijo ya terminó la tarea.", "¿Terminaste la tarea?", ["Terminaste la tarea.", "¡Terminaste la tarea!"], "Pregunta de sí o no: la voz sube al final."),
         ("Le alegra que su hijo por fin haya terminado.", "¡Terminaste la tarea!", ["¿Terminaste la tarea?", "Terminaste la tarea."], "Hay emoción: exclamación."),
         ("Ve llegar el autobús y avisa con prisa a su amiga.", "¡Llegó el autobús!", ["¿Llegó el autobús?", "Llegó el autobús."], "Un aviso urgente es una exclamación."),
         ("Quiere saber a qué hora abre la clínica.", "¿A qué hora abre la clínica?", ["La clínica abre temprano.", "¡Qué temprano abre la clínica!"], "Pregunta con <em>qué</em>: la voz empieza alta y baja al final."),
         ("Quiere saber si queda leche en el refrigerador.", "¿Queda leche?", ["Queda leche.", "¡Queda leche!"], "Pregunta de sí o no."),
         ("Le sorprende ver nieve en pleno abril.", "¡Está nevando en abril!", ["¿Está nevando en abril?", "Está nevando en abril."], "La sorpresa se expresa con exclamación."),
         ("Le explica a un compañero el horario de la tienda, sin emoción especial.", "La tienda cierra a las nueve.", ["¿La tienda cierra a las nueve?", "¡La tienda cierra a las nueve!"], "Es una afirmación: la voz baja al final."),
         ("Busca una farmacia y le pregunta a alguien en la calle.", "¿Dónde queda la farmacia?", ["La farmacia queda cerca.", "¡Qué cerca queda la farmacia!"], "Pregunta con <em>dónde</em>."),
         ("Su amiga consiguió un trabajo nuevo y usted la felicita.", "¡Felicidades por tu nuevo trabajo!", ["¿Tienes un trabajo nuevo?", "Tienes un trabajo nuevo."], "Felicitar es expresar alegría: exclamación."),
         ("Le cuenta al médico cómo se siente.", "Me duele la cabeza desde ayer.", ["¿Me duele la cabeza desde ayer?", "¡Me duele la cabeza desde ayer!"], "Informa un hecho: afirmación.")]
TEXTOS = [("La biblioteca del barrio", ["La biblioteca del barrio abre todos los días a las nueve. Allí se pueden pedir libros prestados, usar las computadoras y leer el periódico sin pagar nada.",
                                         "Los martes por la tarde hay clases gratuitas de inglés, y los sábados por la mañana, una hora de cuentos para niños. Para sacar libros solo hace falta la tarjeta de la biblioteca, que se obtiene con una identificación y un comprobante de domicilio. ¿Ya tiene la suya?"]),
          ("El mercado del sábado", ["Todos los sábados, la calle principal se llena de puestos de colores. Hay frutas, verduras, pan recién hecho y flores. Don Ernesto vende los mejores mangos del mercado; siempre le regala uno a cada niño que pasa.",
                                     "—¡Pruebe este, señora, que está dulcísimo! —grita con alegría.",
                                     "Al mediodía, cuando el sol aprieta, la gente busca la sombra de los árboles y compra agua fresca de jamaica. A las tres, los puestos se recogen y la calle vuelve a quedar en silencio."]),
          ("Mi primer día de trabajo", ["Mi primer día en la fábrica empezó muy temprano. Llegué a las seis menos cuarto, nervioso y con mucho sueño. Un supervisor me recibió en la puerta, me dio un casco y unas gafas de seguridad, y me explicó las reglas: nunca correr, usar siempre el equipo y avisar de cualquier problema.",
                                        "Mis compañeros me ayudaron toda la mañana. A la hora del almuerzo, uno de ellos me preguntó:", "—¿Qué tal te va?", "—Mejor de lo que pensaba —le respondí."])]
FRASES = ("Cuando llegué a Chicago / no conocía a nadie. // Los primeros meses / trabajé de noche en una panadería / y estudié inglés por la mañana. // "
          "Hoy, / después de cinco años, / tengo amigos, / un trabajo de día / y muchas ganas de seguir aprendiendo.")


def texto_lectura(tid, parrafos):
    return f'<div class="texto-lectura" id="{tid}">' + "".join(f"<p>{p}</p>" for p in parrafos) + "</div>"


def crono(cid, tid):
    return f'''<div class="crono" id="{cid}" data-texto="{tid}">
<p class="crono-reloj" id="{cid}-tiempo" aria-live="off">0:00</p>
<p><button type="button" class="btn" id="{cid}-empezar">Empezar</button> <button type="button" class="btn-sec" id="{cid}-terminar" disabled>Terminar</button></p>
<p class="fb" id="{cid}-res" role="status" aria-live="polite"></p>
<table class="tabla-ej"><caption>Resultados de mis pasadas</caption><thead><tr><th scope="col">Pasada</th><th scope="col">Tiempo</th><th scope="col">Palabras por minuto</th></tr></thead><tbody><tr><td>—</td><td>Todavía no hay pasadas.</td><td></td></tr></tbody></table>
<p>Los resultados se borran al cerrar la página. Anótelos en su cuaderno.</p>
</div>'''


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En el Nivel 1 practicó la fluidez con textos cortos. Ahora va a leer textos más largos, con diálogos y comas que cambian el sentido. Recuerde las tres partes:</p>
{C.tabla("Las tres partes de la fluidez", ["Parte", "Qué significa", "Error típico"],
         [["Precisión", "Leer cada palabra tal como está escrita.", "Saltarse palabras o cambiar <em>casa</em> por <em>cosa</em>."],
          ["Ritmo", "Una velocidad cómoda, como al hablar.", "Leer palabra por palabra, o tan rápido que no se entiende."],
          ["Expresión", "Las pausas y el tono que pide el texto.", "Leer una pregunta como si fuera una afirmación."]])}
<h3>Leer por grupos de sentido</h3>
<p>Un buen lector no lee palabra por palabra: agrupa las palabras que van juntas en el sentido. En este texto, cada <strong>/</strong> es una pausa breve y cada <strong>//</strong>, una pausa más larga.</p>
<div class="texto-lectura"><p>{FRASES}</p></div>
{LE.escuchar(FRASES.replace(" // ", ". ").replace(" / ", ", ").replace("//", "").replace("/", ""), "Escuchar la lectura por grupos")}
{C.caja("tip", "Pruébelo", "<p>Lea el texto dos veces: primero haciendo las pausas marcadas; después, en un texto sin marcas, decidiendo usted dónde van. Notará que entiende más.</p>")}"""

    s2 = f"""<h3>Una coma cambia el sentido</h3>
{C.tabla("Con coma y sin coma", ["Oración", "Qué quiere decir"],
         [["No, quiero agua.", "Dice que no a otra cosa y pide agua."], ["No quiero agua.", "No quiere agua."],
          ["Juan, mi vecino vino.", "Le hablo a Juan para contarle que vino mi vecino."], ["Juan, mi vecino, vino.", "Vino Juan, que es mi vecino."]])}
{C.caja("tip", "Dos usos de la coma que cambian la lectura", "<ul><li>El <strong>nombre de la persona a quien se le habla</strong> va separado por coma: «Juan, ven».</li><li>Una <strong>explicación</strong> va entre dos comas: «Juan, mi vecino, vino».</li></ul>")}
{P("Compruebe", "<em>María, la doctora, llamó.</em> ¿Qué quiere decir?", ["María es la doctora, y llamó", "Le hablo a María para contarle que llamó la doctora"], 0, {}, "Las dos comas encierran una explicación: <strong>la doctora es María</strong>.")}
<h3>La entonación</h3>
{C.tabla("Tipos de oración y su entonación", ["Tipo", "Qué hace la voz", "Ejemplo"],
         [["Afirmación", "Baja al final.", "El autobús llegó tarde."], ["Pregunta de sí o no", "Sube al final.", "¿El autobús llegó tarde?"],
          ["Pregunta con qué, dónde, cuándo, quién, cómo", "Empieza alta en esa palabra y baja al final.", "¿Cuándo llegó el autobús?"], ["Exclamación", "Más fuerza y emoción.", "¡El autobús llegó tarde otra vez!"]])}
{LE.escuchar("El autobús llegó tarde. ¿El autobús llegó tarde? ¿Cuándo llegó el autobús? ¡El autobús llegó tarde otra vez!", "Escuchar los cuatro ejemplos")}
{C.caja("ojo", "Mire antes de leer", "<p>En español, los signos de pregunta y de exclamación se escriben al principio y al final. Cuando vea <strong>¿</strong> o <strong>¡</strong>, prepare la voz desde esa palabra.</p>")}
<h3>El diálogo con raya</h3>
<p>En español, el diálogo se marca con <strong>raya (—)</strong>. La raya al comienzo de la línea indica que alguien habla; las rayas del medio encierran las palabras del narrador: «—¡Pruebe este, señora! <em>—grita con alegría</em>.» Al leer, cambie un poco la voz entre el personaje y el narrador.</p>"""

    lecturas = "".join(f"<h3>{t}</h3>{texto_lectura('tx' + str(i), ps)}{LE.escuchar(' '.join(ps), 'Escuchar el modelo')}{crono('cr' + str(i), 'tx' + str(i))}" for i, (t, ps) in enumerate(TEXTOS[:1], 1))
    s3 = f"""<p>Escuche el modelo siguiendo el texto con la vista. Después lea en voz alta tres veces con el cronómetro: en cada pasada, mejore una cosa (menos tropiezos, mejores pausas o más expresión).</p>
{lecturas}
{C.caja("tip", "¿Cuánto es bueno?", "<p>Lo más importante es <strong>mejorar de una pasada a otra sin perder precisión</strong>. Como orientación, en este nivel un buen objetivo es leer un texto como este a unas <strong>100 palabras por minuto</strong> con muy pocos tropiezos. Si lee más rápido pero se salta palabras, baje la velocidad.</p>")}
{C.tabla("Rúbrica de fluidez", ["Criterio", "1 · Empezando", "2 · En camino", "3 · Bien", "4 · Muy bien"],
         [["Precisión", "Muchos tropiezos.", "Varios tropiezos.", "Uno o dos tropiezos.", "Lee todas las palabras como están."], ["Ritmo", "Palabra por palabra.", "Lento, con paradas largas.", "Casi siempre cómodo.", "Natural, como si hablara."],
          ["Pausas", "No respeta los signos.", "Respeta algunos.", "Respeta casi todos.", "Respeta todos los signos."], ["Expresión", "Voz plana.", "A veces cambia el tono.", "Preguntas y exclamaciones bien.", "Da vida al texto y a los personajes."]])}
<p>Encontrará dos textos más en la práctica de esta lección.</p>"""

    secciones = [("s1", "Leer por grupos de sentido", s1), ("s2", "Comas, entonación y diálogo", s2), ("s3", "Lectura repetida con cronómetro", s3)]
    tarea = [("Mis tres pasadas.", "Lea «La biblioteca del barrio» tres veces con el cronómetro y anote en su cuaderno las palabras por minuto de cada pasada."),
             ("Mi grabación.", "Grábese leyendo uno de los textos de la práctica. Escúchese y califíquese con la rúbrica."),
             ("Mis grupos de sentido.", "Copie un párrafo de un periódico y marque con / y // dónde haría las pausas. Léalo en voz alta.")]
    quiz = [
        ("¿Qué es leer con fluidez?", ["Leer con precisión, buen ritmo y expresión", "Leer lo más rápido posible"], 0, {}, "<strong>Precisión, ritmo y expresión.</strong>"),
        ("¿Qué es leer por grupos de sentido?", ["Juntar las palabras que van juntas en el sentido", "Leer palabra por palabra"], 0, {}, "<strong>Agrupar</strong> las palabras que van juntas."),
        ("<em>Pedro, come.</em> ¿Qué quiere decir?", ["Le pido a Pedro que coma", "Cuento que Pedro come"], 0, {}, "Le hablo a Pedro: la coma separa su nombre."),
        ("<em>Ana, mi prima, viene mañana.</em>", ["Ana es mi prima", "Le hablo a Ana"], 0, {}, "Las dos comas encierran una explicación."),
        ("En una pregunta de sí o no, la voz…", ["sube al final", "baja al final"], 0, {}, "<strong>Sube</strong> al final."),
        ("¿Para qué sirve el signo <strong>¿</strong> al principio?", ["Para preparar la voz desde el comienzo", "Solo de adorno"], 0, {}, "Para <strong>preparar la voz</strong>."),
        ("¿Qué marca la raya (—) en un diálogo?", ["Que habla un personaje, o las palabras del narrador", "El final del texto"], 0, {}, "El <strong>diálogo</strong>."),
        ("Quiere saber si queda leche. ¿Cómo se escribe?", ["¿Queda leche?", "¡Queda leche!", "Queda leche."], 0, {1: "No hay emoción: es una pregunta.", 2: "Es una pregunta."}, "<strong>¿Queda leche?</strong>"),
        ("Si lee más rápido pero se salta palabras, conviene…", ["bajar la velocidad", "leer aún más rápido"], 0, {}, "<strong>Bajar la velocidad</strong>: primero la precisión."),
        ("¿Qué es lo más importante entre una pasada y otra?", ["Mejorar sin perder precisión", "Terminar en menos de un minuto"], 0, {}, "<strong>Mejorar</strong> sin perder precisión."),
    ]
    filas = [
        ("Precisión", "Leo todas las palabras como están.", "Tengo algunos tropiezos.", "Me salto o cambio palabras (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Pausas y comas", "Respeto los signos y sé cuándo una coma cambia el sentido.", "Respeto los puntos, pero no siempre las comas.", "Leo sin pausas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Expresión", "Leo preguntas, exclamaciones y diálogos con el tono justo.", "A veces.", "Leo con voz plana (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Terminó el Tema 1. Ya lee palabras largas y textos completos con fluidez. En el Tema 2 estudiará la <strong>gramática de la oración</strong>, empezando por los sustantivos y los adverbios.</p>"
    glosario = [("Fluidez", "Leer con precisión, ritmo y expresión."), ("Grupo de sentido", "Palabras que se leen juntas porque forman una idea."),
                ("Entonación", "La «música» de la voz: sube, baja o se hace más fuerte."), ("Raya", "Signo (—) que marca el diálogo en español."),
                ("Palabras por minuto", "Medida de la velocidad de lectura.")]
    conexion = ("<p>En las dos lecciones anteriores aprendió a leer palabras largas por sílabas y por partes. Ahora une todo: leer un texto completo en voz alta como un buen lector, para que la mente quede libre para entender.</p>"
                "<p><strong>Lo que necesita:</strong> un lugar tranquilo para leer en voz alta y, si puede, el teléfono para grabarse.</p>")
    estd = LE.estandares([], base=["R.2.1"], fund=["RF.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Leer como se habla: con precisión, ritmo y expresión.", ["Fundamentos de lectura", "Fluidez"],
                            ["<strong>Leer</strong> por grupos de sentido.", "<strong>Interpretar</strong> las comas que cambian el significado.",
                             "<strong>Dar</strong> la entonación de afirmaciones, preguntas y exclamaciones, y leer diálogos con raya.", "<strong>Medir</strong> y mejorar la velocidad con lectura repetida."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-1", LE.titulo("2-1")), glosario, P)


def practica():
    pz = [{"enun": f"<strong class=\"grande\">{f}</strong> {LE.escuchar(f, '')}<br>¿Qué quiere decir?", "ops": o, "ok": k, "enOrden": True, "pista": "", "exp": e} for f, o, k, e in PAUSAS]
    en = [{"enun": f"<strong>{s}</strong><br>¿Cómo se escribe?", "ops": [ok] + d, "ok": 0, "pista": "¿Es una pregunta, una emoción o un dato?", "exp": f"<strong>{ok}</strong> {e}"} for s, ok, d, e in ENTON]
    lect = "".join(f"<h3>{t}</h3>{texto_lectura('px' + str(i), ps)}{LE.escuchar(' '.join(ps), 'Escuchar el modelo')}{crono('pc' + str(i), 'px' + str(i))}" for i, (t, ps) in enumerate(TEXTOS[1:], 1))
    mods = [("pausas", "Las comas cambian el sentido", C.om("m1", "Lea la oración (o escúchela) y elija qué quiere decir.")),
            ("entonacion", "Situación y entonación", C.om("m2", "Elija la oración que corresponde a la situación.")),
            ("lectura", "Lectura repetida", "<p>Lea cada texto tres veces con el cronómetro.</p>" + lect)]
    js = C.js_datos("PZ", pz) + C.js_datos("EN", en) + 'creaBanco("m1", PZ);\ncreaBanco("m2", EN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
