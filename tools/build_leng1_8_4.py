# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.4 · Presentación oral breve.
Fuente: clases_leng1/clase_8-4.html (GEDparaHispanos), adaptada al marco de LearnGED (sin práctica en gramatica: se escribió aquí).
Añade un cronómetro para ensayar la presentación de tres minutos.
Uso: python3 tools/build_leng1_8_4.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-4"
PARTES = ["Apertura", "Desarrollo", "Cierre"]
FRASES = [("Buenos días, soy María Pérez. Hoy les voy a contar por qué decidí volver a estudiar.", 0), ("Buenas tardes. Me llamo José y quiero hablarles de mi familia.", 0),
          ("Hola a todos. Mi tema de hoy es cómo llegué a Chicago.", 0), ("Mi primera razón fue darles el ejemplo a mis hijos.", 1),
          ("La segunda idea es que con el GED puedo conseguir un mejor trabajo.", 1), ("Por ejemplo, el año pasado no pude solicitar un puesto porque pedían el diploma.", 1),
          ("Por eso digo siempre: nunca es tarde para estudiar. Muchas gracias.", 2), ("En resumen: vengo de lejos, avanzo paso a paso y voy a ser enfermero. Gracias.", 2),
          ("Si yo puedo, ustedes también pueden. Muchas gracias por escucharme.", 2)]
PROB = ["Volumen muy bajo", "Habla demasiado rápido", "Muchas muletillas", "Lee todo del papel", "No mira al público"]
CASOS = [("Carmen habla tan bajito que los de atrás no la oyen.", 0), ("Por los nervios, Luis dice todo en un minuto y nadie lo sigue.", 1),
         ("Pedro dice «eh… este… o sea…» en casi todas las oraciones.", 2), ("Rosa lee su guion palabra por palabra sin levantar la vista.", 3),
         ("Jorge mira el techo y el suelo todo el tiempo.", 4), ("Ana dice «¿no?» y «¿verdad?» al final de cada frase.", 2),
         ("Marta habla tan rápido que se come las palabras.", 1), ("Raúl se esconde detrás de la hoja y la recita.", 3), ("La voz de Elena casi no se oye desde la tercera fila.", 0),
         ("Carlos mira solo sus zapatos mientras habla.", 4)]
MULE = [("eh…", True), ("este…", True), ("o sea…", True), ("¿no?", True), ("mmm…", True), ("como que…", True), ("bueno…", True),
        ("Por ejemplo", False), ("En resumen", False), ("Primero", False), ("Muchas gracias", False), ("Por eso", False)]

CRONO = """<div class="caja cronometro" id="cronometro">
<p><strong>⏱️ Cronómetro de ensayo</strong> · meta: unos 3 minutos (apertura 30 s, desarrollo 2 min, cierre 30 s)</p>
<p class="crono-num" id="cr-num" aria-live="off">0:00</p>
<p class="crono-fase" id="cr-fase" aria-live="polite">Pulse «Empezar» y diga su presentación.</p>
<p><button type="button" class="btn" data-cr="go">▶️ Empezar</button> <button type="button" class="btn-sec" data-cr="stop">⏸️ Parar</button> <button type="button" class="btn-sec" data-cr="reset">↺ Volver a cero</button></p></div>
<script>(function(){var t0=0,acc=0,id=null,num=document.getElementById("cr-num"),fase=document.getElementById("cr-fase"),caja=document.getElementById("cronometro"),ult="";
function seg(){return acc+(id?(Date.now()-t0)/1000:0);}
function pinta(){var s=Math.floor(seg()),m=Math.floor(s/60),r=s%60;num.textContent=m+":"+(r<10?"0":"")+r;
var f=s<30?"Apertura: salude y anuncie su tema.":s<150?"Desarrollo: sus dos o tres ideas, con ejemplos.":s<180?"Cierre: resuma y dé las gracias.":s<210?"Ya pasó de 3 minutos: vaya cerrando.":"Pasó de 3 minutos y medio: recorte algo en el próximo ensayo.";
if(f!==ult){fase.textContent=f;ult=f;}caja.classList.toggle("crono-largo",s>=210);}
caja.addEventListener("click",function(e){var b=e.target.closest("[data-cr]");if(!b)return;var a=b.getAttribute("data-cr");
if(a==="go"&&!id){t0=Date.now();id=setInterval(pinta,250);}
else if(a==="stop"&&id){acc=seg();clearInterval(id);id=null;pinta();fase.textContent="Duración: "+num.textContent+". "+(seg()<150?"Fue corta: puede añadir un ejemplo.":seg()<=210?"¡Buen tiempo!":"Fue larga: recorte algo.");}
else if(a==="reset"){if(id){clearInterval(id);id=null;}acc=0;ult="";pinta();fase.textContent="Pulse «Empezar» y diga su presentación.";}});})();</script>"""


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En esta lección va a preparar una <strong>presentación oral de unos tres minutos</strong> sobre un tema personal. Será el ensayo del proyecto final (Lección 8.5). Como estudia por su cuenta, su público será su teléfono: se va a grabar, mirar y evaluar con la rúbrica. Si alguien de su casa quiere escucharle, ¡mejor!</p>
{C.caja("tip", "Idea clave", "<p><strong>No se memoriza palabra por palabra.</strong> Se prepara un esquema y se ensaya en voz alta varias veces. Si memoriza todo y los nervios le borran una palabra, se cae el discurso; si domina la estructura, puede cambiar las palabras sin perder el rumbo.</p>")}
{C.tabla("La estructura de cualquier presentación", ["Parte", "Tiempo (de 3 min)", "Qué hacer", "Ejemplo"],
         [["🚀 Apertura", "30 segundos", "Saludar, presentarse y decir el tema. Enganchar al público.", "«Buenos días, soy María Pérez. Hoy les voy a contar por qué decidí volver a estudiar a los cincuenta años.»"],
          ["💡 Desarrollo", "2 minutos", "Dos o tres ideas con ejemplos concretos. Mejor pocas ideas bien explicadas.", "«Mi primera razón fue darles el ejemplo a mis hijos. La segunda, conseguir un mejor trabajo…»"],
          ["🎯 Cierre", "30 segundos", "Resumir en una frase y terminar con una frase memorable o una invitación. Nunca con «bueno… eso es todo».", "«Por eso digo siempre: nunca es tarde para volver a estudiar. Muchas gracias.»"]])}
<h3>Un guion modelo: «Mi historia, mis metas»</h3>
<div class="texto-lectura"><p><strong>🚀 Apertura.</strong> «Buenas tardes a todos. Soy José Martínez. Hoy quiero contarles tres cosas: de dónde vengo, dónde estoy y a dónde quiero llegar.» <em>(Voz firme, mirar al público, pausa de un segundo antes de empezar.)</em></p>
<p><strong>💡 Idea 1.</strong> «Nací en Michoacán, México. Llegué a Chicago a los veinticinco años. Trabajé muchos años en la construcción y nunca pude terminar la escuela.»</p>
<p><strong>💡 Idea 2.</strong> «Hoy estoy en el Nivel 1 de Artes del Lenguaje, preparándome para el GED. Mi familia me apoya. Usar la computadora ha sido un reto, pero ya estudio mis lecciones en línea.»</p>
<p><strong>💡 Idea 3.</strong> «Mi meta es terminar el GED en dos años y entrar al programa de enfermería. Quiero ayudar a otros hispanos que llegan a este país sin conocer el sistema.» <em>(Pausa breve antes de cada idea.)</em></p>
<p><strong>🎯 Cierre.</strong> «En resumen: vengo de lejos, avanzo paso a paso y voy a ser enfermero. Si yo puedo a los cuarenta y siete años, ustedes también pueden. Muchas gracias.»</p></div>
<p>El guion no es un texto seguido: son frases cortas y notas de voz y gesto para mirar si se traba.</p>
{P("Compruebe", "«Por eso digo siempre: nunca es tarde para estudiar. Muchas gracias.» ¿Qué parte es?", PARTES, 2, {0: "No saluda ni anuncia el tema.", 1: "No desarrolla una idea nueva."}, "El <strong>cierre</strong>: resume y agradece.")}"""

    s2 = f"""{C.tabla("Los cuatro aspectos de la voz", ["Aspecto", "Qué es", "Consejo"],
         [["🔊 Volumen", "Qué tan alto se habla.", "Imagine a una persona al fondo del cuarto y háblele a ella, sin gritar."],
          ["⏩ Velocidad", "Qué tan rápido se habla. Los nervios aceleran.", "Haga una pausa de un segundo después de cada idea importante."],
          ["🎵 Modulación", "Los cambios de tono. Una voz siempre igual aburre.", "Diga las palabras clave con un tono un poco más alto y firme."],
          ["⏸️ Pausas", "El silencio bien usado.", "Antes de la idea principal, respire y calle un segundo: el público prestará atención."]])}
<h3>Las muletillas</h3>
<p>Las <strong>muletillas</strong> son palabras o sonidos vacíos que se dicen sin querer mientras se piensa: <em>eh…, este…, mmm…, o sea…, ¿no?, ¿verdad?, como que…, bueno…</em> No aportan nada y comunican inseguridad.</p>
{C.caja("tip", "En vez de «eh…»", "<p>Respire, haga silencio un segundo y siga. El público lee el silencio como reflexión, no como duda.</p>")}
{C.caja("ojo", "Otros ruidos que distraen", "<ul><li><strong>Tics:</strong> tocarse el pelo, jugar con un anillo.</li><li><strong>Mirar el suelo o el techo:</strong> rompe el contacto con el público.</li><li><strong>Leer todo del papel:</strong> el papel es una guía, no un texto para recitar.</li><li><strong>Hablar muy bajo:</strong> el público se cansa y se pierde.</li></ul>")}
{P("Compruebe", "Por los nervios, Luis dice todo en un minuto y nadie lo sigue. ¿Qué debe cuidar?", ["La velocidad", "El volumen", "Las muletillas"], 0, {1: "Sí se le oye: el problema es la prisa.", 2: "No se mencionan muletillas."}, "La <strong>velocidad</strong>: pausas después de cada idea.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · mi guion</span>
<p>Prepare en su cuaderno el guion de una presentación de tres minutos sobre su historia, sus metas, su familia o su trabajo. Frases cortas y notas, no un texto palabra por palabra:</p>
<ol><li><strong>Apertura (30 s):</strong> saludo, nombre y tema.</li><li><strong>Idea 1 (40 s)</strong> con un ejemplo.</li><li><strong>Idea 2 (40 s)</strong> con un ejemplo.</li><li><strong>Idea 3 (40 s)</strong> con un ejemplo.</li><li><strong>Cierre (30 s):</strong> resumen y una frase memorable.</li></ol></div>
<p><strong>Ensaye tres veces en voz alta:</strong> la primera, leyendo; la segunda, mirando solo de reojo; la tercera, sin mirar. Mida el tiempo con este cronómetro.</p>
{CRONO}
{C.tabla("Rúbrica de la presentación", ["Criterio", "4 · Excelente", "3 · Bien", "2 · En camino", "1 · Empezando"],
         [["Estructura", "Apertura, 2 o 3 ideas con ejemplos y cierre claro.", "Tiene las tres partes; un ejemplo flojo.", "Falta una parte.", "No se distinguen las partes."],
          ["Voz", "Se oye bien, a buen ritmo, con pausas.", "Se oye; a veces rápido.", "Muy bajo o muy rápido a ratos.", "Cuesta entender."],
          ["Muletillas y ruidos", "Casi ninguna.", "Algunas.", "Muchas.", "En casi cada frase."],
          ["Contacto y tiempo", "Mira a la cámara o al público; dura de 2½ a 3½ minutos.", "Mira casi siempre; tiempo cercano.", "Lee mucho del papel; tiempo muy corto o largo.", "Lee todo; sin control del tiempo."]])}
<details class="caja caja-tip"><summary><strong>Cómo grabarse con el teléfono</strong></summary>
<ol><li>Apoye el teléfono en algo firme, a la altura de los ojos, en posición horizontal.</li><li>Póngase a un metro y medio, con luz de frente (no de espaldas a la ventana).</li>
<li>Abra la cámara en modo video, respire y empiece con su apertura.</li><li>Mire el video una vez con sonido y otra sin sonido (para ver sus gestos). Califíquese con la rúbrica.</li>
<li>Escriba una cosa que hizo bien y una que va a mejorar. Grábese otra vez.</li></ol></details>"""

    secciones = [("s1", "La estructura del discurso", s1), ("s2", "La voz y las muletillas", s2), ("s3", "Mi guion, mi ensayo y la rúbrica", s3)]
    tarea = [("Mi guion.", "Termine el guion de la sección 3."),
             ("Tres ensayos.", "Ensaye tres veces con el cronómetro: leyendo, mirando de reojo y sin mirar."),
             ("Mi grabación.", "Grábese con el teléfono y califíquese con la rúbrica. Anote su puntaje (de 4 a 16), una cosa que hizo bien y una que va a mejorar. Guarde el video: lo usará en el proyecto final.")]
    quiz = [
        ("¿Conviene memorizar la presentación palabra por palabra?", ["No: se domina la estructura y se ensaya", "Sí, siempre"], 0, {}, "<strong>No</strong>: con los nervios, una palabra olvidada tumba todo."),
        ("¿Cuánto dura la apertura en una presentación de 3 minutos?", ["Unos 30 segundos", "Unos 2 minutos", "Unos 10 minutos"], 0, {1: "Eso es el desarrollo.", 2: "Demasiado."}, "Unos <strong>30 segundos</strong>."),
        ("¿Qué se hace en el desarrollo?", ["Explicar 2 o 3 ideas con ejemplos", "Saludar", "Dar las gracias"], 0, {1: "Eso es la apertura.", 2: "Eso es el cierre."}, "<strong>2 o 3 ideas con ejemplos.</strong>"),
        ("¿Cuál es un mal cierre?", ["«Bueno… eso es todo.»", "«Nunca es tarde para estudiar. Gracias.»"], 0, {}, "<strong>«Bueno… eso es todo»</strong>: es débil."),
        ("¿Qué es una muletilla?", ["Una palabra vacía como «eh…» o «o sea…»", "Una pausa bien usada"], 0, {}, "Una <strong>palabra vacía</strong>."),
        ("¿Qué hacer en vez de decir «eh…»?", ["Respirar y hacer silencio un segundo", "Decir «este…»", "Hablar más rápido"], 0, {1: "También es muletilla.", 2: "Empeora."}, "<strong>Respirar y callar un segundo.</strong>"),
        ("Hablar tan bajo que no se oye es un problema de…", ["volumen", "modulación", "estructura"], 0, {1: "La modulación son los cambios de tono.", 2: "No es de las partes."}, "<strong>Volumen.</strong>"),
        ("¿Para qué sirve una pausa antes de la idea principal?", ["Para que el público preste atención", "Para descansar"], 0, {}, "Para que el público <strong>preste atención</strong>."),
        ("¿Cómo se usa el papel durante la presentación?", ["Como guía para mirar si se traba", "Para leerlo todo"], 0, {}, "Como <strong>guía</strong>."),
        ("¿Cuántas veces conviene ensayar en voz alta?", ["Al menos tres", "Ninguna"], 0, {}, "<strong>Al menos tres.</strong>"),
    ]
    filas = [
        ("Estructura", "Mi guion tiene apertura, 2 o 3 ideas con ejemplos y cierre.", "Le falta un ejemplo o el cierre es flojo.", "No tengo guion (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Voz", "Cuido el volumen, la velocidad, el tono y las pausas.", "Cuido uno o dos aspectos.", "No me fijo en la voz (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Ensayo", "Ensayé tres veces, me grabé y me califiqué.", "Ensayé, pero no me grabé.", "No ensayé (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya tiene su guion y su primer ensayo. En la próxima lección va a armar su <strong>proyecto final: «Mi historia, mis metas»</strong>.</p>"
    glosario = [("Guion", "Esquema de frases cortas y notas para una presentación."), ("Apertura", "Inicio: saludo, nombre y tema."), ("Desarrollo", "Las ideas principales con ejemplos."),
                ("Cierre", "Resumen y frase final."), ("Muletilla", "Palabra o sonido vacío: eh…, este…, o sea…"), ("Modulación", "Los cambios de tono de la voz.")]
    conexion = ("<p>En la Lección 8.3 trabajó con la computadora. Ahora va a preparar una presentación oral breve sobre un tema personal: el ensayo general del proyecto final.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un teléfono para grabarse.</p>")
    estd = LE.estandares([], base=["W.1"], fund=["SL.4", "SL.6"])
    return C.pagina_leccion(N, LE.titulo(N), "Un guion claro, una voz que se oye y un público que no se pierde.", ["Comunicación oral", "Presentación"],
                            ["<strong>Organizar</strong> una presentación en apertura, desarrollo y cierre.", "<strong>Cuidar</strong> el volumen, la velocidad, el tono y las pausas.",
                             "<strong>Evitar</strong> las muletillas y los ruidos que distraen.", "<strong>Ensayar</strong>, grabarse y evaluarse con una rúbrica."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-5", LE.titulo("8-5")), glosario, P)


def practica():
    par = [{"enun": f"<strong>«{f}»</strong><br>¿En qué parte de la presentación va?", "ops": PARTES, "ok": k, "enOrden": True, "pista": "Apertura: saludo y tema. Desarrollo: ideas y ejemplos. Cierre: resumen y gracias.",
            "exp": f"Va en el <strong>{PARTES[k].lower()}</strong>."} for f, k in FRASES]
    dia = [{"enun": f"<div class=\"texto-lectura\"><p>{c}</p></div>¿Cuál es el problema principal?", "ops": PROB, "ok": k, "enOrden": True, "pista": "Piense: ¿se oye? ¿va muy rápido? ¿dice palabras vacías? ¿lee? ¿mira al público?",
            "exp": f"<strong>{PROB[k]}</strong>."} for c, k in CASOS]
    mul = [{"enun": f"<strong class=\"grande\">«{m}»</strong><br>¿Es una muletilla?", "ops": ["Sí: es una muletilla", "No: dice algo útil"], "ok": 0 if v else 1, "enOrden": True, "pista": "",
            "exp": "Es una <strong>muletilla</strong>: no aporta nada; mejor una pausa." if v else "<strong>No es muletilla</strong>: ordena o cierra la presentación."} for m, v in MULE]
    mods = [("partes", "¿Apertura, desarrollo o cierre?", C.om("m1", "Decida en qué parte va cada frase.")),
            ("diagnostico", "Diagnostique el problema", C.om("m2", "Lea el caso y elija el problema principal.")),
            ("muletillas", "¿Muletilla o no?", C.om("m3", "Decida si la palabra es una muletilla."))]
    js = C.js_datos("PAR", par) + C.js_datos("DIA", dia) + C.js_datos("MUL", mul) + 'creaBanco("m1", PAR);\ncreaBanco("m2", DIA);\ncreaBanco("m3", MUL);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
