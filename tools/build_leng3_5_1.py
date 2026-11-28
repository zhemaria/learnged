# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 5.1 · Razones y evidencias del autor.
Fuente: clases_leng3/clase_5-1.html (GEDparaHispanos) y gramatica/n3-l5-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_5_1.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_3_1 import texto

LE.nivel(3)
N = "5-1"
PT = ["Afirmación", "Razón", "Evidencia"]
AP = ["La apoya", "No la apoya"]


def A(t, k):
    return f'<span class="a-{k}">{t}</span>'


CARTA = [f"{A('La biblioteca del barrio debería abrir los domingos.', 'af')} Hoy cierra a las cinco de la tarde entre semana y no abre el fin de semana, justo cuando más la necesitamos.",
         f"{A('Muchos vecinos solo tienen libre el domingo.', 'ra')} {A('En la encuesta que hizo la asociación de vecinos este verano, 7 de cada 10 de las 300 personas que respondieron dijeron que trabajan los sábados.', 'ev')} Para ellos, la biblioteca no existe.",
         f"{A('Además, los niños necesitan un lugar para hacer la tarea con internet.', 'ra')} {A('La maestra Elena Ríos, de la escuela primaria de la calle 31, contó en la última reunión de padres que uno de cada tres alumnos de su grupo no tiene internet en casa.', 'ev')} {A('Mi propio vecino, Tomás, hace las tareas en el estacionamiento de una cafetería, usando su wifi desde afuera.', 'ev')}",
         f"{A('Abrir un día más no costaría casi nada.', 'ra')} {A('Estoy segura de que la ciudad tiene el dinero; solo falta voluntad.', 'sa')}",
         f"{A('Y, por último, todo el mundo sabe que leer nos hace mejores personas.', 'sa')}",
         f"{A('Pido a la concejala del distrito que proponga abrir la biblioteca los domingos, al menos de diez de la mañana a cuatro de la tarde.', 'af')} — Marisol Díaz, vecina del barrio"]
PA = [("un argumento sobre el transporte", "La ciudad debería poner un autobús nocturno en la avenida Pulaski.", 0, "Es lo que el autor quiere que aceptemos."),
      ("un argumento sobre el transporte", "Muchas personas del barrio trabajan en turnos de noche.", 1, "Explica por qué hace falta el autobús."),
      ("un argumento sobre el transporte", "Según la cámara de comercio, cuatro fábricas de la zona tienen turnos que terminan a medianoche.", 2, "Es un dato con su fuente que prueba la razón."),
      ("un argumento sobre la escuela", "Las escuelas deberían empezar las clases más tarde.", 0, "Es la idea que se defiende."),
      ("un argumento sobre la escuela", "Los adolescentes rinden más cuando duermen lo suficiente.", 1, "Explica por qué conviene empezar más tarde."),
      ("un argumento sobre la escuela", "En un distrito que retrasó el horario una hora, las faltas a clase bajaron una cuarta parte.", 2, "Es un ejemplo con resultados medibles."),
      ("un argumento sobre la salud", "Hay que poner una clínica gratuita en el barrio.", 0, "Es lo que se pide."),
      ("un argumento sobre la salud", "Muchas familias no tienen seguro médico.", 1, "Explica por qué hace falta la clínica."),
      ("un argumento sobre la salud", "La enfermera de la escuela dice que atiende a diez niños por semana que no han visto a un médico en años.", 2, "Es el testimonio de alguien que conoce el problema."),
      ("un argumento sobre el medio ambiente", "El supermercado debería dejar de dar bolsas de plástico.", 0, "Es la idea que se defiende."),
      ("un argumento sobre el medio ambiente", "Las bolsas de plástico tardan muchísimo en deshacerse.", 1, "Explica por qué conviene dejarlas."),
      ("un argumento sobre el medio ambiente", "En la limpieza del parque del mes pasado, los voluntarios recogieron más de mil bolsas.", 2, "Es un dato que prueba el problema."),
      ("un argumento sobre el trabajo", "La fábrica debería ofrecer clases de inglés a sus empleados.", 0, "Es lo que se propone."),
      ("un argumento sobre el trabajo", "Los empleados que hablan inglés pueden recibir mejores puestos.", 1, "Explica por qué serían útiles las clases.")]
APX = [("Hay que arreglar los baches de la calle 18.", "El taller de la esquina dice que este mes reparó doce llantas dañadas en esa calle.", 0, "Es pertinente y viene de quien lo sabe."),
       ("Hay que arreglar los baches de la calle 18.", "La calle 18 tiene muchos restaurantes famosos.", 1, "Habla de la calle, pero no de los baches."),
       ("El gimnasio de la escuela debe abrir por las tardes.", "Hoy no hay ningún otro lugar techado en el barrio donde los jóvenes puedan hacer deporte en invierno.", 0, "Muestra la necesidad que el gimnasio cubriría."),
       ("El gimnasio de la escuela debe abrir por las tardes.", "A mi sobrino le encanta el baloncesto.", 1, "Es un caso personal que no muestra una necesidad del barrio."),
       ("La ciudad debe plantar más árboles en las calles.", "Un estudio de la universidad encontró que las calles con árboles son varios grados más frescas en verano.", 0, "Un estudio pertinente y confiable."),
       ("La ciudad debe plantar más árboles en las calles.", "Todo el mundo sabe que los árboles son bonitos.", 1, "«Todo el mundo sabe» no es evidencia, y lo bonito no es la razón."),
       ("El curso de computación debería ser gratuito.", "En la encuesta del centro, la mitad de los alumnos dijo que no se inscribe porque no puede pagarlo.", 0, "Muestra que el precio impide inscribirse."),
       ("El curso de computación debería ser gratuito.", "Las computadoras son cada vez más rápidas.", 1, "No tiene relación con que el curso sea gratuito."),
       ("Hace falta un semáforo frente a la escuela.", "La policía registró cuatro atropellos de peatones en ese cruce en los últimos dos años.", 0, "Un dato pertinente de una fuente confiable."),
       ("Hace falta un semáforo frente a la escuela.", "Estoy seguro de que un semáforo lo arreglaría todo.", 1, "La seguridad del autor no es evidencia."),
       ("La clínica debería atender también los sábados.", "La recepcionista dice que la lista de espera para citas entre semana es de tres semanas.", 0, "Muestra que la clínica no alcanza."),
       ("La clínica debería atender también los sábados.", "La clínica se inauguró hace diez años.", 1, "Es un dato cierto, pero no apoya la afirmación.")]
SA = [("La escuela debería tener un huerto. Primero, los niños aprenderían ciencias: la maestra de la escuela vecina, que ya tiene uno, dice que sus alumnos mejoraron en ciencias. Segundo, comerían mejor: en esa misma escuela, la cafetería usa las verduras del huerto. Y tercero, es obvio que a todos los niños les gustan las plantas.",
       ["A todos los niños les gustan las plantas.", "Los niños aprenderían ciencias.", "Los niños comerían mejor."], "«Es obvio» y «a todos» sin ninguna evidencia."),
      ("El barrio necesita una parada de autobús en la calle 47. Los ancianos del asilo caminan más de un kilómetro para llegar a la parada más cercana, según el mapa de la CTA. Además, una parada nueva atraería muchos negocios, estoy seguro.",
       ["Una parada atraería muchos negocios.", "Los ancianos caminan más de un kilómetro.", "La parada más cercana está lejos del asilo."], "Solo dice «estoy seguro», sin datos."),
      ("La biblioteca debería prestar herramientas, no solo libros. Muchas familias no pueden comprar un taladro para usarlo una sola vez. En otras ciudades, algunas bibliotecas públicas ya prestan herramientas desde hace años. Y seguro que nadie las devolvería rotas.",
       ["Nadie devolvería las herramientas rotas.", "Muchas familias no pueden comprar herramientas.", "En otras ciudades ya funciona algo así."], "Es una suposición sin ninguna prueba."),
      ("Las tiendas del barrio deberían tener letreros en español. Según la asociación de vecinos, la mitad de los vecinos habla español en casa y muchos clientes mayores no leen bien el inglés. Además, todo el mundo prefiere comprar donde le hablan en su idioma.",
       ["Todo el mundo prefiere comprar en su idioma.", "La mitad de los vecinos habla español en casa.", "Muchos clientes mayores no leen bien el inglés."], "«Todo el mundo» sin evidencia; las otras dos razones tienen fuente."),
      ("El centro comunitario debería abrir una guardería. Muchas madres no pueden estudiar porque no tienen con quién dejar a sus hijos: lo dijeron 40 de las 60 alumnas del curso de inglés. Es evidente que una guardería resolvería todos los problemas del barrio.",
       ["La guardería resolvería todos los problemas del barrio.", "Muchas madres no tienen con quién dejar a sus hijos.", "Las madres no pueden estudiar por falta de cuidado infantil."], "Exagera («todos los problemas») y no da evidencia."),
      ("La ciudad debe limpiar el lote abandonado de la calle Archer. Los vecinos han visto ratas allí, y el departamento de salud recibió doce quejas este año. Seguramente el lote vale millones de dólares.",
       ["El lote vale millones de dólares.", "Los vecinos han visto ratas en el lote.", "Hubo doce quejas al departamento de salud."], "Es una suposición sin datos, y además no apoya la afirmación.")]
NOTA = '<p class="fuente">Argumentos creados para practicar; las personas y los datos son de ejemplo.</p>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Un vendedor le dice: «Este carro es el mejor que puede comprar». Antes de firmar, usted preguntaría: ¿por qué?, ¿cómo lo sabe? Si le responde «porque gasta poca gasolina, y aquí está la prueba oficial de consumo», tiene una razón con su evidencia. Si le responde «porque todo el mundo lo dice», no tiene nada. Leer un argumento es hacer esas mismas preguntas al autor.</p>
{C.tabla("Las tres partes de un argumento", ["Parte", "Qué es", "Pregunta que responde", "Ejemplo"],
         [["Afirmación", "La idea que el autor quiere que usted acepte. Se puede discutir.", "¿Qué piensa el autor?", "La ciudad debe poner más paradas de autobús en el barrio."],
          ["Razón", "Por qué el autor piensa eso.", "¿Por qué?", "Muchos vecinos caminan más de un kilómetro para llegar a una parada."],
          ["Evidencia", "Los hechos que prueban la razón.", "¿Cómo lo sabe?", "Un mapa del transporte público muestra que la parada más cercana está a más de un kilómetro de la escuela."]])}
{C.caja("tip", "Afirmación no es hecho", "<p>«El autobús 9 pasa por la calle Ashland» es un hecho: se comprueba. «Debería pasar más seguido» es una afirmación: se puede estar de acuerdo o no. Por eso necesita razones y evidencias.</p>")}
{C.caja("tip", "Dónde suele estar la afirmación", "<p>Al principio o al final del texto, y a veces en el título. Palabras como <em>debe, debería, es necesario, hay que, es mejor</em> suelen anunciarla.</p>")}
{P("Partes 1", "¿Cuál es una afirmación (y no un hecho)?", ["El autobús cuesta dos dólares con veinticinco.", "La ciudad debería bajar las tarifas del autobús.", "El autobús pasa cada quince minutos."], 1, {0: "Se puede comprobar: es un hecho.", 2: "Se puede comprobar: es un hecho."}, "Se puede discutir: es una <strong>afirmación</strong>.")}"""

    s2 = f"""{C.tabla("Tipos de evidencia con su fuerza y su límite", ["Tipo", "Ejemplo", "Su fuerza", "Su límite"],
         [["Datos y cifras", "«El 40 % de los accidentes ocurre en esa esquina.»", "Es medible y se puede comprobar.", "Hay que saber de dónde salen."],
          ["Ejemplos", "«En una ciudad vecina pusieron semáforos y bajaron los accidentes.»", "Muestra que algo funciona en un caso real.", "Un caso no prueba que funcione siempre."],
          ["Testimonio de un experto", "«Según la ingeniera de tránsito de la ciudad…»", "Viene de alguien que sabe del tema.", "Hay que ver si el experto es del tema."],
          ["Experiencia personal", "«Mi hijo casi fue atropellado ahí.»", "Conmueve y acerca el problema.", "Es un solo caso; por sí sola no basta."]])}
{C.caja("tip", "La mejor evidencia combina", "<p>Un dato muestra el tamaño del problema y una experiencia le pone cara. Un buen argumento usa varios tipos de evidencia.</p>")}
{P("Tipos 1", "«La doctora Pérez, cardióloga del hospital del condado, recomienda caminar a diario.» ¿Qué tipo de evidencia es?", ["Experiencia personal", "Un dato de una encuesta", "Testimonio de un experto"], 2, {0: "No cuenta algo que le pasó a ella.", 1: "No hay cifras."}, "Habla una especialista: <strong>testimonio de un experto</strong>.")}"""

    s3 = f"""<p>Para evaluar un argumento, pase cada evidencia por tres preguntas:</p>
<ol class="proceso"><li><strong>¿Es pertinente?</strong> ¿Habla directamente de la razón, o solo del mismo tema?</li><li><strong>¿Es suficiente?</strong> ¿Basta para convencer, o es un solo caso?</li><li><strong>¿Es confiable?</strong> ¿Se sabe de dónde viene?</li></ol>
<p>Y busque las <strong>razones sin apoyo</strong>: las que el autor da sin ninguna evidencia. Suelen aparecer con frases como estas:</p>
{C.tabla("Frases que suelen acompañar a una razón sin apoyo", ["Frase", "Por qué no basta"],
         [["«Todo el mundo sabe que…»", "Que mucha gente lo crea no lo prueba."], ["«Estoy seguro de que…»", "La seguridad del autor no es una evidencia."],
          ["«Es obvio que…»", "Si fuera obvio, no haría falta decirlo; y no se demuestra."], ["«Siempre» / «nunca» / «todos»", "Una generalización necesita mucha evidencia."]])}
{C.caja("tip", "Un paso hacia el Nivel 4", "<p>Aquí aprende a ver si hay evidencia y si es pertinente. En el Nivel 4 profundizará en la validez del razonamiento y en los errores de lógica que usan algunos argumentos.</p>")}
{P("Apoya 1", "Afirmación: <em>El parque necesita más luces.</em> Evidencia: «El parque tiene árboles muy bonitos.»", AP, 1, {0: "¿Habla de la luz o de la seguridad?"}, "<strong>No la apoya</strong>: habla del parque, pero no es pertinente.")}
{P("Apoya 2", "Afirmación: <em>El parque necesita más luces.</em> Evidencia: «Este año hubo cinco robos de noche en el parque, según la policía.»", AP, 0, {1: "Es pertinente y tiene una fuente."}, "<strong>La apoya</strong>: es pertinente y de una fuente confiable.")}
{P("Apoya 3", "Afirmación: <em>La escuela debe ofrecer clases de inglés por la noche.</em> Evidencia: «Es obvio que todos quieren aprender inglés.»", AP, 1, {0: "«Es obvio» y «todos» no son evidencia."}, "<strong>No la apoya</strong>: «es obvio» y «todos» no prueban nada.")}"""

    carta = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(CARTA, 1))
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in CARTA)
    s4 = f"""<p>Una vecina escribió esta carta al periódico del barrio. Léala y, en su cuaderno, separe la afirmación, las razones y las evidencias. ¿Hay alguna razón sin apoyo? Después pulse <strong>Mostrar las partes</strong>.</p>
<p>{LE.escuchar(plano, "Escuchar la carta")} <button type="button" class="btn-sec" id="btn-a51" aria-pressed="false">Mostrar las partes</button></p>
<div class="articulo lectura-arg" id="carta-51"><p><strong>Carta al editor · Que la biblioteca abra los domingos</strong></p>{carta}</div>
<p class="leyenda-partes" id="ley-51"><span style="background:#dbeafe">Afirmación</span><span style="background:#dcfce7">Razón</span><span style="background:#fef3c7">Evidencia</span><span style="background:#fee2e2">Sin apoyo</span></p>
<p class="fuente">La carta, sus personas y sus datos son inventados, para practicar.</p>
<script>(function(){{var b=document.getElementById("btn-a51"),t=document.getElementById("carta-51"),l=document.getElementById("ley-51");b.addEventListener("click",function(){{var on=t.classList.toggle("arg-on");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las partes":"Mostrar las partes";}});}})();</script>
<h3>Evalúe el argumento</h3>
{P("Carta 1", "¿Cuál es la afirmación de la carta?", ["Muchos vecinos del barrio trabajan los sábados.", "La biblioteca del barrio debería abrir los domingos.", "La maestra dijo que en su grupo faltan computadoras."], 1, {0: "Es una evidencia.", 2: "Es una evidencia, y además no dice eso."}, "Es la idea que Marisol quiere que aceptemos; está al principio y se repite al final.")}
{P("Carta 2", "«7 de cada 10 de las 300 personas trabajan los sábados.» ¿Qué tipo de evidencia es?", ["Una experiencia personal", "El testimonio de un experto", "Un dato de una encuesta"], 2, {0: "No le pasó a ella.", 1: "No habla un experto."}, "Es una cifra que sale de una encuesta: un dato.")}
{P("Carta 3", "¿Qué razón <strong>no</strong> tiene evidencia?", ["Muchos vecinos solo tienen libre el domingo.", "Abrir un día más no costaría casi nada.", "Los niños necesitan internet para la tarea."], 1, {0: "La apoya la encuesta.", 2: "La apoyan la maestra y Tomás."}, "Solo dice «estoy segura»; no da ningún dato del costo.")}
{P("Carta 4", "¿Por qué «todo el mundo sabe que leer nos hace mejores personas» no convence como razón?", ["Porque la lectura no es buena para nadie", "Que mucha gente lo crea no lo demuestra", "Porque está al final de la carta"], 1, {0: "No se discute si leer es bueno, sino si está probado.", 2: "El lugar no importa."}, "Es una generalización sin evidencia, aunque mucha gente esté de acuerdo.")}
{P("Carta 5", "El caso de Tomás, ¿basta por sí solo para probar la razón?", ["Sí: un solo caso prueba lo que pasa en todo el barrio", "No: porque no es el caso real de un vecino", "No: es un solo caso; ayuda junto con el dato de la maestra"], 2, {0: "Un caso no basta.", 1: "Sí es un vecino; el problema es que es uno solo."}, "Una experiencia personal conmueve, pero necesita otra evidencia que muestre que no es un caso aislado.")}"""

    s5 = f"""<p>Un <strong>esquema del argumento</strong> pone cada parte en su lugar. Así queda el de la carta de Marisol:</p>
<div class="esquema"><p class="esq-a"><strong>Afirmación:</strong> la biblioteca debería abrir los domingos.</p>
<p class="esq-r"><strong>Razón 1:</strong> muchos vecinos solo tienen libre el domingo. → <em>Evidencia:</em> encuesta de 300 vecinos (7 de cada 10 trabajan el sábado).</p>
<p class="esq-r"><strong>Razón 2:</strong> los niños necesitan internet para la tarea. → <em>Evidencia:</em> testimonio de la maestra (uno de cada tres sin internet) y el caso de Tomás.</p>
<p class="esq-r"><strong>Razón 3:</strong> no costaría casi nada. → <em>Sin evidencia:</em> solo «estoy segura».</p>
<p class="esq-r"><strong>Razón 4:</strong> leer nos hace mejores personas. → <em>Sin evidencia:</em> «todo el mundo sabe».</p></div>
{P("Esquema", "¿Qué haría más fuerte la razón «abrir un día más no costaría casi nada»?", ["Repetir la frase con más seguridad", "Un dato del costo real de abrir un día más", "Decir que todos los vecinos están de acuerdo"], 1, {0: "La seguridad no es evidencia.", 2: "Eso es otra generalización."}, "Un <strong>dato</strong> del costo la convertiría en una razón con evidencia.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Vean juntos un anuncio de la televisión. ¿Qué afirma? ¿Qué razones da? ¿Hay alguna evidencia de verdad, o solo frases como «el mejor» y «el favorito de todos»?</p>")}"""

    secciones = [("s1", "Las tres partes de un argumento", s1), ("s2", "Tipos de evidencia", s2), ("s3", "¿La evidencia apoya la afirmación?", s3),
                 ("s4", "Lectura: «Que la biblioteca abra los domingos»", s4), ("s5", "El esquema del argumento", s5)]
    tarea = [("Mejore la carta.", "Las razones 3 y 4 de Marisol no tienen evidencia. Escriba qué evidencia podría buscar para apoyarlas (por ejemplo, qué dato o qué testimonio). "
              "<details class=\"transc\"><summary>Ver ideas</summary><p>Para la razón 3, Marisol podría citar el presupuesto de la biblioteca o el costo de los sueldos de un día, o el ejemplo de otra biblioteca de la ciudad que ya abre los domingos. Para la razón 4, podría citar un estudio sobre los beneficios de la lectura, o cambiar la razón por una más concreta y fácil de probar.</p></details>"),
             ("Su esquema.", "Busque una carta al editor o un artículo de opinión en un periódico en español. Haga su esquema: afirmación, razones y evidencias. Marque las razones sin apoyo."),
             ("Su argumento.", "Escriba una afirmación sobre algo de su barrio y dos razones, cada una con un tipo de evidencia distinto.")]
    quiz = [
        ("¿Qué es la <strong>afirmación</strong> de un argumento?", ["La idea que el autor quiere que usted acepte", "Un dato del texto que se puede comprobar", "La última oración que aparece en el texto"], 0, {1: "Eso es un hecho.", 2: "No siempre está al final."}, "La idea que el autor quiere que <strong>acepte</strong>."),
        ("¿A qué pregunta responde la evidencia?", ["¿Cómo lo sabe?", "¿Qué piensa el autor?", "¿Quién escribió el texto?"], 0, {1: "Esa es la afirmación.", 2: "No."}, "<strong>¿Cómo lo sabe?</strong>"),
        ("¿Cuál es el límite de una experiencia personal como evidencia?", ["Es un solo caso y por sí sola no basta", "Nunca es verdad lo que cuenta una persona", "Siempre es más débil que una opinión"], 0, {1: "Puede ser verdad.", 2: "No."}, "Es <strong>un solo caso</strong>."),
        ("Una evidencia es <strong>pertinente</strong> cuando…", ["habla directamente de la razón que apoya", "es muy larga y tiene muchas cifras", "la dice una persona famosa del barrio"], 0, {1: "El largo no la hace pertinente.", 2: "La fama no la hace pertinente."}, "Habla <strong>directamente</strong> de la razón."),
        ("¿Qué frase suele acompañar a una razón sin apoyo?", ["«Todo el mundo sabe que…»", "«Según el censo de 2020…»", "«En la encuesta de la escuela…»"], 0, {1: "Da una fuente.", 2: "Da una fuente."}, "<strong>«Todo el mundo sabe que…»</strong>"),
        ("Afirmación: «Hay que poner un semáforo en la esquina.» ¿Qué evidencia la apoya mejor?", ["Hubo seis accidentes ahí este año, según la policía.", "La esquina queda cerca de una panadería.", "Mucha gente piensa que los semáforos son útiles."], 0, {1: "No es pertinente.", 2: "Es una opinión general."}, "Un <strong>dato pertinente</strong> con su fuente."),
        ("¿Por qué un buen argumento usa varios tipos de evidencia?", ["Porque cada tipo tiene una fuerza y un límite distintos", "Porque así el texto queda más largo y se ve mejor", "Porque usar un solo tipo de evidencia está prohibido"], 0, {1: "No es por el largo.", 2: "No está prohibido."}, "Cada tipo tiene su <strong>fuerza</strong> y su <strong>límite</strong>."),
        ("«Las bolsas de plástico tardan muchísimo en deshacerse.» En un argumento contra las bolsas, esta oración es…", ["una razón", "la afirmación", "una evidencia con fuente"], 0, {1: "No es lo que se pide.", 2: "No da un dato ni una fuente."}, "Una <strong>razón</strong>: explica por qué."),
        ("¿Qué palabras suelen anunciar una afirmación?", ["debe, debería, hay que", "según, de acuerdo con", "primero, luego, después"], 0, {1: "Anuncian una fuente.", 2: "Anuncian una secuencia."}, "<strong>Debe, debería, hay que.</strong>"),
        ("Para evaluar una evidencia, ¿qué tres preguntas conviene hacer?", ["¿Es pertinente, suficiente y confiable?", "¿Es larga, bonita y fácil de leer?", "¿Es nueva, famosa y divertida?"], 0, {1: "No.", 2: "No."}, "<strong>Pertinente, suficiente y confiable.</strong>"),
    ]
    filas = [
        ("Partes del argumento", "Separo la afirmación, las razones y las evidencias.", "Confundo a veces la razón con la evidencia.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Tipos de evidencia", "Reconozco cuatro tipos y sus límites.", "Conozco algunos.", "Me cuesta (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Evaluar", "Encuentro las razones sin apoyo y la evidencia que no es pertinente.", "Las encuentro a veces.", "No las veo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya separa la afirmación, las razones y las evidencias, y ve cuándo una razón no tiene apoyo. En la próxima lección aprenderá a <strong>integrar información de dos textos</strong>.</p>"
    glosario = [("Afirmación", "La idea que el autor quiere que el lector acepte; se puede discutir."), ("Razón", "Por qué el autor piensa lo que afirma."),
                ("Evidencia", "Los hechos que prueban una razón: datos, ejemplos, testimonios o experiencias."), ("Pertinente", "Que habla directamente de lo que se quiere probar.")]
    conexion = ("<p>En la Lección 7.1 del Nivel 2 escribió un texto de opinión con razones. Hoy lee argumentos de otros con ojo crítico: ¿qué afirman y cómo lo prueban?</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, para la tarea, una carta al editor o un artículo de opinión.</p>")
    estd = LE.estandares(["R.6.3", "R.6.4"], base=["R.6.1", "W.1"])
    return C.pagina_leccion(N, LE.titulo(N), "¿Qué afirma el autor y cómo lo prueba?", ["Argumentos", "Evidencia"],
                            ["<strong>Separar</strong> la afirmación, las razones y las evidencias.", "<strong>Reconocer</strong> cuatro tipos de evidencia y sus límites.",
                             "<strong>Evaluar</strong> si una evidencia es pertinente, suficiente y confiable.", "<strong>Encontrar</strong> las razones sin apoyo."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-2", LE.titulo("5-2")), glosario, P)


def practica():
    pa = [{"enun": f'<p>De {t}:</p><p class="frase">{o}</p><p>¿Qué parte del argumento es?</p>', "ops": PT, "ok": k, "enOrden": True,
           "pista": "¿Es lo que el autor quiere que acepte, por qué lo piensa o cómo lo prueba?", "exp": f"<strong>{PT[k]}.</strong> {n}"} for t, o, k, n in PA]
    ap = [{"enun": f'<p class="rel">Afirmación: <em>{a}</em></p><p class="frase">Evidencia: «{e}»</p>', "ops": AP, "ok": k, "enOrden": True,
           "pista": "¿La evidencia habla directamente de lo que se afirma? ¿Es un dato, o solo una opinión o un caso suelto?", "exp": f"<strong>{AP[k]}.</strong> {n}"} for a, e, k, n in APX]
    sa = [{"enun": texto([t]) + "<p><strong>¿Qué razón <u>no</u> tiene evidencia?</strong></p>", "ops": o, "ok": 0,
           "pista": "Esa razón sí tiene apoyo en el texto. Busque la que solo se apoya en «es obvio», «estoy seguro» o «todo el mundo».", "exp": n} for t, o, n in SA]
    mods = [("partes", "Afirmación, razón o evidencia", C.om("m1", "Decida qué parte del argumento es cada oración.") + NOTA),
            ("apoya", "¿La evidencia apoya la afirmación?", C.om("m2", "Decida si la evidencia apoya la afirmación.")),
            ("sin-apoyo", "La razón sin apoyo", C.om("m3", "Lea el argumento y encuentre la razón que no tiene evidencia."))]
    js = C.js_datos("PA", pa) + C.js_datos("AP", ap) + C.js_datos("SA", sa) + 'creaBanco("m1", PA);\ncreaBanco("m2", AP);\ncreaBanco("m3", SA);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
