# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 2.1 · Comillas, cursiva, dos puntos y punto y coma.
Fuente: clases_leng3/clase_2-1.html (GEDparaHispanos) y gramatica/n3-l2-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_2_1.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "2-1"


def TI(t):
    return f'<em class="pt-ti">{t}</em>'


def CO_(t):
    return f'<span class="pt-co">«{t}»</span>'


def SI(t):
    return f'<b class="pt-si">{t}</b>'


BOLETIN = [
    f"Este mes, la biblioteca de la calle 26 recomienda tres clásicos en español{SI(':')} {TI('Platero y yo')}, de Juan Ramón Jiménez{SI(';')} {TI('La Edad de Oro')}, de José Martí{SI(';')} y {TI('Cuentos de la selva')}, de Horacio Quiroga.",
    f"En {TI('La Edad de Oro')}, que Martí escribió para los niños de América en 1889, aparece el poema {CO_('Los zapaticos de rosa')}. La bibliotecaria, la señora Delgado, lo explica así{SI(':')} {CO_('Es un libro para niños que los adultos también disfrutan')}.",
    f"Los libros se pueden pedir de lunes a sábado{SI(';')} los préstamos duran tres semanas. Además, el boletín del mes de octubre trae un artículo titulado {CO_('Cómo leer con sus hijos')}, escrito por una maestra de la escuela del barrio.",
]
TIT = [(["Mi libro favorito es <em>Cien años de soledad</em>.", "Mi libro favorito es <em>Cien Años de Soledad</em>.", "Mi libro favorito es «Cien Años De Soledad»."], "Libro completo: cursiva, y mayúscula solo en la primera palabra."),
       (["Lea el capítulo «El trabajo de la tierra».", "Lea el capítulo <em>El Trabajo de la Tierra</em>.", "Lea el capítulo «El Trabajo De La Tierra»."], "Un capítulo es parte de un libro: entre comillas."),
       (["Compré <em>La Opinión</em> en el quiosco.", "Compré «la opinión» en el quiosco.", "Compré <em>La opinión</em> en el quiosco."], "Nombre de un periódico: cursiva y mayúscula en las palabras importantes."),
       (["Mi canción preferida es «Guantanamera».", "Mi canción preferida es <em>GUANTANAMERA</em>.", "Mi canción preferida es Guantanamera, sin marcas."], "Una canción, que es parte de un disco, va entre comillas."),
       (["Anoche vimos la película <em>Coco</em>.", "Anoche vimos la película «Coco».", "Anoche vimos la película coco."], "Una película es una obra completa: cursiva."),
       (["El artículo «Cómo ahorrar en invierno» salió en <em>El Nuevo Herald</em>.", "El artículo <em>Cómo Ahorrar en Invierno</em> salió en «El Nuevo Herald».", "El artículo «Cómo Ahorrar En Invierno» salió en <em>el nuevo herald</em>."], "El artículo (una parte) entre comillas; el periódico (la obra completa) en cursiva."),
       (["Martí publicó <em>Versos sencillos</em> en 1891.", "Martí publicó <em>Versos Sencillos</em> en 1891.", "Martí publicó «Versos Sencillos» en 1891."], "Libro completo: cursiva y mayúscula solo en la primera palabra."),
       (["El poema «Los zapaticos de rosa» está en <em>La Edad de Oro</em>.", "El poema <em>Los Zapaticos de Rosa</em> está en «La Edad de Oro».", "El poema «Los Zapaticos De Rosa» está en La Edad de Oro."], "El poema va entre comillas y el libro en cursiva. <em>La Edad de Oro</em> lleva mayúscula en <em>Edad</em> y <em>Oro</em> porque nació como una revista mensual, y los nombres de revistas siguen la regla de los periódicos."),
       (["A mano escribí: <u>Platero y yo</u>.", "A mano escribí: Platero Y Yo.", "A mano escribí: \"PLATERO Y YO\"."], "A mano, el título de un libro se subraya."),
       (["El episodio «La gran sorpresa» fue el mejor de la serie.", "El episodio <em>La Gran Sorpresa</em> fue el mejor de la serie.", "El episodio la gran sorpresa fue el mejor de la serie."], "Un episodio es parte de una serie: entre comillas.")]
DP = [(["Necesito tres documentos: el pasaporte, una factura y una foto.", "Necesito: el pasaporte, una factura y una foto.", "Necesito tres documentos, el pasaporte: una factura y una foto."], "Los dos puntos anuncian la lista después de «tres documentos»."),
      (["El letrero decía: «Prohibido fumar».", "El letrero decía «Prohibido fumar:».", "El letrero: decía «Prohibido fumar»."], "Los dos puntos anuncian la cita textual."),
      (["Llegué tarde por una razón: el tren se descompuso.", "Llegué tarde por: una razón el tren se descompuso.", "Llegué: tarde por una razón, el tren se descompuso."], "Los dos puntos anuncian la explicación."),
      (["Querida tía:", "Querida tía,", "Querida tía;"], "El saludo de una carta lleva dos puntos en español."),
      (["Mis hijos se llaman Ana, Luis y Pedro.", "Mis hijos se llaman: Ana, Luis y Pedro.", "Mis hijos: se llaman Ana, Luis y Pedro."], "Sin una palabra que anuncie la lista, no hacen falta los dos puntos."),
      (["Mi madre siempre me dice: «Estudia, que nadie te lo quita».", "Mi madre siempre me dice, «Estudia, que nadie te lo quita».", "Mi madre siempre me dice «Estudia, que nadie te lo quita.»"], "Dos puntos antes de la cita y punto después de las comillas."),
      (["Solo me falta una cosa: aprobar el examen de Ciencias.", "Solo me falta una cosa; aprobar el examen de Ciencias.", "Solo me falta: una cosa aprobar el examen de Ciencias."], "Los dos puntos anuncian qué es esa cosa."),
      (["Compramos pan, leche y huevos.", "Compramos: pan, leche y huevos.", "Compramos pan: leche y huevos."], "No se ponen dos puntos entre el verbo y lo que sigue.")]
SIG = {";": "punto y coma ( ; )", ",": "coma ( , )", ":": "dos puntos ( : )"}
PC = [("Llovió toda la noche ___ la calle amaneció inundada.", ";", "Dos oraciones completas muy relacionadas: punto y coma. Con coma sería una oración corrida."),
      ("Vinieron Ana, de Puebla ___ Luis, de Lima; y Rosa, de Cali.", ";", "La lista ya tiene comas dentro: los elementos se separan con punto y coma."),
      ("Estudió mucho ___ sin embargo, no aprobó.", ";", "Antes de <em>sin embargo</em> que une dos oraciones: punto y coma."),
      ("Para la receta necesita tres cosas ___ arroz, frijoles y cebolla.", ":", "Una lista anunciada por «tres cosas»: dos puntos."),
      ("Compré manzanas ___ peras y uvas.", ",", "Una lista simple, sin comas dentro: coma."),
      ("El jefe nos dijo ___ «Mañana se trabaja».", ":", "Antes de una cita textual: dos puntos."),
      ("La tienda abre a las nueve ___ por lo tanto, llegue temprano.", ";", "Antes de <em>por lo tanto</em> que une dos oraciones: punto y coma."),
      ("Visitamos Chicago, en Illinois ___ Milwaukee, en Wisconsin; y Detroit, en Michigan.", ";", "Lista con comas dentro: punto y coma."),
      ("No pude ir por un motivo ___ estaba enfermo.", ":", "Anuncia la explicación: dos puntos."),
      ("El examen es mañana ___ hoy repaso todo.", ";", "Dos oraciones completas relacionadas: punto y coma.")]
MA = [(["El examen es el martes 14 de noviembre.", "El examen es el Martes 14 de Noviembre.", "El examen es el martes 14 de Noviembre."], "Los días y los meses van en minúscula."),
      (["Mi esposo es salvadoreño y habla inglés.", "Mi esposo es Salvadoreño y habla Inglés.", "Mi esposo es salvadoreño y habla Inglés."], "Las nacionalidades y los idiomas van en minúscula."),
      (["Ayer habló el alcalde de Chicago.", "Ayer habló el Alcalde de Chicago.", "Ayer habló el alcalde de chicago."], "El cargo en minúscula; el nombre de la ciudad, en mayúscula."),
      (["Trabajo en la Universidad de Chicago.", "Trabajo en la universidad de Chicago.", "Trabajo en la Universidad De Chicago."], "El nombre de una institución lleva mayúscula en sus palabras importantes."),
      (["Vivo en el norte de la ciudad.", "Vivo en el Norte de la ciudad.", "Vivo en el NORTE de la ciudad."], "Los puntos cardinales van en minúscula."),
      (["Mis abuelos viven en América del Sur.", "Mis abuelos viven en América del sur.", "Mis abuelos viven en américa del Sur."], "Cuando forma parte de un nombre propio, el punto cardinal va en mayúscula."),
      (["ÁFRICA ES UN CONTINENTE MUY GRANDE.", "AFRICA ES UN CONTINENTE MUY GRANDE.", "ÀFRICA ES UN CONTINENTE MUY GRANDE."], "Las mayúsculas llevan tilde: <em>Á</em>."),
      (["La doctora Pérez me atendió en el hospital.", "La Doctora Pérez me atendió en el hospital.", "La doctora pérez me atendió en el hospital."], "El título en minúscula; el apellido, en mayúscula."),
      (["Estudio para el GED en la biblioteca.", "Estudio para el ged en la biblioteca.", "Estudio para el Ged en la biblioteca."], "Las siglas van en mayúscula."),
      (["En primavera abren el mercado del barrio.", "En Primavera abren el mercado del barrio.", "En primavera abren el Mercado del barrio."], "Las estaciones del año van en minúscula.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Mire este título como lo escribiría alguien acostumbrado al inglés: «El Viejo Y El Mar». En español se escribe <em>El viejo y el mar</em>: en cursiva y con mayúscula solo en la primera palabra. La puntuación y las mayúsculas cambian de un idioma a otro, y quien escribe en los dos suele mezclarlas. Esta lección le da las reglas del español para los casos que más se equivocan.</p>
<p>En el Nivel 2 aprendió que en español:</p>
<ul><li>El saludo de una carta lleva <strong>dos puntos</strong>, no coma: «Estimada señora Morales:».</li>
<li>El diálogo se marca con <strong>raya</strong>: «—¿Vienes mañana? —preguntó Ana.»</li>
<li>Las <strong>mayúsculas</strong> van al principio de la oración y en los nombres propios.</li></ul>
<p>Y en la Lección 1.3 vio que el <strong>punto y coma</strong> puede separar dos oraciones completas muy relacionadas. Hoy amplía esas herramientas.</p>"""

    s2 = f"""<p>La regla depende de si el título es de una <strong>obra completa</strong> o de una <strong>parte</strong> de ella:</p>
{C.tabla("Cuándo se escribe un título en cursiva y cuándo entre comillas", ["Se escribe en…", "Para…", "Ejemplos"],
         [["<em>Cursiva</em>", "Obras completas: libros, películas, periódicos, revistas, discos, programas de televisión, cuadros.", "<em>Platero y yo</em> · <em>La Opinión</em> · <em>Cien años de soledad</em>"],
          ["«Comillas»", "Partes de una obra: un artículo de un periódico, un capítulo, un poema de un libro, una canción de un disco, un episodio.", "el poema «Los zapaticos de rosa», de <em>La Edad de Oro</em>"]])}
{C.caja("tip", "¿Y si escribe a mano?", "<p>A mano no hay cursiva: en su lugar se <u>subraya</u> el título. En la computadora, en el celular o en el GED, use la cursiva (o las comillas, si el programa no la permite).</p>")}
{C.caja("ojo", "La mayúscula del título", "<p>En español solo lleva mayúscula la <strong>primera palabra</strong> del título y los nombres propios que contenga: <em>El amor en los tiempos del cólera</em>, no «El Amor en los Tiempos del Cólera». La única excepción son los nombres de periódicos y revistas, que llevan mayúscula en las palabras importantes: <em>El Nuevo Herald</em>, <em>La Opinión</em>.</p>")}
{P("Título 1", "¿Cómo se escribe el título de un artículo de periódico?", ["En cursiva", "En mayúsculas", "Entre comillas"], 2, {0: "La cursiva es para obras completas.", 1: "Las mayúsculas no marcan títulos."}, "Un artículo es una parte del periódico: <strong>entre comillas</strong>.")}
{P("Título 2", "¿Cuál está bien escrita?", ["Mi libro favorito es <em>Cien Años de Soledad</em>.", "Mi libro favorito es <em>Cien años de soledad</em>.", "Mi libro favorito es «Cien Años De Soledad»."], 1, {0: "Solo la primera palabra lleva mayúscula.", 2: "Un libro completo va en cursiva, y sobran mayúsculas."}, "Libro completo: cursiva, y mayúscula solo en la primera palabra.")}"""

    s3 = f"""<p>Las comillas encierran las <strong>palabras exactas</strong> de otra persona. Es lo que hará en el GED cuando cite la evidencia de un texto:</p>
<p class="formula">En un discurso de 1891, José Martí pidió una república «con todos, y para el bien de todos».</p>
<p class="fuente">José Martí, discurso en Tampa, Florida, 26 de noviembre de 1891.</p>
<p>En español hay tres clases de comillas. Se usan primero las angulares, y las otras sirven para una cita dentro de otra cita:</p>
<p class="frase">« » angulares · “ ” inglesas · ‘ ’ simples</p>
<p class="formula">Rosa me contó: «Mi abuela siempre decía “más vale tarde que nunca”».</p>
{C.caja("ojo", "El punto va después de las comillas", "<p>En español el punto, la coma y el punto y coma van <strong>fuera</strong>, después de cerrar las comillas: «…para el bien de todos»<strong>.</strong> En inglés es al revés (\"…of all.\"), y por eso se confunde mucho.</p>")}
{C.caja("tip", "Otros usos", "<p>Las comillas también marcan una palabra usada con un sentido especial o irónico: «Su “ayuda” fue dejarme todo el trabajo». Las palabras de otro idioma, en cambio, van en cursiva, sin comillas: «Trabajo en el <em>deli</em> de la esquina».</p>")}
{P("Comillas 1", "¿Cuál está bien puntuada?", ["Martí pidió una república «con todos, y para el bien de todos.»", "Martí pidió una república: con todos, y para el bien de todos.", "Martí pidió una república «con todos, y para el bien de todos»."], 2, {0: "El punto va después de cerrar las comillas.", 1: "Las palabras exactas van entre comillas."}, "Comillas para la cita y el punto <strong>después</strong> de cerrarlas.")}"""

    s4 = f"""<p>Los dos puntos <strong>anuncian</strong> lo que viene después. Se usan en cuatro casos:</p>
{C.tabla("Usos de los dos puntos", ["Uso", "Ejemplo"],
         [["Antes de una enumeración anunciada.", "Para el trámite necesita tres documentos<strong>:</strong> el pasaporte, la factura de la luz y una foto."],
          ["Antes de una cita textual.", "El letrero decía<strong>:</strong> «Prohibido estacionar»."],
          ["Antes de una explicación o una conclusión.", "No fui a la fiesta por una razón<strong>:</strong> tenía que trabajar."],
          ["En el saludo de una carta.", "Estimado señor Ramírez<strong>:</strong>"]])}
{C.caja("ojo", "No entre el verbo y lo que sigue", "<p>«Compré<s>:</s> pan, leche y huevos» está mal. Los dos puntos van solo si antes se anuncia la lista: «Compré tres cosas: pan, leche y huevos». Sin anunciarla: «Compré pan, leche y huevos».</p>")}
{C.caja("tip", "Después de los dos puntos", "<p>Se sigue en minúscula, salvo que venga una cita (dijo: «Ya voy») o el texto de una carta, que empieza en otra línea con mayúscula.</p>")}
{P("Dos puntos 1", "¿Cuál usa bien los dos puntos?", ["Necesito: pan, leche y huevos.", "Necesito tres cosas: pan, leche y huevos.", "Necesito pan: leche y huevos."], 1, {0: "Quedaron pegados al verbo.", 2: "Parten la lista por la mitad."}, "«Tres cosas» anuncia la lista.")}
{P("Dos puntos 2", "¿Qué anuncian los dos puntos en «No fui por una razón: tenía fiebre»?", ["Una cita textual", "Una lista de cosas", "Una explicación"], 2, {0: "No hay palabras de otra persona.", 1: "Solo hay una razón."}, "Anuncian la <strong>explicación</strong>: tenía fiebre.")}"""

    s5 = f"""<p>El punto y coma es una pausa más fuerte que la coma y más débil que el punto. Tiene tres usos:</p>
{C.tabla("Usos del punto y coma", ["Uso", "Ejemplo"],
         [["Separar dos oraciones completas muy relacionadas (Lección 1.3).", "Llovió toda la noche<strong>;</strong> la calle amaneció inundada."],
          ["Separar los elementos de una lista que ya tienen comas dentro.", "Vinieron Ana, de Puebla<strong>;</strong> Luis, de Lima<strong>;</strong> y Rosa, de Cali."],
          ["Antes de <em>sin embargo, por lo tanto, por eso, además</em> cuando unen dos oraciones (después va coma).", "Estudió mucho<strong>;</strong> sin embargo, no aprobó el examen."]])}
{C.caja("tip", "¿Por qué en la lista?", "<p>Sin punto y coma, «Vinieron Ana, de Puebla, Luis, de Lima, y Rosa, de Cali» parece una lista de seis cosas. El punto y coma agrupa a cada persona con su ciudad.</p>")}
{P("Signo 1", "«Estudió mucho ___ sin embargo, no aprobó.» ¿Qué signo va?", [SIG[","], SIG[";"], SIG[":"]], 1, {0: "Con coma sería una oración corrida.", 2: "No se anuncia nada."}, "Antes de <em>sin embargo</em> que une dos oraciones: punto y coma.")}
{P("Signo 2", "«Para la receta necesita tres cosas ___ arroz, frijoles y cebolla.» ¿Qué signo va?", [SIG[";"], SIG[","], SIG[":"]], 2, {0: "No son dos oraciones completas.", 1: "«Tres cosas» anuncia la lista."}, "Una lista anunciada: dos puntos.")}"""

    s6 = f"""<p>El inglés usa muchas más mayúsculas que el español. Estas palabras van en <strong>minúscula</strong> en español:</p>
{C.tabla("Palabras que van en minúscula en español y en mayúscula en inglés", ["En minúscula", "Ejemplo en español", "En inglés sería…"],
         [["Días de la semana y meses", "el lunes 5 de octubre", "Monday, October"], ["Idiomas y nacionalidades", "habla español; es mexicana", "Spanish, Mexican"],
          ["Cargos y títulos", "el alcalde, la doctora Pérez, el presidente", "the Mayor, Doctor Pérez"], ["Puntos cardinales", "vivo en el norte de la ciudad", "the North Side"],
          ["Las palabras de un título, menos la primera", "<em>El viejo y el mar</em>", "<em>The Old Man and the Sea</em>"]])}
<p>Van en <strong>mayúscula</strong>: los nombres de instituciones (el Concejo Municipal, la Universidad de Chicago), las siglas (GED, ONU) y los puntos cardinales cuando forman parte de un nombre (América del Norte).</p>
{C.caja("ojo", "Las mayúsculas llevan tilde", "<p><strong>África</strong>, <strong>Óscar</strong>, <strong>ATENCIÓN</strong>. Quitarle la tilde a una mayúscula es un error.</p>")}
{P("Mayúscula 1", "¿Cuál está bien escrita?", ["El Lunes 5 de Octubre hablé con el Alcalde.", "El lunes 5 de Octubre hablé con el Alcalde.", "El lunes 5 de octubre hablé con el alcalde."], 2, {0: "Días, meses y cargos van en minúscula.", 1: "Meses y cargos van en minúscula."}, "Todo en minúscula: día, mes y cargo.")}
{P("Mayúscula 2", "¿Cuál está bien escrita?", ["Mi vecina es Colombiana y habla Inglés.", "Mi vecina es colombiana y habla inglés.", "Mi vecina es colombiana y habla Inglés."], 1, {0: "Nacionalidades e idiomas van en minúscula.", 2: "Los idiomas van en minúscula."}, "Nacionalidad e idioma en minúscula.")}"""

    bol = "".join(f"<p>{p}</p>" for p in BOLETIN)
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in BOLETIN)
    s7 = f"""<p>Lea el boletín de una biblioteca de barrio. Después pulse <strong>Mostrar la puntuación</strong>: verá marcados los títulos, las comillas, los dos puntos y los puntos y coma. Para cada marca, explique en su cuaderno qué regla de esta lección se aplica.</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-p21" aria-pressed="false">Mostrar la puntuación</button></p>
<div class="articulo lectura-pt" id="lect-21"><p><strong>Recomendaciones de la biblioteca</strong></p>{bol}</div>
<p class="leyenda-partes" id="ley-21"><span style="background:#dbeafe">Título en cursiva</span><span style="background:#dcfce7">Entre comillas</span><span style="background:#fef3c7">Dos puntos y punto y coma</span></p>
<p class="fuente">La biblioteca, la señora Delgado y el boletín son inventados para la lección. Los libros y sus autores son reales.</p>
<script>(function(){{var b=document.getElementById("btn-p21"),t=document.getElementById("lect-21"),l=document.getElementById("ley-21");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-pt");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar la puntuación":"Mostrar la puntuación";}});}})();</script>
<h3>¿Por qué se escribe así?</h3>
{P("Boletín 1", "¿Por qué <em>Platero y yo</em> va en cursiva?", ["Es el nombre de un personaje famoso", "Es el título de un libro completo", "Es una cita textual del autor"], 1, {0: "Aquí es el título de un libro.", 2: "No son palabras citadas."}, "Las obras completas van en cursiva.")}
{P("Boletín 2", "¿Por qué «Los zapaticos de rosa» va entre comillas?", ["Es el título de un libro completo", "Son palabras de la bibliotecaria", "Es un poema dentro de un libro"], 2, {0: "El libro es <em>La Edad de Oro</em>.", 1: "Es un título, no una cita."}, "Las partes de una obra van entre comillas.")}
{P("Boletín 3", "¿Por qué hay punto y coma en la lista de los tres libros?", ["Porque cada libro es una oración completa", "Porque cada libro lleva su autor separado por coma", "Porque la lista tiene más de dos libros"], 1, {0: "No son oraciones.", 2: "Una lista simple va con comas."}, "La lista ya tiene comas dentro (libro, autor): el punto y coma agrupa cada libro con su autor.")}
{P("Boletín 4", "¿Dónde va el punto en la cita de la bibliotecaria?", ["Antes de cerrar las comillas", "No lleva punto porque es una cita", "Después de cerrar las comillas"], 2, {0: "Así es en inglés.", 1: "La oración termina y necesita su punto."}, "En español, el punto va después de las comillas de cierre.")}
{P("Boletín 5", "¿Por qué <em>lunes</em> y <em>octubre</em> van en minúscula?", ["Porque no están al principio de la oración", "Porque los días y los meses van en minúscula en español", "Porque son palabras de uso muy frecuente"], 1, {0: "Aunque estuvieran en medio, en inglés irían con mayúscula: la razón es la regla del español.", 2: "La frecuencia no decide."}, "En español, a diferencia del inglés, los días y los meses van en minúscula.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Busquen juntos en casa un libro, una revista o un periódico en español. Escriban en una hoja el título como debe ir (a mano, subrayado) y el título de una de sus partes entre comillas.</p>")}"""

    secciones = [("s1", "Repaso: lo que ya sabe", s1), ("s2", "Los títulos: cursiva o comillas", s2), ("s3", "Las comillas para citar", s3), ("s4", "Los dos puntos", s4),
                 ("s5", "El punto y coma", s5), ("s6", "Mayúsculas: la norma española", s6), ("s7", "Lectura: «Recomendaciones de la biblioteca»", s7)]
    tarea = [("Mis títulos.", "Escriba a mano el título de su libro favorito (subrayado), de una película (subrayado) y de una canción (entre comillas). Revise las mayúsculas."),
             ("Una cita.", "Escriba una oración que cite algo que le dijo alguien de su familia, con los dos puntos y las comillas en su sitio, y el punto después de las comillas."),
             ("Corrija.", "«Mi hijo nació el Martes 3 de Marzo» · «El Alcalde habló en Inglés y en Español» · «Para el viaje llevo: ropa, comida y agua» · «Leí \"Cien Años De Soledad.\"» "
              "<details class=\"transc\"><summary>Ver las respuestas</summary><p>«Mi hijo nació el martes 3 de marzo.» · «El alcalde habló en inglés y en español.» · «Para el viaje llevo ropa, comida y agua.» (o «Para el viaje llevo tres cosas: ropa, comida y agua.») · «Leí <em>Cien años de soledad</em>.» (en cursiva o, a mano, subrayado; con mayúscula solo en la primera palabra; y el punto, al final).</p></details>")]
    quiz = [
        ("¿Cómo se escribe correctamente el título de un libro en la computadora?", ["<em>Cuentos de la selva</em>", "«Cuentos De La Selva»", "<em>Cuentos De La Selva</em>"], 0, {1: "Un libro va en cursiva y sobran mayúsculas.", 2: "Sobran mayúsculas."}, "<em>Cuentos de la selva</em>."),
        ("¿Cómo se escribe el título de un artículo de periódico?", ["Entre comillas", "En cursiva", "En mayúsculas"], 0, {1: "La cursiva es para obras completas.", 2: "No."}, "<strong>Entre comillas.</strong>"),
        ("Si escribe a mano, ¿qué sustituye a la cursiva de un título?", ["El subrayado", "Las comillas simples", "Las mayúsculas"], 0, {1: "No.", 2: "No."}, "El <strong>subrayado</strong>."),
        ("¿Qué comillas se usan primero en español?", ["Las angulares « »", "Las inglesas “ ”", "Las simples ‘ ’"], 0, {1: "Son para una cita dentro de otra.", 2: "Son para un tercer nivel."}, "Las <strong>angulares</strong>."),
        ("¿Cuál usa bien los dos puntos?", ["Necesito tres cosas: pan, leche y huevos.", "Necesito: pan, leche y huevos.", "Necesito pan: leche y huevos."], 0, {1: "Quedaron pegados al verbo.", 2: "Parten la lista."}, "Con la lista <strong>anunciada</strong>."),
        ("¿Cuál está bien puntuada?", ["Estudió mucho; sin embargo, no aprobó.", "Estudió mucho, sin embargo no aprobó.", "Estudió mucho: sin embargo; no aprobó."], 0, {1: "Con coma es una oración corrida.", 2: "Los signos están cambiados."}, "Punto y coma antes de <em>sin embargo</em> y coma después."),
        ("¿Por qué hay punto y coma en «Vinieron Ana, de Puebla; Luis, de Lima; y Rosa, de Cali»?", ["La lista ya tiene comas dentro", "Separa dos oraciones completas", "Siempre se usa antes de la y"], 0, {1: "No son oraciones.", 2: "No siempre."}, "La lista <strong>ya tiene comas</strong>."),
        ("¿Cuál está bien escrita?", ["El lunes 5 de octubre hablé con el alcalde.", "El Lunes 5 de Octubre hablé con el Alcalde.", "El lunes 5 de Octubre hablé con el Alcalde."], 0, {1: "Sobran mayúsculas.", 2: "Sobran mayúsculas."}, "Todo en <strong>minúscula</strong>."),
        ("¿Cuál está bien escrita?", ["Mi vecina es colombiana y habla inglés.", "Mi vecina es Colombiana y habla Inglés.", "Mi vecina es colombiana y habla Inglés."], 0, {1: "Sobran mayúsculas.", 2: "Sobra una mayúscula."}, "Nacionalidad e idioma en <strong>minúscula</strong>."),
        ("¿Cómo se escribe correctamente en mayúsculas?", ["ATENCIÓN AL CLIENTE", "ATENCION AL CLIENTE", "ATENCIÒN AL CLIENTE"], 0, {1: "Las mayúsculas llevan tilde.", 2: "La tilde del español va hacia la derecha: ´."}, "<strong>ATENCIÓN</strong>, con tilde."),
    ]
    filas = [
        ("Títulos y comillas", "Sé cuándo va cursiva y cuándo comillas, y dónde va el punto.", "Dudo con las partes de una obra.", "Los confundo (<a href=\"#s2\">repase las secciones 2 y 3</a>)."),
        ("Dos puntos y punto y coma", "Los uso en sus casos y no los pongo tras el verbo.", "A veces dudo entre uno y otro.", "No los distingo (<a href=\"#s4\">repase las secciones 4 y 5</a>)."),
        ("Mayúsculas", "Escribo en minúscula días, meses, idiomas y cargos.", "Se me escapa alguna mayúscula del inglés.", "Uso mayúsculas como en inglés (<a href=\"#s6\">repase la sección 6</a>)."),
    ]
    cierre = "<p>Ya escribe títulos, citas y listas con la puntuación española. En la próxima lección usará las <strong>raíces griegas y latinas</strong> para entender palabras nuevas.</p>"
    glosario = [("Cursiva", "Letra inclinada que marca los títulos de obras completas y las palabras de otro idioma."), ("Comillas", "Signos (« ») que encierran una cita textual o el título de una parte de una obra."),
                ("Dos puntos", "Signo (:) que anuncia una lista, una cita o una explicación."), ("Punto y coma", "Signo (;) que separa oraciones muy relacionadas o elementos de una lista con comas.")]
    conexion = ("<p>En la Lección 1.3 usó el punto y coma para corregir oraciones corridas. Hoy completa la puntuación que más pide el GED al citar textos y escribir listas.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, si puede, un libro o periódico en español.</p>")
    estd = LE.estandares(["L.2.4", "L.2.1"], base=["L.1.4"])
    return C.pagina_leccion(N, LE.titulo(N), "La puntuación y las mayúsculas del español.", ["Puntuación", "Mayúsculas"],
                            ["<strong>Escribir</strong> títulos en cursiva o entre comillas.", "<strong>Citar</strong> con comillas y el punto en su lugar.",
                             "<strong>Usar</strong> los dos puntos y el punto y coma en sus casos.", "<strong>Aplicar</strong> la norma española de las mayúsculas."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-2", LE.titulo("2-2")), glosario, P)


def practica():
    def cual(datos, pista):
        return [{"enun": "<p>¿Cuál está bien escrita?</p>", "ops": o, "ok": 0, "pista": pista, "exp": f"«{o[0]}» · {e}"} for o, e in datos]
    ti = cual(TIT, "¿Es una obra completa (cursiva) o una parte (comillas)? ¿Cuántas mayúsculas lleva el título?")
    dp = cual(DP, "¿Hay algo antes que anuncie la lista, la cita o la explicación? ¿Quedaron los dos puntos pegados al verbo?")
    orden = [";", ",", ":"]
    pc = [{"enun": f'<p class="frase">{t.replace("___", "<span class=hueco-sig>?</span>")}</p><p>¿Qué signo va?</p>', "ops": [SIG[x] for x in orden], "ok": orden.index(k), "enOrden": True,
           "pista": "¿Une dos oraciones completas? ¿La lista ya tiene comas? ¿Se anuncia algo?", "exp": e} for t, k, e in PC]
    ma = cual(MA, "Días, meses, idiomas, nacionalidades, cargos, estaciones y puntos cardinales van en minúscula.")
    mods = [("titulos", "Títulos", C.om("m1", "Elija la oración que escribe bien el título.")),
            ("dos-puntos", "Dos puntos", C.om("m2", "Elija la oración que usa bien los dos puntos.")),
            ("signos", "Coma, punto y coma o dos puntos", C.om("m3", "Decida qué signo va en el lugar marcado.")),
            ("mayusculas", "Mayúsculas", C.om("m4", "Elija la oración que sigue la norma española de las mayúsculas."))]
    js = C.js_datos("TI", ti) + C.js_datos("DP", dp) + C.js_datos("PC", pc) + C.js_datos("MA", ma) + 'creaBanco("m1", TI);\ncreaBanco("m2", DP);\ncreaBanco("m3", PC);\ncreaBanco("m4", MA);\n'
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
