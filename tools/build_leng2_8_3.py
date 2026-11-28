# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 8.3 · Proyecto final y evaluación del nivel.
Fuente: clases_leng2/clase_8-3.html (GEDparaHispanos), adaptada al marco de LearnGED.
La página de práctica es la evaluación final del Nivel 2: 32 preguntas (4 de cada tema), sorteadas en cada intento entre
las preguntas de los cuestionarios de todas las lecciones del nivel (se recogen ejecutando sus builders y se descartan las que
remiten a un texto, un audio, una gráfica o un mapa de su lección). Hay que volver a correr este builder cuando cambie un cuestionario.
Uso: python3 tools/build_leng2_8_3.py
"""
import os, sys, importlib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
import graficas_n2 as G
from build_leng2_7_1 import taller

LE.nivel(2)
N = "8-3"
NIV = 2
MALO = ["En el cuento", "En el texto", "del texto", "el texto", "En la gráfica", "la gráfica", "En el mapa", "Las Flores", "En la tabla", "audio", "<svg", "<figure",
        "class=\"fuente\"", "En «", "Según la", "Según el", "artículo", "lección", "sección", "data-", "párrafo", "fragmento", "diálogo", "Ana", "Tomás", "Marta",
        "Roberto", "Lucía", "la rúbrica", "esta carta", "este aviso", "la noticia", "la entrevista", "el poema", "la foto", "el mapa", "el discurso", "Lincoln", "ochenta y siete", "evaluación final", "Nivel 2"]
CULT, LIB = ["Tomates", "Chiles", "Calabazas", "Cilantro"], [120, 45, 80, 15]
TEXTO_ANA = [
    "Un huerto comunitario es, según la «Guía de huertos urbanos», «un terreno que un grupo de vecinos cultiva en conjunto». Estos huertos dan tres beneficios principales: alimentos frescos, unión entre vecinos y aprendizaje para los niños.",
    "En primer lugar, producen alimentos. En el huerto de la calle Quince se cultivan tomates, chiles, calabazas y cilantro, y cada familia cuida su propia parcela. Como muestra la gráfica, el producto más abundante del verano fue el tomate.",
    "En segundo lugar, unen a los vecinos. Tomás, uno de los voluntarios, explica: «Como ahora pasamos más tiempo afuera, los vecinos nos conocemos mejor».",
    "Por último, los niños aprenden. Según Tomás, en el huerto «aprenden de dónde viene la comida».",
    "En resumen, un huerto comunitario da comida, une a la comunidad y enseña a los más pequeños."]
RUBRICA = [["Dos fuentes con cita", "Dos fuentes bien identificadas, con citas entre comillas", "Dos fuentes; una sin cita", "Una sola fuente", "Sin fuentes"],
           ["Texto coherente y ordenado", "Introducción, desarrollo y conclusión claros; buenos conectores", "Estructura clara con algún salto", "Ideas sueltas, sin orden claro", "Texto incompleto"],
           ["Gráfica o tabla", "Con título, etiquetas y fuente, y mencionada en el texto", "Completa, pero no se menciona en el texto", "Le falta el título o las etiquetas", "Sin gráfica ni tabla"],
           ["Presentación oral", "Inicio, desarrollo y cierre; voz clara; responde preguntas", "Ordenada, pero lee demasiado", "Se entiende, pero desordenada", "Difícil de seguir"],
           ["Compartir y comentar", "Entrega el proyecto y comenta el de dos compañeros", "Entrega y comenta el de uno", "Entrega sin comentar", "No entrega"]]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Llegó a la última lección del Nivel 2. En estas semanas leyó con fluidez, construyó oraciones más ricas, puntuó diálogos, encontró ideas principales, leyó gráficas y fuentes, escribió textos de opinión, informativos y narrativos, y practicó cómo conversar y presentar. Ahora va a unir todo en un proyecto sobre un tema que le interese, y va a comprobar lo aprendido con la evaluación final.</p>
<p>Elija un tema que le importe (la salud, el trabajo, su barrio, la historia de su país, la naturaleza) e investíguelo. El proyecto «Mi tema, mis fuentes» tiene cuatro partes:</p>
{C.tabla("Las cuatro partes del proyecto", ["Parte", "Qué incluye", "Dónde lo aprendió"],
         [["📚 Dos fuentes", "Al menos una primaria o una secundaria de confianza. Anote de dónde salen y cite algo de cada una.", "<a href=\"leccion-6-2.html\">Lección 6.2</a>"],
          ["✍️ Un texto", "Informativo o de opinión, de 8 a 12 oraciones.", "<a href=\"leccion-7-2.html\">Lección 7.2</a> o <a href=\"leccion-7-1.html\">7.1</a>"],
          ["📊 Una gráfica o una tabla", "Con título, etiquetas y la fuente de los datos.", "<a href=\"leccion-6-1.html\">Lección 6.1</a>"],
          ["🎤 Una presentación", "De 3 a 4 minutos, en vivo o grabada. Al final responde una o dos preguntas.", "<a href=\"leccion-8-2.html\">Lección 8.2</a>"]])}
{C.caja("tip", "Elija un tema pequeño", "<p>«La salud» es demasiado amplio para tres minutos; «por qué conviene caminar todos los días» cabe perfectamente. Un buen tema se puede explicar en una oración.</p>")}
{P("Un buen tema", "¿Cuál de estos temas cabe mejor en una presentación de tres minutos?", ["La historia completa de América Latina", "La salud de las personas en el mundo", "Por qué conviene caminar todos los días"], 2,
   {0: "Es demasiado amplio: daría para un libro.", 1: "Es demasiado amplio: daría para un curso entero."}, "Es un tema concreto que se explica en una oración.")}"""

    parrafos = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{t}</p>' for i, t in enumerate(TEXTO_ANA, 1))
    s2 = f"""<p>Así quedó el proyecto de Ana. Ana es un personaje creado para esta lección, y su proyecto usa la entrevista de la <a href="leccion-8-2.html">Lección 8.2</a>. Fíjese en cómo se conectan las cuatro partes.</p>
<h3>📚 Parte 1 · Las dos fuentes</h3>
<ul><li><strong>Fuente A (primaria):</strong> la entrevista a Tomás, voluntario del huerto de la calle Quince. Él vivió lo que cuenta.</li>
<li><strong>Fuente B (secundaria):</strong> «Guía de huertos urbanos», un artículo de la biblioteca del barrio. Dice: «Un huerto comunitario es un terreno que un grupo de vecinos cultiva en conjunto. Además de alimentos, ofrece un lugar de encuentro y de aprendizaje para los niños».</li></ul>
<p class="fuente">La entrevista y la guía son inventadas para la lección.</p>
<h3>✍️ Parte 2 · El texto informativo</h3>
<p>{LE.escuchar(" ".join(TEXTO_ANA), "Escuchar el texto")}</p>
<div class="articulo"><p><strong>Un huerto que une al barrio</strong></p>{parrafos}</div>
<h3>📊 Parte 3 · La gráfica</h3>
{G.barras("Cosecha del huerto de la calle Quince en un verano", "Cultivo", "Libras cosechadas", CULT, LIB, py=30)}
<p class="fuente">Fuente: registro de los voluntarios del huerto. Datos de ejemplo para la lección.</p>
<h3>🎤 Parte 4 · El guion de la presentación</h3>
{C.tabla("Guion de Ana", ["Parte", "Qué dice"],
         [["Inicio", "«Buenas tardes. Hoy les voy a hablar de los huertos comunitarios y de por qué creo que ayudan a un barrio entero.»"],
          ["Desarrollo", "«Consulté dos fuentes: una entrevista a un voluntario y una guía de la biblioteca. Encontré tres beneficios… (explica cada uno y muestra la gráfica). Fíjense en la barra de los tomates: es la más alta, con 120 libras.»"],
          ["Cierre", "«En resumen, un huerto da comida, une y enseña. ¿Tienen alguna pregunta?»"]])}
<h3>Analice el proyecto de Ana</h3>
{P("Proyecto 1", "¿Qué tipo de fuente es la entrevista a Tomás?", ["Secundaria: la escribió un periodista", "Primaria: él participa en el huerto", "Ninguna: es solo una opinión suya"], 1,
   {0: "Tomás habla de lo que él mismo vive.", 2: "Una entrevista a un testigo es una fuente."}, "Tomás vivió lo que cuenta: es una fuente <strong>primaria</strong>.")}
{P("Proyecto 2", "¿Qué tipo de texto escribió Ana?", ["Narrativo: cuenta una historia", "De opinión: defiende una postura", "Informativo: explica con datos"], 2,
   {0: "No hay personajes ni trama.", 1: "Explica beneficios; no discute una postura."}, "Organiza la información en tres categorías: alimentos, unión y aprendizaje.")}
{P("Proyecto 3", "¿Cómo cita Ana sus fuentes?", ["Usa comillas y nombra la fuente", "Copia el artículo de la guía", "Escribe solo lo que ella piensa"], 0,
   {1: "Solo toma frases cortas.", 2: "Sí cita: busque las comillas."}, "«según la Guía…», «Tomás… explica: “…”».")}
{P("Proyecto 4", "¿Qué dato de la gráfica menciona Ana en su presentación?", ["La barra de los tomates, la más alta", "La barra del cilantro, la más baja", "El título y la fuente de los datos"], 0,
   {1: "Vuelva al guion: ¿qué barra señala?", 2: "Vuelva al guion: ¿qué barra señala?"}, "Señala un dato concreto: 120 libras de tomates.")}"""

    s3 = f"""<p>El GED y la evaluación de este nivel tienen preguntas de opción múltiple con textos y gráficas. Estas cinco estrategias le ayudan:</p>
<ol><li><strong>Lea la pregunta antes que el texto.</strong> Así sabe qué buscar.</li>
<li><strong>Vuelva al texto.</strong> La respuesta está en el texto o en la gráfica, no en lo que usted piensa del tema.</li>
<li><strong>Elimine opciones.</strong> Descarte las que son falsas, las que hablan de otra cosa y las que exageran («siempre», «nunca», «todos»).</li>
<li><strong>Cuide el tiempo.</strong> Si una pregunta lo traba, márquela, siga y vuelva al final.</li>
<li><strong>No deje ninguna en blanco.</strong> Una respuesta razonada vale más que un espacio vacío.</li></ol>
<h3>Cinco preguntas modelo sobre el proyecto de Ana</h3>
<p>Responda con el texto y la gráfica de la <a href="#s2">sección 2</a>. La explicación le dice qué estrategia ayudaba.</p>
{P("Modelo 1", "Según la gráfica, ¿cuántas libras de calabaza se cosecharon?", ["45", "80", "120"], 1, {0: "Esas son las de chiles.", 2: "Esas son las de tomates."},
   "Lea el número sobre la barra de las calabazas. <strong>Estrategia 1:</strong> lea la pregunta primero y busque solo ese dato.")}
{P("Modelo 2", "¿Cuál es la idea principal del texto de Ana?", ["Los tomates son el mejor cultivo de todos los huertos", "Un huerto comunitario da comida, une y enseña", "Tomás es un voluntario del huerto de la calle Quince"], 1,
   {0: "Exagera («el mejor… de todos») y el texto no lo dice.", 2: "Es solo un detalle."}, "Está en el párrafo 1 y se repite en la conclusión. <strong>Estrategia 3:</strong> elimine la opción que exagera y la que es solo un detalle.")}
{P("Modelo 3", "¿Qué afirmación apoyan los datos de la gráfica?", ["El cilantro es el cultivo más difícil", "Se cosecharon más chiles que cilantro", "Los vecinos prefieren las calabazas"], 1,
   {0: "La gráfica no habla de dificultad.", 2: "La gráfica no habla de gustos."}, "45 es más que 15. <strong>Estrategia 2:</strong> vuelva a la gráfica; las otras opciones inventan causas o gustos.")}
{P("Modelo 4", "¿Qué evidencia apoya que el huerto une a los vecinos?", ["«…se cultivan tomates, chiles, calabazas y cilantro.»", "«…los vecinos nos conocemos mejor.»", "«…el producto más abundante del verano fue el tomate.»"], 1,
   {0: "Habla de alimentos, no de unión.", 2: "Habla de alimentos, no de unión."}, "Es la cita de Tomás en el párrafo 3. <strong>Estrategia 2:</strong> busque la cita que demuestra directamente la afirmación.")}
{P("Modelo 5", "¿Cuál es el propósito del texto de Ana?", ["Entretener con una historia", "Vender productos del huerto", "Informar sobre los huertos"], 2,
   {0: "No cuenta una historia.", 1: "No ofrece nada en venta."}, "Explica qué son los huertos y sus beneficios. Si duda, piense qué hace el texto en general, no un párrafo suelto.")}"""

    s4 = f"""{C.tabla("Su proyecto, paso a paso", ["Paso", "Qué hacer"],
         [["1 · Mi tema en una oración", "Voy a investigar ______."],
          ["2 · Mis dos fuentes", "Fuente A: ______ (¿quién?, ¿cuándo?, ¿primaria o secundaria?). Fuente B: ______. Busque en la biblioteca, en sitios del gobierno (.gov) o de universidades (.edu), o en el <a href=\"/es/estudios-sociales/fuentes/\">Archivo de fuentes</a>."],
          ["3 · Mi texto", "¿Informativo o de opinión? Use la plantilla de la Lección 7.2 o 7.1 e incluya al menos una cita de cada fuente."],
          ["4 · Mi gráfica o tabla", "Hágala a mano o en una hoja de cálculo, con título, etiquetas y la fuente de los datos."],
          ["5 · Mi presentación", "Prepare el guion (inicio, desarrollo, cierre), ensaye y preséntela en clase o grábela con la <a href=\"leccion-8-2.html#s3\">grabadora de la Lección 8.2</a>."]])}
<p>Escriba aquí el texto de su proyecto:</p>
{taller("2-8-3", "El texto de mi proyecto (de 8 a 12 oraciones)", "Mi tema… Según [fuente A], «…». En primer lugar… Como muestra mi gráfica… En resumen…", 8, 110,
        ["según", "en primer lugar", "en segundo lugar", "por último", "además", "por ejemplo", "es decir", "como muestra", "porque", "por eso", "sin embargo", "en resumen", "en conclusión", "creo que"],
        ["Mi tema cabe en una oración.", "Uso dos fuentes y digo de dónde salen.", "Incluyo al menos una cita entre comillas de cada fuente.", "Mi texto tiene introducción, desarrollo y conclusión.",
         "Menciono mi gráfica o mi tabla en el texto.", "Escuché mi texto en voz alta y revisé la ortografía y la puntuación."])}
{C.caja("tip", "Comparto mi investigación", "<p>Presente su proyecto a su familia o a un compañero antes de la clase. Pídale que le haga una pregunta al final: así practica responder.</p>")}
<h3>Autoevaluación con la rúbrica</h3>
<p>Antes de entregar, califique su proyecto con la misma rúbrica que usará su maestro. Sea honesto: sirve para mejorar antes de entregar.</p>
{C.tabla("Rúbrica del proyecto final", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"], RUBRICA)}
<p>Total: 20 puntos. Con <strong>16 o más</strong>, su proyecto está sólido. Si algún criterio quedó en 2 o menos, mejórelo antes de entregar: todavía está a tiempo.</p>"""

    temas = "".join(f"<li><strong>Tema {k}</strong> · {v}</li>" for k, v in LE.NIVELES[NIV][1].items())
    s5 = f"""<p>Antes de la evaluación, mire el camino recorrido:</p>
<ol class="sin-num">{temas}</ol>
<p>La <a href="practica-8-3.html"><strong>evaluación final del Nivel 2</strong></a> está en la página de práctica de esta lección:</p>
<ul><li>Tiene <strong>32 preguntas</strong>, cuatro de cada tema, sin límite de tiempo (calcule unos 60 minutos). Las preguntas cambian en cada intento.</li>
<li>Al corregir verá su puntaje <strong>por tema</strong>: sabrá qué domina y qué necesita repasar.</li>
<li>Cada pregunta que falle trae un enlace a la lección que la explica.</li>
<li>Puede imprimir el resumen, con su nombre y la fecha (o guardarlo en PDF), y usarlo como guía de estudio. Si su programa pide una evaluación oficial, estará en Brightspace.</li></ul>
{C.caja("tip", "La meta es el 80 %", "<p>Si acierta <strong>26 preguntas o más</strong>, domina el Nivel 2. Si no, no pasa nada: el resumen le dice exactamente qué repasar.</p>")}
<h3>🎓 Lo que aprendió en el Nivel 2</h3>
<ul><li>Leer con <strong>fluidez</strong> y descifrar palabras nuevas por sus partes y por el contexto.</li>
<li>Construir oraciones <strong>simples, compuestas y complejas</strong>, con buena concordancia, puntuación y ortografía.</li>
<li>Encontrar la <strong>idea principal</strong>, la estructura y el propósito de un texto, y <strong>comparar</strong> dos textos.</li>
<li>Leer <strong>gráficas, tablas y fuentes</strong>, y citar evidencia.</li>
<li><strong>Escribir</strong> textos de opinión, informativos y narrativos, y revisarlos.</li>
<li><strong>Conversar</strong>, escuchar y presentar con claridad.</li></ul>
{C.caja("ojo", "Antes de irse, revísese", "<ul><li>¿Entregó su proyecto con sus cuatro partes?</li><li>¿Imprimió o guardó el resumen de su evaluación final?</li><li>¿Qué tres lecciones va a repasar antes de empezar el Nivel 3?</li></ul>")}"""

    secciones = [("s1", "El proyecto «Mi tema, mis fuentes»", s1), ("s2", "Proyecto modelo: los huertos comunitarios", s2), ("s3", "Estrategias de examen", s3),
                 ("s4", "Su proyecto, paso a paso", s4), ("s5", "La evaluación final y el cierre del nivel", s5)]
    tarea = [("Mi proyecto.", "Termine las cuatro partes de su proyecto, califíquelo con la rúbrica y entréguelo a su maestro."),
             ("Mi evaluación.", "Haga la evaluación final del Nivel 2 e imprima o guarde su resumen."),
             ("Mi plan de repaso.", "Para cada tema por debajo del 75 %, escriba qué lección va a repasar y cuándo. Después, repita la evaluación.")]
    quiz = [
        ("¿Cuántas fuentes debe usar el proyecto final, como mínimo?", ["Dos", "Una", "Cinco"], 0, {1: "Se piden más.", 2: "No hacen falta tantas."}, "<strong>Dos</strong> fuentes, con una cita de cada una."),
        ("¿Qué debe llevar siempre una gráfica del proyecto?", ["Título, etiquetas y fuente", "Muchos colores y dibujos", "Solo los números, sin título"], 0, {1: "Adornan, pero no informan.", 2: "Sin título no se entiende."}, "<strong>Título, etiquetas y fuente.</strong>"),
        ("¿Cuánto debe durar la presentación del proyecto?", ["De 3 a 4 minutos", "Unos 30 segundos", "Más de 20 minutos"], 0, {1: "Es muy poco.", 2: "Es demasiado."}, "<strong>De 3 a 4 minutos.</strong>"),
        ("Una entrevista a alguien que vivió los hechos es una fuente…", ["primaria", "secundaria", "inventada"], 0, {1: "Esa resume o explica lo que otros vivieron.", 2: "No."}, "<strong>Primaria.</strong>"),
        ("¿Qué estrategia conviene usar primero en una pregunta de examen con un texto largo?", ["Leer la pregunta antes que el texto", "Leer el texto tres veces seguidas", "Elegir la opción más larga"], 0, {1: "Gasta tiempo.", 2: "La longitud no dice nada."}, "<strong>Leer la pregunta primero.</strong>"),
        ("Una opción que dice «siempre», «nunca» o «todos» suele ser…", ["una exageración que conviene revisar", "la respuesta correcta", "una cita textual"], 0, {1: "No necesariamente.", 2: "No."}, "Suele <strong>exagerar</strong>."),
        ("Si una pregunta del examen lo traba, conviene…", ["marcarla, seguir y volver al final", "quedarse en ella hasta resolverla", "dejarla en blanco para siempre"], 0, {1: "Pierde tiempo para las demás.", 2: "Una respuesta razonada vale más."}, "<strong>Marcarla y volver.</strong>"),
        ("¿Dónde está la respuesta a una pregunta sobre un texto?", ["En el texto o en la gráfica", "En lo que yo pienso del tema", "En lo que dice un amigo"], 0, {1: "La opinión propia puede engañar.", 2: "No."}, "En el <strong>texto o la gráfica</strong>."),
        ("¿Cuántas preguntas tiene la evaluación final del Nivel 2?", ["32, cuatro de cada tema", "10, todas del Tema 8", "100, sin orden"], 0, {1: "No.", 2: "No."}, "<strong>32.</strong>"),
        ("¿Qué porcentaje indica que domina el Nivel 2?", ["80 % (26 preguntas o más)", "50 % (16 preguntas o más)", "100 % (las 32 preguntas)"], 0, {1: "Es poco.", 2: "No hace falta la perfección."}, "<strong>80 %.</strong>"),
    ]
    filas = [
        ("Mi proyecto", "Tiene dos fuentes, texto, gráfica y presentación.", "Me falta una parte.", "Todavía no lo empiezo (<a href=\"#s4\">vea la sección 4</a>)."),
        ("Estrategias", "Uso las cinco estrategias al responder.", "Uso algunas.", "No las recuerdo (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Evaluación", "Llegué al 80 % o hice mi plan de repaso.", "Hice la evaluación, pero sin plan.", "No la he hecho (<a href=\"#s5\">vea la sección 5</a>)."),
    ]
    cierre = "<p>¡Terminó el Nivel 2 de Artes del Lenguaje! En el Nivel 3 dará el salto a la lectura inferencial, al lenguaje figurado avanzado y a la escritura argumentada que pide el GED.</p>"
    glosario = [("Proyecto", "Trabajo que reúne varias destrezas alrededor de un tema."), ("Estrategia de examen", "Una forma ordenada de responder mejor y más rápido."),
                ("Autoevaluación", "Calificar el propio trabajo con criterios claros.")]
    conexion = ("<p>Este proyecto reúne todo el nivel: las fuentes de la Lección 6.2, las gráficas de la 6.1, la escritura del Tema 7 y la presentación de la 8.2.</p>"
                "<p><strong>Lo que necesita:</strong> un tema que le interese, acceso a la biblioteca o a internet para sus fuentes, y unos 60 minutos tranquilos para la evaluación.</p>")
    estd = LE.estandares(["W.2"], base=["R.8.1", "R.4.1"], fund=["SL.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Unir todo lo aprendido y medir el camino recorrido.", ["Proyecto final", "Evaluación del nivel"],
                            ["<strong>Investigar</strong> un tema con dos fuentes y escribir sobre él.", "<strong>Representar</strong> datos en una gráfica o tabla y presentarlos.",
                             "<strong>Aplicar</strong> cinco estrategias de examen.", "<strong>Medir</strong> lo aprendido en los ocho temas con la evaluación final."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, (None, "Siguiente: Nivel 3 de Artes del Lenguaje (en preparación)."), glosario, P)


def banco():
    """Recoge las preguntas de los cuestionarios de todas las lecciones del Nivel 2."""
    cap, orig = [], LE._quiz_original

    def captura(items):
        cap.extend(items)
        return orig(items)
    salida = []
    for t in range(1, 9):
        for n in range(1, 7):
            try:
                m = sys.modules[__name__] if (t, n) == (8, 3) else importlib.import_module(f"build_leng2_{t}_{n}")
            except ModuleNotFoundError:
                continue
            LE.nivel(NIV)
            cap.clear()
            antes = C.quiz_html
            C.quiz_html = captura
            try:
                m.leccion()
            finally:
                C.quiz_html = antes
            for preg, ops, ok, pistas, sol in cap:
                if any(x in preg for x in MALO):
                    continue
                salida.append({"t": t, "l": f"{t}-{n}", "q": preg, "o": list(ops), "c": ok, "s": sol})
    LE.nivel(NIV)
    return salida


def practica():
    B = banco()
    temas = {str(k): v for k, v in LE.NIVELES[NIV][1].items()}
    titulos = {f"{t}-{n}": LE.titulo(f"{t}-{n}") for t in range(1, 9) for n in range(1, 7) if f"{t}-{n}" in LE.LECCIONES[NIV]}
    cont = """<div id="evf" class="evaluacion">
<p>Responda las 32 preguntas y pulse <strong>Corregir</strong> al final. Las preguntas cambian en cada intento.</p>
<p><label for="evf-nombre"><strong>Su nombre</strong> (aparecerá en el resumen):</label> <input type="text" id="evf-nombre" autocomplete="name" class="evf-nombre"></p>
<ol id="evf-lista" class="evf-lista"></ol>
<p><button type="button" class="btn" id="evf-corregir">✅ Corregir</button> <button type="button" class="btn-sec" id="evf-otra">🔄 Otra evaluación</button> <button type="button" class="btn-sec" id="evf-imp" hidden>🖨️ Imprimir o guardar en PDF</button></p>
<div id="evf-res" aria-live="polite"></div></div>"""
    js = (f"var EVB = {json.dumps(B, ensure_ascii=False)};\nvar EVT = {json.dumps(temas, ensure_ascii=False)};\nvar EVL = {json.dumps(titulos, ensure_ascii=False)};\n" + r"""
(function () {
  var lista = document.getElementById("evf-lista"), res = document.getElementById("evf-res"), sel = [], cor = false;
  function baraja(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
  function limpio(s) { return s.replace(/[<>&"]/g, ""); }
  function nueva() {
    sel = []; cor = false;
    for (var t = 1; t <= 8; t++) { var p = baraja(EVB.filter(function (q) { return q.t === t; })).slice(0, 4); sel = sel.concat(p); }
    lista.innerHTML = "";
    sel.forEach(function (q, i) {
      var orden = baraja(q.o.map(function (o, k) { return k; }));
      q._elegida = null;
      var li = document.createElement("li"); li.className = "evf-p";
      li.innerHTML = '<p class="evf-tema">Tema ' + q.t + '</p><p class="evf-q" id="evf-q' + i + '">' + q.q + '</p><div class="opciones" role="radiogroup" aria-labelledby="evf-q' + i + '">' +
        orden.map(function (k) { return '<button type="button" class="opcion" role="radio" aria-checked="false" data-k="' + k + '">' + q.o[k] + '</button>'; }).join("") + '</div><div class="evf-fb"></div>';
      li.querySelectorAll(".opcion").forEach(function (b) {
        b.addEventListener("click", function () { if (cor) return; li.querySelectorAll(".opcion").forEach(function (x) { x.classList.remove("elegida"); x.setAttribute("aria-checked", "false"); });
          b.classList.add("elegida"); b.setAttribute("aria-checked", "true"); q._elegida = +b.getAttribute("data-k"); li.classList.remove("evf-falta"); });
      });
      lista.appendChild(li);
    });
    res.innerHTML = ""; document.getElementById("evf-imp").hidden = true; document.getElementById("evf-corregir").disabled = false;
  }
  function corregir() {
    var faltan = sel.filter(function (q) { return q._elegida === null; }).length;
    if (faltan && !cor) {
      lista.querySelectorAll(".evf-p").forEach(function (li, i) { li.classList.toggle("evf-falta", sel[i]._elegida === null); });
      res.innerHTML = '<p class="fb pista">Faltan ' + faltan + ' pregunta' + (faltan > 1 ? 's' : '') + ' por responder (marcadas en amarillo).</p>'; return;
    }
    cor = true; document.getElementById("evf-corregir").disabled = true;
    var porTema = {}, total = 0, malas = [];
    sel.forEach(function (q, i) {
      var li = lista.children[i], bien = q._elegida === q.c;
      porTema[q.t] = porTema[q.t] || [0, 0]; porTema[q.t][1]++; if (bien) { porTema[q.t][0]++; total++; } else malas.push(q);
      li.classList.add(bien ? "evf-bien" : "evf-mal");
      li.querySelectorAll(".opcion").forEach(function (b) { var k = +b.getAttribute("data-k"); if (k === q.c) b.classList.add("correcta"); else if (k === q._elegida) b.classList.add("incorrecta"); b.disabled = true; });
      li.querySelector(".evf-fb").innerHTML = (bien ? "✅ " : "❌ ") + q.s + (bien ? "" : ' <a href="leccion-' + q.l + '.html">Repase la Lección ' + q.l.replace("-", ".") + '</a>');
    });
    var pct = Math.round(total / sel.length * 100), filas = "";
    for (var t = 1; t <= 8; t++) { var p = porTema[t] || [0, 0], v = p[1] ? Math.round(p[0] / p[1] * 100) : 0;
      filas += '<tr><th scope="row">Tema ' + t + ' · ' + EVT[t] + '</th><td>' + p[0] + ' de ' + p[1] + '</td><td>' + (v >= 75 ? "✅ Lo domina" : "📚 Repasar") + '</td></tr>'; }
    var rep = {}; malas.forEach(function (q) { rep[q.l] = 1; });
    var links = Object.keys(rep).sort(function (a, b) { var x = a.split("-"), y = b.split("-"); return x[0] - y[0] || x[1] - y[1]; })
      .map(function (l) { return '<li><a href="leccion-' + l + '.html">Lección ' + l.replace("-", ".") + ' · ' + (EVL[l] || "") + '</a></li>'; }).join("");
    var nom = limpio(document.getElementById("evf-nombre").value.trim()) || "(sin nombre)";
    var hoy = new Date().toLocaleDateString("es-US", { year: "numeric", month: "long", day: "numeric" });
    res.innerHTML = '<div class="evf-resumen"><h3>📋 Resumen de mi evaluación final · Nivel 2</h3><p><strong>Estudiante:</strong> ' + nom + ' · <strong>Fecha:</strong> ' + hoy + '</p><p class="evf-total">' + total + ' de ' + sel.length + ' (' + pct + ' %)</p><p>' +
      (pct >= 80 ? "🎉 <strong>¡Domina el Nivel 2!</strong> Está listo para el Nivel 3." : "Va por buen camino. Repase los temas marcados y repita la evaluación: la meta es el 80 % (26 preguntas).") +
      '</p><table class="tabla-ej"><caption>Resultado por tema</caption><thead><tr><th scope="col">Tema</th><th scope="col">Aciertos</th><th scope="col">Estado</th></tr></thead><tbody>' + filas + '</tbody></table>' +
      (links ? '<p><strong>Lecciones para repasar:</strong></p><ul>' + links + '</ul>' : '') + '</div>';
    document.getElementById("evf-imp").hidden = false; res.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  document.getElementById("evf-corregir").addEventListener("click", corregir);
  document.getElementById("evf-otra").addEventListener("click", function () { nueva(); window.scrollTo({ top: lista.getBoundingClientRect().top + window.scrollY - 90 }); });
  document.getElementById("evf-imp").addEventListener("click", function () { window.print(); });
  nueva();
})();
""")
    mods = [("evaluacion", "Evaluación final del Nivel 2", cont)]
    return C.pagina_practica(N, "Evaluación final del Nivel 2", f"32 preguntas · 4 de cada tema · sorteadas entre {len(B)} · meta: 80 %", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 4 horas")
