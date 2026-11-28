# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 4.2 · Géneros literarios: poema, drama y prosa.
Fuente: clases_leng3/clase_4-2.html (GEDparaHispanos) y gramatica/n3-l4-2.html, adaptadas al marco de LearnGED.
Textos literarios de dominio público: José Martí, Versos sencillos (1891); Serafín y Joaquín Álvarez Quintero, Mañana de sol (1905);
Juan Ramón Jiménez, Platero y yo (1914); y fragmentos breves de autores clásicos.
Uso: python3 tools/build_leng3_4_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from datos_drama_n3 import DRAMA

LE.nivel(3)
N = "4-2"
G = ["Poema", "Drama", "Prosa"]


def R(t, k):
    return f'<span class="rima r{k}">{t}</span>'


ESTROFAS = [[f"Cultivo una rosa bl{R('anca', 'a')},", f"en julio como en en{R('ero', 'b')},", f"para el amigo sinc{R('ero', 'b')}", f"que me da su mano fr{R('anca', 'a')}."],
            [f"Y para el cruel que me arr{R('anca', 'a')}", f"el corazón con que v{R('ivo', 'c')},", f"cardo ni ortiga cult{R('ivo', 'c')}:", f"cultivo la rosa bl{R('anca', 'a')}."]]
PLATERO = ["Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Solo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.",
           "Lo dejo suelto, y se va al prado, y acaricia tibiamente con su hocico, rozándolas apenas, las florecillas rosas, celestes y gualdas… Lo llamo dulcemente: «¿Platero?», y viene a mí con un trotecillo alegre que parece que se ríe, en no sé qué cascabeleo ideal…",
           "Come cuanto le doy. Le gustan las naranjas mandarinas, las uvas moscateles, todas de ámbar, los higos morados, con su cristalina gotita de miel…",
           "Es tierno y mimoso igual que un niño, que una niña…; pero fuerte y seco como de piedra. Cuando paso sobre él, los domingos, por las últimas callejas del pueblo, los hombres del campo, vestidos de limpio y despaciosos, se quedan mirándolo:",
           "—Tiene acero…", "Tiene acero. Acero y plata de luna, al mismo tiempo."]
GE = [("Volverán las oscuras golondrinas<br>en tu balcón sus nidos a colgar,<br>y otra vez con el ala a sus cristales<br>jugando llamarán.", "Gustavo Adolfo Bécquer, <em>Rimas</em>", 0, "Versos cortos agrupados en estrofa, con ritmo: un yo que le habla a un «tú»."),
      ("Juventud, divino tesoro,<br>¡ya te vas para no volver!<br>Cuando quiero llorar, no lloro…<br>y a veces lloro sin querer…", "Rubén Darío, «Canción de otoño en primavera»", 0, "Versos con rima (<em>tesoro / lloro</em>, <em>volver / querer</em>)."),
      ("Hombres necios que acusáis<br>a la mujer sin razón,<br>sin ver que sois la ocasión<br>de lo mismo que culpáis…", "Sor Juana Inés de la Cruz", 0, "Una estrofa de cuatro versos con rima."),
      ("Yo soy un hombre sincero<br>de donde crece la palma,<br>y antes de morirme quiero<br>echar mis versos del alma.", "José Martí, <em>Versos sencillos</em>", 0, "Un yo poético que habla de sí mismo en versos que riman."),
      ("DOÑA LAURA. También usted ha debido pedirme permiso para sentarse en este banco, que es mío.<br>DON GONZALO. Aquí no hay bancos de nadie.", "Álvarez Quintero, <em>Mañana de sol</em>", 1, "Nombres de personajes y diálogo directo, sin narrador."),
      ("DON JUAN. ¡Cuál gritan esos malditos!<br>Pero ¡mal rayo me parta<br>si en concluyendo la carta<br>no pagan caros sus gritos!", "José Zorrilla, <em>Don Juan Tenorio</em>", 1, "Está en verso, pero habla un personaje: es teatro en verso."),
      ("SEGISMUNDO. ¿Qué es la vida? Un frenesí.<br>¿Qué es la vida? Una ilusión,<br>una sombra, una ficción…", "Calderón de la Barca, <em>La vida es sueño</em>", 1, "Teatro en verso: el nombre del personaje lo delata."),
      ("<em>(Entra MARÍA con una carta en la mano.)</em><br>MARÍA. ¿Ya pasó el cartero?<br>JOSÉ. <em>(Sin levantar la vista del periódico.)</em> Hace una hora.", "Fragmento creado para practicar", 1, "Acotaciones entre paréntesis y diálogo de personajes."),
      ("En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.", "Miguel de Cervantes, <em>Don Quijote de la Mancha</em>", 2, "Un narrador cuenta; la línea sigue hasta el margen."),
      ("Pues sepa vuestra merced, ante todas cosas, que a mí llaman Lázaro de Tormes, hijo de Tomé González y de Antona Pérez, naturales de Tejares, aldea de Salamanca.", "<em>Lazarillo de Tormes</em>", 2, "Prosa con narrador en primera persona."),
      ("Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.", "Juan Ramón Jiménez, <em>Platero y yo</em>", 2, "Prosa poética: tiene ritmo, pero se escribe en párrafos y la cuenta un narrador."),
      ("Para los niños es este periódico, y para las niñas, por supuesto. Sin las niñas no se puede vivir, como no puede vivir la tierra sin luz.", "José Martí, <em>La Edad de Oro</em>", 2, "Martí también escribió en prosa: aquí habla directamente a sus lectores en párrafos.")]
ROSA = "Cultivo una rosa blanca,<br>en julio como en enero,<br>para el amigo sincero<br>que me da su mano franca."
RA = [("DOÑA LAURA. <em>(Deteniéndola.)</em> Pero escucha.", "¿Qué es «(Deteniéndola.)»?", ["Una acotación: dice lo que hace el personaje", "Algo que doña Laura dice en voz alta", "La voz del narrador que cuenta la escena"], "Las acotaciones van entre paréntesis y no se dicen."),
      (ROSA, "¿Cuántos versos tiene esta estrofa?", ["Cuatro", "Uno", "Ocho"], "Cada línea es un verso; las cuatro forman una estrofa."),
      (ROSA, "¿Qué verso rima con el primero (<em>blanca</em>)?", ["El cuarto (<em>franca</em>)", "El segundo (<em>enero</em>)", "El tercero (<em>sincero</em>)"], "Riman desde la última vocal acentuada: <em>bl-anca / fr-anca</em>."),
      ("Lo dejo suelto, y se va al prado, y acaricia tibiamente con su hocico las florecillas…", "¿En qué persona está el narrador?", ["En primera persona: «Lo dejo»", "En tercera persona: «se va al prado»", "No hay narrador: es un diálogo"], "Quien cuenta participa en la historia."),
      ("Lugar apartado de un paseo público, en Madrid. Un banco a la izquierda del actor. Es una mañana de otoño templada y alegre.", "¿Qué parte de una obra de teatro es este texto?", ["La acotación inicial, que describe el lugar y la hora", "El diálogo de la protagonista con la criada", "El narrador que cuenta lo que piensa la protagonista"], "Las obras suelen empezar con una acotación que sitúa la escena."),
      ("Tiene acero. Acero y plata de luna, al mismo tiempo.", "¿Qué rasgo de la prosa poética aparece aquí?", ["Una imagen poética («plata de luna») dentro de un párrafo", "Versos cortos que riman y forman una sola estrofa", "Nombres de personajes delante de su diálogo"], "La prosa poética usa imágenes sin dejar de ser prosa."),
      ("MARÍA. ¿Ya pasó el cartero?<br>JOSÉ. Hace una hora.", "¿Cómo sabemos quién habla en un drama?", ["Por el nombre del personaje delante de lo que dice", "Porque el narrador lo dice con «dijo María» o «contestó José»", "Por el número de verso que lleva cada una de las líneas"], "En el teatro no hay «dijo»: el nombre va delante."),
      ("¿Qué es poesía?, dices mientras clavas<br>en mi pupila tu pupila azul.<br>¿Qué es poesía? ¿Y tú me lo preguntas?<br>Poesía… eres tú.", "¿Quién habla en este poema?", ["Un yo poético que le habla a un «tú»", "Un narrador que cuenta la vida de otros", "Dos personajes que discuten en escena"], "En la lírica, un «yo» expresa lo que siente."),
      ("Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón.", "¿Cómo está organizado este texto?", ["En oraciones dentro de un párrafo", "En versos agrupados en una estrofa", "En diálogo con acotaciones entre paréntesis"], "La línea continúa hasta el margen: es prosa."),
      ("PETRA. Tome usted. <em>(Le da un cartucho de papel pequeñito y se va por la izquierda.)</em>", "¿Para quién está escrita la acotación?", ["Para los actores y el director de la obra", "Para que el público la escuche en voz alta", "Para que la lea en voz alta otro personaje"], "Indica movimientos: el público los ve, no los oye.")]
FS = [("El poema de Martí empieza con «Cultivo una rosa blanca» y termina con «cultivo la rosa blanca». ¿Qué efecto tiene?", ["Muestra que su respuesta no cambia, sea amigo o enemigo", "Hace que el poema parezca que no tiene un final claro", "Sirve solo para que el poema tenga más versos y más rima"], "La estructura circular expresa la constancia de su generosidad."),
      ("«En julio como en enero». ¿Por qué el poeta nombra dos meses opuestos?", ["Para decir «siempre», en cualquier época del año", "Para indicar en qué meses florecen las rosas blancas", "Para contar cuándo conoció a su amigo más sincero"], "Los extremos representan todo el año."),
      ("En <em>Mañana de sol</em>, ninguna acotación dice que doña Laura sea tierna. ¿Cómo lo sabe el lector?", ["Por lo que hace: guarda migas para «los más chicos»", "Porque el narrador lo explica bien en un párrafo", "Porque lo dice la rima de todos sus diálogos"], "En el teatro, los actos y las palabras revelan el carácter."),
      ("¿Por qué los versos de los <em>Versos sencillos</em> son cortos y riman?", ["Para que suenen como canciones populares y se recuerden", "Porque Martí no sabía escribir versos más largos", "Porque así lo exige siempre el teatro clásico español"], "La forma sencilla acerca el poema a todos los lectores."),
      ("<em>Platero y yo</em> está contado en primera persona. ¿Qué aporta eso?", ["Vemos a Platero con los ojos de alguien que lo quiere", "Sabemos exactamente lo que piensa el burro en cada momento", "La historia es más objetiva, más fría y más imparcial"], "La primera persona transmite el cariño desde dentro."),
      ("Platero es «tierno y mimoso igual que un niño… pero fuerte y seco como de piedra». ¿Qué sugieren las dos comparaciones juntas?", ["Que Platero reúne ternura y fuerza al mismo tiempo", "Que Platero cambia de carácter según el día de la semana", "Que el narrador no sabe bien cómo es Platero de verdad"], "Los contrarios se resumen al final: «acero y plata de luna»."),
      ("Si <em>Mañana de sol</em> se contara en prosa, con narrador, ¿qué cambiaría?", ["Alguien nos diría cómo son los personajes, en vez de verlo nosotros", "Los personajes hablarían todos en verso y con mucha rima", "Desaparecerían de la historia el parque, el banco y los pájaros"], "El teatro muestra; la narración cuenta y explica."),
      ("¿Por qué la primera acotación de <em>Mañana de sol</em> describe tanto a doña Laura («no chochea»)?", ["Para que la actriz y el director sepan cómo es y cómo actuar", "Para que el público lo escuche en voz alta al empezar la obra", "Para que el lector sepa en qué año exacto se escribió la obra"], "Las acotaciones guían la representación.")]


def plano(h):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", h)).strip()


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Imagine que quiere contar lo mucho que quiere a alguien. Puede escribirle unos versos, puede representar una escena en la que dos personas hablan, o puede contarlo en un párrafo. Es el mismo cariño, pero cada forma lo dice de otra manera. En esta lección leerá tres textos clásicos de la literatura en español sobre el mismo tema, el cariño, y descubrirá qué hace cada forma con él.</p>
<p>Un <strong>género literario</strong> es una manera de escribir literatura. Basta con mirar un texto, antes de leerlo, para saber a qué género pertenece:</p>
{C.tabla("Los tres géneros literarios y sus rasgos", ["Género", "Cómo se ve", "Sus rasgos", "Quién habla"],
         [["Poema (lírica)", "Líneas cortas que no llegan al margen, agrupadas en bloques.", "Versos (cada línea), estrofas (cada grupo de versos), ritmo y, muchas veces, rima.", "Un yo poético que expresa lo que siente."],
          ["Drama (teatro)", "Nombres de personajes seguidos de lo que dicen, y textos entre paréntesis.", "Diálogo, personajes, acotaciones (las indicaciones entre paréntesis), actos y escenas.", "Los personajes, directamente. No hay narrador."],
          ["Prosa (narrativa)", "Líneas que llegan al margen, agrupadas en párrafos.", "Párrafos, oraciones completas, descripción y acciones.", "Un narrador, que puede ser parte de la historia (primera persona) o no (tercera persona)."]])}
{C.caja("ojo", "Las excepciones", "<p>Hay teatro escrito en verso (casi todo el teatro clásico español, como <em>La vida es sueño</em> de Calderón) y hay prosa muy musical, llamada <strong>prosa poética</strong> (como <em>Platero y yo</em>). Para decidir el género, pregúntese primero: ¿hay personajes que hablan sin narrador? Entonces es drama, aunque esté en verso.</p>")}
{P("Género 1", "«SEGISMUNDO. ¿Qué es la vida? Un frenesí. / ¿Qué es la vida? Una ilusión…» (Calderón). Está en verso. ¿De qué género es?", G, 1, {0: "Fíjese en el nombre delante: habla un personaje.", 2: "No hay narrador."}, "<strong>Drama</strong>: es teatro en verso.")}
{P("Género 2", "«En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo…» (Cervantes). ¿De qué género es?", G, 2, {0: "La línea sigue hasta el margen.", 1: "No hay personajes con su nombre delante."}, "<strong>Prosa</strong>: un narrador cuenta.")}"""

    poema = "".join('<div class="estrofa">' + "".join(f'<span class="v"><span class="v-n" aria-hidden="true">{i * 4 + k + 1}</span>{v}</span>' for k, v in enumerate(e)) + "</div>" for i, e in enumerate(ESTROFAS))
    s2 = f"""<p><strong>José Martí</strong> (La Habana, 1853 – Dos Ríos, 1895) fue poeta, periodista y héroe de la independencia de Cuba. Este es el poema XXXIX de sus <em>Versos sencillos</em> (1891), uno de los más conocidos de la lengua española.</p>
<p>{LE.escuchar(plano(" ".join(" ".join(e) for e in ESTROFAS)), "Escuchar el poema")} <button type="button" class="btn-sec" id="btn-p42" aria-pressed="false">Mostrar los versos y la rima</button></p>
<div class="poema" id="poema-42"><p class="poema-tit">XXXIX</p>{poema}</div>
<p class="fuente">José Martí, <em>Versos sencillos</em> (1891). Dominio público.</p>
<script>(function(){{var b=document.getElementById("btn-p42"),t=document.getElementById("poema-42");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-rima");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar los versos y la rima":"Mostrar los versos y la rima";}});}})();</script>
<h3>La forma del poema</h3>
<ul><li><strong>Versos y estrofas:</strong> tiene 8 versos agrupados en 2 estrofas de 4 versos.</li>
<li><strong>Medida:</strong> cada verso tiene 8 sílabas (al leer en voz alta, las vocales que se juntan entre palabras cuentan como una: <em>cul-ti-vou-na-ro-sa-blan-ca</em>). Son versos cortos y fáciles de recordar, como los de las canciones populares: por eso se llaman «sencillos».</li>
<li><strong>Rima:</strong> en cada estrofa riman el primer verso con el cuarto (<em>blanca / franca</em>) y el segundo con el tercero (<em>enero / sincero</em>). Las palabras riman desde la última vocal acentuada.</li></ul>
<h3>Cómo la forma ayuda al sentido</h3>
<p>El poema empieza y termina igual: «Cultivo una rosa blanca» y «cultivo la rosa blanca». Entre esas dos líneas aparece el enemigo, el que «arranca el corazón». Pero la forma vuelve al principio, como si dijera: pase lo que pase, mi respuesta es la misma. La <strong>estructura circular</strong> del poema es su mensaje: el cariño y la generosidad no cambian, ni con el amigo ni con el enemigo, «en julio como en enero».</p>
{P("Poema 1", "¿Qué palabra rima con <em>sincero</em>?", ["franca", "enero", "vivo"], 1, {0: "Rima con <em>blanca</em>.", 2: "Rima con <em>cultivo</em>."}, "<em>Enero / sincero</em>: riman desde la última vocal acentuada (-ero).")}
{P("Poema 2", "¿Qué quiere decir «en julio como en enero»?", ["Solo en verano y en invierno", "Siempre, en cualquier época del año", "Cuando hace mucho frío o mucho calor"], 1, {0: "Son dos meses opuestos que representan todo el año.", 2: "No habla del clima, sino del tiempo."}, "Dos meses opuestos representan todo el año: el cariño es constante.")}
{P("Poema 3", "¿Qué ofrece el poeta al «cruel que me arranca el corazón»?", ["Cardo y ortiga", "Un amigo sincero", "La misma rosa blanca"], 2, {0: "Dice que <em>no</em> los cultiva.", 1: "No."}, "Al enemigo le da <strong>la misma rosa blanca</strong>.")}"""

    s3 = f"""<p>Los hermanos <strong>Serafín y Joaquín Álvarez Quintero</strong>, de Andalucía, escribieron juntos cientos de obras de teatro. <em>Mañana de sol</em> (1905) es una comedia en un acto: en un banco de un parque de Madrid se encuentran dos viejitos que no se conocen… o eso creen. Este es el comienzo de la obra.</p>
<p>{LE.escuchar(plano(re.sub(r'<span class="acot">.*?</span>', ' ', DRAMA)), "Escuchar la escena")}</p>
<div class="drama">{DRAMA}</div>
<p class="fuente">Serafín y Joaquín Álvarez Quintero, <em>Mañana de sol</em> (1905). Dominio público. Ortografía actualizada.</p>
<h3>La forma del drama</h3>
<ul><li><strong>Personajes y diálogo:</strong> el texto es lo que dicen los personajes, cada intervención precedida por su nombre en mayúsculas. No hay un narrador que nos cuente lo que pasa.</li>
<li><strong>Acotaciones:</strong> los textos entre paréntesis (aquí, en cursiva y en otro color) no se dicen en voz alta. Son instrucciones del autor para los actores y el director: dónde ocurre la escena, cómo son los personajes, qué hacen y cómo lo dicen.</li>
<li>La primera acotación es larga: describe el lugar, la hora y a doña Laura. Las demás son breves y marcan movimientos y gestos.</li></ul>
<h3>Cómo la forma ayuda al sentido</h3>
<p>En el teatro conocemos a los personajes por lo que dicen y lo que hacen, no porque alguien nos los describa. Doña Laura tiene setenta años, pero su ingenio está intacto: cuando Petra no sabe «dónde tiene la cabeza», le contesta «En la escarapela del guarda», o sea, en el novio. Y las acotaciones nos muestran su ternura: cada mañana trae migas para «los tunantes», los pájaros, y reparte la última porción para «los más chicos».</p>
{P("Drama 1", "¿Qué es «(Siéntase en el banco.)»?", ["Algo que doña Laura le dice en voz alta a Petra", "Una acotación: indica lo que hace el personaje", "Un comentario del narrador de la historia"], 1, {0: "Va entre paréntesis: no se dice.", 2: "En el teatro no hay narrador."}, "Las acotaciones no se dicen: indican acciones, gestos o el lugar.")}
{P("Drama 2", "«¿Dónde tengo la cabeza?» — «En la escarapela del guarda.» ¿Qué muestra esta respuesta de doña Laura?", ["Que doña Laura no oye bien lo que le dicen", "Que el guarda le quitó la cabeza a Petra", "Su humor: sabe que Petra piensa en el novio"], 2, {0: "Responde con ingenio, no por error.", 1: "Es una broma, no algo literal."}, "El diálogo deja ver el carácter del personaje sin que nadie lo describa.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Lean la escena en voz alta, uno como doña Laura y otro como Petra. El que no lee los diálogos lee las acotaciones… pero en voz baja, como un director. Después cambien los papeles.</p>")}"""

    pl = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(PLATERO, 1))
    s4 = f"""<p><strong>Juan Ramón Jiménez</strong> (Moguer, 1881 – San Juan de Puerto Rico, 1958) recibió el Premio Nobel de Literatura en 1956. <em>Platero y yo</em> (1914) cuenta, en capítulos breves, la vida de un poeta y su burro Platero en el pueblo andaluz de Moguer. Este es el primer capítulo.</p>
<p>{LE.escuchar(" ".join(PLATERO), "Escuchar el capítulo")}</p>
<div class="articulo"><p><strong>I · Platero</strong></p>{pl}</div>
<p class="fuente">Juan Ramón Jiménez, <em>Platero y yo</em> (1914). Dominio público. Ortografía actualizada.</p>
<h3>La forma de la prosa</h3>
<ul><li><strong>Párrafos y oraciones:</strong> el texto llega hasta el margen y se organiza en párrafos; cada párrafo muestra un aspecto de Platero: cómo es por fuera, cómo se mueve, qué come, cómo es por dentro.</li>
<li><strong>Narrador en primera persona:</strong> quien cuenta es el «yo» del título, que vive con Platero: «Lo dejo suelto», «Lo llamo dulcemente», «Come cuanto le doy».</li>
<li><strong>Prosa poética:</strong> aunque no tiene versos, usa recursos de la poesía: comparaciones («cual dos escarabajos de cristal negro», «igual que un niño»), metáforas («espejos de azabache» por los ojos) y ritmo (la serie «pequeño, peludo, suave»).</li></ul>
<h3>Cómo la forma ayuda al sentido</h3>
<p>El narrador en primera persona nos acerca a Platero como lo ve alguien que lo quiere: no es «un burro», es <em>su</em> burro. Y el final une los contrarios que el capítulo ha ido mostrando: Platero es blando y tierno como un niño, pero «fuerte y seco como de piedra». La última frase lo resume con una imagen: «Acero y plata de luna, al mismo tiempo».</p>
{P("Prosa 1", "¿Quién narra el capítulo?", ["Platero, el burro, que habla de sí mismo", "Un narrador en primera persona que vive con Platero", "Un narrador que no participa en la historia"], 1, {0: "Platero no habla: «Lo llamo», dice el narrador.", 2: "«Lo dejo suelto»: participa."}, "«Lo dejo suelto», «Lo llamo»: es el «yo» del título.")}
{P("Prosa 2", "«Solo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.» ¿Qué recurso aparece?", ["Una acotación y un diálogo", "Un verso y su rima final", "Una metáfora y una comparación"], 2, {0: "No es teatro.", 1: "Es prosa: no hay versos."}, "«Espejos de azabache» es metáfora; «cual dos escarabajos», comparación: prosa poética.")}"""

    s5 = f"""<p>Los tres textos hablan del cariño, pero cada género lo muestra a su manera:</p>
{C.tabla("Comparación de los tres textos de la lección", ["", "Poema (Martí)", "Drama (Álvarez Quintero)", "Prosa (Juan Ramón Jiménez)"],
         [["¿Cariño por quién?", "Por el amigo… y también por el enemigo.", "Por los pajaritos del parque (y por la criada, a quien deja ir a ver a su novio).", "Por su burro Platero."],
          ["¿Quién lo expresa?", "Un yo poético que habla de sí mismo.", "Los personajes, con sus palabras y sus actos.", "Un narrador en primera persona."],
          ["¿Cómo?", "Una imagen que se repite: la rosa blanca.", "Gestos mostrados en las acotaciones: repartir las migas.", "Descripción con comparaciones y detalles."],
          ["La forma al servicio del sentido", "La estructura circular dice que el cariño no cambia.", "Sin narrador, el lector descubre el carácter por sí mismo.", "La primera persona nos hace ver a Platero con los ojos de quien lo quiere."]])}
{P("Forma 1", "¿En qué texto descubre el lector el carácter del personaje sin que nadie lo describa por dentro?", ["En el poema, por la rima de las estrofas", "En la prosa, porque el narrador lo explica todo", "En el drama, por lo que dice y hace doña Laura"], 2, {0: "El poema habla de un yo, no de un personaje.", 1: "Ahí sí hay alguien que describe."}, "El teatro muestra a los personajes a través de diálogos y acotaciones.")}
{P("Forma 2", "Si <em>Platero</em> se contara en tercera persona («Un hombre tenía un burro…»), ¿qué se perdería?", ["La descripción de cómo es por fuera el burro", "La cercanía de quien lo quiere y lo describe", "Los nombres de las frutas que le gusta comer"], 1, {0: "Eso podría seguir.", 2: "Eso podría seguir."}, "La primera persona hace sentir el cariño desde dentro.")}
{C.caja("tip", "Tres formas, un tema", "<p>Si tiene con quién practicar, elijan juntos un tema (la madre, el barrio, el primer trabajo). Uno escribe cuatro versos, otro una escena de seis líneas con una acotación, y otro un párrafo. Léanlos en voz alta: ¿qué dice mejor cada forma?</p>")}
<h3>Rúbrica de la tarea</h3>
{C.tabla("Rúbrica: tres criterios en cuatro niveles", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"],
         [["Distingue poema, drama y prosa", "Identifica el género sin error y lo justifica", "Identifica el género, justificación incompleta", "Duda entre dos géneros", "No identifica el género"],
          ["Identifica los rasgos", "Señala dos rasgos precisos con ejemplos del texto", "Dos rasgos sin ejemplo", "Un rasgo", "Ningún rasgo"],
          ["Relaciona forma y sentido", "Explica qué aporta la forma al sentido", "Lo menciona sin explicarlo", "Describe la forma, sin relacionarla", "No lo aborda"]])}
<p>Total: 12 puntos.</p>"""

    secciones = [("s1", "Tres géneros, tres formas", s1), ("s2", "El poema: «Cultivo una rosa blanca»", s2), ("s3", "El drama: «Mañana de sol»", s3),
                 ("s4", "La prosa: «Platero y yo»", s4), ("s5", "Tres formas, un tema", s5)]
    tarea = [("Un texto literario.", "Busque un texto literario breve (un poema, una escena de teatro o un fragmento de novela), copie unas líneas y diga de qué género es y qué dos rasgos lo distinguen."),
             ("Cambie la forma.", "Convierta las dos primeras intervenciones de <em>Mañana de sol</em> en un párrafo en prosa con narrador: «Doña Laura llegó al parque…». ¿Qué gana y qué pierde?"),
             ("Su redondilla.", "Escriba una estrofa de cuatro versos sobre alguien a quien quiere, con rima entre el primer y el cuarto verso y entre el segundo y el tercero.")]
    quiz = [
        ("¿Cómo se llama cada línea de un poema?", ["Verso", "Estrofa", "Párrafo"], 0, {1: "Es un grupo de versos.", 2: "Es de la prosa."}, "<strong>Verso.</strong>"),
        ("¿Qué es una <strong>estrofa</strong>?", ["Un grupo de versos", "Una palabra que rima", "Una indicación para los actores"], 0, {1: "No.", 2: "Eso es una acotación."}, "Un <strong>grupo de versos</strong>."),
        ("¿Qué es una <strong>acotación</strong>?", ["Una indicación del autor sobre acciones, gestos o lugar", "Una línea del poema que rima con la siguiente", "La opinión del narrador sobre los personajes"], 0, {1: "Eso es un verso.", 2: "En el teatro no hay narrador."}, "Una <strong>indicación del autor</strong>."),
        ("¿Qué género <strong>no</strong> tiene narrador?", ["El drama", "La prosa", "La novela"], 0, {1: "Tiene narrador.", 2: "Tiene narrador."}, "El <strong>drama</strong>."),
        ("¿Qué es la <strong>prosa poética</strong>?", ["Prosa que usa recursos de la poesía, como comparaciones y ritmo", "Un poema escrito en estrofas de cuatro versos que riman", "Una obra de teatro escrita completa en verso"], 0, {1: "Eso es un poema.", 2: "Eso es teatro en verso."}, "Prosa con <strong>recursos de la poesía</strong>."),
        ("Para decidir si un texto en verso es drama, conviene preguntarse…", ["¿hay personajes que hablan sin narrador?", "¿cuántas sílabas tiene cada verso?", "¿en qué año se escribió el texto?"], 0, {1: "Eso no decide el género.", 2: "Eso no decide el género."}, "Si hablan <strong>personajes sin narrador</strong>, es drama."),
        ("¿Quién habla en un poema lírico?", ["Un yo poético que expresa lo que siente", "Los personajes con su nombre delante", "Un narrador que cuenta una historia"], 0, {1: "Eso es el drama.", 2: "Eso es la prosa."}, "Un <strong>yo poético</strong>."),
        ("Un texto llega hasta el margen, está en párrafos y lo cuenta alguien. Es…", ["prosa", "un poema", "un drama"], 0, {1: "Los versos no llegan al margen.", 2: "En el drama no hay narrador."}, "<strong>Prosa.</strong>"),
        ("Dos palabras riman cuando…", ["suenan igual desde la última vocal acentuada", "tienen el mismo número de letras", "empiezan con la misma sílaba"], 0, {1: "No.", 2: "No."}, "Desde la <strong>última vocal acentuada</strong>."),
        ("Un narrador en primera persona…", ["participa en la historia y dice «yo»", "nunca aparece en la historia", "es siempre el autor real del libro"], 0, {1: "Ese es el de tercera persona.", 2: "No siempre."}, "Participa y dice <strong>«yo»</strong>."),
    ]
    filas = [
        ("Géneros", "Distingo poema, drama y prosa a simple vista, también las excepciones.", "Dudo con el teatro en verso.", "Los confundo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Rasgos", "Nombro versos, estrofas, rima, acotaciones y narrador con ejemplos.", "Conozco algunos.", "Me cuesta (<a href=\"#s2\">repase las secciones 2 a 4</a>)."),
        ("Forma y sentido", "Explico qué aporta la forma al sentido de cada texto.", "Describo la forma sin relacionarla.", "No lo veo (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya distingue el poema, el drama y la prosa, reconoce sus rasgos y ve cómo la forma ayuda al sentido. En la próxima lección trabajará el <strong>lenguaje figurado</strong>: símiles, metáforas, modismos y refranes.</p>"
    glosario = [("Verso", "Cada línea de un poema."), ("Estrofa", "Grupo de versos."), ("Rima", "Igualdad de sonidos al final de los versos, desde la última vocal acentuada."),
                ("Acotación", "Indicación del autor de teatro, entre paréntesis, sobre el lugar, las acciones o los gestos."), ("Prosa poética", "Prosa que usa recursos de la poesía.")]
    conexion = ("<p>En la Lección 4.1 vio cómo se organizan los textos informativos. Hoy ve cómo se organizan los textos literarios, con tres clásicos de la lengua española.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, si puede, alguien con quien leer la escena de teatro.</p>")
    estd = LE.estandares(["R.5.2", "R.5.4"], base=["R.3.4"])
    return C.pagina_leccion(N, LE.titulo(N), "El mismo tema, tres maneras de decirlo.", ["Literatura", "Géneros literarios"],
                            ["<strong>Distinguir</strong> el poema, el drama y la prosa, y sus excepciones.", "<strong>Reconocer</strong> versos, estrofas, rima, acotaciones y narrador.",
                             "<strong>Explicar</strong> cómo la forma de un texto ayuda a su sentido."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-3", LE.titulo("4-3")), glosario, P)


def practica():
    frag = lambda t, f: f'<div class="texto-breve"><p>{t}</p><p class="fuente">{f}</p></div>'
    ge = [{"enun": frag(t, f) + "<p><strong>¿De qué género es?</strong></p>", "ops": G, "ok": k, "enOrden": True,
           "pista": "¿Hay nombres de personajes antes de lo que dicen? ¿Son líneas cortas agrupadas en estrofas? ¿O es un párrafo contado por un narrador?", "exp": f"<strong>{G[k]}.</strong> {n}"} for t, f, k, n in GE]
    ra = [{"enun": f'<div class="texto-breve"><p>{t}</p></div><p class="rel">{q}</p>', "ops": o, "ok": 0,
           "pista": "Verso y estrofa son del poema; diálogo y acotación, del drama; párrafo y narrador, de la prosa.", "exp": n} for t, q, o, n in RA]
    fs = [{"enun": f'<p class="rel">{q}</p>', "ops": o, "ok": 0, "pista": "Piense en qué hace la forma: ¿repite, compara, muestra sin explicar, cuenta desde dentro?", "exp": n} for q, o, n in FS]
    mods = [("genero", "¿Qué género es?", C.om("m1", "Lea el fragmento y decida si es un poema, un drama o prosa.") + '<p class="fuente">Fragmentos de obras de dominio público, salvo uno creado para practicar.</p>'),
            ("rasgos", "Los rasgos de cada género", C.om("m2", "Lea el fragmento y responda sobre sus rasgos.")),
            ("forma-sentido", "Forma y sentido", C.om("m3", "Piense qué aporta la forma de cada texto a lo que dice."))]
    js = C.js_datos("GE", ge) + C.js_datos("RA", ra) + C.js_datos("FS", fs) + 'creaBanco("m1", GE);\ncreaBanco("m2", RA);\ncreaBanco("m3", FS);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
