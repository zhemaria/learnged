# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 1.1 · Pronombres relativos y conjunciones subordinantes.
Fuente: clases_leng3/clase_1-1.html (GEDparaHispanos) y gramatica/n3-l1-1.html, adaptadas al marco de LearnGED.
Datos del incendio: U.S. Census Bureau, «History and the Census: 1871 Great Chicago Fire» (census.gov); consultado en noviembre de 2026.
Uso: python3 tools/build_leng3_1_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "1-1"


def R(t):  # relativo o conjunción
    return f'<b class="cl-w">{t}</b>'


def S(t):  # cláusula subordinada
    return f'<span class="cl-s">{t}</span>'


LECTURA = [
    f"La noche del 8 de octubre de 1871, un fuego {S(R('que') + ' comenzó en el granero de la familia O’Leary')}, en la calle DeKoven, empezó a extenderse por Chicago. {S(R('Como') + ' el verano había sido muy seco')}, la madera de las casas y de las aceras ardía con facilidad.",
    f"{S(R('Aunque') + ' los bomberos trabajaron sin descanso')}, el viento empujó las llamas hacia el norte y el este. El fuego cruzó el río Chicago, {S(R('cuyas') + ' orillas estaban llenas de almacenes y depósitos de madera')}, y llegó al centro, {S(R('donde') + ' estaban los bancos, los hoteles y los periódicos')}.",
    f"El incendio no se apagó {S(R('hasta que') + ' empezó a llover')}, el 10 de octubre. Murieron unas 300 personas, se destruyeron unos 17 500 edificios y unas 90 000 personas, {S(R('que') + ' eran casi la tercera parte de los habitantes')}, se quedaron sin hogar.",
    f"Durante años se culpó a una vaca {S(R('que') + ', según la leyenda, había pateado una lámpara')}. Nadie lo probó nunca, y en 1997 el Concejo Municipal declaró inocentes a Catherine O’Leary y a su vaca.",
    f"Uno de los pocos edificios {S(R('que') + ' sobrevivieron')} fue la Torre del Agua, {S(R('la cual') + ' todavía se puede visitar en la avenida Michigan')}. {S(R('Para que') + ' una tragedia así no se repitiera')}, la ciudad adoptó reglas más estrictas para construir.",
]

RE = [("El hombre ___ hijos juegan en el parque es mi vecino.", ["cuyos", "cuyo", "que sus"], "<em>Cuyos</em> concuerda con <em>hijos</em>, lo que se posee."),
      ("La ciudad ___ nací está en Michoacán.", ["donde", "cuya", "quien"], "Es un lugar: <em>donde</em>."),
      ("La enfermera ___ me atendió fue muy amable.", ["que", "cuya", "donde"], "Una persona, sin comas ni preposición: <em>que</em>."),
      ("Le presento a Luis, ___ trabaja conmigo en el almacén.", ["quien", "cuyo", "donde"], "Una persona, entre comas: <em>quien</em>."),
      ("Estas son las razones por ___ me mudé.", ["las cuales", "los cuales", "quienes"], "Tras una preposición, y concuerda con <em>razones</em>: <em>por las cuales</em>."),
      ("La empresa ___ dueño es mexicano abrió otra tienda.", ["cuyo", "cuya", "que su"], "<em>Cuyo</em> concuerda con <em>dueño</em>, no con <em>empresa</em>."),
      ("Los niños con ___ juega mi hijo viven en la esquina.", ["quienes", "cuyos", "donde"], "Personas en plural, tras una preposición: <em>con quienes</em>."),
      ("El parque ___ corremos los sábados está cerrado.", ["donde", "cuyo", "quien"], "Es un lugar: <em>donde</em>."),
      ("La computadora ___ compré ya no funciona.", ["que", "quien", "cuya"], "Una cosa: <em>que</em>. <em>Quien</em> es solo para personas."),
      ("El problema del ___ le hablé ya se resolvió.", ["cual", "quien", "cuyo"], "<em>Del cual</em>: tras la preposición; <em>quien</em> no sirve para cosas."),
      ("Conocí a una escritora ___ libros leí en la escuela.", ["cuyos", "cuyas", "que sus"], "<em>Cuyos</em> concuerda con <em>libros</em>."),
      ("Mis tíos, ___ viven en Texas, vienen en diciembre.", ["quienes", "quien", "cuyos"], "Personas en plural, entre comas: <em>quienes</em>."),
      ("La caja ___ llegó ayer está dañada.", ["que", "quien", "cuya"], "Una cosa: <em>que</em>."),
      ("Es una casa ___ jardín está lleno de flores.", ["cuyo", "cuya", "que su"], "<em>Cuyo</em> concuerda con <em>jardín</em>.")]
CO = [("Los vecinos que tienen perro pagan una cuota extra.", ["Solo pagan los vecinos que tienen perro.", "Todos los vecinos tienen perro y pagan."], "Sin comas, la cláusula separa a los que tienen perro del resto."),
      ("Los vecinos, que tienen perro, pagan una cuota extra.", ["Todos los vecinos tienen perro y pagan.", "Solo pagan los vecinos que tienen perro."], "Entre comas, la cláusula añade un dato sobre todos los vecinos."),
      ("Mi hermana que vive en Houston es maestra.", ["Tengo más de una hermana; hablo de la de Houston.", "Tengo una sola hermana y añado dónde vive."], "Sin comas, la cláusula distingue a esa hermana de las demás."),
      ("Mi hermana, que vive en Houston, es maestra.", ["Tengo una sola hermana y añado dónde vive.", "Tengo más de una hermana; hablo de la de Houston."], "Entre comas, solo se añade un dato."),
      ("Los estudiantes que llegaron tarde no entraron al examen.", ["Algunos llegaron tarde, y solo esos no entraron.", "Todos llegaron tarde, así que nadie entró."], "Sin comas: solo el grupo que llegó tarde."),
      ("Los estudiantes, que llegaron tarde, no entraron al examen.", ["Todos llegaron tarde, así que nadie entró.", "Algunos llegaron tarde, y solo esos no entraron."], "Entre comas: el dato vale para todos."),
      ("Las manzanas que estaban podridas fueron a la basura.", ["Solo se tiraron las manzanas podridas.", "Se tiraron todas: todas estaban podridas."], "Sin comas, se separa a las podridas de las buenas."),
      ("Las manzanas, que estaban podridas, fueron a la basura.", ["Se tiraron todas: todas estaban podridas.", "Solo se tiraron las manzanas podridas."], "Entre comas, todas estaban podridas."),
      ("El río Chicago, que cruza el centro, se tiñe de verde cada marzo.", ["Hay un solo río Chicago; se añade un dato.", "Hay varios ríos Chicago; se habla de uno."], "Un nombre propio ya dice de cuál se trata: la cláusula va entre comas.")]
CJ = [("No pude dormir ___ el vecino hizo una fiesta.", ["porque", "aunque", "para que"], "Causa."),
      ("___ estaba muy cansada, terminó su turno.", ["Aunque", "Porque", "Para que"], "Obstáculo que no impidió la acción."),
      ("Hable más despacio ___ todos le entiendan.", ["para que", "porque", "aunque"], "Finalidad, con subjuntivo: <em>entiendan</em>."),
      ("___ termine la tarea, podrá descansar.", ["Cuando", "Aunque", "Ya que"], "Tiempo. Va en subjuntivo porque todavía no ha pasado."),
      ("No saldremos de viaje ___ el carro esté arreglado.", ["a menos que", "ya que", "porque"], "Condición: si el carro no está arreglado, no hay viaje."),
      ("Apague la estufa ___ se queme la comida.", ["antes de que", "porque", "ya que"], "Tiempo, con subjuntivo: <em>se queme</em>."),
      ("___ no tiene carro, lo llevo yo.", ["Como", "Aunque", "Para que"], "Causa al principio de la oración: <em>como</em>."),
      ("Escucho la radio ___ cocino.", ["mientras", "para que", "a menos que"], "Dos acciones al mismo tiempo."),
      ("Lleve el paraguas ___ llueva.", ["en caso de que", "ya que", "porque"], "Condición, con subjuntivo: <em>llueva</em>."),
      ("Me quedé en la oficina ___ terminé el informe.", ["hasta que", "para que", "a menos que"], "Tiempo, hasta un momento."),
      ("___ el examen fue difícil, casi todos aprobaron.", ["A pesar de que", "Ya que", "Para que"], "Obstáculo que no impidió aprobar."),
      ("Le presto el dinero ___ me lo devuelva el viernes.", ["siempre que", "ya que", "porque"], "Condición, con subjuntivo: <em>devuelva</em>."),
      ("Cerramos temprano ___ mañana es día feriado.", ["ya que", "aunque", "a menos que"], "Causa."),
      ("___ llegó el autobús, todos subieron corriendo.", ["En cuanto", "Para que", "A menos que"], "Tiempo: justo después de un momento.")]
UN = [("Tengo un amigo. Su esposa es dentista.", ["Tengo un amigo cuya esposa es dentista.", "Tengo un amigo que su esposa es dentista.", "Tengo un amigo cuyo esposa es dentista."], "<em>Cuya</em>, que concuerda con <em>esposa</em>."),
      ("Este es el restaurante. Allí celebramos mi cumpleaños.", ["Este es el restaurante donde celebramos mi cumpleaños.", "Este es el restaurante cuyo celebramos mi cumpleaños.", "Este es el restaurante quien celebramos mi cumpleaños."], "Un lugar: <em>donde</em>."),
      ("Ahorro cada mes. Así mi familia podrá viajar en verano.", ["Ahorro cada mes para que mi familia pueda viajar en verano.", "Ahorro cada mes para que mi familia puede viajar en verano.", "Ahorro cada mes aunque mi familia pueda viajar en verano."], "Finalidad: <em>para que</em> con subjuntivo."),
      ("El tráfico era terrible. Llegamos a tiempo.", ["A pesar de que el tráfico era terrible, llegamos a tiempo.", "Como el tráfico era terrible, llegamos a tiempo.", "A pesar de que el tráfico era terrible llegamos, a tiempo."], "Obstáculo, y la coma después de la cláusula que va primero."),
      ("Conocí a la doctora. La doctora operó a mi padre.", ["Conocí a la doctora que operó a mi padre.", "Conocí a la doctora cuya operó a mi padre.", "Conocí a la doctora donde operó a mi padre."], "Una persona: <em>que</em>."),
      ("Mi jefe me dio el día libre. Yo había trabajado el domingo.", ["Mi jefe me dio el día libre porque yo había trabajado el domingo.", "Mi jefe me dio el día libre para que yo había trabajado el domingo.", "Mi jefe me dio el día libre aunque yo había trabajado el domingo."], "Trabajar el domingo es la causa del día libre."),
      ("Va a firmar el documento. Primero léalo con calma.", ["Antes de que firme el documento, léalo con calma.", "Antes de que firma el documento, léalo con calma.", "Antes de que firme el documento léalo, con calma."], "<em>Antes de que</em> pide subjuntivo, y la coma va después de la cláusula."),
      ("Mis padres viven en Cicero. Vinieron de Jalisco.", ["Mis padres, quienes vinieron de Jalisco, viven en Cicero.", "Mis padres, cuyos vinieron de Jalisco, viven en Cicero.", "Mis padres quien vinieron de Jalisco viven en Cicero."], "Personas en plural, entre comas porque solo se añade un dato."),
      ("Puede salir temprano. Antes tiene que terminar el inventario.", ["Puede salir temprano siempre que termine el inventario.", "Puede salir temprano siempre que termina el inventario.", "Puede salir temprano ya que termine el inventario."], "Condición: <em>siempre que</em> con subjuntivo."),
      ("Pienso algo. El examen será fácil.", ["Pienso que el examen será fácil.", "Pienso de que el examen será fácil.", "Pienso que de el examen será fácil."], "Sin <em>de</em>: se dice «pienso eso», no «pienso de eso».")]


def hueco(t):
    return t.replace("___", "<span class=\"hueco\">_____</span>")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Compare estas dos versiones:</p>
<ul><li>«Tengo un vecino. El hijo de mi vecino arregla computadoras. Mi vecino vive en el segundo piso.»</li>
<li>«Mi vecino del segundo piso, cuyo hijo arregla computadoras, me ayudó ayer.»</li></ul>
<p>La segunda no repite <em>vecino</em> tres veces: lo une todo con un <strong>pronombre relativo</strong>. En el GED, muchas preguntas de corrección piden justamente esto: unir ideas con la palabra precisa y la puntuación correcta.</p>
<p>En el Nivel 2 aprendió que una <strong>oración compleja</strong> tiene una <strong>cláusula principal</strong>, que se sostiene sola, y una <strong>cláusula subordinada</strong>, que depende de ella y empieza con una palabra de enlace:</p>
{C.tabla("Cláusula principal y cláusula subordinada", ["Cláusula principal", "Cláusula subordinada"],
         [["No fui a trabajar", "porque estaba enferma."], ["Terminé la tarea", "aunque estaba cansado."], ["El libro … es muy bueno.", "que me prestó"]])}
<p>En esta lección conocerá más palabras de enlace de dos tipos: los <strong>pronombres relativos</strong> (como <em>que</em>), que unen una idea a un sustantivo, y las <strong>conjunciones subordinantes</strong> (como <em>porque</em> o <em>aunque</em>), que unen una idea a todo lo que pasa en la oración principal.</p>
{P("Repaso", "En «Terminé la tarea aunque estaba cansado», ¿cuál es la cláusula que se sostiene sola?", ["aunque estaba cansado", "Terminé la tarea", "estaba cansado"], 1,
   {0: "Empieza con una palabra de enlace: depende de la otra.", 2: "Sola, no dice qué pasó con la tarea; es parte de la subordinada."}, "«Terminé la tarea» tiene sentido completo: es la <strong>cláusula principal</strong>.")}"""

    s2 = f"""<p>Un <strong>pronombre relativo</strong> se refiere a una palabra que ya apareció (su <strong>antecedente</strong>) y la conecta con más información, sin repetirla:</p>
<p class="formula">Compré una lámpara. La lámpara no funciona. → La lámpara <strong>que</strong> compré no funciona.</p>
{C.tabla("Pronombres relativos: uso y ejemplo", ["Relativo", "Se usa para…", "Ejemplo"],
         [["<strong>que</strong>", "Personas o cosas. Es el más común.", "El fuego <strong>que</strong> comenzó en el granero duró dos días."],
          ["<strong>quien, quienes</strong>", "Solo personas. Sobre todo después de una preposición o entre comas.", "La señora a <strong>quien</strong> ayudé me dio las gracias."],
          ["<strong>el cual, la cual, los cuales, las cuales</strong>", "Personas o cosas, casi siempre después de una preposición. Concuerda con el antecedente.", "Esa es la razón por <strong>la cual</strong> renuncié."],
          ["<strong>cuyo, cuya, cuyos, cuyas</strong>", "Posesión: algo que pertenece al antecedente.", "Conocí a un señor <strong>cuya</strong> hija es médica."],
          ["<strong>donde</strong>", "Lugares.", "Esta es la fábrica <strong>donde</strong> trabajo."]])}
{C.caja("ojo", "Cuyo concuerda con lo que se posee", "<p>No concuerda con el dueño: el señor <strong>cuya</strong> hija (con <em>hija</em>), la señora <strong>cuyo</strong> carro (con <em>carro</em>), los vecinos <strong>cuyas</strong> ventanas (con <em>ventanas</em>).</p>")}
{C.caja("ojo", "El error «que su»", "<p>En la conversación se oye mucho «el vecino <s>que su</s> hijo arregla computadoras». En la escritura formal, y en el GED, se escribe «el vecino <strong>cuyo</strong> hijo arregla computadoras». Si ve <em>que su</em>, casi siempre puede cambiarlo por <em>cuyo</em>.</p>")}
{C.caja("ojo", "Quien no sirve para cosas", "<p>«La caja <s>quien</s> llegó» está mal; se dice «la caja <strong>que</strong> llegó». Y recuerde su plural: «mis primos, <strong>quienes</strong> viven en Cicero».</p>")}
{C.caja("tip", "Sin tilde", "<p>Los relativos <em>que, quien, cual, donde</em> no llevan tilde. La tilde aparece solo cuando preguntan o exclaman: «¿<strong>Qué</strong> compró?», «¿<strong>Dónde</strong> trabaja?».</p>")}
{P("Relativo 1", hueco("La señora ___ hija estudia conmigo es enfermera."), ["cuya", "cuyo", "que su"], 0, {1: "Concuerda con lo que se posee: <em>hija</em>.", 2: "«Que su» es de la conversación; en la escritura, <em>cuya</em>."}, "<em>Cuya</em> concuerda con <em>hija</em>.")}
{P("Relativo 2", hueco("Ese es el motivo por ___ renuncié."), ["quien", "el cual", "cual"], 1, {0: "<em>Quien</em> no sirve para cosas.", 2: "Le falta el artículo: <em>el cual</em>."}, "Después de una preposición: <em>por el cual</em>.")}
{P("Relativo 3", hueco("Mis vecinos, ___ llegaron de Puebla, abrieron una panadería."), ["quien", "cuyos", "quienes"], 2, {0: "Son varios vecinos: plural.", 1: "No se habla de algo que pertenezca a los vecinos."}, "Personas en plural, entre comas: <em>quienes</em>.")}"""

    s3 = f"""<p>Una cláusula con relativo puede ir <strong>sin comas</strong> o <strong>entre comas</strong>, y no significa lo mismo:</p>
{C.tabla("La cláusula de relativo sin comas y entre comas", ["Oración", "Qué significa"],
         [["Los empleados que trabajaron el sábado cobrarán extra.", "Solo algunos trabajaron el sábado, y solo esos cobrarán extra. La cláusula <strong>separa</strong> a un grupo del resto."],
          ["Los empleados, que trabajaron el sábado, cobrarán extra.", "Todos los empleados trabajaron el sábado, y todos cobrarán extra. La cláusula solo <strong>añade un dato</strong>."]])}
{C.caja("tip", "La prueba del paréntesis", "<p>Si puede quitar la cláusula y la oración sigue hablando de las mismas personas o cosas, va entre comas. «Mi madre, que vive en Durango, me llama cada domingo.» Usted tiene una sola madre: la cláusula añade un dato, así que va entre comas.</p>")}
{P("Comas 1", "«Los vecinos que tienen perro pagan una cuota extra.» ¿Qué significa?", ["Todos los vecinos tienen perro y pagan.", "Solo pagan los vecinos que tienen perro."], 1, {0: "Sin comas, la cláusula separa a un grupo."}, "Sin comas, la cláusula separa a los que tienen perro del resto.")}
{P("Comas 2", "«Mi hermana, que vive en Houston, es maestra.» ¿Qué significa?", ["Tengo una sola hermana y añado dónde vive.", "Tengo varias hermanas; hablo de la de Houston."], 0, {1: "Las comas indican que solo se añade un dato."}, "Entre comas, la cláusula solo añade un dato.")}"""

    s4 = f"""<p>Las <strong>conjunciones subordinantes</strong> unen una cláusula a la principal y dicen qué relación hay entre las dos. Conviene aprenderlas por grupos, según lo que expresan:</p>
{C.tabla("Conjunciones subordinantes agrupadas por lo que expresan", ["Expresan…", "Conjunciones", "Ejemplo"],
         [["Causa: por qué", "porque, ya que, puesto que, como (al principio)", "<strong>Como</strong> había tráfico, llegué tarde."],
          ["Obstáculo que no impide la acción", "aunque, a pesar de que, si bien", "<strong>A pesar de que</strong> llovía, se jugó el partido."],
          ["Tiempo: cuándo", "cuando, mientras, en cuanto, antes de que, después de que, hasta que", "Esperé <strong>hasta que</strong> me llamaron."],
          ["Condición", "si, siempre que, a menos que, en caso de que", "Puede usar el carro <strong>siempre que</strong> lo devuelva lleno."],
          ["Finalidad: para qué", "para que, a fin de que", "Le dejo la llave <strong>para que</strong> pueda entrar."]])}
{C.caja("ojo", "Las que piden subjuntivo", "<p>Después de <em>para que, antes de que, a menos que</em> y <em>en caso de que</em>, el verbo va siempre en subjuntivo: <strong>para que venga</strong> (no «para que viene»), <strong>antes de que salga</strong>, <strong>a menos que llueva</strong>.</p>")}
{C.caja("ojo", "«Pienso de que…»: sobra el de", "<p>Este error se llama <strong>dequeísmo</strong> y aparece en el GED. Haga la prueba de cambiar la cláusula por <em>eso</em>: «pienso eso» (sin <em>de</em>), así que «pienso <strong>que</strong>…»; pero «estoy seguro de eso», así que «estoy seguro <strong>de que</strong>…».</p>")}
{C.caja("tip", "La coma", "<p>Como en el Nivel 2: si la cláusula subordinada va primero, se separa con coma. «Como había tráfico<strong>,</strong> llegué tarde.»</p>")}
{P("Conjunción 1", hueco("Le dejo la llave ___ pueda entrar."), ["porque", "para que", "si bien"], 1, {0: "No es la causa: es para qué.", 2: "<em>Si bien</em> es un obstáculo."}, "Finalidad: <em>para que</em>, con subjuntivo (<em>pueda</em>).")}
{P("Conjunción 2", hueco("Llegué tarde ___ salí muy temprano."), ["ya que", "para que", "aunque"], 2, {0: "Salir temprano no causa llegar tarde.", 1: "No expresa finalidad."}, "Salir temprano no impidió llegar tarde: obstáculo, <em>aunque</em>.")}
{P("Conjunción 3", hueco("Lea el contrato ___ lo firme."), ["antes de que", "ya que", "aunque"], 0, {1: "No es una causa: es un momento.", 2: "No es un obstáculo."}, "Tiempo: <em>antes de que</em>, con subjuntivo (<em>firme</em>).")}"""

    lect = "".join(f"<p>{p}</p>" for p in LECTURA)
    plano = " ".join(__import__("re").sub("<[^>]+>", "", p) for p in LECTURA)
    s5 = f"""<p>Lea el texto una vez para entenderlo. Después pulse <strong>Mostrar las cláusulas</strong>: verá en negrita los relativos y las conjunciones y, subrayada, cada cláusula subordinada. Para cada una, piense: ¿de qué palabra o de qué idea depende?</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-cl" aria-pressed="false">Mostrar las cláusulas</button></p>
<div class="articulo lectura-cl" id="lect-11"><p><strong>El Gran Incendio de Chicago</strong></p>{lect}</div>
<p class="fuente">Datos: Oficina del Censo de los EE. UU., «History and the Census: 1871 Great Chicago Fire» (census.gov). Consultado en noviembre de 2026.</p>
<script>(function(){{var b=document.getElementById("btn-cl"),t=document.getElementById("lect-11");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las cláusulas":"Mostrar las cláusulas";}});}})();</script>
<h3>¿De qué depende cada cláusula?</h3>
{P("Lectura 1", "«<em>que comenzó en el granero de la familia O’Leary</em>» da información sobre…", ["la calle DeKoven", "el fuego", "la noche del 8 de octubre"], 1, {0: "La calle aparece después, entre comas.", 2: "<em>Que</em> se refiere a un sustantivo que va justo antes."}, "El relativo <em>que</em> se refiere a <em>un fuego</em>: el fuego comenzó en el granero.")}
{P("Lectura 2", "«<em>cuyas orillas estaban llenas de almacenes</em>»: ¿de quién son las orillas?", ["de los almacenes de madera", "del centro de la ciudad", "del río Chicago"], 2, {0: "Los almacenes están en las orillas; no son sus dueños.", 1: "El centro aparece después."}, "<em>Cuyas</em> indica posesión: las orillas del río. Concuerda con <em>orillas</em>.")}
{P("Lectura 3", "«<em>Como el verano había sido muy seco</em>» expresa…", ["un obstáculo que no detuvo el fuego", "la causa de que la madera ardiera", "el momento en que llegó la lluvia"], 1, {0: "Eso lo expresa <em>aunque</em>, en el párrafo 2.", 2: "Eso lo expresa <em>hasta que</em>."}, "<em>Como</em> al principio de la oración expresa causa.")}
{P("Lectura 4", "«<em>la cual todavía se puede visitar</em>» se refiere a…", ["la Torre del Agua", "uno de los edificios destruidos", "la avenida Michigan"], 0, {1: "Habla de algo que todavía existe.", 2: "<em>La cual</em> se refiere a lo que va justo antes de la coma."}, "<em>La cual</em> es femenino singular, como <em>la Torre del Agua</em>.")}
{P("Lectura 5", "«<em>Para que una tragedia así no se repitiera</em>» expresa…", ["la causa de un incendio tan grande", "el momento de la reconstrucción", "la finalidad de las reglas nuevas"], 2, {0: "<em>Para que</em> no expresa causa.", 1: "No dice cuándo."}, "<em>Para que</em> expresa finalidad; por eso el verbo va en subjuntivo: <em>se repitiera</em>.")}"""

    s6 = f"""<p>Una cada par de oraciones en una sola, en su cuaderno, con la palabra de enlace que se pide. No repita el sustantivo y ponga la coma donde haga falta.</p>
<ol><li>Tengo una vecina. Su hijo arregla computadoras. → posesión (<em>cuyo</em>)</li>
<li>Visité la escuela. Allí estudié de niño. → lugar (<em>donde</em>)</li>
<li>Ahorro cada semana. Quiero que mis hijos estudien. → finalidad (<em>para que</em>)</li>
<li>Hacía frío. Salimos a caminar. → obstáculo (<em>aunque</em>, al principio)</li>
<li>El jefe felicitó a Marta. Marta terminó el proyecto a tiempo. → relativo de persona (<em>quien</em>, entre comas)</li></ol>
<details class="transc"><summary>Ver las respuestas</summary><p>Tengo una vecina cuyo hijo arregla computadoras. · Visité la escuela donde estudié de niño. · Ahorro cada semana para que mis hijos estudien. · Aunque hacía frío, salimos a caminar. · El jefe felicitó a Marta, quien terminó el proyecto a tiempo.</p></details>
{P("La mejor unión 1", "«El tráfico era terrible. Llegamos a tiempo.» ¿Cuál es la mejor manera de unirlas?", ["Como el tráfico era terrible, llegamos a tiempo.", "A pesar de que el tráfico era terrible llegamos, a tiempo.", "A pesar de que el tráfico era terrible, llegamos a tiempo."], 2,
   {0: "<em>Como</em> expresa causa: cambia el sentido.", 1: "La coma va después de la cláusula que va primero."}, "Obstáculo, y la coma después de la cláusula que va primero.")}
{P("La mejor unión 2", "«Mis padres viven en Cicero. Vinieron de Jalisco.» ¿Cuál es la mejor manera de unirlas?", ["Mis padres quien vinieron de Jalisco viven en Cicero.", "Mis padres, quienes vinieron de Jalisco, viven en Cicero.", "Mis padres, cuyos vinieron de Jalisco, viven en Cicero."], 1,
   {0: "Son dos personas (plural) y faltan las comas.", 2: "<em>Cuyos</em> indica posesión."}, "Personas en plural, entre comas porque solo se añade un dato.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Uno dice dos oraciones cortas («Tengo un primo. Mi primo maneja un tráiler.») y el otro las une en voz alta con un relativo («Tengo un primo que maneja un tráiler»). Luego cambien de papel.</p>")}"""

    secciones = [("s1", "Repaso: la oración compleja", s1), ("s2", "Los pronombres relativos", s2), ("s3", "Con comas o sin comas: cambia el sentido", s3),
                 ("s4", "Las conjunciones subordinantes", s4), ("s5", "Lectura: «El Gran Incendio de Chicago»", s5), ("s6", "Una con precisión", s6)]
    tarea = [("Tres oraciones complejas.", "Escriba sobre su barrio o su trabajo una oración con <em>que</em>, otra con <em>cuyo</em> (o <em>cuya</em>) y otra con una conjunción subordinante de esta lección. Subraye la cláusula subordinada."),
             ("Corrija.", "Reescriba bien estas oraciones: «La señora que su carro está mal estacionado debe moverlo» · «Le llamo para que me ayuda» · «Pienso de que el examen será fácil» · «La caja quien llegó ayer está rota». "
              "<details class=\"transc\"><summary>Ver las respuestas</summary><p>«La señora cuyo carro está mal estacionado debe moverlo.» · «Le llamo para que me ayude.» · «Pienso que el examen será fácil.» · «La caja que llegó ayer está rota.»</p></details>"),
             ("Con y sin comas.", "Escriba un par de oraciones como las de la <a href=\"#s3\">sección 3</a> (una con comas y otra sin ellas) y explique en una línea qué cambia.")]
    quiz = [
        ("¿Qué relativo se usa <strong>solo para personas</strong>?", ["quien", "cuyo", "donde"], 0, {1: "Indica posesión.", 2: "Indica lugar."}, "<strong>Quien.</strong>"),
        (hueco("Complete: «La mujer ___ carro está mal estacionado debe moverlo.»"), ["cuyo", "cuya", "que su"], 0, {1: "Concuerda con <em>carro</em>, no con <em>mujer</em>.", 2: "Es de la conversación."}, "<strong>Cuyo</strong>, que concuerda con <em>carro</em>."),
        ("¿Cuál oración está bien escrita?", ["El vecino cuyo perro ladra se mudó.", "El vecino que su perro ladra se mudó.", "El vecino quien perro ladra se mudó."], 0, {1: "«Que su» se cambia por <em>cuyo</em>.", 2: "<em>Quien</em> no indica posesión."}, "Con <strong>cuyo</strong>."),
        ("«Los alumnos que aprobaron recibirán un diploma.» ¿Quiénes lo recibirán?", ["Solo los alumnos que aprobaron", "Todos los alumnos, sin excepción", "Los que todavía no aprobaron"], 0, {1: "Sin comas, la cláusula separa a un grupo.", 2: "No."}, "Solo <strong>los que aprobaron</strong>."),
        ("«Los alumnos, que aprobaron, recibirán un diploma.» Las comas indican que…", ["todos los alumnos aprobaron", "solo algunos alumnos aprobaron", "ningún alumno aprobó todavía"], 0, {1: "Eso sería sin comas.", 2: "No."}, "<strong>Todos</strong> aprobaron."),
        (hueco("Complete: «Ese es el banco en ___ abrí mi cuenta.»"), ["el cual", "quien", "cuyo"], 0, {1: "<em>Quien</em> no sirve para cosas.", 2: "No hay posesión."}, "<strong>En el cual.</strong>"),
        ("¿Qué expresa <strong>aunque</strong>?", ["Un obstáculo que no impide la acción", "La causa por la que algo sucede", "El momento en que algo sucede"], 0, {1: "Eso es <em>porque</em>.", 2: "Eso es <em>cuando</em>."}, "Un <strong>obstáculo</strong>."),
        (hueco("Complete: «Le mando el mapa para que no se ___.»"), ["pierda", "pierde", "perdió"], 0, {1: "<em>Para que</em> pide subjuntivo.", 2: "<em>Para que</em> pide subjuntivo."}, "<strong>Pierda</strong> (subjuntivo)."),
        ("¿Qué conjunción expresa <strong>causa</strong>?", ["ya que", "a menos que", "para que"], 0, {1: "Expresa condición.", 2: "Expresa finalidad."}, "<strong>Ya que.</strong>"),
        ("¿Cuál oración está bien escrita?", ["Creo que mañana va a llover.", "Creo de que mañana va a llover.", "Creo que de mañana va a llover."], 0, {1: "Dequeísmo: «creo eso», sin <em>de</em>.", 2: "Sobra el <em>de</em>."}, "<strong>Creo que…</strong>"),
        ("En «El taller donde trabajo cierra a las seis», ¿cuál es la cláusula principal?", ["El taller cierra a las seis", "Trabajo en un taller", "Donde trabajo hasta las seis"], 0, {1: "Esa idea está en la subordinada.", 2: "Empieza con un relativo: es subordinada."}, "<strong>El taller cierra a las seis.</strong>"),
        ("¿Cuál es la mejor manera de unir «Llovía mucho. El partido no se suspendió.»?", ["A pesar de que llovía mucho, el partido no se suspendió.", "Como llovía mucho, el partido no se suspendió por eso.", "Para que lloviera mucho, el partido no se suspendió."], 0, {1: "<em>Como</em> expresa causa: no tiene sentido.", 2: "<em>Para que</em> expresa finalidad: no tiene sentido."}, "Con <strong>a pesar de que</strong>."),
    ]
    filas = [
        ("Relativos", "Elijo que, quien, el cual, cuyo y donde, y evito «que su».", "Dudo con cuyo y el cual.", "Me confundo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Comas", "Sé qué cambia con comas y sin comas.", "A veces lo dudo.", "No veo la diferencia (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Conjunciones", "Elijo la conjunción por su sentido y uso bien el subjuntivo.", "Elijo bien, pero fallo en el verbo.", "Las confundo (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya une ideas con relativos y conjunciones precisas. En la próxima lección trabajará los <strong>tiempos compuestos</strong> y la <strong>forma progresiva</strong>.</p>"
    glosario = [("Antecedente", "La palabra a la que se refiere un pronombre relativo."), ("Pronombre relativo", "Palabra (que, quien, el cual, cuyo, donde) que une una cláusula a un sustantivo."),
                ("Conjunción subordinante", "Palabra (porque, aunque, para que…) que une una cláusula a la principal y dice qué relación hay."),
                ("Dequeísmo", "Poner un «de» que sobra antes de «que»: «pienso de que»."), ("Subjuntivo", "Forma del verbo para lo deseado, posible o no ocurrido: «para que venga».")]
    conexion = ("<p>En la Lección 2.3 del Nivel 2 aprendió a formar oraciones simples, compuestas y complejas. Hoy amplía la oración compleja con nuevas palabras de enlace.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y unos minutos para leer en voz alta.</p>")
    estd = LE.estandares(["L.1.6", "L.1.3"], base=["L.2.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Unir ideas con la palabra precisa y la puntuación correcta.", ["Gramática", "Oraciones complejas"],
                            ["<strong>Usar</strong> los pronombres relativos que, quien, el cual, cuyo y donde.", "<strong>Distinguir</strong> la cláusula de relativo con comas y sin comas.",
                             "<strong>Elegir</strong> la conjunción subordinante según su sentido.", "<strong>Evitar</strong> los errores «que su» y «pienso de que»."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-2", LE.titulo("1-2")), glosario, P)


def practica():
    g = lambda t: f'<p class="frase">{hueco(t)}</p>'
    re_ = [{"enun": g(t), "ops": o, "ok": 0, "pista": "¿Es una persona, una cosa o un lugar? ¿Hay una preposición antes? ¿Se habla de algo que pertenece a alguien?",
            "exp": f"«{t.replace('___', o[0])}» · {e}"} for t, o, e in RE]
    co = [{"enun": f'<p class="frase">{t}</p><p>¿Qué significa?</p>', "ops": o, "ok": 0, "pista": "Fíjese en las comas: ¿la cláusula separa a un grupo o habla de todos?", "exp": e} for t, o, e in CO]
    cj = [{"enun": g(t), "ops": o, "ok": 0, "pista": "Lea la oración con esa conjunción: ¿dice lo que se quiere decir? ¿Suena bien el verbo?",
           "exp": "«" + (lambda x: x[0].upper() + x[1:])(t.replace("___", o[0])) + f"» · {e}"} for t, o, e in CJ]
    un = [{"enun": f'<p class="frase">{t}</p><p>¿Cuál es la mejor manera de unirlas?</p>', "ops": o, "ok": 0,
           "pista": "Esa versión cambia el sentido, usa mal la palabra de enlace o pone mal la coma. Léala en voz alta.", "exp": f"«{o[0]}» · {e}"} for t, o, e in UN]
    mods = [("relativos", "Elija el relativo", C.om("m1", "Complete con el pronombre relativo correcto.")),
            ("comas", "¿Con comas o sin comas?", C.om("m2", "Lea la oración y decida qué significa según sus comas.")),
            ("conjunciones", "Elija la conjunción", C.om("m3", "Complete con la conjunción que da el sentido correcto.")),
            ("union", "La mejor unión", C.om("m4", "Elija la manera de unir las dos oraciones que conserva el sentido y está bien escrita."))]
    js = C.js_datos("RE", re_) + C.js_datos("CO", co) + C.js_datos("CJ", cj) + C.js_datos("UN", un) + 'creaBanco("m1", RE);\ncreaBanco("m2", CO);\ncreaBanco("m3", CJ);\ncreaBanco("m4", UN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
