# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 7.3 · Narración con escenario y diálogo; proceso de revisión.
Fuente: clases_leng2/clase_7-3.html (GEDparaHispanos) y gramatica/n2-l7-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_7_3.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng2_7_1 import taller

LE.nivel(2)
N = "7-3"
HIST = [("La mudanza", ["Aquella mañana de junio, la familia Ortiz despertó antes del amanecer.", "Primero desarmaron las camas y guardaron la ropa en cajas.", "Luego llegó el camión que habían alquilado.", "Mientras los adultos cargaban los muebles, los niños se despidieron de los vecinos.", "Esa noche durmieron por primera vez en su nuevo apartamento."]),
        ("El apagón", ["Era una noche de agosto y hacía mucho calor.", "De repente, se apagaron todas las luces del edificio.", "Don Ramón bajó con una linterna para ver qué pasaba.", "Al rato, los vecinos sacaron sillas a la acera y se pusieron a conversar.", "Cuando volvió la luz, nadie quería volver a entrar."]),
        ("La entrevista de trabajo", ["Hace dos años, Carmen vio un anuncio de empleo en la biblioteca.", "Esa misma tarde preparó su currículum con ayuda de la bibliotecaria.", "Una semana después, la llamaron para una entrevista.", "El día de la entrevista respondió a todas las preguntas con calma.", "Desde entonces trabaja en esa empresa."]),
        ("La tormenta de nieve", ["El lunes por la mañana empezó a nevar con fuerza.", "Al mediodía, la escuela mandó a los niños a casa.", "Por la tarde, la nieve ya cubría los carros.", "Por la noche, los vecinos salieron con palas a limpiar la acera.", "Al día siguiente, el barrio amaneció blanco y en silencio."]),
        ("La carta del abuelo", ["Al principio, Daniel no entendía por qué su madre lloraba.", "Entonces ella le mostró una carta vieja que había encontrado en un cajón.", "Era del abuelo, escrita el día que llegó a este país.", "Juntos la leyeron en voz alta, despacio.", "Por fin, Daniel entendió de dónde venía su familia."]),
        ("El partido final", ["Faltaban cinco minutos y el equipo del barrio perdía por un gol.", "En ese momento, Julio robó el balón en el centro del campo.", "Corrió hacia la portería y disparó con todas sus fuerzas.", "El balón pegó en el poste y entró.", "Al final del partido, todos lo levantaron en hombros."])]
DIAL = [(["—¿Dónde está la parada? —preguntó la señora.", "—¿Dónde está la parada? —Preguntó la señora.", "\"¿Dónde está la parada?\", preguntó la señora."], "Raya, y el verbo de decir en minúscula."),
        (["—Aquí cerca —respondió el chofer—. Dos cuadras a la derecha.", "—Aquí cerca —respondió el chofer. —Dos cuadras a la derecha.", "—Aquí cerca, respondió el chofer, dos cuadras a la derecha."], "El punto va después de la segunda raya."),
        (["—Gracias —dijo ella.", "— Gracias — dijo ella.", "-Gracias -dijo ella."], "La raya va pegada a la palabra y es más larga que el guion."),
        (["—Mamá, ya llegué —gritó Tomás desde la puerta.", "—Mamá, ya llegué —Gritó Tomás desde la puerta.", "Mamá, ya llegué —gritó Tomás desde la puerta."], "Raya al inicio y verbo en minúscula."),
        (["—No sé —contestó Luis—. Tal vez mañana.", "—No sé —contestó Luis—, Tal vez mañana.", "—No sé —contestó Luis— tal vez mañana."], "Después de la segunda raya va el punto y luego mayúscula."),
        (["—¡Qué sorpresa! —exclamó la abuela.", "—¡Qué sorpresa!, —exclamó la abuela.", "—¡Qué sorpresa! —Exclamó la abuela."], "Tras «!» no va coma; el verbo, en minúscula."),
        (["—Tengo hambre —dijo el niño, y se sentó a la mesa.", "—Tengo hambre —dijo el niño y se sentó a la mesa—.", "—Tengo hambre. —dijo el niño, y se sentó a la mesa."], "Si el narrador cierra la oración, no hace falta la segunda raya."),
        (["—¿Vienes? —le pregunté.<br>—Sí, espérame —respondió Ana.", "—¿Vienes? —le pregunté. —Sí, espérame —respondió Ana.", "—¿Vienes? —le pregunté. Sí, espérame, respondió Ana."], "Cada personaje empieza en una línea nueva."),
        (["—Mira —susurró Elena—, ahí viene el maestro.", "—Mira —susurró Elena— ahí viene el maestro.", "—Mira, susurró Elena, —ahí viene el maestro."], "Si la oración sigue, la coma va después de la segunda raya."),
        (["—Buenos días —saludó la doctora—. ¿Cómo se siente hoy?", "—Buenos días —saludó la doctora. ¿Cómo se siente hoy?", "—Buenos días —saludó la doctora—, ¿Cómo se siente hoy?"], "La segunda raya cierra al narrador; después, punto y la pregunta.")]
MEJ = ["El escenario: cuándo y dónde", "Los detalles concretos", "El diálogo con raya", "Los conectores de tiempo"]
REV = [("Fui a la fiesta. Bailamos mucho.", "El viernes por la noche, en el salón de la iglesia, fui a la fiesta de mi prima. Bailamos mucho.", 0, "Ahora sabemos cuándo y dónde."),
       ("Compré comida para la cena.", "Compré pollo, arroz, aguacates y tortillas para la cena.", 1, "«Comida» se volvió algo que se puede imaginar."),
       ("Mi hermano dijo que no podía venir.", "—No puedo ir —me dijo mi hermano—. Tengo turno doble.", 2, "Las palabras del hermano ahora son diálogo."),
       ("Me levanté. Desayuné. Salí. Perdí el autobús.", "Primero me levanté y desayuné. Luego salí corriendo, pero al final perdí el autobús.", 3, "Los conectores ordenan y unen las acciones."),
       ("El parque estaba bonito.", "El parque estaba lleno de flores amarillas y olía a hierba recién cortada.", 1, "«Bonito» se cambió por lo que se ve y se huele."),
       ("La maestra nos saludó.", "—Bienvenidos a la clase de los martes —nos saludó la maestra.", 2, "Se oye la voz de la maestra.")]
COM = [("Narración de Pedro sobre su primer día en la fábrica. No dice qué hacía allí.", ["Me gustó cuando conoces a tu supervisor. ¿Podrías añadir qué tarea hacías?", "Está bien, pero creo que le falta algo, aunque no sé bien qué cosa es.", "Las historias de fábrica son siempre aburridas para todos los lectores."], "Señala algo bueno y pide un detalle concreto."),
       ("Narración de Lucía sobre una tormenta. Todo el diálogo está entre comillas.", ["¿Podrías escribir el diálogo con raya? Así se ve más claro quién habla.", "Tu historia está mal hecha; hay que repetirla entera desde el principio.", "Está perfecta así como está; no cambies nada de nada, ni una coma."], "Amable, concreto y útil."),
       ("Narración de Óscar sobre su boda. Los hechos están desordenados.", ["Me encantó el baile. ¿Podrías contar primero la ceremonia y después la fiesta?", "No entendí nada de lo que escribiste; es muy confuso y no se sigue.", "Escribe como escribo yo, con mis palabras, y seguro te quedará bien."], "Propone una solución concreta al desorden."),
       ("La narración de una compañera no dice dónde pasa.", ["¿Podrías añadir dónde estaban? Me costó imaginar el lugar.", "Tu historia está mal escrita; tienes que hacerla otra vez.", "Escribe como yo lo hago y seguro que quedará mucho mejor."], "Amable, concreto y útil.")]
PRIMER = ["Eran las seis menos cuarto de un martes de septiembre, y el salón 214 del centro comunitario todavía olía a pintura fresca. Rosa se sentó en la última fila, con el cuaderno nuevo apretado contra el pecho. Hacía veinte años que no pisaba una escuela.",
          "Primero llegó un muchacho con el uniforme de una cafetería; luego, dos señoras que se saludaron con un abrazo. A las seis en punto entró la maestra, una mujer alta de voz tranquila.",
          "—Buenas tardes a todos —dijo, y escribió su nombre en la pizarra—. Me llamo Elena. ¿Quién quiere empezar a presentarse?",
          "Nadie levantó la mano. Rosa sintió que el corazón le golpeaba las costillas. De repente, se oyó a sí misma:",
          "—Yo. Me llamo Rosa, tengo cuarenta y dos años y quiero sacar el GED antes de que mi hija termine la secundaria.",
          "Hubo un silencio corto. Después, el muchacho de la cafetería sonrió.", "—Pues yo quiero sacarlo antes que usted —dijo en broma.",
          "Todos se rieron, y Rosa también. Esa noche, en el autobús de vuelta a casa, abrió el cuaderno y escribió en la primera página: «Día 1. Lo logré»."]
TIEMPO = ["al principio", "primero", "aquella mañana", "hace años", "luego", "después", "más tarde", "entonces", "de repente", "de pronto", "en ese momento", "mientras", "mientras tanto", "al final", "por fin", "esa noche", "desde entonces"]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Todos tenemos historias que contar: el día que llegamos a este país, el nacimiento de un hijo, el primer empleo. Contarlas en voz alta es fácil; escribirlas para que otra persona las vea y las oiga exige algunas herramientas. En esta lección aprenderá a situar su historia en un lugar y un tiempo, a contarla en orden y a dar voz a sus personajes con el diálogo. Y aprenderá algo que hacen todos los escritores: <strong>revisar</strong>. Nadie escribe bien a la primera.</p>
{C.tabla("Los ingredientes de una narración", ["Ingrediente", "Qué es"],
         [["Escenario", "Dónde y cuándo pasa la historia: «un martes de septiembre, en el salón 214»."], ["Personajes", "Quiénes participan. Bastan unos detalles para verlos: «una mujer alta de voz tranquila»."],
          ["Secuencia", "Los hechos en orden: inicio, desarrollo y desenlace, como vio en la Lección 4.2."], ["Diálogo", "Las palabras de los personajes, escritas con raya. Dan vida a la escena."]])}
{C.caja("tip", "Muestre, no solo diga", "<p>«Rosa estaba nerviosa» informa. «Rosa sintió que el corazón le golpeaba las costillas» hace que el lector lo sienta.</p>")}
<h3>Narración modelo: el primer día</h3>
{LE.escuchar(" ".join(PRIMER), "Escuchar la narración")}
<div class="texto-lectura"><p><strong>El primer día</strong></p>{"".join(f"<p>{p}</p>" for p in PRIMER)}</div>
<p class="fuente">Texto escrito para esta lección.</p>
{P("Modelo 1", "¿Dónde y cuándo pasa la historia?", ["En el salón 214, un martes de septiembre por la tarde", "En un autobús, un sábado de septiembre por la noche", "En una cafetería, un martes de septiembre por la mañana"], 0, {1: "El autobús aparece solo al final.", 2: "El muchacho trabaja en una cafetería, pero la historia no pasa allí."}, "Lo dice la primera oración: es el escenario.")}
{P("Modelo 2", "¿Qué oración <strong>muestra</strong> que Rosa estaba nerviosa?", ["«Rosa se sentó en la última fila.»", "«Rosa sintió que el corazón le golpeaba las costillas.»", "«Hacía veinte años que no pisaba una escuela.»"], 1, {0: "Es un hecho, no muestra el sentimiento.", 2: "Explica su situación."}, "No dice «nerviosa», pero lo hace sentir.")}
{P("Modelo 3", "¿Qué hecho es el de mayor tensión?", ["Rosa se presenta delante de todos", "La maestra escribe su nombre", "Llegan dos señoras y se abrazan"], 0, {1: "Es un detalle.", 2: "Es un detalle."}, "Nadie se atreve, y Rosa habla.")}"""

    s2 = f"""<p>Una narración avanza en el tiempo. Los conectores de tiempo le dicen al lector cuándo pasa cada cosa:</p>
{C.tabla("Conectores de tiempo para narrar", ["Para…", "Conectores"],
         [["Empezar", "al principio, primero, aquella mañana, hace años"], ["Continuar", "luego, después, más tarde, entonces"], ["Algo inesperado", "de repente, de pronto, en ese momento"],
          ["Al mismo tiempo", "mientras, mientras tanto"], ["Terminar", "al final, por fin, esa noche, desde entonces"]])}
{P("Orden", "En «El primer día», ¿qué pasó <strong>primero</strong>?", ["La maestra escribe su nombre en la pizarra.", "Rosa se sienta en la última fila.", "Rosa se presenta delante de todos."], 1, {0: "Eso pasa a las seis en punto.", 2: "Eso pasa después."}, "Rosa se sienta; luego entra la maestra; después Rosa se presenta; esa noche escribe en el cuaderno.")}
<h3>El diálogo bien puntuado</h3>
<p>Recuerde las tres reglas de la raya de la Lección 3.1:</p>
<ol><li>Cada intervención empieza en una línea nueva con raya pegada a la primera palabra: <em>—Yo.</em></li>
<li>Las palabras del narrador van entre rayas; si empiezan con un verbo de decir, van en minúscula: <em>—Buenas tardes —dijo.</em></li>
<li>Si el personaje sigue hablando, el punto va después de la segunda raya: <em>—Buenas tardes —dijo—. Me llamo Elena.</em></li></ol>
{C.caja("tip", "Más allá de «dijo»", "<p>Para que el diálogo tenga vida, varíe los verbos: <em>preguntó, respondió, susurró, gritó, explicó, añadió</em>. Y cuide que cada personaje hable como él: el muchacho bromea, la maestra habla con calma.</p>")}
{P("Raya 1", "«—Todavía no —respondí—. Llegué tarde del trabajo.»", ["Bien puntuado", "Mal puntuado"], 0, {1: "Raya pegada, verbo en minúscula y punto después de la segunda raya."}, "<strong>Bien puntuado.</strong>")}
{P("Raya 2", "«\"Ven a comer\", dijo mi madre.»", ["Bien puntuado", "Mal puntuado"], 1, {0: "En una narración, el diálogo va con raya."}, "Se escribe: —Ven a comer —dijo mi madre.")}
{P("Raya 3", "«—Ahora voy —Dije yo.»", ["Bien puntuado", "Mal puntuado"], 1, {0: "Mire el verbo de decir."}, "«dije» va en minúscula: —Ahora voy —dije yo.")}"""

    s3 = f"""<p>Los escritores siguen un proceso de revisión:</p>
<ol class="proceso"><li>Escribir</li><li>Leer en voz alta</li><li>Recibir comentarios</li><li>Revisar</li></ol>
<p>Compare el primer borrador de Marta con su versión revisada, después de leerla en voz alta y escuchar a una compañera.</p>
<div class="dos-textos"><div class="texto-lectura"><p><strong>Borrador inicial</strong></p><p>Fui al mercado. Había mucha gente. Compré cosas. Una señora me habló. me dijo que los mangos estaban baratos. Volví a casa.</p></div>
<div class="texto-lectura tb"><p><strong>Versión revisada</strong></p><p>El sábado por la mañana fui al mercado del barrio. Había tanta gente que casi no se podía caminar entre los puestos. Mientras escogía tomates, una señora mayor se acercó.</p><p>—Lleve mangos, señorita —me dijo—. Hoy están a dos por un dólar.</p><p>Le hice caso y compré seis. Al final, volví a casa cargada y contenta.</p></div></div>
{C.tabla("Mejoras de la versión revisada", ["Qué mejoró", "Ejemplo"],
         [["Escenario", "«El sábado por la mañana», «el mercado del barrio»"], ["Detalles", "«tanta gente que casi no se podía caminar»; «tomates» en lugar de «cosas»"], ["Diálogo con raya", "«—Lleve mangos, señorita —me dijo—.»"],
          ["Conectores de tiempo", "«mientras», «al final»"], ["Corrección", "La mayúscula olvidada en «me dijo» ya no aparece"]])}
<h3>Leer y comentar</h3>
<p>Un buen comentario ayuda al escritor a mejorar sin desanimarlo. Debe ser <strong>amable, concreto y útil</strong>. Use estas frases:</p>
<ul><li>Para lo positivo: «Me gustó cuando…», «La parte de… me hizo sentir…».</li><li>Para sugerir: «¿Podrías añadir…?», «No entendí bien… ¿Podrías explicar…?», «¿Qué pasaría si…?».</li></ul>
{C.tabla("Comentarios poco útiles y útiles", ["Poco útil", "Útil"],
         [["Está bien.", "Me gustó cuando la señora te habla; se oye su voz."], ["No me gustó.", "¿Podrías añadir cuándo pasó? No sé si era de día o de noche."], ["Está muy corto.", "¿Qué pasó después de comprar los mangos? Me quedé con ganas de saberlo."]], fila_th=False)}
{P("Comentario", "Un compañero escribió el diálogo con comillas. ¿Cuál es el comentario más útil?", ["Los diálogos así no sirven para nada.", "Está perfecto, no cambies nada.", "Me encanta lo que dice tu abuelo. ¿Probamos a escribirlo con raya?"], 2, {0: "No es amable ni útil.", 1: "No ayuda a mejorar."}, "Reconoce lo bueno y propone el cambio.")}
<h3>Taller: escriba y revise su narración</h3>
<p>Elija un momento real o inventado: el día que llegó a una ciudad nueva · su primer empleo · una sorpresa · un viaje que no salió como esperaba · el día que conoció a alguien importante.</p>
<h4>Paso 1 · Su borrador</h4>
<p>Escriba sin miedo: el borrador no tiene que ser perfecto. Incluya un escenario (cuándo y dónde), los hechos en orden y al menos dos líneas de diálogo.</p>
{taller("2-7-3a", "Mi borrador", "Aquella mañana, en… Primero… De repente… —… Al final…", 6, 80, TIEMPO, [])}
<h4>Paso 2 · Léalo en voz alta y pida comentarios</h4>
<p>Pulse «Escuchar mi texto» o léalo usted en voz alta: oirá las partes que suenan raras. Si puede, léaselo a alguien y pídale un «Me gustó cuando…» y un «¿Podrías añadir…?».</p>
<h4>Paso 3 · Su versión revisada</h4>
<p>Copie su borrador aquí abajo y mejórelo con los comentarios que recibió y con la lista de revisión.</p>
<p><button type="button" class="btn-sec" id="pasar-borr">⬇️ Copiar el borrador aquí abajo</button> <span class="tl-aviso" id="pasar-aviso" aria-live="polite"></span></p>
{taller("2-7-3b", "Mi versión revisada", "Copie su borrador y mejórelo aquí.", 8, 120, TIEMPO,
        ["El escenario dice cuándo y dónde pasa la historia.", "Los hechos van en orden, con conectores de tiempo.", "Hay al menos dos intervenciones de diálogo.", "Cada intervención empieza en línea nueva con raya pegada a la palabra.",
         "Los verbos de decir (dijo, preguntó…) van en minúscula.", "Apliqué al menos una sugerencia que recibí.", "Cambié palabras generales («cosas», «bien») por detalles concretos.", "Escuché mi versión revisada en voz alta."])}
<script>(function(){{var btn=document.getElementById("pasar-borr"),av=document.getElementById("pasar-aviso"),seguro=false;
btn.addEventListener("click",function(){{var a=document.getElementById("tl-2-7-3a"),b=document.getElementById("tl-2-7-3b");if(!a||!b)return;
if(!a.value.trim()){{av.textContent="Primero escriba su borrador en el paso 1.";return;}}
if(b.value.trim()&&b.value!==a.value&&!seguro){{seguro=true;av.textContent="Ya tiene texto en la versión revisada. Pulse otra vez para reemplazarlo por el borrador.";setTimeout(function(){{seguro=false;}},4000);return;}}
seguro=false;b.value=a.value;b.dispatchEvent(new Event("input"));av.textContent="✓ Borrador copiado. Ahora mejórelo.";b.focus();}});}})();</script>
{C.tabla("Rúbrica de la narración y la revisión", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"],
         [["Escenario y secuencia", "Lugar y tiempo claros; hechos en orden con conectores", "Escenario claro; algún salto en el orden", "Falta el lugar o el tiempo", "No se entiende qué pasó ni dónde"],
          ["Diálogo puntuado", "Dos o más intervenciones, todas con raya bien usada", "Diálogo con algún error de raya", "Diálogo con comillas o sin marcas", "No hay diálogo"],
          ["Aplica una sugerencia", "Aplica la sugerencia y lo explica", "Aplica una sugerencia", "Menciona la sugerencia, pero no la aplica", "No hay revisión"],
          ["Mejora del borrador", "Más detalles, mejor orden y menos errores", "Mejora en dos aspectos", "Mejora en un aspecto", "Igual que el borrador"]])}
<p>Total: 16 puntos.</p>
<p>Si tiene con quién practicar, lea su narración en voz alta. Su compañero le da dos comentarios: uno con «Me gustó cuando…» y otro con «¿Podrías añadir…?». Después cambien los papeles.</p>"""

    secciones = [("s1", "Los ingredientes y una narración modelo", s1), ("s2", "La secuencia y el diálogo", s2), ("s3", "Revisar, comentar y escribir", s3)]
    tarea = [("Para el foro.", "Entregue su narración revisada. Debajo, escriba una oración que diga qué cambió gracias a un comentario: «Gracias a la sugerencia de…, añadí…»."),
             ("Comente dos narraciones.", "Deje a dos compañeros un «Me gustó cuando…» y un «¿Podrías añadir…?»."),
             ("Un recuerdo con diálogo.", "Escriba una escena corta (cinco o seis líneas) de una conversación que recuerde con alguien de su familia. Cuide la raya.")]
    quiz = [
        ("El <strong>escenario</strong> de una narración es…", ["el lugar y el tiempo en que pasa", "el personaje más importante", "la última parte de la historia"], 0, {1: "Eso es el protagonista.", 2: "Eso es el desenlace."}, "<strong>Dónde y cuándo.</strong>"),
        ("¿Qué oración presenta mejor un escenario?", ["Una noche de enero, en la parada del autobús, nevaba sin parar.", "De repente, alguien gritó mi nombre desde el otro lado.", "Al final, todos volvimos a casa cansados pero felices."], 0, {1: "No dice dónde ni cuándo.", 2: "Es un final."}, "Dice <strong>cuándo y dónde</strong>."),
        ("¿Qué conector indica algo <strong>inesperado</strong>?", ["De repente", "Al final", "Primero"], 0, {1: "Termina.", 2: "Empieza."}, "<strong>De repente.</strong>"),
        ("Ordene: (A) Llegó al hospital. (B) Sintió el dolor. (C) Nació su hija. ¿Cuál es el orden lógico?", ["B, A, C", "A, B, C", "C, B, A"], 0, {1: "Primero sintió el dolor.", 2: "Es al revés."}, "<strong>B, A, C.</strong>"),
        ("¿Cuál está <strong>bien puntuado</strong>?", ["—¿Me ayudas? —preguntó Luis.", "—¿Me ayudas? —Preguntó Luis.", "\"¿Me ayudas?\", preguntó Luis."], 0, {1: "El verbo de decir va en minúscula.", 2: "En el diálogo va raya."}, "Raya y verbo en minúscula."),
        ("¿Cuál está <strong>bien puntuado</strong>?", ["—Ya voy —dijo Ana—. Espérame un minuto.", "—Ya voy —dijo Ana. —Espérame un minuto.", "— Ya voy, dijo Ana, espérame un minuto."], 0, {1: "Falta la segunda raya antes del punto.", 2: "La raya va pegada y el narrador entre rayas."}, "El punto va después de la segunda raya."),
        ("En un diálogo, cada vez que habla un personaje distinto…", ["se empieza una línea nueva con raya", "se sigue escribiendo en la misma línea", "se usan comillas inglesas o latinas"], 0, {1: "No se sabría quién habla.", 2: "En la narración se usa raya."}, "Línea nueva con <strong>raya</strong>."),
        ("¿Cuál es el orden del proceso de revisión?", ["Escribir, leer en voz alta, recibir comentarios, revisar", "Revisar, escribir, recibir comentarios, publicar", "Recibir comentarios, escribir, publicar, leer"], 0, {1: "No se revisa antes de escribir.", 2: "Primero hay que escribir."}, "Escribir → leer → comentar → revisar."),
        ("Borrador: «Comimos cosas.» Revisado: «Comimos tamales de pollo y arroz con frijoles.» ¿Qué mejoró?", ["Los detalles concretos", "La puntuación del diálogo", "El escenario de la historia"], 0, {1: "No hay diálogo.", 2: "No dice dónde ni cuándo."}, "Los <strong>detalles concretos</strong>."),
        ("Un buen comentario debe ser…", ["amable, concreto y útil", "corto, general y rápido", "largo, duro y detallado"], 0, {1: "General no ayuda.", 2: "Duro desanima."}, "<strong>Amable, concreto y útil.</strong>"),
    ]
    filas = [
        ("Escenario y personajes", "Mi narración dice dónde y cuándo, y muestra cómo se sienten los personajes.", "Digo dónde, pero no cuándo.", "No sitúo la historia (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Secuencia y diálogo", "Uso conectores de tiempo y escribo el diálogo con raya.", "Me equivoco con alguna raya.", "Escribo el diálogo con comillas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Revisión", "Escribí un borrador, lo leí en voz alta, recibí comentarios y lo mejoré.", "Revisé solo la ortografía.", "No revisé (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 7. Ya escribe opinión, información y narración, y sabe revisar. En el Tema 8 trabajará la <strong>conversación, la comprensión auditiva y el proyecto final</strong> del nivel.</p>"
    glosario = [("Narración", "Texto que cuenta hechos en orden."), ("Escenario", "Dónde y cuándo pasa una historia."),
                ("Borrador", "Primera versión de un texto, que luego se revisa."), ("Revisar", "Releer y mejorar un texto con ayuda de comentarios.")]
    conexion = ("<p>En la Lección 3.1 aprendió la raya del diálogo y en la 4.2 el mapa de la historia. Hoy los usará para escribir su propia narración, y la mejorará con un proceso de revisión.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, un recuerdo para contar y, si puede, alguien que escuche su texto.</p>")
    estd = LE.estandares(["W.3", "L.2.4"], base=["R.3.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Contar una historia con escenario y diálogo, y mejorarla.", ["Escritura", "Narración"],
                            ["<strong>Situar</strong> una historia en un escenario.", "<strong>Ordenar</strong> los hechos con conectores de tiempo.",
                             "<strong>Escribir</strong> el diálogo con raya.", "<strong>Revisar</strong> un borrador con comentarios."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-1", LE.titulo("8-1")), glosario, P)


def practica():
    orden = []
    for ti, pasos in HIST:
        r = random.Random(ti); ini = list(range(len(pasos)))
        while ini == sorted(ini): r.shuffle(ini)
        orden.append({"titulo": f"«{ti}»", "intro": "Ordene los hechos con los botones ▲ y ▼. Los conectores de tiempo le ayudan.", "pasos": pasos, "inicio": ini, "cons": {}, "general": "Lea la historia en voz alta en este orden."})
    di = [{"enun": "<strong>¿Cuál está bien puntuado?</strong>", "ops": ops, "ok": 0, "pista": "Revise: ¿la raya está pegada?, ¿el verbo de decir está en minúscula?, ¿el signo va después de la segunda raya?", "exp": e} for ops, e in DIAL]
    re_ = []
    for a, b, k, e in REV:
        ops = [MEJ[k]] + [m for j, m in enumerate(MEJ) if j != k][:2]
        re_.append({"enun": f'<div class="dos-textos"><div class="texto-lectura"><p><strong>Borrador:</strong> {a}</p></div><div class="texto-lectura tb"><p><strong>Revisado:</strong> {b}</p></div></div><strong>¿Qué mejoró principalmente?</strong>',
                    "ops": ops, "ok": 0, "pista": "Compare las dos versiones: ¿qué tiene la revisada que no tenía el borrador?", "exp": e})
    re_ += [{"enun": f'<div class="texto-lectura"><p>{t}</p></div><strong>¿Cuál es el comentario más útil?</strong>', "ops": ops, "ok": 0, "pista": "Un buen comentario es amable, concreto y útil.", "exp": e} for t, ops, e in COM]
    mods = [("orden", "Ordene la historia", C.orden("m1", "Ponga los hechos en el orden en que ocurrieron.")), ("dialogo", "El diálogo bien puntuado", C.om("m2", "Elija la versión puntuada con la raya correcta.")),
            ("revision", "Revisar y comentar", C.om("m3", "Compare el borrador con la versión revisada, o elija el comentario más útil."))]
    js = C.js_datos("OR", orden) + C.js_datos("DI", di) + C.js_datos("RE", re_) + 'creaOrden("m1", OR);\ncreaBanco("m2", DI);\ncreaBanco("m3", RE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
