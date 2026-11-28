# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 4.3 · Leer con ilustraciones y características del texto.
Fuente: clases_leng2/clase_4-3.html (GEDparaHispanos) y gramatica/n2-l4-3.html, adaptadas al marco de LearnGED.
Dato real: agua para emergencias según Ready.gov (FEMA), consultado el 28 de noviembre de 2026.
Uso: python3 tools/build_leng2_4_3.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "4-3"
TX = [("Cómo cuidar sus dientes", ["Cepillarse bien", "El hilo dental", "La visita al dentista"], "Cepíllese dos veces al día durante dos minutos."),
      ("Los volcanes", ["¿Cómo se forma un volcán?", "Tipos de erupciones", "Los volcanes de América Latina"], "El volcán Popocatépetl, en México, sigue activo."),
      ("Cómo abrir una cuenta de banco", ["Qué documentos llevar", "Cuenta de ahorros o cuenta corriente", "Cómo evitar las comisiones"], "Cada banco pide sus propios documentos: pregunte antes de ir."),
      ("La migración de la mariposa monarca", ["Un viaje de miles de kilómetros", "Dónde pasan el invierno", "Por qué están en peligro"], "Millones de mariposas cubren los árboles en Michoacán."),
      ("Ahorrar energía en casa", ["Las luces", "La calefacción y el aire acondicionado", "Los aparatos que se quedan enchufados"], "Un foco LED gasta mucho menos que uno común."),
      ("Los derechos del trabajador", ["El salario mínimo", "Las horas extras", "La seguridad en el trabajo"], "Todo trabajador tiene derecho a un lugar de trabajo seguro.")]
PRED = [(0, ["Consejos para mantener los dientes sanos", "La historia de los dentistas más famosos", "Los mejores cepillos del mercado y sus precios"], "Los tres subtítulos son hábitos de cuidado."),
        (1, ["Cómo se forman los volcanes, cómo hacen erupción y cuáles hay en América Latina", "Cómo escapar de un incendio forestal y proteger a la familia", "Los mejores lugares turísticos de México y de Centroamérica"], "El título da el tema y los subtítulos, las partes."),
        (2, ["Los pasos y documentos para abrir una cuenta de banco", "La historia de los bancos en Estados Unidos", "Por qué es mejor guardar el dinero en casa"], "Los subtítulos explican qué llevar, qué tipo elegir y cómo ahorrar en comisiones."),
        (3, ["El largo viaje de la mariposa monarca y los peligros que enfrenta", "Cómo cultivar flores en el jardín para atraer mariposas", "Los insectos más peligrosos de todo el mundo"], "Viaje, invierno y peligro: esas son las tres partes."),
        (4, ["Maneras de gastar menos electricidad y gas en casa", "Cómo instalar un aire acondicionado en casa", "La historia de la electricidad en el mundo"], "Cada subtítulo es un lugar de la casa donde se puede ahorrar."),
        (5, ["Los derechos básicos de quien trabaja: salario, horas extras y seguridad", "Cómo conseguir un trabajo mejor pagado en poco tiempo", "La historia de los sindicatos en Estados Unidos"], "Los subtítulos nombran tres derechos.")]
SECC = [(0, "¿Cuántas veces al año conviene ir al dentista?", 2), (0, "¿Cómo se usa el hilo dental?", 1), (1, "¿Qué volcanes hay en Guatemala?", 2),
        (1, "¿Qué pasa debajo de la tierra para que nazca un volcán?", 0), (2, "¿Sirve el pasaporte como identificación?", 0), (2, "¿Cómo evito pagar dinero cada mes por tener la cuenta?", 2),
        (3, "¿En qué lugar de México descansan las mariposas en invierno?", 1), (3, "¿Por qué hay cada vez menos mariposas?", 2), (4, "¿Conviene desenchufar el televisor por la noche?", 2),
        (4, "¿A qué temperatura poner el termostato en invierno?", 1), (5, "¿Cuánto deben pagarme si trabajo más de cuarenta horas?", 1), (5, "¿Qué hago si en mi trabajo no me dan equipo de protección?", 2)]
IMG = [("Un dibujo de una boca abierta con un cepillo inclinado sobre los dientes.", "Incline el cepillo hacia la encía.", ["Párrafo sobre cómo cepillarse bien", "Párrafo sobre el precio de las consultas", "Párrafo sobre la historia del cepillo"], 0),
       ("Un mapa de América del Norte con flechas de Canadá a México.", "La ruta de las monarcas cada otoño.", ["Párrafo sobre por qué están en peligro", "Párrafo sobre el viaje de miles de kilómetros", "Párrafo sobre qué comen las orugas"], 1),
       ("Una gráfica de barras con el gasto de luz de una casa mes a mes.", "El gasto sube en julio y agosto por el aire acondicionado.", ["Párrafo sobre las luces LED", "Párrafo sobre la calefacción y el aire acondicionado", "Párrafo sobre la historia de la electricidad"], 1),
       ("Una foto de un trabajador con casco, chaleco y gafas.", "El equipo de protección es obligatorio en la construcción.", ["Párrafo sobre la seguridad en el trabajo", "Párrafo sobre el salario mínimo", "Párrafo sobre las vacaciones pagadas"], 0),
       ("Una tabla que compara dos tipos de cuenta con sus comisiones.", "Comparación de una cuenta de ahorros y una cuenta corriente.", ["Párrafo sobre los documentos que hay que llevar", "Párrafo sobre cómo elegir el tipo de cuenta", "Párrafo sobre los horarios del banco"], 1),
       ("Un dibujo del interior de un volcán con la lava subiendo por una chimenea.", "El magma sube desde el interior de la Tierra.", ["Párrafo sobre cómo se forma un volcán", "Párrafo sobre los volcanes de América Latina", "Párrafo sobre los terremotos"], 0),
       ("Un dibujo de un enchufe con varios cables y una regleta apagada.", "Una regleta con interruptor apaga todo de una vez.", ["Párrafo sobre los aparatos que se quedan enchufados", "Párrafo sobre las ventanas", "Párrafo sobre la calefacción"], 0),
       ("Una foto de un bosque de oyameles cubierto de mariposas naranjas.", "Así pasan el invierno las monarcas en Michoacán.", ["Párrafo sobre el viaje de ida", "Párrafo sobre dónde pasan el invierno", "Párrafo sobre cómo se reconoce una monarca"], 1)]
CARACT = ["Título", "Subtítulo", "Negrita", "Pie de foto", "Lista", "Recuadro", "Tabla", "Glosario"]
QUE_ES = [("Va arriba de todo, en letra grande, y dice el tema del texto completo.", 0), ("Divide el texto en partes y dice de qué trata cada una.", 1),
          ("Una palabra escrita en letra más gruesa porque es importante.", 2), ("Una o dos oraciones debajo de una imagen que explican lo que muestra.", 3),
          ("Varios elementos uno debajo del otro, con puntos o números.", 4), ("Un cuadro de color, aparte del texto, con un dato curioso.", 5),
          ("Datos organizados en filas y columnas.", 6), ("Una lista de palabras difíciles con su significado, al final del texto.", 7),
          ("En una receta, los ingredientes escritos uno debajo del otro.", 4), ("«¿Sabía que…?», en un cuadro aparte con fondo amarillo.", 5),
          ("El horario de los autobuses con las horas de salida y de llegada de cada parada.", 6), ("«Figura 2. El corazón tiene cuatro cavidades.»", 3)]
FUENTE = ('<p class="fuente">Fuente del dato del agua: Ready.gov, de la Agencia Federal para el Manejo de Emergencias (FEMA), «Build a Kit»: un galón de agua por persona y por día, para beber y para la higiene. '
          'Consultado el 28 de noviembre de 2026. La tabla multiplica ese dato por tres días.</p>')

MAPA = """<svg viewBox="0 0 420 220" role="img" aria-labelledby="fig1-t fig1-d" style="max-width:420px;width:100%">
<title id="fig1-t">Mapa de un plan familiar</title><desc id="fig1-d">La casa de la familia. Una flecha corta lleva al punto de encuentro 1, en la esquina del parque, a dos cuadras. Una flecha larga lleva al punto de encuentro 2, la escuela, fuera del barrio.</desc>
<defs><marker id="fl" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#b42318"/></marker></defs>
<rect x="5" y="5" width="250" height="210" rx="10" fill="#f1f5f9" stroke="#94a3b8" stroke-dasharray="6 4"/><text x="15" y="25" font-size="13" fill="#475569">Barrio</text>
<rect x="30" y="140" width="70" height="55" fill="#fde68a" stroke="#92400e"/><polygon points="25,140 65,110 105,140" fill="#b45309"/><text x="65" y="173" text-anchor="middle" font-size="14" font-weight="700">Casa</text>
<rect x="150" y="40" width="90" height="70" rx="8" fill="#bbf7d0" stroke="#166534"/><text x="195" y="80" text-anchor="middle" font-size="14" font-weight="700">Parque</text>
<circle cx="150" cy="110" r="13" fill="#b42318"/><text x="150" y="115" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">1</text>
<line x1="95" y1="140" x2="138" y2="118" stroke="#b42318" stroke-width="3" marker-end="url(#fl)"/>
<rect x="300" y="60" width="105" height="70" rx="6" fill="#dbeafe" stroke="#1e40af"/><text x="352" y="100" text-anchor="middle" font-size="14" font-weight="700">Escuela</text>
<circle cx="300" cy="130" r="13" fill="#b42318"/><text x="300" y="135" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">2</text>
<path d="M100,185 C200,215 260,190 288,138" fill="none" stroke="#b42318" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#fl)"/>
</svg>"""


def articulo_emergencia():
    t = lambda x: f'<p class="art-txt">{x}</p>'
    return f"""<article class="articulo vistazo" id="art-emerg">
<p class="art-tit">Prepárese para una emergencia en casa</p>
{t("Una tormenta de nieve, un apagón o una inundación pueden dejar a una familia varios días sin luz, sin agua o sin poder salir. Nadie puede evitar una emergencia, pero sí se puede estar preparado. Estos son los pasos más importantes.")}
<h5>¿Por qué prepararse?</h5>
{t("En una emergencia grande, los servicios de ayuda pueden tardar en llegar a todos los hogares. Por eso, los expertos recomiendan que cada familia pueda arreglárselas por su cuenta durante <strong>al menos tres días</strong>.")}
<h5>Arme un kit de emergencia</h5>
{t("Un <strong>kit de emergencia</strong> es una mochila o una caja con lo necesario para pasar unos días sin ayuda. Debe incluir:")}
<ul class="art-txt"><li>Agua: <strong>un galón por persona por día</strong>.</li><li>Comida enlatada y un abrelatas manual.</li><li>Una linterna y pilas de repuesto.</li><li>Un botiquín de primeros auxilios.</li>
<li>Las medicinas que toma cada miembro de la familia.</li><li>Copias de los documentos importantes en una bolsa de plástico.</li></ul>
<p class="graf-tit">Tabla 1. Agua necesaria para tres días</p>
{C.tabla("Tabla 1. Agua necesaria para tres días", ["Personas en la casa", "Galones de agua"], [["1", "3"], ["2", "6"], ["4", "12"]])}
<div class="caja caja-tip"><span class="etiqueta et-verde">¿Sabía que…?</span><p>Las mascotas también necesitan su propio kit: agua, comida para varios días, una correa y una copia de su registro de vacunas.</p></div>
<h5>Haga un plan familiar</h5>
{t("Siéntense en familia y decidan qué hará cada uno. Elijan un <strong>punto de encuentro</strong> cerca de la casa, por ejemplo la esquina de un parque, y otro fuera del barrio, por si no pueden volver. Anoten en un papel los teléfonos importantes: casi nadie los recuerda de memoria.")}
<figure><div class="art-fig">{MAPA}</div><figcaption>Figura 1. Un plan familiar marca dos puntos de encuentro: uno cerca de casa (1) y otro fuera del barrio (2).</figcaption></figure>
<h5>Manténgase informado</h5>
{t("Durante una emergencia, siga las noticias en la radio o en el teléfono. Muchas ciudades envían alertas al celular con instrucciones. Una <strong>radio de pilas</strong> funciona aunque no haya luz.")}
<h5>Glosario</h5>
<dl class="glosario-art"><dt>apagón:</dt><dd>falta de electricidad en una zona.</dd><dt>botiquín:</dt><dd>caja con lo necesario para curar heridas pequeñas.</dd><dt>punto de encuentro:</dt><dd>lugar donde la familia se reúne si se separa.</dd></dl>
</article>
{FUENTE}
<script>(function(){{var a=document.getElementById("art-emerg"),b=document.getElementById("btn-vistazo"),n=document.getElementById("nota-vistazo");
b.addEventListener("click",function(){{var v=a.classList.toggle("vistazo");b.textContent=v?"Mostrar el artículo completo":"Volver al modo vistazo";b.setAttribute("aria-pressed",v?"false":"true");n.hidden=!v;}});}})();</script>"""


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Un cuento se lee de principio a fin. Un texto informativo, no siempre: un folleto de la clínica, una página de un libro de ciencias o un artículo de internet están llenos de ayudas que el autor pone para que el lector encuentre lo que busca: títulos, subtítulos, palabras en negrita, imágenes, recuadros. Los buenos lectores las usan antes, durante y después de leer. En el GED, muchos textos de Ciencias y Estudios Sociales vienen con estas ayudas, y saber usarlas ahorra tiempo.</p>
{C.tabla("Características del texto informativo", ["Característica", "Para qué sirve"],
         [["Título", "Dice el tema del texto completo."], ["Subtítulos", "Dividen el texto en partes y dicen de qué trata cada una."], ["Negritas", "Destacan las palabras o ideas más importantes."],
          ["Imágenes y pies de foto", "Muestran lo que el texto explica; el pie, debajo, dice qué es la imagen."], ["Listas", "Ordenan pasos o elementos para leerlos rápido."],
          ["Recuadros", "Agregan información extra o curiosa, separada del texto principal."], ["Tablas y gráficas", "Organizan datos y números."], ["Glosario", "Explica las palabras difíciles, normalmente al final."]])}
{C.caja("tip", "Las ayudas son parte del texto", "<p>La información de un pie de foto, una tabla o un recuadro también cuenta. En los exámenes, muchas respuestas están justamente ahí.</p>")}
{P("Compruebe", "¿Dónde se explican las palabras difíciles de un texto?", ["En el glosario", "En el recuadro", "En el subtítulo"], 0, {1: "El recuadro trae información extra.", 2: "El subtítulo dice de qué trata una parte."}, "En el <strong>glosario</strong>.")}"""

    s2 = f"""<p>Antes de leer un texto informativo, dedique un minuto a darle un <strong>vistazo</strong>. No lee las oraciones: solo mira las ayudas.</p>
<ol><li>Lea el <strong>título</strong>: ¿cuál es el tema?</li><li>Lea los <strong>subtítulos</strong>: ¿en qué partes se divide?</li><li>Mire las <strong>imágenes, tablas y pies de foto</strong>.</li>
<li>Fíjese en las <strong>negritas</strong>.</li><li><strong>Prediga</strong>: ¿qué va a aprender? ¿Para qué cree que se escribió?</li></ol>
<p>Pruébelo: el artículo está en «modo vistazo». Las oraciones aparecen borrosas y solo se leen las ayudas. Mire solo lo que se ve y responda las preguntas antes de leerlo completo.</p>
<p><button type="button" class="btn" id="btn-vistazo" aria-pressed="false" aria-controls="art-emerg">Mostrar el artículo completo</button></p>
<p class="nota-vistazo" id="nota-vistazo">Modo vistazo: las oraciones están borrosas a propósito. Si usa un lector de pantalla, lea solo el título, los subtítulos y las palabras en negrita.</p>
{articulo_emergencia()}
{P("Vistazo 1", "Según el título, ¿cuál es el tema?", ["Cómo estar preparados para una emergencia en casa", "Cómo arreglar los aparatos que se dañan en casa", "Cómo comprar una casa en una ciudad grande"], 0, {1: "El título no habla de reparaciones.", 2: "El título no habla de comprar."}, "El título lo dice directamente.")}
{P("Vistazo 2", "Según los subtítulos, ¿qué partes tendrá el texto?", ["Los precios de los alimentos y dónde comprarlos", "Por qué prepararse, el kit, el plan familiar y cómo informarse", "La historia de las grandes tormentas del país"], 1, {0: "Ningún subtítulo habla de precios.", 2: "Ningún subtítulo habla de historia."}, "Cada subtítulo anuncia una parte.")}
{P("Vistazo 3", "Mirando la tabla y la figura, ¿qué cree que va a aprender?", ["Cuánta agua guardar y dónde reunirse con la familia", "Cómo se dibujan los mapas de las ciudades", "Cuánto cuesta el agua embotellada en la tienda"], 0, {1: "El mapa es un ejemplo, no una clase de dibujo.", 2: "La tabla no habla de precios."}, "La tabla habla de agua y la figura, de puntos de encuentro.")}
{P("Vistazo 4", "¿Cuál cree que es el propósito del autor?", ["Entretener con la historia de una familia", "Informar y dar consejos prácticos", "Persuadir al lector de vender su casa"], 1, {0: "No hay personajes ni historia.", 2: "No hay nada que vender."}, "Subtítulos con instrucciones (<em>arme, haga, manténgase</em>) y datos.")}
<p>Ahora pulse «Mostrar el artículo completo», léalo entero y compruebe si sus predicciones fueron correctas.</p>"""

    s3 = f"""<p>Cuando busca un dato concreto, no hace falta releer todo: los subtítulos le dicen en qué parte está. Lea la pregunta, piense qué palabra clave busca y vaya a la sección cuyo subtítulo se relaciona. Ahí, lea con atención.</p>
{P("¿Dónde buscar? 1", "¿Cuántos días debe poder arreglárselas sola una familia?", ["¿Por qué prepararse?", "Haga un plan familiar", "Manténgase informado"], 0, {1: "Esa sección habla de puntos de encuentro.", 2: "Esa sección habla de noticias y alertas."}, "Está en la primera sección: al menos tres días.")}
{P("¿Dónde buscar? 2", "¿Qué hay que llevar para curar una herida pequeña?", ["Manténgase informado", "Arme un kit de emergencia", "Haga un plan familiar"], 1, {0: "Esa sección habla de noticias.", 2: "Esa sección habla del plan."}, "El botiquín aparece en la lista del kit.")}
{P("¿Dónde buscar? 3", "¿Dónde debe reunirse la familia si se separa?", ["Arme un kit de emergencia", "¿Por qué prepararse?", "Haga un plan familiar"], 2, {0: "El kit no dice dónde reunirse.", 1: "Esa sección explica por qué."}, "El punto de encuentro está en el plan familiar.")}
<h3>Las imágenes y las tablas también dicen</h3>
<p>Una imagen no es decoración: se lee. Para leerla, pregúntese qué muestra, qué dice el pie de foto y qué agrega al texto. Una tabla se lee por filas y columnas: busque el título, los encabezados y el dato donde se cruzan.</p>
{P("Imagen y tabla 1", "Según la Tabla 1, ¿cuánta agua necesita una familia de cuatro personas para tres días?", ["4 galones", "12 galones", "3 galones"], 1, {0: "Ese es el número de personas.", 2: "Eso es lo que necesita una sola persona."}, "Fila de 4 personas, columna de galones: <strong>12</strong>.")}
{P("Imagen y tabla 2", "En la Figura 1, ¿dónde está el punto de encuentro número 1?", ["En la escuela, fuera del barrio", "Dentro de la casa de la familia", "En la esquina del parque, cerca de casa"], 2, {0: "Ese es el punto 2.", 1: "Los puntos de encuentro están fuera de la casa."}, "El círculo 1 está junto al parque.")}
{P("Imagen y tabla 3", "¿Dónde está la información sobre las mascotas?", ["En el glosario", "En un recuadro", "En el pie de la figura"], 1, {0: "El glosario explica palabras.", 2: "El pie habla de los puntos de encuentro."}, "En el recuadro <strong>«¿Sabía que…?»</strong>.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · un texto de su vida</span>
<p>Busque un texto informativo real: un folleto de la clínica, una página de un libro de ciencias de sus hijos, un artículo de una revista o una página web de su ciudad.</p>
<ol><li>Haga el vistazo previo y escriba su predicción en dos oraciones.</li><li>Haga una lista de todas las características que tiene (título, subtítulos, negritas…).</li>
<li>Lea el texto y escriba si su predicción fue correcta.</li><li>Escriba una pregunta sobre un dato del texto y anote en qué sección encontró la respuesta.</li></ol>
<p>Si tiene con quién practicar, con el libro de ciencias o de historia de un hijo o sobrino, hagan juntos el vistazo previo de un capítulo antes de que lo estudie. Es la misma estrategia para cualquier edad.</p></div>"""

    secciones = [("s1", "Las características del texto informativo", s1), ("s2", "Antes de leer: el vistazo previo", s2), ("s3", "Durante la lectura: subtítulos, imágenes y tablas", s3)]
    tarea = [("Mi kit.", "Con la información del artículo, escriba la lista del kit de emergencia de su casa: cuántas personas son, cuánta agua necesitan para tres días (use la tabla) y qué medicinas o documentos deben ir."),
             ("Mi plan.", "Dibuje en su cuaderno el mapa de su barrio con dos puntos de encuentro, como la Figura 1, y escríbale un pie de foto."),
             ("Un folleto.", "Escriba un folleto corto sobre un tema que conozca bien (su trabajo, una receta, su deporte favorito) con título, dos subtítulos, una lista, dos palabras en negrita y un recuadro de «¿Sabía que…?».")]
    PQ = ('<div class="texto-lectura"><p><strong>Cuide su espalda en el trabajo</strong><br><em>Subtítulos:</em> Cómo levantar cajas · Pausas para estirarse · Cuándo ir al médico<br>'
          '<em>Imagen:</em> una persona dobla las rodillas para levantar una caja. <em>Pie de foto:</em> «Doble las rodillas, no la espalda».</p></div>')
    quiz = [
        ("¿Para qué sirven los <strong>subtítulos</strong>?", ["Dividen el texto en partes y dicen de qué trata cada una", "Explican el significado de las palabras difíciles", "Dan los datos numéricos del texto"], 0, {1: "Eso hace el glosario.", 2: "Eso hacen las tablas."}, "Dividen el texto en <strong>partes</strong>."),
        ("El <strong>pie de foto</strong> es…", ["el texto que explica qué muestra una imagen", "la última página de un libro", "el título de una tabla de datos"], 0, {1: "No es una página.", 2: "La tabla tiene su propio título."}, "Explica la <strong>imagen</strong>."),
        ("Las <strong>negritas</strong> sirven para…", ["destacar las palabras o ideas más importantes", "indicar que el texto es una historia", "señalar las palabras mal escritas"], 0, {1: "No tienen que ver con el tipo de texto.", 2: "No marcan errores."}, "<strong>Destacar</strong> lo importante."),
        ("¿Qué hace en un <strong>vistazo previo</strong>?", ["Mira el título, los subtítulos, las imágenes y las negritas", "Lee todo el texto lo más rápido posible", "Lee solamente el último párrafo"], 0, {1: "En el vistazo no se leen las oraciones.", 2: "Se miran las ayudas de todo el texto."}, "Mira solo las <strong>ayudas</strong>."),
        (PQ + "¿Cuál es el tema del texto?", ["El cuidado de la espalda en el trabajo", "Cómo encontrar un buen médico", "Los distintos tipos de cajas"], 0, {1: "Es solo una parte.", 2: "Las cajas son un ejemplo."}, "Lo dice el <strong>título</strong>."),
        (PQ + "¿En qué sección buscaría cómo levantar algo pesado?", ["Cómo levantar cajas", "Pausas para estirarse", "Cuándo ir al médico"], 0, {1: "Esa sección habla de estiramientos.", 2: "Esa sección habla de cuándo consultar."}, "«<strong>Cómo levantar cajas</strong>»."),
        (PQ + "Según el pie de foto, ¿qué consejo da la imagen?", ["Doblar las rodillas, no la espalda", "Levantar la caja con un solo brazo", "Pedir ayuda siempre al supervisor"], 0, {1: "El pie no dice eso.", 2: "El pie no dice eso."}, "<strong>Doblar las rodillas.</strong>"),
        ("Un recuadro con el título «¿Sabía que…?» suele traer…", ["información extra o curiosa sobre el tema", "la idea principal de todo el texto", "el nombre del autor del texto"], 0, {1: "La idea principal no va aparte.", 2: "No es para eso."}, "Información <strong>extra</strong>."),
        ("En una tabla, el dato que busca está…", ["donde se cruzan la fila y la columna correctas", "siempre en la primera fila", "en el título de la tabla"], 0, {1: "Depende de lo que busque.", 2: "El título dice de qué trata."}, "Donde se <strong>cruzan</strong> fila y columna."),
        ("Si busca un solo dato en un texto largo con subtítulos, conviene…", ["ir a la sección cuyo subtítulo se relaciona con la pregunta", "leer todo el texto de nuevo desde el principio", "mirar solamente las imágenes del texto"], 0, {1: "Se pierde tiempo.", 2: "El dato puede estar en el texto."}, "Usar los <strong>subtítulos</strong>."),
    ]
    filas = [
        ("Características", "Reconozco título, subtítulos, negritas, pies de foto, listas, recuadros, tablas y glosario.", "Reconozco las más comunes.", "No sé para qué sirven (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Vistazo previo", "Antes de leer, miro las ayudas y hago una predicción.", "A veces empiezo a leer sin mirar.", "Nunca miro las ayudas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Buscar datos", "Uso los subtítulos para buscar y leo imágenes y tablas.", "Encuentro el dato, pero releo todo.", "No sé dónde buscar (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 4. Ya lee textos de varios párrafos con método. En el Tema 5 conocerá los <strong>tiempos verbales</strong> y cómo cambian el sentido de un texto.</p>"
    glosario = [("Vistazo previo", "Mirada rápida a las ayudas de un texto antes de leerlo."), ("Pie de foto", "Texto breve debajo de una imagen que explica lo que muestra."),
                ("Recuadro", "Cuadro aparte con información extra."), ("Glosario", "Lista de palabras difíciles con su significado.")]
    conexion = ("<p>En el Nivel 1 leyó escenas, artículos, mapas y gráficas. Ahora usará todas esas ayudas juntas para leer más rápido y encontrar los datos en un texto informativo largo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, un folleto o una página de un libro de ciencias.</p>")
    estd = LE.estandares(["R.5.4", "R.2.1"], base=["R.5.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Las ayudas que el autor pone para el lector.", ["Lectura", "Texto informativo"],
                            ["<strong>Reconocer</strong> las características del texto informativo.", "<strong>Hacer</strong> un vistazo previo y una predicción.",
                             "<strong>Usar</strong> los subtítulos para buscar información.", "<strong>Leer</strong> imágenes, pies de foto y tablas."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-1", LE.titulo("5-1")), glosario, P)


def ficha(i, pie=True):
    t, s, pf = TX[i]
    return (f'<article class="articulo ficha"><p class="art-tit">{t}</p>' + "".join(f"<h5>{x}</h5>" for x in s) +
            (f'<p class="art-sub">Pie de foto: «{pf}»</p>' if pie else "") + "</article>")


def practica():
    pr = [{"enun": ficha(i) + "<p><strong>¿De qué tratará el texto?</strong></p>", "ops": ops, "ok": 0, "pista": "Vuelva a leer el título y los tres subtítulos: la respuesta debe abarcarlos todos.", "exp": e} for i, ops, e in PRED]
    su = [{"enun": ficha(i, False) + f"<p><strong>{q}</strong><br>¿En qué sección buscaría?</p>", "ops": TX[i][1], "ok": k, "enOrden": True,
           "pista": "¿Qué palabra clave tiene la pregunta? Busque el subtítulo que se relaciona con ella.", "exp": f"La respuesta está en «{TX[i][1][k]}»."} for i, q, k in SECC]
    im = [{"enun": f'<div class="texto-lectura"><p><strong>Imagen:</strong> {d}<br><strong>Pie de foto:</strong> «{pf}»</p></div><strong>¿Qué parte del texto acompaña esta imagen?</strong>', "ops": ops, "ok": k,
           "pista": "Fíjese en las palabras clave del pie de foto y búsquelas entre las opciones.", "exp": "La imagen y su pie muestran lo que explica ese párrafo."} for d, pf, ops, k in IMG]
    ca = []
    for d, k in QUE_ES:
        r = random.Random(d); otras = [c for j, c in enumerate(CARACT) if j != k]; r.shuffle(otras)
        ca.append({"enun": f"<span class=\"grande\">{d}</span><br><strong>¿Qué característica es?</strong>", "ops": [CARACT[k]] + otras[:3], "ok": 0,
                   "pista": "Piense dónde aparece y para qué sirve.", "exp": f"<strong>{CARACT[k]}</strong>."})
    mods = [("prediccion", "Prediga con el vistazo", C.om("m1", "Mire solo el título, los subtítulos y el pie de foto. ¿De qué tratará el texto?")),
            ("subtitulos", "¿En qué sección buscaría?", C.om("m2", "Lea la pregunta y elija el subtítulo de la sección donde está la respuesta.")),
            ("imagenes", "Imágenes y pies de foto", C.om("m3", "Lea la descripción de la imagen y su pie de foto, y decida qué parte del texto ilustra.")),
            ("caracteristicas", "¿Qué característica es?", C.om("m4", "Reconozca cada ayuda del texto por lo que hace."))]
    js = (C.js_datos("PR", pr) + C.js_datos("SU", su) + C.js_datos("IM", im) + C.js_datos("CA", ca) +
          'creaBanco("m1", PR);\ncreaBanco("m2", SU);\ncreaBanco("m3", IM);\ncreaBanco("m4", CA);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
