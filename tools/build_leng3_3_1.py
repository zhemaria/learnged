# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 3.1 · Tema central, ideas principales y resumen objetivo.
Fuente: clases_leng3/clase_3-1.html (GEDparaHispanos) y gramatica/n3-l3-1.html, adaptadas al marco de LearnGED.
Datos del agua de Chicago: Ciudad de Chicago, Departamento de Agua, «Water Supply» (chicago.gov); Biblioteca de la Universidad de
Chicago, «Chicago's Water Tunnels» (lib.uchicago.edu); Chicago Sun-Times, 30 de junio de 2026 (tuberías de plomo). Consultados en noviembre de 2026.
Uso: python3 tools/build_leng3_3_1.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "3-1"


def I(t):
    return f'<span class="idea">{t}</span>'


AGUA = [f"Cada vez que alguien abre una llave en Chicago, el agua que sale ha hecho un largo viaje desde el lago Míchigan. {I('Que esa agua llegue limpia a las casas es el resultado de más de ciento cincuenta años de ingeniería y de lecciones aprendidas, muchas veces a un alto precio.')}",
        f"{I('A mediados del siglo XIX, la ciudad tomaba el agua cerca de la orilla, en el mismo lago donde echaba sus aguas negras.')} Las enfermedades que viajan por el agua, como el cólera y la fiebre tifoidea, eran frecuentes. Para alejarse de la contaminación, la ciudad construyó una toma de agua a unos tres kilómetros de la costa, unida a la tierra por un túnel bajo el lago. Se terminó en 1867.",
        f"{I('Pero el problema seguía, porque las aguas negras llegaban al lago por el río Chicago. En 1900, la ciudad tomó una medida atrevida: con un gran canal, invirtió el curso del río para que corriera lejos del lago.')} Desde entonces, el río fluye hacia el interior, rumbo a la cuenca del río Misisipi.",
        f"{I('Hoy el sistema es mucho más grande y seguro.')} Dos tomas de agua, a unos tres kilómetros de la orilla, envían el agua por túneles a unos sesenta metros bajo el fondo del lago. Llega a dos plantas de purificación, una de ellas junto a Navy Pier, considerada la más grande del mundo. Allí el agua se filtra y se desinfecta antes de llegar a la ciudad y a más de cien suburbios.",
        f"{I('Sin embargo, el trabajo no ha terminado.')} Muchas casas antiguas todavía reciben el agua por tuberías de plomo, un metal que puede dañar la salud, sobre todo la de los niños. Chicago es la ciudad del país con más tuberías de este tipo: unas 400 000. La ciudad tiene un plan para reemplazarlas, pero tardará muchos años en completarlo."]
RES = [("A", "El texto explica cómo Chicago llegó a tener agua limpia. En el siglo XIX, la ciudad tomaba agua contaminada cerca de la orilla, y para resolverlo construyó una toma lejos de la costa y, en 1900, invirtió el curso del río. Hoy dos tomas y dos plantas purifican el agua para la ciudad y sus suburbios, aunque todavía falta reemplazar las tuberías de plomo."),
       ("B", "Es increíble lo que hizo Chicago con su agua. Los ingenieros del siglo XIX fueron unos genios, sobre todo los que invirtieron el río. Hoy tenemos la mejor planta del mundo, pero la ciudad debería darse prisa con las tuberías de plomo, porque es injusto que los niños sigan en peligro."),
       ("C", "En 1867 se terminó una toma de agua a tres kilómetros de la costa. En 1900 se invirtió el río Chicago. Los túneles están a sesenta metros bajo el fondo del lago. Una planta está junto a Navy Pier. El plomo puede dañar la salud de los niños.")]
TEXTOS = [
    (["En muchas ciudades, los huertos comunitarios han convertido terrenos abandonados en lugares verdes donde los vecinos cultivan verduras.",
      "Además de comida fresca, estos huertos reúnen a personas de distintas edades y culturas, que se ayudan y comparten lo que saben.",
      "Muchos vecinos cuentan también que, desde que hay huerto, el barrio tiene menos basura en la calle y más actividad al aire libre."],
     ["Los huertos comunitarios benefician a los barrios de varias maneras.", "Los huertos dan verduras frescas a los vecinos de la ciudad.", "Los vecinos notan menos basura en las calles de los barrios."],
     "Cada párrafo da un beneficio distinto: comida, convivencia y un barrio más limpio y activo.",
     ["El texto explica que los huertos comunitarios ayudan a los barrios: dan comida fresca, unen a los vecinos y se relacionan con calles más limpias y activas.",
      "Los huertos comunitarios son lo mejor que le puede pasar a un barrio, y todas las ciudades del país deberían tener uno en cada una de sus calles.",
      "En los huertos se cultivan verduras. Hay personas de distintas edades y culturas. Hay menos basura. La gente sale más a la calle de su barrio."],
     "El primero dice el tema central y las tres ideas, sin opinar. El segundo opina; el tercero es una lista sin tema central."),
    (["El primer tren subterráneo del mundo se abrió en Londres en 1863. Sus vagones eran de madera y los movían locomotoras de vapor.",
      "Con el tiempo llegaron los trenes eléctricos, más limpios y rápidos, y otras grandes ciudades construyeron sus propios metros.",
      "Hoy los metros transportan a millones de personas cada día y siguen cambiando: algunos ya funcionan sin conductor."],
     ["El metro ha cambiado mucho desde su origen y sigue transformándose.", "El primer metro, en Londres, tenía vagones de madera y de vapor.", "Algunos metros modernos ya funcionan sin ningún conductor a bordo."],
     "El texto sigue la historia del metro de su origen a hoy. Las otras opciones son detalles de un párrafo.", None, None),
    (["Dormir poco no solo produce cansancio. Quien duerme mal tiene más dificultad para concentrarse y recordar lo que aprendió.",
      "La falta de sueño también afecta el humor: las personas se irritan con más facilidad y toman peores decisiones.",
      "Por último, a largo plazo, dormir mal se relaciona con problemas del corazón y con un sistema de defensas más débil."],
     ["Dormir poco perjudica la mente, el ánimo y la salud.", "Dormir poco produce mucho cansancio durante el día.", "Las personas que duermen mal se enojan con facilidad."],
     "Los tres párrafos son tres clases de daño: en la mente, en el ánimo y en el cuerpo.",
     ["Según el texto, dormir poco afecta la concentración y la memoria, empeora el humor y las decisiones, y a largo plazo daña el corazón y las defensas.",
      "Dormir poco es lo peor que uno puede hacerse, y la gente debería acostarse temprano todos los días de la semana, sin ninguna excepción.",
      "Quien duerme mal recuerda menos y se concentra peor, según dice el primer párrafo del texto, y eso le pasa a mucha gente que trabaja."],
     "El primero resume todo el texto en orden y sin opinar."),
    (["Durante años, las fábricas de la región echaron sus desechos al río. Los peces desaparecieron y nadie se atrevía a bañarse en sus aguas.",
      "Un día, los vecinos se organizaron, presionaron a las autoridades y lograron leyes más estrictas para las fábricas.",
      "Hoy el río tiene peces otra vez, y los sábados las familias van a pasear por la orilla que antes evitaban."],
     ["La presión de los vecinos logró recuperar un río contaminado.", "Las fábricas de la región contaminaron el río durante años.", "Las familias pasean los sábados por la orilla del río."],
     "El texto va del problema a la acción de los vecinos y a la solución: esa es la idea que une todo.",
     ["El texto cuenta cómo un río contaminado por las fábricas se recuperó gracias a que los vecinos se organizaron y lograron leyes más estrictas.",
      "Las fábricas son malas porque contaminan, y por suerte los vecinos valientes de la región lograron vencerlas al final de una larga lucha.",
      "Hoy las familias de la región van a pasear los sábados por la orilla del río, que antes todos evitaban porque el agua estaba muy sucia."],
     "El primero da el problema, la acción y el resultado, sin juicios."),
    (["Aprender un segundo idioma de adulto es más difícil que de niño, pero no imposible. Los adultos tienen ventajas que los niños no tienen.",
      "Por ejemplo, un adulto puede usar lo que ya sabe de gramática en su propia lengua para entender la nueva, y sabe organizar su tiempo de estudio.",
      "Además, los adultos suelen tener una razón clara para aprender, como un trabajo mejor, y esa meta los ayuda a no rendirse."],
     ["Los adultos tienen ventajas propias para aprender otro idioma.", "Aprender un segundo idioma de adulto es imposible.", "Los niños aprenden idiomas más rápido que los adultos."],
     "El primer párrafo lo anuncia y los otros dos dan las ventajas. La segunda opción contradice el texto.",
     ["La autora sostiene que aprender un idioma de adulto es difícil pero posible, porque los adultos aprovechan lo que saben de su lengua, se organizan y tienen metas.",
      "Aprender idiomas es facilísimo a cualquier edad, y cualquier persona puede hablar uno nuevo con solo un mes de estudio, aunque no tenga una meta clara.",
      "Los adultos saben organizar su tiempo de estudio mucho mejor que los niños, que todavía no tienen esa costumbre ni esa disciplina para aprender."],
     "El primero tiene la idea central y sus razones. El segundo exagera y dice lo contrario del texto."),
    (["El maíz se cultivaba en México hace miles de años. Los pueblos antiguos lo seleccionaron a partir de una planta silvestre con granos muy pequeños.",
      "Después de 1492, el maíz viajó a Europa, África y Asia, donde se convirtió en un alimento básico para millones de personas.",
      "Hoy es uno de los cultivos más importantes del planeta y se usa para comida, para alimentar ganado y hasta para fabricar combustible."],
     ["El maíz pasó de ser una planta mexicana a un cultivo de todo el mundo.", "El maíz salió de una planta silvestre que tenía granos muy pequeños.", "Hoy el maíz se usa para alimentar ganado y para fabricar combustible."],
     "El texto sigue el viaje del maíz desde México hasta el mundo entero.",
     ["El texto explica que el maíz, cultivado primero en México, se extendió por el mundo después de 1492 y hoy es uno de los cultivos más importantes.",
      "El maíz es el alimento más rico del mundo, y todos los mexicanos deberían sentirse orgullosos de haberlo cultivado primero hace tantos años.",
      "Después de 1492 el maíz llegó a Europa, a África y a Asia, donde se volvió un alimento básico para millones de personas de esos continentes."],
     "El primero sigue el viaje del maíz completo y no opina.")]
OB = [("El texto explica cómo funciona una planta de purificación de agua.", 0, "Dice de qué trata, sin juzgar."),
      ("Por suerte, la ciudad decidió invertir el curso del río.", 1, "<em>Por suerte</em> es un juicio de quien resume."),
      ("Según el autor, los huertos reducen la basura en las calles.", 0, "Atribuye la idea al autor: es objetiva."),
      ("Los vecinos hicieron un trabajo admirable para limpiar el río.", 1, "<em>Admirable</em> es una opinión."),
      ("El artículo describe tres beneficios de dormir bien.", 0, "Cuenta lo que hace el texto."),
      ("El gobierno debería invertir más dinero en los metros.", 1, "<em>Debería</em> es una opinión, salvo que lo diga el autor."),
      ("Después, el maíz llegó a Europa, África y Asia.", 0, "Un hecho del texto."),
      ("Es injusto que tantas casas todavía tengan tuberías de plomo.", 1, "<em>Injusto</em> es un juicio."),
      ("La autora sostiene que los adultos tienen ventajas para aprender idiomas.", 0, "Cuenta lo que sostiene la autora, sin opinar sobre ello."),
      ("El texto es aburrido, pero tiene datos interesantes.", 1, "Opina sobre el texto en vez de resumirlo."),
      ("Al final, el autor advierte que el problema no está resuelto.", 0, "Dice lo que hace el autor."),
      ("Lamentablemente, las fábricas contaminaron el río durante años.", 1, "<em>Lamentablemente</em> añade un sentimiento de quien resume."),
      ("El primer metro del mundo se abrió en Londres en 1863.", 0, "Un hecho que da el texto."),
      ("Los ingenieros de Chicago fueron unos genios.", 1, "<em>Genios</em> es una opinión.")]
OBT = ["Objetiva", "Con opinión"]


def texto(ps):
    return '<div class="texto-breve">' + "".join(f"<p>{p}</p>" for p in ps) + "</div>"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Si alguien le pregunta de qué trata una película, puede contestar «de una familia» o «de una familia que lo pierde todo y aprende a empezar de nuevo». La primera respuesta dice el <strong>tema</strong>; la segunda, el <strong>tema central</strong>: lo que la película quiere decir sobre ese tema. En el GED, las preguntas sobre la idea central y el resumen piden siempre la segunda clase de respuesta.</p>
<p>En el Nivel 2 aprendió que la <strong>idea principal</strong> de un párrafo es lo más importante que dice, y que los <strong>detalles de apoyo</strong> la explican con datos, ejemplos o razones. Muchas veces la idea principal está en la primera oración del párrafo, pero puede estar al final o no estar escrita.</p>
<p>Ahora los textos son más largos: tienen varias partes, y cada una tiene su propia idea principal. El trabajo de esta lección es ver cómo esas ideas se juntan en una sola.</p>"""

    s2 = f"""{C.tabla("Diferencia entre tema, tema central e idea principal", ["Concepto", "Qué es", "Cómo se dice", "Ejemplo"],
         [["Tema", "El asunto del texto: de qué trata.", "Unas pocas palabras.", "el agua de Chicago"],
          ["Tema central (o idea central)", "Lo que el autor dice sobre ese asunto en todo el texto.", "Una oración completa.", "El agua limpia de Chicago es el resultado de muchos años de soluciones a la contaminación, y el trabajo todavía no termina."],
          ["Ideas principales", "Lo más importante de cada párrafo o sección.", "Una oración por parte.", "En el siglo XIX, el agua de la ciudad estaba contaminada."]])}
{C.caja("tip", "Una imagen", "<p>Piense en una mesa. Las ideas principales son las <strong>patas</strong> y el tema central es la <strong>tabla</strong> que se apoya en todas ellas. Si una idea no sostiene la tabla, probablemente es un detalle.</p>")}
{C.caja("ojo", "El error más común", "<p>Elegir como tema central un detalle llamativo (una fecha, una cifra, un nombre) o una idea que solo aparece en un párrafo. El tema central tiene que valer para <strong>todo</strong> el texto.</p>")}
{P("Tema 1", "¿Cuál podría ser un <strong>tema</strong>?", ["Las aves migran para sobrevivir al invierno.", "La migración de las aves", "Muchas aves viajan miles de kilómetros."], 1, {0: "Es una oración completa: sería un tema central.", 2: "Es una oración con un detalle."}, "El tema se dice en <strong>pocas palabras</strong>.")}
{P("Tema 2", "Un texto habla, párrafo por párrafo, de los beneficios del ejercicio para el corazón, el sueño y el ánimo. ¿Cuál es su tema central?", ["El ejercicio ayuda a dormir mejor por la noche.", "Hay que caminar treinta minutos al día.", "El ejercicio beneficia la salud de varias maneras."], 2,
   {0: "Es la idea de un solo párrafo.", 1: "El texto no lo dice."}, "Es la idea que vale para los tres párrafos.")}"""

    s3 = f"""<ol class="proceso"><li>Mire el <strong>título</strong> y, si hay, los subtítulos: casi siempre dicen el tema.</li>
<li>Lea el <strong>primer y el último párrafo</strong> con atención: allí el autor suele presentar y cerrar su idea.</li>
<li>Anote la <strong>idea principal de cada párrafo</strong> en una oración corta, al margen o en su cuaderno.</li>
<li>Busque lo que tienen en común esas ideas y escríbalo en una oración: «El autor quiere que entienda que…».</li>
<li><strong>Compruebe:</strong> ¿su oración vale para todos los párrafos? ¿Hay alguno que no encaje? Si lo hay, ajústela.</li></ol>"""

    lect = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(AGUA, 1))
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in AGUA)
    s4 = f"""<p>Lea el texto y escriba en su cuaderno la idea principal de cada párrafo, en una oración. Luego pulse <strong>Mostrar las ideas principales</strong> y compare. Por último, escriba el tema central.</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-i31" aria-pressed="false">Mostrar las ideas principales</button></p>
<div class="articulo lectura-cl" id="lect-31"><p><strong>El agua que bebe Chicago</strong></p>{lect}</div>
<p class="fuente">Datos: Ciudad de Chicago, Departamento de Agua, «Water Supply» (chicago.gov); Biblioteca de la Universidad de Chicago, «Chicago’s Water Tunnels»; <em>Chicago Sun-Times</em>, 30 de junio de 2026, sobre las tuberías de plomo. Consultados en noviembre de 2026.</p>
<script>(function(){{var b=document.getElementById("btn-i31"),t=document.getElementById("lect-31");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las ideas principales":"Mostrar las ideas principales";}});}})();</script>
<h3>Compruebe su lectura</h3>
{P("Agua 1", "¿Cuál es el <strong>tema</strong> del texto?", ["La historia del lago Míchigan", "El agua potable de Chicago", "Las enfermedades del siglo XIX"], 1, {0: "El lago aparece, pero el texto habla del agua que se bebe.", 2: "Solo se mencionan en el párrafo 2."}, "El tema se dice en pocas palabras: de qué trata todo el texto.")}
{P("Agua 2", "¿Cuál es el <strong>tema central</strong>?", ["Chicago tiene la planta de purificación de agua más grande del mundo, que está junto a Navy Pier.", "En 1900 Chicago invirtió el curso del río con un canal para que corriera lejos del lago Míchigan.", "El agua limpia de Chicago es fruto de muchos años de soluciones a la contaminación, y el trabajo continúa."], 2,
   {0: "Es un detalle del párrafo 4.", 1: "Es la idea del párrafo 3."}, "Es la única idea que vale para los cinco párrafos.")}
{P("Agua 3", "¿Cuál es la idea principal del párrafo 2?", ["El cólera y la fiebre tifoidea son enfermedades que viajan por el agua.", "En el siglo XIX la ciudad tomaba agua contaminada cerca de la orilla.", "La primera toma de agua lejos de la costa se terminó en 1867."], 1,
   {0: "Es un detalle que apoya la idea.", 2: "Es un detalle: una fecha."}, "Las enfermedades y la fecha son detalles que apoyan esa idea.")}
{P("Agua 4", "¿Para qué sirve el párrafo 5 dentro del texto?", ["Explica cómo funcionan por dentro las plantas de purificación", "Muestra que el problema del agua todavía no está resuelto del todo", "Cuenta la historia de las primeras tuberías de la ciudad"], 1,
   {0: "Eso está en el párrafo 4.", 2: "Habla de las tuberías de hoy, no de su historia."}, "Con «Sin embargo, el trabajo no ha terminado» el autor añade la última parte del tema central.")}
{P("Agua 5", "«La planta junto a Navy Pier es la más grande del mundo.» ¿Qué es esta información en el texto?", ["El tema central del texto", "La idea principal del párrafo 1", "Un detalle de apoyo del párrafo 4"], 2,
   {0: "Es demasiado concreta para todo el texto.", 1: "Está en el párrafo 4."}, "Apoya la idea de que hoy el sistema es más grande y seguro.")}"""

    s5 = f"""<p>Un <strong>resumen objetivo</strong> cuenta lo esencial de un texto como lo contaría un testigo imparcial. Tiene cinco reglas:</p>
{C.tabla("Reglas del resumen objetivo", ["Sí", "No"],
         [["Empieza con el tema central.", "Empezar con un detalle o una fecha."], ["Responde quién, qué y cómo (y cuándo o por qué, si importa).", "Copiar todas las cifras y los nombres."],
          ["Usa sus palabras.", "Copiar oraciones del texto."], ["Sigue el orden del texto.", "Saltar de una parte a otra."],
          ["Es neutral: dice lo que dice el autor.", "Dar su opinión (<em>me parece, es increíble, deberían</em>) o añadir cosas que el texto no dice."]])}
<h3>Una plantilla para empezar</h3>
<p class="formula">El texto «___» explica que ___ [tema central]. Primero, ___. Después, ___. Por último, ___.</p>
{C.caja("tip", "¿Qué tan largo?", "<p>Para un texto como el de la lectura, de tres a cinco oraciones. Si su resumen tiene casi el mismo largo que el texto, no es un resumen: es una copia.</p>")}
{C.caja("ojo", "Las palabras que delatan una opinión", "<p><em>increíble, mejor, peor, genial, injusto, debería, me parece, por suerte, lamentablemente</em>. Si alguna aparece en su resumen, pregúntese si la dice el autor o la dice usted.</p>")}
{P("Objetiva 1", "En un resumen, «Por suerte, la ciudad decidió invertir el curso del río» es una oración…", OBT, 1, {0: "Busque una palabra que juzgue."}, "<em>Por suerte</em> es un juicio de quien resume.")}
{P("Objetiva 2", "En un resumen, «Al final, el autor advierte que el problema no está resuelto» es una oración…", OBT, 0, {1: "Cuenta lo que hace el autor, sin juzgarlo."}, "Dice lo que hace el autor: es objetiva.")}
<h3>Compare tres resúmenes</h3>
<p>Tres personas resumieron «El agua que bebe Chicago». Léalos y responda.</p>
{"".join(f'<div class="texto-breve"><p><strong>Resumen {k}.</strong> {t}</p></div>' for k, t in RES)}
{P("Resúmenes 1", "¿Qué resumen es objetivo y completo?", ["El resumen A", "El resumen B", "El resumen C"], 0, {1: "Busque las palabras que delatan una opinión.", 2: "¿Dice de qué trata el texto?"}, "Empieza con el tema central, sigue el orden del texto, usa otras palabras y no opina.")}
{P("Resúmenes 2", "¿Qué problema tiene el resumen B?", ["Copia todas las fechas del texto", "Mete opiniones que el texto no dice", "Está escrito en un orden distinto"], 1, {0: "No tiene fechas.", 2: "Sigue el orden."}, "<em>Increíble, genios, la mejor, debería, injusto</em>: son opiniones de quien escribe.")}
{P("Resúmenes 3", "¿Qué problema tiene el resumen C?", ["Tiene muchas opiniones de quien lo escribe", "Habla de cosas que el texto nunca dice", "Es una lista de detalles sin tema central"], 2, {0: "No opina.", 1: "Todos los datos están en el texto."}, "Son datos ciertos, pero no dice de qué trata el texto ni cómo se relacionan.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Después de ver una noticia en la televisión, cada uno la resume en tres oraciones sin opinar. Luego comparen: ¿alguien metió una opinión sin darse cuenta?</p>")}"""

    secciones = [("s1", "Repaso: la idea principal", s1), ("s2", "Tema, tema central e ideas principales", s2), ("s3", "Cómo encontrar el tema central", s3),
                 ("s4", "Lectura: «El agua que bebe Chicago»", s4), ("s5", "El resumen objetivo", s5)]
    tarea = [("Su resumen.", "Escriba su propio resumen objetivo de «El agua que bebe Chicago» con la plantilla de la <a href=\"#s5\">sección 5</a>. Revise que no tenga ninguna palabra de opinión."),
             ("Tema y tema central.", "Piense en una película o un libro que conozca bien. Escriba su tema en pocas palabras y su tema central en una oración completa. "
              "<details class=\"transc\"><summary>Ver un ejemplo</summary><p>Película: <em>Coco</em>. Tema: la familia y la memoria. Tema central: recordar a quienes ya murieron mantiene viva a la familia, y los sueños propios no deben costar el amor de los nuestros.</p></details>"),
             ("Un artículo real.", "Busque un artículo corto en un periódico en español (en papel o en línea). Anote la idea principal de cada párrafo y escriba un resumen de tres oraciones.")]
    quiz = [
        ("¿Cuál es la diferencia entre <strong>tema</strong> y <strong>tema central</strong>?", ["El tema dice de qué trata; el tema central, lo que se dice de ello", "El tema es largo y el tema central es corto", "El tema está al principio y el tema central al final"], 0, {1: "Es al revés: el tema es corto.", 2: "No depende del lugar."}, "El tema central es <strong>lo que se dice</strong> sobre el tema."),
        ("¿Cómo se expresa el tema central?", ["En una oración completa", "En una o dos palabras", "Con una pregunta"], 0, {1: "Así se dice el tema.", 2: "No."}, "En una <strong>oración completa</strong>."),
        ("¿Cuál es el error más común al buscar el tema central?", ["Elegir un detalle llamativo de un solo párrafo", "Leer el título antes de empezar el texto", "Anotar la idea principal de cada párrafo"], 0, {1: "Eso ayuda.", 2: "Eso ayuda."}, "Elegir un <strong>detalle</strong>."),
        ("¿Qué partes del texto conviene leer con más atención para encontrar el tema central?", ["El título, el primer párrafo y el último", "Solo las oraciones que tienen números", "Las palabras en negrita del medio"], 0, {1: "Los números suelen ser detalles.", 2: "No."}, "<strong>Título, primer y último párrafo.</strong>"),
        ("¿Con qué empieza un buen resumen objetivo?", ["Con el tema central", "Con el dato más curioso", "Con su opinión sobre el texto"], 0, {1: "Es un detalle.", 2: "Un resumen objetivo no opina."}, "Con el <strong>tema central</strong>."),
        ("¿Qué oración <strong>no</strong> debe ir en un resumen objetivo?", ["Es increíble lo que lograron los ingenieros.", "El texto explica cómo se limpia el agua.", "Después, la ciudad invirtió el curso del río."], 0, {1: "Es objetiva.", 2: "Es objetiva."}, "<em>Increíble</em> es una opinión."),
        ("¿Qué preguntas responde un resumen objetivo?", ["Quién, qué y cómo", "Qué me gustó y qué no", "Cuántas palabras tiene el texto"], 0, {1: "Eso es opinión.", 2: "No."}, "<strong>Quién, qué y cómo.</strong>"),
        ("¿Cuál de estas reglas es correcta para un resumen?", ["Seguir el orden del texto", "Copiar las oraciones más largas", "Incluir todas las cifras"], 0, {1: "Hay que usar sus palabras.", 2: "Solo lo esencial."}, "<strong>Seguir el orden.</strong>"),
        ("Un resumen tiene casi el mismo largo que el texto original. ¿Qué pasa?", ["No resume: es casi una copia", "Es el mejor resumen posible", "Tiene demasiadas opiniones"], 0, {1: "Un resumen es corto.", 2: "El largo no dice eso."}, "Es casi una <strong>copia</strong>."),
        ("Las ideas principales de cada párrafo y el tema central se relacionan así:", ["Las ideas principales sostienen el tema central", "El tema central es un detalle de cada idea", "No tienen ninguna relación entre sí"], 0, {1: "Es al revés.", 2: "Sí la tienen."}, "Como las <strong>patas</strong> y la tabla de una mesa."),
    ]
    filas = [
        ("Tema y tema central", "Distingo el tema, el tema central y las ideas principales.", "A veces elijo un detalle.", "Los confundo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Encontrar el tema central", "Sigo los cinco pasos y compruebo que valga para todo el texto.", "Me salto la comprobación.", "No sé por dónde empezar (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Resumen objetivo", "Resumo en tres a cinco oraciones, en orden y sin opinar.", "Se me escapa alguna opinión.", "Copio o hago listas (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya encuentra el tema central y resume sin opinar. En la próxima lección aprenderá a <strong>citar detalles</strong> y a distinguir lo que el texto dice de lo que se infiere.</p>"
    glosario = [("Tema", "El asunto de un texto, dicho en pocas palabras."), ("Tema central", "Lo que el autor dice sobre el tema en todo el texto, en una oración."),
                ("Idea principal", "Lo más importante de un párrafo o una sección."), ("Resumen objetivo", "Lo esencial de un texto, en sus palabras, en orden y sin opinar.")]
    conexion = ("<p>En la Lección 4.1 del Nivel 2 encontró la idea principal de varios párrafos. Hoy la convierte en el tema central de un texto largo y aprende a resumirlo.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno para anotar la idea de cada párrafo.</p>")
    estd = LE.estandares(["R.2.1", "R.2.2"], base=["R.2.3", "W.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Lo que el texto dice en todo y en cada parte.", ["Comprensión", "Idea central y resumen"],
                            ["<strong>Distinguir</strong> el tema, el tema central y las ideas principales.", "<strong>Encontrar</strong> el tema central de un texto largo en cinco pasos.",
                             "<strong>Escribir</strong> un resumen objetivo, sin opiniones."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-2", LE.titulo("3-2")), glosario, P)


def practica():
    tc = [{"enun": texto(ps) + "<p><strong>¿Cuál es el tema central?</strong></p>", "ops": o, "ok": 0, "pista": "¿Esa idea vale para los tres párrafos o solo para uno? ¿Contradice algo del texto?", "exp": n}
          for ps, o, n, _, _ in TEXTOS]
    ob = [{"enun": f'<p class="frase">{t}</p><p>En un resumen, esta oración es…</p>', "ops": OBT, "ok": k, "enOrden": True,
           "pista": "Busque palabras que juzguen o que digan lo que alguien «debería» hacer.", "exp": f"<strong>{OBT[k]}.</strong> {e}"} for t, k, e in OB]
    rs = [{"enun": texto(ps) + "<p><strong>¿Cuál es el mejor resumen?</strong></p>", "ops": r, "ok": 0, "pista": "¿Ese resumen dice el tema central? ¿Opina? ¿Se queda en un solo detalle?", "exp": nr}
          for ps, _, _, r, nr in TEXTOS if r]
    mods = [("tema-central", "El tema central", C.om("m1", "Lea el texto breve y elija su tema central.")),
            ("objetiva", "¿Objetiva o con opinión?", C.om("m2", "Decida si cada oración de un resumen es objetiva o mete la opinión de quien lo escribe.")),
            ("resumen", "El mejor resumen", C.om("m3", "Lea el texto breve y elija el resumen objetivo y completo."))]
    js = C.js_datos("TC", tc) + C.js_datos("OB", ob) + C.js_datos("RS", rs) + 'creaBanco("m1", TC);\ncreaBanco("m2", OB);\ncreaBanco("m3", RS);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
