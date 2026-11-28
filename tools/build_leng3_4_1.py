# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 4.1 · Estructuras del texto: cronología, comparación y causa-efecto.
Fuente: clases_leng3/clase_4-1.html (GEDparaHispanos) y gramatica/n3-l4-1.html, adaptadas al marco de LearnGED.
Datos: Chicago Architecture Center, «The Chicago L» (architecture.org); Ciudad de Chicago, comunicado del 6 de junio de 2017 (Union Loop);
Distrito Metropolitano de Recuperación de Agua (MWRD), «Tunnel and Reservoir Plan» (mwrd.org). Consultados en noviembre de 2026.
Uso: python3 tools/build_leng3_4_1.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_3_1 import texto

LE.nivel(3)
N = "4-1"
E = ["Descripción", "Secuencia cronológica", "Comparación y contraste", "Causa y efecto", "Problema y solución"]
O = ["Mapa de rasgos", "Línea del tiempo", "Diagrama de Venn o tabla de dos columnas", "Cadena de causa y efecto", "Cajas de problema y solución"]


def S(t):
    return f'<b class="cl-w">{t}</b>'


TA = f"El 6 de junio de 1892 salió el primer tren elevado de Chicago, que corría por encima de las calles del South Side. {S('Cinco años después')}, en 1897, se terminó el circuito de vías elevadas que rodea el centro, la zona conocida como el Loop. {S('Más tarde')}, en 1943, abrió el primer tramo subterráneo, bajo la calle State. {S('Finalmente')}, en 1947, todas las líneas pasaron a manos de la Autoridad de Tránsito de Chicago, la CTA, que las administra hasta hoy."
TB = f"{S('Tanto')} rentar {S('como')} comprar una casa exigen un pago cada mes y una buena relación con quien recibe ese dinero. {S('Sin embargo')}, son muy distintos. Quien renta puede mudarse con más facilidad y no paga las reparaciones grandes; {S('en cambio')}, quien compra no puede irse tan rápido, pero cada pago lo acerca a ser dueño. {S('Mientras que')} la renta puede subir cada año, la cuota de un préstamo con interés fijo se mantiene igual."
TC = f"En buena parte de Chicago, el agua de la lluvia y las aguas negras de las casas corren por las mismas tuberías. Cuando cae una tormenta muy fuerte, el sistema se llena y, {S('como resultado')}, el agua sube por los desagües y entra a los sótanos. {S('Debido a')} ese mismo exceso, a veces hay que dejar salir agua sucia al río. {S('Para resolver el problema')}, en los años setenta se empezó a construir el llamado Túnel Profundo, un sistema de túneles y depósitos bajo tierra que guarda el agua de las tormentas hasta que puede limpiarse."
ES = [("Para sembrar tomates, primero elija un lugar con sol. Luego cave un hoyo profundo y ponga la planta. Después riéguela bien y, finalmente, clávele una vara para que crezca derecha.", 1, [2, 3], "<em>Primero, luego, después, finalmente</em>: pasos en orden."),
      ("El jaguar es el felino más grande de América. Tiene la piel amarilla con manchas negras en forma de roseta, una cabeza ancha y mandíbulas muy fuertes. Además, a diferencia de otros felinos, le gusta nadar.", 0, [2, 4], "Explica cómo es el jaguar. <em>A diferencia de</em> aparece una vez, pero la mayor parte describe."),
      ("El autobús y el tren llegan al centro en casi el mismo tiempo. Sin embargo, el autobús para en más esquinas, mientras que el tren es más rápido en las horas de tráfico. En cambio, el autobús llega más cerca de muchas casas.", 2, [1, 0], "<em>Sin embargo, mientras que, en cambio</em>: compara dos medios de transporte."),
      ("Durante el verano casi no llovió. Por eso el nivel del río bajó tanto que los barcos de carga no podían pasar. Como resultado, muchos productos tardaron más en llegar a las tiendas y subieron de precio.", 3, [1, 4], "Una cadena: sequía → río bajo → retrasos → precios más altos."),
      ("Los vecinos se quejaban de que los autos pasaban muy rápido frente a la escuela. Para resolverlo, la ciudad instaló reductores de velocidad y un guardia en el cruce. Desde entonces, no ha habido accidentes.", 4, [3, 1], "Problema, lo que se hizo y el resultado."),
      ("En 1959 triunfó la revolución en Cuba. En los años siguientes, miles de cubanos salieron hacia Miami. Más tarde, en 1980, el éxodo del Mariel llevó a más de cien mil personas en pocos meses.", 1, [3, 2], "Fechas en orden: secuencia cronológica."),
      ("Las abejas visitan las flores para alimentarse. Al hacerlo, llevan el polen de una flor a otra, y gracias a eso muchas plantas producen frutos. Por lo tanto, si desaparecen las abejas, habrá menos frutas y verduras.", 3, [0, 4], "<em>Gracias a eso, por lo tanto</em>: causas y consecuencias."),
      ("Tanto el español como el portugués vienen del latín y comparten muchas palabras. Sin embargo, la pronunciación es muy distinta: el portugués tiene sonidos nasales que el español no tiene.", 2, [0, 3], "<em>Tanto… como, sin embargo</em>: semejanzas y diferencias."),
      ("Muchos estudiantes adultos no pueden ir a clase porque trabajan en horarios que cambian. Una solución que ha funcionado son las clases en línea grabadas, que cada uno ve cuando puede.", 4, [3, 2], "Un problema y una solución que funciona."),
      ("El corazón humano tiene cuatro cavidades: dos aurículas arriba y dos ventrículos abajo. Sus paredes son de músculo, y entre las cavidades hay válvulas que dejan pasar la sangre en una sola dirección.", 0, [1, 3], "Explica cómo está formado el corazón: sus partes.")]
PS = [("<b>Primero</b> se lava el arroz y después se fríe.", 1, [2, 0], "Orden de pasos."),
      ("<b>Como resultado</b> de la huelga, la fábrica cerró una semana.", 3, [1, 4], "Introduce una consecuencia."),
      ("<b>A diferencia de</b> los perros, los gatos no necesitan salir a pasear.", 2, [0, 3], "Marca un contraste."),
      ("<b>Una solución</b> fue abrir la biblioteca también los domingos.", 4, [3, 1], "Presenta una solución."),
      ("El mercado <b>está formado por</b> cincuenta puestos de comida y ropa.", 0, [2, 4], "Dice cómo es, de qué partes se compone."),
      ("<b>Años más tarde</b>, la familia volvió a su pueblo.", 1, [3, 2], "Marca el paso del tiempo."),
      ("<b>Debido al</b> frío, se congelaron las tuberías.", 3, [0, 1], "Introduce la causa."),
      ("<b>Ambos</b> hermanos estudiaron en la misma escuela.", 2, [0, 1], "Señala algo en común: una semejanza."),
      ("<b>El problema</b> es que el edificio no tiene elevador.", 4, [0, 3], "Presenta un problema."),
      ("Mi hija estudia de día, <b>mientras que</b> mi hijo estudia de noche.", 2, [1, 3], "Aquí <em>mientras que</em> contrasta, no indica tiempo."),
      ("<b>Mientras</b> esperaba el autobús, empezó a llover.", 1, [2, 3], "Aquí <em>mientras</em> indica tiempo: dos cosas a la vez."),
      ("La tormenta <b>provocó</b> cortes de luz en todo el barrio.", 3, [4, 0], "<em>Provocar</em> indica causa y efecto."),
      ("<b>Por ejemplo</b>, el ajolote puede regenerar sus patas.", 0, [3, 2], "Da un ejemplo para describir."),
      ("<b>Gracias a</b> la nueva ley, los inquilinos tienen más protección.", 4, [1, 0], "Muestra el resultado de una solución."),
      ("<b>Sin embargo</b>, la ciudad del sur es más barata que la del norte.", 2, [1, 4], "Introduce un contraste."),
      ("<b>Finalmente</b>, se firmó el tratado de paz.", 1, [4, 3], "Cierra una secuencia.")]
OR = [("La historia de su familia desde que sus abuelos llegaron al país, año por año.", 1, [2, 0]),
      ("Las diferencias y semejanzas entre la escuela de su país y la de los Estados Unidos.", 2, [1, 3]),
      ("Cómo el cierre de una fábrica dejó sin trabajo a cientos de personas y bajaron las ventas de las tiendas del barrio.", 3, [1, 0]),
      ("Las características del águila calva: su tamaño, su plumaje, lo que come y dónde vive.", 0, [2, 4]),
      ("Un barrio sin transporte que logró, con firmas de los vecinos, que pusieran una nueva ruta de autobús.", 4, [3, 1]),
      ("Los pasos para solicitar una licencia de manejo en Illinois.", 1, [0, 4]),
      ("Rentar o comprar una casa: ventajas de cada opción.", 2, [4, 3]),
      ("Por qué la contaminación del aire provoca enfermedades y cómo esas enfermedades aumentan los gastos médicos.", 3, [2, 0])]


def tres(c, a, b, L=E):
    return [L[c], L[a], L[b]]


def organizadores():
    caja = lambda tit, cuerpo, pie: f'<figure class="org"><figcaption>{tit}</figcaption><div class="org-dib" aria-hidden="true">{cuerpo}</div><p>{pie}</p></figure>'
    b = lambda t, c="": f'<span class="org-b{c}">{t}</span>'
    return ('<div class="orgs">'
            + caja("Descripción · mapa de rasgos", b("tema", " org-c") + b("rasgo") + b("rasgo") + b("rasgo"), "El tema en el centro y sus rasgos alrededor.")
            + caja("Secuencia · línea del tiempo", b("1") + "→" + b("2") + "→" + b("3") + "→" + b("4"), "Los hechos o pasos en orden, uno detrás de otro.")
            + caja("Comparación · dos columnas", b("A") + b("B") + b("en qué se parecen", " org-l") + b("en qué se diferencian", " org-l"), "Un diagrama de Venn también sirve.")
            + caja("Causa y efecto · cadena", b("causa") + "→" + b("efecto") + "→" + b("efecto"), "Un efecto puede ser la causa del siguiente.")
            + caja("Problema y solución · tres cajas", b("problema") + "→" + b("solución") + "→" + b("resultado"), "Qué pasaba, qué se hizo y qué se logró.")
            + "</div>")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Piense en una receta, en un anuncio que compara dos teléfonos y en una noticia sobre por qué subió la gasolina. Los tres son textos informativos, pero están organizados de manera muy distinta: el primero va paso a paso, el segundo compara y el tercero explica causas y efectos. Reconocer cómo está organizado un texto le ayuda a entenderlo más rápido y a encontrar la respuesta sin releerlo entero.</p>
<p>La <strong>estructura</strong> de un texto es la forma en que el autor ordena sus ideas. En el Nivel 2 estudió la estructura de una historia: inicio, nudo y desenlace. Los textos informativos también tienen estructuras, y cada una responde a una pregunta distinta:</p>
<ul><li>¿Cómo es? → <strong>descripción</strong></li><li>¿En qué orden pasó? → <strong>secuencia cronológica</strong></li><li>¿En qué se parecen y en qué se diferencian? → <strong>comparación y contraste</strong></li>
<li>¿Por qué pasó y qué provocó? → <strong>causa y efecto</strong></li><li>¿Qué problema hay y cómo se resuelve? → <strong>problema y solución</strong></li></ul>
{C.caja("tip", "Un truco del GED", "<p>Si la pregunta dice «¿qué ocurrió después de…?», busque en un texto cronológico la palabra señal de tiempo. Si dice «¿qué causó…?», busque las palabras de causa. La estructura le dice dónde mirar.</p>")}"""

    s2 = f"""{C.tabla("Las cinco estructuras del texto informativo con sus palabras señal", ["Estructura", "Qué hace el autor", "Palabras señal"],
         [["Descripción", "Explica cómo es algo: sus partes, rasgos o ejemplos.", "por ejemplo, se caracteriza por, tiene, está formado por, también"],
          ["Secuencia cronológica", "Cuenta hechos o pasos en el orden en que ocurren.", "primero, luego, después, finalmente, en 1892, años más tarde, mientras tanto"],
          ["Comparación y contraste", "Muestra semejanzas y diferencias entre dos o más cosas.", "igual que, también, ambos, en cambio, sin embargo, a diferencia de, mientras que"],
          ["Causa y efecto", "Explica por qué pasa algo y qué consecuencias tiene.", "porque, por eso, por lo tanto, como resultado, debido a, provoca, en consecuencia"],
          ["Problema y solución", "Presenta un problema y una o varias maneras de resolverlo.", "el problema, la dificultad, una solución, para resolver, se propuso, gracias a"]])}
{C.caja("ojo", "Mientras y también tienen dos usos", "<p><em>Mientras</em> puede indicar tiempo («mientras cocinaba») o contraste («Ana trabaja de día, mientras que Luis trabaja de noche»); <em>también</em> aparece en descripciones y en comparaciones. Las palabras señal son pistas, no pruebas: mire cómo se usan en el texto.</p>")}
{P("Señal 1", "«<b class=\"marca\">Debido a</b> la lluvia, se suspendió el partido.» ¿A qué estructura apunta?", tres(3, 0, 4), 0, {1: "No describe cómo es algo.", 2: "No hay un problema con su solución."}, "<em>Debido a</em> introduce la causa.")}
{P("Señal 2", "«Luis trabaja de día, <b class=\"marca\">mientras que</b> su esposa trabaja de noche.» ¿A qué estructura apunta?", tres(1, 2, 3), 1, {0: "Aquí <em>mientras que</em> no indica tiempo.", 2: "No hay una causa."}, "Aquí <em>mientras que</em> contrasta dos horarios.")}"""

    s3 = f"""<p>Un <strong>organizador gráfico</strong> es un dibujo sencillo que muestra cómo se relacionan las ideas. Cada estructura tiene el suyo:</p>
{organizadores()}
{P("Organizador 1", "¿Qué organizador sirve para comparar dos cosas?", ["Una cadena de causas", "Una línea del tiempo", "Un diagrama de Venn"], 2, {0: "Sirve para causa y efecto.", 1: "Sirve para la secuencia."}, "El <strong>diagrama de Venn</strong> o una tabla de dos columnas.")}"""

    plano = " ".join(re.sub("<[^>]+>", "", t) for t in (TA, TB, TC))
    s4 = f"""<p>Lea los tres textos. Para cada uno, decida la estructura y dibuje en su cuaderno su organizador gráfico. Después pulse <strong>Mostrar las palabras señal</strong> para comprobar sus pistas.</p>
<p>{LE.escuchar(plano, "Escuchar los textos")} <button type="button" class="btn-sec" id="btn-s41" aria-pressed="false">Mostrar las palabras señal</button></p>
<div class="lectura-cl" id="lect-41">
<div class="articulo"><p><strong>Texto A · El tren elevado de Chicago</strong></p><p>{TA}</p></div>
<div class="articulo"><p><strong>Texto B · Rentar o comprar casa</strong></p><p>{TB}</p></div>
<div class="articulo"><p><strong>Texto C · ¿Por qué se inundan los sótanos?</strong></p><p>{TC}</p></div></div>
<p class="fuente">Datos de los textos A y C: Chicago Architecture Center, «The Chicago L»; Ciudad de Chicago, comunicado del 6 de junio de 2017; Distrito Metropolitano de Recuperación de Agua del Gran Chicago (MWRD), «Tunnel and Reservoir Plan». Consultados en noviembre de 2026.</p>
<script>(function(){{var b=document.getElementById("btn-s41"),t=document.getElementById("lect-41");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las palabras señal":"Mostrar las palabras señal";}});}})();</script>
<h3>¿Cómo está organizado?</h3>
{P("Textos 1", "¿Qué estructura tiene el texto A?", tres(1, 2, 3), 0, {1: "¿Qué compara? Fíjese en las fechas.", 2: "No explica por qué pasó algo."}, "Fechas en orden y <em>después, más tarde, finalmente</em>.")}
{P("Textos 2", "¿Qué estructura tiene el texto B?", tres(4, 1, 2), 2, {0: "No hay un problema que resolver.", 1: "No hay fechas ni pasos."}, "<em>Tanto… como, sin embargo, en cambio, mientras que</em>: compara rentar y comprar.")}
{P("Textos 3", "Según el texto A, ¿qué pasó <strong>después</strong> de que se terminara el Loop?", ["Salió el primer tren elevado", "Abrió el primer tramo subterráneo", "Se fundó la ciudad de Chicago"], 1, {0: "Eso fue antes, en 1892.", 2: "El texto no habla de eso."}, "En un texto cronológico, la respuesta está en el hecho siguiente: 1943.")}
{P("Textos 4", "Según el texto C, ¿qué <strong>causa</strong> que el agua entre a los sótanos?", ["Que se haya construido el Túnel Profundo", "Que el río esté demasiado limpio", "Que el sistema se llene durante una tormenta fuerte"], 2, {0: "Esa es la solución.", 1: "El texto no dice eso."}, "La causa aparece antes de <em>como resultado</em>.")}"""

    s5 = f"""<p>Los textos reales a menudo <strong>combinan estructuras</strong>. El texto C, por ejemplo, explica causas y efectos (la tormenta llena el sistema y el agua entra a los sótanos) y al final presenta una solución (el Túnel Profundo). Cuando una pregunta pide «la estructura» de un texto, busque la <strong>principal</strong>: la que organiza la mayor parte.</p>
{C.caja("tip", "Pregúntese", "<p>¿Qué pregunta responde la mayor parte del texto? El texto C responde sobre todo a «¿por qué se inundan los sótanos?», así que su estructura principal es causa y efecto; la solución es el cierre.</p>")}
{P("Principal", "¿Cuál es la estructura principal del texto C?", tres(0, 3, 2), 1, {0: "No describe cómo es algo.", 2: "No compara dos cosas."}, "Explica por qué se inundan los sótanos. Al final añade una solución.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Elijan un tema de la casa (cómo preparar el café, el carro viejo y el nuevo, por qué subió la cuenta de la luz). Cada uno lo explica en voz alta con una estructura distinta y el otro adivina cuál usó.</p>")}"""

    secciones = [("s1", "¿Por qué importa la estructura?", s1), ("s2", "Las cinco estructuras", s2), ("s3", "Un organizador para cada estructura", s3),
                 ("s4", "Lectura: tres textos, tres estructuras", s4), ("s5", "Cuando un texto combina estructuras", s5)]
    tarea = [("Tres organizadores.", "Dibuje en su cuaderno el organizador de cada texto de la lectura y llénelo con su información."),
             ("Escriba con estructura.", "Escriba un párrafo de cinco oraciones sobre un tema que conozca bien con una de las cinco estructuras. Subraye sus palabras señal."),
             ("Busque en su día.", "Encuentre en casa o en internet tres textos reales (una receta, un anuncio, una noticia…) y anote la estructura de cada uno y una palabra señal que lo pruebe.")]
    quiz = [
        ("¿Qué estructura responde a «¿en qué orden pasó?»?", ["Secuencia cronológica", "Descripción", "Problema y solución"], 0, {1: "Responde «¿cómo es?».", 2: "Responde «¿cómo se resuelve?»."}, "<strong>Secuencia cronológica.</strong>"),
        ("¿Qué palabras señal indican comparación y contraste?", ["en cambio, sin embargo, ambos", "primero, luego, finalmente", "porque, por eso, provoca"], 0, {1: "Son de secuencia.", 2: "Son de causa y efecto."}, "<strong>En cambio, sin embargo, ambos.</strong>"),
        ("«Como resultado de la sequía, subió el precio del maíz.» ¿Qué estructura tiene?", ["Causa y efecto", "Descripción", "Secuencia cronológica"], 0, {1: "No describe.", 2: "No ordena fechas ni pasos."}, "<strong>Causa y efecto.</strong>"),
        ("Un texto explica cómo es el sistema solar, planeta por planeta, con sus rasgos. ¿Qué estructura tiene?", ["Descripción", "Problema y solución", "Causa y efecto"], 0, {1: "No hay problema.", 2: "No hay causas."}, "<strong>Descripción.</strong>"),
        ("¿Qué organizador gráfico corresponde a la secuencia cronológica?", ["Una línea del tiempo", "Un diagrama de Venn", "Una tabla de dos columnas"], 0, {1: "Sirve para comparar.", 2: "Sirve para comparar."}, "Una <strong>línea del tiempo</strong>."),
        ("En una cadena de causa y efecto…", ["un efecto puede ser la causa del siguiente", "todas las causas ocurren a la vez", "el efecto siempre va antes de la causa"], 0, {1: "No.", 2: "Es al revés."}, "Un efecto puede ser la <strong>causa</strong> del siguiente."),
        ("Cuando un texto combina estructuras, ¿cuál es la principal?", ["La que organiza la mayor parte del texto", "La que aparece en la última oración", "La que tiene más palabras señal juntas"], 0, {1: "Puede ser solo el cierre.", 2: "Las palabras señal son pistas, no pruebas."}, "La que organiza la <strong>mayor parte</strong>."),
        ("«Mientras cocinaba, escuchaba la radio.» Aquí <em>mientras</em> indica…", ["tiempo: dos acciones a la vez", "contraste entre dos personas", "la causa de una acción"], 0, {1: "No hay dos personas.", 2: "No."}, "<strong>Tiempo.</strong>"),
        ("«Para resolver la falta de parques, el barrio convirtió un terreno en jardín.» ¿Qué estructura tiene?", ["Problema y solución", "Secuencia cronológica", "Comparación y contraste"], 0, {1: "No hay pasos ni fechas.", 2: "No compara."}, "<strong>Problema y solución.</strong>"),
        ("«El colibrí se caracteriza por su tamaño pequeño y sus alas muy rápidas.» ¿Qué estructura tiene?", ["Descripción", "Causa y efecto", "Problema y solución"], 0, {1: "No hay causa.", 2: "No hay problema."}, "<strong>Descripción.</strong>"),
    ]
    filas = [
        ("Estructuras", "Reconozco las cinco estructuras por la pregunta que responden.", "Confundo a veces dos de ellas.", "No las distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Palabras señal", "Uso las palabras señal como pistas y miro cómo se usan.", "Me fío solo de una palabra.", "No las veo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Organizadores", "Dibujo el organizador adecuado para cada texto.", "Dudo cuál usar.", "Me cuesta (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya reconoce cómo se organiza un texto y lo usa para encontrar información. En la próxima lección verá los <strong>géneros literarios</strong>: poema, drama y prosa.</p>"
    glosario = [("Estructura del texto", "La forma en que el autor ordena sus ideas."), ("Palabra señal", "Palabra que indica cómo se relacionan las ideas: primero, sin embargo, por eso…"),
                ("Organizador gráfico", "Dibujo sencillo que muestra cómo se relacionan las ideas de un texto."), ("Secuencia cronológica", "Hechos o pasos contados en el orden en que ocurren.")]
    conexion = ("<p>En la Lección 4.2 del Nivel 2 estudió la estructura de una historia. Hoy ve cómo se organizan los textos informativos de Ciencias y Estudios Sociales.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno para dibujar organizadores gráficos.</p>")
    estd = LE.estandares(["R.5.1", "R.3.3"], base=["R.3.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Cómo ordena el autor sus ideas.", ["Comprensión", "Estructura del texto"],
                            ["<strong>Reconocer</strong> cinco estructuras del texto informativo.", "<strong>Usar</strong> las palabras señal como pistas.",
                             "<strong>Representar</strong> cada estructura con su organizador gráfico.", "<strong>Encontrar</strong> la estructura principal de un texto que combina varias."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-2", LE.titulo("4-2")), glosario, P)


def practica():
    es = [{"enun": texto([t]) + "<p><strong>¿Qué estructura tiene este texto?</strong></p>", "ops": tres(c, *d), "ok": 0,
           "pista": "Busque las palabras señal y pregúntese qué pregunta responde la mayor parte del texto.", "exp": n} for t, c, d, n in ES]
    ps = [{"enun": f'<p class="frase">{t.replace("<b>", "<b class=marca>")}</p><p>¿A qué estructura apunta la palabra marcada?</p>', "ops": tres(c, *d), "ok": 0,
           "pista": "¿La palabra ordena en el tiempo, compara, da una causa, presenta un problema o describe?", "exp": f"<strong>{E[c]}.</strong> {n}"} for t, c, d, n in PS]
    org = [{"enun": f'<p class="frase">{t}</p><p>¿Qué organizador usaría?</p>', "ops": tres(c, *d, L=O), "ok": 0,
            "pista": "¿El texto ordena en el tiempo, compara, encadena causas, describe o resuelve un problema?", "exp": f"<strong>{O[c]}.</strong>"} for t, c, d in OR]
    mods = [("estructura", "¿Qué estructura tiene?", C.om("m1", "Lea el texto breve y elija su estructura principal.")),
            ("senal", "Las palabras señal", C.om("m2", "Decida a qué estructura apunta la palabra marcada.")),
            ("organizador", "El organizador adecuado", C.om("m3", "Elija el organizador gráfico que mejor representa cada tema."))]
    js = C.js_datos("ES", es) + C.js_datos("PS", ps) + C.js_datos("OR", org) + 'creaBanco("m1", ES);\ncreaBanco("m2", PS);\ncreaBanco("m3", OR);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
