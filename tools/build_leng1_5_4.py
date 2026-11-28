# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.4 · Seguir instrucciones paso a paso.
Fuente: clases_leng1/clase_5-4.html (GEDparaHispanos) y gramatica/n1-l5-4.html, adaptadas al marco de LearnGED.
Cambio respecto de la fuente: se quitó «Escriba su nombre, su dirección y su teléfono» de la práctica de contar acciones,
porque un solo verbo con tres datos se puede contar como una acción o como tres.
Uso: python3 tools/build_leng1_5_4.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-4"
# (texto con * en las órdenes, explicación)
ORDENES = [("*Lave* las verduras y *córtelas* en trozos pequeños.", "Las órdenes son <strong>lave</strong> y <strong>córtelas</strong>."),
           ("*Escriba* su nombre tal como aparece en su identificación.", "La orden es <strong>escriba</strong>. <em>Aparece</em> no es una orden: dice dónde está el nombre."),
           ("Si siente mareos, *suspenda* el medicamento y *llame* a su médico.", "Las órdenes son <strong>suspenda</strong> y <strong>llame</strong>. <em>Siente</em> dice cuándo hacerlo."),
           ("*Lee* el texto y *elige* la respuesta que mejor lo resume.", "Las órdenes son <strong>lee</strong> y <strong>elige</strong> (de tú). <em>Resume</em> no es una orden."),
           ("*Agite* bien el frasco antes de usarlo.", "La orden es <strong>agite</strong>."),
           ("*Marca* la casilla si tienes hijos menores de cinco años.", "La orden es <strong>marca</strong>. <em>Tienes</em> dice en qué caso marcar."),
           ("*Mantenga* el producto fuera del alcance de los niños.", "La orden es <strong>mantenga</strong>."),
           ("*Precaliente* el horno y *engrase* el molde mientras la mezcla reposa.", "Las órdenes son <strong>precaliente</strong> y <strong>engrase</strong>. <em>Reposa</em> dice lo que hace la mezcla."),
           ("*Complete* todos los campos que tienen un asterisco.", "La orden es <strong>complete</strong>. <em>Tienen</em> no es una orden."),
           ("*Subraya* las palabras que no conoces y *búscalas* en el diccionario.", "Las órdenes son <strong>subraya</strong> y <strong>búscalas</strong>. <em>Conoces</em> no es una orden."),
           ("Cuando el agua hierva, *añada* la sal y *espere* diez minutos.", "Las órdenes son <strong>añada</strong> y <strong>espere</strong>. <em>Hierva</em> dice lo que hace el agua."),
           ("*Presione* el botón verde hasta que la luz se apague.", "La orden es <strong>presione</strong>. <em>Se apague</em> dice lo que hace la luz.")]
NUM = ["Una", "Dos", "Tres", "Cuatro"]
CONTAR = [("Lea el texto.", 0, "lea"), ("Lea el texto y conteste la pregunta.", 1, "lea, conteste"), ("Escriba su nombre, firme y ponga la fecha.", 2, "escriba, firme, ponga"),
          ("Abra la caja, saque el aparato y retire el plástico.", 2, "abra, saque, retire"), ("Tome una pastilla con agua.", 0, "tome"), ("Lave la herida, séquela y cúbrala con una gasa.", 2, "lave, séquela, cúbrala"),
          ("Lee el párrafo y subraya la idea principal.", 1, "lee, subraya"), ("Complete el formulario.", 0, "complete"), ("Encienda el horno, espere diez minutos y meta la bandeja.", 2, "encienda, espere, meta"),
          ("Marque una sola respuesta.", 0, "marque"), ("Identifica al protagonista y describe su conflicto.", 1, "identifica, describe"), ("Agite antes de usar.", 0, "agite"),
          ("Lea las dos cartas, compárelas y escriba en qué se parecen.", 2, "lea, compárelas, escriba"), ("Imprima la página y fírmela.", 1, "imprima, fírmela"),
          ("Desconecte el aparato antes de limpiarlo.", 0, "desconecte"), ("Corte el pollo, sazónelo, póngalo en la bandeja y hornéelo una hora.", 3, "corte, sazónelo, póngalo, hornéelo"),
          ("Llena la solicitud y entrégala en la ventanilla.", 1, "llena, entrégala"), ("Escuche la grabación, tome notas, responda las preguntas y revise sus respuestas.", 3, "escuche, tome, responda, revise"),
          ("Ordene los pasos de la receta.", 0, "ordene")]
# Preguntas con trampa: hay que leer exactamente lo que se pide. (texto, pregunta, respuesta, distractores, explicación)
TRAMPAS = [("Para cuidar las plantas en invierno, riéguelas menos, póngalas cerca de la ventana y no les eche abono.", "¿Qué consejo <strong>no</strong> da el texto?", "Cambiarlas de maceta", ["Regarlas menos", "Ponerlas cerca de la ventana"],
            "El texto no habla de cambiar la maceta. Los otros dos consejos sí aparecen: la pregunta pide el que <strong>no</strong> está."),
           ("La biblioteca abre de lunes a viernes de 9:00 a 6:00 y los sábados de 10:00 a 2:00. Los domingos está cerrada.", "¿Qué día <strong>no</strong> se puede ir a la biblioteca?", "El domingo", ["El sábado", "El lunes"],
            "El domingo está cerrada."),
           ("Tome una pastilla cada ocho horas, con comida. No tome más de tres pastillas en un día.", "¿Cuántas pastillas puede tomar como <strong>máximo</strong> en un día?", "Tres", ["Ocho", "Una"],
            "<strong>Tres</strong>. El ocho son las horas entre una pastilla y otra, no las pastillas."),
           ("Para inscribirse necesita una identificación con foto, un comprobante de domicilio y su número de teléfono.", "¿Qué documento <strong>no</strong> se pide?", "El acta de nacimiento", ["La identificación con foto", "El comprobante de domicilio"],
            "El acta de nacimiento no aparece en la lista."),
           ("Mezcle la harina con el azúcar. Después agregue los huevos de uno en uno. Por último, añada la leche.", "¿Qué se agrega <strong>justo antes</strong> de la leche?", "Los huevos", ["La harina", "El azúcar"],
            "Los huevos se agregan después de la harina y el azúcar, y justo antes de la leche."),
           ("El autobús 9 pasa cada 10 minutos de día y cada 30 minutos después de las 10 de la noche.", "¿Cada cuánto pasa el autobús a las <strong>11 de la noche</strong>?", "Cada 30 minutos", ["Cada 10 minutos", "No pasa"],
            "A las 11 de la noche ya son más de las 10: pasa cada 30 minutos."),
           ("Marque con una X las frutas: manzana, zanahoria, pera, lechuga, uva.", "¿Cuántas palabras hay que marcar?", "Tres", ["Cinco", "Dos"],
            "Solo las frutas: manzana, pera y uva. La zanahoria y la lechuga son verduras."),
           ("Todos los empleados deben usar casco en la obra, excepto en la oficina.", "¿Dónde <strong>no</strong> es obligatorio el casco?", "En la oficina", ["En la obra", "En todas partes"],
            "<strong>Excepto</strong> indica lo que queda fuera de la regla: la oficina.")]


DESAFIO = """<div class="caja desafio" id="desafio">
<p><strong>📝 Lea las cinco instrucciones antes de hacer nada.</strong></p>
<ol><li>Lea todas las instrucciones de este recuadro antes de hacer nada.</li><li>Escriba su nombre en el campo «Nombre».</li><li>Pulse el botón «Aplaudir».</li><li>Pulse el botón «Saltar».</li>
<li>Después de leer las cinco instrucciones, pulse solo el botón «He leído todo» y no haga nada más.</li></ol>
<p><label>Nombre: <input type="text" id="des-nombre" autocomplete="off"></label></p>
<p><button type="button" class="btn-sec" data-des="aplaudir">👏 Aplaudir</button> <button type="button" class="btn-sec" data-des="saltar">🦘 Saltar</button> <button type="button" class="btn" data-des="leido">✅ He leído todo</button></p>
<p class="fb" id="des-fb" aria-live="polite"></p>
<p><button type="button" class="btn-sec" data-des="otra">Volver a empezar</button></p></div>
<script>(function(){var hecho=[],cerrado=false,fb=document.getElementById("des-fb"),nom=document.getElementById("des-nombre");
nom.addEventListener("input",function(){if(!cerrado&&hecho.indexOf("nombre")<0)hecho.push("nombre");});
document.getElementById("desafio").addEventListener("click",function(e){var b=e.target.closest("[data-des]");if(!b)return;var d=b.getAttribute("data-des");
if(d==="otra"){hecho=[];cerrado=false;nom.value="";fb.className="fb";fb.textContent="";return;}if(cerrado)return;
if(d==="leido"){cerrado=true;if(!hecho.length){fb.className="fb bien";fb.innerHTML="✅ <strong>¡Muy bien!</strong> Leyó todo antes de actuar: la última instrucción pedía pulsar solo «He leído todo».";}
else{fb.className="fb mal";fb.innerHTML="Ya había hecho otras cosas antes de llegar al final. La instrucción 5 pedía pulsar <strong>solo</strong> «He leído todo». Por eso el paso 1 del método es leer todo antes de empezar. Pulse «Volver a empezar» si quiere intentarlo otra vez.";}}
else{hecho.push(d);fb.className="fb pista";fb.textContent=(d==="aplaudir"?"👏 ¡Plas, plas!":"🦘 ¡Salto!")+" ¿Ya leyó las cinco instrucciones?";}});})();</script>"""


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Todos los días leemos instrucciones: una receta, las indicaciones del médico, un formulario, la etiqueta de un medicamento, un examen. En el GED, leer bien lo que pide cada pregunta es tan importante como saber la respuesta.</p>
<p>Casi nadie se equivoca por falta de inteligencia, sino por tres razones:</p>
<ul><li><strong>No lee toda la instrucción</strong> antes de empezar: actúa después de la primera línea.</li>
<li><strong>No encuentra los verbos clave</strong>: las palabras que dicen qué hay que hacer.</li>
<li><strong>No comprueba al final</strong> si hizo todo lo que se pedía.</li></ul>
{C.caja("tip", "Idea central", "<p>Leer una instrucción no es como leer una historia. Una instrucción exige precisión: hay que hacer <strong>exactamente</strong> lo que se pide, ni más ni menos.</p>")}"""

    s2 = f"""<h3>El método de los cuatro pasos</h3>
{C.tabla("El método para seguir cualquier instrucción", ["Paso", "Qué hacer"],
         [["1 · Leer todo", "Lea la instrucción completa antes de hacer nada."], ["2 · Pensar", "¿Qué tengo que hacer exactamente? ¿Una cosa o varias?"],
          ["3 · Subrayar los verbos", "Encuentre las órdenes: <em>lea, escriba, marque, seleccione, complete</em>."], ["4 · Comprobar", "Al terminar, revise que hizo todo lo que se pedía. Ni menos, ni más."]])}
<h3>Los verbos de instrucción más frecuentes</h3>
{C.tabla("Verbos de instrucción y lo que piden", ["Verbo", "Qué hay que hacer"],
         [["Lea", "Mirar y comprender el texto completo."], ["Escriba", "Producir un texto con sus palabras."], ["Marque · Seleccione", "Elegir una opción entre varias."],
          ["Complete", "Llenar un espacio en blanco."], ["Identifique", "Reconocer y señalar algo en el texto."], ["Subraye", "Trazar una línea debajo de una palabra o frase."],
          ["Ordene", "Poner en la secuencia correcta."], ["Explique", "Dar las razones o decir cómo funciona algo."]])}
{C.caja("tip", "Usted o tú", "<p>Las instrucciones formales (formularios, medicinas, exámenes) suelen hablar de usted: <em>lea, escriba, marque</em>. Otras hablan de tú: <em>lee, escribe, marca</em>. Significan lo mismo.</p>")}
{C.caja("ojo", "No todos los verbos son órdenes", "<p>En «Cuando el agua <em>hierva</em>, <strong>añada</strong> la sal», <em>hierva</em> dice lo que hace el agua; la orden para usted es <strong>añada</strong>.</p>")}
<h3>Una instrucción como las del GED</h3>
<div class="texto-lectura"><p>Lea el siguiente párrafo. Identifique el argumento principal del autor y seleccione la opción que mejor lo resume.</p></div>
<ul><li><strong>Leer todo:</strong> pide tres acciones, no una.</li><li><strong>Pensar:</strong> primero leer, después identificar el argumento y por último seleccionar.</li>
<li><strong>Subrayar los verbos:</strong> <em>lea, identifique, seleccione</em>.</li><li><strong>Comprobar:</strong> que la opción elegida resuma el argumento principal y no un simple detalle.</li></ul>
{C.caja("ojo", "Cuidado con «no» y «excepto»", "<p>Si la pregunta dice «¿Qué idea <strong>no</strong> menciona el autor?» y usted elige una que sí menciona, falló por leer de prisa. Las palabras <strong>no</strong>, <strong>excepto</strong>, <strong>solo</strong> y <strong>máximo</strong> cambian por completo lo que se pide.</p>")}
{P("Compruebe", "<em>Escriba su nombre, firme y ponga la fecha.</em> ¿Cuántas acciones pide?", NUM[:3], 2, {0: "Hay más de un verbo de orden.", 1: "Cuente otra vez: escriba, firme…"}, "<strong>Tres</strong>: escriba, firme y ponga.")}"""

    s3 = f"""<h3>El desafío de las instrucciones</h3>
<p>Un ejercicio clásico de atención. Antes de tocar cualquier botón o campo, lea el recuadro completo.</p>
{DESAFIO}
{P("Compruebe", "<em>Tome una pastilla cada ocho horas. No tome más de tres en un día.</em> ¿Cuántas pastillas puede tomar como <strong>máximo</strong> en un día?", ["Tres", "Ocho", "Una"], 0,
   {1: "El ocho son las horas entre una pastilla y otra.", 2: "Una es lo que se toma cada vez, no el máximo del día."}, "<strong>Tres</strong>: lo dice la segunda oración.")}"""

    secciones = [("s1", "¿Por qué fallamos al seguir instrucciones?", s1), ("s2", "El método de los cuatro pasos", s2), ("s3", "Práctica: el desafío", s3)]
    tarea = [("Instrucciones de la vida real.", "Busque en su casa tres textos con instrucciones: la caja de un medicamento, una receta, el reverso de un producto de limpieza, un formulario o un manual."),
             ("Analícelas.", "Para cada uno, copie una instrucción tal como aparece, subraye los verbos de orden y escriba cuántas acciones pide y en qué orden."),
             ("La trampa.", "¿Alguna instrucción tiene <em>no</em>, <em>excepto</em>, <em>solo</em> o <em>máximo</em>? Cópiela y explique qué cambia esa palabra.")]
    quiz = [
        ("¿Cuál es el primer paso para seguir una instrucción?", ["Leerla completa antes de hacer nada", "Empezar enseguida", "Preguntar a otra persona"], 0, {1: "Empezar sin leer todo es el error más común.", 2: "Primero hay que leerla."}, "<strong>Leerla completa.</strong>"),
        ("¿Qué son los verbos de instrucción?", ["Las órdenes que dicen qué hay que hacer", "Los nombres de las cosas", "Los adjetivos"], 0, {1: "Esos son sustantivos.", 2: "No."}, "Las <strong>órdenes</strong>: lea, escriba, marque…"),
        ("<em>Si siente mareos, suspenda el medicamento.</em> ¿Cuál es la orden?", ["suspenda", "siente", "mareos"], 0, {1: "Siente dice cuándo.", 2: "Es un sustantivo."}, "<strong>suspenda</strong>."),
        ("<em>Lea el texto y conteste la pregunta.</em> ¿Cuántas acciones pide?", NUM[:3], 1, {0: "Hay dos órdenes.", 2: "Cuente los verbos de orden."}, "<strong>Dos</strong>: lea y conteste."),
        ("¿Qué pide el verbo <strong>complete</strong>?", ["Llenar un espacio en blanco", "Dibujar una línea", "Ordenar pasos"], 0, {1: "Eso es subrayar.", 2: "Eso es ordenar."}, "<strong>Llenar un espacio.</strong>"),
        ("«Lee» y «lea» significan…", ["lo mismo: uno es de tú y otro de usted", "cosas distintas"], 0, {}, "Lo <strong>mismo</strong>."),
        ("¿Qué palabra cambia por completo lo que pide una pregunta?", ["no", "el", "texto"], 0, {1: "Es un artículo.", 2: "No cambia lo que se pide."}, "<strong>No</strong> (y también excepto, solo, máximo)."),
        ("<em>Use casco en la obra, excepto en la oficina.</em> ¿Dónde no hace falta el casco?", ["En la oficina", "En la obra", "En todas partes"], 0, {1: "En la obra sí hace falta.", 2: "Excepto deja fuera solo la oficina."}, "<strong>En la oficina.</strong>"),
        ("¿Qué se hace en el último paso del método?", ["Comprobar que hizo todo lo que se pedía", "Empezar de nuevo", "Leer solo la primera línea"], 0, {1: "No hace falta empezar de nuevo.", 2: "Hay que leer todo."}, "<strong>Comprobar.</strong>"),
        ("En el desafío, ¿qué había que hacer?", ["Pulsar solo «He leído todo»", "Aplaudir y saltar", "Escribir el nombre"], 0, {1: "La instrucción 5 decía que no se hiciera nada más.", 2: "La instrucción 5 decía que no se hiciera nada más."}, "Pulsar <strong>solo «He leído todo»</strong>."),
    ]
    filas = [
        ("Leer todo", "Leo la instrucción completa antes de actuar.", "A veces empiezo antes de terminar de leer.", "Actúo con la primera línea (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Verbos de orden", "Encuentro todas las órdenes y no confundo los demás verbos.", "Se me escapa alguna orden.", "No las distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Palabras trampa", "Me fijo en no, excepto, solo y máximo.", "A veces no las veo.", "No sé qué cambian (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya tiene un método para seguir cualquier instrucción. En la próxima lección verá por qué pasan las cosas: <strong>la causa y el efecto</strong>.</p>"
    glosario = [("Instrucción", "Texto que dice qué hacer y cómo."), ("Verbo de orden (imperativo)", "Verbo que manda hacer algo: lea, escriba, marque."),
                ("Palabra trampa", "Palabra como no, excepto, solo o máximo, que cambia lo que se pide.")]
    conexion = ("<p>En la Lección 5.3 aprendió las palabras que ordenan los hechos. Ahora va a llevar esa destreza a lo más práctico: seguir instrucciones escritas. Leerlas bien protege su tiempo, su salud y sus resultados en el examen.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y tres textos con instrucciones de su casa.</p>")
    estd = LE.estandares(["R.3.1", "R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Hacer exactamente lo que se pide: ni más ni menos.", ["R.3.1 · Secuencia", "R.2.1 · Detalles explícitos"],
                            ["<strong>Aplicar</strong> el método de los cuatro pasos.", "<strong>Encontrar</strong> los verbos de orden de una instrucción.",
                             "<strong>Contar</strong> cuántas acciones pide una instrucción.", "<strong>Reconocer</strong> las palabras que cambian lo que se pide: no, excepto, solo, máximo."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-5", LE.titulo("5-5")), glosario, P)


def practica():
    mar = [{"consigna": "Toque solo los verbos que le dicen al lector qué hacer.", "texto": t, "exp": e} for t, e in ORDENES]
    con = [{"enun": f"<strong>{t}</strong><br>¿Cuántas acciones pide esta instrucción?", "ops": NUM, "ok": k, "enOrden": True, "pista": "Cuente los verbos que son órdenes.",
            "exp": f"Pide <strong>{NUM[k].lower()}</strong>: {v}."} for t, k, v in CONTAR]
    tra = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>{q}", "ops": [ok] + d, "ok": 0, "pista": "Lea la pregunta otra vez, palabra por palabra. ¿Hay un «no», un «excepto» o un «máximo»?", "exp": e}
           for t, q, ok, d, e in TRAMPAS]
    mods = [("ordenes", "Encuentre las órdenes", LE.marcar("m1", "Toque los verbos de orden. Si se equivoca, vuelva a tocar la palabra para quitar la marca. Después pulse <strong>Comprobar</strong>.")),
            ("contar", "¿Cuántas acciones pide?", C.om("m2", "Cuente los verbos de orden.")),
            ("trampas", "Lea exactamente lo que se pide", C.om("m3", "Lea el texto y la pregunta con cuidado: algunas preguntas tienen trampa."))]
    js = C.js_datos("MAR", mar) + C.js_datos("CON", con) + C.js_datos("TRA", tra) + 'creaMarcar("m1", MAR);\ncreaBanco("m2", CON);\ncreaBanco("m3", TRA);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
