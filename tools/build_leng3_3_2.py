# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 3.2 · Citar detalles: lo explícito y lo inferido.
Fuente: clases_leng3/clase_3-2.html (GEDparaHispanos) y gramatica/n3-l3-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_3_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_3_1 import texto

LE.nivel(3)
N = "3-2"
EI = ["Explícito", "Inferido"]
LAVANDERIA = ["Carmen Rivas llegó a Chicago desde Guatemala en 1998. Durante veinte años trabajó en una lavandería de Albany Park, doblando ropa ajena de seis de la mañana a seis de la tarde.",
              "Mientras las máquinas giraban, los clientes esperaban sentados, mirando el celular o la pared. Un día, Carmen llevó de su casa una caja con diez libros en español y la puso junto a las sillas, con un letrero escrito a mano: «Llévate uno, trae otro».",
              "Durante dos semanas nadie tocó la caja. Pero un mes después, los diez libros habían desaparecido y en su lugar había treinta que Carmen no conocía. Algunos clientes empezaron a llegar con bolsas de libros de sus casas.",
              "Pronto hubo que poner un estante. La dueña de la lavandería, que al principio había dicho que los libros «estorbaban», terminó comprando dos estantes más. Por las tardes, los niños hacían la tarea entre los libros mientras sus madres esperaban la ropa, y a veces Carmen les leía un cuento en voz alta.",
              "Carmen se jubiló en 2019, pero los estantes siguen allí, con más de trescientos libros. Cuando le preguntan por qué empezó, contesta: «Yo aprendí a leer de grande. Sé lo que es tener hambre de un libro y no tener ninguno»."]
T1 = ["Cada mañana, don Julio abre su panadería a las cinco. A las seis ya hay fila en la puerta: obreros que van a la fábrica, madres que llevan a los niños a la escuela y algún taxista que termina su turno.",
      "Su pan de elote se acaba antes de las ocho. «Mi abuela me enseñó la receta en Michoacán», cuenta mientras amasa. Nunca la ha escrito en un papel."]
T2 = ["La biblioteca del barrio empezó a prestar computadoras portátiles en marzo. En el primer mes se prestaron doscientas, y la lista de espera llegó a cien personas.",
      "Para el verano, la biblioteca compró cincuenta computadoras más con una donación de una empresa local. Aun así, la bibliotecaria dice que todavía no alcanzan."]
T3 = ["Lucía revisó el pronóstico tres veces antes de salir. Guardó el paraguas en la mochila, aunque el cielo estaba despejado, y se puso las botas de lluvia.",
      "En el autobús, una señora le miró los pies y sonrió. Dos horas después, cuando Lucía salió de clase, caía un aguacero y las calles estaban inundadas."]
T4 = ["El huracán tocó tierra el jueves por la noche. Al día siguiente, la ciudad amaneció sin electricidad y con árboles caídos en muchas calles.",
      "Las escuelas permanecieron cerradas toda la semana. Los voluntarios de la iglesia repartieron agua y comida en el estacionamiento, porque los supermercados no tenían luz para abrir."]
DL = [(T1, "La panadería de don Julio es muy popular.", ["«A las seis ya hay fila en la puerta.»", "«Don Julio abre su panadería a las cinco.»", "«Nunca la ha escrito en un papel.»"], "La fila antes de que amanezca prueba que mucha gente va."),
      (T1, "Don Julio aprendió a hacer pan de su familia.", ["«Mi abuela me enseñó la receta en Michoacán.»", "«Su pan de elote se acaba antes de las ocho.»", "«Cada mañana, don Julio abre su panadería.»"], "Lo dice él mismo en la cita."),
      (T1, "El pan de elote es el que más se vende.", ["«Su pan de elote se acaba antes de las ocho.»", "«Mi abuela me enseñó la receta en Michoacán.»", "«A las seis ya hay fila en la puerta.»"], "Que se acabe tan temprano muestra que se vende mucho."),
      (T2, "Mucha gente quería una computadora prestada.", ["«La lista de espera llegó a cien personas.»", "«La biblioteca empezó a prestar computadoras en marzo.»", "«Compró cincuenta computadoras más.»"], "Cien personas esperando prueban la demanda."),
      (T2, "La biblioteca recibió ayuda de fuera.", ["«Con una donación de una empresa local.»", "«En el primer mes se prestaron doscientas.»", "«La bibliotecaria dice que todavía no alcanzan.»"], "La donación es ayuda de fuera."),
      (T2, "El problema de la falta de computadoras no se ha resuelto del todo.", ["«La bibliotecaria dice que todavía no alcanzan.»", "«Compró cincuenta computadoras más.»", "«Se prestaron doscientas en el primer mes.»"], "Aunque compraron más, todavía faltan. La segunda opción, sola, haría pensar lo contrario."),
      (T4, "El huracán causó daños en la ciudad.", ["«La ciudad amaneció sin electricidad y con árboles caídos.»", "«El huracán tocó tierra el jueves por la noche.»", "«Los voluntarios repartieron agua y comida.»"], "Sin luz y con árboles caídos: son los daños."),
      (T4, "La comunidad se ayudó después del huracán.", ["«Los voluntarios de la iglesia repartieron agua y comida.»", "«Las escuelas permanecieron cerradas toda la semana.»", "«Los supermercados no tenían luz para abrir.»"], "Los voluntarios ayudando a los vecinos prueban la idea.")]
EIX = [(T1, "Don Julio abre la panadería a las cinco.", 0, "Está escrito en la primera oración."),
       (T1, "Don Julio es de Michoacán o tiene familia allí.", 1, "Se deduce de que su abuela le enseñó la receta en Michoacán."),
       (T1, "Don Julio se sabe la receta de memoria.", 1, "Se deduce de que nunca la ha escrito."),
       (T3, "Lucía llevaba paraguas.", 0, "Dice que lo guardó en la mochila."),
       (T3, "Lucía sabía que iba a llover.", 1, "No lo dice, pero revisó el pronóstico, llevó paraguas y botas."),
       (T3, "La señora del autobús pensó que las botas eran exageradas.", 1, "Se deduce de que le miró los pies y sonrió con el cielo despejado."),
       (T3, "Cuando Lucía salió de clase, llovía mucho.", 0, "Dice que «caía un aguacero»."),
       (T2, "La biblioteca prestó doscientas computadoras el primer mes.", 0, "Está escrito en el texto."),
       (T2, "El préstamo de computadoras tuvo éxito.", 1, "Se deduce de la lista de espera y de que compraron más."),
       (T4, "Los supermercados estaban cerrados.", 1, "Se deduce de que «no tenían luz para abrir»."),
       (T4, "Las escuelas cerraron toda la semana.", 0, "Está escrito: «permanecieron cerradas toda la semana»."),
       (T4, "Muchas familias no tenían comida ni agua en casa.", 1, "Se deduce de que los voluntarios tuvieron que repartirlas.")]
CI = [(T1, "Cita textual de lo que dice don Julio", ["Don Julio cuenta: «Mi abuela me enseñó la receta en Michoacán».", "Don Julio cuenta: «Mi abuela me enseñó la receta en Michoacán.»", "Don Julio cuenta: \"Mi abuela le enseñó la receta en Michoacán\"."], "Palabras exactas, comillas angulares y el punto después de cerrarlas. La tercera cambia una palabra (<em>le</em>)."),
      (T1, "Paráfrasis del segundo párrafo", ["Según el texto, el pan de elote de don Julio se termina muy temprano.", "Según el texto, «el pan de elote de don Julio se termina muy temprano».", "Según el texto, «su pan de elote» se termina, «antes de las ocho.»"], "La paráfrasis va con sus palabras y sin comillas."),
      (T2, "Cita textual corta dentro de una oración", ["La bibliotecaria opina que las computadoras «todavía no alcanzan».", "La bibliotecaria opina que las computadoras «todavía no alcanzan.»", "La bibliotecaria opina que las computadoras «todavía no son suficientes»."], "Solo la parte que prueba, exacta, y el punto fuera. La tercera cambia las palabras."),
      (T2, "Paráfrasis con su fuente", ["En el primer párrafo, el texto dice que cien personas esperaban una computadora.", "«En el primer párrafo, cien personas esperaban una computadora prestada.»", "Cien personas esperaban, «una computadora», según el primer párrafo."], "Con sus palabras, diciendo de dónde sale."),
      (T3, "Cita textual del final", ["El texto dice que, al salir de clase, «caía un aguacero».", "El texto dice que, al salir de clase, «llovía muchísimo».", "El texto dice que, al salir de clase, caía un aguacero»."], "Exacta y con las dos comillas. La segunda cambia las palabras; la tercera olvida abrirlas."),
      (T4, "Cita textual con su párrafo", ["Según el segundo párrafo, las escuelas «permanecieron cerradas toda la semana».", "Según el segundo párrafo, las escuelas «estuvieron cerradas una semana».", "Según el segundo párrafo las escuelas permanecieron cerradas toda la semana»."], "Palabras exactas, comillas completas y el punto después.")]
NOTA_T = '<p class="fuente">Historias y personajes creados para la práctica.</p>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Si alguien le dice «Su vecino está de vacaciones», usted puede preguntar: «¿Cómo lo sabe?». Si le contesta «Me lo dijo él», la información es <strong>explícita</strong>. Si le contesta «Hace una semana que no recoge el periódico y su carro no está», es una <strong>inferencia</strong>: no se lo dijeron, pero lo deduce de las pistas. Las dos pueden ser ciertas, pero se apoyan en cosas distintas.</p>
<p>La <strong>evidencia textual</strong> es la parte del texto que prueba lo que usted dice sobre él. Responder bien una pregunta de lectura no es adivinar lo que el autor «quiso decir», sino poder señalar dónde lo dice o qué pistas lo muestran.</p>
{C.caja("tip", "En el GED", "<p>Muchas preguntas tienen dos partes: en la parte A se elige una respuesta y en la parte B, la oración del texto que la apoya. Otras veces se pregunta directamente: «¿Qué detalle del texto apoya la idea de que…?». Y en la Respuesta Extendida, citar la evidencia es una parte central de la nota.</p>")}
{C.caja("tip", "El hábito de esta lección", "<p>Cada vez que responda algo sobre un texto, pregúntese «<strong>¿dónde lo dice?</strong>». Si no puede señalarlo, revise su respuesta.</p>")}"""

    s2 = f"""{C.tabla("Diferencia entre información explícita e inferida", ["", "Explícito", "Inferido"],
         [["Qué es", "Lo que el texto dice con palabras.", "Lo que no dice, pero se deduce de sus pistas."],
          ["Cómo se prueba", "Señalando la oración que lo dice.", "Señalando las pistas y explicando cómo llevan a la idea."],
          ["Ejemplo: «Ana se puso el abrigo, los guantes y la bufanda antes de salir.»", "Ana se puso el abrigo antes de salir.", "Hace frío afuera."]])}
{C.caja("tip", "La prueba", "<p>Busque la idea en el texto. Si la encuentra escrita, aunque sea con otras palabras, es explícita. Si tiene que juntar pistas para llegar a ella, es inferida.</p>")}
{C.caja("ojo", "Inferido no es inventado", "<p>Una inferencia sale de las pistas del texto. «Ana va a esquiar» no es una inferencia válida: el texto no da ninguna pista de eso. En la Lección 3.3 practicará cómo distinguir una inferencia bien apoyada de una que va demasiado lejos.</p>")}"""

    lect = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(LAVANDERIA, 1))
    s3 = f"""<p>Lea la historia. Los párrafos están numerados para que pueda citarlos. Después responda: para cada idea, piense si está escrita en el texto o si la deduce de las pistas.</p>
<p>{LE.escuchar(" ".join(LAVANDERIA), "Escuchar la historia")}</p>
<div class="articulo"><p><strong>Los libros de la lavandería</strong></p>{lect}</div>
<p class="fuente">Historia y personajes creados para esta lección.</p>
<h3>¿Lo dice el texto o se infiere?</h3>
{P("Lavandería 1", "«Carmen trabajó veinte años en la lavandería.»", EI, 0, {1: "Busque en el párrafo 1."}, "<strong>Explícito</strong>: lo dice el párrafo 1.")}
{P("Lavandería 2", "«A Carmen le importaba que otras personas pudieran leer.»", EI, 1, {0: "¿Lo dice con esas palabras?"}, "<strong>Inferido</strong>: se deduce de lo que hizo y de su respuesta del párrafo 5.")}
{P("Lavandería 3", "«La dueña cambió de opinión sobre los libros.»", EI, 1, {0: "El texto no usa esas palabras."}, "<strong>Inferido</strong>: primero dijo que «estorbaban» y después compró estantes.")}
{P("Lavandería 4", "«De niña, Carmen no tuvo acceso a libros.»", EI, 1, {0: "El texto no lo dice así."}, "<strong>Inferido</strong>: de «aprendí a leer de grande» y «tener hambre de un libro y no tener ninguno».")}
{P("Lavandería 5", "¿Cuál de estas ideas <strong>no</strong> tiene evidencia en el texto?", ["Carmen les leía cuentos a los niños.", "Carmen trajo los primeros libros.", "Carmen abrió una biblioteca pública."], 2, {0: "Lo dice el párrafo 4.", 1: "Lo dice el párrafo 2."}, "Ninguna pista habla de una biblioteca pública: sería inventar.")}"""

    s4 = f"""<p>Imagine la pregunta: «¿Qué detalle muestra que los clientes valoraron la idea de Carmen?». Mire tres posibles respuestas:</p>
{C.tabla("Tres posibles evidencias y por qué sirven o no", ["Evidencia", "¿Sirve?"],
         [["«Algunos clientes empezaron a llegar con bolsas de libros de sus casas.» (párrafo 3)", "✓ Sí. Prueba directamente que los clientes participaron por su cuenta."],
          ["«Mientras las máquinas giraban, los clientes esperaban sentados.» (párrafo 2)", "✗ Habla de los clientes, pero no de lo que pensaban de los libros. Está relacionada, pero no prueba."],
          ["«Durante dos semanas nadie tocó la caja.» (párrafo 3)", "✗ Muestra lo contrario: al principio no les interesó."]])}
{C.caja("tip", "Tres trampas de las respuestas falsas", "<p>La evidencia que solo habla del <strong>mismo tema</strong>, la que es <strong>demasiado general</strong> y la que <strong>contradice</strong> la idea. La buena evidencia prueba la idea sin que usted tenga que añadir nada.</p>")}
{P("Evidencia 1", "Idea: <em>Al principio, a los clientes no les interesaron los libros.</em> ¿Qué oración lo prueba?", ["«Los clientes esperaban sentados, mirando el celular.»", "«Durante dos semanas nadie tocó la caja.»", "«Carmen llevó de su casa una caja con diez libros.»"], 1,
   {0: "Habla de los clientes, pero no de los libros.", 2: "Habla de Carmen, no del interés de los clientes."}, "Prueba directamente la falta de interés al principio.")}
{P("Evidencia 2", "Idea: <em>La lavandería se convirtió en un lugar para las familias.</em> ¿Qué oración lo prueba?", ["«Algunos clientes empezaron a llegar con bolsas de libros.»", "«Carmen se jubiló en 2019, pero los estantes siguen allí.»", "«Los niños hacían la tarea entre los libros mientras sus madres esperaban la ropa.»"], 2,
   {0: "Habla de los libros, no de las familias.", 1: "Habla de los estantes."}, "Muestra a madres e hijos usando el lugar.")}
{P("Evidencia 3", "Idea: <em>El trabajo de Carmen era largo y pesado.</em> ¿Qué oración lo prueba?", ["«Carmen llegó a Chicago desde Guatemala en 1998.»", "«Doblando ropa ajena de seis de la mañana a seis de la tarde.»", "«Mientras las máquinas giraban, los clientes esperaban.»"], 1,
   {0: "Habla de su llegada.", 2: "Habla de los clientes."}, "Doce horas al día doblando ropa: prueba lo largo de la jornada.")}"""

    s5 = f"""<p>Hay dos maneras de usar la evidencia en sus respuestas escritas:</p>
{C.tabla("Cita textual y paráfrasis", ["Manera", "Cómo se hace", "Ejemplo"],
         [["Cita textual", "Copia las palabras exactas entre comillas (Lección 2.1).", "Carmen explica que sabe «lo que es tener hambre de un libro y no tener ninguno»."],
          ["Paráfrasis", "Dice la idea con sus palabras, sin comillas, y señala de dónde sale.", "Según el párrafo 4, la dueña cambió de opinión y compró más estantes."]])}
<h3>Frases para introducir la evidencia</h3>
<p class="formula">Según el texto, … · En el párrafo 3, el autor dice que … · Como afirma Carmen, «…» · El texto muestra que … cuando dice «…»</p>
{C.caja("ojo", "Tres cuidados", "<p>La cita debe ser <strong>exacta</strong> (no cambie ni una palabra dentro de las comillas), <strong>corta</strong> (solo la parte que prueba) y <strong>explicada</strong> (después de citar, diga en una oración por qué prueba su idea). Y recuerde: el punto va después de cerrar las comillas.</p>")}
{P("Citar 1", "¿Cuál es una cita textual bien escrita?", ["Carmen dice que sabe \"lo que es tener hambre de libros.\"", "Carmen dice que sabe «lo que es tener hambre de un libro».", "Carmen dice que sabe lo que es tener hambre de un libro»."], 1,
   {0: "Cambia las palabras y pone el punto dentro.", 2: "Falta la comilla de apertura."}, "Palabras exactas, comillas completas y el punto después.")}
{P("Citar 2", "¿Cuál es una paráfrasis?", ["«Algunos clientes empezaron a llegar con bolsas de libros.»", "Algunos clientes «empezaron a llegar con bolsas».", "Según el párrafo 3, los clientes trajeron libros de sus casas."], 2,
   {0: "Es una cita textual.", 1: "Mezcla una cita."}, "Con sus palabras, sin comillas y diciendo de dónde sale.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Lean juntos una noticia. Uno dice algo sobre ella («el alcalde está preocupado») y el otro pregunta «¿dónde lo dice?». Hay que señalar la frase o explicar las pistas.</p>")}"""

    secciones = [("s1", "¿Por qué importa la evidencia?", s1), ("s2", "Lo explícito y lo inferido", s2), ("s3", "Lectura: «Los libros de la lavandería»", s3),
                 ("s4", "Elegir la mejor evidencia", s4), ("s5", "Cómo citar la evidencia", s5)]
    tarea = [("Responda con evidencia.", "En su cuaderno, responda con dos o tres oraciones y una cita de «Los libros de la lavandería»: ¿por qué cree que Carmen puso los libros en la lavandería? "
              "<details class=\"transc\"><summary>Ver una respuesta posible</summary><p>Carmen puso los libros porque quería que otros tuvieran lo que a ella le faltó. Ella misma explica: «Yo aprendí a leer de grande. Sé lo que es tener hambre de un libro y no tener ninguno» (párrafo 5). Esa cita muestra que conocía por experiencia la falta de libros y quería evitársela a los demás.</p></details>"),
             ("Dos columnas.", "Divida una página en dos columnas, <em>Explícito</em> e <em>Inferido</em>, y escriba tres ideas sobre la dueña de la lavandería en cada una, con el número de párrafo que las apoya."),
             ("Una noticia real.", "Busque una noticia corta y escriba una paráfrasis y una cita textual de ella, con su frase de introducción.")]
    quiz = [
        ("¿Qué es la evidencia textual?", ["La parte del texto que prueba lo que usted dice", "Su opinión personal sobre lo que dice el texto", "El título y los subtítulos que tiene el texto"], 0, {1: "La opinión no prueba nada.", 2: "No."}, "La parte del texto que <strong>prueba</strong>."),
        ("«Ana se puso el abrigo, los guantes y la bufanda.» ¿Qué se <strong>infiere</strong>?", ["Hace frío afuera.", "Ana se puso el abrigo.", "Ana va a esquiar."], 0, {1: "Está escrito: es explícito.", 2: "No hay pistas: sería inventar."}, "<strong>Hace frío</strong>: se deduce de las pistas."),
        ("Una idea que se encuentra escrita en el texto, aunque con otras palabras, es…", ["explícita", "inferida", "inventada"], 0, {1: "No hace falta deducirla.", 2: "No."}, "<strong>Explícita.</strong>"),
        ("Una inferencia válida…", ["sale de las pistas del texto", "es lo que uno se imagina", "está escrita palabra por palabra"], 0, {1: "Eso sería inventar.", 2: "Eso es lo explícito."}, "Sale de las <strong>pistas</strong>."),
        ("Una evidencia que habla del mismo tema pero no prueba la idea es…", ["una trampa: está relacionada, pero no prueba", "la mejor evidencia que se puede elegir", "una cita textual perfecta para responder"], 0, {1: "No prueba.", 2: "No prueba."}, "Una <strong>trampa</strong>."),
        ("Al citar, ¿qué no se puede hacer dentro de las comillas?", ["Cambiar las palabras", "Escribir más de una palabra", "Usar la cita en una respuesta"], 0, {1: "Sí se puede.", 2: "Para eso sirve."}, "No se pueden <strong>cambiar las palabras</strong>."),
        ("¿Qué lleva una paráfrasis?", ["La idea con sus palabras y de dónde sale", "Las palabras exactas entre comillas", "Su opinión sobre la idea del autor"], 0, {1: "Eso es una cita textual.", 2: "No."}, "Sus palabras y la <strong>fuente</strong>."),
        ("Después de citar una evidencia, conviene…", ["explicar en una oración por qué prueba su idea", "poner otra cita sin explicar nada", "terminar la respuesta en ese momento"], 0, {1: "Falta la explicación.", 2: "Falta la explicación."}, "<strong>Explicarla.</strong>"),
        ("¿Dónde va el punto en una cita textual al final de la oración?", ["Después de cerrar las comillas", "Antes de cerrar las comillas", "No lleva punto"], 0, {1: "Así es en inglés.", 2: "Sí lleva."}, "<strong>Después</strong> de cerrar las comillas."),
        ("¿Qué pregunta conviene hacerse al responder sobre un texto?", ["¿Dónde lo dice?", "¿Me gusta el texto?", "¿Cuántas páginas tiene?"], 0, {1: "No ayuda a probar.", 2: "No."}, "<strong>¿Dónde lo dice?</strong>"),
    ]
    filas = [
        ("Explícito e inferido", "Distingo lo que el texto dice de lo que se deduce.", "A veces los confundo.", "No veo la diferencia (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Elegir evidencia", "Elijo la oración que prueba la idea, sin trampas.", "Elijo a veces la que solo habla del tema.", "Me cuesta (<a href=\"#s4\">repase la sección 4</a>)."),
        ("Citar", "Cito exacto, corto y explicado, o parafraseo con la fuente.", "Olvido explicar la cita.", "No sé citar (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya distingue lo explícito de lo inferido y cita la evidencia. En la próxima lección practicará cómo <strong>hacer inferencias</strong> bien apoyadas.</p>"
    glosario = [("Evidencia textual", "La parte del texto que prueba lo que se dice sobre él."), ("Explícito", "Lo que el texto dice con palabras."),
                ("Inferido", "Lo que no se dice, pero se deduce de las pistas del texto."), ("Paráfrasis", "Decir una idea del texto con otras palabras, sin comillas y con su fuente.")]
    conexion = ("<p>En la Lección 3.1 encontró el tema central y resumió un texto. Hoy aprende a probar cada idea con la parte del texto que la sostiene.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, para la tarea, una noticia corta.</p>")
    estd = LE.estandares(["R.2.8", "W.1"], base=["R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "¿Dónde lo dice el texto?", ["Comprensión", "Evidencia textual"],
                            ["<strong>Distinguir</strong> la información explícita de la inferida.", "<strong>Elegir</strong> la evidencia que prueba una idea, sin caer en trampas.",
                             "<strong>Citar</strong> con exactitud o parafrasear con la fuente."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-3", LE.titulo("3-3")), glosario, P)


def practica():
    dl = [{"enun": texto(t) + f'<p class="rel">Idea: <em>{i}</em></p><p><strong>¿Qué oración lo prueba?</strong></p>', "ops": o, "ok": 0,
           "pista": "Esa oración habla del mismo texto, pero ¿prueba la idea sin añadir nada? ¿O dice lo contrario?", "exp": n} for t, i, o, n in DL]
    ei = [{"enun": texto(t) + f'<p class="rel">{i}</p><p><strong>Esta idea es…</strong></p>', "ops": EI, "ok": k, "enOrden": True,
           "pista": "Busque la idea en el texto: ¿está escrita, o la saca juntando pistas?", "exp": f"<strong>{EI[k]}.</strong> {n}"} for t, i, k, n in EIX]
    ci = [{"enun": texto(t) + f'<p class="rel">Se pide: {i}</p><p><strong>¿Cuál está bien escrita?</strong></p>', "ops": o, "ok": 0,
           "pista": "¿Las palabras entre comillas son exactas? ¿Están las dos comillas? ¿Dónde va el punto? ¿La paráfrasis lleva comillas?", "exp": n} for t, i, o, n in CI]
    mods = [("donde", "¿Dónde lo dice?", C.om("m1", "Lea el texto breve y elija la oración que prueba la idea.") + NOTA_T),
            ("explicito", "¿Explícito o inferido?", C.om("m2", "Decida si la idea está escrita en el texto o se deduce de sus pistas.")),
            ("cita", "La cita bien escrita", C.om("m3", "Elija la cita textual o la paráfrasis bien escrita."))]
    js = C.js_datos("DL", dl) + C.js_datos("EI", ei) + C.js_datos("CI", ci) + 'creaBanco("m1", DL);\ncreaBanco("m2", EI);\ncreaBanco("m3", CI);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
