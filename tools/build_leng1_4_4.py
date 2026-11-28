# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.4 · Los detalles que sostienen la idea.
Fuente: clases_leng1/clase_4-4.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Datos del huracán Ike: National Hurricane Center, Tropical Cyclone Report AL092008 (2009, actualizado en 2014),
y Federación Internacional de la Cruz Roja, llamamiento MDRCU0001 (2008).
Uso: python3 tools/build_leng1_4_4.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "4-4"
TIPOS = ["Ejemplo", "Dato", "Descripción"]
DETALLES = [("En Baracoa, por ejemplo, olas enormes pasaron por encima de las casas.", 0), ("Los vientos llegaron a unas 130 millas por hora.", 1),
            ("Las calles quedaron inundadas y muchas casas perdieron el techo.", 2), ("El huerto tiene 15 parcelas, una para cada familia.", 1),
            ("Las plantas verdes y las flores amarillas llenan de color el terreno.", 2), ("La señora Elena, por ejemplo, ya no compra tomates.", 0),
            ("Caminar 30 minutos al día baja la presión arterial.", 1), ("Mi vecino Pedro, por ejemplo, perdió diez libras caminando.", 0),
            ("El parque huele a pasto recién cortado y se oyen pájaros.", 2), ("La biblioteca presta más de 2,000 libros al mes.", 1),
            ("Mi primo, por ejemplo, encontró trabajo por internet.", 0), ("La cocina era pequeña, con paredes amarillas y una ventana al patio.", 2),
            ("El 40 % de los estudiantes trabaja de día.", 1), ("Los sábados, por ejemplo, la clínica atiende sin cita.", 0), ("El café humeaba en la taza blanca.", 2)]
# (idea principal, tres que apoyan, una intrusa)
INTRUSOS = [("Caminar todos los días es bueno para la salud.", ["Mejora el corazón.", "Ayuda a dormir mejor.", "Baja la presión arterial."], "Chicago tiene muchos parques bonitos."),
            ("Aprender a usar la computadora ayuda en la vida adulta.", ["Permite buscar trabajo por internet.", "Facilita escribir a la escuela de los hijos.", "Sirve para pagar cuentas desde casa."], "Las computadoras de antes eran grandes y grises."),
            ("Las bibliotecas ofrecen muchos servicios gratis.", ["Prestan libros y películas.", "Tienen computadoras con internet.", "Dan clases de inglés."], "Algunas bibliotecas son edificios muy antiguos."),
            ("Desayunar bien ayuda a rendir en el trabajo.", ["Da energía para la mañana.", "Ayuda a concentrarse.", "Evita comer de más al mediodía."], "Mi tía vende pan en el mercado."),
            ("Los huertos comunitarios mejoran el barrio.", ["Llenan de color terrenos vacíos.", "Las familias cosechan sus verduras.", "Los niños aprenden de dónde viene la comida."], "Los tomates son originarios de América."),
            ("Ahorrar un poco cada semana sirve de mucho.", ["Ayuda en una emergencia.", "Permite comprar algo grande sin deudas.", "Da tranquilidad."], "Los bancos abren a las nueve."),
            ("Leer con los hijos los ayuda en la escuela.", ["Aprenden palabras nuevas.", "Les gusta más la lectura.", "Pasan tiempo con la familia."], "Los libros infantiles tienen muchos colores."),
            ("El transporte público ahorra dinero.", ["No se paga gasolina.", "No se paga estacionamiento.", "El pase mensual cuesta menos que el seguro del carro."], "Los autobuses de Chicago son azules y blancos.")]
IKE = "El huracán Ike causó mucho daño en Cuba en 2008. Llegó a la provincia de Holguín con vientos de unas 130 millas por hora, y en todo el país más de 300,000 viviendas sufrieron daños. Las calles quedaron inundadas y muchas casas perdieron el techo. En Baracoa, por ejemplo, olas enormes pasaron por encima de las casas de la costa."
HUERTO = "Los huertos comunitarios mejoran la vida del barrio. El huerto de mi calle tiene 15 parcelas, una para cada familia. Las plantas verdes y las flores amarillas llenan de color un terreno que antes estaba vacío. La señora Elena, por ejemplo, ya no compra tomates en la tienda: los cosecha ella misma. Además, los niños aprenden de dónde vienen los alimentos."
COMPU = "Aprender a usar la computadora ayuda mucho en la vida adulta. Permite buscar trabajo y llenar solicitudes por internet. Mi primo, por ejemplo, encontró su empleo actual en una página de anuncios. Las computadoras de antes eran grandes y grises. Además, con el correo electrónico es fácil comunicarse con la escuela de los hijos."


def leccion():
    P = C.Practicas()
    s1 = f"""<p>La idea principal sola no basta: necesita <strong>detalles de apoyo</strong> que la expliquen y la hagan creíble. Los detalles funcionan como <strong>pruebas</strong>: razones, ejemplos o datos que muestran por qué la idea es verdad.</p>
<div class="texto-lectura"><p><mark>El huracán Ike causó mucho daño en Cuba en 2008.</mark> Llegó a la provincia de Holguín con vientos de unas 130 millas por hora, y en todo el país más de 300,000 viviendas sufrieron daños. Las calles quedaron inundadas y muchas casas perdieron el techo. En Baracoa, por ejemplo, olas enormes pasaron por encima de las casas de la costa.</p>
<p class="nota-fina">Datos: Centro Nacional de Huracanes de los Estados Unidos, informe sobre el huracán Ike (2008), y Cruz Roja Internacional.</p></div>
<p>La idea principal (resaltada) dice <strong>qué pasó</strong>. Los detalles dicen <strong>cuánto, cómo y dónde</strong>. Sin ellos, la idea sería solo una afirmación sin pruebas.</p>
<h3>Tres clases de detalles</h3>
{C.tabla("Tres formas de apoyar una idea", ["Tipo", "Qué es", "Ejemplo del párrafo de Ike"],
         [["💡 Ejemplo", "Un caso concreto que muestra la idea. Suele llevar <em>por ejemplo</em>.", "En Baracoa, por ejemplo, olas enormes pasaron por encima de las casas."],
          ["🔢 Dato", "Un número, una cantidad, una fecha, un porcentaje.", "Los vientos llegaron a unas 130 millas por hora."],
          ["🖼️ Descripción", "Lo que se ve, se oye o se siente: ayuda a imaginar.", "Las calles quedaron inundadas y muchas casas perdieron el techo."]])}
{C.caja("tip", "Un buen párrafo mezcla los tres", "<p>Datos para dar peso, ejemplos para concretar, descripciones para imaginar. En el GED, cuando un texto argumenta, los <strong>datos</strong> y los <strong>ejemplos</strong> son la evidencia que usted tendrá que evaluar.</p>")}
{P("Compruebe", "<em>El huerto tiene 15 parcelas, una para cada familia.</em> ¿Qué tipo de detalle es?", TIPOS, 1,
   {0: "No es un caso de una persona o un lugar concreto.", 2: "No describe cómo se ve: da una cantidad."}, "Es un <strong>dato</strong>: da un número.")}"""

    s2 = f"""<p>A veces un párrafo tiene una oración que no se conecta con la idea principal. Es un <strong>detalle intruso</strong>: sobra, no aporta, distrae. Saber detectarlo es una destreza del examen GED.</p>
{C.caja("ojo", "Cómo detectar un intruso", "<p>Pregúntese en cada oración: <strong>«¿Esta oración me ayuda a entender o a probar la idea principal?»</strong> Si la respuesta es no, es un intruso, aunque hable de algo parecido.</p>")}
<div class="texto-lectura"><p><mark>Caminar todos los días tiene muchos beneficios para la salud.</mark> Mejora el corazón y baja la presión arterial. <s>La ciudad de Chicago tiene muchos parques bonitos.</s> Ayuda a controlar el peso y a dormir mejor. Lo mejor es que no necesita equipo especial.</p></div>
<p>«La ciudad de Chicago tiene muchos parques bonitos» habla de Chicago, no de los beneficios de caminar. Aunque suene relacionada (se camina en los parques), no apoya la idea.</p>
{P("Compruebe", "Idea: <em>Ahorrar un poco cada semana sirve de mucho.</em> ¿Cuál es la intrusa?", ["Ayuda en una emergencia.", "Los bancos abren a las nueve.", "Da tranquilidad."], 1,
   {0: "Es una razón para ahorrar: apoya la idea.", 2: "Es una razón para ahorrar: apoya la idea."}, "<strong>Los bancos abren a las nueve</strong>: es verdad, pero no dice por qué ahorrar sirve.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Lea el párrafo. Divida una hoja en dos columnas: a la izquierda, la idea principal; a la derecha, tres detalles con su tipo (ejemplo, dato o descripción). Después compare.</p></div>
<div class="texto-lectura"><p>{HUERTO}</p></div>
<details class="caja caja-tip"><summary><strong>Ya hice mi tabla: ver el modelo</strong></summary>
<p><strong>Idea principal:</strong> los huertos comunitarios mejoran la vida del barrio (al inicio).</p>
<ul><li><strong>Dato:</strong> el huerto tiene 15 parcelas, una para cada familia.</li><li><strong>Descripción:</strong> las plantas verdes y las flores amarillas llenan de color el terreno.</li><li><strong>Ejemplo:</strong> la señora Elena ya no compra tomates.</li></ul>
<p>La última oración (los niños aprenden) también apoya la idea: es otra razón por la que el huerto mejora el barrio.</p></details>"""

    secciones = [("s1", "Los detalles: las pruebas de la idea", s1), ("s2", "El detalle intruso", s2), ("s3", "Práctica: la idea y sus detalles", s3)]
    tarea = [("Mi mapa de la idea.", f"Copie este párrafo en su cuaderno. Escriba la idea principal, dos detalles con su tipo, y marque la oración intrusa explicando por qué no apoya la idea.<br><em>{COMPU}</em>"),
             ("Compruebe su mapa.", "La intrusa es «Las computadoras de antes eran grandes y grises»: describe las computadoras, pero no dice por qué aprender a usarlas ayuda. ¿La encontró?"),
             ("Un texto de su vida.", "En una noticia o un folleto, busque un dato, un ejemplo y una descripción, y cópielos.")]
    quiz = [
        ("¿Qué hacen los detalles de apoyo?", ["Explican y prueban la idea principal", "Cambian de tema", "Repiten el título"], 0, {1: "Eso hace el intruso.", 2: "Repetir no apoya."}, "<strong>Explican y prueban</strong> la idea principal."),
        ("¿Cuáles son los tres tipos de detalles?", ["Ejemplos, datos y descripciones", "Títulos, comas y puntos", "Sujetos, verbos y adjetivos"], 0, {1: "Eso es puntuación.", 2: "Eso es gramática."}, "<strong>Ejemplos, datos y descripciones.</strong>"),
        ("<em>Los vientos llegaron a unas 130 millas por hora.</em> ¿Qué tipo es?", TIPOS, 1, {0: "No es un caso concreto.", 2: "No dice cómo se ve: da un número."}, "Un <strong>dato</strong>."),
        ("<em>Mi vecino Pedro, por ejemplo, perdió diez libras caminando.</em> ¿Qué tipo es?", TIPOS, 0, {1: "Tiene un número, pero sobre todo es el caso de una persona.", 2: "No describe cómo se ve algo."}, "Un <strong>ejemplo</strong>: el caso concreto de Pedro."),
        ("<em>El café humeaba en la taza blanca.</em> ¿Qué tipo es?", TIPOS, 2, {0: "No es un caso que pruebe algo.", 1: "No tiene números."}, "Una <strong>descripción</strong>: lo que se ve."),
        ("¿Qué es un detalle <strong>intruso</strong>?", ["Una oración que no apoya la idea principal", "La idea principal", "El detalle más importante"], 0, {1: "La idea principal no es intrusa.", 2: "El intruso no apoya nada."}, "Una oración que <strong>no apoya</strong> la idea."),
        ("¿Qué pregunta ayuda a encontrar el intruso?", ["¿Esta oración apoya la idea principal?", "¿Esta oración es la más larga?"], 0, {}, "<strong>¿Esta oración apoya la idea principal?</strong>"),
        ("Idea: <em>El transporte público ahorra dinero.</em> ¿Cuál es la intrusa?", ["No se paga gasolina.", "No se paga estacionamiento.", "Los autobuses de Chicago son azules y blancos."], 2, {0: "Explica el ahorro.", 1: "Explica el ahorro."}, "<strong>El color de los autobuses</strong> no dice nada del ahorro."),
        ("¿Qué palabra anuncia muchas veces un ejemplo?", ["por ejemplo", "sin embargo", "ayer"], 0, {1: "Anuncia un contraste.", 2: "Dice cuándo."}, "<strong>por ejemplo</strong>."),
        ("¿Por qué son útiles los datos?", ["Dan peso y precisión a la idea", "Hacen el texto más largo"], 0, {}, "Dan <strong>peso y precisión</strong>: son evidencia."),
    ]
    filas = [
        ("Reconocer los detalles", "Separo la idea principal de sus detalles en cualquier párrafo.", "A veces confundo un detalle con la idea.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Clasificar los detalles", "Digo si un detalle es ejemplo, dato o descripción.", "Confundo el ejemplo con la descripción.", "No sé clasificarlos (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Encontrar el intruso", "Encuentro la oración que no apoya y explico por qué.", "La encuentro, pero no sé explicar por qué.", "No la veo (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe ver cómo se sostiene un párrafo: la idea principal y sus pruebas. En la próxima lección aprenderá a descifrar palabras desconocidas sin diccionario, con las <strong>claves del contexto</strong>.</p>"
    glosario = [("Detalle de apoyo", "Oración que explica o prueba la idea principal."), ("Ejemplo", "Caso concreto que muestra la idea."), ("Dato", "Número, cantidad, fecha o porcentaje."),
                ("Descripción", "Lo que se ve, se oye o se siente."), ("Detalle intruso", "Oración que no apoya la idea principal.")]
    conexion = ("<p>En la Lección 4.3 aprendió a encontrar la idea principal. Pero la idea sola no basta: necesita detalles que la expliquen y la hagan creíble. Sin detalles, la idea queda vacía; sin idea principal, los detalles no tienen sentido.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un folleto o una noticia corta.</p>")
    estd = LE.estandares(["R.2.5", "R.8.2"], base=["R.8.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Una idea sin pruebas es solo una opinión.", ["R.2.5 · Detalles de apoyo", "R.8.2 · Evidencia"],
                            ["<strong>Reconocer</strong> los detalles que apoyan la idea principal.", "<strong>Clasificar</strong> los detalles: ejemplo, dato o descripción.",
                             "<strong>Detectar</strong> el detalle intruso que no apoya la idea.", "<strong>Hacer</strong> el mapa de un párrafo: idea y detalles."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-5", LE.titulo("4-5")), glosario, P)


def practica():
    tip = [{"enun": f"<strong>{d}</strong><br>¿Qué tipo de detalle es?", "ops": TIPOS, "ok": k, "enOrden": True,
            "pista": "Ejemplo: un caso concreto (por ejemplo…). Dato: un número. Descripción: lo que se ve, se oye o se siente.", "exp": f"Es <strong>{TIPOS[k].lower()}</strong>."} for d, k in DETALLES]
    intr = [{"enun": f"Idea principal: <strong>{i}</strong><br>¿Cuál de estas oraciones <strong>no</strong> la apoya?", "ops": a + [x], "ok": 3,
             "pista": "Pregúntese en cada una: ¿me ayuda a entender o a probar la idea?", "exp": f"<strong>{x}</strong> no dice nada que pruebe la idea."} for i, a, x in INTRUSOS]
    par = []
    for n, (i, a, x) in enumerate(INTRUSOS):
        orden = a[:n % 3] + [x] + a[n % 3:]
        par.append({"enun": "<div class=\"texto-lectura\"><p>" + " ".join([i] + orden) + "</p></div>¿Qué oración <strong>sobra</strong> en este párrafo?", "ops": orden, "ok": orden.index(x), "enOrden": True,
                    "pista": "La primera oración es la idea principal. Busque la que no la apoya.", "exp": f"<strong>{x}</strong> no apoya la idea: {i[0].lower() + i[1:]}"})
    mods = [("tipos", "¿Ejemplo, dato o descripción?", C.om("m1", "Clasifique cada detalle.")),
            ("intruso", "Encuentre el intruso", C.om("m2", "Tres oraciones apoyan la idea; una no.")),
            ("parrafo", "La oración que sobra", C.om("m3", "Lea el párrafo completo y busque la oración que no apoya la idea."))]
    js = C.js_datos("TIP", tip) + C.js_datos("INT", intr) + C.js_datos("PAR", par) + 'creaBanco("m1", TIP);\ncreaBanco("m2", INT);\ncreaBanco("m3", PAR);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
