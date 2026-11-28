# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 1.3 · Corregir fragmentos y oraciones corridas.
Fuente: clases_leng3/clase_1-3.html (GEDparaHispanos) y gramatica/n3-l1-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_1_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "1-3"
T3 = ["Correcta", "Fragmento", "Corrida"]


def F(t):
    return f'<span class="err-f">{t}</span>'


def K(t):
    return f'<span class="err-c">{t}</span>'


CARTA = ["Estimado señor Ramírez:",
         f"Le escribo para informarle sobre la calefacción del apartamento 3B. {F('Desde el lunes pasado.')} {K('El radiador no calienta, mis hijos tienen frío por la noche.')} {K('Llamé dos veces a la oficina nadie contestó.')} {F('Porque el buzón de voz estaba lleno.')}",
         f"El técnico vino el miércoles, revisó el radiador y dijo que faltaba una pieza. {F('Esperando la pieza desde entonces.')} {K('Le pido que resuelva el problema pronto, el pronóstico anuncia temperaturas bajo cero.')}",
         "Atentamente,<br>Lucía Ortega"]
CL = [("Mi primo vende carros usados, gana muy buen dinero.", 2, "Dos oraciones completas unidas solo con una coma."),
      ("Cuando termine mi turno en la fábrica.", 1, "La cláusula con <em>cuando</em> depende de una idea que no está."),
      ("Cerraron la carretera por la nieve; tomamos otro camino.", 0, "El punto y coma separa bien las dos oraciones."),
      ("La señora que vende flores en la esquina de mi casa.", 1, "Tiene un sujeto largo, pero ningún verbo principal: <em>vende</em> está dentro de la cláusula con <em>que</em>."),
      ("El tren se retrasó media hora llegamos tarde al concierto.", 2, "Dos oraciones pegadas sin ningún signo."),
      ("Lavé la ropa, limpié la cocina y preparé la cena.", 0, "Serie de acciones del mismo sujeto, con <em>y</em> antes de la última."),
      ("Buscando un apartamento cerca del trabajo.", 1, "Solo hay un gerundio: falta el verbo conjugado."),
      ("Aunque estaba cansada, terminó el informe.", 0, "La cláusula con <em>aunque</em> va unida a su idea principal."),
      ("El médico me revisó, mañana me dan los resultados.", 2, "Dos oraciones con sujetos distintos unidas solo con una coma."),
      ("Porque el jefe nos pidió quedarnos hasta tarde.", 1, "Una cláusula con <em>porque</em> sola."),
      ("Llegaron.", 0, "Tiene verbo conjugado y el sujeto (<em>ellos</em>) se sobrentiende."),
      ("Después de la tormenta de anoche.", 1, "Una frase de tiempo sin verbo."),
      ("Mi hijo juega fútbol los sábados y mi hija toma clases de piano.", 0, "Dos oraciones unidas por <em>y</em>."),
      ("Tengo que renovar la licencia, se vence el mes que viene.", 2, "Dos oraciones completas unidas solo con una coma. Se puede corregir con <em>porque</em>."),
      ("Para pagar la renta a tiempo.", 1, "Una frase de finalidad sin verbo conjugado."),
      ("No vino a trabajar, pero avisó a tiempo.", 0, "El conector <em>pero</em> separa bien las dos ideas.")]
CO = [("Perdí el autobús, llegué tarde al trabajo.", ["Como perdí el autobús, llegué tarde al trabajo.", "Perdí el autobús, llegué, tarde al trabajo.", "Perdí el autobús llegué tarde al trabajo."], "<em>Como</em> muestra la causa y separa las dos ideas."),
      ("Me encanta esta ciudad. Aunque los inviernos son muy fríos.", ["Me encanta esta ciudad, aunque los inviernos son muy fríos.", "Me encanta esta ciudad aunque. Los inviernos son muy fríos.", "Me encanta esta ciudad, los inviernos son muy fríos."], "El fragmento con <em>aunque</em> se une a la idea principal."),
      ("El restaurante estaba lleno esperamos casi una hora.", ["El restaurante estaba lleno, así que esperamos casi una hora.", "El restaurante estaba lleno, esperamos casi una hora sentados.", "El restaurante, estaba lleno esperamos casi una hora."], "<em>Así que</em> muestra la consecuencia y separa las ideas."),
      ("Los niños del grupo de la tarde.", ["Los niños del grupo de la tarde salen a las cinco.", "Los niños, del grupo de la tarde de los martes.", "Los niños del grupo. De la tarde de los martes."], "Faltaba el verbo conjugado."),
      ("Quería ir a la boda, no conseguí boleto de avión.", ["Quería ir a la boda, pero no conseguí boleto de avión.", "Quería ir a la boda, porque no conseguí boleto de avión.", "Quería ir a la boda no conseguí boleto de avión."], "Las ideas se oponen: <em>pero</em>."),
      ("Trabajando en dos lugares para mantener a mi familia.", ["Estoy trabajando en dos lugares para mantener a mi familia.", "Trabajando, en dos lugares para mantener a mi familia.", "Trabajando en dos lugares. Para mantener a mi familia."], "Se completa con un verbo conjugado: <em>estoy trabajando</em>."),
      ("La tienda abre a las nueve, cierra a las seis.", ["La tienda abre a las nueve y cierra a las seis.", "La tienda abre a las nueve, cierra, a las seis.", "La tienda abre. A las nueve, cierra a las seis."], "Dos acciones del mismo sujeto unidas por <em>y</em>."),
      ("Si llueve mañana. Suspenderemos el picnic.", ["Si llueve mañana, suspenderemos el picnic.", "Si llueve mañana suspenderemos. El picnic.", "Si llueve. Mañana suspenderemos el picnic."], "La condición se une a su resultado, con coma porque va primero."),
      ("Mi vecina es enfermera, trabaja en el hospital del condado.", ["Mi vecina es enfermera; trabaja en el hospital del condado.", "Mi vecina es enfermera, trabaja, en el hospital del condado.", "Mi vecina es enfermera trabaja en el hospital del condado."], "El punto y coma separa dos oraciones muy relacionadas."),
      ("Después de ocho años de trabajo duro. Abrió su propio negocio.", ["Después de ocho años de trabajo duro, abrió su propio negocio.", "Después de ocho años. De trabajo duro abrió su propio negocio.", "Después de ocho años de trabajo, duro abrió su propio negocio."], "La frase de tiempo se une a la oración que le da sentido."),
      ("Ya pagué la factura del gas, falta pagar la de la luz.", ["Ya pagué la factura del gas. Falta pagar la de la luz.", "Ya pagué la factura del gas, falta, pagar la de la luz.", "Ya pagué la factura del gas falta pagar la de la luz."], "Un punto y dos oraciones."),
      ("Estudio por las noches. Porque de día trabajo.", ["Estudio por las noches porque de día trabajo.", "Estudio por las noches, de día trabajo.", "Estudio por las noches. Porque, de día trabajo."], "El fragmento con <em>porque</em> se une a la idea que explica.")]
ED = [(["Mi familia llegó a Chicago en 2015.", "Al principio vivíamos con mis tíos.", "Encontramos un apartamento, nos mudamos en mayo."], 2, "Oración corrida: «Encontramos un apartamento y nos mudamos en mayo.»"),
      (["El sábado hubo una feria de salud en la escuela.", "Ofrecían exámenes gratis de la vista.", "Y vacunas contra la gripe para toda la familia."], 2, "Fragmento sin verbo: se une a la oración anterior: «…exámenes gratis de la vista y vacunas contra la gripe…»."),
      (["Cuando terminé la secundaria.", "Empecé a trabajar en una panadería.", "Allí aprendí a hacer pan dulce."], 0, "Fragmento con <em>cuando</em>: «Cuando terminé la secundaria, empecé a trabajar en una panadería.»"),
      (["El jefe nos reunió a todos el lunes.", "Anunció que la fábrica abriría un segundo turno.", "Necesitan veinte trabajadores más, pagarán un dólar extra por hora."], 2, "Oración corrida: «Necesitan veinte trabajadores más y pagarán un dólar extra por hora.»"),
      (["Mi hija quiere estudiar medicina.", "Porque le gusta ayudar a la gente.", "Este año sacó las mejores notas de su clase."], 1, "Fragmento con <em>porque</em>: «Mi hija quiere estudiar medicina porque le gusta ayudar a la gente.»"),
      (["Revisé el carro antes del viaje.", "Le cambié el aceite, revisé las llantas y llené el tanque.", "Salimos a las seis de la mañana el carro no dio problemas."], 2, "Oración corrida sin ningún signo: «Salimos a las seis de la mañana, y el carro no dio problemas.» La serie del medio es correcta."),
      (["Los precios de la comida subieron este año.", "Muchas familias buscan ofertas.", "Comprando en tiendas más baratas o en mercados al aire libre."], 2, "Fragmento con gerundio: «Compran en tiendas más baratas o en mercados al aire libre.»"),
      (["Mi esposo trabaja de noche.", "Duerme por la mañana, por la tarde cuida a los niños.", "Los fines de semana descansamos juntos."], 1, "Oración corrida: «Duerme por la mañana y por la tarde cuida a los niños.»"),
      (["Para aprobar el examen de manejo.", "Hay que estudiar el manual del estado.", "También conviene practicar con alguien que tenga licencia."], 0, "Fragmento de finalidad: «Para aprobar el examen de manejo, hay que estudiar el manual del estado.»")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En las preguntas de corrección del GED aparece un párrafo con errores y hay que elegir la mejor corrección. Dos errores salen una y otra vez: el <strong>fragmento</strong> («Porque perdí el autobús.») y la <strong>oración corrida</strong> («Perdí el autobús, llegué tarde al trabajo.»). Los dos nacen de lo mismo: al escribir rápido, ponemos el punto donde no va o no lo ponemos donde sí va.</p>
<p>Una <strong>oración completa</strong> necesita tres cosas:</p>
<ul><li>Un <strong>verbo conjugado</strong>, que dice quién hace la acción y cuándo: <em>trabaja, llegaron, había salido</em>.</li>
<li>Un <strong>sujeto</strong>, que puede estar escrito («Mi hermana trabaja») o entenderse por el verbo («Trabajo de noche»: el sujeto es <em>yo</em>).</li>
<li><strong>Sentido completo</strong>: se entiende sola, sin esperar otra idea.</li></ul>
<p>Por eso «Llegaron.» es una oración completa, aunque tenga una sola palabra, y «Los vecinos del segundo piso.» no lo es, aunque tenga cinco.</p>
{C.caja("tip", "Ya lo vio antes", "<p>En el Nivel 1 distinguió la oración del fragmento, y en la Lección 2.3 del Nivel 2 usó la «prueba del fragmento» con las cláusulas que dependen de otra. Aquí lo lleva a párrafos completos.</p>")}
{P("Completa", "¿Por qué «Llegaron.» es una oración completa?", ["Porque empieza con mayúscula y tiene un punto", "Porque tiene un verbo conjugado y el sujeto se entiende", "Porque es tan corta que no puede tener errores"], 1,
   {0: "Un fragmento también empieza con mayúscula y lleva punto.", 2: "La longitud no decide."}, "Verbo conjugado (<em>llegaron</em>) y sujeto que se entiende (<em>ellos</em>).")}"""

    s2 = f"""<p>Un <strong>fragmento</strong> empieza con mayúscula y termina con punto, pero no es una oración completa. Hay tres tipos frecuentes:</p>
{C.tabla("Tipos de fragmento y cómo corregirlos", ["Tipo", "Fragmento", "Corrección"],
         [["Cláusula subordinada sola: empieza con <em>porque, aunque, cuando, si, que…</em>", "Porque perdí el autobús.", "Llegué tarde porque perdí el autobús."],
          ["Sin verbo conjugado: solo un sujeto o una frase de lugar o de tiempo.", "Los trabajadores del turno de noche.", "Los trabajadores del turno de noche cobran más."],
          ["Con gerundio o infinitivo, sin verbo conjugado.", "Esperando noticias del hospital.", "Pasamos la noche esperando noticias del hospital."]])}
{C.caja("tip", "Dos maneras de arreglarlo", "<p><strong>Únalo</strong> a la oración de al lado («Llegué tarde. Porque perdí el autobús.» → «Llegué tarde porque perdí el autobús.») o <strong>complételo</strong> con lo que le falta («Esperando noticias.» → «Estamos esperando noticias.»).</p>")}
{C.caja("tip", "La prueba en voz alta", "<p>Lea el grupo de palabras solo, como si fuera lo único que alguien le dice. Si se queda esperando el resto («¿porque perdió el autobús… qué?»), es un fragmento.</p>")}
{P("Fragmento 1", "¿Cuál es un fragmento?", ["Fuimos a cenar después de la reunión.", "Después de la reunión, fuimos a cenar.", "Después de la reunión de padres."], 2, {0: "Tiene verbo conjugado: <em>fuimos</em>.", 1: "Tiene verbo conjugado: <em>fuimos</em>."}, "Es una frase de tiempo sin verbo conjugado.")}
{P("Fragmento 2", "«Esperando el autobús en la esquina.» ¿Qué le falta?", ["Una coma después de «esperando»", "Un verbo conjugado", "Un punto y coma al final"], 1, {0: "Una coma no le da sentido completo.", 2: "Un signo no le da sentido completo."}, "Le falta un verbo conjugado: «<strong>Estoy</strong> esperando el autobús en la esquina».")}"""

    s3 = f"""<p>Una <strong>oración corrida</strong> es lo contrario de un fragmento: dos oraciones completas pegadas como si fueran una. Aparece de dos formas:</p>
<ul><li><strong>Sin nada entre ellas:</strong> «Llegué tarde el jefe se enojó.»</li>
<li><strong>Unidas solo con una coma:</strong> «Llegué tarde, el jefe se enojó.» La coma no tiene fuerza para separar dos oraciones completas.</li></ul>
{C.tabla("Cuatro maneras de corregir una oración corrida", ["Manera", "Ejemplo"],
         [["1. Punto y mayúscula: dos oraciones.", "Llegué tarde<strong>. E</strong>l jefe se enojó."], ["2. Punto y coma, si las ideas están muy relacionadas.", "Llegué tarde<strong>;</strong> el jefe se enojó."],
          ["3. Un conector de la oración compuesta (<em>y, pero, sino</em>), con su coma si la lleva.", "Llegué tarde <strong>y</strong> el jefe se enojó."],
          ["4. Una conjunción subordinante (Lección 1.1), que muestra la relación.", "<strong>Como</strong> llegué tarde, el jefe se enojó."]])}
{C.caja("tip", "¿Cuál elegir?", "<p>En el GED, la mejor corrección es la que <strong>conserva el sentido</strong>. Si la segunda idea es consecuencia de la primera, una conjunción (<em>como, porque</em>) o <em>y</em> lo muestran mejor que un punto. Si las ideas se oponen, use <em>pero</em>.</p>")}
{C.caja("ojo", "No es corrida", "<p>Una serie de acciones del mismo sujeto, separadas por comas y con <em>y</em> antes de la última: «El técnico vino, revisó el radiador y se fue». Las comas separan los verbos de una enumeración, como en una lista de compras.</p>")}
<p class="fuente">El nombre «oración corrida» viene de los materiales del GED en inglés (<em>run-on sentence</em>); los libros de gramática en español no lo usan. La norma dice lo mismo: la coma no separa dos oraciones independientes; para eso están el punto, el punto y coma o un conector.</p>
{P("Corrida 1", "¿Cuál es una oración corrida?", ["Llovía mucho y la calle se inundó.", "Como llovía mucho, la calle se inundó.", "Llovía mucho, la calle se inundó."], 2, {0: "El conector <em>y</em> une bien las dos ideas.", 1: "<em>Como</em> une bien las dos ideas."}, "Dos oraciones completas unidas solo con una coma.")}
{P("Corrida 2", "¿Cuál corrige mejor «El examen fue difícil, todos aprobaron»?", ["El examen fue difícil, por eso todos aprobaron.", "El examen fue difícil, pero todos aprobaron.", "El examen fue difícil todos aprobaron."], 1, {0: "«Por eso» cambia el sentido: la dificultad no hace aprobar.", 2: "Sigue siendo corrida, ahora sin ningún signo."}, "Las ideas se oponen: <em>pero</em>.")}
<h3>Practique: correcta, fragmento o corrida</h3>
{P("Clasifique 1", "«El autobús llegó tarde, los pasajeros estaban furiosos.»", T3, 2, {0: "¿Cuántas oraciones completas hay? ¿Qué las une?", 1: "Tiene verbos conjugados y sentido completo… dos veces."}, "<strong>Corrida</strong>: dos oraciones completas unidas solo con una coma.")}
{P("Clasifique 2", "«Aunque la tienda abre a las nueve.»", T3, 1, {0: "¿Qué pasa aunque la tienda abra a las nueve?", 2: "Hay una sola cláusula, y depende de otra."}, "<strong>Fragmento</strong>: una cláusula con <em>aunque</em> sola.")}
{P("Clasifique 3", "«Hace mucho frío; póngase el abrigo.»", T3, 0, {1: "Las dos partes tienen verbo y sentido completo.", 2: "El punto y coma sí separa dos oraciones."}, "<strong>Correcta</strong>: el punto y coma separa bien dos oraciones muy relacionadas.")}"""

    carta = "".join(f"<p>{p}</p>" for p in CARTA)
    plano = " ".join(re.sub("<[^>]+>", " ", p) for p in CARTA)
    s4 = f"""<p>Lucía escribió esta carta al administrador de su edificio, pero la envió sin revisarla. Léala con ojos de editor: tiene <strong>tres fragmentos</strong> y <strong>tres oraciones corridas</strong>. Encuéntrelos en su cuaderno y luego pulse <strong>Mostrar los errores</strong> para comprobarlo.</p>
<p>{LE.escuchar(plano, "Escuchar la carta")} <button type="button" class="btn-sec" id="btn-e13" aria-pressed="false">Mostrar los errores</button></p>
<div class="articulo carta-ed" id="carta-13">{carta}</div>
<p class="leyenda-partes" id="ley-13"><span style="background:#fce7f3">Fragmento</span><span style="background:#ffedd5">Oración corrida</span></p>
<p class="fuente">Lucía es un personaje creado para esta lección.</p>
<script>(function(){{var b=document.getElementById("btn-e13"),t=document.getElementById("carta-13"),l=document.getElementById("ley-13");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-err");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar los errores":"Mostrar los errores";}});}})();</script>
{C.caja("tip", "Fíjese", "<p>«El técnico vino el miércoles, revisó el radiador y dijo que faltaba una pieza» <strong>no</strong> es una oración corrida: es una serie de acciones del mismo sujeto, con <em>y</em> antes de la última.</p>")}
<h3>¿Cuál es la mejor corrección?</h3>
{P("Carta 1", "«Desde el lunes pasado. El radiador no calienta, mis hijos tienen frío.»", ["Desde el lunes pasado el radiador. No calienta, mis hijos tienen frío.", "Desde el lunes pasado, el radiador no calienta, y mis hijos tienen frío.", "Desde el lunes, pasado el radiador no calienta mis hijos tienen frío."], 1,
   {0: "Crea otro fragmento.", 2: "La coma está fuera de lugar y sigue habiendo dos oraciones pegadas."}, "El fragmento se une a la oración siguiente, y la coma con <em>y</em> separa las dos ideas.")}
{P("Carta 2", "«Llamé dos veces a la oficina nadie contestó. Porque el buzón de voz estaba lleno.»", ["Llamé dos veces a la oficina, nadie contestó, porque el buzón de voz estaba lleno.", "Llamé dos veces. A la oficina nadie contestó. Porque el buzón de voz estaba lleno.", "Llamé dos veces a la oficina, pero nadie contestó porque el buzón de voz estaba lleno."], 2,
   {0: "Sigue habiendo dos oraciones unidas solo con una coma.", 1: "Sigue el fragmento con <em>porque</em>."}, "<em>Pero</em> corrige la oración corrida, y el fragmento con <em>porque</em> se une a la idea que explica.")}
{P("Carta 3", "«Esperando la pieza desde entonces.»", ["Desde entonces estamos esperando la pieza.", "Esperando, la pieza desde entonces.", "Desde entonces. Esperando la pieza."], 0, {1: "Sigue sin verbo conjugado.", 2: "Ahora son dos fragmentos."}, "Se completa con un verbo conjugado: <em>estamos esperando</em>.")}
{P("Carta 4", "«Le pido que resuelva el problema pronto, el pronóstico anuncia temperaturas bajo cero.»", ["Le pido que resuelva el problema pronto el pronóstico anuncia temperaturas bajo cero.", "Le pido que resuelva el problema pronto, ya que el pronóstico anuncia temperaturas bajo cero.", "Le pido que resuelva el problema pronto, el pronóstico, anuncia temperaturas bajo cero."], 1,
   {0: "Ahora no hay nada entre las dos oraciones.", 2: "Una coma más no corrige nada."}, "<em>Ya que</em> une las dos ideas y muestra la causa de la urgencia.")}
<details class="transc"><summary>Ver la carta corregida</summary>
<p>Estimado señor Ramírez:</p><p>Le escribo para informarle sobre la calefacción del apartamento 3B. Desde el lunes pasado, el radiador no calienta, y mis hijos tienen frío por la noche. Llamé dos veces a la oficina, pero nadie contestó porque el buzón de voz estaba lleno.</p>
<p>El técnico vino el miércoles, revisó el radiador y dijo que faltaba una pieza. Desde entonces estamos esperando la pieza. Le pido que resuelva el problema pronto, ya que el pronóstico anuncia temperaturas bajo cero.</p><p>Atentamente,<br>Lucía Ortega</p>
<p class="fuente">La coma antes de «y mis hijos» separa dos oraciones con sujetos distintos y evita leer «el radiador no calienta y mis hijos» como una sola cosa. Hay otras correcciones válidas; lo importante es que ninguna oración quede incompleta ni pegada a otra solo con una coma.</p></details>
{C.caja("tip", "Si tiene con quién practicar", "<p>Pídale a alguien que le dicte un mensaje corto de varias oraciones, sin decirle dónde van los puntos. Escríbalo y después revisen juntos si quedó algún fragmento o alguna oración corrida.</p>")}"""

    secciones = [("s1", "Repaso: ¿qué es una oración completa?", s1), ("s2", "Los fragmentos", s2), ("s3", "Las oraciones corridas", s3), ("s4", "Editor por un día: «La carta de Lucía»", s4)]
    tarea = [("Revise algo suyo.", "Busque un mensaje o un correo que haya escrito esta semana. Cópielo en su cuaderno y revise cada oración: ¿hay algún fragmento o alguna oración corrida? Corríjalos."),
             ("Corrija de cuatro maneras.", "Corrija «Hoy hay examen, estudié toda la noche» de las cuatro maneras de la <a href=\"#s3\">sección 3</a>. ¿Cuál le parece más clara?"),
             ("Complete los fragmentos.", "Convierta en oraciones completas: «Cuando termine el semestre.» · «Los niños de la escuela de mi barrio.» · «Buscando un trabajo con mejor horario.» "
              "<details class=\"transc\"><summary>Ver respuestas posibles</summary><p>«Hoy hay examen. Estudié toda la noche.» · «Hoy hay examen; estudié toda la noche.» · «Hoy hay examen y estudié toda la noche.» · «Como hoy hay examen, estudié toda la noche.» (La última muestra mejor la relación de causa.)</p>"
              "<p>«Cuando termine el semestre, buscaré otro trabajo.» · «Los niños de la escuela de mi barrio ganaron el concurso.» · «Estoy buscando un trabajo con mejor horario.»</p></details>")]
    quiz = [
        ("¿Qué es un fragmento?", ["Palabras con punto que no forman una idea completa", "Dos oraciones completas unidas con una coma", "Una oración con sujeto, verbo y sentido"], 0, {1: "Esa es la oración corrida.", 2: "Esa es la oración completa."}, "Palabras que <strong>no forman una idea completa</strong>."),
        ("¿Cuál es un fragmento?", ["Después de la reunión de padres.", "Después de la reunión, fuimos a cenar.", "Fuimos a cenar después de la reunión."], 0, {1: "Tiene verbo conjugado.", 2: "Tiene verbo conjugado."}, "Una frase de tiempo <strong>sin verbo</strong>."),
        ("¿Cuál es una oración corrida?", ["Llovía mucho, la calle se inundó.", "Llovía mucho y la calle se inundó.", "Como llovía mucho, la calle se inundó."], 0, {1: "<em>Y</em> une bien.", 2: "<em>Como</em> une bien."}, "Dos oraciones unidas <strong>solo con una coma</strong>."),
        ("¿Cómo se corrige «Porque no tenía dinero.»?", ["No compré el libro porque no tenía dinero.", "Porque no tenía dinero, y no lo compré.", "Porque, no tenía dinero para el libro."], 0, {1: "Mezcla <em>porque</em> y <em>y</em>.", 2: "Sigue siendo un fragmento."}, "Se une a la idea que explica."),
        ("¿Qué signo puede separar dos oraciones completas muy relacionadas?", ["El punto y coma", "La coma sola", "El guion"], 0, {1: "La coma no tiene fuerza para eso.", 2: "No."}, "El <strong>punto y coma</strong>."),
        ("¿Cuál oración está bien escrita?", ["Me levanté, me bañé y salí al trabajo.", "Me levanté me bañé salí al trabajo.", "Me levanté, me bañé, salí, al trabajo."], 0, {1: "Faltan las comas y la <em>y</em>.", 2: "Sobra la última coma y falta la <em>y</em>."}, "Una <strong>serie</strong> de acciones con <em>y</em> antes de la última."),
        ("¿Cuál es una oración corrida sin ningún signo entre las dos ideas?", ["Mi tía cocina muy bien sus tamales son famosos.", "Mi tía cocina muy bien; sus tamales son famosos.", "Mi tía cocina muy bien y sus tamales son famosos."], 0, {1: "El punto y coma separa bien.", 2: "<em>Y</em> une bien."}, "No hay nada entre las dos oraciones."),
        ("¿Cuál corrige mejor «El banco cerró temprano, no pude depositar el cheque»?", ["Como el banco cerró temprano, no pude depositar el cheque.", "El banco cerró temprano, entonces, no pude depositar el cheque.", "El banco, cerró temprano no pude depositar el cheque."], 0, {1: "Siguen unidas solo con comas.", 2: "La coma está mal y siguen pegadas."}, "<strong>Como</strong> muestra la causa."),
        ("¿Cuál es un fragmento?", ["Los vecinos del segundo piso.", "Los vecinos llegaron anoche.", "Llegaron."], 0, {1: "Tiene verbo.", 2: "Tiene verbo y sujeto que se entiende."}, "Tiene sujeto, pero <strong>no tiene verbo</strong>."),
        ("En el GED, la mejor corrección de una oración corrida es la que…", ["conserva el sentido de las dos ideas", "usa siempre un punto y coma", "pone la mayor cantidad de comas"], 0, {1: "No siempre.", 2: "Más comas no corrigen."}, "La que <strong>conserva el sentido</strong>."),
    ]
    filas = [
        ("Fragmentos", "Encuentro los fragmentos y los uno o los completo.", "Los encuentro, pero dudo cómo arreglarlos.", "No los veo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Oraciones corridas", "Las corrijo de cuatro maneras y elijo la que conserva el sentido.", "Uso siempre el punto.", "No las distingo (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Editar", "Reviso un párrafo completo como en el GED.", "Reviso oraciones sueltas.", "Me pierdo en un párrafo (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya encuentra y corrige fragmentos y oraciones corridas. ¡Terminó el Tema 1! En el Tema 2 verá la <strong>puntuación avanzada</strong> y el <strong>vocabulario académico</strong>.</p>"
    glosario = [("Fragmento", "Grupo de palabras con punto que no forma una oración completa."), ("Oración corrida", "Dos oraciones completas pegadas sin nada o solo con una coma."),
                ("Verbo conjugado", "Verbo que dice quién hace la acción y cuándo: trabaja, llegaron."), ("Punto y coma", "Signo (;) que separa dos oraciones completas muy relacionadas.")]
    conexion = ("<p>En las Lecciones 1.1 y 1.2 unió ideas y ordenó acciones. Hoy revisará que cada oración esté completa y separada como debe.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y un mensaje o correo que haya escrito esta semana.</p>")
    estd = LE.estandares(["L.2.2"], base=["L.2.4", "L.1.6"])
    return C.pagina_leccion(N, LE.titulo(N), "Poner el punto donde va.", ["Gramática", "Corrección de oraciones"],
                            ["<strong>Reconocer</strong> las tres partes de una oración completa.", "<strong>Encontrar y corregir</strong> fragmentos.",
                             "<strong>Corregir</strong> oraciones corridas de cuatro maneras.", "<strong>Editar</strong> un párrafo como en el GED."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-1", LE.titulo("2-1")), glosario, P)


def practica():
    cl = [{"enun": f'<p class="frase">{t}</p><p>¿Cómo está escrita?</p>', "ops": T3, "ok": k, "enOrden": True,
           "pista": "¿Hay un verbo conjugado con sentido completo? ¿Hay dos oraciones completas pegadas con una coma o sin nada?", "exp": f"<strong>{T3[k]}.</strong> {e}"} for t, k, e in CL]
    co = [{"enun": f'<p class="frase">{t}</p><p>¿Cuál es la mejor corrección?</p>', "ops": o, "ok": 0, "pista": "Esa versión deja un fragmento, pega dos oraciones con una coma o cambia el sentido.",
           "exp": f"«{o[0]}» · {e}"} for t, o, e in CO]
    ed = [{"enun": f'<p class="frase">{" ".join(p)}</p><p>¿Qué parte tiene un error?</p>', "ops": p, "ok": k, "enOrden": True,
           "pista": "Lea esa parte sola: ¿tiene un verbo conjugado y sentido completo? ¿Son dos oraciones pegadas?", "exp": e} for p, k, e in ED]
    mods = [("clasifique", "Correcta, fragmento o corrida", C.om("m1", "Lea la oración y decida cómo está escrita.")),
            ("correccion", "Elija la corrección", C.om("m2", "Elija la versión que corrige el error y conserva el sentido.")),
            ("editor", "Editor por un día", C.om("m3", "Lea el párrafo y encuentre la parte que tiene el error."))]
    js = C.js_datos("CL", cl) + C.js_datos("CO", co) + C.js_datos("ED", ed) + 'creaBanco("m1", CL);\ncreaBanco("m2", CO);\ncreaBanco("m3", ED);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
