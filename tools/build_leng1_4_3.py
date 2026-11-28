# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.3 · A la caza de la idea principal.
Fuente: clases_leng1/clase_4-3.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_4_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "4-3"

# (párrafo, posición 0 inicio / 1 medio / 2 final, idea correcta, demasiado amplia, demasiado estrecha)
PARRAFOS = [
    ("Caminar todos los días tiene muchos beneficios para la salud. Mejora el corazón, ayuda a dormir mejor, baja la presión arterial y mantiene el peso saludable. Caminar 30 minutos al día es suficiente para sentir la diferencia.",
     0, "Caminar todos los días es bueno para la salud.", "El ejercicio es importante.", "Caminar ayuda a dormir mejor."),
    ("A muchas personas no les gustan los gimnasios. Pero caminar todos los días tiene muchos beneficios para la salud. Mejora el corazón, ayuda a dormir mejor y baja la presión arterial. Lo mejor es que solo necesita sus zapatos.",
     1, "Caminar todos los días es bueno para la salud.", "A la gente no le gustan los gimnasios.", "Caminar baja la presión arterial."),
    ("El parque del barrio se llena los domingos. Las familias llegan temprano con comida para compartir. Los niños juegan al fútbol y los abuelos conversan a la sombra. Por la tarde, algunos vecinos tocan música. El parque es el corazón de la vida del barrio.",
     2, "El parque es el centro de la vida del barrio.", "Los barrios tienen muchas cosas.", "Los niños juegan al fútbol."),
    ("Mucha gente piensa que cocinar en casa toma demasiado tiempo. Sin embargo, cocinar en casa tiene grandes ventajas. Se gasta menos dinero que comiendo en la calle. Uno sabe qué ingredientes lleva la comida. Además, es una ocasión para compartir con la familia.",
     1, "Cocinar en casa tiene grandes ventajas.", "La comida es necesaria.", "Cocinar en casa cuesta menos."),
    ("Las bibliotecas públicas ofrecen mucho más que libros. Tienen computadoras con internet gratis. Muchas dan clases de inglés y de ciudadanía. También prestan películas y tienen actividades para niños.",
     0, "Las bibliotecas públicas ofrecen muchos servicios.", "Leer es bueno.", "Las bibliotecas tienen computadoras."),
    ("El autobús llegó con veinte minutos de retraso. Después, el elevador del trabajo estaba descompuesto y Rosa subió seis pisos a pie. A la hora del almuerzo se le cayó el café sobre la camisa. Para Rosa, fue un lunes terrible.",
     2, "Rosa tuvo un lunes muy malo.", "Los lunes existen.", "El elevador estaba descompuesto."),
    ("Antes, para pagar la luz había que ir a una oficina y hacer fila. Hoy, la tecnología facilita los pagos de la casa. Se pueden pagar las cuentas desde el celular. Los bancos mandan avisos cuando se acerca la fecha. Y muchos pagos se pueden programar para que salgan solos.",
     1, "La tecnología hace más fácil pagar las cuentas.", "La tecnología cambió el mundo.", "Los bancos mandan avisos."),
    ("Los perros son buenos compañeros para las personas mayores. Los obligan a salir a caminar todos los días. Les dan cariño y compañía. Además, ayudan a sentirse más seguros en casa.",
     0, "Los perros son buenos compañeros para los mayores.", "Los animales son interesantes.", "Los perros obligan a caminar."),
    ("Ana estudia inglés en el autobús. Por la noche, cuando los niños duermen, repasa sus apuntes. Los sábados va a la biblioteca a practicar con otras personas. Ana se esfuerza mucho para aprender inglés.",
     2, "Ana se esfuerza mucho para aprender inglés.", "Aprender es importante.", "Ana estudia en el autobús."),
    ("Los huracanes causan mucho daño en el Caribe. Sus vientos arrancan árboles y techos. Las lluvias inundan calles y casas. Muchas familias se quedan sin luz durante días.",
     0, "Los huracanes causan mucho daño en el Caribe.", "La naturaleza es poderosa.", "Las lluvias inundan las calles."),
]
POS = ["Al inicio", "En el medio", "Al final"]


def svg_sol():
    aria = "Organizador en forma de sol. En el centro, la idea principal: Los huracanes causan mucho daño en el Caribe. Alrededor, tres rayos con los detalles: vientos que arrancan árboles y techos, inundaciones, y familias sin luz."
    F = 'font-family="Segoe UI, Arial, sans-serif"'
    s = [f'<svg class="recorrido" style="max-width:640px" viewBox="0 0 640 330" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">']
    for x2, y2 in ((120, 70), (520, 70), (320, 300)):
        s.append(f'<line x1="320" y1="165" x2="{x2}" y2="{y2}" stroke="#f5b301" stroke-width="10" stroke-linecap="round"/>')
    s.append('<circle cx="320" cy="165" r="98" fill="#fff3c4" stroke="#b45309" stroke-width="4"/>')
    for i, l in enumerate(["Los huracanes", "causan mucho daño", "en el Caribe"]):
        s.append(f'<text x="320" y="{145 + 24 * i}" text-anchor="middle" {F} font-size="19" font-weight="700" fill="#5c3900">{l}</text>')
    for (x, y, a, b) in ((120, 52, "Vientos que arrancan", "árboles y techos"), (520, 52, "Lluvias que inundan", "calles y casas"), (320, 300, "Familias sin luz", "durante días")):
        s.append(f'<rect x="{x - 110}" y="{y - 36}" width="220" height="56" rx="10" fill="#e3f0f8" stroke="#0b679c" stroke-width="2"/>')
        s.append(f'<text x="{x}" y="{y - 12}" text-anchor="middle" {F} font-size="15" fill="#004b75">{a}</text><text x="{x}" y="{y + 8}" text-anchor="middle" {F} font-size="15" fill="#004b75">{b}</text>')
    s.append("</svg>")
    return "".join(s)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>La <strong>idea principal</strong> es el mensaje central de un párrafo: lo que explica de qué se trata todo lo que está leyendo. Las demás oraciones son <strong>detalles</strong>: ejemplos, datos o descripciones que la apoyan.</p>
{C.caja("tip", "La prueba del párrafo", "<p>Si quita la idea principal, el párrafo se queda vacío y pierde su sentido. Si quita un detalle, todavía se entiende. Por eso la idea principal es la oración más importante.</p>")}
<h3>El sol y sus rayos</h3>
<p>Imagine que la idea principal es el sol y los detalles son sus rayos: los rayos no existen sin el sol, y el sol no se ve sin sus rayos.</p>
{svg_sol()}
{C.caja("ojo", "Ni muy amplia ni muy estrecha", "<p>Una buena idea principal no es <strong>demasiado amplia</strong> (<em>«la naturaleza es poderosa»</em>: cabe en mil textos) ni <strong>demasiado estrecha</strong> (<em>«las lluvias inundan las calles»</em>: es solo un detalle). Está en el medio: cubre todo el párrafo y dice algo concreto.</p>")}
{P("Compruebe", f"<div class=\"texto-lectura\"><p>{PARRAFOS[4][0]}</p></div>¿Cuál es la idea principal?", [PARRAFOS[4][3], PARRAFOS[4][2], PARRAFOS[4][4]], 1,
   {0: "Es demasiado amplia: el párrafo no habla de leer en general.", 2: "Es solo un detalle: las computadoras son uno de los servicios."}, f"<strong>{PARRAFOS[4][2]}</strong> Las demás oraciones son los servicios que la prueban.")}"""

    s2 = f"""<p>Mucha gente cree que la idea principal siempre está en la primera oración. No siempre. El autor puede ponerla en tres lugares:</p>
{C.tabla("Dónde puede estar la idea principal", ["Lugar", "Cómo lo hace el autor"],
         [["⬆️ Al inicio", "Dice la idea de entrada y después la apoya con detalles. Es lo más común."],
          ["↔️ En el medio", "Empieza con un ejemplo, una pregunta o lo que otros piensan; después da la idea y termina con más apoyo. Palabras como <em>pero</em> o <em>sin embargo</em> suelen anunciarla."],
          ["⬇️ Al final", "Da primero los detalles y guarda la idea como conclusión. Palabras como <em>por eso</em> o <em>en resumen</em> suelen anunciarla."]])}
<h3>La misma idea en tres lugares</h3>
<div class="texto-lectura"><p><strong>1 · Al inicio.</strong> <mark>Caminar todos los días tiene muchos beneficios para la salud.</mark> Mejora el corazón, ayuda a dormir mejor, baja la presión arterial y mantiene el peso saludable. Caminar 30 minutos al día es suficiente para sentir la diferencia.</p>
<p><strong>2 · En el medio.</strong> A muchas personas no les gustan los gimnasios. Pero <mark>caminar todos los días tiene muchos beneficios para la salud.</mark> Mejora el corazón, ayuda a dormir mejor y baja la presión arterial. Lo mejor es que solo necesita sus zapatos.</p>
<p><strong>3 · Al final.</strong> Caminar mejora el corazón. También ayuda a dormir mejor y baja la presión arterial. Caminar 30 minutos al día mantiene el peso saludable y no necesita equipo especial. Por todo eso, <mark>caminar todos los días tiene muchos beneficios para la salud.</mark></p></div>
{C.caja("tip", "Mire también el título", "<p>Muchas veces el título ya avisa cuál va a ser la idea principal. En el examen GED, las preguntas de idea principal son de las más comunes: <em>¿Cuál es la idea principal del párrafo 2?</em></p>")}
{P("Compruebe", f"<div class=\"texto-lectura\"><p>{PARRAFOS[5][0]}</p></div>¿Dónde está la idea principal?", POS, 2,
   {0: "La primera oración es un detalle: un problema del día.", 1: "Las oraciones del medio cuentan más problemas: son detalles."}, "<strong>Al final</strong>: «Para Rosa, fue un lunes terrible» reúne todos los detalles.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · el mapa de la idea, en su cuaderno</span>
<p>Lea este párrafo en voz alta. Dibuje en su cuaderno un sol como el de la sección 1: la idea principal en el centro y los detalles como rayos. Anote también dónde está la idea: al inicio, en el medio o al final.</p></div>
<div class="texto-lectura"><p>{PARRAFOS[3][0]}</p></div>
<details class="caja caja-tip"><summary><strong>Ya hice mi mapa: ver el modelo</strong></summary>
<p><strong>Idea principal (el sol):</strong> cocinar en casa tiene grandes ventajas. Está <strong>en el medio</strong>: la primera oración solo dice lo que mucha gente piensa, y el «sin embargo» anuncia la idea del autor.</p>
<p><strong>Detalles (los rayos):</strong> se gasta menos dinero · se sabe qué ingredientes lleva · se comparte con la familia.</p></details>"""

    secciones = [("s1", "¿Qué es la idea principal?", s1), ("s2", "Dónde se esconde la idea principal", s2), ("s3", "Actividad: el mapa de la idea", s3)]
    tarea = [("Una idea en una oración.", f"Lea este párrafo y escriba su idea principal en una sola oración, con sus palabras; después diga dónde está.<br><em>{PARRAFOS[2][0]}</em>"),
             ("Tres párrafos de su vida.", "Busque tres párrafos cortos (de una noticia, un folleto o un libro) y subraye en cada uno la oración que dice la idea principal. Si no hay una oración así, escríbala usted."),
             ("Revise su respuesta.", "La idea principal del párrafo del parque está al final: «El parque es el corazón de la vida del barrio». ¿Coincide con la suya? ¿La escribió con sus palabras?")]
    quiz = [
        ("¿Qué es la idea principal?", ["El mensaje central del párrafo", "La primera palabra", "El detalle más curioso"], 0, {1: "No es una palabra suelta.", 2: "Los detalles apoyan la idea principal."}, "El <strong>mensaje central</strong>."),
        ("¿Qué pasa si se quita la idea principal de un párrafo?", ["El párrafo pierde su sentido", "No pasa nada"], 0, {}, "El párrafo <strong>pierde su sentido</strong>."),
        ("¿Dónde puede estar la idea principal?", ["Solo al inicio", "Al inicio, en el medio o al final", "Solo en el título"], 1, {0: "No siempre está al inicio.", 2: "El título ayuda, pero la idea está en el párrafo."}, "<strong>Al inicio, en el medio o al final.</strong>"),
        ("¿Cuál es una idea <strong>demasiado amplia</strong> para un párrafo sobre los beneficios de caminar?", ["El ejercicio es importante.", "Caminar es bueno para la salud.", "Caminar baja la presión."], 0, {1: "Esa es la idea principal justa.", 2: "Esa es un detalle: es demasiado estrecha."}, "<strong>El ejercicio es importante</strong>: cabe en mil textos."),
        ("¿Cuál es un <strong>detalle</strong>, no la idea principal?", ["Las bibliotecas ofrecen muchos servicios.", "Las bibliotecas prestan películas."], 1, {}, "<strong>Prestar películas</strong> es uno de los servicios: un detalle."),
        ("¿Qué palabras suelen anunciar la idea principal al final?", ["por eso, en resumen", "había una vez", "por ejemplo"], 0, {1: "Así empiezan los cuentos.", 2: "Por ejemplo anuncia un detalle."}, "<strong>Por eso, en resumen</strong>."),
        (f"<em>{PARRAFOS[8][0]}</em> ¿Dónde está la idea principal?", POS, 2, {0: "La primera oración es un ejemplo de su esfuerzo.", 1: "Las del medio son más ejemplos."}, "<strong>Al final</strong>: «Ana se esfuerza mucho para aprender inglés»."),
        (f"<em>{PARRAFOS[7][0]}</em> ¿Cuál es la idea principal?", [PARRAFOS[7][2], PARRAFOS[7][3], PARRAFOS[7][4]], 0, {1: "Demasiado amplia.", 2: "Es solo un detalle."}, f"<strong>{PARRAFOS[7][2]}</strong>"),
        ("¿Qué representan los rayos del sol en el organizador?", ["Los detalles", "La idea principal", "El título"], 0, {1: "La idea principal es el sol.", 2: "El título no está en el organizador."}, "Los <strong>detalles</strong>."),
        ("¿Qué palabra suele anunciar la idea principal en el medio, después de lo que otros piensan?", ["sin embargo", "primero", "ayer"], 0, {1: "Primero ordena pasos.", 2: "Ayer dice cuándo."}, "<strong>Sin embargo</strong> (o <em>pero</em>)."),
    ]
    filas = [
        ("Encontrar la idea principal", "La encuentro esté donde esté y la digo con mis palabras.", "La encuentro cuando está al inicio.", "Elijo un detalle (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Ni amplia ni estrecha", "Distingo la idea justa de una demasiado amplia y de un detalle.", "Me confundo con la idea amplia.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Ubicar la idea", "Digo si está al inicio, en el medio o al final.", "Me cuesta cuando está en el medio.", "Creo que siempre está al inicio (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe cazar la idea principal. En la próxima lección mirará de cerca a los rayos del sol: los <strong>detalles de apoyo</strong>, sus tipos y el detalle «intruso» que no apoya nada.</p>"
    glosario = [("Idea principal", "El mensaje central de un párrafo o de un texto."), ("Detalle de apoyo", "Oración que explica o prueba la idea principal."),
                ("Demasiado amplia", "Idea tan general que no dice nada concreto del párrafo."), ("Demasiado estrecha", "Idea que es solo un detalle y no cubre todo el párrafo.")]
    conexion = ("<p>Ya conoce las cuatro estrategias de la lectura activa. Ahora va a trabajar una destreza central del examen GED: encontrar la idea principal. Todo texto bien escrito tiene un mensaje central que organiza lo demás; si no lo encuentra, el texto se vuelve una lista de datos sueltos.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y tres párrafos cortos de su vida diaria.</p>")
    estd = LE.estandares(["R.2.1", "R.2.4", "R.2.5"])
    return C.pagina_leccion(N, LE.titulo(N), "Todo párrafo tiene un sol; búsquelo.", ["R.2 · Idea principal"],
                            ["<strong>Reconocer</strong> la idea principal de un párrafo y separarla de los detalles.", "<strong>Distinguir</strong> una idea justa de una demasiado amplia o demasiado estrecha.",
                             "<strong>Ubicar</strong> la idea principal al inicio, en el medio o al final.", "<strong>Dibujar</strong> el mapa de la idea: el sol y sus rayos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-4", LE.titulo("4-4")), glosario, P)


def practica():
    cual = [{"enun": f"<div class=\"texto-lectura\"><p>{p}</p></div>¿Cuál es la idea principal?", "ops": [ok, a, e], "ok": 0,
             "pistas": {1: "Esa es demasiado amplia: podría ser de cualquier texto.", 2: "Esa es solo un detalle: no cubre todo el párrafo."}, "exp": f"<strong>{ok}</strong>"} for p, pos, ok, a, e in PARRAFOS]
    donde = [{"enun": f"<div class=\"texto-lectura\"><p>{p}</p></div>¿Dónde está la idea principal?", "ops": POS, "ok": pos, "enOrden": True,
              "pista": "Busque la oración que reúne a todas las demás. Fíjese en palabras como pero, sin embargo o por eso.", "exp": f"<strong>{POS[pos]}</strong>: «{ok[:-1].lower()}»."} for p, pos, ok, a, e in PARRAFOS]
    tipo = []
    for p, pos, ok, a, e in PARRAFOS:
        for t, k in ((ok, 0), (a, 1), (e, 2)):
            tipo.append({"enun": f"<div class=\"texto-lectura\"><p>{p}</p></div>¿Cómo es esta idea para el párrafo?<br><strong>«{t}»</strong>",
                         "ops": ["La idea principal justa", "Demasiado amplia", "Demasiado estrecha (un detalle)"], "ok": k, "enOrden": True,
                         "pista": "Amplia: podría ser de cualquier texto. Estrecha: es solo una parte del párrafo.", "exp": ["Cubre todo el párrafo y dice algo concreto.", "Podría servir para muchos textos distintos.", "Es solo una parte: un detalle del párrafo."][k]})
    mods = [("cual", "¿Cuál es la idea principal?", C.om("m1", "Lea el párrafo y elija la idea principal: ni muy amplia ni muy estrecha.")),
            ("donde", "¿Dónde está la idea principal?", C.om("m2", "Diga si está al inicio, en el medio o al final.")),
            ("amplia", "¿Justa, amplia o estrecha?", C.om("m3", "Decida cómo es cada idea para el párrafo."))]
    js = (C.js_datos("CUA", cual) + C.js_datos("DON", donde) + C.js_datos("TIP", tipo) + 'creaBanco("m1", CUA);\ncreaBanco("m2", DON);\ncreaBanco("m3", TIP);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
