# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 3.1 · Mayúsculas, comas, dos puntos y raya.
Fuente: clases_leng2/clase_3-1.html (GEDparaHispanos) y gramatica/n2-l3-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_3_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "3-1"
MAY = [(["El martes tengo cita con el dentista.", "El Martes tengo cita con el Dentista.", "El Martes tengo cita con el dentista."], "Los días van con minúscula, y <em>dentista</em> también."),
       (["Mi hija nació en marzo, en primavera.", "Mi hija nació en Marzo, en Primavera.", "Mi hija nació en marzo, en Primavera."], "Meses y estaciones, con minúscula."),
       (["Mi esposo es guatemalteco y habla español y quiché.", "Mi esposo es Guatemalteco y habla Español y Quiché.", "Mi esposo es guatemalteco y habla Español y quiché."], "Nacionalidades e idiomas, con minúscula."),
       (["Vivimos cerca del lago Míchigan.", "Vivimos cerca del Lago Míchigan.", "Vivimos cerca del lago míchigan."], "<em>lago</em> en minúscula; el nombre propio, con mayúscula. En español se escribe <em>Míchigan</em>, con tilde."),
       (["Estudio en Truman College desde agosto.", "Estudio en truman college desde Agosto.", "Estudio en Truman College desde Agosto."], "La institución, con mayúscula; el mes, con minúscula."),
       (["El Día de Acción de Gracias cenamos pavo.", "El día de acción de gracias cenamos pavo.", "El Día de Acción de gracias cenamos Pavo."], "Las festividades llevan mayúscula en sus palabras principales."),
       (["La señora López trabaja en la Cruz Roja.", "La Señora López trabaja en la cruz roja.", "La señora lópez trabaja en la Cruz Roja."], "<em>señora</em>, en minúscula; el apellido y la institución, con mayúscula."),
       (["Mis suegros llegan de Ecuador el viernes.", "Mis suegros llegan de ecuador el Viernes.", "Mis Suegros llegan de Ecuador el viernes."], "El país, con mayúscula; el día, con minúscula."),
       (["ÁREA DE ESPERA", "AREA DE ESPERA", "Área De Espera"], "Las mayúsculas llevan tilde cuando les corresponde."),
       (["En Año Nuevo comemos doce uvas.", "En año nuevo comemos doce uvas.", "En Año nuevo comemos Doce Uvas."], "<em>Año Nuevo</em> es una festividad."),
       (["El doctor Ramírez atiende en la avenida Kedzie.", "El Doctor Ramírez atiende en la Avenida Kedzie.", "El doctor ramírez atiende en la avenida kedzie."], "<em>doctor</em> y <em>avenida</em>, en minúscula; los nombres, con mayúscula."),
       (["Ángela llegó de Puerto Rico en diciembre.", "Angela llegó de puerto rico en diciembre.", "Ángela llegó de Puerto Rico en Diciembre."], "El nombre lleva tilde también en mayúscula; el mes, con minúscula."),
       (["Mi clase de inglés es los lunes y miércoles.", "Mi clase de Inglés es los Lunes y Miércoles.", "Mi clase de inglés es los Lunes y miércoles."], "Idiomas y días, con minúscula."),
       (["Celebramos el Día de los Muertos en noviembre.", "Celebramos el día de los muertos en Noviembre.", "Celebramos el Día de los Muertos en Noviembre."], "Festividad con mayúscula; mes con minúscula.")]
COMA = [(["Necesito harina, azúcar, huevos y mantequilla.", "Necesito harina, azúcar, huevos, y mantequilla.", "Necesito harina azúcar, huevos y mantequilla."], "Coma entre los elementos, pero no antes de <em>y</em>."),
        (["María, ¿puedes ayudarme?", "María ¿puedes ayudarme?", "María ¿puedes, ayudarme?"], "Al llamar a María, su nombre se separa con coma."),
        (["Mi sobrino, que vive en Texas, viene mañana.", "Mi sobrino que vive en Texas, viene mañana.", "Mi sobrino, que vive en Texas viene mañana."], "La explicación va entre dos comas."),
        (["El dueño de la tienda de la esquina me regaló el pan.", "El dueño de la tienda de la esquina, me regaló el pan.", "El dueño, de la tienda de la esquina me regaló el pan."], "No hay coma entre el sujeto y el verbo, aunque el sujeto sea largo."),
        (["Estaba cansada. Sin embargo, terminé el trabajo.", "Estaba cansada. Sin embargo terminé, el trabajo.", "Estaba cansada. Sin, embargo terminé el trabajo."], "Después de <em>sin embargo</em> al comienzo, va coma."),
        (["Si tiene tiempo, pase por mi casa.", "Si tiene tiempo pase, por mi casa.", "Si, tiene tiempo pase por mi casa."], "La parte que depende va primero: coma después."),
        (["Gracias, doctor.", "Gracias doctor.", "Gracias doctor,"], "Al dirigirse al doctor, coma."),
        (["Houston, 2 de febrero de 2026", "Houston 2 de febrero, de 2026", "Houston, 2, de febrero de 2026"], "Coma entre el lugar y el día."),
        (["No tengo tiempo, pero te ayudo.", "No tengo tiempo pero, te ayudo.", "No tengo, tiempo pero te ayudo."], "Coma antes de <em>pero</em>."),
        (["Mis hijos, mi esposo y yo fuimos al parque.", "Mis hijos mi esposo, y yo fuimos al parque.", "Mis hijos, mi esposo y yo, fuimos al parque."], "Enumeración dentro del sujeto, sin coma antes del verbo."),
        (["Por eso, llegamos tarde.", "Por eso llegamos, tarde.", "Por, eso llegamos tarde."], "Después de <em>por eso</em> al comienzo, va coma."),
        (["Señor Díaz, su mesa está lista.", "Señor Díaz su mesa, está lista.", "Señor, Díaz su mesa está lista."], "Al llamar al señor Díaz, coma después de su nombre."),
        (["Carmen, la enfermera, me tomó la presión.", "Carmen la enfermera me tomó, la presión.", "Carmen, la enfermera me tomó la presión."], "<em>la enfermera</em> explica quién es Carmen: va entre comas."),
        (["El curso empieza el lunes y termina en diciembre.", "El curso empieza el lunes, y termina en diciembre.", "El curso, empieza el lunes y termina en diciembre."], "Sin coma antes de <em>y</em> ni entre sujeto y verbo.")]
DIAL = [(["Estimada señora Morales:", "Estimada señora Morales,", "Estimada Señora Morales;"], "El saludo de una carta formal lleva dos puntos."),
        (["Querido Juan:", "Querido Juan,", "Querido Juan;"], "También el saludo de confianza: dos puntos."),
        (["Hola, Lupita:", "Hola Lupita,", "Hola, Lupita,"], "Coma porque se llama a Lupita, y dos puntos al final."),
        (["Atentamente,<br>Rosa Méndez", "Atentamente:<br>Rosa Méndez", "Atentamente;<br>Rosa Méndez"], "La despedida lleva coma y la firma va abajo."),
        (["—¿Vienes a cenar? —preguntó mi madre.", "\"¿Vienes a cenar?\", preguntó mi madre.", "—¿Vienes a cenar? —Preguntó mi madre."], "Raya pegada, y el verbo de decir en minúscula."),
        (["—Sí, ya voy —respondí.", "- Sí, ya voy - respondí.", "—Sí, ya voy, —respondí."], "La raya es más larga que el guion y va pegada a la palabra."),
        (["—Hace frío —dijo Pedro—. Cierra la ventana.", "—Hace frío —dijo Pedro. Cierra la ventana.", "—Hace frío. —dijo Pedro—. Cierra la ventana."], "Pedro sigue hablando: el punto va después de la segunda raya."),
        (["—¡Qué sorpresa! —exclamó Ana.", "—¡Qué sorpresa! —Exclamó Ana.", "—¡Qué sorpresa!, exclamó Ana."], "Después de <em>!</em>, el verbo de decir sigue en minúscula."),
        (["Mi abuela siempre decía: «A quien madruga, Dios lo ayuda».", "Mi abuela siempre decía, «A quien madruga, Dios lo ayuda».", "Mi abuela siempre decía «a quien madruga, Dios lo ayuda»:"], "Dos puntos antes de las palabras exactas de alguien."),
        (["Traiga estos documentos: identificación, recibo de luz y una foto.", "Traiga estos documentos, identificación, recibo de luz y una foto.", "Traiga: estos documentos identificación, recibo de luz y una foto."], "Dos puntos antes de una enumeración anunciada."),
        (["Saludos cordiales,<br>Departamento de Recursos Humanos", "Saludos Cordiales:<br>Departamento de recursos humanos", "saludos cordiales,<br>Departamento de Recursos Humanos"], "Despedida con coma; el nombre de la oficina, con mayúscula."),
        (["—No sé —contestó—. Pregúntale a tu papá.", "—No sé, contestó. Pregúntale a tu papá.", "\"No sé\", contestó, \"pregúntale a tu papá\"."], "En un diálogo, el español usa raya.")]
DIALOGO = ["—Mamá, ¿ya le escribiste a la maestra? —preguntó Daniel.", "—Sí, ya le mandé la nota —respondió Lucía—. Le dije que volvemos el miércoles.",
           "—¿Y qué te contestó?", "—Que no hay problema, pero que no olvides la tarea."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Quien vive en Estados Unidos lee inglés todos los días: en el trabajo, en la escuela de los hijos, en los letreros. El inglés tiene sus propias reglas, y a veces se nos pegan cuando escribimos en español. En inglés se escribe <em>Monday</em>, <em>January</em> y <em>Spanish</em> con mayúscula; una carta empieza con <em>Dear Mr. Smith,</em>; y el diálogo va entre comillas. En español, las tres cosas se hacen de otra manera. Esta lección le enseña la norma del español, la que se usa en el examen GED en español.</p>
<p>Ya sabe del Nivel 1 que la mayúscula va al comienzo de un texto y después de un punto. Además, llevan mayúscula inicial:</p>
{C.tabla("Palabras que llevan mayúscula", ["Con mayúscula", "Ejemplos"],
         [["Nombres y apellidos de personas", "Lucía Pérez · Daniel · el doctor Ramírez"], ["Lugares: ciudades, países, ríos, montañas", "Chicago · México · el río Bravo · los Andes"],
          ["Instituciones, empresas y organismos", "Truman College · Departamento de Salud · Cruz Roja"], ["Festividades", "Navidad · Año Nuevo · Día de Acción de Gracias · Día de los Muertos"]])}
<p>En cambio, el español escribe con minúscula muchas palabras que el inglés escribe con mayúscula:</p>
{C.tabla("Palabras que van con minúscula en español", ["En español, con minúscula", "Ejemplos", "En inglés"],
         [["Días de la semana", "el lunes, el sábado", "Monday, Saturday"], ["Meses", "en enero, el 5 de octubre", "January, October"],
          ["Idiomas y nacionalidades", "hablo español · es mexicano · la comida cubana", "Spanish, Mexican, Cuban"], ["Estaciones del año", "en verano, este invierno", "summer, winter"],
          ["calle, río, doctor… delante del nombre", "la calle Ashland · el río Misisipi · la doctora López", "Ashland Street, Dr. López"]])}
{C.caja("tip", "Las mayúsculas llevan tilde", "<p>Si la palabra lleva tilde, la lleva también en mayúscula: <em>Ángela, Óscar, ATENCIÓN, ÁREA DE ESPERA</em>.</p>")}
{P("Compruebe", "¿Cuál está bien escrita?", ["El Martes tengo cita.", "El martes tengo cita."], 1, {0: "Los días van con minúscula en español."}, "<strong>el martes</strong>: con minúscula.")}
{P("Compruebe", "¿Cuál está bien escrita?", ["Mi esposo habla español.", "Mi esposo habla Español."], 0, {1: "Los idiomas van con minúscula."}, "<strong>español</strong>, con minúscula.")}"""

    s2 = f"""{C.tabla("Usos de la coma", ["Se usa coma…", "Ejemplo"],
         [["En una enumeración, entre los elementos. Antes del último, si va <em>y, o, ni</em>, no se pone coma.", "Compré pan, leche, huevos y café."],
          ["Al llamar a alguien por su nombre o su cargo.", "Ana, ven a comer. · Gracias, doctora."], ["Para encerrar una explicación que se podría quitar.", "Mi vecino, que es electricista, arregló la luz."],
          ["Después de <em>sin embargo, por eso, además, es decir</em>, al comienzo.", "Llovía mucho. Sin embargo, salimos."], ["Después de la parte que depende, si va primero (Lección 2.3).", "Cuando llegué, todos dormían."],
          ["En las fechas, entre el lugar y el día.", "Chicago, 5 de octubre de 2026"]])}
{C.caja("ojo", "Dos comas que no van", "<ul><li><strong>Entre el sujeto y el verbo:</strong> «Mis hermanos mayores, viven en Texas» está mal, aunque el sujeto sea largo.</li>"
        "<li><strong>Antes de la <em>y</em> final de una enumeración:</strong> en inglés se escribe <em>bread, milk, and eggs</em>; en español, <em>pan, leche y huevos</em>.</li></ul>")}
{P("Compruebe", "¿Cuál tiene bien las comas?", ["Compré pan, leche, y huevos.", "Compré pan, leche y huevos."], 1, {0: "Antes de la y final no va coma."}, "<strong>pan, leche y huevos</strong>: sin coma antes de y.")}
{P("Compruebe", "¿Cuál tiene bien las comas?", ["Mi vecino, que es electricista, arregló la luz.", "Mi vecino que es electricista, arregló la luz."], 0, {1: "La explicación va entre dos comas, no con una sola."}, "La explicación va <strong>entre dos comas</strong>.")}"""

    s3 = f"""<p>Los <strong>dos puntos</strong> ( : ) detienen la lectura para anunciar lo que viene. Se usan:</p>
<ul><li><strong>Después del saludo de una carta o un correo:</strong> <em>Estimada señora Morales:</em> · <em>Querida Ana:</em> · <em>Hola, Pedro:</em>. El texto empieza en la línea siguiente, con mayúscula.</li>
<li><strong>Antes de una enumeración anunciada:</strong> <em>Necesito tres cosas: paciencia, tiempo y práctica.</em> Lo que sigue va con minúscula.</li>
<li><strong>Antes de las palabras exactas de alguien:</strong> <em>Mi madre siempre decía: «Estudia, que nadie te lo quita».</em></li></ul>
{C.caja("ojo", "El saludo con coma es inglés", "<p><em>Dear Mrs. Morales,</em> lleva coma en inglés, pero en español el saludo lleva <strong>dos puntos</strong>. En <em>Hola, Pedro:</em> hay una coma porque se llama a Pedro, y los dos puntos al final.</p>")}
{C.caja("tip", "La despedida", "<p>Las despedidas como <em>Atentamente</em>, <em>Saludos cordiales</em> o <em>Un abrazo</em> van seguidas de <strong>coma</strong>, y la firma va en la línea siguiente.</p>")}
<h3>La raya en el diálogo</h3>
<p>En español, el diálogo de una historia se escribe con <strong>raya</strong> ( — ), una línea más larga que el guion ( - ). Tres reglas:</p>
<ol><li>Cada vez que habla un personaje, la línea empieza con raya, pegada a la primera palabra: <em>—Ya llegué.</em></li>
<li>Las palabras del narrador van entre rayas, y si son un verbo de decir (<em>dijo, preguntó, respondió</em>) empiezan con minúscula: <em>—Ya llegué —dijo Ana.</em></li>
<li>Si el personaje sigue hablando después del narrador, el signo de puntuación va después de la segunda raya: <em>—Ya llegué —dijo Ana—. ¿Hay café?</em></li></ol>
{C.caja("tip", "¿Y las comillas?", "<p>Las comillas ( « » o \" \" ) sirven para citar las palabras de alguien dentro de un texto: <em>El letrero decía «Cerrado los domingos».</em> Para los diálogos de una historia, el español usa la raya.</p>")}
{P("Compruebe", "¿Cómo empieza una carta formal en español?", ["Estimada señora Morales,", "Estimada señora Morales:"], 1, {0: "La coma en el saludo es del inglés."}, "<strong>Estimada señora Morales:</strong>, con dos puntos.")}
{P("Compruebe", "¿Cuál está bien escrita?", ["—Ya llegué —dijo Ana.", "—Ya llegué —Dijo Ana."], 0, {1: "El verbo de decir va en minúscula."}, "<strong>—dijo Ana</strong>, en minúscula.")}"""

    s4 = f"""<p>Lea la nota y el diálogo como un «detective de puntuación». En su cuaderno, explique por qué lleva mayúscula cada palabra que la tiene en medio de una oración, y para qué sirven los dos puntos, las comas y las rayas. Luego compare con las respuestas.</p>
<div class="texto-lectura carta"><p style="text-align:right">Chicago, 5 de octubre de 2026</p>
<p>Estimada señora Morales:</p>
<p>Le escribo para informarle que mi hijo, Daniel Pérez, no podrá asistir a clases el lunes 12 y el martes 13 de octubre. Viajaremos a Milwaukee para visitar a su abuela, que está enferma. Daniel llevará sus libros, su cuaderno y las tareas de la semana.</p>
<p>Le agradezco su comprensión.</p>
<p>Atentamente,<br>Lucía Pérez</p></div>
{LE.escuchar(" ".join(DIALOGO), "Escuchar el diálogo")}
<div class="texto-lectura">{"".join(f"<p>{d}</p>" for d in DIALOGO)}</div>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary>
<ul><li><strong>Mayúsculas:</strong> Chicago, Milwaukee (lugares); Morales, Daniel Pérez, Lucía Pérez (personas). Van en minúscula <em>señora, lunes, martes</em> y <em>octubre</em>.</li>
<li><strong>Comas:</strong> <em>Chicago, 5 de octubre</em> (fecha); <em>mi hijo, Daniel Pérez, no podrá</em> (explicación); <em>su abuela, que está enferma</em> (explicación); <em>sus libros, su cuaderno y</em> (enumeración, sin coma antes de y); <em>Atentamente,</em> (despedida); <em>Mamá, ¿ya…?</em> y <em>Sí, ya…</em> (llamar a alguien y separar el sí).</li>
<li><strong>Dos puntos:</strong> después del saludo <em>Estimada señora Morales:</em>; el texto sigue con mayúscula en la línea siguiente.</li>
<li><strong>Rayas:</strong> cada intervención empieza con raya; <em>—preguntó Daniel</em> y <em>—respondió Lucía—</em> son palabras del narrador; en <em>—respondió Lucía—.</em> el punto va después de la segunda raya porque Lucía sigue hablando.</li></ul></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · corrija el mensaje</span>
<p>Este correo tiene <strong>once errores</strong> de mayúsculas y puntuación, casi todos copiados del inglés. Cópielo corregido en su cuaderno.</p>
<div class="texto-lectura carta"><p>Dear Señor García,</p><p>le escribo para confirmar mi cita del Jueves 9 de Octubre. Necesito llevar tres documentos, mi identificación, el comprobante de domicilio, y la carta del banco. Mi esposa que habla Inglés me va a acompañar.</p><p>Gracias<br>Roberto Díaz</p></div>
<details><summary><strong>Ver la versión corregida</strong></summary>
<div class="texto-lectura carta"><p>Estimado señor García:</p><p>Le escribo para confirmar mi cita del jueves 9 de octubre. Necesito llevar tres documentos: mi identificación, el comprobante de domicilio y la carta del banco. Mi esposa, que habla inglés, me va a acompañar.</p><p>Gracias,<br>Roberto Díaz</p></div>
<p><strong>Los once cambios:</strong> Dear → Estimado · Señor → señor · coma del saludo → dos puntos · le → Le · Jueves → jueves · Octubre → octubre · coma antes de la lista → dos puntos · sin coma antes de <em>y</em> · comas en <em>, que habla inglés,</em> · Inglés → inglés · coma después de la despedida <em>Gracias,</em>.</p></details>
<p>Si tiene con quién practicar: busquen juntos un correo o una nota de la escuela escritos en español y revisen sus mayúsculas y sus comas.</p></div>"""

    secciones = [("s1", "Mayúscula y minúscula", s1), ("s2", "La coma", s2), ("s3", "Los dos puntos y la raya", s3), ("s4", "Lectura: una nota a la maestra", s4)]
    tarea = [("Una nota de verdad.", "Escriba una nota formal a la escuela de sus hijos, a su trabajo o a una oficina: lugar y fecha, saludo con dos puntos, dos párrafos cortos, despedida y firma. Incluya una enumeración y una explicación entre comas."),
             ("Un diálogo.", "Escriba un diálogo de seis líneas entre dos personas que planean una fiesta. Use raya, al menos dos verbos de decir y una pregunta."),
             ("Cazador de anglicismos.", "Busque en anuncios, menús o letreros en español de su barrio dos palabras con mayúscula «a la inglesa» (meses, días, idiomas) y escriba cómo deberían ir.")]
    quiz = [
        ("¿Cuál va con minúscula en español?", ["el nombre de un mes", "el nombre de un país", "el nombre de una persona"], 0, {1: "Los países llevan mayúscula.", 2: "Las personas llevan mayúscula."}, "Los <strong>meses</strong> van con minúscula."),
        ("¿Cuál está bien escrita?", ["Celebramos el Día de los Muertos en noviembre.", "Celebramos el Día de los Muertos en Noviembre."], 0, {1: "El mes va con minúscula."}, "Festividad con mayúscula; <strong>noviembre</strong>, con minúscula."),
        ("¿Cuál está bien escrita?", ["La doctora López atiende hoy.", "La Doctora López atiende hoy."], 0, {1: "doctora va con minúscula delante del nombre."}, "<strong>la doctora López.</strong>"),
        ("¿Cuál tiene bien las comas?", ["Mis hermanos mayores viven en Texas.", "Mis hermanos mayores, viven en Texas."], 0, {1: "No va coma entre el sujeto y el verbo."}, "Sin coma entre <strong>sujeto y verbo</strong>."),
        ("¿Cuál tiene bien las comas?", ["Ana, ven a comer.", "Ana ven, a comer."], 0, {1: "La coma separa el nombre de la persona a quien se llama."}, "<strong>Ana, ven a comer.</strong>"),
        ("¿Cuál tiene bien la coma?", ["Llovía. Sin embargo, salimos.", "Llovía. Sin embargo salimos."], 0, {1: "Al comienzo, sin embargo lleva coma después."}, "Coma después de <strong>sin embargo</strong>."),
        ("¿Qué signo va después del saludo de una carta en español?", ["los dos puntos", "la coma", "el punto y coma"], 0, {1: "La coma es del inglés.", 2: "No se usa en el saludo."}, "<strong>Los dos puntos.</strong>"),
        ("¿Qué signo va después de <em>Atentamente</em>?", ["la coma", "los dos puntos", "el punto"], 0, {1: "Los dos puntos van en el saludo.", 2: "No va punto."}, "<strong>La coma</strong>, y la firma abajo."),
        ("¿Cuál está bien escrita?", ["—Hace frío —dijo Pedro—. Cierra la ventana.", "—Hace frío —dijo Pedro. Cierra la ventana."], 0, {1: "Falta la raya que cierra las palabras del narrador."}, "El punto va <strong>después de la segunda raya</strong>."),
        ("En un diálogo de una historia, el español usa…", ["la raya ( — )", "las comillas ( \" \" )", "el guion ( - )"], 0, {1: "Las comillas citan palabras dentro de un texto.", 2: "El guion es más corto."}, "<strong>La raya.</strong>"),
    ]
    filas = [
        ("Mayúsculas", "Uso minúscula en días, meses, idiomas y cargos, y mayúscula en nombres, lugares, instituciones y fiestas.", "A veces se me pega la mayúscula del inglés.", "No distingo los casos (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Comas", "Pongo coma en enumeraciones, llamadas y explicaciones, y nunca entre sujeto y verbo.", "Pongo coma antes de la y final.", "No sé dónde va (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Cartas y diálogos", "Escribo el saludo con dos puntos, la despedida con coma y el diálogo con raya.", "Dudo dónde va el punto con la raya.", "Escribo cartas y diálogos a la inglesa (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya escribe las mayúsculas y los signos según la norma del español. En la próxima lección verá <strong>la tilde y las letras que suenan igual</strong>.</p>"
    glosario = [("Enumeración", "Lista de elementos separados por comas."), ("Explicación entre comas", "Información que se puede quitar sin cambiar la idea principal."),
                ("Raya", "Signo largo ( — ) que marca quién habla en un diálogo."), ("Anglicismo", "Uso copiado del inglés: Martes con mayúscula, Dear… con coma.")]
    conexion = ("<p>En la Lección 2.3 vio la coma de las oraciones compuestas y complejas. Hoy completará los usos de la coma y verá otros signos que el inglés usa de otra manera.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, y si puede, una nota o un correo en español para revisar.</p>")
    estd = LE.estandares(["L.2.1", "L.2.4"], base=["W.3"])
    return C.pagina_leccion(N, LE.titulo(N), "La norma del español, no la del inglés.", ["Ortografía", "Puntuación"],
                            ["<strong>Usar</strong> la mayúscula y la minúscula según la norma del español.", "<strong>Poner</strong> la coma en su lugar, y no ponerla entre sujeto y verbo.",
                             "<strong>Escribir</strong> el saludo y la despedida de una carta.", "<strong>Puntuar</strong> un diálogo con raya."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-2", LE.titulo("3-2")), glosario, P)


def practica():
    def banco(d, enun, pista):
        return [{"enun": enun, "ops": ops, "ok": 0, "pista": pista, "exp": e} for ops, e in d]
    ma = banco(MAY, "¿Cuál está bien escrita?", "Revise los días, los meses, los idiomas y las palabras como señora o doctor.")
    co = banco(COMA, "¿Cuál tiene las comas en su lugar?", "¿Hay una coma entre el sujeto y el verbo? ¿O antes de la y final?")
    di = banco(DIAL, "¿Cuál está bien escrita?", "Saludo con dos puntos, despedida con coma, diálogo con raya y verbo de decir en minúscula.")
    mods = [("mayusculas", "Mayúscula o minúscula", C.om("m1", "Elija la versión bien escrita.")),
            ("comas", "Las comas", C.om("m2", "Elija la versión con las comas en su lugar.")),
            ("cartas-dialogos", "Cartas y diálogos", C.om("m3", "Elija la versión puntuada según la norma del español."))]
    js = C.js_datos("MA", ma) + C.js_datos("CO", co) + C.js_datos("DI", di) + 'creaBanco("m1", MA);\ncreaBanco("m2", CO);\ncreaBanco("m3", DI);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
