# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 5.3 · Fuentes primarias y secundarias: citar y relacionar.
Fuente: clases_leng3/clase_5-3.html (GEDparaHispanos) y gramatica/n3-l5-3.html, adaptadas al marco de LearnGED.
Cartas: Emmett J. Scott, «Letters of Negro Migrants of 1916-1918», The Journal of Negro History 4 (1919), dominio público; traducción
del Archivo de fuentes de LearnGED (/es/estudios-sociales/fuentes/cartas-migrantes-1917.html).
Uso: python3 tools/build_leng3_5_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_3_1 import texto

LE.nivel(3)
N = "5-3"
PS = ["Primaria", "Secundaria"]
REL = ["La primaria confirma lo que dice la secundaria", "La secundaria explica el contexto de la primaria", "La primaria añade detalles que la secundaria no da"]
ARCHIVO = "/es/estudios-sociales/fuentes/cartas-migrantes-1917.html"
SECUNDARIA = ["Entre 1916 y 1970, cerca de seis millones de afroamericanos dejaron el sur rural de los Estados Unidos y se establecieron en las ciudades del norte y del oeste. A ese desplazamiento se le llama la Gran Migración.",
              "Las causas fueron varias. Durante la Primera Guerra Mundial, las fábricas del norte necesitaban trabajadores, y la llegada de inmigrantes europeos se había reducido. Al mismo tiempo, en el sur, las leyes de segregación y la violencia contra la población negra hacían la vida cada vez más difícil.",
              "Chicago fue uno de los destinos principales. Entre 1910 y 1920, su población afroamericana pasó de unos 44 000 a unos 109 000 habitantes. El periódico afroamericano <em>Chicago Defender</em>, que circulaba por el sur, publicaba ofertas de trabajo y animaba a sus lectores a mudarse. Miles de personas le escribieron para pedir información.",
              "La llegada no fue fácil: muchos encontraron trabajo, pero también discriminación en la vivienda y en el empleo. Aun así, la migración transformó la cultura, la política y la música de las ciudades del norte."]
CARTA1 = "«Estimado señor: He visto por el <em>Chicago Defender</em> que usted y la gente de Chicago están ayudando a los recién llegados. Le pido información sobre las condiciones en algún pueblo pequeño cerca de Chicago. Aquí hay algunas familias que están pensando en mudarse, y desean saber qué esperar antes de salir. Sírvase informar sobre el trato, el trabajo, el alquiler y las escuelas.»"
CARTA2 = "«Soy lector constante del <em>Defender</em> y estoy pensando en irme de aquí hacia algún punto del norte. […] Estoy empleado ahora como obrero en un taller de estructuras; llevo cinco años con la firma. […] Tengo 31 años, tengo una esposa muy trabajadora y no tengo hijos. Si hay posibilidades de trabajo de cualquier clase, hágamelo saber.»"
SEC_B = "<strong>Fuente secundaria.</strong> Entre 1916 y 1970, cerca de seis millones de afroamericanos dejaron el sur rural. Durante la Primera Guerra Mundial, las fábricas del norte necesitaban trabajadores. Chicago fue uno de los destinos principales: entre 1910 y 1920, su población afroamericana pasó de unos 44 000 a unos 109 000 habitantes. El <em>Chicago Defender</em> publicaba ofertas de trabajo y animaba a sus lectores a mudarse."
C1 = "<strong>Carta de Sanford, Florida (1917).</strong> «Aquí hay algunas familias que están pensando en mudarse, y desean saber qué esperar antes de salir. Sírvase informar sobre el trato, el trabajo, el alquiler y las escuelas.»"
C2 = "<strong>Carta de Dallas, Texas (1917).</strong> «Soy lector constante del <em>Defender</em> y estoy pensando en irme de aquí hacia algún punto del norte. […] Tengo 31 años, tengo una esposa muy trabajadora y no tengo hijos.»"
C3 = "<strong>Carta de Mobile, Alabama (1917).</strong> «Durante siete años tuve fama de lavandera de primera clase en Selma. […] Ahora hago trabajo doméstico, pero quisiera ponerme en contacto con Chicago.»"
CL = [("Para estudiar la Gran Migración: una carta escrita en 1917 por un obrero de Dallas que quería mudarse a Chicago.", 0, "La escribió alguien que vivía ese momento."),
      ("Para estudiar la Gran Migración: un libro de historia publicado en 2010.", 1, "Lo escribió un historiador muchos años después."),
      ("Para estudiar el Gran Incendio de Chicago: el testimonio de una mujer que escapó de las llamas en 1871.", 0, "Es la voz de una testigo."),
      ("Para estudiar el Gran Incendio de Chicago: un artículo de una enciclopedia en línea.", 1, "Resume lo que otros investigaron."),
      ("Para estudiar la Declaración de Independencia: el documento firmado en 1776.", 0, "Es el documento mismo, de su época."),
      ("Para estudiar la Gran Depresión: una fotografía de 1936 de una familia que vivía en una tienda de campaña.", 0, "La fotografía se tomó en ese momento."),
      ("Para estudiar la Gran Depresión: un documental de televisión de 2018 que explica sus causas.", 1, "Se hizo mucho después para explicar el hecho."),
      ("Para estudiar la llegada del ser humano a la Luna: la grabación de la transmisión en vivo de 1969.", 0, "Se grabó mientras ocurría."),
      ("Para estudiar el movimiento por los derechos civiles: el discurso de Martin Luther King Jr. en Washington en 1963.", 0, "Es el discurso de alguien que protagonizó el hecho."),
      ("Para estudiar el movimiento por los derechos civiles: el capítulo de un libro de texto de secundaria.", 1, "Explica el hecho después, a partir de otras fuentes."),
      ("Para estudiar la Casa Hull de Chicago: el libro en el que Jane Addams contó cómo la fundó en 1889.", 0, "Lo escribió la propia fundadora sobre lo que vivió."),
      ("Para estudiar la vida en Chicago en 1917: un artículo del <em>Chicago Defender</em> publicado ese año.", 0, "Un periódico de la época es fuente primaria para estudiar esa época."),
      ("Para estudiar la vida en Chicago en 1917: un artículo publicado hoy que analiza la prensa de 1917.", 1, "Se escribió mucho después y analiza otras fuentes."),
      ("Para estudiar su familia: el acta de nacimiento de su abuelo.", 0, "Es un documento de su época.")]
EV = [([SEC_B, C1], "¿Qué cita muestra cuánto creció la población afroamericana de Chicago?", ["«pasó de unos 44 000 a unos 109 000 habitantes»", "«desean saber qué esperar antes de salir»", "«cerca de seis millones de afroamericanos»"], "La fuente secundaria da la cifra de Chicago. Los seis millones son de todo el país."),
      ([SEC_B, C1], "¿Qué cita muestra que las familias querían informarse antes de decidir?", ["«desean saber qué esperar antes de salir»", "«Chicago fue uno de los destinos principales»", "«las fábricas del norte necesitaban trabajadores»"], "Es la voz de las propias familias, en la carta de Sanford."),
      ([SEC_B, C2], "¿Qué cita muestra la influencia del <em>Chicago Defender</em> en los lectores del sur?", ["«Soy lector constante del Defender y estoy pensando en irme»", "«Tengo 31 años, tengo una esposa muy trabajadora»", "«su población afroamericana pasó de unos 44 000»"], "El obrero relaciona su lectura del <em>Defender</em> con su idea de migrar."),
      ([SEC_B, C2], "¿Qué fuente explica por qué había trabajo en el norte?", ["La secundaria: «las fábricas del norte necesitaban trabajadores»", "La carta: «estoy pensando en irme de aquí hacia algún punto del norte»", "La carta: «tengo una esposa muy trabajadora y no tengo hijos»"], "La carta no explica la causa; la secundaria sí."),
      ([SEC_B, C3], "¿Qué cita muestra que la autora de Mobile tenía experiencia en un oficio?", ["«tuve fama de lavandera de primera clase en Selma»", "«Ahora hago trabajo doméstico, pero quisiera ponerme en contacto»", "«las fábricas del norte necesitaban trabajadores»"], "Siete años con fama de lavandera de primera muestran su experiencia."),
      ([SEC_B, C3], "¿Qué cita sugiere que la autora de Mobile trabajaba en algo que no era su oficio?", ["«Ahora hago trabajo doméstico»", "«tuve fama de lavandera de primera clase»", "«las fábricas del norte necesitaban trabajadores»"], "Había sido lavandera de primera y ahora hacía trabajo doméstico: buscaba algo mejor.")]
RE = [("Una fotografía de 1936 muestra a una familia que vive en una tienda de campaña junto a un camino.", "Un libro de historia explica que en la Gran Depresión millones de familias perdieron su casa.", 0, "La foto es un caso real de lo que dice el libro."),
      ("El diario de una enfermera de 1918 cuenta que en su hospital no quedaban camas libres.", "Un artículo explica que en 1918 una pandemia de gripe llenó los hospitales del mundo.", 1, "El artículo explica por qué el hospital estaba lleno."),
      ("Una carta de 1917 pregunta por «el trato, el trabajo, el alquiler y las escuelas» en Chicago.", "Una enciclopedia dice que millones de afroamericanos se mudaron al norte entre 1916 y 1970.", 2, "La carta muestra qué preocupaba a la gente, algo que el dato general no dice."),
      ("El testimonio de un sobreviviente de 1871 describe el ruido del viento y el calor de las llamas.", "Un libro dice que el Gran Incendio de Chicago destruyó más de 17 000 edificios.", 2, "El testimonio da lo que se vivió; el libro da la cifra."),
      ("Un volante de 1966 invita a una marcha por la vivienda justa en Chicago.", "Un artículo explica que en esos años muchas familias negras no podían comprar casa en ciertos barrios.", 1, "El artículo explica por qué se organizó la marcha."),
      ("El libro de Jane Addams cuenta que en la Casa Hull daban clases a inmigrantes de muchos países.", "Una enciclopedia dice que la Casa Hull ofrecía servicios a los inmigrantes del oeste de Chicago.", 0, "El relato de la fundadora confirma lo que dice la enciclopedia.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Hace más de cien años, un obrero de Dallas escribió a un periódico de Chicago para preguntar si había trabajo en el norte. Su carta, de unas pocas líneas, es una <strong>fuente primaria</strong>: la voz de alguien que vivió la historia. Un libro que hoy explica por qué millones de personas como él se mudaron es una <strong>fuente secundaria</strong>. Las dos son valiosas, y juntas cuentan mucho más que cada una por separado. En el GED de Estudios Sociales es frecuente que aparezca una fuente de cada clase sobre el mismo hecho.</p>
{C.tabla("Diferencias entre fuente primaria y secundaria con ejemplos", ["", "Fuente primaria", "Fuente secundaria"],
         [["Qué es", "Creada por alguien que vivió el hecho, en su época.", "Creada después por alguien que estudió el hecho."],
          ["Ejemplos", "Cartas, diarios, fotografías, leyes, discursos, entrevistas, un artículo de periódico de esos días.", "Libros de historia, enciclopedias, documentales, artículos que analizan lo que pasó."]])}
{C.caja("tip", "Depende de la pregunta", "<p>Un artículo de periódico de 1917 es fuente primaria para estudiar 1917. Un artículo de hoy sobre 1917 es secundaria. Lo que importa es si quien la hizo estuvo allí.</p>")}
{P("Clase 1", "¿Cuál es una fuente <strong>secundaria</strong>?", ["Una foto tomada en una calle de Chicago en 1918", "Un documental de 2015 sobre la Gran Migración", "Una carta escrita por una lavandera de Alabama en 1917"], 1, {0: "Se tomó en ese momento.", 2: "La escribió alguien que lo vivía."}, "Se hizo mucho después para explicar el hecho.")}"""

    s2 = f"""{C.tabla("Fuerza y límite de cada clase de fuente", ["", "Fuente primaria", "Fuente secundaria"],
         [["Su fuerza", "La voz directa, los detalles, lo que sentía la gente en ese momento.", "El panorama completo, las cifras, las causas y las consecuencias."],
          ["Su límite", "Muestra solo lo que vio una persona, desde su punto de vista.", "Es una interpretación; depende de las fuentes que usó el autor."]])}
{C.caja("tip", "El punto de vista", "<p>Pregúntese siempre <strong>quién</strong> escribió la fuente, <strong>cuándo</strong> y <strong>para qué</strong>. Una carta para pedir trabajo no cuenta lo mismo que un discurso político, aunque hablen de la misma época.</p>")}
{P("Fuerza", "¿Cuál es la principal fuerza de una fuente primaria?", ["Las cifras exactas y el panorama completo", "La voz directa y los detalles de la época", "Que nunca tiene ningún punto de vista"], 1, {0: "Eso lo da la secundaria.", 2: "Al contrario: tiene el de quien la escribió."}, "La <strong>voz directa</strong> y los detalles.")}"""

    sec = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(SECUNDARIA, 1))
    s3 = f"""<p>Lea primero la fuente secundaria, que da el panorama, y después las dos cartas. En su cuaderno, anote para cada fuente: quién la escribió, cuándo y para qué.</p>
<div class="articulo"><p><strong>Fuente 1 · Secundaria: «La Gran Migración y Chicago»</strong></p><p>{LE.escuchar(re.sub('<[^>]+>', '', ' '.join(SECUNDARIA)), "Escuchar la fuente 1")}</p>{sec}</div>
<p class="fuente">Texto escrito para esta lección a partir de fuentes históricas. Cifras de población: censos de los EE. UU. de 1910 y 1920, según la <em>Encyclopedia of Chicago</em> (Chicago Historical Society), «Great Migration». Consultada en noviembre de 2026.</p>
<div class="articulo"><p><strong>Fuente 2 · Primaria: dos cartas de 1917</strong></p><p>{LE.escuchar(re.sub('<[^>]+>', '', CARTA1 + ' ' + CARTA2), "Escuchar las cartas")}</p>
<p><strong>Carta 1 · Sanford, Florida, 27 de abril de 1917</strong></p><p>{CARTA1}</p>
<p><strong>Carta 2 · Dallas, Texas, 23 de abril de 1917</strong></p><p>{CARTA2}</p></div>
<p class="fuente">Cartas anónimas recopiladas por Emmett J. Scott en <em>The Journal of Negro History</em> (1919). Dominio público. Traducción del <a href="{ARCHIVO}">Archivo de fuentes de LearnGED: Cartas de migrantes, 1917</a>, donde puede leer once cartas completas con su original en inglés.</p>
<h3>Analice las fuentes</h3>
{P("Fuentes 1", "¿Por qué las cartas son fuentes primarias?", ["Las publicó en 1919 una revista de historia muy conocida", "Las escribieron personas que vivían esa época y pensaban migrar", "Hablan de la Gran Migración con muchas cifras y fechas"], 1, {0: "Lo que importa es quién las escribió.", 2: "No tienen cifras."}, "Quien escribe estaba viviendo el hecho, en su época.")}
{P("Fuentes 2", "¿Qué información da <strong>solo</strong> la fuente secundaria?", ["Qué preguntaban las familias de Sanford antes de mudarse", "La edad del obrero que escribió desde Dallas", "Cuántos afroamericanos vivían en Chicago en 1910 y en 1920"], 2, {0: "Eso está en la carta.", 1: "Eso está en la carta."}, "Las cifras y el panorama vienen de la fuente secundaria.")}
{P("Fuentes 3", "¿Qué dato de la carta de Dallas muestra que su autor tenía experiencia de trabajo?", ["«Soy lector constante del Defender.»", "«Llevo cinco años con la firma.»", "«Tengo una esposa muy trabajadora.»"], 1, {0: "Habla de lo que lee.", 2: "Habla de su esposa."}, "Cinco años en el mismo trabajo muestran experiencia y estabilidad.")}
{P("Fuentes 4", "Según la fuente secundaria, ¿por qué había trabajo en el norte?", ["El <em>Chicago Defender</em> daba empleo a sus lectores", "En el norte se pagaba lo mismo que en el sur", "Las fábricas necesitaban obreros durante la guerra"], 2, {0: "Publicaba ofertas, no daba empleo.", 1: "El texto no lo dice."}, "Párrafo 2: la guerra y la menor llegada de inmigrantes europeos.")}
{P("Fuentes 5", "¿Cuál es el punto de vista de quien escribe las cartas?", ["El de un historiador que estudia la migración", "El de una persona que está decidiendo si migrar", "El de un periodista del <em>Chicago Defender</em>"], 1, {0: "No estudia: lo vive.", 2: "Escribe al periódico, no para él."}, "Escriben para pedir información antes de decidir.")}"""

    s4 = f"""<p>Al responder sobre fuentes, cite la evidencia como aprendió en la Lección 3.2 y diga siempre de qué fuente sale:</p>
<ul><li>Según la fuente secundaria, la población afroamericana de Chicago «pasó de unos 44 000 a unos 109 000 habitantes» entre 1910 y 1920.</li>
<li>En la carta de Dallas, el autor dice que es «lector constante del <em>Defender</em>».</li></ul>
{C.tabla("Idea central de cada fuente", ["Fuente", "Idea central"],
         [["Secundaria", "Millones de afroamericanos dejaron el sur por el trabajo en el norte y la discriminación en el sur, y Chicago fue uno de sus destinos principales."],
          ["Cartas", "Personas del sur que pensaban mudarse pedían información concreta sobre el trabajo y la vida en Chicago antes de decidirse."]])}
{P("Citar", "¿Cómo se cita correctamente la evidencia de una carta?", ["El autor de la carta de Dallas dice que es lector constante del Defender.»", "En la carta de Dallas, el autor dice que es «lector constante del Defender».", "En la carta de Dallas, «el autor es lector» constante, del Defender, dice."], 1, {0: "Falta la comilla de apertura.", 2: "Cambia las palabras de la cita."}, "Dice de qué fuente sale, con las palabras exactas entre comillas.")}"""

    s5 = f"""<p>Una fuente primaria y una secundaria sobre el mismo hecho suelen relacionarse de una de estas maneras:</p>
{C.tabla("Maneras en que se relacionan una fuente primaria y una secundaria", ["Relación", "En esta lección"],
         [["La primaria <strong>confirma</strong> lo que dice la secundaria.", "La secundaria dice que miles de personas escribieron al <em>Defender</em>; las cartas son pruebas de eso."],
          ["La secundaria <strong>explica el contexto</strong> de la primaria.", "Las cartas no dicen por qué había trabajo en el norte; la secundaria lo explica con la guerra."],
          ["La primaria <strong>añade</strong> lo que la secundaria no puede dar.", "Las cartas muestran las preguntas concretas de la gente: el trato, el alquiler, las escuelas."]])}
{P("Relación 1", "La fuente secundaria dice que «miles de personas» escribieron al <em>Defender</em>. ¿Qué hacen las cartas?", ["Lo contradicen con otros datos", "No tienen relación con eso", "Lo confirman con ejemplos reales"], 2, {0: "No contradicen nada.", 1: "Son justamente esas cartas."}, "Las cartas son pruebas de lo que afirma la secundaria.")}
{P("Relación 2", "¿Qué añaden las cartas que la fuente secundaria no puede dar?", ["La cantidad total de personas que migraron", "Las preguntas y la vida concreta de quienes migraban", "Las fechas en que empezó y terminó la migración"], 1, {0: "Eso lo da la secundaria.", 2: "Eso lo da la secundaria."}, "La voz directa: qué les preocupaba y quiénes eran.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Pídale a alguien de su familia que le cuente cómo llegó a este país o a esta ciudad. Su relato es una fuente primaria. Después busque un artículo sobre la migración de esa época y compare: ¿qué confirma?, ¿qué añade el relato?</p>")}"""

    secciones = [("s1", "Repaso: primaria y secundaria", s1), ("s2", "Qué aporta cada clase de fuente", s2), ("s3", "Lectura: la Gran Migración en dos fuentes", s3),
                 ("s4", "Citar evidencia de cada fuente", s4), ("s5", "Relacionar las dos fuentes", s5)]
    tarea = [("Más cartas.", f"Abra las <a href=\"{ARCHIVO}\">Cartas de migrantes, 1917</a> en el Archivo de fuentes y lea otras dos. Para cada una, escriba quién la escribe, qué pide y qué dice de su vida."),
             ("Relacione.", "Escriba un párrafo que relacione una de esas cartas con la fuente secundaria de la lección, con una cita de cada una."),
             ("Su fuente primaria.", "Piense en un documento de su propia vida que dentro de cien años sería una fuente primaria (una carta, una foto, un recibo, un mensaje). ¿Qué le contaría a un historiador?")]
    quiz = [
        ("¿Qué es una fuente primaria?", ["La creada por alguien que vivió el hecho, en su época", "La creada años después por un historiador", "La que aparece en las primeras páginas de un libro"], 0, {1: "Esa es la secundaria.", 2: "No tiene que ver con el lugar."}, "Creada por alguien que <strong>vivió</strong> el hecho."),
        ("¿Cuál es una fuente <strong>primaria</strong> sobre la Primera Guerra Mundial?", ["El diario de un soldado escrito en 1917", "Una enciclopedia publicada en el año 2000", "Un libro de texto de historia de hoy"], 0, {1: "Es secundaria.", 2: "Es secundaria."}, "El <strong>diario</strong> de un soldado."),
        ("Un artículo de periódico de 1917 sobre un hecho de 1917 es…", ["una fuente primaria para estudiar ese año", "siempre una fuente secundaria", "una fuente que no sirve para estudiar"], 0, {1: "Depende de la pregunta.", 2: "Sí sirve."}, "<strong>Primaria</strong> para estudiar 1917."),
        ("¿Cuál es un límite de la fuente secundaria?", ["Es una interpretación que depende de sus fuentes", "No tiene ningún dato ni cifra exacta", "Siempre está escrita por un testigo"], 0, {1: "Suele tener cifras.", 2: "Al contrario."}, "Es una <strong>interpretación</strong>."),
        ("¿Cuál es un límite de la fuente primaria?", ["Muestra solo lo que vio una persona, desde su punto de vista", "No dice nada de lo que se vivía en esa época", "Siempre fue escrita muchos años después del hecho"], 0, {1: "Al contrario.", 2: "Al contrario."}, "Muestra un <strong>solo punto de vista</strong>."),
        ("¿Qué preguntas conviene hacerse ante cualquier fuente?", ["Quién la escribió, cuándo y para qué", "Cuántas páginas tiene y de qué color es", "Si el autor es famoso o no"], 0, {1: "No.", 2: "No."}, "<strong>Quién, cuándo y para qué.</strong>"),
        ("Un artículo explica por qué en 1918 los hospitales estaban llenos; el diario de una enfermera dice que no había camas. ¿Cómo se relacionan?", ["La secundaria explica el contexto de la primaria", "La primaria contradice a la secundaria", "No tienen ninguna relación"], 0, {1: "No se oponen.", 2: "Hablan de lo mismo."}, "La secundaria <strong>explica el contexto</strong>."),
        ("Al citar evidencia de varias fuentes, conviene…", ["decir de qué fuente sale cada cita", "mezclar las citas sin decir de dónde son", "usar solo la fuente más larga"], 0, {1: "Así se confunden.", 2: "Se pierde información."}, "Decir de <strong>qué fuente</strong> sale."),
        ("El acta de nacimiento de su abuelo, para estudiar su familia, es una fuente…", ["primaria", "secundaria", "inventada"], 0, {1: "Es de su época.", 2: "No."}, "<strong>Primaria.</strong>"),
        ("Una foto de 1936 de una familia sin casa y un libro sobre la Gran Depresión. La foto…", ["confirma con un caso real lo que dice el libro", "contradice todo lo que explica el libro", "no se relaciona con el libro"], 0, {1: "No.", 2: "Sí se relaciona."}, "La foto <strong>confirma</strong> con un caso real."),
    ]
    filas = [
        ("Primaria o secundaria", "Distingo las dos clases según quién hizo la fuente y cuándo.", "Dudo con los periódicos y los libros.", "Las confundo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Citar", "Cito la evidencia y digo de qué fuente sale.", "Olvido decir la fuente.", "No sé citar (<a href=\"#s4\">repase la sección 4</a>)."),
        ("Relacionar", "Explico si una fuente confirma, explica o añade.", "Lo veo solo a veces.", "No veo la relación (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya distingue las fuentes, cita su evidencia y explica cómo se relacionan. ¡Terminó el Tema 5! En el Tema 6 leerá en las materias: <strong>gráficas, datos y procedimientos</strong>.</p>"
    glosario = [("Fuente primaria", "La creada por alguien que vivió el hecho, en su época."), ("Fuente secundaria", "La creada después por alguien que estudió el hecho."),
                ("Punto de vista", "Desde dónde ve el hecho quien escribe: quién es, cuándo y para qué escribe."), ("Gran Migración", "El traslado de millones de afroamericanos del sur al norte y al oeste de los EE. UU., entre 1916 y 1970.")]
    conexion = ("<p>En la Lección 6.2 del Nivel 2 conoció las fuentes primarias y secundarias. Hoy las cita y las relaciona, como pide el GED de Estudios Sociales.</p>"
                f"<p><strong>Lo que necesita:</strong> su cuaderno y, para la tarea, el <a href=\"{ARCHIVO}\">Archivo de fuentes</a>.</p>")
    estd = LE.estandares(["R.7.3", "R.7.2"], base=["R.2.8", "W.1"])
    return C.pagina_leccion(N, LE.titulo(N), "La voz de quien lo vivió y la mirada de quien lo estudió.", ["Fuentes", "Estudios Sociales"],
                            ["<strong>Distinguir</strong> fuentes primarias y secundarias, y su fuerza y su límite.", "<strong>Analizar</strong> quién escribió una fuente, cuándo y para qué.",
                             "<strong>Citar</strong> la evidencia diciendo de qué fuente sale.", "<strong>Explicar</strong> si una fuente confirma, explica o añade."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-1", LE.titulo("6-1")), glosario, P)


def practica():
    cl = [{"enun": f'<p class="frase">{t}</p><p>¿Qué clase de fuente es?</p>', "ops": PS, "ok": k, "enOrden": True,
           "pista": "¿Quien la hizo vivió el hecho, en su época, o lo estudió después?", "exp": f"<strong>{PS[k]}.</strong> {n}"} for t, k, n in CL]
    ev = [{"enun": texto(f) + f'<p class="rel">{q}</p>', "ops": o, "ok": 0, "pista": "Esa cita es de las fuentes, pero ¿responde a esta pregunta? Fíjese de qué fuente sale.", "exp": n} for f, q, o, n in EV]
    re_ = [{"enun": texto([f"<strong>Fuente primaria.</strong> {p}", f"<strong>Fuente secundaria.</strong> {s}"]) + "<p><strong>¿Cómo se relacionan?</strong></p>", "ops": REL, "ok": k, "enOrden": True,
            "pista": "¿La primaria es un ejemplo de lo que dice la secundaria? ¿La secundaria explica por qué pasó? ¿La primaria da algo nuevo?", "exp": f"<strong>{REL[k]}.</strong> {n}"} for p, s, k, n in RE]
    mods = [("clase", "¿Primaria o secundaria?", C.om("m1", "Decida si cada fuente es primaria o secundaria para el tema indicado.")),
            ("evidencia", "La evidencia de cada fuente", C.om("m2", "Lea las fuentes y elija la cita que responde a la pregunta.") + f'<p class="fuente">Cartas de 1917 del <a href="{ARCHIVO}">Archivo de fuentes</a>.</p>'),
            ("relacion", "¿Cómo se relacionan las fuentes?", C.om("m3", "Decida si la primaria confirma, si la secundaria explica o si la primaria añade.") + '<p class="fuente">Pares de fuentes descritos para practicar.</p>')]
    js = C.js_datos("CL", cl) + C.js_datos("EV", ev) + C.js_datos("RE", re_) + 'creaBanco("m1", CL);\ncreaBanco("m2", EV);\ncreaBanco("m3", RE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
