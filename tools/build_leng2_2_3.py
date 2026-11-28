# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 2.3 · Oraciones simples, compuestas y complejas.
Fuente: clases_leng2/clase_2-3.html (GEDparaHispanos) y gramatica/n2-l2-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_2_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "2-3"
T = ["Simple", "Compuesta", "Compleja"]
CLASES = [("Mi hija estudia enfermería en Truman College.", 0, "Un solo verbo: <em>estudia</em>."),
          ("Los sábados limpiamos la casa y los domingos descansamos.", 1, "Dos ideas del mismo peso unidas por <em>y</em>."),
          ("Si necesita ayuda, llámeme.", 2, "<em>Si necesita ayuda</em> es una condición que depende de <em>llámeme</em>."),
          ("El supervisor revisó todas las cajas antes de la entrega.", 0, "Un solo verbo: <em>revisó</em>."),
          ("Quería comprar pan, pero la panadería estaba cerrada.", 1, "Contraste con <em>pero</em> entre dos ideas que pueden ir solas."),
          ("Aunque estaba lloviendo, salimos a caminar.", 2, "<em>Aunque estaba lloviendo</em> no tiene sentido sola."),
          ("No vino a la reunión ni avisó.", 1, "Dos ideas negativas unidas por <em>ni</em>."),
          ("Me acosté temprano porque mañana trabajo.", 2, "<em>porque mañana trabajo</em> explica la causa y depende de la otra idea."),
          ("Mañana vamos a visitar a mis suegros.", 0, "Solo <em>vamos</em> está conjugado."),
          ("¿Pagas tú o pago yo?", 1, "Dos opciones unidas por <em>o</em>."),
          ("Cuando sonó el teléfono, yo estaba en la ducha.", 2, "<em>Cuando sonó el teléfono</em> indica el momento y depende de la otra idea."),
          ("El libro que me prestaste es muy interesante.", 2, "<em>que me prestaste</em> depende de <em>el libro</em>."),
          ("Mi abuelo nació en un pueblo pequeño de Guatemala.", 0, "Un solo verbo: <em>nació</em>."),
          ("No pedí sopa, sino que pedí una ensalada.", 1, "<em>sino</em> corrige lo negado: dos ideas del mismo peso."),
          ("Mientras yo cocino, tú pones la mesa.", 2, "<em>Mientras yo cocino</em> indica el tiempo y depende de la otra idea."),
          ("Mi esposo maneja un camión y yo trabajo en una oficina.", 1, "Dos ideas del mismo peso unidas por <em>y</em>.")]
CONEC = [("Me quedé en casa ___ estaba enferma.", ["porque", "aunque", "pero"], "Causa."),
         ("Estaba enferma, ___ fui a trabajar.", ["pero", "porque", "si"], "Contraste."),
         ("___ estaba enferma, fui a trabajar.", ["Aunque", "Porque", "Si"], "Un obstáculo que no impidió la acción."),
         ("___ terminas temprano, vamos al cine.", ["Si", "Sino", "Aunque"], "Condición."),
         ("No es mi hermano, ___ mi primo.", ["sino", "si no", "pero"], "Corrige lo negado."),
         ("___ estudias, no vas a aprobar.", ["Si no", "Sino", "Aunque"], "Condición negativa: <em>si no</em>, separado."),
         ("¿Quieres café ___ té?", ["o", "ni", "pero"], "Dar a elegir."),
         ("No tengo hambre ___ sed.", ["ni", "o", "pero"], "Dos ideas negativas."),
         ("Hablo español ___ inglés.", ["e", "y", "u"], "Antes del sonido <em>i</em>: <em>e</em>."),
         ("Llegaron siete ___ ocho personas.", ["u", "o", "e"], "Antes del sonido <em>o</em>: <em>u</em>."),
         ("Ponga agua ___ hielo en la hielera.", ["y", "e", "u"], "Después de <em>hi</em> viene otra vocal (<em>hie-</em>): se queda la <em>y</em>."),
         ("___ llegué a casa, los niños ya dormían.", ["Cuando", "Aunque", "Sino"], "Tiempo."),
         ("Escucho la radio ___ manejo.", ["mientras", "sino", "ni"], "Dos acciones al mismo tiempo."),
         ("La señora ___ vive al lado es enfermera.", ["que", "porque", "pero"], "<em>que</em> une la idea con <em>la señora</em>."),
         ("Ahorré durante un año ___ quería comprar una computadora.", ["porque", "aunque", "o"], "Causa."),
         ("El examen era difícil, ___ lo aprobé.", ["pero", "porque", "ni"], "Contraste.")]
UNION = [("Hacía mucho calor. Abrí las ventanas.", ["Como hacía mucho calor, abrí las ventanas.", "Hacía mucho calor porque abrí las ventanas.", "Hacía mucho calor, sino abrí las ventanas."], "La causa es el calor."),
         ("Quería ir a la fiesta. Tenía que trabajar.", ["Quería ir a la fiesta, pero tenía que trabajar.", "Quería ir a la fiesta porque tenía que trabajar.", "Quería ir a la fiesta, sino tenía que trabajar."], "Las dos ideas se oponen: <em>pero</em>, con coma."),
         ("Terminé la tarea. Me fui a dormir.", ["Cuando terminé la tarea, me fui a dormir.", "Cuando terminé la tarea me, fui a dormir.", "Aunque terminé la tarea, me fui a dormir."], "Primero una cosa y luego otra: <em>cuando</em>, con coma después."),
         ("Mi hijo no come carne. No come pescado.", ["Mi hijo no come carne ni pescado.", "Mi hijo no come carne, pero pescado.", "Mi hijo no come carne sino pescado."], "Dos ideas negativas: <em>ni</em>."),
         ("Puede pagar en efectivo. Puede pagar con tarjeta.", ["Puede pagar en efectivo o con tarjeta.", "Puede pagar en efectivo ni con tarjeta.", "Puede pagar en efectivo porque con tarjeta."], "Dar a elegir: <em>o</em>."),
         ("Estaba cansado. Siguió trabajando.", ["Aunque estaba cansado, siguió trabajando.", "Porque estaba cansado, siguió trabajando.", "Si estaba cansado, siguió trabajando."], "El cansancio no impidió que siguiera: <em>aunque</em>."),
         ("Estudia todos los días. Aprobará el examen.", ["Si estudia todos los días, aprobará el examen.", "Aunque estudia todos los días, aprobará el examen.", "Estudia todos los días, sino aprobará el examen."], "Una condición y su resultado: <em>si</em>."),
         ("La reunión no es el lunes. Es el martes.", ["La reunión no es el lunes, sino el martes.", "La reunión no es el lunes, si no el martes.", "La reunión no es el lunes porque el martes."], "Se corrige lo negado: <em>sino</em>, junto."),
         ("Compré una lámpara. La lámpara no funciona.", ["La lámpara que compré no funciona.", "La lámpara porque compré no funciona.", "La lámpara, sino compré, no funciona."], "<em>que</em> une la segunda idea con <em>la lámpara</em>."),
         ("Mi esposa cocina. Yo lavo los platos.", ["Mi esposa cocina y yo lavo los platos.", "Mi esposa cocina ni yo lavo los platos.", "Mi esposa cocina sino yo lavo los platos."], "Se suman dos ideas: <em>y</em>."),
         ("Perdí el autobús. Llegué tarde.", ["Llegué tarde porque perdí el autobús.", "Perdí el autobús porque llegué tarde.", "Llegué tarde aunque perdí el autobús."], "La causa es perder el autobús."),
         ("Llueve mucho. El partido se juega.", ["Aunque llueve mucho, el partido se juega.", "Como llueve mucho, el partido se juega.", "Si llueve mucho, el partido no se juega."], "La lluvia no impide el partido: <em>aunque</em>.")]
VA = "El lunes me desperté tarde. La alarma no sonó. Me vestí muy rápido. No desayuné. Salí corriendo. El autobús ya se había ido. Esperé el siguiente. Llegué al trabajo a las nueve y media. Estaba muy nerviosa. Mi supervisora no se enojó. Ella también llegó tarde ese día."
VB = "El lunes me desperté tarde porque la alarma no sonó. Me vestí muy rápido y salí corriendo sin desayunar, pero el autobús ya se había ido. Mientras esperaba el siguiente, pensaba en mi supervisora. Llegué al trabajo a las nueve y media, muy nerviosa. Aunque llegué tarde, ella no se enojó, porque ese día también se le hizo tarde."
VBm = VB.replace("porque la", "<strong>porque</strong> la").replace("rápido y", "rápido <strong>y</strong>").replace("pero el", "<strong>pero</strong> el").replace("Mientras", "<strong>Mientras</strong>").replace("Aunque", "<strong>Aunque</strong>").replace("porque ese", "<strong>porque</strong> ese")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Lea esto: «Me levanté tarde. Perdí el autobús. Llegué tarde al trabajo. Mi jefe no se enojó.» Se entiende, pero suena entrecortado, como un telegrama. Ahora lea esto: «Como me levanté tarde, perdí el autobús y llegué tarde al trabajo, pero mi jefe no se enojó.» Es la misma información, unida con <strong>conectores</strong>. Unir ideas así es una destreza clave para la escritura del GED.</p>
<p>Una <strong>oración simple</strong> tiene un solo verbo conjugado. Puede ser corta o larga, pero expresa una sola acción o un solo estado:</p>
<ul><li><em>Mi hermano trabaja.</em></li><li><em>Mi hermano trabaja todas las noches en un taller de la calle 26.</em></li>
<li><em>Mañana voy a estudiar en la biblioteca.</em> (<em>Voy a estudiar</em> funciona como un solo verbo: solo <em>voy</em> está conjugado).</li></ul>
{C.caja("tip", "Cuente los verbos", "<p>Para saber qué tipo de oración tiene, busque los verbos conjugados: los que dicen quién hace la acción y cuándo. Uno: <strong>simple</strong>. Dos o más: <strong>compuesta</strong> o <strong>compleja</strong>.</p>")}
{P("Compruebe", "<em>Mi abuelo nació en un pueblo pequeño de Guatemala.</em> Esta oración es…", T, 0, {1: "Tiene un solo verbo conjugado.", 2: "Tiene un solo verbo conjugado."}, "<strong>Simple</strong>: un solo verbo, <em>nació</em>.")}"""

    s2 = f"""<p>Una <strong>oración compuesta</strong> une dos oraciones que podrían ir solas, con un conector en medio. Las dos ideas tienen el <strong>mismo peso</strong>.</p>
{C.tabla("Conectores de la oración compuesta", ["Conector", "Sirve para…", "Ejemplo"],
         [["y (e)", "Sumar ideas.", "Mi esposo cocina y yo lavo los platos."], ["o (u)", "Dar a elegir.", "¿Llama usted o llamo yo?"], ["ni", "Sumar dos ideas negativas.", "No llamó ni escribió."],
          ["pero", "Contrastar: la segunda idea va en otra dirección.", "Quería ir, pero llovía."], ["sino", "Corregir algo negado antes.", "No vino el lunes, sino que llegó el martes."]])}
{C.caja("tip", "«y» se vuelve «e», y «o» se vuelve «u»", "<p>Delante del sonido <em>i</em> se escribe <strong>e</strong>: <em>padres e hijos, español e inglés</em>. Delante del sonido <em>o</em> se escribe <strong>u</strong>: <em>siete u ocho, mujer u hombre</em>. Excepción: si después de <em>hi</em> viene otra vocal, se queda la <em>y</em>: <em>agua y hielo</em>.</p>")}
{C.caja("tip", "La coma", "<p>Antes de <strong>pero</strong> y de <strong>sino</strong> va coma: <em>Quería ir, pero llovía.</em> Antes de <em>y, o, ni</em>, normalmente no.</p>")}
{C.caja("ojo", "«sino» o «si no»", "<p><strong>sino</strong>, junto, corrige: <em>No quiero té, sino café.</em> <strong>si no</strong>, separado, es una condición: <em>Si no llueve, iremos al parque.</em></p>")}
{P("Compruebe", "Hablo español ___ inglés.", ["e", "y"], 0, {1: "Delante del sonido i, la y cambia."}, "<strong>e</strong>: español e inglés.")}
{P("Compruebe", "No es mi hermano, ___ mi primo.", ["si no", "sino"], 1, {0: "Aquí no hay condición: se corrige lo negado."}, "<strong>sino</strong>, junto: corrige.")}"""

    s3 = f"""<p>Una <strong>oración compleja</strong> tiene una idea principal y otra que <strong>depende</strong> de ella. La parte que depende empieza con un conector y no tiene sentido completo por sí sola.</p>
{C.tabla("Conectores de la oración compleja", ["Conector", "Indica…", "Ejemplo"],
         [["porque, como", "Causa: por qué.", "No salí porque estaba enferma."], ["aunque", "Un obstáculo que no impide la acción.", "Aunque estaba cansado, terminé la tarea."],
          ["cuando, mientras", "Tiempo: cuándo.", "Cuando llegué, todos dormían."], ["si", "Condición.", "Si estudia cada día, aprobará."], ["que", "Une una idea con otra palabra.", "El libro que me prestó es muy bueno."]])}
{C.caja("tip", "La prueba del fragmento", "<p>Tape la idea principal. Lo que queda, «porque estaba enferma», no se sostiene solo: es un <strong>fragmento</strong>, como vio en el Nivel 1. Por eso esa parte depende de la otra.</p>")}
{C.caja("tip", "La coma", "<p>Si la parte que depende va <strong>primero</strong>, se separa con coma: <em>Cuando llegué, todos dormían.</em> Si va después, normalmente no: <em>Todos dormían cuando llegué.</em></p>")}
{C.caja("tip", "Un dato de gramática", "<p>En los libros de gramática española, estas dos clases se llaman también oraciones compuestas <em>coordinadas</em> (las de la sección 2) y <em>subordinadas</em> (las de esta sección). En el curso usamos <strong>compuesta</strong> y <strong>compleja</strong>, los nombres que verá en los materiales del GED.</p>")}
{P("Compruebe", "<em>Aunque estaba lloviendo, salimos a caminar.</em> Esta oración es…", T, 2, {0: "Tiene dos verbos conjugados.", 1: "«Aunque estaba lloviendo» no puede ir sola."}, "<strong>Compleja</strong>: la parte con <em>aunque</em> depende de la otra.")}
{P("Compruebe", "___ estaba enferma, fui a trabajar.", ["Porque", "Aunque", "Si"], 1, {0: "La enfermedad no fue la causa de ir a trabajar.", 2: "No es una condición."}, "<strong>Aunque</strong>: un obstáculo que no impidió la acción.")}"""

    s4 = f"""<p>Lea en voz alta las dos versiones. Tienen exactamente la misma información. ¿Cuál suena mejor? ¿Por qué? Escriba su respuesta en el cuaderno y marque los conectores de la versión B.</p>
<h3>Versión A · solo oraciones simples</h3>
{LE.escuchar(VA, "Escuchar A")}
<div class="texto-lectura"><p>{VA}</p></div>
<h3>Versión B · con conectores</h3>
{LE.escuchar(VB, "Escuchar B")}
<div class="texto-lectura"><p>{VB}</p></div>
<details class="caja caja-tip"><summary><strong>Ver una respuesta posible</strong></summary>
<p>{VBm}</p>
<p>La versión B se lee con más fluidez y muestra cómo se relacionan las ideas: <em>porque</em> explica la causa, <em>pero</em> marca un problema, <em>mientras</em> une dos momentos y <em>aunque</em> presenta algo que no impidió el resultado. En la versión A, el lector tiene que adivinar esas relaciones.</p>
<p>Ojo: no todo debe unirse. Una oración simple, bien colocada, también es valiosa; lo que se evita es una cadena de oraciones cortas iguales.</p></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · una las ideas</span>
<p>Una cada par de oraciones en una sola. Use el conector que pide la relación indicada y ponga la coma donde haga falta.</p>
<ol><li>Estudio de noche. Trabajo de día. → causa (<em>porque</em>)</li><li>Quería comprar el carro. No tenía el dinero. → contraste (<em>pero</em>)</li>
<li>Llueve. Llevo paraguas. → condición (<em>si</em>, al principio)</li><li>Estaba enfermo. Fue a trabajar. → obstáculo (<em>aunque</em>, al principio)</li>
<li>Mi hija canta. Mi hijo toca la guitarra. → suma (<em>y</em>)</li></ol>
<details><summary><strong>Ver las respuestas</strong></summary><p>Estudio de noche porque trabajo de día. · Quería comprar el carro, pero no tenía el dinero. · Si llueve, llevo paraguas. · Aunque estaba enfermo, fue a trabajar. · Mi hija canta y mi hijo toca la guitarra.</p></details>
<p>Si tiene con quién practicar: uno dice una oración corta («Hoy hace frío») y el otro la continúa con un conector («…pero voy a salir igual»). Cambien el conector cada vez.</p></div>"""

    secciones = [("s1", "La oración simple", s1), ("s2", "La oración compuesta: ideas del mismo peso", s2),
                 ("s3", "La oración compleja: una idea que depende de otra", s3), ("s4", "Lectura comparada: «Una mañana difícil»", s4)]
    tarea = [("Reescriba su rutina.", "Tome el párrafo de su rutina de la Lección 2.2 y reescríbalo uniendo oraciones con al menos cuatro conectores distintos."),
             ("Mis conectores.", "Escriba una oración con cada uno: <em>y, o, pero, sino, porque, aunque, cuando, si</em>. Marque con un color los verbos."),
             ("Las comas.", "Ponga la coma donde falte: «Si tiene tiempo llámeme» · «Quería ir pero no pude» · «Cuando terminé la tarea me acosté»."
              "<details><summary>Ver las respuestas</summary><p>Si tiene tiempo, llámeme. · Quería ir, pero no pude. · Cuando terminé la tarea, me acosté.</p></details>")]
    quiz = [
        ("¿Cuántos verbos conjugados tiene una oración simple?", ["Uno", "Dos", "Tres o más"], 0, {1: "Con dos ya es compuesta o compleja.", 2: "Con dos ya es compuesta o compleja."}, "<strong>Uno.</strong>"),
        ("<em>Los sábados limpiamos la casa y los domingos descansamos.</em><br>¿Qué tipo de oración es?", T, 1, {0: "Tiene dos verbos.", 2: "Las dos ideas pueden ir solas."}, "<strong>Compuesta</strong>: dos ideas del mismo peso con <em>y</em>."),
        ("<em>Me acosté temprano porque mañana trabajo.</em><br>¿Qué tipo de oración es?", T, 2, {0: "Tiene dos verbos.", 1: "«porque mañana trabajo» no puede ir sola."}, "<strong>Compleja</strong>: la causa depende de la idea principal."),
        ("¿Qué conector indica un <strong>contraste</strong>?", ["pero", "porque", "cuando"], 0, {1: "Indica causa.", 2: "Indica tiempo."}, "<strong>pero</strong>."),
        ("Llegaron siete ___ ocho personas.", ["u", "o"], 0, {1: "Delante del sonido o, la o cambia."}, "<strong>u</strong>: siete u ocho."),
        ("___ llueve, no iremos al parque.", ["Si", "Sino"], 0, {1: "Aquí hay una condición."}, "<strong>Si</strong>: condición."),
        ("¿Cuál tiene bien la coma?", ["Cuando llegué, todos dormían.", "Cuando llegué todos, dormían."], 0, {1: "La coma va después de la parte que depende."}, "<strong>Cuando llegué, todos dormían.</strong>"),
        ("¿Cuál tiene bien la coma?", ["Quería ir, pero llovía.", "Quería ir pero, llovía."], 0, {1: "La coma va antes de pero."}, "<strong>Quería ir, pero llovía.</strong>"),
        ("<em>Estaba cansado. Siguió trabajando.</em> La mejor unión:", ["Aunque estaba cansado, siguió trabajando.", "Porque estaba cansado, siguió trabajando.", "Si estaba cansado, siguió trabajando."], 0,
         {1: "El cansancio no fue la causa.", 2: "No es una condición."}, "<strong>Aunque</strong>: el cansancio no lo impidió."),
        ("<em>Perdí el autobús. Llegué tarde.</em> La mejor unión:", ["Llegué tarde porque perdí el autobús.", "Perdí el autobús porque llegué tarde.", "Llegué tarde aunque perdí el autobús."], 0,
         {1: "Eso invierte la causa.", 2: "Perder el autobús sí causó la demora."}, "La causa es <strong>perder el autobús</strong>."),
    ]
    filas = [
        ("Tipos de oración", "Cuento los verbos y digo si la oración es simple, compuesta o compleja.", "Confundo la compuesta con la compleja.", "No sé contar los verbos (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Conectores", "Elijo el conector según la relación: suma, contraste, causa, tiempo, condición.", "Dudo entre aunque y pero, o entre sino y si no.", "Uno todo con «y» (<a href=\"#s2\">repase las secciones 2 y 3</a>)."),
        ("Comas", "Pongo coma antes de pero y sino, y después de la parte que depende cuando va primero.", "A veces olvido la coma.", "No sé dónde va (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 2. Ya sabe unir ideas con fluidez. En el Tema 3 pasará a la <strong>ortografía</strong>: la tilde, las letras que suenan igual y los signos de puntuación.</p>"
    glosario = [("Oración simple", "Tiene un solo verbo conjugado."), ("Oración compuesta", "Une dos ideas del mismo peso con y, o, ni, pero o sino."),
                ("Oración compleja", "Tiene una idea principal y otra que depende de ella (porque, aunque, cuando, si, que)."), ("Conector", "Palabra que une ideas y muestra cómo se relacionan.")]
    conexion = ("<p>En las lecciones 2.1 y 2.2 trabajó con las palabras dentro de la oración. Ahora unirá oraciones enteras. En el Nivel 1 aprendió a evitar los fragmentos; hoy verá cómo una idea que depende de otra se convierte en una oración completa.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y el párrafo de su rutina de la Lección 2.2.</p>")
    estd = LE.estandares(["L.1.6", "L.2.4"], base=["L.2.2", "L.1.9"])
    return C.pagina_leccion(N, LE.titulo(N), "Del telegrama a la prosa: unir ideas con conectores.", ["Gramática", "Tipos de oración"],
                            ["<strong>Reconocer</strong> oraciones simples, compuestas y complejas.", "<strong>Elegir</strong> el conector según la relación entre las ideas.",
                             "<strong>Puntuar</strong> con coma las oraciones compuestas y complejas.", "<strong>Unir</strong> oraciones cortas en una prosa más fluida."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-1", LE.titulo("3-1")), glosario, P)


def practica():
    cl = [{"enun": f"<span class=\"grande\">{o}</span><br>¿Qué tipo de oración es?", "ops": T, "ok": k, "enOrden": True, "pista": "Cuente los verbos conjugados. Si hay dos, ¿pueden ir solas las dos partes?",
           "exp": f"<strong>{T[k]}</strong>. {e}"} for o, k, e in CLASES]
    def may(s): return s[0].upper() + s[1:]
    cx = [{"enun": f"<span class=\"grande\">{o.replace('___', '_____')}</span>", "ops": ops, "ok": 0, "pista": "Lea la oración con ese conector: ¿dice lo que se quiere decir?",
           "exp": f"«{may(o.replace('___', ops[0]))}» · {e}"} for o, ops, e in CONEC]
    un = [{"enun": f"<span class=\"par\">{par}</span><br>¿Cuál es la mejor manera de unirlas?", "ops": ops, "ok": 0, "pista": "Esa versión cambia el sentido o tiene un error de puntuación. Léala en voz alta.",
           "exp": f"«{ops[0]}» · {e}"} for par, ops, e in UNION]
    mods = [("tipos", "¿Simple, compuesta o compleja?", C.om("m1", "Clasifique la oración.")),
            ("conector", "Elija el conector", C.om("m2", "Elija el conector que da el sentido correcto.")),
            ("union", "La mejor unión", C.om("m3", "Dos oraciones cortas y tres maneras de unirlas: elija la que conserva el sentido."))]
    js = C.js_datos("CL", cl) + C.js_datos("CX", cx) + C.js_datos("UN", un) + 'creaBanco("m1", CL);\ncreaBanco("m2", CX);\ncreaBanco("m3", UN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
