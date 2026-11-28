# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 8.2 · Comprensión auditiva y presentación oral con audio.
Fuente: clases_leng2/clase_8-2.html (GEDparaHispanos) y gramatica/n2-l8-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_8_2.py
"""
import os, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng2_7_1 import taller

LE.nivel(2)
N = "8-2"
NOTICIA = ("Buenos días. Les informamos que el lunes abrió sus puertas una nueva clínica comunitaria en el barrio Las Flores. La clínica atenderá de lunes a sábado, de ocho de la mañana a ocho de la noche. "
           "Ofrece consultas médicas, vacunas y atención dental, y su personal habla inglés y español. Según la directora, la doctora Inés Vargas, la clínica se construyó porque los vecinos tenían que viajar más de una hora para ver a un médico. "
           "Como resultado, muchas familias dejaban de ir a sus citas. El precio de las consultas depende de los ingresos de cada familia, y nadie se quedará sin atención por no poder pagar. "
           "El primer día, la clínica atendió a ciento veinte pacientes. Una vecina, la señora Carmen Ruiz, dijo: «Es lo mejor que le ha pasado a este barrio en muchos años». Para pedir una cita, llame a la clínica o visite su página en internet.")
ENTREVISTA = [("Periodista", "Tomás, ¿cómo empezó el huerto?"), ("Tomás", "Hace tres años, este terreno estaba lleno de basura. Un grupo de vecinos pidió permiso a la ciudad para limpiarlo y sembrar."),
              ("Periodista", "¿Y qué cultivan?"), ("Tomás", "Tomates, chiles, calabazas y cilantro. Cada familia cuida su propia parcela."),
              ("Periodista", "¿Qué ha cambiado en el barrio?"), ("Tomás", "Mucho. Como ahora pasamos más tiempo afuera, los vecinos nos conocemos mejor. Además, los niños aprenden de dónde viene la comida. Yo creo que todos los barrios deberían tener un huerto."),
              ("Periodista", "¿Qué necesitan ahora?"), ("Tomás", "Más voluntarios para regar en verano, porque con el calor la tierra se seca muy rápido.")]
AVISO_CITA = "Hola, habla Patricia, del consultorio de la doctora Ríos. Le llamo para recordarle su cita del jueves a las tres y media. Por favor, llegue quince minutos antes y traiga su tarjeta del seguro. Si no puede venir, llámenos al menos un día antes."
AVISO_BIB = "Buenas noches. La biblioteca del barrio ofrecerá clases gratuitas de computación para adultos a partir del primero de marzo. Las clases serán los martes y jueves de seis a ocho. Los cupos son limitados, así que conviene inscribirse pronto en el mostrador principal."
ESC = [("Atención, pasajeros. Debido a obras en la vía, el tren de la línea azul no se detendrá en la estación Damen este fin de semana. Los pasajeros pueden usar el autobús gratuito que sale cada diez minutos desde la estación anterior.", "¿Qué cambia este fin de semana?", ["El tren no se detiene en una estación", "El tren será gratis para todos", "El tren pasará cada diez minutos"], "«…no se detendrá en la estación Damen»."),
       (AVISO_CITA, "¿A qué hora es la cita?", ["A las tres y media", "A las tres y cuarto", "A las cuatro y media"], "Las tres y cuarto es la hora de llegada, no la de la cita."),
       (AVISO_CITA, "¿Qué debe llevar a la cita?", ["La tarjeta del seguro", "Una receta médica", "Los resultados de laboratorio"], "«…traiga su tarjeta del seguro»."),
       ("El pronóstico para mañana: por la mañana, cielo nublado y temperaturas cerca de los cuarenta grados. Por la tarde llegará la lluvia, que podría convertirse en nieve durante la noche. Se recomienda manejar con precaución.", "¿Qué tiempo hará por la tarde?", ["Lluvia", "Nieve", "Sol"], "La nieve llegaría por la noche."),
       (AVISO_BIB, "¿Por qué conviene inscribirse pronto?", ["Porque los cupos son limitados", "Porque las clases son caras", "Porque empiezan mañana"], "«…los cupos son limitados, así que…»."),
       (AVISO_BIB, "¿Cuál es la idea principal del aviso?", ["Habrá clases gratis de computación en la biblioteca", "La biblioteca cerrará los martes y jueves", "La biblioteca necesita computadoras nuevas"], "Es el tema de todo el aviso."),
       ("Señores clientes: les recordamos que la tienda cerrará hoy a las nueve de la noche por inventario. Mañana abriremos en nuestro horario normal, a las siete de la mañana. Gracias por su comprensión.", "¿Por qué cierra la tienda a las nueve hoy?", ["Por inventario", "Por un día festivo", "Por obras en el local"], "«…cerrará hoy a las nueve de la noche por inventario»."),
       ("Hola, mamá. Soy Daniel. Salí tarde del trabajo porque hubo una reunión, así que no voy a llegar a cenar. Guárdame un plato, por favor. Llego como a las diez.", "¿Por qué Daniel no llega a cenar?", ["Porque salió tarde por una reunión", "Porque perdió el autobús", "Porque fue a cenar con amigos"], "Causa: la reunión."),
       ("En la reunión de hoy, el comité de vecinos decidió pintar el salón comunitario el próximo sábado. Se necesitan diez voluntarios. Quien quiera ayudar puede anotarse en la lista de la entrada. La pintura la donó la ferretería de la esquina.", "¿Quién donó la pintura?", ["La ferretería de la esquina", "El comité de vecinos del barrio", "Los diez voluntarios del sábado"], "Último detalle del aviso.")]
HO = ["Hecho", "Opinión"]
HECHO = [("El autobús número nueve pasa cada quince minutos.", 0, "Se comprueba con el horario."), ("Me parece que el autobús es la forma más cómoda de viajar.", 1, "«Me parece» y «la más cómoda»."),
         ("La clínica atendió a ciento veinte pacientes el primer día.", 0, "Es un número que se puede verificar."), ("Esa clínica es la mejor de toda la ciudad.", 1, "«La mejor» es una valoración."),
         ("El lago Míchigan se congela en parte durante los inviernos fríos.", 0, "Se puede observar y comprobar."), ("El invierno en Chicago es insoportable.", 1, "«Insoportable» expresa un sentimiento."),
         ("Creo que la ciudad debería poner más bancas en los parques.", 1, "«Creo que» y «debería»."), ("El parque Grant está junto al lago.", 0, "Se comprueba en un mapa."),
         ("Las clases de inglés son gratuitas en la biblioteca.", 0, "Se puede preguntar y comprobar."), ("Las clases de la biblioteca son increíbles.", 1, "«Increíbles» es una opinión."),
         ("Según el informe de la ciudad, el número de visitantes del parque subió el año pasado.", 0, "Cita un dato de un informe."), ("Todo el mundo debería aprender a cocinar.", 1, "«Debería» señala una opinión.")]
CE = [("Debido a la tormenta de nieve, las escuelas cerraron el lunes.", "¿Cuál es la causa?", ["La tormenta de nieve", "El cierre de las escuelas", "El lunes"], "«Debido a» marca la causa."),
      ("Debido a la tormenta de nieve, las escuelas cerraron el lunes.", "¿Cuál es el efecto?", ["Las escuelas cerraron", "Hubo una tormenta", "Nevó toda la noche"], "Lo que pasó como resultado."),
      ("Ana estudió todas las noches; por eso aprobó el examen.", "¿Cuál es el efecto?", ["Aprobó el examen", "Estudió todas las noches", "Tenía un examen"], "«Por eso» introduce el efecto."),
      ("Como subió el precio de la gasolina, más personas usan el tren.", "¿Cuál es la causa?", ["Subió el precio de la gasolina", "Más personas usan el tren", "El tren es más rápido"], "«Como» al inicio marca la causa."),
      ("La fábrica cerró, así que muchas familias se mudaron.", "¿Cuál es el efecto?", ["Muchas familias se mudaron", "La fábrica cerró", "Las familias buscaron casa"], "«Así que» introduce el efecto."),
      ("Las plantas se secaron porque no llovió en todo el mes.", "¿Cuál es la causa?", ["No llovió en todo el mes", "Las plantas se secaron", "Hacía frío"], "«Porque» introduce la causa."),
      ("El puente estaba en reparación; como resultado, el tráfico se desvió por la avenida.", "¿Cuál es el efecto?", ["El tráfico se desvió", "El puente estaba en reparación", "La avenida es ancha"], "«Como resultado» introduce el efecto."),
      ("A causa de una falla eléctrica, el tren llegó con media hora de retraso.", "¿Cuál es la causa?", ["Una falla eléctrica", "El retraso del tren", "La media hora"], "«A causa de» marca la causa."),
      ("Luis se quedó dormido, así que perdió el autobús y llegó tarde al trabajo.", "¿Qué causó que Luis llegara tarde?", ["Se quedó dormido y perdió el autobús", "El autobús se descompuso en el camino", "Había mucho tráfico en la avenida"], "Una cadena: dormirse → perder el autobús → llegar tarde.")]


def audio(titulo, texto, transcr_html, nota):
    return (f'<div class="caja caja-tip"><p><strong>🎧 {titulo}</strong></p><div class="escucha" data-texto="{H.escape(texto, quote=True)}"><p>Este audio necesita JavaScript.</p></div>'
            f'<details class="transc"><summary>📄 Ver la transcripción (después de escuchar)</summary>{transcr_html}<p class="fuente">{nota}</p></details></div>')


def oye(texto):
    return (f'<p><button type="button" class="btn-sec" data-hablar="{H.escape(texto, quote=True)}" data-vel="0.85">🔊 Escuchar</button></p>'
            f'<details class="transc"><summary>📄 Ver la transcripción</summary><p>{texto}</p></details>')


def leccion():
    P = C.Practicas()
    ent_txt = " ".join(f"{q}: {t}" for q, t in ENTREVISTA)
    s1 = f"""<p>Pasamos más tiempo escuchando que leyendo: las noticias de la radio, los avisos del trabajo, las explicaciones del médico, los mensajes de voz. Escuchar bien es difícil porque las palabras pasan y no vuelven, como en un texto escrito. En esta lección aprenderá una estrategia para no perderse y usará lo que ya sabe de la lectura (idea principal, detalles, hechos y opiniones) con los oídos. Al final grabará su propia presentación.</p>
<p>Los audios usan la voz del navegador. Si no se oyen, puede leer la transcripción de cada uno.</p>
<ol><li><strong>Antes de escuchar:</strong> lea las preguntas. Así sabe qué buscar.</li><li><strong>Primera pasada, la idea general:</strong> escuche sin escribir. ¿De qué trata? ¿Quién habla?</li>
<li><strong>Segunda pasada, los detalles:</strong> escuche con papel y lápiz. Anote números, nombres, fechas y palabras clave, no oraciones completas.</li><li><strong>Después:</strong> responda y compruebe con la transcripción.</li></ol>
{C.caja("tip", "Las señales del que habla", "<p>«Lo más importante es…», «en primer lugar…», «según…», «como resultado…». Cuando las oiga, preste más atención: viene algo importante.</p>")}
<h3>Audio 1: una noticia</h3>
<p>Lea primero las preguntas que están debajo del audio. Después escuche dos veces.</p>
{audio("Noticia: «Abre una clínica comunitaria»", NOTICIA, f"<p>{NOTICIA}</p>", "Noticia inventada para la lección.")}
{P("Noticia 1", "<strong>Primera pasada.</strong> ¿Cuál es la idea principal?", ["Abrió una clínica comunitaria en el barrio Las Flores", "Una vecina habla de los problemas del barrio", "Las consultas médicas son cada vez más caras"], 0, {1: "Es solo un detalle del final.", 2: "La noticia no dice eso."}, "Es de lo que trata toda la noticia.")}
{P("Noticia 2", "<strong>Segunda pasada.</strong> ¿Qué días atiende la clínica?", ["Todos los días de la semana", "De lunes a sábado", "Solo de lunes a viernes"], 1, {0: "El domingo cierra.", 2: "También abre el sábado."}, "«De lunes a sábado, de ocho a ocho».")}
{P("Noticia 3", "¿Cuántos pacientes atendió el primer día?", ["Ochenta", "Doce", "Ciento veinte"], 2, {0: "Escuche otra vez el final.", 1: "Escuche otra vez el final."}, "«…atendió a ciento veinte pacientes».")}
{P("Noticia 4", "¿Quién es Inés Vargas?", ["Una vecina del barrio", "La directora de la clínica", "La periodista que da la noticia"], 1, {0: "La vecina es Carmen Ruiz.", 2: "La periodista no dice su nombre."}, "«Según la directora, la doctora Inés Vargas…».")}"""

    s2 = f"""<p>Lo vio en la Lección 7.2 con textos escritos: un <strong>hecho</strong> se puede comprobar; una <strong>opinión</strong> dice lo que alguien piensa o siente. Al escuchar, las opiniones suelen llegar con estas señales:</p>
<ul><li><strong>Verbos y frases de opinión:</strong> creo que, pienso que, me parece, en mi opinión, debería.</li><li><strong>Palabras que valoran:</strong> lo mejor, lo peor, maravilloso, terrible, increíble.</li>
<li><strong>El tono de voz:</strong> más emoción, más fuerza en ciertas palabras.</li></ul>
{C.caja("ojo", "Cuidado", "<p>Una noticia puede citar una opinión. «La señora Ruiz dijo que es lo mejor del barrio» es un hecho (es verdad que lo dijo), pero <strong>lo que ella dice</strong> es una opinión.</p>")}
{P("¿Hecho u opinión? 1", "«El personal habla inglés y español.»", HO, 0, {1: "Se puede comprobar en la clínica."}, "<strong>Hecho.</strong>")}
{P("¿Hecho u opinión? 2", "«Es lo mejor que le ha pasado a este barrio en muchos años.»", HO, 1, {0: "«Lo mejor» es una valoración."}, "<strong>Opinión</strong> de la señora Ruiz.")}
<h3>Causa y efecto</h3>
<p>La <strong>causa</strong> es por qué pasa algo; el <strong>efecto</strong> es lo que pasa como resultado.</p>
{C.tabla("Señales de causa y de efecto", ["Señales de causa", "Señales de efecto"], [["porque, ya que, debido a, a causa de, como…", "por eso, por lo tanto, como resultado, así que, en consecuencia"]], fila_th=False)}
<p>En la noticia: «La clínica se construyó <strong>porque</strong> los vecinos tenían que viajar más de una hora». Causa: el viaje largo. Efecto: se construyó la clínica. Y otra: «<strong>Como resultado</strong>, muchas familias dejaban de ir a sus citas».</p>
{C.caja("tip", "Prueba rápida", "<p>Una las dos partes con «por eso». «Los vecinos tenían que viajar mucho, por eso se construyó la clínica.» Lo que va antes de «por eso» es la causa.</p>")}
{P("Causa y efecto", "«Debido a la lluvia, se suspendió el partido.» ¿Cuál es la causa?", ["La lluvia", "La suspensión del partido", "El partido"], 0, {1: "Eso es el efecto.", 2: "Busque la señal «debido a»."}, "«Debido a» marca la causa.")}
<h3>Audio 2: una entrevista</h3>
{audio("Entrevista: «El huerto de la calle Quince»", ent_txt, "".join(f"<p><strong>{q}:</strong> {t}</p>" for q, t in ENTREVISTA), "Entrevista inventada para la lección.")}
{P("Entrevista 1", "¿Cómo estaba el terreno hace tres años?", ["Ya tenía un huerto pequeño", "Lleno de basura", "Era un parque con juegos"], 1, {0: "Escuche la primera respuesta.", 2: "Escuche la primera respuesta."}, "«Estaba lleno de basura».")}
{P("Entrevista 2", "Según Tomás, ¿por qué los vecinos se conocen mejor?", ["Porque hacen fiestas cada mes", "Porque pasan más tiempo afuera", "Porque tienen un grupo de mensajes"], 1, {0: "No lo dice.", 2: "No lo dice."}, "Causa: pasan más tiempo afuera.")}
{P("Entrevista 3", "¿Cuál de estas frases de Tomás es una <strong>opinión</strong>?", ["«Todos los barrios deberían tener un huerto.»", "«Cada familia cuida su propia parcela.»", "«Hace tres años el terreno tenía basura.»"], 0, {1: "Es un dato.", 2: "Es un dato."}, "«Deberían» señala una opinión.")}"""

    s3 = f"""<p>Va a contar en unos tres minutos una experiencia suya: su primer trabajo en este país, un viaje, un logro, un día difícil que terminó bien. Use lo que aprendió de la narración (Lección 7.3): escenario, hechos en orden y detalles.</p>
{C.tabla("Guion de «Cuento mi experiencia»", ["Parte", "Qué decir"],
         [["Inicio (30 segundos)", "Hoy les voy a contar… Pasó en… (cuándo y dónde)."], ["Desarrollo (2 minutos)", "Primero… Luego… De repente… Recuerdo que… (detalles: qué veía, oía, sentía)."], ["Cierre (30 segundos)", "Al final… De esa experiencia aprendí que…"]])}
<p>Escriba su guion. No lo va a leer palabra por palabra: le servirá para ordenar las ideas.</p>
{taller("2-8-2", "Mi guion para «Cuento mi experiencia»", "Hoy les voy a contar… Pasó en… Primero… Luego… Al final… De esa experiencia aprendí que…", 8, 150,
        ["primero", "luego", "después", "más tarde", "entonces", "de repente", "al final", "por fin", "recuerdo que", "aprendí que", "por eso", "porque"],
        ["Digo cuándo y dónde pasó.", "Cuento los hechos en orden.", "Incluyo detalles de lo que veía, oía o sentía.", "Tengo un cierre: lo que aprendí.", "Ensayé en voz alta y dura unos tres minutos."])}
{C.caja("tip", "Al hablar", "<p>Hable un poco más despacio que en una conversación, haga pausas entre las partes, mire a la cámara o a su público y varíe el tono. Antes de grabar, ensaye dos o tres veces en voz alta.</p>")}
<h3>Grabe su presentación</h3>
<p>Puede grabarla aquí mismo, desde la computadora o el celular. El navegador le pedirá permiso para usar el micrófono. <strong>La grabación no se envía a ningún lugar:</strong> se queda en su equipo hasta que la descargue.</p>
<div class="grabadora" data-nombre="cuento-mi-experiencia"><p>La grabadora necesita JavaScript.</p></div>
<p>Si prefiere, use la grabadora de voz de su celular. Después, entregue el archivo como le indique su maestro (por ejemplo, en la tarea de Brightspace).</p>
{C.tabla("Rúbrica de comprensión auditiva y presentación", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"],
         [["Ideas y detalles del audio", "Identifica la idea principal y todos los detalles pedidos", "Idea principal y casi todos los detalles", "Solo la idea principal", "No identifica la idea principal"],
          ["Hechos y opiniones", "Los distingue siempre y explica la señal", "Los distingue casi siempre", "Los confunde a menudo", "No los distingue"],
          ["Causa y efecto", "Reconoce causa y efecto y sus señales", "Reconoce la mayoría", "Reconoce alguna con ayuda", "No las reconoce"],
          ["Presentación con audio", "Clara, ordenada, con detalles y buen ritmo", "Clara y ordenada, con pocos detalles", "Se entiende, pero desordenada", "Difícil de seguir"]])}
<p>Total: 16 puntos.</p>"""

    secciones = [("s1", "Escuchar en dos pasadas: una noticia", s1), ("s2", "Hecho, opinión, causa y efecto: una entrevista", s2), ("s3", "Prepare y grabe su presentación", s3)]
    tarea = [("Mi grabación.", "Grabe su presentación «Cuento mi experiencia» (unos tres minutos) y entréguela a su maestro."),
             ("Escuche a un compañero.", "Escuche la grabación de otra persona y coméntela: la idea principal, un detalle que recuerde y un «Me gustó cuando…»."),
             ("Radio en dos pasadas.", "Escuche una noticia breve en la radio o en un pódcast en español. En la primera pasada anote el tema; en la segunda, tres detalles, un hecho y una opinión.")]
    NQ = "<p class=\"fuente\">Pregunta sobre el audio 1 (la clínica), de la sección 1.</p>"
    quiz = [
        ("En la <strong>primera pasada</strong> de un audio conviene…", ["buscar la idea general sin escribir", "anotar todos los números", "copiar las oraciones completas"], 0, {1: "Eso es en la segunda.", 2: "No da tiempo."}, "La <strong>idea general</strong>."),
        ("En la <strong>segunda pasada</strong> conviene anotar…", ["números, nombres y palabras clave", "oraciones completas, palabra por palabra", "solo la primera y la última frase"], 0, {1: "No da tiempo.", 2: "Se pierde lo del medio."}, "<strong>Palabras clave.</strong>"),
        (NQ + "¿Hasta qué hora atiende la clínica?", ["Hasta las ocho de la noche", "Hasta las seis de la tarde", "Hasta la medianoche"], 0, {1: "Escuche otra vez.", 2: "Escuche otra vez."}, "<strong>Hasta las ocho de la noche.</strong>"),
        (NQ + "¿Cómo se decide el precio de las consultas?", ["Según los ingresos de cada familia", "Es el mismo precio para todos", "Es gratis solo los sábados"], 0, {1: "Depende de algo.", 2: "No lo dice."}, "Según los <strong>ingresos</strong>."),
        (NQ + "¿Por qué se construyó la clínica?", ["Porque los vecinos viajaban más de una hora para ver a un médico", "Porque la ciudad tenía dinero que le había sobrado ese año", "Porque la directora vive en el barrio Las Flores desde niña"], 0, {1: "No lo dice.", 2: "No lo dice."}, "Busque «porque» en la noticia."),
        (NQ + "«Es lo mejor que le ha pasado a este barrio.» Esto es…", ["una opinión de la señora Ruiz", "un hecho comprobado por la clínica", "un dato de la directora"], 0, {1: "«Lo mejor» es una valoración.", 2: "Lo dijo una vecina."}, "<strong>Opinión.</strong>"),
        ("«A causa del accidente, el tráfico se detuvo.» ¿Cuál es el <strong>efecto</strong>?", ["El tráfico se detuvo", "El accidente", "La causa del accidente"], 0, {1: "Esa es la causa.", 2: "No es un efecto."}, "El tráfico <strong>se detuvo</strong>."),
        ("¿Qué palabra señala un <strong>efecto</strong>?", ["por eso", "porque", "debido a"], 0, {1: "Señala la causa.", 2: "Señala la causa."}, "<strong>Por eso.</strong>"),
        ("¿Qué señal suele anunciar una opinión al escuchar?", ["«creo que»", "«el lunes»", "«ciento veinte»"], 0, {1: "Es un dato.", 2: "Es un dato."}, "<strong>Creo que.</strong>"),
        ("Antes de grabar una presentación, lo mejor es…", ["ensayarla en voz alta dos o tres veces", "leer el guion lo más rápido posible", "grabarla sin prepararla, para que sea natural"], 0, {1: "Se entiende peor.", 2: "Se desordena."}, "<strong>Ensayar.</strong>"),
    ]
    filas = [
        ("Escuchar", "Escucho en dos pasadas y encuentro la idea general y los detalles.", "Encuentro la idea general, pero pierdo detalles.", "Me pierdo al escuchar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Hecho, opinión, causa", "Distingo hechos y opiniones, y causas y efectos, por sus señales.", "Dudo en algunos casos.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Presentación", "Escribí el guion, ensayé y grabé unos tres minutos.", "Grabé sin ensayar.", "No grabé (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya escucha con estrategia y habla en público. En la última lección hará el <strong>proyecto final</strong> y la <strong>evaluación del Nivel 2</strong>.</p>"
    glosario = [("Pasada", "Cada vez que se escucha un audio."), ("Transcripción", "El texto escrito de lo que se dice en un audio."),
                ("Causa", "Por qué pasa algo."), ("Efecto", "Lo que pasa como resultado.")]
    conexion = ("<p>En la Lección 7.2 distinguió datos y opiniones en textos escritos, y en la 7.3 escribió una narración. Hoy hará lo mismo con los oídos y con su voz.</p>"
                "<p><strong>Lo que necesita:</strong> papel y lápiz, la voz del navegador encendida y, para grabar, un micrófono o un celular.</p>")
    estd = LE.estandares(["R.3.4"], base=["R.2.1", "R.8.4"], fund=["SL.2", "SL.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Escuchar con estrategia y contar su experiencia.", ["Comunicación oral", "Escuchar y presentar"],
                            ["<strong>Escuchar</strong> en dos pasadas: idea general y detalles.", "<strong>Distinguir</strong> hechos y opiniones al escuchar.",
                             "<strong>Reconocer</strong> causas y efectos por sus señales.", "<strong>Preparar y grabar</strong> una presentación de tres minutos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-3", LE.titulo("8-3")), glosario, P)


def practica():
    es = [{"enun": oye(t) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Vuelva a escuchar el audio con esa pregunta en mente.", "exp": e} for t, q, ops, e in ESC]
    ho = [{"enun": oye(t) + "<p><strong>¿Es un hecho o una opinión?</strong></p>", "ops": HO, "ok": k, "enOrden": True, "pista": "¿Se puede comprobar, o es lo que alguien piensa o siente?",
           "exp": f"<strong>{HO[k]}</strong>. {e}"} for t, k, e in HECHO]
    ce = [{"enun": oye(t) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Busque la palabra señal: «porque, debido a, como» marcan la causa; «por eso, así que, como resultado», el efecto.", "exp": e} for t, q, ops, e in CE]
    mods = [("escuchar", "Escuche y responda", C.om("m1", "Escuche el aviso o el mensaje y responda. Si la voz no suena, abra la transcripción.")),
            ("hecho-opinion", "¿Hecho u opinión?", C.om("m2", "Escuche la frase y decida si es un hecho o una opinión.")),
            ("causa-efecto", "Causa y efecto", C.om("m3", "Escuche la frase y encuentre la causa o el efecto."))]
    js = C.js_datos("ES", es) + C.js_datos("HO", ho) + C.js_datos("CE", ce) + 'creaBanco("m1", ES);\ncreaBanco("m2", HO);\ncreaBanco("m3", CE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
