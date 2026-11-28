# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 7.2 · Texto informativo: categorías, datos y conclusión.
Fuente: clases_leng2/clase_7-2.html (GEDparaHispanos) y gramatica/n2-l7-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_7_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng2_7_1 import taller

LE.nivel(2)
N = "7-2"
TEMAS = {"agua": ("El ciclo del agua", ["Evaporación", "Condensación", "Precipitación"]), "gob": ("Los tres poderes del gobierno", ["Legislativo", "Ejecutivo", "Judicial"]),
         "salud": ("Una vida saludable", ["Alimentación", "Ejercicio", "Descanso"]), "seres": ("Los seres vivos", ["Plantas", "Animales", "Hongos"]),
         "colon": ("La vida en las trece colonias", ["Trabajo", "Religión", "Gobierno"])}
CAT = [("agua", "El calor del sol convierte el agua de los lagos en vapor.", 0, "Líquido que pasa a vapor: evaporación."), ("agua", "El vapor se enfría en el aire y forma las nubes.", 1, "Vapor que se vuelve gotas: condensación."),
       ("agua", "El agua cae de las nubes en forma de lluvia, nieve o granizo.", 2, "La caída del agua: precipitación."), ("agua", "En los días calurosos, los charcos desaparecen rápidamente.", 0, "El agua se evapora con el calor."),
       ("gob", "El Senado tiene dos senadores por cada estado.", 0, "El Senado es parte del Congreso."), ("gob", "El presidente puede firmar o vetar una ley.", 1, "Lo hace el poder ejecutivo."),
       ("gob", "Los jueces de la Corte Suprema tienen cargos vitalicios, es decir, para toda la vida.", 2, "Los jueces son el poder judicial."), ("gob", "La Cámara de Representantes tiene 435 miembros con voto.", 0, "Otra parte del Congreso."),
       ("salud", "Las verduras de hoja verde tienen hierro y vitaminas.", 0, "Habla de comida."), ("salud", "Caminar rápido varias veces por semana fortalece el corazón.", 1, "Habla de actividad física."),
       ("salud", "Los adultos necesitan dormir al menos siete horas.", 2, "Habla del sueño."), ("salud", "Beber agua en lugar de refrescos reduce el azúcar en la dieta.", 0, "Habla de lo que comemos y bebemos."),
       ("seres", "Fabrican su propio alimento por medio de la fotosíntesis.", 0, "Solo las plantas hacen fotosíntesis."), ("seres", "Los champiñones y el moho que crece en el pan pertenecen a este grupo.", 2, "Son hongos."),
       ("seres", "Se mueven de un lugar a otro para buscar alimento.", 1, "Los animales se desplazan."), ("colon", "En las colonias del sur, grandes plantaciones cultivaban tabaco y arroz.", 0, "Habla del trabajo y la economía."),
       ("colon", "Muchos colonos de Nueva Inglaterra llegaron buscando libertad para practicar su fe.", 1, "Habla de religión."), ("colon", "Algunas colonias elegían asambleas que aprobaban leyes locales.", 2, "Habla de gobierno.")]
DO = ["Dato", "Opinión"]
DATOP = [("«El corazón humano tiene cuatro cavidades.»", 0, "Se comprueba en cualquier libro de biología."), ("«Las ciencias son la materia más aburrida de la escuela.»", 1, "«Más aburrida» es un gusto personal."),
         ("«Abraham Lincoln fue el decimosexto presidente de los Estados Unidos.»", 0, "Se comprueba en los registros históricos."), ("«Lincoln dio el discurso más emocionante de la historia.»", 1, "«Más emocionante» depende de quien lo escuche."),
         ("«El agua se congela a 32 grados Fahrenheit.»", 0, "Se comprueba con un termómetro."), ("«Los días de nieve son terribles.»", 1, "«Terribles» es una opinión."),
         ("«México se independizó de España en el siglo XIX.»", 0, "Es un hecho histórico."), ("«La comida mexicana es la más sabrosa del mundo.»", 1, "«La más sabrosa» depende del gusto."),
         ("«El Sol es una estrella.»", 0, "Es un dato de la ciencia."), ("«Todos deberían aprender astronomía.»", 1, "«Deberían» expresa una opinión."),
         ("«La biblioteca presta libros sin costo a los residentes.»", 0, "Se comprueba preguntando en la biblioteca."), ("«La biblioteca de mi barrio es increíble.»", 1, "«Increíble» expresa un sentimiento."),
         ("«Las abejas ayudan a polinizar muchos cultivos.»", 0, "Se ha estudiado y comprobado."), ("«Creo que las abejas son los insectos más interesantes.»", 1, "«Creo que» anuncia una opinión."),
         ("«La Declaración de Independencia se firmó en 1776.»", 0, "Lo dicen los documentos."), ("«Chicago tiene el mejor transporte público del país.»", 1, "«El mejor» se puede discutir.")]
CONC = [("los tres estados de la materia", ["En conclusión, la materia puede ser sólida, líquida o gaseosa, y cambia de estado con la temperatura.", "En conclusión, el hielo es mucho más divertido que el vapor para los niños pequeños y para los grandes.", "En conclusión, el mercurio es un metal muy curioso, porque es líquido a temperatura ambiente."], 0, "Resume las categorías. Las otras opinan o traen un dato nuevo."),
        ("los beneficios del ejercicio", ["En resumen, el gimnasio de mi barrio es el más moderno y el más barato de la ciudad.", "En resumen, hacer ejercicio fortalece el corazón, mejora el ánimo y ayuda a dormir mejor.", "En resumen, los Juegos Olímpicos modernos empezaron en Atenas en el año 1896."], 1, "Vuelve al tema y resume."),
        ("las causas de la Revolución estadounidense", ["En síntesis, los colonos no tenían ninguna razón para quejarse de los impuestos.", "En síntesis, George Washington fue más tarde el primer presidente del país.", "En síntesis, los impuestos y la falta de representación llevaron a los colonos a rebelarse."], 2, "Resume las causas sin opinar ni añadir datos nuevos."),
        ("cómo ahorrar en el supermercado", ["En resumen, hacer una lista, comparar precios y comprar en temporada ayuda a gastar menos.", "En resumen, ir al supermercado es la tarea más aburrida de toda la semana.", "En resumen, uno de los primeros supermercados de autoservicio abrió en Tennessee en 1916."], 0, "Recoge las tres estrategias del texto."),
        ("los servicios de la clínica comunitaria", ["En conclusión, la clínica abrió hace años y tiene un estacionamiento muy amplio.", "En conclusión, con sus consultas, sus vacunas y su farmacia, la clínica cuida la salud del barrio.", "En conclusión, todos deberían ir a la clínica en lugar de ir al hospital."], 1, "Recuerda las categorías y el tema."),
        ("el ciclo de vida de la mariposa", ["En síntesis, las mariposas monarca viajan miles de millas hasta México cada año.", "En síntesis, las mariposas son los insectos más bonitos de todo el jardín.", "En síntesis, la mariposa pasa por cuatro etapas: huevo, oruga, crisálida y adulta."], 2, "Resume las etapas del tema.")]
BIB = ["La biblioteca pública ofrece muchos servicios gratuitos que no todos conocen. Se pueden agrupar en tres categorías: los préstamos, la tecnología y los programas para la comunidad.",
       "En primer lugar, la biblioteca presta materiales. Con una tarjeta gratuita, cualquier residente puede llevarse libros, películas y audiolibros. Muchas bibliotecas también tienen libros en español y en otros idiomas.",
       "En segundo lugar, la biblioteca ofrece tecnología. Hay computadoras con internet, impresoras y, en muchas sucursales, conexión inalámbrica, es decir, internet sin cables para usar con el teléfono o la computadora portátil.",
       "Por último, la biblioteca organiza programas para la comunidad. Por ejemplo, hay horas de cuentos para niños, clases de inglés para adultos y talleres para buscar empleo.",
       "En resumen, gracias a sus préstamos, su tecnología y sus programas, la biblioteca pública es un recurso valioso y gratuito para toda la familia."]
MAT = ["La materia es todo lo que ocupa un lugar y tiene masa. En la naturaleza aparece principalmente en tres estados: sólido, líquido y gaseoso.",
       "Los sólidos tienen forma y volumen propios. Sus partículas están muy juntas y casi no se mueven. Una piedra, una cuchara y el hielo son sólidos.",
       "Los líquidos, en cambio, tienen volumen propio, pero toman la forma del recipiente que los contiene. Sus partículas se deslizan unas sobre otras. El agua, la leche y el aceite son líquidos.",
       "Los gases no tienen forma ni volumen propios: se expanden hasta llenar todo el espacio disponible. El aire que respiramos y el vapor de agua son gases.",
       "Una misma sustancia puede pasar de un estado a otro. Por ejemplo, el agua se congela a 32 °F (0 °C) y hierve a 212 °F (100 °C) al nivel del mar. En conclusión, conocer los tres estados de la materia ayuda a entender fenómenos cotidianos, como el hielo que se derrite o la ropa que se seca al sol."]
CONECTORES = ["en primer lugar", "en segundo lugar", "por último", "por un lado", "por otro lado", "es decir", "o sea", "esto significa que", "por ejemplo", "como", "entre ellos",
              "en cambio", "a diferencia de", "al igual que", "en resumen", "en conclusión", "en síntesis", "además", "también"]


def numerado(titulo, ps):
    return f'<div class="texto-lectura"><p><strong>{titulo}</strong></p>' + "".join(f'<p><span class="num-p">{i}</span> {t}</p>' for i, t in enumerate(ps, 1)) + "</div>"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Imagine que un vecino recién llegado le pregunta qué servicios hay en el barrio. No le diría todo de golpe y en desorden: le hablaría primero de las escuelas, luego de las clínicas y después del transporte. Sin darse cuenta, estaría organizando la información en <strong>categorías</strong>. Eso es un texto informativo: explicar un tema con orden para que el lector lo entienda.</p>
{C.tabla("Opinar frente a informar", ["Texto", "Qué quiere", "Cómo es"],
         [["De opinión (Lección 7.1)", "Convencer.", "Tiene una postura y razones. Usa «creo que», «debería»."], ["Informativo (esta lección)", "Explicar.", "Tiene un tema y categorías. Usa hechos, datos y definiciones, sin opiniones del autor."]])}
<p>La estructura de un texto informativo:</p>
<ul><li><strong>Introducción:</strong> presenta el tema y anuncia las categorías.</li><li><strong>Un párrafo por categoría:</strong> empieza con una oración temática y sigue con datos, detalles, ejemplos o definiciones.</li>
<li><strong>Conclusión:</strong> vuelve al tema y resume lo más importante, sin añadir información nueva.</li></ul>
<h3>Texto modelo: la biblioteca pública</h3>
{LE.escuchar(" ".join(BIB), "Escuchar el texto")}
{numerado("Mucho más que libros", BIB)}
<p class="fuente">Texto escrito para esta lección.</p>
<div class="esquema" role="img" aria-label="Esquema del texto: tema, los servicios gratuitos de la biblioteca. Préstamos: tarjeta gratuita; libros, películas, audiolibros; libros en otros idiomas. Tecnología: computadoras con internet; impresoras; conexión inalámbrica, con su definición. Programas: cuentos para niños; clases de inglés; talleres de empleo.">
<p class="esq-tema">Tema: los servicios gratuitos de la biblioteca</p>
<div class="esq-cats"><div><p class="esq-cat">Préstamos</p><ul><li>Tarjeta gratuita</li><li>Libros, películas, audiolibros</li><li>Libros en otros idiomas</li></ul></div>
<div><p class="esq-cat">Tecnología</p><ul><li>Computadoras con internet</li><li>Impresoras</li><li>Conexión inalámbrica (definición)</li></ul></div>
<div><p class="esq-cat">Programas</p><ul><li>Cuentos para niños</li><li>Clases de inglés</li><li>Talleres de empleo</li></ul></div></div></div>
{C.caja("tip", "Fíjese", "<p>La introducción anuncia las tres categorías, cada párrafo trata solo una y empieza con su oración temática, y la conclusión repite las tres sin añadir nada nuevo. En todo el texto no aparece ni una opinión del tipo «creo que».</p>")}
{P("Modelo 1", "¿Cuál es la oración temática del párrafo 3?", ["«Hay computadoras con internet, impresoras…»", "«En segundo lugar, la biblioteca ofrece tecnología.»", "«…es decir, internet sin cables…»"], 1, {0: "Es un detalle.", 2: "Es una definición."}, "La primera oración dice de qué trata el párrafo.")}
{P("Modelo 2", "¿Qué palabra se define en el texto?", ["Audiolibros", "Inalámbrica", "Talleres"], 1, {0: "No se explica.", 2: "No se explica."}, "«…conexión inalámbrica, es decir, internet sin cables…».")}"""

    pod = [("Está formado por el Senado y la Cámara de Representantes.", 0, "Es el Congreso."), ("Lo encabeza el presidente.", 1, "El presidente dirige el poder ejecutivo."),
           ("La Corte Suprema es su tribunal más alto.", 2, "Judicial = tribunales."), ("Decide si una ley respeta la Constitución.", 2, "Interpreta las leyes.")]
    POD = ["Legislativo", "Ejecutivo", "Judicial"]
    s2 = f"""<p>Antes de escribir, se reúnen los datos y se agrupan. Pregúntese: <strong>«¿De qué trata este dato?»</strong>. Los datos que responden lo mismo van juntos.</p>
<p>Tema: <strong>los tres poderes del gobierno de los Estados Unidos</strong>. ¿A qué categoría pertenece cada dato?</p>
{"".join(P(f"Categoría {i}", t, POD, k, {j: "Repase la Lección 6.3: legislativo hace, ejecutivo aplica, judicial interpreta." for j in range(3) if j != k}, f"<strong>{POD[k]}</strong>: {e}") for i, (t, k, e) in enumerate(pod, 1))}
{C.caja("tip", "Así nace el texto", "<p>Con esos datos ya agrupados, el texto se escribe casi solo: un párrafo para el poder legislativo, otro para el ejecutivo y otro para el judicial.</p>")}
<h3>Dato u opinión</h3>
<p>Un <strong>dato</strong> se puede comprobar: con un número, un documento, un experimento o una fuente. Una <strong>opinión</strong> dice lo que alguien piensa o siente, y otra persona puede pensar distinto. En un texto informativo solo van datos.</p>
{C.tabla("Datos y opiniones", ["Dato", "Opinión"], [["El lago Míchigan es uno de los cinco Grandes Lagos.", "El lago Míchigan es el más bonito de todos."], ["El agua hierve a 212 °F al nivel del mar.", "El té sabe mejor con el agua muy caliente."]], fila_th=False)}
{C.caja("ojo", "Palabras que delatan una opinión", "<p><em>mejor, peor, bonito, feo, increíble, terrible, debería, creo, me parece.</em> Si una oración tiene una de ellas, revise si es un dato.</p>")}
{P("¿Dato u opinión? 1", "«La Constitución de los Estados Unidos se firmó en 1787.»", DO, 0, {1: "Se puede comprobar en los documentos."}, "<strong>Dato.</strong>")}
{P("¿Dato u opinión? 2", "«El invierno es la peor estación del año.»", DO, 1, {0: "«La peor» depende de quien lo diga."}, "<strong>Opinión.</strong>")}"""

    s3 = f"""<p>La misma estructura sirve para las materias del GED. Lea este texto y busque las categorías.</p>
{LE.escuchar(" ".join(MAT), "Escuchar el texto")}
{numerado("Los estados de la materia", MAT)}
<p class="fuente">Texto escrito para esta lección.</p>
{P("Materia 1", "¿Cuáles son las categorías del texto?", ["Sólido, líquido y gaseoso", "Agua, leche y aceite", "Hielo, piedra y cuchara"], 0, {1: "Son ejemplos de líquidos.", 2: "Son ejemplos de sólidos."}, "Las anuncia el párrafo 1.")}
{P("Materia 2", "¿Qué conector usa el párrafo 3 para comparar con los sólidos?", ["En cambio", "Por ejemplo", "En conclusión"], 0, {1: "Da ejemplos.", 2: "Cierra el texto."}, "«Los líquidos, en cambio…».")}
<h3>Conectores y conclusión</h3>
{C.tabla("Conectores del texto informativo", ["Para…", "Conectores"],
         [["Ordenar categorías", "en primer lugar, en segundo lugar, por último, por un lado, por otro lado"], ["Definir o aclarar", "es decir, o sea, esto significa que"], ["Dar ejemplos", "por ejemplo, como, entre ellos"],
          ["Comparar", "en cambio, a diferencia de, al igual que"], ["Concluir", "en resumen, en conclusión, en síntesis"]])}
<p>Una buena conclusión informativa vuelve al tema, con otras palabras; recuerda las categorías o la idea más importante, y <strong>no añade</strong> datos nuevos ni opiniones.</p>
{P("Conclusión 1", "Texto sobre <strong>el ciclo del agua</strong>. ¿Cuál es la mejor conclusión?", ["En conclusión, la lluvia es lo mejor para las plantas y los jardines.", "En conclusión, el agua pasa por la evaporación, la condensación y la precipitación sin parar.", "En conclusión, los océanos cubren la mayor parte de la superficie de la Tierra."], 1,
   {0: "Es una opinión.", 2: "Trae un dato nuevo."}, "Resume las etapas del ciclo.")}
<h3>Taller: escriba su texto informativo</h3>
<p>Elija un tema de una materia o proponga uno suyo: los tres poderes del gobierno · los estados de la materia · el ciclo del agua · una festividad de su país · los servicios de su barrio.</p>
<div class="caja caja-tip"><p><strong>Introducción:</strong> ______ se puede explicar en (dos / tres) partes: ______, ______ y ______.<br><strong>Categoría 1:</strong> En primer lugar, ______. Por ejemplo, ______.<br>
<strong>Categoría 2:</strong> En segundo lugar, ______, es decir, ______.<br><strong>Categoría 3:</strong> Por último, ______.<br><strong>Conclusión:</strong> En resumen, ______.</p></div>
{taller("2-7-2", "Su texto informativo (8 a 10 oraciones)", "Tema y categorías… En primer lugar, … En segundo lugar, … Por último, … En resumen, …", 8, 90, CONECTORES,
        ["La introducción presenta el tema y anuncia las categorías.", "Cada párrafo o grupo de oraciones trata una sola categoría.", "Incluyo al menos dos datos que se pueden comprobar.", "Incluyo una definición (es decir…, o sea…).",
         "No hay opiniones: quité «creo», «mejor», «bonito»…", "La conclusión vuelve al tema y no añade datos nuevos.", "Escuché mi texto en voz alta y revisé la ortografía y la puntuación."])}
{C.tabla("Rúbrica del texto informativo", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"],
         [["Categorías", "Dos o tres categorías claras, cada una en su lugar", "Categorías claras, con algún dato fuera de lugar", "Las categorías se mezclan", "Información sin orden"],
          ["Datos y definiciones", "Varios datos y al menos una definición, sin opiniones", "Dos datos; quizás una opinión", "Un dato", "Solo opiniones"],
          ["Conectores", "Ordenan, definen y dan ejemplos", "Algunos, bien usados", "Pocos o repetidos", "Ninguno"],
          ["Conclusión", "Vuelve al tema y resume sin datos nuevos", "Vuelve al tema, pero no resume", "Añade información nueva", "No hay conclusión"]])}
<p>Total: 16 puntos.</p>
<p>Si tiene con quién practicar, escriban en papelitos diez datos sobre un tema (por ejemplo, su país de origen) y repártanlos en tres montones según su categoría: geografía, comida, fiestas.</p>"""

    secciones = [("s1", "Opinar frente a informar y un texto modelo", s1), ("s2", "Categorías, datos y opiniones", s2), ("s3", "Un texto de ciencias, la conclusión y el taller", s3)]
    tarea = [("Para el foro.", "Termine su texto informativo del taller, con al menos dos datos y una conclusión. Cópielo y entréguelo a su maestro o publíquelo en el foro del curso."),
             ("Esquema de un texto real.", "Lea un artículo corto de una revista o de un sitio de noticias. Dibuje su esquema: el tema arriba y sus categorías debajo, con dos datos en cada una."),
             ("Caza de opiniones.", "En ese mismo artículo, busque una oración que sea opinión, si la hay. Explique qué palabra la delata.")]
    quiz = [
        ("El propósito de un texto informativo es…", ["explicar un tema", "convencer al lector", "contar una historia"], 0, {1: "Eso es la opinión.", 2: "Eso es la narración."}, "<strong>Explicar.</strong>"),
        ("En un texto informativo, cada párrafo del cuerpo…", ["trata una sola categoría", "mezcla todas las categorías", "da la opinión del autor"], 0, {1: "Así se pierde el lector.", 2: "No lleva opiniones."}, "<strong>Una categoría</strong> por párrafo."),
        ("¿Qué debe hacer la introducción?", ["Presentar el tema y anunciar las categorías", "Dar todos los datos del texto de una vez", "Repetir la conclusión palabra por palabra"], 0, {1: "Los datos van en el cuerpo.", 2: "Va al principio, no al final."}, "Presenta y <strong>anuncia</strong>."),
        ("Tema: <strong>la alimentación saludable</strong>. ¿En qué categoría va «las manzanas tienen fibra»?", ["Frutas", "Ejercicio", "Horas de sueño"], 0, {1: "No habla de ejercicio.", 2: "No habla de sueño."}, "<strong>Frutas.</strong>"),
        ("Tema: <strong>los tres poderes</strong>. «Puede vetar una ley» es un dato del poder…", ["ejecutivo", "judicial", "legislativo"], 0, {1: "Los jueces no vetan.", 2: "El Congreso hace las leyes."}, "El <strong>ejecutivo</strong>: el presidente."),
        ("¿Cuál de estas oraciones es un <strong>dato</strong>?", ["La Tierra gira alrededor del Sol.", "El verano es la mejor época del año.", "Los gatos son más simpáticos que los perros."], 0, {1: "«La mejor» es opinión.", 2: "«Más simpáticos» es opinión."}, "Se puede comprobar."),
        ("¿Cuál de estas oraciones es una <strong>opinión</strong>?", ["El museo de ciencias es el más interesante de la ciudad.", "El museo de ciencias abre a las nueve y media.", "El museo de ciencias está junto al lago."], 0, {1: "Es un dato.", 2: "Es un dato."}, "«El más interesante» es opinión."),
        ("Según el texto de la materia, los líquidos…", ["toman la forma del recipiente", "tienen forma propia", "no tienen volumen propio"], 0, {1: "Eso es de los sólidos.", 2: "Eso es de los gases."}, "Toman la forma del <strong>recipiente</strong>."),
        ("«La fotosíntesis, ___, el proceso con el que las plantas fabrican su alimento, necesita luz.»", ["es decir", "por último", "en cambio"], 0, {1: "No ordena.", 2: "No compara."}, "<strong>es decir</strong>: define."),
        ("Al revisar su texto informativo encuentra «creo que es la mejor fiesta». ¿Qué hace?", ["La cambio por un dato sobre la fiesta", "La dejo, porque da más fuerza al texto", "La paso a la introducción del texto"], 0, {1: "Un texto informativo no lleva opiniones.", 2: "Sigue siendo una opinión."}, "La cambia por un <strong>dato</strong>."),
    ]
    filas = [
        ("Estructura", "Mi texto tiene introducción con categorías, un párrafo por categoría y conclusión.", "Me falta anunciar las categorías.", "Escribo sin orden (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Datos", "Agrupo datos por categoría y quito las opiniones.", "Se me cuela alguna opinión.", "No distingo dato y opinión (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Conclusión y taller", "Escribí 8 a 10 oraciones y una conclusión sin datos nuevos.", "Mi conclusión añade algo nuevo.", "No terminé el texto (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya escribe textos informativos ordenados. En la próxima lección escribirá una <strong>narración</strong> con escenario y diálogo, y aprenderá a revisarla.</p>"
    glosario = [("Texto informativo", "Texto que explica un tema con datos, sin opiniones."), ("Categoría", "Grupo de datos que tratan de lo mismo."),
                ("Oración temática", "La que abre un párrafo y dice de qué trata."), ("Dato", "Información que se puede comprobar.")]
    conexion = ("<p>En la Lección 7.1 escribió para convencer. Hoy escribirá para explicar, como en los textos de Ciencias y Estudios Sociales que leyó en el Tema 6.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un tema que conozca bien.</p>")
    estd = LE.estandares(["W.2", "W.3"], base=["R.5.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Explicar un tema con orden: categorías, datos y conclusión.", ["Escritura", "Texto informativo"],
                            ["<strong>Distinguir</strong> el texto informativo del de opinión.", "<strong>Agrupar</strong> los datos en categorías.",
                             "<strong>Separar</strong> los datos de las opiniones.", "<strong>Escribir</strong> un texto informativo con una conclusión ligada al tema."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-3", LE.titulo("7-3")), glosario, P)


def practica():
    ca = [{"enun": f"<p>Tema: <strong>{TEMAS[t][0]}</strong></p><span class=\"grande\">{d}</span><br>¿En qué categoría va?", "ops": TEMAS[t][1], "ok": k, "enOrden": True,
           "pista": "¿De qué trata el dato? Busque la categoría que responde a esa pregunta.", "exp": f"<strong>{TEMAS[t][1][k]}</strong>. {e}"} for t, d, k, e in CAT]
    do = [{"enun": f"<span class=\"grande\">{t}</span><br>¿Es un dato o una opinión?", "ops": DO, "ok": k, "enOrden": True,
           "pista": "¿Se puede comprobar, o depende de lo que alguien piensa o siente?", "exp": f"<strong>{DO[k]}</strong>. {e}"} for t, k, e in DATOP]
    cn = [{"enun": f"<p>Texto sobre: <strong>{t}</strong></p><strong>¿Cuál es la mejor conclusión?</strong>", "ops": ops, "ok": k,
           "pista": "¿Esa conclusión trae un dato nuevo o una opinión? La buena solo vuelve al tema y resume.", "exp": e} for t, ops, k, e in CONC]
    mods = [("categorias", "¿En qué categoría va?", C.om("m1", "Lea el dato y elija su categoría.")), ("dato-opinion", "¿Dato u opinión?", C.om("m2", "Decida si la oración es un dato o una opinión.")),
            ("conclusion", "La mejor conclusión", C.om("m3", "Elija la conclusión que vuelve al tema sin datos nuevos ni opiniones."))]
    js = C.js_datos("CA", ca) + C.js_datos("DO", do) + C.js_datos("CN", cn) + 'creaBanco("m1", CA);\ncreaBanco("m2", DO);\ncreaBanco("m3", CN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
