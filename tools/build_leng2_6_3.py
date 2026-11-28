# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 6.3 · Vocabulario de dominio en ciencias e historia.
Fuente: clases_leng2/clase_6-3.html (GEDparaHispanos) y gramatica/n2-l6-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_6_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "6-3"
CIEN = [("biología", ["El estudio de los seres vivos", "El estudio de las rocas y montañas", "El estudio del clima y la lluvia"], "bio = vida; -logía = estudio de."),
        ("geología", ["El estudio de la tierra y las rocas", "El estudio de los animales salvajes", "El estudio de las estrellas y planetas"], "geo = tierra."),
        ("hidratar", ["Dar agua", "Dar calor", "Dar luz"], "hidro = agua."),
        ("termómetro", ["Aparato que mide la temperatura", "Aparato que mide la distancia", "Aparato que mide el peso"], "termo = calor; -metro = medida."),
        ("fotosíntesis", ["Las plantas fabrican alimento con la luz", "Las plantas absorben agua por la raíz", "Los animales digieren las plantas"], "foto = luz; síntesis = fabricar, unir."),
        ("ecosistema", ["Los seres vivos de un lugar y su ambiente", "Un sistema de riego para los cultivos", "Un grupo de animales de la misma especie"], "eco = casa, ambiente."),
        ("célula", ["La unidad más pequeña de un ser vivo", "Una de las partes del sistema solar", "Un tipo de roca que sale de volcanes"], "Todos los seres vivos están hechos de células."),
        ("organismo", ["Cualquier ser vivo", "Una máquina de laboratorio", "Una sustancia química"], "Una bacteria, un árbol y una persona son organismos."),
        ("hipótesis", ["Una explicación posible que se pone a prueba", "El resultado final que ya se comprobó", "La lista de pasos que sigue un experimento"], "El experimento sirve para comprobarla o descartarla."),
        ("variable", ["Lo que cambia o se mide en un experimento", "Lo que nunca cambia en un experimento", "El nombre que recibe el laboratorio"], "Por ejemplo, la cantidad de agua que recibe una planta."),
        ("materia", ["Todo lo que ocupa un lugar y tiene masa", "Solo los objetos sólidos y duros", "Solo lo que se puede ver a simple vista"], "El aire también es materia."),
        ("biodiversidad", ["La variedad de seres vivos de un lugar", "La cantidad de agua de un río", "La temperatura media de una región"], "bio = vida; diverso = variado."),
        ("antibiótico", ["Medicina que actúa contra las bacterias", "Vitamina que da más energía al cuerpo", "Aparato que mide la presión de la sangre"], "anti = contra; bio = vida (las bacterias)."),
        ("geotérmica", ["Energía que viene del calor de la tierra", "Energía que viene de la fuerza del viento", "Energía que viene de la luz del sol"], "geo = tierra; termo = calor."),
        ("evaporación", ["El agua líquida se convierte en vapor", "El vapor se convierte en gotas", "El agua cae como lluvia"], "Lo contrario es la condensación."),
        ("herbívoro", ["Animal que solo come plantas", "Animal que solo come carne", "Animal que come de todo"], "hierba + -voro (que come).")]
HIST = [("democracia", ["Gobierno del pueblo", "Gobierno de un rey", "Gobierno de los militares"], "demo = pueblo; -cracia = gobierno."),
        ("constitución", ["La ley más importante de un país", "Un discurso del presidente", "Un impuesto a los productos"], "Organiza el gobierno y protege derechos."),
        ("enmienda", ["Un cambio o una adición a la Constitución", "Una multa por no cumplir con la ley", "Un juicio importante de la Corte Suprema"], "La Constitución de los Estados Unidos tiene 27."),
        ("sufragio", ["El derecho a votar", "El derecho a protestar", "El deber de pagar impuestos"], "Sufragio femenino: el voto de las mujeres."),
        ("abolición", ["La eliminación de una ley o práctica", "La creación de una ley nueva", "El estudio de una ley antigua"], "Abolir = eliminar."),
        ("colonia", ["Territorio gobernado por otro país", "País que gobierna a otros", "Grupo de ciudadanos que votan"], "Las trece colonias eran gobernadas por Inglaterra."),
        ("emigrar", ["Salir del propio país para vivir en otro", "Llegar a un país para vivir en él", "Viajar dentro del mismo país"], "e- = hacia fuera."),
        ("inmigrar", ["Llegar a un país para vivir en él", "Salir del propio país para siempre", "Visitar otro país de vacaciones"], "in- = hacia dentro."),
        ("poder legislativo", ["El que hace las leyes", "El que aplica las leyes", "El que juzga según las leyes"], "En los Estados Unidos es el Congreso."),
        ("poder ejecutivo", ["El que aplica las leyes", "El que escribe las leyes", "El que juzga según las leyes"], "Lo encabeza el presidente."),
        ("poder judicial", ["El que interpreta las leyes en los tribunales", "El que escribe y vota las leyes en el Congreso", "El que dirige el ejército y la policía"], "La Corte Suprema está en la cima."),
        ("ciudadano", ["Miembro de un país con derechos y deberes", "Persona que vive en una gran ciudad", "Empleado del gobierno de una ciudad"], "Los ciudadanos pueden votar."),
        ("independencia", ["Libertad de un país para gobernarse solo", "Unión de varios países en uno", "Guerra entre dos partes de un país"], "Los Estados Unidos la declararon en 1776."),
        ("internacional", ["Entre varios países", "Dentro de un solo país", "Contra otro país"], "inter = entre."),
        ("antiesclavista", ["Que está en contra de la esclavitud", "Que está a favor de la esclavitud", "Que estudia la historia de la esclavitud"], "anti = contra."),
        ("impuesto", ["Dinero que se paga al gobierno", "Dinero que el gobierno regala", "Dinero que se presta a un banco"], "Con los impuestos se pagan escuelas, carreteras…")]
CTX = [("Los <strong>carnívoros</strong>, es decir, los animales que comen carne, cazan a otros animales.", "¿Qué significa «carnívoros»?", ["Animales que comen carne", "Animales que viven en el agua", "Animales que duermen de día"], "Definición con «es decir»."),
       ("Los <strong>combustibles fósiles</strong>, como el carbón y el petróleo, se formaron hace millones de años.", "¿Qué son los «combustibles fósiles»?", ["Materiales como el carbón y el petróleo", "Plantas que crecen en el desierto", "Máquinas que producen energía limpia"], "Ejemplos con «como»."),
       ("El clima de la región es <strong>árido</strong>; en cambio, la costa recibe mucha lluvia.", "¿Qué significa «árido»?", ["Seco", "Lluvioso", "Frío"], "Contraste con «en cambio»: lo opuesto a mucha lluvia."),
       ("Los colonos pagaban un <strong>tributo</strong>, un impuesto, a la Corona.", "¿Qué significa «tributo»?", ["Un impuesto", "Un regalo", "Una cosecha"], "Sinónimo entre comas."),
       ("La <strong>epidemia</strong> se extendió rápidamente: miles de personas enfermaron en pocas semanas.", "¿Qué significa «epidemia»?", ["Enfermedad que afecta a muchas personas a la vez", "Medicina nueva que cura muy rápido", "Hospital especial para los enfermos graves"], "«Miles de personas enfermaron» lo explica."),
       ("El general era <strong>implacable</strong> con sus enemigos, pero generoso con sus soldados.", "¿Qué significa «implacable»?", ["Que no tiene compasión", "Que es muy generoso", "Que es muy joven"], "Contraste con «pero generoso»."),
       ("Los <strong>mamíferos</strong>, por ejemplo, los perros, las ballenas y los seres humanos, alimentan a sus crías con leche.", "¿Qué son los «mamíferos»?", ["Animales que alimentan a sus crías con leche", "Animales que ponen huevos en el agua", "Animales que viven solo en el mar"], "Ejemplos y definición en la misma oración."),
       ("La enmienda fue <strong>ratificada</strong>; los estados la aprobaron y entró en vigor.", "¿Qué significa «ratificada»?", ["Aprobada", "Rechazada", "Olvidada"], "Sinónimo después del punto y coma."),
       ("La <strong>erosión</strong>, o sea, el desgaste de la tierra por el agua y el viento, formó el Gran Cañón.", "¿Qué significa «erosión»?", ["Desgaste de la tierra por el agua y el viento", "Erupción de un volcán muy antiguo", "Movimiento de la tierra durante un temblor"], "Definición con «o sea»."),
       ("A diferencia de los países <strong>neutrales</strong>, ese país sí participó en la guerra.", "¿Qué hacen los países «neutrales» en una guerra?", ["No toman partido", "Atacan primero", "Ganan siempre"], "Contraste con «a diferencia de»."),
       ("El nuevo medicamento resultó <strong>eficaz</strong>: casi todos los pacientes mejoraron.", "¿Qué significa «eficaz»?", ["Que da el resultado esperado", "Que es muy caro", "Que es difícil de encontrar"], "«Casi todos mejoraron» lo explica."),
       ("Durante la <strong>Gran Depresión</strong>, una crisis económica que empezó en 1929, millones de personas perdieron su empleo.", "¿Qué fue la «Gran Depresión»?", ["Una crisis económica", "Una enfermedad muy contagiosa", "Una guerra entre dos países"], "Definición entre comas."),
       ("Las plantas absorben <strong>nutrientes</strong>, como el nitrógeno y el potasio, a través de las raíces.", "¿Qué son los «nutrientes»?", ["Sustancias que alimentan a la planta", "Insectos que dañan las raíces", "Hojas que caen en otoño"], "Ejemplos con «como»."),
       ("El presidente <strong>vetó</strong> la ley; se negó a firmarla.", "¿Qué significa «vetó»?", ["La rechazó", "La escribió", "La aprobó"], "Sinónimo después del punto y coma.")]
CICLO = "El agua de la Tierra está siempre en movimiento. El calor del sol calienta los océanos, los ríos y los lagos, y parte del agua se convierte en vapor. Este proceso se llama evaporación. El vapor sube y, al llegar a zonas más frías de la atmósfera, se transforma otra vez en gotas diminutas que forman las nubes; es decir, se produce la condensación. Cuando las gotas se juntan y pesan demasiado, caen como lluvia, nieve o granizo. Esta caída se llama precipitación. Por último, el agua corre por la superficie o se filtra en el suelo hasta volver a los ríos y a los océanos, y el ciclo comienza de nuevo."


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Cada oficio tiene sus palabras. Un mecánico habla de «bujías» y «embrague»; una cocinera, de «sofrito» y «baño María». Las materias escolares también: en Ciencias dirá «fotosíntesis» y «ecosistema»; en Estudios Sociales, «enmienda» y «sufragio». No hace falta memorizar un diccionario entero. En esta lección aprenderá las palabras más frecuentes del GED y dos herramientas para descifrar las que no conoce: las partes de la palabra y las pistas del contexto.</p>
{C.tabla("Tres clases de palabras", ["Clase", "Qué son", "Ejemplos"],
         [["Cotidianas", "Las de todos los días.", "casa, comer, rápido, agua"], ["Académicas generales", "Aparecen en todas las materias.", "analizar, causa, efecto, comparar, concluir, evidencia"],
          ["De dominio", "Propias de una materia.", "célula, átomo (ciencias); constitución, colonia (historia)"]])}
{C.caja("tip", "Una ventaja del español", "<p>Muchas palabras científicas del inglés vienen del latín y del griego, igual que las nuestras. <em>Photosynthesis</em> es «fotosíntesis»; <em>democracy</em> es «democracia». Si las conoce en una lengua, casi siempre las reconoce en la otra.</p>")}
<h3>Vocabulario de ciencias</h3>
{C.tabla("Raíces frecuentes en ciencias", ["Pieza", "Significa", "Ejemplos"],
         [["bio-", "vida", "biología, biodiversidad, antibiótico"], ["eco-", "casa, ambiente", "ecosistema, ecología"], ["foto-", "luz", "fotosíntesis, fotografía"], ["hidro-", "agua", "hidratar, hidroeléctrica"],
          ["termo-", "calor, temperatura", "termómetro, térmico"], ["geo-", "tierra", "geología, geografía"], ["-logía", "estudio de", "biología, zoología"], ["-metro", "medida", "termómetro, barómetro"]])}
<ul><li><strong>Célula:</strong> la unidad más pequeña de un ser vivo.</li><li><strong>Organismo:</strong> cualquier ser vivo, desde una bacteria hasta una persona.</li>
<li><strong>Ecosistema:</strong> los seres vivos de un lugar y el ambiente en que viven.</li><li><strong>Fotosíntesis:</strong> proceso en que las plantas usan la luz del sol para fabricar su alimento.</li>
<li><strong>Hipótesis:</strong> una explicación posible que se pone a prueba con un experimento.</li><li><strong>Variable:</strong> lo que cambia o se mide en un experimento.</li>
<li><strong>Materia:</strong> todo lo que ocupa un lugar y tiene masa.</li></ul>
{P("Ciencias 1", "<strong>Hidroeléctrica:</strong> energía producida con…", ["la fuerza del agua", "la luz del sol", "el calor de la tierra"], 0, {1: "La luz es foto-.", 2: "La tierra es geo-."}, "hidro = agua.")}
{P("Ciencias 2", "<strong>Termómetro:</strong> aparato que mide…", ["la lluvia", "el peso", "la temperatura"], 2, {0: "termo- no es agua.", 1: "termo- no es peso."}, "termo = calor; -metro = medida.")}"""

    s2 = f"""{C.tabla("Raíces frecuentes en historia y gobierno", ["Pieza", "Significa", "Ejemplos"],
         [["demo-", "pueblo", "democracia, demografía"], ["-cracia", "gobierno, poder", "democracia, aristocracia"], ["anti-", "contra", "antiesclavista"], ["inter-", "entre", "internacional"],
          ["in- / e-", "hacia dentro / hacia fuera", "inmigrar / emigrar"]])}
<ul><li><strong>Constitución:</strong> la ley más importante de un país; organiza el gobierno y protege derechos.</li><li><strong>Enmienda:</strong> un cambio o una adición a la Constitución.</li>
<li><strong>Sufragio:</strong> el derecho a votar.</li><li><strong>Abolición:</strong> el acto de eliminar una ley o una práctica, como la esclavitud.</li>
<li><strong>Colonia:</strong> territorio gobernado por otro país lejano.</li>
<li><strong>Poder legislativo, ejecutivo y judicial:</strong> el que hace las leyes (Congreso), el que las aplica (presidente) y el que las interpreta (tribunales).</li></ul>
{C.caja("tip", "Inmigrar o emigrar", "<p>La misma persona hace las dos cosas. Quien sale de Guatemala <strong>emigra</strong> (sale de su país); al llegar a Chicago, <strong>inmigra</strong> (entra en el nuevo).</p>")}
{P("Historia 1", "<strong>Sufragio:</strong>", ["el derecho a trabajar", "el derecho a votar", "el deber de pagar impuestos"], 1, {0: "No es el trabajo.", 2: "No son los impuestos."}, "Sufragio universal: todos pueden votar.")}
{P("Historia 2", "El <strong>poder legislativo</strong>…", ["interpreta las leyes en los tribunales", "aplica las leyes desde la presidencia", "hace las leyes"], 2, {0: "Ese es el judicial.", 1: "Ese es el ejecutivo."}, "En los Estados Unidos es el Congreso.")}
<h3>Una palabra, dos materias</h3>
<p>Algunas palabras comunes tienen un significado especial en cada materia. El contexto le dice cuál es.</p>
{C.tabla("Palabras que cambian según la materia", ["Palabra", "En ciencias", "En historia y gobierno"],
         [["estado", "Forma de la materia: sólido, líquido o gaseoso", "Un país o una de sus partes (el estado de Illinois)"], ["cámara", "Espacio cerrado (la cámara de un experimento)", "Grupo de legisladores (la Cámara de Representantes)"],
          ["poder", "Energía o fuerza de algo (el poder del viento)", "Autoridad para gobernar (el poder ejecutivo)"], ["revolución", "Una vuelta completa (la Tierra alrededor del Sol)", "Un cambio político profundo (la Revolución mexicana)"],
          ["corte", "Una sección (el corte de una hoja al microscopio)", "Un tribunal (la Corte Suprema)"]])}
{P("Dos materias 1", "«El hielo es agua en <strong>estado</strong> sólido.»", ["Forma de la materia", "Parte de un país"], 0, {1: "Habla del hielo."}, "Sólido, líquido o gaseoso.")}
{P("Dos materias 2", "«La Tierra tarda un año en completar una <strong>revolución</strong> alrededor del Sol.»", ["Una vuelta completa", "Un cambio político"], 0, {1: "Habla de la Tierra y el Sol."}, "En ciencias: una vuelta.")}
{P("Dos materias 3", "«El proyecto de ley pasó a la <strong>Cámara</strong> de Representantes.»", ["Un espacio cerrado", "Un grupo de legisladores"], 1, {0: "Habla de una ley."}, "Es una parte del Congreso.")}"""

    s3 = f"""<p>Los textos de ciencias e historia suelen explicar sus palabras difíciles. Busque estas cuatro pistas, que ya conoce de la Lección 5.2:</p>
{C.tabla("Pistas del contexto en ciencias e historia", ["Pista", "Señales", "Ejemplo"],
         [["Definición", "es, es decir, o sea, se llama, entre comas o rayas", "Los herbívoros, es decir, los animales que solo comen plantas, viven en la sabana."],
          ["Ejemplo", "como, por ejemplo, entre ellos", "Los combustibles fósiles, como el carbón y el petróleo, contaminan el aire."],
          ["Sinónimo", "una palabra parecida cerca", "La antigua ley fue derogada; el gobierno la anuló y dejó de aplicarse."],
          ["Contraste", "pero, en cambio, a diferencia de", "Unos estados eran esclavistas; en cambio, otros prohibían la esclavitud."]])}
{C.caja("tip", "Compruebe su adivinanza", "<p>Cambie la palabra difícil por el significado que cree y lea la oración otra vez. Si tiene sentido, acertó.</p>")}
{P("Contexto 1", "«El rey era un <strong>tirano</strong>; en cambio, su hijo gobernó con justicia.» ¿Qué significa «tirano»?", ["Un gobernante cruel e injusto", "Un gobernante joven y nuevo", "Un gobernante rico y poderoso"], 0, {1: "Busque el contraste.", 2: "Busque el contraste."}, "Contraste: lo opuesto de «con justicia».")}
{P("Contexto 2", "«La sequía fue <strong>devastadora</strong>: destruyó casi todas las cosechas.» ¿Qué significa «devastadora»?", ["Que causa mucho daño", "Que dura muy poco", "Que llega sin avisar"], 0, {1: "Lea lo que sigue a los dos puntos.", 2: "Lea lo que sigue a los dos puntos."}, "«Destruyó casi todas» lo explica.")}
<h3>Lectura: el ciclo del agua</h3>
{LE.escuchar(CICLO, "Escuchar el texto")}
<div class="texto-lectura"><p>{CICLO.replace("evaporación", "<strong>evaporación</strong>", 1).replace("condensación", "<strong>condensación</strong>").replace("precipitación", "<strong>precipitación</strong>")}</p></div>
<p class="fuente">Texto escrito para esta lección.</p>
{P("Ciclo 1", "¿Qué es la <strong>evaporación</strong>, según el texto?", ["El agua que cae como lluvia", "El agua que se convierte en vapor por el calor", "El agua que se filtra en el suelo"], 1, {0: "Eso es la precipitación.", 2: "Eso pasa al final del ciclo."}, "«…parte del agua se convierte en vapor. Este proceso se llama evaporación.»")}
{P("Ciclo 2", "¿Qué pista usa el texto para explicar la <strong>condensación</strong>?", ["Un contraste con «pero»", "Una definición con «es decir»", "Un ejemplo con «como»"], 1, {0: "No hay «pero».", 2: "No hay «como»."}, "«…es decir, se produce la condensación».")}
{P("Ciclo 3", "¿Qué significa <strong>diminutas</strong> en «gotas diminutas»?", ["Muy frías", "Muy pequeñas", "Muy pesadas"], 1, {0: "El texto no lo dice así.", 2: "Si pesaran, no flotarían."}, "Forman nubes: son tan pequeñas que flotan.")}
<p>Si tiene con quién practicar, escojan un artículo corto de ciencias o de historia. Cada uno subraya tres palabras de dominio y explica al otro qué pista usó para entenderlas.</p>"""

    secciones = [("s1", "Tres clases de palabras y vocabulario de ciencias", s1), ("s2", "Vocabulario de historia y gobierno", s2), ("s3", "Pistas del contexto y el ciclo del agua", s3)]
    tarea = [("Mi glosario.", "Empiece un cuaderno con dos columnas, «Ciencias» e «Historia». Anote diez palabras de esta lección con su significado en sus propias palabras y una oración de ejemplo."),
             ("Cazador de raíces.", "Busque en casa, en las etiquetas o en las noticias, cinco palabras con bio-, eco-, foto-, hidro-, termo- o geo-. Explique qué significa cada una."),
             ("Pistas en acción.", "Lea un documento del <a href=\"/es/estudios-sociales/fuentes/\">Archivo de fuentes</a>. Copie dos palabras difíciles y escriba qué pista del contexto le ayudó a entenderlas.")]
    quiz = [
        ("Las palabras de <strong>dominio</strong> son…", ["las propias de una materia, como ciencias o historia", "las que usamos todos los días en casa y en la calle", "las que solo se usan en otros países de habla hispana"], 0, {1: "Esas son las cotidianas.", 2: "No tiene que ver con los países."}, "Las propias de una <strong>materia</strong>."),
        ("<strong>Fotosíntesis</strong> tiene la pieza <em>foto-</em>, que significa…", ["luz", "agua", "vida"], 0, {1: "Agua es hidro-.", 2: "Vida es bio-."}, "<strong>Luz.</strong>"),
        ("¿Qué estudia la <strong>biología</strong>?", ["Los seres vivos", "Las rocas y los volcanes", "Los gobiernos antiguos"], 0, {1: "Eso es la geología.", 2: "Eso es la historia."}, "Los <strong>seres vivos</strong>."),
        ("En un experimento, la <strong>variable</strong> es…", ["lo que cambia o se mide", "el nombre del científico", "el lugar donde se hace"], 0, {1: "No es una persona.", 2: "No es un lugar."}, "Lo que <strong>cambia</strong>."),
        ("<strong>Democracia</strong> significa…", ["gobierno del pueblo", "gobierno de los ricos", "gobierno de un rey"], 0, {1: "demo- es pueblo.", 2: "demo- es pueblo."}, "Gobierno del <strong>pueblo</strong>."),
        ("Una persona sale de Honduras para vivir en otro país. Desde el punto de vista de Honduras, esa persona…", ["emigra", "inmigra", "se coloniza"], 0, {1: "Eso es desde el país al que llega.", 2: "No existe ese uso."}, "<strong>Emigra</strong>: sale."),
        ("«El vapor es agua en <strong>estado</strong> gaseoso.» Aquí «estado» significa…", ["forma de la materia", "parte de un país", "situación de ánimo"], 0, {1: "Habla del vapor.", 2: "Habla del vapor."}, "<strong>Forma de la materia.</strong>"),
        ("«La Revolución mexicana comenzó en 1910.» Aquí «revolución» significa…", ["un cambio político profundo", "una vuelta alrededor del Sol", "un movimiento de una máquina"], 0, {1: "Eso es en ciencias.", 2: "No habla de máquinas."}, "Un <strong>cambio político</strong>."),
        ("«Los <strong>roedores</strong>, como el ratón y la ardilla, tienen dientes que crecen siempre.» ¿Qué pista del contexto hay?", ["Ejemplo", "Contraste", "Sinónimo"], 0, {1: "No hay nada contrario.", 2: "No hay otra palabra igual."}, "<strong>Ejemplo</strong>: «como»."),
        ("Según el texto del ciclo del agua, las nubes se forman por…", ["la condensación", "la precipitación", "la filtración"], 0, {1: "La precipitación es la caída.", 2: "La filtración es en el suelo."}, "La <strong>condensación</strong>."),
    ]
    filas = [
        ("Raíces", "Uso bio-, geo-, hidro-, demo-, -cracia y otras piezas para entender palabras nuevas.", "Reconozco algunas piezas.", "No miro las piezas (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Palabras clave", "Explico las palabras clave de ciencias e historia y sus dos sentidos.", "Conozco algunas.", "No las conozco (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Contexto", "Uso las cuatro pistas y compruebo mi adivinanza.", "Uso solo la definición.", "No uso pistas (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 6. Ya lee gráficas, fuentes y vocabulario de las otras materias del GED. En el Tema 7 pasará a la <strong>escritura</strong>: el texto de opinión, el informativo y la narración.</p>"
    glosario = [("Palabra de dominio", "Palabra propia de una materia."), ("Raíz griega o latina", "Pieza que da significado a muchas palabras: bio-, geo-, demo-."),
                ("Enmienda", "Cambio o adición a la Constitución."), ("Hipótesis", "Explicación posible que se pone a prueba.")]
    conexion = ("<p>En la Lección 5.2 aprendió a descubrir palabras por el contexto y los afijos. Hoy aplicará esas herramientas al vocabulario de Ciencias y de Estudios Sociales, las otras dos materias de lectura del GED.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.4.1"], base=["R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Las palabras de ciencias e historia, pieza por pieza.", ["Vocabulario", "Ciencias e historia"],
                            ["<strong>Distinguir</strong> palabras cotidianas, académicas y de dominio.", "<strong>Usar</strong> raíces griegas y latinas para entender términos.",
                             "<strong>Reconocer</strong> palabras con un sentido en cada materia.", "<strong>Aplicar</strong> las pistas del contexto a textos de ciencias e historia."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-1", LE.titulo("7-1")), glosario, P)


def practica():
    def termino(d, pista):
        return [{"enun": f"<span class=\"grande\">{w}</span><br>¿Qué significa?", "ops": ops, "ok": 0, "pista": pista, "exp": f"<strong>{w}</strong>: {ops[0][0].lower() + ops[0][1:]}. {n}"} for w, ops, n in d]
    ci = termino(CIEN, "Busque la pieza conocida dentro de la palabra.")
    hi = termino(HIST, "Busque la pieza conocida o piense dónde ha oído la palabra.")
    cx = [{"enun": f'<div class="texto-lectura"><p>{o}</p></div><strong>{q}</strong>', "ops": ops, "ok": 0, "pista": "Busque la pista cerca de la palabra: una definición, un ejemplo, un sinónimo o un contraste.", "exp": n} for o, q, ops, n in CTX]
    mods = [("ciencias", "Vocabulario de ciencias", C.om("m1", "Elija el significado de la palabra.")), ("historia", "Vocabulario de historia y gobierno", C.om("m2", "Elija el significado de la palabra.")),
            ("contexto", "Pistas del contexto", C.om("m3", "Lea la oración y descubra la palabra en negrita."))]
    js = C.js_datos("CI", ci) + C.js_datos("HI", hi) + C.js_datos("CX", cx) + 'creaBanco("m1", CI);\ncreaBanco("m2", HI);\ncreaBanco("m3", CX);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
