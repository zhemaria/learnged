# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 6.2 · Fuentes primarias y secundarias: introducción.
Fuente: clases_leng2/clase_6-2.html (GEDparaHispanos) y gramatica/n2-l6-2.html, adaptadas al marco de LearnGED.
El Discurso de Gettysburg (Abraham Lincoln, 19 de noviembre de 1863) es de dominio público; la traducción es de la lección.
Uso: python3 tools/build_leng2_6_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "6-2"
PS = ["Primaria", "Secundaria"]
CLAS = [("Una carta que un soldado escribió a su esposa durante la Segunda Guerra Mundial", 0, "La escribió alguien que vivía la guerra."),
        ("Un libro de texto de Estudios Sociales sobre la Segunda Guerra Mundial", 1, "Su autor explica la guerra a partir de otras fuentes."),
        ("La Declaración de Independencia de 1776", 0, "Es el documento original, escrito en el momento."),
        ("Un artículo de revista de 2010 que analiza la Declaración de Independencia", 1, "Lo escribió alguien 234 años después."),
        ("Una foto de la Marcha sobre Washington de 1963", 0, "Se tomó durante el hecho."),
        ("Una biografía de Martin Luther King Jr. publicada en 1995", 1, "Su autor estudió la vida de King después."),
        ("El diario que escribió Ana Frank mientras estaba escondida", 0, "Lo escribió ella misma, día a día."),
        ("Una enciclopedia en línea con un artículo sobre César Chávez", 1, "Resume lo que otras fuentes documentaron."),
        ("Una entrevista de radio a un trabajador del campo que participó en la huelga de la uva de 1965", 0, "Es la voz de un participante."),
        ("Un documental de 2018 sobre la huelga de la uva", 1, "Se hizo décadas después, con otras fuentes."),
        ("Una ley aprobada por el Congreso en 1964", 0, "Es el documento original del momento."),
        ("Un resumen de esa ley escrito por un profesor en 2021", 1, "Explica la ley después."),
        ("Un cartel de propaganda de 1917 que llama a los jóvenes al ejército", 0, "Se creó y se usó en esa época."),
        ("Un libro de historia de 1900 sobre la llegada de Colón en 1492", 1, "Es antiguo, pero su autor no vivió 1492."),
        ("El acta de nacimiento de su abuela", 0, "Se hizo en el momento del nacimiento."),
        ("Una página web que explica la historia de su ciudad", 1, "Su autor reunió y explicó información de otras fuentes."),
        ("Una moneda romana encontrada en una excavación", 0, "Es un objeto de la época."),
        ("El testimonio de una sobreviviente del terremoto de México de 1985", 0, "Ella vivió el terremoto."),
        ("Un capítulo de libro que compara varios terremotos del siglo XX", 1, "Analiza hechos que su autor estudió."),
        ("El discurso que dio un presidente el día que asumió el cargo", 0, "Lo pronunció en el momento.")]
VIAJE = "«El barco salió de Veracruz el 3 de marzo. Éramos doscientos pasajeros y apenas había agua. A los diez días, muchos niños estaban enfermos. Mi madre repartía su pan entre los más pequeños.»"
ABEJAS = "«Las abejas polinizan muchos de los cultivos que comemos. Sin ellas, frutas como las manzanas y las almendras serían escasas. En los últimos años, sin embargo, muchas colonias han desaparecido.»"
CARTA = "«Querido hermano: aquí en Chicago el invierno es terrible. El viento corta la cara y la nieve llega a las rodillas. Pero en la fábrica pagan bien y ya ahorré para traer a Rosa en primavera.»"
CITAS = [(VIAJE, "el viaje fue muy duro.", ["«…apenas había agua. A los diez días, muchos niños estaban enfermos.»", "«El barco salió de Veracruz el 3 de marzo. Éramos doscientos pasajeros…»", "«Mi madre repartía su pan entre los más pequeños.»"], "Falta de agua y niños enfermos demuestran que fue duro."),
         (VIAJE, "la madre de quien escribe era generosa.", ["«Mi madre repartía su pan entre los más pequeños.»", "«Éramos doscientos pasajeros y apenas había agua.»", "«…muchos niños estaban enfermos.»"], "Compartir su pan demuestra generosidad."),
         (ABEJAS, "las abejas son importantes para la alimentación.", ["«Sin ellas, frutas como las manzanas y las almendras serían escasas.»", "«En los últimos años, sin embargo, muchas colonias han desaparecido.»", "«…frutas como las manzanas y las almendras…»"], "Sin abejas habría pocas frutas: demuestra su importancia."),
         (ABEJAS, "hay un problema con las abejas.", ["«…muchas colonias han desaparecido.»", "«Las abejas polinizan muchos de los cultivos…»", "«…frutas como las manzanas y las almendras…»"], "La desaparición de colonias es el problema."),
         (CARTA, "el autor tiene planes para el futuro.", ["«…ya ahorré para traer a Rosa en primavera.»", "«Querido hermano: aquí en Chicago el invierno es terrible.»", "«El viento corta la cara y la nieve llega a las rodillas.»"], "Traer a Rosa es un plan."),
         (CARTA, "al autor le cuesta el clima de Chicago.", ["«El viento corta la cara y la nieve llega a las rodillas.»", "«Pero en la fábrica pagan bien y ya ahorré para traer a Rosa…»", "«Querido hermano: aquí en Chicago…»"], "Describe lo duro del clima."),
         ("«La vacuna contra la viruela, creada por Edward Jenner en 1796, fue la primera vacuna moderna. Gracias a las campañas de vacunación, en 1980 la viruela se declaró erradicada en todo el mundo.»", "las vacunas pueden acabar con una enfermedad.",
          ["«…en 1980 la viruela se declaró erradicada en todo el mundo.»", "«La vacuna contra la viruela, creada por Edward Jenner en 1796…»", "«…fue la primera vacuna moderna.»"], "«Erradicada» quiere decir eliminada por completo."),
         ("«El 1 de diciembre de 1955, en Montgomery, Rosa Parks se negó a ceder su asiento de autobús a un pasajero blanco. Fue arrestada. Su arresto inspiró un boicot a los autobuses que duró más de un año.»", "la acción de Rosa Parks tuvo consecuencias importantes.",
          ["«Su arresto inspiró un boicot a los autobuses que duró más de un año.»", "«…Rosa Parks se negó a ceder su asiento de autobús a un pasajero blanco.»", "«El 1 de diciembre de 1955, en Montgomery…»"], "El boicot fue la consecuencia."),
         ("«Hoy recorrimos doce millas. El camino está lleno de piedras y los bueyes están cansados. Esta noche, junto al fuego, papá tocó el violín y todos cantamos. Por un momento olvidamos el cansancio.»", "el grupo encontró momentos de alegría en el viaje.",
          ["«…papá tocó el violín y todos cantamos.»", "«Hoy recorrimos doce millas.»", "«El camino está lleno de piedras y los bueyes están cansados.»"], "Cantar junto al fuego es un momento alegre."),
         ("«El nuevo parque tiene canchas, juegos para niños y un huerto comunitario. Desde que abrió, los vecinos dicen que se ven más en la calle y que el barrio parece más seguro.»", "el parque cambió la vida del barrio.",
          ["«…los vecinos dicen que se ven más en la calle…»", "«El nuevo parque tiene canchas…»", "«…juegos para niños y un huerto comunitario.»"], "Habla de cómo cambió el barrio, no solo de lo que tiene el parque.")]
PV = [("<strong>Periódico del sindicato, 1937:</strong> «Miles de trabajadores valientes defendieron hoy su derecho a una vida digna.»", "¿Cómo ve el autor a los huelguistas?", ["Con admiración", "Con desprecio", "Sin ninguna opinión"], "«Valientes» y «vida digna» muestran admiración."),
      ("<strong>Periódico de los empresarios, 1937:</strong> «Un grupo de agitadores paralizó hoy la producción y dejó sin trabajo a cientos de familias.»", "¿Cómo ve el autor a los huelguistas?", ["Como alborotadores que causan daño", "Como héroes que luchan por todos", "Como personas sin ninguna culpa"], "«Agitadores» y «paralizó» son palabras negativas."),
      ("<strong>Carta al alcalde:</strong> «Le escribo porque en mi calle no hay alumbrado desde hace dos meses. Le ruego que envíe a alguien a repararlo cuanto antes.»", "¿Cuál es el propósito de la carta?", ["Pedir una solución", "Contar una historia divertida", "Felicitar al alcalde"], "«Le ruego que envíe…» es una petición."),
      ("<strong>Folleto de la ciudad:</strong> «El nuevo tren llegará al aeropuerto en 20 minutos. Funcionará de 5 de la mañana a 1 de la madrugada.»", "¿Cuál es el propósito del folleto?", ["Informar", "Convencer de votar", "Expresar tristeza"], "Da datos de horario y duración."),
      ("<strong>Discurso de una candidata:</strong> «Si votan por mí, cada familia tendrá una escuela de calidad cerca de casa. Juntos podemos lograrlo.»", "¿Cuál es el propósito del discurso?", ["Convencer al público", "Informar de forma neutral", "Contar un recuerdo personal"], "Pide el voto con una promesa."),
      ("<strong>Diario de un colono, 1849:</strong> «Por fin llegamos a California. Dicen que hay oro en cada río. ¡Pronto seremos ricos!»", "¿Qué punto de vista muestra el autor?", ["Optimista y lleno de esperanza", "Triste, cansado y sin ánimo", "Neutral: solo da datos del viaje"], "«¡Pronto seremos ricos!» es optimismo."),
      ("<strong>Recuerdo de una mujer indígena de California, escrito años después:</strong> «Cuando llegaron los buscadores de oro, los ríos se ensuciaron y perdimos los lugares donde pescábamos.»", "¿Por qué su punto de vista es distinto del del colono?", ["Porque la llegada del oro la perjudicó", "Porque ella no vivió en California", "Porque escribe sobre otro país"], "Para ella, la fiebre del oro trajo pérdidas."),
      ("<strong>Anuncio de 1920:</strong> «¡Compre el nuevo jabón Espuma Blanca! Sus sábanas quedarán más blancas que nunca.»", "¿Para qué le sirve hoy este anuncio a un historiador?", ["Para saber qué se vendía y cómo", "Para saber si el jabón era el mejor", "Para conocer la fábrica del jabón"], "Una fuente puede ser útil aunque no sea neutral."),
      ("<strong>Enfermera en un hospital de guerra, 1864:</strong> «Hoy llegaron cuarenta heridos. No hay vendas suficientes. Escribo esto a las tres de la madrugada, sin haber dormido.»", "¿Qué hace valiosa esta fuente?", ["Es el testimonio directo de una testigo", "Es una explicación escrita años después", "Presenta las opiniones de los dos bandos"], "Es primaria: ella lo vivió."),
      ("<strong>Reseña de un vecino:</strong> «El restaurante de la esquina es el mejor del barrio. La comida es deliciosa y los dueños son amabilísimos.»", "¿Qué tipo de texto es?", ["Una opinión personal", "Un informe con datos", "Una ley de la ciudad"], "«El mejor», «deliciosa» y «amabilísimos» son opiniones.")]
GETT = ["Hace ochenta y siete años, nuestros padres crearon en este continente una nueva nación, concebida en libertad y consagrada a la idea de que todos los hombres son creados iguales.",
        "Ahora estamos librando una gran guerra civil, que pone a prueba si esa nación, o cualquier nación así concebida y así consagrada, puede durar mucho tiempo. Estamos reunidos en un gran campo de batalla de esa guerra. Hemos venido a dedicar una parte de este campo como lugar de descanso final para quienes dieron aquí su vida para que esa nación pudiera vivir. Es del todo justo y apropiado que lo hagamos.",
        "Pero, en un sentido más amplio, no podemos dedicar, no podemos consagrar, no podemos santificar esta tierra. Los hombres valientes, vivos y muertos, que lucharon aquí, ya la han consagrado, muy por encima de nuestro pobre poder de añadir o quitar algo. El mundo apenas notará ni recordará por mucho tiempo lo que decimos aquí, pero nunca podrá olvidar lo que ellos hicieron aquí.",
        "Somos nosotros, los vivos, quienes debemos dedicarnos a la obra inconclusa que quienes lucharon aquí han hecho avanzar tan noblemente. Somos nosotros quienes debemos dedicarnos a la gran tarea que todavía tenemos por delante: que de estos muertos honrados tomemos mayor devoción por la causa por la que ellos dieron la última y completa medida de su devoción; que decidamos firmemente que estos muertos no habrán muerto en vano; que esta nación, bajo Dios, tenga un nuevo nacimiento de la libertad, y que el gobierno del pueblo, por el pueblo y para el pueblo no desaparezca de la tierra."]
SEC = "El Discurso de Gettysburg es breve: en inglés tiene unas 270 palabras. Antes de Lincoln, el orador principal del acto, Edward Everett, habló durante unas dos horas. Algunos periódicos de la época criticaron el discurso del presidente; otros lo elogiaron. Con el paso del tiempo, sin embargo, el texto de Lincoln se volvió un símbolo. Los historiadores señalan que Lincoln presentó la guerra no solo como una lucha para mantener unido el país, sino como una prueba de que un gobierno democrático, basado en la igualdad, podía sobrevivir. Hoy muchas escuelas piden a sus estudiantes que lo aprendan de memoria."


def caja_txt(t): return f'<div class="texto-lectura"><p>{t}</p></div>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Imagine que quiere saber cómo fue la boda de sus abuelos. Puede mirar las fotos de ese día, leer la invitación o escuchar a su abuela contarla. También puede leer lo que escribió años después un primo que no estuvo allí. Las dos cosas le informan, pero no son iguales: unas vienen del momento y la otra lo cuenta después. Los historiadores llaman a las primeras <strong>fuentes primarias</strong> y a la segunda <strong>fuente secundaria</strong>. En el GED de Estudios Sociales leerá muchas de las dos.</p>
{C.tabla("Fuentes primarias y secundarias", ["", "Fuente primaria", "Fuente secundaria"],
         [["¿Quién la crea?", "Alguien que vivió o presenció el hecho", "Alguien que lo estudió después"], ["¿Cuándo?", "En el momento o poco después", "Más tarde, a veces siglos después"],
          ["Ejemplos", "Cartas, diarios, discursos, fotos, leyes, entrevistas a testigos, objetos de la época", "Libros de texto, enciclopedias, biografías, artículos que analizan el hecho, documentales"],
          ["Lo que aporta", "La voz directa de la época", "Una explicación ordenada, con contexto"]])}
{C.caja("tip", "La pregunta clave", "<p>«¿Quien lo hizo estuvo allí, en ese tiempo?». Si la respuesta es sí, es primaria. Ojo: una fuente no es primaria por ser antigua. Un libro de historia de 1900 sobre Cristóbal Colón es secundario, porque su autor no vivió en 1492.</p>")}
{P("¿Primaria o secundaria? 1", "El diario de una enfermera durante la Guerra Civil", PS, 0, {1: "Lo escribió una testigo, día a día."}, "<strong>Primaria</strong>: lo escribió una testigo.")}
{P("¿Primaria o secundaria? 2", "Un documental de 2015 sobre la batalla de Gettysburg", PS, 1, {0: "Se hizo mucho después."}, "<strong>Secundaria</strong>: se hizo a partir de otras fuentes.")}
{P("¿Primaria o secundaria? 3", "Una biografía de Lincoln escrita en 1920", PS, 1, {0: "Es antigua, pero ¿su autor vivió los hechos?"}, "<strong>Secundaria</strong>: es antigua, pero su autor no vivió los hechos.")}"""

    s2 = f"""<p><strong>El contexto.</strong> En julio de 1863, durante la Guerra Civil de los Estados Unidos, se libró en Gettysburg, Pensilvania, una de las batallas más sangrientas de la guerra: en tres días hubo decenas de miles de muertos, heridos y desaparecidos. Cuatro meses después, el 19 de noviembre de 1863, se inauguró allí un cementerio para los soldados de la Unión. El presidente Abraham Lincoln habló apenas unos dos minutos. Su discurso se convirtió en uno de los textos más famosos de la historia del país.</p>
<p>Lea el discurso completo. Es una traducción hecha para esta lección; el original está en inglés. Los párrafos están numerados para poder citarlos.</p>
{LE.escuchar(" ".join(GETT), "Escuchar el discurso")}
<div class="texto-lectura">{"".join(f'<p><span class="num-p">{i}</span> {t}</p>' for i, t in enumerate(GETT, 1))}<p><em>Abraham Lincoln, 19 de noviembre de 1863. Traducción de la lección.</em></p></div>
{C.caja("tip", "«Hace ochenta y siete años»", "<p>1863 − 87 = 1776, el año de la Declaración de Independencia. Lincoln no dice la fecha: espera que su público haga la cuenta. Y la frase «todos los hombres son creados iguales» está tomada de esa Declaración.</p>")}
{P("Lectura 1", "¿Dónde y cuándo pronunció Lincoln el discurso?", ["En Gettysburg, el día de la batalla", "En Gettysburg, cuatro meses después de la batalla", "En Washington, al terminar la guerra"], 1, {0: "La batalla fue en julio.", 2: "La guerra no había terminado."}, "La batalla fue en julio; el discurso, el 19 de noviembre de 1863.")}
{P("Lectura 2", "En el párrafo 3, ¿quiénes ya consagraron esa tierra?", ["El presidente y su gobierno", "Los hombres valientes que lucharon allí", "El público que escucha el discurso"], 1, {0: "Lincoln dice que ellos no pueden.", 2: "Lincoln dice que ellos no pueden."}, "«Los hombres valientes, vivos y muertos, que lucharon aquí, ya la han consagrado».")}
{P("Lectura 3", "¿Qué pide Lincoln a los vivos en el párrafo 4?", ["Que vuelvan a sus casas en paz", "Que construyan un monumento mayor", "Que continúen la obra de los soldados"], 2, {0: "Relea el comienzo del párrafo 4.", 1: "No habla de monumentos."}, "«…debemos dedicarnos a la obra inconclusa…».")}
{P("Lectura 4", "¿Cuál es la idea central del discurso?", ["Honrar a los muertos dándole sentido a su sacrificio", "Describir con detalle cómo se desarrolló la batalla", "Explicar las causas por las que empezó la Guerra Civil"], 0, {1: "No describe la batalla.", 2: "No explica las causas."}, "Los honra y pide que «no habrán muerto en vano».")}
<h3>Una fuente secundaria sobre el mismo hecho</h3>
<p>Ahora lea un texto escrito hoy sobre el discurso, como el que encontraría en una enciclopedia o un libro de texto.</p>
{LE.escuchar(SEC, "Escuchar el texto")}
{caja_txt(SEC)}
<p class="fuente">Texto escrito para esta lección con datos históricos conocidos.</p>
{C.tabla("Las dos fuentes sobre Gettysburg", ["", "El discurso", "El texto explicativo"],
         [["¿Quién?", "Lincoln, que estaba allí", "Un autor de hoy"], ["¿Cuándo?", "1863, el día del acto", "Más de 150 años después"],
          ["¿Para qué?", "Honrar a los muertos y animar a seguir la lucha", "Informar y explicar la importancia del discurso"], ["Tipo", "Primaria", "Secundaria"]])}
{C.caja("tip", "Se complementan", "<p>La fuente primaria le da la voz de Lincoln; la secundaria le da lo que él no podía saber, por ejemplo, que su discurso se volvería famoso. Por eso el GED a menudo pone una de cada tipo y pregunta qué tienen en común o en qué se diferencian.</p>")}"""

    s3 = f"""<p><strong>Citar evidencia</strong> es copiar las palabras exactas del texto que demuestran lo que usted dice. Las palabras copiadas van entre comillas, y conviene indicar de dónde salen.</p>
<div class="caja caja-tip"><p><strong>Afirmación:</strong> Lincoln pensaba que lo que hicieron los soldados importaba más que los discursos.</p>
<p><strong>Evidencia:</strong> En el párrafo 3, Lincoln dice que el mundo «apenas notará ni recordará por mucho tiempo lo que decimos aquí, pero nunca podrá olvidar lo que ellos hicieron aquí».</p>
<p><strong>Explicación:</strong> Lincoln compara las palabras del acto con las acciones de los soldados y dice que las acciones se recordarán más.</p></div>
<p>Frases útiles para presentar una cita: <em>Según el autor… · En el párrafo 2, Lincoln afirma que… · El texto dice… · Como señala el discurso…</em></p>
{C.caja("ojo", "La mejor cita", "<p>No es la más larga ni la más bonita: es la que <strong>demuestra directamente</strong> la afirmación. Una cita que solo habla del mismo tema no basta.</p>")}
{P("Cita 1", "<strong>Afirmación:</strong> Lincoln creía que la nación se fundó sobre la igualdad.", ["«…consagrada a la idea de que todos los hombres son creados iguales.»", "«Estamos reunidos en un gran campo de batalla de esa guerra.»", "«Es del todo justo y apropiado que lo hagamos.»"], 0, {1: "No habla de igualdad.", 2: "No habla de igualdad."}, "Es la única cita que habla de igualdad.")}
{P("Cita 2", "<strong>Afirmación:</strong> Lincoln quería que la democracia sobreviviera.", ["«…quienes dieron aquí su vida…»", "«Los hombres valientes, vivos y muertos…»", "«…que el gobierno del pueblo… no desaparezca de la tierra.»"], 2, {0: "Habla de los muertos.", 1: "Habla de los soldados."}, "«Gobierno del pueblo» es la democracia; pide que no desaparezca.")}
<h3>Punto de vista y propósito</h3>
<p>Toda fuente la escribe alguien, con su <strong>punto de vista</strong> (cómo ve el hecho) y con un <strong>propósito</strong> (para qué escribe). Una fuente primaria es valiosa, pero no es neutral: muestra lo que vio y pensó una persona. Por eso los historiadores comparan varias.</p>
<p>Lea dos descripciones de un mismo hecho. Son ejemplos inventados para la lección.</p>
<div class="dos-textos"><div class="texto-lectura"><p><strong>Diario de una costurera, 1911:</strong> «Hoy salimos a la calle cientos de mujeres. Trabajamos doce horas por un sueldo que no alcanza para el pan. Pedimos poco: un día más corto y ventanas que se abran. Volveremos mañana.»</p></div>
<div class="texto-lectura tb"><p><strong>Aviso del dueño de la fábrica, 1911:</strong> «Unas pocas empleadas abandonaron hoy su puesto. La fábrica ofrece trabajo seguro y sueldos justos. Quien no regrese el lunes perderá su empleo.»</p></div></div>
{C.tabla("Punto de vista y propósito de las dos fuentes", ["", "La costurera", "El dueño"],
         [["¿Cuántas eran?", "«cientos de mujeres»", "«unas pocas empleadas»"], ["¿Cómo era el trabajo?", "Mucho tiempo, poco sueldo", "Seguro y con sueldo justo"], ["Propósito", "Registrar la protesta y su razón", "Hacer que las trabajadoras regresen"]])}
{C.caja("tip", "Las palabras delatan el punto de vista", "<p>«Cientos» frente a «unas pocas», «salimos» frente a «abandonaron su puesto». Las dos son fuentes primarias del mismo día y cuentan cosas muy distintas. Para saber qué pasó, el historiador necesita más fuentes: una foto, un periódico, una lista de trabajadoras.</p>")}
{P("¿Quién lo diría? 1", "«Nos duelen los ojos de coser con tan poca luz.»", ["La costurera", "El dueño"], 0, {1: "Habla en primera persona del trabajo."}, "Habla de las condiciones del trabajo: la costurera.")}
{P("¿Quién lo diría? 2", "«Las que regresen el lunes conservarán su puesto.»", ["La costurera", "El dueño"], 1, {0: "Su propósito es que vuelvan a trabajar."}, "Quiere que vuelvan: el dueño.")}
{P("¿Quién lo diría? 3", "¿Por qué ninguna de las dos fuentes basta para saber cuántas mujeres salieron?", ["Porque cada una exagera según su interés", "Porque son demasiado cortas para saberlo", "Porque las dos son fuentes secundarias"], 0, {1: "El largo no es el problema.", 2: "Las dos son primarias."}, "Cada una tiene un punto de vista: hay que buscar más fuentes.")}
<h3>El Archivo de fuentes</h3>
<p>En la sección de Estudios Sociales de LearnGED hay un <a href="/es/estudios-sociales/fuentes/">Archivo de fuentes</a> con documentos históricos reales. Antes de leer cualquiera, hágale estas cuatro preguntas:</p>
{C.tabla("Cuatro preguntas para cualquier fuente", ["Pregunta", "Qué averigua"], [["¿Quién?", "¿Quién lo escribió o lo creó? ¿Estuvo allí?"], ["¿Cuándo?", "¿En qué fecha? ¿Antes, durante o después del hecho?"],
                                                                                  ["¿Para quién?", "¿A quién iba dirigido: al público, a una persona, al gobierno?"], ["¿Para qué?", "¿Quería informar, convencer, pedir algo, recordar?"]])}
<p>Con esas cuatro respuestas ya sabe si es primaria o secundaria, y entiende su punto de vista antes de leer la primera línea.</p>
<p>Si tiene con quién practicar, busquen en casa una fuente primaria de su propia familia: una carta, una foto antigua, un acta de nacimiento. Respondan juntos las cuatro preguntas.</p>"""

    secciones = [("s1", "¿Primaria o secundaria?", s1), ("s2", "El Discurso de Gettysburg y una fuente secundaria", s2), ("s3", "Citar evidencia, punto de vista y propósito", s3)]
    tarea = [("Del Archivo.", "Elija un documento del <a href=\"/es/estudios-sociales/fuentes/\">Archivo de fuentes</a>. Responda por escrito las cuatro preguntas (¿quién?, ¿cuándo?, ¿para quién?, ¿para qué?) y diga si es primario o secundario."),
             ("Mi cita.", "Escriba una afirmación sobre el Discurso de Gettysburg y apóyela con una cita entre comillas, indicando el párrafo. Termine con una oración de explicación, como en el modelo de la sección 3."),
             ("Dos puntos de vista.", "Piense en algo que pasó en su trabajo, su escuela o su barrio. Escriba dos oraciones que lo cuenten: una desde su punto de vista y otra desde el de otra persona involucrada.")]
    G = caja_txt("«…que el gobierno del pueblo, por el pueblo y para el pueblo no desaparezca de la tierra.» (Lincoln, 1863)")
    quiz = [
        ("Una <strong>fuente primaria</strong> es…", ["una fuente creada por alguien que vivió el hecho", "una fuente que explica el hecho años después", "cualquier fuente que tenga más de cien años"], 0, {1: "Eso es una fuente secundaria.", 2: "La edad no basta."}, "La crea alguien que <strong>vivió</strong> el hecho."),
        ("¿Cuál de estas es una fuente <strong>secundaria</strong>?", ["Un libro de texto sobre la Revolución mexicana", "Una foto tomada durante la Revolución mexicana", "Una carta de un soldado de la Revolución"], 0, {1: "Se tomó en el momento.", 2: "La escribió un testigo."}, "El <strong>libro de texto</strong>."),
        ("¿Cuál de estas es una fuente <strong>primaria</strong>?", ["El diario de una inmigrante que llegó en 1910", "Un artículo de 2020 sobre la inmigración de 1910", "Una enciclopedia sobre la historia de la inmigración"], 0, {1: "Se escribió después.", 2: "Resume otras fuentes."}, "El <strong>diario</strong>."),
        ("Una biografía de George Washington escrita en 1850 es una fuente…", ["secundaria, porque su autor no vivió los hechos", "primaria, porque es muy antigua", "primaria, porque habla de un presidente"], 0, {1: "La edad no basta.", 2: "El tema no la hace primaria."}, "<strong>Secundaria.</strong>"),
        ("¿Por qué el Discurso de Gettysburg es una fuente primaria?", ["Lo pronunció Lincoln en el lugar y en la época", "Lo estudian hoy en todas las escuelas del país", "Es un texto muy breve y fácil de recordar"], 0, {1: "Que se estudie no lo hace primario.", 2: "El largo no importa."}, "Lincoln <strong>estaba allí</strong>."),
        ("«Hace ochenta y siete años» se refiere al año…", ["1776", "1863", "1787"], 0, {1: "Ese es el año del discurso.", 2: "Haga la cuenta: 1863 − 87."}, "1863 − 87 = <strong>1776</strong>."),
        ("¿Cuál era el propósito principal de Lincoln en su discurso?", ["Honrar a los soldados y animar a seguir la lucha", "Contar paso a paso cómo se desarrolló la batalla", "Anunciar al país que la guerra había terminado"], 0, {1: "No describe la batalla.", 2: "La guerra seguía."}, "<strong>Honrar</strong> y animar."),
        (G + "¿Qué idea apoya esta cita?", ["Lincoln quería que la democracia sobreviviera", "Lincoln quería terminar pronto el acto", "Lincoln quería más soldados para el ejército"], 0, {1: "La cita no habla del acto.", 2: "La cita no habla de soldados."}, "La <strong>democracia</strong>."),
        ("La mejor cita para apoyar una afirmación es la que…", ["la demuestra directamente", "es la más larga del texto", "habla del mismo tema en general"], 0, {1: "El largo no importa.", 2: "Hablar del tema no basta."}, "La <strong>demuestra</strong> directamente."),
        ("La costurera dice «cientos de mujeres» y el dueño dice «unas pocas». Esto muestra que…", ["cada uno cuenta el hecho desde su punto de vista", "uno de los dos dice siempre la verdad", "las dos son fuentes secundarias"], 0, {1: "No se puede saber con dos fuentes.", 2: "Las dos son primarias."}, "Cada fuente tiene su <strong>punto de vista</strong>."),
    ]
    filas = [
        ("Tipos de fuente", "Distingo las fuentes primarias de las secundarias con la pregunta clave.", "Me confundo con las fuentes antiguas.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Leer una fuente primaria", "Entiendo el Discurso de Gettysburg y lo comparo con una fuente secundaria.", "Lo entiendo con ayuda.", "No lo entiendo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Citar y punto de vista", "Elijo la cita que demuestra y reconozco el punto de vista de cada fuente.", "Elijo citas que solo hablan del tema.", "No sé citar (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya reconoce las fuentes y sabe citarlas. En la próxima lección trabajará el <strong>vocabulario de ciencias e historia</strong>.</p>"
    glosario = [("Fuente primaria", "Creada en el momento o por alguien que vivió el hecho."), ("Fuente secundaria", "Creada después por alguien que estudió el hecho."),
                ("Citar", "Copiar entre comillas las palabras exactas de un texto."), ("Evidencia", "Las palabras o los datos que demuestran una afirmación.")]
    conexion = ("<p>En la Lección 5.1 comparó dos textos y su punto de vista. Hoy hará lo mismo con documentos históricos, y aprenderá a citar las palabras exactas que apoyan lo que usted afirma.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.8.2", "R.6.1", "R.9.2"], base=["R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "La voz del momento y la explicación de después.", ["Lectura", "Fuentes"],
                            ["<strong>Distinguir</strong> fuentes primarias y secundarias.", "<strong>Leer</strong> una fuente primaria: el Discurso de Gettysburg.",
                             "<strong>Citar</strong> evidencia que demuestre una afirmación.", "<strong>Reconocer</strong> el punto de vista y el propósito de una fuente."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-3", LE.titulo("6-3")), glosario, P)


def practica():
    cl = [{"enun": f"<span class=\"grande\">{d}</span><br>¿Es una fuente primaria o secundaria?", "ops": PS, "ok": k, "enOrden": True,
           "pista": "¿La persona que lo creó estuvo allí, en ese tiempo?", "exp": f"<strong>{PS[k]}</strong>. {e}"} for d, k, e in CLAS]
    ci = [{"enun": caja_txt(t) + f"<p><strong>Afirmación:</strong> {a}</p><strong>¿Qué cita la demuestra mejor?</strong>", "ops": ops, "ok": 0,
           "pista": "Esa cita habla del tema, pero ¿demuestra exactamente la afirmación?", "exp": e} for t, a, ops, e in CITAS]
    pv = [{"enun": caja_txt(t) + f"<strong>{q}</strong>", "ops": ops, "ok": 0, "pista": "Fíjese en las palabras que elige el autor y en lo que quiere lograr.", "exp": e} for t, q, ops, e in PV]
    mods = [("tipo", "¿Primaria o secundaria?", C.om("m1", "Decida si la fuente es primaria o secundaria.")),
            ("citas", "La cita que demuestra", C.om("m2", "Lea el texto y elija la cita que demuestra la afirmación.")),
            ("punto-de-vista", "Punto de vista y propósito", C.om("m3", "Lea la fuente y responda sobre su punto de vista o su propósito."))]
    js = C.js_datos("CL", cl) + C.js_datos("CI", ci) + C.js_datos("PV", pv) + 'creaBanco("m1", CL);\ncreaBanco("m2", CI);\ncreaBanco("m3", PV);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
