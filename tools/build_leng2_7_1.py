# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 7.1 · Texto de opinión: postura clara y razones con conectores.
Fuente: clases_leng2/clase_7-1.html (GEDparaHispanos) y gramatica/n2-l7-1.html, adaptadas al marco de LearnGED.
Datos citados en el texto modelo: Academia Estadounidense de Pediatría (healthychildren.org, «How to Make a Family Media Plan»: zonas sin pantallas, como la mesa);
CDC (150 minutos de actividad moderada a la semana para adultos). Consultados el 28 de noviembre de 2026.
Uso: python3 tools/build_leng2_7_1.py
"""
import os, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "7-1"
POSTURA_T = [
    ("Muchos trabajadores pasan más de una hora al día en el tráfico. Si las empresas permitieran trabajar desde casa dos días por semana, esas horas se usarían en la familia o en el descanso. Además, habría menos carros en las calles. Por eso, las empresas deberían ofrecer esa opción siempre que sea posible.",
     ["Las empresas deberían permitir trabajar desde casa", "Hay demasiado tráfico en las calles de la ciudad", "Los trabajadores necesitan más horas de descanso"], "La última oración lo resume: «las empresas deberían ofrecer esa opción»."),
    ("En mi opinión, el desayuno escolar gratuito debería ofrecerse a todos los niños. Un niño con hambre no puede concentrarse en clase. Además, cuando el desayuno es para todos, nadie se siente señalado por pedirlo.",
     ["El desayuno escolar gratis debería ser para todos", "Los niños con hambre no se concentran en clase", "Algunos niños se sienten mal al pedir comida"], "«En mi opinión…» presenta la postura; lo demás son razones."),
    ("Los teléfonos celulares no deberían estar permitidos en el salón de clase. Distraen a los estudiantes y facilitan copiar en los exámenes. Por supuesto, los padres necesitan comunicarse en una emergencia; sin embargo, pueden llamar a la oficina de la escuela.",
     ["Los celulares no deberían estar permitidos en clase", "Los padres necesitan comunicarse en emergencias", "Los estudiantes copian en los exámenes"], "La primera oración da la postura."),
    ("Aunque los libros electrónicos son prácticos, creo que los niños pequeños deberían leer en papel. Pasar páginas, señalar dibujos y volver atrás es más fácil con un libro en la mano. Por otra parte, el papel no tiene notificaciones que distraigan.",
     ["Los niños pequeños deberían leer en papel", "Los libros electrónicos son muy prácticos", "El papel no tiene notificaciones que distraen"], "«Creo que…» marca la postura; «aunque son prácticos» es una concesión."),
    ("Cada verano, la piscina del parque cierra a las seis de la tarde, justo cuando muchos padres salen del trabajo. Las familias que trabajan no pueden aprovecharla. Por todo esto, pido que la piscina abra hasta las nueve de la noche.",
     ["La piscina debería abrir hasta las nueve", "Los padres salen del trabajo a las seis", "En verano hace calor en el parque"], "La petición final es la postura.")]
POSTURA_Q = [(["La ciudad debería poner más paradas de autobús en el barrio.", "En el barrio hay tres paradas de autobús en la calle principal.", "Algunos vecinos usan el autobús todos los días y otros no."], "Dice qué piensa el autor y qué debería hacerse."),
             (["Aprender un oficio es tan valioso como ir a la universidad.", "Hay muchos oficios, como la plomería y la electricidad.", "Muchas personas estudian en la universidad y otras trabajan."], "Toma partido de forma clara."),
             (["Los supermercados deberían cobrar las bolsas de plástico.", "Las bolsas de plástico tienen ventajas y desventajas.", "En el supermercado venden bolsas de plástico."], "«Ventajas y desventajas» no toma partido."),
             (["Todos los adultos deberían aprender primeros auxilios.", "Los primeros auxilios se enseñan en algunos cursos.", "La Cruz Roja es una organización internacional."], "Es una afirmación que se puede defender con razones."),
             (["La biblioteca debería abrir los domingos.", "La biblioteca está en la calle principal.", "No sé si la biblioteca debería abrir más días."], "Las dudas no son una postura.")]
AS = ["Con apoyo", "Sin apoyo"]
RAZ = [("«Es obvio que los perros son mejores mascotas que los gatos.»", 1, "«Es obvio» no prueba nada."), ("«Los perros ayudan a hacer ejercicio, porque hay que sacarlos a caminar todos los días.»", 0, "Da un hecho comprobable."),
       ("«Las bicicletas son el mejor transporte del mundo y punto.»", 1, "«Y punto» cierra sin explicar."), ("«La bicicleta ahorra dinero: no necesita gasolina, seguro ni estacionamiento.»", 0, "Enumera hechos concretos."),
       ("«Todo el mundo sabe que el café es malo.»", 1, "«Todo el mundo sabe» es una señal vacía."), ("«Beber agua en lugar de refrescos reduce el azúcar que consumimos, porque los refrescos llevan mucho azúcar añadido.»", 0, "Explica con un hecho."),
       ("«Las clases en línea son malísimas.»", 1, "Solo repite la opinión con más fuerza."), ("«Las clases en línea permiten estudiar a quienes trabajan, ya que pueden conectarse por la noche.»", 0, "Da una razón comprobable."),
       ("«Los médicos recomiendan que los adultos duerman al menos siete horas para que el cuerpo se recupere.»", 0, "Cita lo que dicen los expertos."), ("«Dormir es lo más importante, sin ninguna duda.»", 1, "«Sin ninguna duda» no es un apoyo."),
       ("«Un huerto en casa ahorra dinero: un sobre de semillas suele costar menos que los tomates que se compran en un mes.»", 0, "Compara precios."), ("«Los huertos son bonitos y a todos les encantan.»", 1, "«A todos les encantan» no se puede comprobar."),
       ("«Leer el periódico nos mantiene informados sobre las decisiones del gobierno local.»", 0, "Explica qué se gana."), ("«Cualquier persona inteligente estaría de acuerdo conmigo.»", 1, "Ataca a quien no piensa igual, pero no da razones.")]
CON = [("Prefiero cocinar en casa ___ es más barato y más sano.", ["porque", "sin embargo", "en conclusión"], "Explica la causa."), ("El parque es grande. ___, tiene canchas de fútbol y de básquetbol.", ["Además", "Por lo tanto", "Aunque"], "Añade información."),
       ("La tienda cerró temprano; ___, no pude comprar la leche.", ["por eso", "además", "en primer lugar"], "Muestra la consecuencia."), ("Es cierto que el curso es difícil; ___, vale la pena.", ["sin embargo", "por lo tanto", "también"], "Responde a una objeción."),
       ("___, el transporte público mejora la vida de toda la ciudad.", ["En conclusión", "Porque", "Por ejemplo"], "Cierra el texto."), ("___, hacer ejercicio mejora la salud. En segundo lugar, reduce el estrés.", ["En primer lugar", "Sin embargo", "Por lo tanto"], "Ordena la primera razón."),
       ("No fui a la fiesta ___ tenía que trabajar al día siguiente.", ["ya que", "además", "sin embargo"], "Da la causa."), ("Los precios suben cada mes. ___, muchas familias buscan un segundo empleo.", ["Por lo tanto", "En primer lugar", "Aunque"], "Consecuencia."),
       ("___ la casa es pequeña, tiene mucha luz.", ["Aunque", "Porque", "Por lo tanto"], "Contrasta dos ideas."), ("Las frutas tienen vitaminas. ___, tienen fibra.", ["También", "Sin embargo", "Por eso"], "Añade otra ventaja."),
       ("Hay muchos parques en Chicago, ___ el parque Lincoln y el parque Grant.", ["por ejemplo", "por lo tanto", "sin embargo"], "Presenta ejemplos."),
       ("Las aceras están rotas y varios vecinos se han caído. ___, la ciudad debe arreglarlas cuanto antes.", ["Por lo tanto", "Sin embargo", "Por ejemplo"], "La segunda idea es la consecuencia de la primera."),
       ("Estudié mucho; ___, aprobé el examen.", ["por lo tanto", "aunque", "en primer lugar"], "Consecuencia."), ("Me gusta el invierno. ___, el frío de enero es difícil de soportar.", ["Sin embargo", "Además", "Por lo tanto"], "Objeción o contraste.")]
CONECTORES = ["creo que", "en mi opinión", "considero que", "pienso que", "porque", "ya que", "puesto que", "en primer lugar", "en segundo lugar", "además", "también", "por otra parte",
              "por lo tanto", "por eso", "así que", "es cierto que", "sin embargo", "aunque", "en conclusión", "en resumen", "por todo esto", "por ejemplo"]
MODELO = ('<span class="p-pos">Creo que las familias deberían apagar el teléfono durante la cena.</span> '
          '<span class="p-raz"><span class="p-con">En primer lugar,</span> la cena es muchas veces el único momento del día en que todos están juntos. Los padres trabajan y los hijos estudian; <span class="p-con">por lo tanto,</span> esos minutos son valiosos para conversar.</span> '
          '<span class="p-raz"><span class="p-con">Además,</span> el teléfono interrumpe la conversación: cada mensaje que llega hace que alguien deje de escuchar. La Academia Estadounidense de Pediatría aconseja a las familias tener zonas sin pantallas, como la mesa del comedor.</span> '
          '<span class="p-con">Es cierto que</span> a veces hay que contestar una llamada urgente; <span class="p-con">sin embargo,</span> se puede dejar el teléfono en otra habitación con el volumen alto. '
          '<span class="p-fin"><span class="p-con">En conclusión,</span> apagar el teléfono durante la cena es un gesto pequeño que ayuda a mantener unida a la familia.</span>')
RECICLAR = ["Nuestro edificio necesita contenedores para reciclar. Cada semana sacamos bolsas llenas de latas, botellas y cartón que terminan en el vertedero, aunque podrían tener una segunda vida.",
            "En primer lugar, reciclar ahorra energía. Fabricar una lata con aluminio reciclado gasta mucha menos energía que fabricarla desde cero. Además, reciclar reduce la basura: el papel y el cartón son una parte grande de lo que tiramos, y casi todo se puede reciclar.",
            "Algunos vecinos dicen que separar la basura es complicado. Sin embargo, bastan dos contenedores con un cartel claro: uno para papel y cartón y otro para latas, botellas y plásticos.",
            "Por todo esto, pido a la administración que instale los contenedores este mes. Es un cambio pequeño que nos beneficia a todos."]


def plano(t):
    import re
    return re.sub(r"<[^>]+>", "", t)


def taller(clave, etiqueta, guia, oraciones, palabras, conectores, lista):
    a = lambda x: H.escape(x, quote=True)
    return (f'<div class="taller" data-clave="{clave}" data-etiqueta="{a(etiqueta)}" data-guia="{a(guia)}" data-oraciones="{oraciones}" data-palabras="{palabras}" '
            f'data-conectores="{a("|".join(conectores))}" data-lista="{a("|".join(lista))}"><p>El taller de escritura necesita JavaScript.</p></div>'
            '<p class="fuente">Su texto se guarda solo en este navegador. Para entregarlo, use «Copiar mi texto».</p>')


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Todos los días damos nuestra opinión: qué tienda tiene mejores precios, a qué hora conviene salir, qué candidato nos convence. Pero escribir una opinión que convenza a otros exige algo más: decir con claridad qué piensa, explicar por qué y apoyarlo con hechos. En el GED escribirá un texto argumentativo; esta lección es el primer escalón. Al final escribirá su propio texto de opinión.</p>
{C.tabla("Las cuatro partes de un texto de opinión", ["Parte", "Qué es"],
         [["1. Postura", "Lo que usted piensa, dicho en una oración clara: «Creo que…», «En mi opinión…»"], ["2. Razones", "Dos o tres motivos, cada uno apoyado en un hecho, un dato o un ejemplo."],
          ["3. Conectores", "Palabras que unen las ideas: porque, además, por lo tanto."], ["4. Conclusión", "Repite la postura con otras palabras y cierra el texto."]])}
{C.caja("tip", "Postura clara", "<p>El lector debe saber lo que usted piensa desde la primera oración. «Hay cosas buenas y malas» no es una postura. «Las escuelas deberían empezar más tarde» sí lo es.</p>")}
<h3>Texto modelo: el teléfono en la mesa</h3>
<p>Lea el texto. Después pulse <strong>Mostrar las partes</strong> para ver cómo está construido.</p>
<p>{LE.escuchar(plano(MODELO), "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-partes" aria-pressed="false">Mostrar las partes</button></p>
<div class="texto-lectura" id="modelo-71"><p><strong>Un rato sin pantallas</strong></p><p>{MODELO}</p></div>
<p class="leyenda-partes" id="ley-71"><span style="background:#dbeafe">Postura</span><span style="background:#dcfce7">Razón</span><span style="background:#fef3c7">Conector</span><span style="background:#fce7f3">Conclusión</span></p>
<p class="fuente">Texto escrito para esta lección. La recomendación citada es de la Academia Estadounidense de Pediatría (healthychildren.org, «How to Make a Family Media Plan»), que sugiere zonas sin pantallas como la mesa del comedor. Consultado el 28 de noviembre de 2026.</p>
<script>(function(){{var b=document.getElementById("btn-partes"),t=document.getElementById("modelo-71"),l=document.getElementById("ley-71");b.addEventListener("click",function(){{var on=t.classList.toggle("partes-on");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las partes":"Mostrar las partes";}});}})();</script>
{C.caja("tip", "Fíjese", "<p>Cada razón tiene su apoyo. La razón 1 se apoya en un hecho de la vida diaria (padres que trabajan, hijos que estudian) y la razón 2, en la recomendación de una organización de médicos. El autor también reconoce una objeción («es cierto que…») y la responde.</p>")}
{P("Comprueba 1", "¿Qué apoyo tiene la razón 2?", ["Que los padres trabajan y los hijos estudian", "La recomendación de la Academia de Pediatría", "Que a veces hay llamadas urgentes"], 1, {0: "Ese es el apoyo de la razón 1.", 2: "Esa es la objeción."}, "Una organización de médicos aconseja zonas sin pantallas.")}
{P("Comprueba 2", "¿Qué objeción reconoce el autor?", ["Que la cena dura muy poco tiempo", "Que a veces hay que contestar una llamada urgente", "Que los niños no quieren conversar"], 1, {0: "El texto no lo dice.", 2: "El texto no lo dice."}, "«Es cierto que a veces hay que contestar una llamada urgente».")}"""

    s2 = f"""<p>Una opinión sin apoyo solo repite lo que usted piensa con más fuerza. Una razón apoyada le da al lector algo que puede comprobar: un hecho, un dato, un ejemplo o lo que dice un experto.</p>
{C.tabla("Opiniones sin apoyo frente a razones apoyadas", ["Sin apoyo", "Con apoyo"],
         [["El transporte público es lo mejor y punto.", "El transporte público ahorra dinero: un pase mensual puede costar menos que la gasolina y el estacionamiento de un mes."],
          ["Todo el mundo sabe que leer es bueno.", "Leer con los niños amplía su vocabulario, porque oyen palabras que no se usan en la conversación diaria."],
          ["Caminar es muy, muy saludable.", "Caminar es saludable: los CDC recomiendan a los adultos unos 150 minutos de actividad moderada a la semana, como caminar rápido."]], fila_th=False)}
<p class="fuente">Dato de los CDC (Centros para el Control y la Prevención de Enfermedades de los EE. UU.), recomendaciones de actividad física para adultos. Consultado el 28 de noviembre de 2026.</p>
{C.caja("ojo", "Cuidado con las señales vacías", "<p>«Todo el mundo sabe», «es obvio», «y punto», «sin duda» no prueban nada. Pregúntese siempre: <strong>«¿Y cómo lo sé?»</strong>. La respuesta a esa pregunta es el apoyo.</p>")}
{P("¿Con apoyo? 1", "«Los parques mejoran la salud: dan un lugar gratuito para caminar y hacer ejercicio.»", AS, 0, {1: "Da un hecho que se puede comprobar."}, "<strong>Con apoyo.</strong>")}
{P("¿Con apoyo? 2", "«Todo el mundo sabe que la comida rápida es mala.»", AS, 1, {0: "«Todo el mundo sabe» no prueba nada."}, "<strong>Sin apoyo</strong>: señal vacía.")}
<h3>Conectores</h3>
{C.tabla("Conectores para el texto de opinión", ["Para…", "Conectores"],
         [["Dar la postura", "creo que, en mi opinión, considero que, pienso que"], ["Explicar la causa", "porque, ya que, puesto que"], ["Ordenar y añadir razones", "en primer lugar, en segundo lugar, además, también, por otra parte"],
          ["Mostrar la consecuencia", "por lo tanto, por eso, así que"], ["Reconocer una objeción", "es cierto que…; sin embargo, aunque"], ["Concluir", "en conclusión, en resumen, por todo esto"]])}
{C.caja("tip", "Puntuación", "<p>Los conectores como <em>además, sin embargo, por lo tanto, en conclusión</em> llevan coma detrás cuando empiezan la oración: «Además, …». Lo vio en la Lección 3.1.</p>")}
{P("Conector 1", "«El alquiler sube cada año. ___, muchas familias se mudan a las afueras.»", ["Por lo tanto", "Además", "En primer lugar"], 0, {1: "No añade: muestra un resultado.", 2: "No ordena razones."}, "Muestra una consecuencia.")}
{P("Conector 2", "«Es cierto que la ciudad es ruidosa; ___, ofrece más trabajo.»", ["por eso", "sin embargo", "también"], 1, {0: "No es una consecuencia.", 2: "No suma: contrasta."}, "Responde a la objeción.")}"""

    s3 = f"""<p>Este segundo texto no tiene marcas. Léalo y responda.</p>
{LE.escuchar(" ".join(RECICLAR), "Escuchar el texto")}
<div class="texto-lectura"><p><strong>Reciclar empieza en casa</strong></p>{"".join(f'<p><span class="num-p">{i}</span> {t}</p>' for i, t in enumerate(RECICLAR, 1))}</div>
<p class="fuente">Texto escrito para esta lección.</p>
{P("Partes 1", "¿Cuál es la postura del texto?", ["El edificio necesita contenedores para reciclar", "La basura del edificio huele mal en verano", "Los vecinos deberían comprar menos cosas"], 0, {1: "El texto no lo dice.", 2: "El texto no lo dice."}, "Primera oración del párrafo 1.")}
{P("Partes 2", "¿Cuántas razones da en el párrafo 2?", ["Una", "Dos", "Cuatro"], 1, {0: "Busque «en primer lugar» y «además».", 2: "Busque «en primer lugar» y «además»."}, "Ahorra energía y reduce la basura.")}
{P("Partes 3", "¿Qué hace el párrafo 3?", ["Da una tercera razón a favor", "Responde a una objeción", "Presenta la conclusión del texto"], 1, {0: "Fíjese en «Algunos vecinos dicen…».", 2: "La conclusión está en el párrafo 4."}, "«Algunos vecinos dicen…; sin embargo…».")}
{P("Partes 4", "¿Qué pide el autor al final?", ["Que la administración instale los contenedores", "Que los vecinos limpien mejor el edificio", "Que la ciudad suba las multas por la basura"], 0, {1: "El texto no lo pide.", 2: "El texto no lo pide."}, "Una conclusión puede terminar con una petición.")}
<h3>Taller: escriba su texto de opinión</h3>
<p>Elija un tema o proponga uno suyo: ¿Deberían los adolescentes trabajar mientras estudian? · ¿Es mejor vivir en la ciudad o en un pueblo? · ¿Deberían las escuelas ofrecer clases en dos idiomas? · ¿Conviene comprar en línea o en la tienda?</p>
<p>Planifique con esta plantilla antes de escribir:</p>
<div class="caja caja-tip"><p><strong>Postura:</strong> Creo que ______.<br><strong>Razón 1:</strong> En primer lugar, ______ porque ______ (hecho o ejemplo).<br><strong>Razón 2:</strong> Además, ______. Por ejemplo, ______.<br>
<strong>Objeción (opcional):</strong> Es cierto que ______; sin embargo, ______.<br><strong>Conclusión:</strong> En conclusión, ______.</p></div>
{taller("2-7-1", "Su texto de opinión (6 a 8 oraciones)", "Creo que… En primer lugar, … Además, … En conclusión, …", 6, 70, CONECTORES,
        ["Mi postura está en la primera oración.", "Doy al menos dos razones.", "Cada razón tiene un hecho, un dato o un ejemplo.", "Uso al menos tres conectores distintos.", "Mi conclusión repite la postura con otras palabras.", "Escuché mi texto en voz alta y revisé la ortografía y la puntuación."])}
{C.tabla("Rúbrica del texto de opinión", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Inicial"],
         [["Postura clara", "Clara desde la primera oración y se mantiene", "Clara, pero aparece tarde", "Se adivina, pero no se dice", "No hay postura"],
          ["Razones con apoyo", "Dos o tres razones, todas con hechos o ejemplos", "Dos razones; una sin apoyo", "Una razón con apoyo", "Solo opiniones sin apoyo"],
          ["Conectores", "Variados y bien usados", "Algunos, bien usados", "Pocos o repetidos", "Ninguno"],
          ["Conclusión", "Retoma la postura con otras palabras", "Repite la postura igual", "Cierra sin relación con la postura", "No hay conclusión"]])}
<p>Total: 16 puntos.</p>
<p>Si tiene con quién practicar, cada uno dice en voz alta su postura sobre un tema y una razón. El otro tiene que añadir un conector y una segunda razón.</p>"""

    secciones = [("s1", "Las cuatro partes y un texto modelo", s1), ("s2", "Razones con apoyo y conectores", s2), ("s3", "Encuentre las partes y escriba su texto", s3)]
    tarea = [("Para el foro.", "Termine su texto de opinión del taller (6 a 8 oraciones, con postura, dos razones apoyadas y conclusión). Pulse «Copiar mi texto» y péguelo en el foro del curso o entréguelo a su maestro."),
             ("Comente a un compañero.", "Lea el texto de otra persona y responda: ¿cuál es su postura? ¿Qué razón le convenció más y por qué?"),
             ("Caza de conectores.", "Busque una carta al editor o una columna de opinión en un periódico. Copie cinco conectores y diga para qué sirve cada uno.")]
    quiz = [
        ("En un texto de opinión, la <strong>postura</strong> es…", ["lo que el autor piensa sobre el tema", "el dato más importante del texto", "la última oración del texto"], 0, {1: "Un dato es un apoyo.", 2: "Puede estar en cualquier lugar, mejor al principio."}, "Lo que el autor <strong>piensa</strong>."),
        ("¿Cuál de estas oraciones es una <strong>postura clara</strong>?", ["La ciudad debería abrir las piscinas públicas todo el verano.", "Las piscinas públicas tienen cosas buenas y también cosas malas.", "En el verano hace mucho calor en Chicago y en otras ciudades."], 0, {1: "No toma partido.", 2: "Es un dato."}, "Toma partido."),
        ("¿Dónde conviene poner la postura?", ["Al principio del texto", "En medio de las razones", "Solo en la conclusión"], 0, {1: "El lector se pierde.", 2: "La conclusión la repite."}, "Al <strong>principio</strong>."),
        ("¿Cuál es una <strong>razón con apoyo</strong>?", ["Las vacunas protegen: gracias a ellas se erradicó la viruela.", "Las vacunas son buenas, eso lo sabe todo el mundo.", "Las vacunas son lo mejor, sin ninguna duda."], 0, {1: "Señal vacía.", 2: "Señal vacía."}, "Da un <strong>hecho</strong>."),
        ("La pregunta que le ayuda a encontrar el apoyo de una razón es…", ["¿Y cómo lo sé?", "¿Me gusta esta idea?", "¿Es corta la oración?"], 0, {1: "El gusto no es apoyo.", 2: "El largo no importa."}, "<strong>¿Y cómo lo sé?</strong>"),
        ("«Llovió toda la semana; ___, el partido se suspendió.»", ["por lo tanto", "además", "en primer lugar"], 0, {1: "No suma.", 2: "No ordena."}, "Consecuencia."),
        ("«El curso es gratuito. ___, se puede tomar en línea.»", ["Además", "Sin embargo", "En conclusión"], 0, {1: "No hay contraste.", 2: "No es el cierre."}, "Añade."),
        ("¿Qué conector sirve para responder a una objeción?", ["sin embargo", "además", "por ejemplo"], 0, {1: "Suma.", 2: "Da ejemplos."}, "<strong>Sin embargo.</strong>"),
        ("¿Cuál es la mejor <strong>conclusión</strong> para un texto que defiende los huertos comunitarios?", ["En resumen, un huerto comunitario da comida fresca y une a los vecinos.", "Las zanahorias del huerto tardan un par de meses en crecer.", "Mi vecina, que vive en el tercer piso, tiene un perro que ladra mucho."], 0, {1: "Es un detalle.", 2: "No tiene relación."}, "Retoma la postura."),
        ("Antes de entregar un texto de opinión, conviene…", ["leerlo en voz alta y revisar la lista", "hacerlo más largo con frases repetidas", "quitar todos los conectores"], 0, {1: "Repetir no ayuda.", 2: "Los conectores ayudan."}, "<strong>Leerlo y revisarlo.</strong>"),
    ]
    filas = [
        ("Postura", "Escribo mi postura en la primera oración, con claridad.", "Mi postura aparece tarde.", "No tomo partido (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Razones y conectores", "Doy dos razones con apoyo y uso conectores variados.", "Una razón no tiene apoyo.", "Solo repito mi opinión (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Mi texto", "Escribí 6 a 8 oraciones con las cuatro partes y lo revisé.", "Me falta una parte.", "No terminé el texto (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya escribe un texto de opinión con sus cuatro partes. En la próxima lección escribirá un <strong>texto informativo</strong> organizado en categorías.</p>"
    glosario = [("Postura", "Lo que el autor piensa sobre el tema."), ("Razón con apoyo", "Motivo respaldado por un hecho, un dato, un ejemplo o un experto."),
                ("Objeción", "Lo que diría alguien que no está de acuerdo."), ("Señal vacía", "Expresión como «es obvio» que no prueba nada.")]
    conexion = ("<p>En la Lección 2.3 aprendió a unir ideas con conectores, y en la 5.1 a reconocer el punto de vista de un autor. Hoy usará las dos cosas para escribir su propia opinión.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un tema que le importe.</p>")
    estd = LE.estandares(["W.2", "L.1.9"], base=["R.8.2", "R.8.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Decir lo que piensa, explicar por qué y apoyarlo.", ["Escritura", "Opinión"],
                            ["<strong>Reconocer</strong> las cuatro partes de un texto de opinión.", "<strong>Distinguir</strong> razones con apoyo de opiniones sin apoyo.",
                             "<strong>Usar</strong> conectores con su puntuación.", "<strong>Escribir</strong> un texto de opinión de 6 a 8 oraciones."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-2", LE.titulo("7-2")), glosario, P)


def practica():
    po = [{"enun": f'<div class="texto-lectura"><p>{t}</p></div><strong>¿Cuál es la postura del autor?</strong>', "ops": ops, "ok": 0,
           "pista": "La postura es lo que el autor quiere que usted piense, no un dato ni una razón.", "exp": e} for t, ops, e in POSTURA_T]
    po += [{"enun": "<strong>¿Cuál de estas oraciones es una postura clara?</strong>", "ops": ops, "ok": 0, "pista": "Una postura toma partido y se puede defender con razones.", "exp": e} for ops, e in POSTURA_Q]
    ra = [{"enun": f"<span class=\"grande\">{t}</span><br>¿Tiene apoyo?", "ops": AS, "ok": k, "enOrden": True, "pista": "Pregúntese: «¿Y cómo lo sé?». ¿La oración responde a esa pregunta?",
           "exp": f"<strong>{AS[k]}</strong>. {e}"} for t, k, e in RAZ]
    def may(s): return s[0].upper() + s[1:]
    co = [{"enun": f"<span class=\"grande\">«{o.replace('___', '_____')}»</span><br>¿Qué conector completa mejor la oración?", "ops": ops, "ok": 0,
           "pista": "¿Qué relación hay entre las dos ideas: causa, suma, consecuencia, contraste o cierre?", "exp": f"«{may(o.replace('___', ops[0]))}» · {e}"} for o, ops, e in CON]
    mods = [("postura", "La postura", C.om("m1", "Encuentre la postura del autor o la oración que toma partido.")), ("apoyo", "¿Con apoyo o sin apoyo?", C.om("m2", "Decida si la razón tiene apoyo.")),
            ("conectores", "Elija el conector", C.om("m3", "Elija el conector que completa mejor la oración."))]
    js = C.js_datos("PO", po) + C.js_datos("RA", ra) + C.js_datos("CO", co) + 'creaBanco("m1", PO);\ncreaBanco("m2", RA);\ncreaBanco("m3", CO);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
