# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 1.2 · Tiempos compuestos y la forma progresiva.
Fuente: clases_leng3/clase_1-2.html (GEDparaHispanos) y gramatica/n3-l1-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_1_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_1_1 import hueco

LE.nivel(3)
N = "1-2"


def V(t):  # tiempo compuesto
    return f'<b class="cl-w">{t}</b>'


def G(t):  # forma progresiva
    return f'<b class="cl-p">{t}</b>'


HISTORIA = [
    f"Rosa se despertó a las seis. La noche anterior {V('había planchado')} su mejor blusa y {V('había repasado')} las preguntas más comunes de una entrevista. Cuando llegó a la oficina, otros tres candidatos ya {G('estaban esperando')}. Mientras esperaba su turno, {G('estaba pensando')} en todo lo que {V('había aprendido')} en sus clases.",
    f"—¿{V('Ha trabajado')} antes en un almacén? —le preguntó la gerente.",
    f"—Sí. {V('He trabajado')} cinco años en almacenes. En el último, {G('estuve manejando')} el montacargas casi todo el tiempo.",
    "—¿Y qué hace ahora?",
    f"—{G('Estoy estudiando')} para el GED. Para junio {V('habré terminado')} los cuatro exámenes.",
    f"La gerente sonrió y le dio las gracias. Dos días después, Rosa {G('estaba cocinando')} cuando sonó el teléfono: le {V('habían dado')} el trabajo.",
]
CO = [("Este mes ___ tres veces al médico.", ["he ido", "había ido", "habré ido"], "<em>Este mes</em> todavía no termina: pretérito perfecto."),
      ("Cuando llegó la ambulancia, el herido ya ___.", ["se había despertado", "se ha despertado", "se habrá despertado"], "Antes de otra acción pasada: pluscuamperfecto."),
      ("Para el viernes, ya ___ todo el inventario.", ["habremos contado", "habíamos contado", "hemos contado"], "Terminado antes de un momento futuro: futuro perfecto."),
      ("¿Quién ha ___ la ventana?", ["roto", "rompido", "rota"], "Participio irregular de <em>romper</em>: <em>roto</em>."),
      ("Todavía no he ___ esa película.", ["visto", "vido", "veído"], "Participio irregular de <em>ver</em>: <em>visto</em>."),
      ("Mis padres han ___ a su país.", ["vuelto", "volvido", "vueltos"], "Participio irregular, y el participio no cambia: <em>vuelto</em>."),
      ("¿Dónde ha ___ las llaves?", ["puesto", "ponido", "ponida"], "Participio irregular de <em>poner</em>: <em>puesto</em>."),
      ("Ya se lo he ___ muchas veces.", ["dicho", "decido", "dicido"], "Participio irregular de <em>decir</em>: <em>dicho</em>."),
      ("___ dos accidentes en la autopista esta mañana.", ["Hubo", "Hubieron", "Hubimos"], "<em>Haber</em> con el sentido de «existir» va siempre en singular."),
      ("En la reunión ___ más de cincuenta padres.", ["había", "habían", "habíamos"], "<em>Haber</em> con el sentido de «existir» va siempre en singular."),
      ("Mi hija ___ terminado la tarea.", ["ha", "a", "ah"], "<em>Ha</em> es el verbo <em>haber</em>; <em>a</em> es la preposición."),
      ("Ojalá que ___ suficiente comida para todos.", ["haya", "haiga", "halla"], "<em>Haya</em>, del verbo <em>haber</em>. (<em>Halla</em> es de <em>hallar</em>, encontrar)."),
      ("Cuando me mudé a Chicago, nunca ___ la nieve.", ["había visto", "he visto", "habré visto"], "Algo que no había ocurrido antes de la mudanza: pluscuamperfecto."),
      ("Ya ___ las ventanas, así que el aire está fresco.", ["hemos abierto", "hemos abrido", "habemos abierto"], "Participio irregular <em>abierto</em>, y la forma es <em>hemos</em>.")]
PR = [("En este momento los niños están ___ un cuento.", ["leyendo", "leendo", "leído"], "Gerundio de <em>leer</em>: <em>leyendo</em>."),
      ("Shh, el bebé está ___.", ["durmiendo", "dormiendo", "dormido"], "Gerundio de <em>dormir</em>: <em>durmiendo</em>."),
      ("El cliente estaba ___ un descuento.", ["pidiendo", "pediendo", "pedido"], "Gerundio de <em>pedir</em>: <em>pidiendo</em>."),
      ("¿Me está ___?", ["oyendo", "oíendo", "oiendo"], "Gerundio de <em>oír</em>: <em>oyendo</em>."),
      ("Ya vamos ___ para su casa.", ["yendo", "iendo", "ido"], "Gerundio de <em>ir</em>: <em>yendo</em>."),
      ("Mi vecino siempre está ___ la verdad.", ["diciendo", "deciendo", "dicho"], "Gerundio de <em>decir</em>: <em>diciendo</em>."),
      ("Cuando sonó el teléfono, yo ___.", ["estaba cocinando", "estoy cocinando", "he cocinando"], "Acción en marcha en el pasado, interrumpida por otra."),
      ("A esta hora mañana ___ hacia Texas.", ["estaré manejando", "estaba manejando", "estoy manejado"], "Acción en marcha en un momento futuro."),
      ("Ahora mismo ___ para el examen de Ciencias.", ["estoy estudiando", "estaba estudiando", "he estudiando"], "Acción en marcha ahora."),
      ("Los obreros ___ la calle toda la semana pasada.", ["estuvieron arreglando", "están arreglando", "estarán arreglando"], "Una acción en marcha durante un tiempo del pasado ya cerrado."),
      ("Mientras usted ___ los platos, yo barro la cocina.", ["lava", "lavó", "lavará"], "Dos acciones a la vez en presente: con <em>mientras</em> basta el presente simple."),
      ("Los vecinos están ___ más muebles.", ["trayendo", "traiendo", "traído"], "Gerundio de <em>traer</em>: <em>trayendo</em>.")]
LI = [("Cuando llegué a la fiesta, mis amigos ya se habían ido.", ["Mis amigos se fueron.", "Yo llegué a la fiesta."], "<em>Se habían ido</em>: pluscuamperfecto, pasó antes."),
      ("Cuando la policía llegó, el ladrón ya había escapado.", ["El ladrón escapó.", "La policía llegó."], "<em>Había escapado</em> ocurrió antes de que llegara la policía."),
      ("Juan estaba duchándose cuando se fue la luz.", ["Juan empezó a ducharse.", "Se fue la luz."], "La ducha estaba en marcha cuando la luz se fue."),
      ("Encontré el anillo que había perdido en mayo.", ["Perdí el anillo.", "Encontré el anillo."], "<em>Había perdido</em>: antes de encontrarlo."),
      ("Para cuando usted despierte, yo ya habré salido.", ["Yo saldré.", "Usted despertará."], "El futuro perfecto <em>habré salido</em> estará terminado antes de que usted despierte."),
      ("Me dijeron que el examen ya había empezado.", ["El examen empezó.", "Me lo dijeron."], "Cuando se lo dijeron, el examen ya había empezado."),
      ("Estábamos cenando cuando tocaron a la puerta.", ["Empezamos a cenar.", "Tocaron a la puerta."], "La cena estaba en marcha cuando tocaron."),
      ("Cuando terminó la reunión, ya habíamos tomado una decisión.", ["Tomamos la decisión.", "Terminó la reunión."], "<em>Habíamos tomado</em>: la decisión fue antes del final."),
      ("Para las cinco, el camión ya habrá llegado.", ["El camión llegará.", "Serán las cinco."], "<em>Habrá llegado</em>: terminado antes de las cinco."),
      ("Mi abuela nos contó que había nacido en un pueblo pequeño.", ["Mi abuela nació.", "Mi abuela nos lo contó."], "<em>Había nacido</em>: mucho antes de contarlo.")]
GE = [(["Le enviaremos la factura la próxima semana.", "Le estaremos enviando la factura la próxima semana."], "Para el futuro basta el futuro simple."),
      (["Llamo para preguntar por mi pedido.", "Estoy llamando para preguntar por mi pedido."], "Lo que hace al hablar se dice en presente."),
      (["Mañana salgo para Guadalajara.", "Mañana estoy saliendo para Guadalajara."], "El progresivo no anuncia planes."),
      (["Recibí una caja que contenía herramientas.", "Recibí una caja conteniendo herramientas."], "El gerundio no describe a un sustantivo: se usa un relativo."),
      (["Se cayó de la escalera y se rompió la pierna.", "Se cayó de la escalera, rompiéndose la pierna."], "El gerundio no expresa algo que pasó después."),
      (["Le adjunto el formulario.", "Le estoy adjuntando el formulario."], "En un correo, lo que hace al escribir va en presente."),
      (["Necesitamos un empleado que hable inglés.", "Necesitamos un empleado hablando inglés."], "Para describir a la persona se usa un relativo."),
      (["El próximo año abrimos otra sucursal.", "El próximo año estamos abriendo otra sucursal."], "Planes futuros: presente o futuro, no progresivo."),
      (["Ahora estoy estudiando para el GED.", "Ahora estudiando para el GED."], "Aquí la forma progresiva sí va: una acción en marcha en esta etapa, con su verbo <em>estar</em>."),
      (["Ganó el premio y lo celebró con su familia.", "Ganó el premio, celebrándolo con su familia."], "La celebración fue después del premio: dos verbos unidos por <em>y</em>.")]


def linea(frase, pasos):
    li = "".join(f'<li><span class="lt-n">{n}</span>{t}</li>' for n, t in pasos)
    return f'<div class="linea-t"><p class="lt-frase">«{frase}»</p><ol class="lt">{li}</ol></div>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Lea estas dos oraciones:</p>
<ul><li>«Cuando llegué a la parada, el autobús <strong>salió</strong>.»</li><li>«Cuando llegué a la parada, el autobús ya <strong>había salido</strong>.»</li></ul>
<p>En la primera, usted llegó justo a tiempo de verlo irse. En la segunda, cuando llegó ya no había autobús. Un solo verbo cambia toda la historia. Esta lección le enseña a usar los tiempos que ordenan las acciones, una destreza que el GED pone a prueba en las preguntas de corrección.</p>
<p>Los <strong>tiempos simples</strong> se forman con una sola palabra. Ya los conoce:</p>
{C.tabla("Tiempos simples del verbo trabajar", ["Tiempo", "Ejemplo", "Se usa para…"],
         [["Presente", "Yo <strong>trabajo</strong> en un almacén.", "Lo que pasa ahora o de costumbre."], ["Pretérito", "Ayer <strong>trabajé</strong> diez horas.", "Una acción terminada en el pasado."],
          ["Imperfecto", "De joven <strong>trabajaba</strong> en el campo.", "Una costumbre o una descripción en el pasado."], ["Futuro", "Mañana <strong>trabajaré</strong> temprano.", "Lo que pasará."]])}
<p>Los tiempos compuestos y la forma progresiva usan <strong>dos palabras</strong>: un verbo que ayuda (<em>haber</em> o <em>estar</em>) y el verbo principal. Esa segunda palabra añade un matiz: si la acción ya estaba terminada o si estaba en marcha.</p>"""

    s2 = f"""<p>Un <strong>tiempo compuesto</strong> se forma con el verbo <em>haber</em> conjugado y el <strong>participio</strong> del verbo principal. El participio termina en <em>-ado</em> (trabajado) o en <em>-ido</em> (comido, vivido) y nunca cambia.</p>
{C.tabla("Los tres tiempos compuestos más usados", ["Tiempo", "Haber", "Se usa para…", "Ejemplo"],
         [["Pretérito perfecto", "he, has, ha, hemos, han", "Algo que pasó dentro de un tiempo que todavía sigue (hoy, este año, en mi vida).", "Este año <strong>he ahorrado</strong> mil dólares."],
          ["Pluscuamperfecto", "había, habías, había, habíamos, habían", "Algo que pasó antes de otra acción pasada.", "Cuando llegué, el autobús ya <strong>había salido</strong>."],
          ["Futuro perfecto", "habré, habrás, habrá, habremos, habrán", "Algo que estará terminado antes de un momento futuro.", "Para diciembre <strong>habré terminado</strong> el curso."]])}
<h3>Participios irregulares que conviene conocer</h3>
<p>hacer → <strong>hecho</strong> · decir → <strong>dicho</strong> · escribir → <strong>escrito</strong> · ver → <strong>visto</strong> · poner → <strong>puesto</strong> · volver → <strong>vuelto</strong> · abrir → <strong>abierto</strong> · romper → <strong>roto</strong> · morir → <strong>muerto</strong> · resolver → <strong>resuelto</strong> · cubrir → <strong>cubierto</strong></p>
{C.caja("tip", "¿«Comí» o «he comido»?", "<p>En casi toda América Latina se usa más el pretérito («Hoy comí poco»), y es correcto. El pretérito perfecto («Hoy he comido poco») subraya que el tiempo del que se habla no ha terminado. Las dos formas son válidas; lo importante es reconocer el pretérito perfecto cuando lo lea y formarlo bien cuando lo use.</p>")}
{C.caja("ojo", "«Habían muchas personas»", "<p>Cuando <em>haber</em> significa «existir», va siempre en singular: «<strong>Había</strong> muchas personas», «<strong>Hubo</strong> tres accidentes», «Va a <strong>haber</strong> problemas». Lo mismo con «Habíamos diez en la reunión»: se escribe «<strong>Éramos</strong> diez en la reunión». Este error aparece mucho en el GED.</p>")}
{C.caja("ojo", "Ha, a y haya", "<p><strong>Ha</strong> (con h) es el verbo <em>haber</em> y va antes de un participio: «Mi hija <strong>ha</strong> llegado». <strong>A</strong> es la preposición: «Voy <strong>a</strong> la tienda». Y la forma correcta es <strong>haya</strong>, nunca «haiga»: «Espero que <strong>haya</strong> llegado bien».</p>")}
{P("Compuesto 1", hueco("Este año yo ___ mucho dinero."), ["había ahorrado", "he ahorrado", "habré ahorrado"], 1, {0: "No hay otra acción pasada después.", 2: "No habla de un momento futuro."}, "<em>Este año</em> todavía no termina: pretérito perfecto.")}
{P("Compuesto 2", hueco("Cuando llegamos al cine, la película ya ___."), ["ha empezado", "habrá empezado", "había empezado"], 2, {0: "La llegada es pasada: hace falta un tiempo anterior a ella.", 1: "No habla del futuro."}, "Antes de otra acción pasada: pluscuamperfecto.")}
{P("Compuesto 3", hueco("Mi hermano ha ___ una carta al alcalde."), ["escrito", "escribido", "escrita"], 0, {1: "Es un participio irregular.", 2: "El participio de un tiempo compuesto no cambia."}, "Participio irregular: <em>escrito</em>.")}
{P("Compuesto 4", hueco("___ muchas personas en la fiesta."), ["Habían", "Había", "Habíamos"], 1, {0: "<em>Haber</em> como «existir» va en singular.", 2: "<em>Haber</em> como «existir» va en singular."}, "<em>Haber</em> con el sentido de «existir» va en singular.")}"""

    s3 = f"""<p>La <strong>forma progresiva</strong> muestra una acción <strong>en marcha</strong>, que todavía no ha terminado en el momento del que se habla. Se forma con <em>estar</em> conjugado y el <strong>gerundio</strong>, que termina en <em>-ando</em> (trabajando) o en <em>-iendo</em> (comiendo, viviendo).</p>
{C.tabla("La forma progresiva en presente, pasado y futuro", ["Forma", "Ejemplo", "Qué muestra"],
         [["Presente progresivo", "<strong>Estoy estudiando</strong> para el GED.", "Algo en marcha ahora mismo o en esta etapa de su vida."],
          ["Pasado progresivo", "<strong>Estaba cocinando</strong> cuando sonó el teléfono.", "Algo en marcha cuando otra acción lo interrumpió."],
          ["Futuro progresivo", "A esta hora mañana <strong>estaré manejando</strong> a Texas.", "Algo que estará en marcha en un momento futuro."]])}
<h3>Gerundios que cambian</h3>
<p>leer → <strong>leyendo</strong> · oír → <strong>oyendo</strong> · traer → <strong>trayendo</strong> · ir → <strong>yendo</strong> · dormir → <strong>durmiendo</strong> · pedir → <strong>pidiendo</strong> · decir → <strong>diciendo</strong> · venir → <strong>viniendo</strong></p>
{C.caja("tip", "La acción interrumpida y la que interrumpe", "<p>En el pasado, la acción larga va en progresivo (o en imperfecto) y la acción corta que la corta va en pretérito: «<strong>Estaba durmiendo</strong> cuando <strong>sonó</strong> la alarma». La alarma interrumpió el sueño.</p>")}
{P("Progresiva 1", hueco("Los niños están ___ un cuento."), ["leendo", "leído", "leyendo"], 2, {0: "Entre dos vocales, la <em>i</em> se vuelve <em>y</em>.", 1: "Ese es el participio."}, "Gerundio de <em>leer</em>: <em>leyendo</em>.")}
{P("Progresiva 2", hueco("Ayer a esta hora yo ___ en el taller."), ["estoy trabajando", "estaba trabajando", "he trabajando"], 1, {0: "Habla de ayer.", 2: "<em>Haber</em> va con participio, no con gerundio."}, "Una acción en marcha en un momento del pasado.")}"""

    s4 = f"""<p>Imagine el tiempo como una línea. Los tiempos compuestos le dicen qué acción ocurrió <strong>antes</strong>; la forma progresiva, qué acción estaba <strong>en marcha</strong>. Lea cada línea en orden, del primer punto al último:</p>
<div class="lineas-t">{linea("Cuando llegué a la parada, el autobús ya había salido.", [("1.º", "El autobús había salido."), ("2.º", "Yo llegué a la parada."), ("Ahora", "Lo cuento.")])}
{linea("Estaba cocinando cuando sonó el teléfono.", [("1.º", "Empecé a cocinar: estaba cocinando…"), ("2.º", "…y en medio sonó el teléfono."), ("Ahora", "Lo cuento.")])}
{linea("Para diciembre habré terminado el curso.", [("Ahora", "Estoy en el curso."), ("1.º", "El curso habrá terminado…"), ("2.º", "…antes de que llegue diciembre.")])}</div>
{C.caja("tip", "La pista de «ya»", "<p>La palabra <strong>ya</strong> suele acompañar al pluscuamperfecto y al futuro perfecto: «ya había salido», «ya habré terminado». Es una pista de que una acción terminó antes que otra.</p>")}
{P("Primero 1", "«Cuando la policía llegó, el ladrón ya había escapado.» ¿Qué pasó primero?", ["La policía llegó.", "El ladrón escapó."], 1, {0: "<em>Había escapado</em> es anterior."}, "<em>Había escapado</em> ocurrió antes de que llegara la policía.")}
{P("Primero 2", "«Estábamos cenando cuando tocaron a la puerta.» ¿Qué empezó primero?", ["Empezamos a cenar.", "Tocaron a la puerta."], 0, {1: "La cena ya estaba en marcha."}, "La cena estaba en marcha cuando tocaron.")}"""

    s5 = f"""<p>En inglés la forma <em>-ing</em> se usa muchísimo, y a veces se pasa al español donde no corresponde. En la escritura formal, y en el GED, estas son las formas correctas:</p>
{C.tabla("Usos del gerundio que vienen del inglés y su forma correcta", ["Se oye…", "En buen español", "Por qué"],
         [["Le estaremos enviando la factura.", "Le <strong>enviaremos</strong> la factura.", "Para el futuro basta el futuro simple."],
          ["Estoy llamando para preguntar por mi pedido.", "<strong>Llamo</strong> para preguntar por mi pedido.", "Una acción que ocurre al hablar se dice en presente."],
          ["Mañana estoy saliendo de viaje.", "Mañana <strong>salgo</strong> de viaje.", "En español el progresivo no anuncia planes futuros."],
          ["Una caja conteniendo libros.", "Una caja <strong>que contiene</strong> libros.", "El gerundio no describe a un sustantivo; se usa un relativo."],
          ["Chocó contra un poste, rompiéndose el brazo.", "Chocó contra un poste <strong>y se rompió</strong> el brazo.", "El gerundio no expresa algo que pasó después."]])}
{C.caja("tip", "La prueba", "<p>Si el gerundio se puede cambiar por un tiempo simple sin perder nada, use el tiempo simple. «Estoy estudiando para el GED» sí pasa la prueba, porque la acción está en marcha en esta etapa; «le estaremos enviando» no la pasa.</p>")}
{P("Gerundio 1", "¿Cuál está en buen español?", ["Recibí una caja conteniendo herramientas.", "Recibí una caja que contenía herramientas."], 1, {0: "El gerundio no describe a un sustantivo."}, "Se usa un relativo: <em>que contenía</em>.")}
{P("Gerundio 2", "¿Cuál está en buen español?", ["Mañana salgo para Guadalajara.", "Mañana estoy saliendo para Guadalajara."], 0, {1: "El progresivo no anuncia planes."}, "Para un plan, presente o futuro: <em>salgo</em>.")}"""

    hist = "".join(f"<p>{p}</p>" for p in HISTORIA)
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in HISTORIA)
    s6 = f"""<p>Lea la historia. Después pulse <strong>Mostrar los verbos</strong>: verá en morado los tiempos compuestos y en verde las formas progresivas. En su cuaderno, dibuje una línea de tiempo y coloque en orden cinco acciones de la historia.</p>
<p>{LE.escuchar(plano, "Escuchar la historia")} <button type="button" class="btn-sec" id="btn-v12" aria-pressed="false">Mostrar los verbos</button></p>
<div class="articulo lectura-cl" id="lect-12"><p><strong>La entrevista de Rosa</strong></p>{hist}</div>
<p class="leyenda-partes" id="ley-12"><span style="background:#ede9fe">Tiempo compuesto</span><span style="background:#dcfce7">Forma progresiva</span></p>
<p class="fuente">Rosa es un personaje creado para esta lección.</p>
<script>(function(){{var b=document.getElementById("btn-v12"),t=document.getElementById("lect-12"),l=document.getElementById("ley-12");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar los verbos":"Mostrar los verbos";}});}})();</script>
<h3>¿Cuándo pasó cada cosa?</h3>
{P("Rosa 1", "«La noche anterior había planchado su blusa.» ¿Qué pasó primero?", ["Despertarse a las seis", "Planchar la blusa", "Llegar a la oficina"], 1, {0: "<em>Había planchado</em> es anterior a despertarse.", 2: "Llegar a la oficina fue después."}, "El pluscuamperfecto <em>había planchado</em> indica que fue antes de despertarse.")}
{P("Rosa 2", "Cuando Rosa llegó, los otros candidatos «ya estaban esperando». Eso significa que…", ["empezaron a esperar después que ella", "se fueron en cuanto ella llegó", "esperaban desde antes de que ella llegara"], 2, {0: "<em>Ya</em> indica que la espera había empezado.", 1: "Seguían esperando."}, "La forma progresiva muestra una acción en marcha cuando ella llegó.")}
{P("Rosa 3", "«He trabajado cinco años en almacenes»: ¿de qué habla Rosa?", ["De su experiencia hasta hoy", "De un trabajo que hará pronto", "De algo que hizo una sola vez"], 0, {1: "No es futuro.", 2: "Fueron cinco años."}, "El pretérito perfecto conecta el pasado con el presente: es la experiencia que tiene hoy.")}
{P("Rosa 4", "«Para junio habré terminado los cuatro exámenes» significa que…", ["en junio empezará los cuatro exámenes", "en junio los exámenes ya estarán terminados", "terminó los exámenes el junio pasado"], 1, {0: "<em>Habré terminado</em>: terminado antes de junio.", 2: "Es futuro."}, "El futuro perfecto: algo terminado antes de un momento futuro.")}
{P("Rosa 5", "«Le habían dado el trabajo.» ¿Cuándo le dieron el trabajo?", ["Durante la entrevista", "Después de la llamada", "Antes de la llamada"], 2, {0: "La gerente solo le dio las gracias.", 1: "<em>Habían dado</em> es anterior a la llamada."}, "<em>Habían dado</em>: la decisión ya estaba tomada cuando la llamaron.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Túrnense para decir una oración con <em>cuando</em> y dos acciones del día («Cuando llegué a casa, mi hijo ya había comido»). El otro dice cuál pasó primero.</p>")}"""

    secciones = [("s1", "Repaso: los tiempos simples", s1), ("s2", "Los tiempos compuestos: haber + participio", s2), ("s3", "La forma progresiva: estar + gerundio", s3),
                 ("s4", "La línea del tiempo: ¿qué pasó primero?", s4), ("s5", "Cuidado con el gerundio que viene del inglés", s5), ("s6", "Lectura: «La entrevista de Rosa»", s6)]
    tarea = [("Mi historia en dos tiempos.", "Escriba un párrafo de cinco o seis oraciones sobre un día importante de su vida (su llegada a este país, su primer trabajo, el nacimiento de un hijo). Use al menos un pluscuamperfecto (<em>había…</em>) y un pasado progresivo (<em>estaba…</em>)."),
             ("Mis metas.", "Escriba tres oraciones con el futuro perfecto sobre lo que habrá logrado en un año: «Para octubre del año que viene, habré…»."),
             ("Corrija.", "Reescriba bien: «Habían muchos niños en el parque» · «Le estaremos llamando la próxima semana» · «Mi hijo ha rompido la ventana» · «Espero que haiga suficiente comida». "
              "<details class=\"transc\"><summary>Ver las respuestas</summary><p>«Había muchos niños en el parque.» · «Le llamaremos la próxima semana.» · «Mi hijo ha roto la ventana.» · «Espero que haya suficiente comida.»</p></details>")]
    quiz = [
        ("¿Cómo se forma un tiempo compuesto?", ["haber + participio", "estar + gerundio", "ser + infinitivo"], 0, {1: "Esa es la forma progresiva.", 2: "No."}, "<strong>Haber + participio.</strong>"),
        ("¿Cuál es el participio de <em>escribir</em>?", ["escrito", "escribido", "escribiendo"], 0, {1: "Es irregular.", 2: "Ese es el gerundio."}, "<strong>Escrito.</strong>"),
        (hueco("Complete: «Cuando llegué a la parada, el autobús ya ___.»"), ["había salido", "ha salido", "habrá salido"], 0, {1: "La llegada es pasada.", 2: "No es futuro."}, "<strong>Había salido.</strong>"),
        (hueco("Complete: «Para el año próximo, ya ___ el GED.»"), ["habré aprobado", "había aprobado", "he aprobado"], 0, {1: "Es futuro.", 2: "Es futuro."}, "<strong>Habré aprobado.</strong>"),
        ("¿Cuál oración está bien escrita?", ["Había mucha gente en la tienda.", "Habían mucha gente en la tienda.", "Habíamos mucha gente en la tienda."], 0, {1: "<em>Haber</em> como «existir» va en singular.", 2: "<em>Haber</em> como «existir» va en singular."}, "<strong>Había.</strong>"),
        ("¿Cuál oración usa la forma progresiva?", ["Estoy leyendo un libro muy bueno.", "He leído un libro muy bueno.", "Leí ayer un libro muy bueno."], 0, {1: "Es un tiempo compuesto.", 2: "Es un tiempo simple."}, "<strong>Estoy leyendo.</strong>"),
        ("¿Cuál es el gerundio de <em>leer</em>?", ["leyendo", "leendo", "leído"], 0, {1: "La <em>i</em> se vuelve <em>y</em>.", 2: "Es el participio."}, "<strong>Leyendo.</strong>"),
        ("«Estaba durmiendo cuando sonó la alarma.» ¿Qué acción interrumpe a la otra?", ["Sonó la alarma", "Estaba durmiendo", "Ninguna, son a la vez"], 0, {1: "Esa es la que estaba en marcha.", 2: "Una corta a la otra."}, "<strong>Sonó la alarma.</strong>"),
        ("¿Cuál es la forma más natural en español?", ["Le enviaremos la factura mañana.", "Le estaremos enviando la factura mañana.", "Le vamos a estar enviando la factura."], 0, {1: "Viene del inglés.", 2: "Viene del inglés."}, "<strong>Le enviaremos.</strong>"),
        ("¿Cuál dice bien que el viaje es mañana?", ["Mañana salgo de viaje.", "Mañana estoy saliendo de viaje.", "Mañana estaré saliendo de viaje."], 0, {1: "El progresivo no anuncia planes.", 2: "El progresivo no anuncia planes."}, "<strong>Mañana salgo.</strong>"),
        ("¿Qué indica «Hoy he comido poco»?", ["Algo pasó en un día que aún sigue", "Algo que va a pasar más tarde hoy", "Una costumbre de un tiempo pasado"], 0, {1: "Ya pasó.", 2: "No es una costumbre."}, "Un tiempo que <strong>todavía sigue</strong>."),
        ("¿Cuál oración está bien escrita?", ["Espero que haya llegado bien.", "Espero que haiga llegado bien.", "Espero que a llegado bien."], 0, {1: "«Haiga» no es correcto.", 2: "<em>A</em> es la preposición."}, "<strong>Haya.</strong>"),
    ]
    filas = [
        ("Tiempos compuestos", "Uso he, había y habré + participio, y conozco los irregulares.", "Dudo con los participios irregulares.", "Los confundo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Forma progresiva", "Uso estar + gerundio para acciones en marcha, sin el gerundio del inglés.", "A veces uso el progresivo para planes.", "No la distingo (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Orden de las acciones", "Sé qué pasó primero por el tiempo del verbo.", "A veces lo dudo.", "Me pierdo (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya ordena las acciones con los tiempos compuestos y la forma progresiva. En la próxima lección aprenderá a corregir <strong>fragmentos</strong> y <strong>oraciones corridas</strong>.</p>"
    glosario = [("Participio", "Forma del verbo en -ado o -ido (trabajado, comido) que va con haber."), ("Gerundio", "Forma del verbo en -ando o -iendo (trabajando, comiendo) que va con estar."),
                ("Tiempo compuesto", "Haber + participio: he comido, había comido, habré comido."), ("Pluscuamperfecto", "Había + participio: algo anterior a otra acción pasada."),
                ("Forma progresiva", "Estar + gerundio: una acción en marcha.")]
    conexion = ("<p>En la Lección 1.1 unió ideas con relativos y conjunciones. Hoy aprenderá a ordenar en el tiempo las acciones de esas ideas.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno para dibujar líneas de tiempo.</p>")
    estd = LE.estandares(["L.1.4", "L.1.1"], base=["L.1.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Ordenar las acciones con haber y estar.", ["Gramática", "Tiempos verbales"],
                            ["<strong>Formar</strong> el pretérito perfecto, el pluscuamperfecto y el futuro perfecto.", "<strong>Usar</strong> la forma progresiva para acciones en marcha.",
                             "<strong>Decidir</strong> qué acción pasó primero por el tiempo del verbo.", "<strong>Evitar</strong> «habían muchas personas» y el gerundio que viene del inglés."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-3", LE.titulo("1-3")), glosario, P)


def practica():
    def comp(datos, pista):
        return [{"enun": f'<p class="frase">{hueco(t)}</p>', "ops": o, "ok": 0, "pista": pista,
                 "exp": "«" + (lambda x: x[0].upper() + x[1:])(t.replace("___", o[0])) + f"» · {e}"} for t, o, e in datos]
    co = comp(CO, "¿El participio es irregular? ¿La acción pasó antes de otra? ¿<em>Haber</em> significa «existir»?")
    pr = comp(PR, "Revise el gerundio: algunos cambian la vocal o llevan <em>y</em>. ¿La acción estaba en marcha ahora, antes o después?")
    li = [{"enun": f'<p class="frase">{t}</p><p>¿Qué pasó (o empezó) primero?</p>', "ops": o, "ok": 0, "pista": "Busque el tiempo compuesto (<em>había…, habré…</em>) o la forma progresiva (<em>estaba…</em>).", "exp": e} for t, o, e in LI]
    ge = [{"enun": "<p>¿Cuál está en buen español?</p>", "ops": o, "ok": 0, "pista": "¿Ese gerundio se podría cambiar por un tiempo simple o por <em>que</em> + verbo sin perder nada?", "exp": f"«{o[0]}» · {e}"} for o, e in GE]
    mods = [("compuestos", "Tiempos compuestos", C.om("m1", "Complete con el tiempo compuesto o el participio correcto.")),
            ("progresiva", "Forma progresiva", C.om("m2", "Complete con el gerundio o la forma progresiva correcta.")),
            ("primero", "¿Qué pasó primero?", C.om("m3", "Lea la oración y decida qué acción pasó o empezó primero.")),
            ("gerundio", "El gerundio en buen español", C.om("m4", "Elija la versión que usa bien el gerundio."))]
    js = C.js_datos("CO", co) + C.js_datos("PR", pr) + C.js_datos("LI", li) + C.js_datos("GE", ge) + 'creaBanco("m1", CO);\ncreaBanco("m2", PR);\ncreaBanco("m3", LI);\ncreaBanco("m4", GE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
